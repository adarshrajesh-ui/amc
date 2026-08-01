#!/usr/bin/env python3
"""Two first-hand assessment-shape reports from reddit comments the Arctic Shift mirror holds.

These come out of a 260-thread comment sweep whose overwhelming majority was AI-generated
advice spam from accounts marketing interviews.chat, QuantGrind and Beyz; those were rejected
under the prep-vendor exclusion. The two below carry no vendor pitch and describe the shape of
a round rather than selling a product. Neither states a question, and both say so in `doubt`.
"""
import json
import sys

CMTS = json.load(open('raw/pages/arctic/comments.json', encoding='utf-8'))
R = []


def add(cid, firm, role, level, cycle, office, rnd, rname, section, qtype, qtext, quote,
        poster, doubt):
    c = CMTS[cid]
    body = c.get('body') or ''
    if quote not in body:
        print('QUOTE NOT FOUND in', cid, file=sys.stderr)
        sys.exit(1)
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': 'unknown', 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': None,
        'reported_answer': None,
        'source_url': 'https://www.reddit.com' + c['permalink'],
        'source_type': 'reddit_thread', 'source_quote': quote, 'source_language': 'en',
        'post_date': 'unknown', 'access': 'archive_only', 'retrieval_method': 'webfetch',
        'upstream_source': None, 'poster_context': poster, 'doubt': doubt})


MIRROR = ('reddit.com returns 403 to this machine, so this comment was read from the Arctic '
          'Shift mirror rather than from reddit itself.')
SLOP = ('The thread pool this came from is heavily contaminated: of 17 comments in a 260-thread '
        'sweep that matched on question-like phrasing, 15 were AI-written advice replies from '
        'accounts marketing interviews.chat, QuantGrind or Beyz. This one carries no product '
        'pitch, which is why it was kept, but the same generative pattern cannot be ruled out.')

add('ozifwmk', 'SIG', 'quant_trader', 'internship', '2027', 'unknown', 'online_assessment',
    'SIG Quant Trading summer intern OA', 'the content of the OA as a whole',
    'assessment_format',
    ('I went through the SIG process a couple years ago and the OA was basically a condensed '
     'version of their interview style. Think dice sums, coin flips with a twist, and some game '
     'theory scenarios where you\'re setting prices.'),
    ('I went through the SIG process a couple years ago and the OA was basically a condensed '
     'version of their interview style. Think dice sums, coin flips with a twist, and some game '
     'theory scenarios where you\'re setting prices.'),
    ('A reply on the r/quantfinance thread "SIG Quant Trading 2027 Summer Intern OA" from '
     'someone who says they sat the SIG process a couple of years earlier; the same comment '
     'states the OA runs 60 minutes and involves no Zetamac-style mental-math drilling.'),
    MIRROR + ' It is a characterisation of the question types, not a question: "dice sums", '
             '"coin flips with a twist" and price-setting game theory are categories, and no '
             'individual problem is stated. The commenter dates their own experience to "a '
             'couple years ago", so it does not describe the 2027-cycle OA the thread is about. '
             + SLOP)

add('nzhes41', 'HRT', 'quant_developer', 'unknown', 'unknown', 'London', 'phone_technical',
    'HRT London Algo Dev phone screen', 'the split of the 45-minute phone screen',
    'assessment_format',
    ('hrt london algo dev phone screens are typically 45min split between algorithms and '
     'probability/stats, sometimes a bit of systems design depending on the interviewer.'),
    ('hrt london algo dev phone screens are typically 45min split between algorithms and '
     'probability/stats, sometimes a bit of systems design depending on the interviewer.'),
    ('A reply on the r/quantfinance thread "HRT algo dev interviews" describing the London Algo '
     'Dev phone screen and the later rounds.'),
    MIRROR + ' The commenter never claims to have sat this interview themselves — the whole '
             'reply is written in the generalising register ("typically", "tend to", "usually") '
             'that the AI-written advice replies in this subreddit also use. It states round '
             'structure and topic areas only; not one question appears in it. ' + SLOP)

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('appended', len(R), 'records')
