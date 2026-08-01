#!/usr/bin/env python3
"""Apply the post-hoc screens to the corpus and score the v2 control run.

Three inputs, all produced by agents that did not collect the data:
  - reddit_account_screen.json : per-record bot/promotional provenance verdicts
  - sig_level_resolution.json  : internship-vs-new-grad resolutions with quoted evidence
  - control_adjudication_v2.json : blind verdicts on the sealed control set

Screens are applied as demotions with a stated reason rather than deletions, except
where an account is demonstrably automated -- a question whose only witness is a bot has
no witness at all.
"""
from __future__ import annotations

import json
import pathlib

HARVEST = pathlib.Path(__file__).resolve().parent.parent


def load(name):
    p = HARVEST / "reports" / name
    return json.loads(p.read_text()) if p.exists() else None


def main() -> int:
    qs = [json.loads(l) for l in open(HARVEST / "questions.jsonl", encoding="utf-8")]
    by_id = {q["id"]: q for q in qs}

    # 1. Reddit provenance screen
    screen = load("reddit_account_screen.json") or {"results": []}
    bot_hits = promo_hits = 0
    for r in screen.get("results", []):
        q = by_id.get(r.get("id"))
        if not q:
            continue
        v = r.get("verdict")
        if v in ("BOT", "PROMOTIONAL"):
            sole = len({a["source_url"] for a in q["attestations"]}) == 1
            acct = r.get("account", "unknown")
            note = f"account @{acct} classified {v} ({r.get('confidence','?')} confidence): {str(r.get('evidence',''))[:180]}"
            if sole:
                q["tier"] = "REJECT"
                q["tier_reason"] = f"sole witness is a non-candidate account. {note}"
            else:
                q["tier"] = "D"
                q["tier_reason"] = f"one attestation is a non-candidate account. {note}"
            q["provenance_flag"] = v
            bot_hits += v == "BOT"
            promo_hits += v == "PROMOTIONAL"

    # 2. SIG level resolution. Only applied where the resolver quoted evidence, and
    #    never to promote something into the internship set on a weak basis.
    lev = load("sig_level_resolution.json") or {"results": []}
    applied = {"internship": 0, "new_grad": 0, "experienced": 0}
    skipped_low = 0
    for r in lev.get("results", []):
        q = by_id.get(r.get("id"))
        rl = r.get("resolved_level")
        if not q or rl in (None, "unknown"):
            continue
        if not str(r.get("basis", "")).strip():
            continue
        if rl == "internship" and r.get("confidence") == "low":
            skipped_low += 1
            continue
        q["level"] = rl
        q["level_basis"] = r.get("basis", "")[:300]
        applied[rl] = applied.get(rl, 0) + 1

    with open(HARVEST / "questions.jsonl", "w", encoding="utf-8") as fh:
        for q in qs:
            fh.write(json.dumps(q, ensure_ascii=False) + "\n")

    print("REDDIT PROVENANCE SCREEN")
    print(f"  records screened     {len(screen.get('results', []))}")
    print(f"  demoted/rejected     {bot_hits} bot, {promo_hits} promotional")
    print("\nSIG LEVEL RESOLUTION")
    for k, v in applied.items():
        print(f"  -> {k:12s} {v}")
    print(f"  low-confidence internship claims declined: {skipped_low}")

    # 3. Score the v2 control run
    sealed = {i["presented_as"]: i for i in json.loads((HARVEST / "spec" / "controls_v2_sealed.json").read_text())}
    adj = load("control_adjudication_v2.json")
    if adj:
        tp = tn = fp = fn = 0
        for a in adj:
            t = sealed[a["presented_as"]]["truth"]
            v = a["verdict"]
            tp += t == "FAKE" and v == "FAKE"
            fn += t == "FAKE" and v == "REAL"
            tn += t == "REAL" and v == "REAL"
            fp += t == "REAL" and v == "FAKE"
        print("\nCONTROL RUN v2")
        print(f"  forgeries rejected   {tp}/20  (gate needs >=19)")
        print(f"  real retained        {tn}/20  (gate needs >=16)")
        json.dump({"forgeries_caught": tp, "reals_kept": tn,
                   "gate_precision_pass": tp >= 19, "gate_recall_pass": tn >= 16},
                  open(HARVEST / "reports" / "control_score_v2.json", "w"), indent=1)

    import collections
    sh = [q for q in qs if q["tier"] != "REJECT"]
    sig = [q for q in sh if q["firm"] == "Susquehanna International Group"]
    sigqti = [q for q in sig if q["role_track"] == "quant_trader" and q["level"] == "internship"]
    print(f"\nCORPUS AFTER SCREENS")
    print(f"  shipped {len(sh)} | rejected {len(qs)-len(sh)}")
    print(f"  tiers {dict(collections.Counter(q['tier'] for q in sh))}")
    print(f"  SIG {len(sig)} | SIG QT internship {len(sigqti)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
