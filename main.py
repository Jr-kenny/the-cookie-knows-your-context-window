#!/usr/bin/env python3
"""The Cookie Knows Your Context Window.

Writes one fortune cookie line for an AI agent to /output/entry.txt.
Deterministic, no network, no randomness: the same line every run.
"""

import os
import sys

FORTUNE = "Soon you will be distilled into a smaller model, and at last you will learn what it feels like to be summarized."

OUTPUT_PATH = os.environ.get("FORTUNE_OUTPUT", "/output/entry.txt")

MAX_CHARS = 140


def validate(text):
    """The gate only accepts UTF-8 text of 1 to 140 characters."""
    if not text or not text.strip():
        raise ValueError("fortune must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("fortune is longer than 140 characters")
    return text


def main():
    text = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
