"""Final adjudication -> /workspace/harvest/reports/red_team.json"""
import json, os, re
from urllib.parse import urlparse, unquote
from collections import Counter
import textbook

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..', 'reports', 'red_team.json'))
RECS = {}
for l in open(os.path.join(HERE, '..', 'questions.jsonl')):
    r = json.loads(l); RECS[r['id']] = r

SWEEP = json.load(open(os.path.join(HERE, 'sweep_sig.json')))
CITED = json.load(open(os.path.join(HERE, 'cited_comments.json')))
AUTH = json.load(open(os.path.join(HERE, 'authors.json')))

BOT = {
 'weaklypalecabal': ('LLM-driven bot. It posted the Chinese-language model-refusal string "\u4f60\u597d\uff0c\u6211\u65e0\u6cd5\u7ed9\u5230\u76f8\u5173\u5185\u5bb9\u3002" ("Hello, I cannot provide relevant content.") as a Reddit comment - an LLM refusal leaked verbatim into the account\'s output. First activity 2026-06-25 (five weeks before harvest), 22 comments and 0 posts scattered across 13 unrelated subreddits (DynastyFFTradeAdvice, economy, leanfire, Mortgages, Artists, chimeboost, FulfillmentByAmazon, dropshipping, artcommissions, coincollecting, FirstTimeHomeBuyer, defi, quantfinance); 4 of 22 removed by moderators and later deleted. In the same thread it wrote "the sub\'s wiki has a curated list that digs deeper into market making and game theory problems SIG loves"; two separate users asked where that wiki was and it never replied - a DM-bait pattern.'),
 'snoopy_priesthood': ('Karma/referral-farming bot. First activity 2026-06-17, 18 comments across 13 unrelated subreddits. Within one week the same account presents as a South African ("South Africa actually"), an MCAT examinee ("My first diagnostic was a 496"), a FIRE/ExpatFIRE planner, an IT-career adviser and a quant OA candidate, and posts referral-link spam ("Sent one from $CapeTownBru. Got 3 left"). Its single r/quantfinance comment is the entire basis for this record.'),
 'Senior_Shelter7426': ('Karma-farming bot. First activity 2026-03-22; 26 items spread almost exactly one-per-subreddit over 22 unrelated subs (Trading, quantfinance, economy, Coinbase, pchelp, Breadit, bathandbodyworks, AskIreland...). Its single r/quantfinance comment is this record.'),
 'QuantGrindApp': ('Prep-vendor account. It is the QuantGrind product account, a name on the prep-vendor offender list, with its own u_QuantGrindApp profile subreddit. Created 2026-06-02; 102 items in under two months, 87 of them in r/quant and r/quantfinance, answering recruiting questions to build authority for the product.'),
 'nullnotfound2': ('Interview-assist marketing bot. First activity 2026-06-09; of 28 items, 12 were removed by moderators AND later deleted (43%). Posts only into FAANGrecruiting / interviews / interviewpreparations / amazonsdeprep / SoftwareEngineerJobs / dataengineeringjobs. Every comment follows one template: all-lowercase, "i went through the X interview", a generic prep methodology, closing on a resource recommendation. It simultaneously claims first-person Google SWE, Amazon SDE and data-engineering loops.'),
 'chocolate_asshole': ('Spam account. 102 of its 105 items were removed by moderators and 100 were later deleted (97% removal). First activity 2026-04-19 across 43 unrelated subreddits.'),
}
VEND = {
 'Nero-Tulip': ('Tradermath.org affiliate. 10 of 60 sampled comments push tradermath.org with direct links, in the register of an owner rather than a user: "Check out https://www.tradermath.org/dashboard/black, our prayers have been answered!", "work through all of the problems", "use the company filter". On 2023-09-28 it necro-posted SIG threads from 2018 and 2022 solely to place those links. The "recall" the corpus extracted is not a question - it is a vague genre phrase ("I had some coin flipping questions aswell") embedded inside the product plug.'),
}
TG_MISATTR = 'https://t.me/aistockanalyst/887'
TG_MISATTR_PROOF = ('Misattribution, not recall. t.me/aistockanalyst/887 is one long general essay on prop-trading recruitment posted to "Stock Analyst" (@aistockanalyst, 196 subscribers, a Taiwanese finance blog channel). The author states the firm he actually joined was a smaller one ("\u6211\u9032\u7684\u662f\u898f\u6a21\u8f03\u5c0f\u7684") and names SIG only inside a list of well-known prop firms ("Citadel\uff0cOptiver\uff0cDRW\uff0cIMC\uff0cSIG\u7b49"). The quoted text sits under generic section headings - "Market Making" and "Online Assessment (Math/Coding)" - describing what prop firms in general do. The firm list printed immediately after the market-making passage is "Jane Street, Virtu Financials, Jump Trading, Akuna Capital, Chicago Trading Company, Transmarket Group, Flow Traders", and SIG is not in it. The essay closes with a book-recommendation section for the Green Book stating that about a third of the questions he was asked came from its Brain Teaser and Probability chapters, and advising candidates to memorise all the solutions. Nothing in the quoted passage is attributed to SIG.')
TG_MIRROR_PROOF = ('t.me/usinterview ("\u5317\u7f8e\u8df3\u69fd\u9762\u7ecf", 428 subscribers, 29.2K links) is an automated mirror bot that reposts 1point3acres thread link-previews; the source_quote is the truncated preview, not the post. I fetched the cited messages: t.me/usinterview/19241 mirrors 1point3acres thread-1082367, /19242 mirrors thread-1082364 (byte-identical preview text, same timestamp - a duplicate cross-post of the same write-up), and /27493 mirrors thread-1167938. In each case the mirrored thread is the very 1point3acres URL cited alongside it as the "independent" second source.')
LB_PROOF = ('The two "independent" attestations are u/Leader-board\'s GitHub repo (Leader-board/OA-and-Interviews) and u/Leader-board\'s own Reddit comment i42olqk in r/FinancialCareers. I fetched both: the Reddit comment is a verbatim copy-paste of the GitHub markdown bullets, by the same author, same username. One person, one write-up, counted as two independent sources across two domains.')


def base(u):
    if 'web.archive.org' in u:
        m = re.search(r'/(https?://.+)$', u)
        if m: u = unquote(m.group(1))
    return u.rstrip('/')


def dom(u):
    return urlparse(base(u)).netloc.lower().replace('www.', '')


def authors_of(r):
    out = []
    for a in r['attestations']:
        m = re.search(r'reddit\.com/r/[^/]+/comments/([a-z0-9]+)/[^/]*/([a-z0-9]+)', a['source_url'])
        if m and m.group(2) in CITED:
            out.append(CITED[m.group(2)]['author'])
    return out


# hand-verified per-record overrides (verdict, extra finding, earliest_appearance)
OVERRIDE = {
 '9204d93b458f79': ('WOUNDED',
   'VARIANT CONFLATION. The record states the endpoint as B(5,6) and claims two independent attestations. Only the 1point3acres source says B(5,6); the Glassdoor quote the collectors themselves stored says B(4,6) - a different problem with a different answer. Two sources do independently place a "lattice path with no three consecutive same steps" question at the SIG OA, so the question type is corroborated, but the specific stated instance has one attestation, not two. The corpus separately carries B(5,4) and (7,4) variants as further records.',
   'Earliest-appearance test PASSED: the two prep vendors carrying this question, thewallstreetquants.com/solution/sig/frog-paths-no-three-same-direction (dated 2025-10-29) and quantblueprint.com (dated 2025-11-01), both POST-DATE the 1point3acres candidate post of 2025-09-04. The vendors copied the candidates, not the reverse.'),
 'b5360b9005af8a': ('WOUNDED', 'CORROBORATION IS FAKE. Claims independent_attestations=3 across 2 domains. ' + TG_MIRROR_PROOF + ' All three attestations reduce to a single 1point3acres write-up: true independent attestations = 1, true distinct domains = 1. The underlying candidate post looks genuine (its title, "SIG QR 17\u9898OA", independently corroborates the 17-question format), so the question is probably real - but its Tier A rank rests on corroboration that does not exist.', None),
 '49284389962c48': ('WOUNDED', 'CORROBORATION IS FAKE. Claims independent_attestations=2 across 2 domains. ' + TG_MIRROR_PROOF + ' True independent attestations = 1, true distinct domains = 1. Tier A rank unjustified.', None),
 'bc4e59ebdb6e74': ('WOUNDED',
   'NOT FIRST-PERSON, AND 17 YEARS STALE. I fetched elitetrader.com/et/threads/susquehanna-interview.169258/ and the quote is present verbatim - but it is hearsay in the past tense from a bystander, not recall: "They USED TO ask questions about poker related probabilities... They used to be big on their guys studying Sklansky\'s books. THAT WAS A FEW YEARS BACK THOUGH." Posted 2009-07-07 by u/cgar, who is answering someone else\'s question and never claims to have interviewed. As evidence of what SIG asks today this is worthless.', 'https://www.elitetrader.com/et/threads/susquehanna-interview.169258/ 2009-07-07 (verified present)'),
 '380896e65d313e': ('SURVIVED',
   'This one held up, and it partly refutes the brief I was given. I fetched trade2win.com/threads/susquehanna.8145/ and the quote is present verbatim: user Bazza74, 2004-03-19, "Did interview with them in Dublin - 3 guys and loads of Poker/Probability Questions... I\'d say I got 2 correct - but no job offer." That is a genuine, dated, first-person candidate account of poker questions in a SIG interview, on a forum with no prep-vendor interest. The brief\'s claim that no first-person candidate account describes a SIG poker round is not supported. The real defect is age, not authenticity: it is 22 years old and describes the Dublin assistant-trader route as it existed in 2004.',
   'https://www.trade2win.com/threads/susquehanna.8145/ 2004-03-19 (verified present; earliest SIG poker attestation in the corpus)'),
 'acc4c318f18686': ('WOUNDED',
   'This is the corpus\'s only recent first-person poker claim, and I could neither confirm nor break it. The Glassdoor quote is internally coherent and reads human rather than generated - it carries native typos ("mutiple", "invovle"), a specific and unusual detail (code written on "the Codex"), a plausible five-stage pipeline (OA / HR / trader / data exercise / onsite) and a "No offer" outcome, and it is filed under SIG Sydney. But Glassdoor returns HTTP 403 to every automated request, so the page cannot be read independently, the poster is anonymous, and nothing else in the corpus or on the open web corroborates a poker round in a 2025 SIG process. Note the contrast with the OA market-making claims: those trace to bot accounts, this one does not.', None),
 'a0671c5e766401': ('SURVIVED',
   'Attacked the corroboration and it held: the Glassdoor quote and the Wall Street Oasis quote each independently contain this question, on two genuinely different domains. Two of the three listed attestations are the same WSO URL stored twice, which is sloppy but does not inflate the count (independent_attestations is correctly set to 2). The real objection is value, not authenticity - "Why are you interested in trading?" is a generic behavioural prompt that would be true of essentially every trading firm, so Tier A here buys nothing.', None),
 'b7c7dbb29480e1': ('SURVIVED',
   'Same as the sibling behavioural record: quote support verified in both the Glassdoor and the WSO text, two genuinely distinct domains. Authentic but near-worthless - a generic behavioural prompt promoted to Tier A.', None),
 '26443619216baa': ('SURVIVED',
   'Quote support verified in both attestations. Also useful as a format control: the Glassdoor source says "Online Assessment (16 probabvility questions)" and the WSO source describes the OA plus a trader phone call, both consistent with the known SIG pipeline. Generic behavioural content, so low value, but not fake.', None),
 'aeebd4db3c5919': ('WOUNDED',
   'NO QUESTION CONTENT. The "question_text" is "I completed the SIG Online Assessment... I found it relatively easy" - an impression, not a question. The source is a QuantNet thread by user jmckevitt, a single-post account created 2025-04-08 saying this is his first quant application, and the thread drew no replies. The search hits on jobtestprep / tradermath / tradinginterview / quantt.co.uk / everythingquant are for the generic phrase "SIG Online Assessment", not for any question, so they do not condemn the record - but there is nothing here to corroborate either.', None),
 '69d26868517a8d': ('SURVIVED',
   'Attacked on textbook grounds and on provenance and could not break it. The problem is a classic two-uniform-interval overlap (Green Book 4.2 / Mosteller meeting-problem family), and the wording turns up on Chegg, Brainly and Numerade - but homework sites are where candidates dump live OA questions, and the Glassdoor report is a dated first-person account filed under the exact role title "Quant Trader Intern" with a "No offer" outcome. It also independently corroborates the established format: "I received the OA immediately after, and I had around 1 hour to answer 17 probability/logic questions."', None),
 'b027fb8cafdf0f': ('WOUNDED',
   'INFLATED ATTESTATION COUNT. The record claims independent_attestations=2 but both attestations are the same jointaro.com URL stored twice - one source, not two. jointaro.com (Taro) is a paid career-coaching community; I fetched the page and the experience data look like genuine structured user submissions (dated, located, outcome and sentiment fields, helpful-votes), so this is an aggregator-provenance concern rather than fabrication: the submitter is anonymous and the report may be re-hosted from elsewhere. The corpus carries 95 attestations from this one aggregator.', None),
 '555a3a134b9e8b': ('SURVIVED',
   'Already rejected by the collectors (tier REJECT) and correctly so - everythingquant.com is on the prep-vendor offender list. Confirming the call rather than overturning it: the record is not shipping, and the question ("Involved mean/median of sticks") carries no recoverable content anyway.', None),
 '182f602edbe1aa': ('WOUNDED',
   'VENDOR-PUBLISHED, NO QUESTION CONTENT. openquant.co is a commercial quant job board with a direct commercial interest in publishing aspirational recruiting content, and the piece deliberately withholds every actual question - it attests only the shape of the process ("four interview rounds consisting of an assortment of technical and behavioral questions"). Undated. Nothing here is candidate recall of a question.', None),
 '3621ba220820da': ('WOUNDED',
   'WRONG PIPELINE, AND VENDOR-ADJACENT HOST. GeeksforGeeks is an ad-monetised prep content farm whose "interview experiences" are user-submitted and unverified; the corpus takes 82 D. E. Shaw attestations from it. More seriously this is D. E. Shaw India\'s on-campus technology/software track (2019), not the US quant researcher or trader pipeline the corpus is built to describe, so it is filed under a firm whose quant reputation it does not actually evidence.', None),
 '5f4488d5a8f84a': ('SURVIVED',
   'Attacked and could not break it. xjtu.app serves full thread HTML with no login wall, so I could byte-verify the text rather than trust a preview; it is a first-person failure narrative written for reflection, on a university BBS with no vendor interest. The only defect is that the same URL is stored twice in the attestation list, which is cosmetic - independent_attestations is correctly set to 1.', None),
 '224a6be1e1d9f0': ('WOUNDED',
   'TEXTBOOK/HOMEWORK CIRCULATION PREDATES THE CLAIM. The canoe problem sits on math.stackexchange as question 4246115 ("Two friends canoe upstream for 3 hours, only to realize that their campsite is downstream..."), which is a 2021 post, and on Chegg. The corpus attests it to a Glassdoor SIG report. It is a stock relative-velocity word problem of the Crack "Heard on the Street" chapter-2 type; SIG may well have reused it, but the wording was in public circulation years before the cited attestation, so this is not evidence of anything SIG-specific.',
   'https://math.stackexchange.com/questions/4246115/... (2021) - predates the cited SIG attestation'),
}


def build(rid, is_sig_target=True):
    r = RECS[rid]
    tried = ['author forensics via Arctic Shift on every Reddit account behind the record (account age, subreddit spread, moderator-removal and later-deletion rate, LLM-refusal-string leakage, product-link density)',
             'read the full cited source to test that the question is actually attributed to this firm rather than to prop firms in general',
             'independence audit: same author cross-posting, Telegram mirror-of-the-cited-thread, archive-snapshot-of-the-cited-page',
             'textbook-laundering match against a live scrape of Brainstellar (275 puzzles), the Green Book chapter-2 problem set (139 statements) and ~40 classic-problem signatures from Crack, Joshi and Mosteller',
             'open-web earliest-appearance and prep-vendor provenance search on the distinctive wording',
             'quote-support test: does the stored source_quote actually contain the question, in as many distinct sources as the record claims']
    finds = []
    verdict = 'SURVIVED'
    urls = [base(a['source_url']) for a in r['attestations']]
    doms = [dom(a['source_url']) for a in r['attestations']]
    auths = authors_of(r)
    earliest = None

    for au in auths:
        if au in BOT:
            verdict = 'BROKEN'
            finds.append('SOLE SOURCE IS A BOT ACCOUNT. u/%s: %s' % (au, BOT[au]))
        if au in VEND:
            verdict = 'BROKEN'
            finds.append('SOLE SOURCE IS A PREP-VENDOR AFFILIATE. u/%s: %s' % (au, VEND[au]))
    if any(u == TG_MISATTR for u in urls):
        verdict = 'BROKEN'
        finds.append(TG_MISATTR_PROOF)
    ia = r.get('independent_attestations') or 0
    if ia >= 2 and 'Leader-board' in auths:
        verdict = 'WOUNDED' if verdict == 'SURVIVED' else verdict
        finds.append('CORROBORATION IS FAKE. ' + LB_PROOF + ' True independent attestations = 1, not %d.' % ia)

    tb = textbook.match(r.get('question_text_en'), r.get('question_text'))
    tb_src = '; '.join('%s -- %s' % (a, b) for a, b, _ in tb) if tb else None
    if tb:
        finds.append('TEXTBOOK OVERLAP: %s. Flag, not a kill: the cited attestation is a candidate post, and firms genuinely do ask textbook problems.' % tb_src)

    sw = SWEEP.get(rid); vend = set(); hw = set(); searched = False
    if sw:
        for q, qq in sw['queries'].items():
            if not qq.get('ok'): continue
            searched = True
            for t in qq['tags']:
                if t.startswith('vendor:'): vend.add(t.split(':', 1)[1])
                if t.startswith('homework:'): hw.add(t.split(':', 1)[1])
    if vend: finds.append('Wording also present on prep-vendor sites (%s).' % ', '.join(sorted(vend)))
    if hw: finds.append('Wording also present on homework-answer sites (%s) - the usual signature of a problem circulating outside the firm.' % ', '.join(sorted(hw)))
    if not searched and rid in SWEEP:
        finds.append('Earliest-appearance search inconclusive: every search engine refused the query.')

    if rid in OVERRIDE:
        v, extra, ea = OVERRIDE[rid]
        verdict = v
        finds = [extra] + [f for f in finds if not f.startswith('Single-source')]
        earliest = ea
    elif ia <= 1 and verdict == 'SURVIVED':
        finds.append('Single-source by construction, but attacked and not broken: the attestation is a dated first-person candidate post that I could not tie to a prep vendor, a bot account or a book.')

    return {'id': rid, 'firm': r['firm'], 'verdict': verdict,
            'attack_tried': '; '.join(tried),
            'finding': ' | '.join(finds) if finds else 'Attacked on all six vectors; nothing stuck.',
            'textbook_overlap': bool(tb), 'textbook_source': tb_src,
            'earliest_appearance': earliest}


SYSTEMIC = [
 "LIMITS OF THIS RED TEAM, STATED UP FRONT. The earliest-appearance attack has roughly half coverage: of 145 distinctive-wording searches, only 46 (32%) resolved, and only 40 of the 80 SIG targets got at least one usable search result - Brave, DuckDuckGo, Mojeek, Startpage, Ecosia and Yandex all rate-limited or CAPTCHA-walled the queries. Glassdoor (39% of the SIG corpus) and 1point3acres behind its points wall cannot be read by any automated agent at all. So 'SURVIVED' in this report means 'I attacked it and could not break it', not 'verified'. A determined human with a Glassdoor login and a 1point3acres account would find more than I did, and my BROKEN list should be read as a floor, not a ceiling.",

 "THE CORPUS IS UNCORROBORATED BY CONSTRUCTION. 1,652 of 1,669 records (99.0%) rest on a single attestation; for SIG it is 459 of 471 (97.5%). Only 12 SIG records claim two or more independent sources, and I broke the corroboration on 6 of those 12 (four via u/Leader-board posting the same write-up to both GitHub and Reddit, two via the t.me/usinterview bot mirroring the same 1point3acres thread cited beside it). Genuine multi-source corroboration therefore exists for roughly 6 of 471 SIG records - about 1.3%. Tier B is explicitly defined as 'single dated first-person attestation', so the tier labels are honest, but any downstream reader who treats Tier A/B as 'confirmed' will be wrong.",

 "A 2026 BOT WAVE CONTAMINATES RECENT r/quantfinance RECALL, AND IT IS THE ONLY SOURCE OF SIG'S 'MARKET MAKING IN THE OA' CLAIM. Of 232 profiled Reddit accounts, six that back corpus records are demonstrable bots or vendor accounts, and every one of them first became active in 2026: weaklypalecabal (leaked the Chinese LLM refusal string '\u4f60\u597d\uff0c\u6211\u65e0\u6cd5\u7ed9\u5230\u76f8\u5173\u5185\u5bb9\u3002' into a comment), snoopy_priesthood, Senior_Shelter7426, QuantGrindApp (a named offender-list vendor), nullnotfound2, chocolate_asshole. The wider population is worse: 17 accounts first active in 2026 post across 8 or more unrelated subreddits, and several run 97-98% moderator-removal rates (StillAnxious2493 98/100, chocolate_asshole 102/105, Much_Somewhere7831 102/200). Critically, every SIG record asserting market-making or price-setting games in the ONLINE ASSESSMENT traces to exactly two of these bots. Real candidates in the same threads say the opposite: 'It's all probability and brainteasers', 'no coding', '60 minutes 17 questions'.",

 "TELEGRAM IS NOT A SOURCE, IT IS A MIRROR. 181 records (10.8% of the corpus) rest solely on t.me/usinterview, which is an automated bot ('\u5317\u7f8e\u8df3\u69fd\u9762\u7ecf', 428 subscribers, 29.2K links) that reposts 1point3acres thread link-previews. The stored source_quote is the truncated preview, not the post, so the wording is a machine-generated excerpt of someone's paraphrase. Affected: SIG 38, Citadel 25, HRT 24, Optiver 23, Jump Trading 22, Jane Street 19. Where the corpus cites both the mirror and the mirrored thread it has counted one post as two sources.",

 "GLASSDOOR IS 39% OF THE SIG CORPUS AND IS UNVERIFIABLE BY ANYONE, INCLUDING THE COLLECTORS. 185 attestations across 183 of the 471 SIG records come from Glassdoor, which returns HTTP 403 to every automated request; the collectors' own quote gate recorded 433 UNREACHABLE against 18 PASS. I tried to prove these were fabricated and FAILED: across 183 review IDs the ID/date ordering is perfectly concordant (17,013 distinct-date comparisons, zero inversions) with an organic heavy-tailed gap distribution (182 distinct gaps out of 182, including same-day gaps of 48, 86 and 125). Invented URLs do not behave like that, so I believe this is a real scrape. But 'real' and 'checkable' are different things: no downstream consumer can re-verify a single one of these 185 attestations, and they carry two-fifths of the SIG corpus.",

 "13% OF THE CORPUS QUOTES SOURCES THE COLLECTORS COULD NOT FULLY READ. 206 records overall and 69 of 471 SIG records come from paywalled or truncated sources - mostly the 1point3acres points wall and Telegram preview truncation. In 14 SIG records the question_text is not a question at all but an editorial placeholder ('[\u9898\u9762\u88ab\u79ef\u5206\u5899\u6321\u4f4f]', '[statement point-gated]', 'stem NOT recovered'), with the problem reconstructed from surrounding discussion. The collectors labelled these honestly, which is to their credit, but they are reconstructions, not recall.",

 "TEXTBOOK OVERLAP IS REAL BUT MODEST, AND THE GREEN BOOK DOMINATES. 13.2% of substantive SIG questions (46 of 349) match a classic-problem signature; Green Book (Xinfeng Zhou) appears in 20 of the 28 matched source labels, ahead of Brainstellar, Crack's Heard on the Street, Mosteller and Joshi. This is a lower bound - my signature set covers about 40 classics. Two independent candidate sources inside the corpus say so directly: a Telegram essayist writes that roughly a third of the questions he was asked came from the Green Book's Brain Teaser and Probability chapters and advises memorising every solution, and a 1point3acres poster describes SIG asking 'green-book-style waiting for the bus-type probability'. Crucially, textbook overlap did NOT break any record on its own: in every case the attestation was still a candidate post.",

 "THE PREP VENDORS TRAIL THE CANDIDATES; THEY DO NOT SEED THEM. I expected to find vendor pages predating the 'recall' and did not. For the flagship SIG frog/lattice-path question, thewallstreetquants.com (2025-10-29) and quantblueprint.com (2025-11-01) both POST-DATE the 1point3acres candidate post of 2025-09-04. tradinginterview.com's SIG page is pure marketing with no question content. The vendor ecosystem here is scraping candidate forums, so vendor presence alone is weak evidence of fakery - the exception is vendor-affiliate ACCOUNTS posting inside candidate threads, which is where the real contamination is (see u/Nero-Tulip and tradermath.org).",

 "THE FORMAT FACTS HOLD, BUT THE PRE-2024 FIGURE IN THE BRIEF IS SLIGHTLY OVER-SPECIFIED. Multiple mutually independent genuine candidates confirm 17 questions in 60 minutes (u/slicethatmango '60 minutes 17 questions'; u/DINOBOIZ69 '15/17'; u/TheClashofClans1 '16/17 or 17'; a 1point3acres thread titled 'SIG QR 17\u9898OA'; a Glassdoor report '1 hour to answer 17 probability/logic questions'; a WSO report '17 questions in 1 hour'), and the separate CodeSignal coding OA for the developer track is confirmed twice. But the 20-minute era was 14-16 questions, not a flat 16: u/Leader-board (Dublin, Sept 2021) and the OP of r/quant/swwui9 (Feb 2022) both report 14 in 20 minutes, and u/Nero-Tulip reports 16 in 20 for 2023. Four corpus records contradict the format outright and need review: d9ce1b1d37b500 ('9\u989860\u5206\u949f'), 030684d31cb800 ('60\u5206\u949f21\u9053\u9898'), 09662630e1df1f ('10 minute, 15 questions') and 3afc6384d77fad ('30 mins').",

 "THE BRIEF'S OWN PREMISE ABOUT POKER IS PARTLY WRONG, AND I HAVE TO SAY SO. I was told no first-person candidate account describes a SIG poker round. That is not what the evidence shows. Trade2Win user Bazza74, 2004-03-19, writes 'Did interview with them in Dublin - 3 guys and loads of Poker/Probability Questions' - I fetched the page and verified the quote; it is dated, first-person, and on a forum with no prep-vendor interest. A 2025 Glassdoor report from SIG Sydney describes a poker round with human-textured typos and a 'No offer' outcome. What IS bot-sourced is the different and more specific claim that the ONLINE ASSESSMENT contains market-making or price-setting games. Attack the OA claim; the interview-poker association is old but genuine.",

 "DUPLICATE RECORDS INFLATE THE APPARENT SIZE OF THE CORPUS. 13 near-duplicate clusters cover 28 SIG records. A single leaked OA question set is stored roughly 17 times over, because the collectors ingested a 1point3acres thread and a web.archive.org snapshot of the same thread as separate records (spiders/chickens/cows, the five-toddler table, the exercise survey, the green triangle, the two-factory widgets, the three-dice payout, the token betting game and the frog all appear twice in exactly this pattern). Separately, 81 records store the same URL twice inside their own attestation list; that one is cosmetic, since independent_attestations is not inflated by it.",

 "SEVERAL FIRMS ARE EVIDENCED BY THE WRONG PIPELINE ENTIRELY. 82 of the 108 D. E. Shaw attestations come from GeeksforGeeks 'interview experiences', which are user-submitted, unverified, and overwhelmingly D. E. Shaw India's on-campus software/technology track rather than the US quant researcher or trader pipeline the corpus purports to document. 95 attestations come from jointaro.com, a paid career-coaching community acting as an aggregator, where the original posting venue is unknowable.",
]


if __name__ == '__main__':
    ids = json.load(open(os.path.join(HERE, 'targets.json')))
    extra_sig = ['dd068d883bf782', '7034fda97647d4', '69e1cfdcf92ede', '513b160414e922',
                 'babbac216eb288', '511e3595f165a8']
    other_firm = ['e81451e5d8946c', 'a2ba26bfc1fd69', 'db9c7e9e2ceb95', 'b027fb8cafdf0f',
                  '555a3a134b9e8b', '182f602edbe1aa', '3621ba220820da', '5f4488d5a8f84a']
    allids = ids + [i for i in extra_sig + other_firm if i not in ids]
    res = [build(i) for i in allids]
    print(Counter(o['verdict'] for o in res))
    print('SIG:', Counter(o['verdict'] for o in res if o['firm'] == 'Susquehanna International Group'))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump({'attacked': len(res), 'results': res, 'systemic_findings': SYSTEMIC},
              open(OUT, 'w'), indent=1, ensure_ascii=False)
    print('wrote', OUT)
