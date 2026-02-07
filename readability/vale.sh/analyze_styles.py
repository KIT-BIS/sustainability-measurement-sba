#!/usr/bin/env python3
"""
Comprehensive Vale Style Comparison Tool
Analyzes vale results across different styles with multiple comparison approaches
"""

import os
import re
from collections import defaultdict, Counter
from pathlib import Path

def parse_vale_file(filepath):
    """Parse a vale result file and extract issues"""
    issues = []

    with open(filepath, 'r') as f:
        content = f.read()

    # Extract issues using regex
    # Pattern: line:col  severity  message  rule
    pattern = r'(\d+):(\d+)\s+(error|warning|suggestion)\s+(.+?)\s{2,}([\w\.\-]+)'

    for match in re.finditer(pattern, content):
        line, col, severity, message, rule = match.groups()
        issues.append({
            'line': int(line),
            'col': int(col),
            'severity': severity,
            'message': message.strip(),
            'rule': rule.strip()
        })

    return issues

def analyze_style_directory(style_path):
    """Analyze all result files in a style directory"""
    style_data = {
        'files': {},
        'rule_counts': Counter(),
        'severity_counts': Counter(),
        'rule_severity': defaultdict(Counter),
        'total_issues': 0
    }

    for result_file in Path(style_path).glob('vale-results.*.txt'):
        filename = result_file.stem.replace('vale-results.', '')
        issues = parse_vale_file(result_file)

        style_data['files'][filename] = issues
        style_data['total_issues'] += len(issues)

        for issue in issues:
            style_data['rule_counts'][issue['rule']] += 1
            style_data['severity_counts'][issue['severity']] += 1
            style_data['rule_severity'][issue['rule']][issue['severity']] += 1

    return style_data

def compare_styles(base_dir):
    """Compare all styles in the directory"""
    styles = {}

    for style_dir in Path(base_dir).iterdir():
        if style_dir.is_dir() and not style_dir.name.startswith('.'):
            print(f"Analyzing {style_dir.name}...")
            styles[style_dir.name] = analyze_style_directory(style_dir)

    return styles

def print_comparison_report(styles):
    """Print comprehensive comparison report"""

    print("\n" + "="*80)
    print("COMPREHENSIVE VALE STYLE COMPARISON")
    print("="*80)

    # 1. Basic Stats with Weighted Scores
    print("\n1. WEIGHTED SCORE COMPARISON")
    print("-" * 80)
    print(f"{'Style':<15} {'Errors':<8} {'Warnings':<10} {'Suggest':<10} {'Weighted':>10}")
    print("-" * 80)

    weighted_scores = {}
    for style_name in sorted(styles.keys()):
        data = styles[style_name]
        errors = data['severity_counts']['error']
        warnings = data['severity_counts']['warning']
        suggestions = data['severity_counts']['suggestion']
        weighted = (errors * 3) + (warnings * 2) + (suggestions * 1)
        weighted_scores[style_name] = weighted

        print(f"{style_name:<15} {errors:<8} {warnings:<10} {suggestions:<10} {weighted:>10}")

    # 2. Rule Coverage Analysis
    print("\n\n2. RULE COVERAGE BY STYLE")
    print("-" * 80)
    all_rules = set()
    for data in styles.values():
        all_rules.update(data['rule_counts'].keys())

    print(f"{'Style':<15} {'Unique Rules':<15} {'Total Rules':>15}")
    print("-" * 80)
    for style_name in sorted(styles.keys()):
        unique_rules = len(styles[style_name]['rule_counts'])
        print(f"{style_name:<15} {unique_rules:<15} {len(all_rules):>15}")

    # 3. Top Rules per Style
    print("\n\n3. TOP 5 RULES BY STYLE (most frequent issues)")
    print("-" * 80)
    for style_name in sorted(styles.keys()):
        print(f"\n{style_name}:")
        data = styles[style_name]
        for rule, count in data['rule_counts'].most_common(5):
            severities = data['rule_severity'][rule]
            sev_str = ", ".join([f"{s}: {c}" for s, c in severities.items()])
            print(f"  {rule:<35} {count:>4} issues ({sev_str})")

    # 4. Focus Area Analysis
    print("\n\n4. FOCUS AREA ANALYSIS")
    print("-" * 80)

    focus_categories = {
        'Style & Formatting': ['Headings', 'Colons', 'Capitalization', 'Exclamation'],
        'Word Choice': ['WordList', 'Will', 'Passive', 'FirstPerson'],
        'Spelling': ['Spelling'],
        'Grammar': ['ThereIs', 'Wordiness', 'So', 'Weasel'],
        'Technical': ['Acronyms', 'HeadingAcronyms']
    }

    for style_name in sorted(styles.keys()):
        print(f"\n{style_name}:")
        data = styles[style_name]
        focus_breakdown = defaultdict(int)

        for rule, count in data['rule_counts'].items():
            categorized = False
            for category, keywords in focus_categories.items():
                if any(keyword in rule for keyword in keywords):
                    focus_breakdown[category] += count
                    categorized = True
                    break
            if not categorized:
                focus_breakdown['Other'] += count

        total = sum(focus_breakdown.values())
        for category in sorted(focus_breakdown.keys(), key=lambda x: focus_breakdown[x], reverse=True):
            count = focus_breakdown[category]
            pct = (count / total * 100) if total > 0 else 0
            print(f"  {category:<25} {count:>4} issues ({pct:>5.1f}%)")

    # 5. Issue Density per File
    print("\n\n5. AVERAGE ISSUE DENSITY PER FILE")
    print("-" * 80)
    print(f"{'Style':<15} {'Total Files':<15} {'Avg Issues/File':>20}")
    print("-" * 80)
    for style_name in sorted(styles.keys()):
        data = styles[style_name]
        file_count = len(data['files'])
        avg_density = data['total_issues'] / file_count if file_count > 0 else 0
        print(f"{style_name:<15} {file_count:<15} {avg_density:>20.2f}")

    # 6. Recommendations
    print("\n\n6. RECOMMENDATIONS")
    print("-" * 80)

    sorted_by_score = sorted(weighted_scores.items(), key=lambda x: x[1])

    print("\nBest for minimal friction (lowest weighted score):")
    print(f"  ✓ {sorted_by_score[0][0]} (score: {sorted_by_score[0][1]})")

    print("\nBest for comprehensive checking (highest weighted score):")
    print(f"  ✓ {sorted_by_score[-1][0]} (score: {sorted_by_score[-1][1]})")

    # Find style with most balanced distribution
    print("\nBest for balanced error/warning distribution:")
    for style_name in sorted(styles.keys()):
        data = styles[style_name]
        errors = data['severity_counts']['error']
        warnings = data['severity_counts']['warning']
        if errors > 0 and warnings > 0:
            ratio = min(errors, warnings) / max(errors, warnings)
            print(f"  {style_name}: {errors} errors, {warnings} warnings (ratio: {ratio:.2f})")

if __name__ == '__main__':
    base_dir = '/Users/stekoe/Downloads/vale.sh'
    styles = compare_styles(base_dir)
    print_comparison_report(styles)
