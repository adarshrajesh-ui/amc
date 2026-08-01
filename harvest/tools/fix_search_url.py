#!/usr/bin/env python3
"""Three Akuna records cite a nowcoder *search results* URL rather than the thread they
were read from. The bodies are clearly real (they carry usernames, universities and post
titles), but a search page is dynamic: a verifier re-fetching that URL will not find the
quote, and plain curl returns an empty body because the results are client-rendered.

I could not recover the underlying /discuss/ permalinks, so rather than drop real
material or leave it overstated, downgrade the honesty fields and say so in `doubt`.
"""
import glob
import json
import os

BAD = "nowcoder.com/search"
NOTE = (" PROVENANCE WEAKNESS: source_url is a nowcoder search-results page, not the thread "
        "permalink. The page is client-rendered, so an automated re-fetch of this URL will "
        "not contain the quote; I could not recover the underlying /discuss/ permalink.")

n = 0
for path in sorted(glob.glob("/workspace/harvest/raw/_tier_a_parts/p*.jsonl")):
    out, changed = [], 0
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        o = json.loads(line)
        if BAD in o.get("source_url", ""):
            o["access"] = "snippet_only"
            o["retrieval_method"] = "websearch_snippet"
            if NOTE.strip() not in (o.get("doubt") or ""):
                o["doubt"] = (o.get("doubt") or "").rstrip() + NOTE
            changed += 1
        out.append(json.dumps(o, ensure_ascii=False))
    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
        print("%s: downgraded %d records" % (os.path.basename(path), changed))
        n += changed
print("total %d" % n)
