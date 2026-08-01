#!/usr/bin/env python3
"""Independently re-execute every answer's verification program.

The solvers each reported running their own checks. That is their claim, not evidence.
This runs every `verify_code` block in a fresh subprocess and compares the actual output
against the recorded `verify_output`, so a solver that mis-transcribed a result -- or
never ran the code at all -- is caught here rather than by whoever studies from the key.
"""
from __future__ import annotations

import concurrent.futures as cf
import glob
import json
import pathlib
import re
import subprocess
import sys
import tempfile

HARVEST = pathlib.Path(__file__).resolve().parent.parent
NUM = re.compile(r"-?\d+\.?\d*(?:[eE][-+]?\d+)?")


def run_one(rec):
    code = rec.get("verify_code")
    if not code:
        return {**rec, "_status": "NO_CODE"}
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as fh:
        fh.write(code)
        path = fh.name
    try:
        p = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        return {**rec, "_status": "TIMEOUT", "_actual": ""}
    finally:
        pathlib.Path(path).unlink(missing_ok=True)

    out = (p.stdout or "").strip()
    if p.returncode != 0:
        return {**rec, "_status": "ERROR", "_actual": (p.stderr or "")[-300:]}
    line = next((l for l in out.splitlines() if l.strip().startswith("CHECK")), out.splitlines()[-1] if out.splitlines() else "")
    recorded = (rec.get("verify_output") or "").strip()

    # Compare the numbers in the CHECK line rather than the string, since Monte Carlo
    # output legitimately differs in trailing digits between runs on different machines.
    a, b = NUM.findall(line), NUM.findall(recorded)
    status = "MATCH"
    if not recorded:
        status = "NO_RECORDED"
    elif len(a) != len(b):
        status = "SHAPE_DIFF"
    else:
        for x, y in zip(a, b):
            try:
                fx, fy = float(x), float(y)
            except ValueError:
                if x != y:
                    status = "DIFF"
                    break
                continue
            tol = max(2e-3 * max(abs(fx), abs(fy)), 2e-3)
            if abs(fx - fy) > tol:
                status = "DIFF"
                break
    # A CHECK line is only meaningful if its two halves agree with each other.
    self_ok = None
    if len(a) >= 2:
        try:
            fx, fy = float(a[0]), float(a[-1])
            self_ok = abs(fx - fy) <= max(5e-3 * max(abs(fx), abs(fy)), 5e-3)
        except ValueError:
            self_ok = None
    return {**rec, "_status": status, "_actual": line, "_self_consistent": self_ok}


def main() -> int:
    recs = []
    for f in sorted(glob.glob(str(HARVEST / "answers" / "solved_*.json"))):
        recs.extend(json.load(open(f, encoding="utf-8")))
    print(f"{len(recs)} answers; running verifications...", file=sys.stderr)

    results = []
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for i, r in enumerate(ex.map(run_one, recs), 1):
            results.append(r)
            if i % 25 == 0:
                print(f"  {i}/{len(recs)}", file=sys.stderr, flush=True)

    import collections
    tally = collections.Counter(r["_status"] for r in results)
    selfbad = [r for r in results if r.get("_self_consistent") is False]

    print("\nverification replay")
    for k, v in tally.most_common():
        print(f"  {k:14s} {v}")
    print(f"\nCHECK lines whose two halves disagree: {len(selfbad)}")
    for r in selfbad:
        print(f"   {r['review_id']}: {r['_actual'][:130]}")
    bad = [r for r in results if r["_status"] in ("ERROR", "TIMEOUT", "DIFF", "SHAPE_DIFF")]
    if bad:
        print(f"\nreplay problems ({len(bad)}):")
        for r in bad:
            print(f"   {r['review_id']:12s} {r['_status']:12s} actual={r.get('_actual','')[:90]!r}")
            print(f"                 recorded={(r.get('verify_output') or '')[:90]!r}")

    json.dump(results, open(HARVEST / "answers" / "verification_replay.json", "w"),
              ensure_ascii=False, indent=1)
    ok = tally.get("MATCH", 0)
    withcode = len(recs) - tally.get("NO_CODE", 0)
    print(f"\n{ok}/{withcode} verification programs reproduced their recorded result")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
