# Sleep-debt damage estimation

A reproducible quantitative estimate of the health and cognitive damage from ~3 years of chronic
sleep restriction in one specific 18-year-old, and of what recovery requires.

**Read [`REPORT.md`](REPORT.md).** Every number in it is regenerable with `make all` from a fixed
seed.

## What this is

A staged evidence-synthesis pipeline ("software factory"): 21 parallel evidence-acquisition shards,
schema-enforced handoffs, blinded re-extraction with inter-rater gates, Bayesian hierarchical
meta-analysis, Monte Carlo propagation, bias analysis, an adversarial review board, and two full
rework loops.

| | |
|---|---|
| Evidence records | 621, across 21 domain shards |
| Effect estimates | 2,099 (1,116 with a usable standard error) |
| Citation verification | 611 identifiers resolved against Crossref and PubMed with title matching; 0 unverified |
| Blinded re-extraction | 140 targets re-extracted by 6 independent agents |
| Monte Carlo draws | 1,000,000, fixed seed |
| Tests | 43, including calibration regression against published pooled estimates |
| Acceptance gates | 14/16 clean pass, 2 qualified and described |

## Layout

```
spec/          JSON schemas, extraction codebook, acceptance gates
evidence/      one YAML record per study, plus screening logs and per-shard syntheses
src/           exposure, synthesis, simulation, bias, life table, recovery, report compiler
tests/         unit, property and calibration-regression tests
figures/       dose-response, forest, recovery, multiverse, value-of-information, comparators
reports/       verification, agreement, adjudication, 3 red-team critiques, objection log, gates
results.json   every headline number, machine readable, with intervals
REPORT.md      the human answer
```

## Reproducing

```bash
pip install numpy scipy statsmodels matplotlib pandas jsonschema pytest pyyaml numpyro arviz
make all          # validate, verify, agreement, model, tests, gates
make verify-offline   # re-verify citations from the cached API responses, no network
```

## Prompts

- [`prompts/sleep-debt-damage-estimate.md`](prompts/sleep-debt-damage-estimate.md) — the
  software-factory prompt this repository was built from.
