#!/usr/bin/env python3
"""Step 2/3: pull account metadata and full comment+post history for every account
behind a reddit_thread attestation."""
import json
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, '/workspace/harvest/tools')
from screen_lib import get

attrib = json.load(open('/workspace/harvest/redteam/screen_attrib.json'))
authors = sorted({a['author'] for a in attrib if a.get('author')})
print('accounts to profile: %d' % len(authors), flush=True)

MAXPAGES = 12


def page(kind, author):
    out, after = [], None
    for _ in range(MAXPAGES):
        kw = dict(author=author, limit=100, sort='asc')
        if after:
            kw['after'] = after
        d = get('%s/search' % kind, **kw)
        if not d:
            break
        new = [x for x in d if x.get('id') not in {y.get('id') for y in out}]
        out.extend(new)
        if len(d) < 100 or not new:
            break
        after = max(x['created_utc'] for x in d)
    return out


def profile(a):
    try:
        info = get('users/search', author=a) or []
        cs = page('comments', a)
        ps = page('posts', a)
        return a, {'info': info[0] if info else None, 'comments': cs, 'posts': ps}
    except Exception as e:
        return a, {'error': str(e)}


res = {}
with ThreadPoolExecutor(max_workers=4) as ex:
    for i, (a, d) in enumerate(ex.map(profile, authors)):
        res[a] = d
        nc, np_ = len(d.get('comments') or []), len(d.get('posts') or [])
        print('[%3d/%d] %-28s info=%s comments=%d posts=%d' % (
            i + 1, len(authors), a, 'Y' if d.get('info') else 'N', nc, np_), flush=True)

json.dump(res, open('/workspace/harvest/redteam/screen_hist.json', 'w'))
print('done')
