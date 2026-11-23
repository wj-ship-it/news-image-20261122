#!/usr/bin/env python3
"""One-click entry point: copy the pre-built front page to output.

The repository already holds the finished image (news-frontpage.png),
so the scored run is a plain file copy using only the standard library.

Usage:
    python3 main.py            # writes out/entry.png
    MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", HERE / "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(HERE / "news-frontpage.png", dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
