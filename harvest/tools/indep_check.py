#!/usr/bin/env python3
"""Independent quote checks for hosts this machine can actually reach.

Reddit is fetched from the Arctic Shift public archive (comment/submission ids),
nowcoder over plain HTTP. Everything else is handled by hand via WebFetch/WebSearch.
"""
import html
import json
import re
import sys
import time
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


FULLWIDTH = {
    "，": ",", "。": ".", "；": ";", "：": ":", "？": "?", "！": "!",
    "（": "(", "）": ")", "【": "[", "】": "]", "、": ",", "～": "~",
    "％": "%", "＋": "+", "－": "-", "＝": "=", "／": "/", "＊": "*",
    "《": "<", "》": ">", "「": '"', "」": '"', "…": ".",
}


def norm(s):
    s = html.unescape(s or "")
    s = s.replace("\u200b", "").replace("\ufeff", "")
    s = re.sub(r"[‘’`´]", "'", s)
    s = re.sub(r"[“”]", '"', s)
    s = re.sub(r"[–—−]", "-", s)
    s = re.sub(r"\\", "", s)
    for a, b in FULLWIDTH.items():
        s = s.replace(a, b)
    s = "".join(chr(ord(c) - 0xFEE0) if 0xFF01 <= ord(c) <= 0xFF5E else c for c in s)
    s = re.sub(r"[\s\u3000]+", "", s)
    return s.lower()


def strip_html(doc):
    doc = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", doc)
    doc = re.sub(r"(?s)<[^>]+>", " ", doc)
    return html.unescape(doc)


def longest_common_prefix_frac(quote, hay):
    q, h = norm(quote), norm(hay)
    if q in h:
        return 1.0, len(q)
    lo, hi = 0, len(q)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if q[:mid] in h:
            lo = mid
        else:
            hi = mid - 1
    return lo / max(len(q), 1), lo


def reddit_bodies(url):
    """Return candidate text blobs from Arctic Shift for a reddit permalink."""
    m = re.search(r"/comments/([a-z0-9]+)(?:/[^/]*)?(?:/(?:comment/)?([a-z0-9]{5,10}))?/?$", url)
    if not m:
        return []
    post_id, cmt_id = m.group(1), m.group(2)
    out = []
    if cmt_id and cmt_id != "_":
        d = json.loads(get(f"https://arctic-shift.photon-reddit.com/api/comments/ids?ids={cmt_id}"))
        for c in d.get("data", []):
            out.append(("comment " + c["id"] + " by " + str(c.get("author")) + " link_id=" + str(c.get("link_id")), c.get("body", "")))
        time.sleep(1.5)
    d = json.loads(get(f"https://arctic-shift.photon-reddit.com/api/posts/ids?ids={post_id}"))
    for p in d.get("data", []):
        out.append(("post " + p["id"] + " t=" + str(p.get("title")), (p.get("title", "") + "\n" + (p.get("selftext") or ""))))
    time.sleep(1.5)
    try:
        d = json.loads(get(f"https://arctic-shift.photon-reddit.com/api/comments/tree?link_id={post_id}&limit=2000"))

        def walk(nodes):
            for n in nodes:
                dat = n.get("data") if isinstance(n, dict) and "data" in n else n
                if isinstance(dat, dict):
                    if dat.get("body"):
                        out.append(("thread-comment " + str(dat.get("id")) + " by " + str(dat.get("author")), dat["body"]))
                    for k in ("replies", "children"):
                        if isinstance(dat.get(k), list):
                            walk(dat[k])
        walk(d.get("data", []))
    except Exception as e:
        out.append(("tree-error", str(e)))
    return out


def main():
    sample = json.load(open("/workspace/harvest/reports/_sample45.json"))["sample"]
    want = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    for s in sample:
        url = s["source_url"]
        if want and s["id"] not in want:
            continue
        host = re.sub(r"^https?://", "", url).split("/")[0]
        try:
            if "reddit.com" in host:
                blobs = reddit_bodies(url)
            elif "nowcoder.com" in host:
                blobs = [("page", strip_html(get(url)))]
            else:
                continue
        except Exception as e:
            print(f"{s['id']}  ERROR {type(e).__name__}: {e}\n  {url}\n")
            continue
        best = (0.0, 0, "")
        for label, body in blobs:
            frac, n = longest_common_prefix_frac(s["source_quote"], body)
            if frac > best[0]:
                best = (frac, n, label)
        print(f"{s['id']}  {s['source_type']:14s} blobs={len(blobs)} best_prefix={best[0]:.2%} ({best[1]}/{len(norm(s['source_quote']))} chars) via [{best[2][:70]}]")
        print(f"  {url}")
        if best[0] < 1.0:
            q = norm(s["source_quote"])
            print(f"  matched head : {q[:best[1]][-90:]!r}")
            print(f"  first diverge: {q[best[1]:best[1]+90]!r}")
        print()


if __name__ == "__main__":
    main()
