#!/usr/bin/env python3
"""
GitHub Issue Metrics Extractor

Extracts GitHub issue data between two dates and outputs to Markdown format.
Output includes: title, url, assignee, author, time_to_close, time_to_first_response
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Optional
import requests


def fetch_issues(repo: str, start_date: str, end_date: str, token: str) -> list:
    """Fetch issues from GitHub API between start_date and end_date."""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    search_query = f'repo:{repo} is:issue created:{start_date}..{end_date} -reason:"not planned"'
    url = "https://api.github.com/search/issues"

    all_issues = []
    page = 1
    per_page = 100

    print(f"Search query: {search_query}", file=sys.stderr)

    while True:
        params = {
            "q": search_query,
            "per_page": per_page,
            "page": page,
            "sort": "created",
            "order": "asc"
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error: API request failed with status {response.status_code}", file=sys.stderr)
            print(f"Response: {response.text}", file=sys.stderr)
            sys.exit(1)

        data = response.json()
        total_count = data.get("total_count", 0)
        issues = data.get("items", [])

        print(f"Page {page}: Got {len(issues)} issues (total: {total_count})", file=sys.stderr)

        if not issues:
            break

        all_issues.extend(issues)

        # Check if we've retrieved all results
        if len(all_issues) >= total_count:
            break

        # GitHub Search API only returns first 1000 results
        if page >= 10 or len(all_issues) >= 1000:
            break

        page += 1

    print(f"Total issues fetched: {len(all_issues)}", file=sys.stderr)
    return all_issues


def calculate_time_to_first_response(issue: dict, token: str) -> Optional[str]:
    """Calculate time to first response and return formatted string."""
    created_at = datetime.fromisoformat(issue["created_at"].replace("Z", "+00:00"))

    # Fetch comments and timeline to find first response
    comments_url = issue["comments_url"]
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(comments_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Warning: Failed to fetch comments for issue {issue['number']}: {response.status_code}", file=sys.stderr)
            return None

        comments = response.json()
        if not comments:
            return None

        # Find first comment from someone other than the issue author
        author = issue["user"]["login"]
        for comment in comments:
            if comment["user"]["login"] != author:
                first_response_at = datetime.fromisoformat(comment["created_at"].replace("Z", "+00:00"))
                duration = first_response_at - created_at
                return format_duration(duration)
    except Exception as e:
        print(f"Warning: Error calculating time to first response for issue {issue['number']}: {e}", file=sys.stderr)
        return None

    return None


def calculate_time_to_close(issue: dict) -> Optional[str]:
    """Calculate time to close and return formatted string."""
    if issue["state"] != "closed" or not issue.get("closed_at"):
        return None

    created_at = datetime.fromisoformat(issue["created_at"].replace("Z", "+00:00"))
    closed_at = datetime.fromisoformat(issue["closed_at"].replace("Z", "+00:00"))
    duration = closed_at - created_at
    return format_duration(duration)


def format_duration(duration) -> str:
    """Format timedelta to string like '2 days, 11:19:58'."""
    days = duration.days
    seconds = duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if days > 0:
        return f"{days} day{'s' if days != 1 else ''}, {hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{hours}:{minutes:02d}:{secs:02d}"


def extract_issue_data(issue: dict, token: str) -> dict:
    """Extract required fields from issue."""
    assignee = issue["assignee"]["login"] if issue.get("assignee") else None
    author = issue["user"]["login"]

    time_to_close = calculate_time_to_close(issue)
    time_to_first_response = calculate_time_to_first_response(issue, token)

    return {
        "title": issue["title"],
        "url": issue["html_url"],
        "assignee": assignee,
        "author": author,
        "time_to_close": time_to_close,
        "time_to_first_response": time_to_first_response
    }


def parse_duration_to_seconds(duration_str: Optional[str]) -> Optional[float]:
    """Parse duration string like '2 days, 11:19:58' to total seconds."""
    if not duration_str or duration_str == "None":
        return None

    try:
        total_seconds = 0.0
        parts = duration_str.split(", ")

        # Handle days
        if "day" in parts[0]:
            days = int(parts[0].split()[0])
            total_seconds += days * 86400  # 24 * 60 * 60
            time_part = parts[1] if len(parts) > 1 else "0:0:0"
        else:
            time_part = parts[0]

        # Handle time (HH:MM:SS)
        time_components = time_part.split(":")
        if len(time_components) == 3:
            h, m, s = map(int, time_components)
            total_seconds += h * 3600 + m * 60 + s

        return total_seconds
    except Exception:
        return None


def calculate_statistics(durations: list) -> dict:
    """Calculate average, median, and 90th percentile from duration strings."""
    # Convert to seconds, filter out None values
    seconds_list = [parse_duration_to_seconds(d) for d in durations if d is not None]
    seconds_list = [s for s in seconds_list if s is not None]

    if not seconds_list:
        return {"average": None, "median": None, "percentile_90": None}

    seconds_list.sort()

    # Calculate average
    avg_seconds = sum(seconds_list) / len(seconds_list)

    # Calculate median
    n = len(seconds_list)
    if n % 2 == 0:
        median_seconds = (seconds_list[n//2 - 1] + seconds_list[n//2]) / 2
    else:
        median_seconds = seconds_list[n//2]

    # Calculate 90th percentile
    index_90 = int(n * 0.9)
    if index_90 >= n:
        index_90 = n - 1
    percentile_90_seconds = seconds_list[index_90]

    # Convert back to duration format
    from datetime import timedelta
    return {
        "average": format_duration(timedelta(seconds=avg_seconds)),
        "median": format_duration(timedelta(seconds=median_seconds)),
        "percentile_90": format_duration(timedelta(seconds=percentile_90_seconds))
    }


def write_markdown_report(issues_data: list, repo: str, start_date: str, end_date: str, output_file: str):
    """Write issues data to markdown file in the same format as openness.md."""
    with open(output_file, "w") as f:
        f.write("# Issue Metrics\n\n")

        # Calculate statistics for time to first response and time to close
        time_to_first_response_list = [i["time_to_first_response"] for i in issues_data]
        time_to_close_list = [i["time_to_close"] for i in issues_data]

        stats_first_response = calculate_statistics(time_to_first_response_list)
        stats_close = calculate_statistics(time_to_close_list)

        # Statistics table
        f.write("| Metric | Average | Median | 90th percentile |\n")
        f.write("| --- | --- | --- | ---: |\n")
        f.write(f"| Time to first response | {stats_first_response['average'] or 'None'} | {stats_first_response['median'] or 'None'} | {stats_first_response['percentile_90'] or 'None'} |\n")
        f.write(f"| Time to close | {stats_close['average'] or 'None'} | {stats_close['median'] or 'None'} | {stats_close['percentile_90'] or 'None'} |\n\n")

        # Count statistics
        closed_issues = [i for i in issues_data if i["time_to_close"] is not None]
        open_issues = [i for i in issues_data if i["time_to_close"] is None]

        f.write("| Metric | Count |\n")
        f.write("| --- | ---: |\n")
        f.write(f"| Number of items that remain open | {len(open_issues)} |\n")
        f.write(f"| Number of items closed | {len(closed_issues)} |\n")
        f.write(f"| Total number of items created | {len(issues_data)} |\n\n")

        # Issue details table
        f.write("| Title | URL | Assignee | Author | Time to first response | Time to close |\n")
        f.write("| --- | --- | --- | --- | --- | --- |\n")

        for issue in issues_data:
            assignee = issue["assignee"] if issue["assignee"] else "None"
            author = f"[{issue['author']}](https://github.com/{issue['author']})"
            time_to_first = issue["time_to_first_response"] if issue["time_to_first_response"] else "None"
            time_to_close = issue["time_to_close"] if issue["time_to_close"] else "None"

            f.write(f"| {issue['title']} | {issue['url']} | {assignee} | {author} | {time_to_first} | {time_to_close} |\n")

        f.write("\n")
        f.write(f"Search query used: `repo:{repo} is:issue created:{start_date}..{end_date} -reason:\"not planned\"`\n")


def get_issue_metrics(repo, start_date, end_date, token):
    issues = fetch_issues(repo, start_date, end_date, token)
    issues_data = []
    for i, issue in enumerate(issues, 1):
        issue_data = extract_issue_data(issue, token)
        issues_data.append(issue_data)

    time_to_first_response_list = [i["time_to_first_response"] for i in issues_data]
    time_to_close_list = [i["time_to_close"] for i in issues_data]

    stats_first_response = calculate_statistics(time_to_first_response_list)
    stats_close = calculate_statistics(time_to_close_list)

    return {
        "average_first_response": stats_first_response["average"],
        "median_first_response": stats_first_response["median"],
        "percentile_90_first_response": stats_first_response["percentile_90"],
        "average_close": stats_close["average"],
        "median_close": stats_close["median"],
        "percentile_90_close": stats_close["percentile_90"],
    }

def main():
    parser = argparse.ArgumentParser(
        description="Extract GitHub issue metrics to Markdown format"
    )
    parser.add_argument(
        "--repo",
        required=True,
        help="Repository in format 'owner/repo' (e.g., 'codecentric/spring-boot-admin')"
    )
    parser.add_argument(
        "--start-date",
        required=True,
        help="Start date in YYYY-MM-DD format"
    )
    parser.add_argument(
        "--end-date",
        required=True,
        help="End date in YYYY-MM-DD format"
    )
    parser.add_argument(
        "--output",
        default="openness.md",
        help="Output file path (default: openness.md)"
    )
    parser.add_argument(
        "--token",
        help="GitHub personal access token (or set GITHUB_TOKEN env var)"
    )

    args = parser.parse_args()

    # Get token from args or environment
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GitHub token required. Use --token or set GITHUB_TOKEN env var", file=sys.stderr)
        sys.exit(1)

    # Validate dates
    try:
        datetime.strptime(args.start_date, "%Y-%m-%d")
        datetime.strptime(args.end_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Dates must be in YYYY-MM-DD format", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching issues from {args.repo} created between {args.start_date} and {args.end_date}...")
    issues = fetch_issues(args.repo, args.start_date, args.end_date, token)
    print(f"Found {len(issues)} issues")

    print(f"Processing issues and extracting metrics...")
    issues_data = []
    for i, issue in enumerate(issues, 1):
        print(f"Processing issue {i}/{len(issues)}: {issue['title'][:50]}...", end="\r")
        issue_data = extract_issue_data(issue, token)
        issues_data.append(issue_data)

    print(f"\nWriting markdown report...")
    write_markdown_report(issues_data, args.repo, args.start_date, args.end_date, args.output)
    print(f"Done! Metrics saved to {args.output}")


if __name__ == "__main__":
    main()
