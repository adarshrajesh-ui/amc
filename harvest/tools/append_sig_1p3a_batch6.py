#!/usr/bin/env python3
"""Pass six of the SIG x 1point3acres harvest: new threads found by sweeping the
company tag-listing pages (/bbs/tag/sig-905-N.html), which carry ungated ~200-char
thread previews, plus three in-place enrichments of records whose answer text a wider
snippet window later exposed.

Sourcing rule unchanged: every quote was copied out of a WebSearch "Highlights" block
quoting a www.1point3acres.com URL, retrieved in THIS pass.
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

new_records = []

# ---------------------------------------------------------------------------
# thread-1183374 : "SIG 2027 OA" — the 2027 cycle. Poster says the paper is
# almost identical to 2026 but with TWO NEW questions, and names both.
# ---------------------------------------------------------------------------
T1183374 = "https://www.1point3acres.com/bbs/thread-1183374-1-1.html"
T1183374_QUOTE = (
    "SIG 2027 OA|sig面经|一亩三分地海外面经版 ... 一亩三分地»论坛›海外求职›海外面经› SIG 2027 OA ... "
    "| 回复: 0 | 直达 SIG 2027 OA 数科面经 sig | ... "
    "| 注册一亩三分地论坛，查看更多干货！ 您需要登录才可以下载或查看附件。没有帐号？注册账号 x "
    "和26年几乎一样加了两道新题 1）a farmer is waiting for two flowers to blossom in the next 60 d "
    "您好！本帖隐藏的内容需要积分高于 188 才可浏览您当前积分为 0。使用VIP即刻解锁阅读权限或查看其他获取积分的方式 "
    "游客，您好！本帖隐藏的内容需要积分高于 188 才可浏览您当前积分为 0。 VIP即刻解锁阅读权限或查看其他获取积分的方式 "
    "Unlock interview details and practice with AI Curated Interview Questions from Top Companies "
    "umbers. Expected number of consecutive pairs. |"
)
T1183374_COMMON = dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="2027",
    round="online_assessment",
    round_name="SIG 2027 OA",
    section_context=(
        "poster's framing: 和26年几乎一样加了两道新题 — 'almost identical to the 2026 paper, with two new "
        "questions added'. These are those two."
    ),
    source_url=T1183374,
    source_language="mixed",
    post_date="2026",
    poster_context=(
        "Thread 'SIG 2027 OA' on the 数科面经 board, tagged sig, zero replies at time of retrieval — i.e. a "
        "brand-new posting for the 2027 recruiting cycle. The value of this thread is that the poster has "
        "already sat both the 2026 and 2027 papers and explicitly isolates the delta between them, which no "
        "other thread in the shard does."
    ),
)

new_records.append(dict(
    T1183374_COMMON,
    question_type="probability",
    question_text="1）a farmer is waiting for two flowers to blossom in the next 60 d[ays] …",
    question_text_en=(
        "1) A farmer is waiting for two flowers to blossom in the next 60 d[ays] … [statement truncated by the "
        "188-point paywall at exactly this point]"
    ),
    reported_answer=None,
    source_quote=T1183374_QUOTE,
    doubt=(
        "Cut off after fourteen words, right where the blooming durations would be given, so it is not solvable "
        "as recorded. I am keeping it for two reasons. First, it is dated evidence of what changed for the 2027 "
        "cycle. Second, and more usefully, it corroborates the 'A gradener is eagerly waiti…' fragment recovered "
        "independently from the sig-905-8 tag page (K小姐, 2024-09-04) — two posters two years apart, in "
        "different threads, both truncated, both describing someone waiting for flowers to bloom in a fixed "
        "window. That cross-attestation is why I believe the item is real even though neither source states it "
        "fully. I have deliberately NOT completed the sentence, even though prep-vendor pages hosting "
        "screenshots of the live Mettl screen do give a full version, because those are excluded sources."
    ),
))

new_records.append(dict(
    T1183374_COMMON,
    question_type="expected_value",
    question_text="…umbers. Expected number of consecutive pairs.",
    question_text_en=(
        "[Second new question. The paywall swallows the front of the statement; the visible tail is:] "
        "'…[n]umbers. Expected number of consecutive pairs.'"
    ),
    reported_answer=None,
    source_quote=T1183374_QUOTE,
    doubt=(
        "Five words, and the first is itself truncated (…umbers, almost certainly 'numbers'). What is "
        "establishable: the 2027 paper added an expectation question about the number of consecutive pairs in "
        "some arrangement of numbers. The setup — how many numbers, whether they are a random permutation, a "
        "random subset, or a shuffled deck — is entirely absent, and I have not guessed at it. Recorded because "
        "'expected number of consecutive pairs' is a specific enough phrase to be recognisable to someone who "
        "sits the test, and because it is the only 2027-cycle content in the shard beyond its sibling record."
    ),
))

# ---------------------------------------------------------------------------
# tag page /bbs/tag/sig-905-8.html : the K小姐 thread preview.
# "SIG QR Fulltime Entry Level 一共17道题"
# ---------------------------------------------------------------------------
new_records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="unknown",
    round="online_assessment",
    round_name="SIG QR Fulltime Entry Level OA",
    section_context=(
        "一共17道题 一个小时 (17 questions, one hour). Poster's characterisation: 非常简单的概率/逻辑 "
        "逻辑完全不需要准备类似于简单的智力题 概率也比较基础 — very easy probability/logic; the logic needs no "
        "preparation at all and is like simple IQ-test puzzles; the probability is fairly basic."
    ),
    question_type="probability",
    question_text="1. A gradener is eagerly waiti … [preview truncated by the tag page]",
    question_text_en="1. A gardener is eagerly waiti[ng] … [preview truncated]",
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/tag/sig-905-8.html",
    source_quote=(
        "| | SIG QR Fulltime Entry Level 一共17道题 一个小时非常简单的概率/逻辑 逻辑完全不需要准备类似于简单的智力题 "
        "概率也比较基础，我先分享两个我卡壳了的，加米继续发1. A gradener is eagerly waiti ... | 海外面经 | "
        "K小姐 2024-9-4 | 4 2215 | wayneguan3 2024-9-19 04:53 | ... "
        "| | SIG Full Time Entry Level 诚信分享 求大米 求大米 谢谢 | 海外面经 | K小姐 2024-9-4 | 0 1197 | "
        "K小姐 2024-9-4 20:42 |"
    ),
    source_language="mixed",
    post_date="2024-09-04",
    poster_context=(
        "Recovered from the ungated ~200-character thread preview on the SIG company tag-listing page "
        "https://www.1point3acres.com/bbs/tag/sig-905-8.html. Thread by 一亩三分地 user K小姐, posted "
        "2024-09-04 on 海外面经 (4 replies, 2215 views, last reply by wayneguan3 on 2024-09-19). The poster "
        "says they are sharing the two questions they got stuck on and will post more if given rice points "
        "(我先分享两个我卡壳了的，加米继续发). The same user posted a second SIG thread the same day. The thread "
        "body itself is point-gated."
    ),
    doubt=(
        "Truncated after six words, so this is not usable as a question — only the opening clause and the "
        "poster's own typo ('gradener') are established. Two things make it worth keeping. The role track is "
        "unusually well specified for this shard: the poster labels it 'SIG QR Fulltime Entry Level', which is "
        "why role_track is quant_researcher. And it is independently corroborated by the 2027 thread "
        "(thread-1183374), whose first new question begins 'a farmer is waiting for two flowers to blossom in "
        "the next 60 d…' — same scenario, different poster, two years apart. The full statement is available on "
        "homework-farm pages that host photographs of the live Mettl screen, but those are excluded sources so "
        "I have NOT completed the sentence from them. Note the poster promised a second stuck-on question that "
        "I never recovered."
    ),
))

# ---------------------------------------------------------------------------
# thread-1165150 : "SIG Quant Research & Systematic Trading挂经" — ECON PhD.
# Recruiter round names a 9-sided-dice question.
# ---------------------------------------------------------------------------
new_records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="2026",
    round="phone_technical",
    round_name="recruiter 第一轮 (recruiter first round)",
    section_context=(
        "Full pipeline the poster reports: 11月OA → 12月底 recruiter 第一轮 → 1月初 Quant 电面 → 月底 Data Task "
        "→ Data Task Virtual Review. They were cut at the data-task round. The recruiter round is described as "
        "green-book probability questions plus this dice item."
    ),
    question_type="probability",
    question_text=(
        "[原帖在检索结果中以 GBK/UTF-8 乱码返回，以下为解码后的文本：] "
        "recruiter第一轮基本上就是绿皮书 概率题 还有 9面筛子出顺子"
    ),
    question_text_en=(
        "[The thread came back through the search index as GBK/UTF-8 mojibake; this is the decoded text.] "
        "'The recruiter's first round was basically the Green Book — probability questions — plus: a 9-sided "
        "die, rolling a straight (i.e. a run of consecutive values).'"
    ),
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/thread-1165150-1-1.html",
    source_quote=(
        "SIG Quant Research & Systematic Trading鎸傜粡|sig闈㈢粡|涓€浜╀笁鍒嗗湴娴峰闈㈢粡鐗� ... "
        "# SIG Quant Research & Systematic Trading鎸傜粡 ... "
        "鏂伴矞鐨凟CON PhD鎶藉鎸傜粡 Timeline澶ф鏄�11鏈圤A锛�12鏈堝簳recruiter绗竴杞紝1鏈堝垵Quant鐢甸潰锛�"
        "鏈堝簳Data Task锛屽墠澶〥ata Task Virtual Review. 鎸傚湪data task杩欎竴杞€俁ecruiter涔嬪墠璇磋繖涓€杞�"
        "濡傛灉杩囦簡涓嬩竴杞槸onsite銆� OA鎴戜箣鍓嶅彂浜�17閬撻 recruiter绗竴杞熀鏈笂灏辨槸缁跨毊涔� 姒傜巼棰� "
        "杩樻湁 9闈㈢瓫瀛愬嚭椤哄瓙 ... "
        "| 鍙互闂笅quant 鐢甸潰鍚庡涔呴€氱煡涓嬩竴杞殑鍛€锛屾垜鍛ㄤ竴鐢甸潰鐨勶紝鐜板湪娌℃敹鍒版秷鎭笉鐭ラ亾姒傜巼澶т笉澶с€� | ... "
        "> qhy0903 鍙戣〃浜� 2026-03-25 12:40:13 ... 绗竴杞甴r搴楅潰鍗婂皬鏃� 绗簩杞拰quant鑱婂畬澶ф"
    ),
    source_language="zh",
    post_date="2026-03",
    poster_context=(
        "Thread 'SIG Quant Research & Systematic Trading挂经' on 海外面经, tagged sig; replies dated "
        "2026-03-25. The poster self-identifies as an ECON PhD applying to Quant Research and Systematic "
        "Trading, and says the OA they had already posted elsewhere was the 17-question paper "
        "(OA我之前发了17道题). Decoded timeline: OA in November, recruiter round late December, quant phone "
        "interview early January, Data Task at the end of that month, Data Task Virtual Review just before "
        "posting; they were rejected at the data task."
    ),
    doubt=(
        "Two problems. First, the encoding: the search index returned this thread as mojibake (UTF-8 bytes "
        "rendered through GBK), so I reconstructed the Chinese by re-encoding to gb18030 and decoding as UTF-8. "
        "The reconstruction is legible and internally consistent, but a handful of characters were already lost "
        "to replacement bytes before I saw it, so I have put the raw mojibake in source_quote rather than a "
        "cleaned-up version I would be inventing. Second, even decoded, '9面筛子出顺子' names a question in six "
        "characters — a 9-sided die and a 'straight' — without saying how many rolls, whether the straight must "
        "be in order, or what is being computed. 筛子 is also the common misspelling of 骰子 (dice). It is "
        "recorded because it is the only attestation anywhere in the shard of a 9-sided die, and because it "
        "pins the item to a specific round (recruiter first round) on a specific track."
    ),
))

# ---------------------------------------------------------------------------
# thread-1090023 : "[实习] SIG qr oa（1）" — INTERNSHIP-tagged QR OA.
# ---------------------------------------------------------------------------
new_records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="internship",
    cycle="unknown",
    round="online_assessment",
    round_name="SIG Problem Solving Assessment",
    section_context="一共17道题，概率题居多 (17 questions in total, mostly probability); 一个小时十七题",
    question_type="probability",
    question_text="一共17道题，概率题居多。",
    question_text_en="17 questions in total, the majority of them probability.",
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/thread-1090023-1-1.html",
    source_quote=(
        "SIG qr oa（1）|sig求职讨论|一亩三分地求职（非面经）版 ... "
        "一亩三分地»论坛›海外求职›求职（非面经）› SIG qr oa（1） ... # [实习] SIG qr oa（1） ... "
        "| 一共17道题，概率题居多。 | ... 上一篇：请教mock interview的网站和效果下一篇： SIG qr oa（2） | ... "
        "> 清爽的绿茶 发表于 2024-10-09 08:32:10.1point3acres 感谢楼主，请问楼主收到的OA是一个小时的"
        "Problem Solving Assessment吗 ... | 是的，一个小时十七题 | ... | 第二部分呢 |"
    ),
    source_language="zh",
    post_date="2024-10",
    poster_context=(
        "Thread 'SIG qr oa（1）' on the 求职（非面经） board, tagged sig, and — importantly — carrying the "
        "forum's own [实习] (internship) prefix, which is why level is 'internship' here. It is the first of a "
        "pair; the next thread by the same poster is 'SIG qr oa（2）'. The post itself is an image dump (the "
        "sibling tag-page preview for part 2 reads 'SIG qr oa第二部分。题型都是一样的，但是数字会改，"
        "建议自己做一遍然后开始做oa'), which is why only the one-line caption is indexable."
    ),
    doubt=(
        "This is a section descriptor, not a question — the actual questions were posted as photographs, and "
        "images are invisible to the search index, so nothing of the 17 items themselves is recoverable from "
        "this thread. I am recording it because it is the ONLY 1point3acres source in this shard that pins the "
        "17-question / 60-minute Problem Solving Assessment to the *internship* level on the *QR* track — every "
        "other 17-question thread is full-time or unlabelled — and because the reply exchange confirms the "
        "format explicitly ('is the OA you got the one-hour Problem Solving Assessment?' / 'Yes, seventeen "
        "questions in an hour'). Treat it as a format attestation, not a question."
    ),
))

# ---------------------------------------------------------------------------
# Write new records, then apply in-place enrichments.
# ---------------------------------------------------------------------------
with open(OUT, "a", encoding="utf-8") as fh:
    for rec in new_records:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
print(f"appended {len(new_records)} records")

rows = []
with open(OUT, encoding="utf-8") as fh:
    for line in fh:
        line = line.strip()
        if line:
            rows.append(json.loads(line))

patched = 0

for r in rows:
    # -- thread-686183 round-1 Q1: a reader posted a full worked solution.
    if (r["source_url"].endswith("thread-686183-1-1.html")
            and r["question_text"].startswith("1. 圆里随机画n条线")):
        r["reported_answer"] = (
            "Expectation = n + 1 + n(n−1)/6. Worked out in full by a reader: 「第一轮第一题是认真的吗？ "
            "刚用了很长时间算了一下，感觉有几个点需要注意： 首先，任意两条线相交的概率是1/3; 其次，需要考虑所有线两两组合的"
            "情况，即有choose 2 from n 种情况，以下表示为C； 然后，n条线m个交点可以把平面分成 n+m+1块； 为了方便，"
            "可以用C 表示 然后可以列出式子 \\sum_{k=0}^{C} (n+k+1)* (choose k from C) (1/3)^k*(2/3)^(C-k), "
            "然后还要用组合恒等式k*(choose k from n) = n*(choose k-1 from n-1) 最后得出期望是 n + 1 + n*(n-1)/6; "
            "如果面到这个题绝壁完蛋」. Two supporting facts are stated separately in the thread: 「n 条线 m 个交点是 "
            "n+m+1 块」 and 「相交的概率是1/3 （只用考虑4个点的顺序）」 — the 1/3 comes from considering only the "
            "cyclic order of the 4 endpoints. A third reader confirms the shape of the result: "
            "「那么也就是相当于n+n*(n-1)/6+1？ 题目很精彩」."
        )
        r["source_quote"] = (
            "# SIG 1轮+2轮面经 ... SIG 面经 第一轮： 1. 圆里随机画n条线，问能把圆分成几分 （期望）？ "
            "把分成的份数和交点个数对应起来，然后算交点个数的期望。 2. 扔硬币 进入 HTH HHT 之一就结束，"
            "问进入每一个的概率是多大？（不太记得具体ending state是啥了） 3. 三 ... "
            "| 第一轮第一题是认真的吗？ 刚用了很长时间算了一下，感觉有几个点需要注意： 首先，任意两条线相交的概率是1/3; "
            "其次，需要考虑所有线两两组合的情况，即有choose 2 from n 种情况，以下表示为C； 然后，n条线m个交点可以把平面"
            "分成 n+m+1块； 为了方便，可以用C 表示 然后可以列出式子 \\sum_{k=0}^{C} (n+k+1)* (choose k from C) "
            "(1/3)^k*(2/3)^(C-k), 然后还要用组合恒等式k*(choose k from n) = n*(choose k-1 from n-1) "
            "最后得出期望是 n + 1 + n*(n-1)/6; 如果面到这个题绝壁完蛋 | ... "
            "| 感谢！ … 1. n条线m个交点，分成的块数是n+m+1，为啥啊？画了几个例子，确实如此，但没想到如何证明 "
            "2. 1/3那个有点印象，类似的题看到过，两个结合在一起让人眼前一亮，那么也就是相当于n+n*(n-1)/6+1？ 题目很精彩 | ... "
            "| 有几个交点，就能推算出分成了几块 n 条线 m 个交点是 n+m+1 块 ... 相交的概率是1/3 （只用考虑4个点的顺序）|"
        )
        r["doubt"] = (
            r["doubt"].rstrip()
            + " [Updated in a later pass: a wider snippet window exposed a reader's complete worked solution "
              "and the closed form n + 1 + n(n−1)/6, which I have added to reported_answer. Caveat on that "
              "answer: it is a forum reader's derivation, not SIG's answer key, and the same reader opens with "
              "'第一轮第一题是认真的吗？' ('is round 1 question 1 serious?') and closes with '如果面到这个题绝壁完蛋' "
              "('if you get this in an interview you're absolutely dead'), so even they treat it as unreasonably "
              "hard for a phone screen. The 1/3 pairwise-intersection probability is asserted, not proved, in "
              "the thread.]"
        )
        patched += 1

    # -- thread-719224 Q2: the poster's own corrected Markov write-up surfaced.
    if (r["source_url"].endswith("thread-719224-1-1.html")
            and r["question_type"] == "probability"):
        r["question_text"] = (
            "[题面被积分墙挡住。以下为楼主自己更正后的解法，题目结构由此可还原：掷某种随机装置，"
            "每次出现 8 的概率 0.07、出现 9 的概率 0.08、出现 10 的概率 0.09（其余 0.76 为无事发生），"
            "问「8 和 10 都出现」的概率。] "
            "我刚刚发现我第二题理解错了，我之前理解的是只要出现8或者10就算赢，所以之前那个帖子里算的概率都将近1了。"
            "现在我理解就是要8和10都出现才可以。我重新算了一下，还是markov方法： "
            "假设从初始状态到最终状态(8和10出现)的概率是p(s), 从出现一次8的状态到最终状态的概率是p(8)，"
            "相应的p(9)和p(10)是同样的意思，然后p(8,9)是从出现了一次8和9的状态到最终状态，同理p(9, 10)。"
            "然后就可以列方程： p(s) = 0.76p(s) + 0.07p(8) + 0.08p(9) + 0.09p(10) "
            "p(8) = 0.83p(8) + 0.09 + 0.08p(8,9). p(9) = 0.76p(9) + 0.07p(8,9) + 0.09p(9, 10). "
            "p(10) = 0.85p(10) + 0.07 + 0.08p(9,10). p(8,9) = 0.83p(8,9) + 0.09 p(9,10) = 0.85p(9,10) = 0.07"
        )
        r["question_text_en"] = (
            "[Statement behind the paywall. This is the poster's own corrected solution, from which the "
            "structure is recoverable: something is generated repeatedly, with per-trial probability 0.07 of "
            "an 8, 0.08 of a 9 and 0.09 of a 10 (the remaining 0.76 being nothing); asked for the probability "
            "that BOTH an 8 and a 10 appear.] 'I've just realised I misread question 2. I had read it as "
            "winning if either an 8 or a 10 shows up, which is why the probability I computed in that earlier "
            "post came out near 1. Now I read it as needing both the 8 and the 10. I've recomputed, still by "
            "the Markov method: let p(s) be the probability of getting from the initial state to the final "
            "state (8 and 10 have appeared), p(8) the probability from the state where an 8 has appeared once, "
            "similarly p(9) and p(10); p(8,9) is from the state where an 8 and a 9 have each appeared, likewise "
            "p(9,10). Then you can set up the equations: [system as quoted].'"
        )
        r["reported_answer"] = (
            "p(s) = 13118/21675, per the poster's corrected Markov solution. They immediately flag it as "
            "impractical under the time limit: 「但是可以看出来这个方法计算量很大，而且超级容易出错。我很担心就20分钟，"
            "这道题用这个方法得用去一大半时间，然后还有可以因为计算出错。我目前没有想到其他更简单的方法了」 — this "
            "method is very computation-heavy and extremely error-prone; with only 20 minutes it would eat more "
            "than half the time, and they could not find a simpler approach."
        )
        r["source_url"] = "https://www.1point3acres.com/bbs/thread-719224-2-1.html"
        r["source_quote"] = (
            "SIG Quantitative Evaluation 2021. OA 2021-02最新|sigPM面经|一亩三分地数科面经版 ... "
            "| 我刚刚发现我第二题理解错了，我之前理解的是只要出现8或者10就算赢，所以之前那个帖子里算的概率都将近1了。"
            "现在我理解就是要8和10都出现才可以。我重新算了一下，还是markov方法： 假设从初始状态到最终状态(8和10出现)"
            "的概率是p(s), 从出现一次8的状态到最终状态的概率是p(8)，相应的p(9)和p(10)是同样的意思，然后p(8,9)是从出现了"
            "一次8和9的状态到最终状态，同理p(9, 10)。然后就可以列方程： "
            "p(s) = 0.76p(s) + 0.07p(8) + 0.08p(9) + 0.09p(10) p(8) = 0.83p(8) + 0.09 + 0.08p(8,9). "
            "1point3acres.com p(9) = 0.76p(9) + 0.07p(8,9) + 0.09p(9, 10). p(10) = 0.85p(10) + 0.07 + "
            "0.08p(9,10). 1point3acres p(8,9) = 0.83p(8,9) + 0.09 p(9,10) = 0.85p(9,10) = 0.07 "
            "最后解出来p(s)=13118 / 21675,但是可以看出来这个方法计算量很大，而且超级容易出错。我很担心就20分钟，"
            "这道题用这个方法得用去一大半时间，然后还有可以因为计算出错。我目前没有想到其他更简单的方法了 | ... "
            "| 不是的，也是数学题，题型和你这个差不多。有四个section,第一个section里有4道题，要求全部做完，"
            "第二个里有5道题，希望做出尽量多的题，然后后面两个section都是附加题… |"
        )
        r["doubt"] = (
            "The statement itself never appeared; everything here is reverse-engineered from the poster's own "
            "corrected working, and I have marked that explicitly inside question_text rather than writing a "
            "clean problem. Specifically: the numbers 0.07 / 0.08 / 0.09 and the 'both 8 and 10' win condition "
            "are read off the transition equations, but WHAT is being rolled or drawn is nowhere stated — I "
            "assumed nothing about the mechanism. The poster is also on record having misread the question once "
            "already (their first attempt treated it as 8 OR 10), so even this second reading is their "
            "interpretation, not a quotation. The answer 13118/21675 is their arithmetic, unverified by anyone "
            "else in the thread. Recovered from page 2 of the thread (…/thread-719224-2-1.html); the earlier "
            "pass had only the page-1 fragment."
        )
        patched += 1

    # -- thread-1144112 Q17: the poster's commentary on the frog problem surfaced.
    if (r["source_url"].endswith("thread-1144112-1-1.html")
            and r["question_text"].startswith("Question 17")):
        r["reported_answer"] = (
            "No closed-form answer given. The poster's commentary: 「这个问题我每次都是手算出来的，没有找到什么对于"
            "B(m,n)的general solution … 数字都会是6以下，问题 … 或者建议提前跑 … 想到什么general solution，"
            "欢迎探讨」 — they hand-count it every time, have found no general solution for B(m,n), note the "
            "coordinates are always below 6, and suggest running code in advance; they invite discussion if "
            "anyone has a general solution."
        )
        r["doubt"] = (
            r["doubt"].rstrip()
            + " [Updated in a later pass: a wider snippet window exposed both the tail of the statement "
              "('Additionally, [the frog won't] move three steps in the same [direction]. Compute the number of "
              "ways [to reach] B') and the poster's commentary, now in reported_answer. Note that the poster "
              "explicitly says they have no general solution and hand-count each instance, which is consistent "
              "with the sibling records in this shard reporting the same problem with different endpoints — "
              "B(5,6), B(5,4) and (7,4) — i.e. SIG varies the coordinates between sittings.]"
        )
        patched += 1

with open(OUT, "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"patched {patched} existing records; file now has {len(rows)} records")
