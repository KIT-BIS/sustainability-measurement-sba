# Markdownlint

This file documents the Markdownlint rules used for this documentation site, including any local guidance, rationale,
and per-rule `LEVEL` metadata (e.g. `Error`, `Warning`, `Info`). The `LEVEL` entries are also consumed by
`scripts/mdl-group-by-file.py` to enrich its grouped report output.

## MD001 - Header levels should only increment by one level at a time

## MD002 - First header should be a top level header

## MD003 - Header style

## MD004 - Unordered list style

## MD005 - Inconsistent indentation for list items at the same level

## MD006 - Consider starting bulleted lists at the beginning of the line

## MD007 - Unordered list indentation

LEVEL: Warning

It is recommended to use consistent indentation for unordered lists to improve readability and maintain a clean

## MD009 - Trailing spaces

LEVEL: Warning
Trailing spaces can cause formatting issues and may not be displayed correctly in all markdown parsers. It is
recommended to remove trailing spaces from markdown files to improve readability and ensure proper formatting in all
markdown parsers.

## MD010 - Hard tabs

LEVEL: Error
Hard tabs are not allowed in markdown files as they can cause formatting issues and may not be displayed correctly in
all markdown parsers. It is recommended to use spaces instead of tabs for indentation in markdown files.

## MD011 - Reversed link syntax

## MD012 - Multiple consecutive blank lines

## MD013 - Line length

Not applicable as we generate HTML pages from markdown files and the line length is not relevant for the generated HTML.

## MD014 - Dollar signs used before commands without showing output

## MD018 - No space after hash on atx style header

## MD019 - Multiple spaces after hash on atx style header

## MD020 - No space inside hashes on closed atx style header

## MD021 - Multiple spaces inside hashes on closed atx style header

## MD022 - Headers should be surrounded by blank lines

LEVEL: Warning
Headers should be surrounded by blank lines to improve readability and ensure proper formatting in all markdown parsers.

## MD023 - Headers must start at the beginning of the line

LEVEL: Warning
Headers should start at the beginning of the line to improve readability and ensure proper formatting in all markdown
parsers.

## MD024 - Multiple headers with the same content

LEVEL: Warning
That is not wrong at all, but it is not recommended as it may cause confusion for readers and make it harder to navigate
the document.

## MD025 - Multiple top level headers in the same document

LEVEL: Error
Multiple top level headers (e.g., "# Header") in the same document can cause confusion for readers and make it harder to
navigate the document. It is recommended to use only one top level header per document to provide a clear title for the
document and improve readability.

## MD026 - Trailing punctuation in header

## MD027 - Multiple spaces after blockquote symbol

## MD028 - Blank line inside blockquote

## MD029 - Ordered list item prefix

LEVEL: Warning
It is recommended to use a consistent ordered list item prefix (e.g., "1.", "2.", "3.") to improve readability.

## MD030 - Spaces after list markers

## MD031 - Fenced code blocks should be surrounded by blank lines

LEVEL: Warning

## MD032 - Lists should be surrounded by blank lines

## MD033 - Inline HTML

LEVEL: Info
Some code might contain inline HTML, but it is generally recommended to avoid using inline HTML in markdown files as it
can cause formatting issues and may not be displayed correctly in all markdown parsers.

## MD034 - Bare URL used

LEVEL: Warning
Bare URL may be enclosed in code blocks and allowed therer

## MD035 - Horizontal rule style

## MD036 - Emphasis used instead of a header

LEVEL: Warning
Using emphasis (e.g., "*Header*") instead of a header (e.g., "# Header") is not recommended as it can cause confusion
for readers and may not be displayed correctly in all markdown parsers. It is recommended to use proper header syntax
for section titles to improve readability and ensure proper formatting in all markdown parsers.

## MD037 - Spaces inside emphasis markers

## MD038 - Spaces inside code span elements

## MD039 - Spaces inside link text

## MD040 - Fenced code blocks should have a language specified

LEVEL: Warning
It is recommended to specify the language for fenced code blocks to enable syntax highlighting and improve readability.

## MD041 - First line in file should be a top level header

LEVEL: Error
The first line in a markdown file should be a top level header (e.g., "# Header") to provide a clear title for the
document and improve readability.

## MD046 - Code block style

LEVEL: Warning
It is recommended to use fenced code blocks (``` or ~~~) instead of indented code blocks for better readability and to
avoid issues with inconsistent indentation.

## MD047 - File should end with a single newline character
