#!/usr/bin/env python3
"""Sixth @usinterview batch — a targeted sweep for the firms thinnest in the corpus
(Two Sigma, Jane Street, Five Rings, DRW, IMC) plus the firms that co-occur with them.
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
TRUNC = ('The Telegram link preview is cut off at a fixed length and visibly ends in "…", so only '
         'the opening of the recall is readable. 1point3acres Cloudflare-blocks this machine and '
         'the Wayback Machine has no 200 snapshot of this thread, so the rest is unrecoverable')

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


def ctx(tags, extra=''):
    return TG + f'. Forum tags: {tags}' + (f'. {extra}' if extra else '')


# ======================================================= CITADEL onsite, with real code
CIT = dict(mid='14353', date='2022-08-18', firm='Citadel', role='quant_developer',
           level='experienced', cycle='2023', rnd='onsite',
           rname='Citadel onsite for a senior developer role',
           poster=ctx('#Chicagotrading 码农类General@全职 Onsite 在职跳槽 — the forum hashtag is '
                      'Chicago Trading Company, but the thread title covers three firms: '
                      '[求米][CTC][Citadel][Millennium] senior developer 面经',
                      'The poster numbers the Citadel onsite questions 1), 2), 3) …'))
CIT_DOUBT = (
    'The thread bundles three employers (CTC, Citadel and Millennium) into one write-up and is '
    'hashtagged for a fourth-party board, so there is some risk of the poster mis-filing which '
    'question came from which firm — though these two are explicitly introduced by the heading '
    '"Citadel Onsite：". The preview cuts off at "3）", so the list is incomplete. ' + TRUNC)

add(**CIT, section='question 1 of the numbered onsite list',
    qtype='counting_dp_staircase',
    qtext='1) 爬楼梯， 每次可以1/2/3步， 多少种爬法',
    qtext_en=('1) Climbing stairs, where each step may be 1, 2 or 3 steps — how many ways are '
              'there to climb?'),
    quote='Citadel Onsite：1) 爬楼梯， 每次可以1/2/3步， 多少种爬法',
    doubt=('The number of stairs is not given, so this is the problem family rather than an '
           'instance — presumably n was supplied verbally. ' + CIT_DOUBT),
    lang='mixed')

add(**CIT, section='question 2 of the numbered onsite list',
    qtype='language_cpp_implicit_conversion',
    qtext=('2) C++ 函数 void func(int8_t i);void main() { int32_t x = 1; func(x); }会发生什么 ？'),
    qtext_en=('2) A C++ function void func(int8_t i); void main() { int32_t x = 1; func(x); } — '
              'what happens?'),
    quote=('2) C++ 函数 void func(int8_t i);void main() { int32_t x = 1; func(x); }会发生什么 ？'),
    doubt=('This one reproduces the actual code the candidate was shown, which is rare in this '
           'shard and makes it the strongest item in the message. The only gap is that the '
           'follow-up — whether the interviewer wanted the narrow-conversion rule, the value for '
           'x=1 specifically, or what happens for larger x — is not recorded. ' + CIT_DOUBT),
    lang='mixed')

# ======================================================= TWO SIGMA OA — the recurring pair
TS_BANK = (
    'Two Sigma\'s code test is visibly a fixed bank: four independent posters here — '
    't.me/usinterview/14767 (2022), 14905 (2022), 25390 (2025) and 27708 (2026) — name the same '
    'problems, and three of them use the same nicknames "IPO" and "下水道" (sewer). That '
    'cross-corroboration across four years is the main reason to believe these reports')

add('14767', '2022-09-26', 'Two Sigma', 'quant_developer', 'new_grad', '2023',
    'online_assessment',
    'Two Sigma code test, obtained through the Grace Hopper Celebration',
    'the first of the two problems',
    'coding_auction_allocation',
    '第一题IPO求没有分到shares的bidder，输出的时候忘记转成list导致有3个test没过',
    ('Question 1, IPO: find the bidders who were not allocated any shares. When outputting I '
     'forgot to convert to a list, which caused 3 tests to fail.'),
    '第一题IPO求没有分到shares的bidder，输出的时候忘记转成list导致有3个test没过',
    ctx('#TwoSigma 码农类General@全职 在线笔试 在职跳槽',
        'The poster says they got the code test via GHC and calls both problems "地里老题目" (old '
        'questions already on the forum)'),
    ('The allocation rule — which is the entire problem — is not stated: how bids are ranked, how '
     'ties at the same price are broken and how the share pool is exhausted are all missing. A '
     'later poster (t.me/usinterview/27708) fills part of this in independently, saying you sort '
     'first, then group, then round-robin within each equal-price band using timestamps; I have '
     'kept that in that record rather than importing it here. ' + TS_BANK + '. ' + TRUNC),
    lang='mixed')

add('14767', '2022-09-26', 'Two Sigma', 'quant_developer', 'new_grad', '2023',
    'online_assessment',
    'Two Sigma code test, obtained through the Grace Hopper Celebration',
    'the second of the two problems',
    'coding_tree_construction',
    '第二题sewer tree structure，构建一个TreeNode',
    'Question 2, sewer tree structure: build a TreeNode.',
    '第二题sewer tree structure，构建一个TreeNode',
    ctx('#TwoSigma 码农类General@全职 在线笔试 在职跳槽'),
    ('Eight words. The input format, what the tree represents and what has to be returned are all '
     'absent — "build a TreeNode" is not a specification. Its worth is as the earliest dated '
     'attestation of the problem that three later posters call 下水道 (sewer). ' + TS_BANK + '. ' +
     TRUNC),
    lang='mixed')

add('25390', '2025-09-19', 'Two Sigma', 'quant_developer', 'experienced', '2026',
    'phone_technical',
    'Two Sigma tech screen, following the OA',
    'the tech-screen implementation task',
    'coding_hashmap_from_scratch',
    'Tech screen：从头implement一个hashmap，不能用任何自带的hashtale lib。实现两个',
    ('Tech screen: implement a hashmap from scratch, without using any built-in hashtable library. '
     'Implement two …'),
    'Tech screen：从头implement一个hashmap，不能用任何自带的hashtale lib。实现两个',
    ctx('#twosigma 码农类General@全职 技术电面 在职跳槽',
        'The same message gives the OA as "IPO + 下水道" and links a sibling forum thread'),
    ('The preview is cut off at "实现两个" (implement two …), exactly where the two required '
     'methods would have been named, so which operations the hashmap had to support is unknown. '
     'The constraint that no built-in hashtable library may be used is clear and is the '
     'substantive part. ' + TRUNC),
    lang='mixed')

add('27708', '2026-03-25', 'Two Sigma', 'quant_developer', 'experienced', '2026',
    'online_assessment',
    'Two Sigma OA — the poster says every question was already circulating on the forum',
    'the IPO problem, described with the poster\'s own solution approach',
    'coding_auction_allocation',
    ('楼主遇到了ipo 和 下水道，原题到处都搜得到ipo比较麻烦，我参考了hack2hire里面的解法，先排序再分组'
     '，同价区做round-robin，一开始忘了同价组用timest'),
    ('I got IPO and sewer; the originals can be found everywhere. IPO is the fiddlier one — I '
     'followed the solution from hack2hire: sort first, then group, do round-robin within the '
     'equal-price band; at first I forgot that the equal-price group uses timest[amps] …'),
    ('楼主遇到了ipo 和 下水道，原题到处都搜得到ipo比较麻烦，我参考了hack2hire里面的解法，先排序再分组'
     '，同价区做round-robin，一开始忘了同价组用timest'),
    ctx('#twosigma 码农类General@全职 Onsite 在职跳槽 — note the round tag says Onsite while the '
        'title and body describe an OA'),
    ('What is recorded is the poster\'s solution recipe, not the problem statement, and they say '
     'outright that they took it from "hack2hire" — a third-party prep site — rather than deriving '
     'it, so this is a description of an answer circulating online rather than independent '
     'evidence of the question. The preview also breaks mid-word at "timest". It is kept because '
     'the sort/group/round-robin-by-timestamp detail is a concrete constraint that no other poster '
     'in this shard supplies, and because it corroborates the IPO problem four years after the '
     'first sighting. ' + TS_BANK + '. ' + TRUNC),
    lang='mixed')

TS23 = dict(mid='23803', date='2025-06-21', firm='Two Sigma', role='quant_researcher',
            level='experienced', cycle='2025', rnd='online_assessment',
            rname='Two Sigma 2025 OA for a quant role',
            poster=ctx('#twosigma 金工类@全职 在线笔试 在职跳槽 — quant track, full-time, online '
                       'written test, experienced hire'))
TS23_DOUBT = ('The poster lists the three problems in a single unpunctuated run and gives topic '
              'labels rather than statements, so no input format, no constraints and no required '
              'output are recoverable for any of them. The preview also cuts off in the middle of '
              'the third. ' + TRUNC)

add(**TS23, section='the first of three problems on the quant OA',
    qtype='coding_linear_interpolation',
    qtext='第一题还是经典的Linear Interpolation，注意有重复数据的edge case',
    qtext_en=('Question 1 is still the classic Linear Interpolation — watch out for the '
              'duplicate-data edge case.'),
    quote='第一题还是经典的Linear Interpolation，注意有重复数据的edge case',
    doubt=('The duplicate-data edge case the poster flags is the one genuinely informative detail; '
           'what is being interpolated, and over what, is not said. ' + TS23_DOUBT),
    lang='mixed')

add(**TS23, section='the second of three problems on the quant OA',
    qtype='data_analysis_descriptive_and_regression',
    qtext='第二题是NYC temp dataset，简单的median，variance和regression',
    qtext_en=('Question 2 is the NYC temperature dataset — simple median, variance and '
              'regression.'),
    quote='第二题是NYC temp dataset，简单的median，variance和regression',
    doubt=('Names a dataset (NYC temperatures) and three statistics, but not what was to be '
           'regressed on what, nor over what period. ' + TS23_DOUBT),
    lang='mixed')

add(**TS23, section='the third, bonus problem on the quant OA',
    qtype='linear_algebra_computation',
    qtext='第三题bonus是matrix计算相关的再改',
    qtext_en='Question 3, a bonus, is matrix-computation related, modified again.',
    quote='第三题bonus是matrix计算相关的再改',
    doubt=('The least informative of the three — "matrix-computation related" with the sentence '
           'then cut off mid-thought. Recorded only to register that the 2025 quant OA had a third '
           'bonus item of this kind. ' + TS23_DOUBT),
    lang='mixed')

add('18407', '2024-05-21', 'Two Sigma', 'quant_researcher', 'experienced', '2024',
    'online_assessment', 'Two Sigma OA — the poster\'s third attempt at the same test',
    'the format of the test',
    'coding_recycled_bank',
    'OA 180min 还是地里那三道原题',
    'OA, 180 minutes, still the same three original questions that are on the forum.',
    'OA 180min 还是地里那三道原题',
    ctx('#twosigma 金工类@全职 在线笔试 在职跳槽',
        'The thread is titled "怎么都过不了OA系列" (the can-never-pass-the-OA series); the poster '
        'says this is their third time taking Two Sigma\'s OA, that all cases passed each time, '
        'and that HR still said the code test score was below the bar'),
    ('No question content at all — this is format plus a complaint. It earns its place as evidence '
     'about the bank rather than about any question: an independent poster stating that the same '
     'three problems recurred across three sittings, in 180 minutes, which is what the other Two '
     'Sigma records in this batch imply. Passing all visible test cases and still failing on '
     '"code test score" suggests hidden tests or a style/efficiency component, though the poster '
     'does not say so. ' + TRUNC),
    lang='mixed')

# ======================================================= JANE STREET
add('24502', '2025-08-01', 'Jane Street', 'quant_developer', 'experienced', '2026',
    'phone_technical',
    'Jane Street MLE 店面 (phone screen) — first round, an SWE interview',
    'the first-round coding problem',
    'coding_interpreter_implementation',
    ('第一轮swe面试，告诉一种特殊的很简易的编程语言，用你擅长的语言编译实现，之后有些OOD感觉的'
     'followup'),
    ('Round 1, an SWE interview: they describe a special, very simple programming language, and '
     'you implement/compile it in a language you are good at; then there are some follow-ups with '
     'an object-oriented-design feel.'),
    ('第一轮swe面试，告诉一种特殊的很简易的编程语言，用你擅长的语言编译实现，之后有些OOD感觉的'
     'followup'),
    ctx('#janestreet MachineLearningEng@全职 技术电面 在职跳槽 — the thread title 简洁MLE店面挂经 '
        'uses 简洁 as a homophone for 简街, the usual Chinese nickname for Jane Street',
        'The poster notes a recruiter reached out and that the interviews did not require running '
        'code — "api记不清可以hallucinate" (if you cannot remember an API you may hallucinate it)'),
    ('The grammar of the "special, very simple programming language" is not given, and that is the '
     'question — without it there is nothing to implement. Whether the task was an interpreter or '
     'a compiler is also ambiguous in the Chinese ("编译实现"). The follow-ups are characterised '
     'only by feel. ' + TRUNC),
    lang='mixed')

add('27088', '2026-02-01', 'Jane Street', 'quant_developer', 'new_grad', 'unknown',
    'phone_technical', 'Jane Street phone interview',
    'the problem, quoted as far as the preview reaches',
    'coding_timeseries_matrix_alignment',
    ('当年校招的题给定一组 M 个 code 和 N 个时间节点，一个理想的数据形态是是一个 N x M 的 matrix，'
     '纵向数据按时间排序，横向数据按照 c'),
    ('The question from campus recruiting back then: given a set of M codes and N time points, the '
     'ideal shape of the data is an N x M matrix, with the vertical data sorted by time and the '
     'horizontal data by c…'),
    ('当年校招的题给定一组 M 个 code 和 N 个时间节点，一个理想的数据形态是是一个 N x M 的 matrix，'
     '纵向数据按时间排序，横向数据按照 c'),
    ctx('#janestreet 码农类General@全职 技术电面 在职跳槽',
        'The poster opens "陈年题了发上来分享一下！" (an old question, posting it to share) and '
        'says it was from campus recruiting "当年" (back in that year)'),
    ('Two problems. First, the preview is severed mid-word at "按照 c", right where the column '
     'ordering was being defined, and the task itself — what to do with the data once the ideal '
     'matrix shape is described — never appears. Second, the poster says openly that this is a '
     '陈年题, an old question from their campus-recruiting year, and gives no year, so the cycle '
     'is unknown and the recall is years old. ' + TRUNC),
    lang='mixed')

# ======================================================= verify + emit
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
        bad.append((mid, rec['firm'], rec['source_quote'][:70]))

for b in bad:
    sys.stderr.write(f'QUOTE NOT FOUND: {b}\n')

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in ok:
        f.write(json.dumps({k: rec[k] for k in ORDER}, ensure_ascii=False) + '\n')
print(f'verified+written={len(ok)}  failed={len(bad)}')
