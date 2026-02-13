# WCAG LEVEL AA CONFORMITY ANALYSIS

Analyzing 1 URL(s)...

Scanning: http://sustainability.spring-boot-admin.com/admin/applications

Analysis complete. Found 5 unique violation type(s) with 12 total instance(s).

## INDIVIDUAL VIOLATIONS

| ID             | Impact   | WCAG Criterion   | Description                                                |   Occurrences |
|----------------|----------|------------------|------------------------------------------------------------|---------------|
| button-name    | Critical | N/A              | Buttons must have discernible text                         |             1 |
| image-alt      | Critical | N/A              | Images must have alternative text                          |             1 |
| color-contrast | Serious  | N/A              | Elements must meet minimum color contrast ratio thresholds |             8 |
| html-has-lang  | Serious  | N/A              | <html> element must have a lang attribute                  |             1 |
| link-name      | Serious  | N/A              | Links must have discernible text                           |             1 |

## VIOLATIONS BY URL

### http://sustainability.spring-boot-admin.com/admin/applications

| Element                                                                                                                      | Violation ID   | Impact   | Description                                                | Issue                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------|----------------|----------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| button[title=""]                                                                                                             | button-name    | Critical | Buttons must have discernible text                         | Element does not have inner text that is visible to screen readers                                                                                                                      |
| .is-active > span > span (+7 more)                                                                                           | color-contrast | Serious  | Elements must meet minimum color contrast ratio thresholds | Element has insufficient color contrast of 3.9 (foreground color: #ffffff, background color: #1e9084, font size: 12.0pt (16px), font weight: normal). Expected contrast ratio of 4.5:1  |
| p                                                                                                                            |                |          |                                                            | Element has insufficient color contrast of 2.53 (foreground color: #9ca3af, background color: #ffffff, font size: 12.0pt (16px), font weight: normal). Expected contrast ratio of 4.5:1 |
| #billing-service > header > h3 > .w-full.flex > .min-w-\[29rem\].flex-row.inline-flex > .status-badge.up[data-v-1a9c14bf=""] |                |          |                                                            | Element has insufficient color contrast of 4.13 (foreground color: #15803d, background color: #bbf7d0, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1  |
| html                                                                                                                         | html-has-lang  | Serious  | <html> element must have a lang attribute                  | The <html> element does not have a lang attribute                                                                                                                                       |
| img                                                                                                                          | image-alt      | Critical | Images must have alternative text                          | Element does not have an alt attribute                                                                                                                                                  |
| a[href$="about"]                                                                                                             | link-name      | Serious  | Links must have discernible text                           | Element does not have text that is visible to screen readers                                                                                                                            |

Total violations on this page: 12

## OVERALL STATISTICS

| Metric                    | Value   |
|---------------------------|---------|
| Total URLs analyzed       | 1       |
| URLs with violations      | 1       |
| Unique violation types    | 5       |
| Total violation instances | 12      |
| Critical issues           | 2       |
| Serious issues            | 10      |
| Moderate issues           | 0       |
| Minor issues              | 0       |
| Overall Conformance       | FAIL    |

## SEVERITY BREAKDOWN

| Severity   |   Count | Percentage   |
|------------|---------|--------------|
| Critical   |       2 | 16.7%        |
| Serious    |      10 | 83.3%        |
| Moderate   |       0 | 0.0%         |
| Minor      |       0 | 0.0%         |

## WCAG CRITERION BREAKDOWN

| WCAG Criterion                  |   Count | Percentage   |
|---------------------------------|---------|--------------|
| 1.4.3 Contrast (Minimum)        |       8 | 66.7%        |
| 4.1.2 Name, Role, Value         |       1 | 8.3%         |
| 3.1.1 Language of Page          |       1 | 8.3%         |
| 1.1.1 Non-text Content          |       1 | 8.3%         |
| 2.4.4 Link Purpose (In Context) |       1 | 8.3%         |

## TOP 10 ISSUES BY FREQUENCY

|   Rank | Violation ID   | WCAG   | Description                                                |   Occurrences |
|--------|----------------|--------|------------------------------------------------------------|---------------|
|      1 | color-contrast | N/A    | Elements must meet minimum color contrast ratio thresholds |             8 |
|      2 | button-name    | N/A    | Buttons must have discernible text                         |             1 |
|      3 | html-has-lang  | N/A    | <html> element must have a lang attribute                  |             1 |
|      4 | image-alt      | N/A    | Images must have alternative text                          |             1 |
|      5 | link-name      | N/A    | Links must have discernible text                           |             1 |

## CONFORMANCE SUMMARY

**WCAG 2.1 Level AA Conformance:** FAIL

The analyzed website(s) do NOT conform to WCAG 2.1 Level AA standards. 2 critical issue(s) must be addressed immediately.

**Note:** Automated testing can only detect approximately 50% of accessibility issues.
Manual testing and user testing with assistive technologies is strongly recommended.

