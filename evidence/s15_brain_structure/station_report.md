# Station report — shard `s15_brain_structure`

**Domain:** whether chronic sleep restriction during adolescence (ages 16–19) leaves a structural or
developmental mark on the brain — the "permanent damage" channel.

| Metric | Value |
|---|---|
| Records screened | **121** (gate G1 threshold ≥ 25) |
| Records included | **30** |
| Records excluded | **91** |
| Effect estimates extracted | **72** |
| Records validating against `effect.schema.json` | **30 / 30 (100%)** |
| Records with `status: VERIFIED` | **30 / 30 (100%)** |
| Identifiers that failed verification | **0** |
| Effects carrying a verbatim quote | **72 / 72 (100%)** |
| Tier distribution | T1 = 11 · T3 = 2 · T4 = 2 · T5 = 7 · TX = 8 |
| Age-match distribution | `exact_16_19` = 3 · `good_young_adult` = 3 · `mixed` = 14 · `fair_adult` = 7 · `poor_midlife` = 3 |

---

## 1. What I did

**Search.** PubMed E-utilities (`esearch` / `esummary` / `efetch`) through three helper scripts I
wrote in `_tools/`: `search.sh` (query → PMID + year + journal + DOI + title), `abs.sh` (full
abstract + metadata), `pmc.sh` (PMC Open Access full text including tables and captions). Query
families run: adolescent sleep duration × brain structure / cortical thickness / grey matter volume;
named-cohort searches (ABCD, IMAGEN, Generation R) and named-author searches (Urrila, Cheng, Taki,
Kocevska); longitudinal MRI × adolescent sleep; experimental sleep deprivation × grey matter /
cortical thickness / diffusion; CPAP and recovery-sleep imaging; diffusion MRI × adolescent sleep
duration; Mendelian randomization × sleep × brain structure; synaptic homeostasis and pruning ×
adolescence; rodent adolescent sleep restriction × durable neural change.

**Verification.** Every included record's PMID was resolved against PubMed `esummary` **and** its
DOI against Crossref, with programmatic title-similarity scoring and a check that PubMed's own DOI
for the PMID matches the DOI in the record (`_tools/verify.py`). Final pass, driven directly off the
30 YAML files: **0 failures, title similarity 1.000 for all 30.** (An earlier, wider 35-pair check
that also covered records I subsequently excluded had a minimum of 0.876.)

**Extraction.** One YAML per study, validated with `_tools/validate.py` (jsonschema Draft-7 against
`/workspace/spec/effect.schema.json`, plus hand checks the schema cannot express: `study_id` matches
filename, shard field correct, CI lower < upper, every effect carries a quote).

**Deliverables.** 30 YAML records · `screening_log.md` (every screened PMID with a decision and
reason) · `structure_summary.md` (per-hour effects with CIs, cross-sectional vs longitudinal
separation, state-vs-trait quantification, reversibility, verdict with probability) · this report.

---

## 2. Coverage of the seven required extractions

| # | Required | Status | What I found |
|---|---|---|---|
| 1 | Cross-sectional + longitudinal MRI of adolescent sleep duration and brain structure; the four named seeds | **Complete, with corrections** | All four seeds located and extracted: `urrila2017` (PMID 28181512, *Sci Rep*), `cheng2021` (32015467, *Mol Psychiatry*), `taki2012` (22197742), `kocevska2017` (28364462, Generation R). Plus newer ABCD (`limasantos2025`, `yang2022`, `chen2026`) and IMAGEN (`lapidaire2021`, `guldner2023`) analyses the seeds predate. |
| 2 | **Longitudinal** — does short sleep at T1 predict *change* by T2? | **Complete** | Seven longitudinal designs found. **Four are unambiguously null for sleep duration**, including the two largest (`fjell2023`, `limasantos2025`) and the only one spanning the subject's exact window (`guldner2023`, 14.5 → 19.8 y). The three positive ones have n = 39 (`wild2026`), no control arm (`alvarezornelas2025`), or measure *stability* rather than change (`yang2022`). |
| 3 | Experimental deprivation → acute volume change (state, not trait) | **Complete — this literature exists and I quantified it** | Six lab studies: `bernardi2016`, `elvsashagen2015`, `elvsashagen2017`, `voldsbekk2022`, `sun2020`, `liu2014`. Structural metrics move within **hours**; the acute state effect (d_z ≈ 0.43–0.53 minimum detectable at n = 16–23) is **4.5–5.6× larger** than the entire habitual cross-sectional association (d = 0.095). |
| 4 | Do volume differences **reverse**? | **Complete** | `bernardi2016`: *"All changes reverted after recovery sleep."* `canessa2011`: GM volume increased after 3 months of OSA treatment. `xu2025`: **randomised** CPAP trial (n = 148) moved cortical thickness −0.06 mm (−0.10, −0.01) — and produced **zero** cognitive benefit (MoCA −0.04, −0.72 to 0.65, p = 0.91). |
| 5 | White matter / diffusion FA per hour of sleep | **Partial — the per-hour figure does not exist** | Best available are per-SD, not per-hour: `mulder2019` −0.12 SD (−0.20, −0.05) corticospinal and uncinate FA per SD of sleep problems. Adolescent longitudinal FA vs sleep *duration* is **null** in `guldner2023`, `telzer2015` and `limasantos2025`. No study reports FA per hour of sleep at ages 16–19. |
| 6 | Pubertal stage / sensitive period / pruning | **Complete, and it points earlier than 16–19** | `gay2024` deprived mice at three separated stages: **juveniles** were vulnerable, adolescents grouped with adults in *"comparative resilience."* `feinberg2006` (longitudinal PSG): NREM delta power fell 25% from age 12→14 and tracked **age, not Tanner stage**. `tuan2019`: impaired microglial pruning is adolescent-specific in mice but yields **more** synapses, predicting *larger* volumes — opposite to the human cross-sectional sign. |
| 7 | Animal chronic adolescent restriction → durable change, with translation problem | **Complete** | `howard2019` (**rat**, 10 d restriction + **4 weeks free sleep**) is the single strongest pro-permanence finding I located, and I weight rather than dismiss it: object-location memory deficit persisted into adulthood. But it **measured no brain**, so it cannot establish a *structural* mark. Full five-point translation problem stated in `structure_summary.md` §6 and in each animal record. |

---

## 3. What I could not find — and why the absence is itself the finding

1. **No pooled per-hour volumetric estimate for sleep duration exists anywhere in this literature.**
   `namsrai2025` is a systematic review with meta-analysis of **106 studies / 108,364
   participants**, restricted to analyses adjusting for age, sex and head size. It produced exactly
   one pooled voxel-based finding, and it was for REM sleep behaviour disorder — not sleep duration.
   `ananth2026`, the most recent review aimed squarely at this shard's question, states that *"no
   review has systematically examined the effects of insufficient sleep on structural brain
   development."*
2. **The named seed study cannot supply the requested units.** `urrila2017` reports grey matter
   volume in **arbitrary units** (*"GMV is expressed in arbitrary units"*), publishing only
   peak-voxel *t* statistics, cluster extents and MNI coordinates. Any mm³-per-hour value attributed
   to that paper would be fabricated. I report this as reality per hard rule 4 rather than
   manufacturing a number.
3. **`taki2012` publishes direction and significance only** — no coefficient, no CI, and the full
   text is not in PMC Open Access.
4. **Zero studies image habitual 5–6 h sleepers aged 16–19 longitudinally.** Cohort mean weekday
   sleep is 8 h 18 min in the best-age-matched sample (`lapidaire2021`, mean age 16.8) and 8.8 h in
   `urrila2017`. At 5.5 h the subject sits **2.8–4.1 SD below** the means of the cohorts that
   generated every slope in this field.
5. **`liu2014`'s sample size is not recoverable** from the abstract; I re-fetched it to confirm and
   set `n: null` rather than guess. Same for the animal records' per-group n.
6. **No observational study in this shard controlled participants' sleep on the night before the
   scan** — which is what makes the state-vs-trait problem unresolvable from existing data.

---

## 4. Does ANY of this evidence support a claim of permanent structural damage in a specific 19-year-old?

**No. Bluntly: no.** Not in magnitude, not in design, not in causal direction, not in permanence.

- **Magnitude.** The largest credible effects are ≈1% of a structure per SD of a fairly severe
  exposure (`kocevska2017`, −7.3 cm³, −12.1 to −2.6) or 0.22% of variance (`cheng2021`, r = 0.047,
  d = 0.095, 0.058–0.132, n = 11,067). Normal inter-individual variation in regional brain volume is
  roughly 8–10% — **8–10× larger than the largest group effect on offer.**
- **Design.** The four largest, best-designed longitudinal tests are null for sleep duration.
  `fjell2023`: *"for no region or metric was the P value smaller than 0.05."* Across the whole field,
  51.9% of cross-sectional studies found associations versus only 45.5% of longitudinal ones
  (`namsrai2025`) — backwards from what a real progressive process would produce.
- **Causal direction.** Four independent designs put the arrow **brain → sleep**: both MR studies
  (`fjell2023` forward-null but intracranial volume → sleep supported; `zhang2024` brain regions as
  the *exposure*), `cheng2021`'s cross-lagged panel (depressive problems → shorter sleep β = −0.081,
  p < 1e-4; forward path null, p = 0.17), and `chen2026`'s polygenic natural-short-sleeper subtype.
- **Permanence.** `bernardi2016` reports **100% reversal** of acute GM/WM/ventricular/diffusivity
  changes after one recovery night. `canessa2011` and the randomised `xu2025` show movement under
  treatment. Cortical maturation continues into the mid-20s, so the subject is still inside the
  window in which these measures change.
- **Functional meaning.** `xu2025` is the decisive test: randomisation moved cortical thickness and
  bought **nothing** on the pre-registered cognitive endpoint (p = 0.91). A fraction-of-a-percent
  observational volume difference has **no established mapping to any functional consequence** for
  an individual.
- **Base rate.** *"Fewer than 30% of high school students obtain the recommended 8–10 h"*
  (`ananth2026`). His exposure is the statistical norm for his generation, and the largest study of
  the question puts the volumetric optimum at **6.5 h (95% CI 5.7–7.3)** — essentially at the top of
  his weekday range.

**Probability I assign:** P(detectable, permanent, sleep-attributable structural change in this
individual) **≈ 0.03**; P(functionally meaningful permanent structural damage) **≈ 0.01**. Kept
separate and deliberately higher: P(some durable neurobiological change of any kind, not necessarily
structural or detectable) **≈ 0.25** — this is where `howard2019` and `tuan2019` legitimately move
the posterior, and I refuse to launder it into a structural claim it cannot support. Decomposition
into five conditional steps is in `structure_summary.md` §7.

---

## 5. My own confidence

Using the four `gates.md` axes, for the shard's headline conclusion — *no support for permanent
structural damage*:

| Axis | Grade | Reason |
|---|---|---|
| Quantity | **B** | 30 records, 7 longitudinal designs, 6 acute lab studies, 2 MR, 1 large meta-analysis. Adequate but not ≥ 10 independent studies of the specific exposure. |
| Quality / tier | **B** | 11 × T1 and 2 × T3 anchor the causal and reversibility claims; the *positive* findings are almost entirely TX/T5. Note the asymmetry: the strongest designs produce the nulls. |
| Transportability | **C** | Only 3 records are `exact_16_19` (`lapidaire2021`, `guldner2023`, `telzer2015`). No cohort sampled 5–6 h habitual sleep at 16–19. `fjell2023`, the single most decisive study, is ages 20–89. |
| Model dependence | **B** | The *null* is stable across specifications, cohorts and countries. The sign of the *positive* cross-sectional literature is not: `fjell2023` finds short sleep associated with **thicker** cortex, `wild2026` and `40099522` report sign-inconsistent directions, and `sun2020` disagrees with itself by region and morphometric measure. |

**Overall confidence in the negative conclusion: high (≈0.9).** Confidence that the residual
uncertainty is *small* rather than merely *unmeasured*: **moderate (≈0.6)** — see the gap below.

I am **not** confident about, and have not claimed: any per-hour mm³ slope at 16–19 (none exists);
any dose-response shape below 5 h in adolescents (unsampled); anything about sub-MRI-resolution
synaptic or epigenetic change (unmeasurable in a living human).

---

## 6. The single biggest evidence gap

**Nobody has ever scanned habitual 5–6 h sleepers aged 16–19 more than once.**

The exposure this factory is estimating is, for brain structure, **unstudied**. Every number in the
field comes from cohorts averaging 8.3–8.8 h weekday sleep, and every reassuring null is therefore
an extrapolation *downward* past the sampled range — while the only dataset that does sample 3–5 h
(`fjell2023`: n = 541 at 3–4 h, 2,937 at 4–5 h, 13,863 at 5–6 h) finds the curve **turning the other
way**, which is reassuring but comes from adults aged 20–89.

The study that would settle this and does not exist: repeated structural MRI plus **actigraphy**,
across ages 16 → 20, sampling the genuine 5–6 h tail, with pre-scan sleep measured so state can be
separated from trait. `wild2026` is the closest existing design — objective exposure plus repeated
imaging — and it has **n = 39** at ages 10–14 with ~28 models and no stated multiplicity correction.

The honest form of the conclusion is therefore: **the absence of demonstrated permanent structural
damage rests on a strong and consistent set of nulls in adjacent exposure ranges, not on a direct
test of this exposure.** That distinction should propagate into the downstream posterior as width,
not as a shifted mean.

---

## 7. Handling notes for the downstream pooler

**Only 20 of 72 effects carry a standard error; 18 carry a CI.** The remaining 52 are honest
encodings of results the source published qualitatively (direction and significance only, no
magnitude) — `value: ±1.0` for a signed direction, `0.0` for an explicit null, with `se: null`.
**These are not poolable as continuous estimates** and must be consumed as direction/vote-count
evidence only. Twelve are encoded nulls. I never invented an SE (hard rule / conversion guidance).

**Of those 20, only ~7 are genuine sleep→structure magnitudes** (`cheng2021` ×1, `kocevska2017` ×2,
`mulder2019` ×2, `xu2025` ×1, `alvarezornelas2025` ×1). The rest are exposure distributions
(`lapidaire2021`, `urrila2017`), optima in hours (`fjell2023` ×3), reverse-direction MR
(`zhang2024` ×2), psychiatric or cognitive outcomes (`guldner2023` ×2, `xu2025` MoCA), a
state-correlation (`sun2020`) and a stability coefficient (`yang2022`). **Zero are per-hour volume
slopes in 16–19 year olds.**

**Cohort-family de-duplication (gate G6) — these families contribute multiple correlated effects:**

| `cohort_family` | Effects | Studies |
|---|---|---|
| `ABCD` | 10 | `cheng2021`, `limasantos2025`, `yang2022`, `chen2026` |
| `IMAGEN` | 10 | `urrila2017`, `lapidaire2021`, `guldner2023` |
| `Lifebrain_UKB_pooled` | 6 | `fjell2023` |
| `Generation_R` | 6 | `kocevska2017`, `mulder2019` |
| `Oslo_sleep_deprivation` | 5 | `elvsashagen2015`, `elvsashagen2017`, `voldsbekk2022` |

`ABCD`, `IMAGEN`, `Generation_R` and `Oslo_sleep_deprivation` each span multiple study records with
**overlapping participants** — do not treat them as independent. `fjell2023` itself pools Lifebrain
and UK Biobank, so it will overlap any other UK Biobank effect elsewhere in the factory.

**Records that must not be pooled without a flag:**

- `alvarezornelas2025` — largest volumetric reduction in the whole shard (−12.93 cm³, −1.78% total
  GM) but **no control arm** and **internally contradictory statistics**: OR 1.52 with 95% CI
  0.93–4.14 (crosses 1) reported as p = 0.01. Documented in the record's `rob` and `notes`.
- `canessa2011` — encoded `lab_restriction_within_subject` / T1 because treatment was deliberately
  administered and patients serve as their own controls, but it is an **uncontrolled pre-post**
  (n = 17); ROBINS-I would rate it serious. Exposure is OSA (hypoxaemia + fragmentation), not
  restriction.
- `wild2026` — n = 39, ~28 models, no stated multiplicity correction; and its direction
  (*"attenuated structural changes"*) is not obviously harm against a normatively **decreasing**
  trajectory.
- Animal records (`tuan2019`, `gay2024`, `howard2019`) — `cohort_family` set to `animal_mouse` /
  `animal_rat` so they cannot be pooled with human effects. Per-group n not recoverable → `n: null`.

**Sign convention applied throughout:** negative = worse/smaller for the subject. Every effect has a
`direction_note`, because several findings in this literature run *opposite* to the intuitive
direction (acute deprivation *increases* GM density and volume; short sleep associates with
*thicker* cortex in `fjell2023`; rodent sleep loss yields *more* synapses). A pooler that assumes
"less sleep → smaller brain" and flips signs to match will produce a badly wrong answer.

---

## 8. Verification status

All 30 included records: PMID resolved via PubMed `esummary`, DOI resolved via Crossref, PubMed's
DOI for each PMID matching the record's DOI, title similarity **1.000**, `status: VERIFIED`.
**Zero unresolved or fabricated identifiers.**

**One near-miss, caught and corrected (logged per hard rule 3).** My first-pass XML parser returned
DOI `10.1111/jsr.12373` for PMID 28181512 (`urrila2017`); Crossref resolved that DOI to a
*different* paper (*"Sleep and academic performance in later adolescence"*, *J Sleep Res*). Cause:
the parser was reading `<ArticleId>` nodes from the article's **reference list** as well as its own
`ArticleIdList`. Correct DOI is **`10.1038/srep41678`** (*"Sleep habits, academic performance, and
the adolescent brain structure"*, *Scientific Reports*), confirmed via Crossref. `abs.sh` was fixed
to read identifiers only from `PubmedData/ArticleIdList`, and all 30 records were then re-verified.
This is exactly the failure mode that hard rule 3 exists to catch, and it argues for programmatic
verification of every identifier in every shard rather than spot checks.
