import json
import os
import shutil
import argparse
from datetime import datetime
from playwright.sync_api import sync_playwright


def measure_energy_and_network_traffic(url, time):
    data_path = os.path.join(os.getcwd(), "data")
    if os.path.exists(data_path):
        shutil.rmtree(data_path)
    os.mkdir(data_path)

    profile_path = os.path.join(data_path, "web_profile.json")
    har_path = os.path.join(data_path, "network.har")

    env = os.environ.copy()
    env["MOZ_PROFILER_STARTUP"] = "1"
    env["MOZ_PROFILER_SHUTDOWN"] = profile_path
    env["MOZ_PROFILER_STARTUP_ENTRIES"] = "10000000"
    env["MOZ_PROFILER_STARTUP_FEATURES"] = "js,stackwalk,cpu,power,gpu"

    with sync_playwright() as p:
        browser = p.firefox.launch(
            headless=False,
            env=env,
            firefox_user_prefs={
                "request.performance.power-profiling": True
            }
        )

        context = browser.new_context(
            record_har_path=har_path,
            record_har_content="attach",
            locale="de-DE",
            timezone_id="Europe/Berlin",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            ignore_https_errors=True
        )

        page = context.new_page()

        page.goto(url)
        page.wait_for_timeout(time)

        context.close()
        browser.close()
        network_data = extract_network_data(har_path)
        energy_data = extract_energy_data(profile_path)

    return {
        "network_energy_mwh": network_data,
        "cpu_energy_mwh": energy_data["Power: CPU package"],
        "dram_energy_mwh": energy_data["Power: DRAM"],
        "all": energy_data
    }


def extract_network_data(har_path):
    with open(har_path, "r", encoding="utf-8") as f:
        har = json.load(f)

    total_bytes = 0
    entries = har.get("log", {}).get("entries", [])

    for entry in entries:
        response = entry.get("response", {})
        content = response.get("content", {})

        body_size = content.get("size", 0)
        header_size = response.get("headersSize", 0)

        if body_size > 0:
            total_bytes += body_size
        if header_size > 0:
            total_bytes += header_size

    # Energy factor 0.059
    result = round((total_bytes / 1000000000) * 0.059 * 1000000, 2)
    return result


def extract_energy_data(json_path):
    energy_data = {}
    with open(json_path, encoding="utf-8") as a:
        my_json = json.load(a)
        for node in my_json['counters']:
            if node.get('category') == 'power' or 'power' in node.get('name', '').lower():

                samples = node.get('samples', {})
                values = samples.get('data')

                joule_sum = 0
                prev = 0
                for key, value in values:
                    joule = 0

                    if value > 0:
                        joule = value / 277777777
                    joule_sum += joule
                    prev = key
                energy_data[node.get('name')] = round(joule_sum / 3.6, 2)
    return energy_data


def main():
    parser = argparse.ArgumentParser(description="Measure energy consumption and network traffic of a web page")
    parser.add_argument("--url", type=str, default="http://localhost:8888/wallboard",
                        help="URL to measure (default: http://localhost:8888/wallboard)")
    parser.add_argument("--time", type=int, default=5,
                        help="Time to wait in seconds (default: 5)")
    parser.add_argument("--iterations", type=int, default=1,
                        help="Number of measurement iterations to perform (default: 1)")

    args = parser.parse_args()

    all_results = []

    for i in range(1, args.iterations + 1):
        print(f"\n=== Iteration {i}/{args.iterations} ===")

        result = measure_energy_and_network_traffic(args.url, args.time * 1000)
        result["iteration"] = i
        result["timestamp"] = datetime.now().isoformat()

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"result_{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        print(f"Result written to {filename}")
        print(result)

        all_results.append(result)

    if args.iterations > 1:
        summary_filename = f"summary_{args.iterations}iterations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(summary_filename, "w", encoding="utf-8") as f:
            json.dump({
                "url": args.url,
                "measurement_time_seconds": args.time,
                "total_iterations": args.iterations,
                "results": all_results
            }, f, indent=2)

        print(f"\n=== Summary ===")
        print(f"Summary written to {summary_filename}")

        avg_network = sum(r["network_energy_mwh"] for r in all_results) / len(all_results)
        avg_cpu = sum(r["cpu_energy_mwh"] for r in all_results) / len(all_results)
        print(f"Average network energy: {avg_network:.2f} mWh")
        print(f"Average CPU energy: {avg_cpu:.2f} mWh")


if __name__ == '__main__':
    main()
