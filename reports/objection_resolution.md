# Objection resolution log (Gate G13)

Three critics filed independent critiques: a methodologist (23 numbered objections), a domain
skeptic (26), and a contrarian arguing the null. Every objection is resolved here as one of
`ACCEPTED-AND-FIXED`, `ACCEPTED-AS-LIMITATION`, or `REJECTED-WITH-REASON`.

Two full rework loops followed the review. The headline numbers moved substantially and in one
direction: **every correction that changed a number made the damage estimate smaller, except the
two that added missing harm channels.** That asymmetry is itself a finding, and it is reported in
`REPORT.md` rather than buried here.

## Summary of what the review changed

| Quantity | Before review | After two rework loops | Driver |
|---|---|---|---|
| Cumulative debt vs need | 3,329 h | 2,921 h | sleep-need referent corrected and un-clipped |
| Mean nightly deficit | 3.20 h | 2.81 h | same |
| Vigilance g now | −0.87 | −0.79 | dose transport now carries duration uncertainty |
| Measured IQ change | −0.70 [−6.70, +6.95] | −0.70 [−3.42, +0.33] | bimodal route mixture removed |
| Permanent IQ change | −0.02 [−0.54, +0.57] | 0.00 [−1.65, 0.00] | permanence recast as an event, developmental pathway added |
| Life expectancy lost | 0.22 mo | 0.06 mo | mortality dose-response replaced categorical RR |
| Comparator rank | "1 of 8, least harmful" | 3 of 8 on a like-for-like basis | comparison basis made symmetric |
| Multiverse branches | 6 | 18 | sleep-need referent added as an axis |

---

## CRITICAL objections

**M1 / S7 — The mortality channel used the categorical RR 1.12 when its own evidence station
supplied dose-specific values (1.04 at 5 h, 1.01 at 6 h) and instructed the model to use them.**
`ACCEPTED-AND-FIXED`. `model.py` now interpolates a dose-response curve at the subject's estimated
mean sleep and applies the residual causal fraction to that. Life-expectancy loss fell from 0.22
to 0.06 months. The critics were right and the error was exactly as described: the categorical
contrast assigns the subject the average risk of everyone sleeping under 7 h rather than the risk
at his own dose.

**S1 / S2 — `klerman2008`'s 8.9 h is a maximal sleep *capacity* measured with a daytime nap
opportunity, and was being used as a nocturnal *requirement*; and `need_curve` clipped need at a
floor of 8.0 h so the hypothesis that he needs less could not be represented, while the value
*reported* as the inferred need bypassed the clip.** `ACCEPTED-AND-FIXED`, and this was the most
serious defect found. The clip is removed, the reported need is now computed with the identical
expression and bounds the ledger consumes, and the referent is a named switchable choice
(`capacity_based` / `guideline_midpoint` / `nocturnal_floor`) with the guideline midpoint as
primary. Debt now varies from 2,183 h to 3,322 h across those choices, where previously it barely
moved. The referent was also added as a third multiverse axis.

**M2 — `domain_profile_chronic_restriction` pooled a meta-analytic composite together with three
of its own constituent sub-domains as four independent studies.** `ACCEPTED-AND-FIXED`. Only the
composite is pooled; the sub-domains are reported descriptively and explicitly marked
`pool: False`. This was a genuine violation of the project's own de-duplication rule inside the
primary cognition parameter.

**M3 — Where k ≤ 2 the posterior predictive interval is entirely prior-determined.**
`ACCEPTED-AND-FIXED`. For k ≤ 2 the model now reports the study-level sampling interval and flags
it. The example the critic gave was decisive: the learning-loss channel was reported as
−0.886 [−2.968, +1.247] where the single study's own interval was [−1.532, −0.248]; the prior was
flipping the interval across zero.

**M4 / S10 / S11 — Route C (`binks1999`) generated the entire upper limb of the IQ interval, was
transported with the wrong conversion, and the "four independent routes" share one study.**
`ACCEPTED-AND-FIXED`. Routes A and B are algebraically near-identical (both driven by `lim2010`),
so B alone is the primary and A is a consistency check. Route C is reported as a *bound* on the
decrement rather than averaged in. The IQ interval narrowed from [−6.70, +6.95] to [−3.42, +0.33]
and is no longer bimodal. The claim that he might test 7 points above his own rested self is gone.

**M5 / S12 — Permanence conflated a probability of an event with a fraction of a magnitude, and
could not represent a developmental effect unrelated in size to the current state deficit.**
`ACCEPTED-AND-FIXED`. Permanence is now an explicit event with probability drawn from the
brain-structure shard's own two published figures (0.03 detectable structural, 0.25 durable
neurobiological), plus a second, independent developmental pathway with its own event probability
and magnitude prior. The permanent interval is now asymmetric toward harm ([−1.65, 0.00]) instead
of symmetric around zero, which is the honest shape given that no study has followed habitual
5-6 h sleepers aged 16-19 longitudinally.

**S19 — Drowsy-driving and injury mortality was absent, and adolescent mortality is dominated by
injury.** `ACCEPTED-AND-FIXED`. A twenty-first evidence shard was commissioned during rework. The
channel is 0.03 months (0.01-0.14) conditional on being a typical licensed teenage driver, zero if
he does not drive, and is de-duplicated against the all-cause window term (11.7% overlap). It is
*smaller* than the critic expected but comparable to the entire chronic-disease window term, and
unlike every other mortality channel it acts during the exposure window.

---

## MAJOR objections

**M6 — None of the six simulated recovery policies delivered adequate sleep, and the policy the
report prescribes was absent from the menu.** `ACCEPTED-AND-FIXED`. Two adequate policies added.
Only "9 h in bed plus a 45-minute nap" achieves a positive nightly balance against the primary
need referent; 9.5 h in bed alone does not, because sustained nocturnal sleep saturates near 7.9 h.
That is now stated as the prescription rather than a bare hours number.

**S24 / M22 — The prescription exceeded the model's own sustained ceiling, unflagged.**
`ACCEPTED-AND-FIXED`. `sustained_tst` was capping no-nap policies at the *with-nap* asymptote
(8.9 h) instead of the nocturnal asymptote (7.9 h), which let the model prescribe a dose it
simultaneously called unachievable. Fixed, and a `reachability_check` now reports the probability
that his need exceeds what nocturnal sleep alone can deliver.

**M10 — The Q7 ranking placed this exposure first only because the permanence discount applied to
it was far harsher than the one applied to any comparator; the "same footing" claim was false.**
`ACCEPTED-AND-FIXED`, and this was the most misleading single claim in the draft. The comparator
column credits accumulated damage pro-rata; our mechanistic estimate credits cessation. Both bases
are now computed. On a like-for-like basis this exposure ranks **3rd of 8**, mid-band, not least
harmful. The cigarette-equivalent figure spans 0.7/day to 13.3/day depending on basis and is
therefore flagged in the report as not robust and not to be quoted as a headline.

**M15 — `route_d` applied a cardiovascular confounding-survival fraction to a cognitive outcome.**
`ACCEPTED-AND-FIXED`. Now uses the cognition-specific gradient measured by the academic shard
(cross-sectional associations shrink 3-7x against quasi-experimental designs, survival 0.14-0.33).

**M8 — `studied_deficit_h = 3.7` was a bare scalar sitting multiplicatively in every cognition
number, and the ~25x duration extrapolation was handled by nothing.** `ACCEPTED-AND-FIXED`. The
studied contrast now carries uncertainty, and an explicit duration-extrapolation factor is applied,
centred slightly above 1 with wide bounds in both directions because the three published
history-weighting forms disagree and no experiment is long enough to discriminate them.

**S17 — `cousins2018` is over-read: encoding happened during the restricted week and only
retrieval followed recovery sleep, so it does not show a persisting deficit in the faculty of
encoding.** `ACCEPTED-AND-FIXED`. Renamed and reinterpreted as the learning-loss channel: material
learned while restricted stays less well learned. The report now states explicitly that this is
knowledge not acquired, not a permanent ability change.

**S13 — "Every immune marker normalised given adequate recovery sleep" is contradicted by the
project's own immune shard.** `ACCEPTED-AND-FIXED` in wording: the claim is now conditioned on
recovery *dose*, since the one study that varied recovery while holding restriction constant found
abnormalities persisting after 8 h of recovery and resolving only after 10 h or a nap plus 8 h.

**M19 — The g-loading discount was clipped, piling 12% of the mass on a boundary atom.**
`ACCEPTED-AND-FIXED`: truncated by resampling instead of clipped.

**M14 — The multiverse was too small and omitted the choices that move the answer.**
`ACCEPTED-AND-FIXED`: 6 branches to 18, with the sleep-need referent added. Spread ratio rose from
1.39 to 2.38, which is a more honest statement of model dependence.

**S21 — The academic channel was parameterised and never reported.** `ACCEPTED-AND-FIXED`. Now
reported with both a linear and a saturating transport, because the per-hour coefficient is
identified over 20-40 minute sleep changes and applying it linearly to a 2.8 h deficit is a 5-9x
extrapolation. This is plausibly the largest real cost of the exposure.

**M7 — Publication-bias diagnostics were computed, reported, and then not propagated.**
`ACCEPTED-AS-LIMITATION`. Egger, PET-PEESE and trim-and-fill are computed and reported per
parameter, and the memory shard's finding that bias inflates sleep-memory effects (0.44 to 0.28
after correction) is stated in the report. They are not propagated into the primary posterior
because with k = 1-5 per parameter these estimators are too unstable to correct with; PET-PEESE on
five studies has enormous variance. Correcting would move the estimates toward zero, so this
choice is conservative with respect to harm, and it is disclosed rather than silently made.

**M9 — The predictive-versus-mean choice is applied to only some inputs.**
`ACCEPTED-AS-LIMITATION`. The predictive distribution is used for the pooled effect parameters,
which is where between-study heterogeneity lives and where the individual-versus-average
distinction bites. It is documented in the report that this choice is what makes the vigilance
interval cross zero, and both the mean CI and the predictive interval are published in
`results.json` for every pooled parameter so a reader can substitute.

**M11 — The G3 rescue is circular: the sign-reconciliation operation is fitted to the reference
extractor's answer and cannot fail.** `ACCEPTED-AS-LIMITATION`, and the criticism is correct. The
gate ledger now states that G3 **fails raw** and that the sign-reconciled figure is not an
independent pass. The substantive defence is separate from the statistic: an independent
adjudicator went to the primary sources for all nine disputed effects and found 8 of 9 disputes
were caused by our codebook, with `spec/gates.md` carrying a sign convention that never propagated
to the extraction instructions. That is direct evidence about the cause, not a fitted rescue. The
remediation is the explicit per-construct canonicalisation now in `analysis_set.py`.

**M12 — `extraction_error_sd()` uses the sign-reconciled ICC while the gate is applied to the raw
figure, and its scale constant is too small.** `ACCEPTED-AS-LIMITATION`, documented in the
docstring. The term is a small variance addition; making it larger widens intervals, so the
current setting is anti-conservative by a modest amount. Disclosed rather than fixed because
re-deriving it properly requires a second blinded round.

**S3 / S4 — The SD of individual need rests on n = 15, and "sleep need" is defined by the most
sleep-sensitive test in the battery then used as the denominator for unrelated outcomes.**
`ACCEPTED-AS-LIMITATION`. The SD was widened from 0.70 to 0.80 h and hard bounds replaced the
clip, but the criticism stands: this is the weakest-evidenced parameter in the model and it is the
one the value-of-information analysis identifies as most worth measuring. Stated as such in the
report and in the measurement protocol.

**S5 / S6 / Contrarian 1.1-1.4 — Two thirds of the exposure posterior sits on calibrations the
measurement shard disfavours, and a sustained 3.2 h/night deficit for 1040 nights is not
consistent with the observable facts about a functioning student.** `ACCEPTED-AS-LIMITATION`, and
partly addressed. The deficit fell to 2.81 h with the referent fix. The calibration remains a
mixture rather than the shard's single recommendation, because model averaging over defensible
calibrations is the more honest treatment than adopting one; but the report now states the
contrarian's low-end exposure explicitly, and the multiverse shows the full range. The critics are
right that the central deficit is at the high end of what is plausible.

**S16 — The vigilance point estimate is read as a measurement when its interval spans "no deficit"
to "pathological".** `ACCEPTED-AS-LIMITATION` and now stated in exactly those terms in the report.

**S20 — "Slow-wave sleep is preserved" is partly a stage-scoring artefact.**
`ACCEPTED-AS-LIMITATION`; the report states the preservation finding and this caveat together, and
notes it does not rescue 5-6 h nights.

**S23 — The 21% disorder posterior is a base rate wearing a posterior's clothes and its
composition may be backwards.** `ACCEPTED-AS-LIMITATION`. Reported with its components and with
the shard's own admission that every likelihood ratio in it is a construction from published means
rather than a measured diagnostic accuracy, because no study has validated any sleep questionnaire
against an objective circadian standard in adolescents. The report keeps the actionable part (the
specific features that would change the answer) and drops any claim to precision.

**S25 — The pessimism of the recovery projections is an arithmetic consequence of the contested
need parameter.** `ACCEPTED-AND-FIXED` by the referent correction; recovery percentages rose
materially, and the adequate policies added under M6 reach 89% at one year.

---

## Objections rejected

**M13 — The tau prior `2 x median(se)` is a double use of the data.** `REJECTED-WITH-REASON` as a
defect, `ACCEPTED` as a documentation requirement. The critic's own quantification found it
produces the *widest* intervals of any option short of 4x, so it is conservative rather than
anti-conservative; and the alternative of a fixed absolute scale is worse here because the
parameters live on scales differing by two orders of magnitude (Hedges' g near 1, log hazard
ratios near 0.01), so a single fixed scale would be uninformative on one and dominant on the
other. The finding that the prior scale alone determines whether the vigilance interval excludes
zero is accepted and stated in the report.

**S8 / S9 — The residual causal fractions are too generous / too stingy.**
`REJECTED-WITH-REASON` in both directions, since the two critics disagreed about the sign. The
mortality fraction of 0.25 is bracketed by the shard's measured attenuation range (0-28% survives
genetic instrumentation, 7-63% survives covariate adjustment) and the psychiatric non-causal share
of 0.55-0.70 is taken from three independent estimates. Both are carried as distributions, not
points, and the E-values are published so a reader can see that a confounder of strength ~1.5
would erase the mortality association entirely.

**Contrarian's central thesis, that the damage is negligible.** `REJECTED-WITH-REASON`, on the
contrarian's own evidence. Its recomputation moved the numbers a long way and still could not
reach zero: all 21 cells of its sensitivity grid returned a negative vigilance effect and a
positive sleep debt, and 89.5% of its own favourable posterior left the subject in net debt. Its
strongest specific finding — that the learning-loss channel rests on k = 1 while two age-matched
nulls in the corpus cannot enter any pool because they carry `se: null` — is accepted and now
disclosed in the report as a one-directional data-integrity limitation.

**Contrarian's claim that the report is too reassuring about the prescription.**
`ACCEPTED-WITH-REASON` (against its own mandate). It is right that a 9-9.5 h target derived from a
need prior resting on 15 subjects should not be issued ahead of the measurement that would collapse
the interval. The report now leads the prescription with the ad-lib measurement protocol and gives
the population-prior target as a starting point rather than a conclusion.

---

## Unresolved

None blocking. Four items are carried as explicit limitations that further work would need to
address rather than defects in the current numbers: the `se: null` exclusion of qualitative nulls
from inverse-variance pools (one-directional, favours harm), the unpropagated publication-bias
correction (one-directional, favours harm), the extraction-error variance term's derivation, and
the fact that the sleep-need parameter — the most influential in the model — rests on the thinnest
evidence base of any parameter used.
