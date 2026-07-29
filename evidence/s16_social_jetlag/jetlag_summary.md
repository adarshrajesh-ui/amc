# Social jetlag: the subject's exposure, its independent effect, and the weekend catch-up verdict

Shard `s16_social_jetlag`. 81 records screened, 41 included, 111 effect estimates, 42/42 identifier
checks passed against both Crossref and PubMed.

**One-paragraph bottom line.** The subject's social jetlag is about **1.75 h (plausible range
1.0–2.75 h on ordinary weekends, 2.25–3.5 h on his occasional 10–11 h weekends)**. That places him
**at or slightly below the mean for his age** — social jetlag peaks between 2.1 h and 3.3 h at ages
15–16 in the two largest normative datasets, and >80% of adolescents exceed 1 h. **He is not a social
jetlag outlier; he is an outlier in sleep duration.** Misalignment does carry harm independent of
duration — that is established causally, with sleep duration equated to within three minutes — but at
his dose the independent increment is small and lands mostly **below the ~2 h threshold** at which
adolescent depression and academic effects switch on. On weekend catch-up, the protective and harmful
literatures are not actually contradictory: they concern **different outcomes** and, more
importantly, **different exposure definitions**. Net position for this subject: weekend catch-up is
**mildly net-protective, with a defensible interval spanning "modestly protective" to "neutral"**,
and it becomes net-harmful only on his 10–11 h weekend nights.

---

## 1. The construct and the formula

Social jetlag was defined by Wittmann, Dinich, Merrow & Roenneberg (Chronobiol Int 2006;23:497–509,
DOI `10.1080/07420520500545979`, PMID 16687322):

> "The discrepancy between work and free days, between social and biological time, can be described
> as 'social jetlag.'"

The formal equation comes from the originators' own later review (Roenneberg et al., Biology
2019;8:54, PMID 31336976):

> "Originally, SJL was defined as the absolute difference between the midsleep on free days (MSF) and
> that on workdays (MSW; see Equation (3))."

**SJL = |MSF − MSW|**, where midsleep MS = sleep onset + (sleep duration / 2).

Expanding that identity is what makes the subject's arithmetic tractable, because we were given
durations rather than clock times:

```
SJL = (SO_free − SO_work)  +  (D_free − D_work)/2
      \__ term A __________/    \__ term B _______/
      weekend bedtime delay     half the weekend oversleep
```

Two things follow immediately, and both matter downstream.

First, **social jetlag is not a pure timing measure.** Term B means that a person who goes to bed at
exactly the same time every night but sleeps longer at weekends still registers positive social
jetlag. The originators concede the problem directly: *"SJL is also positively associated with
perceived sleep debt, making it difficult to disentangle pure sleep timing effects and those of sleep
deprivation."* This is the single biggest reason the social-jetlag literature and the sleep-duration
literature cannot be cleanly added together — they partly measure the same thing.

Second, **weekend catch-up sleep mechanically generates social jetlag.** Term B is literally half the
catch-up duration. So "catch-up sleep" and "social jetlag" are two codings of one behaviour, which is
the key to §5.

---

## 2. The subject's social jetlag, computed

Reported pattern: weekday sleep ~5–6 h from age 16 to 19; weekend/holiday ~7–8 h; occasional 10–11 h
weekend nights; occasional 3–4 h pre-exam nights.

I need term A (weekend bedtime delay), which was not reported. I bound it at 0 h (a subject who never
shifts bedtime), 0.75 h (central; typical of a late-chronotype student), and 1.5 h (upper).

**Term B, half the weekend oversleep:**

| D_weekday | D_weekend | oversleep | term B |
|---|---|---|---|
| 6.0 h | 7.0 h | 1.0 h | 0.50 h |
| 5.5 h | 7.5 h | 2.0 h | 1.00 h |
| 5.0 h | 8.0 h | 3.0 h | 1.50 h |
| 5.5 h | 10.5 h | 5.0 h | 2.50 h |

**Full grid, SJL = A + B:**

| scenario | A = 0 h | A = 0.75 h | A = 1.5 h |
|---|---|---|---|
| 6.0 → 7.0 h (mild) | 0.50 | **1.25** | 2.00 |
| 5.5 → 7.5 h (central) | 1.00 | **1.75** | 2.50 |
| 5.0 → 8.0 h (severe weekday) | 1.50 | **2.25** | 3.00 |
| 5.5 → 10.5 h (long weekend night) | 2.50 | **3.25** | 4.00 |

**Point estimate and interval:**

- **Central estimate: 1.75 h** (weekday 5.5 h, weekend 7.5 h, bedtime delay 0.75 h).
- **Typical-weekend range: 1.0 – 2.75 h.** Full span across all assumptions 0.50 – 3.00 h.
- **On his occasional 10–11 h weekend nights: 2.25 – 4.00 h, central 3.25 h.**
- Weekend catch-up **duration**: 1.0 – 3.0 h typically; 4.5 – 5.5 h on long nights.
- Catch-up **ratio** (D_free / D_work): 1.17 – 1.60 typically; **1.75 – 2.10** on long nights.

I recommend the modeller carry **SJL ≈ 1.75 h (95% plausible 1.0–2.75)** as the habitual exposure and
treat the long-weekend excursions as an intermittent ~3.25 h state occupying perhaps 10–25% of
weekends.

**Sanity check against a near-identical real cohort.** Kim et al. (Arch Pediatr Adolesc Med
2011;165:806, PMID 21893646) measured 2,638 Korean high-school students at **mean age 17.3**:

> "The mean (SD) sleep duration on weekdays was 5 hours 42 minutes (1 hour 0 minutes) per day and on
> weekends was 8 hours 24 minutes (1 hour 36 minutes) per day. The mean (SD) weekend catch-up sleep
> was 2 hours 42 minutes (1 hour 42 minutes) per day."

Weekday 5.70 h, weekend 8.40 h, catch-up 2.70 h. That is **our subject's pattern almost exactly**,
occurring as the population mean of an entire national school cohort at his age. Whatever else is
true, his pattern is not unusual for a 17-year-old student.

---

## 3. Where that sits in the age-specific normative distribution

This is the question the shard brief flagged as critical, and the honest answer is that the two
largest datasets disagree by about 1.2 h, so I report both rather than picking one.

| Source | n | Population | Mean SJL | Age-specific peak |
|---|---|---|---|---|
| **Randler 2019** (Sleep Med, PMID 30921684) | 18,323 | Germany, ages 0–25 | — | **3:18 h (3.30 h) at age 16** |
| **Illingworth 2025** (Chronobiol Int, PMID 39760865) | 19,760 | England, ages 9–18 | 1:53 h (SD 1:07) | **2:07 h (2.12 h) at age 15** |
| Martins 2025 (Sleep Health, PMID 39532610) | 64,029 | Brazil, ages 12–17 | — | >80% exceed 1 h; prevalence highest at 16–17 |
| Jiang 2024 (Sleep Med, PMID 38991425) | 609 | Shanghai, grades 6–9 | — | 39.0–44.5% exceed 1 h |
| Parsons 2015 (Int J Obes, PMID 25601363) | 815 | NZ adults, age 38 | 0.88 h (SD 0.96) | — (adult comparator) |

Randler: *"Social jetlag increased until 16 years to 3:18 h."* Illingworth: *"The mean SJL was 1 h 53
min (SD = 1 h 7 min) and peaked at 2 h 7 min at age 15."*

The two are not reconcilable by measurement detail alone; they are different countries, instruments
and age-binning. Taking them as bracketing the truth, **the normative mean SJL at ages 15–17 is
somewhere in 2.1–3.3 h.**

**Placement of the subject.** Against Illingworth, which is the only anchor publishing an SD, his
central 1.75 h gives z = (1.75 − 1.883)/1.117 = **−0.12, i.e. the 45th percentile.** Against
Randler's 3.30 h peak he is **well below average.** Even his long-weekend excursions (~3.25 h) only
reach roughly the Illingworth 92nd percentile and merely match the Randler mean.

> **Verdict on outlier status: the subject is TYPICAL, not extreme, on social jetlag — around the
> 45th percentile for his age, and below the mean on either anchor.** His weekday sleep *duration*
> (5–6 h against a normative ~7–8 h at 16–19) is where he is genuinely deviant. Any modelling that
> assigns him a large *extra* penalty for being unusually misaligned is not supported by the
> normative data.

Two further reasons this age band is special, both from the best longitudinal data (Crowley et al.,
PLoS One 2014;9:e112199, PMID 25380248, actigraphy plus laboratory melatonin, ages 9–19):

- The circadian delay is **still actively progressing at his exact age**: *"the largest (~1 h) shift
  occurring between ages 11 and 13 years in the younger cohort and between 17 and 19 years in the
  older cohort."* Average melatonin onset in the older cohort was 20:54.
- But the *social jetlag* should be **easing** as he leaves high school: *"Weekday sleep offset
  shifted earlier with age in the younger cohort and later in the older cohort after age 17.
  Weekend–weekday sleep offset differences increased with age in the younger cohort and decreased in
  the older cohort after age 17."* Randler independently identifies **16–17 as the breakpoint** after
  which sleep behaviour turns back toward *"less socially jetlagged behavior."*

So the subject is passing the peak of his misalignment exposure, not entering it — though a college
schedule with early classes can hold it open.

**On pubertal staging, I must report reality against the brief.** I was asked for phase-delay
estimates *by pubertal stage*. In the best longitudinal data, pubertal stage adds essentially nothing
once you know chronological age: *"Tanner stage added no statistically significant information above
chronological age other than for sleep onset on weekdays in the younger group, in which Tanner stage
≥ 3 was associated with an approximate 12-minute later sleep onset."* The pubertal framing traces to
Carskadon 1993 (PMID 8506460), which used a morningness/eveningness **questionnaire** rather than
measured phase and found the association **in girls only, with a non-significant trend in boys.** For
an 18-year-old male, a Tanner-stage-indexed phase-delay estimate is not supportable. Use
age-indexed estimates: **~1 h of delay across 17→19.**

---

## 4. The independent effect of misalignment, adjusted for duration

### 4a. Causal evidence with duration held constant

This is the strongest thing my shard has, and it is unambiguous. **Leproult, Holmbäck & Van Cauter
(Diabetes 2014;63:1860, PMID 24458353, DOI `10.2337/db13-1546`)** randomised 26 adults to eight
nights of 5 h sleep either at fixed nocturnal bedtimes or with bedtimes delayed 8.5 h on four of
eight days. Sleep amount was equated to **three minutes**:

> "Daily total sleep time (SD) during the intervention was nearly identical in the aligned and
> misaligned conditions (4 h 48 min [5 min] vs. 4 h 45 min [6 min])."

| Outcome | Restriction alone | Restriction + misalignment | Ratio | p |
|---|---|---|---|---|
| Insulin sensitivity, men (n=10 vs 9) | −32% (SD 25) | **−58% (SD 13)** | 1.81× | 0.011 |
| Insulin sensitivity, all (n=12 vs 13) | −34% (SD 23) | **−47% (SD 20)** | 1.38× | 0.026 |
| hsCRP, men | +64% (SD 63) | **+146% (SD 103)** | 2.28× | 0.049 |

Computed Hedges' g for the male insulin-sensitivity contrast: **g = −1.23 (SE 0.505)**, from
SD_pooled = 20.26, d = −1.283, J = 0.955. The subject is male, and the male subgroup is both the
larger and the significant one.

**So misalignment roughly doubles the metabolic cost of a fixed amount of sleep loss.** Corroborated
mechanistically: Scheer 2009 (PNAS, PMID 19255424) showed misalignment alone raised glucose 6%
*despite* 22% higher insulin, cut leptin 17%, and pushed 3 of 8 healthy subjects into a prediabetic
postprandial range; Wong 2015 (JCEM, PMID 26580236) found the observational analogue with
**actigraphic** SJL surviving adjustment for sleep duration *and* sleep debt (HOMA-IR β = 0.11,
p = .031; BMI β = 0.17, p = .001); Parsons 2015 found SJL→BMI, fat mass, MetS, hsCRP and HbA1c all
significant in models *"Controlling for sex, chronotype and sleep duration"*, in a cohort where **SJL
and sleep duration were uncorrelated (r = −0.04, p = 0.28)** — the cleanest demonstration that these
are separable exposures.

And in adolescents specifically, Hasler 2022 (Psychol Med, PMID 33729109) is the only experimental
misalignment study in the right age group. It imposed a school-year schedule (20:00–05:30) versus a
summer schedule (00:00–09:30) — literally the weekday/weekend contrast — and found reduced ventral
striatal reward response and reduced inferior frontal gyrus inhibition **"after accounting for the
prior night's total sleep time"**, with the inhibition effect **specific to the morning scan**.

### 4b. Three reasons to scale the independent effect down hard for this subject

1. **Dose.** Leproult delayed bedtimes by **8.5 h**; Scheer and Morris used **12 h** inversions. Our
   subject's weekly shift is **~1.75 h** — a factor of 5–7 smaller. The dose–response curve between
   1.75 h and 8.5 h of misalignment is **entirely unmeasured**. This is the largest single source of
   uncertainty in my shard.

2. **Proportion.** Morris 2015 (PNAS, PMID 25870289) is the calibration record that keeps this
   honest. A **full 12 h behavioural inversion raised postprandial glucose by only 6%**, while simply
   eating in the biological evening raised it **17%**. Even *maximal* misalignment produces a smaller
   glycaemic effect than ordinary circadian phase variation. That is a strong argument against
   attributing a large metabolic burden to 1.75 h of social jetlag.

3. **Thresholds, and they sit above him.** Two independent literatures put the inflection at ~2 h:
   - Depression (Sun 2025, PMID 40597088): SJL ≥2 h → OR **1.44** (1.18–1.77); SJL 1–2 h → OR **1.05**
     (1.00–1.09), *"not significantly associated."*
   - Academics (Sánchez-Charcopa 2026, PMID 42470595): *"Severe social jetlag (> 2 h) was consistently
     associated with lower academic performance, while mild jetlag (1-2 h) showed no effect,
     suggesting a threshold pattern."*

   **The subject's central 1.75 h falls in the null band.** His long-weekend excursions cross into the
   elevated band.

### 4c. Duration-adjusted per-unit effects worth pooling

| Outcome | Effect | Source | Duration-adjusted? |
|---|---|---|---|
| GPA, per +1 h SJL | OR **0.76** (0.68–0.85) | Sánchez-Charcopa 2026, n=788, ages 12–17 | **Yes** (overall sleep duration) |
| Maths grade, per +1 h SJL | OR 0.81 (0.72–0.91) | same | **Yes** |
| MetS, SJL >2 h vs <1 h (<61 y) | PR **2.13** (1.3–3.4) | Koopman 2017, n=1,585 | **Yes** (+ BMI) |
| Diabetes/prediabetes, >2 h vs <1 h (<61 y) | PR 1.75 (1.2–2.5) | Koopman 2017 | **Yes** |
| Diabetes/prediabetes, 1–2 h vs <1 h (<61 y) | PR 1.39 (1.1–1.9) | Koopman 2017 | **Yes** |
| HOMA-IR, per 1 SD SJL (SD=32 min) | β 0.11, p=.031 | Wong 2015, n=447 | **Yes** (+ sleep debt) |
| BMI, per unit SJL | β 0.10, p=0.012 | Parsons 2015, n=815 | **Yes** |
| BMI, any SJL vs none | **0.49 kg/m²** (0.21–0.77) | Bouman 2023, 20 studies | Mixed |
| BMI, pooled correlation | r **0.12** (0.07–0.17) | Arab 2024, 43 studies, n=231,648 | No |
| Anxiety, continuous SJL | Fisher z **0.061** (0.027–0.096) | Ravenhall 2026, n=235,526 | No |

**The academic effect is the one I would weight most heavily for this subject**: it is per-hour,
duration-adjusted, uses official school records, and comes from a population his age.

### 4d. Countervailing evidence the modeller must not skip

- **The famous Roenneberg 2012 SJL→BMI result does not apply to a normal-weight person.** The
  association is confined to participants already at BMI ≥25: *"social jetlag does not explain the
  variance in weight in the normal BMI group [n=43,302]... it is positively associated with weight
  increase in the overweight group."* Also, a formal **Erratum exists** (DOI
  `10.1016/j.cub.2013.04.011`, Crossref-confirmed) whose content I could not retrieve.
- **Bouman 2023 is null for every clinical endpoint**: *"No statistically significant associations
  were found for obesity, abdominal obesity, high- and low-density lipoprotein levels, cholesterol,
  triglycerides, diastolic blood pressure, hypertension, fasting glucose, homeostatic model
  assessment for insulin resistance, metabolic syndrome or T2D."*
- **In children and adolescents the adiposity signal does not survive quality adjustment**
  (Zhou 2026): *"after adjusting for study quality, these associations became non-significant."*
- **The only prospective adolescent SJL–adiposity study is null in boys** (Jiang 2024): *"no
  significant associations among boys were observed."* Díaz-Morales 2015 similarly reports SJL *"may
  be more detrimental to girls' performance."* Our subject is male; there is a recurring sex pattern
  here that attenuates his expected effect.
- **Exposure misclassification is likely severe.** Hasler 2025 (Sleep, PMID 39901722) reports that in
  high-school students, self-report proxies *"for circadian timing were poor approximations of
  biological circadian phase."* Nearly every observational estimate above is built on self-report.

---

## 5. The critical tension: is weekend catch-up protective or harmful?

Both literatures are real. They are **not** in genuine contradiction, for two reasons that I can
state precisely.

### 5a. Resolution 1 — they measure different exposures

This is the deeper of the two, and it follows from the algebra in §1.

- **"Weekend catch-up sleep" is coded as a DURATION difference** (weekend TST − weekday TST, or their
  ratio). More catch-up means *more total sleep*. Coded this way, it is protective, because it is
  partly a proxy for *getting more sleep*.
- **"Social jetlag" is coded as a TIMING difference** (MSF − MSW). More social jetlag means *more
  phase instability*. Coded this way, it is harmful.

**The same weekend lie-in increases both.** So the sign of the estimate is substantially determined
by which variable the analyst chose to code, not by a disagreement about biology. The clearest single
demonstration is that two studies of *Korean adolescents* reach opposite conclusions: Lee 2025
(duration coding) finds catch-up ≥3 h → overweight/obesity **OR 0.67**; Zhou 2026 (timing coding)
finds highest-vs-lowest SJL → overweight/obesity **OR 1.25**.

### 5b. Resolution 2 — the dose–response is U-shaped, and each camp sampled one arm

Kim & Casement (Sleep 2026;49:zsag113, PMID 42023681), 1,867 adolescents with **Fitbit-measured**
sleep, tested non-linearity explicitly:

> "Adolescents with moderate WCS (≤2 h) had lower odds of clinical level anxiety than those with
> consistent sleep (odds ratio = 0.49, confidence interval = 0.30 to 0.78, p = .003). Quadratic
> models revealed U-shaped associations: both weekend sleep loss and excessive WCS were linked to
> elevated anxiety (p = .005) and depressive symptoms (p = .043), with the lowest symptoms at
> moderate WCS."

Independently replicated in n=270,619 Korean adolescents (Lee 2022, PMID 35715557): catch-up ratio
**≥1.50 → increased depression odds even with good sleep quality**, while ratio **<1.00 with weekday
sleep <5 h was the worst of all**. Moderate catch-up is the optimum; both extremes are worse.

### 5c. Outcome-by-outcome breakdown

| Outcome | Direction of weekend catch-up | Best evidence | Strength |
|---|---|---|---|
| **All-cause mortality** | **PROTECTIVE** | Åkerstedt 2019 (T5, n=43,880, 13 y): consistently ≤5 h HR **1.65** (1.22–2.23); *"The mortality rate of individuals with short sleep during weekdays, but medium or long sleep over weekends (SML), did not differ from the reference group rate."* Long weekend sleep alone carried no excess. | Moderate. Only mortality evidence on this pattern; adults, null in ≥65 s; SML point estimate is figure-only. |
| **Depression / mood** | **PROTECTIVE** | Carbone 2026 (NHANES, **ages 16–24**, n=1,087): WCS → **41% lower odds** of daily depressive symptoms, covarying weekday duration *and* midpoint. Kim DJ, Lee 2022: catch-up <1.00 ratio with <5 h weekday is worst. | Moderate; exactly age-matched but cross-sectional, single-item outcome, no CI published. |
| **Anxiety** | **PROTECTIVE up to ~2 h, then HARMFUL** | Kim & Casement 2026: OR **0.49** at ≤2 h; U-shaped, and the U survived adjustment for weekday duration and timing. | Moderate; objective sleep, explicit non-linearity. |
| **Suicidality / self-injury** | **HARMFUL** | Kang 2014 (n=4,145): longer WCUS → suicide attempt/self-injury (p=0.011). | Weak. Cross-sectional, reverse causation wide open, and the authors read catch-up as *"an indicator of insufficient weekday sleep."* |
| **Attention / cognition** | **HARMFUL** | Kim 2011 (n=2,638, age 17.3): more WCUS → more omission/commission errors on sustained and divided attention, *after adjusting for weekday sleep duration*. | Moderate; objective tasks, but authors again treat catch-up as a *marker* of sleep debt — risk of double-counting the weekday-restriction effect. |
| **Insulin sensitivity (acute)** | **HARMFUL** | Depner 2019 (T1): SR −13% vs **WR −27%** whole-body; hepatic −23% **only** in WR; DLMO delayed **1.7 h** in WR vs ~25 min in SR. | See 5d — weaker than usually claimed. |
| **Metabolic syndrome (habitual)** | **PROTECTIVE** | Kim DJ 2020 (KNHANES, n=1,812 chronic short sleepers): *"WCUS was significantly associated with lower MetS prevalence"* in adjusted models. | Weak-moderate; cross-sectional, midlife, no ORs published. |
| **Adiposity / BMI** | **CONTESTED — protective cross-sectionally, harmful within-person** | Lee 2025 OR **0.67**; Choi 2023 RR **1.93** for failing to catch up. **But** Park & Kim 2023 (T5, 6 waves, individual fixed effects): *"Controlling for individual heterogeneity ... changed the sign of the WCS duration coefficient, suggesting that a longer WCS duration is positively associated with BMI (b = 0.021)."* | See 5e. |
| **Circadian phase** | **HARMFUL, unambiguously** | Depner 2019: weekend recovery delayed DLMO **~1.7 h** vs ~25 min without it. This is the mechanism. | Strong for the mechanism itself. |

### 5d. Why the Depner "catch-up is harmful" result is weaker than it is usually cited as being

Almost the entire harmful-metabolic position rests on this one study, so its limits decide how much
the tension is worth. I read the full text. The analysis is **within-group only**:

> "Mixed-Effects ANOVAs with either study day ... as fixed factors, and participant as a random
> factor were used to test for **within group** differences"

**The 27%-versus-13% comparison was never statistically tested.** There is no between-arm contrast,
no CI, and no p-value for "WR minus SR" anywhere in the paper. They are two separately estimated
within-arm changes in groups of n=14. The WR insulin-sensitivity loss also **lost significance when
body weight was controlled (P = 0.054)**, and diet was ad libitum, so energy intake is a mediator
rather than a control. I therefore recorded the two within-arm changes separately with `se: null` and
**refused to emit a WR-versus-SR effect size**.

What Depner *does* establish solidly, and what should be carried forward:
- A real ad libitum weekend recovers only **1.1 h of sleep in total** across both nights.
- Weekend recovery **delays circadian phase ~1.7 h**, four times the drift seen without it. Catch-up
  sleep demonstrably manufactures misalignment.
- Hepatic insulin sensitivity fell **only** in the weekend-recovery arm.
- Benefits observed during the weekend itself **did not survive** the return to short sleep.

Set against it, Buxton 2012 (PMID 22496545) found that metabolic derangements *"normalized during the
9 days of recovery sleep and stable circadian re-entrainment"* — recovery works when it is long
enough and phase-stable, which is precisely what a 2-day weekend is not.

### 5e. The one study that genuinely threatens the protective column

Park & Kim 2023 (Public Health, PMID 36521277) is the strongest observational design here: six waves
of Korean panel data with **individual fixed effects**, which removes all stable confounding. It
reports that **62% of the cross-sectional short-sleep→BMI association is confounding**, and that
catch-up's coefficient **flips sign** under within-person identification.

That is strong evidence the many Korean cross-sectional "catch-up protects against obesity" findings
(Lee 2025, Choi 2023, Kim DJ 2020, Son 2020 — several of which share the KNHANES cohort family and
must **not** be pooled as independent) are substantially confounded by who chooses to catch up.

Note the magnitudes even so: weekday short sleep moves BMI by **0.203**, catch-up by **0.021**. The
duration effect is an order of magnitude larger than the catch-up effect **in either direction**. The
authors' own conclusion is the position I adopt: *"WCS duration is protective only for those who are
most sleep deprived."* Our subject is exactly that person.

---

## 6. Net verdict on weekend catch-up for this subject

**Position: mildly net-protective. Interval: modestly protective to neutral. Not net-harmful at his
typical weekend dose; net-harmful on his 10–11 h weekend nights.**

The reasoning, in order of weight:

1. **The relevant counterfactual is not "consistently adequate sleep" — it is "consistently short."**
   The subject is not choosing between 7.5 h every night and his current pattern; his weekday
   constraint is fixed. Against the *consistently short* comparator, the evidence is consistent and
   favourable: mortality HR **1.65** for consistently ≤5 h versus **no detectable excess** for short
   weekdays with long weekends; depression worst at catch-up ratio <1.00 with weekday <5 h; obesity
   risk **1.93×** for <6 h weekdays *with* <3 h of catch-up.
2. **His typical catch-up (1–3 h duration, ratio 1.17–1.60) sits at or just past the top of the
   beneficial band** identified by both U-shape studies (optimum ≤2 h; harm from ratio ≥1.50).
3. **His long-weekend nights (catch-up 4.5–5.5 h, ratio 1.75–2.10, SJL ~3.25 h) are clearly in the
   harmful arm** — above Lee 2022's ≥1.50 ratio threshold, above the ~2 h SJL depression and academic
   thresholds, and in Åkerstedt's consistently-long band (HR 1.25) at the duration end.
4. **Park & Kim's sign reversal caps how protective I am willing to call it.** This is why my interval
   extends to *neutral* rather than stopping at *protective*.
5. **Catch-up is a partial substitute, not a fix.** Carbone 2026: *"Healthy weekday sleep duration at
   an optimal time each had twice the benefit for depressive symptoms."* Depner: a real weekend
   recovers only 1.1 h.
6. **Domain-specific exceptions the modeller should apply rather than average away:** catch-up is
   harmful for **circadian phase** (~1.7 h delay, unambiguous), **acute hepatic/whole-body insulin
   sensitivity** (Depner, with the caveats in §5d), and **attention** (Kim 2011) — though the
   attention and suicidality signals likely reflect catch-up acting as a *marker* of weekday sleep
   debt, so counting them as separate harms would double-count the duration effect other shards are
   already estimating.

**Suggested encoding.** Rather than a single multiplier, apply an outcome-specific modifier to the
weekday-restriction harm:

| Domain | Catch-up modifier | Rationale |
|---|---|---|
| Mortality | **0.6–1.0** (offsets much of it) | Åkerstedt SML null vs SS HR 1.65 |
| Depression / anxiety | **0.6–0.9** (protective) | Carbone 41% lower odds; Kim & Casement OR 0.49 |
| Adiposity / metabolic (habitual) | **0.9–1.1** (≈neutral) | Protective cross-sectional vs sign-flip under fixed effects |
| Insulin sensitivity (acute) | **1.0–1.5** (aggravating) | Depner, downweighted for the untested contrast |
| Circadian phase / academics | **1.0–1.3** (aggravating) | Phase delay is real; ~2 h SJL threshold approached |

And separately: **SJL ≈ 1.75 h (1.0–2.75)** as the misalignment exposure, applied to the
duration-adjusted per-hour effects in §4c, with **wide uncertainty** because (a) every causal estimate
comes from 8.5–12 h misalignment doses, 5–7× his, and (b) self-reported timing is a poor proxy for
measured phase in his age group.

---

## 7. What would change this verdict

- **A dose–response study of misalignment between 1 and 3 h.** Every causal estimate available uses
  8.5–12 h. This is the single biggest gap in my domain.
- **A between-group test of weekend recovery versus continuous restriction.** Depner's arms were
  never compared. One adequately powered contrast would settle §5d.
- **The Roenneberg 2012 supplementary Table S1B and its 2013 Erratum**, which together hold the
  per-hour SJL→BMI coefficient that the task asked for and that I could not obtain.
- **Åkerstedt's Figure 4 numeric values** for the short-weekday/long-weekend cell, the single most
  decision-relevant point estimate in the protective column, currently available to me only as a
  stated null.
