#!/usr/bin/env python3
"""Batch 4: Jane Street trader-intern recalls on 1point3acres, Blind threads, Reddit
comments, and one openquant Q&A.

Reddit note: reddit.com 403s every direct request from this host, so the comment bodies
were read in full from the Arctic Shift archive mirror
(arctic-shift.photon-reddit.com), which serves the author-written body verbatim. The
canonical reddit permalink is recorded as source_url because that is where a human
should go to check it; a verifier hitting reddit.com directly will be blocked rather
than contradicted.
"""
import sys
sys.path.insert(0, "/workspace/harvest/tools")
from tiera_lib import write

R = []

# ===========================================================================
# 1point3acres thread-829095: "Jane Street Quantitative Trader Intern面经"
# ===========================================================================
T829095 = "https://www.1point3acres.com/bbs/thread-829095-1-1.html"
T829095_R1 = ("正在面试Jane Street Quantitative Trader Intern Timeline: 10.23 海投 10.28 收到邮件约电面 "
              "11.4 第一轮电面 11.11 约第二轮电面 11.16 第二轮电面 11.17 约第三轮电面 12.7 第三轮电面 12.10 约final round "
              "面试问题： 第一轮： 1. 一个数所有数位乘积10000， 这个数最小是多少（255558），最大是多少（无穷大） "
              "2. 周六有20%几率下雨，周日有30%，如果相互独立至少一天下雨几率是多少（44%），如果周六下雨使周日更有可能下雨，"
              "这个几率会上升还是下降，如果不知道是否相互独立，至少一天下雨")
T829095_BID = ("ional的对手玩，但可以告诉对手你有关你的bid的information（must be true），请问你说什么能提升你的预期收益 "
               "(7) 你和一个绝对rational的对手玩，他知道前10次扔硬币的结果，你应该出价多少 12月底要final round了orz")
T829095_BASE = dict(
    firm="Jane Street", source_url=T829095, source_type="1point3acres",
    source_language="zh", access="snippet_only", retrieval_method="websearch_snippet",
    office="unknown", cycle="unknown", platform="unknown",
    role_track="quant_trader", level="internship", post_date="2021-12",
    poster_context="Thread titled 'Jane Street Quantitative Trader Intern面经[持续更新][求加米]'; poster is mid-process (正在面试) and gives a full timeline from 10.23 海投 to 12.10 约final round. A reply in the thread is dated 2021-12-15.",
)
R.append(dict(T829095_BASE, round="phone_technical", round_name="第一轮电面",
    section_context="第一轮", question_type="combinatorics",
    question_text="一个数所有数位乘积10000， 这个数最小是多少（255558），最大是多少（无穷大）",
    question_text_en="A number whose digits multiply to 10000: what is the smallest such number (255558), and the largest (infinite)?",
    reported_answer="最小 255558，最大 无穷大",
    source_quote=T829095_R1,
    doubt="Transcribed by the candidate mid-process rather than from a recording; the parenthesised answers are his own and the 'largest is infinite' reading depends on an unstated convention about leading or trailing 1s.",
))
R.append(dict(T829095_BASE, round="phone_technical", round_name="第一轮电面",
    section_context="第一轮", question_type="probability",
    question_text="周六有20%几率下雨，周日有30%，如果相互独立至少一天下雨几率是多少（44%），如果周六下雨使周日更有可能下雨，这个几率会上升还是下降，如果不知道是否相互独立，至少一天下雨",
    question_text_en="There is a 20% chance of rain on Saturday and 30% on Sunday. If they are independent, what is the probability it rains on at least one day (44%)? If rain on Saturday makes rain on Sunday more likely, does that probability go up or down? And if you do not know whether they are independent, [what can you say about] rain on at least one day?",
    reported_answer="44%",
    source_quote=T829095_R1,
    doubt="The final clause is cut off by 1point3acres' points wall mid-sentence, so the third sub-question (the bounds under unknown dependence) is incomplete.",
))
R.append(dict(T829095_BASE, round="phone_technical", round_name="面试问题 (round not separable in the visible snippet)",
    section_context=None, question_type="betting_odds_arbitrage",
    question_text="你和一个绝对rational的对手玩，但可以告诉对手你有关你的bid的information（must be true），请问你说什么能提升你的预期收益",
    question_text_en="You play against a perfectly rational opponent, but you may tell the opponent some information about your bid (it must be true). What can you say that raises your expected payoff?",
    reported_answer="告诉那个对手自己会从0～100随机bid",
    source_quote=T829095_BID,
    doubt="The visible snippet begins mid-word ('ional的对手玩' = rational), so the setup of the bidding game itself is behind the paywall and this question is missing its premise; the round it belongs to cannot be determined.",
))
R.append(dict(T829095_BASE, round="phone_technical", round_name="面试问题 (round not separable in the visible snippet)",
    section_context=None, question_type="poker_game_theory",
    question_text="(7) 你和一个绝对rational的对手玩，他知道前10次扔硬币的结果，你应该出价多少",
    question_text_en="(7) You play against a perfectly rational opponent who knows the results of the first 10 coin tosses. How much should you bid?",
    reported_answer=None,
    source_quote=T829095_BID,
    doubt="Numbered (7) in a list whose items (1)-(6) are hidden by the paywall, so the shared game setup - what is being bid on and what the payoff is - is not visible.",
))
R.append(dict(T829095_BASE, round="phone_technical", round_name="面试问题 (bidding game, answers discussed in replies)",
    section_context=None, question_type="betting_odds_arbitrage",
    question_text="[bidding game where the opponent bids uniformly on 0-87] 那我是对面就直接出88吧",
    question_text_en="[On the bidding game] So as the other side I would just bid 88? If the opponent bids 88 his expected payoff is 100 - 88 = 12. If he bids 51 his expected payoff is 50/87 * (100 - 51) = 28 > 12; 50/87 is the probability that a uniform draw on 0-87 lands below 51.",
    reported_answer="如果对方出88，他的期望收益是 100 - 88 = 12. 如果对方出51，他的期望收益是 50/87 * (100 - 51) = 28 > 12.",
    source_quote="0-87那我是对面就直接出88吧 如果对方出88，他的期望收益是 100 - 88 = 12. 如果对方出51，他的期望收益是 50/87 * (100 - 51) = 28 > 12. 50/87 是0-87随机到了一个小于51的数的概率",
    doubt="This is a reader (yz9, 2021-12-15) working through the problem in a reply, not the interviewer's prompt; the original question is behind the points wall, so the setup is reconstructed from the discussion.",
))

# ===========================================================================
# 1point3acres thread-1016826: "Jane Street Quant Trader Intern HK onsite挂经"
# ===========================================================================
T1016826 = "https://www.1point3acres.com/bbs/thread-1016826-1-1.html"
T1016826_INTRO = ("刚来地里，记一个自己19年面试JS quant trader HK office 实习的经验，希望能给自己攒攒米。"
                  "当时是在学校宣讲会上看到的JS，回去之后就投了HK office，投完大概过了几天就收到了面试安排，"
                  "一共是三个电面 + onsite 四轮，不问简历不问自我介绍上来直接了当就是做题，问的都是概率题，"
                  "认认真真刷完绿皮书应该基本可以进onsite，但onsite因为轮次多压力大，题目变化也多，加上楼主没有任何quant经验，"
                  "加上当时很紧张，所以不出意外地挂了T_T")
T1016826_BASE = dict(
    firm="Jane Street", source_url=T1016826, source_type="1point3acres",
    source_language="zh", access="snippet_only", retrieval_method="websearch_snippet",
    office="Hong Kong", cycle="unknown", platform="unknown",
    role_track="quant_trader", level="internship", post_date="2023",
    poster_context="Poster recalls interviewing for the Jane Street Hong Kong office quant trader internship in 2019 (19年), writing it up years later; clarifying replies in the thread are dated 2023-10-19. He says he was rejected.",
)
R.append(dict(T1016826_BASE, round="onsite", round_name="三个电面 + onsite 四轮",
    section_context="一共是三个电面 + onsite 四轮", question_type="probability",
    question_text="不问简历不问自我介绍上来直接了当就是做题，问的都是概率题，认认真真刷完绿皮书应该基本可以进onsite",
    question_text_en="No resume questions, no self-introduction - straight into problems. Everything asked was probability. If you work carefully through the Green Book you can basically get to the onsite.",
    reported_answer=None,
    source_quote=T1016826_INTRO,
    doubt="A characterisation of the rounds, not a question, and it explicitly points at the Green Book (Xinfeng Zhou) as the source of the material rather than reproducing anything.",
))
R.append(dict(T1016826_BASE, round="onsite", round_name="onsite第三题",
    section_context="onsite", question_type="expected_value",
    question_text="是一副52张扑克牌中任意拿的25张，任意抽完之后可以全部翻开看到是多少，然后把这25张组合成5组，要求最大化好牌的组数，并且算组数的期望",
    question_text_en="You take any 25 cards from a 52-card deck; after drawing you may turn them all face up and see what they are. You then combine those 25 into 5 groups, maximising the number of groups that are 'good hands', and compute the expected number of such groups.",
    reported_answer=None,
    source_quote="是一副52张扑克牌中任意拿的25张，任意抽完之后可以全部翻开看到是多少，然后把这25张组合成5组，要求最大化好牌的组数，并且算组数的期望",
    doubt="This restatement is the poster answering a reader's clarifying question years after the fact, and a further reply shows other readers still could not agree on what 好牌 (a good hand) or 'maximise' meant, so the prompt remains ambiguous.",
))

# ===========================================================================
# 1point3acres thread-818997: "简街Trader Intern 挂经 求米"
# ===========================================================================
T818997 = "https://www.1point3acres.com/bbs/thread-818997-1-1.html"
T818997_R1 = ("三轮店面，最后跪. 1point 3acres 一轮主要是简单的概率问题 分解数字问乘积最大怎么分解 "
              "投四个硬币问期望，如果加上可以翻转硬币的权力，期望怎么变，翻到指定结果的期望数量是多少 "
              "一个箱子里有三个红球两个蓝球，抽到红")
T818997_BASE = dict(
    firm="Jane Street", source_url=T818997, source_type="1point3acres",
    source_language="zh", access="snippet_only", retrieval_method="websearch_snippet",
    office="unknown", cycle="unknown", platform="unknown",
    role_track="quant_trader", level="internship", post_date="unknown",
    round="phone_technical", round_name="三轮店面 [电面]",
    poster_context="Thread titled '简街Trader Intern 挂经 求米' on 1point3acres' 数科面经 board; poster says 三轮店面，最后跪 (three phone rounds, failed at the end) and numbers the rounds 一/二/三.",
)
R.append(dict(T818997_BASE, section_context="一轮主要是简单的概率问题",
    question_type="combinatorics",
    question_text="分解数字问乘积最大怎么分解",
    question_text_en="Decompose a number - how do you split it so that the product is largest?",
    reported_answer=None,
    source_quote=T818997_R1,
    doubt="Compressed to a single clause with the number itself omitted, so the actual instance is unrecoverable; a replier even asks whether it is the same as another thread's question, and the poster does not confirm.",
))
R.append(dict(T818997_BASE, section_context="一轮主要是简单的概率问题",
    question_type="expected_value",
    question_text="投四个硬币问期望，如果加上可以翻转硬币的权力，期望怎么变，翻到指定结果的期望数量是多少",
    question_text_en="Toss four coins and give the expectation; then, if you are given the power to flip coins over, how does the expectation change, and what is the expected number [of flips] to reach a specified outcome?",
    reported_answer=None,
    source_quote=T818997_R1,
    doubt="The payoff function is never stated - 'the expectation' of what is left implicit - so the question can only be reconstructed approximately.",
))
R.append(dict(T818997_BASE, section_context="一轮主要是简单的概率问题",
    question_type="expected_value",
    question_text="一个箱子里有三个红球两个蓝球，抽到红[球] ... [follow-]up是考虑有n+1个红球，n个蓝球的情况",
    question_text_en="A box contains three red balls and two blue balls; drawing a red ... The follow-up considers the case of n+1 red balls and n blue balls.",
    reported_answer="最佳策略：直到收集到3个红球才停止。",
    source_quote=T818997_R1,
    doubt="The snippet truncates at 抽到红, so the stopping-rule question itself is cut off; the answer quoted here comes from a replier summarising, not from the interviewer.",
))
R.append(dict(T818997_BASE, section_context="三",
    question_type="market_making",
    question_text="知道自己的骰子点数，之后两人竞标一个装有两人点数和金额的箱子，求在无限进行游戏和有限进行游戏下的最优策略",
    question_text_en="You know your own die roll; then the two of you bid for a box containing an amount of money equal to the sum of both players' rolls. Find the optimal strategy both when the game is played infinitely and when it is played a finite number of times.",
    reported_answer=None,
    source_quote="知道自己的骰子点数，之后两人竞标一个装有两人点数和金额的箱子，求在无限进行游戏和有限进行游戏下的最优策略",
    doubt="A replier says outright he does not understand what 有限/无限进行游戏 means here and offers two incompatible readings, so the mechanics of the auction are genuinely unclear from the text.",
))
R.append(dict(T818997_BASE, section_context="二",
    question_type="logic_brainteaser",
    question_text="箱子里的球是等量无穷多，因此比例总是1:1，求各个箱子里分别是什么球 ... 每个箱子恰少其中一种",
    question_text_en="The balls in the boxes are infinite and in equal quantity so the ratio is always 1:1; work out what balls are in each box ... each box is missing exactly one of the kinds.",
    reported_answer=None,
    source_quote="箱子里的球是等量无穷多，因此比例总是1:1，求各个箱子里分别是什么球",
    doubt="Assembled from the poster's clarification to a reader rather than from the original statement; how many boxes and colours there are is never made explicit in the visible text.",
))

# ===========================================================================
# Blind.
# ===========================================================================
BL_TRANS = "https://www.teamblind.com/post/transitioning-from-tech-to-trading-firms-rc7dtjvv"
BL_TRANS_Q = ("For one, they don't don't care about system design the way big tech does. Jane Street asks you to build "
              "full working systems from scratch in 45 minutes. Things like an arbitrage system, a real-time order "
              "book stream comparator, a ring buffer, or a text editor backend. They keep adding follow-ups. Citadel "
              "and HRT lean heavier into C++ fundamentals, concurrency, memory models, and probability.")
BL_TRANS_DOUBT = ("Posted by an account flaired 'Salesforce' who has not said he interviewed anywhere; the comment "
                  "ends by plugging a paid question-leak site, another user replies 'Chatgpt ahh comment into an "
                  "undisclosed ad', and Blind shows 'Flagged by the community' on this thread - so this may be "
                  "vendor astroturf rather than a real recall.")
R.append(dict(
    firm="Jane Street", source_url=BL_TRANS, source_type="blind", source_language="en",
    access="full_text", retrieval_method="webfetch", post_date="2026-07-04",
    office="unknown", cycle="unknown", platform="unknown",
    role_track="quant_developer", level="experienced",
    round="unknown", round_name="interview process (round not specified)",
    section_context="45 minutes per system",
    question_type="coding_algorithms",
    question_text="Jane Street asks you to build full working systems from scratch in 45 minutes. Things like an arbitrage system, a real-time order book stream comparator, a ring buffer, or a text editor backend. They keep adding follow-ups.",
    question_text_en=None, reported_answer=None,
    source_quote=BL_TRANS_Q,
    poster_context="Reply by user 'Leyaou' (company flair Salesforce) to a thread asking about moving from Big Tech to trading firms as a software engineer.",
    doubt=BL_TRANS_DOUBT,
))
R.append(dict(
    firm="Citadel", source_url=BL_TRANS, source_type="blind", source_language="en",
    access="full_text", retrieval_method="webfetch", post_date="2026-07-04",
    office="unknown", cycle="unknown", platform="unknown",
    role_track="quant_developer", level="experienced",
    round="unknown", round_name="interview process (round not specified)",
    section_context=None,
    question_type="coding_algorithms",
    question_text="Citadel and HRT lean heavier into C++ fundamentals, concurrency, memory models, and probability. ... You will most likely get questions on lock-free data structures, cache behavior, and low-level systems stuff that big tech interviews never touch.",
    question_text_en=None, reported_answer=None,
    source_quote=BL_TRANS_Q,
    poster_context="Reply by user 'Leyaou' (company flair Salesforce) to a thread asking about moving from Big Tech to trading firms as a software engineer.",
    doubt=BL_TRANS_DOUBT + " It also lumps Citadel together with HRT, so nothing here is specifically attributable to Citadel.",
))

BL_JSQ = "https://www.teamblind.com/post/quant-interviews-at-jane-street-fsroxvol"
R.append(dict(
    firm="Jane Street", source_url=BL_JSQ, source_type="blind", source_language="en",
    access="full_text", retrieval_method="webfetch", post_date="2026-06-14",
    office="unknown", cycle="unknown", platform="unknown",
    role_track="quant_researcher", level="unknown",
    round="unknown", round_name="quant researcher interview process",
    section_context=None, question_type="probability",
    question_text="similar to trader roles. lots of probability questions, need to answer perfectly and give confidence intervals on anything you estimate.",
    question_text_en=None, reported_answer=None,
    source_quote="similar to trader roles. lots of probability questions, need to answer perfectly and give confidence intervals on anything you estimate.",
    poster_context="Blind user flaired 'ex-AT&T oeGp70', Jun 14, answering a thread that asks 'what is the interview process like for quant researcher roles for prob stats?'.",
    doubt="Two sentences of second-hand-sounding advice; the poster never claims to have interviewed at Jane Street himself and names no question.",
))

BL_CIT = "https://www.teamblind.com/post/interview-prep-guidance-for-citadel-market-structure-research-uxomsahq"
BL_CIT_BASE = dict(
    firm="Citadel", source_url=BL_CIT, source_type="blind", source_language="en",
    access="full_text", retrieval_method="webfetch",
    office="unknown", cycle="unknown", platform="unknown",
    role_track="quant_researcher", level="experienced", question_text_en=None,
    reported_answer=None,
)
R.append(dict(BL_CIT_BASE, post_date="2024-10-09", office="London",
    round="phone_technical", round_name="first round",
    section_context="40 minutes", question_type="coding_algorithms",
    question_text="I got 2 lc hard for 40min in London. Didn't make it further, I think it is much harder than faang",
    source_quote="I got 2 lc hard for 40min in London. Didn’t make it further, I think it is much harder than faang",
    poster_context="Blind user flaired 'Microsoft hdbd rjz', Oct 9 2024, replying to a candidate scheduled for a Citadel market structure research first round.",
    doubt="Says only that the round was two LeetCode-hard problems in 40 minutes without naming either; it is also unclear whether he interviewed for the same market-structure-research team the thread is about.",
))
R.append(dict(BL_CIT_BASE, post_date="2024-10-27",
    round="onsite", round_name="all six loops",
    section_context="six loops", question_type="coding_algorithms",
    question_text="I completed all six loops. They were enjoyable and covered various topics, from LC hard to runtime optimization to opinions about X versus Y. Understanding Linux memory management, CPU caching, and networking at a graduate level was critical. The rounds also get more challenging.",
    source_quote="I completed all six loops. They were enjoyable and covered various topics, from LC hard to runtime optimization to opinions about X versus Y. Understanding Linux memory management, CPU caching, and networking at a graduate level was critical.",
    poster_context="Blind user flaired 'Amazon L7sa', Oct 27 2024, in the Citadel market structure research prep thread.",
    doubt="Summarises six rounds in three sentences with no question reproduced, and does not state which Citadel team or role the loops were for.",
))

# ===========================================================================
# Reddit (bodies read in full from the Arctic Shift archive mirror).
# ===========================================================================
RD_BASE = dict(source_type="reddit_thread", source_language="en",
               access="full_text", retrieval_method="webfetch",
               office="unknown", cycle="unknown", platform="unknown",
               question_text_en=None, reported_answer=None)
RD_NOTE = (" reddit.com blocks direct requests from this host, so the comment body was read verbatim from the "
           "Arctic Shift archive mirror of Reddit rather than from reddit.com itself.")

R.append(dict(RD_BASE,
    firm="IMC Trading",
    source_url="https://www.reddit.com/r/FinancialCareers/comments/lunjav/imc_trading_intern_video_interview/gp7lewr/",
    post_date="2021-02-28", role_track="quant_trader", level="internship",
    round="unknown", round_name="video interview (thread title: IMC Trading Intern Video Interview)",
    section_context=None, question_type="poker_game_theory",
    question_text="I was asked about an extended example. The example had something to do with two players, betting, and cards. I was asked to consider \"winning strategies\" for person 1 / person 2, so I guess a bit of game theory. It was more intuitive than mental math.",
    source_quote="My experience a few years ago was that I was asked about an extended example. The example had something to do with two players, betting, and cards. I was asked to consider \"winning strategies\" for person 1 / person 2, so I guess a bit of game theory. It was more intuitive than mental math.",
    poster_context="u/darnforgotmypassword commenting on the thread 'IMC Trading Intern Video Interview' in r/FinancialCareers." + RD_NOTE,
    doubt="The commenter says 'my experience a few years ago' and 'It's been a while so the details are lost on me, unfortunately. This is just an anecdote' - so even he treats the recall as unreliable.",
))
R.append(dict(RD_BASE,
    firm="Citadel",
    source_url="https://www.reddit.com/r/csMajors/comments/1u4dhg7/citadel_swe_intern_interview/ord8pus/",
    post_date="2026-06-13", role_track="quant_developer", level="unknown",
    round="phone_technical", round_name="technical round",
    section_context="medium to hard difficulty", question_type="coding_algorithms",
    question_text="a question i remember was something like median from a data stream, plus code review and debugging discussions. so i'd say it's more like medium to hard difficulty. but i also had a bit of technical discussion toward the end (like c++/language fundamentals & computer architecture)",
    source_quote="a question i remember was something like median from a data stream, plus code review and debugging discussions. so i'd say it's more like medium to hard difficulty.",
    poster_context="u/nullnotfound2 replying in r/csMajors thread 'Citadel SWE Intern interview'." + RD_NOTE,
    doubt="The commenter opens with 'not sure if my insights would still be accurate since i interviewed last year and it wasn't exactly for an internship', so both the recency and the internship label are disclaimed by the source; level is therefore left unknown.",
))
R.append(dict(RD_BASE,
    firm="IMC Trading",
    source_url="https://www.reddit.com/r/csMajors/comments/16zricy/imc_trading_swe_intern_oa/k3gjbtp/",
    post_date="2023-10-04", role_track="quant_developer", level="internship",
    round="online_assessment", round_name="OA (thread title: IMC Trading SWE Intern OA)",
    section_context=None, question_type="coding_algorithms",
    question_text="The OA is two LC medium-hards if I remember correctly.",
    source_quote="Unfortunately, if you haven’t done the OA yet, it’s extremely unlikely that they’ll still have space for you by the time you would finish the whole process. The OA is two LC medium-hards if I remember correctly.",
    poster_context="u/Sven9888 in r/csMajors thread 'IMC Trading SWE Intern OA'." + RD_NOTE,
    doubt="Hedged with 'if I remember correctly' and gives only a difficulty band, naming neither problem.",
))

# ===========================================================================
# openquant.co Q&A with an incoming Jane Street quant trading intern.
# ===========================================================================
R.append(dict(
    firm="Jane Street",
    source_url="https://openquant.co/blog/how-to-land-a-quant-internship-at-jane-street",
    source_type="blog", source_language="en", access="snippet_only",
    retrieval_method="websearch_snippet", post_date="unknown",
    office="unknown", cycle="unknown", platform="unknown",
    role_track="quant_trader", level="internship",
    round="unknown", round_name="four interview rounds: Round 1-3 phone screen, Round 4 on-site interviews",
    section_context="four rounds", question_type="other",
    question_text="In totality, I had four interview rounds consisting of an assortment of technical and behavioral questions. The technical side mainly involved probability, statistics, expected value, market making, and game theory questions.",
    question_text_en=None, reported_answer=None,
    source_quote="In totality, I had four interview rounds consisting of an assortment of technical and behavioral questions. The technical side mainly involved probability, statistics, expected value, market making, and game theory questions.",
    poster_context="Q&A published by openquant.co with a named-as-anonymous incoming Jane Street Quantitative Trading intern; the site states 'Out of respect for Jane Street's process, we won't delve into the specifics of what questions were asked'.",
    doubt="The publisher deliberately withholds every actual question, so this attests only the shape of the process; openquant.co is a commercial quant job board, which gives it an incentive to publish this kind of content for traffic.",
))

write(R)
