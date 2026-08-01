#!/usr/bin/env python3
"""Find every WallStreetOasis per-interview permalink for the Tier-A firms.

The company interview page only ever renders its ten most recent entries in full; the
?page=N views swap a metadata table but keep the same ten write-ups. The individual
/company/<firm>/interview/<slug> pages carry the rest, and the only complete index of
those slugs is the sitemap, which WSO serves through the jina proxy but not to a direct
request. Walk the sitemap index, keep the lines naming one of our firms, and write them
out for the fetcher.
"""
import re
import subprocess
import sys
import time

SLUGS = ["hudson-river-trading-llc", "jump-trading", "drw", "five-rings-capital-llc",
         "akuna-capital-llc", "old-mission-capital", "two-sigma-investments", "de-shaw"]
WANT = re.compile(r"https://www\.wallstreetoasis\.com/company/(%s)/interview/[a-z0-9\-]+"
                  % "|".join(SLUGS))
OUT = "/workspace/harvest/.verify_cache/_wso_permalinks.txt"


def jina(url, tries=3):
    for a in range(1, tries + 1):
        p = subprocess.run(["curl", "-sL", "--max-time", "90", "-A", "Mozilla/5.0",
                            "https://r.jina.ai/" + url], capture_output=True, text=True)
        if len(p.stdout) > 500:
            return p.stdout
        time.sleep(a * 8)
    return ""


def main():
    lo, hi = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1, 40)
    found = set()
    try:
        found = set(open(OUT, encoding="utf-8").read().split())
    except OSError:
        pass
    for page in range(lo, hi + 1):
        body = jina("https://www.wallstreetoasis.com/sitemap.xml?page=%d" % page)
        hits = set(WANT.findall(body) and WANT.pattern and
                   [m.group(0) for m in WANT.finditer(body)])
        new = hits - found
        found |= hits
        print("page %d: %d bytes, %d hits (%d new), %d total"
              % (page, len(body), len(hits), len(new), len(found)), flush=True)
        with open(OUT, "w", encoding="utf-8") as f:
            f.write("\n".join(sorted(found)) + "\n")
        if not body:
            print("  empty -> stopping", flush=True)
            break
        time.sleep(2)


if __name__ == "__main__":
    main()
