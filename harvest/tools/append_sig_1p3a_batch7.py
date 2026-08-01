#!/usr/bin/env python3
"""Pass seven (final) of the SIG x 1point3acres harvest.

Three round-level attestations that fill the shard's two thinnest cells: the
internship level and the final/onsite round. Same sourcing rule as every earlier
pass — WebSearch "Highlights" blocks quoting www.1point3acres.com, retrieved in this
pass.
"""

import json

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
# thread-1089922 : "求海纳国际 SIG qr intern final 面经" — QR INTERN.
# 海纳国际 is one of SIG's Chinese names.
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="internship",
    cycle="2025",
    round="phone_technical",
    round_name="第一轮技术电面 (first-round technical phone screen)",
    section_context=(
        "The pipeline the thread establishes: OA → 第一轮技术电面 → a recruiting-team call about background "
        "and career interest → further rounds → team match. This record is the technical phone screen."
    ),
    question_type="probability",
    question_text="奥奥是BQ之后纯概率",
    question_text_en=(
        "'Oh I see — so after the behavioural questions it's pure probability.' (Answering another reader who "
        "asked 请问技术电面会问什么啊 — 'what does the technical phone screen ask?')"
    ),
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/thread-1089922-1-1.html",
    source_quote=(
        "求海纳国际 SIG qr intern final 面经|sig面经|一亩三分地海外面经版 ... "
        "一亩三分地»论坛›海外求职›海外面经›求海纳国际 SIG qr intern final 面经 ... "
        "| 回复: 11 | 直达 求海纳国际 SIG qr intern final 面经 海外面经 sig | ... "
        "| 我SIG过了OA，过了第一轮技术电面，现在这一轮是说是和recruiting team里一个人聊background, career interest。"
        "我也想了解下这轮会问什么问题，后边还有几轮面试？ | ... "
        "| wth961209 发表于 2024-10-4 22:53我SIG过了OA，过了第一轮技术电面，现在这一轮是说是和recruiting team里"
        "一个人聊background, career inter ... 主要是recruiter和你聊过去项目和经历，根据这个给你介绍几个组，"
        "然后让你给一两个preference，但不用选定。再给你介绍一下后面的流程。全面完之后才到team match环节。 | ... "
        "| wth961209 发表于 2024-10-5 01:53我SIG过了OA，过了第一轮技术电面，现在这一轮是说是和recruiting team里"
        "一个人聊background, career inter ... 奥奥是BQ之后纯概率 | ... "
        "| wth961209 发表于 2024-10-4 22:53 ... 请问技术电面会问什么啊 | ... "
        "| kk_zard 发表于 2024-12-05 01:01:45我想请问一下大概有哪些类别的组啊？… recruiter是根据你的过去经历会给你"
        "推荐几个组，具体怎么选我也不知道，我第一轮面完就挂了。 |"
    ),
    source_language="zh",
    post_date="2024-10",
    poster_context=(
        "Thread '求海纳国际 SIG qr intern final 面经' on 海外面经, tagged sig, 11 replies; the exchange quoted "
        "runs 2024-10-04 to 2024-12-05. 海纳国际 is one of SIG's Chinese names, alongside 萨斯奎哈纳 and "
        "萨斯奎汗 — all three turned up as distinct search handles. The title says qr intern, which fixes both "
        "role_track and level. The thread is someone asking what the rounds contain; the quoted line is the "
        "answer they arrive at after being told."
    ),
    doubt=(
        "This names a round's content in five characters, not a question — 'after BQ it's pure probability'. "
        "Nothing is recoverable as an item. It is here because the internship level is the emptiest cell in "
        "this shard and this is one of very few 1point3acres sources that states a track (QR), a level "
        "(intern), a round (first technical phone screen) and its content together. Note also that it is a "
        "reader paraphrasing what they were told, not the interviewee's own write-up, which is one remove "
        "further from first-hand than most records here."
    ),
))

# ---------------------------------------------------------------------------
# thread-1091467 : "SIG：HR面->终面所有面经+总结的历年面经" — full loop, PhD, FAIL.
# Final round had at least 3 questions; readers found Q1 and Q3 impenetrable.
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="2024",
    round="superday",
    round_name="final round / 终面",
    section_context=(
        "Full loop reported: HR筛选 → 技术电面 → Onsite → 视频面试, ending in a rejection. The poster notes "
        "似乎地里没有太多终面的面经 — there is not much final-round recall on the forum — which is why they "
        "wrote it up."
    ),
    question_type="other",
    question_text=(
        "[终面题目本身在积分墙后。可确认的是终面至少有三题，且第 1、3 题连读者读完题解都无从下手：] "
        "请问lz final round 第1，3题有什么可以参考的思路吗？ 看了之后没什么头绪。。。然后lz是有finance背景吗？"
    ),
    question_text_en=(
        "[The final-round questions themselves are behind the paywall. What is established: the final round "
        "had at least three questions, and questions 1 and 3 left even a reader who had read the write-up with "
        "no idea how to start.] Reader: 'Could I ask whether there's any line of approach for final-round "
        "questions 1 and 3? After reading them I have no clue… also, does OP have a finance background?'"
    ),
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/thread-1091467-1-1.html",
    source_quote=(
        "SIG：HR面->终面所有面经+总结的历年面经|sig面经|一亩三分地海外面经版 ... "
        "# SIG：HR面->终面所有面经+总结的历年面经 ... "
        "2024(7-9月) 金工类 博士 全职@sig - 网上海投 - HR筛选 技术电面 Onsite 视频面试 | 😐 Neutral 😐 Average | "
        "Fail | 在职跳槽 ... "
        "本帖最后由 论坛匿名用户 于 2024-10-13 10:22 编辑 7月初在Linkedin上看到SIG的job post，q ... "
        "| 难受。 但希望这些面经对后来人有帮助吧。尤其是似乎地里没有太多终面的面经。 祝大家找工好运。求加米！ | ... "
        "| 非常感谢lz分享！ 请问lz final round 第1，3题有什么可以参考的思路吗？ 看了之后没什么头绪。。。"
        "然后lz是有finance背景吗？ | ... "
        "| 请问final round就是virtual的吗？没有onsite的部分还是virtual过了之后还会有onsite？ |"
    ),
    source_language="zh",
    post_date="2024-10-13",
    poster_context=(
        "Thread 'SIG：HR面->终面所有面经+总结的历年面经' on 海外面经, tagged sig. The forum's structured header "
        "reads 2024(7-9月) 金工类 博士 全职@sig - 网上海投 - HR筛选 技术电面 Onsite 视频面试 | Fail | 在职跳槽 — "
        "a PhD-level experienced hire in the quantitative-finance category who went through the whole loop and "
        "was rejected. They applied off a LinkedIn job post in early July."
    ),
    doubt=(
        "No question text at all — this is a reader's request for hints, quoted because it is the only "
        "evidence in the shard about SIG's FINAL round structure, and because the poster themselves says "
        "final-round recall is scarce on the forum. It establishes only: the final round has at least three "
        "questions, and at least two of them are hard enough that a reader with the write-up in front of them "
        "could not find an approach. The role track is never stated beyond 金工类 (quantitative finance "
        "category), which spans QR, QT and QST at SIG, so role_track stays unknown. I considered dropping this "
        "for having zero question content and kept it only as a round-structure attestation."
    ),
))

# ---------------------------------------------------------------------------
# tag page /bbs/tag/sig-905-8.html : "萨斯奎汗 25intern oa" preview — a third
# Chinese transliteration of Susquehanna, and a 2025 INTERN OA.
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="unknown",
    level="internship",
    cycle="2025",
    round="online_assessment",
    round_name="萨斯奎汗 25intern oa",
    section_context="17个选择题 (17 multiple-choice questions); poster could only upload 9 images, rest in replies",
    question_type="probability",
    question_text=(
        "17个选择题我只能说大概我不是目标员工（。一半脑筋急转弯 一半概率论 "
        "要做的话建议概率和期望和积分那些公式复习复习再做只能发9张图，剩下见评"
    ),
    question_text_en=(
        "17 multiple-choice questions. All I can say is I'm probably not their target hire. Half brainteasers, "
        "half probability theory. If you're going to sit it, I'd suggest revising probability, expectation and "
        "those integral formulas first. I can only upload 9 images — the rest are in the replies."
    ),
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/tag/sig-905-8.html",
    source_quote=(
        "| | 萨斯奎汗 25intern oa 悲痛求米 17个选择题我只能说大概我不是目标员工（。一半脑筋急转弯 一半概率论 "
        "要做的话建议概率和期望和积分那些公式复习复习再做只能发9张图，剩下见评 | 海外面经 | 匿名 2024-8-27 | "
        "1 371 | 地里匿名用户 2024-8-27 12:52 | ... "
        "| | SIG OA题目 一共有四题，70min。第一题10行搞定就不放了。 | 海外面经 | 匿名 2024-9-7 | 5 2499 | "
        "Gatslby 2025-8-17 15:41 |"
    ),
    source_language="zh",
    post_date="2024-08-27",
    poster_context=(
        "Recovered from the ungated ~200-character thread preview on the SIG company tag-listing page "
        "https://www.1point3acres.com/bbs/tag/sig-905-8.html. Anonymous poster, 海外面经 board, 2024-08-27, "
        "1 reply, 371 views — a low-traffic thread that would be easy to miss. Note the thread title uses "
        "萨斯奎汗, a third Chinese transliteration of Susquehanna distinct from 萨斯奎哈纳 and 海纳国际; "
        "searching only for 'SIG' misses posts titled this way. 悲痛求米 ('grief-stricken, please give me "
        "rice') marks it as a post-rejection recall post."
    ),
    doubt=(
        "Characterises the paper rather than quoting any item: 17 multiple-choice, half brainteaser and half "
        "probability, with a revision recommendation that includes integrals. No question is recoverable, and "
        "the actual questions were posted as photographs (只能发9张图), which the search index cannot read. "
        "Recorded for three reasons: it is dated internship-level content (25intern, posted August 2024); the "
        "explicit mention of 积分 (integrals) corroborates the separate calculus attestation in thread-719224 "
        "about a fifth-derivative question, which no other source in the shard mentions; and it establishes "
        "萨斯奎汗 as a search handle. The role track is nowhere stated — 'intern' alone does not distinguish QT "
        "from QR — so role_track is unknown."
    ),
))

with open(OUT, "a", encoding="utf-8") as fh:
    for rec in records:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"appended {len(records)} records to {OUT}")
