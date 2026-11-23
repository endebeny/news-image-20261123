"""Entry for make.fun bounty news-image-20261123.

Copies the pre-drawn front-page image (news-2026-11-23.png, in this
repository) to /output/entry.png.

Deterministic: stdlib only, no network, no randomness, no timestamps.
Running it twice writes byte-identical output. The source is validated
(PNG magic, 1 MiB cap) and the output is written atomically, so a
failed run never leaves a partial entry.png behind.
"""

import hashlib
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "news-2026-11-23.png"
DEST = Path("/output/entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # bounty cap: image at most 1 MiB


def main() -> None:
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("source image is not a PNG file")
    if len(data) > MAX_BYTES:
        raise SystemExit("source image exceeds the 1 MiB cap")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    tmp = DEST.with_suffix(".png.tmp")
    tmp.write_bytes(data)
    os.replace(tmp, DEST)
    digest = hashlib.sha256(DEST.read_bytes()).hexdigest()
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
