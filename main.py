#!/usr/bin/env python3
"""The Excuse That Almost Works — Make Fun bounty entry (Account 2).

Writes a single line of plain text to <out_dir>/entry.txt:
a rushed text a gamer sends their boss to skip work during
GTA 6 launch week. Pure stdlib, no network.
"""

import os

ENTRY = "Lift's been stuck between floors since 7, building manager says don't use the stairs either."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
