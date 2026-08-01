#!/usr/bin/env python3
"""Draw the stratified verification sample used by reports/independent_verification.json.

Seed is fixed so the draw is reproducible by anyone re-running this file.
"""
import json
import random
from collections import defaultdict

SEED = 42
SIG = "Susquehanna International Group"

SIG_QUOTA = {
    "glassdoor": 3,
    "reddit_thread": 2,
    "1point3acres": 2,
    "chat_telegram": 2,
    "wso": 2,
    "blog": 1,
    "github_repo": 1,
    "university_bbs": 1,
    "blind": 1,
}
OTHER_QUOTA = {
    "blog": 4,
    "wso": 4,
    "chat_telegram": 3,
    "nowcoder": 3,
    "1point3acres": 3,
    "reddit_thread": 2,
    "glassdoor": 2,
    "interview_review_site": 2,
    "interview_review_db": 2,
    "university_bbs": 2,
    "blind": 1,
    "firm_official_pdf": 1,
    "other": 1,
}

records = []
with open("/workspace/harvest/questions.jsonl") as fh:
    for line in fh:
        line = line.strip()
        if line:
            records.append(json.loads(line))

by_stratum = defaultdict(list)
for rec in records:
    bucket = "sig" if rec["firm"] == SIG else "other"
    seen = set()
    for att in rec.get("attestations", []):
        st = att.get("source_type", "?")
        if st in seen:
            continue
        seen.add(st)
        by_stratum[(bucket, st)].append((rec, att))

rng = random.Random(SEED)
picked = []
picked_ids = set()
# Spread the non-SIG draw over firms rather than letting one firm dominate.
firm_used = defaultdict(int)


def draw(bucket, quota, firm_cap):
    for stype in sorted(quota):
        pool = sorted(by_stratum[(bucket, stype)], key=lambda p: (p[0]["id"], p[1]["source_url"]))
        rng.shuffle(pool)
        taken = 0
        for cap in (firm_cap, 99):
            for rec, att in pool:
                if taken >= quota[stype]:
                    break
                if rec["id"] in picked_ids or firm_used[rec["firm"]] >= cap:
                    continue
                picked.append((rec, att))
                picked_ids.add(rec["id"])
                firm_used[rec["firm"]] += 1
                taken += 1
            if taken >= quota[stype]:
                break


draw("sig", SIG_QUOTA, 99)
draw("other", OTHER_QUOTA, 3)

out = []
for rec, att in picked:
    out.append(
        {
            "id": rec["id"],
            "firm": rec["firm"],
            "source_type": att.get("source_type"),
            "source_url": att.get("source_url"),
            "source_quote": att.get("source_quote"),
            "question_text": rec.get("question_text"),
            "post_date": att.get("post_date"),
            "retrieval_method": att.get("retrieval_method"),
            "access": att.get("access"),
        }
    )

with open("/workspace/harvest/reports/_sample45.json", "w") as fh:
    json.dump({"seed": SEED, "sample_size": len(out), "sample": out}, fh, indent=1, ensure_ascii=False)

print(f"seed={SEED} n={len(out)}")
for i, s in enumerate(out):
    print(f"{i:3d} {s['source_type']:22s} {s['firm'][:34]:34s} {s['id']} {s['source_url'][:80]}")
