# Screening log — `s01_cognition_dose_response`

**185 candidate records screened** (PubMed unique PMIDs; the brief required ≥30, the extraction instructions ≥25). **30 included**, 155 excluded, each with a reason below.

Every PMID in this log was resolved against the PubMed E-utilities `esummary` endpoint, so every title, journal and year below is the value NCBI returned rather than a recalled one. **All 185 identifiers resolved; none failed.** The 30 included records were additionally verified against Crossref by DOI and PubMed by PMID using `/workspace/src/verify_refs.py`'s own logic: **30/30 VERIFIED, title similarity 1.000 for all 30.**

## Search strategy

Three rounds, deliberately sequenced from broad to narrow. Round 3 was added after reading the full text of Campbell 2018, whose discussion cited an age-matched dose-response study (Short et al.) that the first two rounds had missed — reference-chasing from retrieved full texts turned out to be the highest-yield discovery route for this domain.

**Round 1 — broad topical sweep (7 queries, PubMed esearch, retmax 12)**

```
chronic sleep restriction dose response neurobehavioral adolescents time in bed
sleep restriction adolescents randomized crossover cognitive performance time in bed
unified mathematical model performance impairment chronic sleep restriction total sleep deprivation
sleep restriction 4 hours 6 hours 8 hours time in bed psychomotor vigilance dose
school start time later sleep adolescent academic quasi-experiment
sleep extension adolescents cognitive performance randomized
chronic sleep restriction recovery sleep dose response neurobehavioral adults 6 hours
```

**Round 2 — title-field and author-field narrowing (6 queries, retmax 15)**

```
"sleep restriction"[ti] AND adolescen*[ti]
"sleep restriction"[ti] AND ("dose-response"[ti] OR "dose response"[ti])
"sleep restriction"[ti] AND (vigilance[ti] OR "psychomotor"[ti] OR attention[ti])
"chronic sleep restriction"[ti] AND recovery[ti]
Chee MW[au] AND (adolescen* OR "sleep restriction")
"Need for Sleep"[ti]
```

**Round 3 — targeted author and protocol sweeps to close age-matched gaps (10 queries, retmax 20)**

```
Short MA[au] AND (adolescen* OR "sleep restriction" OR "sleep need")
Carskadon MA[au] AND "sleep restriction" AND (adolescen* OR vigilance OR performance)
("need for sleep study"[tiab] OR "Need for Sleep"[tiab]) AND (adolescen* OR "sleep restriction")
Lo JC[au] AND (adolescen* OR "sleep restriction" OR vigilance)
Cousins JN[au] AND ("sleep restriction" OR adolescen*)
Ong JL[au] AND ("sleep restriction" OR adolescen*)
"sleep restriction" AND ("time in bed" AND (dose OR "dose-response")) AND (adolescen* OR "young adult")
Campbell IG[au] AND ("time in bed" OR "sleep restriction")
"chronic sleep restriction" AND ("psychomotor vigilance" OR PVT) AND (cumulative OR accumulat*)
"sleep restriction"[ti] AND ("working memory"[ti] OR "executive"[ti] OR cognition[ti]) AND adolescen*
```

In addition, identifiers were chased by hand out of the reference lists and discussion sections of every full text retrieved — this is how `ramakrishnan2016`, `short2018`, `campbell2017` and `campbell2019` were found, and it is how the Belenky↔UMP↔Banks parameter chain in `notes_for_modeller.md` §10 was assembled.

## Decision counts

| Decision | n | Meaning |
|---|---|---|
| `INCLUDED` | 30 | **Included** — extracted to a YAML record in this shard. |
| `E-NOEXTRACT` | 10 | On topic but contributes no extractable quantity beyond the records already included (usually because full text was unobtainable and the abstract carries no per-arm numbers). Each of these carries an individual note below. |
| `E-DUP` | 2 | Same cohort or protocol as an already-included record; extracting it would double-count a correlated effect. |
| `E-ACUTE` | 6 | Acute exposure only — a single night of restriction, or total sleep deprivation — so it fails the ≥5 consecutive nights criterion that defines this shard's domain. |
| `E-NAP` | 11 | Nap, split-sleep or polyphasic schedule. The exposure structure differs from sustained nocturnal restriction, so the dose is not comparable. |
| `E-MEMORY` | 7 | Memory-consolidation outcome — belongs to `s03_memory_consolidation`. |
| `E-OTHERDOM` | 34 | Outcome lies outside this shard's domain (metabolic, immune, endocrine, cardiovascular, mood-only, EEG-only or imaging-only) and belongs to another shard. |
| `E-OBS` | 23 | Cross-sectional or observational; no experimentally imposed sleep dose. |
| `E-CLIN` | 28 | Clinical or patient population (ADHD, insomnia, psychosis, cancer, autism, bipolar disorder, eczema, sleep apnoea), not healthy volunteers. |
| `E-CASE` | 14 | Case report, narrative review, editorial, book chapter, or consensus/guideline statement — no primary dose-response data. |
| `E-INSTR` | 6 | Instrument, device or measurement-methods paper; yields no dose-response estimate. |
| `E-ANIMAL` | 5 | Animal model (rodent), not human. |
| `E-OFFTOPIC` | 6 | Not about the sleep-restriction dose-response; matched the search terms incidentally. |
| `E-CORR` | 3 | Correction, corrigendum or erratum record. |
| **Total** | **185** | |

## Included records (30)

| PMID | Year | Journal | Title | `study_id` |
|---|---|---|---|---|
| 18533328 | 2008 | Chronobiol Int | Sleepiness and performance in response to repeated sleep restriction and subsequent recovery during semi-laboratory conditions | `axelsson2008` |
| 17803017 | 2007 | J Clin Sleep Med | Behavioral and physiological consequences of sleep restriction | `banks2007` |
| 20815182 | 2010 | Sleep | Neurobehavioral dynamics following chronic sleep restriction: dose-response effects of one night for recovery | `banks2010` |
| 21532951 | 2011 | Sleep | Maximizing sensitivity of the psychomotor vigilance test (PVT) to sleep loss | `basner2011` |
| 12603781 | 2003 | J Sleep Res | Patterns of performance degradation and restoration during sleep restriction and subsequent recovery: a sleep dose-response study | `belenky2003` |
| 28419388 | 2017 | Sleep | Daytime Sleepiness Increases With Age in Early Adolescence: A Sleep Restriction Dose-Response Study | `campbell2017` |
| 30169721 | 2018 | Sleep | Differential and interacting effects of age and sleep restriction on daytime sleepiness and vigilance in adolescence: a longitudinal study | `campbell2019` |
| 39283917 | 2024 | Sleep | Sleep restriction and age effects on distinct aspects of cognition in adolescents | `campbell2024` |
| 20371466 | 2010 | Sci Transl Med | Uncovering residual effects of chronic sleep loss on human performance | `cohen2010` |
| 27039223 | 2017 | Sleep Med Rev | Effects of sleep manipulation on cognitive functioning of adolescents: A systematic review | `debruin2017` |
| 9231952 | 1997 | Sleep | Cumulative sleepiness, mood disturbance, and psychomotor vigilance performance decrements during a week of sleep restricted to 4-5 hours per night | `dinges1997` |
| 38767872 | 2024 | JAMA Neurol | Effect of Sleep Restriction on Adolescent Cognition by Adiposity: A Randomized Crossover Trial | `duraccio2024` |
| 38219041 | 2024 | Sleep | Neurobehavioral functions during recurrent periods of sleep restriction: effects of intra-individual variability in sleep duration | `koa2024` |
| 20438143 | 2010 | Psychol Bull | A meta-analysis of the impact of short-term sleep deprivation on cognitive variables | `lim_dinges2010` |
| 26612392 | 2016 | Sleep | Cognitive Performance, Sleepiness, and Mood in Partially Sleep Deprived Adolescents: The Need for Sleep Study | `lo2016` |
| 28364507 | 2017 | Sleep | Neurobehavioral Impact of Successive Cycles of Sleep Restriction With and Without Naps in Adolescents | `lo2017` |
| 30753648 | 2019 | Sleep | Differential effects of split and continuous sleep on neurobehavioral function and glucose tolerance in sleep-restricted adolescents | `lo2019` |
| 35089345 | 2022 | Sleep | Staying vigilant during recurrent sleep restriction: dose-response effects of time-in-bed and benefits of daytime napping | `lo2022` |
| 28757454 | 2017 | Neurosci Biobehav Rev | The neurocognitive consequences of sleep restriction: A meta-analytic review | `lowe2017` |
| 18938181 | 2009 | J Theor Biol | A new mathematical model for the homeostatic effects of sleep loss on neurobehavioral performance | `mccauley2009` |
| 8776790 | 1996 | Sleep | Effects of sleep deprivation on performance: a meta-analysis | `pilcher1996` |
| 27242464 | 2016 | Front Behav Neurosci | Differential Kinetics in Alteration and Recovery of Cognitive Processes from a Chronic Sleep Restriction in Young Healthy Men | `rabat2016` |
| 23623949 | 2013 | J Theor Biol | A unified mathematical model to quantify performance impairment for both chronic sleep restriction and total sleep deprivation | `rajdev2013` |
| 26518594 | 2016 | Sleep | A Unified Model of Performance: Validation of its Predictions across Different Sleep/Wake Schedules | `ramakrishnan2016` |
| 19294951 | 2009 | Sleep | Banking sleep: realization of benefits during subsequent sleep restriction and recovery | `rupp2009` |
| 29325109 | 2018 | Sleep | Estimating adolescent sleep need using dose-response modeling | `short2018` |
| 33630069 | 2021 | Sleep | Effects of six weeks of chronic sleep restriction with weekend recovery on cognitive performance and wellbeing in high-performing adults | `smith2021` |
| 12683469 | 2003 | Sleep | The cumulative cost of additional wakefulness: dose-response effects on neurobehavioral functions and sleep physiology from chronic sleep restriction and total sleep deprivation | `vandongen2003` |
| 15164894 | 2004 | Sleep | Systematic interindividual differences in neurobehavioral impairment from sleep loss: evidence of trait-like differential vulnerability | `vandongen2004` |
| 33274389 | 2021 | Sleep | Residual, differential neurobehavioral deficits linger after multiple recovery nights following chronic sleep restriction or acute total sleep deprivation | `yamazaki2021` |

## Near-miss exclusions (12) — on topic, individually justified

These are the exclusions most likely to be questioned, so each carries its own reason rather than a category label. Several were excluded **only** because full text could not be obtained; they are the records worth revisiting if the orchestrator has better journal access.

| PMID | Year | Journal | Title | Code | Reason |
|---|---|---|---|---|---|
| 42323045 | 2026 | Biosystems | A unified clearance-based model of homeostatic drive across acute and chronic sleep loss | `E-NOEXTRACT` | Chronic-restriction biomathematical model (2026, Biosystems) - abstract only, no equations or fitted parameters retrievable; the parameterised form in ramakrishnan2016 supersedes it for this shard's purposes |
| 40385325 | 2025 | Sleep Adv | Changes in sleep architecture during recurrent cycles of sleep restriction: a comparison between stable and variable short sleep schedules | `E-DUP` | Sleep architecture across recurrent restriction cycles - same Chee-lab cohort family as lo2022 / koa2024 |
| 37193276 | 2023 | Sleep Adv | Dynamics of recovery sleep from chronic sleep restriction | `E-DUP` | Dynamics of recovery sleep from chronic sleep restriction - same Chee-lab recurrent-restriction cohort family already represented by lo2022 and koa2024 |
| 37193393 | 2022 | Sleep Adv | Predicting vigilance vulnerability during 1 and 2 weeks of sleep restriction with baseline performance metrics | `E-NOEXTRACT` | Predicting vigilance vulnerability from baseline performance during 1-2 weeks of restriction - individual-differences prediction, and the trait-vulnerability evidence is already carried by vandongen2004 |
| 27868260 | 2017 | J Sleep Res | An experimental study of adolescent sleep restriction during a simulated school week: changes in phase, sleep staging, performance and sleepiness | `E-NOEXTRACT` | Short et al. simulated school week in adolescents - on topic and age-matched, but full text is paywalled at Wiley with no OA copy and the abstract reports no per-arm numbers; the same group's dose-response study (PMID 29325109) is included instead |
| 28123662 | 2016 | Sleep Sci | Sleep restriction may lead to disruption in physiological attention and reaction time | `E-NOEXTRACT` | Small uncontrolled study of restriction, attention and reaction time; no usable dose contrast or dispersion reported |
| 24602612 | 2014 | J Adolesc Health | The effects of sleep restriction on executive inhibitory control and affect in young adults | `E-NOEXTRACT` | Sleep restriction, executive inhibitory control and affect in young adults - short exposure, no dose ladder, no retrievable per-arm data |
| 23523432 | 2013 | Sleep Med | The effects of sleep extension on sleep and cognitive performance in adolescents with chronic sleep reduction: an experimental study | `E-NOEXTRACT` | Sleep extension in adolescents with chronic sleep reduction; extension arm only, no restriction dose ladder |
| 21950514 | 2011 | J Clin Exp Neuropsychol | Effect of chronic sleep restriction on sleepiness and working memory in adolescents and young adults | `E-NOEXTRACT` | Chronic restriction, sleepiness and working memory in adolescents AND young adults (J Clin Exp Neuropsychol 2011) - on topic and age-matched, but paywalled with no OA copy and no per-arm numbers in the abstract |
| 20681233 | 2010 | Aviat Space Environ Med | Time of day effects on neurobehavioral performance during chronic sleep restriction | `E-NOEXTRACT` | Time-of-day effects on neurobehavioural performance during chronic restriction - time-of-day modifier only, no dose ladder; the same modifier is captured in rabat2016 and campbell2019 |
| 18484365 | 2008 | Chronobiol Int | Effects of context on sleepiness self-ratings during repeated partial sleep deprivation | `E-NOEXTRACT` | Context effects on sleepiness self-ratings during repeated partial deprivation - same Axelsson cohort already included as axelsson2008 |
| 6111825 | 1981 | Psychophysiology | Cumulative effects of sleep restriction on daytime sleepiness | `E-NOEXTRACT` | Carskadon & Dement 1981, the original cumulative-restriction paper (Psychophysiology) - PubMed carries no abstract, the article predates electronic full text and no OA copy exists; its cumulative-sleepiness finding is carried secondhand in banks2007 |

## All other exclusions, grouped by reason

### `E-ACUTE` — 6 records

Acute exposure only — a single night of restriction, or total sleep deprivation — so it fails the ≥5 consecutive nights criterion that defines this shard's domain.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 41431161 | 2026 | J Sleep Res | Acute Effects of Sleep Extension on Fatigue, Inhibitory Control, Short-Term Vigilance and Neuromuscular Function in Youth Elite Ice Hockey Players: A Randomised Crossover Trial — Acute sleep extension, single intervention - not sustained restriction |
| 40222592 | 2025 | Neurobiol Learn Mem | Memory impairments observed after a half night sleep restriction are not mediated by working memory, attention, or inhibitory control mechanisms — Half-night restriction, single night |
| 34557048 | 2021 | Nat Sci Sleep | Impaired Vigilant Attention Partly Accounts for Inhibition Control Deficits After Total Sleep Deprivation and Partial Sleep Restriction — Total sleep deprivation only |
| 30425658 | 2018 | Front Psychiatry | Acute Sleep Restriction Has Differential Effects on Components of Attention — Acute restriction, differential effects on components of attention - single night |
| 15648465 | 2004 | Percept Mot Skills | Performance on a dual driving simulation and subtraction task following sleep restriction — Dual driving simulation and subtraction after acute restriction |
| 11693688 | 2001 | Percept Mot Skills | Effects of acute sleep restriction on behavior, sustained attention, and response inhibition in children — Acute restriction in children - single night, and below the age band |

### `E-NAP` — 11 records

Nap, split-sleep or polyphasic schedule. The exposure structure differs from sustained nocturnal restriction, so the dose is not comparable.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 41641962 | 2026 | Sleep | Neurobehavioral functions and sleep architecture during polyphasic and monophasic short sleep schedules — Polyphasic vs monophasic short sleep schedules - different exposure structure |
| 41757514 | 2026 | Sleep | Cheating hypnos: can polyphasic sleep schedules reduce the need for sleep? |
| 39965883 | 2025 | J Sports Sci | Enhanced physical performance, attention, and mood states after a nap opportunity following a sleep restriction night in female athletes: A randomized controlled trial — Nap opportunity after a single night of restriction |
| 35090173 | 2022 | Sleep | A sleep schedule incorporating naps benefits the transformation of hierarchical knowledge |
| 36041284 | 2022 | Sleep Med Rev | Systematic review and meta-analyses on the effects of afternoon napping on cognition — Meta-analysis of afternoon napping - different exposure structure |
| 33313925 | 2021 | Sleep | Memory performance following napping in habitual and non-habitual nappers |
| 33674679 | 2021 | Sci Rep | Splitting sleep between the night and a daytime nap reduces homeostatic sleep pressure and enhances long-term memory |
| 32619240 | 2020 | Sleep | Cognitive effects of split and continuous sleep schedules in adolescents differ according to total sleep opportunity — Split versus continuous sleep schedules in adolescents by total sleep opportunity - split-sleep exposure structure; the continuous arms duplicate the Lo cohort family already included |
| 30715485 | 2019 | Sleep | A split sleep schedule rescues short-term topographical memory after multiple nights of sleep restriction |
| 31285846 | 2019 | NPJ Sci Learn | Does splitting sleep improve long-term memory in chronically sleep deprived adolescents? |
| 28934525 | 2017 | Sleep | Short Daytime Naps Briefly Attenuate Objectively Measured Sleepiness Under Chronic Sleep Restriction — Short daytime naps under chronic restriction in adolescents |

### `E-MEMORY` — 7 records

Memory-consolidation outcome — belongs to `s03_memory_consolidation`.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 41943473 | 2026 | J Biol Rhythms | Overnight Motor Memory Consolidation in Adolescents: Effects of Change in Dim Light Melatonin Onset After Sleep Restriction |
| 40934018 | 2025 | Sleep Adv | Sleep restriction impairs item memory discrimination but not general recognition in young adolescents |
| 37193282 | 2023 | Sleep Adv | Advantage conferred by overnight sleep on schema-related memory may last only a day |
| 31303555 | 2019 | J Adolesc Health | Multi-Night Sleep Restriction Impairs Long-Term Retention of Factual Knowledge in Adolescents |
| 28677325 | 2018 | J Sleep Res | Memory encoding is impaired after multiple nights of partial sleep restriction |
| 27137944 | 2016 | PLoS Biol | Cued Reactivation of Motor Learning during Sleep Leads to Overnight Changes in Functional Brain Activity and Connectivity |
| 25174663 | 2014 | Neuropsychologia | Time- but not sleep-dependent consolidation promotes the emergence of cross-modal conceptual representations |

### `E-OTHERDOM` — 34 records

Outcome lies outside this shard's domain (metabolic, immune, endocrine, cardiovascular, mood-only, EEG-only or imaging-only) and belongs to another shard.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 41165770 | 2026 | Sleep | Glucose homeostasis during recurrent periods of sleep restriction and recovery in healthy young adults — Glucose homeostasis during recurrent restriction - metabolic outcome, belongs to s07_metabolic |
| 41206488 | 2026 | Sleep | Sleep restriction increases reward sensitivity during sequential updating — Reward sensitivity during sequential updating under restriction |
| 41730935 | 2026 | Sci Rep | Late evening room light and sleep restriction reduces the ability of bright morning light to phase advance adolescents' circadian clocks — Evening light and restriction on circadian phase shifting |
| 41825204 | 2026 | Clin Nutr | Adolescent sleep restriction, macronutrient consumption, and self-reported hunger: A randomized clinical trial — Adolescent restriction, macronutrients and hunger - belongs to s09_obesity_bmi |
| 42330816 | 2026 | Sleep Med | Distal skin temperature stabilization is tightly coupled with sleep onset across structured and free-living conditions — Distal skin temperature and sleep onset - physiological outcome |
| 39325824 | 2025 | Sleep | Effects of night-to-night variations in objectively measured sleep on blood glucose in healthy university students |
| 40934020 | 2025 | Sleep Adv | Experimentally induced sleep restriction relates to less healthy eating behaviors in some adolescents: effects of age, sex, race, weight class, and socioeconomic status — Eating behaviours under induced restriction in adolescents - belongs to s09_obesity_bmi |
| 36805763 | 2024 | Sleep | Altered neuronal response to visual food stimuli in adolescents undergoing chronic sleep restriction — fMRI response to food stimuli under chronic restriction in adolescents |
| 37798133 | 2024 | Sleep | Maturational trend of daytime sleep propensity in adolescents — Maturational trend of daytime sleep propensity - normative sleepiness, same Campbell cohort family |
| 38602131 | 2024 | Sleep | The dynamic responses of mood and sleep physiology to chronic sleep restriction and subsequent recovery sleep — Mood and sleep physiology responses to chronic restriction - mood and PSG outcomes, not objective neurobehavioural performance |
| 39546870 | 2024 | Sleep Med | The impact of sleep restriction on cerebrovascular reactivity and cognitive outcomes in healthy adolescents: A pilot crossover trial — Cerebrovascular reactivity and cognition - vascular outcome primary |
| 36916319 | 2023 | Sleep | Sleep restriction effects on sleep spindles in adolescents and relation of these effects to subsequent daytime sleepiness and cognition — Sleep spindles under restriction in adolescents - EEG outcome |
| 37469985 | 2023 | Front Endocrinol (Lausanne) | Social jetlag is associated with adverse cardiometabolic latent traits in early adolescence: an observational study |
| 37536212 | 2023 | Sleep Med | Development of evening sleep homeostatic pressure in early adolescent boys — Development of evening sleep homeostatic pressure in early adolescent boys - EEG homeostatic outcome |
| 34379782 | 2022 | Sleep | Cortical thinning and sleep slow wave activity reductions mediate age-related improvements in cognition during mid-late adolescence — Cortical thinning and slow-wave activity mediating age-related change - brain-structure outcome |
| 35218665 | 2022 | Sleep | Impact of chronic sleep restriction on sleep continuity, sleep structure, and neurobehavioral performance — Chronic restriction effects on sleep continuity and sleep structure; the neurobehavioural component duplicates cohorts already included |
| 35669317 | 2022 | Sleep Adv | Sleep restriction and age effects on waking alpha EEG activity in adolescents — Waking alpha EEG under restriction in adolescents - EEG outcome |
| 36062257 | 2022 | Front Behav Neurosci | Contrasting Effects of Sleep Restriction, Total Sleep Deprivation, and Sleep Timing on Positive and Negative Affect — Restriction, deprivation and sleep timing on positive/negative affect - mood outcome |
| 33245773 | 2021 | Sleep | Sleep duration and mood in adolescents: an experimental study — Sleep duration and mood in adolescents - mood outcome |
| 33507305 | 2021 | Sleep | Effects of sleep restriction on the sleep electroencephalogram of adolescents — Sleep EEG under restriction in adolescents - EEG outcome |
| 33615598 | 2021 | J Sleep Res | Neuronal activation and performance changes in working memory induced by chronic sleep restriction in adolescents — fMRI neuronal activation during working memory under chronic restriction - imaging outcome, belongs with the brain-structure/imaging evidence |
| 33893807 | 2021 | Sleep | Homeostatic response to sleep restriction in adolescents — Homeostatic (EEG) response to restriction in adolescents |
| 31874181 | 2020 | Physiol Behav | A sleep intervention study comparing effects of sleep restriction and fragmentation on sleep and vigilance and the need for recovery — Restriction versus fragmentation, sleep and mood outcomes |
| 32146167 | 2020 | Sleep Health | The roles of repetitive negative thinking and perfectionism in explaining the relationship between sleep onset difficulties and depressed mood in adolescents |
| 32240932 | 2020 | Sleep Med Rev | The relationship between sleep duration and mood in adolescents: A systematic review and meta-analysis |
| 30668606 | 2019 | PLoS One | Shorter sleep durations in adolescents reduce power density in a wide range of waking electroencephalogram frequencies — Waking EEG power under shorter sleep in adolescents - EEG outcome |
| 31096123 | 2019 | Sleep Med | Effects of sleep extension on cognitive/motor performance and motivation in military tactical athletes — Sleep extension in military athletes; outcome is motor performance and motivation, and exposure is extension not restriction |
| 29783103 | 2018 | J Adolesc | Sleep spindles and cognitive performance across adolescence: A meta-analytic review |
| 30056287 | 2018 | Sleep Med | Sleep spindles in adolescence: a comparison across sleep restriction and sleep extension |
| 30216577 | 2018 | J Neuroendocrinol | Variability of the cortisol awakening response and morning salivary oxytocin in late adolescence — Cortisol awakening response and salivary oxytocin - endocrine outcome |
| 27397569 | 2016 | Sleep | Restricting Time in Bed in Early Adolescence Reduces Both NREM and REM Sleep but Does Not Increase Slow Wave EEG — TIB restriction reduces NREM and REM sleep in early adolescence - sleep architecture outcome from the same Campbell cohort already included |
| 22116514 | 2012 | Am J Physiol Regul Integr Comp Physiol | The maturational trajectories of NREM and REM sleep durations differ across adolescence on both school-night and extended sleep — Maturational trajectories of NREM and REM durations - normative architecture |
| 22140557 | 2011 | PLoS One | Temporal dissociation between myeloperoxidase (MPO)-modified LDL and MPO elevations during chronic sleep restriction and recovery in healthy young men |
| 18246977 | 2007 | Sleep | The increase in longitudinally measured sleepiness across adolescence is related to the maturational decline in low-frequency EEG power — Longitudinal sleepiness and maturational EEG decline - same Campbell cohort family, EEG outcome |

### `E-OBS` — 23 records

Cross-sectional or observational; no experimentally imposed sleep dose.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 41084944 | 2026 | J Sleep Res | Sleep Reactivity Amplifies the Impact of Pre-Sleep Cognitive Arousal on Sleep Disturbances |
| 41309418 | 2026 | Sleep Health | Changes in sleep from adolescence to young adulthood: Findings from the Eating and Activity over Time 2010-2018 Study |
| 40035495 | 2025 | Behav Sleep Med | No Earlier Than 9:45 A.M. A Qualitative Study of Adolescents' Experiences of Later School Start Times in Aotearoa New Zealand |
| 40159406 | 2025 | Sleep Breath | The yin and yang of sleep-wake regulation: gender gap in need for sleep persists across the human lifespan |
| 40488416 | 2025 | Sleep | A longitudinal study of sleep in university freshmen: facilitating and impeding factors |
| 41056215 | 2025 | PLoS Biol | Identification of five sleep-biopsychosocial profiles with specific neural signatures linking sleep variability with health, cognition, and lifestyle factors |
| 38366364 | 2024 | Sleep | Keeping the balance: the benefits of catch-up sleep versus the risks of sleep irregularity — Catch-up sleep versus sleep irregularity - observational |
| 38938171 | 2024 | Sleep | Bidirectional associations between the duration and timing of nocturnal sleep and daytime naps in adolescents differ from weekdays to weekends |
| 36528521 | 2023 | J Adolesc Health | Adherence to 24-Hour Movement Recommendations and Health Indicators in Early Adolescence: Cross-Sectional and Longitudinal Associations in the Adolescent Brain Cognitive Development Study |
| 36707974 | 2023 | J Sleep Res | Fetal and infant growth patterns, sleep, and 24-h activity rhythms: a population-based prospective cohort study in school-age children |
| 37305962 | 2023 | Pediatrics | Earlier Bedtime and Its Effect on Adolescent Sleep Duration — Earlier bedtime intervention effect on adolescent sleep duration - exposure is bedtime advance, outcome is sleep duration not cognition |
| 33322992 | 2022 | J Appl Gerontol | Prevalent Insomnia Concerns and Perceived Need for Sleep Intervention Among Direct-Care Workers in Long-Term Care |
| 33544942 | 2022 | Health Promot J Austr | The need for sleep and circadian education in Australian high schools: incidental results from a survey of university students |
| 35942298 | 2022 | Prev Med Rep | Identifying modifiable obesogenic behaviors among Latino adolescents in primary pediatric care |
| 36272919 | 2022 | Sleep Health | Bedtime procrastination and chronotype differentially predict adolescent sleep on school nights and non-school nights |
| 33991891 | 2021 | Sleep Med | Chronic sleep restriction triggers inadequate napping habits in adolescents: a population-based study — Population-based survey of adolescent napping habits |
| 30649545 | 2019 | Sleep | Sleep duration and cognition: is there an ideal amount? — Sleep duration and cognition, ideal-amount analysis - observational |
| 31150946 | 2019 | Sleep Med | How internal and external cues for bedtime affect sleep and adaptive functioning in adolescents — Internal versus external bedtime cues and adaptive functioning - observational |
| 29934128 | 2018 | Sleep Med Rev | Sleep duration and risk-taking in adolescents: A systematic review and meta-analysis — Systematic review and meta-analysis of sleep duration and risk-taking - observational exposure and a non-neurobehavioural outcome |
| 30212878 | 2018 | Sleep | Dissociable effects of self-reported daily sleep duration on high-level cognitive abilities — Self-reported daily sleep duration and high-level cognition - observational, no experimental dose |
| 28243156 | 2017 | Nat Sci Sleep | An investigation of the longitudinal relationship between sleep and depressed mood in developing teens — Longitudinal association of sleep with depressed mood - observational, and a mood outcome |
| 28525634 | 2017 | Sleep | Association Between Weekend Catch-up Sleep and Lower Body Mass: Population-Based Study |
| 22851809 | 2012 | Sleep | Deterioration of neurobehavioral performance in resident physicians during repeated exposure to extended duration work shifts — Resident physicians on extended-duration work shifts - occupational exposure, not a controlled restriction dose |

### `E-CLIN` — 28 records

Clinical or patient population (ADHD, insomnia, psychosis, cancer, autism, bipolar disorder, eczema, sleep apnoea), not healthy volunteers.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 41125743 | 2026 | Mol Psychiatry | Structural covariance network topology in individuals at clinical high risk for psychosis: the ENIGMA-CHR Study |
| 41177928 | 2026 | Pediatr Blood Cancer | The Association of Sleep Quality, Sociodemographic, and Disease-Related Factors in Youth Living With Sickle Cell Disease |
| 42054261 | 2026 | Horm Res Paediatr | US Adolescents of Asian Ethnicity Have Higher Risk of Polycystic Ovary Syndrome |
| 42153457 | 2026 | J Child Neurol | Mania in Juvenile Neuronal Ceroid Lipofuscinosis (CLN3 Disease): A Rare Neuropsychiatric Presentation in an Adolescent |
| 39419235 | 2025 | Am J Prev Med | Hypertensive Blood Pressure in Adolescent Females With Polycystic Ovary Syndrome |
| 40113374 | 2025 | Am J Prev Med | Response to "Hypertensive Blood Pressure in Adolescent Girls With Features of PCOS" |
| 40406966 | 2025 | Pediatr Dermatol | Racial and Ethnic Differences in the Burden of Alopecia Areata in Contemporary Pediatric Practice |
| 40583576 | 2025 | Diabetes Care | High Prevalence of Prediabetes Among Asian and Pacific Islander Adolescents With Overweight or Obesity in a Primary Care Population |
| 40583752 | 2025 | East Asian Arch Psychiatry | Youth mental health services in Hong Kong: evidence, interconnectedness, and challenges |
| 40986731 | 2025 | Gastroenterol Nurs | Gastrointestinal and Sleep Disorders in Children With and Without Autism |
| 38018135 | 2024 | Psychol Med | Childhood abuse v. neglect and risk for major psychiatric disorders |
| 38231515 | 2024 | JAMA Netw Open | Hemoglobin A1c and Type 2 Diabetes Incidence Among Adolescents With Overweight and Obesity |
| 38444225 | 2024 | Pediatr Obes | Alanine aminotransferase elevation varies by ethnicity among Asian and Pacific Islander children with overweight or obesity |
| 38852279 | 2024 | Transl Oncol | Exosomal mRNA Cargo are biomarkers of tumor and immune cell populations in pediatric osteosarcoma |
| 36111359 | 2023 | J Clin Sleep Med | Snoring was related to self-reported daytime sleepiness and tiredness in young adults performing compulsory conscript service |
| 36173066 | 2023 | Curr Neuropharmacol | Sleep Disturbance, Irritability, and Response to Lurasidone Treatment in Children and Adolescents with Bipolar Depression |
| 37084344 | 2023 | J Pediatr Gastroenterol Nutr | Prevalence of Elevated ALT in Adolescents in the US 2011-2018 |
| 37517174 | 2023 | Asian J Psychiatr | Primary health level screening for postpartum depression during well-child visits: Prevalence, associated risk factors, and breastfeeding |
| 35205674 | 2022 | Cancers (Basel) | Prevalence of Sleep Disorders, Risk Factors and Sleep Treatment Needs of Adolescents and Young Adult Childhood Cancer Patients in Follow-Up after Treatment |
| 35596599 | 2022 | J Pediatr Endocrinol Metab | Ethnic diversity and burden of polycystic ovary syndrome among US adolescent females |
| 35882855 | 2022 | Transl Psychiatry | Neuroanatomical heterogeneity and homogeneity in individuals at clinical high risk for psychosis |
| 33314496 | 2021 | J Sleep Res | The acute effects of sleep restriction therapy for insomnia on circadian timing and vigilance — Sleep restriction therapy for insomnia - clinical intervention in patients |
| 32157691 | 2020 | J Child Psychol Psychiatry | Impact of sleep restriction on affective functioning in adolescents with attention-deficit/hyperactivity disorder |
| 30768404 | 2019 | J Am Acad Child Adolesc Psychiatry | Shortened Sleep Duration Causes Sleepiness, Inattention, and Oppositionality in Adolescents With Attention-Deficit/Hyperactivity Disorder: Findings From a Crossover Sleep Restriction/Extension Study — Adolescents with ADHD - clinical population |
| 31257931 | 2019 | Chronobiol Int | Decreased need for sleep as an endophenotype of bipolar disorder: an actigraphy study |
| 29773219 | 2018 | Sleep Med | An open trial of bedtime fading for sleep disturbances in preschool children: a parent group education approach — Open trial of bedtime fading for sleep disturbance in preschool children - clinical intervention, wrong age band |
| 28802380 | 2017 | Int J Pediatr Otorhinolaryngol | Can telemetry data obviate the need for sleep studies in Pierre Robin Sequence? |
| 27823708 | 2016 | Sleep Med | Thermoregulation, scratch, itch and sleep deficits in children with eczema — Children with eczema - clinical population, sleep deficit is a consequence not an imposed dose |

### `E-CASE` — 14 records

Case report, narrative review, editorial, book chapter, or consensus/guideline statement — no primary dose-response data.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 32644337 | 2026 |  | Mood Disorder |
| 41322726 | 2025 | Cureus | Transient Psychotic Symptoms Induced by Acute Sleep Deprivation in a Factory Worker: A Case Report |
| 38149645 | 2024 | J Clin Sleep Med | Recommended protocols for the Multiple Sleep Latency Test and Maintenance of Wakefulness Test in children: guidance from the American Academy of Sleep Medicine |
| 38283846 | 2024 | Front Psychiatry | Case report: Periventricular heterotopia and early-onset bipolar disorder in adolescent patient with history of childhood attention deficit hyperactivity disorder |
| 38387329 | 2024 | Neurophysiol Clin | Long sleep time and excessive need for sleep: State of the art and perspectives |
| 38975397 | 2024 | Cureus | Elevated Cortisol Levels and Manic Symptoms in a 16-Year-Old Female: A Case Report |
| 35961036 | 2023 | Annu Rev Psychol | Understanding the Need for Sleep to Improve Cognition |
| 37974686 | 2023 | Indian J Otolaryngol Head Neck Surg | Underlining the Need for Sleep Medicine and Surgery as a Separate Postgraduate Branch |
| 34220667 | 2021 | Front Neurol | The Fundamental Need for Sleep in Neurocritical Care Units: Time for a Paradigm Shift |
| 30295966 | 2020 | Eur J Neurosci | Tired and stressed: Examining the need for sleep |
| 31780247 | 2020 | Trends Cogn Sci | The Need for Sleep in the Adolescent Brain |
| 31072562 | 2019 | Prog Brain Res | The impact of sleep deprivation on declarative memory |
| 31072563 | 2019 | Prog Brain Res | Adolescent sleep restriction effects on cognition and mood — Narrative review chapter (Prog Brain Res) on adolescent sleep restriction effects on cognition and mood - no primary data; its primaries are already extracted here |
| 29213138 | 2018 | Nat Rev Neurosci | Sleep: I feel the need, the need for sleep |

### `E-INSTR` — 6 records

Instrument, device or measurement-methods paper; yields no dose-response estimate.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 38087674 | 2024 | Sleep Health | Selecting a sleep tracker from EEG-based, iteratively improved, low-cost multisensor, and actigraphy-only devices |
| 37193407 | 2022 | Sleep Adv | Ultra-short objective alertness assessment: an adaptive duration version of the 3 minute PVT (PVT-BA) accurately tracks changes in psychomotor vigilance induced by sleep restriction |
| 33623459 | 2021 | Nat Sci Sleep | Multi-Night Validation of a Sleep Tracking Ring in Adolescents Compared with a Research Actigraph and Polysomnography |
| 29736916 | 2019 | J Sleep Res | Reliability of sleep spindle measurements in adolescents: How many nights are necessary? — Reliability of sleep-spindle measurement across nights - methods paper |
| 31538605 | 2019 | J Clin Sleep Med | Validation of a Consumer Sleep Wearable Device With Actigraphy and Polysomnography in Adolescents Across Sleep Opportunity Manipulations |
| 28199718 | 2017 | Sleep | How Many Sleep Diary Entries Are Needed to Reliably Estimate Adolescent Sleep? — How many sleep-diary entries are needed to estimate adolescent sleep - measurement-reliability methods paper |

### `E-ANIMAL` — 5 records

Animal model (rodent), not human.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 38659740 | 2024 | bioRxiv | Adolescent chronic sleep restriction promotes alcohol drinking in adulthood: evidence from epidemiological and preclinical data |
| 38991453 | 2024 | J Neuroimmunol | Geraniol (GER) attenuated chronic sleep restriction (CSR)-induced neuroinflammation in adolescent mice |
| 39188806 | 2024 | Front Neurosci | Chronic sleep restriction during juvenility alters hedonic and anxiety-like behaviours in a sex-dependent fashion in adolescent Wistar rats |
| 33268891 | 2021 | Nature | Availability of food determines the need for sleep in memory consolidation |
| 31379490 | 2019 | Front Neurosci | Gating and the Need for Sleep: Dissociable Effects of Adenosine A(1) and A(2A) Receptors |

### `E-OFFTOPIC` — 6 records

Not about the sleep-restriction dose-response; matched the search terms incidentally.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 37004704 | 2023 | Acta Neurol Belg | Assessing the impact of sleep restriction on the attention and executive functions of medical students: a prospective cohort study — Medical students' attention and executive function - uncontrolled occupational exposure, not an experimental dose |
| 37193396 | 2022 | Sleep Adv | Low-intensity scheduled morning exercise for adolescents with a late chronotype: a novel treatment to advance circadian phase? — Scheduled morning exercise for late chronotype adolescents - exercise/circadian intervention, not a sleep dose |
| 33373678 | 2021 | Prog Neuropsychopharmacol Biol Psychiatry | Coffee effectively attenuates impaired attention in ADORA2A C/C-allele carriers during chronic sleep restriction — Coffee/ADORA2A genotype countermeasure during chronic restriction - exposure confounded with a stimulant by design |
| 34022854 | 2021 | BMC Musculoskelet Disord | The effects of combined motor control and isolated extensor strengthening versus general exercise on paraspinal muscle morphology and function in patients with chronic low back pain: a randomised controlled trial protocol |
| 27546185 | 2017 | Sleep Med Rev | Can exercise regulate the circadian system of adolescents? Novel implications for the treatment of delayed sleep-wake phase disorder — Systematic review of exercise as a circadian regulator in adolescents - exposure is exercise, not sleep dose |
| 29029309 | 2017 | Sleep | Limited Efficacy of Caffeine and Recovery Costs During and Following 5 Days of Chronic Sleep Restriction — Caffeine countermeasure study during 5 days of restriction; the exposure is confounded with a stimulant intervention by design |

### `E-CORR` — 3 records

Correction, corrigendum or erratum record.

| PMID | Year | Journal | Title |
|---|---|---|---|
| 37193269 | 2023 | Sleep Adv | Correction |
| 37193285 | 2023 | Sleep Adv | Correction to: Ultra-short objective alertness assessment: an adaptive duration version of the 3 minute PVT (PVT-BA) accurately tracks changes in psychomotor vigilance induced by sleep restriction |
| 37939437 | 2023 | Asian J Psychiatr | Corrigendum to "Primary health level screening for postpartum depression during well-child visits: Prevalence, associated risk factors, and breastfeeding" [Asian J. Psychiatry 87 (2023) 103701] |

