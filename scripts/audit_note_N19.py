#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N19: companion-code sensitivity re-run (block :124-125).

The referent is external: github.com/arvomm/cacophony-public-code, notebooks/scoring.ipynb,
pinned below. The notebook's cell 1 imports pandas, matplotlib and scipy at top level. The audit
interpreter has numpy and pandas; scipy and matplotlib are absent (recorded at run time without
importing them), and nothing is installed, so the notebook cannot run here as released. Even with
all three present, running it would import and execute the clone's own `dcm_lab` package, which
this audit never does. So this script PORTS the notebook's scoring path (the numpy core of
dcm_lab/score.py, dcm_lab/truth.py and the CSV loader of dcm_lab/indicators.py) into numpy +
stdlib, and VALIDATES the port by regenerating every printed output stored in the notebook and
comparing it to the stored text byte for byte. Only then are the block's strikes run.

Third-party code is never imported or executed. The clone is read as data: the indicator CSV,
the notebook JSON (for its stored outputs and its cell-6 table), mapping.md (for the
demandingness table), pyproject.toml (version), and its .git HEAD/refs files (for the pin).
The script spawns no process and makes no network call. Run it with `python -I` from a
directory outside the clone, passing the clone by path:

    cd <scratchpad>/n19/run && <python> -I <repo>/scripts/audit_note_N19.py --ext <scratchpad>/n19/ext

Outputs: results/raw/2026-10-09_note-N19-cacophony.md and .json (paths relative to the repo).
"""
import argparse
import csv
import datetime
import hashlib
import importlib.metadata
import importlib.util
import io
import itertools
import json
import os
import re
import sys

import numpy as np

ROOT_DEFAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
NOTE = "RESEARCH-NOTE-v0_3-draft.md"
OUT_MD = "results/raw/2026-10-09_note-N19-cacophony.md"
OUT_JSON = "results/raw/2026-10-09_note-N19-cacophony.json"

EXT_URL = "https://github.com/arvomm/cacophony-public-code"
PIN_SHA = "b6ba87b55bd1184dd33f550bcd53875a6553494f"
PINNED_FILES = {   # sha256 of the files this script reads from the clone, at the pinned commit
    "notebooks/scoring.ipynb": "67f064f03160bb03a8b94c5153e76354e98e79afca343e82727e0d91cb6fde37",
    "dcm priors/Indicators Caco Nodes DCM priors.csv": "2c081311e02db976dbe1c856a49375cc8cdbaa5f6814e350d7fa3e3f38adba72",
    "dcm priors/mapping.md": "fdc60376954d87950fcf26a6cdba06420a41db764236df92705b45c8ce90e471",
    # the three modules ported below; hashed so the port is tied to the exact source it mirrors
    "dcm_lab/score.py": "ccaeb50fb74a7138feb6aa2998ef590bb94821f0437cfa60e003e3b237a176d8",
    "dcm_lab/truth.py": "18b4a9016b3da2ff91d05ebe06dfd20f1b0972c2dae1c433273236ec0602565f",
    "dcm_lab/indicators.py": "e2479713d53dc558221fabdfbcfcbce89fb9ece8eb20edafbe0bf7e3a83394f8",
}
NOTE_SHA = "5a34309ffe402cdeb99d0c60635adac67e08db23d82fc496142c656777d14871"
NOTE_S8 = (140, 149)   # the note's section 8, 1-indexed inclusive (task routing)
CSV_REL = "dcm priors/Indicators Caco Nodes DCM priors.csv"
NETPROC_PAT = r"requests|urllib|http|socket|subprocess|os\.system|Popen|!pip|%pip|wget|curl"
N1_FINAL = "results/raw/2026-10-09_note-N1-claims-ledger-final.md"   # read only, for one cross-reference
NOTE_GAP_PHRASE = "carry most of the gap between their optimist and sceptic verdicts"
GAP_TAU = 0.001   # post-hoc section: smallest aggregate gap counted as a gap (the aggregates' reported precision)


def package_status(names=("numpy", "pandas", "scipy", "matplotlib")):
    """Which packages this interpreter can see. find_spec locates a top-level package without
    importing it; importlib.metadata reads the installed dist-info. Nothing is imported."""
    res = {}
    for n in names:
        try:
            v = importlib.metadata.version(n)
        except importlib.metadata.PackageNotFoundError:
            v = None
        res[n] = {"present": importlib.util.find_spec(n) is not None, "version": v}
    return res


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_git_head(gitdir):
    """Resolve HEAD by reading files only (no git process)."""
    head = open(os.path.join(gitdir, "HEAD")).read().strip()
    if not head.startswith("ref:"):
        return head, "(detached)"
    ref = head.split(":", 1)[1].strip()
    loose = os.path.join(gitdir, ref)
    if os.path.isfile(loose):
        return open(loose).read().strip(), ref
    packed = os.path.join(gitdir, "packed-refs")
    if os.path.isfile(packed):
        for line in open(packed):
            parts = line.strip().split(" ")
            if len(parts) == 2 and parts[1] == ref:
                return parts[0], ref
    raise RuntimeError("cannot resolve HEAD in " + gitdir)


def disp(p, root):
    """Public-safe display of a path: scratch paths shortened, repo paths made relative."""
    p = os.path.abspath(p)
    if "/scratchpad/" in p:
        return "<scratchpad>/" + p.split("/scratchpad/", 1)[1]
    if p.startswith(root + os.sep):
        return os.path.relpath(p, root)
    return p


# ----------------------------------------------------------------------------------------------
# Port of dcm_lab (pinned commit). Each function mirrors the named source function line for line.
# ----------------------------------------------------------------------------------------------
L = 5                                                   # truth.py: L
C_PRIOR_SWEEP = [("Beta(1,1)", (1.0, 1.0)), ("Beta(2,2)", (2.0, 2.0)),
                 ("Beta(6,2)", (6.0, 2.0)), ("Beta(2,6)", (2.0, 6.0))]   # truth.py
ROOT_CELL7 = ("Beta(0.5,0.5)", (0.5, 0.5))   # not in the sweep: notebook cell 7 (markdown) advises also trying it
CELL7_ADVICE = "Beta (1/2, 1/2)"             # the phrase as cell 7 writes it; asserted present at run time
C_ALPHA_PRIOR = (8.0, 2.0)                              # truth.py
C_BETA_PRIOR = (2.0, 8.0)                               # truth.py
N_DRAWS = 5000                                          # notebook cell 1
SEED = 0                                                # notebook cell 1
HDI_PROB = 0.89                                         # notebook cell 1


def _parse_level(level_str):                            # indicators.py: _parse_level
    s = str(level_str).strip()
    for sep in ("–", "-"):
        if sep in s:
            head, tail = s.split(sep, 1)
            return int(head.strip()), tail.strip()
    raise ValueError("could not parse level string %r" % (level_str,))


def load_indicators(csv_path):                          # indicators.py: load_indicators (csv, not pandas)
    out = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for j, row in enumerate(csv.DictReader(f)):
            level, level_name = _parse_level(row["Level of C"])
            out.append(dict(j=j, level=level, level_name=level_name, name=row["Name"].strip(),
                            chosen_node=row["chosen dcm node"].strip(),
                            support=(row.get("chosen node support") or "").strip(),
                            demandingness=(row.get("chosen node demandingness") or "").strip(),
                            alpha=float(row["prior alpha"]), beta=float(row["prior beta"])))
    return out


def indicators_by_level(inds):                          # indicators.py
    g = {}
    for ind in inds:
        g.setdefault(ind["level"], []).append(ind)
    return g


def level_counts(inds):                                 # indicators.py
    return {lvl: len(ix) for lvl, ix in indicators_by_level(inds).items()}


def make_prior_config(root_prior, a, b, strict=False):  # truth.py: make_prior_config
    return {"root": root_prior, "c_alpha": C_ALPHA_PRIOR, "c_beta": C_BETA_PRIOR, "strict": bool(strict),
            "indicator_alpha": np.asarray(a, dtype=float), "indicator_beta": np.asarray(b, dtype=float)}


def _safe_log(x):                                       # score.py
    return np.log(np.maximum(x, 1e-300))


def hdi_from_samples(samples, prob=0.89, axis=0):       # score.py: hdi_from_samples
    s = np.asarray(samples)
    if s.ndim == 1:
        ss = np.sort(s)
        n = ss.shape[0]
        k = int(np.ceil(prob * n))
        if k >= n:
            return float(ss[0]), float(ss[-1])
        widths = ss[k:] - ss[: n - k]
        i = int(np.argmin(widths))
        return float(ss[i]), float(ss[i + k])
    if axis == 0:
        ss = np.sort(s, axis=0)
    else:
        ss = np.sort(s, axis=1).T
    n = ss.shape[0]
    k = int(np.ceil(prob * n))
    if k >= n:
        return ss[0].copy(), ss[-1].copy()
    widths = ss[k:] - ss[: n - k]
    i = np.argmin(widths, axis=0)
    cols = np.arange(ss.shape[1])
    return ss[i, cols], ss[i + k, cols]


def _enumerate_configs_full(L_=L):                      # score.py
    return [tuple(c) for c in itertools.product((0, 1), repeat=L_)]


def depth_of(cfg):                                      # score.py
    hi = 0
    for k in range(len(cfg)):
        if cfg[k]:
            hi = k + 1
    return hi


def _config_arrays(L_=L):                               # score.py
    configs = _enumerate_configs_full(L_)
    return configs, np.array(configs, dtype=int), np.array([depth_of(c) for c in configs], dtype=int)


def _sample_edge_logprobs(pc, n_draws, seed):           # score.py: _sample_edge_logprobs
    configs, cfg_mat, depth_idx = _config_arrays(L)
    n_cfg = cfg_mat.shape[0]
    rng = np.random.default_rng(seed)
    pi = rng.beta(*pc["root"], size=n_draws)
    if pc.get("strict", False):
        aC = np.ones((n_draws, L - 1))
    else:
        aC = rng.beta(*pc["c_alpha"], size=(n_draws, L - 1))
    bC = rng.beta(*pc["c_beta"], size=(n_draws, L - 1))
    log_pi, log_1mpi = _safe_log(pi), _safe_log(1.0 - pi)
    log_aC, log_1maC = _safe_log(aC), _safe_log(1.0 - aC)
    log_bC, log_1mbC = _safe_log(bC), _safe_log(1.0 - bC)
    log_p_cfg = np.zeros((n_draws, n_cfg))
    for ci, cfg in enumerate(configs):
        lp = log_pi if cfg[L - 1] == 1 else log_1mpi
        for e in range(L - 1):
            parent, child = cfg[e + 1], cfg[e]
            if parent == 1:
                lp = lp + (log_aC[:, e] if child == 1 else log_1maC[:, e])
            else:
                lp = lp + (log_bC[:, e] if child == 1 else log_1mbC[:, e])
        log_p_cfg[:, ci] = lp
    return cfg_mat, depth_idx, log_p_cfg


def prior_predictive_score(e_input, pc, level_of, n_draws=5000, seed=0, return_per_theta=False,
                           unscored=()):
    """score.py: prior_predictive_score. `unscored` (audit addition, default empty = the source's
    behaviour) removes the listed indicators from the likelihood: their message is 1 under both
    parent states, i.e. the indicator is treated as unobserved."""
    alpha, beta = pc["indicator_alpha"], pc["indicator_beta"]
    n_ind = len(alpha)
    e = np.asarray(e_input, dtype=np.int64)
    assert e.shape == (n_ind,)
    level_of = np.asarray(level_of, dtype=int)
    m1 = np.where(e == 1, alpha, 1.0 - alpha)
    m0 = np.where(e == 1, beta, 1.0 - beta)
    log_m1, log_m0 = _safe_log(m1), _safe_log(m0)
    for j in unscored:
        log_m1[j] = 0.0
        log_m0[j] = 0.0
    log_top_0, log_top_1 = np.zeros(L), np.zeros(L)
    for j in range(n_ind):
        k = int(level_of[j])
        log_top_0[k] += log_m0[j]
        log_top_1[k] += log_m1[j]
    cfg_mat, depth_idx, log_p_cfg = _sample_edge_logprobs(pc, n_draws, seed)
    n_cfg = cfg_mat.shape[0]
    log_lik_cfg = cfg_mat @ log_top_1 + (1 - cfg_mat) @ log_top_0
    log_joint = log_p_cfg + log_lik_cfg[None, :]
    log_joint -= log_joint.max(axis=1, keepdims=True)
    joint = np.exp(log_joint)
    joint /= joint.sum(axis=1, keepdims=True)
    post_C_per_theta = joint @ cfg_mat
    post_C = post_C_per_theta.mean(axis=0)
    depth_mask = np.zeros((n_cfg, L + 1))
    depth_mask[np.arange(n_cfg), depth_idx] = 1.0
    post_dep_per_theta = joint @ depth_mask
    post_dep = post_dep_per_theta.mean(axis=0)
    res = {"P(C_i=1|e)": {i + 1: float(post_C[i]) for i in range(L)},
           "P(depth=d|e)": {d: float(post_dep[d]) for d in range(L + 1)},
           "most_likely_depth": int(np.argmax(post_dep)),
           "_log_top": (log_top_1.copy(), log_top_0.copy())}
    if return_per_theta:
        res["P(C_i=1|e,theta)_per_draw"] = post_C_per_theta
        res["P(depth=d|e,theta)_per_draw"] = post_dep_per_theta
    return res


def overall_credence(post_C_per_theta, level_credences):  # score.py: overall_credence
    w = np.asarray(level_credences, dtype=float).ravel()
    assert w.shape == (L,) and w.sum() > 0
    w = w / w.sum()
    return np.asarray(post_C_per_theta, dtype=float) @ w


def prior_depth_distribution(pc, n_draws=5000, seed=0):  # score.py
    cfg_mat, depth_idx, log_p_cfg = _sample_edge_logprobs(pc, n_draws, seed)
    n_cfg = cfg_mat.shape[0]
    p = np.exp(log_p_cfg)
    p /= p.sum(axis=1, keepdims=True)
    dm = np.zeros((n_cfg, L + 1))
    dm[np.arange(n_cfg), depth_idx] = 1.0
    return (p @ dm).mean(axis=0)


def prior_C_marginals(pc, n_draws=5000, seed=0):        # score.py
    cfg_mat, depth_idx, log_p_cfg = _sample_edge_logprobs(pc, n_draws, seed)
    p = np.exp(log_p_cfg)
    p /= p.sum(axis=1, keepdims=True)
    return (p @ cfg_mat).mean(axis=0)


def format_score(scored, prior_depth=None, prior_C=None):  # score.py: format_score
    lines = ["Per-level posteriors P(C_i = 1 | e):"]
    for i, v in scored["P(C_i=1|e)"].items():
        bar = "#" * int(round(v * 40))
        suffix = f"    prior = {prior_C[i-1]:.3f}" if prior_C is not None else ""
        lines.append(f"  C{i}: {v:.3f}  {bar}{suffix}")
    lines.append("")
    lines.append("Posterior over depth (highest active level):")
    for d, v in scored["P(depth=d|e)"].items():
        bar = "#" * int(round(v * 40))
        suffix = f"    prior = {prior_depth[d]:.3f}" if prior_depth is not None else ""
        lines.append(f"  depth = {d}: {v:.3f}  {bar}{suffix}")
    lines.append("")
    lines.append(f"Most likely depth: {scored['most_likely_depth']}")
    return "\n".join(lines)


# ----------------------------------------------------------------------------------------------
# Regeneration of the notebook's printed outputs (cells 1, 10, 12, 16, 18, 25, 28, 31).
# ----------------------------------------------------------------------------------------------
class Out:
    def __init__(self):
        self.buf = io.StringIO()

    def p(self, *args):
        self.buf.write(" ".join(str(a) for a in args) + "\n")

    def text(self):
        return self.buf.getvalue()


CASES = [   # notebook cell 16
    ('A: mostly yes everywhere (~80% per level)', [0.80, 0.80, 0.80, 0.80, 0.80]),
    ('B: strong on levels 1-2, weak below', [0.80, 0.80, 0.15, 0.15, 0.15]),
    ('C: all no', [0.00, 0.00, 0.00, 0.00, 0.00]),
    ('D: strong on levels 1-4, weak on level 5', [0.80, 0.80, 0.80, 0.80, 0.20]),
    ('E: about half yes everywhere (the ambiguous one)', [0.50, 0.50, 0.50, 0.50, 0.50]),
]
SYSTEMS = {   # notebook cell 31 (the authors' illustrative evidence vectors)
    'Human': [1] * 37,
    'Fly': [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1],
    'LLM-optimist': [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'LLM-sceptic': [1, 1, 1, 0, 0, 0, 0, 0, 0] + [0] * 28,
    'Thermostat': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}
MY_CREDENCES_CELL28 = np.array([0.3, 0.2, 0.1, 0.3, 0.1])   # notebook cell 28


class Model:
    def __init__(self, inds):
        self.inds = inds
        self.N = len(inds)
        self.alpha = np.array([i["alpha"] for i in inds], dtype=float)
        self.beta = np.array([i["beta"] for i in inds], dtype=float)
        self.level_of = np.array([i["level"] - 1 for i in inds], dtype=int)

    def cfg(self, root_ab, strict=False, alpha=None, beta=None):
        return make_prior_config(root_ab, self.alpha if alpha is None else alpha,
                                 self.beta if beta is None else beta, strict=strict)

    def e_from_fractions(self, fractions):              # notebook cell 10
        e = np.zeros(self.N, dtype=int)
        by_lvl = indicators_by_level(self.inds)
        for k_idx, f in enumerate(fractions):
            idxs = [i["j"] for i in by_lvl.get(k_idx + 1, [])]
            for j in idxs[:int(round(f * len(idxs)))]:
                e[j] = 1
        return e


def regenerate(m):
    """Return {cell_index: printed text} for the notebook cells with stream output."""
    out = {}
    # cell 1
    o = Out()
    o.p(f'Network: {L} levels, {m.N} indicators.  Chain: C5 -> C4 -> C3 -> C2 -> C1 (root = C5).')
    o.p('Indicators per level:')
    for lvl, count in sorted(level_counts(m.inds).items()):
        name = indicators_by_level(m.inds)[lvl][0]["level_name"]
        o.p(f'  Level {lvl} ({name}): {count} indicators')
    o.p(f'\nEdge priors:  alpha_C ~ Beta{C_ALPHA_PRIOR} (mean {C_ALPHA_PRIOR[0]/sum(C_ALPHA_PRIOR):.2f}) '
        f'·  beta_C ~ Beta{C_BETA_PRIOR} (mean {C_BETA_PRIOR[0]/sum(C_BETA_PRIOR):.2f})')
    o.p(f'Monte-Carlo draws per prior: {N_DRAWS};  HDI band probability: {HDI_PROB}')
    out[1] = o.text()
    # cell 10
    o = Out()
    e_demo = m.e_from_fractions([0.5, 0.5, 0.5, 0.5, 0.5])
    prior_C_gen = prior_C_marginals(m.cfg((1.0, 1.0)), n_draws=N_DRAWS, seed=SEED)
    prior_dep_gen = prior_depth_distribution(m.cfg((1.0, 1.0)), n_draws=N_DRAWS, seed=SEED)
    for label, strict in [('GENERALISED  (Condition 2B: alpha_C~Beta(8,2))', False),
                          ('STRICT       (Condition 2A: alpha_C = 1)', True)]:
        sc = prior_predictive_score(e_demo, m.cfg((1.0, 1.0), strict=strict), m.level_of,
                                    n_draws=N_DRAWS, seed=SEED)
        o.p('=' * 66)
        o.p(f'{label}   — root Beta(1,1), case = half-yes everywhere')
        o.p(format_score(sc, prior_depth=prior_dep_gen, prior_C=prior_C_gen))
    out[10] = o.text()
    # cell 12 (printed lines only)
    o = Out()
    all_cfg = _enumerate_configs_full(L)
    stair = np.array([list(c) == [1] * sum(c) + [0] * (L - sum(c)) for c in all_cfg])
    e_gap = m.e_from_fractions([0.7, 0.7, 0.8, 0.1, 0.8])
    cfg_mat, depth_idx, log_p_cfg = _sample_edge_logprobs(m.cfg((1.0, 1.0)), N_DRAWS, SEED)
    m1 = np.where(e_gap == 1, m.alpha, 1 - m.alpha)
    m0 = np.where(e_gap == 1, m.beta, 1 - m.beta)
    lt1, lt0 = np.zeros(L), np.zeros(L)
    for j in range(m.N):
        lt1[m.level_of[j]] += np.log(max(m1[j], 1e-300))
        lt0[m.level_of[j]] += np.log(max(m0[j], 1e-300))
    log_lik = cfg_mat @ lt1 + (1 - cfg_mat) @ lt0
    lj = log_p_cfg + log_lik[None, :]
    lj -= lj.max(1, keepdims=True)
    joint = np.exp(lj)
    joint /= joint.sum(1, keepdims=True)
    p_cfg = joint.mean(0)
    o.p(f'Non-staircase posterior mass (generalised): {p_cfg[~stair].sum():.3f}')
    o.p('Config string is C1C2C3C4C5 (1=on).')
    out[12] = o.text()
    # cell 16
    o = Out()
    for name, frac in CASES:
        e = m.e_from_fractions(frac)
        counts = [int(e[m.level_of == k].sum()) for k in range(L)]
        sizes = [int((m.level_of == k).sum()) for k in range(L)]
        o.p(f'{name:55s}   yes per level: [' + ', '.join(f'{c}/{s}' for c, s in zip(counts, sizes)) + ']')
    out[16] = o.text()
    # cell 18
    o = Out()
    case_name, frac = CASES[4]
    e_demo = m.e_from_fractions(frac)
    o.p(f'Input: {case_name}\n')
    for label, ab in C_PRIOR_SWEEP:
        sc = prior_predictive_score(e_demo, m.cfg(ab), m.level_of, n_draws=N_DRAWS, seed=SEED)
        prior_dep = prior_depth_distribution(m.cfg(ab), n_draws=N_DRAWS, seed=SEED)
        prior_C = prior_C_marginals(m.cfg(ab), n_draws=N_DRAWS, seed=SEED)
        o.p('=' * 70)
        o.p(f'root pi = {label}')
        o.p(format_score(sc, prior_depth=prior_dep, prior_C=prior_C))
    out[18] = o.text()
    # cell 25
    o = Out()
    e_custom = np.zeros(m.N, dtype=int)
    my_root = (1.0, 1.0)
    my_strict = False
    cfg_custom = m.cfg(my_root, strict=my_strict)
    prior_dep = prior_depth_distribution(cfg_custom, n_draws=N_DRAWS, seed=SEED)
    prior_C = prior_C_marginals(cfg_custom, n_draws=N_DRAWS, seed=SEED)
    sc_custom = prior_predictive_score(e_custom, cfg_custom, m.level_of, n_draws=N_DRAWS, seed=SEED,
                                       return_per_theta=True)
    o.p(f'Custom case   root = Beta{my_root}   strict = {my_strict}')
    o.p('Yes per level: ' + ', '.join(
        f'L{k+1}: {int(e_custom[m.level_of==k].sum())}/{int((m.level_of==k).sum())}' for k in range(L)))
    o.p()
    o.p(format_score(sc_custom, prior_depth=prior_dep, prior_C=prior_C))
    out[25] = o.text()
    # cell 28
    o = Out()
    case_name, frac = CASES[4]
    e_E = m.e_from_fractions(frac)
    sc = prior_predictive_score(e_E, m.cfg((1.0, 1.0)), m.level_of, n_draws=N_DRAWS, seed=SEED,
                                return_per_theta=True)
    per = sc['P(C_i=1|e,theta)_per_draw']
    mixed = overall_credence(per, MY_CREDENCES_CELL28)
    pm = per.mean(0)
    plo, phi = hdi_from_samples(per, prob=HDI_PROB, axis=0)
    mlo, mhi = hdi_from_samples(mixed, prob=HDI_PROB)
    o.p(f'Case: {case_name}   (generalised model, root Beta(1,1))')
    o.p(f'Theoretical credences P(L*=i): {list(MY_CREDENCES_CELL28)}\n')
    for k in range(L):
        o.p(f'  C{k+1}: mean = {pm[k]:.3f},  {int(HDI_PROB*100)}% HDI = [{plo[k]:.3f}, {phi[k]:.3f}]')
    o.p(f'\nOverall credence P(C|E) = sum_i P(L*=i) P(C_i|E):  mean = {mixed.mean():.3f},  '
        f'{int(HDI_PROB*100)}% HDI = [{mlo:.3f}, {mhi:.3f}]')
    out[28] = o.text()
    # cell 31
    o = Out()
    equal = np.full(L, 1 / L)
    hdr = f'{"system":<14}  ' + '  '.join(f'C{k+1}' + '   ' for k in range(L)) + '   P(C|E)  [89% HDI]'
    o.p(hdr)
    o.p('-' * len(hdr))
    for name, e in SYSTEMS.items():
        assert len(e) == m.N
        sc = prior_predictive_score(np.asarray(e, int), m.cfg((1.0, 1.0)), m.level_of,
                                    n_draws=N_DRAWS, seed=SEED, return_per_theta=True)
        per = sc['P(C_i=1|e,theta)_per_draw']
        mixed = overall_credence(per, equal)
        ml, mh = hdi_from_samples(mixed, prob=HDI_PROB)
        cells_ = '  '.join(f'{v:.3f}' for v in per.mean(0))
        o.p(f'{name:<14}  {cells_}    {mixed.mean():.3f}  [{ml:.3f}, {mh:.3f}]')
    out[31] = o.text()
    return out


def stored_streams(nb):
    """{cell_index: concatenated stored stream text} for code cells with stream output."""
    res = {}
    for i, c in enumerate(nb["cells"]):
        if c["cell_type"] != "code":
            continue
        t = "".join("".join(o.get("text", "")) for o in c.get("outputs", []) if o.get("output_type") == "stream")
        if t:
            res[i] = t
    return res


def parse_cell6_table(nb):
    """Parse the stored text/plain table of cell 6 (j, level, name, alpha, beta)."""
    c = nb["cells"][6]
    txt = None
    for o in c.get("outputs", []):
        d = o.get("data", {})
        if "text/plain" in d:
            txt = "".join(d["text/plain"])
    rows = {}
    pat = re.compile(r"^\s*(\d+)\s+(\d+)\s+(\d)\s+(.*?)\s+(\d+\.\d+)\s+(\d+\.\d+)\s*\\?\s*$")
    for line in txt.splitlines():
        mt = pat.match(line)
        if mt:
            idx, j, lvl, name, a, b = mt.groups()
            rows[int(j)] = dict(level=int(lvl), name=name, alpha=float(a), beta=float(b))
    return rows


# ----------------------------------------------------------------------------------------------
# The block's re-run
# ----------------------------------------------------------------------------------------------
def summarize(m, e, root=(1.0, 1.0), strict=False, seed=SEED, unscored=(), alpha=None, beta=None,
              weightings=None):
    pc = m.cfg(root, strict=strict, alpha=alpha, beta=beta)
    sc = prior_predictive_score(np.asarray(e, int), pc, m.level_of, n_draws=N_DRAWS, seed=seed,
                                return_per_theta=True, unscored=unscored)
    per = sc['P(C_i=1|e,theta)_per_draw']
    lo, hi = hdi_from_samples(per, prob=HDI_PROB, axis=0)
    lt1, lt0 = sc["_log_top"]
    res = {"per_level_mean": [float(v) for v in per.mean(0)],
           "per_level_hdi89": [[float(a), float(b)] for a, b in zip(lo, hi)],
           "log10_LR_per_level": [float((a - b) / np.log(10)) for a, b in zip(lt1, lt0)],
           "aggregates": {}}
    for wname, w in (weightings or {}).items():
        mixed = overall_credence(per, w)
        ml, mh = hdi_from_samples(mixed, prob=HDI_PROB)
        res["aggregates"][wname] = {"weights": [float(x) for x in np.asarray(w, float) / np.sum(w)],
                                    "mean": float(mixed.mean()), "hdi89": [float(ml), float(mh)]}
    return res


def f3(x):
    return f"{x:.3f}"


def f6(x):
    return f"{x:.6f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ext", required=True, help="the clone of the external repository (read as data)")
    ap.add_argument("--repo", default=ROOT_DEFAULT)
    ap.add_argument("--out-md", default=OUT_MD)
    ap.add_argument("--out-json", default=OUT_JSON)
    args = ap.parse_args()
    root = os.path.abspath(args.repo)
    ext = os.path.abspath(args.ext)
    assert not os.path.commonpath([ext, root]) == root, "the clone must be outside the repository"

    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    head, head_ref = read_git_head(os.path.join(root, ".git"))
    block_sha = sha256_file(os.path.join(root, BLOCK))
    script_path = os.path.abspath(__file__)
    script_sha = sha256_file(script_path)

    # ---- pin the external repository ----
    ext_head, ext_ref = read_git_head(os.path.join(ext, ".git"))
    assert ext_head == PIN_SHA, "clone HEAD %s != pinned %s" % (ext_head, PIN_SHA)
    file_shas = {}
    for rel, want in PINNED_FILES.items():
        got = sha256_file(os.path.join(ext, rel))
        assert got == want, "sha256 mismatch for %s: %s" % (rel, got)
        file_shas[rel] = got
    file_shas["pyproject.toml"] = sha256_file(os.path.join(ext, "pyproject.toml"))   # read for the version only
    pyproj = open(os.path.join(ext, "pyproject.toml"), encoding="utf-8").read()
    ext_version = re.search(r'^version\s*=\s*"([^"]+)"', pyproj, re.M).group(1)

    nb = json.load(open(os.path.join(ext, "notebooks/scoring.ipynb"), encoding="utf-8"))
    exec_counts = [c.get("execution_count") for c in nb["cells"] if c["cell_type"] == "code"]
    review = {"savefig_cells": [], "netproc_cells": []}
    for i, c in enumerate(nb["cells"]):
        if c["cell_type"] != "code":
            continue
        src = "".join(c.get("source", []))
        if "savefig" in src:
            review["savefig_cells"].append(i)
        if re.search(NETPROC_PAT, src):
            review["netproc_cells"].append(i)
    nb_py = nb.get("metadata", {}).get("language_info", {}).get("version")
    nb_cell1_imports = sorted(set(re.findall(r"^\s*(?:import|from)\s+(pandas|scipy|matplotlib)\b",
                                             "".join(nb["cells"][1].get("source", [])), re.M)))
    cell7_src = "".join(nb["cells"][7].get("source", []))
    assert nb["cells"][7]["cell_type"] == "markdown" and CELL7_ADVICE in cell7_src, "cell 7 advice not found"
    pkgs = package_status()

    # ---- load, validate the port ----
    inds = load_indicators(os.path.join(ext, CSV_REL))
    m = Model(inds)
    assert m.N == 37
    regen = regenerate(m)
    stored = stored_streams(nb)
    validation = []
    for ci in sorted(stored):
        if ci == 20:   # cell 20 prints only the word 'Computed.'; no number to validate
            validation.append({"cell": ci, "chars": len(stored[ci]), "match": stored[ci] == "Computed.\n",
                               "note": "prints only 'Computed.'"})
            continue
        r = regen.get(ci)
        validation.append({"cell": ci, "chars": len(stored[ci]), "match": r == stored[ci],
                           "note": "" if r == stored[ci] else "MISMATCH"})
    missing = sorted(set(regen) - set(stored))
    t6 = parse_cell6_table(nb)
    t6_ok = 0
    t6_bad = []
    for ind in inds:
        r = t6.get(ind["j"])
        nm = r["name"].rstrip(".") if r else None
        ok = (r is not None and r["level"] == ind["level"] and abs(r["alpha"] - round(ind["alpha"], 3)) < 1e-9
              and abs(r["beta"] - round(ind["beta"], 3)) < 1e-9 and ind["name"].startswith(nm))
        t6_ok += ok
        if not ok:
            t6_bad.append(ind["j"])
    port_ok = all(v["match"] for v in validation) and not missing and t6_ok == 37

    # ---- indicators of interest, as the notebook names them ----
    def find(level, name):
        hits = [i for i in inds if i["level"] == level and i["name"] == name]
        assert len(hits) == 1, (level, name)
        return hits[0]
    META2 = find(2, "Meta-cognition")
    META3 = find(3, "Metacognition")
    COUP = find(1, "Coupling between reported states and subsequent behaviour")
    opt = np.array(SYSTEMS["LLM-optimist"], dtype=int)

    # mapping.md: the demandingness -> beta table line for 'Weakly undemanding'
    mapping_lines = open(os.path.join(ext, "dcm priors/mapping.md"), encoding="utf-8").read().splitlines()
    wu_line = [(n + 1, s) for n, s in enumerate(mapping_lines) if re.match(r"^\|\s*Weakly undemanding\s*\|", s)]
    assert len(wu_line) == 1
    wu_beta = float(wu_line[0][1].split("|")[2].strip())

    W = {"equal": np.full(L, 1 / L),
         "notebook_cell28": MY_CREDENCES_CELL28,
         "L1L2_only": np.array([0.5, 0.5, 0.0, 0.0, 0.0])}

    def strike(js):
        e = opt.copy()
        for j in js:
            e[j] = 0
        return e

    conds = [
        ("baseline", "LLM-optimist at released defaults", opt, {}),
        ("strike_meta_L2", "strike L2 'Meta-cognition' (j=%d): set 1 -> 0" % META2["j"], strike([META2["j"]]), {}),
        ("strike_meta_L3", "strike L3 'Metacognition' (j=%d): already 0 in the vector" % META3["j"],
         strike([META3["j"]]), {}),
        ("strike_coupling", "strike L1 'Coupling between reported states and subsequent behaviour' (j=%d): set 1 -> 0"
         % COUP["j"], strike([COUP["j"]]), {}),
        ("unscored_meta_L2", "alternative reading: L2 'Meta-cognition' removed from the likelihood (unobserved)",
         opt, {"unscored": (META2["j"],)}),
        ("unscored_coupling", "alternative reading: L1 coupling removed from the likelihood (unobserved)",
         opt, {"unscored": (COUP["j"],)}),
    ]
    results = {}
    for key, desc, e, kw in conds:
        r = summarize(m, e, weightings=W, **kw)
        r["description"] = desc
        r["yes_per_level"] = [int(e[m.level_of == k].sum()) for k in range(L)]
        results[key] = r
    base_eq = results["baseline"]["aggregates"]["equal"]["mean"]

    # diagnostic (post-hoc): would the coupling strike move the verdict if the indicator were demanding?
    cf = {}
    for tag, (a_, b_) in {"coupling_as_fallback_0.73_0.10": (0.73, 0.10),
                          "coupling_as_metacognition_0.93_0.30": (META2["alpha"], META2["beta"])}.items():
        a2, b2 = m.alpha.copy(), m.beta.copy()
        a2[COUP["j"]], b2[COUP["j"]] = a_, b_
        rb = summarize(m, opt, alpha=a2, beta=b2, weightings={"equal": W["equal"]})
        rs = summarize(m, strike([COUP["j"]]), alpha=a2, beta=b2, weightings={"equal": W["equal"]})
        cf[tag] = {"alpha": a_, "beta": b_, "baseline": rb, "strike": rs}

    # robustness: the authors' root-prior sweep and the strict model, equal credences
    rob = {}
    for key in ("baseline", "strike_meta_L2", "strike_coupling"):
        e = dict((c[0], c[2]) for c in conds)[key]
        row = {}
        for label, ab in C_PRIOR_SWEEP:
            row["generalised " + label] = summarize(m, e, root=ab, weightings={"equal": W["equal"]})
        row["generalised " + ROOT_CELL7[0] + " [cell 7]"] = summarize(m, e, root=ROOT_CELL7[1],
                                                                       weightings={"equal": W["equal"]})
        row["strict Beta(1,1)"] = summarize(m, e, strict=True, weightings={"equal": W["equal"]})
        rob[key] = row
    # Monte Carlo spread of the equal-credence aggregate across seeds 0..19
    seeds = {}
    for key in ("baseline", "strike_meta_L2", "strike_coupling"):
        e = dict((c[0], c[2]) for c in conds)[key]
        vals = [summarize(m, e, seed=s, weightings={"equal": W["equal"]})["aggregates"]["equal"]["mean"]
                for s in range(20)]
        seeds[key] = {"seeds": "0..19", "min": min(vals), "max": max(vals), "values": vals}

    # Levels 1-2 weightings (checker finding 2): w = (t, 1-t, 0, 0, 0) gives t*C1 + (1-t)*C2, so the
    # aggregate over all such weightings runs between C2 (t = 0) and C1 (t = 1); (0.5, 0.5) is the midpoint.
    l12_range = {}
    for key, r in results.items():
        c1, c2 = r["per_level_mean"][0], r["per_level_mean"][1]
        b1, b2 = results["baseline"]["per_level_mean"][0], results["baseline"]["per_level_mean"][1]
        l12_range[key] = {"all_level2": c2, "midpoint_0.5_0.5": r["aggregates"]["L1L2_only"]["mean"], "all_level1": c1,
                          "change_vs_baseline_all_level2": c2 - b2, "change_vs_baseline_all_level1": c1 - b1}

    # ---- POST-HOC (checker finding 1; not in the block's procedure): the optimist-sceptic gap ----
    scep = np.array(SYSTEMS["LLM-sceptic"], dtype=int)
    two = (COUP["j"], META2["j"])
    assert all(opt[j] == 1 and scep[j] == 0 for j in two)
    scep_add = scep.copy()
    for j in two:
        scep_add[j] = 1
    gap_vecs = {"optimist": opt, "sceptic": scep,
                "optimist_strike_both": strike(two),
                "optimist_strike_coupling": strike([COUP["j"]]),
                "optimist_strike_meta_L2": strike([META2["j"]]),
                "sceptic_add_both": scep_add}
    gres = {k: summarize(m, e, weightings=W) for k, e in gap_vecs.items()}
    assert gres["optimist"]["per_level_mean"] == results["baseline"]["per_level_mean"]
    shares = {}
    for wname in W:
        o_ = gres["optimist"]["aggregates"][wname]["mean"]
        s_ = gres["sceptic"]["aggregates"][wname]["mean"]
        row = {"optimist": o_, "sceptic": s_, "gap": o_ - s_}
        for k in ("optimist_strike_both", "optimist_strike_coupling", "optimist_strike_meta_L2"):
            v = gres[k]["aggregates"][wname]["mean"]
            row[k] = {"aggregate": v, "share_of_gap_closed": (o_ - v) / (o_ - s_)}
        v = gres["sceptic_add_both"]["aggregates"][wname]["mean"]
        row["sceptic_add_both"] = {"aggregate": v, "share_of_gap_closed": (v - s_) / (o_ - s_)}
        shares[wname] = row
    po = np.array(gres["optimist"]["per_level_mean"])
    gvec = po - np.array(gres["sceptic"]["per_level_mean"])          # per-level gap
    cvec = po - np.array(gres["optimist_strike_both"]["per_level_mean"])   # per-level part closed by both strikes
    assert np.all(gvec > 0)
    vertices = [{"level": i + 1, "gap": float(gvec[i]), "closed": float(cvec[i]), "share": float(cvec[i] / gvec[i])}
                for i in range(L)]

    def max_share(tau):
        """max over weightings w (simplex) with aggregate gap g.w >= tau of (c.w)/(g.w). A ratio of two linear
        functions with a positive denominator is quasilinear, so the maximum over the polytope
        {w in simplex, g.w >= tau} is at one of its vertices: a simplex vertex with g_i >= tau, or the point
        where an edge from such a vertex to one with g_k < tau crosses g.w = tau."""
        cand = []
        for i in range(L):
            if gvec[i] >= tau:
                w_ = np.zeros(L)
                w_[i] = 1.0
                cand.append(w_)
                for k in range(L):
                    if gvec[k] < tau:
                        t = (tau - gvec[k]) / (gvec[i] - gvec[k])
                        w_ = np.zeros(L)
                        w_[i], w_[k] = t, 1.0 - t
                        cand.append(w_)
        best = max(cand, key=lambda w_: float(cvec @ w_) / float(gvec @ w_))
        return {"tau": tau, "weights": [float(x) for x in best], "share": float(cvec @ best) / float(gvec @ best),
                "gap_at_max": float(gvec @ best)}
    gap_max = {"levels_1_2_only": max((v for v in vertices if v["level"] in (1, 2)), key=lambda v: v["share"]),
               "gap_at_least_tau": max_share(GAP_TAU),
               "unrestricted": max(vertices, key=lambda v: v["share"])}
    posthoc_gap = {"post_hoc": True, "adopted": False, "indicators_struck": list(two),
                   "sceptic_vector": SYSTEMS["LLM-sceptic"], "per_condition": gres, "shares_by_weighting": shares,
                   "per_level_vertices": vertices, "max_over_weightings": gap_max}

    # ---- the note, section 8 ----
    note_path = os.path.join(root, NOTE)
    note_sha = sha256_file(note_path)
    assert note_sha == NOTE_SHA, "note sha256 changed: " + note_sha
    note_lines = open(note_path, encoding="utf-8").read().splitlines()
    s8 = note_lines[NOTE_S8[0] - 1:NOTE_S8[1]]
    assert s8[0].startswith("## 8."), s8[0][:40]
    numerals = []
    for off, line in enumerate(s8):
        for mt in re.finditer(r"(?<![\w.])\d+(?:\.\d+)?%?(?:B\b)?", line):
            numerals.append({"line": NOTE_S8[0] + off, "token": mt.group(0)})
    set0_lines = [n + 1 for n, s in enumerate(note_lines) if "set to 0" in s]
    gap_lines = [n + 1 for n, s in enumerate(note_lines) if NOTE_GAP_PHRASE in s]
    assert len(gap_lines) == 1, gap_lines
    wd_lines = [NOTE_S8[0] + off for off, s in enumerate(s8) if "what-if is withdrawn" in s]
    assert len(wd_lines) == 1, wd_lines
    posthoc_gap["note_line"] = gap_lines[0]
    posthoc_gap["note_withdrawal_line"] = wd_lines[0]
    posthoc_gap["note_phrase"] = NOTE_GAP_PHRASE
    # Cross-reference into N1 final, by N1's stable row ids rather than line numbers (Code's fix after the
    # values-check: N1 final is another item's file and is re-run after this one is committed, so its line
    # numbers and sha change; this script no longer reads it).
    n1_ref = {"path": N1_FINAL, "rows_note_line": ["S1#145"], "span_note": "S1 span note (note:29 stale against section 8)"}

    # ---- assemble ----
    J = {"item": "N19", "block": BLOCK, "block_sha256": block_sha, "block_lines": "124-125",
         "stamp": stamp, "head": head, "script": "scripts/audit_note_N19.py", "script_sha256": script_sha,
         "interpreter": sys.executable, "python": sys.version.split()[0], "numpy": np.__version__,
         "interpreter_packages": pkgs, "script_imports": "numpy + standard library only",
         "external": {"url": EXT_URL, "pinned_commit": ext_head, "ref": ext_ref, "pyproject_version": ext_version,
                      "file_sha256": file_shas, "notebook_execution_counts": exec_counts,
                      "notebook_kernel_python": nb_py, "notebook_review": review,
                      "notebook_cell1_third_party_imports": nb_cell1_imports,
                      "notebook_cell7_root_prior_advice": CELL7_ADVICE,
                      "netproc_pattern": NETPROC_PAT},
         "defaults": {"N_DRAWS": N_DRAWS, "SEED": SEED, "HDI_PROB": HDI_PROB, "root_prior": [1.0, 1.0],
                      "model": "generalised (Condition 2B)", "alpha_C_prior": list(C_ALPHA_PRIOR),
                      "beta_C_prior": list(C_BETA_PRIOR), "credences_cell31": "equal, 1/5 each"},
         "port_validation": {"cells": validation, "regenerated_without_stored": missing,
                             "cell6_rows_matching": t6_ok, "cell6_rows_mismatching": t6_bad, "port_ok": port_ok},
         "indicators": {k: {kk: v[kk] for kk in ("j", "level", "level_name", "name", "chosen_node", "support",
                                                 "demandingness", "alpha", "beta")}
                        | {"optimist_value": int(opt[v["j"]])}
                        for k, v in (("metacognition_L2", META2), ("metacognition_L3", META3), ("coupling_L1", COUP))},
         "mapping_md_weakly_undemanding": {"line": wu_line[0][0], "beta": wu_beta},
         "optimist_vector": SYSTEMS["LLM-optimist"],
         "conditions": results, "levels_1_2_weighting_range": l12_range,
         "counterfactual_coupling_params": cf, "robustness": rob, "seed_spread": seeds,
         "note": {"path": NOTE, "sha256": note_sha, "section8_lines": list(NOTE_S8), "numerals": numerals,
                  "set_to_0_lines": set0_lines},
         "post_hoc_gap_share": posthoc_gap, "n1_final_crossref": n1_ref}

    md = []
    w = md.append
    w("# AUDIT-note-release v1.2 -- N19: companion-code sensitivity re-run (block :124-125)")
    w("")
    w(f"- Code stamp: {stamp} (date -u equivalent); HEAD `{head}`")
    w(f"- Block `{BLOCK}` sha256 `{block_sha}`")
    w(f"- Script `scripts/audit_note_N19.py` sha256 `{script_sha}`; interpreter {sys.executable} "
      f"(Python {sys.version.split()[0]}, numpy {np.__version__}); run with `-I`")
    w(f"- Command: `cd <scratchpad>/n19/run && {sys.executable} -I {script_path} "
      f"--ext {disp(ext, root)}` (cwd outside the clone; the clone is passed by path)")
    w(f"- External repository: {EXT_URL}, cloned with `git clone` into a new empty directory outside the repository; "
      f"HEAD pinned at `{ext_head}` ({ext_ref}); pyproject version {ext_version}. The script asserts the pin by "
      f"reading the clone's .git files (no git process).")
    w(f"- `notebooks/scoring.ipynb` sha256 `{file_shas['notebooks/scoring.ipynb']}`; its code cells carry execution "
      f"counts {exec_counts[0]}..{exec_counts[-1]} in order (one clean top-to-bottom run); kernel Python {nb_py}.")
    w(f"- Other files read from the clone (sha256): " + "; ".join(
        f"`{k}` `{v[:16]}...`" for k, v in file_shas.items() if k != "notebooks/scoring.ipynb"))
    w(f"- Note `{NOTE}` sha256 `{note_sha}` (asserted equal to the routed sha); section 8 = lines "
      f"{NOTE_S8[0]}-{NOTE_S8[1]}.")
    w("")
    w("## 1. Method")
    w("")
    def andjoin(xs):
        xs = list(xs)
        return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]
    have_l = [f"{n} {v['version']}" for n, v in pkgs.items() if v["present"]]
    lack_l = [n for n, v in pkgs.items() if not v["present"]]
    have = andjoin(have_l)
    lack = andjoin(lack_l) if lack_l else "nothing"
    lack_verb = "is" if len(lack_l) <= 1 else "are"
    w(f"The notebook's cell 1 imports {andjoin(nb_cell1_imports)} at top level (and `dcm_lab/indicators.py` imports "
      f"pandas). This interpreter has {have}; {lack} {lack_verb} "
      f"absent (checked with `importlib.util.find_spec` and `importlib.metadata`, which locate a package without "
      f"importing it). Nothing was installed, so the notebook cannot run here as released. That is not the only "
      f"reason for the port: even with all three present, running the notebook would import and execute the "
      f"clone's own `dcm_lab` package, and this audit reads third-party code as data only. This script itself "
      f"imports numpy and the standard library only. "
      "The notebook's code cells were read as JSON and reviewed before anything ran. No file of the clone was "
      "imported or executed. The scoring path the notebook uses (`dcm_lab/score.py`: `_sample_edge_logprobs`, "
      "`prior_predictive_score`, `overall_credence`, `hdi_from_samples`, `prior_C_marginals`, "
      "`prior_depth_distribution`, `format_score`; `dcm_lab/truth.py` constants and `make_prior_config`; the CSV loader "
      "of `dcm_lab/indicators.py`) is ported line for line into this script; pandas is used upstream only to read "
      "the CSV and to display a table, scipy only for a plot's density curve, matplotlib only for figures. The port "
      "is accepted only if it regenerates every printed output stored in the notebook exactly (section 2).")
    w("")
    w(f"Review of the notebook's code cells (read as JSON before anything ran; Code read every cell, and this script "
      f"re-scans them): cells matching network/process patterns "
      f"(`{NETPROC_PAT}`): {review['netproc_cells'] or 'none'}. "
      f"Cell 1 inserts the repository root (`..` of the working directory) at the front of `sys.path`, imports "
      f"`dcm_lab`, and creates `../outputs/figures`; cells calling `savefig` (PNG writes there): "
      f"{review['savefig_cells']}. Running the notebook as-is would execute the clone's package and write inside the "
      f"clone; the port avoids both.")
    w("")
    w(f"Released defaults (notebook cell 1 and `truth.py`): N_DRAWS = {N_DRAWS}, SEED = {SEED}, HDI probability "
      f"{HDI_PROB}; generalised model (Condition 2B), alpha_C ~ Beta{C_ALPHA_PRIOR}, beta_C ~ Beta{C_BETA_PRIOR}; "
      f"root pi ~ Beta(1,1); cell 31 scores the five illustrative systems with equal credences P(L*=i) = 1/5. "
      f"Every condition below uses these defaults and the same seed, so all conditions share one set of 5000 prior "
      f"draws (common random numbers) and differences between them are exact for that draw set.")
    w("")
    w("## 2. Port validation against the notebook's stored outputs")
    w("")
    w("| cell | stored stream chars | regenerated text equals stored text |")
    w("|---|---|---|")
    for v in validation:
        w(f"| {v['cell']} | {v['chars']} | {'yes' if v['match'] else 'NO'}{(' (' + v['note'] + ')') if v['note'] else ''} |")
    w("")
    w(f"Cell 6's stored indicator table (j, level, name, alpha, beta as displayed): {t6_ok}/37 rows match the CSV "
      f"this script parsed{'' if not t6_bad else '; mismatching j: ' + str(t6_bad)}. "
      f"Port verdict: **{'PASS' if port_ok else 'FAIL'}** -- "
      + ("every stored printed output is regenerated character for character, including cell 31's "
         "`LLM-optimist ... 0.394  [0.387, 0.400]`." if port_ok else "the re-run below does not carry; see the JSON."))
    w("")
    w("## 3. The indicators, as the notebook names them")
    w("")
    w("| j | level | name (CSV `Name`, shown in notebook cell 6) | DCM node | support | demandingness | alpha (TPR) | beta (FPR) | LLM-optimist |")
    w("|---|---|---|---|---|---|---|---|---|")
    for ind in (COUP, META2, META3):
        w(f"| {ind['j']} | {ind['level']} ({ind['level_name']}) | {ind['name']} | {ind['chosen_node']} | "
          f"{ind['support'] or '-'} | {ind['demandingness'] or '-'} | {ind['alpha']} | {ind['beta']} | {int(opt[ind['j']])} |")
    w("")
    w(f"- The vector is named `LLM-optimist` in cell 31. Cell 6's display truncates j={COUP['j']}'s name to "
      f"`Coupling between reported states and subsequen...`; the full name above is the CSV's.")
    w(f"- The notebook has two metacognition indicators: Level 2 `Meta-cognition` (j={META2['j']}, the computational-"
      f"level one) and Level 3 `Metacognition` (j={META3['j']}, a default-fallback row). The optimist vector scores "
      f"the Level 2 one present and the Level 3 one absent, so 'strike the metacognition indicator' acts on j={META2['j']}; "
      f"striking j={META3['j']} is a no-op (shown for completeness).")
    w(f"- Coupling's stated false-positive rate: CSV `prior beta` = {COUP['beta']} for j={COUP['j']} (demandingness "
      f"`{COUP['demandingness']}`); `dcm priors/mapping.md`:{wu_line[0][0]} maps 'Weakly undemanding' to beta = "
      f"{wu_beta:.2f}; notebook cell 6 displays beta 0.70 on row {COUP['j']}. The model's beta is "
      f"P(I = 1 | parent C1 = 0), the indicator's rate when the Level 1 node is off.")
    w("")
    w("## 4. Results (released defaults; 'strike' = the indicator's 1 set to 0)")
    w("")
    w("Aggregates are the notebook's `overall_credence` (sum_i P(L*=i) P(C_i|e)), mean over draws with the 89% HDI. "
      "**The block's 'Level 1-2-heavy weighting' is not defined in the block, the note, or the notebook**; the only "
      "non-equal credence vector in the notebook is cell 28's illustrative (0.3, 0.2, 0.1, 0.3, 0.1), which puts 0.5 "
      "on Levels 1-2 (and 0.3 on Level 4); it is shown as `cell-28 vector` for reference, not as the block's weighting. "
      "The column `L1-2 only` is the equal split (0.5, 0.5, 0, 0, 0). It is the midpoint of the weightings that put "
      "all their weight on Levels 1-2, not a bound on them: for w = (t, 1-t, 0, 0, 0) the aggregate is "
      "t x C1 + (1-t) x C2, so across those weightings it runs from C2 (all on Level 2) to C1 (all on Level 1); the "
      "range table after the bullets gives both ends per condition. Because the aggregate is linear in the "
      "credences, any other weighting w gives sum_i w_i x C_i from the row (the JSON carries 6+ decimals).")
    w("")
    w("| condition | yes per level | C1 | C2 (computational) | C3 | C4 | C5 | equal credences [89% HDI] | cell-28 vector | L1-2 only |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for key, r in results.items():
        a = r["aggregates"]
        pl = r["per_level_mean"]
        w(f"| {key}: {r['description']} | {r['yes_per_level']} | " + " | ".join(f3(x) for x in pl) +
          f" | {f3(a['equal']['mean'])} [{f3(a['equal']['hdi89'][0])}, {f3(a['equal']['hdi89'][1])}] | "
          f"{f3(a['notebook_cell28']['mean'])} | {f3(a['L1L2_only']['mean'])} |")
    w("")
    b = results["baseline"]
    for key in ("strike_meta_L2", "strike_coupling", "unscored_meta_L2", "unscored_coupling"):
        r = results[key]
        w(f"- {key}: C1 {f6(b['per_level_mean'][0])} -> {f6(r['per_level_mean'][0])}; "
          f"C2 {f6(b['per_level_mean'][1])} -> {f6(r['per_level_mean'][1])} "
          f"(89% HDI [{f3(r['per_level_hdi89'][1][0])}, {f3(r['per_level_hdi89'][1][1])}]); "
          f"equal-credence aggregate {f6(b['aggregates']['equal']['mean'])} -> {f6(r['aggregates']['equal']['mean'])} "
          f"(change {r['aggregates']['equal']['mean'] - b['aggregates']['equal']['mean']:+.6f}); "
          f"cell-28 {f6(b['aggregates']['notebook_cell28']['mean'])} -> {f6(r['aggregates']['notebook_cell28']['mean'])}; "
          f"L1-2 only {f6(b['aggregates']['L1L2_only']['mean'])} -> {f6(r['aggregates']['L1L2_only']['mean'])}.")
    w("")
    w("Weightings on Levels 1-2 only, w = (t, 1-t, 0, 0, 0): the aggregate at both ends and at the midpoint, and the "
      "change from baseline at both ends (the change at any t lies between them):")
    w("")
    w("| condition | all on Level 2 (t = 0; = C2) | midpoint (0.5, 0.5) | all on Level 1 (t = 1; = C1) | "
      "change vs baseline, all on Level 2 | change vs baseline, all on Level 1 |")
    w("|---|---|---|---|---|---|")
    for key, rr in l12_range.items():
        w(f"| {key} | {f6(rr['all_level2'])} | {f6(rr['midpoint_0.5_0.5'])} | {f6(rr['all_level1'])} | "
          f"{rr['change_vs_baseline_all_level2']:+.6f} | {rr['change_vs_baseline_all_level1']:+.6f} |")
    w("")
    w("Per-level evidence, log10 of P(e_level | C_i = 1) / P(e_level | C_i = 0) (theta-independent):")
    w("")
    w("| condition | L1 | L2 | L3 | L4 | L5 |")
    w("|---|---|---|---|---|---|")
    for key in ("baseline", "strike_meta_L2", "strike_coupling"):
        w(f"| {key} | " + " | ".join(f"{x:+.3f}" for x in results[key]["log10_LR_per_level"]) + " |")
    w("")
    lr_c = (1 - COUP["alpha"]) / (1 - COUP["beta"]) / (COUP["alpha"] / COUP["beta"])
    lr_m = (1 - META2["alpha"]) / (1 - META2["beta"]) / (META2["alpha"] / META2["beta"])
    w(f"A strike multiplies its level's likelihood ratio by ((1-a)/(1-b)) / (a/b): coupling (a={COUP['alpha']}, "
      f"b={COUP['beta']}) {lr_c:.4f}; Level 2 metacognition (a={META2['alpha']}, b={META2['beta']}) {lr_m:.4f}.")
    w("")
    w("## 5. Diagnostic (post-hoc, computed-new): is the coupling strike inert because of its beta?")
    w("")
    w("The coupling indicator's (alpha, beta) is replaced, with everything else at defaults, and the strike rerun:")
    w("")
    w("| coupling (alpha, beta) | baseline C1 | struck C1 | baseline aggregate (equal) | struck aggregate (equal) |")
    w("|---|---|---|---|---|")
    w(f"| released ({COUP['alpha']}, {COUP['beta']}) | {f6(b['per_level_mean'][0])} | "
      f"{f6(results['strike_coupling']['per_level_mean'][0])} | {f6(b['aggregates']['equal']['mean'])} | "
      f"{f6(results['strike_coupling']['aggregates']['equal']['mean'])} |")
    for tag, c in cf.items():
        w(f"| {tag} ({c['alpha']}, {c['beta']}) | {f6(c['baseline']['per_level_mean'][0])} | "
          f"{f6(c['strike']['per_level_mean'][0])} | {f6(c['baseline']['aggregates']['equal']['mean'])} | "
          f"{f6(c['strike']['aggregates']['equal']['mean'])} |")
    w("")

    def mult(a_, b_):
        return (1 - a_) / (1 - b_) / (a_ / b_)
    rel_ratio = (1 - COUP["alpha"]) / (1 - COUP["beta"])
    w("Why each counterfactual row's struck values are what they are. A struck indicator (e = 0) contributes "
      "(1 - alpha) to its level's likelihood when C1 = 1 and (1 - beta) when C1 = 0, and the posterior depends only "
      "on their ratio (the level's common factor cancels when the posterior is normalised). So two (alpha, beta) "
      "pairs with the same (1 - alpha)/(1 - beta) give the same struck posterior, whatever their unstruck values.")
    w("")
    for tag, c in cf.items():
        r_ = (1 - c["alpha"]) / (1 - c["beta"])
        same = abs(r_ - rel_ratio) < 1e-12
        dpl = max(abs(x - y) for x, y in zip(c["strike"]["per_level_mean"],
                                             results["strike_coupling"]["per_level_mean"]))
        dag = abs(c["strike"]["aggregates"]["equal"]["mean"] - results["strike_coupling"]["aggregates"]["equal"]["mean"])
        w(f"- {tag}: (1 - alpha)/(1 - beta) = {1 - c['alpha']:.2f}/{1 - c['beta']:.2f} = {r_:.4f}, against "
          f"{1 - COUP['alpha']:.2f}/{1 - COUP['beta']:.2f} = {rel_ratio:.4f} as released"
          + (f" -- the same ratio, so its struck row equals the released struck row (largest per-level difference "
             f"{dpl:.1e}, aggregate difference {dag:.1e}: floating-point rounding, not a copy). Its baseline differs "
             f"(alpha/beta = {c['alpha'] / c['beta']:.2f} against {COUP['alpha'] / COUP['beta']:.2f} as released), "
             f"so the strike here multiplies the Level 1 likelihood ratio by {mult(c['alpha'], c['beta']):.4f}, "
             f"against {mult(COUP['alpha'], COUP['beta']):.4f} as released (it divides the ratio by "
             f"{1 / mult(c['alpha'], c['beta']):.1f} instead of {1 / mult(COUP['alpha'], COUP['beta']):.1f}), and "
             f"still leaves the aggregate at {f3(c['strike']['aggregates']['equal']['mean'])}. The row is a real "
             f"test of the diagnostic, not a duplicate."
             if same else
             f"; the strike multiplies the Level 1 likelihood ratio by {mult(c['alpha'], c['beta']):.4f}, against "
             f"{mult(COUP['alpha'], COUP['beta']):.4f} as released, and the struck aggregate is "
             f"{f6(c['strike']['aggregates']['equal']['mean'])}."))
    w("")
    w("## 6. Robustness (equal credences)")
    w("")
    w("| condition | " + " | ".join(rob["baseline"].keys()) + " |")
    w("|---|" + "---|" * len(rob["baseline"]))
    for key, row in rob.items():
        w(f"| {key} | " + " | ".join(f3(v["aggregates"]["equal"]["mean"]) for v in row.values()) + " |")
    w("")
    k7 = "generalised " + ROOT_CELL7[0] + " [cell 7]"
    w(f"- The four `generalised` Beta(a,b) columns are `truth.py`'s root-prior sweep. The `{k7}` column is not in "
      f"the sweep: notebook cell 7 (markdown) says the uniform Beta(1,1) was used but advises users to also try "
      f"\"{CELL7_ADVICE}\". Its means: " + "; ".join(
          f"{key} {f6(row[k7]['aggregates']['equal']['mean'])} [89% HDI {f3(row[k7]['aggregates']['equal']['hdi89'][0])}, "
          f"{f3(row[k7]['aggregates']['equal']['hdi89'][1])}]" for key, row in rob.items()) + ".")
    for key, s in seeds.items():
        w(f"- Monte Carlo spread, {key}, seeds {s['seeds']} at N_DRAWS = {N_DRAWS}: equal-credence aggregate "
          f"min {f6(s['min'])}, max {f6(s['max'])}.")
    w("")
    J["_md_sections_done"] = True

    # ---- verdicts against the note ----
    sc_ = results["strike_coupling"]["aggregates"]["equal"]["mean"]
    moves = abs(sc_ - base_eq)
    base3 = f3(base_eq)
    sweep_base = {k: f3(v["aggregates"]["equal"]["mean"]) for k, v in rob["baseline"].items()}
    gen_all_0394 = all(v == "0.394" for k, v in sweep_base.items() if k.startswith("generalised"))
    gen_txt = ("0.394 at all four shapes of `truth.py`'s sweep and at cell 7's Beta(1/2,1/2)" if gen_all_0394
               else str(sweep_base))
    seed_all_0394 = f3(seeds["baseline"]["min"]) == "0.394" and f3(seeds["baseline"]["max"]) == "0.394"
    cf_struck = {t: c["strike"]["aggregates"]["equal"]["mean"] for t, c in cf.items()}
    cf_all_inert = all(f3(v) == base3 for v in cf_struck.values())
    verdicts = [
        ("0.394 (LLM-optimist, equal level credences, released defaults)",
         "reproduced" if (port_ok and base3 == "0.394") else "discrepant",
         f"CONFIRMS. Notebook cell 31's stored output and this port both give {base3} [89% HDI "
         f"{f3(b['aggregates']['equal']['hdi89'][0])}, {f3(b['aggregates']['equal']['hdi89'][1])}] (mean {f6(base_eq)}). "
         f"Root priors (generalised): {gen_txt}; strict model "
         f"Beta(1,1): {sweep_base['strict Beta(1,1)']}; seeds 0..19: "
         f"{'all round to 0.394' if seed_all_0394 else 'not all 0.394'} ({f6(seeds['baseline']['min'])} to "
         f"{f6(seeds['baseline']['max'])})"),
        ("0.70 (coupling indicator's false-positive rate; 'weakly undemanding')",
         "reproduced" if (COUP["beta"] == 0.7 and COUP["demandingness"] == "weakly undemanding" and wu_beta == 0.70)
         else "discrepant",
         f"CONFIRMS. CSV row j={COUP['j']} `prior beta` {COUP['beta']}, demandingness `{COUP['demandingness']}`; "
         f"mapping.md:{wu_line[0][0]} (Weakly undemanding -> 0.70); cell 6 displays 0.70. The note's gloss (the model "
         f"expects coupling reports in systems that are not conscious) matches mapping.md's reading of beta as background "
         f"prevalence; in the network beta conditions on the Level 1 node C1 = 0"),
        ("'Striking the behavioral coupling indicator ... moves nothing' (coupling set to 0)",
         "computed-new",
         f"CONFIRMS. Equal-credence aggregate {f6(base_eq)} -> {f6(sc_)} (|change| {moves:.2e}; {base3} -> {f3(sc_)}); "
         f"C1 {f6(b['per_level_mean'][0])} -> {f6(results['strike_coupling']['per_level_mean'][0])}"),
        ("'... because that indicator is scored as weakly undemanding (false-positive rate 0.70)'",
         "computed-new",
         ("THE NOTE'S CLAUSE DOES NOT HOLD ON THIS VECTOR: the 0.70 is not why the strike moves nothing. "
          "Why: with the coupling indicator given a demanding false-positive rate instead (0.10, the fallback pair; "
          "0.30, the Level 2 metacognition pair), the strike is still inert: struck aggregate "
          + "; ".join(f"{t} {f6(v)}" for t, v in cf_struck.items())
          + f", all {base3} (section 5). The strike is inert because the vector's other Level 1 answers already put C1 "
          f"at {f6(b['per_level_mean'][0])} (Level 1 log10 likelihood ratio {b['log10_LR_per_level'][0]:+.3f}; "
          f"{results['strike_coupling']['log10_LR_per_level'][0]:+.3f} after the strike), so C1 is saturated whatever "
          f"the indicator's beta. The 0.70 does make the indicator low-leverage in general (a strike multiplies the "
          f"Level 1 likelihood ratio by {lr_c:.4f}, against {lr_m:.4f} for Level 2 metacognition), but that is not what "
          f"decides the result here. Status: the number in the clause (0.70) is reproduced in the row above; this row "
          f"tests only the clause's 'because', by a diagnostic added after the results were seen, so under rule 11 it "
          f"is computed-new (post-hoc: it flags, it does not adjudicate). Whether the row should read discrepant "
          f"instead is the PI's call. Whoever carries this row must carry this sentence with the status")
         if cf_all_inert else
         ("PARTLY: the counterfactual parameterisations move the struck aggregate: "
          + "; ".join(f"{t} {f6(v)}" for t, v in cf_struck.items()))),
    ]
    extras = ({3: {"note_clause_holds": False, "post_hoc": True,
                   "flag": "the note's 'because' clause does not hold on this vector; status computed-new under rule 11; "
                           "discrepant vs computed-new is the PI's call"}}
              if cf_all_inert else {3: {"note_clause_holds": "partly", "post_hoc": True}})
    J["verdicts"] = [{"claim": c, "status": s, "basis": t} | extras.get(i, {}) for i, (c, s, t) in enumerate(verdicts)]
    w("## 7. Against the note's section 8 (lines 140-149)")
    w("")
    w("| note claim | status | basis |")
    w("|---|---|---|")
    for c, s, t in verdicts:
        w(f"| {c} | {s} | {t} |")
    w("")
    w(f"- Metacognition strike: section 8 of the note (v0.3) withdraws the what-if and carries no number for it, so "
      f"this run has nothing in section 8 to confirm or correct there (note line {gap_lines[0]} still leans on it: "
      f"see section 8 below, post-hoc). The block's figures are in section 4 for the record "
      f"(computed-new): computational-level posterior C2 {f3(b['per_level_mean'][1])} -> "
      f"{f3(results['strike_meta_L2']['per_level_mean'][1])}; aggregate {f3(base_eq)} -> "
      f"{f3(results['strike_meta_L2']['aggregates']['equal']['mean'])} under equal credences.")
    w(f"- Coupling strike: the note's verify brackets (lines {', '.join(str(x) for x in set0_lines)}) describe the "
      f"re-run as setting the coupling indicator to 0; this run does exactly that (section 4, `strike_coupling`).")
    w("")
    w("Numerals in section 8, with whether this item bears on them:")
    w("")
    tags = {"0.394": "N19: reproduced (above)", "0.70": "N19: reproduced (above)",
            "0": "N19: the bracket's 'set to 0' -- the procedure this run follows"}
    for n in numerals:
        if n["line"] == 144 and n["token"] in tags:
            tag = tags[n["token"]]
        elif n["line"] == 140:
            tag = "section number; not a figure"
        elif n["line"] in (144, 148) and n["token"] in ("4", "5"):
            tag = "a link or level label; not a figure"
        else:
            tag = "outside N19: not from the companion code (N1's ledger)"
        n["n19"] = tag
        w(f"- line {n['line']}: `{n['token']}` -- {tag}")
    w("")

    # ---- section 8: POST-HOC gap share (checker finding 1) ----
    def pc(x):   # one decimal; shares that would print as 0.0% keep two significant figures
        return f"{100 * x:.2g}%" if 0 < abs(100 * x) < 0.05 else f"{100 * x:.1f}%"
    sh = shares
    n_diff = int((opt != scep).sum())
    gm = gap_max
    w(f"## 8. POST-HOC -- not in the block's procedure; flagged, not adopted: do the two indicators carry most of "
      f"the optimist-sceptic gap? (note line {gap_lines[0]})")
    w("")
    w(f"Added after the results were seen, at the checker's flag. Under rule 11 (CLAUDE.md ledger: post-hoc analyses "
      f"license pre-registrations, never verdicts) it supports a sentence for the design seat and the PI, not a verdict. Note line {gap_lines[0]} says the note will show, on the "
      f"framework's released model, that \"the two indicators my data bear on {NOTE_GAP_PHRASE}\". The two "
      f"indicators are Level 1 coupling (j={COUP['j']}, link 5) and Level 2 `Meta-cognition` (j={META2['j']}, "
      f"link 4). Both are 1 in `LLM-optimist` and 0 in `LLM-sceptic` (notebook cell 31); the two vectors differ on "
      f"{n_diff} of the 37 indicators. Share of the gap closed = (optimist - optimist with the indicator(s) struck) / "
      f"(optimist - sceptic), at the released defaults on the same 5000 draws. The last column runs the other way: "
      f"(sceptic with both set to 1 - sceptic) / (optimist - sceptic).")
    w("")
    w("| weighting | optimist | sceptic | gap | optimist, both struck | share closed by both | metacognition (j=14) "
      "alone | coupling (j=7) alone | other way: sceptic + both |")
    w("|---|---|---|---|---|---|---|---|---|")
    wlabel = {"equal": "equal credences", "notebook_cell28": "cell-28 credences (0.3, 0.2, 0.1, 0.3, 0.1)",
              "L1L2_only": "Levels 1-2 only (0.5, 0.5, 0, 0, 0)"}
    for wname, row in sh.items():
        w(f"| {wlabel[wname]} | {f6(row['optimist'])} | {f6(row['sceptic'])} | {f6(row['gap'])} | "
          f"{f6(row['optimist_strike_both']['aggregate'])} | **{pc(row['optimist_strike_both']['share_of_gap_closed'])}** | "
          f"{pc(row['optimist_strike_meta_L2']['share_of_gap_closed'])} | "
          f"{pc(row['optimist_strike_coupling']['share_of_gap_closed'])} | "
          f"{pc(row['sceptic_add_both']['share_of_gap_closed'])} |")
    w("")
    w("Maximum over weightings. The aggregate is linear in the credences, so the share is a ratio of two linear "
      "functions of the weighting and its maximum lies at a vertex: all weight on one level, or (with a floor on "
      "the gap) the point where an edge of the simplex meets the floor. Per level (all weight on that level):")
    w("")
    w("| all weight on | optimist C_i | sceptic C_i | gap | closed by both | share |")
    w("|---|---|---|---|---|---|")
    ps_ = gres["sceptic"]["per_level_mean"]
    for v in vertices:
        i = v["level"] - 1
        w(f"| Level {v['level']} | {po[i]:.6g} | {ps_[i]:.6g} | {v['gap']:.3g} | {v['closed']:.3g} | {pc(v['share'])} |")
    w("")
    g12, gt, gu = gm["levels_1_2_only"], gm["gap_at_least_tau"], gm["unrestricted"]
    w(f"- Weightings on Levels 1-2 only: at most {pc(g12['share'])} (all weight on Level {g12['level']}).")
    w(f"- Every weighting whose aggregate gap is at least {GAP_TAU} (the aggregates' reported precision; a smaller "
      f"gap shows in no reported verdict): at most {pc(gt['share'])}, at w = "
      f"({', '.join(f'{x:.4g}' for x in gt['weights'])}), where the gap is {gt['gap_at_max']:.4g}. That maximiser "
      f"puts just enough weight on Level 2 to meet the floor and the rest where there is no gap; its share is Level "
      f"2's {pc(vertices[1]['share'])} moved by near-zero terms. The value depends on the floor: it rises towards "
      f"the unrestricted ratio below as the floor goes to 0.")
    lv35 = [v for v in vertices if v["level"] >= 3]
    w(f"- Unrestricted: the largest ratio is {pc(gu['share'])}, with all weight on Level {gu['level']}. At Levels 3-5 "
      f"both verdicts are already near zero (optimist at most {max(po[2:]):.1e}, sceptic at most {max(ps_[2:]):.1e}) "
      f"and the gap is at most {max(v['gap'] for v in lv35):.1e}, so a ratio there divides one near-zero number by "
      f"another. There is no gap there to carry.")
    w("")
    eq_, c28_, l12_ = (sh[k]["optimist_strike_both"]["share_of_gap_closed"] for k in ("equal", "notebook_cell28", "L1L2_only"))
    coup_eq = sh["equal"]["optimist_strike_coupling"]["share_of_gap_closed"]
    rev_eq = sh["equal"]["sceptic_add_both"]["share_of_gap_closed"]
    contradicts = max(eq_, c28_, l12_, gt["share"], rev_eq) <= 0.5
    posthoc_gap["contradicts_note_line"] = contradicts
    if contradicts:
        w(f"**This contradicts note line {gap_lines[0]} (\"{NOTE_GAP_PHRASE}\"), reading 'most' as more than half.** "
          f"Striking both indicators closes {pc(eq_)} of the gap under equal credences, {pc(c28_)} under the "
          f"cell-28 credences and {pc(l12_)} under (0.5, 0.5, 0, 0, 0). With all weight on Level 2, the most "
          f"favourable level that has a gap to close, it closes {pc(g12['share'])}; under any weighting with a gap of at least {GAP_TAU}, at "
          f"most {pc(gt['share'])}. Run the other way, adding both to the sceptic closes {pc(rev_eq)}. The coupling "
          f"indicator alone closes {pc(coup_eq)} under equal credences. Section 8 of the note (line {wd_lines[0]}) "
          f"already withdraws the metacognition strike, which supplies almost all of what the pair closes; so on the "
          f"note's own terms line {gap_lines[0]} has {pc(coup_eq)} behind it. The line has no numeral of its own.")
    else:
        w(f"**Mixed against note line {gap_lines[0]}:** at least one reading closes more than half of the gap "
          f"(equal {pc(eq_)}, cell-28 {pc(c28_)}, Levels 1-2 {pc(l12_)}, floor-restricted maximum {pc(gt['share'])}, "
          f"other way {pc(rev_eq)}).")
    w("")
    w("This is a sentence for the design seat and the PI. It is not adopted, and N19 edits no note text.")
    w("")

    # ---- section 9: values-check ----
    rng = l12_range
    w("## 9. Values-check (checker's findings on this raw, and their dispositions)")
    w("")
    w("Changes at the values-check: wording, plus the rows, columns and sections listed below. No computation "
      "that produced an earlier figure was altered.")
    w("")
    n1_txt = (f" One correction to the flag: the checker said N1's numeral matcher cannot catch line "
              f"{gap_lines[0]}, since it has no numerals. But N1 final's note rows (`{N1_FINAL}`) already carry "
              f"note:{gap_lines[0]} as row {n1_ref['rows_note_line'][0]}, matched on the word 'two', and N1's "
              f"{n1_ref['span_note']} calls the line stale. What N19 adds is the number.")
    w(f"1. **HIGH (note line {gap_lines[0]}): APPLIED** as section 8, labelled post-hoc. Striking both indicators "
      f"closes {pc(eq_)} of the gap under equal credences, {pc(c28_)} under cell-28 and {pc(l12_)} under Levels 1-2 "
      f"only. The maximum is {pc(gt['share'])} (gap at least {GAP_TAU}) or {pc(g12['share'])} (Levels 1-2 only), and "
      f"coupling alone closes {pc(coup_eq)}. This raw's section 8 states plainly that this contradicts the line's 'carry most "
      f"of the gap'. It is a sentence for the design seat and the PI, not adopted.{n1_txt}")
    w(f"2. **LOW-MEDIUM: APPLIED.** Section 4 no longer says (0.5, 0.5, 0, 0, 0) bounds the Levels 1-2 weightings. "
      f"It now calls it the midpoint and adds a range table. Over those weightings the aggregate runs from "
      f"{f6(rng['baseline']['all_level2'])} to {f6(rng['baseline']['all_level1'])} at baseline, from "
      f"{f6(rng['strike_meta_L2']['all_level2'])} to {f6(rng['strike_meta_L2']['all_level1'])} after the "
      f"metacognition strike, and from {f6(rng['strike_coupling']['all_level2'])} to "
      f"{f6(rng['strike_coupling']['all_level1'])} after the coupling strike. The metacognition strike's change "
      f"runs from {rng['strike_meta_L2']['change_vs_baseline_all_level1']:+.6f} (all on Level 1) to "
      f"{rng['strike_meta_L2']['change_vs_baseline_all_level2']:+.6f} (all on Level 2).")
    w(f"3. **LOW: APPLIED.** Section 1 and the script's docstring no longer say 'numpy only'. The interpreter has "
      f"{have}; {lack} {lack_verb} absent. The JSON records this under "
      f"`interpreter_packages`. The port's justification is kept on two grounds: the absent packages are imported at "
      f"top level by notebook cell 1, and running the notebook would execute the clone's `dcm_lab` package in any "
      f"case.")
    w("4. **LOW, for the PI: APPLIED.** The 'because ... weakly undemanding' row keeps the status computed-new, "
      "because the diagnostic is post-hoc (rule 11). Its basis now opens by saying that the note's clause does not "
      "hold on this vector, and says why: C1 is saturated by the vector's other Level 1 answers, and a demanding "
      "beta is just as inert. The JSON row carries `note_clause_holds: false` and a `flag`, so a carrier that keeps "
      "only structured fields still sees it. Discrepant versus computed-new remains the PI's call.")
    fb = cf["coupling_as_fallback_0.73_0.10"]
    w(f"5. **INFO: APPLIED.** Section 5 now explains why the (0.73, 0.10) row's struck values equal the released "
      f"struck row's ({f6(fb['strike']['aggregates']['equal']['mean'])}; C1 {f6(fb['strike']['per_level_mean'][0])}): "
      f"(1 - alpha)/(1 - beta) = {rel_ratio:.2f} in both, and a struck indicator enters the posterior only through "
      f"that ratio. "
      f"The baselines differ, so there the strike divides the Level 1 likelihood ratio by "
      f"{1 / mult(fb['alpha'], fb['beta']):.1f}, against {1 / mult(COUP['alpha'], COUP['beta']):.1f} as released. "
      f"The diagnostic stands.")
    w(f"6. **INFO: APPLIED.** Section 6 adds the Beta(1/2,1/2) root prior advised in notebook cell 7: "
      + "; ".join(f"{key} {f6(row[k7]['aggregates']['equal']['mean'])}" for key, row in rob.items())
      + ". 0.394 holds.")
    w("")
    w("The builder's own flagged findings: (B1) 'Level 1-2-heavy weighting' is undefined. Kept in section 4, with "
      "the wording correction of finding 2. (B2) The 'because' clause is the same row as finding 4, disposed of "
      "there. (B3) `README-NOTE.md` and N1's provisional ledger rows L159/L160 still say N19 is 'not run'. Those are "
      "not N19's files and are unchanged here; they are for N1 final once this raw is committed.")
    w("")
    md_text = "\n".join(md) + "\n"
    J.pop("_md_sections_done", None)

    os.makedirs(os.path.dirname(os.path.join(root, args.out_md)), exist_ok=True)
    with open(os.path.join(root, args.out_json), "w", encoding="utf-8") as f:
        json.dump(J, f, indent=1)
        f.write("\n")
    with open(os.path.join(root, args.out_md), "w", encoding="utf-8") as f:
        f.write(md_text)
    print(md_text)


if __name__ == "__main__":
    main()
