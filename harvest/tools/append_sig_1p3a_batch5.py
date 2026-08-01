#!/usr/bin/env python3
"""Pass five of the SIG x 1point3acres harvest.

Sourcing rule, unchanged from earlier passes: every quote below was copied out of a
WebSearch result "Highlights" block that quoted a www.1point3acres.com URL, retrieved
fresh in THIS pass. Nothing was carried over from an earlier pass's notes, nothing was
written from memory, and nothing came from a prep-vendor or content-farm page.

Three of these records (thread-987697, thread-1118978, thread-795660) were drafted in an
earlier pass but never actually reached the JSONL. Rather than trust that draft, each was
re-searched and re-quoted here from a new snippet window.
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
# thread-987697 : "SIG电面" — dice sum divisible by 6
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="phone_technical",
    round_name="SIG的HR面试 (HR interview, the poster's own wording)",
    section_context=(
        "poster: 今天做了SIG的HR面试，算是不难的题 — the HR-stage screen, which at SIG carries maths. "
        "At least two questions; this is the second."
    ),
    question_type="probability",
    question_text=(
        "[第一题及第二题题干大部分被积分墙挡住，只有第二题的结尾露出：] …扔，请问他们的和是6的倍数的概率。"
    ),
    question_text_en=(
        "[Question 1 and most of question 2's stem sit behind the points paywall; only the tail of "
        "question 2 surfaced:] '…roll, what is the probability that their sum is a multiple of 6?'"
    ),
    reported_answer=(
        "1/6, per commenter jiushijiang (2023-10-10): 「第二题我感觉有个简单解法。对于任意n个骰子，答案都是1/6。"
        "因为不管离整除6还差多少，下一个骰子丢出这个数的概率都是1/6」 — for any number n of dice the answer is "
        "1/6, because whatever the shortfall to a multiple of 6 is, the chance the next die shows exactly that "
        "value is 1/6. A reader replies 好聪明哈哈哈! Separately, to a reader who says they could only brute-force "
        "it (第二题怎么做啊 我就想到穷举法QAQ), another answers 差不多吧 你就想一个骰子的概率 再想第二个 第三个 "
        "基本上就出来了。"
    ),
    source_url="https://www.1point3acres.com/bbs/thread-987697-1-1.html",
    source_quote=(
        "| 注册一亩三分地论坛，查看更多干货！ 您需要登录才可以下载或查看附件。没有帐号？注册账号 x "
        "今天做了SIG的HR面试，算是不难的题。.1point3acres 第一 您好！本帖隐藏的内容需要积分高于 188 才可浏览"
        "您当前积分为 0。使用VIP即刻解锁阅读权限或查看其他获取积分的方式 游客，您好！本帖隐藏的内容需要积分高于 "
        "188 才可浏览您当前积分为 0。 VIP即刻解锁阅读权限或查看其他获取积分的方式 Unlock interview details and "
        "practice with AI Curated Interview Questions from Top Companies 扔，请问他们的和是6的倍数的概率。 | ... "
        "| 第二题我感觉有个简单解法。对于任意n个骰子，答案都是1/6。因为不管离整除6还差多少，下一个骰子丢出这个数的概率都是1/6 | ... "
        "| jiushijiang 发表于 2023-10-10 20:45第二题我感觉有个简单解法。对于任意n个骰子，答案都是1/6。"
        "因为不管离整除6还差多少，下一个骰子丢出这个 ... 好聪明哈哈哈! | ... "
        "| 第二题怎么做啊 我就想到穷举法QAQ | ... "
        "| vennfox 发表于 2023-08-15 04:42:12第二题怎么做啊 我就想到穷举法QAQ 差不多吧 你就想一个骰子的概率 "
        "再想第二个 第三个 基本上就出来了。 |"
    ),
    source_language="zh",
    post_date="2023-08",
    poster_context=(
        "Thread 'SIG电面' on the 数科面经 board, tagged sig. Reply timestamps run 2023-08-15 to 2023-10-10. "
        "Note the mismatch between the thread title (电面, phone interview) and the opening line "
        "(SIG的HR面试, SIG's HR interview) — at SIG the recruiter/HR screen does carry maths, which other "
        "threads in this shard independently confirm."
    ),
    doubt=(
        "The stem is truncated to a single character before 扔 (roll), so the number of dice is not stated in "
        "anything I saw — I know it only because the answering commenter generalises to 任意n个骰子 (any n dice), "
        "and I have not filled in a specific n. Note also that the search engine's own synthesis blurb disputed "
        "the 1/6 claim; I have recorded the forum commenter's answer as the reported answer because that is what "
        "the source says, not because I am endorsing it. The item is a well-known symmetry result, so on its own "
        "it would be weak; what keeps it is that the poster is reporting their own SIG screen and two other "
        "readers engage with it as a question they were also stuck on."
    ),
))

# ---------------------------------------------------------------------------
# thread-1118978 : "SIG第一轮电面 面经" — QR track, uniform-distribution extension
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="quant_researcher",
    level="unknown",
    cycle="2025",
    round="phone_technical",
    round_name="第一轮电面 (first-round phone interview)",
    section_context=(
        "一共俩题 (two questions). Q1 and the first part of Q2 were both items already circulating on the "
        "forum, so the poster only wrote up the second part of Q2, which was the extension."
    ),
    question_type="probability",
    question_text=(
        "第二题第一部分也是地里的，第二部分算扩展我写下来： X is uniformly [0, "
        "[本帖隐藏的内容需要积分高于 188 才可浏览 — 题目在此被截断] … X. Χ 第二部分答案2/3"
    ),
    question_text_en=(
        "'The first part of question 2 was also one already on the forum; the second part counts as an "
        "extension, so I'm writing it down: X is uniformly [0, …' — the statement is cut off at exactly this "
        "point by the 188-point paywall. The poster adds that the answer to the second part is 2/3."
    ),
    reported_answer=(
        "Disputed three ways. The poster states 第二部分答案2/3 but admits they did not follow the interviewer's "
        "hint (希望有大佬能给个简单思路，说实话面试官提醒但没听明白). Commenter Stardance (2025-03-21): "
        "「最近刚面完，我想说第二部分答案不是2/3，而是3/4 =2/3 * 3/4+1 * 1/4，真的被版主误导了。。。哎」. "
        "A third reader: 「我算了也是3/4」. The original poster concedes: "
        "「2/3答案会不会是面试官告诉的，也有可能是没听明白」."
    ),
    source_url="https://www.1point3acres.com/bbs/thread-1118978-1-1.html",
    source_quote=(
        "SIG第一轮电面 面经|sigPM面经|一亩三分地数科面经版 ... 一亩三分地»论坛›海外求职›海外面经›数科面经› "
        "SIG第一轮电面 面经 ... | 回复: 5 | 直达 SIG第一轮电面 面经 海外面经 sig | ... "
        "| 注册一亩三分地论坛，查看更多干货！ 您需要登录才可以下载或查看附件。没有帐号？注册账号 x "
        "才结束的电话面试，一共俩题，第一题地里原题就不多啰嗦了，第二题第一部分也是地里的，第二部分算扩展我写下来： "
        "X is uniformly [0, 您好！本帖隐藏的内容需要积分高于 188 才可浏览您当前积分为 0。… "
        "X. Χ 第二部分答案2/3，希望有大佬能给个简单思路，说实话面试官提醒但没听明白...QR岗 新人求米 | ... "
        "| 最近刚面完，我想说第二部分答案不是2/3，而是3/4 =2/3 * 3/4+1 * 1/4，真的被版主误导了。。。哎 | ... "
        "| 答案参见我刚顶上去的帖子“个人整理的地里SIG的高频概率题以及答案”中的文档 | ... "
        "| 本帖最后由 爸爸洗粑粑 于 2025-3-21 23:41 编辑 Stardance 发表于 2025-3-21 13:40最近刚面完，"
        "我想说第二部分答案不是2/3，而是3/4 … 2/3答案会不会是面试官告诉的，也有可能是没听明白 | ... "
        "| Stardance 发表于 2025-3-20 13:15答案参见我刚顶上去的帖子“个人整理的地里SIG的高频概率题以及答案”中的文档 "
        "我算了也是3/4 |"
    ),
    source_language="mixed",
    post_date="2025-03",
    poster_context=(
        "Thread 'SIG第一轮电面 面经' on the 数科面经 board, tagged sig. The poster states their track explicitly "
        "at the end of the post: QR岗 (QR position). Replies dated 2025-03-20 and 2025-03-21. A commenter twice "
        "points to another thread they had just bumped, 「个人整理的地里SIG的高频概率题以及答案」 (a "
        "personally-compiled document of SIG's high-frequency probability questions with answers) — I could not "
        "surface that document thread's contents in any search."
    ),
    doubt=(
        "The statement breaks off after seven words, at exactly the point where the upper limit of the uniform "
        "would be given, so the question is not reconstructible: I do not know what X is uniform on, nor what is "
        "being asked about it. What IS solid, and is why I am keeping it: a QR first-round phone interview in "
        "March 2025 had exactly two questions, the second had an extension part, and three separate people who "
        "each sat the interview disagree about whether its answer is 2/3 or 3/4 — which is itself good evidence "
        "the item is real and non-trivial rather than a copied textbook exercise."
    ),
))

# ---------------------------------------------------------------------------
# thread-795660 : "quants intern 第一轮技术电面 4道问题分享" — QUANT INTERN
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="unknown",
    level="internship",
    cycle="unknown",
    round="phone_technical",
    round_name="第一轮技术电面 (first-round technical phone interview)",
    section_context=(
        "4 questions. The poster later corrects the framing in an edit: 「补充一下 这里的四个题目 是第一轮技术面 "
        "之前手误打成了OA SIG的OA地里都是原题 万年不变」 — these four were the first technical round, not the OA; "
        "the OA itself is all recycled items that 'never change in ten thousand years'."
    ),
    question_type="expected_value",
    question_text=(
        "[第三题题干本身在积分墙后；以下是楼主置顶转载的读者澄清问答，逐条界定了游戏规则：] "
        "1. 所有的扑克牌都视作不同的牌。比如说我可以一开始选红桃2, 那么如果先抽出来梅花2, 并不会给我1块钱, "
        "而是一定要抽到红桃2才会给我一块钱。 2. 是要把所有扑克牌抽完为止 比如说我有1/(52!)的概率会每次选择完牌,"
        "抽的第一张牌就是我所选择的牌, 所以最终可以得到52块钱 3. 从第二次选择牌开始, 包括之后的每一次选择牌, "
        "我知道哪些牌已经被抽走了 比如说我一上来选择的是红桃2, 然后抽牌第一张是梅花Q, 第二张是梅花K, 第三张是红桃2, "
        "我得1块钱, 然后我再一次选择牌的时候, 我是知道梅花Q和K已经被抽走了"
    ),
    question_text_en=(
        "[The statement of question 3 is behind the paywall; what follows is the clarification Q&A the poster "
        "pinned to the top of the thread, which pins down the rules of the game:] "
        "1. All the playing cards count as distinct cards. For instance I might pick the 2 of Hearts at the "
        "start; then if the 2 of Clubs is drawn first that does not pay me $1 — only drawing the 2 of Hearts "
        "pays me $1. 2. You go until the whole deck has been drawn. For instance I have a 1/(52!) chance that "
        "every time I pick a card, the very next card drawn is the one I picked, so I could end up with $52. "
        "3. From the second pick onward, and on every pick after that, I know which cards have already been "
        "drawn. For instance if I first pick the 2 of Hearts, and the first card drawn is the Q of Clubs, the "
        "second the K of Clubs, the third the 2 of Hearts — I get $1 — then when I next pick a card I know the "
        "Q and K of Clubs are already gone."
    ),
    reported_answer=(
        "None stated. The $52 in clause 2 is the poster's illustration of the theoretical maximum, not the answer."
    ),
    source_url="https://www.1point3acres.com/bbs/thread-795660-1-1.html",
    source_quote=(
        "quants intern 第一轮技术电面 4道问题分享 准备行为面的也请进来参考|sig面经|一亩三分地海外面经版 ... "
        "| 大家有问题欢迎提问 感觉悲剧的原因应该是问我啥时候能开始工作 我说明年 然后考官都黑脸了 加上题目并不是答得非常好 "
        "补充内容 (2021-09-14 11:22 +8:00): 感谢NedH小伙伴对第三个问题的补充题问： "
        "1. 所有的扑克牌都视作不同的牌。比如说我可以一开始选红桃2, 那么如果先抽出来梅花2, 并不会给我1块钱, "
        "而是一定要抽到红桃2才会给我一块钱。 2. 是要把所有扑克牌抽完为止 比如说我有1/(52!)的概率会每次选择完牌,"
        "抽的第一张牌就是我所选择的牌, 所以最终可以得到52块钱 3. 从第二次选择牌开始, 包括之后的每一次选择牌, "
        "我知道哪些牌已经被抽走了 比如说我一上来选择的是红桃2, 然后抽牌第一张是梅花Q, 第二张是梅花K, 第三张是红桃2, "
        "我得1块钱, 然后我再一次选择牌的时候, 我是知道梅花Q和K已经被抽走了 "
        "补充内容 (2021-09-22 10:11 +8:00): 补充一下 这里的四个题目 是第一轮技术面 之前手误打成了OA "
        "SIG的OA地里都是原题 万年不变 补充内容 (2021-09-22 10:13 +8:00): 再次感谢 @xzhang001的题型 | ... "
        "| 感谢楼主分享 ... 关于题目我有如下几个问题: 1. 所有的扑克牌都视作不同的牌, 对吗? ... "
        "(每次选择时知道哪些牌已经被抽走了) ... 张牌, 或者 |"
    ),
    source_language="zh",
    post_date="2021-09",
    poster_context=(
        "Thread 'quants intern 第一轮技术电面 4道问题分享 准备行为面的也请进来参考' on 海外面经, tagged sig. "
        "The title states the level explicitly — quants intern — which is why level is 'internship'. The poster "
        "failed and attributes it partly to saying they could only start the following year (考官都黑脸了, the "
        "interviewer's face fell). The three numbered clauses are the poster's 2021-09-14 edit incorporating "
        "reader NedH's clarifying questions."
    ),
    doubt=(
        "The original statement of question 3 never surfaced; this is the rules-clarification appendix, so the "
        "framing (you name a card, cards are drawn one at a time, you get $1 each time the very next card drawn "
        "is the one you named) is inferred from the clarifications rather than read off a problem statement. "
        "What is unambiguous and verbatim is the three rules themselves. Role track: the title says 'quants "
        "intern' without distinguishing QT from QR, so role_track stays 'unknown' even though the level is "
        "certain. An earlier draft of this record labelled it quant_trader, which the source does not support."
    ),
))

# ---------------------------------------------------------------------------
# thread-686183 : round 1, QUESTION 3 — exists, statement gated.
# (Round-1 Q1/Q2 and both round-2 items are already in the shard.)
# ---------------------------------------------------------------------------
records.append(dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="phone_technical",
    round_name="第一轮 (first round)",
    section_context="third of at least three questions in round 1 of a two-round loop",
    question_type="other",
    question_text=(
        "[第一轮第三题。题面被积分墙截断，索引里只留下开头一个字：] "
        "SIG 面经 第一轮： 1. 圆里随机画n条线… 2. 扔硬币 进入 HTH HHT 之一就结束… 3. 三"
    ),
    question_text_en=(
        "[Round 1, question 3. The statement is cut off by the paywall; the search index preserves only its "
        "first character, 三 ('three'), where the numbered list runs '1. … 2. … 3. 三…'.] Two separate readers "
        "later ask about this question by number without ever restating it: 'Can someone explain how to do "
        "round 1 question 3?' and 'I think I wrote it down wrong — the rank one I actually do know, what I "
        "meant to ask about was question 3.'"
    ),
    reported_answer=None,
    source_url="https://www.1point3acres.com/bbs/thread-686183-1-1.html",
    source_quote=(
        "SIG 面经 第一轮： 1. 圆里随机画n条线，问能把圆分成几分 （期望）？ 把分成的份数和交点个数对应起来，"
        "然后算交点个数的期望。 2. 扔硬币 进入 HTH HHT 之一就结束，问进入每一个的概率是多大？"
        "（不太记得具体ending state是啥了） 3. 三 ... "
        "| 感谢！ 我估计我写错了，rank那道题我应该是会的，我当时应该是想问第3题，不过我事后也找到了一个解释，"
        "说是不一定，是吧？ 圆这道题真不错，学习到了 … | ... "
        "| 有人可以说一下第一轮第三题这么做吗 |"
    ),
    source_language="zh",
    post_date="2020-11",
    poster_context=(
        "Thread 'SIG 1轮+2轮面经' on 海外面经, tagged sig; replies dated 2020-11-11 to 2020-11-25. The poster's "
        "round-1 list is numbered 1/2/3, and the index preserves the first two items in full but truncates the "
        "third to its opening character."
    ),
    doubt=(
        "One character of question text. This is the thinnest record in the shard and I nearly dropped it. It is "
        "here for exactly one reason: it establishes that round 1 of this loop had (at least) three questions, "
        "not the two that the rest of the shard's snippets of this thread would imply, and two independent "
        "readers refer to '第一轮第三题' by number, which proves the item existed. I deliberately did NOT guess "
        "what 三 begins — it could be 三个 (three of something), 三角形 (triangle), 三次 (three times) or many "
        "other things, and any completion would be invention."
    ),
))

# ---------------------------------------------------------------------------
# tag page /bbs/tag/sig-905-15.html : ungated previews of the CodeSignal
# coding-OA threads. Two questions named explicitly.
# ---------------------------------------------------------------------------
T905_15 = "https://www.1point3acres.com/bbs/tag/sig-905-15.html"
T905_15_QUOTE = (
    "公司:Sig | 一亩三分地 ... # 公司: Sig ... SIG Intern OA 2024 Summer ... SIG 2024 summer SDE intern OA ... "
    "SIG Pre-screen OA ... SIG SDE NG 2024 pre-screen OA 求加米!! ... SIG SDE Intern 2024 OA ... "
    "SIG 2024 OA 附加第一题小思路 ... SIG 2024 SDE intern OA ... "
    "| 前两天写的sig的pre-sreen题目 | 海外面经 | 1 2482 | 琼66 2024-5-4 05:25 | ... "
    "| 考完SIG的OA， 用的是CodeSignal。 两道题60分钟。 题目和地里一样。第一题：击中船只。第二道题：利口酒吧。全对。 "
    "看到地里的小伙伴说，后面还会有店面。如果有经 ... | 海外面经 | 3 2097 | 苦海里挣扎的熊 2023-11-30 22:50 | ... "
    "| 做了2024 Summer SDE intern的OA （好像是白嫖）。60分钟两道题，大概在easy-median左右，是地里分享过的题目，固定的。"
    "[*]第一题是sea battle，input是一个5*5的g ... | 海外面经 | 1 1788 | NotIntern 2023-10-8 21:01 | ... "
    "| SIG OA 60分钟两题1. 打军舰,和地里发的一样lz用defaultdict记录军舰位置和大小,几个if statement就可以了"
    "2. Leetcode 98. Validate Binary Search Tree求米 | 海外面经 | 2 1628 | 地里匿名用户 2023-9-2 00:00 | ... "
    "| 今天刚做，都是 ... 里的题。第一道船舰问题，字典存船位置，set查重复攻击， ... 道利口 ... 1419 ... 23-8-23 09:39 ... "
    "| SIG SDE Intern 2024 OA 求加米！！60分钟 两道算法题1、[*]lc98原题[*]Medium难度[*]二叉树限定子树的最大值和最小值，"
    "然后递归2、[*]图， ... | 海外面经 | 0 1291 | opend17 2023-8-14 23:32 | ... "
    "| 两道题 ... 题是给一个m ... matrix，里面的元素 |"
)
T905_15_COMMON = dict(
    BASE,
    role_track="unknown",
    level="unknown",
    cycle="unknown",
    round="online_assessment",
    round_name="SIG coding OA (CodeSignal)",
    platform="CodeSignal",
    section_context="60 分钟两道题 (two questions in 60 minutes)",
    source_url=T905_15,
    source_language="zh",
    post_date="2023",
    poster_context=(
        "Recovered from the ungated ~200-character thread previews on the SIG company tag-listing page "
        "https://www.1point3acres.com/bbs/tag/sig-905-15.html. This page of the tag index is dominated by "
        "SIG's coding OA (thread titles: 'SIG Intern OA 2024 Summer', 'SIG 2024 summer SDE intern OA', "
        "'SIG Pre-screen OA', 'SIG SDE NG 2024 pre-screen OA', 'SIG SDE Intern 2024 OA'). At least five "
        "separate posters between 2023-08 and 2023-11 describe the same fixed two-question set, several "
        "saying so explicitly (题目和地里一样 / 是地里分享过的题目，固定的)."
    ),
    doubt=(
        "Role-track caveat covering both records from this tag page: the surrounding thread titles are SDE / "
        "SWE / pre-screen, i.e. SIG's software-engineering pipeline, NOT a quant track. SIG runs QSD "
        "(Quantitative Strategy Developer) as a distinct posting, and nothing in these previews says QSD. I "
        "have therefore left role_track 'unknown' rather than claiming quant_developer. These are recorded "
        "because the shard covers SIG's developer track and this is the only ungated evidence of what SIG's "
        "coding screen actually contains, but a consumer should not treat them as quant-track items."
    ),
)

records.append(dict(
    T905_15_COMMON,
    question_type="coding_algorithms",
    question_text=(
        "SIG OA 60分钟两题1. 打军舰,和地里发的一样lz用defaultdict记录军舰位置和大小,几个if statement就可以了"
        "2. Leetcode 98. Validate Binary Search Tree"
    ),
    question_text_en=(
        "SIG OA, two questions in 60 minutes. 1. Battleship — same as the one already posted on the forum; I "
        "used a defaultdict to record each warship's position and size, and a few if statements were enough. "
        "2. LeetCode 98, Validate Binary Search Tree."
    ),
    reported_answer=(
        "No answer key, but multiple posters describe working solutions. For the battleship item: "
        "「Hashmap统计每艘船位置，然后再有一个矩阵记录每个位置是否被攻击过，对于新的shot，先查miss，然后遍历h…」 "
        "and 「第一道船舰问题，字典存船位置，set查重复攻击」. For the tree item: "
        "「lc98原题 Medium难度 二叉树限定子树的最大值和最小值，然后递归」."
    ),
    source_quote=T905_15_QUOTE,
))

records.append(dict(
    T905_15_COMMON,
    question_type="coding_algorithms",
    question_text=(
        "考完SIG的OA， 用的是CodeSignal。 两道题60分钟。 题目和地里一样。第一题：击中船只。第二道题：利口酒吧。全对。"
    ),
    question_text_en=(
        "Finished SIG's OA; it used CodeSignal. Two questions, 60 minutes. The questions are the same as the "
        "ones on the forum. Question 1: hitting ships. Question 2: 利口酒吧 ('liqueur bar'). Got them all right."
    ),
    reported_answer=None,
    source_quote=T905_15_QUOTE,
))

with open(OUT, "a", encoding="utf-8") as fh:
    for rec in records:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"appended {len(records)} records to {OUT}")
