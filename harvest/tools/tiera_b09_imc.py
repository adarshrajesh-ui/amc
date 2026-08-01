#!/usr/bin/env python3
"""IMC Trading: a Launchpad HireVue recall, a Chicago SWE-intern OA note, and the WSO
quantitative-trader intern superday write-up.

The Launchpad items come from a forum thread hosted on everythingquant.com. That domain
is on this project's prep-vendor exclusion list, and the exclusion is about who attests a
question -- here the attester is a dated forum user recounting his own sitting, not the
vendor's editorial. The records go in with that conflict stated in full in `doubt` so a
reviewer can drop them on one grep if they disagree.
"""
import sys

sys.path.insert(0, "/workspace/harvest/tools")
import tiera_lib

# ------------------------------------------------------- IMC Launchpad HireVue (forum)

EQ_URL = "https://everythingquant.com/forum/post/imc-launchpad-hirevue-oa/"
EQ_LIST = ('Yes, it was pretty easy. 3 technical questions, followed by 3 behavioural '
           'questions. 1. Involved mean/median of sticks 2. Simple expected value '
           'calculation for stocks 3. Rates of change for trains 4. "Introduce yourself" '
           '5. "What was a time where you failed, and how did you learn and recover from '
           'the situation?" 6. "What is your greatest achievement?"')
EQ_STOCK = ('The stock question was something like, "you take 1% more trades per day, but '
            'get 1% less profit for all your trades. Should you do the extra 1% of trades?". '
            'Cannot precisely remember the other two.')
EQ_POSTER = ("u/digress_regress on the EverythingQuant forum, replying 495 days before a "
             "2026-08-01 fetch (so roughly 2025-03) to u/TheNotoriousBID's thread 'IMC "
             "Launchpad Hirevue OA' ('Anyone done the hirevue oa for imc launchpad? How was "
             "it? What did they ask?'). Says of the assessment: 'Yes, it was pretty easy.'")
EQ_DOUBT = ("Hosted on everythingquant.com, which this project treats as a prep-vendor / "
            "content-farm domain and therefore as negative evidence; the mitigating fact is "
            "that this is a user forum thread with dated back-and-forth replies rather than "
            "vendor editorial, and the poster himself says he 'cannot precisely remember' two "
            "of the three technical items, so the labels are approximate.")

EQ = [
    ("Involved mean/median of sticks", "statistics_regression", EQ_LIST),
    ("Simple expected value calculation for stocks", "expected_value", EQ_LIST),
    ("Rates of change for trains", "logic_brainteaser", EQ_LIST),
    ('"Introduce yourself"', "behavioral", EQ_LIST),
    ('"What was a time where you failed, and how did you learn and recover from the situation?"',
     "behavioral", EQ_LIST),
    ('"What is your greatest achievement?"', "behavioral", EQ_LIST),
    ('you take 1% more trades per day, but get 1% less profit for all your trades. Should you '
     'do the extra 1% of trades?', "expected_value", EQ_STOCK),
]

recs = []
for qtext, qtype, quote in EQ:
    recs.append({
        "firm": "IMC Trading",
        "role_track": "unknown",
        "level": "unknown",
        "cycle": "unknown",
        "office": "unknown",
        "round": "online_assessment",
        "round_name": "hirevue oa for imc launchpad",
        "platform": "unknown",
        "section_context": "3 technical questions, followed by 3 behavioural questions",
        "question_type": qtype,
        "question_text": qtext,
        "question_text_en": None,
        "reported_answer": None,
        "source_url": EQ_URL,
        "source_type": "blog",
        "source_quote": quote,
        "source_language": "en",
        "post_date": "2025-03",
        "access": "full_text",
        "retrieval_method": "webfetch",
        "poster_context": EQ_POSTER,
        "doubt": EQ_DOUBT,
    })

# ------------------------------------------------------ IMC SWE intern OA (Taro, Chicago)

TARO_URL = ("https://www.jointaro.com/interviews/companies/imc-trading/experiences/"
            "software-engineer-internship-chicago-illinois-august-1-2025-no-offer-positive-"
            "0655bf94/")
recs.append({
    "firm": "IMC Trading",
    "role_track": "quant_developer",
    "level": "internship",
    "cycle": "unknown",
    "office": "Chicago, Illinois",
    "round": "online_assessment",
    "round_name": "The OA",
    "platform": "unknown",
    "section_context": "There were two questions in the OA, and I was allowed two hours to solve them",
    "question_type": "coding_algorithms",
    "question_text": "Object-oriented programming questions. You had to complete a half-completed class.",
    "question_text_en": None,
    "reported_answer": None,
    "source_url": TARO_URL,
    "source_type": "blog",
    "source_quote": ("The OA was really hard. There were two questions in the OA, and I was "
                     "allowed two hours to solve them. I was not able to solve either "
                     "question. lol lol."),
    "source_language": "en",
    "post_date": "2025-08-01",
    "access": "full_text",
    "retrieval_method": "webfetch",
    "poster_context": ("Anonymous Taro (jointaro.com) interview experience, 'IMC Trading "
                       "Software Engineer (Internship) Interview Experience - Chicago, "
                       "Illinois', dated August 1, 2025, marked 'Positive Experience / No "
                       "Offer'; the candidate solved neither OA question."),
    "doubt": ("The 'Questions' field gives a category, not a problem statement, so the actual "
              "task is unrecoverable; Taro also appends a separate machine-tagged list of "
              "LeetCode problems ('Asteroid Collision' etc.) to every company page, and those "
              "are NOT attributed to this candidate, so anyone reading the page could easily "
              "mistake site-generated content for this recall."),
})

# ------------------------------------- IMC quantitative trader intern superday (WSO, blocked)

WSO_URL = ("https://www.wallstreetoasis.com/company/imc-financial-markets/interview/"
           "quantitative-trader-intern-1")
WSO_POSTER = ("Wall Street Oasis company-page interview entry, 'Intern Interview - IMC "
              "Financial Markets (Chicago)', filed by a quantitative-trader intern candidate "
              "who went OA -> recruiter call -> two back-to-back trader technicals -> "
              "superday and declined to share technical specifics ('While I can't share "
              "specifics').")
WSO_DOUBT = ("wallstreetoasis.com/company/ is behind Cloudflare from this host, so the text "
             "was only ever seen as a search-engine excerpt and could not be re-read in "
             "context; the same candidate explicitly withholds the technical questions, so "
             "only the behavioural prompts survive and they may be paraphrased.")
WSO_BEHAV = ('Some q\'s include "what would you do if trading doesn\'t work out", "what makes '
             'a good trader" and multiple stories of past failure and how you dealt with it.')

for qtext, qtype, quote, rnd, rname in [
    ('what would you do if trading doesn\'t work out', "behavioral", WSO_BEHAV, "superday",
     "The final superday consists of lunch, trading-desk shadow, 2 technicals and 1 behavioural"),
    ('what makes a good trader', "behavioral", WSO_BEHAV, "superday",
     "The final superday consists of lunch, trading-desk shadow, 2 technicals and 1 behavioural"),
    ("questions mainly assess how you make bets / decisions and how you justify them / react "
     "to being wrong", "betting_odds_arbitrage",
     "which is 2 back-to-back 1-on-1 interviews with traders asking open ended questions. "
     "While I can't share specifics, no preparation is really needed (aside from some game "
     "theory ideas) as questions mainly assess how you make bets / decisions and how you "
     "justify them / react to being wrong.",
     "phone_technical", "a technical interview, which is 2 back-to-back 1-on-1 interviews with traders"),
    ("Technicals included a trading simulator and a more classic QT interview but very open "
     "ended.", "trading_game",
     "Technicals included a trading simulator and a more classic QT interview but very open "
     "ended. Both of these cannot be prepped for and you will make loads of mistakes, but "
     "they are testing how quickly you can recover from these mistakes and how you respond "
     "to feedback.",
     "superday", "The final superday"),
]:
    recs.append({
        "firm": "IMC Trading",
        "role_track": "quant_trader",
        "level": "internship",
        "cycle": "unknown",
        "office": "Chicago",
        "round": rnd,
        "round_name": rname,
        "platform": "unknown",
        "section_context": None,
        "question_type": qtype,
        "question_text": qtext,
        "question_text_en": None,
        "reported_answer": None,
        "source_url": WSO_URL,
        "source_type": "wso",
        "source_quote": quote,
        "source_language": "en",
        "post_date": "unknown",
        "access": "snippet_only",
        "retrieval_method": "websearch_snippet",
        "poster_context": WSO_POSTER,
        "doubt": WSO_DOUBT,
    })

tiera_lib.write(recs)
