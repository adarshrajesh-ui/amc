#!/usr/bin/env python3
"""Records recovered from reddit through the Arctic Shift mirror.

reddit.com returns 403 to this machine, so nothing here was read on reddit itself — every byte
came from arctic-shift.photon-reddit.com, which keeps post and comment bodies including ones
reddit has since removed. The snapshot the quotes are checked against is
raw/pages/arctic/{posts,comments}.json.

r/quant automod-removes standalone assessment threads, which is why the surviving recall is
concentrated in r/quantfinance and r/csMajors and in megathread replies.
"""
import json
import sys

POSTS = json.load(open('raw/pages/arctic/posts.json', encoding='utf-8'))
CMTS = json.load(open('raw/pages/arctic/comments.json', encoding='utf-8'))

MIRROR = ('Read through the Arctic Shift reddit mirror (arctic-shift.photon-reddit.com), not on '
          'reddit.com, which returns 403 to this machine; the mirror preserves post and comment '
          'bodies verbatim')

R = []


def add(kind, rid, firm, role, level, cycle, rnd, rname, section, qtype, qtext, qtext_en,
        quote, poster, doubt, answer=None, office='unknown', lang='en', platform='unknown',
        date=None, access='archive_only'):
    obj = (POSTS if kind == 'post' else CMTS).get(rid)
    if obj is None:
        R.append(('MISSING', rid, qtype))
        return
    url = 'https://www.reddit.com' + (obj.get('permalink') or '')
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': platform, 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext_en,
        'reported_answer': answer, 'source_url': url, 'source_type': 'reddit_thread',
        'source_quote': quote, 'source_language': lang, 'post_date': date or 'unknown',
        'access': access, 'retrieval_method': 'webfetch', 'upstream_source': None,
        'poster_context': poster, 'doubt': doubt, '_k': kind, '_id': rid})


# ==================================================================== Optiver OA, the real intro
# u/jhwyz pasted the assessment platform's own instructions table, which names all five tests,
# what each measures and how long it runs.
OPT_OA = dict(kind='post', rid='1urevoj', firm='Optiver', role='quant_researcher',
              level='internship', cycle='2026', rnd='online_assessment',
              rname='Optiver Quantitative Researcher internship online assessment — a five-test '
                    'battery the candidate launches from one "Start assessments" button',
              date='2026-04-08',
              poster=('u/jhwyz in r/quantfinance, asking how to prepare. Rather than describing the '
                      'assessment they pasted the platform\'s own instruction table verbatim, '
                      'including the "When you are ready to take the assessments, just click on the '
                      '\'Start assessments\' button below" header and the markdown table pipes. '
                      + MIRROR))
OPT_D = ('This is the assessment\'s own instruction text, not a question — it tells you what each '
         'test measures and how long you get, but no individual prompt is reproduced. Its value is '
         'that it is a verbatim paste rather than a recollection: the markdown table syntax, the '
         'stray Wikipedia link and the inconsistent capitalisation ("Likelihood-list") are all '
         'artefacts of copying out of the real email or portal. The obvious way it could be wrong is '
         'if the poster fabricated the paste wholesale, but the specific, unglamorous test names are '
         'independently echoed by other posters in this corpus. Note it is the QR intern variant; '
         'Optiver runs different batteries for different tracks.')

add(**OPT_OA, section='test 1 of the five-test battery',
    qtype='assessment_format_probability',
    qtext=('**1.**\u00a0**Beat The Odds** This test will assess your ability to apply probability theory. '
           'You have a limited time per question; and 45 minutes to complete the assessment overall.'),
    qtext_en=None,
    quote=('**1.**\u00a0**Beat The Odds** This test will assess your ability to apply probability theory. '
           'You have a limited time per question; and 45 minutes to complete the assessment overall.'),
    doubt=OPT_D)

add(**OPT_OA, section='test 2 of the five-test battery',
    qtype='assessment_format_numerical',
    qtext='**2.**\u00a0**NumberLogic** You will have 25 minutes to complete a numerical reasoning test.',
    qtext_en=None,
    quote='**2.**\u00a0**NumberLogic** You will have 25 minutes to complete a numerical reasoning test.',
    doubt=OPT_D)

add(**OPT_OA, section='test 3 of the five-test battery',
    qtype='assessment_format_ranking',
    qtext=('**3.**\u00a0**Likelihood-list** This test will assess your ability to rank possible outcomes '
           'from most likely to least likely based the information provided.'),
    qtext_en=None,
    quote=('**3.**\u00a0**Likelihood-list** This test will assess your ability to rank possible outcomes '
           'from most likely to least likely based the information provided.'),
    doubt=OPT_D + ' The missing "on" in "based the information provided" is Optiver\'s own typo.')

add(**OPT_OA, section='test 4 of the five-test battery',
    qtype='assessment_format_estimation_intervals',
    qtext=('**4.**\u00a0**Intervals** This test will assess your ability to estimate numerical values and '
           'quantify your uncertainty by setting upper and lower bounds around your answers. The '
           'overall assessment will take about 15 minutes to complete.'),
    qtext_en=None,
    quote=('**4.**\u00a0**Intervals** This test will assess your ability to estimate numerical values and '
           'quantify your uncertainty by setting upper and lower bounds around your answers. The '
           'overall assessment will take about 15 minutes to complete.'),
    doubt=OPT_D)

add(**OPT_OA, section='test 5 of the five-test battery',
    qtype='assessment_format_orderbook_arbitrage',
    qtext=('**5.**\u00a0**Orderbooks** This test will assess your ability to find opportunities where '
           'buying and selling different combinations of items can result in a profit. The overall '
           'assessment will take about 15 minutes.'),
    qtext_en=None,
    quote=('**5.**\u00a0**Orderbooks** This test will assess your ability to find opportunities where '
           'buying and selling different combinations of items can result in a profit. The overall '
           'assessment will take about 15 minutes.'),
    doubt=OPT_D)

# ==================================================================== Optiver OA, sat and described
add('post', '1urtesj', 'Optiver', 'unknown', 'internship', '2026', 'online_assessment',
    'Optiver Future Focus online assessment, sat the same week',
    'the poster\'s section-by-section account of the test they had just taken',
    'assessment_format',
    ('The probability was actually ok but the number logic? Man it\'s much harder than I thought, '
     'towards the end got some random arr number mixed I\'m not doing this shi in a min? Skipped at '
     'least 5 questions'),
    None,
    ('The probability was actually ok but the number logic? Man it\'s much harder than I thought, '
     'towards the end got some random arr number mixed I\'m not doing this shi in a min? Skipped at '
     'least 5 questions'),
    ('u/HussarL in r/quantfinance. They describe accidentally submitting the application while '
     'half-asleep, getting the OA immediately, obtaining an extension and preparing for only two '
     'days. ' + MIRROR),
    ('Not a question — a candidate\'s reaction to a section. It corroborates the NumberLogic test '
     'named in the pasted Optiver instructions and adds a per-question time budget ("in a min"), but '
     'the description of the items themselves ("some random arr number mixed") is too garbled to '
     'reconstruct anything. Written in a venting register, so the difficulty claims are impressions '
     'rather than measurements.'),
    date='2026-04-09')

add('post', '1urtesj', 'Optiver', 'unknown', 'internship', '2026', 'online_assessment',
    'Optiver Future Focus online assessment, sat the same week',
    'the poster\'s remark about a section they expected but did not get',
    'assessment_format',
    'Bit disappointed no 80 in 8 I really like those kind questions',
    None,
    'Bit disappointed no 80 in 8 I really like those kind questions',
    ('u/HussarL in r/quantfinance, immediately after listing how they did on the probability, number '
     'logic, Intervals and Orderbook sections. ' + MIRROR),
    ('"80 in 8" is used with no explanation, on the assumption the reader knows it — the natural '
     'reading is Optiver\'s 80-questions-in-8-minutes arithmetic sprint, and I am recording that '
     'reading as an inference, not as something the poster stated. What is solidly attested is that a '
     'section by that name exists in Optiver\'s repertoire and was absent from this particular '
     'battery, which is itself a useful negative datapoint about the QR/Future Focus variant.'),
    date='2026-04-09')

# ==================================================================== Five Rings QT intern OA
add('post', '1v8csts', 'Five Rings', 'quant_trader', 'internship', '2027', 'online_assessment',
    'Five Rings Quant Trading Intern 2027 HackerRank OA',
    'the poster comparing the OA they were sent against the format they had read about',
    'assessment_format',
    ('The HackerRank is 17 min, which seems different from the format with 19 questions. Has anyone '
     'taken it? How many questions and how much time per question do we get?'),
    None,
    ('The HackerRank is 17 min, which seems different from the format with 19 questions. Has anyone '
     'taken it? How many questions and how much time per question do we get?'),
    ('u/Upstairs-Schedule240 in r/quantfinance, holding an invitation for the Five Rings QT Intern '
     '2027 OA. ' + MIRROR),
    ('The poster has the invitation in front of them, so the 17-minute limit is first-hand; the '
     '19-question figure they contrast it with is second-hand from what they had read. No question '
     'content at all. Note this dovetails with a separate 1point3acres-sourced record in this corpus '
     'where a Five Rings candidate refers to "the 19 one min questions" as having become the OA.'),
    date='2026-07-20')

add('comment', 'p0auxxj', 'Five Rings', 'quant_trader', 'internship', '2026', 'online_assessment',
    'Five Rings Quant Trading Intern OA, sat the previous cycle',
    'a reply from someone who had taken the same OA a year earlier',
    'assessment_format',
    'I did it last year and it was 17 min, 17 questions brutal mental maths.',
    None,
    'I did it last year and it was 17 min, 17 questions brutal mental maths.',
    ('u/SidKT746 replying in r/quantfinance to the Five Rings QT Intern OA thread, and asking to DM '
     'the OP about how they would approach the problems. ' + MIRROR),
    ('First-hand but a year stale by their own admission, and it contradicts the 19-question figure '
     'circulating in the same thread — 17 questions in 17 minutes versus 19 questions at a minute '
     'each. Both cannot describe the same sitting, which is a useful reminder that OA formats drift '
     'between cycles. No question content.'),
    date='2026-07-21')

add('comment', 'kvqwhc3', 'Five Rings', 'quant_trader', 'new_grad', '2024', 'online_assessment',
    'Five Rings new-grad trader assessment',
    'a commenter listing the mental-arithmetic techniques the test rewards',
    'assessment_format_mental_math',
    'Lot of mental math tricks (geometry approximation, log approximation, power of 2).',
    None,
    'Lot of mental math tricks (geometry approximation, log approximation, power of 2).',
    ('u/IntegralSolver69 replying in r/quant to a candidate who had just passed Five Rings CV screen. '
     'They add "Idk what they\'re testing with this except if you have contacts who already '
     'interviewed". ' + MIRROR),
    ('A list of three technique categories, not questions — but unusually specific ones (geometry '
     'approximation, log approximation, powers of 2) that a person guessing would be unlikely to '
     'produce in that combination. The commenter does not say they sat the test themselves, so '
     'first-hand status is unestablished.'),
    date='2024-03-20')

# ==================================================================== the shrinkage question
add('post', '1ut6ytx', 'Citadel', 'quant_researcher', 'unknown', '2025', 'unknown',
    'a question the poster says came up at Citadel Securities, Two Sigma, Tower Research and '
    'Arrowstreet over the previous year',
    'the question as the poster states it, before the spoiler-tagged answer',
    'statistics_shrinkage_regression_to_mean',
    ('You observe a value X from a noisy dataset. You know the noise has mean zero. What is your best '
     'estimate of the actual underlying value?'),
    None,
    ('You observe a value X from a noisy dataset. You know the noise has mean zero. What is your best '
     'estimate of the actual underlying value?'),
    ('u/Zealousideal-Fig9666 in r/quantfinance, in a post titled "A simple interview question that '
     'trips up candidates at citsec, two sigma, tower, and arrowstreet last year". They give the '
     'answer behind a reddit spoiler tag and then derive beta = Cov(V, X) / Var(X) = Var(V) / '
     '(Var(V) + Var(noise)). ' + MIRROR),
    ('The strongest reason to distrust this is register: the post is written as teaching content — '
     'hook, spoiler tag, worked derivation, closing tie-in to why regularisation works — which is the '
     'house style of engagement-farmed quant posts, and it sat at score 0. The poster never says they '
     'personally sat any of the four interviews, and attributing one question to four firms at once '
     'is exactly the kind of claim nobody can check. Against that: a separate commenter in the thread '
     '(u/rsha256) writes "I interviewed and got offers at multiple of the firms mentioned and while I '
     'was asked similar questions, I merely said X and not beta * X", which is independent first-hand '
     'corroboration that the question is really asked, from someone who disputes the grading rather '
     'than the premise. Firm field set to Citadel because it is named first; the post attributes it '
     'equally to Two Sigma, Tower Research and Arrowstreet, so treat the firm as unresolved.'),
    answer=('The poster\'s answer: not X, but beta times X, shrunk toward the mean, with '
            'beta = Cov(V, X) / Var(X) = Var(V) / (Var(V) + Var(noise)); e.g. with equal signal and '
            'noise variance and X = 10 the estimate is 5'),
    date='2026-01-13')

add('comment', 'owtn07s', 'Citadel', 'quant_researcher', 'unknown', '2025', 'unknown',
    'the same shrinkage question, as corroborated by a candidate who was asked it',
    'a reply from someone who says they were asked similar questions and took the other side',
    'solution_discussion_only',
    ('Yep I interviewed and got offers at multiple of the firms mentioned and while I was asked '
     'similar questions, I merely said X and not beta \\* X (and one of them even said “correct”) and '
     'then I always just mansplained the Russian tank problem'),
    None,
    ('Yep I interviewed and got offers at multiple of the firms mentioned and while I was asked '
     'similar questions, I merely said X and not beta \\* X (and one of them even said “correct”) and '
     'then I always just mansplained the Russian tank problem'),
    ('u/rsha256 replying in r/quantfinance to the shrinkage post above. ' + MIRROR),
    ('Not a question statement — it is corroboration plus a dissent, logged because it is the only '
     'first-hand voice on that thread. The commenter is deliberately vague about which firms ("multiple '
     'of the firms mentioned") and says "similar questions" rather than this one, so it does not pin '
     'the prompt down. Their claim that an interviewer accepted the un-shrunk answer directly '
     'contradicts the OP\'s framing, which is worth carrying forward: at least one of the two accounts '
     'is wrong about how the question is graded.'),
    date='2026-01-13')

# ==================================================================== HRT systems engineer
add('post', '1uaog6u', 'HRT', 'quant_developer', 'experienced', '2026', 'phone_technical',
    'HRT Systems Engineer — the poster describes round 1 (passed) and what they were told about round 2',
    'the two rounds as described by the candidate in the middle of the process',
    'assessment_format',
    ('I passed the initial phone screen where they asked deep linux questions. Now I have a second '
     'round which is coding in python and told they’ll focus on Data manipulation, dictionary and '
     'sets, etc.'),
    None,
    ('I passed the initial phone screen where they asked deep linux questions. Now I have a second '
     'round which is coding in python and told they’ll focus on Data manipulation, dictionary and '
     'sets, etc.'),
    ('u/Creative-Complex-813 in r/csMajors, a systems engineer with a Linux/DevOps background who says '
     'they are panicking about the second round. ' + MIRROR),
    ('Half of this is first-hand ("they asked deep linux questions" — a round they sat) and half is '
     'the recruiter\'s advance description of a round they had not yet sat, which recruiters routinely '
     'get wrong. No individual question is given: "deep linux questions" is a characterisation, not a '
     'prompt.'),
    date='2026-06-20')

add('comment', 'osqr5e4', 'HRT', 'quant_developer', 'experienced', '2026', 'phone_technical',
    'HRT Systems Engineer coding round',
    'a reply describing how the round escalates',
    'assessment_format',
    ('They ask you basically leetcode medium question and if you successfully solve this, then step by '
     'step they try to make hard.. like ask you for manipulate test case, logic, space complexity...'),
    None,
    ('They ask you basically leetcode medium question and if you successfully solve this, then step by '
     'step they try to make hard.. like ask you for manipulate test case, logic, space complexity...'),
    ('u/ArgumentLow4169 replying in r/csMajors to the HRT Systems Engineer thread. ' + MIRROR),
    ('Describes the shape of the round (a LeetCode-medium seed problem that the interviewer escalates '
     'with follow-ups on test cases, logic and space complexity) without naming a single problem. The '
     'commenter gives no evidence of having sat it and the English is loose enough that they may be '
     'relaying second-hand.'),
    date='2026-06-20')

add('comment', 'irh0g7x', 'HRT', 'quant_developer', 'experienced', '2023', 'onsite',
    'HRT Core Dev onsite',
    'a reply breaking the onsite into its component round types',
    'assessment_format',
    ('* Given a description of some complicated data structure / algorithm, implement it in C++.\n'
     '* Bunch of lower-level question similar to the first phone screen, except you might be asked to '
     'sketch out code.\n* "Design a system that does X" style questions where you have to weigh '
     'tradeoffs, estimate performance, think about bottlenecks, etc.'),
    None,
    ('* Given a description of some complicated data structure / algorithm, implement it in C++.\n'
     '* Bunch of lower-level question similar to the first phone screen, except you might be asked to '
     'sketch out code.\n* "Design a system that does X" style questions where you have to weigh '
     'tradeoffs, estimate performance, think about bottlenecks, etc.'),
    ('u/isac_3236 replying in r/csMajors to a candidate who had found phone-screen reports but nothing '
     'about the HRT Core Dev onsite. They open "The onsite is split into a bunch of separate rounds, '
     'but roughly:" and sign off "Good luck!". ' + MIRROR),
    ('Three round archetypes, none of them an actual question — "some complicated data structure" and '
     '"Design a system that does X" are placeholders the commenter uses deliberately. Reads first-hand '
     'from the level of detail but they never say so. This is the most substantive answer in a thread '
     'whose OP complained they could find nothing about this round anywhere.'),
    date='2022-10-08')

# ==================================================================== Citadel Securities Sydney
add('comment', 'oio5sip', 'Citadel', 'quant_trader', 'internship', '2026', 'superday',
    'Citadel Securities Sydney/Australia quant trading internship interview loop',
    'a first-hand walk-through of the loop, answering the OP\'s checklist of topic guesses',
    'assessment_format',
    ('there’s 1 coding round (third round) which is mostly pandas work and a coding-type brain teaser. '
     'the rest is a combination of fermi problems, market making, some probability/expectation stuff, '
     'and then some behaviourals in most interviews (all with actual traders though, no full hr round). '
     'I wasn’t asked any mental maths'),
    None,
    ('there’s 1 coding round (third round) which is mostly pandas work and a coding-type brain teaser. '
     'the rest is a combination of fermi problems, market making, some probability/expectation stuff, '
     'and then some behaviourals in most interviews (all with actual traders though, no full hr round). '
     'I wasn’t asked any mental maths'),
    ('u/SharpPomegranate2868 in r/quantfinance, replying in a thread asking specifically about the '
     'Sydney process. They open by calling another reply in the thread a bot, then give this account; '
     'they also note "I wasn\'t ever asked any options stuff". ' + MIRROR),
    ('No question is reproduced — this is a round-by-round topic map. It is worth keeping because the '
     'negative claims are specific and falsifiable (no mental maths, no options, no full HR round, '
     'traders conduct every interview), and because it is one of very few accounts of the Sydney desk '
     'specifically rather than the US process. The commenter says "I wasn\'t asked", implying they sat '
     'it, but never states which cycle.'),
    office='Sydney', date='2026-04-28')

add('comment', 'ohsa6tm', 'Citadel', 'quant_trader', 'internship', '2026', 'superday',
    'Citadel Securities Sydney/Australia quant trading internship interview loop',
    'a shorter reply in the same thread, comparing it to Optiver',
    'assessment_format',
    ('pretty similar to optiver tbh tons of mental math fast probability brainteasers basic mm theory '
     'one tiny options bit behavioral was shallow'),
    None,
    ('pretty similar to optiver tbh tons of mental math fast probability brainteasers basic mm theory '
     'one tiny options bit behavioral was shallow'),
    ('u/chocolate_asshole in r/quantfinance, in the same Citadel Securities Sydney thread. ' + MIRROR),
    ('Directly contradicts the other first-hand reply in the same thread, which says there was no '
     'mental maths and no options content, where this one reports "tons of mental math" and "one tiny '
     'options bit". Both are logged precisely because they disagree; at most one can describe the loop '
     'accurately, and a downstream reader should not treat either as settled. Unpunctuated and '
     'offhand, with no claim of having sat it.'),
    office='Sydney', date='2026-04-21')

# ==================================================================== Optiver module names, csMajors
add('comment', 'ngor45u', 'Optiver', 'quant_developer', 'new_grad', '2026', 'online_assessment',
    'Optiver Amsterdam SWE 2026 new-grad OA',
    'a commenter naming the three tests they had just been sent',
    'assessment_format',
    'Also did you prep for the OAs I just got mine. Number Logic, Zap-N and beat the odds',
    None,
    'Also did you prep for the OAs I just got mine. Number Logic, Zap-N and beat the odds',
    ('u/Next-Temporary-7115 replying in r/csMajors to a candidate who had passed the Optiver OA and '
     'been invited to a behavioural round. ' + MIRROR),
    ('Three test names given in passing by someone who says they have just received the assessment, so '
     'first-hand and current, but with no description of any of them. Two of the three (Number Logic, '
     'Beat The Odds) match the names in Optiver\'s own pasted instruction table elsewhere in this '
     'corpus, which is good mutual corroboration; the third, "Zap-N", does not appear in that QR '
     'battery at all — consistent with Optiver running different module sets for SWE and QR, but not '
     'proof of it.'),
    office='Amsterdam', date='2025-09-28')

# ==================================================================== Optiver QR OA, vendor-adjacent
add('comment', 'owg2v7x', 'Optiver', 'quant_researcher', 'internship', '2026', 'online_assessment',
    'Optiver QR intern OA',
    'a reply characterising each named module of the battery',
    'assessment_format',
    ('The two that actually trip people up are NumberLogic and the timed probability one, and both '
     'come down to speed more than depth. It\'s arithmetic under a clock, so drill mental math '
     '(Zetamac is the standard one) until you\'re not thinking about the multiplication anymore, and '
     'the probability questions are mostly basic conditional/expected value stuff but you don\'t get '
     'time to rederive from scratch. Intervals is a calibration thing, don\'t set your bounds too '
     'tight trying to look confident, they\'re grading whether the true value lands inside.'),
    None,
    ('The two that actually trip people up are NumberLogic and the timed probability one, and both '
     'come down to speed more than depth. It\'s arithmetic under a clock, so drill mental math '
     '(Zetamac is the standard one) until you\'re not thinking about the multiplication anymore, and '
     'the probability questions are mostly basic conditional/expected value stuff but you don\'t get '
     'time to rederive from scratch. Intervals is a calibration thing, don\'t set your bounds too '
     'tight trying to look confident, they\'re grading whether the true value lands inside.'),
    ('u/QuantGrindApp replying in r/quantfinance to the Optiver QR intern OA thread. ' + MIRROR),
    ('VENDOR SOURCE — the account name is a product name and the comment ends by pitching that product '
     '("I run QuantGrind (full disclosure, it\'s mine)"), so this is marketing with useful content '
     'attached and must be discounted accordingly. Nothing here is a question; it is a module-by-module '
     'characterisation. The claim worth extracting is the grading rule asserted for Intervals — that '
     'you are scored on whether the true value falls inside your bounds rather than on tightness — '
     'which is a specific, checkable assertion that the official instruction text in this corpus does '
     'not state.'),
    date='2026-04-08')

# ==================================================================== Optiver institutional trader
add('comment', 'o3h2tgo', 'Optiver', 'quant_trader', 'internship', '2026', 'phone_technical',
    'Optiver Institutional Trader Intern technical interview',
    'a reply describing what the technical round centres on',
    'assessment_format',
    ('The technical interview is usually centered on probability,  logical thinking and fast mental '
     'math rather than anything you would learn in a finance class.'),
    None,
    ('The technical interview is usually centered on probability,  logical thinking and fast mental '
     'math rather than anything you would learn in a finance class.'),
    ('u/landau007 replying in r/quantfinance. They hedge the whole comment with "From what I have '
     'seen". ' + MIRROR),
    ('Explicitly second-hand — the commenter opens "From what I have seen", not "when I did it" — and '
     'the content is the generic probability/logic/mental-math triad that appears in every thread of '
     'this kind, so it carries almost no information. Logged under the do-not-over-filter rule with '
     'that reservation stated plainly. The double space after "probability," is in the original.'),
    date='2026-02-04')

# ------------------------------------------------------------------ emit with verification
fails = []
out = []
for rec in R:
    if isinstance(rec, tuple):
        fails.append(rec)
        continue
    k, rid = rec.pop('_k'), rec.pop('_id')
    obj = (POSTS if k == 'post' else CMTS)[rid]
    body = (obj.get('selftext') if k == 'post' else obj.get('body')) or ''
    if rec['source_quote'] not in body:
        fails.append((rid, rec['question_type'], rec['source_quote'][:60]))
        continue
    out.append(rec)

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as fh:
    for rec in out:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'appended {len(out)} records; {len(fails)} quote failures')
for f in fails:
    print('  FAIL', f, file=sys.stderr)
