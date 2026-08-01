#!/usr/bin/env python3
"""Step 1b: attribute each quote to the account that actually wrote *that text*.

A thread-level URL is ambiguous: the harvester often cites the thread but quotes a
commenter inside it. Resolve by matching the stored source_quote against the post
selftext first, then against every comment in the thread.
"""
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, '/workspace/harvest/tools')
from screen_lib import get, parse_url

rows = [json.loads(l) for l in open('/workspace/harvest/questions.jsonl')]
urlrecs = json.load(open('/workspace/harvest/redteam/screen_urls.json'))
byurl = {}
for o in urlrecs:
    for cid, u in o['refs']:
        byurl[(cid, u)] = o

# threads we need full comment trees for
need = sorted({o['post_id'] for o in urlrecs if not o['comment_id']})
print('fetching comment trees for %d threads' % len(need), flush=True)


def tree(pid):
    out, after = [], None
    for _ in range(6):
        kw = dict(link_id='t3_' + pid, limit=100)
        if after:
            kw['after'] = after
        d = get('comments/search', **kw)
        if not d:
            break
        out.extend(d)
        if len(d) < 100:
            break
        after = max(x['created_utc'] for x in d)
    return pid, out


trees = {}
with ThreadPoolExecutor(max_workers=4) as ex:
    for pid, cs in ex.map(tree, need):
        trees[pid] = cs
print('trees fetched: %d (total comments %d)' % (len(trees), sum(len(v) for v in trees.values())), flush=True)
json.dump({k: v for k, v in trees.items()}, open('/workspace/harvest/redteam/screen_trees.json', 'w'))


def norm(s):
    s = re.sub(r'\s+', ' ', (s or '')).strip().lower()
    return re.sub(r'[^a-z0-9 ]+', '', s)


def best_match(quote, cands):
    """cands: list of (author, text, obj). Return best by longest shared snippet."""
    q = norm(quote)
    if len(q) < 25:
        return None
    # try progressively shorter prefixes/windows of the quote
    for L in (200, 120, 80, 50, 35):
        wins = [q[i:i + L] for i in range(0, max(1, len(q) - L + 1), max(1, L // 2))][:8]
        for w in wins:
            if len(w) < 30:
                continue
            hits = [c for c in cands if w in norm(c[1])]
            if len(hits) == 1:
                return hits[0]
            if len(hits) > 1:
                return sorted(hits, key=lambda c: len(c[1]))[0]
    return None


out = []
stats = {'comment_permalink': 0, 'post_selftext': 0, 'matched_comment': 0, 'fallback_post_author': 0,
         'fallback_context_name': 0, 'unattributed': 0}
for r in rows:
    for a in r.get('attestations', []):
        if a.get('source_type') != 'reddit_thread':
            continue
        o = byurl.get((r['id'], a['source_url']))
        quote = a.get('source_quote') or ''
        pc = a.get('poster_context') or ''
        claimed = re.findall(r'u/([A-Za-z0-9_\-]{3,25})', pc)
        rec = {'id': r['id'], 'firm': r['firm'], 'tier': r['tier'], 'url': a['source_url'],
               'post_date': a.get('post_date'), 'quote': quote[:1200], 'poster_context': pc,
               'claimed': claimed, 'subreddit': (o or {}).get('subreddit'),
               'title': (o or {}).get('title'), 'post_id': (o or {}).get('post_id'),
               'comment_id': (o or {}).get('comment_id')}
        if o and o['comment_id']:
            rec['author'] = o['author']
            rec['author_basis'] = 'comment permalink'
            rec['created_utc'] = o['created_utc']
            rec['text'] = o['body']
            stats['comment_permalink'] += 1
        elif o:
            pid = o['post_id']
            self_txt = o['body'] or ''
            cands = [(c['author'], c.get('body') or '', c) for c in trees.get(pid, [])
                     if c.get('author') not in (None, '[deleted]', 'AutoModerator')]
            if norm(quote)[:60] and norm(quote)[:60] in norm(self_txt):
                rec['author'] = o['author']
                rec['author_basis'] = 'quote found in post selftext'
                rec['created_utc'] = o['created_utc']
                rec['text'] = self_txt
                stats['post_selftext'] += 1
            else:
                m = best_match(quote, cands)
                if m:
                    rec['author'] = m[0]
                    rec['author_basis'] = 'quote matched to comment %s in thread' % m[2]['id']
                    rec['created_utc'] = m[2]['created_utc']
                    rec['comment_id'] = m[2]['id']
                    rec['text'] = m[1]
                    stats['matched_comment'] += 1
                elif claimed and any(c.lower() in {x[0].lower() for x in cands} for c in claimed):
                    nm = [c for c in claimed if c.lower() in {x[0].lower() for x in cands}][0]
                    hit = [x for x in cands if x[0].lower() == nm.lower()][0]
                    rec['author'] = hit[0]
                    rec['author_basis'] = 'poster_context name present as commenter (quote not text-matched)'
                    rec['created_utc'] = hit[2]['created_utc']
                    rec['text'] = hit[1]
                    stats['fallback_context_name'] += 1
                else:
                    rec['author'] = o['author']
                    rec['author_basis'] = 'fallback: thread OP (quote not located)'
                    rec['created_utc'] = o['created_utc']
                    rec['text'] = self_txt
                    stats['fallback_post_author'] += 1
        else:
            rec['author'] = None
            rec['author_basis'] = 'unresolved'
            stats['unattributed'] += 1
        out.append(rec)

json.dump(out, open('/workspace/harvest/redteam/screen_attrib.json', 'w'), indent=1)
print(json.dumps(stats, indent=1))
import collections
ac = collections.Counter(x['author'] for x in out)
print('distinct authors: %d over %d attestations' % (len(ac), len(out)))
