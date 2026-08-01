#!/usr/bin/env python3
"""p09: 1point3acres (via WebSearch snippets) + Glassdoor pages served as full text
by the search tool.

Provenance notes that apply to the whole file:
 * 1point3acres 403s every direct request from this box. Everything sourced from it
   here is text the search engine returned verbatim in its Highlights block, so
   `access` is snippet_only and `retrieval_method` is websearch_snippet.
 * The Glassdoor pages below were returned by the search tool as a complete
   page-text dump (saved into .verify_cache), so those are access=full_text even
   though a direct WebFetch of glassdoor.com is blocked.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p09_1p3a_glassdoor.jsonl")
rows = []


def add(**kw):
    rec = {
        "firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
        "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
        "section_context": None, "question_type": "other", "question_text": None,
        "question_text_en": None, "reported_answer": None, "source_url": None,
        "source_type": None, "source_quote": None, "source_language": "en",
        "post_date": "unknown", "access": "snippet_only",
        "retrieval_method": "websearch_snippet", "poster_context": None, "doubt": None,
    }
    rec.update(kw)
    for k in ("firm", "question_text", "source_url", "source_type", "source_quote", "doubt"):
        assert rec[k], "missing %s in %s" % (k, rec.get("question_text"))
    rows.append(rec)


# =====================================================================================
# 1point3acres — Jump Trading tag page. The tag listing shows the opening lines of each
# thread, which is where the OA question lists sit, so the previews are the evidence.
# =====================================================================================
JT_TAG = "https://www.1point3acres.com/bbs/tag/jumptrading-8699-1.html"
P3A_DOUBT = ("1point3acres blocks this box, so this is the search engine's verbatim "
             "Highlights excerpt of the page rather than a page I loaded; the thread "
             "body itself is points-gated, so I cannot see the poster's full wording.")

add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="Jump Trading OA",
    question_type="coding_algorithms",
    question_text="source file and destination file comparison，有更改就return",
    question_text_en="Compare a source file and a destination file; return if there is any change.",
    source_url=JT_TAG, source_type="1point3acres",
    source_quote="Jump Trading OA [*]source file and destination file comparison，有更改就return[*]workflow management system debug 嵌套input处理",
    source_language="mixed", post_date="2026-02-01",
    poster_context="匿名 poster, thread listed on the 1point3acres jumptrading tag page, dated 2026-2-1, 5 replies / 1632 views",
    doubt=P3A_DOUBT + " The preview compresses the whole OA into two bullet fragments, so this is the poster's shorthand, not the problem statement.")

add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="Jump Trading OA",
    question_type="coding_algorithms",
    question_text="workflow management system debug 嵌套input处理",
    question_text_en="Debug a workflow management system; handling of nested input.",
    source_url=JT_TAG, source_type="1point3acres",
    source_quote="Jump Trading OA [*]source file and destination file comparison，有更改就return[*]workflow management system debug 嵌套input处理",
    source_language="mixed", post_date="2026-02-01",
    poster_context="匿名 poster, thread listed on the 1point3acres jumptrading tag page, dated 2026-2-1, 5 replies / 1632 views",
    doubt=P3A_DOUBT + " Two bullet fragments only; 'workflow management system debug' names the task but not the actual problem.")

add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="新鲜 C++ OA",
    platform="Codility", section_context="codility3题140分钟",
    question_type="coding_algorithms",
    question_text="数组X，Y，长度相同。X/Y 代表一个fraction，找出出现次数最多的fraction，返回次数，例如2/3和4/6相等。",
    question_text_en="Arrays X and Y of equal length. X[i]/Y[i] represents a fraction; find the most frequently occurring fraction and return its count — e.g. 2/3 and 4/6 are equal.",
    source_url=JT_TAG, source_type="1point3acres",
    source_quote="Jump trading 新鲜 C++ OA 求加米 codility3题140分钟[*]数组X，Y，长度相同。X/Y 代表一个fraction，找出出现次数最多的fraction，返回次数，例如2/3和4/6相等。",
    source_language="mixed", post_date="2026-02-13",
    poster_context="匿名 poster, 'Jump trading 新鲜 C++ OA 求加米', 1point3acres jumptrading tag page, dated 2026-2-13, 0 replies / 1858 views",
    doubt=P3A_DOUBT + " The tag preview renders X[i]/Y[i] as 'X/Y' because the [i] was eaten as BBCode, so the indices are my reading of an obviously index-wise operation.")

add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="新鲜 C++ OA",
    platform="Codility", section_context="codility3题140分钟",
    question_type="coding_algorithms",
    question_text="字符串处理，包含数字，空格，+， -， D",
    question_text_en="String processing, containing digits, spaces, +, -, D ...",
    source_url=JT_TAG, source_type="1point3acres",
    source_quote="[*]字符串处理，包含数字，空格，+， -， D ...",
    source_language="mixed", post_date="2026-02-13",
    poster_context="匿名 poster, 'Jump trading 新鲜 C++ OA 求加米', 1point3acres jumptrading tag page, dated 2026-2-13",
    doubt=P3A_DOUBT + " The tag preview is cut off mid-sentence at 'D ...', so the question is truncated and the task is not recoverable.")

# The thread page for the same 2026-02-13 C++ OA, whose visible (non-gated) portion
# carries a third bullet the tag preview cut off.
JT_THREAD = "https://www.1point3acres.com/bbs/thread-1165004-1-1.html"
add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="技术电面 / codility3题140分钟",
    platform="Codility", section_context="codility3题140分钟",
    question_type="coding_algorithms",
    question_text="正整数数组，找出最大的subset的长度。这个subset里面所有的数AND结果为正。",
    question_text_en="Given an array of positive integers, find the length of the largest subset such that the AND of all numbers in the subset is positive.",
    source_url=JT_THREAD, source_type="1point3acres",
    source_quote="正整数数组，找出最大的subset的长度。这个subset里面所有的数AND结果为正。",
    source_language="zh", post_date="2026-02-13",
    poster_context=("匿名用户-HEHZE, posted 2026-2-13 11:40:33; header line reads "
                    "'2026(1-3月) 码农类General 本科 全职@jumptrading - Other - 技术电面'"),
    doubt=P3A_DOUBT + " The post header says 全职 (full-time), not an internship, and most of the body sits behind a 188-point paywall — this bullet is one of the few lines rendered outside it.")

add(firm="Jump Trading", role_track="quant_developer", level="internship", cycle="2025",
    office="unknown", round="online_assessment",
    round_name="投简历后一周内收到笔试邮件，OA共有三道题",
    section_context="OA共有三道题，有OOD也有算法题，总时长165分钟，一旦开始不能停止，但可以跳题做",
    question_type="coding_algorithms",
    question_text="第一题是一个OOD的文件解析，给一个FILE的抽象类，其中",
    question_text_en="The first question was an OOD file-parsing problem: you are given an abstract FILE class, in which ...",
    source_url=JT_TAG, source_type="1point3acres",
    source_quote="求米，jump trading 2025 C++ Software Engineer (Intern)面经 投简历后一周内收到笔试邮件，OA共有三道题，有OOD也有算法题，总时长165分钟，一旦开始不能停止，但可以跳题做。第一题是一个OOD的文件解析，给一个FILE的抽象类，其中 ...",
    source_language="mixed", post_date="2025-03-22",
    poster_context="爱听歌的自行车, 'jump trading 2025 C++ Software Engineer (Intern)面经', 2025-3-22, 3 replies / 2489 views",
    doubt=P3A_DOUBT + " The preview truncates at '其中 ...', so only the setup of question 1 is visible and the actual requirement is missing.")

add(firm="Jump Trading", role_track="quant_researcher", level="internship", cycle="unknown",
    office="unknown", round="phone_technical",
    round_name="Jumptrading QR intern电面他家无oa，hr+电面+onsite",
    section_context="简单自我介绍，没有过简历，直接做题",
    question_type="coding_algorithms",
    question_text="1. n*n",
    question_text_en="1. n*n ...",
    source_url=JT_TAG, source_type="1point3acres",
    source_quote="[气球R]Jumptrading QR intern电面他家无oa，hr+电面+onsite （听说hr和电面顺序可能会换）前段时间过了电面，流程如下：简单自我介绍，没有过简历，直接做题。1. n*n ...",
    source_language="mixed", post_date="2025-01-23",
    poster_context="微信用户_yuoz2, '北美quant最新面试经验题目jumptrading面经', 2025-1-23, 0 replies / 3680 views",
    doubt=P3A_DOUBT + " The preview cuts off at '1. n*n ...' — the question is a stub. Its value is the process detail (QR intern has no OA: hr + phone + onsite), not the question.")

add(firm="Jump Trading", role_track="quant_researcher", level="internship", cycle="unknown",
    office="芝加哥/纽约", round="phone_technical", round_name="Jump QR实习 HR面+技术面",
    question_type="behavioral",
    question_text="问为啥想做量化然后对他们了解多少，问想通过实习获得什么之类的。还问毕业打不打算留在学术界",
    question_text_en="Asked why I want to do quant and how much I know about them, what I want to get out of the internship, and whether I plan to stay in academia after graduating.",
    source_url=JT_TAG, source_type="1point3acres",
    source_quote="Jump QR实习 HR面+技术面 简历海投 芝加哥/纽约Office 一周之后收到回复约HR面。HR面大概就闲聊，然后问为啥想做量化然后对他们了解多少，问想通过实习获得什么之类的。还问毕业打不打算留在学术界 ...",
    source_language="mixed", post_date="2025-10-02",
    poster_context="匿名 poster, 'Jump QR实习 HR面+技术面', 1point3acres jumptrading tag page, 2025-10-2, 2 replies / 2583 views",
    doubt=P3A_DOUBT + " These are HR-screen behavioural prompts paraphrased by the poster ('之类的' = 'and so on'), not verbatim interviewer wording.")

# =====================================================================================
# 1point3acres — HRT
# =====================================================================================
HRT_THREAD = "https://www.1point3acres.com/bbs/thread-1022110-1-1.html"
add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    cycle="unknown", office="unknown", round="online_assessment",
    round_name="网上海投 - 在线笔试", section_context="150 分钟 3道题",
    question_type="coding_algorithms",
    question_text="第一题：给你一个数n，问比它小的数里面有多少fancy number，fancy number的定义是转成4",
    question_text_en="Question 1: given a number n, how many 'fancy numbers' are there below it? A fancy number is defined as one that, converted to base 4, ...",
    source_url=HRT_THREAD, source_type="1point3acres",
    source_quote="150 分钟 3道题 第一题：给你一个数n，问比它小的数里面有多少fancy number，fancy number的定义是转成4",
    source_language="mixed", post_date="2023-10",
    poster_context=("Thread 'HRT Algo Dev OA'; header line reads '2023(10-12月) 码农类General "
                    "本科 实习@hudson-river-trading - 网上海投 - 在线笔试 | Neutral | Average | "
                    "Other | 应届毕业生'"),
    doubt=P3A_DOUBT + " The definition of 'fancy number' is cut off exactly at '转成4' (converted to base 4), so the predicate is incomplete; a replier's answer describes it as '4-base fancy numbers', which is consistent but is a second person's reading.")

add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    cycle="unknown", office="unknown", round="online_assessment",
    round_name="网上海投 - 在线笔试", section_context="150 分钟 3道题",
    question_type="coding_algorithms",
    question_text="ht的node，其他node全部保留。 总体感觉思考难度中等，代码量挺大，2个半小时给的不多。",
    question_text_en="... the node of [rig]ht, all other nodes are kept. Overall the thinking difficulty felt medium, the amount of code was quite large, and two and a half hours was not much.",
    source_url=HRT_THREAD, source_type="1point3acres",
    source_quote="| ht的node，其他node全部保留。 总体感觉思考难度中等，代码量挺大，2个半小时给的不多。 |",
    source_language="mixed", post_date="2023-10",
    poster_context="Thread 'HRT Algo Dev OA', 实习@hudson-river-trading, 在线笔试, 2023(10-12月)",
    doubt=P3A_DOUBT + " This is a tail fragment of question 3 — the snippet begins mid-word ('ht的node'), so the problem statement is largely missing. A replier describes q3 as topological sort plus a two-tree node-deletion walk, which is a third party's reconstruction.")

HRT_COLL = "https://www.1point3acres.com/bbs/collection/238911"
add(firm="Hudson River Trading", role_track="quant_developer", level="new_grad",
    cycle="unknown", office="unknown", round="online_assessment",
    round_name="Hudson river trading 0909full-time NG OA 新鲜出炉 (HRT)(OA)",
    question_type="coding_algorithms",
    question_text="第三题，给定一个文本string，int limit(分段过后的长度限制不能超过这个长度)，让你切",
    question_text_en="Question 3: given a text string and an int limit (the length limit that each segment must not exceed after splitting), split it ...",
    source_url=HRT_COLL, source_type="1point3acres",
    source_quote="HRT新鲜出炉笔试题：新人求大米，求积分！第一二题基础，基本随便过的easy题第三题，给定一个文本string，int limit(分段过后的长度限制不能超过这个长度)，让你切 ...",
    source_language="mixed", post_date="2022-09-09",
    poster_context="匿名 poster, listed in the 'HRT面经' 淘帖 collection, dated 2022-9-9, 11 replies / 3960 views",
    doubt=P3A_DOUBT + " The collection preview truncates at '让你切 ...' so the splitting objective is missing; the poster explicitly labels questions 1 and 2 as easy without stating them.")

add(firm="Hudson River Trading", role_track="quant_developer", level="new_grad",
    cycle="unknown", office="unknown", round="online_assessment",
    round_name="HRT NG OA 要开摄像头和录屏", platform="CodeSignal",
    question_type="coding_algorithms",
    question_text="['A','a','b','B','C']，ret",
    question_text_en="['A','a','b','B','C'], ret[urn] 2 (ignoring case)",
    source_url=HRT_COLL, source_type="1point3acres",
    source_quote="HRT\n...\nNG OA 要开摄像头和录屏",
    source_language="mixed", post_date="2022-10-11",
    poster_context="地里匿名用户, listed in the 'HRT面经' 淘帖 collection, dated 2022-10-11; entry marked [阅读权限 …] (read-permission gated)",
    doubt=P3A_DOUBT + " The search engine's own excerpt is elided with '...' around this entry, so I can quote only the fragment either side of the ellipsis; the example array and the 'ret…2（忽略大…' answer fragment appeared in the excerpt but not as one contiguous run I can honestly quote.")

add(firm="Hudson River Trading", role_track="quant_developer", level="unknown",
    cycle="unknown", office="unknown", round="phone_technical",
    round_name="hrt 电面", section_context="HRT先得做OA，三道题，题目挺简单，一个小时都过了test case。然后是两轮电面",
    question_type="coding_algorithms",
    question_text="基本就是问python语法，比如coroutine以及context manager相关的知识",
    question_text_en="Basically asked about Python syntax, for example knowledge related to coroutines and context managers.",
    source_url=HRT_COLL, source_type="1point3acres",
    source_quote="hrt 电面 HRT先得做OA，三道题，题目挺简单，一个小时都过了test case。然后是两轮电面，",
    source_language="mixed", post_date="2022-11-24",
    poster_context="leogalante, listed in the 'HRT面经' 淘帖 collection, dated 2022-11-24, 4 replies / 4930 views",
    doubt=P3A_DOUBT + " The Python-syntax sentence sits after an ellipsis in the engine's excerpt, so my source_quote covers only the contiguous run that precedes it; the question itself is a topic list, not a stated problem.")

add(firm="Hudson River Trading", role_track="quant_researcher", level="unknown",
    cycle="unknown", office="unknown", round="online_assessment", round_name="HRT QR OA",
    section_context="一共四道题", question_type="coding_algorithms",
    question_text="HRT QR OA hudson-river-trading OA 一共四道题**** 本内容被作者隐藏 ****",
    question_text_en="HRT QR OA — four questions in total. **** This content has been hidden by the author ****",
    source_url=HRT_COLL, source_type="1point3acres",
    source_quote="HRT QR OA hudson-river-trading OA 一共四道题**** 本内容被作者隐藏 ****新人求米,谢谢!补充内容 (2022-11-03 05:51 +8:00):简单写了回忆版的1，3，4的代码",
    source_language="mixed", post_date="2022-11-02",
    poster_context="匿名 poster, 'HRT QR OA', 淘帖 collection 'HRT面经', 2022-11-2, 55 replies / 8993 views",
    doubt=P3A_DOUBT + " The author hid the body ('本内容被作者隐藏'), so no question content exists here at all — this record only attests that the HRT QR OA had four questions in Nov 2022. Included for the round/section fact, not for a question.")

add(firm="Hudson River Trading", role_track="quant_developer", level="unknown",
    cycle="unknown", office="unknown", round="online_assessment", round_name="[OA分享]",
    platform="CodeSignal", question_type="other",
    question_text="Code Signal 上做的OA，要求打开摄像头以及共享屏幕。但是如果你有第二个屏幕还是可以在上面看一些function的调用之类的",
    question_text_en="The OA was done on CodeSignal; it requires you to turn on your camera and share your screen. But if you have a second monitor you can still look up things like function calls on it.",
    source_url=HRT_COLL, source_type="1point3acres",
    source_quote="[OA分享] Hudson River Trading Code Signal 上做的OA，要求打开摄像头以及共享屏幕。但是如果你有第二个屏幕还是可以在上面看一些function的调用之类的，我觉得应该没什么问题。Code signal 似乎每个人拿 ...",
    source_language="mixed", post_date="2022-09-11",
    poster_context="匿名 poster, '[OA分享]', 淘帖 collection 'HRT面经', 2022-9-11, 5 replies / 3250 views",
    doubt=P3A_DOUBT + " This describes the proctoring format, not a question; I am recording it because it pins the platform (CodeSignal, camera + screen-share) for HRT's 2022 OA, and the question_type is 'other' for that reason.")

# =====================================================================================
# Glassdoor — Five Rings Quantitative Researcher (page served as full text by search)
# =====================================================================================
FR_GD = ("https://www.glassdoor.com/Interview/Five-Rings-Quantitative-Researcher-Interview-Questions-"
         "EI_IE375785.0,10_KO11,34.htm")
GD_DOUBT = ("Glassdoor entries are anonymous, self-reported and undated as to the question itself; "
            "the reviewer supplies the interview month but nothing verifies they interviewed at all. "
            "Glassdoor blocks direct fetching from this box — this text came back as a complete "
            "page-text dump from the search tool, which I saved to the verifier cache.")

add(firm="Five Rings", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical",
    round_name="30-40 mins initial screen with HR",
    section_context="it's all about some(12 - 15) hard probability / stats questions",
    question_type="probability", question_text="Dice roll, Linear Regression etc.",
    source_url=FR_GD, source_type="glassdoor",
    source_quote="30-40 mins initial screen with HR and it's all about some(12 - 15) hard probability / stats questions.",
    source_language="en", post_date="2024-03-03", access="full_text",
    poster_context="Anonymous Interview Candidate, Mar 3, 2024, No Offer, Positive Experience, Difficult Interview",
    doubt=GD_DOUBT + " 'Dice roll, Linear Regression etc.' is a two-word topic list, not a question — no problem is actually stated.")

add(firm="Five Rings", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical",
    round_name="Initial call with recruiter",
    section_context="a few behavioral questions and then ~10 rapid fire stats and probability questions. The time allotted for each question varied from 20 seconds to 90 seconds",
    question_type="behavioral",
    question_text="Why are you interested in quantitative finance?",
    source_url=FR_GD, source_type="glassdoor",
    source_quote="Initial call with recruiter involved a few behavioral questions and then \\~10 rapid fire stats and probability questions. The time allotted for each question varied from 20 seconds to 90 seconds, so it required very quick thinking.",
    source_language="en", post_date="2024-04-09", access="full_text",
    poster_context="Anonymous Interview Candidate, Apr 9, 2024, No Offer, Neutral Experience, Difficult Interview; applied online, process took 2 weeks, interviewed 3/1/2024",
    doubt=GD_DOUBT + " The listed question is the behavioural one; the ~10 rapid-fire stats problems that are the interesting part were not written down by the poster.")

add(firm="Five Rings", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical",
    round_name="The first round is an HR call, which lasts around 30 minutes",
    question_type="probability",
    question_text="Mainly about probability problems and mental math",
    source_url=FR_GD, source_type="glassdoor",
    source_quote="The first round is an HR call, which lasts around 30 minutes. The interviewer asked many technical questions and there were no behavioral questions.",
    source_language="en", post_date="2023-11-28", access="full_text",
    poster_context="Anonymous Interview Candidate, Nov 28, 2023, No Offer, Neutral Experience, Average Interview; applied online, process took 4 weeks",
    doubt=GD_DOUBT + " The 'question' is a category label ('probability problems and mental math'), so nothing specific is recoverable.")

add(firm="Five Rings", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical", round_name="Interview",
    question_type="statistics_regression",
    question_text="Typical statistical and probability questions",
    source_url=FR_GD, source_type="glassdoor",
    source_quote="Throughout the interview apparently the HR has no technical background about the questions being asked.",
    source_language="en", post_date="2023-09-16", access="full_text",
    poster_context="Anonymous Interview Candidate, Sep 16, 2023, No Offer, Negative Experience, Average Interview",
    doubt=GD_DOUBT + " Purely a category label; the entry's substance is a complaint about scheduling, and it contributes no question content.")

add(firm="Five Rings", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical", round_name="Phone interview with HR",
    question_type="probability",
    question_text="math and probability and statistic problems",
    source_url=FR_GD, source_type="glassdoor",
    source_quote="Phone interview with HR. It is difficult as the time limit. I have to have the answer in a short time. And there should be many rounds of phone interview.",
    source_language="en", post_date="2021-10-27", access="full_text",
    poster_context="Anonymous Interview Candidate, Oct 27, 2021, No Offer, Neutral Experience, Difficult Interview; applied online, process took 1 week, interviewed 10/1/2021",
    doubt=GD_DOUBT + " Category label only. Kept for the round structure it attests (HR-run timed phone screen, multiple phone rounds), not for question content.")

add(firm="Five Rings", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="unknown", round_name="Multiple rounds of video interviews",
    question_type="behavioral",
    question_text="Talk about your past internship project",
    source_url=FR_GD, source_type="glassdoor",
    source_quote="Multiple rounds of video interviews. Then I dropped out of the interview process. The questions were interesting and challenging.",
    source_language="en", post_date="2021-07-24", access="full_text",
    poster_context="Anonymous Interview Candidate, Jul 24, 2021, No Offer, Positive Experience, Difficult Interview",
    doubt=GD_DOUBT + " The poster dropped out partway, and does not say which of the 'multiple rounds of video interviews' this prompt came from, so the round is unknown.")

# =====================================================================================
# Glassdoor — Hudson River Trading, "Intern" job-title page (full text dump)
# =====================================================================================
HRT_GD = ("https://www.glassdoor.com/Interview/Hudson-River-Trading-Intern-Interview-Questions-"
          "EI_IE470937.0,20_KO21,27.htm")

add(firm="Hudson River Trading", role_track="unknown", level="internship", cycle="unknown",
    office="New York, NY", round="online_assessment",
    round_name="a coding assessment", section_context="4 questions in 90 minutes",
    question_type="coding_algorithms",
    question_text="Non disclosure agreement, but the brainteasers are probability based (with kind of intuition to bring). LC hard for the programming !",
    source_url=HRT_GD, source_type="glassdoor",
    source_quote="The coding assessment is difficult (4 questions in 90 minutes) and the rounds of interview are difficult as well (one brain-teaser like interview and one programming one).",
    source_language="en", post_date="2022-11-11", access="full_text",
    poster_context="Anonymous Interview Candidate in New York, NY, Nov 11, 2022, No offer, Negative experience, Difficult interview; applied online, process took 2 weeks, interviewed Oct 2022",
    doubt=GD_DOUBT + " The poster explicitly cites an NDA and therefore withholds the problems; what survives is the format (4 questions / 90 minutes, probability brainteaser round, LeetCode-hard programming round), not any question.")

add(firm="Hudson River Trading", role_track="unknown", level="internship", cycle="unknown",
    office="New York, NY", round="online_assessment",
    round_name="an online accessment test through Codelity", platform="unknown",
    section_context="three c++ questions. The time limit is two hours",
    question_type="coding_algorithms", question_text="sum up some numbers",
    source_url=HRT_GD, source_type="glassdoor",
    source_quote="I take an online accessment test through Codelity with three c++ questions. The time limit is two hours. These questions are very easy but you need to be very familiar with c++ language.",
    source_language="en", post_date="2019-11-06", access="full_text",
    poster_context="Anonymous Interview Candidate in New York, NY, Nov 6, 2019, No offer, Neutral experience, Easy interview; applied online, process took 2 weeks, interviewed Oct 2019",
    doubt=GD_DOUBT + " 'sum up some numbers' is a four-word gloss of the problem, so the actual task is unrecoverable; the platform name is the poster's misspelling of Codility.")

add(firm="Hudson River Trading", role_track="unknown", level="internship", cycle="unknown",
    office="unknown", round="online_assessment",
    round_name="Had to complete an OA that took about an hour",
    question_type="coding_algorithms",
    question_text="This was a leetcode question, probably an easy or medium about data structures.",
    source_url=HRT_GD, source_type="glassdoor",
    source_quote="Resume screening and phone interview going over past projects. Had to complete an OA that took about an hour. This was a leetcode question, probably an easy or medium about data structures.",
    source_language="en", post_date="2021-09-23", access="full_text",
    poster_context="Anonymous employee, Sep 23, 2021, Accepted offer, Neutral experience, Average interview; applied online, process took 2 months, interviewed Sep 2021",
    doubt=GD_DOUBT + " The poster is hedging ('probably an easy or medium'), so even the difficulty is a guess and no problem is stated.")

add(firm="Hudson River Trading", role_track="unknown", level="internship", cycle="unknown",
    office="unknown", round="phone_technical", round_name="phone call interview",
    question_type="logic_brainteaser", question_text="algorithms, math, puzzles",
    source_url=HRT_GD, source_type="glassdoor",
    source_quote="I was asked some behavioral and background questions followed by algorithms and math questions. Interviewer was helpful in guiding through the problems.",
    source_language="en", post_date="2016-01-03", access="full_text",
    poster_context="Anonymous Interview Candidate, Jan 3, 2016, No offer, Neutral experience, Average interview; applied online for the internship, process took 1 week, interviewed Oct 2015",
    doubt=GD_DOUBT + " Three-word topic list from a 2015 interview; nothing specific, and old enough that HRT's intern process has certainly changed.")

add(firm="Hudson River Trading", role_track="unknown", level="internship", cycle="unknown",
    office="New York, NY", round="onsite",
    round_name="Six thirty minute interviews", question_type="behavioral",
    question_text="Explain to me what the company does.",
    source_url=HRT_GD, source_type="glassdoor",
    source_quote="Six thirty minute interviews, nice people, wide range of people that interviewed me, some technical questions, mainly a behavioral conversation, asked about my resume a lot, asked about classes in school a lot, asked me about my trading knowledge",
    source_language="en", post_date="2023-06-16", access="full_text",
    poster_context="Anonymous Interview Candidate in New York, NY, Jun 16, 2023, No offer, Neutral experience, Difficult interview; applied online, process took 4 weeks, interviewed Mar 2023",
    doubt=GD_DOUBT + " I label this onsite because the poster describes six back-to-back 30-minute interviews, but they never use the word 'onsite' and it could have been a virtual superday.")

add(firm="Hudson River Trading", role_track="unknown", level="internship", cycle="unknown",
    office="New York, NY", round="unknown", round_name="Interview",
    question_type="behavioral", question_text="tell me about yourself and what you do",
    source_url=HRT_GD, source_type="glassdoor",
    source_quote="detail oriented, lots of follow ups, very nice people, i found it a good experience but stressed me out a lot in preparing.",
    source_language="en", post_date="2025-01-08", access="full_text",
    poster_context="Anonymous employee in New York, NY, Jan 8, 2025, Accepted offer, Positive experience, Difficult interview",
    doubt=GD_DOUBT + " A generic opener with no round attached; included only because it is a dated accepted-offer intern account of HRT.")


with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
