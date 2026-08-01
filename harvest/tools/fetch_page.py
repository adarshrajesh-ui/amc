#!/usr/bin/env python3
"""Fetch a URL and dump a plain-text rendering next to the raw HTML.

Keeps the raw bytes so quotes can be verified character-for-character later.
"""
import hashlib
import html
import os
import re
import subprocess
import sys

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
OUT = "/workspace/harvest/.pc2/pages"


def slug(url):
    return hashlib.sha1(url.encode()).hexdigest()[:16]


def to_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?is)<br\s*/?>", "\n", raw)
    raw = re.sub(r"(?is)</(p|div|li|tr|h[1-6]|blockquote|article)>", "\n", raw)
    txt = re.sub(r"(?s)<[^>]+>", " ", raw)
    txt = html.unescape(txt)
    txt = re.sub(r"[ \t\xa0]+", " ", txt)
    txt = re.sub(r"\n\s*\n\s*\n+", "\n\n", txt)
    return txt.strip()


def fetch(url):
    os.makedirs(OUT, exist_ok=True)
    s = slug(url)
    hp, tp = f"{OUT}/{s}.html", f"{OUT}/{s}.txt"
    if not os.path.exists(hp):
        p = subprocess.run(
            ["curl", "-sSL", "--max-time", "45", "-A", UA, url],
            capture_output=True,
            text=True,
            errors="replace",
        )
        if p.returncode != 0 or not p.stdout:
            return None, f"FAIL {url} rc={p.returncode}"
        open(hp, "w").write(p.stdout)
    txt = to_text(open(hp, errors="replace").read())
    open(tp, "w").write(f"URL: {url}\n\n{txt}")
    return tp, f"OK {len(txt)}B {url}"


if __name__ == "__main__":
    for u in sys.argv[1:]:
        path, msg = fetch(u)
        print(msg, "->", path)
