#!/usr/bin/env python3
"""Crawl XenForo thread URLs and extract post bodies, keeping the raw HTML."""
import concurrent.futures as cf
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


def get(url, outdir):
    h = hashlib.sha1(url.encode()).hexdigest()[:16]
    hp = os.path.join(outdir, h + ".html")
    if os.path.exists(hp) and os.path.getsize(hp) > 2000:
        return hp
    p = subprocess.run(
        ["curl", "-sSL", "--max-time", "35", "-A", UA, url],
        capture_output=True,
        text=True,
        errors="replace",
    )
    if p.returncode != 0 or len(p.stdout) < 2000:
        return None
    open(hp, "w").write(p.stdout)
    return hp


def posts_of(path):
    raw = open(path, errors="replace").read()
    url = ""
    m = re.search(r'<link rel="canonical" href="([^"]+)"', raw)
    if m:
        url = m.group(1)
    out = []
    for p in re.findall(r'(?is)<div class="bbWrapper">(.*?)</article>', raw):
        t = re.sub(r"(?is)<blockquote.*?</blockquote>", " ", p)
        t = re.sub(r"(?is)<br\s*/?>", "\n", t)
        t = re.sub(r"(?s)<[^>]+>", " ", t)
        t = html.unescape(t)
        t = re.sub(r"[ \t\xa0]+", " ", t).strip()
        if len(t) > 60:
            out.append(t)
    return url, out


if __name__ == "__main__":
    listfile, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    urls = [u.strip() for u in open(listfile) if u.strip()]
    print(f"crawling {len(urls)} urls -> {outdir}", flush=True)
    done = 0
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for path in ex.map(lambda u: get(u, outdir), urls):
            done += 1
            if done % 50 == 0:
                print(f"  {done}/{len(urls)}", flush=True)
    print("crawl complete", flush=True)
