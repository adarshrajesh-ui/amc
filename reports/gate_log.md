# Gate ledger

**14 of 16 gates pass cleanly.** 2 are qualified: G3 fails as literally specified and was remediated, and G4 passes on the field the model actually uses while failing on two it does not. Both are described below rather than silently relaxed, because a clean scoreboard obtained by redefining the gate is worth nothing.

| Gate | Station | Requirement | Threshold | Observed | Result |
|---|---|---|---|---|---|
| G0 | S0 | All evidence records validate against effect.schema.json | 100% | 597 records, 0 problems | PASS |
| G1 | S1 | Records screened per shard | >= 25 | min included per shard = 15 across 20 shards | PASS |
| G2 | S2 | Citation verification against Crossref and/or PubMed | 100% verified | 593 verified + 4 official-source, 0 unverified of 597 | PASS |
| G3 | S3 | Blinded re-extraction agreement on continuous values | ICC >= 0.90 | raw 0.7216 (FAILS), sign-reconciled 0.9706 | FAIL-REMEDIATED |
| G4 | S3 | Blinded re-extraction agreement on categorical fields | kappa >= 0.80 | tier 0.8958 (passes), design 0.7713 (fails), risk-of-bias 0.3601 (fails) | PARTIAL |
| G5 | S4 | Exposure engine reproduces the closed-form envelope | within 20% | 5.8% | PASS |
| G6 | S5 | Cohort-family de-duplication applied | enforced | 40 multi-study cohort families detected and collapsed in pooling | PASS |
| G7 | S6 | Monte Carlo draws | >= 1e6 | 1,000,000 | PASS |
| G8 | S6 | MCMC diagnostics where MCMC used | R-hat < 1.01, ESS > 1000, 0 divergences | R-hat 1.0000/1.0002, ESS 3564/3708, divergences 0 (asserted in tests) | PASS |
| G9 | S8 | Calibration regression tests reproducing published estimates | >= 5 targets | 43 tests total; 8 named published-target reproductions | PASS |
| G10 | S8 | Life table reproduces published national life expectancy | within 0.3 y | e19 error 0.00025 y, e65 error 0.00037 y | PASS |
| G11 | S8 | Unit and property tests | all pass | 43 passed | PASS |
| G12 | S9 | Red-team critiques filed | 3 | 3 filed: contrarian, domain_skeptic, methodologist | PASS |
| G13 | S9 | Objections resolved in writing | 100% | see reports/objection_resolution.md | PASS |
| G14 | S9 | Full rework loops completed | >= 2 | 2 (loop 1: sign canonicalisation, task-key collision, verifier normalisation; loop 2: need referent, mortality dose-response, IQ route structure, k<=2 intervals, academic and injury channels, ceiling coherence) | PASS |
| G15 | S10 | Every headline number has estimate, interval and grade | 100% | see REPORT.md dashboard | PASS |

## Notes on gates that failed, partially passed, or needed remediation

**G1 (PASS)** — Screening counts per shard were 40-313; the figure shown is INCLUDED records, which is lower than screened by design.

**G2 (PASS)** — 593 of 597 identifiers resolve and title-match; the remaining 4 are official statistical products with no DOI, verified by domain. No fabricated citation was found.

**G3 (FAIL-REMEDIATED)** — FAILS AS SPECIFIED. The gate is written on the raw values and the raw weighted-mean ICC is 0.7216. It reaches 0.9706 only after allowing a whole-record sign flip, and one reviewer correctly pointed out that the reconciliation is fitted to the reference extractor's answer and therefore cannot fail, so the reconciled figure is NOT an independent pass. The substantive defence is separate from the statistic: an independent adjudicator went to the primary sources for all nine disputed effects and found 8 of 9 disputes were caused by a sign convention that existed in spec/gates.md but never propagated into the extraction instructions. That is evidence about the cause. Remediated by explicit per-construct canonicalisation in analysis_set.py, but no post-remediation blinded round was run, so the remediation is unverified by independent measurement.

**G4 (PARTIAL)** — PARTIAL. Tier, which is what the model weights on, passes at 0.90. Design misses at 0.77 because the tier codebook has no slot for meta-analytic designs. Risk of bias fails badly at 0.36, so risk of bias carries NO numeric weight in the primary model and is reported descriptively only. Weighting on a judgement with kappa 0.36 would be spurious precision.

**G5 (PASS)** — Initially failed at 121%, which exposed two real bugs: the pre-exposure baseline years were summed into the headline debt, and the time-in-bed and self-report corrections were compounding. Both fixed.

**G6 (PASS)** — dedupe_by_cohort collapses families by inverse variance and floors the SE at the best single SE. Reviewer note carried as a limitation: the grouping key is nullable, so families that no shard labelled cannot be detected.

**G8 (PASS)** — Required a non-centered parameterisation; the centered form produced 146 divergences. NUTS also agrees with exact grid marginalisation to 0.0005 on mu, which is a stronger check than the diagnostics alone.

**G11 (PASS)** — Caught three real bugs: trim-and-fill mislabelled and one-sided, and the TIB-to-TST regression extrapolating to predict more sleep than time in bed.
