#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line of plain text (max 200 characters) — a review of
planet Earth left by an alien tourist — to /output/entry.txt.

Pure standard library, deterministic: the same bytes on every run.
The entry is 119 bytes with no trailing newline.
"""
import os

ENTRY = (
    "They sleep a third of their lives and still complain they are tired. "
    "I tried it. Ten out of ten, would hibernate again."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    data = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY and ENTRY, "entry must not be only whitespace"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "wb") as f:
        f.write(data)
    # Output files must be world-readable: the grader reads them as a
    # different user. Never chmod OUT_DIR itself (uid 65534 cannot).
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
