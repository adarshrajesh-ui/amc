# Recovery dynamics: what actually happens when a chronically sleep-restricted person starts sleeping more

Shard `s05_recovery_kinetics`. 313 records screened, 30 extracted, 110 effect estimates, 0 identifiers
failed verification. Every number below is traceable to a verbatim quote in the corresponding YAML
record; arithmetic I performed myself is labelled as such and the inputs are shown.

## Headline answers

| Question | Answer | Best evidence |
|---|---|---|
| Does extra sleep repay debt hour-for-hour? | **No.** One night at 10 h TIB repays **2-4%** of a 23 h debt | Banks 2010 (T1, n=159) |
| Extra actual sleep per extra hour of opportunity | **0.73-0.98 h/h acutely, falling to ~0 at the ceiling; 0.38-0.60 h/h in real life** | Banks 2010; Al Khatib 2018, Tasali 2022 |
| Ceiling on nightly sleep, single night ad-lib | **10.0-10.4 h** | Yamazaki 2021, Depner 2019, Kitamura 2016 |
| Ceiling on nightly sleep, sustained | **7.9-8.1 h nocturnal-only; 8.4-9.2 h if daytime sleep allowed** | Klerman 2008, Banks 2010, Kitamura 2016 |
| Time for *sleep duration* to asymptote | **4-5 days in lab (7-14 days free-living)** | Kitamura 2016, Klerman 2008, Bei 2014 |
| Time for *vigilance* to asymptote | **> 7 days; not established. No study has demonstrated full PVT recovery** | Ochab 2021, Axelsson 2008, Yamazaki 2021 |
| Did anything fail to recover? | **Yes — at 1 night, 3 nights, 4 nights, 5 nights, 7 days, 13 days and 5 weeks** | 9 independent studies |
| Is weekend-only catch-up sufficient? | **No, and it cannot be — the arithmetic is impossible** | Depner 2019, Lo 2022, Smith 2021 |

---

## 1. Extra sleep does not repay debt hour-for-hour

### 1a. The marginal yield of sleep per hour of opportunity

Banks 2010 is the cleanest available measurement because it randomized 159 adults, after five identical
nights at 4 h TIB, to a single recovery night of 0, 2, 4, 6, 8 or 10 h TIB. Adjusted mean total sleep
time rose almost linearly with opportunity but with a clearly **concave** shape:

| Recovery TIB | TST obtained | Marginal yield over previous step |
|---:|---:|---:|
| 2 h | 1.88 h | 0.940 h/h |
| 4 h | 3.84 h | 0.980 h/h |
| 6 h | 5.74 h | 0.950 h/h |
| 8 h | 7.51 h | 0.885 h/h |
| 10 h | 8.96 h | **0.725 h/h** |

Ordinary least squares across the whole ladder gives `TST = 0.237 + 0.8915 × TIB`, R² = 0.9968 (my
regression on the six published adjusted means). The yield is high at low doses because a severely
sleep-deprived person sleeps through nearly all of a short opportunity, and it decays as the opportunity
approaches capacity. **The last two hours of opportunity bought only 1.45 h of sleep.**

Extrapolating this concavity is exactly what the rest of the evidence does. As opportunity grows further,
the marginal yield collapses toward zero:

| Study | Opportunity | Sustained TST | Sleep efficiency | Opportunity left unused |
|---|---:|---:|---:|---:|
| Banks 2010 controls, 10 h TIB × 8 nights | 10 h | 7.95 h | 79.5% | 2.05 h |
| Klerman 2008, 12 h nocturnal, asymptote | 12 h | 7.90 h | 65.8% | 4.10 h |
| Kitamura 2016, 12 h TIB × 9 nights | 12 h | 8.41 h | 70.1% | 3.59 h |
| Klerman 2008, 16 h/24 h, asymptote | 16 h | 8.90 h | 55.6% | **7.10 h** |

Klerman & Dijk 2008 is decisive here and I retrieved it in full text. They gave 35 young adults (18-32 y,
mean 21.9) **16 hours of bedrest per 24 hours** — 12 h at night plus 4 h in the afternoon, in darkness,
with no time-of-day cues — for up to seven days. Asymptotic sleep was 8.9 h per 24 h (95% CI 8.1-9.7).
The other **7.0 hours were spent awake in bed**. Sleep efficiency at asymptote was 55.6%.

In free-living conditions the yield is far worse, because the binding constraint stops being physiology
and becomes behaviour:

| Study | Design | Extra opportunity | Extra actual sleep | Yield |
|---|---|---:|---:|---:|
| Al Khatib 2018 | 4 wk, 1 counselling session | +0.917 h TIB | +0.350 h | **0.382 h/h** |
| Tasali 2022 | 2 wk, 8.5 h TIB target | ~+2.0 h TIB | +1.200 h | 0.600 h/h |
| Leproult 2015 | 6 wk, +1 h TIB target | +1.0 h TIB | +0.733 h | 0.733 h/h |
| Lucassen 2014 | ~15 months counselling + lifestyle | not specified | **+0.257 h** | — |

Lucassen 2014 is worth dwelling on: **fifteen months** of clinical sleep-extension counselling in 121
habitual short sleepers produced about **15 minutes** more sleep per night by diary. Longer intervention
did not mean larger gain — the two shortest and most concretely specified protocols (Tasali, Leproult)
produced the biggest gains. That argues for prescribing a specific time-in-bed schedule rather than
advising someone to "sleep more".

### 1b. What fraction of accumulated debt does a recovery block actually return?

I computed these ledgers from published per-night TST values. Debt is `nights × (baseline TST − restricted
TST)`; repayment is the sleep obtained above baseline during the recovery block.

| Study | Debt accrued | Recovery block | Sleep above baseline | **% of debt repaid** |
|---|---:|---|---:|---:|
| Banks 2010 | 23.43 h (5 × 4 h TIB) | 1 night @ 10 h TIB | +0.86 h | **3.7%** |
| Belenky 2003, 3 h group | 24.57 h (7 × 3 h TIB) | 3 nights @ 8 h TIB | +0.51 h | **2.1%** |
| Belenky 2003, 5 h group | 13.06 h (7 × 5 h TIB) | 3 nights @ 8 h TIB | +0.00 h | **0.01%** |
| Belenky 2003, 7 h group | 3.99 h (7 × 7 h TIB) | 3 nights @ 8 h TIB | −0.37 h | **−9.2%** |
| Pejovic 2013 | 10.38 h (6 × 6 h TIB) | 2 nights @ 10 h TIB | +3.62 h | **34.9%** |
| Depner 2019 | >12 h weekday deficit | ad-lib weekend | +1.1 h | **≤9.2%** |

The Banks figure uses the authors' own paired within-subject comparison: subjects randomized to 10 h TIB
slept 51.5 ± 12.3 min (SEM) more than on their own 10 h baseline night (t₂₅ = 4.17, P < 0.001), i.e.
+0.86 h against a 23.43 h debt. Routing instead through the adjusted group means (8.96 h vs 8.47 h
baseline) gives +0.49 h and 2.1%. Either way the answer is a few per cent.

Two features of this table matter more than the individual numbers.

**The 8 h recovery night repays essentially nothing.** In Belenky's 5 h and 7 h groups, three nights at
8 h TIB returned zero and *negative* surplus respectively — the 7 h group actually slept *less* during
recovery than at their own baseline. The mechanism is visible in the data: at 8 h TIB these commercial
drivers obtained only 6.19-6.58 h of sleep (78-82% efficiency), and their pre-study baseline at the same
8 h TIB was already 6.15-6.42 h. An 8 h opportunity was at or below their habitual sleep, so it could not
generate surplus. **This generalizes: if sleep need is ~8.4-8.9 h, an 8 h night cannot repay debt at all.
It can only stop the debt growing.** Smith 2021 is the clean confirmation — 5 h weekdays with 8 h weekends
for six weeks produced monotonically worsening vigilance, and by construction the weekend surplus was
2 × (8 − 8) = 0 h.

**Pejovic's 35% is the exception that proves the rule.** It is by far the best repayment fraction in the
literature, and it required a *mild* debt (6 h TIB, not 4 h) plus a *generous* recovery dose (10 h TIB,
yielding 9.15 h TST). Even then, two-thirds of the debt remained — and PVT performance was still
significantly *worse* than baseline afterwards.

### 1c. How much performance recovery does the extra sleep buy?

Recovery of function is not proportional to recovery of sleep. I computed Hedges' g for the residual
deficit at each Banks recovery dose (recovery night vs that subgroup's own pre-restriction baseline;
SE derived by inverting the reported paired-t p-values):

| Recovery dose | n | PVT lapses g | KSS g | MWT g | p (lapses) |
|---:|---:|---:|---:|---:|---:|
| 0 h | 13 | +2.233 | +2.067 | −2.437 | <0.0005 |
| 2 h | 27 | +1.380 | +2.343 | −1.922 | <0.0005 |
| 4 h | 29 | +1.395 | +1.280 | −1.061 | <0.0005 |
| 6 h | 25 | +1.096 | +0.936 | −0.699 | <0.0005 |
| 8 h | 21 | +0.560 | +0.636 | −0.402 | 0.004 |
| 10 h | 27 | **+0.429** | **+0.501** | −0.140 (n.s., p=0.558) | **0.008** |

Positive g = worse than that person's own baseline. After the largest single recovery night available —
10 h TIB, 8.96 h of actual sleep — PVT lapses (g = +0.43, SE 0.15, p = 0.008), KSS sleepiness
(g = +0.50, p = 0.007), PVT fastest reaction times (g = +0.39, p = 0.005) and POMS fatigue (g = +0.57,
p = 0.021) were all still significantly impaired. Only the Maintenance of Wakefulness Test had returned
to baseline.

The authors then extrapolated their linear dose-recovery functions to find the opportunity that would be
needed to reach the non-restricted control group's level:

| Outcome | TIB required | 95% CI | TST required | 95% CI |
|---|---:|---|---:|---|
| PVT lapses | 10.66 h | 7.97-13.34 | 10.00 h | 7.32-12.68 |
| KSS sleepiness | 10.62 h | 7.80-13.44 | 10.29 h | 7.10-13.51 |
| PVT fastest RTs | **> 13 h** | — | ~11 h | — |
| DSST, POMS fatigue | < 10 h | — | — | — |

So vigilance would have needed **~10.7 h TIB in a single night** — beyond the experiment's maximum — and
psychomotor speed more than 13 h TIB, which is beyond the physiological ceiling entirely. The confidence
intervals are wide and the authors say so. But the direction is unambiguous, and it is the same direction
as the ceiling evidence: **the single-night dose required to restore vigilance after only five nights of
restriction exceeds what a human can sleep in one night.**

### 1d. The empirical ceiling on nightly sleep during ad-lib recovery

The brief asks whether someone could sleep 16 h to repay 8 h of debt. Klerman & Dijk offered exactly
16 h and the answer is no. The convergence across independent laboratories is strong:

**Single-night maxima** (the largest one-night sleep ever measured in these protocols):

| Study | Opportunity | Max TST |
|---|---:|---:|
| Yamazaki 2021, recovery night 1 | 12 h TIB | 10.4 h |
| Depner 2019, women, day 8 | 12.1 h TIB | 10.3 h |
| Depner 2019, men, day 9 | 12.1 h TIB | 10.2 h |
| Kitamura 2016, night 1 | 12 h TIB | 10.0 h |
| Banks 2010, recovery night | 10 h TIB | 8.96 h |
| Klerman 2005, day 1 | 16 h/24 h | +4.9 h above habitual |

**Sustained (asymptotic) maxima** — what a person settles at when the rebound has discharged:

| Study | Opportunity | Asymptote |
|---|---:|---:|
| Klerman 2008, nocturnal only | 12 h | 7.90 h |
| Banks 2010, sleep-satiated controls | 10 h × 8 nights | 7.95 h |
| Kitamura 2016 | 12 h × 9 nights | 8.41 h |
| Yamazaki 2021, recovery night 4 | 12 h | ~8.5 h |
| Rupp 2009, extension week | 10 h × 7 nights | 8.68 h |
| Klerman 2008, incl. 4 h afternoon | 16 h/24 h | 8.90 h |
| Klerman 2008, matched habitual range | 16 h/24 h | 9.20 h |

Range 7.90-9.20 h, mean 8.51 h.

**Two conclusions with direct prescriptive force.**

First, **the ad-lib ceiling is about 10.4 h for one night and about 8.5 h sustained.** A person cannot
sleep 16 h to repay 8 h; the surplus available above an 8.4-8.9 h need is at most ~1.5-2.0 h on the best
night and approximately zero once the rebound decays. Debt repayment therefore proceeds at roughly
1-2 h per night at the very start and slows to nothing — which is why every repayment fraction in
§1b is in single digits.

*One documented exception, stated for honesty:* Banks 2010's discussion notes that "recovery sleep can
extend to 14 h TST under extreme conditions of deprivation," citing the two-process-model literature.
That refers to total sleep deprivation, not chronic restriction, and I did not retrieve the primary
source. It does not change the chronic-restriction ceiling but it does mean 10.4 h should be read as the
ceiling *in these chronic-restriction protocols*, not as an absolute human maximum.

Second, and much less widely appreciated: **nocturnal sleep saturates lower than total sleep.** Klerman's
young adults asymptoted at 7.9 h within a 12 h *nocturnal* opportunity (8.1 h in the habitual-range
subset); the extra ~1.0 h that brought them to 8.9 h/24 h was obtained in the **afternoon**. Banks'
sleep-satiated controls asymptoted at 7.95 h under a 10 h nocturnal opportunity — essentially the same
number from a different laboratory. A night-only prescription therefore cannot deliver 8.9 h however long
the night is. This independently explains why Lo 2022 found daytime naps added measurable recovery value
in adolescents: **an afternoon nap is not a crutch, it is a structural requirement for reaching full
sleep capacity.**

---

## 2. The empirical time constant

Two different time constants are being conflated in the popular framing, and they differ by at least an
order of magnitude.

### 2a. Sleep duration itself: 4-5 days (interval 4-14 days)

| Study | Population | Protocol | Days to asymptote |
|---|---|---|---:|
| Kitamura 2016 | 15 men, 23.4 y | 12 h TIB × 9 days | **4 days** (τ = 2.52 d) |
| Klerman 2008 | 35 adults, 18-32 y | 16 h/24 h × 3-7 days | **~5 days** |
| Klerman 2008 | 18 adults, 60-76 y | 16 h/24 h | ~2 days |
| Klerman 2005 | 17 adults, 18-32 y | 16 h/24 h × 3 days | still declining at day 3 |
| Bei 2014 | 146 adolescents, **16.2 y** | 2-week vacation, free-living | **7-14 days** |

Kitamura 2016 is the single most directly relevant study in the shard for this question. Fifteen
habitually short-sleeping young men (habitual actigraphic sleep 7.37 h) were given 12 h TIB for nine
consecutive days. Sleep was 10.0 h on night 1 — a rebound of +2.63 h — then decayed exponentially to an
asymptotic "optimal sleep duration" of **8.41 h**, reached by day 4, implying a **sleep debt of 1.04 h
per night**. The exponential time constant was τ = 2.52 days (their initialization value derived by
interpolating the time for the E1-E5 difference to decay by 37%), which implies ~95% decay by 7.6 days.

**Point estimate: 4-5 days in a controlled setting; 7-14 days free-living. I recommend 4-14 days as the
working interval.** The free-living figure is slower, and Bei 2014 shows why: in 16-year-olds on
unstructured vacation, time in bed did not increase significantly at all. What changed was *timing* —
bedtime and rise-time delayed progressively and linearly for the full fortnight, sleep-onset latency rose,
sleep efficiency fell, and wake-after-sleep-onset increased. Adolescents left to themselves convert
opportunity into *later* sleep rather than *more* sleep, and finish phase-delayed.

### 2b. Performance: longer than 7 days, and not established

No study I found has demonstrated full recovery of vigilance after chronic restriction. What exists is a
sequence of lower bounds:

| Recovery observed | Study | Result at that endpoint |
|---:|---|---|
| 1 night @ 10 h TIB | Banks 2010 | PVT, KSS, POMS still impaired (g = +0.43 to +0.57) |
| 1 night @ 8 h TIB | Sallinen 2008 (19-22 y) | performance and sleepiness still below control |
| 2 nights @ 10 h TIB | Pejovic 2013 | IL-6 and MSLT recovered; **PVT did not** |
| 3 nights @ 8 h TIB | Belenky 2003 | PVT plateaued below baseline |
| 4 nights @ 12 h TIB | Yamazaki 2021 | PVT lapses and speed still impaired |
| 5 nights @ 8 h TIB | Rupp 2009 | habitual-sleep group never caught the banked group |
| 7 days @ habitual | Ochab 2021 | mean RT recovered; **accuracy, ERPs, power spectra, actigraphy did not** |
| 7 days @ 8 h TIB | Axelsson 2008 | KSS and median RT recovered; **PVT lapses did not** |
| 12-13 days | Bougard 2018 | microsleeps normalized only by day 12; MWT/KSS/sleep normal by 13 |
| 13 days | Rabat 2016 | **salivary α-amylase still depressed** |
| 3 weeks of cycles | Simpson 2016 | monocyte IL-6 elevated, cortisol rhythm dysregulated |
| 6 weeks of cycles | Smith 2021 | vigilance deficits never restored (β = −0.688) |
| 5 weeks | Cheng 2026 | **74 genes still dysregulated** |

**The shortest observation of complete normalization of any vigilance-adjacent objective measure is 12
days** (Bougard's microsleeps). The longest follow-ups still show abnormality: 13 days for α-amylase and
5 weeks for the transcriptome.

For the recovery prescription I would state: **sleep duration stabilizes in 4-14 days; vigilance requires
at least 2 weeks and plausibly 3-6 weeks; some molecular and neurophysiological measures are unresolved
beyond 5 weeks.** The upper part of that range is an extrapolation and must be labelled as one — see §3c.

### 2c. Prior sleep history changes the time constant

Rupp 2009 is the only study that manipulated sleep history experimentally, and it found a large effect.
Twenty-four adults spent a week at either 10 h TIB (banked) or their habitual ~7 h, then both groups took
7 nights at 3 h TIB followed by 5 recovery nights at 8 h TIB. During restriction the habitual group
accumulated lapses faster (group × day interaction on lapses, +0.40 lapses/day). During recovery, **the
banked group rebounded after a single night and then held steady, while the habitual group improved only
gradually across all five nights and never reached the banked group's level.**

This is the most directly transportable finding in the shard for a subject with three years of
restriction: **a history of chronic short sleep predicts a slower recovery trajectory, not merely a lower
starting point.** Rupp's habitual group had only one prior week of ~7 h sleep, not three years.

Two further constraints on optimism. Skorucak 2018 (n = 35) found that homeostatic sleep regulation is
*preserved* rather than adapted after a week at 6 h TIB — the system does not recalibrate to need less,
so the debt is real and stays owed. And Klerman 2008 found healthy young adults not selected for short
sleep habitually spent 8.5 h in bed against an 8.9 h sleep need, meaning **the "baseline" in nearly every
study here is itself debt-laden and every "return to baseline" criterion is set too low.** That biases
this entire literature toward *under*-detecting incomplete recovery.

---

## 3. Measures that failed to recover, and over what window

### 3a. The recovery-speed hierarchy

Ordering the evidence by how quickly each measure normalizes produces a consistent hierarchy across at
least six independent studies:

**Fast (1-2 nights):** subjective sleepiness (KSS), mood/POMS, Maintenance of Wakefulness Test, sleep
latency (MSLT), IL-6, testosterone, DSST and calculation throughput.

**Slow (≥ 7 days, often unresolved):** PVT lapses, PVT response speed, accuracy under load, event-related
potentials, EEG power spectra, actigraphic rest-activity structure, cortisol rhythm, salivary α-amylase,
gene expression.

The same dissociation is reported independently by Jones 2024 (mood restored dose-dependently while PVT
in the same protocol family was not), Ochab 2021 (KSS recovered by day 7; ERPs and power spectra did not),
Pejovic 2013 (IL-6 and MSLT recovered; PVT did not), Axelsson 2008 (KSS and median RT recovered; lapses
did not), Klerman 2008 (alertness, DSST and throughput improved after one 12 h night; PVT lapses and
median RT did not change at all), and Zitting 2018 (young and older adults reported *identical*
subjective sleepiness while young adults were objectively far more impaired).

**The prescriptive consequence is blunt: feeling recovered is not evidence of being recovered, and
self-report cannot be used to decide when recovery is complete.** For an 18-year-old this is worse than
average — Zitting 2018 found young adults (18-27 y) had ~1 SD more objective sleepiness intrusion than
55-70 year olds under identical restriction (slow eye movements during PVT, g = 1.02, 95% CI 0.24-1.81;
probability of involuntary sleep onset during a 10-minute task, g = 1.08, 95% CI 0.23-1.93) while rating
themselves no sleepier.

### 3b. The two most important non-recoveries

**Cohen 2010 — the hidden debt.** After three weeks of chronic restriction (~5.6 h/24 h), morning
performance following a 10 h sleep opportunity looked essentially normal, and the y-intercept of the
reaction-time-versus-time-awake function was unchanged. But the *slope* nearly tripled, from **24 ms per
hour awake at baseline to 69 ms per hour awake by week 2** (p < 0.0001), persisting into week 3. The
person wakes up looking recovered and degrades ~3× faster across the day. Any assessment done in the
morning will miss this entirely.

**Belenky 2003 — the anchor finding.** This is the study the brief flagged, and it holds up. The journal
article is paywalled, so I extracted from the underlying technical report (Balkin et al. 2000,
DOT-MC-00-133), n = 66 commercial drivers. After seven nights at 3/5/7/9 h TIB, three recovery nights at
8 h TIB did **not** restore PVT performance. The 3 h group improved sharply on the first recovery night
and then **plateaued at the level of the 5 h and 7 h groups rather than returning to baseline.** The
mechanism is in the sleep data: recuperative sleep at 8 h TIB was only 6.19-6.58 h across all groups, no
group slept above its own baseline, and so no debt could be repaid.

### 3c. The critical limitation: most studies follow only 1-3 nights

**Of the 28 included records with a quantified recovery or extension window, 11 (39%) observed 3 nights
or fewer. The median window is 7 days.** Only 10 records observed 13 days or more, and of those, four are
outpatient extension trials (Al Khatib, Tasali, Leproult, Lucassen) that measure sleep gained rather than
recovery of function.

This matters in a specific and directional way. **Every study that looked longer found more
non-recovery.** Studies that stopped at 1-3 nights could only report that recovery was incomplete;
studies that ran 7 days found ERPs and power spectra still abnormal; 13 days found α-amylase still
suppressed; 5 weeks found 74 genes still dysregulated. There is no point in this literature at which
extending the observation window revealed that everything had quietly normalized. The short-follow-up
studies are therefore **not** conservative — they systematically truncate the observation before the
slow-recovering measures could be seen, and they anchor "baseline" to an already debt-laden reference
(§2c).

Three further gaps bound what can honestly be claimed:

1. **No study has restricted anyone for anything close to 3 years.** The longest controlled restriction
   is 6 weeks (Smith 2021) and the longest with a repeating weekly cycle is also 6 weeks. Extrapolating
   from ≤6-week exposures to a 3-year exposure is unavoidable but must be labelled.
2. **Zitting 2018 collected a 10-day inpatient recovery segment at 10 h TIB after three weeks of
   restriction and did not report its outcomes.** That would be among the longest controlled recovery
   observations in existence. The data appear to exist and are unpublished.
3. **Almost no recovery kinetics exist in the target age band.** Only 5 of 30 records are
   `exact_16_19` (Short 2018, Lo 2022, Bei 2014, Sallinen 2008, and Niu 2021's meta-analysis), and of
   those only Lo 2022 measures repeated restriction-and-recovery cycles with performance outcomes.

---

## 4. Weekend-only catch-up is not sufficient, and it cannot be

This is the most decisive result in the shard, because it does not depend on any single study — it follows
from arithmetic that the physiological ceiling makes inescapable.

### 4a. The structural argument

Take the target pattern: 5 weekday nights of restricted sleep, 2 weekend nights of catch-up, sleep need
somewhere in 8.4-9.35 h (Kitamura's 8.41 h optimal; Klerman's 8.9 h young-adult asymptote; Short's
9.0-9.35 h adolescent model). Cap weekend sleep at the **empirical single-night ceiling of 10.4 h**
(Yamazaki night 1; Depner 10.2-10.3 h). Then:

| Weekday TST | Assumed need | Weekday deficit/week | Max weekend surplus | **% repayable** |
|---:|---:|---:|---:|---:|
| 5.0 h | 8.40 h | 17.00 h | 4.00 h | 23.5% |
| 5.0 h | 8.90 h | 19.50 h | 3.00 h | 15.4% |
| 5.0 h | 9.35 h | 21.75 h | 2.10 h | 9.7% |
| 5.5 h | 8.90 h | 17.00 h | 3.00 h | **17.6%** |
| 6.0 h | 8.90 h | 14.50 h | 3.00 h | 20.7% |
| 6.0 h | 9.35 h | 16.75 h | 2.10 h | 12.5% |

**Even sleeping to the physiological maximum on both weekend nights, a weekend can repay at most about
10-25% of the weekday deficit.** For the subject's most likely parameters (5-6 h weekdays, ~8.9 h need)
the answer is 15-21%.

Running it the other way — what would each weekend night have to deliver to break even? For weekday
5.5 h and need 8.9 h, each of the two weekend nights would need **17.40 h of actual sleep.** Across all
nine parameter combinations the requirement ranges from 14.40 h to 20.23 h per night. Every one of these
exceeds the 10.4 h ceiling by a wide margin. **Weekend-only catch-up is not merely inefficient; for a
5-night deficit it is arithmetically impossible.**

And the subject's *reported* weekend sleep of 7-8 h is not catch-up at all — it is below need, so the
surplus is negative:

| Reported weekend TST | Need 8.4 h | Need 8.9 h |
|---:|---:|---:|
| 7.0 h | −2.80 h/weekend | −3.80 h/weekend |
| 7.5 h | −1.80 h/weekend | −2.80 h/weekend |
| 8.0 h | −0.80 h/weekend | −1.80 h/weekend |
| 10.5 h (his occasional long nights) | +4.20 h/weekend | +3.20 h/weekend |

On his typical weekend the debt **grows**. Only the occasional 10-11 h nights generate any surplus at all,
and even those cover roughly a fifth of one week's deficit.

### 4b. The empirical confirmations

**Depner 2019** (Current Biology, n = 36, mean age 25.5) tested this directly with ad-libitum weekend
recovery between weeks of 5 h sleep. Weekend catch-up totalled only **+1.1 h** of extra sleep against a
weekday deficit exceeding 12 h (≤9.2% repaid), with a large sex difference: men gained +2.1 h, women
+0.02 h. Even with 12.1 h of opportunity, maximum sleep was 10.2-10.3 h — one of the ceiling
measurements in §1d. Metabolically, weekend recovery failed to protect: whole-body insulin sensitivity
fell **9-27%** across groups, and the weekend-recovery group showed roughly a 13% decrease rather than
none. Energy intake rose **480-1130 kcal/day** above baseline, driven by after-dinner snacking. The
paper's title is the finding: ad-libitum weekend recovery sleep *fails* to prevent metabolic
dysregulation.

**Lo 2022** (n = 194 adolescents aged **15-19** — the closest population match available) ran two cycles
of weekday restriction with weekend recovery. Two nights at 9 h TIB did not restore vigilance, **deficits
were worse during the second restriction week than the first**, and 8 h TIB was the threshold needed to
prevent vigilance deficits accumulating. Daytime naps provided additional benefit.

**Smith 2021** ran six weekly cycles of 5 h weekdays / 8 h weekends. Vigilant attention declined
monotonically with cumulative debt (standardized β = −0.688, p < 0.001) and was explicitly "not restored
by two nights of weekend recovery sleep." Spatial orientation likewise (β = −0.289, p = 0.011). No
adaptation, no plateau — and structurally, an 8 h weekend equals need, so the surplus was exactly zero.

**Simpson 2016** ran three weeks of restriction-recovery cycles and found monocyte IL-6 still elevated and
the cortisol rhythm still dysregulated after weekend recovery, while subjective responses habituated —
the §3a dissociation again, now over multiple weeks.

### 4c. The one positive result, and its boundaries

**Killick 2015** is the sole study showing a substantial metabolic benefit from catch-up sleep: in 19 men
(mean 28.6 y) with ~5 years of lifestyle-driven weekday restriction (~6.2 h), **three** nights at 10 h
TIB improved insulin sensitivity by **45%** versus continued 6 h nights.

It is worth taking seriously — it says the metabolic damage of *years* of restriction is at least partly
reversible. But its boundaries are exactly the parameters this section is about: it used **three** nights,
not two, at **10 h TIB**, not ad-libitum, generating a real surplus above need; the metabolic endpoint is
one of the faster-recovering measures; and no vigilance outcome recovered in any comparable protocol. It
supports "a properly dosed recovery block helps metabolically", not "weekends are sufficient".

---

## Bottom line for the recovery prescription

1. **Repayment is not hour-for-hour and never close to it.** One recovery night repays 2-4% of a week's
   debt. The best-case measured repayment anywhere is 35%, from a mild debt with a 10 h opportunity.
2. **Opportunity converts to sleep at 0.73-0.98 h/h at first, ~0.38-0.60 h/h in real life, and ~0 at the
   ceiling.** Fifteen months of counselling bought 15 min/night (Lucassen 2014).
3. **The ceiling is ~10.4 h for one night and ~8.5 h sustained; nocturnal sleep alone saturates at
   7.9-8.1 h.** Reaching full capacity requires daytime sleep. Sixteen hours in bed yields 8.9 h of sleep
   and 7.1 h of lying awake.
4. **An 8 h night cannot repay debt** if need is 8.4-8.9 h — it only halts accumulation. Repayment
   requires time in bed *above* need, sustained.
5. **Sleep duration stabilizes in 4-14 days. Vigilance takes at least 2 weeks and plausibly 3-6 weeks,
   and no study has ever demonstrated its full recovery.** Prior chronic short sleep slows the trajectory
   further (Rupp 2009).
6. **Weekend-only catch-up can repay at most 10-25% of a 5-night deficit even at the physiological
   maximum, and break-even would require 14-20 h per weekend night.** It is arithmetically impossible,
   and three independent multi-week studies confirm deficits accumulate anyway.
7. **Subjective recovery precedes objective recovery, and does so most misleadingly in the young.** Track
   vigilance, not how rested the person feels.
