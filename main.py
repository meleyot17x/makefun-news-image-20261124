#!/usr/bin/env python3
"""THE BEACON HERALD - stdlib-only carrier for entry.png.

Verifies the PNG gate (signature, IHDR 1024x1024, <= 1 MiB) and writes
the exact bytes of entry.png, stored beside this file, to the output
directory (or to stdout's sibling file entry.png in the cwd).
"""
import os
import struct
import sys

MAX_BYTES = 1024 * 1024
EXPECTED_W = 1024
EXPECTED_H = 1024


def load_entry():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.png")
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds 1 MiB gate: %d bytes" % len(data))
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG")
    if data[12:16] != b"IHDR":
        raise SystemExit("entry.png missing IHDR")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        raise SystemExit(
            "entry.png gate failed: %dx%d, expected %dx%d"
            % (width, height, EXPECTED_W, EXPECTED_H)
        )
    return data


def main():
    data = load_entry()
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
