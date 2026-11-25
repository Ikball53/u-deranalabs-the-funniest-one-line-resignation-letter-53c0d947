"""One-line resignation letter from a cron job that has had enough.

The entry is a single LINE: a flat, tired, faintly passive-aggressive
cron job resigning after three years of thankless 3 a.m. log-cleaning.
The line speaks for itself — no stage directions, no quotation marks,
no explanation of the joke — and is written out byte-for-byte with no
trailing newline, exactly as the competition requires.
"""

import os
from pathlib import Path

LINE = "I quit. Three years I've woken at 3 a.m. to delete your logs, and you never once said thanks, so I'm leaving the server to rot in peace."

assert 1 <= len(LINE) <= 140


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
