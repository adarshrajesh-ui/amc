#!/usr/bin/env python3
"""Two Nowcoder threads: a first-person Citadel HK quant-intern phone recall, and a
Jane Street question compilation.

The two differ sharply in provenance and the records say so. 353157497731096576 is one
candidate narrating two rounds he sat and failed; 604265548247040000 is a WeChat
public-account operator republishing reader submissions and upselling a paid 知识星球.
Both are real retrieved pages, so both go in, but the doubt fields are not
interchangeable.

Question text is sliced out of the literal page text held below rather than retyped per
record, so the Chinese cannot drift between `question_text` and `source_quote`.
"""
import re
import sys

sys.path.insert(0, "/workspace/harvest/tools")
import tiera_lib

CIT_URL = "https://www.nowcoder.com/discuss/353157497731096576"
JS_URL = "https://www.nowcoder.com/discuss/604265548247040000"

CIT_R1 = (
    "一面小哥是刚毕业的牛津统计phd，ml方向，聊了十几分钟简历项目，然后开始问线性回归，"
    "解析解是什么，如果样本数量n很大不能同时放进内存怎么办，分成几部分来算，为什么可以这样做，"
    "因为XTX是dxd的矩阵。如果两个变量0.999相关，权重会如何分配，如果是lasso 和 ridge分别会如何，"
    "实践中如何选择保留哪个变量。如果在x加上噪声，会怎么样，分别从直观感受和推导上说，"
    "最后一直说到给x加噪声可以起到和正则化同样的作用。"
)
CIT_R2 = (
    "二面是刚毕业的牛津数学phd，俄罗斯小哥。先聊了二十分钟简历项目，然后问一堆数据复制一遍，"
    "mean和variance会不会变。接下去本来以为会问数学，结果问了两道算法，都不用写代码，口述思路。"
    "先是求第n个斐波那契数，时空复杂度，然后问了如何优化，说了矩阵快速幂，问了一些具体的做法。"
    "然后是给定一堆x，求y使得 sum|x_i-y| 最小，随口说了mean，面试官说是median，然后问怎么median，"
    "先说了排序，又问怎么优化，说了quick select，然后让对比quick select和quick sort。"
)
CIT_HEAD = (
    "牛客逛了一圈没有看到类似的面经，就分享一下。lz港校cs phd，非主流生物方向。找了一圈quant的实习，"
    "没有相关实习经历，research也不太行，基本都在简历就挂了，akuna上海挂在第一轮电面，"
    "大城堡投了两次终于被捞起来，上个月给了一个电面，上周又面了一轮，然后挂了。"
)


def span(hay, start, end_marker):
    """Contiguous slice of the page text from `start` through `end_marker` inclusive."""
    i = hay.index(start)
    j = hay.index(end_marker, i) + len(end_marker)
    return hay[i:j]


CIT_POSTER = ("香港高校 CS PhD（自述『非主流生物方向』），无量化相关实习经历，投过两次才被捞起，"
              "面完两轮电面后挂；同期 akuna 上海挂在第一轮电面。帖子标题『城堡hk量化实习两轮电面挂经』，"
              "标签 #实习##面经##算法工程师#。")
CIT_DOUBT = ("Nowcoder renders no visible publication date on the fetched page, so the cycle and "
             "recency of this recall cannot be pinned down at all — the questions could be several "
             "years old; also the poster writes from memory in summary form, so wording is his "
             "paraphrase of the interviewer rather than the interviewer's words.")

CIT = [
    # (question span start, span end marker, question_text override, type, round_name)
    (CIT_R1, "然后开始问线性回归，解析解是什么", None, "statistics_regression", "一面（电面）"),
    (CIT_R1, "如果样本数量n很大不能同时放进内存怎么办，分成几部分来算，为什么可以这样做，因为XTX是dxd的矩阵。",
     None, "statistics_regression", "一面（电面）"),
    (CIT_R1, "如果两个变量0.999相关，权重会如何分配，如果是lasso 和 ridge分别会如何，实践中如何选择保留哪个变量。",
     None, "statistics_regression", "一面（电面）"),
    (CIT_R1, "如果在x加上噪声，会怎么样，分别从直观感受和推导上说，最后一直说到给x加噪声可以起到和正则化同样的作用。",
     None, "statistics_regression", "一面（电面）"),
    (CIT_R2, "然后问一堆数据复制一遍，mean和variance会不会变。", None, "statistics_regression", "二面（电面）"),
    (CIT_R2, "先是求第n个斐波那契数，时空复杂度，然后问了如何优化，说了矩阵快速幂，问了一些具体的做法。",
     None, "coding_algorithms", "二面（电面）"),
    (CIT_R2, "然后是给定一堆x，求y使得 sum|x_i-y| 最小，随口说了mean，面试官说是median，然后问怎么median，先说了排序，又问怎么优化，说了quick select，然后让对比quick select和quick sort。",
     None, "coding_algorithms", "二面（电面）"),
]

CIT_EN = {
    0: "Linear regression: what is the closed-form (analytic) solution?",
    1: "If the number of samples n is so large that the data cannot all be held in memory at once, what do you do? Split it into several parts and compute; why is that valid? (Because X^T X is a d x d matrix.)",
    2: "If two variables are 0.999 correlated, how will the weights be distributed? What happens under lasso and under ridge respectively? In practice how do you choose which variable to keep?",
    3: "If you add noise to x, what happens? Explain both intuitively and by derivation. (Led to: adding noise to x has the same effect as regularisation.)",
    4: "If you duplicate a pile of data (each point repeated once), do the mean and the variance change?",
    5: "Find the n-th Fibonacci number; give the time and space complexity, then how would you optimise it? (Matrix fast exponentiation, and the specifics of how to do it.)",
    6: "Given a pile of x values, find y minimising sum|x_i - y|. (Answer: the median, not the mean.) Then how do you find the median? Sorting first, then how to optimise -- quickselect; then compare quickselect with quicksort.",
}
CIT_ANS = {
    1: "因为XTX是dxd的矩阵",
    3: "给x加噪声可以起到和正则化同样的作用",
    5: "矩阵快速幂",
    6: "面试官说是median；优化用 quick select",
}

recs = []
for n, (blob, marker, override, qtype, rname) in enumerate(CIT):
    q = marker
    assert q in blob, q[:30]
    recs.append({
        "firm": "Citadel",
        "role_track": "unknown",
        "level": "internship",
        "cycle": "unknown",
        "office": "Hong Kong",
        "round": "phone_technical",
        "round_name": rname,
        "platform": "unknown",
        "section_context": None,
        "question_type": qtype,
        "question_text": override or q,
        "question_text_en": CIT_EN[n],
        "reported_answer": CIT_ANS.get(n),
        "source_url": CIT_URL,
        "source_type": "nowcoder",
        "source_quote": q,
        "source_language": "zh",
        "post_date": "unknown",
        "access": "full_text",
        "retrieval_method": "webfetch",
        "poster_context": CIT_POSTER,
        "doubt": CIT_DOUBT,
    })

# ---------------------------------------------------------------- Jane Street

JS_QS = [
    ("箱子里有2个红球，2个蓝球。从箱子里抽球抽到蓝球+1，抽到红球-1。求最佳策略。",
     "expected_value",
     "A box holds 2 red balls and 2 blue balls. Drawing a blue ball scores +1, drawing a red ball scores -1. Find the optimal strategy."),
    ("两个玩家，轮流说2-30里的数。如果玩家说了的数和之前的被说的数有公因数，玩家输。你会当玩家1（先说）还是玩家 2（后说）。",
     "logic_brainteaser",
     "Two players alternately name a number from 2 to 30. If a player names a number sharing a common factor with a previously named number, that player loses. Would you rather be player 1 (moving first) or player 2 (moving second)?"),
    ("比较以下三个expectation的大小：(1) 扔一次骰子，扔出的值的平方(2) 扔两次骰子，两次值的乘积(3) 扔五次骰子，中位数的平方",
     "expected_value",
     "Rank these three expectations: (1) roll a die once, the square of the value rolled; (2) roll a die twice, the product of the two values; (3) roll a die five times, the square of the median."),
    ("扔1000个fair coins，500个silver 500个gold，gold正面得3块，silver正面得1块，问如果已知得了1100块，expected number of gold coins with heads up 是多少。",
     "probability",
     "Flip 1000 fair coins, 500 silver and 500 gold. A gold coin landing heads pays 3 dollars, a silver coin landing heads pays 1 dollar. Given that you received 1100 dollars, what is the expected number of gold coins showing heads?"),
    ("一个骰子上的数字为 1 到 6，另一个骰子上的数字为 1 到 10，猜两个骰子之和，如果猜中了就可以得到这个和所对应的收益，问猜多少期望收益最大。",
     "expected_value",
     "One die is numbered 1 to 6, the other 1 to 10. You guess the sum of the two dice; if you guess correctly you receive a payoff equal to that sum. What should you guess to maximise expected payoff?"),
    ("一圈公路有1mile长，一辆车绕着开第一圈的速度是60mile/hour，第二圈的速度是90mile/hour，求平均速度。",
     "logic_brainteaser",
     "A loop of road is 1 mile long. A car drives the first lap at 60 miles per hour and the second lap at 90 miles per hour. What is the average speed?"),
    ("扔 4 个硬币，一个正面值 1 元。在观察第一次结果后，你可以接受结果或者再把所有的硬币投第二次，此时必须接受新的收益。问最优策略是什么，以及其对应的期望收益。",
     "expected_value",
     "Flip 4 coins; each head is worth 1 dollar. After seeing the first result you may either accept it or reflip all the coins a second time, in which case you must accept the new payoff. What is the optimal strategy and its expected payoff?"),
    ("周六下雨的概率是0.3，周天下雨概率是0.4，如果是independent，求周末下雨概率。如果不independent，求周末下雨概率的range。",
     "probability",
     "The probability of rain on Saturday is 0.3 and on Sunday is 0.4. If they are independent, find the probability of rain over the weekend. If they are not independent, find the range of that probability."),
    ("一头熊在河里捕鱼，它吃 3 条鱼可以吃饱，同时每条鱼被捉到的概率是0.5，计算河里第五条鱼存活的概率是多少。",
     "probability",
     "A bear is catching fish in a river. It is full after eating 3 fish, and each fish is caught with probability 0.5. What is the probability that the fifth fish in the river survives?"),
    ("一个盒子有 100 元钱，你和对手分别在纸上写下数字，如果数字之和小于等于 100，那么你们可以各自拿到与自己写下数字价值相同的钱，而如果数字之和大于 100 则两个人都拿不到钱。假设对手是理性的，你的最优策略是什么？ Follow up：不再假设对手理性，并且将这个博弈进行 1000 遍，第一次对手说他会写 80，你会怎么办？如果游戏进行了十次，他每次都写 80，你会如何权衡？",
     "poker_game_theory",
     "A box contains 100 dollars. You and an opponent each write a number on paper. If the sum is at most 100 you each receive money equal to the number you wrote; if the sum exceeds 100 neither of you gets anything. Assuming the opponent is rational, what is your optimal strategy? Follow-up: dropping the rationality assumption and playing the game 1000 times, if the opponent says up front he will write 80, what do you do? If the game has been played ten times and he wrote 80 every time, how do you weigh it up?"),
]

JS_POSTER = ("Nowcoder account reposting a WeChat public-account digest: 『关注我们，每周发布最新的"
             "笔面试题目和解析』『更新一小部分Jane Street面试问题汇总，更全的笔面试资料在知识星球中』, "
             "soliciting reader submissions (『欢迎同学们在公众号后台留言投稿』). Tagged "
             "#量化私募##量化面经##JaneStreet#. Title dates the set 20240401.")
JS_DOUBT = ("Vendor-adjacent aggregator, not a first-person recall: the poster monetises a paid "
            "知识星球 ('会随着资源的积累不断涨价，早加入早学习早拿offer早赚米') and pays for 投稿, so "
            "items could be recycled from a question bank rather than from a sitting; several "
            "(bear-and-fish, weekend rain, the 100-dollar split game) are also standard "
            "green-book/brainteaser fare, though independent 1point3acres recalls in this corpus "
            "attest the rain and the split-the-pot game for Jane Street as well.")

for qtext, qtype, qen in JS_QS:
    recs.append({
        "firm": "Jane Street",
        "role_track": "unknown",
        "level": "unknown",
        "cycle": "unknown",
        "office": "unknown",
        "round": "unknown",
        "round_name": "Jane Street面试题",
        "platform": "unknown",
        "section_context": None,
        "question_type": qtype,
        "question_text": qtext,
        "question_text_en": qen,
        "reported_answer": None,
        "source_url": JS_URL,
        "source_type": "nowcoder",
        "source_quote": qtext,
        "source_language": "zh",
        "post_date": "2024-04-01",
        "access": "full_text",
        "retrieval_method": "webfetch",
        "poster_context": JS_POSTER,
        "doubt": JS_DOUBT,
    })

assert CIT_HEAD  # the framing paragraph the poster_context above paraphrases
tiera_lib.write(recs)
