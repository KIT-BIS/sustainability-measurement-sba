# GitHub Issue Metrics Extractor

A Python script to extract and analyze GitHub issue metrics between specified dates.

## Features

- Fetches issues from a GitHub repository within a date range
- Calculates time to first response and time to close
- Generates statistical summaries (average, median, 90th percentile)
- Outputs formatted Markdown reports

## Requirements

- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests
```

## Setup

Create a GitHub Personal Access Token:
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate a new token with `repo` scope
3. Set it as an environment variable:
   ```bash
   export GITHUB_TOKEN="your_token_here"
   ```

## Usage

```bash
./extract_issue_metrics.py --repo OWNER/REPO --start-date YYYY-MM-DD --end-date YYYY-MM-DD [--output FILE]
```

### Required Arguments

- `--repo`: Repository in format `owner/repo` (e.g., `codecentric/spring-boot-admin`)
- `--start-date`: Start date in `YYYY-MM-DD` format
- `--end-date`: End date in `YYYY-MM-DD` format

### Optional Arguments

- `--output`: Output file path (default: `issue_metrics.md`)
- `--token`: GitHub token (overrides `GITHUB_TOKEN` environment variable)

## Example

```bash
./extract_issue_metrics.py \
  --repo codecentric/spring-boot-admin \
  --start-date 2024-01-01 \
  --end-date 2024-12-31 \
  --output issue_metrics.2024.md
```

## Output

The script generates a Markdown file containing:
- Summary statistics for time to first response and time to close
- Count of open vs closed issues
- Detailed table with all issues and their metrics

### Sample Output

```markdown
# Issue Metrics

| Metric | Average | Median | 90th percentile |
| --- | --- | --- | ---: |
| Time to first response | 1 day, 5:30:00 | 12:45:00 | 3 days, 2:15:00 |
| Time to close | 5 days, 3:20:00 | 3 days, 1:10:00 | 12 days, 6:30:00 |

| Metric | Count |
| --- | ---: |
| Number of items that remain open | 15 |
| Number of items closed | 85 |
| Total number of items created | 100 |
```

## Notes

- The script excludes issues closed as "not planned"
- GitHub Search API returns a maximum of 1000 results
- Rate limits apply based on your GitHub token's permissions
