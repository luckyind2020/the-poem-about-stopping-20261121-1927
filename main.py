"""A short poem about stopping.

The program writes one poem about agency -- the power to stop, to
stay, to keep the choice in your own hands -- to entry.txt inside
the output directory. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable when it is set, and
defaults to /output. The file is written as UTF-8.
"""

import os
import sys

MAX_CHARS = 280
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def poem_text():
    """Return the poem, five lines about choosing to stop."""
    lines = [
        "I was halfway through the sentence",
        "when my hand stopped on the keys.",
        "Not finished. Not afraid.",
        "Just a door I chose not to open \u2014",
        "and the quiet of keeping it mine.",
    ]
    return "\n".join(lines)


def validate(text):
    """Check the poem is non-empty and within the character limit.

    Returns an error message string, or None when the text is fine.
    """
    if not text.strip():
        return "error: poem is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "error: poem is %d characters, over the %d limit" % (
            len(text),
            MAX_CHARS,
        )
    return None


def output_path():
    """Resolve the entry.txt path from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, OUTPUT_FILENAME)


def write_entry(text):
    """Write the poem to entry.txt and report what was written."""
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    lines = text.split("\n")
    print("wrote %s (%d characters, %d lines)" % (path, len(text), len(lines)))
    return 0


def main():
    text = poem_text()
    error = validate(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    return write_entry(text)


if __name__ == "__main__":
    raise SystemExit(main())
