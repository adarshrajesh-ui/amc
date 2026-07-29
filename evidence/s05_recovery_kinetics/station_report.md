# Station report - shard `s05_recovery_kinetics`

**Domain:** what actually happens when a chronically sleep-restricted person starts sleeping more.

| | |
|---|---:|
| Records screened (unique PMIDs) | 313 |
| Records included (one YAML each) | 30 |
| Effect estimates extracted | 110 |
| Identifiers verified against Crossref + PubMed | 34 |
| Identifiers that failed verification | **0** |
| Access: full text / abstract only / secondhand | 16 / 14 / **0** |
| Evidence tier: T1 / T4 | 29 / 1 |
| Population match: `exact_16_19` / `good_young_adult` / `fair_adult` / `poor_midlife` / `mixed` | 5 / 11 / 10 / 3 / 1 |
| Schema validation failures | **0** |

Deliverables in this directory: 30 `<study_id>.yaml` records, `recovery_dynamics.md` (the four required
analyses), `screening_log.md` (all 313 records with decisions and reasons), and this report.

## What I did

Two PubMed sweeps (22 queries; the first natural-language sweep under-returned because PubMed ANDs bare
keywords, so the second used field-tagged `[tiab]` boolean queries), plus citation-chasing out of included
papers' discussion sections, which is how I found four of the most valuable records (Cohen 2010,
Klerman & Dijk 2008, Leproult 2015, Zitting 2018). Bougard 2018 and Axelsson 2008 — the two longest
recovery observations in the classical literature — were found in Ochab 2021's discussion, not by search.

Every DOI and PMID was verified programmatically against `api.crossref.org` and NCBI E-utilities before
its record was written; results are in `/tmp/s05/verification.json`. All 34 resolved to the expected
title. Effect sizes were computed in a single auditable script (`/tmp/s05/compute.py`,
`/tmp/s05/final_ledger.py`) and the arithmetic is reproduced in each record's `conversion_formula`.

All seven required extractions were completed. Three notes on where reality differed from the brief:

- **Belenky et al. 2003** is paywalled. I extracted the recovery-phase numbers from the underlying
  technical report (Balkin et al. 2000, DOT-MC-00-133, n = 66 commercial drivers), which contains the
  per-night sleep and PVT tables the journal article summarizes. The brief's expectation of incomplete
  recovery is correct and I found the mechanism: recuperative sleep at 8 h TIB was only 6.19-6.58 h, no
  group slept above its own baseline, so no debt could be repaid. The DOT report describes a 4-day
  recovery period while the data and the JSR paper report 3 recovery nights; I recorded 3.
- **Klerman & Dijk** is two papers, not one. The 2008 Current Biology paper has the 8.9 h young-adult
  asymptote; a 2005 *Sleep* paper (PMID 16295210) from the same 16 h/24 h protocol has the day-1 rebound
  (+4.9 h). I extracted both and flagged them as the same `cohort_family` — their habitual-sleep ranges
  are identical (6.1-10.3 h), so the samples almost certainly overlap and must not be pooled.
- **Jones 2024** is the same University of Pennsylvania protocol family as Banks 2010, extended to a 12 h
  dose arm. Flagged as `UPenn_Dinges_SR_dose_response` on both records. Use Banks for numeric
  dose-response; Jones only for the mood domain.

I upgraded one record mid-session: `klerman2008` began as `secondhand` (numbers quoted through Kitamura
2016) and is now `full_text` after I located PMC2582347. That mattered — the full text yielded the
nocturnal-only asymptote (7.9 h), the days-to-asymptote figure (~5 days), and the PVT null after one 12 h
night, none of which were available secondhand. There are now **no secondhand records in the shard.**

## The six most decision-relevant estimates

| # | Finding | Number | Study | Tier |
|---:|---|---|---|---|
| 1 | Debt repaid by one recovery night at 10 h TIB | **2-4%** of a 23.4 h debt (+0.86 h, 51.5 ± 12.3 min, p<0.001) | Banks 2010, n=159 | T1 |
| 2 | Sustained sleep ceiling given 16 h/24 h in bed | **8.9 h** (95% CI 8.1-9.7); nocturnal-only **7.9 h**; 7.1 h spent awake in bed | Klerman & Dijk 2008, n=53 | T1 |
| 3 | Sleep need, days to asymptote, and debt in habitual short sleepers | habitual 7.37 h → asymptote **8.41 h** by **day 4**; debt **1.04 h/night** | Kitamura 2016, n=15 | T1 |
| 4 | Residual vigilance deficit after the largest single recovery night | PVT lapses **g = +0.43** (SE 0.15, p=0.008); ~**10.7 h TIB** needed to match controls | Banks 2010 | T1 |
| 5 | Weekend catch-up repayment | ad-lib weekend returns **+1.1 h** (≤9.2%); insulin sensitivity still falls **9-27%** | Depner 2019, n=36 | T1 |
| 6 | Vigilance not restored by repeated weekend recovery over 6 weeks | **β = −0.688**, p<0.001, monotonic, no plateau | Smith 2021, n=15 | T1 |

Supporting these, the four independent demonstrations of non-recovery at long follow-up are Ochab 2021
(7 days: ERPs, power spectra, accuracy, actigraphy), Rabat 2016 (13 days: salivary α-amylase),
Cheng 2026 (5 weeks: 74 genes) and Cohen 2010 (morning performance normal but the reaction-time slope
across the day nearly triples, 24 → 69 ms/h).

## My own confidence

**High confidence (multiple independent laboratories, consistent direction and magnitude):**

- Recovery sleep does not repay debt hour-for-hour; single-night repayment is a few per cent.
- The sustained sleep ceiling is ~8.4-8.9 h, and nocturnal-only sleep saturates near 7.9-8.1 h. Seven
  studies converge on 7.90-9.20 h with mean 8.51 h.
- Weekend-only catch-up is insufficient. This is the strongest claim in the shard because it follows from
  arithmetic that the ceiling makes inescapable (10-25% repayable at maximum; break-even needs 14-20 h
  per weekend night), and it is confirmed empirically by three multi-week studies in three countries.
- Subjective sleepiness and mood recover well before objective vigilance. Reported independently by six
  studies. This is the single most actionable behavioural point in the shard.
- Sleep *duration* asymptotes in about 4-5 days in the laboratory.

**Moderate confidence:**

- The 7-14 day free-living stabilization window rests largely on one observational study (Bei 2014), which
  is however the only one in exactly the target age band.
- Prior chronic short sleep slows the recovery trajectory. Rupp 2009 shows it clearly but n = 24 and the
  history manipulation was one week, not three years.
- Kitamura's 1.04 h/night debt estimate is precise-looking but comes from n = 15 Japanese men; the
  asymptote (8.41 h) is more trustworthy than the debt figure, which depends on the habitual measurement.

**Low confidence / explicitly extrapolated:**

- Any statement about how long a **3-year** exposure takes to resolve. The longest controlled restriction
  in existence is 6 weeks. My "3-6 weeks and possibly longer" is an extrapolation and is labelled as such
  in `recovery_dynamics.md` §2b and §3c. The downstream model should widen uncertainty here substantially.
- The Banks extrapolated intersection doses (10.66 h TIB for PVT lapses, >13 h for PVT speed). The authors
  themselves note the confidence intervals are large (7.97-13.34 h for lapses).
- Effects derived from p-values rather than dispersion — Smith 2021's betas, Zitting 2018's group
  contrasts, Simpson 2016's IL-6. Each is flagged `inferred_from_ci: true` with the derivation shown.
- Fourteen records are `abstract_only`. Eleven effects across the shard are encoded as direction
  indicators (`scale: probability`, `value: 1.0`, `se: null`) because the abstract stated a direction with
  no extractable magnitude. These carry no effect size and should not be pooled as if they did; I chose
  this over inventing numbers.

## The single biggest gap in the evidence for this domain

**No study has ever tracked recovery long enough, in an adolescent, to observe vigilance return to a
debt-free baseline — and the structure of the literature makes this gap self-concealing.**

Three facts compound into one problem:

1. **Follow-up is far too short.** Of 28 included records with a quantified recovery window, 11 (39%)
   observed 3 nights or fewer; the median is 7 days. The longest observation of *functional* recovery is
   13 days (Bougard 2018, Rabat 2016).
2. **Every extension of the window revealed more non-recovery, never less.** 1-5 nights: vigilance
   impaired. 7 days: ERPs, power spectra, accuracy, actigraphy impaired. 13 days: α-amylase suppressed.
   5 weeks: 74 genes dysregulated. There is no point at which looking longer showed things had quietly
   normalized. Short follow-up is therefore not conservative; it truncates observation before the
   slow-recovering measures become visible.
3. **The comparator is contaminated.** Klerman 2008 found healthy young adults not selected for short
   sleep habitually spent 8.5 h in bed against an 8.9 h need and slept more when allowed. So the
   "baseline" against which recovery is judged in nearly every study already carries a deficit, and every
   "returned to baseline" verdict is measured against a bar set too low.

Together these mean the literature systematically **understates** how long and how incompletely recovery
proceeds — the errors do not cancel, they compound in one direction. The honest position is that the upper
bound on recovery time for chronic restriction is unknown, and the available evidence is consistent with
it being considerably longer than any study has looked.

Two concrete, tractable items that would close much of this gap:

- **Zitting 2018 contains an unreported 10-day inpatient recovery segment at 10 h TIB following three
  weeks of chronic restriction with circadian disruption** ("After the three weeks of CSR-FD, there was a
  10-day recovery segment with a 10-hour sleep opportunity each night"). No recovery-phase outcomes appear
  anywhere in the paper — all reported results concern baseline and the three forced-desynchrony cycles.
  This would be among the longest controlled recovery observations in existence, in 18-27 year olds, and
  the data appear to have been collected. Worth requesting from the authors.
- **Almost no recovery kinetics exist in 16-19 year olds.** Only 5 of 30 records are `exact_16_19`, and
  only Lo 2022 (n = 194, ages 15-19) measures repeated restriction-and-recovery cycles with performance
  outcomes. Since Zitting 2018 shows young adults are *more* vulnerable than older adults (g ≈ 1.0 on two
  objective measures) while reporting *identical* subjective sleepiness, the adult-cohort recovery
  estimates that dominate this shard most likely **understate** the deficit in an 18-year-old. The
  downstream model should not shrink these effects toward zero on age grounds.

## Notes for the pooler

- `cohort_family` is set wherever overlap is plausible. Watch four clusters:
  `UPenn_Dinges_SR_dose_response` (banks2010, jones2024), `BWH_Klerman_bedrest_extension`
  (klerman2005, klerman2008), `BWH_Czeisler_CSR_FD` (zitting2018), and the Singapore adolescent
  programme (lo2022, which already pools Lo 2016 and Lo 2017 — both excluded for that reason).
- Three excluded records are same-cohort duplicates of included ones (Rupp 2010, Depner 2021, Lo 2016/2017)
  and are logged as `E6_same_cohort` in `screening_log.md`.
- Sign conventions vary by construct and are stated in every `direction_note`. For PVT lapses a
  **positive** g means worse (more lapses); for MWT latency a **negative** g means worse. Do not assume a
  uniform harm direction.
- Van Dongen 2003 (PMID 12683469) is excluded here as belonging to the cognition dose-response shard; its
  recovery phase is reported without extractable per-night numbers.
- `scale: years` is used twice as a generic numeric-duration scale for day counts (klerman2008
  days-to-asymptote, bei2014 days-to-stabilize) because the schema enum has no `days` option. The `unit`
  field states days explicitly in both cases.
