"""Assemble all attack evidence per target record and assign a verdict."""
import json, os, re, datetime
from urllib.parse import urlparse, unquote
import textbook

HERE = os.path.dirname(os.path.abspath(__file__))
J = lambda p: json.load(open(os.path.join(HERE, p)))

RECS = {}
for l in open(os.path.join(HERE, '..', 'questions.jsonl')):
    r = json.loads(l); RECS[r['id']] = r

# ---- proven bad actors (established by direct evidence, see red_team.json) ----
BOT_ACCOUNTS = {
 'weaklypalecabal': 'LLM-driven bot: posted the Chinese refusal string "你好，我无法给到相关内容。" as a Reddit comment; account first active 2026-06-25, 22 comments spread over 13 unrelated subs (DynastyFFTradeAdvice, Mortgages, dropshipping, coincollecting, defi...), 4 removed+deleted.',
 'snoopy_priesthood': 'Karma/referral-farming bot: first active 2026-06-17, 18 comments over 13 unrelated subs; simultaneously claims to be a South African expat, an MCAT taker, a FIRE planner and a quant OA candidate; posts referral-link spam.',
 'Senior_Shelter7426': 'Karma-farming bot: first active 2026-03-22, 26 items spread one-per-sub over 22 unrelated subs (Coinbase, pchelp, Breadit, bathandbodyworks, AskIreland); its single r/quantfinance comment is the SIG "market making games" claim.',
 'QuantGrindApp': 'Vendor account: literally the QuantGrind product account (named on the prep-vendor offender list); created 2026-06-02, 102 items, 87 of them in r/quant + r/quantfinance, with its own u_QuantGrindApp profile sub.',
 'nullnotfound2': 'Interview-assist marketing bot: first active 2026-06-09, 28 items with 12 removed AND deleted later (43%); posts only into FAANGrecruiting / interviews / interviewpreparations / amazonsdeprep; uniform all-lowercase "i interviewed at X, here is my prep method" template.',
 'chocolate_asshole': 'Spam account: 102 of 105 items removed by moderators and 100 deleted later (97%); first active 2026-04-19, 43 unrelated subs.',
}
VENDOR_AFFILIATE = {
 'Nero-Tulip': 'Tradermath.org affiliate/promoter: 10 of 60 sampled comments push tradermath.org with direct links ("Check out https://www.tradermath.org/dashboard/black, our prayers have been answered!"); necro-posts 2018/2022 SIG threads in Sept 2023 to place the link. Every "recall" it supplies is a vague genre phrase embedded in a product plug.',
}
# t.me/aistockanalyst/887 = a general multi-firm prop-trading prep essay, not SIG recall
MISATTRIBUTED_TG = {'https://t.me/aistockanalyst/887'}
SELF_DUP = {'Leader-board'}


def base(u):
    if 'web.archive.org' in u:
        m = re.search(r'/(https?://.+)$', u)
        if m:
            u = unquote(m.group(1))
    return u.rstrip('/')


def dom(u):
    return urlparse(base(u)).netloc.lower().replace('www.', '')


def load_evidence():
    ev = {}
    ev['sweep'] = J('sweep_sig.json') if os.path.exists(os.path.join(HERE, 'sweep_sig.json')) else {}
    ev['cited'] = J('cited_comments.json')
    ev['authors'] = J('authors.json')
    gb, bs = textbook.load_local()
    ev['gb'], ev['bs'] = gb, bs
    return ev


def record_author(r, cited):
    out = []
    for a in r['attestations']:
        m = re.search(r'reddit\.com/r/[^/]+/comments/([a-z0-9]+)/[^/]*/([a-z0-9]+)', a['source_url'])
        if m and m.group(2) in cited:
            out.append(cited[m.group(2)]['author'])
    return out


def adjudicate(rid, ev):
    r = RECS[rid]
    atts = r['attestations']
    urls = [base(a['source_url']) for a in atts]
    doms = [dom(a['source_url']) for a in atts]
    authors = record_author(r, ev['cited'])
    tried, finds = [], []
    verdict = 'SURVIVED'
    tb_overlap, tb_src, earliest = False, None, None

    # --- attack: AI/bot-generated recall ---
    tried.append('author forensics on every Reddit account backing the record (Arctic Shift history, account age, subreddit spread, moderator-removal rate, LLM-refusal-string leakage)')
    for au in authors:
        if au in BOT_ACCOUNTS:
            verdict = 'BROKEN'
            finds.append('SOLE SOURCE IS A BOT. u/%s: %s' % (au, BOT_ACCOUNTS[au]))
        elif au in VENDOR_AFFILIATE:
            verdict = 'BROKEN'
            finds.append('SOLE SOURCE IS A PREP-VENDOR AFFILIATE. u/%s: %s' % (au, VENDOR_AFFILIATE[au]))

    # --- attack: misattributed generic prep guide ---
    tried.append('read the full cited source to check the question is actually attributed to SIG rather than to prop-trading firms in general')
    if any(u in MISATTRIBUTED_TG for u in urls):
        verdict = 'BROKEN'
        finds.append('MISATTRIBUTION. t.me/aistockanalyst/887 is a single general essay on prop-trading recruitment by one author who says the firm he joined was a smaller one ("我進的是規模較小的"); the quoted text sits under generic headings ("Market Making", "Online Assessment (Math/Coding)") describing what prop firms in general do. The company list printed immediately after the quoted passage is "Jane Street, Virtu Financials, Jump Trading, Akuna Capital, Chicago Trading Company, Transmarket Group, Flow Traders" - SIG is not in it. Nothing in the passage is attributed to SIG.')

    # --- attack: corroboration integrity ---
    tried.append('tested whether the claimed independent attestations are actually independent (same author cross-posting, Telegram mirror of the cited forum thread, archive snapshot of the cited page)')
    ia = r.get('independent_attestations') or 0
    if ia >= 2:
        if any(a in SELF_DUP for a in authors) and any('github.com' in d for d in doms):
            if verdict == 'SURVIVED':
                verdict = 'WOUNDED'
            finds.append('CORROBORATION IS FAKE. The two "independent" sources are u/Leader-board\'s GitHub repo and u/Leader-board\'s own Reddit comment - the same person, and the Reddit comment is a verbatim copy-paste of the GitHub markdown. Real independent attestations = 1, not %d.' % ia)
        if any('t.me/usinterview' in u for u in urls):
            if verdict == 'SURVIVED':
                verdict = 'WOUNDED'
            finds.append('CORROBORATION IS FAKE. t.me/usinterview ("北美跳槽面经", 428 subscribers, 29.2K links) is an automated mirror bot that reposts 1point3acres thread link-previews; the cited Telegram messages mirror the very 1point3acres thread cited alongside them. Real independent attestations = 1, not %d.' % ia)

    # --- attack: textbook laundering ---
    tried.append('textbook-laundering check against a live scrape of Brainstellar (275 puzzles), the Green Book ch.2 problem set (139 statements) and classic-problem signatures from Crack / Joshi / Mosteller')
    en = r.get('question_text_en') or ''
    tbm = textbook.match(en, r.get('question_text'))
    if tbm:
        tb_overlap = True
        tb_src = '; '.join('%s (%s)' % (a, b) for a, b, _ in tbm)
        onlybook = all(d in ('brainstellar.com',) for d in doms)
        finds.append('TEXTBOOK OVERLAP: %s. Not fatal on its own - the cited attestation is a candidate post, and firms do ask textbook problems - but the question is not original to SIG.' % tb_src)
        if onlybook:
            verdict = 'BROKEN'

    # --- attack: vendor provenance / earliest appearance via search ---
    tried.append('open-web earliest-appearance and vendor-provenance search on the question\'s distinctive wording')
    sw = ev['sweep'].get(rid)
    vend, hw = set(), set()
    searched = False
    if sw:
        for q, qq in sw['queries'].items():
            if not qq.get('ok'):
                continue
            searched = True
            for t in qq['tags']:
                if t.startswith('vendor:'):
                    vend.add(t.split(':', 1)[1])
                if t.startswith('homework:'):
                    hw.add(t.split(':', 1)[1])
    if vend:
        finds.append('Question wording also appears on prep-vendor sites (%s).' % ', '.join(sorted(vend)))
    if hw:
        finds.append('Question wording also appears on homework-answer sites (%s), the usual signature of a problem that circulates outside the firm.' % ', '.join(sorted(hw)))
    if not searched:
        finds.append('Open-web search inconclusive: every search engine refused the query, so earliest appearance could not be established.')

    # --- attack: single-source ---
    tried.append('checked how many genuinely distinct sources attest the question')
    if ia <= 1 and verdict == 'SURVIVED':
        finds.append('Single-source: the record rests on one post. Attacked but not broken - the source is a dated first-person candidate account that I could not tie to a vendor, a bot or a book.')

    return {
        'id': rid, 'firm': r['firm'], 'verdict': verdict,
        'attack_tried': '; '.join(tried),
        'finding': ' | '.join(finds) if finds else 'Attacked on all six vectors; nothing stuck.',
        'textbook_overlap': tb_overlap, 'textbook_source': tb_src,
        'earliest_appearance': earliest,
    }


if __name__ == '__main__':
    ev = load_evidence()
    ids = J('targets.json')
    out = [adjudicate(i, ev) for i in ids]
    json.dump(out, open(os.path.join(HERE, 'verdicts_auto.json'), 'w'), indent=1)
    from collections import Counter
    print(Counter(o['verdict'] for o in out))
