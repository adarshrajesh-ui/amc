SHELL := /bin/bash
PY    := python3
SRC   := src

.PHONY: all validate verify agreement exposure synthesis lifetable recovery model test report clean gates

all: validate verify agreement model test gates
	@echo
	@echo "=== pipeline complete: results.json and REPORT.md regenerated from a fixed seed ==="

## --- S0/S2: schema validation and citation verification -------------------------------
validate:
	$(PY) $(SRC)/validate_evidence.py --strict

verify:
	$(PY) $(SRC)/verify_refs.py

# Re-verify without touching the network, using the cached API responses.
verify-offline:
	$(PY) $(SRC)/verify_refs.py --offline

## --- S3: blinded re-extraction agreement ----------------------------------------------
sample:
	$(PY) $(SRC)/make_blind_sample.py

agreement:
	cd $(SRC) && $(PY) agreement.py

## --- S4-S6: engines --------------------------------------------------------------------
exposure:
	cd $(SRC) && $(PY) exposure.py

synthesis:
	cd $(SRC) && $(PY) synthesis.py

lifetable:
	cd $(SRC) && $(PY) lifetable.py

recovery:
	cd $(SRC) && $(PY) recovery.py

analysis-set:
	cd $(SRC) && $(PY) analysis_set.py

## --- S6/S7: propagation, bias analysis, multiverse, figures ---------------------------
model:
	cd $(SRC) && $(PY) model.py

## --- S8: verification ------------------------------------------------------------------
test:
	$(PY) -m pytest tests/ -q

## --- S10: report -----------------------------------------------------------------------
report:
	cd $(SRC) && $(PY) build_report.py

gates:
	cd $(SRC) && $(PY) gate_report.py

clean:
	rm -rf $(SRC)/__pycache__ tests/__pycache__ .pytest_cache
