#!/usr/bin/env python3
"""p11: Wall Street Oasis firm pages (fetched through r.jina.ai because WSO is behind
Cloudflare) plus the DRW Glassdoor company page returned as full text by the search tool.

WSO entries carry two dates: 'Interviewed:' (when the interview happened) and
'Date Submitted:' (when it was written up). I use the interview month for post_date
because that is what dates the question, and put both in poster_context.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p11_wso_new_drw_gd.jsonl")
rows = []


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
    rows.append(rec)


WSO_DOUBT = ("WSO interview entries are anonymous and unverified; the poster writes them up "
             "months after the fact (the 'Date Submitted' here trails the interview month), so "
             "wording is recalled rather than transcribed.")

U_AK = "https://www.wallstreetoasis.com/company/akuna-capital-llc/interview"
U_DRW = "https://www.wallstreetoasis.com/company/drw/interview"
U_FR = "https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview"
U_HRT = "https://www.wallstreetoasis.com/company/hudson-river-trading-llc/interview"
U_JT = "https://www.wallstreetoasis.com/company/jump-trading/interview"
U_OM = "https://www.wallstreetoasis.com/company/old-mission-capital/interview"

# ============================== Akuna Capital ==============================
add(firm="Akuna Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="Chicago", round="superday",
    round_name="Top performers of the Akuna 201 course get expedited to the final rounds",
    section_context="The course lasts 5 days and there is a quiz each day",
    question_type="mental_math_speed",
    question_text="Mental math (2x2 operations), series, and probability.",
    source_url=U_AK,
    source_quote="Top performers of the Akuna 201 course get expedited to the final rounds. The course lasts 5 days and there is a quiz each day. Had to do an HR zoom interview before the final round. HR interview consisted of very basic questions such as \"why akuna\"/ \"why trading\".",
    post_date="2026-04", poster_context=(
        "Anonymous interview candidate in Chicago, Junior Trader Interview - Sales and Trading; "
        "Interviewed: April 2026, Date Submitted: May 05, 2026, No Offer, Applied Online, "
        "process 1-2 months"),
    doubt=WSO_DOUBT + " The listed question is a three-item topic label rather than a problem; its value is the Akuna 201 course detail (5 days, daily quiz, top performers expedited) in the narrative.")

add(firm="Akuna Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="Chicago", round="online_assessment", round_name="received math test",
    section_context="math test 80 questions, the math test was based on arithmetic questions mental math",
    question_type="mental_math_speed",
    question_text="Doing mental math without paper pen and no calculators allowed",
    source_url=U_AK,
    source_quote="Applied online, received math test 80 questions, the math test was based on arithmetic questions mental math.",
    post_date="2025-11", poster_context=(
        "Anonymous interview candidate in Chicago, Junior trader Interview - Sales and Trading; "
        "Interviewed: November 2025, Date Submitted: Mar 12, 2026, No Offer, Applied Online, "
        "process less than 1 month"),
    doubt=WSO_DOUBT + " No individual problem is given — the entry attests the format (80 arithmetic questions, no calculator, then a separate expected-value probability test) rather than any question.")

add(firm="Akuna Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="Chicago", round="online_assessment", round_name="a probability test",
    section_context="This was followed by a probability test, involved calculating expected value questions of events",
    question_type="expected_value",
    question_text="This was followed by a probability test, involved calculating expected value questions of events",
    source_url=U_AK,
    source_quote="This was followed by a probability test, involved calculating expected value questions of events",
    post_date="2025-11", poster_context=(
        "Anonymous interview candidate in Chicago, Junior trader Interview - Sales and Trading; "
        "Interviewed: November 2025, Date Submitted: Mar 12, 2026, No Offer"),
    doubt=WSO_DOUBT + " A description of the section, not a question; recorded because it pins Akuna's second-stage screen as expected-value probability rather than more mental math.")

add(firm="Akuna Capital", role_track="quant_researcher", level="internship", cycle="unknown",
    office="New York", round="online_assessment",
    round_name="Online assessment followed by video interview",
    section_context="OA was straightforward python leetcode-style questions, however the video interview was nontraditional requiring you to verbally work through ~7 recorded math questions",
    question_type="other", question_text="Convergence time of newton's method",
    source_url=U_AK,
    source_quote="Online assessment followed by video interview. OA was straightforward python leetcode-style questions, however the video interview was nontraditional requiring you to verbally work through ~7 recorded math questions.",
    post_date="2025-10", poster_context=(
        "Anonymous interview candidate in New York, Quantitative Research Intern Interview - "
        "Quantitative Research; Interviewed: October 2025, Date Submitted: Nov 30, 2025, No Offer, "
        "Applied Online, process less than 1 month"),
    doubt=WSO_DOUBT + " 'Convergence time of newton's method' is a four-word topic, so the actual prompt is lost; the recorded-video format (~7 verbal math questions) matches Akuna's known VidCruiter-style screen but the poster does not name the platform.")

add(firm="Akuna Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="Chicago", round="online_assessment", round_name="a math assessment",
    section_context="It was timed mental math problems where you oculd not use a calulator. The test was around 70 questions and soon got harder as the questions went on.",
    question_type="mental_math_speed",
    question_text="The mental math problems which were timed, one example was the 56*56",
    source_url=U_AK,
    source_quote="It was timed mental math problems where you oculd not use a calulator. The test was around 70 questions and soon got harder as the questions went on. The second part of the exam was sceniors to see if you make quick decisions.",
    post_date="2025-07", poster_context=(
        "Anonymous interview candidate in Chicago, Junior Trader Interview - Prop Trading; "
        "Interviewed: July 2025, Date Submitted: Sep 01, 2025, No Offer, applied on LinkedIn"),
    doubt=WSO_DOUBT + " Only one concrete item (56*56) survives out of ~70; the rest is described in the aggregate.")

# ============================== DRW ==============================
add(firm="DRW", role_track="unknown", level="unknown", cycle="unknown", office="Chicago",
    round="superday", round_name="On-site superday after take-home assignment",
    question_type="coding_algorithms",
    question_text="One graph problem that I to this day don't know how to do",
    source_url=U_DRW,
    source_quote="On-site superday after take-home assignment. Most interviews went alright, one graph problem in particular was quite difficult; interviewers seemed to be averse to any feedback from my end.",
    post_date="2020-09", poster_context=(
        "Anonymous interview candidate in Chicago, Full Time Interview - Generalist; "
        "Interviewed: September 2020, Date Submitted: Jul 02, 2026, No Offer, "
        "College / University / On Campus Recruiting"),
    doubt=WSO_DOUBT + " The poster explicitly cannot state the problem ('I to this day don't know how to do'), so no content is recoverable; the write-up also lands almost six years after the interview.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="London",
    round="online_assessment",
    round_name="Got a online assesment which consisted of math, statistics, and probability theory",
    question_type="probability",
    question_text="eg. one question was about markov chains but I don't remember any other specific ones",
    source_url=U_DRW,
    source_quote="Got a online assesment which consisted of math, statistics, and probability theory (eg. one question was about markov chains but I don't remember any other specific ones).",
    post_date="2026-10", poster_context=(
        "Anonymous interview candidate in London, Trader Intern Interview; Interviewed: "
        "October 2026, Date Submitted: Jan 11, 2026, No Offer, Applied Online"),
    doubt=WSO_DOUBT + " The poster says outright they remember only the topic ('markov chains'). The dates are also internally inconsistent — WSO shows Interviewed: October 2026 but Date Submitted: Jan 11, 2026, i.e. submitted before the stated interview.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="London",
    round="phone_technical", round_name="a short phone interview with a recruiter. Behavioural and mental math.",
    question_type="behavioral",
    question_text="Tell me about a time when you had to work in a group towards a common goal",
    source_url=U_DRW,
    source_quote="Did well on that and got a short phone interview with a recruiter. Behavioural and mental math.",
    post_date="2026-10", poster_context=(
        "Anonymous interview candidate in London, Trader Intern Interview; Interviewed: "
        "October 2026, Date Submitted: Jan 11, 2026, No Offer, Applied Online"),
    doubt=WSO_DOUBT + " Same entry with the contradictory interview/submission dates noted above; this behavioural prompt is generic enough to be boilerplate.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="London",
    round="phone_technical",
    round_name="technical interview based on normal distribution and market making",
    section_context="OA consisting of maths and stats questions 45mins long",
    question_type="market_making",
    question_text="Make me a market on the amount of diapers used in the UK daily",
    source_url=U_DRW,
    source_quote="OA consisting of maths and stats questions 45mins long. recruiter screen based on motivations, technical interview based on normal distribution and market making, final round consisting of machine learning data task and two back to back technical interviews with prob and stats",
    post_date="2025-10", poster_context=(
        "Anonymous interview candidate in London, Quant Intern Interview - Trading; Interviewed: "
        "October 2025, Date Submitted: Nov 08, 2025, No Offer, Applied Online, process 1-2 months"),
    doubt=WSO_DOUBT + " The poster does not say which of the several technical rounds the diaper market-making question came from; I attribute it to the market-making technical round they describe, which is inference.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="unknown",
    round="online_assessment",
    round_name="First an online test consisting of 6 hard math questions",
    section_context="ranging from fundamental linear algebra, statistics and calculus. One of the questions is impossible to solve, left it blank. Still got to the next round.",
    question_type="coding_algorithms",
    question_text="Please write me a binary search to qucikly locate timstamps",
    source_url=U_DRW,
    source_quote="First an online test consisting of 6 hard math questions, ranging from fundamental linear algebra, statistics and calculus. One of the questions is impossible to solve, left it blank. Still got to the next round.",
    post_date="2023-12", poster_context=(
        "Anonymous interview candidate, QT intern Interview - Trading; Interviewed: December 2023, "
        "Date Submitted: Oct 24, 2025, No Offer, College / University / On Campus Recruiting"),
    doubt=WSO_DOUBT + " The binary-search question comes from the pair-coding round rather than the 6-question OA the section_context describes, and the write-up lands almost two years after the interview.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="London",
    round="phone_technical", round_name="a behavioral where they asked why DRW, why Quant and some mental math questions",
    section_context="6 Question OA at first", question_type="mental_math_speed",
    question_text="Quite easy behavioral. Just practice mental math",
    source_url=U_DRW,
    source_quote="6 Question OA at first followed by a behavioral where they asked why DRW, why Quant and some mental math questions.",
    post_date="2025-10", poster_context=(
        "Anonymous interview candidate in London, Trading Intern Interview - Generalist; "
        "Interviewed: October 2025, Date Submitted: Oct 19, 2025, No Offer, Applied Online"),
    doubt=WSO_DOUBT + " The 'question' field is advice, not a question; kept because it independently corroborates the 6-question DRW OA format from a second London intern candidate in the same month.")

add(firm="DRW", role_track="quant_trader", level="unknown", cycle="unknown", office="Chicago",
    round="superday", round_name="in person superday. The super day consisted of 3 interviews.",
    question_type="options_theory", question_text="Explain how to price an option",
    source_url=U_DRW,
    source_quote="Had the online math assessment, and then had a zoom interview, then had a in person superday. The super day consisted of 3 interviews.",
    post_date="2025-06", poster_context=(
        "Anonymous employee in Chicago, Quant Trading Analyst Interview - Quantitative Trading; "
        "Interviewed: June 2025, Date Submitted: Oct 16, 2025, Accepted Offer, sourced by Recruiter"),
    doubt=WSO_DOUBT + " The poster does not say which of the three superday interviews asked this, and 'Quant Trading Analyst' with an accepted offer is most likely a full-time role, so I have left level unknown rather than guessing.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="Chicago",
    round="phone_technical",
    round_name="technical phone interview on EV calculations, market making, and mathematical modeling",
    section_context="Online assessment involving mathematics questions and brainteasers (linear algebra, matrix calculations, statistics + markov chains, probability brainteasers etc.)",
    question_type="market_making",
    question_text="Market making and fermi estimation on random quantities",
    source_url=U_DRW,
    source_quote="Online assessment involving mathematics questions and brainteasers (linear algebra, matrix calculations, statistics + markov chains, probability brainteasers etc.). Followed by technical phone interview on EV calculations, market making, and mathematical modeling.",
    post_date="2025-09", poster_context=(
        "Anonymous interview candidate in Chicago, Quant Trading Intern Interview - Quantitative "
        "Trading; Interviewed: September 2025, Date Submitted: Oct 12, 2025, No Offer, "
        "College / University / On Campus Recruiting"),
    doubt=WSO_DOUBT + " A topic label rather than a stated problem; useful mainly as a third independent account of DRW's OA topic mix (linear algebra, matrices, Markov chains, probability brainteasers).")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="London",
    round="phone_technical", round_name="1-1 technical interview",
    section_context="Then there was a 6 question OA which consisted of math/stats questions.",
    question_type="logic_brainteaser",
    question_text="Apples and Oranges question with the mislabeled boxes",
    source_url=U_DRW,
    source_quote="One of the questions in the interview was the apples and oranges question.",
    post_date="2024-09", poster_context=(
        "Anonymous interview candidate in London, Quant Intern Interview - Quant; Interviewed: "
        "September 2024, Date Submitted: Dec 24, 2024, No Offer, Applied Online, process 1-2 months"),
    doubt=WSO_DOUBT + " The mislabeled apples-and-oranges boxes puzzle is a very old standard that appears in every brainteaser collection, so the content is textbook; what supports it here is a dated first-person account naming it as a DRW 1-1 question.")

# ============================== Five Rings ==============================
add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="unknown",
    office="New York", round="phone_technical",
    round_name="The recruiter set up a 1:1 call",
    section_context="a brief behavioral component (why trading? and why five rings?) and then dove into 10 questions each with a 30 second time limit. You are encouraged to solve it as fast as possible, but accuracy is more important.",
    question_type="other",
    question_text="I am not allowed to share any questions due to signing and agreement with the company.",
    source_url=U_FR,
    source_quote="The recruiter set up a 1:1 call which consisted of a brief behavioral component (why trading? and why five rings?) and then dove into 10 questions each with a 30 second time limit.",
    post_date="2024-08", poster_context=(
        "Anonymous interview candidate in New York, Trading Intern Interview - Prop Trading; "
        "Interviewed: August 2024, Date Submitted: Aug 23, 2024, No Offer, Applied Online"),
    doubt=WSO_DOUBT + " The poster deliberately withholds every question citing an agreement with Five Rings, so this contributes only the format (10 questions, 30 seconds each, accuracy over speed) and no content at all.")

add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="unknown",
    office="New York", round="phone_technical",
    round_name="First round was 10 questions with 30 seconds to respond to each round",
    section_context="followed by 3-4 rounds of probability questions",
    question_type="other", question_text="Calculate the length of x^2 from 0 to 9",
    source_url=U_FR,
    source_quote="First round was 10 questions with 30 seconds to respond to each round, followed by 3-4 rounds of probability questions. I made it to the third round, then got rejected even though I had answered all questions correctly.",
    post_date="2024-07", poster_context=(
        "Anonymous interview candidate in New York, Intern Interview - Quant; Interviewed: "
        "July 2024, Date Submitted: Jan 11, 2025, No Offer, "
        "College / University / On Campus Recruiting"),
    doubt=WSO_DOUBT + " 'Length of x^2 from 0 to 9' is presumably the arc length of y = x^2 on [0,9], but the poster does not say so, and a 30-second budget implies an estimate rather than the exact integral.")

# ============================== Hudson River Trading ==============================
add(firm="Hudson River Trading", role_track="quant_researcher", level="internship",
    cycle="unknown", office="New York", round="online_assessment",
    round_name="Online assessment with 3 coding questions on hacker rank",
    platform="HackerRank", section_context="ranging from dp to tree traversal. given 90 minutes",
    question_type="coding_algorithms", question_text="Nothing particularly difficult",
    source_url=U_HRT,
    source_quote="Online assessment with 3 coding questions on hacker rank, ranging from dp to tree traversal. given 90 minutes",
    post_date="2024-10", poster_context=(
        "Anonymous interview candidate in New York, SummerIintern Interview - Quantitative "
        "Research; Interviewed: October 2024, Date Submitted: Oct 20, 2024, No Offer, Applied Online"),
    doubt=WSO_DOUBT + " The poster's answer to 'interview questions' is literally 'Nothing particularly difficult', so no problem is stated; the entry's value is the format (HackerRank, 3 questions, 90 minutes, DP and tree traversal) for a 2024 HRT summer QR intern.")

add(firm="Hudson River Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="New York", round="phone_technical", round_name="phone screen",
    section_context="I had a Hackerrank test. Seems like they look at your profile and only then send the test. Got 3 problems, Leetcode Medium/Hard. Solved all 3 in C++.",
    platform="HackerRank", question_type="expected_value",
    question_text="Questions on EV for coin tosses, law of large numbers, Bayes theorem",
    source_url=U_HRT,
    source_quote="I had a Hackerrank test. Seems like they look at your profile and only then send the test. Got 3 problems, Leetcode Medium/Hard. Solved all 3 in C++. Then received a phone screen. Basic EV questions, problems were variations of problems from the green book.",
    post_date="2020-10", poster_context=(
        "Anonymous interview candidate in New York, Algorithm Developer Interview - Prop Trading; "
        "Interviewed: October 2020, Date Submitted: Oct 22, 2023, No Offer, Applied Online"),
    doubt=WSO_DOUBT + " The poster himself says the problems were 'variations of problems from the green book' (Xinfeng Zhou), so the content is textbook — what carries it is his dated first-person claim that HRT asked green-book variants on the phone screen.")

# ============================== Jump Trading ==============================
add(firm="Jump Trading", role_track="quant_researcher", level="internship", cycle="unknown",
    office="unknown", round="onsite",
    round_name="A single online video interview first, then one full day of online interviews (with 3-4 different people, ~1 hour each)",
    section_context="Math and coding questions", question_type="behavioral",
    question_text="What was the most unreasonable thing that you've ever done?",
    source_url=U_JT,
    source_quote="A single online video interview first, then one full day of online interviews (with 3-4 different people, ~1 hour each). Math and coding questions.",
    post_date="2019-09", poster_context=(
        "Anonymous employee, Quant Research Intern Interview - Quantitative Research; Interviewed: "
        "September 2019, Date Submitted: Sep 09, 2020, Accepted Offer, Applied Online"),
    doubt=WSO_DOUBT + " The one question recorded is behavioural even though the poster says the day was 'math and coding questions', so the technical content of an accepted-offer Jump QR intern loop is missing.")

add(firm="Jump Trading", role_track="quant_developer", level="internship", cycle="unknown",
    office="Cambridge", round="onsite", round_name="an in person technical interview",
    question_type="coding_algorithms",
    question_text="Then I was asked about how I would store key value pairs. And then ended in a discussion about how I would implement a hash map data structure. I was asked about the tradeoffs between various implementations. I had to implement methods to add the key to the hashmap and method to retrieve a key from the hashmap.",
    source_url=U_JT,
    source_quote="No difficult questions, just general questions about my resume, then general questions about C and pointers and arrays. Then I was asked about how I would store key value pairs. And then ended in a discussion about how I would implement a hash map data structure. I was asked about the tradeoffs between various implementations.",
    post_date="2019-08", poster_context=(
        "Anonymous interview candidate in Cambridge, Software Development Internship Interview - "
        "Engineering; Interviewed: August 2019, Date Submitted: Oct 08, 2019, No Offer, "
        "College / University / On Campus Recruiting"),
    doubt=WSO_DOUBT + " A hash-map design discussion is the most generic possible systems question, so nothing here is distinctively Jump.")

add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="Urbana", round="onsite",
    round_name="initial interview was a whiteboard interview with two other engineers",
    section_context="The interview was 45 minutes long and consisted of a straightforward whiteboard question with two separate tasks",
    question_type="coding_algorithms",
    question_text="1. Convert decimal-based number to a 16-bit binary representation\n\n 2. Represent as 4x4 matrix of 0s and 1s\n\n 3. Detect if path of 0s exists in matrix from top left to bottom right cell and if so, print out the path in the format of a string; otherwise, return a \"No path\" string",
    source_url=U_JT,
    source_quote="1. Convert decimal-based number to a 16-bit binary representation",
    post_date="2017-09", poster_context=(
        "Anonymous interview candidate in Urbana, Jump Trading Interview - Software; Interviewed: "
        "September 2017, Date Submitted: Feb 05, 2018, No Offer, "
        "College / University / On Campus Recruiting; on-campus whiteboard round with two engineers"),
    doubt=WSO_DOUBT + " The poster says 'two separate tasks' but then lists three numbered steps, so their own count is inconsistent; my source_quote is only the first step because the three are separated by blank lines in the rendered page and I cannot honestly quote them as one contiguous run.")

add(firm="Jump Trading", role_track="quant_trader", level="internship", cycle="unknown",
    office="Chicago", round="onsite",
    round_name="a superday consisting of 4 interviews",
    section_context="One was a purely coding interview with a laptop in front of me (C++). Another was purely mathematical/linear algebra done on the whiteboard. The third and fourth were pen/paper brainteaser and math/probability questions.",
    question_type="coding_algorithms", question_text="Implement a trie in C++.",
    source_url=U_JT, source_quote="Implement a trie in C++.",
    post_date="2013-03", poster_context=(
        "Anonymous interview candidate in Chicago, Algorithmic Trading Intern Interview - Trading; "
        "Interviewed: March 2013, Date Submitted: Jan 06, 2014, No Offer, "
        "College / University / On Campus Recruiting; flown to Chicago for the final round"),
    doubt=WSO_DOUBT + " The interview is from 2013, so it says little about Jump's current intern process.")

add(firm="Jump Trading", role_track="quant_trader", level="internship", cycle="unknown",
    office="Chicago", round="onsite", round_name="a superday consisting of 4 interviews",
    question_type="logic_brainteaser",
    question_text="Swap two variables without additional storage (i.e. no using a temp).",
    source_url=U_JT,
    source_quote="Swap two variables without additional storage (i.e. no using a temp).",
    post_date="2013-03", poster_context=(
        "Anonymous interview candidate in Chicago, Algorithmic Trading Intern Interview - Trading; "
        "Interviewed: March 2013, Date Submitted: Jan 06, 2014, No Offer"),
    doubt=WSO_DOUBT + " Standard XOR-swap trivia from 2013, and the poster does not say which of the four superday rounds asked it.")

add(firm="Jump Trading", role_track="quant_trader", level="internship", cycle="unknown",
    office="Chicago", round="onsite", round_name="a superday consisting of 4 interviews",
    question_type="combinatorics",
    question_text="How many 0's are in 1000! (factorial)?",
    source_url=U_JT, source_quote="How many 0's are in 1000! (factorial)?",
    post_date="2013-03", poster_context=(
        "Anonymous interview candidate in Chicago, Algorithmic Trading Intern Interview - Trading; "
        "Interviewed: March 2013, Date Submitted: Jan 06, 2014, No Offer"),
    doubt=WSO_DOUBT + " A textbook trailing-zeros counting problem, from 2013; the poster attributes it to the pen-and-paper brainteaser rounds but does not say which.")

# ============================== Old Mission Capital ==============================
add(firm="Old Mission Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="Chicago", round="phone_technical",
    round_name="interviewed with a Floor Trader at Old Mission",
    question_type="market_making", question_text="Market Making Questions",
    source_url=U_OM,
    source_quote="Behavioral/situational questions: how would you react if x happened in the trading pit? How do you handle stress and criticism? Some basic mental math, fermi questions, and options strategy (which options or combinations of options to buy when).",
    post_date="2025-04", poster_context=(
        "Anonymous interview candidate in Chicago, Floor Trader Interview - Prop Trading; "
        "Interviewed: April 2025, Date Submitted: Jun 16, 2025, No Offer, Applied Online, "
        "process 2-3 months"),
    doubt=WSO_DOUBT + " 'Market Making Questions' is a bare label; the narrative is richer than the question field, which is why my quote is taken from the narrative.")

add(firm="Old Mission Capital", role_track="quant_researcher", level="internship", cycle="unknown",
    office="New York", round="phone_technical",
    round_name="Phone interview questions were mostly mental math, probability, and statistics",
    question_type="probability",
    question_text="What is the probability of drawing a 4 of a kind in a 5 card poker hand?",
    source_url=U_OM,
    source_quote="What is the probability of drawing a 4 of a kind in a 5 card poker hand?",
    post_date="2014-03", poster_context=(
        "Anonymous interview candidate in New York, Quantitative Research Intern Interview - "
        "Quantitative Research; Interviewed: March 2014, Date Submitted: Feb 28, 2015, No Offer, "
        "Applied Online"),
    doubt=WSO_DOUBT + " The poster says outright that 'Some questions seemed to come straight from popular quant interview study books', and this is one of them; it is included because a dated first-person account attributes it to Old Mission, not because the content is novel. The interview is also from 2014.")

# ============================== DRW — Glassdoor company page ==============================
DRW_GD = "https://www.glassdoor.com/Interview/DRW-Interview-Questions-E235115.htm"
GD_DOUBT = ("Glassdoor entries are anonymous and self-reported with no verification. Glassdoor "
            "blocks direct fetching from this box; this text arrived as a complete page-text dump "
            "from the search tool and was saved into the verifier cache.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="unknown",
    round="online_assessment", round_name="OA with 6 probability questions",
    section_context="some easy some really tough. Need to get 5/6 to pass, maybe 6/6 correct.",
    question_type="probability",
    question_text="OA with 6 probability questions, some easy some really tough. Need to get 5/6 to pass, maybe 6/6 correct.",
    source_url=DRW_GD, source_type="glassdoor",
    source_quote="OA with 6 probability questions, some easy some really tough. Need to get 5/6 to pass, maybe 6/6 correct. R1 Interview of typical behaviorals + probability math question with proof.",
    post_date="2025-04-17", access="full_text", retrieval_method="websearch_snippet",
    poster_context="Anonymous Interview Candidate, Quant Trader Intern Interview, Apr 17, 2025, No offer, Positive experience, Difficult interview",
    doubt=GD_DOUBT + " No individual problem is stated. The pass bar ('need to get 5/6') is the poster's guess — they were rejected, so they cannot know the threshold.")

add(firm="DRW", role_track="quant_trader", level="internship", cycle="unknown", office="unknown",
    round="phone_technical", round_name="R1 Interview of typical behaviorals + probability math question with proof",
    question_type="probability",
    question_text="R1 Interview of typical behaviorals + probability math question with proof.",
    source_url=DRW_GD, source_type="glassdoor",
    source_quote="R1 Interview of typical behaviorals + probability math question with proof.",
    post_date="2025-04-17", access="full_text", retrieval_method="websearch_snippet",
    poster_context="Anonymous Interview Candidate, Quant Trader Intern Interview, Apr 17, 2025, No offer, Difficult interview",
    doubt=GD_DOUBT + " Describes the round rather than the problem; notable only because it says DRW asked for a proof, which distinguishes R1 from the numeric OA.")

add(firm="DRW", role_track="quant_developer", level="unknown", cycle="unknown", office="unknown",
    round="take_home", round_name="Take home coding assignment —given a week or so to complete",
    section_context="No test cases were provided which made it trickier. Took maybe a few hours in total",
    question_type="coding_algorithms",
    question_text="Implement a game according to some specs. No test cases given",
    source_url=DRW_GD, source_type="glassdoor",
    source_quote="Take home coding assignment —given a week or so to complete. Wasn't too hard but didn't receive offer. No test cases were provided which made it trickier. Took maybe a few hours in total",
    post_date="2025-05-22", access="full_text", retrieval_method="websearch_snippet",
    poster_context="Anonymous Interview Candidate, Software Engineer Interview, May 22, 2025, No offer, Neutral experience, Average interview",
    doubt=GD_DOUBT + " The poster never says which game or what the specs were, so only the format survives.")

add(firm="DRW", role_track="unknown", level="internship", cycle="unknown", office="London, England",
    round="unknown", round_name="Intern Interview", question_type="statistics_regression",
    question_text="My research project related questions",
    source_url=DRW_GD, source_type="glassdoor",
    source_quote="They ask me about data analysis, statistics and coding questions.",
    post_date="2025-04-26", access="full_text", retrieval_method="websearch_snippet",
    poster_context="Anonymous employee in London, England, Intern Interview, Apr 26, 2025, Accepted offer, Positive experience, Difficult interview",
    doubt=GD_DOUBT + " Most of this entry is about the office and the lifts; the question field is a bare label and the role track is not stated, so I left it unknown.")

add(firm="DRW", role_track="quant_developer", level="internship", cycle="unknown",
    office="London, England", round="onsite",
    round_name="a few rounds and many one on one interviews with engineers",
    question_type="behavioral", question_text="Why do you want to work here?",
    source_url=DRW_GD, source_type="glassdoor",
    source_quote="The interview process consists of a few rounds and many one on one interviews with engineers who ask leetcode style questions and ask about knowledge of low levem systems too.",
    post_date="2025-05-18", access="full_text", retrieval_method="websearch_snippet",
    poster_context="Anonymous employee in London, England, Software Engineering Intern Interview, May 18, 2025, Accepted offer, Positive experience, Difficult interview",
    doubt=GD_DOUBT + " The recorded question is the behavioural one; the LeetCode-style and low-level-systems content the poster mentions is not written down.")


with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
