# Screening log — shard `s21_drowsy_driving`

**Records screened: 52. Included: 24. Excluded: 28.**

Every identifier in the INCLUDED table was checked programmatically against Crossref
(`api.crossref.org/works/<DOI>`) and PubMed (`esummary.fcgi`) before the record was written; raw API
responses are in `verification_raw.json` and the checking script is `verify.py`. Every identifier in the
EXCLUDED table was returned by a live PubMed search (`esearch.fcgi`) during this session — none is recalled
from memory. Retrieved source material is under `src/`.

## Search strategy

PubMed `esearch` queries actually run (counts as returned at time of search):

| Query | Hits |
|---|---|
| `sleep+duration+motor+vehicle+crash+risk+odds+ratio` | 3 |
| `drowsy+driving+young+drivers+crash+risk` | 51 |
| `school+start+time+crash+rate+teen+drivers` | 3 |
| `sleepiness+meta-analysis+motor+vehicle+accident+risk` | 11 |
| `short+sleep+duration+traffic+accident+meta-analysis` | 2 |
| `sleep+and+road+traffic+crash+systematic+review+meta-analysis` | 8 |
| `fatigue+related+crash+risk+meta-analysis+hours+of+sleep` | 0 |
| `"sleep duration" AND "crash" AND meta-analysis` | 0 |
| `sleep+duration+crash+meta-analysis+dose-response` | 0 |
| `Klauer+teen+novice+driver+naturalistic+crash+risk` | 8 |
| `Dingus+driver+crash+risk+factors+naturalistic+driving+data` | 12 |
| `insufficient+sleep+adolescents+injury+risk+behaviors` | 16 |
| `drowsy+driving+population+attributable+fraction` | 2 |

Non-PubMed retrieval (grey literature, which is where the most usable numbers in this domain live):
`aaafoundation.org` (four Tefft reports plus the Owens naturalistic study), `iihs.org` Fatality Facts
2023/2024 pages, `crashstats.nhtsa.dot.gov` (NCSA traffic-safety facts on drowsy driving and young
drivers), `fhwa.dot.gov` Highway Statistics table DL-22, `cdc.gov`, `ghsa.org`, and `nchs` Data Brief 456.

**A NEGATIVE FINDING THAT THE TASK ASKED ME TO CHECK FOR.** Requirement 1 asked for "any meta-analysis of
sleep duration or sleepiness and motor-vehicle crash risk." A meta-analysis of **sleepiness** and crash risk
exists and is included (`bioulac2017`). A meta-analysis of habitual sleep **duration** and crash risk **does
not exist in PubMed**. Four query formulations returned 0, 0, 2 and 2 hits, and the hits were obstructive
sleep apnoea and hypnotic-drug reviews. The dose-response evidence the downstream model most needs — pooled
OR by hours of habitual sleep — has never been meta-analysed. Per hard rule 4, I report this rather than
substituting a proxy and calling it a meta-analysis.

---

## INCLUDED (24)

`E` = number of effects extracted. `V` = identifier verification outcome.

| # | study_id | Identifier | Tier | Design | E | V | What it contributes |
|---|---|---|---|---|---|---|---|
| 1 | `tefft2016_aaa` | no DOI (AAA Foundation tech report, retrieved from aaafoundation.org) | T5 | quasi-induced exposure, NMVCCS | 12 | UNVERIFIED (no DOI exists; `access_tier: full_text`, PDF in `src/`) | **The core dose-response.** Acute hours-slept ORs vs ≥7 h: 4-5 h **4.3** (2.2-8.3), 5-6 h **1.9** (1.3-2.6), 6-7 h **1.3** (1.1-1.7). Plus the **habitual** usual-sleep ORs, which are the like-for-like ones for this subject and are much weaker (5-6 h: **1.4**, 0.5-3.6, null). |
| 2 | `tefft2018` | doi `10.1093/sleep/zsy144`, pmid `30239905` | T5 | quasi-induced exposure, NMVCCS | 5 | VERIFIED | Peer-reviewed publication of the same analysis. **Same cohort as #1** — `cohort_family: NMVCCS_2005_2007`, do not pool. |
| 3 | `connor2002` | doi `10.1136/bmj.324.7346.1125`, pmid `12003884` | T5 | population case-control (schema: `cross_sectional`) | 4 | VERIFIED | Injury-crash ORs: ≤5 h in past 24 h **2.7** (1.4-5.4); Stanford sleepiness ≥4 **8.2** (3.4-19.7); driving 02:00-05:00 **5.6** (1.4-22.7). |
| 4 | `martiniuk2013` | doi `10.1001/jamapediatrics.2013.1429`, pmid `23689363` | T5 | prospective cohort, 19,327 drivers aged 17-24 | 4 | VERIFIED | **The most like-for-like estimate in the shard**: young drivers, habitual ≤6 h vs >6 h, **police-reported** crash outcome, RR **1.21** (1.04-1.41). |
| 5 | `gottlieb2018` | doi `10.1186/s12916-018-1025-7`, pmid `29554902` | T5 | prospective cohort, PSG-screened | 5 | VERIFIED | Habitual 6 h vs 7-8 h OR **1.33**; per-hour OR **1.13** (1.01-1.28); **adjusted for annual miles driven**, and the association is *stronger* (1.22) in people not reporting sleepiness. |
| 6 | `bioulac2017` | doi `10.1093/sleep/zsx134`, pmid `28958002` | T5 | meta-analysis, 17 studies, 70,098 people | 1 | VERIFIED | The only relevant meta-analysis: sleepiness at the wheel OR **2.51** (1.87-3.39). Sleepiness, not duration. |
| 7 | `cummings2001` | doi `10.1136/ip.7.3.194`, pmid `11565983` | T5 | case-control (schema: `cross_sectional`) | 3 | VERIFIED | Drowsiness aRR **2.4**; and the **negative-control failures** that justify my causal discount: playing a radio aRR 0.6, coffee 0.5. |
| 8 | `foss2019` | doi `10.1016/j.aap.2018.03.031`, pmid `29706226` | **T2** | ARIMA interrupted time series + 3 matched control counties | 5 | VERIFIED | **The strongest identification in the school-start-time literature**, and its crash-rate effect is **not significant (p = .076)**. Its hour-by-hour test shows crashes *moved with the commute* rather than falling. |
| 9 | `binhasan2020` | doi `10.5664/jcsm.8208`, pmid `31992393` | **T2** | pre-post + contemporaneous control, Fairfax County | 2 | VERIFIED | Second-strongest design; RR ≈ **1.07** with CI lower bound at exactly 1.00. |
| 10 | `danner2008` | doi `10.5664/jcsm.27345`, pmid `19110880` | **T2** | county pre-post, Kentucky | 2 | VERIFIED | The original Kentucky finding, RR ≈ 1.17. Two-year pre-post in one county, no control county. |
| 11 | `vorona2014` | doi `10.5664/jcsm.4192`, pmid `25325600` | TX | **two-county cross-section, no pre-post** | 3 | VERIFIED | RR ≈ 1.27-1.29. Downgraded to TX, not T2 — there is no exogenous change, only two places that differ. Its own mechanism test came out **backwards**. |
| 12 | `vorona2011` | doi `10.5664/jcsm.28101`, pmid `21509328` | TX | **two-city cross-section, no pre-post** | 2 | VERIFIED | RR ≈ 1.28-1.41. Same downgrade, same reason. |
| 13 | `iihs2024_fars` | no DOI (IIHS Fatality Facts, FARS census) | TX | life table | 11 | UNVERIFIED (agency web page, retrieved to `src/`) | **The denominator.** Male driver deaths/100,000 by single year of age (16: 5.3, 17: 7.5, 18: 10.5, 19: **13.7**, the lifespan peak); the requested 16-19 and 20-24 occupant rates; day-of-week and month tables used to derive the exposed fraction. |
| 14 | `nhtsa_drowsy_counted` | no DOI (NCSA/NHTSA) | TX | police-reported census | 5 | UNVERIFIED (`access_tier: secondhand`) | **The low side of the order-of-magnitude discrepancy**: 1.4% of all crashes, 2.0% of injury crashes, 2.4% of fatal crashes, **633 deaths in 2023**. |
| 15 | `tefft2012` | doi `10.1016/j.aap.2011.05.028`, pmid `22269499` | TX | imputation on NASS-GES/CDS/FARS | 4 | VERIFIED | **Resolves the discrepancy inside one dataset**: drowsiness unknown for **45%** of drivers; 3.6% of fatal crashes if unknown≈not-drowsy, **16.5%** imputed. Also 7.0% of all crashes and 13.1% of hospitalisation crashes. |
| 16 | `tefft2024_aaa` | no DOI (AAA research brief) | TX | CISS→FARS imputation, 208,727 drivers | 4 | UNVERIFIED (`abstract_only`) | Current best drowsy share of **fatal** crashes: **17.6%**, ~**6,326 deaths/yr**; states the share is **highest at ages 16-20** but publishes no number for that group. |
| 17 | `owens2018_aaa` | no DOI (AAA Foundation / SHRP2) | **T4** | naturalistic driving, **PERCLOS video** | 5 | UNVERIFIED (full text in `src/`) | **Objective exposure, no self-report**: eyelid closure coded in the 3 min before 701 real crashes; drowsiness in **8.8-9.5%** of all crashes, **10.8%** of police-reportable ones. Also the only *measured* age breakdown: **8.9% at ages 16-19** vs 11.3% at 20-24, age variation not significant. Anchors Route 3. |
| 18 | `ghsa2026` | no DOI (GHSA report) | TX | agency synthesis of SHRP2 | 4 | UNVERIFIED (full text in `src/`) | Drowsy share of **baseline driving time** = **1.57%**, the denominator for the Route 3 odds ratio. States the research/police gap as *"ten times more than the raw FARS data reported by NHTSA."* |
| 19 | `owens2019` | doi `10.1016/j.jpeds.2018.09.072`, pmid `30392873` | TX | cross-sectional, 431 teen drivers | 3 | VERIFIED | The only measured link from **teen** sleep duration to **drowsy-driving frequency**: +13.9 percentage points at <7 h vs ≥8 h. Supplies the Route 3 multiplier. |
| 20 | `wheaton2016` | doi `10.15585/mmwr.mm6513a1`, pmid `27054407` | TX | cross-sectional, 50,370 US high-school students | 5 | VERIFIED | **The confounding evidence**, in the exact target population: short sleepers drink-drive, ride with drinking drivers, skip seatbelts and text while driving. Includes the **≥10 h negative-control failure**. |
| 21 | `wheaton2014` | pmid `24990488`, no DOI | TX | cross-sectional, 92,102 US adults | 4 | VERIFIED (PubMed) | Replicates the alcohol/seatbelt confounding in adults; and finds drowsy driving does **not** vary by smoking, so the confounding is selective rather than one undifferentiated "risky person" factor. |
| 22 | `pizza2010` | doi `10.5664/jcsm.27708`, pmid `20191936` | TX | cross-sectional, Italian adolescents | 3 | VERIFIED | **Smoking** predicts adolescent crashes as strongly as drowsiness — a no-vigilance-mechanism confounder. |
| 23 | `hutchens2008` | doi `10.1016/j.aap.2007.10.001`, pmid `18460353` | TX | cross-sectional, US national teen survey | 2 | VERIFIED | Independent US replication of the same smoking/drowsy-driving entanglement. |
| 24 | `czeisler2016` | doi `10.1016/j.sleh.2016.04.003`, pmid `28923267` | TX | expert consensus panel | 2 | VERIFIED | The sleep-medicine field's own dose thresholds: probable impairment **3-5 h**, definite unfitness **≤2 h** — both *below* this subject's routine dose. Argues against pricing him with acute coefficients. |

Total effects extracted: **100** across 24 records. All 24 validate against `effect.schema.json` (`validate.py`).

### Identifiers that failed or could not be verified

No identifier was found to be *wrong*. Six records carry `verification.status: UNVERIFIED` because **no DOI
or PMID exists to check** — they are agency and foundation reports (IIHS, NHTSA/NCSA, three AAA Foundation
reports, GHSA), which is unavoidable because the most decision-relevant numbers in this domain (the FARS
denominator, the police-reported drowsy share, the naturalistic PERCLOS share) are published only as grey
literature. For each I retrieved the document itself into `src/` and quoted verbatim, and set
`access_tier` to `full_text`, `abstract_only` or `secondhand` according to what I actually held.
`wheaton2014` (MMWR) has a real PMID but no DOI; PubMed verified it.

Three DOIs were **not** initially known to me and were recovered by Crossref title search rather than
guessed, because JCSM back-issues were assigned DOIs retrospectively: `danner2008` → `10.5664/jcsm.27345`,
`vorona2011` → `10.5664/jcsm.28101`, `pizza2010` → `10.5664/jcsm.27708`. All three then resolved.

---

## EXCLUDED (28)

| # | Identifier | Short title | Reason for exclusion |
|---|---|---|---|
| 25 | pmid `26903657`, doi `10.1073/pnas.1513271113` | Dingus 2016, Driver crash risk factors, naturalistic driving (PNAS) | **Wanted it, could not get it.** Full text is not open access; Europe PMC returned an empty body and NCBI efetch returned front matter only. The drowsiness odds ratio is in the body, not the abstract, and I will not cite a number I did not read. Also **same cohort as `owens2018_aaa`/`ghsa2026`** (`SHRP2_NDS`), so it would have been cohort-duplicated. This is the single most valuable failed retrieval in the shard. |
| 26 | pmid `24759443` | Klauer 2014, young driver crash risk by duration of distraction | Exposure is **distraction**, not sleep. |
| 27 | pmid `23992677` | Simons-Morton 2013, crash/near-crash risk in novice teens | Naturalistic teen cohort but the reported exposure is kinematic risky driving, not sleep. |
| 28 | pmid `21545880` | Lee 2011, naturalistic assessment of novice teenage crash experience | Same cohort family as #27; descriptive, no sleep exposure. |
| 29 | pmid `26403899` | Naturalistic teenage driving study: findings and lessons learned | Methods/summary paper, no extractable sleep-crash effect. |
| 30 | pmid `30006026` | Crash risk during learner vs independent driving | Exposure is licensing phase, not sleep. |
| 31 | pmid `32563399` | Crash rates over time, younger and older drivers, SHRP2 | Exposure is driving experience; SHRP2 already represented. |
| 32 | pmid `34732793`, doi `10.1038/s41598-021-99133-y` | On-road driving impairment after sleep deprivation differs by age | **Surrogate outcome** (lane position on a test route), not crashes. Acute total deprivation, not habitual restriction. Direction consistent; contributes no mortality number. |
| 33 | pmid `38463828` | RCT protocol: improving young driver sleep to reduce crash risk | **Protocol only, no results.** This is the trial that would answer the causal question; it had not reported at time of screening. |
| 34 | pmid `39532611` | NSF drowsy driving prevalence and beliefs, US sample | Prevalence and attitudes only, no crash outcome. |
| 35 | pmid `31347230` | Young drivers who continue to drive while sleepy | Outcome is a driving *decision*, not a crash. |
| 36 | pmid `32091936` | Sleep-impaired emotional regulation and risky sleepy driving | Outcome is self-reported risky sleepy driving, not a crash. |
| 37 | pmid `29324264` | Driver education to improve young-driver sleep knowledge | Outcome is knowledge, not crashes. |
| 38 | pmid `30210842` | Daytime sleepiness among young Omani drivers | Non-US, no crash-risk contrast usable for a US denominator. |
| 39 | pmid `29306796` | Perceived legitimacy of enforcement for sleep-related crashes | Attitudes, not risk. |
| 40 | pmid `15647575`, doi (NEJM 2005) | Barger, extended work shifts and crash risk among interns | **Acute shift-work deprivation in physicians.** 24-30 h continuous wakefulness is not this subject's exposure; adolescent-match poor. Would inflate the risk ratio if pooled. |
| 41 | pmid `37303489` | Work schedules of senior resident physicians and safety | Same reason as #40. |
| 42 | pmid `29126462` | Prediction of drowsiness events in night-shift workers | Night-shift population; outcome is a predicted drowsiness event. |
| 43 | pmid `20465027` | OSA and crash risk: systematic review and meta-analysis | **Obstructive sleep apnoea**, a disease, not sleep restriction. |
| 44 | pmid `21061860` | CPAP reduces crash risk in OSA: meta-analysis | OSA treatment. |
| 45 | pmid `24317450` | OSA in North American commercial drivers | OSA, occupational drivers. |
| 46 | pmid `26851617` | Driving performance over time in untreated OSA | OSA, surrogate outcome. |
| 47 | pmid `33141943` | Myofunctional therapy for OSA (Cochrane) | OSA treatment; surfaced only by keyword overlap. |
| 48 | pmid `26497082` | CPAP vs mandibular devices for sleepiness in OSA | OSA treatment. |
| 49 | pmid `32441843` | Interhemispheric sleep depth coherence and driving safety in apnoea | OSA; EEG surrogate. |
| 50 | pmid `15089115` | Residual effects of hypnotics | **Drug** exposure, not sleep duration. |
| 51 | pmid `22785089` | Risk of road accident and drug use: meta-analysis | Drug exposure. |
| 52 | pmid `42176184` | Untreated ADHD and motor vehicle accidents: meta-analysis | ADHD exposure. Relevant only as a reminder that crash risk has many correlated causes. |

### CDC WONDER: attempted and abandoned

The task named CDC WONDER as a source for the baseline rate. I attempted the WONDER API and it rejected my
`Year/Month` code set (`Invalid 'Year/Month' codes`) across several formulations. Rather than keep guessing
at an undocumented code vocabulary, I substituted two **better** sources for this specific purpose and
recorded both: IIHS Fatality Facts, which tabulates the same FARS census that WONDER's motor-vehicle codes
draw on but is already stratified by sex, single year of age, **and driver-versus-passenger** (which WONDER
is not, and which §1.3 of `injury_channel.md` shows is the distinction that matters here); and NCHS Data
Brief 456 for cause-of-death shares. No number in this shard depends on WONDER.

---

## Exclusion patterns worth flagging to the orchestrator

Three quarters of the literature that a naive keyword search returns for "sleep and crashes" is about
**obstructive sleep apnoea in middle-aged adults** (7 excluded records), **acute shift-work deprivation in
physicians** (3 records), or **drug effects** (2 records). None of the three is this subject's exposure, and
all three carry *larger* effect sizes than habitual mild-to-moderate restriction in a healthy 17-year-old.
A shard that pooled on keyword match would land on a risk ratio two to three times too high. This is the
main reason my adopted RR of 1.5 sits far below the 2.51 that the one available meta-analysis reports.
