#!/usr/bin/env python3
"""Normalize, cluster and tier the raw collector output.

Collectors were given controlled vocabularies but returned a lot of free text
("Quantitative Trader", "intern（暑期实习）", "OA / 笔试"). Normalizing here rather than
trusting the collectors keeps the mapping auditable in one place: every raw value that
did not map cleanly is reported rather than silently bucketed into `unknown`.
"""
from __future__ import annotations

import collections
import glob
import hashlib
import json
import pathlib
import re
import sys
import unicodedata

HARVEST = pathlib.Path(__file__).resolve().parent.parent

ROLE = {
    "quant_trader": ["quant_trader", "quantitative trader", "trader", "trading", "assistant trader", "qt"],
    "quant_researcher": ["quant_researcher", "quantitative research", "researcher", "qr", "quant research"],
    "quant_developer": ["quant_developer", "software", "developer", "swe", "engineer", "sde", "dev"],
    "quant_analyst": ["quant_analyst", "analyst"],
    "data_scientist": ["data_scientist", "data scien", "数科"],
}
LEVEL = {
    "internship": ["intern", "实习", "summer analyst", "placement", "co-op"],
    "new_grad": ["new_grad", "new grad", "graduate", "campus", "校招", "grad "],
    "experienced": ["experienced", "lateral", "full-time hire", "社招"],
}
ROUND = {
    "online_assessment": ["online_assessment", "oa", "online assessment", "笔试", "网测", "written test"],
    "math_sequences_test": ["math_sequences", "sequences", "mental math", "arithmetic", "maths test"],
    "phone_technical": ["phone", "电面", "first round", "round 1", "screen", "technical interview"],
    "superday": ["superday", "super day", "final round"],
    "onsite": ["onsite", "on-site", "office interview", "现场"],
    "trading_game": ["trading_game", "trading game", "market making game", "market-making game"],
    "take_home": ["take_home", "take home", "takehome"],
    "datathon": ["datathon"],
}


def bucket(value, table, default="unknown"):
    v = str(value or "").strip().casefold()
    if not v or v in ("none", "null", "unknown", "n/a"):
        return default, False
    for canon, needles in table.items():
        for n in needles:
            if n in v:
                return canon, True
    return default, False


def norm_text(s: str) -> str:
    s = unicodedata.normalize("NFKC", str(s or ""))
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def skeleton(s: str) -> str:
    """Question identity with numbers removed.

    The SIG cartography agent established that the question bank is refreshed by
    mutating parameters while keeping the problem skeleton (the frog's target moved
    B(5,4)->B(5,6); a betting game's win probability 3/4->2/3). Exact-number matching
    would therefore split one recurring question into several, so clustering keys on
    the de-numbered skeleton and treats parameter drift as the same item.
    """
    s = norm_text(s).casefold()
    s = re.sub(r"\d+(?:[.,/]\d+)?", "#", s)
    s = re.sub(r"[^\w#\u4e00-\u9fff]+", " ", s)
    toks = [t for t in s.split() if t]
    return " ".join(toks[:40])


# Order matters: the longest/most specific alias must win, because "Citadel Securities"
# also contains "citadel". Matching is on whole words -- a substring test silently
# folded every "Two Sigma" record into Susquehanna, since "two sigma" contains "sig".
FIRM_CANON = [
    ("citadel securities", "Citadel Securities"),
    ("two sigma", "Two Sigma"),
    ("susquehanna", "Susquehanna International Group"),
    ("sig", "Susquehanna International Group"),
    ("citadel", "Citadel"),
    ("d. e. shaw", "D. E. Shaw"),
    ("de shaw", "D. E. Shaw"),
    ("deshaw", "D. E. Shaw"),
    ("hudson river trading", "Hudson River Trading"),
    ("hrt", "Hudson River Trading"),
    ("point72", "Point72 / Cubist"),
    ("cubist", "Point72 / Cubist"),
    ("jane street", "Jane Street"),
    ("optiver", "Optiver"),
    ("imc", "IMC Trading"),
    ("jump trading", "Jump Trading"),
    ("drw", "DRW"),
    ("five rings", "Five Rings"),
    ("akuna", "Akuna Capital"),
    ("old mission", "Old Mission Capital"),
]


def canon_firm(f: str) -> str:
    v = norm_text(f)
    low = v.casefold()
    for alias, canon in FIRM_CANON:
        if re.search(r"(?<![a-z0-9])" + re.escape(alias) + r"(?![a-z0-9])", low):
            return canon
    return v or "unknown"


VENDOR_DOMAINS = (
    "jobtestprep", "quantblueprint", "tradermath", "tradinginterview", "everythingquant",
    "theinterviewden", "techinterview.org", "howtoanalyzedata", "programhelp", "prepfully",
    "interviewquery", "tryexponent", "quantt.co.uk", "scoutify", "learncswithus",
)


def main() -> int:
    files = [f for f in sorted(glob.glob(str(HARVEST / "raw" / "*.jsonl"))) if not f.endswith("_all.jsonl")]
    recs, unmapped = [], collections.Counter()

    # Records the red team demonstrably broke. Kept out of the shipped tiers but
    # written to rejects/ with the proof, because an invisible reject pile makes
    # over-filtering undetectable.
    broken_path = HARVEST / "reports" / "red_team.json"
    broken: dict[str, str] = {}
    if broken_path.exists():
        try:
            rt = json.loads(broken_path.read_text())
            for r in rt.get("results", []):
                if r.get("verdict") == "BROKEN":
                    broken[r["id"]] = r.get("finding", "red team broke this record")
        except Exception as e:
            print(f"warning: could not read red_team.json ({e})", file=sys.stderr)

    for f in files:
        shard = pathlib.Path(f).stem
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue

            rt, ok_r = bucket(r.get("role_track"), ROLE)
            lv, ok_l = bucket(r.get("level"), LEVEL)
            rd, ok_d = bucket(r.get("round"), ROUND)
            if not ok_r and r.get("role_track"):
                unmapped[f"role:{r.get('role_track')}"] += 1
            if not ok_l and r.get("level"):
                unmapped[f"level:{r.get('level')}"] += 1
            if not ok_d and r.get("round"):
                unmapped[f"round:{r.get('round')}"] += 1

            qt = norm_text(r.get("question_text"))
            url = str(r.get("source_url") or "").strip()
            quote = norm_text(r.get("source_quote"))

            rec = {
                "shard": shard,
                "firm": canon_firm(r.get("firm")),
                "role_track": rt,
                "role_track_raw": r.get("role_track"),
                "level": lv,
                "level_raw": r.get("level"),
                "cycle": norm_text(r.get("cycle")) or "unknown",
                "office": norm_text(r.get("office")) or "unknown",
                "round": rd,
                "round_name": norm_text(r.get("round_name")),
                "platform": norm_text(r.get("platform")),
                "section_context": norm_text(r.get("section_context")),
                "question_type": norm_text(r.get("question_type")) or "other",
                "question_text": qt,
                "question_text_en": norm_text(r.get("question_text_en")),
                "reported_answer": norm_text(r.get("reported_answer")),
                "source_url": url,
                "source_type": norm_text(r.get("source_type")) or "other",
                "source_quote": quote,
                "source_language": norm_text(r.get("source_language")) or "en",
                "post_date": norm_text(r.get("post_date")) or "unknown",
                "access": norm_text(r.get("access")) or "unknown",
                "retrieval_method": norm_text(r.get("retrieval_method")),
                "poster_context": norm_text(r.get("poster_context")),
                "doubt": norm_text(r.get("doubt")),
                "upstream_source": norm_text(r.get("upstream_source")),
                "vendor_domain": any(v in url.casefold() for v in VENDOR_DOMAINS),
            }
            recs.append(rec)

    # Cluster on question skeleton so parameter-refreshed variants of one item collapse,
    # while every attestation stays attached -- corroboration count is the main tiering
    # input and collapsing duplicates without preserving sources would destroy it.
    clusters: dict[str, dict] = {}
    for r in recs:
        key_src = r["question_text"] or r["source_quote"]
        sk = skeleton(key_src)
        if len(sk) < 12:
            sk = "SHORT::" + hashlib.sha1((r["source_url"] + key_src).encode()).hexdigest()[:12]
        ck = hashlib.sha1((r["firm"] + "|" + sk).encode()).hexdigest()[:14]
        c = clusters.setdefault(ck, {"id": ck, "firm": r["firm"], "members": []})
        c["members"].append(r)

    out = []
    for ck, c in clusters.items():
        ms = c["members"]
        canon = max(ms, key=lambda m: len(m["question_text"]))
        urls = {m["source_url"] for m in ms if m["source_url"]}
        domains = {re.sub(r"^www\.", "", m["source_url"].split("/")[2]) for m in ms if m["source_url"].count("/") > 2}
        # Independent attestation counts distinct URLs, not records: one thread quoted
        # five times is one witness, and treating it as five would fake corroboration.
        n_att = len(urls)
        n_dom = len(domains)
        dated = [m for m in ms if re.match(r"^\d{4}", m["post_date"])]
        recent = [m for m in dated if m["post_date"][:4] >= "2024"]
        has_full = any(m["access"] == "full_text" for m in ms)
        vendor_only = all(m["vendor_domain"] for m in ms)

        # Systemic risks the red team established across whole classes of record.
        # These do not disprove an item, so per the brief they are demoted to Tier D
        # and shipped with the reason stated, never silently dropped.
        flags = []
        if all("t.me/usinterview" in m["source_url"] for m in ms):
            flags.append("sole source is a Telegram bot that mirrors 1point3acres previews, not an independent witness")
        if any(m["source_type"] == "reddit_thread" for m in ms) and all(
            m["post_date"][:4] == "2026" for m in ms if re.match(r"^\d{4}", m["post_date"])
        ) and dated:
            flags.append("2026-vintage Reddit recall, the cohort where the red team found bot and LLM-generated comments")
        qt_l = canon["question_text"].casefold()
        if len(canon["question_text"]) < 40 or qt_l.startswith(("format note", "no question", "answer fragment")):
            flags.append("record carries round/format information rather than a recoverable question")

        if ck in broken:
            tier = "REJECT"
            why = "red team BROKEN: " + broken[ck][:200]
        elif vendor_only:
            tier = "REJECT"
            why = "sole attestation is a prep-vendor domain"
        elif flags:
            tier, why = "D", "; ".join(flags)
        elif n_att >= 2 and n_dom >= 2 and dated and has_full:
            tier, why = "A", f"{n_att} independent attestations across {n_dom} domains, dated, full text"
        elif dated and has_full:
            tier, why = "B", "single dated first-person attestation with full-text access"
        elif has_full or dated:
            tier, why = "C", "attested but weak: missing date or full-text access"
        else:
            tier, why = "C", "snippet/compilation only, undated"

        out.append({
            "id": ck,
            "firm": c["firm"],
            "role_track": canon["role_track"],
            "level": canon["level"],
            "cycle": canon["cycle"],
            "round": canon["round"],
            "round_name": canon["round_name"],
            "platform": canon["platform"],
            "section_context": canon["section_context"],
            "question_type": canon["question_type"],
            "question_text": canon["question_text"],
            "question_text_en": canon["question_text_en"],
            "reported_answer": canon["reported_answer"],
            "tier": tier,
            "tier_reason": why,
            "independent_attestations": n_att,
            "distinct_domains": n_dom,
            "recent_cycle": bool(recent),
            "shards": sorted({m["shard"] for m in ms}),
            "attestations": [
                {
                    "source_url": m["source_url"], "source_type": m["source_type"],
                    "source_quote": m["source_quote"], "source_language": m["source_language"],
                    "post_date": m["post_date"], "access": m["access"],
                    "retrieval_method": m["retrieval_method"], "poster_context": m["poster_context"],
                    "doubt": m["doubt"],
                } for m in ms
            ],
            "doubt": canon["doubt"],
        })

    outp = HARVEST / "questions.jsonl"
    with open(outp, "w", encoding="utf-8") as fh:
        for r in out:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"raw records      {len(recs)}")
    print(f"clusters         {len(out)}")
    print(f"collapsed        {len(recs)-len(out)} duplicate attestations merged")
    print()
    for k in ("tier", "firm", "role_track", "level", "round"):
        c = collections.Counter(r[k] if not isinstance(r[k], list) else "?" for r in out)
        print(f"-- {k}: " + ", ".join(f"{v}={n}" for v, n in c.most_common(10)))
    print(f"\nmulti-attestation clusters: {sum(1 for r in out if r['independent_attestations']>=2)}")
    print(f"cross-domain clusters:      {sum(1 for r in out if r['distinct_domains']>=2)}")
    if unmapped:
        print(f"\ntop unmapped raw vocabulary values ({len(unmapped)} distinct):")
        for v, n in unmapped.most_common(12):
            print(f"   {n:4d}  {v[:100]}")
    print(f"\nwrote {outp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
