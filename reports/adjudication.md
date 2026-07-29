# Adjudication of disputed effect estimates

Station: quality assurance, final authority. Blinding lifted. Every verdict below rests on a source
I retrieved in this session; every quote is verbatim from that retrieval. Machine-readable verdicts:
`data/adjudicated_effects.json`.

**Headline: 8 of the 9 disputes were caused by our own task specification, not by the
literature.** Only `huang2016::2` is a genuine source failure. One real source defect exists
(`lo2016` prints Cohen's d on two scales in one sentence) but it did not cause the disagreement —
Team 1 had already caught and corrected it. Fix the codebook; do not discount the literature.

## Retrieval log

| study | identifier | retrieved | completeness |
|---|---|---|---|
| lo2016 (J Sleep Res) | PMID 27291639 / PMC5324680 | Europe PMC full-text XML | full, incl. footnotes |
| lo2016 (Sleep 39(3)) | PMID 26612392 / PMC4763363 | PMC HTML | full text; publisher blocks XML/PDF |
| huang2016 | PMID 27253768 / PMC4989257 | PMC HTML | full text **except Table 2, which is image-only** |
| rabat2016 | PMID 27242464 / PMC4876616 | Europe PMC full-text XML | full, incl. Table 1 |
| dama2025 | PMID 40129277 / PMC11948252 | PMC HTML | full text |
| koyama2022 | PMID 35609056 / PMC9129010 | Europe PMC full-text XML | full |
| klingenberg2013 | PMID 23814346 / PMC3669075 | NCBI efetch abstract | abstract only; decisive sentence is in the abstract |
| huang2023 | PMID 36859313 / PMC9979412 | Europe PMC full-text XML | full, incl. Table 2 |
| zitting2018 | PMID 30038272 / PMC6056541 | Europe PMC full-text XML | full |

Nothing below is inferred from a source I could not open. The one item I could not verify is the
numeric content of huang2016 Table 2 (see A2); that gap is stated where it bites.

---

# Part A — magnitude disputes

## A1. `lo2016::1` — prioritization benefit, control arm

**VERDICT: `CORRECT_VALUE: +0.484`, scale `cohens_d` interpreted as within-subject `d_z`** (SE 0.208,
95% CI 0.08 to 0.89, n = 26, paired). Team 1 was right; its 0.48 is correct to two decimals.

**This was never a magnitude disagreement.** The task id `lo2016::1` is not unique. Three evidence
records share `study_id: lo2016`:

- `evidence/s03_memory_consolidation/lo2016.yaml` — Lo, Bennion & Chee, *J Sleep Res* 2016;25(6):664-672,
  DOI 10.1111/jsr.12424, PMID 27291639. Effect 1 = prioritization benefit, control arm, d = 0.48.
- `evidence/s01_cognition_dose_response/lo2016.yaml` and `evidence/s02_cognition_meta/lo2016.yaml` —
  Lo, Ong, Leong, Gooley & Chee, *Sleep* 2016;39(3):687-698, DOI 10.5665/sleep.5552, PMID 26612392.
  Effect 1 of the s01 record = PVT lapses, g = 2.399.

`src/make_blind_sample.py` keys both the task file and the truth file on `study_id::effect_index`, so
the truth row for `lo2016::1` came from the s03 record while the task handed to Team 2 carried the
*Sleep* 39(3) citation, DOI, PMID and the construct `pvt_lapses`. Team 2 extracted PVT lapses from a
different paper and its −2.399 was then differenced against a memory-consolidation d. The "6-fold
discrepancy" is an id collision.

### The source defect underneath it (real, and worth the finding)

The disputed sentence, verbatim (DOI 10.1111/jsr.12424, PMID 27291639):

> "the benefit of prioritization on memory was greater 1 week after encoding relative to initially
> only for the control group (t(25) = 2.47, P = 0.021, d = 0.99), and not the SR group
> (t(29) = 1.45, P = 0.16, d = 0.26; Fig. 3)."

Both statistics come from **paired** t-tests, but the two printed d values are on different scales.
Every printed d in the paper except the SR-arm one equals `2t/sqrt(df)` — the equal-n
*independent-groups* conversion — while the SR-arm 0.26 equals `t/sqrt(n)`, i.e. `d_z`:

| contrast | t (df) | printed d | 2t/sqrt(df) | d_z = t/sqrt(n) |
|---|---|---|---|---|
| HL vs nHL, initial | 4.99 (55) | 1.35 | 1.346 | 0.667 |
| HL vs nHL, 1 week | 6.28 (55) | 1.69 | 1.694 | 0.839 |
| HL vs nHL, 6 weeks | 5.56 (44) | 1.68 | 1.676 | 0.829 |
| forgetting, initial→1 wk | 7.98 (55) | 2.15 | 2.152 | 1.066 |
| forgetting, 1 wk→6 wk | 8.53 (44) | 2.57 | 2.572 | 1.271 |
| prioritization benefit, all subjects | 2.77 (55) | 0.75 | 0.747 | 0.370 |
| **prioritization benefit, control arm** | **2.47 (25)** | **0.99** | **0.988** | **0.484** |
| **prioritization benefit, SR arm** | **1.45 (29)** | **0.26** | 0.539 | **0.265** |
| prioritization benefit, 6 wk vs 1 wk | 0.40 (44) | 0.069 | 0.121 | 0.060 |

So the headline contrast "control d = 0.99 versus SR d = 0.26" compares a between-groups-style d
against a within-subject d_z and overstates the difference by a factor of ~2. (The last row matches
neither formula — a third internal inconsistency.) On one consistent scale the contrast is
0.484 versus 0.265, a difference of 0.220, which is what the paper's own null three-way interaction
already implied: F(2,42) = 0.90, P = 0.41, eta_p^2 = 0.041. `d_z` is the right scale here because
the construct is a paired within-arm change over a week.

Team 2's −2.399, judged on its own terms (the *Sleep* 39(3) paper), is also not defensible. Verbatim
(DOI 10.5665/sleep.5552, PMID 26612392):

> "To quantify the local effect size of partial sleep deprivation on each measure, we used a similar
> statistical model but excluded the recovery days to compute Cohen f2 of the group x day
> interaction." … "The SART was less sensitive (f2 = 0.20) than the PVT (f2 = 1.48; Figure 3)."

`d = 2*sqrt(f2)` presumes a one-way fixed-effects two-group design where `f = d/2`. Here f² is a
PROC MIXED *local* effect size for a group × day interaction across 10 days and 3 daily batteries
with a baseline covariate. The conversion does not hold.

**Cause: task specification / tooling (non-unique `task_id`), plus a genuine source defect
(two d scales in one sentence) that the source caused but did not drive this dispute.**

**Companion fix required, outside the dispute:** `s01_cognition_dose_response/lo2016.yaml` effect 1
carries `value: +2.399` with `direction_note: "positive = worse vigilance"`, which violates the
canonical convention (more lapses = worse ⇒ must be −2.399), and carries `quote: null` while being
figure-digitized, violating extraction hard-rule 2. Its magnitude is at least corroborated: figure
digitisation (15.84 lapses / SD_pooled 6.51 = 2.433) and the f² route (2*sqrt(1.48) = 2.433) agree,
though both are approximate. See `collision_records` in the JSON.

## A2. `huang2016::2` — spacing × TIB interaction

**VERDICT: `EXCLUDE` — no defensible Hedges' g is extractable.** Neither team was right.

What the paper actually reports for this interaction, verbatim (DOI 10.5665/sleep.6092,
PMID 27253768):

> "After spaced items and massed items were studied an equal number of times, there was a significant
> interaction between study spacing and TIB (LR chi2 = 8.40, P < 0.01), whereby sleep restriction was
> associated with a significant decrease in cued recall performance on massed items (indicated by the
> red asterisk, P < 0.05), but not on spaced items." (Figure 2 caption)

> "There was a significant interaction between study spacing and TIB for sleep (Table 2), such that
> test performance on massed items was poorer in individuals who underwent sleep restriction
> (Tukey test, P < 0.001), while test performance on spaced items was similar between sleep groups
> (Tukey test, P = 0.80; Figure 2B)."

No Cohen's d, no g, no cell means, no SDs. The model is a 4-factor ANOVA/GLM (TIB and order
between-subjects; spacing and session within-subject) fitted by likelihood ratio. Team 2's claim that
Table 2 is supplied only as an image is correct, and I could not retrieve its numeric contents:
PMC renders it as an image and the publisher blocks XML and PDF retrieval (OUP and PMC PDF endpoints
both returned HTML challenge pages from this environment). Team 1's quoted eta² = 0.020 is therefore
**unverified**, though it is consistent with the paper's own chi²-to-eta² scaling elsewhere in the
same model family: "there was a significant interaction between Set and TIB (LR chi2 = 8.48,
P = 0.037, eta2 = 0.017)".

The two conversion routes disagree by 2.7×:

| route | arithmetic | g |
|---|---|---|
| Team 1, eta² | d = 2*sqrt(0.020/0.980) = 0.2857; J = 0.986 | **0.282** |
| Team 2, LR chi² | z = sqrt(8.40) = 2.898; d = z*sqrt(1/30+1/26) = 0.7766; J = 0.986 | **0.766** |

Both are invalid, for different reasons. The LR chi² is computed across 3 test sessions × 2 spacing
levels, so its effective sample size far exceeds 56; treating sqrt(chi²) as a 56-subject between-group
z inflates d. eta² in a multifactor mixed model is a partial variance share, not a two-group SMD, and
deflates it. Decisively, the target quantity is an **interaction** — a difference of within-subject
difference scores — and the standardising SD for that difference is never reported. A g here would be
a number with no denominator.

If the factory needs a number from this study, re-scope the construct to the simple effect (massed
items, 5 h vs 9 h TIB, at a stated retention interval) and digitise Figure 2B, which does show
mean ± SEM, with `from_figure: true`. That is a different construct and must be renamed.

**Cause: the source (no SMD-convertible statistic, image-only table), with a secondary specification
failure — the codebook mandated `hedges_g` for an interaction construct and offered neither a
sanctioned conversion nor a "not extractable" escape hatch, so both teams invented one.**

## A3. `rabat2016::0` — KSS "plateaus between day 4 and day 7"

**VERDICT: `RECODE`.** The construct as named is not an effect size; it is a claim about the shape of
a time course. Neither team's number answers it, because there is nothing there to answer.

Primary source, Table 1 verbatim (DOI 10.3389/fnbeh.2016.00095, PMID 27242464; columns are
Baseline B2, SR1, SR4, SR7, Recovery R3, R13; `###` = p < 0.001 vs B2):

> "Daily score 3.22 ± 0.31 3.82 ± 0.32 4.66 ± 0.31### 4.73 ± 0.43### 2.85 ± 0.42 2.92 ± 0.40"

and the authors' own reading of it:

> "Under such sleep restriction conditions, we observed that subjects felt sleepy from the 4th day
> until the last day and this subjective complaint seems to rapidly ceil at a score of 5."

Recode into two records, replacing the one:

1. `kss_sleepiness_day7_vs_baseline` — `hedges_g = −1.082`, SE ≈ 0.44, n = 12.
   SD from SEM×sqrt(12): B2 = 1.074, SR7 = 1.490; SD_pooled = 1.299; d_av = 1.51/1.299 = 1.163;
   within-subject small-sample correction J = 1 − 3/(4(n−1)−1) = 0.930 ⇒ g = 1.082. Negative because
   higher KSS = sleepier = worse. SE is an independent-groups approximation and therefore
   conservative; the paper reports no pre-post correlation. **This is the quantity both teams
   actually extracted.**
2. `kss_plateau_day4_to_day7` — `raw_units`, unit "KSS points, SR7 minus SR4", `value = +0.07`
   (4.73 − 4.66; g = 0.05). Morning KSS is 5.38 at both SR4 and SR7 (exactly zero change); evening
   KSS moves 4.17 → 4.00, i.e. the other way, and was never significant (p > 0.28 at SR4, p > 0.06 at
   SR7). Not poolable as a harm effect — it is a kinetics descriptor and should be flagged
   `poolable: false`.

On the magnitude: Team 1's 1.123 applied the between-groups correction (df = 2n−2) to a paired design;
Team 2's 1.08 used the within-subject correction (df = n−1), which is right for d_av. Team 2 also had
the canonical sign right. Team 1 was right about what matters scientifically (the plateau is the
finding) but recorded it in a `hedges_g` slot that cannot express it.

**Cause: task specification. The construct name encodes a time-course shape while the schema mandates
a standardised mean difference. The source reports everything needed, clearly.**

---

# Part B — sign-convention disputes

Canonical convention applied throughout: **negative = subject worse off, positive = subject better
off** for continuous outcomes; for `log_rr`/`log_hr`/`log_or`, **positive = elevated risk**.

The convention exists — `spec/gates.md` line 28: *"Effect sign: negative = worse for the subject on
cognition/health scales; log-scale ratios positive = elevated risk. Every record must state
`direction_note`."* — but it appears **only** in the QA gate document. It is absent from
`spec/EXTRACTION_INSTRUCTIONS.md`, the document extractors are told to read before doing anything,
and absent from the re-extraction task schema, which carries `target_unit` but no direction field.
That omission accounts for B2, B3, B4 and the B6 class. The remaining two, B1 and B5, come from a
second gap in the same rule: it says nothing about contrasts that are not between sleep conditions,
so it cannot be applied to them at all.

## B1. `dama2025::2` — depression severity in DSWPD

**VERDICT: `EXCLUDE`. The canonical convention does not apply.** `canonical_sign_applies: false`.

Verbatim (DOI 10.1177/07067437251328308, PMID 40129277):

> "Two studies were suspected to largely contribute to the heterogeneity in the model, since both of
> them used predefined cut-off values for their depression measures to exclude participants from their
> study samples. As a part of a sensitivity analysis, we removed these two studies from the model.
> DSWPD status continued to have a significantly large effect on depression severity but now without
> any heterogeneity in the model (N: 14 estimates, 612 participants (DSWPD: 327 participants;
> non-DSWPD: 285 participants), Cohen's d = 1.02, 95% CI [0.85-1.19], I2 = 0%)."

The contrast is a diagnostic group (delayed sleep-wake phase disorder) versus controls, pooled from
cross-sectional and case-control studies. Neither arm is a sleep dose and the subject is in neither
arm by exposure; a diagnosis is not a sleep condition our exposure engine can assign. Assigning it a
harm sign implies a causal contrast the design cannot support, so it must be **excluded from any
pooled harm estimate** rather than signed. If retained as context only, record magnitude 1.02 with
`unit: "SD units, DSWPD minus non-DSWPD, higher = more severe depression"` and `poolable: false`.

Both teams had the magnitude right and both were wrong to sign it. Team 2 was also right on n: the
sensitivity model has **612** participants, not the 766 screened into the review (Team 1's n).

**Cause: task specification. The convention is silent on contrasts that are not between sleep
conditions, and the task labelled the exposure `descriptive` while demanding a signed d.**

## B2. `koyama2022_diabetes_lifetime::1` — years of potential life lost to diabetes

**VERDICT: `CORRECT_VALUE: −6.2`, scale `years`.** Team 1 right.

Verbatim (DOI 10.1371/journal.pone.0268805, PMID 35609056):

> "For example, during the earliest time period in 1997-1999, a person diagnosed with diabetes at age
> 20 was estimated to lose on average 8.9 (95% CI: 8.7-9.1) years of potential life due to diabetes,
> decreasing to an average of 6.2 (95% CI: 6.1-6.4) years in 2015-2018."

A loss of 6.2 life-years is unambiguously worse off, so the canonical signed value is **−6.2** years
(SE 0.077 from the simulation interval, which is a Monte Carlo percentile interval, not an analytic
CI). Team 2's +6.2 faithfully followed the task's `target_unit`, "years of potential life lost due to
diabetes, adult aged 20", which encodes the direction in words and thereby makes a positive number
mean a decrement.

Note for the modeller: this is an **absolute baseline-risk quantity with no sleep exposure**. It is a
consequence-severity input, not a sleep effect, and must not enter a pooled sleep-harm estimate.

**Cause: task specification (direction-laden `unit` string plus no sign rule in the task). The source
is unambiguous.**

## B3. `klingenberg2013::1` — Matsuda index of insulin sensitivity

**VERDICT: `CORRECT_VALUE: −28`, scale `pct_change`.** Team 1 right.

Verbatim (DOI 10.5665/sleep.2816, PMID 23814346, abstract Results):

> "The homeostasis model assessment of insulin resistance (HOMA-IR) index was 65% higher (P = 0.002)
> and the Matsuda index was 28% lower (P = 0.007) in the SS condition compared to the LS condition."

A lower Matsuda index is lower whole-body insulin sensitivity, i.e. worse off, so **−28**. SE 9.32
percentage points (t = 3.0048 at df = 20 for two-sided p = 0.007; 28/3.0048). Team 2's +28 is
verbatim-faithful to the recorded unit string "% lower Matsuda index in short-sleep vs long-sleep
condition".

This record is also the cleanest proof of the codebook defect. Inside the *same file*,
`klingenberg2013::0` records HOMA-IR as **+65** with `direction_note: "positive = HARM (higher
HOMA-IR = more insulin resistance)"`, while `klingenberg2013::1` records Matsuda as **−28** with
`direction_note: "negative = HARM"`. One extractor, one study, two opposite conventions — because
both records inherited the sign of the raw measured direction rather than a valence. Under the
canonical convention HOMA-IR must be **−65** and fasting insulin (`::2`, currently +59) must be −59.

**Cause: task specification.**

## B4. `huang2023_cvdfree_life_expectancy::1` — CVD-free life expectancy, males

**VERDICT: `CORRECT_VALUE: −0.55`, scale `years`.** Team 1 right.

Verbatim (DOI 10.1186/s12916-023-02732-x, PMID 36859313, abstract; Table 2 agrees):

> "We observed a gradual loss in CVD-free life expectancy toward poor sleep such as, compared with
> healthy sleepers, poor sleepers lost 1.80 [95% CI 0.96-2.75] and 2.31 [1.46-3.29] CVD-free years in
> females and males, respectively, while intermediate sleepers lost 0.48 [0.41-0.55] and 0.55
> [0.49-0.61] years."

Unlike B1 and B5 this *is* a sleep-exposure contrast (composite sleep profile, intermediate versus
healthy), so the canonical convention applies: 0.55 CVD-free years lost = worse off = **−0.55**
(SE 0.031). Team 2's +0.55 followed the unit string "CVD-free years lost at age 40".

Exposure caveat for the transportability grade: the exposure is a 5-item composite (chronotype,
duration, insomnia complaints, snoring, daytime sleepiness), of which duration is one item, so the
task's `habitual_short_sleep` overstates the match. Age 40 baseline, not adolescent.

**Cause: task specification.**

## B5. `zitting2018::1` — age moderation of inadvertent sleep during PVT

**VERDICT: `EXCLUDE`. The canonical convention does not apply.** `canonical_sign_applies: false`.
Neither team was right, because both assigned a sign the design cannot support.

Verbatim (DOI 10.1038/s41598-018-29358-x, PMID 30038272):

> "Young participants were also significantly more likely to have at least one inadvertent sleep
> during their PVTs than were older participants [chi2 (1, N = 23) = 5.49, p = 0.0191]."

The contrast is **young versus older adults**, both exposed to the same 21-day 5.6 h/24 h chronic
sleep deficiency plus forced-desynchrony protocol. There is no restricted arm and no rested referent,
so "worse for the subject under restriction" has no referent to attach to; the sign is a category
error in either direction. Both teams computed the same magnitude by the same route
(phi = sqrt(5.49/23) = 0.489; d = 2*phi/sqrt(1−phi²) = 1.120; J = 0.964; g = 1.079).

If the factory wants an age-vulnerability multiplier, it must be modelled as an explicit moderator
with its own declared polarity (e.g. "positive = young more vulnerable"), stored in a separate field,
and never folded into the harm sign. Two further cautions: the outcome is a dichotomy ("at least one
inadvertent sleep") in N = 23, so |g| ≈ 1.08 is fragile; and n is **23** (12 young, 11 older for PVT
measures), not the 24 Team 1 recorded — Team 2 right on n.

**Cause: task specification.**

## B6. `unit` strings that encode direction — the class defect

`klingenberg2013::1` ("% lower Matsuda index …"), `koyama2022_diabetes_lifetime::1` ("years of
potential life lost …") and `huang2023_cvdfree_life_expectancy::1` ("CVD-free years lost at age 40
…") all carry the direction inside the `unit` string, so a positive number denotes a decrement and
the number contradicts the convention it is stored under. All three are among the disputes above,
and in all three Team 2 read the unit string literally — which, given what the task file gave it, was
the more disciplined reading.

**VERDICT for the class: `RECODE` the codebook, not the numbers.** `unit` must name a
direction-neutral quantity ("% change in Matsuda index", "change in CVD-free life-years"); direction
must live only in the sign and in `direction_note`.

Corpus scan of all 1,999 effects in 597 evidence files:

- **197** effects carry a direction word (lower / higher / lost / gained / reduction / deficit …)
  inside `unit`.
- **28** of those have a `unit` whose direction word contradicts the sign of the stored value, after
  excluding log-scale ratios and unit strings that already self-document polarity. Most are
  qualitative or descriptive slots rather than true sign errors, but each is a place where a
  downstream reader cannot recover orientation from the number.
- Keyword scan of `direction_note` (heuristic, so treat as an order of magnitude): **133** effects
  explicitly declare "positive = harm/worse" *and* store a positive value — orientation-documented
  and canonically wrong — against **287** that declare "negative = worse" and comply. The 133 are
  concentrated in outcomes whose measured scale runs the "wrong" way: PVT lapses, KSS, HOMA-IR,
  cortisol, insulin, glucose.

The six sign disputes are the visible tip of that 133. Reconciling signs is exactly what turned the
G3 gate from fail to pass (`reports/agreement.json`: ICC 0.827 raw, 0.981 sign-reconciled), which
means the gate is currently being carried by a post-hoc sign flip rather than by agreement.

---

# The general question: source ambiguity or specification ambiguity?

**Specification: 8 of 9. Source: 1 of 9.** Honest tally, one line each:

| dispute | primary cause | why |
|---|---|---|
| `lo2016::1` | **specification / tooling** | `task_id` = `study_id::effect_index` is not unique; 3 records share `study_id: lo2016`, so the two teams extracted different papers |
| `huang2016::2` | **source** | paper reports no g, no means, no SDs; only an LR chi² from a 4-factor model and an image-only table |
| `rabat2016::0` | **specification** | construct name describes a time-course shape; schema demands a standardised mean difference |
| `dama2025::2` | **specification** | convention silent on diagnostic-group contrasts |
| `koyama2022_diabetes_lifetime::1` | **specification** | direction-laden `unit`; no sign rule in the task file |
| `klingenberg2013::1` | **specification** | same |
| `huang2023_cvdfree_life_expectancy::1` | **specification** | same |
| `zitting2018::1` | **specification** | convention silent on between-age-group contrasts |
| unit-string class (B6) | **specification** | by construction |

Secondary source defects exist and are worth logging, but they are not what the teams fought over:
`lo2016` (J Sleep Res) prints Cohen's d on two scales inside one sentence, inflating its own headline
contrast ~2× — a real reporting defect, already caught and corrected by Team 1 before the dispute;
and `huang2016` reports its key interaction only as a likelihood-ratio statistic.

**So: fix the codebook. Do not discount the literature.** Five concrete changes, in order of how much
they buy:

1. Move the sign convention out of `spec/gates.md` and into `spec/EXTRACTION_INSTRUCTIONS.md` as a
   hard rule, stated as valence ("negative = the subject is worse off"), with worked examples for
   outcomes whose measured scale runs the wrong way (lapses, KSS, HOMA-IR, cortisol). Add a
   validator: the sign of `value` must agree with the polarity asserted in `direction_note`.
2. Make `task_id` unique — `shard/study_id::effect_index`, or hash the file path. The current key
   silently overwrites truth rows whenever a study appears in more than one shard, which is common
   here (`lo2016` ×3). This is a data-integrity bug beyond these disputes and it is in
   `src/make_blind_sample.py` lines 73 and 110.
3. Add a `contrast_class` field with values `sleep_dose` / `group_moderator` / `baseline_risk` /
   `descriptive`, and let only `sleep_dose` carry a canonical sign or enter pooled harm. That single
   field disposes of `dama2025::2`, `zitting2018::1` and `koyama2022_diabetes_lifetime::1` without
   argument.
4. Forbid direction words in `unit`; require direction-neutral units plus an explicit
   `higher_is_better: true|false` boolean, from which the validator can derive the canonical sign
   mechanically.
5. Give extractors an explicit `NOT_EXTRACTABLE` verdict with a reason code, and ship a whitelist of
   sanctioned conversions (t, F, exact p, means+SDs, ratios+CIs). Ban conversion from interaction
   statistics — omnibus chi², partial eta², Cohen's f² — to a standardised mean difference. That
   removes `huang2016::2`-style inventions at the source, and would have blocked both the 0.282 and
   the 0.766.

Also propagate the two spillover fixes named above: `s01_cognition_dose_response/lo2016.yaml`
effect 1 (sign, and a missing quote on a figure-digitised value), and `klingenberg2013::0` / `::2`
(HOMA-IR +65 → −65, fasting insulin +59 → −59).
