# Screening log — shard `s15_brain_structure`

**Domain:** does chronic sleep restriction during adolescence (16–19) leave a structural or
developmental mark on the brain?

**Records screened:** 121 · **Included:** 30 · **Excluded:** 91
(counts recomputed programmatically from this file: 30 included rows + 23 excluded table rows +
68 compact-list exclusions = 121 unique PMIDs, no duplicates, no include/exclude overlap)
**Identifier verification:** all 30 included records had PMID resolved via PubMed esummary AND
DOI resolved via Crossref, with PubMed's DOI for the PMID matching the record's DOI and
title-similarity **1.000 for all 30** on the final pass (see `_tools/verify.py`). An earlier
35-pair check that also covered later-excluded records had a minimum similarity of 0.876.
**Zero identifiers failed verification.** One near-miss caught and corrected — see the note at
the bottom of this file.

Search strategy: PubMed E-utilities (esearch/esummary/efetch) via `_tools/search.sh`; full text
via PMC Open Access (`_tools/pmc.sh`) where available. Query families run: adolescent sleep
duration × brain structure/cortical thickness/gray matter; ABCD / IMAGEN / Generation R cohort
searches; longitudinal MRI + adolescent sleep; experimental sleep deprivation × gray matter /
cortical thickness / diffusion; CPAP / recovery sleep × brain structure; diffusion MRI ×
adolescent sleep duration; Mendelian randomization × sleep × brain; synaptic homeostasis /
pruning × adolescence; rodent adolescent sleep restriction × durable neural change.

---

## INCLUDED (30)

| # | PMID | Study | Design | Tier | n | Why included |
|---|------|-------|--------|------|---|--------------|
| 1 | 37798367 | `fjell2023` No phenotypic or genotypic evidence for a link between sleep duration and brain atrophy | Longitudinal MRI + MR | T3 | 47,029 (51,295 obs; 8,153 longitudinal) | **Keystone.** Longitudinal null for atrophy; cross-sectional optimum 6.5 h (5.7–7.3); MR null |
| 2 | 26812659 | `bernardi2016` Sleep reverts changes in human gray and white matter caused by wake-dependent training | Within-subject | T1 | 16 | **State-vs-trait keystone.** All acute GM/WM changes reverted after recovery sleep |
| 3 | 33566829 | `lapidaire2021` Irregular sleep habits, regional grey matter volumes… adolescents | Cross-sectional | TX | 101 | **Best age match (mean 16.8 y).** Sleep debt null; only weekend timing significant |
| 4 | 36610292 | `guldner2023` Adolescent catch-up sleep, white-matter maturation and internalizing problems | Longitudinal DTI 14.5→19.8 y | T5 | 111 | **Best-matched longitudinal.** Weekday TIB change → FA change NULL; catch-up sleep protective |
| 5 | 32015467 | `cheng2021` Sleep duration, brain structure, and psychiatric and cognitive problems in children | Cross-sectional (ABCD) | TX | 11,067 | Seed study. r=0.047; thickness null; cross-lagged shows reverse causation |
| 6 | 28181512 | `urrila2017` Sleep habits, academic performance, and the adolescent brain structure | Cross-sectional (IMAGEN) | TX | 177 | Seed study. GMV in **arbitrary units** — no mm³/hour extractable |
| 7 | 22197742 | `taki2012` Sleep duration during weekdays affects hippocampal gray matter volume in children | Cross-sectional | TX | 290 | Seed study. Direction only; failed replication by `urrila2017` |
| 8 | 28364462 | `kocevska2017` Developmental course of sleep disturbances… brain morphology at age 7 (Generation R) | Prospective exposure, 1 scan | T5 | 720 | **Only interpretable cm³ estimate:** −7.3 cm³ (−12.1, −2.6) per SD |
| 9 | 31240728 | `mulder2019` Childhood sleep disturbances and white matter microstructure in preadolescence | Prospective exposure, 1 scan | T5 | 2,449 | Best-quantified FA effect: −0.12 SD (−0.20, −0.05) per SD |
| 10 | 26093368 | `telzer2015` Sleep variability in adolescence is associated with altered brain development | Longitudinal diary → DTI | T5 | 48 | **Average sleep duration NULL for FA**; only variability mattered |
| 11 | 39580729 | `limasantos2025` Impact of insufficient sleep on white matter development | Longitudinal NODDI (ABCD) | T5 | 1,016 | **FA null** (`p>.050`); only ODI moved |
| 12 | 41562565 | `wild2026` Sleep as a moderator of adolescent brain development | Longitudinal MRI + actigraphy | T4 | 39 | Only study with objective exposure + repeated structural MRI |
| 13 | 35914537 | `yang2022` Effects of sleep duration on neurocognitive development (propensity matched, ABCD) | Propensity-matched longitudinal | T5 | 8,323 | Widely cited as "long-lasting"; actually shows *stability*, r=0.61 |
| 14 | 28526620 | `elvsashagen2017` Cortical structural plasticity after a day of waking and sleep deprivation | Within-subject + control arm | T1 | 61 | Cortical thickness changes **morning→evening within one day** |
| 15 | 26020651 | `elvsashagen2015` Widespread changes in white matter microstructure after a day of waking and SD | Within-subject | T1 | 21 | FA rose then fell within a single 23-h period |
| 16 | 35422097 | `voldsbekk2022` Widespread alterations in cortical microstructure after 32 h of SD | Parallel-arm | T1 | 41 | **Myelin-sensitive** T1w/T2w ratio moved in 32 h, survived motion/hydration adjustment |
| 17 | 24346259 | `liu2014` Long-term total sleep deprivation reduces thalamic gray matter volume | Within-subject | T1 | not reported | 72 h total SD → **no** whole-brain GM or hippocampal change |
| 18 | 32903801 | `sun2020` Alteration of brain gray matter density after 24 h of SD | Within-subject | T1 | 23 | Frontal GM density **increased**; tracked subjective sleepiness (r=0.625) |
| 19 | 21037021 | `canessa2011` OSA: brain structural changes and neurocognitive function before and after treatment | Uncontrolled pre-post | T1 | 32 | GM volume **increased** after 3 months of treatment |
| 20 | 39998447 | `xu2025` Effects of CPAP on neuroimaging biomarkers and cognition: RCT | RCT | T1 | 148 | **Highest tier on reversibility.** Thickness moved; primary cognitive endpoint NULL (p=0.91) |
| 21 | 40086297 | `namsrai2025` Sleep characteristics and brain structure: systematic review with meta-analysis | Meta-analysis | TX | 108,364 (106 studies) | Top of hierarchy; produced **no** pooled per-hour volumetric estimate |
| 22 | 41794771 | `chen2026` Neuroimaging subtypes of adolescent sleep insufficiency… natural short sleepers | Cross-sectional (ABCD) | TX | not reported | Three causally distinct subtypes; one is genetically-predisposed and phenotypically normal |
| 23 | 39632091 | `zhang2024` Genetically supported causality between brain structural connectome and sleep duration | Two-sample MR | T3 | not reported | **Reverse causation:** brain structure → sleep duration |
| 24 | 36575851 | `hansen2023` Socioeconomic disparities in sleep duration are associated with cortical thickness | Cross-sectional | TX | 94 | Documents the SES → routines → sleep → thickness confounding path |
| 25 | 40449887 | `alvarezornelas2025` Sleep deprivation as a risk factor for cortical gray matter reduction in new medical residents | Within-person longitudinal | T5 | 41 | **Largest pro-harm number in the literature** (−1.78% GM in 4 mo); included with its fatal flaws documented |
| 26 | 31229687 | `tuan2019` Microglia-mediated synaptic pruning is impaired in sleep-deprived adolescent mice | Animal (mouse) | T1 | not reported | Most direct pruning evidence; adolescent-specific |
| 27 | 39441640 | `gay2024` Developing forebrain synapses are uniquely vulnerable to sleep loss | Animal (mouse), 3 ages | T1 | not reported | Best sensitive-period test; vulnerable stage was **juvenile, not adolescent** |
| 28 | 30896191 | `howard2019` Immediate and long-lasting cognitive consequences of adolescent chronic sleep restriction | Animal (rat) + recovery | T1 | not reported | **Only study testing persistence after recovery.** Positive — but behavioural, no brain measure |
| 29 | 16857890 | `feinberg2006` Adolescent decline of NREM delta… linked to age and sex but not pubertal stage | Longitudinal PSG | T4 | 69 | Normative pruning trajectory (−25% ages 12→14); age-driven, **not** puberty-driven |
| 30 | 42509928 | `ananth2026` Structural brain correlates of insufficient sleep in adolescents: narrative review | Narrative review | TX | — | Confirms no pooled estimate exists; base rate (<30% of US students meet recommendations) |

---

## EXCLUDED (91)

### Considered seriously, then excluded

| PMID | Record | Exclusion reason |
|------|--------|------------------|
| 40244849 | Ma 2025, *Cell Rep* — Neural correlates of device-based sleep characteristics in adolescents (ABCD, n=3,222) | **Objective sleep + longitudinal (9→14 y), genuinely relevant.** Excluded because sparse canonical correlation analysis and hierarchical clustering yield latent multivariate dimensions and biotypes with **no extractable per-hour or per-SD structural effect estimate**. Nothing poolable. Its heterogeneity conclusion duplicates `chen2026`, which is retained. |
| 35714839 | Vulser 2023, *JAACAP* — Chronotype, longitudinal volumetric brain variations throughout adolescence (IMAGEN, n=128, ages 14→19) | Longitudinal GMV in the exact target window, but exposure is **chronotype/eveningness, not sleep duration**. Noted for direction: higher eveningness → **LARGER** right mPFC GMV at both 14 and 19 — opposite sign to the "short sleep shrinks mPFC" claim. Logged rather than extracted because the exposure does not map to sleep restriction. |
| 40099522 | Guo 2025, *Sleep* — Moderating role of subjective daytime sleepiness (n=81, actigraphy, age 10.5) | Age 10.5 and n=81. Also reports sleep duration **negatively** correlated with insula GMV (longer sleep → smaller volume), another sign inconsistency; logged not extracted. |
| 26065720 | Chest 2015 — Effect of CPAP on cognition, brain function and structure in **elderly** OSA: randomized pilot | Elderly; pilot. Superseded by `xu2025` (n=148 RCT) and `canessa2011` for the reversibility question. |
| 24808886 | Front Neurol 2014 — Volumetric brain morphometry changes in OSA: effects of CPAP + literature review | Mixed primary/review format; superseded by `xu2025`. |
| 33358980 | Brain Behav Immun 2021 — Voluntary exercise ameliorates synaptic pruning deficits in sleep-deprived adolescent mice | Same lab/model as `tuan2019` (retained); primary exposure of interest is exercise. Corroborative only. |
| 31263066 | J Neurosci 2019 — SD by novel objects increases synapse density and axon-spine interface in CA1 of adolescent mice | Corroborates `tuan2019` direction (more synapses, not fewer). Excluded to avoid over-weighting one rodent model. |
| 34193511 | eNeuro 2021 — Effects of severe sleep disruption on synaptic ultrastructure of young mice | Young (not adolescent-specific) mice; ultrastructure only; no recovery arm. |
| 42519017 | iScience 2026 — Sleep modulates SV2A and spine density across cortical regions and development | Animal, molecular; no adolescent-specific chronic restriction arm. |
| 35662652 | Pharmacol Biochem Behav 2022 — Chronic REM sleep restriction during juvenility, long-term anxiety and neurotransmission (rats) | **Juvenile**, not adolescent; outcome is anxiety behaviour/neurotransmitters, not structure. |
| 37657176 | Sleep Med 2023 — Sleep disorders causally affect brain cortical structure: MR study | Exposure is **sleep disorders** (insomnia, OSA), not sleep duration. |
| 21203377 | Sleep 2011 — Adolescent changes in homeostatic regulation of delta/theta during NREM | Companion to `feinberg2006` (retained); normative, no restriction exposure. |
| 40837838 | Front Aging Neurosci 2025 — Distinct effect of partial SD on gray matter in young and old adults | Considered for the acute strand; adds nothing beyond `sun2020`/`elvsashagen2017` and mixes elderly. |
| 37034160 | Front Neurosci 2023 — Altered isotropic volume fraction in gray matter after SD (NODDI) | Acute; duplicates `voldsbekk2022`/`elvsashagen2015` strand. |
| 36421858 | Brain Sci 2022 — Vigilant attention, CBF and GMV change after 36 h SD: pilot | Self-described pilot; small n. |
| 37805053 | Brain Res Bull 2023 — Plasma Aβ after SD and brain structural remodeling in night-shift workers | Primary outcome is amyloid; night-shift circadian inversion ≠ subject's exposure. |
| 30471387 | Neuroimage 2019 — Cerebral blood flow changes after wake, sleep and SD | Perfusion, not structure (mechanistically supportive of the state interpretation). |
| 38007724 | Stud Health Technol Inform 2023 — Age-related subcortical morphology after 3 h SD | Conference proceedings; not peer-reviewed primary. |
| 42335796 | Compr Psychiatry 2026 — Neuroimaging insights on sleep disturbances and risk for MDD in youth: systematic review | Outcome is depression risk, not structural permanence; `ananth2026` covers the structural review. |
| 42055498 | Sleep Med 2026 — OSA with A/T/N biomarkers, neurodegeneration and CPAP-related changes | Elderly neurodegeneration; wrong population. |
| 32623206 | J Adolesc 2020 — Sleep **quality** and diffusion-derived white matter integrity in early adolescence | Exposure is sleep quality, not duration. |
| 27397561 | Sleep 2016 — Sleep duration and white matter quality in **middle-aged** adults | Midlife; superseded by `fjell2023` for the adult strand. |
| 29244799 | Pediatr Res 2018 — Prenatal/early postnatal brain development and childhood sleep patterns (Generation R) | Direction is brain → sleep in **infants**; supports the reverse-causation point but no extractable adolescent effect. |

### Excluded — wrong outcome (functional, behavioural or non-imaging)

`41496291` (intrinsic *functional* architecture) · `41891324` (neural sensitivity to social media, functional) ·
`38464778` (resting-state fMRI meta-analysis) · `26712339` (functional connectome) · `29244642` (SD and anxious brain, functional) ·
`31461677` (white matter and mood degradation, wrong exposure) · `40819829` (grey matter–CSF fMRI coupling) ·
`42457937` (emotion regulation, no imaging) · `42437621` (trauma → psychopathology, no imaging) ·
`42381189` (self-regulation, canonical correlation, no imaging) · `41883200` (ADHD symptom severity) ·
`41870441` (wearables and transdiagnostic mental health, no imaging) · `41438611` (neighbourhood disadvantage, no imaging) ·
`30169721` (sleepiness/vigilance under restriction — belongs to cognition shards) · `25325507` (³¹P MRS bioenergetics) ·
`30042667` (machine-learning prediction, methods paper)

### Excluded — wrong population or clinical condition

`37331007` (paediatric ME/CFS) · `38558207` (chronic headache in youth) · `39537644` (psychosis continuum) ·
`33601229` (medication-free ADHD adolescents) · `32954401`, `30346595` (OSA neuropathology, post-mortem/elderly) ·
`27139243`, `22670023`, `20739254`, `14751008`, `35045769`, `33621163`, `29394413` (OSA/sleepiness reviews in adults and elderly) ·
`36570704` (maternal sleep deprivation, offspring — prenatal exposure) · `37148913` (pharmacological rescue, SAG treatment) ·
`32198011` (endocannabinoid REM SD, mechanism-of-drug focus) · `25707915` (rat pain modulation) · `42129147` (thalamic nuclei across psychiatric disorders)

### Excluded — off-topic exposure or outcome

`41436889`, `42424896` (obesity/weight gain) · `36325967` (morningness–eveningness development) ·
`37058610` (alcohol and sleep EEG) · `32544374` (auditory radiation microstructure, single obscure tract) ·
`41975627` (external counterpulsation therapy) · `42464462` (stimulant medication) ·
`42294390` (physical activity and cognition) · `41898365` (diabetes and brain health) ·
`32033054`, `39794834`, `30268792`, `40097472` (diet quality / 24-h movement guidelines) ·
`33757816`, `29475430` (early adversity reviews) · `36192372` (circadian genes and autism) ·
`42129562`, `40832429`, `38942983` (biological-ageing clocks) · `37336327` (lifestyle risk factors, adult lifespan)

### Excluded — not a primary study

`27534393` (CNS-2016 meeting abstract compilation) · `35388223`, `36151472` (Nature brain charts + correction — normative, no sleep) ·
`33913199` (ENIGMA-Sleep roadmap) · `31791002` (narrative review, fronto-limbic) · `32248785` (review, synaptic ultrastructure) ·
`33324997` (ORACLE study protocol) · `30631284` (Danish VIA 11 study protocol) · `34692610` (ABCD cohort descriptive overview) ·
`38609481` (mood variability, exploratory) · `39537024` (rest–activity rhythms, circadian framing) ·
`37944709` (COVID-era stress, ABCD) · `35367190` (hyperemesis gravidarum offspring) · `39809303` (exercise in coronary artery disease)

---

## Verification incident (recorded per hard rule 3)

While extracting `urrila2017` my first-pass XML parser returned DOI `10.1111/jsr.12373` for
PMID 28181512. Crossref resolved that DOI to *"Sleep and academic performance in later
adolescence: results from a large population-based study"* (Journal of Sleep Research) — **a
different paper**. Cause: the parser was reading `<ArticleId>` nodes from the reference list as
well as the article's own `ArticleIdList`. Corrected DOI is **`10.1038/srep41678`**, confirmed by
Crossref as *"Sleep habits, academic performance, and the adolescent brain structure"*, Scientific
Reports. The parser was fixed to read identifiers only from `PubmedData/ArticleIdList`, and all 30
included records were then re-verified against both PubMed and Crossref with title matching.

**Net result: 0 fabricated or unresolved identifiers in the final record set.**
