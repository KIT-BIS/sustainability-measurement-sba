# WCAG LEVEL A CONFORMITY ANALYSIS

Analyzing 1 URL(s)...

Scanning: http://sustainability.spring-boot-admin.com/admin/applications

Analysis complete. Found 4 unique violation type(s) with 4 total instance(s).

## INDIVIDUAL VIOLATIONS

| ID            | Impact   | WCAG Criterion   | Description                               |   Occurrences |
|---------------|----------|------------------|-------------------------------------------|---------------|
| button-name   | Critical | N/A              | Buttons must have discernible text        |             1 |
| image-alt     | Critical | N/A              | Images must have alternative text         |             1 |
| html-has-lang | Serious  | N/A              | <html> element must have a lang attribute |             1 |
| link-name     | Serious  | N/A              | Links must have discernible text          |             1 |

## VIOLATIONS BY URL

### http://sustainability.spring-boot-admin.com/admin/applications

| Element          | Violation ID   | Impact   | Description                               | Issue                                                              |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------------|
| button[title=""] | button-name    | Critical | Buttons must have discernible text        | Element does not have inner text that is visible to screen readers |
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute                  |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                             |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers       |

Total violations on this page: 4

## OVERALL STATISTICS

| Metric                    | Value   |
|---------------------------|---------|
| Total URLs analyzed       | 1       |
| URLs with violations      | 1       |
| Unique violation types    | 4       |
| Total violation instances | 4       |
| Critical issues           | 2       |
| Serious issues            | 2       |
| Moderate issues           | 0       |
| Minor issues              | 0       |
| Overall Conformance       | FAIL    |

## SEVERITY BREAKDOWN

| Severity   |   Count | Percentage   |
|------------|---------|--------------|
| Critical   |       2 | 50.0%        |
| Serious    |       2 | 50.0%        |
| Moderate   |       0 | 0.0%         |
| Minor      |       0 | 0.0%         |

## WCAG CRITERION BREAKDOWN

| WCAG Criterion                  |   Count | Percentage   |
|---------------------------------|---------|--------------|
| 4.1.2 Name, Role, Value         |       1 | 25.0%        |
| 3.1.1 Language of Page          |       1 | 25.0%        |
| 1.1.1 Non-text Content          |       1 | 25.0%        |
| 2.4.4 Link Purpose (In Context) |       1 | 25.0%        |

## TOP 10 ISSUES BY FREQUENCY

|   Rank | Violation ID   | WCAG   | Description                               |   Occurrences |
|--------|----------------|--------|-------------------------------------------|---------------|
|      1 | button-name    | N/A    | Buttons must have discernible text        |             1 |
|      2 | html-has-lang  | N/A    | <html> element must have a lang attribute |             1 |
|      3 | image-alt      | N/A    | Images must have alternative text         |             1 |
|      4 | link-name      | N/A    | Links must have discernible text          |             1 |

## CONFORMANCE SUMMARY

**WCAG 2.1 Level A Conformance:** FAIL

The analyzed website(s) do NOT conform to WCAG 2.1 Level A standards. 2 critical issue(s) must be addressed immediately.

**Note:** Automated testing can only detect approximately 50% of accessibility issues.
Manual testing and user testing with assistive technologies is strongly recommended.

