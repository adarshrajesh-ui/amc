#!/usr/bin/env python3
"""Two image posts whose pictures were downloaded and transcribed.

r/quantfinance is currently flooded with "<Firm> Interview Question" image posts: 21 from
u/Local_Ad135, 14 from u/nickgotgameon and 5 from u/Due_Department_3090, all branded question
cards driving traffic to prep products (u/Local_Ad135's cards carry quantprof.org and the
@quant_prof YouTube handle; u/nickgotgameon's body text cites quantprep.io; u/MentalMathApe
cites tradermath.org). That whole cluster is vendor marketing and is rejected under the hard
exclusions. The two records below are the exceptions worth keeping, and both are flagged.

i.redd.it serves images to this machine without an account, so the pictures really were read.
The post metadata comes from the Arctic Shift mirror since reddit.com itself 403s here.
"""
import json
import sys

POSTS = json.load(open('raw/pages/arctic/posts.json', encoding='utf-8'))
R = []


def add(rid, firm, role, level, cycle, rnd, rname, section, qtype, qtext, quote, poster, doubt,
        img, answer=None, office='unknown', date='unknown'):
    o = POSTS[rid]
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': 'unknown', 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext,
        'reported_answer': answer,
        'source_url': 'https://www.reddit.com' + (o.get('permalink') or ''),
        'source_type': 'reddit_thread', 'source_quote': quote, 'source_language': 'en',
        'post_date': date, 'access': 'screenshot_only', 'retrieval_method': 'webfetch',
        'upstream_source': None, 'poster_context': poster, 'doubt': doubt, '_img': img})


add('17lm2gx', 'Optiver', 'quant_researcher', 'unknown', '2024', 'online_assessment',
    'Optiver Quantitative Research 2023/2024 assessment portal, Amsterdam',
    'the candidate\'s own assessment dashboard, showing the four tasks in the battery and how far '
    'through them they were',
    'assessment_format',
    ('Project: AMS - Quant Research 2023/2024 | Task / Status | Optiver - Quantitative Research Test '
     '- 2023… : Completed | Zap-N test : Completed | Start NumberLogic test : New | Start Beat The '
     'Odds test : Pending'),
    ('Project: AMS - Quant Research 2023/2024 | Task / Status | Optiver - Quantitative Research Test '
     '- 2023… : Completed | Zap-N test : Completed | Start NumberLogic test : New | Start Beat The '
     'Odds test : Pending'),
    ('u/phygrad in r/quant, posting the screenshot under the title "[Optiver OA] Does this mean I '
     'have passed the tests before?" — a candidate who does not understand their own portal, which '
     'is a good sign the screenshot is theirs. They posted it twice within two minutes (17lm143 and '
     '17lm2gx), consistent with a fumbled submission rather than a campaign. Post metadata read via '
     'the Arctic Shift mirror; the image itself downloaded from i.redd.it and transcribed here.'),
    ('SCREENSHOT — transcribed by eye from https://i.redd.it/rmnvtvqcvsxb1.png, stored at '
     'raw/pages/redditimg/17lm2gx.png. It cannot be byte-verified, and the first task name is '
     'truncated by the column width in the image itself ("Optiver - Quantitative Research Test - '
     '2023…"), so I have reproduced the ellipsis rather than guessing the rest. No question content '
     'whatsoever — this is the task list, not a test. What makes it worth keeping is that it is a '
     'picture of Optiver\'s own portal rather than anyone\'s recollection, and it independently '
     'corroborates three module names that appear in this corpus from three unrelated places: '
     '"Zap-N" (a reddit commenter on r/csMajors), and "NumberLogic" and "Beat The Odds" (both in an '
     'Optiver instruction table pasted to r/quantfinance and in a 1point3acres recall recovered from '
     'the Wayback Machine). "AMS" is presumably Amsterdam, but the image does not say so and I have '
     'not asserted it in the office field.'),
    'raw/pages/redditimg/17lm2gx.png', date='2023-11-01')

add('1v9w4ai', 'SIG', 'unknown', 'unknown', 'unknown', 'online_assessment',
    'a question filed under "Susquehanna" and "Online Assessment" on a third-party question bank',
    'the full problem statement and its accompanying diagram, as rendered by the question bank',
    'puzzle_balance_weights',
    ('A hanging weight system consists of several geometric shapes, each with a fixed but unknown '
     'weight. The system below is perfectly balanced, and the total weight of all shapes combined is '
     '96 pounds. Compute the weight of the green triangle in pounds.'),
    ('A hanging weight system consists of several geometric shapes, each with a fixed but unknown '
     'weight. The system below is perfectly balanced, and the total weight of all shapes combined is '
     '96 pounds. Compute the weight of the green triangle in pounds.'),
    ('u/Due_Department_3090 in r/quantfinance, title "Susquehanna Online Assessment Quant Question | '
     '“Easy”". The image is not a photograph of an assessment — it is a screenshot of a question-bank '
     'website\'s question page, complete with the site\'s own chrome: a breadcrumb reading "Maths · '
     'Susquehanna · Easy · Pro", an answer box placeholder "Answer (e.g. 6, 2/3, 0.75)", a Submit '
     'button, a "0/200" character counter, "Add working (optional)" and "Show hint (optional)". Post '
     'metadata read via the Arctic Shift mirror; the image downloaded from i.redd.it and transcribed.'),
    ('VENDOR REPRODUCTION, NOT THE ASSESSMENT. This is a screenshot of a paid question bank (note the '
     '"Pro" tier badge) that has tagged one of its own problems "Susquehanna", and the poster is one '
     'of three accounts running a high-volume "<Firm> Interview Question" image campaign in '
     'r/quantfinance — 5 posts from this account, 21 from u/Local_Ad135 whose cards are branded '
     'quantprof.org, 14 from u/nickgotgameon whose body text cites quantprep.io. On its own that '
     'would make this a straight reject under the prep-vendor exclusion, and the firm tag would be '
     'worth nothing: question banks attribute freely and unverifiably. It is kept for one specific '
     'reason. A separate record in this corpus, from a 1point3acres SIG QR OA recall forwarded to '
     'Telegram in August 2024, has a candidate writing 求绿色三角形的重量 ("find the weight of the '
     'green triangle") about a diagram-based balance puzzle in a SIG assessment. So a green-triangle '
     'hanging-weight problem in a SIG OA is attested independently of any vendor, and this image is '
     'the only place a full statement of such a problem could be read. Treat the wording and the '
     '96-pound total as the vendor\'s, not SIG\'s. The diagram — a mobile with orange and blue '
     'hexagons, pink pentagons, grey octagons, green triangles, a red circle and yellow stars hanging '
     'from a 96 lbs beam — is essential to solving it and is not reproducible as text. Transcribed by '
     'eye from https://i.redd.it/oy3wtqnz66gh1.jpeg, stored at raw/pages/redditimg/1v9w4ai.jpeg; not '
     'byte-verifiable.'),
    'raw/pages/redditimg/1v9w4ai.jpeg', date='2026-07-27')

out = []
for rec in R:
    img = rec.pop('_img')
    import os
    if not os.path.exists(img):
        print('  MISSING IMAGE', img, file=sys.stderr)
        continue
    out.append(rec)

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as fh:
    for rec in out:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
print(f'appended {len(out)} screenshot records')
