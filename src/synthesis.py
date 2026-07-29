"""S5 Synthesis engine: meta-analytic pooling.

Primary analysis is a Bayesian hierarchical (random-effects) model. The posterior is obtained
two independent ways so they can check each other:

  * exact marginalisation of tau on a dense grid (no sampler, no convergence question)
  * NUTS via numpyro, which supplies the R-hat / ESS diagnostics the gate requires

Agreement between the two is a verification test, not a formality: a sampler that disagrees
with the exact posterior is broken.

Frequentist REML with the Hartung-Knapp-Sidik-Jonkman adjustment is the sensitivity analysis.

Two things this module reports that a plain pooled mean would hide:

  prediction interval - the interval for a *new* study, i.e. for one individual. With
                        heterogeneous evidence this is far wider than the CI on the mean,
                        and it is the interval that actually applies to the subject.
  cohort de-duplication - effects sharing a cohort_family are collapsed, so UK Biobank does
                        not vote once per publication.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import optimize, stats

ROOT = Path(__file__).resolve().parent.parent
CAUSAL_TIERS = ("T1", "T2", "T3")


# ======================================================================================
# Frequentist pooling
# ======================================================================================
def dersimonian_laird_tau2(y: np.ndarray, v: np.ndarray) -> float:
    w = 1.0 / v
    mu = float((w * y).sum() / w.sum())
    q = float((w * (y - mu) ** 2).sum())
    df = len(y) - 1
    c = float(w.sum() - (w ** 2).sum() / w.sum())
    return max(0.0, (q - df) / c) if c > 0 else 0.0


def reml_tau2(y: np.ndarray, v: np.ndarray) -> float:
    def neg_ll(log_tau2):
        t2 = math.exp(log_tau2)
        w = 1.0 / (v + t2)
        mu = (w * y).sum() / w.sum()
        return 0.5 * (np.log(v + t2).sum() + (w * (y - mu) ** 2).sum() + math.log(w.sum()))

    if len(y) < 2:
        return 0.0
    best, best_val = 0.0, neg_ll(math.log(1e-10))
    res = optimize.minimize_scalar(neg_ll, bounds=(math.log(1e-10), math.log(100.0)),
                                   method="bounded")
    if res.success and res.fun < best_val:
        best = math.exp(res.x)
    return max(0.0, best)


def pool_frequentist(y: np.ndarray, se: np.ndarray) -> dict:
    """REML random-effects pooling with the HKSJ variance adjustment and a prediction interval."""
    y, se = np.asarray(y, float), np.asarray(se, float)
    k = len(y)
    v = se ** 2
    if k == 1:
        return {"k": 1, "mu": float(y[0]), "se": float(se[0]),
                "ci95": [float(y[0] - 1.96 * se[0]), float(y[0] + 1.96 * se[0])],
                "tau2": 0.0, "tau": 0.0, "i2": 0.0, "pi95": None, "method": "single_study"}
    tau2 = reml_tau2(y, v)
    w = 1.0 / (v + tau2)
    mu = float((w * y).sum() / w.sum())
    se_fe = math.sqrt(1.0 / w.sum())
    # Hartung-Knapp-Sidik-Jonkman
    q_hk = float((w * (y - mu) ** 2).sum() / (k - 1))
    se_hk = se_fe * math.sqrt(max(q_hk, 1.0)) if k > 1 else se_fe
    tcrit = stats.t.ppf(0.975, k - 1)
    # heterogeneity
    w_fe = 1.0 / v
    mu_fe = (w_fe * y).sum() / w_fe.sum()
    q = float((w_fe * (y - mu_fe) ** 2).sum())
    i2 = max(0.0, (q - (k - 1)) / q) * 100 if q > 0 else 0.0
    pi_half = tcrit * math.sqrt(se_hk ** 2 + tau2)
    return {
        "k": k, "mu": mu, "se": se_hk,
        "ci95": [mu - tcrit * se_hk, mu + tcrit * se_hk],
        "tau2": tau2, "tau": math.sqrt(tau2), "i2": i2, "q": q,
        "pi95": [mu - pi_half, mu + pi_half],
        "method": "REML+HKSJ",
    }


# ======================================================================================
# Bayesian pooling: exact grid marginalisation
# ======================================================================================
def pool_bayes_grid(y, se, tau_scale: float | None = None, n_draws: int = 40_000,
                    seed: int = 7, n_grid: int = 600) -> dict:
    """Hierarchical normal-normal model with a half-normal prior on tau.

    p(mu, tau | y) with mu marginally flat. tau is integrated on a grid, which is exact up
    to grid resolution and needs no convergence diagnostics.
    """
    y, se = np.asarray(y, float), np.asarray(se, float)
    k = len(y)
    if tau_scale is None:
        # Weakly informative: scaled to the typical precision of the evidence, so the prior
        # does not accidentally dominate on log-ratio scales where effects are ~0.1.
        tau_scale = max(np.median(se) * 2.0, 1e-3)
    tau_grid = np.linspace(1e-6, tau_scale * 8, n_grid)

    log_post = np.empty(n_grid)
    mu_hat = np.empty(n_grid)
    mu_sd = np.empty(n_grid)
    for i, tau in enumerate(tau_grid):
        v = se ** 2 + tau ** 2
        w = 1.0 / v
        m = (w * y).sum() / w.sum()
        s2 = 1.0 / w.sum()
        # Marginal likelihood of y given tau with mu integrated out under a flat prior:
        #   log p(y|tau) = -0.5 [ sum log(v_i + tau^2) + log(sum w_i) + sum w_i (y_i - m)^2 ]
        # up to a constant. This is the REML criterion, so the grid posterior and reml_tau2
        # are maximising the same function and must agree.
        ll = -0.5 * (np.log(v).sum() + math.log(w.sum()) + (w * (y - m) ** 2).sum())
        log_prior = -0.5 * (tau / tau_scale) ** 2          # half-normal
        log_post[i] = ll + log_prior
        mu_hat[i], mu_sd[i] = m, math.sqrt(s2)

    log_post -= log_post.max()
    post = np.exp(log_post)
    post /= post.sum()

    rng = np.random.default_rng(seed)
    idx = rng.choice(n_grid, size=n_draws, p=post)
    mu_draws = mu_hat[idx] + rng.normal(0, 1, n_draws) * mu_sd[idx]
    tau_draws = tau_grid[idx]
    # predictive distribution for one new unit (i.e. for this individual)
    pred_draws = mu_draws + rng.normal(0, 1, n_draws) * tau_draws

    return {
        "k": k, "method": "bayes_grid_halfnormal_tau",
        "tau_prior_scale": tau_scale,
        "mu_median": float(np.median(mu_draws)),
        "mu_mean": float(np.mean(mu_draws)),
        "mu_ci95": [float(np.percentile(mu_draws, 2.5)), float(np.percentile(mu_draws, 97.5))],
        "tau_median": float(np.median(tau_draws)),
        "tau_ci95": [float(np.percentile(tau_draws, 2.5)), float(np.percentile(tau_draws, 97.5))],
        "pred_median": float(np.median(pred_draws)),
        "pred_ci95": [float(np.percentile(pred_draws, 2.5)), float(np.percentile(pred_draws, 97.5))],
        "prob_harm_direction_negative": float(np.mean(mu_draws < 0)),
        "mu_draws": mu_draws, "tau_draws": tau_draws, "pred_draws": pred_draws,
    }


def pool_bayes_nuts(y, se, tau_scale: float | None = None, seed: int = 7) -> dict | None:
    """Same model via NUTS, to supply R-hat / ESS for gate G8 and cross-check the grid."""
    try:
        import jax
        import jax.numpy as jnp
        import numpyro
        import numpyro.distributions as dist
        from numpyro.infer import MCMC, NUTS
    except Exception:  # noqa: BLE001
        return None

    y_a, se_a = np.asarray(y, float), np.asarray(se, float)
    if tau_scale is None:
        tau_scale = max(np.median(se_a) * 2.0, 1e-3)

    def model(y_obs, se_obs):
        mu = numpyro.sample("mu", dist.Normal(0.0, 10.0 * max(tau_scale, 0.1)))
        tau = numpyro.sample("tau", dist.HalfNormal(tau_scale))
        # Non-centered parameterisation. The centered form has a funnel geometry that
        # produces divergences whenever tau can approach zero, which it can here.
        z = numpyro.sample("z", dist.Normal(0.0, 1.0).expand([len(y_obs)]))
        theta = mu + tau * z
        numpyro.sample("obs", dist.Normal(theta, se_obs), obs=y_obs)

    kernel = NUTS(model, target_accept_prob=0.99, max_tree_depth=12)
    mcmc = MCMC(kernel, num_warmup=2000, num_samples=4000, num_chains=4,
                chain_method="sequential", progress_bar=False)
    mcmc.run(jax.random.PRNGKey(seed), jnp.asarray(y_a), jnp.asarray(se_a),
             extra_fields=("diverging",))
    samples = mcmc.get_samples(group_by_chain=True)

    def rhat_ess(x):
        # x: (chains, draws)
        m, n = x.shape
        chain_means = x.mean(axis=1)
        chain_vars = x.var(axis=1, ddof=1)
        w = chain_vars.mean()
        b = n * chain_means.var(ddof=1) if m > 1 else 0.0
        var_hat = ((n - 1) / n) * w + b / n
        rhat = math.sqrt(var_hat / w) if w > 0 else float("nan")
        # ESS from autocorrelation of the pooled chains
        flat = x.reshape(-1)
        flat = flat - flat.mean()
        nfft = 1
        while nfft < 2 * len(flat):
            nfft *= 2
        f = np.fft.rfft(flat, n=nfft)
        acov = np.fft.irfft(f * np.conjugate(f), n=nfft)[:len(flat)].real / len(flat)
        if acov[0] <= 0:
            return rhat, float("nan")
        rho = acov / acov[0]
        s = 0.0
        for t in range(1, len(rho) - 1, 2):
            pair = rho[t] + rho[t + 1]
            if pair < 0:
                break
            s += pair
        ess = len(flat) / (1 + 2 * s) if (1 + 2 * s) > 0 else float("nan")
        return rhat, ess

    mu_chains = np.asarray(samples["mu"])
    tau_chains = np.asarray(samples["tau"])
    r_mu, ess_mu = rhat_ess(mu_chains)
    r_tau, ess_tau = rhat_ess(tau_chains)
    extra = mcmc.get_extra_fields() if hasattr(mcmc, "get_extra_fields") else {}
    divergences = int(np.sum(np.asarray(extra.get("diverging", [])))) if extra else 0
    mu_flat = mu_chains.reshape(-1)
    return {
        "method": "nuts_numpyro", "k": len(y_a),
        "mu_median": float(np.median(mu_flat)),
        "mu_ci95": [float(np.percentile(mu_flat, 2.5)), float(np.percentile(mu_flat, 97.5))],
        "tau_median": float(np.median(tau_chains)),
        "rhat_mu": float(r_mu), "ess_mu": float(ess_mu),
        "rhat_tau": float(r_tau), "ess_tau": float(ess_tau),
        "divergences": divergences,
        "n_chains": mu_chains.shape[0], "n_draws_per_chain": mu_chains.shape[1],
    }


# ======================================================================================
# Bias diagnostics
# ======================================================================================
def eggers_test(y, se) -> dict:
    y, se = np.asarray(y, float), np.asarray(se, float)
    if len(y) < 3:
        return {"n": len(y), "slope": None, "p": None}
    prec = 1.0 / se
    z = y / se
    slope, intercept, r, p, stderr = stats.linregress(prec, z)
    # In the standard parameterisation the *intercept* of z on precision tests asymmetry.
    return {"n": len(y), "intercept": float(intercept), "p_intercept": float(p),
            "slope": float(slope), "note": "regression of y/se on 1/se; intercept != 0 indicates asymmetry"}


def pet_peese(y, se) -> dict:
    """PET-PEESE: bias-corrected estimate of the effect at zero standard error."""
    y, se = np.asarray(y, float), np.asarray(se, float)
    k = len(y)
    if k < 4:
        return {"k": k, "pet": None, "peese": None, "recommended": None}
    w = 1.0 / se ** 2
    # PET: WLS of y on se
    X = np.column_stack([np.ones(k), se])
    W = np.diag(w)
    beta_pet = np.linalg.solve(X.T @ W @ X, X.T @ W @ y)
    # PEESE: WLS of y on se^2
    X2 = np.column_stack([np.ones(k), se ** 2])
    beta_peese = np.linalg.solve(X2.T @ W @ X2, X2.T @ W @ y)
    resid = y - X @ beta_pet
    dof = max(k - 2, 1)
    s2 = float((w * resid ** 2).sum() / dof)
    cov = s2 * np.linalg.inv(X.T @ W @ X)
    t_pet = beta_pet[0] / math.sqrt(max(cov[0, 0], 1e-18))
    p_pet = 2 * (1 - stats.t.cdf(abs(t_pet), dof))
    # conditional estimator: use PEESE only if PET finds evidence of a non-zero effect
    recommended = float(beta_peese[0]) if p_pet < 0.10 else float(beta_pet[0])
    return {"k": k, "pet": float(beta_pet[0]), "pet_p": float(p_pet),
            "peese": float(beta_peese[0]), "recommended": recommended}


def trim_and_fill(y, se, max_iter: int = 50) -> dict:
    """Duval-Tweedie trim-and-fill using the L0 estimator of the number of missing studies.

    Deviations of exactly zero carry no sign and are excluded from the rank statistic; leaving
    them in makes the count depend on arbitrary tie-breaking in the sort, which showed up as
    phantom fills on perfectly symmetric input.
    """
    y, se = np.asarray(y, float), np.asarray(se, float)
    k = len(y)
    if k < 4:
        return {"k": k, "n_filled": 0, "adjusted_mu": None, "estimator": "L0"}
    v = se ** 2
    w = 1.0 / v
    mu = (w * y).sum() / w.sum()
    unadjusted = float(mu)
    r0 = 0
    for _ in range(max_iter):
        d = y - mu
        nz = np.abs(d) > 1e-12
        dn = d[nz]
        kk = len(dn)
        if kk < 4:
            return {"k": k, "n_filled": 0, "adjusted_mu": float(mu),
                    "unadjusted_mu": unadjusted, "estimator": "L0"}
        order = np.argsort(np.abs(dn))
        ranks = np.empty(kk)
        ranks[order] = np.arange(1, kk + 1)
        # Suppression can be on either side, so the statistic is evaluated in both
        # orientations: an excess of positive deviations implies missing negative studies and
        # vice versa. Testing only one orientation silently misses half of all real cases.
        t_plus = ranks[dn > 0].sum()
        t_minus = ranks[dn < 0].sum()
        l0_missing_negative = (4.0 * t_plus - kk * (kk + 1)) / (2.0 * kk - 1)
        l0_missing_positive = (4.0 * t_minus - kk * (kk + 1)) / (2.0 * kk - 1)
        if l0_missing_negative >= l0_missing_positive:
            l0, excess_side = l0_missing_negative, 1.0
        else:
            l0, excess_side = l0_missing_positive, -1.0
        r0 = max(0, int(round(l0)))
        if r0 == 0:
            return {"k": k, "n_filled": 0, "adjusted_mu": float(mu),
                    "unadjusted_mu": unadjusted, "estimator": "L0"}
        # Mirror the r0 most extreme studies from the over-represented side.
        cand = np.where(np.sign(d) == excess_side)[0]
        cand = cand[np.argsort(-np.abs(d[cand]))][:r0]
        filled_y = 2 * mu - y[cand]
        y2 = np.concatenate([y, filled_y])
        v2 = np.concatenate([v, se[cand] ** 2])
        w2 = 1.0 / v2
        mu_new = (w2 * y2).sum() / w2.sum()
        if abs(mu_new - mu) < 1e-9:
            mu = mu_new
            break
        mu = mu_new
    return {"k": k, "n_filled": int(r0), "adjusted_mu": float(mu),
            "unadjusted_mu": unadjusted, "estimator": "L0"}


def e_value(rr: float) -> float:
    """VanderWeele-Ding E-value: the minimum confounder association that could explain away RR."""
    rr = max(rr, 1.0 / rr) if rr > 0 else float("nan")
    return rr + math.sqrt(rr * (rr - 1.0))


# ======================================================================================
# De-duplication
# ======================================================================================
def dedupe_by_cohort(rows: list[dict], value_key: str = "value", se_key: str = "se") -> list[dict]:
    """Collapse effects sharing a cohort_family into one inverse-variance-weighted effect.

    Prevents a single mega-cohort from voting once per publication. Effects with no declared
    family are treated as independent.
    """
    groups = defaultdict(list)
    out = []
    for r in rows:
        fam = r.get("cohort_family")
        if not fam:
            out.append(r)
        else:
            groups[fam].append(r)
    for fam, group in groups.items():
        if len(group) == 1:
            out.append(group[0])
            continue
        y = np.array([g[value_key] for g in group], float)
        se = np.array([g[se_key] for g in group], float)
        w = 1.0 / se ** 2
        merged = dict(group[0])
        merged[value_key] = float((w * y).sum() / w.sum())
        # Correlated within-cohort estimates: the naive combined SE would be too small, so
        # keep the most precise single SE as a conservative floor.
        merged[se_key] = float(se.min())
        merged["study_id"] = f"{fam}_pooled({len(group)})"
        merged["_collapsed_from"] = [g.get("study_id") for g in group]
        out.append(merged)
    return out


def pool_by_tier(rows: list[dict]) -> dict:
    """Pool overall and separately by identification strength, then report the tier gap."""
    def _pool(subset):
        if not subset:
            return None
        y = np.array([r["value"] for r in subset], float)
        se = np.array([r["se"] for r in subset], float)
        b = pool_bayes_grid(y, se)
        f = pool_frequentist(y, se)
        return {"bayes": {k: v for k, v in b.items() if not k.endswith("_draws")},
                "frequentist": f,
                "study_ids": [r.get("study_id") for r in subset],
                "tiers": [r.get("tier") for r in subset]}

    causal = [r for r in rows if r.get("tier") in CAUSAL_TIERS]
    assoc = [r for r in rows if r.get("tier") not in CAUSAL_TIERS]
    all_pool = _pool(rows)
    c_pool, a_pool = _pool(causal), _pool(assoc)
    ratio = None
    if c_pool and a_pool:
        mc, ma = c_pool["bayes"]["mu_median"], a_pool["bayes"]["mu_median"]
        if abs(ma) > 1e-9:
            ratio = mc / ma
    return {
        "all": all_pool, "causal_T1_T3": c_pool, "associational_T4_TX": a_pool,
        "causal_to_associational_ratio": ratio,
        "tier_disagreement_exceeds_2x": (ratio is not None and (ratio > 2 or ratio < 0.5)),
    }


if __name__ == "__main__":
    # Self-check against a textbook example: five studies, known pooled behaviour.
    y = np.array([-0.76, -0.55, -0.48, -0.38, -0.25])
    se = np.array([0.10, 0.09, 0.08, 0.13, 0.13])
    print("frequentist:", json.dumps(pool_frequentist(y, se), indent=1))
    b = pool_bayes_grid(y, se)
    print("bayes grid:  mu=%.4f  CI=[%.4f, %.4f]  tau=%.4f  pred CI=[%.4f, %.4f]"
          % (b["mu_median"], *b["mu_ci95"], b["tau_median"], *b["pred_ci95"]))
    n = pool_bayes_nuts(y, se)
    if n:
        print("bayes NUTS:  mu=%.4f  CI=[%.4f, %.4f]  rhat=%.4f  ess=%.0f  div=%d"
              % (n["mu_median"], *n["mu_ci95"], n["rhat_mu"], n["ess_mu"], n["divergences"]))
        print("grid-vs-NUTS mu difference: %.5f" % abs(b["mu_median"] - n["mu_median"]))
    print("egger:", eggers_test(y, se))
    print("pet-peese:", pet_peese(y, se))
    print("trim-and-fill:", trim_and_fill(y, se))
    print("E-value for RR 1.12:", round(e_value(1.12), 3))
