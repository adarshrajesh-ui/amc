#!/usr/bin/env python3
"""List WSO 'Interview Questions' blocks that no record in the corpus has captured yet."""
import glob
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"
PARTS = glob.glob("/workspace/harvest/raw/_tier_a_parts/p0*.jsonl")

have = []
for p in PARTS:
    for line in open(p, encoding="utf-8"):
        line = line.strip()
        if line:
            have.append(json.loads(line))


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


HAVE_Q = [norm(o["source_quote"]) for o in have] + [norm(o["question_text"]) for o in have]

for f in sorted(glob.glob(os.path.join(CACHE, "*wallstreetoasis*"))):
    t = open(f, encoding="utf-8", errors="replace").read()
    i = t.find("Interview Questions & Answers")
    if i < 0:
        continue
    body = t[i:]
    # entries look like:  #### <role> Interview - <group>  ... Interview Questions\n\n<q>\n\n[Sample Answer]
    blocks = re.split(r"\n#### ", body)
    print("\n" + "=" * 100)
    print(os.path.basename(f))
    for b in blocks[1:]:
        head = b.split("\n")[0].strip()
        m = re.search(r"(?s)\nInterview Questions\s*\n(.*?)(?:\n\[Sample Answer\]|\Z)", b)
        if not m:
            continue
        q = m.group(1).strip()
        if not q:
            continue
        dt = re.search(r"Interviewed:\s*(.+)", b)
        seen = any(norm(q)[:60] and norm(q)[:60] in h for h in HAVE_Q)
        flag = "HAVE" if seen else "NEW "
        print("  [%s] %-52s %-18s | %s" % (flag, head[:52],
                                           (dt.group(1).strip() if dt else "?"),
                                           q.replace("\n", " ")[:190]))
