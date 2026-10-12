#!/usr/bin/env python3
"""Verify this package's checksums and PNG dimensions using Python 3."""

import hashlib
import json
import struct
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent
    failures = []
    checked = set()
    for line in (root / "checksums.sha256").read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            failures.append(f"Missing or invalid path: {relative}")
            continue
        checked.add(relative)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            failures.append(f"Checksum mismatch: {relative}")
    actual = {
        str(path.relative_to(root))
        for path in root.rglob("*")
        if path.is_file()
        and path.name not in {"checksums.sha256", ".DS_Store"}
        and not {".git", "__pycache__"}.intersection(path.relative_to(root).parts)
    }
    if actual != checked:
        failures.append(f"Unlisted files: {sorted(actual - checked)}")
    info = json.loads((root / "asset-info.json").read_text(encoding="utf-8"))
    image = (root / info["spritesheet"]).read_bytes()
    if image[:8] != b"\x89PNG\r\n\x1a\n" or image[12:16] != b"IHDR":
        failures.append("Spritesheet is not a PNG with an IHDR header")
    elif struct.unpack(">II", image[16:24]) != (info["width"], info["height"]):
        failures.append("Spritesheet dimensions differ from asset-info.json")
    if hashlib.sha256(image).hexdigest() != info["sha256"]:
        failures.append("Spritesheet hash differs from asset-info.json")
    for failure in failures:
        print(failure)
    if failures:
        raise SystemExit(1)
    print(f"Verified {len(checked)} files; spritesheet is {info['width']} x {info['height']}.")


if __name__ == "__main__":
    main()
