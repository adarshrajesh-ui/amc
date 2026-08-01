#!/usr/bin/env python3
"""Fourth @usinterview batch — messages fetched earlier but never mined.

Every quote is checked against the stored copy of the message page before the record is
emitted; anything that does not match is dropped and reported.
"""
import html
import json
import os
import re
import sys

PAGES = 'raw/pages/tgmsg'
BLOCKS = re.compile(
    r'<div class="(?:tgme_widget_message_text[^"]*|link_preview_title|link_preview_description)"'
    r'[^>]*>(.*?)</div>', re.S)
_cache = {}


def page_text(mid):
    if mid not in _cache:
        raw = open(os.path.join(PAGES, f'{mid}.html'), encoding='utf-8', errors='replace').read()
        parts = []
        for b in BLOCKS.findall(raw):
            t = re.sub(r'<script.*?</script>', ' ', b, flags=re.S)
            t = re.sub(r'<br\s*/?>', '\n', t)
            t = re.sub(r'<[^>]+>', '\n', t)
            parts.append(html.unescape(t))
        _cache[mid] = '\n'.join(parts)
    return _cache[mid]


TG = ('@usinterview is a public Telegram channel that auto-forwards new 1point3acres 海外面经 '
      'threads. The message carries the thread title, the firm/round/seniority tags the poster '
      'chose on the forum, and the opening of the post body as a link preview')
TRUNC = ('Telegram link previews are cut off at a fixed length, and the preview visibly ends in '
         '"…" — so only the opening of the recall is readable here. 1point3acres itself '
         'Cloudflare-blocks this machine and the Wayback Machine has no 200 snapshot of this '
         'thread (checked against a CDX sweep of 153,275 archived 1point3acres thread URLs), so '
         'the remainder cannot be recovered')

R = []


def add(mid, date, firm, role, level, cycle, rnd, rname, section, qtype, qtext, qtext_en,
        quote, poster, doubt, answer=None, office='unknown', lang='zh'):
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': 'unknown', 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext_en,
        'reported_answer': answer, 'source_url': f'https://t.me/usinterview/{mid}',
        'source_type': 'chat_telegram', 'source_quote': quote, 'source_language': lang,
        'post_date': date, 'access': 'full_text', 'retrieval_method': 'webfetch',
        'upstream_source': ('1point3acres thread auto-forwarded into the channel; the forum thread '
                            'itself is not readable from this machine'),
        'poster_context': poster, 'doubt': doubt, '_mid': mid})


# ---------------------------------------------------------------- SIG, 17-question QR OA
SIG_1082364 = dict(
    mid='19242', date='2024-08-23', firm='SIG', role='quant_researcher', level='experienced',
    cycle='2024', rnd='online_assessment',
    rname='SIG QR 在线笔试 — the poster titles it "SIG QR 17题OA" (17-question OA)',
    poster=(TG + '. Forum tags: #sig 金工类@全职 在线笔试 在职跳槽 — quant track, full-time, online '
            'written test, experienced hire changing jobs. The poster opens "新题库…感觉还挺难的…" '
            '(new question bank… feels quite hard)'))

add(**SIG_1082364,
    section='listed among the questions the poster says are new relative to the forum question bank',
    qtype='puzzle_balance_weights',
    qtext='求绿色三角形的重量（6lb)',
    qtext_en='Find the weight of the green triangle (6 lb).',
    quote='还有两道新题是地里的，求绿色三角形的重量（6lb)',
    answer='6lb — but see doubt: it is not clear whether 6lb is the answer or a given',
    doubt=('One clause long, and the shape/colour vocabulary ("绿色三角形") is the signature of a '
           'diagram-based balance puzzle whose picture is not in the message at all, so the '
           'weighings that determine the triangle are entirely absent. I also cannot tell from the '
           'syntax whether "（6lb)" is the poster supplying the answer or restating a given in the '
           'figure; I have put it in reported_answer but flagged it here rather than assert it. '
           'The sentence is also internally confusing — 还有两道新题是地里的 says "two more new '
           'questions are [already] in the forum", which contradicts the surrounding claim that '
           'these are new. ' + TRUNC))

add(**SIG_1082364,
    section='listed among the questions the poster says are new relative to the forum question bank',
    qtype='probability_expected_value_dice',
    qtext='扔2次骰子获得最大收益',
    qtext_en='Roll a die twice, obtaining the maximum payoff.',
    quote='扔2次骰子获得最大收益',
    doubt=('Seven characters. This is a topic label, not a problem statement: it does not say what '
           'the payoff function is, whether the roller may stop after the first roll (the usual '
           'form of this family of questions, in which case the answer depends on an optimal '
           'stopping threshold), or what is being asked for. I will not supply the missing '
           'structure. Kept only because it is a genuine report of a question appearing on a dated '
           'SIG OA. ' + TRUNC))

add(**SIG_1082364,
    section='listed among the questions the poster says are new relative to the forum question bank',
    qtype='combinatorics_arrangements',
    qtext='还有2种饼干，A有6个，B有8个，7个排成一排有多少排列组合 2^7-1',
    qtext_en=('There are also 2 kinds of cookie, 6 of A and 8 of B; if 7 are arranged in a row, how '
              'many arrangements are there? 2^7-1'),
    quote='还有2种饼干，A有6个，B有8个，7个排成一排有多少排列组合 2^7-1',
    answer='2^7-1',
    doubt=('This is the most complete of the three, but the reported answer does not obviously '
           'follow from the statement as written: with 6 A-cookies and 8 B-cookies available, the '
           'number of distinguishable length-7 sequences is 2^7 minus the single all-A string that '
           'the supply of 6 makes impossible — which does give 2^7-1, but only under a reading of '
           '"排列组合" that the poster never states. Because I cannot separate the poster\'s answer '
           'from the poster\'s paraphrase of the question, treat 2^7-1 as reported, not verified. ' +
           TRUNC))

# ---------------------------------------------------------------- HRT C++ experienced OA
add('20778', '2024-12-20', 'HRT', 'quant_developer', 'experienced', '2024', 'online_assessment',
    'HRT 在线笔试 for an experienced C++ role — 70 minutes, 4 questions',
    'the poster describes the first two questions as easy and similar to ones already on the forum',
    'coding_filesystem_tree',
    '前两题比较简单，地里有类似的题目，创建目录和文件的那题',
    ('The first two questions were fairly easy, similar to ones already on the forum — the one '
     'about creating directories and files.'),
    '前两题比较简单，地里有类似的题目，创建目录和文件的那题',
    (TG + '. Forum tags: #Hudson River Trading 码农类General@全职 在线笔试 在职跳槽 — engineering '
     'track, full-time, online written test, experienced hire. The poster says the test was 70 '
     'minutes for 4 questions, that they spent too long on boundary conditions in q3 and timed '
     'out, and so never finished q4'),
    ('This is a back-reference ("the one about creating directories and files"), not a problem '
     'statement — the poster is pointing at a question they assume the reader already knows from '
     'the forum, so the interface, the operations to support and the expected complexity are all '
     'missing. The preview cuts off at exactly "q3: ", which is where the poster was about to '
     'give the one question they described in detail. ' + TRUNC),
    lang='mixed')

# ---------------------------------------------------------------- Akuna Shanghai QR OA
add('21929', '2025-03-18', 'Akuna', 'quant_researcher', 'experienced', '2025',
    'online_assessment',
    'Akuna Capital Shanghai 在线笔试 — Python-only, 3 questions, 2 hours',
    'the first of the three coding questions',
    'coding_profit_cost_optimisation',
    '给两个list，分别为profit和cost，收益',
    'Given two lists, one of profits and one of costs, the return …',
    '给两个list，分别为profit和cost，收益',
    (TG + '. Forum tags: #akunacapital 金工类@全职 在线笔试 在职跳槽. The poster says they wanted to '
     'return to China (有心回国), applied to the Shanghai office for Quantitative Researcher, got an '
     'OA invitation quickly, and that the test mandated Python, 3 questions in 2 hours, all of '
     'which are already on the forum (地里都有)'),
    ('The preview dies mid-sentence on the word 收益 (return/profit), which is where the actual '
     'objective function would have been defined — so what is to be maximised, under what '
     'constraint, is unknown, and the other two questions are not visible at all. What survives is '
     'the input shape only. Note also the poster\'s own caveat that these questions are already '
     'circulating on the forum, which means this is a recycled bank rather than a fresh test. ' +
     TRUNC),
    office='Shanghai', lang='mixed')

# ---------------------------------------------------------------- Citadel NXT Engineering Test
add('25939', '2025-10-21', 'Citadel', 'quant_developer', 'experienced', '2026',
    'online_assessment',
    'Citadel "NXT Engineering Test" OA — 90 minutes, 2 coding + 8 multiple choice',
    'the first coding question',
    'coding_string_processing',
    ('第一题描述有点绕但其实很简单的string 处理: 给一个sources (string 二维数组) return一个 string '
     '一维数组input: sourcesP1:'),
    ('Question 1: the description is a bit convoluted but it is really very simple string '
     'processing — given "sources" (a 2-D array of strings), return a 1-D array of strings. '
     'Input: sources; P1: …'),
    ('第一题描述有点绕但其实很简单的string 处理: 给一个sources (string 二维数组) return一个 string '
     '一维数组input: sourcesP1:'),
    (TG + '. Forum tags: #citadel 码农类General@全职 在线笔试 在职跳槽 — engineering track, '
     'full-time, online written test, experienced hire. The poster gives the format as 90 minutes, '
     '2 coding questions and 8 multiple choice'),
    ('The preview is severed exactly where the worked example began — "input: sourcesP1:" is the '
     'start of a concrete input listing that would have made the transformation clear, and without '
     'it the rule mapping a 2-D string array to a 1-D one is undetermined. The poster themselves '
     'call the description convoluted. The second coding question and all 8 multiple-choice '
     'questions are not visible. The named test ("NXT Engineering Test") and the 90/2/8 format are '
     'the reliable part of this record. ' + TRUNC),
    lang='mixed')

# ---------------------------------------------------------------- HRT watcher problem
add('26730', '2025-12-22', 'HRT', 'quant_developer', 'experienced', '2026', 'phone_technical',
    'HRT 技术电面 (technical phone interview)',
    'the single problem, which the poster says the interviewer read out rather than sending',
    'coding_grid_movement_constraint',
    '题目描述一维数组上，玩家被 watcher 盯着就不能走。入参包括：',
    ('Problem description: on a one-dimensional array, the player cannot move while a watcher has '
     'eyes on them. The input parameters include: …'),
    '题目描述一维数组上，玩家被 watcher 盯着就不能走。入参包括：',
    (TG + '. Forum tags: #hudson-river-trading 码农类General@全职 技术电面 在职跳槽. The poster is '
     'annoyed that the interviewer would not hand over the problem in writing — "有点无语，题目得做'
     '笔记，面试官不直接给你" (you have to take notes, the interviewer does not give it to you '
     'directly) — and says it was not an algorithms question but that time was tight'),
    ('The preview stops at the colon that introduces the parameter list, so the win condition, the '
     'watchers\' movement rule and what the function must return are all missing; "被 watcher 盯着'
     '就不能走" is one sentence of a simulation spec. It is worth keeping because the poster '
     'explicitly says the interviewer dictated the problem verbally, which is why the recall is a '
     'reconstruction from notes rather than a paste — that is a reason to distrust the wording but '
     'evidence that the encounter was real. ' + TRUNC),
    lang='mixed')

# ---------------------------------------------------------------- HRT fullstack phone screen
HRT_FS = dict(
    mid='27902', date='2026-04-06', firm='HRT', role='quant_developer', level='experienced',
    cycle='2026', rnd='phone_technical',
    rname='HRT Fullstack Phone Screen',
    poster=(TG + '. Forum tags: #hudson-river-trading 码农类General@全职 技术电面 在职跳槽 — '
            'engineering track, full-time, technical phone interview, experienced hire. Unusually '
            'for this channel the preview is NOT truncated: it ends without an ellipsis, so this '
            'appears to be the poster\'s complete list of what was asked'))
HRT_FS_DOUBT = (
    'The poster wrote the round up as a bare run-on list with no separators — "Python context '
    'managerReact memoization，performance，hooks，render" — so these are topic headings, not '
    'questions as posed; what specifically was asked about a context manager is not recoverable. '
    'They are kept separate because they are plainly distinct prompts. The one genuine mitigation '
    'is that this preview is not truncated, so unlike the rest of this batch nothing is being '
    'hidden by the ellipsis. Note this is a fullstack engineering screen at a quant firm, not a '
    'quantitative assessment.')

add(**HRT_FS, section='the technical portion of the screen', qtype='language_python_semantics',
    qtext='Python context manager',
    qtext_en='Python context manager.',
    quote='Python context manager',
    doubt=HRT_FS_DOUBT, lang='mixed')

add(**HRT_FS, section='the technical portion of the screen', qtype='frontend_react_performance',
    qtext='React memoization，performance，hooks，render',
    qtext_en='React memoization, performance, hooks, render.',
    quote='React memoization，performance，hooks，render',
    doubt=HRT_FS_DOUBT, lang='mixed')

add(**HRT_FS, section='the closing scenario question',
    qtype='scenario_debugging_oncall',
    qtext='Oncall的时候如果一个同事告诉你app render太慢了怎么办',
    qtext_en=('When you are on call, what do you do if a colleague tells you the app is rendering '
              'too slowly?'),
    quote='Oncall的时候如果一个同事告诉你app render太慢了怎么办',
    doubt=('This one is a complete question as posed and needs no reconstruction, which makes it '
           'the soundest item in this message. ' + HRT_FS_DOUBT), lang='mixed')

# ---------------------------------------------------------------- SIG phone screen
SIG_1036408 = dict(
    mid='17164', date='2024-01-03', firm='SIG', role='quant_developer', level='experienced',
    cycle='2024', rnd='phone_technical',
    rname='SIG 店面 (phone interview) — the poster says they had just finished it',
    poster=(TG + '. Forum tags: #sig 码农类General@全职 技术电面 在职跳槽 — engineering track, '
            'full-time, technical phone interview, experienced hire. The post opens with four '
            'repetitions of 求大米 (begging for forum karma) and 刚面完的 新鲜热乎的 (just '
            'finished, fresh off the stove)'))

add(**SIG_1036408,
    section='the opening segment, which revisits the candidate\'s own online assessment',
    qtype='followup_complexity_optimisation',
    qtext='先讨论OA的思路 然后问问有没有优化 时间和空间复杂度',
    qtext_en=('First we discussed the approach to the OA, then he asked whether there were any '
              'optimisations, and the time and space complexity.'),
    quote='先讨论OA的思路 然后问问有没有优化 时间和空间复杂度',
    doubt=('This describes the shape of the round rather than quoting a question: the interviewer '
           'walked the candidate through their own earlier OA submission and pushed on complexity. '
           'Which OA problem was under discussion is not stated anywhere in the visible text, so '
           'the substantive content is unknown. Recorded because "they re-open your OA solution and '
           'ask you to optimise it" is itself a checkable claim about SIG\'s process. ' + TRUNC),
    lang='mixed')

add(**SIG_1036408,
    section='a short coding exercise after the OA discussion',
    qtype='concurrency_multithreading',
    qtext='然后有个小的coding 他问我有没有有没有写过多线程',
    qtext_en=('Then there was a small coding exercise; he asked me whether I had ever written '
              'multithreaded code.'),
    quote='然后有个小的coding 他问我有没有有没有写过多线程',
    doubt=('The preview is cut off immediately after this, so whether the multithreading question '
           'went beyond "have you written any" into an actual exercise is unknown — the "小的'
           'coding" (small coding task) is mentioned but never specified. The doubled 有没有有没有 '
           'is the poster typing quickly, not a transcription error on my part. ' + TRUNC),
    lang='mixed')

# ---------------------------------------------------------------- verify + emit
ORDER = ['firm', 'role_track', 'level', 'cycle', 'office', 'round', 'round_name', 'platform',
         'section_context', 'question_type', 'question_text', 'question_text_en',
         'reported_answer', 'source_url', 'source_type', 'source_quote', 'source_language',
         'post_date', 'access', 'retrieval_method', 'upstream_source', 'poster_context', 'doubt']


def norm(s):
    return re.sub(r'\s+', '', s.replace('\u00a0', ' ').replace('\u200b', ''))


ok, bad = [], []
for rec in R:
    mid = rec.pop('_mid')
    if norm(rec['source_quote']) in norm(page_text(mid)):
        ok.append(rec)
    else:
        bad.append((mid, rec['firm'], rec['source_quote'][:60]))

for b in bad:
    sys.stderr.write(f'QUOTE NOT FOUND: {b}\n')

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in ok:
        f.write(json.dumps({k: rec[k] for k in ORDER}, ensure_ascii=False) + '\n')
print(f'verified+written={len(ok)}  failed={len(bad)}')
