#!/usr/bin/env bash
# Script to scan all pages from pages_to_scan.txt and generate individual WCAG reports
#
# Usage: ./scan_all_pages.sh [-l LEVEL]
# Options:
#   -l, --level LEVEL    WCAG conformance level (A, AA, or AAA). Default: AA

set -e  # Exit on error

PAGES_FILE="pages_to_scan.txt"
BASE_OUTPUT_DIR="reports"
LEVEL="AA"  # Default to AA

# Parse command line arguments
while getopts "l:-:" opt; do
  case $opt in
    l)
      LEVEL="$OPTARG"
      ;;
    -)
      case "$OPTARG" in
        level=*)
          LEVEL="${OPTARG#level=}"
          ;;
        *)
          echo "Invalid option: --$OPTARG" >&2
          exit 1
          ;;
      esac
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done
shift $((OPTIND-1))

# Validate level
if [[ ! "$LEVEL" =~ ^(A|AA|AAA)$ ]]; then
    echo "Error: Level must be A, AA, or AAA (got: $LEVEL)"
    exit 1
fi

# Set output directory based on WCAG level
OUTPUT_DIR="$BASE_OUTPUT_DIR/$LEVEL"

# Check if pages file exists
if [ ! -f "$PAGES_FILE" ]; then
    echo "Error: $PAGES_FILE not found"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "Using WCAG Level $LEVEL"
echo "Reports will be saved to: $OUTPUT_DIR/"
echo ""

# Read each line from the pages file
line_number=0
while IFS= read -r url || [ -n "$url" ]; do
    # Skip empty lines
    if [ -z "$url" ]; then
        continue
    fi

    line_number=$((line_number + 1))

    # Extract a clean filename from the URL (last part only)
    # Remove protocol, extract last path segment, clean special chars
    filename=$(echo "$url" | sed 's|https\?://||' | sed 's|.*/||' | sed 's|[?&=]|_|g')
    output_file="$OUTPUT_DIR/wcag-report-${filename}.md"

    echo "[$line_number] Scanning: $url"
    echo "    Output: $output_file"

    # Run the WCAG checker and save output to markdown file
    if python3 check_wcag.py --level "$LEVEL" "$url" > "$output_file" 2>&1; then
        echo "    ✓ Complete"
    else
        echo "    ✗ Failed (see $output_file for details)"
    fi

    echo ""
done < "$PAGES_FILE"

echo "All scans complete. Reports saved in $OUTPUT_DIR/"
