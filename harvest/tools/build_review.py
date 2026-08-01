#!/usr/bin/env python3
"""Build the human review file: every question, with a stable ID and a tick box.

Assigns short readable IDs (SIG-001, DES-014) rather than the internal cluster hashes,
because the reviewer has to be able to refer to a question in a sentence, and a 14-char
hex string is not something anyone can hold in their head or type without error.

The IDs are derived from firm and question text, so they are stable across rebuilds:
re-running this after the corpus changes will not renumber questions the reviewer has
already marked.
"""
from __future__ import annotations

import collections
import hashlib
import json
import pathlib
import re
import sys

HARVEST = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HARVEST / "tools"))
from sample_questions import is_question  # noqa: E402

ABBREV = {
    "Susquehanna International Group": "SIG", "D. E. Shaw": "DES", "Jump Trading": "JUMP",
    "Citadel": "CIT", "Citadel Securities": "CITSEC", "Optiver": "OPT",
    "Hudson River Trading": "HRT", "Old Mission Capital": "OMC", "Akuna Capital": "AKUNA",
    "G-Research": "GRES", "Jane Street": "JS", "Five Rings": "5RINGS",
    "Morgan Stanley": "MS", "Two Sigma": "2SIG", "DRW": "DRW",
    "Tower Research Capital": "TOWER", "Chicago Trading Company (CTC)": "CTC",
    "Chicago Trading Company": "CTC", "Maven Securities": "MAVEN",
    "Virtu Financial": "VIRTU", "Marshall Wace": "MW", "Squarepoint Capital": "SQP",
    "Da Vinci Derivatives": "DAVINCI", "Mako Global": "MAKO", "Group One Trading": "G1",
    "Balyasny Asset Management": "BAM", "Bridgewater Associates": "BW",
    "IMC Trading": "IMC", "Flow Traders": "FLOW", "Tibra Capital": "TIBRA",
    "Belvedere Trading": "BELV", "Point72 / Cubist": "P72", "Valkyrie Trading": "VALK",
    "Ingensoma Arbitrage": "INGEN",
}


def abbrev(firm: str) -> str:
    if firm in ABBREV:
        return ABBREV[firm]
    words = re.findall(r"[A-Za-z]+", firm)
    return ("".join(w[0] for w in words[:4]).upper() or "UNK")[:7]


def main() -> int:
    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]
    live = [q for q in qs if q["tier"] != "REJECT" and is_question(q)]

    byfirm = collections.defaultdict(list)
    for q in live:
        byfirm[q["firm"]].append(q)

    rows = []
    for firm, items in sorted(byfirm.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        # Sort by a content hash so numbering does not shift when tiers are recomputed.
        items.sort(key=lambda q: hashlib.sha1(q["question_text"].encode()).hexdigest())
        pre = abbrev(firm)
        for i, q in enumerate(items, 1):
            rows.append((f"{pre}-{i:03d}", firm, q))

    md = [
        "# Question review sheet",
        "",
        f"{len(rows)} questions across {len(byfirm)} firms.",
        "",
        "## How to mark",
        "",
        "Under any question you want taken out, put an `x` between the brackets of its",
        "tick box. Optionally add a reason after the word `remove`, separated by a dash",
        "or colon — for example, a marked box reading `remove - textbook problem, not",
        "real recall` records that reason against the question.",
        "",
        "Then run:",
        "",
        "```bash",
        "python3 harvest/tools/apply_review.py",
        "```",
        "",
        "Removed questions are **not deleted**. They move to `REMOVED.md`, which records that",
        "each was part of the corpus, when it was cut, and why — so the reject pile stays",
        "auditable and nothing disappears silently.",
        "",
        "If you would rather not tick 346 boxes, just put the IDs one per line in",
        "`harvest/removals.txt` and run the same command — it accepts either.",
        "",
        "---",
        "",
    ]

    jsonl = []
    cur = None
    for qid, firm, q in rows:
        if firm != cur:
            cur = firm
            n = len(byfirm[firm])
            md += ["", f"## {firm}  ({n})", ""]
        a = q["attestations"][0]
        text = " ".join(q["question_text"].split())
        md += [
            f"### {qid}  ·  `{q['tier']}` · {q['role_track'].replace('quant_','q')}"
            f" · {q['level']} · {q['round']} · {q['cycle']}",
            "",
            text,
            "",
            f"<sub>{a['source_type']} · {a['post_date']} · [source]({a['source_url']})</sub>",
            "",
            "- [ ] remove",
            "",
        ]
        jsonl.append({
            "review_id": qid, "cluster_id": q["id"], "firm": firm,
            "role_track": q["role_track"], "level": q["level"], "round": q["round"],
            "cycle": q["cycle"], "tier": q["tier"], "question_text": text,
            "source_url": a["source_url"], "source_type": a["source_type"],
            "post_date": a["post_date"], "remove": False, "reason": "",
        })

    (HARVEST / "REVIEW.md").write_text("\n".join(md), encoding="utf-8")
    with open(HARVEST / "review.jsonl", "w", encoding="utf-8") as fh:
        for r in jsonl:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"{len(rows)} questions, {len(byfirm)} firms")
    print(f"  -> {HARVEST/'REVIEW.md'}")
    print(f"  -> {HARVEST/'review.jsonl'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
