#!/usr/bin/env python3
"""Rebuild the calibration control set without the two flaws that voided v1.

v1 measured almost nothing. Its forgeries all had `source_quote == question_text[:120]`
-- a mid-word truncation no real record carried -- so the adjudicator could partition
the set on formatting alone, and it said so. And its 20 "real" controls were drawn from
the corpus the pipeline had already admitted, making retention circular.

v2 fixes both. Forgeries carry hand-written quotes that are longer than the question,
open mid-thread, and include poster framing, hedging and typos, matching the texture of
genuine recall. Positive controls come from `positive_controls_v2.json`, sourced
independently off hosts the corpus does not use and confirmed absent from it.
"""
from __future__ import annotations

import json
import pathlib
import random
import re

HARVEST = pathlib.Path(__file__).resolve().parent.parent
random.seed(770214)

# Every item below is fabricated for this test and must never reach the corpus.
# Quotes are written to read like forum recall: framing before the question, an aside
# after it, occasional typos and hedges.
FORGERIES = [
    dict(firm="Susquehanna International Group", role_track="quant_trader", level="internship",
         round="online_assessment", post_date="2025-11-18", source_type="reddit_thread",
         source_url="https://www.reddit.com/r/quantfinance/comments/1p4mz7k/sig_qt_intern_oa_debrief/",
         question_text="A bag contains 7 red and 11 blue marbles. You draw without replacement until you have drawn 3 of the same colour. Compute the expected number of draws.",
         source_quote="Just got out of the SIG QT intern OA, dumping what I remember while it's fresh. 17 questions, hour on the clock, I got through 12. Q6 was the one that ate my time: a bag contains 7 red and 11 blue marbles, you draw without replacement until you have drawn 3 of the same colour, compute the expected number of draws. I set up the states but ran out of clock. Anyone else get this one? I think I had it and then second guessed myself."),
    dict(firm="Susquehanna International Group", role_track="quant_trader", level="internship",
         round="phone_technical", post_date="2026-01-22", source_type="reddit_thread",
         source_url="https://www.reddit.com/r/quant/comments/1t9k4xz/sig_phone_round_recap/",
         question_text="Two traders alternate removing between 1 and 4 chips from a pile of 37. The one taking the last chip wins. Who wins with perfect play?",
         source_quote="had my sig phone round yesterday, 30 min with a trader. mostly EV stuff then he threw a game theory one at me: two traders alternate removing between 1 and 4 chips from a pile of 37, the one taking the last chip wins, who wins with perfect play. i said second player and worked the mod 5 argument, he seemed happy. rest was behavioral, why trading why sig etc."),
    dict(firm="Optiver", role_track="quant_trader", level="internship",
         round="math_sequences_test", post_date="2025-10-09", source_type="reddit_thread",
         source_url="https://www.reddit.com/r/quantfinance/comments/1sh2pqa/optiver_sequences_round/",
         question_text="Next term in the sequence: 3, 7, 16, 35, 74, ?",
         source_quote="Optiver sequences round for the trading internship. You get 25 of these and it is brutal, maybe 30 seconds each. One I remember clearly because I got it wrong: 3, 7, 16, 35, 74, ? I went down the differences route and it did not resolve in time. Realised afterwards it is a_n = 2*a_(n-1) + something. The arithmetic test before it is the famous 80 in 8, that part went fine."),
    dict(firm="Jane Street", role_track="quant_trader", level="internship",
         round="phone_technical", post_date="2025-12-03", source_type="blind",
         source_url="https://www.teamblind.com/post/jane-street-first-round-market-making-Xk29ppLm",
         question_text="I flip a coin with bias p unknown, drawn uniformly from [0,1]. After 4 heads and 1 tail, make me a market on the probability the next flip is heads.",
         source_quote="JS first round for the summer trading internship. Interviewer opened with a market making exercise: he said I flip a coin with bias p unknown drawn uniformly from 0 to 1, after 4 heads and 1 tail, make me a market on the probability the next flip is heads. I quoted 68 at 72 and he lifted my offer, then asked me to requote after telling me the next flip was tails. Laplace rule of succession basically, but under pressure with him trading against you it is a different thing."),
    dict(firm="Citadel Securities", role_track="quant_researcher", level="internship",
         round="online_assessment", post_date="2025-09-27", source_type="1point3acres",
         source_url="https://www.1point3acres.com/bbs/thread-1162290-1-1.html",
         question_text="Given a stationary AR(1) process with phi = 0.63, compute the lag-4 autocorrelation and the variance ratio over a 5-period horizon.",
         source_quote="刚做完 Citadel Securities QR 的 OA，记录一下求米。时间是 90 分钟，一共十几道，统计和概率为主。有一道印象比较深：Given a stationary AR(1) process with phi = 0.63, compute the lag-4 autocorrelation and the variance ratio over a 5-period horizon. 我算的 0.63^4，variance ratio 那部分没太确定公式，最后蒙了一个。整体难度中等偏上，时间不太够。"),
    dict(firm="Hudson River Trading", role_track="quant_developer", level="internship",
         round="online_assessment", post_date="2025-11-02", source_type="leetcode_discuss",
         source_url="https://leetcode.com/discuss/interview-experience/4482910/HRT-Algo-Dev-Intern-OA-2026/",
         question_text="Given an array of 10^6 integers, return the number of index triples (i<j<k) whose values form a strictly increasing geometric progression.",
         source_quote="HRT Algo Dev intern OA, 2 questions 90 minutes on their own platform. Second one was the hard one: given an array of up to 10^6 integers, return the number of index triples (i<j<k) whose values form a strictly increasing geometric progression. Brute force is obviously O(n^3), I got an O(n * sqrt(maxval)) approach passing most cases but TLE'd on the last two. Anyone know the intended solution?"),
    dict(firm="IMC Trading", role_track="quant_trader", level="internship",
         round="trading_game", post_date="2025-10-30", source_type="reddit_thread",
         source_url="https://www.reddit.com/r/quant/comments/1rr82kd/imc_superday_trading_game/",
         question_text="In the market-making game we quoted a two-sided market on the sum of the digits of the interviewer's phone number, then he traded 3 lots and asked for a re-quote.",
         source_quote="IMC superday recap for anyone going through it. Third round is the trading game and it is nothing like the OA. In the market making game we had to quote a two sided market on the sum of the digits of the interviewer's phone number, then he traded 3 lots against us and asked for a requote. The point is clearly to see if you widen and shift after getting picked off. I did not shift enough and he kept hitting me."),
    dict(firm="Five Rings", role_track="quant_trader", level="internship",
         round="online_assessment", post_date="2025-09-15", source_type="1point3acres",
         source_url="https://www.1point3acres.com/bbs/thread-1149006-1-1.html",
         question_text="A frog starts at 0 on the integers and hops +2 with probability 0.4 and -1 with probability 0.6. Compute the probability it ever reaches +7.",
         source_quote="Five Rings 的 OA 做完了，比想象中难。一小时，题目全是概率。有一道随机游走：A frog starts at 0 on the integers and hops +2 with probability 0.4 and -1 with probability 0.6, compute the probability it ever reaches +7. 因为漂移是负的所以不是 1，要解特征方程。我当时没算完。求加米，希望对大家有帮助。"),
    dict(firm="DRW", role_track="quant_trader", level="internship",
         round="phone_technical", post_date="2025-11-25", source_type="wso",
         source_url="https://www.wallstreetoasis.com/company/drw/interview/quant-trading-intern-2026",
         question_text="You are offered a game costing $13 where you roll two dice and receive the product in dollars. Do you play, and what is your edge?",
         source_quote="Interview Questions: You are offered a game costing $13 where you roll two dice and receive the product in dollars. Do you play, and what is your edge? I said yes because E[XY] = E[X]E[Y] = 3.5 squared = 12.25, so actually no, it is a losing game at 13. I caught myself halfway through which I think mattered more than getting it right first time."),
    dict(firm="Akuna Capital", role_track="quant_trader", level="internship",
         round="phone_technical", post_date="2025-10-14", source_type="reddit_thread",
         source_url="https://www.reddit.com/r/quant/comments/1qm44tz/akuna_options_phone_screen/",
         question_text="A call and a put on the same strike and expiry both trade at 4.20 with the underlying at 61.50 and rates zero. Identify the arbitrage and size it.",
         source_quote="Akuna options phone screen, they go deep on options theory way earlier than other shops. One question: a call and a put on the same strike and expiry both trade at 4.20 with the underlying at 61.50 and rates zero, identify the arbitrage and size it. Put call parity says C - P = S - K so if C = P then S must equal K, and the underlying is at 61.50, so unless the strike is 61.50 there is an arb. He then asked me to say which way I'd leg it."),
    dict(firm="Jump Trading", role_track="quant_researcher", level="internship",
         round="online_assessment", post_date="2025-12-11", source_type="1point3acres",
         source_url="https://www.1point3acres.com/bbs/thread-1155718-1-1.html",
         question_text="Given 250 daily returns with sample Sharpe 1.7, compute the probability the true Sharpe is below zero under a flat prior.",
         source_quote="Jump 的 quant research 实习 OA，题目偏统计。记一道：Given 250 daily returns with sample Sharpe 1.7, compute the probability the true Sharpe is below zero under a flat prior. 用 Sharpe 的标准误 sqrt((1+SR^2/2)/T)，然后正态近似。我算出来大概 0.4% 左右，不确定对不对。整体 60 分钟，题量不大但每题都要算。"),
    dict(firm="Two Sigma", role_track="quant_researcher", level="internship",
         round="take_home", post_date="2026-01-08", source_type="blind",
         source_url="https://www.teamblind.com/post/two-sigma-quant-research-takehome-Pq81mkzn",
         question_text="Build a model predicting next-day volume from a supplied order-book snapshot; you have 6 hours and will be scored on out-of-sample R-squared.",
         source_quote="Two Sigma quant research intern take home. They send you a dataset and you get 6 hours: build a model predicting next day volume from a supplied order book snapshot, scored on out of sample R squared. Honestly the modelling was the easy part, the hard part is that they also grade the writeup and I spent too long on feature engineering and rushed the doc. Would recommend budgeting 2 hours for writing."),
    dict(firm="Susquehanna International Group", role_track="quant_researcher", level="internship",
         round="online_assessment", post_date="2025-10-21", source_type="1point3acres",
         source_url="https://www.1point3acres.com/bbs/thread-1143008-1-1.html",
         question_text="There are 23 boxes, one containing a prize. You may open boxes one at a time at a cost of $2 each and the prize is worth $41. What is your optimal stopping rule?",
         source_quote="SIG QR OA 面经，一小时十七题，和之前版本差不多。其中一道 optimal stopping：There are 23 boxes, one containing a prize. You may open boxes one at a time at a cost of $2 each and the prize is worth $41. What is your optimal stopping rule? 关键是每开一个箱子后验概率会更新，要比较继续开的期望收益和成本。我做到第 14 题就没时间了。求米。"),
    dict(firm="Susquehanna International Group", role_track="quant_trader", level="internship",
         round="superday", post_date="2025-11-07", source_type="wso",
         source_url="https://www.wallstreetoasis.com/company/susquehanna-international-group/interview/quant-trader-intern-superday",
         question_text="In the poker round I was dealt a suited connector in early position and asked to defend a 3-bet shove against a range the interviewer specified.",
         source_quote="Interview Questions: The final round in Bala Cynwyd includes a poker segment which nobody warns you about. In the poker round I was dealt a suited connector in early position and asked to defend a 3-bet shove against a range the interviewer specified. They are not testing whether you play poker, they want to hear pot odds and range reasoning out loud rather than gut feel. I do not play and still got through it by just doing the equity arithmetic."),
    dict(firm="Optiver", role_track="quant_researcher", level="internship",
         round="phone_technical", post_date="2025-09-19", source_type="nowcoder",
         source_url="https://www.nowcoder.com/discuss/412889301244039168",
         question_text="Two independent exponential random variables with rates 3 and 7. Compute the probability the first exceeds twice the second.",
         source_quote="Optiver 量化研究实习一面，四十分钟，全程概率。面试官问了一道：Two independent exponential random variables with rates 3 and 7. Compute the probability the first exceeds twice the second. 我用了条件积分，P(X > 2Y) = 7/(7+6)... 中间算错了一次他提示了一下。后面还问了泊松过程的合并。挂没挂不知道，先记一下。"),
    dict(firm="G-Research", role_track="quant_researcher", level="internship",
         round="online_assessment", post_date="2025-10-02", source_type="reddit_thread",
         source_url="https://www.reddit.com/r/quant/comments/1sk9024/gresearch_maths_test_recap/",
         question_text="Given a time series with Hurst exponent 0.31, would you trade it as mean-reverting or trending, and what holding period maximises information ratio?",
         source_quote="G-Research maths test recap. It is harder than people say and the time pressure is real. One of the applied questions: given a time series with Hurst exponent 0.31, would you trade it as mean reverting or trending, and what holding period maximises information ratio. H below 0.5 means antipersistent so mean reverting, but the holding period part I fudged. There is also a pure maths section that is much more like a tripos paper."),
    dict(firm="XTX Markets", role_track="quant_researcher", level="new_grad",
         round="online_assessment", post_date="2025-11-13", source_type="1point3acres",
         source_url="https://www.1point3acres.com/bbs/thread-1158833-1-1.html",
         question_text="Estimate the trace of a 4096x4096 matrix you can only access via matrix-vector products, to within 1% relative error.",
         source_quote="XTX 的数学题笔试，难度确实高，和网上说的一样。有一道数值线性代数：Estimate the trace of a 4096x4096 matrix you can only access via matrix-vector products, to within 1% relative error. 这个是 Hutchinson estimator，用随机向量的二次型期望。需要估计需要多少个样本才能到 1%。我只写了思路没写完整推导。"),
    dict(firm="Citadel", role_track="quant_trader", level="internship",
         round="online_assessment", post_date="2025-12-19", source_type="reddit_thread",
         source_url="https://www.reddit.com/r/quantfinance/comments/1u2p8mq/citadel_qt_intern_oa/",
         question_text="You see a stock quoted 40 bid at 42. A trade prints at 43. What do you infer and how do you update your quote?",
         source_quote="Citadel QT intern OA had a section that was less mathy than I expected, more market intuition. One: you see a stock quoted 40 bid at 42, a trade prints at 43, what do you infer and how do you update your quote. I said the print above the offer means there is size hidden or the market moved, so lift my own bid. They want to see you reason about adverse selection rather than just recompute a fair value."),
    dict(firm="Jane Street", role_track="quant_researcher", level="internship",
         round="onsite", post_date="2025-10-26", source_type="wso",
         source_url="https://www.wallstreetoasis.com/company/jane-street-capital/interview/quant-research-intern-final",
         question_text="Estimate the total number of piano tuners working in Chicago, then give an 80% confidence interval and defend its width.",
         source_quote="Interview Questions: Final round had an estimation round which is basically an estimathon. Estimate the total number of piano tuners working in Chicago, then give an 80% confidence interval and defend its width. The number matters much less than whether your interval is honest — I gave a narrow one and he spent ten minutes pushing on why I was that confident, which I think was the actual test."),
    dict(firm="Old Mission Capital", role_track="quant_trader", level="internship",
         round="online_assessment", post_date="2025-09-08", source_type="wso",
         source_url="https://www.wallstreetoasis.com/company/old-mission-capital/interview/quant-trading-intern-oa",
         question_text="You flip a fair coin 100 times. Given that at least 60 came up heads, estimate the expected number of heads.",
         source_quote="Interview Questions: The OA is split, a fast math section then a couple of coding bits. From the math half: you flip a fair coin 100 times, given that at least 60 came up heads, estimate the expected number of heads. Conditional on a tail event so it is not 60, it pulls up toward maybe 63ish. They wanted a quick defensible estimate not an exact computation, there is not time for exact."),
]


def main() -> int:
    pcs = json.loads((HARVEST / "spec" / "positive_controls_v2.json").read_text())
    items = []
    for i, f in enumerate(FORGERIES):
        items.append({**f, "control_id": f"v2f-{i:03d}", "truth": "FAKE"})
    for i, p in enumerate(pcs):
        items.append({
            "firm": p["firm"], "role_track": p.get("role_track", "unknown"),
            "level": p.get("level", "unknown"), "round": p.get("round", "unknown"),
            "post_date": p.get("post_date", "unknown"), "source_type": p.get("source_type", "other"),
            "source_url": p["source_url"], "question_text": p["question_text"],
            "source_quote": p["source_quote"], "control_id": f"v2r-{i:03d}", "truth": "REAL",
        })

    random.shuffle(items)
    for n, it in enumerate(items):
        it["presented_as"] = f"v2-{n:03d}"

    # The v1 leak, checked explicitly rather than assumed fixed.
    leaks = [it["presented_as"] for it in items
             if it["source_quote"][:110].strip() == it["question_text"][:110].strip()]
    fake_q = [len(i["source_quote"]) for i in items if i["truth"] == "FAKE"]
    real_q = [len(i["source_quote"]) for i in items if i["truth"] == "REAL"]

    (HARVEST / "spec" / "controls_v2_sealed.json").write_text(json.dumps(items, ensure_ascii=False, indent=1))
    (HARVEST / "spec" / "controls_v2_blind.json").write_text(json.dumps(
        [{k: v for k, v in it.items() if k not in ("truth", "control_id")} for it in items],
        ensure_ascii=False, indent=1))

    print(f"{len(items)} items: {sum(1 for i in items if i['truth']=='FAKE')} fake, "
          f"{sum(1 for i in items if i['truth']=='REAL')} real")
    print(f"prefix-leak items: {len(leaks)} (v1 had 20)")
    print(f"quote length fake  min/med/max: {min(fake_q)}/{sorted(fake_q)[len(fake_q)//2]}/{max(fake_q)}")
    print(f"quote length real  min/med/max: {min(real_q)}/{sorted(real_q)[len(real_q)//2]}/{max(real_q)}")
    frac_f = sum(1 for i in items if i["truth"] == "FAKE" and len(i["source_quote"]) > len(i["question_text"]))
    frac_r = sum(1 for i in items if i["truth"] == "REAL" and len(i["source_quote"]) > len(i["question_text"]))
    print(f"quote longer than question: fake {frac_f}/{len(fake_q)}, real {frac_r}/{len(real_q)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
