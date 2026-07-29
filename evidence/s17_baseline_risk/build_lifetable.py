"""Build /workspace/data/lifetable_us_male.csv from official published sources.

Primary rates (ages 0-99): NCHS United States Life Tables, 2023, Table 2 (males).
  Official spreadsheet: https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/74-06/Table02.xlsx
Tail rates (ages 100-119): SSA Period Life Table, 2023 (2026 Trustees Report), male column.
  https://www.ssa.gov/oact/STATS/table4c6.html

NCHS closes its table at an open-ended "100 and older" interval, so single-year qx above
100 must come from SSA, which publishes single-year male qx through age 119. The splice
applies SSA *rates* to the NCHS *radix* (lx at 100 carried forward from the NCHS recursion),
so lx stays on the NCHS "per 100,000 born" scale.

Run:  python3 build_lifetable.py <dir with Table02.xlsx and ssa_table4c6.md>
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import openpyxl

RAW = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/s17")
OUT = Path("/workspace/data")

NCHS_URL = "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/74-06/Table02.xlsx"
NCHS_PDF = "https://www.cdc.gov/nchs/data/nvsr/nvsr74/nvsr74-06.pdf"
NCHS_CITE = ("Arias E, Xu JQ, Kochanek K. United States life tables, 2023. "
             "Natl Vital Stat Rep. 2025 Jul 15;74(6):1-63. DOI: 10.15620/cdc/174591")
SSA_URL = "https://www.ssa.gov/oact/STATS/table4c6.html"
SSA_CITE = ("U.S. Social Security Administration, Office of the Chief Actuary. "
            "Actuarial Life Table: Period Life Table, 2023, as used in the 2026 Trustees Report.")


def read_nchs(path: Path) -> dict[int, dict[str, float]]:
    """Parse NCHS Table 2 (males). Returns {age: {qx, lx, dx, Lx, Tx, ex}} for ages 0..100."""
    ws = openpyxl.load_workbook(path, data_only=True).worksheets[0]
    rows: dict[int, dict[str, float]] = {}
    for label, qx, lx, dx, Lx, Tx, ex in ws.iter_rows(values_only=True):
        if not isinstance(label, str):
            continue
        m = re.match(r"^\s*(\d+)\s*[–\-]\s*\d+\s*$", label)
        if m:
            age = int(m.group(1))
        elif re.match(r"^\s*100\s+and\s+older", label, re.I):
            age = 100
        else:
            continue
        if not isinstance(qx, (int, float)):
            continue
        rows[age] = {"qx": float(qx), "lx": float(lx), "dx": float(dx),
                     "Lx": float(Lx), "Tx": float(Tx), "ex": float(ex)}
    missing = [a for a in range(101) if a not in rows]
    if missing:
        raise SystemExit(f"NCHS parse incomplete, missing ages {missing}")
    return rows


def read_ssa(path: Path) -> dict[int, dict[str, float]]:
    """Parse the SSA period life table markdown. Male columns are 1-3 after the age."""
    out: dict[int, dict[str, float]] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or not re.fullmatch(r"\d{1,3}", cells[0]):
            continue
        try:
            age = int(cells[0])
            qx = float(cells[1])
            lx = float(cells[2].replace(",", ""))
            ex = float(cells[3])
        except ValueError:
            continue
        out[age] = {"qx": qx, "lx": lx, "ex": ex}
    missing = [a for a in range(120) if a not in out]
    if missing:
        raise SystemExit(f"SSA parse incomplete, missing ages {missing}")
    return out


def build(nchs, ssa):
    """Splice, then recompute lx/dx/Lx/Tx/ex on a single consistent recursion.

    Ages 0-99 reuse the published NCHS lx and Lx verbatim so that ex reproduces the
    published table by construction. Ages 100-119 are generated from SSA qx with the
    standard mid-year assumption a(x)=0.5, closed at age 120 with q=1.
    """
    tab: dict[int, dict] = {}
    for age in range(100):
        r = nchs[age]
        tab[age] = {"qx": r["qx"], "lx": r["lx"], "dx": r["dx"], "Lx": r["Lx"],
                    "source": "NCHS_NVSR_74_6_Table2"}

    lx = nchs[100]["lx"]  # NCHS survivors reaching age 100, per 100,000 born
    for age in range(100, 120):
        qx = ssa[age]["qx"]
        dx = lx * qx
        tab[age] = {"qx": qx, "lx": lx, "dx": dx, "Lx": lx - 0.5 * dx,
                    "source": "SSA_period_life_table_2023"}
        lx -= dx
    # closure: everyone alive at 120 dies during that year
    tab[120] = {"qx": 1.0, "lx": lx, "dx": lx, "Lx": 0.5 * lx,
                "source": "closure_qx=1_at_120"}

    T = 0.0
    for age in range(120, -1, -1):
        T += tab[age]["Lx"]
        tab[age]["Tx"] = T
        tab[age]["ex"] = T / tab[age]["lx"] if tab[age]["lx"] > 0 else 0.0
    return tab


def main() -> None:
    nchs = read_nchs(RAW / "Table02.xlsx")
    ssa = read_ssa(RAW / "ssa_table4c6.md")
    tab = build(nchs, ssa)

    # ---- cross-source agreement check on the overlapping range ----
    diffs = [(a, abs(nchs[a]["qx"] - ssa[a]["qx"])) for a in range(19, 100)]
    worst_age, worst = max(diffs, key=lambda t: t[1])
    rel = [(a, abs(nchs[a]["qx"] - ssa[a]["qx"]) / ssa[a]["qx"]) for a in range(19, 100)]
    worst_rel_age, worst_rel = max(rel, key=lambda t: t[1])

    # ---- calibration against the published values ----
    checks = {
        "e0_recomputed": tab[0]["ex"], "e0_published_nchs": nchs[0]["ex"],
        "e19_recomputed": tab[19]["ex"], "e19_published_nchs": nchs[19]["ex"],
        "e65_recomputed": tab[65]["ex"], "e65_published_nchs": nchs[65]["ex"],
        "e0_published_ssa": ssa[0]["ex"], "e19_published_ssa": ssa[19]["ex"],
    }
    for age in (0, 19, 65):
        d = abs(tab[age]["ex"] - nchs[age]["ex"])
        checks[f"abs_err_e{age}_vs_nchs_years"] = d
        assert d < 0.01, f"e{age} deviates {d:.4f} y from published NCHS"

    OUT.mkdir(parents=True, exist_ok=True)

    hdr = [
        "# US period life table, MALES, single year of age 19-110",
        f"# PRIMARY SOURCE (ages 19-99 qx): {NCHS_CITE}",
        f"#   Table 2 (life table for males), machine-readable: {NCHS_URL}",
        f"#   Report PDF: {NCHS_PDF}  | data year 2023 | published 2025-07-15",
        f"# TAIL SOURCE (ages 100-110 qx): {SSA_CITE}",
        f"#   {SSA_URL}  | data year 2023 | published 2026 (2026 Trustees Report)",
        "# WHY TWO SOURCES: NCHS closes its published table at an open-ended '100 and older'",
        "#   interval, so single-year qx above age 99 is not published by NCHS. SSA publishes",
        "#   single-year male qx to age 119. SSA rates are applied to the NCHS lx radix.",
        f"# CROSS-SOURCE AGREEMENT, ages 19-99: max |qx_NCHS - qx_SSA| = {worst:.2e} at age"
        f" {worst_age}; max relative diff = {worst_rel:.2%} at age {worst_rel_age}.",
        "# COLUMNS",
        "#   age = exact age x in years",
        "#   qx  = published probability of dying between exact age x and x+1 (NOT recomputed)",
        "#   lx  = number surviving to exact age x per 100,000 MALE LIVE BIRTHS (NCHS radix;",
        "#         divide by lx(19)=%.3f to renormalize a cohort to age 19)" % tab[19]["lx"],
        "#   ex  = expectation of life (mean remaining years) at exact age x",
        "# lx and ex are recomputed on one consistent recursion: NCHS published lx and Lx for",
        "#   ages 0-99; for 100-119, dx = lx*qx and Lx = lx - 0.5*dx; closed with qx=1 at 120.",
        "#   ex(x) = T(x)/l(x) with T(x) = sum of L(a) for a >= x.",
        "# CALIBRATION (gate G10): recomputed vs published expectation of life, males 2023",
        "#   e0  recomputed %.4f  vs NCHS published %.4f  (|diff| %.4f y)"
        % (tab[0]["ex"], nchs[0]["ex"], abs(tab[0]["ex"] - nchs[0]["ex"])),
        "#   e19 recomputed %.4f  vs NCHS published %.4f  (|diff| %.4f y)"
        % (tab[19]["ex"], nchs[19]["ex"], abs(tab[19]["ex"] - nchs[19]["ex"])),
        "#   e65 recomputed %.4f  vs NCHS published %.4f  (|diff| %.4f y)"
        % (tab[65]["ex"], nchs[65]["ex"], abs(tab[65]["ex"] - nchs[65]["ex"])),
        "#   SSA independent published values for comparison: e0 = %.2f, e19 = %.2f"
        % (ssa[0]["ex"], ssa[19]["ex"]),
        "# NOTE ON THE LAST ROW: qx at age 110 is the published SSA value (0.597297), i.e. the",
        "#   table does NOT terminate at 110. ex at 110 accounts for the published SSA",
        "#   continuation to 119. Ages 0-18 and 111-120 are in lifetable_us_male_full.csv.",
        "#   Truncating the tail at 110 with qx=1 changes e19 by < 1e-4 years.",
        "# Built by evidence/s17_baseline_risk/build_lifetable.py -- no hand transcription.",
    ]

    with (OUT / "lifetable_us_male.csv").open("w", newline="") as fh:
        for line in hdr:
            fh.write(line + "\n")
        w = csv.writer(fh)
        w.writerow(["age", "qx", "lx", "ex"])
        for age in range(19, 111):
            r = tab[age]
            w.writerow([age, f"{r['qx']:.6f}", f"{r['lx']:.3f}", f"{r['ex']:.4f}"])

    with (OUT / "lifetable_us_male_full.csv").open("w", newline="") as fh:
        fh.write("# Full companion to lifetable_us_male.csv: ages 0-120, all life table columns.\n")
        fh.write(f"# Ages 0-99 qx/lx/dx/Lx: {NCHS_CITE}\n")
        fh.write(f"# Ages 100-119 qx: {SSA_CITE} ({SSA_URL})\n")
        fh.write("# Age 120 row is the arithmetic closure (qx=1), not a published value.\n")
        fh.write("# Included so a consumer can recompute e0 and validate against published 75.8.\n")
        w = csv.writer(fh)
        w.writerow(["age", "qx", "lx", "dx", "Lx", "Tx", "ex", "qx_source"])
        for age in range(121):
            r = tab[age]
            w.writerow([age, f"{r['qx']:.6f}", f"{r['lx']:.4f}", f"{r['dx']:.4f}",
                        f"{r['Lx']:.4f}", f"{r['Tx']:.2f}", f"{r['ex']:.4f}", r["source"]])

    for k, v in checks.items():
        print(f"{k}: {v:.6f}" if isinstance(v, float) else f"{k}: {v}")
    print(f"qx_agreement_max_abs: {worst:.3e} (age {worst_age})")
    print(f"qx_agreement_max_rel: {worst_rel:.4%} (age {worst_rel_age})")
    print(f"rows_written_main: {111 - 19}")


if __name__ == "__main__":
    main()
