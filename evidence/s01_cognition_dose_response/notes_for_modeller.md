# Published functional forms for the accumulation of neurobehavioral deficit under chronic sleep restriction

Shard: `s01_cognition_dose_response`. Everything below is quoted verbatim from a source I retrieved and
read. Where I fitted or derived a parameter myself, it is labelled **DERIVED** and the arithmetic is
given. Nothing here is recalled from memory.

There are **six structurally different published functional forms**, and they are not
reparameterisations of each other. They disagree about whether deficit accumulates without bound,
whether it plateaus, whether the brain keeps a running "sleep debt" tally, and what recovery does.
Section 7 sets out the disagreement explicitly, because averaging over these forms would be a modelling
error.

**If you read only one section, read §10.** It is the only functional form in this file that is both
completely specified (all equations, all eight fitted parameters with standard errors) and validated
out-of-sample against studies it was not fitted to. It puts a number — **τ_LA = 7.00 ± 1.67 days** — on the
history-weighting fork that §7.1 otherwise has to leave open, and that number is the single strongest
argument in this shard against linearly extrapolating a 14-day accumulation slope to three years.

Contents: §1 Van Dongen power law and excess wakefulness · §2 Belenky asymptotic/core-sleep form ·
§3 McCauley bifurcating ODE system (full parameter set) · §4 Cohen slope-multiplier form ·
§5 Banks recovery dose-response (exponential) · §6 per-night accumulation rates · §7 how the forms
conflict · §8 dose thresholds by cognitive domain · §9 recommended parameterisation ·
**§10 the Unified Model of Performance — fully parameterised and out-of-sample validated** ·
**§11 age-matched adolescent per-hour slopes** (the only place in this file where the dose-response
coefficients come from subjects the same age as our subject).

---

## 1. Van Dongen et al. 2003 — power law in days (the primary dose-response form)

Source: Van Dongen HP, Maislin G, Mullington JM, Dinges DF. *Sleep* 2003;26(2):117-126.
doi 10.1093/sleep/26.2.117, PMID 12683469. Full text retrieved.

### 1.1 The model, verbatim

> "The following non-linear mixed-effects model was fitted to the neurobehavioral performance data y,
> expressed as difference from baseline, for each neurobehavioral assay:
>
> (1) y_t ~ β · t^θ
>
> where t denotes days of sleep restriction. The parameter β is a normally distributed random effect
> with condition-specific mean representing rate of change, used to quantify the build-up of
> neurobehavioral performance impairment across days of sleep restriction for each chronic sleep
> restriction condition. The parameter θ represents curvature in the response profile, which is
> necessary to accommodate any non-linearity in the metric of the outcome variable y. A single model was
> fitted for the three sleep restriction conditions, and a separate model was fitted for the total sleep
> deprivation condition."

Note carefully: `y` is **change from baseline**, and one model was fitted across the 8 h / 6 h / 4 h arms
jointly with **condition-specific means for β but a single shared θ per assay**. So in this
parameterisation **the dose enters only through β**, and the *shape* of accumulation over days is
assumed identical across doses. That is an assumption, not a finding, and it is the assumption McCauley
2009 later rejects.

### 1.2 Published θ (curvature) estimates, verbatim

> "For the 8 h, 6 h and 4 h sleep period conditions, curvature (parameter θ in equation (1)) was
> statistically estimated to be 0.78 ± 0.04 for psychomotor vigilance task performance, 0.59 ± 0.04 for
> digit symbol substitution task performance, and 0.45 ± 0.04 for serial addition/subtraction task
> performance (estimate ± s.e.). For the 0 h sleep condition, curvature was statistically estimated to
> be 0.57 ± 0.19 for psychomotor vigilance task performance, 0.74 ± 0.12 for digit symbol substitution
> task performance, and 0.67 ± 0.12 for serial addition/subtraction task performance (estimate ± s.e.).
> These values indicate that cognitive performance impairment accumulated near-linearly over days for
> all four experimental conditions"

> "The curvature for subjective sleepiness as assessed by the SSS was statistically estimated to be
> 0.86 ± 0.14 for the 0 h sleep condition, and 0.24 ± 0.04 for the 8 h, 6 h and 4 h sleep period
> conditions (θ estimate ± s.e.). Thus, the profile of subjective sleepiness across days was near-linear
> for the 0 h sleep condition, while it was near-saturating for the 4 h and 6 h sleep period conditions"

> "The curvature for KSS responses to sleep loss was statistically estimated to be 0.81 ± 0.16 for the
> 0 h sleep condition, and 0.16 ± 0.03 for the 8 h, 6 h and 4 h sleep period conditions (θ estimate ±
> s.e.). Thus, as with the SSS, the profile of subjective sleepiness rated on the KSS was near-linear
> across days for the 0 h sleep condition, while it was near-saturating for the 4 h and 6 h chronic
> sleep restriction conditions."

**θ table (all published, with published SEs), chronic restriction arms:**

| Assay | θ | s.e. | Reading |
|---|---|---|---|
| PVT lapses | 0.78 | 0.04 | near-linear, barely decelerating |
| DSST correct responses | 0.59 | 0.04 | moderately decelerating |
| Serial addition/subtraction | 0.45 | 0.04 | strongly decelerating, close to √t |
| Stanford Sleepiness Scale | 0.24 | 0.04 | "near-saturating" |
| Karolinska Sleepiness Scale | 0.16 | 0.03 | "near-saturating" |

**This table is the quantitative answer to the habituation question in the shard brief.** Same subjects,
same days, same model. The objective vigilance exponent is **0.78 / 0.24 = 3.25 times** the subjective
exponent (**DERIVED** ratio). Objective impairment keeps climbing nearly linearly while the subjective
signal flattens out. The dissociation is not that subjective sleepiness fails to rise — it does rise —
but that it *saturates* while performance does not, so the gap between how impaired someone feels and
how impaired they are **widens with every additional night**.

### 1.3 β estimates — NOT published numerically; **DERIVED** by curve tracing

The paper reports F tests on β but does not print the per-arm β values. I recovered them by tracing the
published best-fit curves in Figure 1 (raster image extracted from the PDF, axes calibrated on tick
labels, then least-squares fit of β with θ held at the published value). Script: `/tmp/lit/fitcurves.py`.
Cross-checked visually against an overlay of detected curve pixels.

| Assay | θ used | β(8 h) | β(6 h) | β(4 h) | fitted value at day 14: 8h / 6h / 4h |
|---|---|---|---|---|---|
| PVT lapses | 0.78 | 0.3341 | 1.2770 | 1.9087 | +2.62 / +10.00 / +14.95 |
| SSS sleepiness | 0.24 | 0.1498 | 0.5170 | 0.5596 | +0.28 / +0.97 / +1.05 |
| DSST correct | 0.59 | 2.0251 | 0.2505 | −1.0839 | +9.61 / +1.19 / −5.14 |
| SAST throughput | 0.45 | 0.8571 | 0.6364 | 0.0176 | +2.81 / +2.09 / +0.06 |

Sign conventions follow the figure: upward is *worse* for PVT and SSS, *better* for DSST and SAST.

**DERIVED dose slopes** (ordinary least squares of the four-row table above against TIB in hours, 3 dose
levels — a crude linear summary of a relationship that is not linear, provided because the brief asks
for a per-hour figure):

- PVT lapses: **d(β)/d(TIB h) = −0.263 lapses·day^−0.78 per hour of TIB**;
  **d(day-14 lapses)/d(TIB h) = −3.09 lapses per hour of TIB**
- SSS: d(day-14 SSS)/d(TIB h) = −0.19 SSS points per hour of TIB
- DSST: d(day-14 correct)/d(TIB h) = +3.69 responses per hour of TIB
- SAST: d(day-14 throughput)/d(TIB h) = +0.69 per hour of TIB

Note the PVT dose response is markedly **convex**: going 8→6 h costs 7.4 lapses at day 14, going 6→4 h
costs a further 5.0. Fitting a single per-hour slope across the 4-8 h range therefore *understates* the
cost of the first two hours lost and *overstates* the cost of the next two. **Use the three per-arm
points, not the slope.**

### 1.4 The excess-wakefulness model — the second, and more transportable, form

This is the form the paper's title refers to, and it is the one that unifies restriction with total
deprivation. Verbatim:

> "In the statistical model we developed, parameter ξ was defined as the (a priori unknown) critical wake
> duration (i.e., the postulated maximum period of stable waking neurobehavioral functioning).
> Cumulative excess wakefulness Σ in the 8 h, 6 h and 4 h sleep period conditions was then obtained by:
>
> (3a) Σ_t = (24 h – ξ) t – CTST_t
>
> where t denotes days of sleep restriction. The variable CTST_t represents cumulative total sleep time
> (measured polysomnographically) as a function of t. Over days of sleep restriction, cumulative excess
> wakefulness was equivalent to cumulative sleep loss relative to a critical daily sleep duration of
> 24 h – ξ. In the 0 h sleep condition, however, each day without sleep (beyond the critical wake
> duration ξ) added 24 h to the cumulative excess wakefulness. Thus, in the 0 h sleep condition,
> cumulative excess wakefulness Σ was given by:
>
> (3b) Σ_t = 24 h · t
>
> where again t denotes days of sleep restriction. A non-linear mixed-effects model was formulated to
> describe lapses in behavioral alertness as a function of cumulative excess wakefulness:
>
> (4) y_t ~ γ (Σ_t)^θ
>
> where y denoted PVT performance lapses (expressed as difference from baseline), and θ was a parameter
> quantifying curvature (as in equation (1)). The parameter γ was a normally distributed random effect
> representing the rate of increase in PVT lapses per hour of cumulative excess wakefulness. The critical
> wake duration ξ (i.e., the postulated maximum period of stable waking neurobehavioral functioning) was
> incorporated in equation (4), via equation (3a), as a second normally distributed random effect."

**Fitted parameters, verbatim:**

> "The statistically estimated value for ξ was 15.84 ± 0.73 h (estimate ± s.e.). For the subject
> population in our experiments, limiting daily wakefulness to this critical wake duration would be
> expected to prevent the build-up of neurobehavioral deficits. Accordingly, daily sleep need to prevent
> cumulative neurobehavioral deficits in these subjects would appear to be 24 h – ξ = 8.16 ± 0.73 h
> (estimate ± s.e.). The statistically estimated standard deviation over subjects for ξ was
> 3.58 ± 1.19 h (estimate ± s.e.); this standard deviation reflects considerable inter-individual
> variability in the postulated critical wake duration ξ."

> "Taking into account between-subjects variance in ξ and γ, the statistical model in equation (4)
> explained 83.0% of the variance in the PVT data (Figure 1A). The value for curvature θ was 0.67 ± 0.05
> (estimate ± s.e.). Thus, across days of sleep restriction, the build-up of psychomotor vigilance
> performance impairment in all four experimental conditions was well approximated by a single near-linear
> function of cumulative excess wakefulness."

> "When expressed as a function of cumulative sleep debt—the sum of all hours of sleep loss relative to
> the above-estimated subject-specific daily sleep need—the neurobehavioral response to chronic sleep
> restriction appeared to be fundamentally different than the neurobehavioral response to total sleep
> deprivation (Figure 4A). When expressed as a function of cumulative excess wakefulness, however, the
> neurobehavioral responses to chronic sleep restriction and to total sleep deprivation were well
> approximated by a single near-linear model (Figure 4B). This illustrates the monotonic,
> near-proportional relationship between cumulative excess wakefulness and neurobehavioral performance
> impairment irrespective of daily sleep ration in these experiments."

**This is the single most useful equation in the shard for our subject**, because it is the only
published form that handles a *mixed* schedule (weekday restriction + weekend catch-up + occasional
all-nighters) in one currency. Practical recipe:

```
critical daily sleep need  = 24 - ξ = 8.16 h   (s.e. 0.73; between-subject SD 3.58)
Σ  = Σ_over_days max(0, 8.16 - TST_that_day)   in hours     [restriction days]
Σ += 24 h per day of complete sleep loss                    [total deprivation days]
PVT lapse increase over baseline  =  γ · Σ^0.67
```

Two warnings. (a) **γ is a random effect and its mean is not printed in the paper.** I could not extract
it, and I have not invented it; it must be calibrated from the per-arm day-14 values in §1.3, or treated
as a free parameter with the ξ variance above. (b) The model has **no recovery term at all** — Σ is
monotone non-decreasing, so it cannot represent catch-up sleep. McCauley 2009 identifies exactly this as
its defining limitation: *"the excess wakefulness model is not useful for computational predictions of
neurobehavioral impairment, because it does not explicitly state how recovery from the effects of prior
sleep loss would be achieved."*

### 1.5 The practice-effect confound, from the same paper's own control arm

> "Subjects allowed an 8 h sleep period per night displayed only minor, non-significant increases in
> lapses of behavioral alertness over the 14 days. The statistically estimated mean of β in equation (1)
> for the 8 h sleep period condition was not significantly different from zero (t30 = 0.77, P = 0.45) for
> the psychomotor vigilance task (Figure 1A). Subjects in the 8 h sleep period condition demonstrated
> normal performance learning curves on the digit symbol substitution task (Figure 1C) and the serial
> addition/subtraction task (Figure 1D)."

And from the Figure 1 caption, on how the authors handled it:

> "For the DSST and SAST, these gray bands are curved parallel to the practice effect displayed by the
> subjects in the 8 h sleep period condition, to compensate for different amounts of practice on these
> tasks."

**DERIVED**, from my traced 8 h curves (§1.3): over 14 days at 9 test bouts per day, the 8 h control arm
drifted **+2.62 lapses** on the PVT but **+9.61 correct responses** on the DSST and **+2.81** on the SAST.
So DSST improvement from practice alone (+9.61) is *larger in magnitude* than the entire 4 h arm's
14-day decline (−5.14). **Any throughput-task trajectory must be practice-corrected or it is
uninterpretable; the PVT needs little correction.** Cohen et al. 2010 state the general principle
verbatim: *"The PVT does not display appreciable practice effects (34), making it an ideal test to compare
performance across protocols that have different frequencies of exposure to the task."*

### 1.6 One counter-intuitive covariate worth carrying

> "Partial correlation, controlling for experimental condition, revealed a modest but significant positive
> relationship between average sleep duration in the 5 days prior to the experiment and rate of increase
> in PVT lapses over the 14 days of sleep restriction (r32 = 0.29, P = 0.048). This suggests that those
> subjects who habitually slept longest tended to be more affected by the 14 days of imposed sleep
> restriction."

This partly offsets the Rupp 2009 banking result (prior extension *protects*): here longer habitual
sleepers *deteriorated faster* once restricted. The two are reconcilable if what matters is the deficit
relative to one's own need, but it means the sign of "prior sleep history" as a moderator is not settled.

---

## 2. Belenky et al. 2003 — asymptotic / core-sleep form (a plateau model)

Source: Belenky G, Wesensten NJ, Thorne DR, Thomas ML, Sing HC, Redmond DP, Russo MB, Balkin TJ.
*Journal of Sleep Research* 2003;12(1):1-12. doi 10.1046/j.1365-2869.2003.00337.x. Full text retrieved.

No equation is fitted, but the functional form is stated explicitly and it is a **different shape** from
Van Dongen's power law. Verbatim:

> "In this view, sleep durations that do not satisfy the core sleep requirement would, across days, result
> in continued degradation of alertness and performance; whereas sleep durations that satisfy the core
> requirement would produce deficits in alertness and performance relative to baseline, but degradation
> would not continue across days indefinitely – an asymptotic, stable level of reduced alertness and
> performance would eventually be achieved; and additional sleep (i.e. incremental increases in the
> duration of sleep beyond the core requirement) would produce correspondingly higher, and stable, levels
> of alertness and performance."

The observed pattern that motivates it, verbatim from the abstract:

> "In the 3-h group, speed (mean and fastest 10% of responses) on the psychomotor vigilance task (PVT)
> declined, and PVT lapses (reaction times greater than 500 ms) increased steadily across the 7 days of
> sleep restriction. In the 7- and 5-h groups speed initially declined, then appeared to stabilize at a
> reduced level; lapses were increased only in the 5-h group. In the 9-h group, speed and lapses remained
> at baseline levels."

And on recovery — the finding that most constrains any weekend-catch-up model:

> "During recovery, PVT speed in the 7- and 5-h groups (and lapses in the 5-h group) remained at the
> stable, but reduced levels seen during the last days of the experimental phase, with no evidence of
> recovery. Speed and lapses in the 3-h group recovered rapidly following the first night of recovery
> sleep; however, recovery was incomplete with speed and lapses stabilizing at a level comparable with
> the 7- and 5-h groups."

> "These results suggest that the brain adapts to chronic sleep restriction. In mild to moderate sleep
> restriction this adaptation is sufficient to stabilize performance, although at a reduced level. These
> adaptive changes are hypothesized to restrict brain operational capacity and to persist for several days
> after normal sleep duration is restored, delaying recovery."

> "chronic sleep restriction leads to long-time-constant changes that may have adaptive value, serving to
> stabilize performance. However, these adaptive changes appear to come at a cost – brain operational
> capacity is capped in a manner that apparently precludes rapid recovery to baseline levels of alertness
> and performance when sleep durations are extended to baseline levels. In contrast, rapid recovery to
> baseline is typical of performance following acute TSD."

**Implied functional form**: piecewise in dose. Above a "core requirement", deficit → a dose-dependent
plateau; below it, deficit grows without stabilising. This is qualitatively the same structure McCauley
2009 derives from first principles, and Belenky's own 3 h vs 5 h/7 h split brackets the threshold between
3 and 5 h TIB — consistent with McCauley's 3.8 h estimate.

**DERIVED per-arm numbers** (digitised from Figures 3, 4, 7; script `/tmp/lit/belenky_fig.py`; PVT lapses,
change from baseline at day 7 of restriction):
9 h **+0.04**, 7 h **+2.05**, 5 h **+4.72**, 3 h **+15.51**.
OLS across the four doses: **−2.45 lapses per hour of TIB**, or **−2.95 lapses per hour of PSG-verified
TST** (achieved TST was 7.93, 6.28, 4.66, 2.87 h for the 9/7/5/3 h arms). The relationship is strongly
convex — the 3 h arm alone accounts for most of the slope.

**Residual deficit retained after 3 recovery nights at 8 h TIB**, as a percentage of the day-7 deficit
(**DERIVED**): 7 h arm **112%**, 5 h arm **93%**, 3 h arm **38%**. The mild and moderate arms retained
essentially all of their deficit.

---

## 3. McCauley et al. 2009 — coupled ODEs with a bifurcation (reconciles §1 and §2)

Source: McCauley P, Kalachev LV, Smith AD, Belenky G, Dinges DF, Van Dongen HPA. *Journal of Theoretical
Biology* 2009;256(2):227-239. doi 10.1016/j.jtbi.2008.09.012, PMID 18938181. Full text retrieved.

### 3.1 The specific model examined, verbatim

> "We now consider a particular case of the model of Eqs. (11):
>
> (21a) [ṗₙ u̇ₙ] = [[α11, α12], [0, α22]] [pₙ uₙ] + [β1(t) β2(t)]  for t ∈ [tₙ, tₙ+Wₙ],
> (21b) [q̇ₙ v̇ₙ] = [[σ11, σ12], [0, σ22]] [qₙ vₙ] + [γ1(t) γ2(t)]  for t ∈ [tₙ+Wₙ, tₙ+Tₙ],
>
> where α11 < 0 and σ11 < 0, and where α11 ≠ α22 and σ11 ≠ σ22."

Here `p` is performance during wake, `q` performance during sleep, `u`/`v` the (moving) asymptotes, `W`
daily wake duration, `T` the wake/sleep cycle length. The whole novelty is that `α22 > 0` lets the
asymptote itself drift, which is what the two-process model forbids.

### 3.2 Fitted parameter estimates, verbatim (Eqs. 27)

> "Using least-squares regression on all 404 data points shown in Fig. 1a, we find the following
> parameter estimates: (27)
>
> [[α11, α12], [0, α22]] = [[−0.0135, 0.000929], [0, 0.00743]]
> [[σ11, σ12], [0, σ22]] = [[−2.17, 0.872], [0, −0.0397]]
> δ = 19.8, γ = 5.86, μ = 0.472, θ = 12.7, p₀(t₀) = 4.49, u₀(t₀) = 29.9"

with the circadian non-homogeneities defined as

> "(26a) [β1(t) β2(t)] = [γ·c(t−θ) + μ, 0] for t ∈ [tₙ, tₙ+Wₙ],
> (26b) [γ1(t) γ2(t)] = [γ·c(t−θ) + μ, 0] for t ∈ [tₙ+Wₙ, tₙ+Tₙ].
> Here γ and μ are parameters scaling the circadian process, and θ is a phase parameter shifting it in
> time."

(`c(t)` is the Borbély & Achermann 1999 circadian process. `t₀ = 7.5 h`, `T` and `τ` fixed at 24 h,
initial conditions set to the W = 16 h equilibrium.)

### 3.3 The bifurcation — the single most important threshold in this shard

> "Evaluation of Eq. (22) given the parameter estimates in Eqs. (27) indicates that there must be a
> bifurcation at Wc = 20.2h. That is, the model should flip from a state of convergence to a state of
> divergence when daily wakefulness is increased to more than 20.2h (i.e., when daily sleep is reduced to
> less than 3.8h)."

> "Thus, for α22 > 0, the model behavior is such that if the amount of wakefulness W in each wake/sleep
> cycle exceeds a critical threshold Wc, the model flips from a state in which performance predictions
> converge toward an asymptotically stable equilibrium, to a state in which performance predictions
> diverge away from an unstable equilibrium."

From the Figure 2 caption, the three regimes stated compactly:

> "For daily wake durations below this bifurcation threshold (green and yellow), the model converges to an
> asymptotically stable equilibrium, meaning that performance impairment ultimately levels off. For daily
> wake durations beyond the bifurcation threshold (gray and black), the model diverges from an unstable
> equilibrium, meaning that performance impairment tends to escalate. At exactly the bifurcation value
> W = Wc (red), there is no equilibrium state, resulting in an asymptotically linear build-up of
> performance impairment across days."

That last clause matters for reading §1: **Van Dongen's apparently linear 4 h accumulation is what a
system sitting essentially *at* its bifurcation looks like** (4 h sleep ≈ 20 h wake ≈ Wc = 20.2 h), not
evidence of genuinely unbounded linear growth.

### 3.4 Fit quality and out-of-sample validation, verbatim

> "With the parameter estimates of Eqs. (27), the model explains 72.4% of the variance in the group-average
> data of Fig. 1a. It fits substantially better to the data than the original two-process model (Fig. 1b,
> explained variance 22.6%) and the extended two-process model (Fig. 1c, explained variance 38.4%)."

> "Applying linear scaling to account for any irrelevant differences in absolute performance outcomes
> (e.g., due to variations in population characteristics or performance testing conditions), we find the
> scaling factor to be 1.17—suitably close to 1. The corresponding performance predictions are shown in
> Fig. 4b. They explain 72.2% of the variance in the data, and fit well to the observed performance
> changes across days."

Note the second quote: parameters fitted to Van Dongen's 4/6/8/0 h data transferred to Belenky's 3/5/7/9 h
data with only a scale factor. That is real cross-study transportability of a single dose-response surface.

### 3.5 The model's structural claim about "sleep debt", verbatim

> "In our new model class (which encompasses the original two-process model and other models based upon
> it), performance is actually a function of the prevailing wake/sleep ratio. Provided the duration of
> wakefulness does not exceed the critical threshold Wc, performance predictions converge across days from
> the present performance level to the applicable steady state (i.e., asymptotically stable equilibrium).
> Sleep/wake history is fully represented by the current performance level (p or q) and the current level
> of the asymptote (u or v), and past amounts of sleep and wake have no further impact beyond the present.
> In this view, the brain does not need to maintain a running tally of sleep and wakefulness—it does not
> need to keep track of a 'sleep debt' (cf. Dement, 2006)."

### 3.6 Mechanism, with an age-transportability warning

> "SWA during sleep is substantially preserved when wake duration is no greater than ~20h per day
> (Brunner et al., 1993; Van Dongen et al., 2003). However, when daily wakefulness is extended beyond
> ~20h, then insufficient time for sleep remains to fully express SWA (see Van Dongen and Dinges, 2003b).
> The reduction in SWA could be related to the qualitative change in the effects of sleep loss on
> neurobehavioral performance when wakefulness is extended beyond the critical wake duration Wc."

If Wc is set by how much sleep time is needed to express a given quantity of slow-wave activity, then Wc
is **age-dependent**, because adolescent SWA is substantially higher than adult SWA. **No paper I could
find calibrates Wc in adolescents.** Treat 3.8 h as an adult figure with unknown adolescent offset.

### 3.7 Successor model (abstract only — no parameters extracted)

McCauley P, Kalachev LV, Mollicone DJ, Banks S, Dinges DF, Van Dongen HPA. *Sleep*
2013;36(12):1987-1997. doi 10.5665/sleep.3246, PMID 24293775. Adds time-dependent circadian amplitude
without adding parameters. Verbatim from the abstract:

> "The updated model predicts that the homeostatic equilibrium for sleep/wake regulation—and thus
> sensitivity to sleep loss—depends not only on the duration but also on the circadian timing of prior
> sleep."

Only the abstract is in PMC; **I did not extract equations or parameters from it and none should be
attributed to it here.**

---

## 4. Cohen et al. 2010 — a two-process form in which the chronic term acts on the *slope*

Source: Cohen DA, Wang W, Wyatt JK, Kronauer RE, Dijk DJ, Czeisler CA, Klerman EB. *Science Translational
Medicine* 2010;2(14):14ra3. doi 10.1126/scitranslmed.3000458, PMID 20371466. Full text retrieved.

This is a **fourth structure**, and the only one supported by data that separates time-awake from
circadian phase. Verbatim:

> "When the chronic sleep loss data were fit with a linear model, there was no significant difference
> across weeks of the protocol in the y-intercept, which reflects the theoretical effect of acute
> homeostatic sleep pressure at awakening, ignoring the impact of sleep inertia (10). This is not
> consistent with the single homeostatic process predictions. However, there was a marked increase in
> slope after the first week, reflecting slower reaction times with increasing hours awake (1st week:
> slope = 24 msec/hour awake; 2nd week: slope = 69 msec/hour awake; 3rd week: slope = 65 msec/hour
> awake). The differences in slope between the 1st and 2nd weeks were significant (p<0.0001)."

> "This analysis indicates that the 10-hour sleep opportunities in the chronic sleep loss protocol were
> sufficient to dissipate an acute homeostatic process to baseline levels in this task even during the 3rd
> week, but a separate chronic sleep homeostatic process accelerated the performance deterioration over
> consecutive hours awake."

Implied form: `deficit(h, weeks) = intercept + slope(weeks) · h`, with the chronic exposure entering
**multiplicatively on hours awake** rather than additively on level. The slope roughly tripled (24 → 69
ms/h) and then held (65 ms/h in week 3) — i.e. it converged to a plateau, consistent with §3 at a dose
(5.6 h-equivalent) above the bifurcation.

Supporting levels, verbatim:

> "When comparing the first PVT results at 2 hours awake, performance was near baseline levels across all
> three weeks of chronic sleep loss (two baseline days: median RT = 256msec; 1st week: median RT =256msec;
> 2nd week: median RT = 278msec; and 3rd week: median RT = 291msec), and not significantly different from
> the control data with a 1:2 sleep:wake ratio (1st week: 270msec; 2nd week: 305msec; 3rd week: 309msec;
> p=0.42). In contrast, when comparing the last performance test of each wake episode, which was
> administered at 30 consecutive hours awake, there was a dramatic increase in median RT between the first
> and second weeks on the chronic sleep loss protocol (1st week: median RT = 667ms; 2nd week: median RT =
> 1,954msec; 3rd week: median RT = 2,013msec)."

**Modelling consequence, and it is a big one.** If the chronic term is a slope multiplier, then *time of
day at measurement* is a first-order moderator, not a nuisance. Same subjects, same weeks: **+13.7%** at
2 h awake versus **+193%** at 30 h awake (**DERIVED** from the medians above). Any impairment estimate for
our subject that is calibrated on morning testing will understate his evening impairment by roughly an
order of magnitude.

---

## 5. Banks et al. 2010 — the recovery dose-response function (exponential in dose)

Source: Banks S, Van Dongen HPA, Maislin G, Dinges DF. *Sleep* 2010;33(8):1013-1026.
doi 10.1093/sleep/33.8.1013, PMID 20815182. Abstract only (no PMC body deposit, no OA copy located), so
**no fitted coefficients could be extracted — only the functional form and the incompleteness result.**

This is the only randomised dose-response experiment on *recovery* sleep: 159 healthy adults, five nights
at 4 h TIB, then randomised to one of six single-night recovery doses (0, 2, 4, 6, 8 or 10 h TIB), against
a 10 h TIB control arm. Verbatim:

> "While TST, stage 2, REM sleep and NREM slow wave energy (SWE) increased linearly across recovery sleep
> doses, best-fitting neurobehavioral recovery functions were **exponential** across recovery sleep doses
> for PVT and KSS outcomes, and **linear** for the MWT."

> "Analyses based on return to baseline and on estimated intersection with control condition means revealed
> recovery was **incomplete at the 10 h TIB (8.96 h TST)** for PVT performance, KSS sleepiness, and POMS
> fatigue. Both TST and SWE were elevated above baseline at the maximum recovery dose of 10 h TIB."

> "Neurobehavioral deficits induced by 5 nights of sleep restricted to 4 h improved monotonically as acute
> recovery sleep dose increased, but some deficits remained after 10 h TIB for recovery. Complete recovery
> from such sleep restriction may require a longer sleep period during 1 night, and/or multiple nights of
> recovery sleep. It appears that acute recovery from chronic sleep restriction occurs as a result of
> elevated sleep pressure evident in both increased SWE and TST."

**Three modelling consequences:**

1. **Recovery is concave in dose; sleep physiology is linear in dose.** Behaviour saturates while sleep
   architecture keeps filling in proportionally. So the marginal value of recovery hours falls, and our
   subject's occasional 10-11 h weekend nights sit in the flat region — not worthless, but inefficient.
2. **Recovery is monotone with no threshold.** Every extra hour helps. Weekend sleep can be modelled as
   partially restorative on a concave function, not as all-or-nothing.
3. **Inferring behavioural recovery from sleep physiology is systematically optimistic.** Yamazaki 2021
   confirms this from the other direction: PSG-measured sleep had normalised by recovery night 4 (R1 was
   *"longer and of higher efficiency and better quality than R4"*) while PVT lapses and response speed
   *"failed to completely recover."*

**How much recovery is enough? Every window so far tested is insufficient**, and this is now consistent
across six laboratories:

| Recovery window | Dose | Result for PVT | Source |
|---|---|---|---|
| 1 night | up to 10 h TIB (randomised 6-dose ladder) | incomplete | Banks 2010 |
| 2 nights | unspecified | claimed sufficient — the only optimistic result, from an unspecified subset | Dinges 1997 |
| 2 nights, repeated weekly × 6 weeks | 8 h TIB weekends | *"not restored"* | Smith 2021 |
| 3 nights | 8 h TIB | 93–112% of the 5 h/7 h-arm deficit retained (**DERIVED**) | Belenky 2003 |
| 4 nights | 12 h TIB | lapses and response speed *"failed to completely recover"* | Yamazaki 2021 |
| 7 nights | 8 h TIB | *"return to the baseline for sleepiness and median reaction time, but not for lapses"* | Axelsson 2008 |

**A weekend does not clear a week's vigilance deficit.** This is the single most robust recovery finding in
the shard, and Smith 2021 tested it in exactly our subject's schedule shape.

Yamazaki 2021 adds a refinement that bears on §7: **what fails to recover depends on the exposure type.**
After chronic restriction it is PVT lapses and speed; after 36 h total deprivation it is subjective vigor,
with PVT recovering. Verbatim: *"PVT impairments from SR failed to reverse completely; by contrast, vigor
did not recover after TSD; all other deficits were reversed after sleep loss."* That is direct evidence
against the excess-wakefulness unification (§1.4), which predicts a single common currency.

---

## 6. Per-night accumulation rates that can be used directly

The cleanest published per-night coefficients, all as reported (no conversion), for use as priors on the
accumulation rate:

| Source | Dose | Outcome | Rate per night | s.e. |
|---|---|---|---|---|
| Axelsson 2008 (n=9, adults) | 4 h TIB × 5 | PVT lapses/test | **+0.69** | 0.16 |
| Axelsson 2008 | 4 h TIB × 5 | KSS sleepiness (9-pt) | **+0.64** | 0.05 |
| Axelsson 2008 | 4 h TIB × 5 | PVT median RT (ms) | **+6.6** | 1.6 |
| Lo 2016 (n=56, **adolescents**) | 5 h TIB × 7 | PVT lapses (**DERIVED**, OLS on digitised M1–M7) | **+2.51** | — |
| Lo 2016 control arm | 9 h TIB × 7 | PVT lapses (**DERIVED**) | **+0.10** | — |
| Lo 2016 net (SR − control) | 5 h vs 9 h TIB | PVT lapses (**DERIVED**) | **+2.41** | — |

Axelsson's verbatim source sentence:

> "The mixed-effect regression models showed that each day of restricted sleep resulted in an increase of
> sleepiness by 0.64+/- .05 KSS units (a nine-step scale, p < .001), increase of median reaction times of
> 6.6+/- 1.6 ms ( p = .003), and increase of lapses/test of 0.69 +/- .16 ms ( p < .001)."

(The "ms" on the lapse coefficient is a typo in the published abstract; the outcome is lapses per test.)

**The adolescent rate is 3.5× the adult rate at a milder dose** (+2.41 lapses/night at 5 h TIB in
16-year-olds versus +0.69 lapses/night at 4 h TIB in 23-28-year-olds). This is the largest single
age-transportability signal in the shard and it points the same way as Lo 2016's own adult comparison.
Both are cross-study comparisons with different labs and tasks, so treat the *direction* as well
supported and the *factor* as soft.

---

## 7. The forms disagree. Do not average them.

| | accumulation over days | plateau? | sleep-debt bookkeeping | recovery |
|---|---|---|---|---|
| **Van Dongen power law** (§1.1) | β·t^θ, θ≈0.78 for PVT | no, never | implicit in t | not represented |
| **Van Dongen excess wakefulness** (§1.4) | γ·Σ^0.67, Σ monotone ↑ | no | **yes, unweighted tally** | **cannot represent it** |
| **Belenky core sleep** (§2) | grows then flattens above core need | **yes, dose-dependent** | no | slow, "several days", incomplete |
| **McCauley bifurcation** (§3) | converges below Wc, diverges above | **yes, if W < Wc = 20.2 h** | **no — explicitly denies it** | modest improvement after a better night |
| **Cohen two-process** (§4) | slope multiplier rises then flattens | yes, in the slope | no | full acute discharge each night; chronic term persists |
| **Rajdev unified** (below) | two-process + recency-weighted debt | not stated in abstract | **yes, recency-weighted** | reproduces slow CSR recovery and banking |
| **UMP, parameterised** (§10) | 1 − e^(−t/τ_LA), **τ_LA = 7.00 ± 1.67 d** | **yes — ~95% by day 21** | **yes, exponentially recency-weighted** | limited by extant debt; debt floor −0.11 vs ceiling +1 |

### 7.1 The history-weighting fork, which matters most for a three-year exposure

Rajdev P, Thorsley D, Rajaraman S, Rupp TL, Wesensten NJ, Balkin TJ, Reifman J. *Journal of Theoretical
Biology* 2013;331:66-77. doi 10.1016/j.jtbi.2013.04.013, PMID 23623949. **Abstract only** — paywalled at
Elsevier, not in PMC, Unpaywall reports no OA location. **I could not extract a single equation or
coefficient from this paper, so nothing here should be implemented from it.** Verbatim from the abstract:

> "we developed a unified mathematical model that incorporates extant sleep debt as a function of a known
> sleep/wake history, **with recent history exerting greater influence**. This incorporation of sleep/wake
> history into the classical two-process model captures an individual's capacity to recover during sleep as
> a function of sleep debt and naturally bridges the continuum from CSR to TSD by reducing to the classical
> two-process model in the case of TSD."

> "this model better accounted for the relatively slow recovery process that is known to characterize CSR,
> as well as the enhanced performance that has been shown to result from sleep banking."

The three published positions on how history enters, and what each implies for our subject:

| Form | How history enters | Implication for a 3-year exposure |
|---|---|---|
| Van Dongen excess wakefulness (§1.4) | unweighted cumulative sum | deficit reflects **all ~1,000+ short nights**; would be enormous |
| McCauley bifurcation (§3.5) | present state only | deficit reflects **current wake/sleep ratio only**; duration irrelevant |
| Rajdev unified | recency-weighted | deficit reflects roughly **the last few weeks** |

**No experiment in this shard runs long enough to discriminate between these.** The longest is Smith 2021 at
six weeks. This is irreducible structural uncertainty and is the single largest reason to carry wide
intervals on any three-year extrapolation. Do not silently pick one.

**Partial resolution — the recency-weighted arm now has a number (see §10).** Ramakrishnan et al. 2016
(*Sleep* 39(1):249-262, PMID 26518594, full text retrieved) fit exactly this model class to Belenky 2003's
four dose arms and published every parameter with a standard error, including the debt time constant
**τ_LA = 7.00 (1.67) days**. That converts "recent history exerts greater influence" from a qualitative claim
into a quantified exponential with an e-folding time of one week: **63% of the asymptotic deficit by day 7,
86% by day 14, 95% by day 21**, and between 94.6% and 99.97% by day 30 across the parameter's whole 95%
interval (3.73–10.27 d). So two of the three positions in the table above — recency weighting and pure
state-dependence — now both predict that a three-year exposure yields essentially the same neurobehavioural
state as a three-week exposure at the same dose. Only the unweighted-cumulative form predicts continued
growth, and it is the only one of the three with **no fitted decay parameter at all**. The fork is not closed,
but it is no longer symmetric: the weight of the *parameterised* evidence favours saturation.

### 7.2 The sharpest empirical conflict: recovery

The sharpest conflict is about **recovery**, and McCauley 2009 states it explicitly:

> "However, the excess wakefulness model and the model introduced in the present paper make contradictory
> predictions for performance impairment after a period of chronic sleep restriction followed by a limited
> amount of recovery sleep (Fig. 6)."

with the two predictions spelled out in the Figure 6 caption:

> "(a) Predictions for performance changes across days according to the excess wakefulness model (Van
> Dongen et al., 2003). This model predicts that performance deteriorates progressively across the five
> days with 20h wake/4h sleep, and continues to deteriorate at a slower rate following the day with 18h
> wake/6h sleep. (b) Predictions for performance changes across days according to the model defined by
> Eqs. (21), (26) and (27). This new model also predicts that performance deteriorates progressively
> across the five days with 20h wake/4h sleep, but forecasts a modest relative performance improvement
> following the day with 18h wake/6h sleep."

**This is unresolved in the literature and it is exactly the case our subject occupies** — weekday
restriction punctuated by longer weekend sleep. Carry it as structural uncertainty (e.g. model averaging
over §1.4 and §3 with a wide prior), not as a settled choice.

**Where the empirical evidence actually leans, on the narrow recovery question:** toward incomplete
recovery, and against the optimistic reading. Belenky 2003 found 93–112% of the 5 h/7 h arms' lapse
deficit still present after **3** nights at 8 h TIB; Axelsson 2008 found lapses still not normalised after
**7** nights at 8 h TIB; Lo 2017 found incomplete recovery after 2 nights in adolescents; Lo 2019 found
*further* deterioration in a second restriction week despite intervening recovery nights. Only Dinges 1997
suggests 2 nights suffice, from an unspecified subset. **A weekend does not clear a week's deficit.**

---

## 8. There is no single dose threshold — it differs by cognitive domain

Source: Campbell IG, Kurinec CA, Zhang ZY, Cruz-Basilio A, Figueroa JG, Bottom VB, Whitney P, Hinson JM,
Van Dongen HPA. *Sleep* 2024;47(12):zsae216. doi 10.1093/sleep/zsae216, PMID 39283917. Abstract only
(PMC12477114 has no body deposit; no OA copy located), so **no magnitudes are available — only the
threshold structure.**

This is the only ≥3-dose within-subject chronic-restriction experiment in adolescents that ladders the
**mild** dose range, and it is the only evidence anywhere in this shard on the 7–10 h segment of the curve.
Design: 7, 8.5 or 10 h TIB for four consecutive nights, every participant completing all three conditions;
two cohorts (n = 77 aged 9.9–16.2 studied annually for 3 years; n = 82 aged 15–22.8). Verbatim:

> "Restricting TIB to 7 hours was associated with impaired top-down attentional control and cognitive
> flexibility, but performance did not differ between 8.5 and 10 hours of TIB conditions. **Psychomotor
> vigilance test performance decreased as TIB was restricted from 10 to 8.5 hours and decreased further with
> restriction to 7 hours.** Sternberg test measures of working memory were not significantly affected by TIB
> restriction."

> "The effects of sleep loss on these cognitive measures did not change significantly with age, but
> age-related improvement in many of the measures may compensate for some sleep loss effects. The findings
> here do not indicate an adolescent decrease in sleep need; however, **the minimal duration of sleep needed
> for optimal performance appears to differ depending on the cognitive measure.**"

**Implied threshold structure, in adolescents:**

| Outcome | Behaviour across 10 → 8.5 → 7 h TIB | Implied minimum dose |
|---|---|---|
| PVT (vigilance) | graded decline at every step, no floor found | **> 10 h**, or at least no threshold in range |
| Top-down attentional control, cognitive flexibility | flat 10 → 8.5, impaired at 7 | ~8.5 h |
| Working memory (Sternberg) | no significant effect at any dose | ≤ 7 h |

Three consequences. First, **a model with one shared sleep-need parameter across cognitive outcomes is
mis-specified** — the authors say so explicitly. Second, **our subject's 7–8 h weekend sleep is already on
the descending limb for vigilance**, so his deficit is not confined to weekdays. Third, the domain ordering
(vigilance most sensitive → executive control intermediate → working memory least) now replicates across
five independent lines of evidence: Van Dongen 2003's accumulation exponents (§1.2), Lim & Dinges 2010's
pooled TSD estimates, Lowe 2017's pooled restriction estimates, Smith 2021's six-week battery (only
vigilant attention and spatial orientation of ten domains moved), and this study.

Two companion papers from the same programme and cohort, screened and reported here but **not** given
separate evidence records because they would double-count the sample:

- Campbell IG, Burright CS, Kraus AM, Grimm KJ, Feinberg I. *Sleep* 2017;40(5):zsx046, PMID 28419388.
  Same 7/8.5/10 h protocol, n = 77 aged 9.9–14, MSLT and KSS outcomes. Note the design caveat that applies
  to the whole programme: *"The order in which they completed the schedules was not randomized but was
  accounted for in all statistical analyses."*
- Campbell IG, Van Dongen HPA, Gainer M, Karmouta E, Feinberg I. *Sleep* 2018;41(12):zsy177, PMID 30169721.
  n = 76, longitudinal. Reports an adolescent-specific subjective/objective dissociation worth carrying:
  *"MSLT-measured daytime sleepiness decreased with longer TIB and increased with age. The TIB and age
  effects interacted such that the TIB effect decreased with age. PVT performance improved with longer TIB
  and improved with age, but the benefit that increased TIB conferred on PVT performance did not change with
  age."* So across adolescence the **sleepiness** response to dose attenuates while the **vigilance**
  response to dose does not — the felt signal weakens with age while the measured cost does not.

### 8.1 The accumulation slope is not stationary across weeks

Four studies, three laboratories, both age groups: a second week of restriction is worse than the first
*despite* intervening recovery nights.

- **Lo 2017** (adolescents, 5 h TIB): *"worse this Monday than last Friday, p = .02"* and *"the rate of
  deterioration was faster during the second period of sleep restriction than the first period."*
- **Lo 2019** (adolescents, 6.5 h continuous or 5 h + nap): *"Both groups showed further deterioration in
  performance during the second sleep restriction period (e.g. SR13 vs. SR23: p = 0.02 and 0.03)."*
- **Koa 2024** (young adults, 6 h TIB weekdays / 8 h weekends, randomised, PMID 38219041,
  doi 10.1093/sleep/zsae010): *"The stable short sleep group showed faster vigilance deterioration in the
  second week of sleep restriction as compared to the first. This effect was not observed in the variable
  short sleep group."*
- **Smith 2021** (midlife adults, 5 h weekdays / 8 h weekends, six weekly cycles): deficits *"not restored
  by two nights of weekend recovery sleep."*

**A three-year exposure therefore cannot be modelled as a fixed-slope repetition of one week.** Whatever
form is chosen needs a slowly moving state variable; McCauley's drifting asymptote (§3.1, `α22 > 0`) is the
natural candidate.

### 8.2 Total sleep time is not a sufficient exposure statistic

Two independent demonstrations that *distribution* carries information beyond the total:

- **Lo 2019**: the split-sleep arm slept **15–21 min less** per 24 h than the continuous arm yet had
  *"fewer vigilance lapses, better working memory and executive function, faster processing speed, lower
  level of subjective sleepiness, and more positive mood, even though PSG-verified total sleep time was less
  than the continuous sleep group."*
- **Koa 2024**: the two short-sleep arms had **matched weekly totals** (stable 6+6+6+6+6 = 30 h; variable
  8+4+8+4+6 = 30 h) but only the stable arm showed week-2 vigilance ratcheting.

A dose-response function keyed purely on mean nightly TST will mis-price any schedule containing naps or
night-to-night variability.

### 8.3 Practice effects run in both directions

The shard brief asks about practice as a confound. It is worse than a simple upward bias:

- **Restriction suppresses learning.** Koa 2024: *"Subjective alertness and **practice-based improvement in
  processing speed** were attenuated in both short sleep groups."* So on throughput tasks the
  restricted-vs-control gap conflates acute impairment with failure to learn at the normal rate. These are
  different constructs and a difference score cannot separate them.
- **The magnitude is large on throughput tasks.** Van Dongen 2003's 8 h control arm gained **+9.61** DSST
  correct responses over 14 days (**DERIVED**, §1.3) — larger in magnitude than the entire 4 h arm's 14-day
  decline of −5.14.
- **The PVT is the exception and that is why it is the primary outcome.** Van Dongen's 8 h arm drifted only
  **+2.62** lapses over 14 days at 9 bouts/day, and its β was not significantly different from zero
  (t30 = 0.77, P = 0.45). Cohen 2010: *"The PVT does not display appreciable practice effects (34)."*

**Rule: use PVT lapses or mean 1/RT. Treat any DSST or serial-addition trajectory as uninterpretable without
an explicitly modelled learning curve.**

---

## 9. Recommended parameterisation for our subject, and what it rests on

Our subject: 18-year-old male, weekday TIB ≈ 5–6 h from age 16 to 19, weekend/holiday 7–8 h, occasional
3–4 h pre-exam nights, occasional 10–11 h weekend nights.

1. **Use the excess-wakefulness currency (§1.4) as the exposure metric**, because it is the only published
   form that accepts a heterogeneous schedule. Set critical daily sleep need at 8.16 h (s.e. 0.73,
   between-subject SD 3.58 h). Note this makes his weekday deficit ≈ 2.2–3.2 h/night of excess wakefulness.
2. **But cap it with a plateau (§2/§3)**, because Σ is monotone and would otherwise predict unbounded
   growth over three years, which no experiment supports and which McCauley 2009 argues against on
   dynamical grounds. His weekday dose (5–6 h) is **above** Wc = 3.8 h, i.e. in the *convergent* regime —
   predicting a deficit that plateaus at a dose-dependent, still-impaired level rather than growing
   without limit.
3. **Treat the pre-exam 3–4 h nights separately**, as they fall at or below Wc, in the *divergent* regime,
   and Cohen 2010 shows acute loss on a chronically loaded substrate is ~3× more damaging than the same
   acute loss when rested (667 → 1,954 ms at 30 h awake, week 1 → week 2).
4. **Anchor the magnitude on the per-arm day-14 values in §1.3**, not on a per-hour slope — the dose
   response is convex over 4–8 h.
5. **Inflate for adolescence.** Lo 2016 (exact age match, 16.6 ± 1.1 y) gives Hedges' **|g| = 1.79 at
   night 5 rising to 2.40 at night 7** for PVT lapses at 5 h vs 9 h TIB (2.31 on the baseline-unadjusted
   night-7 contrast), versus **|g| = 1.44 (SE 0.49)** for Van Dongen's adults at the *harsher* 4 h dose
   after *twice* as many nights. Magnitudes only — the sign convention differs between the two records
   because the constructs differ. Direction is solid; the factor is soft, because the two comparisons
   differ in dose, duration, task version and laboratory simultaneously. Both numbers are figure-digitised
   and their full arithmetic is in the `conversion_formula` of the respective records.
6. **Use PVT lapses or mean 1/RT as the outcome.** Not median RT (Basner & Dinges 2011: *"PVT mean and
   median metrics, which are among the most widely used outcomes, should be avoided as primary measures of
   alertness"*), and not DSST/serial-addition throughput without practice correction (§1.5).
7. **Do not use his subjective sleepiness as a proxy for anything.** θ_SSS = 0.24 vs θ_PVT = 0.78 (§1.2);
   Rupp 2009 found zero subjective group difference where PVT and MWT both found significant ones; Van
   Dongen 2004 found subjective and objective vulnerability load on *separate* trait dimensions.
8. **Widen the individual-level interval substantially.** Van Dongen 2004: vulnerability is trait-like,
   stable across sessions weeks apart, and unpredicted by baseline performance. Axelsson 2008 puts one
   between-subject SD at **3.2 nights of 4 h TIB** for lapses. Van Dongen 2003 puts the between-subject SD
   of critical wake duration ξ at **3.58 h**. For a single named person, that person-level term likely
   dominates the group dose-response uncertainty.
9. **Do not credit the weekends with clearing the weekday deficit.** Smith 2021 ran exactly this schedule
   shape — 5 h weekdays, 8 h weekends, six weekly cycles — and the vigilance deficit was *"not restored by
   two nights of weekend recovery sleep."* Five other studies bound recovery the same way (§5 table). Model
   weekend sleep as **partially** restorative on a concave function (§5), not as a reset.
10. **Give the weekend dose its own (smaller) deficit term rather than treating 7–8 h as neutral.** Campbell
   2024 found PVT performance degraded going from 10 h to 8.5 h TIB in adolescents, and further at 7 h (§8).
   There is no safe vigilance threshold in the range his weekends occupy.
11. **Let the accumulation slope grow across weeks, not just the level.** Four studies show week 2 is worse
   than week 1 and deteriorates faster (§8.1). A fixed-slope weekly repetition will understate a three-year
   exposure.
12. **Use separate thresholds per cognitive outcome, and expect most domains to be spared.** Vigilance
   degrades from 10 h down; executive control has a threshold near 8.5 h; working memory was unaffected at
   any dose tested (§8). Over six weeks at 5 h weekdays, 8 of 10 domains in a full battery showed no
   significant effect (Smith 2021). A single "global cognition" decrement would be both too broad and, for
   vigilance specifically, far too small — the pooled slope in Smith 2021 was only 18% of the
   vigilant-attention slope.
13. **Carry the history-weighting fork as explicit structural uncertainty (§7.1).** Unweighted accumulation,
   pure state-dependence, and recency weighting give materially different three-year answers, and no
   experiment is long enough to choose between them. **But see §10** — the recency-weighted arm of that fork
   is now quantified at τ_LA = 7.00 ± 1.67 d, which means it predicts ~95% saturation within three weeks.
14. **If you implement exactly one dynamic model, implement the UMP of §10, and treat its saturation as the
   central case.** It is the only form here fitted to one study and then validated on 14 conditions from five
   other studies in four other laboratories without refitting. Its τ_LA = 7 d implies the neurobehavioural
   deficit is ~63% saturated by day 7, ~86% by day 14 and ~95% by day 21 on a fixed schedule. Under any value
   in its 95% interval (3.7–10.3 d), saturation at one month is between 94.6% and 99.97% complete. Adopting
   this as the central case, with McCauley's bifurcation (§3.3) as the pessimistic alternative, spans the
   plausible range better than any single form.
15. **Use the age-matched slopes in §11 for the level, and the adult forms only for the shape in time.** The
   only per-hour coefficients in this file measured in adolescents are Campbell's
   **0.24 dB PVT log-SNR per hour of TIB** and **0.56 ± 0.07 KSS points per hour of TIB**, plus Short's
   **9.35 h** modelled adolescent requirement. Every dynamic form in §§1–5 and §10 is calibrated exclusively
   on adults; none has ever been fitted to adolescent data. Combining an adolescent level with an adult time
   course is the least-bad option available, and the mismatch should be stated as a limitation rather than
   hidden inside a pooled estimate.
16. **Convert TIB to sleep before applying any per-hour slope.** Campbell 2019 measured
   **41.5 ± 0.8 min of PSG sleep per hour of TIB** in adolescents — 69% efficiency (§11.3). Van Dongen 2003,
   Belenky 2003, Lo 2016 and the Campbell series all express dose as *time in bed*; Short 2018's 9.35 h and
   the UMP's debt scale are in *sleep*. Mixing the two axes without this factor is a silent ~45% error.

---

## 10. Ramakrishnan et al. 2016 — the Unified Model of Performance (UMP): the recency-weighted debt form, **fully parameterised and validated out of sample**

Source: Ramakrishnan S, Wesensten NJ, Balkin TJ, Reifman J. *A Unified Model of Performance: Validation of
its Predictions across Different Sleep/Wake Schedules.* **Sleep** 2016;39(1):249-262.
doi 10.5665/sleep.5358, PMID 26518594. **Full text retrieved** (Europe PMC PDF render, PMC4678351).

This is the paper that closes the gap left open in §7.1. The Rajdev et al. 2013 model discussed there was
retrievable only as an abstract, so its recency-weighting had no numerical value attached. This paper is the
same model family, **fitted to Belenky 2003's four-arm dose-response data and then used to predict 14
conditions from five other studies in four other laboratories with no refitting.** It is therefore the only
form in this file whose parameters are both complete and externally tested.

### 10.1 The governing equations, verbatim from Table 2

> **Performance impairment (P):**
> P(t) = S(t) + κC(t)  (1)
> where C and S denote the circadian and homeostatic processes of the two-process model at time t,
> respectively, and κ represents the circadian amplitude.
>
> **Circadian process (C):**
> C(t) = Σ_{i=1}^{5} aᵢ sin[ i (2π/τ) (t + φ) ]  (2)
> where aᵢ, i = 1, …, 5, represent the amplitude of the five harmonics (a₁ = 0.97, a₂ = 0.22, a₃ = 0.07,
> a₄ = 0.03, and a₅ = 0.001), τ denotes the period of the circadian oscillator (~24 h), and φ denotes the
> circadian phase.
>
> **Homeostatic process (S):**
> dS(t)/dt = [U − S(t)] / τ_w  during wakefulness
> dS(t)/dt = [L(t) − S(t)] / τ_s  during sleep  (3)
> where U and L denote the upper and lower asymptotes of process S, respectively, τ_w and τ_s denote the time
> constants of the increasing and decreasing sleep pressure during wakefulness and sleep, respectively.
> S(0) = S₀ and L(0) = L₀ correspond to the initial state values for S and L, respectively.
>
> **Lower asymptote (L) of process S:**
> L(t) = U × Debt(t)  (4)
> where Debt denotes the sleep debt.
>
> **Sleep debt (Debt):**
> dDebt(t)/dt = [Loss(t) − Debt(t)] / τ_LA  (5a)
> Loss(t) = 1 during wakefulness ; Loss(t) = −2 during sleep  (5b)
> where τ_LA denotes the time constant of the exponential decay of the effect of sleep history on
> performance.

**The structural claim in one sentence, verbatim from the text:**

> "In the UMP, process S is dependent on prior sleep debt such that the capacity to recover during sleep
> varies inversely with extant sleep debt. Specifically, the UMP modulates the lower asymptote of process S
> as a function of the sleep debt resulting from prior sleep/wake history such that the most recent sleep
> loss exerts the greatest effect, with the sleep loss influence decreasing with increasing temporal
> distance."

So the mechanism by which chronic restriction differs from acute deprivation is explicit: accumulated debt
raises the *floor* that a night of sleep can discharge to. You cannot recover to baseline while carrying debt.

### 10.2 The fitted parameters, verbatim (standard errors in parentheses)

Fitted by least squares on the group-average PVT lapse data of **all four Belenky 2003 arms simultaneously**
(7 nights at 3, 5, 7 and 9 h TIB, with 3 nights of 8 h TIB baseline and 3 nights of 8 h TIB recovery):

> "By minimizing the objective function in Equation 6, we obtained the following UMP parameter estimates
> (standard error): U = 18.35 (0.73) lapses, τ_w = 40.00 (3.19) h, τ_s = 2.11 (0.11) h, S₀ = 0.00 (0.66)
> lapses, κ = 3.26 (0.26) lapses, φ = 2.31 (0.26) h, τ_LA = 7.00 (1.67) d, L₀ = −4.96 (0.00) lapses."

| Parameter | Estimate (SE) | Units | What it controls |
|---|---|---|---|
| U | 18.35 (0.73) | lapses | upper asymptote of homeostatic process — **ceiling on harm** |
| τ_w | 40.00 (3.19) | h | rise of sleep pressure during wake |
| τ_s | 2.11 (0.11) | h | fall of sleep pressure during sleep |
| S₀ | 0.00 (0.66) | lapses | initial homeostatic state |
| κ | 3.26 (0.26) | lapses | circadian amplitude |
| φ | 2.31 (0.26) | h | circadian phase |
| **τ_LA** | **7.00 (1.67)** | **days** | **time constant of sleep-debt accumulation and clearance** |
| L₀ | −4.96 (0.00) | lapses | initial lower asymptote |

For the validation studies the initial conditions were recomputed rather than refitted, verbatim:

> "the S₀ and L₀ parameters were computed to be 0.50 and 0.00 lapses, respectively."

**Debt is bounded, and asymmetrically.** Verbatim on the rescaling, which matters for weekend catch-up:

> "However, it is unlikely that normal, healthy, non-sleep-deprived individuals can sleep for 24 consecutive
> hours during 24 h of TIB. In fact, the estimated maximal capacity for sleep (under well-rested conditions)
> in young adults when given 16 h of sleep opportunity per 24 h is 8.9 h. Therefore, in the current work, we
> modified the UMP to impose a minimum debt level of −0.11 (corresponding to the asymptotic debt limit
> associated with 8.9 h of sleep/day) instead of the previous limit of −2."

with the important qualifier, also verbatim:

> "(The revised debt limit associated with 8.9 h of sleep/day is reached only under well-rested conditions.
> Under sleep-deprived conditions or when carrying a positive sleep debt, an individual can certainly sleep
> > 8.9 h/day, and this is considered in our model.)"

Debt runs from −0.11 to +1: **roughly a 9:1 asymmetry between how readily debt accrues and how much credit
can be banked.** This is the model-side counterpart of the empirical finding (§5) that recovery saturates.

### 10.3 What τ_LA = 7 days implies for a three-year exposure — **DERIVED**

Equation 5a is a first-order linear ODE, so on a fixed schedule the debt term approaches its asymptote as
1 − e^(−t/τ_LA):

| Days on a fixed schedule | Fraction of asymptotic deficit reached (τ_LA = 7 d) |
|---|---|
| 7 | 63.2% |
| 14 | 86.5% |
| 21 | 95.0% |
| 28 | 98.2% |
| 30 | 98.6% |

**Arithmetic:** 1 − exp(−7/7) = 0.6321; 1 − exp(−14/7) = 0.8647; 1 − exp(−21/7) = 0.9502;
1 − exp(−28/7) = 0.9817; 1 − exp(−30/7) = 0.9862.

Sensitivity across the 95% interval on τ_LA (7.00 ± 1.96 × 1.67 → **3.73 to 10.27 d**), at 30 days:
1 − exp(−30/3.727) = **99.97%**; 1 − exp(−30/10.273) = **94.6%**. So the parameter is loose to a factor of
three, yet the conclusion is unchanged across its whole admissible range.

**This is the single most consequential number in this file.** Van Dongen 2003's 14-day trajectory looks
near-linear precisely *because* 14 days is only two time constants — the curvature exists but is modest over
that window, which is exactly why the same data can support both a "still rising at day 14" reading and an
exponential-saturation reading. Extrapolating the apparent linear slope out to ~1,000 nights is the error
this parameter forbids: on this form our subject's neurobehavioural deficit reached steady state roughly
three weeks after the schedule began at age 16, and the remaining three years added essentially nothing
*through this pathway*.

**The caveat that must travel with it.** τ_LA governs the *state* variable this class of model tracks —
current performance capacity. It says nothing about slow structural or cumulative-risk processes with much
longer time constants (neurodevelopment, metabolic and cardiovascular remodelling, academic trajectory), which
are other shards' territory. Saturation of the vigilance deficit at three weeks is fully compatible with a
monotonically worsening three-year outcome on those axes. Read τ_LA as bounding the **neurobehavioural
state**, not total harm.

### 10.4 Out-of-sample performance, verbatim — and how much confidence it actually buys

> "The UMP accurately predicted PVT performance trends across 14 different sleep/wake conditions, yielding
> average prediction errors between 7% and 36%, with the predictions lying within 2 standard errors of the
> measured data 87% of the time. In addition, the UMP accurately predicted performance impairment (average
> error of 15%) for schedules (TSD and naps) not used in model development."

Training and validation studies, from Table 1 (each cross-referenced to this shard's own records):

| Role | Study | Schedule | This shard's record |
|---|---|---|---|
| **Training T1** | Belenky 2003 | 7 nights at 3 / 5 / 7 / 9 h TIB, 4 arms | `belenky2003` |
| Validation V1 | Rupp 2012 | 64 h TSD; 7 nights 3 h TIB | screened, not extracted |
| Validation V2 | Tucker 2010 | 62 h TSD; 10 h TIB control | screened, not extracted |
| Validation V3 | Philip 2012 | 40 h TSD; 5 nights 4 h TIB | screened, not extracted |
| Validation V4 | Banks 2010 | 5 nights 4 h TIB + graded recovery | `banks2010` |
| Validation V5 | Doran/Van Dongen | TSD and nap schedules | — |

**Three reasons this is less conclusive than it looks, stated plainly:**

1. **A free per-condition intercept.** Verbatim: *"we added a constant value δ to the UMP predicted output
   P(t, wᵢ, Θ) for each study condition, where δ was computed as the difference between the average number of
   measured PVT (or SRTT) lapses and the average number of predicted lapses P(t, wᵢ, Θ) on the first day of
   TSD/CSR for that particular study condition."* What is validated is the **shape** of the trajectory, not
   its level.
2. **Accuracy degrades exactly where our subject sits.** In-sample RMSE ranged from **1.20 lapses at 7 h TIB
   to 3.26 lapses at 3 h TIB**, and verbatim: *"the fit on the last 2 d of CSR for the 3-h TIB condition was,
   on average, lower than the data by 4.92 lapses."* The model **under-predicts** harm at severe doses — the
   3–5 h range our subject's worst nights occupy.
3. **Every dataset is adult.** No parameter in the table above has ever been estimated or validated in
   adolescents. This is the largest single reason to inflate uncertainty when transporting τ_LA to a 16–19
   year old.

Also note the model **assumed circadian phase φ was identical across all six studies** ("we assumed that the
entrained circadian phase φ of each group of subjects was similar across all studies"). Short 2018 measured
DLMO under three restriction doses in adolescents and found **dose-dependent phase delays**, so that
assumption is known to be wrong under restriction — see §11.4.

### 10.5 Where this leaves the §7.1 fork

§7.1 posed three incompatible history-weighting schemes and said no experiment could discriminate them. That
is still true empirically, but one arm now has a number:

| Weighting | Effective memory | Predicted 3-year deficit vs 3-week deficit | Status |
|---|---|---|---|
| Unweighted cumulative (§1.4) | all ~1,000 nights | vastly larger | no fitted decay parameter |
| Pure state-dependence (§3.5) | present state only | identical | McCauley; explicitly denies debt |
| **Exponential recency (§10)** | **τ_LA = 7.00 ± 1.67 d** | **~5% larger** | **fitted, with SE, validated out of sample** |

Two of the three now predict that a three-year exposure produces essentially the same neurobehavioural state
as a three-week exposure at the same dose. Only the unweighted-cumulative form predicts continued growth, and
it is the one with no fitted decay parameter. **The weight of the parameterised evidence favours saturation.**

---

## 11. Age-matched adolescent coefficients — the only ones in this file measured at our subject's age

Every form in §§1–5 and §10 is calibrated on adults. This section collects the dose-response coefficients
that were measured in adolescents. There are not many, and none of them is embedded in a dynamic model, but
they are the correct source for the *level* of the effect even when the *shape in time* has to come from
adult data.

### 11.1 Objective vigilance, per hour of TIB — Campbell et al. 2018

Source: Campbell IG, Van Dongen HPA, Gainer M, Karmouta E, Feinberg I. *Sleep* 2018;41(12):zsy177.
doi 10.1093/sleep/zsy177, PMID 30169721. Full text retrieved. n = 76, ages 9.8–16.2, three TIB doses
(7 / 8.5 / 10 h) × 4 consecutive nights, within-subject, repeated annually for 3 years.

Per-dose model estimates, verbatim:

> "With age centered at 13.2 years and time of day centered at 09:00 am, model estimates of LSNR for 7, 8.5,
> and 10 hours TIB were 12.15, 12.55, and 12.88 dB, respectively, constituting an 18.3%
> (10[(12.88–12.15)/10)–1) improvement in the fidelity of information processing from 7 to 10 hours TIB."

and the continuous-sleep version, verbatim:

> "With TST as a continuous measure, PVT LSNR increased by 0.29 ± 0.04 dB (mean ± SE) for each additional
> hour of TST (F1,2067 = 45.2, p < 0.0001). TST effects did not interact significantly with age
> (F1,2067 = 2.19, p = 0.14)."

**DERIVED** — OLS through the three per-dose points gives **0.2433 dB per hour of TIB**
(Sxy/Sxx = 1.095/4.5); residuals are −0.0117, +0.0233, −0.0117 dB, i.e. the three points are **almost
exactly collinear**, so the adolescent dose-response is **linear in TIB across 7–10 h**. Rescaling the
published continuous-TST slope onto a TIB axis using 41.5 min/h (§11.3) gives 0.29 × 0.69167 = **0.2006 dB
per hour of TIB (SE 0.0277)**. The two routes agree to within 20%; carrying the discrepancy in quadrature
gives **0.243 dB/h of TIB, SE 0.051**.

Why LSNR rather than lapses, verbatim — and this is the reason it is worth using for a maturing subject:

> "The LSNR is particularly suitable as an outcome measure in longitudinal studies where reference
> performance may be dynamically changing over time (age), as the interpretation of the difference between
> conditions is independent of the reference point (e.g. a –3dB change in LSNR always means a 50% reduction
> in the fidelity of information processing regardless of the reference point from which the change is
> measured)."

**Calibration anchor supplied by the authors**, verbatim:

> "the 10-hour TIB value of 12.88 dB is about 2 dB lower than well-rested baseline performance observed in
> adults, and performance in adults drops by approximately –3 dB on the LSNR scale (i.e. 50%) during the
> early morning trough of performance after being kept awake all night."

So four nights at 7 h TIB costs adolescents −0.73 dB, roughly **a quarter of the LSNR cost of one
all-nighter**. Useful as a sanity bound on how much a single bad week can do.

**Crucially, this slope does not attenuate with age:** the TIB × age interaction was null on both
specifications (F2,2318 = 2.10, p = 0.12 categorical; F1,2067 = 2.19, p = 0.14 continuous). That is the formal
licence for carrying it across the 16–19 window. One qualification, verbatim:

> "However, for the older participants 10 hours TIB did not produce better performance than 8.5 hours TIB.
> Post hoc analyses for the 10 versus 8.5 hours TIB conditions showed a significant LSNR improvement for the
> youngest quartile (F1,562 = 6.47, p = 0.011) but not for the oldest quartile (F1,544 = 1.17, p = 0.28)."

i.e. the **top** of the curve may flatten with age while the cost of falling to 7 h does not. For our subject
that asymmetry makes weekend catch-up above ~8.5 h worth *less* than a linear model implies, while his
weekday deficit costs full price.

### 11.2 Subjective sleepiness, per hour of TIB — Campbell et al. 2017

Source: Campbell IG, Burright CS, Kraus AM, Grimm KJ, Feinberg I. *Sleep* 2017;40(5):zsx046.
doi 10.1093/sleep/zsx046, PMID 28419388. Full text retrieved. n = 76 analysed, ages 9.9–14.0 (mean 12.2),
same 7 / 8.5 / 10 h × 4-night protocol, all participants completing all three schedules.

Verbatim:

> "Subjective sleepiness rating on the KSS (Figure 5) increased with decreasing TIB (F1,810 = 68.6.
> p < .0001). Linear mixed effects analysis estimated that for the third lab visit at 15:00, the average KSS
> rating for 7-h TIB was 6.33 (±0.28 SE) points and decreased by 0.56 (=/− 0.07) points for each additional
> hour in bed."

(The "=/−" is a typographical error for "±" in the published text.)

So: **0.56 ± 0.07 KSS points per hour of TIB**, anchored at 6.33 ± 0.28 on the 9-point scale at 7 h TIB.
Extrapolating, 10 h TIB → 6.33 − 3 × 0.56 = **4.65**. Three hours of TIB moves adolescents about **1.7 points
on a 9-point scale** and never out of the middle of the range.

Set that against the objective channel in the **same subjects on the same afternoons**, verbatim:

> "Pooling all participants and the 4 MSLTs across the day, participants who kept the 10-h TIB schedule fell
> asleep during 41% of the MSLTs. This percentage increased to 58% for the 8.5-h schedule and to 80% for the
> 7-h schedule."

**A 1.7-point self-report shift accompanies a near-doubling of objectively measured sleep propensity
(41% → 80%).** That is the subjective/objective dissociation quantified on both channels in one sample, at
the *mild* end of the dose range. Note also that successive 1.5 h cuts cost 17 then 22 percentage points —
the objective curve **accelerates** rather than saturating across 10 → 7 h.

And the age structure differs between the two channels — verbatim:

> "KSS ratings did not change with age (F1,74 = 0.16, p = .69) nor did the TIB effect on KSS ratings differ
> by age (F1,810 = 0.24, p = .63)."

versus, for the MSLT in the same paper, a significant age × TIB interaction (t75 = −3.40, p = .0011 at 8.5 h;
t75 = −4.25, p < .0001 at 7 h). Combined with §11.1, adolescence gives a **three-way** dissociation: the PVT
response to dose is constant with age, the MSLT response **shrinks** with age, and the KSS response is
constant with age. A single latent "sleepiness/impairment" factor cannot reproduce that.

### 11.3 The TIB → sleep conversion factor, measured by PSG in adolescents

Verbatim (Campbell 2018):

> "The 3 years average (±SE) of night 4 total sleep time (TST) for all subjects was 530 ± 2 minutes,
> 471 ± 2, and 405 ± 1 for 10, 8.5, and 7 hours in bed, respectively. Mixed-effect analysis showed that this
> TIB effect represented a significant (F1,471 = 2777, p < 0.0001) increase of 41.5 ± 0.8 minutes of TST for
> each additional hour of TIB."

**41.5 ± 0.8 min of sleep per hour of time in bed = 69% efficiency.** Campbell 2017's year-1 values agree to
within 4 min (405 ± 2 / 472 ± 2 / 534 ± 3). Consequences:

- A "6 h TIB" arm is roughly **5.1 h of sleep**. Every TIB-denominated dose in this file overstates sleep.
- To convert a per-hour-of-TIB effect into a per-hour-of-sleep effect, **divide by 0.692** — which *inflates*
  it by ~45%. Both axes appear among this shard's sources, so mixing them is a silent 45% error.
- Our subject's self-reported 5–6 h is more plausibly time in bed than sleep, so his true sleep on those
  nights may be nearer **3.5–4.2 h**. That pushes him toward, and on 3–4 h pre-exam nights below,
  McCauley's bifurcation threshold of 3.8 h daily sleep (§3.3).

### 11.4 The adolescent sleep requirement, and the circadian feedback term

Source: Short MA, Weber N, Reynolds C, Coussens S, Carskadon MA. *Estimating adolescent sleep need using
dose-response modeling.* **Sleep** 2018;41(4):zsy011. doi 10.1093/sleep/zsy011, PMID 29325109.
**Abstract only** — bronze OA at OUP but every retrieval route returns HTTP 403; no green copy exists in PMC,
Europe PMC, OpenAlex or Semantic Scholar. **No equations or per-arm data could be extracted, and none should
be attributed to it here.** n = 34, ages **15–17** — the closest age match in this shard — with three doses
(5 / 7.5 / 10 h TIB) for 5 nights, in-laboratory, PVT every 3 h.

Verbatim from the abstract:

> "Dose-dependent deficits to sleep duration, circadian phase timing, lapses of attention, and subjective
> sleepiness occurred. Less TIB resulted in less sleep, more lapses of attention, greater subjective
> sleepiness, and larger circadian phase delays. Sleep need estimated from 10-hour TIB sleep opportunities
> was approximately 9 hours, while modeling PVT lapse data suggested that **9.35 hours of sleep is needed to
> maintain optimal sustained attention performance**."

Two independent corroborations of the 10 h-TIB ceiling, from Campbell 2018's full text, verbatim:

> "The 530 minutes sleep duration that we report for the 10 hours TIB condition is very similar to the 533
> minutes mean for 15- to 17-year-old participants on a 10 hours TIB schedule in Short et al.'s study and is
> similar to the values reported by Carskadon et al. in 1983."

**Why the 9.35 h figure reframes every other number in this file.** Almost all adult dose-response work here
is expressed against an **8 h TIB** referent, and 8 h TIB yields well under 8 h of sleep. If the adolescent
optimum is 9.35 h of *sleep*, then:

- an 8 h-TIB adult "control" arm is itself restricted by adolescent standards;
- every "per hour below 8 h" effect size in this shard is measured **from a point already on the descending
  limb**, and is therefore **biased toward zero** when transported to an adolescent;
- our subject is never at the optimum — weekdays at 5–6 h are **3.35–4.35 h/night short**, and weekends at
  7–8 h are **still 1.35–2.35 h/night short**. No part of his week constitutes recovery to optimum.

**The circadian feedback term, which no dynamic form in this file contains.** Restriction produced
*dose-dependent circadian phase delays*. With a fixed school rise time, that makes the exposure **partly
self-sustaining**: shorter TIB delays the pacemaker, the delayed pacemaker makes an earlier bedtime harder,
and weekday TIB shortens further. Campbell 2018 flags the same mechanism as an untested limitation of its own
design ("It remains possible that shortening TIB by delaying bedtime produced a circadian phase delay and
that this delay differed by age"); Short et al. measured it and found it. **A model treating weekday sleep as
an exogenous constant over three years omits a compounding term.** This is also why the UMP's assumption of a
common fixed φ across studies (§10.4) is known to fail under restriction.

### 11.5 Summary table of age-matched coefficients

| Quantity | Estimate | SE | Source | Age |
|---|---|---|---|---|
| PVT log-SNR per hour of TIB | 0.243 dB | 0.051 | Campbell 2018 (**DERIVED**) | 9.8–16.2 |
| PVT log-SNR per hour of sleep | 0.29 dB | 0.04 | Campbell 2018 (published) | 9.8–16.2 |
| PVT fidelity loss, 7 h vs 10 h TIB, 4 nights | −15.5% | — | Campbell 2018 (**DERIVED**) | 9.8–16.2 |
| KSS points per hour of TIB | 0.56 | 0.07 | Campbell 2017 (published) | 9.9–14.0 |
| MSLT sleep-onset rate, 10 / 8.5 / 7 h TIB | 41 / 58 / 80 % | — | Campbell 2017 (published) | 9.9–14.0 |
| MSLT log-odds vs 10 h TIB: 8.5 h / 7 h | 0.86 / 1.90 | 0.07 / 0.08 | Campbell 2018 (published) | 9.8–16.2 |
| TST per hour of TIB | 41.5 min | 0.8 | Campbell 2018 (published) | 9.8–16.2 |
| Night-4 TST at 7 / 8.5 / 10 h TIB | 405 / 471 / 530 min | 1 / 2 / 2 | Campbell 2018 (published) | 9.8–16.2 |
| Modelled sleep required for optimal PVT | 9.35 h | — | Short 2018 (published) | **15–17** |
| TST obtained on a 10 h TIB opportunity | 533 min (8.88 h) | — | Short 2018 via Campbell 2018 | **15–17** |

**All of the above are 4–5 night exposures.** Not one age-matched study runs long enough to estimate an
accumulation *rate* in adolescents, so the time course must be borrowed from the adult forms in §§1–5 and
§10. That borrowing is the largest single unquantified assumption in this shard's dose-response backbone.
