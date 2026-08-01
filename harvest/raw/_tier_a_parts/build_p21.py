#!/usr/bin/env python3
"""p21: teamblind threads read through the Next.js payload.

p17 and p18 read Blind's schema.org JSON-LD block. That block turns out to be an
incomplete mirror of the thread — replies written from a company page are missing from
it, which is how an Old Mission SWE OA recall sat unread in the cache through two
passes. blind_next.py parses the __NEXT_DATA__ payload instead, which carries every
comment plus the poster's own verified employer, and blind_scan2.py re-ran the whole
cache through it.

Blind answers plain curl with the full thread, so these are full_text / webfetch.
The company shown against each comment is Blind's verified employer badge for the
poster, which is worth stating: it is evidence about who is talking, not about whether
they interviewed where they claim.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p21_blind_next.jsonl")
rows = []

BADGE = ("Blind verifies a poster's employer, not their candidacy, so the badge below attests "
         "who they work for and nothing about whether they sat this interview. ")


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
    rows.append(rec)


# ---------------------------------------------------------------- Old Mission
U = "https://www.teamblind.com/post/Old-Mission-Capital---Quant-Trader-TCWLB-QwSx7h11"
OMC = ("Thread 'Old Mission Capital - Quant Trader TC/WLB?' opened 2022-10-14 by a poster asking "
       "how hard it is to move from SWE to trading at OMC")

add(firm="Old Mission Capital", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="the OA",
    section_context="multiple choice Qs and a medium-ish leetcode Q, under an hour",
    question_type="coding_algorithms",
    question_text=("Just did the OA with multiple choice Qs and a medium-ish leetcode Q in under "
                   "an hour."),
    source_url=U, post_date="2022-10-19",
    source_quote=("How's the interview process like for SWEs? Just did the OA with multiple choice "
                  "Qs and a medium-ish leetcode Q in under an hour."),
    poster_context=("Reply from a Stripe-badged poster on " + OMC + "; this is the comment the "
                    "JSON-LD parser dropped"),
    doubt=(BADGE + "Reports the OA's shape, not its content — no multiple-choice topic and no "
           "LeetCode problem is named. Its value is as independent corroboration of the "
           "1point3acres recall of an Old Mission SWE OA built from MCQs plus coding."))

add(firm="Old Mission Capital", role_track="quant_trader", level="unknown", cycle="unknown",
    office="unknown", round="math_sequences_test", round_name="a math assessment",
    section_context="math assessment, then a technical interview with a recruiter, then a Super day",
    question_type="other",
    question_text=("Trading has a math assessment, and then an interview (technical) with a "
                   "recruiter, and then a Super day of interviews. I think all aspects of the "
                   "process is primarily math, stats, and game theory focused."),
    source_url=U, post_date="2022-10-20",
    source_quote=("Trading has a math assessment, and then an interview (technical) with a "
                  "recruiter, and then a Super day of interviews. I think all aspects of the "
                  "process is primarily math, stats, and game theory focused."),
    poster_context=("Reply from a poster badged 'Financial Service Company' on " + OMC + ", who "
                    "answers throughout as an insider ('I've had a few friends with CS "
                    "backgrounds come in')"),
    doubt=(BADGE + "The poster hedges with 'I think', and speaks as someone near the firm rather "
           "than as a candidate who sat the process, so this is second-hand description of the "
           "funnel. No question is reproduced."))

add(firm="Old Mission Capital", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="onsite", round_name="final round onsite with 2/3 engineers",
    section_context="one phone round with an engineer, then a final round onsite",
    question_type="other",
    question_text=("I believe it's one phone round with an engineer and then a final round onsite "
                   "with 2/3 engineers."),
    source_url=U, post_date="2022-10-19",
    source_quote=("I believe it's one phone round with an engineer and then a final round onsite "
                  "with 2/3 engineers.  Seems like OMC process has been quite efficient this year."),
    poster_context=("Reply from a poster badged 'Financial Service Company' on " + OMC),
    doubt=(BADGE + "Prefixed 'I believe', so the poster is not certain even of the round count, "
           "and no question content is given. Kept because Old Mission is the thinnest firm in "
           "this shard and the SWE funnel is otherwise undocumented here."))


# ---------------------------------------------------------------- DRW
U = "https://www.teamblind.com/post/drw-interview-prep-jgqrcap4"
DRWP = ("Thread 'DRW interview prep' opened 2025-10-16 by a Goldman Sachs-badged poster with "
        "three DRW interviews already scheduled, asking what to expect")

add(firm="DRW", role_track="quant_developer", level="unknown", cycle="unknown", office="unknown",
    round="phone_technical", round_name="90mns coding session", platform="unknown",
    section_context="first of three scheduled interviews; run inside a remote VM over Amazon DCV",
    question_type="coding_algorithms",
    question_text=("1st one is 90mns coding session, I need to download Amazon dcv client to login "
                   "into some virtual machine before the interview."),
    source_url=U, post_date="2025-10-16",
    source_quote=("1st one is 90mns coding session, I need to download Amazon dcv client to login "
                  "into some virtual machine before the interview."),
    poster_context=DRWP,
    doubt=(BADGE + "Written before the interviews rather than after, so it attests what the "
           "recruiter scheduled, not what was asked. The Amazon DCV detail is corroborated "
           "independently in the DRW senior-SWE thread in this batch."))

add(firm="DRW", role_track="quant_developer", level="unknown", cycle="unknown", office="unknown",
    round="phone_technical", round_name="technical troubleshooting and system design",
    platform="unknown", section_context="second and third of three interviews, via a Codility link",
    question_type="other",
    question_text=("For 2nd and 3rd, I've got a codility link and recruiter said will focus on "
                   "technical troubleshooting and system design."),
    source_url=U, post_date="2025-10-16",
    source_quote=("For 2nd and 3rd, I've got a codility link and recruiter said will focus on "
                  "technical troubleshooting and system design."),
    poster_context=DRWP,
    doubt=(BADGE + "The poster is relaying the recruiter's description in advance, so this is "
           "hearsay about the format. Codility recurs across the DRW records in this set, which "
           "is at least consistent."))

add(firm="DRW", role_track="quant_developer", level="unknown", cycle="unknown", office="unknown",
    round="phone_technical", round_name="DRW SWE interview", platform="unknown",
    section_context=None, question_type="other",
    question_text="They asked me some weird math questions. Not leetcode",
    source_url=U, post_date="2025-10-16",
    source_quote="They asked me some weird math questions. Not leetcode",
    poster_context=("Reply from a Spotify-badged poster on " + DRWP + ", who confirms in a "
                    "follow-up that this was for a SWE position"),
    doubt=(BADGE + "A single line with no question in it — it establishes only that a DRW SWE "
           "loop can be maths-led rather than LeetCode-led. Under the 40-character target because "
           "that is the whole comment."))

U = "https://www.teamblind.com/post/drw-senior-software-engineer-interview-2fu5tboo"
add(firm="DRW", role_track="quant_developer", level="experienced", cycle="unknown",
    office="unknown", round="phone_technical", round_name="1st round interview",
    section_context="DRW blockchain team", question_type="coding_algorithms",
    question_text=("You will have to download Amazon DCV Viewer and remote into an EC2 instance. "
                   "You will have to complete a coding task in an ide of your choice with the "
                   "interviewer also logged in. Pretty standard stuff, not hardcore leetcode."),
    source_url=U, post_date="2025-02-05",
    source_quote=("You will have to download Amazon DCV Viewer and remote into an EC2 instance. "
                  "You will have to complete a coding task in an ide of your choice with the "
                  "interviewer also logged in. Pretty standard stuff, not hardcore leetcode."),
    poster_context=("Reply on 'DRW Senior Software Engineer Interview', a thread opened 2025-02-04 "
                    "by a FactTube-badged poster on TC 300k asking about the DRW blockchain team's "
                    "rounds"),
    doubt=(BADGE + "Describes the environment and difficulty but not the task. Note the same "
           "thread contains an obvious joke reply ('reverse a binary tree using only one finger "
           "on the keyboard') which is excluded; the tone of the thread is partly unserious."))

U = "https://www.teamblind.com/post/DRW-phone-interview-qPFU5TMW"
add(firm="DRW", role_track="quant_developer", level="new_grad", cycle="unknown", office="unknown",
    round="online_assessment", round_name="OA", platform="unknown",
    section_context="new grad SWE OA scoring", question_type="coding_algorithms",
    question_text="You get more points on OA if you write at least 1/3 questions in C++ iirc",
    source_url=U, post_date="2020-09-01",
    source_quote="You get more points on OA if you write at least 1/3 questions in C++ iirc",
    poster_context=("Reply on 'DRW phone interview', opened 2020-08-31 by a poster interviewing "
                    "for a DRW new grad SWE role and asking whether the interviews are "
                    "language-agnostic; a second reply adds 'Gotta know java or c++'"),
    doubt=(BADGE + "Hedged with 'iirc', and a language-weighted OA score is an unusual enough "
           "claim that it may be a misremembering of general advice to prefer C++. Recorded "
           "because it is a specific, falsifiable claim about how DRW marks its OA."))


# ---------------------------------------------------------------- Two Sigma
# Dropped from this batch: the 'Phone was LC med. Onsite was 2 LC med, 2 LC hard all in
# morning' comment on /post/two-sigma-interview-nocvbgm4. It is genuinely in the bytes the
# URL serves, but only inside the Next.js payload — it never reaches rendered HTML, so a
# verifier that strips <script> before matching would call it a fabrication. Not worth the
# ambiguity for a round-shape datapoint the mazcdp6r thread already supplies.
U = "https://www.teamblind.com/post/two-sigma-interview-advice-mazcdp6r"
add(firm="Two Sigma", role_track="quant_developer", level="experienced", cycle="unknown",
    office="unknown", round="onsite", round_name="Onsite",
    section_context="3 rounds: 1 LC hard, 1 LC hard, 2 LC medium + 1 LC Easy",
    question_type="coding_algorithms",
    question_text=("Onsite was 3 rounds: 1 LC hard, 1 LC hard, 2 LC medium + 1 LC Easy, if you "
                   "don't get all test cases for 1 problem you automatically get rejected"),
    source_url=U, post_date="2021-04-21",
    source_quote=("Onsite was 3 rounds: 1 LC hard, 1 LC hard, 2 LC medium + 1 LC Easy, if you "
                  "don't get all test cases for 1 problem you automatically get rejected"),
    poster_context=("Reply from an Intuit-badged poster on the 'Two Sigma interview advice' "
                    "thread; a separate reply on the same thread reports being asked 'standard "
                    "leetcode (pretty easy ones actually) plus one guy wanted me to do some "
                    "linear algebra derivations'"),
    doubt=(BADGE + "The automatic-rejection rule is the poster's inference about how they were "
           "graded, not something an interviewer told them; it cannot be checked."))

add(firm="Two Sigma", role_track="quant_developer", level="experienced", cycle="unknown",
    office="unknown", round="onsite", round_name="Onsite", question_type="linear_algebra",
    section_context="one interviewer within an otherwise LeetCode-style onsite",
    question_text=("I was asked standard leetcode (pretty easy ones actually) plus one guy wanted "
                   "me to do some linear algebra derivations."),
    source_url=U, post_date="2021-04-21",
    source_quote=("I was asked standard leetcode (pretty easy ones actually) plus one guy wanted "
                  "me to do some linear algebra derivations. I hadn't touched linalg in years and "
                  "didn't remember shit about doing matrix math, so I bombed that one, which I "
                  "assume is what sank me."),
    poster_context="Reply from an Apple-badged poster on the 'Two Sigma interview advice' thread",
    doubt=(BADGE + "Which derivations were asked is never said — the poster admits they could not "
           "do them, so they may not have understood the question well enough to report it."))


# ---------------------------------------------------------------- Five Rings
U = "https://www.teamblind.com/post/45-minute-quant-research-video-interview-five-rings-mowddgjw"
add(firm="Five Rings", role_track="quant_researcher", level="unknown", cycle="unknown",
    office="unknown", round="phone_technical",
    round_name="45 minute video interview at Five Rings for Quant Research",
    section_context="45 minutes", question_type="stochastic_calculus",
    question_text="Brownian motion, calculus, some number theory/combinatorics",
    source_url=U, post_date="2023-08-20",
    source_quote="Brownian motion, calculus, some number theory/combinatorics",
    poster_context=("Reply on a thread opened 2023-08-18 by a poster with an upcoming 45-minute "
                    "Five Rings Quant Research video interview who 'couldn't find much info about "
                    "this firm'"),
    doubt=(BADGE + "A bare topic list posted in answer to 'what should I expect', with no claim "
           "attached that the replier sat the interview — it may be advice rather than recall. "
           "Included because Five Rings QR rounds are barely documented anywhere and the topic "
           "set is narrower than generic quant advice would be."))

U = "https://www.teamblind.com/post/Five-Rings-New-Grad-SWE-Interview-Process-yDKtzVTA"
add(firm="Five Rings", role_track="quant_developer", level="new_grad", cycle="unknown",
    office="unknown", round="phone_technical", round_name="first technical round",
    question_type="coding_algorithms",
    question_text="Know about stacks, queues, dynamic growing arrays",
    source_url=U, post_date="2023-03-19",
    source_quote="Know about stacks, queues, dynamic growing arrays",
    poster_context=("Reply on 'Five Rings New Grad SWE Interview Process', opened 2023-03-19 by a "
                    "poster with a first technical round upcoming; another reply on the same "
                    "thread says 'There is almost no one here who will be able to give you useful "
                    "information. Five Rings is too small.'"),
    doubt=(BADGE + "Advice phrased as an imperative, not a recall — the replier never says they "
           "interviewed. The neighbouring comment complaining that nobody on Blind knows anything "
           "about Five Rings undercuts it further."))

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
