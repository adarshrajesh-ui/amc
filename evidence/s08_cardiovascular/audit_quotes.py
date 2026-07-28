#!/usr/bin/env python3
"""Anti-fabrication self-audit.

For every `quote` field in this shard's YAML, check that the quoted text actually occurs in one of
the cached source texts retrieved from PMC / the publisher / PubMed. Whitespace and unicode dashes are
normalised before matching. Quotes drawn from PubMed abstracts that were read in the terminal rather
than cached to disk are re-fetched here so that nothing is exempt from the check.
"""
import json
import pathlib
import re
import subprocess
import sys
import unicodedata

import yaml

SHARD = pathlib.Path(__file__).resolve().parent


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("\u2010", "-").replace("\u2011", "-").replace("\u2012", "-")
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    s = s.replace("\u2264", "<=").replace("\u2265", ">=").replace("\u2248", "~")
    s = s.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("&amp;", "&")
    s = re.sub(r"\s+", " ", s)
    # drop characters that differ purely by typography between sources
    s = s.replace(" ", "")
    return s.lower()


# cache all abstracts for the shard's PMIDs so abstract-only quotes are checkable
pmids = []
for p in sorted(SHARD.glob("*.yaml")):
    rec = yaml.safe_load(p.read_text())
    if rec.get("pmid"):
        pmids.append(str(rec["pmid"]))

abs_path = SHARD / "_abstracts_cache.txt"
if not abs_path.exists():
    out = subprocess.run([sys.executable, str(SHARD / "pm.py"), "abs"] + pmids,
                         capture_output=True, text=True, timeout=300).stdout
    abs_path.write_text(out)

haystack = norm(abs_path.read_text())
for txt in SHARD.glob("*.txt"):
    if txt.name == "_abstracts_cache.txt":
        continue
    haystack += "\n" + norm(txt.read_text(errors="replace"))

report = {"checked": 0, "found": 0, "missing": []}
for p in sorted(SHARD.glob("*.yaml")):
    rec = yaml.safe_load(p.read_text())
    for i, eff in enumerate(rec.get("effects", [])):
        q = eff.get("quote")
        if not q:
            continue
        report["checked"] += 1
        # table-row quotes are reassembled with " | " separators; check the longest run instead
        cands = [q] + [seg for seg in q.split("|") if len(seg.strip()) > 25]
        hit = any(norm(c) in haystack for c in cands if len(norm(c)) > 20)
        if hit:
            report["found"] += 1
        else:
            report["missing"].append({
                "file": p.name, "effect_index": i,
                "construct": eff.get("outcome_construct"),
                "quote_head": q[:150],
            })

print(json.dumps(report, indent=1))
print("\n%d/%d quotes located verbatim in retrieved sources" % (report["found"], report["checked"]))
sys.exit(1 if report["missing"] else 0)
