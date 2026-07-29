# Converting hazard ratios into absolute damage: the two calculations, and the three ways to get them wrong

Shard `s17_baseline_risk`. This document specifies, with citations, (1) how to turn a hazard
ratio applied over part of the lifespan into a change in life expectancy, and (2) how to turn
age-specific incidence into a lifetime risk when death competes. It also states, with worked
arithmetic, why the model **must not** multiply a hazard ratio by a lifetime risk.

Everything here is executable: `hr_to_life_expectancy.py` in this directory implements all of
it against `/workspace/data/lifetable_us_male_full.csv`, and every number quoted below is
reproducible by running it.

---

## 0. Notation and the input life table

| symbol | meaning |
|---|---|
| `q(x)` | probability of dying between exact ages `x` and `x+1` |
| `mu(x)` | force of mortality (hazard) over `[x, x+1)`, assumed piecewise constant |
| `l(x)` | survivors to exact age `x`, radix 100,000 male live births |
| `L(x)` | person-years lived in `[x, x+1)` |
| `T(x)` | person-years lived above `x` |
| `e(x)` | expectation of life at `x` = `T(x)/l(x)` |
| `a(x)` | mean fraction of the year lived by those dying in `[x, x+1)` |
| `i(x)` | probability a disease-free survivor at `x` has a first event in `[x, x+1)` |

The relationship between a one-year probability and a piecewise-constant hazard is

```
mu(x) = -ln(1 - q(x))          q(x) = 1 - exp(-mu(x))
```

This matters. **A hazard ratio multiplies `mu`, not `q`.** For small `q` the distinction is
negligible; at `q = 0.36` (a male aged 100) applying HR = 1.5 to `q` gives 0.55 while applying
it to `mu` gives 0.50. Getting this backwards produces a systematic bias concentrated exactly
where most of the surviving cohort's remaining life is being resolved.

Baseline schedule: NCHS *United States Life Tables, 2023*, Table 2 (males), spliced above age
99 with the SSA period life table for 2023 (which publishes single-year `q(x)` to 119, whereas
NCHS closes at an open "100 and older" interval). Published anchors: **e0 = 75.8178 y,
e19 = 57.6565 y, e65 = 18.1943 y**. Rebuilding `e(x)` from `q(x)` alone with `a(x) = 0.5`
reproduces these to 0.0025 y, 0.0003 y and 0.0004 y respectively — two orders of magnitude
inside gate G10's 0.3-year tolerance.

- Arias E, Xu JQ, Kochanek K. United States life tables, 2023. *Natl Vital Stat Rep.* 2025 Jul
  15;74(6):1–63. doi:10.15620/cdc/174591
- U.S. Social Security Administration, Office of the Chief Actuary. *Period Life Table, 2023,
  as used in the 2026 Trustees Report.* https://www.ssa.gov/oact/STATS/table4c6.html
- Preston SH, Heuveline P, Guillot M. *Demography: Measuring and Modeling Population
  Processes.* Blackwell; 2001. (Canonical statement of the single-decrement life table and of
  `e(x) = T(x)/l(x)`.)

---

## 1. Hazard ratio over a window → change in life expectancy

### 1.1 The method: a hazard-modified (impact) life table

This is the standard demographic construction. Do not try to do it with a closed-form formula;
rebuild the table.

1. Read the published baseline `q(x)` for `x = 19 … 120`.
2. Convert to hazards: `mu(x) = -ln(1 - q(x))`.
3. **Choose the exposure window** `[a1, a2)` over which the exposure actually elevates the
   hazard. This is a modelling assumption, not a datum, and it dominates the answer (§1.3).
4. **Choose the cause fraction** `f(x)` — the share of age-`x` mortality that the hazard ratio
   plausibly acts on. If the HR came from an all-cause mortality analysis, `f = 1`. If it came
   from a cause-specific analysis (CVD mortality, suicide), `f(x)` is that cause's share of
   age-`x` mortality and the modified hazard is

   ```
   mu'(x) = mu(x) * [ 1 + f(x) * (HR - 1) ]
   ```

   This is the cause-modified life table; it reduces to `mu'(x) = mu(x) * HR` when `f = 1`.
5. Convert back, `q'(x) = 1 - exp(-mu'(x))`, and re-run the life table:
   `d(x) = l(x) q'(x)`, `L(x) = l(x) - (1 - a(x)) d(x)`, `T(x) = sum_{u >= x} L(u)`,
   `e'(x) = T(x)/l(x)`.
6. Report `Delta e(19) = e'(19) - e(19)`. **In months**, per the project units convention.

Citations for the construction and for the cause-modification step:

- Beltrán-Sánchez H, Preston SH, Canudas-Romo V. An integrated approach to cause-of-death
  analysis: cause-deleted life tables and decompositions of life expectancy. *Demogr Res.*
  2008;19:1323–1350. doi:10.4054/DemRes.2008.19.35 — cause-deleted and cause-modified life
  tables, and the exact algebra for scaling one cause's contribution to `mu(x)`.
- Arriaga EE. Measuring and explaining the change in life expectancies. *Demography.*
  1984;21(1):83–96. doi:10.2307/2061029 — decomposition of a difference in `e(x)` into
  age-specific contributions. Use this to report *which ages* the lost months come from,
  which is far more informative than the scalar.
- Barendregt JJ, Van Oortmarssen GJ, Van Hout BA, Van Den Bosch JM, Bonneux L. Coping with
  multiple morbidity in a life table. *Math Popul Stud.* 1998;7(1):29–49.
  doi:10.1080/08898489809525445 — multistate extension when the exposure acts through several
  competing diseases at once, which is our situation (sleep → BMI → {diabetes, CVD, …}).
- Chaput JP, Carrier J, Bastien C, Gariépy G, Janssen I. Years of life gained when meeting
  sleep duration recommendations in Canada. *Sleep Med.* 2022;100:85–88.
  doi:10.1016/j.sleep.2022.08.006 — a **published application of exactly this method to sleep
  duration**. Their inputs are precisely steps 1–6: sleep-category prevalence, meta-analytic
  all-cause mortality RRs, and national life-table `q(x)`.

### 1.2 Sanity table: all-cause HR sustained for life from age 19

Baseline `e(19) = 57.657 y = 691.9 months`.

| all-cause HR from 19 to death | `Delta e(19)` | months |
|---|---|---|
| 1.05 | −0.592 y | **−7.1** |
| 1.07 | −0.821 y | **−9.9** |
| 1.10 | −1.158 y | **−13.9** |
| 1.13 | −1.488 y | **−17.9** |
| 1.20 | −2.227 y | **−26.7** |
| 1.30 | −3.218 y | **−38.6** |

Useful rule of thumb for review: in a low-mortality male population, **each 1% of lifelong
excess all-cause hazard costs about 0.11 years ≈ 1.3 months of `e(19)`**, mildly concave in
HR. If a reviewer sees a claimed life-expectancy loss that is not roughly consistent with this
scaling given the claimed HR and window, one of the three is wrong.

### 1.3 The window is the whole ballgame

Same HR = 1.13, different windows:

| window over which HR = 1.13 applies | `Delta e(19)` | months |
|---|---|---|
| ages 19–21 only (the 3-year exposure itself) | −0.0258 y | **−0.31** |
| ages 19–39 | −0.252 y | −3.0 |
| ages 40–64 | −0.520 y | −6.2 |
| ages 50+ | −1.087 y | −13.0 |
| ages 65+ | −0.740 y | −8.9 |
| lifelong from 19 | −1.488 y | −17.9 |

**A factor of 58 separates "the harm happens during the exposure" from "the exposure
permanently reprograms mortality risk."** This is the single most consequential modelling
choice in the mortality channel, and it is a choice about *biological persistence*, not about
effect size. Excess mortality hazard during ages 19–21 is nearly free in life-expectancy terms
because baseline mortality there is tiny (`q(19) = 0.00106`); the same relative excess at 65+
is expensive because that is where the deaths are.

Implication for the pipeline: the mortality shard's HR is nearly useless on its own. It must
be paired with an explicit, defended persistence model. Three defensible scenarios:

- **Transient.** Hazard elevated only ages 19–22, returns to baseline. `Delta e(19)` ≈ −0.3
  months at HR 1.13. Supported by recovery-sleep evidence if the mediators normalise.
- **Mediator-locked.** The exposure shifts a persistent mediator (BMI, insulin sensitivity,
  blood pressure) and the hazard stays elevated for life. `Delta e(19)` ≈ −18 months at HR
  1.13. Supported by Ward 2017 (a severely obese 19-year-old has only a 6.1% chance of not
  being obese at 35 — BMI status at 19 is close to absorbing).
- **Delayed onset.** No excess hazard until the mediator matures into disease, say from 40.
  `Delta e(19)` ≈ −12 months at HR 1.13.

Report all three. Do not average them.

### 1.4 Cause-specific HRs must be down-weighted by the cause fraction

HR = 1.5 applied lifelong from 19:

| cause fraction `f` | interpretation | `Delta e(19)` | months |
|---|---|---|---|
| 1.00 | all-cause mortality | −5.011 y | −60.1 |
| 0.30 | ≈ CVD share of male mortality | −1.703 y | −20.4 |
| 0.20 | narrower CVD/metabolic share | −1.158 y | −13.9 |
| 0.10 | one specific cause | −0.592 y | −7.1 |

Two cause fractions this project needs:

- **Suicide, males aged 15–24: 19.9% of all-cause mortality at that age.** From
  NCHS Data Brief 509 (21.1 suicides per 100,000 males aged 15–24 in 2022) divided by the
  life-table all-cause `q(19) = 0.001061`. Suicide is the dominant young-male cause, so a
  psychiatric-channel HR is *not* a small perturbation at these ages.
- **CVD**: roughly 20–30% of male all-cause mortality across the adult lifespan, rising with
  age. Take `f(x)` age-specific from NVSS cause-of-death tables rather than using one scalar.

---

## 2. Lifetime risk from age-specific incidence, with death competing

### 2.1 The estimand

The right target is the **cumulative incidence function** (CIF, also called the subdistribution
function or crude cumulative incidence):

```
CIF_1(t) = integral_0^t  S(u) * lambda_1(u) du ,      S(u) = exp( - integral_0^u [lambda_1 + lambda_2] )
```

where `lambda_1` is the cause-1 (disease) hazard, `lambda_2` the hazard of death from other
causes, and `S` is *event-free and alive* survival. Note that `S` contains **both** hazards.
That is the whole point: you cannot become demented after you are dead.

The **wrong** target is `1 − KM`, the Kaplan–Meier complement obtained by treating death as
censoring. Censoring assumes the person remains at risk unobserved. Death does not.
`1 − KM` estimates a counterfactual "risk if nobody ever died of anything else," which is not
a quantity anyone wants and which is always ≥ the CIF.

### 2.2 The discrete recursion to implement

Per single year of age from index age `a`, with `i(x)` = one-year event probability among
event-free survivors and `q(x)` = one-year probability of death from other causes:

```
A(a)  = 1                                        # P(alive and event-free at exact age a)
LR    = 0
for x = a, a+1, ... , omega:
    LR   += A(x) * i(x) * (1 - 0.5 * q(x))       # actuarial correction: events and deaths
    A(x+1) = A(x) * (1 - i(x)) * (1 - q(x))      #   compete within the interval
return LR
```

The `(1 − 0.5 q(x))` factor is the standard actuarial half-interval adjustment: within a
one-year interval an event and a competing death can both be "due", and each must get half the
interval. Omitting it biases `LR` upward by a few percent at old ages, where `q` is large.

Citations:

- Kalbfleisch JD, Prentice RL. *The Statistical Analysis of Failure Time Data.* 2nd ed. Wiley;
  2002. Chapter 8 — cause-specific hazards and the CIF; the Aalen–Johansen estimator is the
  nonparametric version of the recursion above.
- Beiser A, D'Agostino RB, Seshadri S, Sullivan LM, Wolf PA. Computing estimates of incidence,
  including lifetime risk: Alzheimer's disease in the Framingham Study. The Practical Incidence
  Estimators (PIE) macro. *Stat Med.* 2000;19(11–12):1495–1522. PMID 10844714 — the reference
  implementation used by every Framingham lifetime-risk paper cited in
  `baseline_risks.yaml`. Use this when you want to match a published lifetime risk.
- Fine JP, Gray RJ. A proportional hazards model for the subdistribution of a competing risk.
  *J Am Stat Assoc.* 1999;94(446):496–509. doi:10.1080/01621459.1999.10474144 — regression
  directly on the CIF. **Read the caveat in §3.3**: a Fine–Gray subdistribution hazard ratio
  and a cause-specific (Cox) hazard ratio are different parameters and are not interchangeable.

### 2.3 How much this matters — published, same-cohort, same-men evidence

Not a simulation. Two papers report both estimators for the same subjects:

| source | men, endpoint, index age | competing-risk adjusted | not adjusted | ratio |
|---|---|---|---|---|
| Chêne 2015 (Framingham) | dementia from 45 | **13.8%** (12.2–15.3) | 61.0% (50.4–71.5) | **4.42×** |
| Chêne 2015 (Framingham) | Alzheimer's from 45 | **10.3%** (8.9–11.8) | 53.3% (41.1–65.5) | 5.17× |
| Seshadri 1997 (Framingham) | dementia from 65 | **10.9%** (8.0–13.8) | 32.8% to age 100 | 3.01× |
| Seshadri 1997 (Framingham) | Alzheimer's from 65 | **6.3%** (3.9–8.7) | 25.5% to age 100 | 4.05× |

Seshadri et al. state the mechanism in their own abstract: *"Conventional estimates of
cumulative incidence overestimate the risk when there is a substantial probability of mortality
due to competing causes."*

The bias is largest exactly where this project needs numbers: late-onset diseases in men, whose
competing mortality is high. **A 3–5× inflation is not a rounding error; it is the difference
between "1 in 10" and "2 in 3."**

- Chêne G, Beiser A, Au R, Preis SR, Wolf PA, Dufouil C, Seshadri S. Gender and incidence of
  dementia in the Framingham Heart Study from mid-adult life. *Alzheimers Dement.*
  2015;11(3):310–320. doi:10.1016/j.jalz.2013.10.005
- Seshadri S, Wolf PA, Beiser A, et al. Lifetime risk of dementia and Alzheimer's disease. The
  impact of mortality on risk estimates in the Framingham Study. *Neurology.*
  1997;49(6):1498–1504. doi:10.1212/wnl.49.6.1498

### 2.4 Audit rule for every lifetime risk entering the model

Each absolute risk must carry a `competing_risk_adjusted` flag, and adjusted and unadjusted
figures must never be pooled or compared. In `baseline_risks.yaml` the flag is set for every
record. Note in particular that **Vasan 2002's 90% residual lifetime risk of hypertension is
NOT adjusted** — the paper's own `MAIN OUTCOME MEASURES` reads *"Residual lifetime risk
(lifetime cumulative incidence not adjusted for competing causes of mortality) for
hypertension."* It is therefore not comparable to the Framingham dementia or CVD lifetime
risks in the same file.

---

## 3. The prohibited operation: HR × lifetime risk

> **Do not compute `absolute_risk_exposed = lifetime_risk_baseline × HR`.**

There are three independent reasons, and they push in the same direction: naive multiplication
**overstates** the harm.

### 3.1 A hazard ratio is not a risk ratio once risk is large

Under proportional hazards with a constant ratio `theta`, survival transforms as
`S_1(t) = S_0(t)^theta`, so the correct cumulative incidence is

```
CIF_exposed = 1 - (1 - CIF_baseline) ^ HR
```

Naive multiplication is the first-order Taylor expansion of this around `CIF = 0`. It is fine
for rare outcomes and catastrophic for common ones. With the actual denominators from
`baseline_risks.yaml`:

| outcome | baseline | HR | correct | naive | naive overstates the *increment* by |
|---|---|---|---|---|---|
| dementia, men from 45 (Chêne) | 0.138 | 1.20 | 0.163 | 0.166 | 1.09× |
| MDD morbid risk, men (McGrath) | 0.201 | 1.20 | 0.236 | 0.241 | 1.15× |
| diabetes from 20, men (Gregg) | 0.402 | 1.20 | 0.460 | 0.482 | **1.38×** |
| CVD from 50, men (Lloyd-Jones) | 0.517 | 1.20 | 0.582 | 0.620 | **1.58×** |
| hypertension from 55 (Vasan) | 0.900 | 1.20 | 0.937 | **1.080** | **4.88×** |

The hypertension row returns a probability of 1.08. Any pipeline that can emit a probability
above 1 has no guard rail on this operation; add an assertion.

Even `1 − (1 − CIF)^HR` is only an approximation, because it assumes the hazard ratio is
constant over all ages and that no competing risk is differentially affected. Prefer §2.2:
scale `i(x)` by the HR at each age and re-run the recursion.

### 3.2 Competing mortality absorbs part of the effect

If the exposure also raises the mortality hazard `lambda_2` (short sleep plausibly does), then
exposed people spend *less* time at risk of the non-fatal outcome. The CIF of the non-fatal
outcome therefore rises by *less* than the disease-hazard ratio implies, and can even fall
while the disease hazard rises. Naive multiplication ignores this entirely. This is why
`hr_to_life_expectancy.lifetime_risk()` takes the mortality schedule as an argument rather than
a scalar.

### 3.3 A lifetime risk and a hazard ratio usually refer to different things

Four mismatches to check before any multiplication:

1. **Index age.** `Delta` risk depends on where you start. Gregg 2014's 40.2% is *from age 20*;
   Lloyd-Jones 2006's 51.7% is *from age 50* conditional on being CVD-free at 50, which
   requires first multiplying by `P(survive 19 → 50) = 0.9216` and then adding the incidence
   between 19 and 50 that the published figure excludes.
2. **Case definition.** Gregg 2014 is *diagnosed* diabetes of any type; NHANES total diabetes
   in men is 18.0% versus 12.9% diagnosed, so the diagnosed-based lifetime risk understates the
   biological disease by a factor of about 1/0.717. Vasan 2002 is ≥140/90; the 2024 NHANES
   figure is ≥130/80. Substituting one for the other silently changes the answer.
3. **Estimator.** Cause-specific Cox HRs (what most cohort papers report) describe the hazard
   among those still at risk; Fine–Gray subdistribution HRs describe the CIF directly. Only the
   latter can be read off as "changes absolute risk by." Khan 2018's *competing* hazard ratios
   in `baseline_risks.yaml` are the former.
4. **Population.** An HR estimated in UK Biobank 40–69-year-olds applied to a Framingham-based
   lifetime risk for a 2026 US 19-year-old compounds two transportability leaps. Inflate
   uncertainty accordingly; do not treat the CI on either input as the CI on the product.

### 3.4 What to do instead — the required procedure

```
1. Take the published age-specific incidence i(x) (or reconstruct it so that the recursion in
   §2.2 reproduces the published lifetime risk to within Monte Carlo error). CALIBRATE FIRST:
   if your i(x) does not reproduce the published baseline lifetime risk, stop.
2. Scale the incidence HAZARD, in the window where the exposure acts:
       lambda_1'(x) = lambda_1(x) * HR(x)   for x in [a1, a2), else lambda_1(x)
3. Scale the mortality hazard too, if the exposure affects mortality (§1).
4. Re-run the competing-risk recursion with BOTH modified schedules.
5. Report the difference in CIF as an absolute risk difference in percentage points, plus the
   number needed to harm = 1 / risk difference.
6. Report Delta e(19) in months from the hazard-modified life table (§1) as a separate number.
   Do not add it to the risk difference; they are different units answering different questions.
```

---

## 4. Calibration targets for gate G10 and the regression tests

| target | published value | source |
|---|---|---|
| male `e0`, US 2023 | 75.8 y (75.8178 full precision) | NCHS NVSR 74(6) Table 2 |
| male `e19`, US 2023 | 57.7 y (57.6565 full precision) | NCHS NVSR 74(6) Table 2 |
| male `e65`, US 2023 | 18.2 y (18.1943 full precision) | NCHS NVSR 74(6) Table 2 |
| male `e0` (independent) | 75.79 y | SSA period life table 2023 |
| male `e19` (independent) | 57.62 y | SSA period life table 2023 |
| dementia LR, men from 45, competing-risk adjusted | 13.8% (12.2–15.3) | Chêne 2015 |
| dementia LR, men from 45, unadjusted | 61.0% (50.4–71.5) | Chêne 2015 |
| CVD LR, men from 50 | 51.7% (49.3–54.2) | Lloyd-Jones 2006 |
| diabetes LR, men from 20 | 40.2% (39.2–41.3) | Gregg 2014 |
| male `e50`, US 2023 | 29.96 y (29.9611 full precision) | NCHS NVSR 74(6) Table 2 |
| life expectancy gap, short vs recommended sleep, at age 20 | 1.2 y | Chaput 2022 |

The Chaput row is the end-to-end test. **Feeding an all-cause mortality HR of 1.10–1.13 lifelong
from age 20 through this shard's life table returns −1.15 to −1.48 years at age 20; Chaput et
al.'s independently published figure is −1.2 years.** Two different life tables (Canadian vs
US), two different implementations, one answer. If a future change to the exposure engine or
the life table breaks this agreement, the change is wrong.

### 4.1 Bracketing the mortality channel with four independent publications

The four published sleep life-expectancy estimates disagree by a factor of four, and the
disagreement is not noise — it orders itself precisely by how much *non-sleep* lifestyle each
contrast absorbs:

| study | estimate | index age | what the contrast actually is |
|---|---|---|---|
| Chaput 2022 | +1.20 y | 20 | sleep **duration alone**, life table + meta-analytic RR |
| Huang 2023 | −2.31 y | 40 | 5-item sleep composite, **CVD-free** years, men, UK Biobank |
| Li 2024 | −4.70 y | 30 | 5-factor sleep composite, men, NHIS–NDI |
| Ma 2023 | +5.00 y | 50 | **1 of 8** cardiovascular-health components, *not mutually adjusted* |

Ma et al.'s 5.0-year figure is the one a reader is most likely to quote and the one least
entitled to be quoted, and the paper refutes it with its own arithmetic: the tobacco component
alone is worth 7.4 years and the sleep component alone 5.0 years, summing to **12.4 years,
which already exceeds the entire high-versus-low total LE8 contrast of 8.9 years** before the
remaining six components are counted. Component contrasts that sum to more than the whole
cannot be independent; the sleep contrast is carrying most of the smoking, diet, BMI, glucose
and blood-pressure effect. Confirming this, mean sleep-health score is 68.2 in their low-CVH
stratum versus 93.2 in the high-CVH stratum, so the sleep score is largely a proxy for overall
cardiovascular health.

Allocating Ma's **male** total of 8.1 years equally across its 8 components gives ≈1.0 year for
sleep. That is *our* arithmetic and not published by Ma et al., but it converges with Chaput's
independently derived 1.2 years and with the HR 1.10–1.13 range above. Three unrelated methods
— a Canadian life table driven by meta-analytic relative risks, a US NHANES cohort life table,
and this shard's hazard-modified NCHS life table — agree on roughly **1.0–1.5 years of `e19`
for a lifelong short-sleep habit.** That is the defensible prior for the mortality channel.

The decisive caveat is section 1.3, not the choice among these four papers: **all four price a
lifelong habit.** The subject's documented exposure is three years at ages 16–19. The same
HR 1.13 confined to ages 19–21 costs 0.026 years — about **0.3 months, roughly 58× smaller**
than the lifelong figure. Choosing between 1.2 and 5.0 years is a second-order argument; the
exposure window is the first-order one.

---

## 5. What this shard could not supply, and what the model should do about it

1. **Age-specific cumulative incidence of diabetes at 50/65/80 for US males is not published.**
   `baseline_risks.yaml` carries `DERIVED_BOUNDS` for it with deliberately wide ranges. Do not
   use them as point estimates; derive the schedule from the published lifetime risk plus the
   NHANES prevalence shape and carry the full width.
2. **Male dementia lifetime risk is uncertain by a factor of 3.6, and the uncertainty is
   asymmetric.** Five published estimates, converted to a common index age of 19 by
   multiplying by `S(19→index)` from this shard's life table, span 8.7% to 31.3%:

| study | index age | as published | × `S(19→index)` | from age 19 |
|---|---|---|---|---|
| Seshadri 1997 (Framingham, men) | 65 | 10.9% | 0.7996 | 8.7% |
| Chêne 2015 (Framingham, men) | 45 | 13.8% | 0.9418 | 13.0% |
| Fishman 2017 (men, via Hudomiet) | 70 | 24.0% | 0.7274 | 17.5% |
| Hudomiet 2025 (HRS, men, derived) | 70 | 37.8% | 0.7274 | 27.5% |
| Fang 2025 (ARIC, overall) | 55 | 35.0% | 0.8943 | 31.3% |

   Standardising the index age does **not** narrow the range, which proves index age is not the
   driver — ascertainment is. Hudomiet et al. (2025) diagnose the mechanisms, and **all four
   bias downward**: claims data miss undiagnosed dementia; the calibrated cutoff method
   underpredicts prevalence at 85+ by 4.8 points (validated against the ADAMS clinical
   substudy, where their model gave 0.359 against an observed 0.358 while the cutoff method
   gave 0.310); estimates from status measured months before death miss terminal progression;
   and older cohorts had lower life expectancy, so more members died young where dementia risk
   is low. Because every identified bias points the same way, **the low end is likelier to be
   wrong than the high end.** Use 20–30% as the central band and carry 9–31%; do not treat
   Chêne's 13.8% as the point estimate. Separately, only 20.1% live with dementia for 5+ years
   against 41.3% who ever have it, so a QALY model that applies a multi-year disability weight
   to the lifetime risk roughly doubles the true loss.
3. **No published QALY estimate exists for short sleep.** Life-years, yes (Chaput 2022, Li
   2024); utility-weighted QALYs, no. If this pipeline emits one it is novel and has nothing to
   validate against.
4. **Every absolute risk here is a period estimate for a cohort that is not the subject's.**
   A 2023 period life table assumes a 19-year-old faces 2023's age-80 mortality in 2087. Real
   cohort mortality will almost certainly be lower, which *shrinks* absolute life-expectancy
   losses and *raises* lifetime risks of late-onset disease. Run the multiverse both ways.
