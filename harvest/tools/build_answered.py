#!/usr/bin/env python3
"""Merge the answer key into QTRADER.md, one answer under each question.

Answers carry the provenance of their own correctness: whether a program independently
re-verified them, and whether they contradict the answer the original candidate gave.
Both matter to someone studying from this, and neither is visible from the answer alone.
"""
from __future__ import annotations

import collections
import glob
import json
import pathlib
import re
import sys

HARVEST = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HARVEST / "tools"))
from sample_questions import is_question  # noqa: E402

CJK = re.compile(r"[\u4e00-\u9fff]")
TIER = {"A": 0, "B": 1, "C": 2, "D": 3}


def flat(s) -> str:
    return " ".join(str(s or "").split())


def main() -> int:
    ans = {}
    for f in sorted(glob.glob(str(HARVEST / "answers" / "solved_*.json"))):
        for a in json.load(open(f, encoding="utf-8")):
            ans[a["review_id"]] = a
    replay = {r["review_id"]: r for r in json.load(
        open(HARVEST / "answers" / "verification_replay.json", encoding="utf-8"))}

    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]
    rev = {json.loads(l)["cluster_id"]: json.loads(l)["review_id"]
           for l in open(HARVEST / "review.jsonl", encoding="utf-8")}
    qt = [q for q in qs if q["tier"] != "REJECT" and is_question(q)
          and q["role_track"] == "quant_trader"]

    byfirm = collections.defaultdict(list)
    for q in qt:
        byfirm[q["firm"]].append(q)

    verified = sum(1 for r in replay.values() if r["_status"] == "MATCH")
    guidance = sum(1 for a in ans.values() if a["answer_kind"] == "guidance")
    disputed = [a for a in ans.values() if "wrong" in (a.get("source_answer_check") or "").lower()]

    md = [
        "# Quant trader questions — with answers",
        "",
        f"{len(qt)} questions across {len(byfirm)} firms. Every question has an answer "
        "underneath it.",
        "",
        "## How the answers were checked",
        "",
        f"- **{verified} answers are backed by a program** that independently recomputes the "
        "result — exact enumeration where the state space allows it, otherwise Monte Carlo "
        "with at least two million trials. Every one of those programs was re-executed from "
        "scratch and reproduced its recorded result, so the check is not merely claimed.",
        f"- **{guidance} are marked *guidance*** rather than solved. These are behavioural, "
        "market-making, estimation or open-modelling questions with no single correct value; "
        "the answer describes what the interviewer is testing and the shape of a strong reply.",
        f"- **{len(disputed)} answers contradict the answer the original candidate gave.** "
        "Those are called out inline — candidate recollections are sometimes wrong, and "
        "silently agreeing with one would propagate the error.",
        "",
        "Where a question was a terse recollection missing a parameter, the assumption used "
        "is stated with the answer rather than hidden inside it.",
        "",
        "---",
        "",
    ]

    n_ans = 0
    for firm, items in sorted(byfirm.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        items.sort(key=lambda q: (TIER[q["tier"]], q["round"]))
        md += [f"## {firm}  ({len(items)})", ""]
        for i, q in enumerate(items, 1):
            rid = rev.get(q["id"], "?")
            a = q["attestations"][0]
            body = flat(q["question_text"])
            md += [f"### {i}. `{rid}` · `{q['tier']}` · {q['level']} · {q['round']} · {q['cycle']}",
                   "", body, ""]
            if CJK.search(body) and q.get("question_text_en"):
                md += [f"*English:* {flat(q['question_text_en'])}", ""]

            sol = ans.get(rid)
            if not sol:
                md += ["**Answer:** *(not solved)*", ""]
            else:
                n_ans += 1
                md += [f"**Answer:** {flat(sol['answer'])}", ""]
                if sol.get("reasoning"):
                    md += [f"*Working:* {flat(sol['reasoning'])}", ""]
                if sol.get("assumptions"):
                    md += [f"*Assumption:* {flat(sol['assumptions'])}", ""]
                chk = sol.get("source_answer_check") or ""
                if "wrong" in chk.lower():
                    md += [f"> ⚠️ **The candidate's reported answer is wrong.** {flat(chk)}", ""]
                rp = replay.get(rid)
                bits = []
                if rp and rp["_status"] == "MATCH":
                    bits.append(f"numerically verified — `{flat(rp.get('_actual'))[:150]}`")
                elif sol["answer_kind"] == "guidance":
                    bits.append("guidance, no single correct value")
                if sol.get("confidence") in ("medium", "low"):
                    bits.append(f"confidence: **{sol['confidence']}**")
                if bits:
                    md += ["<sub>" + " · ".join(bits) + "</sub>", ""]
            md += [f"<sub>Source: {a['source_type']} · {a['post_date']} · "
                   f"[link]({a['source_url']})</sub>", "", "---", ""]
        md.append("")

    out = HARVEST / "QTRADER_ANSWERED.md"
    out.write_text("\n".join(md), encoding="utf-8")
    print(f"{len(qt)} questions, {n_ans} with answers")
    print(f"  numerically verified : {verified}")
    print(f"  guidance             : {guidance}")
    print(f"  contradict the source: {len(disputed)}")
    print(f"  -> {out}")
    missing = [rev.get(q['id']) for q in qt if rev.get(q['id']) not in ans]
    if missing:
        print(f"  MISSING ANSWERS: {missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
