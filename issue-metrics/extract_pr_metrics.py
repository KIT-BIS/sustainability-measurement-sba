#!/usr/bin/env python3
"""
GitHub Pull Request Metrics Extractor

Extracts GitHub PR data between two dates and outputs to Markdown format.
Output includes: title, url, author, time_to_first_review, time_to_merge, review_comments
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Optional
import requests


# Common bot usernames to filter out
BOT_USERNAMES = {
    'renovate',
    'renovate[bot]',
    'dependabot',
    'dependabot[bot]',
    'github-actions',
    'github-actions[bot]',
    'greenkeeper',
    'greenkeeper[bot]',
    'snyk-bot',
    'mergify',
    'mergify[bot]',
    'codecov',
    'codecov[bot]',
}


def fetch_pull_requests(repo: str, start_date: str, end_date: str, token: str, exclude_bots: bool = True) -> list:
    """Fetch pull requests from GitHub API between start_date and end_date."""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    search_query = f'repo:{repo} is:pr created:{start_date}..{end_date} -is:draft'
    url = "https://api.github.com/search/issues"

    all_prs = []
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
        prs = data.get("items", [])

        print(f"Page {page}: Got {len(prs)} PRs (total: {total_count})", file=sys.stderr)

        if not prs:
            break

        all_prs.extend(prs)

        # Check if we've retrieved all results
        if len(all_prs) >= total_count:
            break

        # GitHub Search API only returns first 1000 results
        if page >= 10 or len(all_prs) >= 1000:
            break

        page += 1

    print(f"Total PRs fetched: {len(all_prs)}", file=sys.stderr)

    # Filter out bot PRs if requested
    if exclude_bots:
        original_count = len(all_prs)
        all_prs = [pr for pr in all_prs if pr["user"]["login"] not in BOT_USERNAMES]
        filtered_count = original_count - len(all_prs)
        if filtered_count > 0:
            print(f"Filtered out {filtered_count} PRs from bots", file=sys.stderr)

    return all_prs


def fetch_pr_details(pr_url: str, token: str) -> Optional[dict]:
    """Fetch detailed PR information from the PR API endpoint."""
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(pr_url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None
        return response.json()
    except Exception as e:
        print(f"Warning: Error fetching PR details: {e}", file=sys.stderr)
        return None


def fetch_pr_reviews(pr: dict, token: str) -> list:
    """Fetch reviews for a pull request."""
    reviews_url = pr["pull_request"]["url"] + "/reviews"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(reviews_url, headers=headers, timeout=10)
        if response.status_code != 200:
            return []
        return response.json()
    except Exception as e:
        print(f"Warning: Error fetching reviews for PR {pr['number']}: {e}", file=sys.stderr)
        return []


def calculate_time_to_first_review(pr: dict, token: str) -> Optional[str]:
    """Calculate time to first review and return formatted string."""
    created_at = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))

    # Fetch reviews and review comments
    reviews = fetch_pr_reviews(pr, token)

    # Also fetch review comments (inline code comments)
    comments_url = pr["pull_request"]["url"] + "/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    review_comments = []
    try:
        response = requests.get(comments_url, headers=headers, timeout=10)
        if response.status_code == 200:
            review_comments = response.json()
    except Exception as e:
        print(f"Warning: Error fetching review comments for PR {pr['number']}: {e}", file=sys.stderr)

    # Also check regular comments
    issue_comments = []
    try:
        response = requests.get(pr["comments_url"], headers=headers, timeout=10)
        if response.status_code == 200:
            issue_comments = response.json()
    except Exception as e:
        print(f"Warning: Error fetching issue comments for PR {pr['number']}: {e}", file=sys.stderr)

    # Find earliest review/comment from someone other than the PR author
    author = pr["user"]["login"]
    earliest_review = None

    # Check reviews
    for review in reviews:
        if review["user"]["login"] != author and review["state"] != "PENDING":
            review_time = datetime.fromisoformat(review["submitted_at"].replace("Z", "+00:00"))
            if earliest_review is None or review_time < earliest_review:
                earliest_review = review_time

    # Check review comments
    for comment in review_comments:
        if comment["user"]["login"] != author:
            comment_time = datetime.fromisoformat(comment["created_at"].replace("Z", "+00:00"))
            if earliest_review is None or comment_time < earliest_review:
                earliest_review = comment_time

    # Check issue comments
    for comment in issue_comments:
        if comment["user"]["login"] != author:
            comment_time = datetime.fromisoformat(comment["created_at"].replace("Z", "+00:00"))
            if earliest_review is None or comment_time < earliest_review:
                earliest_review = comment_time

    if earliest_review:
        duration = earliest_review - created_at
        return format_duration(duration)

    return None


def calculate_time_to_merge(pr: dict) -> Optional[str]:
    """Calculate time to merge and return formatted string."""
    if pr["state"] != "closed" or not pr.get("closed_at"):
        return None

    # Check if PR was actually merged (not just closed)
    if not pr.get("pull_request", {}).get("merged_at"):
        return None

    created_at = datetime.fromisoformat(pr["created_at"].replace("Z", "+00:00"))
    merged_at = datetime.fromisoformat(pr["pull_request"]["merged_at"].replace("Z", "+00:00"))
    duration = merged_at - created_at
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


def extract_pr_data(pr: dict, token: str) -> dict:
    """Extract required fields from pull request."""
    author = pr["user"]["login"]

    time_to_merge = calculate_time_to_merge(pr)
    time_to_first_review = calculate_time_to_first_review(pr, token)

    # Get review comment count
    review_comments = pr.get("comments", 0)

    return {
        "title": pr["title"],
        "url": pr["html_url"],
        "author": author,
        "time_to_first_review": time_to_first_review,
        "time_to_merge": time_to_merge,
        "review_comments": review_comments,
        "state": pr["state"]
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


def write_markdown_report(prs_data: list, repo: str, start_date: str, end_date: str, output_file: str, bots_excluded: bool = True):
    """Write PR data to markdown file."""
    with open(output_file, "w") as f:
        f.write("# Pull Request Metrics\n\n")

        # Calculate statistics for time to first review and time to merge
        time_to_first_review_list = [pr["time_to_first_review"] for pr in prs_data]
        time_to_merge_list = [pr["time_to_merge"] for pr in prs_data]

        stats_first_review = calculate_statistics(time_to_first_review_list)
        stats_merge = calculate_statistics(time_to_merge_list)

        # Statistics table
        f.write("| Metric | Average | Median | 90th percentile |\n")
        f.write("| --- | --- | --- | ---: |\n")
        f.write(f"| Time to first review | {stats_first_review['average'] or 'None'} | {stats_first_review['median'] or 'None'} | {stats_first_review['percentile_90'] or 'None'} |\n")
        f.write(f"| Time to merge | {stats_merge['average'] or 'None'} | {stats_merge['median'] or 'None'} | {stats_merge['percentile_90'] or 'None'} |\n\n")

        # Count statistics
        merged_prs = [pr for pr in prs_data if pr["time_to_merge"] is not None]
        open_prs = [pr for pr in prs_data if pr["state"] == "open"]
        closed_not_merged = [pr for pr in prs_data if pr["state"] == "closed" and pr["time_to_merge"] is None]

        f.write("| Metric | Count |\n")
        f.write("| --- | ---: |\n")
        f.write(f"| Number of PRs that remain open | {len(open_prs)} |\n")
        f.write(f"| Number of PRs merged | {len(merged_prs)} |\n")
        f.write(f"| Number of PRs closed (not merged) | {len(closed_not_merged)} |\n")
        f.write(f"| Total number of PRs created | {len(prs_data)} |\n\n")

        # PR details table
        f.write("| Title | URL | Author | Time to first review | Time to merge | Comments |\n")
        f.write("| --- | --- | --- | --- | --- | ---: |\n")

        for pr in prs_data:
            author = f"[{pr['author']}](https://github.com/{pr['author']})"
            time_to_first = pr["time_to_first_review"] if pr["time_to_first_review"] else "None"
            time_to_merge = pr["time_to_merge"] if pr["time_to_merge"] else "None"

            f.write(f"| {pr['title']} | {pr['url']} | {author} | {time_to_first} | {time_to_merge} | {pr['review_comments']} |\n")

        f.write("\n")
        f.write(f"Search query used: `repo:{repo} is:pr created:{start_date}..{end_date} -is:draft`\n")
        if bots_excluded:
            f.write(f"\nNote: PRs from bots (renovate, dependabot, github-actions, etc.) are excluded from this report.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Extract GitHub pull request metrics to Markdown format"
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
        default="pr_metrics.md",
        help="Output file path (default: pr_metrics.md)"
    )
    parser.add_argument(
        "--token",
        help="GitHub personal access token (or set GITHUB_TOKEN env var)"
    )
    parser.add_argument(
        "--include-bots",
        action="store_true",
        help="Include PRs from bots (renovate, dependabot, etc.) - by default they are excluded"
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

    print(f"Fetching pull requests from {args.repo} created between {args.start_date} and {args.end_date}...")
    exclude_bots = not args.include_bots
    prs = fetch_pull_requests(args.repo, args.start_date, args.end_date, token, exclude_bots)
    print(f"Found {len(prs)} pull requests")

    print(f"Processing pull requests and extracting metrics...")
    prs_data = []
    for i, pr in enumerate(prs, 1):
        print(f"Processing PR {i}/{len(prs)}: {pr['title'][:50]}...", end="\r")
        pr_data = extract_pr_data(pr, token)
        prs_data.append(pr_data)

    print(f"\nWriting markdown report...")
    write_markdown_report(prs_data, args.repo, args.start_date, args.end_date, args.output, exclude_bots)
    print(f"Done! Metrics saved to {args.output}")


if __name__ == "__main__":
    main()
