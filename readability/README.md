# Readability Analysis Tools

Tools for analyzing the readability of markdown documentation using multiple readability metrics: Flesch Reading Ease, Flesch-Kincaid Grade Level, and Linsear Write Formula.

## Setup

### Create a Virtual Environment

It's recommended to use a Python virtual environment to isolate dependencies:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

When the virtual environment is active, you'll see `(.venv)` in your terminal prompt.

To deactivate the virtual environment when done:
```bash
deactivate
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Flesch Reading Ease Score

Calculates readability scores where higher scores indicate easier-to-read text (90+ = very easy, <30 = very difficult).

```bash
./calculate_flesch.py <docs_directory> [--min-words N]
```

Example:
```bash
./calculate_flesch.py /path/to/docs --min-words 10
```

### Flesch-Kincaid Grade Level

Calculates U.S. grade level scores based on sentence length and syllable count. The score directly indicates the educational grade level needed to understand the text.

```bash
./calculate_flesch-kincaid.py <docs_directory> [--min-words N]
```

Example:
```bash
./calculate_flesch-kincaid.py /path/to/docs --min-words 10
```

### Linsear Write Formula

Calculates grade level scores specifically designed for technical writing. The score represents the U.S. grade level needed to understand the text.

```bash
./calculate_linsear_score.py <docs_directory> [--min-words N]
```

Example:
```bash
./calculate_linsear_score.py /path/to/docs --min-words 10
```

## Options

- `docs_directory`: Path to the directory containing markdown files (required)
- `--min-words N`: Minimum word count for files to be analyzed (default: 3)

## Output

All scripts generate detailed reports including:
- **All Files Table**: Lists all analyzed files with their score, interpretation, word count, sentence count, and syllable count
- **Overall Statistics**: Total words, sentences, syllables, averages, and overall score
- **Score/Grade Level Distribution**: Breakdown of files by difficulty level
- **Top 10 Most Difficult Files**: Files requiring the highest reading level
- **Top 10 Easiest Files**: Files with the lowest reading level

## Readability Metrics Explained

### Flesch Reading Ease
- **Range**: 0-100 (higher = easier)
- **Interpretation**:
  - 90-100: Very Easy (5th grade)
  - 60-70: Standard (8th-9th grade)
  - 0-30: Very Difficult (College graduate)
- **Best for**: General readability assessment

### Flesch-Kincaid Grade Level
- **Range**: 0-18+ (indicates U.S. grade level)
- **Interpretation**: Score of 8.0 means 8th grade reading level
- **Best for**: Determining educational level required
- **Formula**: 0.39 × (words/sentences) + 11.8 × (syllables/words) - 15.59

### Linsear Write Formula
- **Range**: 0-18+ (indicates U.S. grade level)
- **Interpretation**: Score of 12.0 means 12th grade reading level
- **Best for**: Technical documentation
- **Focus**: Specifically designed for technical writing evaluation
