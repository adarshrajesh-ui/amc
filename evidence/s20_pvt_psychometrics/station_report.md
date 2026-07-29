# station_report.md — shard `s20_pvt_psychometrics`

**Domain:** the measurement science needed to make a 4-week n-of-1 self-experiment statistically real, and
the quantitative basis for the claim that the subject cannot tell how impaired he is.

**Output:** 44 records screened, **31 included**, 13 excluded, **108 effect estimates**, all validating
against `effect.schema.json`. Deliverables: `protocol_basis.md`, `screening_log.md`, this report, and one
YAML per study.

---

## 1. The headline finding, and it is not the one the brief expected

The brief asked me to compute the number of nights per condition for 80% power. I did, and the answer is
that **the 4-week protocol cannot deliver it for a 1–2 h contrast.**

```
Required:  31 analysed nights per condition (62 nights), assuming independent nights
           20–28 calendar weeks once night-to-night dependence is modelled
Available: 28 nights → 11–16% power → minimum detectable effect ≈ 5 h/night of deficit
```

The arithmetic is in `protocol_basis.md` §5 and reduces to
`n = 2(1.960 + 0.8416)²/d² = 15.6978/0.5314 = 29.5`, then 31 with the exact-t correction, where
`d = 0.212/0.225 × 0.773 = 0.729`.

I want to be explicit that this is the shard's most decision-relevant output, because a 4-week study that
reports "no significant effect" at 11–16% power would be reporting its own weakness as if it were a fact
about the subject, and that is the specific way this self-experiment is most likely to mislead. The fix is
cheap and is spelled out in §8: **widen the contrast to 3 h, lengthen the periods to 14 nights, run 12
weeks, and test 5 times a day with evening weighting → 78–96% power.** If only 4 weeks are available, the
study must be declared in advance to be an estimation and feasibility exercise that reports an interval.

## 2. The six numbers the report needs from me

| Quantity | Value | Provenance |
|---|---|---|
| Primary outcome | **mean 1/RT** on a 3-min PVT-B, 355 ms lapse threshold | 6 independent datasets converge (`protocol_basis.md` §1) |
| Within-person SD at rested baseline | **4.0–4.14% of own mean** (lab); **6.0%** used for planning | Basner Table 4 and Thompson SEM%, two independent routes |
| Expected effect, 2 h/night contrast | **0.212 s⁻¹ ≈ 5.7% of own mean** at 4.5 nights exposure | Pejovic 4.7–7.9%; Basner × Van Dongen linearisation 5.7% |
| Nights per condition for 80% power | **31 analysed nights** (62 total); 20–28 weeks with dependence | derived, arithmetic shown |
| Actigraphy nights for habitual duration | **14 minimum, 28 preferred** | Knutson variance components: 13 nights for R = 0.80, 15 for SEM ≤ 20 min |
| Practice-effect washout | **≥ 5 discarded familiarisation sessions** + retained log(session) covariate | Basner 2020 speed β = 0.02 (P = 0.44) but accuracy β = 0.09 (P = 0.02) |

Plus the physiological washout, which is a separate and larger constraint: **≥ 4–5 nights** of extended
sleep before an extension period's data are clean, because "only 1 h of PSD takes four days to recover".

## 3. What I did that goes beyond transcription

- **Reconstructed and independently verified two mangled tables.** Basner 2011 Table 4 arrived
  column-interleaved from the PDF text layer. I reconstructed the column assignment and then verified it by
  recomputing all 14 published required-sample-sizes from the published effect sizes using the authors'
  own stated method; all 14 reproduced to ±1 subject. Same procedure for Van Dongen 2004 Table 2 and Rupp
  2012 Table 3, recomputing every ICC from the published variance components (13 and 4 respectively, all
  matching to ±0.003).
- **Derived the actigraphy night-count from variance components rather than quoting a convention.** Knutson
  publishes SDs, not night counts. I derived the single-night ICC (0.236), the Spearman-Brown counts and
  the precision-based counts, and argued which route applies to an n-of-1 (the precision route, because the
  reliability route depends on between-person variance, a quantity that does not exist with one subject).
  The two routes happen to converge on two weeks.
- **Cross-validated the effect size two ways.** A Pejovic-based route (4.7–7.9% of baseline) and a
  Basner-slope × Van Dongen-critical-wake-duration linearisation (5.7%) agree. Independent datasets,
  independent methods.
- **Cross-validated the σ two ways.** Basner's paired-difference SD implies ≤ 4.00% of the mean; Thompson
  independently measured 4.14%. Different labs, different test durations, different statistics.
- **Modelled the dependence structure explicitly** rather than assuming independent nights, including the
  AR(1) design-effect table and the period-level variance floor (effective nights per period is capped at
  1/φ no matter how long you measure). This is what turns a comfortable 31 nights into an uncomfortable
  20–28 weeks, and it is the part most likely to be omitted by a less careful analysis.

## 4. Where I contradicted the brief or the literature, and reported reality

Four places, all recorded in the relevant YAML:

1. **The PVT-B paper reports no correlation with the 10-min PVT.** The brief asked for "the correlation and
   the effect-size attenuation". The attenuation exists (22.7%, range 6.9–67.8%). A correlation coefficient
   does not appear anywhere in that paper; the authors validated concordance with effect-size comparison and
   mixed-model version × time interaction tests over 1,656 paired administrations. I did not manufacture an
   `r`. The nearest verified PVT-shortening correlation is in Grant 2017.
2. **PVT test-retest reliability is not "above 0.8".** That claim is repeated verbatim in both Basner 2011
   papers, sourced to a 2005 book chapter I could not retrieve and for which no identifier resolves. The
   directly measured values I did retrieve are 0.51 (lapses, n = 372), 0.69 (median RT, n = 372), 0.79
   (mean RT, between-day) and 0.83 (fastest 10% RT). I did not propagate the 0.8 figure.
3. **The PVT is not practice-effect-free.** Response *speed* genuinely is (β = 0.02, P = 0.44 across 15
   administrations), but *accuracy* is not (β = 0.09, P = 0.02), Thompson found a significant systematic
   mean-RT shift between sessions 1 and 2 (P = 0.01), and Van Dongen 2004 found the PVT was the one measure
   of 13 with a significant order effect (F = 4.36, P = 0.014) — in the direction of getting worse.
4. **Pejovic's Results text and Table 3 disagree.** The text calls three PVT contrasts "significant" where
   the table gives P = 0.08, 0.07 and 0.03. I extracted the table values, which means the honest reading is
   that a 2 h/night restriction for 6 nights produced only a *marginal* group-level PVT lapse effect with
   n = 30. That is inconvenient for the report's narrative and it is the single most important input to my
   power calculation, so it must not be softened.

I also refused one tempting shortcut: Cohen 2010's forced-desynchrony effect sizes are enormous and would
have made the power calculation look comfortable. That exposure is nothing like a 1–2 h nightly contrast, so
I used the paper directionally (evening-weighted testing) and kept its numbers out of the arithmetic.

## 5. The dissociation evidence is strong, and one common version of it is wrong

The "you cannot tell how impaired you are" claim is well supported, and the best single form of it is a
within-study contrast rather than a correlation: over 14 days of restriction in the same people on the same
days, PVT lapses accumulated near-linearly (θ = 0.78 ± 0.04) while Stanford Sleepiness Scale ratings
plateaued (θ = 0.24 ± 0.04), and the authors ruled out a scale ceiling by showing θ = 0.86 ± 0.14 for the
same scale under total deprivation. Sleep debt correlates r = 0.052 with subjective sleepiness and r = −0.486
with objective sleepiness in the same men. And for recovery — the part that matters most, because the subject
will otherwise stop after two good nights — Pejovic measured all three signals in the same 30 people:
subjective sleepiness and MSLT latency both came back *better than baseline* after 2 nights of 10 h TIB
while PVT lapses were *still worse than baseline* and had not improved at all from the restricted state.

**The wrong version to avoid:** "objective measures recover more slowly than subjective ones" is not
generally true, and Kitamura found the opposite ordering. Three things get called objective and they recover
at different rates — sleep propensity (MSLT/MWT) fastest and sometimes overshooting, subjective sleepiness
fast and saturating, attentional performance (PVT) slowest. The defensible claim is specifically about the
PVT. I have flagged this in two records because it is the kind of overreach that would be easy for a
downstream writer to commit.

## 6. My confidence, by component

| Component | Confidence | Why |
|---|---|---|
| Choice of primary outcome (mean 1/RT over lapses) | **High** | Six independent datasets, four different designs, unanimous |
| Effect size for a 2 h/night contrast | **Moderate** | Two independent routes agree, but both are in adults and one relies on a dose linearisation |
| Within-person σ at rested baseline | **Moderate** | Two independent routes agree to within 4%, but both are laboratory figures and the ×1.5 field factor is an assumption |
| Night-to-night dependence (ρ, φ) | **Low** | **Entirely assumed.** No published value for a free-living daily PVT series that I could retrieve |
| Required sample size | **Moderate** for the ordering, **low** for the precise number | The answer moves between 7 and 238 nights per condition across plausible inputs (§7 sensitivity table). What is robust is the *conclusion*: 4 weeks is short by roughly a factor of three or more |
| Actigraphy night count | **High** | Derived from published variance components and corroborated by three independent recommendations |
| Ad-lib protocol specification | **High** | Two full-text protocols, one of which reaches an asymptote and one of which demonstrates that 3 days does not |
| Practice-effect requirement | **High** for the direction, **low** for "5 sessions" | The β values are solid; the session count is my design choice, and I have labelled it as such |
| Subjective/objective dissociation | **High** | Multiple within-study, same-subject, same-day contrasts |
| Transportability to an 18-year-old | **Low** | See §7 |

## 7. The single biggest gap in the evidence for my domain

**There is no published within-person, day-to-day variance structure for a free-living daily PVT series in
an adolescent or young adult.** Everything downstream of that gap is an assumption:

- σ_w comes from two *laboratory* sources (Basner's 3-bout daily means under controlled conditions;
  Thompson's two-session test-retest in females aged 20–63). The ×1.5 inflation to field conditions is a
  number I invented for lack of anything better, and it enters the sample size **quadratically**.
- The night-to-night autocorrelation ρ, and the period-level state-variance share φ, have **no empirical
  basis at all** in my records. They are the difference between "62 nights" and "20–28 weeks" — a factor of
  three to four in the study's duration. I searched the operational-PVT literature (Arsintescu 2019/2020/2022)
  specifically for this and none of it reports an extractable within-person variance parameter.

Two consequences the downstream model should absorb:

1. **Inflate the uncertainty on my sample size substantially, and treat the direction as the finding rather
   than the number.** "4 weeks is short by a factor of ~3, and the shortfall is dominated by two unmeasured
   variance parameters" is what I can actually defend.
2. **The protocol should be designed to measure its own parameters.** A two-week run-in at a constant TIB,
   with the full daily PVT battery, would estimate σ_w and ρ directly for this subject and convert the whole
   calculation from assumption to measurement. I have put this in `protocol_basis.md` §7 as a precondition
   rather than an optional refinement. Fixing the duration first and discovering σ_w afterwards is how
   self-experiments end up uninterpretable.

**A close second gap: age.** Only 3 of my 31 records are `exact_16_19` — Acebo 1999 (actigraphy night counts),
Wilson 2010 (PVT reliability in a classroom) and Short 2018 — and a further 6 are `good_young_adult`. The
remaining 22 are adults, including **every record that contributes to the effect size or the σ**: Pejovic
mean age 24.7 is the closest, then Basner 22–45, Thompson 20–63, Knutson 38–50.

`short2018_adolescent_sleep_need` is the one record that ran almost exactly the manipulation this protocol
needs (7.5 h vs 10 h TIB for 5 nights, 10-min PVT every 3 hours, ages 15–17), and its per-condition means and
effect sizes sit behind a paywall that no route I tried could open (publisher returns HTML to non-browser
clients, no PMC deposit, no Wayback snapshot). **Retrieving `10.1093/sleep/zsy011` in full is the single
highest-value action anyone could take on this shard's behalf**, because it would replace the adult-derived,
linearisation-dependent Δ with a directly measured, age-matched one. The direction of the current bias is at
least favourable: adolescents need more sleep and are more affected per hour lost, so an adult-derived Δ
probably understates the effect, making my sample sizes conservative in the useful direction.

## 8. De-duplication notes for the pooler

- `basner2011_pvt_metrics` and `basner2011_pvtb` and `basner2011_pvtb_fitness_for_duty` share the
  `UPenn_Dinges_TSD_PSD` cohort family and overlapping subjects. **Not independent; do not pool as three
  studies.**
- `vandongen2004_traitlike`, `rupp2012_traitlike`, `yamazaki2020_traitlike` and `dennis2017_traitlike` share
  laboratory lineage and probably some individuals. The trait-ICC estimate is best treated as one finding
  replicated four times, not four independent estimates.
- `vandongen2003_subjective_plateau` will also be extracted by shards s01 and s06. I deliberately took only
  the dissociation parameters (θ values, subjective-plateau statistics) and the sleep-need parameters
  (critical wake duration ξ), not the primary dose-response lapse effects. De-duplicate on
  `cohort_family: UPenn_Dinges_dose_response_2003`.
- Several records carry a `value` that is a placeholder encoding a qualitative finding (e.g. `1.0` meaning
  "confirmed, no numeric statistic published", or a `ci` field holding a published *range across metrics*
  rather than a confidence interval). Each such case says so explicitly in `conversion_formula` and warns
  against pooling. The pooler should filter on those notes rather than on `scale` alone.

## 9. Files produced

```
protocol_basis.md                        the powered protocol, with all arithmetic shown
screening_log.md                         44 records, every exclusion with a reason
station_report.md                        this file
31 × <study_id>.yaml                     108 effect estimates, all schema-valid
verify.sh  bioc.py  pmchtml.py           the retrieval and verification helpers I wrote
```

`pmchtml.py` is worth keeping: fetching and flattening rendered PMC HTML is the only route that worked for
non-open-access PMC deposits, where both the BioC and Europe PMC XML APIs refuse.
