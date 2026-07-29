# protocol_basis.md — the measurement and power basis for a powered n-of-1 sleep self-experiment

Shard `s20_pvt_psychometrics`. Every number below traces to a YAML record in this directory, and every
record's DOI/PMID was verified against Crossref and PubMed. Numbers I computed myself are labelled
**[DERIVED]**; numbers I assumed because no source exists are labelled **[ASSUMPTION]**. Nothing here is
a recalled figure.

**Headline answer, stated up front.** For the briefed contrast (a 1–2 h/night difference in time in bed)
measured with a daily 3-minute PVT-B, the required sample size is **31 analysed nights per condition
(62 analysed nights)** under the most favourable assumption that nights are statistically independent.
Once realistic night-to-night autocorrelation is modelled, the same target needs **20–28 calendar weeks**.
**The 4-week protocol as briefed delivers 11–16% power for a 2 h contrast, not 80%.** It is 80%-powered
only for an effect roughly five times larger. Section 8 gives the smallest design that does reach 80%.

---

## 1. Choice of primary outcome: mean 1/RT (response speed), not lapses

Five independent datasets converge on the same answer, and it is not the metric most people use.

| Evidence | Speed metric | Lapse metric | Source record |
|---|---|---|---|
| Effect size, chronic partial restriction (d_z, 10-min PVT) | mean 1/RT **1.21** (rank 1 of 10) | lapses **0.91** (rank 5); lapse probability **0.88** (rank 8) | `basner2011_pvt_metrics` |
| Effect size at a *low* restriction dose (1 night 4 h TIB) | mean 1/RT d_z **0.59** → N = 25 | lapses d_z **0.37** → N = 61 | `basner2011_pvt_metrics` Table 4 |
| Between-day test–retest, rested (5-min PVT) | mean RT ICC **0.79**, SEM% **4.14%** | error metrics SEM% **32.6–168.7%** | `thompson2022_pvt5_reliability` |
| Test–retest, n = 372 | median RT ICC **0.69** | lapse count ICC **0.51** | `sunwoo2012_pvt_reliability` |
| Practice effect over 15 administrations | PVT speed β = **0.02** SD, P = 0.44 | PVT accuracy β = **0.09** SD, P = **0.02** | `basner2020_practice_effects` |
| Survives shortening the test | mean RT, fastest 10%, slowest 10% all retain significance at 2 and 5 min | lapse percentage **loses** significance | `loh2004_short_pvt_validity` |
| Retains a large effect on the 3-min PVT-B | mean 1/RT and slowest 10% 1/RT only | lapses drop to medium (0.65 → 0.76 with a 355 ms threshold) | `basner2011_pvtb` |

Mean RT is explicitly ruled out: it ranked 9 of 10 under chronic restriction (d_z 0.43), and Basner &
Dinges write that "PVT mean and median metrics, which are among the most widely used outcomes, should be
avoided as primary measures of alertness."

**Keep a lapse count as a secondary outcome anyway, for one reason: it is the only PVT quantity with an
externally anchored absolute scale.** `basner2011_pvtb_fitness_for_duty` found that **11 and 20 lapses**
on a 3-min PVT-B at the 355 ms threshold "optimally divided" simulated luggage-screening threat-detection
performance into high, medium and low bands, in a 34-hour total-deprivation protocol. Every other number
in this shard is a standardised or within-person-relative change, which is right for inference and useless
to a subject looking at today's score. Plotting the daily lapse count with horizontal reference lines at
11 and 20 gives the experiment an interpretable y-axis. Two caveats that must travel with those lines:
they were derived and tested in the same 36 subjects with no external validation, and they come from acute
total deprivation in a sample of mean age 30.8 — they are a reference annotation, not a diagnostic
threshold for chronic 1–2 h restriction in an 18-year-old.

**Primary outcome: mean 1/RT (inverse seconds) from a 3-minute PVT-B, inter-stimulus interval 1–4 s,
lapse threshold set to 355 ms for the secondary lapse outcome.** The 355 ms threshold is mandatory, not
cosmetic: with the standard 500 ms threshold the PVT-B shows genuine differential insensitivity to sleep
loss (version × time interaction P < 0.0001), which disappears at 355 ms (P = 0.3531 under partial
deprivation) — `basner2011_pvtb`.

One unresolved disagreement, reported rather than smoothed over: Basner's own data show effect sizes
saturating after the third minute under chronic restriction, Loh 2004 endorses 5 min and is
non-committal about 2 min, and Thompson 2022 asserts 5 min is more valid than 3 min. I specify 3 min
because compliance dominates everything else in a self-experiment, and I pay for it explicitly with the
published 22.7% effect-size penalty in section 4.

---

## 2. Within-person SD of the primary metric at rested baseline

This is the number without which no sample size can be computed, and it is the weakest link in the chain.
Two independent routes, in different units, agree.

**Route A — absolute, from Basner & Dinges 2011 Table 4.** The SD of the within-subject difference
between the day after baseline night 2 (10 h TIB) and the day after one night of 4 h TIB, for the daily
mean of three 10-min PVT bouts, is **σ_diff = 0.212 s⁻¹** (95% CI 0.162–0.254). A paired difference of
two daily means decomposes as

```
σ_diff² = 2·σ_w² + σ_vuln²
```

where σ_w is the within-person night-to-night SD and σ_vuln is between-person differential vulnerability
to the manipulation. Dropping σ_vuln gives a strict upper bound on σ_w: **[DERIVED]**

```
σ_w ≤ 0.212 / √2 = 0.1499 s⁻¹
```

Taking the differential-vulnerability share to be the PVT trait ICC of 0.675 from `vandongen2004_traitlike`
gives the other end: σ_w = 0.212·√((1 − 0.675)/2) = **0.0855 s⁻¹**. So σ_w lies in **0.086–0.150 s⁻¹**
for a daily mean of three 10-min bouts under laboratory conditions.

**Route B — relative, from Thompson et al. 2022.** Between-day standard error of measurement for the
5-min PVT in rested subjects: **SEM% = 4.14%** of the mean for mean RT (ICC 0.79), 4.43% for fastest 10%
RT (ICC 0.83). For y = 1/x the delta method gives dy/y = −dx/x, so the coefficient of variation of 1/RT
equals that of RT to first order: **CV(mean 1/RT) ≈ 4.14%**. **[DERIVED]**

**The two routes agree.** Expressing Route A's upper bound as a percentage requires a rested mean 1/RT,
which Basner reports only in a figure I did not digitise. Assuming ~3.75 s⁻¹ (mean RT ≈ 267 ms, bracketed
by Pejovic's baseline median RT of 231.5 ms and the usual right skew of the RT distribution)
**[ASSUMPTION]**:

```
0.1499 / 3.75 = 4.00%     vs Thompson's independently measured 4.14%
```

Two different laboratories, two different PVT durations, two different statistical routes, 4.00% versus
4.14%. That agreement is the single most reassuring result in this shard.

**Planning value.** Both routes are laboratory figures: fixed clock times, controlled caffeine, no
illness, no exam weeks. A free-living daily series in a college student will be noisier, and there is no
published field-condition σ for a home daily PVT that I could retrieve. I therefore apply a field
inflation factor of **×1.5 [ASSUMPTION]**:

```
σ_w(lab)   = 0.150 s⁻¹  = 4.0% of the person's own rested mean
σ_w(field) = 0.225 s⁻¹  = 6.0% of the person's own rested mean     ← PLANNING VALUE
```

Section 7 gives the sensitivity of the answer to this factor. It matters quadratically, so it is the
first thing a pilot week should measure.

---

## 3. Expected effect size for a 1–2 h/night sleep manipulation

Two independent routes again, and again they agree — which matters, because a 1–2 h contrast is a *small*
effect on the PVT and the literature is dominated by 4 h TIB studies.

**Route 1 — direct empirical analogue.** `pejovic2013_recovery_dissociation` ran exactly 6 h vs 8 h TIB
for 6 nights in 30 young adults (mean age 24.7). Raw changes from Table 3:

- median RT 231.5 → 251.4 ms = **+8.60%**, which is a fall in 1/RT of 8.60/108.60 = **7.92%** **[DERIVED]**
- fastest 10% RT 181.9 → 190.9 ms = **+4.95%** → 1/RT falls **4.72%** **[DERIVED]**

So a 2 h/night contrast sustained ~6 nights moves reaction speed by roughly **5–8% of baseline**. Note the
paired d_z values were only 0.33–0.42 and only fastest-10% RT reached P < 0.05 with n = 30. A 1–2 h
manipulation is genuinely a small group-level PVT effect, and the protocol must be built for that.

**Route 2 — dose linearisation, Basner × Van Dongen.** `basner2011_pvt_metrics` Table 4 gives the
mean-1/RT deficit after k nights of 4 h TIB relative to a 10 h TIB baseline: 0.125, 0.248, 0.314, 0.440,
0.545 s⁻¹ for k = 1…5. OLS on k: **slope = 0.1032 s⁻¹ per night** (intercept 0.0248). **[DERIVED]**

`vandongen2003_subjective_plateau` established that PVT lapses are "near-linearly related to the
cumulative duration of wakefulness in excess of 15.84 h (s.e. 0.73 h)", a model explaining 83.0% of the
PVT variance. Using ξ = 15.84 h to convert nights into hours of excess wakefulness: **[DERIVED]**

```
4 h TIB  → ~4.0 h sleep → 20.0 h wake → excess = 20.0 − 15.84 = 4.16 h/night
slope per (hour of excess wakefulness × night) = 0.1032 / 4.16 = 0.02481 s⁻¹
```

Applying that to the intended contrast, at 95% sleep efficiency: **[DERIVED]**

| TIB | TST | wake | excess over 15.84 h |
|---|---|---|---|
| 8.5 h | 8.07 h | 15.93 h | 0.09 h |
| 6.5 h | 6.17 h | 17.82 h | 1.98 h |
| 5.5 h | 5.22 h | 18.77 h | 2.93 h |

Differential excess wakefulness: **1.90 h/night** for a 2 h TIB contrast, 2.85 h/night for a 3 h contrast.

```
Δ(mean 1/RT) after m nights of a 2 h contrast = 0.02481 × 1.90 × m
  m = 1   → 0.047 s⁻¹
  m = 3   → 0.141 s⁻¹
  m = 4.5 → 0.212 s⁻¹     ← PLANNING VALUE
  m = 7   → 0.330 s⁻¹
```

**The two routes cross-validate.** Route 2 at 4.5 nights gives 0.212 s⁻¹ = 5.7% of the assumed 3.75 s⁻¹
mean; Route 1 gives 4.7–7.9% for 6 nights. Independent datasets, independent methods, same answer.

**Adopted Δ = 0.212 s⁻¹ ≈ 5.7% of the person's own rested mean 1/RT**, for a 2 h/night TIB contrast at a
mean accumulated exposure of 4.5 nights (which is what nights 4–7 of a 7-night period deliver).

*Caveat on extrapolation.* The linearisation is calibrated on 1–5 nights at 4.16 h/night excess, i.e.
cumulative excess wakefulness of 4–21 h. Van Dongen's curvature parameter for PVT lapses is θ = 0.78 ± 0.04,
slightly sub-linear, so extrapolating far beyond ~25 h cumulative excess overstates Δ. Where I extrapolate
(section 8) I discount by (W/W_cal)^0.78 rather than linearly and say so.

*The right-aged study exists and I could not get its numbers.* `short2018_adolescent_sleep_need` ran
exactly the manipulation this protocol needs — 7.5 h vs 10 h TIB (a 2.5 h/night contrast) for 5 nights,
with a 10-min PVT every 3 hours — in 34 adolescents aged 15–17, and confirmed a monotonic dose-dependent
increase in lapses. The per-condition means and effect sizes are in the paywalled full text (OUP blocks the
PDF, no PMC deposit, no Wayback snapshot). **Every record contributing to Δ or σ in this shard is therefore
in adults**, the closest being Pejovic at mean age 24.7, and the downstream model should inflate uncertainty
accordingly. Retrieving that full text is the highest-value single action anyone could take on this shard's
behalf.

*Direction of the age bias.* Adolescents are more, not less, affected per hour of lost sleep, and they need
more sleep to begin with (section 10). So an adult-derived Δ is more likely to understate than overstate
the effect in an 18-year-old, which makes the sample sizes below conservative in the useful direction.

---

## 4. The PVT-B penalty

`basner2011_pvtb`: "effect sizes for the PVT-B were lower compared to the PVT. They decreased on average
by 22.7%. The smallest decrease (6.9%) ... and the highest decrease (67.8%)". This is an attenuation of
d_z, i.e. of Δ/σ jointly, so it applies once, to the effect size:

```
attenuation factor = 1 − 0.227 = 0.773
```

For mean 1/RT specifically under chronic partial restriction the metric retained a "large" effect size
(≥ 0.8, down from 1.21), implying a factor ≥ 0.66 for this particular metric. I use the published mean of
0.773 and treat 0.66 as the pessimistic bound.

---

## 5. THE POWER CALCULATION — arithmetic shown

**Test.** Two-sided α = 0.05, power 0.80, comparing the mean daily PVT-B score between conditions within
one person. Constants:

```
z_{1−α/2} = 1.9600
z_{1−β}   = 0.8416
(z_{1−α/2} + z_{1−β})² = 7.8489
```

**Step 1 — standardised effect per analysed night.** **[DERIVED]**

```
d(10-min PVT) = Δ / σ_w      = 0.2121 / 0.2249 = 0.9433
d(3-min PVT-B) = 0.9433 × 0.773 = 0.7290
```

**Step 2 — required nights per condition, independent nights.**

```
n per condition = 2 (z_{1−α/2} + z_{1−β})² / d²
                = 2 × 7.8489 / 0.7290²
                = 15.6978 / 0.5314
                = 29.5
```

Iterating with the exact non-central t (rather than the normal approximation) to account for the
estimated variance:

```
n = 31 per condition   → achieved power 0.806 at α = 0.05
```

### ► **ANSWER: 31 analysed nights per condition — 62 analysed nights in total.**

This is a floor, not an estimate. It assumes every night contributes independent information, that σ_w
in the field equals 1.5× the laboratory value, and that the 2 h contrast has been in force for ~4.5
nights when each measurement is taken.

**Step 3 — correcting for night-to-night dependence.** Consecutive nights of a daily PVT series are not
independent: they share caffeine habits, workload, term-time stress, illness and the residue of the
previous night. Two standard models, both giving the effective number of independent nights per block of
m analysed nights.

*AR(1) with correlation ρ:*

| m analysed nights | ρ=0 | ρ=0.1 | ρ=0.2 | ρ=0.3 | ρ=0.4 | ρ=0.5 |
|---|---|---|---|---|---|---|
| 4 | 4.00 | 3.45 | 2.98 | **2.57** | 2.23 | 1.94 |
| 5 | 5.00 | 4.26 | 3.64 | 3.10 | 2.64 | 2.25 |
| 7 | 7.00 | 5.90 | 4.96 | 4.16 | 3.47 | 2.88 |
| 10 | 10.00 | 8.35 | 6.96 | 5.76 | 4.74 | 3.85 |
| 12 | 12.00 | 9.99 | 8.29 | 6.84 | 5.59 | 4.50 |

*Period-level state variance (compound symmetry), share φ of total within-person variance:*
Var(period mean) = σ_w²(φ + (1−φ)/m), so effective nights per period = 1/(φ + (1−φ)/m), which is **capped
at 1/φ no matter how many nights you measure** — 3.33 nights per period at φ = 0.3. This cap is the single
most important structural fact in the whole calculation: *daily measurement cannot buy unlimited power
within a fixed number of periods.*

Consequences for the 31-nights-per-condition target, using ρ = 0.3 **[ASSUMPTION]** and a 7-night period
with the first 2–4 nights discarded as washout:

| Period length | Analysed nights/period | Effective nights/period | Periods per condition | Calendar nights | Weeks |
|---|---|---|---|---|---|
| 7 | 4 | 2.57 | 13 | 182 | **26** |
| 7 | 5 | 3.10 | 10 | 140 | **20** |
| 14 | 10 | 5.76 | 6 | 168 | **24** |
| 14 | 12 | 6.84 | 5 | 140 | **20** |

Under the harsher compound-symmetry model with φ = 0.3 and only P − 2 degrees of freedom at the period
level, the requirement rises to 14 seven-night periods per condition (196 nights, 28 weeks) or 5
fourteen-night periods per condition (140 nights, 20 weeks).

### ► **So: 31 analysed nights per condition; 20–28 calendar weeks once dependence is modelled.**

**Step 4 — what the briefed 4-week protocol actually delivers.** Take the best available 28-night design
(4 periods of 7 nights, ABBA or BAAB, first 2 nights of each restriction period and first 4 nights of
each extension period discarded, 4 analysed nights per period):

| φ | Effective nights/condition | Power at Δ = 0.212 s⁻¹ | Minimum detectable effect |
|---|---|---|---|
| 0.0 | 7.50 | **16%** | 6.5 h/night of excess wakefulness |
| 0.1 | 5.88 | 13% | 7.3 h/night |
| 0.2 | 4.84 | 12% | 8.1 h/night |
| 0.3 | 4.11 | **11%** | 8.8 h/night |
| 0.5 | 3.16 | 10% | 10.0 h/night |

Even the day-level-degrees-of-freedom version of the same design (which is the optimistic bound) only
reaches 27–30%. And the 95% confidence interval it produces for the treatment effect is
**±0.24 to ±0.67 s⁻¹**, against a target effect of 0.212 s⁻¹ — the interval is one to three times wider
than the thing being measured.

### ► **The 4-week protocol is 80%-powered only for a contrast of roughly 5 h/night, i.e. for near-total sleep deprivation. For the briefed 1–2 h contrast it is an uninformative test.**

This is not a reason to abandon it, but it *is* a reason to declare in advance what it is: an estimation
and feasibility exercise that reports an effect with its confidence interval, plus a measurement of the
subject's own σ_w and ρ so that a properly powered version can be planned. A 4-week protocol that
reports "no significant effect" would be reporting its own lack of power, not a fact about the subject.

---

## 6. Design constraints imposed by sleep physiology and by CENT

The power arithmetic is not the binding constraint. Carryover is.

**Recovery is slow and asymmetric.** Four independent records agree:

- `pejovic2013_recovery_dissociation`: after 6 nights of 6 h TIB, **2 nights of 10 h TIB produced no
  detectable PVT improvement** (lapses restriction → recovery, P = 0.69, d_z = −0.07), and PVT lapses were
  still **worse than baseline** (P = 0.04, d_z = −0.39).
- `belenky2003_recovery`: PVT deficits from mild-to-moderate restriction did not resolve over 3 nights of
  8 h sleep.
- `banks2010_recovery_dose`: recovery after chronic restriction is exponential/saturating and incomplete
  after one night of 10 h TIB.
- `kitamura2016_adlib_sleep_debt`: **"only 1 h of PSD takes four days to recover to their optimal level."**

Deficits accumulate within a night or two; recovery takes four or more. Therefore:

1. **Nightly alternation (ABABAB) is invalid.** The extension nights would be contaminated by unrecovered
   debt and the estimated effect would be biased toward zero.
2. **Periods must be blocks of ≥ 7 nights**, with the opening nights of each *extension* period discarded
   (≥ 4 nights, from Kitamura) and the opening nights of each *restriction* period discarded (≥ 2 nights,
   less because onset is fast). The washout is deliberately asymmetric.
3. **Longer periods are doubly good.** They raise the accumulated exposure at measurement, so Δ grows
   linearly with period length, and Δ enters n quadratically. A 14-night period roughly doubles Δ relative
   to a 7-night period. This runs against the usual n-of-1 advice to maximise the number of crossovers and
   is the key non-obvious design conclusion of this shard.

**What CENT requires** (`cent2015_nof1_reporting`, `senn2019_nof1_sample_size`, `statinwise2021_nof1_series`):

- multiple crossovers, not one before/after comparison — a pre-post design is classified as
  non-experimental and outside CENT's scope, so **at least 4 periods (2 per condition)** are needed;
- randomised period order within pairs or blocks, with the full intended sequence pre-specified and
  recorded before the trial starts (items 8a–8c);
- a run-in period, and a washout between periods or explicit modelling of carryover (item 12c makes
  carryover, period effects and intra-subject correlation **mandatory** analysis targets);
- reporting of the outcome instrument's validity and reliability (item 6a.1) — which is exactly why the
  ICC and σ_w extractions above are part of the protocol, not background;
- blinding is impossible for a sleep-duration manipulation. CENT does not require it and gives no n-of-1
  guidance on it. Mitigations, not substitutes: the PVT is an objective reaction-time measure rather than a
  rated judgement; pre-register the analysis and the sequence; collect the subjective rating *before* each
  PVT so expectancy contamination can be estimated; and record the design as permanently "some concerns".

**Analysis model** (following StatinWISE, the best real worked example): a linear mixed model for daily
mean 1/RT with a fixed effect for condition, a fixed linear or log period term, a random effect for
period, an **AR(1) residual structure within period**, robust standard errors, and a retained
log_e(session) practice covariate. Report the effect with a confidence interval, and report the estimated
ρ and σ_w as results in their own right. StatinWISE is also the reality anchor: six 2-month periods with
7 daily measurements each reached only **55–70% individual-level power** for a moderate effect — and they
had the advantage of a blinded placebo.

---

## 7. Sensitivity of the sample size

Required analysed nights per condition (exact t, independent nights, 3-min PVT-B, α = 0.05, power 0.80):

| Δ (s⁻¹) ↓ / σ_w (s⁻¹) → | 0.150 | 0.187 | **0.225** | 0.262 | 0.300 |
|---|---|---|---|---|---|
| 0.100 (2 h × ~2 nights) | 61 | 93 | 134 | 182 | 238 |
| 0.150 (2 h × ~3 nights) | 28 | 42 | 61 | 82 | 107 |
| **0.212 (2 h × 4.5 nights)** | 15 | 22 | **31** | 42 | 54 |
| 0.250 | 11 | 16 | 23 | 30 | 39 |
| 0.330 (2 h × 7 nights) | 7 | 10 | 14 | 18 | 23 |

The answer swings between 7 and 238 nights per condition across plausible inputs. The two inputs that
matter most are σ_w (quadratically) and the accumulated exposure at measurement (also quadratically, via
Δ). Both are measurable in a two-week pilot, and **the pilot should be run before committing to a
duration.** Fixing the design first and discovering σ_w afterwards is how self-experiments end up
uninterpretable.

---

## 8. The smallest design that actually reaches 80% power

Searching over period length, washout, number of periods and instrument, with θ = 0.78 discounting
applied to extrapolated exposures:

| Design | Δ (s⁻¹) | d | Eff. nights/cond | Power (φ=0.15 / 0.30) |
|---|---|---|---|---|
| **As briefed:** 2 h contrast, 4×7 nights, 3-min PVT-B ×3 bouts | 0.236 | 0.81 | 4.1 | — / **11%** |
| 2 h contrast, 8×7 nights (8 weeks) | 0.236 | 0.81 | 8.2 | — / 28% |
| 2 h contrast, 4×14 nights (8 weeks), 10-min PVT ×5 bouts | 0.348 | 1.82 | 8.6 / 5.4 | 53% / 39% |
| **2 h contrast, 6×14 nights (12 weeks), 10-min PVT ×5 bouts** | 0.348 | 1.82 | 12.9 / 8.2 | **93% / 78%** |
| 3 h contrast, 4×14 nights (8 weeks), 10-min PVT ×5 bouts | 0.478 | 2.50 | 8.6 / 5.4 | 74% / 59% |
| **3 h contrast, 6×14 nights (12 weeks), 10-min PVT ×5 bouts** | 0.478 | 2.50 | 12.9 / 8.2 | **>99% / 96%** |

### ► Recommended powered protocol: **6 periods of 14 nights (12 weeks), randomised ABBABA-type sequence balanced 3 restriction / 3 extension, first 2 nights of each restriction period and first 5 nights of each extension period discarded, 5 PVT bouts per analysed day with evening weighting.**

Three cheap levers do most of the work, and all three have evidential support:

1. **Widen the contrast** from 2 h to 3 h (5.5 h vs 8.5 h TIB). Δ scales with the differential excess
   wakefulness, 1.90 → 2.85 h/night.
2. **Lengthen the periods** to 14 nights, roughly doubling the accumulated exposure at measurement.
3. **Test more often per day, and later in the day.** `cohen2010_residual_recovery` shows early-in-day
   performance can look recovered after chronic restriction while later-in-day performance is severely
   impaired, so evening bouts carry more signal. `sunwoo2012_pvt_reliability` also found statistically
   significant time-of-day effects in the PVT, so **the clock time of every bout must be fixed** or time
   of day will masquerade as a treatment effect.

If 12 weeks is not available, run the 4 weeks as a pilot whose declared purpose is to estimate σ_w and ρ
and to establish compliance — and report the effect as an interval, never as a significance test.

---

## 9. Nights of actigraphy needed for a stable habitual-duration estimate

`knutson2007_actigraphy_variability` (CARDIA, n = 669) is the only record giving the variance components
from which any night count can be derived. Sleep duration, adjusted for age, race, sex and weekend nights:
between-subject SD **0.70 h**, within-subject **daily** SD **1.26 h**, within-subject yearly SD 0.39 h.
"individuals differ more from day to day than they do from each other."

**Single-night ICC [DERIVED]:**

```
ICC(1) = 0.70² / (0.70² + 1.26²) = 0.4900 / 2.0776 = 0.236
```

About 76% of the variance in one night's actigraphic sleep duration is within-person noise.

**Route B, reliability (Spearman–Brown), k = R(1−r)/(r(1−R)) with r = 0.236: [DERIVED]**

```
R = 0.70 → k =  7.6 →  8 nights
R = 0.80 → k = 13.0 → 13 nights
R = 0.90 → k = 29.2 → 30 nights
```

**Route C, precision of *this person's* own mean, SEM(k) = 1.26/√k: [DERIVED]**

```
k =  3 → 43.6 min        SEM ≤ 30 min needs k ≥  7
k =  7 → 28.6 min        SEM ≤ 20 min needs k ≥ 15
k = 14 → 20.2 min        SEM ≤ 15 min needs k ≥ 26
k = 28 → 14.3 min        SEM ≤ 10 min needs k ≥ 58
```

Route C is the correct one for an n-of-1 — the reliability route answers "how many nights to rank people",
which depends on between-person variance, a quantity that does not exist when there is one subject.
Conveniently both routes converge: 13 nights (R = 0.80) and 15 nights (SEM ≤ 20 min) both round to two
weeks.

### ► **ANSWER: 14 nights minimum, 28 nights preferred.**

Corroboration and qualifications:

- `aili2017_actigraphy_nights`: **> 7 nights** needed for reliable total sleep time in working adults;
  weekend–weekday sleep differed by 38 min.
- `acebo1999_actigraphy_nights`: **5+ nights** for reliability generally, **7+ nights** for sleep duration
  specifically, in adolescents; up to 28% data loss, so oversample.
- `aasm2018_actigraphy_guideline`: the AASM minimum of **72 hours** is driven by the CPT billing code, not
  by reliability, and the guideline explicitly excludes healthy normal sleepers. It should not be cited as
  a psychometric standard. The guideline's own upper figure is 14 consecutive days.
- **The window must be a whole number of weeks** so the weekday/weekend mix is balanced, and weekday and
  weekend means must be reported **separately** rather than collapsed. This subject's weekday/weekend split
  is systematic and large; Knutson's 1.26 h is a weekend-*adjusted* residual, so it excludes exactly that
  component. With 14 nights there are only 10 weekday nights, giving SEM(weekday mean) = 1.26/√10 = 23.9
  min; 28 nights gives 20 weekday nights and 16.9 min. **[DERIVED]**
- Knutson's cohort was 38–50 years old. `kitamura2016_adlib_sleep_debt` found a mean *within-person range*
  of 6.36 h across ~14 nights in men aged 20–26, whereas a normal variable with SD 1.26 h would give an
  expected range of about 4.0 h over 14 draws **[DERIVED]** — young adults are more variable than
  Knutson's midlife cohort, so 1.26 h is a floor for an 18-year-old and 28 nights is the safer choice.
- Diary and actigraphy must run **concurrently**, as in `pejovic2013_recovery_dissociation`'s 2-week
  screening and `kitamura2016_adlib_sleep_debt`'s 2-week habitual measurement.

---

## 10. Ad-libitum sleep protocol to measure individual sleep need

Primary source `kitamura2016_adlib_sleep_debt` (15 healthy men, mean age 23.1, range 20–26 — the best
young-male match available), corroborated by `klerman2005_adlib_sleep_need` (ages 18–32).

**Procedure.**

1. **Habitual phase.** 14 nights (28 preferred) of concurrent actigraphy + sleep diary at home, on the
   subject's normal schedule, to fix habitual sleep duration (HSD). Kitamura: "They recorded their daily
   HSD at home using an actigraph and sleep diary for approximately 2 weeks."
2. **Adaptation.** 2 nights at 8 h TIB.
3. **Extension phase.** **9 consecutive nights at 12 h TIB.** No alarm, no naps outside the TIB window,
   no caffeine or alcohol, dark and quiet bedroom, fixed lights-out clock time. Kitamura's exact wording:
   "9 consecutive days of extended sleep sessions (sessions E1–E9) with TIB set at 12 h".
4. **Estimate.** Fit an exponential decay to nightly total sleep time across E1–E9. **The asymptote is the
   optimal sleep duration (OSD).** Potential sleep debt = OSD − HSD.
5. **Measure alongside** each night/day: total sleep time (PSG ideally, actigraphy as the feasible
   substitute), subjective sleepiness (VAS/KSS), and an objective alertness measure.

**What to expect, so the subject can be told in advance.**

| Quantity | Value | Source |
|---|---|---|
| First-night TST rebound above habitual | **+3.22 h** (TST 10.59 h vs HSD 7.37 h) | `kitamura2016` |
| Nights until TST stops declining | **4** ("no significant differences in TST between each of E4–E8 and E9") | `kitamura2016` |
| Group mean OSD | **8.41 ± 0.18 h**, individual range **7.29–9.26 h** | `kitamura2016` |
| Potential sleep debt in men reporting no sleep problems | **1.04 ± 0.24 h** (95% CI 0.57–1.58) | `kitamura2016` |
| Time to discharge 1 h/night of debt | **4 days** of extended opportunity | `kitamura2016` |
| Correlation, first-night rebound with 9-day debt | **r = 0.769**, P = 0.001 | `kitamura2016` |
| Correlation, sleep debt with subjective sleepiness (VAS) | **r = 0.052**, P = 0.854 | `kitamura2016` |
| Correlation, sleep debt with objective sleepiness (MWT) | **r = −0.486**, P = 0.066 (β = −0.544, P = 0.029 adjusted) | `kitamura2016` |
| Performance-derived sleep need, adults (independent method) | **8.16 h** (24 − 15.84 h critical wake duration, s.e. 0.73) | `vandongen2003` |
| Performance-derived sleep need, **ages 15–17** | **9.35 h** from PVT lapse dose-response modelling | `short2018` |
| Opportunity-derived sleep need, **ages 15–17** | **~9.0 h** obtained under 10 h TIB | `short2018` |

**Set the extension arm from the subject's own asymptote, and set it high.** Two independent methods agree
within each age band, and the adolescent figures sit about 0.9–1.2 h above the adult ones: 9.0 and 9.35 h at
ages 15–17 versus 8.41 and 8.16 h at ages 20–32. An 18–19-year-old sits between those bands, so the prior for
his sleep need is roughly **8.5–9.0 h, not 8.4 h**. This has a design consequence that is easy to miss and
expensive to get wrong: if the "extension" arm is set to 8.5 h TIB (≈8.07 h sleep) and his true need is 8.7 h,
then the control condition is *itself* mildly restricted, he never returns to a rested state, the washout never
completes, and carryover contaminates every period — biasing the whole experiment toward a null.
**Specify the extension arm as measured OSD + 0.5 h of TIB** (so ≈9.0–9.5 h TIB for a typical result), and
verify by actigraphy that the arm actually delivers sleep at or above OSD.

Reassuringly, the effect size in section 3 is robust to this: because Δ depends on the *differential* excess
wakefulness between arms, shifting the critical wake duration ξ from 15.84 h to 15.3 h (a 8.7 h sleep need)
changes the 2 h-contrast differential from 1.90 to 1.89 h/night — a 0.5% change. **[DERIVED]**

**Three nights is not enough.** `klerman2005_adlib_sleep_need` gave 18–32-year-olds a **16 h** daily sleep
opportunity (12 h nocturnal + 4 h midday) for only 3 days: sleep rebounded by 4.9 h on day 1 and was
**still 10.2 h on day 3, with no asymptote reached**. Their conclusion — "HBD appears to be an inaccurate
reflection of sleep need in young adults" — is the point of running the protocol at all. Also from that
record: 82% of healthy young adults on their habitual schedule showed an MSLT latency < 5 min at least once.

**Cheap substitute, endorsed by the authors.** A 9-night 12 h TIB protocol is not feasible outside term
breaks. Because the first-night rebound correlates at r = 0.769 (r² = 0.59) with the 9-day-derived debt, a
1–2 night ad-lib probe recovers most of the information. Kitamura explicitly frames weekend catch-up as the
naturalistic version of this, which makes **"weekend sleep minus weekday sleep approaching zero"** a
legitimate, measurable intervention target for this subject.

**Do not expect the subject to feel any of this.** "the participants had no awareness of any problems with
their sleep habits such as sleepiness or perceived sleep loss. However, even in this group of healthy
individuals who subjectively reported having enough sleep, we observed a TST rebound of more than 3 h in
average at E1. Thus, they were experiencing possible sleep loss without being aware of it."

---

## 11. Practice-effect washout requirement

Two separate things get called "washout" here and they must not be conflated.

**(a) Practice/learning washout — the instrument.** The Dinges group's frequently repeated claim is that
"PVT performance does not improve as a function of repeated administration". Measured directly across 15
administrations in the same 46 people (`basner2020_practice_effects`):

- **PVT response speed: standardised practice β = 0.02 (SE 0.03), P = 0.44** — genuinely null, and the PVT
  was the only test of 10 in the battery with no significant speed practice effect.
- **PVT accuracy (the lapse side): β = 0.09 (SE 0.04), P = 0.02** — small but real.
- For the other 9 tests, "Protracted, non-linear practice effects well beyond the second administration
  were observed", so one or two familiarisation sessions is demonstrably insufficient in general.
- Administration interval (4×/day vs every ≥10 days) did not modify the PVT practice slope, so **daily
  testing incurs no extra practice penalty**.

Two records qualify the null:

- `thompson2022_pvt5_reliability`: 5-min PVT **mean RT showed a significant systematic between-session
  shift (P = 0.01)**, which the authors attribute to a learning curve; fastest-10% RT did not.
- `vandongen2004_traitlike`: the PVT was the **one measure of 13 with a significant order effect
  (F = 4.36, P = 0.014)** across repeated exposures — in the direction of getting *worse*.

### ► **Requirement: ≥ 5 familiarisation sessions, all discarded, before any analysed data; plus a retained log_e(session) practice covariate in the analysis model.**

The session count is a design choice I am making from these records, not an extracted number. It is set by
the accuracy metric and by Thompson's session-1→2 shift, and it is cheap insurance: because the speed
practice slope is null, the covariate should estimate to ~zero, and if it does not, that is itself a
finding. For comparison, `pejovic2013_recovery_dissociation` used only "three practice trials within an
hour the night before the next day's testing", which these data suggest is too few.

**(b) Physiological washout — the exposure.** Governed by section 6: **≥ 4–5 nights** of extended
opportunity before an extension period's data are clean (Kitamura's 4 days per hour of debt), with 2–3
nights demonstrably insufficient (Pejovic, Belenky, Banks). Restriction onset is faster, so 2 discarded
nights suffice at the start of a restriction period. The washout is asymmetric by design.

**(c) Pre-trial debt clearance.** This subject has been carrying an estimated debt for ~3 years. The run-in
must clear it *before* the first period, otherwise the "extension" condition is measuring recovery rather
than a steady state. The ad-lib protocol of section 10 does double duty as this run-in — which is the
efficient ordering: habitual measurement → ad-lib debt clearance and sleep-need estimation → PVT
familiarisation → randomised periods.

---

## 12. Why an n-of-1 design at all, and how to read the subjective measures

**The n-of-1 justification is quantitative, not rhetorical.** The neurobehavioural response to sleep loss
is trait-like and reproducible within a person: ICC **0.675** for PVT lapses and **0.675–0.922** across 13
measures over two identical 36-h exposures (`vandongen2004_traitlike`); **0.89** for PVT lapses and 0.86
for PVT speed across two *different* sleep-loss paradigms (`rupp2012_traitlike`); **0.78–0.91** in the
largest sample, n = 83 (`yamazaki2020_traitlike`); **0.72–0.92** over follow-ups of up to 8.4 years
(`dennis2017_traitlike`). If roughly 70–90% of the variance in the response is stable between-person
variation, a population-average effect size can badly misestimate this specific individual — which is the
entire justification for measuring him rather than looking him up in a table. The PVT also loaded on its
own factor, separate from subjective sleepiness and from cognitive throughput, so the two are not
interchangeable readouts even at the level of individual differences.

**The subject will not be able to feel the effect, and the protocol must be built on that assumption.**

- Subjective sleepiness **saturates** while performance keeps degrading: over 14 days of restriction,
  curvature θ = **0.24 ± 0.04** for the Stanford Sleepiness Scale versus **0.78 ± 0.04** for PVT lapses in
  the same people on the same days. The plateau is not a scale ceiling — under total deprivation the same
  scale gave θ = 0.86 ± 0.14 (`vandongen2003_subjective_plateau`).
- Subjective sleepiness could not distinguish 6 h from 4 h TIB (rate of change, F(1,30) = 0.10, P = 0.75),
  while performance clearly could.
- Sleep debt is **uncorrelated** with subjective sleepiness (r = 0.052) but correlated with objective
  sleepiness (r = −0.486) in the same men (`kitamura2016_adlib_sleep_debt`).
- Restricted individuals **underestimate** their own impairment, most severely during the biological night
  (`zhou2012_subjective_underestimation`).
- A subjective questionnaire explains only ~4–7% of the variance in objective sleepiness (ESS vs MSLT
  r ≈ −0.20 to −0.27, n = 372; `sunwoo2012_pvt_reliability`).
- **Recovery is where this bites hardest.** After 6 nights of 6 h TIB followed by 2 nights of 10 h TIB
  (`pejovic2013_recovery_dissociation`, n = 30, all three measures in the same people on the same days):
  subjective sleepiness was **better than baseline** (P = 0.04), MSLT latency was **2.50 min longer than
  baseline** (P < 0.01), and PVT lapses were **still worse than baseline** (P = 0.04) with **no improvement
  at all** from restriction to recovery (P = 0.69). The subject will conclude he is fine after two good
  nights, and the PVT will disagree.

**One nuance that must not be flattened.** `kitamura2016` found the *opposite* ordering — objective
sleepiness (MWT) normalised after one extended night while subjective ratings took ~4 days. The resolution
is that three things are being called "objective" and they recover at different rates: **sleep propensity**
(MSLT/MWT) recovers fastest and can overshoot; **subjective sleepiness** recovers fast and saturates under
accumulating restriction; **attentional performance** (PVT) recovers slowest. The defensible claim is
specifically about the PVT, not about "objective measures" in general.

**Protocol consequences.** Collect the subjective rating (KSS or VAS) *before* every PVT bout at every
session, and analyse the subjective–objective discordance as a pre-specified secondary outcome. It is both
the expectancy control for an unblindable design and, on this evidence, the finding most likely to change
the subject's behaviour.

---

## 13. Where to get a validated PVT

| Implementation | Duration | Availability | Validation record |
|---|---|---|---|
| **PC-PVT** (Walter Reed / US Army) | configurable | freely distributed, Windows, standard PC hardware; validated for millisecond timing accuracy | `khitrov2014_pcpvt` |
| **PC-PVT 2.0** | configurable | updated platform adding analysis, prediction and visualisation | `reifman2018_pcpvt2` |
| **PVT-B** | 3 min | the basis of the ISS "Reaction Self Test"; the specification (ISI 1–4 s, 355 ms lapse threshold) is fully published and reimplementable | `basner2011_pvtb` |
| Smartphone/tablet 3-min PVT | 3 min | reports significant lapse-count correlations with a 10-min laptop PVT | `grant2017_pvt3_smartphone` |

**PC-PVT 2.0 on a dedicated laptop with a wired keyboard or gamepad is the recommended choice**, with the
PVT-B specification (3 min, ISI 1–4 s, 355 ms threshold) configured on top of it. Two hardware warnings:
touchscreen and browser input latency is not millisecond-accurate and varies by device, and Basner's own
PVT-B/PVT comparison was confounded by running the two tests on *different* hardware — the authors call
for studies "using the same hardware for both tests". Whatever device is chosen must be the only device
used for the entire study, and PVT-B and 10-min PVT scores are **not** interchangeable in absolute terms
(PVT-B responses are faster with more false starts and fewer 500 ms lapses); only within-subject change is
comparable.

---

## 14. Assembled protocol specification

| Element | Specification | Basis |
|---|---|---|
| Habitual-sleep measurement | 14 nights minimum, **28 preferred**; concurrent actigraphy + diary; whole weeks; weekday and weekend means reported separately | §9 |
| Sleep-need measurement | 2 adaptation nights at 8 h TIB, then **9 nights at 12 h TIB**; exponential decay fit; OSD = asymptote; debt = OSD − HSD | §10 |
| Extension (control) arm | **measured OSD + 0.5 h of TIB** (prior ≈9.0–9.5 h TIB for an 18–19 year old), verified by actigraphy | §10 |
| PVT familiarisation | **≥ 5 sessions, discarded**; log_e(session) covariate retained in the model | §11 |
| Instrument | PC-PVT 2.0 configured as PVT-B: 3 min, ISI 1–4 s, 355 ms lapse threshold; single fixed device | §13 |
| Primary outcome | **mean 1/RT**; secondary: slowest 10% 1/RT, lapses at 355 ms plotted against reference lines at 11 and 20, KSS collected before each bout | §1, §12 |
| Bouts per day | **3 minimum, 5 preferred**, at fixed clock times, evening-weighted | §8 |
| Contrast | 6.5 h vs 8.5 h TIB (2 h) as briefed; **5.5 h vs 8.5 h (3 h) strongly preferred** for power | §3, §8 |
| Period length | **14 nights**; discard first 2 nights of restriction periods and first 5 of extension periods | §6 |
| Number of periods | **6 (3 per condition)**, order randomised and recorded in advance, balanced against linear drift | §6, §8 |
| Duration | **12 weeks** for 78–96% power; 4 weeks is a pilot only (11–16% power) | §5, §8 |
| Required nights per condition | **31 analysed nights** (independent-night basis); 20–28 weeks of calendar time if only a 2 h contrast and a 3-min test are used | §5 |
| Analysis | linear mixed model, condition + period effects, AR(1) residuals within period, robust SEs; report effect with CI, and report estimated σ_w and ρ | §6 |
| Pre-registration | full randomised sequence, primary outcome, and analysis model committed before night 1 | §6 |

**The single most important sentence in this document:** the 4-week window is set by convenience, and it is
about a third of what the briefed 1–2 h contrast requires. Either the contrast widens, or the duration
extends, or the study is declared to be an estimation exercise. Reporting a null result from a design with
11–16% power as evidence of no effect would be the worst available outcome.
