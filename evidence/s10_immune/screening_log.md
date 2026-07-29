# s10_immune — screening log

**Screened: 44 candidate records. Included with a YAML record: 25. Excluded: 19.**

Search route: PubMed E-utilities (`_tools/pmquery.sh` for esearch→esummary, `_tools/pmabs.sh` for
abstracts), Europe PMC and PMC for full text (`_tools/getft.sh`, `_tools/html2txt.py`), Crossref +
PubMed esummary for identifier verification (`_tools/verify.py` → `_tools/verification.json`).

Query families run: sleep + rhinovirus/common cold challenge; sleep + vaccination/antibody/immunogenicity;
sleep duration + CRP/IL-6/TNF meta-analysis; sleep restriction + recovery sleep + inflammation; sleep +
pneumonia/respiratory infection cohort; sleep + infection in adolescents/college students; sleep +
NK cell/T cell function; Mendelian randomization + sleep + inflammation; sleep + COVID vaccine
breakthrough.

---

## Included (25) — one YAML record each

| # | study_id | PMID | Tier | Why included |
|---|---|---|---|---|
| 1 | `prather2015_rhinovirus` | 26118561 | T2 | Required #1. Actigraphy + experimental rhinovirus challenge; ORs by category, absolute rates, and the crucial infection-vs-illness split |
| 2 | `cohen2009_cold` | 19139325 | T2 | Required #2. Dose-response by self-reported duration AND sleep efficiency before viral challenge |
| 3 | `spiegel2002_influenza_vaccine` | 12243633 | T1 | Required #3. The seminal influenza-vaccine restriction experiment. `access_tier: secondhand` — see exclusion note below |
| 4 | `lange2003_hepa` | 14508028 | T1 | Required #3. Hepatitis A vaccination, one night of total deprivation, ~2-fold titre difference |
| 5 | `lange2011_memory` | 21632713 | T1 | Required #3. Cellular immune memory, 1-year follow-up, seroprotection failures — the durability evidence |
| 6 | `prather2012_hepb` | 22851802 | T4 | Required #3. Hepatitis B, actigraphy, clinical protection at 6 months |
| 7 | `spiegel2023_vaccine_meta` | 36917932 | T1 | Required #3. The vaccine-immunogenicity meta-analysis, with the subjective/objective and sex splits |
| 8 | `irwin2016_inflammation_meta` | 26140821 | TX | Required #4. The CRP/IL-6 meta-analysis; extracted the short-duration-specific nulls. Tiered `TX` not `T1` because the pooled duration-inflammation studies are predominantly cross-sectional, so the pooled estimate inherits cross-sectional design |
| 9 | `besedovsky2019_review` | 30920354 | TX | Required #5. Mechanism + route to primaries + secondhand source for #3 |
| 10 | `ballesio2026_experimental_meta` | 40474574 | T1 | Newest (search to Mar 2025) experimental inflammation meta-analysis; supersedes Irwin's experimental arm |
| 11 | `pejovic2013_recovery` | 23941878 | T1 | Required #6. IL-6 fully normalised after 2×10 h recovery; best-matched dose (6 h weeknights) |
| 12 | `simpson2016_repeated_recovery` | 27263430 | T1 | Required #6. 3 weeks of 5×4 h + 2×8 h — the closest model of the subject's actual weekly pattern |
| 13 | `vanleeuwen2009_recovery` | 19240794 | T1 | Required #6. CRP higher AFTER the recovery weekend; cell counts recovered, cytokines did not |
| 14 | `faraut2011_nap_recovery` | 20699115 | T1 | Required #6. The only study varying RECOVERY DOSE — reconciles the contradictory recovery literature |
| 15 | `benedict2012_h1n1` | 22217111 | T1 | Key null: antibody deficit gone by day 10, null to day 52 |
| 16 | `pratherleung2016_nhanes` | 27064773 | TX | Best source of population ABSOLUTE 30-day infection rates by sleep category; 6 h null |
| 17 | `patel2012_pneumonia` | 22215923 | T5 | Only prospective cohort with a radiographically confirmed serious-infection endpoint |
| 18 | `martinezalbert2025_infection` | 39842484 | TX | Required #7-adjacent. Youngest observational sample (57% aged 18-25); isolates social jet lag |
| 19 | `forthun2023_gp_infection` | 36937728 | TX | Only record disaggregating by infection SITE — reveals the respiratory null |
| 20 | `prather2021_influenza` | 32236831 | T5 | Vaccine response in ages 18-25 specifically; localises the sensitive window to 2 nights pre-vaccination |
| 21 | `jaiswal2024_breakthrough` | 38409137 | T4 | Strongest null: objective sleep, real-world COVID breakthrough, n=5,265+2,583 |
| 22 | `zhang2023_mr_inflammation` | 37535878 | T3 | Only Mendelian randomization record; causal direction runs inflammation→sleep |
| 23 | `stager2023_adolescent_crp` | 37395694 | T5 | Required #7. Only longitudinal adolescent-exposure study with objectively measured adult CRP |
| 24 | `moralesmunoz2024_alspac` | 38717746 | T5 | Only prospective evidence of a persisting inflammatory trace (IL-6) after sustained short sleep in the young |
| 25 | `fondell2011_nk_tcell` | 21496482 | TX | Cleanest demonstration that immune markers move in OPPOSITE directions under short sleep |

All 25 identifiers returned `crossref_ok: true` and `pubmed_ok: true`; the DOI recorded in PubMed
matched the asserted DOI for all 25; Crossref-vs-PubMed title similarity was 1.000 for 24 of 25 and
0.991 for the remaining one (`spiegel2002_influenza_vaccine`, a punctuation difference in the JAMA
letter title). **Zero identifiers failed verification.**

---

## Excluded (19) — with reasons

### Excluded: primary studies already pooled inside an included meta-analysis (avoiding double-counting)

| Candidate | PMID | Reason for exclusion |
|---|---|---|
| Vgontzas AN et al. Adverse effects of modest sleep restriction on sleepiness, performance, and inflammatory cytokines. J Clin Endocrinol Metab 2004 | 15126529 | Pooled inside `irwin2016_inflammation_meta` and `ballesio2026_experimental_meta`. Its 6 h × 1 week IL-6 result is already represented, and the same group's `pejovic2013_recovery` (included) supersedes it by adding the recovery arm |
| Meier-Ewert HK et al. Effect of sleep loss on C-reactive protein, an inflammatory marker of cardiovascular risk. J Am Coll Cardiol 2004 | 14975482 | Pooled inside both included inflammation meta-analyses. Extracting it separately would double-count the CRP experimental evidence |
| Mullington JM et al. Cardiovascular, inflammatory, and metabolic consequences of sleep deprivation. Prog Cardiovasc Dis 2009 | 19110131 | Narrative review, superseded by `besedovsky2019_review` (more recent, more comprehensive, immunology-specific) |
| Ayling K et al. Positive mood on the day of influenza vaccination... Brain Behav Immun 2018 | 28923405 | Pooled inside `spiegel2023_vaccine_meta` (self-report arm). Population is 65-85 y — `poor_elderly`, the age group whose exclusion *created* the significant self-report effect. Retaining it separately would add an elderly cohort with no transportability to an 18-year-old |
| Schmid SM et al. and Baek et al. multi-night restriction studies | — | Identified only as the named outlier studies inside `ballesio2026_experimental_meta` (Schmid 2011 d=−1.38 for IL-6; Baek 2020 d=−0.70 for CRP). I recorded BOTH the outlier-included and outlier-excluded pooled estimates in that record rather than extracting the outliers separately, which preserves the information without cherry-picking |

### Excluded: wrong outcome domain (no immune, infection, vaccine or inflammatory endpoint)

| Candidate | PMID | Reason |
|---|---|---|
| Sivertsen B et al. Sleep across the pandemic in Norwegian university and college students, 2010-2023. J Sleep Res 2026 | 41711230 | Large student sleep-epidemiology series but **no infection or immune outcome** — descriptive sleep prevalence only. Closest hit to "college students + sleep" in my searches, and it has no immune data |
| Mizumoto A et al. Lifestyle and psychological factors associated with depression in college students. J Prev Med Public Health 2025 | 40841977 | Outcome is depression; belongs to a psychiatric shard |
| Kim S et al. Perceived financial hardship and sleep duration among Korean adolescents. Sci Rep 2025 | 40721479 | Sleep is the *outcome*, not the exposure; no immune measure |
| Mitchell J et al. Inequities in sleep duration and quality among adolescents in Canada. BMC Public Health 2024 | 39334116 | Descriptive sleep epidemiology in adolescents; no immune or infection outcome |
| Cotter DL et al. Sleep duration/efficiency, pollutant exposure and white matter integrity in adolescence. bioRxiv 2025 | 39990345 | Brain-structure outcome; also a preprint |
| Tian T et al. Circadian clock genes: potential therapeutic targets for autoimmune diseases. J Autoimmun 2026 | 41411761 | Mechanistic/therapeutic review of autoimmunity, largely preclinical; not sleep-duration exposure in humans |

### Excluded: exposure not interpretable as chronic sleep restriction, or hopelessly confounded

| Candidate | PMID | Reason |
|---|---|---|
| Ferreira ABM et al. Sleep restriction and intensified training on mucosal immunity in young soccer players. J Strength Cond Res 2026 | 42139594 | **Genuine near-miss and worth flagging.** 16 male youth athletes, actigraphy, salivary IgA + URTI severity — right population, right outcome. Excluded because the sleep reduction was only **−44 min vs baseline (~10%)**, nowhere near a 5-6 h schedule, and it is completely confounded with a **75% increase in training load** in the same week. There is no sleep-only contrast. Directionally consistent with harm (URTI severity rose only in the reduced-sleep week), but not usable as an effect estimate |
| Yu JE, Eun D, Jee YS. Daily life patterns, psychophysical conditions, and immunity of adolescents in the COVID-19 era. Healthcare 2022 | 35742203 | Retrospective quasi-experimental + qualitative interviews during lockdown; sleep is one of many "daily life patterns", immunity measures are non-specific, and lockdown confounds both exposure and infection opportunity |
| Louis J et al. Impact of sleeping with reduced glycogen stores on immunity and sleep in triathletes. Eur J Appl Physiol 2016 | 27491620 | Exposure is a nutritional/glycogen manipulation, not sleep restriction; athletes |
| Smith TJ et al. Supplemental protein and a multinutrient beverage speed wound healing after acute sleep restriction. J Nutr 2022 | 35285906 | Randomises a *nutritional* intervention, not sleep; wound healing is a peripheral immune outcome and the sleep arm is not the contrast of interest |
| Zhu Y et al. Sleep behaviors modify the association between hemoglobin concentration and respiratory infection. Front Physiol 2025 | 41098689 | Sleep enters only as an *effect modifier* of a haemoglobin-infection association; no main effect of sleep duration on infection is estimable |

### Excluded: could not obtain and no usable secondhand numbers

| Candidate | Identifier | Reason |
|---|---|---|
| Comment on Zhang et al. MR analysis. Sleep 2023;46(10):zsad223 | doi 10.1093/sleep/zsad223 | A published Comment that may qualify `zhang2023_mr_inflammation`'s conclusions. I did not retrieve it. **Flagged as a known gap in my reading** rather than silently ignored |
| Spiegel 2002 full text (JAMA research letter) | PMID 12243633 | *Not excluded as a record* — retained as `spiegel2002_influenza_vaccine` with `access_tier: secondhand`. Logged here because the **full text itself** could not be obtained: paywalled, no PubMed abstract, no PMC deposit, and a WebFetch of the JAMA page timed out. All its numbers come from three Crossref-verified secondary sources |

---

## Access-tier accounting for the 25 included records

Both tables below are read directly out of the YAML `access_tier:` and `tier:` fields rather than
tallied by hand, and both sum to 25.

| access_tier | n | Records |
|---|---|---|
| `full_text` | 16 | ballesio2026, benedict2012, besedovsky2019, cohen2009, forthun2023, irwin2016, martinezalbert2025, patel2012, pejovic2013, prather2012_hepb, prather2015, pratherleung2016, simpson2016, spiegel2023, stager2023, vanleeuwen2009 |
| `abstract_only` | 8 | faraut2011, fondell2011, jaiswal2024, lange2003, lange2011, moralesmunoz2024, prather2021, zhang2023 |
| `secondhand` | 1 | spiegel2002 |

## Tier distribution

| tier | n | Records |
|---|---|---|
| T1 randomized / within-subject lab protocol (incl. meta-analyses of such) | 10 | ballesio2026, benedict2012, faraut2011, lange2003, lange2011, pejovic2013, simpson2016, spiegel2002, spiegel2023, vanleeuwen2009 |
| T2 quasi-experiment | 2 | cohen2009, prather2015 |
| T3 Mendelian randomization | 1 | zhang2023 |
| T4 prospective cohort, objective exposure | 2 | jaiswal2024, prather2012_hepb |
| T5 prospective cohort, self-reported exposure | 4 | moralesmunoz2024, patel2012, prather2021, stager2023 |
| TX cross-sectional / review / context-only | 6 | besedovsky2019, fondell2011, forthun2023, irwin2016, martinezalbert2025, pratherleung2016 |

`spiegel2023_vaccine_meta` is tiered T1 despite `design: meta_analysis_observational` because 3 of its
7 pooled studies are experimental restriction protocols and the authors reanalysed participant-level
data; its prospective-only subgroup estimate (0.67) is reported separately in the record so the pooler
can down-weight if it disagrees with that call.

## Population-match distribution

Relevant because the target is 18 years old. From the YAML `population.adolescent_match:` fields:

| adolescent_match | n | Records |
|---|---|---|
| `exact_16_19` | 1 | stager2023 |
| `good_young_adult` | 9 | benedict2012, faraut2011, lange2003, lange2011, martinezalbert2025, pejovic2013, prather2021, spiegel2002, vanleeuwen2009 |
| `fair_adult` | 3 | fondell2011, prather2015, simpson2016 |
| `poor_midlife` | 4 | cohen2009, patel2012, prather2012_hepb, pratherleung2016 |
| `mixed` | 8 | ballesio2026, besedovsky2019, forthun2023, irwin2016, jaiswal2024, moralesmunoz2024, spiegel2023, zhang2023 |

Only **one** record has adolescent-exact exposure, and it is a null. Ten of 25 are `good_young_adult`
or better, but every one of those is a short-term lab protocol — none follows adolescents over years.
