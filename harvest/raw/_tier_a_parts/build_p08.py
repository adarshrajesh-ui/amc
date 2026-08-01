import io
import json

OUT = "/workspace/harvest/raw/_tier_a_parts/p08_wso_gap_glassdoor.jsonl"

WSO_JUMP = "https://www.wallstreetoasis.com/company/jump-trading/interview"
WSO_OMC = "https://www.wallstreetoasis.com/company/old-mission-capital/interview"
WSO_TS = "https://www.wallstreetoasis.com/company/two-sigma-investments/interview"
WSO_DRW = "https://www.wallstreetoasis.com/company/drw/interview"
WSO_FR = "https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview"
WSO_AK = "https://www.wallstreetoasis.com/company/akuna-capital-llc/interview"

WSO_DOUBT = ("Wall Street Oasis interview entries are anonymous and unverified by the site, and this "
             "one is a company roll-up page whose displayed sample of entries can change, so a later "
             "re-fetch may not show it.")

rows = []


def add(**kw):
    base = dict(firm="", role_track="unknown", level="unknown", cycle="unknown", office="unknown",
                round="unknown", round_name="", platform="unknown", section_context=None,
                question_type="other", question_text="", question_text_en=None, reported_answer=None,
                source_url="", source_type="wso", source_quote="", source_language="en",
                post_date="unknown", access="full_text", retrieval_method="webfetch",
                poster_context="", doubt="")
    base.update(kw)
    rows.append(base)


# ---------------- Jump Trading, WSO "algo trader Interview - Research", Oct 2018 ----------------
JA = dict(firm="Jump Trading", source_url=WSO_JUMP, office="Chicago", level="unknown",
          role_track="quant_trader", post_date="2018-12-24", round="onsite",
          round_name="1 round on campus interview (45min), followed by an onsite with 4 rounds",
          poster_context=("Anonymous WSO entry, 'algo trader Interview - Research', anonymous interview "
                          "candidate in Chicago, Interviewed: October 2018, Date Submitted: Dec 24, 2018, "
                          "No Offer, source College / University / On Campus Recruiting. The poster prefaces "
                          "the list with 'overall, the problems are not difficult.'"))

add(**JA, question_type="probability",
    question_text="I'm dealing a deck of poker, you can stop me anytime. If the next card is red, you win. Otherwise you lose. What's optimal strategy and the probability of winning ?",
    source_quote="I'm dealing a deck of poker, you can stop me anytime. If the next card is red, you win. Otherwise you lose. What's optimal strategy and the probability of winning ?",
    doubt=WSO_DOUBT + " This red-card optional-stopping problem is a staple of the Green Book and of Jane Street lore, so the content is textbook; the dated on-campus context is what supports it here.")

add(**JA, question_type="probability",
    question_text="one iteration of bubble sort, what's the probability that the array will be sorted.",
    source_quote="one iteration of bubble sort, what's the probability that the array will be sorted.",
    doubt=WSO_DOUBT + " The statement is under-specified (it does not say the input is a uniformly random permutation), which is either sloppy recall or an accurate record of a terse interviewer.")

# ---------------- Jump Trading, Algorithmic Trading Intern, March 2013 ----------------
JI = dict(firm="Jump Trading", source_url=WSO_JUMP, office="Chicago", level="internship",
          role_track="quant_trader", post_date="2014-01-06", round="superday",
          round_name="superday consisting of 4 interviews",
          section_context=("on-campus first round with 2 technical coding questions (~30 minutes), then a "
                           "Chicago superday of 4 interviews: one pure coding in C++, one mathematical/linear "
                           "algebra on whiteboard, and two pen/paper brainteaser and math/probability rounds"),
          poster_context=("Anonymous WSO entry, 'Algorithmic Trading Intern Interview - Trading', anonymous "
                          "interview candidate in Chicago, Interviewed: March 2013, Date Submitted: Jan 06, 2014, "
                          "No Offer, College / University / On Campus Recruiting."))

add(**JI, question_type="coding_algorithms",
    question_text="Implement a trie in C++.",
    source_quote="Implement a trie in C++.",
    doubt=WSO_DOUBT + " Dated March 2013, so it says nothing about Jump's current intern loop, and the line is short enough to be generic.")

add(**JI, question_type="logic_brainteaser",
    question_text="Swap two variables without additional storage (i.e. no using a temp).",
    source_quote="Swap two variables without additional storage (i.e. no using a temp).",
    doubt=WSO_DOUBT + " The identical question is independently reported for a Jump Trading software developer intern in a 2012 jointaro entry, which is either corroboration or a sign this is simply a very common question.")

add(**JI, question_type="combinatorics",
    question_text="How many 0's are in 1000! (factorial)?",
    source_quote="How many 0's are in 1000! (factorial)?",
    doubt=WSO_DOUBT + " Trailing-zeros-of-a-factorial is a classic textbook counting exercise; only the dated first-person superday context ties it to Jump.")

# ---------------- Jump Trading, Software Development Internship, Aug 2019 ----------------
add(firm="Jump Trading", source_url=WSO_JUMP, office="Cambridge", level="internship",
    role_track="quant_developer", post_date="2019-10-08", round="onsite",
    round_name="in person technical interview",
    section_context="behavioral phone screen first, then an in-person technical interview a few days later",
    question_type="coding_algorithms",
    question_text="Then I was asked about how I would store key value pairs. And then ended in a discussion about how I would implement a hash map data structure. I was asked about the tradeoffs between various implementations.",
    source_quote="Then I was asked about how I would store key value pairs. And then ended in a discussion about how I would implement a hash map data structure.",
    poster_context=("Anonymous WSO entry, 'Software Development Internship Interview - Engineering', "
                    "anonymous interview candidate in Cambridge, Interviewed: August 2019, "
                    "Date Submitted: Oct 08, 2019, No Offer."),
    doubt=WSO_DOUBT + " The poster explicitly says there were 'No difficult questions', so this is a routine CS-fundamentals discussion rather than a distinctive Jump question.")

# ---------------- Old Mission Capital, Floor Trader, April 2025 ----------------
OM = dict(firm="Old Mission Capital", source_url=WSO_OMC, office="Chicago", level="unknown",
          role_track="quant_trader", post_date="2025-06-16", round="phone_technical",
          round_name="call with head of desk at Old Mission (was told this was the last round)",
          poster_context=("Anonymous WSO entry, 'Floor Trader Interview - Prop Trading', anonymous interview "
                          "candidate in Chicago, Interviewed: April 2025, Date Submitted: Jun 16, 2025, No Offer, "
                          "Applied Online, 2-3 months. Poster was told 'market making portion of the interview "
                          "was too weak.'"))

add(**OM, question_type="statistics_regression",
    question_text="Confidence interval on S&P 500 return past 30 years",
    source_quote="Confidence interval on S&P 500 return past 30 years",
    section_context="Basic stats principles, (estimation, confidence intervals, normal distribution, skew) asked to create confidence intervals on many different things",
    doubt=WSO_DOUBT + " Recorded as a five-word topic line; the interviewer's exact framing is not preserved.")

add(**OM, question_type="statistics_regression",
    question_text="Confidence interval of portfolio value if you invested $1 in S&P 500 30 years ago",
    source_quote="Confidence interval of portfolio value if you invested $1 in S&P 500 30 years ago",
    doubt=WSO_DOUBT + " Same terse-topic-line caveat as the other confidence-interval question from this entry.")

add(**{**OM, "round_name": "interviewed with a Floor Trader at Old Mission"}, question_type="options_theory",
    question_text="If you think the market is overestimating volatility, what options strategy can you use",
    source_quote="If you think the market is overestimating volatility, what options strategy can you use",
    doubt=WSO_DOUBT + " Standard options-intuition question that any options shop might ask.")

add(**{**OM, "round": "trading_game", "round_name": "market making game"}, question_type="market_making",
    question_text="Then market making game, you quote bid ask, interviewer either buys from or sells to you, and you update your bid ask for the next iteration. Keep track of maximum drawdown, current p&l, short/long exposure, weighted average price between rounds. Many follow up questions about your logic and reasoning for your quote.",
    source_quote="Then market making game, you quote bid ask, interviewer either buys from or sells to you, and you update your bid ask for the next iteration.",
    doubt=WSO_DOUBT + " This describes the format of the market-making exercise, not the underlying instrument or event being quoted, so no specific question is recoverable.")

# ---------------- Two Sigma ----------------
add(firm="Two Sigma", source_url=WSO_TS, office="New York", level="unknown",
    role_track="quant_researcher", post_date="2026-01-14", round="phone_technical",
    round_name="Three rounds of tech interviews",
    section_context="One is like model design- predict rent prices in Manhattan. Then live coding and states. Stats round is about proof of OLS/optimizaition/Langrange, etc, quite difficult",
    question_type="ml_modeling",
    question_text="One is like model design- predict rent prices in Manhattan.",
    source_quote="One is like model design- predict rent prices in Manhattan.",
    poster_context=("Anonymous WSO entry, 'Junior Quant Researcher Interview - Quantitative Research', "
                    "anonymous interview candidate in New York, Interviewed: November 2025, "
                    "Date Submitted: Jan 14, 2026, No Offer, Applied Online."),
    doubt=WSO_DOUBT + " The prompt is compressed to one clause, so the actual brief (data available, target, constraints) is unknown.")

add(firm="Two Sigma", source_url=WSO_TS, office="New York", level="unknown",
    role_track="quant_researcher", post_date="2026-01-14", round="phone_technical",
    round_name="Stats round",
    question_type="statistics_regression",
    question_text="Stats round is about proof of OLS/optimizaition/Langrange, etc, quite difficult",
    source_quote="Stats round is about proof of OLS/optimizaition/Langrange, etc, quite difficult",
    poster_context=("Same anonymous WSO 'Junior Quant Researcher' entry, Interviewed November 2025."),
    doubt=WSO_DOUBT + " A topic list rather than a question; kept because it evidences that Two Sigma's QR stats round demands derivations, not just recall.")

add(firm="Two Sigma", source_url=WSO_TS, office="New York", level="internship",
    role_track="quant_researcher", post_date="2025-08-29", round="phone_technical",
    round_name="The first round focuses on statistics",
    section_context="first round on statistics; final stage has two rounds, first math and second coding",
    question_type="statistics_regression",
    question_text="Everything was fairly standard. They asked me basic linear algebra and statistics modeling questions.",
    source_quote="They asked me basic linear algebra and statistics modeling questions.",
    poster_context=("Anonymous WSO entry, 'Quant research intern Interview - Research', anonymous interview "
                    "candidate in New York, Interviewed: September 2023, Date Submitted: Aug 29, 2025, No Offer."),
    doubt=WSO_DOUBT + " No actual question is reproduced — only the topic areas of a Two Sigma quant research intern loop.")

# ---------------- DRW Trader Intern, London ----------------
DT = dict(firm="DRW", source_url=WSO_DRW, office="London", level="internship",
          role_track="quant_trader", post_date="2026-01-11",
          poster_context=("Anonymous WSO entry, 'Trader Intern Interview', anonymous interview candidate in "
                          "London, Interviewed: October 2026, Date Submitted: Jan 11, 2026, No Offer, Applied Online. "
                          "Note the site shows an 'Interviewed' month later than the submission date, which is "
                          "internally inconsistent."))

add(**DT, round="online_assessment", round_name="online assesment",
    question_type="probability",
    question_text="Got a online assesment which consisted of math, statistics, and probability theory (eg. one question was about markov chains but I don't remember any other specific ones).",
    source_quote="one question was about markov chains but I don't remember any other specific ones",
    doubt=WSO_DOUBT + " The poster explicitly cannot recall any specific question beyond the topic 'markov chains'.")

add(**DT, round="phone_technical", round_name="short phone interview with a recruiter. Behavioural and mental math.",
    question_type="mental_math_speed",
    question_text="Mental math multiplication (e.g. 73*74)",
    source_quote="Mental math multiplication (e.g. 73*74)",
    doubt=WSO_DOUBT + " The '73*74' is the poster's illustrative example, so it may not be the literal number pair asked.")

# ---------------- Five Rings QR Internship (Sept 2025) ----------------
add(firm="Five Rings", source_url=WSO_FR, office="New York", level="internship",
    role_track="quant_researcher", post_date="2026-07-28", round="phone_technical",
    round_name="The first tech round",
    section_context="First OA (proctored, various math problems), then a first tech round covering 3 probability questions",
    question_type="probability",
    question_text="A question on ordered stats. X and Y in a normal distribution. Find the distribution/expectation value of max(X, Y).",
    source_quote="A question on ordered stats. X and Y in a normal distribution. Find the distribution/expectation value of max(X, Y).",
    poster_context=("Anonymous WSO entry, 'QR Internship Interview', anonymous interview candidate in New York, "
                    "Interviewed: September 2025, Date Submitted: Jul 28, 2026, No Offer, Applied Online."),
    doubt=WSO_DOUBT + " The statement omits whether X and Y are independent or standard normal, so it is the candidate's compression of the prompt rather than the prompt itself.")

add(firm="Five Rings", source_url=WSO_FR, office="New York", level="internship",
    role_track="quant_trader", post_date="2022-06-25", round="phone_technical",
    round_name="1st round video interview with trader",
    section_context="online application -> hr interview (fermi questions under tight time constraints) -> 1st round video interview with trader",
    question_type="probability",
    question_text="proof of answer to a probability question involving discrete math",
    source_quote="proof of answer to a probability question involving discrete math",
    poster_context=("Anonymous WSO entry, 'quantitative trading intern Interview - Prop Trading', anonymous "
                    "interview candidate in new york, Interviewed: October 2021, Date Submitted: Jun 25, 2022, No Offer."),
    doubt=WSO_DOUBT + " Only the shape of the question is recorded — that a proof was demanded — not the question itself.")

add(firm="Five Rings", source_url=WSO_FR, office="New York", level="internship",
    role_track="quant_trader", post_date="2022-11-18", round="phone_technical",
    round_name="the first consisted of a series of fast-paced estimation-style questions",
    section_context="4 interviews total; the next 3 focused on math (probability, stochastic processes) and game theory; offer received without a superday",
    question_type="fermi_estimation",
    question_text="There were many estimation questions which you have to be ready for. There is calculus, combinatorics, etc. to be done in 30 second time intervals for the first interview.",
    source_quote="There is calculus, combinatorics, etc. to be done in 30 second time intervals for the first interview.",
    poster_context=("Anonymous WSO entry, 'Quant Trading Intern Interview - Prop Trading', anonymous EMPLOYEE "
                    "in New York (i.e. the poster took the offer), Interviewed: September 2022, "
                    "Date Submitted: Nov 18, 2022, Accepted Offer, Applied Online."),
    doubt=WSO_DOUBT + " Describes the 30-second-per-question format rather than any question; valuable mainly as corroboration of Five Rings' timed first round from someone who accepted an offer.")

# ---------------- Akuna junior trader ----------------
add(firm="Akuna Capital", source_url=WSO_AK, level="unknown", role_track="quant_trader",
    post_date="2025-11", round="unknown", round_name="Junior trader Interview - Sales and Trading",
    question_type="mental_math_speed",
    question_text="Doing mental math without paper pen and no calculators allowed",
    source_quote="Doing mental math without paper pen and no calculators allowed",
    poster_context="Anonymous WSO entry, 'Junior trader Interview - Sales and Trading', Interviewed: November 2025.",
    doubt=WSO_DOUBT + " States the constraint (no paper, no calculator) but reproduces no arithmetic item.")

# ---------------- Glassdoor: Five Rings Quant Trader Intern ----------------
GD_FR = "https://www.glassdoor.com/Interview/Five-Rings-Quant-Trader-Intern-Interview-Questions-EI_IE375785.0,10_KO11,30.htm"
GD_DOUBT = ("Glassdoor blocks direct fetching from this environment; I read the page through the r.jina.ai "
            "text proxy, and Glassdoor entries are anonymous and unverified, with only the posting date shown "
            "(not necessarily the interview date).")

add(firm="Five Rings", source_url=GD_FR, source_type="glassdoor", office="New York, NY",
    level="internship", role_track="quant_trader", post_date="2026-02-12",
    round="online_assessment", round_name="OA",
    section_context="OA was on mental math, probability, and geometry; 'You need to answer the questions extremely quickly.'",
    question_type="mental_math_speed",
    question_text="Estimating the values of log",
    source_quote="OA was on mental math, probability, and geometry. You need to answer the questions extremely quickly.",
    access="full_text", retrieval_method="webfetch",
    poster_context=("Glassdoor 'Quant Trader Intern Interview', Anonymous Interview Candidate, New York, NY, "
                    "posted Feb 12, 2026, No offer, Neutral experience, Difficult interview."),
    doubt=GD_DOUBT + " The question itself is logged as a four-word fragment ('Estimating the values of log') with no argument or accuracy target, so it is a topic label more than a question.")

add(firm="Five Rings", source_url=GD_FR, source_type="glassdoor", office="New York, NY",
    level="internship", role_track="quant_trader", post_date="2025-04-22",
    round="online_assessment", round_name="the OA",
    section_context="Is rapid fire, with ~20 mins for 15 of these difficult questions",
    question_type="fermi_estimation",
    question_text="estimating the Arc length of sin(x) from 0 to pi",
    source_quote="Only did the OA, got questions such as estimating the Arc length of sin(x) from 0 to pi. Is rapid fire, with ~20 mins for 15 of these difficult questions.",
    access="full_text", retrieval_method="webfetch",
    poster_context=("Glassdoor 'Quant Trader Intern Interview', Anonymous Interview Candidate, New York, NY, "
                    "posted Apr 22, 2025, No offer, Neutral experience, Difficult interview."),
    doubt=GD_DOUBT + " This closely parallels the WSO Five Rings entry 'Calculate the length of x^2 from 0 to 9', which is either strong corroboration that Five Rings asks timed arc-length estimation or evidence that one recall seeded the other.")

add(firm="Five Rings", source_url=GD_FR, source_type="glassdoor", office="unknown",
    level="internship", role_track="quant_trader", post_date="2026-04-07",
    round="phone_technical", round_name="hour long interview with mostly technical questions",
    section_context="'The interviewer said there were a couple of rounds to get the winternship role'",
    question_type="probability",
    question_text="Quite hard, few probability questions but they did give hints",
    source_quote="Quite hard, few probability questions but they did give hints",
    access="full_text", retrieval_method="webfetch",
    poster_context=("Glassdoor 'Quant Trader Intern Interview', Anonymous Interview Candidate, posted Apr 7, 2026, "
                    "No offer, Negative experience, Difficult interview; refers to a 'winternship' (winter internship)."),
    doubt=GD_DOUBT + " No question text at all is given — only that the round contained a few probability questions with hints. Kept purely as round-level evidence.")

with io.open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", len(rows), "->", OUT)
