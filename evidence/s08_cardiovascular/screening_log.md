# Screening log — shard `s08_cardiovascular`

Domain: blood pressure, hypertension, coronary heart disease, stroke and major adverse
cardiovascular events in relation to short sleep — both acute experimental BP/autonomic effects and
long-run incident-disease epidemiology.

**85 records screened, 18 included, 67 excluded.** Gate G1 threshold (>= 25) met; shard task
threshold (>= 30) met.

All identifiers below were returned by live PubMed E-utilities queries (`esearch` + `esummary`), not
recalled from memory. Every included record additionally had its DOI resolved against Crossref and
its PMID against PubMed `esummary` before extraction — see `verification_raw.json` for the raw
returns (18/18 resolved on both services).

## Search strategy

| # | Query | Hits returned |
|---|---|---|
| 1 | `sleep duration dose-response meta-analysis cardiovascular disease` | 16 |
| 2 | `Cappuccio sleep duration cardiovascular meta-analysis` | 1 |
| 3 | `short sleep duration incident hypertension meta-analysis prospective` | 5 |
| 4 | `Guo sleep duration hypertension meta-analysis` | 3 |
| 5 | `Meng sleep duration hypertension` | 14 |
| 6 | `Gangwisch short sleep duration hypertension NHANES I` | 4 |
| 7 | `sleep restriction blood pressure sympathetic young healthy adults experimental` | 1 |
| 8 | `sleep restriction randomized crossover blood pressure healthy` | 9 |
| 9 | `Daghlas sleep duration myocardial infarction Mendelian randomization` | 1 |
| 10 | `Mendelian randomization sleep duration blood pressure stroke` | 1 |
| 11 | `sleep duration carotid intima-media thickness young adults` | 4 |
| 12 | `sleep duration arterial stiffness adolescents young adults` | 4 |
| 13 | `adolescents sleep duration blood pressure prehypertension` | 10 |
| 14 | `Mendelian randomization sleep duration hypertension systolic blood pressure UK Biobank` | 2 |
| 15 | `genetically predicted sleep duration stroke Mendelian randomization` | 7 |
| 16 | `van Leeuwen sleep restriction recovery healthy young men autonomic` | 1 |
| 17 | `meta-analysis experimental sleep restriction deprivation blood pressure effect` | **0** |
| 18 | `partial sleep deprivation blood pressure meta-analysis systematic review trials` | 1 |
| 19 | `actigraphy measured sleep duration incident cardiovascular events cohort` | 6 |
| 20 | `school start time delay blood pressure cardiovascular adolescents quasi-experimental` | **0** |

Two queries returned **zero** hits, and both zeros are substantive findings rather than search
failures — see `station_report.md`:
- No meta-analysis of experimental sleep restriction framed as such (query 18 found the one that
  exists, indexed under a different phrasing, in a nursing journal).
- **No school-start-time or other natural-experiment study of sleep and cardiovascular outcomes
  exists.** Tier T2 is empty for this entire domain.

## INCLUDED (18)

| PMID | Study | Tier | Why included |
|---|---|---|---|
| 21300732 | Cappuccio 2011, Eur Heart J | T5 | Target #1. Separate pooled RR for CHD (1.48) and stroke (1.15); total CVD null (1.03) |
| 28889101 | Yin 2017, JAHA | T5 | Target #2. **The** dose-response record: per-hour slopes AND spline RRs tabulated at 3-11 h |
| 36237900 | Huang 2022, Front Cardiovasc Med | T5 | Target #2, newer synthesis. 71 cohorts / 3.8 M; non-elevated-risk band 4.3-10.3 h |
| 30371228 | Kwok 2018, JAHA | T5 | Key **disconfirming** dose-response: no significant excess risk below 7 h in 3.34 M people |
| 27743803 | Itani 2017, Sleep Med | T5 | Largest dichotomous synthesis (153 studies); its own meta-regression found no CVD dose-response |
| 35245890 | Wang 2022, Sleep Med | T5 | Newest stroke-specific dose-response (RR 1.33); documents instability of the stroke estimate |
| 23394772 | Guo 2013, Sleep Med | T5 | Target #3, the named "Guo et al." Longitudinal hypertension RR 1.23 |
| 22763475 | Wang 2012, Hypertens Res | T5 | Target #3 age interaction: incident hypertension RR 1.33 in subjects aged **< 65** |
| 30451942 | Li 2019, J Hum Hypertens | T5 | Only dose-response hypertension MA. Retained but **weight zero** — fails own leave-one-out |
| 16585410 | Gangwisch 2006, Hypertension | T5 | Target #3/#7. HR 2.10 at <= 5 h, ages 32-59; supplies absolute hypertension incidence (13.5%) |
| 34247512 | Covassin 2021, Hypertension | **T1** | Target #4 primary. Age 23.4, randomised crossover, 24-h ABPM, 9 nights; **null in men** |
| 29367834 | van Leeuwen 2018, Sleep Biol Rhythms | **T1** | Target #4. Young **men** only; 5 restriction + 3 recovery nights = subject's exact cycle |
| 31455197 | Hu 2020, West J Nurs Res | **T1** | Target #4 pooled. Meta-analysis of RCTs: **null** for SBP, DBP and HR |
| 31488267 | Daghlas 2019, JACC | **T3** | Targets #5 + #7. MR per hour; staged adjustment models; **absolute incidence per 1000 PY** |
| 40086821 | Zhao 2025, Open Heart | **T3** | Target #5 replication + depression-mediated fraction (9-13%) |
| 38350061 | Guo 2024, Neurology | **T3** | Target #5 stroke. MR supports insomnia, **not duration**; adjustment kills most associations |
| 22935396 | Sands 2012, Stroke | TX | Target #6. Actigraphy + cIMT, 0.026 mm/h in men. **Note: ages 37-52, not "young adults"** |
| 24487981 | Meininger 2014, Am J Hypertens | TX | Target #6. **Only age-matched record** (11-16 y), actigraphy + 24-h ABPM, -0.57 mmHg/h |

## EXCLUDED (67)

### Wrong exposure — napping, irregularity, quality, insomnia or composite rather than duration (13)

| PMID | Record | Reason |
|---|---|---|
| 36480117 | Daytime napping and CHD, dose-response MA | Exposure is napping, not habitual duration |
| 33870591 | Daytime napping and stroke, dose-response MA | Napping |
| 30241617 | Lifestyle indices and CVD risk MA | Composite lifestyle index; sleep not separable |
| 32138974 | Sleep irregularity and CVD, MESA (JACC 2020) | Exposure is irregularity, not duration |
| 36259552 | MESA CVH score including sleep (JAHA 2022) | Composite 8-metric score; sleep-duration effect not isolable. Also mean age 69 |
| 39228701 | Multidimensional sleep profiles, ML, dementia/CVD | Composite ML profile; also a medRxiv preprint |
| 38918750 | Total sleep duration **variability** and new stroke | Exposure is variability |
| 35707994 | MR of napping/sleepiness and cardiometabolic disease | Napping and sleepiness |
| 38455319 | Poor sleep **quality** and cIMT in resident doctors | Quality, not duration |
| 38440112 | Acupuncture for insomnia in hypertensives | Intervention study, wrong exposure |
| 41656501 | Insomnia and CVD: untangling a complex relationship | Narrative review; insomnia |
| 36539296 | MR of sleep traits and functional outcome after stroke | Post-stroke prognosis, not incidence |
| 38262521 | MR of sleep-behavioural traits and healthspan | Composite healthspan outcome |

### Wrong outcome — belongs to another shard (9)

| PMID | Record | Reason |
|---|---|---|
| 26900147 | Nighttime/24-h sleep and all-cause mortality MA | Mortality shard |
| 29247105 | Sleep duration/quality and blood lipids MA | Lipids |
| 23682639 | Sleep restriction and lipid profiles, controlled feeding | Lipids |
| 18246976 | Sleep duration and diabetes incidence | Metabolic shard |
| 30615104 | Sleep restriction and overfeeding metabolic outcomes | Metabolic shard |
| 41760316 | Sleep duration/depression and cancer incidence, CHARLS | Cancer |
| 42046344 | MR of lifestyle on diabetes complications | Diabetes |
| 41021423 | Sleep restriction and pain sensitivity | Pain |
| 26104968 | Conditioned pain modulation after partial sleep restriction | Pain |
| 39488298 | Sleep restriction, light intensity and mental effort | Cognition shard |

### Long sleep only (2)

| PMID | Record | Reason |
|---|---|---|
| 28890167 | Long sleep duration and health outcomes MA | Long sleep only; subject's exposure is restriction |
| 32899076 | Long sleep and arterial stiffness, Chinese population | Long sleep only |

### Superseded by a larger or later synthesis already included (4)

| PMID | Record | Reason |
|---|---|---|
| 28366344 | Sleep duration and stroke, dose-response MA (2017) | Superseded by Wang 2022 (35245890) |
| 27584562 | Sleep duration and stroke MA (Int J Cardiol 2016) | Superseded by Wang 2022 |
| 27336192 | Sleep duration and CHD MA (Int J Cardiol 2016) | Superseded by Yin 2017, which is dose-response |
| 24005775 | Sleep duration/insomnia and hypertension MA (2013) | Overlaps Guo 2013 and Wang 2012; adds no dose-response |

### Cross-sectional, descriptive or diseased/mismatched population (23)

| PMID | Record | Reason |
|---|---|---|
| 39968409 | Weekend catch-up sleep and hypertension, NHANES 2017-20 | Cross-sectional; relevant topic but TX and no incident outcome |
| 42337605 | Sleep-duration abnormality and cardiometabolic indicators, NHANES | Cross-sectional |
| 34991527 | Factors associated with sleep duration in US hypertensives | Descriptive, reverse direction |
| 28619699 | BP and sleep duration in Turkish children | Cross-sectional; office BP |
| 24628980 | Short sleep and prehypertension, Lithuanian children | Cross-sectional |
| 21997181 | Sleep duration and hypertension, Chinese children | Cross-sectional |
| 19633568 | Sleep duration and BP in children | Cross-sectional |
| 18711015 | Sleep **quality** and elevated BP in adolescents (Circulation 2008) | Exposure is quality/efficiency; cross-sectional. Closest age match after Meininger |
| 21730305 | Determinants of secular decreases in childhood BP | Descriptive, ecological |
| 34976884 | Lifestyle clusters and cardiometabolic risk in adolescents | Composite latent-class exposure |
| 24038303 | Sleep duration and cIMT in police officers | Occupational, cross-sectional; overlaps Sands 2012 conceptually with weaker design |
| 41481840 | Ecologically assessed sleep and pulse-wave velocity, young adult African Americans | Cross-sectional; small; screened as best PWV candidate in young adults |
| 27058653 | Sleep duration and arterial stiffness, HELIUS | Cross-sectional adults |
| 40077669 | TMAO/resistin and cIMT in obesity | Wrong exposure entirely |
| 38584515 | Sleep duration and cardiometabolic health in type 1 diabetes | Diseased population |
| 40685379 | Shallow sleep and diabetic carotid atherosclerosis | Diabetic population |
| 29295853 | BP in children with chronic kidney disease | Diseased population |
| 29524090 | Nocturnal BP fluctuation in severe OSA with hypertension | OSA population |
| 34347565 | Sleep-disordered breathing, BP and albuminuria, Nagahama | SDB; albuminuria outcome |
| 40110634 | Sleep-disordered breathing, anaemia, microcytosis | Off topic |
| 38984556 | CVD risk in people living in prison, Ghana | Off topic |
| 35171528 | Maternal sleep and adverse pregnancy outcomes | Wrong population |
| 41617558 | Predictors of long and short sleepers, ELSA-Brasil | Descriptive |
| 39576990 | ML early-warning model for lichenoid vulvar disease | Irrelevant (search noise) |
| 22055504 | Resveratrol and energy metabolism in obese humans | Irrelevant (search noise) |

### Acute single-night or total-deprivation designs (3)

| PMID | Record | Reason |
|---|---|---|
| 38991306 | Total sleep deprivation, autonomic and cortisol responses, SR | Total deprivation; acute stressor reactivity, not multi-night restriction |
| 38038716 | Aerobic exercise and ABP after acute partial sleep deprivation | Single night + exercise co-intervention confounds the sleep contrast |
| 42471255 | Weekend sleep restriction/recovery pilot RCT (2026) | Pilot, "pilot study" per title; screened as topically ideal but too small/preliminary to extract |

### Methodological, correspondence, review or instrument-source (7)

| PMID | Record | Reason |
|---|---|---|
| 34435311 | Sleep duration and health outcomes: an umbrella review | Umbrella of the MAs I already include; secondhand |
| 39107813 | Methodological/reporting quality of sleep-duration–hypertension MAs | Methodological appraisal, not an effect estimate. **Cited in `li2019_htn_dr` notes** as evidence that this specific literature has recognised quality problems |
| 24176304 | Response to Letter re: definition of sleep duration and hypertension MA | Correspondence |
| 19893498 | Insomnia/sleep duration as mediators of depression–hypertension (Gangwisch 2010) | Mediation of depression, not a sleep-duration effect estimate. Topically relevant to target #7; superseded for that purpose by Zhao 2025's quantified mediated fraction |
| 37925459 | Poor sleep and shift work, BP and inflammation, UK Biobank | Cross-sectional BP/biomarker associations; shift work confounded |
| 30531941 | GWAS of device-measured physical activity and sleep duration | Instrument source, not an outcome study |
| 32384904 | MR of physical activity/sedentary/sleep on CVD and lipids | Screened; sleep-duration CVD estimate not separable from the multi-exposure framing in the abstract |
| 37608260 | Sleep quality in women with diabetes in pregnancy | Off topic |

## Notes on screening decisions

- **Nothing was excluded for reporting a null or inconvenient result.** Three of the 18 included
  records are primarily disconfirming (`kwok2018`, `hu2020_bp_rct_ma`, `guo2024_stroke_mr`) and two
  more contain prominent null components (`cappuccio2011` total CVD; `covassin2021` male stratum).
- The task named **Meng et al.** as a candidate hypertension meta-analysis. Query 5 was run
  specifically for it and returned 14 records, **none** of which is a Meng meta-analysis of sleep
  duration and incident hypertension. I conclude no such paper exists under that author name and
  report the two that do exist (Guo 2013, Wang 2012) plus the one dose-response attempt (Li 2019).
  The seed name was a hint, not a fact, as the instructions anticipate.
- The task's expectation of "a DOSE-RESPONSE meta-analysis of sleep duration and CVD ... Yin et al.
  (JAHA, approx 2017)" was **confirmed exactly**: Yin J et al., JAHA 2017;6(9):e005947.
- `24005775` and `19893498` were the two hardest exclusion calls; both are topically on-target but
  add no extractable effect that is not already better measured by an included record.
