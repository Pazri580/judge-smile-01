#!/usr/bin/env python3
"""Write one warm line about a small good thing today to /output/entry.txt.

The line is fixed text: short (1-200 characters), a single line, and not
only whitespace. The program checks the text against those bounds before
writing anything, so an out-of-range line fails loudly instead of being
submitted half-formed. Validation is collected up front so every problem
is reported at once instead of one at a time.
"""

import os
import sys

LINE = (
    "The neighbor left a mango on my doorstep with a note that just said "
    "'too many' — I ate it standing in the hallway, juice on my chin, "
    "grinning like I'd won something."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> list[str]:
    """Return every way the text breaks the entry gate, or [] when it is valid."""
    problems: list[str] = []
    if not text.strip():
        problems.append("entry is only whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        problems.append(
            f"entry is {len(text)} characters, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    return problems


def main() -> int:
    problems = validate(LINE)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
