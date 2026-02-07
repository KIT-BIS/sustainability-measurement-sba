# Comprehensive Vale Style Comparison

## 1. Weighted Score Comparison

**Formula:** `(Errors × 3) + (Warnings × 2) + (Suggestions × 1)`

| Style | Errors | Warnings | Suggestions | Weighted Score |
|-------|--------|----------|-------------|--------------|
| Google | 12 | 130 | 0 | 296 |
| Microsoft | 13 | 27 | 0 | **93** |
| RedHat | 12 | 115 | 0 | 266 |
| Vale | 56 | 3 | 0 | 174 |

## 2. Rule Coverage by Style

| Style | Unique Rules | Total Rules |
|-------|--------------|-------------|
| Google | 9 | 25 |
| Microsoft | 7 | 25 |
| RedHat | **12** | 25 |
| Vale | 3 | 25 |

## 3. Top 5 Rules by Style

### Google

| Rule | Issues | Severity |
|------|--------|----------|
| Google.WordList | 64 | warning: 64 |
| Google.Headings | 30 | warning: 30 |
| Google.Will | 12 | warning: 12 |
| Google.We | 11 | warning: 11 |
| Google.Colons | 9 | warning: 9 |

### Microsoft

| Rule | Issues | Severity |
|------|--------|----------|
| Microsoft.We | 11 | warning: 11 |
| Microsoft.HeadingAcronyms | 8 | warning: 8 |
| Microsoft.Foreign | 6 | error: 6 |
| write-good.ThereIs | 6 | error: 6 |
| Microsoft.Adverbs | 5 | warning: 5 |

### RedHat

| Rule | Issues | Severity |
|------|--------|----------|
| RedHat.Spelling | 30 | warning: 30 |
| RedHat.TermsWarnings | 22 | warning: 22 |
| RedHat.SmartQuotes | 20 | warning: 20 |
| RedHat.GitLinks | 17 | warning: 17 |
| RedHat.Slash | 7 | warning: 7 |

### Vale

| Rule | Issues | Severity |
|------|--------|----------|
| Vale.Spelling | 50 | error: 50 |
| write-good.ThereIs | 6 | error: 6 |
| write-good.Weasel | 3 | warning: 3 |

## 4. Focus Area Analysis

### Google

| Focus Area | Issues | Percentage |
|------------|--------|------------|
| Word Choice | 76 | 53.5% |
| Style & Formatting | 39 | 27.5% |
| Other | 18 | 12.7% |
| Grammar | 9 | 6.3% |

### Microsoft

| Focus Area | Issues | Percentage |
|------------|--------|------------|
| Other | 23 | 57.5% |
| Grammar | 9 | 22.5% |
| Technical | 8 | 20.0% |

### RedHat

| Focus Area | Issues | Percentage |
|------------|--------|------------|
| Other | 88 | 69.3% |
| Spelling | 30 | 23.6% |
| Grammar | 9 | 7.1% |

### Vale

| Focus Area | Issues | Percentage |
|------------|--------|------------|
| Spelling | 50 | 84.7% |
| Grammar | 9 | 15.3% |

## 5. Average Issue Density per File

| Style | Total Files | Avg Issues/File |
|-------|-------------|---------------|
| Google | 14 | 10.14 |
| Microsoft | 14 | **2.86** |
| RedHat | 14 | 9.07 |
| Vale | 14 | 4.21 |

## 6. Recommendations

### Best for minimal friction (lowest weighted score)
- ✓ **Microsoft** (score: 93)

### Best for comprehensive checking (highest weighted score)
- ✓ **Google** (score: 296)

### Best for balanced error/warning distribution

| Style | Errors | Warnings | Ratio |
|-------|--------|----------|-------|
| Google | 12 | 130 | 0.09 |
| Microsoft | 13 | 27 | **0.48** |
| RedHat | 12 | 115 | 0.10 |
| Vale | 56 | 3 | 0.05 |

---

## Summary

- **For development teams**: Use **Microsoft** - minimal friction with balanced checks (2.86 issues/file)
- **For public documentation**: Use **RedHat** - comprehensive coverage with 12 unique rules
- **For brand consistency**: Use **Google** - strong word choice and formatting enforcement
- **For technical accuracy**: Use **Vale** - focused on spelling/technical terms (84.7% spelling)
