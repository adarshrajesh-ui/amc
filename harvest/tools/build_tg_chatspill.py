#!/usr/bin/env python3
"""Records from @aistockanalyst — a Telegram channel that reposts Chinese-language
quant-careers group chat dumps (speaker-tagged 【Alice】/【Bob】 turns, the signature of
a QQ/WeChat 群 transcript pasted onward).
"""
import html
import json
import os
import re
import sys

PAGES = 'raw/pages/tgmsg2'
TEXT = re.compile(r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', re.S)


def page_text(name: str) -> str:
    raw = open(os.path.join(PAGES, f'{name}.html'), encoding='utf-8', errors='replace').read()
    parts = []
    for body in TEXT.findall(raw):
        t = re.sub(r'<br\s*/?>', '\n', body)
        t = re.sub(r'<[^>]+>', '', t)
        parts.append(html.unescape(t))
    return '\n'.join(parts)


COMMON = {
    'source_type': 'chat_wechat_repost',
    'access': 'full_text',
    'retrieval_method': 'webfetch',
    'source_language': 'zh',
    'office': 'China (mainland campus recruiting)',
    'platform': 'unknown',
    'reported_answer': None,
}

SPILL = ('Reposted into the public Telegram channel @aistockanalyst. The message is formatted as '
         'speaker-tagged turns (【Alice】 / 【Bob】), i.e. it is a transcript of a Chinese-language '
         'group chat (QQ 群 / 微信群) pasted onward; the chat itself is not readable from here')

R = []


def add(msg, date, firm, role, level, cycle, rnd, rname, section, qtype, qtext, qtext_en,
        quote, poster, doubt):
    R.append(dict(firm=firm, role_track=role, level=level, cycle=cycle,
                  round=rnd, round_name=rname, section_context=section, question_type=qtype,
                  question_text=qtext, question_text_en=qtext_en,
                  source_url=f'https://t.me/aistockanalyst/{msg}', source_quote=quote,
                  post_date=date, upstream_source=SPILL, poster_context=poster, doubt=doubt,
                  **COMMON))
    R[-1]['_p'] = f'aistock_{msg}'


add(1288, '2026-06-16',
    '孝庸基金 (unidentified Chinese fund, name written in homophone-obfuscated form)',
    'quant_researcher', 'unknown', 'unknown', 'online_assessment',
    '笔试 (written test) for a 量化岗 (quant role)',
    'the opening line of the pasted group-chat transcript',
    'coding_game_simulation',
    '孝庸基金量化岗笔试题是敲代码，坦克大战',
    'The written test for the quant role at [孝庸] Fund is a coding task: Tank Battle.',
    '孝庸基金量化岗笔试题是敲代码，坦克大战',
    'a participant in a Chinese quant-careers group chat answering someone about written tests',
    'The firm name 孝庸基金 is almost certainly a deliberate homophone substitution — a convention '
    'Chinese posters use to keep firm names out of search indexes — and I have not decoded it, so '
    'the employer is effectively unidentified and is NOT one of the named target firms. The '
    '"question" is a four-character label ("坦克大战", Tank Battle) with no spec, rules, interface or '
    'time limit. Its only real value is as evidence of the format: a domestic Chinese fund using a '
    'game-implementation coding task as its quant written test.')

add(1288, '2026-06-16',
    'zd (unidentified Chinese fund, referred to only by initials)',
    'quant_researcher', 'internship', 'unknown', 'take_home',
    'QR take-home project',
    'a group-chat participant relaying what a fellow intern encountered',
    'orderbook_reconstruction',
    '之前一个一起实习的同学去面过zd的qr岗，给的是一个project，给定entrust和trade的数据，撮合出最细颗粒度的ob，错误率不得高于4%',
    'A classmate I interned with previously interviewed for the QR role at [zd]; they were given a '
    'project: given entrust (order) and trade data, match them to reconstruct the finest-granularity '
    'order book, with an error rate no higher than 4%.',
    '之前一个一起实习的同学去面过zd的qr岗，给的是一个project，给定entrust和trade的数据，撮合出最细颗粒度的ob，错误率不得高于4%（其实感觉要么全对要么错一大堆hh，而且qr要求撮订单簿就很离谱）',
    'a participant in a Chinese quant-careers group chat describing a task given to a friend',
    'SECOND-HAND: the speaker did not sit this assessment — they are relaying what a fellow intern '
    'was given ("之前一个一起实习的同学"). The firm is named only as "zd", which I have not decoded '
    'and will not guess at, and it is not one of the named target firms. The 4% error-rate '
    'threshold and the entrust/trade → order-book reconstruction task are unusually concrete for a '
    'chat relay, which is what makes it worth keeping, but the speaker themself calls the '
    'requirement absurd, so their rendering of it may be distorted.')

add(951, '2025-07-26',
    'unnamed foreign (外资) quant firm recruiting at Tsinghua/Peking University',
    'quant_researcher', 'new_grad', 'unknown', 'onsite',
    'campus-recruiting technical interview conducted in Chinese',
    'the speaker recalling questions they were personally asked',
    'physics_open_question',
    '解释一下Kerr黑洞是什么；解释一下EPR悖论',
    'Explain what a Kerr black hole is; explain the EPR paradox.',
    '面试时有机会遇到千奇百怪的问题，例如我自己就被问过：「解释一下Kerr黑洞是什么；解释一下EPR悖论」等千奇百怪的东西，这些随缘就行。',
    'someone who says they run a quant firm\'s campus recruiting at Tsinghua and Peking University, '
    'recalling questions they were themselves asked as a candidate',
    'The firm is never named — the speaker says only that it was a 外资 (foreign-invested) firm '
    'recruiting on Chinese campuses — so this cannot be attributed to any target firm. The two '
    'questions are quoted inside 「」 as things the speaker was personally asked, which is '
    'first-hand, but they are offered as examples of "千奇百怪" (weird and wonderful) one-offs, not '
    'as a standard item. Note also this message is one long essay-style post; it reads like curated '
    'career advice that may itself have been copied from elsewhere before reaching Telegram.')

missing, out = [], []
for rec in R:
    p = rec.pop('_p')
    txt = page_text(p).replace('\u00a0', ' ')
    q = rec['source_quote'].replace('\u00a0', ' ')
    if q in txt or re.sub(r'\s+', '', q) in re.sub(r'\s+', '', txt):
        out.append(rec)
    else:
        missing.append((p, q[:70]))

for m in missing:
    sys.stderr.write(f'QUOTE NOT FOUND: {m}\n')

order = ['firm', 'role_track', 'level', 'cycle', 'office', 'round', 'round_name', 'platform',
         'section_context', 'question_type', 'question_text', 'question_text_en', 'reported_answer',
         'source_url', 'source_type', 'source_quote', 'source_language', 'post_date', 'access',
         'retrieval_method', 'upstream_source', 'poster_context', 'doubt']
with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in out:
        f.write(json.dumps({k: rec[k] for k in order}, ensure_ascii=False) + '\n')
print(f'verified+written={len(out)}  failed={len(missing)}')
