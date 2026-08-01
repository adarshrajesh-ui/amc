#!/usr/bin/env python3
"""Emit the SIG x 1point3acres harvest as JSONL.

Every record below was transcribed from a WebSearch result "Highlights" block that
quoted a www.1point3acres.com URL. Nothing here was written from memory.
"""

import json
import os

OUT = "/workspace/harvest/raw/sig_1point3acres.jsonl"

BASE = {
    "firm": "Susquehanna International Group",
    "source_type": "1point3acres",
    "access": "snippet_only",
    "retrieval_method": "websearch_snippet",
    "office": "unknown",
    "platform": "unknown",
}

# ---------------------------------------------------------------------------
# thread-1144112 : "2026 SIG Quant Research OA整理 【带答案】"
# ---------------------------------------------------------------------------
T1144112 = "https://www.1point3acres.com/bbs/thread-1144112-1-1.html"
T1144112_COMMON = dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="2026",
    round="online_assessment",
    round_name="SIG Quant Research OA",
    section_context="17 questions in 1 hour; poster: 前9个偏简单，后面8个偏难 (first 9 easier, last 8 harder)",
    source_url=T1144112,
    source_language="mixed",
    post_date="unknown",
    poster_context=(
        "Thread titled '2026 SIG Quant Research OA整理 【带答案】' in 一亩三分地 海外面经 board. "
        "Poster says they have taken this OA several times ('已经做了好几次了') and wrote the "
        "answers/explanations themselves, asking for rice points ('自己写的答案和解释，求加米！！！')."
    ),
)

records = []

records.append(dict(
    T1144112_COMMON,
    question_type="logic_brainteaser",
    question_text=(
        "Question 1: You walk into a barn and see a collection of spiders, chickens, and cows. "
        "You notice that there are 520 legs in total. The number of chickens is twice the number "
        "of cows and the number of spiders is twice the number of chickens. Compute the number of spiders."
    ),
    question_text_en=None,
    reported_answer="52 (poster: 答案：52， 变形的“鸡兔同笼”问题 — a variant of the classic chickens-and-rabbits-in-a-cage problem)",
    source_quote=(
        "SIG 的OA万年不变，1小时17个题，已经做了好几次了。前9个偏简单，后面8个偏难。把带答案的版本给大家整理下。"
        "自己写的答案和解释，求加米！！！ Question 1: You walk into a barn and see a collection of spiders, "
        "chickens, and cows. You notice that there are 520 legs in total. The number of chickens is twice the "
        "number of cows and the number of spiders is twice the number of chickens. Compute the number of spiders. "
        "答案：52， 变形的“鸡兔同笼”问题"
    ),
    doubt=(
        "This exact wording is also plastered across prep-vendor/content-farm pages (programhelp.net, "
        "csoahelp.com, studyx.ai screenshots), so it is impossible to rule out that the 1p3a poster copied it "
        "from an aggregator rather than from their own sitting. Mitigating: the studyx.ai copies are photographs "
        "of a live 'Susquehanna Problem Solving Assessment' Mettl screen showing this question numbering, which "
        "is consistent with a genuine SIG item."
    ),
))

records.append(dict(
    T1144112_COMMON,
    question_type="logic_brainteaser",
    question_text=(
        "Question 2: I need to seat 5 toddlers (Anna, Brian, Charlie, Dixie, Eva) at a round table with these "
        "rules: i) Anna won’t sit next to Brian or Eva. ii) Brian won’t sit next to Charlie. iii) Dixie won’t "
        "sit next to Eva or Charlie. If Dixie is sitting to the left of Anna, who is sitting to the left of Brian?"
    ),
    question_text_en=None,
    reported_answer="Eva (poster gives the full arrangement: 答案: Eva, B–D–A–C–E)",
    source_quote=(
        "Question 2: I need to seat 5 toddlers (Anna, Brian, Charlie, Dixie, Eva) at a round table with these "
        "rules: i) Anna won’t sit next to Brian or Eva. ii) Brian won’t sit next to Charlie. iii) Dixie won’t "
        "sit next to Eva or Charlie. If Dixie is sitting to the left of Anna, who is sitting to the left of "
        "Brian? 答案: Eva, B–D–A–C–E"
    ),
    doubt=(
        "A Numerade page carries a near-identical puzzle with a different final condition ('if Brian is sitting "
        "to the right of Eva, who is sitting to the right of Anna?'), which means the item circulates as a "
        "generic logic puzzle and the firm attribution could be bolted on. However this exact SIG-numbered "
        "variant is independently attested on a second 1p3a thread (SIG Trader OA, thread-1086565)."
    ),
))

records.append(dict(
    T1144112_COMMON,
    question_type="probability",
    question_text=(
        "Question 3: 1000 people were surveyed about their preferred method of exercise. The table shows "
        "results by age group. If you meet a 33-year-old who took the survey, compute the probability she "
        "prefers swimming."
    ),
    question_text_en=None,
    reported_answer="52/269 (poster: 答案52/269， 简单条件概率问题，只看 33-37 岁这组：总共有 269 人，其中 52 人选了游泳。所以概率 = 52 ÷ 269 = 52/269)",
    source_quote=(
        "答案52/269， 简单条件概率问题，只看 33-37 岁这组：总共有 269 人，其中 52 人选了游泳。所以概率 = 52 ÷ 269 = 52/269"
        " ... Question 3: 1000 people were surveyed about their preferred method of exercise. The table shows "
        "results by age group. If you meet a 33-year-old who took the survey, compute the probability she prefers swimming."
    ),
    doubt=(
        "The question depends on a data table that is an image in the original post and was never rendered in "
        "any snippet, so the item is unusable without it. The numbers 52 and 269 come from the poster's answer "
        "text, not from a table I saw. Also, in the snippet the answer for Q3 and a stray card-expectation "
        "answer ('由于对称性，4 种牌相加，期望 = 4 × (3/14) = 6/7') appear glued together, so the page's own "
        "ordering may be corrupted."
    ),
))

records.append(dict(
    T1144112_COMMON,
    question_type="logic_brainteaser",
    question_text=(
        "Questions 4 Compute the weight of the green triangle in pounds if the following system is balanced "
        "and weighs 96 pounds in total."
    ),
    question_text_en=None,
    reported_answer="6 (poster: 答案：6。确定红圈三角的重量就行，系统平衡，所以三角形 = 96/2/2/2/2)",
    source_quote=(
        "Questions 4 Compute the weight of the green triangle in pounds if the following system is balanced and "
        "weighs 96 pounds in total. 答案：6。确定红圈三角的重量就行，系统平衡，所以三角形 = 96/2/2/2/2"
    ),
    doubt=(
        "The balance diagram is an image and was never visible; the text alone is not solvable. Third-party "
        "homework sites solving screenshots of the same item give 8 lbs and 48 lbs, contradicting the 6 lbs "
        "here — probably different shape layouts across sittings, but it means the reported answer is only "
        "valid for this poster's diagram. Independently corroborated as a real SIG item by 1p3a thread-1082367 "
        "('求绿色三角形的重量（6lb)'), which gives the same answer."
    ),
))

records.append(dict(
    T1144112_COMMON,
    question_type="probability",
    question_text=(
        "Question 5: Factory A makes 40% red widgets and 60% black widgets. Factory B makes 80% red widgets "
        "and 20% black widgets. Two widgets are sampled uniformly at random from one of the companies, also "
        "selected uniformly at random. The widgets are both red. Compute the probability they were from Factory A."
    ),
    question_text_en=None,
    reported_answer="1/5 (poster: 答案：1/5， 最典型的贝叶斯问题，和袋子里抽球一样。)",
    source_quote=(
        "Question 5: Factory A makes 40% red widgets and 60% black widgets. Factory B makes 80% red widgets and "
        "20% black widgets. Two widgets are sampled uniformly at random from one of the companies, also selected "
        "uniformly at random. The widgets are both red. Compute the probability they were from Factory A. "
        "答案：1/5， 最典型的贝叶斯问题，和袋子里抽球一样。"
    ),
    doubt=(
        "Widely mirrored on content farms, so copying cannot be excluded. Strongest independent support: "
        "studyx.ai hosts two separate photographs of a live 'Susquehanna Problem Solving Assessment' Mettl "
        "screen showing this as Question 5 with the answer-entry format 'numerator in the first blank and the "
        "denominator in the second blank', which matches SIG's actual test UI."
    ),
))

records.append(dict(
    T1144112_COMMON,
    question_type="expected_value",
    question_text=(
        "Question 6: You roll three fair 6-sided dice. If they all show the same number, you earn $20. If "
        "exactly two of the numbers are the same, you earn $10. If all of the numbers are different, you lose "
        "$2. Compute your expected return per roll in dollars. (Round to the nearest cent.)"
    ),
    question_text_en=None,
    reported_answer="3.61 (poster: 答案：3.61 分三种情况，求期望。)",
    source_quote=(
        "Question 6: You roll three fair 6-sided dice. If they all show the same number, you earn $20. If "
        "exactly two of the numbers are the same, you earn $10. If all of the numbers are different, you lose "
        "$2. Compute your expected return per roll in dollars. (Round to the nearest cent.) 答案：3.61 分三种情况，求期望。"
    ),
    doubt=(
        "Same content-farm mirroring problem as Q1/Q5. I could not independently verify the answer 3.61 against "
        "a second 1point3acres poster."
    ),
))

records.append(dict(
    T1144112_COMMON,
    question_type="probability",
    question_text=(
        "Question 16: Suppose you have 3 tokens for a betting game and your goal is to reach 5 tokens before "
        "running out. Each turn you bet as many tokens as possible but not more than needed to reach 5. You win "
        "each bet with probability 2/3. Compute the probability you reach 5 tokens before running out. (Give "
        "your answer as a reduced fraction.)"
    ),
    question_text_en=None,
    reported_answer=(
        "62/77. Poster's working: 把资金 0 和 5 当成终点，其他金额是状态。按“押到能押的最大额但不超过到 5 的差”建方程："
        "P3=2/3+1/3·P1, P1=2/3·P2, P2=2/3·P4, P4=2/3+1/3·P3。解出从 3 开始的成功概率 P3=62/77。"
        "本质是一个马尔可夫链/赌徒破产的问题。"
    ),
    source_quote=(
        "Question 16: Suppose you have 3 tokens for a betting game and your goal is to reach 5 tokens before "
        "running out. Each turn you bet as many tokens as possible but not more than needed to reach 5. You win "
        "each bet with probability 2/3​. Compute the probability you reach 5 tokens before running out. (Give "
        "your answer as a reduced fraction.) 答案：62/77 把资金 0 和 5 当成终点，其他金额是状态。"
        "按“押到能押的最大额但不超过到 5 的差”建方程： P3=23+13P1, P1=23P2, P2=23P4, P4=23+13P3 ... "
        "解出从 3 开始的成功概率 P3=62/77。 本质是一个马尔可夫链/赌徒破产的问题。"
    ),
    doubt=(
        "The LaTeX in the source rendered as mangled digit soup ('P3=23+13P1'), so I reconstructed the fractions "
        "as 2/3 and 1/3 from the surrounding \\frac{2}{3}/\\frac{1}{3} markup that was also present. The stated "
        "system is not self-consistent as a gambler's-ruin chain under the stated betting rule, so either the "
        "poster's equations or my reading of the mangled text is off — but 62/77 is stated plainly twice."
    ),
))

records.append(dict(
    T1144112_COMMON,
    question_type="combinatorics",
    question_text=(
        "Question 17: A frog is traveling from point A(0,0) to point B(5,6) but each step can only be 1 unit up "
        "or 1 unit to the right. Additionally, the frog refuses to move three steps in the same direction "
        "consecutively. Compute the number of ways the frog can move from A to B."
    ),
    question_text_en=None,
    reported_answer=(
        "No closed form given. Poster: 这个问题我每次都是手算出来的，没有找到什么对于B(m,n)的general solution。"
        "但一般给的数字都会是6以下，问题不大。或者建议提前跑个dp，把各种mn都列出来。"
    ),
    source_quote=(
        "Question 17: A frog is traveling from point A(0,0) to point B(5,6) but each step can only be 1 unit up "
        "or 1 unit to the right. Additionally, the frog refuses to move three steps in the same direction "
        "consecutively. Compute the number of ways the frog can move from A to B. 答案：这个问题我每次都是手算出来的，"
        "没有找到什么对于B(m,n)的general solution。但一般给的数字都会是6以下，问题不大。或者建议提前跑个dp，把各种mn都列出来。"
        "如果有人想到什么general solution，欢迎探讨！"
    ),
    doubt=(
        "Very well attested — three separate 1point3acres threads report this same frog item with three "
        "different endpoints (B(5,6) here, B(7,4) in thread-1114232, B(5,4) in thread-1146142), which is exactly "
        "the 'same question, numbers changed' pattern posters describe for SIG. Low fabrication risk; the "
        "endpoint here is specific to this sitting."
    ),
))

# ---------------------------------------------------------------------------
# thread-1114232 : "SIG QR OA 青蛙题目+答案"
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="unknown",
    round="online_assessment",
    round_name="SIG QR OA",
    section_context="1hr 17道题的OA (17 questions in 1 hour)",
    question_type="combinatorics",
    question_text="青蛙想从（0，0）跳到（7，4），每次只能向右跳一格或向上跳一格。青蛙不愿意同方向连续跳三次。共多少种不同跳法？",
    question_text_en=(
        "A frog wants to jump from (0,0) to (7,4); each jump can only be one square to the right or one square "
        "up. The frog is unwilling to jump three times in a row in the same direction. How many different jump "
        "sequences are there?"
    ),
    reported_answer=(
        "30. Poster gives two derivations: a case count ('最终答案合计情况1的（1+6+9+2）和情况2的3*(2+2) 共30种'), "
        "and a composition count ('分拆4个R字符拆成2段有1种，拆成3段有3种，拆成4段有1种；7个U字符拆成4段有4种，拆成5段有10种；"
        "所以答案是3 * 4 + 2 * 1 * 4 + 1 * 10 = 30'). A commenter adds a DP: "
        "dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + dp[i-2][j-1] + dp[i-2][j-2], "
        "边界条件是 dp[0][0] = 2, dp[1][0] = dp[2][0] = dp[0][1] = dp[0][2] = 1"
    ),
    source_url="https://www.1point3acres.com/bbs/thread-1114232-1-1.html",
    source_quote=(
        "1hr 17道题的OA，题型和地里一样除了青蛙这道题比较复杂，其他题目都是比较典型的Bayes和小学简单奥数题。"
        "在这里分享一下青蛙跳格子这题我感觉算得比较快的方法。如果有更闪电运算的思路也请大家多多分享。 ... "
        "> 青蛙想从（0，0）跳到（7，4），每次只能向右跳一格或向上跳一格。青蛙不愿意同方向连续跳三次。共多少种不同跳法？ ... "
        "> 放1个，两种放法，共计2 * > (2, 1), (1, 2)，中间2个位置放2个，一种方法，共计2*1=2 > > **> 情况3**> : "
        "剩7-1=6个U，中间一个空位至多放1个，头尾之和至少为5，无解。 > 最终答案合计情况1的（1+6+9+2）和情况2的3*(2+2) 共30种。 ... "
        "这么分类数很容易数错一种方法是动态规划，不用复杂思考考虑最后的连续U序列和R序列，得到递推公式 "
        "dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + dp[i-2][j-1] + dp[i-2][j-2] ... "
        "边界条件是dp[0][0] = 2, dp[1][0] = dp[2][0] = dp[0][1] = dp[0][2] = 1 ... "
        "另一种方法是分拆4个R字符拆成2段有1种，拆成3段有3种，拆成4段有1种 ... 7个U字符拆成4段有4种，拆成5段有10种 ... "
        "所以答案是3 \\* 4 + 2 \\* 1 \\* 4 + 1 \\* 10 = 30"
    ),
    source_language="zh",
    post_date="unknown",
    poster_context=(
        "Standalone thread devoted to just this one question, titled 'SIG QR OA 青蛙题目+答案'. The post body "
        "and the whole comment thread of alternative solutions came back in the snippet, unusually — most of "
        "this thread was NOT point-gated."
    ),
    doubt=(
        "The strongest record in the shard: the question, the answer, and two independent reader-supplied "
        "solution methods all came back verbatim, and the poster explicitly frames it as 'the one hard question' "
        "in an otherwise-familiar 17-question set. The only real doubt is that the coordinates (7,4) differ from "
        "the (5,6) and (5,4) reported on sibling threads, so no single coordinate pair is 'the' SIG version."
    ),
))

# ---------------------------------------------------------------------------
# thread-1146142 : "[面试经验] Susquehanna OA 题 （新人求大米！！）"
# ---------------------------------------------------------------------------
T1146142 = "https://www.1point3acres.com/bbs/thread-1146142-1-1.html"
T1146142_COMMON = dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="online_assessment",
    round_name="Susquehanna OA",
    section_context="Overview: 60min, 17questions. Difficulty in increasing order.",
    source_url=T1146142,
    source_language="mixed",
    post_date="unknown",
    poster_context=(
        "Thread '[面试经验] Susquehanna OA 题 （新人求大米！！）' on the 海外面经 board, tagged sig. Poster is a "
        "first-time contributor asking for rice points; explicitly says they are only posting the hard questions "
        "they can remember. One reply asks the poster to share the remaining questions."
    ),
    doubt=(
        "The thread never states which role track (QT vs QR vs analyst) or whether internship or full-time, so "
        "role_track and level are left unknown rather than guessed. The 60min/17-question format matches what "
        "other threads call the QR-side 'Problem Solving Assessment', but that is inference, not what the thread says."
    ),
)

records.append(dict(
    T1146142_COMMON,
    question_type="expected_value",
    question_text=(
        "Q12 A spinner has three regions, and thee probabilities of landing in each region are 1/6, 1/6, 2/3. "
        "Compute the expected number of spins it would take to land in two distinct regions."
    ),
    question_text_en=None,
    reported_answer=None,
    source_quote=(
        "Overview: 60min, 17questions Difficulty in increasing order The first few questions are rather easy, "
        "I’ll just post the difficult questions that I can remember. Q17. A frog is traveling fro point A(0,0) "
        "to point B(5,4), but each step can only be 1 unit up or 1 unit to the right. Additionally, the frog "
        "refuses to move three steps in the sam [本帖隐藏的内容需要积分高于 188 才可浏览] "
        "ng simultaneously at some time. Q12 A spinner has three regions, and thee probabilities of landing in "
        "each region are 1/6, 1/6, 2/3. Compute the expected number of spins it would take to land in two "
        "distinct regions."
    ),
    doubt=(
        "Transcribed exactly including the poster's typo 'thee'. No answer was given in the thread. A studyx.ai "
        "photograph of a live Mettl 'Susquehanna Problem Solving Assessment' screen shows this same Question 12 "
        "with different region probabilities (1/6, 1/3, 1/2), which corroborates the item as genuinely SIG's "
        "while confirming the numbers rotate between sittings."
    ),
))

records.append(dict(
    T1146142_COMMON,
    question_type="combinatorics",
    question_text=(
        "Q17. A frog is traveling fro point A(0,0) to point B(5,4), but each step can only be 1 unit up or 1 "
        "unit to the right. Additionally, the frog refuses to move three steps in the sam[e direction "
        "consecutively — text cut off by the forum paywall]"
    ),
    question_text_en=None,
    reported_answer=None,
    source_quote=(
        "Q17. A frog is traveling fro point A(0,0) to point B(5,4), but each step can only be 1 unit up or 1 "
        "unit to the right. Additionally, the frog refuses to move three steps in the sam "
        "[本帖隐藏的内容需要积分高于 188 才可浏览]"
    ),
    doubt=(
        "Truncated mid-sentence by the points paywall; I completed the final clause in brackets only because "
        "the identical sentence appears in full on thread-1144112. The truncation is marked, not hidden. "
        "Typo 'fro point' is the poster's."
    ),
))

# ---------------------------------------------------------------------------
# thread-1086565 : "SIG Trader OA 新人求米！"  (QUANT TRADER track)
# ---------------------------------------------------------------------------
T1086565 = "https://www.1point3acres.com/bbs/thread-1086565-1-1.html"
T1086565_COMMON = dict(
    BASE,
    role_track="quant_trader",
    level="unknown",
    cycle="unknown",
    round="online_assessment",
    round_name="SIG Trader OA",
    section_context="unknown (poster only says the Trader OA resembles the QR one: 'Trader OA 与QR相似')",
    source_url=T1086565,
    source_language="mixed",
    post_date="unknown",
    poster_context=(
        "Thread 'SIG Trader OA 新人求米！' on 海外面经, tagged sig. Opening line: "
        "'Trader OA 与QR相似，分享一下面经，求大家赏赐大米。感谢！' — a first-time poster sharing a Trader-track "
        "OA recall and asking for rice points."
    ),
)

records.append(dict(
    T1086565_COMMON,
    question_type="probability",
    question_text=(
        "1. Assume that in a bakery, each customer buys only one item at a time. There is a 70% chance a "
        "customer will buy a croissant and a 30% chance a customer will buy a muffin. There are only 2 muffins "
        "left and 5 people are still waiting in line. Compute the probability that these two m[uffins ... — "
        "text cut off by the forum paywall]"
    ),
    question_text_en=None,
    reported_answer=None,
    source_quote=(
        "Trader OA 与QR相似，分享一下面经，求大家赏赐大米。感谢！ 1. Assume that in a bakery, each customer buys "
        "only one item at a time. There is a 70% chance a customer will buy a croissant and a 30% chance a "
        "customer will buy a muffin. There are only 2 muffins leftand 5 people are still waiting in line. "
        "Compute the probability that these two m [本帖隐藏的内容需要积分高于 188 才可浏览]"
    ),
    doubt=(
        "Truncated at 'these two m' by the paywall; I did NOT complete the sentence from the vendor mirrors that "
        "show it continuing '...muffins will be sufficient, i.e., no customer will want a muffin and find that "
        "there are none left', because that completion comes from csoahelp.com, an OA-proxy vendor, not from "
        "1point3acres. The 'leftand' run-together is the source's. This is the only QT-track thread in the shard "
        "with real question text, and its value is that it shows the QT OA reuses the QR item bank."
    ),
))

records.append(dict(
    T1086565_COMMON,
    question_type="logic_brainteaser",
    question_text=(
        "[... 5 toddlers at a round table, opening sentence cut off by the paywall ...] are some problems! "
        "i. Anna won't sit next to Brian or Eva. ii. Brian won't sit next to Charlie. iii. Dixie won't sit next "
        "to Eva or Charlie. If Dixie is sitting to the left of Anna, who is sitting to the left of Brian?"
    ),
    question_text_en=None,
    reported_answer=None,
    source_quote=(
        "[本帖隐藏的内容需要积分高于 188 才可浏览] are some problems! i. Anna won't sit next to Brian or Eva. "
        "ii. Brian won't sit next to Charlie. iii. Dixie won't sit next to Eva or Charlie. If Dixie is sitting "
        "to the left of Anna, who is sitting to the left of Brian?"
    ),
    doubt=(
        "The question's opening ('I need to seat 5 toddlers around a round table for lunch, but there ...') is "
        "behind the paywall — only the tail from 'are some problems!' onward was visible, so the names Anna/"
        "Brian/Charlie/Dixie/Eva are inferred to be the same cast from the constraint list, which does name all "
        "five. Confirms the seating item appears on the Trader track, not just QR."
    ),
))

# ---------------------------------------------------------------------------
# thread-1082367 (dup: thread-1082364) : "SIG QR 17题OA"
# text recovered from the tag-listing preview at /bbs/tag/sig-905-8.html
# ---------------------------------------------------------------------------
T1082367 = "https://www.1point3acres.com/bbs/thread-1082367-1-1.html"
T1082367_PREVIEW = (
    "SIG QR 17题OA 新题库…感觉还挺难的…还有两道新题是地里的，求绿色三角形的重量（6lb)， 扔2次骰子获得最大收益"
    "还有2种饼干，A有6个，B有8个，7个排成一排有多少排列组合 2^7-1还 ... | 海外面经 | physicsbamboo74 2024-8-23 "
    "| 3 2121 | 微信用户_nzr9e 2024-11-2 19:46"
)
T1082367_COMMON = dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="unknown",
    round="online_assessment",
    round_name="SIG QR 17题OA",
    section_context="17 questions; poster calls it a refreshed item bank ('新题库…感觉还挺难的…')",
    source_url=T1082367,
    source_language="zh",
    post_date="2024-08-23",
    poster_context=(
        "Posted by user physicsbamboo74 on 2024-08-23. The post body is point-gated on the thread page, but the "
        "company tag-listing page https://www.1point3acres.com/bbs/tag/sig-905-8.html carries an ungated ~200-char "
        "preview of the same post, which is where this text came from. The same preview is listed twice on that "
        "page (3 replies/2121 views and 4 replies/2240 views), matching duplicate thread ids 1082364 and 1082367."
    ),
)

records.append(dict(
    T1082367_COMMON,
    question_type="logic_brainteaser",
    question_text="求绿色三角形的重量（6lb)",
    question_text_en="Find the weight of the green triangle (6 lb)",
    reported_answer="6lb (given inline by the poster)",
    source_quote=T1082367_PREVIEW,
    doubt=(
        "Only a telegraphic one-line mention, not the question statement — the poster is listing which items "
        "appeared, not reproducing them. Value is corroborative: it independently confirms the green-triangle "
        "balance item and its answer of 6 lb, matching thread-1144112's Question 4, from a sitting a year earlier."
    ),
))

records.append(dict(
    T1082367_COMMON,
    question_type="expected_value",
    question_text="扔2次骰子获得最大收益",
    question_text_en="Roll a die twice, maximise the payoff",
    reported_answer=None,
    source_quote=T1082367_PREVIEW,
    doubt=(
        "Extremely terse — five characters naming a topic, not a question statement. I am recording it because "
        "the provenance is a real 1p3a post listing items that actually appeared, but nobody could reconstruct "
        "the item from this. The classic version (roll, optionally re-roll, take the second roll; fair value "
        "4.25) is a well-known textbook problem, so a reader might wrongly assume that framing."
    ),
))

records.append(dict(
    T1082367_COMMON,
    question_type="combinatorics",
    question_text="2种饼干，A有6个，B有8个，7个排成一排有多少排列组合 2^7-1还 ...",
    question_text_en=(
        "Two kinds of cookies, 6 of type A and 8 of type B; how many arrangements are there of 7 of them in a "
        "row? [poster writes] 2^7-1 ..."
    ),
    reported_answer="poster writes '2^7-1' inline before the preview is cut off",
    source_quote=T1082367_PREVIEW,
    doubt=(
        "The preview truncates at '2^7-1还 ...' so it is unclear whether 2^7-1 is the poster's answer, a wrong "
        "first guess they were about to correct, or part of a longer sentence. The stated counts (6 of A, 8 of "
        "B, arrange 7) don't obviously produce 2^7-1, which makes me suspect the poster compressed two different "
        "items into one clause."
    ),
))

records.append(dict(
    T1082367_COMMON,
    question_type="other",
    question_text="速度2mile/h. 问第二天几点出发（地里有）",
    question_text_en="speed 2 mile/h. Asks what time they set out the next day (already posted on the forum)",
    reported_answer=None,
    source_quote=(
        "新题库…感觉还挺难的… 还有两道新题是地里的，求绿色三角形的重量（6l "
        "[本帖隐藏的内容需要积分高于 188 才可浏览] 速度2mile/h. 问第二天几点出发（地里有）"
    ),
    doubt=(
        "A fragment surfacing from the far side of the paywall — just a rate and a question stem. It plainly "
        "belongs to the recurring SIG river/canoe rate problem (1p3a has a whole thread titled 'SIG math OA真题"
        "与答案: canoe time', thread-1092209, which stayed image-gated), but I could not recover the statement "
        "from any 1point3acres source, so I have deliberately not filled it in."
    ),
))

# ---------------------------------------------------------------------------
# thread-686183 : "SIG 1轮+2轮面经"  (interview rounds, not OA)
# ---------------------------------------------------------------------------
T686183 = "https://www.1point3acres.com/bbs/thread-686183-1-1.html"
T686183_QUOTE = (
    "SIG 面经 第一轮： 1. 圆里随机画n条线，问能把圆分成几分 （期望）？ 把分成的份数和交点个数对应起来，然后算交点个数的期望。 "
    "2. 扔硬币 进入 HTH HHT 之一就结束，问进入每一个的概率是多大？（不太记得具体ending state是啥了） 3. 三 ... "
    "> qldx 发表于 2020-11-11 11:12感觉好有难度，第一轮的第一题，和第二轮的第二题怎么做啊 ... "
    "| 有几个交点，就能推算出分成了几块 n 条线 m 个交点是 n+m+1 块 m = sum_{i,j} I（i,j）每两条线是否相交的indicator "
    "function 两条线相交的概率是1/3 （只用考虑4个点的顺序） 就可以算了"
)
T686183_COMMON = dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="phone_technical",
    round_name="第一轮 (first round)",
    section_context="first round of a two-round loop; the poster lists at least 3 questions",
    source_url=T686183,
    source_language="zh",
    post_date="2020-11",
    poster_context=(
        "Thread 'SIG 1轮+2轮面经' on 海外面经, tagged sig. Replies are dated 2020-11-11 and 2020-11-25, so the "
        "sitting is autumn 2020. Comment thread contains a detailed derivation of question 1 giving the expected "
        "number of regions as n + 1 + n(n-1)/6."
    ),
)

records.append(dict(
    T686183_COMMON,
    question_type="expected_value",
    question_text="1. 圆里随机画n条线，问能把圆分成几分 （期望）？",
    question_text_en=(
        "1. You draw n random lines (chords) in a circle; how many pieces do they divide the circle into (in "
        "expectation)?"
    ),
    reported_answer=(
        "Poster's own hint: 把分成的份数和交点个数对应起来，然后算交点个数的期望。 A commenter derives "
        "n + 1 + n*(n-1)/6, via 'n 条线 m 个交点是 n+m+1 块' and '两条线相交的概率是1/3 （只用考虑4个点的顺序）'."
    ),
    source_quote=T686183_QUOTE,
    doubt=(
        "The thread does not state the role track, so I left it unknown rather than assuming QR — this matters "
        "because SIG runs separate QT/QR loops. The question itself is verbatim and the comment thread contains "
        "two independent full derivations, so the item is solid; a third 1p3a thread (thread-1042392) shows the "
        "same question being asked in a 2024 first round, so it is a long-running SIG staple."
    ),
))

records.append(dict(
    T686183_COMMON,
    question_type="probability",
    question_text="2. 扔硬币 进入 HTH HHT 之一就结束，问进入每一个的概率是多大？（不太记得具体ending state是啥了）",
    question_text_en=(
        "2. Flip a coin; the game ends as soon as you hit one of HTH or HHT. What is the probability of ending "
        "on each one? (I don't remember exactly what the ending states were.)"
    ),
    reported_answer=None,
    source_quote=T686183_QUOTE,
    doubt=(
        "The poster themselves flags that they may be misremembering the ending states — '（不太记得具体ending "
        "state是啥了）' — so the specific patterns HTH and HHT are not reliable, only the shape of the question "
        "(a Penney's-game race between two length-3 patterns)."
    ),
))

# ---------------------------------------------------------------------------
# thread-1042392 : "SIG OA和一面/二面挂经"
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="unknown",
    round="phone_technical",
    round_name="一面 (first round)",
    section_context="OA + 一面 + 二面; poster says the OA itself was easy and entirely recycled ('OA就很简单 都是题库里的内容最多变了变数字')",
    question_type="expected_value",
    question_text=(
        "[statement point-gated; only the poster's solution and the follow-up discussion were visible] "
        "... /3*C^2_n 然后用交点个数算块数=刀数+交点数+1就完事了。 — and in the comments: 为什么两刀相交的概率是1/3呀 "
        "就是我们考虑圆上任意四个点（因为两刀两个点，三个点的情况测度为0，比起两刀四个点，可以忽略掉在算期望的时候）；"
        "用两条线连起来这四个点的方式一共三种，两种情况下这两刀是平行的，第三种情况是两刀是相交的，所以两刀相交的概率就是1/3."
    ),
    question_text_en=(
        "[statement gated] ... /3*C(n,2), then use the number of intersection points to get the number of "
        "pieces = number of cuts + number of intersections + 1, and you're done. — comment: why is the "
        "probability that two cuts intersect 1/3? Consider any four points on the circle (two cuts give two "
        "points each; the three-point case has measure zero and can be ignored when taking the expectation); "
        "there are three ways to join those four points with two lines, in two of them the cuts don't cross, in "
        "the third they do, so the probability two cuts intersect is 1/3."
    ),
    reported_answer="pieces = cuts + intersections + 1, with E[intersections] = (1/3)*C(n,2)",
    source_url="https://www.1point3acres.com/bbs/thread-1042392-1-1.html",
    source_quote=(
        ". .и 图片好像一次上传不完。OA就很简单 都是题库里的内容最多变了变数字 只要地里的题全都会做了，oa肯定没有问题的。 .. "
        "一面流程和其他地里小伙伴也差不多，先问了问要不要sponsor，然后说可以sponsor。然后问了问认不认识SIG工作的朋友什么的。 "
        "[本帖隐藏的内容需要积分高于 188 才可浏览] /3*C^2_n 然后用交点个数算块数=刀数+交点数+1就完事了。 "
        "二面就纯bq，问了一些地里其他一样的bq，类似与why QR? why SIG这种之类的。 莫名其妙挂了 不明白 ... "
        "匿名用户 发表于 2024-2-5 01:31. ---- 为什么两刀相交的概率是1/3呀 就是我们考虑圆上任意四个点"
        "（因为两刀两个点，三个点的情况测度为0，比起两刀四个点，可以忽略掉在算期望的时候）；用两条线连起来这四个点的方式一共三种，"
        "两种情况下这两刀是平行的，第三种情况是两刀是相交的，所以两刀相交的概率就是1/3.。求加米。。。 ... "
        "猫咪猫咪爪 发表于 2024-02-18 15:38:50很好的解法。一个小问题是：这两条线不一定“平行”，在圆内不相交即可。"
    ),
    source_language="zh",
    post_date="2024-02",
    poster_context=(
        "Thread 'SIG OA和一面/二面挂经' (OA + round 1 + round 2 rejection writeup) on the 数科面经 board, tagged "
        "sig. Role track is QR: the poster reports the round-2 behavioural questions were 'why QR? why SIG'. "
        "Comment timestamps are 2024-02-05 and 2024-02-18."
    ),
    doubt=(
        "The biggest caveat in this record: the question statement itself never came out from behind the "
        "paywall. What is verbatim is the poster's solution sketch and a commenter's proof of the 1/3 crossing "
        "probability. I have deliberately left question_text as that fragment rather than reconstructing a "
        "clean question, even though thread-686183 shows the same item stated plainly. Treat this as "
        "corroboration that the circle-cutting question recurs, not as an independent question statement."
    ),
))

# ---------------------------------------------------------------------------
# thread-719224 : "SIG Quantitative Evaluation 2021. OA 2021-02最新"  (QUANT DEVELOPER)
# ---------------------------------------------------------------------------
T719224 = "https://www.1point3acres.com/bbs/thread-719224-1-1.html"
T719224_COMMON = dict(
    BASE,
    role_track="quant_developer",
    level="unknown",
    cycle="unknown",
    round="online_assessment",
    round_name="SIG Quantitative Evaluation",
    section_context=(
        "总时长20分钟，一共是16道题 (16 questions in 20 minutes). A reply describing the same test adds: "
        "有四个section，第一个section里有4道题，要求全部做完，第二个里有5道题，希望做出尽量多的题，"
        "然后后面两个section都是附加题 (four sections: 4 compulsory, then 5, then two bonus sections)."
    ),
    source_url=T719224,
    source_language="mixed",
    post_date="2021-02",
    poster_context=(
        "Thread 'SIG Quantitative Evaluation 2021. OA 2021-02最新' on the 数科面经 board. Opening line states "
        "the role explicitly: '刚刚结束的sig（一家对冲基金）的quantitative developer 笔试！总时长20分钟，一共是16道题'. "
        "First-time poster asking for rice points. This is the only quant-developer-labelled OA recall I recovered."
    ),
)

records.append(dict(
    T719224_COMMON,
    question_type="logic_brainteaser",
    question_text=(
        "1. Knights always tell truth, Knaves always tell lies, and Visitors can either tell truth or lie. "
        "These people(One Knight, One Knaves, One Visitor) [text cut off by the forum paywall]"
    ),
    question_text_en=None,
    reported_answer=None,
    source_quote=(
        "刚刚结束的sig（一家对冲基金） 的quantitative developer 笔试！总时长20分钟，一共是16道题。。简直不能再难"
        "（md得什么脑子才可以进这种公司？？？？）然后我是第一次发这个东西！ 折腾好久才写出来这些东西！"
        "因为地里乱七八糟规定太多，所以一直没有发成功！！！ 手有余香！！真的是新人求大米！一粒就好谢谢您 "
        ".1point3acres -baidu 1point3acres 1. Knights always tell truth, Knaves always tell lies, and Visitors "
        "can either tell truth or lie. These people(One Knight, One Knaves, One Visitor)"
    ),
    doubt=(
        "Truncated right where the actual statements of the three characters would begin, so the puzzle is not "
        "reconstructible — only the setup and the unusual three-type variant (Knight / Knave / Visitor, rather "
        "than the standard two-type Knights-and-Knaves) are established. That three-type variant is itself the "
        "useful signal, since it is not the textbook version."
    ),
))

records.append(dict(
    T719224_COMMON,
    question_type="expected_value",
    question_text=(
        "If day is a “Good” Day, [there] is a 60% chance that the next day will be “Good” and a 40% chance it "
        "will be “Bad”. If day is a “Bad” Day, there is a 70% chance that the next day will be “Bad” and 30% "
        "chance it will be “Good”. If today is Good Day, on average, how many days do we have to wait until the "
        "next “Bad” Day?"
    ),
    question_text_en=None,
    reported_answer=(
        "No final number stated. A commenter gives the full method: 如果今天是好天气，1天后是坏天气的概率是0.4，"
        "2天后坏天气的概率是0.6*0.4，3天后坏天气的概率是0.6*0.6*0.4 ... n天后的坏天气概率是0.6^(n-1)*0.4, then sums "
        "n * P(n) by the 错位相减 (shift-and-subtract) trick, noting it matches the Markov-chain answer."
    ),
    source_quote=(
        "ge, how many days do we have to wait until the next “Bad” Day? 这个有很多种解法，一种麻烦的是马尔可夫过程，"
        "或者就是找规律然后用等比数列求和（*0.6 错位相减） ... 我就直接打字了。如果今天是好天气，1天后是坏天气的概率是0.4，"
        "2天后坏天气的概率是0.6*0.4，3天后坏天气的概率是0.6*0.6*0.4，4天后的坏天气概率是0.6^3*0.4 . .... "
        "以此类推你可以找规律，n天后的坏天气概率是0.6^(n-1)*4 ... If day is a “Good” Day, is a 60% chance that the "
        "next day will be “Good” and a 40% chance it will be “Bad”. If day is a “Bad” Day, there is a 70% chance "
        "that the next day will be “Bad” and 30% chance it will be “Good”. If today is Good Day, on average, how "
        "many days do we have to wait until the next “Bad” Day?"
    ),
    doubt=(
        "The snippet returned this question's text in two disjoint pieces — the tail ('ge, how many days ...') "
        "appeared before the head — so I reassembled them into reading order. The head as returned reads 'If day "
        "is a “Good” Day, is a 60% chance', missing 'there'; I bracketed that one word rather than silently "
        "fixing it. Everything else is character-for-character. Note the commenter's 'n天后的坏天气概率是"
        "0.6^(n-1)*4' drops the decimal point on 0.4 — that typo is theirs."
    ),
))

records.append(dict(
    T719224_COMMON,
    question_type="probability",
    question_text=(
        "[statement point-gated; reconstructed only as far as the poster's own description] 第二题 ... "
        "要8和10都出现才可以 — a repeated-trial problem in which the game is won once both an 8 and a 10 have "
        "occurred. The poster's Markov states use per-step probabilities 0.07 (an 8), 0.08 (a 9), 0.09 (a 10) "
        "and 0.76 (none of them)."
    ),
    question_text_en=None,
    reported_answer="p(s) = 13118 / 21675",
    source_quote=(
        "我刚刚发现我第二题理解错了，我之前理解的是只要出现8或者10就算赢，所以之前那个帖子里算的概率都将近1了。"
        "现在我理解就是要8和10都出现才可以。我重新算了一下，还是markov方法： 假设从初始状态到最终状态(8和10出现)的概率是p(s), "
        "从出现一次8的状态到最终状态的概率是p(8)，相应的p(9)和p(10)是同样的意思，然后p(8,9)是从出现了一次8和9的状态到最终状态，"
        "同理p(9, 10)。然后就可以列方程： p(s) = 0.76p(s) + 0.07p(8) + 0.08p(9) + 0.09p(10) "
        "p(8) = 0.83p(8) + 0.09 + 0.08p(8,9). p(9) = 0.76p(9) + 0.07p(8,9) + 0.09p(9, 10). "
        "p(10) = 0.85p(10) + 0.07 + 0.08p(9,10). p(8,9) = 0.83p(8,9) + 0.09 p(9,10) = 0.85p(9,10) = 0.07 "
        "最后解出来p(s)=13118 / 21675,但是可以看出来这个方法计算量很大，而且超级容易出错。我很担心就20分钟，"
        "这道题用这个方法得用去一大半时间，然后还有可以因为计算出错。我目前没有想到其他更简单的方法了"
    ),
    doubt=(
        "The weakest question_text in the shard: the statement never appeared, so all I can honestly report is "
        "what the poster's own correction reveals about it. I have not invented a statement. The poster also "
        "says they initially misread the question, so even their description is second-pass. The transition "
        "probabilities 0.07/0.08/0.09 don't correspond to any obvious dice or card mechanism, which suggests the "
        "original gave an explicit probability table. Retrieved from page 2 of the thread "
        "(https://www.1point3acres.com/bbs/thread-719224-2-1.html)."
    ),
))

records.append(dict(
    T719224_COMMON,
    question_type="other",
    question_text="有个求五次导数的题我花了很久还做错了，我看了地里这个题就是有技巧可以很快的算出答案",
    question_text_en=(
        "There was a question asking for a fifth derivative that took me ages and I still got it wrong; when I "
        "looked at this question on the forum it turns out there's a trick that gets the answer quickly."
    ),
    reported_answer=None,
    source_quote=(
        "不是的，也是数学题，题型和你这个差不多。有四个section,第一个section里有4道题，要求全部做完，第二个里有5道题，"
        "希望做出尽量多的题，然后后面两个section都是附加题，他们说如果你前两个里的题都做出来并认为都对的时候，可以尝试这里的题。"
        "我只做完了前两个section里的题，就是算各种概率，排列组合还有一点微积分求导求极限这类题。"
        "有个求五次导数的题我花了很久还做错了，我看了地里这个题就是有技巧可以很快的算出答案，这样就可以节省时间作出更多的题了。"
    ),
    doubt=(
        "This is a commenter describing their own SIG sitting, not the thread author's, and it names a question "
        "type ('find the fifth derivative') without stating the function — so it is a topic attestation, not a "
        "recoverable question. Recording it only because it is the sole 1p3a evidence I found that the SIG OA "
        "includes calculus (求导求极限) alongside probability and combinatorics."
    ),
))

# ---------------------------------------------------------------------------
# thread-1143308 : "SIG 26 NG OA - General Coding Assessment"
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="unknown",
    level="new_grad",
    cycle="2026",
    round="online_assessment",
    round_name="SIG 26 NG OA - General Coding Assessment",
    section_context="70分钟，4道题目 (4 problems in 70 minutes)",
    question_type="coding_algorithms",
    question_text="第一题 Given an array of integers numbers, [text cut off by the forum paywall]",
    question_text_en="Problem 1: Given an array of integers numbers, [cut off]",
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/thread-1143308-1-1.html",
    source_quote=(
        "注册一亩三分地论坛，查看更多干货！ 您需要登录才可以下载或查看附件。没有帐号？注册账号 x "
        "70分钟，4道题目，比较简单 第一题 Given an array of integers numbers, "
        "[本帖隐藏的内容需要积分高于 188 才可浏览] 希望对大家有帮助。求加米看面经！加米不会扣米~ ... "
        "lasa 发表于 2025-9-3 15:39最后一题这么难吗 难度一般，主要是实现起来比较麻烦 ... "
        "微信用户_873ead5 发表于 2025-9-9 17:08你后面有后续嘛，我oa过了但是发了拒信 没有后续也没有拒信，被ghost了"
    ),
    source_language="mixed",
    post_date="2025-09",
    poster_context=(
        "Thread 'SIG 26 NG OA - General Coding Assessment' on 海外面经, tagged sig. Replies dated 2025-09-03 and "
        "2025-09-05/09 place the sitting in the 2026 new-grad cycle. Poster describes it as 'fairly easy'; a "
        "commenter says the last problem is 'average difficulty, just fiddly to implement'."
    ),
    doubt=(
        "Cut off after eight words, so there is no usable problem here — only the format (4 problems / 70 "
        "minutes) is established. Critically, the thread says 'General Coding Assessment' and never names a "
        "quant role, so this may be the plain SWE track rather than quant developer; I have left role_track "
        "unknown rather than guess, per the labelling rule."
    ),
))

# ---------------------------------------------------------------------------
# thread-1009682 : "SIG 2024 OA 附加第一题小思路"
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="2024",
    round="online_assessment",
    round_name="SIG 2024 OA",
    section_context="two coding problems",
    question_type="coding_algorithms",
    question_text="题目地里都有，第一题是战船游戏，第二题是 Leetcode 98。",
    question_text_en=(
        "The problems are all already on the forum: problem 1 is the battleship game, problem 2 is LeetCode 98."
    ),
    reported_answer=(
        "Poster's approach to problem 1: O(n) 的复杂度，过一遍格子记录血量，再过一遍坐标列表执行攻击操作 "
        "(one pass over the grid recording ship hit points, then one pass over the coordinate list applying attacks)."
    ),
    source_url="https://www.1point3acres.com/bbs/thread-1009682-1-1.html",
    source_quote=(
        "注册一亩三分地论坛，查看更多干货！ 您需要登录才可以下载或查看附件。没有帐号？注册账号 x "
        "题目地里都有，第一题是战船游戏，第二题是 Leetcode 98。 说一下第一题的思路，我看有说超时的，基本上不太可能，因 "
        "[本帖隐藏的内容需要积分高于 188 才可浏览] (n) 的复杂度，过一遍格子记录血量，再过一遍坐标列表执行攻击操作。"
    ),
    source_language="zh",
    post_date="unknown",
    poster_context=(
        "Thread 'SIG 2024 OA 附加第一题小思路' (a note on the approach to problem 1) on 海外面经, tagged sig. The "
        "poster is commenting on problems already circulating on the forum rather than transcribing them."
    ),
    doubt=(
        "Names the problems rather than stating them ('battleship game', 'LeetCode 98' = Validate Binary Search "
        "Tree). No role track given, and the SIG tag pages show this same battleship+LC98 pair recurring in "
        "threads explicitly labelled 'SDE Intern' and 'Software Developer - Campus', so this is most likely the "
        "software track rather than a quant track — recorded with role_track unknown and flagged accordingly."
    ),
))

# ---------------------------------------------------------------------------
# thread-1019255 : "SIG 终面"
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="superday",
    round_name="final round (终面) — two technical rounds",
    section_context=(
        "Commenter reports the final round is two rounds, not four hours as advertised; second round required "
        "only pseudocode ('第二轮的题目虽然跟楼主的不同，但也是很简单，而且只需要写psudo code')."
    ),
    question_type="coding_algorithms",
    question_text="请问能再说一下收银台那题么, 是不是object-oriented programming类型,让你一个设计",
    question_text_en=(
        "Could you say more about the cash-register question? Is it an object-oriented programming type where "
        "they have you design a ...?"
    ),
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/thread-1019255-1-1.html",
    source_quote=(
        "本帖最后由 匿名 于 2023-10-19 01:31 编辑 “本来说要面四个小时，结果面了两小时就结束了” - 楼主不用自我怀疑，"
        "他们final round就是两轮的，面之前已经跟HR确认过，不存在面挂了不继续的可能性。 ... "
        "我从phone screening开始就各种秒，final round第一轮和楼主是一模一样的题目，轻松秒杀。写完code一通讲解，清晰明了，"
        "面试官后来都没啥可问的了，只能在那做各种假设问我怎么改code应对。第二轮的题目虽然跟楼主的不同，但也是很简单，"
        "而且只需要写psudo code，也是直接秒杀。 ... 多谢楼主分享.请问能再说一下收银台那题么, "
        "是不是object-oriented programming类型,让你一个设计"
    ),
    source_language="zh",
    post_date="2023-10-19",
    poster_context=(
        "Thread 'SIG 终面' on 海外面经, tagged sig. The original post is point-gated; what surfaced is a long "
        "reply from another candidate who went through the same loop and got the identical first-round question, "
        "plus a third reader asking the OP to elaborate on the cash-register problem."
    ),
    doubt=(
        "Weak as a question record: what I have is a reader *asking about* the cash-register question, not the "
        "question itself, and the asker's own sentence is truncated. It establishes that a cash-register / "
        "OOD-style design problem was used in a SIG final round in October 2023, and nothing more. Role track "
        "is not stated anywhere in the visible text."
    ),
))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    for rec in records:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"wrote {len(records)} records to {OUT}")
