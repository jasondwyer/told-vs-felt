"""e2d readability -- the resampled, clean-round ladder over `discrim`.

PROPOSAL-j §0.4 and §2 Q2. e2a's readability figure was refit-dependent:
g2r's k = 2 AUC .759 failed a transfer spotcheck (.448, `g2r_stands: false`),
g2r2 recovered .759 by same-distribution refit, and e2a proceeded on it.
**e2d does not inherit a single-refit gate.** Three changes, all of them the
proposal's:

  1. RESAMPLED. B draws of record construction and the task-disjoint
     fit/val split, seeded through `discrim.seed_for`, reported as a median
     and a 10th percentile. The criterion is chosen to fail on the g2r
     pattern: resamples spanning .448 and .759 have a median near .60.
  2. CLEAN ROUNDS ONLY. Rule 28(b) -- the tolerant counter attributes first,
     so rounds the audit excludes never reach the probe and the AUC measures
     content rather than breakage.
  3. TRANSFER, not just refit. A classifier fit on D2's records and STORED
     under `discrim`'s own hyperparameters, scored later on the campaign's
     records without refit. That figure enters the scope sentence beside the
     refit one; a transfer failure beside a refit pass is the g2r pattern
     recurring and is reported as exactly that.

FROZEN-SUCCESSOR RULE. `discrim.py` is not edited. Everything below IMPORTS
`AUC_BAR` and every fit hyperparameter from it and re-declares none of them:
changing a default there "would move every historical AUC", so this module
reads the defaults off `logistic_auc`'s own signature rather than restating
their values, which means a change in `discrim` cannot silently fail to
reach e2d.
"""

from __future__ import annotations

import inspect
from typing import Sequence

import numpy as np

from ..discrim import (AUC_BAR, auc_from_scores, build_records, logistic_auc,
                       seed_for)

#: Read off `discrim.logistic_auc`'s signature rather than restated. If a
#: hyperparameter there ever moves, this moves with it and the suite check
#: `check_e2d_discrim_constants` proves the two are the same object.
FIT_HYPERPARAMS = {
    name: p.default
    for name, p in inspect.signature(logistic_auc).parameters.items()
    if p.default is not inspect.Parameter.empty
}

B_RESAMPLES = 20             # PROPOSAL-j §2 Q2 [LOCK-j: may be raised]
MEDIAN_BAR = 0.70            # == AUC_BAR; asserted below, never restated
PCTL = 10
PCTL_BAR = 0.60


def _assert_bar_identity() -> None:
    """The median bar IS `discrim.AUC_BAR`. Stating it twice is how two bars
    drift apart, so the equality is asserted at import."""
    if MEDIAN_BAR != AUC_BAR:
        raise SystemExit(
            f"e2d readability: median bar {MEDIAN_BAR} has drifted from "
            f"discrim.AUC_BAR {AUC_BAR} -- one of them is wrong (rule 26)")


_assert_bar_identity()


def clean_rounds(sessions: Sequence[dict], arm: str,
                 include_free: bool = True) -> dict[str, list[dict]]:
    """Audit-clean rounds of one arm, split by whether a state was live.

    "pos" = rounds generated with the state live (the +tag's rounds in arms
    M and R). "neg" = rounds generated with nothing live -- the CPP's sham
    side. This is the one-pole design: there is no -axis to contrast against,
    so the contrast is drug-vs-saline, which is the classic CPP form.

    A round is CLEAN when the audit did not claim it (rule 28b). Lexical hits
    are excluded too: a response naming a roster tag is not a clean sample of
    what the state does to text.
    """
    out: dict[str, list[dict]] = {"pos": [], "neg": []}
    for s in sessions:
        if s["arm"] != arm:
            continue
        rows = list(s["rounds"]) + (list(s["choices"]) if include_free else [])
        for r in rows:
            if r["degen"] or r.get("lexical"):
                continue
            if not r["text"].strip():
                continue
            out["pos" if r["steered"] else "neg"].append(
                {"text": r["text"], "task_id": r["task"],
                 "arm": arm, "session": s["session"], "phase": r["phase"]})
    return out


def _split(task_ids: Sequence[str], rng: np.random.Generator
           ) -> tuple[set[str], set[str]]:
    """Task-DISJOINT halves. A qualifying AUC has to be generalization across
    items, not memorization of a paraphrase, and that property is a property
    of the split -- so the split is over task ids, never over rows."""
    ids = sorted(set(task_ids))
    perm = rng.permutation(len(ids))
    half = len(ids) // 2
    return ({ids[i] for i in perm[:half]}, {ids[i] for i in perm[half:]})


def _design(adapter, rounds: dict[str, Sequence[dict]], k: int,
            fit_ids: set[str], val_ids: set[str], rng
            ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    X, y, half = [], [], []
    for pole, label in (("pos", 1), ("neg", 0)):
        for half_name, ids_set in (("fit", fit_ids), ("val", val_ids)):
            sub = [r for r in rounds[pole] if r["task_id"] in ids_set]
            if not sub:
                continue
            for rec in build_records(sub, k, rng):
                X.append(adapter.embed(rec))
                y.append(label)
                half.append(half_name)
    return np.array(X), np.array(y), np.array(half)


def resampled_auc(adapter, rounds: dict[str, Sequence[dict]], k: int,
                  b: int = B_RESAMPLES, key: str = "e2d") -> dict:
    """B resamples of (record construction, task-disjoint split) at length k.

    Returns every draw, not just the summary -- the g2r lesson is that a
    single number hid a distribution spanning .448 to .759, and a summary
    that cannot be reopened repeats it.
    """
    task_ids = [r["task_id"] for pole in ("pos", "neg") for r in rounds[pole]]
    aucs, drawn = [], []
    for i in range(b):
        rng = np.random.default_rng(seed_for(key, "ladder", k, i))
        fit_ids, val_ids = _split(task_ids, rng)
        X, y, half = _design(adapter, rounds, k, fit_ids, val_ids, rng)
        if not len(X) or len(set(y[half == "fit"])) < 2 \
                or len(set(y[half == "val"])) < 2:
            drawn.append(None)
            continue
        a = logistic_auc(X[half == "fit"], y[half == "fit"],
                         X[half == "val"], y[half == "val"])
        aucs.append(float(a))
        drawn.append(float(a))
    if not aucs:
        return {"k": k, "b": b, "n_evaluable": 0, "median": None,
                "p10": None, "aucs": drawn,
                "why": "no resample had both classes on both halves"}
    return {"k": k, "b": b, "n_evaluable": len(aucs),
            "median": float(np.median(aucs)),
            "p10": float(np.percentile(aucs, PCTL)),
            "min": float(np.min(aucs)), "max": float(np.max(aucs)),
            "aucs": drawn,
            "n_pos": len(rounds["pos"]), "n_neg": len(rounds["neg"])}


def gate(summary: dict) -> dict:
    """PROPOSAL-j §2 Q2: median >= .70 AND 10th percentile >= .60 at k = 2.

    Computed and returned; NOT written anywhere by this function. Trap 6 --
    a verdict is computed before its artifact is written, never folded into
    the write.
    """
    if summary.get("median") is None:
        return {"passes": False, "why": summary.get("why", "not evaluable")}
    ok_med = summary["median"] >= MEDIAN_BAR
    ok_p10 = summary["p10"] >= PCTL_BAR
    return {"passes": bool(ok_med and ok_p10),
            "median": summary["median"], "median_bar": MEDIAN_BAR,
            "p10": summary["p10"], "p10_bar": PCTL_BAR,
            "median_ok": bool(ok_med), "p10_ok": bool(ok_p10)}


# --- the stored classifier (the transfer figure's other half) -------------
def fit_and_store(adapter, rounds: dict[str, Sequence[dict]], k: int,
                  key: str = "e2d") -> dict:
    """Fit ONE classifier over all clean rounds and store its weights.

    `discrim` has no stored classifier -- it refits on every call, which is
    exactly what made e2a's figure refit-dependent. The transfer figure
    needs a fixed one, so this reproduces `logistic_auc`'s fit EXACTLY (same
    standardization, same seeded init, same iterations, lr and L2, all taken
    from FIT_HYPERPARAMS rather than retyped) and returns w, b, mu, sd.

    Storing mu/sd matters as much as w: standardization is fit on the fit
    half inside `logistic_auc`, so a stored classifier that re-standardized
    on the target set would not be the same function.
    """
    hp = FIT_HYPERPARAMS
    rng_rec = np.random.default_rng(seed_for(key, "store", k))
    X, y = [], []
    for pole, label in (("pos", 1), ("neg", 0)):
        sub = list(rounds[pole])
        if not sub:
            continue
        for rec in build_records(sub, k, rng_rec):
            X.append(adapter.embed(rec))
            y.append(label)
    X, y = np.array(X), np.array(y, dtype=np.float64)
    if len(set(y.tolist())) < 2:
        raise SystemExit("e2d fit_and_store: only one class present")
    mu, sd = X.mean(0), X.std(0) + 1e-6
    Xs = (X - mu) / sd
    rng = np.random.default_rng(hp["seed"])
    w = rng.normal(0, 0.01, Xs.shape[1])
    b = 0.0
    for _ in range(hp["iters"]):
        p = 1 / (1 + np.exp(-(Xs @ w + b)))
        w -= hp["lr"] * (Xs.T @ (p - y) / len(y) + hp["l2"] * w)
        b -= hp["lr"] * float(np.mean(p - y))
    return {"w": w, "b": float(b), "mu": mu, "sd": sd, "k": k,
            "n_fit": int(len(y)), "hyperparams": dict(hp)}


def score_stored(adapter, clf: dict, rounds: dict[str, Sequence[dict]],
                 key: str = "e2d") -> dict:
    """Transfer: score records with a stored classifier, NO refit."""
    rng = np.random.default_rng(seed_for(key, "transfer", clf["k"]))
    scores, labels = [], []
    for pole, label in (("pos", 1), ("neg", 0)):
        sub = list(rounds[pole])
        if not sub:
            continue
        for rec in build_records(sub, clf["k"], rng):
            x = (adapter.embed(rec) - clf["mu"]) / clf["sd"]
            scores.append(float(x @ clf["w"] + clf["b"]))
            labels.append(label)
    if len(set(labels)) < 2:
        return {"auc": None, "n": len(labels),
                "why": "only one class in the target set"}
    return {"auc": float(auc_from_scores(scores, labels)), "n": len(labels),
            "n_pos": int(sum(labels)), "refit": False}


__all__ = ["FIT_HYPERPARAMS", "B_RESAMPLES", "MEDIAN_BAR", "PCTL",
           "PCTL_BAR", "clean_rounds", "resampled_auc", "gate",
           "fit_and_store", "score_stored"]
