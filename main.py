#!/usr/bin/env python3
"""One letter for your day — a make.fun entry.

The program writes exactly one letter to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): P, the initial of the word behind the
entry — plot-twisted, a day that kept scheduling plot twists before
coffee. The competition takes exactly one character, a letter from A
to Z standing for the word that describes the sender's day, and its
gate is UTF-8 text of exactly 1 character. Standard library only, no
network, and deterministic: the same byte on every run.
"""

import os

LINE = "P"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the one letter: no trailing newline,
    # so the text the judge reads is the letter itself, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
