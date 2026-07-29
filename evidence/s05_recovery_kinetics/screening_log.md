# Screening log - shard `s05_recovery_kinetics`

**Domain screened:** what happens when a chronically sleep-restricted person starts sleeping more - recovery-sleep dose-response, sleep-debt repayment, recovery time constants, measures that fail to recover, weekend catch-up sufficiency, sleep extension in habitual short sleepers, and whether sleep need itself changes after chronic restriction.

| | Count |
|---|---:|
| Records screened (unique PMIDs) | **313** |
| Included (one YAML record each) | **30** |
| Excluded | **283** |
| PubMed queries run | 22 |
| Identifiers that failed verification | **0** |

The spec requires at least 25 records screened; this shard screened 313. Every DOI and PMID attached to an included record was verified programmatically against Crossref and PubMed E-utilities before the record was written, and all 30 resolved to the expected title. No identifier failed, so no record required `access_tier: secondhand`.

## Search strategy

Two sweeps. The first used natural-language queries; these under-returned because PubMed ANDs bare keywords, so the second sweep used field-tagged boolean queries with `[tiab]` restrictions. Five further records were found outside the sweeps - one named in the task brief and four by chasing citations out of included papers - and they are flagged in the route column of the inclusion table.

### Sweep 1 - natural-language queries

- `sleep restriction recovery sleep neurobehavioral dose response`
- `sleep extension habitual short sleepers randomized weeks`
- `weekend catch-up sleep metabolic randomized`
- `recovery sleep after chronic sleep restriction adolescents`
- `sleep debt repayment recovery nights performance`
- `maximal sleep capacity sleep extension asymptote`
- `sleep banking prophylactic sleep extension`
- `multiple nights recovery sleep incomplete performance`
- `sleep extension trial insulin sensitivity short sleepers`
- `catch-up sleep blood pressure inflammation recovery`

### Sweep 2 - field-tagged boolean queries

- `("sleep restriction"[tiab] AND "recovery"[tiab] AND (performance[tiab] OR vigilance[tiab] OR "psychomotor"[tiab]))`
- `("sleep extension"[tiab] OR "extended sleep"[tiab]) AND (randomized[tiab] OR trial[tiab] OR intervention[tiab])`
- `("catch-up sleep"[tiab] OR "weekend recovery sleep"[tiab] OR "weekend catch"[tiab])`
- `("sleep debt"[tiab] AND (recovery[tiab] OR repay*[tiab] OR extension[tiab]))`
- `("recovery sleep"[tiab] AND ("chronic sleep restriction"[tiab] OR "partial sleep deprivation"[tiab]))`
- `("sleep need"[tiab] AND ("sleep extension"[tiab] OR asymptot*[tiab] OR "maximal"[tiab]))`
- `(adolescen*[tiab] AND "sleep restriction"[tiab] AND recovery[tiab])`
- `("sleep opportunity"[tiab] AND (16-h[tiab] OR "16 h"[tiab] OR extended[tiab]) AND (young[tiab] OR older[tiab]))`
- `("insufficient sleep"[tiab] AND recovery[tiab] AND (insulin[tiab] OR metabolic[tiab] OR glucose[tiab]))`
- `("sleep restriction"[tiab] AND recovery[tiab] AND (interleukin[tiab] OR "IL-6"[tiab] OR cortisol[tiab] OR inflammat*[tiab]))`
- `("social jetlag"[tiab] AND (weekend[tiab] OR catch[tiab]))`
- `("sleep restriction"[tiab] AND ("13 days"[tiab] OR "12 days"[tiab] OR "seven days of recovery"[tiab] OR "week of recovery"[tiab]))`

## Included records (30)

| PMID | Journal | Year | Title | study_id | Discovery route |
|---|---|---|---|---|---|
| 29381788 | Am J Clin Nutr | 2018 | Sleep extension is a feasible lifestyle intervention in free-living adults who are habitually short sleepers: a potential strategy for decreasing intake of free sugars? A randomized controlled pilot study. | `alkhatib2018` | PubMed sweep |
| 18533328 | Chronobiol Int | 2008 | Sleepiness and performance in response to repeated sleep restriction and subsequent recovery during semi-laboratory conditions. | `axelsson2008` | PubMed sweep |
| 20815182 | Sleep | 2010 | Neurobehavioral dynamics following chronic sleep restriction: dose-response effects of one night for recovery. | `banks2010` | PubMed sweep |
| 23992480 | J Sleep Res | 2014 | Actigraphy-assessed sleep during school and vacation periods: a naturalistic study of restricted and extended sleep opportunities in adolescents. | `bei2014` | PubMed sweep |
| 12603781 | J Sleep Res | 2003 | Patterns of performance degradation and restoration during sleep restriction and subsequent recovery: a sleep dose-response study. | `belenky2003` | PubMed sweep |
| 29631192 | Conscious Cogn | 2018 | Daytime microsleeps during 7 days of sleep restriction followed by 13 days of sleep recovery in healthy young adults. | `bougard2018` | PubMed sweep |
| 41848057 | Sleep | 2026 | Transcriptomic recovery and persistence patterns reveal the biological cost of sleep debt in healthy adult males. | `cheng2026` | PubMed sweep |
| 20371466 | Sci Transl Med | 2010 | Uncovering residual effects of chronic sleep loss on human performance. | `cohen2010` | CITATION-CHASE (from Banks 2010 / Yamazaki 2021 discussion) |
| 30827911 | Curr Biol | 2019 | Ad libitum Weekend Recovery Sleep Fails to Prevent Metabolic Dysregulation during a Repeating Pattern of Insufficient Sleep and Weekend Recovery Sleep. | `depner2019` | PubMed sweep |
| 38602131 | Sleep | 2024 | The dynamic responses of mood and sleep physiology to chronic sleep restriction and subsequent recovery sleep. | `jones2024` | PubMed sweep |
| 25683266 | Clin Endocrinol (Oxf) | 2015 | Metabolic and hormonal effects of 'catch-up' sleep in men with chronic, repetitive, lifestyle-driven sleep restriction. | `killick2015` | PubMed sweep |
| 27775095 | Sci Rep | 2016 | Estimating individual optimal sleep duration and potential sleep debt. | `kitamura2016` | PubMed sweep |
| 16295210 | Sleep | 2005 | Interindividual variation in sleep duration and its association with sleep debt in young adults. | `klerman2005` | PubMed sweep |
| 18656358 | Curr Biol | 2008 | Age-related reduction in the maximal capacity for sleep-implications for insomnia. | `klerman2008` | CITATION-CHASE (cited by Kitamura 2016 for the 8.9 h asymptote) |
| 25348128 | Sleep | 2015 | Beneficial impact of sleep extension on fasting insulin sensitivity in adults with habitual sleep restriction. | `leproult2015` | CITATION-CHASE (from Al Khatib 2018 / Tasali 2022) |
| 35089345 | Sleep | 2022 | Staying vigilant during recurrent sleep restriction: dose-response effects of time-in-bed and benefits of daytime napping. | `lo2022` | PubMed sweep |
| 24482677 | PLoS One | 2014 | Sleep extension improves neurocognitive functions in chronically sleep-deprived obese individuals. | `lucassen2014` | PubMed sweep |
| 33571888 | Sleep Med Rev | 2021 | The feasibility of at-home sleep extension in adolescents and young adults: A meta-analysis and systematic review. | `niu2021` | PubMed sweep |
| 34469434 | PLoS One | 2021 | Observing changes in human functioning during induced sleep deficiency and recovery periods. | `ochab2021` | TARGETED (named in task brief) |
| 23941878 | Am J Physiol Endocrinol Metab | 2013 | Effects of recovery sleep after one work week of mild sleep restriction on interleukin-6 and cortisol secretion and daytime sleepiness and performance. | `pejovic2013` | PubMed sweep |
| 27242464 | Front Behav Neurosci | 2016 | Differential Kinetics in Alteration and Recovery of Cognitive Processes from a Chronic Sleep Restriction in Young Healthy Men. | `rabat2016` | PubMed sweep |
| 19294951 | Sleep | 2009 | Banking sleep: realization of benefits during subsequent sleep restriction and recovery. | `rupp2009` | PubMed sweep |
| 18533327 | Chronobiol Int | 2008 | Recovery of cognitive performance from sleep debt: do a short rest pause and a single recovery night help? | `sallinen2008` | PubMed sweep |
| 29325109 | Sleep | 2018 | Estimating adolescent sleep need using dose-response modeling. | `short2018` | PubMed sweep |
| 27263430 | Brain Behav Immun | 2016 | Repeating patterns of sleep restriction and recovery: Do we get used to it? | `simpson2016` | PubMed sweep |
| 29722893 | Sleep | 2018 | Response to chronic sleep restriction, extension, and subsequent total sleep deprivation in humans: adaptation or preserved sleep homeostasis? | `skorucak2018` | PubMed sweep |
| 33630069 | Sleep | 2021 | Effects of six weeks of chronic sleep restriction with weekend recovery on cognitive performance and wellbeing in high-performing adults. | `smith2021` | PubMed sweep |
| 35129580 | JAMA Intern Med | 2022 | Effect of Sleep Extension on Objectively Assessed Energy Intake Among Adults With Overweight in Real-life Settings: A Randomized Clinical Trial. | `tasali2022` | PubMed sweep |
| 33274389 | Sleep | 2021 | Residual, differential neurobehavioral deficits linger after multiple recovery nights following chronic sleep restriction or acute total sleep deprivation. | `yamazaki2021` | PubMed sweep |
| 30038272 | Sci Rep | 2018 | Young adults are more vulnerable to chronic sleep deficiency and recurrent circadian disruption than older adults. | `zitting2018` | CITATION-CHASE (age-vulnerability modifier) |

## Exclusions by reason

| Code | n | Reason applied |
|---|---:|---|
| `E8_no_recovery_phase_or_outcome` | 145 | Screened on title/abstract: no recovery, extension or catch-up phase, or no quantitative recovery outcome relevant to this shard. |
| `E1_restriction_only` | 56 | Measures the cost of restriction but reports no recovery, extension or catch-up phase. Restriction dose-response is another shard's domain. |
| `E7_review` | 19 | Review, meta-analysis, commentary or guideline whose primary studies were screened individually; no new recovery data. |
| `E3_clinical_population` | 13 | Clinical population (sleep, psychiatric or medical disorder); exposure confounded, not healthy chronic restriction. |
| `E2_animal` | 12 | Animal model; not transportable to a human recovery prescription. |
| `E9_children_or_elderly` | 10 | Children under 15 or elderly cohort; poor transportability and no recovery-kinetics outcome. |
| `E10_nap` | 7 | Napping/siesta countermeasure rather than a recovery-sleep dose study; adolescent nap evidence is captured within lo2022. |
| `E4_off_domain_outcome` | 5 | Outcome outside this shard (pain, immunisation, athletic/exercise performance, pharmacological countermeasure, light manipulation, substance use). |
| `E10_shiftwork_or_operational` | 4 | Shift-work or operational-fatigue setting; exposure confounded by circadian misalignment and work demands. |
| `E6_same_cohort` | 3 | Same participant cohort as an included record; excluded to prevent double-counting. |
| `E5_tsd_only` | 2 | Acute total sleep deprivation only; no chronic restriction followed by a recovery phase. |
| `E6_upstream_shard` | 1 | Belongs to an upstream shard, and its recovery phase is reported without extractable numbers. |
| `E8_protocol_paper` | 1 | Study-protocol/design paper with no outcome results. |
| `E4_off_domain_biology` | 1 | Molecular/genetic outcome outside this shard; the transcriptomic recovery question is already covered by cheng2026. |
| `E7_model_not_data` | 1 | Biomathematical model fitted to already-included primaries; no new observations. |
| `E5_tsd_not_chronic` | 1 | Banking/extension design but tested against acute total sleep deprivation rather than chronic restriction. |
| `E8_not_recovery_outcome` | 1 | Addresses individual-difference stability rather than recovery of function. |
| `E8_adherence_not_kinetics` | 1 | Behavioural adherence trial; reports sleep gained but no recovery trajectory of function. |

### Exclusions that were close calls

These eleven were individually assessed rather than screened out by rule, because each was a plausible candidate for inclusion. The reason is recorded per record.

| PMID | Journal | Year | Title | Code | Reason |
|---|---|---|---|---|---|
| 27015382 | Med Sci Sports Exerc | 2016 | Sleep Extension before Sleep Loss: Effects on Performance and Neuromuscular Function. | `E5_tsd_not_chronic` | Sleep extension before sleep loss (Med Sci Sports Exerc 2016) - 6 nights extension followed by ONE night of TOTAL sleep deprivation, outcomes neuromuscular/time-to-exhaustion. Banking design but against acute TSD, not chronic restriction, and no cognitive recovery trajectory. rupp2009 (INCLUDED) is the definitive banking record. |
| 26612392 | Sleep | 2016 | Cognitive Performance, Sleepiness, and Mood in Partially Sleep Deprived Adolescents: The Need for Sleep Study. | `E6_same_cohort` | Lo 2016 Need for Sleep study - same Singapore adolescent programme pooled into lo2022 (INCLUDED, n=194). Superseded. |
| 28364507 | Sleep | 2017 | Neurobehavioral Impact of Successive Cycles of Sleep Restriction With and Without Naps in Adolescents. | `E6_same_cohort` | Lo 2017 successive restriction cycles +/- naps - same Singapore adolescent programme pooled into lo2022 (INCLUDED). Superseded. |
| 34059916 | Sleep | 2021 | Effects of ad libitum food intake, insufficient sleep and weekend recovery sleep on energy balance. | `E6_same_cohort` | Depner 2021 energy balance - SAME 36-participant weekend-recovery cohort as depner2019 (INCLUDED). Excluded to avoid double-counting. |
| 12683469 | Sleep | 2003 | The cumulative cost of additional wakefulness: dose-response effects on neurobehavioral functions and sleep physiology from chronic sleep restriction and total sleep deprivation. | `E6_upstream_shard` | Van Dongen 2003 dose-response of RESTRICTION (14 d, 4/6/8 h TIB). Canonical, but restriction dose-response belongs to shard s01; its 3 recovery nights at 8 h TIB are described only qualitatively as incomplete, with no per-night numbers I could quote. Belenky 2003 + Banks 2010 supersede it for recovery-phase numerics. |
| 26518594 | Sleep | 2016 | A Unified Model of Performance: Validation of its Predictions across Different Sleep/Wake Schedules. | `E7_model_not_data` | Unified Model of Performance validation - biomathematical model fitted to already-included primaries; contributes no new recovery observations. |
| 30072950 | Front Endocrinol (Lausanne) | 2018 | Sleep Extension in Short Sleepers: An Evaluation of Feasibility and Effectiveness for Weight Management and Cardiometabolic Disease Prevention. | `E7_review` | Narrative review of sleep extension feasibility for weight management; no primary data. Its evidence base is captured by niu2021, tasali2022, alkhatib2018, leproult2015 (all INCLUDED). |
| 34279625 | Eur J Cardiovasc Nurs | 2022 | Feasibility of sleep extension and its effect on cardiometabolic parameters in free-living settings: a systematic review and meta-analysis of experimental studies. | `E7_review` | Review, meta-analysis, commentary or guideline whose primary studies are already screened individually; no new recovery data. |
| 36546351 | Sleep | 2023 | A randomized-controlled trial of a digital, small incentive-based intervention for working adults with short sleep. | `E8_adherence_not_kinetics` | Ong 2023 digital incentive intervention for short sleepers - behavioural adherence RCT; reports sleep gained but no performance or physiological recovery trajectory. niu2021 (INCLUDED) covers at-home extension feasibility more completely. |
| 30724415 | J Sleep Res | 2019 | Trait-like characteristics of sleep EEG power spectra in adolescents across sleep opportunity manipulations. | `E8_not_recovery_outcome` | Trait-like stability of adolescent sleep EEG power spectra across sleep-opportunity manipulations - addresses individual-difference stability of spectra, not recovery of function. Same Singapore adolescent programme as lo2022 (INCLUDED). |
| 20423926 | Clin Trials | 2010 | Treatment of obesity with extension of sleep duration: a randomized, prospective, controlled trial. | `E8_protocol_paper` | Cizza 2010 - STUDY PROTOCOL/design paper for the NIDDK Sleep Extension Study with interim enrolment counts only, no outcome results. The completed cognitive results of that same study are captured by lucassen2014 (INCLUDED). |

## Full exclusion table (283 records)

| PMID | Journal | Year | Title | Code |
|---|---|---|---|---|
| 19021851 | J Sleep Res | 2008 | Sleep extension versus nap or coffee, within the context of 'sleep debt'. | `E10_nap` |
| 20699115 | Brain Behav Immun | 2011 | Benefits of napping and an extended duration of recovery sleep on alertness and immune cells after acute sleep restriction. | `E10_nap` |
| 25668196 | J Clin Endocrinol Metab | 2015 | Napping reverses the salivary interleukin-6 and urinary norepinephrine changes induced by sleep restriction. | `E10_nap` |
| 28116761 | J Sleep Res | 2017 | Assessing the benefits of napping and short rest breaks on processing speed in sleep-restricted adolescents. | `E10_nap` |
| 28329386 | Sleep | 2017 | EEG Changes Accompanying Successive Cycles of Sleep Restriction With and Without Naps in Adolescents. | `E10_nap` |
| 34559915 | Scand J Med Sci Sports | 2021 | The impact of daytime napping on athletic performance - A narrative review. | `E10_nap` |
| 39412012 | Rev Prat | 2024 | [Research on napping: where do we stand?]. | `E10_nap` |
| 31739848 | J Clin Sleep Med | 2019 | Technology Assisted Behavior Intervention to Extend Sleep Among Adults With Short Sleep Duration and Prehypertension/Stage 1 Hypertension: A Randomized Pilot Feasibility Study. | `E10_shiftwork_or_operational` |
| 32468730 | J Sleep Res | 2021 | Feasibility, acceptability and affective consequences of at-home sleep extension in young women with depressive symptoms: A pilot study. | `E10_shiftwork_or_operational` |
| 42091122 | J Diabetes Sci Technol | 2026 | Digital Intervention Increasing Sleep Duration Among People With Type 2 Diabetes: Pilot Randomized Controlled Trial. | `E10_shiftwork_or_operational` |
| 42471255 | Clin Investig Arterioscler | 2026 | Pilot study of the impact of weekend sleep restriction and recovery sleep on metabolic and cardiovascular risk indicators: Results from a randomized crossover clinical trial. | `E10_shiftwork_or_operational` |
| 1693894 | Electroencephalogr Clin Neurophysiol | 1990 | Effect of partial sleep deprivation on sleep stages and EEG power spectra: evidence for non-REM and REM sleep homeostasis. | `E1_restriction_only` |
| 10607119 | J Sleep Res | 1994 | Sleep restriction and SWS-suppression: effects on daytime alertness and night-time recovery. | `E1_restriction_only` |
| 12686280 | Clin Neurophysiol | 2003 | Oculomotor impairment during chronic partial sleep deprivation. | `E1_restriction_only` |
| 15583226 | Ann Intern Med | 2004 | Brief communication: Sleep curtailment in healthy young men is associated with decreased leptin levels, elevated ghrelin levels, and increased hunger and appetite. | `E1_restriction_only` |
| 16297554 | Pain | 2005 | Sustained sleep restriction reduces emotional and physical well-being. | `E1_restriction_only` |
| 16384630 | Biol Psychol | 2006 | The contribution of sleep to improvements in working memory scanning speed: a study of prolonged sleep restriction. | `E1_restriction_only` |
| 16676776 | Sleep | 2006 | Tiagabine is associated with sustained attention during sleep restriction: evidence for the value of slow-wave sleep enhancement? | `E1_restriction_only` |
| 16978648 | J Psychiatr Res | 2007 | Effect of flumazenil-augmentation on microsleep and mood in depressed patients during partial sleep deprivation. | `E1_restriction_only` |
| 18761394 | Brain Res Bull | 2008 | Effects of sleep restriction periods on serum cortisol levels in healthy men. | `E1_restriction_only` |
| 19238809 | Sleep | 2009 | Sleep homeostasis during repeated sleep restriction and recovery: support from EEG dynamics. | `E1_restriction_only` |
| 19240794 | PLoS One | 2009 | Sleep restriction increases the risk of developing cardiovascular diseases by augmenting proinflammatory responses through IL-17 and CRP. | `E1_restriction_only` |
| 19552702 | J Sleep Res | 2009 | CNS arousal and neurobehavioral performance in a short-term sleep restriction paradigm. | `E1_restriction_only` |
| 20580748 | Behav Brain Res | 2010 | Age-related changes during a paradigm of chronic sleep restriction. | `E1_restriction_only` |
| 21256802 | Sleep Med | 2011 | Sleep restriction over several days does not affect long-term recall of declarative and procedural memories in adolescents. | `E1_restriction_only` |
| 22131603 | Sleep | 2011 | Habitual short sleep impacts frontal switch mechanism in attention to novelty. | `E1_restriction_only` |
| 22140557 | PLoS One | 2011 | Temporal dissociation between myeloperoxidase (MPO)-modified LDL and MPO elevations during chronic sleep restriction and recovery in healthy young men. | `E1_restriction_only` |
| 21835655 | Sleep Med Rev | 2012 | Immune, inflammatory and cardiovascular consequences of sleep restriction and recovery. | `E1_restriction_only` |
| 22844441 | PLoS One | 2012 | Impact of five nights of sleep restriction on glucose metabolism, leptin and testosterone in young adult men. | `E1_restriction_only` |
| 22996147 | J Clin Endocrinol Metab | 2012 | Implications of sleep restriction and recovery on metabolic outcomes. | `E1_restriction_only` |
| 23281720 | Chronobiol Int | 2013 | Effects of partial sleep deprivation on proinflammatory cytokines, growth hormone, and steroid hormone concentrations during repeated brief sprint interval exercise. | `E1_restriction_only` |
| 23916734 | Brain Res | 2013 | Sleep allostasis in chronic sleep restriction: the role of the norepinephrine system. | `E1_restriction_only` |
| 25355222 | J Neurosci | 2014 | Sleep restriction impairs blood-brain barrier function. | `E1_restriction_only` |
| 25932797 | Int J Cardiol | 2015 | Vascular response to 1 week of sleep restriction in healthy subjects. A metabolic response? | `E1_restriction_only` |
| 26271391 | Int Arch Occup Environ Health | 2016 | The impact of sleep restriction while performing simulated physical firefighting work on cortisol and heart rate responses. | `E1_restriction_only` |
| 27091536 | Sleep | 2016 | EEG Changes across Multiple Nights of Sleep Restriction and Recovery in Adolescents: The Need for Sleep Study. | `E1_restriction_only` |
| 26534845 | Accid Anal Prev | 2017 | The efficacy of objective and subjective predictors of driving performance during sleep restriction and circadian misalignment. | `E1_restriction_only` |
| 27868260 | J Sleep Res | 2017 | An experimental study of adolescent sleep restriction during a simulated school week: changes in phase, sleep staging, performance and sleepiness. | `E1_restriction_only` |
| 28444400 | Sleep | 2017 | Effects of Insufficient Sleep on Pituitary-Adrenocortical Response to CRH Stimulation in Healthy Men. | `E1_restriction_only` |
| 29073206 | PLoS Comput Biol | 2017 | Modeling the adenosine system as a modulator of cognitive performance and sleep patterns during sleep restriction and recovery. | `E1_restriction_only` |
| 28677325 | J Sleep Res | 2018 | Memory encoding is impaired after multiple nights of partial sleep restriction. | `E1_restriction_only` |
| 28912361 | J Appl Physiol (1985) | 2018 | Impact of sleep restriction on local immune response and skin barrier restoration with and without "multinutrient" nutrition intervention. | `E1_restriction_only` |
| 29367834 | Sleep Biol Rhythms | 2018 | Physiological and autonomic stress responses after prolonged sleep restriction and subsequent recovery sleep in healthy young men. | `E1_restriction_only` |
| 29438540 | Sleep | 2018 | Influence of sleep restriction on weight loss outcomes associated with caloric restriction. | `E1_restriction_only` |
| 30056287 | Sleep Med | 2018 | Sleep spindles in adolescence: a comparison across sleep restriction and sleep extension. | `E1_restriction_only` |
| 31072563 | Prog Brain Res | 2019 | Adolescent sleep restriction effects on cognition and mood. | `E1_restriction_only` |
| 31484696 | J Lipid Res | 2019 | Four nights of sleep restriction suppress the postprandial lipemic response and decrease satiety. | `E1_restriction_only` |
| 31698968 | Chronobiol Int | 2020 | Evening chronotype, late weekend sleep times and social jetlag as possible causes of sleep curtailment after maintaining perennial DST: ain't they as black as they are painted? | `E1_restriction_only` |
| 31874181 | Physiol Behav | 2020 | A sleep intervention study comparing effects of sleep restriction and fragmentation on sleep and vigilance and the need for recovery. | `E1_restriction_only` |
| 32200304 | Sleep Med | 2020 | Effects of sleep restriction on subjective and physiological variables in middle-aged Korean adults: an intervention study. | `E1_restriction_only` |
| 33507305 | Sleep | 2021 | Effects of sleep restriction on the sleep electroencephalogram of adolescents. | `E1_restriction_only` |
| 33893807 | Sleep | 2021 | Homeostatic response to sleep restriction in adolescents. | `E1_restriction_only` |
| 34580319 | Sci Rep | 2021 | Interindividual differences in attentional vulnerability moderate cognitive performance during sleep restriction and subsequent recovery in healthy young men. | `E1_restriction_only` |
| 35039109 | Public Health Nutr | 2022 | Short sleep and social jetlag are associated with higher intakes of non-milk extrinsic sugars, and social jetlag is associated with lower fibre intakes in those with adequate sleep duration: a cross-sectional analysis from the National Diet and Nutrition Survey Rolling Programme (Years 1-9). | `E1_restriction_only` |
| 35218665 | Sleep | 2022 | Impact of chronic sleep restriction on sleep continuity, sleep structure, and neurobehavioral performance. | `E1_restriction_only` |
| 36401418 | Medicine (Baltimore) | 2022 | Partial sleep restriction-induced changes in stress, quality of life, and lipid metabolism in relation to cold hypersensitivity: A before-and-after intervention study. | `E1_restriction_only` |
| 36547105 | Clocks Sleep | 2022 | Mild to Moderate Sleep Restriction Does Not Affect the Cortisol Awakening Response in Healthy Adult Males. | `E1_restriction_only` |
| 37193393 | Sleep Adv | 2022 | Predicting vigilance vulnerability during 1 and 2 weeks of sleep restriction with baseline performance metrics. | `E1_restriction_only` |
| 37192838 | Menopause | 2023 | Association between weekend catch-up sleep and hyperuricemia with insufficient sleep in postmenopausal Korean women: a nationwide cross-sectional study. | `E1_restriction_only` |
| 37193276 | Sleep Adv | 2023 | Dynamics of recovery sleep from chronic sleep restriction. | `E1_restriction_only` |
| 37850195 | Nat Sci Sleep | 2023 | Sleep Architecture and Sleep EEG Alterations are Associated with Impaired Cognition Under Sleep Restriction. | `E1_restriction_only` |
| 38036605 | Sci Rep | 2023 | Insufficient sleep and weekend recovery sleep: classification by a metabolomics-based machine learning ensemble. | `E1_restriction_only` |
| 38219041 | Sleep | 2024 | Neurobehavioral functions during recurrent periods of sleep restriction: effects of intra-individual variability in sleep duration. | `E1_restriction_only` |
| 39043348 | Brain Behav Immun | 2024 | Effects of low-dose acetylsalicylic acid on the inflammatory response to experimental sleep restriction in healthy humans. | `E1_restriction_only` |
| 41165770 | Sleep | 2026 | Glucose homeostasis during recurrent periods of sleep restriction and recovery in healthy young adults. | `E1_restriction_only` |
| 41641962 | Sleep | 2026 | Neurobehavioral functions and sleep architecture during polyphasic and monophasic short sleep schedules. | `E1_restriction_only` |
| 41686719 | Neuroimmunomodulation | 2026 | The Effect of Low-Dose Acetylsalicylic Acid on Cellular Immune Responses to Experimental Sleep Restriction in Healthy Humans. | `E1_restriction_only` |
| 17548824 | Proc Natl Acad Sci U S A | 2007 | Repeated sleep restriction in rats leads to homeostatic and allostatic responses during recovery sleep. | `E2_animal` |
| 23666828 | Obesity (Silver Spring) | 2013 | Partial sleep deprivation by environmental noise increases food intake and body weight in obesity-resistant rats. | `E2_animal` |
| 25515100 | Sleep | 2015 | Psychomotor vigilance task performance during and following chronic sleep restriction in rats. | `E2_animal` |
| 25900125 | J Sleep Res | 2015 | Chronic sleep restriction induces long-lasting changes in adenosine and noradrenaline receptor density in the rat brain. | `E2_animal` |
| 26663203 | Exp Physiol | 2016 | Restriction of rapid eye movement sleep during adolescence increases energy gain and metabolic efficiency in young adult rats. | `E2_animal` |
| 28335560 | Nutrients | 2017 | Serum Amyloid A Production Is Triggered by Sleep Deprivation in Mice and Humans: Is That the Link between Sleep Loss and Associated Comorbidities? | `E2_animal` |
| 34193511 | eNeuro | 2021 | Effects of Severe Sleep Disruption on the Synaptic Ultrastructure of Young Mice. | `E2_animal` |
| 34636307 | Curr Pharm Biotechnol | 2022 | Xiaoyao Pill Improves the Affective Dysregulation of Sleep-deprived Female Mice by Inhibiting Brain Injury and Regulating the Content of Monoamine Neurotransmitter. | `E2_animal` |
| 39188806 | Front Neurosci | 2024 | Chronic sleep restriction during juvenility alters hedonic and anxiety-like behaviours in a sex-dependent fashion in adolescent Wistar rats. | `E2_animal` |
| 40113071 | Neuroscience | 2025 | Postnatal sleep restriction in male mice impairs the development of parvalbumin-positive neurons in the prefrontal cortex and increases anxiety-like behaviour. | `E2_animal` |
| 41409981 | Front Microbiol | 2025 | Abdominal massage modulates gut microbiota and brain-gut peptides in insomnia model rats. | `E2_animal` |
| 42419467 | Behav Processes | 2026 | REM sleep deprivation during mid-pregnancy alters exploratory behaviors in dams and induces locomotor hyperactivity in mouse offspring. | `E2_animal` |
| 7864267 | Am J Psychiatry | 1995 | Early versus late partial sleep deprivation in patients with premenstrual dysphoric disorder and normal comparison subjects. | `E3_clinical_population` |
| 10220004 | Psychiatry Res | 1999 | Sleep EEG studies during early and late partial sleep deprivation in premenstrual dysphoric disorder and normal control subjects. | `E3_clinical_population` |
| 33371502 | Cancers (Basel) | 2020 | Social Jetlag and Prostate Cancer Incidence in Alberta's Tomorrow Project: A Prospective Cohort Study. | `E3_clinical_population` |
| 33754249 | Sleep Breath | 2021 | Efficacy of simplified-cognitive behavioral therapy for insomnia(S-CBTI) among female COVID-19 patients with insomnia symptom in Wuhan mobile cabin hospital. | `E3_clinical_population` |
| 34742038 | Sleep Med | 2021 | Associations of adverse childhood experiences with adolescent total sleep time, social jetlag, and insomnia symptoms. | `E3_clinical_population` |
| 35173132 | Ind Health | 2022 | Do holidays change subjective sleep length or sleep debt in shift work disorder? | `E3_clinical_population` |
| 35686375 | J Clin Sleep Med | 2022 | Later sleep timing and social jetlag are related to increased inflammation in a population with a high proportion of OSA: findings from the Cleveland Family Study. | `E3_clinical_population` |
| 36889010 | Arch Gerontol Geriatr | 2023 | Sleep duration, weekend catch-up sleep, and risk of obstructive sleep apnea in relation to handgrip strength. | `E3_clinical_population` |
| 37864347 | J Atten Disord | 2024 | Association of Time in Bed, Social Jetlag, and Sleep Disturbances With Cognitive Performance in Children With ADHD. | `E3_clinical_population` |
| 40066650 | Sleep | 2025 | Chronotype, sleep timing, sleep regularity, and cancer risk: A systematic review. | `E3_clinical_population` |
| 41416569 | Alzheimers Dement | 2025 | Accelerometer-measured weekend catch-up sleep and incident dementia: A prospective cohort study. | `E3_clinical_population` |
| 41546844 | Cancer Causes Control | 2026 | Sleep midpoint, social jetlag, and cancer risk in the Cancer Prevention Study-3. | `E3_clinical_population` |
| 41642757 | Biopsychosoc Sci Med | 2026 | Cognitive-Behavioral Sleep and Nutritional Intervention Enhances Recovery and Survival in Rectal Cancer Patients Undergoing Abdominoperineal Resection: A Randomized Controlled Trial. | `E3_clinical_population` |
| 24194869 | PLoS One | 2013 | Partial sleep restriction activates immune response-related gene expression pathways: experimental and epidemiological studies in humans. | `E4_off_domain_biology` |
| 17910386 | Sleep | 2007 | Elevated inflammatory markers in response to prolonged sleep restriction are associated with increased pain experience in healthy volunteers. | `E4_off_domain_outcome` |
| 20171656 | J Psychiatr Res | 2010 | Modafinil reduces microsleep during partial sleep deprivation in depressed patients. | `E4_off_domain_outcome` |
| 28722214 | Hum Psychopharmacol | 2017 | Impairment due to combined sleep restriction and alcohol is not mitigated by decaying breath alcohol concentration or rest breaks. | `E4_off_domain_outcome` |
| 29029309 | Sleep | 2017 | Limited Efficacy of Caffeine and Recovery Costs During and Following 5 Days of Chronic Sleep Restriction. | `E4_off_domain_outcome` |
| 30580190 | Sleep Med | 2019 | Sleep extension reduces pain sensitivity. | `E4_off_domain_outcome` |
| 27015382 | Med Sci Sports Exerc | 2016 | Sleep Extension before Sleep Loss: Effects on Performance and Neuromuscular Function. | `E5_tsd_not_chronic` |
| 16018336 | Aviat Space Environ Med | 2005 | Oculomotor responses during partial and total sleep deprivation. | `E5_tsd_only` |
| 36804738 | J Neurosci | 2023 | Total Sleep Deprivation Increases Brain Age Prediction Reversibly in Multisite Samples of Young Healthy Adults. | `E5_tsd_only` |
| 26612392 | Sleep | 2016 | Cognitive Performance, Sleepiness, and Mood in Partially Sleep Deprived Adolescents: The Need for Sleep Study. | `E6_same_cohort` |
| 28364507 | Sleep | 2017 | Neurobehavioral Impact of Successive Cycles of Sleep Restriction With and Without Naps in Adolescents. | `E6_same_cohort` |
| 34059916 | Sleep | 2021 | Effects of ad libitum food intake, insufficient sleep and weekend recovery sleep on energy balance. | `E6_same_cohort` |
| 12683469 | Sleep | 2003 | The cumulative cost of additional wakefulness: dose-response effects on neurobehavioral functions and sleep physiology from chronic sleep restriction and total sleep deprivation. | `E6_upstream_shard` |
| 26518594 | Sleep | 2016 | A Unified Model of Performance: Validation of its Predictions across Different Sleep/Wake Schedules. | `E7_model_not_data` |
| 26206724 | Sports Med | 2015 | Stress, Sleep and Recovery in Elite Soccer: A Critical Review of the Literature. | `E7_review` |
| 27039223 | Sleep Med Rev | 2017 | Effects of sleep manipulation on cognitive functioning of adolescents: A systematic review. | `E7_review` |
| 29352373 | Sports Med | 2018 | Sleep Interventions Designed to Improve Athletic Performance and Recovery: A Systematic Review of Current Approaches. | `E7_review` |
| 30072950 | Front Endocrinol (Lausanne) | 2018 | Sleep Extension in Short Sleepers: An Evaluation of Feasibility and Effectiveness for Weight Management and Cardiometabolic Disease Prevention. | `E7_review` |
| 31166059 | J Sleep Res | 2019 | The effects of sleep extension on cardiometabolic risk factors: A systematic review. | `E7_review` |
| 33054339 | Appl Physiol Nutr Metab | 2020 | Sleep timing, sleep consistency, and health in adults: a systematic review. | `E7_review` |
| 33352457 | Sleep Med | 2021 | Sleep extension in athletes: what we know so far - A systematic review. | `E7_review` |
| 33383394 | Sleep Med | 2021 | Sleep interventions and glucose metabolism: systematic review and meta-analysis. | `E7_review` |
| 33849816 | Prim Care Diabetes | 2021 | Effects of sleep intervention on glucose control: A narrative review of clinical evidence. | `E7_review` |
| 34507028 | Sleep Med Rev | 2021 | Behavioral interventions to extend sleep duration: A systematic review and meta-analysis. | `E7_review` |
| 34573197 | Brain Sci | 2021 | Physical Therapy Exercises for Sleep Disorders in a Rehabilitation Setting for Neurological Patients: A Systematic Review and Meta-Analysis. | `E7_review` |
| 34279625 | Eur J Cardiovasc Nurs | 2022 | Feasibility of sleep extension and its effect on cardiometabolic parameters in free-living settings: a systematic review and meta-analysis of experimental studies. | `E7_review` |
| 36481460 | Int J Psychophysiol | 2023 | Effect of sleep deprivation plus existing therapies on depression: A systematic review and meta-analysis of randomized controlled trials. | `E7_review` |
| 37413721 | Sleep Med Rev | 2023 | Interventions to increase sleep duration in young people: A systematic review. | `E7_review` |
| 37462808 | Sports Med Open | 2023 | The Impact of Sleep Interventions on Athletic Performance: A Systematic Review. | `E7_review` |
| 37684151 | Sleep Health | 2023 | The importance of sleep regularity: a consensus statement of the National Sleep Foundation sleep timing and variability panel. | `E7_review` |
| 39886718 | Cureus | 2024 | A Narrative Review of the Impact of Sleep on Athletes: Sleep Restriction Causes and Consequences, Monitoring, and Interventions. | `E7_review` |
| 39849882 | Diab Vasc Dis Res | 2025 | The effect of non-pharmacological sleep interventions on glycaemic measures in adults with sleep disturbances and behaviours: A systematic review and meta-analysis. | `E7_review` |
| 40021063 | J Affect Disord | 2025 | Association of weekend catch-up sleep with depression: A systematic review and meta-analysis. | `E7_review` |
| 36546351 | Sleep | 2023 | A randomized-controlled trial of a digital, small incentive-based intervention for working adults with short sleep. | `E8_adherence_not_kinetics` |
| 1760089 | Epilepsy Res Suppl | 1991 | General considerations of sleep and sleep deprivation. | `E8_no_recovery_phase_or_outcome` |
| 7886233 | Prog Neurobiol | 1994 | Does the function of REM sleep concern non-REM sleep or waking? | `E8_no_recovery_phase_or_outcome` |
| 8746400 | Sleep | 1995 | We are chronically sleep deprived. | `E8_no_recovery_phase_or_outcome` |
| 8621064 | FASEB J | 1996 | Partial night sleep deprivation reduces natural killer and cellular immune responses in humans. | `E8_no_recovery_phase_or_outcome` |
| 8657093 | Neurophysiol Clin | 1996 | [Is the animal in hibernal sleep awake?]. | `E8_no_recovery_phase_or_outcome` |
| 9231952 | Sleep | 1997 | Cumulative sleepiness, mood disturbance, and psychomotor vigilance performance decrements during a week of sleep restricted to 4-5 hours per night. | `E8_no_recovery_phase_or_outcome` |
| 10459393 | Biol Psychiatry | 1999 | Sleep deprivation in depression: what do we know, where do we go? | `E8_no_recovery_phase_or_outcome` |
| 10543671 | Lancet | 1999 | Impact of sleep debt on metabolic and endocrine function. | `E8_no_recovery_phase_or_outcome` |
| 12015376 | J Appl Physiol (1985) | 2002 | Effects of sleep pressure on endogenous cardiac autonomic activity and body temperature. | `E8_no_recovery_phase_or_outcome` |
| 12531127 | Sleep Med Rev | 2002 | Therapeutic use of sleep deprivation in depression. | `E8_no_recovery_phase_or_outcome` |
| 14646794 | Rev Neurol (Paris) | 2003 | [Impact of sleep debt on physiological rhythms]. | `E8_no_recovery_phase_or_outcome` |
| 22033593 | Dialogues Clin Neurosci | 2003 | Chronobiology and mood disorders. | `E8_no_recovery_phase_or_outcome` |
| 14996032 | J Sleep Res | 2004 | Corticospinal excitability and sleep: a motor threshold assessment by transcranial magnetic stimulation after awakenings from REM and NREM sleep. | `E8_no_recovery_phase_or_outcome` |
| 15642774 | Hypertension | 2005 | Sleep deprivation potentiates activation of cardiovascular and catecholamine responses in abstinent alcoholics. | `E8_no_recovery_phase_or_outcome` |
| 15892922 | Clin Sports Med | 2005 | Sleep extension: getting as much extra sleep as possible. | `E8_no_recovery_phase_or_outcome` |
| 19300585 | Neuropsychiatr Dis Treat | 2007 | Sleep deprivation: Impact on cognitive performance. | `E8_no_recovery_phase_or_outcome` |
| 18295089 | Neurol Clin | 2008 | Sleep, recovery, and performance: the new frontier in high-performance athletics. | `E8_no_recovery_phase_or_outcome` |
| 18561896 | Biol Psychiatry | 2008 | Sleep loss activates cellular inflammatory signaling. | `E8_no_recovery_phase_or_outcome` |
| 18779203 | Chest | 2008 | Sleep loss and sleepiness: current issues. | `E8_no_recovery_phase_or_outcome` |
| 19084768 | Phys Med Rehabil Clin N Am | 2009 | Sleep, recovery, and performance: the new frontier in high-performance athletics. | `E8_no_recovery_phase_or_outcome` |
| 20394317 | Sleep | 2010 | Circadian and wake-dependent influences on subjective sleepiness, cognitive throughput, and reaction time performance in older and young adults. | `E8_no_recovery_phase_or_outcome` |
| 20823775 | Curr Opin Clin Nutr Metab Care | 2010 | Do all sedentary activities lead to weight gain: sleep does not. | `E8_no_recovery_phase_or_outcome` |
| 20890372 | Nat Sci Sleep | 2010 | Differential impact of chronotype on weekday and weekend sleep timing and duration. | `E8_no_recovery_phase_or_outcome` |
| 21550729 | Med Hypotheses | 2011 | Sleep and muscle recovery: endocrinological and molecular basis for a new and promising hypothesis. | `E8_no_recovery_phase_or_outcome` |
| 21737301 | Cytokine | 2011 | Effect of one night of sleep loss on changes in tumor necrosis factor alpha (TNF-α) levels in healthy men. | `E8_no_recovery_phase_or_outcome` |
| 23820239 | Brain Behav Immun | 2013 | Subjective health perception in healthy young men changes in response to experimentally restricted sleep and subsequent recovery sleep. | `E8_no_recovery_phase_or_outcome` |
| 24082305 | Sleep | 2013 | Vascular compliance limits during sleep deprivation and recovery sleep. | `E8_no_recovery_phase_or_outcome` |
| 24444805 | Neurobiol Aging | 2014 | Aging induced endoplasmic reticulum stress alters sleep and sleep homeostasis. | `E8_no_recovery_phase_or_outcome` |
| 25141012 | PLoS One | 2014 | Hawthorne effect with transient behavioral and biochemical changes in a randomized controlled sleep extension trial of chronically short-sleeping obese adults: implications for the design and interpretation of clinical studies. | `E8_no_recovery_phase_or_outcome` |
| 25325509 | Sleep | 2015 | Sleep deprivation and divergent toll-like receptor-4 activation of cellular inflammation in aging. | `E8_no_recovery_phase_or_outcome` |
| 25707282 | Methods Enzymol | 2015 | Phenotyping of neurobehavioral vulnerability to circadian phase during sleep loss. | `E8_no_recovery_phase_or_outcome` |
| 26257477 | Ind Psychiatry J | 2015 | Fatigue management in the workplace. | `E8_no_recovery_phase_or_outcome` |
| 27070173 | Chronobiol Int | 2016 | Chronotype, social jetlag and sleep debt are associated with dietary intake among Brazilian undergraduate students. | `E8_no_recovery_phase_or_outcome` |
| 27305623 | Chronobiol Int | 2016 | Differences in circadian phase and weekday/weekend sleep patterns in a sample of middle-aged morning types and evening types. | `E8_no_recovery_phase_or_outcome` |
| 27429749 | Extrem Physiol Med | 2016 | Chronic occupational exposures can influence the rate of PTSD and depressive disorders in first responders and military personnel. | `E8_no_recovery_phase_or_outcome` |
| 28164452 | Obes Rev | 2017 | Sleep-obesity relation: underlying mechanisms and consequences for treatment. | `E8_no_recovery_phase_or_outcome` |
| 28525634 | Sleep | 2017 | Association Between Weekend Catch-up Sleep and Lower Body Mass: Population-Based Study. | `E8_no_recovery_phase_or_outcome` |
| 28778243 | Sleep Med Clin | 2017 | Nonpharmacologic Management of Excessive Daytime Sleepiness. | `E8_no_recovery_phase_or_outcome` |
| 28944399 | Curr Neurol Neurosci Rep | 2017 | Neurobehavioral Effects and Biomarkers of Sleep Loss in Healthy Adults. | `E8_no_recovery_phase_or_outcome` |
| 29925863 | Sci Rep | 2018 | Social jetlag impairs balance control. | `E8_no_recovery_phase_or_outcome` |
| 30280909 | Child Obes | 2019 | Prospective Associations between Weekend Catch-Up Sleep, Physical Activity, and Childhood Obesity. | `E8_no_recovery_phase_or_outcome` |
| 30753648 | Sleep | 2019 | Differential effects of split and continuous sleep on neurobehavioral function and glucose tolerance in sleep-restricted adolescents. | `E8_no_recovery_phase_or_outcome` |
| 30773079 | J Biol Rhythms | 2019 | Sex Moderates Relationships Among School Night Sleep Duration, Social Jetlag, and Depressive Symptoms in Adolescents. | `E8_no_recovery_phase_or_outcome` |
| 30786775 | Chronobiol Int | 2019 | Sleep duration and social jetlag are independently associated with anxious symptoms in adolescents. | `E8_no_recovery_phase_or_outcome` |
| 31246714 | Med Sci Sports Exerc | 2019 | Extended Sleep Maintains Endurance Performance Better than Normal or Restricted Sleep. | `E8_no_recovery_phase_or_outcome` |
| 31285846 | NPJ Sci Learn | 2019 | Does splitting sleep improve long-term memory in chronically sleep deprived adolescents? | `E8_no_recovery_phase_or_outcome` |
| 31352036 | Chest | 2019 | The Impact of Sleep and Circadian Disorders on Physician Burnout. | `E8_no_recovery_phase_or_outcome` |
| 31389873 | Curr Sports Med Rep | 2019 | Sleep Deprivation and Its Contribution to Mood and Performance Deterioration in College Athletes. | `E8_no_recovery_phase_or_outcome` |
| 33089155 | Clocks Sleep | 2019 | Prolonged Waking and Recovery Sleep Affect the Serum MicroRNA Expression Profile in Humans. | `E8_no_recovery_phase_or_outcome` |
| 32016401 | Sleep | 2020 | Effect of cognitive load and emotional valence of distractors on performance during sleep extension and subsequent sleep deprivation. | `E8_no_recovery_phase_or_outcome` |
| 32335037 | Sleep Health | 2020 | Associations of sleep duration and social jetlag with cardiometabolic risk factors in the study of Latino youth. | `E8_no_recovery_phase_or_outcome` |
| 32386694 | Sleep Med Clin | 2020 | Nonpharmacologic Management of Excessive Daytime Sleepiness. | `E8_no_recovery_phase_or_outcome` |
| 32422497 | Med Hypotheses | 2020 | Sleep debt induces skeletal muscle injuries in athletes: A promising hypothesis. | `E8_no_recovery_phase_or_outcome` |
| 32485292 | Brain Behav Immun | 2020 | Sleep loss disrupts pericyte-brain endothelial cell interactions impairing blood-brain barrier function. | `E8_no_recovery_phase_or_outcome` |
| 33275183 | Curr Diab Rep | 2020 | Sleep Extension: A Potential Target for Obesity Treatment. | `E8_no_recovery_phase_or_outcome` |
| 32671396 | Sleep | 2021 | Alzheimer's disease genetic risk and sleep phenotypes in healthy young men: association with more slow waves and daytime sleepiness. | `E8_no_recovery_phase_or_outcome` |
| 33044669 | Neurol Sci | 2021 | Weekend catch-up sleep is associated with reduced metabolic derangements in Korean adults. | `E8_no_recovery_phase_or_outcome` |
| 33094485 | Am J Ind Med | 2021 | Interactions between home, work, and sleep among firefighters. | `E8_no_recovery_phase_or_outcome` |
| 33169493 | J Sleep Res | 2021 | Adverse interaction effects of chronic and acute sleep deficits on spatial working memory but not on verbal working memory or declarative memory. | `E8_no_recovery_phase_or_outcome` |
| 33245773 | Sleep | 2021 | Sleep duration and mood in adolescents: an experimental study. | `E8_no_recovery_phase_or_outcome` |
| 33249482 | Sleep | 2021 | Macro- and microvascular reactivity during repetitive exposure to shortened sleep: sex differences. | `E8_no_recovery_phase_or_outcome` |
| 33749139 | Neuropsychopharmacol Rep | 2021 | False-positive cases in multiple sleep latency test by accumulated sleep debt. | `E8_no_recovery_phase_or_outcome` |
| 33960554 | J Sleep Res | 2021 | Negative social jetlag - Special consideration of leisure activities and evidence from birdwatchers. | `E8_no_recovery_phase_or_outcome` |
| 34031933 | J Sleep Res | 2021 | Sleep duration and physical performance during a 6-week military training course. | `E8_no_recovery_phase_or_outcome` |
| 34038836 | Nutr Res | 2021 | Objectively measured chronotype and social jetlag are associated with habitual dietary intake in undergraduate students. | `E8_no_recovery_phase_or_outcome` |
| 34106271 | Sleep | 2021 | Optimal sleep and work schedules to maximize alertness. | `E8_no_recovery_phase_or_outcome` |
| 34144910 | Paediatr Respir Rev | 2021 | Chronic sleep deprivation in teenagers: Practical ways to help. | `E8_no_recovery_phase_or_outcome` |
| 34323993 | Sleep | 2021 | Perceived daily sleep need and sleep debt in adolescents: associations with daily affect over school and vacation periods. | `E8_no_recovery_phase_or_outcome` |
| 34902073 | Curr Diab Rep | 2021 | Type 1 Diabetes, Sleep, and Hypoglycemia. | `E8_no_recovery_phase_or_outcome` |
| 34459060 | J Sleep Res | 2022 | Sleep extension and metabolic health in male overweight/obese short sleepers: A randomised controlled trial. | `E8_no_recovery_phase_or_outcome` |
| 34624897 | Sleep | 2022 | Concordance of multiple methods to define resiliency and vulnerability to sleep loss depends on Psychomotor Vigilance Test metric. | `E8_no_recovery_phase_or_outcome` |
| 34702962 | Eur J Clin Nutr | 2022 | Changes in chronotype and social jetlag during adolescence and their association with concurrent changes in BMI-SDS and body composition, in the DONALD Study. | `E8_no_recovery_phase_or_outcome` |
| 34711770 | J Strength Cond Res | 2022 | Monitoring Effects of Sleep Extension and Restriction on Endurance Performance Using Heart Rate Indices. | `E8_no_recovery_phase_or_outcome` |
| 35162788 | Int J Environ Res Public Health | 2022 | Gaming Behaviors and the Association with Sleep Duration, Social Jetlag, and Difficulties Falling Asleep among Norwegian Adolescents. | `E8_no_recovery_phase_or_outcome` |
| 35196551 | Ann Hepatol | 2022 | Weekend catch-up sleep is associated with the alleviation of non-alcoholic fatty liver disease. | `E8_no_recovery_phase_or_outcome` |
| 35242006 | Front Neurosci | 2022 | The 3-Minute Psychomotor Vigilance Test Demonstrates Inadequate Convergent Validity Relative to the 10-Minute Psychomotor Vigilance Test Across Sleep Loss and Recovery. | `E8_no_recovery_phase_or_outcome` |
| 35271678 | PLoS One | 2022 | Impact of military training stress on hormone response and recovery. | `E8_no_recovery_phase_or_outcome` |
| 35691776 | Trends Neurosci | 2022 | Neural consequences of chronic sleep disruption. | `E8_no_recovery_phase_or_outcome` |
| 36129517 | J Exp Med | 2022 | Sleep exerts lasting effects on hematopoietic stem cell function and diversity. | `E8_no_recovery_phase_or_outcome` |
| 36152143 | Rev Endocr Metab Disord | 2022 | Sleep, testosterone and cortisol balance, and ageing men. | `E8_no_recovery_phase_or_outcome` |
| 36404842 | J Diabetes Metab Disord | 2022 | The OPTIMISE study protocol: a multicentre optimisation trial comparing continuous glucose monitoring, snacking habits, sleep extension and values-guided self-care interventions to improve glucose time-in-range in young people (13-20 years) with type 1 diabetes. | `E8_no_recovery_phase_or_outcome` |
| 36612896 | Int J Environ Res Public Health | 2022 | Different Effects of Social Jetlag and Weekend Catch-Up Sleep on Well-Being of Adolescents According to the Actual Sleep Duration. | `E8_no_recovery_phase_or_outcome` |
| 35389330 | Arch Suicide Res | 2023 | Social Jetlag and Other Aspects of Sleep Are Linked to Non-Suicidal Self-Injury Among College Students. | `E8_no_recovery_phase_or_outcome` |
| 36650276 | Sci Rep | 2023 | Association between weekend catch-up sleep and dyslipidemia among Korean workers. | `E8_no_recovery_phase_or_outcome` |
| 36746104 | Addict Behav | 2023 | Association of smartphone use with abnormal social jetlag among adolescents in Korea before and after COVID-19. | `E8_no_recovery_phase_or_outcome` |
| 37046112 | Sleep Breath | 2023 | Evaluation of weekend catch-up sleep and weekday sleep duration in relation to metabolic syndrome in Korean adults. | `E8_no_recovery_phase_or_outcome` |
| 37087961 | Sleep Med | 2023 | Quantifying teenagers' sleep patterns and sex differences in social jetlag using at-home sleep monitoring. | `E8_no_recovery_phase_or_outcome` |
| 37184756 | Sleep Breath | 2023 | The association between social jetlag and depression is independent of sleep debt. | `E8_no_recovery_phase_or_outcome` |
| 37432273 | Nutrients | 2023 | Association of Eating Pattern, Chronotype, and Social Jetlag: A Cross-Sectional Study Using Data Accumulated in a Japanese Food-Logging Mobile Health Application. | `E8_no_recovery_phase_or_outcome` |
| 37528259 | Eur J Nutr | 2023 | Exploring the relationship between social jetlag with gut microbial composition, diet and cardiometabolic health, in the ZOE PREDICT 1 cohort. | `E8_no_recovery_phase_or_outcome` |
| 37595432 | Sleep Med | 2023 | Country differences in nocturnal sleep variability: Observations from a large-scale, long-term sleep wearable study. | `E8_no_recovery_phase_or_outcome` |
| 37817267 | Trials | 2023 | Sleep Technology Intervention to Target Cardiometabolic Health (STITCH): a randomized controlled study of a behavioral sleep extension intervention compared to an education control to improve sleep duration, blood pressure, and cardiometabolic health among adults with elevated blood pressure/hypertension. | `E8_no_recovery_phase_or_outcome` |
| 37857769 | Sci Rep | 2023 | Chronotype predicts working memory-dependent regional cerebral oxygenation under conditions of normal sleep and following a single night of sleep extension. | `E8_no_recovery_phase_or_outcome` |
| 38468911 | Sleep Biol Rhythms | 2023 | Association between weekend catch-up sleep and the risk of depression among Korean middle-aged adults. | `E8_no_recovery_phase_or_outcome` |
| 38469084 | Sleep Biol Rhythms | 2023 | Efficacy of sleep extension therapy using a remote support system in university students with increased social jetlag: a parallel, single-blind, randomized controlled trial. | `E8_no_recovery_phase_or_outcome` |
| 35549578 | Hum Factors | 2024 | Recovery of Cognitive Performance Following Multi-Stressor Military Training. | `E8_no_recovery_phase_or_outcome` |
| 37697814 | J Sleep Res | 2024 | Longitudinal course and outcome of social jetlag in adolescents: A 1-year follow-up study of the adolescent sleep health epidemiological cohorts. | `E8_no_recovery_phase_or_outcome` |
| 37935914 | Sleep | 2024 | Severe atopic dermatitis, sleep disturbance, and low light exposure. | `E8_no_recovery_phase_or_outcome` |
| 37966411 | J Adolesc Health | 2024 | Perceived Epidemic Impacts and Mental Symptom Trajectories in Adolescents Back to School After COVID-19 Restriction: A Longitudinal Latent Class Analysis. | `E8_no_recovery_phase_or_outcome` |
| 38268197 | J Physiol | 2024 | Sleep extension and cardiometabolic health: what it is, possible mechanisms and real-world applications. | `E8_no_recovery_phase_or_outcome` |
| 38382765 | Prev Med | 2024 | Is the association between social jetlag and BMI mediated by lifestyle? A cross-sectional survey study in the Dutch general population. | `E8_no_recovery_phase_or_outcome` |
| 38412653 | J Psychosom Res | 2024 | Association between weekend catch-up sleep and the risk of prediabetes and diabetes: A cross-sectional study using KNHANES. | `E8_no_recovery_phase_or_outcome` |
| 38452941 | J Affect Disord | 2024 | Association between weekend catch-up sleep and depressive symptoms in American adults: Finding from NHANES 2017-2020. | `E8_no_recovery_phase_or_outcome` |
| 38589752 | Sports Med Open | 2024 | Sleep and Ultramarathon: Exploring Patterns, Strategies, and Repercussions of 1,154 Mountain Ultramarathons Finishers. | `E8_no_recovery_phase_or_outcome` |
| 38705524 | J Affect Disord | 2024 | Examining the connection between weekend catch-up sleep and depression: Insights from 2017 to 2020 NHANES information. | `E8_no_recovery_phase_or_outcome` |
| 38816707 | BMC Psychiatry | 2024 | Characterising illness stages and recovery trajectories of eating disorders in young people via remote measurement technology (STORY): a multi-centre prospective cohort study protocol. | `E8_no_recovery_phase_or_outcome` |
| 38874812 | Eur J Sport Sci | 2024 | Sleep deprivation and recovery: Endurance racing as a novel model. | `E8_no_recovery_phase_or_outcome` |
| 38878158 | Sleep Breath | 2024 | Can weekend catch-up sleep decrease the risk of cognitive dysfunction in older adults? | `E8_no_recovery_phase_or_outcome` |
| 38895883 | Sleep | 2024 | Device-measured weekend catch-up sleep, mortality, and cardiovascular disease incidence in adults. | `E8_no_recovery_phase_or_outcome` |
| 39119912 | J Biosci | 2024 | Paradoxical sleep deprivation and restriction promote castration-like effects and local inflammatory responses in male gerbil prostate. | `E8_no_recovery_phase_or_outcome` |
| 39535530 | J Occup Health | 2024 | Association between physical activity patterns of working-age adults and social jetlag, depressive symptoms, and presenteeism. | `E8_no_recovery_phase_or_outcome` |
| 40666637 | Aust J Psychol | 2024 | Adolescent and young adult sleep and sleep-related behaviour change before and during the COVID-19 pandemic lockdown in Canada. | `E8_no_recovery_phase_or_outcome` |
| 39532610 | Sleep Health | 2025 | Prevalence of social jetlag and associated factors in Brazilian adolescents: Results from a country-wide cross-sectional study. | `E8_no_recovery_phase_or_outcome` |
| 39673900 | Sleep Med | 2025 | Associations between sleep opportunity, sleep problems, and social jetlag and toddlers' adiposity: A cross-sectional study. | `E8_no_recovery_phase_or_outcome` |
| 39910840 | Ren Fail | 2025 | Association between weekend catch-up sleep and chronic kidney disease: insights from NHANES 2017-2020. | `E8_no_recovery_phase_or_outcome` |
| 39945719 | Sleep | 2025 | Weekend sleep extension, social jetlag, and incidence of coronary calcium score: the ELSA-Brasil study. | `E8_no_recovery_phase_or_outcome` |
| 39987959 | Contemp Clin Trials | 2025 | Developing a multicomponent intervention to increase glucose time in range in adolescents and young adults with type 1 diabetes: An optimisation trial to screen continuous glucose monitoring, sleep extension, healthier snacking and values-guided self-management intervention components. | `E8_no_recovery_phase_or_outcome` |
| 40264068 | BMC Public Health | 2025 | Weekend catch-up sleep and frailty in US adults: a cross-sectional study from NHANES 2017-2020. | `E8_no_recovery_phase_or_outcome` |
| 40412461 | Neurosci Biobehav Rev | 2025 | The sleep paradox: The effect of weekend catch-up sleep on homeostasis and circadian misalignment. | `E8_no_recovery_phase_or_outcome` |
| 40437485 | BMC Med | 2025 | Investigating the associations between weekend catch-up sleep and insulin resistance: NHANES cross-sectional study. | `E8_no_recovery_phase_or_outcome` |
| 40443304 | Kidney Res Clin Pract | 2025 | Weekend catch-up sleep and its association with chronic kidney disease and albuminuria in middle age and older adults from the National Health and Nutrition Examination Survey (2017-2020). | `E8_no_recovery_phase_or_outcome` |
| 40458091 | Front Public Health | 2025 | Association between weekend catch-up sleep and gallstone disease in US adults: a cross-sectional study from NHANES 2017-2020. | `E8_no_recovery_phase_or_outcome` |
| 40518072 | J Cardiol | 2025 | Association of weekend catch-up sleep, sleep durations and cardiometabolic multimorbidity: Based on NHANES. | `E8_no_recovery_phase_or_outcome` |
| 40538806 | Front Endocrinol (Lausanne) | 2025 | Association between weekend catch-up sleep and glycemic control among individuals with diabetes: a population-based study. | `E8_no_recovery_phase_or_outcome` |
| 40581101 | J Affect Disord | 2025 | Association between wearable device-measured weekend catch-up sleep and brain health in UK Biobank participants. | `E8_no_recovery_phase_or_outcome` |
| 40596991 | BMC Psychiatry | 2025 | Association of weekend catch-up sleep ratio with depressive risk: insights from NHANES 2021-2023. | `E8_no_recovery_phase_or_outcome` |
| 40742144 | J Clin Sleep Med | 2025 | Association of weekend catch-up sleep with the atherosclerotic cardiovascular disease risk score: a hypothesis-generating study from US and Korean National Health and Nutrition Examination Surveys. | `E8_no_recovery_phase_or_outcome` |
| 40859789 | Chronobiol Int | 2025 | Chrononutrition and sleep patterns in individuals with diabetes mellitus: Assessing misalignments and social jetlag. | `E8_no_recovery_phase_or_outcome` |
| 40878374 | Psychiatry Investig | 2025 | Association Between Weekend Catch-Up Sleep and Depression: Evidence From the 2017-2018 National Health and Nutrition Examination Survey. | `E8_no_recovery_phase_or_outcome` |
| 40917570 | Sleep Adv | 2025 | Homeostatic forces underlying the daily pattern of sleep propensity. | `E8_no_recovery_phase_or_outcome` |
| 40988202 | Medicine (Baltimore) | 2025 | The association between weekend catch-up sleep and obesity in U.S. adults: A cross-sectional analysis of NHANES 2017-2020. | `E8_no_recovery_phase_or_outcome` |
| 41061839 | J Stroke Cerebrovasc Dis | 2025 | Nonlinear association between weekend catch-up sleep and stroke prevalence in U.S. adults. | `E8_no_recovery_phase_or_outcome` |
| 41148489 | Sleep Breath | 2025 | Can weekend catch-up sleep repay the sleep debt? Balancing short-term relief with long-term risks. | `E8_no_recovery_phase_or_outcome` |
| 41272564 | BMC Public Health | 2025 | Gender differences in the relationships between weekday sleep duration, weekend catch-up sleep, and hypertension. | `E8_no_recovery_phase_or_outcome` |
| 41416045 | Front Psychiatry | 2025 | Association between weekend catch-up sleep and specific depressive symptoms: a real world research. | `E8_no_recovery_phase_or_outcome` |
| 29630288 |  | 2026 | EMS Provider Health And Wellness. | `E8_no_recovery_phase_or_outcome` |
| 41192734 | J Affect Disord | 2026 | Weekend catch-up sleep and depressive symptoms in late adolescence and young adulthood: Results from the National Health and Nutrition Examination Survey. | `E8_no_recovery_phase_or_outcome` |
| 41568778 | Sleep | 2026 | Chronic sleep loss and A1 adenosine receptors in the human brain. | `E8_no_recovery_phase_or_outcome` |
| 41595471 | Genes (Basel) | 2026 | Somatostatin-Expressing Neurons Regulate Sleep Deprivation and Recovery. | `E8_no_recovery_phase_or_outcome` |
| 41615003 | Sleep | 2026 | Perspectives on idiopathic hypersomnia: diagnostic challenges, unknown pathophysiological, and emerging therapeutic strategies. | `E8_no_recovery_phase_or_outcome` |
| 41678723 | Mil Med | 2026 | Higher Baseline Diet Quality Is Positively Associated With Academic and Physical Performance Among United States Military Academy Cadets. | `E8_no_recovery_phase_or_outcome` |
| 41831129 | Clin Exp Med | 2026 | Association between weekend catch-up sleep and Metabolic dysfunction-associated steatotic liver disease in US adults. | `E8_no_recovery_phase_or_outcome` |
| 42045986 | J Sleep Res | 2026 | Peripheral Inflammation and Sleep Loss Induce Coordinated Motivational Changes: An Experimental Two-Hit Stress Model. | `E8_no_recovery_phase_or_outcome` |
| 42470595 | Eur J Pediatr | 2026 | Social jetlag and academic performance in adolescents: insights from a region with structural circadian misalignment. | `E8_no_recovery_phase_or_outcome` |
| 42472824 | Nutr Metab (Lond) | 2026 | Work-to-sleep ratio as a novel marker of NAFLD risk: evidence from U.S. and Korean national cohorts. | `E8_no_recovery_phase_or_outcome` |
| 30724415 | J Sleep Res | 2019 | Trait-like characteristics of sleep EEG power spectra in adolescents across sleep opportunity manipulations. | `E8_not_recovery_outcome` |
| 20423926 | Clin Trials | 2010 | Treatment of obesity with extension of sleep duration: a randomized, prospective, controlled trial. | `E8_protocol_paper` |
| 21262888 | Pediatrics | 2011 | Sleep duration, sleep regularity, body weight, and metabolic homeostasis in school-aged children. | `E9_children_or_elderly` |
| 26317786 | Chronobiol Int | 2015 | Associations of chronotype with social jetlag and behavioral problems in preschool children. | `E9_children_or_elderly` |
| 29298086 | Child Obes | 2018 | Sleep and Adiposity in Preadolescent Children: The Importance of Social Jetlag. | `E9_children_or_elderly` |
| 32279704 | J Clin Sleep Med | 2020 | Association between weekend catch-up sleep and executive functions in Chinese school-aged children. | `E9_children_or_elderly` |
| 34692778 | Front Cardiovasc Med | 2021 | Social Jetlag and Cardiometabolic Risk in Preadolescent Children. | `E9_children_or_elderly` |
| 36094530 | JAMA Pediatr | 2022 | Nonpharmacological Interventions to Lengthen Sleep Duration in Healthy Children: A Systematic Review and Meta-analysis. | `E9_children_or_elderly` |
| 37193406 | Sleep Adv | 2022 | Interaction effects of sex on the sleep loss and social jetlag-related negative mood in Japanese children and adolescents: a cross-sectional study. | `E9_children_or_elderly` |
| 36863827 | Am J Clin Nutr | 2023 | The effect of modest changes in sleep on dietary intake and eating behavior in children: secondary outcomes of a randomized crossover trial. | `E9_children_or_elderly` |
| 37980245 | Sleep Health | 2024 | Predictors for achieving optimal sleep in healthy children: Exploring sleep patterns in a sleep extension trial. | `E9_children_or_elderly` |
| 42199500 | Front Pediatr | 2026 | Protocol for a randomized controlled trial investigating the effects of sleep extension on body weight and learning in children (More2Sleep). | `E9_children_or_elderly` |

