#!/bin/bash
THRESHOLD_DAYS=90

python calc_retention.py --threshold-days $THRESHOLD_DAYS --index sba-issue_raw --since-months 6  > retention_issues_last_6_months.txt
python calc_retention.py --threshold-days $THRESHOLD_DAYS --index sba-issue_raw --since-months 12 > retention_issues_last_12_months.txt
python calc_retention.py --threshold-days $THRESHOLD_DAYS --index sba-issue_raw --since 2014-01-01 > retention_issues_since_beginning_of_project.txt

python calc_retention.py --threshold-days $THRESHOLD_DAYS --index sba-pull_raw --since-months 6  > retention_pull_last_6_months.txt
python calc_retention.py --threshold-days $THRESHOLD_DAYS --index sba-pull_raw --since-months 12 > retention_pull_last_12_months.txt
python calc_retention.py --threshold-days $THRESHOLD_DAYS --index sba-pull_raw --since 2014-01-01 > retention_pull_since_beginning_of_project.txt