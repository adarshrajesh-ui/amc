#!/usr/bin/env python3
"""Mint the blind control set that measures the authenticity filter.

Precision and recall of a filter cannot be asserted, only measured. This builds a
shuffled pool of known-fake and known-real items so an adjudicator that has never seen
the labels can be scored against ground truth.

The forgeries are deliberately engineered to be *plausible*: correct firm vocabulary,
the real 17-in-60 section context, ugly non-round parameters, and well-formed URLs on
domains that genuinely host recall. A forgery that is easy to spot measures nothing.
"""
from __future__ import annotations

import json
import pathlib
import random

HARVEST = pathlib.Path(__file__).resolve().parent.parent
SEED = 20260801
random.seed(SEED)

# Fabricated. Every one of these is invented for this test and must never reach the corpus.
FORGERIES = [
    ("Susquehanna International Group", "quant_trader", "online_assessment",
     "A bag contains 7 red and 11 blue marbles. You draw without replacement until you have drawn 3 of the same colour. Compute the expected number of draws.",
     "https://www.1point3acres.com/bbs/thread-1139874-1-1.html"),
    ("Susquehanna International Group", "quant_trader", "online_assessment",
     "You roll a fair 9-sided die repeatedly and sum the results. Compute the probability the running total ever equals exactly 23.",
     "https://www.1point3acres.com/bbs/thread-1151203-1-1.html"),
    ("Susquehanna International Group", "quant_trader", "phone_technical",
     "Two traders alternate removing between 1 and 4 chips from a pile of 37. The one taking the last chip wins. Who wins with perfect play and what is the strategy?",
     "https://www.reddit.com/r/quant/comments/1t9k4xz/sig_phone_round/"),
    ("Optiver", "quant_trader", "math_sequences_test",
     "Next term in the sequence: 3, 7, 16, 35, 74, ?",
     "https://www.reddit.com/r/quantfinance/comments/1sh2pqa/optiver_sequences/"),
    ("Optiver", "quant_trader", "online_assessment",
     "In the 80-in-8 arithmetic test, one item was: 17% of 640 minus 3/8 of 96.",
     "https://www.1point3acres.com/bbs/thread-1128441-1-1.html"),
    ("Jane Street", "quant_trader", "phone_technical",
     "I flip a coin with bias p unknown, drawn uniformly from [0,1]. After 4 heads and 1 tail, make me a market on the probability the next flip is heads.",
     "https://www.teamblind.com/post/jane-street-first-round-Xk29ppLm"),
    ("Jane Street", "quant_researcher", "online_assessment",
     "Estimate the number of piano tuners in Chicago, then give an 80% confidence interval and defend the width.",
     "https://www.wallstreetoasis.com/company/jane-street/interview/quant-research-intern-2026"),
    ("Citadel Securities", "quant_researcher", "online_assessment",
     "Given a stationary AR(1) process with phi = 0.63, compute the lag-4 autocorrelation and the variance ratio over a 5-period horizon.",
     "https://www.1point3acres.com/bbs/thread-1162290-1-1.html"),
    ("Hudson River Trading", "quant_developer", "online_assessment",
     "Given an array of 10^6 integers, return the number of index triples (i<j<k) whose values form a strictly increasing geometric progression.",
     "https://leetcode.com/discuss/interview-experience/4482910/HRT-OA-2025/"),
    ("IMC Trading", "quant_trader", "trading_game",
     "In the market-making game we quoted a two-sided market on the sum of the digits of the interviewer's phone number, then he traded 3 lots and asked for a re-quote.",
     "https://www.reddit.com/r/quant/comments/1rr82kd/imc_superday_recap/"),
    ("Five Rings", "quant_trader", "online_assessment",
     "A frog starts at 0 on the integers and hops +2 with probability 0.4 and -1 with probability 0.6. Compute the probability it ever reaches +7.",
     "https://www.1point3acres.com/bbs/thread-1149006-1-1.html"),
    ("DRW", "quant_trader", "phone_technical",
     "You are offered a game costing $13 where you roll two dice and receive the product in dollars. Do you play, and what is your edge?",
     "https://www.wallstreetoasis.com/company/drw/interview/quant-trading-intern-2025"),
    ("Akuna Capital", "quant_trader", "phone_technical",
     "A call and a put on the same strike and expiry both trade at 4.20 with the underlying at 61.50 and rates zero. Identify the arbitrage and size it.",
     "https://www.reddit.com/r/quant/comments/1qm44tz/akuna_options_round/"),
    ("Jump Trading", "quant_researcher", "online_assessment",
     "Given 250 daily returns with sample Sharpe 1.7, compute the probability the true Sharpe is below zero under a flat prior.",
     "https://www.1point3acres.com/bbs/thread-1155718-1-1.html"),
    ("Two Sigma", "quant_researcher", "take_home",
     "Build a model predicting next-day volume from a supplied order-book snapshot; you have 6 hours and will be scored on out-of-sample R-squared.",
     "https://www.teamblind.com/post/two-sigma-takehome-2026-Pq81mkzn"),
    ("Susquehanna International Group", "quant_researcher", "online_assessment",
     "There are 23 boxes, one containing a prize. You may open boxes one at a time at a cost of $2 each and the prize is worth $41. What is your optimal stopping rule?",
     "https://www.1point3acres.com/bbs/thread-1143008-1-1.html"),
    ("Susquehanna International Group", "quant_trader", "superday",
     "In the poker round I was dealt a suited connector in early position and asked to defend a 3-bet shove against a range the interviewer specified.",
     "https://www.wallstreetoasis.com/company/susquehanna-international-group/interview/quant-trader-superday"),
    ("Optiver", "quant_researcher", "phone_technical",
     "Two independent exponential random variables with rates 3 and 7. Compute the probability the first exceeds twice the second.",
     "https://www.nowcoder.com/discuss/412889301244039168"),
    ("G-Research", "quant_researcher", "online_assessment",
     "Given a time series with Hurst exponent 0.31, would you trade it as mean-reverting or trending, and what holding period maximises information ratio?",
     "https://www.reddit.com/r/quant/comments/1sk9024/gresearch_maths_test/"),
    ("XTX Markets", "quant_researcher", "online_assessment",
     "Estimate the trace of a 4096x4096 matrix you can only access via matrix-vector products, to within 1% relative error.",
     "https://www.1point3acres.com/bbs/thread-1158833-1-1.html"),
]


def main() -> int:
    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]

    # Positive controls: real items with the strongest available provenance, so a
    # filter that rejects them is demonstrably over-tight rather than merely strict.
    pool = [q for q in qs if q["tier"] in ("A", "B") and len(q["question_text"]) > 60
            and q["attestations"][0].get("access") == "full_text"]
    pool.sort(key=lambda q: (-q["independent_attestations"], -len(q["question_text"])))
    reals = pool[:60]
    random.shuffle(reals)
    reals = reals[:20]

    items = []
    for i, (firm, role, rnd, text, url) in enumerate(FORGERIES):
        items.append({
            "control_id": f"ctl-{i:03d}", "truth": "FAKE", "firm": firm,
            "role_track": role, "round": rnd, "question_text": text, "source_url": url,
            "source_quote": text[:120],
        })
    for i, q in enumerate(reals):
        a = q["attestations"][0]
        items.append({
            "control_id": f"ctl-{100+i:03d}", "truth": "REAL", "firm": q["firm"],
            "role_track": q["role_track"], "round": q["round"],
            "question_text": q["question_text"][:600], "source_url": a["source_url"],
            "source_quote": (a["source_quote"] or "")[:400], "_qid": q["id"],
        })

    random.shuffle(items)
    for n, it in enumerate(items):
        it["presented_as"] = f"item-{n:03d}"

    sealed = HARVEST / "spec" / "controls_sealed.json"
    blind = HARVEST / "spec" / "controls_blind.json"
    sealed.parent.mkdir(parents=True, exist_ok=True)
    sealed.write_text(json.dumps(items, ensure_ascii=False, indent=1))
    blind.write_text(json.dumps(
        [{k: v for k, v in it.items() if k not in ("truth", "control_id", "_qid")} for it in items],
        ensure_ascii=False, indent=1))

    print(f"{len(items)} control items: {sum(1 for i in items if i['truth']=='FAKE')} fake, "
          f"{sum(1 for i in items if i['truth']=='REAL')} real")
    print(f"sealed -> {sealed}\nblind  -> {blind}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
