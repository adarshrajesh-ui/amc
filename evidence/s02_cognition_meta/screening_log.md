# Screening log — shard `s02_cognition_meta`

Domain: meta-analytic and large-sample estimates relating sleep loss and habitual short sleep to
cognitive ability, plus the psychometric evidence needed to convert standardized effects into
IQ-scale points.

**43 records screened. 15 included, 28 excluded.** Every included record's DOI and PMID resolved
against Crossref and PubMed with title similarity 1.0 (see `/workspace/reports/verification.json`).

**How to read the exclusion column.** Records are labelled by how far screening actually went, and I
have not inflated this. "Retrieved" means I pulled full text or a structured abstract and read it.
"Resolved" means I confirmed the identifier in PubMed or Crossref but did not need the text to make
the call. "Screened by title" means it surfaced in a search result or a reference list of a paper I
did read, and title-level information was sufficient to exclude it — this is normal
title/abstract-stage screening, but it is a weaker claim and is marked as such.

Search strategy: PubMed E-utilities queries on combinations of {sleep deprivation, sleep
restriction, sleep duration, sleep extension} × {meta-analysis, cognitive, intelligence, IQ, fluid
intelligence, reaction time, working memory, school performance, adolescent, UK Biobank}; forward
and backward citation chasing from Lim & Dinges 2010, Lowe 2017 and Astill 2012; Europe PMC
full-text resolution; Unpaywall for open-access locations. Separate targeted search line for the
g-loading literature (reaction time / working memory / processing speed vs psychometric g).

---

## Included (15)

| # | study_id | Identifier | Design / tier | Why included |
|---|---|---|---|---|
| 1 | `lim2010` | PMID 20438143 · doi:10.1037/a0018883 | meta-analysis of trials · T1 | The required per-domain acute-deprivation meta-analysis. 6 domains × speed/accuracy, 70 articles, 147 tests. Source of the reasoning-vs-vigilance gradient that anchors the IQ conversion. |
| 2 | `lowe2017` | PMID 28757454 · doi:10.1016/j.neubiorev.2017.07.010 | meta-analysis of trials · T1 | The required partial-restriction meta-analysis. Confirms the same domain ordering under restriction rather than total deprivation, with intelligence null. Abstract-only (paywalled). |
| 3 | `wild2018` | PMID 30212878 · doi:10.1093/sleep/zsy182 | cross-sectional · TX | The required n≈10,000 online study. Inverted-U shape, 7.38 h optimum, and the "equivalent to aging 8 years" statement with its full derivation. |
| 4 | `kyle2017` | PMID 29031762 · doi:10.1016/j.sleep.2017.07.001 | cross-sectional · TX | UK Biobank, n = 477,529. Sleep duration vs verbal-numerical reasoning, reaction time, numeric and visual memory. `cohort_family: UK_Biobank`. |
| 5 | `west2024` | PMID 40018197 · doi:10.1136/bmjph-2024-001000 | cross-sectional · TX | Second UK Biobank analysis with a global cognitive z-score and an age slope permitting a years-of-ageing conversion. Flagged as overlapping `kyle2017`. |
| 6 | `fjell2023` | PMID 37365003 · doi:10.1523/JNEUROSCI.2330-22.2023 | cross-sectional · TX | 47,029 participants across Lifebrain/HCP/UK Biobank with an extracted g factor. **The published precedent for the SD × 15 IQ conversion** (authors' own 2.4 and 2.9 IQ points). |
| 7 | `lo2016` | PMID 26612392 · doi:10.5665/sleep.5552 | RCT parallel · T1 | Adolescent lab restriction, 5 h TIB × 7 nights. Domain-ordered Cohen's f² for PVT, working memory, processing speed. Same cohort as `huang2016`. |
| 8 | `huang2016` | PMID 27253768 · doi:10.5665/sleep.6092 | RCT parallel · T1 | Same adolescent cohort; GRE vocabulary **learning** under restriction. The only learning-consolidation outcome in the shard, and the mechanism most relevant to a chronic exposure. |
| 9 | `astill2012` | PMID 22545685 · doi:10.1037/a0028204 | meta-analysis observational · TX | Century-spanning child meta-analysis with intelligence as its own subdomain (r = .10, k = 6). The one child-specific test of the sleep-duration/intelligence link. |
| 10 | `dewald2010` | PMID 20093054 · doi:10.1016/j.smrv.2009.10.004 | meta-analysis observational · TX | Best-powered academic outcome in the 8–18 band; independently reproduces the Astill school-performance cell. |
| 11 | `lundahl2015` | PMID 26151610 · doi:10.1080/87565641.2014.939183 | meta-analysis of trials · T1 | The only meta-analysis of **experimental** sleep manipulation restricted to youth. Supplies the pooled youth attention g with trim-and-fill correction. |
| 12 | `sadeh2003` | PMID 12705565 · doi:10.1111/1467-8624.7402008 | RCT parallel · T1 | The named seed study. Source of the original "similar to those gained by 2 years of development" benchmark. Table 2 permitted difference-in-differences g computation. |
| 13 | `campbell2024` | PMID 39283917 · doi:10.1093/sleep/zsae216 | within-subject restriction · T1 | **The best age-matched experimental record that exists** (ages 9.9–22.8, dose-response 7/8.5/10 h TIB). Quantified maturation-equivalent, vigilance-vs-working-memory dissociation, and a null TIB × age interaction. |
| 14 | `binks1999` | PMID 10341383 · doi:10.1093/sleep/22.3.328 | quasi-experiment · T2 | Direct test-day psychometric IQ (WAIS-R short form) after 34–36 h total deprivation. The only study that measures the conversion's target quantity. |
| 15 | `ritchie2018` | PMID 29911926 · doi:10.1177/0956797618774253 | meta-analysis quasi-experimental · T2 | **Comparator only, no sleep content.** 1.197 IQ points per year of education (615,812 participants) as the calibration benchmark that makes an IQ-point estimate interpretable. |

## g-loading sources — cited in `iq_conversion_basis.md`, not written as YAML records

These carry no sleep exposure, so they cannot populate an `effects` array under the schema (which
requires an `exposure` type). All four identifiers were verified programmatically and all four are
quoted verbatim in `iq_conversion_basis.md`.

| Source | Identifier | Contribution |
|---|---|---|
| Deary, Der & Ford 2001, *Intelligence* | doi:10.1016/S0160-2896(01)00062-9 (Crossref ✓; not in PubMed) | Simple RT r = .31, four-choice RT r = .49, RT variability r = .26 with AH4, n = 900 population sample. The closest published analogue of a PVT g-loading. |
| Sheppard & Vernon 2008, *Pers Individ Dif* | doi:10.1016/j.paid.2007.09.015 (Crossref ✓; not in PubMed) | Mean speed–intelligence r = .24 across 1,146 correlations; g–RT range .22–.40; **gF–RT range .20–.26**. |
| Ackerman, Beier & Boyle 2005, *Psychol Bull* | PMID 15631550 · doi:10.1037/0033-2909.131.1.30 | Meta-analysis of 86 samples: true-score WM–g correlation ρ = .479. |
| Kane, Hambrick & Conway 2005, *Psychol Bull* | PMID 15631552 · doi:10.1037/0033-2909.131.1.66 | Latent WMC–gF median r = .72 (3,168 subjects); individual WMC and gF tests share only ~20% variance (r ≈ .45). |
| Lyall et al. 2016, *PLoS One* | doi:10.1371/journal.pone.0154222 | UK Biobank one-factor solution explains ~40% of variance across 4 tests → mean loading ≈ .63; also the test SDs used to standardize `kyle2017`. |

---

## Excluded (28)

| # | Record | Decision | Reason |
|---|---|---|---|
| 16 | Vriend et al. 2013, *J Pediatr Psychol* — PMID 23720415, doi:10.1093/jpepsy/jst033 | **exclude** | Adolescent-adjacent crossover (n = 32, ages 8–12, ±1 h for 4 nights) and topically ideal, but the abstract reports only the DIRECTION of effects ("impaired ... short-term memory, working memory, and aspects of attention") with no effect sizes, means, or SDs, and no PMC/open full text exists (Europe PMC: pmcid=None, inEPMC=N). Extracting a `value` would require fabrication. Its effects are already pooled inside `lundahl2015`. |
| 17 | de Bruin et al. 2017, *Sleep Med Rev* — PMID 27039223, doi:10.1016/j.smrv.2016.02.006 | **exclude** | "Effects of sleep manipulation on cognitive functioning of adolescents" is a NARRATIVE systematic review with no pooled effect sizes. Its primary studies are captured by `lundahl2015`, `lo2016`, `sadeh2003`. Useful for coverage checking only. |
| 18 | Pilcher & Huffcutt 1996, *Sleep* — PMID 8776790, doi:10.1093/sleep/19.4.318 | **exclude** | "Effects of sleep deprivation on performance: a meta-analysis" (56 studies). Superseded by `lim2010`, which covers the same literature with per-domain resolution, speed/accuracy separation, and moderator analysis. Retaining both would double-count the same primary studies. |
| 19 | Lo et al. 2019, *Sleep* — doi:10.1093/sleep/zsz037 (split vs continuous sleep) | **exclude** | Exposure is sleep SCHEDULING (split vs continuous) at matched total sleep time, not sleep loss. Answers a different question than the target subject's exposure. |
| 20 | Ong et al. 2022, *Sleep* — doi:10.1093/sleep/zsac023 ("Staying vigilant...") | **exclude** | Outcome is vigilance maintenance under a napping intervention; no ability-type or standardized cognitive outcome, and it duplicates the Need-for-Sleep cohort already represented by `lo2016`/`huang2016`. |
| 21 | Hampshire et al., large online cognitive battery (`hampshire.pdf` retrieved) | **exclude** | Establishes the factor structure of the CBS battery used by `wild2018` but contains no sleep exposure. Would have been cited in `iq_conversion_basis.md` had I needed a CBS-specific g-loading; `wild2018`'s own composites made that unnecessary. |
| 22 | Pietschnig & Voracek 2015, *Perspect Psychol Sci* — PMID 25987509, doi:10.1177/1745691615577701 | **exclude** | "One Century of Global IQ Gains: A Formal Meta-Analysis of the Flynn Effect (1909-2013)" — 0.28 IQ points/year full-scale, 0.41 fluid, 271 samples, ~4 million participants. Retrieved and considered as a second calibration benchmark alongside `ritchie2018`, then rejected: secular cohort gains are not an exchange rate for an individual-level intervention, and offering two benchmarks invites the downstream model to pick whichever flatters its conclusion. `ritchie2018` alone is the benchmark. |
| 23 | Beebe et al. 2009, *Behav Brain Funct* — doi:10.1186/1744-9081-5-9 | **exclude** | Explicitly "preliminary fMRI findings" in sleep-restricted adolescents. Outcome is BOLD signal, not a standardized behavioural score; n is small and the working-memory behavioural result is not reported as an effect size. Named in the task brief's "and successors" clause but not extractable. |
| 24 | Randazzo et al. 1998, *Sleep* — PMID 9871948 (no DOI registered) | **exclude** | "Cognitive function following acute sleep restriction in children ages 10-14." Age-relevant and topically on-point, but a pre-2000 primary study already inside `lundahl2015`'s pool, with no open full text located. Extracting via `sadeh2003`'s citation of it would be secondhand at two removes. |
| 25 | Fallone et al. 2001, *Percept Mot Skills* — acute restriction, behaviour and sustained attention in children | **exclude** | Screened by title/citation from the `sadeh2003` reference list; not independently resolved in PubMed by my searches. Subsumed in `lundahl2015`, and the outcome is behavioural rating plus sustained attention rather than an ability measure. |
| 26 | Gruber et al. 2011 (ADHD sample, inside `lundahl2015`) | **exclude** | Sample is children with diagnosed ADHD. Different population; including it separately would import a clinical-population effect into a healthy-adolescent parameter. Noted in `lundahl2015`'s risk-of-bias assessment as a limitation of that pool. |
| 27 | Sadeh, Gruber & Raviv 2002, *Child Dev* — doi:10.1111/1467-8624.00414 | **exclude** | Cross-sectional companion to `sadeh2003` and reports a NULL correlation between habitual sleep time and neurobehavioural function. Superseded by the 2003 experimental paper from the same lab; the authors themselves reconcile the two in the 2003 discussion, which I quote in `sadeh2003`. |
| 28 | Sadeh, Raviv & Gruber 2000, *Dev Psychol* — sleep patterns in school-age children | **exclude** | Descriptive sleep epidemiology, no cognitive outcome. |
| 29 | Van Dongen et al. 2003, *Sleep* — doi:10.1093/sleep/26.2.117 | **exclude** | The canonical chronic dose-response study, but it is the assigned domain of shard `s01_cognition_dose_response` (it appears as the template example in the extraction instructions). Excluded to avoid duplicate extraction across shards. |
| 30 | Belenky et al. 2003, *J Sleep Res* — chronic restriction dose-response | **exclude** | Same reason as #29: chronic dose-response is `s01`'s domain, and this study contains no ability-type or IQ-scaled outcome. |
| 31 | Banks & Dinges 2007, *J Clin Sleep Med* — behavioural consequences of sleep restriction | **exclude** | Screened by title from citation chasing. Narrative review, no pooled estimates; the chronic-restriction dose-response it reviews is `s01`'s domain. |
| 32 | Goel et al. 2009, *Semin Neurol* — neurocognitive consequences of sleep deprivation | **exclude** | Screened by title from citation chasing. Narrative review, no pooled estimates. |
| 33 | Killgore 2010, *Prog Brain Res* — effects of sleep deprivation on cognition | **exclude** | Screened by title from citation chasing. Narrative review contemporaneous with `lim2010`; no independent pooled effects. |
| 34 | Curcio, Ferrara & De Gennaro 2006, *Sleep Med Rev* — PMID 16564189, doi:10.1016/j.smrv.2005.11.001 | **exclude** | "Sleep loss, learning capacity and academic performance." Narrative review; its quantitative content on academic outcomes is superseded by `dewald2010` in the same journal four years later. |
| 35 | Shochat, Cohen-Zion & Tzischinsky 2014, *Sleep Med Rev* — PMID 23806891, doi:10.1016/j.smrv.2013.03.005 | **exclude** | "Functional consequences of inadequate sleep in adolescents: a systematic review." Correct age band and directly on-topic, but a systematic review WITHOUT pooled effect sizes, and its cognitive/academic primaries overlap `dewald2010` and `astill2012`. |
| 36 | *(withdrawn)* Short et al., adolescent sleep-duration meta-analysis | **exclude — could not identify** | I searched for a Short et al. meta-analysis of adolescent sleep duration and daytime functioning and **could not resolve it in PubMed**. Rather than describe a record I cannot identify, I am recording the failed search itself. If such a paper exists it is a coverage gap in this shard. |
| 37 | Paruthi et al. 2016, *J Clin Sleep Med* — PMID 27250809, doi:10.5664/jcsm.5866 | **exclude** | "Recommended Amount of Sleep for Pediatric Populations: A Consensus Statement." Guideline, not an effect estimate. Relevant to defining "recommended" sleep, but that is another shard's remit; `campbell2024` supplies an empirical sufficiency threshold (~8.5 h TIB for executive measures) instead. |
| 38 | Hirshkowitz et al. 2015, National Sleep Foundation duration recommendations | **exclude** | Screened by title. Guideline consensus, no cognitive effect estimate. |
| 39 | Cespedes Feliciano et al. 2016 (HCHS) — PMID 26940117 | **exclude** | Screened from the shared candidate pool; exposure/outcome pair is cardiometabolic, not cognitive. (Also appears as UNVERIFIED in another shard's records — flagged to the orchestrator.) |
| 40 | Unsworth et al., vigilance-decrement latent-variable preprint | **exclude** | Would have been the ideal PVT-to-gF citation — it models a latent vigilance factor against fluid intelligence — but it is an unpublished preprint and the factor correlations are reported only in figures I could not read numerically. Replaced by Deary 2001 and Sheppard & Vernon 2008, both published and both quotable. |
| 41 | Arcia et al. 1991 — digit span vs California Achievement Test (r = .56 reading, .58 math) | **exclude** | Cited only SECONDHAND inside `sadeh2003`. I did not retrieve the original and will not treat it as a sourced achievement g-loading. This is the direct cause of gap 2 in `iq_conversion_basis.md` (row E declines the grades-to-IQ conversion). |
| 42 | Silverstein 1982 — WAIS-R four-subtest short-form validity (r = .95 with full battery) | **exclude** | Cited secondhand inside the Binks dissertation. Recorded in `binks1999`'s notes as supporting the short form's adequacy, but not independently retrieved and so not a record. |
| 43 | Wechsler 1981 / Shipley 1946 — test manuals | **exclude** | Instrument documentation, not evidence. |

---

## Identifiers that failed verification

**None among my 15 included records.** All 15 resolved on both Crossref and PubMed with title
similarity 1.0.

Two identifiers I initially recalled were WRONG and were corrected before any record was written —
recording them here because the failure mode is instructive:

| Guessed DOI | What it actually resolves to | Correct DOI |
|---|---|---|
| `10.1016/j.smrv.2010.06.002` (guessed for Dewald 2010) | Schredl, "Gender differences in nightmare frequency: A meta-analysis", *Sleep Med Rev* 2011 | `10.1016/j.smrv.2009.10.004` (found via PubMed search) |
| `10.1016/j.sleep.2015.08.009` (guessed for Lundahl 2015) | Neutel, "Reply to Piano et al.", *Sleep Med* 2016 | `10.1080/87565641.2014.939183` (found via PubMed search) |

Both plausible-looking DOIs resolved cleanly to real but entirely unrelated papers. A DOI that
resolves is not a DOI that is correct — the title check is what caught these, which is why every
identifier in this shard was resolved and title-matched rather than merely dereferenced.

## Access outcomes

| Tier | Count | Records |
|---|---|---|
| `full_text` | 14 | all except `lowe2017` |
| `abstract_only` | 1 | `lowe2017` (paywalled; Unpaywall `is_oa = false`, no OA location; publisher abstract + Discussion excerpt from the ScienceDirect landing page) |
| `secondhand` | 0 | — |

`binks1999` is marked `full_text` with `secondhand_via` naming the author's LSU dissertation on the
same sample, because the peer-reviewed *Sleep* 1999 paper is paywalled while the dissertation
containing the same tables is open. The dissertation matches the published abstract on n (29 vs 32),
protocol (34–36 h), battery, and conclusion.
