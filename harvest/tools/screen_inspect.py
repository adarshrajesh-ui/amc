#!/usr/bin/env python3
"""Print a full dossier for one account: metadata, subreddit spread, timeline,
the exact cited text, and a sample of unrelated activity."""
import collections
import datetime as dt
import json
import sys

H = json.load(open('/workspace/harvest/redteam/screen_hist.json'))
A = json.load(open('/workspace/harvest/redteam/screen_attrib.json'))
S = json.load(open('/workspace/harvest/redteam/screen_signals.json'))


def ts(x):
    try:
        return dt.datetime.fromtimestamp(int(x), dt.timezone.utc).strftime('%Y-%m-%d %H:%M')
    except Exception:
        return '?'


def dossier(name, nsample=14, width=420):
    d = H.get(name) or {}
    s = S.get(name) or {}
    print('=' * 110)
    print('ACCOUNT %s   records=%s  firms=%s' % (name, s.get('n_records'), s.get('firms')))
    print('  first_seen=%s last_seen=%s span=%sd items=%s subs=%s singleton_subs=%s karma=%s' % (
        s.get('first_seen'), s.get('last_seen'), s.get('span_days'), s.get('n_items'),
        s.get('n_subreddits'), s.get('frac_singleton_subs'), s.get('total_karma')))
    print('  reported num_comments=%s num_posts=%s | acct age at citation=%s d' % (
        s.get('num_comments_reported'), s.get('num_posts_reported'), s.get('acct_age_days_at_citation')))
    print('  link%%=%s ending-on-link=%s removed%%=%s' % (
        s.get('frac_with_link'), s.get('n_ending_on_link'), s.get('frac_removed')))
    print('  TOP SUBS:', s.get('top_subs'))
    if s.get('llm_artifacts'):
        print('  !! LLM ARTIFACTS:')
        for a in s['llm_artifacts'][:8]:
            print('     [%s] %s' % (a['label'], a['excerpt'][:300].replace('\n', ' ')))
    if s.get('promo_hits'):
        print('  !! PROMO:')
        for a in s['promo_hits'][:8]:
            print('     [%s own=%s] %s' % (a['domain'], a['own_promo'], a['excerpt'][:300].replace('\n', ' ')))

    print('\n  --- CITED CONTENT (%d) ---' % len([x for x in A if x['author'] == name]))
    for x in [x for x in A if x['author'] == name]:
        print('  * %s | %s | %s | r/%s | %s' % (x['id'], x['firm'], x['post_date'], x['subreddit'], x['author_basis']))
        print('    thread: %s' % (x['title'] or '')[:110])
        print('    text: %s' % (x.get('text') or '')[:width].replace('\n', ' '))

    items = [(c.get('created_utc'), 'c', c.get('subreddit'), c.get('body') or '')
             for c in (d.get('comments') or [])] + \
            [(p.get('created_utc'), 'p', p.get('subreddit'), (p.get('title') or '') + ' :: ' + (p.get('selftext') or ''))
             for p in (d.get('posts') or [])]
    items = sorted([i for i in items if i[0]], key=lambda i: i[0])
    print('\n  --- ACTIVITY SAMPLE (%d items) ---' % len(items))
    step = max(1, len(items) // nsample)
    for i in items[::step][:nsample]:
        print('  %s %s r/%-24s %s' % (ts(i[0]), i[1], (i[2] or '?')[:24], (i[3] or '')[:210].replace('\n', ' ')))


if __name__ == '__main__':
    for n in sys.argv[1:]:
        dossier(n)
