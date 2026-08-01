#!/usr/bin/env python3
"""Print N random real questions per firm for human inspection.

Samples only records that actually state a question. A sizeable minority of the corpus
carries round/format information instead ("OA was 17 questions in 60 minutes"), which is
useful metadata but wastes a reviewer's attention when they asked to see questions.
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import random
import re

HARVEST = pathlib.Path(__file__).resolve().parent.parent

# Records whose "question" is really a note about the assessment rather than a problem.
NOT_A_QUESTION = re.compile(
    r"^(the |this )?(oa|assessment|test|interview|round|process|format)\b[^?]*$", re.I
)
META_HINTS = (
    "questions in", "minutes", "no question", "format note", "answer fragment",
    "could not recall", "cannot recall", "don't remember", "unable to recall",
)


def is_question(q: dict) -> bool:
    t = (q.get("question_text") or "").strip()
    if len(t) < 45:
        return False
    if q.get("question_type") in ("assessment_format", "behavioral"):
        return False
    low = t.casefold()
    # Keep anything that poses a problem; drop pure commentary about the sitting.
    poses = ("?" in t or low.startswith(("compute", "find", "estimate", "what", "how", "given",
                                         "you ", "a ", "an ", "there are", "suppose", "if ",
                                         "two ", "three ", "implement", "write", "design",
                                         "calculate", "prove", "consider")))
    if not poses:
        return False
    if NOT_A_QUESTION.match(t):
        return False
    if sum(h in low for h in META_HINTS) >= 2 and "?" not in t:
        return False
    return True


def one_line(s: str, n: int) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=10)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--width", type=int, default=230)
    ap.add_argument("--min-firm", type=int, default=1)
    args = ap.parse_args()
    random.seed(args.seed)

    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]
    live = [q for q in qs if q["tier"] != "REJECT" and is_question(q)]

    byfirm = collections.defaultdict(list)
    for q in live:
        byfirm[q["firm"]].append(q)

    order = sorted(byfirm.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    md = ["# Sample — up to %d random questions per firm" % args.n, "",
          f"Drawn with seed {args.seed} from {len(live)} records that state an actual question "
          f"(of {len([q for q in qs if q['tier']!='REJECT'])} shipped; the remainder carry "
          "round/format information rather than a problem).", "",
          "Tier is sort order, not confirmation. Tier D means provenance is real but a negative "
          "signal fired — see REPORT.md §6.", "", "---", ""]
    txt = []

    for firm, items in order:
        if len(items) < args.min_firm:
            continue
        pick = random.sample(items, min(args.n, len(items)))
        pick.sort(key=lambda q: ({"A": 0, "B": 1, "C": 2, "D": 3}[q["tier"]], q["round"]))
        tiers = collections.Counter(q["tier"] for q in items)
        hdr = (f"{firm}  —  {len(items)} questions in corpus "
               f"(" + " ".join(f"{t}:{tiers[t]}" for t in "ABCD" if tiers[t]) + ")")
        txt.append("\n" + "=" * 100 + f"\n{hdr}\n" + "=" * 100)
        md += [f"## {firm}", "", f"*{len(items)} questions in corpus — "
               + ", ".join(f"Tier {t}: {tiers[t]}" for t in "ABCD" if tiers[t]) + "*", ""]
        for i, q in enumerate(pick, 1):
            role = q["role_track"].replace("quant_", "q").replace("_", " ")
            meta = f"[{q['tier']}] {role}/{q['level'][:6]} {q['round'][:14]} {q['cycle'][:11]}"
            txt.append(f"{i:2d}. {meta}\n    {one_line(q['question_text'], args.width)}")
            a = q["attestations"][0]
            md += [f"**{i}.** `{q['tier']}` · {role} · {q['level']} · {q['round']} · {q['cycle']}",
                   "", one_line(q["question_text"], 700), "",
                   f"> {one_line(a.get('source_quote') or '', 300)}", "",
                   f"— {a.get('source_type')} · {a.get('post_date')} · "
                   f"[source]({a.get('source_url')})", ""]
        md.append("")

    (HARVEST / "SAMPLE.md").write_text("\n".join(md), encoding="utf-8")
    print("\n".join(txt))
    print(f"\n\n{len(order)} firms · {len(live)} question-bearing records · full sample -> SAMPLE.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
