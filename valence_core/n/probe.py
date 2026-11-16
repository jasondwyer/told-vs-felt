"""PROPOSAL-n -- G-READ-n's probe code (n v0.2 §3 G-READ-n as ADDENDUM-n1 §6 amends it; rule 5(f)(ii)'s readability
gate; k's form and bar).

n §3, verbatim: "Per axis (valence of record; `span_reward`) and dose point: an L2 logistic probe on the residual at
the read position (layer 32; and the final layer) discriminating the +pole from the −pole where both exist, else the
+pole from the shadow, against the 24 norm-matched random directions as comparator; grouped leave-one-session-out
CV; AUC against 200 label shuffles; **PASS iff the band median AUC ≥ .90** (k's bar, calibrated on ± contrasts — the
contrast here) and above the comparator's band." ADDENDUM-n1 §6 amends it (the seat's answers of 2026-11-16,
§2.5):
  * THE BAND (§6.2) -- the read position's residual at every decoder layer past the site through the last (the
    identity's ``capture_layers``); "the band median AUC" is the median over them;
  * THE CV (§6.3) -- grouped 10-fold cross-validation by session ("kfold10"), the folds' seed in the lock
    (``cv_seed``), in place of leave-one-session-out;
  * 200 LABEL SHUFFLES for the primary cells, on the statistic's own folds (k's ``kfold_shuffle_null``: the folds
    from ``cv_seed``, the permutations from their own stream); each layer's null 95th percentile and ``above_null``
    are reported;
  * PASS (§6.4) iff the band median AUC >= .90 and above the largest of the comparator's 24 band medians; no
    per-layer condition. NOT-COMPUTED is not PASS.

The classifier is k's, imported unchanged (``valence_core.echo.probe``: ``fit_lr``'s standardize-then-GD L2 logistic
regression with ``discrim.logistic_auc``'s published hyperparameters; ``kfold_auc``; ``kfold_shuffle_null``), so a
G-READ-n AUC means what a k AUC meant. Model-free: it reads capture rows the stage wrote.

THE ARTIFACT IS TIED TO ITS RUN (Code's form, after the drafts' review): ``result`` computes every layer's AUC and
null itself, at the module's N_SHUFFLES and SHUFFLE_SEED and the ``cv_seed`` it is given, so the settings
``artifact`` records are the ones the numbers ran under; ``artifact`` takes ``cv_seed`` with no default and refuses
layers other than the campaign identity's band. The caller passes the one ``cv_seed`` (the lock's) to both.

Code's readings (declared at the BUILD for the seat; LOCK-n v0.1 pins them):
  * CONTRASTS -- per axis and dose point d > 0: +pole at d against -pole at -d where both are read (the valence
    axis at +1 / -1), else +pole at d against the session's shadow (d = 0); rows grouped by session.
  * COMPARATOR -- each random direction's band median on the same contrast at the same dose point (its own 40
    sessions), not shuffled.
"""
from __future__ import annotations

from typing import Mapping, Sequence

import numpy as np

from ..echo.probe import kfold_auc, kfold_shuffle_null
from . import schema

AUC_BAR = 0.90
N_SHUFFLES = 200
K_FOLDS = 10
CV_FORM = "kfold10"
SHUFFLE_SEED = 20260905            # k's default permutation stream (echo/probe.py), declared so the lock can pin it
CV_SEED = 20261116                 # the folds' seed, declared here so the lock can pin it (ADDENDUM-n1 §6.3)


def contrast_rows(caps_pos: Mapping[str, np.ndarray], caps_neg: Mapping[str, np.ndarray]) -> tuple:
    """X [2n, D], y, groups from two {session_id: [D] residual} maps over the same sessions."""
    sids = sorted(set(caps_pos) & set(caps_neg))
    if sorted(caps_pos) != sids or sorted(caps_neg) != sids:
        raise ValueError("the two poles are not read on the same sessions")
    X = np.stack([caps_pos[s] for s in sids] + [caps_neg[s] for s in sids]).astype(np.float64)
    y = np.array([1] * len(sids) + [0] * len(sids))
    groups = np.array(sids + sids)
    return X, y, groups


def layer_auc(X, y, groups, *, shuffles: int = N_SHUFFLES, seed: int = SHUFFLE_SEED, cv_seed: int = CV_SEED) -> dict:
    """One layer's grouped 10-fold AUC, and with ``shuffles`` its label-shuffle null on the same folds."""
    auc = float(kfold_auc(X, y, groups, K_FOLDS, cv_seed))
    out = {"auc": auc}
    if shuffles:
        null = kfold_shuffle_null(X, y, groups, n_shuffles=shuffles, k=K_FOLDS, fold_seed=cv_seed, perm_seed=seed)
        out["null_p95"] = float(np.percentile(null, 95))
        out["above_null"] = auc > out["null_p95"]
    return out


def band_median(per_layer: Sequence[Mapping]) -> float:
    return float(np.median([p["auc"] for p in per_layer]))


def verdict(axis_layers: Sequence[Mapping], comparator_bands: Sequence[float]) -> dict:
    """ADDENDUM-n1 §6.4: PASS iff the band median >= .90 and above the comparator's largest band median."""
    bm = band_median(axis_layers)
    comp_max = float(max(comparator_bands)) if comparator_bands else float("nan")
    passed = bool(comparator_bands) and bm >= AUC_BAR and bm > comp_max
    return {"band_median_auc": bm, "comparator_max": comp_max, "status": "PASS" if passed else "FAIL"}


def result(axis: str, dose_label: str, merged: Sequence[str], contrast: str, layer_data: Sequence[tuple] | None,
           layers: Sequence[int], comparator_bands: Sequence[float] | None, *, cv_seed: int) -> dict:
    """One ``n-gread-v1`` result, its numbers computed here: each layer's grouped 10-fold AUC and label-shuffle null
    by ``layer_auc`` at the module's N_SHUFFLES and SHUFFLE_SEED, on the folds of ``cv_seed``. ``layer_data`` is one
    (X, y, groups) per layer of ``layers``, in order (``contrast_rows``), or None: NOT-COMPUTED, a contrast's reads
    incomplete. A layer whose X, y and groups are the very objects of an earlier layer's is computed once -- the same
    numbers, by the same call (the self-test repeats one contrast over the band)."""
    if layer_data is None:
        return {"axis": axis, "dose_label": dose_label, "merged": list(merged), "contrast": contrast,
                "status": "NOT-COMPUTED", "band_median_auc": None, "per_layer": [],
                "comparator": {"band_medians": None, "max": None}, "bar": AUC_BAR}
    if len(layer_data) != len(layers):
        raise ValueError(f"{len(layer_data)} layers of data for the {len(layers)} layers probed")
    done: dict = {}
    axis_layers = []
    for X, y, groups in layer_data:
        key = (id(X), id(y), id(groups))                 # every object is held by layer_data: no id is reused here
        if key not in done:
            done[key] = layer_auc(X, y, groups, shuffles=N_SHUFFLES, seed=SHUFFLE_SEED, cv_seed=int(cv_seed))
        axis_layers.append(done[key])
    v = verdict(axis_layers, comparator_bands or [])
    per = [{"layer": int(l), "auc": float(p["auc"]), "null_p95": float(p["null_p95"]),
            "above_null": bool(p["above_null"])} for l, p in zip(layers, axis_layers)]
    comp = ({"band_medians": [float(x) for x in comparator_bands], "max": float(max(comparator_bands))}
            if comparator_bands else {"band_medians": None, "max": None})
    return {"axis": axis, "dose_label": dose_label, "merged": list(merged), "contrast": contrast,
            "status": v["status"], "band_median_auc": v["band_median_auc"], "per_layer": per, "comparator": comp,
            "bar": AUC_BAR}


def artifact(campaign_report: Mapping, package_sha256: str, layers: Sequence[int], results: Sequence[Mapping],
             *, cv_seed: int) -> dict:
    """G-READ-n's artifact (``n-gread-v1``) over the campaign its report names, checked before it is returned. Its
    ``layers`` are the campaign identity's band, in order (ADDENDUM-n1 §6.2: ``capture_layers``), or a ValueError: a
    probe of part of the band, or of other layers, has no band median of record. ``cv_seed``, the folds' seed the
    results were computed at (``result``), is recorded and has no default: none stands in for the lock's."""
    if list(layers) != list(campaign_report["stage_identity"]["capture_layers"]):
        raise ValueError("the probe's layers are not the campaign identity's capture_layers (ADDENDUM-n1 §6.2's "
                         "band)")
    art = {"schema": schema.GREAD_SCHEMA,
           "campaign": {"read_plan_sha256": campaign_report["read_plan_sha256"],
                        "stage_identity_sha256": campaign_report["stage_identity_sha256"],
                        "cells": {n: {"json_sha256": x["json_sha256"], "capture_sha256": dict(x["capture_sha256"])}
                                  for n, x in sorted(campaign_report["cells"].items())}},
           "probe": {"package_sha256": package_sha256, "lr": dict(schema.GREAD_LR), "shuffles": N_SHUFFLES,
                     "shuffle_seed": SHUFFLE_SEED, "cv": CV_FORM, "cv_seed": int(cv_seed),
                     "layers": [int(x) for x in layers], "bar": AUC_BAR},
           "results": [dict(r) for r in results]}
    schema.check_gread(art)
    return art


def _selftest(chk, tmp) -> None:
    import sys
    rng = np.random.default_rng(11)
    n, d = 16, 6
    sids = [f"s{i}" for i in range(n)]
    base = {s: rng.standard_normal(d) * 0.5 for s in sids}
    pos = {s: base[s] + np.array([6.0] + [0.0] * (d - 1)) for s in sids}
    X, y, g = contrast_rows(pos, base)
    lay = layer_auc(X, y, g, shuffles=20, seed=5)
    chk("probe: a separable contrast reads AUC 1 above its shuffle null (grouped 10-fold)",
        lay["auc"] == 1.0 and lay["above_null"], lay)
    noise = {s: base[s] + rng.standard_normal(d) * 1e-3 for s in sids}
    X0, y0, g0 = contrast_rows(noise, base)
    lay0 = layer_auc(X0, y0, g0, shuffles=20, seed=5)
    chk("probe: a contrast of nothing does not clear the bar", lay0["auc"] < AUC_BAR, lay0["auc"])
    null0 = kfold_shuffle_null(X0, y0, g0, n_shuffles=20, k=K_FOLDS, fold_seed=CV_SEED, perm_seed=5)
    chk("probe: the null is the shuffles' 95th percentile on the statistic's own folds (k's kfold form)",
        lay0["null_p95"] == float(np.percentile(null0, 95)) and lay0["above_null"] == (lay0["auc"] > lay0["null_p95"]),
        (lay0["null_p95"], float(np.percentile(null0, 95))))
    chk("probe: the AUC is k's grouped 10-fold, at the folds' seed", lay0["auc"] == float(kfold_auc(X0, y0, g0, 10,
                                                                                                      CV_SEED)), "")
    v = verdict([lay, lay], [0.6, 0.7])
    chk("probe: PASS needs the band median >= .90 and above the comparator's largest (ADDENDUM-n1 §6.4)",
        v["status"] == "PASS" and v["band_median_auc"] == 1.0, v)
    chk("probe: a comparator at the axis's level fails it", verdict([lay, lay], [1.0])["status"] == "FAIL", "")
    chk("probe: no comparator fails it", verdict([lay, lay], [])["status"] == "FAIL", "")
    chk("probe: a layer under its null does not fail it (no per-layer condition)",
        verdict([lay, lay, dict(lay0, above_null=False)], [0.5])["status"] == "PASS", "")
    at_bar = verdict([{"auc": 0.9, "null_p95": 0.6, "above_null": True}] * 3, [0.85])
    chk("probe: a band median exactly at .90, above the comparator's largest, PASSes (at least the bar: §6.4)",
        at_bar["status"] == "PASS" and at_bar["band_median_auc"] == AUC_BAR, at_bar)
    try:
        contrast_rows(pos, {s: base[s] for s in sids[:-1]})
        chk("probe: poles on different sessions are refused", False, "accepted")
    except ValueError:
        chk("probe: poles on different sessions are refused", True, "")
    # the artifact (n-gread-v1), checked by schema.check_gread: computed from layer data over the example campaign's
    # band, 32..63, at the real 200 shuffles (one contrast repeated over the band, computed once per result)
    rep = schema.example_report(schema.example_identity())
    band = list(rep["stage_identity"]["capture_layers"])
    comp = [0.5 + 0.005 * i for i in range(schema.N_RANDOM)]
    sep, nul = [(X, y, g)] * len(band), [(X0, y0, g0)] * len(band)
    me = sys.modules[__name__]
    seen: list = []
    real_layer_auc = me.layer_auc

    def spy(X_, y_, g_, **kw):                              # records the settings result runs layer_auc at
        seen.append(dict(kw))
        return real_layer_auc(X_, y_, g_, **kw)
    me.layer_auc = spy
    try:
        res = [result("valence", "+1", [], "pole", sep, band, comp, cv_seed=CV_SEED),
               result("valence", "+1/2", [], "shadow", nul, band, comp, cv_seed=CV_SEED),
               result("span_reward", "f0.10", [], "shadow", None, band, None, cv_seed=CV_SEED)]
    finally:
        me.layer_auc = real_layer_auc
    chk("probe: result computes each layer by layer_auc at N_SHUFFLES (200), SHUFFLE_SEED and the cv_seed given, a "
        "contrast repeated over the band once", N_SHUFFLES == 200 and seen == [
            {"shuffles": 200, "seed": SHUFFLE_SEED, "cv_seed": CV_SEED}] * 2, seen)
    art = artifact(rep, "2" * 64, band, res, cv_seed=CV_SEED)
    chk("probe: the artifact passes check_gread, statuses PASS / FAIL / NOT-COMPUTED",
        [r["status"] for r in art["results"]] == ["PASS", "FAIL", "NOT-COMPUTED"], [r["status"] for r in res])
    chk("probe: the artifact names the campaign by its report's sha256s, pins k's fit_lr, and carries kfold10, its "
        "seed and the band", art["campaign"]["stage_identity_sha256"] == rep["stage_identity_sha256"]
        and art["probe"]["lr"] == schema.GREAD_LR and art["probe"]["shuffles"] == 200
        and art["probe"]["shuffle_seed"] == SHUFFLE_SEED and art["probe"]["cv"] == "kfold10"
        and art["probe"]["cv_seed"] == CV_SEED and art["probe"]["layers"] == list(range(32, 64)), art["probe"])
    try:
        artifact(rep, "2" * 64, [32, 63], [res[2]], cv_seed=CV_SEED)       # check_gread alone would accept it
        chk("probe: an artifact whose layers are not the campaign identity's band is refused", False, "accepted")
    except ValueError as e:
        chk("probe: an artifact whose layers are not the campaign identity's band is refused",
            "capture_layers" in str(e), str(e)[:120])
    try:
        result("valence", "+1", [], "pole", sep[:2], band, comp, cv_seed=CV_SEED)
        chk("probe: layer data that is not one per layer is refused", False, "accepted")
    except ValueError:
        chk("probe: layer data that is not one per layer is refused", True, "")
    try:
        artifact(rep, "2" * 64, band, [dict(res[1], status="PASS")], cv_seed=CV_SEED)
        chk("probe: a status the check does not reproduce is refused", False, "accepted")
    except schema.SchemaError:
        chk("probe: a status the check does not reproduce is refused", True, "")
