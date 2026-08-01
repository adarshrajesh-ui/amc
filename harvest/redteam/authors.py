"""Profile every Reddit account that backs a corpus record.

Signals: account age at time of post, total cached history, removal/deletion rate,
subreddit spread, multi-firm 'perfect recall' claims, and AI-marketing texture.
"""
import json, os, re, sys, time, datetime
from concurrent.futures import ThreadPoolExecutor
import net

HERE = os.path.dirname(os.path.abspath(__file__))
API = 'https://arctic-shift.photon-reddit.com/api'


def get_author(a):
    out = {'author': a}
    try:
        b = net.fetch('%s/comments/search?author=%s&limit=100' % (API, a), 'auc')
        d = json.loads(b).get('data', [])
    except Exception:
        d = []
    try:
        pb = net.fetch('%s/posts/search?author=%s&limit=100' % (API, a), 'aup')
        pd = json.loads(pb).get('data', [])
    except Exception:
        pd = []
    out['n_comments'] = len(d)
    out['n_posts'] = len(pd)
    items = d + pd
    if items:
        cu = [i.get('created_utc') for i in items if i.get('created_utc')]
        out['first_utc'] = min(cu) if cu else None
        out['last_utc'] = max(cu) if cu else None
        acc = [i.get('author_created_utc') for i in items if i.get('author_created_utc')]
        out['author_created_utc'] = min(acc) if acc else None
        rem = sum(1 for i in items if (i.get('_meta') or {}).get('removal_type'))
        dele = sum(1 for i in items if (i.get('_meta') or {}).get('was_deleted_later'))
        out['removed'] = rem
        out['deleted_later'] = dele
        out['subs'] = {}
        for i in items:
            s = i.get('subreddit')
            out['subs'][s] = out['subs'].get(s, 0) + 1
        out['bodies'] = [re.sub(r'\s+', ' ', (i.get('body') or i.get('selftext') or ''))[:600]
                         for i in items][:60]
    return out


def main():
    names = json.load(open(sys.argv[1]))
    outp = sys.argv[2]
    res = {}
    if os.path.exists(outp):
        res = json.load(open(outp))
    todo = [n for n in names if n not in res and n not in ('[deleted]', 'AutoModerator', None)]
    print('profiling', len(todo), flush=True)
    with ThreadPoolExecutor(max_workers=5) as ex:
        for i, r in enumerate(ex.map(get_author, todo)):
            res[r['author']] = r
            if i % 20 == 0:
                print(' ..', i, flush=True); json.dump(res, open(outp, 'w'))
    json.dump(res, open(outp, 'w'))
    print('done', len(res))


if __name__ == '__main__':
    main()
