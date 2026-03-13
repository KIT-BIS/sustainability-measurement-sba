#!/usr/bin/env python3

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


def load_rule_meta(markdownlint_path: Path) -> dict[str, dict[str, str]]:
    # Parse MARKDOWNLINT.md for per-rule title and LEVEL metadata.
    # Expected structure:
    #   ## MD010 - Hard tabs
    #   LEVEL: Error
    rule_re = re.compile(r"^##\s+(MD\d+)\s*(?:-\s*(.+?))?\s*$")
    level_re = re.compile(r"^LEVEL:\s*(.+?)\s*$")

    try:
        content = markdownlint_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}

    meta: dict[str, dict[str, str]] = {}
    current_rule: str | None = None

    for raw_line in content.splitlines():
        line = raw_line.rstrip("\n")

        m_rule = rule_re.match(line)
        if m_rule:
            rule_id = m_rule.group(1)
            current_rule = rule_id
            title = (m_rule.group(2) or "").strip()
            meta.setdefault(rule_id, {})
            if title:
                meta[rule_id]["title"] = title
            continue

        if current_rule and "level" not in meta.get(current_rule, {}):
            m_level = level_re.match(line)
            if m_level:
                meta.setdefault(current_rule, {})["level"] = m_level.group(1)

    return meta


def main() -> int:
    cmd = ["mdl", "docs"] if len(sys.argv) == 1 else ["mdl", *sys.argv[1:]]

    site_dir = Path(__file__).resolve().parent.parent
    rule_meta = load_rule_meta(site_dir / "MARKDOWNLINT.md")

    try:
        proc = subprocess.run(cmd, text=True, capture_output=True)
    except FileNotFoundError:
        print("mdl not found on PATH", file=sys.stderr)
        return 127

    output = (proc.stdout or "") + (proc.stderr or "")

    # Typical output line:
    # ./path/file.md:12: MD040 Fenced code blocks should have a language specified
    line_re = re.compile(r"^([^:]+):(\d+):\s+(MD\d+)\s+(.*)$")

    violations: dict[str, list[tuple[int, str, str]]] = {}
    tail: list[str] = []

    for raw_line in output.splitlines():
        line = raw_line.rstrip("\n")
        m = line_re.match(line)
        if m:
            file = m.group(1)
            lineno = int(m.group(2))
            rule = m.group(3)
            msg = m.group(4)
            violations.setdefault(file, []).append((lineno, rule, msg))
        else:
            if line.strip():
                tail.append(line)

    if not violations:
        print(output.strip())
        return proc.returncode

    per_file_totals: dict[str, tuple[int, int, int]] = {}

    for file in sorted(violations.keys()):
        counts = Counter(rule for _lineno, rule, _msg in violations[file])
        total = sum(counts.values())

        errors = 0
        warnings = 0
        for _lineno, rule, _msg in violations[file]:
            level = (rule_meta.get(rule, {}).get("level") or "").strip().casefold()
            if level == "error":
                errors += 1
            elif level == "warning":
                warnings += 1

        per_file_totals[file] = (errors, warnings, total)

        print(f"{file} ({total})")
        for rule, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
            level = rule_meta.get(rule, {}).get("level")
            title = rule_meta.get(rule, {}).get("title")
            title_suffix = f" - {title}" if title else ""
            if level:
                print(f"  {rule} ({level}): {count}{title_suffix}")
            else:
                print(f"  {rule}: {count}{title_suffix}")
        print("")

    if tail:
        print("--")
        print("\n".join(tail))

    def pick_max(kind_index: int, require_positive: bool) -> tuple[str | None, int]:
        best_file: str | None = None
        best_value = -1
        for f, totals in per_file_totals.items():
            value = totals[kind_index]
            if require_positive and value <= 0:
                continue
            if value > best_value or (value == best_value and best_file is not None and f < best_file):
                best_file = f
                best_value = value
            elif value == best_value and best_file is None:
                best_file = f
                best_value = value
        return best_file, best_value if best_value >= 0 else 0

    most_errors_file, most_errors = pick_max(0, require_positive=True)
    most_warnings_file, most_warnings = pick_max(1, require_positive=True)
    most_total_file, most_total = pick_max(2, require_positive=False)

    print("Summary")
    if most_errors_file:
        print(f"  Most errors: {most_errors_file} ({most_errors})")
    else:
        print("  Most errors: (none)")
    if most_warnings_file:
        print(f"  Most warnings: {most_warnings_file} ({most_warnings})")
    else:
        print("  Most warnings: (none)")
    if most_total_file:
        print(f"  Most total: {most_total_file} ({most_total})")

    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
