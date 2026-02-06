#!/usr/bin/env python3
import re
from pathlib import Path


def remove_frontmatter(text):
    """Remove YAML/metadata frontmatter from markdown text.

    Removes content between --- delimiters at the start of the file,
    including any leading whitespace.
    """
    # Remove leading whitespace and frontmatter (---...---)
    text = re.sub(r'^\s*---[\s\S]*?---\s*', '', text)
    return text


def remove_imports(text):
    """Remove JavaScript/TypeScript import statements from MDX files.

    Removes various import patterns:
    - import something from "path";
    - import { something } from "path";
    - import * as something from "path";
    - import "path";
    """
    # Remove all import statements (single or multi-line)
    text = re.sub(r'^import\s+.*?;?\s*$', '', text, flags=re.MULTILINE)
    return text


def remove_code_blocks(text):
    """Remove code blocks from markdown text."""
    # Remove fenced code blocks (```...```)
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Remove inline code (`...`)
    text = re.sub(r'`[^`]+`', '', text)
    return text


def remove_html_and_jsx(text):
    """Remove HTML tags and React/JSX components."""
    # Remove JSX expressions in curly braces (e.g., {variable}, {expression})
    text = re.sub(r'\{[^}]*\}', '', text)
    # Remove self-closing tags (e.g., <br />, <img src="..." />)
    text = re.sub(r'<[^>]+/>', '', text)
    # Remove opening and closing HTML/JSX tags (e.g., <div>, </div>, <Component prop="value">)
    text = re.sub(r'</?[a-zA-Z][^>]*>', '', text)
    return text


def remove_markdown_syntax(text):
    """Remove markdown syntax elements."""
    # Remove headers (#, ##, etc.)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove emphasis markers (*, _, etc.)
    text = re.sub(r'[*_]{1,2}([^*_]+)[*_]{1,2}', r'\1', text)
    # Remove admonitions (:::note, :::info, :::tip, etc.)
    text = re.sub(r'^:::[a-z]+\s*$', '', text, flags=re.MULTILINE)
    # Remove HTML comments
    text = re.sub(r'<!--[\s\S]*?-->', '', text)
    # Remove image syntax
    text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', text)
    return text


def clean_text(text):
    """Clean text by removing metadata, imports, code blocks, HTML/JSX, and markdown syntax.

    Processing order:
    1. Remove frontmatter/metadata headers first
    2. Remove JavaScript/TypeScript imports (for MDX files)
    3. Remove code blocks
    4. Remove HTML/JSX tags
    5. Remove remaining markdown syntax
    """
    text = remove_frontmatter(text)
    text = remove_imports(text)
    text = remove_code_blocks(text)
    text = remove_html_and_jsx(text)
    text = remove_markdown_syntax(text)
    return text


def find_documentation_files(docs_dir):
    """Find all markdown files in the documentation directory.

    Args:
        docs_dir: Path to the documentation directory (can be string or Path object)

    Returns:
        Sorted list of Path objects for all .md and .mdx files found
    """
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        return []

    md_files = list(docs_path.glob('**/*.md'))
    mdx_files = list(docs_path.glob('**/*.mdx'))

    return sorted(md_files + mdx_files)
