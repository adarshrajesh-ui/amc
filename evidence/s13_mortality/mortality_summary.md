# All-cause mortality and habitual sleep duration — shard `s13_mortality`

**28 records, 122 effect estimates, 72 records screened and adjudicated, 0 identifiers failed verification.**

Subject: male, 19, weekday sleep ~5-6 h from age 16 to 19, weekend and holiday sleep ~7-8 h,
occasional 3-4 h pre-exam nights, occasional 10-11 h weekend nights, **exposure now endable**.

---

## 0. The one-paragraph answer

The published "short sleepers die 12% sooner" figure does not describe this subject, and the gap is
not a matter of taste — it is four separate, individually documented, multiplicative corrections.
(1) **Dose**: the 12-14% figure comes from categorical contrasts that pool cutpoints from <5 h to <7 h
and are dominated by people sleeping ≤5 h and below; at the subject's actual 5-6 h the dose-response
splines give RR **1.01-1.06**, and the largest head-to-head cohort gives **HR 1.02 (0.82-1.26)** for
self-reported 5-6 h weekday sleep. (2) **Sex**: the best dose-response meta-regression finds the
short-sleep arm is **null in males** (RR 1.02 at both 5 h and 6 h). (3) **Confounding and reverse
causation**: measured covariates remove **7-63%** of the crude association, early-death exclusion
removes a further ~12 percentage points, and genetic instrumentation removes **72-100%** of it. (4) **Age at exposure and exposure ending**: every usable estimate measures the hazard of *being*
a short sleeper in midlife or later, followed from that moment. **There is no evidence — none, of any
design — on a time-limited adolescent exposure that then ends.** Multiplying the documented
corrections, the residual permanent mortality effect attributable to this subject's three years is
**~1% of the published short-sleep hazard (span 0-12%), statistically indistinguishable from zero**,
and the well-defined component — the excess hazard *during* ages 16-19 — is worth **≈0.006-0.05
months** of life expectancy (un-discounted ceiling 0.2 months) because adolescent baseline mortality
is tiny. Everything materially above that will come from assuming permanent cumulative damage, which
is an assumption, not a finding.

---

## 1. The dose-response curve

### 1.1 Where the nadir is — the most robust fact in this domain

| Source | n | Nadir |
|---|---|---|
| `yin2017` dose-response MA, 40 cohorts | 3 582 016 | **7.0 h** |
| `liu2017` non-linear meta-regression, 40 cohorts | 2 200 425 | **~7.0 h** |
| `kripke2002` CPS-II | 1 100 000 | **7 h** ("best survival") |
| `svensson2021` Asia Cohort Consortium, 9 cohorts | 322 721 | **7.0 h**, both sexes |
| `chaput2026` UK Biobank | 76 811 | **7.2 h** self-report, **7.7 h** device |

**Consequence for the pipeline: the referent must be 7 h, not 8 h.** Several primary studies use an
8 h referent (`xiao2019`), which mechanically inflates every short-sleep estimate. Any conversion
that treats 8 h as optimal is double-counting.

### 1.2 The curve itself, at the doses that matter

| Sleep (h/night) | `yin2017` RR (95% CI) | `liu2017` RR | `liu2017` **males only** | `zhao2023` self-report weekday HR |
|---|---|---|---|---|
| ≤4 | 1.08 (1.06-1.09) | 1.05 (1.02-1.07) | — | 1.63 (1.04-2.54) |
| 5 | **1.04 (1.03-1.05)** | **1.06 (1.03-1.09)** | **1.02 (0.97-1.08)** | 0.68 (0.43-1.08) at 4-5 h |
| 6 | **1.01 (1.00-1.01)** | **1.04 (1.03-1.06)** | **1.02 (0.98-1.06)** | **1.02 (0.82-1.26)** at 5-6 h |
| 7 | 1.00 (nadir) | 1.00 (nadir) | 1.00 | 0.93 (0.79-1.09) at 6-7 h |
| 9 | 1.15 (1.14-1.16) | — | — | — |
| 10 | 1.32 (1.29-1.35) | 1.25 (1.22-1.28) | — | — |

**Per-hour slopes (`yin2017`):** below the nadir **RR 1.06 (1.04-1.07) per hour less**; above the
nadir **RR 1.13 (1.11-1.15) per hour more**. The curve is more than twice as steep going up as going
down.

**Threshold, from three independent sources:**
- `itani2017` meta-regression (5 172 710 people): mortality "linearly increased" only **below six hours**.
- `kripke2002` (1.1 million): excess exceeded 15% only **below ~4.5 h** (and above 8.5 h).
- `yin2017` spline: RR at 6 h is **1.01**, i.e. arithmetically indistinguishable from the nadir.

### 1.3 The categorical-versus-dose gap, which is where the headline number comes from

| Contrast | Estimate | log |
|---|---|---|
| `cappuccio2010` "short sleep" categorical (16 studies, 27 cohorts, 1 382 999 people, 112 566 deaths) | RR **1.12 (1.06-1.18)** | 0.1133 |
| `itani2017` "short sleep" categorical | RR **1.12 (1.08-1.16)** | 0.1133 |
| `ungvari2025` "short sleep" <7 h (newest synthesis, 2025) | HR **1.14 (1.10-1.18)** | 0.1310 |
| `yin2017` spline **at 6 h** | RR **1.01** | 0.0100 |
| `yin2017` spline **at 5 h** | RR **1.04** | 0.0392 |

The categorical estimate is **3-11x** the dose-specific estimate at the subject's actual dose.
The categorical "short" bin is dominated by people sleeping ≤5 h and below, and pools heterogeneous
cutpoints (`cappuccio2010` pools cutpoints from <5 h to <7 h). **Using 1.12 for a 5-6 h sleeper is a
category error, and it is the single most likely way for this pipeline to overstate the answer.**

### 1.4 The shape is J, not U — and that is the reverse-causation fingerprint

| Source | Short | Long | Long/short log ratio |
|---|---|---|---|
| `cappuccio2010` | 1.12 | **1.30** | 2.3x |
| `itani2017` / `jike2018` | 1.12 | **1.39** | 2.9x |
| `yin2017` | 1.13 | **1.35** | 2.4x |
| `ungvari2025` | 1.14 | **1.34** | 2.2x |
| `zhang2025` (UK Biobank observational) | 1.246 | **1.735** | 2.5x |
| `svensson2021` (≥10 h, men) | — | **1.34** | — |

In every large dataset, **long sleep looks 2-3x worse than short sleep on the log scale**. No
biological account of sleep loss predicts that. Illness that lengthens sleep and also kills predicts
it exactly. The decisive control comes from `pienaar2021`, which restricted pooling to **disease-free
employed adults aged 18-64**: there the two arms become **symmetric** — short ≤6 h RR 1.16
(1.11-1.22), long ≥8 h RR 1.18 (1.13-1.24). Removing sick people removes the asymmetry. That is what
reverse causation looks like when you take it out.

---

## 2. Objective versus self-report

**The task's stated premise was that objective measurement WEAKENS the short-sleep association. In
five independent analyses it STRENGTHENS it. I am reporting reality.**

### 2.1 Same people, same model, only the instrument changes — `zhao2023` (SHHS, n=5027, 1172 deaths, 11 y)

All-cause mortality, fully adjusted (incl. AHI and oxygen desaturation), referent 7-8 h:

| Sleep | **PSG-measured** | **Self-report, weekday** | **Self-report, weekend** |
|---|---|---|---|
| ≤4 h | **2.43** (1.83-3.22) | 1.63 (1.04-2.54) | 1.89 (1.23-2.89) |
| 4-5 h | **1.66** (1.30-2.12) | **0.68** (0.43-1.08) | 0.96 (0.62-1.50) |
| 5-6 h | **1.37** (1.10-1.71) | **1.02** (0.82-1.26) | 1.10 (0.88-1.38) |
| 6-7 h | **1.42** (1.15-1.76) | 0.93 (0.79-1.09) | 0.94 (0.80-1.12) |
| >8 h | 1.63 (0.79-3.34), n=54 | 1.26 (1.08-1.47) | 1.16 (1.01-1.35) |

Three things in this table settle the question, and none of them is the direction of the difference:

1. **The objective curve is not graded.** PSG 6-7 h (1.42) is *no better* than PSG 5-6 h (1.37). If
   lost sleep did graded damage, one hour of extra measured sleep could not buy nothing.
2. **The self-report curve at the subject's dose is flat, and non-monotone.** 5-6 h → 1.02;
   6-7 h → 0.93; 4-5 h → **0.68**. Nothing believes 4-5 h protects against death. Measurement error
   and selection produce that pattern; a dose-response cannot.
3. **The two instruments were only weakly correlated with each other** (authors' own statement). So
   they are not two noisy readings of one exposure — they are **two different exposures sharing a
   label**. PSG-derived short sleep in a 64-year-old is substantially fragmented, apnoeic, medicated,
   pathological sleep. Self-reported weekday short sleep is closer to "goes to bed late".
   **The subject's exposure is the second one, and the second one is null at 5-6 h.**

### 2.2 The other objective analyses agree on direction

| Study | Cohort | Objective estimate | Self-report comparator |
|---|---|---|---|
| `chaput2026` | UK Biobank, 76 811 | device **SPT 5 h vs 7 h: HR 1.43** (1.27-1.64); device TST: 1.21 (1.12-1.28) | same people, **1.16** (1.00-1.35) |
| `saintmaurice2024` | UK Biobank, 88 282 | actigraphy **5 h vs 7 h: HR 1.29** (1.09-1.52) | — |
| `liang2023` | UK Biobank, 90 398 | device short: **HR 1.27** (1.11-1.45) | — |
| `yoshiike2023` | SHHS, 3128, aged 40-64 | PSG TST <330 min: **HR 2.01** (1.45-2.87) | — |
| `fernandezmendoza2019` | Penn State, 1654, 19.2 y | PSG <6 h **×** cardiometabolic disease: **HR 2.14** (1.51-3.01) | — |

### 2.3 Why "objective is stronger" does **not** rescue the causal reading

- `saintmaurice2024` found **sleep fragmentation (WASO, awakenings) had NO association** with
  mortality, while sleep **timing** did (HR ~1.20 for extreme L5 midpoints). If the mechanism were
  sleep loss, fragmentation should matter. If the mechanism is disordered life and disordered
  physiology, timing matters and fragmentation is redundant with duration.
- `liang2023` found long duration **combined with low efficiency** gave HR 2.11 (1.44-3.09) — the
  pathological-sleep phenotype, not the short-sleep phenotype, carries the biggest hazard.
- `windred2024` (60 977, same cohort): **sleep regularity out-predicted sleep duration**, and adding
  duration to a regularity model improved nothing (p = 0.14-0.20).
- `fernandezmendoza2019`: objective short sleep amplified mortality **specifically in people who
  already had stage-2 hypertension or type 2 diabetes**. In a 19-year-old, that interaction term is
  empty.
- `kurina2013`'s critical review notes survey-reported and physiologically measured sleep duration
  agree poorly, which is now confirmed quantitatively by `zhao2023`.

**Verdict:** objective devices measure short sleep *better* — and in a 60-year-old, short sleep
measured better is a *better marker of illness*. Strengthening on objective measurement is evidence
that the signal is pathology, not that it is behavioural sleep debt.

---

## 3. Mendelian randomization

Three MR analyses exist. They do not agree, and the two more direct ones are null.

| Study | Instrument / exposure | Outcome | Result | vs observational |
|---|---|---|---|---|
| `zhang2025` | genetically predicted short **and** long sleep duration, IVW | **all-cause mortality** | **NULL** | observational HRs in same paper: short **1.246** (1.195-1.298), long **1.735** (1.643-1.831) → **0% survives** |
| `sambou2024` | genetically predicted healthy (7-8 h) sleep duration, 590 instruments, one-sample | terminated healthspan (composite of 8 events incl. death) | **OR 0.98 (0.97-1.00)**, p=0.036 | observational HR 0.93 (0.92-0.96) → **28% survives** |
| `wu2024` | genetically predicted **binary** short sleep (<7 h), 140 instruments, MVMR | parental lifespan | **β = -0.60 (SE 0.176)**, p<0.001; mediated via CAD, T2D, depression | — |

Three problems that stop MR from settling this:

1. **`wu2024` contradicts itself.** The *binary* short-sleep instrument gave β = -0.60, but the
   *continuous* sleep-duration instrument in the same paper gave **β = +0.24 (SE 0.388), null**. If
   sleeping less causally shortens life, a continuous instrument for hours of sleep should show it.
   It did not.
2. **Units.** `wu2024`'s β is on the Timmers parental-survival Cox residual scale. It **cannot** be
   converted to months of life expectancy without assumptions the paper does not supply, and I did
   not invent them. Any downstream code that treats -0.60 as years or months is fabricating.
3. **The estimand is wrong for us even when MR is valid.** MR estimates the effect of *lifelong
   genetic liability to sleep slightly less*, typically minutes-per-allele. Our question is the effect
   of *behaviourally sleeping 5-6 h for three years in adolescence and then stopping*. MR neither
   licenses nor excludes that.

Corroborating (screened, excluded as a preprint with a biomarker outcome, PMID 42465890): a 2026
five-dataset analysis found the poor-sleep/accelerated-ageing correlation **robust to chronic disease
burden but NOT robust to shared genetic and early-environmental factors among twins**, with "mixed"
MR evidence — the same conclusion from a different direction.

**Verdict: MR provides no support for a large causal mortality effect of habitual sleep duration.
Two of three analyses are consistent with no effect on death at all.**

---

## 4. Weekend catch-up — every cell, and the contradiction

### 4.1 `akerstedt2019` (required extraction 4) — Swedish National March Cohort, n=38 015, 13 y

Categories: short ≤5 h, medium 6-7 h, long ≥8 h. **Referent = MM (6-7 h on both weekdays and
weekends)** — note this is *not* "consistently 7 h" as the task assumed; the paper's referent is a
6-7 h band, and its companion `akerstedt2017` concludes 6 h is the nadir in this cohort.

| Cell | Weekday | Weekend | **Age <65** HR (95% CI) | Whole cohort | Age ≥65 |
|---|---|---|---|---|---|
| **SS** | ≤5 h | ≤5 h | **1.65 (1.22-2.23)** | 1.10 (0.95-1.28) | 0.97 (0.81-1.18) |
| **SML** | ≤5 h | **≥6 h (catch-up)** | **1.09 (0.77-1.54)** | 1.04 (0.79-1.37) | — |
| **MM** | 6-7 h | 6-7 h | **1.00 (referent)** | 1.00 | 1.00 |
| **ML** | 6-7 h | ≥8 h | 1.02 (0.86-1.21) | — | — |
| **LL** | ≥8 h | ≥8 h | 1.25 (1.05-1.50) | 1.06 (0.95-1.17) | — |

Weekend sleep alone, age <65, referent 7 h weekend: **≤5 h → 1.52 (1.15-2.02)**; additionally
adjusted for weekday sleep **→ 1.40 (0.97-2.02)**; **6 h → 0.82 (0.62-1.07)**.

Survival-time (quantile) analysis, **months of age at death at the 25th percentile**, fully adjusted,
whole cohort: **SS −9.2 months (−18.2 to −0.2); SML −6.1 months (−19.4 to +7.2)**.

**The rescue arithmetic:** ln(1.09)/ln(1.65) = 0.0862/0.5008 = **17%**, i.e. weekend catch-up is
associated with removal of **~83% of the excess log-hazard** of consistent short sleep in the under-65s.

**Four reasons not to bank that 83%:**
1. It is a between-person comparison of two small cells (52 vs 37 deaths); the 1.65-vs-1.09
   difference is **never formally tested**.
2. The SS cell's mean age is **61.2 y**, the SML cell's is **46.1 y** — the "rescued" group is 15
   years younger, and age is the dominant mortality predictor.
3. **The paper's own survival-time analysis does not reproduce the rescue** (−6.1 months for SML vs
   −9.2 for SS, overlapping intervals; on the age-adjusted model the ordering actually reverses,
   −8.4 for SML vs −7.8 for SS). The two analyses in one paper disagree.
4. The whole-cohort SS estimate is 1.10 and the ≥65 estimate is 0.97, so the 1.65 that generates the
   83% only exists in one age stratum.

### 4.2 The other three catch-up studies — and they do not agree

| Study | Design | Exposure | Result |
|---|---|---|---|
| `akerstedt2019` | self-report, Swedish, <65 y | short weekday + long weekend | **1.09 vs 1.65** → protective |
| `li2026` | **objective**, UK Biobank, 85 618 | severe restriction **without** vs **with** rebound | **1.42 (1.24-1.63) → 1.13 (0.95-1.36)**; ln(1.13)/ln(1.42) = **35% survives**, i.e. rebound removes ~65% → protective |
| `chaput2024` | **objective**, UK Biobank, 73 513 | ≥2 h weekend catch-up vs none | **HR 1.17 (0.97-1.41)** — *harmful direction*; dose-response null; **null in the <6 h-weekday subgroup** → **not protective** |
| `yoshiike2023` | **PSG + self-report**, SHHS, aged **40-64** | catch-up × objective sleep ability | see below → **not protective at the subject's dose** |

`yoshiike2023` full table, all-cause mortality, Model 2 (adjusted for weekday sleep duration, social
jetlag, napping, Epworth, hypnotics, insomnia, REM%), referent = no catch-up + normal PSG TST:

| PSG TST | Catch-up | Primary cutoffs (n=3128) | Stricter cutoffs (n=2028) |
|---|---|---|---|
| short (<360 / <330 min) | none | 1.17 (0.82-1.66) | 1.51 (0.96-2.37) |
| short | **1 h** | **1.44 (0.94-2.20)** | **1.84 (1.08-3.14)** |
| short | ≥2 h | 1.29 (0.73-2.27) | 1.47 (0.73-2.98) |
| normal (≥360 / ≥390 min) | none | 1.00 (ref) | 1.00 (ref) |
| normal | **1 h** | **0.48 (0.27-0.83)** | **0.36 (0.17-0.78)** |
| normal | **≥2 h** | **1.15 (0.65-2.05)** | 0.87 (0.39-1.96) |

Interaction between continuous TST and catch-up: **P = 0.67 and P = 0.63 — not significant.**

Three findings that bear directly on the subject:
- **The benefit is not monotone in catch-up, and his swing is the wrong size.** 1 h of catch-up with
  adequate sleep: 0.48. **≥2 h of catch-up with adequate sleep: 1.15 — nothing.** The subject goes
  from 5-6 h to 7-8 h, a ~2 h swing. **That is the null cell.**
- **Catch-up did not rescue objectively short sleepers** — it was numerically *worse* than no catch-up
  in the same stratum (1.44 vs 1.17; 1.84 vs 1.51).
- **The protective cells are not credible as causal effects.** 0.48 and 0.36 mean 52% and 64%
  mortality reductions from one hour of weekend lie-in, off 17 and 9 deaths. That is the size of the
  healthy-participant selection available in this design — which is the same selection inflating
  `li2026`.

Supporting: `zhao2023` finds self-reported **weekend** sleep >8 h carries HR **1.16 (1.01-1.35)** in
its elderly cohort — the weekend extension itself looking mildly harmful, almost certainly a
reverse-causation artefact, but not an endorsement of catch-up.

### 4.3 Weekend-catch-up verdict

**Two studies say catch-up helps, two say it does not. The two that say it does not are both
objectively measured, one shares its cohort with `li2026` and reaches the opposite conclusion, and
the only study that formally tested the interaction found none.** The most favourable reconciliation
is that `li2026` conditions on *being restricted* and asks whether rebound follows (the subject's
counterfactual), whereas `chaput2024` contrasts catchers-up against non-catchers-up across the whole
distribution and so partly measures irregularity — which `windred2024` shows predicts mortality
better than duration does. That is a *reading*, not a result.

**Instruction to the pooler: `akerstedt2019`, `li2026`, `chaput2024` and `yoshiike2023` must not be
averaged. `li2026`/`chaput2024` share `cohort_family: UK_Biobank`; `yoshiike2023`/`zhao2023` share
`SHHS`; `akerstedt2019`/`akerstedt2017` share the Swedish March Cohort. Grade the protective
weekend-catch-up effect D on model dependence (sign-unstable) — a GUESS under `gates.md`.**

---

## 5. Confounding attenuation — how much of the crude association survives?

Every attenuation I could compute directly, with the arithmetic:

| Analysis | Contrast | Crude | → adjusted | → + extra control | Surviving fraction of crude **log** |
|---|---|---|---|---|---|
| `zhao2023` | PSG 5-6 h vs 7-8 h | 1.92 | 1.48 (age/sex) → **1.37** (full) | — | **48%** (0.3148/0.6523) |
| `zhao2023` | PSG ≤4 h vs 7-8 h | 4.29 | 2.82 → **2.43** | — | **61%** (0.8879/1.4563) |
| `yoshiike2023` | PSG <360 min, no catch-up | 1.52 | 1.43 → 1.21 → **1.17** | — | **37%** (0.1570/0.4187) |
| `akerstedt2017` | ≤5 h vs 7 h, **age <65** | 1.45 | **1.37** | **1.31** (excluding deaths in first 2 y) | 85% adjusted; **73%** after early-death exclusion |
| `akerstedt2017` | ≤5 h vs 7 h, whole cohort | 1.13 | **1.12** | — | 93% |
| `sambou2024` | healthy sleep duration, same cohort | HR 0.93 obs | — | **OR 0.98 (MR)** | **28%** (0.0202/0.0726) |
| `zhang2025` | short sleep, same cohort | HR 1.246 obs | — | **MR NULL** | **0%** |

**Summary of the attenuation ladder:**
- **Measured covariates alone remove 7-63%** of the crude log association. The removal is *larger for
  smaller sleep deficits* (`zhao2023`: 52% removed at 5-6 h vs 39% at ≤4 h) — exactly what you expect
  if the moderate categories are mostly confounding.
- **Excluding early deaths removes a further ~12 percentage points** (`akerstedt2017`: 85% → 73%).
  `yoshiike2023`'s 2-year-exclusion sensitivity analysis "did not show any different results".
- **Adjusting for prevalent disease matters enormously in the populations where it can be measured**:
  `fernandezmendoza2019` shows the PSG short-sleep hazard is concentrated in those with existing
  cardiometabolic disease (HR 2.14), and `pienaar2021` shows that restricting to disease-free
  employed adults makes the short and long arms symmetric (1.16 vs 1.18).
- **Genetic instrumentation removes 72-100%.**
- **`ferrie2007` supplies the cleanest single reverse-causation demonstration**: in Whitehall II, a
  *decrease* in sleep duration predicted CVD mortality **HR 2.4 (1.4-4.1)** *and* an *increase*
  predicted non-CVD mortality **HR 2.1 (1.4-3.1)** — both directions of change roughly doubled
  mortality, and adjustment for socio-demographics, existing morbidity and health behaviours "left
  these associations largely unchanged". A causal-sleep-loss model explains the first result and
  cannot explain the second. Incipient disease perturbing sleep explains both.

**Best single attenuation number for the downstream model: ~35-50% of the crude short-sleep
association survives full covariate adjustment plus early-death exclusion, and 0-28% survives genetic
instrumentation. I recommend a residual-causal fraction of 0.25 (range 0.0-0.50) applied to
covariate-adjusted observational estimates.**

---

## 6. Age at exposure (required extraction 6) — the answer is the opposite of reassuring

| Source | Finding |
|---|---|
| `akerstedt2017` (Swedish March, 43 863) | ≤5 h vs 7 h: **age <45 → HR 2.45 (1.19-5.04)**; age <65 → 1.37 (1.09-1.71); **age ≥65 → 1.05 (0.90-1.22)**, i.e. null |
| `akerstedt2019` (same cohort) | SS vs MM: **age <65 → 1.65**; whole cohort → 1.10; **age ≥65 → 0.97** |
| `li2026` | **moderate** restriction without rebound: **age ≤65 subgroup HR 1.43 (1.13-1.79)**, versus 1.15 (1.01-1.31) for moderate restriction without rebound in the whole cohort — the under-65s carry the signal |
| `svensson2021` (322 721) | **age is a significant modifier in MEN (all-cause χ²₅ = 41.49, P < .001) and not in women** |

**The short-sleep mortality association is LARGER in younger strata and vanishes in the elderly. It
does not attenuate in younger cohorts.** Do not use "he is young, so it matters less" as an argument;
the evidence points the other way.

**But note carefully what "younger" means here: 45-64, not 16-19.** And the reason the association is
larger in younger adults is at least partly competing risks — in the over-65s, everything kills you,
so the short-sleep coefficient is diluted. Extrapolating the *slope* of that age gradient down to 19
is unwarranted, and I do not do it. `akerstedt2017`'s <45 estimate rests on very few deaths
(CI 1.19-5.04, a 4.2-fold span).

---

## 7. Adolescent exposure: **INSUFFICIENT EVIDENCE**

**There is no study, of any design, that measures sleep duration in adolescence, follows participants
to death, and reports a short-sleep-specific mortality estimate.** I screened 80 records across two
dedicated queries plus a title-restricted Europe PMC query. The query space is empty — query 14
returned bariatric surgery, SUDEP and neonatal pulmonology records.

**The single existing near-miss is `duggan2014`** (Terman Life Cycle Study, n=1145, childhood sleep
reported by parents/teachers ~1922, followed to death):
- It models a **quadratic** deviation from age-predicted sleep: **HR 1.15 (1.05-1.27) in males** for
  deviation in **either** direction. It therefore **cannot** yield a short-sleep-specific estimate —
  a short sleeper and a long sleeper get the same coefficient.
- Females: 1.02 (0.91-1.14), null.
- Cohort born 1904-1915, gifted Californian children, left-truncated (enrolled at ~11 y and had to
  survive to enrolment), exposure by proxy report, era-specific mortality causes.
- It cannot distinguish "trait" from "state": a child who slept short was probably a person who slept
  short for decades, which is the *opposite* of our subject's time-limited exposure.

**On the actual counterfactual — a 3-year adolescent restriction followed by normalisation — the
evidence base is empty.** The closest proxies, and what each does and does not license:

| Proxy | What it shows | Why it is not the answer |
|---|---|---|
| `wang2020` (Kailuan, 52 599) | all-cause mortality: low-**stable** (4.2-4.9 h) HR **1.50** (1.07-2.10); normal-**decreasing** **1.34** (1.15-1.57). **The abstract does NOT report an all-cause mortality HR for the low-increasing group** (4.9 → 6.9 h, the short sleeper who normalised) — only its **cardiovascular-event** HR, **1.22 (1.04-1.43)**, against **1.47 (1.05-2.05)** for low-stable | The only apples-to-apples comparison available is for cardiovascular **events**, not death: ln(1.22)/ln(1.47) = **52% of the excess log-hazard remained after normalising**. I must not silently substitute that for a mortality estimate, and the absence of a reported mortality HR for the normalising group is itself a limitation, not a null. Normalisation also happened in **midlife after decades**, not at 19 after 3 years |
| `li2026` | rebound removes ~65% of the excess hazard of severe restriction | Same-week rebound, not a 3-year exposure ending; contradicted by `chaput2024` in the same cohort |
| `ferrie2007` | hazard tracks the **current trajectory**, symmetrically in both directions | Midlife drift, cause-specific outcomes |
| `windred2024` | regularity (a **concurrent** state marker) out-predicts duration; duration adds nothing | If the signal is concurrent, stopping stops the risk — favourable, but this is an inference |

---

## 8. What fraction of this risk plausibly applies to a 3-year adolescent exposure that then ends?

### 8.1 What the hazard ratios actually mean

**Every estimate in sections 1-6 answers this question: "among people who, at one moment in midlife or
later, reported or were measured to sleep X hours, what was the death rate over the following
5-20 years?"** It is a **current-state** hazard for a person whose exposure is ongoing and whose
short sleep is entangled with their health, work, mood, poverty and medication at the moment of
measurement. It is **not** an estimate of the residue of a past exposure. Reading `cappuccio2010`'s
1.12 as "1.12x for life because he slept badly at 17" is not a cautious use of the number; it is a
different quantity with no evidential support.

### 8.2 The documented multiplicative chain

Starting from the published categorical short-sleep hazard (HR 1.12-1.14, log ≈ 0.113-0.131):

| Correction | Source | Retained fraction of log-effect |
|---|---|---|
| **(a) Dose** — 5-6 h, not the ≤5 h-and-below categorical bin | `yin2017` 6 h RR 1.01 / 5 h 1.04; `liu2017` 1.04-1.06; `zhao2023` self-report 5-6 h HR 1.02 | **0.09-0.50** |
| **(b) Sex** — male | `liu2017` males-only 1.02 at both 5 h and 6 h (contradicted by `ungvari2025`, so treated as a wide range) | **0.2-1.0** |
| **(c) Confounding + reverse causation** | §5 ladder: 37-93% survives covariate adjustment, 73% survives adjustment + early-death exclusion, 0-28% survives MR | **0.0-0.50**, central **0.25** |
| **(d) Exposure ended, and was 3 years long in adolescence** | **NO DIRECT EVIDENCE.** Proxies span 0.35 retention (`li2026`, mortality) to 0.52 (`wang2020`, cardiovascular **events** — not mortality, which it does not report for the normalising group), against `ferrie2007`/`windred2024` implying ~0 residue | **0.0-0.50**, central **0.15** |

Products, computed explicitly:

| Scenario | (a) × (b) × (c) × (d) | Retained fraction |
|---|---|---|
| central, (b) = 0.5 | 0.25 × 0.5 × 0.25 × 0.15 | **0.005** |
| central, (b) = 1.0 (i.e. no male discount, per `ungvari2025`) | 0.25 × 1.0 × 0.25 × 0.15 | **0.009** |
| upper bound, every correction at its most conservative | 0.50 × 1.0 × 0.50 × 0.50 | **0.125** |
| lower bound | any correction at 0 | **0.0** |

### 8.3 Answer

> **My best estimate is that ~1% of the published short-sleep mortality hazard (RR 1.12-1.14) applies
> as a permanent residue of this subject's three-year adolescent exposure, with a plausible span of
> 0% to 12%, and it is not statistically distinguishable from zero. Under `gates.md` this is grade D
> on transportability and grade D on model dependence, so it must be labelled a GUESS.**

Stated the other way, for the model that prefers to start from a dose-appropriate estimate rather than
the categorical headline: **of the current-state hazard for a male sleeping 5-6 h (RR 1.01-1.06),
about 4% (0-25%) survives as a permanent residue** — corrections (c) and (d) only, since (a) and (b)
are already built into that starting point.

### 8.4 The component that IS well defined, and is small

The excess hazard **during** the exposure window (ages 16-19) is arithmetically tractable, and it is
where the honest, defensible answer lives. Correction (d) does not apply here — we are pricing the
exposure while it is happening — so only (a), (b) and (c) discount it:

- Baseline all-cause mortality for a 16-19-year-old male is on the order of **6-9 deaths per 10 000
  per year** (the S8 life-table station must supply the exact national value; I did not import one and
  have not fabricated it).
- Over 3 years that is ~0.002 cumulative probability of death.
- Applying the full un-discounted HR of 1.14 gives ~0.0003 excess probability of death; at ~60 years
  (720 months) of remaining life per death, that is **≈0.2 months — the un-discounted ceiling**.
- Applying (a) × (b) × (c): central 0.25 × 0.5 × 0.25 = **0.031** → **≈0.006 months**; upper
  0.5 × 1.0 × 0.5 = 0.25 → **≈0.05 months**.

**So the exposure-window term is ≈0.006-0.05 months, ceiling 0.2 months.** The permanent-residue term
is 0-12% of whatever the S8 life-table station computes for a lifelong HR of 1.12-1.14 from age 19
(**I deliberately do not compute that conversion — it requires a life table I do not hold, and
inventing one would be a fabrication**). **The permanent-residue term will dominate the total if the
downstream model gives it any real weight, which is precisely why its prior must carry mass at zero:
it rests on no mortality evidence whatsoever.**

Two caveats in opposite directions, both important:

- **Upward:** adolescent mortality is dominated by **injury, motor-vehicle crash and suicide**, not
  cardiometabolic disease. Drowsy driving is a real, plausibly large mechanism by which sleep
  restriction kills 16-19-year-olds, and it is **completely absent from every study in this shard**
  (all of which follow midlife adults dying of CVD and cancer). If another shard has crash-risk
  evidence, that pathway could dominate the entire adolescent-window estimate and my ≈0.006-0.05-month
  figure would be an underestimate — it should be **added to**, not netted against, that shard's number.
  **This is my domain's biggest blind spot.**
- **Downward:** the subject's weekly average sleep is **6.1-6.4 h** — (5.5 × 5 + 7.5 × 2)/7 = 6.07 h
  at the bottom of his weekday range, (6.0 × 5 + 7.5 × 2)/7 = 6.43 h at the top — which on `yin2017`'s
  spline sits at **RR ≈ 1.01** and on `liu2017`'s at **RR ≈ 1.04**, i.e. inside the flat region,
  essentially at the nadir.

### 8.5 Explicit instructions to the downstream model

1. **Use the dose-specific spline values (RR 1.01-1.06 at 5-6 h), not the categorical 1.12-1.14.**
2. **Set the referent at 7 h, not 8 h.**
3. **Apply a residual-causal fraction of 0.25 (0.0-0.50)** to covariate-adjusted observational estimates.
4. **Do not apply a protective multiplier for weekend catch-up.** Sign-unstable; grade D.
5. **De-duplicate by `cohort_family`**: `UK_Biobank` (chaput2026, chaput2024, saintmaurice2024,
   liang2023, li2026, windred2024, zhang2025, sambou2024 — **eight records, one cohort**);
   `SHHS` (zhao2023, yoshiike2023); Swedish March Cohort (akerstedt2017, akerstedt2019);
   `CPS_II` (kripke2002, and it is a dominant constituent of cappuccio2010 and liu2017);
   `Whitehall_II` (ferrie2007, also inside cappuccio2010).
6. **Do not convert `wu2024`'s β = -0.60 into months.** The unit is a parental-survival Cox residual.
7. **Model the adolescent-window effect and any permanent-residue effect as separate terms**, and give
   the residue term a prior mass at zero. The evidence for the residue term is **INSUFFICIENT**, not
   merely uncertain.
