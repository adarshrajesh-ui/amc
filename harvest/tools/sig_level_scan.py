#!/usr/bin/env python3
"""Print, per target record, the cited Reddit comment plus everything else its author
said in that thread, and flag level-bearing language anywhere in the thread."""
import json
import os
import re
import sys

CACHE = '/workspace/harvest/.siglvl_cache'
SIGNAL = re.compile(
    r'(intern(ship)?s?\b|summer|penultimate|placement year|sophomore|junior\b|senior in|'
    r'undergrad|graduat|new.?grad|full.?time|\bFT\b|\bNG\b|campus|final year|'
    r'PhD|master|freshman|class of|20\d\d start|return offer|实习|暑期|校招|全职)', re.I)


def load(kind, tid):
    p = os.path.join(CACHE, f'{kind}_{tid}.json')
    if not os.path.exists(p):
        return []
    return json.load(open(p)).get('data') or []


def main():
    tgt = json.load(open('/tmp/sig_unknown.json'))
    want = {}
    for r in tgt:
        for a in r['attestations']:
            u = a['source_url']
            if 'reddit.com' not in u:
                continue
            m = re.search(r'/comments/([a-z0-9]+)/', u)
            if not m:
                continue
            tid = m.group(1)
            cm = re.search(r'/_/([a-z0-9]+)/?$', u)
            want.setdefault(tid, []).append((r['id'], cm.group(1) if cm else None))

    for tid, recs in want.items():
        posts = load('post', tid)
        cmts = load('cmts', tid)
        by_id = {c['id']: c for c in cmts}
        post = posts[0] if posts else {}
        print('=' * 100)
        print(f'THREAD {tid} | r/{post.get("subreddit")} | {post.get("title")}')
        print(f'  OP=u/{post.get("author")}  comments_fetched={len(cmts)}')
        optext = (post.get('selftext') or '')
        for m in SIGNAL.finditer(optext):
            print(f'   [OP-SIGNAL] ...{optext[max(0,m.start()-90):m.end()+90]}...'.replace('\n', ' '))
        for rid, cid in recs:
            print(f'  --- record {rid}  comment={cid}')
            c = by_id.get(cid) if cid else None
            if cid and not c:
                print('      (comment not in fetched page)')
            author = c.get('author') if c else post.get('author')
            if c:
                print(f'      AUTHOR u/{author}')
                print('      BODY:', (c.get('body') or '').replace('\n', ' ')[:800])
            # everything else this author said in the thread
            for o in cmts:
                if o.get('author') == author and (not c or o['id'] != c['id']):
                    b = (o.get('body') or '').replace('\n', ' ')
                    print(f'      ALSO[{o["id"]}]:', b[:500])
        # thread-wide level signals
        print('  --- thread-wide signals:')
        for c in cmts:
            b = c.get('body') or ''
            for m in SIGNAL.finditer(b):
                print(f'      u/{c.get("author")} [{c["id"]}]: ...'
                      f'{b[max(0,m.start()-90):m.end()+90]}...'.replace('\n', ' '))
                break


if __name__ == '__main__':
    main()
