# WCAG LEVEL AA CONFORMITY ANALYSIS

Analyzing 1 URL(s)...

Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/env

Analysis complete. Found 4 unique violation type(s) with 193 total instance(s).

## INDIVIDUAL VIOLATIONS

| ID            | Impact   | WCAG Criterion   | Description                                        |   Occurrences |
|---------------|----------|------------------|----------------------------------------------------|---------------|
| image-alt     | Critical | N/A              | Images must have alternative text                  |             1 |
| dlitem        | Serious  | N/A              | <dt> and <dd> elements must be contained by a <dl> |           190 |
| html-has-lang | Serious  | N/A              | <html> element must have a lang attribute          |             1 |
| link-name     | Serious  | N/A              | Links must have discernible text                   |             1 |

## VIOLATIONS BY URL

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/env

| Element                                                                                                                                          | Violation ID   | Impact   | Description                                        | Issue                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------|----------|----------------------------------------------------|--------------------------------------------------------------|
| .break-inside-avoid.mb-4.border:nth-child(1) > .rounded-b.py-3.px-4 > div > .-mx-4.-my-3 > .sm\:grid.sm\:grid-cols-3.sm\:gap-4 > dt (+189 more)  | dlitem         | Serious  | <dt> and <dd> elements must be contained by a <dl> | Description list item does not have a <dl> parent element    |
| .break-inside-avoid.mb-4.border:nth-child(1) > .rounded-b.py-3.px-4 > div > .-mx-4.-my-3 > .sm\:grid.sm\:grid-cols-3.sm\:gap-4 > dd              |                |          |                                                    | Description list item does not have a <dl> parent element    |
| .break-inside-avoid.mb-4.border:nth-child(3) > .rounded-b.py-3.px-4 > div > .-mx-4.-my-3 > .sm\:grid.sm\:grid-cols-3.sm\:gap-4:nth-child(1) > dt |                |          |                                                    | Description list item does not have a <dl> parent element    |
| html                                                                                                                                             | html-has-lang  | Serious  | <html> element must have a lang attribute          | The <html> element does not have a lang attribute            |
| img                                                                                                                                              | image-alt      | Critical | Images must have alternative text                  | Element does not have an alt attribute                       |
| a[href$="about"]                                                                                                                                 | link-name      | Serious  | Links must have discernible text                   | Element does not have text that is visible to screen readers |

Total violations on this page: 193

## OVERALL STATISTICS

| Metric                    | Value   |
|---------------------------|---------|
| Total URLs analyzed       | 1       |
| URLs with violations      | 1       |
| Unique violation types    | 4       |
| Total violation instances | 193     |
| Critical issues           | 1       |
| Serious issues            | 192     |
| Moderate issues           | 0       |
| Minor issues              | 0       |
| Overall Conformance       | FAIL    |

## SEVERITY BREAKDOWN

| Severity   |   Count | Percentage   |
|------------|---------|--------------|
| Critical   |       1 | 0.5%         |
| Serious    |     192 | 99.5%        |
| Moderate   |       0 | 0.0%         |
| Minor      |       0 | 0.0%         |

## WCAG CRITERION BREAKDOWN

| WCAG Criterion                  |   Count | Percentage   |
|---------------------------------|---------|--------------|
| 1.3.1 Info and Relationships    |     190 | 98.4%        |
| 3.1.1 Language of Page          |       1 | 0.5%         |
| 1.1.1 Non-text Content          |       1 | 0.5%         |
| 2.4.4 Link Purpose (In Context) |       1 | 0.5%         |

## TOP 10 ISSUES BY FREQUENCY

|   Rank | Violation ID   | WCAG   | Description                                        |   Occurrences |
|--------|----------------|--------|----------------------------------------------------|---------------|
|      1 | dlitem         | N/A    | <dt> and <dd> elements must be contained by a <dl> |           190 |
|      2 | html-has-lang  | N/A    | <html> element must have a lang attribute          |             1 |
|      3 | image-alt      | N/A    | Images must have alternative text                  |             1 |
|      4 | link-name      | N/A    | Links must have discernible text                   |             1 |

## CONFORMANCE SUMMARY

**WCAG 2.1 Level AA Conformance:** FAIL

The analyzed website(s) do NOT conform to WCAG 2.1 Level AA standards. 1 critical issue(s) must be addressed immediately.

**Note:** Automated testing can only detect approximately 50% of accessibility issues.
Manual testing and user testing with assistive technologies is strongly recommended.

