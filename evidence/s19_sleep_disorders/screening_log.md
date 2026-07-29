# Screening log — shard `s19_sleep_disorders`

Every candidate record considered, with its identifier, decision and reason. **62 records screened, 35
included, 27 excluded.** Every identifier below was resolved programmatically against the PubMed E-utilities
`esummary` endpoint and/or the Crossref works API before being written here; none is recalled from memory.

Search strategy: PubMed E-utilities (`esearch` + `esummary` + `efetch`) across seven topic blocks —
(1) DSWPD/delayed sleep phase prevalence, (2) BIISS/insufficient sleep syndrome, (3) insomnia prevalence,
(4) OSA prevalence in young/lean males, (5) screening instruments (ESS, ISI, MCTQ, CSRQ), (6) AASM
guidelines (circadian treatment, actigraphy), (7) consumer wearable validity. Full text obtained via
Unpaywall → Europe PMC / PMC → publisher (PLOS XML, Wiley OA) → institutional repository, with
`pdfminer.six` for PDF-only sources.

Note on tiering: almost everything in this domain is `TX` (cross-sectional, normative or guideline). That is
inherent to the questions asked — prevalence, diagnostic criteria and instrument cut-offs are not
randomisable. The three exceptions are flagged below.

---

## Included (35)

### Block 1 — DSWPD and delayed chronotype prevalence

| # | Identifier | Study | Why included |
|---|---|---|---|
| 1 | PMID 24330358 | Sivertsen 2013, *BMC Public Health* | DSPS prevalence in n≈9,338 Norwegian adolescents **aged exactly 16-19**; also the only source giving a directly measured LR+ for oversleeping (5.52) |
| 2 | PMID 22153780 | Saxvig 2012, *Sleep Med* | Separates delayed phase **trait** (8.4%) from delayed phase **with impairment** (5.7%) in 16-19 y — the trait/disorder distinction my whole analysis turns on |
| 3 | PMID 33097403 | Sivertsen 2021, *Sleep Med* | DSWPD by self-reported **ICSD-3** criteria in Norwegian university students; supplies the male-specific figure (4.7%) |
| 4 | PMID 27537980 | Danielsson 2016, *Chronobiol Int* | DSPD by **DSM-5** criteria, ages 16-26, Sweden — independent country and criteria set |
| 5 | PMID 37275982 | Futenma 2023, *Front Psychiatry* | DSWPD alongside hypersomnolence; helps bound the differential |
| 6 | PMID 41371273 | **Jääkallio 2026**, *Pediatrics* | **T4.** The only prospective source: DSP **70% stable** over 19 months from mean age 16.8; and behavioural rather than physiological predictors. Answers "will he grow out of it?" |
| 7 | PMID 40129277 | **Dama 2025**, *Can J Psychiatry* | Most recent systematic review confined to DSWPD in young people; pooled depression association d=0.92, plus the 0.13-0.17% general-population vs 3.3-17.9% young-person contrast |

### Block 2 — BIISS

| # | Identifier | Study | Why included |
|---|---|---|---|
| 8 | PMID 36337802 | Mader 2022, *Cureus* | **ICSD-3 BIISS criteria A-F verbatim** — the task's explicit requirement, plus the ICSD-3 "preferably at least two weeks" actigraphy statement |
| 9 | PMID 30789063 | Williams 2020, *Behav Sleep Med* | BIISS (9.9%) **and** insomnia (22.1%) in the same US college sample |
| 10 | PMID 20303581 | Pallesen 2011, *J Adolesc* | BIISS 10.4% in Norwegian 16-19 y — independent replication of Williams to within 0.5 pp |

### Block 3 — Insomnia prevalence

| # | Identifier | Study | Why included |
|---|---|---|---|
| 11 | PMID 23611716 | Hysing 2013, *J Sleep Res* | DSM-5 insomnia in 16-19 y Norwegians; also the 65%-exceed-30-min latency figure that kills the conventional SOL threshold |
| 12 | PMID 30515935 | Sivertsen 2019, *J Sleep Res* | DSM-5 insomnia in students, male-specific (22.2%) |
| 13 | PMID 16452333 | Johnson 2006, *Pediatrics* | The Pediatrics paper named in the task. **Diagnostic-interview** based (10.7% lifetime), methodologically strongest and lowest |
| 14 | PMID 12531146 | Ohayon 2002, *Sleep Med Rev* | Documents the definitional ladder — why estimates vary threefold |
| 15 | PMID 40369835 | **van Straten 2025**, *J Sleep Res* | The recent meta-analysis the task asked for. Interview 12.4% vs self-report 16.3%; ISI≥10 recovers 12.5%. **Also documents that no contributing study had a mean age below 37 y** |

### Block 4 — OSA prevalence

| # | Identifier | Study | Why included |
|---|---|---|---|
| 16 | PMID 23589584 | Peppard 2013, *Am J Epidemiol* | The Wisconsin paper named in the task; supplies **BMI-stratified** male rates, incl. lean men with ESS>10 (2.7%) — my closest anchor for a lean 19-y-old |
| 17 | PMID 31300334 | Benjafield 2019, *Lancet Respir Med* | Named in the task. Included to **document that it is restricted to ages 30-69** and supplies nothing for this age band |
| 18 | PMID 30922948 | Chan 2019, *Chest* | Childhood→young-adult (mean 20.2 y) OSA trajectory |
| 19 | PMID 26846837 | Bixler 2016, *Eur Respir J* | Penn State Child Cohort, **lab PSG**, population-representative adolescents; 100% remission of childhood AHI≥5 |

### Block 5 — Screening instruments

| # | Identifier | Study | Why included |
|---|---|---|---|
| 20 | PMID 1798888 | Johns 1991, *Sleep* | ESS original validation — included specifically to establish that **it contains no cut-off** |
| 21 | PMID 9415943 | Johns & Hocking 1997, *Sleep* | The actual origin of the ESS >10 threshold and the 0-10 normal range |
| 22 | PMID 28449902 | Janssen 2017, *Sleep Med* | ESS-CHAD validation; the developers' own statement that **no adolescent cut-off exists** |
| 23 | PMID 21532953 | Morin 2011, *Sleep* | ISI ≥10 cut-off, sens 86.1%/spec 87.7% → LR+ 7.00 / LR− 0.159 [derived] |
| 24 | PMID 33640841 | **Michaud 2021**, *Sleep Med* | Only ISI validation against a **structured DSM-5 interview (SCID-5)** in **young adults**; gives a lower cut-off (≥8) and the strongest rule-out in the set (<7, LR− 0.057) |
| 25 | PMID 31336976 | Roenneberg 2019, *Biology* | **The MSFsc formula** and the mechanism by which late chronotype under social constraint produces exactly this subject's pattern |
| 26 | PMID 28636610 | Fischer 2017, *PLoS One* | Age- **and sex**-specific mid-sleep norms by single year; peak male lateness at 19.2 y. Nationally representative |
| 27 | PMID 29341314 | Dewald-Kaufmann 2018, *J Sleep Res* | CSRQ — the only instrument here **validated in adolescents**; ROC cut-offs 28/40/51. Also shows it cannot separate insomnia from DSWPD |
| 28 | PMID 29991437 | Smith 2018, *J Clin Sleep Med* | AASM actigraphy clinical practice guideline: 72 h minimum to 14 days |

### Block 6 — Treatment (needed because the recommendation differs by diagnosis)

| # | Identifier | Study | Why included |
|---|---|---|---|
| 29 | PMID 26414986 | Auger 2015, *J Clin Sleep Med* | The AASM intrinsic-CRSWD guideline the task named; melatonin doses/timings and light parameters verbatim |
| 30 | PMID 22131604 | Gradisar 2011 RCT, *Sleep* | **T1.** Doubly load-bearing: supplies the **disease-present distributions** (SOL, TST, weekend gap in diagnosed DSPD) that every LR I derived depends on, *and* the adolescent CBT+bright-light effect (NNT 1.4) |
| 31 | PMID 29912983 | **Sletten 2018**, *PLoS Med* | **T1.** The randomised melatonin trial that post-dates the guideline: 0.5 mg 1 h pre-bedtime, 34 min advance, NNT 3.5, DLMO **not** significantly shifted. Also the only **DLMO-confirmed** DSWPD sample, which supplied the ESS and ISI disease-present distributions |
| 32 | PMID 21257344 | Gradisar 2011 meta, *Sleep Med* | 41 worldwide surveys establishing that the subject's pattern **is the adolescent norm** — the basis for the LR≈1 finding |

### Block 7 — Consumer wearable validity

| # | Identifier | Study | Why included |
|---|---|---|---|
| 33 | PMID 33378539 | Chinoy 2021, *Sleep* | **T1.** Seven devices vs PSG head-to-head with **limits of agreement**; no industry funding; includes a disrupted-sleep night |
| 34 | PMID 39484805 | Lee 2025, *J Clin Sleep Med* | Most recent wearable meta-analysis; pooled TST −16.9 min |
| 35 | PMID 31778122 | **Haghayegh 2019**, *J Med Internet Res* | Stratifies by **device generation**, which reconciles the apparent Chinoy/Lee contradiction; and identifies that current devices significantly **underestimate sleep onset latency** — the variable my analysis leans on hardest |

---

## Excluded (27)

| # | Identifier | Record | Decision | Reason |
|---|---|---|---|---|
| 36 | PMID 38054481 | Delayed sleep wake phase disorder in adolescents: an updated review. *Curr Opin Pediatr* 2024 | EXCLUDE | Narrative review. Contains no primary prevalence data; its sources are the primaries already extracted (#1-4). No quotable original estimate |
| 37 | PMID 34419186 | Circadian rhythm sleep-wake disturbances and depression in young people. *Lancet Psychiatry* 2021 | EXCLUDE | Narrative review, superseded for my purpose by the meta-analysis at #7, which pools the same literature quantitatively |
| 38 | PMID 32358212 | Sleep Disorders in Adolescents. *Pediatrics* 2020 | EXCLUDE | Narrative clinical review; no original estimates with dispersion |
| 39 | PMID 17383934 | Sleep, circadian rhythms, and delayed phase in adolescence. *Sleep Med* 2007 | EXCLUDE | Narrative review, 2007 vintage; superseded by #25/#26 for chronotype and #32 for adolescent norms |
| 40 | PMID 17936039 | Roenneberg, Epidemiology of the human circadian clock. *Sleep Med Rev* 2007 | EXCLUDE | Superseded by the same author's 2019 self-critical review (#25) for the MSFsc formula, and by Fischer 2017 (#26) for age/sex norms in a representative sample |
| 41 | PMID 20113918 | Lund 2010, Sleep patterns in a large population of college students. *J Adolesc Health* | EXCLUDE | Cross-sectional, no disorder-level ascertainment against ICSD/DSM criteria; cannot contribute a prior for any named disorder |
| 42 | PMID 20864434 | Gaultney 2010, Prevalence of sleep disorders in college students. *J Am Coll Health* | EXCLUDE | Reports "**risk for** at least one sleep disorder" (27%) from a screening questionnaire, not diagnosed prevalence, and gives no disorder-specific rates for the four candidates in my partition |
| 43 | PMID 31791166 | The µMCTQ: ultra-short Munich ChronoType Questionnaire. *J Biol Rhythms* 2020 | EXCLUDE | Instrument variant. MSFsc computation already extracted from #25; the ultra-short form would add administration convenience but no new psychometric threshold |
| 44 | PMID 37225252 | External validity of the reduced MEQ for Children and Adolescents: an actigraphic study. *J Sleep Res* 2024 | EXCLUDE | Chronotype **preference** instrument, not a DSWPD diagnostic screener. The MCTQ is preferred because it outputs clock times usable for light/melatonin timing, whereas the MEQ outputs an ordinal preference score |
| 45 | PMID 1027738 | Horne & Östberg 1976, Morningness-eveningness self-assessment questionnaire | EXCLUDE | As above — foundational but ordinal-score output, no diagnostic threshold, and no clock-time output for treatment timing |
| 46 | PMID 18630661 | Morningness-eveningness in adolescents. *Span J Psychol* 2008 | EXCLUDE | MEQ-based, small non-representative sample; Fischer 2017 (#26) supplies far better norms |
| 47 | PMID 40433950 | MEQ reliability/factor structure in Spanish adolescents. *Chronobiol Int* 2025 | EXCLUDE | Translation and factor-structure study; no diagnostic cut-off |
| 48 | PMID 39686205 | Morningness-eveningness preference and motor wake-sleep inertia in adolescents. *Sensors* 2024 | EXCLUDE | Outcome (motor inertia) outside my remit; not a prevalence or instrument-threshold source |
| 49 | PMID 29991438 | AASM actigraphy **systematic review** companion. *J Clin Sleep Med* 2018 | EXCLUDE | Companion evidence review to the guideline already included at #28; same evidence base, would double-count |
| 50 | PMID 18041479 | AASM 2007 practice parameters, circadian rhythm sleep disorders. *Sleep* | EXCLUDE | Superseded by the 2015 guideline (#29), which the task explicitly asked for |
| 51 | PMID 17520797 | AASM practice parameters, actigraphy, 2007 update. *Sleep* | EXCLUDE | Superseded by #28 |
| 52 | PMID 12749556 | AASM practice parameters, actigraphy, 2002 update. *Sleep* | EXCLUDE | Superseded by #28 |
| 53 | PMID 12749557 | The role of actigraphy in the study of sleep and circadian rhythms. *Sleep* 2003 | EXCLUDE | Superseded by #28 |
| 54 | PMID 24144243 | Saxvig 2014 RCT, bright light + melatonin for DSPD. *Chronobiol Int* | EXCLUDE | Genuine near-miss. Excluded because #30 covers the adolescent behavioural+light contrast with a cleaner design and #31 covers melatonin with a larger, DLMO-confirmed, double-blind sample. Would add a third partially-overlapping treatment estimate without changing the recommendation |
| 55 | PMID 24132057 | Companion to #54 — sleepiness and cognitive outcomes. *J Biol Rhythms* 2013 | EXCLUDE | Companion report of the same trial; outcomes outside my remit |
| 56 | PMID 33870175 | Melatonin for DSWPD in children: an overview. *Sleep Med X* 2020 | EXCLUDE | Narrative overview; the underlying paediatric dosing trial is already captured verbatim inside #29 |
| 57 | PMID 1674014 | Dahlitz 1991, Delayed sleep phase syndrome response to melatonin. *Lancet* | EXCLUDE | n very small, 1991, superseded by the randomised trial at #31 |
| 58 | PMID 30132686 | Prolonged-release melatonin for insomnia in autism. *J Child Adolesc Psychopharmacol* 2018 | EXCLUDE | Wrong population (ASD) and wrong indication (insomnia, not DSWPD) |
| 59 | PMID 39879677 | Resistance vs aerobic exercise for DSWPD in **male college students aged 18-28**. *Sleep Med* 2025 | EXCLUDE | Population-exact and therefore tempting, but excluded: 3-day intervention, randomised crossover with no washout described, and the abstract reports only P-values with no effect sizes, SDs or n. Nothing extractable without fabrication. **Flagged as a lead in `station_report.md`** |
| 60 | PMID 32048595 | Basis B1 multisensor wearable vs PSG in healthy young adults. *J Clin Sleep Med* 2020 | EXCLUDE | Discontinued device (Basis B1 was withdrawn from market), n=18/40 nights, and reports correlations plus accuracy/sensitivity/specificity but no TST bias with limits of agreement. #33-35 cover this better |
| 61 | PMID 34741243 | Consumer-grade sleep trackers are still not up to par. *Sleep Breath* 2022 | EXCLUDE | Commentary/short report; no pooled bias or limits of agreement |
| 62 | PMID 36256631 | Fitbit Charge 4 in Chinese patients with chronic insomnia. *PLoS One* 2022 | EXCLUDE | Single device in a clinical insomnia population; #35 pools Fitbit models by generation, which is the more useful analysis |

---

## Identifiers that failed verification

**None.** All 62 identifiers listed above resolved successfully. Two access failures are recorded, neither of
which is a verification failure:

| Identifier | Issue | How handled |
|---|---|---|
| PMID 41371273 / DOI 10.1542/peds.2025-071832 | Unpaywall reports `is_oa: false`, `oa_status: closed`; no OA copy located | Included at `access_tier: abstract_only`. I deliberately did **not** compute a CI on its 70% stability figure because the abstract supplies two candidate denominators (315 and 207) without saying which applies — manufacturing one would have produced a fake interval |
| DOI 10.1016/j.sleep.2010.11.008 (Gradisar 2011 meta, #32) | Paywalled; no OA copy via Unpaywall or OpenAlex | Included at `access_tier: abstract_only` with `se: null` and `ci: null`; the "2+ hours" figure is recorded as a **lower bound**, not a point estimate |

## Access-tier summary

| Tier | Count |
|---|---|
| `full_text` | 17 |
| `abstract_only` | 18 |
| `secondhand` | 0 |

## Evidence-tier summary

| Tier | Count | Records |
|---|---|---|
| `T1` randomised / within-subject | 3 | `gradisar2011rct`, `sletten2018`, `chinoy2021` |
| `T4` prospective cohort, objective exposure | 3 | `bixler2016`, `chan2019`, `jaakallio2026` |
| `TX` cross-sectional / normative / guideline | 29 | all others |

The `TX` dominance is unavoidable: prevalence, ICSD-3 criteria and instrument cut-offs cannot be
randomised. The downstream model should treat the prevalence priors as `TX`-quality and inflate uncertainty
accordingly, which is what the intervals in `screening_priors.md` attempt to do.
