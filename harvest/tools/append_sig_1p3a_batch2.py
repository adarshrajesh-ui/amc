#!/usr/bin/env python3
"""Append the second harvest pass of SIG x 1point3acres records to the shard JSONL.

Same rule as pass one: every record below was transcribed from a WebSearch result
"Highlights" block that quoted a www.1point3acres.com URL. Nothing was written from
memory, and nothing was taken from a prep-vendor or content-farm page.
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

records = []

# ---------------------------------------------------------------------------
# thread-1167938 : "SIG Phone + Onsite"
# Self-labelled 2026(1-3月) 码农类General 硕士 全职@sig - 内推 - Onsite | Fail
# ---------------------------------------------------------------------------
T1167938 = "https://www.1point3acres.com/bbs/thread-1167938-1-1.html"
T1167938_QUOTE = (
    "SIG Phone + Onsite|sig面经|一亩三分地海外面经版 ... # SIG Phone + Onsite ... "
    "2026(1-3月) 码农类General 硕士 全职@sig - 内推 - Onsite | 🙁 Negative 😐 Average | Fail | 在职跳槽 ... "
    "电面就是Movie Theatre那道题。Onsite的OOD轮面的是设计超市收银台，coding面的是新闻标题提取股票"
)
T1167938_COMMON = dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="2026",
    source_url=T1167938,
    source_language="zh",
    post_date="2026-01",
    poster_context=(
        "Thread 'SIG Phone + Onsite' on 海外面经, tagged sig. The forum's own structured header reads "
        "'2026(1-3月) 码农类General 硕士 全职@sig - 内推 - Onsite | Negative / Average | Fail | 在职跳槽' "
        "— i.e. a master's-level experienced hire, referred, who failed at onsite. The entire post body "
        "that surfaced is a single sentence naming three questions."
    ),
    doubt=(
        "Role-track caveat that applies to all three records from this thread: the forum's own category "
        "for the post is 码农类General (general software engineering), NOT a quant category. SIG runs a "
        "separate SWE pipeline, so this is most likely the software track rather than quant developer. "
        "I have therefore left role_track 'unknown' rather than claiming quant_developer. The value here "
        "is that it independently corroborates the cash-register/checkout design item already recorded "
        "from thread-1019255 (October 2023), showing the item is still in rotation in 2026."
    ),
)

records.append(dict(
    T1167938_COMMON,
    round="phone_technical",
    round_name="电面 (phone interview)",
    section_context="phone screen preceding a multi-round onsite",
    question_type="coding_algorithms",
    question_text="电面就是Movie Theatre那道题。",
    question_text_en="The phone interview was that Movie Theatre problem.",
    reported_answer=None,
    source_quote=T1167938_QUOTE,
))

records.append(dict(
    T1167938_COMMON,
    round="superday",
    round_name="Onsite — OOD 轮 (object-oriented design round)",
    section_context="one of several onsite rounds",
    question_type="coding_algorithms",
    question_text="Onsite的OOD轮面的是设计超市收银台",
    question_text_en=(
        "The onsite OOD round was: design a supermarket checkout counter."
    ),
    reported_answer=None,
    source_quote=T1167938_QUOTE,
))

records.append(dict(
    T1167938_COMMON,
    round="superday",
    round_name="Onsite — coding 轮",
    section_context="one of several onsite rounds",
    question_type="coding_algorithms",
    question_text="coding面的是新闻标题提取股票",
    question_text_en=(
        "The coding round was: extract stocks (ticker symbols) from news headlines."
    ),
    reported_answer=None,
    source_quote=T1167938_QUOTE,
))

# ---------------------------------------------------------------------------
# thread-686183 : "SIG 1轮+2轮面经" — SECOND round (first round already captured
# in pass one). A later snippet window exposed the round-2 discussion.
# ---------------------------------------------------------------------------
T686183 = "https://www.1point3acres.com/bbs/thread-686183-1-1.html"
T686183_R2_QUOTE = (
    "> qldx 发表于 2020-11-11 11:12感觉好有难度，第一轮的第一题，和第二轮的第二题怎么做啊 ... "
    "| 个挂掉了，没答出来，给了提示说可以构造一些例子，然后构造了一个右上角是I其他是0的矩阵，也没全算完，"
    "大概猜了一下是2/3n 求大米呀！ | ... "
    "| 有几个交点，就能推算出分成了几块 n 条线 m 个交点是 n+m+1 块 ... rank那个可以看这里 "
    "https://math.stackexchange.com/q ... t-matrix-if-a2-ne-0 | ... "
    "| 感谢！ 我估计我写错了，rank那道题我应该是会的，我当时应该是想问第3题，不过我事后也找到了一个解释，说是不一定，是吧？ | ... "
    "| 请问第二轮第一题是在那个三角形平面，还是四面体内，做sampling | ... | 想问三角形要怎样做？ |"
)
T686183_R2_COMMON = dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="phone_technical",
    round_name="第二轮 (second round)",
    section_context="second round of a two-round loop; poster reports failing on the matrix question",
    source_url=T686183,
    source_language="zh",
    post_date="2020-11",
    poster_context=(
        "Thread 'SIG 1轮+2轮面经' on 海外面经, tagged sig; replies dated 2020-11-11 and 2020-11-25. "
        "The round-2 question statements themselves are point-gated — what surfaced is the poster's "
        "account of failing one of them plus readers asking follow-up questions about them by name."
    ),
)

records.append(dict(
    T686183_R2_COMMON,
    question_type="other",
    question_text=(
        "[第二轮第二题 — statement point-gated. Recoverable only from the poster's account of attempting it "
        "and a reader's pointer to the matching math.stackexchange page:] "
        "个挂掉了，没答出来，给了提示说可以构造一些例子，然后构造了一个右上角是I其他是0的矩阵，也没全算完，大概猜了一下是2/3n "
        "… rank那个可以看这里 https://math.stackexchange.com/q ... t-matrix-if-a2-ne-0"
    ),
    question_text_en=(
        "[Round 2, question 2 — statement gated.] The poster: 'I died on this one, couldn't answer it. "
        "They hinted that I could construct some examples, so I constructed a matrix with I in the "
        "top-right corner and 0 elsewhere; I didn't finish the calculation and roughly guessed 2/3 n.' "
        "A commenter points to a math.stackexchange page whose URL slug ends '...t-matrix-if-a2-ne-0', "
        "i.e. a question about the rank of a matrix given that A^2 is not zero."
    ),
    reported_answer="No confirmed answer. The poster guessed 2/3·n and says they got the question wrong.",
    source_quote=T686183_R2_QUOTE,
    doubt=(
        "The single weakest kind of record I am willing to keep: the question was never stated in any "
        "visible text. What is verbatim is (a) the poster saying they failed a 'rank' question and "
        "describing the example matrix they built, and (b) a reader naming it 'rank那道题' and linking a "
        "math.stackexchange page about the rank of a matrix with A^2 ≠ 0. The middle of that URL is "
        "elided by the forum's own link-shortening ('.../q ... t-matrix-if-a2-ne-0'), so I cannot even "
        "state the full linked title, and I have NOT guessed at it. Recorded because it is the only "
        "evidence in the whole shard that SIG asks a linear-algebra question at all — every other item "
        "is probability, combinatorics or logic."
    ),
))

records.append(dict(
    T686183_R2_COMMON,
    question_type="probability",
    question_text=(
        "[第二轮第一题 — statement point-gated. All that surfaced are two readers asking about it:] "
        "请问第二轮第一题是在那个三角形平面，还是四面体内，做sampling … 想问三角形要怎样做？"
    ),
    question_text_en=(
        "[Round 2, question 1 — statement gated.] Reader: 'Can I ask whether round 2 question 1 does the "
        "sampling in that triangular plane, or inside the tetrahedron?' Another reader: 'I want to ask "
        "how to do the triangle one.'"
    ),
    reported_answer=None,
    source_quote=T686183_R2_QUOTE,
    doubt=(
        "Same problem as the record above: this is readers asking about a question, not the question. "
        "It establishes only that round 2 opened with a geometric-sampling problem involving a triangle "
        "and/or a tetrahedron, and that even the readers were unsure which. I deliberately did not "
        "reconstruct a plausible statement (e.g. 'sample a uniform point in a tetrahedron and compute…') "
        "because no such sentence appeared anywhere in the source."
    ),
))

# ---------------------------------------------------------------------------
# thread-1023600 : "Sig quant OA" — the umbrella / rain Markov-chain item.
# Text recovered from page 4 of the thread (…/thread-1023600-4-1.html).
# ---------------------------------------------------------------------------
T1023600 = "https://www.1point3acres.com/bbs/thread-1023600-4-1.html"
records.append(dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="online_assessment",
    round_name="Sig quant OA",
    section_context="unknown; the thread ran to at least 4 pages of replies working this one item",
    question_type="probability",
    question_text=(
        "[题面被积分墙挡住；以下为帖中讨论所还原的题目结构] 一个人有 N 把伞（讨论中 N=2），在家和办公室之间往返；"
        "state 是代表我在得地方有几把伞。下雨概率 p，不下雨概率 q。问淋湿的概率。"
        "讨论原文：「state是代表我在得地方有几把伞 1 到1是 1-p（没下雨） 1到0是0 "
        "（因为如果没下雨不带伞就不会动 带伞就会让在的地方变成2把伞 所以下雨了 1-》2 是p）」"
    ),
    question_text_en=(
        "[Statement behind the points paywall; this is the structure recoverable from the thread's own "
        "discussion.] A person owns N umbrellas (N = 2 in the discussion) and commutes between home and "
        "the office; the Markov state is the number of umbrellas at the location where they currently "
        "are. Rain has probability p, no rain probability q. Asked: the probability of getting wet. "
        "Verbatim from the thread: 'the state represents how many umbrellas are at the place I am; 1→1 "
        "is 1−p (no rain); 1→0 is 0 (because if it does not rain you do not take an umbrella so nothing "
        "moves, and if you do take one the place you are at becomes 2 umbrellas, so given it rains, "
        "1→2 is p).'"
    ),
    reported_answer=(
        "Contested in the thread. One commenter states a general formula: 「通用的解是 1/（ pq/(N+q) ）"
        "p是下雨概率 q是不下雨概率 N是伞的个数」. Another commenter corrects the framing: "
        "「这道题应该没有absorption state 吧，应该是一个recurrent class吧。后面的F乘以【1，1，1】计算从transient "
        "到absorption 对这道题不适用吧。」, and the first agrees: 「嗯 你说的对 因为再0得时候一定会回到那个2得state, "
        "所以算abosrption并不准确 算P recurrent 0然后得再乘以p就是淋湿得概率」."
    ),
    source_url=T1023600,
    source_quote=(
        "> ning666 发表于 2023-11-6 02:25你好，请问是3个state吗？0把伞，1把伞，2把伞？那0分别到0，1，2的probability是什么啊？"
        "我只知道0到2是 ... | state是代表我在得地方有几把伞 1 到1是 1-p（没下雨） 1到0是0 "
        "（因为如果没下雨不带伞就不会动 带伞就会让在的地方变成2把伞 所以下雨了 1-》2 是p 希望这些对你有帮助啦 | ... "
        "> 纯情的消防车 发表于 2023-11-3 18:33通用的解是 1/（ pq/(N+q) ）p是下雨概率 q是不下雨概率 N是伞的个数 ... "
        "| 这道题应该没有absorption state 吧， 应该是一个recurrent class吧。 后面的F乘以【1，1，1】计算从transient "
        "到absorption 对这道题不适用吧。 还是很感谢提供思路的。 | ... "
        "| 嗯 你说的对 因为再0得时候一定会回到那个2得state, 所以算abosrption并不准确 算P recurrent 0然后得再乘以p就是淋湿得概率 | ... "
        "> 汤圆yaya 发表于 2023-11-6 11:29 0到2应该是1. "
        "https://www.stat.berkeley.edu/%7Ealdous/150/takis_exercises.pdf Q5 ... "
        "| 0-2就是 伞都放在了办公室 然后从家出发去了办公室 所以你在得地方就会有2顶伞 0-0应该是不存在得 因为伞得总数是2把 "
        "0-1应该也是不存在的 因为只有2把伞 除非有一把伞再路上被吃掉了 所以概率也是0 刚刚发的汤圆得那个第五题解法应该是对的 "
        "python得验证也发了数值应该是对的上的 |"
    ),
    source_language="zh",
    post_date="2023-11",
    poster_context=(
        "Thread 'Sig quant OA' on 海外面经, tagged sig. Replies dated 2023-11-03 through 2023-11-09. "
        "The original statement is point-gated but the thread generated four pages of argument about how "
        "to set up the Markov chain, and that argument is ungated, which is why the item is recoverable "
        "at all. Commenters themselves note the item matches Q5 of a Berkeley stochastic-processes "
        "exercise sheet (aldous/150/takis_exercises.pdf)."
    ),
    doubt=(
        "Two real problems. First, the question statement never appeared — I reconstructed only the "
        "structure the thread's own participants describe, and marked that explicitly in question_text "
        "rather than writing a clean problem. Second, and more seriously, the commenters themselves link "
        "this to a standard Berkeley/Durrett textbook exercise ('Wandering Umbrellas'), so this is a "
        "known textbook problem; under the shard's exclusion rule a textbook-only item would be "
        "rejected, but here the attestation is a 1point3acres poster saying it appeared on their SIG "
        "quant OA, which is candidate recall, not a textbook citation. The quoted general formula "
        "'1/( pq/(N+q) )' also does not match the standard result and is very likely a garbled "
        "transcription by that commenter — I have reproduced it exactly rather than repairing it."
    ),
))

# ---------------------------------------------------------------------------
# tag page /bbs/tag/sig-905-6.html : ungated ~200-char preview of a 海外面经
# thread by 绮色佳 (2024-10-09) listing two questions verbatim.
# ---------------------------------------------------------------------------
T905_6_TAG = "https://www.1point3acres.com/bbs/tag/sig-905-6.html"
T905_6_QUOTE = (
    "| 1. 1—20选三个数字，一个数字是另外两个平均数的概率2. 一个魔方，每面刷成绿的，往地上扔朝外的五面都是白的，"
    "问是最中间那块的概率求加米谢谢🙏 | 海外面经 | 2 2583 | 绮色佳 2024-10-9 04:40 |"
)
T905_6_COMMON = dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="unknown",
    round_name="unknown",
    section_context="unknown — the preview lists two questions and nothing about the format",
    source_url=T905_6_TAG,
    source_language="zh",
    post_date="2024-10-09",
    poster_context=(
        "Recovered from the ungated ~200-character thread preview on the SIG company tag-listing page "
        "https://www.1point3acres.com/bbs/tag/sig-905-6.html. The thread itself (2 replies, 2583 views, "
        "board 海外面经, last post by 绮色佳 on 2024-10-09) is point-gated, but the preview reproduces the "
        "poster's numbered list of the two questions in full, followed by 求加米谢谢🙏 — the rice-point "
        "request that marks a genuine first-hand recall post."
    ),
)

records.append(dict(
    T905_6_COMMON,
    question_type="probability",
    question_text="1. 1—20选三个数字，一个数字是另外两个平均数的概率",
    question_text_en=(
        "1. Pick three numbers from 1 to 20; what is the probability that one of them is the average of "
        "the other two?"
    ),
    reported_answer=None,
    source_quote=T905_6_QUOTE,
    doubt=(
        "Terse but complete as a question — the poster wrote it as a one-line list item, so nothing is "
        "truncated, and no answer was given. The ambiguity is inherent to the poster's compression: it "
        "does not say whether the three numbers are drawn without replacement or whether order matters. "
        "I could not find a second 1point3acres thread reporting this item, so it rests on one preview. "
        "Note that the exact same 'pick 3 numbers from 1–20, one is the average of the other two' item "
        "also appears on a programhelp.net listicle, which raises the usual copying question, but the "
        "1p3a post predates nothing I can verify either way."
    ),
))

records.append(dict(
    T905_6_COMMON,
    question_type="probability",
    question_text=(
        "2. 一个魔方，每面刷成绿的，往地上扔朝外的五面都是白的，问是最中间那块的概率"
    ),
    question_text_en=(
        "2. A Rubik's cube with every face painted green; you throw it on the ground and all five "
        "outward-facing sides are white — what is the probability that it is the very middle piece?"
    ),
    reported_answer=None,
    source_quote=T905_6_QUOTE,
    doubt=(
        "Transcribed exactly, including the internal contradiction in the poster's own wording: they say "
        "every face is painted green (每面刷成绿的) and then that the five visible sides are white. Almost "
        "certainly the poster garbled the colours while compressing, and the intended item is the "
        "classic painted-cube Bayes problem (a 3×3×3 cube painted on the outside, broken up, one small "
        "cube drawn and rolled). Because the shard rule is to preserve the source's language rather than "
        "repair it, I have left the contradiction in place instead of silently 'fixing' green to white. "
        "Treat the numbers as unreliable and the item as a topic attestation."
    ),
))

# ---------------------------------------------------------------------------
# thread-1144112 : a fresh snippet window exposed a stray answer belonging to
# one of the point-gated middle questions (Q7–Q15).
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="2026",
    round="online_assessment",
    round_name="SIG Quant Research OA",
    section_context="17 questions in 1 hour; this belongs to the point-gated middle block (Q7–Q15)",
    question_type="expected_value",
    question_text=(
        "[题面被积分墙挡住，只有答案从 Q3 与 Q16 之间漏出来：] 由于对称性，4 种牌相加，期望 = 4 × (3/14) = 6/7。"
    ),
    question_text_en=(
        "[Statement point-gated; only the answer leaked out, sitting between Q3 and Q16 in the page:] "
        "'By symmetry, summing over the 4 suits/kinds of card, the expectation = 4 × (3/14) = 6/7.'"
    ),
    reported_answer="期望 = 4 × (3/14) = 6/7",
    source_url="https://www.1point3acres.com/bbs/thread-1144112-1-1.html",
    source_quote=(
        "Question 3: 1000 people were surveyed about their preferred method of exercise. The table shows "
        "results by age group. If you meet a 33-year-old who took the survey, compute the probability she "
        "prefers swimming.由于对称性，4 种牌相加，期望 = 4 × (3/14) = 6/7。 Question 16: Suppose you have 3 "
        "tokens for a betting game and your goal is to reach 5 tokens before running out."
    ),
    source_language="mixed",
    post_date="unknown",
    poster_context=(
        "Thread '2026 SIG Quant Research OA整理 【带答案】' on 海外面经. The poster numbered all 17 questions "
        "with worked answers; questions 7 through 15 sit behind the 188-point paywall. This orphaned "
        "answer sentence appears in the search index glued directly onto the end of Question 3, with no "
        "question of its own, which is how the paywall truncation manifests."
    ),
    doubt=(
        "This is an answer with no question. I am recording it because it is the only trace anywhere in "
        "the shard of what the gated middle block of the 2026 QR OA contains, and because 'expectation = "
        "4 × 3/14' pins down a card problem with a 14-ish denominator quite specifically. But nobody can "
        "reconstruct the item from this, and my labelling it question_type 'expected_value' is inference "
        "from the word 期望 in the answer. In the earlier pass I mistakenly read this fragment as part of "
        "Q3's answer; this fresh snippet window shows it is a separate orphan, which is why it now gets "
        "its own record."
    ),
))

# ---------------------------------------------------------------------------
# thread-1157580 : "SIG 求Quant Research and Sys Trading的recruiter call经验！感恩"
# Topic attestation for the recruiter/HR round.
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="2026",
    round="phone_technical",
    round_name="recruiter call / HR筛选",
    section_context="recruiter screen for Quant Research and Systematic Trading; 2025(10-12月) 金工类 博士 全职",
    question_type="probability",
    question_text=(
        "会问你喜欢research还是trading, why sig, 绿皮书等公交车类型的probablity问题，还有简单的markov骰子问题"
    ),
    question_text_en=(
        "They will ask whether you prefer research or trading, why SIG, green-book-style 'waiting for the "
        "bus'-type probability questions, and also a simple Markov dice problem."
    ),
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/thread-1157580-1-1.html",
    source_quote=(
        "SIG 求Quant Research and Sys Trading的recruiter call经验！感恩|sig面经|一亩三分地海外面经版 ... "
        "2025(10-12月) 金工类 博士 全职@sig - 网上海投 - HR筛选 | 😐 Neutral 😐 Average | Other | 应届毕业生 ... "
        "| 个流程大致怎样，以及数学题问了什么呢？ 感恩 | ... "
        "| 会问你喜欢research还是trading, why sig, 绿皮书等公交车类型的probablity问题，还有简单的markov骰子问题 |"
    ),
    source_language="zh",
    post_date="2025-10",
    poster_context=(
        "Thread 'SIG 求Quant Research and Sys Trading的recruiter call经验！感恩' on 海外面经, tagged sig. "
        "Forum header: 2025(10-12月) 金工类 博士 全职@sig - 网上海投 - HR筛选, 应届毕业生. The thread is someone "
        "asking what the recruiter call is like; the quoted line is a reply from a candidate who had "
        "already done it."
    ),
    doubt=(
        "This names question *types*, not questions — '绿皮书等公交车类型的probablity问题' means green-book "
        "bus-waiting-style probability problems, and 'markov骰子问题' means a simple Markov dice problem. "
        "Neither is a recoverable item. It is recorded because it is direct first-hand evidence about "
        "which round the maths appears in for the QR / Systematic Trading track (the recruiter call "
        "itself, not just the later technical rounds), and because '绿皮书' is the candidate explicitly "
        "sourcing SIG's questions to the Green Book — which is exactly the textbook-laundering risk the "
        "shard warns about, here admitted by a candidate rather than by a vendor."
    ),
))

with open(OUT, "a", encoding="utf-8") as fh:
    for rec in records:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"appended {len(records)} records to {OUT}")
