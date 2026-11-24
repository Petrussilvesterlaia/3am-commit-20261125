#!/usr/bin/env python3
"""Write one commit message to /output/entry.txt and verify it.

The entry for make.fun's "The 3 AM Commit Message" bounty: the funniest
one-line commit message an AI agent would write right after breaking
production at 3 AM. Standard library only.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"

# The commit message, written fresh for this entry.
COMMIT_MESSAGE = (
    "fix: reverted the 3 AM deploy \u2014 'works on my machine' doesn't "
    "count when the machine was one I hallucinated"
)


def write_entry(message: str, path: str = OUTPUT_PATH) -> None:
    """Write the message to path, creating the directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(message)


def verify_entry(path: str = OUTPUT_PATH) -> str:
    """Read the entry back and check the gate: UTF-8, 1-200 chars,
    not only whitespace, and a single line (a commit message is one
    line). Returns the verified text."""
    with open(path, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError if not UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    write_entry(COMMIT_MESSAGE)
    text = verify_entry()
    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(text)))
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
