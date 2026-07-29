# Screening log — shard `s17_baseline_risk`

**Domain:** absolute baseline risks for a US male, plus the life-table machinery for converting
hazard ratios into life-expectancy changes.

**Search corpus.** 36 PubMed E-utilities queries plus targeted retrieval of official statistical
products from CDC/NCHS, SSA, SAMHSA/NSDUH, NIMH and RAND. Those queries surfaced **141 distinct
PubMed records**; 24 abstracts were pulled in full for assessment, alongside 11 non-PubMed
official sources. **29 records included.** Every included record was verified through Crossref
and/or PubMed before being written (see `verification` in each YAML file); 27 of 29 resolve with
title similarity 1.00 against the recorded citation, and the 2 that do not are government
statistical products with no DOI or PMID, flagged `UNVERIFIED` in-record.

Search caches, retrieved PDFs and the extracted text used for every quote are in `/tmp/s17/`.
The exact query strings are listed in section 5.

---

## 1. Included — life table and mortality machinery

| # | identifier | source | decision | reason |
|---|---|---|---|---|
| 1 | doi:10.15620/cdc/174591 | Arias E, Xu JQ, Kochanek K. United States Life Tables, 2023. NVSR 74(6), 2025 | **INCLUDE** | Most recent published NCHS life table. Table 2 (males) downloaded as the official `Table02.xlsx`, giving `qx`, `lx`, `dx`, `Lx`, `Tx`, `ex` at full precision for ages 0–100. Primary `qx` source for ages 19–99. Published `e0` = 75.8178, `e19` = 57.6565. |
| 2 | ssa.gov/oact/STATS/table4c6.html | SSA Office of the Chief Actuary, Period Life Table 2023 (2026 Trustees Report) | **INCLUDE**, marked `UNVERIFIED` | The **only** way to satisfy the brief's "qx to age 110": NCHS closes at an open-ended "100 and older" interval, so single-year `qx` above 99 is not published by NCHS. SSA publishes male `qx` to 119. No DOI or PMID exists for an SSA actuarial table, so verification status is honest rather than fabricated. Also serves as an independent check on ages 19–99: max relative `qx` disagreement with NCHS is 6.78% (at age 19, where `qx` is ~0.001 so the absolute gap is negligible), and max absolute disagreement is 1.05×10⁻² (at age 97). |
| 3 | PMID 10844714 | Beiser A, D'Agostino RB, Seshadri S, et al. Computing estimates of incidence, including lifetime risk. *Stat Med* 2000 | **INCLUDE as method citation** | The reference implementation (PIE macro) for lifetime risk with competing mortality. Cited in `competing_risk_method.md` §2; contributes no numeric estimate, so no YAML record. |
| 4 | doi:10.4054/DemRes.2008.19.35 | Beltrán-Sánchez H, Preston SH, Canudas-Romo V. *Demogr Res* 2008 | **INCLUDE as method citation** | Cause-deleted and cause-modified life tables — the formal basis for the cause-fraction down-weighting in §1.4. Method only, no YAML record. |
| 5 | doi:10.2307/2061029 | Arriaga EE. Measuring and explaining the change in life expectancies. *Demography* 1984 | **INCLUDE as method citation** | Decomposition of a difference in `e(x)` by age, used to attribute the life-expectancy change to exposure windows in §1.3. Method only. |
| 6 | doi:10.1080/01621459.1999.10474144 | Fine JP, Gray RJ. *J Am Stat Assoc* 1999 | **INCLUDE as method citation** | Subdistribution hazard regression; cited in §2 to distinguish cause-specific from subdistribution hazards. Method only. |

## 2. Included — absolute baseline risks

| # | identifier | source | decision | reason |
|---|---|---|---|---|
| 7 | PMID 25128274 | Gregg EW, Zhuo X, Cheng YJ, et al. *Lancet Diabetes Endocrinol* 2014 | **INCLUDE** | The paper the brief named. Lifetime risk of diagnosed diabetes from age 20, US males, competing-risk adjusted: **40.2% (39.2–41.3)** for 2000–2011. |
| 8 | PMID 35609056 | Koyama AK, et al. *PLoS One* 2022 | **INCLUDE** | Newer US lifetime-risk estimate (32.8%, 2015–2018) using the same Markov approach. Directly contradicts the direction implied by rising prevalence; both retained. |
| 9 | PMID 14532317 | Narayan KMV, et al. Lifetime risk for diabetes mellitus in the US. *JAMA* 2003 | **INCLUDE** | Original "1 in 3" analysis. Also the only source found for QALYs lost to diabetes (18.6 QALYs, men diagnosed at 40) — usable only as a downstream multiplier. |
| 10 | PMID 17372155 | Narayan KMV, et al. Effect of BMI on lifetime risk for diabetes. *Diabetes Care* 2007 | **INCLUDE**, `abstract_only` | **Most transportable diabetes record in the shard**: indexed at exactly age 18 and stratified by BMI, the mediator short sleep actually moves (7.6% underweight → 70.3% very obese). Full text paywalled, so intermediate BMI categories recorded as `null`, not interpolated. |
| 11 | doi:10.15620/cdc/165794 | Gwira JA, Fryar CD, Gu Q, et al. NCHS Data Brief, 2024 | **INCLUDE** | Current NHANES total (diagnosed + undiagnosed) diabetes prevalence, US males 20+: 18.0% (15.7–20.4), with 20–39 / 40–59 / 60+ bands. |
| 12 | PMID 11866648 | Vasan RS, et al. Residual lifetime risk for developing hypertension. *JAMA* 2002 | **INCLUDE** | The paper the brief named. Residual lifetime risk **~90%** for 55- and 65-year-olds. |
| 13 | PMID 40085792 | Fryar CD, et al. Hypertension Prevalence. NCHS Data Brief 511, 2024 | **INCLUDE** | The "newer estimates" the brief asked for: US male prevalence 30.0% (18–39), 55.9% (40–59), 72.7% (60+). |
| 14 | PMID 10023892 | Lloyd-Jones DM, et al. Lifetime risk of developing coronary heart disease. *Lancet* 1999 | **INCLUDE** | Lifetime CHD risk at 40, men: **48.6% (45.8–51.3)**. |
| 15 | PMID 16461820 | Lloyd-Jones DM, et al. *Circulation* 2006 | **INCLUDE** | Lifetime CVD risk at 50 by risk-factor burden, men: 51.7% overall, 5.2% with all factors optimal. The risk-factor gradient is what a mediator model needs. |
| 16 | PMID 23117780 | Wilkins JT, et al. Lifetime risk and years lived free of total CVD. *JAMA* 2012 | **INCLUDE** | Total CVD lifetime risk at 45, men: **60.3% (59.3–61.2)**, plus years-lived-free — a health-expectancy quantity usable as a QALY proxy. |
| 17 | PMID 29490333 | Khan SS, et al. Association of BMI with lifetime risk of CVD. *JAMA Cardiol* 2018 | **INCLUDE** | Competing-risk-adjusted CVD hazard ratios by BMI in middle-aged men (1.21 overweight → 3.14 morbidly obese), so the sleep → BMI → CVD path can be priced on the same scale as the lifetime risks. |
| 18 | PMID 24418058 | Chêne G, et al. Gender and incidence of dementia in Framingham. *Alzheimers Dement* 2015 | **INCLUDE** | The paper the brief named. Male lifetime dementia risk from 45: **13.8% (12.2–15.3)** competing-risk adjusted versus **61.0%** unadjusted — the single best published demonstration of the bias this shard exists to prevent (4.42×). |
| 19 | PMID 9409336 | Seshadri S, et al. Lifetime risk of dementia and Alzheimer's disease. *Neurology* 1997 | **INCLUDE** | The paper the brief named. Remaining lifetime risk at 65, men: 10.9% (8.0–13.8), versus 32.8% naive cumulative incidence (3.01×). |
| 20 | PMID 39806070 | Fang M, et al. Lifetime risk of dementia. *Nat Med* 2025 | **INCLUDE** | Newest US estimate, 35% after age 55 (ARIC, active surveillance). Contradicts Chêne by 2.5×; both carried. |
| 21 | PMID 40739976 | Hudomiet P, Hurd MD, Rohwedder S. *Demography* 2025 | **INCLUDE** | Found late and decisive: the **arbitrator** for the dementia disagreement. 41.3% of those dying after 70 had dementia, and the discussion diagnoses why earlier US estimates are lower — four mechanisms, all biasing downward. Also gives duration (only 20.1% for 5+ years), which a QALY model needs. |
| 22 | PMID 39808758 | Emmerich SD, et al. Obesity Prevalence in Adults. NCHS Data Brief 508, 2024 | **INCLUDE** | Direct answer to "obese by midlife for a US male" read as period prevalence: **45.4%** at 40–59; already 34.3% at 20–39. |
| 23 | PMID 29171811 | Ward ZJ, et al. Simulation of growth trajectories of childhood obesity into adulthood. *NEJM* 2017 | **INCLUDE** | The only *incidence*-style answer: **57.3%** of today's US children projected obese at 35, plus the persistence coefficient a sleep → BMI model needs. |
| 24 | PMID 12813115 | Kessler RC, et al. Epidemiology of major depressive disorder (NCS-R). *JAMA* 2003 | **INCLUDE** | The paper the brief named. MDD lifetime prevalence 16.2% (15.1–17.3), 12-month 6.6%. |
| 25 | PMID 29450462 | Hasin DS, et al. Epidemiology of adult DSM-5 MDD. *JAMA Psychiatry* 2018 | **INCLUDE** | NESARC-III, the newer replication and the one with a clean male-specific figure: male lifetime 14.7%, versus Kessler's sex-pooled 16.2%. |
| 26 | PMID 37531964 | McGrath JJ, et al. *Lancet Psychiatry* 2023 | **INCLUDE** | WMH morbid risk to age 75 — a projected *lifetime* risk rather than a prevalence-to-date, which is the correct estimand for an 18-year-old whose risk period has barely started (male 20.1%). |
| 27 | NSDUH 2024 detailed tables 6.39B | SAMHSA, Center for Behavioral Health Statistics and Quality | **INCLUDE**, marked `UNVERIFIED` | The only source giving past-year major depressive episode for **males aged 18–25 specifically**: 12.4% (SE 0.58). No DOI or PMID for the detailed-table release. |
| 28 | doi:10.15620/cdc/160504 | Garnett MF, Curtin SC. Suicide Mortality in the US, 2002–2022. NCHS Data Brief 509 | **INCLUDE** | Male suicide rate, ages 15–24: **21.1 per 100,000** (2022), with the 2018–2022 series. |
| 29 | PMID 37367034 | Curtin SC, Garnett MF. NCHS Data Brief 471, 2023 | **INCLUDE as age-gradient supplement** | The 15–24 band straddles the subject's age. This brief splits it: 11.8 (15–19) versus 19.4 (20–24) per 100,000, both sexes — a 1.64× gradient across exactly the ages modelled. Recorded inside the suicide entry as a ratio, not as a male rate. |

## 3. Included — published sleep life-expectancy estimates (deliverable 4 cross-checks)

| # | identifier | source | decision | reason |
|---|---|---|---|---|
| 30 | PMID 36029755 | Chaput JP, et al. Years of life gained when meeting sleep duration recommendations in Canada. *Sleep Med* 2022 | **INCLUDE** | **The end-to-end calibration target.** Sleep *duration alone*, life table + meta-analytic RR: 1.2 years at age 20 versus short sleepers. Our machinery reproduces it at an all-cause HR of 1.10–1.13. |
| 31 | PMID 37831896 | Li H, et al. *QJM* 2024 | **INCLUDE** | US NHIS–NDI, men: 4.7 years at age 30 — but for a 5-factor sleep composite, so an upper bound on a syndrome, not on duration. |
| 32 | PMID 36859313 | Huang BH, et al. *BMC Med* 2023 | **INCLUDE** | CVD-free life expectancy, men: 2.31 years lost (poor sleepers), 0.55 (intermediate). The intermediate contrast is the relevant one for mild restriction and is 4× smaller. |
| 33 | PMID 37036905 | Ma H, et al. Cardiovascular Health and Life Expectancy. *Circulation* 2023 | **INCLUDE** | Found late. The **largest** published sleep life-expectancy figure (5.0 y at 50) and the one most likely to be misquoted; included specifically so the pipeline sees why it is a ceiling. Its own arithmetic refutes it: tobacco (7.4 y) + sleep (5.0 y) = 12.4 y exceeds the entire 8.9-y total contrast. |
| 34 | PMID 28983434 | Hafner M, et al. Why Sleep Matters. *Rand Health Q* 2017 | **INCLUDE** | The RAND report the brief named. **Reports reality against the brief's hint:** RAND publishes *no* life-expectancy or QALY estimate. Its usable quantities are the imported mortality RRs (1.13 for <6 h, 1.07 for 6–7 h) and economic costs ($280–411 bn/yr US). rand.org returns 403; retrieved from the PMC copy of the *Rand Health Quarterly* reprint. |

---

## 4. Excluded — assessed and rejected, with reasons

The 141 surfaced PubMed records less the 26 included leaves 115 exclusions. Grouped by reason;
individually named where a reviewer would plausibly ask why.

### 4.1 Task-named source that could not be quoted (1)

| identifier | source | reason for exclusion |
|---|---|---|
| PMID 41562125 / doi:10.1161/CIR.0000000000001412 | **2026 AHA Heart Disease and Stroke Statistics Update**, *Circulation* 2026;153(9):e275–e906 | **The one task-named source this shard could not open.** Existence, DOI, PMID and pagination all verified, and confirmed as the *current* edition (superseding PMID 39866113, the 2025 update, which is excluded for the same reason). But ahajournals.org returns HTTP 403 for both the HTML and reader views, there is no PMC copy, and the PubMed abstract is a scope statement with no statistics. Hard rule 2 forbids extracting a number that cannot be quoted, so nothing was taken rather than recalled. Independently, the Update does not compute lifetime risk itself — its lifetime-risk statements cite Lloyd-Jones 1999/2006 and Wilkins 2012, all of which are included here at first hand, so extracting it would have double-counted Framingham. Logged in `baseline_risks.yaml` as `aha_statistical_update_cvd_lifetime_risk` with an action note for an operator who has institutional access. |

### 4.2 Wrong estimand for a lifetime-risk denominator (11)

| identifier | source | reason |
|---|---|---|
| PMID 34170288 | Trends in prevalence of diabetes and control of risk factors, 1999–2018, *JAMA* 2021 | Trend analysis of prevalence; superseded for denominator purposes by the current NHANES brief (#11). |
| PMID 34107181 | Trends in diabetes treatment and control, *NEJM* 2021 | Treatment/control outcomes, not incidence or lifetime risk. |
| PMID 40339738 | Diabetes prevalence, awareness, and control, 2017–2023 | Duplicates NHANES coverage already held from the primary NCHS brief. |
| PMID 21050532, 23102115, 29155682, 28463104, 24429341 | Older NCHS hypertension briefs (1999–2016 data) | Superseded by Data Brief 511 (#13); retaining them would add nothing but stale denominators. |
| PMID 23101933 | Prevalence of uncontrolled CVD risk factors, 1999–2010 | Risk-factor control, not disease risk. |
| PMID 41027398 | CVD risk factors in adults, Aug 2021–Aug 2023 | Risk-factor prevalence; the CVD *lifetime risk* deliverable is served by #14–16. |
| PMID 39380201 | NHANES 2017–March 2020 prepandemic file documentation | Methodological documentation, contains no estimates. |

### 4.3 Right topic, wrong population (9)

| identifier | source | reason |
|---|---|---|
| PMID 33957617 | Sleep duration, mortality and quality of life in chronic kidney disease (KNHANES) | The *only* paper found linking sleep to a QALY-like outcome, and it is CKD patients in Korea. Not transportable to a healthy US 19-year-old; recorded as such in the `qaly_estimate_for_short_sleep` block. |
| PMID 33225415 | Lifetime risk of diabetes in metropolitan cities in India | Wrong country; Indian lifetime risks differ substantially. |
| PMID 41092927, 41092928 | GBD 2023 global mortality / cause-of-death, *Lancet* 2025 | GBD life tables are modelled estimates; for a single-country US male life table NCHS and SSA are the authoritative national sources and are already included. Retained as a fallback only. |
| PMID 39240352 | Gestational diabetes and cognition in parous women | Female-only, wrong exposure. |
| PMID 18606953 | Psychiatric disorders in pregnant and postpartum women | Female-only. |
| PMID 40694784 | Obesity and insulin resistance in perimenopausal women | Female-only. |
| PMID 41687052 | Obesity among US active-component service members | Selected occupational population with fitness standards; not general-population. |
| PMID 34291279, 40915576, 41325988 | Childhood/adolescent adiposity trends (NHANES, COVID-era) | Prevalence trends in children; the *projection to adulthood* deliverable is served by Ward 2017 (#23). |

### 4.4 Right cohort, wrong disorder — NCS-R / NESARC family (19)

All are companion papers from the same two surveys already represented by #24, #25 and #26.
Excluded to avoid double-counting correlated estimates from a single `cohort_family`, and
because none reports MDD in males 18–25.

PMID 15939839 (12-month DSM-IV disorders), 19012815 (cannabis withdrawal), 19274052
(irritability in MDD), 19486727 (alcohol transitions), 19540311 (anxiety genetics), 19564874
(bipolar with frequent episodes), 20124111 and 20124112 (childhood adversities), 20713498 (MDD
with subthreshold bipolarity), 21190638 (chronic MDD and dysthymia), 21457678 (obesity and
substance/mood disorders), 21867593 (alcohol severity predicting depression), 21999032 (racial
differences in MDD treatment), 22147808 (DSM-IV disorders in NCS-A), 22273480 (lifetime
comorbidity in NCS-A), 22752056 (intermittent explosive disorder), 26039070 (DSM-5 alcohol use
disorder), 26374990 and 27337416 (prescription opioid use disorder), 35275407 (alcohol
withdrawal).

**One near-miss inside this group:** PMID 15939837 (Kessler 2005, *Arch Gen Psychiatry*,
lifetime prevalence and age-of-onset of DSM-IV disorders) was assessed carefully because its
age-of-onset distributions are relevant to an 18-year-old. It is **cited inside the
`kessler2003_mdd_ncsr` record** for the median-age-of-onset figure rather than given its own
record, because it reports the same NCS-R sample and a separate record would let the pooler
count NCS-R twice.

### 4.5 Adjacent outcome, not a shard deliverable (10)

| identifier | source | reason |
|---|---|---|
| PMID 35057911 | Lifetime risk of heart failure in Framingham, *JACC* 2022 | Well-executed and same method, but heart failure is not among the seven outcomes assigned; the CVD-total deliverable is served by Wilkins 2012. Flagged in the station report as the cheapest available extension. |
| PMID 18031707 | Lifetime risk of stroke and dementia (Framingham), *Lancet Neurol* 2007 | Review of the Framingham estimates already held first-hand from Seshadri 1997 and Chêne 2015. |
| PMID 34487721 | GBD stroke burden | Stroke-specific, global. |
| PMID 41240917 | Lifetime and 10-year risk of cognitive impairment by amyloid PET severity, *Lancet Neurol* 2026 | Conditions on an amyloid-PET biomarker the subject has no measurement of; not a population denominator. |
| PMID 28323826 | APOE-related risk of MCI and dementia for prevention trials | Genotype-conditional risk; not applicable without genotype. |
| PMID 39480421, 39772767, 40250880, 41632497, 41637062, 42012820 | Cost-effectiveness and treatment-equity models (aducanumab, semaglutide, tirzepatide, BP intensity, hearing loss, Alzheimer treatment equity) | Intervention economics. Their QALY figures are conditional on treatment and cannot serve as baseline risks. Screened specifically because they were the closest hits to a "QALY" query, and none supplies a sleep-related QALY. |
| PMID 39171613, 41584203 | Life's Essential 8 meta-analysis and LE8–frailty study | LE8 composite outcomes; the one LE8 paper with a life-expectancy estimate and a separable sleep component (Ma 2023) is included as #33. |

### 4.6 Off-topic — surfaced by broad query terms (65)

Screened by title and journal, excluded without full-text retrieval. Includes clinical and
surgical series, oncology risk, transplant, imaging, rheumatology, orthopaedics, urology,
veterinary medicine and non-English reports, e.g. PMID 20470470 (menopause management in
Portuguese), 42424802 (bovine respiratory disease in feedlot cattle), 42389461 (total hip
arthroplasty bearing surfaces), 42405711 (second primary cancer after prostate radiotherapy),
41423240 (Japanese-language QoL and metabolic syndrome report), 42432261 (pancreatic IPMN),
42439920 (fibroblast activation protein), plus intracerebral-haemorrhage, atrial-fibrillation
and bariatric-surgery series. Full identifier list in `/tmp/s17/surfaced_titles.json`.

---

## 5. Queries run

**PubMed (36).** Life tables and method: cause-deleted life tables / decompositions of life
expectancy (Beltrán-Sánchez); Barendregt coping with multiple morbidity in a life table
(0 hits); Fine–Gray subdistribution of a competing risk; Beiser/D'Agostino computing estimates
of incidence including lifetime risk. Diabetes: lifetime risk diabetes United States Gregg
years of life lost modelling; Narayan lifetime risk for diabetes mellitus United States;
trends prevalence diabetes control risk factors US adults; prevalence total diabetes
undiagnosed United States adults age groups NHANES 2021–2023. Hypertension: residual lifetime
risk hypertension Framingham Vasan; hypertension prevalence among adults United States NHANES
age sex data brief. CVD: lifetime risk cardiovascular disease Lloyd-Jones risk factor burden 50
years age; lifetime risk total cardiovascular disease Wilkins years lived free; Berry lifetime
risks of cardiovascular disease NEJM 2012 (0 hits); lifetime risk cardiovascular disease young
adulthood age 20 30 years cohort (0 hits); Heart Disease and Stroke Statistics 2025 Update AHA;
Heart Disease and Stroke Statistics 2026 Update AHA[Title]. Dementia: lifetime risk of dementia
among US adults; lifetime risk dementia Alzheimer Seshadri Framingham mortality risk estimates;
Chêne gender incidence dementia Framingham mid-adult life. Obesity: lifetime risk of obesity
United States adults; prevalence of obesity severe obesity United States NHANES adults
2021–2023; Stierman NHANES obesity prevalence adults; Ward simulation of growth trajectories of
childhood obesity into adulthood. Depression: epidemiology of major depressive disorder NCS-R
Kessler 2003; Kessler lifetime prevalence age of onset DSM-IV NCS-R; Kessler Berglund Demler Jin
Merikangas Walters lifetime prevalence DSM-IV disorders; Hasin epidemiology adult DSM-5 major
depressive disorder United States. Suicide: Garnett Curtin suicide mortality in the United
States NCHS data brief; Curtin suicide rates United States 15 24 provisional. Sleep and life
expectancy: sleep duration life expectancy years of life lost modelling population; short sleep
duration quality adjusted life years lost; sleep duration mortality life expectancy years
gained; healthy sleep habits gain in life expectancy; sleep patterns life expectancy men women
low-risk sleep factors; Hafner why sleep matters economic costs of insufficient sleep
cross-country; insufficient sleep mortality risk economic cost gross domestic product RAND
(0 hits).

**Non-PubMed retrieval (11).** `ftp.cdc.gov` NVSR 74-06 `Table02.xlsx` and the report PDF;
`ssa.gov/oact/STATS/table4c6.html` (403 to direct requests, retrieved through a text proxy);
NCHS Data Briefs 471, 508, 509, 511, 516, 540 (PDFs); NSDUH 2024 detailed tables (ZIP, table
6.39B); NIMH statistics pages for depression and suicide; RAND RR-1791 (403, retrieved via the
PMC reprint); Crossref and PubMed E-utilities for identifier verification on every record.

**Retrieval failures, all logged rather than worked around.** `ahajournals.org` 403 (AHA
Statistical Update, both editions — no number extracted); `diabetesjournals.org` 403 plus a
Cloudflare challenge through the text proxy (Narayan 2007 Table 2 — intermediate BMI categories
left `null`); `rand.org` 403 (worked around legitimately via the peer-reviewed PMC reprint of
the same report); `ssa.gov` 403 (worked around via text proxy, values cross-checked against
NCHS over the overlapping ages 19–99).
