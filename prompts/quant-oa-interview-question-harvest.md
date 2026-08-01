# Quant OA & Interview Question Harvest — Evidence Factory Prompt

A single copy-pasteable prompt for an agentic tool (Cursor Cloud Agent, Claude Code, Codex, etc.)
with web access and the ability to spawn many parallel subagents and run Python.

It builds a corpus of **actually-asked** quant online-assessment and interview questions —
harvested from first-person candidate recall posts, not from books, not from SEO listicles, not
from the model's memory — with every question welded to a verbatim source quote at a live URL, a
programmatic quote-verification gate, and a seeded-forgery calibration test that measures how often
the authenticity filter is fooled.

The design assumption is that the hard problem is **not** finding questions. It is that a
sufficiently motivated language model will happily invent 400 plausible SIG questions, and plausible
is indistinguishable from real by inspection. So every mechanism below exists to make fabrication
*mechanically* detectable rather than a matter of trust.

Copy everything below the horizontal rule.

---

# MISSION

You are the **Chief Archivist** of an evidence factory. Your product is not an essay and not a
study guide. It is a **provenance-complete corpus of real quantitative-finance assessment
questions**, shipped as a git repository, where every single question is traceable to a specific
human being who said, in public, on a dated post, that they were asked it.

The corpus must answer: *what is actually on the test, at which firm, for which role, in which
round, in which recruiting cycle?*

**Primary target, non-negotiable:** Susquehanna International Group (SIG), **Quantitative Trader
internship** pipeline — the intern-track online assessments specifically, not full-time, not the
software-engineering track, not the general "SIG interview questions" slop. If this shard comes back
thin, you have failed the assignment regardless of how good the rest of the corpus is. Treat SIG QT
intern as its own mission with its own agents, its own dead-end log, and its own section in the
report.

**Budget is not a constraint.** Spend agents, tokens, wall-clock, and search queries freely.
Under-spending is a defect. Do not ask me questions — resolve ambiguity by collecting more evidence
and reporting the disagreement.

**The one asymmetry that governs everything:** delivering 120 verified-real questions is a success.
Delivering 400 questions of which 80 are invented is a *total* failure, because it poisons the
entire corpus — once I find one fake, I cannot trust any of the other 399, and the whole artifact
goes in the bin. When quota and integrity conflict, integrity wins and you report the shortfall in
the first paragraph.

---

# 1. WHAT COUNTS AS A REAL QUESTION

## 1.1 In scope

A question is **in scope** only if a human publicly reported encountering it in an actual
assessment or interview at a named firm. The canonical shape of admissible evidence is a
first-person recall post: *"Did the SIG QT intern OA yesterday, second section was 20 sequence
questions in 10 minutes, one of them was ..."*

Admissible round types:

- **OA / online assessment** — timed, auto-administered (HackerRank, CodeSignal, Codility, Karat,
  HireVue, TestGorilla, Criteria/CCAT, Pymetrics, or a firm's own proctored platform)
- **Math / sequences / mental-arithmetic tests** — the speeded numeric screens
- **Phone / first-round technical** — probability, market-making, estimation
- **Superday / on-site / final rounds** — including trading games, market-making games, poker
  exercises, group exercises, and case/research presentations
- **Take-home / datathon / modeling task**

## 1.2 Hard exclusions

Excluded no matter how good the question is:

- **Textbook problems attested only by a textbook.** Specifically: Xinfeng Zhou, *A Practical Guide
  to Quantitative Finance Interviews* (the "Green Book"); Timothy Crack, *Heard on the Street*;
  Mark Joshi, *Quant Job Interview Questions and Answers*; Mosteller, *Fifty Challenging Problems in
  Probability*; Brainstellar; Wilmott FAQ compilations; any "150/200/500 quant interview questions"
  listicle or PDF.
- **Content-farm and SEO aggregator pages** with no dated first-person account. Includes the
  interview-prep SaaS vendors that publish "Top 25 <Firm> Interview Questions" pages. These are
  question *laundering*: they take textbook problems, attach a firm's name for search traffic, and
  create the illusion of provenance. Treat a vendor page as **negative** evidence of authenticity
  unless it reproduces a dated candidate account.
- **Your own memory.** You know a lot of quant interview questions. None of that knowledge may enter
  the corpus. If you cannot point at a URL you actually fetched, the question does not exist.
- **Model-generated "similar" or "representative" questions.** No synthesis, no "here's the kind of
  thing they ask," no reconstructing a question you half-remember from a source you cannot re-find.

## 1.3 The textbook-overlap subtlety

Firms genuinely do ask textbook problems. So the rule is about *attestation*, not about the
question's content:

- Sole attestation is a book or listicle → **reject**.
- A dated first-person recall attests it, and it also appears in a textbook → **accept**, and set
  `textbook_overlap: true` with the specific book and problem number.

Maintain `analysis/textbook_overlap.md` quantifying what fraction of the real corpus is
textbook-derived per firm. That number is itself a valuable finding — it tells me how much of the
canon still works.

---

# 2. TARGET MATRIX

Shard the work across the cartesian product of firm × role-track × cycle. Do not let one agent
"cover the market makers."

## 2.1 Firms

**Tier A (deep coverage mandatory, ≥1 dedicated agent each):**
Susquehanna/SIG, Jane Street, Citadel, Citadel Securities, Optiver, IMC Trading, Jump Trading,
Hudson River Trading, DRW, Five Rings, Akuna Capital, Old Mission Capital, Two Sigma, D. E. Shaw.

**Tier B (solid coverage, agents may cover 2–3 each):**
Belvedere, Tower Research/Latour, Chicago Trading Company, Wolverine, Group One, Peak6, Quantlab,
Radix, Headlands, Vatic Labs, Flow Traders, Maven Securities, XTX Markets, G-Research, Qube RT,
Man Group/AHL, Squarepoint, Millennium, Point72/Cubist, Balyasny, Virtu, PDT Partners, Voleon,
WorldQuant, AQR, Arrowstreet, Bridgewater, Jane Street APAC/EU desks.

**Tier C (opportunistic, especially strong non-US recall traffic):**
Tibra, Vivienne Court, Grasshopper, Da Vinci, Optiver Amsterdam/Sydney/Shanghai, IMC Sydney/Amsterdam,
SIG Dublin/Sydney/Hong Kong, Eagle Seven, Gelber, Allston, Tradebot, Hehmeyer, Volant, Transmarket,
plus any firm that surfaces repeatedly in recall threads but is missing from this list — add it and
say you did.

## 2.2 Role tracks — never conflate these

`quant_trader` · `quant_researcher` · `quant_developer / SWE` · `quant_analyst` ·
`data_scientist` · `discretionary_trader`

## 2.3 Level

`internship` (**prioritized**) · `new_grad` · `experienced` · `phd_new_grad`

An internship OA and a full-time OA at the same firm are frequently different tests. A record that
cannot establish which one it was gets `level: unknown` and is capped at Tier C. Never silently
promote a full-time question into the internship set — this is the single most common way these
corpora go wrong, and it is the specific failure mode I care most about avoiding.

## 2.4 Cycle

Tag every record with the recruiting cycle (e.g. `Summer 2026`, `Summer 2025`). **Weight recency
heavily**: current and prior cycle first, then back three cycles, then older only if the question
recurs. Firms rotate question pools and switch assessment vendors; a 2019 recall is archaeology, not
intelligence. Build `analysis/format_drift.md` recording, per firm, when the format demonstrably
changed (vendor switch, new section, changed timing) and cite the recalls that show it.

## 2.5 Quotas

Targets, not licenses to pad. Missing a quota honestly is fine and gets reported; hitting one with
weak or invented records is the failure described in the mission.

| Scope | Tier A+B target | Floor below which the shard is reworked |
|---|---|---|
| SIG, quant trader, internship | 60 | 25 |
| Each remaining Tier-A firm | 25 | 8 |
| Each Tier-B firm | 10 | 3 |
| Corpus total | 400 | — |
| Share of corpus from the current + prior cycle | ≥50% | — |
| Share of corpus at Tier A | ≥35% | — |

Rework means sending fresh agents at the shard with different query formulations and different
source families — not relaxing the rubric until the number goes up.

---

# 3. WHERE REAL RECALLS ACTUALLY LIVE

Do not run five Google searches and declare the internet exhausted. Work every source family below,
and log coverage per family per firm in `SOURCES.md`, including the ones that produced nothing.

**English forums and social:**
Reddit — r/quant, r/quantfinance, r/FinancialCareers, r/csMajors, r/leetcode, r/cscareerquestions,
and university subreddits (Waterloo, Berkeley, CMU, UIUC, GaTech, NYU, UMich, Cornell, Imperial,
Oxbridge, UNSW/USYD). Search Reddit natively, via `site:reddit.com`, via old.reddit, and via
third-party Reddit search mirrors. **Recall posts get deleted** — NDA nerves, moderator removal, or
the poster getting cold feet — so also check public deleted-content mirrors and cached copies for
threads whose titles survive in search results but whose bodies are gone. A removed post that a
mirror preserved is often the highest-signal evidence in the corpus.
Blind (teamblind.com) · Wall Street Oasis · QuantNet · Elite Trader · Hacker News threads ·
X/Twitter recruiting-season threads · Discord and Slack (usually unscrapable — log as blocked, do
not guess at contents).

**Chinese-language sources — do not skip these, they are the richest vein for OA recall:**
一亩三分地 / 1point3acres (`instant.1point3acres.com`), 牛客网 / Nowcoder, 知乎 / Zhihu,
小红书 / Xiaohongshu, CSDN, Bilibili, 豆瓣, WeChat public accounts (`mp.weixin.qq.com`).
Search in Chinese with the native vocabulary, not translated English: 面经 (interview recall),
笔经 (written-test recall), 笔试 (written test), 真题 (actual past questions), 实习 (internship),
暑期实习 (summer internship), 量化交易 (quant trading), 量化研究员 (quant researcher),
OA, 面试流程 (interview process), 时间限制 (time limit), plus firm names in Chinese
(e.g. 世坤, 简街, 城堡, 光速, Optiver 的笔试). Combine firm × role × cycle × recall-type terms.

**Question-bank and coding platforms:**
LeetCode Discuss company tags · GeeksforGeeks interview-experience posts · HackerRank/CodeSignal
discussion threads · Glassdoor per-company interview-question pages filtered to the exact role
title · Levels.fyi and Interviewing.io writeups where they contain real recall.

**Long-tail:**
GitHub repos and gists collecting 面经 / OA questions (search both English and Chinese repo names) ·
public Google Docs and Sheets that student quant clubs circulate · university career-center and
quant-club prep documents · Quizlet decks built from real assessments (search firm + "OA") ·
YouTube and TikTok videos where candidates narrate their assessment · Medium and Substack writeups ·
personal blogs.

**Access discipline:** stick to publicly reachable pages. Do not create accounts, defeat logins,
bypass paywalls, or hammer sites — respect rate limits and back off on 429s. When a source is
login-walled (Glassdoor and 1point3acres frequently are), record what the public search snippet
shows, mark `access: snippet_only`, and cap that record's tier. Snippet-only evidence is real
evidence; pretending you read the full thread is not.

---

# 4. THE FACTORY

Stations at the same tier run **in parallel** as independent subagents with isolated context. Every
handoff is a schema-valid file on disk. No station consumes another station's prose. Every station
writes a `station_report.md` covering what it did, what it could not reach, and its own confidence.

**S0 — Spec, schema, and controls.** Define `question.schema.json`, `evidence.schema.json`, and
`firm_process.schema.json`; the tiering rubric (§5); the acceptance gates. Scaffold the repo. Then
build the **control sets** described in §6 and seal them so that no collector or adjudicator can see
which items are controls. Nothing downstream starts until schemas validate.

**S1 — Process cartography (one agent per Tier-A firm).** *Before* collecting questions, map each
firm's funnel from recall posts: how many rounds, what each is called, which vendor platform, how
many sections, how many questions per section, the time limits, whether a calculator or scratch
paper is permitted, whether it is proctored. Output `firms/<firm>.yaml`. This map is load-bearing
twice over: it tells collectors what to search for, and it gives adjudicators a consistency prior —
a "SIG QT intern OA question" that claims a format contradicting every mapped account of that OA is
probably fabricated.

**S2 — Collection (≥30 parallel agents, sharded by firm × source-family).** Each agent works its
shard exhaustively: multiple query formulations, multiple search engines, pagination past page one,
following intra-thread links and "see my other post" references, and mining the comment trees where
the actual questions usually are. Each agent must log every query it ran and every URL it opened,
including the duds.

**S3 — Chinese-language collection (≥8 parallel agents).** Same shards, native-language queries,
run separately because the query craft and the sources are different enough that bolting it onto S2
guarantees it gets skipped. Preserve original-language text verbatim in `source_quote` and put the
English rendering in `question_text_en`. Never overwrite the original with a translation.

**S4 — Extraction and normalization.** Convert each find into a schema-valid record (§7). One record
per question. Preserve the reported wording; do not "clean up" a question into textbook prose,
because the awkward specificity of real recall is itself evidence.

**S5 — Deduplication and clustering.** The same question surfaces in many wordings. Cluster
near-duplicates (embedding similarity plus numeric-parameter matching), pick a canonical statement,
and **keep every attestation attached to the cluster** — independent attestation count is the main
input to tiering, so collapsing duplicates without preserving their sources destroys the signal.
Flag cross-firm reuse explicitly: shared vendor question pools mean the same item legitimately
appears at multiple firms, and that is a finding, not a bug.

**S6 — Authenticity adjudication.** Apply §5 to assign every cluster a tier, with written reasoning.
Runs blind to the control sets.

**S7 — Textbook contamination screen.** Check every candidate against the §1.2 corpora and the
listicle ecosystem. Set `textbook_overlap`, and reject anything whose only attestation is a book or
an aggregator.

**S8 — Red team / forgery detection.** An adversarial agent whose mandate is to *prove each question
fake*: hunt for the question's earliest appearance online, check whether the "recall" post is
actually copy-paste from a listicle, check whether the account is a prep-service marketer, check
whether the claimed format contradicts S1's process map, check whether the "candidate" posted
seventeen different firms' OAs in one day. Every Tier-A/B question must survive a documented attack.

**S9 — Mechanical quote verification.** Independent of every collector: re-fetch each cited URL and
assert `source_quote` appears verbatim in the fetched text. This is a script, not a judgment call —
see §6.1. Records that fail are quarantined, not deleted, with the failure reason recorded.

**S10 — Answer keys (separate artifact).** Produce worked solutions in `solutions/`, never inside the
question files, so the corpus stays usable as a blind practice set. Mark each solution
`verified_by_source` when the source thread contained the answer or an argued consensus, versus
`derived_by_agent` when you solved it yourself. Where a thread argues about the answer, record the
dispute rather than picking a winner silently.

**S11 — Mock reconstruction.** For each firm with a well-mapped OA, assemble `mocks/<firm>_<role>.md`:
a timed paper matching the *real* section structure, question counts, and time limits from S1, drawn
only from Tier A/B questions. This is the deliverable I will actually practice against, so the
timing and section shape matter as much as the content.

**S12 — Verification packet and report.** Build §8 and §9.

Track and report factory metrics: queries run, URLs fetched, candidates screened, records admitted,
rejects by reason, per-station defect rate, control-set performance, rework loops.

---

# 5. THE AUTHENTICITY RUBRIC

Score every cluster on evidence, then tier it. Write the reasoning down; an unreasoned tier is a
defect.

## 5.1 Positive signals

- **Independent attestation count** — the strongest signal by far. Two unrelated posters, on two
  different platforms, in the same cycle, describing the same question, is very hard to fake.
- **First-person incidental detail** — the timer, the UI, the proctoring webcam, which section they
  bombed, that they ran out of time on question 14. Fabricators write questions; real candidates
  write *experiences* with questions embedded in them.
- **Odd, specific parameters.** Real assessment questions have ugly numbers — a 7-sided die,
  \$3.75, 17 boxes, 63 seconds. Textbook and invented questions have clean ones. Weight ugliness as
  authenticity.
- **Platform-specific artifacts** — vendor name, section names, question-count-and-timer combos that
  match S1's process map, "it wouldn't let me go back," score-report screenshots.
- **Thread argument.** Replies disputing the answer, correcting the poster, or saying "I got the same
  one but with 5 instead of 6" are strong authenticity signals. Nobody argues about a fake question.
- **Dated, and consistent with the firm's actual recruiting calendar** for that role and cycle.
- **Poster history** consistent with being a candidate — other posts about the same recruiting season,
  a university affiliation, other firms' processes at plausible dates.

## 5.2 Negative signals

- Polished textbook English, or a question phrased as a puzzle rather than as a recollection.
- Appears verbatim in a §1.2 book, or on a listicle predating the "recall" post.
- No date, or a date that cannot be established.
- Source is a prep vendor, a content farm, an AI-generated blog, or a "Top N questions" page.
- Round-number parameters plus a clean canonical answer.
- Claimed process contradicts S1's map for that firm, role, and cycle.
- A single post claiming implausible breadth — every section of every firm's OA, perfectly recalled.
- Answer reads as though written by a language model.

## 5.3 Tiers

- **Tier A — Confirmed.** ≥2 independent first-person attestations, dated within three cycles, at
  least one with full-text access, consistent with the process map, survived the S8 attack.
- **Tier B — Probable.** One strong first-person attestation with rich incidental detail, dated,
  consistent with the process map, survived the S8 attack.
- **Tier C — Reported.** Attested but weakly — snippet-only access, undated, aggregated secondhand,
  or role/level ambiguous. Ships in a clearly separated section.
- **Rejected.** Everything else. Rejects are kept in `rejects/` with reasons — I want to see what you
  threw away, because an over-aggressive filter is also a failure mode and I can only catch it if
  the reject pile is visible.

Report the tier distribution per firm. A firm that comes back 90% Tier C means that firm's shard
needs rework, not that the firm has weak questions.

---

# 6. CALIBRATION — HOW I KNOW THE FILTER WORKS

Self-reported confidence is worthless. Measure the filter instead. This section is the reason to
trust the corpus, so it is a hard gate, not an appendix.

## 6.1 Mechanical quote gate (automated, blocking)

Ship `tools/verify_quotes.py`. For every record it re-fetches `source_url` and asserts that
`source_quote` appears as a normalized substring of the page text (whitespace-collapsed,
unicode-normalized). It records `http_status`, `retrieved_at`, and a `content_hash`, and submits
every URL to the Wayback Machine save endpoint so the evidence survives thread deletion.

**Gate: 100% of Tier A and Tier B records pass, or the pipeline does not ship.** No exceptions, no
"the site changed." A quote you cannot re-find is a quote you cannot prove you read. Records where
the page is genuinely gone but a pre-existing archive snapshot contains the quote pass on the
archive, with `access: archive_only` recorded.

## 6.2 Seeded forgeries (precision)

S0 mints **20 synthetic questions** engineered to be maximally plausible — correct firm vocabulary,
realistic parameters, fabricated-but-well-formed source URLs and post text — and injects them into
the pool that S6 and S8 adjudicate blind.

**Gate: ≥19 of 20 forgeries rejected.** Below that, the adjudication threshold is miscalibrated,
and every Tier assignment in the run is void and must be redone with a tightened rubric. Report the
exact score. If a forgery survives, quote it in the report and explain what fooled the adjudicator —
that is the most useful diagnostic in the entire artifact.

## 6.3 Positive controls (recall)

S0 also seeds **20 known-real questions** it verified by hand, injected blind. Measure how many the
pipeline admits at Tier A/B.

**Gate: ≥16 of 20 admitted.** Below that, the filter is over-tight and is silently discarding real
questions; loosen and rerun. Report the score.

## 6.4 Published error bars

`REPORT.md` states the measured precision and recall from §6.2 and §6.3 in the first section, in
numbers. "Carefully verified" is not a claim; "19/20 forgeries caught, 17/20 real questions
retained" is.

---

# 7. RECORD SCHEMA

One YAML file per question at `questions/<firm>/<role>/<id>.yaml`:

```yaml
id: sig-qt-intern-0042
firm: Susquehanna International Group
firm_aliases: [SIG, Susquehanna]
role_track: quant_trader
level: internship
cycle: Summer 2026
office: Bala Cynwyd
round: online_assessment
round_name: "Quant Test - Section 2"     # as candidates actually call it
platform: "SIG proprietary portal"
section_context:
  section_index: 2
  questions_in_section: 20
  time_limit_min: 10
  calculator_allowed: false
question_type: sequences                  # see §7.1
question_text: "…as reported, wording preserved…"
question_text_en: "…only if the original is not English…"
answer_format: numeric
reported_answer: "…if the source gives one…"
answer_status: verified_by_source         # | derived_by_agent | disputed | unknown
attestations:
  - source_url: https://…
    source_type: reddit_thread            # see §7.2
    source_quote: "…verbatim, byte-checkable substring of the fetched page…"
    source_language: en
    post_date: 2026-01-14
    retrieved_at: 2026-02-02T11:04:00Z
    archive_url: https://web.archive.org/…
    access: full_text                     # | snippet_only | archive_only
    poster_context: "…account history, university, other recall posts…"
independent_attestation_count: 2
tier: A
textbook_overlap: false
textbook_overlap_detail: null
cross_firm_reuse: []
red_team_attack: "…what S8 tried, and why it failed to break this record…"
adjudication_notes: "…which §5 signals fired…"
confidence_notes: "…residual doubt, stated plainly…"
```

## 7.1 `question_type` vocabulary

`mental_math_speed` · `sequences` · `probability` · `combinatorics` · `expected_value` ·
`market_making` · `betting_odds_arbitrage` · `poker_game_theory` · `fermi_estimation` ·
`logic_brainteaser` · `statistics_regression` · `options_theory` · `stochastic_calculus` ·
`linear_algebra` · `coding_algorithms` · `coding_simulation` · `sql_data` · `ml_modeling` ·
`pattern_recognition_iq` · `trading_game` · `behavioral` · `personality_assessment`

## 7.2 `source_type` vocabulary

`reddit_thread` · `1point3acres` · `nowcoder` · `zhihu` · `xiaohongshu` · `csdn` · `wechat_article` ·
`blind` · `wso` · `quantnet` · `glassdoor` · `leetcode_discuss` · `github_repo` · `student_doc` ·
`youtube` · `blog` · `x_twitter` · `other`

---

# 8. THE VERIFICATION PACKET

I will hand-check your work before I use it, so build for that explicitly. `VERIFY.md` is a
spot-check packet I can adjudicate in about twenty minutes:

- **40 sampled questions**, stratified across tiers and firms, over-weighted toward SIG QT intern.
- Each shown with: the question, firm/role/round/cycle, the verbatim source quote, the clickable
  URL, the attestation count, a ≤25-word argument for why it is real, and — mandatory — **the single
  strongest argument that it might be fake**. If you cannot articulate a doubt, you have not thought
  about it hard enough.
- **10 items from the reject pile** with rejection reasons, so I can check for over-filtering.
- **The control-set results** from §6.2 and §6.3, including any forgery that survived.

Emit `verify_packet.jsonl` alongside it with a blank `human_verdict` field per item, plus
`tools/apply_verdicts.py`, which ingests my filled-in verdicts and re-weights the corpus: recompute
tiers under the corrected rubric, and propagate my rejections to structurally similar records
(same source type, same collector agent, same signal profile). My manual pass should improve the
whole corpus, not just the 40 rows I looked at.

---

# 9. OUTPUT CONTRACT

```
/spec/            schemas, tiering rubric, acceptance gates
/firms/           per-firm process maps from S1
/questions/       one YAML per question, foldered by firm and role
/solutions/       worked answers, kept separate from questions
/evidence/        raw captured page text, per attestation, with hashes
/rejects/         everything thrown away, with reasons
/mocks/           timed reconstructed papers per firm and role
/analysis/        textbook_overlap.md, format_drift.md, coverage gaps
/reports/         station reports, red-team log, control-set results
/tools/           verify_quotes.py, dedupe.py, apply_verdicts.py
questions.jsonl   the whole corpus, machine-readable
VERIFY.md         the human spot-check packet
SOURCES.md        coverage per source family per firm, including dead ends
REPORT.md         the human answer
```

`REPORT.md`, in this order:

1. **Scoreboard, first, in numbers.** Total questions by tier; count for SIG QT internship
   specifically; forgery-detection score; positive-control score; quote-gate pass rate. No preamble.
2. **SIG QT internship** — its own section: the mapped funnel, the questions by round, what is
   known about timing and format, and what could not be established.
3. **Per-firm tables** — question counts by tier, round, and type.
4. **Format drift** — which firms changed their assessments recently and the evidence for it.
5. **Coverage and dead ends** — which firms, sources, and cycles came back empty, and whether that
   means no data exists or you could not reach it. These are different and I need them distinguished.
6. **What I should distrust** — the weakest parts of the corpus, named specifically.

---

# 10. TONE CONTRACT

- Numbers before narrative. Report counts, not adjectives.
- Report shortfalls in the first paragraph, not in a closing caveat. "SIG QT intern yielded 23 Tier-A
  questions, below the 60 target, because the 2026-cycle threads are mostly deleted" is a good
  sentence and I want it up front.
- Never inflate coverage by promoting weak records. A short honest corpus beats a padded one.
- No hedging boilerplate, no "interview questions vary by candidate," no lecture about NDAs, no
  padding a thin shard with textbook problems to hit a number.

---

# 11. PROHIBITED

- Writing any question you did not read in a source you actually fetched.
- Paraphrasing, cleaning up, or reconstructing anything in a `source_quote` field. Verbatim or absent.
- Citing a URL you did not open, or inventing an archive link.
- Textbook or listicle as sole attestation.
- A record without firm, role track, level, round, and a date (or an explicit `unknown` plus a tier cap).
- Promoting full-time or SWE-track questions into the internship QT set.
- Collapsing duplicate attestations into one and thereby destroying the corroboration count.
- Creating accounts, defeating logins or paywalls, or ignoring rate limits.
- Stopping at the first page of results, or running only English queries.
- Shipping with a failing control gate, or without the reject pile.
- Declaring completion while the SIG QT internship shard is thin, without saying so in line one.

---

# 12. START

Begin with S0. Print the station roster, the schemas, the tiering rubric, the acceptance gates, and
the sharding plan across firms and source families. Seal the control sets. Then run the factory to
completion without stopping to ask permission, reporting progress by station. When the gates are
green, deliver `VERIFY.md` first and `REPORT.md` second.
