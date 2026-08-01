#!/usr/bin/env python3
"""Second pass over the WallStreetOasis per-interview permalinks.

build_p23 took the permalinks that had already been reconciled against the company
listing pages; this pass takes the remainder that wso_perm.py --new still reports as
unmined. Two Old Mission permalinks (quant-trader, senior-software-engineer) are
deliberately absent: their full text already reached the dataset through the company
listing page, so recording them again under the permalink URL would double-count.
Non-quant D. E. Shaw and Two Sigma tracks (fundamental equities, compliance, SBD,
product & capital strategy) are also skipped as out of shard scope.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p26_wso_perm2.jsonl")

WSO_POSTER = ("Anonymous WallStreetOasis interview submission; WSO records the interview "
              "month, city and the submitter's self-reported job title but nothing else "
              "about them")
WSO_DOUBT = ("WSO interview submissions are anonymous, self-reported and never verified "
             "against an actual application, and the site awards content credits for "
             "submitting, which gives a mild incentive to embellish.")

rows = []


def add(**kw):
    o = {
        "firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
        "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
        "section_context": None, "question_type": "other", "question_text": None,
        "question_text_en": None, "reported_answer": None, "source_url": None,
        "source_type": "wso", "source_quote": None, "source_language": "en",
        "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": WSO_POSTER, "doubt": WSO_DOUBT,
    }
    o.update(kw)
    rows.append(o)


# ---------------------------------------------------------------- Akuna Capital
U = "https://www.wallstreetoasis.com/company/akuna-capital-llc/interview/junior-trader-42"
add(firm="Akuna Capital", role_track="quant_trader", level="new_grad",
    round="online_assessment", round_name="a couple rounds of online assessments",
    question_type="other", post_date="2025-03", source_url=U,
    question_text=("Process is a couple of rounds of online assessment, then Zoom calls with "
                   "traders, then a behavioural round with an HR rep"),
    source_quote=("Starts with a couple rounds of online assessments before moving to zoom "
                  "calls with traders and a behavioral round with an hr rep"),
    poster_context="Anonymous WSO submission, Junior trader, interviewed March 2025",
    doubt=(WSO_DOUBT + " Describes only the shape of the funnel; no individual question is "
           "reported, so this attests the round structure and nothing about content."))

# ---------------------------------------------------------------- D. E. Shaw
U = "https://www.wallstreetoasis.com/company/de-shaw/interview/associate-0"
add(firm="D. E. Shaw", role_track="unknown", level="new_grad",
    round="phone_technical", round_name="a R1, 30-min video interview",
    section_context="30-minute first-round video interview; a writing sample is required with the application",
    question_type="logic_brainteaser", post_date="2026-02", source_url=U,
    question_text="First-round 30-minute video interview mixing behavioural questions and brain teasers",
    source_quote=("got an invite for a R1, 30-min video interview, consisting of behaviorals "
                  "and brain teasers. They require submitting a writing sample"),
    poster_context=("Anonymous WSO submission, Associate, interviewed February 2026; applied "
                    "on Handshake through their college portal and submitted a physics class "
                    "research paper as the writing sample"),
    doubt=(WSO_DOUBT + " The title 'Associate' plus a required writing sample suggests this may "
           "be D. E. Shaw's non-quant associate track rather than a quant seat, so role_track "
           "is left unknown; no brain teaser is actually quoted."))

U = "https://www.wallstreetoasis.com/company/de-shaw/interview/summer-intern-0"
add(firm="D. E. Shaw", role_track="unknown", level="internship",
    round="phone_technical", round_name="interview ... with a member of the recruiting team",
    question_type="behavioral", post_date="2025-05", source_url=U,
    question_text="CV-related and behavioural/situational questions from a recruiter, answered with the STAR framework",
    source_quote=("interview was with a member of the recruiting team and consists mostly of "
                  "CV related and behavioural/situational questions, they value good "
                  "communication so candidates who break down their thought process for the "
                  "situational questions and use the STAR framework well will have a higher "
                  "chance of passing the interview"),
    poster_context=("Anonymous WSO submission titled 'summer intern', interviewed May 2025; "
                    "applied online without a cover letter and did not progress further"),
    doubt=(WSO_DOUBT + " The submission does not name a desk or role family, so it may not be "
           "a quant internship at all; the advice about STAR is the poster's inference rather "
           "than something an interviewer told them."))

# ---------------------------------------------------------------- DRW
U = "https://www.wallstreetoasis.com/company/drw/interview/quant-researcher-2"
add(firm="DRW", role_track="quant_researcher", level="unknown",
    round="take_home", round_name="take home OA",
    question_type="other", post_date="2024-04", source_url=U,
    question_text="Take-home online assessment followed by a live technical test, after an intro call with the head of desk",
    source_quote=("Intro call with head of desk, take home OA then live technical test. Hiring "
                  "process was fine, took a about 2 weeks to hear back after OA"),
    poster_context="Anonymous WSO submission, Quant Researcher, interviewed April 2024",
    doubt=(WSO_DOUBT + " Records the round sequence only; the poster reports nothing about what "
           "the take-home actually contained."))

U = "https://www.wallstreetoasis.com/company/drw/interview/quant-trading-analyst-0"
add(firm="DRW", role_track="quant_trader", level="new_grad",
    round="online_assessment", round_name="the online math assessment",
    question_type="other", post_date="2025-06", source_url=U,
    question_text="Online math assessment as the first stage",
    source_quote="Had the online math assessment, and then had a zoom interview, then had a in person superday.",
    poster_context="Anonymous WSO submission, Quant Trading Analyst, interviewed June 2025",
    doubt=(WSO_DOUBT + " Names the assessment as a 'math assessment' but reports no question "
           "from it, so the topic label rests on one word."))
add(firm="DRW", role_track="quant_trader", level="new_grad",
    round="superday", round_name="in person superday", section_context="3 interviews",
    question_type="other", post_date="2025-06", source_url=U,
    question_text="In-person superday consisting of 3 interviews",
    source_quote="then had a in person superday. The super day consisted of 3 interviews.",
    poster_context="Anonymous WSO submission, Quant Trading Analyst, interviewed June 2025",
    doubt=(WSO_DOUBT + " Only the count of interviews is given; nothing about their content."))

U = "https://www.wallstreetoasis.com/company/drw/interview/software-engineering-intern-0"
add(firm="DRW", role_track="quant_developer", level="internship", office="Chicago",
    round="online_assessment", round_name="an OA",
    section_context="four questions: two LC medium and two LC hard (DP)",
    question_type="coding_algorithms", post_date="2023-02", source_url=U,
    question_text="OA with four questions: two LeetCode-medium and two LeetCode-hard dynamic programming problems",
    source_quote=("I was sent an OA with four questions which consisted of two lc medium and two "
                  "lc hard (dp) problem"),
    poster_context=("Anonymous WSO submission, Software engineering intern, interviewed February "
                    "2023; recruited through a university program for the data exchange team in Chicago"),
    doubt=(WSO_DOUBT + " Difficulty is graded by LeetCode analogy rather than by quoting the "
           "problems, so 'two hard DP' is the poster's own calibration."))
add(firm="DRW", role_track="quant_developer", level="internship", office="Chicago",
    round="phone_technical", round_name="a technical interview" ,
    question_type="coding_algorithms", post_date="2023-02", source_url=U,
    question_text="System design question about arranging seats in a theatre",
    source_quote="It was partly behavioral and partly system design. System design questions were about arranging seats in a theatre.",
    poster_context=("Anonymous WSO submission, Software engineering intern, interviewed February "
                    "2023; interview was with the hiring manager for the Chicago data exchange team"),
    doubt=(WSO_DOUBT + " 'Arranging seats in a theatre' is a summary of the prompt, not the "
           "prompt itself, so the actual constraints asked for are unknown."))
add(firm="DRW", role_track="quant_developer", level="internship", office="Chicago",
    round="phone_technical", round_name="a technical interview",
    question_type="other", post_date="2023-02", source_url=U,
    question_text="Questions about contracts",
    source_quote="He also asked questions about contracts and stuff.",
    poster_context=("Anonymous WSO submission, Software engineering intern, interviewed February "
                    "2023, data exchange team in Chicago"),
    doubt=(WSO_DOUBT + " 'contracts and stuff' is too vague to tell whether this meant futures "
           "contracts, C++ contracts or something else entirely."))

U = "https://www.wallstreetoasis.com/company/drw/interview/trader-intern-1"
add(firm="DRW", role_track="quant_trader", level="internship", office="London",
    round="online_assessment", round_name="online assesment",
    question_type="probability", post_date="2026-10", source_url=U,
    question_text="Online assessment of math, statistics and probability theory; one question was about Markov chains",
    source_quote=("Got a online assesment which consisted of math, statistics, and probability "
                  "theory (eg. one question was about markov chains but I don't remember any "
                  "other specific ones)."),
    poster_context="Anonymous WSO submission, Trader Intern, London, marked 'Interviewed October 2026', outcome No Offer",
    doubt=(WSO_DOUBT + " WSO displays the interview month as October 2026, which is in the future "
           "relative to when this page was retrieved (August 2026), so the submitter's date entry "
           "is wrong by at least a couple of months. The poster also states outright that they "
           "cannot remember any question other than the Markov chain one."))
add(firm="DRW", role_track="quant_trader", level="internship", office="London",
    round="phone_technical", round_name="a short phone interview with a recruiter",
    question_type="mental_math_speed", post_date="2026-10", source_url=U,
    question_text="Behavioural questions and mental math in a short recruiter phone screen",
    source_quote="Did well on that and got a short phone interview with a recruiter. Behavioural and mental math.",
    poster_context="Anonymous WSO submission, Trader Intern, London, marked 'Interviewed October 2026'",
    doubt=(WSO_DOUBT + " The stated interview month is in the future relative to retrieval, and "
           "'mental math' is a category label rather than a reported question."))

U = "https://www.wallstreetoasis.com/company/drw/interview/trading-intern-7"
add(firm="DRW", role_track="quant_trader", level="internship",
    round="online_assessment", round_name="6 Question OA", section_context="6 questions",
    question_type="other", post_date="2025-10", source_url=U,
    question_text="Online assessment of 6 questions",
    source_quote="6 Question OA at first followed by a behavioral where they asked why DRW, why Quant and some mental math questions.",
    poster_context="Anonymous WSO submission, Trading Intern, interviewed October 2025",
    doubt=(WSO_DOUBT + " Gives the question count but no question content, and the count "
           "conflicts with other DRW intern reports of longer assessments."))
add(firm="DRW", role_track="quant_trader", level="internship",
    round="phone_technical", round_name="a behavioral",
    question_type="behavioral", post_date="2025-10", source_url=U,
    question_text="Why DRW, why Quant",
    source_quote="followed by a behavioral where they asked why DRW, why Quant and some mental math questions.",
    poster_context="Anonymous WSO submission, Trading Intern, interviewed October 2025",
    doubt=(WSO_DOUBT + " These are the two most predictable motivational questions at any trading "
           "firm, so their presence carries little discriminating information."))
add(firm="DRW", role_track="quant_trader", level="internship",
    round="phone_technical", round_name="a behavioral",
    question_type="mental_math_speed", post_date="2025-10", source_url=U,
    question_text="Mental math questions inside the behavioural round",
    source_quote="why Quant and some mental math questions.",
    poster_context="Anonymous WSO submission, Trading Intern, interviewed October 2025",
    doubt=(WSO_DOUBT + " Short quote and no example computation is given; only that mental math "
           "appeared in an otherwise behavioural call."))

# ---------------------------------------------------------------- Five Rings
U = "https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview/quant-trading-intern-0"
add(firm="Five Rings", role_track="quant_trader", level="internship",
    round="phone_technical", round_name="the first [interview]",
    section_context="4 interviews total, no superday",
    question_type="fermi_estimation", post_date="2022-09", source_url=U,
    question_text="A series of fast-paced estimation-style questions in the first interview",
    source_quote="The first consisted of a series of fast-paced estimation-style questions.",
    poster_context="Anonymous WSO submission, Quant Trading Intern, interviewed September 2022; received an offer without a superday",
    doubt=(WSO_DOUBT + " Characterises the round rather than quoting an estimation prompt, and a "
           "submitter who received an offer has an incentive to present the process favourably."))
add(firm="Five Rings", role_track="quant_trader", level="internship",
    round="phone_technical", round_name="The next 3 interviews",
    question_type="probability", post_date="2022-09", source_url=U,
    question_text="Math interviews covering probability and stochastic processes",
    source_quote=("The next 3 interviews were all focused on measuring my skills in math "
                  "(probability, stochastic processes, etc.) and game theory."),
    poster_context="Anonymous WSO submission, Quant Trading Intern, interviewed September 2022; received an offer",
    doubt=(WSO_DOUBT + " Topic list only, with an 'etc.' that leaves the coverage open; no "
           "individual problem is recalled."))
add(firm="Five Rings", role_track="quant_trader", level="internship",
    round="phone_technical", round_name="The next 3 interviews",
    question_type="poker_game_theory", post_date="2022-09", source_url=U,
    question_text="Game theory questions across the three technical interviews",
    source_quote="focused on measuring my skills in math (probability, stochastic processes, etc.) and game theory",
    poster_context="Anonymous WSO submission, Quant Trading Intern, interviewed September 2022",
    doubt=(WSO_DOUBT + " 'Game theory' is a one-word topic label; whether this meant a trading "
           "game, a poker variant or textbook equilibrium problems is not stated."))

# ---------------------------------------------------------------- Hudson River Trading
U = "https://www.wallstreetoasis.com/company/hudson-river-trading-llc/interview/summer-intern"
add(firm="Hudson River Trading", role_track="unknown", level="internship",
    round="phone_technical", round_name="1-on-1 phone interview with an HR rep",
    question_type="behavioral", post_date="2022-08", source_url=U,
    question_text="Primarily behavioural questions in a 1-on-1 HR phone screen",
    source_quote="1-on-1 phone interview with an HR rep. Did not advance past this point in the process. Primarily bheavioral questions.",
    poster_context="Anonymous WSO submission, Summer Intern, interviewed August 2022; did not advance past the HR screen",
    doubt=(WSO_DOUBT + " The poster was rejected at the first screen, so they never saw the "
           "technical stages and cannot speak to them; the typo 'bheavioral' suggests a hurried "
           "write-up."))

U = "https://www.wallstreetoasis.com/company/hudson-river-trading-llc/interview/summeriintern"
add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    round="online_assessment", round_name="Online assessment", platform="HackerRank",
    section_context="3 coding questions, 90 minutes",
    question_type="coding_algorithms", post_date="2024-10", source_url=U,
    question_text="Online assessment with 3 coding questions on HackerRank, ranging from dynamic programming to tree traversal, in 90 minutes",
    source_quote="Online assessment with 3 coding questions on hacker rank, ranging from dp to tree traversal. given 90 minutes",
    poster_context="Anonymous WSO submission titled 'SummerIintern', interviewed October 2024",
    doubt=(WSO_DOUBT + " Names the topics and the timing but not the problems, so the DP and "
           "tree-traversal labels are the poster's classification of what they saw."))

# ---------------------------------------------------------------- Jump Trading
U = "https://www.wallstreetoasis.com/company/jump-trading/interview/algo-trader"
add(firm="Jump Trading", role_track="quant_trader", level="new_grad",
    round="onsite", round_name="an onsite with 4 rounds",
    section_context="45-minute on-campus round, then a 4-round onsite",
    question_type="other", post_date="2018-10", source_url=U,
    question_text="On-campus 45-minute interview followed by a four-round onsite",
    source_quote="I applied through college and went through a 1 round on campus interview (45min), followed by an onsite with 4 rounds.",
    poster_context="Anonymous WSO submission, algo trader, interviewed October 2018; applied through college",
    doubt=(WSO_DOUBT + " Structure only, and from 2018, so it may not describe Jump's current "
           "process; no question content at all."))

U = "https://www.wallstreetoasis.com/company/jump-trading/interview/quant-research-intern-0"
add(firm="Jump Trading", role_track="quant_researcher", level="internship",
    round="onsite", round_name="one full day of online interviews",
    section_context="3-4 interviewers, roughly 1 hour each",
    question_type="coding_algorithms", post_date="2019-09", source_url=U,
    question_text="Math and coding questions across a full day of interviews with 3-4 people, about an hour each",
    source_quote=("A single online video interview first, then one full day of online interviews "
                  "(with 3-4 different people, ~1 hour each). Math and coding questions."),
    poster_context="Anonymous WSO submission, Quant Research Intern, interviewed September 2019",
    doubt=(WSO_DOUBT + " 'Math and coding questions' is the entire content description, and the "
           "2019 date makes it a poor guide to the current loop."))

U = "https://www.wallstreetoasis.com/company/jump-trading/interview/quantitative-research"
add(firm="Jump Trading", role_track="quant_researcher", level="unknown",
    round="phone_technical", round_name="the first-round interview",
    question_type="coding_algorithms", post_date="2025-10", source_url=U,
    question_text="A simple coding question in the first round",
    source_quote="the first-round interview, which included a simple coding question and some basic OLS and probability/expectation problems.",
    poster_context=("Anonymous WSO submission, Quantitative Research, interviewed October 2025; "
                    "HR first invited them to a dinner, then scheduled the first round via Doodle"),
    doubt=(WSO_DOUBT + " 'Simple' is the poster's judgement and the problem itself is not given."))
add(firm="Jump Trading", role_track="quant_researcher", level="unknown",
    round="phone_technical", round_name="the first-round interview",
    question_type="statistics_regression", post_date="2025-10", source_url=U,
    question_text="Basic OLS problems in the first round",
    source_quote="which included a simple coding question and some basic OLS and probability/expectation problems",
    poster_context="Anonymous WSO submission, Quantitative Research, interviewed October 2025",
    doubt=(WSO_DOUBT + " Names OLS as the topic without giving the setup, so what was actually "
           "derived or computed is unknown."))
add(firm="Jump Trading", role_track="quant_researcher", level="unknown",
    round="phone_technical", round_name="the first-round interview",
    question_type="expected_value", post_date="2025-10", source_url=U,
    question_text="Probability and expectation problems in the first round",
    source_quote="and some basic OLS and probability/expectation problems",
    poster_context="Anonymous WSO submission, Quantitative Research, interviewed October 2025",
    doubt=(WSO_DOUBT + " Short topic-level quote; no problem statement is preserved."))
add(firm="Jump Trading", role_track="quant_researcher", level="unknown",
    round="onsite", round_name="the final round",
    section_context="four interviews: two math, one coding, one behavioural",
    question_type="other", post_date="2025-10", source_url=U,
    question_text="Final round of four interviews: two math interviews, one coding interview, one behavioural interview",
    source_quote=("I was invited to the final round, which consisted of four interviews: two math "
                  "interviews, one coding interview, and one behavioral interview."),
    poster_context="Anonymous WSO submission, Quantitative Research, interviewed October 2025",
    doubt=(WSO_DOUBT + " Composition of the loop only; the poster reports nothing that was asked "
           "inside any of the four."))

U = "https://www.wallstreetoasis.com/company/jump-trading/interview/quantitative-researcher-intern"
add(firm="Jump Trading", role_track="quant_researcher", level="internship",
    round="phone_technical", round_name="an online interview",
    question_type="probability", post_date="2023-10", source_url=U,
    question_text="Probability questions in the online interview",
    source_quote=("It started with an online interview, where I was asked some probability, linear "
                  "algebra and programming questions"),
    poster_context="Anonymous WSO submission, Quantitative Researcher Intern, interviewed October 2023",
    doubt=(WSO_DOUBT + " Three topics named in one sentence with no problem preserved from any "
           "of them."))
add(firm="Jump Trading", role_track="quant_researcher", level="internship",
    round="phone_technical", round_name="an online interview",
    question_type="linear_algebra", post_date="2023-10", source_url=U,
    question_text="Linear algebra questions in the online interview",
    source_quote="where I was asked some probability, linear algebra and programming questions",
    poster_context="Anonymous WSO submission, Quantitative Researcher Intern, interviewed October 2023",
    doubt=(WSO_DOUBT + " Topic label only; linear algebra is unusual enough in a first round that "
           "it would be worth corroborating against another account."))
add(firm="Jump Trading", role_track="quant_researcher", level="internship",
    round="phone_technical", round_name="an online interview",
    question_type="coding_algorithms", post_date="2023-10", source_url=U,
    question_text="Programming questions in the online interview",
    source_quote="I was asked some probability, linear algebra and programming questions, and then it was final on site interview",
    poster_context="Anonymous WSO submission, Quantitative Researcher Intern, interviewed October 2023",
    doubt=(WSO_DOUBT + " No language, platform or problem is given."))
add(firm="Jump Trading", role_track="quant_researcher", level="internship",
    round="onsite", round_name="final on site interview",
    question_type="other", post_date="2023-10", source_url=U,
    question_text="Final onsite where people from different groups ask questions",
    source_quote="then it was final on site interview, where people from different groups ask me questions.",
    poster_context="Anonymous WSO submission, Quantitative Researcher Intern, interviewed October 2023",
    doubt=(WSO_DOUBT + " Says only that multiple groups interviewed them; no content whatsoever."))

U = "https://www.wallstreetoasis.com/company/jump-trading/interview/software-development-internship"
add(firm="Jump Trading", role_track="quant_developer", level="internship",
    round="phone_technical", round_name="behavioral phone screen interview",
    question_type="behavioral", post_date="2019-08", source_url=U,
    question_text="Behavioural phone screen, then an in-person technical interview",
    source_quote="First I had a behavioral phone screen interview then I was contacted for an in person technical interview a few days later.",
    poster_context="Anonymous WSO submission, Software Development Internship, interviewed August 2019",
    doubt=(WSO_DOUBT + " Sequence only, from 2019; nothing about what either interview contained."))

# ---------------------------------------------------------------- Old Mission Capital
U = "https://www.wallstreetoasis.com/company/old-mission-capital/interview/junior-quant-trader"
add(firm="Old Mission Capital", role_track="quant_trader", level="new_grad",
    round="phone_technical", round_name="Standard brainteaser and probability questions",
    question_type="logic_brainteaser", post_date="2022-08", source_url=U,
    question_text="Standard brainteaser questions of the kind asked at quant funds",
    source_quote="Standard brainteaser and probability questions as asked at quant funds.",
    poster_context="Anonymous WSO submission, Junior Quant Trader, interviewed August 2022",
    doubt=(WSO_DOUBT + " The poster explicitly calls the questions 'standard ... as asked at quant "
           "funds', i.e. they are describing a genre rather than recalling Old Mission's own "
           "problems, and that genre overlaps heavily with the published interview books."))
add(firm="Old Mission Capital", role_track="quant_trader", level="new_grad",
    round="phone_technical", round_name="Standard brainteaser and probability questions",
    question_type="probability", post_date="2022-08", source_url=U,
    question_text="Standard probability questions of the kind asked at quant funds",
    source_quote="Standard brainteaser and probability questions as asked at quant funds. Overall very fast and efficient",
    poster_context="Anonymous WSO submission, Junior Quant Trader, interviewed August 2022; the interview involved a skills test, IQ test and personality test",
    doubt=(WSO_DOUBT + " Same sentence as the brainteaser record; 'standard' signals textbook "
           "overlap rather than a firm-specific recall."))

U = "https://www.wallstreetoasis.com/company/old-mission-capital/interview/quant-trading-intern"
add(firm="Old Mission Capital", role_track="quant_trader", level="internship",
    round="online_assessment", round_name="an initial Coding and Mathematics assessment",
    question_type="logic_brainteaser", post_date="2018-11", source_url=U,
    question_text="Initial Coding and Mathematics assessment, mainly brainteasers with some probability/statistics",
    source_quote=("Received an initial Coding and Mathematics assessment. The assessment was "
                  "challenging and mainly brainteasers with some Prob/Stats."),
    poster_context="Anonymous WSO submission, Quant Trading Intern, interviewed November 2018; submitted a resume at a career fair and also applied online",
    doubt=(WSO_DOUBT + " From 2018, so the assessment described may no longer resemble the "
           "current one; no individual brainteaser is recalled."))
add(firm="Old Mission Capital", role_track="quant_trader", level="internship",
    round="online_assessment", round_name="an initial Coding and Mathematics assessment",
    section_context="2 coding questions/exercises, one challenging and one easy",
    question_type="coding_algorithms", post_date="2018-11", source_url=U,
    question_text="Coding portion of the assessment: 2 questions/exercises, one challenging and one easy",
    source_quote="The coding consisted of 2 questions/exercises, one was pretty challenging the other was easy.",
    poster_context="Anonymous WSO submission, Quant Trading Intern, interviewed November 2018",
    doubt=(WSO_DOUBT + " Counts and relative difficulty only; the problems themselves are not "
           "described, and the 2018 date limits how much it says about the current OA."))
add(firm="Old Mission Capital", role_track="quant_trader", level="internship",
    round="phone_technical", round_name="phone call with the trader",
    section_context="4 questions in the trader phone interview; poster got 2 of 4",
    question_type="other", post_date="2018-11", source_url=U,
    question_text="Four challenging questions in the phone interview with a trader",
    source_quote=("The questions in the phone call with the trader were pretty challenging and "
                  "while I was able to get 2/4 correct. I did not make it to the next round."),
    poster_context="Anonymous WSO submission, Quant Trading Intern, interviewed November 2018; had two phone interviews three weeks after the assessment, one HR and one with a trader",
    doubt=(WSO_DOUBT + " Gives the question count and their own score but not a single question; "
           "a rejected candidate may also over-rate the difficulty."))

U = "https://www.wallstreetoasis.com/company/old-mission-capital/interview/quantitative-research-intern"
add(firm="Old Mission Capital", role_track="quant_researcher", level="internship",
    round="phone_technical", round_name="phone interview",
    question_type="mental_math_speed", post_date="2014-03", source_url=U,
    question_text="Phone interview questions mostly mental math",
    source_quote=("Phone interview questions were mostly mental math, probability, and statistics. "
                  "Some questions seemed to come straight from popular quant interview study books."),
    poster_context="Anonymous WSO submission, Quantitative Research Intern, interviewed March 2014; got the phone screen two business days after applying online",
    doubt=(WSO_DOUBT + " The poster themselves says the questions 'seemed to come straight from "
           "popular quant interview study books', so this attests that Old Mission asked "
           "textbook material rather than establishing any original question. It is also from "
           "2014."))
add(firm="Old Mission Capital", role_track="quant_researcher", level="internship",
    round="phone_technical", round_name="phone interview",
    question_type="probability", post_date="2014-03", source_url=U,
    question_text="Phone interview questions on probability and statistics, several apparently taken from popular quant interview study books",
    source_quote="mostly mental math, probability, and statistics. Some questions seemed to come straight from popular quant interview study books.",
    poster_context="Anonymous WSO submission, Quantitative Research Intern, interviewed March 2014",
    doubt=(WSO_DOUBT + " Explicit textbook overlap flagged by the poster, and a 2014 date makes "
           "it weak evidence about the present process."))

U = "https://www.wallstreetoasis.com/company/old-mission-capital/interview/trader-0"
add(firm="Old Mission Capital", role_track="quant_trader", level="unknown", office="Chicago",
    round="onsite", round_name="an interview with a senior trader, last interview was with CEO",
    section_context="20-minute phone screen, then a senior trader, then the CEO",
    question_type="logic_brainteaser", post_date="2020-09", source_url=U,
    question_text="Lots of questions about hypothetical scenarios to see how you think",
    source_quote=("Initial phone screen about 20 minutes, then an interview with a senior trader, "
                  "last interview was with CEO. Lots of questions about hypothetical scenarios to "
                  "see how you think, stats, and market making/options."),
    poster_context="Anonymous WSO submission, Trader, interviewed September 2020; final round was with the CEO",
    doubt=(WSO_DOUBT + " 'Hypothetical scenarios' is not specific enough to reconstruct a single "
           "question, and the submission does not say whether this was a campus or experienced hire."))
add(firm="Old Mission Capital", role_track="quant_trader", level="unknown", office="Chicago",
    round="onsite", round_name="an interview with a senior trader, last interview was with CEO",
    question_type="market_making", post_date="2020-09", source_url=U,
    question_text="Market making and options questions with a senior trader and the CEO",
    source_quote="Lots of questions about hypothetical scenarios to see how you think, stats, and market making/options.",
    poster_context="Anonymous WSO submission, Trader, interviewed September 2020",
    doubt=(WSO_DOUBT + " Topic list only; no market was actually quoted or described."))
add(firm="Old Mission Capital", role_track="quant_trader", level="unknown", office="Chicago",
    round="onsite", round_name="an interview with a senior trader, last interview was with CEO",
    question_type="statistics_regression", post_date="2020-09", source_url=U,
    question_text="Statistics questions with a senior trader and the CEO",
    source_quote="to see how you think, stats, and market making/options.",
    poster_context="Anonymous WSO submission, Trader, interviewed September 2020",
    doubt=(WSO_DOUBT + " The word 'stats' is the whole of the evidence for this topic."))

U = "https://www.wallstreetoasis.com/company/old-mission-capital/interview/trading-intern-2"
add(firm="Old Mission Capital", role_track="quant_trader", level="internship",
    round="phone_technical", round_name="Phone interview with probability and brainteaser type questions",
    question_type="probability", post_date="2014-01", source_url=U,
    question_text="Phone interview with probability and brainteaser questions; the poster advises reviewing combinatorics, expectation and conditional probability",
    source_quote=("Phone interview with probability and brainteaser type questions. Most questions "
                  "seem to come straight from the quant interview books. Best to review "
                  "combinatorics/expectation/conditional probability"),
    poster_context="Anonymous WSO submission, Trading Intern, interviewed January 2014",
    doubt=(WSO_DOUBT + " The poster states the questions came 'straight from the quant interview "
           "books', so this is attestation that Old Mission reused textbook problems, not a "
           "record of an original one. From 2014."))
add(firm="Old Mission Capital", role_track="quant_trader", level="internship",
    round="phone_technical", round_name="Phone interview with probability and brainteaser type questions",
    question_type="combinatorics", post_date="2014-01", source_url=U,
    question_text="Combinatorics, expectation and conditional probability were the areas the poster says to review",
    source_quote="Best to review combinatorics/expectation/conditional probability",
    poster_context="Anonymous WSO submission, Trading Intern, interviewed January 2014",
    doubt=(WSO_DOUBT + " This is the poster's revision advice inferred after the fact, one step "
           "removed from a question they were actually asked."))

# ---------------------------------------------------------------- Two Sigma
U = "https://www.wallstreetoasis.com/company/two-sigma-investments/interview/software-engineering-intern-1"
add(firm="Two Sigma", role_track="quant_developer", level="internship",
    round="online_assessment", round_name="an online assessment OA",
    section_context="2 questions: one LeetCode-medium equivalent, one LeetCode-hard equivalent",
    question_type="coding_algorithms", post_date="2025-02", source_url=U,
    question_text="First OA question: data structures and sweep line algorithms",
    source_quote=("Question was a leetcode medium equivalent followed by a leetcode hard "
                  "equivalent. First question was checking simple knowledge of data structures "
                  "and sweep line algorithms."),
    poster_context="Anonymous WSO submission, Software Engineering Intern, interviewed February 2025; process took about 3 weeks",
    doubt=(WSO_DOUBT + " The first question is described by technique rather than quoted, so "
           "'sweep line' is the poster's classification."))
add(firm="Two Sigma", role_track="quant_developer", level="internship",
    round="online_assessment", round_name="an online assessment OA",
    question_type="coding_algorithms", post_date="2025-02", source_url=U,
    question_text="Given a binary array, sort it so that all 0s come before all 1s",
    reported_answer="In-place sorting with two pointers, per the poster's description",
    source_quote=("Second question was ''Given a binary array, sort it so that all 0s come before "
                  "all 1s.\" Essentially a test of inplace sorting and two pointer techniques."),
    poster_context="Anonymous WSO submission, Software Engineering Intern, interviewed February 2025",
    doubt=(WSO_DOUBT + " The poster labels this the 'leetcode hard equivalent' half of the OA, but "
           "sorting a binary array in place is a textbook easy problem, so either the pairing is "
           "misremembered or the real prompt carried constraints they did not reproduce."))
add(firm="Two Sigma", role_track="quant_developer", level="internship",
    round="phone_technical", round_name="an online one-on-one interview",
    question_type="coding_algorithms", post_date="2025-02", source_url=U,
    question_text="A LeetCode-hard equivalent coding problem in the one-on-one round",
    source_quote=("Second round was an online one-on-one interview which consisted of a leetcode "
                  "style coding problem leetcode hard equivalent then some probability based questions."),
    poster_context="Anonymous WSO submission, Software Engineering Intern, interviewed February 2025",
    doubt=(WSO_DOUBT + " Difficulty by analogy only; the problem is not stated."))
add(firm="Two Sigma", role_track="quant_developer", level="internship",
    round="phone_technical", round_name="an online one-on-one interview",
    question_type="probability", post_date="2025-02", source_url=U,
    question_text="Probability-based questions after the coding problem in the one-on-one round",
    source_quote="a leetcode style coding problem leetcode hard equivalent then some probability based questions",
    poster_context="Anonymous WSO submission, Software Engineering Intern, interviewed February 2025",
    doubt=(WSO_DOUBT + " Notable mainly because it shows probability appearing in a software "
           "engineering loop, but no question is preserved."))


# WSO serves each submission twice: inside the paginated company listing and at its own
# permalink. Where an earlier pass already recorded a question from the listing copy, the
# permalink copy is the same human saying the same thing, so it is dropped here rather
# than counted twice.
DROP = {
    ("DRW", "OA with four questions: two LeetCode-medium and two LeetCode-hard dynamic programming problems"),
    ("DRW", "System design question about arranging seats in a theatre"),
    ("DRW", "Online assessment of math, statistics and probability theory; one question was about Markov chains"),
    ("DRW", "Behavioural questions and mental math in a short recruiter phone screen"),
    ("DRW", "Why DRW, why Quant"),
    ("DRW", "Mental math questions inside the behavioural round"),
    ("Hudson River Trading", "Online assessment with 3 coding questions on HackerRank, ranging from dynamic programming to tree traversal, in 90 minutes"),
    ("Hudson River Trading", "Primarily behavioural questions in a 1-on-1 HR phone screen"),
    ("Jump Trading", "Linear algebra questions in the online interview"),
    ("Two Sigma", "Given a binary array, sort it so that all 0s come before all 1s"),
}

# Permalinks whose submission was already mined from the listing page. The surviving
# records draw on different sentences of the same write-up, so they are kept, but they
# are not independent of the listing-page records and say so.
SAME_SUBMISSION = {
    "drw/interview/quant-researcher-2", "drw/interview/quant-trading-analyst-0",
    "drw/interview/software-engineering-intern-0", "drw/interview/trading-intern-7",
    "jump-trading/interview/quant-research-intern-0",
    "jump-trading/interview/quantitative-research",
    "jump-trading/interview/quantitative-researcher-intern",
    "old-mission-capital/interview/junior-quant-trader",
    "old-mission-capital/interview/trading-intern-2",
    "two-sigma-investments/interview/software-engineering-intern-1",
}
NOTE = (" The same submission is also recorded in this dataset from WallStreetOasis's "
        "paginated company listing page, so the two are one account, not two.")

kept = []
for o in rows:
    if (o["firm"], o["question_text"]) in DROP:
        continue
    if any(s in o["source_url"] for s in SAME_SUBMISSION):
        o["doubt"] += NOTE
    kept.append(o)

with open(OUT, "w", encoding="utf-8") as f:
    for o in kept:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
print("wrote %d records (%d dropped as listing-page duplicates) to %s"
      % (len(kept), len(rows) - len(kept), OUT))
