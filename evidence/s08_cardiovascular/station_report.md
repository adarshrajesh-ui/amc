# Station report — shard `s08_cardiovascular`

**Domain:** blood pressure, hypertension, coronary heart disease, stroke and major adverse
cardiovascular events in relation to short sleep — both the acute experimental BP/autonomic effects
and the long-run incident-disease epidemiology.

**Output:** 18 YAML records, 71 effect estimates, `screening_log.md`, `cardio_summary.md`.

---

## 1. What I did

1. Read `spec/EXTRACTION_INSTRUCTIONS.md` and `spec/effect.schema.json` in full before searching.
2. Ran 20 PubMed E-utilities queries (`esearch` + `esummary`), screening **85 records**. Every PMID in
   this shard came from a live query return, not from recall.
3. Retrieved **full text** for 6 papers (Yin 2017, Covassin 2021, Daghlas 2019, Guo 2024, Zhao 2025,
   Huang 2022, Meininger 2014) via PMC or the publisher, because the numbers the task required —
   spline RRs at 5 h and 6 h, staged adjustment models, absolute incidence per 1000 person-years,
   sex-stratified BP — are **not in the abstracts**. Abstract-only extraction would have missed the
   two most decision-relevant findings in the shard.
4. Verified all 18 DOI/PMID pairs against Crossref and PubMed before writing any record
   (`verify_batch.py` → `verification_raw.json`): **18/18 resolved on both services**.
5. Computed every log-scale conversion and SE numerically rather than by hand
   (`se = (ln(upper) − ln(lower))/3.92`), and recorded the arithmetic in each `conversion_formula`.
6. Validated all records against the schema (`validate.py`): **18 files, 71 effects, 0 failures**.
7. Ran the pipeline's own `src/verify_refs.py`: **18/18 s08 records VERIFIED, title similarity 1.000
   on every one**, no duplicate study_ids from this shard.
8. Ran an **anti-fabrication quote audit** (`audit_quotes.py`) that mechanically checks every `quote`
   field against the cached source texts: **71/71 quotes located verbatim**.

### The quote audit caught four real defects — worth recording

I wrote `audit_quotes.py` because a hand-transcribed quote is exactly where a fabricated number would
hide, and self-assessment is not evidence. On its first run it flagged 10 of 71 quotes, and 4 of those
were genuine transcription defects that I then fixed:

- **Yin 2017 table rows (6 quotes).** I had reassembled Table 2 rows with `" | "` cell separators for
  readability. The numbers were correct but the string was a reconstruction, not verbatim source text.
  Rewritten to match the source's own whitespace so the row now matches character-for-character.
- **Yin 2017 stroke nadir.** I had expanded the source's `≈` to the word "approximately". Restored.
- **van Leeuwen 2018 (3 quotes).** I had substituted `+/-` for the source's `±`. Restored.
- **Zhao 2025 stroke null.** I had joined two non-adjacent sentences with `" ... "`, presenting them as
  one quote. Replaced with the single contiguous sentence that actually carries the evidential weight
  (the complete enumeration of short-sleep results, which names CAD, MI and HF and omits stroke), with
  the second sentence's role explained in `conversion_formula` instead.

None of these changed an extracted number, but all four would have made a downstream reviewer unable
to find the quoted text in the source, which is the failure mode the hard rules exist to prevent.
The audit is re-runnable offline against the cached `*.txt` extracts.

### Reproducing this shard

```bash
cd /workspace/evidence/s08_cardiovascular
python3 verify_batch.py     # re-verify all 18 DOI/PMID pairs against Crossref + PubMed
python3 validate.py         # schema validation (Gate G0)
python3 audit_quotes.py     # check every quote against cached sources (offline)
python3 pm.py search "<query>" 20   # re-run any screening query
python3 pm.py abs <PMID>            # re-fetch any abstract
cd /workspace && python3 src/verify_refs.py   # Gate G2
```

The `*.txt` files are the text extracts of the full texts I actually read, retained as the provenance
trail for every quoted number and as the corpus `audit_quotes.py` checks against. I deleted the raw
`*.html` originals (2.7 MB) after extraction to keep the shard directory small.

---

## 2. The seven required extractions — status

| # | Requested | Status | Key numbers |
|---|---|---|---|
| 1 | Cappuccio 2011 EHJ, CHD and stroke separately | **Done, as described** | CHD RR 1.48 (1.22-1.80); stroke 1.15 (1.00-1.31); **total CVD null, 1.03 (0.93-1.15)**. 15 studies / 24 samples, 474,684 participants, 16,067 events |
| 2 | Dose-response MA incl. Yin 2017 + newer; RR per hour and at 5 h and 6 h | **Done, as described** | Yin per hour: CVD 1.06, CHD 1.07, stroke 1.05. **At 6 h: CVD 1.02, CHD 1.05, stroke 0.99. At 5 h: CVD 1.05, CHD 1.11, stroke 1.02.** Newer (Huang 2022, 3.8 M): risk not elevated anywhere in 4.3-10.3 h |
| 3 | Hypertension MA; age interaction | **Done, with a correction** | Guo 2013 RR 1.23 (1.06-1.42); Wang 2012 RR **1.33** (1.11-1.61) in **< 65 y**; Itani 2017 RR 1.17. **"Younger" means under 65 — nobody near 19.** No "Meng" MA exists |
| 4 | Experimental BP/HR/sympathetic; reversal | **Done — and it is largely null in males** | Covassin: 24-h MAP +2.1 (0.6,3.6), SBP +3.1, DBP +2.2, HR **no change**; **men: no 24-h effect, daytime MAP −3.8**. Hu 2020 pooled RCTs: SBP +1.0 (−2.3,4.2) **ns**. NE +55.5 pg/mL, FMD −2.2%. Reversal **partial** |
| 5 | Daghlas MR + MR of BP/stroke; vs observational; causality | **Done, with author-list and scale corrections** | MR per hour lost: **1.25 (1.05-1.49)**; replication 1.12 (1.01-1.25); 1-sample **ns** (p=0.17). Observational adjusted 1.20 (1.07-1.33). **Stroke: no MR support for duration in either MR study** |
| 6 | Adolescent/young-adult BP and vascular markers | **Done — and it is thin, as anticipated** | Meininger (ages 11-16, actigraphy + 24-h ABPM): **−0.57 mmHg per hour**. Sands cIMT −0.026 mm/h in men — **but ages 37-52, not young adults** |
| 7 | Confounding; adjustment sets; before/after | **Done — the shard's most important result** | 6 h vs 7-8 h MI: **1.16 crude → 1.05 (0.98-1.13) adjusted. 67% of the crude log-HR attenuated away.** BMI ~23%, SES/behaviour/comorbidity ~55%, depression 9-13% |
| — | Absolute event rate + cohort age for every ratio | **Done where published** | UK Biobank MI: **1.70/1000 PY at 6 h vs 1.47 at 7-8 h = 1 extra MI per 4,348 PY, at ages 40-69**. See §5 for what I could not get |

---

## 3. Corrections to the task's premises

Per instruction 4 ("Seed names in your task are hints, not truth"), reporting reality:

1. **Daghlas author list.** The task said "Daghlas, Dashti, Lane, **Saxena, Rutter** et al." The actual
   order is **Daghlas I, Dashti HS, Lane J, Aragam KG, Rutter MK, Saxena R, Vetter C** — Aragam and
   Vetter (senior/corresponding) were omitted and Saxena/Rutter transposed. Journal, year, volume and
   pages match exactly (JACC 2019;74(10):1304-1314).
2. **"Meng et al." hypertension meta-analysis does not exist.** A dedicated query returned 14 records,
   none of them a Meng meta-analysis of sleep duration and incident hypertension. The real
   hypertension syntheses are Guo 2013, Wang 2012 and one dose-response attempt (Li 2019).
3. **Internal discrepancy inside Daghlas 2019.** The abstract says "5,128 incident cases"; the Results
   text says "5,218 incident MIs". Table 1's per-stratum counts sum to **5,218**
   (82+310+1058+3248+375+129+16), corroborating the Results figure. I used 5,218 and flagged it.
4. **The "age interaction" does not mean what it is usually taken to mean.** Both sources define
   "younger" as under 65 (Wang 2012) or 32-59 (Gangwisch 2006). Neither is relevant to a 19-year-old,
   and for hard CVD endpoints Yin 2017 reports the interaction running the *opposite* direction.
5. **CARDIA is not a young-adult sample at the relevant visit.** Sands 2012 is widely cited as
   young-adult evidence; participants were **37-52** at actigraphy and carotid ultrasound.
6. **The task framing "the acute experimental blood-pressure effects" presumes an effect that the
   pooled randomised evidence does not show** — and specifically does not show in males.

---

## 4. What I could not find

| Sought | Result |
|---|---|
| **Any natural experiment** (school start times, DST, time-zone boundaries) with a cardiovascular outcome | **Zero records.** Tier T2 is completely empty for this domain |
| Prospective cohort with **objective** (actigraphy/PSG) sleep duration and incident CVD, duration isolated | **None usable.** The one candidate (MESA, JAHA 2022) uses a composite 8-metric cardiovascular-health score in a cohort of mean age **69**; the duration effect is not separable. **Tier T4 effectively empty** |
| Any study following **adolescents** to incident cardiovascular events | **None exists.** Would require 40+ years of follow-up from adolescence |
| Per-hour RRs with CIs from Huang 2022 | Not published — results are given as spline boundaries and figures. PMC copy would not render; used the publisher's full text and the verified abstract |
| SE or CI for Meininger's −0.57 mmHg coefficient | Not reported. Bounded from `P < 0.0001` → SE < 0.1465; recorded the **maximum** consistent SE (conservative) with `inferred_from_ci: true` |
| Point estimate for Kwok 2018's sub-7 h arm | Not reported — the paper states only that no significant difference was found. Recorded as a directional null with `se: null`, explicitly flagged as ineligible for inverse-variance weighting |
| Stratum-specific absolute rates from any meta-analysis | None report them. Only Daghlas 2019 publishes incidence per 1000 person-years by sleep stratum |
| **Age-specific baseline MI/stroke/hypertension incidence for a 19-year-old male** | **Not retrieved, and not invented.** This is a genuine hand-off: the baseline-risk/life-table station must supply it |

Four records carry `value: 0` with `se: null` as explicit **directional nulls** (Kwok sub-7 h arm;
Itani's absent dose-response; Guo 2024 and Zhao 2025 duration-stroke nulls; Covassin's male-stratum
and heart-rate nulls; Li 2019's unreported categorical magnitudes). These encode real published
non-findings. **They must not receive inverse-variance weight** — each says so in its
`conversion_formula`.

---

## 5. My own confidence

**Moderate on the direction, low on the magnitude, high on the claim that the magnitude is small at
this subject's exposure.**

What I trust:
- The dose-response *shape* is robust: flat between 6 and 7 h, steeper on the long arm than the short
  arm. Reproduced by four independent syntheses covering 3.3-5.2 M participants each.
- The 67% attenuation on adjustment is a real, published, decomposable number from a well-powered
  cohort with a fully enumerated covariate set.
- The experimental picture for young males — sympathetic activation and endothelial impairment, but no
  reliable blood-pressure rise — is consistent across a randomised crossover trial, a young-male
  crossover study, and a meta-analysis of RCTs.

What I do not trust:
- **Any single pooled ratio.** The spread across syntheses for the same exposure and outcome is larger
  than most individual confidence intervals — CVD at 6 h ranges from "1.02" to "not elevated at all",
  stroke from 0.99 to 1.33. This is heterogeneity between analysts, not sampling error, and no
  inverse-variance pool will represent it honestly. **The downstream model must inflate the stroke and
  total-CVD intervals well beyond what the reported CIs imply.**
- **Every ratio's transportability to age 19.** 13 of 18 records are `poor_midlife`.
- **Self-reported exposure throughout the epidemiology.** Yin 2017 used questionnaires in 48/67 studies
  and interviews in 19 — zero objective measurement. A single self-report item is a poor proxy for
  three years of a specific weekday/weekend pattern, and it is systematically correlated with the
  confounders (deprivation, shift work, depression) that drive the association.
- **The sex-stratified estimates**, since the two best ones contradict each other about which sex is
  vulnerable.

Where I may have erred: I resolved the observational-versus-MR tension (§3.3 of `cardio_summary.md`)
by presenting two readings rather than choosing. A methodologist may reasonably argue that Daghlas's
Model 3 is so heavily over-adjusted for mediators (hypertension, diabetes, cholesterol, BMI and three
drug classes) that the "67% attenuation" headline is misleading as a confounding estimate. I have
flagged this inside the record and the summary rather than picking a side, and I graded the
confounding-survival number **D on quantity** because it rests on one cohort's table.

---

## 6. The single biggest gap in the evidence for this domain

**There is no evidence at all — of any tier — connecting sleep restriction during adolescence to
cardiovascular outcomes at any later age.**

The gap is structural, not incidental. Concretely:

- The **exposure window** is wrong in every event-based study. All 13 midlife/elderly records measure
  sleep duration *once*, in adults aged 40-70, and relate it to events over the following 5-25 years.
  None measures adolescent sleep. The subject's exposure — three years of weekday restriction at ages
  16-19 — has never been studied against a cardiovascular endpoint.
- The **outcome** is unreachable at his age. Cardiovascular events in 19-year-olds are so rare that no
  feasible cohort could detect an effect; the honest question is whether adolescent restriction shifts
  a *risk trajectory*, and answering it requires either decades of follow-up from adolescence (does
  not exist) or a validated surrogate with demonstrated prognostic value from youth (also does not
  exist — the two surrogate records here are cross-sectional, one is in 37-52 year olds, and the other
  reports 0.57 mmHg per hour).
- The two designs that could bridge the gap are **both empty**. Tier **T2** (natural experiments) has
  zero cardiovascular studies despite an extensive school-start-time literature on sleep and
  academic/behavioural outcomes. Tier **T4** (prospective objective exposure) has no cohort that
  isolates sleep duration — the sole actigraphy/PSG cohort with incident CVD folds duration into an
  8-metric composite in a cohort of mean age 69.

**The consequence for the pipeline.** Every cardiovascular number this shard hands downstream is a
*double* extrapolation: from midlife to adolescence, and from a one-off self-reported duration to a
three-year structured weekday/weekend pattern. The MR records mitigate the confounding problem but
not the age problem — the sleep-duration GWAS is itself built on middle-aged UK Biobank
self-reports, so genetic liability to short sleep at age 56 is doing the work of measured restriction
at age 18. Uncertainty on the cardiovascular component of the final estimate should be dominated by
this transportability gap rather than by the sampling error in any published confidence interval, and
the cardiovascular contribution to total damage should be reported as **small with wide intervals
straddling zero** rather than as a precise small number.

---

## 7. Files

| File | Contents |
|---|---|
| `cardio_summary.md` | Dose-response curve; observational-vs-MR comparison; explicit confounding-survival statement; absolute risk; confidence grades |
| `screening_log.md` | All 85 screened records with decisions and reasons; 20 search queries |
| `*.yaml` (18) | Evidence records, schema-valid, verbatim quote per effect |
| `verification_raw.json` | Raw Crossref + PubMed returns for all 18 identifiers |
| `verify_batch.py` | Identifier verification script |
| `validate.py` | Schema validation (Gate G0) |
| `pm.py` | PubMed search / abstract / Crossref helper |
| `*.txt`, `*.html` | Cached retrieved full texts (provenance for every quoted number) |
