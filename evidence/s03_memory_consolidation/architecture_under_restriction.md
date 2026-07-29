# Sleep architecture under partial restriction: what is actually lost at 5–6 h

**Shard:** `s03_memory_consolidation`
**Purpose:** the modeller needs to know whether a 5–6 h night loses the *consolidation-relevant*
sleep, or whether it preferentially loses REM while sparing slow-wave sleep (SWS). This determines
whether a naive "hours below 8" ledger over- or under-states the learning-loss channel.

**Headline answer, in three steps.**

1. **A stage-minutes ledger is the wrong ledger.** Restricting time in bed (TIB) to 5–7 h removes
   almost *no* SWS — SWS minutes are actively defended down to 4 h TIB. The loss falls on stage N2
   (largest absolute share) and REM (largest proportional share). Five doses, five independent
   laboratories, adolescents and adults, unanimous direction.
2. **So "SWS preserved" does not license "consolidation preserved."** The marker most tightly tied to
   declarative consolidation — sleep-spindle (sigma, 11–15 Hz) activity, which lives inside N2 — falls
   ~28–40% from 10 h to 7 h TIB even though N3 minutes do not move.
3. **But the spindle pathway is too weak to carry a large learning loss.** The only meta-analysis of
   the spindle→memory slope puts it at r = 0.21 for declarative memory (r = 0.13 in the subset least
   exposed to selective reporting), with significant publication bias. Multiplied through, a 28–40%
   spindle loss buys only ~0.07–0.21 SD of declarative memory — far short of the g ≈ −0.9 the
   matched-dose behavioural studies report.

**The consequence for the report:** the sleep-architecture route predicts a *small* consolidation loss
at 5–6 h. If the behavioural deficits at that dose are real, they are more likely deficits of *encoding
capacity while awake* than of overnight consolidation. Sections 1–3 give the stage numbers, section 4
gives the five findings that break a minutes-based model, section 5 gives the recommendation.

**A note on the framing in the task description**, which asked whether 5–6 h nights "actually lose the
consolidation-relevant sleep or preferentially lose REM." The dichotomy does not survive the evidence.
REM *is* preferentially lost — but REM duration is the one architecture variable that repeatedly fails
to predict memory (section 4b: β = −0.016 across 427 effect sizes; section 4d: r > −0.50 in the *wrong*
direction at the subject's own dose). So the stage that is preferentially lost is not the
consolidation-relevant one, and the stage that is consolidation-relevant is not preferentially lost.

---

## 1. Primary quantitative anchor: adolescent TIB dose–response, 4 consecutive nights

Campbell IG, Cruz-Basilio A, Darchia N, Zhang ZY, Feinberg I. **Effects of sleep restriction on the
sleep electroencephalogram of adolescents.** *Sleep.* 2021;44(6):zsaa280.
DOI `10.1093/sleep/zsaa280` · PMID `33507305` · verified Crossref + PubMed · full text via PMC8343600.

Design: 77 participants (41 male), ages 9.9–16.2 y, longitudinal over 3 years; **each participant
kept all three schedules** — four consecutive nights of 7, 8.5, or 10 h TIB. PSG on night 4.

Table 1, quoted verbatim from the paper:

> Mean (± standard error) sleep stage data for the three time in bed conditions
>
> | | 7 h | 8.5 h | 10 h |
> | --- | --- | --- | --- |
> | Total sleep time (min) | 406 ± 1 | 472 ± 2 | 530 ± 2 |
> | NREM (min) | 318 ± 2 | 360 ± 2 | 402 ± 2 |
> | N2 (min) | 203 ± 2 | 250 ± 2 | 291 ± 3 |
> | N3 (min) | 114 ± 2 | 111 ± 2 | 111 ± 2 |
> | REM (min) | 89 ± 1 | 112 ± 1 | 128 ± 2 |
> | Sleep onset latency (min) | 3.7 ± 1.3 | 11.2 ± 0.7 | 21.4 ± 1.4 |

Statistical confirmation, quoted verbatim:

> Reducing TIB significantly decreased both NREM (F2,149 = 795, p < 0.0001) and REM durations
> (F2,149 = 225, p < 0.0001). ... The effect of TIB reduction on NREM duration resulted from a
> significant (F2,149 = 545, p < 0.0001) stage N2 decrease. **Stage N3 duration showed a trend
> (F2,149 = 2.53, p = 0.084) to increase with TIB reduction.**

### Arithmetic decomposition (my computation from the quoted table)

Cutting TIB from 10 h to 7 h costs **124 min of total sleep time (−23.4%)**. That loss is
apportioned as:

| Stage | 10 h → 7 h change | % change | share of the 124-min TST loss |
| --- | --- | --- | --- |
| N2 | −88 min | −30.2% | **71.0%** |
| REM | −39 min | −30.5% | **31.5%** |
| N3 (SWS) | **+3 min** | **+2.7%** | **−2.4%** (i.e. N3 *gained*) |

Going only from 10 h to 8.5 h: TST −58 min, of which N2 −41 min, REM −16 min, **N3 exactly 0 min**.

As a proportion of total sleep, SWS is *up-weighted* under restriction while REM is slightly
down-weighted:

| | 7 h TIB | 8.5 h TIB | 10 h TIB |
| --- | --- | --- | --- |
| N3 as % of TST | 28.1% | 23.5% | 20.9% |
| REM as % of TST | 21.9% | 23.7% | 24.2% |

**Caveat on transportability:** this cohort is 9.9–16.2 y, younger than the 18-year-old subject, and
the shortest dose is 7 h TIB — milder than the subject's 5–6 h weekday exposure. It cannot be
extrapolated to 5 h without the studies in section 2.

---

## 2. Corroboration at the 4–5 h dose (2a–2e adolescents; 2f adults)

### 2a. 4 h TIB — the cleanest stage-by-stage percentages anywhere in this literature

Kopasz M, Loessl B, Valerius G, Koenig E, Matthaeas N, Hornyak M, Kloepfer C, Nissen C, Riemann D,
Voderholzer U. **No persisting effect of partial sleep curtailment on cognitive performance and
declarative memory recall in adolescents.** *J Sleep Res.* 2010;19(1 Pt 1):71–79.
DOI `10.1111/j.1365-2869.2009.00742.x` · PMID `19656277` · verified · abstract only.

n = 22, aged 14–16 y, randomized cross-over, PSG. One night of 4 h TIB vs a 9 h control night.
Quoted verbatim from the abstract:

> During the 4-h night, we observed a curtailment of **50% of non-rapid eye movement (non-REM), 5%
> of slow wave sleep (SWS) and 70% of REM sleep** compared with the control night.

This is the single most compact statement of the phenomenon: at less than half of normal TIB, SWS is
**95% intact** while REM is **70% gone**.

### 2b. 5 h TIB for 7 nights — SWS minutes statistically indistinguishable from 9 h

Ong JL, Lo JC, Gooley JJ, Chee MWL. **EEG Changes across Multiple Nights of Sleep Restriction and
Recovery in Adolescents: The Need for Sleep Study.** *Sleep.* 2016;39(6):1233–1240.
DOI `10.5665/sleep.5840` · PMID `27091536` · verified · full text via PMC4863211.

n = 55 (29 sleep-restricted, 26 control), 25 male, mean age **16.6 ± 1.0 y** — the closest
population match in this whole literature to the subject. Boarding-school quasi-laboratory:
3 nights 9 h TIB → 7 nights 5 h (SR) or 9 h (control) → 3 recovery nights 9 h. Participants
"reported habitual TIBs of approximately 6 h on week nights" — i.e. the subject's own exposure.

> Across the sleep restriction nights, **total SWS duration was preserved relative to the 9 h
> baseline sleep opportunity, while other sleep stages were reduced.**

> Although SWS duration was slightly elevated on M7 in the SR group (SR: 109.26 ± 3.33 min vs.
> Control: 97.17 ± 5.31 min; P = 0.03), **mean SWS across manipulation nights did not differ between
> groups (SR: 101.10 ± 3.36 min vs. Control: 99.13 ± 5.42 min; P = 0.75).**

My computation on those means (treating the ± values as SEM, as labelled): pooled SD 23.09,
**Hedges' g = +0.08, SE 0.27, 95% CI [−0.45, +0.61]** for SWS minutes at 5 h vs 9 h TIB. A tight null
centred on zero. Meanwhile:

> When sleep opportunity was reduced from 9 h to 5 h in SR participants, TST and durations of N1, N2,
> and REM sleep across the entire night decreased ... **TST and all sleep macro-structure measures,
> except for SWS duration, were affected by our sleep restriction manipulation.**

### 2c. 5 h TIB for 7 nights — the same result with per-night significance tests

Lo JC, Bennion KA, Chee MWL. **Sleep restriction can attenuate prioritization benefits on declarative
memory consolidation.** *J Sleep Res.* 2016;25(6):664–672.
DOI `10.1111/jsr.12424` · PMID `27291639` · verified Crossref + PubMed · full text via PMC5324680.

n = 56, 25 male, mean age **16.6 ± 1.1 y**, ages 15–19 — an exact match to the subject's age band.
Randomized parallel groups: 7 nights of 5 h TIB (n = 30) vs 9 h TIB (n = 26), PSG on manipulation
nights M1, M4 and M7. This is the same Duke-NUS Need for Sleep protocol as Ong 2016 but reports the
stage comparisons night by night, which no other source in this file does:

> Polysomnography data on the baseline night revealed no significant differences between groups in
> total sleep time (TST), wake after sleep onset (WASO), sleep onset latency and the duration of N1,
> N2, N3, and rapid eye movement (REM) sleep (all Ps > 0.12). Conversely, on all manipulation nights
> (M1, M4, M7), relative to the control group, participants in the SR group had shorter TST, WASO,
> sleep latency, N1, N2, and REM sleep (all Ps < 0.001; Fig. 4; Supporting information, Appendix S3);
> **the only sleep parameter that did not differ between groups was the duration of N3 (M1: P = 0.23;
> M4: P = 0.36; M7: P = 0.10).**

And stated again in the discussion:

> the SR group in the present study **maintained their absolute amount of N3 sleep during the
> manipulation period despite a marked reduction in TST and all other sleep stages.**

My computation (back-computed from the reported P values at df = 54): the REM deficit is
**g ≤ −0.92** (lower bound, from P < 0.001), while for N3 the group difference is bounded at
**|g| ≈ 0.32** (M1, P = 0.23), 0.24 (M4, P = 0.36) and 0.44 (M7, P = 0.10) — and the sign is not even
recoverable, because the paper never states which arm had numerically more N3. The contrast between a
stage cut at P < 0.001 and a stage that cannot be distinguished on any of three nights is the
cleanest single demonstration of selective SWS defence at the subject's exact dose and age.

The authors draw the protective inference explicitly: **"N3 may offset detrimental effects of sleep
restriction on memory"** and this "speaks to the resilience of adolescents in the context of
declarative memory consolidation." Section 4d records the finding in the same paper that cuts against
the REM half of the story.

### 2d. 5 h TIB for 5 nights — independent replication

Skorucak J, Weber N, Carskadon MA, Reynolds C, Coussens S, Achermann P, Short MA. **Homeostatic
response to sleep restriction in adolescents.** *Sleep.* 2021;44(9):zsab106.
DOI `10.1093/sleep/zsab106` · PMID `33893807` · verified · full text via publisher.

n = 34, ages 15–17 y (mean 15.91, SD 0.86), parallel groups at 5, 7.5, or 10 h TIB for 5 nights
between 10 h baseline and 10 h recovery nights.

> During the experimental nights, **although time spent in SWS did not differ from the baseline
> levels, participants in the 5-h condition spent less time in REM sleep**, when compared to 7.5-h
> and 10-h conditions.

> Total duration of REM sleep in minutes was lower than baseline for all experimental nights in the
> 5-h condition, and for N1, N3 and N5 in the 7.5-h condition.

> The proportion of total sleep spent in SWS (%TST) was **increased** in 5-h and 7.5-h sleep
> restriction conditions for all experimental nights, reflecting an increased sleep drive.

Cumulative dose over the 5 nights: "approximately 20 h for 5-h, and approximately 8 h for 7.5-h
condition."

### 2e. Same result across a 5-arm dose–response, 9/8/7/6/5 h

Voderholzer U, Piosczyk H, Holz J, Landmann N, Feige B, Loessl B, Kopasz M, Doerr JP, Riemann D,
Nissen C. **Sleep restriction over several days does not affect long-term recall of declarative and
procedural memories in adolescents.** *Sleep Med.* 2011;12(2):170–178.
DOI `10.1016/j.sleep.2010.07.017` · PMID `21256802` · verified · abstract + partial full text.

88 adolescents aged 14–16 randomized across **five** TIB doses — 9, 8, 7, 6 or 5 h — for four
consecutive nights, with PSG.

> **Polysomnographic monitoring after sleep restriction demonstrated a high preservation of the
> amount of slow wave sleep in the restricted conditions.**

This is the only study covering the subject's exact 6 h weekday dose in a randomized design. It
reports SWS preservation but I could not retrieve the per-arm stage minutes (paywalled tables);
recorded as `abstract_only` for the architecture claim.

### 2f. Adult replication — the pattern is not an adolescent peculiarity

Every source above is 9–19 years old. If SWS preservation were specific to adolescence the argument
would not transport as the subject ages, so an adult check matters.

Brunner DP, Dijk DJ, Tobler I, Borbély AA. **Effect of partial sleep deprivation on sleep stages and
EEG power spectra: evidence for non-REM and REM sleep homeostasis.** *Electroencephalogr Clin
Neurophysiol.* 1990;75(6):492–499. DOI `10.1016/0013-4694(90)90136-8` · PMID `1693894` · verified ·
abstract only. Young adults; n not stated in the abstract.

Design note worth flagging: restriction was implemented by keeping only **"the first 4 h of the
habitual bedtime period"** — i.e. by cutting the *end* of the night, which is how the subject's short
weeknights were actually produced (fixed school wake time, bedtime not advanced to match).

> After 2 baseline nights (B1, B2) of 7.5 h, sleep was restricted for 2 nights (D1, D2) to the first
> 4 h of the habitual bedtime period. … **During the deprivation nights, stages 1 and 2 and REM sleep
> were reduced, while slow wave sleep (SWS; stages 3 and 4) was not significantly affected. However,
> the time integral of EEG power density in the range of 0.75–4.5 Hz (slow wave energy) was reduced.**

Two things to take from this. First, the stage dissociation replicates in adults at the same 4 h dose
as Kopasz 2010. Second — and this is the 1990 antecedent of the Campbell sigma result in section 4a —
**slow wave *energy* fell while SWS *minutes* did not.** The minutes ledger and the spectral-energy
ledger disagreed thirty years before anyone framed it as a spindle question.

---

## 3. Consolidated dose–response table

Every row below is quoted or arithmetically derived from a verified source above. Rows marked
"adolescent" are in 14–19-year-olds, the right population.

| TIB dose | Source | TST | SWS / N3 | REM | Verdict on SWS |
| --- | --- | --- | --- | --- | --- |
| 10 h (ref) | Campbell 2021, adolescent | 530 min | 111 min | 128 min | reference |
| 9 h (ref) | Ong 2016, adolescent | — | 99.1 min | — | reference |
| 8.5 h | Campbell 2021, adolescent | 472 min | 111 min | 112 min | **0 min lost** |
| 7.5 h | Skorucak 2021, adolescent | ↓ vs baseline | no change vs baseline | ↓ on 3 of 5 nights | preserved |
| 7 h | Campbell 2021, adolescent | 406 min | 114 min (+3) | 89 min (−39) | **preserved / trend up** |
| 6 h | Voderholzer 2011, adolescent | — | "high preservation" | — | preserved |
| 5 h | Ong 2016, adolescent | ↓ | 101.1 min (P = 0.75 vs 99.1) | ↓ | **preserved** |
| 5 h | Lo 2016, adolescent 15–19 | ↓ (P < 0.001) | no difference on any night (P = 0.23 / 0.36 / 0.10) | ↓ (P < 0.001) | **preserved** |
| 5 h | Skorucak 2021, adolescent | ↓ (~20 h cumulative) | no change; ↑ as %TST | ↓ every night | preserved |
| 4 h | Kopasz 2010, adolescent | ↓ | **−5%** | **−70%** | 95% preserved |
| 4 h | Brunner 1990, young **adult** | ↓ | no significant change | ↓ | preserved |

Direction is unanimous across five independent laboratories (Davis, Singapore, Adelaide, Freiburg,
Zurich), five doses, and both adolescents and adults. **SWS minutes are essentially incompressible down to 4 h TIB. REM absorbs the
disproportionate share of the loss, and N2 absorbs the largest absolute share.**

Mechanism, quoted from Campbell 2021 — this is the reason the result is so robust:

> Slow-wave EEG activity is normally concentrated in the first part of the night. **The last 3 h in
> bed includes very little stage N3 sleep; therefore, eliminating these 3 h had little effect on the
> total delta activity of the night.**

---

## 4. Five findings that break the naive minutes-based model

A modeller who stops at section 3 will conclude "5–6 h nights preserve the consolidation-relevant
stage, so the learning-loss channel is small." That conclusion may well be roughly right, but every
step of the reasoning behind it is unsafe, and two of the five findings below push in the opposite
direction from the other three. Read all five before setting a prior.

### 4a. Sleep spindles fall ~40% even though N3 minutes do not

Same paper, Campbell 2021. Sigma (11–15 Hz) activity is the accepted EEG signature of sleep
spindles, and spindles — not SWS minutes — are the marker most consistently tied to overnight
declarative retention.

> From 10 h TIB to 7 h TIB, **sigma energy decreased from 0.504 to 0.361 mV2 s, a 39.6% decrease.**
> ... From 10 h TIB to 7 h TIB, sigma power decreased from 21.8 to 19.4 µV2, a 12.2% decrease.

> In other words, the **23% reduction in TST with TIB restriction from 10 to 7 h was associated with
> not only a 40% loss of all-night accumulated sigma activity** but also with a significant decrease
> in the rate of sigma production.

> The larger size of the effect and the altered pattern of sigma power across the night would argue
> that **the TIB reduction of sigma power is likely to be of greater biological significance than
> the small delta increase.**

*Arithmetic note:* the authors' "39.6%" is computed on the 7 h value as denominator
(0.143 / 0.361 = 39.6%). Expressed as a fraction of the 10 h baseline the reduction is
0.143 / 0.504 = **28.4%**. Both are correct descriptions of the same two numbers; the modeller
should use 28.4% if treating 10 h as the referent. I quote the authors' figure because it is what
the literature cites.

Corroborated at the 5 h dose: Reynolds CM, Gradisar M, Coussens S, Short MA. **Sleep spindles in
adolescence: a comparison across sleep restriction and sleep extension.** *Sleep Med.*
2018;50:166–174. DOI `10.1016/j.sleep.2018.05.019` · PMID `30056287` · verified · abstract only.
Same 34-participant 5 / 7.5 / 10 h protocol as Skorucak: "when experiencing severe sleep
restriction, fast spindles in adolescents were lower in amplitude and longer in duration." Note the
partial disagreement, which Campbell flags himself: "Reynolds et al. did not find a spindle
difference between participants keeping 7.5 and 10 h TIB schedules. The contradiction may be related
to the older age, 15–17 years, of their participants." So at 7.5 h the spindle effect may be absent
in older adolescents, appearing only at 5 h.

So: **the architecture variable that actually moves at the subject's dose is spindle/sigma activity, not
SWS minutes** — a 3 h TIB cut is a ~28–40% loss on sigma rather than a ~0% loss on N3. But before
keying the learning-loss channel to spindles, read 4a-bis: the spindle→memory slope is small.

### 4a-bis. …but the spindle→memory coefficient is small, and may be an artefact

The inference "spindles fall 40%, therefore consolidation falls a lot" needs the spindle-to-memory
slope. There is exactly one meta-analysis of it, and it does not support a large slope:

Kumral D, Matzerath A, Leonhart R, Schönauer M. **Spindle-dependent memory consolidation in healthy
adults: A meta-analysis.** *Neuropsychologia.* 2023;189:108661.
DOI `10.1016/j.neuropsychologia.2023.108661` · PMID `37597610` · verified · full text via the
bioRxiv preprint `10.1101/2022.07.18.500433` (verified, posted 2022-07-19).
53 studies, 1427 effect sizes, total N = 1896.

> the pooled correlation between sleep spindles and memory performance was **r = 0.236; CI:
> [0.161–0.308]; p < 0.001**, reflecting a small- to moderate effect size

> memory type is a significant moderator of the spindle-memory association (Qm(1) = 7.589, p = 0.006),
> with a stronger spindle-memory association for procedural memory (r = 0.319, p < .001, k = 392) than
> for **declarative memory (r = 0.210, p < .001, k = 812)**

Declarative memory — the channel that matters for schoolwork — is the *weaker* of the two. And the
literature is badly selection-biased. The modified Egger test is significant (β = 1.64, SE = 0.53,
p = 0.0020); the sample-size/effect-size correlation is r = −0.175, p < 0.001; the constituent studies
are tiny (mean N = 35.7, falling to 18.6 and a range of 6–44 once one large study is excluded); and for
declarative memory the effects authors *chose* to publish are nearly double those that had to be
requested from them:

> While in studies with declarative memory we found the effect size of reported studies (r = 0.254,
> k = 517) were higher than **unreported ones (r = 0.131, k = 295)** … (Qm(1) = 6.094, p = 0.014)

The authors further report that a PET-PEESE reanalysis of their own open dataset "reduces the
correlation between sleep spindles and memory function to insignificance." (I could not retrieve that
reanalysis and do not treat it as verified; it is quoted as reported.)

**Multiply it through.** Sigma energy falls 28–40% from 10 h to 7 h TIB, which is roughly 0.5–1.0 SD of
spindle activity depending on the between-subject SD assumed. At r = 0.21 that is **0.11–0.21 SD** of
declarative memory; at the less-biased r = 0.13 it is **0.065–0.13 SD**. So the spindle pathway, taken
at face value, predicts a *small* learning loss — roughly 0.07–0.21 SD, an order of magnitude below the
g = −0.89 that `cousins2018` measures behaviourally at the same dose. The spindle mechanism is real
enough to prefer over an SWS-minutes ledger, but it cannot carry the size of effect the behavioural
studies report. Note also the design extrapolation: these correlations come from natural
between-subject variation during *unrestricted* sleep, and none of the 53 studies restricted sleep.

### 4b. The largest meta-analysis finds stage minutes do not moderate the sleep benefit at all

Berres S, Erdfelder E. **The sleep benefit in episodic memory: An integrative review and a
meta-analysis.** *Psychol Bull.* 2021;147(12):1309–1353. DOI `10.1037/bul0000350` · PMID `35404637`.
823 effect sizes, 271 independent samples, 177 articles.

Three moderator analyses, quoted verbatim:

> the results from the TST subgroup analysis showed **no statistically significant effect of TST on
> the sleep benefit, β = −0.003, SE = 0.03, 95% CI [−0.07, 0.07], t(14.68) = 0.09, p = .931,
> k = 641, m = 207** ... Across all analyses, TST never significantly predicted the sleep benefit in
> episodic memory.

> We also investigated whether more time spent in SWS increases the sleep benefit ... **This effect
> was not significant** although descriptively in line with the expectation, **β = 0.05, SE = 0.08,
> 95% CI [−0.13, 0.23], t(14.52) = 0.60, p = .558, k = 427, m = 123** ... Across all analyses
> performed, SWS never significantly predicted the sleep benefit in episodic memory.

> Again, however, the **REM sleep effect was not statistically significant and was even opposite in
> direction, β = −0.016, SE = 0.12, 95% CI [−0.28, 0.25], t(15.63) = 0.13, p = .901, k = 427,
> m = 123.**

This is a strong constraint. Across 427–641 effect sizes there is **no measurable dose–response from
SWS minutes, REM minutes, or total sleep time to the size of the sleep benefit in episodic memory.**
The CIs are wide enough not to exclude modest effects, but a model that scales consolidation loss
linearly in lost SWS or REM minutes has no meta-analytic support.

### 4c. Countervailing evidence: a ~6 h threshold and a late-REM requirement

The one study that directly regressed overnight improvement on stage timing found both SWS *and*
REM mattered, with a sharp threshold near 6 h:

Stickgold R, Whidbee D, Schirmer B, Patel V, Hobson JA. **Visual discrimination task improvement: A
multi-step process occurring during sleep.** *J Cogn Neurosci.* 2000;12(2):246–254.
DOI `10.1162/089892900562075` · PMID `10771409` · verified · abstract only.

> When tested within 24 hr of training, **improvement was not observed unless subjects obtained at
> least 6 hr of posttraining sleep** prior to retesting, in which case improvement was proportional
> to the amount of sleep in excess of 6 hr. For subjects averaging 8 hr of sleep, overnight
> improvement was proportional to the **amount of slow wave sleep (SWS) in the first quarter of the
> night, as well as the amount of rapid eye movement sleep (REM) in the last quarter.** REM during
> the intervening 4 hr did not appear to contribute to improvement. A two-step process, modeling
> throughput as the product of the amount of early SWS and late REM, **accounts for 80 percent of
> intersubject variance.**

This matters enormously for the 5–6 h question, and it points the opposite way from section 3.
Restriction implemented by delaying bedtime and advancing wake time removes **the last quarter of
the night** — precisely where the late REM that this model requires is located. If consolidation
throughput is multiplicative in (early SWS × late REM), then preserving early SWS is worthless when
late REM goes to near zero: the product collapses. This is a procedural/perceptual task, not
declarative, and it is a single small study whose threshold has not been replicated at this
precision — but it is the only quantitative model of stage *timing* rather than stage *totals*, and
it predicts that 5–6 h nights are damaging for exactly the reason the naive ledger misses.

Note the tension with 4b: Berres & Erdfelder find REM *totals* do not moderate the sleep benefit,
while Stickgold finds late-REM *placement* is half the mechanism. These are compatible if placement
matters and totals do not, which is itself an argument against a minutes-based ledger.

### 4d. Within a restricted week, *more* REM predicted *worse* retention

This is the finding that most directly falsifies a "REM loss ⇒ learning loss" model at the subject's
dose, and it comes from the same Lo 2016 record as the architecture data in section 2c — same 5 h
arm, same PSG nights, same participants. Correlating mean stage minutes across M1/M4/M7 against prose
recall 6 weeks after encoding, within the sleep-restricted arm (n = 30):

> Also in the SR group, there was an **inverse linear relation between average REM duration and memory
> for total, HL, and nHL (r > −0.50, P < 0.013) content at the delayed time point** (Fig. 5f–h).

> **Unexpectedly, under conditions of sleep restriction, greater REM sleep was associated with poorer
> memory after an extended time interval (here, 6 weeks).**

Meanwhile the stage that *did* predict better retention was N2 — the stage that absorbs the largest
absolute share of the loss (−88 min from 10 h to 7 h in Campbell's table, 71% of the total TST loss),
and the stage that carries the spindles of section 4a:

> In the SR group, longer average N2 duration was associated with better memory for total (i.e. HL and
> nHL) content and nHL content at the post-manipulation time point (both r = 0.45, P = 0.014 ...), and
> better memory for total, HL, and nHL content at the delayed time point (r > 0.56, P < 0.005).

Two cautions before this is over-weighted. These are within-arm correlations on n = 30, and only the
N2 correlations differed significantly *between* groups (Fisher's Z > 2.22, two-tailed P < 0.026), so
the REM result is not established as restriction-specific. The authors themselves urge caution:
findings "occurring in the context of sleep restriction should be interpreted cautiously." But the
direction is the point. If REM loss were the mechanism by which 5 h nights damage declarative
learning, the REM correlation inside the restricted arm should be positive; it is reliably negative
across all three content types.

**Net effect on the ledger question:** the two stages that restriction actually removes are REM and
N2. Of those, REM shows no meta-analytic moderation (4b) and a negative within-arm correlation here,
while N2 shows a positive within-arm correlation and carries the spindle activity that falls ~28–40%
(4a). Both lines of evidence therefore point at **N2/spindles, not REM**, as the pathway worth
modelling — which is the opposite of what the "REM is disproportionately cut" framing in the task
description suggests.

---

## 5. Recommendation to the modeller

1. **Do not scale the learning-loss channel to lost SWS minutes.** At 5–7 h TIB, lost SWS is
   approximately zero (Campbell: +3 min at 7 h; Ong: g = +0.08, 95% CI [−0.45, +0.61] at 5 h;
   Kopasz: −5% at 4 h). A ledger keyed to SWS will return ~no learning loss, which four adolescent
   experiments say is the wrong answer for the wrong reason.
2. **Do not scale it to REM minutes either.** REM does take the disproportionate hit
   (−30.5% at 7 h, −70% at 4 h), and it is tempting to key the channel to REM. But Berres &
   Erdfelder's 427-effect-size analysis finds REM duration does not predict the sleep benefit
   (β = −0.016, 95% CI [−0.28, 0.25]) — and the sign is negative. Independently, within Lo 2016's
   5 h arm more REM predicted *worse* 6-week retention (r > −0.50, P < 0.013; section 4d). Two
   independent lines of evidence, one meta-analytic and one at the subject's exact dose and age,
   both decline to support a REM-keyed channel. **The disproportionate REM loss is real but appears
   not to be the mechanism of learning loss.**
3. **Prefer spindle/sigma activity as the exposure variable** — it is the only architecture measure
   that moves substantially at the subject's dose (−28% to −40% from 10 h to 7 h TIB) *and* has a
   mechanistic link to declarative consolidation. **But bound the resulting effect at ~0.07–0.21 SD.**
   The spindle→declarative-memory correlation is r = 0.21 (Kumral 2023, k = 812), falling to r = 0.13
   in the subset least exposed to selective reporting, with a significant Egger test and a reported
   PET-PEESE reanalysis that nulls it entirely. Multiplying a 0.5–1.0 SD spindle loss by r = 0.13–0.21
   gives 0.065–0.21 SD. **A spindle-keyed channel therefore cannot reproduce the g ≈ −0.9 that the
   matched-dose behavioural studies report** — which is itself informative: it suggests those
   behavioural effects are driven by impaired *encoding capacity* while awake (`cousins2018`,
   `yoo2007`) rather than by impaired overnight consolidation.
4. **Treat the 5–6 h band as genuinely uncertain rather than clearly safe or clearly damaging.**
   The naive "hours below 8" ledger is not conservative in a predictable direction — it is
   mis-specified. Section 3 pushes the estimate down; sections 4a and 4c push it back up. My
   recommendation is to model the learning-loss channel on *behavioural* outcomes at the matched
   dose and to use this architecture file only to set the *prior width*, not the point estimate.
   The matched-dose behavioural records in this shard split, and the modeller must carry both sides:
   impairment in `cousins2018` (g = −0.89) and `huang2016` (g ≤ −0.93, massed learning only), versus
   no gross impairment in `lo2016` (5 h × 7 nights, exact age match) and `voderholzer2011`
   (5-arm, 9–5 h). The split tracks *when* the restriction fell relative to encoding, not the dose —
   see `station_report.md`.
5. **Weekend recovery does not repair architecture within one night.** Ong 2016: "Total REM sleep,
   N2, and TST duration remained above baseline levels by the third recovery sleep episode" —
   i.e. a REM debt was still being repaid three nights later. Brunner 1990 adds a sharper version:
   sigma-band (13–16 Hz) power was *reduced* during the recovery nights themselves, after total sleep
   time had already been restored. If spindle activity is still suppressed once TST is back to normal,
   then a 7–8 h weekend does not immediately restore spindle-mediated consolidation capacity. Treat as
   suggestive only — one 1990 study, n unstated, no memory outcome. See the recoverability records
   (`yoo2007`, `cousins2018`, `stickgold2000nn`, `kopasz2010`, `berres2021`) for the memory-outcome
   consequences.

---

## Sources used in this file (all identifiers verified programmatically)

| Study | DOI | PMID | Access |
| --- | --- | --- | --- |
| Campbell 2021 | 10.1093/sleep/zsaa280 | 33507305 | full_text |
| Ong 2016 | 10.5665/sleep.5840 | 27091536 | full_text |
| Lo 2016 | 10.1111/jsr.12424 | 27291639 | full_text |
| Skorucak 2021 | 10.1093/sleep/zsab106 | 33893807 | full_text |
| Kopasz 2010 | 10.1111/j.1365-2869.2009.00742.x | 19656277 | abstract_only |
| Brunner 1990 (adult) | 10.1016/0013-4694(90)90136-8 | 1693894 | abstract_only |
| Voderholzer 2011 | 10.1016/j.sleep.2010.07.017 | 21256802 | abstract_only |
| Reynolds 2018 | 10.1016/j.sleep.2018.05.019 | 30056287 | abstract_only |
| Berres & Erdfelder 2021 | 10.1037/bul0000350 | 35404637 | full_text (accepted preprint 10.31234/osf.io/r2an6) |
| Kumral 2023 (spindle→memory slope) | 10.1016/j.neuropsychologia.2023.108661 | 37597610 | full_text (preprint 10.1101/2022.07.18.500433) |
| Stickgold 2000 (JOCN) | 10.1162/089892900562075 | 10771409 | abstract_only |
