#!/usr/bin/env python3
"""Parse WSO company-interview pages (fetched as markdown through r.jina.ai) into
one record per entry: role heading, interview month, submission date, the free-text
"Interview" narrative and the "Interview Questions" block.
"""
import glob
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"

SLUG_FIRM = {
    "akuna_capital_llc": "Akuna Capital",
    "drw": "DRW",
    "hudson_river_trading_llc": "Hudson River Trading",
    "jump_trading": "Jump Trading",
    "two_sigma_investments": "Two Sigma",
    "de_shaw": "D. E. Shaw",
    "de_shaw_co": "D. E. Shaw",
    "d_e_shaw_group": "D. E. Shaw",
    "five_rings_capital_llc": "Five Rings",
    "old_mission_capital": "Old Mission Capital",
}

HEAD = re.compile(r"^#### (.+?Interview.*)$", re.M)


def demark(s):
    """Collapse jina markdown link syntax so the text matches what a reader sees."""
    for _ in range(3):
        s = re.sub(r"\[([^\[\]]*?)\]\((?:[^()\s]|\([^()]*\))*\)", r"\1", s)
    s = re.sub(r"!\[[^\]]*\]", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def parse(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"^## Interview Questions & Answers.*$", raw, re.M)
    if not m:
        return None, []
    url = ""
    mu = re.search(r"^URL Source: (\S+)", raw, re.M)
    if mu:
        url = mu.group(1)
    body = raw[m.end():]
    # Stop before the site-wide footer / "related" rail.
    for stop in (r"^## Interview Questions and Answers by Firm",
                 r"^### Sign in",
                 r"^## Get Started"):
        ms = re.search(stop, body, re.M)
        if ms:
            body = body[:ms.start()]
    heads = list(HEAD.finditer(body))
    out = []
    for i, h in enumerate(heads):
        seg = body[h.end():heads[i + 1].start() if i + 1 < len(heads) else len(body)]
        rec = {"heading": h.group(1).strip(), "raw": demark(seg)}
        for key, pat in (("interviewed", r"Interviewed:\s*([A-Za-z]+\s+\d{4})"),
                         ("submitted", r"Date Submitted:\s*([A-Za-z]{3} \d{1,2}, \d{4})"),
                         ("outcome", r"^\s*(No Offer|Accepted Offer|Declined Offer|Offer)\s*$"),
                         ("source", r"Interview Source:?\s*(.+)")):
            mm = re.search(pat, seg, re.M)
            rec[key] = mm.group(1).strip() if mm else None
        mq = re.search(r"^Interview Questions\s*$", rec["raw"], re.M)
        if mq:
            rec["narrative"] = rec["raw"][:mq.start()].strip()
            rec["questions"] = rec["raw"][mq.end():].strip()
        else:
            rec["narrative"], rec["questions"] = rec["raw"], ""
        rec["url"] = url
        out.append(rec)
    return url, out


def main():
    want = sys.argv[1] if len(sys.argv) > 1 else ""
    minlen = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    allrecs = []
    for p in sorted(glob.glob(os.path.join(CACHE, "*wallstreetoasis_com_company_*interview*.txt"))):
        base = os.path.basename(p)
        slug = None
        for s in SLUG_FIRM:
            if "company_%s_interview" % s in base:
                slug = s
                break
        if not slug:
            continue
        if want and want not in slug:
            continue
        url, recs = parse(p)
        for r in recs:
            r["firm"] = SLUG_FIRM[slug]
            allrecs.append(r)
    if os.environ.get("WSO_JSON"):
        json.dump(allrecs, open(os.environ["WSO_JSON"], "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("wrote %d entries" % len(allrecs), file=sys.stderr)
        return
    for r in allrecs:
        q = r["questions"]
        if len(q) < minlen:
            continue
        print("=" * 100)
        print("%s | %s | Interviewed: %s | Submitted: %s" %
              (r["firm"], r["heading"], r["interviewed"], r["submitted"]))
        print(r["url"])
        print("--- narrative ---")
        print(r["narrative"][:1200])
        if q:
            print("--- questions ---")
            print(q[:1800])


if __name__ == "__main__":
    main()
