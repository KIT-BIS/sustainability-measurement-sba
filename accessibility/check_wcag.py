#!/usr/bin/env python3
"""WCAG conformity checker for websites."""

import argparse
import os
import sys
from typing import List, Dict, Any
from collections import defaultdict
from tabulate import tabulate
from playwright.sync_api import sync_playwright
from axe_playwright_python.sync_playwright import Axe

from accessibility.wcag_utils import (
    run_accessibility_scan,
    categorize_by_severity,
    categorize_by_wcag_criterion,
    get_wcag_criterion_info,
    count_violation_instances,
    format_impact_level,
    get_conformance_status,
    interpret_conformance_status
)


def aggregate_violations(all_results: List[Dict[str, Any]]) -> List[Dict]:
    """
    Aggregate violations from multiple URLs.

    Args:
        all_results: List of results from multiple URL scans

    Returns:
        List of aggregated violations with URL information
    """
    violations_by_id = defaultdict(lambda: {
        'id': '',
        'impact': '',
        'description': '',
        'help': '',
        'helpUrl': '',
        'tags': [],
        'nodes': [],
        'urls': set()
    })

    for result in all_results:
        url = result['url']
        violations = result['violations']

        for violation in violations:
            vid = violation['id']
            if not violations_by_id[vid]['id']:
                # First time seeing this violation ID
                violations_by_id[vid]['id'] = vid
                violations_by_id[vid]['impact'] = violation.get('impact', 'minor')
                violations_by_id[vid]['description'] = violation.get('description', '')
                violations_by_id[vid]['help'] = violation.get('help', '')
                violations_by_id[vid]['helpUrl'] = violation.get('helpUrl', '')
                violations_by_id[vid]['tags'] = violation.get('tags', [])

            # Add nodes and URL
            violations_by_id[vid]['nodes'].extend(violation.get('nodes', []))
            violations_by_id[vid]['urls'].add(url)

    # Convert to list and convert sets to lists
    result = []
    for v in violations_by_id.values():
        v['urls'] = list(v['urls'])
        result.append(v)

    return result


def print_individual_violations_table(violations: List[Dict]):
    """Print table of all unique violations."""
    if not violations:
        print("No violations found.")
        print()
        return

    # Sort by impact (critical > serious > moderate > minor)
    impact_order = {'critical': 0, 'serious': 1, 'moderate': 2, 'minor': 3}
    sorted_violations = sorted(violations, key=lambda v: impact_order.get(v.get('impact', 'minor'), 4))

    table_data = []
    for violation in sorted_violations:
        vid = violation['id']
        impact = format_impact_level(violation.get('impact', 'minor'))
        description = violation.get('help', violation.get('description', ''))
        node_count = len(violation.get('nodes', []))

        # Extract WCAG criterion
        tags = violation.get('tags', [])
        wcag_tags = [tag for tag in tags if tag.startswith('wcag') and len(tag) > 4]
        wcag_criterion = 'N/A'
        if wcag_tags:
            # Parse first WCAG tag
            tag = wcag_tags[0]
            numeric = tag[4:].rstrip('a')
            if len(numeric) >= 3:
                criterion_id = f"{numeric[0]}.{numeric[1]}.{numeric[2:]}"
                criterion_name = get_wcag_criterion_info(criterion_id)
                wcag_criterion = f"{criterion_id} {criterion_name}"

        table_data.append([vid, impact, wcag_criterion, description, node_count])

    print(tabulate(table_data, headers=['ID', 'Impact', 'WCAG Criterion', 'Description', 'Occurrences'], tablefmt='github'))
    print()


def print_per_url_breakdown(all_results: List[Dict[str, Any]]):
    """Print detailed breakdown for each URL."""
    print("## VIOLATIONS BY URL")
    print()

    for result in all_results:
        url = result['url']
        violations = result['violations']

        print(f"### {url}")
        print()

        if not violations:
            print("No violations found on this page.")
            print()
            continue

        table_data = []
        for violation in violations:
            vid = violation['id']
            impact = format_impact_level(violation.get('impact', 'minor'))
            description = violation.get('help', violation.get('description', ''))

            # Get first few nodes as examples
            nodes = violation.get('nodes', [])
            for i, node in enumerate(nodes[:3]):  # Show up to 3 examples
                target = node.get('target', ['Unknown'])
                target_str = target[0] if isinstance(target, list) and target else str(target)

                # Get failure message
                failure_summary = ''
                failures = node.get('any', []) + node.get('all', []) + node.get('none', [])
                if failures:
                    failure_summary = failures[0].get('message', '')

                # Only show ID, impact, description on first row
                if i == 0:
                    extra = f" (+{len(nodes)-1} more)" if len(nodes) > 1 else ""
                    table_data.append([target_str + extra, vid, impact, description, failure_summary])
                else:
                    table_data.append([target_str, '', '', '', failure_summary])

        print(tabulate(table_data, headers=['Element', 'Violation ID', 'Impact', 'Description', 'Issue'], tablefmt='github'))
        print()
        print(f"Total violations on this page: {count_violation_instances(violations)}")
        print()


def print_statistics(all_violations: List[Dict], all_results: List[Dict[str, Any]]):
    """Print overall statistics."""
    print("## OVERALL STATISTICS")
    print()

    total_instances = count_violation_instances(all_violations)
    severity_counts = categorize_by_severity(all_violations)

    urls_with_violations = sum(1 for r in all_results if len(r['violations']) > 0)

    stats_table = [
        ["Total URLs analyzed", len(all_results)],
        ["URLs with violations", urls_with_violations],
        ["Unique violation types", len(all_violations)],
        ["Total violation instances", total_instances],
        ["Critical issues", count_violation_instances(severity_counts.get('critical', []))],
        ["Serious issues", count_violation_instances(severity_counts.get('serious', []))],
        ["Moderate issues", count_violation_instances(severity_counts.get('moderate', []))],
        ["Minor issues", count_violation_instances(severity_counts.get('minor', []))],
        ["Overall Conformance", get_conformance_status(all_violations)]
    ]

    print(tabulate(stats_table, headers=['Metric', 'Value'], tablefmt='github'))
    print()


def print_severity_breakdown(all_violations: List[Dict]):
    """Print severity distribution."""
    print("## SEVERITY BREAKDOWN")
    print()

    severity_counts = categorize_by_severity(all_violations)
    total_instances = count_violation_instances(all_violations)

    if total_instances == 0:
        print("No violations to categorize.")
        print()
        return

    severity_table = []
    for severity in ['critical', 'serious', 'moderate', 'minor']:
        count = count_violation_instances(severity_counts.get(severity, []))
        percentage = (count / total_instances * 100) if total_instances > 0 else 0
        severity_table.append([format_impact_level(severity), count, f"{percentage:.1f}%"])

    print(tabulate(severity_table, headers=['Severity', 'Count', 'Percentage'], tablefmt='github'))
    print()


def print_wcag_breakdown(all_violations: List[Dict]):
    """Print WCAG criterion distribution."""
    print("## WCAG CRITERION BREAKDOWN")
    print()

    wcag_counts = categorize_by_wcag_criterion(all_violations)
    total_instances = count_violation_instances(all_violations)

    if total_instances == 0 or not wcag_counts:
        print("No WCAG criteria violations to categorize.")
        print()
        return

    # Sort by count (descending)
    sorted_wcag = sorted(wcag_counts.items(), key=lambda x: count_violation_instances(x[1]), reverse=True)

    wcag_table = []
    for criterion_id, viols in sorted_wcag:
        criterion_name = get_wcag_criterion_info(criterion_id)
        count = count_violation_instances(viols)
        percentage = (count / total_instances * 100) if total_instances > 0 else 0
        wcag_table.append([f"{criterion_id} {criterion_name}", count, f"{percentage:.1f}%"])

    print(tabulate(wcag_table, headers=['WCAG Criterion', 'Count', 'Percentage'], tablefmt='github'))
    print()


def print_top_issues(all_violations: List[Dict]):
    """Print top issues by frequency."""
    print("## TOP 10 ISSUES BY FREQUENCY")
    print()

    # Sort by node count
    sorted_violations = sorted(all_violations, key=lambda v: len(v.get('nodes', [])), reverse=True)

    top_10 = sorted_violations[:10]
    if not top_10:
        print("No issues to display.")
        print()
        return

    top_table = []
    for i, violation in enumerate(top_10, 1):
        vid = violation['id']
        description = violation.get('help', violation.get('description', ''))
        node_count = len(violation.get('nodes', []))

        # Extract WCAG criterion
        tags = violation.get('tags', [])
        wcag_tags = [tag for tag in tags if tag.startswith('wcag') and len(tag) > 4]
        wcag_criterion = 'N/A'
        if wcag_tags:
            tag = wcag_tags[0]
            numeric = tag[4:].rstrip('a')
            if len(numeric) >= 3:
                criterion_id = f"{numeric[0]}.{numeric[1]}.{numeric[2:]}"
                wcag_criterion = f"{criterion_id}"

        top_table.append([i, vid, wcag_criterion, description, node_count])

    print(tabulate(top_table, headers=['Rank', 'Violation ID', 'WCAG', 'Description', 'Occurrences'], tablefmt='github'))
    print()




def check_wcag_conformity():
    working_dir = os.getcwd()

    file_path = os.path.join(working_dir, "accessibility\\pages_to_scan.txt")

    urls = []
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    all_results = run_scans(urls)
    return compute_conformity_score(all_results)





def compute_conformity_score(all_results: List[Dict]):

    weights = {
        "critical": 10,
        "serious": 7,
        "moderate": 3,
        "minor": 1,
    }

    score = 0
    total_score = 0

    for result in all_results:

        for violation in result.get("violations", []):
            impact = violation.get("impact")
            total_score += weights.get(impact, 0)

        for passed in result.get("passes", []):
            impact = passed.get("impact")
            w = weights.get(impact, 0)
            total_score += w
            score += w


    if total_score > 0:
        return score / total_score
    else:
        return 0



def run_scans(urls: List[str]):
    all_results = []
    try:
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            # Create Axe instance
            axe = Axe()

            # Scan each URL
            for url in urls:
                #print(f"Scanning: {url}")
                try:
                    results = run_accessibility_scan(url, page, axe)
                    all_results.append({
                        'url': url,
                        'violations': results.get('violations', []),
                        'passes': results.get('passes', []),
                        'incomplete': results.get('incomplete', []),
                        'inapplicable': results.get('inapplicable', [])
                    })
                except Exception as e:
                    print(f"Error scanning {url}: {str(e)}")
                    print()

            # Close browser
            browser.close()

    except Exception as e:
        print(f"Error initializing browser: {str(e)}")
        print("Make sure you have run: playwright install chromium")
        sys.exit(1)

    if not all_results:
        print("No results to display.")
        sys.exit(1)

    return all_results


def main():
    """Main function to run WCAG conformity checks."""
    parser = argparse.ArgumentParser(
        description='Check WCAG 2.1 conformity for websites (A, AA, or AAA).'
    )
    parser.add_argument(
        'urls',
        nargs='+',
        help='One or more URLs to check'
    )
    parser.add_argument(
        '--level',
        type=str,
        choices=['A', 'AA', 'AAA'],
        default='AA',
        help='WCAG conformance level to check (default: AA)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Save report to file (optional)'
    )

    args = parser.parse_args()

    # Validate URLs
    urls = args.urls
    for url in urls:
        if not url.startswith('http://') and not url.startswith('https://'):
            print(f"Error: Invalid URL '{url}'. URLs must start with http:// or https://")
            sys.exit(1)

    print(f"# WCAG LEVEL {args.level} CONFORMITY ANALYSIS")
    print()
    print(f"Analyzing {len(urls)} URL(s)...")
    print()

    all_results = run_scans(urls)

    # Aggregate violations
    all_violations = aggregate_violations(all_results)
    total_instances = count_violation_instances(all_violations)

    print()
    print(f"Analysis complete. Found {len(all_violations)} unique violation type(s) with {total_instances} total instance(s).")
    print()

    # Print report sections
    print("## INDIVIDUAL VIOLATIONS")
    print()
    print_individual_violations_table(all_violations)

    print_per_url_breakdown(all_results)

    print_statistics(all_violations, all_results)

    print_severity_breakdown(all_violations)

    print_wcag_breakdown(all_violations)

    print_top_issues(all_violations)

    # Conformance summary
    print("## CONFORMANCE SUMMARY")
    print()
    status = get_conformance_status(all_violations)
    print(f"**WCAG 2.1 Level {args.level} Conformance:** {status}")
    print()
    print(interpret_conformance_status(all_violations, level=args.level))
    print()
    print("**Note:** Automated testing can only detect approximately 50% of accessibility issues.")
    print("Manual testing and user testing with assistive technologies is strongly recommended.")
    print()


if __name__ == '__main__':
    main()
