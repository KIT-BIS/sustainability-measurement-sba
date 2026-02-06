#!/usr/bin/env python3
import argparse
import textstat
from pathlib import Path
from tabulate import tabulate

from markdown_utils import clean_text, find_documentation_files

def calculate_flesch_score(text):
    """Calculate Flesch Reading Ease score using textstat package."""
    # Clean the text
    cleaned_text = clean_text(text)

    # Check if we have enough text to analyze
    if len(cleaned_text.strip()) == 0:
        return None, 0, 0, 0

    # Use textstat to calculate various metrics
    flesch_score = textstat.flesch_reading_ease(cleaned_text)
    word_count = textstat.lexicon_count(cleaned_text)
    sentence_count = textstat.sentence_count(cleaned_text)
    syllable_count = textstat.syllable_count(cleaned_text)

    # Return None if the text is too short
    if word_count == 0 or sentence_count == 0:
        return None, 0, 0, 0

    return flesch_score, word_count, sentence_count, syllable_count

def interpret_flesch_score(score):
    """Interpret the Flesch Reading Ease score."""
    if score >= 90:
        return "Very Easy (5th grade)"
    elif score >= 80:
        return "Easy (6th grade)"
    elif score >= 70:
        return "Fairly Easy (7th grade)"
    elif score >= 60:
        return "Standard (8th-9th grade)"
    elif score >= 50:
        return "Fairly Difficult (10th-12th grade)"
    elif score >= 30:
        return "Difficult (College)"
    else:
        return "Very Difficult (College graduate)"

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Calculate Flesch Reading Ease scores for markdown documentation files.'
    )
    parser.add_argument(
        'docs_dir',
        type=Path,
        help='Path to the documentation directory'
    )
    parser.add_argument(
        '--min-words',
        type=int,
        default=3,
        help='Minimum number of words required for a file to be evaluated (default: 3)'
    )

    args = parser.parse_args()
    docs_dir = args.docs_dir
    min_words = args.min_words

    if not docs_dir.exists():
        print(f"Error: Directory does not exist: {docs_dir}")
        parser.exit(1)

    if not docs_dir.is_dir():
        print(f"Error: Path is not a directory: {docs_dir}")
        parser.exit(1)

    files = find_documentation_files(docs_dir)

    if not files:
        print(f"No documentation files found in {docs_dir}")
        return

    print("# FLESCH READING EASE ANALYSIS - SPRING BOOT ADMIN DOCUMENTATION")
    print(f"Analyzing files in: {docs_dir}  ")
    print(f"Minimum words threshold: {min_words}  ")
    print()

    results = []
    skipped_files = 0
    total_words = 0
    total_sentences = 0
    total_syllables = 0

    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            score, words, sentences, syllables = calculate_flesch_score(content)

            if score is not None and words >= min_words:
                relative_path = file_path.relative_to(docs_dir)
                # Use cleaned content for preview to show what's actually being analyzed
                cleaned_content = clean_text(content)
                results.append({
                    'path': str(relative_path),
                    'score': score,
                    'words': words,
                    'sentences': sentences,
                    'syllables': syllables
                })
                total_words += words
                total_sentences += sentences
                total_syllables += syllables
            elif score is not None and words < min_words:
                skipped_files += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Sort by score (lowest to highest - most difficult first)
    results.sort(key=lambda x: x['score'])

    # Print individual file results as table
    print("## ALL FILES")
    print()
    all_results_table = []
    for result in results:
        all_results_table.append([
            result['path'],
            f"{result['score']:.2f}",
            interpret_flesch_score(result['score']),
            result['words'],
        ])
    print(tabulate(all_results_table, headers=['File', 'Score', 'Level', 'Words'], tablefmt='github'))

    print()
    print("## OVERALL STATISTICS")

    if total_words > 0 and total_sentences > 0:
        # Calculate overall Flesch Reading Ease score using textstat
        # We need to calculate it from all the text combined
        all_text = []
        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    all_text.append(clean_text(content))
            except Exception:
                pass

        combined_text = '\n'.join(all_text)
        overall_score = textstat.flesch_reading_ease(combined_text)

        stats_table = [
            ["Total files analyzed", len(results)],
            ["Total words", f"{total_words:,}"],
            ["Total sentences", f"{total_sentences:,}"],
            ["Total syllables", f"{total_syllables:,}"],
            ["Average words per sentence", f"{total_words/total_sentences:.2f}"],
            ["Average syllables per word", f"{total_syllables/total_words:.2f}"],
            ["Overall Flesch Reading Ease Score", f"{overall_score:.2f}"],
            ["Overall Interpretation", interpret_flesch_score(overall_score)]
        ]

        if skipped_files > 0:
            stats_table.insert(1, [f"Files skipped (< {min_words} words)", skipped_files])

        print(tabulate(stats_table, headers=['Metric', 'Value'], tablefmt='github'))
        print()

        # Score distribution
        print("## SCORE DISTRIBUTION:")
        print()
        very_easy = sum(1 for r in results if r['score'] >= 90)
        easy = sum(1 for r in results if 80 <= r['score'] < 90)
        fairly_easy = sum(1 for r in results if 70 <= r['score'] < 80)
        standard = sum(1 for r in results if 60 <= r['score'] < 70)
        fairly_difficult = sum(1 for r in results if 50 <= r['score'] < 60)
        difficult = sum(1 for r in results if 30 <= r['score'] < 50)
        very_difficult = sum(1 for r in results if r['score'] < 30)

        distribution_table = [
            ["Very Easy", "90+", very_easy],
            ["Easy", "80-89", easy],
            ["Fairly Easy", "70-79", fairly_easy],
            ["Standard", "60-69", standard],
            ["Fairly Difficult", "50-59", fairly_difficult],
            ["Difficult", "30-49", difficult],
            ["Very Difficult", "<30", very_difficult]
        ]
        print(tabulate(distribution_table, headers=['Level', 'Score Range', 'Files'], tablefmt='github'))
        print()

        # Top most difficult and easiest
        print("TOP 10 MOST DIFFICULT FILES:")
        print()
        difficult_table = []
        for i, result in enumerate(results[:10], 1):
            difficult_table.append([
                i,
                result['path'],
                f"{result['score']:.2f}",
                interpret_flesch_score(result['score'])
            ])
        print(tabulate(difficult_table, headers=['Rank', 'File', 'Score', 'Level'], tablefmt='github'))

        print()
        print("TOP 10 EASIEST FILES:")
        print()
        easiest_table = []
        for i, result in enumerate(reversed(results[-10:]), 1):
            easiest_table.append([
                i,
                result['path'],
                f"{result['score']:.2f}",
                interpret_flesch_score(result['score'])
            ])
        print(tabulate(easiest_table, headers=['Rank', 'File', 'Score', 'Level'], tablefmt='github'))

if __name__ == '__main__':
    main()
