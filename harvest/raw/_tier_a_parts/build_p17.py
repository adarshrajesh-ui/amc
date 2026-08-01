#!/usr/bin/env python3
"""p17: teamblind, read through the page's JSON-LD comment tree.

Blind renders only the opening post into HTML, so the earlier Blind pass could
only quote opening posts. The replies ship inside the schema.org
DiscussionForumPosting block on the same page, which curl already had — the
comments were simply invisible to a tag-stripping reader. blind_comments.py
parses that block, which is where the material below comes from.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p17_blind_jsonld.jsonl")
rows = []

URL = "https://www.teamblind.com/post/tc-interviews-advice-de-shaw-jane-street-hrt-citadel-hkuvevyq"
POSTER = ("Blind OP posting under the Uber company tag as 'ellllllll', ~3 years experience, "
          "interviewing for non-quant SWE roles in NYC across D.E. Shaw, Jane Street, HRT, "
          "Citadel, Facebook, Amazon and Goldman; reports back on 2020-06-17 that they were "
          "'rejected by JS and DESco' and had a second HRT phone screen scheduled")
DOUBT = ("Blind handles are company-verified only, so the poster's employer is attested but their "
         "candidacy is not; the comment lumps several firms together into one 'overall mix' rather "
         "than reporting each firm separately, so the attribution to any single firm is the "
         "poster's generalisation. ")

add_common = dict(
    role_track="quant_developer", level="experienced", cycle="unknown", office="New York",
    round="phone_technical", round_name="the phone screens", platform="unknown",
    section_context="All non-quant SWE; all in NYC", source_url=URL, source_type="blind",
    source_language="en", post_date="2020-06-17", access="full_text",
    retrieval_method="webfetch", poster_context=POSTER,
)

QUOTE = ("Tbh I only had a vague idea of what to expect. At least the phone screens were not LC, "
         "and certainly no systems design yet (though likely for onsite). Each firm was unique, "
         "but the overall mix was: problem solving, simple probability, OS/programming language "
         "trivia. HRT is the only one so far with C++-specific interviewing.")


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
    assert len(rec["source_quote"]) >= 20
    rows.append(rec)


add(firm="D. E. Shaw", question_type="probability",
    question_text=("the overall mix was: problem solving, simple probability, OS/programming "
                   "language trivia"),
    source_quote=QUOTE,
    doubt=(DOUBT + "The poster also says they were 'woefully unprepared for DES', so their read on "
           "what D. E. Shaw actually asked is coloured by having done badly."),
    **add_common)

add(firm="Hudson River Trading", question_type="coding_algorithms",
    question_text="HRT is the only one so far with C++-specific interviewing.",
    source_quote=QUOTE,
    doubt=(DOUBT + "For HRT specifically this is a single clause contrasting it with the other "
           "firms, not a description of any question."),
    **add_common)

add(firm="Hudson River Trading", question_type="other",
    question_text=("At least the phone screens were not LC, and certainly no systems design yet "
                   "(though likely for onsite)."),
    source_quote=QUOTE,
    doubt=(DOUBT + "Negative evidence — what the screen was not — which is weaker than a recall of "
           "what it was, and the poster hedges the onsite with 'though likely'."),
    **add_common)

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
