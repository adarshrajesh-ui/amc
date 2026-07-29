# Acceptance gates

A gate failure halts the pipeline. Every gate result is logged to `reports/gate_log.md`.

| ID | Station | Gate | Threshold |
|---|---|---|---|
| G0 | S0 | All evidence records validate against `effect.schema.json` | 100% |
| G1 | S1 | Records screened per shard | >= 25 |
| G2 | S2 | Citation verification against Crossref and/or PubMed | 100% of primary-model records `VERIFIED` |
| G3 | S3 | Blinded re-extraction agreement, continuous effect values | ICC >= 0.90 |
| G4 | S3 | Blinded re-extraction agreement, categorical fields (design, tier, RoB) | kappa >= 0.80 |
| G5 | S4 | Exposure engine reproduces closed-form envelope for total debt | within 20% |
| G6 | S5 | Cohort-family de-duplication applied; no family contributes > 1 effect per outcome without RVE | enforced |
| G7 | S6 | Monte Carlo draws | >= 1e6 |
| G8 | S6 | MCMC diagnostics where MCMC used | R-hat < 1.01, ESS > 1000, 0 divergences |
| G9 | S8 | Calibration regression tests reproducing published pooled estimates | >= 5 targets, each within MC error |
| G10 | S8 | Life table reproduces published national life expectancy | within 0.3 years |
| G11 | S8 | Unit + property tests | all pass |
| G12 | S9 | Red-team critiques filed | 3 (methodologist, domain skeptic, contrarian) |
| G13 | S9 | Objections resolved in writing | 100%, none unresolved |
| G14 | S9 | Full rework loops completed | >= 2 |
| G15 | S10 | Every headline number carries point estimate, 95% interval, confidence grade | 100% |

## Units convention

- Sleep duration: hours of **total sleep time (TST)** unless explicitly labelled `TIB`.
- Debt: hours, cumulative, signed so that **positive = hours of sleep owed**.
- Effect sign: negative = worse for the subject on cognition/health scales; log-scale ratios
  positive = elevated risk. Every record must state `direction_note`.
- Time constants: days.
- Life expectancy: months (report years only in appendix).

## Confidence ledger grades

Each headline number gets four letter grades A-D:

1. **Quantity** — A: >=10 independent studies; B: 5-9; C: 2-4; D: 1 or indirect only.
2. **Quality/tier** — A: T1/T2 dominant; B: T3/T4 dominant; C: T5 dominant; D: cross-sectional or mechanistic only.
3. **Transportability** — A: exposure and age both match a 16-19 year old; B: young adult; C: midlife extrapolated; D: age-mismatched or exposure-mismatched.
4. **Model dependence** — A: robust across the whole multiverse; B: sign stable, magnitude varies < 2x; C: magnitude varies > 2x; D: sign flips across defensible specifications.

Any number graded D on transportability or model dependence is labelled a **GUESS** in the report body.
