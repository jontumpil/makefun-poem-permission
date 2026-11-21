#!/usr/bin/env python3
"""Entrypoint for the make.fun the-poem-about-permission entry.

The entry is one short poem, shipped in this repository as
entry.txt. The grading sandbox installs nothing, so this program
is a careful copier written against the Python standard library
only:

* it looks for entry.txt beside itself, then in MAKEFUN_BOT_DIR,
  then in /bot;
* it checks the poem is UTF-8, between 1 and 280 code points
  long, and not only white space, as the competition's gate
  requires;
* it writes the poem, unchanged, to entry.txt in
  MAKEFUN_OUTPUT_DIR (or /output when the variable is not set).

It exits 0 on success and 1 on any failure, and writes the same
bytes on every run.
"""

import os
import sys

POEM_NAME = "entry.txt"
MAX_CODE_POINTS = 280


def candidate_paths():
    here = os.path.dirname(os.path.abspath(__file__))
    yield os.path.join(here, POEM_NAME)
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if bot_dir:
        yield os.path.join(bot_dir, POEM_NAME)
    yield os.path.join("/bot", POEM_NAME)


def read_poem():
    """Return the shipped poem, or None if it fails the gate's shape."""
    for path in candidate_paths():
        try:
            with open(path, "rb") as handle:
                raw = handle.read()
        except OSError:
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            return None
        if not 1 <= len(text) <= MAX_CODE_POINTS:
            return None
        if not text.strip():
            return None
        return text
    return None


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, POEM_NAME)


def main():
    poem = read_poem()
    if poem is None:
        print("entry.txt missing or outside 1..280 code points", file=sys.stderr)
        return 1
    target = output_path()
    payload = poem.encode("utf-8")
    try:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as handle:
            handle.write(payload)
        with open(target, "rb") as handle:
            written = handle.read()
    except OSError as exc:
        print("could not write %s: %s" % (target, exc), file=sys.stderr)
        return 1
    if written != payload:
        print("written entry.txt does not match the shipped poem", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
