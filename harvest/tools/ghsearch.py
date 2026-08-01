#!/usr/bin/env python3
"""Thin wrapper over the GitHub code-search API via the authenticated gh CLI."""
import json
import subprocess
import sys
import time
from urllib.parse import quote


def search(q, per_page=20):
    url = f"/search/code?q={quote(q)}&per_page={per_page}"
    for attempt in range(6):
        p = subprocess.run(
            ["gh", "api", "-H", "Accept: application/vnd.github.text-match+json", url],
            capture_output=True,
            text=True,
        )
        if p.returncode == 0:
            return json.loads(p.stdout)
        if "429" in p.stderr or "rate limit" in p.stderr.lower():
            time.sleep(4 + 4 * attempt)
            continue
        return {"error": p.stderr[:400]}
    return {"error": "rate limited"}


if __name__ == "__main__":
    for q in sys.argv[1:]:
        print(f"\n########## {q}")
        d = search(q)
        if "error" in d:
            print("  ERROR:", d["error"])
            continue
        print(f"  total={d.get('total_count')}")
        for it in d.get("items", []):
            print(f"  - {it['repository']['full_name']} :: {it['path']}")
            for m in it.get("text_matches", [])[:2]:
                frag = " ".join(m.get("fragment", "").split())
                print(f"      ~ {frag[:220]}")
        time.sleep(3)
