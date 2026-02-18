#!/usr/bin/env python3
"""Analyze Vale results from all style folders and generate summary statistics."""

import os
import re
from pathlib import Path
from collections import defaultdict, Counter

def parse_vale_results(file_path):
    """Parse a Vale results file and extract issues."""
    issues = []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match issue lines: " 1:56    suggestion  Use semicolons judiciously.     Google.Semicolons "
    pattern = r'^\s+\d+:\d+\s+(error|warning|suggestion)\s+.+?\s+(\S+\.\S+)\s*$'

    for line in content.split('\n'):
        match = re.match(pattern, line)
        if match:
            severity = match.group(1)
            rule = match.group(2)
            issues.append({'severity': severity, 'rule': rule})

    return issues

def analyze_style(style_dir):
    """Analyze all results for a given style."""
    result_files = list(Path(style_dir).glob('vale-results.*.txt'))

    all_issues = []
    for result_file in result_files:
        issues = parse_vale_results(result_file)
        all_issues.extend(issues)

    # Count severities
    severity_counts = Counter(issue['severity'] for issue in all_issues)

    # Count rules
    rule_counts = Counter(issue['rule'] for issue in all_issues)

    # Categorize rules
    rule_categories = defaultdict(list)
    for rule in rule_counts:
        category = rule.split('.')[1] if '.' in rule else rule
        rule_categories[category].append(rule)

    return {
        'total_issues': len(all_issues),
        'file_count': len(result_files),
        'severity_counts': dict(severity_counts),
        'rule_counts': dict(rule_counts),
        'rule_categories': dict(rule_categories),
        'unique_rules': len(rule_counts)
    }

def main():
    """Main analysis function."""
    styles = ['Google', 'Microsoft', 'RedHat', 'Vale']
    base_dir = Path(__file__).parent

    results = {}
    for style in styles:
        style_dir = base_dir / style
        if style_dir.exists():
            results[style] = analyze_style(style_dir)

    # Generate summary
    print("# Vale Style Comparison Analysis")
    print()
    print("## Overview")
    print()
    print("| Style | Files | Total Issues | Errors | Warnings | Suggestions | Issues/File |")
    print("|-------|-------|--------------|--------|----------|-------------|-------------|")

    for style in styles:
        if style in results:
            data = results[style]
            sev = data['severity_counts']
            errors = sev.get('error', 0)
            warnings = sev.get('warning', 0)
            suggestions = sev.get('suggestion', 0)
            total = data['total_issues']
            files = data['file_count']
            density = total / files if files > 0 else 0

            print(f"| {style} | {files} | {total} | {errors} | {warnings} | {suggestions} | {density:.2f} |")

    print()
    print("## Detailed Analysis")
    print()

    for style in styles:
        if style in results:
            data = results[style]
            print(f"### {style}")
            print()
            print(f"- **Unique Rules**: {data['unique_rules']}")
            print(f"- **Issue Density**: {data['total_issues'] / data['file_count']:.2f} issues/file")

            # Severity balance
            sev = data['severity_counts']
            errors = sev.get('error', 0)
            warnings = sev.get('warning', 0)
            if warnings > 0:
                ratio = errors / warnings
                print(f"- **Severity Ratio**: {ratio:.2f} (errors/warnings)")

            # Top rules
            print(f"- **Top Rules**:")
            top_rules = sorted(data['rule_counts'].items(), key=lambda x: x[1], reverse=True)[:5]
            for rule, count in top_rules:
                print(f"  - {rule}: {count}")

            print()

if __name__ == '__main__':
    main()
