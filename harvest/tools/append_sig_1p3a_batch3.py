#!/usr/bin/env python3
"""Third and final harvest pass for the SIG x 1point3acres shard.

A later, much wider snippet window on thread-1103279 exposed most of the
'SIG data exercise 面经' reply thread ungated. Same sourcing rule as passes one
and two: WebSearch "Highlights" blocks quoting www.1point3acres.com only.
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

T1103279 = "https://www.1point3acres.com/bbs/thread-1103279-1-1.html"
T1103279_QUOTE = (
    "SIG data exercise 面经|SIG求职讨论|一亩三分地求职（非面经）版 ... # [找工就业] SIG data exercise 面经 ... "
    "| 请问大家有人面过SIG 的data exercise吗？是需要用pandas处理股票数据吗？谢谢！ | ... "
    "| 上周面试的这周已经过了，这次不是预测股票价格了，这次是根据价格找策略了。不过估计每个人不一样。"
    "主要是你就当一个作业做一下就可以了。题目本身不难，但是可以做的比较复杂，面试本身基本上就是沟通你的思路，"
    "作业做的好就可以了，但是这个作业挺费时间的。 | ... "
    "| 你好！请问data exercise之前是phone tech面吗～麻烦问下phone tech面都是什么问题呀！非常非常感谢 | ... "
    "| 那个可以回家做一整个星期的？我好久以前面的不知道有没有变题。记得当时就是给你一堆股票的time series数据"
    "让你预测未来股票走向好像。我试了老半天也预测不了未来…但是还是过了。 | ... "
    "| 好像就是些很简单的iq题，还有点什么basic probability 啊之类的。我感觉iq有130就能随便过。 | ... "
    "| data exercise做完了之后最后final round有一道 winners curse theorem还挺神奇的 |"
)
T1103279_COMMON = dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    source_url=T1103279,
    source_language="zh",
    post_date="2025-09",
    poster_context=(
        "Thread 'SIG data exercise 面经' on the 求职（非面经） board, tagged sig. Opened as a question "
        "('has anyone interviewed for SIG's data exercise? do you need pandas to process stock data?') and "
        "answered by at least three different candidates who had each done the exercise in different "
        "years. Replies dated 2025-09-17 through 2025-09-25. Unusually, almost the whole reply thread "
        "came back ungated."
    ),
)

records = []

records.append(dict(
    T1103279_COMMON,
    round="take_home_assignment",
    round_name="SIG data exercise (take-home)",
    section_context="take-home you can work on for a whole week (可以回家做一整个星期)",
    question_type="statistics_regression",
    question_text=(
        "记得当时就是给你一堆股票的time series数据让你预测未来股票走向好像。"
    ),
    question_text_en=(
        "As I remember it, they give you a pile of stock time-series data and have you predict the "
        "future direction of the stocks, something like that."
    ),
    reported_answer=(
        "No solution given. The candidate adds: 我试了老半天也预测不了未来…但是还是过了。 "
        "('I tried for ages and couldn't predict the future… but I passed anyway.')"
    ),
    source_quote=T1103279_QUOTE,
    doubt=(
        "The commenter hedges twice in one sentence — '记得当时' (as I remember) and '好像' (something like "
        "that) — and explicitly flags that it was long ago and the task may have changed since "
        "('我好久以前面的不知道有没有变题'). So this is a recollection of a task, not a task specification. "
        "The role track is never stated anywhere in the thread. Its real value is the pairing with the "
        "record below: the two together show SIG rotates the data exercise between a forecasting brief "
        "and a strategy-design brief."
    ),
))

records.append(dict(
    T1103279_COMMON,
    round="take_home_assignment",
    round_name="SIG data exercise (take-home)",
    section_context=(
        "take-home; the interview afterwards is a discussion of your approach "
        "(面试本身基本上就是沟通你的思路)"
    ),
    question_type="statistics_regression",
    question_text=(
        "这次不是预测股票价格了，这次是根据价格找策略了。不过估计每个人不一样。"
        "题目本身不难，但是可以做的比较复杂"
    ),
    question_text_en=(
        "This time it wasn't predicting stock prices, this time it was finding a strategy from the "
        "prices. Though I'd guess it differs person to person. The problem itself isn't hard, but you "
        "can make it fairly elaborate."
    ),
    reported_answer=None,
    source_quote=T1103279_QUOTE,
    doubt=(
        "A description of the brief rather than the brief itself — no data, no instruments, no metric, "
        "no deliverable. The candidate also warns the assignment varies between candidates "
        "('估计每个人不一样'), so even the one-line characterisation may not generalise. Recorded because "
        "it is dated (they passed the week of 2025-09-17) and first-hand, and because it establishes "
        "that the SIG data exercise as of late 2025 is a strategy-design task, which contradicts the "
        "older forecasting version in the sibling record."
    ),
))

records.append(dict(
    T1103279_COMMON,
    round="phone_technical",
    round_name="phone tech 面 (before the data exercise)",
    section_context="the technical phone screen that precedes the data exercise",
    question_type="probability",
    question_text=(
        "好像就是些很简单的iq题，还有点什么basic probability 啊之类的。我感觉iq有130就能随便过。"
    ),
    question_text_en=(
        "It was just some very simple IQ questions, plus a bit of basic probability and that sort of "
        "thing. My feeling is that with an IQ of 130 you'd pass easily."
    ),
    reported_answer=None,
    source_quote=T1103279_QUOTE,
    doubt=(
        "Names question categories, not questions — this is a direct answer to another reader asking "
        "'what questions are in the phone tech round?', and the answer given is a shrug. No item is "
        "recoverable. It is recorded only because it pins the difficulty and content of the screen that "
        "gates the data exercise, and because it is one of the very few first-hand statements in the "
        "shard about a round other than the OA."
    ),
))

with open(OUT, "a", encoding="utf-8") as fh:
    for rec in records:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"appended {len(records)} records to {OUT}")
