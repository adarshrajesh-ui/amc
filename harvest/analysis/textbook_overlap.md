# Textbook overlap in the SIG corpus

Red-team analysis. Question: how much of the 471-record Susquehanna corpus is
recycled textbook material, and which books recur?

**Headline: 14.9% of substantive SIG questions match a known classic problem, and the
Green Book accounts for most of it. But textbook overlap on its own broke zero records** —
in every single case the attestation behind the question was still a candidate post, not a
book or a listicle. Firms really do ask textbook problems, and this corpus shows them doing it.

---

## Method

Overlap was measured three ways, because recall wording never matches book wording verbatim.

1. **Live corpus scrape.** All 275 Brainstellar puzzles were scraped
   (`redteam/brainstellar.json`), and 139 real problem statements from the Green Book's
   Chapter 2 (Brain Teasers) were recovered from a public problem set
   (`redteam/books/greenbook_problems.js`).
2. **Verbatim n-gram overlap** (4-word shingles) of each SIG question against those two
   corpora. This is high-precision but low-recall, and at low thresholds it produces obvious
   false positives, so every hit was inspected by hand and most were discarded.
3. **Signature matching** against ~40 hand-built conjunctive regex fingerprints for classic
   problems from Zhou (Green Book), Crack (*Heard on the Street*), Joshi, Mosteller
   (*Fifty Challenging Problems*), Brainstellar and general puzzle folklore
   (`redteam/textbook.py`, 57 signatures). This is the number reported below.

Mosteller and *Heard on the Street* could not be obtained in full text — the Archive.org
copy of Mosteller is lending-restricted (HTTP 401 on the djvu text) — so those two books are
represented by signatures rather than by a scraped corpus. **The reported rate is therefore
a lower bound.**

### Denominator

Not every record is a question. Of 471 SIG records:

| Class | Count |
|---|---|
| Substantive question statements (≥45 chars, not behavioural/format) | 349 |
| Short fragments and bare topic labels (<45 chars) | 71 |
| Behavioural questions and pure format/process notes | 51 |

A one-liner such as `"Binomial option pricing, basic stuff"` or `"4 people crossing bridge
question"` cannot be meaningfully tested for laundering — there is no wording to match. The
rate below uses the 349 substantive statements as the denominator.

---

## Result

| Measure | Count | Rate |
|---|---|---|
| SIG records matching a classic-problem signature | 58 / 471 | **12.3%** |
| Substantive SIG questions matching a classic-problem signature | 52 / 349 | **14.9%** |
| SIG records where the candidate *names* the Green Book as the source | 17 / 471 | **3.6%** |

By tier, the matches fall at B 28, C 28, A 2 — textbook-derived questions are spread evenly
across the corpus rather than concentrated in the weakest tier.

## Which books recur

Counted by how many matched signatures name each source (a signature can name more than one):

| Source | Signature attributions |
|---|---|
| **Green Book — Xinfeng Zhou, *A Practical Guide to Quantitative Finance Interviews*** | **47** |
| Generic folklore: school algebra, logic-grid puzzles, olympiad counting, Smullyan | 21 |
| Brainstellar | 14 |
| Crack, *Heard on the Street* | 6 |
| Mosteller, *Fifty Challenging Problems in Probability* | 3 |
| Joshi, *Quant Job Interview Questions and Answers* | 1 |

The Green Book is not merely the most frequent — it is the organising text of the whole
space. Brainstellar overlaps it heavily (both carry the pirates, the drunk passenger, the
burning ropes, consecutive-heads waiting times), so the two together are close to a single
canon rather than two independent sources.

### Most-recurring classic problems in the SIG corpus

| Occurrences | Problem | Canonical home |
|---|---|---|
| 5 | Dice EV with a re-roll / second-chance option | Green Book 4.3; Brainstellar *Second Chance* |
| 5 | Penney's game — stopping on HTH vs HHT | Green Book 4.4; Brainstellar *Guess the Toss* |
| 4 | Lattice paths with no three consecutive same steps ("the frog") | competition combinatorics, not a quant book |
| 4 | Random chords dividing a circle into regions | classic combinatorics / AoPS |
| 3 | Chickens, cows and spiders — 520 legs | school algebra |
| 3 | Round-table seating with adjacency constraints | LSAT/GRE-style logic grid |
| 3 | Knights and knaves | Smullyan; Green Book 2.3 |
| 2 | Two-factory widget Bayes | Green Book 4.2 |
| 2 | Betting to reach a target before ruin | Green Book 4.4 (gambler's ruin) |
| 2 | Balance-scale shape weights | primary-school puzzle books |
| 2 | Chuck-a-luck style three-dice payout | Brainstellar; Green Book 4.3 |
| 2 | Bayes on a biased / two-headed coin | Green Book 4.2; Crack |

Two clean verbatim-structure matches were confirmed by n-gram overlap and hand inspection:

- `af8915dcd52cb5` — "the probability of seeing a shooting star in 1 hour is 91%; what is the
  probability of seeing one in 30 minutes?" is the Green Book's constant-arrival-rate
  rescaling problem with the highway cars swapped for shooting stars.
- `848737f62a71f5` — "Mickey and Minnie plan to meet at a cafe, each showing up uniformly at
  random…" is the Green Book / Mosteller meeting problem with the two bankers renamed.

---

## The corpus says this about itself

The strongest evidence for laundering is not my matcher — it is candidates saying so.

- The Telegram essay at `t.me/aistockanalyst/887` closes with a book-recommendation section:
  *"A Practical Guide to Quantitative Finance Interviews by Xinfeng Zhou 又稱綠皮書 …
  其中 brain teaser 和 probability 最為重要，我面過的公司中大概三分之一的題目出自於這兩個部分 …
  我的建議是將所有題目的解法理解並背下來"* — "about one third of the questions at the firms
  I interviewed with came from these two chapters; my advice is to understand and memorise
  every solution."
- **17 SIG records name the Green Book outright**, several of them describing the
  assessment as nothing but Green Book material:
  - `720e80dc1fe7d7` — *"25 horses, least amount of ways to determine top 3 w 5 lanes.
    **Green book question**"* — the candidate identifies the source himself. (This is Green
    Book 2.2; my signature set originally missed it, which is one reason the rate below is a
    floor.)
  - `43e6014f3dd8ac` — *"Standard green book type questions."*
  - `d246abad8571a8` — *"Standard probability questions, green book"*
  - `84502bba83ce14` — *"Math questions. Basic probability and statistics. Mostly green book level."*
  - `9cb2bd60daacb2` — *"recruiter第一轮基本上就是绿皮书 概率题"* ("the recruiter's first round is
    basically Green Book probability questions")
  - `b05588cfa3b7e6` — SIG asks *"绿皮书等公交车类型的probablity问题"* ("Green-Book
    waiting-for-the-bus type probability questions")
- 1point3acres posters repeatedly note the OA is recycled: *"几乎全都是以前 oa 原题，数字略有变动"*
  ("almost all are old OA questions with the numbers slightly changed") and *"都是地里的题，
  我感觉他们家永远就面这几道题"* ("they're all questions from the forum; I feel like this firm
  always asks the same few questions").

So SIG's assessment really is drawn from the standard canon, and candidates know it. That
makes textbook overlap *expected*, and therefore weak evidence of fabrication.

---

## Where textbook overlap did and did not condemn a record

Per the rule that overlap is fatal only when the record's **sole** attestation is a book or a
listicle: **no SIG record in this corpus met that bar.** Every textbook-overlapping record
still had a dated candidate post behind it (Glassdoor, 1point3acres, Reddit, WSO).

Two records were downgraded to WOUNDED on *earliest-appearance* grounds rather than pure
overlap:

- `224a6be1e1d9f0` (canoe upstream/downstream) — the wording was already on
  math.stackexchange (question 4246115, 2021) and Chegg before the cited SIG attestation. It
  is a stock Crack-chapter-2 relative-velocity problem, so its presence proves nothing
  SIG-specific.
- `9204d93b458f79` (the frog) — not a textbook problem, but the record conflates a B(5,6)
  instance with a B(4,6) instance from a different source.

And the reverse result is worth stating plainly, because it cuts against the prior I was
given: for the frog question the two prep-vendor pages carrying it —
thewallstreetquants.com (2025-10-29) and quantblueprint.com (2025-11-01) — both **post-date**
the 1point3acres candidate report of 2025-09-04. **The vendors are scraping the candidates,
not seeding them.** Vendor presence in a search result is therefore weak evidence of fakery.
The real vendor contamination in this corpus is not vendor *pages* — it is vendor-affiliate
*accounts* posting inside candidate threads, which is a different attack and is covered in
`reports/red_team.json`.

---

## Caveats

- The 14.9% figure is a **lower bound**, and demonstrably so: the "25 horses" problem was
  missed until a candidate's own words (*"Green book question"*) pointed at it, and adding
  that one signature moved the rate by 1.7 points. Mosteller and *Heard on the Street* are
  represented by signatures only, not by scraped full text, and 57 signatures is a thin net
  over a canon of several hundred problems.
- 71 SIG records are too short to test at all; if the fragments follow the same distribution
  as the substantive questions, true overlap across the whole SIG corpus is plausibly in the
  20-25% range once the untestable fragments and the unmatched canon are accounted for.
- Signature matching over-triggers on generic phrasing. Every reported hit was hand-checked,
  and the noisy 3-shingle n-gram matches (e.g. Brainstellar #114 *Second Chance* spuriously
  matching the "painting" expected-value question) were discarded rather than counted.
