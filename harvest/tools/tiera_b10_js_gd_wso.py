#!/usr/bin/env python3
"""Jane Street: Glassdoor quantitative-researcher entries and a WSO quantitative-trading
intern entry.

Both hosts block direct fetching from here, so these are search-engine excerpts and are
labelled snippet_only. Only spans that appeared unbroken inside a single highlight block
are quoted; anywhere the excerpt showed an ellipsis the span was split rather than
stitched, because stitching across a gap manufactures text nobody wrote.
"""
import sys

sys.path.insert(0, "/workspace/harvest/tools")
import tiera_lib

GD_URL = ("https://www.glassdoor.com/Interview/Jane-Street-Quantitative-Researcher-"
          "Interview-Questions-EI_IE255549.0,11_KO12,35.htm")
GD_POSTER = ("Anonymous entries on the Glassdoor 'Jane Street Quantitative Researcher "
             "interview questions' page; each is filed by a self-identified candidate for "
             "the Quantitative Researcher role, and none of them states a level or cycle.")
GD_DOUBT = ("Anonymous and unverified: Glassdoor rewards posting an interview with access to "
            "other people's, which incentivises thin or invented entries, and the page could "
            "not be re-read directly because Glassdoor blocks this host -- only the "
            "search-engine excerpt was ever visible, so surrounding context is missing.")

GD = [
    ("Expected value of a sequential throw game", "expected_value",
     "probability questions, dice, etc. not too hard if you have prepared, so do many "
     "probability questions beforehand, focusing on expected value, sequential throws, mixed "
     "card games and so forth. several rounds with different questions each time",
     "unknown", "several rounds with different questions each time"),
    ("some typical stochastic analysis question about martingale, bs model, and simple SDE "
     "solving", "statistics_regression",
     "first is the math part, as some typical stochastic analysis question about martingale, "
     "bs model, and simple SDE solving. Second part is coding test,",
     "unknown", "first is the math part"),
    ("2 python code problems with leed code hard level questions.", "coding_algorithms",
     "2 python code problems with leed code hard level questions.",
     "unknown", "Second part is coding test"),
    ("A typical question is like given a game, what is the optimal strategy?",
     "poker_game_theory",
     "Solve math puzzles involving probability and game theory. The problems are essentially "
     "the same as the trader interviews. A typical question is like given a game, what is the "
     "optimal strategy? Some questions are pretty open ended.",
     "unknown", "Solve math puzzles involving probability and game theory"),
    ("Probability and Game Theory, optimal strategy and the expected return",
     "poker_game_theory",
     "Probability and Game Theory, optimal strategy and the expected return",
     "unknown", "Quantitative Researcher Interview"),
]

recs = []
for qtext, qtype, quote, rnd, rname in GD:
    recs.append({
        "firm": "Jane Street",
        "role_track": "quant_researcher",
        "level": "unknown",
        "cycle": "unknown",
        "office": "unknown",
        "round": rnd,
        "round_name": rname,
        "platform": "unknown",
        "section_context": None,
        "question_type": qtype,
        "question_text": qtext,
        "question_text_en": None,
        "reported_answer": None,
        "source_url": GD_URL,
        "source_type": "glassdoor",
        "source_quote": quote,
        "source_language": "en",
        "post_date": "unknown",
        "access": "snippet_only",
        "retrieval_method": "websearch_snippet",
        "poster_context": GD_POSTER,
        "doubt": GD_DOUBT,
    })

# --------------------------------------------------------- WSO Jane Street intern (NY)

WSO_URL = ("https://www.wallstreetoasis.com/company/jane-street-capital/interview/"
           "quantitative-trading-5")
WSO_QUOTE = ("There is no Online Assessments and if you pass the resume stage they'll move "
             "straight to the in person interview. The first round interview is calculating "
             "basic EVs related to many different scenarios and the level of difficulty is "
             "about the problems in the green book. The second round is playing a game with a "
             "trader but I guess they focus more on how you approach the problem and how you "
             "communicate rather than figuring out the right solution in the first try.")
WSO_POSTER = ("Wall Street Oasis entry 'Intern Interview - Jane Street Capital (New York)', "
              "Group/Division Quantitative Trading, interviewed October 2025, length of "
              "process 1-2 months, '1 on 1 Interview'.")

for qtext, qtype, rnd, rname in [
    ("The first round interview is calculating basic EVs related to many different scenarios "
     "and the level of difficulty is about the problems in the green book.",
     "expected_value", "onsite", "The first round interview"),
    ("The second round is playing a game with a trader but I guess they focus more on how you "
     "approach the problem and how you communicate rather than figuring out the right "
     "solution in the first try.",
     "trading_game", "trading_game", "The second round"),
]:
    recs.append({
        "firm": "Jane Street",
        "role_track": "quant_trader",
        "level": "internship",
        "cycle": "unknown",
        "office": "New York",
        "round": rnd,
        "round_name": rname,
        "platform": "unknown",
        "section_context": "There is no Online Assessments",
        "question_type": qtype,
        "question_text": qtext,
        "question_text_en": None,
        "reported_answer": None,
        "source_url": WSO_URL,
        "source_type": "wso",
        "source_quote": WSO_QUOTE,
        "source_language": "en",
        "post_date": "2025-10",
        "access": "snippet_only",
        "retrieval_method": "websearch_snippet",
        "poster_context": WSO_POSTER,
        "doubt": ("The candidate characterises the round rather than reproducing a question, "
                  "and explicitly benchmarks the difficulty against the green book, so what "
                  "survives here is a difficulty claim rather than an attested problem; the "
                  "WSO company pages are Cloudflare-blocked from this host, so only the "
                  "search excerpt was seen."),
    })

tiera_lib.write(recs)
