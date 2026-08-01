#!/usr/bin/env python3
"""p19: second reddit pass.

The first Arctic Shift sweep counted a 422 "Timeout. Maybe slow down a bit" as an
empty result, which silently wrote off every large subreddit. Re-running the same
queries one year-window at a time with a real backoff roughly doubled the corpus
(1,205 -> 2,476 firm-mentioning threads, ~26k comments) and surfaced the DRW and
Five Rings material below, neither of which the first pass had.

Same caveat as p16: read from the Arctic Shift mirror, since reddit.com refuses
this host.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p19_reddit_pass2.jsonl")
rows = []

MIRROR = ("Read from the Arctic Shift mirror of the reddit dump "
          "(arctic-shift.photon-reddit.com), because reddit.com refuses this host; the quote is "
          "verbatim from the archived comment body, so an edit or deletion after archiving would "
          "leave the live permalink out of step. ")


def add(**kw):
    rec = {
        "firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
        "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
        "section_context": None, "question_type": "other", "question_text": None,
        "question_text_en": None, "reported_answer": None, "source_url": None,
        "source_type": "reddit_thread", "source_quote": None, "source_language": "en",
        "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": None, "doubt": None,
    }
    rec.update(kw)
    rec["doubt"] = MIRROR + rec["doubt"]
    for k in ("firm", "question_text", "source_url", "source_quote", "doubt"):
        assert rec[k], "missing %s in %r" % (k, rec.get("question_text"))
    assert len(rec["source_quote"]) >= 20, "short quote: %r" % rec["source_quote"]
    rows.append(rec)


# ============================================================================ DRW
DRW_COD = "https://www.reddit.com/r/csMajors/comments/i9t195/drw_codility/"

add(firm="DRW", role_track="quant_developer", level="internship", office="unknown",
    round="online_assessment", round_name="DRW codility", platform="unknown",
    section_context="two questions", question_type="coding_algorithms",
    question_text=("The first question was a string based question. I would say that its difficulty "
                   "was Leetcode medium."),
    source_url=DRW_COD,
    source_quote=("1. The first question was a string based question. I would say that its "
                  "difficulty was Leetcode medium."),
    post_date="2020-10-03",
    poster_context=("r/csMajors commenter u/11AMBoi answering the 'DRW codility' thread, which was "
                    "opened by someone who had just been invited to the DRW SWE internship coding challenge"),
    doubt="Topic-level: gives the shape and difficulty band of the problem but not the problem.")

add(firm="DRW", role_track="quant_developer", level="internship", office="unknown",
    round="online_assessment", round_name="DRW codility", platform="unknown",
    section_context="two questions", question_type="coding_algorithms",
    question_text=("The second question was pretty tricky. I tried to think of a DP based solution "
                   "but it turned out to be more of a Math oriented problem. Definitely more like a "
                   "Leetcode medium to hard problem."),
    source_url=DRW_COD,
    source_quote=("2. The second question was pretty tricky. I tried to think of a DP based "
                  "solution but it turned out to be more of a Math oriented problem."),
    post_date="2020-10-03",
    poster_context="r/csMajors commenter u/11AMBoi in the 'DRW codility' thread",
    doubt=("Topic-level, and the only substantive claim — that it looked like DP but was really a "
           "maths problem — is the poster's own misreading rather than a description of the prompt."))

add(firm="DRW", role_track="quant_developer", level="internship", office="unknown",
    round="online_assessment", round_name="DRW codility", platform="unknown",
    section_context="2 LC mediums, and one Leetcode Hard",
    question_type="coding_algorithms",
    question_text=("It was a 2 LC mediums, and one Leetcode Hard. The evaluation of some was on "
                   "basis of correctness and other on basis of performance."),
    source_url=DRW_COD,
    source_quote=("Took mine today. It was a 2 LC mediums, and one Leetcode Hard. The evaluation of "
                  "some was on basis of correctness and other on basis of performance."),
    post_date="2020-09-05",
    poster_context="r/csMajors commenter u/chandlerbing__, reporting the same day they sat the DRW Codility test",
    doubt=("Same-day, so the recall is fresh, but it reports difficulty bands and the marking "
           "scheme rather than any question. Note it says three questions where the other commenter "
           "in the same thread says two, so the paper differed between candidates or one of them "
           "is misremembering."))

# ===================================================================== Five Rings
add(firm="Five Rings", role_track="unknown", level="unknown", office="unknown",
    round="phone_technical", round_name="final interview",
    section_context="in just five minutes", question_type="other",
    question_text=("five rings asked me to fix the OA i got an 8/10 on a month ago in just five "
                   "minutes. FIVE MINUTES."),
    source_url="https://www.reddit.com/r/csMajors/comments/1fw7lh1/keep_failing_final_interviews/",
    source_quote=("I've had terrible experiences with five rings and databricks in particular since "
                  "five rings asked me to fix the OA i got an 8/10 on a month ago in just five "
                  "minutes. FIVE MINUTES."),
    post_date="2024-10-04",
    poster_context=("r/csMajors OP u/Enough_Hospital9224, venting about repeatedly failing final "
                    "interviews; scored 8/10 on the Five Rings OA a month before this round"),
    doubt=("Written in frustration, and the poster does not say which OA questions they were made "
           "to revisit. What it does attest is an unusual round format — being handed back your own "
           "OA and given five minutes to repair it — which no other source in this file describes."))

add(firm="Five Rings", role_track="quant_trader", level="unknown", office="unknown",
    round="phone_technical", round_name="Five Rings QT Connect", question_type="behavioral",
    question_text=("I was asked to schedule an interview and they said that no technical questions "
                   "would be asked."),
    source_url="https://www.reddit.com/r/csMajors/comments/1hxmayj/five_rings_qt_connect_experienceinterview/",
    source_quote=("Also, I was asked to schedule an interview and they said that no technical "
                  "questions would be asked. Does anyone have experience with Five Rings behavioral "
                  "interviews?"),
    post_date="2025-01-09",
    poster_context="r/csMajors OP u/risioso, asking about the Five Rings QT Connect programme; says they 'can't find anything about it online'",
    doubt=("Reports what the recruiter told them to expect, before the interview happened, so it is "
           "an expectation rather than a recall; nobody in the thread ever answered with what "
           "actually got asked."))

# ============================================================ Hudson River Trading
add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    office="unknown", round="online_assessment", round_name="the algo dev oa",
    section_context="3.5/4 problems ... something like 910/1050 or 520/600",
    question_type="coding_algorithms",
    question_text=("for context i solved 3.5/4 problems on the algo dev oa so something like "
                   "910/1050 or 520/600. (for swe i didn't solve the second question so that's "
                   "cooked for sure"),
    source_url="https://www.reddit.com/r/csMajors/comments/1n2tr62/quick_questions_about_hrt_process/",
    source_quote=("for context i solved 3.5/4 problems on the algo dev oa so something like 910/1050 "
                  "or 520/600."),
    post_date="2025-08-29",
    poster_context=("r/csMajors OP u/444amnsc, who sat both the HRT Algo Dev and the HRT SWE OA; "
                    "reports back a week later 'damn, got 6/10 on one problem and aced the rest and "
                    "got rejected yesterday'"),
    doubt=("Attests the shape of HRT's Algo Dev OA — four problems, partial credit, a four-figure "
           "point total — and its severity, but reproduces no question. The two point totals quoted "
           "(910/1050 and 520/600) are the poster hedging about which scale they saw."))

add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    office="unknown", round="online_assessment", round_name="CodeSignal GCA",
    platform="CodeSignal", question_type="coding_algorithms",
    question_text=("Took CodeSignal GCA for the first time for internships in HRT, Roblox, Capital "
                   "One and got an 834 (couldn't pass one test case on the third question)."),
    source_url="https://www.reddit.com/r/csMajors/comments/wvbaiu/codesignal_scores_for_companies/",
    source_quote=("Took CodeSignal GCA for the first time for internships in HRT, Roblox, Capital "
                  "One and got an 834 (couldn't pass one test case on the third question)."),
    post_date="2022-08-22",
    poster_context="r/csMajors OP u/OofBoof112, asking whether an 834 GCA score is worth sending",
    doubt=("Attests only that HRT accepted a CodeSignal General Coding Assessment score for 2022 "
           "internships — a shared industry test rather than an HRT-authored paper, so the "
           "questions are not HRT's. Included for the platform fact, not for content."))

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
