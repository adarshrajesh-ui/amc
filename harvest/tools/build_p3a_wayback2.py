#!/usr/bin/env python3
"""Second Wayback/1point3acres batch — Jane Street onsite and HRT round 1."""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p3a_extract2 import load  # noqa: E402

SNAP = {
    '1145993': ('20251010155502', '1p3a_1145993__20251010155502.html'),
    '1145403': ('20251011032412', '1p3a_1145403__20251011032412.html'),
}
_c = {}


def page_text(tid):
    if tid not in _c:
        s = load(os.path.join('raw/pages/wayback', SNAP[tid][1]))
        s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
        s = re.sub(r'<br\s*/?>', '\n', s)
        s = re.sub(r'<[^>]+>', '\n', s)
        s = html.unescape(s)
        s = re.sub(r'[ \t\u00a0]+', ' ', s)
        _c[tid] = re.sub(r'\n+', '\n', s)
    return _c[tid]


P3A = ('1point3acres 海外面经版 recall thread, recovered from a Wayback Machine snapshot because '
       '1point3acres itself Cloudflare-blocks this machine')
WALL = '本帖隐藏的内容需要积分高于 188 才可浏览 (the forum\'s 188-karma wall)'

R = []


def add(tid, **kw):
    ts = SNAP[tid][0]
    kw['_tid'] = tid
    kw.setdefault('source_url',
                  f'https://web.archive.org/web/{ts}/https://www.1point3acres.com/bbs/thread-{tid}-1-1.html')
    kw.setdefault('source_type', 'other')
    kw.setdefault('access', 'archive_only')
    kw.setdefault('retrieval_method', 'wayback')
    kw.setdefault('upstream_source', None)
    kw.setdefault('platform', 'unknown')
    kw.setdefault('reported_answer', None)
    R.append(kw)


add('1145993',
    firm='Jane Street', role_track='quant_developer', level='experienced', cycle='2025',
    office='unknown', round='onsite',
    round_name='Jane Street onsite — the poster says this was the only question asked',
    section_context='the sole onsite coding question, given with a worked example and a Python stub',
    question_type='coding_diff_merge',
    question_text=('merge diffs:\n\n{0: A, 3: B} + {0: C, 4: D}\n\norig:\n\n{0: z, 1: z, 2: z}\n\n'
                   'new:\n\n{0: C, 1: A, 2: z, 3: z, 4: D, 5: B, 6: z}\n\n"""\n\n'
                   'def merge_diffs(diff_one, diff_two):\n\n… [karma wall] …\n\n'
                   'ong> merge(self, diff_one, start, end):\n\n        pass'),
    question_text_en=('Merge diffs. Example: {0: A, 3: B} + {0: C, 4: D}; original {0: z, 1: z, '
                      '2: z}; new {0: C, 1: A, 2: z, 3: z, 4: D, 5: B, 6: z}. Implement '
                      'def merge_diffs(diff_one, diff_two). A second stub visible below the karma '
                      'wall reads "...merge(self, diff_one, start, end): pass".'),
    source_quote=('上个月考了Jane street的on-site，这是唯一一个题目，merge diffs:\n'
                  '{0: A, 3: B} + {0: C, 4: D}\norig:\n{0: z, 1: z, 2: z}\nnew:\n'
                  '{0: C, 1: A, 2: z, 3: z, 4: D, 5: B, 6: z}'),
    source_language='mixed', post_date='2025-09',
    poster_context=(P3A + '; forum metadata tags the post 工程类@全职 Onsite 在职跳槽 (engineering, '
                    'full-time, experienced hire). The poster states this was the only question in '
                    'the entire onsite'),
    doubt=('This is the strongest Jane Street record in the shard because it reproduces the '
           'assessment\'s own worked example and function signature rather than a paraphrase — but '
           'the prose explaining what a "diff" means and how the two are to be combined is behind '
           f'{WALL}, and a replier on the same thread says exactly that: "这题规则是什么意思，可以求'
           '题主在解释一下嘛" (what do the rules of this problem mean, could the OP explain again). '
           'So the semantics that make the worked example make sense are missing, and my own '
           'reading of the example is not asserted here. The second stub is also mangled by the '
           'wall markup ("ong> merge(self, ...)"), so the class it belongs to is unknown.'))

add('1145403',
    firm='HRT', role_track='quant_developer', level='experienced', cycle='2025', office='unknown',
    round='phone_technical',
    round_name='HRT 一面 (first round) for an Algorithm Engineer role',
    section_context='the single coding question in round 1',
    question_type='coding_simulation',
    question_text='问了一个题\n\n写Word[le]',
    question_text_en='They asked one question: write Word[le].',
    source_quote='问了一个题\n写Word',
    source_language='zh', post_date='2025-09-13',
    poster_context=(P3A + '; forum metadata tags the post 金工类@全职 视频面试 在职跳槽 (quant track, '
                    'full-time, experienced hire). In a reply the poster says '
                    '"面的是algorithm engineer岗，感觉比较偏sde" — the role is Algorithm Engineer and '
                    'feels closer to SDE — and gives the pipeline as one coding round, one '
                    'non-coding technical round, then onsite'),
    doubt=('The snapshot is truncated by the karma wall in the middle of the word "Wordle" — the '
           'page literally ends at "写Word" — so the specification, interface and constraints are '
           'entirely absent. What makes it worth keeping is the cross-corroboration: the same '
           'candidate\'s post also reached Telegram (t.me/usinterview/25282), and a separate '
           'candidate reported a Wordle problem in HRT\'s phone screen six months earlier '
           '(1point3acres thread 1120333). A replier here pushes back — "奇怪，rd1不是考概率吗，怎么'
           'wordle都出来了" (odd, isn\'t round 1 meant to be probability? how has Wordle turned up) '
           '— which is evidence that HRT\'s round 1 is not uniform across candidates.'))

missing, out = [], []
for rec in R:
    tid = rec.pop('_tid')
    txt = page_text(tid).replace('\u00a0', ' ')
    q = rec['source_quote'].replace('\u00a0', ' ')
    if q in txt or re.sub(r'\s+', '', q) in re.sub(r'\s+', '', txt):
        out.append(rec)
    else:
        missing.append((tid, rec['firm'], q[:80]))

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
