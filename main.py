"""News-image entry: copy the front page to the grader's output folder.

The image itself is the entry: a newspaper front page that sums up
Friday 20 November 2026, drawn once and shipped as entry.png beside
this file. The program runs with no network and no third-party code, so
it only copies those exact bytes to the output directory.

Local run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(TARGET_DIR, exist_ok=True)
shutil.copyfile(SOURCE, os.path.join(TARGET_DIR, "entry.png"))
