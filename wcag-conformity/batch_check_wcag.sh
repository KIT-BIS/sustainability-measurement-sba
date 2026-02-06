#!/usr/bin/env bash
#
# Batch WCAG conformity checker
# Runs WCAG checks on multiple websites from a list
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WCAG_SCRIPT="${SCRIPT_DIR}/check_wcag.py"

# Default output directory
OUTPUT_DIR="${SCRIPT_DIR}/reports"

# Virtual environment
VENV_DIR="${SCRIPT_DIR}/../.venv"

# Activate virtual environment if it exists
if [[ -d "$VENV_DIR" ]] && [[ -f "$VENV_DIR/bin/activate" ]]; then
    # shellcheck disable=SC1091
    source "$VENV_DIR/bin/activate"
fi

# Usage function
usage() {
    cat << EOF
Usage: $0 [OPTIONS] <url_list_file>

Run WCAG conformity checks on multiple websites from a list.

Arguments:
    url_list_file       File containing URLs, one per line

Options:
    -o, --output DIR    Output directory for reports (default: ./reports)
    -c, --combined      Generate a combined report for all URLs
    -h, --help          Show this help message

Examples:
    # Check URLs from file, save individual reports
    $0 urls.txt

    # Specify custom output directory
    $0 -o /path/to/reports urls.txt

    # Generate both individual and combined reports
    $0 -c urls.txt

URL List File Format:
    Each line should contain one URL:
    https://example.com
    https://example.com/about
    https://example.com/contact

    Empty lines and lines starting with # are ignored.

EOF
    exit 1
}

# Parse command line arguments
COMBINED=false
URL_FILE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -o|--output)
            OUTPUT_DIR="$2"
            shift 2
            ;;
        -c|--combined)
            COMBINED=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        -*)
            echo -e "${RED}Error: Unknown option $1${NC}"
            usage
            ;;
        *)
            URL_FILE="$1"
            shift
            ;;
    esac
done

# Check if URL file is provided
if [[ -z "$URL_FILE" ]]; then
    echo -e "${RED}Error: URL list file is required${NC}"
    usage
fi

# Check if URL file exists
if [[ ! -f "$URL_FILE" ]]; then
    echo -e "${RED}Error: File not found: $URL_FILE${NC}"
    exit 1
fi

# Check if WCAG script exists
if [[ ! -f "$WCAG_SCRIPT" ]]; then
    echo -e "${RED}Error: WCAG checker script not found: $WCAG_SCRIPT${NC}"
    exit 1
fi

# Check if script is executable
if [[ ! -x "$WCAG_SCRIPT" ]]; then
    echo -e "${RED}Error: WCAG checker script is not executable: $WCAG_SCRIPT${NC}"
    echo -e "${YELLOW}Run: chmod +x $WCAG_SCRIPT${NC}"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Batch WCAG Conformity Checker${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "URL list file: ${GREEN}$URL_FILE${NC}"
echo -e "Output directory: ${GREEN}$OUTPUT_DIR${NC}"
echo -e "Combined report: ${GREEN}$COMBINED${NC}"
echo ""

# Read URLs from file (skip empty lines and comments)
mapfile -t URLS < <(grep -v '^#' "$URL_FILE" | grep -v '^[[:space:]]*$')

if [[ ${#URLS[@]} -eq 0 ]]; then
    echo -e "${RED}Error: No URLs found in $URL_FILE${NC}"
    exit 1
fi

echo -e "Found ${GREEN}${#URLS[@]}${NC} URL(s) to check"
echo ""

# Initialize counters
TOTAL=${#URLS[@]}
SUCCESS=0
FAILED=0
FAILED_URLS=()

# Process each URL individually
echo -e "${BLUE}Processing individual URLs...${NC}"
echo ""

for i in "${!URLS[@]}"; do
    URL="${URLS[$i]}"
    NUM=$((i + 1))

    echo -e "${BLUE}[$NUM/$TOTAL]${NC} Checking: ${GREEN}$URL${NC}"

    # Create a safe filename from URL
    FILENAME=$(echo "$URL" | sed -E 's|https?://||' | sed 's|[^a-zA-Z0-9]|-|g' | sed 's|--*|-|g' | sed 's|^-||' | sed 's|-$||')
    REPORT_FILE="${OUTPUT_DIR}/wcag-report-${FILENAME}.md"

    # Run WCAG checker
    if "$WCAG_SCRIPT" "$URL" > "$REPORT_FILE" 2>&1; then
        echo -e "  ${GREEN}✓${NC} Report saved to: $REPORT_FILE"
        SUCCESS=$((SUCCESS + 1))
    else
        echo -e "  ${RED}✗${NC} Failed to check $URL"
        REPORT_FILE="${OUTPUT_DIR}/wcag-error-${FILENAME}.log"
        echo -e "  ${YELLOW}!${NC} Error log saved to: $REPORT_FILE"
        FAILED=$((FAILED + 1))
        FAILED_URLS+=("$URL")
    fi
    echo ""
done

# Generate combined report if requested
if [[ "$COMBINED" = true ]]; then
    echo -e "${BLUE}Generating combined report...${NC}"
    COMBINED_REPORT="${OUTPUT_DIR}/wcag-report-combined.md"

    if "$WCAG_SCRIPT" "${URLS[@]}" > "$COMBINED_REPORT" 2>&1; then
        echo -e "${GREEN}✓${NC} Combined report saved to: $COMBINED_REPORT"
    else
        echo -e "${RED}✗${NC} Failed to generate combined report"
        FAILED=$((FAILED + 1))
    fi
    echo ""
fi

# Summary
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo -e "Total URLs: ${BLUE}$TOTAL${NC}"
echo -e "Successful: ${GREEN}$SUCCESS${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo ""

if [[ $FAILED -gt 0 ]]; then
    echo -e "${RED}Failed URLs:${NC}"
    for url in "${FAILED_URLS[@]}"; do
        echo -e "  - $url"
    done
    echo ""
fi

echo -e "Reports saved to: ${GREEN}$OUTPUT_DIR${NC}"
echo ""

# Exit with appropriate code
if [[ $FAILED -gt 0 ]]; then
    exit 1
else
    echo -e "${GREEN}All checks completed successfully!${NC}"
    exit 0
fi
