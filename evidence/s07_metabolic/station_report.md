# Station report — shard `s07_metabolic`

Domain: glucose metabolism, insulin sensitivity, and type 2 diabetes risk from short sleep.
Deliverables: 30 YAML records, `screening_log.md`, `metabolic_summary.md`, this report.

## Headline counts

| metric | value |
|---|---|
| records screened | 54 |
| records included | 30 |
| effect estimates extracted | 105 |
| identifiers `VERIFIED` (Crossref **and** PubMed) | 29 / 30 |
| identifiers that failed to resolve | **0** |
| schema validation against `effect.schema.json` | **30 / 30 pass, 0 problems** |
| effects lacking a verbatim `quote` | **0** |
| tier mix | T1 = 18, T3 = 5, T5 = 3, TX = 4, **T2 = 0, T4 = 0** |
| access tier | full_text = 12, abstract_only = 17, secondhand = 1 |
| `adolescent_match` | exact_16_19 = 4, good_young_adult = 6, fair_adult = 5, poor_midlife = 12, mixed = 3 |

Gates: **G0 pass** (100% schema-valid), **G1 pass** (54 screened ≥ 25, and ≥ 30 as the task required),
**G2 pass** (every primary-model record VERIFIED; the single `CHECK` is a documented Crossref
subtitle artefact on `cappuccio2010`, whose DOI matches the DOI PubMed registers against its PMID).

## What I did

Worked the seven required extractions in order, then went looking for what the task's seed names
would have missed. Retrieval used PubMed E-utilities, Europe PMC REST (search + `fullTextXML`), NCBI
PMC efetch, Crossref, and Unpaywall. Five helper scripts in `_tools/` make the work reproducible:
`pmfetch.sh` (search/summary/abstract/Crossref), `x2t.py` (JATS/HTML → plain text for quoting),
`verify.py` (per-record DOI + PMID verification with title-similarity check → `_verify.json`),
`convert.py` (every effect-size conversion), `validate.py` (schema + hand checks). All arithmetic is
echoed to `_conversions.txt` with a CI back-check on each ratio, so any number in any record can be
re-derived without re-reading the sources.

Effect-size handling: ratios → `log_rr`/`log_hr`/`log_or` with `se = (ln(upper) − ln(lower))/3.92`;
where only a p-value and n existed, SE was backed out from the t-distribution and
`inferred_from_ci: true` set. Where p was published only as a **bound** (`nedeltcheva2009`,
`nedeltcheva2012`, `klingenberg2013`), I used the bound, which yields a **conservative** (upper-bound)
SE, and said so in `conversion_formula`. Where no SE was derivable I set `se: null` rather than
inventing one. That applies to 47 of 105 effects, but the figure needs unpacking: **25** are
deliberate placeholders encoding an explicit null or a direction-only flag (`value: 0` or `±1`, e.g.
`beals2026`'s clamp null, `dutil2024`'s restriction arm, `gao2020`'s continuous instrument), and
**22** are real magnitudes for which no dispersion was published — of which several are descriptive
point parameters that do not need an SE (`shan2015`'s 7.5 h nadir, `matthews2012`'s actigraphy-diary
discrepancy, `liu2025`'s age-of-maximal-association). The genuinely regrettable cases are
`spiegel1999`'s three magnitudes, `leproult2014`'s four percentages, `depner2019`'s two, and
`dutil2024`'s and `killick2015`'s headline percentages: **58 of 105 effects (55%) carry a usable SE**,
and every one that does not says why.

## Five findings that changed my own picture of this literature

1. **The MR literature is no longer null for short sleep.** Five earlier MR studies (`gao2020`,
   `wang2019`, `dashti2019`, `bos2019`) are null, and the natural conclusion — repeated in many
   reviews — is that sleep duration is not causal. **`kuroda2025` (April 2025) reports OR 1.12
   (1.02–1.23)**, significant, by meta-analysing DIAGRAM and FinnGen. Every earlier point estimate was
   positive and in the 1.12–1.18 range; they were underpowered, not contradictory. Had I stopped at
   the classic MR papers I would have filed a materially wrong conclusion.
2. **`kuroda2025` also lets the observational-vs-causal gap be computed *within one cohort*** —
   Cox HR 1.30 (self-report) or 1.52 (accelerometer) versus MR OR 1.12. Surviving fraction on the log
   scale: **0.43** or **0.27**. That is the shard's single most defensible answer to section (c), and
   it does not depend on comparing across incommensurable studies.
3. **Objective exposure measurement makes short sleep look *worse* and long sleep look *harmless*.**
   Same cohort, same paper: short-sleep HR 1.30 → **1.52** with accelerometry, long-sleep HR 1.46 →
   **1.08 (null)**, and the curve shape goes from U to J. Combined with MR (long sleep OR 0.80,
   P-non-linearity 0.94), **the long-sleep limb of the classic U-curve does not survive** — which
   matters directly, because the subject has occasional 10–11 h weekend nights.
4. **The severity of the canonical protocols is doing most of the work in the headline numbers.**
   The dose ladder in `metabolic_summary.md` §a.1 runs from HOMA-IR +65% at 4 h TIB for 3 nights
   down to HOMA-IR +0.27–0.30 units at 6.2 h — and to *nothing detectable* at 6.2 h for one week in
   adolescents. I went looking specifically for realistic-dose, long-duration protocols and found
   three the seed names did not mention: `zuraikat2024` (**6 weeks** at 6.2 h — the longest protocol
   in the literature), `nedeltcheva2009`/`nedeltcheva2012` (14 days at 5.5 h), and `dutil2024`.
5. **Measurement method is a first-order confounder, and it points one way.** `buxton2010` (IVGTT
   −20% vs clamp −11% in the same people), `nedeltcheva2012` (IVGTT −26% while OGTT and 24-h glucose
   were unimpaired, with the authors explaining *why* the IVGTT misleads under sleep loss),
   `sondrup2022` (whole-body effect real, peripheral effect absent), and `beals2026` (clamp + tracers,
   **null**) all agree: surrogate indices overstate the sleep effect. Any pooled estimate dominated by
   HOMA-IR and IVGTT studies is biased upward.

## What I could not find

- **No prospective cohort anywhere with objective sleep exposure and incident glycaemic outcomes in
  adolescents.** `adolescents polysomnography short sleep duration insulin resistance HOMA cohort`
  returned **zero** PubMed hits; a full Europe PMC sweep of the Penn State Child Cohort (35 records,
  all screened) produced no sleep-duration → insulin-resistance estimate. **This is why the shard has
  no T4 record**, and why all three age-matched observational records (`javaheri2011`, `matthews2012`,
  `chen2021`) are cross-sectional TX.
- **No T2 (quasi-experimental) evidence.** The school-start-time natural experiments exist and are in
  exactly the right age group, but their outcomes are weight and behaviour, not glycaemia
  (`37201593`, `30060859`, `28670711`, `38847813` — all screened and excluded). The instrument the
  factory would most want is unavailable for this outcome.
- **Only two randomised sleep-manipulation trials with a glycaemic outcome exist in adolescents**
  (`klingenberg2013`, `dutil2024`). That is the entire experimental base at the subject's age.
- **`spiegel1999`'s magnitudes are secondhand and its subjects' age is unpublished.** The *Lancet*
  1999 text is paywalled (Unpaywall `is_oa=false`, no PMC deposit). Design, n and p-values are
  first-hand from the abstract; the 30–40% figures come from two independently retrieved open-access
  sources. The abstract says only "11 young men", so `age_mean` and `age_range` are `null` — I declined
  to fill in the University of Chicago volunteer-pool range I could have guessed. The single most-cited
  study in this domain is the one whose numbers I am least able to stand behind directly.
- **No numeric effect size for `dutil2024`'s primary outcome and none for `beals2026`'s.** Both
  publish "significant, large effect size" / "no differences" without point estimates or CIs, and both
  full texts are publisher-blocked. `dutil2024` is the best age-matched trial in the shard and
  `beals2026` is the best-measured extension trial, so these two reporting gaps are costly.
- **`zuraikat2024`'s OGTT outcomes** (Matsuda, disposition index, glucose/insulin AUC) are listed as
  measured but not reported in the retrievable abstract. I recorded this as a selective-reporting
  concern rather than inferring nulls.
- Publisher blocking was pervasive: Europe PMC `fullTextXML` returned 0 bytes, or NCBI PMC returned
  "The publisher of this article does not allow downloading of the full text in XML form", for OUP
  (*Sleep*), the ADA (*Diabetes Care*), *Annals of Internal Medicine*, and Cell Press (*Current
  Biology*). Hence 17 `abstract_only` records. Where an abstract published dispersion directly
  (`zuraikat2024` gives β ± SEM; `nedeltcheva2009` gives means ± SD with p-values) no precision was
  lost; where it did not, `se: null` is set with a reason.

## Where I am confident, and where I am not

**Confident.** (i) The direction and rough magnitude of the acute effect at realistic doses: a
HOMA-IR shift of a few tenths of a unit, or ~10–11% by clamp, at 6 h/night sustained for weeks.
(ii) That the classic 40–65% figures are protocol artefacts and must not be transported to this
subject. (iii) That the long-sleep limb of the U-curve is not causal. (iv) That timing/regularity is
at least as important as duration — five independent lines converge (`leproult2014`, `yuan2021` vs
`buxton2012_fd`, `cheung2026`, `chen2021`, `gao2020` insomnia, `liu2025` chronotype).
(v) That roughly a quarter to a half of the observational short-sleep excess survives causal scrutiny.

**Not confident.** (i) **Reversibility magnitude.** Three surrogate-index trials say extension helps
(+45%, +20%, −0.79 HOMA-IR); the one clamp-with-tracers trial says it does nothing. I graded this
**C on model dependence** and flag it for the red-team station rather than papering over it.
(ii) **Any long-run number for an 18-year-old.** Graded **D on transportability** — a GUESS under
`gates.md` — because no adolescent cohort exists and `liu2025` shows the association *attenuating*
with age above 30 with no data below 30, so even the direction of the age extrapolation is uncertain.
(iii) **Whether weekend catch-up helps.** Experiments say insufficient (`depner2019`, `cheung2026`);
NHANES says it helps precisely in the subject's stratum (`wang2025_wsr`, males with weekday sleep
≤7 h) — but only with the circadian penalty statistically removed, and on a rescaled outcome.
(iv) **Glucose effectiveness**, where `spiegel1999` (−30%) and `nedeltcheva2009` (+15%) flatly
disagree in sign; I flagged it as sign-unstable and excluded it from the headline numbers.

## Three traps I have flagged for downstream stations

1. **Unit hazard.** `wang2025_wsr`'s βs are on a HOMA-IR index **rescaled to 0–100**;
   `zuraikat2024`'s (+0.30) and `hartescu2022`'s (−0.79) are **raw** HOMA-IR units. The rescaling
   bounds are not recoverable, so **no conversion factor exists**. Pooling them together would be a
   serious error, and the numbers look superficially comparable, which is what makes it dangerous.
2. **Tier mismatch inside `kuroda2025`.** Tiered T3 because MR is the primary design, but effect 4
   (accelerometer <6 h, HR 1.52) is properly **T4** — one of very few in existence — and effect 5 is
   properly **T5**. Effects 1–3 and 4–5 are not independent.
3. **Explicit nulls are encoded `value: 0, se: null`** in seven records. These are reported
   non-significances with **unknown** confidence intervals, not zero-variance estimates. `beals2026`
   is the important case: because no CI is published, the effect sizes it can exclude are unknown, so
   it cannot be used to bound the reversibility effect quantitatively — only to widen the posterior.

## The single biggest gap in the evidence for this domain

**Nothing connects the acute, well-measured, reversible metabolic changes to long-run disease risk at
the subject's age.** The two halves of this shard do not touch:

- The **experimental** half is T1, mechanistically clean, partly age-matched, and measures insulin
  sensitivity over 3 nights to 6 weeks. It says the effect is real, modest at realistic doses, and
  largely reversible.
- The **epidemiological** half is T5/T3, measures incident diabetes over 10–14 years, and is entirely
  drawn from cohorts with median ages of 49–58.

There is **no study of any design** that follows adolescents with objective sleep measurement to a
glycaemic endpoint, and **no** experimental protocol longer than 6 weeks. So the inference "3 years of
weekday short sleep at ages 16–19 moved this subject's diabetes risk by X" is not an extrapolation
along a measured curve — it requires two unmeasured assumptions: that a transient insulin-sensitivity
decrement in adolescence leaves a durable trace after the exposure ends, and that midlife per-hour
risk coefficients apply to adolescent exposure. **Neither is tested anywhere in this literature.**
The evidence that bears on the first is mildly discouraging for the "durable trace" view — every
recovery record shows the acute changes reverse when sleep is restored, and `killick2015` shows
reversal after a *five-year* history of weekday restriction — which argues that the subject's risk,
having now returned to adequate sleep, should be modelled as **largely recovering**, with the residual
long-run increment small (of order 2–4% relative) and labelled a GUESS.

If one further record could be obtained, I would spend it on the full text of
**PMID 37792965** (Morales-Ghinaglia et al., *Sleep* 2024, Penn State Child Cohort): median age 16,
≥5 nights actigraphy plus PSG, with sleep midpoint, sleep irregularity and social jetlag as exposures
— the subject's exact pattern, at his exact age. Its published effects are effect-modification terms
on a composite metabolic-syndrome score, so I could not extract a glycaemia-specific estimate from the
abstract, and the full text is publisher-blocked. It is the closest thing in existence to a study of
this subject.
