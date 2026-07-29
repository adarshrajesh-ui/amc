# Metabolic summary — shard `s07_metabolic`

Glucose metabolism, insulin sensitivity, and type 2 diabetes risk from short sleep.
30 records, 105 effect estimates, 29/30 identifiers `VERIFIED` (the 30th is a documented Crossref
subtitle artefact). Every number below is traceable to a `quote` field in the named YAML record;
all arithmetic is reproduced in `_conversions.txt`.

**Subject:** 18-year-old male; weekday sleep ~5–6 h from age 16 to 19; weekend/holiday 7–8 h;
occasional 3–4 h nights before exams; occasional 10–11 h weekend nights.
Weekly average = (5.5×5 + 7.5×2)/7 = **6.07 h/day**, i.e. **0.93 h/day below a 7 h referent**.

> **The one-sentence answer.** "Your insulin sensitivity is measurably worse this week" is well
> supported and reverses within days-to-weeks of sleeping more; "your lifetime diabetes risk moved"
> is supported but small — of order a **3–8% relative** increase, not a doubling — and roughly
> **half of even that** dissolves under genetic-instrument and confounding scrutiny.

---

## (a) Acute, reversible changes and their recovery time constants

### a.1 The dose ladder — why protocol severity, not biology, drives the headline numbers

This is the most important table in the shard. Read it top to bottom: as the protocol becomes
realistic, the effect shrinks by roughly an order of magnitude.

| record | protocol | achieved sleep | duration | tier | age match | insulin/glucose effect |
|---|---|---|---|---|---|---|
| `spiegel1999` | 4 h TIB vs **12 h TIB** | ~4 h | 6 nights | T1 | young men | glucose tolerance **−40%**; glucose effectiveness −30%; AIRg −30%; **SI itself NOT significant** |
| `klingenberg2013` | 4 h TIB, **adolescent boys** | ~4 h | 3 nights | T1 | **exact_16_19** | HOMA-IR **+65%** (se 18.3); Matsuda **−28%**; fasting insulin **+59%**; fasting glucose unchanged |
| `broussard2012` | 4.5 h TIB | ~4.5 h | 4 nights | T1 | good_young_adult | adipocyte Akt EC50 **≈3-fold** worse (d = 1.42, se 0.54); pAkt/tAkt AUC −30% |
| `buxton2010` | 5 h TIB vs 10 h | ~5 h | 7 nights | T1 | good_young_adult | IVGTT SI **−20%** (se 5.1); **clamp M only −11%** (se 5.5) |
| `ness2019` | 5 h TIB | ~5 h | 5 nights | T1 | good_young_adult | IVGTT insulin sensitivity d = **−0.98** (se 0.31) |
| `nedeltcheva2009` | 5.5 h TIB, **ad libitum food** | ~5.7 h | **14 days** | T1 | poor_midlife | SI **−17.5%** (se 6.9); 2-h OGTT glucose **+9.1%** (se 2.9) |
| `nedeltcheva2012` | 5.5 h TIB, **hypocaloric diet** | ~5.7 h | **14 days** | T1 | poor_midlife | **OGTT and 24-h glucose NOT impaired**; IVGTT said −26% but authors distrust it |
| `zuraikat2024` | −1.5 h/night, free-living | **6.2 h** | **42 days** | T1 | fair_adult (women) | HOMA-IR **+0.30** units (se 0.12); premenopausal **+0.27** (se 0.13) |
| `dutil2024` | −1.5 h TIB, **adolescents** | **6.2 h** | 7 days | T1 | **exact_16_19** | insulin sensitivity **NOT significantly changed** |

**The subject's weekday dose sits at the bottom two rows, not the top two.** The 40–65% figures come
from 4 h protocols against 9–12 h referents — contrasts 3–4× wider than the subject's ~1.5 h weekday
deficit. Transporting them would overstate the effect several-fold.

**Two convergent readings of the bottom of the ladder:**
- **Dose:** at 6.2 h achieved sleep, the effect is a HOMA-IR shift of ~0.3 units — against a typical
  healthy young HOMA-IR of 1–2, that is roughly **+14% to +27%**, not +65%.
- **Time:** the same 6.2 h dose produced *nothing detectable* at 7 days (`dutil2024`) but a clear
  effect at 42 days (`zuraikat2024`). At realistic doses the cost **accumulates over weeks**, whereas
  4 h protocols produce damage within 3–6 nights. The subject's exposure was ~3 years, far beyond
  either horizon, so accumulation is the relevant regime — but nothing here measures it directly.

### a.2 Measurement method is a first-order confounder in this literature

Surrogate indices systematically overstate the sleep effect relative to clamp measurement. This is
not speculation; four records converge on it:

- `buxton2010`: same participants, **IVGTT −20% but clamp −11%**.
- `nedeltcheva2012`: IVGTT said SI −26%, while OGTT and 24-h glucose showed **no impairment at all**;
  the authors attribute the IVGTT figure to sleep-loss-induced cortisol/GH/ghrelin excursions
  corrupting the Minimal-model fit, and state the test's utility was "limited".
- `sondrup2022` (meta-analysis, 21 trials): clamp-measured **whole-body** insulin sensitivity is
  genuinely reduced, but **peripheral (muscle) insulin sensitivity is unaffected** — so the deficit
  is hepatic/adipose, not muscular.
- `beals2026`: the only extension trial using **clamp + stable-isotope tracers** found **no effect**
  in any tissue compartment.

**Consequence for the modeller:** prefer clamp-based magnitudes (~10–11%) over IVGTT/HOMA-based ones
(~20–65%) when estimating the true insulin-sensitivity change, and inflate uncertainty on any
estimate derived from HOMA-IR or Matsuda.

### a.3 Recovery time constants — resolved as far as the evidence allows

| horizon | record | what recovered | what did NOT |
|---|---|---|---|
| **2 nights** at 10 h | `ness2019` | lipid/NEFA dynamic response fully normalised | **disposition index still suppressed, d = −0.77 (se 0.29)** — glycaemic control had *not* recovered |
| **2 weekend nights** ad lib | `depner2019` | — | insulin sensitivity **−9% to −27%** after weekend recovery vs −13% under sustained restriction; recovery added only **~1.1 h** cumulatively and **delayed circadian phase** |
| **weekend within a 5-day cycle** | `cheung2026` | — | 8 h weekend recovery **insufficient**; and schedule **variability** (8/4/8/4/6 h) caused **~2.5× worse** 2-h glucose deterioration (d = 0.99 vs 0.39) than stable 6 h at *identical total sleep* |
| **3 nights** at 10 h | `killick2015` | insulin sensitivity **+45%** (ΔISx +8.57, se 3.83) in men with a 5-year weekday-restriction history | — |
| **6 nights** at 12 h | `spiegel1999` | all carbohydrate-metabolism abnormalities absent — this *is* the referent condition | no within-week resolution: recovery measured only at the end |
| **9 days** | `buxton2012_fd` | **full normalisation** of glucose and resting metabolic rate | — but the insult included circadian disruption |
| **6 weeks**, +1.1 h | `beals2026` | sleep health and regularity improved | **NO change in multiorgan insulin sensitivity or glycemic control (clamp + tracers)** |
| **6 weeks**, +79 min | `hartescu2022` | HOMA-IR **−0.79** units between-group (se 0.34) | — |
| **7 days**, +1 h, adolescents | `dutil2024` | insulin sensitivity **+20%** | — |

**Time constant, stated honestly.** The acute changes are **reversible on a scale of days to ~1–2
weeks given a large recovery dose** (`spiegel1999` 6×12 h; `buxton2012_fd` 9 days; `killick2015`
3×10 h). They are **not** reversible within 2 nights (`ness2019`, `depner2019`), which is precisely
the recovery the subject actually got each weekend. In units of days, a defensible summary is:
**lipid/dynamic measures τ ≲ 2 days; glycaemic/β-cell measures τ ≈ 3–9 days at a 10–12 h recovery
dose, and > 2 days at any realistic dose.**

**Critical caveat — the recovery evidence does not agree with itself.** Three positive extension
trials (`killick2015` +45% by IVGTT, `dutil2024` +20% by Matsuda, `hartescu2022` −0.79 HOMA-IR) versus
one null (`beals2026`, clamp + tracers). The null used the best measurement and the positives used
surrogates — exactly the bias direction of §a.2. Grade recovery magnitude **C on model dependence**:
sign stable across the positives, but it flips to null in the best-measured trial. Reporting +45%
alone would be indefensible.

### a.4 Timing and regularity matter at least as much as duration — and possibly more

This is the shard's most decision-relevant finding for a subject whose defining pattern is
weekday/weekend alternation, not uniform short sleep.

- `leproult2014`: at **identical 5 h TIB**, adding circadian misalignment **roughly doubled** the fall
  in insulin sensitivity (**−58% vs −32%**) and cut the disposition index by 48% in men.
- `yuan2021`: **3 weeks of sleep restriction WITHOUT circadian disruption produced no adverse
  glycaemic effect**, whereas `buxton2012_fd` — the same ~5.6 h dose for 3 weeks **WITH** forced
  desynchrony — impaired postprandial glucose via inadequate insulin secretion. Sleep loss alone was
  not sufficient; misalignment was.
- `cheung2026`: variability caused ~2.5× worse deterioration than stable short sleep at identical
  total sleep.
- `chen2021`: in adolescents, **1 h later weekend sleep midpoint** raised log HOMA-IR by 0.0486
  (+5.0%) — **the same magnitude as 1 h less weekday sleep** (−0.049 per hour), and independent of it.
- `sondrup2022`: circadian misalignment and slow-wave-sleep suppression harm insulin sensitivity;
  **REM disturbance and sleep fragmentation do not**.
- `liu2025`: evening chronotype OR **1.59** — *larger* than short sleep's 1.18.
- `gao2020`: genetically predicted **insomnia** causes T2D (OR 1.14, P≈1×10⁻⁸) while sleep **duration**
  does not reach significance.

**Implication:** the subject's ~2 h weekend phase shift is plausibly a comparable or larger metabolic
exposure than his weekday duration deficit. A model that scores only hours of sleep debt will
**understate** his exposure. The dominant caveat pulling the other way is `wang2025_wsr`, below.

### a.5 Does weekend catch-up help or hurt? Genuinely unresolved

- **Experiments say it is insufficient:** `depner2019` (recovery did not prevent dysregulation, and
  delayed circadian phase), `cheung2026` (8 h weekend recovery insufficient; variability actively
  harmful).
- **Population data say it helps, specifically for men who are short weekday sleepers:**
  `wang2025_wsr` (NHANES, n=4,036) found weekend recovery associated with **lower** insulin resistance
  in **males** (β = −0.68, se 0.29) and in those with **weekday sleep ≤7 h** (β = −0.39, se 0.17), with
  **no** association in women or in those already sleeping >7 h — and a threshold at ~2 h of recovery.
  The subject sits in every favourable stratum.
- **But** that model adjusts for social jetlag *and* weekday sleep hours, so it estimates the benefit
  of recovered sleep **with the circadian penalty statistically removed** — which is not what a real
  person doing both simultaneously experiences. It is also cross-sectional (TX), self-reported, mean
  age 49.6, and its outcome is a **HOMA-IR index rescaled to 0–100**, so its βs are *not* comparable
  to raw-HOMA-IR effects. See the unit hazard in §Pooling cautions.

**Honest position:** weekend catch-up is probably **partially** mitigating relative to no catch-up,
while remaining clearly inferior to adequate weekday sleep, and it carries a circadian cost that the
observational estimate excludes by construction.

---

## (b) Long-run incident-disease risk per hour of habitual short sleep

### b.1 The dose-response curve (`shan2015`, the primary anchor)

Dose-response meta-analysis, **10 prospective studies, 482,502 participants, 18,443 incident T2D**.
Shape: **U-shaped, nadir at 7–8 h/day**.

| contrast | RR (95% CI) | log_rr | se | provenance |
|---|---|---|---|---|
| **per 1 h shorter, below 7 h** | **1.09 (1.04–1.15)** | 0.086178 | 0.025648 | **reported** |
| 6 h vs 7 h | 1.09 (1.04–1.15) | 0.086178 | 0.025648 | reported (= 1 h) |
| **5 h vs 7 h** | **1.19 (1.07–1.31)** | 0.172355 | 0.051297 | **DERIVED** — log-linear extrapolation, k=2 |
| 4 h vs 7 h | 1.30 (1.11–1.51) | 0.258533 | 0.076945 | **DERIVED, BEYOND DATA — do not use** |
| per 1 h longer, above 8 h | 1.14 (1.03–1.26) | 0.131028 | 0.051417 | reported |

The 5 h and 6 h values the task asked for: **RR 1.19 at 5 h and RR 1.09 at 6 h, relative to 7 h.**
The 5 h figure is *derived*, not published — `shan2015` reports the per-hour slope, and I extrapolated
log-linearly (`conversion_formula` in the record documents this). Treat the 4 h row as illustrative
only; it lies outside the data.

### b.2 Comparators and convergence

| record | population | short-sleep estimate | long-sleep estimate |
|---|---|---|---|
| `shan2015` | 482,502; 10 studies | per-h below 7 h **RR 1.09 (1.04–1.15)** | per-h above 8 h RR 1.14 (1.03–1.26) |
| `cappuccio2010` | 107,756; 10 studies | ≤5–6 h **RR 1.28 (1.03–1.60)**; ≤5 h RR 1.36; **men RR 2.07 (1.16–3.72)** vs women 1.07 | >8–9 h RR 1.48 (1.13–1.96) |
| `liu2025` | **1,478,297; 53 studies** | <7 h **OR 1.18 (1.13–1.23)**; men OR 1.13 (1.04–1.24) | >8 h OR 1.13 (1.09–1.18) |
| `kuroda2025` | UK Biobank 385,135 | self-report ≤5 h **HR 1.30 (1.23–1.39)**; **accelerometer <6 h HR 1.52 (1.09–2.13)** | self-report ≥10 h HR 1.46; **accelerometer ≥10 h HR 1.08 (0.92–1.27), null** |

Short-sleep estimates converge tightly on **RR/OR ≈ 1.1–1.3**. The `cappuccio2010` male-specific
RR of 2.07 is the outlier and is **not reproduced**: `liu2025`, on 14× the sample, gives men OR 1.13.
Do not carry 2.07 as a male multiplier.

**Two findings that materially change how the curve should be used:**

1. **Objective exposure makes short sleep look *worse*, not better.** Within the identical UK Biobank
   cohort, `kuroda2025` gives HR 1.30 by questionnaire but **1.52 by accelerometry**. Self-report
   measurement error biases the conventional literature **downward**. `matthews2012` shows the
   mechanism in adolescents: they over-reported sleep by **1.0 h** versus actigraphy.
2. **The long-sleep limb collapses under better measurement.** Same cohort: ≥10 h gives HR 1.46 by
   questionnaire but **1.08 (null)** by accelerometry, and the curve shape changes from **U** to **J**.
   MR agrees (§c.3).

### b.3 Applying the curve to the subject

Using the `shan2015` slope at the subject's weekly average of 6.07 h (0.93 h below 7 h):

| basis | RR (95% CI) |
|---|---|
| weekly average 6.07 h | **1.083 (1.034–1.135)** |
| weekdays alone, 5.5 h (upper bound, ignores weekend recovery) | 1.138 (1.055–1.227) |

So the observational dose-response implies roughly a **3–14% relative** increase in T2D risk,
best estimate **~8%**, if this exposure were treated as habitual adult sleep. Against a lifetime
baseline of 5–10%, that is an absolute excess of **~0.4–0.8 percentage points** before any
attenuation.

**Four reasons this is an upper bound for *this* subject, not an estimate:**
1. **Age.** All four epidemiological records are midlife-to-elderly (`kuroda2025` median age 58;
   `wang2025_wsr` mean 49.6). **There is no adolescent cohort with incident T2D anywhere in this
   literature.** `liu2025` found the association *strongest at ages 30–39 and attenuating thereafter*,
   with **no data below 30** — so the age trend cannot even be extrapolated downward with confidence.
2. **Duration.** These RRs describe *habitual, sustained* adult sleep over 10–14 years of follow-up.
   The subject's exposure was **3 years in adolescence**, followed by an open future. Nothing here
   licenses treating 3 adolescent years as equivalent to a lifelong exposure.
3. **Pattern.** The exposure is a single average duration. The subject's alternating schedule, whose
   circadian component §a.4 identifies as at least as damaging, is unrepresented.
4. **Confounding.** See §c.

### b.4 Age-matched observational evidence (all cross-sectional, TX)

The only records in the subject's age band, and they are directionally consistent:

- `javaheri2011` (n=387, actigraphy, adolescents): **U-shaped**; HOMA at 5.0 h is **+20.4%** vs the
  age-appropriate optimum of **7.75 h**; at 10.5 h, +23.0%. Short-sleep association **attenuated after
  adiposity adjustment**; long-sleep association **persisted**.
- `matthews2012` (n=245, actigraphy, high-schoolers): shorter **weekday** sleep → higher HOMA-IR;
  **null for long sleep**; adolescents over-reported sleep by **1.0 h**.
- `chen2021` (n=384, Mexican adolescents, mean 13.8 y): per 1 h less weekday sleep, log HOMA-IR
  **+0.049** (se 0.025, ≈ +5.0% HOMA-IR); per 1 h later weekend midpoint, **+0.0486**, independently.

`javaheri2011`'s **+20.4% HOMA at 5 h** is the single most transportable quantitative anchor in the
shard for the subject's *current* state — right age, objective exposure, age-appropriate referent —
but it is cross-sectional and its short-sleep arm did not survive adiposity adjustment.

---

## (c) How much of (b) survives MR and confounding adjustment

### c.1 The direct answer: roughly 40%, and `kuroda2025` lets us compute it within one cohort

`kuroda2025` is the only record reporting a conventional and an MR estimate in the **same** cohort:

| analysis | estimate | log scale |
|---|---|---|
| Cox, self-reported ≤5 h vs 7 h | HR 1.30 (1.23–1.39) | 0.262364 |
| Cox, accelerometer <6 h vs 7–8 h | HR 1.52 (1.09–2.13) | 0.418710 |
| **Two-sample MR, short-sleep instrument** | **OR 1.12 (1.02–1.23)** | **0.113329** |

**Surviving fraction = 0.113329 / 0.262364 = 0.43** against the self-report anchor, or **0.27**
against the accelerometer anchor. So **roughly a quarter to a half** of the observational short-sleep
excess survives genetic instrumentation; the remainder is confounding and reverse causation.

Applied to the subject's weekly average (§b.3, log 0.080022):

| | RR |
|---|---|
| observational, unattenuated | 1.083 |
| **MR-attenuated at 0.43** | **1.035** |
| MR-attenuated at 0.27 | 1.022 |

**Headline for section (c): after causal attenuation, the subject's habitual-exposure T2D risk
increment is of order 2–4% relative — an absolute excess near 0.1–0.4 percentage points on a 5–10%
baseline.** This is small enough that the modeller should be explicit that it is dwarfed by
adiposity, family history, and physical activity.

### c.2 MR is *not* uniformly null — the literature converged in 2025

This is the shard's most important update, and earlier reviews get it wrong:

| record | instrument | estimate | verdict |
|---|---|---|---|
| `gao2020` | 17 SNPs, short sleep, DIAGRAM | OR 1.15 (0.96–1.38), P=0.09 | null |
| `gao2020` | 56 SNPs, **continuous** duration | OR 1.00 (1.00–1.00), P=0.43 | **flatly null** |
| `wang2019` | per hour, DIAGRAM/MAGIC | OR 0.85 → **1.18 per hour *less*** sleep | null (wide) |
| `dashti2019` | sleep-duration GWAS | no causal effect on T2D or BMI | null |
| `bos2019` | glycaemic traits, NEO | null | null |
| **`kuroda2025`** | **23 SNPs, DIAGRAM + FinnGen** | **OR 1.12 (1.02–1.23)** | **SIGNIFICANT** |

**Every point estimate is positive and in the range 1.12–1.18.** The earlier studies were
underpowered; `kuroda2025` gained precision by meta-analysing two outcome consortia. The correct
reading is **convergence on a modest causal effect of about OR 1.12–1.15**, detectable only in the
best-powered analysis — **not** that MR refutes the association. Equally, it is much smaller than
`kuroda2025`'s own accelerometer-based HR of 1.52.

One dissent worth carrying: `gao2020`'s best-powered *continuous* instrument (56 SNPs) is exactly
1.00. Keep non-trivial prior mass on the true per-hour duration effect being near zero.

### c.3 The long-sleep limb does **not** survive — and this is a clean, useful result

- `kuroda2025` MR: long sleep **OR 0.80 (0.60–1.07)** — point estimate *protective*, opposite to the
  same cohort's Cox HR of 1.46.
- `kuroda2025` non-linear MR: 9 h vs 7 h **HR 0.77 (0.52–1.15)**, and **P for non-linearity = 0.94** —
  the genetically instrumented curve is **linear, with no U-shape at all**.
- `kuroda2025` accelerometer Cox: ≥10 h **HR 1.08 (0.92–1.27)**, null; shape becomes **J**, not U.
- `gao2020` MR long sleep: OR 1.10 (0.79–1.51), null.
- `dashti2019`: genetic correlation with T2D appears for **long** sleep but not short — consistent
  with long sleep being a *marker* of illness rather than a cause.

**Directly decision-relevant:** the subject's occasional **10–11 h weekend nights should be modelled
as recovery behaviour, not as an independent metabolic risk exposure.** The observational long-sleep
hazards (`shan2015` RR 1.14/h; `cappuccio2010` RR 1.48; `javaheri2011` +23% HOMA at 10.5 h) survive
neither objective measurement nor genetic instrumentation. Downweight the long-sleep arm heavily.

### c.4 What confounding adjustment does — BMI and sleep apnoea

- `bos2019`: cross-sectional short-sleep/poor-quality associations with fasting insulin (+14.5%) and
  HOMA-IR (+14.3%) **disappeared entirely after adjustment for BMI and sleep-apnoea risk**, and its
  MR arm on glycaemic traits was null.
- `javaheri2011`: the adolescent **short-sleep** HOMA association **attenuated after adiposity
  adjustment** (the long-sleep one did not).
- `kuroda2025`'s Cox models already adjust for BMI, deprivation, income, education, employment,
  activity, smoking, alcohol, cohabitation, and hypertension — and still return HR 1.30/1.52. So
  measured-confounder adjustment does **not** abolish the association in the largest cohort.

**But BMI adjustment is ambiguous, and this must be stated.** Short sleep *causes* weight gain, so
BMI is plausibly a **mediator**, not only a confounder; adjusting for it removes part of the real
causal pathway and *understates* the total effect. `zuraikat2024` resolves this for the experimental
arm decisively: in a **randomised** design, "change in adiposity did not mediate the effects of SR on
glucose metabolism or change results … when included as a covariate." So the glycaemic effect exists
**without** an adiposity pathway, which means the observational BMI-adjustment attenuation in
`bos2019` and `javaheri2011` more likely reflects **confounding in those cross-sectional designs**
than absence of a real effect.

### c.5 Where the causal signal actually localises

Across MR and trial evidence, duration is the *weakest* of the sleep exposures:

| exposure | best causal estimate | source |
|---|---|---|
| **insomnia / sleep continuity** | **OR 1.14 (1.09–1.19), P≈1×10⁻⁸** | `gao2020` MR |
| short sleep **duration** | OR 1.12 (1.02–1.23) | `kuroda2025` MR |
| continuous sleep duration | OR 1.00 (1.00–1.00) | `gao2020` MR |
| long sleep duration | OR 0.80 (0.60–1.07) | `kuroda2025` MR |
| evening **chronotype** (observational) | OR 1.59 | `liu2025` |
| **circadian misalignment** (experimental) | insulin sensitivity −58% vs −32% at equal sleep | `leproult2014` |

**Duration is real but modest; timing and continuity look larger.** For a subject whose exposure is
as much a *timing* pattern as a *duration* deficit, this reallocates the risk narrative.

---

## Answers to the seven required extractions

1. **`spiegel1999`** — 4 h TIB × 6 nights vs 12 h TIB × 6 nights in 11 young men. Glucose tolerance
   **−40%**, glucose effectiveness **−30%**, AIRg **−30%**; evening cortisol raised (p=0.0001);
   **insulin sensitivity itself was NOT significantly reduced** (per `buxton2010`'s Discussion).
   **Recovery-phase (12 h) values:** there are none to report separately — the 12 h condition **is**
   the referent, so the fully-rested state is the zero point by construction and the abnormalities are
   *absent* after 6 nights at 12 h. **Age:** reported only as "11 young men"; no mean or range is
   published and the *Lancet* text is paywalled, so `age_mean`/`age_range` are `null`, not guessed.
   `access_tier: secondhand` for the magnitudes.
2. **`buxton2010`** — 5 h TIB × 7 nights, healthy men: insulin sensitivity **−20%** by IVGTT
   (se 5.1) but **−11%** by euglycemic clamp (se 5.5); salivary cortisol +51%.
   **`buxton2012_fd`** — 5.6 h/day × 3 weeks **with forced desynchrony**: postprandial glucose rose
   via inadequate insulin secretion; **full normalisation after 9 days** of recovery + re-entrainment.
   Read with **`yuan2021`**: 3 weeks of the same restriction **without** circadian disruption caused
   **no** adverse glycaemic effect.
3. **`broussard2012`** — 4.5 h TIB × 4 nights, n=7: adipocyte Akt phosphorylation **EC50 ≈3-fold
   higher** (0.71 vs 0.24 nM; paired diff 0.47 nM, se 0.125; **Cohen's d = 1.42, se 0.54**);
   pAkt/tAkt total AUC **−30%**. Effect is in *peripheral tissue at the molecular level*.
4. **`shan2015`** — see §b.1: per 1 h below 7 h **RR 1.09 (1.04–1.15)**; **6 h RR 1.09**, **5 h RR 1.19
   (derived)**; **10 studies, 482,502 participants, 18,443 cases**; shape **U-shaped, nadir 7–8 h**.
   Comparators in §b.2, including `cappuccio2010` (RR 1.28; men 2.07 — **not replicated**).
5. **Adolescents** — `klingenberg2013` (T1, 4 h TIB × 3 nights, boys 16–17: HOMA-IR **+65%**),
   `dutil2024` (T1, the only adolescent randomised trial with a glycaemic primary outcome:
   extension **+20%**, restriction to 6.2 h **null**), `javaheri2011` / `matthews2012` / `chen2021`
   (TX, actigraphy). **Age match is flagged on every record.** The critical gap: **no prospective
   adolescent cohort with objective sleep and incident glycaemic outcomes exists** — searches
   returned zero — so all age-matched observational evidence is cross-sectional (TX).
6. **MR vs observational** — §c.1–c.3. Gap: observational **1.09–1.52**, MR **1.12** →
   **~27–43% of the observational excess survives**. MR is **not** uniformly null once `kuroda2025`
   is included; the long-sleep limb does **not** survive at all.
7. **Reversibility** — §a.3. Reversible on a **days-to-~1–2-week** scale given a large recovery dose;
   **not** reversible in 2 nights (`ness2019`: disposition index still suppressed, d = −0.77;
   `depner2019`: weekend recovery insufficient and phase-delaying). Confidence limited by the
   `beals2026` clamp null.

---

## Pooling cautions for downstream stations

1. **Unit hazard — do not pool HOMA-IR effects blindly.** `wang2025_wsr` reports βs on a HOMA-IR index
   **rescaled to 0–100**; `zuraikat2024` (+0.30) and `hartescu2022` (−0.79) are in **raw** HOMA-IR
   units. I could not recover the rescaling bounds, so **no conversion factor exists**. Pooling these
   on a common scale would be a serious error.
2. **Cohort-family de-duplication (gate G6).** `kuroda2025` effects 4–5 are **UK Biobank** and overlap
   `shan2015`/`liu2025`/`cappuccio2010` syntheses; `gao2020` and `dashti2019` share the UK Biobank +
   23andMe exposure GWAS (both list n=446,118); `wang2025_wsr` is **NHANES** (as is excluded PMID
   40437485). `cohort_family` is populated on every observational effect.
3. **Tier mismatch inside `kuroda2025`.** The record is tiered **T3** (MR is the primary design), but
   effect 4 (accelerometer <6 h, HR 1.52) is properly **T4** and effect 5 (questionnaire, HR 1.30)
   properly **T5**. Effect 4 is one of very few T4 short-sleep/T2D estimates in existence. Do not pool
   effects 1–3 with 4–5 as independent.
4. **Sign conventions are not uniform.** Extension/recovery records (`dutil2024`, `killick2015`,
   `hartescu2022`, `wang2025_wsr`) are signed so that **benefit** is the favourable direction; most
   restriction records are signed so **negative = harm**. Read `direction_note` on every effect
   rather than flipping signs mechanically.
5. **Explicit nulls are encoded as `value: 0, se: null`** (`dutil2024` restriction arm, `beals2026`,
   `nedeltcheva2012` OGTT, `gao2020` continuous instrument, `bos2019` post-adjustment,
   `javaheri2011` post-adiposity, `yuan2021`). These are **reported non-significances with unknown
   confidence intervals**, not zero-variance estimates. Do not treat them as infinitely precise.
6. **Derived values are labelled.** `shan2015`'s 5 h and 4 h RRs are log-linear extrapolations of the
   published per-hour slope, not published figures. The 4 h row lies outside the data.

## Confidence grades (per `gates.md`)

| headline number | quantity | quality | transportability | model dependence |
|---|---|---|---|---|
| Acute insulin-sensitivity fall at realistic dose (~10–11% clamp; HOMA-IR +0.27–0.30) | **B** (5–9 trials) | **A** (T1 dominant) | **C** (one adolescent trial, and it was null) | **C** (varies >2× by measurement method) |
| Recovery time constant (days-to-weeks; >2 nights) | **C** (2–4 studies) | **A** (T1) | **B** | **C** (`beals2026` null flips it) |
| Observational T2D RR per hour below 7 h (1.09) | **A** (≥10 studies) | **C** (T5 dominant) | **D — GUESS** (no adolescent cohort exists) | **B** (1.09–1.52 across measures) |
| MR-attenuated causal RR for the subject (~1.02–1.04) | **C** | **B** (T3) | **D — GUESS** (midlife instruments, lifelong exposure) | **C** |
| Long sleep as independent risk | **B** | **B** | **C** | **D — GUESS** (sign flips: RR 1.14–1.48 observational vs OR 0.80 MR) |

Per `gates.md`, anything graded **D** on transportability or model dependence must be labelled a
**GUESS** in the report body. That applies to **both** long-run risk numbers and to the long-sleep
arm. The acute, reversible findings are the only part of this shard's evidence that is
adolescent-relevant, experimentally grounded, and safe to state without that label.

## The single biggest gap

**There is no prospective cohort — and no trial of more than 7 days — that measures objective sleep
and glycaemic outcomes in 16–19-year-olds.** Everything long-run is midlife extrapolation; everything
adolescent is either 3–7 nights of lab restriction or cross-sectional. The bridge from "his insulin
sensitivity is measurably worse" to "his diabetes risk moved" is therefore **not** empirically
observed at his age — it is an assumption the downstream model must make explicitly and carry wide
uncertainty on.
