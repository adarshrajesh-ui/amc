#!/usr/bin/env python3
"""p24: four Blind threads the earlier board sweep missed, plus HRT's own process page,
one nowcoder post and two 1point3acres replies.

The Blind sweep walked the company interview boards; these four surfaced only from a
site:teamblind.com search and were not in the cache. Three carry replies with real
content; the Five Rings one (ss2aHcfs) has no answers and is recorded in the log as a
dry hole rather than mined.

The HRT careers-blog entry is the firm describing its own SWE/Algo-Engineering loop.
It is not a candidate recall and carries no question, but it is primary-source and
pins down round structure that candidate accounts only sketch, so it goes in with
role/level left honest rather than guessed.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p24_blind_misc.jsonl")
rows = []


def add(**kw):
    rec = {"firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
           "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
           "section_context": None, "question_type": "other", "question_text": None,
           "question_text_en": None, "reported_answer": None, "source_url": None,
           "source_type": "blind", "source_quote": None, "source_language": "en",
           "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
           "poster_context": None, "doubt": None}
    rec.update(kw)
    rows.append(rec)


# --------------------------------------------------- Blind: HRT NG algo dev, Feb 2025
U = "https://www.teamblind.com/post/hrt-ng-algo-developer-interview-process-x0b1ybun"
OP = ("Blind thread opened by 'coolerdan' posting under an ex-Lennox International tag: "
      "'I was reached out by recruiter, I cleared OA will be having screening soon, any idea "
      "what to expect?'; the OA description below is the OP answering a follow-up question "
      "in their own thread on 2025-02-04")
BD = ("Blind verifies only the poster's employer, not their candidacy, and the OP posts under "
      "an ex-employer tag; ")
add(firm="Hudson River Trading", role_track="quant_developer", level="new_grad",
    round="online_assessment", round_name="OA", source_url=U, post_date="2025-02-04",
    question_type="coding_algorithms",
    question_text="HRT new-grad Algo Developer OA: 3 questions, the third split into two parts "
                  "where part 2 builds on part 1",
    section_context="3 questions; question 3 has a part 1 and a part 2",
    source_quote="For OA: 3 questions, 1st one was relatively easy 2nd one: was hard 3rd one "
                 "part 1 was doable Part 2 was doable but couldn\u2019t able to solve it Rest "
                 "I\u2019ve solved with full score.",
    poster_context=OP,
    doubt=BD + "the OP describes difficulty and their own score but never states what any of the "
               "three questions actually asked, so this pins the OA's shape and nothing more.")
add(firm="Hudson River Trading", role_track="quant_developer", level="new_grad",
    round="phone_technical", round_name="screening", source_url=U, post_date="2025-02-04",
    question_type="logic_brainteaser",
    question_text="HRT screening round is either coding - where they describe a complicated "
                  "system or data structure, discuss implementing it, then have you implement "
                  "it - or a behavioral/experience interview with probability-style brainteasers",
    source_quote="If coding then they'll explain some complicated system / data structure that "
                 "you'll chat about implementing then you will implement it. If not coding, "
                 "then it will be a typical behavioral / experience interview with typical "
                 "probability esque brainteasers.",
    poster_context="Reply from a Blind user tagged Virtu Financial, dated 2025-02-04, answering "
                   "the OP's question about what to expect after clearing the OA",
    doubt=BD + "this is a Virtu employee telling the OP what to expect rather than someone "
               "reporting their own HRT screening, so it is second-hand and undated as to when "
               "they saw the process.")

# ------------------------------------ Blind: Old Mission / Jump SWE loop, Sep 2022
U = "https://www.teamblind.com/post/old-mission-capital-jump-trading-xnpmnp28"
OP = ("Blind thread opened by 'yatta' under a Bloomberg tag asking 'what kind of questions does "
      "Old Mission capital and Jump Trading asks for SWE interview? Do they do leetcode style "
      "DSA questions or mostly language specific, low level, OS , thread type questions?'; the "
      "reply below is from a Blind user tagged Meta, 2022-09-30")
BD = ("Blind verifies the replier's own employer (Meta) but not that they interviewed at either "
      "firm; ")
for firm in ("Old Mission Capital", "Jump Trading"):
    add(firm=firm, role_track="quant_developer", level="unknown", round="onsite",
        round_name="5 interview in a row, each one is 1 hour length", source_url=U,
        post_date="2022-09-30", question_type="coding_algorithms",
        section_context="5 back-to-back 1-hour interviews",
        question_text="implement deque which invalidates iterators, implement lazy leaky "
                      "singletone, implement allocator, tell me about virtual memory, codeforces "
                      "div2 D questions, sfinae simple stuff",
        source_quote="I had 5 interview in a row, each one is 1 hour length. They do ask low "
                     "level stuff, OS, etc. For example, implement deque which invalidates "
                     "iterators, implement lazy leaky singletone, implement allocator, tell me "
                     "about virtual memory, codeforces div2 D questions, sfinae simple stuff. But "
                     "also they ask some simple questions, so you may be lucky",
        poster_context=OP,
        doubt=BD + "and critically the replier never says which of the two firms this was: "
                   "another commenter asks 'Was this jump or old mission ?' and gets no answer, "
                   "so the same recall is recorded against both firms and at most one is right.")

# ----------------------------------------- Blind: HRT C++ SWE first round, Oct 2023
U = "https://www.teamblind.com/post/hudson-river-trading-c-software-engineer-interview-dbyj50eq"
add(firm="Hudson River Trading", role_track="quant_developer", level="new_grad",
    round="phone_technical", round_name="first round after the OA", source_url=U,
    post_date="2023-10-25", question_type="coding_algorithms",
    question_text="A hard dynamic-programming problem, solution only - no code required",
    source_quote="I was asked dp hard problem. Just to give solution, no code required",
    poster_context="Reply from a Blind user tagged Meta to 'HungrySWE' (Tesla tag), who opened "
                   "the thread asking what to expect in the first round after the HRT OA for a "
                   "C++ Software Engineer role and noted they are interviewing as a newgrad",
    doubt="A single 12-word reply that does not state the problem, does not say when the "
          "replier interviewed, and does not confirm they were on the same C++ SWE track as the "
          "OP; another commenter asks 'Is it low level C++ role or Algo dev/eng?' and gets no "
          "answer.")

# ------------------------------- HRT's own description of the SWE/Algo Eng process
U = "https://www.hudsonrivertrading.com/hrtbeat/interview-at-hrt/"
FIRM_DOUBT = ("This is HRT's own recruiting-blog post, so it is the employer's account of its "
              "process rather than a candidate's: it is authoritative on structure but "
              "self-presenting, undated on the page, and describes the campus SWE and Algo "
              "Engineering roles only - it says nothing about the quant trading or research "
              "tracks, and no actual question appears anywhere in it.")
add(firm="Hudson River Trading", role_track="quant_developer", level="unknown",
    round="take_home", round_name="Take-Home Tests", source_url=U, source_type="blog",
    post_date="unknown", question_type="coding_algorithms",
    question_text="HRT campus SWE/Algo Engineering pipeline: a take-home test, roughly two phone "
                  "interviews, and a full day of back-to-back onsite interviews",
    section_context="take-home is timed with a deadline, run over HackerRank or Codility",
    platform="HackerRank",
    source_quote="At a high level, you can expect a take-home test, roughly two phone interviews, "
                 "and a full day of back-to-back \u201consite\u201d interviews (that can be "
                 "conducted virtually or onsite).",
    poster_context="Posted by Hudson River Trading on its own HRTBeat careers blog, covering the "
                   "campus interview process for its 'Software Engineering' and 'Algo "
                   "Engineering' roles",
    doubt=FIRM_DOUBT)
add(firm="Hudson River Trading", role_track="quant_developer", level="unknown",
    round="phone_technical", round_name="Technical Discussion", source_url=U, source_type="blog",
    post_date="unknown", question_type="other",
    question_text="45-minute technical discussion on one of: Knowledge of Systems / Data "
                  "Structure / Problem Solving; plus a programming round in C++ or Python "
                  "depending on the team",
    section_context="usually a 45-minute discussion",
    source_quote="Technical Discussion: These rounds are usually a 45-minute discussion around "
                 "one of the following topics: Knowledge of Systems / Data Structure / Problem "
                 "Solving.",
    poster_context="Hudson River Trading's own HRTBeat careers blog, section 'Phone Interviews'",
    doubt=FIRM_DOUBT)
add(firm="Hudson River Trading", role_track="quant_developer", level="unknown", round="onsite",
    round_name="Onsite Interviews", source_url=U, source_type="blog", post_date="unknown",
    question_type="other",
    question_text="Onsite is graded on programming skills, systems-level knowledge (memory, I/O, "
                  "process management) and problem-solving",
    source_quote="Systems-level knowledge: Here we\u2019re looking for candidates with "
                 "fundamental systems knowledge (memory, I/O, process management). Can you "
                 "understand what is happening under the hood?",
    poster_context="Hudson River Trading's own HRTBeat careers blog, section 'Onsite Interviews'",
    doubt=FIRM_DOUBT)

# ------------------------------------------------------------- nowcoder: Akuna OA
U = "https://www.nowcoder.com/feed/main/detail/1a1602a27b864be3a1a49807669fd7f1"
add(firm="Akuna Capital", role_track="data_scientist", level="unknown",
    round="online_assessment", round_name="\u7b14\u8bd5", source_url=U, source_type="nowcoder",
    post_date="unknown", question_type="logic_brainteaser", source_language="zh",
    question_text="\u8fd8\u4ee5\u4e3a\u662fleetcode\u90a3\u79cd\u7c7b\u578b \u53cd\u6b63\u6211"
                  "\u662f\u771f\u7684\u4e0d\u61c2 \u6837\u4f8b\u7b80\u5355\u6c42\u6700\u5c0f"
                  "\u516c\u500d\u6570\u8ba9\u6211\u4ee5\u4e3a\u6d4b\u8bd5\u4e5f\u662f\u8fd9"
                  "\u6837 \u4fe1\u5fc3\u6ee1\u6ee1\u70b9\u8fdb\u53bb\u2026\u2026 \u667a\u529b"
                  "\u9898+\u7f16\u7a0b\u9898\u7684\u8d76\u811a",
    question_text_en="I thought it would be the LeetCode type. The sample question was a simple "
                     "lowest-common-multiple one, which made me assume the test would be like "
                     "that too, so I went in full of confidence... it felt like brainteasers "
                     "plus coding questions.",
    source_quote="\u8fd8\u4ee5\u4e3a\u662fleetcode\u90a3\u79cd\u7c7b\u578b \u53cd\u6b63\u6211"
                 "\u662f\u771f\u7684\u4e0d\u61c2 \u6837\u4f8b\u7b80\u5355\u6c42\u6700\u5c0f"
                 "\u516c\u500d\u6570\u8ba9\u6211\u4ee5\u4e3a\u6d4b\u8bd5\u4e5f\u662f\u8fd9"
                 "\u6837 \u4fe1\u5fc3\u6ee1\u6ee1\u70b9\u8fdb\u53bb\u2026\u2026 \u667a\u529b"
                 "\u9898+\u7f16\u7a0b\u9898\u7684\u8d76\u811a",
    poster_context="Nowcoder user \u725b\u5ba2913648960, East China Normal University "
                   "(\u534e\u4e1c\u5e08\u8303\u5927\u5b66), self-identified data analyst; post "
                   "titled 'akuna\u7b14\u8bd5\u597d\u96be [exploding-head emoji] \u76f4\u63a5"
                   "\u653e\u5f03\u4e86' tagged #\u79cb\u62db# #\u7b14\u8bd5#",
    doubt="The poster gave up on the test, so this describes their impression of it rather than "
          "the questions: the only concrete item is the practice sample (lowest common multiple), "
          "not a real test question. Nowcoder does not surface a post date on the feed permalink.")

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("%d records -> %s" % (len(rows), OUT))
