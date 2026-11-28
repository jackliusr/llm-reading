#!/usr/bin/env python3
"""Convert dates like "01 Jun 2026" to ISO format in Markdown files."""

import argparse
import re
from collections.abc import Iterator
from datetime import datetime
from pathlib import Path


DATE_PATTERN = re.compile(r"(?<!\d)(\d{2} [A-Z][a-z]{2} \d{4})(?!\d)")
MARKDOWN_SUFFIXES = {".md", ".markdown"}


def normalize_dates(text: str) -> str:
    """Replace valid dates in day-month-year format with ISO dates."""

    def replace(match: re.Match[str]) -> str:
        try:
            date = datetime.strptime(match.group(1), "%d %b %Y")
        except ValueError:
            return match.group(1)
        return date.strftime("%Y-%m-%d")

    return DATE_PATTERN.sub(replace, text)


def markdown_files(root: Path) -> Iterator[Path]:
    """Yield Markdown files below root, excluding Git metadata."""
    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and path.suffix.lower() in MARKDOWN_SUFFIXES:
            yield path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert dates like '01 Jun 2026' to '2026-06-01' in Markdown files."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=Path("."),
        help="directory to scan recursively (default: current directory)",
    )
    args = parser.parse_args()

    if not args.directory.is_dir():
        parser.error(f"not a directory: {args.directory}")

    updated = 0
    for path in markdown_files(args.directory):
        with path.open("r", encoding="utf-8", newline="") as file:
            original = file.read()
        normalized = normalize_dates(original)
        if normalized != original:
            with path.open("w", encoding="utf-8", newline="") as file:
                file.write(normalized)
            print(f"Updated {path}")
            updated += 1

    print(f"Updated {updated} Markdown file(s).")


if __name__ == "__main__":
    main()