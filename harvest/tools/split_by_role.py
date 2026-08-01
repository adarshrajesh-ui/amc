#!/usr/bin/env python3
"""Partition the corpus into one file per role track.

Role track is the split that matters most here because the tracks sit different
assessments -- at SIG the developer track takes a CodeSignal coding OA while trader and
researcher candidates take the same 17-question maths paper -- so mixing them produces a
practice set that is wrong for whoever reads it.

Every question lands in exactly one file, including the ones whose track was never
established. Those get their own file rather than being dropped or guessed at.
"""
from __future__ import annotations

import collections
import json
import pathlib
import re
import sys

HARVEST = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HARVEST / "tools"))
from sample_questions import is_question  # noqa: E402

CJK = re.compile(r"[\u4e00-\u9fff]")
TIER = {"A": 0, "B": 1, "C": 2, "D": 3}

TRACKS = {
    "quant_trader": (
        "QTRADER.md", "Quant trader questions",
        "The trading track: probability, expected value, market making, mental arithmetic, "
        "estimation and game theory. At SIG this track sits the same 17-question / 60-minute "
        "maths paper as quant research, so the two sets are worth reading together.",
    ),
    "quant_researcher": (
        "QRESEARCH.md", "Quant researcher questions",
        "The research track: statistics, regression, stochastic processes, modelling and "
        "data tasks. Overlaps heavily with the trader track at firms that run one paper for "
        "both.",
    ),
    "quant_developer": (
        "QDEV.md", "Quant developer / software engineering questions",
        "The developer and SWE tracks, a genuinely different assessment from the trading and "
        "research pipelines. This set is the largest because developer-track recall is shared "
        "far more freely, not because these firms mostly ask coding questions.",
    ),
    "quant_analyst": (
        "QANALYST.md", "Quant analyst questions",
        "A small set, and the track label is the least consistently applied of the four — "
        "several of these could reasonably be filed as trader or researcher.",
    ),
    "unknown": (
        "ROLE_UNKNOWN.md", "Questions with no established role track",
        "The source never stated which track these came from, so they were left unlabelled "
        "rather than guessed at. **If you are preparing for a trading seat, read this file "
        "as well as QTRADER.md** — a good share of it is probably trader material that the "
        "poster simply did not label.",
    ),
}


def flat(s) -> str:
    return " ".join(str(s or "").split())


# Collectors recorded "no answer given" as free text in several languages rather than as
# null, so rendering the field naively prints "Reported answer: not stated", which reads
# like an answer and wastes the reader's eye on 188 records.
_NULLISH = re.compile(
    r"^(not\s+(stated|given|recovered|provided|applicable|available)|n/?a\b|none|unknown"
    r"|未给答案|不适用|没有答案)", re.I)


def real_answer(s) -> str:
    t = flat(s)
    return "" if not t or _NULLISH.match(t) else t


def render(track_key, title, blurb, items, total):
    byfirm = collections.defaultdict(list)
    for q in items:
        byfirm[q["firm"]].append(q)
    lv = collections.Counter(q["level"] for q in items)
    md = [
        f"# {title}", "",
        f"{len(items)} questions across {len(byfirm)} firms, out of the {total}-question corpus.",
        "", blurb, "",
        "**By level:** " + " · ".join(f"{k} {v}" for k, v in lv.most_common()),
        "",
        "Tier is sort order, not confirmation: A means multiple independent dated attestations, "
        "B a single dated full-text one, C weak or snippet-only, D provenance real but a "
        "negative signal fired. See `REPORT.md` §6.",
        "", "---", "",
    ]
    for firm, its in sorted(byfirm.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        its.sort(key=lambda q: (TIER[q["tier"]], q["round"]))
        md += [f"## {firm}  ({len(its)})", ""]
        for i, q in enumerate(its, 1):
            a = q["attestations"][0]
            body = flat(q["question_text"])
            md += [f"**{i}.** `{q['tier']}` · {q['level']} · {q['round']} · {q['cycle']}",
                   "", body, ""]
            if CJK.search(body) and q.get("question_text_en"):
                md += [f"*English:* {flat(q['question_text_en'])}", ""]
            ans = real_answer(q.get("reported_answer"))
            if ans:
                md += [f"*Reported answer:* {ans[:400]}", ""]
            md += [f"<sub>{a['source_type']} · {a['post_date']} · "
                   f"[source]({a['source_url']})</sub>", ""]
        md.append("")
    return "\n".join(md)


def main() -> int:
    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]
    live = [q for q in qs if q["tier"] != "REJECT" and is_question(q)]

    byrole = collections.defaultdict(list)
    for q in live:
        byrole[q["role_track"] if q["role_track"] in TRACKS else "unknown"].append(q)

    written, covered = [], 0
    for key, (fname, title, blurb) in TRACKS.items():
        items = byrole.get(key, [])
        if not items:
            continue
        (HARVEST / fname).write_text(render(key, title, blurb, items, len(live)), encoding="utf-8")
        written.append((fname, len(items)))
        covered += len(items)

    assert covered == len(live), f"partition lost questions: {covered} != {len(live)}"
    for f, n in written:
        print(f"{n:5d}  {f}")
    print(f"{covered:5d}  TOTAL (partition is complete, every question in exactly one file)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
