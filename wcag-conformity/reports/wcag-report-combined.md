# WCAG LEVEL AA CONFORMITY ANALYSIS

Analyzing 14 URL(s)...

Scanning: http://sustainability.spring-boot-admin.com/admin/applications
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/details
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/metrics
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/env
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/beans
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/configprops
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/conditions
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/scheduledtasks
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/depenedencies
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/sbom
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/logfile
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/loggers
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/threaddump
Scanning: http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/mappings

Analysis complete. Found 6 unique violation type(s) with 270 total instance(s).

## INDIVIDUAL VIOLATIONS

| ID             | Impact   | WCAG Criterion   | Description                                                |   Occurrences |
|----------------|----------|------------------|------------------------------------------------------------|---------------|
| button-name    | Critical | N/A              | Buttons must have discernible text                         |             3 |
| image-alt      | Critical | N/A              | Images must have alternative text                          |            14 |
| color-contrast | Serious  | N/A              | Elements must meet minimum color contrast ratio thresholds |            34 |
| html-has-lang  | Serious  | N/A              | <html> element must have a lang attribute                  |            14 |
| link-name      | Serious  | N/A              | Links must have discernible text                           |            15 |
| dlitem         | Serious  | N/A              | <dt> and <dd> elements must be contained by a <dl>         |           190 |

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

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/metrics

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

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

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/beans

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/configprops

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/conditions

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/scheduledtasks

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/depenedencies

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/sbom

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/logfile

| Element                               | Violation ID   | Impact   | Description                               | Issue                                                              |
|---------------------------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------------|
| .btn.px-3.py-2:nth-child(1) (+1 more) | button-name    | Critical | Buttons must have discernible text        | Element does not have inner text that is visible to screen readers |
| .btn.px-3.py-2:nth-child(2)           |                |          |                                           | Element does not have inner text that is visible to screen readers |
| html                                  | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute                  |
| img                                   | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                             |
| a[href$="about"]                      | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers       |

Total violations on this page: 5

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

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/threaddump

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

### http://sustainability.spring-boot-admin.com/admin/instances/e53a359b8ec7/mappings

| Element          | Violation ID   | Impact   | Description                               | Issue                                                        |
|------------------|----------------|----------|-------------------------------------------|--------------------------------------------------------------|
| html             | html-has-lang  | Serious  | <html> element must have a lang attribute | The <html> element does not have a lang attribute            |
| img              | image-alt      | Critical | Images must have alternative text         | Element does not have an alt attribute                       |
| a[href$="about"] | link-name      | Serious  | Links must have discernible text          | Element does not have text that is visible to screen readers |

Total violations on this page: 3

## OVERALL STATISTICS

| Metric                    | Value   |
|---------------------------|---------|
| Total URLs analyzed       | 14      |
| URLs with violations      | 14      |
| Unique violation types    | 6       |
| Total violation instances | 270     |
| Critical issues           | 17      |
| Serious issues            | 253     |
| Moderate issues           | 0       |
| Minor issues              | 0       |
| Overall Conformance       | FAIL    |

## SEVERITY BREAKDOWN

| Severity   |   Count | Percentage   |
|------------|---------|--------------|
| Critical   |      17 | 6.3%         |
| Serious    |     253 | 93.7%        |
| Moderate   |       0 | 0.0%         |
| Minor      |       0 | 0.0%         |

## WCAG CRITERION BREAKDOWN

| WCAG Criterion                  |   Count | Percentage   |
|---------------------------------|---------|--------------|
| 1.3.1 Info and Relationships    |     190 | 70.4%        |
| 1.4.3 Contrast (Minimum)        |      34 | 12.6%        |
| 2.4.4 Link Purpose (In Context) |      15 | 5.6%         |
| 3.1.1 Language of Page          |      14 | 5.2%         |
| 1.1.1 Non-text Content          |      14 | 5.2%         |
| 4.1.2 Name, Role, Value         |       3 | 1.1%         |

## TOP 10 ISSUES BY FREQUENCY

|   Rank | Violation ID   | WCAG   | Description                                                |   Occurrences |
|--------|----------------|--------|------------------------------------------------------------|---------------|
|      1 | dlitem         | N/A    | <dt> and <dd> elements must be contained by a <dl>         |           190 |
|      2 | color-contrast | N/A    | Elements must meet minimum color contrast ratio thresholds |            34 |
|      3 | link-name      | N/A    | Links must have discernible text                           |            15 |
|      4 | html-has-lang  | N/A    | <html> element must have a lang attribute                  |            14 |
|      5 | image-alt      | N/A    | Images must have alternative text                          |            14 |
|      6 | button-name    | N/A    | Buttons must have discernible text                         |             3 |

## CONFORMANCE SUMMARY

**WCAG 2.1 Level AA Conformance:** FAIL

The analyzed website(s) do NOT conform to WCAG 2.1 Level AA standards. 17 critical issue(s) must be addressed immediately.

**Note:** Automated testing can only detect approximately 50% of accessibility issues.
Manual testing and user testing with assistive technologies is strongly recommended.

