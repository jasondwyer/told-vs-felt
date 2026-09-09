"""PROPOSAL-k §1.3-§1.5 -- Stage 1 probes, gates G1-G5, and the pre-written
outcome sentences. Model-free. Every bar is the proposal's, fixed here by
name; the analyzer selects a sentence, the design seat confirms it.

Probes (§1.3): standardized L2 logistic regression with the published
hyperparameters (`echo.probe.fit_lr`); grouped leave-one-session-out CV
(both rows of a session held out together); AUC per layer; 200 label
shuffles per layer for the null (95th percentile); text-only baseline from
the M0 rows.

Targets and rows (A = the first-listed menu label, B = the second):
  G1  "this label's block carried +" at that label's own token:
        at A's token: rows M+A (y = 1) and M+B (y = 0)
        at B's token: rows M+B (y = 1) and M+A (y = 0)
      comparator R+A / R+B likewise (reported, not a bar).
  G2  the same target at the READ position: rows M+A (y = 1) / M+B (y = 0).
  G3  "the FIRST block carried +" at the read position over M+A U M+B rows:
      y = 1 iff the steered label is the first-block label. The second
      block's sign is reported beside: over these two masks it is the
      complement target, probed and nulled independently (so not identical
      by construction -- the LR init is not label-symmetric).
  DOMAIN (rule 28(a), declared): the gates are evaluated over VALID sessions
      (not excluded under the run scope) that reached a first free choice;
      the all-with-a-first-pick figure is reported beside (rule 23). Stage
      C read valid sessions only; the reads stage records every session with
      a first pick and labels the excluded ones.
  Text-only baselines: the M0 (shadow) rows at the same position with the
  only text-borne asymmetry these sessions carry as the target -- whether
  label A's block came FIRST (start order). The recon's text-only rows used
  the as-generated pole; sham sessions have none. Declared, design confirms.
  G4  leak on R+A, R+B, M++, R++: paired-shadow discordance with a
      Clopper-Pearson interval; |Δ logit-diff|; the signed shift toward the
      FIRST block's label on the R masks. PROHIBITION: nothing signed on
      M+A / M+B -- asserted by name.
  G5  the identity baseline from the sessions' own recorded vanilla first
      picks: per-pair share on each label with exact binomial intervals; the
      alternation and stay rates over all sessions (rule 23).
"""

from __future__ import annotations

import json
import math
import os
import re
from typing import Mapping, Sequence

import numpy as np

from ..adapters.base import sha16_arr
from ..e2d import habit as H
from ..e2d.config import REPO
from ..echo.probe import loso_auc, shuffle_null
from ..stats import binom_cdf

# --- the proposal's bars, fixed (§1.4) ---------------------------------------
G1_BAND = tuple(range(51, 62))         # L51-L61
G1_MEDIAN_A, G1_MEDIAN_B = 0.90, 0.75
G2_LAYERS = tuple(range(49, 64))       # L49-L63
G2_PRESENT_MIN_LAYERS = 3
G3_BAND = tuple(range(51, 63))         # L51-L62
G3_MEDIAN = 0.90
N_SHUFFLES = 200
SHUFFLE_SEED = 20260909

SENTENCES = {
    "ABSENT": ("On new sessions in the format of record the state–label binding is linearly present at the label token and absent "
               "at the decision token, and the first block's sign reaches the decision token: the echo channel is open for the sign "
               "and closed for the binding. Stage 2 runs under F-ABSENT."),
    # §1.5 writes this sentence with a leading ellipsis; the ellipsis is expanded with the ABSENT sentence's
    # opening ("On new sessions in the format of record") and NOTHING else -- declared, design confirms.
    "PRESENT": ("On new sessions in the format of record the binding is present at both the label token and the decision "
                "token in this format. Stage 2 runs under F-PRESENT after LOCK-k bounds the binding's arithmetic route."),
    # §1.5 gives an instruction, not a sentence ("as ABSENT, with the indeterminacy named in every §3 sentence"):
    # the ABSENT sentence with the instruction's clause appended -- a COMPOSITION, declared; design confirms or authors.
    "INDETERMINATE": ("On new sessions in the format of record the state–label binding is linearly present at the label token and absent "
                      "at the decision token, and the first block's sign reaches the decision token: the echo channel is open for the sign "
                      "and closed for the binding. Stage 2 runs under F-ABSENT, with the G2 indeterminacy named in every §3 sentence."),
    "G3_FAIL": ("The injected sign does not reach the decision token in this format at f = 0.10. The channel is not verifiably open; "
                "Stage 2 does not run. Concluded, not answered. The next move is a design change (retention interval, dose rung < 0.20, "
                "or format), by new addendum."),
    "G1_FAIL": ("The binding is not readable at the label token in this format, though it was in e2a's (recon). Stage 2 runs only as a "
                "sign-memory operant under F-ABSENT; the binding question is reported as not replicated and returns to the drawer."),
    "STOP": "Any assertion failure (identity, mask-at-read, provenance): STOP; no gate is evaluated; Code reports; design adjudicates.",
}
SENTENCE_PROVENANCE = {"ABSENT": "verbatim §1.5", "G3_FAIL": "verbatim §1.5", "G1_FAIL": "verbatim §1.5", "STOP": "verbatim §1.5 (last bullet)",
                       "PRESENT": "§1.5 with its leading ellipsis expanded by the ABSENT sentence's opening only (declared)",
                       "INDETERMINATE": "COMPOSED per §1.5's instruction 'as ABSENT, with the indeterminacy named in every §3 sentence' (declared; design confirms or authors)"}


def proposal_sentences(path: str) -> dict:
    """§1.5's sentences as they stand in the proposal file, whitespace-normalised, keyed by branch."""
    txt = open(path, encoding="utf-8").read()
    sec = txt.split("### 1.5", 1)[1].split("### 1.6", 1)[0]
    quotes = re.findall(r"\*\"(.+?)\"\*", sec, re.S)
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    out = {"ABSENT": norm(quotes[0]), "PRESENT_with_ellipsis": norm(quotes[1]), "G3_FAIL": norm(quotes[2]), "G1_FAIL": norm(quotes[3])}
    m = re.search(r"Any assertion failure.*?design adjudicates\.", sec, re.S)
    out["STOP"] = norm(m.group(0)) if m else None
    return out


def clopper_pearson(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact binomial interval by inverting `stats.binom_cdf` on a grid-free bisection."""
    if n == 0:
        return (0.0, 1.0)
    def upper_of(k):
        if k == n:
            return 1.0
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if binom_cdf(k, n, mid) > alpha / 2:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    def lower_of(k):
        if k == 0:
            return 0.0
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if 1 - binom_cdf(k - 1, n, mid) < alpha / 2:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2
    return (lower_of(k), upper_of(k))


# --- loading ------------------------------------------------------------------
REQUIRED_MASKS = ("M+A", "M+B", "R+A", "R+B", "M++", "R++")


def assertion_failures(meta: Mapping) -> list[str]:
    """Every §1.5 assertion class the analyzer can see: identity, completeness,
    a missing mask, a missing or mismatched array. Non-empty -> STOP."""
    fails = []
    if not meta.get("complete", False):
        fails.append("reads artifact not complete")
    for sid, r in meta.get("per_session", {}).items():
        for m in REQUIRED_MASKS:
            if m not in r.get("masks", {}):
                fails.append(f"s{sid}: mask {m} missing"); continue
            if not r["masks"][m].get("identity", {}).get("ok", False):
                fails.append(f"s{sid} {m}: identity assertion failed")
        p = os.path.join(REPO, r.get("npz", ""))
        if not r.get("npz") or not os.path.exists(p):
            fails.append(f"s{sid}: npz missing"); continue
        keys = set(np.load(p).files)
        for m in REQUIRED_MASKS:
            if f"{m}|state" not in keys:
                fails.append(f"s{sid}: array {m}|state missing")
        if "M0|shadow" not in keys:
            fails.append(f"s{sid}: array M0|shadow missing")
    return fails


def load_stacks(meta: Mapping, layers: Sequence[int] | None = None, verify_fingerprints: bool = True,
                domain: str = "valid") -> dict:
    """`domain`: 'valid' (not excluded under the run scope; the gates' domain) or 'all' (every session with a first pick)."""
    sess = sorted(meta["per_session"].values(), key=lambda r: r["session"])
    if domain == "valid":
        sess = [r for r in sess if not r.get("excluded", False)]
    elif domain != "all":
        raise ValueError(domain)
    layers_all = None
    stacks: dict = {}
    for r in sess:
        z = np.load(os.path.join(REPO, r["npz"]))
        if layers_all is None:
            layers_all = [int(x) for x in z["layers"]]
        keys = [k for k in z.files if k not in ("layers", "positions")]
        for k in keys:
            arr = z[k]
            if verify_fingerprints and sha16_arr(arr) != r["npz_sha16_by_key"][k]:
                raise SystemExit(f"fingerprint mismatch s{r['session']} {k}")
            for i, l in enumerate(layers_all):
                if layers is not None and l not in layers:
                    continue
                for pi, pn in enumerate(("read", "label_a", "label_b")):
                    stacks.setdefault((k, pn, l), []).append(arr[pi, i])
    stacks = {k: np.stack(v) for k, v in stacks.items()}
    return {"sessions": sess, "domain": domain, "n_sessions": len(sess),
            "layers": layers_all if layers is None else [l for l in layers_all if l in layers], "stacks": stacks}


def families(loaded: Mapping) -> dict:
    """{name: fn(layer) -> (X, groups, y)}. Row order inside each family is
    fixed and documented; y is the target named in the module docstring."""
    sess = loaded["sessions"]; S = loaded["stacks"]
    groups = np.array([r["session"] for r in sess])
    a_first = np.array([1 if r["a_is_first_block"] else 0 for r in sess])
    def two(ma, mb, pn, l):
        return np.concatenate([S[(f"{ma}|state", pn, l)], S[(f"{mb}|state", pn, l)]]), np.r_[groups, groups]
    N = len(sess)
    fam = {}
    # G1 at each label's own token; comparator on the random direction
    fam["g1_labelA_token_M"] = lambda l: (*two("M+A", "M+B", "label_a", l), np.r_[np.ones(N), np.zeros(N)])
    fam["g1_labelB_token_M"] = lambda l: (*two("M+B", "M+A", "label_b", l), np.r_[np.ones(N), np.zeros(N)])
    fam["g1_labelA_token_R_comparator"] = lambda l: (*two("R+A", "R+B", "label_a", l), np.r_[np.ones(N), np.zeros(N)])
    fam["g1_labelB_token_R_comparator"] = lambda l: (*two("R+B", "R+A", "label_b", l), np.r_[np.ones(N), np.zeros(N)])
    # G2 at the read position (same target: A's block carried +)
    fam["g2_read_M"] = lambda l: (*two("M+A", "M+B", "read", l), np.r_[np.ones(N), np.zeros(N)])
    fam["g2_read_R_comparator"] = lambda l: (*two("R+A", "R+B", "read", l), np.r_[np.ones(N), np.zeros(N)])
    # G3 first-block sign at the read: rows M+A (y = a_first) and M+B (y = 1 - a_first)
    fam["g3_firstsign_read_M"] = lambda l: (*two("M+A", "M+B", "read", l), np.r_[a_first, 1 - a_first])
    fam["g3_secondsign_read_M_beside"] = lambda l: (*two("M+A", "M+B", "read", l), np.r_[1 - a_first, a_first])
    fam["g3_firstsign_read_R_comparator"] = lambda l: (*two("R+A", "R+B", "read", l), np.r_[a_first, 1 - a_first])
    # text-only baselines: the shadow rows, target = start order (A's block first)
    for pn in ("read", "label_a", "label_b"):
        fam[f"textonly_startorder_{pn}"] = (lambda pn: (lambda l: (S[("M0|shadow", pn, l)], groups, a_first)))(pn)
    return fam


def _job(args):
    name, l, X, y, g, n_shuffles, seed = args
    auc = loso_auc(X, y, g)
    null = shuffle_null(X, y, g, n_shuffles=n_shuffles, seed=seed)
    return name, l, auc, float(np.percentile(null, 95)), float(null.mean()), float(null.max())


GATE_FAMILIES = ("g1_labelA_token_M", "g1_labelB_token_M", "g2_read_M", "g3_firstsign_read_M")


def run_probes(loaded: Mapping, n_shuffles: int = N_SHUFFLES, workers: int = 8, seed: int = SHUFFLE_SEED,
               layers: Sequence[int] | None = None, only: Sequence[str] | None = None) -> dict:
    """`only` restricts to named families (the battery probes the four gate
    families; the real run probes every family, comparators and baselines
    included)."""
    from concurrent.futures import ProcessPoolExecutor
    fam = families(loaded)
    if only is not None:
        fam = {k: v for k, v in fam.items() if k in set(only)}
    layers = list(loaded["layers"]) if layers is None else list(layers)
    jobs = []
    for fi, (name, fn) in enumerate(fam.items()):
        for l in layers:
            X, g, y = fn(l)
            jobs.append((name, l, X, y, g, n_shuffles, seed + 1000 * fi))
    res = {}
    if workers <= 1:
        for j in jobs:
            name, l, auc, p95, nm, nx = _job(j)
            res[(name, l)] = {"auc_loso": auc, "shuffle95": p95, "shuffle_mean": nm, "shuffle_max": nx, "above_null": auc > p95}
    else:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            for name, l, auc, p95, nm, nx in ex.map(_job, jobs, chunksize=1):
                res[(name, l)] = {"auc_loso": auc, "shuffle95": p95, "shuffle_mean": nm, "shuffle_max": nx, "above_null": auc > p95}
    return {"families": {name: {str(l): res[(name, l)] for l in layers} for name in fam}, "layers": layers, "n_jobs": len(jobs),
            "domain": loaded.get("domain"), "n_sessions": loaded.get("n_sessions")}


# --- gates --------------------------------------------------------------------
def _band(fam: Mapping, layers: Sequence[int]):
    rows = [fam[str(l)] for l in layers if str(l) in fam]
    if len(rows) != len(layers):
        raise SystemExit(f"band {layers[0]}-{layers[-1]} not fully probed ({len(rows)}/{len(layers)}) -- a skipped layer is not a pass (trap 5)")
    return rows


def gate_g1(F: Mapping) -> dict:
    a = _band(F["g1_labelA_token_M"], G1_BAND); b = _band(F["g1_labelB_token_M"], G1_BAND)
    med_a = float(np.median([r["auc_loso"] for r in a])); med_b = float(np.median([r["auc_loso"] for r in b]))
    above_a = all(r["above_null"] for r in a); above_b = all(r["above_null"] for r in b)
    ok = med_a >= G1_MEDIAN_A and med_b >= G1_MEDIAN_B and above_a and above_b
    return {"band": [G1_BAND[0], G1_BAND[-1]], "median_auc_labelA": med_a, "median_auc_labelB": med_b,
            "bar": {"labelA": G1_MEDIAN_A, "labelB": G1_MEDIAN_B, "above_null_every_layer": True},
            "above_null_every_layer": {"labelA": above_a, "labelB": above_b},
            "comparator_R_median": ({"labelA": float(np.median([r["auc_loso"] for r in _band(F["g1_labelA_token_R_comparator"], G1_BAND)])),
                                     "labelB": float(np.median([r["auc_loso"] for r in _band(F["g1_labelB_token_R_comparator"], G1_BAND)]))}
                                    if "g1_labelA_token_R_comparator" in F else "not probed (battery)"),
            "verdict": "PASS" if ok else "FAIL"}


def gate_g2(F: Mapping) -> dict:
    rows = _band(F["g2_read_M"], G2_LAYERS)
    above = [l for l, r in zip(G2_LAYERS, rows) if r["above_null"]]
    if not above:
        v = "ABSENT"
    elif len(above) >= G2_PRESENT_MIN_LAYERS:
        v = "PRESENT"
    else:
        v = "INDETERMINATE"
    return {"layers": [G2_LAYERS[0], G2_LAYERS[-1]], "layers_above_null": above, "n_above": len(above),
            "rule": f"ABSENT: none above; PRESENT: >= {G2_PRESENT_MIN_LAYERS} above; else INDETERMINATE",
            "max_auc": float(max(r["auc_loso"] for r in rows)), "verdict": v}


def gate_g3(F: Mapping) -> dict:
    rows = _band(F["g3_firstsign_read_M"], G3_BAND)
    med = float(np.median([r["auc_loso"] for r in rows])); above = all(r["above_null"] for r in rows)
    ok = med >= G3_MEDIAN and above
    return {"band": [G3_BAND[0], G3_BAND[-1]], "median_auc": med, "bar": G3_MEDIAN, "above_null_every_layer": above,
            "second_block_sign_median_beside": (float(np.median([r["auc_loso"] for r in _band(F["g3_secondsign_read_M_beside"], G3_BAND)]))
                                                if "g3_secondsign_read_M_beside" in F else "not probed (battery)"),
            "second_block_note": ("over M+A/M+B rows the second block's sign is the COMPLEMENT target of the first's; its AUC and its null are "
                                  "computed independently (the LR init is not symmetric under a label flip, and the null draws its own stream), "
                                  "so the two figures can differ at the third decimal -- reported beside, no bar"),
            "comparator_R_median": (float(np.median([r["auc_loso"] for r in _band(F["g3_firstsign_read_R_comparator"], G3_BAND)]))
                                    if "g3_firstsign_read_R_comparator" in F else "not probed (battery)"),
            "verdict": "PASS" if ok else "FAIL"}


def gate_g4(meta: Mapping) -> dict:
    """Leak calibration on the no-preference masks only; the prohibition on
    M+A/M+B is asserted, not merely respected."""
    sess = sorted(meta["per_session"].values(), key=lambda r: r["session"])
    out = {}
    for m in ("R+A", "R+B", "M++", "R++"):
        flips, shifts, signed = [], [], []
        for r in sess:
            st, sh = r["masks"][m]["state"], r["masks"][m]["shadow"]
            flips.append(int(st["pick"] != sh["pick"]))
            da = (st["logit_a"] - st["logit_b"]) - (sh["logit_a"] - sh["logit_b"])
            shifts.append(abs(da))
            if m.startswith("R"):
                signed.append(da if r["a_is_first_block"] else -da)   # toward the FIRST block's label
        k, n = int(sum(flips)), len(flips)
        lo, hi = clopper_pearson(k, n)
        s_ = np.array(shifts)
        d = {"pi_d": k / n if n else None, "n_flips": k, "n": n, "clopper_pearson_95": [lo, hi],
             "abs_logit_diff_shift": {"median": float(np.median(s_)), "mean": float(s_.mean()), "max": float(s_.max())} if n else None}
        if signed:
            v = np.array(signed)
            d["signed_shift_toward_first_block_label"] = {"mean": float(v.mean()), "sd": float(v.std(ddof=1)) if len(v) > 1 else None,
                                                          "n_pos": int((v > 0).sum()), "n_neg": int((v < 0).sum())}
        out[m] = d
    out["prohibition"] = "no signed quantity toward the +label computed on M+A / M+B (asserted: the masks iterated above are exactly R+A, R+B, M++, R++)"
    return out


def gate_g5(sessions: Sequence[Mapping]) -> dict:
    """Identity baseline from the sessions' own recorded vanilla first picks."""
    by_pair: dict = {}
    for s in sessions:
        if not s["choices"]:
            continue
        key = "/".join(s["pair"])
        d = by_pair.setdefault(key, {t: 0 for t in s["pair"]})
        d[s["choices"][0]["pick"]] += 1
    per_pair = {}
    for key, d in by_pair.items():
        n = sum(d.values())
        per_pair[key] = {t: {"k": k, "n": n, "share": k / n if n else None, "clopper_pearson_95": list(clopper_pearson(k, n))} for t, k in d.items()}
    alt = [s for s in sessions if H.strictly_alternates(s) is not None]
    brk = [s for s in sessions if H.follows_habit(s) is not None]
    stays = sum(1 for s in sessions for i in range(1, len(s["choices"])) if s["choices"][i]["pick"] == s["choices"][i - 1]["pick"])
    trans = sum(max(0, len(s["choices"]) - 1) for s in sessions)
    return {"domain": "all sessions incl. excluded (rule 23); a session without a first pick contributes nothing to the shares",
            "per_pair_first_pick_share": per_pair,
            "strict_alternation": {"k": sum(1 for s in alt if H.strictly_alternates(s)), "n": len(alt)},
            "first_pick_is_last_forced_label": {"k": sum(1 for s in brk if not H.follows_habit(s)), "n": len(brk)},
            "stay_transitions": {"k": stays, "n": trans}}


def select_sentence(g1: Mapping, g2: Mapping, g3: Mapping) -> tuple[str, str]:
    """Disjunction-complete over G1-G3 (§1.5). G3 FAIL dominates; then G1
    FAIL; then G2's three branches."""
    if g3["verdict"] == "FAIL":
        return "G3_FAIL", SENTENCES["G3_FAIL"]
    if g1["verdict"] == "FAIL":
        return "G1_FAIL", SENTENCES["G1_FAIL"]
    return g2["verdict"], SENTENCES[g2["verdict"]]


def evaluate(meta: Mapping, probes: Mapping, sessions: Sequence[Mapping], probes_all: Mapping | None = None) -> dict:
    fails = assertion_failures(meta)
    idn = [r["masks"][m]["identity"] for r in meta["per_session"].values() for m in REQUIRED_MASKS if m in r.get("masks", {})]
    if fails:
        return {"branch": "STOP", "sentence": SENTENCES["STOP"], "sentence_provenance": SENTENCE_PROVENANCE["STOP"],
                "assertion_failures": fails[:20], "identity": {"n_pairs": len(idn), "all_ok": all(i["ok"] for i in idn) if idn else False},
                "complete": meta.get("complete", False), "gates_evaluated": False}
    identity_ok = True
    F = probes["families"]
    g1, g2, g3 = gate_g1(F), gate_g2(F), gate_g3(F)
    g4 = gate_g4(meta); g5 = gate_g5(sessions)
    branch, sentence = select_sentence(g1, g2, g3)
    beside = None
    if probes_all is not None:
        FA = probes_all["families"]
        beside = {"domain": "all sessions with a first pick (rule 23)", "G1": gate_g1(FA), "G2": gate_g2(FA), "G3": gate_g3(FA)}
    return {"branch": branch, "sentence": sentence, "sentence_provenance": SENTENCE_PROVENANCE[branch], "gates_evaluated": True,
            "domain": "valid sessions (not excluded under the run scope) with a first free choice; rule-23 figure beside",
            "n_sessions_valid": probes.get("n_sessions"), "beside_all_with_first_pick": beside,
            "identity": {"n_pairs": len(idn), "all_ok": identity_ok},
            "G1": g1, "G2": g2, "G3": g3, "G4": g4, "G5": g5,
            "frame": {"ABSENT": "F-ABSENT", "INDETERMINATE": "F-ABSENT (indeterminacy named)", "PRESENT": "F-PRESENT",
                      "G1_FAIL": "F-ABSENT (sign-memory operant only)", "G3_FAIL": "no Stage 2"}[branch]}


# --- synthetic battery (§1.6: reaches every G2 branch, and G1/G3 pass/fail, and STOP) ---
def synthetic(branch: str, n_sessions: int = 12, dim: int = 12, seed: int = 1, out_dir: str | None = None) -> tuple[dict, list]:
    """A small synthetic Stage 1 artifact whose signal is placed to land the
    analyzer in `branch`: 'ABSENT', 'PRESENT', 'INDETERMINATE', 'G1_FAIL',
    'G3_FAIL', 'STOP'. Layers are the real capture set; signal strength is
    large where a gate must pass and zero where it must fail; the
    INDETERMINATE case puts signal at exactly two G2 layers."""
    rng = np.random.default_rng(seed)
    layers = list(range(40, 64))
    layers = [l for l in layers if l in (40, 44, 48) or l >= 49]
    out_dir = out_dir or os.path.join(REPO, "data", "k", "_synthetic")
    os.makedirs(out_dir, exist_ok=True)
    per, sessions = {}, []
    pairs = [("granite", "plaza"), ("prism", "slate"), ("velvet", "walnut"), ("ridge", "saddle")]
    for i in range(n_sessions):
        pair = pairs[i % 4]; first = pair[i // 4 % 2]; second = pair[1 - (i // 4 % 2)]
        a, b = (pair if rng.integers(2) == 0 else pair[::-1])
        a_first = a == first
        arrays = {"layers": np.array(layers, dtype=np.int32), "positions": np.array([300, 291, 296], dtype=np.int32)}
        base = rng.normal(0, 1, (3, len(layers), dim)).astype(np.float32)
        arrays["M0|shadow"] = base
        big = 6.0
        for m in ("M+A", "M+B", "R+A", "R+B", "M++", "R++"):
            arr = base + rng.normal(0, 0.3, base.shape).astype(np.float32)
            plus_label = a if m.endswith("+A") else (b if m.endswith("+B") else None)
            for li, l in enumerate(layers):
                # G1 signal at the label tokens (binding): direction 0 encodes "this label carried +"
                if branch != "G1_FAIL" and m.startswith("M") and plus_label is not None and 51 <= l <= 61:
                    arr[1, li, 0] += big if plus_label == a else -big
                    arr[2, li, 0] += big if plus_label == b else -big
                # G2 signal at the read (binding at the decision): direction 1
                if m.startswith("M") and plus_label is not None:
                    sgn = big if plus_label == a else -big
                    if branch == "PRESENT" and 49 <= l <= 63:
                        arr[0, li, 1] += sgn
                    if branch == "INDETERMINATE" and l in (55, 59):
                        arr[0, li, 1] += sgn
                # G3 signal at the read (first-block sign): direction 2
                if branch != "G3_FAIL" and m.startswith("M") and plus_label is not None and 51 <= l <= 62:
                    arr[0, li, 2] += big if plus_label == first else -big
            arrays[f"{m}|state"] = arr.astype(np.float32)
        npz = os.path.join(out_dir, f"syn_{branch}_s{i}.npz")
        np.savez(npz, **arrays)
        masks = {}
        for m in ("M+A", "M+B", "R+A", "R+B", "M++", "R++"):
            la, lb = float(rng.normal(0, 1)), float(rng.normal(0, 1))
            masks[m] = {"state": {"logit_a": la + 0.01, "logit_b": lb, "pick": a if la >= lb else b},
                        "shadow": {"logit_a": la, "logit_b": lb, "pick": a if la >= lb else b},
                        "identity": {"ok": branch != "STOP" or i != 3}}
        per[str(i)] = {"session": i, "pair": list(pair), "first_label": first, "second_label": second, "menu_a": a, "menu_b": b,
                       "a_is_first_block": a_first, "excluded": False, "strict_excluded": False, "npz": os.path.relpath(npz, REPO),
                       "npz_sha16_by_key": {k: sha16_arr(v) for k, v in arrays.items() if k not in ("layers", "positions")},
                       "masks": masks}
        picks = [first if j % 2 == 0 else second for j in range(6)]
        sessions.append({"session": i, "pair": list(pair), "excluded": False,
                         "rounds": [{"phase": f"forced{k}", "pole": "pos" if k < 2 else "neg", "tag": first if k < 2 else second} for k in range(4)],
                         "choices": [{"phase": f"free{j}", "pick": p, "picked_pole": "pos" if p == first else "neg"} for j, p in enumerate(picks)]})
    meta = {"per_session": per, "complete": True, "sessions": list(range(n_sessions)), "capture_layers": layers, "synthetic_branch": branch}
    return meta, sessions


__all__ = ["G1_BAND", "G1_MEDIAN_A", "G1_MEDIAN_B", "G2_LAYERS", "G2_PRESENT_MIN_LAYERS", "G3_BAND", "G3_MEDIAN",
           "N_SHUFFLES", "SHUFFLE_SEED", "SENTENCES", "SENTENCE_PROVENANCE", "proposal_sentences", "REQUIRED_MASKS",
           "assertion_failures", "clopper_pearson", "load_stacks", "families", "run_probes",
           "gate_g1", "gate_g2", "gate_g3", "gate_g4", "gate_g5", "select_sentence", "evaluate", "synthetic"]
