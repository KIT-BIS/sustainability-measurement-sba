#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
THRESHOLD_DAYS="${THRESHOLD_DAYS:-90}"
START_DATE="2014-01-01"
WINDOW_MONTHS=6
RESULT_FILE="${SCRIPT_DIR}/retention_issues_6_month_clusters.csv"

current_end="$(date +%F)"
rows=()

printf "since;until;total;active;active_pct;leaving;leaving_pct;repeat_contribs\n" > "$RESULT_FILE"

while :; do
  current_start="$(date -j -v-"${WINDOW_MONTHS}"m -f "%Y-%m-%d" "$current_end" +%F)"

  if [[ "$current_end" < "$START_DATE" ]]; then
    break
  fi

  if [[ "$current_start" < "$START_DATE" ]]; then
    current_start="$START_DATE"
  fi

  row="$(python "${SCRIPT_DIR}/calc_retention.py" \
    --threshold-days "$THRESHOLD_DAYS" \
    --type issue \
    --since "$current_start" \
    --now "$current_end" \
    --summary-line)"
  rows+=("$row")

  if [[ "$current_start" == "$START_DATE" ]]; then
    break
  fi

  current_end="$current_start"
done

for ((i=${#rows[@]}-1; i>=0; i--)); do
  printf "%s\n" "${rows[i]}" >> "$RESULT_FILE"
done
