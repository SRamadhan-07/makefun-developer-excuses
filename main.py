#!/usr/bin/env python3
"""Entry program for make.fun's "Make the AI Judge Laugh: Developer Excuses".

Behaviour: write one funny single-line developer excuse to entry.txt
inside the output directory (MAKEFUN_OUTPUT_DIR, default /output).
The text is written exactly, with no trailing newline, so the file
holds the line and nothing else.
"""

import os

# The excuse in two halves: the denial first, then the confession.
DENIAL = "I didn't push on a Friday. "
CONFESSION = (
    "I pushed on a Thursday at 11:58pm, "
    "which is just Friday wearing a fake moustache."
)

# The competition gate: the entry file must hold 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200

OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def entry_line():
    """Return the exact one-line excuse this entry submits.

    The halves are joined and checked against the gate, so a wording
    edit that drifts outside 1-200 characters fails loudly here
    instead of producing an invalid entry file.
    """
    line = DENIAL + CONFESSION
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError("entry line falls outside the 1-200 character gate")
    return line


def output_path():
    """Resolve the entry.txt path, honouring MAKEFUN_OUTPUT_DIR."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    return os.path.join(directory, OUTPUT_NAME)


def main():
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry_line())


if __name__ == "__main__":
    main()
