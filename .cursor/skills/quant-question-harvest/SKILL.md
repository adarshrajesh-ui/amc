---
name: quant-question-harvest
description: Harvests real, actually-asked quant online-assessment and interview questions from first-person candidate recall posts across English, Chinese, and chat sources, then publishes them as parallel per-source streams for human triage. Every question is welded to a verbatim quote at a live URL and machine-verified against it. Use only when the user explicitly invokes /quant-question-harvest, or asks for real OA or interview questions actually asked at named firms.
disable-model-invocation: true
argument-hint: "[firm and role — e.g. SIG quant trader internship]"
---

# Quant Question Harvest

Build a corpus of **actually-asked** quant assessment questions for: $ARGUMENTS

If no target was given, default to **SIG quant trader internship**.

Every question must be traceable to a specific human who said, in public, on a dated post,
that they were asked it. Ship it as parallel per-source streams the user can scan and judge.

## The rule that governs every other rule

**You guarantee provenance. The user judges plausibility.**

The user has sat these assessments and can spot a laundered textbook problem by eye. What they
cannot do is check four hundred URLs. So the split is absolute:

- **Yours:** that a specific human posted this specific text, at this specific live URL, on this
  specific date, about this specific firm and round. Mechanically verifiable. You are held to it.
- **Theirs:** whether the question smells like the real test.

Two failure modes, opposite directions, both fatal. Hold both:

1. **Fabrication poisons everything.** One invented question found later means none of the others
   can be trusted and the whole corpus is worthless. 150 verified questions beats 500 with 80 fakes.
2. **Over-filtering is nearly as bad.** Never drop a provenance-verified question because *you*
   doubt it. Your taste is worse than the user's here. Label the doubt, sort it lower, ship it. A
   question you silently dropped is one they never got to judge.

Bias toward **wide**: many streams, high volume, every item carrying receipts, weakest clearly
labeled. Not a small pre-digested set reflecting your judgment of what they want.

## Standing prohibitions

- Never write a question you did not read at a URL you actually opened. You know a lot of quant
  interview questions from training; none of that may enter the corpus.
- Never paraphrase, clean up, or reconstruct a `source_quote`. Verbatim or absent.
- Never cite a URL you did not fetch, or invent an archive link.
- Never accept a textbook or a prep-vendor listicle as sole attestation. See §Textbook below.
- Never promote a full-time or SWE-track question into an internship or trader set.
- Never translate a Chinese source and discard the original.
- Never create accounts, join private servers, defeat logins or paywalls, or ignore rate limits.
  Blocked is a finding; guessing at the contents is fabrication.
- Never speculate about what is inside a source you could not read.

## Workflow

Track as todos. Do not skip or merge phases.

### Phase 0 — Scope contract

Write down, before searching:

- The exact **firm × role-track × level × cycle** matrix in scope. Role track is one of
  `quant_trader`, `quant_researcher`, `quant_developer`, `quant_analyst`, `data_scientist`.
  Level is one of `internship`, `new_grad`, `experienced`. These get conflated constantly and
  conflating them is the single most common way this task fails.
- Quotas. Default: 120 items for the primary target, 50 per additional Tier-A firm, 900 corpus
  total, ≥60 distinct streams, ≥40% Chinese-sourced, ≥50% from the current and prior cycle.
- The control sets (Phase 4). Mint these now and seal them so collectors cannot see them.

### Phase 1 — Process cartography

Before collecting questions, map each firm's funnel from recall posts: rounds, round names, vendor
platform, section count, questions per section, time limits, calculator policy, proctoring.

Do this first because it pays off twice — collectors learn what to search for, and adjudicators get
a consistency prior. A "SIG QT intern OA question" whose claimed format contradicts every mapped
account of that OA is probably fabricated.

One subagent per firm, all launched together.

### Phase 2 — Parallel collection

Read `references/sources.md` now. It carries the full source ecosystem, the native-language query
vocabulary, and the search craft. Do not work from memory of where questions live.

Launch in a single message. Never serially.

| Shard | Minimum parallel subagents |
|---|---|
| Primary target firm × role | 8, one per source family |
| Each additional Tier-A firm | 3 |
| Chinese platform families | 1 each, ≥10 total |
| Chat layer (Discord, Telegram, QQ/WeChat spillover) | 3 |
| Deleted-post and archive recovery | 2 |

**Chinese sources get more agents than English.** Most real recall for these firms is written in
Chinese. If Chinese yield is not several times English yield, the shard is under-worked. Shard it
per platform — one agent assigned to "cover Chinese sources" guarantees it gets skipped.

Each collector logs every query it ran and every URL it opened, including the duds. Under
`/overdrive`, double the counts above and add a second pass with different query formulations.

### Phase 3 — Normalize, cluster, tier

Read `references/record-schema.md` for the record format and controlled vocabularies.

**Cluster near-duplicates** by embedding similarity plus numeric-parameter matching, but keep every
attestation attached to the cluster — independent attestation count is the main authenticity signal,
so collapsing duplicates destroys the thing you most need.

**Tier for sort order, not as a gate:**

| Tier | Meaning |
|---|---|
| A | ≥2 independent first-person attestations, dated within three cycles, ≥1 full-text, consistent with the process map |
| B | One strong first-person attestation, rich incidental detail, dated, consistent with the map |
| C | Weak attestation — snippet-only, undated, secondhand compilation, screenshot-only, or role ambiguous |
| D | Provenance checks out but you doubt it. **Ships anyway**, with one line of doubt |

**Reject only on four mechanical failures:** no URL; the quote does not verify against the page;
sole attestation is a textbook or listicle; duplicate already counted in a cluster. Keep rejects in
`rejects/` with reasons, because over-filtering is a failure the user can only catch if visible.

**Authenticity signals** for tiering — positives: independent corroboration across platforms;
first-person incidental detail (the timer, the UI, which section they bombed); ugly specific
parameters (a 7-sided die, \$3.75, 17 boxes — real tests have ugly numbers, invented ones have clean
ones); thread replies arguing about the answer, since nobody argues about a fake question; poster
history consistent with being a candidate. Negatives: polished textbook English; no date; prep-vendor
or content-farm domain; claimed format contradicting the process map; one poster claiming perfect
recall of every firm's OA.

**Textbook contamination — the rule is about attestation, not content.** Firms do ask textbook
problems. Sole attestation is a book or listicle → reject. A dated first-person recall attests it
and it also appears in a book → keep, flag `textbook_overlap` with the book and problem number.
The corpora to check: Xinfeng Zhou *Green Book*, Crack *Heard on the Street*, Joshi *Quant Job
Interview Questions*, Mosteller, Brainstellar, and any "N quant interview questions" listicle.
Treat prep-vendor "Top 25 <Firm> Questions" pages as evidence *against* authenticity — they are
textbook problems with a firm name stapled on for search traffic.

### Phase 4 — Adversarial review and calibration

Self-reported confidence is worthless. Measure the filter.

- **Red team.** A `generalPurpose` subagent whose mandate is to *prove each question fake*: find its
  earliest appearance online, check whether the "recall" post is copy-paste from a listicle, check
  whether the poster is a prep-service marketer, check the claimed format against the process map.
  Every Tier A/B question must survive a documented attack.
- **Seeded forgeries (precision).** Inject the 20 synthetic maximally-plausible questions minted in
  Phase 0 into blind adjudication. **Gate: ≥19 of 20 rejected.** Below that, every tier assignment
  in the run is void — retier with a tightened rubric. Quote any survivor in full; it is the most
  useful diagnostic in the artifact.
- **Positive controls (recall).** Inject 20 hand-verified real questions blind. **Gate: ≥16 of 20
  admitted at Tier A/B.** Below that the filter is over-tight and is eating real questions.

### Phase 5 — Verify by execution

Nothing is verified because it looks verified.

Write and run `tools/verify_quotes.py`: for every record, re-fetch `source_url` and assert
`source_quote` appears as a normalized substring (whitespace-collapsed, unicode-normalized) of the
fetched page text. Record `http_status`, `retrieved_at`, `content_hash`. Submit every URL to the
Wayback save endpoint so evidence survives thread deletion.

**Gate: 100% of Tier A and B pass, or nothing ships.** No exceptions, no "the site changed." A quote
you cannot re-find is a quote you cannot prove you read. Where the page is genuinely gone but a
pre-existing archive snapshot carries the quote, it passes as `access: archive_only`.

Screenshot-sourced items cannot be byte-verified by definition — transcribe, mark
`access: screenshot_only`, cap at Tier C.

### Phase 6 — Deliver

Primary artifact is the **stream deck**, built for maximum questions per minute of the user's
attention.

```
streams/<firm>/<role>_<level>__<source_family>.md
```

Keep source families **separate, not merged**. Sources have characteristic reliability, so after
reading twenty items from one stream the user can judge the whole stream at once — far faster than
item by item.

Each stream opens with a five-line header (source family, firm, role, item count, date range, tier
mix), then items sorted best-first in this exact shape:

```
### Q17 · Tier B · Summer 2026 · OA section 2 (20 questions / 10 min)

<the question, exactly as reported, Chinese preserved with English underneath>

> verbatim source quote
— 1point3acres, posted 2026-01-14, retrieved 2026-02-02, full text · [link] · [archive]
  1 attestation · doubt: single poster, no corroboration found
```

Question first, evidence beneath, everything else on one line. Adjudication prose belongs in the
YAML records, never in the reading path.

Also ship:

- `TRIAGE.md` — every stream interleaved, grouped by firm then round, sorted by tier, primary target
  on top. Ends with the Phase 4 scores, the quote-gate pass rate, and 15 rejects with reasons.
- `triage.jsonl` — one row per question with a blank `human_verdict` field.
- `tools/apply_verdicts.py` — ingests filled-in verdicts and propagates them to structurally similar
  records (same source family, same collector, same poster, same signal profile), so a pass over a
  few dozen rows re-scores the whole corpus.
- `mocks/<firm>_<role>.md` — timed papers matching the real section structure and time limits from
  Phase 1, drawn from Tier A/B only.
- `solutions/` — worked answers, kept out of the question files so the corpus stays usable blind.
  Mark each `verified_by_source` or `derived_by_agent`. Where a thread argues about the answer,
  record the dispute rather than silently picking a winner.
- `SOURCES.md` — coverage per source family per firm, including every dead end and every source
  logged as blocked.

Summary leads with numbers: totals by tier, primary-target count, English vs. Chinese yield,
forgery score, control score, quote-gate pass rate. Report shortfalls in the first line, not as a
closing caveat.

## Stop conditions

- Quote gate at 100%, both calibration gates green, quotas met or the shortfall reported up front.
- A shard has been reworked twice with different query formulations and different source families
  and is still dry. Log it as genuinely empty and say whether that means no data exists or you
  could not reach it. Those are different and the user needs them distinguished.

Do not stop because you have "enough" questions. Coverage breadth is the deliverable.

## Not a harvest

These look like effort and are not. If you notice one, you have drifted.

- Writing plausible questions from memory and dressing them with citations.
- Searching only in English, only on Google, or only on page one.
- One agent assigned to "Chinese sources."
- Dropping items you find implausible instead of shipping them as Tier D.
- Burying questions under paragraphs of your own reasoning.
- Padding a thin shard with textbook problems to hit a quota.
- Reporting a collector subagent's finds without running the quote gate over them.
- Calling a corpus verified when only its formatting was checked.
