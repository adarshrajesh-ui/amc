# Red-team report: the case that the damage is negligible

**Station:** adversarial review board, contrarian seat.
**Mandate:** argue as forcefully as the evidence permits that the true damage from this exposure is
negligible and essentially entirely recoverable, and that the report overstates harm.
**Constraint:** no fabricated citations, no misrepresented studies. Every number below is either
computed by code in this repository or quoted from a `VERIFIED` record in `evidence/`.

**Reproduce with:** `python3 src/redteam_contrarian.py` → `reports/redteam_contrarian_numbers.json`.
That script imports the project's own `exposure.py`, `synthesis.py`, `lifetable.py` and
`analysis_set.py` and reproduces the published headline numbers exactly before changing anything
(debt 3330 h vs published 3329 h; mean TST 5.59 h vs 5.591 h; vigilance *g* −0.873 vs −0.874).

**Check me with:** `python3 src/redteam_check_citations.py` and `python3 src/redteam_check_quotes.py`.
The first re-derives the citation appendix from `evidence/` and fails if any DOI, PMID, access tier
or verification status in this report disagrees with the corpus. The second fails if any quoted
string or load-bearing number is absent from the file it is attributed to. Both currently exit
clean; both caught real defects in my own draft, itemised at the end of the appendix.

---

## Bottom line, stated up front

I can move the headline numbers a long way and stay honest. Under the most favourable defensible
parameter set, cumulative debt falls from ~3300 h to **~930 h**, current vigilance *g* from −0.87 to
**−0.13 to −0.25**, measured IQ change from −0.7 to **−0.15 points**, and life-expectancy loss from
0.22 months to **~0.5 days**. The single largest concession the report should make is that its
"learning-loss channel" of *g* = −0.89 rests on one study while two randomised, age-matched, exact
nulls sitting in the same corpus were silently dropped because their effect rows carry `se: null`;
putting them back gives *g* ≈ **−0.34 with an interval that crosses zero**.

But I could not get to zero, and I want to be clear that this is not for want of trying. **Every one
of the 21 cells in my sensitivity grid returns a negative vigilance effect and a positive sleep
debt.** Two findings in particular survive my best attack essentially intact, and one of them
(`campbell2024`) directly contradicts the referent deflation that does most of the work in my own
recomputation. My verdict is at §4: the report's *permanent* damage numbers are about right, and its
*current-state* numbers are roughly 3–7× too alarming, but the honest case for "negligible" is
weaker than the brief hoped.

---

# 1. The strongest honest case that the damage is negligible

## 1.1 The exposure is overstated, and the shard that measured it says so

The model's own measurement shard concludes that the calibration it needs has never been measured,
and that the two available methods for supplying it disagree by more than anything else in the
calculation. Verbatim, from `evidence/s06_sleep_need_measurement/exposure_priors.md`, under a heading
that reads *"READ THIS FIRST: the sign of the correction is the biggest open question in this shard"*:

> "There are two defensible ways to turn a self-report into an estimate of true sleep, and **they
> disagree by 1.3-2.0 h for this subject — which is larger than any other uncertainty in the
> calculation.**"

The same document then recommends against the very correction that the headline number leans on:

> "**Use the reverse regression. Do not subtract the mean bias.** Subtracting a population-average
> bias from an individual's low report double-counts: it applies the average over-report *and* keeps
> the report's own downward extremity."

The published run does not take that advice: `calibration="mixed"` averages the recommended reverse
regression together with the naive mean-bias subtraction and with no correction at all, in thirds.
The one reverse-regression slope measured in age-matched adolescents is β = 0.19 (95% CI 0.13–0.26),
from actigraphy in 634 14–17-year-olds (`white2026ffcws`, DOI `10.1016/j.sleh.2025.10.003`,
PMID `41198487`):

> "The estimate for calibration, the change in self-reported duration relative to the change in
> actigraphy-assessed duration, was beta = 0.19 (95% CI: 0.13, 0.26) after adjustment for sex,
> caregiver education, income, race and ethnicity."

The only other reverse regression retrieved gives β = 0.333 (95% CI 0.317–0.367) in 2086 adults
(`cespedes2016hchs`, DOI `10.1093/aje/kwv251`, PMID `26940117`). Both slopes move a 5.5 h report
*upward*, to 6.53 h and 5.96 h respectively — the opposite direction to the mean-bias correction,
which sends it to 4.50 h. Reported and true sleep correlate only r = 0.18 in age-matched
adolescents, so a low report is mostly regression to the mean.

**Consequence.** Using the shard's own recommended method at the only age-matched slope in the
literature, and changing nothing else, cuts the debt from 3330 h to **2286 h** and mean nightly
deficit from 3.20 h to 2.20 h.

## 1.2 If the reports were time in bed, the model used the wrong efficiency

The published model averages a "reports = TIB" branch in at 50% weight and converts with a sleep
efficiency of 0.875, taken from meta-analytic actigraphy at *habitual* time in bed
(`evans2021actigraphy`, DOI `10.1093/sleep/zsab088`, PMID `33823052`). But efficiency is not a
constant — it rises sharply as time in bed shortens, because sleep-onset latency collapses.
`campbell2024` measured this directly in 159 participants aged 9.9–22.8 (DOI
`10.1093/sleep/zsae216`, PMID `39283917`):

> "Average (±standard deviation [SD]) night 4 sleep duration of 525.8 ± 36.0 minutes with 10 hours
> TIB decreased to 470.1 ± 20.3 minutes with 8.5 hours TIB and decreased further to 401.7 ± 20.0
> minutes with 7 hours TIB."

That is 87.6% efficiency at 10 h TIB but **95.6% at 7 h TIB**. `campbell2021` gives the mechanism in
the same cohort: sleep-onset latency 21.4 min at 10 h TIB versus 3.7 min at 7 h TIB (DOI
`10.1093/sleep/zsaa280`, PMID `33507305`). A subject reporting 5–6 h in bed is in the
high-efficiency regime, not the 0.875 regime. Substituting 0.956 into the TIB branch alone moves the
debt from 3330 h to **3010 h** and raises mean TST from 5.99 h — a smaller lever than the
calibration, but it runs one way only.

## 1.3 The referent is a satiation ceiling, not a requirement

The model's need prior (9.00 h at 16, 8.70 h at 19) comes from three laboratory asymptotes. Read
what those asymptotes actually are. `klerman2008` (DOI `10.1016/j.cub.2008.06.047`,
PMID `18656358`) gave 35 healthy 18–32-year-olds **16 hours in bed per day** for 3–7 days:

> "Total daily sleep duration, which was initially longer than habitual sleep duration, declined
> during the experiment to asymptotic values that were 1.5 hour shorter in older (7.4 ± 0.4 s.e.m.,
> hour) than younger subjects (8.9 ± 0.4)."

That is the duration to which sleep *falls* when opportunity is unlimited. `short2018sleepneed`'s
9.0 h is the analogous quantity at 10 h TIB (DOI `10.1093/sleep/zsy011`, PMID `29325109`), and
`kitamura2016`'s 8.41 h is an exponential-decay asymptote over nine extended-sleep nights (DOI
`10.1038/srep35812`, PMID `27775095`). None of the three is a measurement of the duration below
which harm occurs. They measure sleep *capacity*.

The quantities that do estimate a functional optimum are consistently lower, and they come from
samples three orders of magnitude larger:

| Outcome | Optimum | Source | n |
|---|---|---|---|
| General cognitive ability (composite) | **7.38 h** | `wild2018` DOI `10.1093/sleep/zsy182`, PMID `30212878` | 10,886 |
| Cortical + subcortical volume and thickness | **6.5 h** (95% CI 5.7–7.3) | `fjell2023` DOI `10.1523/JNEUROSCI.2330-22.2023`, PMID `37365003` | 8,694 |
| Hippocampal volume | **6.3 h** (4.7–7.1) | `fjell2023` | 8,694 |
| All-cause mortality nadir | **7.0 h** | `yin2017` DOI `10.1161/JAHA.117.005947`, PMID `28889101` | 3,582,016 |

Guidelines agree that the model's referent sits at the top of the plausible band, not the middle.
The NSF panel puts 7–9 h as recommended for 18–25-year-olds, **6 h as "may be appropriate"**, and
only <6 h as "not recommended" (`hirshkowitz2015nsf`, DOI `10.1016/j.sleh.2014.12.010`,
PMID `29073412`), and adds: *"the panel emphasized that some individuals might sleep longer or
shorter than the recommended times with no adverse effects."*

`kitamura2016` also supplies the machinery to shrink the *individual* referent for a habitually
short sleeper, using its own data: optimal and habitual sleep duration correlate r = 0.514
(p = 0.050). Regressing optimal on habitual with that slope moves a subject whose habitual duration
is ~0.9 h below the sample mean to a predicted need of ~8.14 h rather than 8.41 h.

**The report already holds a lower number and chose not to headline it.** `exposure.py` computes a
second ledger against the NSF lower bound (8 h under 18, 7 h at 18 and over) on every run, and
`results.json` reports it: `cumulative_debt_vs_guideline_lower_bound_h` = **2195 h
[1066, 3044]**, 34% below the headline 3329 h. That figure is produced by the project's own code, on
the project's own uncorrected exposure, against a referent drawn from the guideline it cites. So the
sensitivity of the headline to the referent is not a contrarian construction; it is already in the
results file, one key away from the number that got quoted. Apply the calibration the measurement
shard recommends *as well*, and you are at my C1/C2 range.

## 1.4 Both sides of the subtraction must be on the same scale

This is the shard's own flagged failure mode, and it is stated as the largest available systematic
error in the whole pipeline. The NSF record's `notes` field says it in as many words:

> "The NSF bands are partly anchored on TIME-IN-BED-contaminated self-report. If the exposure engine
> expresses our subject's sleep as actigraphic/PSG TOTAL SLEEP TIME and compares it to these bands,
> it will OVERSTATE the sleep debt by roughly the TIB-TST gap (~0.8-1.5 h ...). Units must be matched
> on both sides of the subtraction. **This is the single largest systematic error available to the
> downstream model.**"

Two unit-consistent constructions are available. On the **self-report scale**: his reported hours
versus `wild2018`'s self-reported 7.38 h cognitive optimum → debt **1165 h**. On the **objective-TST
scale**: the reverse-regressed exposure versus the same reverse regression applied to `wild2018`'s
optimum (7.0 + 0.19 × (7.38 − 8.0) = 6.88 h) → debt **230 h**, with 38% of the posterior showing no
net debt at all.

I flag the second as a *reductio* rather than an estimate I endorse: at β = 0.19 the report is so
uninformative that essentially no exposure gradient survives. That is a real and damaging finding
about the precision the report claims, but it is not a licence to quote 230 h as the answer.

## 1.5 The largest single input to the vigilance headline is an estimate this project's own adjudicator rejected

`pvt_g_large_dose` pools five effects. The largest, and the only one in the subject's exact age band,
is `lo2016` at *g* = −2.399. The project's own adjudication document
(`reports/adjudication.md`, §A1) finds:

- the value is figure-digitised while carrying `quote: null`, which "violat[es] extraction hard-rule 2";
- it also carries the wrong canonical sign in the corpus (`value: +2.399` with `direction_note:
  "positive = worse vigilance"`);
- the alternative derivation route, `d = 2·sqrt(f²)` from a PROC MIXED group × day interaction, is
  ruled invalid in terms: *"The conversion does not hold."*

The blinded re-extraction recorded confidence `low` on this row and the two extractors disagreed by
the full sign (`reports/agreement.json`: `lo2016::1`, v1 +2.399, v2 −2.399).

Dropping it moves the pooled Bayes mean from −1.116 to **−0.778** and collapses heterogeneity from
I² = 78.8% to 28.1% — i.e. this one row *is* the heterogeneity. The project's own bias diagnostics
point the same way: PET recommends **−0.243** and trim-and-fill **−0.691** for the five-study pool.

There is also a dose argument. The pool mixes contrasts from 4 h TIB vs 10 h to 7 h vs 9 h, and the
resulting effects are not monotone in dose (4 h vs 10 h gives −0.91 while 5 h vs 9 h gives −2.40).
Restricting to the three contrasts nearest the subject's own shortfall (~2 h below referent:
`vandongen2003`, `belenky2003`, `pejovic2013_recovery_dissociation`) gives *g* = **−0.707**. The
single closest-matched study in the entire pool, `pejovic2013_recovery_dissociation` at 6 h vs 8 h
TIB for six nights, gives *g* = **−0.331** (DOI `10.1152/ajpendo.00301.2013`, PMID `23941878`).

## 1.6 A 5–6 h night preserves nearly all of the sleep that plausibly matters

Slow-wave sleep is actively defended under restriction. Five independent laboratories, five doses,
adolescents and adults, unanimous direction:

| Dose | Source | SWS / N3 | REM |
|---|---|---|---|
| 4 h TIB, 1 night, ages 14–16 | `kopasz2010` DOI `10.1111/j.1365-2869.2009.00742.x`, PMID `19656277` | **−5%** | **−70%** |
| 5 h TIB × 7 nights, adolescents | `ong2016` DOI `10.5665/sleep.5840`, PMID `27091536` | 101.1 vs 99.1 min, P = 0.75 | ↓ |
| 5 h TIB × 7 nights, ages 15–19 | `lo2016` DOI `10.5665/sleep.5552`, PMID `26612392` | no difference on any night (P = 0.23 / 0.36 / 0.10) | ↓ (P < 0.001) |
| 5 h TIB × 5 nights, ages 15–17 | `skorucak2021` DOI `10.1093/sleep/zsab106`, PMID `33893807` | unchanged; ↑ as %TST | ↓ every night |
| 7 h vs 10 h TIB, ages 9.9–16.2 | `campbell2021` PMID `33507305` | **+3 min** | −39 min |

`kopasz2010`, verbatim: *"During the 4-h night, we observed a curtailment of 50% of non-rapid eye
movement (non-REM), 5% of slow wave sleep (SWS) and 70% of REM sleep compared with the control
night."*

And the stage that *is* preferentially lost does not predict memory. The only meta-analysis of the
spindle→memory slope puts declarative memory at r = 0.210, falling to r = 0.131 in the subset least
exposed to selective reporting, with significant publication bias (`kumral2023`, DOI
`10.1016/j.neuropsychologia.2023.108661`, PMID `37597610`). Multiplying a 28–40% spindle loss
through that slope buys roughly 0.07–0.21 SD of declarative memory — an order of magnitude short of
the *g* ≈ −0.9 the report attributes to the learning channel.

**An hours-below-need ledger therefore overstates the biological insult**, because the hours removed
are disproportionately the ones with the weakest demonstrated function.

## 1.7 The "learning-loss channel" loses its significance when the age-matched nulls are restored

This is the finding I would most want the board to act on. `encoding_capacity_persisting` has
**k = 1**: `cousins2018` (n = 59, DOI `10.1111/jsr.12578`, PMID `28677325`), `access_tier:
abstract_only`, whose *g* = −0.89 is back-computed from a reported "P = 0.001" because the means and
SDs were never retrievable. It is one arm of one research programme — the record's own
`COHORT OVERLAP WARNING` names `huang2016`, `lo2016` and `ong2016` as members of the same
Need for Sleep protocol at the same boarding school, and warns they "are NOT independent
laboratories."

Meanwhile the corpus contains two randomised restriction experiments in 14–16-year-olds whose
declarative-memory results are exact nulls, both of which drop out of every pool because their effect
rows carry `se: null`:

- `voderholzer2011`, n = 88, five arms at 9 / 8 / 7 / 6 / 5 h for four nights (DOI
  `10.1016/j.sleep.2010.07.017`, PMID `21256802`). Title: *"Sleep restriction over several days does
  not affect long-term recall of declarative and procedural memories in adolescents."* Verbatim:
  *"groups who slept 9, 8, 7, 6 or 5h for four nights after learning showed highly similar levels of
  memory consolidation."*
- `kopasz2010`, n = 22, randomised crossover (PMID `19656277`). Title: *"No persisting effect of
  partial sleep curtailment on cognitive performance and declarative memory recall in adolescents."*

Adding those two rows (SEs approximated as sqrt(4/n) at *g* = 0; the corpus records none) moves the
channel from *g* = −0.890 [−1.533, −0.247] to **−0.315 [−1.649, +1.019]**. Adding `huang2016`'s two
GRE-vocabulary retention rows as well gives **−0.338 [−0.809, +0.132]**. Either way the interval
crosses zero.

Separately, `cousins2018` does not measure what the results file says it measures. Its design tests
the fate of **material studied during the restricted week**, retrieved after both arms had three
recovery nights. It shows that what you learn while short of sleep is learned less well. It says
nothing about whether encoding *capacity* is depressed once sleep normalises — yet
`results.json` reports it as
`encoding_capacity_g_persisting_after_recovery_sleep`, median −0.886, for a subject whose exposure is
ending. Three recovery nights is not permanence.

## 1.8 Every hard outcome is null under the strongest available design

| Outcome | Strongest design | Result |
|---|---|---|
| Alzheimer's disease | Mendelian randomisation, **9 analyses in 7 papers** | all null: `anderson2021` PMID `33150399`; `huang2020` PMID `32817390`; `henry2019` PMID `31062029` (−0.117, CI −0.400 to +0.166); `xiang2024` PMID `38865787` (IVW 0.002); `yuan2022` PMID `35918656`; `xiong2024` PMID `38301285`; `guo2024` PMID `38350061` |
| Alzheimer's, observational | dose-response meta-analysis | `xu2020` PMID `31879285`: shortest vs middle **RR 1.02 (0.76–1.36)** |
| All-cause dementia, short sleep | meta-analysis | `fan2019` PMID `31604673`: **RR 1.20 (0.91–1.59)**, null — while *long* sleep gives RR 1.77 (1.32–2.37) |
| Stroke | Mendelian randomisation ×2 | `guo2024_stroke_mr` PMID `38350061` null; `zhao2025_mr` PMID `40086821` null — while genetically instrumented *insomnia* is positive in the same paper |
| Total CVD | largest meta-analysis | `cappuccio2011` PMID `21300732`: **RR 1.03 (0.93–1.15)** |
| Total CVD at 6 h specifically | dose-response spline, 40 cohorts | `yin2017`: **RR 1.02**; stroke at 6 h **RR 0.99 (0.96–1.03)** |
| Myocardial infarction | Mendelian randomisation | `daghlas2019` PMID `31488267` |
| Adult BMI | Mendelian randomisation ×2 | `hayes2023` PMID `36790827`: **+0.039 SD/h (−0.06, +0.13)**, null and wrong-signed; `wang2019` PMID `30508554`: adult BMI MR null |
| Adolescent BMI | school-start-time quasi-experiment | `widome2023` PMID `37201593`: **−0.02 kg/m² (−0.6, +0.6)** at 2 y |
| Adolescent BMI, direction | bidirectional cohort, ages 16→21 | `sokol2020` PMID `31582778`: BMI → shorter sleep (β = −0.02, p < 0.01); **sleep → BMI null** |
| BMI, intervention | pooled trials | `yoong2016` PMID `27112069`: **−0.04 (−0.18, +0.11)** |
| CRP / IL-6 / TNF | meta-analysis, categorical short-sleep contrast (see caveat at §3.8) | `irwin2016_inflammation_meta` PMID `26140821`: **0.08 (−0.01, 0.16)** / **0.08 (−0.02, 0.18)** / **0.11 (−0.01, 0.22)** |
| Cortical thinning, 32 regions | longitudinal | `fjell2023` PMID `37798367`: **null in all 32**; MR on any MRI measure null |
| Full-scale IQ after 34–36 h total deprivation | quasi-experiment | `binks1999` PMID `10341383`: **+3.6 points (−1.8, +9.0)**; no decrement |
| Working memory, ages 9.9–22.8, 7 h vs 10 h TIB | randomised | `campbell2024` PMID `39283917`: Sternberg slope **+1.8 ms/item (−2.6, +6.2)**, null |
| Higher-order cognition, healthy-weight adolescents | randomised crossover | `duraccio2024` PMID `38767872`: effects present only in the higher-adiposity subgroup; *"No differences emerged for adolescents with healthy weight."* |
| ACT composite, 1 h later school start | quasi-experiment, exact age band | `hinrichs2011` DOI `10.1162/edfp_a_00045`: **−0.005 SD (−0.051, +0.041)** |
| Final adult height | shard synthesis | 0.0 cm (0.0–0.7), `evidence/s11_endocrine_growth/endocrine_summary.md` |
| 24 h growth hormone output | shard synthesis | 0.0% — redistributed, not lost |

## 1.9 Design gradients converge on zero

For BMI the whole ladder is present in one shard and it collapses monotonically
(`evidence/s09_obesity_bmi/station_report.md`, verbatim):

> "Cross-sectional gives 0.35 kg/m²/h → prospective 0.03 kg/m²/h → quasi-experiment −0.02 kg/m²
> (−0.6, 0.6) → MR +0.039 SD (p=0.42). Designs that break confounding and reverse causation all
> shrink the effect toward zero, and the three strongest designs in or near the target age band ...
> are **all null**."

That is a ~12× shrinkage from the weakest to the strongest design, ending in a null. The same
gradient appears elsewhere: 67% of the crude cardiovascular hazard attenuates on staged adjustment
in UK Biobank (`evidence/s08_cardiovascular/cardio_summary.md`); academic effects inflate 3–7× in
weaker designs (`evidence/s04_academic_natural_experiments/causal_summary.md`); and for mortality,
genetic instrumentation removes 72–100% of the association (`zhang2025` PMID `39883542`: 0% survives;
`sambou2024` PMID `38262521`: 28% survives).

The project's own E-value says how little is needed to finish the job: an unmeasured confounder
associated with both short sleep and death at RR ≈ 1.49 explains away the entire mortality
association (`results.json`, `bias_analysis`). Depression, socioeconomic position and undiagnosed
illness are all comfortably that strong.

## 1.10 The mortality number is a category error, and the exposure has ended

Three corrections, each documented, each multiplicative:

1. **Dose.** The headline RR 1.12 is a categorical bin that pools cutpoints from <5 h to <7 h
   (`cappuccio2010`, PMID `20469800`). At 6 h the `yin2017` spline gives **RR 1.01**; at 5 h,
   **1.04**. `itani2017` (5,172,710 people, PMID `27743803`) found mortality "linearly increased"
   only *below* six hours. The categorical estimate is 3–11× the dose-specific one.
2. **Sex.** The best dose-response meta-regression finds the short-sleep arm **null in males**:
   RR 1.02 (0.97–1.08) at 5 h and 1.02 (0.98–1.06) at 6 h (`liu2017`, DOI
   `10.1016/j.smrv.2016.02.005`, PMID `27067616`).
3. **Which exposure.** `zhao2023` (SHHS, PMID `36892074`) measured both instruments in the same
   people. PSG-defined 5–6 h gives HR 1.37 (1.10–1.71); **self-reported weekday 5–6 h gives HR 1.02
   (0.82–1.26)**, and self-reported 4–5 h gives 0.68. The authors report the two instruments were
   only weakly correlated. PSG-short sleep in a 64-year-old is fragmented, apnoeic, medicated sleep;
   the subject's exposure is the self-report kind, and that one is null at his dose.

Add the pattern match: `akerstedt2019` (PMID `29790200`) found that among under-65s, ≤5 h on
weekdays *with* ≥6 h weekend catch-up gives **HR 1.09 (0.77–1.54)** — null — against 1.65 for short
sleep on both. Short weekdays plus longer weekends is the subject's exact pattern.

Finally, the arithmetic of age. A US male's probability of dying between 16 and 19 is 0.0025, so
even a large hazard ratio across the window costs essentially nothing, and there is — as the report
itself concedes — **no evidence of any design that a time-limited adolescent exposure permanently
shifts a hazard**. Recomputed at the dose- and sex-specific hazard with the MR-bounded causal share,
total life-expectancy loss is **0.016 months, i.e. about half a day.**

## 1.11 What recovers, and what "incomplete recovery" actually rests on

Every physiological channel in `results.json` that carries a non-zero value is labelled reversible
by the project itself: testosterone −10.3%, reversing in 3 days (`leproult2011` PMID `21632481`);
insulin sensitivity, reversing in days to ~2 weeks; every immune marker normalising given adequate
recovery sleep; amyloid-β unchanged after 5–8 nights of 4 h sleep. `P(detectable permanent
structural change)` is set at 0.03 (0.01–0.10).

And the empirical basis for "recovery is incomplete" is thinner than the phrase implies. The
`residual_deficit_after_recovery_sleep` pool contains exactly two studies: `banks2010` after **one**
10 h recovery night and `pejovic2013` after **two**. That is the whole evidential foundation for a
claim about a three-year exposure. Of the 28 records in the recovery shard with a quantified window,
11 (39%) observed three nights or fewer, median 7 days
(`evidence/s05_recovery_kinetics/station_report.md`). Nobody has followed functional recovery beyond
13 days in anyone, and only 5 of 30 records are in 16–19-year-olds.

The comparator that matters for reversibility is smoking cessation before 40, which recovers nearly
all lost life expectancy. Against that benchmark, a three-year behavioural exposure ending at 19,
with 58 remaining years of life expectancy ahead of it, has no plausible mechanism for permanence
that the corpus supports.

---

# 2. Recomputation under the most favourable defensible parameters

## 2.1 Branch definitions

Every branch runs the project's own `exposure.py`. Only the named priors change.

| Branch | Calibration | Referent (need at 16 / 19) | Licence |
|---|---|---|---|
| **P** published central | mixed: 50% TIB branch; naive/reverse/none in thirds | 9.00 / 8.70 | as run |
| **C1** | reports = TST, reverse regression at β = 0.19 fixed | 9.00 / 8.70 | `white2026ffcws`, the only age-matched slope; shard's own recommended method |
| **C2** | as C1 | 8.14 / 8.14 | + `kitamura2016`'s own optimal-on-habitual slope (r = 0.514) |
| **C3** | none (reports as given) | 7.38 / 7.38 | unit-matched on the self-report scale vs `wild2018`'s optimum |
| **C4** | reverse, β = 0.19 | 6.88 / 6.88 | unit-matched on the TST scale (`wild2018` optimum through the same calibration) — *reductio* |
| **C6** | reports = TIB, efficiency 0.956 | 9.00 / 8.70 | `campbell2024` efficiency at restricted TIB; isolates this lever only |
| **C5 contrarian central** | reverse, β = 0.333 | 7.40 / 7.20 | `cespedes2016hchs` (larger, tighter) + functional-optimum referent |

## 2.2 Exposure

| Branch | Cumulative debt (h) | 95% CI | Mean TST (h) | Nightly deficit (h) | P(no net debt) |
|---|---|---|---|---|---|
| **P** published | **3330** | 1537 – 5073 | 5.59 | 3.20 | — |
| C6 TIB efficiency | 3010 | 1531 – 4484 | 5.99 | 2.89 | — |
| C1 calibration only | 2286 | 841 – 3720 | 6.67 | 2.20 | 0.001 |
| C2 + individual need | 1539 | 295 – 2773 | 6.67 | 1.48 | — |
| C3 unit-matched, report scale | 1165 | −280 – 2599 | 6.27 | 1.12 | — |
| **C5 contrarian central** | **927** | −519 – 2361 | 6.42 | 0.89 | 0.105 |
| C4 unit-matched, TST scale | 230 | −1216 – 1664 | 6.67 | 0.22 | 0.378 |

Published incremental debt attributable to the change at 16 was 843 h. Under C5 the *total* debt
against the requirement is about the size of the published *increment*.

## 2.3 Current cognitive deficit

Pooled vigilance effect, recomputed:

| Pool | k | Bayes μ | Frequentist μ | I² | PET | Trim-and-fill |
|---|---|---|---|---|---|---|
| all 5, as published | 5 | −1.116 | −1.136 | 78.8% | −0.243 | −0.691 |
| `lo2016` excluded | 4 | **−0.778** | −0.776 | **28.1%** | −0.533 | −0.671 |
| dose-matched (~2 h below referent) | 3 | **−0.707** | −0.725 | 39.5% | — | — |

Transported to the subject's dose with the project's own dose-transport model:

| | Vigilance *g* | 95% CI |
|---|---|---|
| Published | −0.874 | −2.85 – +0.58 |
| **Contrarian, project transport, `lo2016` dropped** | **−0.128** | −0.66 – +0.05 |
| **Contrarian, dose-matched pool anchored at its own 1.75 h shortfall** | **−0.245** | −1.71 – +0.37 |

Full 21-cell grid of medians (rows = exposure branch, columns = pooling choice):

| Branch | all 5 @3.7 h | no `lo2016` @3.7 h | dose-matched @1.75 h |
|---|---|---|---|
| **P published** | **−0.874** | −0.622 | −1.227 |
| C6 | −0.787 | −0.557 | −1.141 |
| C1 | −0.558 | −0.400 | −0.826 |
| C2 | −0.341 | −0.248 | −0.509 |
| C3 | −0.228 | −0.171 | −0.338 |
| **C5** | −0.165 | **−0.127** | −0.245 |
| C4 | −0.016 | −0.017 | −0.020 |

Two things to read off this grid. First, the dominant lever is the exposure calibration (rows), not
the meta-analysis (columns): changing *only* the calibration to the shard's own recommendation
already halves the headline. Second, **every cell is negative.** The dose-matched pool is also not
automatically favourable to me — under the published exposure it makes things *worse* (−1.227),
because correctly anchoring a 2 h contrast implies a steeper per-hour slope.

Learning channel, with the age-matched adolescent nulls restored:

| Pool | *g* | 95% CI |
|---|---|---|
| published (`cousins2018` only) | −0.890 | −1.533 – −0.247 |
| + `voderholzer2011`, `kopasz2010` | **−0.315** | −1.649 – +1.019 |
| + `huang2016` ×2 as well | **−0.338** | −0.809 – +0.132 |

## 2.4 Measured and permanent IQ change

Four routes, contrarian inputs, then the project's own Bayesian model averaging (weights
0.35 / 0.25 / 0.30 / 0.10):

| Route | Points | 95% CI |
|---|---|---|
| A vigilance × measured *g*-loading | −0.25 | −2.02 – +0.10 |
| B reasoning, chronic-scaled | −0.20 | −1.11 – +0.02 |
| C `binks1999` raw (+3.6) | +0.51 | −0.37 – +3.35 |
| C′ `binks1999` corrected for its 2.7-point baseline imbalance | +0.05 | −1.32 – +2.08 |
| D observational, at his dose only (`wild2018` 5.5 h, −0.083 SD) | −0.41 | −1.31 – +0.30 |
| **Measured IQ change now, contrarian** | **−0.15** | **−1.54 – +1.26** |
| Published comparator | −0.70 | −6.70 – +6.95 |

The interval narrows by a factor of ~5 as well as shifting, because most of the published width came
from `lo2016`-driven heterogeneity and from the mixed-calibration exposure.

Permanent change:

| Permanence prior | Points | 95% CI | P(>1 pt loss) |
|---|---|---|---|
| project's Beta(1.2, 18), mean 0.063 | −0.005 | −0.13 – +0.08 | 0.00002 |
| matched to the shard's own P(structural change) = 0.03 | **−0.002** | −0.07 – +0.04 | **0.00000** |

Published comparator: −0.020 [−0.535, +0.574], P(>1 pt) = 0.006. Both agree the permanent
component is indistinguishable from zero; my version is ten times tighter and the probability of a
1-point permanent loss is numerically zero in 400,000 draws.

## 2.5 Life expectancy

| Hazard input | HR while exposed | Window loss (mo) | Permanent residue (mo) | **Total (mo)** |
|---|---|---|---|---|
| Published: categorical RR 1.12 | 1.027 | −0.046 | −0.175 | **−0.223** |
| `yin2017` spline at 6 h, RR 1.01 | 1.002 | −0.004 | −0.014 | **−0.018** |
| **`liu2017` males at 6 h, RR 1.02, MR-bounded causal share** | 1.002 | −0.004 | −0.012 | **−0.016** |

**0.016 months = 0.49 days.** Against the same-footing comparators in `s18` — smoking 20/day 1.8
months, alcohol 200–350 g/week 3.0 months, physical inactivity 0.8 months — this is 1/110th of
smoking a pack a day for the same three years, i.e. a cigarette-equivalent of roughly **0.18 per
day**, versus the published report's 2.5 per day.

## 2.6 The prescription

The published 9.5 h time in bed is a deterministic function of the 8.70 h need prior. At a
functional-optimum referent it becomes:

| Need (TST) | Required TIB |
|---|---|
| 8.70 h (published) | 9.49 h |
| 7.40 h | 8.03 h |
| 7.20 h | **7.81 h** [6.27 – 9.35] |

A prescription of ~8 h in bed is achievable for a college student. A prescription of 9.5 h is at the
97th percentile of US young-adult sleep and, if the referent is wrong, converts a manageable
recommendation into a permanent sense of failure.

---

# 3. What I could not explain away

Listed strongest first. These are the findings that survive my best attack, and two of them
undercut my own recomputation.

**3.1 `campbell2024` refutes my referent deflation for vigilance — at doses above the subject's.**
In 159 participants aged 9.9–22.8, PVT signal-to-noise fell by 0.33 dB going from 10 h to 8.5 h TIB
and by a *further* 0.44 dB going from 8.5 h to 7 h (both p < .0001, PMID `39283917`). At 7 h TIB
these adolescents obtained 6.70 h of measured sleep — **more sleep than my own contrarian central
estimate for the subject (6.42 h)** — and were still measurably impaired relative to 10 h TIB. There
is no threshold in this dose-response anywhere near 7 h. My reply is that this is a state measure of
vigilance taken during restriction and therefore reverses, and that argument holds; but it means my
claim that "the true need is 7–7.5 h" is defensible only for the *durable* outcomes and is
straightforwardly wrong for vigilance.

The maturation-equivalent framing is worth stating precisely, because it is the most rhetorically
powerful number in the whole corpus and I want to be accurate about whose number it is. It is *not*
the authors' framing: it is the corpus's derivation, dividing the total 10 → 7 h deficit (0.77 dB) by
the paper's measured age slope (0.20 ± 0.03 dB per year of adolescent maturation) to give **−3.85
years (−5.34 to −2.36)**, with a documented delta-method SE. The record cross-checks it in the
authors' own percentage units — (7.3% + 9.6%) ÷ 4.7% per year = 3.60 years — and the two agree. So
the arithmetic is sound and the inputs are the paper's, but the "years of maturation lost" gloss is
constructed. Two honest deflations follow: it is a within-4-night state effect, not a permanent
maturational setback, and 7 h TIB is a *more* restricted schedule than the referent I argue for
rather than a sufficiency threshold. With those caveats stated, it is still a real T1 finding in the
right age band, and I cannot make it go away.

**3.2 The sign is stable everywhere.** All 21 grid cells are negative and all seven exposure
branches except the acknowledged *reductio* give a substantial positive debt. Under my own
contrarian central branch, 89.5% of the posterior still has him in net debt. I could not construct a
defensible parameter set that returns zero damage. The published multiverse's conclusion —
"every branch agrees that a substantial deficit accrued" — survives being attacked with a wider
multiverse than the one it ran.

**3.3 My key calibration slope is probably too flat for this subject, and I know why.** β = 0.19 and
β = 0.333 were both estimated from **single-item questionnaires**. This subject gave a structured
account: weekdays separately from weekends, plus exam nights, plus occasional long nights.
`arora2013` (PMID `23951321`) showed in 225 adolescents that sleep diaries correlated significantly
with actigraphy while single-item self-report did not. A structured report should shrink *less*, so
the true β is above 0.333 and my C1/C5 exposures are too optimistic. The shard's β = 0.50 is
labelled a judgement precisely because nobody has measured the right quantity. There is a second
problem: `white2026ffcws`'s actigraphic outcome was **sleep-period time** (first to last sleep epoch,
including onset latency and wake after sleep onset), not total sleep time — the record says so
verbatim — so the slope and the anchor are not on quite the same footing.

**3.4 `girschik2012` will not carry the weight the brief puts on it.** "Everyone reporting ≤6 h
actually slept >6 h" comes from n = 56 Australian women aged 18–80, and the paper's own next clause
is *"although group numbers were small."* The subject is a 16–19-year-old male. The one study that
stratified adolescent report bias by sex found boys **worse**: +1.9 h bias with ICC 0.06, against
+0.5 h and ICC 0.43 in girls (`guedes2016`, PMID `27532757`). Sex runs against me here, not for me.

**3.5 `short2018sleepneed` is T1, age-exact, and says 9 h.** Thirty-four 15–17-year-olds, ten days
in a sleep laboratory: sleep need ~9 h from 10 h TIB opportunities, and 9.35 h modelled as needed
"to maintain optimal sustained attention" (PMID `29325109`). My satiation-versus-requirement
distinction is a genuine argument, not a refutation. The 9.35 h figure in particular is *functionally*
defined — it is a PVT-lapse model, not a satiation ceiling — which is exactly the kind of quantity I
claimed supports a lower referent, and it points the other way.

**3.6 The recovery literature's asymmetry cuts against me and I cannot fix it.** The shard's finding
is that **every** extension of the observation window revealed *more* non-recovery, never less:
1–5 nights vigilance impaired; 7 days ERPs, power spectra, accuracy and actigraphy impaired; 13 days
salivary α-amylase suppressed; 5 weeks 74 genes dysregulated. I can honestly say the optimistic
direction is *unrefuted* because nobody has looked long enough. I cannot honestly say it is
*evidenced*. That is a materially weaker claim than my mandate wanted.

**3.7 Weekend catch-up cannot repay the ledger, and the metabolic evidence says it does not work.**
`depner2019` (PMID `30827911`) is titled *"Ad libitum weekend recovery sleep fails to prevent
metabolic dysregulation during a repeating pattern of insufficient sleep and weekend recovery
sleep"*: in the weekend-recovery arm, whole-body, hepatic and muscle insulin sensitivity fell 9–27%,
and cumulative recovery totalled only ~1.1 h above estimated need (≤9.2% of the debt). Under the
published exposure the arithmetic is decisive — a 16 h weekly weekday deficit against a maximum
weekend surplus of 3 h, i.e. 19% repayable. Under my own numbers the deficit is small enough that
weekends nearly cover it, but the structural point stands and it is not something I refuted.

**3.8 The immune signal is large, objectively measured, and at the right dose.** Actigraphic <5 h
versus >7 h gave OR 4.50 for developing a cold on viral challenge — 39.7% versus 12.8% in absolute
terms (`prather2015_rhinovirus`, PMID `26118561`). And `irwin2016_inflammation_meta`'s IL-6 estimate
is *not* null when sleep is measured objectively: SMD 0.29 (0.05, 0.52), verbatim from the paper's
Figure 4 stratum. I can say these reverse with adequate sleep, which the shard supports; I cannot
say they were never there.

I must also disclose a caveat that the same record raises against my own use of it in §1.8. The
null CRP and IL-6 estimates I cite there are *categorical* <7 h versus 7–8 h contrasts, and the
record's `notes` field flags exactly this: *"this means the <7 h bin lumps a 6.5 h sleeper with a
4 h sleeper, so a threshold effect below ~5-6 h could be diluted to null by this binning — a real
limitation when applying the null to a subject sleeping 5-6 h."* That is the same dose-dilution
argument I deploy *against* the report's categorical mortality RR in §1.10, and intellectual
consistency requires me to accept it here too. The honest scorecard for this paper is the one its
own record states: of 12 short-sleep tests, 10 null and 2 significant — and the binning that
produces most of those nulls is the binning I object to elsewhere.

**3.9 `yang2022` is the one longitudinal adolescent structural finding, and it did not attenuate.**
In propensity-matched ABCD pairs, the grey-matter volume difference between sufficient and
insufficient sleepers persisted essentially undiminished over two years (0.61, 95% CI 0.51–0.69;
PMID `35914537`). It is observational and the matching cannot rule out confounding — and the blinded
re-extraction disagreed on the value (0.61 vs 0.52) — but it is the wrong-signed datum for a claim of
full reversibility.

**3.10 `binks1999` is a null, not a positive, and I should not lean on it.** Its +3.6 IQ points sit
against a **+2.7-point baseline screening-IQ imbalance favouring the deprived group**, recorded in the
same YAML. Corrected, the effect is about +0.9 points. It is also 34–36 h of total deprivation in
n = 61, not chronic restriction. It supports "no large FSIQ decrement." It does not support "sleep
loss improves IQ," and the project's route-C weight of 0.30 on the uncorrected +3.6 is doing
unearned work in *my* favour as much as anyone's.

**3.11 The exposure at ages 14–16 was already below the requirement.** The published note is
correct: most of the debt against an age-appropriate referent predates the change at 16, because
6–8 h at 14–16 is also below the 8–10 h band. My contrarian branches shrink the *level* of the
deficit but do not create a clean pre-exposure baseline, and neither does the report.

---

# 4. Verdict

**The report is too alarming about the present, roughly right about the future, and — in one place —
too reassuring.**

**Too alarming, by roughly 3–7×, on the current-state numbers.** Three specific defects, in
descending order of size:

1. *Cumulative debt (~3300 h).* Built on a calibration the project's own measurement shard tells it
   not to use, averaged in at one-third weight, and compared against a satiation ceiling rather than
   a functional optimum, in violation of the unit-matching warning that the same shard calls "the
   single largest systematic error available to the downstream model." A defensible range is
   **900–2300 h**, and the number should not be quoted without the referent named in the same breath.
   The top of that range is not mine: 2195 h is the project's own
   `cumulative_debt_vs_guideline_lower_bound_h`, already sitting in `results.json`.
2. *Vigilance g = −0.87.* Roughly 40% of the pooled magnitude and essentially all of the
   heterogeneity comes from one row that this project's own adjudicator found rests on an invalid
   conversion, carries `quote: null` while figure-digitised, and was stored with the wrong sign. The
   project's own PET and trim-and-fill diagnostics recommend −0.24 and −0.69. A defensible current
   figure is **−0.13 to −0.35**, i.e. small, not large.
3. *The encoding deficit of g = −0.89 "said to persist after recovery sleep."* This is the report's
   single most alarming claim and it is its weakest. k = 1, abstract-only, back-computed from a
   p-value, one research programme — while two randomised age-matched exact nulls in the same corpus
   are excluded by a recording artefact (`se: null`). Restored, the channel is **−0.34 with an
   interval crossing zero**. The construct name is also wrong: `cousins2018` measured the fate of
   material studied while restricted, not a persisting capacity.

**About right on the permanent numbers.** Permanent IQ change ~0 with the interval including zero,
and life-expectancy loss on the order of tenths of a month, are conclusions I could not overturn —
only tighten. My recomputation moves permanent IQ from −0.02 to −0.002 points and life expectancy
from 0.22 months to 0.5 days. Those are refinements within "negligible," not a change of verdict.
The report deserves credit for getting there despite an inflated exposure and an inflated vigilance
pool, and for excluding dementia rather than assigning it a number.

**Too reassuring in one place: the prescription is presented as the deliverable it is least entitled
to be.** 9.5 h of time in bed is a deterministic transform of an 8.70 h need prior whose
between-person SD rests on **15 Japanese men** (`kitamura2016`), which the shard itself flags as thin.
The report's own value-of-information analysis says individual sleep need is the highest-value
measurement for exactly this output and that measuring it would collapse the interval almost
entirely. Issuing a specific 9.5 h number ahead of that measurement is the most confident claim in
the report and the least supported one.

**Where my own case is weakest, stated plainly.** The strongest honest case for the null is *not*
strong, and the brief asked me to say so if that was what I found. It is a case that the *magnitudes*
are inflated by a factor of a few, not a case that the effects are absent. Three of my load-bearing
arguments have known defects I could not repair: the flat calibration slope was measured on
single-item questionnaires and should not transport to a structured report (§3.3); `girschik2012` is
56 adult women and the one sex-stratified adolescent study runs against me (§3.4); and the referent
deflation is contradicted for vigilance by a 159-participant randomised experiment showing graded
impairment at doses *above* the subject's (§3.1). The sign never flipped in 21 attempts. A
contrarian who claims "negligible and entirely recoverable" for the current state is overreaching on
this evidence base. A contrarian who claims "small, mostly reversible, and much less than the
headline numbers suggest" is on solid ground, and that is where I would ask the board to land.

**The single change I would insist on** is not any of the numbers. It is that
`voderholzer2011` and `kopasz2010` be given standard errors and admitted to
`encoding_capacity_persisting`. Two randomised age-matched nulls are currently invisible to every
pool in the pipeline because of a blank field, and they happen to bear on the report's most alarming
claim. That is a data-integrity failure of the same family as the `task_id` collision the adjudicator
found, and it is currently working in one direction only.

---

## Appendix: citation verification

Every study named above resolves to a record in `evidence/` with `verification.status: VERIFIED`
(CrossRef and PubMed both checked by `src/verify_refs.py`). Identifiers as stored:

| study_id | DOI | PMID | access |
|---|---|---|---|
| `white2026ffcws` | 10.1016/j.sleh.2025.10.003 | 41198487 | full text |
| `cespedes2016hchs` | 10.1093/aje/kwv251 | 26940117 | abstract |
| `lauderdale2008` | 10.1097/EDE.0b013e318187a7b0 | 18854708 | full text |
| `girschik2012` | 10.2188/jea.JE20120012 | 22850546 | full text |
| `guedes2016` | 10.1590/1980-5497201600020011 | 27532757 | abstract |
| `arora2013` | 10.1371/journal.pone.0072406 | 23951321 | full text |
| `hirshkowitz2015nsf` | 10.1016/j.sleh.2014.12.010 | 29073412 | full text |
| `short2018sleepneed` | 10.1093/sleep/zsy011 | 29325109 | abstract |
| `klerman2008` | 10.1016/j.cub.2008.06.047 | 18656358 | full text |
| `kitamura2016` | 10.1038/srep35812 | 27775095 | full text |
| `evans2021actigraphy` | 10.1093/sleep/zsab088 | 33823052 | full text |
| `wild2018` | 10.1093/sleep/zsy182 | 30212878 | full text |
| `fjell2023` (cross-sectional) | 10.1523/JNEUROSCI.2330-22.2023 | 37365003 | full text |
| `fjell2023` (MR / longitudinal) | 10.1038/s41562-023-01707-5 | 37798367 | full text |
| `binks1999` | 10.1093/sleep/22.3.328 | 10341383 | full text |
| `lim2010` | 10.1037/a0018883 | 20438143 | full text |
| `lowe2017` | 10.1016/j.neubiorev.2017.07.010 | 28757454 | abstract |
| `campbell2021` | 10.1093/sleep/zsaa280 | 33507305 | full text |
| `campbell2024` | 10.1093/sleep/zsae216 | 39283917 | full text |
| `duraccio2024` | 10.1001/jamaneurol.2024.1332 | 38767872 | abstract |
| `hinrichs2011` | 10.1162/edfp_a_00045 | — | full text |
| `cousins2018` | 10.1111/jsr.12578 | 28677325 | abstract |
| `voderholzer2011` | 10.1016/j.sleep.2010.07.017 | 21256802 | abstract |
| `kopasz2010` | 10.1111/j.1365-2869.2009.00742.x | 19656277 | abstract |
| `ong2016` | 10.5665/sleep.5840 | 27091536 | full text |
| `skorucak2021` | 10.1093/sleep/zsab106 | 33893807 | full text |
| `kumral2023` | 10.1016/j.neuropsychologia.2023.108661 | 37597610 | full text |
| `banks2010` | 10.1093/sleep/33.8.1013 | 20815182 | full text |
| `pejovic2013` / `pejovic2013_recovery_dissociation` | 10.1152/ajpendo.00301.2013 | 23941878 | full text |
| `huang2016` | 10.5665/sleep.6092 | 27253768 | full text |
| `prather2015_rhinovirus` | 10.5665/sleep.4968 | 26118561 | full text |
| `lo2016` (Sleep 39(3)) | 10.5665/sleep.5552 | 26612392 | full text |
| `vandongen2003` | 10.1093/sleep/26.2.117 | 12683469 | full text |
| `belenky2003` | 10.1046/j.1365-2869.2003.00337.x | 12603781 | full text |
| `basner2011_pvt_metrics` | 10.1093/sleep/34.5.581 | 21532951 | full text |
| `irwin2016_inflammation_meta` | 10.1016/j.biopsych.2015.05.014 | 26140821 | full text |
| `cappuccio2011` | 10.1093/eurheartj/ehr007 | 21300732 | abstract |
| `cappuccio2010` (mortality) | 10.1093/sleep/33.5.585 | 20469800 | abstract |
| `yin2017` | 10.1161/JAHA.117.005947 | 28889101 | full text |
| `liu2017` | 10.1016/j.smrv.2016.02.005 | 27067616 | abstract |
| `zhao2023` | 10.1161/JAHA.122.027832 | 36892074 | full text |
| `zhang2025` | 10.1089/rej.2024.0058 | 39883542 | abstract |
| `sambou2024` | 10.1016/j.jad.2024.01.122 | 38262521 | abstract |
| `akerstedt2019` | 10.1111/jsr.12712 | 29790200 | full text |
| `itani2017` | 10.1016/j.sleep.2016.08.006 | 27743803 | abstract |
| `daghlas2019` | 10.1016/j.jacc.2019.07.022 | 31488267 | full text |
| `guo2024` / `guo2024_stroke_mr` | 10.1212/WNL.0000000000209141 | 38350061 | full text |
| `zhao2025_mr` | 10.1136/openhrt-2024-002866 | 40086821 | full text |
| `anderson2021` | 10.1093/ije/dyaa183 | 33150399 | full text |
| `huang2020` | 10.1212/WNL.0000000000010463 | 32817390 | full text |
| `henry2019` | 10.1093/ije/dyz071 | 31062029 | full text |
| `xiang2024` | 10.1016/j.sleep.2024.06.007 | 38865787 | abstract |
| `yuan2022` | 10.1186/s12877-022-03298-8 | 35918656 | abstract |
| `xiong2024` | 10.1016/j.psychres.2024.115760 | 38301285 | abstract |
| `fan2019` | 10.1016/j.jamda.2019.06.009 | 31604673 | abstract |
| `xu2020` | 10.1136/jnnp-2019-321896 | 31879285 | full text |
| `hayes2023` | 10.1002/oby.23668 | 36790827 | full text |
| `wang2019` | 10.1016/j.ypmed.2018.11.019 | 30508554 | abstract |
| `widome2023` | 10.1016/j.ypmed.2023.107548 | 37201593 | full text |
| `sokol2020` | 10.1038/s41366-019-0462-5 | 31582778 | abstract |
| `yoong2016` | 10.1002/oby.21459 | 27112069 | abstract |
| `weedon2022` | 10.1371/journal.pgen.1010356 | 36137075 | abstract |
| `leproult2011` | 10.1001/jama.2011.710 | 21632481 | full text |
| `depner2019` | 10.1016/j.cub.2019.01.069 | 30827911 | full text |
| `yang2022` | 10.1016/S2352-4642(22)00188-2 | 35914537 | abstract |
| `meredithjones2024` | 10.1186/s12966-024-01590-x | 38627708 | full text |
| `galland2018` | 10.1093/sleep/zsy017 | 29590464 | abstract |
| `pienaar2021` | 10.1177/0890117121992288 | 33567861 | abstract |

Four classes of quantity in this report are *arithmetic on published values* rather than published
numbers, and are labelled as such wherever used:

1. the sleep efficiencies implied by `campbell2024`'s per-condition TST (95.6% at 7 h TIB, 87.6% at
   10 h), computed as quoted-TST ÷ TIB;
2. the standard errors assigned to the two `se: null` adolescent memory nulls (`sqrt(4/n)` at
   *g* = 0, an independent-groups approximation — the corpus records none);
3. the optimal-on-habitual regression slope derived from `kitamura2016`'s reported r = 0.514 and SEMs;
4. confidence intervals shown as ± from a stored standard error where the source reported an SE but
   no interval — normal approximation, `estimate ± 1.96 × SE`. This covers `campbell2024`'s Sternberg
   slope (+1.8 ± 2.26 → −2.6 to +6.2) and the maturation-equivalent −3.85 (−5.34 to −2.36), whose
   construction is spelled out at §3.1.

No effect estimate in this report was invented, and no study is characterised other than as its own
retrieved text characterises it.

**Machine-checkable.** Two audit scripts accompany this report and both exit clean:

- `python3 src/redteam_check_citations.py` — parses the table above, confirms all 70 rows resolve to
  records in `evidence/` whose stored DOI, PMID and access tier match what is printed, that every
  matched record carries `verification.status: VERIFIED`, and that no study named in the body is
  absent from the table. *(This check caught three defects in my own draft: an access tier printed as
  full text where the corpus holds only the abstract, one printed as abstract where the corpus holds
  full text, and a body citation using the shorthand `irwin2016` for
  `irwin2016_inflammation_meta`.)*
- `python3 src/redteam_check_quotes.py` — confirms all 55 verbatim quotations and load-bearing
  numbers appear in the file each is attributed to. *(This one caught a paraphrase of the s06 shard
  that I had presented inside quotation marks; §1.1 now carries the shard's exact words.)*
