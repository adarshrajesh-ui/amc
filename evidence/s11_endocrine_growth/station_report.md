# Station report — s11_endocrine_growth

## What I did

Screened **63 candidate records** across 26 executed PubMed queries plus Europe PMC full-text searches;
**included 33**, yielding **65 effect estimates** in schema-validated YAML (`_build_records.py`
regenerates and validates all of them; last run: `33 records, 65 effects, 0 schema errors`, and all 65
effects carry a verbatim `quote`).

Retrieval routes used: PubMed E-utilities (esearch / esummary / efetch), Crossref `/works/{DOI}` for
every DOI, Europe PMC `fullTextXML`, NCBI PMC `efetch`, OpenAlex for open-access status, and the WHO
CDN for the growth-reference data file.

Full text obtained for 6 records (Leproult 2011 via PMC4445839, Reynolds 2012 via PMC3402517, Killick
2015 via PMC4858168, Balbo 2010 via PMC2902103, Magee 2010 via PMC2925323, WHO 2007 growth reference).
The rest are abstract-only, marked as such, and their `notes` state what could not be read.

## Verification

**Zero identifier failures.** All 34 DOIs and PMIDs submitted resolved to the expected titles. Notably,
two DOIs I constructed by pattern-guessing (`10.1186/s12889-025-21674-y`,
`10.1186/s12902-025-01903-6`) resolved to *entirely different articles* on Crossref; I discarded them
and pulled the real DOIs (`10.1186/s12889-025-21637-3`, `10.1186/s12902-025-01936-x`) from PubMed
`articleids`. That is exactly the failure mode the verification rule exists to catch.

Two records were **excluded because their content was unretrievable even though their identifiers
verified**, rather than recorded with reconstructed numbers:

- **Roche & Davila 1972**, *Pediatrics* 50(6):874-80, "LATE ADOLESCENT GROWTH IN STATURE" (PMID
  4673900, doi 10.1542/peds.50.6.874). Both identifiers verified; PubMed carries no abstract and the
  AAP full text is paywalled. This was the seed I most wanted for the growth-cessation timeline. Its
  function is served by the WHO 2007 reference table (which I parsed directly) plus Gupta 2020.
- **Kelly 2014**, *JCEM* 99(6):2104-12, age-based height-velocity reference ranges (PMID 24601728, doi
  10.1210/jc.2013-4455). Verified; the age-specific percentile tables sit in paywalled figures and PMC
  efetch returns "the publisher of this article does not allow downloading."

**Spiegel 2000** (the crux GH paper) is closed access — OpenAlex `oa_status: closed`, and
journals.physiology.org serves a Cloudflare interstitial. I recorded its abstract findings directly and
sourced the *direction* of the 24-h GH change secondhand from Magee 2010, whose reference list I parsed
programmatically to confirm that its reference [41] is in fact Spiegel 2000. Both records carry
`secondhand_via` fields.

## Where reality differed from the task hints

1. **"Van Cauter's work on age-related changes in SWS and GH secretion (JAMA, approx 2000)"** — exists
   exactly as described (PMID 10938176), but it is an **age-gradient study with no sleep-restriction
   exposure in it at all**. It cannot support any inference about sleep restriction. Its genuine value
   here is the 16–25 y slow-wave-sleep baseline (18.9%, SEM 1.3) and the ageing comparator
   (−372 µg GH/decade).
2. **"Leproult & Van Cauter (JAMA, approx 2011)"** — exists exactly as described (PMID 21632481) and
   the age match is excellent (mean 24.3 y). But it is a **two-page research letter with n=10** from a
   flyer-recruited convenience sample, with the rested condition always run first, and its headline
   effect is only just significant (P=.049; my derived interval on the daytime contrast is −20.6% to
   −0.1%).
3. **The redistribution-vs-loss crux is answered by a paper the task did not name.** Brandenberger &
   Weibel 2004 (*J Sleep Res*, PMID 15339260) measured GH every 10 min over 24 h in day workers and
   night workers and found the sleep pulse = 52.8 ± 3.5% of 24-h production, blunted under displaced
   sleep but **fully compensated by waking pulses so that "the total amount of GH secreted during the
   24 h was constant."** That is the direct measurement the question needed.
4. **The testosterone finding does not replicate cleanly, and the discrepancies are informative rather
   than noise.** Reynolds 2012 found nothing at a *harsher* dose (4 h × 5 nights, p=0.089). Schmid 2012
   found nothing when the 4 h of sleep sat in the *second* half of the night — which is the college
   student's pattern. NHANES 2011–2016 found the *opposite sign* in men aged 20–40 (OR 3.62 for high
   testosterone at ≤6 h). I recorded all of them.
5. **There is no meta-analysis of experimental sleep restriction and cortisol.** I searched for one
   under six formulations. The closest quantitative synthesis is a case-control meta-analysis of
   chronic *insomnia disorder* (Dressle 2022, SMD 0.50), a different exposure — and within it the
   association between the extent of objective sleep loss and the cortisol difference was itself
   non-significant.
6. **No cohort study of adolescent sleep duration and final adult height exists.** See the gap below.

## My confidence, by verdict

| Verdict | Confidence | Why |
|---|---|---|
| GH is redistributed, not lost | **High** | Converging direct 24-h measurement (Brandenberger), the biphasic compensatory profile (Spiegel), and the mechanistic fact that slow-wave sleep is *gained* under 5 h restriction (Leproult 2011). Three independent lines, all one direction. |
| Final adult height loss ≈ 0 (ceiling ~0.7 cm) | **Very high** | Rests on growth-plate arithmetic from an authoritative reference table I parsed myself, not on the sleep literature. Robust to being wrong about every hormone finding: 3.65 cm is all that existed to lose, and 0.40 cm/y remained by 18. |
| Testosterone −10 to −13%, fully reversible | **Moderate-high on the direction, high on the reversibility** | The point estimate rests on n=10 with P=.049 and is contradicted at a harsher dose and in the closest-matched observational age band. The *reversibility* is better supported than the effect itself. |
| Cortisol: evening-confined, ~0 at 5 h | **Moderate** | Well quantified at 4 h (Guyon, n=13) but the interval at the subject's 5–6 h dose is my interpolation between one null (Leproult 2011) and one acute extrapolation (Leproult 1997), and I have flagged it as such. |
| Nothing persists after normalisation | **Moderate-high** | Five separate recovery datasets all null or fully recovered, but none followed a *chronically* restricted subject for more than 3 weeks after normalisation. |
| Bone and pubertal timing: no effect | **Moderate-high for bone, high that puberty is moot** | Two clean nulls at the right dose (Swanson 2022, Depner 2021), but both are small and underpowered, so these are weak nulls rather than strong evidence of no effect. |

## Biggest gap in the evidence for this domain

**There is no prospective cohort — with any exposure measure, self-reported or actigraphic — that
follows adolescents through the end of growth and reports attained adult height as a function of sleep
duration.** Nothing. The entire "sleep affects growth" belief rests on (a) uncontrolled pre/post
adenotonsillectomy series in prepubertal children with obstructive sleep-disordered breathing, whose
one randomised counterpart delivered adiposity rather than stature, and (b) the physiological
observation that GH is secreted during slow-wave sleep — which turns out not to imply 24-h GH loss.

For this particular subject the gap does not matter, because the growth-plate arithmetic settles the
question regardless of what such a cohort would show: an exposure beginning at 16.0 y acts on 3.65 cm
of median residual growth, and 0.40 cm/y by 18. **But it matters enormously for the 13-year-old version
of this question**, where 20–25 cm of growth remain, the pubertal spurt is ongoing, and none of the
evidence in this shard applies. If the pipeline ever needs to answer the adolescent-height question for
a younger exposure onset, this shard's answer must not be reused.

Two secondary gaps worth flagging to the pooler:

1. **No hormone study included a 16–19 year old.** The youngest relevant sample means are 24.3 y
   (Leproult 2011) and 27–29 y elsewhere; Killick 2015's range reaches down to 19. A 19-year-old's
   testosterone baseline is at or near lifetime peak and his slow-wave sleep is at its lifetime maximum
   (18.9% of the sleep period at 16–25 y vs 3.4% at 36–50 y), so both the GH reserve and the
   testosterone headroom are *larger* than in any studied sample. Transportability is assumed, not
   measured, and the assumption is conservative.
2. **Comparator inflation is systematic, not incidental.** Every lab study here except Schmid 2012 and
   Leproult 1997 uses a 10–12 h in-bed comparator. Balbo 2010's 8-h re-study of 9 of Spiegel 1999's 11
   men shows evening cortisol at 8 h landing *between* the 4 h and 12 h conditions, which means roughly
   half the canonical effect is the comparator being supranormal. A pooler that treats these contrasts
   as "restricted vs normal" will overstate every effect in this shard by something like a factor of
   two.
