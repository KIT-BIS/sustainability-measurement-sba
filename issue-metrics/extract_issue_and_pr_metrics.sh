#!/usr/bin/env bash
YEAR=2019

python3 extract_issue_metrics.py \
  --repo codecentric/spring-boot-admin \
  --start-date "$YEAR"-01-01 \
  --end-date "$YEAR"-12-31 \
  --output issue_metrics."$YEAR".md \
  --token $GITHUB_TOKEN

python3 extract_pr_metrics.py \
  --repo codecentric/spring-boot-admin \
  --start-date "$YEAR"-01-01 \
  --end-date "$YEAR"-12-31 \
  --output pr_metrics."$YEAR".md \
  --token $GITHUB_TOKEN