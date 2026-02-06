# WCAG LEVEL AA CONFORMITY ANALYSIS

Analyzing 1 URL(s)...

Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/loggers

Analysis complete. Found 4 unique violation type(s) with 20 total instance(s).

## INDIVIDUAL VIOLATIONS

| ID             | Impact   | WCAG Criterion   | Description                                                |   Occurrences |
|----------------|----------|------------------|------------------------------------------------------------|---------------|
| image-alt      | Critical | N/A              | Images must have alternative text                          |             1 |
| color-contrast | Serious  | N/A              | Elements must meet minimum color contrast ratio thresholds |            17 |
| html-has-lang  | Serious  | N/A              | <html> element must have a lang attribute                  |             1 |
| link-name      | Serious  | N/A              | Links must have discernible text                           |             1 |

## VIOLATIONS BY URL

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/loggers

| Element                                                                                                                                                          | Violation ID   | Impact   | Description                                                | Issue                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|----------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tr:nth-child(2) > .w-1\/4 > .gap-1.is-pulled-right.inline-flex > .btn-group[data-v-51f2155e=""] > .is-info.is-active.logger-control__level--inherited (+16 more) | color-contrast | Serious  | Elements must meet minimum color contrast ratio thresholds | Element has insufficient color contrast of 3.57 (foreground color: #ffffff, background color: #6183e4, font size: 10.5pt (14px), font weight: normal). Expected contrast ratio of 4.5:1 |
| tr:nth-child(3) > .w-1\/4 > .gap-1.is-pulled-right.inline-flex > .btn-group[data-v-51f2155e=""] > .is-info.is-active.logger-control__level--inherited            |                |          |                                                            | Element has insufficient color contrast of 3.57 (foreground color: #ffffff, background color: #6183e4, font size: 10.5pt (14px), font weight: normal). Expected contrast ratio of 4.5:1 |
| tr:nth-child(4) > .w-1\/4 > .gap-1.is-pulled-right.inline-flex > .btn-group[data-v-51f2155e=""] > .is-info.is-active.logger-control__level--inherited            |                |          |                                                            | Element has insufficient color contrast of 3.57 (foreground color: #ffffff, background color: #6183e4, font size: 10.5pt (14px), font weight: normal). Expected contrast ratio of 4.5:1 |
| html                                                                                                                                                             | html-has-lang  | Serious  | <html> element must have a lang attribute                  | The <html> element does not have a lang attribute                                                                                                                                       |
| img                                                                                                                                                              | image-alt      | Critical | Images must have alternative text                          | Element does not have an alt attribute                                                                                                                                                  |
| a[href$="about"]                                                                                                                                                 | link-name      | Serious  | Links must have discernible text                           | Element does not have text that is visible to screen readers                                                                                                                            |

Total violations on this page: 20

## OVERALL STATISTICS

| Metric                    | Value   |
|---------------------------|---------|
| Total URLs analyzed       | 1       |
| URLs with violations      | 1       |
| Unique violation types    | 4       |
| Total violation instances | 20      |
| Critical issues           | 1       |
| Serious issues            | 19      |
| Moderate issues           | 0       |
| Minor issues              | 0       |
| Overall Conformance       | FAIL    |

## SEVERITY BREAKDOWN

| Severity   |   Count | Percentage   |
|------------|---------|--------------|
| Critical   |       1 | 5.0%         |
| Serious    |      19 | 95.0%        |
| Moderate   |       0 | 0.0%         |
| Minor      |       0 | 0.0%         |

## WCAG CRITERION BREAKDOWN

| WCAG Criterion                  |   Count | Percentage   |
|---------------------------------|---------|--------------|
| 1.4.3 Contrast (Minimum)        |      17 | 85.0%        |
| 3.1.1 Language of Page          |       1 | 5.0%         |
| 1.1.1 Non-text Content          |       1 | 5.0%         |
| 2.4.4 Link Purpose (In Context) |       1 | 5.0%         |

## TOP 10 ISSUES BY FREQUENCY

|   Rank | Violation ID   | WCAG   | Description                                                |   Occurrences |
|--------|----------------|--------|------------------------------------------------------------|---------------|
|      1 | color-contrast | N/A    | Elements must meet minimum color contrast ratio thresholds |            17 |
|      2 | html-has-lang  | N/A    | <html> element must have a lang attribute                  |             1 |
|      3 | image-alt      | N/A    | Images must have alternative text                          |             1 |
|      4 | link-name      | N/A    | Links must have discernible text                           |             1 |

## CONFORMANCE SUMMARY

**WCAG 2.1 Level AA Conformance:** FAIL

The analyzed website(s) do NOT conform to WCAG 2.1 Level AA standards. 1 critical issue(s) must be addressed immediately.

**Note:** Automated testing can only detect approximately 50% of accessibility issues.
Manual testing and user testing with assistive technologies is strongly recommended.

