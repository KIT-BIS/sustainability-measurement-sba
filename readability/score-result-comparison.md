# Readability Score Comparison

This document compares the results from three readability metrics across all analyzed files from the Spring Boot Admin documentation.

## Overall Statistics Comparison

| Metric                         | Flesch Reading Ease | Flesch-Kincaid | Linsear Write |
|--------------------------------|---------------------|----------------|---------------|
| **Overall Score**              | 17.57               | 15.66          | 12.40         |
| **Interpretation**             | Very Difficult (College graduate) | College Graduate | 12th Grade |
| **Total Files Analyzed**       | 57                  | 57             | 57            |
| **Total Words**                | 17,605              | 17,605         | 17,605        |
| **Total Sentences**            | 939                 | 939            | 939           |
| **Total Syllables**            | 35,259              | 35,259         | 35,259        |
| **Avg Words/Sentence**         | 18.75               | 18.75          | 18.75         |
| **Avg Syllables/Word**         | 2.00                | 2.00           | 2.00          |

## Score Distribution Comparison

### Flesch Reading Ease
| Level            | Score Range | Files |
|------------------|-------------|-------|
| Very Easy        | 90+         | 0     |
| Easy             | 80-89       | 0     |
| Fairly Easy      | 70-79       | 0     |
| Standard         | 60-69       | 0     |
| Fairly Difficult | 50-59       | 4     |
| Difficult        | 30-49       | 12    |
| Very Difficult   | <30         | 41    |

### Flesch-Kincaid Grade Level
| Grade Level   | Score Range | Files |
|---------------|-------------|-------|
| Kindergarten  | < 1         | 0     |
| Elementary    | 1-5         | 0     |
| Middle School | 6-8         | 0     |
| High School   | 9-12        | 14    |
| College       | 13-13.9     | 5     |
| Graduate      | 14+         | 38    |

### Linsear Write Formula
| Grade Level   | Score Range | Files |
|---------------|-------------|-------|
| Kindergarten  | < 1         | 0     |
| Elementary    | 1-5         | 2     |
| Middle School | 6-8         | 7     |
| High School   | 9-12        | 12    |
| College       | 13-13.9     | 4     |
| Graduate      | 14+         | 32    |

## All Files Side-by-Side Comparison

| File | Flesch Score | Flesch Level | FK Score | FK Grade | Linsear Score | Linsear Grade | Words | Sentences | Syllables |
|------|--------------|--------------|----------|----------|---------------|---------------|-------|-----------|-----------|
| 01-getting-started/10-server-setup.md | 30.32 | Difficult (College) | 15.16 | College Graduate | 12.4 | 12th Grade | 296 | 12 | 530 |
| 01-getting-started/20-client-registration.md | 14.04 | Very Difficult (College graduate) | 16.78 | College Graduate | 11.83 | 11th Grade | 485 | 22 | 977 |
| 01-getting-started/50-snapshots.md | 53.55 | Fairly Difficult (10th-12th grade) | 12.25 | 12th Grade | 15.0 | College Graduate | 26 | 1 | 39 |
| 01-getting-started/index.md | 25.94 | Very Difficult (College graduate) | 14.62 | College Graduate | 18.25 | College Graduate | 381 | 19 | 723 |
| 02-server/01-server.mdx | 40.05 | Difficult (College) | 11.73 | 11th Grade | 12.8 | 12th Grade | 294 | 18 | 522 |
| 02-server/02-security.md | 43.36 | Difficult (College) | 10.29 | 10th Grade | 5.8 | 5th Grade | 458 | 37 | 817 |
| 02-server/10-Events.mdx | 44.61 | Difficult (College) | 11.15 | 11th Grade | 11.33 | 11th Grade | 463 | 28 | 796 |
| 02-server/20-Clustering.mdx | 41.58 | Difficult (College) | 11.38 | 11th Grade | 8.29 | 8th Grade | 284 | 18 | 501 |
| 02-server/30-persistence.md | 19.91 | Very Difficult (College graduate) | 16.28 | College Graduate | 13.0 | College Student | 467 | 20 | 901 |
| 02-server/40-instance-registry.md | 15.9 | Very Difficult (College graduate) | 16.93 | College Graduate | 11.0 | 11th Grade | 474 | 20 | 935 |
| 02-server/index.md | 31.2 | Difficult (College) | 13.5 | College Student | 14.4 | College Graduate | 185 | 10 | 343 |
| 02-server/notifications/90-custom-notifiers.md | 6.65 | Very Difficult (College graduate) | 17.19 | College Graduate | 19.75 | College Graduate | 274 | 14 | 584 |
| 02-server/notifications/index.mdx | 41.92 | Difficult (College) | 10.76 | 10th Grade | 11.0 | 11th Grade | 377 | 28 | 674 |
| 02-server/notifications/notifier-dingtalk.mdx | 15.64 | Very Difficult (College graduate) | 17.29 | College Graduate | 19.5 | College Graduate | 25 | 1 | 49 |
| 02-server/notifications/notifier-discord.mdx | -4.13 | Very Difficult (College graduate) | 18.31 | College Graduate | 15.0 | College Graduate | 18 | 1 | 41 |
| 02-server/notifications/notifier-hipchat.mdx | 17.97 | Very Difficult (College graduate) | 16.47 | College Graduate | 17.5 | College Graduate | 23 | 1 | 45 |
| 02-server/notifications/notifier-lets-chat.mdx | 56.25 | Fairly Difficult (10th-12th grade) | 11.62 | 11th Grade | 15.5 | College Graduate | 25 | 1 | 37 |
| 02-server/notifications/notifier-mail.mdx | 28.95 | Very Difficult (College graduate) | 13.26 | College Student | 11.88 | 11th Grade | 65 | 4 | 124 |
| 02-server/notifications/notifier-mattermost.mdx | -4.1 | Very Difficult (College graduate) | 19.55 | College Graduate | 20.5 | College Graduate | 23 | 1 | 51 |
| 02-server/notifications/notifier-msteams.mdx | 3.26 | Very Difficult (College graduate) | 18.52 | College Graduate | 20.5 | College Graduate | 23 | 1 | 49 |
| 02-server/notifications/notifier-rocketchat.mdx | 38.01 | Difficult (College) | 10.69 | 10th Grade | 6.5 | 6th Grade | 22 | 2 | 41 |
| 02-server/notifications/notifier-slack.mdx | 9.75 | Very Difficult (College graduate) | 17.86 | College Graduate | 19.0 | College Graduate | 24 | 1 | 49 |
| 02-server/notifications/notifier-telegram.mdx | -8.04 | Very Difficult (College graduate) | 20.59 | College Graduate | 23.5 | College Graduate | 25 | 1 | 56 |
| 02-server/notifications/notifier-webex.mdx | -5.04 | Very Difficult (College graduate) | 17.94 | College Graduate | 14.0 | College Graduate | 16 | 1 | 37 |
| 03-client/10-client-features.md | 54.04 | Fairly Difficult (10th-12th grade) | 9.64 | 9th Grade | 13.2 | College Student | 457 | 29 | 739 |
| 03-client/20-registration.md | -8.82 | Very Difficult (College graduate) | 19.77 | College Graduate | 11.43 | 11th Grade | 425 | 20 | 975 |
| 03-client/30-metadata.md | 10.82 | Very Difficult (College graduate) | 16.3 | College Graduate | 22.0 | College Graduate | 421 | 23 | 883 |
| 03-client/40-service-discovery.md | 5.44 | Very Difficult (College graduate) | 16.74 | College Graduate | 29.67 | College Graduate | 478 | 28 | 1040 |
| 03-client/80-configuration.md | 50.65 | Fairly Difficult (10th-12th grade) | 9.41 | 9th Grade | 19.25 | College Graduate | 220 | 17 | 372 |
| 03-client/index.md | 20.27 | Very Difficult (College graduate) | 14.97 | College Graduate | 12.5 | 12th Grade | 292 | 16 | 580 |
| 04-integration/10-eureka.md | 3.69 | Very Difficult (College graduate) | 17.79 | College Graduate | 18.0 | College Graduate | 406 | 20 | 876 |
| 04-integration/20-consul.md | 20.92 | Very Difficult (College graduate) | 15.11 | College Graduate | 26.33 | College Graduate | 307 | 16 | 604 |
| 04-integration/30-zookeeper.md | 2.56 | Very Difficult (College graduate) | 18.04 | College Graduate | 28.33 | College Graduate | 186 | 9 | 403 |
| 04-integration/40-hazelcast.md | 14.21 | Very Difficult (College graduate) | 15.03 | College Graduate | 21.0 | College Graduate | 272 | 18 | 570 |
| 04-integration/index.md | -12.04 | Very Difficult (College graduate) | 22.39 | College Graduate | 30.0 | College Graduate | 330 | 11 | 735 |
| 05-security/10-server-authentication.md | 6.92 | Very Difficult (College graduate) | 17.18 | College Graduate | 6.5 | 6th Grade | 354 | 18 | 753 |
| 05-security/20-actuator-security.md | 8.23 | Very Difficult (College graduate) | 16.2 | College Graduate | 7.67 | 7th Grade | 592 | 36 | 1273 |
| 05-security/30-csrf-protection.md | 31.05 | Difficult (College) | 12.87 | 12th Grade | 8.86 | 8th Grade | 683 | 43 | 1289 |
| 05-security/index.md | -2.04 | Very Difficult (College graduate) | 19.91 | College Graduate | 15.6 | College Graduate | 564 | 22 | 1219 |
| 06-customization/monitoring/01-instance-filters.md | 13.51 | Very Difficult (College graduate) | 17.22 | College Graduate | 19.5 | College Graduate | 353 | 15 | 707 |
| 06-customization/monitoring/02-custom-health-status.md | 9.53 | Very Difficult (College graduate) | 17.95 | College Graduate | 8.0 | 8th Grade | 194 | 8 | 396 |
| 06-customization/server/04-endpoint-detection.md | 16.43 | Very Difficult (College graduate) | 14.82 | College Graduate | 6.0 | 6th Grade | 481 | 31 | 993 |
| 08-third-party/index.md | 6.39 | Very Difficult (College graduate) | 13.11 | College Student | 1.5 | 1st Grade | 3 | 1 | 7 |
| 08-third-party/pyctuator.md | 36.99 | Difficult (College) | 11.98 | 11th Grade | 11.4 | 11th Grade | 78 | 5 | 142 |
| 09-samples/10-sample-servlet.md | 5.55 | Very Difficult (College graduate) | 16.77 | College Graduate | 19.5 | College Graduate | 587 | 34 | 1275 |
| 09-samples/20-sample-reactive.md | -2.85 | Very Difficult (College graduate) | 20.22 | College Graduate | 17.0 | College Graduate | 687 | 26 | 1485 |
| 09-samples/30-sample-eureka.md | -0.71 | Very Difficult (College graduate) | 19.18 | College Graduate | 17.0 | College Graduate | 750 | 32 | 1629 |
| 09-samples/40-sample-consul.md | 7.56 | Very Difficult (College graduate) | 19.21 | College Graduate | 16.0 | College Graduate | 649 | 23 | 1309 |
| 09-samples/50-sample-zookeeper.md | 0.51 | Very Difficult (College graduate) | 17.99 | College Graduate | 13.0 | College Student | 116 | 6 | 256 |
| 09-samples/60-sample-hazelcast.md | 20.57 | Very Difficult (College graduate) | 13.86 | College Student | 20.75 | College Graduate | 321 | 23 | 653 |
| 09-samples/70-sample-custom-ui.md | 34.59 | Difficult (College) | 12.24 | 12th Grade | 13.2 | College Student | 291 | 19 | 539 |
| 09-samples/index.md | 8.66 | Very Difficult (College graduate) | 17.3 | College Graduate | 26.33 | College Graduate | 359 | 17 | 750 |
| 10-reference/10-event-types.md | 1.1 | Very Difficult (College graduate) | 21.11 | College Graduate | 15.0 | College Graduate | 483 | 15 | 988 |
| 10-reference/20-rest-api.md | 23.19 | Very Difficult (College graduate) | 13.36 | College Student | 12.67 | 12th Grade | 524 | 39 | 1053 |
| 10-reference/60-actuator-endpoints.mdx | 20.8 | Very Difficult (College graduate) | 18.56 | College Graduate | 21.5 | College Graduate | 66 | 2 | 119 |
| 10-reference/index.md | 18.24 | Very Difficult (College graduate) | 15.8 | College Graduate | 25.67 | College Graduate | 307 | 15 | 609 |
| 11-upgrading/01-spring-boot-admin-4.md | 37.8 | Difficult (College) | 11.81 | 11th Grade | 10.83 | 10th Grade | 616 | 40 | 1117 |

## Key Insights

### Most Difficult Files (Consensus)
These files ranked in the top 10 most difficult across all three metrics:

1. **04-integration/index.md** - Ranked #1 in Flesch and Flesch-Kincaid, #1 in Linsear
2. **10-reference/10-event-types.md** - Consistently very difficult across all metrics
3. **02-server/notifications/notifier-telegram.mdx** - Extremely difficult across all metrics

### Metric Divergence Examples
Files where metrics significantly disagree:

- **03-client/40-service-discovery.md**: Flesch (5.44 - Very Difficult) vs Linsear (29.67 - College Graduate)
- **05-security/10-server-authentication.md**: Flesch-Kincaid (17.18 - College Graduate) vs Linsear (6.5 - 6th Grade)
- **08-third-party/index.md**: Only 3 words, showing metric instability on small files

### Overall Assessment
- **Flesch Reading Ease** rates the documentation as "Very Difficult (College graduate)" with 72% of files in this category
- **Flesch-Kincaid** rates most files (67%) as requiring a College Graduate reading level
- **Linsear Write** is more lenient, distributing files across a wider range (5th grade to College Graduate)
- The documentation consistently requires advanced reading skills across all metrics, with very few files accessible to general readers
