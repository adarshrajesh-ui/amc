"""Red-team perturbation harness. Mirrors model.build()'s Q2/Q3 chain so single
analytic choices can be swapped and the headline movement measured."""
from __future__ import annotations
import sys, math, json
sys.path.insert(0, "/workspace/src")
import numpy as np
import analysis_set as ASET
import exposure as EXP
import synthesis as SYN
import lifetable as LT

SEED = 20260728
N = 400_000
IQ_SD = 15.0

ASET_R = ASET.resolve()
DERIVED = ASET.DERIVED_PARAMS
ESD = ASET.extraction_error_sd()

_exp = EXP.simulate(n_draws=250_000, seed=SEED, tib_scenario="mixed", calibration="mixed")


def q(x, label=""):
    x = np.asarray(x, float)
    return dict(median=float(np.median(x)), mean=float(np.mean(x)),
                ci95=[float(np.percentile(x, 2.5)), float(np.percentile(x, 97.5))])


def fmt(d):
    return "%+7.3f [%+7.3f, %+7.3f]" % (d["median"], d["ci95"][0], d["ci95"][1])


def prep(name, extraction=True, drop_nested=False):
    eff = [dict(e) for e in ASET_R[name]["effects"]]
    if drop_nested and name == "domain_profile_chronic_restriction":
        eff = [e for e in eff if "overall_neurocognitive" in e["construct"]]
    y = np.array([e["value"] for e in eff], float)
    se = np.array([e["se"] for e in eff], float)
    if extraction and ESD > 0:
        se = np.sqrt(se ** 2 + ESD ** 2)
    rows = SYN.dedupe_by_cohort([{**e, "se": s} for e, s in zip(eff, se)])
    return (np.array([r["value"] for r in rows], float),
            np.array([r["se"] for r in rows], float))


def run(tau_mult=2.0, tau_fixed=None, use_pred=True, drop_nested=False,
        weights=(0.35, 0.25, 0.30, 0.10), studied_deficit=3.7, gamma_lo=0.8, gamma_hi=1.5,
        route_c_chronic=False, extraction_on_all_g=False, deficit_source="mean",
        seed=SEED, n=N, verbose=True, tag=""):
    rng = np.random.default_rng(seed)
    d = _exp["draws"]

    def rs(a):
        a = np.asarray(a, float)
        return a[rng.integers(0, len(a), n)]

    key = {"mean": "mean_nightly_deficit_exposure_h",
           "ewma": "steady_state_ewma_deficit_h"}[deficit_source]
    deficit = np.clip(rs(d[key]), 0.0, None)
    mean_tst = rs(d["mean_tst_exposure_h"])

    def pool(name):
        y, se = prep(name, drop_nested=drop_nested)
        ts = tau_fixed if tau_fixed is not None else max(np.median(se) * tau_mult, 1e-3)
        b = SYN.pool_bayes_grid(y, se, tau_scale=ts, seed=SEED)
        return b

    pvt_b, dom_b = pool("pvt_g_large_dose"), pool("domain_profile_chronic_restriction")
    obs_b = pool("habitual_short_sleep_g_observational")
    keyd = "pred_draws" if use_pred else "mu_draws"

    gamma = rng.uniform(gamma_lo, gamma_hi, n)
    transport = np.clip(deficit / studied_deficit, 0.0, 2.0) ** gamma

    g_vig = rs(pvt_b[keyd]) * transport
    g_dom = rs(dom_b[keyd]) * transport

    de = ASET_R["iq_discount_vigilance_to_g"]["effects"][0]
    disc = np.clip(rng.normal(de["value"], de["se"], n), 0.05, 0.60)
    route_a = g_vig * disc * IQ_SD

    re_ = ASET_R["reasoning_g_total_deprivation"]["effects"][0]
    se_b = math.sqrt(re_["se"] ** 2 + ESD ** 2) if extraction_on_all_g else re_["se"]
    g_reason = rng.normal(re_["value"], se_b, n)
    route_b = g_reason * rng.uniform(0.5, 0.9, n) * transport * IQ_SD

    fe = ASET_R["fsiq_direct_measurement"]["effects"][0]
    cs = rng.uniform(0.5, 0.9, n) if route_c_chronic else 1.0
    route_c = rng.normal(fe["value"], fe["se"], n) * transport * cs

    conf = rng.uniform(*DERIVED["cvd_confounding_survival"]["interval"], n)
    route_d = rs(obs_b[keyd]) * conf * IQ_SD

    w = np.asarray(weights, float)
    which = rng.choice(4, size=n, p=w / w.sum())
    iq = np.select([which == 0, which == 1, which == 2], [route_a, route_b, route_c], route_d)
    perm = iq * rng.beta(1.2, 18.0, n)

    out = {"tag": tag, "transport": q(transport), "vig_g": q(g_vig), "dom_g": q(g_dom),
           "route_a": q(route_a), "route_b": q(route_b), "route_c": q(route_c),
           "route_d": q(route_d), "iq": q(iq), "iq_perm": q(perm),
           "p_perm_lt_-1": float(np.mean(perm < -1)),
           "pvt_tau": pvt_b["tau_median"], "pvt_mu": pvt_b["mu_median"],
           "dom_mu": dom_b["mu_median"], "vig_crosses_zero": bool(q(g_vig)["ci95"][1] > 0)}
    if verbose:
        print(f"--- {tag}")
        for k in ("transport", "vig_g", "dom_g", "route_a", "route_b", "route_c", "route_d", "iq", "iq_perm"):
            print(f"    {k:10s} {fmt(out[k])}")
        print(f"    pvt tau={out['pvt_tau']:.3f} mu={out['pvt_mu']:+.3f} dom mu={out['dom_mu']:+.3f} "
              f"vig CI crosses 0: {out['vig_crosses_zero']}  P(perm<-1pt)={out['p_perm_lt_-1']:.4f}")
    return out


if __name__ == "__main__":
    run(tag="BASELINE (as published)")
