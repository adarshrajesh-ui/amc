# Exposure priors for the sleep-debt engine

Shard `s06_sleep_need_measurement`. 29 verified records, 96 quoted effect estimates, 0 failed identifiers.

Subject: male, weekday sleep reported as ~5-6 h from age 16 to 19, weekends/holidays ~7-8 h, occasional
3-4 h before exams, occasional 10-11 h weekend nights.

---

## READ THIS FIRST: the sign of the correction is the biggest open question in this shard

There are two defensible ways to turn a self-report into an estimate of true sleep, and **they disagree by
1.3-2.0 h for this subject — which is larger than any other uncertainty in the calculation.**

| Method | Formula | Report 5.5 h implies |
|---|---|---|
| Subtract the mean bias | `true = report − 1.0` | **4.50 h** |
| Reverse regression (recommended) | `true = 7.0 + β(report − 8.0)`, β = 0.50 | **5.75 h** |
| Reverse regression at the literature β | same, β = 0.19 (`white2026ffcws`) | **6.53 h** |

Both start from real, verified numbers. They differ because they answer different questions. The mean bias
of ~1.0 h is `E[report − truth]` **averaged over everyone**; it is not `E[truth | report = 5.5]`. Because
reported and true sleep are only weakly correlated (r = 0.18 in age-matched adolescents, `white2026ffcws`;
r = 0.45 in midlife adults, `lauderdale2008`), a low report is substantially *regression to the mean* and
`E[truth | report]` shrinks hard toward the population average.

`girschik2012` observed this directly, which is why I trust it as more than an algebraic artefact:

> "all participants who self-reported a usual sleep duration of 6 hours or less recorded an objective mean
> sleep duration of greater than 6 hours."

**Use the reverse regression. Do not subtract the mean bias.** Subtracting a population-average bias from
an individual's low report double-counts: it applies the average over-report *and* keeps the report's own
downward extremity. The sensitivity range over β = 0.19 to 1.0 must be propagated, and it dominates the
final interval. This is not a detail to be resolved by picking a midpoint quietly — the entire "how bad is
it" answer moves by a factor of ~1.9 depending on this choice.

---

## (i) Self-report minus objective sleep duration: bias in hours

### Evidence

| Study | Population | Age | Reference | Mean bias (h) | SD of difference (h) | r |
|---|---|---|---|---|---|---|
| `white2026ffcws` | US, FFCWS | 14-17 (mean 15.4) | actigraphy* | **+0.46** weekday, +1.24 weekend | **1.55** weekday | 0.18 |
| `short2012diary` | South Australia | 13-18 (mean 15.6) | actigraphy | +1.42 (diary) | — | — |
| `guedes2016` | Brazil | 12-17 | actigraphy | +1.0 all, **+1.9 boys** | 2.1 all, 2.8 boys | ICC 0.06 boys |
| `arora2013` | UK | 11-13 | actigraphy | +1.59 weekday | — | not significant |
| `lauderdale2008` | US, CARDIA | 37-51 | actigraphy | **+0.80** at 6 h measured | 1.19 (derived) | 0.45 |
| `cespedes2016hchs` | US, HCHS/SOL | 18-74 | actigraphy | +1.11 | — | 0.43 |
| `jackson2018mesa` | US, MESA | 54-93 | actigraphy | +0.97 to +1.10 | — | 0.28-0.45 |
| `jackson2018mesa` | US, MESA | 54-93 | **PSG** | +0.82 to +1.22 | — | — |

\* `white2026ffcws` measured actigraphic *sleep-period time* (first to last sleep epoch), not total sleep
time, so its +0.46 h understates the bias against true TST by roughly the SOL + WASO amount (~0.5-0.8 h).

### Recommended prior

```
bias_selfreport_minus_true_TST  ~  Normal(mean = 1.00, sd = 0.30)   hours    # uncertainty in the MEAN
between_person_SD_of_bias       =  1.40  hours   (plausible 1.2 to 1.6)
implied 95% limits of agreement =  −1.74 to +3.74 hours
```

Justification: the adolescent central values (0.46, 1.00, 1.42, 1.59) average **1.12 h**; the adult ones
(0.80, 1.11, and MESA's four-group means of 1.04 h vs actigraphy and 1.01 h vs PSG) average **0.99 h** — an
unusually consistent literature across two age ranges, four countries and two reference standards. The between-person SD comes from the only two studies reporting it directly: 1.19 h
(`lauderdale2008`, derived from the reported SDs and r) and 1.55 h (`white2026ffcws`, reported). Guedes's
2.1-2.8 h is an upper bound from n = 37.

Three reasons this bias is, if anything, **understated** for this particular subject:

1. **Actigraphy is not truth and it over-counts sleep.** `meredithjones2024` validated actigraphy against
   concurrent home PSG in 8-16 year olds: sensitivity 91.8% but specificity only **63.8%**, i.e. a third of
   true wake is scored as sleep. `jackson2018mesa` confirms the consequence — bias against PSG (73 min in
   whites) exceeds bias against actigraphy (66 min). So self-report-minus-**PSG** is larger than the table.
2. **Male sex worsens agreement.** `cespedes2016hchs` found correlations lower with male sex, younger age,
   sleep efficiency < 85% and night-to-night variability >= 1.5 h. The subject is male, 16-19, and swings
   between 3-4 h and 10-11 h — **all four moderators point the same way.** `guedes2016` independently found
   boys' bias (1.9 h, ICC 0.06) far worse than girls' (0.5 h, ICC 0.43).
3. **Self-report questions often capture time in bed, not sleep** — the AASM panel's own admission
   (`watson2015method`). See section (iii).

One counter-consideration I am not hiding: `short2012diary` argues the adolescent gap partly reflects
actigraphy *under*-counting sleep in adolescent boys ("possibly because of increased sleep motor activity
in adolescents that actigraphic algorithms score as wake"). That is the **opposite** direction to
`meredithjones2024`'s direct PSG validation. The conflict is unresolved; it is why the SD on the mean is
0.30 rather than tighter.

---

## (ii) Is the bias duration-dependent? Yes, strongly. Slopes below.

**Forward regression (report on truth)** — `lauderdale2008`, errors-in-variables:

```
d(report)/d(truth) = 0.51   (95% CI 0.35 to 0.67)
=> d(bias)/d(truth) = 0.51 − 1 = −0.49 h per hour  (95% CI −0.65 to −0.33)
```

> "for each additional hour of mean sleep recorded, report of habitual sleep increased, on average, by 31
> minutes" ... "persons sleeping 5 and 7 hours over-reported, on average, by 1.3 and 0.3 hours respectively"

So conditional on **truth**, short sleepers over-report far more (1.3 h at 5 h true vs 0.3 h at 7 h true).

**Reverse regression (truth on report)** — this is the one the model needs, because the report is all we
observe:

| Study | Population | β = d(true)/d(report) |
|---|---|---|
| `white2026ffcws` | adolescents, 14-17, adjusted | **0.19** (95% CI 0.13, 0.26) |
| `cespedes2016hchs` | adults, 18-74 | **0.333** (95% CI 0.317, 0.367) — "20 minutes (95% CI: 19, 22)" per reported hour |

### Recommended calibration

```
E[true weekday TST | report]  =  μ_true + β · (report − μ_report)

  μ_report = 8.0 h     # population mean adolescent self-reported weekday sleep (white2026ffcws: 8.02 h)
  μ_true   = 7.0 h     # population mean adolescent ACTIGRAPHIC weekday TST (derivation below)
  β        = 0.50      # recommended; propagate 0.19 to 1.00 as the sensitivity range
  SD(true | report) = 1.10 h    # residual; see derivation below
```

Residual SD derivation: `SD(true | report) = SD_true · sqrt(1 − r²)`. With `SD_true` = 1.19 h (the
between-person SD of adolescent weekday actigraphic sleep, `white2026ffcws`) this gives **1.17 h** at the
adolescent r = 0.18 and **1.06 h** at the midlife r = 0.45. I recommend **1.10 h**, near the middle. Note
how little the report reduces the uncertainty: conditioning on a self-report shrinks the SD from 1.19 h to
about 1.1 h. That is the honest measure of how uninformative a single sleep self-report is.

`μ_true = 7.0 h` derivation, reconciling three independent sources to a *weekday* *TST* basis:
`galland2018` pools 7.4 h at 15-18 y across day types with weekends +0.93 h, so weekday ≈ 7.4 − (2/7)(0.93)
= **7.13 h**; `evans2021actigraphy` gives 7.18 h at 10-19.99 y across day types, so weekday ≈ **6.9 h**;
`white2026ffcws` gives weekday sleep-period time 7.57 h, so TST ≈ **7.0-7.1 h**. Take 7.0 h.

Why β = 0.50 rather than the literature's 0.19-0.33: those coefficients come from **single-item
questionnaires** ("how many hours do you usually sleep?"). This subject supplied a *structured* account —
weekdays separately from weekends, plus exam nights, plus occasional long nights. `arora2013` shows
structure matters a great deal: sleep diaries correlated significantly with actigraphy while single-item
self-report did **not**, in the same 225 adolescents. A structured account should shrink less than a
single item, but it is not a diary either, so β sits between 0.33 and 1.0. **β = 0.50 is a judgement, not
a measured quantity** — hence the mandatory sensitivity range.

### Resulting exposure estimates

| Report | β = 0.19 | **β = 0.50** | β = 1.00 |
|---|---|---|---|
| 5.0 h | 6.43 h | **5.50 h** | 4.00 h |
| 5.5 h | 6.53 h | **5.75 h** | 4.50 h |
| 6.0 h | 6.62 h | **6.00 h** | 5.00 h |

Each with residual SD 1.10 h. Note that at β = 0.50 and a report of 6.0 h the correction is exactly zero —
the over-reporting and the regression-to-the-mean shrinkage cancel. That coincidence is worth knowing: for
reports near 6 h the naive "take the report at face value" happens to be about right, while both the
"subtract 1 h" and the "shrink to 6.6 h" corrections are wrong in opposite directions.

---

## (iii) Sleep efficiency (TST / time in bed)

### Evidence — four sources, two modalities, tight convergence

| Source | Method | Age | Sleep efficiency (TST/TIB) |
|---|---|---|---|
| `evans2021actigraphy` | actigraphy meta-analysis, 53 articles / 11,525 participants | **10-19.99** | **0.8720** (12 studies) |
| `evans2021actigraphy` | same | 20-29.99 | 0.8779 (9 studies) |
| `mitterling2015` | PSG, in-laboratory | <= 30 | 0.870 (median; printed range 0.719-0.941) |
| `meredithjones2024` | PSG, at home | 8-16 | 0.891 (mean, **SD 0.125**) |

`evans2021actigraphy` states the definition explicitly, which matters because the definition moves the
answer more than the population does: *"Sleep efficiency was operationalized as sleep duration divided by
time in bed and multiplied by 100."*

### Recommended prior

```
sleep_efficiency  ~  Normal(mean = 0.875, sd = 0.06)  truncated to [0.70, 0.98]

TST = 0.875 × TIB          # at TIB = 8.0 h  ->  TST = 7.00 h,  gap = 1.00 h
TIB − TST gap ≈ 1.00 h  (SD ≈ 0.5 h)
```

Two independent internal derivations of that gap agree to within 2 minutes: `meredithjones2024` gives
TST 518 min at 89.1% efficiency, so TIB = 581 min and the gap is **63.4 min**; `mitterling2015` gives
TST 413.5 min at 87.0%, so TIB = 475 min and the gap is **61.8 min**.

Decomposition of the ~1 h gap: sleep-onset latency **19.4 min** (`galland2018`, and "stable" across
3-18 y), WASO **~27 min** (`meredithjones2024`, implied by 95.0% sleep-period efficiency), leaving ~17 min
awake in bed before rising. `mitterling2015` puts young-adult WASO at 6.0% of TIB, consistent.

**No age adjustment is needed** across 16-19. Two meta-analyses independently find sleep efficiency flat
in this range: `ohayon2004` d = 0.01 (95% CI −0.13, 0.15) across childhood-to-adolescence, and
`evans2021actigraphy` r = −0.05 across the whole lifespan with the authors noting that removing any one of
31 effect sizes made it non-significant. `boulos2019`'s adult slope of −2.1 percentage points per decade
would move an 18-year-old by only ~0.4 points relative to a 20-year-old.

Why SD = 0.06 and not the 0.125 that `meredithjones2024` reports: that SD is from a **single** PSG night,
so it mixes between-person variance with night-to-night noise. The subject's exposure is a 3-year habitual
average, over which night-to-night noise averages out, so the relevant quantity is the between-person SD
of *habitual* efficiency, which is smaller. `inderkum2018twin` supports treating efficiency as trait-like
(heritability > 60%, and unlike duration it was "less dependent on the day of measurement"). 0.06 is
narrower than a single-night SD but wide enough to span the 0.870-0.891 disagreement between sources.

**Use this only if the subject's report is a time-in-bed figure.** If he meant time asleep, applying
efficiency a second time double-discounts by ~1 h. Which he meant is not recoverable from the case
description and should be carried as a discrete branch, not averaged away.

---

## (iv) Age-appropriate sleep need

### Ages 16-18

| Source | Type | Estimate |
|---|---|---|
| `short2018sleepneed` | **T1**, n = 34, ages **15-17** | **9.0 h** satiated at 10 h TIB; **9.35 h** for optimal sustained attention |
| `hirshkowitz2015nsf` | guideline, 14-17 y | recommended **8-10 h**; may be appropriate 7-11; not recommended **< 7 h** |
| `paruthi2016` | guideline, 13-18 y | **8-10 h** |
| `ohayon2004` | meta-analysis | TST declines with age on school days (d = −0.57) but **not** on nonschool days (d = −0.04) |

### Ages 18-19

| Source | Type | Estimate |
|---|---|---|
| `klerman2008` | **T1**, n = 35, ages 18-32 | asymptote **8.9 h** (95% CI 8.1-9.7); **9.2 h** in the subset matched on habitual duration |
| `kitamura2016` | **T1**, n = 15, ages 20-26 | optimal sleep duration **8.41 h** (range 7.29-9.26) |
| Van Dongen 2003 | T1, secondhand via `kitamura2016` | 8.16 h to prevent cumulative neurobehavioural deficit |
| `hirshkowitz2015nsf` | guideline, 18-25 y | recommended **7-9 h**; may be appropriate 6-11; not recommended < 6 h |
| `watson2015consensus` | guideline, adults | **">= 7 h"** floor; "**more than 9 hours** ... may be appropriate for **young adults**" |

### Recommended prior

```
sleep_need(age 16-18)  ~  Normal(mean = 9.00, sd = 0.70)   hours
sleep_need(age 18-19)  ~  Normal(mean = 8.70, sd = 0.70)   hours
      SD of individual need: 0.70 h,  plausible range 0.4 to 1.0 h
      thin tails; do NOT add a natural-short-sleeper mixture component above ~1% weight
```

**Do not implement the guideline's one-hour step at the 18th birthday.** `hirshkowitz2015nsf` drops the
recommended band from 8-10 h to 7-9 h the day the subject turns 18, and `paruthi2016`'s teenage band runs
to 18 while NSF's stops at 17 — so the two guidelines *disagree* about an exactly-18-year-old. The
laboratory evidence shows no such step: 9.0 h at ages 15-17 (`short2018sleepneed`) and 8.9 h at ages 18-32
(`klerman2008`). The step is an artefact of where committees drew age brackets. I recommend 9.0 → 8.7 h, a
gentle taper, and note that using the NSF 18-25 midpoint of 8.0 h would understate need by ~0.7-0.9 h
relative to the T1 evidence.

**Do not use the AASM ">= 7 h" as a central estimate.** It is a floor below which harm is asserted, not an
estimate of requirement, and the same statement carves out that > 9 h "may be appropriate for young
adults." Treating 7 h as the requirement understates it by 1.4-1.9 h relative to the three T1 laboratory
asymptotes (8.16 / 8.41 / 8.9 h).

### Where the SD of 0.70 h comes from — and this is thin evidence

**One study.** `kitamura2016`, n = 15 healthy Japanese men aged 20-26, is the only direct measurement of
the between-person SD of individual sleep need I could find:

> "The mean estimated OSD was 8.41 +/- 0.18 h (range, 7.29-9.26 h). The range of OSD was smaller than the
> range of HSD" ... "All results are expressed as means +/- SEM."

Arithmetic: SD = 0.18 × √15 = **0.697 h**. Sampling uncertainty on an SD from n = 15 is
0.697/√(2·14) = 0.132, giving a 95% interval of **0.44 to 0.96 h**. A cross-check from the reported range:
1.97 h span / d₂(15) = 1.97/3.47 = **0.57 h**, so 0.70 is if anything slightly conservative (wide).

Three independent lines bound it from above without pinning it:

- `inderkum2018twin`: free-day duration heritability 0.68, so the trait SD of *unconstrained* duration is
  √0.68 × 1.19 = **0.98 h** — an upper bound only, because free-day duration also contains heritable
  chronotype (sleep midpoint was 90% heritable on free days) and weekend catch-up, neither of which is need.
- `klerman2005`: the observed 6.1-10.3 h spread in habitual duration is *mostly self-imposed restriction*,
  so SD(need) must be well below SD(observed) ≈ 1.0-1.2 h.
- `kitamura2016` again: "The range of OSD was smaller than the range of HSD."

**Do not substitute the population SD of habitual sleep duration (~1.0-1.2 h) for the SD of need.** Doing
so roughly doubles the variance of the requirement and washes out the debt signal.

I deliberately did **not** derive the SD from heritability, though the arithmetic is tempting:
√0.46 × 1.1 = 0.75 h sits seductively close to Kitamura's 0.70. It is invalid — heritable variance in
observed duration includes chronotype, schedule sorting and reporting style, and `kocevska2021herit`'s
6-fold reporter effect (8% parent-report vs 38-52% self-report) proves a large slice of the estimated h² is
measurement artefact.

**On the natural-short-sleeper hypothesis** ("maybe he just needs 6 h"): documented FNSS phenotypes bound
genuine need at ~6.25-6.5 h (`he2009dec2`: carriers 6.25 h vs non-carriers 8.06 h; `shi2019adrb1`:
"lifelong requirement of < 6.5 hours per/night"). But `weedon2022` tested these exact variants in **191,929**
population-sequenced people and found **no association** with sleep duration — "often not highly penetrant
when ascertained incidentally from the general population." And the subject's own pattern contradicts it:
he reports 7-8 h at weekends and occasional 10-11 h nights, which is catch-up behaviour; true natural short
sleepers do not sleep in. Keep any short-sleeper mixture weight below 1%.

---

## (v) Recall rounding and heaping — yes, there is direct evidence

**Whole-hour heaping.** `wheaton2018yrbs`'s instrument permits nothing else:

> "'On an average school night, how many hours of sleep do you get?' Possible responses were 4 or less
> hours, 5 hours, 6 hours, 7 hours, 8 hours, 9 hours, and 10 or more hours."

**Anchoring on a stereotype.** `lauderdale2008`:

> "when pressed to give a response on a survey tend to answer what they believe to be how much adults in
> general sleep — our modal answers were 7 hours for weeknights and 8 hours for weekends. Since most
> actually sleep less than that, it is generally an overestimate, but it is less of an overestimate for
> people who sleep more and more of an overestimate for people who sleep less."

**Modal night, not mean night.** `girschik2012` tested this and found "the use of modal data improved
correlations," i.e. respondents describe a typical night rather than averaging. `watson2015method` concedes
the field has not studied it: "there is little information on how individuals account for such variation in
their reports."

### Recommended prior

```
rounding_error       ~  Uniform(−0.5, +0.5) h        # SD = 1/sqrt(12) = 0.289 h
modal_minus_mean_adj =  −0.20 h  (SD 0.15)           # subtract: his mean weekday sleep < his modal report
interval_report "5-6 h" ~ Uniform(5.0, 6.0)  ≈  Normal(5.5, 0.289)
```

The 0.289 h is an irreducible **floor** on measurement error even for a perfectly honest reporter, and it
should be added in quadrature to, not substituted for, the bias SD in section (i).

The `modal_minus_mean_adj` is a small correction that runs **against** the section (ii) shrinkage, so it is
worth stating explicitly. The subject reports a modal weekday value ("5-6 h") but also reports occasional
3-4 h nights before exams. Those nights pull his weekday *mean* below his *mode*. If ~10% of weekday nights
are at 3.5 h and the rest at 5.5 h, the mean is 0.9(5.5) + 0.1(3.5) = **5.30 h**, i.e. −0.20 h. So his
reported figure, read as a modal night, slightly **overstates** his true weekday average.

One reassurance about the report's plausibility: a 5-6 h school-night report is common, not extreme.
`wheaton2018yrbs` gives the full US high-school distribution, from which I derived the cumulative curve
(the derivation reproduces the paper's independently published 72.7% for < 8 h, confirming the arithmetic):
**20.1% report <= 5 h, 43.0% report < 7 h, 72.7% report < 8 h.** `kocevska2021norms` finds 51.5% of
teenagers below the recommended 8-10 h. So the subject sits between roughly the 20th and 43rd percentile of
reported school-night sleep — low, but not so extreme that the model should down-weight the report as
implausible.

---

## Putting it together: weekday deficit

Using `sleep_need` from (iv), the calibrated exposure from (ii), and a report of 5.5 h:

| | need | TST (β = 0.19) | TST (**β = 0.50**) | TST (β = 1.0) |
|---|---|---|---|---|
| age 16-18 | 9.00 h | deficit 2.47 h | **deficit 3.25 h** | deficit 4.50 h |
| age 18-19 | 8.70 h | deficit 2.17 h | **deficit 2.95 h** | deficit 4.20 h |

Central answer: **a weekday deficit of roughly 3 h per night**, with a defensible range of 2.2 to 4.5 h
driven almost entirely by the calibration choice in section (ii), not by uncertainty about sleep need.
Propagate `SD(true | report) = 1.10 h` and `SD(need) = 0.70 h` (add in quadrature: 1.30 h) on top of that
range.

Two failure modes that would corrupt this number, both flagged above and both easy to commit by accident:

1. **Comparing a PSG/actigraphy TST to a guideline band.** `hirshkowitz2015nsf` warns that its own evidence
   base conflates time in bed with sleep time: *"actual sleep time is typically less than time in bed, which
   biases data toward higher sleep duration estimates."* Subtracting an objective TST from a
   self-report-anchored band overstates the deficit by roughly the 1.0 h efficiency gap. Match units on both
   sides.
2. **Applying both a mean-bias subtraction and a sleep-efficiency multiplication.** Each is a route from a
   subjective report to true sleep. Using both discounts the same ~1 h twice.
