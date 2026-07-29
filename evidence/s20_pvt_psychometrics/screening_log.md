# screening_log.md — shard `s20_pvt_psychometrics`

**44 records screened, 31 included, 13 excluded.** Every identifier below was resolved
programmatically against Crossref (`api.crossref.org/works/<DOI>`) and/or PubMed
(`eutils.../esummary.fcgi`). The identifiers for included rows were read back out of the YAML records
themselves, so this table and the records cannot disagree; the identifiers for excluded rows were
verified live while writing this log.

Access legend: `FT` = full text retrieved and read; `AB` = abstract only (full text blocked or paywalled).

---

## INCLUDED (31)

### Part A1 — which PVT metric is most sensitive to sleep loss

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 1 | 21532951 | 10.1093/sleep/34.5.581 | Basner & Dinges 2011, *Sleep* 34(5):581-591 | `FT` | The named target and the load-bearing record of the shard. Rank-ordered d_z for all 10 PVT metrics under both total and chronic partial deprivation, plus Table 4's raw within-subject differences **and their SDs** — the only published source for the σ the power calculation consumes. Table 4 arrived column-interleaved from the PDF text layer; I reconstructed it and then verified the reconstruction by independently recomputing all 14 published required-sample-sizes from the published effect sizes. All reproduced to ±1 subject. |

### Part A2 — validating a short PVT

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 2 | 22025811 | 10.1016/j.actaastro.2011.07.015 | Basner, Mollicone & Dinges 2011, *Acta Astronaut* 69(11-12):949-959 | `FT` | The named target. Gives the 22.7% mean effect-size attenuation (range 6.9–67.8%) from 10 min → 3 min over 1,656 paired administrations, and the mandatory 355 ms lapse threshold. **Reality check per instruction 4: the paper reports no correlation coefficient between PVT-B and PVT**, contrary to what the brief implies. I did not invent one. |
| 3 | 15354700 | 10.3758/bf03195580 | Loh, Lamond, Dorrian, Roach & Dawson 2004, *Behav Res Methods Instrum Comput* 36(2):339-346 | `AB` | Added because Part A2 otherwise rested on a single paper. Independent, earlier, differently-designed test of the same question, agreeing on both load-bearing points: sensitivity falls monotonically with shortening, and lapse percentage is the metric that breaks first while speed metrics survive at 2 and 5 min. |
| 4 | 21912278 | 10.1097/JOM.0b013e31822b8356 | Basner & Rubinstein 2011, *J Occup Environ Med* 53(10):1146-1154 | `AB` | Supplies the external-validity link Part A2 lacked — the 3-min PVT-B predicts a real non-PVT task (simulated luggage screening) — and independently confirms the 355 ms threshold. Also the only absolute, externally anchored numbers in the shard (11 and 20 lapses per 3-min PVT-B), which give the daily plot an interpretable y-axis. |

### Part A3 — test–retest reliability, within-person SD, practice curve

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 5 | 22215929 | 10.5665/sleep.1606 | Sunwoo et al. 2012, *Sleep* 35(1):149-158 | `AB` | Largest published PVT reliability estimate (n = 372) and it **contradicts** the widely repeated ">0.8 for lapses" folklore: median RT ICC 0.69, lapse count ICC 0.51, rising to 0.85 only when dichotomised. Also supplies the ESS-vs-MSLT correlation range (−0.270 to −0.195) used in Part B. Limitation recorded in the YAML: the four repeats were within one day, so this is not day-to-day reliability. |
| 6 | 34627928 | 10.1016/j.jneumeth.2021.109379 | Thompson et al. 2022, *J Neurosci Methods* 365:109379 | `AB` | The **only** rested-baseline, between-day, short-PVT reliability figures I could verify: mean RT ICC 0.79 / SEM% 4.14%, fastest-10% RT ICC 0.83 / SEM% 4.43%. The 4.14% is one of the two independent routes to σ_w. Also documents that error and lapse metrics have SEM% of 32.6–168.7%, i.e. unusable as a primary outcome. |
| 7 | 20805597 | 10.3758/BRM.42.3.754 | Wilson, Dollman, Lushington & Olds 2010, *Behav Res Methods* 42(3):754-758 | `AB` | The only PVT reliability estimate in an adolescent sample and in a real classroom rather than a laboratory. Included despite abstract-only access because every other reliability record is in adults. |
| 8 | 32539487 | 10.1080/13803395.2020.1773765 | Basner et al. 2020, *J Clin Exp Neuropsychol* 42(5):516-529 | `FT` | Settles the practice-effect question quantitatively across 15 administrations in the same 46 people, and **partially contradicts** the Dinges-group claim that the PVT is practice-free: speed β = 0.02 (SE 0.03, P = 0.44, genuinely null) but accuracy β = 0.09 (SE 0.04, P = 0.02, small but real). Directly determines the run-in requirement. |

### Part A4 — trait-like individual differences (the justification for n-of-1)

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 9 | 15164894 | 10.1093/sleep/27.3.423 | Van Dongen, Baynard, Maislin & Dinges 2004, *Sleep* 27(3):423-433 | `FT` | The named target. PVT lapse ICC 0.675, and 0.675–0.922 across 13 measures over two identical 36-h exposures. I reconstructed all of Table 2 and verified every ICC by recomputing it from the published variance components; all 13 matched to ±0.003. Also supplies a directly measured within-person between-session SD (σ_ws = √138 = 11.75 lapses per 20-min PVT). |
| 10 | 22851812 | 10.5665/sleep.2010 | Rupp, Wesensten & Balkin 2012, *Sleep* 35(8):1163-1172 | `FT` | Cross-paradigm replication: PVT lapse ICC 0.89, PVT speed ICC 0.86. Table 3 reconstructed and ICCs verified against the published variance components. |
| 11 | 31784748 | 10.1093/sleep/zsz292 | Yamazaki & Goel 2020, *Sleep* 43(6):zsz292 | `FT` | Largest sample in this literature (n = 83) and the only one testing demographic moderators; ICCs 0.78–0.91, unaffected by sex, race, age, BMI, season or sleep-loss order. |
| 12 | 29097703 | 10.1038/s41598-017-14006-7 | Dennis, Wohl, Selame & Goel 2017, *Sci Rep* 7(1):14889 | `AB` | Shows the trait ICCs (0.72–0.92) persist over follow-ups of up to 8.4 years. Answers the "is this stable enough to be worth measuring once?" question. |

### Part A5 — where to get a validated PVT

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 13 | 23709163 | 10.3758/s13428-013-0339-9 | Khitrov et al. 2014, *Behav Res Methods* 46(1):140-147 | `AB` | PC-PVT: a freely distributed, validated PVT for standard PC hardware, with published millisecond-timing validation. The practical answer to "where do I actually get one". |
| 14 | 29679703 | 10.1016/j.jneumeth.2018.04.007 | Reifman et al. 2018, *J Neurosci Methods* | `AB` | PC-PVT 2.0, the current version, adding analysis, prediction and visualisation. The recommended implementation. |
| 15 | 27325169 | 10.3758/s13428-016-0763-8 | Grant, Honn, Layton, Riedy & Van Dongen 2017, *Behav Res Methods* | `AB` | The only record reporting an actual correlation between a 3-min app-based PVT and a 10-min laptop PVT — the statistic the PVT-B paper does not report. Included with a hardware-latency warning. |

### Part B6 — the subjective/objective dissociation

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 16 | 12683469 | 10.1093/sleep/26.2.117 | Van Dongen, Maislin, Mullington & Dinges 2003, *Sleep* 26(2):117-126 | `FT` | The primary source for the whole "you cannot tell how impaired you are" claim, in its strongest form: two curvature parameters estimated in the *same* people on the *same* days — PVT lapses θ = 0.78 ± 0.04 (near-linear accumulation) vs Stanford Sleepiness Scale θ = 0.24 ± 0.04 (plateau) — with the no-ceiling argument made explicitly by the authors (SSS θ = 0.86 ± 0.14 under total deprivation). Also the critical wake duration ξ = 15.84 ± 0.73 h that linearises dose in the power calculation. Deliberately restricted to the dissociation and sleep-need parameters to avoid double-counting with shards s01 and s06; de-duplicate on `cohort_family: UPenn_Dinges_dose_response_2003`. |
| 17 | 21564364 | 10.1111/j.1365-2869.2011.00924.x | Zhou et al. 2012, *J Sleep Res* — mismatch between subjective alertness and objective performance is greatest during the biological night | `AB` | Direct evidence that sleep-restricted people *underestimate* their own impairment, using within-person z-standardised PVT and VAS scores, worst during the biological night. Exactly the sub-claim the brief asked for. |

### Part B7 — can the subject detect his own recovery?

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 18 | 23941878 | 10.1152/ajpendo.00301.2013 | Pejovic et al. 2013, *Am J Physiol Endocrinol Metab* 305(7):E890-E896 | `FT` | The single most decision-relevant record in the shard. Subjective sleepiness, MSLT and PVT measured in the same 30 young adults (mean age 24.7) at the same three time points, under a **2 h/night** restriction that matches the intended manipulation. After 2 nights of 10 h TIB: SSS *better* than baseline (P = 0.04), MSLT 2.50 min *longer* than baseline (P < 0.01), PVT lapses *still worse* than baseline (P = 0.04) with no improvement from restriction (P = 0.69). Also the primary Δ calibration anchor. **Reporting discrepancy recorded as reality: the Results text calls three PVT contrasts "significant" where Table 3 gives P = 0.08, 0.07 and 0.03; I extracted the table values.** |
| 19 | 12603781 | 10.1046/j.1365-2869.2003.00337.x | Belenky et al. 2003, *J Sleep Res* | `AB` | Independent confirmation that PVT deficits from mild-to-moderate restriction do not resolve over three nights of 8 h sleep. Establishes that short washouts are insufficient. |
| 20 | 20815182 | 10.1093/sleep/33.8.1013 | Banks, Van Dongen, Maislin & Dinges 2010, *Sleep* 33(8):1013-1026 | `AB` | Recovery is exponential/saturating and incomplete even after one night of 10 h TIB. Third independent line on the washout requirement. |
| 21 | 20371466 | 10.1126/scitranslmed.3000458 | Cohen et al. 2010, *Sci Transl Med* — uncovering residual effects of chronic sleep loss | `FT` | Early-in-day performance can look recovered after chronic restriction while later-in-day performance is severely impaired. Directly motivates evening-weighted PVT timing. **Used directionally only:** I explicitly declined to put its forced-desynchrony effect sizes into the power calculation, because that exposure is nothing like a 1–2 h nightly contrast and doing so would have put false precision on the result. |

### Part C8 — n-of-1 design and analysis

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 22 | 25976398 | 10.1136/bmj.h1738 | Vohra et al. 2015, CENT statement, *BMJ* 350:h1738 | `FT` | The named target. Supplies the definitions (period, block/pair, sequence, washout, run-in) and the 14 of 25 checklist items where CENT adds n-of-1-specific guidance — notably items 8a–8c (randomised period order, full intended sequence pre-specified), item 12c (carryover, period effects and intra-subject correlation are **mandatory** analysis targets) and item 6a.1 (outcome measurement properties must be reported, which is why the ICC/σ_w work is part of the protocol rather than background). Retrieved via a Wayback snapshot after direct publisher fetches returned HTML. **Limitation recorded: CENT is a reporting guideline and contains no sample-size formulae.** |
| 23 | 28882093 | 10.1177/0962280217726801 | Senn 2019, *Stat Methods Med Res* 28(2):372-383 | `AB` | The statistical companion to CENT. Names the five sample-size planning criteria and, critically, the two variance components a power calculation needs: within-cycle within-patient variation and treatment-by-patient interaction. |
| 24 | 33709907 | 10.3310/hta25160 | Herrett et al. 2021, StatinWISE, *Health Technol Assess* | `FT` | A real, rigorous, fully reported series of 200 n-of-1 RCTs, included **for method only** (the statin content is irrelevant here). Gives the reality anchor — six 2-month periods with 7 daily measurements each reached only **55–70% individual-level power**, and they had a blinded placebo — the power lever (more measurements within period), and the exact analysis model (linear mixed model, AR(1) residuals within period, robust SEs) that protocol_basis.md adopts. |

### Part C9 — how many nights of actigraphy

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 25 | 17580601 | 10.1093/sleep/30.6.793 | Knutson, Rathouz, Yan, Liu & Lauderdale 2007, CARDIA, *Sleep* 30(6):793-796 | `FT` | The record that turns the night-count question into a calculation rather than a convention. Supplies the variance components (between-subject SD 0.70 h, within-subject daily SD 1.26 h, within-subject yearly SD 0.39 h) from which I derived the single-night ICC (0.236), the Spearman-Brown counts (8/13/30 nights for R = 0.70/0.80/0.90) and the precision-based counts (7/15/26/58 nights for SEM ≤ 30/20/15/10 min). |
| 26 | 9989370 | 10.1093/sleep/22.1.95 | Acebo et al. 1999, *Sleep* 22(1):95-103 | `AB` | The age-appropriate night-count recommendation (5+ nights generally, 7+ for sleep duration specifically) in children and adolescents, plus the up-to-28% data-loss figure that motivates oversampling. |
| 27 | 27707448 | 10.5664/jcsm.6384 | Aili, Åström-Paulsson, Stoetzer, Svartengren & Hillert 2017, *J Clin Sleep Med* | `FT` | Independent night-count recommendation in working adults (>7 nights for reliable total sleep time), the 38-minute weekend–weekday sleep-duration difference, and low actigraphy-vs-subjective-quality correlations. Retrieved by fetching the rendered PMC HTML with a custom flattener (`pmchtml.py`) after direct PDF fetches returned HTML. |
| 28 | 29991437 | 10.5664/jcsm.7230 | Smith et al. 2018, AASM actigraphy clinical practice guideline, *J Clin Sleep Med* | `FT` | Included as the guideline the report will be asked about, **and to disqualify its headline number**: the 72-hour minimum is driven by the CPT billing code, not by reliability, and the guideline explicitly excludes healthy normal sleepers. Its own upper figure is 14 consecutive days. Tier TX, context only. |

### Part C10 — the ad-libitum sleep protocol

| # | PMID | DOI | Study | Access | Reason |
|---|---|---|---|---|---|
| 29 | 27775095 | 10.1038/srep35812 | Kitamura et al. 2016, *Sci Rep* 6:35812 | `FT` | The primary Part C10 record, and the only retrieved protocol that actually reaches a sleep asymptote: 9 nights at 12 h TIB in 15 men aged 20–26. OSD 8.41 ± 0.18 h (range 7.29–9.26), potential sleep debt 1.04 ± 0.24 h, **4 days to discharge 1 h of debt**, first-night rebound +3.22 h correlating r = 0.769 with the 9-day-derived debt, and debt correlating r = 0.052 with subjective sleepiness versus r = −0.486 with objective. Supplies both the ad-lib protocol and the washout requirement. Also flags a printed typo (`r = 119` for an MWT correlation) which I recorded rather than silently corrected. |
| 30 | 16295210 | 10.1093/sleep/28.10.1253 | Klerman & Dijk 2005, *Sleep* 28(10):1253-1259 | `FT` | The negative control for protocol duration: a **16 h** daily sleep opportunity (12 h nocturnal + 4 h midday) for only 3 days left sleep still at 10.2 h on day 3 with no asymptote reached. This is the evidence that a 3-day ad-lib probe is not enough, and why section 10 of protocol_basis.md specifies 9 nights. |
| 31 | 29325109 | 10.1093/sleep/zsy011 | Short, Weber, Reynolds, Coussens & Carskadon 2018, *Sleep* 41(4):zsy011 | `AB` | The **only `exact_16_19` population match in the shard** (n = 34, ages 15–17) and the adolescent replication of Van Dongen 2003's method: sleep need ~9.0 h from 10 h TIB opportunities and 9.35 h from PVT lapse dose-response modelling. Sets the extension-arm target and shows adolescents need ~0.9–1.2 h more than adults. Included despite abstract-only access because nothing else in the shard is the right age. |

---

## EXCLUDED (13)

| # | PMID | DOI | Study | Reason for exclusion |
|---|---|---|---|---|
| 32 | 20438143 | 10.1037/a0018883 | Lim & Dinges 2010, *Psychol Bull* 136(3):375-389 — meta-analysis of short-term sleep deprivation on cognitive variables | Out of scope. This is the cognition dose-response effect size, which belongs to shard s01; recording it here would create a double-counted effect in the downstream pool. It contains no psychometric parameter (reliability, within-person σ, practice slope), which is my remit. |
| 33 | none resolvable | none resolvable | Dorrian, Rogers & Dinges 2005, "Psychomotor vigilance performance: neurocognitive assay sensitive to sleep loss", book chapter in *Sleep Deprivation: Clinical Issues, Pharmacology and Sleep Loss Effects* | **The most consequential exclusion in the shard.** This is the origin of the claim that PVT test-retest ICCs are "above 0.8" for lapses — restated verbatim in *both* Basner 2011 papers. Multiple structured PubMed searches on author + title terms returned zero hits, consistent with an unindexed edited-volume chapter. I could not retrieve it and could not resolve an identifier, so **I did not record the >0.8 figure anywhere**, and the ICCs I did retrieve (0.51, 0.69, 0.79, 0.83) are all lower. Excluded rather than marked `secondhand` because propagating an unverifiable reliability figure into a power calculation is precisely the failure the instructions forbid. |
| 34 | 15018277 | none in record | Van Dongen, Maislin & Dinges 2004, *Aviat Space Environ Med* 75(3 Suppl):A147-54 | **Folded in, not separately recorded.** Same dataset and same subjects as record #9 with a slightly different ICC computation (PVT ICC 0.69 vs 0.675). A separate record would double-count a correlated effect. Its numbers are quoted inside `vandongen2004_traitlike.yaml`. |
| 35 | — | 10.1136/bmj.h1793 | Vohra et al. 2015, CENT Explanation & Elaboration, *BMJ* 350:h1793 | **Unretrievable.** Open access, but every Wayback snapshot I could fetch truncated at exactly 1 MiB and failed to parse in pdfminer. The CENT statement itself (#22) carries the checklist items the protocol needs, so nothing load-bearing was lost. |
| 36 | 32107202 | 10.1136/bmj.m122 | Porcino et al. 2020, SPENT 2019 (SPIRIT extension for n-of-1 trials), *BMJ* 368:m122 | Redundant with CENT for this purpose. SPENT governs *protocol* reporting rather than design or analysis, and likewise contains no sample-size methodology. Logged so the report can cite it for pre-registration wording if wanted. |
| 37 | 27473269 | 10.1186/s13063-016-1499-6 | Punja et al. 2016, MYNAP n-of-1 trial protocol, *Trials* | A study protocol for melatonin in stimulant-treated ADHD. Neither population nor outcome transfers, and StatinWISE (#24) is a strictly better methodological exemplar because it reports completed results, achieved individual power and the analysis model. |
| 38 | 8238456 | 10.1152/ajpregu.1993.265.4.R846 | Wehr et al. 1993, *Am J Physiol* — conservation of photoperiod-responsive mechanisms in humans | **Secondhand only.** Klerman & Dijk cite an 8.2 h asymptote from this work, but the design is a 14 h extended-dark photoperiod manipulation, not an ad-libitum sleep-opportunity protocol, so the protocol details do not transfer. The 8.2 h figure appears only as an explicitly-labelled secondhand quotation inside `klerman2005_adlib_sleep_need.yaml`. |
| 39 | not resolved | not resolved | Rajaratnam et al., 16 h sleep opportunity, asymptote 8.7 h (cited by Klerman & Dijk) | **Identifier not resolvable.** `Rajaratnam SM[au] AND sleep extension AND 16-h` returned 0 hits and I could not confirm which record was being cited. No identifier assigned; the 8.7 h figure is retained only as an explicitly-labelled secondhand quotation. |
| 40 | 34854507 | 10.1111/jsr.13521 | Arsintescu et al. 2022, *J Sleep Res* 31(3):e13521 — early starts and late finishes in short-haul pilots | Attractive because it is one of the very few free-living **daily-PVT** datasets, but the exposure is shift timing rather than a sleep-duration contrast, and neither a within-person σ nor a day-to-day autocorrelation is reported in extractable form. **This is the gap that forced the ×1.5 field-inflation assumption in protocol_basis.md §2 and the assumed ρ in §5.** |
| 41 | 32838580 | 10.1080/07420528.2020.1804924 | Arsintescu et al. 2020, *Chronobiol Int* 37(9-10):1492-1494 — workload, performance and fatigue in a short-haul airline | Same reason as #40: operational exposure, no extractable within-person variance parameter. |
| 42 | 31449253 | 10.3791/59851 | Arsintescu et al. 2019, *J Vis Exp* — collecting sleep, circadian, fatigue and performance data in complex operational environments | A methods-video protocol paper. No quantitative reliability or variance parameters. |
| 43 | 27868260 | 10.1111/jsr.12473 | Agostini et al. 2017, *J Sleep Res* 26(2) — adolescent sleep restriction during a simulated school week | Right age group and right exposure, but the reported outcomes are circadian phase and subjective measures rather than the PVT psychometric parameters this shard needs. Short 2018 (#31) is the same research lineage and answers the sleep-need question directly. **Flagged for shards s01/s06, which may want it.** |
| 44 | 26851466 | 10.1016/j.apergo.2015.12.004 | Short et al. 2016, *Appl Ergon* — split sleep schedules (6h-on/6h-off) | A split-sleep (biphasic) manipulation, not a monophasic TIB-duration contrast, so neither the effect size nor the σ transfers to the intended protocol. |

---

## Identifier verification outcomes

| Attempted | Outcome |
|---|---|
| All 31 included records | **All VERIFIED.** Every record carries `crossref_ok` and/or `pubmed_ok` reflecting what the API actually returned, and `resolved_title` holds the title as returned rather than as expected. One title resolved shorter than the citation string and was kept as returned: Crossref gives Basner & Rubinstein 2011 as simply "Fitness for Duty", so that record carries `title_similarity: 0.9`. |
| Dorrian, Rogers & Dinges 2005 (#33) | **No DOI or PMID resolvable.** Excluded; the ">0.8 ICC" claim it is the source of was not propagated anywhere. |
| Rajaratnam et al. 16 h protocol (#39) | **Not resolved.** No identifier assigned; figure retained only as labelled secondhand. |
| Full text of 10.1093/sleep/zsy011 (#31) | Identifier verified; **full text not retrievable.** Unpaywall reports bronze OA but the only location is the OUP PDF endpoint, which returns HTML to non-browser clients. No PMC deposit (`elink` returns no `pmc` linkset) and no Wayback snapshot (CDX query returned an empty set). Recorded `abstract_only`. |
| Full text of 10.1136/bmj.h1793 (#35) | Identifier verified; every retrievable snapshot truncated at exactly 1 MiB and failed to parse. Excluded. |

**No identifier written into any YAML record failed verification, and no number in any record lacks a
verbatim supporting quotation in its `quote` or `notes` field.**

## Retrieval methods used, for reproducibility

Direct publisher fetches were frequently blocked (Cloudflare interstitials and HTML returned in place of
PDFs). The working routes, in the order I ended up preferring them, were: Europe PMC REST and its direct
PDF endpoints; the NCBI BioC API for full-text XML (parsed with the local `bioc.py`); rendered PMC HTML
flattened with the local `pmchtml.py` (this is the only route that works for non-OA PMC deposits);
institution-hosted author PDFs; and the Wayback Machine CDX API for publisher PDFs. `verify.sh` wraps the
Crossref, PubMed esummary and PubMed esearch calls used for identifier verification.
