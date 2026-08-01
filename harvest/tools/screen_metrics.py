#!/usr/bin/env python3
"""Step 4b: cadence and spread metrics that separate automation from a busy human.

The decisive one is round-the-clock burst posting: a peak day with hundreds of
items, activity in nearly every hour, and a median gap measured in seconds.
No human sustains that; karma-farming bots do it as a matter of course.
"""
import collections
import datetime as dt
import json
import re
import statistics

H = json.load(open('/workspace/harvest/redteam/screen_hist.json'))
S = json.load(open('/workspace/harvest/redteam/screen_signals.json'))
A = json.load(open('/workspace/harvest/redteam/screen_attrib.json'))

CJK = re.compile(r'[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]')
CYR = re.compile(r'[\u0400-\u04ff]')
# crude romance-language markers, enough to spot a persona posting in 3+ languages
PT_ES = re.compile(r'\b(que|não|nao|você|voce|porque|pero|para|como|muito|isso|tambien|também|'
                   r'estoy|estou|hacer|fazer|pero|obrigado|gracias)\b', re.I)
DE_NL_FR = re.compile(r'\b(nicht|und|aber|ist|het|niet|maar|een|vous|c\'est|pas|mais|être|avec)\b', re.I)


def day(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime('%Y-%m-%d')


def hour(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).hour


out = {}
for n, d in H.items():
    items = [(c['created_utc'], c.get('subreddit'), c.get('body') or '', c.get('link_id'), 'c')
             for c in (d.get('comments') or [])] + \
            [(p['created_utc'], p.get('subreddit'), (p.get('title') or '') + ' ' + (p.get('selftext') or ''),
              't3_' + str(p.get('id')), 'p') for p in (d.get('posts') or [])]
    items = sorted([i for i in items if i[0]])
    if not items:
        out[n] = {'n_items': 0}
        continue
    days = collections.Counter(day(i[0]) for i in items)
    peak_day, peak_n = days.most_common(1)[0]
    pk = [i for i in items if day(i[0]) == peak_day]
    hrs = {hour(i[0]) for i in pk}
    gaps = [pk[i + 1][0] - pk[i][0] for i in range(len(pk) - 1)]
    med_gap = statistics.median(gaps) if gaps else None
    active = max(1.0, (items[-1][0] - items[0][0]) / 86400.0)

    # conversational depth: threads where the account posted more than once
    per_thread = collections.Counter(i[3] for i in items if i[3])
    multi = sum(1 for k, v in per_thread.items() if v > 1)

    txt = ' '.join(i[2] for i in items)
    langs = sum([bool(CJK.search(txt)), bool(CYR.search(txt)),
                 len(PT_ES.findall(txt)) > 25, len(DE_NL_FR.findall(txt)) > 25])

    out[n] = {
        'n_items': len(items),
        'items_per_active_day': round(len(items) / active, 2),
        'peak_day': peak_day, 'peak_day_items': peak_n,
        'peak_day_hours_covered': len(hrs),
        'peak_day_median_gap_s': med_gap,
        'peak_day_subs': len({i[1] for i in pk}),
        'n_threads': len(per_thread), 'threads_multi_comment': multi,
        'frac_threads_revisited': round(multi / max(1, len(per_thread)), 3),
        'n_scripts_langs': langs,
        'machine_cadence': bool(peak_n >= 90 and len(hrs) >= 18 and (med_gap or 9999) <= 300),
    }

json.dump(out, open('/workspace/harvest/redteam/screen_metrics.json', 'w'), indent=1)

recs = collections.Counter(a['author'] for a in A)
print('%-26s %4s %8s %6s %5s %5s %6s %5s %5s %4s %s' % (
    'account', 'rec', 'items/d', 'peak', 'hrs', 'subs', 'medgap', 'thr%', 'langs', 'MACH', 'first'))
for n, m in sorted(out.items(), key=lambda kv: -(kv[1].get('peak_day_items') or 0)):
    if not m.get('n_items'):
        continue
    print('%-26s %4d %8.2f %6d %5d %5d %6s %5.2f %5d %4s %s' % (
        n, recs[n], m['items_per_active_day'], m['peak_day_items'], m['peak_day_hours_covered'],
        m['peak_day_subs'], m['peak_day_median_gap_s'], m['frac_threads_revisited'],
        m['n_scripts_langs'], 'YES' if m['machine_cadence'] else '', S[n]['first_seen']))
