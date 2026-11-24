"""One Line, One Chill — entry program.

Writes a single original horror sentence to /output/entry.txt
(or $OUTPUT_DIR / $MAKEFUN_OUTPUT_DIR when set).

The line is the duel winner of six original drafts, judged pairwise
on the bounty brief: fright first, then vividness, originality, craft.
"""

import os
import sys

LINE = "The dentist found a second set of teeth growing behind mine, and they were already chewing."


def check(line: str) -> None:
    """Gate self-check: one line, 1-200 chars, not whitespace only."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry length {len(line)} outside 1-200")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.strip():
        raise SystemExit("entry must not be whitespace only")


def main() -> int:
    check(LINE)
    out_dir = (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Verify what was actually written, not just what we meant to write.
    with open(path, encoding="utf-8") as f:
        check(f.read().rstrip("\n"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
