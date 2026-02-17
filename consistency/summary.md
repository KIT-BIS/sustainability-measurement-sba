# Vale Style Comparison Summary

Updated: 2026-02-13

## Overview

| Style | Files | Total Issues | Errors | Warnings | Suggestions | Issues/File |
|-------|-------|--------------|--------|----------|-------------|-------------|
| **Vale** | 34 | 88 | 88 | 0 | 0 | **2.59** |
| **Microsoft** | 34 | 408 | 128 | 43 | 237 | **12.00** |
| **Google** | 34 | 480 | 104 | 198 | 178 | **14.12** |
| **RedHat** | 34 | 579 | 101 | 162 | 316 | **17.03** |

## 1. Issue Density (Issues per File)

Most practical metric for daily use:
- **Vale**: 2.59 issues/file (minimal friction - spelling only)
- **Microsoft**: 12.00 issues/file (moderate)
- **Google**: 14.12 issues/file (higher friction)
- **RedHat**: 17.03 issues/file (most comprehensive)

## 2. Rule Coverage & Distribution

How many unique rules each style enforces:
- **Vale**: 1 rule (ultra-focused on spelling)
- **Google**: 14 rules (focused on Google style guide)
- **Microsoft**: 19 rules (comprehensive coverage)
- **RedHat**: 25 rules (most comprehensive)

## 3. Focus Areas & Top Issues

What each style primarily checks:

**Vale**:
- Vale.Spelling: 88 (100% spelling-focused)
- Technical terms: Jolokia, Env, Threaddump, gradle

**Google**:
- Google.WordList: 93 (terminology preferences)
- Vale.Spelling: 88 (technical terms)
- Google.Passive: 76 (avoid passive voice)
- Google.Headings: 67 (heading format)
- Google.Parens: 38 (parentheses usage)

**Microsoft**:
- Vale.Spelling: 88 (technical terms)
- Microsoft.Passive: 76 (avoid passive voice)
- Microsoft.Headings: 67 (heading format)
- Microsoft.Vocab: 34 (terminology)
- Microsoft.Acronyms: 33 (spell out acronyms)

**RedHat**:
- Vale.Spelling: 88 (technical terms)
- RedHat.Headings: 76 (heading format)
- RedHat.PassiveVoice: 71 (avoid passive voice)
- RedHat.Spelling: 53 (additional spelling rules)
- RedHat.TermsSuggestions: 35 (preferred terminology)

## 4. Severity Balance

How strict each style is (error/warning ratio):
- **Microsoft**: 2.98 (strict - nearly 3x more errors than warnings)
- **RedHat**: 0.62 (balanced - slightly more warnings)
- **Google**: 0.53 (lenient - mostly warnings and suggestions)
- **Vale**: N/A (only errors, no warnings/suggestions)

## 5. Common Patterns Across All Styles

Issues found by multiple styles:
- **Spelling**: All styles flag 88 technical terms (Jolokia, gradle, etc.)
- **Passive Voice**: Found by Google (76), Microsoft (76), RedHat (71)
- **Headings**: Format issues in Google (67), Microsoft (67), RedHat (76)

## Recommendations by Use Case

**Minimal friction (Development team)**:
- **Vale** - Only flags spelling errors, very low noise
- Best for teams who want quick checks without style enforcement

**Balanced approach (Technical documentation)**:
- **Microsoft** - Comprehensive rules but moderate issue count
- Good balance between thoroughness and practicality

**Style enforcement (Brand/Marketing)**:
- **Google** - Strong focus on word choice and terminology
- Enforces Google style guide preferences

**Maximum coverage (Public documentation)**:
- **RedHat** - Most comprehensive (25 rules)
- Catches formatting, style, grammar, and terminology issues