# Screening log — shard `s04_academic_natural_experiments`

Domain: Tier-2 quasi-experimental and instrumental-variable evidence on sleep → academic and
cognitive outcomes in adolescents and college students (target age 16–19).

**Records screened: 58. Included: 21. Excluded: 37.**

Every identifier listed below was actually retrieved during this session (Crossref `/works`,
Crossref bibliographic search, or PubMed E-utilities). Identifiers marked **FAILED** did not
resolve to the intended paper and were corrected or dropped — see the "Identifier failures"
section at the end.

## Included (21 records written as YAML)

| # | Identifier | Study | Design / tier | Decision & reason |
|---|---|---|---|---|
| 1 | `10.1257/pol.3.3.62` | Carrell, Maghakian & West 2011, AEJ:EP | quasi-experiment / T2 | **INCLUDE.** Best internal validity in the start-time literature (random section assignment + two administrative bell changes at USAFA). Age 17–22, exact match. No sleep first stage. |
| 2 | `10.1016/j.econedurev.2012.07.006` | Edwards 2012, Econ Educ Rev | quasi-experiment / T2 | **INCLUDE.** Bus-schedule-driven start-time variation, school and student-school FE, n≈100k. Grade-10 persistence result is age-relevant. Sleep not measured. |
| 3 | `10.3368/jhr.53.4.0815-7346r1` | Heissel & Norris 2018, J Human Resources | IV / T2 | **INCLUDE.** Time-zone-boundary IV for sunlight before school; the only study establishing that the effect is puberty-specific. Sleep not measured. |
| 4 | `10.1162/edfp_a_00045` | Hinrichs 2011, Educ Finance Policy | quasi-experiment / T2 | **INCLUDE.** The literature's main *precise null* (95% CI −0.051 to +0.041 SD). Essential to avoid an upward-biased pool. |
| 5 | `10.1126/sciadv.aau6200` / PMID 30547089 | Dunster et al. 2018, Science Advances | quasi-experiment / T2 | **INCLUDE for the first stage only.** Actigraphy: +34 min sleep from a 55-min delay. Grade outcome is an uncontrolled pre/post cohort comparison (RoB high). |
| 6 | `10.1016/j.econedurev.2019.05.011` | Groen & Pabilonia 2019, Econ Educ Rev | quasi-experiment / T2 | **INCLUDE — highest-value record.** Only study measuring BOTH the sleep first stage (time diaries, +36 min/h) and test scores in the same nationally representative high-school sample. |
| 7 | `10.5664/jcsm.6358` / PMID 27855730 | Morgenthaler et al. 2016, JCSM | meta-analysis (observational) / T2 | **INCLUDE for the pooled first stage.** +18.65 min (≤60-min delay), +52.56 min (>60-min delay). Also documents 9-month decay of the sleep gain. |
| 8 | `10.15185/izawol.181` | Shapiro 2015, IZA World of Labor | narrative synthesis / TX | **INCLUDE as context only.** Field consensus value (~0.10 SD per hour of bell time) and policy benchmark. Not an independent estimate; author COI noted. |
| 9 | `10.1016/j.jhealeco.2019.03.007` | Giuntella & Mazzonna 2019, J Health Econ | IV / T2 | **INCLUDE.** Canonical US time-zone-border sunset RD; first stage −19 min. Adults 18–55; cognitive outcome is a self-report impairment dummy. |
| 10 | `10.1007/s13524-017-0609-8` | Giuntella, Han & Mazzonna 2017, Demography | IV / T2 | **INCLUDE.** Sunset IV in China; 0.4–0.6 SD cognition per hour of sleep. Age 45+, poor transportability. |
| 11 | `10.1162/rest_a_01201` | Jagnani 2024, ReStat | IV / T2 | **INCLUDE with heavy downweight.** Only sunset-IV study with an academic outcome; first stage −0.47 h/h. Implied ~1.15 SD/h is implausibly large; Indian children 6–16. |
| 12 | `10.1162/rest_a_00746` | Gibson & Shrader 2018, ReStat | IV / T2 | **INCLUDE.** Best-measured sunset first stages (−0.38 h short run, −0.93 h long run) and the long-run:short-run effect ratio of ~4.5×. Outcome is earnings, not achievement. |
| 13 | `10.1016/j.econedurev.2017.07.002` | Herber, Quis & Heineck 2017, Econ Educ Rev | quasi-experiment (RD) / T2 | **INCLUDE.** The best-identified DST/test-score RD; null (≈0.06 SD math, n.s.). Bounds the acute single-night effect. |
| 14 | `10.1037/a0020118` | Gaski & Sagarin 2011, J Neurosci Psychol Econ | quasi-experiment / T2 | **INCLUDE, flagged for exclusion from pooling.** −0.16 SD SAT in DST counties, but county cross-section confounded by Chicago/Louisville commuting ties. Secondhand via Herber et al. |
| 15 | `10.1016/j.jebo.2019.12.003` | Jin & Ziebarth 2020, JEBO | quasi-experiment / T2 | **INCLUDE.** DST "fall back" event study; extra sleep for the sleep-deprived reduces hospital admissions for 4 days. Health outcome, one-night exposure. |
| 16 | `10.1038/s41539-019-0055-z` / PMID 31583118 | Okano et al. 2019, npj Sci Learn | prospective cohort, objective / **T4 not T2** | **INCLUDE, retiered.** Task listed it as a natural experiment; it has no exogenous variation. Best age match in the shard (88 MIT freshmen, mean 18.19). |
| 17 | `10.1073/pnas.2209123120` / PMID 36780521 | Creswell et al. 2023, PNAS | prospective cohort, objective / T4 | **INCLUDE.** +0.07 GPA per hour of nightly sleep controlling for previous-term GPA; five samples, three universities. The headline GPA-per-hour number. |
| 18 | `10.5665/sleep.5552` / PMID 26612392 | Lo et al. 2016, Sleep (Need for Sleep Study) | RCT parallel / T1 | **INCLUDE — the T1 anchor.** Randomized 5 h vs 9 h TIB × 7 nights in 15–19-year-olds. Cohen f² 0.20–1.48. Incomplete recovery after 2× 9 h nights. |
| 19 | `10.5665/sleep.6092` / PMID 27253768 | Huang et al. 2016, Sleep (same NFS sample) | RCT parallel / T1 | **INCLUDE, de-duplicate against #18.** Same 56 randomized adolescents. Only randomized *academic* learning outcome: restriction destroyed crammed but not spaced vocabulary recall. Abstract only. |
| 20 | `10.1093/qje/qjab013` | Bessone et al. 2021, QJE | RCT parallel / T1 | **INCLUDE as counter-evidence.** Randomized +27 min night sleep → −0.01 SD (SE 0.04) on the overall index; naps → +0.12 SD. Chennai adults, poor age match. |
| 21 | `10.1016/j.sleep.2013.01.012` / PMID 23523432 | Dewald-Kaufmann, Oort & Meijer 2013, Sleep Med | RCT parallel / T1 | **INCLUDE.** The only randomized sleep-*extension* trial in already-sleep-restricted adolescents with a cognitive outcome. n=55, 85.5% female, selective reporting concern. Abstract only. |

## Excluded

### Duplicate / superseded versions of included studies (merged, not double-counted)

| # | Identifier | Record | Reason |
|---|---|---|---|
| 22 | `10.2139/ssrn.1628693` | Edwards, "Early to Rise" SSRN WP | Superseded by published #2. |
| 23 | `10.2139/ssrn.2674256` | Heissel & Norris SSRN WP (13 Apr 2017) | Used as the full-text source for #3; not counted separately. |
| 24 | `10.2139/ssrn.2742562` | Giuntella, Han & Mazzonna SSRN WP | Superseded by published #10. |
| 25 | IZA DP No. 9774 | Giuntella, Han & Mazzonna WP | Full-text source for #10; not counted separately. |
| 26 | `10.2139/ssrn.2615252` (= IZA DP 9088) | "Does Daylight Saving Time Really Make Us Sick?" | Earlier version of #15. |
| 27 | HEDG WP 15/27 (Univ. of York) | Jin & Ziebarth WP | Full-text source for #15. |
| 28 | BLS Working Paper 484 (Oct 2015) | Groen & Pabilonia WP | Full-text source for #6. |
| 29 | Monthly Labor Review summary | Groen & Pabilonia | Summary of #6. |
| 30 | Williams College WP 2015-17 | Gibson & Shrader | Full-text source for #12; note WP IV values (1.5%/4.9%) differ slightly from published (1.1%/5%). |
| 31 | Jagnani WP (2018) | Jagnani | Superseded by published #11. |
| 32 | EIEF/Oxford WP (25 Aug 2016) | Giuntella & Mazzonna | Full-text source for #9. |

### Wrong outcome domain (sleep measured, but no academic or cognitive outcome)

| # | Identifier | Record | Reason |
|---|---|---|---|
| 33 | `10.3109/03014460.2014.897756` | "Does the transition into DST really cause partial sleep deprivation?" Ann Hum Biol 2014 | Measures sleep only; no test score or cognitive outcome. |
| 34 | `10.1080/15402002.2014.963584` | "Start Later, Sleep Later: homeschool vs public/private" Behav Sleep Med | Cross-sectional sleep comparison, no academic outcome. |
| 35 | `10.2139/ssrn.3648795` | "Immigration Policy and Immigrants' Sleep: Evidence from DACA" | Sleep outcome only. |
| 36 | PMID 24252173 | Dewald-Kaufmann et al. 2014, J Child Psychol Psychiatry | Sleep extension → depressive symptoms. Psychiatric outcome, out of this shard's domain (relevant to a psychiatric shard). |
| 37 | `10.5664/jcsm.4194` | "High School Start Times and Death on the Road" JCSM | Editorial; outcome is road deaths. |
| 38 | `10.1037/e592972009-001` | "Saving Daylight, Increasing Danger" (PsycEXTRA) | Grey/dataset record; injury outcome. |
| 39 | `10.1037/e518362013-186` | "Saving Daylight, Losing Motivation: DST and Workplace Loafing" (PsycEXTRA) | Grey record; workplace loafing outcome. |
| 40 | `10.2139/ssrn.6432996` | "Do Analysts Herd More under Sleep Loss? Evidence from DST" | Financial-analyst behaviour, out of domain. |
| 41 | ScienceDirect PII S1570677X15000726 | "An empirical analysis of the demand for sleep: Evidence from ATUS", Econ Hum Biol | Models the *demand* for sleep; no cognitive/academic outcome. DOI not separately verified, so not cited anywhere. |

### Wrong construct, wrong tier, or no extractable effect

| # | Identifier | Record | Reason |
|---|---|---|---|
| 42 | `10.5664/jcsm.6288` | AASM Consensus Statement on Recommended Amount of Sleep | Guideline (TX). Belongs to a sleep-need/normative shard, not a causal-identification shard. |
| 43 | `10.1016/j.sleep.2022.05.498` | Conference abstract, school start times & social jetlag (NZ) | Meeting abstract; no extractable effect estimate. |
| 44 | `10.31234/osf.io/37svc` | "How is Daylight Saving Time still a thing?" (preprint) | Preprint; no test-score outcome. |
| 45 | `10.31235/osf.io/a4j3v` | "Academic achievement gaps by migration background at school starting age in Ireland" | School starting **age**, not start **time**. Search-term collision. |
| 46 | `10.2139/ssrn.2790193` | "School Starting Age, Family Background, and Academic Achievement: Urban China" | School starting age. Collision. |
| 47 | `10.2139/ssrn.2880446` | "School Starting Age and Academic Achievement: China's Junior High Schools" | School starting age. Collision. |
| 48 | `10.1162/rest.90.2.347` | "Why Doesn't Capital Flow from Rich to Poor Countries?" | Crossref search noise. |
| 49 | `10.2307/1928707` | "The Production of Human Capital Over Time" | Crossref search noise. |
| 50 | `10.2307/2109594` | "Entrepreneur Human Capital Inputs and Small Business Longevity" | Crossref search noise. |
| 51 | PMID 42417457 | Cognitive stimulation + physical activity to delay aging-related decline (protocol) | Off topic; protocol only. |
| 52 | PMID 41832477 | Postpartum lifestyle intervention, prior GDM | Off topic. |
| 53 | PMID 39883906 | Ocrelizumab in relapsing MS (OPERA) | Off topic. |
| 54 | PMID 39693261 | Physical therapy timing in subacute mild TBI | Off topic. |
| 55 | PMID 39300465 | TISA pragmatic RCT in a humanitarian setting | Off topic. |
| 56 | PMID 39138502 | ReISE supported work placements | Off topic. |
| 57 | — | Hafner / RAND economic analyses of later school start times | **SOUGHT BUT NOT INCLUDED.** The task named these. RAND's work in this area is a cost–benefit / macroeconomic simulation that *takes* effect sizes from the studies above (chiefly Carrell and Edwards) as inputs and monetizes them. It contains no independent identification strategy and no new first stage, so including it would double-count studies #1 and #2 while adding a modelling layer. Excluded by rule 5 of the extraction instructions (prefer primary studies inside reviews). |
| 58 | — | Randomized trial of sleep extension in **college students** with a **GPA** outcome | **DOES NOT APPEAR TO EXIST.** Searched PubMed for sleep extension × adolescents/college × academic performance; the extension trials that exist (#20, #21) have cognitive or economic outcomes, small samples, or non-student adult populations. This is the single biggest gap in the domain — see `station_report.md`. |

## Identifier failures (all corrected or dropped; none written into a record)

| Guessed identifier | What it actually resolved to | Resolution |
|---|---|---|
| `10.3368/jhr.54.4.0815.7346R1` | Did not resolve (Crossref 404) | Corrected via Crossref title search to `10.3368/jhr.53.4.0815-7346r1` (JHR **53**(4):957–992, not 54). |
| `10.1016/j.econedurev.2012.06.002` | "Family background, self-confidence and economic outcomes" — a *different* Econ Educ Rev article | Corrected to `10.1016/j.econedurev.2012.07.006`. |
| `10.1162/EDFP_a_00034` | "What Do AEFA Members Say? Summary of Results of an Education Finance and Policy Survey" | Corrected to `10.1162/edfp_a_00045`. |
| `10.1007/s13524-017-0603-1` | "Neighborhoods, Schools, and Academic Achievement: A Formal Mediation Analysis" — a different Demography article | Corrected to `10.1007/s13524-017-0609-8`. |
| `10.5664/jcsm.6288` | AASM Consensus Statement on recommended sleep amounts, not the start-time review | Corrected to `10.5664/jcsm.6358` (PMID 27855730). |
| `10.1080/00036846.2017.1290787` (Applied Economics) | Did not resolve | The Herber/Quis/Heineck DST paper is in **Economics of Education Review**: `10.1016/j.econedurev.2017.07.002`. |
| `https://www.bls.gov/osmr/research-papers/2015/pdf/ec150060.pdf` | HTTP 500 | Groen & Pabilonia obtained from the BLS WP 484 mirror plus the published supplementary tables. |
| `https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/` | HTTP 301 | Switched to `https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/`. |

**Zero fabricated identifiers survive into any record.** All 21 DOIs were re-checked against Crossref
in a final sweep (all HTTP 200, all resolved titles matching), and all 7 PMIDs were re-checked against
PubMed E-utilities. Three DOIs (`10.5665/sleep.5552`, `10.5665/sleep.6092`,
`10.1016/j.sleep.2013.01.012`) originated from PubMed records and were subsequently confirmed against
Crossref, so every included record carries `verification.status: VERIFIED` with both
`crossref_ok: true` and, where a PMID exists, `pubmed_ok: true`.
