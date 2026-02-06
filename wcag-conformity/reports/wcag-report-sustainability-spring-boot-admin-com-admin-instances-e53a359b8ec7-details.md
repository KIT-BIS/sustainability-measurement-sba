# WCAG LEVEL AA CONFORMITY ANALYSIS

Analyzing 1 URL(s)...

Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/details

Analysis complete. Found 4 unique violation type(s) with 13 total instance(s).

## INDIVIDUAL VIOLATIONS

| ID             | Impact   | WCAG Criterion   | Description                                                |   Occurrences |
|----------------|----------|------------------|------------------------------------------------------------|---------------|
| image-alt      | Critical | N/A              | Images must have alternative text                          |             1 |
| color-contrast | Serious  | N/A              | Elements must meet minimum color contrast ratio thresholds |             9 |
| html-has-lang  | Serious  | N/A              | <html> element must have a lang attribute                  |             1 |
| link-name      | Serious  | N/A              | Links must have discernible text                           |             2 |

## VIOLATIONS BY URL

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/details

| Element                                                                            | Violation ID   | Impact   | Description                                                | Issue                                                                                                                                                                                  |
|------------------------------------------------------------------------------------|----------------|----------|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .ml-2.transition-opacity.status-badge (+8 more)                                    | color-contrast | Serious  | Elements must meet minimum color contrast ratio thresholds | Element has insufficient color contrast of 4.13 (foreground color: #15803d, background color: #bbf7d0, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1 |
| dd[aria-labelledby="health-v-2__Instance"] > .status-badge.up[data-v-1a9c14bf=""]  |                |          |                                                            | Element has insufficient color contrast of 4.13 (foreground color: #15803d, background color: #bbf7d0, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1 |
| dd[aria-labelledby="health-v-3__diskSpace"] > .status-badge.up[data-v-1a9c14bf=""] |                |          |                                                            | Element has insufficient color contrast of 4.13 (foreground color: #15803d, background color: #bbf7d0, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1 |
| html                                                                               | html-has-lang  | Serious  | <html> element must have a lang attribute                  | The <html> element does not have a lang attribute                                                                                                                                      |
| img                                                                                | image-alt      | Critical | Images must have alternative text                          | Element does not have an alt attribute                                                                                                                                                 |
| a[href$="about"] (+1 more)                                                         | link-name      | Serious  | Links must have discernible text                           | Element does not have text that is visible to screen readers                                                                                                                           |
| .leading-sm                                                                        |                |          |                                                            | Element does not have text that is visible to screen readers                                                                                                                           |

Total violations on this page: 13

## OVERALL STATISTICS

| Metric                    | Value   |
|---------------------------|---------|
| Total URLs analyzed       | 1       |
| URLs with violations      | 1       |
| Unique violation types    | 4       |
| Total violation instances | 13      |
| Critical issues           | 1       |
| Serious issues            | 12      |
| Moderate issues           | 0       |
| Minor issues              | 0       |
| Overall Conformance       | FAIL    |

## SEVERITY BREAKDOWN

| Severity   |   Count | Percentage   |
|------------|---------|--------------|
| Critical   |       1 | 7.7%         |
| Serious    |      12 | 92.3%        |
| Moderate   |       0 | 0.0%         |
| Minor      |       0 | 0.0%         |

## WCAG CRITERION BREAKDOWN

| WCAG Criterion                  |   Count | Percentage   |
|---------------------------------|---------|--------------|
| 1.4.3 Contrast (Minimum)        |       9 | 69.2%        |
| 2.4.4 Link Purpose (In Context) |       2 | 15.4%        |
| 3.1.1 Language of Page          |       1 | 7.7%         |
| 1.1.1 Non-text Content          |       1 | 7.7%         |

## TOP 10 ISSUES BY FREQUENCY

|   Rank | Violation ID   | WCAG   | Description                                                |   Occurrences |
|--------|----------------|--------|------------------------------------------------------------|---------------|
|      1 | color-contrast | N/A    | Elements must meet minimum color contrast ratio thresholds |             9 |
|      2 | link-name      | N/A    | Links must have discernible text                           |             2 |
|      3 | html-has-lang  | N/A    | <html> element must have a lang attribute                  |             1 |
|      4 | image-alt      | N/A    | Images must have alternative text                          |             1 |

## CONFORMANCE SUMMARY

**WCAG 2.1 Level AA Conformance:** FAIL

The analyzed website(s) do NOT conform to WCAG 2.1 Level AA standards. 1 critical issue(s) must be addressed immediately.

**Note:** Automated testing can only detect approximately 50% of accessibility issues.
Manual testing and user testing with assistive technologies is strongly recommended.

