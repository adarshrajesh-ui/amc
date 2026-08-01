#!/usr/bin/env python3
"""p18: teamblind company interview boards.

Each Blind company page exposes /company/<Slug>/posts/<slug>-interview, a listing
of every interview-tagged thread for that firm. Walking those eight listings gave
209 thread URLs, all of which curl fetches whole; blind_comments.py then reads
the JSON-LD comment tree that a tag-stripping reader cannot see.

DRW, Five Rings and Old Mission returned nothing usable from this route — Blind
is a tech-employee board, and those three recruit mostly traders — so everything
below is HRT, Two Sigma or Jump.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p18_blind_boards.jsonl")
rows = []

BLIND_DOUBT = ("Blind verifies the poster's employer, not their candidacy, and threads are "
               "pseudonymous; nothing here can be tied to a named person or a dated application. ")


def add(**kw):
    rec = {
        "firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
        "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
        "section_context": None, "question_type": "other", "question_text": None,
        "question_text_en": None, "reported_answer": None, "source_url": None,
        "source_type": "blind", "source_quote": None, "source_language": "en",
        "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": None, "doubt": None,
    }
    rec.update(kw)
    for k in ("firm", "question_text", "source_url", "source_quote", "doubt"):
        assert rec[k], "missing %s in %r" % (k, rec.get("question_text"))
    assert len(rec["source_quote"]) >= 20, "short quote: %r" % rec["source_quote"]
    rows.append(rec)


# ============================================================ Hudson River Trading
HRT = "https://www.teamblind.com/post/hudson-river-trading-interview-process-87mxp0h4"
BALI = ("Blind user 'balibalo' answering an OP who asked what to expect in the HRT C++ engineer "
        "on-site loop; says further down the thread that they got the offer but turned it down "
        "after six months of negotiation because HRT 'could barely beat my TC at Nvidia'")
BALI_DOUBT = (BLIND_DOUBT + "The poster opens with 'Few years ago when I interviewed i got:', so "
              "the account is undated and several years stale by their own admission. ")

add(firm="Hudson River Trading", role_track="quant_developer", level="experienced",
    round="onsite", round_name="2h in front of a computer to solve 4 questions",
    section_context="2h in front of a computer to solve 4 questions",
    question_type="coding_algorithms",
    question_text=("First one was a warm up to see if you can do some parsing and be careful about "
                   "edge condition. Second one was a simple DS to implement but I think they were "
                   "looking for real world efficiency not just the right complexity. Last two were "
                   "a simple algorithm question, last ones be presented as a bonus question on top "
                   "of the third question but I suspect it was actually needed."),
    reported_answer="I was done in about 1h and used 30 more minutes to clean up the code.",
    source_url=HRT,
    source_quote=("2h in front of a computer to solve 4 questions. First one was a warm up to see "
                  "if you can do some parsing and be careful about edge condition."),
    post_date="2023-05-04", poster_context=BALI,
    doubt=BALI_DOUBT + "Each of the four is described by what it tested rather than what it asked.")

add(firm="Hudson River Trading", role_track="quant_developer", level="experienced",
    round="onsite", round_name="The other interview were less focused on coding but more on finding the right approach",
    question_type="coding_algorithms",
    question_text="One question was about optimization of a backtracking problem, one was more a math question.",
    source_url=HRT,
    source_quote=("One question was about optimization of a backtracking problem, one was more a "
                  "math question."),
    post_date="2023-05-04", poster_context=BALI,
    doubt=BALI_DOUBT + "The 'math question' is left entirely unspecified.")

add(firm="Hudson River Trading", role_track="quant_developer", level="experienced",
    round="onsite", round_name="The other interview were less focused on coding",
    question_type="other",
    question_text="Finally last question was about memory management.",
    source_url=HRT,
    source_quote="Finally last question was about memory management.",
    post_date="2023-05-04", poster_context=BALI, doubt=BALI_DOUBT + "A topic label, not a question.")

add(firm="Hudson River Trading", role_track="quant_developer", level="unknown",
    round="onsite", round_name="stages", question_type="coding_algorithms",
    question_text=("a large coding task where you take a spec and implement it, questions on "
                   'OS/"how computers work", and system design questions are the main things '
                   "usually covered."),
    source_url=HRT,
    source_quote=('If you do poorly you will be sent home early without all stages, but a large '
                  'coding task where you take a spec and implement it, questions on OS/"how '
                  'computers work", and system design questions are the main things usually covered.'),
    post_date="2023-05-04",
    poster_context="Blind user 'abchrt' in the same HRT C++ engineer on-site thread",
    doubt=(BLIND_DOUBT + "Phrased as what is 'usually covered' rather than what happened to this "
           "poster, so it may be second-hand generalisation; the detail that weak candidates are "
           "'sent home early without all stages' does read like inside knowledge."))

# ===================================================================== Two Sigma
TS_ADV = "https://www.teamblind.com/post/two-sigma-interview-advice-mazcdp6r"

add(firm="Two Sigma", role_track="quant_developer", level="experienced",
    round="online_assessment", round_name="the hackerrank test for two sigma",
    platform="HackerRank", section_context="you get 3 hours",
    question_type="coding_algorithms",
    question_text=("Two medium leetcode questions which I've seen before thus I was able to solve "
                   "it in 30 minutes (you get 3 hours)."),
    source_url=TS_ADV,
    source_quote=("Was able to get the hackerrank test for two sigma. Two medium leetcode questions "
                  "which I've seen before thus I was able to solve it in 30 minutes (you get 3 hours)."),
    post_date="2021-04-20",
    poster_context="Blind OP 'nycbatman', 2 years experience, TC 165K, interviewing for a Two Sigma SWE position",
    doubt=BLIND_DOUBT + "Characterises the paper by difficulty band only; no problem is named.")

add(firm="Two Sigma", role_track="quant_developer", level="unknown",
    round="phone_technical", round_name="interview", question_type="coding_algorithms",
    question_text=("Got a leetcode hard. Gave an ideal time complexity solution that the "
                   "interviewer said he hadnt seen before and was very creative. Got rejected lmao"),
    source_url=TS_ADV,
    source_quote=("Got a leetcode hard. Gave an ideal time complexity solution that the interviewer "
                  "said he hadnt seen before and was very creative. Got rejected lmao"),
    post_date="2021-04-20",
    poster_context="Blind user 'US Citizen' replying to the Two Sigma interview-advice OP",
    doubt=(BLIND_DOUBT + "The interesting content is the outcome, not the question, which is "
           "identified only as 'a leetcode hard'."))

add(firm="Two Sigma", role_track="quant_developer", level="unknown",
    round="onsite", round_name="Onsite was 3 rounds",
    section_context="1 LC hard, 1 LC hard, 2 LC medium + 1 LC Easy",
    question_type="coding_algorithms",
    question_text=("Onsite was 3 rounds: 1 LC hard, 1 LC hard, 2 LC medium + 1 LC Easy, if you "
                   "don't get all test cases for 1 problem you automatically get rejected"),
    source_url=TS_ADV,
    source_quote=("Onsite was 3 rounds: 1 LC hard, 1 LC hard, 2 LC medium + 1 LC Easy, if you don't "
                  "get all test cases for 1 problem you automatically get rejected"),
    post_date="2021-04-21",
    poster_context="Blind user 'qtcheeks' in the Two Sigma interview-advice thread",
    doubt=(BLIND_DOUBT + "The claim of an automatic rejection rule for a single failed test case is "
           "the poster's inference about Two Sigma's internal bar, not something a candidate can observe."))

add(firm="Two Sigma", role_track="quant_developer", level="unknown",
    round="onsite", round_name="interview", question_type="linear_algebra",
    question_text=("I was asked standard leetcode (pretty easy ones actually) plus one guy wanted "
                   "me to do some linear algebra derivations."),
    source_url=TS_ADV,
    source_quote=("I was asked standard leetcode (pretty easy ones actually) plus one guy wanted me "
                  "to do some linear algebra derivations. I hadn't touched linalg in years and "
                  "didn't remember shit about doing matrix math, so I bombed that one"),
    post_date="2021-04-21",
    poster_context="Blind user 'jybubdckb' in the Two Sigma interview-advice thread, who says they believe the linear algebra round is what sank them",
    doubt=BLIND_DOUBT + "Which derivations were asked is not recorded.")

add(firm="Two Sigma", role_track="quant_developer", level="unknown",
    round="onsite", round_name="the second round of virtual onsites",
    section_context="the first one was 3 tech interviews", question_type="coding_algorithms",
    question_text="The tech questions were pretty tough. Graph, DFS and DP based.",
    source_url="https://www.teamblind.com/post/two-sigma-second-onsite-round-eyjckwjb",
    source_quote="The tech questions were pretty tough. Graph, DFS and DP based.",
    post_date="2021-07-24",
    poster_context="Blind OP 'cubes3', who had completed a first virtual onsite of 3 technical interviews at Two Sigma and was asking what the second round would hold",
    doubt=BLIND_DOUBT + "Three topic labels and nothing more.")

add(firm="Two Sigma", role_track="quant_developer", level="unknown",
    round="online_assessment", round_name="the OA",
    section_context="2 coding and one systems / sys design round to follow",
    question_type="coding_algorithms",
    question_text="Their OA questions felt like LC mediums (?)",
    source_url="https://www.teamblind.com/post/two-sigma-interview-prep-bmq3cgkd",
    source_quote=("Their OA questions felt like LC mediums (?) . Any insights into what to expect "
                  "and focus on while preparing?"),
    post_date="2024-10-11",
    poster_context="Blind OP 'KeQe71', who had passed the Two Sigma OA and had 2 coding plus one systems/system-design round scheduled",
    doubt=BLIND_DOUBT + "The poster's own question mark shows they are unsure of the difficulty band they are reporting.")

# ==================================================================== Jump Trading
JUMP = "https://www.teamblind.com/post/jump-trading-interview-process-swe-k5k5jexb"

add(firm="Jump Trading", role_track="quant_developer", level="experienced",
    round="onsite", round_name="3 rounds of live coding interviews",
    section_context="online codility test then 3 rounds of live coding interviews",
    platform="unknown", question_type="coding_algorithms",
    question_text=("Two of the questions were leetcode medium-ish. But not exactly leetcode "
                   "questions. The rest were not on leetcode but I would categorize them as high "
                   "medium. They do go very deep into optimization all the way to optimizing for "
                   "the underlying architecture"),
    source_url=JUMP,
    source_quote=("Two of the questions were leetcode medium-ish. But not exactly leetcode "
                  "questions. The rest were not on leetcode but I would categorize them as high "
                  "medium. They do go very deep into optimization all the way to optimizing for "
                  "the underlying architecture"),
    post_date="2022-05-08",
    poster_context=("Blind OP 'LETU43', 5 years experience, interviewing for a Jump Trading SWE "
                    "role; had completed the online Codility test and 3 rounds of live coding and "
                    "was asking about the 3-4 hours of behavioural/technical still to come"),
    doubt=BLIND_DOUBT + "Difficulty bands rather than questions; the one concrete claim is that they push into architecture-level optimisation.")

add(firm="Jump Trading", role_track="quant_developer", level="experienced",
    round="onsite", round_name="behavioral discussions with prospective managers",
    section_context="3-4 more hours of 'behavioral/technical' interviews after the technical onsites",
    question_type="behavioral",
    question_text=("some latency sensitive c++ teams asked me questions about low level c++. Other "
                   "teams asked me about my scripting experience and asked me to walk them through "
                   "something I was proud of at my previous job. No coding."),
    source_url=JUMP,
    source_quote=("For example, some latency sensitive c++ teams asked me questions about low level "
                  "c++. Other teams asked me about my scripting experience and asked me to walk "
                  "them through something I was proud of at my previous job. No coding."),
    post_date="2022-05-08",
    poster_context=("Blind user 'AverageAF', between 2 and 5 years experience and ex-FAANG, "
                    "describing their own Jump Trading team-matching round; says 'Jump is an "
                    "awesome place to be!', so they appear to have joined"),
    doubt=BLIND_DOUBT + "Describes the shape of the team-matching conversations rather than any single question.")

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
