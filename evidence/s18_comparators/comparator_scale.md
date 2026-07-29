# Calibration anchors: what 3 years of a lifestyle exposure beginning at age 16 costs

Shard `s18_comparators`. Purpose: give the modeller a commensurable scale on which
"3 years of adolescent sleep restriction" can be ranked against other common lifestyle
exposures **of the same duration, at the same age, in the same sex**.

Units follow `spec/gates.md`: **life expectancy in months**, years in parentheses.
Sign convention: all figures below are life expectancy **lost**, reported as positive
magnitudes of loss.

Life table: `data/lifetable_us_male_full.csv` (US males 2023, NCHS NVSR 74-6, built and
G10-calibrated by shard `s17_baseline_risk`). Key quantities used throughout:
`e(16) = 60.51 y`, `e(19) = 57.66 y`, `e(30) = 47.54 y`, `e(40) = 38.64 y`, `e(46) = 33.40 y`.

All arithmetic is reproducible: `python3 convert.py` and `python3 comparator_table.py`.

---

## 0. READ THIS FIRST: the number that governs everything

**P(death between exact age 16 and exact age 19) for a US male is 0.00248, i.e. 248 per
100,000.**

Adolescent mortality is minuscule. Consequently, **if an exposure only raises the hazard
while it is happening, then 3 years of it at ages 16-19 costs almost nothing in life
expectancy, no matter how large the hazard ratio.** Tripling the hazard for those three
years costs 107 days. Raising it 20% costs 11 days.

Every published comparator figure in the literature (10 years for smoking, 3 years for
overweight, 4-5 years for heavy drinking) is for a hazard **sustained for the rest of
life**. The entire quantitative content of this shard is the conversion between those two
things, and **the conversion, not the underlying epidemiology, is where all the
uncertainty lives.** The bounds below span a factor of 100-4000 per comparator. Anyone
who reports a single number here without stating the conversion assumption is reporting an
artefact of that assumption.

---

## 1. THE TABLE

Loss of life expectancy from **3 years of exposure beginning at age 16, in a male**, then
cessation.

**Table 1A is the one to read.** It is self-contained: for every comparator it gives the
defensible central estimate, an interval, the reversibility on cessation at 19, and the
exact conversion assumption used to get there. Table 1B then shows how much of each central
estimate is assumption rather than epidemiology, by exposing the two bounds.

### Table 1A — the modeller table

| Comparator | Exposure priced | **LE lost, central** | 80% interval | Reversibility on cessation at 19 | Conversion assumption used |
|---|---|---|---|---|---|
| Smoking, 20 cig/day | 20 cigarettes/day, ages 16-19, then permanent cessation | **1.8 mo** (0.15 y) | 0.6-9.0 mo | **HIGH but incomplete.** Quit at 25-34 leaves all-cause RR 1.05 (1.00-1.11); cessation before 40 removes ~90% of excess. Residual is CUMULATIVE in pack-years (lung-cancer RR still 1.84). | Model P, then scaled **down ~9x** onto the pirie2013 cessation gradient, because smoking hazard is super-linear in duration and pro-rata gives no credit for post-cessation repair. Interval spans cessation-calibrated (low) to full un-discounted Model P (high). |
| Smoking, 10 cig/day | 10 cigarettes/day, ages 16-19, then permanent cessation | **1.0 mo** (0.08 y) | 0.4-4.4 mo | as 20 cig/day: **HIGH but incomplete**, residual cumulative in pack-years. | as 20 cig/day. Dose enters through jackson2025's per-cigarette route, so this row is the 20/day row at half the log-hazard. |
| Overweight, BMI 27.5 vs 22.5 | +5 kg/m2 above optimum for 3 years, ages 16-19, then return to 22.5 | **1.8 mo** (0.15 y) | 0.4-3.0 mo | **PARTIAL, poor in practice.** Metabolic risk reverses on weight loss, but BMI at 30-49 predicts mortality at 50-69 *after adjusting for* BMI at 50-69 (peeters2003), and adolescent adiposity tracks into midlife (twig2016, zheng2017). | Model P at face value (published loss / e(40), x3). Not discounted for reversibility, because the tracking evidence says a 3-year adolescent exposure is usually the start of a trajectory, not a closed window. |
| Obesity grade 1, BMI ~32 | BMI 30-35 for 3 years, ages 16-19, then return to 22.5 | **2.4 mo** (0.20 y) | 0.8-3.2 mo | As overweight, but **worse**: grade-1 obesity present at 18 very rarely resolves, so the closed-window assumption is least credible here. | Model P at face value (psc2009 midpoint 3 y over e(46), x3), undiscounted. The interval's low end is Bound L. |
| Physical inactivity | 0 MET-h/wk leisure activity for 3 years, ages 16-19, then meeting guidelines | **0.8 mo** (0.07 y) | 0.2-3.1 mo | **HIGH** (best-evidenced after smoking). Becoming more active cuts mortality independent of baseline (HR 0.76 per 1 kJ/kg/day/y); rising trajectories beat consistent inactivity even from the lowest baseline. Fitness is a state variable. | Model P **pulled down to just above Bound L**, because high reversibility means a closed 3-year window forfeits little. Interval's high end retains undiscounted Model P for a modeller who rejects that discount. |
| Alcohol, ~200-350 g/wk | 14-25 US standard drinks/week for 3 years, ages 16-19, then moderation | **3.0 mo** (0.25 y) | 1.4-4.2 mo | **SPLIT, and structurally unlike every other row.** Chronic channel (BP, liver, cardiac) largely reversible. Acute injury channel is not reversible but is *resolved inside the window*, so ex ante and ex post loss diverge here alone. | **ADDITIVE, the only row not using a single model**: Bound L injury-window term (from the gbd2016alcohol PAF for males 15-49) PLUS the Model P chronic term. This is why the central estimate exceeds Model P. The window HR of 2.0 is an assumption, not an extraction. |
| Typical Western diet | typical Western vs longevity-optimal diet for 3 years, ages 16-19, then optimal | **1.8 mo** (0.15 y) | 0.1-3.8 mo | **HIGHEST of all comparators, and the source quantifies it itself.** Switching at 60 still gains 8.8 y (6.8-10.0) of the 13.0 y available at 20 - 68% still on the table 40 years later; 3.4 y even at 80. | Model P computed from fadnes2022's **own delayed-cessation gradient** (13.0 y at 20 minus 8.8 y at 60 = 4.2 y spread over 40 exposure-years), not naive pro-rata over e(20), which would give 0.69 y. Their gradient shows marginal cost per bad-diet year RISES with age, so even the high end overstates ages 16-19. |
| REFERENCE: insufficient sleep | short habitual sleep for 3 years, ages 16-19 (this project's own exposure) | **1.2 mo** (0.10 y) | 0.2-3.6 mo | **NOT ESTABLISHED** on the mortality scale by any record in this shard. No sleep study reports a cessation gradient analogous to pirie2013. This is the single biggest asymmetry between our exposure and its comparators. | Model P over e(40), undiscounted **because no cessation evidence exists to discount it with**. Interval deliberately wide: Bound L (cappuccio2010 RR 1.12 across the window) to li2024sleep's 4.7 y pro-rated over e(30). Both published inputs are SUSTAINED midlife exposure. |

### Table 1B — how much of that is assumption

Same central estimates and intervals, now beside the bounds they were drawn from. Read the
bold column; read the two bound columns to see how much of it is assumption.

| Comparator | **RECOMMENDED central (months)** | 80% interval (months) | Bound L: window only | Model P: pro-rata | Model P as permanent HR from age 19 | Bound U: full HR permanent |
|---|---|---|---|---|---|---|
| Smoking, 20 cig/day | **1.8 mo** | 0.6-9.0 mo | 0.04 mo (1 d) | 8.4 mo | 1.0621 | 168 mo (14.0 y) |
| Smoking, 10 cig/day | **1.0 mo** | 0.4-4.4 mo | 0.02 mo (1 d) | 4.2 mo | 1.0387 | 104 mo (8.7 y) |
| Overweight, BMI 27.5 vs 22.5 | **1.8 mo** | 0.4-3.0 mo | 0.35 mo (11 d) | 2.9 mo | 1.0143 | 27 mo (2.3 y) |
| Obesity grade 1, BMI ~32 | **2.4 mo** | 0.8-3.2 mo | 0.79 mo (24 d) | 3.2 mo | 1.0339 | 56 mo (4.6 y) |
| Physical inactivity | **0.8 mo** | 0.2-3.1 mo | 0.61 mo (19 d) | 3.2 mo | 1.0236 | 45 mo (3.7 y) |
| Alcohol, ~200-350 g/wk | **3.0 mo** | 1.4-4.2 mo | 1.76 mo (53 d) | 1.4 mo | 1.0108 | 21 mo (1.7 y) |
| Typical Western diet | **1.8 mo** | 0.1-3.8 mo | 0.09 mo (3 d) | 3.8 mo | 1.0209 | 41 mo (3.4 y) |
| REFERENCE: insufficient sleep | **1.2 mo** | 0.2-3.6 mo | 0.21 mo (6 d) | 1.1 mo | 1.0088 | 17 mo (1.4 y) |

**Column definitions.**

- **Bound L (window only)** — the hazard ratio operates during ages 16, 17 and 18 only,
  then returns to baseline. This is the correct model if the exposure's harm is a
  *contemporaneous physiological state* that resolves completely on cessation. It is the
  floor.
- **Model P (pro-rata cumulative dose)** — the published life-expectancy loss for
  *sustained* exposure is divided by the number of exposure-years the published estimate
  spans, and multiplied by 3. This is the correct model if harm accumulates as an
  irreversible dose. It is my recommended *structural* model, and the column beside it
  re-expresses it as a single **permanent hazard ratio applied from age 19** so the
  modeller can plug it straight into a life table (see §2).
- **Bound U (full HR permanent)** — the *entire* sustained-exposure hazard ratio applied
  permanently from age 19. This is the published headline figure. **It is not defensible
  for a 3-year exposure** and is shown only because the task asked for both bounds and
  because it is what a careless reading of the source papers produces.
- **RECOMMENDED central** — Model P, adjusted down where the comparator has direct
  empirical evidence of post-cessation recovery (smoking, physical inactivity, diet), and
  adjusted *up* where the comparator has a hazard channel concentrated inside the 16-19
  window that pro-rating from midlife misses entirely (alcohol). Per-comparator
  justification in §3.

**The headline ranking.** On a fair 3-years-at-16-19 basis, all of these exposures land in
the same narrow band of roughly **1 to 3 months** of life expectancy. The 10-year, 4-year
and 3-year figures that dominate public discussion of smoking, alcohol and obesity are
figures for *decades* of exposure and do not survive conversion to a 3-year adolescent
window. Alcohol ranks worst, and it ranks worst for a reason that has nothing to do with
chronic disease (§3.4).

---

## 2. The conversion assumption I recommend, and why

### 2.1 The two models, stated precisely

Let \(q_a\) be the baseline probability of dying between exact ages \(a\) and \(a+1\).

**Model W (window / fully reversible).** \(q_a \to \text{HR} \cdot q_a\) for
\(a \in \{16, 17, 18\}\), unchanged thereafter.

**Model P (pro-rata cumulative dose).** The published loss \(L_{\text{pub}}\), earned over
\(E\) exposure-years, is attributed equally per exposure-year:
\[
L_3 = L_{\text{pub}} \cdot \frac{3}{E}
\]

**Model F (full permanent shift).** \(q_a \to \text{HR}_{\text{pub}} \cdot q_a\) for all
\(a \ge 19\). Equals the published headline figure.

### 2.2 Model P has a clean hazard-ratio form, which is what the modeller should use

In this life table, years of life lost is almost exactly linear in the log of a hazard
ratio sustained from a fixed age. Applying HR from age 40 for life:

| HR | YLL at 40 | YLL / ln(HR) |
|---|---|---|
| 1.12 | 1.229 y | 10.85 |
| 1.29 | 2.763 y | 10.85 |
| 1.45 | 4.033 y | 10.85 |
| 2.00 | 7.520 y | 10.85 |
| 2.96 | 11.725 y | 10.80 |

So **YLL ≈ 10.85 × ln(HR)** across the whole plausible range. That linearity means
pro-rating a published life-expectancy loss by \(3/E\) is *equivalent* to applying a
permanent hazard ratio of
\[
\text{HR}_{\text{perm}} = \text{HR}_{\text{pub}}^{\,3/E}
\]
from the end of exposure. Those are the values in the "Model P as permanent HR from age
19" column, and they are the modeller-ready form: they are single numbers that can be
multiplied into \(q_a\) for \(a \ge 19\) and composed multiplicatively with other
exposures. They are all between 1.009 and 1.062.

### 2.3 Recommendation

**Use Model P as the structural default, expressed as the permanent hazard ratio
\(\text{HR}_{\text{pub}}^{3/E}\) applied from age 19. Then move the central estimate
toward Bound L in proportion to the strength of the comparator's post-cessation recovery
evidence, and add a separate within-window term for any comparator whose hazard is
concentrated at ages 16-24.**

Reasons Model P rather than Model W as the default:

1. **It is the only model that respects dose.** Model W makes 3 years of a 40-year habit
   nearly free, which contradicts the entire pack-year literature.
2. **It matches the one published per-unit-exposure estimate we have.** Jackson 2025
   independently derives 17 minutes of life expectancy lost per cigarette for men, purely
   by dividing a lifetime deficit by a lifetime cigarette count. Model P at 20 cig/day
   reproduces 8.4 months for 3 years; the per-cigarette route gives 8.5 months. Those are
   the same calculation, and it is the calculation a published source actually endorses.
3. **It degrades gracefully.** As \(E \to\) the full remaining lifespan, Model P converges
   to Model F; as \(3/E \to 0\) it converges to no effect.

Reasons **not** to use Model P uncorrected:

1. **It assumes harm is linear in exposure-years.** For smoking this is known to be false:
   hazard is strongly super-linear in *duration*, so the first 3 years of a career
   contribute far less than 3/54 of the total. Model P over-charges early exposure.
2. **It gives no credit for repair.** The empirical cessation data (§3.1) show that
   stopping young recovers most of the loss. For smoking, Model P and the
   cessation-calibrated estimate differ by a factor of ~9.
3. **It misses front-loaded acute hazards.** Pro-rating a midlife chronic-disease estimate
   discards the injury mortality that dominates alcohol harm at exactly our subject's age.

### 2.4 Calibration of the life-table engine (a 20% correction)

The raw `10.85 × ln(HR)` rule runs **hot** relative to the published literature. Applying
each source's own HR from age 40 and comparing with that source's own published years:

| Anchor | HR | computed | published | ratio |
|---|---|---|---|---|
| `banks2015` current smoker vs never | 2.96 | 11.73 y | 10 y | 1.17 |
| `psc2009` BMI 40-45 | 2.76 | 10.98 y | 8-10 y | 1.22 |
| `psc2009` BMI 30-35 | 1.45 | 4.03 y | 2-4 y | 1.34 |
| `wood2018` >350 g/wk | 1.514 | 4.50 y | 4-5 y | 1.00 |
| `li2018lifestyle` 5 vs 0 factors, men | 3.85 | 14.6 y | 12.2 y | 1.20 |

Mean overshoot ≈ 18-20%. It arises because the published figures apply their hazard from
later ages, allow attenuation of the hazard ratio with age, and handle competing risks.
**Either use the published years directly and pro-rate them (what I did in the table), or
multiply life-table-derived YLL by 0.80.** Do not mix the two.

---

## 3. Per-comparator detail, reversibility, and the assumption used

### 3.1 Smoking — the benchmark for stopping an exposure young

| | |
|---|---|
| Sustained-exposure anchor | **10 years** LE lost for continuing smokers. Replicated three times independently: `doll2004` (UK male doctors, 50 y follow-up), `jha2013` (US NHIS, "more than 10 years"), `banks2015` (Australian 45 and Up, "an average of 10 years earlier"). `pirie2013` gives 11 years for women. |
| Hazard ratio | 2.96 (2.69-3.25) all-cause, `banks2015`; 2.8 (99% CI 2.4-3.1) for men, `jha2013`; 2.97 (2.88-3.07), `pirie2013`. |
| Dose | `banks2015`: ~2-fold at ≤14/day (mean 10/day), ~4-fold at ≥25/day. Log-hazard is roughly linear in cigarettes/day over this range. |
| Per unit exposure | `jackson2025`: **17 minutes per cigarette for men** (22 for women, 20 sex-averaged). Equivalently, at 10 cig/day, "*By the end of the year, they could have avoided losing 50 days of life*". |
| Model P, 3 years | 8.4 months at 20/day; 4.2 months at 10/day. Matches the per-cigarette route to within 1%. |
| **Reversibility** | **HIGH but INCOMPLETE, and this is the best-evidenced reversibility of any comparator in this shard.** `doll2004`: cessation at 30 gains ~10 of the ~10 years. `jha2013`: quitting at 25-34 gains ~10 years, and "*Cessation before the age of 40 years reduces the risk of death associated with continued smoking by about 90%*". `pirie2013`: quitting at 25-34 leaves all-cause RR **1.05 (1.00-1.11)** — 3% of the excess of a continuing smoker — and "*stopping before age 30 years avoids more than 97% of it*". `banks2015`: those quitting before 45 did not differ significantly from never-smokers. |
| **Irreversible residue** | Real but small on the all-cause scale. `pirie2013`'s quit-at-25-34 group still had lung-cancer RR 1.84 (1.45-2.34). Smoking is the clearest **cumulative pack-year** exposure in the set. |
| Conversion used | Model P, then moved to the **low** end. Pro-rata gives 8.4 months; the cessation evidence gives ~1 month (3% of an 11-year deficit is 0.33 y for a ~13-year career, so ~0.08 y for 3 years). Central **1.8 months**, interval **0.6-9.0 months**. |

**The ~9x disagreement between these two routes is the single most important finding in
this shard.** Pro-rata says a 3-year adolescent smoking habit costs 8 months. The observed
mortality of people who actually did smoke young and then quit says it costs about 1
month. The truth is nearer the second, for two reasons that reinforce each other: smoking
hazard is super-linear in duration (so early years are cheap), and cessation permits
repair. I have carried the pro-rata figure as the upper bound rather than the central
estimate for exactly this reason.

### 3.2 Body mass index

| | |
|---|---|
| Per-unit anchor | **HR 1.29 (1.27-1.32) per +5 kg/m²** above 22.5-25, `psc2009`. `globalbmi2016` (never-smokers only, best confounding control): 1.29 (1.26-1.32) North America, 1.39 (1.34-1.43) Europe. |
| Category HRs | `globalbmi2016`: BMI 25-27.5 → 1.07; 27.5-30 → **1.20 (1.18-1.22)**; 30-35 → **1.45 (1.41-1.48)**; 35-40 → 1.94; 40-60 → 2.76. |
| Published YLL | `psc2009`: **2-4 years** at BMI 30-35, **8-10 years** at BMI 40-45 ("*comparable with the effects of smoking*"). `peeters2003`: 40-year-old male nonsmokers lost **3.1 years** from overweight, **5.8 years** from obesity. `fontaine2003`: max **13 years** for white men aged **20-30** with BMI >45. |
| Age transport | Favourable, unusually. `globalbmi2016`: the HR per 5 kg/m² is **1.52 (1.47-1.56)** when BMI is measured at 35-49 versus 1.21 at 70-89, and **1.51** in men versus 1.30 in women. `fontaine2003`: "*For any given degree of overweight, younger adults generally had greater YLL than did older adults.*" **Using the pooled 1.29 for an 18-year-old male is therefore conservative.** |
| **Reversibility** | **PARTIAL, and in practice poor.** Metabolic risk largely reverses on weight loss, but two findings cut against treating a 3-year adolescent exposure as a closed window: (a) `peeters2003` — "*Body mass index at ages 30 to 49 years predicted mortality after ages 50 to 69 years, even after adjustment for body mass index at age 50 to 69 years*"; (b) adolescent adiposity tracks strongly into midlife (`zheng2017`; `twig2016` HR 3.5 for CV death from BMI measured at mean age 17.3, rising to 4.1 at 30-40 years of follow-up). |
| Conversion used | Model P off `peeters2003`'s 3.1 y over `e(40)` = 38.6 exposure-years → 2.9 months, discounted for partial reversibility. Overweight central **1.8 months** (0.4-3.0); obesity grade 1 central **2.4 months** (0.8-3.2). |

`twig2016` deserves a specific warning. It is the only record in this shard whose exposure
is measured at exactly our subject's age (mean 17.3 y, n = 2.3 million, measured not
self-reported), and its hazard ratios *rise* with follow-up length, which is what
cumulative damage looks like. Applied permanently from 19, HR 3.5 would be 16 years of
life expectancy. **That is an over-attribution and must not be used**: BMI was measured
once, no adult BMI was available, and adolescent BMI tracks into midlife, so the hazard
ratio prices a lifelong adiposity trajectory that merely *starts* in adolescence.

### 3.3 Physical inactivity

| | |
|---|---|
| Individual anchor | `moore2012` (654,827 pooled): life expectancy gain after age 40 versus 0 MET-h/wk is **1.8 y (1.6-2.0)** at 0.1-3.74 MET-h/wk, **3.4 y (3.2-3.5)** at 7.5-14.9 MET-h/wk (the WHO guideline level), **4.5 y (4.3-4.7)** at 22.5+ MET-h/wk. Dose-response is steeply concave: half the benefit arrives at a trivial dose. |
| Population anchor | `lee2012`: eliminating inactivity worldwide would raise population LE by **0.68 y (0.41-0.95)**, and inactivity accounts for 9% (5.1-12.5) of premature mortality. `katzmarzyk2012`: 2.00 y (1.39-2.69) from cutting US sitting below 3 h/day. **Both are population counterfactuals and are routinely misquoted as individual effects — do not use them as comparators.** |
| Device-measured | `ekelund2019`: HR **0.27 (0.23-0.32)** most vs least active accelerometer quartile, i.e. an implied inactive-vs-active HR of 3.7. **Outlier, not used.** Mean age 62.6 y, 73% women, 5.8 y median follow-up: low measured activity in that population is substantially a marker of subclinical disease. Converted naively it would exceed smoking. |
| Age-matched | `hogstrom2016`: aerobic fitness measured by cycle ergometry at mean age **18** in 1,317,713 Swedish conscripts, 29 y follow-up, HR **0.49 (0.47-0.51)** highest vs lowest fifth. Best age match in the shard. Confounded by tracking, and the strongest cause-specific association being death from alcohol and narcotics abuse (HR 0.20) signals that fitness at 18 partly marks a whole behavioural phenotype. |
| **Reversibility** | **HIGH — the best-evidenced reversibility after smoking.** `mok2019` (EPIC-Norfolk, repeated exposure calibrated against heart-rate and movement sensing): each +1 kJ/kg/day/y rise in activity carried HR **0.76 (0.71-0.82)** for all-cause mortality *adjusted for baseline activity*, and increasing trajectories beat consistent inactivity even from the lowest baseline (HR 0.76, 0.65-0.88). Fitness is a state variable restored within months of resuming training. |
| Conversion used | Model P off `moore2012` gives 3.2 months, but reversibility is high, so I place the central estimate near Bound L. Central **0.8 months**, interval **0.2-3.1 months**. |

Note the asymmetry with smoking: for smoking we have direct evidence on quitting *young*
(`pirie2013`, quit at 25-34); for inactivity all the reversibility evidence is from people
aged 40-79. Extrapolating it to a 19-year-old is conservative — recovery should be easier
at 19 — but it is an extrapolation.

### 3.4 Alcohol — the one comparator where the window model dominates

| | |
|---|---|
| Chronic anchor | `wood2018` (599,912 current drinkers, 83 studies, intake corrected for long-term variability using 152,640 repeat assessments): relative to >0-≤100 g/wk, lower life expectancy **at age 40** of approximately **6 months** at 100-200 g/wk, **1-2 years** at 200-350 g/wk, **4-5 years** at >350 g/wk. Per-unit: stroke HR **1.14 (1.10-1.17)** per +100 g/wk. |
| Model P, 3 years | 0.5 months at 100-200 g/wk; **1.4 months** at 200-350 g/wk; 4.2 months at >350 g/wk. |
| **The channel `wood2018` misses** | `gbd2016alcohol`: "*Among the population aged 15-49 years, alcohol use was the leading risk factor globally in 2016, with ... 12.2% (10.8-13.6) of male deaths attributable to alcohol use*", and the leading attributable causes in that band are tuberculosis, **road injuries** and **self-harm**. `wood2018` studies chronic disease in middle-aged and older adults and captures essentially none of this. |
| Window term | The 12.2% PAF implies a population-average hazard ratio over the window of 1/(1-0.122) = 1.139, which costs **7.4 days** for an *average* male. For an individual heavy drinker the hazard ratio is several-fold higher: HR 1.5 → 27 days, HR 2.0 → **53 days**, HR 2.5 → 80 days, HR 3.0 → 107 days. **The HR of 2.0 I use for the central estimate is an assumption, not an extraction** — see the caveat below. |
| **Reversibility** | **SPLIT, and structurally unlike every other comparator.** The chronic channel (blood pressure, hepatic, cardiac remodelling) is largely reversible. The acute injury channel is *not* reversible but is **resolved inside the window**: it is a mortality lottery, so conditional on surviving to 19 unharmed, almost none of it is carried forward. Ex ante expected loss and ex post realised loss therefore diverge sharply for alcohol and for nothing else here. |
| Conversion used | Model P **plus** a window term, because the two channels are additive and act at different times. Central **3.0 months**, interval **1.4-4.2 months**. |

**Caveat, flagged for the confidence ledger.** The individual-level hazard ratio for injury
death in a heavy-drinking 16-19 year old male versus a light-drinking one is *not* an
extraction from any record in this shard. `gbd2016alcohol` gives a population attributable
fraction, from which an individual hazard ratio cannot be recovered without the exposure
prevalence. The 7.4-day population-average figure **is** derivable and defensible; the
53-day figure at HR 2.0 is a modelling assumption. Per `spec/gates.md` this makes the
alcohol central estimate **grade D on model dependence, i.e. a GUESS**, and it is the one
cell in the table I would most like a dedicated shard to replace.

### 3.5 Diet

| | |
|---|---|
| Anchor | `fadnes2022` (Food4HealthyLife, GBD 2019 + food-group meta-analyses, life-table): sustained change from a typical Western diet to the optimal diet **from age 20** would raise LE by **13.0 y (95% UI 9.4-14.3)** for US men. The more realistic "feasibility approach" diet gives **7.3 y (4.7-9.5)**. `fadnes2024` adds adjustment for height, weight and physical activity and gets 9.7 y (8.1-11.3) for US men at 40 — the estimate barely moved, which is modest reassurance against confounding by adiposity and activity. |
| Burden framing | `gbd2017diet`: 11 million (10-12) deaths and 255 million (234-274) DALYs attributable to dietary risks in 2017. Aggregate; not convertible to a per-person 3-year figure. |
| **Reversibility** | **HIGHEST of all comparators, and the source quantifies it itself.** `fadnes2022`: switching at 60 still gains **8.8 y (6.8-10.0)** of the 13.0 y available at 20 — 68% of the benefit is still on the table 40 years later — and even at 80, 3.4 y remains. A 3-year bad-diet window closed at 19 forfeits almost nothing in that model. |
| Conversion used | The authors' **own delayed-cessation gradient**, not naive pro-rata: eating badly from 20 to 60 (40 exposure-years) forfeits 13.0 − 8.8 = 4.2 y, i.e. 0.105 y per exposure-year, so 3 years = **3.8 months**. Naive pro-rata over `e(20)` = 56.7 would give 8.3 months. The 60→80 segment gives 0.27 y per exposure-year, so the marginal cost of a bad-diet year **rises steeply with age** and 3.8 months overstates ages 16-19. Central **1.8 months**, interval **0.1-3.8 months**. |

**Distrust the 13-year headline.** It is the largest single-exposure life-expectancy claim
in this shard, larger than smoking, and it is produced by summing food-group effects
estimated from *separate* observational meta-analyses, which risks double-counting shared
causal pathways. `li2018lifestyle` caps *all five* of these behaviours combined at 12.2 y
(10.1-14.2) for men at age 50. A single-exposure estimate that exceeds the five-exposure
joint estimate is internally inconsistent, and diet's is the one that does.

### 3.6 Insufficient sleep on this same scale — the answer is mostly negative

This was task item 6. What exists:

- **`hafner2016` (RAND Europe RR-1791) does not put sleep on a life-expectancy or QALY
  scale at all.** It prices lost **GDP** and lost **working days**: "up to $411 billion a
  year", 1.56-2.28% of US GDP, "about 1.23 million working days". Its only health input is
  a **borrowed** mortality relative risk — "*An individual that sleeps on average less
  than six hours per night has a ten per cent higher mortality risk than someone sleeping
  between seven and nine hours. An individual sleeping between six to seven hours per day
  still has a four per cent higher mortality risk*" — taken from the observational
  short-sleep literature, i.e. essentially `cappuccio2010`'s RR 1.12. **Do not pool RAND
  with `cappuccio2010`: that double-counts.** Nothing in RAND is commensurable with years
  of life.
- **There is no GBD estimate for sleep.** `welter2026`: "*Despite this considerable
  burden, sleep disorders have been absent from GBD publications since the 2004 update.
  They are currently neither included as primary disorders nor as risk factors.*" GBD
  supplies quotable DALY figures for diet, alcohol, physical inactivity and high BMI, and
  **none for sleep**. Any DALY-space comparison of our subject's exposure against the
  others is therefore impossible from GBD and must go through life expectancy. A report
  that cites a GBD sleep DALY figure has invented it.
- **The closest genuine sleep life-expectancy estimate is `li2024sleep`**: life expectancy
  at age 30 was **4.7 y (2.7-6.7) greater for men** with 5 versus 0-1 low-risk sleep
  factors (all-cause HR 0.70, 0.63-0.77). Two cautions: the exposure is a five-item
  *phenotype* (duration, sleep-onset difficulty, sleep-maintenance difficulty, medication
  use, daytime sleepiness) measured once at mean age 47, not 3 years of adolescent
  restriction; and median follow-up is only 4.3 years while the outcome is life expectancy
  at 30, so the figure is a long extrapolation from a parametric survival model and its
  interval understates the true uncertainty.
- **I found no published QALY estimate for insufficient sleep** on a per-person,
  per-unit-exposure basis. Searches for sleep-QALY and sleep-cost-effectiveness returned
  only disease-specific work (chronic kidney disease, periodontitis).

Placed on the identical footing as the comparators: sustained short sleep is worth
**1.2 months (0.2-3.6)** for 3 years at ages 16-19 — low end from `cappuccio2010`'s RR
1.12 over the window, high end from `li2024sleep` pro-rated over `e(30)` = 47.5. That puts
our own exposure **in the same band as, and slightly below, every comparator in the
table.**

---

## 4. Which comparators are cumulative and irreversible, and which are not

Ranked by how much of the damage from a 3-year adolescent exposure the subject is stuck
with after cessation.

| Comparator | Cumulative irreversible damage? | Evidence | Implication for the conversion |
|---|---|---|---|
| **Smoking** | **Yes, most clearly of any comparator.** Pack-years is a real cumulative dose; `pirie2013` shows lung-cancer RR 1.84 persisting after quitting at 25-34. But the all-cause residue after young cessation is only ~3-5% of the excess. | `doll2004`, `jha2013`, `pirie2013`, `banks2015` — four independent cessation gradients | Model P is structurally right, but must be discounted heavily for young cessation. |
| **BMI** | **Partly.** `peeters2003`: early-adult BMI predicts later mortality after adjustment for later BMI. The bigger problem is not irreversibility but **tracking** — adolescent adiposity usually is not reversed (`zheng2017`, `twig2016`). | `peeters2003` (qualitative only), `twig2016`, `zheng2017` | Model P, lightly discounted. Flag that "3 years then cessation" may be a counterfactual that rarely occurs. |
| **Alcohol** | **Chronic channel: no. Acute channel: irreversible but resolved inside the window.** | `wood2018`, `gbd2016alcohol` | Model P **plus** a window term. Unique structure. |
| **Physical inactivity** | **Largely no.** Fitness is a state variable. `mok2019`: becoming active helps regardless of baseline. | `mok2019` (ages 40-79 only) | Move the central estimate toward Bound L. |
| **Diet** | **Least of all.** `fadnes2022`'s own age gradient leaves 68% of the age-20 benefit available at 60. | `fadnes2022` | Use the delayed-cessation gradient, not pro-rata. Central near Bound L. |
| **Insufficient sleep (ours)** | **Unknown.** No record in this shard establishes a cessation gradient for sleep on the mortality scale. | none | **This is the biggest gap.** See `station_report.md` §4. |

---

## 5. How to use this in the report, and how not to

**Do:**

- Quote the recommended central column with its interval, and name the conversion
  assumption in the same sentence.
- Use the "Model P as permanent HR from age 19" column if you need to compose exposures
  multiplicatively inside a life table. Those hazard ratios are all 1.009-1.062.
- State that all comparators, fairly converted, land in a 1-3 month band. That is the
  headline calibration result and it is far more informative than any single number.

**Do not:**

- Compare "3 years of short sleep" against the *published* 10-year smoking figure, the
  4-5-year heavy-drinking figure, or the 13-year diet figure. Those are decades-long
  exposures. This is the specific error the shard exists to prevent.
- Quote `lee2012`'s 0.68 y or `katzmarzyk2012`'s 2.00 y as individual effects. They are
  population counterfactuals.
- Quote `ekelund2019`'s HR 0.27 as a causal inactivity effect. It is inflated by reverse
  causation in a cohort of mean age 62.6 with 5.8 years of follow-up.
- Cite a GBD figure for sleep. There is none (`welter2026`).
- Treat the alcohol central estimate as an extraction. Its window term rests on an assumed
  hazard ratio and is a **GUESS** under `spec/gates.md`.
