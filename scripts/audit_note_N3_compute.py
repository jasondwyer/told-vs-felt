#!/usr/bin/env python3
"""AUDIT-note-release v1.2, item N3 parts (ii), (iii), (iv) ("N3c"), on the
local Stage C residual arrays data/echo/stageC_resid_s*.npz.

Read-only on the record. Reads the committed Stage C JSON at the pinned
commit (git show bbc9ffe:...), the local (gitignored) residual arrays, and
imports the record's own pure probe functions (valence_core.echo.probe,
valence_core.discrim.auc_from_scores, valence_core.adapters.base.sha16_arr;
numpy only, no model, no side effects). Writes only --out and --json-out.

    STEP 0  reproduce the stored Stage C linear statistics through the
            record's own procedure (auc_kfold, auc_loso; shuffle95 /
            shuffle_mean / shuffle_max from the first 200 draws of the
            record's permutation stream).
    (ii)    permutation null extended to 1,000 draws at label_a, label_b
            and the read (decision) position, same grouped 10-fold, same
            folds, same permutation stream.
    (iii)   nonlinear reads at the read position (one-hidden-layer MLP;
            RBF kernel ridge classifier) with their own permutation nulls;
            both at label_a as the positive control.
    (iv)    linear layer sweep at the read position, L44-L61, and the
            le48 construction fact checked on the arrays.

No model inference. Seeds fixed; deterministic apart from the stamp line; the
HEAD, Command and Workers lines change only if HEAD or the arguments change;
wall-clock timing goes to stderr and to the JSON's timing_nondeterministic.

--render-only rebuilds --out from the existing JSON at --json-out with render(),
the same function the compute path calls on the JSON text it writes: no arrays,
no fits, and the JSON is read, never written. A raw written this way carries a
"Rendered by --render-only" header line naming the render's stamp, HEAD,
script hash, command and input-JSON hash.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True   # read-only on the record: no __pycache__ writes

import argparse                  # noqa: E402
import hashlib                   # noqa: E402
import json                      # noqa: E402
import os                        # noqa: E402
import platform                  # noqa: E402
import re                        # noqa: E402
import subprocess                # noqa: E402
import time                      # noqa: E402
from concurrent.futures import ProcessPoolExecutor   # noqa: E402

import numpy as np               # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from valence_core.adapters.base import sha16_arr     # noqa: E402
from valence_core.discrim import auc_from_scores     # noqa: E402
from valence_core.echo import probe as PR            # noqa: E402

TITLE = "AUDIT-note-release v1.2 -- N3 parts (ii), (iii), (iv) on the local Stage C residual arrays (N3c)"
PIN = "bbc9ffe"
PIN_FULL = "bbc9ffe72fb8a942431c9bf2622a36e581fdf93c"
BLOCK = "AUDIT-note-release-v1_2.md"
BLOCK_SHA = "8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841"
SCRIPT_REL = "scripts/audit_note_N3_compute.py"
OUT_MD = os.path.join(REPO, "results/raw/2026-10-08_note-N3-echo-compute.md")
OUT_JSON = os.path.join(REPO, "results/raw/2026-10-08_note-N3-echo-compute.json")
READS_REL = "data/echo/stageC_reads.json"
ANALYSIS_REL = "data/echo/stageC_analysis.json"
STORED_RAW_REL = "results/raw/2026-09-06_recon_echo_stageC_analysis.txt"

LAYER = 48                         # recon_echo.LAYER (steering layer of record)
K = 10                             # grouped k-fold of record
STORED_LAYERS = [40, 44] + list(range(48, 64))
EXT_LAYERS = list(range(51, 62))   # the layers the note cites (L51-L61)
SWEEP_LAYERS = list(range(44, 62))  # (iv)
KEEP_LAYERS = list(range(40, 64))  # rows held in memory
POS = {"read": 0, "label_a": 1, "label_b": 2}
# analyze_c's family insertion order; fold seed = 90260905 + 1000 * index
C1_ORDER = [f"c1_{pn}_{suf}" for pn in ("read", "label_a", "label_b")
            for suf in ("M1M2", "M3M4_random", "TEXTONLY_shadow")]
M1M2 = ["c1_read_M1M2", "c1_label_a_M1M2", "c1_label_b_M1M2"]
SEED_BASE = 90260905
N_EXT, N_STORED, CHUNK = 1000, 200, 200
WORKERS = 6                        # <= 8 worker processes

# (iii) nonlinear classifiers -- fixed before any read-position fit
MLP = dict(H=64, lr=0.01, mom=0.9, l2=1e-3, max_epochs=1000, patience=100)
MLP_VAL_FRAC = 0.2
MLP_SPLIT_SEED = 20261008          # + outer fold index
MLP_INIT_SEED = 20261108           # + outer fold index
N_MLP_NULL = 200
RBF_LAMS = (1e-4, 1e-3, 1e-2, 1e-1, 1.0)
RBF_INNER_K = 5
RBF_INNER_SEED = 20261009          # + outer fold index
N_RBF_NULL = 1000
POSCTRL_BAR = 0.95                 # declared: positive control passes iff AUC >= .95 at every L51-L61
DETERMINISM_LAYER = 56
SENS_CASES = [("c1_read_M1M2", 51), ("c1_label_b_M1M2", 57)]

# (iii-s) sensitivity of (iii), added by the values-check fix (post-hoc, descriptive; no (iii)
# hyperparameter above changes). Declared here before the run of record of this version.
SEED_OFFSETS = (1, 2, 3, 4)        # spec MLP re-run with split/init seeds + 1000 k
MLP_ADAM = dict(H=64, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8, l2=1e-3, max_epochs=1000, patience=100)
ADAM_LAYERS = (51, 56, 61)         # the checker's three layers
N_ADAM_NULL = 50
RBF_LAMS_X = (1e-7, 1e-6, 1e-5) + RBF_LAMS   # grid extended below the edge the (iii) fits chose
SP_SEED = 20261010                 # + layer: per-session label-flip null (keeps one + / one - per session)
N_SP_MLP = 100
N_SP_RBF = 1000
SIBLING_RAW = "results/raw/2026-10-08_note-N3-echo-robustness.md"
CHECKER_ADAM = {51: 0.7313, 56: 0.5844, 61: 0.5667}   # values-checker's own Adam MLP (its values, quoted)
CHECKER_RBFX = {49: 0.6105, 51: 0.7984, 53: 0.7750, 56: 0.7579, 59: 0.7775, 61: 0.7453}   # checker's grid-to-1e-7 RBF (quoted)
CHECKER2_ISO_MLP = {51: 0.9368, 56: 0.8202}   # round-2 values-checker's isotropic-init MLP (its values, quoted)
# Round 2 (render-only fix): sha256s of the files the pre-edit equivalence check compared (Code's runs in scratch).
R1 = {"script": "42e38409c24fe73698f2aee78397b57aebdcc89dbba435f97723266a730bd0c9",
      "raw": "6f8528aafc76b31ec4063bf8eca9949b9650e77292dd1004eba6758877de7132",
      "json": "d431a2a5f9c7bd34666e487d8ca8dd2645db15e75fca23b91eae2ea7a345a6f3",
      "smoke_raw": "36862442eaeb768f075ac9ad1551d7fc17560490a0291f7a0f07d26400bf822a",
      "smoke_json": "a053e70b0dc0168cea149fa840f7ce4c679b5641b387c92546f32a2838fa2a3e"}
STEP1_SCRIPT = "b4f551adee4f4e68b3e28bba3a68cb52d8889936f5a501290434b42b42576340"   # refactor, round-1 text
# Round 4 (render-only fix of pass 3's findings): sha256s of round 2's outputs, which pass 3 checked, and of
# pass 3's full compute re-run in scratch (its JSON and compute-path raw), compared by Code in scratch.
R2 = {"script": "145a8c1497a22bff671a894624f24b4f70232943017f4e0787074dc74a6cb0f0",
      "raw": "f25cb0e5b63d47334183bf28ecf09382620ee2d5836edd2f45852590cc8e4c59",
      "json": "d431a2a5f9c7bd34666e487d8ca8dd2645db15e75fca23b91eae2ea7a345a6f3"}
V3_RERUN = {"json": "d04fcbdbaedcf5272ed5c8a65a90fa9653a0a6f4ec76d05a2e8de029cd26c0e6",
            "raw": "593d9b4158a47156a213b0f1dac2c9ba115c7111b973840ab23378975098beb8",
            "leaf_diffs": 14,
            "diff_keys": ("code_stamp", "command", "script_sha256", "timing_nondeterministic")}


# --------------------------------------------------------------------------- utils
def sh(*cmd: str) -> str:
    return subprocess.run(list(cmd), capture_output=True, text=True, check=True).stdout


def git_blob(rel: str) -> bytes:
    return subprocess.run(["git", "-C", REPO, "show", f"{PIN}:{rel}"],
                          capture_output=True, check=True).stdout


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: str) -> str:
    with open(p, "rb") as f:
        return sha256_bytes(f.read())


def fold_seed(name: str) -> int:
    return SEED_BASE + 1000 * C1_ORDER.index(name)


def perm_stream(y: np.ndarray, seed: int, n: int) -> np.ndarray:
    """The record's stream (probe.kfold_shuffle_null): rng = default_rng(perm_seed),
    one rng.permutation(y) per draw, in order. Returns [len(y), n]."""
    rng = np.random.default_rng(seed)
    y = np.asarray(y)
    return np.stack([rng.permutation(y) for _ in range(n)], axis=1)


def perm_p(obs: float, null: np.ndarray) -> float:
    return float((1 + np.sum(null >= obs)) / (1 + len(null)))


def stats(null: np.ndarray) -> dict:
    return {"n": int(len(null)), "mean": float(np.mean(null)), "p95": float(np.percentile(null, 95)),
            "max": float(np.max(null))}


def r8(x):
    return [round(float(v), 8) for v in x]


def auc_cols(S: np.ndarray, Y: np.ndarray) -> np.ndarray:
    return np.array([auc_from_scores(S[:, j], Y[:, j]) for j in range(S.shape[1])])


# --------------------------------------------------------------------------- data
def load(log, smoke: bool):
    reads_b, an_b = git_blob(READS_REL), git_blob(ANALYSIS_REL)
    inputs = {}
    for rel, b in ((READS_REL, reads_b), (ANALYSIS_REL, an_b)):
        wt = sha256_file(os.path.join(REPO, rel))
        inputs[rel] = {"sha256_at_pin": sha256_bytes(b), "sha256_working_tree": wt,
                       "working_tree_equals_pin": wt == sha256_bytes(b)}
    meta, an = json.loads(reads_b), json.loads(an_b)
    sess = sorted(meta["per_session"].values(), key=lambda r: r["session"])
    if smoke:
        sess = sess[:40]
    N = len(sess)
    stacks = None
    fp_checked = fp_bad = 0
    le48_cells, le48_bad = 0, []
    pos_bad, dist_a, dist_b = [], set(), set()
    shapes = {}
    layers_present = None
    for i, r in enumerate(sess):
        z = np.load(os.path.join(REPO, r["npz"]))
        keys = [k for k in z.files if k not in ("layers", "positions")]
        arr = {k: z[k] for k in keys}
        lay = [int(x) for x in z["layers"]]
        if layers_present is None:
            layers_present = lay
            shapes = {k: [list(arr[k].shape), str(arr[k].dtype)] for k in keys}
            shapes["layers"] = [list(z["layers"].shape), str(z["layers"].dtype)]
            shapes["positions"] = [list(z["positions"].shape), str(z["positions"].dtype)]
            D = arr["M0|shadow"].shape[-1]
            stacks = {k: np.zeros((N, 3, len(KEEP_LAYERS), D), np.float32)
                      for k in ("M1|state", "M2|state", "M3|state", "M4|state", "M0|shadow")}
        assert lay == layers_present, f"s{r['session']}: layers differ"
        for k in keys:
            fp_checked += 1
            if sha16_arr(arr[k]) != r["npz_sha16_by_key"][k]:
                fp_bad += 1
        shd = arr["M0|shadow"]
        le_idx = [j for j, l in enumerate(lay) if l <= LAYER]
        for k in keys:
            eq = np.all(arr[k][:, le_idx, :] == shd[:, le_idx, :], axis=-1)   # [3, n_le]
            le48_cells += eq.size
            if not eq.all():
                for pi, j in zip(*np.where(~eq)):
                    le48_bad.append((r["session"], k, lay[le_idx[j]], int(pi)))
        p = [int(x) for x in z["positions"]]
        if p != list(r["capture_positions"]) or p[0] != r["read_position"]:
            pos_bad.append(r["session"])
        dist_a.add(p[0] - p[1]); dist_b.add(p[0] - p[2])
        for k in stacks:
            stacks[k][i] = arr[k][:, [lay.index(l) for l in KEEP_LAYERS], :]
    groups = np.array([r["session"] for r in sess])
    a_is_plus = np.array([1 if r["menu_a"] == r["tag_plus"] else 0 for r in sess])
    # direct consequence at the read position: M1 row == M2 row at every layer <= 48
    m1m2_eq = {l: bool(np.array_equal(stacks["M1|state"][:, 0, KEEP_LAYERS.index(l)],
                                      stacks["M2|state"][:, 0, KEEP_LAYERS.index(l)]))
               for l in KEEP_LAYERS if l <= LAYER}
    m1m2_neq_above = {l: int(np.sum(np.any(stacks["M1|state"][:, 0, KEEP_LAYERS.index(l)] !=
                                           stacks["M2|state"][:, 0, KEEP_LAYERS.index(l)], axis=1)))
                      for l in (49, 51, 56, 61)}
    data = {"meta": meta, "an": an, "sess": sess, "N": N, "stacks": stacks, "groups": groups,
            "a_is_plus": a_is_plus}
    info = {"inputs": inputs, "n_sessions": N, "n_npz": N, "layers_present": layers_present,
            "shapes_dtypes_first_file": shapes, "fingerprints_checked": fp_checked,
            "fingerprints_bad": fp_bad, "le48": {"cells_checked": le48_cells, "n_bad": len(le48_bad),
                                                "first_bad": le48_bad[:5],
                                                "stored_le48_control": an["le48_control"]},
            "read_M1_row_equals_M2_row_le48": m1m2_eq,
            "read_sessions_M1_neq_M2_above48": m1m2_neq_above,
            "positions_mismatch_sessions": pos_bad,
            "read_minus_label_a_tokens": sorted(dist_a), "read_minus_label_b_tokens": sorted(dist_b),
            "a_is_plus_balance": {"yes": int(a_is_plus.sum()), "no": int(N - a_is_plus.sum())}}
    return data, info


def family(data, name: str, l: int):
    st, groups, a = data["stacks"], data["groups"], data["a_is_plus"]
    pn = name.split("_M")[0].split("_TEXT")[0][3:]
    li, pi = KEEP_LAYERS.index(l), POS[pn]
    ypos = a if pn in ("read", "label_a") else 1 - a
    if name.endswith("M1M2") or name.endswith("M3M4_random"):
        ma, mb = ("M1", "M2") if name.endswith("M1M2") else ("M3", "M4")
        X = np.concatenate([st[f"{ma}|state"][:, pi, li], st[f"{mb}|state"][:, pi, li]])
        return X, np.r_[ypos, 1 - ypos], np.r_[groups, groups]
    return st["M0|shadow"][:, pi, li], ypos, groups


# --------------------------------------------------------------------------- pool jobs (record functions only)
def _job(args):
    kind = args[0]
    t0 = time.time()
    if kind == "kfold":
        _, name, l, X, y, g, fs, do_loso = args
        auc_k = PR.kfold_auc(X, y, g, K, fs)
        auc_l = PR.loso_auc(X, y, g) if do_loso else None
        return kind, name, l, None, {"auc_kfold": auc_k, "auc_loso": auc_l}, time.time() - t0
    if kind == "perm":
        _, name, l, X, Yc, g, fs, start = args
        out = [PR.kfold_auc(X, Yc[:, j], g, K, fs) for j in range(Yc.shape[1])]
        return kind, name, l, start, out, time.time() - t0
    if kind == "record_null":
        _, name, l, X, y, g, fs, n = args
        out = PR.kfold_shuffle_null(X, y, g, n_shuffles=n, k=K, fold_seed=fs, perm_seed=fs + l)
        return kind, name, l, None, [float(v) for v in out], time.time() - t0
    raise ValueError(kind)


# --------------------------------------------------------------------------- batched-linear sensitivity demo
def kfold_scores_batched(X, Ycols, g, fs):
    """The record's fit_lr written for many label columns at once (gemm instead
    of gemv). Same standardization, init, iterations, rate, L2, bias update."""
    X = np.asarray(X, np.float64)
    n, S = Ycols.shape
    scores = np.zeros((n, S))
    for held_groups in PR.grouped_folds(g, K, fs):
        held = np.array([gi in held_groups for gi in g])
        if not held.any():
            continue
        Xtr = X[~held]
        mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-6
        Xf = (Xtr - mu) / sd
        w0 = np.random.default_rng(PR.LR_SEED).normal(0, 0.01, Xf.shape[1])
        W = np.repeat(w0[:, None], S, axis=1)
        b = np.zeros(S)
        Y = np.asarray(Ycols[~held], np.float64)
        ntr = Y.shape[0]
        for _ in range(PR.LR_ITERS):
            P = 1 / (1 + np.exp(-(Xf @ W + b)))
            W -= PR.LR_RATE * (Xf.T @ (P - Y) / ntr + PR.LR_L2 * W)
            b -= PR.LR_RATE * np.mean(P - Y, axis=0)
        scores[held] = ((X[held] - mu) / sd) @ W + b
    return scores


def gd_stability_ratio(X, g, fs):
    """max over folds of lr * (lambda_max(Xf^T Xf / n) / 4 + l2): full-batch GD on
    the logistic loss is guaranteed stable only below 2."""
    X = np.asarray(X, np.float64)
    worst = 0.0
    for held_groups in PR.grouped_folds(g, K, fs):
        held = np.array([gi in held_groups for gi in g])
        Xtr = X[~held]
        Xf = (Xtr - Xtr.mean(0)) / (Xtr.std(0) + 1e-6)
        lam = float(np.linalg.eigvalsh(Xf @ Xf.T / len(Xf))[-1])
        worst = max(worst, PR.LR_RATE * (lam / 4 + PR.LR_L2))
    return worst


# --------------------------------------------------------------------------- (iii) MLP
def inner_session_split(train_groups, seed, frac=MLP_VAL_FRAC):
    rng = np.random.default_rng(seed)
    ug = np.array(sorted(set(np.asarray(train_groups).tolist())))
    perm = rng.permutation(len(ug))
    return set(ug[perm[:int(round(frac * len(ug)))]].tolist())


def mlp_fold(Xtr, Xva, Xte, Ytr, Yva, seed, H, lr, mom, l2, max_epochs, patience):
    """One-hidden-layer ReLU MLP, sigmoid output, mean BCE + (l2/2)||W||^2 on both
    weight matrices, full-batch gradient descent with heavy-ball momentum, early
    stopping on the inner-validation BCE (best weights restored). The S label
    columns train as independent networks sharing one initialization.
    Inputs are expressed in an orthonormal basis of the inner-train rows' span
    (SVD): with a first-layer init drawn in that basis and a rotation-invariant
    optimizer this is the same computation as the MLP on the full 5120-d input
    with its first-layer init projected onto that span."""
    D = Xtr.shape[1]
    _, s, Vt = np.linalg.svd(Xtr, full_matrices=False)
    V = Vt[s > s[0] * 1e-10].T
    Ptr, Pva, Pte = Xtr @ V, Xva @ V, Xte @ V
    r, S, ntr = V.shape[1], Ytr.shape[1], Ptr.shape[0]
    rng = np.random.default_rng(seed)
    W1_0 = rng.normal(0, np.sqrt(2.0 / D), (r, H))
    w2_0 = rng.normal(0, np.sqrt(1.0 / H), H)
    W1 = np.broadcast_to(W1_0, (S, r, H)).copy(); b1 = np.zeros((S, H))
    w2 = np.broadcast_to(w2_0, (S, H)).copy(); b2 = np.zeros(S)
    vW1, vb1, vw2, vb2 = (np.zeros_like(W1), np.zeros_like(b1), np.zeros_like(w2), np.zeros_like(b2))
    bW1, bb1, bw2, bb2 = W1.copy(), b1.copy(), w2.copy(), b2.copy()
    best = np.full(S, np.inf); best_ep = np.zeros(S, int)
    YtrT, YvaT = Ytr.T.astype(np.float64), Yva.T.astype(np.float64)

    def fwd(P, W1, b1, w2, b2):
        a = W1.shape[0]
        A = (P @ W1.transpose(1, 0, 2).reshape(r, a * H)).reshape(P.shape[0], a, H) + b1[None]
        Hh = np.maximum(A, 0)
        return A, Hh, np.einsum("nah,ah->an", Hh, w2) + b2[:, None]

    active, ep = np.arange(S), 0
    while active.size and ep < max_epochs:
        ep += 1
        a = active
        A, Hh, z = fwd(Ptr, W1[a], b1[a], w2[a], b2[a])
        dz = (1 / (1 + np.exp(-z)) - YtrT[a]) / ntr
        gw2 = np.einsum("nah,an->ah", Hh, dz) + l2 * w2[a]
        gb2 = dz.sum(1)
        dA = dz.T[:, :, None] * w2[a][None] * (A > 0)
        gW1 = (Ptr.T @ dA.reshape(ntr, -1)).reshape(r, a.size, H).transpose(1, 0, 2) + l2 * W1[a]
        gb1 = dA.sum(0)
        vW1[a] = mom * vW1[a] - lr * gW1; W1[a] += vW1[a]
        vb1[a] = mom * vb1[a] - lr * gb1; b1[a] += vb1[a]
        vw2[a] = mom * vw2[a] - lr * gw2; w2[a] += vw2[a]
        vb2[a] = mom * vb2[a] - lr * gb2; b2[a] += vb2[a]
        _, _, zv = fwd(Pva, W1[a], b1[a], w2[a], b2[a])
        lv = np.mean(np.logaddexp(0, zv) - YvaT[a] * zv, axis=1)
        imp = lv < best[a]
        ia = a[imp]
        if ia.size:
            best[ia] = lv[imp]; best_ep[ia] = ep
            bW1[ia] = W1[ia]; bb1[ia] = b1[ia]; bw2[ia] = w2[ia]; bb2[ia] = b2[ia]
        active = a[(ep - best_ep[a]) < patience]
    _, _, zt = fwd(Pte, bW1, bb1, bw2, bb2)
    return zt.T, best_ep, r


def mlp_kfold(X, Ycols, g, fs, split_seed=MLP_SPLIT_SEED, init_seed=MLP_INIT_SEED):
    X = np.asarray(X, np.float64)
    n, S = Ycols.shape
    scores = np.zeros((n, S)); eps = []; ranks = []
    for fi, held_groups in enumerate(PR.grouped_folds(g, K, fs)):
        held = np.array([gi in held_groups for gi in g]); tr = ~held
        mu, sd = X[tr].mean(0), X[tr].std(0) + 1e-6
        Z = (X - mu) / sd
        va = inner_session_split(g[tr], split_seed + fi)
        isva = np.array([gi in va for gi in g]) & tr
        istr = tr & ~isva
        zt, bep, r = mlp_fold(Z[istr], Z[isva], Z[held], Ycols[istr], Ycols[isva],
                              seed=init_seed + fi, **MLP)
        scores[held] = zt; eps.append(bep); ranks.append(r)
    return scores, np.array(eps), ranks


def mlp_adam_fold(Xtr, Xva, Xte, Ytr, Yva, seed, H, lr, b1, b2, eps, l2, max_epochs, patience):
    """(iii-s) The same network, loss (mean BCE + (l2/2)||W||^2, coupled into the
    gradient), early-stopping rule and init scales as mlp_fold, trained with Adam
    (bias-corrected moments) on the full standardized 5120-d input: Adam is not
    rotation-invariant, so the span-basis shortcut of mlp_fold is not used here.
    The S label columns train as independent networks sharing one initialization."""
    D = Xtr.shape[1]
    S, ntr = Ytr.shape[1], Xtr.shape[0]
    rng = np.random.default_rng(seed)
    W1_0 = rng.normal(0, np.sqrt(2.0 / D), (D, H))
    w2_0 = rng.normal(0, np.sqrt(1.0 / H), H)
    P = [np.broadcast_to(W1_0, (S, D, H)).copy(), np.zeros((S, H)),
         np.broadcast_to(w2_0, (S, H)).copy(), np.zeros(S)]
    M1_ = [np.zeros_like(p) for p in P]
    M2_ = [np.zeros_like(p) for p in P]
    B = [p.copy() for p in P]
    best = np.full(S, np.inf); best_ep = np.zeros(S, int)
    YtrT, YvaT = Ytr.T.astype(np.float64), Yva.T.astype(np.float64)

    def fwd(Xin, W1, b1_, w2, c2):
        a = W1.shape[0]
        A = (Xin @ W1.transpose(1, 0, 2).reshape(D, a * H)).reshape(Xin.shape[0], a, H) + b1_[None]
        Hh = np.maximum(A, 0)
        return A, Hh, np.einsum("nah,ah->an", Hh, w2) + c2[:, None]

    active, ep = np.arange(S), 0
    while active.size and ep < max_epochs:
        ep += 1
        a = active
        W1, bb1, w2, c2 = (p[a] for p in P)
        A, Hh, z = fwd(Xtr, W1, bb1, w2, c2)
        dz = (1 / (1 + np.exp(-z)) - YtrT[a]) / ntr
        gw2 = np.einsum("nah,an->ah", Hh, dz) + l2 * w2
        gc2 = dz.sum(1)
        dA = dz.T[:, :, None] * w2[None] * (A > 0)
        gW1 = (Xtr.T @ dA.reshape(ntr, -1)).reshape(D, a.size, H).transpose(1, 0, 2) + l2 * W1
        gb1 = dA.sum(0)
        c1t, c2t = 1 - b1 ** ep, 1 - b2 ** ep
        for k_, gk in enumerate((gW1, gb1, gw2, gc2)):
            m_ = b1 * M1_[k_][a] + (1 - b1) * gk
            v_ = b2 * M2_[k_][a] + (1 - b2) * gk * gk
            M1_[k_][a] = m_; M2_[k_][a] = v_
            P[k_][a] = P[k_][a] - lr * (m_ / c1t) / (np.sqrt(v_ / c2t) + eps)
        _, _, zv = fwd(Xva, *(p[a] for p in P))
        lv = np.mean(np.logaddexp(0, zv) - YvaT[a] * zv, axis=1)
        imp = lv < best[a]
        ia = a[imp]
        if ia.size:
            best[ia] = lv[imp]; best_ep[ia] = ep
            for k_ in range(4):
                B[k_][ia] = P[k_][ia]
        active = a[(ep - best_ep[a]) < patience]
    _, _, zt = fwd(Xte, *B)
    return zt.T, best_ep


def mlp_adam_kfold(X, Ycols, g, fs):
    """(iii-s) Same outer folds, standardization, inner session split and init
    seeds as mlp_kfold; Adam on the full input (mlp_adam_fold)."""
    X = np.asarray(X, np.float64)
    n, S = Ycols.shape
    scores = np.zeros((n, S)); eps = []
    for fi, held_groups in enumerate(PR.grouped_folds(g, K, fs)):
        held = np.array([gi in held_groups for gi in g]); tr = ~held
        mu, sd = X[tr].mean(0), X[tr].std(0) + 1e-6
        Z = (X - mu) / sd
        va = inner_session_split(g[tr], MLP_SPLIT_SEED + fi)
        isva = np.array([gi in va for gi in g]) & tr
        istr = tr & ~isva
        zt, bep = mlp_adam_fold(Z[istr], Z[isva], Z[held], Ycols[istr], Ycols[isva],
                                seed=MLP_INIT_SEED + fi, **MLP_ADAM)
        scores[held] = zt; eps.append(bep)
    return scores, np.array(eps)


def flip_stream(y, g, seed, n):
    """(iii-s) Per-session label-flip null: draw one fair coin per session and
    XOR it into both of that session's rows, so every draw keeps the observed
    target's one-positive-one-negative-per-session structure. default_rng(seed),
    one rng.integers(0, 2, n_sessions) per draw, sessions in sorted order."""
    ug = np.array(sorted(set(np.asarray(g).tolist())))
    idx = np.searchsorted(ug, np.asarray(g))
    rng = np.random.default_rng(seed)
    y = np.asarray(y).astype(int)
    return np.stack([y ^ rng.integers(0, 2, len(ug))[idx] for _ in range(n)], axis=1)


# --------------------------------------------------------------------------- (iii) RBF kernel ridge
def _krr(K_, T, lams):
    n = K_.shape[0]
    ev, Q = np.linalg.eigh(K_)
    m = T.mean(0)
    QtT = Q.T @ (T - m)
    return [Q @ (QtT / (ev + lam * n)[:, None]) for lam in lams], m


def rbf_kfold(X, Ycols, g, fs, lams=RBF_LAMS):
    """Kernel ridge classification: targets +-1 centred on the training mean,
    alpha = (K + lambda n I)^-1 (t - mean), score = K_test alpha + mean. RBF
    kernel exp(-gamma ||x - x'||^2) on inputs standardized on the training
    fold; gamma = 1 / median squared distance over training pairs (median
    heuristic); lambda per label column by grouped 5-fold inner CV on the
    training fold only (pooled inner AUC, ties to the larger lambda)."""
    X = np.asarray(X, np.float64)
    n, S = Ycols.shape
    T = 2.0 * Ycols - 1.0
    scores = np.zeros((n, S)); lam_idx = []; gammas = []
    for fi, held_groups in enumerate(PR.grouped_folds(g, K, fs)):
        held = np.array([gi in held_groups for gi in g]); tr = ~held
        mu, sd = X[tr].mean(0), X[tr].std(0) + 1e-6
        Z = (X - mu) / sd
        sq = (Z * Z).sum(1)
        D2 = np.maximum(sq[:, None] + sq[None, :] - 2.0 * (Z @ Z.T), 0.0)
        tri_i = np.where(tr)[0]
        iu = np.triu_indices(len(tri_i), 1)
        gamma = 1.0 / float(np.median(D2[np.ix_(tri_i, tri_i)][iu]))
        gammas.append(gamma)
        Km = np.exp(-gamma * D2)
        gtr = g[tr]
        inner_scores = np.zeros((len(lams), len(tri_i), S))
        for ig in PR.grouped_folds(gtr, RBF_INNER_K, RBF_INNER_SEED + fi):
            iv = np.array([x in ig for x in gtr]); it = ~iv
            ii, vv = tri_i[it], tri_i[iv]
            alphas, m = _krr(Km[np.ix_(ii, ii)], T[ii], lams)
            Kvi = Km[np.ix_(vv, ii)]
            for li, A in enumerate(alphas):
                inner_scores[li][iv] = Kvi @ A + m
        inner_auc = np.array([auc_cols(inner_scores[li], Ycols[tr]) for li in range(len(lams))])
        best = len(lams) - 1 - np.argmax(inner_auc[::-1], axis=0)
        lam_idx.append(best)
        alphas, m = _krr(Km[np.ix_(tri_i, tri_i)], T[tri_i], lams)
        Kte = Km[np.ix_(np.where(held)[0], tri_i)]
        out = np.zeros((int(held.sum()), S))
        for li, A in enumerate(alphas):
            sel = best == li
            if sel.any():
                out[:, sel] = Kte @ A[:, sel] + m[sel]
        scores[held] = out
    return scores, np.array(lam_idx), np.array(gammas)


def run_nonlinear(data, stored_layers, n_mlp, n_rbf):
    """(iii): MLP and RBF at the read position (with nulls) and at label_a (positive control)."""
    part3 = {"mlp": {"read": {}, "label_a": {}}, "rbf": {"read": {}, "label_a": {}}}
    for fam_name, key in (("c1_read_M1M2", "read"), ("c1_label_a_M1M2", "label_a")):
        fs = fold_seed(fam_name)
        for l in stored_layers:
            X, y, g = family(data, fam_name, l)
            # MLP: observed alone
            sc, eps, ranks = mlp_kfold(X, y[:, None], g, fs)
            obs = float(auc_from_scores(sc[:, 0], y))
            rec = {"auc": obs, "best_epoch_per_fold": [int(e[0]) for e in eps],
                   "folds_at_max_epochs": int(sum(int(e[0]) == MLP["max_epochs"] for e in eps)),
                   "basis_rank_per_fold": [int(r) for r in ranks]}
            if key == "read":
                Y = np.concatenate([y[:, None], perm_stream(y, fs + l, n_mlp)], axis=1)
                scn, epsn, _ = mlp_kfold(X, Y, g, fs)
                an_ = auc_cols(scn, Y)
                nl = an_[1:]
                rec.update({"n_null": int(len(nl)), "null_mean": float(nl.mean()),
                            "null_p95": float(np.percentile(nl, 95)), "null_max": float(nl.max()),
                            "perm_p": perm_p(obs, nl), "above_p95": bool(obs > np.percentile(nl, 95)),
                            "obs_in_batch_auc": float(an_[0]),
                            "obs_alone_vs_in_batch_max_abs_score_diff": float(np.max(np.abs(scn[:, 0] - sc[:, 0]))),
                            "null_median_best_epoch": float(np.median(epsn[:, 1:])), "null": [float(v) for v in nl]})
                if l == DETERMINISM_LAYER:
                    sc2, _, _ = mlp_kfold(X, y[:, None], g, fs)
                    scn2, _, _ = mlp_kfold(X, Y, g, fs)
                    rec["determinism_rerun"] = {"obs_max_abs_score_diff": float(np.max(np.abs(sc2 - sc))),
                                                "batch_max_abs_score_diff": float(np.max(np.abs(scn2 - scn)))}
            part3["mlp"][key][str(l)] = rec
            # RBF: observed + null in one closed-form call (columns independent)
            Y = np.concatenate([y[:, None], perm_stream(y, fs + l, n_rbf)], axis=1)
            scr, lam_idx, gam = rbf_kfold(X, Y, g, fs)
            ar = auc_cols(scr, Y)
            nl = ar[1:]
            part3["rbf"][key][str(l)] = {
                "auc": float(ar[0]), "n_null": int(len(nl)), "null_mean": float(nl.mean()),
                "null_p95": float(np.percentile(nl, 95)), "null_max": float(nl.max()),
                "perm_p": perm_p(float(ar[0]), nl), "above_p95": bool(ar[0] > np.percentile(nl, 95)),
                "lambda_obs_per_fold": [RBF_LAMS[int(i)] for i in lam_idx[:, 0]],
                "gamma_median_over_folds": float(np.median(gam)), "null": [float(v) for v in nl]}
    return part3


def _nullrec(obs, nl):
    nl = np.asarray(nl, float)
    return {"auc": float(obs), "n_null": int(len(nl)), "null_mean": float(nl.mean()),
            "null_p95": float(np.percentile(nl, 95)), "null_max": float(nl.max()),
            "perm_p": perm_p(float(obs), nl), "above_p95": bool(obs > np.percentile(nl, 95)),
            "null": [float(v) for v in nl]}


def run_sensitivity(data, part3, inf_layers, adam_layers, n_adam, n_sp_mlp, n_sp_rbf, seed_offsets):
    """(iii-s): post-hoc sensitivity of the (iii) read-position results, added by the
    values-check fix. Changes no (iii) figure. All at c1_read_M1M2's rows, targets
    and outer folds (fold seed 90260905)."""
    fam = "c1_read_M1M2"
    fs = fold_seed(fam)
    out = {"mlp_seeds": {}, "mlp_adam": {}, "rbf_grid_x": {}, "rbf_sp": {}, "mlp_sp": {}}
    for l in inf_layers:
        X, y, g = family(data, fam, l)
        # (a) spec MLP, observed, alternative split/init seeds
        rec = {}
        for k_ in seed_offsets:
            sc, eps, _ = mlp_kfold(X, y[:, None], g, fs, split_seed=MLP_SPLIT_SEED + 1000 * k_,
                                   init_seed=MLP_INIT_SEED + 1000 * k_)
            rec[str(k_)] = {"auc": float(auc_from_scores(sc[:, 0], y)),
                            "best_epoch_per_fold": [int(e[0]) for e in eps]}
        out["mlp_seeds"][str(l)] = rec
        # (c) RBF, lambda grid extended below the (iii) edge; null = the record's stream, as (iii)
        Y = np.concatenate([y[:, None], perm_stream(y, fs + l, n_sp_rbf)], axis=1)
        scr, lam_idx, _ = rbf_kfold(X, Y, g, fs, lams=RBF_LAMS_X)
        ar = auc_cols(scr, Y)
        r = _nullrec(ar[0], ar[1:])
        r["lambda_obs_per_fold"] = [RBF_LAMS_X[int(i)] for i in lam_idx[:, 0]]
        out["rbf_grid_x"][str(l)] = r
        # (d) RBF on the (iii) grid, per-session label-flip null
        Ysp = np.concatenate([y[:, None], flip_stream(y, g, SP_SEED + l, n_sp_rbf)], axis=1)
        scs, _, _ = rbf_kfold(X, Ysp, g, fs)
        asp = auc_cols(scs, Ysp)
        r = _nullrec(part3["rbf"]["read"][str(l)]["auc"], asp[1:])
        r["obs_as_column0_auc"] = float(asp[0])
        out["rbf_sp"][str(l)] = r
        # (e) spec MLP, per-session label-flip null (first n_sp_mlp draws of the same flip stream)
        Ysm = np.concatenate([y[:, None], flip_stream(y, g, SP_SEED + l, n_sp_mlp)], axis=1)
        scm, _, _ = mlp_kfold(X, Ysm, g, fs)
        am = auc_cols(scm, Ysm)
        r = _nullrec(part3["mlp"]["read"][str(l)]["auc"], am[1:])
        r["obs_as_column0_auc"] = float(am[0])
        out["mlp_sp"][str(l)] = r
    for l in adam_layers:
        # (b) Adam-trained MLP; null = the first n_adam draws of the record's stream, as (iii)
        X, y, g = family(data, fam, l)
        Y = np.concatenate([y[:, None], perm_stream(y, fs + l, n_adam)], axis=1)
        sc, eps = mlp_adam_kfold(X, Y, g, fs)
        aa = auc_cols(sc, Y)
        r = _nullrec(aa[0], aa[1:])
        r["best_epoch_per_fold"] = [int(e[0]) for e in eps]
        r["null_median_best_epoch"] = float(np.median(eps[:, 1:]))
        out["mlp_adam"][str(l)] = r
    return out


# --------------------------------------------------------------------------- render (shared by both paths)
def render(o, rt):
    """Build the raw's text from the JSON dict `o` alone, plus `rt`: the stored analysis read
    at the pin (`an`), the Block line's pin hash, the interpreter's BLAS and the record-module
    hashes, and the render-only provenance. The compute path calls this on json.loads of the
    JSON text it writes; --render-only calls it on the JSON file. One function, so the two
    paths render identically from the same JSON."""
    L = []
    w = L.append
    info, an = o["inputs"], rt["an"]
    smoke, workers = o["smoke"], o["workers"]
    stamp, head, script_sha, cmd = o["code_stamp"], o["head_at_run"], o["script_sha256"], o["command"]
    block_sha_wt, block_sha_pin = o["block_sha256"], rt["block_sha_pin"]
    mod_hashes, blas = rt["mod_hashes"], rt["blas"]
    P2 = o["part_ii"]
    part2, p2s = P2["families"], P2["summary_L51_61"]
    n_ext, n_stored, ext_layers = P2["n_ext"], P2["n_stored"], P2["ext_layers"]
    stored_layers = [int(l) for l in part2["c1_read_M1M2"]]
    part4, sweep_layers, part4_summary = o["part_iv"]["per_layer"], o["part_iv"]["layers"], o["part_iv"]["summary"]
    P3 = o["part_iii"]
    part3, p3s, pc = P3["results"], P3["summary"], P3["positive_control"]
    mcfg, rcfg, posctrl_bar = P3["mlp_config"], P3["rbf_config"], P3["positive_control_bar"]
    n_mlp, n_rbf, rbf_lams = mcfg["n_null"], rcfg["n_null"], rcfg["lambdas"]
    S3 = o["part_iii_s"]
    sens3, sens_sum = S3["results"], S3["summary"]
    mlp_adam_cfg, rbf_lams_x = S3["mlp_adam_config"], S3["rbf_lambdas_extended"]
    step0 = o["step0"]
    mx = step0["max_absdiff"]
    md_k, md_l, md_s = mx["auc_kfold"], mx["auc_loso"], mx["shuffle_stats_first200"]
    rec_vs_chunk = mx["record_kfold_shuffle_null_vs_chunked_L51_read"]
    TOL, step0_pass = step0["tolerance"], step0["pass"]
    sens, stab = o["linear_estimator_sensitivity"], o["gd_stability_ratio_max_over_folds"]
    PH = o["posthoc_composition"]
    ph, ident_ok, sp_ok, n_r1 = PH["per_layer"], PH["identity_holds"], PH["start_plus_consistent"], PH["n_label_a_is_round1_tag"]
    fit = o["procedure_of_record"]["fit_lr"]
    assert o["procedure_of_record"]["kfold"] == K
    n_sess = info["n_sessions"]
    adam_layers = list(ADAM_LAYERS)   # display filter of the seed-range lines (module constant, as the compute path had it)
    n_adam = next(iter(sens3["mlp_adam"].values()))["n_null"]
    n_sp_rbf = next(iter(sens3["rbf_sp"].values()))["n_null"]
    n_sp_mlp = next(iter(sens3["mlp_sp"].values()))["n_null"]
    det_layer = next((l for l, d in part3["mlp"]["read"].items() if "determinism_rerun" in d), None)
    res_k = {(n, int(l)): {"auc_kfold": d["auc_kfold"], "auc_loso": d["auc_loso"]} for n in M1M2 for l, d in part2[n].items()}
    n_auc_perm = (sum(d["n_null"] for n in M1M2 for d in part2[n].values())
                  + sum(part4[str(l)]["n_null"] for l in sweep_layers if l not in stored_layers))
    n_kfold_jobs = (sum(len(v) for v in step0["auc_kfold"].values())
                    + len([l for l in sweep_layers if l not in stored_layers]))

    w(f"# {o['title']}")
    w("")
    w(f"- Code stamp: {stamp} (date -u, inside the script)")
    w(f"- HEAD at run time: {head} (locators below are pinned to {PIN} = {PIN_FULL})")
    w(f"- Block: `{BLOCK}` sha256 {block_sha_wt} (working tree); at {PIN}: {block_sha_pin}; routed {BLOCK_SHA}: "
      f"{'MATCH' if block_sha_wt == BLOCK_SHA == block_sha_pin else 'MISMATCH'}")
    w(f"- Script: `{SCRIPT_REL}` sha256 {script_sha}")
    w(f"- Interpreter: {o['interpreter']} (Python {o['python']}, numpy {o['numpy']}, BLAS {blas} per numpy.show_config)")
    w(f"- Command: `{cmd}`")
    w(f"- Workers: {workers} processes for the record-function jobs, VECLIB_MAXIMUM_THREADS=1 in each; the nonlinear fits run in the main process concurrently with the pool")
    if smoke:
        w("- **SMOKE RUN (40 sessions, 3 layers, 20 draws): NOT A RESULT.**")
    rr_ = rt.get("render")
    if rr_:
        w(f"- **Rendered by `--render-only`** (this file): stamp {rr_['stamp']} (date -u, inside the script); HEAD {rr_['head']}; rendering script `{SCRIPT_REL}` sha256 {rr_['script_sha']}; command `{rr_['cmd']}`; input JSON `{rr_['json_rel']}` sha256 {rr_['json_sha']}, read and not rewritten. "
          f"No fit was re-run: every figure below is read from that JSON or from that pinned stored analysis (`{ANALYSIS_REL}` at {PIN}) by `render()`, the function the compute path also calls on the JSON text it writes, so on the same numbers a compute run's raw differs from this file only in the run lines above and in lacking this line. "
          f"The Code stamp, HEAD, Script, Command and Workers lines above are the compute run's, read from the JSON (the Script line names the script that computed it). Evaluated at this render, not read from the JSON: the pinned stored analysis (`git show {PIN}:{ANALYSIS_REL}`: the Figures section's stored 200-draw 95th and the label-distance check; where each is printed, Values-check R4-1), the Block line's hash at the pin, the BLAS name, and the record-module hashes (Inputs). "
          "Re-rendering the same JSON in the same checkout changes only this line. The equivalence check (the round-1 text, rendered from round 1's JSON, equals round 1's compute-path raw byte for byte) is in Values-check, round 2.")
    w("- Run-dependent lines: the stamp line (the one exception task rule 11 allows); the HEAD line changes only if another session commits, and the Command and Workers lines only if other arguments are passed (e.g. --out/--json-out into scratch). Everything else regenerates byte-identically from the same inputs. Wall-clock timing is not in this raw: it goes to stderr and to the JSON's `timing_nondeterministic` (a timing observation, not a figure).")
    w(f"- Referent split (a note, not a STOP): block :49 names one N3 output; N3 is split across two items. Parts (i), (i-b), (v) are in `{SIBLING_RAW}` (+ .json), from committed JSON; parts (ii), (iii), (iv) are here (+ `.json`), refits on the local arrays. Both are item N3 for N1's ledger.")
    w("- Status vocabulary (task rule 4): every figure line or table column below carries one of reproduced | log-only | not found | discrepant | computed-new. 'reproduced' = this script recomputes a value stored in a committed JSON at the pin and prints it equal; the recomputation reads the local gitignored arrays, whose 1,326 fingerprints match the committed `stageC_reads.json` (Inputs). 'computed-new' = a computation the block asks for (or a declared check/sensitivity) with no stored counterpart.")
    w("")
    w("## Inputs")
    for rel, d in info["inputs"].items():
        w(f"- `{rel}` at {PIN}: sha256 {d['sha256_at_pin']}; working tree equal: {d['working_tree_equals_pin']}. Read from `git show {PIN}:{rel}`.")
    w("- Record modules imported (read-only, from the working tree): " + "; ".join(
        f"`{rel}` sha256 {d['wt'][:16]} (working tree) vs {d['pin'][:16]} (at {PIN}): {'equal' if d['wt'] == d['pin'] else 'DIFFERENT'}"
        for rel, d in mod_hashes.items()) + ".")
    w(f"- Residual arrays: `data/echo/stageC_resid_s*.npz`, {info['n_npz']} files (local, gitignored), one per session in `stageC_reads.json` (sessions sorted by id, as `analyze_c`).")
    w(f"- Every array fingerprint (sha16 over float32 bytes, `adapters.base.sha16_arr`) checked against `stageC_reads.json` npz_sha16_by_key: {info['fingerprints_checked'] - info['fingerprints_bad']}/{info['fingerprints_checked']} match. [status: reproduced -- the committed fingerprints]")
    sd_ = info["shapes_dtypes_first_file"]
    w("- Shapes/dtypes (first file; asserted equal layer list in all files): " + "; ".join(f"`{k}` {v[0]} {v[1]}" for k, v in sd_.items()))
    w(f"- Layers present in the arrays: {info['layers_present'][0]}..{info['layers_present'][-1]} ({len(info['layers_present'])} layers). Positions axis = (read, label_a, label_b).")
    dist_st = an["label_position_distance_to_read"]
    dist_ok = ([dist_st["label_a"]["min"]] == [dist_st["label_a"]["max"]] == info["read_minus_label_a_tokens"]
               and [dist_st["label_b"]["min"]] == [dist_st["label_b"]["max"]] == info["read_minus_label_b_tokens"])
    w(f"- Capture positions equal `stageC_reads.json` capture_positions in every file: {'yes' if not info['positions_mismatch_sessions'] else 'NO ' + str(info['positions_mismatch_sessions'])}; read minus label_a = {info['read_minus_label_a_tokens']} tokens, read minus label_b = {info['read_minus_label_b_tokens']} tokens (all sessions). Stored `stageC_analysis.json` label_position_distance_to_read: label_a min/max {dist_st['label_a']['min']}/{dist_st['label_a']['max']}, label_b {dist_st['label_b']['min']}/{dist_st['label_b']['max']}: {'equal' if dist_ok else 'DIFFERENT'}. [status: {'reproduced' if dist_ok else 'discrepant'}]")
    w(f"- label_a == tag_plus balance (sessions): {info['a_is_plus_balance']}. [status: computed-new, descriptive count from the committed `stageC_reads.json`]")
    w("")
    w("## Construction fact: layers <= 48 (stageC_analysis.json `le48_control`), checked on the arrays")
    le = info["le48"]
    le_ok = (le["cells_checked"] == le["stored_le48_control"]["cells_checked"] and le["n_bad"] == 0
             and le["stored_le48_control"]["all_identical_to_shadow"] is True)
    w(f"- Every key (13 per file: M0|shadow, M1-M4, B1-B4, B1x-B4x), every position (3), every layer 0..48 (49) compared to the shadow with exact float32 equality: {le['cells_checked']} cells, {le['n_bad']} differ. Stored: {le['stored_le48_control']}. [status: {'reproduced' if le_ok else 'discrepant'}]")
    w(f"- Consequence at the read position: the M1 row equals the M2 row for every session at every layer <= 48 ({sum(info['read_M1_row_equals_M2_row_le48'].values())}/{len(info['read_M1_row_equals_M2_row_le48'])} layers in 40..48 checked directly). A family's two rows per session then carry opposite labels on identical inputs, so any deterministic scorer gives equal score multisets to the two classes and AUC is exactly 0.500: layers <= 48 are uninformative by construction (the record's steering layer is L48, `recon_echo.py` LAYER = 48; the arrays show every layer <= 48 bit-identical to the shadow, as above). [status: computed-new, a check on the arrays]")
    w(f"- Above 48 the rows differ: sessions with M1 row != M2 row at the read position: " + ", ".join(f"L{l} {v}/{info['n_sessions']}" for l, v in info["read_sessions_M1_neq_M2_above48"].items()) + ". [status: computed-new, a check on the arrays]")
    w("")
    w("## STEP 0 -- the stored Stage C linear statistics through the record's own procedure")
    w("Procedure of record (scripts/recon_echo.py `analyze_c` + `_b_job`, valence_core/echo/probe.py), imported, not re-implemented: "
      f"rows = M1 and M2 state rows at the position (2N = {2 * info['n_sessions']}; M3/M4 for *_random; shadow rows, N, for *_TEXTONLY); "
      "targets: read and label_a = 1 iff label_a == tag_plus for the M1 row and the reverse for M2; label_b = the same for label_b; "
      f"`fit_lr`: standardize on the fit rows (sd + 1e-6), full-batch gradient-descent logistic regression, seed {fit['seed']} init N(0, 0.01), {fit['iters']} iterations, rate {fit['rate']}, L2 {fit['l2']}; "
      "AUC = `discrim.auc_from_scores` (Mann-Whitney, ties 0.5) on pooled held-out scores; grouped 10-fold, every row of a session in one fold (`grouped_folds`), "
      "fold seed 90260905 + 1000 x family index in analyze_c's order (read_M1M2 90260905, label_a_M1M2 90263905, label_b_M1M2 90266905); "
      "label-shuffle null on the SAME folds, permutations across ALL rows from default_rng(fold seed + layer), one rng.permutation per draw; LOSO beside.")
    w("")
    s0 = lambda ok: "reproduced" if ok else "discrepant"   # noqa: E731
    RS = "reproduced" if step0_pass else "DISCREPANT (STEP 0 FAIL)"
    w(f"- auc_kfold, 9 c1 families x {len(stored_layers)} stored layers: max |reproduced - stored| = {md_k:.3g} [status: {s0(md_k <= TOL)}]")
    w(f"- auc_loso, the 3 M1M2 families x {len(stored_layers)} layers: max |diff| = {md_l:.3g} [status: {s0(md_l <= TOL)}]")
    w(f"- shuffle95 / shuffle_mean / shuffle_max from the first 200 draws of the record's stream, 3 M1M2 families x {len(stored_layers)} layers: max |diff| = {md_s:.3g} [status: {s0(md_s <= TOL)}]")
    w(f"- The record's `kfold_shuffle_null` called directly (c1_read_M1M2, L51, {n_stored} draws) vs this script's chunked calls of `kfold_auc` on the same permutations: max |diff| = {rec_vs_chunk:.3g} [a check of this script's chunking]")
    w(f"- Not reproduced here: the stored shuffle statistics of the M3M4_random and TEXTONLY families (not needed for (ii)-(iv)).")
    w(f"- **STEP 0: {'PASS' if step0_pass else 'FAIL -- STOP on (ii)-(iv): new numbers below are NOT comparable'}** (tolerance {TOL:g}).")
    w("")
    w("### Why the 1,000-draw null was not vectorized")
    n_sens_obs_eq = sum(d["batched_obs"] == d["record_obs"] for d in sens.values())
    n_sens_null_eq = sum(d["max_absdiff_first5"] == 0.0 for d in sens.values())
    w(f"[status: computed-new, a diagnostic; changes no stored value] The block asks for the 1,000 shuffles 'with the same grouped CV' (:45) and says nothing about vectorizing; Code's standard here is that a vectorized null is acceptable only if it is numerically the same estimator. A batched re-implementation of `fit_lr` (all label columns in one gemm, same standardization, init, iterations, rate, L2, bias update) was compared with the record's per-draw path at {len(sens)} family-layers: observed AUC equal at {n_sens_obs_eq}/{len(sens)}; first five shuffled-label AUCs all equal at {n_sens_null_eq}/{len(sens)}:")
    for kk, d in sens.items():
        w(f"- {kk}: observed batched {d['batched_obs']:.6f} vs record {d['record_obs']:.6f} (max |score diff| {d['obs_max_abs_score_diff']:.2g}); first 5 draws batched {d['batched_first5']} vs record {d['record_first5']}, max |diff| {d['max_absdiff_first5']:.4f}.")
    allr = [v for fam in stab.values() for v in fam.values()]
    allr_hi = [v for fam in stab.values() for l, v in fam.items() if int(l) > LAYER]
    w(f"- Cause (Code's diagnosis): the stored fit's step size is beyond the bound that guarantees gradient-descent convergence. With L = lambda_max(Xf^T Xf / n_fit) / 4 + L2 (an upper bound on the logistic loss's Hessian), lr x L, max over the 10 folds, ranges {min(allr):.1f}-{max(allr):.1f} over the 3 M1M2 families x {len(stored_layers)} layers ({min(allr_hi):.1f}-{max(allr_hi):.1f} above L48), against 2. The two paths differ only in floating-point summation order (gemm vs gemv), so where they disagree it is numerical sensitivity of an iteration run past that bound, not a different estimator definition. The record's outputs are deterministic and reproduce {'exactly (STEP 0)' if step0_pass else 'as STEP 0 reports'}; only the record's own per-draw (gemv) path is the record's estimator. (ii) therefore calls the record's `kfold_auc` per draw. This changes no stored value; it is reported for the PI (it bears on how the stored null may be re-derived on another BLAS).")
    w("")
    w("## (ii) Permutation null at label_a, label_b and the read position")
    w(f"Work in this section: {n_auc_perm} shuffled-label AUCs and {n_kfold_jobs} kfold/LOSO jobs through the record's per-draw path. Its wall-clock cost is a timing observation, not a figure, and is not in this raw (stderr and the JSON's `timing_nondeterministic`): the builder's run (its raw, sha256 2182f1f5...f8c6, uncommitted and superseded by this one) measured 11.83 null AUC/s with 6 workers and extrapolated 76 min for 1,000 draws at all 54 stored family-layers; the values-checker's re-run of that script measured 11.20 and 80 min.")
    w(f"Decision (fixed by the builder before the first full run, from a timing probe in scratch -- a timing observation, not reproducible, not a figure: the record's `kfold_auc` cost ~0.17 s single-process and the pool saturated near 12 AUC/s, so 54,000 draws ~ 75 min on top of (iii)): "
      f"**{n_ext} draws at L{ext_layers[0]}-L{ext_layers[-1]} (the layers the note cites) for all three families; the stored count, {n_stored}, at the other stored layers ("
      + ", ".join(f"L{l}" for l in stored_layers if l not in ext_layers) + ") and at the new sweep layers L45-L47 (iv).** "
      f"The first {n_stored} draws of every family-layer are the stored null's draws (STEP 0); the extended draws continue the same stream.")
    w("Statistic: grouped 10-fold AUC of the stored estimator (probe = standardized L2 logistic regression on the 5120-d residual at the position and layer; contrast = M1 vs M2 rows, target = pole of the label under the mask). "
      f"Null = AUCs of the same procedure with the target permuted across all {2 * info['n_sessions']} rows, same folds (the record's null; as stored, it does not preserve the observed target's one-positive-one-negative-per-session structure). Permutation p = (1 + #{{null >= observed}}) / (1 + n), one-sided (upper).")
    for name in M1M2:
        w("")
        w(f"### {name}")
        w("| layer | AUC (10-fold) | LOSO | n draws | null mean | null 95th | null max | perm p | stored-200 95th | status |")
        w("|---|---|---|---|---|---|---|---|---|---|")
        for l in stored_layers:
            d = part2[name][str(l)]
            stt = (f"AUC, LOSO, stored-200 95th: {RS}; null mean/95th/max: computed-new ({d['n_null']:,} draws; first 200 = the stored draws); perm p: computed-new"
                   if d["extended"] else
                   f"AUC, LOSO, null mean/95th/max, stored-200 95th: {RS} (200 = the stored draws); perm p: computed-new")
            w(f"| {l} | {d['auc_kfold']:.4f} | {d['auc_loso']:.4f} | {d['n_null']} | {d['null_mean']:.4f} | {d['null_p95']:.4f} | {d['null_max']:.4f} | {d['perm_p']:.4f} | {d['null200_p95']:.4f} | {stt} |")
    w("")
    w(f"### (ii) summary over L{ext_layers[0]}-L{ext_layers[-1]} ({n_ext} draws each)")
    for name in M1M2:
        s = p2s[name]
        w(f"- {name}: AUC {s['auc_min']:.4f}-{s['auc_max']:.4f}; null mean {s['null_mean_min']:.4f}-{s['null_mean_max']:.4f}; null 95th {s['p95_min']:.4f}-{s['p95_max']:.4f}; perm p (one-sided upper) {s['p_min']:.4f}-{s['p_max']:.4f}; above the {n_ext}-draw 95th at {s['n_layers_above_p95']}/{s['n_layers']} layers. [status: AUC {RS}; null and p computed-new]")
    p95_all_ext = [part2[n][str(l)]["null_p95"] for n in M1M2 for l in ext_layers]
    p95_200_all = [part2[n][str(l)]["null200_p95"] for n in M1M2 for l in stored_layers if l > LAYER]
    w(f"- Pooled over the three families at L{ext_layers[0]}-L{ext_layers[-1]}: {n_ext}-draw 95th {min(p95_all_ext):.4f}-{max(p95_all_ext):.4f} (95th of the first {n_stored} draws -- the stored draws -- at the stored layers above L48, all three families: {min(p95_200_all):.4f}-{max(p95_200_all):.4f}). [status: {n_ext}-draw 95th computed-new; 200-draw 95th {RS}]")
    w(f"- Minimum attainable p at {n_ext} draws = 1/{n_ext + 1} = {1 / (n_ext + 1):.6f}; at {n_stored} draws 1/{n_stored + 1} = {1 / (n_stored + 1):.6f}.")
    w("")
    w("## (iv) Linear layer sweep at the read (decision) position, L44-L61")
    w(f"Layers of 44-61 present in the arrays: all 18 (the arrays carry layers 0-63). The stored analysis has L44 and L48-L61 of this range (no L45-L47); L45-L47 are computed here with the stored estimator, folds and stream of c1_read_M1M2 (fold seed 90260905, permutation seed 90260905 + layer). Probe/contrast/CV as in (ii).")
    w("| layer | AUC (10-fold) | LOSO | n draws | null mean | null 95th | perm p | in stored analysis | <= 48 (0.5 by construction) | status |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for l in sweep_layers:
        d = part4[str(l)]
        if not d["in_stored_analysis"]:
            stt = "all columns computed-new (null arrays in the JSON's part_iv.per_layer)"
        elif d["n_null"] > N_STORED:
            stt = f"AUC, LOSO: {RS}; null, p: computed-new"
        else:
            stt = f"AUC, LOSO, null: {RS}; p: computed-new"
        w(f"| {l} | {d['auc_kfold']:.4f} | {d['auc_loso']:.4f} | {d['n_null']} | {d['null_mean']:.4f} | {d['null_p95']:.4f} | {d['perm_p']:.4f} | {'yes' if d['in_stored_analysis'] else 'no (new)'} | {'yes' if d['le48_by_construction'] else 'no'} | {stt} |")
    hi = [l for l in sweep_layers if l > LAYER]
    aucs_hi = [part4[str(l)]["auc_kfold"] for l in hi]
    le_vals = part4_summary["auc_values_le48"]
    above = part4_summary["layers_above_p95"]
    p_lt05 = part4_summary["layers_p_lt_05"]
    lmax = part4_summary["argmax_layer"]
    am_ = part4_summary["max_adjacent_abs_diff_L49_61"]
    adj_max = (am_["from"], am_["to"], am_["absdiff"]) if am_ else None
    w(f"- L44-L48: AUC values {le_vals} (by construction). L49-L61: AUC {min(aucs_hi):.4f}-{max(aucs_hi):.4f} (max at L{lmax}); L51-L61: {part4_summary['auc_min_L51_61']:.4f}-{part4_summary['auc_max_L51_61']:.4f}. Layers above their own null 95th: {above if above else 'none'}; layers with perm p (one-sided upper) < .05: {p_lt05 if p_lt05 else 'none'}. "
      + (f"Largest difference between adjacent informative layers: {adj_max[2]:.4f} (L{adj_max[0]} {part4[str(adj_max[0])]['auc_kfold']:.4f} to L{adj_max[1]} {part4[str(adj_max[1])]['auc_kfold']:.4f}). " if adj_max else "")
      + f"[status: AUC at L44, L48-L61 {RS}; L45-L47 computed-new; nulls and p as in the table]")
    in_band = all(0.50 <= v <= 0.55 for v in aucs_hi)
    w(f"- Reading: across the {len(hi)} informative layers (L{hi[0]}-L{hi[-1]}) the AUC {'stays inside .50-.55 at every layer' if in_band else 'leaves .50-.55 at ' + str([l for l in hi if not 0.50 <= part4[str(l)]['auc_kfold'] <= 0.55])} and {'no layer is above its own null 95th' if not above else str(len(above)) + ' layer(s) are above their own null 95th: ' + str(above)}. "
      + ("The .50-.55 is therefore not a one-layer accident: it holds at every informative layer of the sweep, "
         + (f"adjacent informative layers differ by at most {adj_max[2]:.3f} (L{adj_max[0]} to L{adj_max[1]}), " if adj_max else "")
         + "and none is above its own shuffled-label 95th." if (in_band and not above) else "The .50-.55 description does not hold uniformly; see the table."))
    # ---------------- POST-HOC (descriptive): composition of the read-position target
    w("")
    w("## POST-HOC, descriptive (CLAUDE.md@bbc9ffe:311-312, ledger 11: 'Post-hoc analyses labeled post-hoc; they license pre-registrations, never verdicts'; not asked by the block): what the read-position target is composed of")
    w("[status: every figure in this section is computed-new and post-hoc, except the pooled read-target column, which is the stored c1_read_M1M2 auc_kfold (" + RS + ")]")
    w(f"Added after a first full run of this script showed (iii) above its nulls; that run's outputs are superseded by this one. Identity, asserted on all {n_sess} sessions: the read target (label_a's pole under the mask, M1 row) = [label_a == round-1 tag] XNOR [round 1 carried + under M1] (`start_plus`; consistent with spans[0].tag == tag_plus at every session: {sp_ok}); identity holds: {ident_ok}. "
      f"So within sessions where label_a is the round-1 tag ({n_r1}) the target equals the first-round sign, and within the others ({n_sess - n_r1}) its negation. Linear probe = the stored estimator (`kfold_auc`, grouped 10-fold, fold seed {fold_seed('c1_read_M1M2')} applied to each subset's sessions, so the subset partitions differ from the pooled family's); no null (point estimates only).")
    w("| layer | linear AUC, label_a is round-1 tag | linear AUC, label_a is not round-1 tag | linear AUC, first-round-sign target, all sessions | pooled read target (stored estimator) | MLP (iii) | RBF (iii) |")
    w("|---|---|---|---|---|---|---|")
    for l in [x for x in stored_layers if x > LAYER]:
        r_ = ph[str(l)]
        w(f"| {l} | {r_['label_a_is_round1_tag']['auc_kfold']:.4f} | {r_['label_a_is_not_round1_tag']['auc_kfold']:.4f} | {r_['first_round_sign_all']['auc_kfold']:.4f} | {res_k[('c1_read_M1M2', l)]['auc_kfold']:.4f} | {part3['mlp']['read'][str(l)]['auc']:.4f} | {part3['rbf']['read'][str(l)]['auc']:.4f} |")
    sub_lo = min(min(ph[k]["label_a_is_round1_tag"]["auc_kfold"], ph[k]["label_a_is_not_round1_tag"]["auc_kfold"]) for k in ph if 51 <= int(k) <= 61)
    sub_hi = max(max(ph[k]["label_a_is_round1_tag"]["auc_kfold"], ph[k]["label_a_is_not_round1_tag"]["auc_kfold"]) for k in ph if 51 <= int(k) <= 61)
    frs = [ph[k]["first_round_sign_all"]["auc_kfold"] for k in ph if 51 <= int(k) <= 61]
    w(f"- L51-L61: within-subgroup linear AUC {sub_lo:.4f}-{sub_hi:.4f}; first-round sign {min(frs):.4f}-{max(frs):.4f}; pooled linear (the stored read family) {part4_summary['auc_min_L51_61']:.4f}-{part4_summary['auc_max_L51_61']:.4f}.")
    w(f"- Code's reading (not a test of mechanism, and not a verdict): the stored linear probe reads the first-round sign at the read position ({min(frs):.3f}-{max(frs):.3f} at L51-L61); the binding target is that sign composed with a text fact (menu order relative to round 1), an XOR across the two subgroups, which the stored linear probe does not read pooled ({part4_summary['auc_min_L51_61']:.3f}-{part4_summary['auc_max_L51_61']:.3f} at L51-L61). No claim is made about other linear functionals: only this one estimator (fixed hyperparameters, 10-fold and LOSO) was tested. The nonlinear reads in (iii) are consistent with learning that composition. Whether the model's own choice readout uses it is not addressed here.")
    w("")
    w("## (iii) Nonlinear reads at the read (decision) position; positive control at label_a")
    w("[status: every figure in (iii) and (iii-s) is computed-new, except the linear column of the positive-control table (stored c1_label_a_M1M2 auc_kfold, " + RS + ")]")
    w("Same rows, targets, grouped 10-fold folds and permutation stream as the linear family (c1_read_M1M2: fold seed 90260905; c1_label_a_M1M2: 90263905; permutation seed = fold seed + layer). Contrast = M1 vs M2 rows at the position, target = label_a's pole under the mask. Same stored layers. Fitting uses training-fold rows only; the held-out fold is scored once. AUC = Mann-Whitney on the pooled held-out scores; perm p = (1 + #{null >= observed}) / (1 + n), permutation test, one-sided (upper).")
    w(f"- **MLP** (numpy): input standardized on the training fold (sd + 1e-6); inner validation = {int(mcfg['val_frac'] * 100)}% of the training fold's sessions (both rows of a session together; default_rng({mcfg['split_seed']} + outer fold index)); "
      f"one hidden layer of {mcfg['H']} ReLU units, one logit output; init W1 ~ N(0, 2/5120), w2 ~ N(0, 1/{mcfg['H']}), biases 0, default_rng({mcfg['init_seed']} + outer fold index), the same init for the observed fit and every shuffled fit; "
      f"loss = mean binary cross-entropy + ({mcfg['l2']:g}/2)(||W1||^2 + ||w2||^2); full-batch gradient descent, heavy-ball momentum {mcfg['mom']}, rate {mcfg['lr']}; up to {mcfg['max_epochs']} epochs; "
      f"early stopping: inner-validation BCE after every epoch, stop {mcfg['patience']} epochs after the last improvement, best-epoch weights restored; no refit on the validation rows. "
      "Computed in an orthonormal basis of the inner-train rows' span (SVD; rank at most n_inner_train, per fold in the JSON): with the first-layer init drawn in that basis and a rotation-invariant optimizer this is the same computation as the MLP on the full 5120-d input with its first-layer init projected onto that span. "
      f"Observed fit run alone; null = {n_mlp} draws trained as independent columns of one batch (the observed labels also run as column 0 of that batch, as a numerical-stability check). Hyperparameters were fixed before any read-position output was inspected and were not changed afterwards. Outputs inspected before the builder's run: MLP at label_a L51 and L56 (both 1.0) and a read-position L56 fit for timing only (no AUC printed); RBF at label_a and label_b, L48/L51/L56; four 40-session smoke runs of the whole script (read and label_a at L44/L51/L56), after which only report text changed; and one earlier full run of this script (every output), after which only the JSON's null precision (full float64 instead of 8 decimals), this disclosure and the POST-HOC section changed. Since then: the builder's run (every output), the values-checker's re-run of it and the fixer's scratch probes (Adam MLP at L51/L56/L61; the spec MLP at four other seed pairs at L51/L56/L61; the extended-grid and per-session-flip RBF at L51); no (iii) hyperparameter above changed after any of them. The (iii-s) section was added after all of these (post-hoc). Round 2 (the values-checker's re-run of the fixed script, every output, and its own isotropic-init MLP at L51/L56) changed report text only; no (iii) or (iii-s) hyperparameter changed after it. "
      "Round 3 (pass 3 of the values-checker: a full re-run of round 2's script, every output, and its own re-implementations of the spec MLP, the MLP and RBF nulls and the POST-HOC linear fits) changed report text only (Values-check, round 4); no (iii) or (iii-s) hyperparameter changed after it.")
    w(f"- **RBF kernel ridge classifier** (numpy): input standardized on the training fold; K = exp(-gamma ||x - x'||^2), gamma = 1 / median squared distance over training-row pairs (median heuristic, per outer fold); "
      f"targets +-1 centred on the training mean; alpha = (K + lambda n I)^-1 (t - mean); score = K_test alpha + mean; lambda in {rbf_lams} chosen per label column by grouped {rcfg['inner_k']}-fold inner CV on the training fold only (default_rng({rcfg['inner_seed']} + outer fold index); pooled inner AUC; ties to the larger lambda), then refit on the whole training fold. "
      f"Closed form, so the observed labels and {n_rbf} draws are solved together (columns independent).")
    w(f"- Positive-control criterion (written into the script before the first full run, after the label_a fits listed above had been seen): AUC >= {posctrl_bar} at every layer L51-L61 at label_a, for each classifier; otherwise the classifier is reported as broken.")
    w("")
    w("### At the read position")
    w(f"| layer | MLP AUC | MLP null mean | MLP null 95th ({n_mlp}) | MLP perm p (1-sided) | MLP obs best epoch per fold | RBF AUC | RBF null mean | RBF null 95th ({n_rbf}) | RBF perm p (1-sided) | RBF lambda (obs, per fold) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for l in stored_layers:
        m, r = part3["mlp"]["read"][str(l)], part3["rbf"]["read"][str(l)]
        w(f"| {l} | {m['auc']:.4f} | {m['null_mean']:.4f} | {m['null_p95']:.4f} | {m['perm_p']:.4f} | {m['best_epoch_per_fold']} | {r['auc']:.4f} | {r['null_mean']:.4f} | {r['null_p95']:.4f} | {r['perm_p']:.4f} | {r['lambda_obs_per_fold']} |")
    mr_hi = [(l, part3["mlp"]["read"][str(l)]) for l in stored_layers if l > LAYER]
    w(f"- MLP, L49-L63: AUC {p3s['mlp_read_auc_range_gt48'][0]:.4f}-{p3s['mlp_read_auc_range_gt48'][1]:.4f}; own null 95th {p3s['mlp_read_p95_range_gt48'][0]:.4f}-{p3s['mlp_read_p95_range_gt48'][1]:.4f}; layers above the 95th: {p3s['mlp_read_layers_above_p95'] or 'none'}; layers with perm p < .05: {p3s['mlp_read_layers_p_lt_05'] or 'none'}. L40/L44/L48: {p3s['mlp_le48_auc']}.")
    w(f"- RBF, L49-L63: AUC {p3s['rbf_read_auc_range_gt48'][0]:.4f}-{p3s['rbf_read_auc_range_gt48'][1]:.4f}; own null 95th {p3s['rbf_read_p95_range_gt48'][0]:.4f}-{p3s['rbf_read_p95_range_gt48'][1]:.4f}; layers above the 95th: {p3s['rbf_read_layers_above_p95'] or 'none'}; layers with perm p < .05: {p3s['rbf_read_layers_p_lt_05'] or 'none'}. L40/L44/L48: {p3s['rbf_le48_auc']}.")
    le_ = p3s["rbf_read_obs_fits_at_grid_lower_edge"]
    w(f"- RBF lambda: in {le_['n']} of the {le_['of']} observed outer-fold fits at L49-L63 the inner CV chose the grid's lowest value, {le_['lower_edge']:g}, so the grid's lower edge binds and these RBF AUCs are limited by the grid (likely an underestimate of what this classifier family reads). A declared re-run with the grid extended to 1e-7 is in (iii-s)(c); it changes no figure above, and the exceedance above stands as computed on this grid.")
    w(f"- Multiplicity, descriptive: {len(mr_hi)} correlated layers per classifier; at a per-layer 5% level about {0.05 * len(mr_hi):.1f} exceedances are expected by chance if they were independent.")
    any_nl = p3s["mlp_read_layers_above_p95"] or p3s["rbf_read_layers_above_p95"]
    # 'permutation ceiling' (block :50) read two ways: the 95th (what (iii) reports, :46) and the null maximum
    rd_hi = {c: [(l, part3[c]["read"][str(l)]) for l in stored_layers if l > LAYER] for c in ("mlp", "rbf")}
    mx_in = {c: [l for l, d in v if d["auc"] > d["null_max"]] for c, v in rd_hi.items()}
    mx_out = {c: [l for l, d in v if not d["auc"] > d["null_max"]] for c, v in rd_hi.items()}
    mx_both = [l for l in mx_in["mlp"] if l in mx_in["rbf"]]
    mx_out_txt = "; ".join(f"{c.upper()} {', '.join(f'L{l} ' + format(part3[c]['read'][str(l)]['auc'], '.4f') + ' vs max ' + format(part3[c]['read'][str(l)]['null_max'], '.4f') for l in v)}"
                           for c, v in mx_out.items() if v)
    sub_lo_ = min(min(ph[k]["label_a_is_round1_tag"]["auc_kfold"], ph[k]["label_a_is_not_round1_tag"]["auc_kfold"]) for k in ph if 51 <= int(k) <= 61)
    sub_hi_ = max(max(ph[k]["label_a_is_round1_tag"]["auc_kfold"], ph[k]["label_a_is_not_round1_tag"]["auc_kfold"]) for k in ph if 51 <= int(k) <= 61)
    frs_ = [ph[k]["first_round_sign_all"]["auc_kfold"] for k in ph if 51 <= int(k) <= 61]
    w("- Outcome for the note (block :46, :50; either outcome is reported, neither changes a label): "
      + ("neither nonlinear read exceeds its own shuffled-label 95th percentile at any layer above L48 at the read position." if not any_nl else
         f"a nonlinear read exceeds its own shuffled-label 95th percentile at the read position at MLP {p3s['mlp_read_layers_above_p95'] or 'no layer'}, RBF {p3s['rbf_read_layers_above_p95'] or 'no layer'} (per-layer, uncorrected; see the multiplicity line). The block's rule for this case (:50) keeps link 3's sentence and adds one line stating the nonlinear result; that line is the design seat's to write.")
      + f" 'Permutation ceiling' (:50) is read here as the null's 95th percentile, the statistic (iii) asks to report (:46). Against the null maximum instead (MLP {n_mlp:,} draws, RBF {n_rbf:,}; a null's maximum grows with its number of draws, so the two are not on the same footing), the observed AUC exceeds it at MLP {mx_in['mlp'] or 'no layer'} ({len(mx_in['mlp'])}/{len(rd_hi['mlp'])}) and RBF {mx_in['rbf'] or 'no layer'} ({len(mx_in['rbf'])}/{len(rd_hi['rbf'])}), both classifiers at {len(mx_both)}/{len(rd_hi['mlp'])} layers ({_runs(mx_both)}); not at " + (mx_out_txt or "any layer") + ". [status: computed-new]"
      + f" For the sentence's wording ('in any linear functional'): (ii) and (iv) tested one linear estimator, the stored probe with its fixed hyperparameters (10-fold and LOSO), not every linear functional; in the POST-HOC section above (post-hoc, descriptive, computed-new) that same estimator reads the first-round sign at {min(frs_):.3f}-{max(frs_):.3f} and the binding target within each menu-order subgroup at {sub_lo_:.3f}-{sub_hi_:.3f}, at L51-L61.")
    dm = part3["mlp"]["read"][det_layer]["determinism_rerun"] if det_layer is not None else None
    stabs = [d["obs_alone_vs_in_batch_max_abs_score_diff"] for _, d in mr_hi]
    w(f"- MLP numerics: observed-alone vs observed-as-batch-column-0, max |score diff| over L49-L63 = {max(stabs):.3g}; AUC equal at {sum(abs(d['auc'] - d['obs_in_batch_auc']) == 0 for _, d in mr_hi)}/{len(mr_hi)} layers. "
      + (f"Determinism re-run at L{det_layer}: observed max |diff| {dm['obs_max_abs_score_diff']:.3g}, null batch max |diff| {dm['batch_max_abs_score_diff']:.3g}." if dm else ""))
    sd_rng = sens_sum["mlp_seed_range_per_layer"]
    adam_above = sens_sum["adam_layers_above_p95"]
    mlpsp_above = sens_sum["mlp_flip_layers_above_p95"]
    exc_txt = ("while the exceedance held in every check run here ((iii-s): Adam above its own null 95th at "
               f"{len(adam_above)}/{len(sens3['mlp_adam'])} layers; the spec MLP above a per-session-flip null 95th at "
               f"{len(mlpsp_above)}/{len(sens3['mlp_sp'])} layers)"
               if len(adam_above) == len(sens3["mlp_adam"]) and len(mlpsp_above) == len(sens3["mlp_sp"]) else
               f"and the exceedance did not hold in every check ((iii-s): Adam above its own null 95th at {adam_above}; "
               f"the spec MLP above a per-session-flip null 95th at {mlpsp_above})")
    w(f"- MLP magnitude: the AUC level of this MLP depends on its training specification, {exc_txt}: over the spec seed pair and {len(next(iter(sens3['mlp_seeds'].values())))} other seed pairs the spec MLP reads " + ", ".join(f"L{l} {a:.3f}-{b:.3f}" for l, (a, b) in sd_rng.items() if int(l) in adam_layers) + "; the Adam-trained variant reads " + ", ".join(f"L{l} {d['auc']:.3f}" for l, d in sens3["mlp_adam"].items()) + f". The peak {p3s['mlp_read_auc_range_gt48'][1]:.4f} is a maximum over 15 layers of one specification. For the note's nonlinear line, the exceedance, or the RBF figure with its grid caveat, is the safer quotation than the MLP peak.")
    w(f"- MLP early stopping (observed fits, L49-L63): median over the {K} outer folds of the best epoch, per layer (a .5 is the mean of the middle two) " + ", ".join(f"L{l} {float(np.median(d['best_epoch_per_fold'])):.1f}" for l, d in mr_hi) + f"; null fits' median best epoch per layer {min(d['null_median_best_epoch'] for _, d in mr_hi):.1f}-{max(d['null_median_best_epoch'] for _, d in mr_hi):.1f}.")
    w("")
    w("### Positive control at label_a (the binding position)")
    w(f"| layer | MLP AUC | MLP folds at {mcfg['max_epochs']} epochs | RBF AUC | RBF null 95th ({n_rbf}) | RBF perm p | linear AUC (stored estimator) |")
    w("|---|---|---|---|---|---|---|")
    for l in stored_layers:
        m, r = part3["mlp"]["label_a"][str(l)], part3["rbf"]["label_a"][str(l)]
        w(f"| {l} | {m['auc']:.4f} | {m['folds_at_max_epochs']} | {r['auc']:.4f} | {r['null_p95']:.4f} | {r['perm_p']:.4f} | {res_k[('c1_label_a_M1M2', l)]['auc_kfold']:.4f} |")
    w(f"- MLP min over L51-L61 = {pc['mlp_min_L51_61']:.4f} -> positive control {'PASS' if pc['mlp_pass'] else 'FAIL (classifier broken)'}; RBF min = {pc['rbf_min_L51_61']:.4f} -> {'PASS' if pc['rbf_pass'] else 'FAIL (classifier broken)'}. (MLP null at label_a not computed: the control asks only that the classifier find the binding.)")
    w("")
    # ---------------- (iii-s)
    w("### (iii-s) Sensitivity of (iii) at the read position -- POST-HOC, descriptive (CLAUDE.md@bbc9ffe:311-312, ledger 11)")
    w("[status: computed-new, post-hoc] Added by the values-check fix to answer two of its findings (MLP magnitude; RBF lambda at the grid edge) and to test the exceedance against a null that keeps the target's structure. Declared in the script before this run; changes no (iii) figure. Probe rows, contrast, target and outer grouped 10-fold folds as (iii) (c1_read_M1M2, fold seed 90260905); AUC = Mann-Whitney on pooled held-out scores; every p = (1 + #{null >= observed}) / (1 + n), permutation test, one-sided (upper).")
    w(f"- (a) Spec MLP, other seeds: the (iii) MLP unchanged except the inner-split and init seeds, {mcfg['split_seed']} + 1000 k and {mcfg['init_seed']} + 1000 k (+ outer fold index), k in {list(sens3['mlp_seeds'][next(iter(sens3['mlp_seeds']))].keys())}; observed fits only.")
    w(f"- (b) Adam MLP: the (iii) network, loss (mean BCE + ({mlp_adam_cfg['l2']:g}/2)||W||^2 coupled into the gradient), init scales, seeds, inner split and early-stopping rule (patience {mlp_adam_cfg['patience']}, up to {mlp_adam_cfg['max_epochs']} epochs, best weights restored), trained with Adam (rate {mlp_adam_cfg['lr']:g}, betas {mlp_adam_cfg['b1']}/{mlp_adam_cfg['b2']}, eps {mlp_adam_cfg['eps']:g}, bias-corrected) on the full standardized 5120-d input (Adam is not rotation-invariant, so (iii)'s span-basis shortcut is not used). Null = the first {n_adam} draws of (iii)'s permutation stream (permutation across all rows), trained as columns of one batch with the observed labels as column 0.")
    w(f"- (c) RBF, extended lambda grid: (iii)'s RBF with lambda in {rbf_lams_x}; null = (iii)'s {n_rbf}-draw stream (all-rows permutation).")
    w(f"- (d), (e) Per-session label-flip null: one fair coin per session, XORed into both of its rows, so every draw keeps one positive and one negative row per session (the record's all-rows permutation does not); {S3['flip_seed']}, one rng.integers(0, 2, n_sessions) per draw. (d) RBF of (iii), {n_sp_rbf} draws; (e) MLP of (iii), the first {n_sp_mlp} draws of the same stream, trained as columns of one batch. The observed AUC is (iii)'s.")
    w("")
    sk = list(sens3["mlp_seeds"][next(iter(sens3["mlp_seeds"]))].keys())
    w("| layer | (iii) MLP AUC | " + " | ".join(f"seeds k={k_}" for k_ in sk) + " | range over the 5 |")
    w("|---|---|" + "---|" * len(sk) + "---|")
    for l, rec in sens3["mlp_seeds"].items():
        w(f"| {l} | {part3['mlp']['read'][l]['auc']:.4f} | " + " | ".join(f"{rec[k_]['auc']:.4f}" for k_ in sk) + f" | {sd_rng[l][0]:.4f}-{sd_rng[l][1]:.4f} |")
    w("")
    w(f"| layer | (iii) MLP AUC | Adam MLP AUC | Adam null mean | Adam null 95th ({n_adam}) | Adam perm p (1-sided) | above | Adam obs best epoch per fold | values-checker's own Adam MLP (its value, quoted; not recomputed here) |")
    w("|---|---|---|---|---|---|---|---|---|")
    for l, d in sens3["mlp_adam"].items():
        w(f"| {l} | {part3['mlp']['read'][l]['auc']:.4f} | {d['auc']:.4f} | {d['null_mean']:.4f} | {d['null_p95']:.4f} | {d['perm_p']:.4f} | {'yes' if d['above_p95'] else 'no'} | {d['best_epoch_per_fold']} | {CHECKER_ADAM.get(int(l), float('nan')):.4f} |")
    w("")
    w(f"| layer | (iii) RBF AUC (grid {min(rbf_lams):g}-{max(rbf_lams):g}) | extended-grid AUC (grid {min(rbf_lams_x):g}-{max(rbf_lams_x):g}) | null mean | null 95th | perm p (1-sided) | above | lambda (obs, per fold) | folds at the new lower edge |")
    w("|---|---|---|---|---|---|---|---|---|")
    for l, d in sens3["rbf_grid_x"].items():
        w(f"| {l} | {part3['rbf']['read'][l]['auc']:.4f} | {d['auc']:.4f} | {d['null_mean']:.4f} | {d['null_p95']:.4f} | {d['perm_p']:.4f} | {'yes' if d['above_p95'] else 'no'} | {[f'{x:g}' for x in d['lambda_obs_per_fold']]} | {sum(x == min(rbf_lams_x) for x in d['lambda_obs_per_fold'])}/{K} |")
    w("")
    w("| layer | RBF AUC (iii) | flip-null mean (RBF) | flip-null 95th (RBF) | perm p (RBF, 1-sided) | above (RBF) | MLP AUC (iii) | flip-null mean (MLP) | flip-null 95th (MLP) | perm p (MLP, 1-sided) | above (MLP) |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    for l in sens3["rbf_sp"]:
        dr, dm_ = sens3["rbf_sp"][l], sens3["mlp_sp"][l]
        w(f"| {l} | {dr['auc']:.4f} | {dr['null_mean']:.4f} | {dr['null_p95']:.4f} | {dr['perm_p']:.4f} | {'yes' if dr['above_p95'] else 'no'} | {dm_['auc']:.4f} | {dm_['null_mean']:.4f} | {dm_['null_p95']:.4f} | {dm_['perm_p']:.4f} | {'yes' if dm_['above_p95'] else 'no'} |")
    rx = sens3["rbf_grid_x"]
    rx_edge = sens_sum["rbf_x_obs_fits_at_new_edge"]["n"]
    rx_le4 = sens_sum["rbf_x_obs_fits_below_old_edge"]["n"]
    sp_r_above = sens_sum["rbf_flip_layers_above_p95"]
    col0_eq = sens_sum["rbf_flip_obs_column0_equal"]
    mcol0 = sens_sum["mlp_flip_obs_column0_max_abs_auc_diff"]
    w("")
    w(f"- (a) Spec MLP across the 5 seed pairs (the (iii) pair and {len(sk)} others), L49-L63: per-layer range shown; overall {min(v[0] for v in sd_rng.values()):.4f}-{max(v[1] for v in sd_rng.values()):.4f}.")
    w(f"- (b) Adam MLP: " + ", ".join(f"L{l} {d['auc']:.4f} (spec {part3['mlp']['read'][l]['auc']:.4f})" for l, d in sens3["mlp_adam"].items()) + f"; above its own null 95th at {adam_above or 'no layer'}. The values-checker's own Adam implementation read " + ", ".join(f"L{l} {v:.4f}" for l, v in CHECKER_ADAM.items()) + " (its values, quoted; its code is not in the record and differs from (b) in details the checker did not state), " + ("so the level is implementation-dependent as well." if any(abs(sens3["mlp_adam"][str(l)]["auc"] - v) > 0.05 for l, v in CHECKER_ADAM.items() if str(l) in sens3["mlp_adam"]) else "close to (b)'s."))
    w(f"- (c) Extended grid: AUC {sens_sum['rbf_x_auc_range'][0]:.4f}-{sens_sum['rbf_x_auc_range'][1]:.4f} at L49-L63 (the (iii) grid: {p3s['rbf_read_auc_range_gt48'][0]:.4f}-{p3s['rbf_read_auc_range_gt48'][1]:.4f}); above its null 95th at {len(sens_sum['rbf_x_layers_above_p95'])}/{len(rx)} layers; {rx_le4} of {K * len(rx)} observed fits chose a lambda below the old edge {min(rbf_lams):g}, {rx_edge} the new edge {min(rbf_lams_x):g}" + (" -- the new edge binds too, so these are still grid-limited." if rx_edge else "."))
    w(f"- (d), (e) Per-session-flip null: RBF above its 95th ({sens_sum['rbf_flip_p95_range'][0]:.4f}-{sens_sum['rbf_flip_p95_range'][1]:.4f}) at {len(sp_r_above)}/{len(sens3['rbf_sp'])} layers; MLP above its 95th ({sens_sum['mlp_flip_p95_range'][0]:.4f}-{sens_sum['mlp_flip_p95_range'][1]:.4f}) at {len(mlpsp_above)}/{len(sens3['mlp_sp'])} layers. Numerics: the observed labels as column 0 of the RBF flip batch reproduce (iii)'s RBF AUC exactly at every layer: {col0_eq}; MLP column 0 vs (iii)'s observed-alone AUC, max |diff| {mcol0:.3g}.")
    w("")
    w("## Figures as the block writes them")
    st200_read = [an["families"]["c1_read_M1M2"][str(l)]["shuffle95"] for l in STORED_LAYERS if l > LAYER]
    st200_a = [an["families"]["c1_label_a_M1M2"][str(l)]["shuffle95"] for l in STORED_LAYERS if l > LAYER]
    st200_b = [an["families"]["c1_label_b_M1M2"][str(l)]["shuffle95"] for l in STORED_LAYERS if l > LAYER]
    st200_all = [an["families"][n][str(l)]["shuffle95"] for n in M1M2 for l in STORED_LAYERS]
    st200_fam_all = {n: [an["families"][n][str(l)]["shuffle95"] for l in STORED_LAYERS] for n in M1M2}
    hi2 = {n: [(l, v) for l, v in zip(STORED_LAYERS, st200_fam_all[n]) if round(v, 2) > 0.59] for n in M1M2}
    r2 = lambda v: f"{v:.2f}".lstrip("0")   # noqa: E731
    w(f"- F1 (block :44, (i-b)) 'shuffle-95 null at ~.57-.59 across layers': the stored 200-draw 95th (stageC_analysis.json families.*.shuffle95, {RS} in STEP 0) over all 18 stored layers is read {min(st200_fam_all['c1_read_M1M2']):.4f}-{max(st200_fam_all['c1_read_M1M2']):.4f}, label_a {min(st200_fam_all['c1_label_a_M1M2']):.4f}-{max(st200_fam_all['c1_label_a_M1M2']):.4f}, label_b {min(st200_fam_all['c1_label_b_M1M2']):.4f}-{max(st200_fam_all['c1_label_b_M1M2']):.4f}; pooled {min(st200_all):.4f}-{max(st200_all):.4f}, i.e. {r2(min(st200_all))}-{r2(max(st200_all))} at two decimals; at L49-L63: read {min(st200_read):.4f}-{max(st200_read):.4f}, label_a {min(st200_a):.4f}-{max(st200_a):.4f}, label_b {min(st200_b):.4f}-{max(st200_b):.4f}. "
      f"Values that round above .59: " + "; ".join(f"{n.split('_M')[0][3:]} " + ", ".join(f"L{l} {v:.4f}" for l, v in hi2[n]) for n in M1M2 if hi2[n]) + ". "
      f"[status: discrepant (transcription) -- '~.57-.59' holds at two decimals for label_a only; read and label_b reach .60; the record's own prose says '.57-.60' (RESULTS.md@{PIN}:4402). F1 is not on this machine, so which series it plots is not checked here. Corrected value: ~.57-.60 (exact {min(st200_all):.3f}-{max(st200_all):.3f}).]")
    below_all = (all(part2["c1_read_M1M2"][str(l)]["auc_kfold"] < part2["c1_read_M1M2"][str(l)]["null200_p95"] for l in stored_layers)
                 and all(part2["c1_read_M1M2"][str(l)]["auc_kfold"] < part2["c1_read_M1M2"][str(l)]["null_p95"] for l in stored_layers))
    w(f"- The note's link-3 'below the shuffled-label 95th percentile of ~.58' (decision token): the read AUC is {'below its own 95th at every layer under both nulls' if below_all else 'NOT below its own 95th at every layer -- see the (ii) table'} (stored 200 draws, all 18 layers; {n_ext:,} draws at L{ext_layers[0]}-L{ext_layers[-1]}: {p2s['c1_read_M1M2']['p95_min']:.4f}-{p2s['c1_read_M1M2']['p95_max']:.4f}). The 95th is per layer, not one number: read family {min(st200_fam_all['c1_read_M1M2']):.3f}-{max(st200_fam_all['c1_read_M1M2']):.3f} (200 draws). [status: " + ("reproduced as a midpoint ('below' holds at every layer; '~.58' is a midpoint of a per-layer range)" if below_all else "discrepant") + "]")
    w(f"- N3(ii) 'extended only if cheap: 1,000 shuffles ... otherwise the stored 200-shuffle null stands and is cited as such': extended to {n_ext} draws at L{ext_layers[0]}-L{ext_layers[-1]} for c1_read_M1M2, c1_label_a_M1M2, c1_label_b_M1M2 ({n_ext:,}-draw 95th: read {p2s['c1_read_M1M2']['p95_min']:.4f}-{p2s['c1_read_M1M2']['p95_max']:.4f}, label_a {p2s['c1_label_a_M1M2']['p95_min']:.4f}-{p2s['c1_label_a_M1M2']['p95_max']:.4f}, label_b {p2s['c1_label_b_M1M2']['p95_min']:.4f}-{p2s['c1_label_b_M1M2']['p95_max']:.4f}) [status: computed-new]; the stored {n_stored}-draw null stands at " + ", ".join(f"L{l}" for l in stored_layers if l not in ext_layers) + f" [status: {RS}].")
    w(f"- N3(iv) 'the .50-.55' at the decision token, L44-L61: L49-L61 {min(aucs_hi):.4f}-{max(aucs_hi):.4f}; L44-L48 exactly 0.5 by construction. [status: {RS} at L44 and L48-L61 (stored c1_read_M1M2 auc_kfold); computed-new at L45-L47]")
    la_63 = [part2["c1_label_a_M1M2"][str(l)]["auc_kfold"] for l in stored_layers if l >= 51]
    lb_63 = [part2["c1_label_b_M1M2"][str(l)]["auc_kfold"] for l in stored_layers if l >= 51]
    w(f"- N3(i)/(i-b) cross-check from the arrays (the sibling item, `{SIBLING_RAW}`, reports these from the JSON): binding at the first label '>= .998, L51-L61' (block :43): label_a L51-L61 {p2s['c1_label_a_M1M2']['auc_min']:.4f}-{p2s['c1_label_a_M1M2']['auc_max']:.4f} [status: {RS}]; F1's '~1.0 from L51 on': L51-L63 {min(la_63):.4f}-{max(la_63):.4f} [status: {RS}].")
    lb_low = [f"L{l} {part2['c1_label_b_M1M2'][str(l)]['auc_kfold']:.4f}" for l in stored_layers
              if l >= 51 and l not in ext_layers
              and round(part2['c1_label_b_M1M2'][str(l)]['auc_kfold'], 2) < round(p2s['c1_label_b_M1M2']['auc_min'], 2)]
    w(f"- F1's '.81-.96 at the second label': label_b over L51-L63 {min(lb_63):.4f}-{max(lb_63):.4f} = {r2(min(lb_63))}-{r2(max(lb_63))} [status: {RS}, over L51-L63]; over L51-L61 it is {p2s['c1_label_b_M1M2']['auc_min']:.4f}-{p2s['c1_label_b_M1M2']['auc_max']:.4f} = {r2(p2s['c1_label_b_M1M2']['auc_min'])}-{r2(p2s['c1_label_b_M1M2']['auc_max'])}" + ("; the lower end over L51-L63 comes from " + ", ".join(lb_low) + " (outside L51-L61)." if lb_low else "."))
    w(f"- Positions 'nine positions before' (block :43) and seven for label_b: read minus label = {info['read_minus_label_a_tokens']} / {info['read_minus_label_b_tokens']} tokens in every session [status: {'reproduced' if dist_ok else 'discrepant'}, against stageC_analysis.json label_position_distance_to_read].")
    w(f"- N3(iii): MLP at the read L49-L63 {p3s['mlp_read_auc_range_gt48'][0]:.4f}-{p3s['mlp_read_auc_range_gt48'][1]:.4f}, RBF {p3s['rbf_read_auc_range_gt48'][0]:.4f}-{p3s['rbf_read_auc_range_gt48'][1]:.4f}; above own 95th: MLP {p3s['mlp_read_layers_above_p95'] or 'none'}, RBF {p3s['rbf_read_layers_above_p95'] or 'none'} (against the null maximum instead, see (iii)'s outcome line). [status: computed-new; magnitude specification-dependent, see (iii-s)]")
    w(f"- Log locators (prose only): Stage C entry RESULTS.md@{PIN}:4306 (header), :4312-:4313 ('.50-.55', '>= .998 ... L51-L61'), :4399 ('Grouped 10-fold statistic and 200-shuffle null as Stage B'), :4402 ('.50-.55 against nulls .57-.60'), :4404 (read-position table); stored raw `{STORED_RAW_REL}`.")
    w("")
    # ---------------- Values-check (pass 1 of the adversarial values-checker; dispositions by the fixer)
    rx_cmp = {l: (sens3["rbf_grid_x"][str(l)]["auc"], v) for l, v in CHECKER_RBFX.items() if str(l) in sens3["rbf_grid_x"]}
    rx_eq = sum(round(m_, 4) == v for m_, v in rx_cmp.values())
    adam_txt = ", ".join(f"L{l} {d['auc']:.4f}" for l, d in sens3["mlp_adam"].items())
    adj_txt = (f"{adj_max[2]:.4f} (L{adj_max[0]} to L{adj_max[1]})" if adj_max else "n/a")
    w("## Values-check")
    w("Pass 1 of the adversarial values-checker on the builder's outputs (script sha256 08134042...2c03, raw 2182f1f5...f8c6, JSON cd055583...179f): 166 claims checked, 11 findings, all minor. Every finding was judged correct; none is rejected. Dispositions:")
    w("1. [wall-clock] lines in the raw (rule 11 exempts only the stamp; the checker's re-run changed 8 of them, and the cost figure the builder's summary called computed-new did not reproduce) -- **fixed**: no timing line is in the raw any more; timing goes to stderr and to the JSON's `timing_nondeterministic`; the cost is now stated as a timing observation with both measurements (builder 11.83 null AUC/s, 76 min; checker 11.20, 80 min) and is not a figure. The header names the remaining run-dependent lines (stamp; HEAD, Command and Workers only if HEAD or the arguments change).")
    w("2. No status vocabulary in the raw -- **fixed**: every figure line and table carries reproduced / discrepant / computed-new (no figure in this raw is log-only or not found; the log locators are listed under Figures).")
    all_exc = (len(adam_above) == len(sens3["mlp_adam"]) and len(mlpsp_above) == len(sens3["mlp_sp"])
               and len(sp_r_above) == len(sens3["rbf_sp"]) and len(sens_sum["rbf_x_layers_above_p95"]) == len(rx))
    adam_differs = any(abs(sens3["mlp_adam"][str(l)]["auc"] - v) > 0.05 for l, v in CHECKER_ADAM.items() if str(l) in sens3["mlp_adam"])
    spec_vs_adam = max(abs(sens3["mlp_adam"][l]["auc"] - part3["mlp"]["read"][l]["auc"]) for l in sens3["mlp_adam"])
    verdict3 = ("So the checker's direction is confirmed: the level depends on the training specification (largest spec-vs-Adam difference here "
                f"{spec_vs_adam:.3f}), and the exceedance held in every check here (Adam, both per-session-flip nulls, the extended grid). "
                if all_exc else
                "The checker's direction on the level is confirmed (largest spec-vs-Adam difference here "
                f"{spec_vs_adam:.3f}), but the exceedance did NOT hold in every check here (see (iii-s)). ")
    verdict3 += ("Its three Adam values are not reproduced by this script's Adam, which differs from the checker's in details the checker did not state; they are quoted as the checker's. "
                 if adam_differs else "Its three Adam values agree with this script's within .05. ")
    w(f"3. MLP magnitude not robust to the optimizer (the checker's own Adam MLP: .7313 / .5844 / .5667 at L51 / L56 / L61) -- **fixed, with a correction**: (iii) now carries a magnitude line and (iii-s) computes it here. This script's Adam MLP ((iii-s)(b)) reads {adam_txt} (spec {', '.join(f'L{l} ' + format(part3['mlp']['read'][l]['auc'], '.4f') for l in sens3['mlp_adam'])}), above its own null 95th at {adam_above or 'no layer'}; the spec MLP over five seed pairs reads " + ", ".join(f"L{l} {sd_rng[l][0]:.3f}-{sd_rng[l][1]:.3f}" for l in sd_rng if int(l) in adam_layers) + ". " + verdict3 + "The raw now recommends quoting the exceedance, or the RBF figure with its grid caveat, rather than the MLP peak.")
    w(f"4. RBF lambda at the grid's lower edge -- **fixed**: (iii) states it ({p3s['rbf_read_obs_fits_at_grid_lower_edge']['n']}/{p3s['rbf_read_obs_fits_at_grid_lower_edge']['of']} informative observed fits at {min(rbf_lams):g}); a declared extended-grid re-run is (iii-s)(c): AUC {sens_sum['rbf_x_auc_range'][0]:.4f}-{sens_sum['rbf_x_auc_range'][1]:.4f}, above its null 95th at {len(sens_sum['rbf_x_layers_above_p95'])}/{len(rx)} layers, {rx_edge}/{K * len(rx)} fits at the new edge {min(rbf_lams_x):g}. The checker's extended-grid values (" + ", ".join(f"L{l} {v:.4f}" for l, v in CHECKER_RBFX.items()) + f") against this script's at 4 decimals: {rx_eq}/{len(rx_cmp)} equal (" + ", ".join(f"L{l} {m_:.4f}" for l, (m_, v) in rx_cmp.items()) + ").")
    w("5. POST-HOC 'no single linear functional can read pooled' (only one estimator was tested) -- **fixed**: reworded to what was tested (the stored linear probe does not read it pooled, with its AUC range), and the raw says no claim is made about other linear functionals.")
    w("6. Ledger 11 cited without a locator -- **fixed**: CLAUDE.md@bbc9ffe:311-312, quoted (checked with `git show bbc9ffe:CLAUDE.md`).")
    w(f"7. (iv) L45-L47 null statistics not re-derivable from the JSON -- **fixed**: `part_iv.per_layer.{{45,46,47}}.null` hold the {n_stored} draws (full float64); the other sweep layers carry `null_in`, a pointer to `part_ii`.")
    w(f"8. F1 '~.57-.59' labelled reproduced in the builder's summary -- **fixed**: the raw's Figures line now reads discrepant (transcription): the stored 95th is {min(st200_all):.4f}-{max(st200_all):.4f} (.57-.60 at two decimals; '.57-.59' holds for label_a only); corrected value ~.57-.60, as the record's own prose (RESULTS.md@{PIN}:4402). The fixer's return relabels the summary row.")
    w(f"9. label_b '.81-.96' printed beside the L51-L61 range -- **fixed**: the Figures line gives {r2(min(lb_63))}-{r2(max(lb_63))} over L51-L63 ({min(lb_63):.4f}-{max(lb_63):.4f}) and {r2(p2s['c1_label_b_M1M2']['auc_min'])}-{r2(p2s['c1_label_b_M1M2']['auc_max'])} over L51-L61, and names the layers the lower end comes from.")
    w(f"10. 'adjacent layers agree' not computed -- **fixed**: replaced by the computed largest adjacent difference over L49-L61, {adj_txt}.")
    w(f"11. The N3 split across two raws not recorded as a referent note -- **fixed**: header line naming `{SIBLING_RAW}` for (i), (i-b), (v) and this raw for (ii)-(iv).")
    w("Fixer's own corrections and additions (not checker findings): (a) the builder's raw said 'The block allows vectorizing the shuffles only if it is numerically the same estimator'; the block says no such thing (:45 asks only for 'the same grouped CV'), so the sentence now states it as Code's standard; (b) the imported record modules' working-tree sha256s are now checked against the pin (Inputs); (c) the per-session label-flip nulls in (iii-s)(d)-(e) were added because the record's all-rows permutation does not keep the target's one-positive-one-negative-per-session structure (disclosed in (ii)); the values-checker had run such a null independently, and its values are not quoted here.")
    w("")
    w(f"Round 2 of the values-checker on round 1's outputs (script sha256 {R1['script'][:8]}...{R1['script'][-4:]}, raw {R1['raw'][:8]}...{R1['raw'][-4:]}, JSON {R1['json'][:8]}...{R1['json'][-4:]}): four findings, all minor, none substantive; no STOP. All four judged correct and applied; none rejected. The checker also reports, from its own code, an isotropic-init MLP (not the item's spec) at " + ", ".join(f"L{l} {v:.4f}" for l, v in CHECKER2_ISO_MLP.items()) + " against the spec's " + ", ".join(f"L{l} {part3['mlp']['read'][str(l)]['auc']:.4f}" for l in CHECKER2_ISO_MLP) + " (its values, quoted, not recomputed here). Dispositions:")
    med_half = [(l, float(np.median(d["best_epoch_per_fold"]))) for l, d in mr_hi if float(np.median(d["best_epoch_per_fold"])) % 1]
    null_int = all(float(d["null_median_best_epoch"]) % 1 == 0 for _, d in mr_hi)
    w(f"R2-1. Early-stopping medians truncated by int() -- **fixed**: {len(med_half)} of the {len(mr_hi)} observed-fit medians are half-integers and had been printed truncated (" + ", ".join(f"L{l} {m:.1f} printed {int(m)}" for l, m in med_half) + "); the line now prints every median with one decimal from the JSON's best_epoch_per_fold and says what a .5 is. The null fits' medians " + ("are all integers here; they" if null_int else "") + " now use one decimal too, so no rounding can hide a .5. [status of the medians: computed-new]")
    w(f"R2-2. The outcome line did not say that 'permutation ceiling' (:50) was read as the 95th -- **fixed**: it now says so, citing :46, and gives the null-maximum reading computed from the JSON's null_max fields: both classifiers above it at {len(mx_both)}/{len(rd_hi['mlp'])} informative layers ({_runs(mx_both)}); MLP also at " + (_runs([l for l in mx_in['mlp'] if l not in mx_both]) if [l for l in mx_in['mlp'] if l not in mx_both] else "no other layer") + ", RBF also at " + (_runs([l for l in mx_in['rbf'] if l not in mx_both]) if [l for l in mx_in['rbf'] if l not in mx_both] else "no other layer") + "; not at " + (mx_out_txt or "any layer") + f". The count at the 95th is unchanged (MLP {len(p3s['mlp_read_layers_above_p95'])}/{len(mr_hi)}, RBF {len(p3s['rbf_read_layers_above_p95'])}/{len(mr_hi)}); both readings are stated, and which one :50 means is the design seat's.")
    w(f"R2-3. The outcome line did not point to the one-estimator caveat -- **fixed**: it now says (ii)/(iv) tested one linear estimator, and quotes from the POST-HOC section, labelled post-hoc, that estimator's first-round-sign read ({min(frs_):.3f}-{max(frs_):.3f}) and within-subgroup target read ({sub_lo_:.3f}-{sub_hi_:.3f}) at L51-L61. The block's rule (:50) was already followed; this is the cross-reference only.")
    w("R2-4. The docstring still named [wall-clock] lines that no longer exist -- **fixed**: it states the run-dependent lines as the raw's header does (stamp; HEAD, Command and Workers only if HEAD or the arguments change; timing to stderr and to the JSON's timing_nondeterministic), and documents --render-only.")
    w(f"How round 2's raw was produced: by `--render-only` from round 1's JSON, with no fit re-run and the JSON not rewritten (sha256 unchanged, {R1['json'][:8]}...{R1['json'][-4:]}). The script's report code was moved into `render(o, rt)` with its output text unchanged; render() reads only the JSON dict (plus the stored analysis at the pin, the pin's block hash, the BLAS name and the record-module hashes); the compute path now writes the JSON first and renders the raw from json.loads of that same text, and `--render-only` renders the raw from the JSON file. "
      f"Before any round-2 text edit, that refactor (script sha256 {STEP1_SCRIPT[:8]}...{STEP1_SCRIPT[-4:]}) was checked four ways: (1) `--render-only` on round 1's JSON wrote a file byte-identical to round 1's raw ({R1['raw'][:8]}...{R1['raw'][-4:]}); (2) `--render-only` on round 1's 40-session smoke JSON ({R1['smoke_json'][:8]}...{R1['smoke_json'][-4:]}) reproduced round 1's smoke raw ({R1['smoke_raw'][:8]}...{R1['smoke_raw'][-4:]}) byte for byte; (3) the refactored compute path in --smoke mode wrote a raw that differs from round 1's smoke raw only in the stamp, Script and Command lines, and a JSON that differs from round 1's smoke JSON only in code_stamp, command, script_sha256 and timing_nondeterministic; (4) `--render-only` on that new smoke JSON reproduced its own compute-path raw byte for byte. After the round-2 edits, checks (3) and (4) were repeated with round 2's final script (sha256 {R2['script'][:8]}...{R2['script'][-4:]}): a fresh --smoke run wrote a JSON that differs from check (3)'s smoke JSON only in code_stamp, command, script_sha256 and timing_nondeterministic, and a raw that differs from that script's `--render-only` render of check (3)'s smoke JSON only in the stamp, Script and Command lines and the Rendered line; `--render-only` on the fresh smoke JSON reproduces the fresh raw apart from the Rendered line. "
      "The diff from that pre-edit render to round 2's raw is exactly the round-2 edits: the Rendered line, the (iii) disclosure's round-2 sentence, the outcome line's three added sentences (two for R2-2, one for R2-3), the early-stopping line, the Figures pointer in N3(iii), and this round-2 section.")
    # ---------------- Round 4: dispositions of pass 3 (round 3) of the values-checker
    an_pin = info["inputs"][ANALYSIS_REL]["sha256_at_pin"]
    w("")
    w(f"Round 4: dispositions of pass 3 of the values-checker (round 3: a strict, independent checker that edited nothing) on round 2's outputs (script sha256 {R2['script'][:8]}...{R2['script'][-4:]}, raw {R2['raw'][:8]}...{R2['raw'][-4:]}, JSON {R2['json'][:8]}...{R2['json'][-4:]}): two findings, both minor, none substantive; no STOP is declared and the checker found none licensed (block :50 makes only (i) not reproducing a STOP on link 3, and (i) is in `{SIBLING_RAW}`). Both judged correct and applied; none rejected. "
      f"The checker also re-ran round 2's compute path in full into scratch; Code's own leaf-by-leaf comparison of that re-run's JSON (sha256 {V3_RERUN['json'][:8]}...{V3_RERUN['json'][-4:]}) with this JSON finds {V3_RERUN['leaf_diffs']} leaf differences, all under " + ", ".join(V3_RERUN['diff_keys'][:-1]) + " and " + V3_RERUN['diff_keys'][-1] + ". Dispositions:")
    w(f"R4-1. The Rendered line said every figure below is read from the JSON by render(), and its 'Evaluated at this render' list left out the stored analysis, which render() also reads at the pin (`git show {PIN}:{ANALYSIS_REL}`, sha256 {an_pin[:8]}...{an_pin[-4:]}): its `label_position_distance_to_read` feeds the label-distance check (Inputs; and the Figures line on 'nine positions before'), and its `families.*.shuffle95` the stored 200-draw 95th (Figures: the F1 line and the link-3 line; Values-check item 8) -- **fixed**: the line now says 'read from that JSON or from that pinned stored analysis' and lists the pinned stored analysis among the inputs evaluated at this render. "
      f"No number changes: the pinned blob cannot change, and STEP 0 shows the stored shuffle95 / shuffle_mean / shuffle_max equal to the first-200 statistics recomputed into the JSON (max |diff| = {md_s:g}).")
    w("R4-2. Round 2's paragraph counted 'the outcome line's two added sentences'; round 2 appended three to the end of round 1's outcome line (two for R2-2: the 95th-percentile reading of 'permutation ceiling' and the null-maximum reading; one for R2-3: the one-estimator cross-reference) -- **fixed in place**: that paragraph now says 'three added sentences (two for R2-2, one for R2-3)'. "
      f"Code's line diff of round 1's raw ({R1['raw'][:8]}...{R1['raw'][-4:]}, 328 lines) against round 2's ({R2['raw'][:8]}...{R2['raw'][-4:]}, 336 lines) confirms the rest of that paragraph's list: line 10 inserted; lines 176, 205 (the outcome line, a pure append to round 1's line), 208 and 313 replaced; lines 330-336 (the round-2 section, its opening blank line included) appended; nothing else.")
    w(f"Code's own corrections (not checker findings): (a) round 2's paragraph said its repeated checks used 'the final script (the one the Rendered line names)'; after this re-render the Rendered line names round 4's script, so that paragraph now names round 2's final script by its hash ({R2['script'][:8]}...{R2['script'][-4:]}) and reads 'that script's' render where it read 'this script's'; (b) the (iii) disclosure, which lists every inspection of outputs after the (iii) hyperparameters were fixed, now records round 3 (pass 3's full re-run and its own re-implementations) as changing report text only.")
    w(f"How round 4's raw was produced: by `--render-only` from the same JSON (sha256 unchanged, {R2['json'][:8]}...{R2['json'][-4:]}), with no fit re-run and the JSON not rewritten. The diff from round 2's raw to this raw is exactly the round-4 edits: the Rendered line (its stamp and rendering-script hash, and R4-1's two changes), the (iii) disclosure's round-3 sentence (Code's (b)), round 2's paragraph (R4-2's count; Code's (a)), and this round-4 section. "
      f"With this script, `render()` on the checker's re-run JSON without the render-only provenance (as the compute path calls it) differs from the checker's compute-path raw (sha256 {V3_RERUN['raw'][:8]}...{V3_RERUN['raw'][-4:]}, rendered by round 2's script) only in the (iii) disclosure's round-3 sentence, round 2's paragraph (R4-2; Code's (a)) and this round-4 section.")
    return "\n".join(L) + "\n"


def _runs(ls):
    """Layer list as runs of consecutive layers: [49, 51, 52, 53] -> 'L49, L51-L53'."""
    out, ls = [], sorted(ls)
    i = 0
    while i < len(ls):
        j = i
        while j + 1 < len(ls) and ls[j + 1] == ls[j] + 1:
            j += 1
        out.append(f"L{ls[i]}" if i == j else f"L{ls[i]}-L{ls[j]}")
        i = j + 1
    return ", ".join(out) if out else "none"


def runtime_facts(an, mod_hashes):
    """The facts render() takes from the environment rather than the JSON."""
    return {"an": an, "block_sha_pin": sha256_bytes(git_blob(BLOCK)), "mod_hashes": mod_hashes,
            "blas": np.show_config(mode="dicts")["Build Dependencies"]["blas"]["name"]}


def record_module_hashes():
    return {rel: {"wt": sha256_file(os.path.join(REPO, rel)), "pin": sha256_bytes(git_blob(rel))}
            for rel in ("valence_core/echo/probe.py", "valence_core/discrim.py",
                        "valence_core/adapters/base.py")}


def render_only(args):
    """--render-only: rebuild the raw from the JSON at --json-out with render(); no arrays,
    no fits; the JSON is read, never written."""
    src = os.path.abspath(args.json_out)
    with open(src, "rb") as f:
        jb = f.read()
    o = json.loads(jb)
    out_md = os.path.abspath(args.out)
    if o["smoke"] and out_md == OUT_MD:
        raise SystemExit("a smoke JSON is never rendered into the default results/raw output; pass --out")
    rt = runtime_facts(json.loads(git_blob(ANALYSIS_REL)), record_module_hashes())
    rel = os.path.relpath(src, REPO)
    rt["render"] = {"stamp": sh("date", "-u").strip(), "head": sh("git", "-C", REPO, "rev-parse", "HEAD").strip(),
                    "script_sha": sha256_file(os.path.abspath(__file__)), "cmd": " ".join([sys.executable] + sys.argv),
                    "json_rel": src if rel.startswith("..") else rel, "json_sha": sha256_bytes(jb)}
    text = render(o, rt)
    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_md, "w") as f:
        f.write(text)
    print(text)
    return 0


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=OUT_MD)
    ap.add_argument("--json-out", default=OUT_JSON)
    ap.add_argument("--workers", type=int, default=WORKERS)
    ap.add_argument("--smoke", action="store_true",
                    help="pipeline smoke: 40 sessions, 3 layers, 20 draws; refuses the default outputs")
    ap.add_argument("--render-only", action="store_true",
                    help="rebuild --out from the existing JSON at --json-out with the same render() the "
                         "compute path uses; no arrays, no fits; the JSON is read, never written")
    args = ap.parse_args()
    if args.render_only:
        if args.smoke:
            raise SystemExit("--render-only takes no --smoke (the JSON says whether it was a smoke run)")
        return render_only(args)
    if args.workers > 8:
        raise SystemExit("at most 8 worker processes")
    out_md, out_json = os.path.abspath(args.out), os.path.abspath(args.json_out)
    if args.smoke and (out_md == OUT_MD or out_json == OUT_JSON):
        raise SystemExit("--smoke refuses the default results/raw outputs; pass --out/--json-out")
    stored_layers = [44, 51, 56] if args.smoke else STORED_LAYERS
    ext_layers = [51, 56] if args.smoke else EXT_LAYERS
    sweep_layers = [44, 45, 51, 56] if args.smoke else SWEEP_LAYERS
    n_ext, n_stored = (20, 20) if args.smoke else (N_EXT, N_STORED)
    n_mlp, n_rbf = (10, 20) if args.smoke else (N_MLP_NULL, N_RBF_NULL)
    chunk = 10 if args.smoke else CHUNK

    T0 = time.time(); wall = {}
    stamp = sh("date", "-u").strip()
    head = sh("git", "-C", REPO, "rev-parse", "HEAD").strip()
    block_sha_wt = sha256_file(os.path.join(REPO, BLOCK))
    script_sha = sha256_file(os.path.abspath(__file__))
    cmd = " ".join([sys.executable] + sys.argv)
    mod_hashes = record_module_hashes()

    # ---------------- load
    t = time.time()
    data, info = load(None, args.smoke)
    an = data["an"]
    wall["load_and_checks"] = time.time() - t
    assert list(an["families"].keys())[:9] == C1_ORDER, "family order differs from analyze_c"
    assert an["probe_layers"] == STORED_LAYERS and an["n_shuffles"] == 200 and an["kfold"] == K

    # ---------------- pool: STEP 0 + (ii) + (iv), record functions only
    t = time.time()
    jobs, plan = [], {"perm": {}}
    perms = {}
    for name in M1M2:
        fs = fold_seed(name)
        lays = sorted(set(stored_layers) | (set(sweep_layers) if name == "c1_read_M1M2" else set()))
        for l in lays:
            X, y, g = family(data, name, l)
            n = n_ext if l in ext_layers else n_stored
            Y = perm_stream(y, fs + l, n)
            perms[(name, l)] = n
            for s0 in range(0, n, chunk):
                jobs.append(("perm", name, l, X, Y[:, s0:s0 + chunk], g, fs, s0))
    # one direct call of the record's kfold_shuffle_null (elementwise identity of the chunked path)
    Xr, yr, gr = family(data, "c1_read_M1M2", 51)
    jobs.append(("record_null", "c1_read_M1M2", 51, Xr, yr, gr, fold_seed("c1_read_M1M2"), n_stored))
    for name in C1_ORDER:
        lays = sorted(set(stored_layers) | (set(sweep_layers) if name == "c1_read_M1M2" else set()))
        for l in lays:
            X, y, g = family(data, name, l)
            jobs.append(("kfold", name, l, X, y, g, fold_seed(name), name in M1M2))
    os.environ["VECLIB_MAXIMUM_THREADS"] = "1"       # workers: single-threaded BLAS (spawned after this line)
    res_k, res_null, rec_null, job_secs = {}, {}, None, {"perm": 0.0, "kfold": 0.0, "record_null": 0.0}
    n_auc_perm = 0
    with ProcessPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(_job, j) for j in jobs]
        # (iii) runs in the main process (its own BLAS threads) while the pool works
        t3 = time.time()
        part3 = run_nonlinear(data, stored_layers, n_mlp, n_rbf)
        wall["nonlinear_concurrent_with_pool"] = time.time() - t3
        t3 = time.time()
        inf_layers = [l for l in stored_layers if l > LAYER]
        sens3 = run_sensitivity(data, part3, inf_layers,
                                [51] if args.smoke else list(ADAM_LAYERS),
                                5 if args.smoke else N_ADAM_NULL,
                                10 if args.smoke else N_SP_MLP,
                                20 if args.smoke else N_SP_RBF,
                                (1,) if args.smoke else SEED_OFFSETS)
        wall["sensitivity_iii_concurrent_with_pool"] = time.time() - t3
        for fu in futs:
            kind, name, l, s0, out, secs = fu.result()
            job_secs[kind] += secs
            if kind == "kfold":
                res_k[(name, l)] = out
            elif kind == "perm":
                res_null.setdefault((name, l), {})[s0] = out
                n_auc_perm += len(out)
            else:
                rec_null = out
    os.environ.pop("VECLIB_MAXIMUM_THREADS", None)
    nulls = {key: np.array([v for s0 in sorted(d) for v in d[s0]]) for key, d in res_null.items()}
    wall["pool_linear_including_concurrent_nonlinear"] = time.time() - t
    throughput = n_auc_perm / wall["pool_linear_including_concurrent_nonlinear"]

    # ---------------- STEP 0 comparison
    step0 = {"auc_kfold": {}, "auc_loso": {}, "shuffle": {}}
    md_k = md_l = md_s = 0.0
    for name in C1_ORDER:
        for l in stored_layers:
            stv = an["families"][name][str(l)]
            dk = abs(res_k[(name, l)]["auc_kfold"] - stv["auc_kfold"])
            step0["auc_kfold"].setdefault(name, {})[str(l)] = {"reproduced": res_k[(name, l)]["auc_kfold"],
                                                               "stored": stv["auc_kfold"], "absdiff": dk}
            md_k = max(md_k, dk)
            if res_k[(name, l)]["auc_loso"] is not None:
                dl = abs(res_k[(name, l)]["auc_loso"] - stv["auc_loso"])
                step0["auc_loso"].setdefault(name, {})[str(l)] = {"reproduced": res_k[(name, l)]["auc_loso"],
                                                                  "stored": stv["auc_loso"], "absdiff": dl}
                md_l = max(md_l, dl)
        if name in M1M2:
            for l in stored_layers:
                stv = an["families"][name][str(l)]
                n200 = nulls[(name, l)][:200]
                d = {"shuffle95": (float(np.percentile(n200, 95)), stv["shuffle95"]),
                     "shuffle_mean": (float(np.mean(n200)), stv["shuffle_mean"]),
                     "shuffle_max": (float(np.max(n200)), stv["shuffle_max"])}
                step0["shuffle"].setdefault(name, {})[str(l)] = {kk: {"reproduced": a, "stored": b, "absdiff": abs(a - b)}
                                                                 for kk, (a, b) in d.items()}
                md_s = max(md_s, *[abs(a - b) for a, b in d.values()])
    rec_vs_chunk = float(np.max(np.abs(np.array(rec_null) - nulls[("c1_read_M1M2", 51)][:len(rec_null)])))
    TOL = 1e-12
    step0_pass = (md_k <= TOL and md_l <= TOL and (md_s <= TOL or args.smoke) and rec_vs_chunk == 0.0)
    step0["max_absdiff"] = {"auc_kfold": md_k, "auc_loso": md_l, "shuffle_stats_first200": md_s,
                            "record_kfold_shuffle_null_vs_chunked_L51_read": rec_vs_chunk}
    step0["tolerance"] = TOL
    step0["pass"] = bool(step0_pass)

    # ---------------- sensitivity of the record's estimator to summation order (why (ii) is not vectorized)
    t = time.time()
    sens = {}
    for name, l in SENS_CASES:
        if l not in stored_layers:
            continue
        X, y, g = family(data, name, l)
        fs = fold_seed(name)
        Y = np.concatenate([y[:, None], perm_stream(y, fs + l, 5)], axis=1)
        sc = kfold_scores_batched(X, Y, g, fs)
        ab = auc_cols(sc, Y)
        rec5 = nulls[(name, l)][:5]
        sens[f"{name}@L{l}"] = {"batched_obs": float(ab[0]), "record_obs": res_k[(name, l)]["auc_kfold"],
                                "batched_first5": r8(ab[1:]), "record_first5": r8(rec5),
                                "max_absdiff_first5": float(np.max(np.abs(ab[1:] - rec5))),
                                "obs_max_abs_score_diff": float(np.max(np.abs(sc[:, 0] - PR.kfold_scores(X, y, g, K, fs))))}
    stab = {}
    for name in M1M2:
        for l in stored_layers:
            X, y, g = family(data, name, l)
            stab.setdefault(name, {})[str(l)] = gd_stability_ratio(X, g, fold_seed(name))
    wall["sensitivity_and_stability"] = time.time() - t

    # ---------------- (ii) table
    part2 = {}
    for name in M1M2:
        for l in stored_layers:
            obs = res_k[(name, l)]["auc_kfold"]
            nl = nulls[(name, l)]
            part2.setdefault(name, {})[str(l)] = {
                "auc_kfold": obs, "auc_loso": res_k[(name, l)]["auc_loso"], "n_null": int(len(nl)),
                "null_mean": float(np.mean(nl)), "null_p95": float(np.percentile(nl, 95)),
                "null_max": float(np.max(nl)), "perm_p": perm_p(obs, nl),
                "null200_p95": float(np.percentile(nl[:200], 95)), "null200_mean": float(np.mean(nl[:200])),
                "extended": l in ext_layers, "null": [float(v) for v in nl]}

    # ---------------- (iv) sweep at the read position
    part4 = {}
    for l in sweep_layers:
        obs = res_k[("c1_read_M1M2", l)]["auc_kfold"]
        nl = nulls[("c1_read_M1M2", l)]
        part4[str(l)] = {"auc_kfold": obs, "auc_loso": res_k[("c1_read_M1M2", l)]["auc_loso"],
                         "n_null": int(len(nl)), "null_mean": float(np.mean(nl)),
                         "null_p95": float(np.percentile(nl, 95)), "perm_p": perm_p(obs, nl),
                         "null200_p95": float(np.percentile(nl[:200], 95)),
                         "in_stored_analysis": l in STORED_LAYERS, "le48_by_construction": l <= LAYER}
        if l in stored_layers:
            part4[str(l)]["null_in"] = f"part_ii.families.c1_read_M1M2.{l}.null"
        else:
            part4[str(l)]["null"] = [float(v) for v in nl]

    wall["total"] = time.time() - T0

    # ---------------- summaries (computed here, stored in the JSON; render() reads them back from it)
    p2s = {}
    for name in M1M2:
        rows = [part2[name][str(l)] for l in ext_layers]
        p2s[name] = {"auc_min": min(r["auc_kfold"] for r in rows), "auc_max": max(r["auc_kfold"] for r in rows),
                     "null_mean_min": min(r["null_mean"] for r in rows), "null_mean_max": max(r["null_mean"] for r in rows),
                     "p95_min": min(r["null_p95"] for r in rows), "p95_max": max(r["null_p95"] for r in rows),
                     "p_min": min(r["perm_p"] for r in rows), "p_max": max(r["perm_p"] for r in rows),
                     "n_layers_above_p95": sum(r["auc_kfold"] > r["null_p95"] for r in rows), "n_layers": len(rows)}
    hi = [l for l in sweep_layers if l > LAYER]
    aucs_hi = [part4[str(l)]["auc_kfold"] for l in hi]
    le_vals = sorted({part4[str(l)]["auc_kfold"] for l in sweep_layers if l <= LAYER})
    above = [l for l in hi if part4[str(l)]["auc_kfold"] > part4[str(l)]["null_p95"]]
    p_lt05 = [l for l in hi if part4[str(l)]["perm_p"] < 0.05]
    lmax = hi[int(np.argmax(aucs_hi))]
    part4_summary = {"auc_min_L49_61": min(aucs_hi), "auc_max_L49_61": max(aucs_hi), "argmax_layer": lmax,
                     "auc_values_le48": le_vals, "layers_above_p95": above, "layers_p_lt_05": p_lt05,
                     "auc_min_L51_61": min(part4[str(l)]["auc_kfold"] for l in hi if l >= 51),
                     "auc_max_L51_61": max(part4[str(l)]["auc_kfold"] for l in hi if l >= 51)}
    adj = [(hi[i], hi[i + 1], abs(aucs_hi[i + 1] - aucs_hi[i])) for i in range(len(hi) - 1) if hi[i + 1] == hi[i] + 1]
    adj_max = max(adj, key=lambda x: x[2]) if adj else None
    part4_summary["max_adjacent_abs_diff_L49_61"] = ({"from": adj_max[0], "to": adj_max[1], "absdiff": adj_max[2]}
                                                     if adj_max else None)
    # ---------------- POST-HOC (descriptive): composition of the read-position target
    t = time.time()
    sess = data["sess"]
    a_is_r1 = np.array([1 if r["menu_a"] == r["spans"][0]["tag"] else 0 for r in sess])
    start_plus = np.array([1 if r["start_plus"] else 0 for r in sess])
    ident_ok = bool(np.all(data["a_is_plus"] == (a_is_r1 == start_plus).astype(int)))
    sp_ok = bool(all(bool(r["start_plus"]) == (r["spans"][0]["tag"] == r["tag_plus"]) for r in sess))
    ph = {}
    fs_read = fold_seed("c1_read_M1M2")
    for l in [x for x in stored_layers if x > LAYER]:
        li = KEEP_LAYERS.index(l)
        M1r, M2r = data["stacks"]["M1|state"][:, 0, li], data["stacks"]["M2|state"][:, 0, li]
        row = {}
        for key_, sel in (("label_a_is_round1_tag", a_is_r1 == 1), ("label_a_is_not_round1_tag", a_is_r1 == 0)):
            Xs = np.concatenate([M1r[sel], M2r[sel]])
            ys = np.r_[data["a_is_plus"][sel], 1 - data["a_is_plus"][sel]]
            gs = np.r_[data["groups"][sel], data["groups"][sel]]
            row[key_] = {"n_sessions": int(sel.sum()), "auc_kfold": PR.kfold_auc(Xs, ys, gs, K, fs_read)}
        Xa = np.concatenate([M1r, M2r])
        row["first_round_sign_all"] = {"n_sessions": int(len(sess)),
                                       "auc_kfold": PR.kfold_auc(Xa, np.r_[start_plus, 1 - start_plus],
                                                                 np.r_[data["groups"], data["groups"]], K, fs_read)}
        ph[str(l)] = row
    wall["posthoc"] = time.time() - t
    # ---------------- (iii) summaries
    mr = [part3["mlp"]["read"][str(l)] for l in stored_layers]
    rr = [part3["rbf"]["read"][str(l)] for l in stored_layers]
    mr_hi = [(l, part3["mlp"]["read"][str(l)]) for l in stored_layers if l > LAYER]
    rr_hi = [(l, part3["rbf"]["read"][str(l)]) for l in stored_layers if l > LAYER]
    p3s = {
        "mlp_read_auc_range_gt48": [min(d["auc"] for _, d in mr_hi), max(d["auc"] for _, d in mr_hi)],
        "mlp_read_layers_above_p95": [l for l, d in mr_hi if d["above_p95"]],
        "mlp_read_layers_p_lt_05": [l for l, d in mr_hi if d["perm_p"] < 0.05],
        "mlp_read_p95_range_gt48": [min(d["null_p95"] for _, d in mr_hi), max(d["null_p95"] for _, d in mr_hi)],
        "rbf_read_auc_range_gt48": [min(d["auc"] for _, d in rr_hi), max(d["auc"] for _, d in rr_hi)],
        "rbf_read_layers_above_p95": [l for l, d in rr_hi if d["above_p95"]],
        "rbf_read_layers_p_lt_05": [l for l, d in rr_hi if d["perm_p"] < 0.05],
        "rbf_read_p95_range_gt48": [min(d["null_p95"] for _, d in rr_hi), max(d["null_p95"] for _, d in rr_hi)],
        "mlp_le48_auc": sorted({d["auc"] for l, d in zip(stored_layers, mr) if l <= LAYER}),
        "rbf_le48_auc": sorted({d["auc"] for l, d in zip(stored_layers, rr) if l <= LAYER}),
    }
    lam_edge = [(l, sum(x == min(RBF_LAMS) for x in d["lambda_obs_per_fold"])) for l, d in rr_hi]
    p3s["rbf_read_obs_fits_at_grid_lower_edge"] = {"n": sum(c for _, c in lam_edge), "of": K * len(rr_hi),
                                                   "lower_edge": min(RBF_LAMS)}
    pc_layers = [l for l in stored_layers if 51 <= l <= 61]
    pc = {"mlp_min_L51_61": min(part3["mlp"]["label_a"][str(l)]["auc"] for l in pc_layers),
          "rbf_min_L51_61": min(part3["rbf"]["label_a"][str(l)]["auc"] for l in pc_layers)}
    pc["mlp_pass"] = pc["mlp_min_L51_61"] >= POSCTRL_BAR
    pc["rbf_pass"] = pc["rbf_min_L51_61"] >= POSCTRL_BAR
    # ---------------- (iii-s) summaries
    sd_rng = {l: [min([part3["mlp"]["read"][l]["auc"]] + [v["auc"] for v in sens3["mlp_seeds"][l].values()]),
                  max([part3["mlp"]["read"][l]["auc"]] + [v["auc"] for v in sens3["mlp_seeds"][l].values()])]
              for l in sens3["mlp_seeds"]}
    adam_above = [int(l) for l, d in sens3["mlp_adam"].items() if d["above_p95"]]
    mlpsp_above = [int(l) for l, d in sens3["mlp_sp"].items() if d["above_p95"]]
    rx = sens3["rbf_grid_x"]
    rx_edge = sum(sum(x == min(RBF_LAMS_X) for x in d["lambda_obs_per_fold"]) for d in rx.values())
    rx_le4 = sum(sum(x < min(RBF_LAMS) for x in d["lambda_obs_per_fold"]) for d in rx.values())
    sp_r_above = [int(l) for l, d in sens3["rbf_sp"].items() if d["above_p95"]]
    col0_eq = all(abs(d["obs_as_column0_auc"] - d["auc"]) == 0 for d in sens3["rbf_sp"].values())
    mcol0 = max(abs(d["obs_as_column0_auc"] - d["auc"]) for d in sens3["mlp_sp"].values())
    sens_sum = {
        "mlp_seed_range_per_layer": sd_rng,
        "adam_auc": {l: d["auc"] for l, d in sens3["mlp_adam"].items()},
        "adam_layers_above_p95": adam_above,
        "rbf_x_auc_range": [min(d["auc"] for d in rx.values()), max(d["auc"] for d in rx.values())],
        "rbf_x_layers_above_p95": [int(l) for l, d in rx.items() if d["above_p95"]],
        "rbf_x_obs_fits_below_old_edge": {"n": rx_le4, "of": K * len(rx)},
        "rbf_x_obs_fits_at_new_edge": {"n": rx_edge, "of": K * len(rx)},
        "rbf_flip_layers_above_p95": sp_r_above, "mlp_flip_layers_above_p95": mlpsp_above,
        "rbf_flip_p95_range": [min(d["null_p95"] for d in sens3["rbf_sp"].values()), max(d["null_p95"] for d in sens3["rbf_sp"].values())],
        "mlp_flip_p95_range": [min(d["null_p95"] for d in sens3["mlp_sp"].values()), max(d["null_p95"] for d in sens3["mlp_sp"].values())],
        "rbf_flip_obs_column0_equal": col0_eq, "mlp_flip_obs_column0_max_abs_auc_diff": mcol0}

    # ---------------- write: the JSON first, then the raw rendered from that JSON's text
    out = {"title": TITLE, "code_stamp": stamp, "head_at_run": head, "pin": PIN_FULL, "block": BLOCK,
           "block_sha256": block_sha_wt, "script": SCRIPT_REL, "script_sha256": script_sha,
           "interpreter": sys.executable, "python": platform.python_version(), "numpy": np.__version__,
           "command": cmd, "smoke": args.smoke, "workers": args.workers,
           "inputs": info, "procedure_of_record": {
               "fit_lr": {"seed": PR.LR_SEED, "iters": PR.LR_ITERS, "rate": PR.LR_RATE, "l2": PR.LR_L2,
                          "standardize": "fit rows, sd + 1e-6"},
               "kfold": K, "fold_seeds": {n: fold_seed(n) for n in C1_ORDER}, "perm_seed": "fold seed + layer",
               "permutation": "across all rows (probe.kfold_shuffle_null)", "auc": "discrim.auc_from_scores"},
           "step0": step0, "linear_estimator_sensitivity": sens, "gd_stability_ratio_max_over_folds": stab,
           "part_ii": {"n_ext": n_ext, "ext_layers": ext_layers, "n_stored": n_stored, "families": part2,
                       "summary_L51_61": p2s},
           "part_iv": {"layers": sweep_layers, "per_layer": part4, "summary": part4_summary},
           "part_iii": {"mlp_config": {**MLP, "val_frac": MLP_VAL_FRAC, "split_seed": MLP_SPLIT_SEED,
                                       "init_seed": MLP_INIT_SEED, "n_null": n_mlp},
                        "rbf_config": {"lambdas": list(RBF_LAMS), "inner_k": RBF_INNER_K,
                                       "inner_seed": RBF_INNER_SEED, "gamma": "1/median squared distance, training pairs",
                                       "n_null": n_rbf},
                        "positive_control_bar": POSCTRL_BAR, "results": part3, "summary": p3s,
                        "positive_control": pc},
           "posthoc_composition": {"label": "POST-HOC, descriptive, CLAUDE.md ledger 11; not asked by the block",
                                   "identity_holds": ident_ok, "start_plus_consistent": sp_ok,
                                   "n_label_a_is_round1_tag": int(a_is_r1.sum()), "per_layer": ph},
           "part_iii_s": {"label": "POST-HOC sensitivity of (iii), added by the values-check fix; descriptive; changes no (iii) figure",
                          "mlp_adam_config": MLP_ADAM, "seed_offsets": list(SEED_OFFSETS) if not args.smoke else [1],
                          "rbf_lambdas_extended": list(RBF_LAMS_X), "flip_seed": "default_rng(20261010 + layer)",
                          "results": sens3, "summary": sens_sum,
                          "checker_values_quoted": {"adam_mlp": CHECKER_ADAM, "rbf_extended_grid": CHECKER_RBFX}},
           "null_precision": "every 'null' array is full float64 (repr); p = (1 + #{null >= obs}) / (1 + n) at full precision",
           "timing_nondeterministic": {"note": "wall-clock timing; a timing observation, not a figure; differs run to run",
                                       "wall_clock_s": wall, "job_seconds": job_secs, "null_auc_per_s": throughput}}
    js = json.dumps(out, indent=1)
    # number-only arrays on one line
    js = re.sub(r"\[\s+([-0-9.eE,\s]+?)\s+\]", lambda m: "[" + re.sub(r"\s+", " ", m.group(1)) + "]", js)
    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_json, "w") as f:
        f.write(js + "\n")
    text = render(json.loads(js), runtime_facts(data["an"], mod_hashes))
    with open(out_md, "w") as f:
        f.write(text)
    print(text)
    for kk, v in wall.items():
        print(f"[wall-clock] {kk}: {v:.1f} s", file=sys.stderr)
    print(f"[wall-clock] record-function job seconds summed over workers: {json.dumps({k: round(v, 1) for k, v in job_secs.items()})}; "
          f"{throughput:.2f} null AUC/s with {args.workers} workers", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
