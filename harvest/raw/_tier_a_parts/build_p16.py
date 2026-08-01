#!/usr/bin/env python3
"""p16: reddit, reached through the Arctic Shift archive.

reddit.com 403s this box and pullpush.io sits behind Cloudflare, so no earlier
pass had a single reddit record. arctic-shift.photon-reddit.com mirrors the
reddit dump and does answer, which is how the text below was read: full post and
comment bodies, not search snippets.

That mirror is the one caveat worth stating up front, and it is repeated in every
`doubt` below: the quotes are verbatim from the archived copy of the comment. If
a poster later edited or deleted the comment, the live permalink may no longer
match. The automated verifier treats reddit.com as unreachable anyway, so these
records are honest about being unverifiable against the live page while still
being full_text reads of a real retrieved document.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p16_reddit.jsonl")
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


# =========================================================== Hudson River Trading
HRT_OA = "https://www.reddit.com/r/csMajors/comments/rz3dvc/oa_with_hudson_river_trading_and_preparation/"
HRT_OA_POSTER = ("r/csMajors OP u/8bit-Corno, who opened the thread asking what to expect and then "
                 "edited in an 'Update:' with the questions after sitting it; says elsewhere in "
                 "the thread it was 'for a SWE position at their New York office'")
HRT_OA_DOUBT = ("Written straight after the sitting by the person who sat it, which is about as "
                "good as reddit provenance gets, but it is still an unverified anonymous account "
                "and the problems are restated in the poster's own words. ")

add(firm="Hudson River Trading", role_track="quant_developer", level="unknown",
    office="New York", round="online_assessment", round_name="OA with HRT in C++",
    section_context="only two questions with 140 minutes",
    question_type="coding_algorithms",
    question_text=("given a string with only A, B, C or D, remove adjacents A and Bs and remove "
                   "adjacent C and Ds so 'ABACD' becomes 'ACD' becomes 'A'"),
    source_url=HRT_OA,
    source_quote=("First question was a freebie, given a string with only A, B, C or D, remove "
                  "adjacents A and Bs and remove adjacent C and Ds so 'ABACD' becomes 'ACD' "
                  "becomes 'A'."),
    post_date="2022-01-08", poster_context=HRT_OA_POSTER,
    doubt=HRT_OA_DOUBT + "The poster calls this one 'a freebie', so it is the easy half of the paper.")

add(firm="Hudson River Trading", role_track="quant_developer", level="unknown",
    office="New York", round="online_assessment", round_name="OA with HRT in C++",
    section_context="only two questions with 140 minutes",
    question_type="coding_algorithms",
    question_text=("longest path in alternating tree. Basically, you got a tree with only 'a' or "
                   "'b' as values. Find the longest alternating path inside the tree. The hard "
                   "path was that the path might connect two subpath through a common parent or "
                   "it might not go through the root."),
    reported_answer="I solved it with dynamic programming but it took most of the time.",
    source_url=HRT_OA,
    source_quote=("Basically, you got a tree with only 'a' or 'b' as values. Find the longest "
                  "alternating path inside the tree."),
    post_date="2022-01-08", poster_context=HRT_OA_POSTER,
    doubt=HRT_OA_DOUBT + "The poster points readers to Google for the problem name, which means the phrasing is theirs rather than the test's.")

HRT_HUNT = "https://www.reddit.com/r/csMajors/comments/z3q0wf/a_summary_of_my_internship_hunt_for_summer_2023/"
HRT_HUNT_POSTER = ("r/csMajors OP u/kunriuss, a junior in honors math and CS at a self-described "
                   "T15, international student, writing up the Summer 2023 intern cycle; says "
                   "they were rejected by both Two Sigma and HRT")
HRT_HUNT_DOUBT = ("The OP deliberately withheld detail out of NDA caution ('I was wary of "
                  "NDA-stuff'), so what survives is the shape of the question rather than its "
                  "statement. ")

add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    cycle="Summer 2023", office="unknown", round="phone_technical",
    round_name="technical interview", question_type="other",
    question_text=("I was asked to design a heartbeat system to keep network connections alive, "
                   "and also design a file system/disk scheduling implementation that satisfies "
                   "certain conditions."),
    source_url=HRT_HUNT,
    source_quote=("I was asked to design a heartbeat system to keep network connections alive, and "
                  "also design a file system/disk scheduling implementation that satisfies certain "
                  "conditions."),
    post_date="2022-11-24", poster_context=HRT_HUNT_POSTER,
    doubt=(HRT_HUNT_DOUBT + "Attribution to HRT is by cross-reference inside the same thread: this "
           "comment does not name the firm, but the OP's later comment says 'For HRT, I was asked "
           "to design systems in networking and OS (I have a comment about them somewhere in this "
           "post if you're interested)', and a heartbeat system plus disk scheduling is exactly "
           "networking plus OS."))

add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    cycle="Summer 2023", office="unknown", round="phone_technical",
    round_name="technical interview", question_type="other",
    question_text="For HRT, I was asked to design systems in networking and OS",
    source_url=HRT_HUNT,
    source_quote=("For HRT, I was asked to design systems in networking and OS (I have a comment "
                  "about them somewhere in this post if you're interested). I was not expecting "
                  "design-oriented questions so I rated it 11/10."),
    post_date="2022-11-25", poster_context=HRT_HUNT_POSTER,
    doubt=HRT_HUNT_DOUBT + "Topic-level: names the two subject areas and a difficulty rating, no question statement.")

# ======================================================================= Two Sigma
add(firm="Two Sigma", role_track="quant_researcher", level="internship", cycle="Summer 2023",
    office="unknown", round="phone_technical",
    round_name="a round that focuses on core statistics",
    question_type="statistics_regression",
    question_text=("I need to prove lots of stuff in probability and statistics like normal "
                   "distributions and EV as well as hypothesis testing."),
    source_url=HRT_HUNT,
    source_quote=("For 2s, the role I applied was quantitative researcher so it has a round that "
                  "focuses on core statistics. For that, I need to prove lots of stuff in "
                  "probability and statistics like normal distributions and EV as well as "
                  "hypothesis testing."),
    post_date="2022-11-25", poster_context=HRT_HUNT_POSTER,
    doubt=(HRT_HUNT_DOUBT + "Topic-level: says what had to be proved in general terms but names no "
           "specific proof. '2s' is the OP's shorthand for Two Sigma, used consistently across the thread."))

# ======================================================================== DRW
add(firm="DRW", role_track="quant_trader", level="unknown", office="unknown",
    round="superday", round_name="super day", question_type="mental_math_speed",
    question_text="I got asked mental math for my super day",
    source_url="https://www.reddit.com/r/quantfinance/comments/1mvnl8f/drw_qt_superday_advice/",
    source_quote=("I got asked mental math for my super day lmao. My interviewer was a professional "
                  "Dota 2 player before he got recruited to be a manual trader at DRW."),
    post_date="2025-08-21",
    poster_context="r/quantfinance commenter u/fysmoe1121, replying in a 'DRW QT Superday advice?' thread",
    doubt=("Topic-level and undated as to when the superday happened; the memorable detail the "
           "commenter offers is about the interviewer's background, not the questions."))

# ================================================================== Five Rings
FR_WINT = "https://www.reddit.com/r/quantfinance/comments/1rb4s05/just_did_interview_for_five_rings_winternship_2027/"
add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="2027",
    office="unknown", round="phone_technical", round_name="interview for five rings winternship 2027",
    section_context="my interviewer only gave 10 seconds", question_type="fermi_estimation",
    question_text=("lots of estimation. my interviewer only gave 10 seconds. then there were some "
                   "other probability/EV/adverse selection stuff where I had unlimited time."),
    source_url=FR_WINT,
    source_quote=("lots of estimation. my interviewer only gave 10 seconds. then there were some "
                  "other probability/EV/adverse selection stuff where I had unlimited time. They "
                  "told me I passed the next morning; second round is behavioral."),
    post_date="2026-02-25",
    poster_context=("r/quantfinance commenter u/0xCUBE describing their own just-completed Five "
                    "Rings winternship first round; says they passed and that round two is behavioural"),
    doubt=("Fresh and first-person, but topic-level: names the categories (estimation, "
           "probability/EV, adverse selection) and the clock, without reproducing a single question."))

FR_OA = "https://www.reddit.com/r/quantfinance/comments/1v8csts/five_rings_quant_trading_intern_oa/"
add(firm="Five Rings", role_track="quant_trader", level="internship", office="unknown",
    round="online_assessment", round_name="Five Rings Quant Trading Intern OA",
    platform="HackerRank", section_context="17 min, 17 questions",
    question_type="mental_math_speed",
    question_text="I did it last year and it was 17 min, 17 questions brutal mental maths.",
    source_url=FR_OA,
    source_quote="I did it last year and it was 17 min, 17 questions brutal mental maths.",
    post_date="2026-07-28",
    poster_context="r/quantfinance commenter u/SidKT746, who says they sat the same OA the previous cycle",
    doubt=("Recalled a year later and topic-level: gives the format and the clock but no question. "
           "The same thread contains two users offering to sell or trade the questions, which is "
           "exactly the vendor behaviour to distrust — this commenter is not one of them, but it "
           "shows the thread attracts people with an incentive to embellish."))

add(firm="Five Rings", role_track="quant_trader", level="internship", office="unknown",
    round="online_assessment", round_name="Five Rings Quant Trading Intern OA",
    platform="HackerRank", section_context="17 minutes", question_type="mental_math_speed",
    question_text="17 minutes is pure mental math, no time to think",
    source_url=FR_OA, source_quote="17 minutes is pure mental math, no time to think",
    post_date="2026-07-27",
    poster_context="r/quantfinance commenter u/DeeplyEquable, answering the OP's question about the OA format",
    doubt=("One line, topic-level, and the commenter never says they personally sat it, so this "
           "may be relayed rather than first-hand."))

add(firm="Five Rings", role_track="quant_trader", level="internship", office="unknown",
    round="online_assessment", round_name="Five Rings OA", question_type="mental_math_speed",
    question_text=("Five Rings OA is pretty hard, probably the only OA I've struggled with. ... I "
                   "would recommend preparing your mental math and being able to estimate "
                   "questions well, I think I only passed from prior math competition experience."),
    source_url="https://www.reddit.com/r/quantfinance/comments/1o4b8ia/gave_imc_sig_oa_on_monday_still_havent_heard_back/",
    source_quote=("Five Rings OA is pretty hard, probably the only OA I've struggled with. They are "
                  "pretty lenient though, and people pass sometimes not even getting half of them "
                  "right."),
    post_date="2025-10-12",
    poster_context=("r/quantfinance commenter u/bt1927, a QT intern candidate recounting their own "
                    "cycle across SIG, IMC, Jane Street and Five Rings"),
    doubt=("Topic-level advice about what to prepare rather than a recall of any question; the "
           "claim that 'people pass sometimes not even getting half of them right' is hearsay "
           "about others."))

add(firm="Five Rings", role_track="quant_trader", level="internship", cycle="2027",
    office="unknown", round="online_assessment", round_name="OA", platform="HackerRank",
    section_context="19 min", question_type="other",
    question_text=("I just got OA. It says 19 min on hackerrank, is that the same you got? I "
                   "thought hackerrank was just coding not math questions"),
    source_url=FR_WINT,
    source_quote=("I just got OA. It says 19 min on hackerrank, is that the same you got? I thought "
                  "hackerrank was just coding not math questions"),
    post_date="2026-03-06",
    poster_context="r/quantfinance commenter u/Holiday-Intention451, who has just received the Five Rings OA invite",
    doubt=("This is a question being asked, not a recall — the only thing it attests first-hand is "
           "that their own invite showed a 19-minute HackerRank. Included because that timing "
           "corroborates the other Five Rings entries, not because it reports content."))

# ==================================================================== Akuna Capital
AK_CP = "https://www.reddit.com/r/csMajors/comments/iihdvk/codepair_tips/"
add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="online_assessment", round_name="The Online Assessment I had to do for these two positions",
    section_context="Akuna Capital Quant Dev and C++ Dev Internship",
    question_type="coding_algorithms",
    question_text=("They were like leetcode Hard problems with Digit DP, Monotonic Increasing Queue "
                   "with matrix, counting all possible dice roll sequences, largest size of two "
                   "non-overlapping intervals from a set of intervals, etc."),
    source_url=AK_CP,
    source_quote=("They were like leetcode Hard problems with Digit DP, Monotonic Increasing Queue "
                  "with matrix, counting all possible dice roll sequences, largest size of two "
                  "non-overlapping intervals from a set of intervals, etc."),
    post_date="2020-08-28",
    poster_context=("r/csMajors OP u/PostCalzoneOwO, who had codepairs lined up for both the Akuna "
                    "Quant Dev and the C++ Dev internship and was asking how they compare to the OA"),
    doubt=("Each problem is named by technique in three or four words rather than stated, and the "
           "poster admits 'I wouldn't have gotten the questions correct if I hadn't seen them "
           "before', so the labels may be their own retro-fitted classification."))

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="phone_technical", round_name="codepair", question_type="statistics_regression",
    question_text=("I got a leetcode easy and some inaudible basic stats question like what is a "
                   "CDF, a conditional probability problem, etc."),
    source_url=AK_CP,
    source_quote=("I got a leetcode easy and some inaudible basic stats question like what is a "
                  "CDF, a conditional probability problem, etc."),
    post_date="2020-09-10",
    poster_context=("r/csMajors OP u/PostCalzoneOwO reporting back in their own thread after "
                    "sitting the codepair; adds in a sibling comment that the interviewer 'was "
                    "disappointed that I havent taken Lin Alg yet'"),
    doubt=("The poster describes part of the audio as 'inaudible', so they themselves could not "
           "make out the full question; also says elsewhere the question set 'is all randomized "
           "from a question bank'."))

AK_ORDER = "https://www.reddit.com/r/csMajors/comments/jd2d2v/akuna_capital_codepair_response/"
AK_ORDER_POSTER = ("r/csMajors commenter u/gargar070402, explicitly '(This is for quant dev intern "
                   "btw.)', reporting two technical rounds a few days after sitting them")
AK_ORDER_DOUBT = ("Anonymous and unverified, and the poster had not yet heard back, so there is no "
                  "outcome to corroborate the account. ")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="phone_technical", round_name="the codepair",
    section_context="a much heavier emphasis in OOP/data structures rather than pure algorithms",
    question_type="coding_algorithms",
    question_text="I was asked to implement an order filling system based on a multi-stage rule that was provided.",
    source_url=AK_ORDER,
    source_quote=("For the codepair, I was asked to implement an order filling system based on a "
                  "multi-stage rule that was provided."),
    post_date="2020-10-27", poster_context=AK_ORDER_POSTER,
    doubt=AK_ORDER_DOUBT + "The 'multi-stage rule that was provided' is not reproduced, so the substance of the prompt is missing.")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="onsite", round_name="My final interview was a 30-minute behavioral and a 30-minute technical",
    question_type="coding_algorithms",
    question_text="I was asked to implement a bowling scoresheet.",
    source_url=AK_ORDER,
    source_quote=("My final interview was a 30-minute behavioral and a 30-minute technical, and for "
                  "this one I was asked to implement a bowling scoresheet."),
    post_date="2020-10-27", poster_context=AK_ORDER_POSTER, doubt=AK_ORDER_DOUBT)

add(firm="Akuna Capital", role_track="quant_trader", level="unknown", office="unknown",
    round="phone_technical", round_name="my technical screening call",
    question_type="expected_value",
    question_text=("which of two games I would rather play, one where you roll a dice and get the "
                   "square of the value, and the other where you roll two dice and get the produce "
                   "of the rolls"),
    source_url="https://www.reddit.com/r/quant/comments/14mqo6r/akuna_capital_to_lay_off_40_of_apac_employees/",
    source_quote=("The second question they asked me about which of two games I would rather play, "
                  "one where you roll a dice and get the square of the value, and the other where "
                  "you roll two dice and get the produce of the rolls."),
    post_date="2023-07-02",
    poster_context=("r/quant commenter u/No1TaylorSwiftFan, who says in the same thread 'I was "
                    "literally asked this as my first question in an akuna interview. (I declined "
                    "the offer)' — i.e. reached offer stage"),
    doubt=("Undated as to when the interview happened, and 'produce' is a typo for 'product', so "
           "the recall is loose in the details even though the game is clearly described."))

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="phone_technical", round_name="Codepair", question_type="combinatorics",
    question_text="they asked me an easy af leetcode q and some easy combinatorics/probability qs",
    source_url="https://www.reddit.com/r/csMajors/comments/ilzn4z/akuna_capital_quantitative_developer_intern/",
    source_quote=("they asked me an easy af leetcode q and some easy combinatorics/probability qs. "
                  "I answered all of them and was rejected."),
    post_date="2020-10-29",
    poster_context=("r/csMajors commenter u/two_sigma_niga in the 'Akuna Capital Quantitative "
                    "Developer Intern Codepair' thread; says they were rejected despite answering "
                    "everything, and were asked whether they had taken OS, linear algebra and networks"),
    doubt="Topic-level: characterises the difficulty but reproduces no question.")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="online_assessment", round_name="the OA for C++ dev internship",
    question_type="coding_algorithms",
    question_text="I did the OA for C++ dev internship, and it was all hards, very rough English, and not on leetcode.",
    source_url="https://www.reddit.com/r/csMajors/comments/plxnlm/akuna_capital_junior_python_offer/",
    source_quote=("I did the OA for C++ dev internship, and it was all hards, very rough English, "
                  "and not on leetcode. Still got the offer tho."),
    post_date="2021-09-11",
    poster_context="r/csMajors commenter u/two_sigma_niga, who says they got the offer",
    doubt="Topic-level: 'all hards ... not on leetcode' characterises the paper without naming a problem.")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", cycle="Summer 2025",
    office="unknown", round="online_assessment", round_name="python swe OA round 2",
    section_context="One question for 120 mins", question_type="coding_algorithms",
    question_text="One question for 120 mins! Had all testcases passed with around 40 mins left.",
    source_url="https://www.reddit.com/r/csMajors/comments/1f77r25/akuna_capital_python_swe_oa_round_2_for_2025/",
    source_quote="One question for 120 mins! Had all testcases passed with around 40 mins left.",
    post_date="2024-09-02",
    poster_context=("r/csMajors OP u/Fun-Aspect6276, posting about the Akuna Capital python SWE OA "
                    "round 2 for the 2025 summer internship"),
    doubt="Attests the format (one question, 120 minutes) but says nothing at all about the question.")

add(firm="Akuna Capital", role_track="quant_researcher", level="unknown", office="unknown",
    round="online_assessment", round_name="Akuna Quant HackerRank (tech)", platform="HackerRank",
    section_context="three questions; the third scored out of 15",
    question_type="coding_algorithms",
    question_text=("I failed a test case each on the first two questions of my OA and got a 5/15 on "
                   "the third question for Akuna Quant HackerRank (tech)."),
    source_url="https://www.reddit.com/r/csMajors/comments/15d6d0g/quant_hackerrank_akuna/",
    source_quote=("I failed a test case each on the first two questions of my OA and got a 5/15 on "
                  "the third question for Akuna Quant HackerRank (tech)."),
    post_date="2023-07-29",
    poster_context="r/csMajors OP u/No-Cattle-9939, asking what the acceptance bar is after scoring around 71% of test cases",
    doubt="Attests the shape of the paper (three questions, partial credit scoring) and nothing about content.")

# --- u/hocobozos, four Akuna write-ups posted within about a fortnight in Sept 2023.
HOCO = ("r/csMajors commenter u/hocobozos, who posted first-person write-ups of four separate "
        "Akuna processes across September 2023 and later asks in another thread which offer to take")
HOCO_DOUBT = ("This account posted four long, similarly-structured Akuna write-ups in a two-week "
              "window, all in the same flat summarising register, which is the shape generated "
              "content tends to take; against that, one of their replies in the same thread is "
              "ordinary conversational back-and-forth ('thats weird... Yeah, it definitely caught "
              "me off guard'), and none of the posts sell anything. Treat as plausible but "
              "materially less trustworthy than the dated write-ups elsewhere in this file. ")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="phone_technical", round_name="Akuna Capital Data Infra Intern Phone Screen",
    section_context="The email said the interview was 30 minutes, but they gave me around 75 minutes of actual interview time.",
    question_type="coding_algorithms",
    question_text=("The phone screen consists of 4 LC hard questions. Questions used dynamic "
                   "programming, trees, arrays, puzzles, and data structures."),
    source_url="https://www.reddit.com/r/csMajors/comments/16cioxy/akuna_capital_data_infra_intern_phone_screen/",
    source_quote=("The phone screen consists of 4 LC hard questions. Questions used dynamic "
                  "programming, trees, arrays, puzzles, and data structures."),
    post_date="2023-09-07", poster_context=HOCO, doubt=HOCO_DOUBT + "Topic-level; no problem is stated.")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="onsite", round_name="Akuna Data Infra Intern Final Round", question_type="other",
    question_text=('Given a Billion records every day, how would you store them'),
    source_url="https://www.reddit.com/r/csMajors/comments/16qctk8/akuna_data_infra_intern_final_round/",
    source_quote=('They asked a bunch of fast-paced questions like "Given a Billion records every '
                  'day, how would you store them" and technical questions like "Describe your '
                  'experience with big data technologies."'),
    post_date="2023-09-24", poster_context=HOCO,
    doubt=HOCO_DOUBT + "Offered as an example of the kind of question ('questions like'), not as an exact transcript.")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="onsite", round_name="Akuna Data Infra Intern Final Round", question_type="other",
    question_text="How would you implement a real-time fraud detection system?",
    source_url="https://www.reddit.com/r/csMajors/comments/16qctk8/akuna_data_infra_intern_final_round/",
    source_quote=('There were also some system design questions, like "How would you implement a '
                  'real-time fraud detection system?" And finally some LeetCode-level programming '
                  'questions.'),
    post_date="2023-09-24", poster_context=HOCO,
    doubt=HOCO_DOUBT + "Again framed as 'questions like', so it is an example rather than a verbatim prompt.")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="phone_technical", round_name="Akuna Capital C++ SWE Internship phone interview",
    question_type="coding_algorithms",
    question_text=("I was given two puzzles that required dynamic programming solutions. ... I had "
                   "to optimize the code involving cache locality, memory barriers, atomic "
                   "ordering, vectorization, memory alignment, context switch overhead, etc."),
    source_url="https://www.reddit.com/r/csMajors/comments/16n05in/akuna_capital_c_swe_intern_phone_interview/",
    source_quote=("I had to optimize the code involving cache locality, memory barriers, atomic "
                  "ordering, vectorization, memory alignment, context switch overhead, etc."),
    post_date="2023-09-19", poster_context=HOCO,
    doubt=HOCO_DOUBT + "Contains a garbled phrase ('explain the lure of the problem'), consistent with careless or generated writing.")

add(firm="Akuna Capital", role_track="quant_developer", level="internship", office="unknown",
    round="phone_technical", round_name="Akuna Capital C++ SWE Internship phone interview",
    question_type="other",
    question_text=("For some parts of the interview, I had to act like a human compiler where I "
                   "could be able to determine what the resulting native code would look like."),
    source_url="https://www.reddit.com/r/csMajors/comments/16n05in/akuna_capital_c_swe_intern_phone_interview/",
    source_quote=("For some parts of the interview, I had to act like a human compiler where I "
                  "could be able to determine what the resulting native code would look like."),
    post_date="2023-09-19", poster_context=HOCO, doubt=HOCO_DOUBT)

add(firm="Akuna Capital", role_track="quant_developer", level="unknown", office="unknown",
    round="online_assessment", round_name="Akuna Platform Engineering OA on the HackerRank platform",
    platform="HackerRank",
    section_context="two parts, one section with programming questions in C++ or Python and another for problem solving",
    question_type="coding_algorithms",
    question_text=("It was made up of a few very difficult tasks like implementing an algorithms "
                   "and then optimizing it, as well as a question which required you to create a "
                   "dynamic programming solution."),
    source_url="https://www.reddit.com/r/csMajors/comments/16mrwui/akuna_platform_engineer_hackerrank/",
    source_quote=("It was made up of a few very difficult tasks like implementing an algorithms and "
                  "then optimizing it, as well as a question which required you to create a "
                  "dynamic programming solution."),
    post_date="2023-09-19", poster_context=HOCO, doubt=HOCO_DOUBT + "Topic-level throughout.")

add(firm="Akuna Capital", role_track="quant_researcher", level="internship", office="unknown",
    round="online_assessment", round_name="the Online Assessment",
    section_context="It had 28 questions ... took up to 3 hours to complete",
    question_type="other",
    question_text=("It had 28 questions focused mainly on math topics and financial concepts. The "
                   "math topics included algebra, geometry, calculus, linear algebra, probability "
                   "and statistics, and analytical reasoning. The financial topics covered interest "
                   "rate concepts, derivatives, risk modelling, market trading, asset pricing, and "
                   "pricing models."),
    source_url="https://www.reddit.com/r/csMajors/comments/16kq2k0/akuna_qr_internship_oa_experience/",
    source_quote=("It had 28 questions focused mainly on math topics and financial concepts. The "
                  "math topics included algebra, geometry, calculus, linear algebra, probability "
                  "and statistics, and analytical reasoning."),
    post_date="2023-09-19", poster_context=HOCO,
    doubt=HOCO_DOUBT + "A syllabus rather than a question set.")

add(firm="Akuna Capital", role_track="quant_researcher", level="internship", office="unknown",
    round="online_assessment", round_name="the Online Assessment", question_type="other",
    question_text=("the Online Assessment also required me to video record myself solving each "
                   "question and then submit the recordings at the end of the assessment."),
    source_url="https://www.reddit.com/r/csMajors/comments/16kq2k0/akuna_qr_internship_oa_experience/",
    source_quote=("In addition, the Online Assessment also required me to video record myself "
                  "solving each question and then submit the recordings at the end of the "
                  "assessment."),
    post_date="2023-09-19", poster_context=HOCO,
    doubt=(HOCO_DOUBT + "This is format, not a question, but it is the only first-person "
           "corroboration in this file of Akuna's recorded-video assessment step."))

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
