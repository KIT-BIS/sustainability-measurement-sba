#!/usr/bin/env python3
import argparse
import textstat
from pathlib import Path
from tabulate import tabulate

from markdown_utils import clean_text, find_documentation_files


def calculate_linear_score(text):
    """Calculate Linsear Write Formula score using textstat package.

    The Linsear Write Formula is specifically designed for technical writing.
    The result represents the grade level needed to understand the text.
    """
    # Clean the text
    cleaned_text = clean_text(text)

    # Check if we have enough text to analyze
    if len(cleaned_text.strip()) == 0:
        return None, 0, 0, 0

    # Use textstat to calculate various metrics
    linsear_score = textstat.linsear_write_formula(cleaned_text)
    word_count = textstat.lexicon_count(cleaned_text)
    sentence_count = textstat.sentence_count(cleaned_text)
    syllable_count = textstat.syllable_count(cleaned_text)

    # Return None if the text is too short
    if word_count == 0 or sentence_count == 0:
        return None, 0, 0, 0

    return linsear_score, word_count, sentence_count, syllable_count


def interpret_linsear_score(score):
    """Interpret the Linsear Write score as grade level."""
    if score < 0:
        return "Below 1st Grade"
    elif score < 1:
        return "Kindergarten"
    elif score < 2:
        return "1st Grade"
    elif score < 3:
        return "2nd Grade"
    elif score < 4:
        return "3rd Grade"
    elif score < 5:
        return "4th Grade"
    elif score < 6:
        return "5th Grade"
    elif score < 7:
        return "6th Grade"
    elif score < 8:
        return "7th Grade"
    elif score < 9:
        return "8th Grade"
    elif score < 10:
        return "9th Grade"
    elif score < 11:
        return "10th Grade"
    elif score < 12:
        return "11th Grade"
    elif score < 13:
        return "12th Grade"
    elif score < 14:
        return "College Student"
    else:
        return "College Graduate"


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Calculate Linsear Write Formula scores for markdown documentation files.'
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

    print("# LINSEAR WRITE FORMULA ANALYSIS - SPRING BOOT ADMIN DOCUMENTATION")
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

            score, words, sentences, syllables = calculate_linear_score(content)

            if score is not None and words >= min_words:
                relative_path = file_path.relative_to(docs_dir)
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

    # Sort by score (highest to lowest - most difficult first)
    results.sort(key=lambda x: x['score'], reverse=True)

    # Print individual file results as table
    print("## ALL FILES")
    print()
    all_results_table = []
    for result in results:
        all_results_table.append([
            result['path'],
            f"{result['score']:.2f}",
            interpret_linsear_score(result['score']),
            result['words'],
            result['sentences'],
            result['syllables']
        ])
    print(tabulate(all_results_table, headers=['File', 'Score', 'Grade Level', 'Words', 'Sentences', 'Syllables'], tablefmt='github'))

    print()
    print("## OVERALL STATISTICS")

    if total_words > 0 and total_sentences > 0:
        # Calculate overall Linsear Write score using textstat
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
        overall_score = textstat.linsear_write_formula(combined_text)

        stats_table = [
            ["Total files analyzed", len(results)],
            ["Total words", f"{total_words:,}"],
            ["Total sentences", f"{total_sentences:,}"],
            ["Total syllables", f"{total_syllables:,}"],
            ["Average words per sentence", f"{total_words / total_sentences:.2f}"],
            ["Average syllables per word", f"{total_syllables / total_words:.2f}"],
            ["Overall Linsear Write Score", f"{overall_score:.2f}"],
            ["Overall Grade Level", interpret_linsear_score(overall_score)]
        ]

        if skipped_files > 0:
            stats_table.insert(1, [f"Files skipped (< {min_words} words)", skipped_files])

        print(tabulate(stats_table, headers=['Metric', 'Value'], tablefmt='github'))
        print()

        # Score distribution
        print("## GRADE LEVEL DISTRIBUTION:")
        print()
        kindergarten = sum(1 for r in results if r['score'] < 1)
        elementary = sum(1 for r in results if 1 <= r['score'] < 6)
        middle_school = sum(1 for r in results if 6 <= r['score'] < 9)
        high_school = sum(1 for r in results if 9 <= r['score'] < 13)
        college = sum(1 for r in results if 13 <= r['score'] < 14)
        graduate = sum(1 for r in results if r['score'] >= 14)

        distribution_table = [
            ["Kindergarten", "< 1", kindergarten],
            ["Elementary", "1-5", elementary],
            ["Middle School", "6-8", middle_school],
            ["High School", "9-12", high_school],
            ["College", "13-13.9", college],
            ["Graduate", "14+", graduate]
        ]
        print(tabulate(distribution_table, headers=['Grade Level', 'Score Range', 'Files'], tablefmt='github'))
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
                interpret_linsear_score(result['score'])
            ])
        print(tabulate(difficult_table, headers=['Rank', 'File', 'Score', 'Grade Level'], tablefmt='github'))

        print()
        print("TOP 10 EASIEST FILES:")
        print()
        easiest_table = []
        for i, result in enumerate(reversed(results[-10:]), 1):
            easiest_table.append([
                i,
                result['path'],
                f"{result['score']:.2f}",
                interpret_linsear_score(result['score'])
            ])
        print(tabulate(easiest_table, headers=['Rank', 'File', 'Score', 'Grade Level'], tablefmt='github'))


if __name__ == '__main__':
    main()
