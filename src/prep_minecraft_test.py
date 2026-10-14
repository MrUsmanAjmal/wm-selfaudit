"""Extract the held-out test split of the TECO Minecraft dataset without downloading the 225 GB archive.

The archive is one tar file split into 11 parts on the Internet Archive. The training set comes first; the test split
is the last ~2.1 GB, inside the last part. We download only that tail with HTTP range requests, find the first tar
header in it, and read the tar stream from there, keeping minecraft/test/* only.
"""
import hashlib
import json
import os
import sys
import tarfile
import time

import requests

PART = 21474836480
LAST = 10434549760
TOTAL = 10 * PART + LAST
URL = "https://archive.org/download/minecraft_marsh_dataset_ak/minecraft.tar.partak"


class RangeStream:
    """Read-only stream over bytes [start, end) of a URL, resuming after dropped connections."""

    def __init__(self, url, start, end, chunk=1 << 20):
        self.url, self.pos, self.end, self.chunk = url, start, end, chunk
        self.buf, self.resp, self.it = b"", None, None
        self.t0, self.start = time.time(), start

    def _open(self):
        for attempt in range(20):
            try:
                self.resp = requests.get(self.url, headers={"Range": f"bytes={self.pos}-{self.end - 1}"},
                                         stream=True, timeout=60)
                if self.resp.status_code == 206:
                    self.it = self.resp.iter_content(self.chunk)
                    return
                raise IOError(f"HTTP {self.resp.status_code}")
            except Exception as e:
                print(f"  connection problem ({e}); retry {attempt + 1}", flush=True)
                time.sleep(min(60, 5 * (attempt + 1)))
        raise IOError("could not reach the Internet Archive")

    def read(self, n=-1):
        while (n < 0 or len(self.buf) < n) and self.pos < self.end:
            if self.it is None:
                self._open()
            try:
                piece = next(self.it)
            except StopIteration:
                self.it = None
                continue
            except Exception as e:
                print(f"  stream interrupted at {self.pos} ({e}); resuming", flush=True)
                self.it = None
                continue
            self.buf += piece
            self.pos += len(piece)
            done = self.pos - self.start
            if done // (200 << 20) != (done - len(piece)) // (200 << 20):
                print(f"  {done / 2**30:.2f} GiB read, {done / 2**20 / (time.time() - self.t0):.1f} MiB/s", flush=True)
        if n < 0:
            out, self.buf = self.buf, b""
        else:
            out, self.buf = self.buf[:n], self.buf[n:]
        return out


def first_header(url, start, probe=8 << 20):
    """Offset (inside the part) of the first tar header at or after `start`; tar headers sit on 512-byte boundaries."""
    data = requests.get(url, headers={"Range": f"bytes={start}-{start + probe - 1}"}, timeout=60).content
    for k in range((-start) % 512, len(data) - 512, 512):
        h = data[k:k + 512]
        if h[257:262] == b"ustar" and h[156:157] in (b"0", b"5") and h[:10] == b"minecraft/":
            return start + k, h[:100].rstrip(b"\0").decode()
    raise SystemExit("no tar header found; increase the probe size")


def extract_test(out, tail_bytes):
    os.makedirs(out, exist_ok=True)
    start, name = first_header(URL, LAST - tail_bytes)
    print(f"reading the last {(LAST - start) / 2**30:.2f} GiB of the archive, starting at {name}", flush=True)
    stream = RangeStream(URL, start, LAST)
    kept, seen_test = 0, False
    with tarfile.open(fileobj=stream, mode="r|") as tar:
        for m in tar:
            if not m.isfile():
                continue
            if "/test/" not in m.name:
                if seen_test:
                    print(f"  unexpected non-test member after the test split: {m.name}", flush=True)
                continue
            seen_test = True
            rel = m.name.split("/test/", 1)[1]
            dst = os.path.join(out, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with tar.extractfile(m) as src, open(dst, "wb") as f:
                f.write(src.read())
            kept += 1
    if not seen_test:
        raise SystemExit("the test split was not found; increase tail_bytes")
    return kept


def manifest(out):
    import cv2
    videos = []
    for root, _, files in os.walk(out):
        for f in sorted(files):
            if not f.endswith(".mp4"):
                continue
            mp4 = os.path.join(root, f)
            npz = mp4[:-4] + ".npz"
            cap = cv2.VideoCapture(mp4)
            frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            cap.release()
            videos.append(dict(path=os.path.relpath(mp4, out).replace("\\", "/"), has_actions=os.path.exists(npz),
                               frames=frames, bytes=os.path.getsize(mp4),
                               md5=hashlib.md5(open(mp4, "rb").read()).hexdigest()))
    json.dump(dict(source=URL, videos=videos), open(os.path.join(out, "manifest.json"), "w"), indent=1)
    return videos


if __name__ == "__main__":
    out = sys.argv[1]
    tail = int(float(sys.argv[2]) * 2**30) if len(sys.argv) > 2 else int(2.3 * 2**30)
    t0 = time.time()
    n = extract_test(out, tail)
    print(f"extracted {n} files in {(time.time() - t0) / 60:.1f} min")
