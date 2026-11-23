"""Entry for make.fun bounty news-image-20261123.

Copies the pre-drawn front-page image (news-2026-11-23.png, in this
repository) to /output/entry.png.

Deterministic: stdlib only, no network, no randomness, no timestamps.
Running it twice writes byte-identical output.
"""

import hashlib
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "news-2026-11-23.png"
DEST = Path("/output/entry.png")


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    digest = hashlib.sha256(DEST.read_bytes()).hexdigest()
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
