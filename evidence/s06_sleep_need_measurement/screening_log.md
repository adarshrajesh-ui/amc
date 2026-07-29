# Screening log — shard `s06_sleep_need_measurement`

**Records screened: 49. Included: 29. Excluded: 20.**

Every identifier below was returned by a live PubMed `esearch`/`esummary` call during this session, so
no PMID or DOI in this table is recalled from memory. All 29 included records were additionally verified
against both Crossref (`api.crossref.org/works/<DOI>`) and PubMed (`esummary.fcgi`), and the DOI that
PubMed reports for the PMID was checked to agree with the DOI recorded in the YAML. **29/29 passed; 0
identifiers failed verification.**

Search strategy: iterative PubMed queries across the two halves of the domain — (A) sleep-need
guidelines, laboratory sleep-satiation/extension protocols, normative distributions, twin and
short-sleeper genetics, short-sleep prevalence; (B) self-report versus actigraphy/PSG agreement,
sleep-efficiency norms, duration-dependent reporting bias, recall rounding. Full text was pursued via
PMC `efetch`, Europe PMC, Unpaywall, publisher PDFs and (where those failed) PMC article HTML.

## Included (29)

| # | study_id | Identifier | Tier | Access | Why included |
|---|---|---|---|---|---|
| 1 | `lauderdale2008` | PMID 18854708 / 10.1097/EDE.0b013e318187a7b0 | TX | full text | The named target. Self-report minus actigraphy bias, calibration slope, r, duration-dependence. |
| 2 | `white2026ffcws` | PMID 41198487 / 10.1016/j.sleh.2025.10.003 | TX | full text | Best age match in shard (mean 15.4 y). Adolescent bias, SD, reverse calibration slope. |
| 3 | `cespedes2016hchs` | PMID 26940117 / 10.1093/aje/kwv251 | TX | abstract | Reverse regression (truth on report) in adults; moderators incl. male sex, night-to-night variability. |
| 4 | `jackson2018mesa` | PMID 29701831 / 10.1093/sleep/zsy057 | TX | abstract | Only retrieved study giving bias against BOTH actigraphy and PSG in the same people. |
| 5 | `short2012diary` | PMID 22437142 / 10.1016/j.sleep.2011.11.005 | TX | abstract | Adolescent diary-vs-actigraphy gap; argues actigraphy under-counts adolescent sleep. |
| 6 | `guedes2016` | PMID 27532757 / 10.1590/1980-5497201600020011 | TX | abstract | Only retrieved study stratifying adolescent bias by sex (boys +1.9 h, ICC 0.06). |
| 7 | `arora2013` | PMID 23951321 / 10.1371/journal.pone.0072406 | TX | full text | Decomposes the gap into recall (13.6 min) vs subjective-objective offset (81.9 min). |
| 8 | `girschik2012` | PMID 22850546 / 10.2188/jea.JE20120012 | TX | full text | Direction of differential error conditional on the REPORT; modal-vs-mean reporting. |
| 9 | `hirshkowitz2015nsf` | PMID 29073412 / 10.1016/j.sleh.2014.12.010 | TX | full text | The named target. NSF bands for 14-17 AND 18-25, all three appropriateness tiers. |
| 10 | `paruthi2016` | PMID 27250809 / 10.5664/jcsm.5866 | TX | full text | The named target. AASM pediatric 13-18 y band + evidence base size (864 articles). |
| 11 | `watson2015consensus` | PMID 26039963 / 10.5665/sleep.4716 | TX | full text | The named target. AASM/SRS adult recommendation, verbatim, incl. young-adult >9 h carve-out. |
| 12 | `watson2015method` | PMID 26235159 / 10.5664/jcsm.4950 | TX | full text | Where the AASM panel states its own evidence-strength and measurement caveats. |
| 13 | `short2018sleepneed` | PMID 29325109 / 10.1093/sleep/zsy011 | T1 | abstract | Only T1 sleep-need estimate in 15-17 year olds (9.0 h satiated, 9.35 h optimal PVT). |
| 14 | `kitamura2016` | PMID 27775095 / 10.1038/srep35812 | T1 | full text | The ONLY direct measurement of the between-person SD of individual sleep need. |
| 15 | `klerman2008` | PMID 18656358 / 10.1016/j.cub.2008.06.047 | T1 | full text | Young-adult sleep-satiation asymptote 8.9 h; habitual-duration spread 6.1-10.3 h. |
| 16 | `klerman2005` | PMID 16295210 / 10.1093/sleep/28.10.1253 | T1 | abstract | Directly tests whether duration spread is need or restriction; answer is restriction. |
| 17 | `kocevska2021herit` | PMID 33636423 / 10.1016/j.smrv.2021.101448 | TX | abstract | Heritability meta-analysis incl. the 6-fold reporter effect (8% parent vs 38-52% self). |
| 18 | `inderkum2018twin` | PMID 29329461 / 10.1093/sleep/zsy004 | TX | abstract | Duration heritability 15% school days vs 68% free days — schedule, not need. |
| 19 | `weedon2022` | PMID 36137075 / 10.1371/journal.pgen.1010356 | TX | abstract | Population null for FNSS variants in ~192k sequenced people; kills the short-sleeper tail. |
| 20 | `he2009dec2` | PMID 19679812 / 10.1126/science.1174443 | TX | full text | DEC2 lower-tail bound on sleep need (6.25 h carriers vs 8.06 h non-carriers). |
| 21 | `shi2019adrb1` | PMID 31473062 / 10.1016/j.neuron.2019.07.026 | TX | full text | ADRB1 FNSS; the "many variants in many genes" polygenic framing for a normal latent need. |
| 22 | `wheaton2018yrbs` | PMID 29370154 / 10.15585/mmwr.mm6703a1 | TX | full text | The named target. Full reported school-night distribution + whole-hour instrument. |
| 23 | `kocevska2021norms` | PMID 33199855 / 10.1038/s41562-020-00965-x | TX | abstract | The named target. 51.5% of teenagers below 8-10 h; self-report/actigraphy sex sign reversal. |
| 24 | `ohayon2004` | PMID 15586779 / 10.1093/sleep/27.7.1255 | TX | full text | The named target. Sleep efficiency flat across adolescence; TST falls on school days only. |
| 25 | `galland2018` | PMID 29590464 / 10.1093/sleep/zsy017 | TX | abstract | Age-matched actigraphy norm: 7.4 h at 15-18 y; SOL 19.4 min; +56 min on nonschool days. |
| 26 | `evans2021actigraphy` | PMID 33823052 / 10.1093/sleep/zsab088 | TX | full text | **Best sleep-efficiency source**: TST/TIB = 87.2% at 10-19.99 y, 87.8% at 20-29.99 y. |
| 27 | `mitterling2015` | PMID 25515109 / 10.5665/sleep.4730 | TX | abstract | PSG sleep efficiency 87.0% at <= 30 y; WASO 6.0%; the young-adult PSG anchor. |
| 28 | `meredithjones2024` | PMID 38627708 / 10.1186/s12966-024-01590-x | TX | full text | PSG efficiency under BOTH definitions (89.1% TIB vs 95.0% SPT); actigraphy specificity 63.8%. |
| 29 | `boulos2019` | PMID 31006560 / 10.1016/S2213-2600(19)30057-8 | TX | abstract | Adult PSG meta-analysis age slopes: efficiency -2.1 pts/decade, TST -10.1 min/decade. |

## Excluded (20)

| # | Identifier | Record | Decision | Reason |
|---|---|---|---|---|
| 30 | PMID 29073398 / 10.1016/j.sleh.2015.10.004 | Hirshkowitz 2015, NSF final report, *Sleep Health* 1(4) | EXCLUDE | Duplicate. Same panel, same bands as `hirshkowitz2015nsf`; including both would double-count one expert panel. |
| 31 | PMID 12683469 / 10.1093/sleep/26.2.117 | Van Dongen 2003, cumulative cost of additional wakefulness | EXCLUDE | Out of domain — cognitive dose-response, belongs to the cognition shard. Its 8.16 h sleep-need figure is retained secondhand inside `kitamura2016`. |
| 32 | PMID 42085943 / 10.1016/j.sleep.2026.108997 | Arizona Twin Project, actigraphy + parent-report heritability | EXCLUDE | Ages 8-13 and the subjective arm is PARENT-report, not self-report; not transportable to an 18-year-old reporting on himself. |
| 33 | PMID 39387212 / 10.1111/ejn.16568 | Genetic contribution to sleep homeostasis in early adolescence | EXCLUDE | Outcome is EEG slow-wave homeostasis, not sleep duration need. |
| 34 | PMID 37753157 / 10.1002/jcv2.12167 | Sub-types of insomnia in adolescents, twin study | EXCLUDE | Insomnia phenotype, not duration or duration measurement. |
| 35 | PMID 35210201 / 10.1016/j.sleh.2021.12.006 | Pubertal onset and actigraphy sleep, middle childhood | EXCLUDE | Middle childhood; superseded for our age band by `galland2018` and `evans2021actigraphy`. |
| 36 | PMID 31408518 / 10.1093/sleep/zsz179 | Sleep duration and PTSD symptoms, twin study | EXCLUDE | Outcome is psychiatric; belongs to another shard. |
| 37 | PMID 24635510 / 10.1111/jsr.12101 | Sleep duration and personality in Croatian twins | EXCLUDE | Outcome is personality; no sleep-need variance component reported. |
| 38 | PMID 24179306 / 10.5665/sleep.3136 | Genetic/environmental contributions to sleep-wake, 12-y-o twins | EXCLUDE | Superseded by `inderkum2018twin`, which is from the same literature but adds the school/free-day contrast that is the decision-relevant part. |
| 39 | PMID 36272246 / 10.1016/j.sleep.2022.09.027 | Sleep-corrected social jetlag and mental health in adolescents | EXCLUDE | Outcome is mental health; social jetlag belongs to the circadian shard. |
| 40 | PMID 35669317 / 10.1093/sleepadvances/zpac015 | Sleep restriction and waking alpha EEG in adolescents | EXCLUDE | Outcome is EEG, not sleep need or measurement error. |
| 41 | PMID 38174382 / 10.1080/24733938.2023.2297903 | Self-report vs actigraphy in female football players | EXCLUDE | Small, female-only, elite-athlete sample; wrong sex and a population with atypical sleep behaviour. |
| 42 | PMID 42432880 / 10.1097/MD.0000000000049698 | Evening smartphone restriction in university students | EXCLUDE | Intervention trial; reports no self-report-vs-objective validation. |
| 43 | PMID 38687600 / 10.2196/53441 | Stress and sleep duration from year-long actigraphy | EXCLUDE | Outcome is the stress-sleep association; no measurement-agreement estimate. |
| 44 | PMID 31923256 / 10.1371/journal.pone.0227002 | Eating-fasting and activity-rest cycles in Indian adolescents | EXCLUDE | Chronobiology of meal timing; no sleep-need or agreement estimate. |
| 45 | PMID 32126835 / 10.1080/07420528.2020.1727916 | Actigraphic sleep and 6-sulfatoxymelatonin in Dutch children | EXCLUDE | Children; single-country, small, superseded by the two actigraphy meta-analyses. |
| 46 | PMID 28040232 / 10.1016/j.jpeds.2016.11.069 | Sleep in children with cystic fibrosis | EXCLUDE | Clinical population; normative values not applicable to a healthy 18-year-old. |
| 47 | PMID 41831264 / 10.1016/j.sleep.2026.108894 | Inadequate sleep, New Mexico Youth Risk & Resiliency Survey | EXCLUDE | Same survey family as `wheaton2018yrbs` (YRBS); state-level subset would double-count. |
| 48 | PMID 39382947 / 10.2196/57803 | Trends in self-perceived overweight among adolescents | EXCLUDE | Irrelevant; returned as search noise. |
| 49 | PMID 29325164 / 10.1093/sleep/zsy012 | Sleep duration in the United States 2003-2016 (ATUS) | EXCLUDE | Self-reported time-use trends only; no objective comparison, so it cannot inform either half of this domain. |

## Full text sought but not obtained (recorded as `access_tier: abstract_only`)

Documented here because in three cases it demonstrably limited the extraction, and the orchestrator
should know which priors would tighten if these were retrieved.

| Record | Barrier | What was lost |
|---|---|---|
| `kocevska2021norms` | Unpaywall `is_oa: false`; Europe PMC `isOpenAccess: N`; no PMC deposit | **The age- and sex-specific reference charts for sleep duration AND efficiency.** The seed task named this as a primary source for the normative distribution; it could not serve that role. Its normative job was reassigned to `galland2018`, `evans2021actigraphy` and `mitterling2015`. |
| `boulos2019` | Unpaywall `is_oa: false`; no PMC deposit | The age-stratified normative table, i.e. the pooled sleep-efficiency **level** for the youngest adult stratum. Only the age **slopes** were obtainable. |
| `galland2018` | Unpaywall says OA but `academic.oup.com` returns a Cloudflare interstitial to scripted requests; the figshare mirror (13450679) exposes no files via the figshare API | SDs around the 7.4 h pooled estimate for 15-18 year olds, so that effect carries `se: null`. |
| `mitterling2015` | PMC4434553 deposit contains abstract only; OUP PDF blocked | The percentile-curve labels, so I could not tell whether the printed 71.9-94.1% interval is 5th-95th or 10th-90th; the sleep-efficiency SD is therefore left `null` with both derivations shown. |
| `inderkum2018twin` | No PMC deposit; OUP paywall | Confidence intervals on the 15% vs 68% heritability estimates (n = 26 twin pairs, so they are wide). |

Two full texts were recovered only by falling back to **PMC article HTML** after the XML deposit turned
out to contain the abstract alone: `evans2021actigraphy` (which yielded the single most useful number in
the shard, the age-banded TST/TIB sleep efficiency) and `paruthi2016`. Worth noting as a method: a PMC
XML deposit of ~10 kB is a signal that the deposit is abstract-only and that the HTML should be tried.
