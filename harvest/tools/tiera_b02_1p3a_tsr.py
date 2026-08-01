#!/usr/bin/env python3
"""Batch 2: 1point3acres Optiver/IMC recalls (search snippets) + The Student Room.

1point3acres 403s every direct request from this host and its recall bodies are
points-gated anyway, so every quote below was copied out of a WebSearch "Highlights"
block. Quotes are restricted to a single contiguous run between the search tool's own
"..." elision markers -- stitching across an elision would produce text that exists
nowhere on the page.

Deliberately EXCLUDED from thread-1141422: four polished English probability questions
that appeared as a separate bulleted list in the snippet. One of them
("A biased coin will be continually flipped where there is a 2/3 chance of Heads ...
You start with $10 and your opponent starts with $20") traces to a Feb 2023
math.stackexchange post, and 1point3acres renders an "AI Curated Interview Questions
from Top Companies" widget on these pages, so they are the widget's content rather than
the poster's recall. See the log for the full reasoning.
"""
import sys
sys.path.insert(0, "/workspace/harvest/tools")
from tiera_lib import write

R = []
A_BASE = dict(source_type="1point3acres", access="snippet_only",
              retrieval_method="websearch_snippet", office="unknown")

# ---------------------------------------------------------------------------
# thread-1164459 "Optiver OA" - 2026(1-3月), PhD, 在线笔试, Fail. Three timed sections.
# ---------------------------------------------------------------------------
T1164459 = "https://www.1point3acres.com/bbs/thread-1164459-1-1.html"
T1164459_Q = ("一共三个部分必须按照顺序做：1）Number Logic 25min 2）Beat the Odds 45min 3) Likelihood Test 25min "
              "1) Number Logic里草稿纸上还记得的一些比较confused的题（不保证答案是对的） 1 2 3 16/5 25/8 36/13 ？ 49/21 "
              "2 2 3 4 5 8 8 ？")
T1164459_BASE = dict(A_BASE,
    firm="Optiver", source_url=T1164459, source_language="zh", post_date="2026",
    role_track="unknown", level="unknown", cycle="unknown",
    round="online_assessment", round_name="在线笔试 / Number Logic",
    platform="unknown",
    section_context="一共三个部分必须按照顺序做：1）Number Logic 25min 2）Beat the Odds 45min 3) Likelihood Test 25min",
    source_quote=T1164459_Q,
    poster_context="1point3acres 海外面经 self-tag: 2026(1-3月) 金工类 博士 其他@optiver - 网上海投 - 在线笔试 | 😐 Neutral 😣 Hard | Fail | 其他. Poster warns 不保证答案是对的 and says these are the items he could still remember from his scratch paper.",
    reported_answer=None,
)
R.append(dict(T1164459_BASE, question_type="sequences",
    question_text="1 2 3 16/5 25/8 36/13 ？ 49/21",
    question_text_en="Find the missing term: 1, 2, 3, 16/5, 25/8, 36/13, ?, 49/21",
    doubt="Reconstructed from the poster's scratch paper after the test, and he explicitly disclaims accuracy; the transcription may have dropped or garbled terms, and the whole page is behind a points wall so only the snippet is visible.",
))
R.append(dict(T1164459_BASE, question_type="sequences",
    question_text="2 2 3 4 5 8 8 ？",
    question_text_en="Find the missing term: 2, 2, 3, 4, 5, 8, 8, ?",
    doubt="Same scratch-paper reconstruction caveat; this sequence is short enough that a single mis-remembered term would change the intended rule entirely.",
))

# ---------------------------------------------------------------------------
# thread-1141209 "Optiver 2026 Quantitative Research Intern-OA" - four sections.
# ---------------------------------------------------------------------------
T1141209 = "https://www.1point3acres.com/bbs/thread-1141209-1-1.html"
T1141209_CODE = ("他们家的笔试应该是群发的，刚投递就收到OA了，四个section，强度很大，邮件里面没有说，但是其实是可以分开做的，"
                 "建议一天做一个section。 Coding 首先coding是可以返回的，如果不会的话建议先跳过，90mins, 平台是hackerank，"
                 "可以test代码； 第一题：题目有点记不清楚了，但是不难，核心考点是考m个a和n个b的排列组合有多少个 "
                 "第二题：股票交易，给你一个orders, 是一个2d array, 里面有 [1, 15]; [-1; 30]....1 代表买，-1 代表买，后面是价格；")
T1141209_TAIL = "骰子掷出每个面的平均次数 掷 4 个骰子，乘积是奇数的概率 小游戏 比较放松了，比大小，看区别，轻松做了 哈哈哈做完第二天就拒了，当试试水了，新人求米求米，谢谢！"
T1141209_BASE = dict(A_BASE,
    firm="Optiver", source_url=T1141209, source_language="zh", post_date="2025",
    role_track="quant_researcher", level="internship", cycle="Summer 2026",
    round="online_assessment", round_name="OA",
    section_context="四个section，强度很大 / Coding 90mins, 平台是hackerank",
    poster_context="Thread titled 'Optiver 2026 Quantitative Research Intern-OA'; poster says the OA arrived immediately after applying and that he was rejected the day after finishing it (做完第二天就拒了).",
    reported_answer=None,
)
R.append(dict(T1141209_BASE, question_type="coding_algorithms", platform="HackerRank",
    question_text="第一题：题目有点记不清楚了，但是不难，核心考点是考m个a和n个b的排列组合有多少个",
    question_text_en="Question 1: I do not remember the statement exactly, but it was not hard; the core point was counting how many arrangements there are of m a's and n b's.",
    source_quote=T1141209_CODE,
    doubt="The poster openly says he cannot remember the statement (题目有点记不清楚了) and gives only the underlying counting idea, so the actual prompt is not preserved.",
))
R.append(dict(T1141209_BASE, question_type="coding_algorithms", platform="HackerRank",
    question_text="第二题：股票交易，给你一个orders, 是一个2d array, 里面有 [1, 15]; [-1; 30]....1 代表买，-1 代表买，后面是价格；",
    question_text_en="Question 2: stock trading. You are given orders, a 2d array containing [1, 15]; [-1, 30] ... where 1 means buy and -1 means buy [sic; evidently sell], followed by the price.",
    source_quote=T1141209_CODE,
    doubt="The snippet is cut off by the points wall before the task itself is stated, so only the input format survives; the poster also writes '-1 代表买' where he plainly means sell.",
))
R.append(dict(T1141209_BASE, question_type="expected_value", platform="unknown",
    question_text="骰子掷出每个面的平均次数",
    question_text_en="The average number of throws for a die to show every face.",
    source_quote=T1141209_TAIL,
    doubt="Recorded as a bare topic phrase rather than a full prompt, so the exact framing (coupon-collector expectation vs something else) is inferred rather than attested.",
))
R.append(dict(T1141209_BASE, question_type="probability", platform="unknown",
    question_text="掷 4 个骰子，乘积是奇数的概率",
    question_text_en="Throw 4 dice; what is the probability that the product is odd?",
    source_quote=T1141209_TAIL,
    doubt="One-line paraphrase by the poster rather than the literal question text; it sits immediately after a points-wall marker so its section within the OA is not certain.",
))
R.append(dict(T1141209_BASE, question_type="trading_game", platform="unknown",
    round="online_assessment", round_name="小游戏",
    question_text="小游戏 比较放松了，比大小，看区别，轻松做了",
    question_text_en="Mini-games: quite relaxed - compare which is bigger, spot the difference; did them easily.",
    source_quote=T1141209_TAIL,
    doubt="Describes the game section impressionistically; no actual game rule or scoring is given, so this attests the section exists more than it attests a question.",
))

# ---------------------------------------------------------------------------
# thread-1141422 "26 summer optiver OA" - 硕士 实习, four modules.
# ---------------------------------------------------------------------------
T1141422 = "https://www.1point3acres.com/bbs/thread-1141422-1-1.html"
T1141422_Q = ("新人求米~optiver暑假量化实习，时间很长，一共4 个modulus ​一、找规律 单选题，大部分都很straightforward，"
              "不会立马skip留到最后做，时间充足最后能有个五分钟检查 12,28,36,84,88,168,？ 4/3,1,5,8,23,47,? 3,1,2,6,12,144,? "
              "1/5,2/3,3/11,3/6,5/17,4/9,? 7,14,24,6,12,22,? 19,18,20,60,15,14,16,? 4,2,6,6,30,150,? 1,3,7,17,41,99,? "
              "二、搬房子 用最少的次数从下面变成上面的样子，似乎没有时间限制，想好再动手！！建议先把一楼的房子搞对，再234楼 "
              "三、连连看 从四个选项中找到和example一样的那个，7-8位数字+字母有点类似车牌号，考反应速度，越往后越快 "
              "四、概率 单选题，中规中矩的绿皮书统计题，比如摇色子抛硬币赌钱")
T1141422_BASE = dict(A_BASE,
    firm="Optiver", source_url=T1141422, source_language="zh", post_date="2025",
    role_track="unknown", level="internship", cycle="Summer 2026",
    round="online_assessment", round_name="OA / 一、找规律",
    platform="unknown",
    section_context="一共4 个modulus：一、找规律 二、搬房子 三、连连看 四、概率",
    source_quote=T1141422_Q,
    poster_context="1point3acres self-tag: 2025(7-9月) 金工类 硕士 实习@optiver - 网上海投 - 在线笔试 | 😃 Positive 😐 Average. Poster closes with 都是真题，觉得有帮助麻烦点赞支持下~求米求米求米.",
    reported_answer=None,
    question_text_en=None,
)
for seq in ["12,28,36,84,88,168,？", "4/3,1,5,8,23,47,?", "3,1,2,6,12,144,?",
            "1/5,2/3,3/11,3/6,5/17,4/9,?", "7,14,24,6,12,22,?",
            "19,18,20,60,15,14,16,?", "4,2,6,6,30,150,?", "1,3,7,17,41,99,?"]:
    R.append(dict(T1141422_BASE, question_type="sequences", question_text=seq,
        question_text_en=f"Find the next term: {seq}",
        doubt="Transcribed from memory after the test and listed without answers, so a mis-remembered term cannot be detected; the eight sequences are given as one undifferentiated block so their order and the multiple-choice options are lost.",
    ))
R.append(dict(T1141422_BASE, question_type="logic_brainteaser",
    round_name="OA / 二、搬房子",
    question_text="二、搬房子 用最少的次数从下面变成上面的样子，似乎没有时间限制，想好再动手！！建议先把一楼的房子搞对，再234楼",
    question_text_en="Module 2, 'moving houses': turn the bottom configuration into the top one in the fewest moves. There seems to be no time limit - think before you act. Advice: get the first-floor houses right first, then floors 2, 3, 4.",
    doubt="The puzzle is visual and the poster describes it only in words, so the actual board configuration - which is the entire question - is not recoverable from this text.",
))
R.append(dict(T1141422_BASE, question_type="other",
    round_name="OA / 三、连连看",
    question_text="三、连连看 从四个选项中找到和example一样的那个，7-8位数字+字母有点类似车牌号，考反应速度，越往后越快",
    question_text_en="Module 3, 'matching': from four options find the one identical to the example. Strings of 7-8 digits plus letters, a bit like a licence plate. Tests reaction speed, and it gets faster as you go.",
    doubt="Describes the format of a speeded perceptual-matching task rather than reproducing an item; no actual string pair is given.",
))
R.append(dict(T1141422_BASE, question_type="probability",
    round_name="OA / 四、概率",
    question_text="四、概率 单选题，中规中矩的绿皮书统计题，比如摇色子抛硬币赌钱",
    question_text_en="Module 4, probability: multiple choice, run-of-the-mill Green Book statistics questions, e.g. rolling dice, flipping coins, betting money.",
    doubt="The poster characterises the section by reference to the Green Book (Xinfeng Zhou) instead of reproducing any item, so this is an overlap claim with a textbook rather than an actual question.",
))

# ---------------------------------------------------------------------------
# IMC on 1point3acres.
# ---------------------------------------------------------------------------
T1155726 = "https://www.1point3acres.com/bbs/thread-1155726-1-1.html"
T1155726_Q = ("本帖最后由 Adam16 于 2025-11-23 21:20 编辑 两道题： 第一题：Waste reduction 一个制药公司的业务场景。"
              "公司为不同病人准备液体药剂，而病人需求量不一致。药剂需要装在容器里，每个“容器集合（container set）”提供不同容量的瓶子。 "
              "给定：多个病人的需求量 requirements；若干个容器集合，每个集合包含若干种容")
T1155726_BASE = dict(A_BASE,
    firm="IMC Trading", source_url=T1155726, source_language="zh", post_date="2025-11-23",
    role_track="quant_developer", level="unknown", cycle="unknown",
    round="online_assessment", round_name="Online Assessment",
    platform="unknown", section_context="两道题",
    poster_context="Thread titled 'IMC 2025/2026 Grad & Intern Software Engineer Online Assessment', edited by user Adam16 on 2025-11-23; a replying user writes OA全对，但等了两个月了，啥消息没有.",
    reported_answer=None,
)
R.append(dict(T1155726_BASE, question_type="coding_algorithms",
    question_text=("第一题：Waste reduction 一个制药公司的业务场景。公司为不同病人准备液体药剂，而病人需求量不一致。"
                   "药剂需要装在容器里，每个“容器集合（container set）”提供不同容量的瓶子。 "
                   "给定：多个病人的需求量 requirements；若干个容器集合，每个集合包含若干种容[量]"),
    question_text_en=("Question 1: 'Waste reduction'. A pharmaceutical-company scenario. The company prepares liquid "
                      "medicine for different patients whose required volumes differ. The medicine must be put in "
                      "containers, and each 'container set' offers bottles of different capacities. Given: the "
                      "requirements of several patients, and several container sets each containing several bottle "
                      "capacities ..."),
    source_quote=T1155726_Q,
    doubt="The snippet is truncated mid-word by the 188-point paywall, so the objective (presumably minimise wasted volume) is cut off; the thread title covers both Grad and Intern so the level cannot be pinned down.",
))
R.append(dict(T1155726_BASE, question_type="coding_algorithms",
    question_text="按照同样的规则往下传播。指令一直传播，直到所有子树节点都收到。 找出所有下属传播过程中，第 k 个收到指令的人是谁",
    question_text_en="[An instruction] propagates downwards following the same rule. The instruction keeps propagating until every node of the subtree has received it. Find who the k-th person to receive the instruction is, across the whole propagation to subordinates.",
    source_quote="按照同样的规则往下传播。指令一直传播，直到所有子树节点都收到。 找出所有下属传播过程中，第 k 个收到指令的人是谁",
    doubt="Only the tail of the second question survives the paywall - the setup that defines the propagation rule and the tree input is hidden, so the prompt is incomplete.",
))

T1144831 = "https://www.1point3acres.com/bbs/thread-1144831-1-1.html"
R.append(dict(A_BASE,
    firm="IMC Trading", source_url=T1144831, source_language="zh", post_date="2025",
    role_track="unknown", level="internship", cycle="Summer 2026",
    round="online_assessment", round_name="oa", platform="HackerRank",
    section_context="120 min 要求写2道题",
    question_type="coding_algorithms",
    question_text="120 min 要求写2道题,在hackerrank上写",
    question_text_en="120 min, required to write 2 problems, written on HackerRank.",
    reported_answer=None,
    source_quote="120 min 要求写2道题,在hackerrank上写",
    poster_context="Thread titled 'IMC 2026 summer intern oa', filed under 1point3acres' 数科面经 (data science) board; 回复: 0.",
    doubt="Everything past the format line is behind a 200-point wall, so no question content is attested at all - this record fixes the round format only. The 数科 board tag hints at a data role but the title does not say, so role_track is left unknown.",
))

T1156476 = "https://www.1point3acres.com/bbs/thread-1156476-1-1.html"
R.append(dict(A_BASE,
    firm="IMC Trading", source_url=T1156476, source_language="zh", post_date="2025-12-02",
    role_track="quant_trader", level="new_grad", cycle="unknown",
    round="phone_technical", round_name="technical interview / 视频面试",
    platform="unknown", section_context="跟hr做technical interview",
    question_type="logic_brainteaser",
    question_text="brain teaser：很简单绿宝书题目，秒。",
    question_text_en="Brain teaser: a very easy Green Book problem, answered instantly.",
    reported_answer=None,
    source_quote="brain teaser：很简单绿宝书题目，秒。",
    poster_context="Anonymous poster 匿名用户-A5TEP, 2025-12-2 03:35:38, self-tagged 2025(10-12月) 金工类 硕士 全职@imc - 网上海投 - 视频面试 | 😃 Positive 😐 Average | Fail | 在职跳槽. Thread title: 'IMC graduate trader technical interview'.",
    doubt="Names no actual question, only that it came from the Green Book - so this is a textbook-overlap claim, not a recovered prompt. The level label also conflicts internally: the title says 'graduate trader' but the poster tags himself 在职跳槽 (moving jobs while employed).",
))

T934179 = "https://www.1point3acres.com/bbs/thread-934179-1-1.html"
T934179_BASE = dict(A_BASE,
    firm="IMC Trading", source_url=T934179, source_language="zh", post_date="2022",
    role_track="quant_trader", level="internship", cycle="unknown",
    platform="unknown",
    poster_context="Self-tagged 2022(7-9月) 金工类 本科 实习@imc - 内推 - 在线笔试 | 😃 Positive 😐 Average | Pass | 应届毕业生; poster states 申请的是Quant Trader Intern.",
    reported_answer=None,
)
R.append(dict(T934179_BASE,
    round="online_assessment", round_name="OA", section_context="两轮网考都没有deadline",
    question_type="other",
    question_text="上周刚做的OA，申请的是Quant Trader Intern。做完OA第二天就收到了下一轮HireVue的email。两轮网考都没有deadline，所以一直在拖...",
    question_text_en="Did the OA last week; I applied for Quant Trader Intern. The day after finishing the OA I got the email for the next round, HireVue. Neither of the two online tests had a deadline, so I kept putting it off...",
    source_quote="新人求大米，加米不会减自己的大米哦。上周刚做的OA，申请的是Quant Trader Intern。做完OA第二天就收到了下一轮HireVue的email。两轮网考都没有deadline，所以一直在拖...",
    doubt="Attests the pipeline (OA then HireVue) for a Quant Trader Intern but reproduces no question; the OA content itself is behind the points wall.",
))
R.append(dict(T934179_BASE,
    round="online_assessment", round_name="HireVue",
    section_context="1-2min之内做一道题然后录个视频讲你的答案",
    question_type="behavioral",
    question_text="behavioral technical 都有 没几道题 前面问why trading 还有几个常见的behavioral technical就是1-2min之内做一道题然后录个视频讲你的答案",
    question_text_en="It has both behavioural and technical - not many questions. It opens with why trading, then a few common behavioural ones; the technical part is: solve a problem within 1-2 minutes, then record a video explaining your answer.",
    source_quote="behavioral technical 都有 没几道题 前面问why trading 还有几个常见的behavioral technical就是1-2min之内做一道题然后录个视频讲你的答案",
    doubt="A reply describing the HireVue round in general terms; the only verbatim question preserved is 'why trading', and the technical items are not named.",
))

# ---------------------------------------------------------------------------
# 1point3acres company tag listing for IMC. These are ~200-char ungated thread
# previews on a PAGINATED tag page, so the URL's contents will drift over time.
# ---------------------------------------------------------------------------
IMCTAG = "https://www.1point3acres.com/bbs/tag/imc-2057-3.html"
IMCTAG_BASE = dict(A_BASE,
    firm="IMC Trading", source_url=IMCTAG, source_language="zh",
    platform="unknown", cycle="unknown", office="unknown",
)
R.append(dict(IMCTAG_BASE,
    role_track="quant_trader", level="unknown", post_date="2024-09-26",
    round="unknown", round_name="Brain teaser", section_context=None,
    question_type="betting_odds_arbitrage",
    question_text="Brain teaser: It was like a coinflip and if u win u get $1, if u lose u lose $1, u have a slight edge int this game, would u play it",
    question_text_en=None,
    reported_answer="obv if u have a slight edg[e]",
    source_quote="Brain teaser: It was like a coinflip and if u win u get $1, if u lose u lose $1, u have a slight edge int this game, would u play it",
    poster_context="Thread preview on the 1point3acres IMC company tag page, attributed to user brawler1232, 2024-9-26 09:29, filed under 海外面经.",
    doubt="Read from a truncated tag-page preview, not the thread itself; the tag page is paginated and re-orders as new threads arrive, so this exact preview may not persist at this URL.",
))
R.append(dict(IMCTAG_BASE,
    role_track="unknown", level="unknown", post_date="2025-10-08",
    round="phone_technical", round_name="hr 之后的第一关",
    section_context="发邮件说是一个小时结果面了1个半小时，前一个小时是brain teaser后面半小时coding",
    question_type="logic_brainteaser",
    question_text="brain teaser 的set up 是三个城市，先是给了一个格图，从上角走到",
    question_text_en="The brain teaser's setup was three cities; first they gave a grid diagram, walking from the top corner to ...",
    reported_answer=None,
    source_quote="hr 之后的第一关，发邮件说是一个小时结果面了1个半小时，前一个小时是brain teaser后面半小时coding。brain teaser 的set up 是三个城市，先是给了一个格图，从上角走到",
    poster_context="Thread preview on the IMC tag page, 地里匿名用户, 2025-10-8 12:41, 8 replies / 3275 views, 海外面经.",
    doubt="The preview truncates exactly where the question is being stated, so the actual task is unknown; tag-page previews also rotate off this URL as newer threads are posted.",
))
R.append(dict(IMCTAG_BASE,
    role_track="quant_developer", level="unknown", post_date="2023-12-22",
    round="online_assessment", round_name="OA", section_context="OA 总共120分钟两道题",
    question_type="coding_algorithms",
    question_text="OA 总共120分钟两道题。第一题是LC1381，increment必须是O(1) Time Complexity (必须用到一个extra stack)第二题是minimum moves of Knight without bishop 。国象的",
    question_text_en="The OA was 120 minutes, two questions. Q1 was LeetCode 1381, where increment must be O(1) time complexity (you must use an extra stack). Q2 was minimum moves of a knight without a bishop - chess.",
    reported_answer=None,
    source_quote="OA 总共120分钟两道题。第一题是LC1381，increment必须是O(1) Time Complexity (必须用到一个extra stack)第二题是minimum moves of Knight without bishop 。国象的",
    poster_context="Thread preview on the IMC tag page, 地里匿名用户, 2023-12-22 21:40, 海外面经.",
    doubt="Truncated tag-page preview; the second problem's constraints are cut off, and the poster identifies Q1 only by its LeetCode number rather than by the prompt IMC actually used.",
))
R.append(dict(IMCTAG_BASE,
    role_track="quant_developer", level="unknown", post_date="2024-11-07",
    round="online_assessment", round_name="OA", section_context="两题120分钟",
    question_type="coding_algorithms",
    question_text="两题120分钟，地里原题第一题：prefix sum matrix, binary searchprefix sum matrix参考莉蔻1292第二题：BFS找minimum cost不光记录坐标还记录当前的cost",
    question_text_en="Two questions, 120 minutes, both already posted here. Q1: prefix sum matrix, binary search - see LeetCode 1292. Q2: BFS to find minimum cost, recording not only the coordinates but also the current cost.",
    reported_answer=None,
    source_quote="两题120分钟，地里原题第一题：prefix sum matrix, binary searchprefix sum matrix参考莉蔻1292第二题：BFS找minimum cost不光记录坐标还记录当前的cost",
    poster_context="Thread preview on the IMC tag page, 地里匿名用户, 2024-11-7 21:05, 5 replies / 2659 views.",
    doubt="Describes the solution techniques rather than the problem statements, and identifies Q1 by a LeetCode number (莉蔻1292); read from a rotating tag-page preview.",
))
R.append(dict(IMCTAG_BASE,
    role_track="unknown", level="unknown", post_date="2025-09-23",
    round="unknown", round_name="一共6题", section_context="没遇到太多地里的原题，一共6题",
    question_type="behavioral",
    question_text="explain your favorite project to a non-technical person and describe why you enjoy it",
    question_text_en=None,
    reported_answer=None,
    source_quote="没遇到太多地里的原题，一共6题，不太记得全部题了。[*]explain your favorite project to a non-technical person and describe why you enjoy it[*]what is the worst c",
    poster_context="Thread preview on the IMC tag page, user Neylsus, 2025-9-23 21:52, 5 replies / 1075 views.",
    doubt="The poster says he cannot remember all six questions, and the preview cuts off in the middle of the second one; the round is never named.",
))

# ---------------------------------------------------------------------------
# The Student Room: Jane Street Strategy and Product HackerRank OA.
# ---------------------------------------------------------------------------
TSR = "https://www.thestudentroom.co.uk/showthread.php?t=7527519"
TSR_BASE = dict(
    firm="Jane Street", source_url=TSR, source_type="university_bbs",
    source_language="en", access="full_text", retrieval_method="webfetch",
    office="unknown", cycle="unknown", role_track="unknown", level="unknown",
    round="online_assessment", round_name="hackerrank for jane street strategy and product",
    platform="HackerRank", post_date="unknown", reported_answer=None,
    question_text_en=None,
)
R.append(dict(TSR_BASE,
    section_context="Jane Street Strategy and Product role",
    question_type="other",
    question_text="It mainly consists of math questions, usually involving reading charts to answer questions, or filling in numbers and multiple-choice options.",
    source_quote="It mainly consists of math questions, usually involving reading charts to answer questions, or filling in numbers and multiple-choice options.",
    poster_context="Reply in a thread started by Abigail2.0 ('I passed my hackerrank for jane street strategy and product'); this answer is given to the direct question 'Would you be willing to chat about how the OA went?'. The Student Room shows only relative timestamps ('10 months ago' as of retrieval on 2026-08-01), so no absolute post date is recoverable.",
    doubt="Characterises the OA rather than reproducing a question, and the replier is not clearly identified as having sat it themselves rather than relaying what they were told.",
))
R.append(dict(TSR_BASE,
    section_context="pre-OA material supplied by the firm",
    question_type="market_making",
    question_text="they have provided a 1 page pdf of order market basics ... are the questions related to that",
    source_quote="Also, they have provided a 1 page pdf of order market basics ... are the questions related to that.",
    poster_context="User SchetV, who says 'Hi i got the OA for the same role and would like to know how i can prepare for the OA.'",
    doubt="This is a candidate asking a question, not reporting one; it only establishes that Jane Street sends a one-page order-market primer before this OA. The ellipsis is present in the original post text, not inserted by me.",
))

write(R)
