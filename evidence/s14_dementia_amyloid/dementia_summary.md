# Long-run neurodegeneration: the glymphatic/amyloid chain and the sleep-duration dementia epidemiology

Shard `s14_dementia_amyloid`. 77 records screened, 38 included, 104 extracted effects, 40/40 identifiers
verified against Crossref *and* PubMed, 104/104 quotes machine-audited back to retrieved source text.

---

## Bottom line

**The popular claim "sleep loss causes Alzheimer's" is a chain of seven inferential links. Links 1-3 are
supported for *total* sleep deprivation in *acute* human experiments. Link 4 — that partial chronic
restriction does the same thing — is the one the subject's exposure actually needs, and the direct
evidence points *against* it. Links 5-7 are unevidenced or contested. Link 8, adolescent exposure, has
zero supporting data.**

**Verdict on a numeric dementia-risk delta for this subject: NOT DEFENSIBLE.** Not "small", not
"uncertain but positive" — not defensible as a number. The recommended encoding for this channel is a
point estimate of zero with an explicitly wide, sign-ambiguous prior, plus the qualitative note that
the direction of prudent advice still favours more sleep. Reasons, in order of force:

1. The 2024 Lancet standing Commission reviewed exactly this question and placed sleep in the
   *insufficient evidence* bin, issuing no population attributable fraction (`livingston2024`).
2. Every Mendelian randomization study located — five of them, plus three cohort papers that ran their
   own MR — finds no causal effect of sleep duration on dementia or AD (`henry2019`, `anderson2021`,
   `huang2020`, `guo2024`, `xiang2024`, `yuan2022`, `xiong2024`, `tao2026`).
3. In the largest dose-response synthesis, risk is *minimised* at 5.6-6 h of nocturnal sleep and rises
   significantly only below 4 h — the subject's weekday 5-6 h sits at or beside the nadir (`xu2020`).
4. The lab study that most closely matches the subject's exposure — 5-8 nights of 4 h sleep, slow-wave
   sleep preserved — found **no change** in any amyloid or neurodegeneration CSF biomarker
   (`olsson2018`).
5. Every exposure measurement in every dementia study is at age 45 or older. Extrapolating to age 19
   spans five decades with no data.

**The blunt statement in the other direction:** this is not a "sleep doesn't matter" finding. It is a
"this specific scary channel cannot carry a number" finding. Long sleep, daytime sleepiness, insomnia
and sleep apnoea all have *better* dementia evidence than short sleep duration — and none of those is
the subject's phenotype. And the reason short sleep has weak dementia evidence is not that it was shown
harmless; it is that the exposure has never been measured in anyone young enough to matter.

---

## Part 1 — The mechanistic chain, link by link

### Link 1: Does sleep increase clearance of metabolites from the brain?
**Status: DISPUTED IN THE ORIGINATING SPECIES.**

`xie2013` (Science, PMID 24136970) is the glymphatic paper. **Species: mouse.** Exposure: acute natural
sleep or ketamine/xylazine anaesthesia versus forced wakefulness. Measured: clearance of an *injected
radiolabelled tracer* (¹²⁵I-Aβ₁₋₄₀) plus interstitial space volume by tetramethylammonium
iontophoresis. Numbers: clearance approximately **2-fold faster** in sleeping mice; interstitial volume
fraction rose **>60%, from 13.6 ± 1.6% awake to 22.7 ± 1.3% anaesthetised in the same mice (n = 10,
P < 0.01)**.

What it is not: it is not a measure of endogenously produced Aβ, not a measure of plaque, not a
cognitive outcome, and not human.

`miao2024` (Nature Neuroscience, PMID 38741022) measured clearance of fluorescent tracers in mouse
brain and reached the opposite conclusion, titled "Brain clearance is **reduced** during sleep and
anesthesia". Awake saline controls cleared **70-80%** of tracer at peak; anaesthesia substantially
reduced this.

*Uncertainty at this link:* two mouse studies, opposite signs, different tracers and methods. The
foundational premise of the whole channel is contested within its own species. Note also that the
subject is not a mouse and is not anaesthetised.

### Link 2: Does acute sleep loss raise brain/CSF Aβ in humans?
**Status: WELL REPLICATED — for total deprivation.**

`shokrikojori2018` (PNAS, PMID 29632177): **n = 20**, within-subject florbetaben PET after rested
wakefulness versus one night of total sleep deprivation. The cluster was **right hippocampal /
parahippocampal / thalamic**; SUVr rose from 1.35 (SD 0.06) to 1.42 (SD 0.07), **a 5% increase,
P < 0.0001, in 19 of 20 participants**. Right-hippocampus ROI Cohen's d = 0.48 (P = 0.046); left
hippocampus null (P = 0.4). Between-subject range of individual change: **−0.58% to +16.1%**.

`ooms2014` (JAMA Neurology, PMID 24887018): **n = 26** middle-aged men. A night of unrestricted sleep
produced **a 6% decrease in CSF Aβ42 of 25.3 pg/mL (95% CI 0.94-49.6, P = .04)**, "whereas sleep
deprivation counteracted this decrease"; between-arm difference **75.8 pg/mL (95% CI 3.4-148.4,
P = .04)**.

Replicated twice more: `blattner2020` (n = 11; overnight CSF **Aβ40 +9.1%, SE 2.9, 95% CI 3.4-14.8,
p = 0.002**; **Aβ42 +8.6%, SE 3.1, 95% CI 2.4-14.9, p = 0.007**), and `forsberg2025` (crossover; Aβ40,
Aβ42 and p-tau significantly lower after sleep than after total deprivation). `lucey2018` found mean
overnight CSF Aβ38/40/42 **30% above each participant's own daytime baseline** under deprivation.

*Uncertainty at this link:* low for the existence of the effect, high for its meaning. Total sample
across all four human studies is 65 people, all middle-aged or adult, all exposed to **zero** hours of
sleep. A 5% PET SUVr change is a soluble-pool signal in a tracer that is not specific to fibrillar
plaque over a single night.

### Link 3: Is the mechanism impaired clearance?
**Status: REFUTED IN HUMANS. This is the most under-reported finding in the field.**

`lucey2018` (Annals of Neurology, PMID 29220873) used stable isotope labelling kinetics to separate
production from clearance. "Formal modeling analysis revealed that the FTRs and delay times were not
significantly different between groups … which strongly suggests a lack of sleep pattern on the overall
clearance processes of brain peptides." The overnight rise was driven by **increased production**, not
by failed clearance. `blattner2020` independently excluded stress and circadian mediation (plasma
cortisol overnight difference +1.9%, 95% CI −13.3 to 17.1, p = 0.81).

*Consequence:* the human data support "staying awake makes more Aβ" and not "sleeping washes Aβ out".
Those are different claims with different implications. A production-side transient that resolves when
neuronal activity normalises is a far weaker basis for cumulative damage than a clearance deficit
would be.

### Link 4: Does *partial chronic* restriction — the subject's actual exposure — do the same thing?
**Status: NOT SUPPORTED. The direct evidence points the other way. This is the load-bearing failure.**

- `olsson2018` (Sleep, PMID 29425372): **5-8 consecutive nights of 4 h sleep** in healthy young adults.
  "No PSD-related changes in CSF biomarkers for amyloid build-up in the brain, Alzheimer's disease
  (AD)-type neurodegeneration, or astroglial activation were observed." CSF orexin rose 27%
  (p = 0.001), proving the protocol was biologically potent. The authors attribute the null to
  **preserved slow-wave sleep**.
- `ju2017` (Brain, PMID 28899014): selective slow-wave disruption raised CSF Aβ40 (r = 0.610,
  P = 0.009), and "this effect was specific for slow wave activity, **and not for sleep duration or
  efficiency**."
- `skorucak2021` (Sleep, PMID 33893807) — **the only adolescent record in this shard**: 34 adolescents,
  5, 7.5 or 10 h sleep opportunity for five nights in a protocol explicitly "designed to mimic a school
  week between two weekends". Slow-wave activity homeostasis was preserved.
- `livingston2024`, the Lancet Commission, states the objection independently: impaired amyloid-β
  clearance "usually occurs during deep sleep at the beginning of the night, which lasts one to two
  hours **so is unlikely to be affected in those reporting sleep disturbances**."

*Synthesis of this link:* the mechanism requires slow-wave sleep to be lost. Partial restriction
preferentially preserves slow-wave sleep — including in adolescents specifically — and when slow-wave
sleep is preserved, the biomarkers do not move. The subject restricts total time in bed; he does not
selectively ablate slow-wave sleep, and his 7-8 h weekends and holidays provide further slow-wave
opportunity. **The chain breaks here, at exactly the link his exposure would have to traverse.**

### Link 5: Does the acute rise reverse with subsequent normal sleep?
**Status: LIKELY YES, BUT NEVER DIRECTLY DEMONSTRATED. Evidence is thin — this must be stated plainly.**

This was flagged as the single most important question in the shard. The honest answer: **no human study
has measured Aβ before deprivation, after deprivation, and again after recovery sleep in the same
people.** A targeted search (`recovery sleep amyloid beta reversal`) returned three records, all rodent.

Four indirect lines converge on reversal:
1. `blattner2020`: the overnight window moved ~9%, but the **36-hour mesor did not move at all**
   (+2.97%, 95% CI −15.3 to 21.2, F(1,10) = 0.13, **p = 0.72**), nor amplitude (p = 0.52), acrophase
   (p = 0.72) or linear rise (p = 0.58). A perturbation of curve *shape* without a shift in *level*.
2. `lucey2018`: the rise is production-side, not clearance-side (Link 3), so it should resolve when
   wake-driven neuronal activity normalises.
3. `forsberg2025`: a crossover design with washout in which participants returned to baseline between
   conditions.
4. `olsson2018`: **5-8 consecutive nights** of restriction produced no biomarker change — which is hard
   to reconcile with a non-reversing overnight increment. If each short night left a residue, eight
   consecutive short nights should have shown one.

*Why this matters so much:* if the overnight elevation fully reverses, the mechanism does not
straightforwardly imply cumulative damage from intermittent restriction, and the entire "each bad night
adds up" framing loses its basis. The evidence favours reversal but is circumstantial. Confidence:
moderate, not high.

### Link 6: Do repeated transient elevations accumulate into plaque?
**Status: NO DIRECT HUMAN EVIDENCE. Pure inference.**

Nothing in the retrieved literature measures cumulative amyloid deposition as a function of a number of
short nights in humans. `olsson2018` is the only multi-night attempt and it is null. This link is
carried entirely by plausibility.

### Link 7: Does the sleep-related amyloid signal translate into dementia decades later?
**Status: WEAK, AND PLAUSIBLY PRODROMAL. See Parts 2-4.**

### Link 8: Does sleep restriction in adolescence affect dementia risk 50-60 years later?
**Status: INSUFFICIENT EVIDENCE. See Part 6.**

---

## Part 2 — Epidemiology, with exposure ages stated

Every estimate below has an exposure age of 45+. **The youngest sleep measurement in the entire dementia
literature located by this shard is at mean age 50.6 years (`sabia2021`).**

### The anchor study
`sabia2021` (Nature Communications, PMID 33879784), Whitehall II. **7,959 participants; 521 incident
dementia cases; mean follow-up 24.6 (SD 7.0) years; mean age at diagnosis 77.1 (SD 5.6) years.**
Sleep ≤6 h vs 7 h referent, fully adjusted:

| Exposure age | HR (95% CI) | log_hr | SE | Mean follow-up |
|---|---|---|---|---|
| 50 | **1.22 (1.01-1.48)** | 0.199 | 0.097 | 24.6 y |
| 60 | **1.37 (1.10-1.72)** | 0.315 | 0.114 | 14.8 y |
| 70 | **1.24 (0.98-1.57)** — the paper's own word is "imprecisely estimated" | 0.215 | 0.120 | 7.5 y |
| Persistent short at 50 *and* 60 *and* 70 | **1.30 (1.00-1.69)** | 0.262 | 0.134 | 7.4 y |
| Accelerometer, lowest tertile | **1.63 (1.04-2.57)** | 0.489 | 0.231 | 6.4 y |

Three features deserve emphasis. The age-50 lower bound is **1.01**. The persistent-short-sleep lower
bound is **exactly 1.00** — this is the "30% higher risk" figure that circulates without its interval.
And the association is *largest* when sleep is measured *closest* to diagnosis, which is what reverse
causation predicts. Questionnaire-accelerometer correlation in the same people was only **r = 0.41**.

### Meta-analyses

| Study | Exposure | Pooled estimate | I² | Follow-up |
|---|---|---|---|---|
| `fan2019` (7 cohorts) | short sleep → all-cause dementia | **HR 1.20 (0.91-1.59)** — NULL | — | — |
| `fan2019` | short sleep → AD | **HR 1.18 (0.91-1.54)** — NULL | — | — |
| `fan2019` | **long** sleep → dementia | **HR 1.77 (1.32-2.37)** | — | — |
| `xu2020` (13 cohorts, 53,014, 6,892 cases) | shortest nocturnal → dementia/cognitive decline | **RR 1.18 (1.01-1.37)** | **57%** | 1-22.6 y, ages 51-83 |
| `xu2020` (3 cohorts, 32,555, 4,115 cases) | shortest nocturnal → **AD** | **RR 1.02 (0.76-1.36)** — EXACTLY NULL | 54% | as above |
| `xu2020` | **longest** nocturnal → **AD** | **RR 1.57 (1.33-1.85)** | **0%** | as above |
| `wu2018` (9 studies, 22,187) | shortest → cognitive disorders | **RR 1.34 (1.15-1.56)** | — | nadir 7-8 h |
| `liang2019` (9 studies, 62,937) | per +1 h → MCI/dementia | **RR 0.98 (0.97-1.00)** | 0% | nadir ~7 h |
| `bubu2017` (27 studies, 69,216) | "sleep problems" → AD | **RR 1.55 (1.25-1.93)** | — | lumped exposure |
| `howard2024` (31 studies) | brief sleep, **follow-up >10 y** | **RR 1.12 (0.95-1.29)** — NULL | 65.9% | >10 y |
| `howard2024` | brief sleep, follow-up ≤10 y | RR 1.46 (interval mis-printed as 1.48-1.77; see erratum PMID 40022863) | 88.9% | ≤10 y |

**Two structural facts jump out of this table.**

*First, the AD-specific short-sleep estimate is null while the long-sleep estimate is the strongest and
most homogeneous result in the literature* (`xu2020`: 1.02 vs 1.57 with I² = 0%; `fan2019`: 1.18 null vs
1.77). The mechanism under evaluation predicts short sleep should drive amyloid and therefore AD. That
is the direction that fails. Long sleep has no clearance rationale at all.

*Second, the dose-response nadir is not where the narrative assumes.* `xu2020`: "the optimal duration
was found to be roughly **5.6-6 hours** for lower risk of cognitive disorder and 5.6-7 hours for lower
risk of AD. The risk … will be significantly elevated when the nocturnal sleep duration is **over 10
hours or less than 4 hours**." `wu2018` and `liang2019` put the nadir at 7-8 h and ~7 h respectively, so
the exact location is unstable — but **no** dose-response analysis places the subject's weekday 5-6 h on
a steeply rising limb, and one places it at the minimum. The subject's occasional 10-11 h weekend nights
fall closer to a category these studies actually flag.

### How consistent is this literature?
`deckers2024`, an umbrella review of 148 systematic reviews (608 primary studies) plus an 18-expert
Delphi, counted how many reviews of each candidate risk factor found an association:

- **Short sleep duration: 5 of 16 reviews positive, 11 null → 31% consistency.**
- Long sleep duration: 7 of 16 → 44%.
- Poor sleep quality 50%, insomnia 44%, sleep-disordered breathing 40%, **daytime sleepiness 5/5 = 100%**.
- For calibration: olfactory impairment 100%, atrial fibrillation 79%, hearing impairment 78%.

Short sleep duration is near the bottom of a 30-factor list. Note also that the experts, asked which
sleep construct to target, chose **sleep-disordered breathing** — not duration.

---

## Part 3 — Reverse causation, quantified

This is the central problem in the literature, and it is quantifiable from four independent angles.

**(1) Dating the signal.** `you2024` (Molecular Psychiatry, PMID 38678085) screened **400 predictors**
against consecutive pre-diagnosis timeframes out to 15 years in **7,620 UK Biobank incident dementia
cases**. Grip strength (OR 0.65, 0.63-0.67), peak expiratory flow (OR 0.78), cystatin C (OR 1.13),
coronary heart disease, diabetes and multiple mental disorders were all detectable **15 years** before
diagnosis. Sleep duration was **not**. It appeared only in the **3-5 year** window (OR 1.13, 1.04-1.24),
"only exhibited associations within five years before the diagnosis", in the same terminal bin as
weight loss and inactivity. The study was abundantly powered to see a 15-year sleep signal — grip
strength's SE was 0.016 — and there was none.

**(2) Follow-up stratification.** `howard2024` (31 studies): brief sleep RR 1.46 with follow-up ≤10 y,
falling to **RR 1.12 (0.95-1.29), non-significant**, with follow-up >10 y. The authors' reading is that
short sleep is prodromal rather than causal. **But this is contested:** `vanwanrooij2025` performed lag
analyses in a Dutch cohort (2,218 participants, 237 dementia cases over 1992/3-2015/6) and found
associations *strengthened* at lag times ≥15 years, and that at short lag (3 years) it was long sleep
(≥9 h) that was associated. Two competent analyses, opposite conclusions. **This specific question is
UNRESOLVED**, and the shard does not pretend otherwise.

**(3) Design-induced inflation, measured within one study.** `tao2026` (CHARLS): identical exposure
definition, identical cohort, **cross-sectional OR 2.99 (2.47-3.62)** versus **longitudinal HR 1.55
(1.25-1.91)** — the log-scale estimate falls by roughly 60% (1.095 → 0.438) simply by measuring sleep
before the outcome rather than alongside it.

**(4) Long-sleep attenuation, which is uncontested.** Via `livingston2024`: in a Swedish cohort of
28,775 people, "the association between long sleep duration and dementia over a 13-year follow-up was
**completely attenuated** after cases occurring in the first 5 years of follow-up were excluded"; and in
the Million Women Study, "there was **no association** between long sleep duration (>8 hours) or daytime
napping and dementia on longer term follow-up after the first five years."

**(5) The direction of causation has been measured directly, and it runs backwards.** `huang2020`
(Neurology, PMID 32817390) found that **genetic liability to AD causes shorter sleep**: self-reported
β = −0.006 (p = 1.9 × 10⁻⁴) and accelerometer-based β = −0.015 per unit AD liability, with no forward
effect. `anderson2021` estimated the reverse-direction magnitude at roughly **0.3 minutes** — real,
detectable, and tiny.

**Additional supporting sign:** the short-sleep association is *unstable in the way confounded
associations are unstable*. `xiong2024` found short sleep predicted **lower** dementia risk in adults
aged 70+ and higher risk in the younger-old, in one cohort with one instrument. A cumulative neurotoxic
mechanism cannot flip sign across a five-year age band.

*Quantified summary of this section:* of the roughly +0.16 to +0.26 log-hazard attributed to short sleep
in the best cohort and meta-analytic estimates, follow-up stratification removes about half or all of it
(`howard2024`: 0.378 → 0.113, non-significant), timing analysis localises what remains to the final 3-5
years before diagnosis (`you2024`), design comparison shows ~60% inflation from measurement timing
(`tao2026`), vascular-risk adjustment attenuates it further and MR removes the remainder (`guo2024`).
**There is no residual after these four operations that has been shown to be causal.**

---

## Part 4 — Mendelian randomization: the cleanest evidence, and it is null

Five dedicated MR studies plus three cohort papers with embedded MR. **Every one fails to support short
sleep duration causing dementia or AD.**

| Study | n / source | Forward: sleep duration → AD/dementia | Notable |
|---|---|---|---|
| `henry2019` | 395,803 | AD **OR 0.89 (0.67-1.18)** per +1 h; all-cause dementia **OR 1.19 (0.65-2.19)** — both null | +1 h → 1% slower reaction time, 3% more visual-memory errors, i.e. *more* sleep looked mildly worse |
| `anderson2021` | 54,162 AD cases/controls | "little evidence to support a causal effect of sleep traits on AD risk" | Napping **protective, OR 0.70**; reverse direction ≈ 0.3 min |
| `huang2020` | 446,118 | No forward effect | **Reverse effect positive**: AD liability → shorter sleep |
| `guo2024` | 502,383 | No MR support for any sleep characteristic on dementia | **Positive control works**: insomnia → stroke **OR 1.31 (1.13-1.51), p = 0.00072** |
| `xiang2024` | GWAS consortia | **OR 1.002 (1.000-1.004)** IVW; **1.004 (1.000-1.007)** MVMR | The *only* nominally positive result, and it says **LONGER** sleep raises AD; magnitude operationally nil |
| `yuan2022` | 483,507 | "no causal association" | Also **no gene × sleep interaction, p = 0.45** |
| `xiong2024` | 7,223 | "did not reveal causal associations" | Cohort found associations; own MR did not |
| `tao2026` | CHARLS + MR | Duration untested causally | Insomnia → dementia **OR 1.06 (1.01-1.13)** — a *different* construct |

The `guo2024` positive control matters enormously: the same MR machinery, in the same biobank, detects
insomnia → stroke at p = 0.0007. The method is not blind. It sees things that are there.

**What MR settles and what it does not.** MR estimates the effect of *lifelong genetically predicted
average* sleep duration — the right target for "does habitually shorter sleep cause dementia", and the
answer is no. It is the *wrong* target for "does three years of behaviourally imposed restriction at
ages 16-19 cause dementia at 70", because no genetic instrument varies on that schedule. So the MR nulls
strongly undercut the general causal claim while leaving a narrow, untested, window-specific hypothesis
formally alive. **A hypothesis that is merely not excluded is not a basis for a numeric risk delta.**

---

## Part 5 — Biomarker cohorts: does short sleep in midlife predict later amyloid?

**No study measures sleep in midlife and amyloid decades later. The closest is 15.7 years, and its
exposure is sleepiness, not duration.**

| Study | Design | Exposure age | Effect |
|---|---|---|---|
| `spira2013` | cross-sectional, n = 70 | ~76 y | Per hour *less* sleep: mean cortical PiB DVR **B = 0.08 (0.03-0.14), p = 0.005**; precuneus **0.11 (0.03-0.18)** |
| `winer2021` | cross-sectional, n = 4,417 | elderly | Shorter sleep ↔ higher Aβ, **β = −0.01 (SE 0.00), p = .005**; short vs normal **0.01 (SE 0.01), p = .048**; **long vs normal: NO difference** |
| `spira2018` | prospective, n = 124 | mean 60.1 y | **Excessive daytime sleepiness → Aβ+ 15.7 y later, OR 2.75** (adjusted). Longest lag available — but exposure is EDS, not duration |
| `winer2020` | prospective, PSG, n = 32 | elderly | Baseline proportion of <1 Hz NREM SWA predicted Aβ accumulation rate (**r = −0.52**); total sleep time **r = −0.36, p = 0.04**; **no sleep measure predicted cognitive change** |
| `lucey2019` | cross-sectional, n = 119 | elderly | NREM SWA tracks **TAU**, not amyloid (AV-45 associations did not survive multiple-comparison correction); gross sleep parameters null |
| `tortcolet2026` | prospective, serial PET, n = 417 | mean 63 y | **MAIN EFFECT NULL**: PSQI × time β = 0.04 (−0.04 to 0.11), p = 0.352. Amyloid-**negative** stratum (n = 309) **null: 0.03 (−0.04, 0.09)**. Positive only in the 85 grey-zone participants (0.28, 0.06-0.50). In amyloid-positive participants the sign **reverses** (−0.41, −0.73 to −0.10, p = 0.010) |

The `tortcolet2026` stratification is the most decision-relevant result in this section. **The
sleep-amyloid link appears only in people who had already begun accumulating amyloid.** In the 309
participants who had not, the coefficient is 0.03 with an interval spanning zero. If the association
requires pre-existing pathology to manifest, it is a modifier of an ongoing disease process in older
adults, not an initiator of pathology in the young — and extrapolating it backwards to adolescence is
misconceived. The authors call their own finding "hypothesis-generating rather than confirmatory".

Note also the internal incoherence of the biomarker and epidemiological literatures taken together:
**short sleep has an amyloid signal but no AD signal; long sleep has an AD signal but no amyloid
signal** (`winer2021` found no long-vs-normal amyloid difference; `xu2020`/`fan2019` found long sleep
the strongest AD predictor). Amyloid cannot be the mediator of the long-sleep association, and if it is
not, the field's only mechanistic bridge does not carry the traffic the epidemiology puts on it.

---

## Part 6 — The critical age question: **INSUFFICIENT EVIDENCE**

**There is no study of sleep restriction in adolescence and dementia risk in later life. None. This is
an absence, not a weak signal.**

The search `adolescent sleep dementia risk later life` returned 8 records: CSF clearance in aging
autistic adults, an anxiety/depression review, a dementia GWAS, a white-matter study in middle-aged
adults, and four Cochrane reviews of sleep interventions in adults aged 60+. Not one had adolescent
sleep as exposure and dementia as outcome.

What exists at the edges:
- `skorucak2021` (PMID 33893807) is the only record in this shard with an adolescent population
  (n = 34, ages matched to the subject). It shows slow-wave homeostasis is **preserved** across five
  nights of 5 h sleep opportunity in a simulated school week. Outcome is sleep EEG, not
  neurodegeneration. Its bearing on the channel is to weaken it, by showing the mechanistically
  required stage is defended in exactly this population.
- `komlo2026` (PMID 41959309) is the only study framed on early-life chronic short sleep and long-run
  cognitive decline. It is a **mouse bioRxiv preprint with no extractable effect sizes**, the exposure
  begins in *young adult* mice and is never withdrawn, and its proposed mechanism is **proteostasis /
  ER stress / unfolded protein response — amyloid is not mentioned at all.** So the single most
  age-relevant experimental study pointing toward harm does not support the amyloid mechanism this
  shard was asked to evaluate.
- `park2025` (PMID 41614054, verified; excluded — `screening_log.md` row 39) is a **published protocol**,
  not results, for exactly the adjacent question (midlife short sleep × obesity → dementia in
  Whitehall II, to 2023). Future tense throughout, so there is nothing to extract. Two of its authors
  wrote `livingston2024` and `sabia2021`, and they still describe the exposure as "a putative risk for
  dementia" against obesity as "an well-known risk factor" *(sic)*. The best available test of this
  shard's question is running but has not reported.

**Explicit statement required by the task:** any number this factory produces for the adolescent
dementia channel is **an extrapolation across five decades with no supporting data**. It would require
assuming, without evidence: (a) that the acute mechanism operates under partial rather than total
restriction — contradicted by `olsson2018`; (b) that it operates in adolescents whose slow-wave sleep is
preserved — contradicted by `skorucak2021`; (c) that transient elevations fail to reverse — contradicted
on balance by four indirect lines; (d) that they accumulate irreversibly over three years — no evidence
either way; (e) that such accumulation persists through fifty subsequent years of normal sleep — no
evidence either way; and (f) that the resulting burden translates into clinical dementia at the rate
implied by cohorts whose exposure was measured at age 50-70 — undercut by null MR and by the
prodromal timing evidence.

---

## Part 7 — Which links in the popular chain are evidenced

| Link | Claim | Status | Best evidence | Uncertainty |
|---|---|---|---|---|
| 1 | Sleep drives brain metabolite clearance | **DISPUTED** | `xie2013` (mouse, ~2× clearance, +60% interstitial volume) vs `miao2024` (mouse, reduced) | Opposite signs within one species |
| 2 | One night without sleep raises human Aβ | **SUPPORTED** | `shokrikojori2018` **5%**, n = 20; `ooms2014`; `blattner2020` **+9.1%/+8.6%**; `forsberg2025` | 65 people total, all exposed to 0 h sleep; individual range −0.58% to +16.1% |
| 3 | Because clearance is impaired | **REFUTED (humans)** | `lucey2018`: turnover rates unchanged; production increased | Low — the kinetic study is direct |
| 4 | Partial chronic restriction does the same | **NOT SUPPORTED** | `olsson2018` null over 5-8 nights of 4 h; `ju2017` "not for sleep duration"; `skorucak2021` | n = 13 in the key null; underpowered but the only direct test, and it points against |
| 5 | The acute rise does not reverse | **AGAINST, indirectly** | `blattner2020` mesor p = 0.72; `lucey2018`; `forsberg2025`; `olsson2018` | No direct test exists anywhere. Moderate confidence only |
| 6 | Transient rises accumulate into plaque | **NO EVIDENCE** | — | Total |
| 7 | Which causes dementia decades later | **WEAK / PLAUSIBLY PRODROMAL** | `sabia2021` HR 1.22-1.37 at ages 50-60; `xu2020` AD **RR 1.02**; 31% review consistency; no MR supports short sleep → dementia | Reverse causation unresolved; long-sleep asymmetry unexplained |
| 8 | Adolescent restriction → dementia at 70 | **INSUFFICIENT EVIDENCE** | Nothing | Complete |

**Where the popular chain actually breaks: at Link 3 (the mechanism is production, not clearance) and
decisively at Link 4 (partial restriction preserves slow-wave sleep and moves no biomarker).** Links 2
and 7 are real findings about different exposures in different people, and joining them requires Links
3-6, which do not hold.

---

## Part 8 — Verdict on a numeric dementia-risk delta for this subject

**A numeric dementia-risk delta for a 19-year-old with this sleep pattern is not defensible. Recommended
encoding: point estimate 0, wide sign-ambiguous prior, channel excluded from the headline damage total
and reported qualitatively.**

The four independent reasons, each sufficient on its own:

1. **Authority.** The 2024 Lancet standing Commission examined this literature and refused to quantify
   it: "there is not enough consistent evidence to meet our high bar of being included as modifiable
   risk factors. These include too little sleep …" and "We are unable to make recommendations on sleep as
   a risk factor." It also pre-empts the inverse error: **"People should not curtail their sleep to
   reduce dementia risk."**
2. **Causal identification.** Eight MR analyses, one working positive control (`guo2024`: insomnia →
   stroke, p = 0.0007), zero support for short sleep → dementia. One nominally positive result, pointing
   at *long* sleep, at OR 1.002.
3. **Exposure mismatch on three axes simultaneously.** Age: 50-70 measured versus 19 required. Dose:
   0 h acute or ≤5 h habitual-in-the-elderly versus 5-6 h on weekdays with 7-8 h recovery. Construct:
   the sleep phenotypes with real dementia evidence are sleep apnoea, insomnia, daytime sleepiness and
   *long* sleep — none of which is a healthy 19-year-old voluntarily curtailing sleep who sleeps normally
   when allowed to.
4. **Dose-response location.** `xu2020` places the risk minimum at **5.6-6 h** of nocturnal sleep with
   significant elevation only below 4 h; `wu2018` and `liang2019` place it at 7-8 h and ~7 h. The
   subject's weekday sleep is inside or adjacent to the nadir on all three curves, not on a rising limb.

**If the downstream model is nonetheless required to emit a number**, the only quotable anchor is
`sabia2021`'s persistent-short-sleep estimate: **HR 1.30 (95% CI 1.00-1.69), log_hr 0.262, SE 0.134**,
for sleep ≤6 h sustained at ages **50, 60 and 70**. It must be transported with every one of these
flags: the lower bound is exactly 1.00; the exposure age is three decades too old; `howard2024` reduces
the comparable estimate to a non-significant RR 1.12 (0.95-1.29) once follow-up exceeds 10 years; the
AD-specific version of this contrast is RR 1.02 (0.76-1.36); and MR gives no causal support. Multiplying
that hazard ratio by an adolescent's remaining lifetime dementia risk would produce a number with no
evidentiary content.

**The honest asymmetry, stated for the record.** The absence of a defensible number does not license
"short sleep is safe for the brain". It licenses only "this channel cannot be quantified". Three things
remain true and belong in the report: short sleep in this literature is at worst weakly and at best not
at all associated with dementia; the *cognitive* and *academic* consequences of the subject's sleep
pattern are a separate matter with far better evidence and belong to other shards; and the Lancet
Commission's own guidance — sleep loss is not a demonstrated dementia risk factor, *and* people should
not cut their sleep — is the correct pair of statements to carry forward.

---

## Files

38 records: `xie2013` `miao2024` `kang2009` `shokrikojori2018` `ooms2014` `lucey2018` `blattner2020`
`ju2017` `olsson2018` `forsberg2025` `skorucak2021` `sabia2021` `bubu2017` `fan2019` `xu2020` `wu2018`
`liang2019` `howard2024` `vanwanrooij2025` `you2024` `xiong2024` `yuan2022` `tao2026` `sun2026`
`anderson2021` `huang2020` `henry2019` `guo2024` `xiang2024` `spira2013` `spira2018` `winer2020`
`winer2021` `lucey2019` `tortcolet2026` `deckers2024` `livingston2024` `komlo2026`.

Reproducibility: `verify.py` → `verification_raw.json`, `verify_out.txt` (40/40 VERIFIED);
`validate.py` (38/38 schema-valid, 0 warnings); `audit_quotes.py` (104/104 quotes traced to retrieved
text); retrieval helpers `pm.py`, `getfull.sh`, `h2t.py`.
