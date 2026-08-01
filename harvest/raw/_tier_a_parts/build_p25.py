#!/usr/bin/env python3
"""p25: the last few sources - QuantNet, eFinancialCareers, two 1point3acres replies.

Four odds and ends that did not belong in any earlier part:

* QuantNet thread 19368 - Akuna's trading-internship screen order (math exam, then
  personality test, then phone). curl gets a Cloudflare interstitial on quantnet, so
  this was read through the WebFetch renderer; labelled retrieval_method=webfetch,
  access=full_text because the whole thread was rendered, but the machine verifier
  will report it UNCHECKABLE from this box.
* eFinancialCareers' round-up of Jump probability questions. This is a compilation the
  outlet assembled from public Glassdoor and WSO submissions, not a first-person
  sitting, so access=compilation_only and the doubt field says so plainly. Included
  rather than dropped because the outlet names its sources and is not selling
  preparation; excluded from any claim about round or date.
* Two replies inside 1point3acres threads whose first posts were already mined but
  whose comment text was not. 1p3a Cloudflare-blocks this box, so both stay
  snippet_only / websearch_snippet.

Rejected while gathering these, all for selling OA/interview 代做 or 辅助 services or
being generated prep content: programhelp.net (+ its dev.to and medium.com@programhelp
mirrors), oavoservice.com, tradinginterview.com, tradermath.org, quantt.co.uk,
quantblueprint.com, everythingquant.com, techinterview.org, myntbit.com, applr.ai,
leakcode.dev, linkjob.ai, getsmartresume.com, interview-help.live.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p25_misc_sources.jsonl")
rows = []


def add(**kw):
    rec = {"firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
           "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
           "section_context": None, "question_type": "other", "question_text": None,
           "question_text_en": None, "reported_answer": None, "source_url": None,
           "source_type": "blog", "source_quote": None, "source_language": "en",
           "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
           "poster_context": None, "doubt": None}
    rec.update(kw)
    rows.append(rec)


# ------------------------------------------------------ QuantNet: Akuna screen order
add(firm="Akuna Capital", role_track="quant_trader", level="internship",
    round="math_sequences_test", round_name="the math exam and personality test",
    source_url="https://quantnet.com/threads/akuna-trading-internship-phone-interview.19368/",
    source_type="quantnet", post_date="2015-02-06", question_type="other",
    question_text="Akuna trading internship screen order: a math exam, then a personality test, "
                  "then a phone interview",
    section_context="personality test notification came 4 days after the math test",
    source_quote="I passed the math exam and personality test for the trading internship at "
                 "Akuna. Gonna have a phone interview next week. Anyone has any idea what will "
                 "come?",
    poster_context="QuantNet user 'Bingohu', joined 2014, 2 messages; opened the thread on "
                   "2015-02-06 and later replied 'I received the notification for personality "
                   "test 4 days after I wrote the math test. PS: I've already failed the phone "
                   "interview'",
    doubt="From 2015, so the pipeline has almost certainly changed - and the poster is asking "
          "what the phone interview contains rather than reporting it, so no question survives, "
          "only the order of the screens. quantnet Cloudflare-blocks this box, so the quote was "
          "read through a rendering proxy rather than raw bytes.")

# ------------------------------- eFinancialCareers: Jump probability question round-up
U = "https://www.efinancialcareers-canada.com/news/electronic-trading-interviews"
EFC_P = ("eFinancialCareers editorial round-up titled 'The interview questions of Jane Street, "
         "Jump and Citadel Securities'; the article states 'We've looked at public submissions "
         "from various sites like Glassdoor and Wall Street Oasis to find the most unusual "
         "examples'")
EFC_D = ("This is a journalist's compilation of questions scraped from Glassdoor and WSO, not a "
         "first-person sitting: no date, round, role track or candidate attaches to any single "
         "question, and eFinancialCareers does not link the individual submissions it drew from, "
         "so the chain of attestation cannot be walked back. Recorded as compilation_only for "
         "exactly that reason. The site is also behind an AWS WAF challenge from this box, so the "
         "text comes from a search-engine extract of the page rather than bytes I fetched.")
for qt, txt in [
    ("probability", "A bee starts at a hive. It has a 20% chance to move forward, a 50% chance "
                    "to stay still, and a 30% to move backward. What percentage of the time does "
                    "it spend in the hive?"),
    ("expected_value", "I'm dealing a deck of cards. You can stop it at any time and if the next "
                       "card is red, you win. What is the optimal strategy for winning?"),
    ("combinatorics", "There are four balls, two black and two white. You pick two and random and "
                      "flip their color from one to the other and repeat. How many times would "
                      "you do this to ensure all four balls are the same color?"),
    ("probability", "What is the probability that two people in a room full of 15 share the same "
                    "birthday?"),
]:
    add(firm="Jump Trading", role_track="unknown", level="unknown", round="unknown",
        round_name="Jump Trading Interview Questions", source_url=U, source_type="blog",
        post_date="unknown", question_type=qt, question_text=txt, source_quote=txt,
        access="compilation_only", retrieval_method="websearch_snippet",
        poster_context=EFC_P, doubt=EFC_D)

# ---------------------------- 1point3acres: reply inside the HRT Algo Dev OA thread
U = "https://www.1point3acres.com/bbs/thread-1022110-1-1.html"
add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    round="online_assessment", round_name="\u5728\u7ebf\u7b14\u8bd5", source_url=U,
    source_type="1point3acres", post_date="unknown", question_type="coding_algorithms",
    source_language="mixed", cycle="2024",
    section_context="150 \u5206\u949f 3\u9053\u9898 (150 minutes, 3 questions)",
    question_text="\u7b2c\u4e8c\u9898 union find\uff0c\u6700\u540ecount\u4e24\u4e2agroup\u7684"
                  "\u6210\u5458\u4e2a\u6570 \u7b2c\u4e09\u9898 \u7b2c\u4e00\u90e8\u5206"
                  "topological sort\uff1f",
    question_text_en="Question 2 is union-find, finally counting the members of the two groups. "
                     "Question 3: is the first part topological sort?",
    source_quote="\u7b2c\u4e8c\u9898 union find\uff0c\u6700\u540ecount\u4e24\u4e2agroup\u7684"
                 "\u6210\u5458\u4e2a\u6570 \u7b2c\u4e09\u9898 \u7b2c\u4e00\u90e8\u5206"
                 "topological sort\uff1f",
    access="snippet_only", retrieval_method="websearch_snippet",
    poster_context="A commenter on the 1point3acres HRT Algo Dev OA thread (original post: "
                   "2023 Oct-Dec, undergraduate, internship @hudson-river-trading, online "
                   "application, online test) who opens with '\u6700\u8fd1\u4e5f\u5728\u51c6"
                   "\u5907hrt oa\u6240\u4ee5\u5c1d\u8bd5\u7740\u60f3\u4e86\u4e00\u4e0b\u8fd9"
                   "3\u9053\u9898' - i.e. they are preparing for the same OA and reasoning "
                   "about the three questions the OP described",
    doubt="This is the single most important caveat on the record: the commenter is guessing at "
          "solutions to questions the OP described, not reporting questions they were asked. "
          "They end the sentence with a question mark. It is evidence about what HRT's questions "
          "2 and 3 were only to the extent the OP's description was accurate and the commenter "
          "read it right. 1point3acres Cloudflare-blocks this box, so this is a search extract.")

# --------------------------- 1point3acres: Old Mission 2024 NG SWE OA, tag-page row
U = "https://www.1point3acres.com/bbs/tag/old-mission-capital-8743-1.html"
add(firm="Old Mission Capital", role_track="quant_developer", level="new_grad",
    round="online_assessment", round_name="OA", source_url=U, source_type="1point3acres",
    post_date="2023-07-21", question_type="coding_algorithms", source_language="mixed",
    cycle="2024", section_context="\u63a8\u6d4b\u662f\u4e24\u4e2a\u5c0f\u65f6\uff1a30\u9053MC "
                                  "+ \u7b97\u6cd52\u9053",
    question_text="\u8001\u4efb\u52a1\u51e0\u5929\u524d\u53d1\u4e8624NG swe\uff0c\u6d77\u6295"
                  "\u7b2c\u4e8c\u5929\u6536\u5230OA\u3002\u63a8\u6d4b\u662f\u4e24\u4e2a\u5c0f"
                  "\u65f6\uff1a30\u9053MC + \u7b97\u6cd52\u9053\uff0c\u76ee\u6d4b\u9009\u62e9"
                  "\u9898\u4f1a\u8003\u7684\u6bd4\u8f83\u6742\u4e5f\u6bd4\u8f83\u5e95\u5c42",
    question_text_en="Old Mission put out the 2024 NG SWE role a few days ago; I got the OA the "
                     "day after a mass application. Guessing it is two hours: 30 multiple choice "
                     "plus 2 algorithm questions. My guess is the multiple choice will be pretty "
                     "miscellaneous and pretty low-level.",
    source_quote="\u8001\u4efb\u52a1\u51e0\u5929\u524d\u53d1\u4e8624NG swe\uff0c\u6d77\u6295"
                 "\u7b2c\u4e8c\u5929\u6536\u5230OA\u3002\u63a8\u6d4b\u662f\u4e24\u4e2a\u5c0f"
                 "\u65f6\uff1a30\u9053MC + \u7b97\u6cd52\u9053\uff0c\u76ee\u6d4b\u9009\u62e9"
                 "\u9898\u4f1a\u8003\u7684\u6bd4\u8f83\u6742\u4e5f\u6bd4\u8f83\u5e95\u5c42",
    access="snippet_only", retrieval_method="websearch_snippet",
    poster_context="1point3acres user '\u70b9\u51fb\u8fd9\u91cc\u70b9\u51fb\u8fd9\u91cc', "
                   "posted 2023-07-21 in \u6d77\u5916\u9762\u7ecf, 16 replies / 6374 views; "
                   "the poster asks how to prepare, using \u8001\u4efb\u52a1 ('old mission', a "
                   "literal-translation nickname) for the firm",
    doubt="The poster twice says \u63a8\u6d4b / \u76ee\u6d4b ('I'm guessing', 'my guess is'), so "
          "the 2-hour / 30-MC / 2-algorithm shape is their expectation before sitting the OA, "
          "not a report of having sat it. 1point3acres blocks this box, so it is a search "
          "extract of a tag-index row rather than the thread itself.")

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("%d records -> %s" % (len(rows), OUT))
