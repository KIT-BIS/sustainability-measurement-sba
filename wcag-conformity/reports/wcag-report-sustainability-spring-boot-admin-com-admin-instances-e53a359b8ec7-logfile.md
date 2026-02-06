# WCAG LEVEL AA CONFORMITY ANALYSIS

Analyzing 1 URL(s)...

Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/logfile

Analysis complete. Found 4 unique violation type(s) with 5 total instance(s).

## INDIVIDUAL VIOLATIONS

| ID            | Impact   | WCAG Criterion   | Description                               |   Occurrences |
|---------------|----------|------------------|-------------------------------------------|---------------|
| button-name   | Critical | N/A              | Buttons must have discernible text        |             2 |
| image-alt     | Critical | N/A              | Images must have alternative text         |             1 |
| html-has-lang | Serious  | N/A              | <html> element must have a lang attribute |             1 |
| link-name     | Serious  | N/A              | Links must have discernible text          |             1 |

## VIOLATIONS BY URL

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/logfile

| Element                               | Violation ID   | Impact   | Description                               | Issue                                                              |
|---------------------------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------------|
| .btn.px-3.py-2:nth-child(1) (+1 more) | button-name    | Critical | Buttons must have discernible text        | Element does not have inner text that is visible to screen readers |
| .btn.px-3.py-2:nth-child(2)           |                |          |                                           | Element does not have inner text that is visible to screen readers |
| html                                  | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute                  |
| img                                   | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                             |
| a[href$="about"]                      | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers       |

Total violations on this page: 5

## OVERALL STATISTICS

| Metric                    | Value   |
|---------------------------|---------|
| Total URLs analyzed       | 1       |
| URLs with violations      | 1       |
| Unique violation types    | 4       |
| Total violation instances | 5       |
| Critical issues           | 3       |
| Serious issues            | 2       |
| Moderate issues           | 0       |
| Minor issues              | 0       |
| Overall Conformance       | FAIL    |

## SEVERITY BREAKDOWN

| Severity   |   Count | Percentage   |
|------------|---------|--------------|
| Critical   |       3 | 60.0%        |
| Serious    |       2 | 40.0%        |
| Moderate   |       0 | 0.0%         |
| Minor      |       0 | 0.0%         |

## WCAG CRITERION BREAKDOWN

| WCAG Criterion                  |   Count | Percentage   |
|---------------------------------|---------|--------------|
| 4.1.2 Name, Role, Value         |       2 | 40.0%        |
| 3.1.1 Language of Page          |       1 | 20.0%        |
| 1.1.1 Non-text Content          |       1 | 20.0%        |
| 2.4.4 Link Purpose (In Context) |       1 | 20.0%        |

## TOP 10 ISSUES BY FREQUENCY

|   Rank | Violation ID   | WCAG   | Description                               |   Occurrences |
|--------|----------------|--------|-------------------------------------------|---------------|
|      1 | button-name    | N/A    | Buttons must have discernible text        |             2 |
|      2 | html-has-lang  | N/A    | <html> element must have a lang attribute |             1 |
|      3 | image-alt      | N/A    | Images must have alternative text         |             1 |
|      4 | link-name      | N/A    | Links must have discernible text          |             1 |

## CONFORMANCE SUMMARY

**WCAG 2.1 Level AA Conformance:** FAIL

The analyzed website(s) do NOT conform to WCAG 2.1 Level AA standards. 3 critical issue(s) must be addressed immediately.

**Note:** Automated testing can only detect approximately 50% of accessibility issues.
Manual testing and user testing with assistive technologies is strongly recommended.

