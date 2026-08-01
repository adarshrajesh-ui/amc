#!/usr/bin/env python3
"""Shared record writer for the Jane Street / Citadel / Optiver / IMC shard.

Every field with a controlled vocabulary is validated on write. Free text creeping into
`role_track` or `round` is the failure mode that silently corrupts a labelled corpus,
and it is much cheaper to reject it here than to find it downstream.
"""
import json
import os

OUT = "/workspace/harvest/raw/tier_a_js_citadel_optiver_imc.jsonl"

FIRMS = {"Jane Street", "Citadel", "Citadel Securities", "Optiver", "IMC Trading"}
ROLE = {"quant_trader", "quant_researcher", "quant_developer", "quant_analyst",
        "data_scientist", "unknown"}
LEVEL = {"internship", "new_grad", "experienced", "unknown"}
ROUND = {"online_assessment", "math_sequences_test", "phone_technical", "superday",
         "onsite", "trading_game", "take_home", "datathon", "unknown"}
QTYPE = {"mental_math_speed", "sequences", "probability", "combinatorics",
         "expected_value", "market_making", "betting_odds_arbitrage",
         "poker_game_theory", "fermi_estimation", "logic_brainteaser",
         "statistics_regression", "options_theory", "coding_algorithms",
         "sql_data", "ml_modeling", "trading_game", "behavioral", "other"}
STYPE = {"reddit_thread", "wso", "blind", "quantnet", "elitetrader", "glassdoor",
         "leetcode_discuss", "github_repo", "blog", "1point3acres", "nowcoder",
         "zhihu", "xiaohongshu", "bilibili", "tieba", "newsmth", "university_bbs",
         "youtube", "student_doc"}
LANG = {"en", "zh", "mixed"}
ACCESS = {"full_text", "snippet_only", "screenshot_only", "compilation_only"}
RETR = {"webfetch", "websearch_snippet"}

FIELDS = ["firm", "role_track", "level", "cycle", "office", "round", "round_name",
          "platform", "section_context", "question_type", "question_text",
          "question_text_en", "reported_answer", "source_url", "source_type",
          "source_quote", "source_language", "post_date", "access",
          "retrieval_method", "poster_context", "doubt"]

CHECKS = {"firm": FIRMS, "role_track": ROLE, "level": LEVEL, "round": ROUND,
          "question_type": QTYPE, "source_type": STYPE, "source_language": LANG,
          "access": ACCESS, "retrieval_method": RETR}


def _seen():
    s = set()
    if os.path.exists(OUT):
        with open(OUT, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                r = json.loads(line)
                s.add((r["source_url"], r["question_text"][:120]))
    return s


def write(records):
    seen = _seen()
    n = skipped = 0
    with open(OUT, "a", encoding="utf-8") as f:
        for r in records:
            for k, allowed in CHECKS.items():
                if r.get(k) not in allowed:
                    raise ValueError(f"bad {k}={r.get(k)!r} in {r.get('source_url')}")
            for k in FIELDS:
                if k not in r:
                    raise ValueError(f"missing field {k} in {r.get('source_url')}")
            if set(r) - set(FIELDS):
                raise ValueError(f"extra fields {set(r) - set(FIELDS)}")
            if not r["question_text"] or not r["source_quote"]:
                raise ValueError(f"empty text in {r['source_url']}")
            if not r["doubt"]:
                raise ValueError(f"empty doubt in {r['source_url']}")
            if len(r["source_quote"]) < 40:
                # Short quotes are allowed only when the source genuinely has no more
                # contiguous text to give; make that a conscious choice, not an accident.
                print(f"  WARN short quote ({len(r['source_quote'])}): {r['source_url']}")
            key = (r["source_url"], r["question_text"][:120])
            if key in seen:
                skipped += 1
                continue
            seen.add(key)
            f.write(json.dumps({k: r[k] for k in FIELDS}, ensure_ascii=False) + "\n")
            n += 1
    print(f"wrote {n}, skipped {skipped} dupes -> {OUT}")
    return n
