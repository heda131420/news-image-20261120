"""Ship the finished front page to the grader.

The picture is the entry: a one-page newspaper that sums up Friday
20 November 2026, rendered once and stored here as entry.png. The
grader runs this file with no network and nothing beyond the standard
library, so the program only places those exact bytes in the output
folder the grader provides. Run it locally with
MAKEFUN_OUTPUT_DIR=out python3 main.py to see the same result."""

from os import environ
from pathlib import Path

HERE = Path(__file__).resolve().parent
PICTURE = HERE / "entry.png"


def main() -> None:
    if not PICTURE.is_file():
        raise SystemExit("entry.png is missing next to main.py")
    target_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.png").write_bytes(PICTURE.read_bytes())


if __name__ == "__main__":
    main()
