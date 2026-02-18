"""Utility functions for WCAG conformity checking."""

from typing import Dict, List, Any
from collections import defaultdict

# Mapping of WCAG Success Criteria IDs to human-readable names
WCAG_CRITERIA = {
    "1.1.1": "Non-text Content",
    "1.2.1": "Audio-only and Video-only (Prerecorded)",
    "1.2.2": "Captions (Prerecorded)",
    "1.2.3": "Audio Description or Media Alternative (Prerecorded)",
    "1.3.1": "Info and Relationships",
    "1.3.2": "Meaningful Sequence",
    "1.3.3": "Sensory Characteristics",
    "1.3.4": "Orientation",
    "1.3.5": "Identify Input Purpose",
    "1.4.1": "Use of Color",
    "1.4.2": "Audio Control",
    "1.4.3": "Contrast (Minimum)",
    "1.4.4": "Resize Text",
    "1.4.5": "Images of Text",
    "1.4.10": "Reflow",
    "1.4.11": "Non-text Contrast",
    "1.4.12": "Text Spacing",
    "1.4.13": "Content on Hover or Focus",
    "2.1.1": "Keyboard",
    "2.1.2": "No Keyboard Trap",
    "2.1.4": "Character Key Shortcuts",
    "2.2.1": "Timing Adjustable",
    "2.2.2": "Pause, Stop, Hide",
    "2.3.1": "Three Flashes or Below Threshold",
    "2.4.1": "Bypass Blocks",
    "2.4.2": "Page Titled",
    "2.4.3": "Focus Order",
    "2.4.4": "Link Purpose (In Context)",
    "2.4.5": "Multiple Ways",
    "2.4.6": "Headings and Labels",
    "2.4.7": "Focus Visible",
    "2.5.1": "Pointer Gestures",
    "2.5.2": "Pointer Cancellation",
    "2.5.3": "Label in Name",
    "2.5.4": "Motion Actuation",
    "3.1.1": "Language of Page",
    "3.1.2": "Language of Parts",
    "3.2.1": "On Focus",
    "3.2.2": "On Input",
    "3.2.3": "Consistent Navigation",
    "3.2.4": "Consistent Identification",
    "3.3.1": "Error Identification",
    "3.3.2": "Labels or Instructions",
    "3.3.3": "Error Suggestion",
    "3.3.4": "Error Prevention (Legal, Financial, Data)",
    "4.1.1": "Parsing",
    "4.1.2": "Name, Role, Value",
    "4.1.3": "Status Messages"
}


def get_wcag_tags_for_level(level: str) -> List[str]:
    """
    Get axe-core tags for specified WCAG conformance level.

    Args:
        level: WCAG level ('A', 'AA', or 'AAA')

    Returns:
        List of axe-core tags to test
    """
    # Level A includes only A criteria
    if level == 'A':
        return ["wcag2a", "wcag21a"]

    # Level AA includes A + AA criteria
    elif level == 'AA':
        return ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]

    # Level AAA includes A + AA + AAA criteria
    elif level == 'AAA':
        return ["wcag2a", "wcag2aa", "wcag2aaa", "wcag21a", "wcag21aa", "wcag21aaa"]

    # Default to AA
    return ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]


def run_accessibility_scan(url: str, page, axe, level: str = 'AA') -> Dict[str, Any]:
    """
    Run WCAG accessibility scan on a URL.

    Args:
        url: The URL to scan
        page: Playwright page object
        axe: Axe instance for scanning
        level: WCAG conformance level to check ('A', 'AA', or 'AAA')

    Returns:
        Dictionary containing violations, passes, incomplete, and inapplicable results
    """
    try:
        # Navigate to the URL
        page.goto(url, timeout=30000, wait_until='load')

        # Wait 5 seconds for dynamic content to load
        page.wait_for_timeout(2000)

        # Run axe scan with specified WCAG level tags
        axe_results = axe.run(page, options={
            "runOnly": {
                "type": "tag",
                "values": get_wcag_tags_for_level(level)
            }
        })

        # AxeResults has a 'response' attribute containing the full results
        return axe_results.response
    except Exception as e:
        raise Exception(f"Failed to scan {url}: {str(e)}")


def categorize_by_severity(violations: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Categorize violations by severity/impact level.

    Args:
        violations: List of violation dictionaries from axe-core

    Returns:
        Dictionary mapping severity levels to lists of violations
    """
    categorized = {
        'critical': [],
        'serious': [],
        'moderate': [],
        'minor': []
    }

    for violation in violations:
        impact = violation.get('impact', 'minor')
        if impact in categorized:
            categorized[impact].append(violation)

    return categorized


def categorize_by_wcag_criterion(violations: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Group violations by WCAG success criterion.

    Args:
        violations: List of violation dictionaries from axe-core

    Returns:
        Dictionary mapping WCAG criterion IDs to lists of violations
    """
    categorized = defaultdict(list)

    for violation in violations:
        # Extract WCAG tags from the violation
        tags = violation.get('tags', [])
        wcag_tags = [tag for tag in tags if tag.startswith('wcag')]

        # Parse WCAG version and level from tags (e.g., 'wcag143' -> '1.4.3')
        for tag in wcag_tags:
            # Extract numeric part (e.g., '143' from 'wcag143')
            if len(tag) > 4:
                numeric = tag[4:]
                # Handle different formats: wcagXYZ or wcagXYZlevel
                # Remove level suffix if present (a, aa, aaa)
                numeric = numeric.rstrip('a')

                # Parse the criterion ID
                if len(numeric) >= 3:
                    # Format: X.Y.Z (e.g., 1.4.3)
                    criterion_id = f"{numeric[0]}.{numeric[1]}.{numeric[2:]}"
                    categorized[criterion_id].append(violation)
                    break  # Only add to first matching criterion

    return dict(categorized)


def get_wcag_criterion_info(criterion_id: str) -> str:
    """
    Get human-readable name for a WCAG criterion ID.

    Args:
        criterion_id: WCAG criterion ID (e.g., '1.4.3')

    Returns:
        Human-readable name or the ID if not found
    """
    return WCAG_CRITERIA.get(criterion_id, criterion_id)


def count_violation_instances(violations: List[Dict]) -> int:
    """
    Count total instances across all violations.

    Args:
        violations: List of violation dictionaries from axe-core

    Returns:
        Total count of violation instances
    """
    total = 0
    for violation in violations:
        nodes = violation.get('nodes', [])
        total += len(nodes)
    return total


def format_impact_level(impact: str) -> str:
    """
    Format impact level for display.

    Args:
        impact: Impact level string (critical, serious, moderate, minor)

    Returns:
        Capitalized impact level
    """
    return impact.capitalize() if impact else 'Unknown'


def get_violation_summary(violations: List[Dict]) -> Dict[str, Any]:
    """
    Generate summary statistics for violations.

    Args:
        violations: List of violation dictionaries from axe-core

    Returns:
        Dictionary with summary statistics
    """
    summary = {
        'total_violations': len(violations),
        'total_instances': count_violation_instances(violations),
        'by_severity': {},
        'by_wcag': {}
    }

    # Count by severity
    severity_counts = categorize_by_severity(violations)
    for severity, viols in severity_counts.items():
        summary['by_severity'][severity] = count_violation_instances(viols)

    # Count by WCAG criterion
    wcag_counts = categorize_by_wcag_criterion(violations)
    for criterion_id, viols in wcag_counts.items():
        criterion_name = get_wcag_criterion_info(criterion_id)
        summary['by_wcag'][f"{criterion_id} {criterion_name}"] = count_violation_instances(viols)

    return summary


def get_conformance_status(violations: List[Dict]) -> str:
    """
    Determine overall WCAG conformance status.

    Args:
        violations: List of violation dictionaries from axe-core

    Returns:
        Conformance status string (PASS or FAIL)
    """
    # Any violations mean non-conformance
    if len(violations) > 0:
        return "FAIL"
    return "PASS"


def interpret_conformance_status(violations: List[Dict], level: str = 'AA') -> str:
    """
    Get detailed interpretation of conformance status.

    Args:
        violations: List of violation dictionaries from axe-core
        level: WCAG conformance level ('A', 'AA', or 'AAA')

    Returns:
        Human-readable conformance interpretation
    """
    if len(violations) == 0:
        return f"The analyzed website(s) CONFORM to WCAG 2.1 Level {level} standards based on automated testing."

    severity_counts = categorize_by_severity(violations)
    critical_count = count_violation_instances(severity_counts.get('critical', []))
    serious_count = count_violation_instances(severity_counts.get('serious', []))

    if critical_count > 0:
        return f"The analyzed website(s) do NOT conform to WCAG 2.1 Level {level} standards. {critical_count} critical issue(s) must be addressed immediately."
    elif serious_count > 0:
        return f"The analyzed website(s) do NOT conform to WCAG 2.1 Level {level} standards. {serious_count} serious issue(s) should be addressed."
    else:
        return f"The analyzed website(s) do NOT conform to WCAG 2.1 Level {level} standards. Moderate and minor issues should be addressed."
