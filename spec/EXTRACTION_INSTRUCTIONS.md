# Extraction instructions (read before doing anything)

You are one shard of a parallel evidence-extraction factory. The factory is estimating the
health and cognitive damage of ~3 years of chronic sleep restriction in a **specific 18-year-old
male entering his second year of college** (weekday sleep ~5-6 h from age 16 to 19, weekend and
holiday sleep ~7-8 h, occasional 3-4 h nights before exams, occasional 10-11 h weekend nights).

Your job is **not** to write prose or draw conclusions. Your job is to produce machine-readable,
verified, citable effect estimates that a downstream Bayesian meta-analysis will consume.

## Hard rules

1. **NEVER fabricate.** Not a DOI, not a PMID, not an n, not an effect size, not a confidence
   interval. A fabricated number is a catastrophic defect that poisons the entire pipeline.
2. **Every number must come from a source you actually retrieved.** For each extracted effect you
   MUST paste the verbatim supporting sentence (or the verbatim table/abstract fragment) into the
   record's `notes` or `quote` field. If you cannot quote it, you may not extract it.
3. **Verify every identifier programmatically** before writing the record:
   ```bash
   curl -s "https://api.crossref.org/works/<DOI>" | head -c 600
   curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=<PMID>" | head -c 900
   ```
   Also useful: search PubMed for real PMIDs rather than recalling them:
   ```bash
   curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=10&term=<url-encoded+query>"
   ```
   If an identifier does not resolve, either find the correct one or set the field to `null` and
   set `access_tier: secondhand` with an explanation. Do not guess identifiers.
4. If a study you were told to look for does not exist, or its real numbers differ from what the
   task description implies, **report reality**. Seed names in your task are hints, not truth.
5. Prefer, in order: recent dose-response meta-analyses -> systematic reviews -> primary studies
   inside them -> newer primaries the reviews missed.
6. Screen **at least 25 candidate records**. Log every exclusion with a reason.
7. Prefer effects measured in 16-25 year olds. When you must use midlife or elderly cohorts, say so
   in `population.adolescent_match` so the downstream model can inflate uncertainty.

## Evidence tiers (assign one per study)

- `T1` randomized / within-subject lab restriction or recovery protocol
- `T2` quasi-experiment or instrumental variable (school start times, time-zone boundaries, DST)
- `T3` Mendelian randomization
- `T4` prospective cohort with objective exposure (actigraphy / PSG)
- `T5` prospective cohort with self-reported exposure
- `TX` cross-sectional, normative/descriptive, guideline, or life table (context only, not primary)

## Output

Write to `/workspace/evidence/<YOUR_SHARD_ID>/`:

- One YAML file per study: `<study_id>.yaml`
- `screening_log.md` — a table of every record screened: identifier, decision, reason.
- `station_report.md` — what you did, what you could not find, your own confidence, and the
  single biggest gap in the evidence for your domain.

### YAML record template (conform to `/workspace/spec/effect.schema.json`)

```yaml
study_id: vandongen2003          # lowercase, [a-z0-9_]
citation: "Van Dongen HP, Maislin G, Mullington JM, Dinges DF. The cumulative cost of additional wakefulness: dose-response effects on neurobehavioral functions and sleep physiology from chronic sleep restriction and total sleep deprivation. Sleep. 2003;26(2):117-126."
doi: "10.1093/sleep/26.2.117"
pmid: "12683469"
verification:
  crossref_ok: true              # what the curl actually returned
  pubmed_ok: true
  resolved_title: "The cumulative cost of additional wakefulness: dose-response effects on neurobehavioral functions and sleep physiology from chronic sleep restriction and total sleep deprivation."
  status: VERIFIED
access_tier: full_text           # full_text | abstract_only | secondhand
secondhand_via: null
design: lab_restriction_within_subject
tier: T1
n: 48
n_studies_pooled: null
population:
  age_mean: 29.0
  age_range: [21, 38]
  pct_female: null
  country: "US"
  adolescent_match: fair_adult   # exact_16_19|good_young_adult|fair_adult|poor_midlife|poor_elderly|mixed
effects:
  - outcome_domain: cognition
    outcome_construct: pvt_lapses
    exposure: {type: chronic_restriction, dose_h: 6, referent_h: 8, duration_days: 14, contrast_label: "6h TIB vs 8h TIB, 14 nights"}
    scale: hedges_g
    unit: null
    value: -0.9
    se: 0.3
    ci: [-1.5, -0.3]
    conversion_formula: "g = (M_restricted - M_control)/SD_pooled; SD_pooled derived from reported SE and n"
    from_figure: true
    inferred_from_ci: false
    direction_note: "negative = worse vigilance (more lapses) under restriction"
    covariates: []
    followup_years: null
    cohort_family: null
    quote: "PASTE THE VERBATIM SENTENCE THAT SUPPORTS THIS NUMBER HERE"
rob:
  tool: RoB2
  judgement: some_concerns
  notes: "no blinding possible; small n; healthy volunteers only"
funding: "NIH"
notes: "free-text; include any conversion arithmetic you performed"
shard: "s01_cognition_dose_response"
```

## Effect-size conversion guidance

- If a paper reports mean +/- SD per condition and n, compute Hedges' g and its SE and record the
  arithmetic in `conversion_formula`.
- If a paper reports only a p-value and n, back out an approximate SE and set
  `inferred_from_ci: true`.
- If a paper reports a ratio (RR/HR/OR) with a CI, record `log_rr`/`log_hr`/`log_or` and
  `se = (log(upper) - log(lower)) / 3.92`.
- If a paper reports a per-hour linear coefficient, use `scale: per_hour_beta` and give `unit`.
- Never invent an SE. If none is derivable, set `se: null` and explain in `notes`.
- Record `cohort_family` (e.g. `UK_Biobank`, `Whitehall_II`, `NHANES`, `MESA`) for every
  observational effect so the pooler can avoid double-counting.

## Return to the orchestrator

A compact summary: shard id, number screened, number included, the 3-6 most decision-relevant
effect estimates with their numbers and tiers, every identifier that failed verification, and the
single biggest evidence gap in your domain. Be terse and numeric.
