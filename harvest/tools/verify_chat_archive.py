#!/usr/bin/env python3
"""Independent re-verification of /workspace/harvest/raw/chat_and_archive.jsonl.

Re-derives the local copy of each source_url from scratch and checks the source_quote
against it, so a bug in any one builder cannot pass unnoticed. Also enforces the
controlled vocabularies and the required field set.
"""
import gzip
import html
import json
import os
import re
import sys
from collections import Counter

JSONL = 'raw/chat_and_archive.jsonl'
FIELDS = ['firm', 'role_track', 'level', 'cycle', 'office', 'round', 'round_name', 'platform',
          'section_context', 'question_type', 'question_text', 'question_text_en',
          'reported_answer', 'source_url', 'source_type', 'source_quote', 'source_language',
          'post_date', 'access', 'retrieval_method', 'upstream_source', 'poster_context', 'doubt']
ROLE = {'quant_trader', 'quant_researcher', 'quant_developer', 'quant_analyst', 'data_scientist',
        'unknown'}
LEVEL = {'internship', 'new_grad', 'experienced', 'unknown'}
ROUND = {'online_assessment', 'math_sequences_test', 'phone_technical', 'superday', 'onsite',
         'trading_game', 'take_home', 'datathon', 'unknown'}
STYPE = {'chat_discord', 'chat_telegram', 'chat_qq_repost', 'chat_wechat_repost', 'chat_slack',
         'reddit_thread', 'tieba', 'douban', 'nowcoder', 'yuque', 'blog', 'other'}
ACCESS = {'full_text', 'snippet_only', 'archive_only', 'screenshot_only', 'compilation_only'}
METHOD = {'webfetch', 'websearch_snippet', 'wayback'}
LANG = {'en', 'zh', 'mixed'}

TG_BLOCKS = re.compile(
    r'<div class="(?:tgme_widget_message_text[^"]*|link_preview_title|link_preview_description)"'
    r'[^>]*>(.*?)</div>', re.S)

_cache = {}


def strip_html(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '\n', s)
    return html.unescape(s)


def local_text(url):
    if url in _cache:
        return _cache[url]
    txt = None
    m = re.match(r'https://t\.me/usinterview/(\d+)$', url)
    if m:
        p = f'raw/pages/tgmsg/{m.group(1)}.html'
        if os.path.exists(p):
            raw = open(p, encoding='utf-8', errors='replace').read()
            txt = '\n'.join(strip_html(b) for b in TG_BLOCKS.findall(raw))
    m = re.match(r'https://t\.me/aistockanalyst/(\d+)$', url)
    if m:
        p = f'raw/pages/tgmsg2/aistock_{m.group(1)}.html'
        if os.path.exists(p):
            raw = open(p, encoding='utf-8', errors='replace').read()
            txt = '\n'.join(strip_html(b) for b in TG_BLOCKS.findall(raw))
    m = re.match(r'https://web\.archive\.org/web/(\d+)/https://www\.1point3acres\.com/bbs/'
                 r'thread-(\d+)-1-1\.html$', url)
    if m:
        ts, tid = m.groups()
        p = f'raw/pages/wayback/1p3a_{tid}__{ts}.html'
        if os.path.exists(p):
            d = open(p, 'rb').read()
            if d[:2] == b'\x1f\x8b':
                d = gzip.decompress(d)
            txt = strip_html(d.decode('gb18030', errors='replace'))
    _cache[url] = txt
    return txt


def norm(s):
    return re.sub(r'\s+', '', s.replace('\u00a0', ' ').replace('\u200b', ''))


def main():
    recs = [json.loads(l) for l in open(JSONL, encoding='utf-8')]
    bad_schema, bad_vocab, no_file, bad_quote = [], [], [], []
    for i, r in enumerate(recs, 1):
        if set(r) != set(FIELDS):
            bad_schema.append((i, sorted(set(FIELDS) ^ set(r))))
        for k, allowed in (('role_track', ROLE), ('level', LEVEL), ('round', ROUND),
                           ('source_type', STYPE), ('access', ACCESS),
                           ('retrieval_method', METHOD), ('source_language', LANG)):
            if r.get(k) not in allowed:
                bad_vocab.append((i, k, r.get(k)))
        for k in ('doubt', 'source_quote', 'question_text', 'source_url'):
            if not (r.get(k) or '').strip():
                bad_schema.append((i, f'empty {k}'))
        txt = local_text(r['source_url'])
        if txt is None:
            no_file.append((i, r['source_url']))
            continue
        if norm(r['source_quote']) not in norm(txt):
            bad_quote.append((i, r['firm'], r['source_url'], r['source_quote'][:70]))

    print(f'records: {len(recs)}')
    print(f'schema problems:   {len(bad_schema)}')
    for b in bad_schema[:10]:
        print('   ', b)
    print(f'vocabulary problems: {len(bad_vocab)}')
    for b in bad_vocab[:10]:
        print('   ', b)
    print(f'no local copy of source: {len(no_file)}')
    for b in no_file[:10]:
        print('   ', b)
    print(f'QUOTE MISMATCHES:  {len(bad_quote)}')
    for b in bad_quote:
        print('   ', b)
    print()
    for k in ('source_type', 'access', 'retrieval_method', 'round', 'level', 'role_track'):
        print(f'{k}: {dict(Counter(r[k] for r in recs))}')
    print('firms:', dict(Counter(r['firm'] for r in recs).most_common()))
    print('distinct source_urls:', len({r['source_url'] for r in recs}))
    return 1 if (bad_schema or bad_vocab or bad_quote or no_file) else 0


if __name__ == '__main__':
    sys.exit(main())
