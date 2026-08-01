#!/usr/bin/env python3
"""Full independent re-verification of raw/chat_and_archive.jsonl.

Covers every source_url shape used in the file, so no record escapes the quote check:
  t.me/<ch>/<id>            -> the saved single-message HTML page
  web.archive.org/.../1p3a  -> the saved Wayback snapshot (Discuz serves GB18030)
  1point3acres.com direct   -> either a saved snapshot or the verbatim WebSearch highlight file
  reddit.com/...            -> the Arctic Shift mirror snapshot (reddit.com itself 403s this box)
Anything with no local copy is reported, not silently passed.
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
_arctic = None


def arctic():
    global _arctic
    if _arctic is None:
        _arctic = (json.load(open('raw/pages/arctic/posts.json', encoding='utf-8')),
                   json.load(open('raw/pages/arctic/comments.json', encoding='utf-8')))
    return _arctic


def strip_html(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '\n', s)
    return html.unescape(s)


def read_maybe_gz(p, enc):
    d = open(p, 'rb').read()
    if d[:2] == b'\x1f\x8b':
        d = gzip.decompress(d)
    return d.decode(enc, errors='replace')


def tg(channel, mid):
    for p in (f'raw/pages/tgmsg/{mid}.html',
              f'raw/pages/tgmsg2/aistock_{mid}.html',
              f'raw/pages/tgmsg/{channel}_{mid}.html',
              f'raw/pages/tgmsg2/{channel}_{mid}.html'):
        if os.path.exists(p):
            raw = open(p, encoding='utf-8', errors='replace').read()
            return '\n'.join(strip_html(b) for b in TG_BLOCKS.findall(raw))
    return None


def highlight_blocks(key):
    """Return the RESULT blocks of the evidence files whose 'URL:' header names `key`.

    Matching on the URL header rather than anywhere in the block matters: the files open with
    a preamble that names every blocked URL, and a naive substring match would verify quotes
    against that prose instead of against the captured page text.
    """
    out = []
    for hp in ('raw/pages/websearch_highlights_1p3a.txt',
               'raw/pages/websearch_highlights_batch2.txt',
               'raw/pages/websearch_highlights_batch3.txt'):
        if not os.path.exists(hp):
            continue
        for block in open(hp, encoding='utf-8').read().split('=' * 80):
            for line in block.splitlines():
                if line.startswith('URL: ') and key in line:
                    out.append(block)
                    break
    return '\n'.join(out) if out else None


def local_text(url):
    if url in _cache:
        return _cache[url]
    txt = None

    m = re.match(r'https://t\.me/([A-Za-z0-9_]+)/(\d+)$', url)
    if m:
        txt = tg(m.group(1), m.group(2))

    m = re.match(r'https://web\.archive\.org/web/(\d+)/https?://(?:www\.)?1point3acres\.com/bbs/'
                 r'thread-(\d+)-1-1\.html$', url)
    if m and txt is None:
        ts, tid = m.groups()
        for p in (f'raw/pages/wayback/1p3a_{tid}__{ts}.html',
                  f'raw/pages/wayback/p3a_{tid}.html'):
            if os.path.exists(p):
                txt = strip_html(read_maybe_gz(p, 'gb18030'))
                break

    m = re.match(r'https://www\.1point3acres\.com/bbs/thread-(\d+)-1-1\.html$', url)
    if m and txt is None:
        tid = m.group(1)
        cands = [f'raw/pages/wayback/p3a_{tid}.html']
        cands += ['raw/pages/wayback/' + f for f in sorted(os.listdir('raw/pages/wayback'))
                  if f.startswith(f'1p3a_{tid}__')]
        for p in cands:
            if os.path.exists(p):
                txt = strip_html(read_maybe_gz(p, 'gb18030'))
                break
        if txt is None:
            txt = highlight_blocks(f'thread-{tid}-1-1.html')

    if txt is None and url.startswith('https://www.nowcoder.com/'):
        txt = highlight_blocks(url)

    m = re.match(r'https://www\.reddit\.com/r/[A-Za-z0-9_]+/comments/([a-z0-9]+)/[^/]*/'
                 r'([a-z0-9]+)/?$', url)
    if m and txt is None:
        posts, cmts = arctic()
        c = cmts.get(m.group(2))
        if c:
            txt = c.get('body') or ''
    m = re.match(r'https://www\.reddit\.com/r/[A-Za-z0-9_]+/comments/([a-z0-9]+)/[^/]*/?$', url)
    if m and txt is None:
        posts, cmts = arctic()
        p = posts.get(m.group(1))
        if p:
            txt = (p.get('title') or '') + '\n' + (p.get('selftext') or '')

    _cache[url] = txt
    return txt


def norm(s):
    return re.sub(r'\s+', '', s.replace('\u00a0', ' ').replace('\u200b', '')
                  .replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"'))


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
        if r.get('access') == 'screenshot_only':
            continue  # image transcription: no byte-verifiable text exists by definition
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
    for b in no_file[:15]:
        print('   ', b)
    print(f'QUOTE MISMATCHES:  {len(bad_quote)}')
    for b in bad_quote[:40]:
        print('   ', b)
    print()
    for k in ('source_type', 'access', 'retrieval_method', 'round', 'level', 'role_track'):
        print(f'{k}: {dict(Counter(r[k] for r in recs))}')
    print('firms:', dict(Counter(r['firm'] for r in recs).most_common()))
    print('distinct source_urls:', len({r['source_url'] for r in recs}))
    return 1 if (bad_schema or bad_vocab or bad_quote or no_file) else 0


if __name__ == '__main__':
    sys.exit(main())
