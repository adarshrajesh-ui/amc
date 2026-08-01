#!/usr/bin/env python3
"""Re-fetch accounts whose history hit the earlier page cap, so subreddit-spread and
cadence statistics are computed over the whole account rather than its first months."""
import json
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, '/workspace/harvest/tools')
from screen_lib import get

H = json.load(open('/workspace/harvest/redteam/screen_hist.json'))
need = [n for n, v in H.items()
        if len(v.get('comments') or []) >= 1100 or len(v.get('posts') or []) >= 690]
print('topping up %d accounts: %s' % (len(need), need), flush=True)

MAXPAGES = 90


def page(kind, author):
    out, seen, after = [], set(), None
    for _ in range(MAXPAGES):
        kw = dict(author=author, limit=100, sort='asc')
        if after:
            kw['after'] = after
        d = get('%s/search' % kind, **kw)
        if not d:
            break
        new = [x for x in d if x.get('id') not in seen]
        for x in new:
            seen.add(x['id'])
        out.extend(new)
        if len(d) < 100 or not new:
            break
        nxt = max(x['created_utc'] for x in d)
        if after is not None and nxt <= after:
            nxt = after + 1
        after = nxt
    return out


def profile(a):
    return a, {'info': (H[a] or {}).get('info'), 'comments': page('comments', a), 'posts': page('posts', a)}


with ThreadPoolExecutor(max_workers=4) as ex:
    for i, (a, d) in enumerate(ex.map(profile, need)):
        H[a] = d
        print('[%2d/%d] %-26s comments=%5d posts=%5d' % (
            i + 1, len(need), a, len(d['comments']), len(d['posts'])), flush=True)

json.dump(H, open('/workspace/harvest/redteam/screen_hist.json', 'w'))
print('done')
