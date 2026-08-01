#!/usr/bin/env python3
"""Concatenate the Tier-A part files into the deliverable JSONL, dropping duplicates
and enforcing the controlled vocabularies so a mislabelled record fails loudly."""
import glob
import json
import os
import re
import sys
from collections import Counter, OrderedDict

PARTS = "/workspace/harvest/raw/_tier_a_parts/p*.jsonl"
OUT = "/workspace/harvest/raw/tier_a_hrt_jump_drw_others.jsonl"

FIRMS = {"Hudson River Trading", "Jump Trading", "DRW", "Five Rings", "Akuna Capital",
         "Old Mission Capital", "Two Sigma", "D. E. Shaw"}
ROLE = {"quant_trader", "quant_researcher", "quant_developer", "quant_analyst",
        "data_scientist", "unknown"}
LEVEL = {"internship", "new_grad", "experienced", "unknown"}
ROUND = {"online_assessment", "math_sequences_test", "phone_technical", "superday",
         "onsite", "trading_game", "take_home", "datathon", "unknown"}
QTYPE = {"mental_math_speed", "sequences", "probability", "combinatorics", "expected_value",
         "market_making", "betting_odds_arbitrage", "poker_game_theory", "fermi_estimation",
         "logic_brainteaser", "statistics_regression", "options_theory", "stochastic_calculus",
         "linear_algebra", "coding_algorithms", "sql_data", "ml_modeling", "trading_game",
         "behavioral", "other"}
STYPE = {"reddit_thread", "wso", "blind", "quantnet", "elitetrader", "glassdoor",
         "leetcode_discuss", "github_repo", "blog", "1point3acres", "nowcoder", "zhihu",
         "xiaohongshu", "bilibili", "tieba", "newsmth", "university_bbs", "youtube",
         "student_doc"}
ACCESS = {"full_text", "snippet_only", "screenshot_only", "compilation_only"}
RETR = {"webfetch", "websearch_snippet"}
LANG = {"en", "zh", "mixed"}

FIELDS = ["firm", "role_track", "level", "cycle", "office", "round", "round_name", "platform",
          "section_context", "question_type", "question_text", "question_text_en",
          "reported_answer", "source_url", "source_type", "source_quote", "source_language",
          "post_date", "access", "retrieval_method", "poster_context", "doubt"]


def key(o):
    q = re.sub(r"\s+", " ", (o["question_text"] or "").lower()).strip()
    q = re.sub(r"[^\w\u4e00-\u9fff ]", "", q)
    return (o["firm"], o["source_url"], q[:160])


def main():
    errs = []
    seen = OrderedDict()
    files = sorted(glob.glob(PARTS))
    for p in files:
        for i, line in enumerate(open(p, encoding="utf-8"), 1):
            line = line.strip()
            if not line:
                continue
            o = json.loads(line)
            where = "%s:%d" % (os.path.basename(p), i)
            for name, allowed in (("firm", FIRMS), ("role_track", ROLE), ("level", LEVEL),
                                  ("round", ROUND), ("question_type", QTYPE),
                                  ("source_type", STYPE), ("access", ACCESS),
                                  ("retrieval_method", RETR), ("source_language", LANG)):
                if o.get(name) not in allowed:
                    errs.append("%s bad %s=%r" % (where, name, o.get(name)))
            for req in ("question_text", "source_url", "source_quote", "doubt"):
                if not o.get(req):
                    errs.append("%s empty %s" % (where, req))
            if len(o.get("source_quote") or "") < 20:
                errs.append("%s source_quote under 20 chars" % where)
            k = key(o)
            if k in seen:
                continue
            seen[k] = OrderedDict((f, o.get(f)) for f in FIELDS)
    if errs:
        print("VALIDATION ERRORS (%d):" % len(errs), file=sys.stderr)
        for e in errs[:40]:
            print("  " + e, file=sys.stderr)
        if "--force" not in sys.argv:
            sys.exit(1)
    with open(OUT, "w", encoding="utf-8") as f:
        for rec in seen.values():
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    recs = list(seen.values())
    print("wrote %d unique records -> %s" % (len(recs), OUT))
    for dim in ("firm", "level", "role_track", "round", "source_type", "access",
                "source_language"):
        c = Counter(r[dim] for r in recs)
        print("\n%s:" % dim)
        for k2, v in c.most_common():
            print("  %4d %s" % (v, k2))


if __name__ == "__main__":
    main()
