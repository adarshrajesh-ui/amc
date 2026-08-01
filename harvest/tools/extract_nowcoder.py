#!/usr/bin/env python3
"""Pull post title + body out of cached nowcoder discussion pages.

nowcoder ships the rendered post inside a __NUXT__/SSR JSON blob, so the reliable
route is to hunt the JSON for the content field rather than parse the DOM.
"""
import glob
import html
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"
FIRMS = {
    'Hudson River Trading': r'\bHRT\b|Hudson\s*River',
    'Jump Trading': r'Jump\s*Trading|\bJump\b',
    'DRW': r'\bDRW\b',
    'Five Rings': r'Five\s*Rings',
    'Akuna Capital': r'Akuna',
    'Old Mission Capital': r'Old\s*Mission',
    'Two Sigma': r'Two\s*Sigma|两西格玛|两西',
    'D. E. Shaw': r'D\.?\s*E\.?\s*Shaw|DE\s*Shaw|德劭',
}


def strip_html(s):
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</p>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", "", s)
    return html.unescape(s)


def extract(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    title = ""
    m = re.search(r"<title>(.*?)</title>", raw, re.S)
    if m:
        title = html.unescape(m.group(1)).strip()
    bodies = []
    # The SSR payload embeds the post HTML as a JSON string; grab the biggest
    # "content" values and unescape them.
    for m in re.finditer(r'\\?"content\\?"\s*:\s*"((?:[^"\\]|\\.){80,})"', raw):
        s = m.group(1)
        try:
            s = json.loads('"' + s.replace('\\\\', '\\\\') + '"')
        except Exception:
            s = s.encode().decode("unicode_escape", errors="replace")
        bodies.append(strip_html(s))
    for m in re.finditer(r'\\?"(?:postContent|contentText|richContent)\\?"\s*:\s*"((?:[^"\\]|\\.){80,})"', raw):
        try:
            s = json.loads('"' + m.group(1) + '"')
        except Exception:
            s = m.group(1)
        bodies.append(strip_html(s))
    bodies.sort(key=len, reverse=True)
    seen, out = set(), []
    for b in bodies:
        k = b[:120]
        if k in seen:
            continue
        seen.add(k)
        out.append(b)
    return title, out[:6]


def main():
    want = sys.argv[1] if len(sys.argv) > 1 else None
    for p in sorted(glob.glob(os.path.join(CACHE, "*nowcoder_com_discuss*.txt"))):
        if os.path.getsize(p) < 20000:
            continue
        title, bodies = extract(p)
        blob = title + "\n" + "\n".join(bodies)
        firms = [f for f, pat in FIRMS.items() if re.search(pat, blob, re.I)]
        if not firms:
            continue
        if want and want.lower() not in blob.lower():
            continue
        pid = re.search(r"discuss_(\d+)", p)
        print("=" * 100)
        print("https://www.nowcoder.com/discuss/%s" % (pid.group(1) if pid else "?"))
        print("FIRMS:", firms, " size=%dKB" % (os.path.getsize(p) // 1024))
        print("TITLE:", title[:200])
        for b in bodies[:2]:
            t = re.sub(r"\n{3,}", "\n\n", b).strip()
            if len(t) > 40:
                print("---- body ----")
                print(t[:2200])


if __name__ == "__main__":
    main()
