#!/usr/bin/env python3
"""Batch 3: two full-text Chinese recalls of the Optiver SDE-intern pipeline.

Both pages were fetched whole. The nowcoder body is server-rendered into the HTML
outside <script>, so these quotes survive a plain re-fetch and tag-strip - checked
before writing, because an earlier pass in this project logged 74 unverifiable
nowcoder quotes.
"""
import sys
sys.path.insert(0, "/workspace/harvest/tools")
from tiera_lib import write

R = []

# ===========================================================================
# nowcoder: "985废柴挑战顶级量化optiver笔试"
# 2025 Shanghai Software Developer Summer Internship. Three-part OA.
# ===========================================================================
NC = "https://www.nowcoder.com/feed/main/detail/3d62edffa9dc40c883d3d019dd7f6789"
NC_P1 = ("2025 Shanghai Software Developer Summer Internshippart1是HackerRank里的，个人实力不济，选择躺平。"
         "第一道写一个newsProvider类，需要实现AddSubscription，RemoveSubscription，NewsReceived，HashMap方法。"
         "第二道写一个卫星网络的类，要实现SatelliteConnected，RelationshipEstablished，MessageReceived三个方法。too hard!")
NC_P2 = ("part2是20道不定项选择题：多线程利用多CPU架构；关系数据库中规范化是什么；二维数组两种遍历方式的快慢；"
         "哈希一些操作的时间复杂度；Linux的system call时间开销为50ns；对于动态数组，哪项平均时间复杂度最低；"
         "小明想学python和java，不推荐哪本书；子网掩码定义同一网络的IP地址范围；UDP传输会发生什么情况；"
         "四个16进制数哪些小于100；给栈操作选最后栈的内容；选择邻接矩阵比领接链表的优势；在多线程程序中修复错误共享；"
         "二进制表示16位整数需要多少位；TCP/IP在哪些情况下不是好的选择；位运算；哪一个概念不用于多线程中的同步；"
         "在给的一个二叉搜索树中对随机的一个node平均比较几次；向空堆中插入65个元素，深度是多少；哪些协议用于Linux进程间通信。")
NC_P3 = ("part3是9个小游戏。1、Balloon，每次充气花费$0.1, 超过某个值会爆炸，爆炸前收回当前的金额。"
         "第一次有30轮，金额不限；第二次20轮，在上次获得的金额基础上打气。本人采用激进的策略结束时是$35,应该不是投资goat。"
         "2、Skyscraper，类似汉诺塔，三个柱子，一些不同颜色的块移动到答案一致。"
         "3、Shapeshift，考反应，出现矩形按左方向键，圆形按右方向键。"
         "4、the switch，有两个框，上面看和是不是奇数，下面框看两组箭头是不是相同。"
         "5、code compare， 一个字符串，有四个选项，选相同字符串，每次估计就5-6秒。我只能记住前三个来做判断(囧)"
         "6、number Box，四个数和中间的结果，通过加减乘除法计算出结果"
         "7、figure it out，猜盖住的牌。最多16种组合，图形，颜色，图纹，点。每次会显示和盖住的牌对比错误和正确几项。"
         "另外两个记不清了，求原谅。")

NC_BASE = dict(
    firm="Optiver", source_url=NC, source_type="nowcoder", source_language="zh",
    access="full_text", retrieval_method="webfetch", post_date="unknown",
    office="Shanghai", role_track="quant_developer", level="internship",
    cycle="Summer 2025", round="online_assessment",
    poster_context="Nowcoder post titled 985废柴挑战顶级量化optiver笔试, tagged #找实习#; the author opens by naming the role as '2025 Shanghai Software Developer Summer Internship' and says of part 1 个人实力不济，选择躺平 (he gave up on it).",
    reported_answer=None,
)
NC_DOUBT_TAIL = ("Nowcoder shows no post date on this page, so the timing is only fixed by the author's own "
                 "'2025 Shanghai Software Developer Summer Internship' label.")

# --- part 1: two HackerRank design problems -------------------------------
R.append(dict(NC_BASE, round_name="part1 (HackerRank)", platform="HackerRank",
    section_context="part1是HackerRank里的",
    question_type="coding_algorithms",
    question_text="第一道写一个newsProvider类，需要实现AddSubscription，RemoveSubscription，NewsReceived，HashMap方法。",
    question_text_en="Problem 1: write a newsProvider class implementing the methods AddSubscription, RemoveSubscription, NewsReceived and HashMap.",
    source_quote=NC_P1,
    doubt="Only the class and method names survive; the actual semantics, inputs and constraints are not recorded, and the author admits he did not seriously attempt part 1. " + NC_DOUBT_TAIL,
))
R.append(dict(NC_BASE, round_name="part1 (HackerRank)", platform="HackerRank",
    section_context="part1是HackerRank里的",
    question_type="coding_algorithms",
    question_text="第二道写一个卫星网络的类，要实现SatelliteConnected，RelationshipEstablished，MessageReceived三个方法。",
    question_text_en="Problem 2: write a satellite-network class implementing three methods: SatelliteConnected, RelationshipEstablished, MessageReceived.",
    source_quote=NC_P1,
    doubt="Same as problem 1: method signatures only, no problem statement, and the author says 'too hard!' rather than describing what was required. " + NC_DOUBT_TAIL,
))

# --- part 2: the 20 multiple-select knowledge questions --------------------
P2_ITEMS = [
    ("多线程利用多CPU架构", "How multithreading exploits a multi-CPU architecture", "other"),
    ("关系数据库中规范化是什么", "What normalisation is in a relational database", "other"),
    ("二维数组两种遍历方式的快慢", "Which of two traversal orders of a 2-D array is faster", "coding_algorithms"),
    ("哈希一些操作的时间复杂度", "Time complexity of some hash-table operations", "coding_algorithms"),
    ("Linux的system call时间开销为50ns", "A Linux system call costs 50ns [of overhead]", "other"),
    ("对于动态数组，哪项平均时间复杂度最低", "For a dynamic array, which operation has the lowest average time complexity", "coding_algorithms"),
    ("小明想学python和java，不推荐哪本书", "Xiao Ming wants to learn Python and Java - which book would you NOT recommend", "other"),
    ("子网掩码定义同一网络的IP地址范围", "A subnet mask defines the range of IP addresses on the same network", "other"),
    ("UDP传输会发生什么情况", "What can happen during UDP transmission", "other"),
    ("四个16进制数哪些小于100", "Which of four hexadecimal numbers are less than 100", "mental_math_speed"),
    ("给栈操作选最后栈的内容", "Given a sequence of stack operations, choose the final contents of the stack", "coding_algorithms"),
    ("选择邻接矩阵比领接链表的优势", "Choose the advantage of an adjacency matrix over an adjacency list", "coding_algorithms"),
    ("在多线程程序中修复错误共享", "Fixing false sharing in a multithreaded program", "coding_algorithms"),
    ("二进制表示16位整数需要多少位", "How many bits are needed to represent a 16-bit integer in binary", "other"),
    ("TCP/IP在哪些情况下不是好的选择", "In which situations is TCP/IP not a good choice", "other"),
    ("位运算", "Bit operations", "other"),
    ("哪一个概念不用于多线程中的同步", "Which concept is NOT used for synchronisation in multithreading", "other"),
    ("在给的一个二叉搜索树中对随机的一个node平均比较几次", "In a given binary search tree, how many comparisons on average to reach a random node", "coding_algorithms"),
    ("向空堆中插入65个元素，深度是多少", "Insert 65 elements into an empty heap - what is the depth", "coding_algorithms"),
    ("哪些协议用于Linux进程间通信", "Which protocols are used for inter-process communication on Linux", "other"),
]
for zh, en, qt in P2_ITEMS:
    R.append(dict(NC_BASE, round_name="part2 (20道不定项选择题)", platform="unknown",
        section_context="part2是20道不定项选择题",
        question_type=qt, question_text=zh, question_text_en=en,
        source_quote=NC_P2,
        doubt="The author lists all twenty items as short topic labels, not as full prompts, so the options and the precise question wording are lost; several labels are ambiguous enough that the intended question could be read more than one way. " + NC_DOUBT_TAIL,
    ))

# --- part 3: the Zap-N mini-games ----------------------------------------
P3_ITEMS = [
    ("1、Balloon，每次充气花费$0.1, 超过某个值会爆炸，爆炸前收回当前的金额。第一次有30轮，金额不限；第二次20轮，在上次获得的金额基础上打气。",
     "Game 1, Balloon: each pump costs $0.1; past some threshold the balloon bursts; bank the current amount before it bursts. The first run has 30 rounds with no cap on the amount; the second has 20 rounds, pumping on top of what you won last time.",
     "trading_game", "本人采用激进的策略结束时是$35,应该不是投资goat。"),
    ("2、Skyscraper，类似汉诺塔，三个柱子，一些不同颜色的块移动到答案一致。",
     "Game 2, Skyscraper: like Towers of Hanoi - three pegs, a number of differently coloured blocks to be moved until they match the target.",
     "logic_brainteaser", None),
    ("3、Shapeshift，考反应，出现矩形按左方向键，圆形按右方向键。",
     "Game 3, Shapeshift: a reaction test - press the left arrow key when a rectangle appears, the right arrow key when a circle appears.",
     "other", None),
    ("4、the switch，有两个框，上面看和是不是奇数，下面框看两组箭头是不是相同。",
     "Game 4, the switch: there are two boxes; in the upper one you judge whether a sum is odd, in the lower one whether two groups of arrows are the same.",
     "mental_math_speed", None),
    ("5、code compare， 一个字符串，有四个选项，选相同字符串，每次估计就5-6秒。",
     "Game 5, code compare: one string and four options; pick the identical string. Roughly 5-6 seconds each.",
     "other", "我只能记住前三个来做判断(囧)"),
    ("6、number Box，四个数和中间的结果，通过加减乘除法计算出结果",
     "Game 6, number Box: four numbers and a target result in the middle; reach the result using addition, subtraction, multiplication and division.",
     "mental_math_speed", None),
    ("7、figure it out，猜盖住的牌。最多16种组合，图形，颜色，图纹，点。每次会显示和盖住的牌对比错误和正确几项。",
     "Game 7, figure it out: guess the covered card. At most 16 combinations across shape, colour, pattern and dots. Each time it shows how many attributes match the covered card and how many do not.",
     "logic_brainteaser", None),
]
for zh, en, qt, ans in P3_ITEMS:
    R.append(dict(NC_BASE, round_name="part3 (9个小游戏)", platform="unknown",
        section_context="part3是9个小游戏",
        question_type=qt, question_text=zh, question_text_en=en,
        source_quote=NC_P3, reported_answer=ans,
        doubt="Described from memory in one or two lines each, with scoring rules and exact parameters mostly absent; the author says of the remaining two games 另外两个记不清了 (cannot remember), so the section is only partly recovered. " + NC_DOUBT_TAIL,
    ))

# ===========================================================================
# xjtu.app: "Optiver 挂经 & 反思总结" - SDE Intern, OA through third round.
# ===========================================================================
XJ = "https://xjtu.app/t/topic/12756"
XJ_OA = ("算法题是在 HackerRank 平台上，两道不太简单的题目。给到我的是一个 LogServer 背景的数据结构题和一个图论题，"
         "当时我没怎么准备，也不太在状态，写的都不好。LogServer 正解感觉是平衡树，图论是拓扑排序；")
XJ_BASE = dict(
    firm="Optiver", source_url=XJ, source_type="university_bbs", source_language="zh",
    access="full_text", retrieval_method="webfetch", post_date="unknown",
    office="unknown", role_track="quant_developer", level="internship",
    cycle="unknown",
    poster_context="Xi'an Jiaotong University community (交大门) write-up: 我从三月开始投 Optiver 到五月下旬收到拒信，经历了从 OA 到一面、二面乃至三面. Author states 我投递的 SDE Intern 岗位, and that this was his first ever application to a company.",
    reported_answer=None,
)
XJ_DOUBT = ("The author states up front that the article will not include 面试的细节 (interview details) or "
            "面试问题的正解, so every problem is named rather than reproduced; the page carries no visible date, "
            "so only the March-to-late-May window he describes is known.")

R.append(dict(XJ_BASE, round="online_assessment", round_name="OA 算法题", platform="HackerRank",
    section_context="我投递的 SDE Intern 岗位 OA 包括三个部分：算法题、基础理论知识题和 Zap-N",
    question_type="coding_algorithms",
    question_text="给到我的是一个 LogServer 背景的数据结构题",
    question_text_en="What I got was a data-structure problem with a LogServer setting.",
    source_quote=XJ_OA,
    doubt=XJ_DOUBT + " He adds only that he believes the intended solution was a balanced tree.",
))
R.append(dict(XJ_BASE, round="online_assessment", round_name="OA 算法题", platform="HackerRank",
    section_context="我投递的 SDE Intern 岗位 OA 包括三个部分：算法题、基础理论知识题和 Zap-N",
    question_type="coding_algorithms",
    question_text="[给到我的是] 一个图论题 ... 图论是拓扑排序",
    question_text_en="[What I got was] a graph-theory problem ... the graph one was topological sorting.",
    source_quote=XJ_OA,
    doubt=XJ_DOUBT + " The problem is identified only by its technique (topological sort).",
))
R.append(dict(XJ_BASE, round="online_assessment", round_name="Zap-N", platform="unknown",
    section_context="OA 三个部分之一",
    question_type="trading_game",
    question_text="Zap-N 是比较有意思的一部分，它由若干个小游戏组成。这些小游戏考察反应力、记忆力、逻辑推理能力，整个玩一遍感觉非常累，但是趣味性还是很足的。",
    question_text_en="Zap-N is the more interesting part; it is made up of a number of mini-games. They test reaction speed, memory and logical reasoning. Playing through the whole thing is exhausting, but it is genuinely fun.",
    source_quote="Zap-N 是比较有意思的一部分，它由若干个小游戏组成。这些小游戏考察反应力、记忆力、逻辑推理能力，整个玩一遍感觉非常累，但是趣味性还是很足的。",
    doubt="Characterises the Zap-N section without naming a single game, so it corroborates the section's existence and purpose but contributes no question content.",
))
R.append(dict(XJ_BASE, round="phone_technical", round_name="一面 (HR 面)", platform="unknown",
    section_context="Optiver 的整个面试流程原则上都是英文交流",
    question_type="behavioral",
    question_text="这一轮是 HR 面，问的都是 BQ",
    question_text_en="This round was the HR round; everything asked was behavioural.",
    source_quote="这一轮是 HR 面，问的都是 BQ，我针对性地做了相关准备。Optiver 的整个面试流程原则上都是英文交流",
    doubt="No behavioural question is quoted, only that the round consisted entirely of them and was conducted in English.",
))
R.append(dict(XJ_BASE, round="phone_technical", round_name="二面 (技术面)", platform="unknown",
    section_context="这一轮开始是技术面，考察 coding 和 system design",
    question_type="coding_algorithms",
    question_text="coding 部分直接给到了 Concurrency Queue，并且平台对该题只有 Python 3 的高亮和补全。",
    question_text_en="The coding part went straight to a Concurrency Queue, and the platform only offered Python 3 highlighting and completion for it.",
    source_quote="coding 部分直接给到了 Concurrency Queue，并且平台对该题只有 Python 3 的高亮和补全。",
    doubt=XJ_DOUBT + " Only the topic name 'Concurrency Queue' is given; whether it had to be lock-free, bounded, or single-producer is inferred from his later remark about spsc.",
))
R.append(dict(XJ_BASE, round="phone_technical", round_name="二面 (技术面) system design", platform="unknown",
    section_context="这一轮开始是技术面，考察 coding 和 system design",
    question_type="coding_algorithms",
    question_text="system design 部分是经典题”Design a ticketing system“。",
    question_text_en="The system design part was the classic question \"Design a ticketing system\".",
    source_quote="system design 部分是经典题”Design a ticketing system“。",
    doubt="The author himself calls it 经典题 (a classic), so it is a standard system-design prompt rather than anything Optiver-specific; no requirements or scale targets are recorded.",
))
R.append(dict(XJ_BASE, round="phone_technical", round_name="三面", platform="unknown",
    section_context="这一面依旧是 coding，注重工程能力的考察",
    question_type="coding_algorithms",
    question_text="让我实现一个多线程应用程序中的某些关键调度逻辑",
    question_text_en="They had me implement some key scheduling logic inside a multithreaded application.",
    source_quote="这一面依旧是 coding，注重工程能力的考察，让我实现一个多线程应用程序中的某些关键调度逻辑。",
    doubt=XJ_DOUBT + " He later reveals the intended answer involved an event queue and using a map key as a search index, but the scenario itself is never stated.",
))

write(R)
