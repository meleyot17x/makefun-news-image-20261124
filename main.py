#!/usr/bin/env python3
"""THE SIGNAL TOWER - NI24 entry program (Final 3, @meleyotcok).

Stdlib-only copy carrier: copies the pre-rendered entry.png shipped in this
repository to the grader output directory. The image was drawn in this
session by compose.py (PIL, local render) and is byte-identical across runs.
No network, no third-party packages, no environment secrets.
"""
import os
import shutil
import struct
import sys

SRC_NAME = "entry.png"
MAX_BYTES = 1048576
EXPECT_W = 1024
EXPECT_H = 1024


def fail(message):
    print("main.py: " + message, file=sys.stderr)
    raise SystemExit(1)


def png_size(path):
    with open(path, "rb") as handle:
        head = handle.read(24)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n":
        fail("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        fail("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    if not os.path.isfile(src):
        fail("entry.png missing from repository")
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        fail("entry.png is %d bytes, over the 1048576 limit" % size)
    width, height = png_size(src)
    if (width, height) != (EXPECT_W, EXPECT_H):
        fail("entry.png is %dx%d, expected 1024x1024" % (width, height))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, SRC_NAME)
    shutil.copyfile(src, dst)
    # Verify the copy before reporting success: same size, still a PNG.
    if os.path.getsize(dst) != size:
        fail("copied entry.png is %d bytes, expected %d"
             % (os.path.getsize(dst), size))
    if png_size(dst) != (EXPECT_W, EXPECT_H):
        fail("copied entry.png failed its dimension check")
    print("copied %s (%d bytes, %dx%d) -> %s (verified)"
          % (src, size, width, height, dst))


if __name__ == "__main__":
    main()
