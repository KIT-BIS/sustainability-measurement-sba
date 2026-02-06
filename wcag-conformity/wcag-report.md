# WCAG LEVEL AA CONFORMITY ANALYSIS

Analyzing 1 URL(s)...

Scanning: https://stekoe.de

Analysis complete. Found 2 unique violation type(s) with 5 total instance(s).

## INDIVIDUAL VIOLATIONS

| ID        | Impact   | WCAG Criterion   | Description                       |   Occurrences |
|-----------|----------|------------------|-----------------------------------|---------------|
| image-alt | Critical | N/A              | Images must have alternative text |             1 |
| link-name | Serious  | N/A              | Links must have discernible text  |             4 |

## VIOLATIONS BY URL

### https://stekoe.de

| Element                                   | Violation ID   | Impact   | Description                       | Issue                                                        |
|-------------------------------------------|----------------|----------|-----------------------------------|--------------------------------------------------------------|
| img                                       | image-alt      | Critical | Images must have alternative text | Element does not have an alt attribute                       |
| .px-12 > a[href="/"] (+3 more)            | link-name      | Serious  | Links must have discernible text  | Element does not have text that is visible to screen readers |
| a[href$="SteKoe"]                         |                |          |                                   | Element does not have text that is visible to screen readers |
| .rounded-full.text-white.p-2:nth-child(2) |                |          |                                   | Element does not have text that is visible to screen readers |

Total violations on this page: 5

## OVERALL STATISTICS

| Metric                    | Value   |
|---------------------------|---------|
| Total URLs analyzed       | 1       |
| URLs with violations      | 1       |
| Unique violation types    | 2       |
| Total violation instances | 5       |
| Critical issues           | 1       |
| Serious issues            | 4       |
| Moderate issues           | 0       |
| Minor issues              | 0       |
| Overall Conformance       | FAIL    |

## SEVERITY BREAKDOWN

| Severity   |   Count | Percentage   |
|------------|---------|--------------|
| Critical   |       1 | 20.0%        |
| Serious    |       4 | 80.0%        |
| Moderate   |       0 | 0.0%         |
| Minor      |       0 | 0.0%         |

## WCAG CRITERION BREAKDOWN

| WCAG Criterion                  |   Count | Percentage   |
|---------------------------------|---------|--------------|
| 2.4.4 Link Purpose (In Context) |       4 | 80.0%        |
| 1.1.1 Non-text Content          |       1 | 20.0%        |

## TOP 10 ISSUES BY FREQUENCY

|   Rank | Violation ID   | WCAG   | Description                       |   Occurrences |
|--------|----------------|--------|-----------------------------------|---------------|
|      1 | link-name      | N/A    | Links must have discernible text  |             4 |
|      2 | image-alt      | N/A    | Images must have alternative text |             1 |

## CONFORMANCE SUMMARY

**WCAG 2.1 Level AA Conformance:** FAIL

The analyzed website(s) do NOT conform to WCAG 2.1 Level AA standards. 1 critical issue(s) must be addressed immediately.

**Note:** Automated testing can only detect approximately 50% of accessibility issues.
Manual testing and user testing with assistive technologies is strongly recommended.

