# Readability Analysis Tools

Tools for analyzing the readability of markdown documentation using Flesch Reading Ease and Linsear Write Formula metrics.

## Setup

### Create a Virtual Environment

It's recommended to use a Python virtual environment to isolate dependencies:

```bash
# Create virtual environment
python3 -m venv ,venv

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

Both scripts generate detailed reports including:
- Individual file scores with interpretation
- Overall statistics (total words, sentences, syllables)
- Score/grade level distribution
- Top 10 most difficult and easiest files
