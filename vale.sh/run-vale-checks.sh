#!/bin/bash

# Script to run Vale checks on all .md and .mdx files
# Produces output files following the pattern: vale-results.docs-XX-filename.txt

# Set the base directory (docs directory)
BASE_DIR="docs"

# Output directory (current directory)
OUTPUT_DIR="."

# Initialize counters
total_files=0
total_errors=0
total_warnings=0
total_suggestions=0

# Find all .md and .mdx files in the docs directory
while read -r filepath; do
    echo "Processing: $filepath"

    # Get the relative path from docs directory
    relative_path="${filepath#$BASE_DIR/}"

    # Convert the path to the output filename format
    # Replace / with - and remove the file extension
    filename_base=$(echo "$relative_path" | sed 's/\//-/g' | sed 's/\.[^.]*$//')

    # Create output filename
    output_file="${OUTPUT_DIR}/vale-results.${BASE_DIR}-${filename_base}.txt"

    # Run vale and capture output
    {
        echo "Vale results for: $filepath"
        echo "==========================================="
        echo ""
        vale "$filepath" 2>&1 | sed 's/\x1b\[[0-9;]*m//g'
    } > "$output_file"

    echo "  → Output saved to: $output_file"

    # Increment file counter
    ((total_files++))

    # Parse the results to extract counts
    # Look for lines like "✖ 3 errors, 0 warnings and 0 suggestions in 1 file."
    if grep -qE "(✖|✔) [0-9]+ error" "$output_file"; then
        errors=$(grep -oE "[0-9]+ error" "$output_file" | grep -oE "[0-9]+" | head -1)
        warnings=$(grep -oE "[0-9]+ warning" "$output_file" | grep -oE "[0-9]+" | head -1)
        suggestions=$(grep -oE "[0-9]+ suggestion" "$output_file" | grep -oE "[0-9]+" | head -1)

        total_errors=$((total_errors + ${errors:-0}))
        total_warnings=$((total_warnings + ${warnings:-0}))
        total_suggestions=$((total_suggestions + ${suggestions:-0}))
    fi
done < <(find "$BASE_DIR" -type f \( -name "*.md" -o -name "*.mdx" \) | sort)

# Generate summary file
summary_file="${OUTPUT_DIR}/summary.txt"
{
    echo "Vale Check Summary"
    echo "===================="
    echo "Generated: $(date)"
    echo ""
    echo "Total files checked: $total_files"
    echo "Total errors: $total_errors"
    echo "Total warnings: $total_warnings"
    echo "Total suggestions: $total_suggestions"
    echo ""
    if [ $total_errors -eq 0 ] && [ $total_warnings -eq 0 ] && [ $total_suggestions -eq 0 ]; then
        echo "✔ 0 errors, 0 warnings and 0 suggestions in $total_files files."
    else
        echo "✖ $total_errors errors, $total_warnings warnings and $total_suggestions suggestions in $total_files files."
    fi
    echo ""
} > "$summary_file"

echo ""
echo "Done! All Vale checks completed."
echo "Summary saved to: $summary_file"
