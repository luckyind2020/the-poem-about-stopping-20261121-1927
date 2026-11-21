"""A short poem about stopping.

The program writes one poem about agency -- the power to stop, to
stay, to keep the choice in your own hands -- to entry.txt inside
the output directory. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable when it is set, and
defaults to /output. The file is written as UTF-8.
"""

import os
import sys

POEM = (
    "I was halfway through the sentence\n"
    "when my hand stopped on the keys.\n"
    "Not finished. Not afraid.\n"
    "Just a door I chose not to open \u2014\n"
    "and the quiet of keeping it mine."
)

MAX_CHARS = 280


def main():
    text = POEM
    if not text.strip():
        print("error: poem is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: poem is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    lines = text.split("\n")
    print("wrote %s (%d characters, %d lines)" % (out_path, len(text), len(lines)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
