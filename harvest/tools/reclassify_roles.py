#!/usr/bin/env python3
"""Collapse the role taxonomy to two tracks and place the unlabelled questions.

Two changes, both requested after reading the split:

1. Merge quant_researcher and quant_analyst into quant_trader. This is defensible rather
   than merely convenient: SIG runs the *same* 17-question paper for trader and
   researcher candidates, so the maths/probability/statistics material is one pool. The
   real fault line is maths-vs-code, not trader-vs-researcher.

2. Place the 45 questions whose source never stated a track, by reading each one's topic.

Assignments in (2) are inferences from content, not claims the source made. They are
recorded with `role_inferred: true` and a stated basis so they can be told apart from
labels a candidate actually gave, and reversed if wrong.
"""
from __future__ import annotations

import collections
import json
import pathlib
import sys

HARVEST = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HARVEST / "tools"))
from sample_questions import is_question  # noqa: E402

# Only these six of the 45 are software questions. Everything else is maths, probability,
# statistics, markets or behavioural, and goes to the trading pool.
TO_DEV = {
    "0f1facfd": "Python file-handle idiom (with open / readline) — language mechanics, not maths",
    "1f7be26e": "Python LEGB scope-resolution order — language mechanics",
    "a8a823ef": "Python module/pickle/import trivia — language mechanics",
    "bfee7851": "graph problem set at an on-site coding round",
    "3563ba24": "class design with four callback APIs updating internal state — software design",
    "b4007519": "two-sum over an array — a standard coding-interview algorithm",
}

# A few worth naming because the call could reasonably have gone the other way.
NOTED = {
    "0a3e3784": "stair-climbing counts is both a Fibonacci combinatorics question and a "
                "standard DP coding exercise; the source phrases it as 'how many ways', "
                "so it is filed as maths",
    "e9c944aa": "Bridgewater's open-debate question is not quantitative, but it belongs to "
                "the non-developer pipeline",
    "57513fe1": "the Citadel Datathon ML items are research-flavoured rather than "
                "engineering; they follow quant_researcher into the trading pool",
}


def main() -> int:
    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]

    merged = collections.Counter()
    placed = collections.Counter()
    skipped = [0]
    for q in qs:
        short = q["id"][:8]
        rt = q["role_track"]

        if rt in ("quant_researcher", "quant_analyst"):
            q["role_track_original"] = rt
            q["role_track"] = "quant_trader"
            q["role_merge_note"] = (
                "merged into quant_trader: these tracks share an assessment at several "
                "firms (SIG runs one 17-question paper for trader and researcher)"
            )
            merged[rt] += 1

        elif rt == "unknown":
            # Infer a track only for records whose question text was actually read.
            # The rest are round/format notes with no topic to reason from, and guessing
            # a track for them would be the exact unjustified relabelling this corpus is
            # meant to avoid. They stay unknown.
            if not is_question(q):
                skipped[0] += 1
                continue
            q["role_track_original"] = "unknown"
            q["role_inferred"] = True
            if short in TO_DEV:
                q["role_track"] = "quant_developer"
                q["role_inference_basis"] = TO_DEV[short]
            else:
                q["role_track"] = "quant_trader"
                q["role_inference_basis"] = NOTED.get(
                    short, f"topic is {q.get('question_type') or 'quantitative'}, not software")
            placed[q["role_track"]] += 1

    with open(HARVEST / "questions.jsonl", "w", encoding="utf-8") as fh:
        for q in qs:
            fh.write(json.dumps(q, ensure_ascii=False) + "\n")

    print("merged into quant_trader : " + ", ".join(f"{k}={v}" for k, v in merged.items()))
    print("unlabelled placed        : " + ", ".join(f"{k}={v}" for k, v in placed.items()))
    print(f"left unknown (metadata-only records, no topic to read) : {skipped[0]}")
    print(f"  of which to developer  : {len(TO_DEV)}")
    for sid, why in TO_DEV.items():
        print(f"     {sid}  {why}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
