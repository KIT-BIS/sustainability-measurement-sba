#!/usr/bin/env python3

import shutil
import sys
import tempfile
from datetime import timedelta
import os
import requests
import zipfile
import io

import readability.calculate_flesch
from consistency import check_consistency
from wcag_conformity import check_wcag
from issue_metrics import extract_issue_metrics
from issue_metrics import extract_pr_metrics

def parse_duration(text: str):
    text = text.strip().lower()
    days = 0

    if "days" in text:
        days_part, time_part = text.split("days, ")
        days = int(days_part.strip())
    else:
        time_part = text

    if time_part.endswith("h"):
        time_part = time_part[:-1]

    parts = list(map(int, time_part.split(":")))

    while len(parts) < 3:
        parts.append(0)

    hours, minutes, seconds = parts

    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

def get_wcag_conformity_score():
    return check_wcag.check_wcag_conformity()*100

def get_documentation_readability_score(temp_dir):
    flesch_score = readability.calculate_flesch.get_flesch_readability_score(temp_dir)
    ideal_flesch_score = 50
    if flesch_score >= ideal_flesch_score:
        return 100

    return 100-((abs(flesch_score-ideal_flesch_score)/ideal_flesch_score)*100)

def get_documentation_consistency_score(temp_dir):
    return (1 - check_consistency.check_consistency(temp_dir)) * 100

def get_maintainer_score():
    token = os.environ.get("GITHUB_TOKEN")

    result_issue = extract_issue_metrics.get_issue_metrics("codecentric/spring-boot-admin", "2025-01-01", "2025-12-31", token)
    ideal_first_response_issue = timedelta(days=7)
    first_response_issue = parse_duration(result_issue["median_first_response"])

    issue_score = 0
    if first_response_issue.days <= ideal_first_response_issue.days:
        issue_score = 100
    else:
       issue_score = (abs(first_response_issue.days - ideal_first_response_issue.days)/ideal_first_response_issue.days) * 100

    result_pr = extract_pr_metrics.get_pr_metrics("codecentric/spring-boot-admin", "2025-01-01", "2025-12-31", token)
    ideal_merge_pr = timedelta(days=14)
    merge_pr = parse_duration(result_pr["median_merge"])

    pr_score = 0
    if merge_pr.days <= ideal_merge_pr.days:
        pr_score = 100
    else:
       pr_score = (abs(merge_pr.days - ideal_merge_pr.days)/ideal_merge_pr.days) * 100

    return (issue_score + pr_score)/2

def main():
    temp_dir = prepare()

    # Documentation quality
    print(f"Documentation Readability Score: {get_documentation_readability_score(temp_dir):.2f}")
    print(f"Documentation Consistency Score: {get_documentation_consistency_score(temp_dir):.2f}")

    # Accessibility
    print(f"WCAG Conformity Score: {get_wcag_conformity_score():.2f}")

    # Openness
    print(f"Maintainer Score: { get_maintainer_score():.2f}")


    clean(temp_dir)


def prepare():
    temp_dir = tempfile.mkdtemp()
    url = "https://github.com/codecentric/spring-boot-admin/archive/refs/tags/4.0.0.zip"
    response = requests.get(url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall(temp_dir)
    else:
        print(f"Failed to download. Status code {response.status_code}")
        sys.exit(1)

    return os.path.join(temp_dir, "spring-boot-admin-4.0.0")

def clean(temp_dir):
    shutil.rmtree(temp_dir)


if __name__ == '__main__':
    main()