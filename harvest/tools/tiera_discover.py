#!/usr/bin/env python3
"""URL discovery across Bing / Baidu / Sogou.

Cursor's WebSearch returns long verbatim excerpts but few links; these engines return
many links but short excerpts. So they are used for opposite jobs: this script finds
candidate thread URLs (especially on Chinese forums, which Google-backed search indexes
poorly), and the excerpt work happens elsewhere against the actual page.

Baidu and Sogou wrap results in redirector links, which are resolved here so the output
is a real thread URL a verifier could re-fetch.
"""
import html as _html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HDRS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}
OUT = "/workspace/harvest/raw/_tiera_discover"
os.makedirs(OUT, exist_ok=True)


def fetch(url, timeout=30):
    import gzip, io
    req = urllib.request.Request(url, headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                d = gzip.GzipFile(fileobj=io.BytesIO(d)).read()
            cs = r.headers.get_content_charset() or "utf-8"
            return d.decode(cs, "replace")
    except Exception as e:
        sys.stderr.write(f"  fetchfail {type(e).__name__} {url[:90]}\n")
        return ""


def strip(s):
    s = re.sub(r"<[^>]+>", "", s)
    return _html.unescape(s).strip()


def bing(q, pages=2):
    out = []
    for p in range(pages):
        u = f"https://www.bing.com/search?q={urllib.parse.quote(q)}&first={p*10+1}&setlang=zh-CN"
        h = fetch(u)
        for m in re.finditer(r'<li class="b_algo".*?</li>', h, re.S):
            blk = m.group(0)
            a = re.search(r'<h2>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', blk, re.S)
            if not a:
                continue
            cap = re.search(r'<p[^>]*>(.*?)</p>', blk, re.S)
            out.append({"url": a.group(1), "title": strip(a.group(2)),
                        "snippet": strip(cap.group(1)) if cap else "", "engine": "bing"})
        time.sleep(1.2)
    return out


def baidu(q, pages=2):
    out = []
    for p in range(pages):
        u = f"https://www.baidu.com/s?wd={urllib.parse.quote(q)}&pn={p*10}"
        h = fetch(u)
        # Baidu puts the real destination in a data attribute on the result container;
        # the visible href is a /link?url= redirector that costs an extra request each.
        for m in re.finditer(r'<div[^>]+class="result[^"]*"[^>]*>(.*?)(?=<div[^>]+class="result|<div id="page)', h, re.S):
            blk = m.group(1)
            a = re.search(r'<a[^>]+href="(http[^"]+)"[^>]*>(.*?)</a>', blk, re.S)
            mu = re.search(r'mu="([^"]+)"', blk)
            if not a:
                continue
            out.append({"url": mu.group(1) if mu else a.group(1),
                        "title": strip(a.group(2)),
                        "snippet": strip(blk)[:400], "engine": "baidu"})
        time.sleep(1.5)
    return out


def sogou(q, pages=2):
    out = []
    for p in range(pages):
        u = f"https://www.sogou.com/web?query={urllib.parse.quote(q)}&page={p+1}"
        h = fetch(u)
        for m in re.finditer(r'<div class="vrwrap">(.*?)</div>\s*</div>\s*</div>', h, re.S):
            blk = m.group(1)
            a = re.search(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', blk, re.S)
            if not a:
                continue
            href = a.group(1)
            if href.startswith("/link?"):
                href = "https://www.sogou.com" + href
            out.append({"url": href, "title": strip(a.group(2)),
                        "snippet": strip(blk)[:400], "engine": "sogou"})
        time.sleep(1.5)
    return out


QUERIES = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else []
store_path = f"{OUT}/results.json"
try:
    store = json.load(open(store_path))
except Exception:
    store = {}

for q in QUERIES:
    if q in store:
        continue
    rows = []
    for fn in (bing, baidu, sogou):
        try:
            rows += fn(q)
        except Exception as e:
            sys.stderr.write(f"  engfail {fn.__name__} {e}\n")
    store[q] = rows
    sys.stderr.write(f"[q] {q}  -> {len(rows)}\n")
    json.dump(store, open(store_path, "w"), ensure_ascii=False)

json.dump(store, open(store_path, "w"), ensure_ascii=False)
print("QUERIES", len(store))
