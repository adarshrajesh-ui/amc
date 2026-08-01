#!/usr/bin/env python3
"""Pull the individual review blocks out of cached Glassdoor interview pages.

Handles both shapes in the cache: r.jina.ai markdown and the search tool's page-text
dump. Each block is date + candidate + outcome + the free-text "Interview" narrative
+ the numbered "Question N" lines.
"""
import glob
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"
DATE = re.compile(r"^(?:###+ )?([A-Z][a-z]{2} \d{1,2}, \d{4})\s*$", re.M)


def demark(t):
    for _ in range(3):
        t = re.sub(r"\[([^\[\]]*?)\]\((?:[^()\s]|\([^()]*\))*\)", r"\1", t)
    t = re.sub(r"!\[[^\]]*\]", " ", t)
    t = re.sub(r"[ \t]+", " ", t)
    return t


def main():
    pat = sys.argv[1] if len(sys.argv) > 1 else "glassdoor"
    for p in sorted(glob.glob(os.path.join(CACHE, "*glassdoor*.txt"))):
        if pat.lower() not in os.path.basename(p).lower():
            continue
        t = demark(open(p, encoding="utf-8", errors="replace").read())
        url = ""
        mu = re.search(r"^URL Source: (\S+)", t, re.M)
        if mu:
            url = mu.group(1)
        # Reviews start after the "companies can't alter or remove interviews" notice.
        i = t.find("companies can't alter or remove")
        body = t[i:] if i > 0 else t
        j = body.find("Viewing 1 -")
        if j > 0:
            body = body[:j]
        marks = list(DATE.finditer(body))
        if not marks:
            continue
        print("#" * 96)
        print(url or os.path.basename(p))
        for k, m in enumerate(marks):
            seg = body[m.start():marks[k + 1].start() if k + 1 < len(marks) else len(body)]
            seg = re.sub(r"\n{2,}", "\n", seg).strip()
            if len(seg) < 80:
                continue
            print("-" * 80)
            print(seg[:1700])


if __name__ == "__main__":
    main()
