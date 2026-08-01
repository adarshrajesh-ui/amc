#!/usr/bin/env python3
"""p13: sources the earlier passes never reached.

- codeforces.com blog write-up of a D. E. Shaw SDE-intern OA (curl reaches it; full text)
- teamblind.com (plain curl returns the whole thread, so these are full_text)
- quantnet.com thread (curl gets 403 but WebFetch renders it; full_text via webfetch)
- 1point3acres tag/thread listing pages, whose row previews carry the question text
  itself. 1p3a is Cloudflare-blocked here, so those are snippet_only off WebSearch.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p13_blind_cf_quantnet_1p3a.jsonl")
rows = []


def add(**kw):
    rec = {
        "firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
        "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
        "section_context": None, "question_type": "other", "question_text": None,
        "question_text_en": None, "reported_answer": None, "source_url": None,
        "source_type": None, "source_quote": None, "source_language": "en",
        "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": None, "doubt": None,
    }
    rec.update(kw)
    for k in ("firm", "question_text", "source_url", "source_type", "source_quote", "doubt"):
        assert rec[k], "missing %s in %r" % (k, rec.get("question_text"))
    assert len(rec["source_quote"]) >= 20, "short quote: %r" % rec["source_quote"]
    rows.append(rec)


# ---------------------------------------------------------------- Codeforces
# AdityaDSingh, "De Shaw Online Assessment (OA) IIT Bhubaneswar (2025) (for SDE Intern)".
# Dated first-person write-up; each problem is reproduced in full.
CF = "https://codeforces.com/blog/entry/145050"
CF_CTX = "3 programming questions, separate timers: Q1 20 min, Q2 30 min, Q3 30 min; attempted in order, no going back"
CF_POSTER = "Codeforces user AdityaDSingh, writing up his own D. E. Shaw OA sat at IIT Bhubaneswar for the SDE Intern 2025 role"
CF_DOUBT = ("Self-reported and undated beyond '2025'; the problems are paraphrased into the poster's own "
            "wording rather than copied from the test screen, so exact constraints may drift.")

add(firm="D. E. Shaw", role_track="quant_developer", level="internship", cycle="2025",
    office="unknown", round="online_assessment", round_name="Online Assessment (OA)",
    platform="unknown", section_context=CF_CTX, question_type="coding_algorithms",
    question_text=("Problem 1: Divisible Substrings (20 mins). Given a string s of lowercase English letters "
                   "(length <= 1000), map each character c to a value using: val(c) = (c - 'a' + 1) / 3 + 1. "
                   "Count the number of substrings such that the sum of character values in the substring is "
                   "divisible by the length of that substring."),
    reported_answer="A brute-force O(n\u00b2) approach, utilizing a nested loop, is effective.",
    source_url=CF, source_type="blog",
    source_quote=("Count the number of substrings such that the sum of character values in the substring is "
                  "divisible by the length of that substring."),
    post_date="2025", poster_context=CF_POSTER, doubt=CF_DOUBT)

add(firm="D. E. Shaw", role_track="quant_developer", level="internship", cycle="2025",
    office="unknown", round="online_assessment", round_name="Online Assessment (OA)",
    platform="unknown", section_context=CF_CTX, question_type="coding_algorithms",
    question_text=("Problem 2: Airport Scanner Simulation (30 mins). Given two arrays: time[i] (time when the "
                   "i-th person wants to access the scanner, sorted) and direction[i] (0 if arrival, 1 if "
                   "departure). Only one person can use the scanner at a time. Priority rules: if the scanner "
                   "was used in the previous second, the same direction gets preference; if unused in the "
                   "previous second, departure (1) gets preference. Determine, for each person (in input "
                   "order), the exact time they pass through the scanner."),
    source_url=CF, source_type="blog",
    source_quote=("Determine, for each person (in input order), the exact time they pass through the scanner."),
    post_date="2025", poster_context=CF_POSTER, doubt=CF_DOUBT)

add(firm="D. E. Shaw", role_track="quant_developer", level="internship", cycle="2025",
    office="unknown", round="online_assessment", round_name="Online Assessment (OA)",
    platform="unknown", section_context=CF_CTX, question_type="coding_algorithms",
    question_text=("Problem 3: Nearest Sensor in Row or Column (30 mins). Given n sensors (n <= 10^5), each "
                   "with a unique string identifier and an (x, y) coordinate with 0 <= x, y <= 10^8. You are "
                   "given q queries, each being a string ID of a sensor. For each query, report the nearest "
                   "sensor in the same row (same y) or the same column (same x). If there are multiple such "
                   "sensors at the same distance, choose the one with the lexicographically smallest ID. If "
                   "there are no such sensors, return \"NONE\"."),
    source_url=CF, source_type="blog",
    source_quote=("For each query, report the nearest sensor in the same row (same y) or the same column "
                  "(same x). If there are multiple such sensors at the same distance, choose the one with the "
                  "lexicographically smallest ID. If there are no such sensors, return \"NONE\"."),
    post_date="2025", poster_context=CF_POSTER, doubt=CF_DOUBT)

# ---------------------------------------------------------------------- Blind
BL = "https://www.teamblind.com/post/swe-to-hedge-fundquant-firm-k6vktyvq"
BL_POSTER = ("Blind user posting under the Jump Trading company tag (handle akdn33), describing the loop they "
             "went through for an infra role; replying to an Amazon SWE asking how to move into HFT")
BL_DOUBT = ("Blind handles are only company-verified, not role-verified, and the poster describes the process "
            "generically ('typically look like this') rather than reciting one sitting, so this is a "
            "composite of their experience rather than a single dated recall.")

add(firm="Jump Trading", role_track="quant_developer", level="experienced", cycle="unknown",
    office="unknown", round="unknown",
    round_name="Virtual screen: this is either a take-home assignment or HackerRank challenge",
    platform="HackerRank", question_type="coding_algorithms",
    question_text=("Virtual screen take-home / HackerRank challenge related to markets: parsing market data to "
                   "build a price-time priority order book."),
    source_url=BL, source_type="blind",
    source_quote=("It\u2019s common for this to be related to markets, like parsing market data to build a "
                  "price-time priority order book."),
    post_date="2025-06-02", access="full_text", retrieval_method="webfetch",
    poster_context=BL_POSTER,
    doubt=BL_DOUBT + " Level is inferred from the thread being about an experienced SWE moving from big tech.")

add(firm="Jump Trading", role_track="quant_developer", level="experienced", cycle="unknown",
    office="unknown", round="onsite",
    round_name="on-site with 3-4 technical rounds and 1 leadership behavioral round",
    platform="unknown", question_type="coding_algorithms",
    question_text="Implement std:: classes like shared_ptr and vector.",
    source_url=BL, source_type="blind",
    source_quote="Expect to be asked to implement std:: classes like shared_ptr and vector.",
    post_date="2025-06-02", access="full_text", retrieval_method="webfetch",
    poster_context=BL_POSTER,
    doubt=BL_DOUBT + " Stated as an expectation to prepare for rather than 'they asked me this'.")

# ------------------------------------------------------------------- QuantNet
# quantnet.com 403s plain curl but renders for WebFetch; thread read in full.
QN = "https://quantnet.com/threads/technical-test-at-top-prop-shop.18878/"
QN_DOUBT_BASE = ("Topic-level recall: the poster names the subject areas that came up on the DRW test rather "
                 "than reproducing any single question, so this documents test composition, not a question. ")

add(firm="DRW", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="online test for quantitative research",
    platform="unknown", section_context="30 mins, 4 questions, pen and paper, no coding",
    question_type="probability",
    question_text="4 pretty difficult probability and linear algebra questions (DRW QR online test, 30 minutes, pen and paper, no coding).",
    source_url=QN, source_type="quantnet",
    source_quote=("For DRW QR role I got 30 mins to solve 4 pretty difficult probability and linear algebra "
                  "questions. Pen and paper, no coding. This was in late 2018"),
    post_date="2020-09", access="full_text", retrieval_method="webfetch",
    poster_context="QuantNet member binomial-torrent (joined 11/5/18), recalling their own DRW QR test from late 2018",
    doubt=QN_DOUBT_BASE + "Recalled roughly two years after the fact.")

add(firm="DRW", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="online test for quantitative research",
    platform="unknown", section_context="Like 13 questions I think with around 30 minutes",
    question_type="probability",
    question_text=("Stochastic processes (Markov), linear algebra, brain teaser, probability and other maths "
                   "\u2014 around 13 questions in about 30 minutes on the DRW quantitative research online test."),
    source_url=QN, source_type="quantnet",
    source_quote=("Last year I remember stochastic processes(I think Markova), linear algebra, brain teaser, "
                  "probability, and some other math that I can\u2019t remember. Like 13 questions I think with "
                  "around 30 minutes but I could be wrong"),
    post_date="2020-09", access="full_text", retrieval_method="webfetch",
    poster_context=("QuantNet member Michsund (joined 12/29/17), who later says 'mine was like Jan 2020', "
                    "answering another user asking how to prepare for the DRW QR online test"),
    doubt=QN_DOUBT_BASE + "The poster explicitly hedges ('I could be wrong') on both the count and the timing.")

add(firm="DRW", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="online assessment",
    platform="unknown", question_type="statistics_regression",
    question_text=("Mostly probability and statistics, plus the technicality behind machine learning models and "
                   "how to interpret the results \u2014 conditional probability, Bayes theorem, Markov chain, "
                   "linear algebra and basic calculus."),
    source_url=QN, source_type="quantnet",
    source_quote=("I gave the test and it was reasonable I guess...mostly probability and statistics...we need "
                  "to have some idea about the technicality behind machine learning models and more "
                  "importantly, how to interpret the results we get on using those models...might give more "
                  "importance to conditional probability, bayes theorem, markov chain, linear algebra, and "
                  "atleast basic calculus"),
    post_date="2020-09", access="full_text", retrieval_method="webfetch",
    poster_context=("QuantNet member Sahaana (joined 9/21/20), reporting back after actually sitting the DRW "
                    "quantitative research online test; elsewhere in the thread says it was '8 questions in 30 minutes'"),
    doubt=QN_DOUBT_BASE + "Poster is deliberately vague, possibly to avoid breaching the test's confidentiality.")

# --------------------------------------------------------------- 1point3acres
# Tag/listing pages: each table row shows the opening ~100 characters of the post,
# which is where posters put the questions. 1p3a is Cloudflare-blocked to this box,
# so the text below is what WebSearch returned, and access is snippet_only.
SNIP = dict(source_type="1point3acres", source_language="zh", access="snippet_only",
            retrieval_method="websearch_snippet")
P3A_DOUBT = ("Read from the tag-page row preview via search rather than the thread body \u2014 1point3acres is "
             "Cloudflare-blocked here and the full post sits behind a points paywall, so the question is "
             "truncated at the preview boundary and cannot be cross-checked against the poster's full text.")

TS22 = "https://www.1point3acres.com/bbs/tag/twosigma-1247-22.html"
add(firm="Two Sigma", role_track="quant_researcher", level="internship", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", section_context="OA\u7684\u4e09\u4e2a\u9898\u90fd\u662f\u6570\u503c\u76f8\u5173\u7684\uff0c\u96be\u5ea6\u4e0d\u5927\uff0c3\u4e2a\u5c0f\u65f6\u975e\u5e38\u5145\u88d5",
    question_type="coding_algorithms",
    question_text="\u6295\u7684quant researcher intern\uff0cOA\u7684\u4e09\u4e2a\u9898\u90fd\u662f\u6570\u503c\u76f8\u5173\u7684\uff0c\u96be\u5ea6\u4e0d\u5927\uff0c3\u4e2a\u5c0f\u65f6\u975e\u5e38\u5145\u88d5",
    question_text_en=("Applied for quant researcher intern; all three OA questions were numerical, not very "
                      "hard, and three hours was very generous."),
    source_url=TS22,
    source_quote="\u6295\u7684quant researcher intern\uff0cOA\u7684\u4e09\u4e2a\u9898\u90fd\u662f\u6570\u503c\u76f8\u5173\u7684\uff0c\u96be\u5ea6\u4e0d\u5927\uff0c3\u4e2a\u5c0f\u65f6\u975e\u5e38\u5145\u88d5",
    post_date="2021-12-30", poster_context="1point3acres \u6d77\u5916\u9762\u7ecf poster, thread bumped 2021-12-30",
    doubt=P3A_DOUBT + " Topic-level: says the questions were 'numerical' without naming them.", **SNIP)

add(firm="Two Sigma", role_track="data_scientist", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", question_type="coding_algorithms",
    question_text="OA\u5c31\u662f\u5f80\u5e38\u7684\u90a3\u4e24\u9053\u9898\u4e00\u4e2alinear interpolate\uff0c \u4e00\u4e2adaily temperature",
    question_text_en="The OA was the usual two questions: one linear interpolate, one daily temperature.",
    source_url=TS22,
    source_quote=("OA\u5c31\u662f\u5f80\u5e38\u7684\u90a3\u4e24\u9053\u9898\u4e00\u4e2alinear interpolate\uff0c "
                  "\u4e00\u4e2adaily temperature, \u6709\u5174\u8da3\u7684\u5c0f\u4f19\u4f34\u53ef\u4ee5\u79c1\u4fe1\u6211\u8ba8\u8bba\u89e3\u6cd5"),
    post_date="2021-12-27", poster_context="1point3acres \u6570\u79d1\u9762\u7ecf (data-science interview) board, thread bumped 2021-12-27",
    doubt=P3A_DOUBT + " Names the questions only by nickname, as problems already well known on the forum.", **SNIP)

add(firm="Two Sigma", role_track="unknown", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical", round_name="\u5e97\u9762 (phone screen)",
    platform="unknown", question_type="coding_algorithms",
    question_text="\u8001\u9898 random number generator\uff0c \u9700\u8981unique \u800c\u4e14\u5728\u7ed9\u5b9arange\u3002",
    question_text_en="The old question: a random number generator that must produce unique values within a given range.",
    source_url=TS22,
    source_quote=("OA\u56e0\u4e3a\u592a\u4e45\u4e4b\u524d\u5fd8\u8bb0\u4e86 \u4f46\u662f\u5e97\u9762\u8fd8\u662f\u8001\u9898 "
                  "random number generator\uff0c \u9700\u8981unique \u800c\u4e14\u5728\u7ed9\u5b9arange\u3002"),
    post_date="2021-09-30", poster_context="1point3acres \u6d77\u5916\u9762\u7ecf poster, thread bumped 2021-09-30",
    doubt=P3A_DOUBT, **SNIP)

add(firm="Two Sigma", role_track="unknown", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical", round_name="\u5e97\u9762 (phone screen)",
    platform="unknown", question_type="coding_algorithms",
    question_text="\u4e07\u5e74\u8001\u9898random number generator; \u53e6\u5916\u662fprocess vs threads + latency vs throughput",
    question_text_en=("The perennial old question, random number generator; also process vs threads + latency "
                      "vs throughput."),
    source_url=TS22,
    source_quote=("\u635e\u5230\u4e00\u4e2aTS\u5e97\u9762\uff0c\u4e07\u5e74\u8001\u9898random number generator; "
                  "\u53e6\u5916\u662fprocess vs threads + latency vs throughput"),
    post_date="2021-09-01", poster_context="1point3acres \u6d77\u5916\u9762\u7ecf poster, thread bumped 2021-09-01",
    doubt=P3A_DOUBT, **SNIP)

TS8 = "https://www.1point3acres.com/bbs/tag/twosigma-1247-8.html"
add(firm="Two Sigma", role_track="unknown", level="experienced", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", question_type="coding_algorithms",
    question_text="\u5730\u91cc\u5e38\u89c1\u7684\u4e24\u9053\u9898\uff0cinterpolation\u548clinear regression\u3002",
    question_text_en="The two questions commonly seen on the forum: interpolation and linear regression.",
    source_url=TS8,
    source_quote=("\u5341\u4e8c\u6708\u4efdOA\uff0c\u5c31\u662f\u5730\u91cc\u5e38\u89c1\u7684\u4e24\u9053\u9898\uff0c"
                  "interpolation\u548clinear regression\u3002"),
    post_date="2022-12",
    poster_context=("1point3acres poster who says \u201822\u5e74\u5341\u4e00\u6708\u4efd\u88ab\u730e\u5934\u642d\u8baa\u2019 "
                    "\u2014 approached by a headhunter, i.e. an experienced hire"),
    doubt=P3A_DOUBT, **SNIP)

add(firm="Two Sigma", role_track="data_scientist", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="\u5728\u7ebf\u7b14\u8bd5",
    platform="unknown", section_context="\u4e00\u5171\u4e09\u5200\u9898, \u7b2c\u4e09\u9898\u4e0d\u7b97\u5206",
    question_type="coding_algorithms",
    question_text=("1, linear Interpolation \u6cd5, \u4e0d\u5141\u8bb8\u8c03\u5305. 2, \u9884\u6d4b\u7ebd\u7ea6\u5e02\u7684"
                   "\u6e29\u5ea6, linear regression"),
    question_text_en=("1. Linear interpolation, no libraries allowed. 2. Predict New York City temperature, "
                      "linear regression."),
    source_url=TS8,
    source_quote=("Two sigma \u5728\u7ebf\u7b14\u8bd5\u9898, \u4e00\u5171\u4e09\u5200\u9898, \u7b2c\u4e09\u9898\u4e0d"
                  "\u7b97\u5206.1, linear Interpolation \u6cd5, \u4e0d\u5141\u8bb8\u8c03\u5305.2, \u9884\u6d4b\u7ebd"
                  "\u7ea6\u5e02\u7684\u6e29\u5ea6, linear regression, \u53ef\u4ee5\u7528"),
    post_date="2023-10-30", poster_context="1point3acres \u6570\u79d1\u9762\u7ecf board, poster \u5927\u5927\u51b0\u7cd6\u846b\u82a6, 2023-10-30",
    doubt=P3A_DOUBT, **SNIP)

add(firm="Two Sigma", role_track="unknown", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", section_context="\u4e24\u9053\u5fc5\u505a\u9898\uff0c\u4e00\u9053\u9009\u505a\u9898",
    question_type="coding_algorithms",
    question_text=("\u7b2c\u4e00\u9898\u662f\u4e00\u5806\u70b9\u7684\u7ebf\u6027\u63d2\u503c\uff0c\u7b2c\u4e8c\u9898\u662fNY"
                   "\u548c\u4e00\u4e9btown\u7684\u6570\u636e\u5904\u7406"),
    question_text_en=("Question 1 is linear interpolation over a set of points; question 2 is data processing "
                      "on NY and some towns."),
    source_url=TS8,
    source_quote=("\u6536\u5230OA\uff0c\u4e24\u9053\u5fc5\u505a\u9898\uff0c\u4e00\u9053\u9009\u505a\u9898\uff0c\u5730"
                  "\u91cc\u9762\u6709\u5b8c\u5168\u4e00\u6837\u7684\u9762\u7ecf\uff0c\u7b2c\u4e00\u9898\u662f\u4e00"
                  "\u5806\u70b9\u7684\u7ebf\u6027\u63d2\u503c\uff0c\u7b2c\u4e8c\u9898\u662fNY\u548c\u4e00\u4e9btown"
                  "\u7684\u6570\u636e\u5904\u7406"),
    post_date="2023-01-18", poster_context="1point3acres \u6d77\u5916\u9762\u7ecf poster \u5c0f\u4ea9_883c82e, timeline dated 01/18/2023",
    doubt=P3A_DOUBT, **SNIP)

add(firm="Two Sigma", role_track="quant_developer", level="internship", cycle="unknown",
    office="UK", round="online_assessment", round_name="ot",
    platform="unknown", section_context="90\u5206\u949f\u4e24\u9898",
    question_type="coding_algorithms",
    question_text=("\u7533\u8bf7\u7684\u662fsde intern\uff0c90\u5206\u949f\u4e24\u9898\uff0c\u7b2c\u4e00\u9898\u53ef"
                   "\u80fd\u662fleetcode easy/medium\uff0c\u7b2c\u4e8c\u9898\u6bd4\u8f83\u96be"),
    question_text_en=("Applied for SDE intern; 90 minutes, two questions. The first is maybe LeetCode "
                      "easy/medium, the second is harder."),
    source_url=TS8,
    source_quote=("\u5750\u6807\u82f1\u56fd\uff0c\u7533\u8bf7\u7684\u662fsde intern\uff0c90\u5206\u949f\u4e24\u9898"
                  "\uff0c\u7b2c\u4e00\u9898\u53ef\u80fd\u662fleetcode easy/medium\uff0c\u7b2c\u4e8c\u9898\u6bd4"
                  "\u8f83\u96be\u3002\u539f\u9898\u8bf7\u89c1\u5730\u91cc\u522b\u7684\u5e16\u5b50\u3002\u7b2c\u4e00"
                  "\u9898\uff1amissin"),
    post_date="2023-03-01", poster_context="1point3acres poster Leahhh147, UK-based SDE intern applicant",
    doubt=P3A_DOUBT + " The preview cuts off mid-word ('\u7b2c\u4e00\u9898\uff1amissin'), so the first question is only partly legible.",
    **SNIP)

TS5 = "https://www.1point3acres.com/bbs/tag/twosigma-1247-5.html"
add(firm="Two Sigma", role_track="unknown", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", question_type="coding_algorithms",
    question_text="\u8fd8\u662f\u5730\u91cc\u90a3\u4e24\u9898\u30021. \u53cc\u6307\u9488+\u6392\u5e8f 2. \u4e8c\u5206\u6cd5",
    question_text_en="Still the same two questions as on the forum. 1. Two pointers + sorting. 2. Binary search.",
    source_url=TS5,
    source_quote=("\u8fd8\u662f\u5730\u91cc\u90a3\u4e24\u9898\u30021. \u53cc\u6307\u9488+\u6392\u5e8f2. \u4e8c\u5206"
                  "\u6cd5\uff11\uff10\u5206\u949f\u5c31\u505a\u5b8c\u4e86"),
    post_date="2025-11-15", poster_context="1point3acres \u6d77\u5916\u9762\u7ecf poster \u5fae\u4fe1\u7528\u6237_124b9f3, 2025-11-15; says HR reached out",
    doubt=P3A_DOUBT + " Describes the solution technique rather than the problem statement.", **SNIP)

add(firm="Two Sigma", role_track="unknown", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", section_context="OA\u4e24\u9053\uff0c\u5168\u90e8case pass\u4e86",
    question_type="coding_algorithms",
    question_text=("\u4e00\u9053\u662f\u5730\u91cc\u51fa\u73b0\u8fc7\u7684IPO\uff0cround robin\u539f\u7406\u3002\u4e00"
                   "\u9053\u662f\u5730\u7406\u51fa\u73b0\u8fc7\u7684\u84c4\u6c34\u6c60\uff0cdfs + \u4e00\u4e2amemo"
                   "\u53ef\u4ee5\u89e3\u51b3\u3002"),
    question_text_en=("One is the IPO question seen on the forum, based on round robin. One is the reservoir "
                      "question seen on the forum, solvable with dfs + a memo."),
    source_url=TS5,
    source_quote=("OA\u4e24\u9053\uff0c\u5168\u90e8case pass\u4e86\u3002\u4e00\u9053\u662f\u5730\u91cc\u51fa\u73b0"
                  "\u8fc7\u7684IPO\uff0cround robin\u539f\u7406\u3002\u4e00\u9053\u662f\u5730\u7406\u51fa\u73b0\u8fc7"
                  "\u7684\u84c4\u6c34\u6c60\uff0cdfs + \u4e00\u4e2amemo\u53ef\u4ee5\u89e3\u51b3\u3002"),
    post_date="2024-11-27", poster_context="1point3acres \u5730\u91cc\u533f\u540d\u7528\u6237, 2024-11-27",
    doubt=P3A_DOUBT, **SNIP)

TS30 = "https://www.1point3acres.com/bbs/tag/twosigma-1247-30.html"
add(firm="Two Sigma", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", question_type="coding_algorithms",
    question_text="OA\uff1a Friends circle & string chains",
    question_text_en="OA: Friends circle & string chains",
    source_url=TS30,
    source_quote=("OA\u53ef\u80fd\u6709\u70b9\u8fc7\u65f6\uff0c\u4f46\u662f\u7535\u8bdd\u9762\u9898\u76ee\u8fd8\u7b97"
                  "\u7ecf\u5178\u3002OA\uff1a Friends circle & string chains"),
    post_date="2020-12-20",
    poster_context="1point3acres poster songweaver, who says they interviewed with Two Sigma's \u91cf\u5316\u7814\u7a76\u7ec4 (quant research group)",
    doubt=P3A_DOUBT + " The poster themself flags the OA as possibly out of date (\u2018OA\u53ef\u80fd\u6709\u70b9\u8fc7\u65f6\u2019).",
    **SNIP)

add(firm="Two Sigma", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", question_type="coding_algorithms",
    question_text="OA\u662f\u4e07\u5e74\u4e0d\u53d8\u7684\u4e24\u9053\u9898\uff08FC & SC\uff09",
    question_text_en="The OA is the same two never-changing questions (FC & SC \u2014 Friends Circle & String Chains).",
    source_url=TS30,
    source_quote=("\u9762software engineer\u5c97\u4f4d\u3002\u5728\u7533\u8bf7\u63d0\u4ea4\u4e86\u4e00\u5468\u5185HR"
                  "\u8054\u7cfb\u4e86\u6211\uff0c\u6548\u7387\u8fd8\u662f\u4e0d\u9519\u7684\u3002OA\u662f\u4e07\u5e74"
                  "\u4e0d\u53d8\u7684\u4e24\u9053\u9898\uff08FC & SC\uff09\u3002"),
    post_date="2020-10-17", poster_context="1point3acres poster alexboyi, found through a headhunter, interviewing for software engineer",
    doubt=P3A_DOUBT + " 'FC & SC' is forum shorthand; my expansion to Friends Circle / String Chains is inferred from the sibling post on the same page.",
    **SNIP)

add(firm="Two Sigma", role_track="data_scientist", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="DS OA",
    platform="unknown", question_type="coding_algorithms",
    question_text="\u7b2c\u4e00\u9898\u662flinear interpolation \u7b2c\u4e8c\u9898\u662fNYC weather",
    question_text_en="Question 1 is linear interpolation, question 2 is NYC weather.",
    source_url=TS30,
    source_quote=("\u62a5\u4e00\u4e2a2 sigma DS OA \u7684data point - \u7b2c\u4e00\u9898\u662flinear "
                  "interpolation\u7b2c\u4e8c\u9898\u662fNYC weather"),
    post_date="2020-03-30", poster_context="1point3acres \u6570\u79d1\u9762\u7ecf poster samonia, 2020-03-30",
    doubt=P3A_DOUBT, **SNIP)

FR = "https://www.1point3acres.com/bbs/tag/fiverings-8581-1.html"
add(firm="Five Rings", role_track="unknown", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown",
    section_context="\u4e00\u517130\u5206\u949f\u5de6\u53f3\uff0c\u7136\u540e\u5206\u7ed9\u6bcf\u9053\u9898\u5927\u6982\u4e5f\u5c311\uff0c2\u5206\u949f",
    question_type="probability",
    question_text="\u4e00\u6839\u6728\u68d2\uff0c\u968f\u673a\u9009\u4e24\u4e2a\u70b9\u6298\u6210\u4e09\u6bb5\uff0c\u7ec4\u6210\u4e09\u89d2\u5f62\u7684\u6982\u7387\u662f\u591a\u5c11\uff1f",
    question_text_en=("A stick is broken at two randomly chosen points into three pieces \u2014 what is the "
                      "probability they form a triangle?"),
    source_url=FR,
    source_quote=("\u5206\u4eab\u4e00\u4e0bfive rings\u7684OA\u3002\u65f6\u95f4\u5f88\u7d27\uff0c\u4e00\u517130\u5206"
                  "\u949f\u5de6\u53f3\uff0c\u7136\u540e\u5206\u7ed9\u6bcf\u9053\u9898\u5927\u6982\u4e5f\u5c311\uff0c2"
                  "\u5206\u949f\u5427\u3002\u4f9d\u7a00\u8bb0\u5f97\u4e00\u4e9b\u9898\u4e00\u6839\u6728\u68d2\uff0c"
                  "\u968f\u673a\u9009\u4e24\u4e2a\u70b9\u6298\u6210\u4e09\u6bb5\uff0c\u7ec4\u6210\u4e09\u89d2\u5f62"
                  "\u7684\u6982\u7387\u662f\u591a\u5c11\uff1f"),
    post_date="2024-12-16", poster_context="1point3acres \u6d77\u5916\u9762\u7ecf poster sherrylou, 2024-12-16",
    doubt=P3A_DOUBT + " This is also a standard textbook problem (broken-stick triangle), so it is not "
                      "distinctive to Five Rings \u2014 but the attestation is a candidate recall, not a textbook.",
    **SNIP)

add(firm="Five Rings", role_track="quant_trader", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical", round_name="\u7b2c\u4e00\u8f6e\u662fHR",
    platform="unknown",
    section_context="HR\u4f1a\u8bfb\u9898\uff0c\u8bfb\u5b8c\u9898\u53ea\u670930\u79d2\u65f6\u95f4\u505a\u7b54",
    question_type="behavioral",
    question_text="\u6bd4\u8f83standard\u7684why trading, why fiverings",
    question_text_en="Fairly standard 'why trading, why Five Rings'.",
    source_url=FR,
    source_quote=("\u7b2c\u4e00\u8f6e\u662fHR\uff0c\u5148\u662f\u7b80\u5355\u95ee\u4e86\u4e00\u4e0b\u6bd4\u8f83"
                  "standard\u7684why trading, why fiverings \u7136\u540e\u76f4\u63a5\u8fdb\u5165\u77ed\u95ee\u9898"
                  "\u3002HR\u4f1a\u8bfb\u9898\uff0c\u8bfb\u5b8c\u9898\u53ea\u670930\u79d2\u65f6\u95f4\u505a\u7b54"),
    post_date="2024-07-28", poster_context="1point3acres poster \u5fae\u4fe1\u7528\u6237_st7pl, 2024-07-28",
    doubt=P3A_DOUBT + " The interesting detail is the 30-second answer clock, not the behavioural question itself.",
    **SNIP)

JT = "https://www.1point3acres.com/bbs/tag/jumptrading-8699-1.html"
add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", question_type="coding_algorithms",
    question_text=("C++\u7684dp\u5199\u4e00\u4e2aOrder Book Keeping\uff0c\u9700\u8981\u5904\u7406Order\u7684\u5404"
                   "\u79cd\u589e\u5220\u6539\u548c\u4ea4\u6613\u7684message\uff0c\u7136\u540e\u5b9e\u65f6\u8f93\u51fa"
                   "bid\u548cask price\u7684\u5bf9\u5e94\u4fe1\u606f\u548cshare\u91cf"),
    question_text_en=("Write an order book keeping system in C++: handle all the add/delete/modify and trade "
                      "messages for orders, then output in real time the corresponding bid and ask price "
                      "information and share quantities."),
    source_url=JT,
    source_quote=("Jump Trading OA \u7ed9\u5927\u5bb6\u53d1\u4e00\u4e2aJump Trading OA C++\u7684dp\u5199\u4e00\u4e2a"
                  "Order Book Keeping\uff0c\u9700\u8981\u5904\u7406Order\u7684\u5404\u79cd\u589e\u5220\u6539\u548c"
                  "\u4ea4\u6613\u7684message\uff0c\u7136\u540e\u5b9e\u65f6\u8f93\u51fabid\u548cask price\u7684\u5bf9"
                  "\u5e94\u4fe1\u606f\u548cshare\u91cf"),
    post_date="2025-07-14", poster_context="1point3acres \u6d77\u5916\u9762\u7ecf, \u533f\u540d poster, 2025-07-14",
    doubt=P3A_DOUBT, **SNIP)

add(firm="Jump Trading", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="OA",
    platform="unknown", section_context="\u4e24\u4e2a\u95ee\u9898\uff0c\u4e00\u5171125\u5206\u949f",
    question_type="coding_algorithms",
    question_text=("\u4e70\u5356\u80a1\u7968\uff0c\u7ed9\u4e00\u4e2a[stork price], \u4e00\u4e2a[sell pattern]\u3002"
                   "\u5176\u4e2dsell pattern\u548cbuy pattern\u662f\u7531-1\uff0c1\u7684\u6570\u7ec4\u7ec4\u6210\uff0c"
                   "1\u4ee3\u8868\u4e0a\u6da8\uff0c -1\u4ee3\u8868\u4e0b\u8dcc"),
    question_text_en=("Buying and selling stock: you are given a [stock price] array and a [sell pattern]. The "
                      "sell pattern and buy pattern are arrays of -1 and 1, where 1 means the price rose and "
                      "-1 means it fell."),
    source_url=JT,
    source_quote=("Jump Trading OA \u4e24\u4e2a\u95ee\u9898\uff0c\u4e00\u5171125\u5206\u949f[*]\u4e70\u5356\u80a1"
                  "\u7968\uff0c\u7ed9\u4e00\u4e2a[stork price], \u4e00\u4e2a[sell pattern], \u4e00\u4e2a. \u5176"
                  "\u4e2dsell pattern\u548cbuy pattern\u662f\u7531-1\uff0c1\u7684\u6570\u7ec4\u7ec4\u6210\uff0c1"
                  "\u4ee3\u8868\u4e0a\u6da8\uff0c -1\u4ee3\u8868\u4e0b\u8dcc"),
    post_date="2025-08-01", poster_context="1point3acres \u6d77\u5916\u9762\u7ecf, \u533f\u540d poster, 2025-08-01",
    doubt=P3A_DOUBT + " The preview contains an obvious typo ('stork price') and a dangling '\u4e00\u4e2a.', so the third input is unrecoverable.",
    **SNIP)

# 1p3a's English-language interview index exposes a one-line summary of each thread even
# when the body is paywalled; this one names three HRT Algo Dev intern OA questions.
HRT1 = "https://www.1point3acres.com/interview/thread/1141239"
HRT_Q = ("Summary of the hudson-river-trading 2026 Algorithm Developer Summer Intern OA covering fancy number "
         "identification, Reversi simulator, and non-binary tree traversal and merging.")
for qtext in ("fancy number identification", "Reversi simulator", "non-binary tree traversal and merging"):
    add(firm="Hudson River Trading", role_track="quant_developer", level="internship", cycle="2026",
        office="unknown", round="online_assessment",
        round_name="2026 Algorithm Developer Summer Intern Online Assessment",
        platform="unknown", section_context="three questions named in the thread summary",
        question_type="coding_algorithms", question_text=qtext,
        source_url=HRT1, source_type="1point3acres", source_quote=HRT_Q,
        source_language="en", post_date="unknown", access="snippet_only",
        retrieval_method="websearch_snippet",
        poster_context="1point3acres interview-thread index entry for a hudson-river-trading Algorithm Developer Summer Intern OA",
        doubt=("Only 1point3acres' own editorial one-line summary of the thread is public \u2014 the candidate's "
               "actual write-up is behind a login, so each question is a two-or-three-word label with no "
               "problem statement, and I could not confirm the posting date."))

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
