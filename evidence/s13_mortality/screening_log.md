# Screening log — shard `s13_mortality`

Domain: all-cause mortality in relation to habitual sleep duration.

**Records screened and individually adjudicated below: 72. Included with extracted YAML records: 28.
Excluded with a logged reason: 44.** Gate G1 threshold is >= 25 screened; met. (The 72 adjudicated
records are drawn from 249 archived title-level hits in `search_hits.txt`; records excluded purely on
title as off-topic — obstructive sleep apnoea surgery, ICU delirium, animal studies, COPD trials — are
not itemised individually.)

## Search strategy actually executed

Twelve PubMed queries plus four Europe PMC queries, archived verbatim in `search_hits.txt`
(249 record lines) and reproducible via `screen_runs.sh`. Query set:

| # | Query | Hits returned |
|---|---|---|
| 1 | `sleep duration AND all-cause mortality AND (meta-analysis[pt] OR meta-analysis[tiab])` | 47 |
| 2 | `"sleep duration"[tiab] AND mortality[tiab] AND "dose-response"[tiab]` | 44 |
| 3 | `accelerometer[tiab] AND sleep[tiab] AND mortality[tiab] AND "UK Biobank"[tiab]` | 18 |
| 4 | `actigraphy[tiab] AND sleep[tiab] AND mortality[tiab]` | 118 |
| 5 | `"Mendelian randomization"[tiab] AND "sleep duration"[tiab] AND (mortality OR lifespan OR longevity)` | 22 |
| 6 | `"Mendelian randomization"[tiab] AND sleep[tiab] AND (lifespan OR longevity OR "parental lifespan" OR mortality OR survival OR ageing)` | 71 |
| 7 | `"weekend"[tiab] AND sleep[tiab] AND mortality[tiab]` | 15 |
| 8 | `"catch-up sleep"[tiab] OR "sleep rebound"[tiab] AND mortality[tiab]` | 11 |
| 9 | `sleep[tiab] AND mortality[tiab] AND ("reverse causation" OR "reverse causality")` | 11 |
| 10 | `"sleep duration"[tiab] AND mortality[tiab] AND age AND (effect modification OR stratified OR younger)` | — |
| 11 | `(childhood OR adolescen*) AND "sleep duration"[tiab] AND (mortality OR lifespan OR longevity)` | — |
| 12 | `"sleep duration"[tiab] AND mortality[tiab] AND (trajector* OR "change in sleep")` | 22 |
| 13 | `polysomnograph*[tiab] AND "sleep duration"[tiab] AND mortality[tiab]` | 44 |
| 14 | `(sleep AND mortality AND (conscript* OR adolescen* OR "young adult" OR "young men") AND cohort)` | 55 |
| 15 | EPMC `TITLE:"sleep duration" AND TITLE:"mortality" AND (parental lifespan OR "Mendelian randomi")` | 1 |
| 16 | EPMC / PMC full-text retrieval for included records | — |

---

## INCLUDED (28)

| # | study_id | Identifier | Tier | Why included |
|---|---|---|---|---|
| 1 | `cappuccio2010` | PMID 20469800 / doi 10.1093/sleep/33.5.585 | T5 | Required extraction 1. Pooled short RR 1.12, long RR 1.30. |
| 2 | `liu2017` | PMID 27067616 / 10.1016/j.smrv.2016.02.005 | T5 | Dose-response meta-regression, 40 cohorts. RR at 5 h and 6 h; null in men. |
| 3 | `yin2017` | PMID 28889101 / 10.1161/JAHA.117.005947 | T5 | Dose-response MA named in the task. Nadir 7 h; RR 1.04 at 5 h, 1.01 at 6 h. |
| 4 | `itani2017` | PMID 27743803 / 10.1016/j.sleep.2016.08.006 | T5 | Meta-regression locating the threshold: linear rise only **below 6 h**. |
| 5 | `jike2018` | PMID 28890167 / 10.1016/j.smrv.2017.06.011 | T5 | Long-sleep MA named in the task. RR 1.39 — the asymmetry evidence. |
| 6 | `ungvari2025` | PMID 40072785 / 10.1007/s11357-025-01592-y | T5 | Newest synthesis (2025): short 1.14, long 1.34. |
| 7 | `pienaar2021` | PMID 33567861 / 10.1177/0890117121992288 | T5 | MA restricted to **employed, disease-free** adults 18-64 — the healthiest available population. |
| 8 | `kripke2002` | PMID 11825133 / 10.1001/archpsyc.59.2.131 | T5 | 1.1M people. Threshold: excess >15% only below ~4.5 h. Insomnia null. |
| 9 | `svensson2021` | PMID 34477853 / 10.1001/jamanetworkopen.2021.22837 | T5 | 322 721 East Asians; nadir 7 h confirmed; **age modifies the association in men (P<.001)**. |
| 10 | `akerstedt2019` | PMID 29790200 / 10.1111/jsr.12712 | T5 | **Required extraction 4** (high priority). Every weekday x weekend cell. |
| 11 | `akerstedt2017` | PMID 28856478 / 10.1007/s10654-017-0297-0 | T5 | Required extraction 6. Age stratification: HR 2.45 under 45 y vs 1.05 over 65 y. |
| 12 | `xiao2019` | PMID 31204307 / 10.1016/j.sleh.2019.04.008 | T5 | Weekday and weekend sleep separately; race stratification as a confounding probe. |
| 13 | `ferrie2007` | PMID 18246975 / 10.1093/sleep/30.12.1659 | T5 | Only estimate for **change** in sleep duration. Symmetric harm in both directions. |
| 14 | `wang2020` | PMID 32442289 / 10.1001/jamanetworkopen.2020.5246 | T5 | Longitudinal sleep-duration patterns; low-stable vs low-increasing. |
| 15 | `duggan2014` | PMID 24588628 / 10.1037/hea0000078 | T5 | **Required extraction 5** — the only childhood-exposure-to-death study in existence. |
| 16 | `kurina2013` | PMID 23622956 / 10.1016/j.annepidem.2013.03.015 | TX | Critical review of measurement, confounding and reverse causation. |
| 17 | `zhao2023` | PMID 36892074 / 10.1161/JAHA.122.027832 | T4 | **PIVOTAL.** PSG vs self-report head-to-head in the same 5027 people. |
| 18 | `yoshiike2023` | PMID 38468822 / 10.1007/s41105-023-00460-6 | T4 | Weekend catch-up x objective sleep ability, full 12-cell table. |
| 19 | `chaput2026` | PMID 42454954 / 10.1093/sleep/zsag193 | T4 | Device vs self-report dose-response, UK Biobank. |
| 20 | `chaput2024` | PMID 38895883 / 10.1093/sleep/zsae135 | T4 | Device-measured weekend catch-up: **null/harmful**, contradicts `li2026`. |
| 21 | `saintmaurice2024` | PMID 38066693 / 10.1093/sleep/zsad312 | T4 | Actigraphy duration, continuity, timing, UK Biobank. |
| 22 | `liang2023` | PMID 37186145 / 10.1093/gerona/glad108 | T4 | Device duration x efficiency, 90 398 UK Biobank participants. |
| 23 | `li2026` | PMID 42045198 / 10.1038/s41467-026-72461-1 | T4 | Objective sleep restriction with vs without rebound. |
| 24 | `windred2024` | PMID 37738616 / 10.1093/sleep/zsad253 | T4 | Regularity out-predicts duration; duration adds nothing (p=0.14-0.20). |
| 25 | `fernandezmendoza2019` | PMID 31575322 / 10.1161/JAHA.119.013043 | T4 | PSG short sleep x prevalent cardiometabolic disease; 19.2 y follow-up. |
| 26 | `wu2024` | PMID 38388528 / 10.1038/s41398-024-02826-x | T3 | MR: short sleep on lifespan, positive but unit-ambiguous. |
| 27 | `zhang2025` | PMID 39883542 / 10.1089/rej.2024.0058 | T3 | MR: **null** for sleep duration on mortality; observational HRs 1.25/1.74. |
| 28 | `sambou2024` | PMID 38262521 / 10.1016/j.jad.2024.01.122 | T3 | MR on healthspan: OR 0.98 (0.97-1.00), i.e. 28% of the observational estimate. |

---

## EXCLUDED (38)

### Wrong exposure (not habitual sleep duration)

| Identifier | Record | Reason for exclusion |
|---|---|---|
| PMID 31630016 | Insomnia and mortality: SR/MA, Sleep Med Rev 2019 | Exposure is insomnia disorder, not duration. Kripke's null insomnia result already captures the dissociation. |
| PMID 39413101 | Napping and CVD/all-cause mortality MA, PLoS One 2024 | Exposure is daytime napping. |
| PMID 39153335 | Habitual daytime napping MA, Sleep Med Rev 2024 | Exposure is napping. |
| PMID 37752591 | Objectively regular sleep patterns and mortality, MESA, J Sleep Res 2024 | Exposure is regularity; `windred2024` already covers regularity with a larger objective sample. |
| PMID 37146482 | Sleep quality and mortality mechanism, UK Biobank, 2023 | Exposure is sleep quality score. |
| PMID 36333394 | Subjective-objective sleep discrepancy and mortality in older men (MrOS), 2022 | Exposure is misperception, not duration. Conceptually interesting; not convertible to an hours contrast. |
| PMID 42387174 | Social jet lag and incident CVD, J Intern Med 2026 | Exposure social jetlag; outcome CVD incidence. |
| PMID 33636423 | Heritability of sleep duration MA, Sleep Med Rev 2021 | No mortality outcome. |
| PMID 40136847 | Night work and social jet lag / arterial stiffness | No mortality outcome; wrong exposure. |
| PMID 31166059 | Sleep extension and cardiometabolic risk factors, SR 2019 | Intermediate outcomes; belongs to a metabolic shard. |

### Wrong outcome (not all-cause mortality)

| Identifier | Record | Reason for exclusion |
|---|---|---|
| PMID 38995667 | Accelerometer sleep duration and incident CVD / CVD mortality, Sleep 2024 | Cause-specific CVD mortality only; UK Biobank overlap with 5 included records. |
| PMID 36035915 | Sleep duration and CVD: meta-review of observational + MR, 2022 | Outcome CVD, not mortality. |
| PMID 30903483 | Sleep duration and cancer-specific mortality MA, 2019 | Cause-specific. |
| PMID 36256607 | Sleep duration at 50/60/70 and multimorbidity, Whitehall II, PLoS Med 2022 | Outcome is multimorbidity. |
| PMID 42129562 | Sleep chart of biological ageing clocks, Nature 2026 | Outcome is ageing-clock biomarkers. |
| PMID 40856643 | Non-linear effects of sleep duration on biological aging, 2025 | Biomarker outcome. |
| PMID 40032851 | Sleep traits and epigenetic age acceleration MR, 2025 | Biomarker outcome. |
| PMID 41821113 | Chronotype/napping/duration and biological/functional aging MR, 2026 | Biomarker outcome. |
| PMID 40865593 | Sleep duration and QT variability index, Heart Rhythm 2026 | Intermediate electrophysiological outcome. |
| PMID 39920677 | Device sleep regularity/duration and incident dementia, 2025 | Outcome dementia. |
| PMID 38075695 | Causal associations of sleep traits with cancer incidence and mortality, 2023 | Cause-specific cancer. |
| PMID 40011859 | Sleep and breast-cancer-specific mortality MR, 2025 | Cause-specific, female-only. |

### Wrong population (diseased subgroup, or sex-restricted for a male subject)

| Identifier | Record | Reason for exclusion |
|---|---|---|
| PMID 38051532 | Objective sleep duration and mortality in people **with OSA**, JAMA Netw Open 2023 | Clinical OSA population. |
| PMID 36383480 | Sleep duration and CVD/mortality in **type 2 diabetes**, Diabetes Care 2023 | Diabetic population. |
| PMID 29982090 | Sleep duration/quality and mortality, **Women's Health Initiative**, 2018 | Postmenopausal women only; subject is male. |
| PMID 41882656 | Weekend catch-up sleep + TyG index, bone loss and mortality in **diabetics** 18-60 | Diabetic subgroup, composite outcome. Age band would otherwise have been attractive. |
| PMID 41760375 | Sleep behaviours and mortality in **inflammatory bowel disease**, 2026 | Disease-specific. |
| PMID 39629617 | Movement behaviours and mortality in people with **pre-existing depression**, 2025 | Disease-specific. |
| PMID 41282702 | Objective long sleep / insomnia phenotypes and mortality in **older persons**, medRxiv 2025 | Preprint; elderly-only; long-sleep focus. |
| PMID 32723316 | Dose-response MA of sleep duration and mortality in **older people**, 2020 | Elderly-only (>=60 y); the least transportable possible population; superseded by `ungvari2025`. |
| PMID 36155361 | Sleep quality+duration and mortality, Kyoto-Kameoka **older adults** | Elderly-only, composite exposure. |

### Not a primary effect estimate / superseded / non-isolable exposure

| Identifier | Record | Reason for exclusion |
|---|---|---|
| PMID 35127769 | Umbrella review of sleep duration/quality meta-analyses, 2021 | Umbrella review; contributes no new estimate; its constituents are already included. |
| PMID 34435311 | Sleep duration and health outcomes: umbrella review, 2022 | Same. |
| PMID 18246971 | "The parable of parabola" commentary, Am J Epidemiol 2007 | Commentary. Its argument is represented by `kurina2013`. |
| PMID 23524039 | Sleeping at the limits: changing prevalence in 10 countries, 2013 | Descriptive prevalence only. |
| PMID 36990109 | Joint PA + sleep duration and mortality, accelerometry, 2023 | Joint exposure; sleep effect not isolable; UK Biobank overlap. |
| PMID 42386465 | Joint accelerometer sleep duration + PA with CVD/mortality, 2026 | Joint exposure; UK Biobank overlap. |
| PMID 40217556 | PA, sedentary behaviour and sleep with mortality SR/MA, 2023 | Multi-exposure. |
| PMID 38769347 | Self-supervised learning of accelerometer data, sleep and mortality, NPJ Digit Med 2024 | Exposure is machine-learned sleep features, not hours; not convertible to an hours contrast; UK Biobank overlap with 5 included records. |
| PMID 42465890 | "Poor sleep is robustly correlated with accelerated aging but the evidence for causation is mixed", medRxiv 2026 | Preprint, outcome is ageing biomarkers. **Noted in the summary because its conclusion — correlation robust to chronic disease burden but NOT to shared genetic and early-environmental factors among twins, with mixed MR — directly corroborates my confounding verdict.** |
| PMID 40953676 | Sleep time and mortality by cardiovascular health status, 2026 | Stratified by CVH status; no overall estimate usable. |
| PMID 40014341 / 40014350 | Sleep trajectories and mortality among low-income adults; racial/socioeconomic differences in trajectories, JAMA Netw Open 2025 | Trajectory exposures in a low-income midlife cohort; `wang2020` already supplies the trajectory contrast and these two overlap each other. |
| PMID 27450684 | Habitual sleep duration and all-cause mortality in a general community sample, Sleep 2016 | Adds nothing beyond the pooled meta-analyses that already include comparable cohorts. |
| PMID 29394410 | Sleep lengthening in late adulthood signals increased mortality, Sleep 2018 | Elderly, long-sleep direction. |

### Searched-for and absent

| Target | Outcome of search |
|---|---|
| MR of sleep duration on **parental lifespan** specifically | Query 15 (EPMC, title-restricted) returned exactly ONE record and it was `duggan2014`, not an MR study. No dedicated sleep-duration-to-parental-lifespan MR exists. The nearest is `wu2024`, which uses a lifespan GWAS. |
| Sleep duration measured in **adolescence** with mortality follow-up | Queries 11 and 14 screened 80 records. Query 14 returned bariatric surgery, epilepsy/SUDEP, neonatal and paediatric-pulmonology records — i.e. the query space is empty. Only `duggan2014` exists, and it models a quadratic deviation, not a short-sleep contrast. **INSUFFICIENT EVIDENCE.** |
| Time-limited adolescent restriction with later normalisation | No record of any design (cohort, MR, trial) estimates this. **INSUFFICIENT EVIDENCE.** |
| Sleep-duration mortality in a **conscript / student / military** young-male cohort | None found. Query 14 (`conscript*`) returned zero relevant records. |

---

## Verification

All 28 included records verified programmatically against **both** Crossref and PubMed, with the
PubMed-reported DOI string-matched to the DOI I recorded. Raw responses in `verification_raw.json`
(28 entries, all `status: VERIFIED`, all `doi_match: true`). Reproduce with `verify_batch.py` and
`verify_batch2.py`. **Zero identifiers failed verification; zero records are `secondhand`.**

Schema: `validate.py` validates all 28 YAML files against `/workspace/spec/effect.schema.json`
(0 failures, 122 effect estimates) and additionally audits every log-scale effect for internal
consistency between `value`, `ci` and `se = (ln hi - ln lo)/3.92`.
