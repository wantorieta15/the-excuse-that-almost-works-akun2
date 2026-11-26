#!/usr/bin/env python3
"""The Excuse That Almost Works — Make Fun bounty entry (Account 2).

Writes exactly one line of plain text to <out_dir>/entry.txt: a rushed
text a gamer sends their boss to skip work during GTA 6 launch week.
The excuse almost works: a boringly specific office-building detail,
and the escape route gets closed by the excuse itself — the lift is
stuck, and the stairs are banned too.

Pure stdlib, no network, no arguments. The entry text is fixed and
validated before writing, so the output is byte-identical every run.
"""

import os

ENTRY = "Lift's been stuck between floors since 7, building manager says don't use the stairs either."

MAX_WORDS = 20
MAX_CHARS = 140


def build_entry() -> str:
    """Return the single-line entry after validating the bounty rules."""
    text = ENTRY.strip()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError("entry has %d words, max is %d" % (len(words), MAX_WORDS))
    if len(text) > MAX_CHARS:
        raise ValueError("entry has %d chars, max is %d" % (len(text), MAX_CHARS))
    if not text.endswith("."):
        raise ValueError("entry must end with a period")
    return text


def write_entry(out_dir: str) -> str:
    """Write the validated entry to <out_dir>/entry.txt, no trailing newline."""
    text = build_entry()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
