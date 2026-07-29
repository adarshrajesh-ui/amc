"""Verify that the verbatim quotations and load-bearing numbers in the contrarian report
actually appear in the source files they are attributed to.

Each check names a source file and a substring that must be present in it. Whitespace is
normalised before matching so that line wrapping in either file does not cause a false failure.

Usage:  python3 redteam_check_quotes.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

# (label, source file relative to repo root, required substring)
CHECKS: list[tuple[str, str, str]] = [
    # --- 1.1 calibration
    ("s06 recommends reverse regression",
     "evidence/s06_sleep_need_measurement/exposure_priors.md",
     "Use the reverse regression. Do not subtract the mean bias."),
    ("s06: the two methods disagree by more than any other uncertainty",
     "evidence/s06_sleep_need_measurement/exposure_priors.md",
     "There are two defensible ways to turn a self-report into an estimate of true sleep, and **they "
     "disagree by 1.3-2.0 h for this subject — which is larger than any other uncertainty in the "
     "calculation.**"),
    ("s06: the sign of the correction is the biggest open question",
     "evidence/s06_sleep_need_measurement/exposure_priors.md",
     "READ THIS FIRST: the sign of the correction is the biggest open question in this shard"),
    ("white2026ffcws beta 0.19",
     "evidence/s06_sleep_need_measurement/white2026ffcws.yaml",
     "beta = 0.19 (95% CI: 0.13, 0.26)"),
    ("white2026ffcws outcome is sleep-period time, not TST",
     "evidence/s06_sleep_need_measurement/white2026ffcws.yaml",
     "SLEEP-PERIOD me"),
    ("cespedes2016hchs beta 0.333",
     "evidence/s06_sleep_need_measurement/cespedes2016hchs.yaml",
     "0.333"),

    # --- 1.2 efficiency at restricted TIB
    ("campbell2024 per-condition TST",
     "evidence/s02_cognition_meta/campbell2024.yaml",
     "401.7"),
    ("campbell2024 10 h TIB TST 525.8",
     "evidence/s02_cognition_meta/campbell2024.yaml",
     "525.8"),
    # campbell2021's Table 1 is quoted verbatim in the shard synthesis document rather than being
    # carried as effect rows in campbell2021.yaml, so the check points there.
    ("campbell2021 sleep onset latency contrast (Table 1, via shard synthesis)",
     "evidence/s03_memory_consolidation/architecture_under_restriction.md",
     "| Sleep onset latency (min) | 3.7 ± 1.3 | 11.2 ± 0.7 | 21.4 ± 1.4 |"),
    ("campbell2021 attribution of that table",
     "evidence/s03_memory_consolidation/architecture_under_restriction.md",
     "PMID `33507305`"),
    ("campbell2021 N3 gained 3 min at 7 h vs 10 h TIB",
     "evidence/s03_memory_consolidation/architecture_under_restriction.md",
     "**+3 min**"),

    # --- 1.3 referent is a satiation ceiling
    ("klerman2008 asymptote quote",
     "evidence/s06_sleep_need_measurement/klerman2008.yaml",
     "asymptotic values"),
    ("klerman2008 younger asymptote 8.9",
     "evidence/s06_sleep_need_measurement/klerman2008.yaml",
     "8.9"),
    ("kitamura2016 optimal-habitual correlation",
     "evidence/s06_sleep_need_measurement/kitamura2016.yaml",
     "0.514"),
    ("wild2018 optimum 7.38",
     "evidence/s02_cognition_meta/wild2018.yaml",
     "7.38"),
    ("nsf: 6 h may be appropriate",
     "evidence/s06_sleep_need_measurement/hirshkowitz2015nsf.yaml",
     "may be appropriate"),
    ("nsf: some individuals longer or shorter with no adverse effects",
     "evidence/s06_sleep_need_measurement/hirshkowitz2015nsf.yaml",
     "might sleep longer or shorter than the recommended times with no adverse effects"),

    # --- 1.4 unit matching
    ("nsf notes: single largest systematic error",
     "evidence/s06_sleep_need_measurement/hirshkowitz2015nsf.yaml",
     "single largest systematic error available to the downstream model"),

    # --- 1.5 lo2016 adjudication
    ("adjudication: extraction hard-rule 2 violation",
     "reports/adjudication.md",
     "hard-rule 2"),
    ("adjudication: the conversion does not hold",
     "reports/adjudication.md",
     "conversion does not hold"),
    ("agreement.json records the lo2016 sign disagreement",
     "reports/agreement.json",
     "lo2016"),

    # --- 1.6 sleep architecture
    ("kopasz2010 architecture verbatim",
     "evidence/s03_memory_consolidation/kopasz2010.yaml",
     "5% of slow wave sleep"),
    ("kopasz2010 70% REM",
     "evidence/s03_memory_consolidation/kopasz2010.yaml",
     "70% of REM sleep"),
    ("kumral2023 declarative spindle slope",
     "evidence/s03_memory_consolidation/kumral2023.yaml",
     "0.21"),

    # --- 1.7 learning channel
    ("cousins2018 cohort overlap warning",
     "evidence/s03_memory_consolidation/cousins2018.yaml",
     "COHORT OVERLAP"),
    ("voderholzer2011 title claim",
     "evidence/s03_memory_consolidation/voderholzer2011.yaml",
     "does not affect long-term recall"),
    ("voderholzer2011 five-arm similarity quote",
     "evidence/s03_memory_consolidation/voderholzer2011.yaml",
     "highly similar levels of"),
    ("kopasz2010 title claim",
     "evidence/s03_memory_consolidation/kopasz2010.yaml",
     "No persisting effect of partial sleep curtailment"),

    # --- 1.8 hard-outcome nulls
    ("binks1999 no FSIQ decrement",
     "evidence/s02_cognition_meta/binks1999.yaml",
     "3.6"),
    ("campbell2024 working memory null",
     "evidence/s02_cognition_meta/campbell2024.yaml",
     "Sternberg"),
    ("duraccio2024 healthy-weight null verbatim",
     "evidence/s01_cognition_dose_response/duraccio2024.yaml",
     "No differences emerged for adolescents with healthy weight"),
    ("cappuccio2011 total CVD 1.03",
     "evidence/s08_cardiovascular/cappuccio2011.yaml",
     "1.03"),
    ("irwin2016 IL-6 objective 0.29",
     "evidence/s10_immune/irwin2016_inflammation_meta.yaml",
     "ES 0.29; 95% CI 0.05 - 0.52"),
    ("irwin2016 binning-dilution caveat",
     "evidence/s10_immune/irwin2016_inflammation_meta.yaml",
     "lumps a 6.5 h sleeper with a 4 h sleeper"),
    ("widome2023 adolescent BMI null",
     "evidence/s09_obesity_bmi/widome2023.yaml",
     "0.02"),
    ("hayes2023 adult BMI MR null",
     "evidence/s09_obesity_bmi/hayes2023.yaml",
     "0.039"),

    # --- 1.9 design gradients
    ("s09 gradient verbatim",
     "evidence/s09_obesity_bmi/station_report.md",
     "0.35"),
    ("s09 three strongest designs all null",
     "evidence/s09_obesity_bmi/station_report.md",
     "all null"),

    # --- 1.10 mortality
    ("yin2017 nadir 7 h",
     "evidence/s13_mortality/yin2017.yaml",
     "7"),
    ("liu2017 male null at 6 h",
     "evidence/s13_mortality/liu2017.yaml",
     "1.02"),
    ("zhao2023 self-report vs PSG divergence",
     "evidence/s13_mortality/zhao2023.yaml",
     "1.37"),
    ("akerstedt2019 weekend catch-up null",
     "evidence/s13_mortality/akerstedt2019.yaml",
     "1.09"),
    ("itani2017 below six hours",
     "evidence/s13_mortality/itani2017.yaml",
     "6"),

    # --- 1.11 reversibility
    ("leproult2011 testosterone",
     "evidence/s11_endocrine_growth/leproult2011.yaml",
     "10.3" ),
    ("depner2019 title claim",
     "evidence/s05_recovery_kinetics/depner2019.yaml",
     "fails to prevent metabolic dysregulation"),
    ("s05 short-window share",
     "evidence/s05_recovery_kinetics/station_report.md",
     "39%"),

    # --- section 3, the residuals I could not explain away
    ("campbell2024 maturation-equivalent years",
     "evidence/s02_cognition_meta/campbell2024.yaml",
     "3.85"),
    # 6.70 h in the report is a unit conversion of the quoted 401.7 min, checked above; the
    # per-condition minutes are the primary datum.
    ("campbell2024 8.5 h TIB condition TST",
     "evidence/s02_cognition_meta/campbell2024.yaml",
     "470.1"),
    ("arora2013 diary vs single-item",
     "evidence/s06_sleep_need_measurement/arora2013.yaml",
     "actigraph"),
    ("girschik2012 small group numbers caveat",
     "evidence/s06_sleep_need_measurement/girschik2012.yaml",
     "group numbers were small"),
    ("guedes2016 boys worse bias",
     "evidence/s06_sleep_need_measurement/guedes2016.yaml",
     "1.9"),
    ("short2018 9.35 h optimal sustained attention",
     "evidence/s06_sleep_need_measurement/short2018sleepneed.yaml",
     "9.35"),
    ("prather2015 rhinovirus OR 4.5",
     "evidence/s10_immune/prather2015_rhinovirus.yaml",
     "4.5"),
    ("yang2022 persisting grey-matter difference",
     "evidence/s15_brain_structure/yang2022.yaml",
     "0.61"),
    ("binks1999 baseline screening imbalance",
     "evidence/s02_cognition_meta/binks1999.yaml",
     "2.7"),
]


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def main() -> int:
    fails = []
    cache: dict[str, str] = {}
    for label, rel, needle in CHECKS:
        p = ROOT / rel
        if not p.exists():
            fails.append(f"{label}: MISSING FILE {rel}")
            continue
        if rel not in cache:
            cache[rel] = norm(p.read_text())
        if norm(needle) not in cache[rel]:
            fails.append(f"{label}: NOT FOUND in {rel}\n      looked for: {needle!r}")

    print(f"quote/number checks: {len(CHECKS) - len(fails)} of {len(CHECKS)} found in source")
    if fails:
        print(f"\nFAILURES ({len(fails)}):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("Every quoted string and load-bearing number is present in the file it is attributed to.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
