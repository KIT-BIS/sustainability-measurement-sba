# WCAG Conformity Checker

Automated WCAG 2.1 Level AA conformity checker for websites using axe-core accessibility testing engine.

## Overview

This tool analyzes websites for WCAG 2.1 Level AA accessibility conformance issues using the industry-standard axe-core engine. It provides detailed reports including violation details, severity breakdowns, WCAG criterion mappings, and actionable recommendations.

## Important Limitations

**Automated testing can only detect approximately 50% of accessibility issues.** This tool should be used as part of a comprehensive accessibility testing strategy that includes:

- Manual testing with assistive technologies (screen readers, keyboard navigation, etc.)
- User testing with people who use assistive technologies
- Expert accessibility reviews
- Testing across different browsers and devices

Passing automated tests does not guarantee full accessibility compliance.

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Create a Virtual Environment

It's recommended to use a Python virtual environment to isolate dependencies:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

When the virtual environment is active, you'll see `(.venv)` in your terminal prompt.

To deactivate the virtual environment when done:
```bash
deactivate
```

### Installation

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Install Playwright browser binaries:

```bash
playwright install chromium
```

This downloads the Chromium browser binary needed for testing (approximately 300MB).

## Usage

### Basic Usage

Check a single website:

```bash
./check_wcag.py https://example.com
```

### Specify WCAG Conformance Level

Check against different WCAG conformance levels:

```bash
# Check Level A (minimum - basic accessibility)
./check_wcag.py --level A https://example.com

# Check Level AA (default - recommended standard)
./check_wcag.py --level AA https://example.com
# or simply:
./check_wcag.py https://example.com

# Check Level AAA (maximum - most comprehensive)
./check_wcag.py --level AAA https://example.com
```

**WCAG Conformance Levels:**
- **Level A**: Minimum accessibility features (e.g., alt text, keyboard access)
- **Level AA**: Industry standard, includes all Level A + additional criteria (e.g., color contrast 4.5:1)
- **Level AAA**: Highest level, includes all Level A + AA + strictest criteria (e.g., enhanced contrast 7:1)

Most organizations target Level AA compliance.

### Check Multiple URLs

Analyze multiple pages from a website:

```bash
./check_wcag.py https://example.com https://example.com/about https://example.com/contact
```

### Save Report to File

Save the report to a markdown file:

```bash
./check_wcag.py https://example.com > wcag-report.md
```

### Batch Processing

Check multiple pages from a file using the batch scanning script:

```bash
# Create a file with URLs (one per line)
# See pages_to_scan.txt for format

# Run batch checks (creates individual reports for each URL)
./scan_all_pages.sh

# Scan with specific conformance level
./scan_all_pages.sh -l AAA
./scan_all_pages.sh --level A
```

The batch script will:
- Read URLs from `pages_to_scan.txt`
- Process each URL individually
- Save separate reports in `reports/{LEVEL}/` directory (e.g., `reports/AA/`, `reports/AAA/`)
- Generate reports named `wcag-report-{last-path-segment}.md`
- Provide progress feedback and error handling

Reports are organized by WCAG level:
```
reports/
├── A/          # Level A reports
├── AA/         # Level AA reports (default)
└── AAA/        # Level AAA reports
```

URL list file format (see `pages_to_scan.txt`):
```
https://example.com
https://example.com/about
https://example.com/contact
```

## Report Sections

The tool generates a comprehensive report with the following sections:

### 1. Individual Violations
Table showing all unique violation types with:
- Violation ID
- Impact level (Critical, Serious, Moderate, Minor)
- WCAG criterion (e.g., 1.4.3 Contrast Minimum)
- Description
- Number of occurrences

### 2. Violations by URL
Detailed breakdown for each analyzed URL showing:
- Specific HTML elements with issues
- Violation type and impact
- Failure messages
- Total violations per page

### 3. Overall Statistics
Summary metrics including:
- Total URLs analyzed
- Number of unique violation types
- Total violation instances
- Counts by severity (critical, serious, moderate, minor)
- Overall conformance status (PASS/FAIL)

### 4. Severity Breakdown
Distribution of violations by impact level with percentages

### 5. WCAG Criterion Breakdown
Violations grouped by WCAG 2.1 success criteria with percentages

### 6. Top 10 Issues
Most frequently occurring violations ranked by frequency

### 7. Conformance Summary
Overall WCAG 2.1 Level AA conformance status with interpretation

## Understanding Results

### Impact Levels

- **Critical**: Must be fixed immediately. Severe accessibility barriers that completely prevent access.
- **Serious**: Should be fixed. Significant accessibility barriers that make content very difficult to access.
- **Moderate**: Good to fix. Noticeable accessibility issues that impact user experience.
- **Minor**: Nice to fix. Small issues that may cause minor inconveniences.

### Common WCAG Criteria

Some frequently encountered WCAG 2.1 Level AA criteria:

- **1.4.3 Contrast (Minimum)**: Text must have sufficient color contrast (4.5:1 for normal text, 3:1 for large text)
- **4.1.2 Name, Role, Value**: UI components must have accessible names and roles for assistive technologies
- **1.3.1 Info and Relationships**: Information and relationships conveyed through presentation must be programmatically determinable
- **2.4.2 Page Titled**: Web pages must have descriptive titles
- **2.4.4 Link Purpose**: The purpose of each link should be clear from link text or context

For complete WCAG 2.1 documentation, visit: https://www.w3.org/WAI/WCAG21/quickref/

## What This Tool Tests

The checker runs automated tests for WCAG 2.1 Level A and AA success criteria, including:

- Color contrast
- Form labels and input purpose
- Heading structure and hierarchy
- Image alt text
- Keyboard accessibility
- Link text and purpose
- Page language
- Semantic HTML structure
- ARIA attributes and roles
- Focus management
- And many more...

## What This Tool Cannot Test

Automated testing cannot verify:

- Logical reading order and focus order
- Quality and accuracy of alt text
- Keyboard navigation flow and usability
- Screen reader experience
- Captioning quality for videos
- Consistency of navigation across pages
- Clarity of error messages and instructions
- User interface predictability
- Content that requires human judgment

These aspects require manual testing.

## Troubleshooting

### Browser Installation Issues

If you get an error about missing browsers:

```bash
playwright install chromium
```

### Permission Errors

If the script is not executable:

```bash
chmod +x check_wcag.py
```

### Timeout Errors

For slow-loading websites, the tool has a 30-second timeout. If a page consistently times out, it may be:
- Very slow to load
- Blocking automated access
- Behind authentication

### No Violations Found

If no violations are found, it means:
- The automated checks passed (good!)
- But remember: this is only ~50% of accessibility issues
- Manual testing is still required

## Technical Details

- **Testing Engine**: axe-core (Deque Systems)
- **Browser Automation**: Playwright (Chromium)
- **WCAG Version**: 2.1 Level A and AA
- **Language**: Python 3.7+

## Additional Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [axe-core Rule Descriptions](https://github.com/dequelabs/axe-core/blob/develop/doc/rule-descriptions.md)
- [WebAIM Resources](https://webaim.org/)
- [A11y Project](https://www.a11yproject.com/)

## Contributing

This tool is part of the sustainability-measurement-sba project. For issues or improvements, please refer to the main project repository.

## License

See LICENSE file in the project root directory.
