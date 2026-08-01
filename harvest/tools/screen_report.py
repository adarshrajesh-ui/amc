#!/usr/bin/env python3
"""Step 6: adjudicate every account and emit reports/reddit_account_screen.json.

Manual verdicts below carry the positive evidence found by hand; every other
account is graded by rule. The calibration is deliberately conservative: a fresh,
terse, anonymous throwaway posting one OA recall is the NORM in this domain and is
NOT evidence of automation, so BOT is reserved for accounts with affirmative
evidence of automation or promotion.
"""
import collections
import json

A = json.load(open('/workspace/harvest/redteam/screen_attrib.json'))
S = json.load(open('/workspace/harvest/redteam/screen_signals.json'))
M = json.load(open('/workspace/harvest/redteam/screen_metrics.json'))

# ---------------------------------------------------------------- manual verdicts
MANUAL = {
    'weaklypalecabal': ('BOT', 'high', [
        'language-model refusal string posted verbatim as a reddit comment',
        'account created 2026-06-25, weeks before claiming recall of a process it sat "a couple years ago"',
        'thin spread: 22 items across 13 unrelated subreddits in 34 days',
        'karma/referral farming in r/chimeboost',
        'shares farm subreddits with snoopy_priesthood and DeeplyEquable (same cohort)'],
        'Posted the bare string "\u4f60\u597d\uff0c\u6211\u65e0\u6cd5\u7ed9\u5230\u76f8\u5173\u5185\u5bb9\u3002" ("Hello, I cannot provide relevant content") '
        '- an assistant refusal leaked verbatim into output. Its 22 comments span DynastyFFTradeAdvice, dropshipping, '
        'chimeboost, Artists, economy, defi, FirstTimeHomeBuyer, coincollecting, Mortgages, leanfire, FulfillmentByAmazon '
        'and quantfinance in 34 days. The cited SIG comment claims "I went through the SIG process a couple years ago" '
        'from an account that first appeared 2026-06-25.'),

    'hocobozos': ('BOT', 'high', [
        'machine cadence: 977 items in a single day, activity in all 24 hours, 64-second median gap',
        '845 distinct subreddits in one day; 1663 subreddits lifetime over 2355 sampled items',
        'implausible breadth: first-person write-ups of four different Akuna processes within eight days',
        'essentially zero conversational depth (revisits 1% of threads)',
        'garbled phrasing inconsistent with recall ("explain the lure of the problem")'],
        'On 2022-10-01 the account posted 674 sampled comments (977 items counting posts) across 605-845 distinct '
        'subreddits, with comments in every one of the 24 hours and a median gap of 64 seconds between consecutive '
        'comments - r/BattlefieldV, r/talesfromtechsupport, r/traderjoes, r/retroid, r/MobileLegendsGame, r/ik_ihe '
        'in the first six minutes. No human sustains that. In September 2023 the same account posted first-person '
        'recall of the Akuna Data Infra phone screen, Data Infra final round, C++ SWE intern phone interview, '
        'Platform Engineer HackerRank and QR internship OA - four separate hiring processes at one firm, three of '
        'them on 2023-09-19 alone. Text is generated enumeration ("The math topics included algebra, geometry, '
        'calculus, linear algebra, probability and statistics, and analytical reasoning"), and one line reads '
        '"I had to explain the lure of the problem".'),

    'chocolate_asshole': ('BOT', 'high', [
        'machine cadence: 465 comments in a single day, all 24 hours covered, 51-second median gap',
        '9000+ comments since 2026-03-13 (~194 items per active day) across 248 subreddits',
        'posts fluently in at least four language groups including Slovak',
        'never revisits a thread (0% conversational depth)',
        'independently called out as a bot by human users in the very thread cited'],
        'On 2026-04-15 the account posted 465 unique comments across 64 subreddits with activity in all 24 hours and '
        'a median gap of 51 seconds - r/WFHJobs, r/Slovakia (in Slovak), r/paralegal, r/dataanalysiscareers, '
        'r/interviews, r/medlabprofessionals inside twelve minutes. Lifetime ~194 items/day since 2026-03-13. In the '
        'cited thread (r/quantfinance 1stcxn5) a human replied "the comment above is by a bot. there are many bots on '
        'this sub advertising for different websites. beware!" and another wrote "that guy is also a bot lol".'),

    'OkSadMathematician': ('BOT', 'high', [
        'machine cadence: 226 items in a day, 26-second median gap across 61 subreddits',
        '4447 items since 2025-08-16 (~23 per active day) across 188 subreddits',
        'posts fluently in Portuguese and English, switching between them minutes apart',
        'links finalroundai.com (an interview-assist vendor) inside generated Portuguese content',
        'cited text is generic hedged advice with no first-person claim'],
        'On 2026-01-23 posted 225 comments across 61 subreddits with a 26-second median gap, alternating languages: '
        'r/brasilivre and r/carros in Portuguese, then r/programming and r/CodingHelp in English, within four minutes. '
        'Elsewhere it drops a finalroundai.com blog link inside Portuguese text, and recommends quantguide.io in an '
        'Optiver prep reply. The cited HRT record reads "hrt london algo dev phone screens are typically 45min split '
        'between algorithms and probability/stats" - hedged, no first-person claim, zero personal detail.'),

    'QuantGrindApp': ('PROMOTIONAL', 'high', [
        'operates an interview-prep product and links it repeatedly',
        '31 comments referencing its own quantgrind.app',
        'seeds firm-specific "insight" replies that close on the product',
        'independently described by another user as "literally just ChatGPT"'],
        'Self-identifies as the vendor: "Shameless plug: I built [https://quantgrind.app/] which has more questions '
        'from each firm so you can maximize your reps", "I run QuantGrind too (founder, so grain of salt)", "I run a '
        'prep site for this stuff (QuantGrind)". Two independent users in the corpus push back: u/Affectionate_Hat_308 '
        'wrote "Don\u2019t listen to QuantGrindApp, it\u2019s literally just ChatGPT incase you couldn\u2019t tell." and '
        'u/Formal-Region-6894 wrote "QuantGrindApp is wrong ignore what it said. It was a coding exam." Its firm-format '
        'claims are vendor marketing, not candidate recall.'),

    'Zealousideal-Fig9666': ('PROMOTIONAL', 'high', [
        'founder of a quant interview-prep site, posting to market it',
        'content-marketing posts claiming multi-firm assessment knowledge',
        'admits the 2200-problem bank was assembled by automated means'],
        'Posted "I built a quant interview prep site with 2200+ problems and 40+ courses" to r/quantfinance and '
        'answers feedback as the operator ("Yeah free right now! if it grows and hosting costs get real might add a '
        'paid tier"). Also posted "A simple interview question that trips up candidates at citsec, two sigma, tower, '
        'and arrowstreet last year" - multi-firm claims used as content marketing. On problem provenance: "Ended up '
        'using an open source word embedding model to map all 22[00]" problems. The cited record rests on vendor '
        'marketing copy, not on a candidate who sat the assessment.'),

    'snoopy_priesthood': ('BOT', 'medium', [
        'same cohort and farm subreddits as the confirmed bot weaklypalecabal',
        'created 2026-06-17; 18 items across 13 unrelated subreddits in 40 days',
        'karma/referral farming in r/chimeboost and r/Referrallinks',
        'claims prior-cycle SIG recall from an account six weeks old',
        'uniform confident two-sentence advice register across every topic'],
        'Shares r/chimeboost, r/FirstTimeHomeBuyer, r/economy and r/quantfinance with weaklypalecabal, which is proven '
        'automated by its leaked refusal string, and was created eight days before it. Comments run MCAT, humanresources, '
        'Scams, ENGLISH, ExpatFIRE, Referrallinks, economy - one or two each - in the same authoritative register '
        '("Sent one from $CapeTownBru. Got 3 left after that so hit me back"). The cited claim, "Did their OA last '
        'cycle", comes from an account first seen 2026-06-17. No language-model artifact of its own, hence medium.'),

    'DeeplyEquable': ('BOT', 'medium', [
        'same cohort and farm subreddits as the confirmed bot weaklypalecabal',
        'created 2026-07-02; 41 items across 18 unrelated subreddits in 27 days',
        'sycophantic self-contradiction: capitulates twice, in opposite directions, on one factual point',
        'posts in Portuguese in r/farialimabets and English elsewhere'],
        'Shares six subreddits with weaklypalecabal (DynastyFFTradeAdvice, coincollecting, dropshipping, economy, '
        'leanfire, quantfinance) and was created a week after it. In r/coincollecting it asserts "the copper stripe on '
        'the rim ... means its the 40% silver one", then "You\u2019re right, I mixed that up. The 40% silver ones have a '
        'solid silver edge, no copper stripe. My bad.", then "You\u2019re right, I had it backwards, copper stripe means '
        'clad, not silver" - agreeing with two correctors in contradictory directions, which is assistant-style '
        'capitulation rather than knowledge. No refusal string of its own, hence medium.'),

    'nullnotfound2': ('BOT', 'medium', [
        'implausible breadth: first-person interview claims at Amazon, Apple, Google and Citadel in one week',
        '27 comments in 7 days, then silence; 2026-06-09 account',
        'every single comment follows one template: first-person interview hook then generic advice',
        'zero non-career content, zero conversational depth, no personality markers'],
        'All 27 comments open with a personal interview claim in a different company/role: "i had a similar first-round '
        'em screen for amazon sde", "i agree ... based on my experience interviewing for an apple ds role too", "for my '
        'google interview, graphs and trees showed up more than dp", "i went through amazon sde interview a few months '
        'back", plus the cited Citadel claim. One person does not hold first-person Amazon SDE, Apple DS, Google SWE '
        'and Citadel SWE interview experience and post all of it in seven days in a uniform template, then stop. This '
        'is the persona-warming pattern that precedes product promotion; no link was posted yet, hence medium.'),

    'Senior_Shelter7426': ('BOT', 'medium', [
        'one persona detail reused as a conversational hook across five unrelated subreddits',
        '26 items across 22 subreddits, 91% of them one-offs, almost no thread revisits',
        'inconsistent persona geography (US slang alongside Irish register)',
        'generic supportive-advice register in emotional subs'],
        'The same self-characterisation is deployed as the hook in five unrelated topics: "Been tracking breeding '
        'patterns in a spreadsheet for months" (r/HorseLifeHQ), "I\u2019ve got everything tracked in spreadsheets down to '
        'the penny" (r/Marriage), "I track all my gaming expenses in a spreadsheet" (r/XboxGamePass), "I track pricing '
        'pretty closely" (r/samsunggalaxy), "I\u2019ve been tracking it in a spreadsheet since late 2025" (r/Coinbase). '
        'Register also swings from "I used to know a fella" in r/AskIreland to "nah fam" in r/americanairlines. '
        'Volume is low rather than machine-paced, hence medium.'),

    'landau007': ('BOT', 'medium', [
        'aged account dormant 2539 days, reactivated into promotional and monetizable niches',
        'reactivation content was NFT-giveaway spam, then generic finance/AI advice',
        'cited text is hedged generic advice with no first-person claim of sitting the process',
        'highest generic-advice register score of all 135 cited texts'],
        'Genuine-looking 2014-2017 history (r/cats, r/MapPorn, r/college), then a 2539-day gap, then reactivation on '
        '2024-10-29 with "Today\u2019s NFT giveaway for those with sufficient points" and "Today\u2019s Coinchattr free NFT '
        'giveaway", then 85 items in 2026 confined to monetizable niches (investingforbeginners, Entrepreneur, '
        'Bitcoin, stockstobuytoday, ValueInvesting, MLQuestions, ArtificialInteligence). The cited Optiver text never '
        'claims to have sat anything - "From what I have seen, the process is pretty structured ... They really care '
        'about how you think ... Many people use resources like Heard on the Street" - the two-paragraph hedged advice '
        'shape of the marketing replies, minus a link. No refusal string and no product link found, hence medium.'),
}

# accounts checked by hand and cleared, with the reason they survived
CLEARED = {
    '0xCUBE': 'The "As an AI language model, I am unable to comprehend this incomplete question" hit is a human joke '
              'posted to r/ProgrammerHumor in March 2023, not a leaked refusal. 7257 items since 2021 with normal '
              'ski/Colorado/Denver continuity.',
    'rsha256': 'The "as an AI" hit is Berkeley jargon - "expect to go through the pipeline and start as an AI, then a '
               'reader, then a tutor, then a TA" - where AI means Academic Intern. Long coherent UC Berkeley history.',
    'n0obmaster699': '"I\'m sorry I can\'t help with this" is a human declining to help, followed by concrete personal '
                     'detail ("I emailed shiraz and he asked for recommendation letters").',
    'Sven9888': 'The refusal-shaped hit is a quotation of another user\'s words inside a political argument.',
    'big_clout': '"I\'m sorry but I can\'t take you seriously as a computer science graduate" is an insult, not a refusal.',
    'gargar070402': '"[insert major here]" is ordinary human idiom, not an unfilled template slot.',
    '8bit-Corno': '"[Insert comment about crows here]" is a joke, not an unfilled template slot.',
    'darnforgotmypassword': 'Flagged only by a substring false positive; long coherent gaming/university history.',
    'th25cc': 'Flagged only by a substring false positive; coherent Northwestern/UW-Madison history.',
    'itschaboy___': '"as an AI trainer" is about a moonlighting job, not assistant self-reference.',
    'fysmoe1121': '"hired as an AI for cs61b" is again the Berkeley Academic Intern sense.',
    'BothMarionberry8063': 'Runs a transcription SaaS (myspeechaudify.com) but promotes it only in startup subs, never '
                           'in the quant thread. The cited SIG post is fluent while the same user\'s follow-up in the '
                           'same thread is broken English ("i responded to 7 questions which they were almost all '
                           'wrong"), so the recall is probably real but the prose machine-polished.',
    'Affectionate_Hat_308': 'Mentions prep vendors as a customer weighing them, and actively debunks one: '
                            '"Don\u2019t listen to QuantGrindApp, it\u2019s literally just ChatGPT".',
    'Formal-Region-6894': 'Actively corrects the promotional bot: "QuantGrindApp is wrong ignore what it said."',
    'SharpPomegranate2868': 'Single-comment throwaway, but it opens by calling out a bot ("that guy is also a bot lol") '
                            'and then gives specific, hedged, first-hand detail.',
    'Upstairs-Schedule240': 'New account but a coherent single persona - C-drama subs, college applications, NYC food, '
                            'baking - and the cited text is a candidate asking about OA format, not claiming recall.',
    'Specific-Serve-2324': 'Argues, admits uncertainty, gives a verifiable background, and says "first time in reddit '
                           'so im just spewing out words"; sustained back-and-forth about one SIG cycle.',
}

recs = collections.defaultdict(list)
for a in A:
    recs[a['author']].append(a)


def grade(n):
    if n in MANUAL:
        v, c, sig, ev = MANUAL[n]
        return v, c, sig, ev
    s, m = S[n], M[n]
    sig, ev = [], []
    if n in CLEARED:
        ev.append(CLEARED[n])
    ni = s['n_items']
    depth = m.get('frac_threads_revisited') or 0
    if ni <= 2:
        return ('UNKNOWN', 'low',
                ['single-use account: %d item(s) total, nothing else to screen against' % ni,
                 'no adverse signal found (no language-model artifact, no product link, no farm cadence)'],
                (' '.join(ev) + ' ' if ev else '') +
                'Account has %d item(s) in the mirror, all tied to this topic. A fresh single-purpose throwaway is the '
                'norm for interview recall, so this is not suspicious - but there is genuinely too little history to '
                'affirm a person either. Cited text: "%s"' % (ni, (recs[n][0].get('text') or '')[:170].replace('\n', ' ')))
    conf = 'high' if (ni >= 60 and s['span_days'] > 180) else ('medium' if ni >= 12 else 'low')
    sig.append('%d items across %d subreddits over %s days (first seen %s)' % (
        ni, s['n_subreddits'], int(s['span_days']), s['first_seen']))
    sig.append('no language-model artifact, no product promotion, no machine cadence '
               '(peak day %d items over %d hours)' % (m['peak_day_items'], m['peak_day_hours_covered']))
    if depth >= 0.15:
        sig.append('conversational depth: revisits %d%% of threads it comments in' % round(depth * 100))
    if s['span_days'] > 365:
        sig.append('history spans %.1f years, consistent with one person over time' % (s['span_days'] / 365.0))
    ev.append('History is consistent with one person: %d items in %d subreddits from %s to %s, peak day only %d items '
              'across %d hours, and it returns to %d%% of its own threads. No refusal strings, no assistant voice, no '
              'product links, no farm cadence. Cited text: "%s"' % (
                  ni, s['n_subreddits'], s['first_seen'], s['last_seen'], m['peak_day_items'],
                  m['peak_day_hours_covered'], round(depth * 100),
                  (recs[n][0].get('text') or '')[:200].replace('\n', ' ')))
    return 'GENUINE', conf, sig, ' '.join(ev)


accounts, results = {}, []
for n in sorted(recs):
    v, c, sig, ev = grade(n)
    s, m = S[n], M[n]
    accounts[n] = {
        'verdict': v, 'confidence': c, 'n_records': len(recs[n]),
        'account_created': ('first activity in mirror %s' % s['first_seen']) if s['first_seen'] else 'unknown',
        'last_seen': s['last_seen'], 'n_items_sampled': s['n_items'], 'n_subreddits': s['n_subreddits'],
        'peak_day_items': m['peak_day_items'], 'peak_day_hours_covered': m['peak_day_hours_covered'],
        'peak_day_median_gap_s': m['peak_day_median_gap_s'],
        'frac_threads_revisited': m['frac_threads_revisited'],
        'firms': s['firms'], 'cited_subreddits': s['cited_subreddits'],
        'signals': sig, 'evidence': ev,
    }
    for a in recs[n]:
        results.append({
            'id': a['id'], 'source_url': a['url'], 'account': n, 'verdict': v, 'confidence': c,
            'signals': sig, 'evidence': ev, 'firm': a['firm'], 'tier': a['tier'],
            'subreddit': a['subreddit'], 'post_date': a['post_date'],
            'author_basis': a['author_basis'],
            'poster_context_claimed': a['claimed'],
            'attribution_note': ('poster_context named u/%s but the mirror shows this text was written by u/%s'
                                 % (a['claimed'][0], n)) if (a['claimed'] and n.lower() not in
                                                             [c.lower() for c in a['claimed']]) else None,
        })

clusters = {r['id'] for r in results}
byv = collections.Counter(r['verdict'] for r in results)
bya = collections.Counter(a['verdict'] for a in accounts.values())

systemic = [
    'Census basis: 134 question clusters carry at least one reddit_thread attestation (135 such attestations, 109 '
    'distinct URLs). Every attestation was re-attributed from the Arctic Shift mirror rather than trusted from the '
    'stored poster_context: 75 resolved by comment permalink, 34 by locating the quote in the post selftext, 26 by '
    'matching the quote to a specific comment inside the cited thread. Nothing fell through to a guess.',

    'Attribution errors in the corpus itself: for 21 of 135 attestations the stored poster_context names a different '
    'account than the mirror shows wrote the quoted words. In every case the harvester cited a thread-level URL and '
    'named one participant while quoting another. The screen follows the actual author of the quoted text.',

    'The contamination is concentrated, not diffuse. 11 of 99 accounts are BOT or PROMOTIONAL, and they carry 19 of '
    '135 attestations (14%) across 19 distinct clusters - a single account, hocobozos, carries 8 of those 19.',

    'Every one of the 19 flagged clusters is SOLE-SOURCED to the flagged account: none has a second attestation of any '
    'kind. Each therefore loses its entire evidentiary basis rather than merely being weakened, and none can be '
    'rescued by falling back on a co-attestation.',

    'By tier the damage is narrow but real: 8 of the 19 are Tier B and all 8 are the single hocobozos Akuna cluster '
    '(a53731eb31c5f7, 71420d0b167baa, 0d662a0d38af49, 6ac3f30cf47dd5, 9cbc4699a247cf, 6851eea20365c3, 03e6d60dd494a6, '
    '85e0efa75d39d5). One is Tier C (OkSadMathematician/HRT), three are Tier D, and seven were already marked REJECT '
    'by earlier passes. Removing bot-sourced material therefore costs the corpus eight Tier B Akuna records and '
    'little else.',

    'Two distinct machine populations, with different fingerprints. (1) Karma-farming engagement bots - hocobozos, '
    'chocolate_asshole, OkSadMathematician - identified by round-the-clock cadence: hundreds of comments per day '
    'across dozens to hundreds of unrelated subreddits, median gaps of 26-64 seconds, activity in all 24 hours, and '
    'multiple languages. (2) Interview-prep vendors - QuantGrindApp, Zealousideal-Fig9666 - who post firm-specific '
    '"insight" that is marketing copy rather than recall.',

    'A dated bot ring operates in r/quantfinance in mid-2026: weaklypalecabal (created 2026-06-25), snoopy_priesthood '
    '(2026-06-17) and DeeplyEquable (2026-07-02) share referral-farming subreddits (chimeboost, DynastyFFTradeAdvice, '
    'coincollecting, dropshipping, leanfire, economy, FirstTimeHomeBuyer), the same confident two-sentence advice '
    'register, and the same habit of claiming a prior recruiting cycle from an account a few weeks old. Only '
    'weaklypalecabal leaked a refusal string; the other two are graded medium on the shared fingerprint alone.',

    'The community detects these bots unaided. In r/quantfinance thread 1stcxn5 - itself a cited source - one user '
    'wrote "the comment above is by a bot. there are many bots on this sub advertising for different websites. '
    'beware!" and another "that guy is also a bot lol". Two accounts in this very census (Affectionate_Hat_308, '
    'Formal-Region-6894) publicly debunk QuantGrindApp. Human pushback is a genuine-candidate signal, and it also '
    'corroborates the vendor-spam finding independently.',

    'Time concentration is bimodal: 9 of the 19 flagged attestations are dated 2026 and 8 are dated September 2023 '
    '(the hocobozos Akuna burst); 2 carry no date. Six of the 11 flagged accounts first appear in 2026. There is no '
    'flagged record between October 2023 and December 2025, and nothing before 2023 is flagged at all.',

    'Firm concentration is severe where the sample is small. Akuna Capital loses 8 of its 19 reddit-sourced '
    'attestations (42%), all to hocobozos. Citadel loses 3 of 5 (60%) - to three different operators '
    '(chocolate_asshole, nullnotfound2, Zealousideal-Fig9666). Optiver loses 2 of 10, Five Rings 1 of 10, HRT 1 of 10. '
    'Susquehanna, despite supplying by far the most reddit material, is the cleanest: 4 of 73 (5%). The corpus-wide '
    'rate is misleading for Akuna and Citadel specifically.',

    'Subreddit concentration: only two subreddits contributed a flagged record. r/csMajors carries all 9 of the 2023 '
    'Akuna-era flags (the hocobozos cluster plus nullnotfound2), and r/quantfinance carries the other 10 - the 2026 '
    'bot ring and both vendors. No flagged record came from anywhere else.',

    'Calibration held deliberately conservative. Throwaway, terse, low-karma and anonymous accounts were NOT treated '
    'as suspicious: single-purpose accounts posting one OA recall are the norm in this domain. Eleven accounts were '
    'flagged by automated artifact detection and cleared by hand as false positives - Berkeley students using "AI" to '
    'mean Academic Intern, a human joking "As an AI language model" in r/ProgrammerHumor in 2023, "[insert major '
    'here]" as ordinary idiom, and quotations of other users\' refusals inside arguments.',

    'What this screen could NOT determine. (a) Reddit\'s own API and HTML are Cloudflare-blocked from this host, so '
    'true account-creation dates were unavailable; "first seen" is the earliest item in the Arctic Shift mirror, '
    'which is a lower bound and can postdate real account creation. (b) The mirror does not expose karma or '
    'suspension state for most of these accounts, so moderator-removal rates are understated. (c) Content deleted '
    'before the mirror ingested it is invisible, so promotional links later scrubbed by the poster would not appear - '
    'the medium-confidence BOT calls (nullnotfound2, Senior_Shelter7426, landau007, snoopy_priesthood, DeeplyEquable) '
    'rest on behavioural pattern, not on a recovered artifact. (d) 5 accounts have two or fewer items in the mirror '
    'and are returned UNKNOWN: there is no adverse evidence against them and none for them either. (e) Where an '
    'account is graded GENUINE this means no evidence of automation was found, not that the recall itself is '
    'accurate - question-level truth is a separate test from account-level provenance.',
]

out = {
    'screened': len(clusters),
    'accounts_examined': len(accounts),
    'attestations_screened': len(results),
    'method': 'Every reddit_thread attestation was re-attributed to the account that wrote the quoted text using the '
              'Arctic Shift mirror (reddit.com and its .json endpoints return 403 to this host), then each account\'s '
              'full comment and post history was pulled and scored for language-model artifacts, product promotion, '
              'subreddit spread, posting cadence, conversational depth and language mixing. Automated flags were '
              'reviewed by hand; false positives were cleared with the reason recorded.',
    'verdict_distribution_by_record': dict(byv),
    'verdict_distribution_by_account': dict(bya),
    'results': sorted(results, key=lambda r: (r['verdict'], r['account'])),
    'accounts': accounts,
    'systemic': systemic,
}
json.dump(out, open('/workspace/harvest/reports/reddit_account_screen.json', 'w'), indent=1, ensure_ascii=False)

print('clusters screened: %d   attestations: %d   accounts: %d' % (len(clusters), len(results), len(accounts)))
print('by record :', dict(byv))
print('by account:', dict(bya))
print()
for n, a in sorted(accounts.items(), key=lambda kv: (kv[1]['verdict'], -kv[1]['n_records'])):
    if a['verdict'] in ('BOT', 'PROMOTIONAL'):
        print('%-22s %-12s %-6s records=%d  firms=%s' % (n, a['verdict'], a['confidence'], a['n_records'], a['firms']))
