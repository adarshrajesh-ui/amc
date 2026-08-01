#!/usr/bin/env python3
"""Split out the quant-developer questions and audit every Chinese translation.

Two outputs:
  QDEV.md         - all quant_developer questions, separated from the trading/research set
  TRANSLATIONS.md - every Chinese-containing question with its source text beside the
                    English, so the rendering can be checked rather than trusted

Translation corrections are applied here rather than in the collectors, so the original
`question_text` is never overwritten -- the Chinese stays authoritative and the English
sits alongside it.
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

# Corrections found by auditing the collectors' renderings against the source text.
# Keyed by cluster id; each entry records what was wrong so the edit is reviewable.
FIXES = {
    "7430d3ba": dict(
        was="Arithmetic, part 1: the input is an arithmetic array",
        note="「算数组」 rendered literally as 'arithmetic array', which is opaque. The "
             "worked example (4 + 5) x 6 shows the input encodes an expression.",
        en="Arithmetic, part 1: the input is an array representing an arithmetic "
           "expression; compute the result considering only + - x /, e.g. (4 + 5) x 6 = ? "
           "You do not need to write the parser, just produce the result.",
    ),
    "5b8b6da3": dict(
        was="A box contains 100 dollars",
        note="「100 元钱」 is yuan, not dollars. The identical question in cluster "
             "fdf6f699 renders it correctly, so the corpus contradicted itself.",
        en="A box holds 100 yuan. You and your opponent each write down a number. If the "
           "sum is at most 100 you each receive money equal to your own number; if the sum "
           "exceeds 100 neither gets anything. Assuming the opponent is rational, what is "
           "your optimal strategy? Follow-up: dropping the rationality assumption and "
           "repeating the game 1000 times, if the opponent says at the first round that he "
           "will write 80, what do you do? If he has written 80 every time for ten rounds, "
           "how do you weigh it up?",
    ),
    "c0303fa0": dict(
        was="…The original poster replies that he had dropped a condition when drawing the grid…",
        note="The English carried a sentence with no counterpart in the quoted Chinese. "
             "It is thread context, not translation, so it moves to a bracketed note.",
        en="[Question 14 — full stem NOT recovered. Attested only via the reply thread:] "
           "'Hi, for Q14 I think AB = 32 also works? Here's the arrangement, I checked and "
           "it satisfies the requirements: 1,4,3,2 / 2,1,4,3 / 4,3,2,1 / 3,2,1,4' "
           "[Thread context, not part of the quoted text: the original poster replies that "
           "he had dropped a condition when drawing the grid, and that with the missing "
           "constraint restored the solution is unique.]",
    ),
}


def flat(s: str) -> str:
    return " ".join(str(s or "").split())


def main() -> int:
    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]

    applied = []
    for q in qs:
        short = q["id"][:8]
        if short in FIXES:
            f = FIXES[short]
            q["question_text_en"] = f["en"]
            q["translation_audit"] = f["note"]
            applied.append((short, f["note"]))

    with open(HARVEST / "questions.jsonl", "w", encoding="utf-8") as fh:
        for q in qs:
            fh.write(json.dumps(q, ensure_ascii=False) + "\n")

    live = [q for q in qs if q["tier"] != "REJECT" and is_question(q)]
    qdev = [q for q in live if q["role_track"] == "quant_developer"]
    zh = [q for q in live if CJK.search(q["question_text"] or "")]

    # --- QDEV.md -------------------------------------------------------------
    byfirm = collections.defaultdict(list)
    for q in qdev:
        byfirm[q["firm"]].append(q)
    md = [
        "# Quant developer / software engineering questions",
        "",
        f"{len(qdev)} questions across {len(byfirm)} firms, split out from the "
        f"{len(live)}-question corpus.",
        "",
        "These are the developer and SWE tracks, kept separate because they are a different "
        "assessment from the trading and research pipelines — at SIG, for instance, the "
        "developer track sits a CodeSignal coding OA while trader and researcher candidates "
        "sit the same 17-question maths paper.",
        "",
        "Note the skew: this set is large because developer-track recall is shared far more "
        "freely than trader-track recall, not because these firms mostly ask coding questions.",
        "",
        "---",
        "",
    ]
    for firm, items in sorted(byfirm.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        order = {"A": 0, "B": 1, "C": 2, "D": 3}
        items.sort(key=lambda q: (order[q["tier"]], q["round"]))
        md += [f"## {firm}  ({len(items)})", ""]
        for i, q in enumerate(items, 1):
            a = q["attestations"][0]
            body = flat(q["question_text"])
            md += [f"**{i}.** `{q['tier']}` · {q['level']} · {q['round']} · {q['cycle']}", "", body, ""]
            if q.get("question_text_en") and CJK.search(body):
                md += [f"*English:* {flat(q['question_text_en'])}", ""]
            md += [f"<sub>{a['source_type']} · {a['post_date']} · "
                   f"[source]({a['source_url']})</sub>", ""]
        md.append("")
    (HARVEST / "QDEV.md").write_text("\n".join(md), encoding="utf-8")

    # --- TRANSLATIONS.md -----------------------------------------------------
    tm = [
        "# Chinese questions with English translations",
        "",
        f"All {len(zh)} questions in the corpus whose text contains Chinese, shown with the "
        "source text above the translation so the rendering can be checked rather than "
        "trusted.",
        "",
        "The Chinese is authoritative and is never overwritten. Where a translation was "
        "corrected during audit, the correction and its reason are recorded inline.",
        "",
        "**Forum slang decoded in these translations:** 面经 interview recall · 笔试 written "
        "test · 地里 \"on the forum\" (1point3acres) · lz / 楼主 original poster · bq "
        "behavioural question · 八股 rote-memorisation questions · 手撕 live coding · "
        "求米 / 加米 requests for forum points.",
        "",
        "---",
        "",
    ]
    for i, q in enumerate(sorted(zh, key=lambda q: (q["firm"], q["id"])), 1):
        a = q["attestations"][0]
        tm += [
            f"### {i}. {q['firm']} · {q['role_track']} · {q['round']} · `{q['tier']}`",
            "",
            "**中文原文 (source):**", "", "> " + flat(q["question_text"]), "",
            "**English:**", "", flat(q.get("question_text_en") or "*(no translation)*"), "",
        ]
        if q.get("translation_audit"):
            tm += [f"**Translation corrected during audit.** {q['translation_audit']}", ""]
        tm += [f"<sub>{a['source_type']} · {a['post_date']} · "
               f"[source]({a['source_url']})</sub>", "", "---", ""]
    (HARVEST / "TRANSLATIONS.md").write_text("\n".join(tm), encoding="utf-8")

    missing = [q for q in zh if not flat(q.get("question_text_en"))]
    print(f"quant_developer questions : {len(qdev)} across {len(byfirm)} firms -> QDEV.md")
    print(f"chinese-containing        : {len(zh)} -> TRANSLATIONS.md")
    print(f"missing a translation     : {len(missing)}")
    print(f"translations corrected    : {len(applied)}")
    for sid, note in applied:
        print(f"   {sid}  {note[:96]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
