"""Download a PDF (or read a local one) and dump its text. Usage: python3 pdf.py <url|path> [outfile]"""
from __future__ import annotations

import io
import sys
import urllib.request

from pypdf import PdfReader

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


def main() -> None:
    src = sys.argv[1]
    if src.startswith("http"):
        req = urllib.request.Request(src, headers={"User-Agent": UA, "Accept": "application/pdf,*/*"})
        with urllib.request.urlopen(req, timeout=120) as fh:
            data = fh.read()
    else:
        data = open(src, "rb").read()
    reader = PdfReader(io.BytesIO(data))
    chunks = []
    for i, page in enumerate(reader.pages):
        chunks.append("\n===== PAGE %d =====\n" % (i + 1) + (page.extract_text() or ""))
    text = "\n".join(chunks)
    if len(sys.argv) > 2:
        open(sys.argv[2], "w", encoding="utf-8").write(text)
        print("wrote %d chars to %s (%d pages)" % (len(text), sys.argv[2], len(reader.pages)))
    else:
        print(text)


if __name__ == "__main__":
    main()
