#!/usr/bin/env python3
"""Citadel SWE-intern recalls from Glassdoor, a Citadel Securities Medium write-up, and
an Optiver data-scientist 笔试 from Nowcoder.

Glassdoor blocks direct fetching, but the search tool captured the whole interview page
to disk, so this reads that capture and asserts every quote against it before writing.
Most Glassdoor entries name a topic ("graph and DP") rather than a problem statement;
they are kept because the reporter is a dated first-person candidate, and the doubt
field says plainly that the wording is a label, not the question.
"""
import pathlib
import sys

sys.path.insert(0, "/workspace/harvest/tools")
import tiera_lib

GD_FILE = pathlib.Path(
    "/home/ubuntu/.cursor/projects/workspace/agent-tools/"
    "e4e76da1-eef9-4bec-b610-9ca6b5c214ea.txt")
GD_TXT = GD_FILE.read_text(encoding="utf-8")
GD_URL = ("https://www.glassdoor.com/Interview/Citadel-Software-Engineering-Intern-"
          "Interview-Questions-EI_IE14937.0,7_KO8,35.htm")

GD_DOUBT_TOPIC = (
    "Glassdoor's 'interview question' field here records a topic label rather than the "
    "problem statement, so the actual question cannot be reconstructed from it; entries "
    "are also anonymous and unverified by Glassdoor, and the site rewards posting an "
    "interview to unlock content, which incentivises thin or invented submissions.")
GD_DOUBT_CONCRETE = (
    "Anonymous, unverified Glassdoor submission posted to unlock site content; the "
    "problem is also a standard LeetCode/BFS exercise, so a candidate could be "
    "recalling practice material rather than the paper in front of them.")

# (date, glassdoor narrative used for context, question text, type, round, round_name,
#  office, extra quote to anchor the record)
GD = [
    ("2025-03-05",
     "Was nervous for this, but the interviewer was friendly. First round was behavioral then one LC I had seen before.",
     "LC Medium - Hardish coding question",
     "coding_algorithms", "phone_technical", "First round was behavioral then one LC",
     "unknown", GD_DOUBT_TOPIC),
    ("2024-12-06",
     "It was a 45 minute call where you solved a Leetcode Medium difficulty type question. You also talked about your resume at the start and had room for questions at the end.",
     "Why do you want to work at Citadel?",
     "behavioral", "phone_technical", "a 45 minute call", "New York, NY", GD_DOUBT_TOPIC),
    ("2024-09-06",
     "Apply online and immediately get a 66 minute hackerrank -- two LC med/hards. This + resume screen determines next rounds.",
     "LC Medium/Hard, implementation questions, why do you want to work here and what do you want to do next summer type stuff",
     "coding_algorithms", "superday",
     "45 minute phone interview that is 15 minutes behavioral and 30 minutes technical ... superday -- basically just the phone round but three of them back to back",
     "New York, NY", GD_DOUBT_TOPIC),
    ("2024-01-09",
     "First round of technical, then 3 back to back onsites.Interviews are not that hard, but you have to pass all of them for an offer.",
     "Leetcode hard of strings, some concurrency and some easies like read number of lines",
     "coding_algorithms", "onsite", "First round of technical, then 3 back to back onsites",
     "unknown", GD_DOUBT_TOPIC),
    ("2023-10-09",
     "Then given a link for an online assessment for initial screening. Involved 90 mins to solve a few questions on the hackerrank site.",
     "One of the problems were based on graphs.",
     "coding_algorithms", "online_assessment", "online assessment for initial screening",
     "unknown", GD_DOUBT_TOPIC),
    ("2023-09-19",
     "Know your D S and A. it is tested during every interview. the final was LC-medium hards. OS trivia may also be asked.",
     "Leetcode style questions- graph and DP",
     "coding_algorithms", "onsite", "the final was LC-medium hards", "unknown", GD_DOUBT_TOPIC),
    ("2023-09-24",
     "I was given 2 coding questions to solve in a little bit over an hour. It used HackerRank, gave a few test cases available and a few locked test cases, as well as an option to make a custom test.",
     "Given an nxn chess board, return the minimum number of knight moves it would take to get from point (a,b) to point(c,d)",
     "coding_algorithms", "online_assessment", "2 coding questions to solve in a little bit over an hour",
     "unknown", GD_DOUBT_CONCRETE),
    ("2023-03-06",
     "Without any recruiter call, I was given an OA to do 30 minutes after submitting the application.",
     "Leetcode DP problems on the hard level",
     "coding_algorithms", "online_assessment", "an OA to do 30 minutes after submitting the application",
     "unknown", GD_DOUBT_TOPIC),
    ("2023-01-18",
     "Online Assessment: Online Assessment was in HackerRank. It consisted of two questions. Both were medium leetcode questions. First question was based on sliding window topic . Second question was based on Dynamic Programming topic. Solved both the questions, still didnt get any reply.",
     "Online Assessment: Online Assessment was in HackerRank. It consisted of two questions. Both were medium leetcode questions. First question was based on sliding window topic . Second question was based on Dynamic Programming topic.",
     "coding_algorithms", "online_assessment", "Online Assessment ... in HackerRank",
     "unknown", GD_DOUBT_TOPIC),
]

SECTION = {
    "2024-09-06": "66 minute hackerrank -- two LC med/hards",
    "2023-10-09": "90 mins to solve a few questions on the hackerrank site",
    "2023-09-24": "2 coding questions to solve in a little bit over an hour",
    "2023-01-18": "two questions. Both were medium leetcode questions",
}

recs = []
for date, narrative, q, qtype, rnd, rname, office, doubt in GD:
    assert narrative in GD_TXT, narrative[:60]
    assert q in GD_TXT, q[:60]
    recs.append({
        "firm": "Citadel",
        "role_track": "quant_developer",
        "level": "internship",
        "cycle": "unknown",
        "office": office,
        "round": rnd,
        "round_name": rname,
        "platform": ("HackerRank" if "ackerrank" in narrative or "HackerRank" in narrative
                     else "unknown"),
        "section_context": SECTION.get(date),
        "question_type": qtype,
        "question_text": q,
        "question_text_en": None,
        "reported_answer": None,
        "source_url": GD_URL,
        "source_type": "glassdoor",
        "source_quote": narrative if len(narrative) > len(q) else q,
        "source_language": "en",
        "post_date": date,
        "access": "full_text",
        "retrieval_method": "websearch_snippet",
        "poster_context": (
            "Anonymous Glassdoor 'Software Engineering Intern Interview' entry at Citadel, "
            f"dated {date}. Narrative on the same card: \"{narrative[:180]}\". Glassdoor "
            "blocks direct fetching from this host; the whole interview page was captured "
            "through the web-search tool, not WebFetch."),
        "doubt": doubt,
    })

# ------------------------------------------------ Citadel Securities, Medium write-up

MED_URL = ("https://medium.com/@adityashrivastava2003/citadel-securities-swe-intern-"
           "singapore-interview-experience-386dc70fc1eb")
MED_POSTER = (
    "Adityashrivastava, a third-year CS undergraduate ('aspiring software engineer "
    "current - swe intern@sharechat'), interviewed for Software Engineer Intern at "
    "Citadel Securities Singapore in Jan 2024 after cold-emailing the CTO; rejected "
    "after failing to finish the round-1 coding problem. Published 2024-12-17.")
MED_DOUBT = (
    "Written eleven months after the fact ('I got this opportunity back in Jan of 2024'), "
    "and the round-1 problem is described only as resembling LRU Cache rather than quoted, "
    "so the actual prompt may have differed; two commenters asked what the HackerRank "
    "problems were and the author never answered, which leaves the OA content unattested.")

MED = [
    ("Conceptual Discussion on C++ TemplatesThe interviewer started by asking in-depth questions about templates in C++. These questions were aimed at testing my understanding of advanced C++ concepts, such as:",
     "The interviewer started by asking in-depth questions about templates in C++ ... such as: How templates work; Use cases for templates in real-world scenarios; Differences between function templates and class templates; Template specialization and instantiation",
     "coding_algorithms"),
    ("Coding Problem: LRU CacheAfter the conceptual discussion, I was given a hard-level problem that resembled the LRU (Least Recently Used) Cache problem. The problem required designing a data structure that could efficiently perform insertions, deletions, and lookups while maintaining a specific order based on usage.",
     "I was given a hard-level problem that resembled the LRU (Least Recently Used) Cache problem. The problem required designing a data structure that could efficiently perform insertions, deletions, and lookups while maintaining a specific order based on usage.",
     "coding_algorithms"),
]

for quote, qtext, qtype in MED:
    recs.append({
        "firm": "Citadel Securities",
        "role_track": "quant_developer",
        "level": "internship",
        "cycle": "2024",
        "office": "Singapore",
        "round": "phone_technical",
        "round_name": "Round 1: Technical Interview",
        "platform": "unknown",
        "section_context": "Duration: 1 hour",
        "question_type": qtype,
        "question_text": qtext,
        "question_text_en": None,
        "reported_answer": None,
        "source_url": MED_URL,
        "source_type": "blog",
        "source_quote": quote,
        "source_language": "en",
        "post_date": "2024-12-17",
        "access": "full_text",
        "retrieval_method": "webfetch",
        "poster_context": MED_POSTER,
        "doubt": MED_DOUBT,
    })

# ------------------------------------------------------ Optiver data scientist, Nowcoder

OPT_URL = "https://www.nowcoder.com/feed/main/detail/464155d6b69747ebaa947add8c266c58"
OPT_QUOTE = ("一共考了两道编程题，合计两个小时。Q1：股票分红，输入 股价 分红 时间   输出 现股价"
             "Q2：动物表演，找某个时间房间内的最大动物")
OPT_POSTER = ("牛客用户 @找到工作了噢（转帖者标注 华东理工大学 golang，发布于上海），帖子"
              "『【2023暑实】optiver数据科学家 笔试』：投递+约笔半个月，时长 2h，形势 HackerRank；"
              "自评『算是目前笔试下来最硬核的一次coding，难度高过了Morgan Stanley，吊打Tencent』。")
OPT_DOUBT = ("The poster records only a one-line label for each problem ('股票分红' / '动物表演'), "
             "not the prompt, so the actual constraints and I/O format are unrecoverable; the "
             "page is also a repost of another user's feed item rather than the original thread.")

for qtext, qtype, qen in [
    ("Q1：股票分红，输入 股价 分红 时间   输出 现股价", "coding_algorithms",
     "Q1: stock dividend -- input: share price, dividend, time; output: the current share price."),
    ("Q2：动物表演，找某个时间房间内的最大动物", "coding_algorithms",
     "Q2: animal show -- find the largest animal in the room at a given time."),
]:
    recs.append({
        "firm": "Optiver",
        "role_track": "data_scientist",
        "level": "internship",
        "cycle": "2023 暑期实习",
        "office": "unknown",
        "round": "online_assessment",
        "round_name": "笔试",
        "platform": "HackerRank",
        "section_context": "一共考了两道编程题，合计两个小时",
        "question_type": qtype,
        "question_text": qtext,
        "question_text_en": qen,
        "reported_answer": None,
        "source_url": OPT_URL,
        "source_type": "nowcoder",
        "source_quote": OPT_QUOTE,
        "source_language": "zh",
        "post_date": "unknown",
        "access": "full_text",
        "retrieval_method": "webfetch",
        "poster_context": OPT_POSTER,
        "doubt": OPT_DOUBT,
    })

tiera_lib.write(recs)
