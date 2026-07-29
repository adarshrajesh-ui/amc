# Station report — shard `s14_dementia_amyloid`

Domain: long-run neurodegeneration. The glymphatic / amyloid-clearance mechanism, and the epidemiology of
sleep duration and incident dementia.

---

## 1. What I did

**Retrieval and verification.** Built four helper scripts (`pm.py` for PubMed/Crossref, `getfull.sh` for
PMC full texts, `h2t.py` for HTML→text, plus `verify.py`) and screened **77 individually identified
candidate records** (plus two categories of non-primary source excluded en bloc) across
five literatures: mouse glymphatic physiology, acute human CSF/PET amyloid experiments, sleep-duration
dementia epidemiology including dose-response and follow-up-stratified meta-analyses, bidirectional
Mendelian randomization, and longitudinal amyloid/tau biomarker cohorts. Included **38 records** yielding
**104 effect estimates**.

**Verification is complete and machine-checked.** All **40/40** (PMID, DOI) pairs I checked — the 38
included studies, plus the `howard2024` corrigendum and the Park 2025 protocol, both verified without
being extracted — resolve on **both** Crossref and PubMed,
with DOI cross-consistency and title-similarity checks (`verify.py` → `verification_raw.json`,
`verify_out.txt`). **No identifier failed verification.** Three records initially failed on
title-similarity because Crossref registers the main title without its subtitle; `verify.py` contains an
explicit documented rule for that case (Crossref title an exact prefix of the PubMed title with matching
DOI) rather than a silent override.

**Every number is traceable.** I wrote `audit_quotes.py`, which normalises unicode/PDF artefacts and
confirms that each of the **104/104** `quote` fields appears in text this shard actually downloaded. Five
quotes splice non-contiguous passages with an ellipsis; the auditor verifies each segment independently
and reports them separately. One quote I had reconstructed across non-adjacent table rows
(`blattner2020`) was caught by this audit and rewritten as the contiguous fragment, with the omission
documented in the record.

**Schema compliance.** `validate.py` checks all 38 records against `effect.schema.json` plus shard-level
invariants (study_id matches filename, every effect quoted, log-scale point estimate inside its own CI,
SE consistent with the CI to within 20%, no non-positive SEs). **38/38 valid, 0 warnings.** It also caught
three open-ended `age_range` values I had encoded as `[65, null]`; these are now `null` with the
eligibility criterion quoted in the notes.

**Arithmetic.** All ratio measures were converted to `log_rr`/`log_hr`/`log_or` with
`se = (ln(upper) − ln(lower))/3.92`, with the arithmetic written into each `conversion_formula`. Where no
SE was derivable I set `se: null` and said why rather than inventing one — this happens in **43 of the 104
effects**, and §6.4 explains how the pooler must handle them. Roughly 24 of the 43 are sources that
reported only a direction, so `value` is a sign placeholder (0 or 1) rather than a magnitude; the other
~19 are genuine magnitudes printed without a usable interval, most importantly `howard2024`'s
short-follow-up brief-sleep estimate (see §3) and `xiong2024`'s headline hazard ratios. That 24/19 split
comes from a crude test on the stored `value` and is indicative only — the `direction_note` on each
effect is authoritative, which is why §6.4 tells the pooler to read it rather than trust a rule.

**Corrections I made to my own work.** Four study_ids were placeholders or misattributions and were
renamed to the true first author after checking the author lists: `zhang2024`→`you2024`,
`lucey2020`→`blattner2020`, `sleepmed2024mr`→`xiang2024`, `psychres2024`→`xiong2024`,
`brainage2026`→`sun2026`, and a sixth (`cacciaglia2026`→`tortcolet2026`) was corrected before the record
was finalised. Verification was re-run after each rename.

---

## 2. What I found that changes the picture

Five findings were not anticipated by the task framing and materially change the channel's assessment.

**(a) The human kinetics refute the clearance interpretation.** `lucey2018` used stable isotope labelling
to separate production from clearance and found turnover rates unchanged: the overnight amyloid rise
under deprivation is driven by **increased production**, not impaired glymphatic clearance. The entire
"sleep washes amyloid out of your brain" framing is a mouse-derived interpretation that the direct human
kinetic measurement does not support.

**(b) The mouse foundation is contested.** `miao2024` (Nature Neuroscience 2024) is titled "Brain
clearance is **reduced** during sleep and anesthesia" and directly contradicts `xie2013`. I extracted
both.

**(c) Partial restriction — the subject's actual exposure — moves no biomarker.** `olsson2018`: 5-8
consecutive nights of 4 h sleep produced no change in CSF Aβ38/40/42, t-tau, p-tau, NfL or GFAP, while
raising orexin 27% (p = 0.001), proving the protocol was potent. The authors attribute the null to
preserved slow-wave sleep. `ju2017` independently showed the amyloid effect is specific to slow-wave
disruption "and not for sleep duration or efficiency", and `skorucak2021` showed slow-wave homeostasis is
preserved in **adolescents** across a simulated 5-night school week at 5 h. The Lancet Commission makes
the same argument unprompted. **This is the link the chain needs and the link where it fails.**

**(d) The dose-response nadir is not where the narrative assumes.** `xu2020`, the largest dose-response
synthesis (17 cohorts in the splines), places the risk minimum at **5.6-6 h** of nocturnal sleep with
significant elevation only below 4 h or above 10 h. `wu2018` and `liang2019` put it at 7-8 h and ~7 h, so
the location is unstable — but no curve places the subject's weekday 5-6 h on a steep rising limb.

**(e) The short/long asymmetry breaks the mechanism.** Across `xu2020`, `fan2019`, `deckers2024`,
`xiong2024`, `yuan2022` and `winer2021`, **long** sleep produces the larger, more consistent and more
homogeneous dementia association (`xu2020` AD: RR 1.57, I² = 0%) while **short** sleep's AD-specific
estimate is exactly null (RR 1.02, 0.76-1.36). Meanwhile `winer2021` found long sleep has **no** amyloid
signal. So short sleep has an amyloid signal but no AD signal, and long sleep has an AD signal but no
amyloid signal. Amyloid cannot be the mediator, and the field's only mechanistic bridge does not carry
the traffic the epidemiology puts on it.

---

## 3. What I could not find, and data problems encountered

- **No human reversibility experiment exists.** Nobody has measured Aβ before deprivation, after
  deprivation, and again after recovery sleep in the same people. A targeted search returned three
  records, all rodent. My conclusion that the acute rise reverses rests on four indirect lines
  (`blattner2020`'s unchanged 36-hour mesor, p = 0.72; `lucey2018`'s production-not-clearance finding;
  `forsberg2025`'s washout crossover; `olsson2018`'s multi-night null) and is labelled moderate
  confidence, not high. **This is the thinnest load-bearing inference in the shard and I want it flagged
  as such.**
- **No study measures sleep before age 45 and dementia later.** The youngest exposure assessment in the
  entire literature is `sabia2021` at mean age 50.6 y.
- **`howard2024` contains an impossible confidence interval** in its abstract: "RR - 1·46; 95 %
  Confidence Intervals [CIs] 1·48-1·77", whose lower bound exceeds the point estimate. A corrigendum
  exists (PMID 40022863, verified) but is paywalled and I could not retrieve its content. I recorded the
  point estimate with `se: null` and documented the problem rather than reverse-engineering a plausible
  interval.
- **`you2024`'s abstract also contains a corrupted interval** ("stroke, OR 2.34 [2.1-1.37]"). I did not
  extract that effect and flagged it so no other shard silently ingests it.
- **The Lancet Commission is paywalled**; I obtained the author-accepted manuscript via Unpaywall →
  UCL Discovery, so quotes are from the accepted version rather than the typeset one.
- **16 of 38 records are abstract-only.** Where a paper reported only a direction or a percentage without
  an interval, I encoded a sign indicator with `se: null` and a `direction_note` stating explicitly that
  the effect must not be pooled as a magnitude. This affects `komlo2026`, `xiong2024`, `yuan2022`'s MR
  null, `anderson2021`'s and `guo2024`'s forward-MR nulls, and `vanwanrooij2025`.

---

## 4. My own confidence

| Claim | Confidence | Basis |
|---|---|---|
| Total sleep deprivation acutely raises human CSF/brain Aβ | **High** | 4 independent studies, consistent direction, one within-subject PET (19/20 participants) |
| The acute rise is production-driven, not clearance-driven | **High** | Direct kinetic measurement (`lucey2018`), plus `blattner2020` excluding cortisol/circadian mediation |
| Partial chronic restriction does *not* replicate the acute biomarker effect | **Moderate** | Only one direct test (`olsson2018`, n = 13) — underpowered, but mechanistically coherent with `ju2017` and `skorucak2021` |
| The acute rise reverses | **Moderate** | Four convergent indirect lines, zero direct tests |
| Short sleep duration in midlife has *some* association with later dementia | **Moderate** | `sabia2021`, `xu2020` — but bare-threshold intervals and 31% replication across reviews |
| That association is not established as causal | **High** | 8 MR analyses with a working positive control; `you2024`'s timing analysis; `howard2024`'s attenuation; `tao2026`'s design comparison; the Lancet Commission's own verdict |
| The reverse-causation share is unresolved | **High confidence that it is unresolved** | `howard2024` and `vanwanrooij2025` reach opposite conclusions with competent methods |
| Nothing supports a numeric adolescent dementia delta | **Very high** | Complete absence of relevant studies, confirmed by targeted search |

**Where I could be wrong, stated fairly.** The strongest counter-case to my conclusion is that the
absence of evidence on adolescents is genuinely just absence: the exposure has never been measured in
anyone young, MR cannot interrogate a time-limited developmental window, and adolescence is a period of
active synaptic reorganisation during which sleep may do things it does not do at 60. `komlo2026` shows
someone is testing this in mice and finding harm — via proteostasis, not amyloid. If a causal
adolescent-window effect exists, none of my evidence would detect it. What I can say is that no evidence
supports assigning it a magnitude, and that the mechanism this shard was asked to evaluate — glymphatic
amyloid clearance — is specifically the one that fails at the partial-restriction step.

The second place I could be wrong is `olsson2018`'s n of 13. A null in 13 people is weak evidence of
absence. I have leaned on it because it is the *only* direct test of the exposure that matters and
because it agrees with `ju2017`'s stage-specificity and `skorucak2021`'s adolescent slow-wave data — but
a well-powered replication could overturn this part of my reasoning.

---

## 5. The single biggest gap in the evidence for my domain

**No study has ever measured sleep in people under 45 and followed them to dementia — and the one
experiment that would settle the mechanism, whether the acute amyloid rise reverses after recovery
sleep, has never been done in humans.**

These two gaps compound. The epidemiology cannot tell us whether an adolescent exposure window exists,
because it has never sampled one. The mechanism cannot substitute for the epidemiology, because the
mechanistic chain fails at the partial-restriction step (`olsson2018`, `ju2017`, `skorucak2021`) and
because its clearance premise is refuted in humans (`lucey2018`) and contested in mice (`miao2024`).
There is therefore no route — empirical or mechanistic — from the existing evidence to a dementia-risk
number for a 19-year-old.

The most valuable single study that could close this gap already has a published protocol: `park2025`
(PMID 41614054, verified), a Whitehall II analysis of midlife short sleep with ~30 years of follow-up and
blood biomarker mediation. It is registered, in future tense, and its identifier is retained in
`verify.py` so the pipeline can pick it up on publication. Even that will have midlife exposure, not
adolescent.

---

## 6. Handling instructions for the pooler

1. **Do not pool this channel into a headline damage total.** Report it qualitatively. If a number is
   structurally required, use 0 with a wide sign-ambiguous prior.
2. **If an anchor is mandatory**, use `sabia2021` persistent short sleep: `log_hr` 0.262, SE 0.134
   (HR 1.30, 95% CI 1.00-1.69), exposure ages 50/60/70 — and carry the flag that `howard2024` reduces
   the comparable estimate to a non-significant RR 1.12 (0.95-1.29) beyond 10 years of follow-up.
3. **De-duplicate by `cohort_family`.** Every observational effect carries one. The overlaps that matter:
   **UK Biobank in some form appears in 18 effects** across six studies — `you2024` and `yuan2022`
   (cohort analyses, `UK_Biobank`), and `guo2024`, `henry2019`, `huang2020`, `anderson2021` (MR, tagged
   `UK_Biobank_exposure` / `UK_Biobank_exposure_IGAP_outcome`). **These MR studies draw sleep instruments
   from the same UK Biobank GWAS and are not independent tests.** `Whitehall_II` carries 5 effects, all
   from `sabia2021` (and the excluded protocol `park2025` will add more). Other multi-effect families:
   `Gothenburg_PSD` (4, `olsson2018` + `forsberg2025` — overlapping Swedish PSD programme), `BLSA` (4,
   `spira2013` + `spira2018`), `AMYPAD_PNHS` (4), `Knight_ADRC` (3, `lucey2019`), `BACS_Berkeley` (3,
   `winer2020`), `A4_Study` (3, `winer2021`), `WashU_SILK` (2, `lucey2018`), `WashU_SWA_disruption`
   (2, `ju2017`), `CHARLS` (2), `ELSA` (2), and the pooled IPD family for `sun2026`.
4. **43 of the 104 effects have `se: null` and none of them may be pooled as a variance-weighted
   magnitude.** Select them programmatically with `e["se"] is None` — that is the authoritative list, and
   every one explains itself in its own `conversion_formula` and `direction_note`. I deliberately did not
   hand-enumerate them here, because the two kinds below cannot be separated by any reliable automatic
   rule and a hand list would go stale. Read the `direction_note`, which always says which kind it is:
   - **Sign indicators** — `value` is a placeholder (typically 0.0 for a reported null, 1.0 for a reported
     effect) and there is *no* magnitude in the source at all. Use for direction only, or discard.
     Examples: both `komlo2026` effects, `xiong2024`'s age-stratified short-sleep reversal, the MR nulls
     in `yuan2022` / `anderson2021` / `guo2024` / `huang2020`, `olsson2018`'s biomarker null,
     `forsberg2025`, `vanwanrooij2025`, `skorucak2021`.
   - **Real magnitudes whose SE the source did not permit deriving.** Usable only if the model can accept
     an externally assumed variance, and only with the flag carried through. Examples: `xiong2024`'s
     long-sleep `log_hr` 0.4947 (from "64 % increased risk", no interval published anywhere);
     `howard2024`'s short-follow-up brief-sleep `log_rr` 0.378 (interval mis-printed in the abstract,
     corrigendum paywalled); `blattner2020`'s mesor contrast (mixed-model df = 10, so CI/3.92 would
     understate the SE); the dose-response nadirs in `wu2018`, `liang2019` and `xu2020`;
     `deckers2024`'s three vote-count proportions; `livingston2024`'s inclusion-decision indicator.
5. **Watch the sign convention on CSF Aβ42.** Acute deprivation *raises* CSF Aβ42, whereas *low* CSF
   Aβ42 is the Alzheimer's biomarker. The acute experimental change and the chronic disease marker move
   in opposite directions; reading the former as movement toward the disease profile inverts the sign.
6. **`per_hour_beta` is used for two per-PSQI-point coefficients** in `tortcolet2026` because the schema
   enum has no generic per-unit option. The `unit` field states this. These are **not** hours-of-sleep
   coefficients.
7. **Three effects carry a `probability` scale that is not a probability**: `livingston2024`'s
   inclusion-decision indicator, `deckers2024`'s replication rates (5/16 and 7/16), and `yuan2022`'s
   interaction p-value. All are documented in their `conversion_formula`.
