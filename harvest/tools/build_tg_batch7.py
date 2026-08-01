#!/usr/bin/env python3
"""Seventh @usinterview batch — the deep before=/q= pagination sweep.

Earlier passes only ever saw the first page of each t.me/s/<ch>?q=<term> search, which is the
most recent ~11 matches. Telegram will page further back, but only when before= precedes q= in
the query string; with the parameters the other way round it silently returns nothing. Fixing
the order exposed the channel's whole firm-hashtag history and with it a large block of recalls
whose link preview happens to contain the question itself rather than just the poster's preamble.

Every quote below is checked against the stored copy of the canonical message page
(raw/pages/tgmsg/<id>.html) before the record is emitted.
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


TG = ('@usinterview ("北美跳槽面经") is a public Telegram channel, readable at t.me/s/usinterview '
      'with no account, that auto-forwards new 1point3acres 海外面经 threads. Each message carries '
      'the thread title, the firm/role/round/seniority tags the poster chose on the forum, and the '
      'opening of the post body as a link preview')
TRUNC = ('The Telegram link preview is cut to a fixed length and visibly ends in "…", so only the '
         'opening of the recall is readable here. 1point3acres Cloudflare-blocks this machine and '
         'the Wayback Machine has no 200 snapshot of the thread, so the remainder is unrecoverable')
KARMA = ('1point3acres hides parts of a post behind a karma wall ("**** 本内容被作者隐藏 ****"), and '
         'the Telegram preview reproduces the placeholder rather than the text, so an unknown amount '
         'of the recall is missing')
UPSTREAM = ('1point3acres forum thread auto-forwarded into the channel; the forum thread itself is '
            'Cloudflare-blocked to this machine, so only the forwarded preview was read')

R = []


def add(mid, date, firm, role, level, cycle, rnd, rname, section, qtype, qtext, qtext_en,
        quote, poster, doubt, answer=None, office='unknown', lang='zh', platform='unknown'):
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': platform, 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext_en,
        'reported_answer': answer, 'source_url': f'https://t.me/usinterview/{mid}',
        'source_type': 'chat_telegram', 'source_quote': quote, 'source_language': lang,
        'post_date': date, 'access': 'full_text', 'retrieval_method': 'webfetch',
        'upstream_source': UPSTREAM, 'poster_context': poster, 'doubt': doubt, '_mid': mid})


def ctx(tags, extra=''):
    return TG + f'. Forum tags: {tags}' + (f'. {extra}' if extra else '')


# ============================================================ HRT first-round phone, 2020
HRT678 = dict(mid='678', date='2020-03-11', firm='HRT', role='unknown', level='experienced',
              cycle='2020', rnd='phone_technical', rname='HRT 一轮电面 (first-round phone screen)',
              poster=ctx('#HRT @全职 技术电面 在职跳槽 — full-time, technical phone screen, '
                         'experienced hire changing jobs',
                         'The poster says 总共问了三道题目 (three questions in total) and numbers them'))

add(**HRT678, section='question 1 of the three the poster numbers',
    qtype='probability_bayes_biased_coin',
    qtext=('一堆硬币，99个正常，1个双head。随机拿一个扔了10次，10次都是head，问拿到的那个是双head的'
           '概率。'),
    qtext_en=('A pile of coins: 99 are normal and 1 is double-headed. You take one at random and '
              'toss it 10 times; all 10 come up heads. What is the probability that the one you '
              'took is the double-headed coin?'),
    quote=('HRT第一轮电面面经总共问了三道题目：1. 一堆硬币，99个正常，1个双head。随机拿一个扔了10次，'
           '10次都是head，问拿到的那个是双head的概率。'),
    doubt=('Fully stated and self-contained, which is the best case for this source, but it is still '
           'a one-line paraphrase written from memory after the call rather than the interviewer\'s '
           'wording, and the poster gives no answer, so nothing here can be cross-checked. '
           'This is also a textbook-shaped Bayes problem, which cuts both ways: it is exactly what a '
           'firm would ask, and also exactly what someone reconstructing a half-remembered call would '
           'reach for. ' + TRUNC))

add(**HRT678, section='question 2 of the three, cut off by the preview truncation',
    qtype='probability_dice',
    qtext='一个骰子扔了10',
    qtext_en='A die is rolled 10 [times] —',
    quote='2. 一个骰子扔了10 ',
    doubt=('This is a fragment, not a question: the preview truncates in the middle of the sentence '
           'after seven characters, so all that survives is that question 2 involved rolling a die ten '
           'times. It is logged because the poster states there were three questions and this fixes '
           'what the second one was about, but nobody could answer it as written and it must not be '
           'treated as a question statement. ' + TRUNC))

# ============================================================ HRT technical phone, 2020-12
HRT4411 = dict(mid='4411', date='2020-12-22', firm='HRT', role='unknown', level='experienced',
               cycle='2021', rnd='phone_technical',
               rname='HRT (Hudson River Trading) 技术电面 — a ~45-minute conversational phone screen',
               poster=ctx('#HRT (Hudson River Trading) @全职 技术电面 在职跳槽',
                          'The poster describes it as 电话聊天形式的技术面试，大概45分钟 (a '
                          'conversation-style technical interview, about 45 minutes) and lists what '
                          'was asked as a numbered list'))
D4411 = ('One clause long and stripped of whatever follow-ups the interviewer actually asked, so this '
         'records the topic rather than the question as put. These are also generic enough that a '
         'poster could have produced them from expectation rather than memory. ' + TRUNC)

add(**HRT4411, section='item 2 of the numbered list of what was asked',
    qtype='cs_fundamentals_memory', qtext='stack和heap的区别',
    qtext_en='The difference between the stack and the heap.',
    quote='问了以下内容：1. 简历的项目2. stack和heap的区别', doubt=D4411)

add(**HRT4411, section='item 3 of the numbered list of what was asked',
    qtype='data_structure_implementation', qtext='如何实现map',
    qtext_en='How would you implement a map?',
    quote='2. stack和heap的区别3. 如何实现map', doubt=D4411)

add(**HRT4411, section='item 4 of the numbered list of what was asked',
    qtype='data_structure_design_randomised',
    qtext='实现一个可以push，randomPop的数据结构。像是LC 380/',
    qtext_en=('Implement a data structure supporting push and randomPop. Something like LeetCode '
              '380/…'),
    quote='4. 实现一个可以push，randomPop的数据结构。像是LC 380/',
    doubt=('The poster\'s own cross-reference to a LeetCode number is cut off mid-way ("LC 380/"), so '
           'it is not clear whether they meant 380 alone or a pair of problems. The prompt itself is '
           'stated clearly enough to be answerable. ' + TRUNC))

# ============================================================ HRT OA, 2021-03
add('5538', '2021-03-08', 'HRT', 'unknown', 'experienced', '2021', 'online_assessment',
    'HRT 80-minute online assessment, two questions',
    'the first of the two OA questions',
    'array_sliding_window_min_range',
    '移除k个连续数字之后数组剩下数字的最小amplitude（max-min）',
    ('The minimum amplitude (max minus min) of what remains of an array after removing k '
     'consecutive numbers.'),
    '今天刚做的HRT 80分钟的OA，两题，一个是移除k个连续数字之后数组剩下数字的最小amplitude（max-min）',
    ctx('#HRT @全职 在线笔试 在职跳槽 — full-time, online written test, experienced hire',
        'The poster says 今天刚做的 (I did it just today), so the recall is same-day'),
    ('Compressed to a single clause, so the exact reading of "移除k个连续数字" is ambiguous — it could '
     'mean removing a contiguous run of k elements or removing k elements that are consecutive in '
     'value, and the two are different problems. Same-day recall of a test the poster had just sat is '
     'about as good as this genre gets on freshness. ' + TRUNC),
    lang='mixed')

add('5538', '2021-03-08', 'HRT', 'unknown', 'experienced', '2021', 'online_assessment',
    'HRT 80-minute online assessment, two questions',
    'the second of the two OA questions, given only as a pointer',
    'assessment_format',
    '另一个是lc 上上周周赛题幺漆漆舞',
    ('The other one was the LeetCode weekly-contest problem from the week before last, [number '
     'written in homophone-obfuscated digits] 幺漆漆舞.'),
    '另一个是lc 上上周周赛题幺漆漆舞',
    ctx('#HRT @全职 在线笔试 在职跳槽'),
    ('Not a question statement at all — it is a pointer to a LeetCode weekly-contest problem whose '
     'number is written in the homophone-obfuscated digits Chinese forum posters use to dodge keyword '
     'filters (幺漆漆舞). I am deliberately not decoding it, because guessing the number would be '
     'inventing the question. What it does attest is that HRT reused a then-recent public contest '
     'problem verbatim in a paid assessment. ' + TRUNC),
    lang='mixed')

# ============================================================ HRT C++ phone, 2021-03
HRT5849 = dict(mid='5849', date='2021-03-22', firm='HRT', role='unknown', level='experienced',
               cycle='2021', rnd='phone_technical',
               rname='HRT 店面 — a 45-minute oral knowledge quiz (45分钟知识问答)',
               poster=ctx('#HRT @全职 技术电面 在职跳槽',
                          'The poster describes the round as 45分钟知识问答，主要设计c++的基础知识 '
                          '(45 minutes of Q&A, mostly C++ fundamentals) and runs the topics together '
                          'in one semicolon-separated list'))
D5849 = ('The poster lists these as a run-on string of topics rather than as questions, so the '
         'phrasing is theirs, not the interviewer\'s, and the boundaries between items are only as '
         'reliable as their punctuation. ' + TRUNC)

add(**HRT5849, section='first item in the semicolon-separated list of what was asked',
    qtype='cs_fundamentals_memory', qtext='stack和heap区别，如何track stack的增长',
    qtext_en='The difference between stack and heap; how do you track the growth of the stack?',
    quote='主要设计c++的基础知识，stack和heap区别，如何track stack的增长', doubt=D5849)

add(**HRT5849, section='second item in the list',
    qtype='cs_fundamentals_containers',
    qtext='map和unordered_map区别时间复杂度，hashmap的实现方式',
    qtext_en=('The difference between map and unordered_map and their time complexities; how a '
              'hashmap is implemented.'),
    quote='map和unordered_map区别时间复杂度，hashmap的实现方式', doubt=D5849)

add(**HRT5849, section='third item in the list',
    qtype='tree_kth_largest', qtext='BST的第k大元素怎么求',
    qtext_en='How do you find the k-th largest element of a BST?',
    quote='hashmap的实现方式，BST的第k大元素怎么求', doubt=D5849)

# ============================================================ HRT Python Core Dev, 2021-08
add('7485', '2021-08-16', 'HRT', 'quant_developer', 'experienced', '2021', 'phone_technical',
    'HRT Python Core Dev phone screen, ~45 minutes',
    'the opening segment on Python fundamentals',
    'language_fundamentals_python',
    '关于Python的基础知识(e.g. 什么是generator，context man',
    'Python fundamentals — e.g. what is a generator, what is a context man[ager]…',
    '一开始是面的关于Python的基础知识(e.g. 什么是generator，context man',
    ctx('#HRT 码农类General@全职 技术电面 在职跳槽 — software-engineering track, full-time, '
        'technical phone screen',
        'The poster says the role is Python Core Dev and calls it 他们比较新的职位 (a fairly new '
        'role for them)'),
    ('The preview truncates in the middle of the word "context man[ager]", and the poster themselves '
     'flags these as examples ("e.g."), so this is a sample of the topic list rather than the '
     'questions asked. ' + TRUNC),
    lang='mixed')

# ============================================================ Jump phone screen, 2022-11
JUMP15126 = dict(mid='15126', date='2022-11-15', firm='Jump Trading', role='quant_developer',
                 level='experienced', cycle='2023', rnd='phone_technical',
                 rname='Jump phone interview',
                 poster=ctx('#jumptrading 码农类General@全职 技术电面 在职跳槽 — software-engineering '
                            'track, full-time, technical phone screen, experienced hire'))

add(**JUMP15126, section='the C++ knowledge segment',
    qtype='language_fundamentals_cpp',
    qtext='c++ 常考语言知识virtual fucntion,virtual table. mutex,smart pointer...',
    qtext_en=('The usual C++ language knowledge: virtual function, virtual table, mutex, smart '
              'pointer…'),
    quote='c++ 常考语言知识virtual fucntion,virtual table. mutex,smart pointer...',
    doubt=('A topic list, not questions — the poster gives the areas covered and trails off with "…" '
           'themselves. The typo "fucntion" is the poster\'s. ' + TRUNC),
    lang='mixed')

add(**JUMP15126, section='the algorithm question',
    qtype='dp_budget_constrained_profit',
    qtext=('算法题:给定n个股票,以及未来的价格,在一定budget的情况下,返回最大的收益. e.g. 当'),
    qtext_en=('Algorithm question: given n stocks and their future prices, subject to a fixed budget, '
              'return the maximum profit. e.g. when…'),
    quote='算法题:给定n个股票,以及未来的价格,在一定budget的情况下,返回最大的收益. e.g. 当',
    doubt=('The worked example the poster was about to give ("e.g. 当…") is exactly where the preview '
           'cuts off, and that example is what would have pinned down the ambiguities — whether you '
           'may buy fractional or multiple units, and whether prices are a single future value per '
           'stock or a time series. As written the problem family is clear but the instance is not. '
           + TRUNC),
    lang='mixed')

# ============================================================ Jane Street MLE phone, 2023-06
add('15898', '2023-06-10', 'Jane Street', 'unknown', 'experienced', '2023', 'phone_technical',
    'Jane Street MLE 第一轮店面 (first-round phone screen) for a machine-learning engineer role',
    'the three coding questions, of which the first two are described',
    'string_compression_then_streaming',
    ('3个coding题，第一题是刷题网肆肆参（压缩字符串），第二和第三题都是第一题的延展。第二题问如果输入'
     '是数据流（网络数据'),
    ('Three coding questions. The first was LeetCode [homophone-obfuscated: 肆肆参 = 443] (string '
     'compression); the second and third were both extensions of the first. The second asked what if '
     'the input is a data stream (network data…'),
    ('3个coding题，第一题是刷题网肆肆参（压缩字符串），第二和第三题都是第一题的延展。第二题问如果输入'
     '是数据流（网络数据'),
    ctx('#janestreet MachineLearningEng@全职 技术电面 在职跳槽 — machine-learning engineer, '
        'full-time, technical phone screen, experienced hire',
        'The poster says a headhunter submitted their CV in April and the first phone screen was '
        'mid-May, so the recall is roughly a month old'),
    ('The problem itself is identified only by a LeetCode number written in homophone-obfuscated '
     'digits plus a two-word gloss ("压缩字符串", string compression); the poster never states the '
     'prompt. The extension — re-do it for a streaming input — is the substantive part and it is '
     'truncated mid-parenthesis. ' + TRUNC),
    lang='mixed')

# ============================================================ Optiver ML phone, 2024-07
add('18931', '2024-07-17', 'Optiver', 'unknown', 'experienced', '2024', 'phone_technical',
    'Optiver 机器学习研究工程师店面 — a 60-minute phone screen run by the hiring manager',
    'question (1) of four, the coding one',
    'array_with_duplicates_coding',
    '(1) coding: 给一个数组，里面可能包含重复的数字。写',
    ('(1) coding: you are given an array which may contain duplicate numbers. Write…'),
    '(1) coding: 给一个数组，里面可能包含重复的数字。写',
    ctx('#optiver MachineLearningEng@全职 技术电面 在职跳槽',
        'The poster states 面试官也是hiring manager (the interviewer was also the hiring manager), '
        '一共考了四道题，不全是coding (four questions in all, not all coding), 60 minutes including '
        'the introduction, and that the role is based in Austin'),
    ('The preview cuts off at the verb "写" (write) — i.e. immediately before the poster said what you '
     'were actually asked to write — so the setup survives but the task does not. Logged for the '
     'round structure it fixes (four questions, 60 minutes, hiring manager, Austin) rather than as an '
     'answerable prompt. ' + TRUNC),
    office='Austin', lang='mixed')

# ============================================================ Optiver ML Perf Eng, 2024-10
add('20082', '2024-10-25', 'Optiver', 'unknown', 'experienced', '2024', 'phone_technical',
    'Optiver Machine Learning Performance Engineer video interview',
    'the design question',
    'api_design_callbacks',
    'design 一个class提供四个api,带on的都是callback 用来update internal data structure。最后一',
    ('Design a class exposing four APIs; the ones prefixed with "on" are callbacks used to update the '
     'internal data structure. The last…'),
    'design 一个class提供四个api,带on的都是callback 用来update internal data structure。最后一',
    ctx('#optiver MachineLearningEng@全职 视频面试 在职跳槽',
        'The poster notes 他们的delta one team尝试在用deep learning 去做hft (their delta one team is '
        'trying to use deep learning for HFT)'),
    ('The four APIs are never named and the preview truncates at "最后一" (the last…), so the actual '
     'interface — which is the whole question — is missing. What survives is the shape of the task '
     'and the on-prefixed-callback convention. ' + TRUNC),
    lang='mixed')

# ============================================================ Jump quant superday, 2024-11
add('20374', '2024-11-14', 'Jump Trading', 'quant_researcher', 'experienced', '2025', 'superday',
    'a batch of superday questions the poster collected across several firms',
    'question 1 of the list the poster says they are sharing',
    'probability_uniform_interval',
    '1.[0,1]上每',
    '1. On [0,1], each…',
    '集中分享一些有价值的面试题1.[0,1]上每',
    ctx('#jumptrading 金工类@全职 Onsite 在职跳槽 — quant track, full-time, onsite, experienced hire',
        'The thread title is 补充分享一点quant面试题目，几家都走到super day了 (sharing some more quant '
        'interview questions, I got to superday at several firms) and the poster says they have '
        'several superdays this month, 一天四五面 (four or five interviews a day)'),
    ('A five-character fragment — the preview dies immediately after "1.[0,1]上每" ("On [0,1], each"). '
     'This is not an answerable question and must not be treated as one; it is logged only because it '
     'attests that the list existed and that its first item was a uniform-on-[0,1] problem. Worse for '
     'attribution: the thread is hashtagged #jumptrading but the poster explicitly says they are '
     'pooling questions from several firms they interviewed with, so even the firm on this fragment '
     'is not safe. ' + TRUNC),
    lang='mixed')

# ============================================================ Optiver phone, 2024-12
OPT20685 = dict(mid='20685', date='2024-12-12', firm='Optiver', role='quant_developer',
                level='experienced', cycle='2025', rnd='phone_technical',
                rname='Optiver technical phone screen',
                poster=ctx('#Optiver 码农类General@全职 技术电面 在职跳槽 — software-engineering '
                           'track, full-time, technical phone screen, experienced hire',
                           'The poster is begging for forum karma (大哥大姐给点米吧) and gives the '
                           'round as a bulleted list, the bullets rendered as [*]'))

add(**OPT20685, section='the second bullet of the round\'s question list',
    qtype='estimation_memory_footprint',
    qtext='An array of 1000 integers of 0-1000000,how many bytes does it require to store?',
    qtext_en='An array of 1000 integers of 0-1000000, how many bytes does it require to store?',
    quote='[*]An array of 1000 integers of 0-1000000,how many bytes does it require to store?',
    doubt=('Rare for this source in that the poster wrote the prompt out in English rather than '
           'paraphrasing it in Chinese, which suggests they were copying the interviewer\'s wording — '
           'but that also means it could have been copied from somewhere else. No answer is given, and '
           'the question is under-specified as written (integer width is exactly what is being probed), '
           'which is consistent with it being a deliberately open estimation prompt. The list continues '
           'past this bullet and is truncated at "[*]Wh". ' + TRUNC),
    lang='en')

# ============================================================ Jane Street phone, 2025-03
add('21868', '2025-03-14', 'Jane Street', 'quant_developer', 'experienced', '2025',
    'phone_technical', 'Jane Street 电面 (phone screen), reported as a fail',
    'the single question, which the poster says had appeared on the forum before',
    'ood_trading_system',
    ('题目是之前地里出现过的trading system。有个class叫Item,里面有buyer，seller，price，item_name'
     '这几个field,还有个class叫Database，有个show_all_items()的method。'),
    ('The question was the trading system one that has appeared on the forum before. There is a class '
     'called Item with the fields buyer, seller, price and item_name, and a class called Database with '
     'a show_all_items() method.'),
    ('题目是之前地里出现过的trading system。有个class叫Item,里面有buyer，seller，price，item_name'
     '这几个field,还有个class叫Database，有个show_all_items()的method。'),
    ctx('#janestreet 码农类General@全职 技术电面 在职跳槽',
        'The poster explicitly says 之前地里出现过 — this exact problem had already been posted on '
        '1point3acres, i.e. Jane Street is reusing it'),
    ('The setup is given in full but the task is not: the poster describes the two classes and their '
     'fields and then the preview ends, so what you were asked to build on top of them is missing. '
     'The poster\'s own claim that the problem was already circulating on the forum is worth taking '
     'seriously in both directions — it makes reuse likely, and it also means the poster could be '
     'reciting the forum version rather than what they were asked. ' + TRUNC),
    lang='mixed')

# ============================================================ Jane Street onsite, 2025-09
add('25338', '2025-09-17', 'Jane Street', 'quant_developer', 'experienced', '2025', 'onsite',
    'Jane Street on-site',
    'the whole onsite — the poster says this was the only question',
    'diff_merge_index_shifting',
    ('merge diffs:{0: A,3: B} + {0: C,4: D}orig:{0: z,1: z,2: z}new:{0: C,1: A,2: z,3: z,4: D,5: B,6'),
    ('merge diffs: {0: A, 3: B} + {0: C, 4: D}; orig: {0: z, 1: z, 2: z}; new: {0: C, 1: A, 2: z, '
     '3: z, 4: D, 5: B, 6…'),
    ('这是唯一一个题目，merge diffs:{0: A,3: B} + {0: C,4: D}orig:{0: z,1: z,2: z}'
     'new:{0: C,1: A,2: z,3: z,4: D,5: B,6'),
    ctx('#janestreet 工程类@全职 Onsite 在职跳槽 — engineering track, full-time, onsite',
        'The poster says 上个月考了Jane street的on-site，这是唯一一个题目 (I sat Jane Street\'s '
        'onsite last month; this was the only question)'),
    ('The poster gives concrete input and expected-output data, which is unusually specific, but no '
     'prose statement of what "merge diffs" is supposed to mean — the semantics have to be inferred '
     'from the example, and the example is itself truncated in the middle of the expected output at '
     '"5: B,6". Whether the interviewer defined the diff format verbally or on a shared screen is not '
     'recoverable. ' + TRUNC),
    lang='mixed')

# ============================================================ Jane Street SRE, 2025-09
add('25499', '2025-09-26', 'Jane Street', 'quant_developer', 'experienced', '2025',
    'phone_technical', '简街SRE代码面试 — a Jane Street SRE coding interview, written on paper',
    'the coding question',
    'rate_limiting_log_scan',
    ('出的相当于一个rate limiting题目。给list of IP access log lines with IP address and timestamp，'
     'flag IP addresses that  access too frequently w'),
    ('What they set was essentially a rate-limiting problem. Given a list of IP access log lines with '
     'IP address and timestamp, flag IP addresses that access too frequently w[ithin…]'),
    ('出的相当于一个rate limiting题目。给list of IP access log lines with IP address and timestamp，'
     'flag IP addresses that  access too frequently w'),
    ctx('#janestreet 码农类General@全职 技术电面 在职跳槽',
        'The poster notes 就是纯纸上写算法 (purely writing the algorithm on paper) — no editor'),
    ('The preview cuts off at "too frequently w", i.e. exactly at the window definition, which is the '
     'only parameter that makes the problem well posed. The poster is partly quoting the prompt in '
     'English inside a Chinese sentence, which suggests they had the wording in front of them; note '
     'the double space in "that  access", which I have preserved. ' + TRUNC),
    lang='mixed')

# ============================================================ Citadel GQS onsite, 2025-10
add('25896', '2025-10-18', 'Citadel', 'quant_developer', 'experienced', '2026', 'onsite',
    'Citadel GQS (Global Quantitative Strategies) in-person onsite',
    'the one question the poster names from the phone round preceding the onsite',
    'graph_dependency_resolution',
    '店湎问了一个计算machine dependency的问题',
    'The phone screen asked a question about computing machine dependency.',
    '店湎问了一个计算machine dependency的问题 有人面过gqs的 in person onsite方便分享一下流程是什么吗',
    ctx('#citadel 码农类General@全职 Onsite 在职跳槽',
        'The whole post is a request for information — the poster gives this one line about the phone '
        'round and then asks whether anyone has done the GQS in-person onsite'),
    ('One clause and no problem statement: "计算machine dependency" names a topic, not a question, and '
     '店湎 is a typo/obfuscation of 店面 (phone screen), so even the round this belongs to is inferred '
     'rather than stated. Logged as a topic datapoint only. This message is unusual in that it is not '
     'truncated — the poster genuinely wrote only this much.'),
    lang='mixed')

# ============================================================ Jane Street frontend, 2025-10
add('25929', '2025-10-21', 'Jane Street', 'quant_developer', 'experienced', '2026',
    'phone_technical',
    'Jane Street 第一次电话面试 (first phone interview) for a Fullstack/Frontend role',
    'the first phone round, described as a build task',
    'frontend_build_calculator',
    ('要求我做一个 calculator，尽量模仿这个网站的功能和样式：https://calculator-eight-zeta.vercel.app/'),
    ('They asked me to build a calculator, imitating the functionality and styling of this site as '
     'closely as possible: https://calculator-eight-zeta.vercel.app/'),
    ('第一次电话面试：要求我做一个 calculator，尽量模仿这个网站的功能和样式：'
     'https://calculator-eight-zeta.vercel.app/'),
    ctx('#janestreet 码农类General@全职 技术电面 在职跳槽',
        'The poster says 我面的是 Fullstack/Frontend 岗位 (I interviewed for the Fullstack/Frontend '
        'role) and was rejected after the second phone round'),
    ('The specification is a URL rather than prose, and I have not opened that URL, so what the target '
     'calculator actually does is not something I can attest to — only that the poster says they were '
     'pointed at it. A live vercel.app link in an interview prompt is also the kind of detail that '
     'could be the poster\'s own scratch deployment rather than the interviewer\'s. ' + TRUNC),
    lang='mixed')

# ============================================================ Citadel NXT OA, 2025-10
add('25939', '2025-10-21', 'Citadel', 'quant_developer', 'experienced', '2026',
    'online_assessment',
    'Citadel NXT Engineering Test — 90 minutes, two coding questions and eight multiple choice',
    'the first of the two coding questions',
    'string_matrix_transform',
    ('第一题描述有点绕但其实很简单的string 处理: 给一个sources (string 二维数组) return一个 string '
     '一维数组input: sourcesP1: '),
    ('The first question is described in a slightly convoluted way but is really very simple string '
     'processing: given sources (a 2-D array of strings), return a 1-D array of strings. input: '
     'sources P1: …'),
    ('90 分钟两道Coding 8道 Multiple Choice第一题描述有点绕但其实很简单的string 处理: 给一个sources '
     '(string 二维数组) return一个 string 一维数组input: sourcesP1: '),
    ctx('#citadel 码农类General@全职 在线笔试 在职跳槽'),
    ('The poster was mid-way through transcribing the worked example ("input: sourcesP1: ") when the '
     'preview cut off, and without that example the transformation from the 2-D input to the 1-D '
     'output is completely undetermined — the poster even says the description was convoluted. The '
     'format line (90 minutes, 2 coding + 8 MCQ) is the solid part of this record. ' + TRUNC),
    lang='mixed')

# ============================================================ Jump quant researcher, 2025-10
add('25992', '2025-10-24', 'Jump Trading', 'quant_researcher', 'experienced', '2026',
    'take_home',
    'a Jump quant-researcher round the poster describes as 比较open ended',
    'the preparation instruction sent before the interview',
    'take_home_dataset_presentation',
    ('找个你喜欢的dataset 和quant researcher的一个比较open ended的面 总体感觉不错As a part of this '
     'interview,we would like for you to prepare the following:* Ple'),
    ('Find a dataset you like — an fairly open-ended interview with a quant researcher; overall a good '
     'impression. "As a part of this interview, we would like for you to prepare the following: * '
     'Ple[ase…]"'),
    ('找个你喜欢的dataset 和quant researcher的一个比较open ended的面 总体感觉不错As a part of this '
     'interview,we would like for you to prepare the following:* Ple'),
    ctx('#jumptrading 码农类General@全职 技术电面 在职跳槽'),
    ('The poster is pasting Jump\'s own email verbatim and the preview truncates at "* Ple" — the '
     'first bullet of the actual instructions. So the format (bring a dataset of your choosing, '
     'discuss it open-endedly with a QR) is attested but the specification is not. ' + TRUNC),
    lang='mixed')

# ============================================================ Eclipse Trading, 2025-11
add('26128', '2025-11-02', 'Eclipse Trading', 'quant_developer', 'experienced', '2026',
    'online_assessment',
    'Eclipse Trading core-dev OA — the poster reproduces the test\'s own comment header',
    'the single problem on the test',
    'cpp_quoting_algorithm',
    ('// This test consists of 1 problem. // Problem 1. // In C++,implement a quoting algorith'),
    ('// This test consists of 1 problem. // Problem 1. // In C++, implement a quoting algorith[m…]'),
    ('OA 题目如下：// This test consists of 1 problem. // Problem 1. // In C++,implement a quoting '
     'algorith'),
    ctx('#akunacapital 码农类General@全职 技术电面 在职跳槽 — note the hashtag says Akuna but the '
        'thread is about a different firm',
        'The poster describes the employer as HK 一个 做 market making 的 prop shop (a Hong Kong '
        'market-making prop shop) and names it Eclipse Trading in the title'),
    ('Not one of the target firms — Eclipse Trading is a Hong Kong market maker — and the forum '
     'hashtag is #akunacapital, which is simply wrong for this thread and shows how unreliable the '
     'tags are as firm attribution. The prompt itself is a verbatim paste of the test\'s comment '
     'header and truncates at "implement a quoting algorith", i.e. before any of the specification. '
     'Kept because a market maker asking for a quoting algorithm in C++ is a real and specific '
     'datapoint, but it is not answerable. ' + TRUNC),
    office='Hong Kong', lang='mixed')

# ============================================================ CTC phone, 2025-11
add('26211', '2025-11-07', 'Chicago Trading Company', 'quant_developer', 'experienced', '2026',
    'phone_technical', 'CTC 电面 (phone screen), reported as a fail',
    'the single coding question',
    'cpp_implement_shared_ptr',
    '用c++写一个shared pointer class',
    'Write a shared pointer class in C++.',
    ('用c++写一个shared pointer class有一个test case没过，死活debug不出来。最后挂了'),
    ctx('#citadel 码农类General@全职 技术电面 在职跳槽 — the hashtag is Citadel but the title says CTC',
        'The poster adds that one test case would not pass, they could not debug it, and the '
        'interviewer 给完题就开始自己干活了，没管我 (set the problem then got on with their own work '
        'and ignored me)'),
    ('The firm attribution is internally inconsistent: the thread is hashtagged #citadel but titled '
     '"CTC 电面", and CTC is Chicago Trading Company, a different firm. I have gone with the title '
     'over the tag, but a reader should treat the firm on this record as contested. The question '
     'itself is short, complete and unambiguous — and also the single most common C++ interview task '
     'in existence, so it carries little information. This message is not truncated.'),
    lang='mixed')

# ============================================================ Optiver OA, 2026-01
add('26844', '2026-01-10', 'Optiver', 'quant_developer', 'experienced', '2026',
    'online_assessment', 'Optiver OA, take-home style — the email said 1-3 hours is typical',
    'the poster\'s answers/test data for Q1 and Q2, given without the prompts',
    'answer_key_fragment_only',
    'Q1: 2011-1-3 2011-1-5Q2: A,B A,C C,D D,B',
    'Q1: 2011-1-3 2011-1-5  Q2: A,B A,C C,D D,B',
    ('如图最近没刷题。花了三个多小时做完他给的测试不全。Q1: 2011-1-3 2011-1-5Q2: A,B A,C C,D D,B'),
    ctx('#optiver 码农类General@全职 在线笔试 在职跳槽',
        'The poster opens 如图 ("as in the picture"), i.e. the actual questions were attached as '
        'images, and warns 他给的测试不全 (the tests they give you are incomplete) and that the email '
        'said it normally takes 1-3 hours'),
    ('This is not a question — it is two lines of data (a pair of dates, and a set of letter pairs '
     'that look like graph edges) with the prompts entirely absent, because the poster attached them '
     'as images and wrote 如图. Telegram\'s link preview does not carry the images. Logged as an '
     'answer/test-data fragment so it is not mistaken for a prompt; on its own it is unusable. '
     + TRUNC),
    lang='mixed')

# ============================================================ Citadel EQR OA, 2026-01
add('26954', '2026-01-21', 'Citadel', 'quant_developer', 'experienced', '2026',
    'online_assessment',
    'Citadel EQR HackerRank OA — three questions, which the poster says they finished in half an hour',
    'the three OA questions, listed together',
    'coding_trio_palindrome_tokens_tree',
    ('OA hackerrank,1个palindrome，1个lazy delete算token valid，最后一个bfs找tree的最长直径上的点'),
    ('OA on HackerRank: one palindrome, one "lazy delete" token-validity problem, and the last one '
     'BFS to find the points on the longest diameter of a tree.'),
    ('OA hackerrank,1个palindrome，1个lazy delete算token valid，最后一个bfs找tree的最长直径上的点，'
     '半小时三个都秒了'),
    ctx('#citadel 码农类General@全职 技术电面 在职跳槽',
        'The poster gives their background as 1.5 YOE hf dev and says a recruiter reached out; they '
        'add 半小时三个都秒了 (I nailed all three in half an hour)'),
    ('Three problems compressed into one clause each, so these are topic labels rather than prompts — '
     '"1个palindrome" in particular could be almost any of a dozen problems. The middle one, "lazy '
     'delete算token valid", is not a standard problem name and I cannot tell what it is without the '
     'prompt. The tree-diameter one is described precisely enough to be identifiable. ' + TRUNC),
    lang='mixed')

# ============================================================ Citadel Securities phone, 2026-01
add('26997', '2026-01-25', 'Citadel', 'quant_developer', 'experienced', '2026', 'phone_technical',
    'Citadel Securities phone interview, reported as a pass',
    'the bulleted list of what was asked, rendered with [*] bullets',
    'cache_design_lru_lfu',
    '[*]LRU implementation[*]LFU implementation[*]Customized Evict fu',
    'LRU implementation; LFU implementation; customized evict fu[nction…]',
    ('虽然还是过了[*]LRU implementation[*]LFU implementation[*]Customized Evict fu'),
    ctx('#citadel 码农类General@全职 技术电面 在职跳槽',
        'The poster prefaces the list with Citsec面试总是有一种，并不是很难，但是里面的人就打死都不想'
        '让你过的感觉 (Citsec interviews always feel like they are not that hard, but the people '
        'inside are dead set against letting you through)'),
    ('Three bullets, each a name rather than a statement, and the third truncates mid-word at '
     '"Customized Evict fu". The sequence — LRU, then LFU, then a custom eviction policy — reads as '
     'one escalating question rather than three separate ones, but the poster does not say so and I '
     'am not going to assume it. ' + TRUNC),
    lang='mixed')

# ============================================================ Jump OA, 2026-01
add('27009', '2026-01-27', 'Jump Trading', 'quant_developer', 'experienced', '2026',
    'online_assessment',
    'Jump OA on Codility — two coding questions, 100 minutes',
    'the second of the two questions',
    'string_parsing_permissions',
    '2.给一坨file query，每行由{owner,permission,filename} 判断哪些是read only',
    ('2. Given a pile of file queries, each line consisting of {owner, permission, filename}, '
     'determine which are read only.'),
    ('两道很straight forward的coding限时100分钟，codility1. 解题思路蕾似牛嗣牛2.给一坨file query，'
     '每行由{owner,permission,filename} 判断哪些是read only'),
    ctx('#jumptrading 码农类General@全职 在线笔试 在职跳槽',
        'The poster calls both questions 很straight forward and is asking for karma (球球大米)'),
    ('The record of the input format is precise but the output condition ("判断哪些是read only") is '
     'stated in five characters with no definition of what makes an entry read-only, which is the '
     'entire content of the problem. Question 1 is given only as 解题思路蕾似牛嗣牛 — a '
     'homophone-obfuscated pointer to another problem — which I have not decoded and am not logging '
     'as a question. This message is not truncated.'),
    lang='mixed')

# ============================================================ Citadel OA optimisation, 2026-02
add('27143', '2026-02-06', 'Citadel', 'quant_developer', 'experienced', '2026',
    'online_assessment', 'Citadel OA — an optimisation/refactoring question',
    'the boilerplate the test hands you, quoted by the poster',
    'code_optimisation_refactor',
    ('/// Refactor and speed up the code below/// The current implementation is correct but slow'
     'int root_node(std::vector out'),
    ('/// Refactor and speed up the code below /// The current implementation is correct but slow '
     'int root_node(std::vector out…'),
    ('这个样板代码非常的奇葩#include /// Refactor and speed up the code below/// The current '
     'implementation is correct but slowint root_node(std::vector out'),
    ctx('#citadel 码农类General@全职 在线笔试 在职跳槽',
        'The poster\'s only comment is 这个样板代码非常的奇葩 (this boilerplate is really bizarre)'),
    ('The poster is pasting the test\'s own comment header and function signature, so the wording is '
     'the assessment\'s rather than a paraphrase — but the paste is truncated at "int '
     'root_node(std::vector out", meaning the slow implementation you are supposed to speed up is '
     'entirely missing, and that body is the question. Note also that the "#include" line lost its '
     'header name to HTML angle-bracket stripping somewhere between the forum and the preview. '
     + TRUNC),
    lang='mixed')

# ============================================================ Two Sigma QR OA, 2026-02
TS27360 = dict(mid='27360', date='2026-02-27', firm='Two Sigma', role='quant_researcher',
               level='experienced', cycle='2026', rnd='online_assessment',
               rname='Two Sigma QR OA — three questions',
               poster=ctx('#twosigma 分析|数据科学类@全职 在线笔试 在职跳槽 — analytics/data-science '
                          'track, full-time, online written test, experienced hire',
                          'The poster labels the recall 新鲜 (fresh)'))

add(**TS27360, section='question 1 of three',
    qtype='piecewise_linear_interpolation',
    qtext='第一题是一个list 把二维的点用线段连起来得到一个分段线性函数 求target x对应函数值',
    qtext_en=('The first question: given a list, join the 2-D points with line segments to get a '
              'piecewise linear function, then find the function value corresponding to a target x.'),
    quote='三道题 第一题是一个list 把二维的点用线段连起来得到一个分段线性函数 求target x对应函数值',
    doubt=('Stated compactly but completely enough to be implementable, which is unusual here. What is '
           'missing is everything that makes it an interview question rather than an exercise — '
           'whether the points arrive sorted, what happens outside the range of the points, and '
           'whether multiple queries are expected. This message is not truncated: the poster wrote '
           'only these two lines.'),
    lang='mixed')

add(**TS27360, section='questions 2 and 3 of three',
    qtype='assessment_format',
    qtext='后两题考的都是拿pandas处理数据',
    qtext_en='The last two questions were both about processing data with pandas.',
    quote='后两题考的都是拿pandas处理数据',
    doubt=('Not a question — a one-line characterisation of two questions the poster chose not to '
           'describe. Logged for the tooling datapoint (a Two Sigma QR assessment testing pandas '
           'directly) and nothing more.'),
    lang='mixed')

# ============================================================ Citadel Securities, 2026-03
add('27466', '2026-03-08', 'Citadel', 'quant_developer', 'experienced', '2026', 'phone_technical',
    'Citadel Securities 一面 (first round) for a C++ Software Engineer role, one hour',
    'the coding half — the poster says the first 30 minutes were CV grilling',
    'concurrency_spmc_queue',
    '后30分钟一道很简单的ood,实现一个Single Producer Multiple Consume',
    ('The last 30 minutes: one very easy OOD question — implement a Single Producer Multiple '
     'Consume[r…]'),
    ('前30分钟拷打简历，后30分钟一道很简单的ood，实现一个Single Producer Multiple Consume'),
    ctx('#citadel 码农类General@全职 技术电面 在职跳槽',
        'The poster notes 面试官是一个工作多年的中国人 (the interviewer was a Chinese engineer with '
        'many years there) and the role is C++ Software Engineer'),
    ('Truncated mid-word at "Single Producer Multiple Consume", so whether the object to implement was '
     'a queue, a ring buffer or something else is not stated — I have not filled that in. The poster '
     'calls it 很简单 (very easy), which is worth noting given SPMC is not usually considered easy; '
     'that may say more about their background than the question. ' + TRUNC),
    lang='mixed')

# ============================================================ Jane Street onsite, 2026-03
add('27543', '2026-03-13', 'Jane Street', 'quant_developer', 'experienced', '2026', 'onsite',
    'Jane Street onsite — two sessions in the morning, reported as a fail',
    'question 1 of the numbered list',
    'class_modification_table',
    ('1. 改已有的一个classclass Table: def_init_(self,filters,times) pass def add_t'),
    ('1. Modify an existing class: class Table: def __init__(self, filters, times): pass; def add_t…'),
    ('1. 改已有的一个classclass Table: def_init_(self,filters,times) pass def add_t'),
    ctx('#janestreet 码农类General@全职 Onsite 在职跳槽',
        'The poster writes 上午两场，中午吃完饭就被送回家了 好难好难懒得面了 躺平！ (two sessions in '
        'the morning, sent home right after lunch; so hard, I cannot be bothered any more, I quit)'),
    ('The class skeleton is being transcribed when the preview cuts off at "def add_t", so the method '
     'you are asked to add — the actual task — is missing, as is what "modify" was supposed to '
     'achieve. The underscores in "def_init_" are mangled markdown from the forum, not the real '
     'signature. ' + TRUNC),
    lang='mixed')

# ============================================================ Citadel GQS QR, 2026-04
add('28247', '2026-04-28', 'Citadel', 'quant_researcher', 'experienced', '2026', 'phone_technical',
    'Citadel GQS Quant Researcher 第一轮 (first round) — 30 minutes of CV discussion then one '
    'technical question',
    'the single technical question of the round',
    'optimisation_quadratic_form_boundedness',
    ('min x^\\top Q x + c^\\top xQ 和 c 都是实数讨论什么时候，这个问题有finit'),
    ('min x^T Q x + c^T x, where Q and c are both real. Discuss when this problem has a finit[e '
     'solution…]'),
    ('只考了一个techiniacl questionmin x^\\top Q x + c^\\top xQ 和 c 都是实数讨论什么时候，这个问题'
     '有finit'),
    ctx('#citadel 金工类@全职 技术电面 在职跳槽 — quant track, full-time, technical phone screen, '
        'experienced hire',
        'The thread title is 求米！2026 Citadel GQS 第一轮 Quant Researcher and the poster says the '
        'round was 30 minutes of CV discussion plus this one technical question'),
    ('The prompt is written in raw LaTeX inside the forum post, which is a good sign that the poster '
     'was reproducing rather than reconstructing, and the question is essentially complete: it asks '
     'when the unconstrained quadratic program is bounded below. It is truncated at "有finit" — the '
     'word is plainly "finite" but I have not completed it in the quote, and any follow-up parts are '
     'lost. "Q 和 c 都是实数" (Q and c are both real) is a loose way of saying real-valued matrix and '
     'vector. ' + TRUNC),
    lang='mixed')

# ============================================================ Akuna OA, 2026-05
add('28581', '2026-05-25', 'Akuna', 'data_scientist', 'experienced', '2026', 'online_assessment',
    'Akuna DataEng OA — the poster pastes their own submitted code rather than the prompts',
    'the signature of the function the OA required',
    'graph_max_difference',
    'public static int maximumDifference(int gNodes,List gFrom,List gTo) {',
    ('public static int maximumDifference(int gNodes, List gFrom, List gTo) { …'),
    'public static int maximumDifference(int gNodes,List gFrom,List gTo) {',
    ctx('#akunacapital DataEng@全职 在线笔试 在职跳槽 — data-engineering track, full-time, online '
        'written test, experienced hire'),
    ('The poster pasted their solution code, not the question, so what maximumDifference is supposed '
     'to compute over the graph (gNodes, gFrom, gTo) is nowhere stated — the name and the signature '
     'are all there is. The generic-type parameters have been eaten by angle-bracket stripping '
     '("List gFrom" was "List<Integer> gFrom"). Logged as evidence of the task shape, not as an '
     'answerable prompt. ' + TRUNC),
    lang='en')

add('28581', '2026-05-25', 'Akuna', 'data_scientist', 'experienced', '2026', 'online_assessment',
    'Akuna DataEng OA — the poster pastes their own submitted code rather than the prompts',
    'a second, SQL section of the same OA',
    'sql_query',
    '50UNION ALLSELECT',
    '…50 UNION ALL SELECT…',
    '50UNION ALLSELECT',
    ctx('#akunacapital DataEng@全职 在线笔试 在职跳槽'),
    ('A three-token fragment of a SQL query with both ends missing. It attests only that the Akuna '
     'DataEng OA had a SQL component alongside the Java graph question — there is no recoverable '
     'question here at all, and it should be read as a section marker rather than content. ' + TRUNC),
    lang='en')

# ============================================================ Jane Street MLE, 2026-05
add('28634', '2026-05-30', 'Jane Street', 'unknown', 'experienced', '2026', 'phone_technical',
    'Jane Street MLE First Round, Coding',
    'the single coding question, with the worked example the poster reproduces',
    'editor_block_shrink_expand',
    ('写一个类似于 vscode 的 code editor，需要支持 block shrink and expandExample：Given:1 a = 12 + '
     'for i in range(10):3 print(i)4 print(i'),
    ('Write a code editor similar to VS Code, which must support block shrink and expand. Example: '
     'Given: 1 a = 1 / 2 + for i in range(10): / 3 print(i) / 4 print(i…'),
    ('First Round,Coding写一个类似于 vscode 的 code editor，需要支持 block shrink and expandExample：'
     'Given:1 a = 12 + for i in range(10):3 print(i)4 print(i'),
    ctx('#janestreet 码农类General@全职 技术电面 在职跳槽'),
    ('The task is stated clearly and the poster starts reproducing the worked example — the "+" on '
     'line 2 is the collapsed-block marker — but the preview truncates partway through it, and the '
     'example is what defines the expected behaviour. Line numbers and code have also been run '
     'together by the loss of the forum\'s line breaks, so "1 a = 12 + for i in range(10):" is really '
     'line 1 "a = 1" followed by line 2 "+ for i in range(10):". ' + TRUNC),
    lang='mixed')

# ============================================================ Optiver SWE phone, 2026-05
add('28643', '2026-05-30', 'Optiver', 'quant_developer', 'experienced', '2026', 'phone_technical',
    'Optiver SWE 电面 (phone screen)',
    'the coding question, which the poster stresses was not LeetCode-style',
    'concurrency_thread_safe_inventory',
    '让实现2个function来买和卖股票，要保证多线程下股票不能超卖（用lock）',
    ('They had me implement 2 functions to buy and sell stock, guaranteeing that under multithreading '
     'the stock cannot be oversold (using a lock).'),
    ('非leetcode. 让实现2个function来买和卖股票，要保证多线程下股票不能超卖（用lock）。我做出来了，'
     '但因为背景方向不match没进入下一轮。'),
    ctx('#optiver 码农类General@全职 技术电面 在职跳槽',
        'The poster adds that they solved it but were not advanced because their background did not '
        'match, and that Optiver 只收junior SWE (is only taking junior SWEs)'),
    ('Complete enough to attempt, and the constraint that matters (no overselling under concurrency, '
     'lock-based) is stated explicitly — the poster even volunteers 非leetcode to distinguish it from '
     'the usual. What is missing is the interface: how many shares, what the functions return on '
     'failure, whether blocking is allowed. This message is not truncated.'),
    lang='mixed')

# ============================================================ Jane Street phone, 2026-06
add('28689', '2026-06-04', 'Jane Street', 'quant_developer', 'experienced', '2026',
    'phone_technical', '简街店面 (Jane Street phone screen)',
    'the whole round as reported — a single sentence',
    'data_structure_ring_buffer',
    '设计环形缓存，时间复杂度不重要，功能完成就行',
    ('Design a ring buffer; time complexity does not matter, it just needs to work.'),
    '设计环形缓存，时间复杂度不重要，功能完成就行。求米！',
    ctx('#janestreet 码农类General@全职 技术电面 在职跳槽',
        'The entire post is this one line plus a request for karma (求米！)'),
    ('One sentence with no capacity, no element type and no statement of which operations were '
     'required, so this is the problem family rather than the problem. The explicit relaxation — '
     'complexity does not matter, just make it work — is the informative part and is the kind of aside '
     'a poster would not invent. Not truncated; the post really is this short.'),
    lang='mixed')

# ============================================================ Citadel EQR OA, 2026-06
add('28725', '2026-06-06', 'Citadel', 'quant_developer', 'experienced', '2026',
    'online_assessment', '城堡 EQR OA — three medium-difficulty questions',
    'all three questions, listed as bullets',
    'coding_trio_obfuscated_leetcode',
    ('三道medium[*]留斯奇: 但是注意最后要返回unique的子字符串[*]幺漆酒漆：比这道LC稍微简单一点，'
     'hashmap+list遍历[*]幺而丝雾：求树的直径的经典题'),
    ('Three mediums. [1] 留斯奇 (homophone-obfuscated LeetCode number): but note that at the end you '
     'must return unique substrings. [2] 幺漆酒漆: slightly easier than that LeetCode problem, '
     'hashmap + list traversal. [3] 幺而丝雾: the classic find-the-diameter-of-a-tree problem.'),
    ('三道medium[*]留斯奇: 但是注意最后要返回unique的子字符串[*]幺漆酒漆：比这道LC稍微简单一点，'
     'hashmap+list遍历[*]幺而丝雾：求树的直径的经典题'),
    ctx('#citadel 码农类General@全职 Onsite 在职跳槽 — note the round tag says Onsite but the title '
        'says OA'),
    ('All three problems are identified only by LeetCode numbers written in homophone-obfuscated '
     'digits (留斯奇, 幺漆酒漆, 幺而丝雾), which forum posters use to evade keyword search. I have '
     'deliberately not decoded them: guessing the numbers would amount to writing the questions '
     'myself. What survives unambiguously is the third one (tree diameter) and the modification on the '
     'first (return unique substrings). The round tag (Onsite) contradicts the title (OA), so the '
     'round on this record is taken from the title. This message is not truncated.'),
    lang='mixed')

# ============================================================ Citadel phone, 2026-06
add('28802', '2026-06-13', 'Citadel', 'quant_developer', 'experienced', '2026', 'phone_technical',
    'Citadel technical phone screen, Data Storage / Infra',
    'the structure of the coding hour',
    'assessment_format',
    '面试形式是 1 小时 coding，题目是 tree / data structure 相关，一共三问，难度逐',
    ('The format is 1 hour of coding; the question is tree / data-structure related, three parts in '
     'all, with difficulty progressi[vely…]'),
    ('分享一个 Citadel technical phone screen 面经，方向是 Data Storage / Infra 相关。面试形式是 1 '
     '小时 coding，题目是 tree / data structure 相关，一共三问，难度逐'),
    ctx('#citadel 码农类General@全职 技术电面 在职跳槽'),
    ('No question text at all — this describes the round (one hour, one tree/data-structure problem in '
     'three escalating parts, Data Storage/Infra team) and truncates at "难度逐" just as the poster '
     'was about to say the difficulty ramps up. Logged as a format datapoint. ' + TRUNC),
    lang='mixed')

# ============================================================ Citadel frontend, 2026-07
add('29074', '2026-07-27', 'Citadel', 'quant_developer', 'experienced', '2026', 'phone_technical',
    '城堡 前端面经 — a Citadel front-end interview',
    'the build task',
    'frontend_build_dashboard',
    'React 实现一个event feed dashboard,non AI assisted',
    'Implement an event feed dashboard in React, non-AI-assisted.',
    'React 实现一个event feed dashboard,non AI assisted 不难但是因为好久没手写代码了手生的很',
    ctx('#citadel 码农类General@全职 技术电面 在职跳槽',
        'The poster adds 不难但是因为好久没手写代码了手生的很 (not hard, but I am rusty from not '
        'having hand-written code in a long time) and part of the post is behind the karma wall'),
    ('One line: the framework, the artefact and the "non AI assisted" restriction, with no '
     'specification of what the dashboard had to do. The "non AI assisted" note is a specific and '
     'currently-topical detail that is unlikely to be invented. The rest of the post is hidden — the '
     'preview ends in the karma-wall placeholder. ' + KARMA),
    lang='mixed')

# ------------------------------------------------------------------ emit with verification
fails = []
out = []
for rec in R:
    mid = rec.pop('_mid')
    if rec['source_quote'] not in page_text(mid):
        fails.append((mid, rec['question_type'], rec['source_quote'][:70]))
        continue
    out.append(rec)

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as fh:
    for rec in out:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'appended {len(out)} records; {len(fails)} quote failures')
for f in fails:
    print('  FAIL', f, file=sys.stderr)
