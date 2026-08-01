#!/usr/bin/env python3
"""p12: DRW Glassdoor per-job-title interview pages, fetched through r.jina.ai
(glassdoor.com refuses this box directly). These are the internship-track pages, so
almost every record here is level=internship.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p12_drw_glassdoor.jsonl")
rows = []


def add(**kw):
    rec = {
        "firm": "DRW", "role_track": "quant_trader", "level": "internship", "cycle": "unknown",
        "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
        "section_context": None, "question_type": "other", "question_text": None,
        "question_text_en": None, "reported_answer": None, "source_url": None,
        "source_type": "glassdoor", "source_quote": None, "source_language": "en",
        "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": None, "doubt": None,
    }
    rec.update(kw)
    for k in ("question_text", "source_url", "source_quote", "doubt"):
        assert rec[k], "missing %s" % k
    rows.append(rec)


QTI = ("https://www.glassdoor.com/Interview/DRW-Quant-Trader-Intern-Interview-Questions-"
       "EI_IE235115.0,3_KO4,23.htm")
QGI = ("https://www.glassdoor.com/Interview/DRW-Quant-Trading-Intern-Interview-Questions-"
       "EI_IE235115.0,3_KO4,24.htm")
QQI = ("https://www.glassdoor.com/Interview/DRW-Quantitative-Trading-Intern-Interview-Questions-"
       "EI_IE235115.0,3_KO4,31.htm")
TIN = ("https://www.glassdoor.com/Interview/DRW-Trading-Intern-Interview-Questions-"
       "EI_IE235115.0,3_KO4,18.htm")

GD = ("Glassdoor interview entries are anonymous and unverified self-reports; the reviewer "
      "supplies the date but nothing confirms the interview happened. Glassdoor blocks direct "
      "fetching from this box, so the page came through the r.jina.ai proxy.")

# ------------------------------- Quant Trader Intern -------------------------------
add(source_url=QTI, round="superday",
    round_name="Oa + behavior + technical + superday superday includes 2 interviews",
    question_type="market_making", question_text="MM games for country population",
    source_quote="Oa + behavior + technical + superday superday includes 2 interviews. one of the interviews is very hard cant even tell you how to do it. kinda random. hard to prepare",
    post_date="2026-06-26",
    poster_context="Anonymous Interview Candidate, Quant Trader Intern Interview, Jun 26, 2026, No offer, Positive experience, Difficult interview",
    doubt=GD + " 'MM games for country population' is a five-word gloss — presumably make a market on some country's population, but the poster never says which country or what the quoting rules were.")

add(source_url=QTI, office="London, England", round="phone_technical",
    round_name="1st round based on CV, market making , math based probability and kelly criterion",
    section_context="OA, 1st round based on CV, market making , math based probability and kelly criterion then optional second round more on math and options maybe",
    question_type="poker_game_theory",
    question_text=("So, let's start with a game where you pick a number between 0 and 100, can be "
                   "any real number, and your opponent also picks a number between 0 and 100. "
                   "Whoever picks the lowest number wins, and the winning amount is the amount of "
                   "the lower number in dollars. So, let's say, if you pick 10, I pick 20, you "
                   "win, and you win 10 dollars. If you pick 10 and I pick 5, then I win, and I "
                   "win 5 dollars. If your opponent wins, then you don't win almost anything, and "
                   "your KNO is 0. So, now imagine yourself, a human person, you're playing "
                   "against a robot. That robot picks a number between 0 and 100 uniformly at "
                   "random. And my question is, what is the strategy here?"),
    source_quote=("So, let's start with a game where you pick a number between 0 and 100, can be "
                  "any real number, and your opponent also picks a number between 0 and 100. "
                  "Whoever picks the lowest number wins, and the winning amount is the amount of "
                  "the lower number in dollars."),
    post_date="2025-09-18",
    poster_context="Anonymous Interview Candidate in London, England, Quant Trader Intern Interview, Sep 18, 2025, No offer, Positive experience, Difficult interview",
    doubt=GD + " The transcript reads as if dictated live, and 'your KNO is 0' is garbled — most likely 'your P&L is 0' or 'your payoff is 0' misheard by speech-to-text — so that clause of the payoff rule is uncertain. Glassdoor also truncates the display with a 'read more' link, so the quote I can verify is the opening run rather than the whole prompt.")

add(source_url=QTI, office="Chicago, IL", round="phone_technical",
    round_name="First round technical interview", question_type="expected_value",
    question_text="Asked me about some expected value, using the knowledge of Confidence Interval and the variance formula.",
    source_quote="First round technical interview: Asked me about some expected value, using the knowledge of Confidence Interval and the variance formula. Not so hard, but will do better if prepared beforehand.",
    post_date="2025-09-13",
    poster_context="Anonymous Interview Candidate in Chicago, IL, Quant Trader Intern Interview, Sep 13, 2025, No offer, Positive experience, Average interview",
    doubt=GD + " Describes the topics (expected value, confidence interval, variance formula) without stating the problem.")

# ------------------------------- Quant Trading Intern -------------------------------
add(source_url=QGI, office="London, England", round="phone_technical",
    round_name="technical interview on probability and behavioral questions",
    section_context="Math test, technical interview on probability and behavioral questions as well. Questions on basic options pricing/ options theory/ greeks and how they are used in practice.",
    question_type="statistics_regression",
    question_text="Confidence intervals. They gave me a function and asked me to prive it's a valid probability distribution.",
    source_quote="Math test, technical interview on probability and behavioral questions as well. Questions on basic options pricing/ options theory/ greeks and how they are used in practice.",
    post_date="2026-02-02",
    poster_context="Anonymous Interview Candidate in London, England, Quant Trading Intern Interview, Feb 2, 2026, No offer, Positive experience, Average interview; applied through college or university, interviewed Aug 2025",
    doubt=GD + " The poster never says which function they were given, so the provable-distribution task cannot be reconstructed; 'prive' is their typo for 'prove'.")

add(source_url=QGI, office="Chicago, IL", round="online_assessment",
    round_name="math online assessment", section_context="7 questions in 45 minutes",
    question_type="other",
    question_text="Interview began with a math online assessment: 7 questions in 45 minutes.",
    source_quote="Interview began with a math online assessment: 7 questions in 45 minutes. Next, a first-round technical interview on Zoom lasting 60 minutes, focused on problem-solving, coding, and clarifying thought process.",
    post_date="2025-10-14",
    poster_context="Anonymous Interview Candidate in Chicago, IL, Quant Trading Intern Interview, Oct 14, 2025, No offer, Neutral experience, Difficult interview",
    doubt=GD + " Format only, no question content. Included because it independently corroborates DRW's 7-question / 45-minute OA against a second September-2025 London account.")

add(source_url=QGI, round="online_assessment",
    round_name="First stage was a math test that had 7 questions",
    section_context="The limit was about 45 minutes. It had linear algebra, probability, brain teasers, optimization, etc. problems.",
    question_type="probability",
    question_text="Probability, brain teasers, markov chains, linear algebra",
    source_quote="First stage was a math test that had 7 questions. The limit was about 45 minutes. It had linear algebra, probability, brain teasers, optimization, etc. problems.",
    post_date="2025-09-08",
    poster_context="Anonymous Interview Candidate, Quant Trading Intern Interview, Sep 8, 2025, No offer, Neutral experience, Difficult interview",
    doubt=GD + " A topic list, not a problem. Note the count conflicts with other DRW accounts that report a 6-question OA, so the number of questions apparently varies by cycle or track.")

# ------------------------------- Quantitative Trading Intern -------------------------------
add(source_url=QQI, round="online_assessment",
    round_name="a six-question online assessment testing coding and problem-solving skills",
    section_context="followed by an interview, then a superday with multiple technical and behavioral rounds",
    question_type="logic_brainteaser",
    question_text="I was asked some green book questions.",
    source_quote="The interview process includes a six-question online assessment testing coding and problem-solving skills, followed by an interview, then a superday with multiple technical and behavioral rounds, leading to a potential offer.",
    post_date="2025-10-23",
    poster_context="Anonymous Interview Candidate, Quantitative Trading Intern Interview, Oct 23, 2025, No offer, Neutral experience, Average interview",
    doubt=GD + " The poster identifies the source of the questions ('green book' = Xinfeng Zhou's A Practical Guide to Quantitative Finance Interviews) rather than any question, so nothing specific survives — but it is direct first-person testimony that DRW asks green-book problems.")

add(source_url=QQI, round="phone_technical",
    round_name="a 45 minutes interview with a trader",
    section_context="First I had to do an online assesment with five probability questions",
    question_type="expected_value",
    question_text="What is the expected value of the sum of the digits of your telephone number?",
    source_quote="First I had to do an online assesment with five probability questions, then a 45 minutes interview with a trader in which i was asked some questions on projects and CV a market making game and probability questions.",
    post_date="2025-10-18",
    poster_context="Anonymous Interview Candidate, Quantitative Trading Intern Interview, Oct 18, 2025, No offer, Positive experience, Average interview",
    doubt=GD + " A nice concrete question, but the poster reports a five-question OA where neighbouring entries say six or seven, so DRW's OA length is inconsistently reported across candidates.")

add(source_url=QQI, office="London, England", round="phone_technical",
    round_name="Technical (market making games followed by probability questions of medium difficulty)",
    section_context="OA (7 qs, Linear algebra, Calculus, Probability), Behavioral (Mental Maths), Technical (market making games followed by probability questions of medium difficulty) -> Superday",
    question_type="market_making",
    question_text="Market making games, followed by a probability question.",
    source_quote="OA (7 qs, Linear algebra, Calculus, Probability), Behavioral (Mental Maths), Technical (market making games followed by probability questions of medium difficulty) -> Superday. The process was overall standard experience and length.",
    post_date="2025-10-10",
    poster_context="Anonymous Interview Candidate in London, England, Quantitative Trading Intern Interview, Oct 10, 2025, No offer, Positive experience, Average interview; applied online, interviewed Sep 2025",
    doubt=GD + " No individual problem; its value is the round-by-round map of DRW's 2025 London intern pipeline (7-question OA, behavioural mental maths, technical market-making, superday).")

# ------------------------------- Trading Intern -------------------------------
add(source_url=TIN, round="phone_technical",
    round_name="one interview followed by coding challenge followed by a superday",
    section_context="the interview tests intuition, lots of questions, mostly medium ones , was asked to give estimate before calculating for each question",
    question_type="expected_value",
    question_text="expected product of heads and tails when flipping a coin 100 times",
    source_quote="one interview followed by coding challenge followed by a superday, the interview tests intuition, lots of questions, mostly medium ones , was asked to give estimate before calculating for each question",
    post_date="2026-06-16",
    poster_context="Anonymous Interview Candidate, Trading Intern Interview, Jun 16, 2026, No offer, Positive experience, Average interview",
    doubt=GD + " Concrete and well-posed, but the poster does not say whether they wanted E[HT] exactly or the estimate-first answer the narrative describes being asked for.")

add(source_url=TIN, office="London, England", round="onsite",
    round_name="Phone screen followed by onsite interview in office",
    section_context="This process happened over a space of 3 weeks. Questions were related to probability and market making games. There was also a coding question.",
    question_type="market_making", question_text="Market making games with current trader",
    source_quote="Phone screen followed by onsite interview in office. This process happened over a space of 3 weeks. Questions were related to probability and market making games. There was also a coding question.",
    post_date="2025-01-24",
    poster_context="Anonymous Interview Candidate in London, England, Trading Intern Interview, Jan 24, 2025, No offer, Neutral experience, Average interview",
    doubt=GD + " No question content beyond the label 'market making games'.")

add(source_url=TIN, round="phone_technical",
    round_name="OA -> phone screen -> final round. The phone screen had technical questions.",
    question_type="expected_value",
    question_text="what is the expected value of rolling a dice",
    source_quote="The interview process was three stages as shown below. OA -> phone screen -> final round. The online assessment you could take any time. The phone screen had technical questions.",
    post_date="2023-10-01",
    poster_context="Anonymous Interview Candidate, Trading Intern Interview, Oct 1, 2023, No offer, Positive experience, Difficult interview",
    doubt=GD + " The single most standard warm-up in quant interviewing, so it carries almost no information beyond confirming DRW opens its phone screen gently.")


with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
