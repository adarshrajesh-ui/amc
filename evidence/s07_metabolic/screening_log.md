# Screening log — shard `s07_metabolic`

Domain: glucose metabolism, insulin sensitivity, and type 2 diabetes risk from short sleep.
Target subject: 18-year-old male, weekday sleep ~5–6 h from age 16 to 19, weekend/holiday 7–8 h,
occasional 3–4 h nights before exams, occasional 10–11 h weekend nights.

**Records screened: 54. Included as YAML records: 30. Excluded: 24.**
Gate G1 (≥25 screened) satisfied; the task's stronger requirement of ≥30 screened is also satisfied.

Search routes used: PubMed E-utilities (esearch / esummary / efetch), Europe PMC REST search and
`fullTextXML`, NCBI PMC efetch, Crossref `/works`, Unpaywall. Every included record's DOI **and**
PMID were checked programmatically against both Crossref and PubMed (`_tools/verify.py`,
results in `_verify.json`): **29/30 VERIFIED, 1 flagged CHECK for a documented metadata artefact
only** (see the Verification note at the end).

---

## Included (30)

Ordered by evidence tier. `match` = `population.adolescent_match`.

| study_id | PMID | design | tier | n | match | effects | access |
|---|---|---|---|---|---|---|---|
| beals2026 | 41564347 | rct_parallel | T1 | 29 | poor_midlife | 2 | abstract_only |
| broussard2012 | 23070488 | rct_crossover | T1 | 7 | good_young_adult | 4 | abstract_only |
| buxton2010 | 20585000 | lab_restriction_within_subject | T1 | 20 | good_young_adult | 3 | full_text |
| buxton2012_fd | 22496545 | lab_restriction_within_subject | T1 | 21 | fair_adult | 2 | abstract_only |
| cheung2026 | 41165770 | rct_parallel | T1 | 48 | good_young_adult | 3 | full_text |
| depner2019 | 30827911 | rct_parallel | T1 | 36 | good_young_adult | 4 | abstract_only |
| dutil2024 | 38070132 | rct_crossover | T1 | 36 | **exact_16_19** | 3 | abstract_only |
| hartescu2022 | 34459060 | rct_parallel | T1 | 18 | poor_midlife | 2 | abstract_only |
| killick2015 | 25683266 | rct_crossover | T1 | 19 | fair_adult | 4 | full_text |
| klingenberg2013 | 23814346 | rct_crossover | T1 | 21 | **exact_16_19** | 5 | abstract_only |
| leproult2014 | 24458353 | rct_parallel | T1 | 26 | fair_adult | 4 | full_text |
| nedeltcheva2009 | 19567526 | rct_crossover | T1 | 11 | poor_midlife | 3 | abstract_only |
| nedeltcheva2012 | 22513492 | rct_crossover | T1 | 10 | poor_midlife | 3 | full_text |
| ness2019 | 30892916 | lab_restriction_within_subject | T1 | 15 | good_young_adult | 3 | abstract_only |
| sondrup2022 | 35189549 | meta_analysis_of_trials | T1 | 21 studies | mixed | 3 | abstract_only |
| spiegel1999 | 10543671 | lab_restriction_within_subject | T1 | 11 | good_young_adult | 4 | **secondhand** |
| yuan2021 | 34744800 | lab_restriction_within_subject | T1 | 30 | fair_adult | 2 | full_text |
| zuraikat2024 | 37955852 | rct_crossover | T1 | 38 | fair_adult | 4 | abstract_only |
| bos2019 | 31096629 | mendelian_randomization | T3 | 58,074 | poor_midlife | 4 | abstract_only |
| dashti2019 | 30846698 | mendelian_randomization | T3 | 446,118 | poor_midlife | 2 | full_text |
| gao2020 | 33384720 | mendelian_randomization | T3 | 446,118 | poor_midlife | 4 | full_text |
| kuroda2025 | 40181521 | mendelian_randomization | T3 | 385,135 | poor_midlife | 6 | full_text |
| wang2019 | 30508554 | mendelian_randomization | T3 | 159,208 | mixed | 4 | abstract_only |
| cappuccio2010 | 19910503 | meta_analysis_observational | T5 | 107,756 | poor_midlife | 5 | full_text |
| liu2025 | 39748566 | meta_analysis_observational | T5 | 1,478,297 | poor_midlife | 5 | full_text |
| shan2015 | 25715415 | dose_response_meta_analysis | T5 | 482,502 | poor_midlife | 5 | abstract_only |
| chen2021 | 33221190 | cross_sectional | TX | 384 | mixed | 3 | abstract_only |
| javaheri2011 | 21146189 | cross_sectional | TX | 387 | **exact_16_19** | 3 | abstract_only |
| matthews2012 | 23024433 | cross_sectional | TX | 245 | **exact_16_19** | 3 | abstract_only |
| wang2025_wsr | 40590721 | cross_sectional | TX | 4,036 | poor_midlife | 3 | full_text |

Totals: 105 effect estimates. Tier mix: T1 = 18, T3 = 5, T5 = 3, TX = 4. **No T2 and no T4 record
exists in this shard** — see the exclusions below for why, and `station_report.md` for the
consequence.

---

## Excluded (24), with reasons

### A. Reviews and commentary — no independent extractable effect estimate

| # | PMID | Record | Decision & reason |
|---|---|---|---|
| 1 | 29510179 | Reutrakul & Van Cauter 2018, *Metabolism* — "Sleep influences on obesity, insulin resistance, and risk of type 2 diabetes" | **EXCLUDE.** Narrative review by the senior author of `spiegel1999`. No pooled estimate, no new data. Paywalled with no PMC deposit, so it could not even be mined for the Spiegel magnitudes I needed. Screened specifically in the hope of resolving the `spiegel1999` secondhand problem; it did not. |
| 2 | 24937041 | Nedeltcheva & Scheer 2014, *Curr Opin Endocrinol Diabetes Obes* | **EXCLUDE.** Narrative review, no extractable estimate. Its primary studies are already captured (`nedeltcheva2009`, `nedeltcheva2012`). |
| 3 | 17308390 | Van Cauter et al. 2007, *Horm Res* — "Impact of sleep and sleep loss on neuroendocrine and metabolic function" | **EXCLUDE.** Narrative review; superseded by `sondrup2022` (quantitative meta-analysis of 21 trials) for the same purpose. |
| 4 | 36754840 | Vgontzas group 2023, *Obesity* — "Sleep variability and regularity as contributors to obesity and cardiometabolic health in adolescence" | **EXCLUDE.** Narrative review, not a primary study — despite an abstract structured with a "RESULTS" heading. Topically a near-perfect match (adolescents, sleep variability, our subject's exact pattern), which is why it was screened; but it reports no numbers. Also note a DOI inconsistency in the PubMed record (header shows `10.1002/oby.23768`, the DOI line shows `10.1002/oby.23667`) — a further reason not to cite it. Its theme is instead covered quantitatively by `cheung2026` and `wang2025_wsr`. |
| 5 | 38243378 | Taheri 2024, *Sleep* — "Waking up to sleep extension for cardiometabolic health" | **EXCLUDE as a record, USED as corroboration.** Invited commentary on `dutil2024`. Retrieved in full and used to confirm that the `dutil2024` insulin-sensitivity index was the Matsuda index and that the magnitude was ~20%, and to recover cohort descriptors that the publisher-blocked primary paper would not yield. Cited inside `dutil2024.yaml` `secondhand_via`. Contributes no independent effect estimate. |
| 6 | 41568460 | Coven, Jelic & St-Onge 2026, *Arterioscler Thromb Vasc Biol* — "Fluctuations in Sleep Duration and Timing and Cardiometabolic Risk" | **EXCLUDE.** Review from the group that produced `zuraikat2024`. No independent estimate; its trial evidence is already captured. |

### B. Wrong outcome — not glucose metabolism / insulin sensitivity / T2D

| # | PMID | Record | Decision & reason |
|---|---|---|---|
| 7 | 42192565 | Dutil et al. 2026, *J Sleep Res* — sleep manipulation and BDNF in adolescents at risk for T2D | **EXCLUDE.** Same SMART2D trial as `dutil2024`, but the outcome is brain-derived neurotrophic factor, not a glycaemic measure. Out of domain, and would double-count the trial. Flagged as a lead for a cognition/neuro shard. |
| 8 | 37201593 | Widome et al. 2023, *Prev Med* — START study, delaying high school start times | **EXCLUDE, WITH REGRET — this is the T2 gap.** A genuine quasi-experiment (natural experiment in school start times) in exactly the right age group, and the only realistic route to T2 evidence for an adolescent sleep exposure. But the outcomes are weight and weight-related behaviours, not glycaemia. Belongs to the anthropometric shard. Its absence is why this shard has **no T2 record at all**. |
| 9 | 30060859 | Gariépy et al. 2018, *J Adolesc Health* — school start time and healthy weight | **EXCLUDE.** Outcome is weight status; no glycaemic measure. |
| 10 | 28670711 | Marx et al. 2017, *Cochrane Database Syst Rev* — later school start times | **EXCLUDE.** Systematic review; outcomes are education, health and well-being broadly, with no glycaemic outcome extracted. |
| 11 | 38847813 | Sadikova et al. 2024, *Soc Psychiatry Psychiatr Epidemiol* — delaying school start times and depressed mood | **EXCLUDE.** Psychiatric outcome; belongs to a mood shard. |
| 12 | 36876501 | Penn State Child Cohort 2023, *Hypertension* — circadian misalignment, visceral adiposity and elevated blood pressure in adolescents | **EXCLUDE.** Blood-pressure outcome; belongs to the cardiovascular shard. Right cohort and right age, wrong outcome. |

### C. Wrong exposure — sleep-disordered breathing rather than sleep duration

| # | PMID | Record | Decision & reason |
|---|---|---|---|
| 13 | 19926716 | Tsaoussoglou et al. 2010, *JCEM* — sleep-disordered breathing in obese children, inflammation and metabolic abnormalities | **EXCLUDE.** Exposure is SDB, not sleep duration or restriction. Relevant only as a reminder that undiagnosed apnoea is a confounder in the observational literature — a point already carried in `bos2019` and `cappuccio2010`. |
| 14 | 34160576 | Penn State Child Cohort 2021, *JAMA Cardiol* — paediatric obstructive sleep apnoea and blood pressure | **EXCLUDE.** Wrong exposure (OSA) and wrong outcome (BP). |
| 15 | 39462147 | 2025, *J Sleep Res* — CRP and detection of hypertension and insulin resistance in mild-to-moderate OSA | **EXCLUDE.** Exposure is OSA severity; the paper is about a biomarker's diagnostic performance, not about sleep duration. |
| 16 | 25684658 | Rodríguez-Colón et al. 2015, *Metabolism* — metabolic syndrome burden and cardiac autonomic modulation, Penn State Children Cohort | **EXCLUDE.** Exposure is metabolic syndrome burden; sleep is not the exposure. Screened because the task named the Penn State child cohorts explicitly. |
| 17 | 25220887 | He et al. 2015, *J Clin Densitom* — abdominal obesity and metabolic syndrome burden in adolescents, Penn State Children Cohort | **EXCLUDE.** Exposure is adiposity, not sleep. |

### D. Right topic, but composite outcome or unusable effect structure

| # | PMID | Record | Decision & reason |
|---|---|---|---|
| 18 | 37792965 | Morales-Ghinaglia et al. 2024, *Sleep* — circadian misalignment modifies the association of visceral adiposity with metabolic syndrome in adolescents (Penn State Child Cohort, median age 16, ≥5 nights actigraphy + PSG) | **EXCLUDE — the most painful exclusion in the log.** Population is an essentially perfect match (median 16 y, objective sleep, sleep midpoint / sleep irregularity / social jetlag as exposures — the subject's exact pattern). But the outcome is a **composite metabolic-syndrome score** that bundles waist circumference, blood pressure, insulin resistance, triglycerides and cholesterol, and the published effects are **effect-modification terms on the visceral-adiposity→MetS association** (e.g. 2.66 [0.30] points where social-jetlag >1.5 h vs 1.08 [0.45] where <30 min), not sleep→glycaemia estimates. No insulin-resistance-specific coefficient is recoverable, and the full text is publisher-blocked (Europe PMC returned 0 bytes for PMC10782492). Extracting a glucose effect from it would require inventing a decomposition. **Highest-priority target if a later station obtains the full text.** |
| 19 | 42299543 | Wang et al. 2026, *Medicine (Baltimore)* — insulin resistance mediates the association between sleep duration and T2D, urban–rural Chinese cohort | **EXCLUDE (borderline).** Topically apt and it is a cohort, but the contribution is a mediation decomposition rather than a dose-response or per-hour risk estimate, and it adds a fourth partially-overlapping observational syntheses stream on top of `shan2015`, `cappuccio2010`, `liu2025` and `kuroda2025`. Excluded on marginal-value and double-counting grounds, not on quality. |

### E. De-duplication — same cohort/resource already represented

| # | PMID | Record | Decision & reason |
|---|---|---|---|
| 20 | 40437485 | Liu, Chu & Ding 2025, *BMC Med* — weekend catch-up sleep and insulin resistance, NHANES cross-sectional | **EXCLUDE for cohort-family duplication (gate G6).** Same question, same outcome (HOMA-IR) and the **same NHANES resource** as the included `wang2025_wsr`. Including both would double-count a single data source in the shard's most decision-relevant exposure contrast. `wang2025_wsr` was preferred because it stratifies by **sex** and by **weekday sleep duration** — the two strata that isolate our subject — and adjusts for social jetlag and weekday sleep hours. Recorded here so a later station can substitute or triangulate; flagged inside `wang2025_wsr.yaml` notes as well. |
| 21 | 39028757 | Singh, Beyl, Marlatt & Ravussin 2025, *JCEM* — "Sleep Duration Alters Overfeeding-mediated Reduction in Insulin Sensitivity" | **EXCLUDE (borderline, next-best addition).** Directly addresses the energy-balance × sleep interaction, which is a live modifier in this shard. Excluded because that interaction is already carried, with a cleaner two-arm contrast, by the matched `nedeltcheva2009` (ad libitum food, weight gain → harm) / `nedeltcheva2012` (hypocaloric, weight loss → no harm) pair. If the modeller wants to put weight on the energy-balance modifier, this is the first record to add. |

### F. Exposure too acute to inform a 3-year chronic exposure

| # | PMID | Record | Decision & reason |
|---|---|---|---|
| 22 | 40841449 | Hsu et al. 2026, *Eur J Appl Physiol* — acute glucose-tolerance impairment after **one night** of partial sleep restriction is not rescued by moderate-intensity walking in young men | **EXCLUDE.** Right population (young men) and a genuinely interesting negative result on exercise as a rescue, but a single night of restriction is a different exposure from 3 years of chronic partial restriction, and single-night studies are systematically more dramatic per unit sleep lost. Kept out to avoid contaminating the chronic dose-response. Noted as relevant if the report addresses "can exercise offset this?". |
| 23 | 42231340 | 2026, *J Transl Med* — body-weight-specific and shared metabolomic responses to acute sleep loss in young adults | **EXCLUDE.** Acute total sleep loss; outcome is an untargeted metabolomic signature with no interpretable glycaemic effect size. |
| 24 | 41666816 | 2026, *Sleep Med* — circadian gene expression in adolescents and concurrent circadian disruption | **EXCLUDE.** Mechanistic transcriptomic outcome, not a glycaemic measure. |

### Additional queries run that returned nothing usable (documented for completeness)

These searches were executed and produced **no new includable record**; they are logged because a
null search result is itself evidence about the state of the literature.

- `Penn State Child Cohort sleep duration insulin resistance adolescents actigraphy` → PubMed COUNT 0.
  Europe PMC `"Penn State Child Cohort" AND (insulin OR HOMA OR glucose)` → 35 hits, all screened;
  none reports sleep duration → insulin resistance as an extractable estimate (rows 12, 14, 16, 17, 18).
- `adolescents polysomnography short sleep duration insulin resistance HOMA cohort` → COUNT 0.
  **There is no prospective adolescent cohort with objective sleep exposure and incident glycaemic
  outcomes.** This is the reason the shard contains no T4 record and why `javaheri2011`,
  `matthews2012` and `chen2021` — the three age-matched observational records — are all TX
  (cross-sectional).
- `experimental sleep restriction adolescents insulin sensitivity randomized crossover` → 3 hits, all
  already handled (`dutil2024`, `klingenberg2013`, `broussard2012`). **Only two randomised
  sleep-manipulation trials with a glycaemic outcome exist in adolescents.**
- `school start time AND (metabolic OR insulin OR glucose OR BMI)` → 7 hits; none with a glycaemic
  outcome (rows 8–11). Confirms the absence of T2 evidence in this domain.

---

## Verification note

`_tools/verify.py` checks each record's DOI against Crossref and its PMID against PubMed, confirms
that the DOI registered against the PMID matches the DOI in the record, and computes a token-Jaccard
similarity between the Crossref and PubMed titles. Result: **29/30 VERIFIED**.

The single `CHECK` is **`cappuccio2010`** (title_similarity 0.64). This is a metadata artefact, not a
citation problem: Crossref stores the title as "Quantity and Quality of Sleep and Incidence of Type 2
Diabetes" and holds the subtitle ("a systematic review and meta-analysis") in a separate field, so the
subtitle tokens are missing from the comparison and drag the Jaccard score below the 0.70 threshold.
The DOI `10.2337/dc09-1124` resolves in Crossref, is the DOI PubMed registers against PMID 19910503,
and journal and year agree. The record is marked `status: VERIFIED` with this artefact documented
inline in the YAML. `broussard2012` (0.71) and `kuroda2025` (0.95) pass but fall below 1.00 for the
same class of reason (subtitle handling and `<scp>` markup around "UK" respectively).

**No identifier failed to resolve. No record required `pmid: null` or `doi: null`.**

## Access-tier note

`full_text` = 12, `abstract_only` = 17, `secondhand` = 1.

The high `abstract_only` count is not a shortcut: it reflects publisher blocking. Europe PMC
`fullTextXML` returned 0 bytes, or NCBI PMC returned "The publisher of this article does not allow
downloading of the full text in XML form", for Oxford University Press (*Sleep*), the American
Diabetes Association (*Diabetes Care*), Annals of Internal Medicine, Cell Press (*Current Biology*),
and others. Every affected record documents the specific failed retrieval route in `secondhand_via`.
Where an abstract published usable dispersion (`zuraikat2024` reports β ± SEM directly;
`nedeltcheva2009` reports per-condition means ± SD with p-values) no precision was lost.

The one `secondhand` record is **`spiegel1999`**, the shard's most-cited study. The *Lancet* 1999
full text is paywalled (Unpaywall `is_oa=false`, no PMC deposit), so the design, n and p-values are
first-hand from the publisher abstract but the 30–40% magnitudes come from two independently
retrieved open-access sources that describe the study (PMC2929498 and the Discussion of `buxton2010`,
PMC2927933). This is documented in the record, and the subject's age — reported only as "11 young
men" — was left `null` rather than guessed.
