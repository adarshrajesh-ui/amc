# The drowsy-driving mortality channel, ages 16-19

**Shard `s21_drowsy_driving`. Every number below is reproduced by `calc.py` in this directory; run it to
check the arithmetic. Every input is sourced to a YAML record in this directory, and every YAML record
carries the verbatim quote that supports its numbers.**

---

## 0. The answer first

| Quantity | Value |
|---|---|
| **Excess probability of death from a drowsy-driving crash, ages 16-18 (3 y), conditional on being a typical licensed US male teenage driver** | **4.7 × 10⁻⁵ (about 1 in 21,000)** |
| **Expected life expectancy lost through this channel** | **0.03 months ≈ 0.9 days** |
| Plausible range | **0.01 – 0.14 months** |
| Extreme bounds (all four inputs simultaneously extreme) | 0.004 – 0.21 months |
| **Same figure if the subject does not drive at all** | **exactly 0** |
| **Is it larger than 0.2 months?** | **NO. It is roughly 6-7× SMALLER.** |

**But that comparison is against the wrong number, and the right comparison matters more.** The
"0.2 months" the task refers to is `s13_mortality`'s explicitly labelled *un-discounted ceiling*, not its
estimate. That shard's own central exposure-window figure is **0.006-0.05 months**
(`/workspace/evidence/s13_mortality/mortality_summary.md` §8.4). Against that:

- **This channel is roughly the same size as, and probably larger than, the entire chronic-disease
  exposure-window mortality effect that the project actually estimated.** My 0.03 months sits in the upper
  half of their 0.006-0.05 band, and my range extends well above its top.
- **It does not, however, exceed the 0.2-month ceiling**, and no honest parameterisation of it gets there
  except by pushing four separate inputs to their extremes at once.
- **A de-duplication warning applies before anything is added** — see §9. `s13`'s calculation applied a
  hazard ratio to *all-cause* adolescent mortality, which already contains motor-vehicle deaths.

So the red-team reviewers were right that the channel was missing and wrong about its size. It is real, it
acts during the exposure window rather than fifty years later, it is the single most defensible mortality
term available for this subject — and it is a few hundredths of a month, not a few tenths.

---

## 1. What is being calculated, and what is being conditioned on

**Quantity.** The increase in the probability that this specific subject dies while driving a motor
vehicle during ages 16, 17 and 18, caused by his sleeping ~5.5-6 h on weekdays instead of ~7.5-8 h, where
that increase operates through impaired vigilance and falling asleep at the wheel.

**Three explicit conditionings, all of which materially change the answer.**

1. **CONDITIONAL ON BEING A TYPICAL LICENSED US MALE TEENAGE DRIVER.** We do not know that he drives.
   About 49% of US males aged 16-19 hold a licence (§2). If he does not drive, **this channel is exactly
   zero** — not small, zero — and the report must be able to present both. If he drives materially more
   than average, scale §5 up linearly: a teen driving twice the average mileage gets ~0.06 months.
2. **HIS EXPOSURE IS HABITUAL, NOT ACUTE.** On a typical Tuesday he sleeps his usual 5.5-6 h. He is not
   acutely deprived *relative to his own baseline*. This distinction is worth a factor of ~1.4 and is
   quantified in §4.
3. **ONLY DRIVER DEATHS COUNT.** His own sleep affects crashes in which he is the driver. Deaths as a
   passenger or pedestrian are excluded — they are not his exposure. This is why the denominator in §1 is
   *driver* deaths and not the all-occupant rate the task asked for (both are recorded in
   `iihs2024_fars.yaml`).

---

## 2. STEP 1 — Baseline: how likely is a US male to die as a driver at ages 16-18?

**Source: `iihs2024_fars.yaml`** — IIHS *Fatality Facts 2024: Teenagers*, tabulating FARS, retrieved
directly from iihs.org and stored at `src/iihs2024_teenagers.txt`. Male passenger-vehicle **driver**
deaths per 100,000 population, by single year of age, 2024:

| Age | Driver deaths | Male population | Rate per 100,000/yr |
|---|---|---|---|
| 16 | 123 | 2,322,582 | 5.3 |
| 17 | 175 | 2,326,541 | 7.5 |
| 18 | 242 | 2,296,205 | 10.5 |
| 19 | 313 | 2,282,142 | **13.7 — the highest of any age in the human lifespan, above 85+ males (11.0)** |

Verbatim: *"The rate of deaths per 100,000 people in 2024 peaked at age 19 for male drivers (13.7)"*.

Pooling the three years of the exposure window (16, 17, 18):

```
540 deaths / 6,945,328 person-years = 7.775 per 100,000 per year
3-year cumulative PER-CAPITA probability = 7.775e-5 x 3 = 2.3325e-4
```

The task asked for the all-motor-vehicle rate for males 16-19 and 20-24; from the companion IIHS 2023
page, male passenger-vehicle **occupant** deaths (drivers + passengers) are **14.6 per 100,000** at 16-19
and **17.4 per 100,000** at 20-24, against 7.4 and 7.7 for females. Those are the requested numbers and
are recorded, but they are *not* the denominator here, for the reason in §1.3.

## 3. STEP 2 — Convert per-capita to per-driver

The IIHS rates are per head of population; roughly half of 16-18-year-olds cannot legally drive at all, so
the per-*driver* rate is about double.

**Source: FHWA Highway Statistics 2023, table DL-22**, retrieved from fhwa.dot.gov. Licensed **male**
drivers aged 19-and-under, US total: **4,552,629**. Male population 16-19 (IIHS, above): 9,227,470.

```
L(16-19) = 4,552,629 / 9,227,470 = 0.4934
```

This slightly *overstates* licensure for 16-18 specifically, because the FHWA numerator includes
19-year-olds (the most-licensed year) and because licensure rises steeply with age. FHWA publishes only a
"19 and under" bin, so I cannot compute single-year licensure and have not guessed it. Using L in
0.40-0.49:

| L | 3-year per-driver probability | Odds |
|---|---|---|
| 0.49 | 4.76 × 10⁻⁴ | 1 in 2,101 |
| 0.45 | 5.18 × 10⁻⁴ | 1 in 1,929 |
| 0.40 | 5.83 × 10⁻⁴ | 1 in 1,715 |

**Independent cross-check from a different agency, different vehicle scope, different denominator.**
NHTSA *Young Drivers 2023* (`src/nhtsa2023_young_drivers_813736.txt`) reports **1,695 male young-driver
(15-20) fatalities** in 2023 and **12,106,873 licensed drivers aged 15-20**, of whom ~6.38 M are male
(FHWA male 19-and-under plus one fifth of the male 20-24 bin). That gives **26.6 deaths per 100,000
licensed male young drivers per year**, i.e. 7.97 × 10⁻⁴ over 3 years. It is higher than the IIHS-derived
figure for two identifiable reasons: it includes **all vehicle types** (motorcycles especially) and it
spans **ages 15-20**, which is older and therefore riskier than 16-18.

**Adopted:**

```
P_base = 5.5e-4        (range 4.5e-4 to 8.0e-4)
```

i.e. **about a 1-in-1,800 chance of dying at the wheel during his first three years of driving.** The
range is asymmetric upward because the IIHS route excludes motorcycles.

## 4. STEP 3 — What fraction of his driving-death risk is incurred while sleep-restricted?

This is the step most analyses skip, and skipping it inflates the answer by more than a factor of two.
His sleep restriction is a **school-weekday** phenomenon: weekends and holidays are 7-8 h
(project specification). But teen crash deaths are *not* uniformly distributed across the calendar, and
they are concentrated precisely in the periods when he is **not** exposed.

**Source: `iihs2024_fars.yaml`**, day-of-week and month tables, 2024, all teen (13-19) crash deaths.

*Day of week.* Mon 377 + Tue 353 + Wed 324 + Thu 375 + Fri 419 = **1,848 of 2,899 = 63.7%** of deaths on
Monday-Friday, which is 5/7 = 71.4% of days.

```
per-day risk weight on weekdays = 0.6375 / 0.7143 = 0.8924
```

(Friday counts as exposed: he drives Friday evening on Thursday night's 5.5-6 h.)

*Month.* Jun 300 + Jul 286 + Aug 273 = **859 of 2,899 = 29.6%** of deaths in the three summer months,
which are 25.2% of days. IIHS: *"In 2024, teenage crash deaths peaked in June."*

```
per-day risk weight in the 9 school months = 0.7037 / 0.7479 = 0.9408
```

*Exposed share of the year.* A US school year is ~180 school days: 180/365 = 0.4932.

```
f = 0.4932 x 0.8924 x 0.9408 = 0.4141
```

**So ~41% of his crash-death risk is incurred while sleep-restricted, not 71% and not 100%.** Adopted
**f = 0.41 (range 0.30-0.55)**. The upper end allows for a college schedule in which term-time is longer
and summer break shorter than a high-school calendar.

*One consideration pushing f up, which I have not applied.* 35% of teen crash deaths occur between 21:00
and 03:00 (IIHS time-of-day table: 18% 21:00-midnight, 17% midnight-03:00). Late-evening weekday driving
follows ~16 h of wakefulness on a 5.5-6 h night, so those hours are exposed and are the hours where
drowsiness bites hardest. Against that, much late-night teen driving is Friday and Saturday night, and
Saturday-night driving follows a 7-8 h Friday sleep. The two effects roughly offset and I have left f at
the calendar-based value rather than adjust it in the favourable direction.

## 5. STEP 4 — The risk ratio, and why I use ~1.5 rather than ~2.5

Five estimates, all in the YAML records, ordered from most to least like-for-like with this subject:

| Source | Exposure | Estimate |
|---|---|---|
| `martiniuk2013` (T5, **police-reported** crashes, 19,327 **young drivers** 17-24, Australia) | habitual ≤6 h vs >6 h | **RR 1.21** (1.04-1.41) |
| `gottlieb2018` (T5, prospective, **adjusted for miles driven**) | habitual 6 h vs 7-8 h | **OR 1.33** (no CI published) |
| `gottlieb2018` | per hour less sleep | **OR 1.13** (1.01-1.28) |
| `tefft2016_aaa` (T5, NMVCCS quasi-induced exposure) | **habitual** usual 5-6 h vs ≥7 h | **OR 1.4** (0.5-3.6) — **null** |
| `tefft2016_aaa` / `tefft2018` | **acute** 5-6 h in past 24 h vs ≥7 h | **OR 1.9** (1.3-2.6) |
| `connor2002` (T5, population case-control, injury crashes) | **acute** ≤5 h in past 24 h | **OR 2.7** (1.4-5.4) |
| `bioulac2017` (meta-analysis, 17 studies, 70,098 people) | **sleepiness at the wheel** | **OR 2.51** (1.87-3.39) |

The three **habitual** estimates cluster at **1.21, 1.33, 1.4**. The **acute** estimates and the
at-the-wheel-sleepiness estimates are 1.9-2.7. The subject is a habitual short sleeper who is *not*
acutely deprived relative to his own baseline on a typical school night, so the habitual estimates are the
like-for-like ones. But he *is* chronically below his biological need, which the habitual studies (all in
adults, all with sparse short-sleep cells) may under-capture.

**Adopted RR = 1.5 (range 1.30-2.20; extreme 1.21-2.51).** Note that 1.5 is *above* all three
like-for-like habitual point estimates. Two further considerations, in opposite directions and both
substantial, justify not going higher:

- **UPWARD.** NMVCCS — the dataset behind the best-fitting odds ratios — **excluded every crash between
  midnight and 05:59**, which are the hours where drowsy crashes concentrate. The author says so:
  *"This study may underestimate the risk of driving while sleep-deprived, because data on crashes that
  occurred between midnight and 6 AM were not available."* And `tefft2024_aaa` reports that the drowsy
  share of fatal crashes is **highest among drivers aged 16-20** — though it publishes no number for that
  group, so I could not scale by it.
- **DOWNWARD, AND THIS ONE IS OBJECTIVE.** The only *measured* age breakdown of drowsy crash involvement
  points the other way. `owens2018_aaa` coded PERCLOS eyelid closure by driver age and found drowsiness in
  **8.9% of crashes by 16-19-year-olds (14/158)** against **9.5% overall** and **11.3% at 20-24**, with
  *"Variation by age, sex, and crash severity was not statistically significant (all P > 0.20)."* So in the
  one dataset that watched drivers' eyes rather than reading police narratives, teenagers were **not**
  disproportionately drowsy when they crashed. That does not refute `tefft2024_aaa` — different outcome
  (all crashes vs fatal), different measure (video vs imputed police coding), and 158 crashes is a small
  cell — but it removes any warrant for applying a youth multiplier on top of RR 1.5.
- **DOWNWARD.** Adolescents need ~9 h, so 5.5-6 h is a larger relative deficit for him than for the
  62-year-olds in `gottlieb2018` — but he is also 17, with the fastest reaction times of his life, and the
  expert consensus panel in `czeisler2016` put probable impairment at **3-5 h** and definite unfitness at
  **≤2 h**, both below his routine dose.

## 6. STEP 5 — The causal fraction: how much of this is real?

The task asked me to state how much of the association I think is causal and why. **My answer is
c = 0.5, range 0.25-0.80.** Here is the evidence on both sides, with numbers.

**Arguments that a large majority is confounding (pushing c down):**

- `wheaton2016` (CDC, **50,370 US high-school students**, four national YRBS waves): students sleeping
  ≤7 h on school nights were significantly more likely to **drink and drive**, **ride with a drinking
  driver**, **not wear seatbelts**, and **text while driving**. CDC's own words: *"some of the increased
  risk associated with insufficient sleep might be caused by engaging in injury-related risk behaviors."*
- **The seatbelt pathway is specifically about dying, not about crashing.** Belt non-use does not cause
  crashes; it converts crashes into deaths. So it inflates the *fatal*-crash association — exactly the
  outcome being priced here — without any vigilance mechanism at all.
- `wheaton2016` **fails a negative control**: students sleeping **≥10 h** *also* showed more seatbelt
  non-use, more riding with drinking drivers and more drinking and driving. A U-shape in risk *behaviour*
  is the signature of an unmeasured third factor, not of a dose-dependent physiological effect.
- `tefft2024_aaa`: **20%** of fatal-crash drivers at BAC ≥0.08 were drowsy versus **11%** of sober ones,
  and one third of drowsy fatal-crash drivers had been drinking. Alcohol and drowsiness are entangled at
  both ends. `wheaton2014` replicates the drinking and seatbelt associations in 92,102 US adults.
- `cummings2001` reports that **playing a radio** halved crash risk (aRR 0.6) and drinking coffee halved
  it (0.5). A radio does not halve crash risk. That is residual confounding by driver and trip type in the
  same models that produced the sleep estimates.
- `pizza2010` and `hutchens2008`, on two continents, independently find that **smoking** predicts young-
  driver crashes as strongly as or more strongly than drowsy driving. Smoking has no vigilance mechanism.
  The crash-prone young driver is a bundle, and sleep is one strand.

**Arguments that a substantial part is causal (holding c up):**

- `gottlieb2018` **adjusts for miles driven per year** — the single dominant confounder, worth aRR 2.2 per
  100 miles in `cummings2001` — and the association survives at 1.13 per hour lost, and *strengthens* to
  1.22 among people who do **not** report being sleepy. The latter is important: it means the association
  is not an artefact of sleepy people reporting both exposure and outcome.
- `martiniuk2013` adjusts for hours driven per week, risky driving behaviour, substance use, psychological
  distress, previous crash, remoteness and socio-economic status, and still finds RR 1.21 for ≤6 h, with
  **police-reported** crashes and **prospective** follow-up — no recall bias in the outcome at all.
- The mechanism is directly observed, not inferred: `owens2018_aaa` coded **eyelid closure on video** in
  the three minutes before 701 real crashes and found drowsiness in 9.5%, against `ghsa2026`'s **1.57% of
  baseline driving time**. Eyes closing before crashes is not a self-report artefact.
- `wheaton2014` finds drowsy driving does **not** vary by smoking status in US adults, so the confounding
  is *selective* (alcohol, seatbelts) rather than one undifferentiated "risky person" factor.
- Part of what looks like confounding may be **mediation**: if sleep loss degrades attention and
  self-regulation, then "short sleepers text while driving" is partly a causal consequence of short sleep,
  not a competing explanation. `binhasan2020` found the crash subtype most responsive to a school-start-
  time delay was the **distraction** subtype, which is consistent with that reading.

**And the quasi-experimental evidence, which the task told me not to oversell.** I have not. Five
school-start-time crash analyses point the same direction and disagree by a factor of six on magnitude:

| Record | Design | Implied effect |
|---|---|---|
| `binhasan2020` | pre-post + contemporaneous control, Fairfax County | RR ≈ **1.07**, CI lower bound exactly 1.00 |
| `foss2019` | **ARIMA interrupted time series + 3 matched control counties** | RR ≈ **1.16**, **p = .076, not significant** |
| `danner2008` | county pre-post, Kentucky | RR ≈ 1.17 |
| `vorona2014` | **two-county cross-section, no pre-post** | RR ≈ 1.27-1.29 |
| `vorona2011` | **two-city cross-section, no pre-post** | RR ≈ 1.28-1.41 |

**The two designs with genuine pre-post identification give the two smallest estimates; the two pure
cross-sections give the two largest.** That ordering is what between-place confounding looks like. And
`foss2019`, the only study in the set with real identification, ran the decisive mechanism test and the
drowsiness hypothesis failed it: crashes fell 25% in the 07:00 hour and rose 21% in the 08:00 hour, fell
48% at 14:00 and rose 32% at 15:00 — **crashes moved with the commute rather than disappearing** — and
*"There was no meaningful change in early morning or nighttime crashes, when drowsiness-induced crashes
might have been expected to be most common."* `vorona2014`'s own mechanism test came out **backwards**:
significantly *more* run-off-road-right crashes (their designated "potentially sleep-related" subtype) in
the *late*-start county.

I therefore treat the school-start-time literature as establishing **sign only**, and as actively arguing
against the strong claim that most teen crash risk is sleep-driven. It is the main reason c is 0.5 rather
than 0.9. Two caveats in the other direction, stated fairly: these studies test a **20-45 minute** dose
shift, not the 1.5-2.5 h that separates this subject from a rested sleeper, so a small noisy effect from a
small dose is not evidence against a larger effect from a larger dose; and `foss2019`'s night-time null is
a null over small counts in one county.

## 7. THE ARITHMETIC — three independent routes

### Route 1 — relative risk × exposed fraction × causal fraction

His risk multiplier relative to a fully-rested counterfactual, where only the exposed fraction f carries
the elevated risk RR:

```
M  = f·RR + (1 - f)
AF = (M - 1) / M                          attributable fraction of his observed risk
excess probability = P_base × AF × c
months lost = excess × 58 years × 12 months/year
```

**Central case, every input from the sections above:**

```
M      = 0.41 × 1.50 + 0.59        = 1.2050
AF     = 0.2050 / 1.2050           = 0.1701
excess = 5.5e-4 × 0.1701 × 0.50    = 4.678e-5
months = 4.678e-5 × 58 × 12        = 0.0326 months
```

**Sensitivity on the risk ratio alone** (P, f, c held at central):

| RR used | Source | Months |
|---|---|---|
| 1.21 | `martiniuk2013`, young drivers, police-reported | 0.0152 |
| 1.33 | `gottlieb2018`, 6 h vs 7-8 h | 0.0228 |
| 1.40 | `tefft2016_aaa`, **habitual** 5-6 h (like-for-like) | 0.0270 |
| **1.50** | **adopted** | **0.0326** |
| 1.90 | `tefft2016_aaa`/`tefft2018`, **acute** 5-6 h | 0.0516 |

**Full-range scenarios:**

| Scenario | P_base | f | RR | c | M | AF | Excess | **Months** |
|---|---|---|---|---|---|---|---|---|
| Low | 4.7e-4 | 0.33 | 1.30 | 0.30 | 1.099 | 0.090 | 1.27e-5 | **0.0088** |
| **Central** | **5.5e-4** | **0.41** | **1.50** | **0.50** | **1.205** | **0.170** | **4.68e-5** | **0.0326** |
| High | 7.0e-4 | 0.50 | 2.20 | 0.75 | 1.600 | 0.375 | 1.97e-4 | **0.1370** |
| Extreme low | 4.5e-4 | 0.30 | 1.21 | 0.20 | 1.063 | 0.059 | 5.33e-6 | 0.0037 |
| Extreme high | 8.0e-4 | 0.55 | 2.51 | 0.85 | 1.831 | 0.454 | 3.09e-4 | 0.2147 |

### Route 2 — drowsy share of fatal crashes × share attributable to habitual restriction

Independent of Route 1: instead of a risk ratio, take the measured drowsy fraction of fatal crashes and
ask what part of *his* drowsy-crash risk his habitual restriction is responsible for (as opposed to long
trips, illness, or the circadian nadir, which would affect a rested sleeper too).

```
excess = P_base × (drowsy share of fatal crashes) × (share attributable to habitual restriction)
```

| Drowsy share used | Source | Attributable share | Excess | **Months** |
|---|---|---|---|---|
| **0.176** | **`tefft2024_aaa`, CISS→FARS 2017-2021, 208,727 drivers** | **0.50** | 4.84e-5 | **0.0337** |
| 0.165 | `tefft2012`, fatal crashes, imputed | 0.50 | 4.54e-5 | 0.0316 |
| 0.095 | `owens2018_aaa`, PERCLOS video, all crashes, all ages | 0.50 | 2.61e-5 | 0.0182 |
| 0.0886 | `owens2018_aaa`, PERCLOS video, **drivers aged 16-19 only** (14/158) | 0.50 | 2.44e-5 | 0.0170 |
| 0.070 | `tefft2012`, all crashes, imputed | 0.50 | 1.93e-5 | 0.0134 |
| **0.024** | **`nhtsa_drowsy_counted` — POLICE-REPORTED. FLOOR.** | 0.50 | 6.60e-6 | **0.0046** |
| 0.250 | CDC's *"as many as 7,500 fatal ... (approximately 25%)"* | 0.70 | 1.40e-4 | 0.0974 |

**Route 2 central = 0.034 months, essentially identical to Route 1's 0.033.**

**The order-of-magnitude discrepancy the task asked about, resolved.** NHTSA's counted figures are 1.4% of
all police-reported crashes, 2.0% of injury crashes, 2.4% of fatal crashes (2011-2015), 1.5% of fatal
crashes in 2023, and **633 deaths** in 2023. The research estimates are 7.0%, 13.1%, 16.5-17.6%, and
**5,967-6,326 deaths/year**. The ratio is ~7× on shares and ~10× on deaths — GHSA states flatly:
*"This is ten times more than the raw FARS data reported by NHTSA."* **Four reasons, only the first
statistical, and all four biasing the official figure downward:**

1. **Missing-data coding.** `tefft2012` shows the resolution *inside one dataset*: the drowsiness status
   of **45% of drivers was unknown**; the same data give **3.6%** of fatal crashes when unknown is
   effectively coded not-drowsy and **16.5%** when it is imputed. This is most of the gap. Note that the
   most common reason drowsiness is unknown in a fatal crash is that the driver died alone — and the
   single-occupant run-off-road-at-night crash is the drowsy signature. The residual bias in the
   imputation therefore points *upward*.
2. **There is no breathalyzer for sleep.** *"there is no test analogous to a breathalyzer that the police
   can administer at the roadside"* (`owens2018_aaa`).
3. **The evidence destroys itself.** A drowsy driver is fully awake after the crash, may not recognise he
   was drowsy, and may not volunteer it.
4. **Reporting policy varies by state and locality** (`ghsa2026`).

**Two entirely unrelated methods agree with each other and disagree with the police figure:**
`tefft2012`'s imputation gives 7.0% (4.6-9.3) of all crashes; `owens2018_aaa`'s direct **video of drivers'
eyelids** gives 8.8-9.5%. I therefore use the research-based share and report the police-reported share
only as a floor. **This single choice moves the answer by a factor of 7** (0.034 vs 0.005 months) and is
the largest discrete fork in the calculation.

### Route 3 — mechanistic, from naturalistic driving data only

No self-report, no police coding, no imputation model anywhere in this route.

```
drowsy share of baseline driving TIME   p0 = 0.0157   ghsa2026 / SHRP2 PERCLOS
drowsy share of CRASHES                pc = 0.0950   owens2018_aaa, same study, same coding

implied crash odds ratio for driving in a PERCLOS-drowsy state:
OR = (0.0950/0.9050) / (0.0157/0.9843) = 0.104972 / 0.015950 = 6.58
```

Habitual short sleep raises the *share of driving time spent drowsy*. `owens2019` (431 Fairfax County
high-school drivers) found drowsy-driving prevalence 13.9 percentage points higher at <7 h than at ≥8 h
school-night sleep, on a 47.6% base — a relative increase of ~1.35×.

```
p1 = 0.0157 × 1.35 = 0.0212
M  = (0.0212×6.58 + 0.9788) / (0.0157×6.58 + 0.9843) = 1.1187 / 1.0879 = 1.0282
AF = 0.0274
excess = 5.5e-4 × 0.0274 = 1.51e-5   →   0.0105 months
```

| Drowsy-time multiplier | p1 | M | Months |
|---|---|---|---|
| 1.20× (conservative) | 0.0188 | 1.016 | 0.0061 |
| **1.35× (`owens2019`)** | **0.0212** | **1.028** | **0.0105** |
| 2.00× (aggressive) | 0.0314 | 1.081 | 0.0285 |

**Route 3 gives 0.011 months — three times smaller than Routes 1 and 2 — and I am reporting it rather
than discarding it.** The reason it is smaller is instructive and is a genuine constraint on the whole
channel: **a large per-episode risk (OR 6.6) applied to a small share of driving time (1.6% rising to 2.1%)
produces a small aggregate excess.** Routes 1 and 2 implicitly assume the exposure raises risk across all
of his weekday driving; Route 3 says it raises risk only during the minority of minutes in which his eyes
are actually closing. No causal discount is applied in Route 3 because it contains no confounded
association — only the `owens2019` multiplier is self-reported.

---

## 8. Reconciliation and the honest range

| Route | Basis | Months |
|---|---|---|
| 1 | risk ratio × exposed fraction × causal fraction | 0.033 |
| 2 | drowsy share of fatal crashes × attributable share | 0.034 |
| 3 | naturalistic drowsy-driving time × naturalistic crash OR | 0.011 |

**Central estimate: 0.03 months ≈ 0.9 days of life expectancy.**
**Plausible range: 0.01 – 0.14 months. Extreme bounds: 0.004 – 0.21 months.**

**The uncertainty spans more than an order of magnitude and I am reporting a range rather than a false
point estimate, as instructed.** The span is ~14× across the plausible range and ~58× across the extremes.
Four inputs drive it, in order of contribution:

1. **Drowsy share of fatal crashes: police-reported 2.4% vs research 17.6% (7×).** Resolved in favour of
   the research figures for the reasons in §7, but it is the biggest fork.
2. **Causal fraction: 0.25 to 0.80 (3.2×).** Not resolvable with current evidence. There is no Mendelian
   randomisation and no randomised trial of adolescent sleep duration with a crash outcome.
3. **Risk ratio: 1.21 to 2.51 (2.1×).** Turns almost entirely on whether the subject's habitual
   restriction should be priced with habitual (1.2-1.4) or acute (1.9-2.7) coefficients.
4. **Baseline and licensure: 4.5e-4 to 8.0e-4 (1.8×).** The most tractable of the four; a single FHWA
   table with single-year-of-age licensure would nearly close it.

### Non-fatal serious outcomes (task requirement #5)

The same subject's excess risk of a *non-fatal* drowsy-driving crash is far larger in absolute terms.
Virginia DMV administrative data across three records (`vorona2011`, `vorona2014`, `binhasan2020`) put
police-reported crash involvement for licensed 16-18-year-olds at **29.6 to 71.2 per 1,000 per year**,
central ~45 per 1,000 = 4.5%/yr, so **~13.5% over three years**.

```
crashes involving drowsiness  = 0.135 × 0.09  (owens2018_aaa / tefft2012 all-crash share) ≈ 1.2%
excess attributable to his habitual restriction (× 0.5)                                   ≈ 0.6%
```

So: **an absolute ~1-in-80 chance of a drowsy-involved police-reported crash over the three years, of
which roughly half — ~1 in 160 — is attributable to the sleep restriction.** That is ~130× more likely
than the excess *death*. `tefft2012` shows drowsy crashes are more severe than average (**13.1%** of
hospital-admission crashes vs **7.0%** of all crashes involve a drowsy driver), so the excess
serious-injury count is enriched relative to the excess crash count; I cannot put a number on excess
hospitalisations because I do not hold a teen hospitalisation-per-crash base rate and will not invent one.

---

## 9. Instructions to the downstream model

1. **Present both conditionings.** Typical licensed teenage driver: **0.03 months (0.01-0.14)**.
   Non-driver: **0**. There is no evidence in the project file that this subject drives, and the channel
   is entirely contingent on it. A model that wants one number should weight by the ~49% male 16-19
   licensure rate, giving an unconditional **~0.015 months** — but the conditional presentation is more
   informative.
2. **DE-DUPLICATE AGAINST `s13_mortality` BEFORE ADDING.** `s13`'s exposure-window figure was computed by
   applying a hazard ratio to **all-cause** adolescent mortality (~0.002 over 3 years), which already
   includes motor-vehicle deaths. My per-capita driver-death probability is 2.33e-4, i.e. **11.7% of
   all-cause adolescent male mortality**. So:
   - `s13`'s **0.2-month ceiling** already notionally contains **~0.023 months** of driver-death term.
     My 0.03 months should **replace** that, not add to it — net addition to the ceiling ≈ 0.01 months.
   - `s13`'s **0.006-0.05-month central band** contains only **~0.001-0.006 months** of driver-death term.
     Net addition there is nearly the whole 0.03 months, which **roughly doubles the credible
     exposure-window mortality total.**
3. **Do not double-count within this shard.** `tefft2016_aaa` and `tefft2018` are the **same** 6,845-7,234
   NMVCCS drivers (`cohort_family: NMVCCS_2005_2007`). `vorona2011`, `vorona2014` and `binhasan2020` all
   use Virginia DMV data on 16-18-year-olds with overlapping jurisdictions
   (`cohort_family: Virginia_DMV_SST`); `binhasan2020`'s "rest of Virginia" control **contains** the other
   two studies' treated units. `owens2018_aaa` and `ghsa2026`'s 1.57% figure are both SHRP2
   (`cohort_family: SHRP2_NDS`). `cummings2001` and `connor2002` are both inside `bioulac2017`'s pool.
4. **This channel acts DURING the window, so no residue discount applies.** Unlike the chronic-disease
   channels, there is no "does the effect persist after the exposure ends" question — the deaths either
   happened between 16 and 19 or they did not. That makes this term far better-defined than the
   permanent-residue term `s13` correctly refuses to compute, even though it is small.
5. **The largest single missing input is an age-stratified drowsy share of FATAL crashes.** `tefft2024_aaa`
   states that the drowsy share is **highest at ages 16-20** and publishes no number for that group. If
   that number exists in the full report it would feed Route 2 directly, and it is the highest-value single
   retrieval anyone could add to this shard. Note that the age-stratified evidence I *do* hold cuts the
   other way: `owens2018_aaa`'s PERCLOS video gives **8.9% at ages 16-19 vs 9.5% at all ages**, no
   significant age variation. So the two age breakdowns available disagree in sign, and neither is precise.
   A downstream model should treat the youth adjustment to this channel as **unresolved and centred on
   1.0**, not as a known multiplier above 1.

---

## 10. Direct answer to the question asked

> Is this larger or smaller than 0.2 months, i.e. does it exceed the entire chronic-disease mortality
> estimate the project produced?

**Smaller — by roughly a factor of 6-7 at the central estimate (0.03 vs 0.2 months). It does not exceed
0.2 months under any parameterisation I regard as defensible; only a scenario that simultaneously pushes
the baseline, the exposed fraction, the risk ratio and the causal fraction to their individual extremes
reaches 0.21 months.**

**Three qualifications that matter more than the headline:**

- **0.2 months is `s13`'s un-discounted ceiling, not its estimate.** Against that shard's actual central
  exposure-window figure of **0.006-0.05 months**, this channel is **comparable in size and probably
  larger**, and after de-duplication it roughly **doubles** the project's credible exposure-window
  mortality total.
- **It is much better-founded than the chronic-disease number.** The chronic-disease term rests on
  transporting hazard ratios from 60-year-olds across a 40-year gap with a residue fraction `s13` itself
  grades D and says must carry prior mass at zero. This term rests on a FARS census denominator, three
  independent estimation routes that agree to within a factor of three, and a mechanism directly observed
  on video. It is a small number that we actually know.
- **Neither number is where the damage from this exposure lives.** Both mortality channels are hundredths
  to tenths of a month. If the project's headline is driven by mortality, the project's headline is being
  driven by its smallest and least certain component.
