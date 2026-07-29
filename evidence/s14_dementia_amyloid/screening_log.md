# Screening log — shard `s14_dementia_amyloid`

Domain: the glymphatic / amyloid-clearance mechanism, and the epidemiology of sleep duration and
incident dementia.

**Totals: 77 individually identified records screened — 38 included (104 extracted effects) and 39
excluded — plus 2 categories of non-primary source excluded en bloc (rows 40-41 below), for 41 exclusion
entries in all. 40/40 (PMID, DOI) pairs verified against both Crossref and PubMed: the 38 included records
plus two identifiers deliberately checked without extraction — the `howard2024` corrigendum and the
Park 2025 protocol (exclusion row 39) (`verify.py` → `verification_raw.json`, `verify_out.txt`).
104/104 quotes machine-audited back to retrieved text (`audit_quotes.py`).
38/38 YAML records validate against `effect.schema.json` (`validate.py`).**

Search strategy: PubMed `esearch` via `pm.py` across the mechanistic literature (glymphatic clearance,
CSF Aβ kinetics, slow-wave disruption), the epidemiological literature (sleep duration and incident
dementia, dose-response and follow-up-stratified meta-analyses), bidirectional Mendelian randomization,
longitudinal amyloid/tau biomarker cohorts, and — exhaustively, because it is the shard's critical
question — adolescent and early-life sleep exposure with long-run neurodegenerative outcomes. Full texts
retrieved from PMC where available (`getfull.sh`), plus one open-access accepted manuscript from a
repository (`livingston2024`, via Unpaywall → UCL Discovery) because the publisher version is paywalled.

---

## Included (38)

| # | study_id | PMID | Tier | Design | n | Adolescent match | Why included |
|---|---|---|---|---|---|---|---|
| 1 | `xie2013` | 24136970 | TX | mouse, within-subject | 77 | mixed | The glymphatic paper. Species = MOUSE, exposure = acute sleep/anaesthesia, measure = exogenous tracer clearance. Task-required. |
| 2 | `miao2024` | 38741022 | TX | mouse, within-subject | 13 | mixed | Direct contradiction of `xie2013`: clearance *reduced* during sleep. Required to characterise mechanistic uncertainty. |
| 3 | `kang2009` | 19779148 | TX | mouse + human | 8 | mixed | Origin of the sleep–Aβ dynamics claim (orexin, ISF Aβ diurnal oscillation). |
| 4 | `shokrikojori2018` | 29632177 | T1 | human PET, within-subject | 20 | fair_adult | Task-required. % Aβ increase after one night of total deprivation, by region, with n. |
| 5 | `ooms2014` | 24887018 | T1 | RCT parallel | 26 | poor_midlife | Task-required. CSF Aβ42 after one night of total deprivation. |
| 6 | `lucey2018` | 29220873 | T1 | within-subject SILK | 8 | fair_adult | Decisive mechanistic re-framing: the acute rise is *increased production*, not impaired clearance. |
| 7 | `blattner2020` | 32250301 | T1 | RCT parallel | 11 | poor_midlife | Third replication (+9.1% Aβ40, +8.6% Aβ42) and rules out cortisol/circadian mediation. 36-h mesor unchanged. |
| 8 | `ju2017` | 28899014 | T1 | RCT crossover | 17 | poor_midlife | Selective slow-wave disruption → CSF Aβ; isolates the *stage* the mechanism requires. |
| 9 | `olsson2018` | 29425372 | T1 | RCT crossover | 13 | good_young_adult | 5–8 nights of 4-h *restriction* (not deprivation) → no CSF biomarker change. Closest lab analogue to the subject's exposure. |
| 10 | `forsberg2025` | 40830882 | T1 | RCT crossover | 12 | good_young_adult | Crossover replication with washout; the design bears on reversibility. |
| 11 | `skorucak2021` | 33893807 | T1 | lab restriction | 34 | **exact_16_19** | The ONLY record in the shard with an adolescent population. Slow-wave homeostasis preserved under 5 nights × 5 h. |
| 12 | `sabia2021` | 33879784 | T5 | prospective cohort | 7959 | poor_midlife | Task-required. Whitehall II HRs at ages 50/60/70, cases, follow-up, accelerometer sub-study. |
| 13 | `bubu2017` | 28364458 | T5 | meta-analysis | 69216 | poor_elderly | Task-required (named seed). |
| 14 | `fan2019` | 31604673 | T5 | meta-analysis | — | poor_elderly | Task-required (named seed). Short sleep null for dementia and AD; long sleep significant. |
| 15 | `xu2020` | 31879285 | T5 | dose-response MA | 53014 | poor_midlife | Largest dose-response synthesis; nadir at 5.6–6 h; AD short-sleep estimate exactly null. |
| 16 | `wu2018` | 28589251 | T5 | dose-response MA | 22187 | poor_elderly | U-shape, lowest risk 7–8 h. |
| 17 | `liang2019` | 30039452 | T5 | dose-response MA | 62937 | poor_elderly | Per-hour RRs; non-linear, peak ~7 h. |
| 18 | `howard2024` | 39442346 | T5 | meta-analysis | — | poor_elderly | Follow-up-stratified: the key reverse-causation test. |
| 19 | `vanwanrooij2025` | 39863328 | T5 | prospective cohort | 2218 | poor_elderly | Lag-time analysis reaching the OPPOSITE conclusion to `howard2024`. Retained to represent the disagreement. |
| 20 | `you2024` | 38678085 | T5 | prospective cohort | 7620 | poor_midlife | Dates each prodromal signal: sleep duration appears ONLY at 3–5 y pre-diagnosis while grip strength appears at 15 y. |
| 21 | `xiong2024` | 38301285 | T5 | prospective cohort | 7223 | poor_elderly | Short-sleep association *reverses sign* across age strata; within-paper MR null. |
| 22 | `yuan2022` | 35918656 | T5 | prospective cohort | 483507 | poor_midlife | No gene×sleep interaction (p=0.45); within-paper MR null; genotype scale anchor (HR 1.93). |
| 23 | `tao2026` | 42498182 | T5 | prospective cohort | 9030 | poor_midlife | Within-study cross-sectional (OR 2.99) vs longitudinal (HR 1.55) — quantifies design-induced inflation. |
| 24 | `sun2026` | 41854616 | T4 | prospective, PSG, IPD MA | 7105 | poor_elderly | Positive control: objective sleep EEG *does* predict dementia (HR 1.39/decade of brain-age index). |
| 25 | `anderson2021` | 33150399 | T3 | Mendelian randomization | 54162 | mixed | Task-required. Little evidence sleep traits → AD; napping protective. |
| 26 | `huang2020` | 32817390 | T3 | Mendelian randomization | 446118 | mixed | Task-required REVERSE direction: AD genetic liability → shorter sleep. |
| 27 | `henry2019` | 31062029 | T3 | Mendelian randomization | 395803 | poor_midlife | No association of instrumented sleep duration with AD or all-cause dementia. |
| 28 | `guo2024` | 38350061 | T3 | Mendelian randomization | 502383 | poor_midlife | Observational association attenuates on vascular adjustment and vanishes in MR. |
| 29 | `xiang2024` | 38865787 | T3 | Mendelian randomization | — | poor_midlife | The only nominally positive sleep-duration MR — and it points at LONG sleep, OR 1.002. |
| 30 | `spira2013` | 24145859 | TX | cross-sectional | 70 | poor_elderly | Task-required (named seed). Original human sleep–amyloid imaging finding. |
| 31 | `spira2018` | 30192978 | T5 | prospective cohort | 124 | poor_midlife | Longest lag in the biomarker literature: EDS at mean age 60 → Aβ positivity 15.7 y later. |
| 32 | `winer2020` | 32888482 | T4 | prospective, PSG | 32 | poor_elderly | Task-required (named seed). Only sleep-forecasts-amyloid-*accumulation* study; duration did NOT forecast. |
| 33 | `winer2021` | 34459862 | TX | cross-sectional | 4417 | poor_elderly | Short sleep ↔ higher Aβ; long sleep shows NO amyloid signal despite stronger epidemiology. |
| 34 | `lucey2019` | 30626715 | TX | cross-sectional | 119 | poor_elderly | Task-required (named seed). NREM SWA tracks TAU, not amyloid; gross sleep parameters null. |
| 35 | `tortcolet2026` | 41998740 | T5 | prospective, serial PET | 417 | poor_elderly | Largest prospective sleep→amyloid-accumulation study; main effect NULL; amyloid-negative stratum null. |
| 36 | `deckers2024` | 38159267 | TX | umbrella review + Delphi | — | mixed | Replication rate of the literature: short sleep positive in 5/16 reviews (31%). |
| 37 | `livingston2024` | 39096926 | TX | commission consensus | — | mixed | 2024 Lancet Commission explicitly places sleep in the *insufficient evidence* bin. |
| 38 | `komlo2026` | 41959309 | TX | mouse preprint | — | mixed | The only record framed on early-life chronic short sleep and long-run cognition. Mouse, preprint, no numbers. |

`howard2024_corr` (PMID 40022863, corrigendum to `howard2024`) was verified and is discussed inside
`howard2024.yaml`; it gets no separate record because an erratum contributes no independent effect.

---

## Excluded (40)

| # | Identifier | Decision | Reason |
|---|---|---|---|
| 1 | PMID 41614054 (`park2025`) | exclude | **Study protocol, not results.** Whitehall II midlife short sleep × obesity → dementia. Written entirely in future tense ("Participants will be divided…", "We will use linear mixed-effects models"). Identifier verified and retained in `verify.py` so the pipeline can pick it up on publication; it is the single most relevant *forthcoming* study for this shard. |
| 2 | PMID 42454954 | exclude | Dose-response sleep duration vs **general health outcomes**, self-report vs device-measured; dementia not a primary outcome. |
| 3 | PMID 42420680 | exclude | Exposure is sleep × **work-related stress interaction**, not sleep duration; cannot yield a marginal duration effect. |
| 4 | PMID 42370981 | exclude | Exposure is a composite modifiable-lifestyle index stratified by **KDIGO renal risk**; sleep not separable. |
| 5 | PMID 42342736 | exclude | Exposure is **melatonin / benzodiazepine / zolpidem prescription**, not sleep duration. |
| 6 | PMID 42334823 | exclude | Exposure is **sedative-hypnotic drug use**. Confounding by indication; not the shard's exposure. |
| 7 | PMID 42277229 | exclude | Plasma **proteomics** of sleep traits; no dementia outcome. |
| 8 | PMID 42018962 | exclude | Special population (**focal epilepsy**); not transportable. |
| 9 | PMID 41950182 | exclude | Systematic review of the **24-h activity composite** (physical activity + sedentary + sleep); sleep duration not separable, and superseded for this question by `xu2020` / `howard2024`. |
| 10 | PMID 41922940 | exclude | Sleep-EEG **cyclic alternating pattern** as dementia predictor; same marker class as `sun2026`, which is larger and IPD-pooled. |
| 11 | PMID 41867174 | exclude | Gene × sleep duration interaction for **glycemic traits**; wrong outcome domain (belongs to a metabolic shard). |
| 12 | PMID 41837677 | exclude | Exposure is **multidimensional sleep health composite**; duration not separable. |
| 13 | PMID 41796014 | exclude | Methodological/descriptive report on the UK Biobank sleep questionnaire; no outcome. |
| 14 | PMID 41720429 | exclude | Exposure is comorbid **OSA + anxiety/depression**. |
| 15 | PMID 41699535 | exclude | **Long** sleep only (CLHLS); adds nothing beyond `xu2020`, `fan2019`, `yuan2022`, `xiong2024` on the long-sleep tail. |
| 16 | PMID 41637960 | exclude | Primary exposure is **serum 25-hydroxyvitamin D**. |
| 17 | PMID 41588822 | exclude | **OSA** mechanisms; not sleep duration. |
| 18 | PMID 41478835 | exclude | Broad modifiable/non-modifiable risk-factor panel vs WMH/amyloid; sleep not isolable. |
| 19 | PMID 41445661 | exclude | **medRxiv preprint**, superseded in scope by `sun2026` and `tortcolet2026`. |
| 20 | PMID 41444571 | exclude | Composite of physical activity, muscle strength, sedentary behaviour and sleep. |
| 21 | PMID 42078877 | exclude | CSF clearance in **aging autistic adults** (Research Square preprint); special population, not peer-reviewed. |
| 22 | PMID 41728498 | exclude | Exposure is **anxiety/depression**, not sleep. |
| 23 | PMID 39046104 | exclude | GWAS meta-analysis of dementia; **no sleep exposure** (a source GWAS, not an effect estimate). |
| 24 | PMID 27397561 | exclude | Outcome is **white-matter microstructure**, not dementia or amyloid — belongs to a brain-structure shard. |
| 25 | PMID 12535460 | exclude | Cochrane review, **CBT for sleep problems in adults 60+**; intervention review, no dementia outcome. |
| 26 | PMID 12519595 | exclude | Cochrane review, exercise for sleep problems 60+; as above. |
| 27 | PMID 12076478 | exclude | Cochrane review, bright light therapy for sleep problems 60+; as above. |
| 28 | PMID 12076472 | exclude | Cochrane review, duplicate record of #25. |
| 29 | PMID 39832661 | exclude | **Mouse**; exposure is sleep *fragmentation* in a transgenic AD model, not duration in wild-type. |
| 30 | PMID 37946213 | exclude | **Mouse**; hexosamine/O-GlcNAc mechanism, no dementia-risk quantity. |
| 31 | PMID 32087293 | exclude | Narrative review of animal models; no primary effect estimates. |
| 32 | PMID 42055498 | exclude | **OSA** vs A/T/N biomarkers. |
| 33 | PMID 41668114 | exclude | Mild behavioural impairment network phenotypes; no sleep exposure. |
| 34 | PMID 40929630 | exclude | Exposure is **chronic insomnia** (a disorder with hyperarousal physiology), not voluntary short sleep. Distinct phenotype; see `tao2026` notes. |
| 35 | PMID 40170406 | exclude | Outcome is **subjective** cognitive decline. |
| 36 | PMID 38669550 | exclude | Data-derived cognition/amyloid phenotypes in veterans; no sleep exposure. |
| 37 | PMID 37889891 | exclude | **Cohort protocol** (Healthy Brain Initiative). |
| 38 | PMID 31944479 | exclude | Amyloid-related hippocampal atrophy; no sleep exposure. |
| 39 | PMID 41614054 | exclude | Park 2025, "Midlife short sleep with and without obesity, and the risk of future dementia" (Whitehall II, Wellcome Open Res). Exactly on-topic, and its identifier **is** verified in `verification_raw.json` — but it is a **protocol, not results** ("Participants *will be* divided into four groups… *We will use* linear mixed-effects models"). No effect estimate exists to extract. See flag #4 below. |
| 40 | — | exclude | Popular-press and review syntheses asserting "sleep loss causes Alzheimer's" (encountered while tracing claims). Excluded as non-primary; the *chain* they assert is instead audited link-by-link in `dementia_summary.md`. |
| 41 | — | exclude | Secondary citations of `xie2013` in mouse glymphatic reviews. Excluded to avoid double-counting a single mouse experiment as multiple records. |

---

## Screening decisions worth flagging to the orchestrator

1. **The adolescent-exposure search returned nothing usable.** The query `adolescent sleep dementia risk
   later life` returned 8 records, of which none had adolescent sleep as exposure and dementia as outcome
   (they were: CSF clearance in autistic adults, an anxiety/depression review, a dementia GWAS, a
   white-matter study in middle-aged adults, and four Cochrane reviews of sleep interventions in adults
   60+). This is a genuine, complete absence rather than a retrieval failure — see `station_report.md`.

2. **The reversibility search returned three records, all rodent.** `recovery sleep amyloid beta reversal`
   returned exactly 3 hits (two mouse experiments, one animal-model review). No human study measures Aβ
   before deprivation, after deprivation, *and* after recovery sleep. The reversibility inference in this
   shard is assembled from four indirect lines and is labelled as such.

3. **Exposure-construct discipline was the main exclusion criterion.** 14 of the 41 exclusion entries
   (#3, #4, #5, #6, #9, #12, #14, #16, #17, #18, #20, #29, #32, #34) were excluded because the exposure was
   obstructive sleep apnoea, insomnia, hypnotic drugs, fragmentation, or a multi-behaviour composite rather
   than sleep *duration*. This matters because the sleep constructs with the strongest dementia evidence
   (OSA, insomnia, daytime sleepiness) are precisely *not* the construct that applies to a healthy
   19-year-old who is voluntarily curtailing sleep and sleeps normally when allowed to.

4. **The most on-topic record I found is a protocol whose results do not yet exist** (exclusion row 39;
   PMID 41614054, verified). Park, Frank, Ren, Livingston and Kivimäki registered a Whitehall II analysis
   of *midlife* short sleep (≤6 h, measured 1997-99) against dementia to 2023, with blood-biomarker
   mediation. Two of its authors wrote the Lancet Commission (`livingston2024`) and the Whitehall II
   dementia paper (`sabia2021`). It states the premise in its own words: "Short sleep duraiton is a
   putative risk for dementia, whereas midlife obesity is an well-known risk factor" *(sic, verbatim
   including the two typos)*. I record this as a screening observation, not as evidence: it carries no
   effect estimate. Its value is as a check on my own reading — the investigators closest to this cohort
   still write "putative" for sleep and "well-known" for obesity in 2025, which is the same asymmetry the
   Lancet Commission encoded by excluding sleep from its modifiable-risk list. It also means the single
   best future test of this shard's central question is already running, and this shard's verdict should
   be revisited when it reports.
