#!/usr/bin/env python3
"""Step 1: map every reddit_thread attestation to the account that actually wrote it.

The stored poster_context names an account, but that is the harvester's own claim;
we re-derive the author from the mirror so a wrong or invented attribution shows up.
"""
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, '/workspace/harvest/tools')
from screen_lib import get, parse_url

rows = [json.loads(l) for l in open('/workspace/harvest/questions.jsonl')]
sel = [r for r in rows if any(a.get('source_type') == 'reddit_thread' for a in r.get('attestations', []))]

# unique (post_id, comment_id) targets
targets = {}
for r in sel:
    for a in r['attestations']:
        if a.get('source_type') != 'reddit_thread':
            continue
        pid, cid = parse_url(a['source_url'])
        targets.setdefault((pid, cid), []).append((r['id'], a['source_url']))

print('clusters=%d  unique url targets=%d' % (len(sel), len(targets)), flush=True)

post_ids = sorted({p for p, c in targets if p})
cmt_ids = sorted({c for p, c in targets if c})


def chunks(xs, n):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


posts, cmts = {}, {}


def fetch_posts(ch):
    d = get('posts/ids', ids=','.join(ch)) or []
    return d


def fetch_cmts(ch):
    d = get('comments/ids', ids=','.join(ch)) or []
    return d


with ThreadPoolExecutor(max_workers=4) as ex:
    for d in ex.map(fetch_posts, list(chunks(post_ids, 20))):
        for x in d:
            posts[x['id']] = x
    for d in ex.map(fetch_cmts, list(chunks(cmt_ids, 20))):
        for x in d:
            cmts[x['id']] = x

print('resolved posts=%d/%d  comments=%d/%d' % (len(posts), len(post_ids), len(cmts), len(cmt_ids)), flush=True)

out = []
for (pid, cid), refs in sorted(targets.items(), key=lambda kv: str(kv[0])):
    obj = cmts.get(cid) if cid else posts.get(pid)
    parent = posts.get(pid)
    rec = {
        'post_id': pid, 'comment_id': cid,
        'kind': 'comment' if cid else 'post',
        'resolved': obj is not None,
        'author': (obj or {}).get('author'),
        'subreddit': (obj or {}).get('subreddit'),
        'created_utc': (obj or {}).get('created_utc'),
        'removed_by_category': (obj or {}).get('removed_by_category'),
        'score': (obj or {}).get('score'),
        'title': (parent or {}).get('title'),
        'thread_author': (parent or {}).get('author'),
        'body': ((obj or {}).get('body') or (obj or {}).get('selftext') or '')[:6000],
        'refs': refs,
    }
    out.append(rec)

json.dump(out, open('/workspace/harvest/redteam/screen_urls.json', 'w'), indent=1)
unres = [o for o in out if not o['resolved']]
print('unresolved targets: %d' % len(unres))
for o in unres:
    print('   ', o['post_id'], o['comment_id'], o['refs'][0][1])
