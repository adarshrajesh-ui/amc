#!/usr/bin/env python3
"""Adjudicate the SIG quant-trader records currently labelled level=unknown.

Decision rule, applied in this order:

1. A source that names the exact role title wins. SIG's own title taxonomy is
   documented and, critically, Glassdoor/WSO/1point3acres all keep intern-marked
   titles separate from non-intern ones, so a non-intern title is positive
   evidence against `internship`.
2. Otherwise, a first-person statement by the *same author* about the *same
   application* wins.
3. Otherwise the record stays `unknown`. Thread framing alone is never enough:
   r/quant 165049h is titled around the "FT Quant Trading OA" yet contains
   commenters who sat the identical paper for the internship, and SIG runs the
   same assessment for both pipelines.

Nothing is promoted to `internship` without evidence naming an internship.
"""
import json
import re

SRC = '/workspace/harvest/questions.jsonl'
OUT = '/workspace/harvest/reports/sig_level_resolution.json'

# --- shared documentary basis for SIG's title taxonomy -----------------------
AT_DOC = (
    'SIG\'s Assistant Trader Program is a graduate programme, not an internship: '
    'Prosple lists "SIG Assistant Trader Program" under "Opportunity type: Graduate Job '
    'or Program" with "Experience requirement: No experience required"; the UCD Career '
    'Guide describes "The Assistant Trader Program where graduates analyze trading '
    'opportunities" and separately notes "SIG offers year round internship opportunities '
    'which provide a stepping stone to becoming an Assistant Trader". Glassdoor keeps '
    '"Assistant Trader" and "Assistant Trader Intern" as separate SIG title pages '
    '(archived 2012-03-02 snapshots of both).')
QT_DOC = (
    'SIG\'s Quantitative Trading (QT) programme is its graduate programme - the Dublin '
    'listing states "Our Quantitative Trading (QT) programme is our full-time, '
    'entry-level programme" and asks for a "Soon-to-be or Recent Grad". Glassdoor lists '
    'SIG\'s intern titles separately from this one ("Trading intern (39)", "Quant trader '
    'intern (26)", "Quantitative trading intern (17)", "Summer intern (15)").')

TITLE_RULE = {
    'Assistant Trader': ('new_grad', AT_DOC),
    'Trader Assistant': ('new_grad', AT_DOC),
    'Quantitative Trader': ('new_grad', QT_DOC),
    # "Trader" is generic: it excludes an internship but does not separate a
    # graduate hire from an experienced one, so it does not resolve on its own.
    'Trader': (None, None),
}

# --- per-record findings from re-fetching the source ------------------------
OVERRIDE = {
    # WSO attestation on this same question names the level outright.
    'a0671c5e766401': ('new_grad', 'high', 'stored_metadata',
        'A second attestation on this record is a Wall Street Oasis entry filed under '
        'the exact role title "Graduate Quant Trader", Group/Division "Quantitative '
        'Trading", Philadelphia, interviewed August 2024 - the WSO permalink slug is '
        'itself /interview/graduate-quant-trader. The Glassdoor attestation\'s title '
        '"Trader" is consistent and is likewise not an intern title.',
        'https://www.wallstreetoasis.com/company/susquehanna-international-group/interview/graduate-quant-trader'),

    # --- Reddit: author states his own level for this application -----------
    'c6244f69af6545': ('new_grad', 'high', 'refetch',
        'u/Luca_I, who wrote "getting ~9 out of 16 was enough for me in Europe" about the '
        'SIG paper he sat, posted in r/quant on 2022-11-03: "I am a maths new grad from '
        'Oxford. No past internship experience. I am getting some tier 2 and tier 1 offers '
        'for quant trading and research (Europe)." That is the cycle he is recalling ("They '
        'used to be like that last year"), and "No past internship experience" rules out an '
        'internship pipeline.',
        'https://www.reddit.com/r/quant/comments/165049h/_/jycf1uf/'),

    '531a1b201a9b7c': ('new_grad', 'medium', 'refetch',
        'u/Prestigious-Way9249 describes this same SIG application in his own posts: '
        '"I had recently applied for SIG for quant trader role and finished the Math test" '
        '(2025-04-04) and, three weeks later, "I have applied for a QST at SIG, it\'s early '
        'grad role and I have finished the Online Assessment, Math Round and Cultural fit '
        'round" (2025-04-23). He was simultaneously interviewing for Amazon SDE1, a '
        'full-time role. No internship language anywhere in his history.',
        'https://www.reddit.com/r/quant/comments/1jtedsn/_/mm9kfjd/'),

    '923936f85205f3': ('new_grad', 'medium', 'refetch',
        'u/thec_oder sat this SIG phone call in the week before 2025-08-18 and his own '
        'posts from the same weeks are all full-time/new-grad hunting: "Optiver QT FT roles '
        '|| Doesn\'t Optiver hire for QT FT roles?" (2025-08-19), "Geneva Trading FT QT OA" '
        '(2025-08-25), "I could not find any new grad roles on their careers site" and '
        '"I was looking for FT QT roles" (2025-09-07).',
        'https://www.reddit.com/r/quantfinance/comments/1mu093d/_/n9fm8kk/'),

    '4829f1fca83253': ('new_grad', 'medium', 'refetch',
        'The author is the thread OP, u/awkerns: "I applied for a QR/QST position with '
        'Susquehanna. I took the OA, flied through... For background, I am a PhD candidate '
        'in statistics" (2025-08-18), and in-thread "Position is a QR/QST position. From '
        'what I can ascertain, it is in their headquarters in PA." Five weeks earlier he '
        'posted "I am finishing my PhD in the US and am looking at positions in the EU" '
        'with "a second kid on the way" - a permanent-role search, not a summer internship.',
        'https://www.reddit.com/r/quantfinance/comments/1mu093d/_/n9fgbbg/'),

    '9fa4c9fabd4562': ('new_grad', 'low', 'refetch',
        'u/BoardCardBox commented in the thread whose OP asks about "the 20min SIG FT Quant '
        'Trading OA" and who confirms "FT" in-thread, replying "Agreed" to a candidate who '
        'said "I had 16 questions on my FT OA". His own history places him as an NYU student '
        'living in the Third North first-year dorm in Aug-Sep 2020, i.e. a senior in Aug 2023 '
        'when he sat this OA. BORDERLINE: the same thread also contains intern candidates '
        '("This was for the trading internship though"), so the thread framing alone is not '
        'decisive.',
        'https://www.reddit.com/r/quant/comments/165049h/_/jybn2uk/'),

    # --- Reddit: internship, established from the author's own cycle --------
    '63ab3d9502dd95': ('internship', 'medium', 'refetch',
        'u/is_quant said he sat this assessment "a month+ ago" from 2020-11-08. The next '
        'day he posted "When does it make sense to get a Master\'s degree before moving '
        'full-time for quant trading? I have a pretty solid quant trading internship lined '
        'up this summer... (even if it\'s just for an accelerated masters at my current '
        'school)" - i.e. a currently-enrolled student in the summer-2021 internship cycle '
        'who had not yet moved full-time. His Dec-2023 comp post ("Firm: ~HRT/JS/SIG/Citadel, '
        'Role: Trader, YoE: 1") confirms he started full-time in 2022, so he was mid-degree '
        'in autumn 2020 and could not have been in a new-grad pipeline.',
        'https://www.reddit.com/r/FinancialCareers/comments/jpwdzb/_/gbm11ql/'),

    'e38c6c66689272': ('internship', 'medium', 'refetch',
        'u/csbsms sat the SIG Trading Online Assessment on 2020-08-18 ("I took it '
        'yesterday"). His own posts put him mid-degree at that point: "Software Engineering '
        'Internship at FANG or a Top Prop Shop? ... I was fortunate enough to get internship '
        'offers for software engineering at multiple FANG companies and a top prop shop" '
        '(2020-11-06, i.e. recruiting for summer 2021) and "I\'m a college senior" '
        '(2022-01-04). A student two years from graduating was recruiting for internships, '
        'not for a new-grad start.',
        'https://www.reddit.com/r/cscareerquestions/comments/icqo2t/_/g24ug3d/'),

    '58915a32eaa925': ('internship', 'low', 'refetch',
        'The only reply to this OP\'s question about "my quantitative trading assessment '
        '(SIG) (Mettl)" characterises the specific role he applied to as the intern class: '
        '"you\'re probably not gonna get the role cuz their intern class is for sure almost '
        'full by now. I heard it was already like 80%- this role has been open since April, '
        'their discovery program yielded candidates" (u/Formal-Region-6894). BORDERLINE: this '
        'is a third party\'s characterisation, not the OP\'s own; the OP never states his level '
        'and his post history contains no other level marker.',
        'https://www.reddit.com/r/quantfinance/comments/1v39kqd/'),
}

# The four Trade2Win records all sit in one thread that names the role explicitly.
T2W = ('new_grad', 'low', 'refetch',
    'Re-fetched the whole thread: it is framed throughout around SIG\'s Assistant Trader '
    'position - the OP wrote "I now have a chance to move into trading \'professionally\' '
    'through an interview I have for an \\"Assistant Trader\\" position with Susquehanna SIG" '
    'and a later poster "I have a phone interview with Susquehanna tomorrow for an assistant '
    'trader position". ' + AT_DOC + ' BORDERLINE: Trade2Win is a UK retail-trading forum and '
    'the posters describe moving into trading "professionally", so an experienced/career-change '
    'entrant into the same programme cannot be excluded; what the evidence does exclude is an '
    'internship.',
    'https://www.trade2win.com/threads/susquehanna.8145/')
for _rid in ('227c296860ea50', '380896e65d313e', 'cacf9642b26c53', 'f28f85bb2c5d38'):
    OVERRIDE[_rid] = T2W

# Why the rest stay unknown. `confidence` on an unknown row means confidence that the
# record is genuinely indeterminate: 'high' = the source carries no level information at
# all, 'medium' = there is a real lean that stopped short of evidence.
GD_TRADER = ('high',
    'Glassdoor review filed under the exact role title "Trader". That excludes an '
    'internship - Glassdoor carries SIG\'s intern titles separately and reviewers use them '
    '("Trading intern (39)", "Quant trader intern (26)", "Quantitative trading intern (17)", '
    '"Summer intern (15)", "Intern (75)") - but "Trader" is a generic title that does not '
    'separate a graduate hire from an experienced one, and the review text carries no '
    'graduation, campus or seniority marker.')
WSO_TRADING = ('high',
    'Re-fetched the WSO company interview page. The entry is filed as "Trading Interview - '
    'Prop Trading", anonymous candidate in Dublin, interviewed September 2025, applied '
    'online - no level marker, while sibling entries on the same page do carry them '
    '("Quant Trader Intern Interview - Quantitative Trading", "Trader Intern Interview", '
    '"Trading Systems Engineer Intern Interview", "internship Interview"). Absence of an '
    'intern marker is not positive evidence of a level.')
P3A = ('high',
    'The 1point3acres thread is titled "SIG Trader OA" / "[面试经验] Susquehanna OA 题 '
    '(新人求大米!!)" and the body is behind the 188-point paywall. Posters on that board do '
    'mark the level in the title when it applies - the same sig tag index carries '
    '"Susquehanna 2025 intern OA" and "SIG Quant Trader Intern 2025 OA Susquehanna" - but '
    'absence of a marker is not positive evidence, and no cycle, school year or role level '
    'is visible in the indexed fragment.')
UNKNOWN_BASIS = {
    'cc591e97228419': ('high',
        'Re-fetched the raw document from raw.githubusercontent.com and scanned it in full: '
        'it is a personal game-theory cheat-sheet ("覆盖SIG量化研究员/交易员面试中的博弈论核心考点") '
        'with no candidate, no date, no cycle and no level marker of any kind. Nothing here '
        'can ever establish a level.'),
    '7a8018367672db': ('high',
        'Re-fetched the full Elite Trader thread. The poster says only "I have a phone '
        'interview with SIG coming up" and, asked "was it for the Dublin office?", answers '
        '"No, it was for the US." No role title, no school year, no programme named.'),
    'fe3323dda05764': ('high',
        'Re-fetched the full Elite Trader thread; same poster and same absence of any role '
        'title, school year or programme. Elite Trader is a professional traders\' forum, so '
        'even the population prior is ambiguous between a graduate and an experienced hire.'),
    'bc4e59ebdb6e74': ('high',
        'Re-fetched the thread: the questioner asked about "an interview with SIG this week '
        'for a trader gig" and the reply is a veteran recalling what SIG "used to ask... '
        'a few years back". No level attaches to either party.'),
    '8ef2f85c3e5ec4': ('medium',
        'NEAR MISS. u/StatArbFinance wrote "Took the SIG one" on 2018-09-03 but never dates '
        'it. His history straddles both pipelines: "I\'m a rising senior in college currently '
        'interning in the summer" (2018-07-10) and "I\'m a senior in college and just received '
        'my full time offer for a quant role in Financ[e]" (2018-08-25). The SIG test could '
        'belong to either the internship cycle he had just finished or the full-time cycle he '
        'was in. Not established.'),
    '713c487629d5ba': ('high',
        'u/th25cc describes sitting the test in September 2018 but never states his level, '
        'and neither does the thread OP. His own thread (r/FinancialCareers 9ceux2) says only '
        '"I have to take math assessments soon for both Goldman Sachs (engineering division in '
        'Salt Lake City) and SIG (trading company in Philadelphia)". No marker in 100 items of '
        'post history around that date.'),
    'a6ae2a1a1f0bbc': ('high',
        'u/AnimalCandid823 says only "Years ago, I was asked about coin flipping..." - no '
        'date, no cycle, no role title. His post history is unrelated (medical subreddits) and '
        'contains no SIG or level marker.'),
    'f82135488935d8': ('high',
        'Same commenter and same comment as the sibling record; he generalises about SIG\'s '
        'question style without naming a role, cycle or level.'),
    '88ac27b8c499a5': ('medium',
        'NEAR MISS. u/BilindaButcherSOM wrote "16 in 20 like you" in a thread whose OP asked '
        'about "the 20min SIG FT Quant Trading OA". But that thread demonstrably mixes '
        'pipelines - u/TheOGBunnyPilot in the same thread: "did all 16 and got probably (12 or '
        '13)/16 right and got rejected. This was for the trading internship though" - and SIG '
        'runs the same paper for both, so "like you" fixes the format, not the pipeline. No '
        'level marker in 150 items of his history.'),
    '539e88ed0685bc': ('medium',
        'NEAR MISS. u/future_gcp_poweruser reads as a working professional rather than a '
        'student - he founded a sole proprietorship "nebenberuflich" (alongside his main job) '
        'and in Jan 2024 wrote "a recruiter got in touch with me and offered me a model '
        'validation position in FX Risk... The pay was considerably lower, though: 80k (in '
        'Germany)". That leans experienced, but he could equally be a finishing PhD, and his '
        'own SIG write-up ("SIG: 10 Questions and a bit more time per question") states no '
        'level. Not established either way.'),
    'b3217fb7a69ea4': ('high',
        'u/mitch_hedbergs_cat is a one-comment account comparing the Optiver and SIG screening '
        'tests from having sat both. No role, cycle or level anywhere; the thread OP is about '
        'Optiver.'),
    'a73ac695055f4d': ('medium',
        'NEAR MISS, and the signals conflict. u/n0obmaster699 wrote "SIG, DRW you name it. Got '
        'DRW FT QR Interview as well" - but "FT" there qualifies DRW, not SIG. A month later he '
        'posted "I received a Hacker Rank for Tower Research capital London QR Intern... I\'m a '
        'mathematics student". He was applying into both intern and full-time pipelines in the '
        'same season, so his SIG level cannot be read off either statement.'),
    '2abd0d2a687ae2': ('medium',
        'NEAR MISS. u/RiemannsDream did this recruiter call "a few months ago" from 2025-08-18 '
        'and was writing his PhD thesis in September 2023, so he was most likely post-PhD and '
        'in a full-time search. He never says so, and SIG runs PhD-level internships as well, '
        'so this is a lean rather than evidence.'),
    'c70f4b1f416de1': ('medium',
        'NEAR MISS. u/Sufficient_Damage_77 is a current CMU undergraduate (he answers '
        'prospective-student questions in r/cmu about the SCS curriculum and quant internship '
        'placement). The assessment is labelled "2027" and sat in June 2026, which fits either '
        'a summer-2027 internship or a 2027 graduate start; a commenter in the same thread asks '
        '"Is this for graduate roles 2027?" and gets no answer. His graduation year is never '
        'stated.'),
    '1356ec14b74889': ('high',
        'The OP states the role and the geography but never the level: "I recently completed '
        'the online assessment for a Quantitative Research role at Susquehanna" and "I applied '
        'for Australia and Ireland and i got called for the assessment in Australia". No level '
        'marker in 162 items of his history.'),
    'f92bb53e785a34': ('high',
        'u/Affectionate_Hat_308 contributes only a claimed pass bar ("70% bar (12 up) or your '
        'test is binned") and is not describing his own SIG sitting. His history shows him '
        'applying across both pipelines at once - "I am already preparing hard for the 2027 '
        'internships and grad roles for QT/QR" - so even his own level would not disambiguate.'),
    'c40ded710442bf': ('high',
        'u/Senior_Shelter7426 is answering a stranger\'s "what to expect" question and states '
        'no level; the thread OP says only "its a QT role and description didn\'t mention '
        'serious programming skill is needed". Neither party names a pipeline.'),
    'c7f0a897cee70e': ('high',
        'u/Destined5828 opens "I did this last cycle" but never says which pipeline, and the '
        'thread OP does not either. His whole visible history is 16 items with no level marker.'),
}
for _rid in ('b264409ce6e9e3', '5a2d6ae55c49ef', 'a2beb8b16aa17e', '1a4799b94f8b61',
             'd881aac67260cf', 'f50fd46b51683e', '6382f3b2c954f5', '03c9d4d4676f82'):
    UNKNOWN_BASIS[_rid] = GD_TRADER
for _rid in ('7cb1422ee7109b', '7ae652b13af2d9', 'cd68eaf4403ed0'):
    UNKNOWN_BASIS[_rid] = WSO_TRADING
for _rid in ('5471472868a46f', 'ddcfc4cdf255d7', '16c4a64340a300'):
    UNKNOWN_BASIS[_rid] = P3A
# Nero-Tulip cross-posted one debrief into three SIG threads of differing framing.
_NT = ('high',
    'u/Nero-Tulip posted near-identical debriefs of the same 2023 paper into three separate '
    'SIG threads on the same day, one of which is an internship thread ("So I just took the '
    'online assessment for SIG\'s trading (internship)") and one of which is not - so the '
    'framing of the thread he happens to be quoted from carries no information about his own '
    'pipeline. He never states his level, and 100 items of his history contain no marker.')
for _rid in ('511e3595f165a8', '513b160414e922', 'babbac216eb288', '69e1cfdcf92ede'):
    UNKNOWN_BASIS[_rid] = _NT

CAMPUS_RE = re.compile(
    r'(college or university|on.campus|career fair|through school|careers services|'
    r'college career)', re.I)


CAMPUS_PHRASE = re.compile(
    r'(I applied through college or university|Applied through college career website|'
    r'Applied through careers services|Submitted resume through school[^.]*|'
    r'[Ww]as contacted by an on-campus recruiter after a career fair|'
    r'on campus recruiting|Recruiters were present at the University career fair)')


def campus_quote(rec, pc):
    for blob in (str(rec.get('section_context') or ''), pc):
        m = CAMPUS_PHRASE.search(blob)
        if m:
            return m.group(0).strip()
    return None


def main():
    rows = [json.loads(l) for l in open(SRC)]
    tgt = [r for r in rows
           if r.get('firm') == 'Susquehanna International Group'
           and r.get('role_track') == 'quant_trader'
           and r.get('level') == 'unknown']

    results = []
    for rec in tgt:
        rid = rec['id']
        att = rec['attestations'][0]
        url = att['source_url']

        if rid in OVERRIDE:
            lvl, conf, method, basis, u = OVERRIDE[rid]
            results.append(dict(id=rid, resolved_level=lvl, confidence=conf,
                                basis=basis, method=method, source_url=u))
            continue

        pc = str(att.get('poster_context') or '')
        m = re.search(r'role title "([^"]+)"', pc)
        title = m.group(1) if m else None
        lvl, doc = TITLE_RULE.get(title, (None, None)) if title else (None, None)

        if lvl:
            cq = campus_quote(rec, pc)
            conf = 'high' if cq else 'medium'
            basis = (f'Glassdoor review filed under the exact role title "{title}". {doc}')
            if cq:
                basis += (f' The same review also records a campus application route '
                          f'("{cq}"), which rules out an experienced hire.')
            results.append(dict(id=rid, resolved_level=lvl, confidence=conf,
                                basis=basis, method='stored_metadata', source_url=url))
        else:
            conf, basis = UNKNOWN_BASIS.get(
                rid, ('high', 'No level marker found in the stored evidence or on re-fetch.'))
            method = 'stored_metadata' if att['source_type'] == 'glassdoor' else 'refetch'
            results.append(dict(id=rid, resolved_level='unknown', confidence=conf,
                                basis=basis, method=method, source_url=url))

    summary = {k: sum(1 for r in results if r['resolved_level'] == k)
               for k in ('internship', 'new_grad', 'experienced')}
    summary['still_unknown'] = sum(1 for r in results if r['resolved_level'] == 'unknown')

    out = {'examined': len(tgt), 'results': results, 'summary': summary}
    json.dump(out, open(OUT, 'w'), indent=1, ensure_ascii=False)
    print('examined', len(tgt))
    print(json.dumps(summary, indent=1))
    from collections import Counter
    print(Counter((r['resolved_level'], r['confidence']) for r in results))


if __name__ == '__main__':
    main()
