#!/usr/bin/env python3
"""Print the text around each Tier-A firm mention inside cached nowcoder pages.

The whole-page extractor drowns in nowcoder's recommendation rail, so instead of
trying to isolate "the post", pull a window around every firm mention and let me
read whether it is a recall or a sidebar link.
"""
import glob
import html
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"
FIRMS = {
    'HRT': r'HRT|Hudson\s*River',
    'Jump': r'Jump\s*Trading',
    'DRW': r'DRW',
    'FiveRings': r'Five\s*Rings',
    'Akuna': r'[Aa]kuna',
    'OldMission': r'Old\s*Mission',
    'TwoSigma': r'Two\s*Sigma|两西格玛',
    'DEShaw': r'D\.?\s*E\.?\s*Shaw|DE\s*Shaw|德劭',
}
PAT = re.compile("|".join(FIRMS.values()))


def clean(raw):
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    # The SSR payload stores Chinese as \uXXXX inside JSON strings. Decode just those
    # escapes; a full unicode_escape pass would destroy the already-UTF-8 body text.
    raw = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), raw)
    raw = raw.replace("\\n", "\n").replace("\\t", " ").replace('\\"', '"').replace("\\/", "/")
    raw = re.sub(r"[ \t\u00a0]+", " ", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw


def main():
    W = int(sys.argv[1]) if len(sys.argv) > 1 else 900
    only = sys.argv[2] if len(sys.argv) > 2 else None
    for p in sorted(glob.glob(os.path.join(CACHE, "*nowcoder_com_discuss*.txt"))):
        if os.path.getsize(p) < 20000:
            continue
        pid = re.search(r"discuss_(\d+)", p)
        pid = pid.group(1) if pid else "?"
        if only and only not in pid:
            continue
        raw = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r"<title>(.*?)</title>", raw, re.S)
        title = html.unescape(m.group(1)).strip() if m else ""
        txt = clean(raw)
        hits = list(PAT.finditer(txt))
        if not hits:
            continue
        print("#" * 100)
        print("https://www.nowcoder.com/discuss/%s   %s   hits=%d" % (pid, title[:90], len(hits)))
        shown = []
        for h in hits:
            s, e = max(0, h.start() - W // 3), min(len(txt), h.end() + W)
            if any(abs(s - x) < W // 2 for x in shown):
                continue
            shown.append(s)
            seg = txt[s:e].strip()
            print("-" * 80)
            print(seg)
            if len(shown) >= 4:
                break


if __name__ == "__main__":
    main()
