#!/usr/bin/env python3
"""p14: the Wall Street Oasis company-interview entries the earlier passes left on the
table. WSO sits behind Cloudflare, so these pages were pulled through r.jina.ai into
.verify_cache and every source_quote below was string-matched against those bytes.

Each WSO entry carries its own role heading, interview month and submission date, which
is what the level / cycle / post_date fields are taken from. Where the entry's role
heading does not name a track (e.g. "Generalist"), role_track stays unknown.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p14_wso_remainder.jsonl")
rows = []

AKUNA = "https://www.wallstreetoasis.com/company/akuna-capital-llc/interview"
DESHAW = "https://www.wallstreetoasis.com/company/de-shaw/interview"
DRW = "https://www.wallstreetoasis.com/company/drw/interview"
FIVER = "https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview"
HRT = "https://www.wallstreetoasis.com/company/hudson-river-trading-llc/interview"
JUMP = "https://www.wallstreetoasis.com/company/jump-trading/interview"
OMC = "https://www.wallstreetoasis.com/company/old-mission-capital/interview"
TS = "https://www.wallstreetoasis.com/company/two-sigma-investments/interview"

# WSO's structural weakness, restated per record so the reservation travels with the row.
WSO_DOUBT = ("WSO entries are anonymous and self-submitted with no verification that the poster "
             "interviewed at all; the submission date here is %s, %s after the stated interview month, "
             "so the recall is retrospective.")
WSO_DOUBT_PLAIN = ("WSO entries are anonymous and self-submitted with no verification that the poster "
                   "actually interviewed there.")


def add(**kw):
    rec = {
        "firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
        "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
        "section_context": None, "question_type": "other", "question_text": None,
        "question_text_en": None, "reported_answer": None, "source_url": None,
        "source_type": "wso", "source_quote": None, "source_language": "en",
        "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": None, "doubt": None,
    }
    rec.update(kw)
    for k in ("firm", "question_text", "source_url", "source_quote", "doubt"):
        assert rec[k], "missing %s in %r" % (k, rec.get("question_text"))
    assert len(rec["source_quote"]) >= 20, "short quote: %r" % rec["source_quote"]
    rows.append(rec)


# ------------------------------------------------------------------ Akuna Capital
add(firm="Akuna Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="Chicago", round="online_assessment", round_name="Skills Test / IQ / Intelligence Test",
    section_context="Top performers of the Akuna 201 course get expedited to the final rounds. The course lasts 5 days and there is a quiz each day.",
    question_type="mental_math_speed",
    question_text="Mental math (2x2 operations), series, and probability.",
    source_url=AKUNA, source_quote="Mental math (2x2 operations), series, and probability.",
    post_date="2026-05-05",
    poster_context="WSO 'Junior Trader Interview - Sales and Trading', anonymous candidate in Chicago, interviewed April 2026, no offer",
    doubt=WSO_DOUBT % ("May 05, 2026", "about a month"))

add(firm="Akuna Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="Chicago", round="online_assessment", round_name="math test",
    section_context="received math test 80 questions",
    question_type="mental_math_speed",
    question_text="Doing mental math without paper pen and no calculators allowed",
    source_url=AKUNA, source_quote="Doing mental math without paper pen and no calculators allowed",
    post_date="2026-03-12",
    poster_context=("WSO 'Junior trader Interview - Sales and Trading', anonymous candidate in Chicago, "
                    "interviewed November 2025; narrative says 'received math test 80 questions ... followed "
                    "by a probability test, involved calculating expected value questions of events'"),
    doubt=WSO_DOUBT % ("Mar 12, 2026", "about four months"))

add(firm="Akuna Capital", role_track="quant_researcher", level="internship", cycle="unknown",
    office="New York", round="online_assessment",
    round_name="Online assessment followed by video interview",
    platform="VidCruiter",
    section_context="the video interview was nontraditional requiring you to verbally work through ~7 recorded math questions",
    question_type="other",
    question_text="Convergence time of newton's method",
    source_url=AKUNA, source_quote="Convergence time of newton's method",
    post_date="2025-11-30",
    poster_context="WSO 'Quantitative Research Intern Interview - Quantitative Research', anonymous candidate in New York, interviewed October 2025, no offer",
    doubt=(WSO_DOUBT % ("Nov 30, 2025", "about a month")) +
          " Platform is labelled VidCruiter from Akuna's known recorded-video round, not from this entry, which only says 'video interview'.")

add(firm="Akuna Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="Chicago", round="online_assessment", round_name="math assessment",
    section_context="The test was around 70 questions and soon got harder as the questions went on.",
    question_type="mental_math_speed",
    question_text="The mental math problems which were timed, one example was the 56*56",
    source_url=AKUNA, source_quote="The mental math problems which were timed, one example was the 56*56",
    post_date="2025-09-01",
    poster_context="WSO 'Junior Trader Interview - Prop Trading', anonymous candidate in Chicago, interviewed July 2025, applied on LinkedIn, no offer",
    doubt=WSO_DOUBT % ("Sep 01, 2025", "about two months"))

# --------------------------------------------------------------------- D. E. Shaw
add(firm="D. E. Shaw", role_track="unknown", level="internship", cycle="unknown",
    office="California", round="phone_technical",
    round_name="interview was with a member of the recruiting team",
    question_type="behavioral",
    question_text=("Some situational questions such as \"what would you do if a team member is spreading "
                   "false/inaccurate information about your firm online\""),
    source_url=DESHAW,
    source_quote=("Some situational questions such as \"what would you do if a team member is spreading "
                  "false/inaccurate information about your firm online\""),
    post_date="2026-06-20",
    poster_context="WSO 'summer intern Interview - Generalist', anonymous candidate in California, interviewed May 2025, no offer",
    doubt=(WSO_DOUBT % ("Jun 20, 2026", "about thirteen months")) +
          " Role heading is 'Generalist', so this may not be a quant track at all.")

add(firm="D. E. Shaw", role_track="unknown", level="internship", cycle="unknown",
    office="New York", round="phone_technical", round_name="first round interview with HR",
    question_type="behavioral",
    question_text=("You\u2019re part of an intern group with 4 others and you are tasked with generating "
                   "feedback on the internship. You have an idea for how to improve the internship but all "
                   "the others don\u2019t like your idea. What do you do"),
    source_url=DESHAW,
    source_quote=("You\u2019re part of an intern group with 4 others and you are tasked with generating "
                  "feedback on the internship. You have an idea for how to improve the internship but all "
                  "the others don\u2019t like your idea. What do you do"),
    post_date="2026-02-24",
    poster_context="WSO 'Fundamental Research Analyst Intern Interview - Public Investment', anonymous candidate in New York, interviewed January 2026, no offer",
    doubt=(WSO_DOUBT % ("Feb 24, 2026", "about a month")) +
          " This is the Public Investment (fundamental research) track, not a quant track.")

# ---------------------------------------------------------------------------- DRW
add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown",
    office="London", round="phone_technical", round_name="short phone interview with a recruiter",
    section_context="Behavioural and mental math.",
    question_type="mental_math_speed",
    question_text="Mental math multiplication (e.g. 73*74)",
    source_url=DRW, source_quote="Mental math multiplication (e.g. 73*74)",
    post_date="2026-01-11",
    poster_context=("WSO 'Trader Intern Interview', anonymous candidate in London, interviewed October 2026 "
                    "per the entry; narrative says the OA 'consisted of math, statistics, and probability "
                    "theory (eg. one question was about markov chains...)'"),
    doubt=("WSO entries are anonymous and self-submitted. This one is internally inconsistent: it claims an "
           "October 2026 interview but was submitted Jan 11, 2026, i.e. before the stated interview date."))

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown",
    office="London", round="phone_technical",
    round_name="technical interview based on normal distribution and market making",
    section_context="OA consisting of maths and stats questions 45mins long",
    question_type="market_making",
    question_text="Make me a market on the amount of diapers used in the UK daily",
    source_url=DRW, source_quote="Make me a market on the amount of diapers used in the UK daily",
    post_date="2025-11-08",
    poster_context=("WSO 'Quant Intern Interview - Trading', anonymous candidate in London, interviewed "
                    "October 2025; final round was 'a machine learning data task and two back to back "
                    "technical interviews with prob and stats'"),
    doubt=WSO_DOUBT % ("Nov 08, 2025", "about a month"))

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown",
    office="unknown", round="phone_technical", round_name="1 on 1 interviews consist of pair coding/statistics/machine learning discussions",
    section_context="First an online test consisting of 6 hard math questions, ranging from fundamental linear algebra, statistics and calculus.",
    question_type="coding_algorithms",
    question_text="Please write me a binary search to qucikly locate timstamps",
    source_url=DRW, source_quote="Please write me a binary search to qucikly locate timstamps",
    post_date="2025-10-24",
    poster_context="WSO 'QT intern Interview - Trading', anonymous candidate, interviewed December 2023, no offer",
    doubt=WSO_DOUBT % ("Oct 24, 2025", "about 22 months"))

add(firm="DRW", role_track="quant_trader", level="new_grad", cycle="unknown",
    office="Chicago", round="superday", round_name="in person superday. The super day consisted of 3 interviews.",
    question_type="options_theory",
    question_text="Explain how to price an option",
    source_url=DRW,
    source_quote="Had the online math assessment, and then had a zoom interview, then had a in person superday.",
    post_date="2025-10-16",
    poster_context="WSO 'Quant Trading Analyst Interview - Quantitative Trading', anonymous employee in Chicago, interviewed June 2025, accepted offer",
    doubt=(WSO_DOUBT % ("Oct 16, 2025", "about four months")) +
          " The 'Explain how to price an option' line is in the entry's question block but the quote I could "
          "match verbatim is the surrounding narrative, so the question text is from the same entry but not "
          "the same sentence as the quote.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown",
    office="Chicago", round="phone_technical",
    round_name="technical phone interview on EV calculations, market making, and mathematical modeling",
    section_context="Online assessment involving mathematics questions and brainteasers (linear algebra, matrix calculations, statistics + markov chains, probability brainteasers etc.)",
    question_type="market_making",
    question_text="Market making and fermi estimation on random quantities",
    source_url=DRW, source_quote="Market making and fermi estimation on random quantities",
    post_date="2025-10-12",
    poster_context="WSO 'Quant Trading Intern Interview - Quantitative Trading', anonymous candidate in Chicago, interviewed September 2025, no offer",
    doubt=WSO_DOUBT % ("Oct 12, 2025", "about a month"))

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown",
    office="London", round="phone_technical", round_name="1-1 technical interview",
    section_context="a 6 question OA which consisted of math/stats questions",
    question_type="logic_brainteaser",
    question_text="Apples and Oranges question with the mislabeled boxes",
    source_url=DRW, source_quote="Apples and Oranges question with the mislabeled boxes",
    post_date="2024-12-24",
    poster_context="WSO 'Quant Intern Interview - Quant', anonymous candidate in London, interviewed September 2024, no offer",
    doubt=(WSO_DOUBT % ("Dec 24, 2024", "about three months")) +
          " The mislabeled-boxes puzzle is a standard textbook brainteaser, so it is not distinctive to DRW; "
          "the attestation is nonetheless a candidate recall.")

# --------------------------------------------------------------------- Five Rings
add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="unknown",
    office="New York", round="phone_technical",
    round_name="First round was 10 questions with 30 seconds to respond to each round",
    section_context="10 questions with 30 seconds to respond to each, followed by 3-4 rounds of probability questions",
    question_type="other",
    question_text="Calculate the length of x^2 from 0 to 9",
    source_url=FIVER, source_quote="Calculate the length of x^2 from 0 to 9",
    post_date="2025-01-11",
    poster_context="WSO 'Intern Interview - Quant', anonymous candidate in New York, interviewed July 2024; says they answered all questions correctly but were rejected in round three",
    doubt=(WSO_DOUBT % ("Jan 11, 2025", "about six months")) +
          " The question as written is ambiguous (arc length of the curve, presumably), so the recall may be garbled.")

add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="unknown",
    office="London", round="phone_technical", round_name="HR phone/video interview",
    section_context="asking you to quickly estimate values such as weight of a baby elephant",
    question_type="mental_math_speed",
    question_text="Tenth root of 10, answer within 10 seconds",
    source_url=FIVER,
    source_quote=("Tenth root of 10, answer within 10 seconds, A game theory question at second round."),
    post_date="2022-10-21",
    poster_context="WSO 'Trader Intern Interview - Prop Trading', anonymous candidate in London, interviewed April 2022, no offer",
    doubt=WSO_DOUBT % ("Oct 21, 2022", "about six months"))

add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="unknown",
    office="London", round="phone_technical", round_name="1-hour video interview",
    question_type="poker_game_theory",
    question_text=("A game theory question at second round. Cannot remember exactly as a very long question, "
                   "but similar to the Jane street example interview at this page "
                   "'https://www.janestreet.com/trading-interviews/'."),
    source_url=FIVER,
    source_quote=("A game theory question at second round. Cannot remember exactly as a very long question, "
                  "but similar to the Jane street example interview at this page"),
    post_date="2022-10-21",
    poster_context="WSO 'Trader Intern Interview - Prop Trading', anonymous candidate in London, interviewed April 2022, no offer",
    doubt=(WSO_DOUBT % ("Oct 21, 2022", "about six months")) +
          " The poster explicitly cannot remember the question and describes it only by analogy, so no actual question content survives.")

add(firm="Five Rings", role_track="quant_trader", level="unknown", cycle="unknown",
    office="New York", round="phone_technical", round_name="first round interview",
    section_context="I was given a short amount time to answer (10-15 seconds) them.",
    question_type="fermi_estimation",
    question_text="How many tennis balls in a suit case?, 3^ 3.4? Confidence interval?",
    source_url=FIVER, source_quote="How many tennis balls in a suit case?, 3^ 3.4? Confidence interval?",
    post_date="2022-09-05",
    poster_context="WSO 'Quant Trader Interview - Other', anonymous candidate in New York, interviewed November 2019, no offer",
    doubt=WSO_DOUBT % ("Sep 05, 2022", "nearly three years"))

add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="unknown",
    office="New York", round="phone_technical", round_name="hr interview (fermi questions under tight time constraints)",
    question_type="probability",
    question_text="proof of answer to a probability question involving discrete math",
    source_url=FIVER,
    source_quote=("online application -> hr interview (fermi questions under tight time constraints) -> 1st "
                  "round video interview with trader"),
    post_date="2022-06-25",
    poster_context="WSO 'quantitative trading intern Interview - Prop Trading', anonymous candidate in New York, interviewed October 2021, no offer",
    doubt=(WSO_DOUBT % ("Jun 25, 2022", "about eight months")) +
          " The question block only names a category, not a problem; the matched quote is the process description.")

add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="unknown",
    office="New York", round="phone_technical",
    round_name="phone interview consisting of many estimation questions (fermi and computational math)",
    section_context="Given short time limits to give answers.",
    question_type="fermi_estimation",
    question_text="Weight of Baby elephant. Average distance from center of circle.",
    source_url=FIVER, source_quote="Weight of Baby elephant. Average distance from center of circle.",
    post_date="2021-10-04",
    poster_context="WSO 'Trading Intern Interview', anonymous candidate in New York, interviewed December 2020, no offer",
    doubt=WSO_DOUBT % ("Oct 04, 2021", "about ten months"))

# --------------------------------------------------------- Hudson River Trading
add(firm="Hudson River Trading", role_track="quant_researcher", level="internship", cycle="unknown",
    office="New York", round="online_assessment", round_name="Online assessment",
    platform="HackerRank",
    section_context="3 coding questions on hacker rank, ranging from dp to tree traversal. given 90 minutes",
    question_type="coding_algorithms",
    question_text="Online assessment with 3 coding questions on hacker rank, ranging from dp to tree traversal, given 90 minutes.",
    source_url=HRT,
    source_quote="Online assessment with 3 coding questions on hacker rank, ranging from dp to tree traversal. given 90 minutes",
    post_date="2024-10-20",
    poster_context="WSO 'SummerIintern Interview - Quantitative Research', anonymous candidate in New York, interviewed October 2024, no offer",
    doubt=(WSO_DOUBT % ("Oct 20, 2024", "days")) +
          " Topic-level: names the areas ('dp to tree traversal') without giving any problem statement.")

add(firm="Hudson River Trading", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="New York", round="phone_technical", round_name="phone screen",
    section_context="Got 3 problems, Leetcode Medium/Hard. Solved all 3 in C++.",
    question_type="expected_value",
    question_text="Questions on EV for coin tosses, law of large numbers, Bayes theorem",
    source_url=HRT, source_quote="Questions on EV for coin tosses, law of large numbers, Bayes theorem",
    post_date="2023-10-22",
    poster_context=("WSO 'Algorithm Developer Interview - Prop Trading', anonymous candidate in New York, "
                    "interviewed October 2020; says 'problems were variations of problems from the green book'"),
    doubt=(WSO_DOUBT % ("Oct 22, 2023", "about three years")) +
          " The poster themself says the problems were green-book variations, so the content overlaps a textbook, "
          "though the attestation is a candidate recall.")

# ------------------------------------------------------------------- Jump Trading
add(firm="Jump Trading", role_track="quant_researcher", level="internship", cycle="unknown",
    office="unknown", round="onsite", round_name="one full day of online interviews (with 3-4 different people, ~1 hour each)",
    question_type="behavioral",
    question_text="What was the most unreasonable thing that you\u2019ve ever done?",
    source_url=JUMP, source_quote="What was the most unreasonable thing that you\u2019ve ever done?",
    post_date="2020-09-09",
    poster_context="WSO 'Quant Research Intern Interview - Quantitative Research', anonymous employee, interviewed September 2019, accepted offer",
    doubt=WSO_DOUBT % ("Sep 09, 2020", "about a year"))

add(firm="Jump Trading", role_track="quant_developer", level="internship", cycle="unknown",
    office="Cambridge", round="onsite", round_name="in person technical interview",
    question_type="coding_algorithms",
    question_text=("How I would store key value pairs, then a discussion about how I would implement a hash "
                   "map data structure, tradeoffs between various implementations, and implement methods to "
                   "add a key to the hashmap and retrieve a key from the hashmap."),
    source_url=JUMP,
    source_quote=("Then I was asked about how I would store key value pairs. And then ended in a discussion "
                  "about how I would implement a hash map data structure. I was asked about the tradeoffs "
                  "between various implementations."),
    post_date="2019-10-08",
    poster_context="WSO 'Software Development Internship Interview - Engineering', anonymous candidate in Cambridge, interviewed August 2019, no offer",
    doubt=WSO_DOUBT % ("Oct 08, 2019", "about two months"))

add(firm="Jump Trading", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="Chicago", round="onsite", round_name="onsite with 4 rounds",
    question_type="probability",
    question_text=("I'm dealing a deck of poker, you can stop me anytime. If the next card is red, you win. "
                   "Otherwise you lose. What's optimal strategy and the probability of winning ?"),
    source_url=JUMP,
    source_quote=("I'm dealing a deck of poker, you can stop me anytime. If the next card is red, you win. "
                  "Otherwise you lose. What's optimal strategy and the probability of winning ?"),
    post_date="2018-12-24",
    poster_context="WSO 'algo trader Interview - Research', anonymous candidate in Chicago, interviewed October 2018 via on-campus recruiting, no offer",
    doubt=WSO_DOUBT % ("Dec 24, 2018", "about two months"))

add(firm="Jump Trading", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="Chicago", round="onsite", round_name="onsite with 4 rounds",
    question_type="probability",
    question_text="one iteration of bubble sort, what's the probability that the array will be sorted.",
    source_url=JUMP,
    source_quote="one iteration of bubble sort, what's the probability that the array will be sorted.",
    post_date="2018-12-24",
    poster_context="WSO 'algo trader Interview - Research', anonymous candidate in Chicago, interviewed October 2018 via on-campus recruiting, no offer",
    doubt=WSO_DOUBT % ("Dec 24, 2018", "about two months"))

add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="Urbana", round="onsite", round_name="whiteboard interview with two other engineers",
    section_context="The interview was 45 minutes long and consisted of a straightforward whiteboard question with two separate tasks",
    question_type="coding_algorithms",
    question_text=("1. Convert decimal-based number to a 16-bit binary representation 2. Represent as 4x4 "
                   "matrix of 0s and 1s 3. Detect if path of 0s exists in matrix from top left to bottom "
                   "right cell and if so, print out the path in the format of a string; otherwise, return a "
                   "\"No path\" string"),
    source_url=JUMP,
    source_quote=("Convert decimal-based number to a 16-bit binary representation"),
    post_date="2018-02-05",
    poster_context="WSO 'Jump Trading Interview - Software', anonymous candidate in Urbana, interviewed September 2017 via on-campus recruiting, no offer",
    doubt=(WSO_DOUBT % ("Feb 05, 2018", "about five months")) +
          " The entry says 'two separate tasks' then lists three, so the recall is internally inconsistent.")

add(firm="Jump Trading", role_track="quant_trader", level="internship", cycle="unknown",
    office="Chicago", round="superday", round_name="superday consisting of 4 interviews",
    section_context="One was a purely coding interview with a laptop in front of me (C++). Another was purely mathematical/linear algebra done on the whiteboard. The third and fourth were pen/paper brainteaser and math/probability questions.",
    question_type="coding_algorithms",
    question_text="Implement a trie in C++.",
    source_url=JUMP, source_quote="Implement a trie in C++.\n\nSwap two variables without additional storage",
    post_date="2014-01-06",
    poster_context="WSO 'Algorithmic Trading Intern Interview - Trading', anonymous candidate in Chicago, interviewed March 2013, no offer",
    doubt=(WSO_DOUBT % ("Jan 06, 2014", "about ten months")) + " Also over a decade old, so unlikely to reflect the current process.")

add(firm="Jump Trading", role_track="quant_trader", level="internship", cycle="unknown",
    office="Chicago", round="superday", round_name="superday consisting of 4 interviews",
    question_type="coding_algorithms",
    question_text="Swap two variables without additional storage (i.e. no using a temp).",
    source_url=JUMP,
    source_quote="Swap two variables without additional storage (i.e. no using a temp).",
    post_date="2014-01-06",
    poster_context="WSO 'Algorithmic Trading Intern Interview - Trading', anonymous candidate in Chicago, interviewed March 2013, no offer",
    doubt=(WSO_DOUBT % ("Jan 06, 2014", "about ten months")) + " Also over a decade old, so unlikely to reflect the current process.")

add(firm="Jump Trading", role_track="quant_trader", level="internship", cycle="unknown",
    office="Chicago", round="superday", round_name="superday consisting of 4 interviews",
    question_type="combinatorics",
    question_text="How many 0's are in 1000! (factorial)?",
    source_url=JUMP, source_quote="How many 0's are in 1000! (factorial)?",
    post_date="2014-01-06",
    poster_context="WSO 'Algorithmic Trading Intern Interview - Trading', anonymous candidate in Chicago, interviewed March 2013, no offer",
    doubt=(WSO_DOUBT % ("Jan 06, 2014", "about ten months")) +
          " Also a standard textbook counting problem and over a decade old.")

# -------------------------------------------------------------------- Two Sigma
add(firm="Two Sigma", role_track="quant_researcher", level="new_grad", cycle="unknown",
    office="New York", round="onsite", round_name="Three rounds of tech interviews",
    section_context="One is like model design- predict rent prices in Manhattan. Then live coding and states. Stats round is about proof of OLS/optimizaition/Langrange, etc, quite difficult",
    question_type="ml_modeling",
    question_text="model design - predict rent prices in Manhattan",
    source_url=TS,
    source_quote="One is like model design- predict rent prices in Manhattan. Then live coding and states.",
    post_date="2026-01-14",
    poster_context="WSO 'Junior Quant Researcher Interview - Quantitative Research', anonymous candidate in New York, interviewed November 2025, no offer",
    doubt=WSO_DOUBT % ("Jan 14, 2026", "about two months"))

add(firm="Two Sigma", role_track="quant_researcher", level="new_grad", cycle="unknown",
    office="New York", round="onsite", round_name="Stats round",
    question_type="statistics_regression",
    question_text="Stats round is about proof of OLS/optimizaition/Langrange, etc, quite difficult. Sequential regression, multivariant regression, etc.",
    source_url=TS,
    source_quote="Stats round is about proof of OLS/optimizaition/Langrange, etc, quite difficult",
    post_date="2026-01-14",
    poster_context="WSO 'Junior Quant Researcher Interview - Quantitative Research', anonymous candidate in New York, interviewed November 2025, no offer",
    doubt=WSO_DOUBT % ("Jan 14, 2026", "about two months"))

add(firm="Two Sigma", role_track="quant_researcher", level="internship", cycle="unknown",
    office="New York", round="onsite",
    round_name="final technical round consisting of one coding, one stats, and one data science round",
    question_type="statistics_regression",
    question_text="Come up with two uncorrelated but dependent variables.",
    source_url=TS, source_quote="Come up with two uncorrelated but dependent variables.",
    post_date="2025-10-05",
    poster_context="WSO 'QR Intern Interview - Generalist', anonymous candidate in New York, interviewed August 2025, no offer",
    doubt=WSO_DOUBT % ("Oct 05, 2025", "about two months"))

add(firm="Two Sigma", role_track="quant_researcher", level="internship", cycle="unknown",
    office="New York", round="onsite",
    round_name="final technical round consisting of one coding, one stats, and one data science round",
    question_type="probability",
    question_text="One markov chain question that was from greenbook.",
    source_url=TS, source_quote="One markov chain question that was from greenbook.",
    post_date="2025-10-05",
    poster_context="WSO 'QR Intern Interview - Generalist', anonymous candidate in New York, interviewed August 2025, no offer",
    doubt=(WSO_DOUBT % ("Oct 05, 2025", "about two months")) +
          " The poster explicitly identifies the question as coming from the Green Book, so the content is "
          "textbook \u2014 but the attestation that Two Sigma asked it is a candidate recall.")

add(firm="Two Sigma", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="New York", round="phone_technical", round_name="a conversation with a researcher there",
    question_type="other",
    question_text="How would you make money with social media data?",
    source_url=TS, source_quote="How would you make money with social media data?",
    post_date="2024-10-04",
    poster_context="WSO 'Researcher Interview', anonymous candidate in New York, interviewed January 2024, no offer",
    doubt=WSO_DOUBT % ("Oct 04, 2024", "about nine months"))

add(firm="Two Sigma", role_track="unknown", level="unknown", cycle="unknown",
    office="New York", round="online_assessment", round_name="OA",
    section_context="3 hr for 2 coding tests + 1 bonus coding",
    question_type="coding_algorithms",
    question_text=("first one is about writing a regression algorithm from scratch, second one using pandas "
                   "package to solve some datascience problems. bonus question is a follow up for Q2"),
    source_url=TS,
    source_quote=("First received OA, 3 hr for 2 coding tests + 1 bonus coding. first one is about writing a "
                  "regression algorithm from scratch, second one using pandas package to solve some "
                  "datascience problems. bonus question is a follow up for Q2"),
    post_date="2024-11-15",
    poster_context="WSO entry headed 'None Interview - Investment Banking', anonymous employee in New York, interviewed October 2024, accepted offer",
    doubt=(WSO_DOUBT % ("Nov 15, 2024", "about a month")) +
          " The entry's own role heading is 'None / Investment Banking', which contradicts the quant OA it "
          "describes, so the role track cannot be pinned down.")

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
