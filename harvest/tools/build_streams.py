#!/usr/bin/env python3
"""Publish the stream deck: the artifact a human actually reads.

Optimised for one thing -- questions per minute of attention. Question first, evidence
compressed underneath, adjudication prose left in the JSON where it belongs.

Streams stay segregated by source family rather than merged, because sources have
characteristic reliability: after twenty items from one stream a reader can judge the
whole stream, which is far faster than judging item by item.
"""
from __future__ import annotations

import collections
import json
import pathlib
import re

HARVEST = pathlib.Path(__file__).resolve().parent.parent
TIER_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, "REJECT": 9}

FAMILY = {
    "1point3acres": "1point3acres", "nowcoder": "nowcoder", "zhihu": "chinese_social",
    "xiaohongshu": "chinese_social", "bilibili": "chinese_social", "weibo": "chinese_social",
    "tieba": "chinese_social", "douban": "chinese_social", "newsmth": "chinese_bbs",
    "university_bbs": "chinese_bbs", "v2ex": "chinese_bbs", "csdn": "chinese_blog",
    "juejin": "chinese_blog", "wechat_article": "chinese_blog",
    "reddit_thread": "reddit", "wso": "wallstreetoasis", "blind": "blind",
    "glassdoor": "glassdoor", "quantnet": "forums", "elitetrader": "forums",
    "trade2win": "forums", "hackernews": "forums",
    "leetcode_discuss": "platforms", "geeksforgeeks": "platforms",
    "github_repo": "github", "student_doc": "compilations", "yuque": "compilations",
    "chat_telegram": "telegram", "chat_discord": "discord",
    "chat_qq_repost": "chat_repost", "chat_wechat_repost": "chat_repost",
    "blog": "blogs", "youtube": "video",
}


def fam(st: str) -> str:
    return FAMILY.get(st, "other")


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.casefold()).strip("_")[:48] or "unknown"


def fmt_item(q: dict, n: int) -> str:
    a = q["attestations"][0]
    head = f"### Q{n} · Tier {q['tier']} · {q['cycle']} · {q['round']}"
    if q.get("section_context"):
        head += f" ({q['section_context'][:70]})"
    body = [head, ""]
    body.append(q["question_text"] or "(no question text recovered)")
    if q.get("question_text_en") and q["question_text_en"] != q["question_text"]:
        body += ["", f"*EN:* {q['question_text_en']}"]
    if q.get("reported_answer"):
        body += ["", f"*Reported answer:* {q['reported_answer'][:300]}"]
    body.append("")
    quote = (a.get("source_quote") or "").replace("\n", " ")[:420]
    body.append("> " + quote)
    bits = [a.get("source_type", "?"), f"posted {a.get('post_date','unknown')}",
            a.get("access", "?"), f"[link]({a.get('source_url','')})"]
    body.append("— " + " · ".join(bits))
    meta = f"  {q['independent_attestations']} attestation(s) across {q['distinct_domains']} domain(s)"
    doubt = q.get("doubt") or q.get("tier_reason") or ""
    if doubt:
        meta += f" · doubt: {doubt[:220]}"
    body.append(meta)
    return "\n".join(body)


def main() -> int:
    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]
    shipped = [q for q in qs if q["tier"] != "REJECT"]
    rejects = [q for q in qs if q["tier"] == "REJECT"]

    streams = collections.defaultdict(list)
    for q in shipped:
        key = (q["firm"], f"{q['role_track']}_{q['level']}", fam(q["attestations"][0].get("source_type", "other")))
        streams[key].append(q)

    sdir = HARVEST / "streams"
    for p in sdir.rglob("*.md"):
        p.unlink()

    index = []
    for (firm, role, family), items in sorted(streams.items(), key=lambda kv: -len(kv[1])):
        items.sort(key=lambda q: (TIER_ORDER[q["tier"]], -len(q["question_text"])))
        d = sdir / slug(firm)
        d.mkdir(parents=True, exist_ok=True)
        path = d / f"{slug(role)}__{slug(family)}.md"
        tiers = collections.Counter(q["tier"] for q in items)
        dates = sorted(a["post_date"] for q in items for a in q["attestations"] if re.match(r"^\d{4}", a["post_date"]))
        hdr = [
            f"# {firm} · {role.replace('_',' ')} · {family}",
            "",
            f"- **Source family:** {family}",
            f"- **Items:** {len(items)}",
            f"- **Date range:** {dates[0] if dates else 'unknown'} – {dates[-1] if dates else 'unknown'}"
            f" ({len(dates)}/{len(items)} dated)",
            f"- **Tier mix:** " + ", ".join(f"{t}={tiers[t]}" for t in "ABCD" if tiers[t]),
            "",
            "---",
            "",
        ]
        chunks = [fmt_item(q, i) for i, q in enumerate(items, 1)]
        path.write_text("\n".join(hdr) + "\n\n".join(chunks) + "\n", encoding="utf-8")
        index.append({"firm": firm, "role": role, "family": family, "n": len(items),
                      "tiers": dict(tiers), "path": str(path.relative_to(HARVEST))})

    # Merged deck, primary target first regardless of size.
    def deck_key(q):
        return (0 if q["firm"] == "Susquehanna International Group" else 1,
                q["firm"], TIER_ORDER[q["tier"]], q["round"])

    out = ["# TRIAGE DECK", "",
           f"{len(shipped)} questions across {len(streams)} streams and "
           f"{len({q['firm'] for q in shipped})} firms. Susquehanna first, then by firm, "
           "tier-sorted within each. Question first, evidence underneath.", "",
           "Read `REPORT.md` for the scoreboard and what to distrust.", "", "---", ""]
    n = 0
    cur = None
    for q in sorted(shipped, key=deck_key):
        grp = (q["firm"], q["round"])
        if grp != cur:
            cur = grp
            out += ["", f"## {q['firm']} — {q['round']}", ""]
        n += 1
        out.append(fmt_item(q, n))
        out.append("")
    (HARVEST / "TRIAGE.md").write_text("\n".join(out), encoding="utf-8")

    with open(HARVEST / "triage.jsonl", "w", encoding="utf-8") as fh:
        for q in sorted(shipped, key=deck_key):
            a = q["attestations"][0]
            fh.write(json.dumps({
                "id": q["id"], "firm": q["firm"], "role_track": q["role_track"],
                "level": q["level"], "round": q["round"], "cycle": q["cycle"],
                "tier": q["tier"], "question_text": q["question_text"],
                "source_url": a["source_url"], "source_type": a["source_type"],
                "post_date": a["post_date"], "human_verdict": "",
            }, ensure_ascii=False) + "\n")

    rd = HARVEST / "rejects"
    rd.mkdir(exist_ok=True)
    (rd / "rejects.md").write_text(
        "# Rejected records\n\nShown so over-filtering is auditable.\n\n" +
        "\n\n".join(
            f"### {q['firm']} · {q['id']}\n\n{q['question_text'][:300]}\n\n"
            f"**Rejected:** {q['tier_reason']}\n\n[source]({q['attestations'][0]['source_url']})"
            for q in rejects),
        encoding="utf-8")

    (HARVEST / "reports" / "stream_index.json").write_text(json.dumps(index, indent=1))
    print(f"{len(streams)} streams, {len(shipped)} shipped, {len(rejects)} rejected")
    print(f"largest: " + ", ".join(f"{i['firm'][:22]}/{i['family']}={i['n']}" for i in index[:5]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
