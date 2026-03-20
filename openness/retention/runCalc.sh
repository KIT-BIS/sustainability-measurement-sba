#!/bin/bash
THRESHOLD_DAYS=90

python calc_retention.py --threshold-days $THRESHOLD_DAYS --type issue --since-months 6  > retention_issues_last_6_months.txt
python calc_retention.py --threshold-days $THRESHOLD_DAYS --type issue --since-months 12 > retention_issues_last_12_months.txt
python calc_retention.py --threshold-days $THRESHOLD_DAYS --type issue --since 2014-01-01 > retention_issues_since_beginning_of_project.txt

python calc_retention.py --threshold-days $THRESHOLD_DAYS --type pull --since-months 6  > retention_pull_last_6_months.txt
python calc_retention.py --threshold-days $THRESHOLD_DAYS --type pull --since-months 12 > retention_pull_last_12_months.txt
python calc_retention.py --threshold-days $THRESHOLD_DAYS --type pull --since 2014-01-01 > retention_pull_since_beginning_of_project.txt