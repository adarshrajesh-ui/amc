# `s09_obesity_bmi` — obesity, BMI and energy balance summary

Subject: 18-year-old male, weekday sleep ~5–6 h from age 16 to 19, weekend/holiday sleep 7–8 h,
occasional 3–4 h pre-exam nights, occasional 10–11 h weekend nights. **Exposure has ended; the
question is what, if anything, persists.**

39 studies extracted, 87 effect estimates, all identifiers verified against Crossref and PubMed.

---

## 0. Exposure dose used for all arithmetic below

Term-time weekly average: (5 nights × 5.5 h + 2 nights × 7.5 h) / 7 = **6.07 h/night**.
Allowing ~30% of the year at holiday sleep of 7.5 h gives an **annualised average of ~6.5 h/night**.

Against an 8 h adolescent referent this is an average deficit of **~1.5 h/night** (range 0.9–1.9 h
depending on referent choice and holiday fraction). Every scaled number below uses **1.5 h/night**
as the central dose and flags the range. Note this is roughly **half** the deficit implied by
looking only at weekdays — a distinction most of the source literature does not make.

---

## 1. The per-hour BMI effect

The single most important finding in this shard is that **the per-hour BMI coefficient varies by a
factor of ~12 depending on study design, and the better designs give the smaller numbers.**

| Source | Design | Tier | Per-hour BMI effect | Scaled to 1.5 h/night deficit |
|---|---|---|---|---|
| Cappuccio 2008 (adults) | pooled cross-sectional | TX | **0.35 kg/m²** per h (0.12–0.57) | **+0.53 kg/m²** (0.18–0.86) |
| Taheri 2004 (midlife, BMI ≈31) | cross-sectional, PSG exposure | TX | **0.37 kg/m²** per h (8 h→5 h: 31.3→32.4) | +0.55 kg/m² |
| Gariépy 2018 (adolescents) | cross-sectional, school-start proxy | TX | 0.12 BMI-z per h (0.00–0.24) | +0.18 BMI-z |
| **Miller 2018 (paediatric)** | **prospective, 24 cohorts** | **T5** | **0.03 kg/m² per h (0.01–0.04)** | **+0.045 kg/m² (0.015–0.06)** |
| Miller 2018 (paediatric) | prospective, 18 cohorts | T5 | 0.03 BMI-z per h (0.01–0.04) | +0.045 BMI-z |
| **Ruan 2015 (paediatric)** | **prospective, dose-response** | **T5** | **0.05 kg/m² per h per YEAR (0.01–0.09)** | **+0.23 kg/m² over 3 y (0.05–0.41)** |
| Widome 2023 (grade 9→11) | quasi-experiment (school start) | T2 | ≈0; BMI DiD **−0.02 kg/m² (−0.6, 0.6)** for ~0.9 h more sleep opportunity over 2 y | ≈0, CI excludes |effect| > 1.0 kg/m² |
| LeMay-Russell 2021 (8–17 y) | prospective, 14-d actigraphy, measured fat mass | T4 | null (p > 0.09) | ≈0 |
| Hayes 2023 (adults) | Mendelian randomization | T3 | +0.039 SD per h (−0.06 to 0.13), p = 0.42 — **wrong sign, null** | ≈0 |

**Recommended prior for the downstream pooler.** Use the prospective paediatric estimates as the
central values, not the cross-sectional ones:

- **Level parameterisation: 0.03 kg/m² per hour of nightly deficit (95% CI 0.01–0.04)** → for this
  subject, **+0.05 kg/m² (0.02–0.06)**.
- **Rate parameterisation: 0.05 kg/m² per hour per year (95% CI 0.01–0.09)** → over 3 years,
  **+0.23 kg/m² (0.05–0.41)**.
- Treat Cappuccio's 0.35 kg/m²/h as a **hard upper bound with near-zero weight**. The same Add Health
  cohort gives a cross-sectional male prevalence ratio of 1.8 and a longitudinal risk ratio of 1.2
  (Suglia 2014) — a ~50% attenuation on the log scale when temporality is imposed. Cappuccio's own
  conclusion: *"Causal inference is difficult due to lack of control for important confounders and
  inconsistent evidence of temporal sequence in prospective studies."*
- **Inflate uncertainty toward zero**: the three designs with the strongest identification in or near
  the target age band — Widome 2023 (T2 quasi-experiment, ages 14–17), Hayes 2023 (T3 MR, adults),
  LeMay-Russell 2021 (T4 objective actigraphy, ages 8–17) — are **all null**.

**Converted to kilograms** at a nominal 1.78 m: 1 kg/m² ≈ 3.17 kg, so the prospective range
0.05–0.23 kg/m² is **≈0.2–0.7 kg**, and the cross-sectional upper bound 0.53 kg/m² is **≈1.7 kg**.

**Obesity-risk framing** (categorical, for completeness):

| Source | Contrast | Estimate |
|---|---|---|
| Zhou 2019 (adults, dose-response) | per 1 h below a 7 h referent | RR **1.09 (1.05–1.14)** → this subject's annualised 6.5 h ≈ RR **1.04**; weekday-only 5.5 h ≈ RR **1.14** |
| Suglia 2014 (Add Health, 16→21 y) | <6 h vs 6–8 h at age 16 → incident obesity at 21 | RR **1.2 (1.0–1.6)** — CI touches the null |
| Miller 2018 (adolescent stratum) | short vs adequate sleep | RR **1.30 (1.11–1.53)** |
| Krueger 2015 (Add Health) | short sleep at 4/4 waves over 15 y | OR **1.45 (1.03–2.04)** |
| Itani 2017 (prospective, all ages) | short vs normal | RR **1.38 (1.25–1.53)**, but the same paper found **no obesity dose-response** |
| Fatima 2015 (paediatric, longitudinal) | short vs **long** sleep | OR **2.15 (1.64–2.81)** — the inflated contrast; do not use as short-vs-normal |
| Deng 2021 (paediatric, prospective) | short vs referent | RR **1.57 (1.36–1.81)**, but the dose-response signal was confined to ages **1–13** |
| Chen 2008 (paediatric) | per 1 h more sleep | OR **0.91 (0.84–1.00)** — CI touches the null |

---

## 2. Experimental energy balance — the numbers, and why they do not add up

### Intake goes up
| Source | Protocol | Extra intake |
|---|---|---|
| **Al Khatib 2017 (pooled, 11 trials, n=172)** | partial sleep deprivation vs control | **+385 kcal/d (252–517)** |
| St-Onge 2011 (n=30, crossover, DLW) | 4 h vs 9 h × 5 nights | +296 kcal/d (SE 123, backed out from P=0.023) |
| Nedeltcheva 2009 (n=11, crossover, 14 d) | 5.5 h vs 8.5 h bedtime | +221 kcal/d **from snacks only**; meals unchanged (P=0.51) |
| Spaeth 2013 (n=225) | 4 h TIB × 5 nights | +553 ± 266 kcal in the 22:00–03:59 window; intake reached 130% vs 101% of requirement |
| Tasali 2022 (n=80, RCT, reverse direction) | **+1.2 h/night** in habitual short sleepers | **−270 kcal/d (−393 to −147)**, i.e. ≈ **−225 kcal per hour of sleep gained** |
| McNeil 2017 (n=43) | individual responses | ΔEI ranged **−813 to +1437 kcal/d** — a substantial minority ate *less* |

### Expenditure also goes up — partially offsetting
| Source | Finding |
|---|---|
| **Markwald 2013** | 24-h EE **+~5% (~111 kcal/d)** during 5 d of 5 h sleep |
| Depner 2021 | 24-h EE **+6 percentage points** vs adequate sleep on day 2 (10 ± 1% vs 4 ± 3%) |
| Nedeltcheva 2009 | +136 kcal/d, not significant (P=0.58) |
| Shechter 2014 | RMR +58 kcal/d (P=0.23); thermic effect of food **identical** (P=0.98) — thermogenesis is not the route |
| **Al Khatib 2017** | pooled: **no significant change in total EE or RMR** |
| St-Onge 2011 | DLW total EE **−22 kcal/d** (P=0.83) |

**Net surplus: +274 kcal/d** if the Markwald offset is real, **+385 kcal/d** if the pooled null for
expenditure is right. The literature genuinely disagrees on this; Capers 2015's RCT-only review sides
with the offset ("sleep restriction increases food intake **and total energy expenditure** with
inconsistent effects on integrated energy balance as operationalized by weight change"), while
Al Khatib's meta-analysis finds no EE effect.

### Weight over the protocol
| Source | Protocol | Weight change |
|---|---|---|
| Markwald 2013 | 5 d insufficient sleep | **+0.82 ± 0.47 kg** |
| Spaeth 2013 | 5 nights, restricted vs control | **+0.86 kg (0.12–1.60)** between groups (0.97 ± 1.4 vs 0.11 ± 1.9 kg) |
| Depner 2019 | 9 nights of 5 h | SR **+1.4 ± 0.5 kg**; catch-up group **+1.3 ± 0.4 kg**; **controls on 9 h also +1.0 ± 0.8 kg** |

### The extrapolation failure — be explicit about this
A sustained +274 kcal/d over 3 years is 300,000 kcal, or **39 kg** at 7,700 kcal/kg. Even using a
proper dynamic energy model — Tasali's cited benchmark, *"a sustained increase in energy intake of
even 100 kcal/d would result in a weight gain of about 4.5 kg over 3 years"* — the prediction is
**~12 kg over 3 years**, or **~9 kg** if scaled to weekday nights only.

**The observed longitudinal divergence is 1–2 kg over 6 years** (Chaput 2008: short sleepers gained
1.98 kg (1.16–2.82) more than average-duration sleepers over 6 y) and **~0.2–0.7 kg** by the
prospective per-hour BMI coefficients in §1. **The laboratory intake signal over-predicts real-world
weight divergence by roughly 10–50×.** Five reasons, all documented in the extracted records:

1. **Lab feeding is not real feeding.** Markwald's protocol served *"∼130–150% more calories than
   BL"* of hyperpalatable food ad libitum. Spaeth's restricted subjects hit 130% of requirement.
2. **Lab doses are far more extreme.** 4 h vs 9–10 h, versus this subject's ~6.5 h annualised average.
3. **The control arms gain weight too.** Depner 2019's adequately-slept controls gained 1.0 ± 0.8 kg;
   the sleep-attributable increment was only **+0.4 kg, 95% CI ≈ −0.21 to +1.01 — not significant**.
   Depner 2021 makes it explicit: 24-h energy balance rose **+798 ± 97 kcal/d** across the protocol
   *"with no significant differences between groups"*, and the authors conclude *"the effects of
   adequate sleep and insufficient sleep, with or without or weekend recovery sleep, on 24 h-EB were
   similar."*
4. **Protocols run 2–14 days**, far too short to capture adaptive compensation.
5. **Expenditure rises**, cancelling ~29% of the intake surplus if Markwald is right.

### Appetite hormones — weaker than the standard narrative
| Source | Leptin | Ghrelin | Design note |
|---|---|---|---|
| Spiegel 2004 (n=12 men, mean 22 y) | **−18%** (P=0.04) | **+28%** (P<0.04) | 4 h vs **10 h**, only **2 days**; hunger +24%, appetite +23% |
| Taheri 2004 (n=1,024, mean 53 y) | **−15.5%** for 5 h vs 8 h habitual | **+14.9%** for 5 h vs 8 h PSG | cross-sectional; ~half Spiegel's magnitude |
| **Nedeltcheva 2009 (n=11, 14 days)** | **no significant difference** | **no significant difference** | **failure to replicate** at 5.5 h vs 8.5 h over 2 weeks |
| Markwald 2013 | weight gain occurred *"despite changes in … ghrelin and leptin, and peptide YY, which signaled excess energy stores"* | | hormones moved the *protective* way while weight rose |

Spiegel's numbers are the best age match in the shard (12 healthy men, 22 ± 2 y, BMI 23.6) but are a
**2-day, 4-h-vs-10-h acute contrast**. The two longer or larger studies (Nedeltcheva 14 days; Markwald
5 days) find the hormone pathway either absent or pointing the wrong way. **Treat −18%/+28% as an
acute upper bound, not a 3-year steady state.**

---

## 3. Mendelian randomization vs observational

| Estimand | Observational | Mendelian randomization |
|---|---|---|
| **Adult BMI per hour** | −0.35 kg/m² (Cappuccio, TX); −0.03 kg/m² (Miller, T5) | **+0.039 SD (−0.06 to 0.13), p = 0.42** — null and wrong-signed (Hayes 2023); *"not clearly associated with BMI in adults"* (Wang 2019) |
| **Clinical obesity** | RR 1.38 (1.25–1.53) (Itani) | **OR 1.00 (0.99–1.00), p = 0.24** (Hayes 2023) |
| **Childhood BMI per hour** | −0.03 BMI-z (Miller); −0.06 BMI-z (Deng) | −0.29 SD (−0.54 to −0.04) (Wang 2019) ≈ −1.4 kg/m²/h; −0.93 SD (−1.74 to −0.11) (Hayes) ≈ −4.4 kg/m²/h |
| **Visceral fat** | not extracted | **−0.11 kg per hour (p = 8×10⁻¹⁶); men −0.17 kg** (Yu 2022), L-shaped |
| **Reverse: BMI → sleep** | **B = −0.02, SE 0.01, p < 0.01** (Sokol 2020, Add Health) | 0.01 (−0.04 to 0.07), p = 0.63 (Hayes) |

**Answer to "does MR support a causal effect of short sleep on BMI?" — No, for adults; weakly and
unstably, for children; and yes for visceral fat specifically.**

- Hayes 2023 is the cleanest test and finds **nothing** for adult BMI or clinical obesity. Its
  own summary: *"There was little evidence for effects of sleep traits on adiposity traits."* In that
  same analysis it is **insomnia**, not short duration, that raises BMI (**0.47 SD, 95% CI 0.22–0.73**).
- The childhood MR estimates are **not credible as magnitudes**. Hayes' −0.93 SD/h implies ~4.4 kg/m²
  per hour; it collapses to **−1.77 SD (95% CI −7.24 to 3.39)** after Steiger filtering. Wang's
  −0.29 SD/h is 3× smaller and its CI barely excludes zero. Wang's own conclusion is the honest
  ceiling: *"A small beneficial effect of sleep on BMI in children cannot be ruled out."*
- Yu 2022's visceral-fat result is the one strong MR signal, and it is **compartment-specific**: MR
  finds an effect on the visceral depot but not on BMI. If real, the expected phenotype is fat
  redistribution without much BMI change — which would make BMI the wrong outcome to be tracking.
- **The MR/observational gap runs in the same direction as the cross-sectional/prospective gap**:
  observational cross-sectional 0.35 kg/m²/h → observational prospective 0.03 kg/m²/h → MR ~0. Two
  independent identification strategies both say the raw association is mostly confounding and
  reverse causation. Sokol 2020's cross-lag models locate the reverse arrow directly: **higher BMI
  precedes shorter sleep, not the reverse**, in the exact age window 12→18→24→32.
- **Caveats that cut the other way, and should widen the posterior rather than close it:** MR
  instruments *lifelong average* habitual sleep duration, so a null MR does not exclude a real effect
  of a discrete 3-year episode; MR instruments for sleep duration are weak (they explained
  **0.13–2.07%** of exposure variance in Hayes); and the GWAS populations are middle-aged. Yang 2024's
  umbrella review asserts that *"a causal role was only demonstrated in obesity, hypertension, and
  CHD by MR"* — **this directly conflicts with the primary MR records extracted here** and names
  neither the study nor the adiposity trait. That conflict is unresolved and is logged as a gap.

---

## 4. Reversibility — the question that actually matters here

### Direct evidence: **INSUFFICIENT EVIDENCE.**

**No study exists that follows people through a defined multi-year period of short sleep, documents
their sleep normalising, and then measures whether weight gained during the exposure persists,
reverses, or continues to accumulate.** I searched for this specifically (persistence/reversal of
sleep-attributable weight gain, former short sleepers, weight regain after sleep normalisation,
recovery-sleep protocols with body-composition follow-up) and found nothing. The closest randomised
protocol, Markwald 2013, follows the transition for **5 days**. The closest observational analysis,
Chaput 2012, does not measure reversal at all — it measures the *rate of further gain*. This is the
single biggest gap in my domain and the downstream model should carry it as unresolved rather than
imputing a value from the analogues below.

### Nearest analogues, in descending order of usefulness

1. **Chaput 2012 (T5, closest in structure, weak in design).** Baseline short sleepers (≤6 h) who
   raised sleep to 7–8 h over 6 years (+1.52 ± 0.66 h/day, n=23) gained **1.1 ± 0.36 kg/m² less BMI**
   and **2.4 ± 0.64 kg less fat mass** than those who stayed short (n=20). Critically, *"We did not
   observe any significant difference in adiposity changes between the control group and
   short-duration sleepers who increased their sleep duration"* — after normalising, their trajectory
   became indistinguishable from adults who had never been short sleepers. The authors' own wording is
   *"an attenuation of fat mass gain"* — **attenuation of future gain, not reversal of past gain.**
   n=43 total, unrandomised, self-selected sleep-changers, obesity-enriched family cohort: RoB high.
2. **Tasali 2022 (T1, best causal design).** +1.2 h/night in habitual short sleepers produced
   **−270 kcal/d** and **−0.87 kg (−1.39 to −0.35) in 2 weeks**; controls *gained* 0.39 kg (0.02–0.76).
   So extending sleep does move weight downward — but over 2 weeks, in adults with overweight aged
   21–40, and the authors state plainly that *"it remains unknown whether extending sleep duration can
   be an effective strategy for preventing or reversing obesity."*
3. **Markwald 2013 (T1, the only direct transition measurement).** Going 5 h → 9 h cut intake
   (*"reduced their food intake after transitioning from the 5-h to 9-h condition"*), and weight
   change over the recovery period was **−0.03 ± 0.50 kg**. Intake reversibility looks fast; the
   ~0.8 kg already gained was **not** lost in 5 days.
4. **Widome 2023 (T2, right age band, precise null).** A real policy that delayed high-school start
   by 50–65 min produced a BMI difference-in-differences of **−0.02 kg/m² (−0.6, 0.6)** over 2 years:
   *"Students' BMIs increased in parallel in both policy change and comparison schools over time."*
   Weight-related *behaviours* improved; BMI did not.
5. **Al Khatib 2018 (T1, counterweight to Tasali).** A second sleep-extension RCT found
   *"no significant differences between groups in markers of energy balance or cardiometabolic
   health."* It also caps the achievable dose: **+0:55 h in bed yielded only +0:21 h of actual sleep**
   (95% CI 0:06–0:36), i.e. ~38% conversion.
6. **Yoong 2016 and Liu 2024 (T1 pooled).** Interventions with a sleep component do not move
   paediatric BMI: **−0.04 kg/m² (−0.18, 0.11)**, I²=0%; and **d = 0.18 (−0.04, 0.40)**, I²=84%. Yoong
   notes the confound honestly — *"only one study included in the meta-analysis successfully changed
   sleep duration in children"* — so this is partly a delivery failure, not only a biology failure.
7. **Depner 2019 (T1) vs Choi 2023 / Lee 2025 (TX) — an unresolved conflict about catch-up sleep.**
   In the laboratory, adding 2 days of ad libitum weekend recovery **did not prevent weight gain**
   (WR +1.3 ± 0.4 kg vs SR +1.4 ± 0.5 kg, SR-vs-WR p = 0.91). Cross-sectionally in adolescents,
   ≥3 h of weekend catch-up sleep is associated with **OR 0.67 (0.57–0.80)** for overweight/obesity
   and **−0.18 BMI-z** (Lee 2025, n=12,434), and <3 h of catch-up among <6 h weekday sleepers with
   **RR 1.93 (1.07–3.48)** (Choi 2023). These point in opposite directions; the observational estimates
   are the ones most vulnerable to reverse causation.

### Explicit reversibility statement for the downstream model

> **On the specific question — is weight gained during 3 years of short sleep persistent after sleep
> normalises? — there is INSUFFICIENT EVIDENCE. No study measures it.**
>
> What the surrounding evidence supports, with numbers:
>
> - **The forward hazard appears to be largely removed once sleep normalises.** Former short sleepers
>   who raised sleep to 7–8 h showed adiposity gain statistically indistinguishable from never-short
>   controls over 6 years (Chaput 2012, T5, RoB high), and 2 weeks of sleep extension produced a
>   negative energy balance and −0.87 kg (Tasali 2022, T1).
> - **There is no evidence that already-accumulated weight spontaneously reverses.** The only direct
>   measurement of the transition shows weight stops rising but does not fall (−0.03 ± 0.50 kg over 5
>   recovery days, Markwald 2013). Nothing longer than 5 days exists.
> - **The amount at stake is small.** The best prospective per-hour coefficients imply
>   **+0.05 to +0.23 kg/m² (≈0.2–0.7 kg)** attributable to this exposure, with a cross-sectional upper
>   bound of ~0.5 kg/m² (≈1.7 kg). The T2 quasi-experiment in the right age band, the T3 MR in adults,
>   and the T4 objectively-measured prospective study are **all null**. A posterior centred near zero
>   with an upper tail around 1–2 kg is defensible; a posterior implying several kg is not.
> - **One mechanism runs the other way and argues for normalising anyway.** In the exact age window,
>   the causal arrow that the data actually support is **BMI → shorter sleep** (Sokol 2020: B = −0.02,
>   SE 0.01, p < 0.01, with the sleep → BMI path null). Any weight already gained can help sustain
>   short sleep, so normalisation is worth doing to break the loop even though the direct weight
>   stake is small.
> - **Caveat outside this shard's extraction:** BMI at 18–19 tracks strongly into adulthood for
>   reasons unrelated to sleep. Whatever weight exists now will tend to persist on its own. That is an
>   assumption flagged for another shard, **not** an effect estimate extracted here.

---

## 5. Six numbers to carry forward

| # | Quantity | Estimate | Source | Tier |
|---|---|---|---|---|
| 1 | Prospective per-hour BMI effect | **0.03 kg/m² per h (0.01–0.04)** → +0.05 kg/m² for this subject | Miller 2018 | T5 |
| 2 | Prospective per-hour BMI **rate** | **0.05 kg/m²/year per h (0.01–0.09)** → +0.23 kg/m² over 3 y | Ruan 2015 | T5 |
| 3 | Pooled experimental intake effect | **+385 kcal/d (252–517)**; expenditure offset +111 kcal/d ⇒ net ~+274 kcal/d | Al Khatib 2017; Markwald 2013 | T1 |
| 4 | Sleep-attributable lab weight gain | **+0.4 kg, 95% CI ≈ −0.21 to +1.01** over 9 nights (controls gained 1.0 kg) | Depner 2019 | T1 |
| 5 | MR, adult BMI per hour | **+0.039 SD (−0.06 to 0.13), p = 0.42** — null | Hayes 2023 | T3 |
| 6 | Quasi-experiment, right age band | **BMI DiD −0.02 kg/m² (−0.6, 0.6)** over 2 y | Widome 2023 | T2 |

**Cross-cutting warning for the pooler:** four records share the **Add Health** cohort
(`suglia2014`, `sokol2020`, `krueger2015`, `asarnow2015`), two share the **Quebec Family Study**
(`chaput2008`, `chaput2012`), and two share the **same Colorado participants**
(`depner2019`, `depner2021`). `cohort_family` is populated on every effect. Do not treat these as
independent.
