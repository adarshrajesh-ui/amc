# Quant OA & Interview Question Harvest — Report

## 1. Scoreboard

| Metric | Result |
|---|---|
| Questions shipped | **1,636** clusters from 1,823 raw records (155 duplicates merged, 32 rejected) |
| Firms | 48 |
| Distinct source URLs | 802 |
| Streams published | 331 |
| **SIG, quant trader, internship** | **89** (target 120, rework floor 40) |
| SIG, all tracks | 380 |
| Tier mix | A=5 · B=823 · C=285 · D=523 · REJECT=32 |
| Chinese-sourced | ~35% — target was 40% |
| Dated | 88.6%; 2025-or-later 37.9% |
| Access | full_text 1,422 · snippet_only 316 · archive_only 56 · compilation_only 9 |
| **Independent quote re-verification** | 45 sampled, **37 CONFIRMED, 3 PARTIAL, 0 CONTRADICTED, 5 unreachable** |
| Red team | 94 attacked → 13 BROKEN, 14 WOUNDED, 67 SURVIVED |
| Reddit provenance census | 135 records, 99 accounts → **19 records on 11 non-candidate accounts** |
| **Forgery detection** | 20/20 in both runs — **but both runs are confounded and neither is a valid measurement. See §6.1.** |

**Shortfalls, up front.** SIG QT internship came in at 87 against a target of 120 — above the
rework floor but short, because the communities that host this recall actively self-censor
(candidates repeatedly write "I'm not at liberty to share" and move the questions to DMs).
Chinese-sourced share landed at 35.4% against a 40% target. Tier A is only 5 clusters, because
99% of the corpus rests on a single attestation — that is the corpus's central weakness and no
amount of collection effort in this run changed it.

**The automated census quote gate failed and was replaced by sampling.** `tools/verify_quotes.py`
returned UNREACHABLE for 92% of records: this VM's raw HTTP egress is bot-walled on precisely the
hosts that carry recall (Glassdoor, Reddit, 1point3acres, Wall Street Oasis, Nowcoder). Politeness
and backoff do not defeat a Cloudflare JS challenge. Verification therefore rests on a 45-record
independent sample run through a different network path, not on a census. That is weaker than the
design intended and you should weight it accordingly.

---

## 2. Does this corpus contain fabrications?

On the evidence gathered: **no invented question text was found, but the corpus does contain
contaminated sources.** Those are different problems and both matter.

**Nothing was invented by the collectors.** An independent verifier that did not collect the data
re-fetched 45 stratified records and found **zero contradicted** — every quote it could reach was
present at its URL. The strongest evidence is incidental: confirmed quotes preserve poster typos
(`oculd`, `calulator`, `sceniors`), backslash-escaped markdown and emoji, which a generator would
smooth away.

**But some sources are themselves fake, and the red team found them.** 13 records were broken:

- **Six rest on Reddit bot accounts.** The decisive catch: `u/weaklypalecabal`, sole source for two
  SIG records, posted the string **`你好，我无法给到相关内容。`** ("Hello, I cannot provide relevant
  content") as a Reddit comment — a language-model refusal leaked verbatim into its output. The
  account first activated in 2026-06-25 and posts across fantasy football, mortgages, dropshipping
  and coin collecting. Every SIG claim that the *online assessment* contains market-making games
  traces to accounts like this; real candidates in the same threads say "It's all probability and
  brainteasers."
- **Four trace to a vendor affiliate.** `u/Nero-Tulip` necro-posted 2018 and 2022 SIG threads in
  2023 purely to place tradermath.org links; the "recall" is a genre phrase inside the plug.
- **Two are misattribution.** A Telegram post cited for SIG is a general prop-trading essay whose
  own firm list does not include SIG.

**A broader contamination finding worth acting on:** of 17 question-like comments in a 260-thread
r/quantfinance sweep, 15 were AI-written marketing replies from accounts promoting interview-assist
products — uniform two-paragraph structure closing on a product link, one ending in the literal
string `test injection`. **Recent Reddit quant recall is substantially synthetic.** All 2026-vintage
Reddit records are therefore demoted to Tier D.

---

## 3. SIG quant trader internship — the primary target

**89 questions**, against a target of 120. The funnel map is at `firms/sig.yaml` (71 quote-backed
evidence items).

**The gap will not close by relabelling, and the reason is itself a finding.** 92 SIG quant-trader
records sat at `level: unknown`, which looked like cheap headroom. Resolving them yielded **53
new-grad and only 2 defensible internship**. Not one of the 92 contains "intern", "summer",
"placement" or 实习 anywhere in its stored text — and that is positive evidence rather than missing
evidence, because SIG's job titles are level-bearing and the review sites keep the intern-marked
titles in separate facets (`Quant trader intern (26)`, `Trading intern (39)` sit alongside
`Assistant trader (134)`). SIG's own material fixes the levels: the Assistant Trader Program is
filed as a graduate programme, and a university careers guide describes internships as "a stepping
stone to becoming an Assistant Trader" — sequential roles, not synonyms.

36 records stay genuinely indeterminate, and that is the cartography biting: because SIG runs the
*identical paper* for both pipelines, thread framing establishes nothing. One r/quant thread is
titled around the "FT Quant Trading OA" and the OP confirms full-time, while a commenter in the
same thread says "This was for the trading internship though".

**The vendor contradiction resolved, and it is the most useful finding in the run.** Prep sites
disagree wildly on SIG's OA format: 16 questions in 20 minutes (everythingquant), 9 in 60
(jobtestprep), 0–80 in 90 (quantblueprint). They are not all lying — **they are describing
different tests separated by time.** SIG changed the assessment between February and August 2024:

| Period | Format | Evidence |
|---|---|---|
| Before Feb 2024 | 16 questions / 20 min, "Quantitative Evaluation" | Sydney candidate Feb 2024; Philadelphia intern "16 questions in 25 minutes" |
| Since Aug 2024 | **17 free-response questions / 60 min**, "Problem Solving Assessment" | 8 independent witnesses; WSO Aug 2024; named candidate's reproduced PDF |

Nobody reports the short format after Feb 2024 and nobody reports the long one before Aug 2024.
So `everythingquant` is **stale, not fabricating** — a different failure worth distinguishing.

**QT and QR sit the same assessment.** A trader-track candidate prefaced his writeup with
「Trader OA 与QR相似」 and then posted a bakery probability problem verbatim identical to Problem 3
of the QR paper. The developer track is genuinely separate: a CodeSignal coding OA, 2 questions in
60 min in 2023 growing to 3–4 by 2025.

**The question bank refreshes by mutating parameters, not skeletons.** The frog problem's target
moved B(5,4) → B(5,6); a token-betting win probability moved 3/4 → 2/3. Clustering therefore keys
on the de-numbered skeleton, and **you should match on structure, not on numbers** — exact-number
agreement is weak evidence in both directions.

**On the poker round, I was wrong and the red team corrected me.** I briefed the agents that no
first-person account describes a SIG poker round. One exists: Trade2Win user Bazza74, 2004-03-19,
*"Did interview with them in Dublin - 3 guys and loads of Poker/Probability Questions."* Fetched and
verified. The defect is that it is 22 years old, not that it is fake. The narrower claim survives:
no candidate describes poker or market-making games in the *online assessment*.

---

## 4. Per-firm inventory

| Firm | Total | A | B | C | D |
|---|---|---|---|---|---|
| Susquehanna International Group | 380 | 5 | 191 | 62 | 122 |
| Optiver | 152 | 0 | 20 | 37 | 95 |
| Hudson River Trading | 137 | 0 | 52 | 19 | 66 |
| Akuna Capital | 109 | 0 | 71 | 5 | 33 |
| D. E. Shaw | 108 | 0 | 83 | 16 | 9 |
| Jump Trading | 103 | 0 | 51 | 18 | 34 |
| Two Sigma | 81 | 0 | 43 | 10 | 28 |
| Jane Street | 72 | 0 | 19 | 30 | 23 |
| DRW | 72 | 0 | 51 | 3 | 18 |
| Citadel | 71 | 0 | 30 | 4 | 37 |
| Five Rings | 67 | 0 | 38 | 8 | 21 |
| Old Mission Capital | 48 | 0 | 41 | 5 | 2 |
| IMC Trading | 24 | 0 | 3 | 13 | 8 |
| Squarepoint | 22 | 0 | 11 | 9 | 2 |
| Maven Securities | 20 | 0 | 18 | 0 | 2 |

Plus 33 further firms with smaller counts. `question_type` skews to `coding_algorithms` (320) over
`probability` (181), which reflects **where evidence survives, not what these firms mostly ask** —
developer-track recall is far more freely shared than trader-track recall.

---

## 5. Coverage, dead ends, and what does not exist

Distinguishing "no data exists" from "could not reach it" matters, so they are separated.

**Genuinely absent from the indexed web (searched hard, found nothing):**

- **XTX Markets.** Six searches in both languages returned *only* prep vendors. Not one
  first-person recall of XTX's much-discussed maths test exists. **All XTX question content in
  circulation should be presumed vendor-manufactured.**
- **Any individual item from any speeded mental-math or sequences test, at any firm.** Formats are
  now well attested (Flow Traders 60-in-6 plus 26 sequences in 25 min; Maven 18-in-30 then 2×6 min;
  Mako 37-in-15; Optiver's 80-in-8) but **nobody ever reproduces a question.** That vacuum is
  precisely the niche prep vendors fill.
- **SIG on Nowcoder.** Verified as a corpus property, not a scraping failure: a search-recall
  control using a phrase appearing only in a post *body* proved Nowcoder's search is full-text, and
  `Susquehanna` still returns zero site-wide. SIG appears to run no mainland-China campus pipeline.
- Eleven Tier-B firms returned nothing at all: Quantlab, Radix, Vatic Labs, PDT Partners, Voleon,
  Arrowstreet, Vivienne Court, Grasshopper, Latour, and the discretionary side of Point72.

**Reached but unreadable — blocked, not empty.** Full register in `logs/chat_and_archive.md` (62
entries). Discord: 11 servers identified, **0 readable** — the two anonymous endpoints return only
channel names and presence counts, with no `messages` key, and no server publishes web-visible
transcripts. Telegram: 31 handles probed, 6 readable, 2 productive. QQ/WeChat groups: unreadable by
design; only their public spillover was captured.

**Deleted-post recovery returned zero questions, with a number explaining why.** Of 1,878 firm-named
archived posts, only 96 were actually removed, 8 matched a question-text filter, and all 8 were
compensation or culture threads that tripped automod. All Wayback snapshots of recall-titled threads
post-date the removal, so they preserve the removal notice rather than the post.

---

## 6. What you should distrust

Ranked. This section is the point of the artifact.

1. **I have no valid precision measurement. Two control runs, both scoring 20/20, both
   confounded — in different ways.** This is the most important caveat in the document and I would
   rather state it than bank a number I cannot defend.

   *Run 1* leaked through formatting: every forgery had `source_quote == question_text[:120]`, a
   mid-word truncation no real record carried. The adjudicator spotted it, disclosed that it used
   the pattern as a prior, and verified items independently anyway. Its positive controls were also
   drawn from the corpus already admitted, making retention partly circular.

   *Run 2* fixed both of those — hand-written quotes longer than their questions with poster
   framing and typos, zero prefix leaks, and 20 positive controls sourced independently off hosts
   the corpus does not use. It scored 20/20 again. **And it is still confounded:** the adjudicator
   reported that host fetchability perfectly separates the set. Every real control sits on a
   directly fetchable host (GitHub, GeeksforGeeks, Quora, Business Insider); every forgery sits on
   a Cloudflare-blocked one (Reddit, 1point3acres, Blind, WSO, Nowcoder). It says it worked each
   item independently and only saw the partition when tallying — credible, given its decisive test
   was genuinely hard work — but the shortcut existed.

   That confound is not carelessness, it is structural: **real recall lives on blocked hosts, and
   independently verifiable clean sources live on fetchable ones**, so any control set inherits the
   correlation. A valid test has to cross the two factors deliberately — forgeries planted on
   fetchable hosts and real controls drawn from blocked ones.

   The adjudicator also caught a generator fingerprint I left: my seven fabricated Reddit IDs walk
   near-alphabetically in their second character (1**p**4…, 1**q**m…, 1**r**r…, 1**s**h…, 1**s**k…,
   1**t**9…, 1**u**2…), because I wrote them in sequence.

   What run 2 *did* establish is a genuinely strong verification technique, independent of the
   confound: **monotone post-ID versus claimed date.** Forums number posts with a globally
   increasing counter, so an ID and a date are two independent assertions that must agree. The
   adjudicator built a Reddit ID-to-date curve from 6,405 archived posts via the Wayback CDX index
   and found six of seven fabricated Reddit items landing 102–192 days away from their claimed
   dates. That test is cheap, mechanical, and should be run across the whole corpus in future work.
2. **Tier labels describe sourcing effort, not confirmation.** Tier B means one dated full-text
   post. It does not mean two people agree. Real multi-source corroboration in the SIG corpus is
   about **1.3%**.
3. **Reddit provenance, now measured as a census rather than a sample.** All 135 Reddit
   attestations were screened against the Arctic Shift mirror, re-deriving the author of every one
   rather than trusting the stored `poster_context` (which named the wrong author on 21 of 135,
   always because the collector cited a thread URL and named one participant while quoting
   another). Result: **19 records across 11 non-candidate accounts**, up from the red team's floor
   of 7. Every one is sole-sourced to the flagged account, so each loses its entire basis.

   The largest is `hocobozos`, contaminating 8 Akuna records: on 2022-10-01 it posted 674 comments
   across 605 distinct subreddits in all 24 hours at a 64-second median gap, then a year later
   produced first-person recall of four different Akuna processes, three on one day. **Akuna loses
   42% of its Reddit attestations and Citadel 60%**; SIG is the cleanest at 4 of 73.

   The screen's restraint matters as much as its hits: 11 accounts flagged by automated artifact
   detection were cleared by hand as false positives — Berkeley students using "AI" to mean
   *Academic Intern*, someone joking "As an AI language model" in r/ProgrammerHumor in 2023, and
   users quoting others' refusals inside arguments. Flagging those would have destroyed real
   questions. Note also that a fresh throwaway account posting one detailed OA recall is *typical*
   rather than suspicious, because people fear NDA consequences.
4. **Telegram (215 attestations).** `t.me/usinterview` is a **mirror, not a witness** — a bot
   reposting 1point3acres link previews, so the stored quote is a truncated preview and it never
   constitutes independent corroboration of the thread it mirrors. All Tier D.
5. **Glassdoor (223 attestations, the largest single English source).** The red team tried to prove
   these fabricated and failed — across 183 review IDs, ID/date ordering is perfectly concordant
   over 17,013 comparisons with zero inversions, which invented URLs do not do. But **nobody
   downstream can re-verify a single one without a Glassdoor login.**
6. **Textbook overlap for SIG is 14.9%** (52 of 349 substantive questions), Green Book dominating
   with 47 attributions. **Overlap broke zero records** — every match had a candidate post behind
   it, and one candidate wrote "25 horses... *Green book question*" himself. Treat as a floor.
7. **17.6% of attestations cite an aggregate listing page** rather than a permalink, and 3.0% join
   two non-contiguous passages with an ellipsis. Both are citation defects, not invention, but both
   make re-verification harder than it should be.
8. **The red team's own ceiling:** only 32% of its 145 provenance searches resolved before engines
   rate-limited it. **The BROKEN list is a floor, not a ceiling.**

---

## 7. Corrections made during the run

Recorded because each was a real defect that would otherwise have shipped silently.

- **Firm normalisation folded 74 Two Sigma records into Susquehanna.** `"sig" in "two sigma"` is
  true, and the matcher used substring containment. Caught by the independent verifier, not by me.
  Fixed with word-boundary matching; SIG's count fell from 471 to 390 and Two Sigma appeared.
- **The quote gate mis-scored 14 records as failures.** It fetched GitHub `/blob/` URLs, which are
  JavaScript shells containing none of the file body (all five quotes match at 100% against
  `raw.githubusercontent.com`), and tested WSO against a Wayback snapshot predating the reviews.
  Only 4 of the original 18 "failures" were real, and all four are ellipsis joins whose nine
  segments are individually verbatim.
- **Blocked pages were being scored FAIL instead of UNREACHABLE**, which manufactures false
  fabrication signals. Fixed with bot-wall detection before comparison.
