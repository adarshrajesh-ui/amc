#!/usr/bin/env python3
"""Step 4: compute bot/promo/genuine signals for every screened account.

Signals are computed, not asserted. Adjudication happens afterwards under the
calibration that throwaway accounts are the NORM for interview recall, so
thin-and-anonymous is not by itself evidence of anything.
"""
import collections
import datetime as dt
import json
import re

H = json.load(open('/workspace/harvest/redteam/screen_hist.json'))
A = json.load(open('/workspace/harvest/redteam/screen_attrib.json'))

# --- language-model artifacts: assistant voice leaking into a "candidate" post ---
LLM_PATS = [
    (r'你好[，,]?\s*我无法', 'zh refusal "你好，我无法"'),
    (r'我无法(提供|给到|回答|完成|协助|满足)', 'zh refusal "我无法提供/给到"'),
    (r'(很)?抱歉[，,]\s*(我无法|我不能|作为)', 'zh refusal "抱歉，我无法"'),
    (r'作为(一个|一名)?\s*(AI|人工智能|大型语言模型|语言模型)', 'zh "作为一个AI/语言模型"'),
    (r'无法给到相关内容', 'zh refusal "无法给到相关内容"'),
    (r'\bas an ai (language model|assistant|,|i )', 'en "as an AI language model/assistant"'),
    (r'\bas a large language model\b', 'en "as a large language model"'),
    (r"\bi (cannot|can not|can't) (provide|assist with|help with|comply|fulfill|generate) (that|this|the requested|relevant)", 'en refusal "I cannot provide that"'),
    (r"i'?m sorry,? but i (can'?t|cannot|am unable)", 'en refusal "I\'m sorry, but I can\'t"'),
    (r"i'?m (not able|unable) to (provide|assist|help) with (that|this)", 'en refusal'),
    (r'\btest injection\b', 'literal "test injection"'),
    (r'\byou are a helpful assistant\b', 'system-prompt fragment'),
    (r'\b(ignore (all )?previous instructions)\b', 'prompt-injection fragment'),
    (r'\[insert [a-z][a-z ]{2,30}\]', 'unfilled template placeholder'),
    (r'\{\{\s*[a-z_][a-z_0-9 ]{1,30}\s*\}\}', 'unfilled mustache placeholder'),
    (r'\bas an ai\b(?!\s*(trainer|engineer|for|researcher|dev))', 'en "as an AI"'),
    (r'\bmy (training data|knowledge cutoff|last update)\b', 'model self-reference'),
    (r'^(certainly|sure)[!,]\s+here', 'assistant opener'),
    (r'\bi hope this helps!\s*$', 'assistant closer'),
]

# --- product promotion: the product must be *linked* or *claimed as one's own* ---
PRODUCT_DOMAINS = [
    'interviews.chat', 'quantgrind.app', 'quantgrind', 'beyz.ai', 'beyzapp', 'usebeyz',
    'finalroundai.com', 'lockedinai', 'cluely.com', 'senseicopilot', 'verveai', 'huru.ai',
    'interviewcoder', 'leetcodewizard', 'ultracode.ai', 'parakeet.ai', 'offerin.ai',
    'quantguide.io', 'quantquestions.io', 'openquant', 'wallstreetquants', 'getcracked.io',
    'tryexponent.com', 'interviewquery.com', 'stratascratch.com', 'prepfully.com',
    'jobright.ai', 'aihirely', 'careerflow.ai', 'resumeworded',
]
OWN_PROMO = re.compile(
    r"(shameless plug|i built|i made|i created|i run|i'?m the founder|i am the founder|founder here|"
    r"we built|we launched|we made|check out my|check out our|my site|my website|my app|our site|our app|"
    r"i've been working on|i have been working on|dm me if you want|link in bio|sign ?up (here|at)|"
    r"try it (out )?(here|at)|use code )", re.I)


def ts(x):
    try:
        return dt.datetime.fromtimestamp(int(x), dt.timezone.utc).strftime('%Y-%m-%d')
    except Exception:
        return None


def analyze(name, d):
    info = d.get('info') or {}
    cs = d.get('comments') or []
    ps = d.get('posts') or []
    items = [(c.get('created_utc'), 'c', c.get('subreddit'), c.get('body') or '', c) for c in cs] + \
            [(p.get('created_utc'), 'p', p.get('subreddit'),
              (p.get('title') or '') + '\n' + (p.get('selftext') or ''), p) for p in ps]
    items = [i for i in items if i[0]]
    items.sort(key=lambda i: (i[0], i[1]))
    texts = [i[3] for i in items]
    subs = collections.Counter(i[2] for i in items if i[2])

    firsts = [x for x in [info.get('earliest_comment_at'), info.get('earliest_post_at')] if x]
    first_seen = min(firsts) if firsts else (items[0][0] if items else None)
    lasts = [x for x in [info.get('last_comment_at'), info.get('last_post_at')] if x]
    last_seen = max(lasts) if lasts else (items[-1][0] if items else None)

    arts = []
    for t in texts:
        for pat, label in LLM_PATS:
            for m in re.finditer(pat, t, re.I | re.M):
                s = max(0, m.start() - 100)
                arts.append({'label': label, 'excerpt': t[s:m.end() + 180].strip()})
    seen, uarts = set(), []
    for a in arts:
        k = (a['label'], a['excerpt'][:70])
        if k in seen:
            continue
        seen.add(k)
        uarts.append(a)

    promo = []
    for t in texts:
        low = t.lower()
        for dom in PRODUCT_DOMAINS:
            if dom not in low:
                continue
            i = low.find(dom)
            ctx = t[max(0, i - 260):i + 200]
            linked = bool(re.search(re.escape(dom) + r'|https?://\S*' + re.escape(dom.split('.')[0]), low))
            owns = bool(OWN_PROMO.search(ctx))
            if owns or (linked and re.search(r'https?://\S*' + re.escape(dom.split('.')[0]), low)):
                promo.append({'domain': dom, 'own_promo': owns, 'excerpt': ctx.strip()})
    seenp, upromo = set(), []
    for p in promo:
        k = (p['domain'], p['excerpt'][:70])
        if k in seenp:
            continue
        seenp.add(k)
        upromo.append(p)

    n_link = sum(1 for t in texts if re.search(r'https?://', t))
    n_endlink = sum(1 for t in texts
                    if re.search(r'(https?://\S+\)?|\[[^\]]+\]\(https?://[^)]+\))\s*$', t.strip()[-200:]))
    removed = sum(1 for i in items if i[4].get('removed_by_category'))
    deleted = sum(1 for i in items if (i[3] or '').strip() in ('[deleted]', '[removed]', '[deleted]\n', ''))

    n = len(items) or 1
    span_days = ((last_seen - first_seen) / 86400.0) if (first_seen and last_seen) else 0
    singles = sum(1 for s, c in subs.items() if c == 1)

    return {
        'account': name, 'has_info': bool(info),
        'first_seen': ts(first_seen), 'last_seen': ts(last_seen),
        'first_seen_ts': first_seen, 'span_days': round(span_days, 1),
        'n_items': len(items), 'n_comments_seen': len(cs), 'n_posts_seen': len(ps),
        'num_comments_reported': info.get('num_comments'), 'num_posts_reported': info.get('num_posts'),
        'total_karma': info.get('total_karma'),
        'n_subreddits': len(subs), 'top_subs': subs.most_common(15),
        'single_item_subs': singles,
        'frac_singleton_subs': round(singles / max(1, len(subs)), 3),
        'llm_artifacts': uarts, 'promo_hits': upromo,
        'n_with_link': n_link, 'frac_with_link': round(n_link / n, 3),
        'n_ending_on_link': n_endlink,
        'n_removed': removed, 'n_deleted_body': deleted,
        'frac_removed': round((removed + deleted) / n, 3),
    }


out = {name: analyze(name, d) for name, d in H.items()}

# attach per-account record load and the cited items
recs = collections.defaultdict(list)
for a in A:
    recs[a['author']].append(a)
for n, s in out.items():
    s['n_records'] = len(recs.get(n, []))
    s['firms'] = sorted({r['firm'] for r in recs.get(n, [])})
    s['cited_subreddits'] = sorted({r['subreddit'] for r in recs.get(n, []) if r.get('subreddit')})
    s['cited_dates'] = sorted({r['post_date'] for r in recs.get(n, []) if r.get('post_date')})
    # account age (days) at the moment of the earliest cited item
    cu = [r.get('created_utc') for r in recs.get(n, []) if r.get('created_utc')]
    if cu and s['first_seen_ts']:
        s['acct_age_days_at_citation'] = round((min(cu) - s['first_seen_ts']) / 86400.0, 1)
    else:
        s['acct_age_days_at_citation'] = None

json.dump(out, open('/workspace/harvest/redteam/screen_signals.json', 'w'), indent=1)


def risk(s):
    r = 0
    if s['llm_artifacts']:
        r += 100
    if any(p['own_promo'] for p in s['promo_hits']):
        r += 60
    elif s['promo_hits']:
        r += 15
    if (s['first_seen'] or '') >= '2026-01-01':
        r += 12
    if s['n_items'] <= 30 and s['n_subreddits'] >= 8:
        r += 15
    if s['frac_singleton_subs'] > 0.7 and s['n_subreddits'] >= 8:
        r += 10
    if s['frac_with_link'] > 0.3:
        r += 8
    if s['frac_removed'] > 0.35:
        r += 6
    if s['span_days'] < 60 and s['n_items'] > 15:
        r += 6
    return r


print('%-28s %5s %4s %5s %5s %5s %6s %5s %5s  %s' % (
    'account', 'risk', 'rec', 'items', 'subs', 'sing%', 'first', 'link%', 'rm%', 'flags'))
for n, s in sorted(out.items(), key=lambda kv: -risk(kv[1])):
    fl = []
    if s['llm_artifacts']:
        fl.append('LLM:' + s['llm_artifacts'][0]['label'][:34])
    if any(p['own_promo'] for p in s['promo_hits']):
        fl.append('OWNPROMO:' + s['promo_hits'][0]['domain'])
    elif s['promo_hits']:
        fl.append('promo?')
    if not s['has_info']:
        fl.append('no-userinfo')
    print('%-28s %5d %4d %5d %5d %5.2f %6s %5.2f %5.2f  %s' % (
        n, risk(s), s['n_records'], s['n_items'], s['n_subreddits'], s['frac_singleton_subs'],
        (s['first_seen'] or '?')[:7], s['frac_with_link'], s['frac_removed'], ' '.join(fl)))
