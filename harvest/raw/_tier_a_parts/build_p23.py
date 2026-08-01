#!/usr/bin/env python3
"""p23: WallStreetOasis per-interview permalinks.

Earlier passes mined https://www.wallstreetoasis.com/company/<firm>/interview, which
renders only the ten most recent write-ups and truncates each of them. The
/interview/<slug> permalinks carry the whole submission, and WSO indexes 13-51 of them
per firm rather than 10 — so most of this text has never been in the dataset. 80
permalinks were fetched through the jina text proxy (WSO Cloudflare-challenges a plain
curl); wso_perm.py parses them and wso_diff.py isolated the sentences absent from both
the listing dumps and every source_quote already recorded.

Everything below is the "Please describe the interview / hiring process." field of a
single dated submission, so round attribution is the submitter's own. WSO submissions
are anonymous and unverified, which is the standing doubt; per-record doubt notes the
sharper problem where there is one.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p23_wso_permalinks.jsonl")
rows = []

ANON = ("Anonymous WallStreetOasis interview submission; WSO records the interview month "
        "and the submitter's self-reported job title and office but nothing else about them")
BASE_DOUBT = ("WSO interview submissions are anonymous, self-reported and never verified "
              "against an actual application, and the site rewards submissions with content "
              "credits, which gives a mild incentive to embellish. ")


def add(url, quote, qtext, qtype, firm, role, level, round_, round_name, post_date,
        doubt_extra="", platform="unknown", section=None, cycle="unknown", answer=None,
        office="unknown", poster=None):
    rows.append({
        "firm": firm, "role_track": role, "level": level, "cycle": cycle, "office": office,
        "round": round_, "round_name": round_name, "platform": platform,
        "section_context": section, "question_type": qtype, "question_text": qtext,
        "question_text_en": None, "reported_answer": answer, "source_url": url,
        "source_type": "wso", "source_quote": quote, "source_language": "en",
        "post_date": post_date, "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": poster or ANON, "doubt": BASE_DOUBT + doubt_extra,
    })


W = "https://www.wallstreetoasis.com/company/"

# ------------------------------------------------------------------ Akuna Capital
add(W + "akuna-capital-llc/interview/junior-trader-44",
    "It was timed mental math problems where you oculd not use a calulator. The test was "
    "around 70 questions and soon got harder as the questions went on. The second part of the "
    "exam was sceniors to see if you make quick decisions.",
    "Timed mental math assessment, around 70 questions, no calculator, getting harder as you "
    "go; second part is scenarios testing quick decision-making",
    "mental_math_speed", "Akuna Capital", "quant_trader", "new_grad", "online_assessment",
    "a math assessment", "2025-07",
    "The submitter's spelling ('oculd', 'calulator', 'sceniors') suggests a hurried write-up, "
    "and 'around 70' is an estimate rather than a counted figure.",
    section="around 70 questions, timed, no calculator")
add(W + "akuna-capital-llc/interview/junior-trader-47",
    "Applied online, received math test 80 questions, the math test was based on arithmetic "
    "questions mental math.",
    "Math test of 80 arithmetic mental-math questions",
    "mental_math_speed", "Akuna Capital", "quant_trader", "new_grad", "online_assessment",
    "math test", "2025-11",
    "Question count (80) differs from the 70 another Junior Trader submission reports four "
    "months earlier, so either the test varies or one of the two counts is misremembered.",
    section="80 questions")
add(W + "akuna-capital-llc/interview/junior-trader-47",
    "This was followed by a probability test, involved calculating expected value questions of "
    "events",
    "Probability test involving calculating expected value of events",
    "expected_value", "Akuna Capital", "quant_trader", "new_grad", "online_assessment",
    "a probability test", "2025-11",
    "Describes the topic of the round rather than any individual question.")
add(W + "akuna-capital-llc/interview/junior-trader-49",
    "Did multiple online assessment first mental math. Probably impossible to do all in the "
    "short time and you lose a lot of time clicking but basically standard mental math and "
    "sequences.",
    "First OA: standard mental math and sequences, too many to finish in the time given",
    "sequences", "Akuna Capital", "quant_trader", "new_grad", "online_assessment",
    "multiple online assessment", "2026-02",
    "The submitter never states which role level this was for beyond the 'Junior Trader' "
    "title, and gives no example question.",
    section="first of at least three online assessments")
add(W + "akuna-capital-llc/interview/junior-trader-49",
    "second online assessment was probability. the format was a little tricky, instead of "
    "typing in probabilities it was more like: \"if you win you get 1$. how much money would "
    "be a fair bet.\" or something like that. but the probabilies were very easy.",
    "Second OA, probability: instead of entering a probability you are asked things like \"if "
    "you win you get 1$. how much money would be a fair bet.\"",
    "betting_odds_arbitrage", "Akuna Capital", "quant_trader", "new_grad", "online_assessment",
    "second online assessment", "2026-02",
    "The submitter explicitly hedges the wording with 'or something like that', so the phrasing "
    "is a reconstruction rather than a transcription.")
add(W + "akuna-capital-llc/interview/junior-trader-49",
    "had to do 3rd online assessment which was just an easy market making game with camera on "
    "and a behavioral question at the end.",
    "Third OA: an easy market making game with camera on, plus a behavioral question at the end",
    "market_making", "Akuna Capital", "quant_trader", "new_grad", "trading_game",
    "3rd online assessment", "2026-02",
    "Consistent with Akuna's known VidCruiter recorded round but the submitter does not name "
    "the platform, so the identification is inference.",
    platform="VidCruiter")
add(W + "akuna-capital-llc/interview/junior-quant-trader-0",
    "Had to take their Options 201 course which took about 5 hours over 3 days. They mentioned "
    "top performers would be expedited to the final round but I had to do a zoom interview in "
    "between.",
    "Akuna's Options 201 course used as a screening stage: about 5 hours over 3 days, top "
    "performers expedited to the final round",
    "options_theory", "Akuna Capital", "quant_trader", "new_grad", "take_home",
    "their Options 201 course", "2026-03",
    "Describes the stage, not a question; and it is a training course doubling as a screen, "
    "so 'assessment' is the submitter's framing.")
add(W + "akuna-capital-llc/interview/junior-trader-48",
    "Top performers of the Akuna 201 course get expedited to the final rounds. The course lasts "
    "5 days and there is a quiz each day.",
    "Akuna 201 course: 5 days with a quiz each day; top performers expedited to the final rounds",
    "options_theory", "Akuna Capital", "quant_trader", "new_grad", "take_home",
    "the Akuna 201 course", "2026-04",
    "Course length (5 days) conflicts with the '5 hours over 3 days' in the March 2026 "
    "Junior Quant Trader submission, so at least one is imprecise.")
add(W + "akuna-capital-llc/interview/quant-developer-1",
    "After applying, I quickly got a Hackerrank OA with 3 roughly Leetcode Medium level "
    "problems. My solutions passed all the provided test cases and a few days later I got "
    "another OA: 15 minutes - 3 quant probability-type questions, 5 minutes each, where I had "
    "to explain my thought process for each question.",
    "Second OA for quant developer: 15 minutes, 3 quant probability-type questions, 5 minutes "
    "each, explaining your thought process aloud for each",
    "probability", "Akuna Capital", "quant_developer", "experienced", "online_assessment",
    "another OA", "2025-09",
    "The submitter does not say the questions themselves, only the format and topic.",
    platform="HackerRank", section="15 minutes, 3 questions, 5 minutes each")
add(W + "akuna-capital-llc/interview/quant-developer-1",
    "The actual question asked was easy but then the interviewer added variations to the "
    "question, was able to answer everything except a question about a very esoteric data "
    "structure I hadn't heard about, which is what seems to have gotten me dinged.",
    "Live Zoom coding interview: an easy base question, then interviewer-added variations, "
    "ending on a very esoteric data structure",
    "coding_algorithms", "Akuna Capital", "quant_developer", "experienced", "phone_technical",
    "a live coding interview over Zoom", "2025-09",
    "The submitter never names the data structure or the base question, so nothing here is "
    "reproducible as a question.")
add(W + "akuna-capital-llc/interview/quant-researcher-intern-1",
    "It began with a technical phone screen conducted by a Senior QR, focusing on quick "
    "probability puzzles, mental math, and some data structure questions.",
    "Technical phone screen with a Senior QR: quick probability puzzles, mental math, and some "
    "data structure questions",
    "probability", "Akuna Capital", "quant_researcher", "internship", "phone_technical",
    "a technical phone screen conducted by a Senior QR", "2024-11",
    "Topic list rather than questions; the '6-7 weeks' process length is the only hard detail.")
add(W + "akuna-capital-llc/interview/quant-researcher-intern-1",
    "These interviews covered a wide range of topics: a deep dive into advanced math and "
    "statistics (linear algebra, probability); a whiteboard coding session focused on "
    "algorithms and python; and a final behavioral interview with a senior manager discussing "
    "my motivation, my understanding of quant trading, and \"why Akuna.\"",
    "Final round, three 1-on-1s: advanced math and statistics (linear algebra, probability); a "
    "whiteboard algorithms/Python session; and a behavioral with a senior manager",
    "linear_algebra", "Akuna Capital", "quant_researcher", "internship", "superday",
    "the final round, which consisted of three intensive 1-on-1 interviews", "2024-11",
    "Reads slightly like a polished summary rather than a recall, which is a mild authenticity "
    "flag, though the specifics (Senior QR phone screen, 6-7 weeks) are concrete.")
add(W + "akuna-capital-llc/interview/quantitative-research-intern",
    "OA was straightforward python leetcode-style questions, however the video interview was "
    "nontraditional requiring you to verbally work through ~7 recorded math questions.",
    "Recorded video interview requiring you to verbally work through about 7 math questions",
    "logic_brainteaser", "Akuna Capital", "quant_researcher", "internship", "online_assessment",
    "video interview", "2025-10",
    "Matches Akuna's known VidCruiter round but the submitter does not name the platform and "
    "does not say what any of the ~7 questions were.",
    platform="VidCruiter", section="~7 recorded math questions")
add(W + "akuna-capital-llc/interview/quantitative-trader-3",
    "2 rounds of online assessments, the first being quick mental math problems, second being "
    "probability questions. Invited to \"phone\" round afterward, which was a zoom interview "
    "with a trader where I was asked \"Why Akuna/trading\" and then 5 or 6 probability/game "
    "style questions.",
    "Zoom interview with a trader: \"Why Akuna/trading\" then 5 or 6 probability/game style "
    "questions",
    "probability", "Akuna Capital", "quant_trader", "unknown", "phone_technical",
    "\"phone\" round", "2025-08",
    "No individual question is given; the two-OA-then-trader-call shape matches other Akuna "
    "submissions, which is corroborating but also means it could be repeated hearsay.")

# ---------------------------------------------------------------------- Five Rings
add(W + "five-rings-capital-llc/interview/intern-1",
    "interviewer was very courteous and professional, the first interview was 10 guesstimation "
    "questions, like number of digits 7 in numbers from 1 to 6000.",
    "How many digit 7s appear in the numbers from 1 to 6000?",
    "fermi_estimation", "Five Rings", "quant_trader", "internship", "phone_technical",
    "the first interview", "2022-11",
    "The submitter gives this as an example of the type ('like ...'), so the exact bound 6000 "
    "may be approximate; it is also a counting question rather than a true estimation one, "
    "despite being grouped with the guesstimation set.",
    section="10 guesstimation questions")
add(W + "five-rings-capital-llc/interview/intern-2",
    "First round was 10 questions with 30 seconds to respond to each round, followed by 3-4 "
    "rounds of probability questions. I made it to the third round, then got rejected even "
    "though I had answered all questions correctly.",
    "First round: 10 questions with 30 seconds to respond to each, then 3-4 further rounds of "
    "probability questions",
    "probability", "Five Rings", "quant_trader", "internship", "phone_technical",
    "First round", "2024-07",
    "'I had answered all questions correctly' is the submitter's own assessment after a "
    "rejection, so the account carries obvious sour-grapes risk.",
    section="10 questions, 30 seconds each")
add(W + "five-rings-capital-llc/interview/qr-internship",
    "The OA covers various math problems and is proctored.\n The first tech round covers 3 "
    "probability questions.",
    "Proctored OA of various math problems, then a first technical round of 3 probability "
    "questions",
    "probability", "Five Rings", "quant_researcher", "internship", "online_assessment",
    "First OA. The first tech round.", "2025-09",
    "Two sentences of description with no question content at all; the 'proctored' detail is "
    "the only non-generic claim.",
    section="3 probability questions in the first tech round")
add(W + "five-rings-capital-llc/interview/quant-trader-1",
    "As some many know, the first round interview was composed of numerous guesstimation "
    "problems (ie. how many balls in suit case ...). I was given a short amount time to answer "
    "(10-15 seconds) them.",
    "How many balls in a suitcase? (given as an example of the numerous guesstimation problems, "
    "10-15 seconds each)",
    "fermi_estimation", "Five Rings", "quant_trader", "unknown", "phone_technical",
    "the first round interview", "2019-11",
    "'As some many know' signals the submitter is partly relaying common knowledge, and the "
    "example question is trailed off with an ellipsis rather than stated in full.",
    section="10-15 seconds per question")
add(W + "five-rings-capital-llc/interview/quantitative-trading-intern-0",
    "online application -> hr interview (fermi questions under tight time constraints) -> 1st "
    "round video interview with trader",
    "HR interview consisting of fermi questions under tight time constraints",
    "fermi_estimation", "Five Rings", "quant_trader", "internship", "phone_technical",
    "hr interview", "2021-10",
    "A one-line pipeline sketch with no questions and no timing figure.")
add(W + "five-rings-capital-llc/interview/trader-intern",
    "Made my application then waited for roughly 2 months, then HR phone/video interview, "
    "asking you to quickly estimate values such as weight of a baby elephant.",
    "Quickly estimate the weight of a baby elephant",
    "fermi_estimation", "Five Rings", "quant_trader", "internship", "phone_technical",
    "HR phone/video interview", "2022-04",
    "Given as an example of the class of question ('values such as'), so the baby elephant may "
    "be the submitter's paraphrase of a similar estimate.")
add(W + "five-rings-capital-llc/interview/trader-intern",
    "We did a game theory question, easy math, but need to be super careful with all conditions "
    "of the question.",
    "A game theory question - easy math, but you must be careful with all the conditions",
    "poker_game_theory", "Five Rings", "quant_trader", "internship", "phone_technical",
    "a 1-hour video interview", "2022-04",
    "The question itself is not stated, only characterised; the submitter also calls the "
    "interviewer 'random unprofessional', so the account is coloured.")
add(W + "five-rings-capital-llc/interview/trading-intern-13",
    "The recruiter set up a 1:1 call which consisted of a brief behavioral component (why "
    "trading? and why five rings?) and then dove into 10 questions each with a 30 second time "
    "limit. You are encouraged to solve it as fast as possible, but accuracy is more important.",
    "Recruiter 1:1: behavioral (why trading? why Five Rings?) then 10 questions each with a "
    "30 second time limit",
    "mental_math_speed", "Five Rings", "quant_trader", "internship", "phone_technical",
    "a 1:1 call", "2024-08",
    "Confirms the 10-questions/30-seconds format several other submissions report, but gives "
    "none of the ten questions.",
    section="10 questions, 30 second time limit each")
add(W + "five-rings-capital-llc/interview/trading-intern-9",
    "Contacted by HR person for phone interview consisting of many estimation questions (fermi "
    "and computational math). Given short time limits to give answers.",
    "Phone interview of many estimation questions, both fermi and computational math, under "
    "short time limits",
    "fermi_estimation", "Five Rings", "quant_trader", "internship", "phone_technical",
    "phone interview", "2020-12",
    "Two sentences with no question content.")
add(W + "five-rings-capital-llc/interview/tactical-developer",
    "Then they scheduled a full day of interviewing (6.5 hours) over zoom, including 1:1 and "
    "2:1 interviews with developers, quants, and traders.",
    "Full day of interviewing (6.5 hours) over Zoom, 1:1 and 2:1 with developers, quants and "
    "traders",
    "other", "Five Rings", "quant_developer", "experienced", "superday",
    "a full day of interviewing", "2021-05",
    "Logistics only - no question content - and the reference-check step described alongside it "
    "is unusual enough to be worth flagging.")

# ---------------------------------------------------------- Hudson River Trading
add(W + "hudson-river-trading-llc/interview/algorithm-developer-0",
    "I had a Hackerrank test. Seems like they look at your profile and only then send the test. "
    "Got 3 problems, Leetcode Medium/Hard. Solved all 3 in C++. Then received a phone screen. "
    "Basic EV questions, problems were variations of problems from the green book.",
    "Phone screen after the HackerRank: basic EV questions, described as variations of problems "
    "from the green book",
    "expected_value", "Hudson River Trading", "quant_developer", "unknown", "phone_technical",
    "a phone screen", "2020-10",
    "The submitter's own framing is that these were green-book variants, which is exactly the "
    "textbook-overlap case: the firm really did ask them, but the questions are not original "
    "to HRT and none is stated individually.",
    platform="HackerRank", section="3 problems, Leetcode Medium/Hard")
add(W + "hudson-river-trading-llc/interview/algorithm-development-internship-0",
    "applied online, talked to them at recruiting event but that did do anything, did online "
    "assessment on hackerrank 4Q 90 minutes, passed all but last one, code was not fast enough "
    "on the last one",
    "HRT algo-dev internship OA on HackerRank: 4 questions in 90 minutes, last one gated on "
    "runtime rather than correctness",
    "coding_algorithms", "Hudson River Trading", "quant_developer", "internship",
    "online_assessment", "online assessment on hackerrank", "2022-09",
    "Gives the shape of the OA but no question; 'code was not fast enough' is the submitter's "
    "inference about why they failed.",
    platform="HackerRank", section="4Q 90 minutes")
add(W + "hudson-river-trading-llc/interview/campus-algo-dev",
    "Submitted my application online and was sent an OA after about a week, with 3 coding "
    "problems, about Easy-Medium leetcode level. About another week after the completion of "
    "this OA I was invited to a one on one interview, which was easy to schedule. I was asked "
    "an expected value question involving order statistics.",
    "An expected value question involving order statistics",
    "expected_value", "Hudson River Trading", "quant_developer", "internship",
    "phone_technical", "a one on one interview", "2024-10",
    "The submitter names the topic (expected value over order statistics) but not the question, "
    "and says they fumbled it, so their recollection of it may be poor.",
    section="OA was 3 coding problems, Easy-Medium leetcode level")
add(W + "hudson-river-trading-llc/interview/developer",
    "OA with 2.5 hours for 3 coding questions:\n 1- brain teaser like question, asking an "
    "optimal algorithm that is unlikely to be found \"naturally\". Either you know the answer "
    "or it's over. Factorization stuff.",
    "OA question 1: a brainteaser-like question asking for an optimal algorithm unlikely to be "
    "found naturally - factorization",
    "coding_algorithms", "Hudson River Trading", "quant_developer", "unknown",
    "online_assessment", "OA with 2.5 hours for 3 coding questions", "2023-12",
    "'Factorization stuff' is as specific as the submitter gets, and the 'either you know it or "
    "it's over' framing may be rationalising a failure.",
    section="2.5 hours, 3 coding questions")
add(W + "hudson-river-trading-llc/interview/developer",
    "2- Manipulation of a certain data structure\n 3- Code a game, might require an ungodly "
    "amount of code",
    "OA questions 2 and 3: manipulation of a certain data structure, and code a game that may "
    "require an ungodly amount of code",
    "coding_algorithms", "Hudson River Trading", "quant_developer", "unknown",
    "online_assessment", "OA with 2.5 hours for 3 coding questions", "2023-12",
    "Neither question is actually stated; 'a certain data structure' names nothing.",
    section="2.5 hours, 3 coding questions")
add(W + "hudson-river-trading-llc/interview/engineer",
    "Did an OA, which consisted of 3 hard LC problems. Two of them were related to 2D DP, one "
    "just had a lot of edge cases.",
    "OA of 3 hard LeetCode-style problems: two on 2D dynamic programming, one heavy on edge "
    "cases",
    "coding_algorithms", "Hudson River Trading", "quant_developer", "unknown",
    "online_assessment", "an OA", "2022-11",
    "Topic labels only; 'hard LC' is the submitter's difficulty calibration.")
add(W + "hudson-river-trading-llc/interview/algo-developer",
    "Started with two phone discussions with HR and another also developer. I was asked some "
    "statistics brainteasers in the phone interview. The final round was scheduled for 5 "
    "1-on-1 interviews with other Quants and Algo Developers. First one was a coding interview; "
    "second was a brainteaser focused interview.",
    "Final round of 5 1-on-1s with Quants and Algo Developers: first a coding interview, second "
    "a brainteaser-focused interview",
    "logic_brainteaser", "Hudson River Trading", "quant_developer", "unknown", "onsite",
    "The final round", "2022-06",
    "The submitter was cut after 2 of the 5 interviews, so their account of the round structure "
    "beyond those two is second-hand from the schedule they were given.",
    section="5 1-on-1 interviews")
add(W + "hudson-river-trading-llc/interview/quant-research-intern",
    "First was a Math Technical Interview, followed by a Coding Interview. Final Onsite "
    "consists of 4-5 interviews including data analysis, coding and math",
    "HRT quant research intern pipeline: Math Technical Interview, then Coding Interview, then "
    "a 4-5 interview onsite covering data analysis, coding and math",
    "other", "Hudson River Trading", "quant_researcher", "internship", "onsite",
    "Final Onsite", "2024-11",
    "Structure only, no questions; the onsite composition may be what the recruiter described "
    "rather than what the submitter sat.",
    section="4-5 interviews")
add(W + "hudson-river-trading-llc/interview/intern-1",
    "there was a resume review first, followed by a behavioural screen then 3 consecutive "
    "technical rounds",
    "HRT internship pipeline: resume review, behavioural screen, then 3 consecutive technical "
    "rounds",
    "other", "Hudson River Trading", "unknown", "internship", "onsite",
    "3 consecutive technical rounds", "2026-01",
    "A single sentence with no role track named and no question content, but it is one of the "
    "few 2026-cycle HRT datapoints.",
    section="3 consecutive technical rounds")

# --------------------------------------------------------------------------- DRW
add(W + "drw/interview/qt-intern",
    "First an online test consisting of 6 hard math questions, ranging from fundamental linear "
    "algebra, statistics and calculus. One of the questions is impossible to solve, left it "
    "blank. Still got to the next round.",
    "Online test of 6 hard math questions across fundamental linear algebra, statistics and "
    "calculus",
    "linear_algebra", "DRW", "quant_trader", "internship", "online_assessment",
    "an online test", "2023-12",
    "'Impossible to solve' is the submitter's judgement of one question they could not do; "
    "none of the six is stated.",
    section="6 hard math questions")
add(W + "drw/interview/qt-intern",
    "Then phone interview and 1 on 1 interviews consist of pair coding/statistics/machine "
    "learning discussions",
    "Phone and 1-on-1 interviews consisting of pair coding, statistics and machine learning "
    "discussions",
    "ml_modeling", "DRW", "quant_trader", "internship", "phone_technical",
    "phone interview and 1 on 1 interviews", "2023-12",
    "Topic list only, and ML in a QT-intern loop is unusual enough to be worth doubting.")
add(W + "drw/interview/quant-intern",
    "Then there was a 6 question OA which consisted of math/stats questions. Then 1-1 technical "
    "interview, where they asked more math/stat questions, and sometimes even market making "
    "questions.\n One of the questions in the interview was the apples and oranges question.",
    "The apples and oranges question",
    "logic_brainteaser", "DRW", "quant_trader", "internship", "phone_technical",
    "1-1 technical interview", "2024-09",
    "The submitter names the puzzle by nickname only - 'the apples and oranges question' - "
    "without stating it, and it is a classic mislabelled-boxes brainteaser found in every "
    "puzzle book, so the wording DRW used is unknown.",
    section="6 question OA before it")
add(W + "drw/interview/quant-intern-0",
    "OA consisting of maths and stats questions 45mins long. recruiter screen based on "
    "motivations, technical interview based on normal distribution and market making, final "
    "round consisting of machine learning data task and two back to back technical interviews "
    "with prob and stats",
    "Technical interview on the normal distribution and market making; final round is a machine "
    "learning data task plus two back-to-back prob/stats interviews",
    "market_making", "DRW", "quant_trader", "internship", "onsite",
    "final round", "2025-10",
    "One run-on sentence covering four stages; the 45-minute OA length matches other DRW "
    "reports, but no individual question appears.",
    section="OA 45 mins")
add(W + "drw/interview/quant-trading-intern-2",
    "Online assessment involving mathematics questions and brainteasers (linear algebra, matrix "
    "calculations, statistics + markov chains, probability brainteasers etc.). Followed by "
    "technical phone interview on EV calculations, market making, and mathematical modeling.",
    "OA topics: linear algebra, matrix calculations, statistics with Markov chains, probability "
    "brainteasers; then a technical phone interview on EV calculations, market making and "
    "mathematical modeling",
    "linear_algebra", "DRW", "quant_trader", "internship", "online_assessment",
    "Online assessment", "2025-09",
    "A topic inventory rather than questions, though it is the most granular DRW OA topic list "
    "in the set and is consistent with the 6-question/45-minute format others report.")
add(W + "drw/interview/full-time",
    "On-site superday after take-home assignment. Most interviews went alright, one graph "
    "problem in particular was quite difficult; interviewers seemed to be averse to any "
    "feedback from my end.",
    "A graph problem at the on-site superday, described as quite difficult",
    "coding_algorithms", "DRW", "unknown", "unknown", "superday",
    "On-site superday", "2020-09",
    "The graph problem is mentioned but not stated, and the submitter's complaint about "
    "interviewers colours the account.")

# --------------------------------------------------------------------- Two Sigma
add(W + "two-sigma-investments/interview/junior-quant-researcher",
    "Three rounds of tech interviews. One is like model design- predict rent prices in "
    "Manhattan. Then live coding and states. Stats round is about proof of OLS/optimizaition/"
    "Langrange, etc, quite difficult",
    "Model design round: predict rent prices in Manhattan",
    "ml_modeling", "Two Sigma", "quant_researcher", "new_grad", "onsite",
    "Three rounds of tech interviews", "2025-11",
    "The 'Junior Quant Researcher' title is the submitter's own and may be a new-grad or an "
    "early-experienced role; the rent-prices prompt is widely reported for Two Sigma, so it may "
    "be repeated from others rather than sat.",
    section="three rounds")
add(W + "two-sigma-investments/interview/junior-quant-researcher",
    "Stats round is about proof of OLS/optimizaition/Langrange, etc, quite difficult",
    "Stats round: proofs around OLS, optimization and Lagrange multipliers",
    "statistics_regression", "Two Sigma", "quant_researcher", "new_grad", "onsite",
    "Stats round", "2025-11",
    "Topic list with typos ('optimizaition', 'Langrange'), no actual proof statement given.")
add(W + "two-sigma-investments/interview/none",
    "First received OA, 3 hr for 2 coding tests + 1 bonus coding. first one is about writing a "
    "regression algorithm from scratch, second one using pandas package to solve some "
    "datascience problems. bonus question is a follow up for Q2",
    "OA: write a regression algorithm from scratch; then use pandas to solve data science "
    "problems; bonus is a follow-up to the second",
    "statistics_regression", "Two Sigma", "quant_researcher", "unknown", "online_assessment",
    "OA", "2024-10",
    "The submission has no job title at all on WSO (the slug is literally 'none'), so the role "
    "track is inferred from the content.",
    section="3 hr for 2 coding tests + 1 bonus coding")
add(W + "two-sigma-investments/interview/quantitative-researcher-5",
    "I received an online assessment that tested coding and statistics ability (e.g., "
    "efficiently implementing linear regression). From there, I had a probability interview "
    "(which is non-standard, I think).",
    "OA testing coding and statistics ability, e.g. efficiently implementing linear regression",
    "statistics_regression", "Two Sigma", "quant_researcher", "unknown", "online_assessment",
    "an online assessment", "2025-11",
    "Corroborates the 'implement regression from scratch' OA reported a year earlier, but the "
    "submitter's parenthetical '(which is non-standard, I think)' shows they are guessing about "
    "the process.")
add(W + "two-sigma-investments/interview/quant-research-intern",
    "So it began with an online assessment of around 2-3 leetcode style hard questions, then to "
    "an open ended data science question (they ask pretty broad things).",
    "OA of around 2-3 LeetCode-style hard questions, then an open-ended data science question",
    "coding_algorithms", "Two Sigma", "quant_researcher", "internship", "online_assessment",
    "an online assessment", "2024-11",
    "'Around 2-3' shows the submitter is not sure of the count, and no question is given.")
add(W + "two-sigma-investments/interview/qr-intern",
    "Coding test, resume screen, then final technical round consisting of one coding, one "
    "stats, and one data science round. then another round with 2-3 hiring managers.",
    "Two Sigma QR intern final technical round: one coding, one stats and one data science "
    "round, then a round with 2-3 hiring managers",
    "other", "Two Sigma", "quant_researcher", "internship", "onsite",
    "final technical round", "2025-08",
    "Pipeline description with no questions.")
add(W + "two-sigma-investments/interview/quant-research-intern-0",
    "The first round focuses on statistics, where they ask standard modeling questions and then "
    "build on your responses. The final stage has two rounds: the first covers math and the "
    "second covers coding. Both are fairly basic.",
    "First round on statistics with standard modeling questions built on your responses; final "
    "stage is a math round and a coding round",
    "statistics_regression", "Two Sigma", "quant_researcher", "internship", "onsite",
    "The final stage", "2023-09",
    "'Fairly basic' contradicts most other Two Sigma QR reports, so either this submitter is "
    "unusually strong or the loop varied.")
add(W + "two-sigma-investments/interview/researcher",
    "During the interview I was asked a very open ended question about how I would make money "
    "using social media data.",
    "How would you make money using social media data?",
    "ml_modeling", "Two Sigma", "quant_researcher", "unknown", "phone_technical",
    "a conversation with a researcher there", "2024-01",
    "A single sentence recall of an open-ended prompt; the submitter says they got no feedback, "
    "so there is no confirmation the round was even scored as technical.")
add(W + "two-sigma-investments/interview/ai-research-scientist",
    "Take home OA. Onsite 5 rounds. Morning 1 math 1 coding 1 open ended. Afternoon open ended "
    "/ resume with hiring managers.",
    "Onsite of 5 rounds: morning is 1 math, 1 coding, 1 open ended; afternoon is open ended and "
    "resume with hiring managers",
    "other", "Two Sigma", "quant_researcher", "experienced", "onsite",
    "Onsite 5 rounds", "2023-02",
    "Telegraphic note-form entry with no questions; the AI Research Scientist track may not "
    "share a loop with the quant research pipeline.")

# ------------------------------------------------------------ Old Mission Capital
add(W + "old-mission-capital/interview/trading-intern-3",
    "Tough interview had several tough probability questions. I was able to solve most of them. "
    "There were 7 questions and they all had to do with probability distributions.",
    "7 questions, all on probability distributions",
    "probability", "Old Mission Capital", "quant_trader", "internship", "phone_technical",
    "Tough interview", "2018-09",
    "Only the count and the topic are given; 'I was able to solve most of them' is unverifiable "
    "self-assessment.",
    section="There were 7 questions")
add(W + "old-mission-capital/interview/trader-intern",
    "Applied online through university job board. Phone interview included arithmetic "
    "operations that was supposed to be done without pen or paper.",
    "Phone interview with arithmetic operations to be done without pen or paper",
    "mental_math_speed", "Old Mission Capital", "quant_trader", "internship", "phone_technical",
    "Phone interview", "unknown",
    "WSO carries no interview date for this submission at all, so it cannot be placed in a "
    "cycle.")
add(W + "old-mission-capital/interview/floor-trader",
    "Basic behavioral/situational questions, why Old Mission, what would you do in x situations "
    "(read job description), going over details of the interview process and the role, "
    "logistics mostly.",
    "Recruiter call: why Old Mission, and what would you do in x situations",
    "behavioral", "Old Mission Capital", "quant_trader", "unknown", "phone_technical",
    "a call with a recruiter", "2025-04",
    "Behavioral only; included because Old Mission coverage is thin and this is one of the few "
    "2025 datapoints, not because it carries a technical question.")
add(W + "old-mission-capital/interview/floor-trader",
    "Was told market making portion of the interview was too weak.",
    "A market making portion of the interview (feedback given was that it was too weak)",
    "market_making", "Old Mission Capital", "quant_trader", "unknown", "onsite",
    "call with head of desk at Old Mission", "2025-04",
    "Establishes that a market-making component exists in the Floor Trader loop but says "
    "nothing about its content or which round it sat in - the submitter themselves says they "
    "cannot confirm which round was last.")

# -------------------------------------------------------------------- Jump Trading
add(W + "jump-trading/interview/quant-research-intern",
    "At the onsite, they gave a presentation on the quant research internship. I had two quant "
    "interviews each 45 minutes I think it was, plus one programming interview that was an hour.",
    "Onsite: two 45-minute quant interviews plus one hour-long programming interview",
    "other", "Jump Trading", "quant_researcher", "internship", "onsite",
    "the onsite", "2018-11",
    "'each 45 minutes I think it was' is explicitly hedged, and no question content survives.",
    section="two quant interviews + one programming interview")
add(W + "jump-trading/interview/algorithmic-trading-intern",
    "Another was purely mathematical/linear algebra done on the whiteboard. The third and "
    "fourth were pen/paper brainteaser and math/probability questions.",
    "Superday rounds: one purely mathematical/linear algebra on the whiteboard, then two "
    "pen-and-paper brainteaser and math/probability rounds",
    "linear_algebra", "Jump Trading", "quant_trader", "internship", "superday",
    "a full day consisting of 4 interviews", "2013-03",
    "From 2013, so the loop has almost certainly changed; no individual question is given.",
    section="4 interviews, one C++ coding on a laptop")
add(W + "jump-trading/interview/quant-researcher",
    "He focused heavily on my PhD research and drilled in several details, asking \"why would "
    "you do this instead of that\" type of questions. Then he asked one question of probability "
    "which can be solved by Bayesian formula.",
    "One probability question solvable by Bayes' formula, after a deep drill on the candidate's "
    "PhD research",
    "probability", "Jump Trading", "quant_researcher", "experienced", "phone_technical",
    "contacted by a quantitative researcher in Chicago", "2018-02",
    "The question is identified only by the method that solves it, not by its statement.")
add(W + "jump-trading/interview/jump-trading",
    "On-campus recruiting process: initial interview was a whiteboard interview with two other "
    "engineers and if you passed that one, there was a full day of onsite interviews at its "
    "Chicago office",
    "On-campus: whiteboard interview with two engineers, then a full day of onsites in Chicago",
    "other", "Jump Trading", "quant_developer", "unknown", "onsite",
    "On-campus recruiting process", "2017-09",
    "Process shape only; from 2017 and with no role level stated.", office="Chicago")

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("%d records -> %s" % (len(rows), OUT))
