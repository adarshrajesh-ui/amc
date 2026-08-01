#!/usr/bin/env python3
"""Apply the reviewer's marks: move cut questions to REMOVED.md, keep the rest.

Nothing is deleted. A removed question keeps its ID, its evidence and its history, and
gains a record of when and why it was cut. That matters for the same reason the reject
pile does: a corpus you can only see the survivors of gives you no way to check whether
the filtering was too aggressive.

Accepts marks from either REVIEW.md tick boxes or a plain removals.txt list of IDs, so
the reviewer can pick whichever is less tedious.
"""
from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import sys

HARVEST = pathlib.Path(__file__).resolve().parent.parent

TICK = re.compile(r"^\s*-\s*\[\s*[xX]\s*\]\s*remove\s*(?:[—:-]\s*(.*))?$")
HEAD = re.compile(r"^###\s+([A-Z0-9]+-\d{3})\b")


def marks_from_md(path: pathlib.Path) -> dict[str, str]:
    out: dict[str, str] = {}
    cur = None
    for line in path.read_text(encoding="utf-8").splitlines():
        h = HEAD.match(line)
        if h:
            cur = h.group(1)
            continue
        m = TICK.match(line)
        if m and cur:
            out[cur] = (m.group(1) or "").strip()
            cur = None
    return out


def marks_from_txt(path: pathlib.Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = re.split(r"[\s,]+", line, maxsplit=1)
        out[parts[0].upper()] = parts[1].strip() if len(parts) > 1 else ""
    return out


def main() -> int:
    review = HARVEST / "review.jsonl"
    if not review.exists():
        print("review.jsonl missing — run build_review.py first", file=sys.stderr)
        return 1
    rows = [json.loads(l) for l in open(review, encoding="utf-8") if l.strip()]
    by_id = {r["review_id"]: r for r in rows}

    marks: dict[str, str] = {}
    md, txt = HARVEST / "REVIEW.md", HARVEST / "removals.txt"
    if md.exists():
        marks.update(marks_from_md(md))
    if txt.exists():
        marks.update(marks_from_txt(txt))

    unknown = sorted(set(marks) - set(by_id))
    for u in unknown:
        print(f"warning: unknown id in marks, ignoring: {u}", file=sys.stderr)

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    # Prior removals are carried forward so repeated runs accumulate history rather
    # than resurrecting anything the reviewer already cut.
    prev_path = HARVEST / "removed.jsonl"
    prev = {json.loads(l)["review_id"]: json.loads(l)
            for l in open(prev_path, encoding="utf-8")} if prev_path.exists() else {}

    kept, removed = [], []
    for r in rows:
        rid = r["review_id"]
        if rid in marks or rid in prev:
            rec = dict(prev.get(rid, r))
            rec["remove"] = True
            rec["reason"] = marks.get(rid) or rec.get("reason") or "no reason given"
            rec.setdefault("removed_on", stamp)
            rec["status"] = "REMOVED BY HUMAN REVIEW — was part of the shipped corpus"
            removed.append(rec)
        else:
            kept.append(r)

    with open(HARVEST / "review.jsonl", "w", encoding="utf-8") as fh:
        for r in kept:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(prev_path, "w", encoding="utf-8") as fh:
        for r in removed:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    import collections
    byfirm = collections.Counter(r["firm"] for r in removed)
    out = [
        "# Removed by review",
        "",
        f"{len(removed)} questions cut from the corpus by human review, out of "
        f"{len(rows)+len(prev)-len(removed) if False else len(rows)} reviewed.",
        "",
        "**These were part of the shipped corpus and were removed deliberately.** They are kept",
        "here rather than deleted so the cut is auditable — if the filtering turns out to have",
        "been too aggressive, everything needed to reverse it is still on this page.",
        "",
        "---",
        "",
    ]
    for firm, n in byfirm.most_common():
        out += [f"## {firm}  ({n} removed)", ""]
        for r in [x for x in removed if x["firm"] == firm]:
            out += [
                f"### ~~{r['review_id']}~~  ·  removed {r.get('removed_on', stamp)}",
                "",
                f"~~{r['question_text']}~~",
                "",
                f"**Reason:** {r['reason']}",
                "",
                f"<sub>was: `{r['tier']}` · {r['role_track']} · {r['level']} · {r['round']} · "
                f"{r['cycle']} · {r['source_type']} · {r['post_date']} · "
                f"[source]({r['source_url']})</sub>",
                "",
            ]
    (HARVEST / "REMOVED.md").write_text("\n".join(out), encoding="utf-8")

    print(f"marked for removal : {len(removed)}")
    print(f"kept               : {len(kept)}")
    if byfirm:
        print("removed by firm    : " + ", ".join(f"{f}={n}" for f, n in byfirm.most_common(8)))
    print(f"\n  -> {HARVEST/'REMOVED.md'}  (audit trail)")
    print(f"  -> {HARVEST/'removed.jsonl'}")
    print(f"  -> {HARVEST/'review.jsonl'}  (survivors)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
