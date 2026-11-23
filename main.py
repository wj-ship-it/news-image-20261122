#!/usr/bin/env python3
"""One-click entry point: regenerate the front page and copy it to output.

Usage:
    python3 main.py            # writes out/entry.png
    MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    subprocess.run([sys.executable, str(HERE / "render.py")],
                   check=True, cwd=HERE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", HERE / "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "news-frontpage.png", out_dir / "entry.png")
    print("wrote", out_dir / "entry.png")


if __name__ == "__main__":
    main()
