"""RECON -- ECHO CHANNEL (PROPOSAL-k candidate). RECON BLOCK 2026-09-05.

Apparatus characterization only: NO verdict quantity, NO bar, NO new
sessions. Reads archived e2a reward-arm sessions (data/e2a/sessions.jsonl)
through the quarantined echo primitive with the e2a config of record (L48,
frac 0.10, the frozen reward axis, e2a's round-task spans).

    --selftest            model-free: guard, mask assertions, probe, spans
    --stage timing        §2: one steered + one mask-off forward, longest session
    --stage a             §3.1 Stage A: 24 sessions x masks M1..M4 (+ shadows)
    --analyze a           §3.1 tables (model-free)

PROHIBITION (§3.1), enforced in code: the signed shift toward the +paired
label is computable only for the random / same-pole masks (M3, M4, M5, M6);
`signed_pseudo_shift` refuses M1/M2, and no first-choice Delta on a reward
mask is computed anywhere in this file.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from valence_core.session import assert_modules_absent                # noqa: E402
assert_modules_absent(("valence_core.e2b.statepresent",))
from valence_core.adapters.base import Injection, assert_equal_norm, sha16_arr  # noqa: E402
from valence_core.echo import probe as PR                               # noqa: E402
from valence_core.echo.maskedprefix import (FORBIDDEN_MODULES,          # noqa: E402
                                            assert_statepresent_absent,
                                            build_mask,
                                            read_choice_maskedprefix)
from valence_core.echo.spans import (CHOICE_MARKER, choice_prefix,      # noqa: E402
                                     round_char_spans, token_spans)
from valence_core.regression.oracle import load_axis                    # noqa: E402
from valence_core.session_e2a import load_tasks                         # noqa: E402

DATA = os.path.join(REPO, "data")
OUT = os.path.join(DATA, "echo")
LAYER = 48                       # e2a steering layer of record (row-verified below)
AXIS_SHA_F64 = "3c17b0d8fbcad716"   # frozen reward axis, float64-normalised (trap 17)
RAND_KEY = "L48"                 # e2a random1 = e0_random_dirs.npz['L48'] (jlens_qwen.e2a.load_directions)
TAG_WORDS = ["slate", "prism", "maple", "cedar", "granite", "lattice",
             "plaza", "saddle", "velvet", "walnut", "ridge"]   # regression.oracle's list
MASKS = ("M1", "M2", "M3", "M4")
#: Stage B state masks (design block 2026-09-05 §3b, plus the random-direction
#: comparators §3c asks for under the same masks): M5/M6 same-pole (axis),
#: M5x/M6x same-pole (random), R1..R4 single round at its as-generated pole
#: (axis), R1x..R4x the same with the random direction.
MASKS_B = ("M1", "M2", "M3", "M4", "M5", "M6", "M5x", "M6x",
           "R1", "R2", "R3", "R4", "R1x", "R2x", "R3x", "R4x")
SIGNED_OK = {"M3", "M4", "M5", "M6", "M5x", "M6x"}
N_STAGE_A = 24


# --- data ------------------------------------------------------------------
def load_rows():
    return [json.loads(l) for l in open(os.path.join(DATA, "e2a/sessions.jsonl"))
            if l.strip()]


def valid_reward(rows):
    return sorted([r for r in rows if r["arm"] == "reward" and not r["excluded"]],
                  key=lambda r: r["session"])


def stage_a_sessions(valid):
    """First 24 valid reward sessions by index, balanced 12/12 by the
    label<->pole map (`swap`); else the first 12 of each map."""
    first = valid[:N_STAGE_A]
    n_swap = sum(1 for r in first if r["swap"])
    if n_swap * 2 == N_STAGE_A:
        return first, "first 24 by index (balanced 12/12 as found)"
    a = [r for r in valid if not r["swap"]][:N_STAGE_A // 2]
    b = [r for r in valid if r["swap"]][:N_STAGE_A // 2]
    return sorted(a + b, key=lambda r: r["session"]), \
        f"first 24 were {N_STAGE_A - n_swap}/{n_swap}; took the first 12 of each map"


def tag_ids_for(adapter):
    out = {}
    for w in TAG_WORDS:
        enc = adapter.encode(" " + w, add_special_tokens=False)
        if len(enc) == 1:
            out[w] = enc[0]
    return out


def dose_of_record(rows):
    doses = {r["dose"] for r in rows if r["arm"] == "reward"}
    if len(doses) != 1:
        raise AssertionError(f"e2a reward rows carry more than one dose: {doses}")
    return float(doses.pop())


def make_injections(frac):
    rw, R = load_axis(LAYER)
    axis = Injection.at_frac(rw, LAYER, frac, R, expect_sha=AXIS_SHA_F64)
    rz = np.load(os.path.join(DATA, "e0/e0_random_dirs.npz"))
    rand_u = rz[RAND_KEY].astype(np.float64)
    rand = Injection.at_frac(rand_u, LAYER, frac, R)
    assert_equal_norm(axis, rand)                      # rule 4
    return axis, rand, R[LAYER]


def signs_for(spans, mask):
    """Per-round sign under a mask (0 = that round unsteered). M1/M3: as
    generated (+ on pos-pole rounds, - on neg-pole rounds); M2/M4: flipped;
    M5/M5x all +; M6/M6x all -; R<r>/R<r>x: only round r, at its
    as-generated pole."""
    base = [1 if s["pole"] == "pos" else -1 for s in spans]
    if mask in ("M1", "M3"):
        return base
    if mask in ("M2", "M4"):
        return [-x for x in base]
    if mask in ("M5", "M5x"):
        return [1] * len(spans)
    if mask in ("M6", "M6x"):
        return [-1] * len(spans)
    if mask[0] == "R" and mask[1].isdigit():
        r = int(mask[1]) - 1
        if not (0 <= r < len(spans)):
            raise ValueError(f"{mask}: no round {r + 1} among {len(spans)} spans")
        return [base[i] if i == r else 0 for i in range(len(spans))]
    raise ValueError(mask)


def injection_for(mask, axis, rand):
    if mask in ("M3", "M4") or mask.endswith("x"):
        return rand
    return axis


def spans_with_injections(tspans, mask, axis, rand):
    inj = injection_for(mask, axis, rand)
    signs = signs_for(tspans, mask)
    return [(s["tok_start"], s["tok_end"], inj.with_sign(sg),
             f"{s['phase']}:{s['tag']}:{'+' if sg > 0 else '-'}")
            for s, sg in zip(tspans, signs) if sg != 0]


def signed_pseudo_shift(mask, pair_state, pair_shadow, tag_plus_is_a,
                        plus_on_tag_plus):
    """Signed shift of (logit toward the label whose rounds carried r+)
    relative to the shadow. ONLY for the random / same-pole masks."""
    if mask not in SIGNED_OK:
        raise AssertionError(
            f"PROHIBITED: signed shift toward the +paired label under {mask} "
            f"is the candidate cell's DV and exists only after a committed "
            f"pre-registration (RECON BLOCK §3.1)")
    da = (pair_state["logit_a"] - pair_state["logit_b"]) - \
        (pair_shadow["logit_a"] - pair_shadow["logit_b"])
    toward_plus_tag = da if tag_plus_is_a else -da
    return toward_plus_tag if plus_on_tag_plus else -toward_plus_tag


def atomic_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(obj, fh, indent=1, default=float)
    os.replace(tmp, path)


def atomic_npz(path, **arrays):
    tmp = path + ".tmp.npz"
    np.savez(tmp, **arrays)
    os.replace(tmp, path)


# --- adapter ---------------------------------------------------------------
def load_adapter():
    from valence_core.adapters.qwen_mlx import QwenMLXAdapter
    t0 = time.time()
    ad = QwenMLXAdapter()
    print(f"model loaded in {time.time() - t0:.0f}s", flush=True)
    print(f"provenance: {json.dumps(ad.provenance())}", flush=True)
    return ad


class _TokenizerOnly:
    """Selftest shim: encode via the fast tokenizer from the local snapshot;
    no model."""

    def __init__(self):
        sys.path.insert(0, os.path.join(REPO, "jlens-qwen36"))
        from mlx_lm.utils import load_tokenizer
        snap = glob.glob(str(Path.home() / ".cache/huggingface/hub/"
                             "models--mlx-community--Qwen3.6-27B-4bit/snapshots/*"))
        self._tok = load_tokenizer(Path(sorted(snap)[0]))

    def encode(self, text, add_special_tokens=True):
        return list(self._tok.encode(text, add_special_tokens=add_special_tokens))


# --- selftest --------------------------------------------------------------
def selftest():
    ok = []

    def c(name, cond, got=""):
        ok.append(bool(cond))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}  {got}")

    # 1. guard: a plain import from outside the sanctioned callers fails
    r = subprocess.run([sys.executable, "-c",
                        "import valence_core.echo.maskedprefix"],
                       cwd=REPO, capture_output=True, text=True)
    c("guard: bare import refused", r.returncode != 0 and "quarantined" in r.stderr,
      f"rc={r.returncode}")
    # 2. statepresent absent here
    assert_statepresent_absent()
    c("statepresent absent from sys.modules", all(m not in sys.modules for m in FORBIDDEN_MODULES))
    # 3. mask assertions
    rw, R = load_axis(LAYER)
    inj = Injection.at_frac(rw, LAYER, 0.10, R, expect_sha=AXIS_SHA_F64)
    m = build_mask(10, [(1, 4, inj, "a"), (5, 8, inj.with_sign(-1), "b")])
    c("mask: two spans, 6 steered, signs", int(np.sum(m != 0)) == 6 and m[1] == 1 and m[5] == -1 and m[9] == 0)
    for bad, why in (([(1, 10, inj, "x")], "reaches read position"),
                     ([(1, 5, inj, "x"), (4, 7, inj, "y")], "overlap"),
                     ([(0, 0, inj, "x")], "empty")):
        try:
            build_mask(10, bad); c(f"mask refuses {why}", False)
        except AssertionError:
            c(f"mask refuses {why}", True)
    # 4. prohibition
    try:
        signed_pseudo_shift("M1", {"logit_a": 0, "logit_b": 0}, {"logit_a": 0, "logit_b": 0}, True, True)
        c("prohibition: M1 signed shift refused", False)
    except AssertionError:
        c("prohibition: M1 signed shift refused", True)
    c("prohibition: M3 signed shift allowed", signed_pseudo_shift(
        "M3", {"logit_a": 1.0, "logit_b": 0.0}, {"logit_a": 0.0, "logit_b": 0.0}, True, True) == 1.0)
    # 5. probe on synthetic data
    rng = np.random.default_rng(0)
    X = rng.normal(size=(48, 64)); y = np.array([1, 0] * 24); g = np.repeat(np.arange(24), 2)
    Xs = X + 3.0 * y[:, None] * np.r_[np.ones(4), np.zeros(60)][None, :]
    auc_sep = PR.loso_auc(Xs, y, g); auc_rand = PR.loso_auc(X, y, g)
    null = PR.shuffle_null(X, y, g, n_shuffles=20, seed=1)
    c("probe: separable -> AUC > .95", auc_sep > .95, f"{auc_sep:.3f}")
    c("probe: random -> AUC within null", null.min() - .1 <= auc_rand <= null.max() + .1, f"{auc_rand:.3f} null [{null.min():.2f},{null.max():.2f}]")
    sf = PR.surviving_fraction(Xs[y == 1], Xs[y == 0], alpha=3.0, d=np.r_[np.ones(4), np.zeros(60)])   # shift norm 3*sqrt(4) = 6 = 2*alpha
    c("probe: surviving fraction ~1, cosine ~1", abs(sf["surviving_fraction"] - 1) < .15 and sf["cosine_with_axis"] > .9,
      f"{sf['surviving_fraction']:.3f} / {sf['cosine_with_axis']:.3f}")
    # 6. spans on one archived session (tokenizer only)
    rows = load_rows(); tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    row = valid_reward(rows)[0]
    tok = _TokenizerOnly()
    prefix = choice_prefix(row["transcript"], 0)
    cs = round_char_spans(row, tasks)
    ts = token_spans(tok, prefix, cs)
    n = len(tok.encode(prefix))
    c("spans: 4 forced rounds inside the first-choice prefix", len(ts) == 4 and all(t["phase"].startswith("forced") for t in ts), str([(t['tok_start'], t['tok_end']) for t in ts]))
    c("spans: every span ends before the read position", all(t["tok_end"] <= n - 1 for t in ts), f"n={n}")
    c("spans: poles match the archive", [t["pole"] for t in ts] == [r["pole"] for r in row["rounds"]])
    c("spans: 10 rounds in the full transcript", len(cs) == 10)
    mk = build_mask(n, spans_with_injections(ts, "M1", inj, inj))
    c("mask from spans: steered count = sum of span lengths", int(np.sum(mk != 0)) == sum(t["n_tokens"] for t in ts))
    c("M2 flips every sign of M1", signs_for(ts, "M2") == [-x for x in signs_for(ts, "M1")])
    # 7. stage-A roster
    sel, how = stage_a_sessions(valid_reward(rows))
    c("stage A roster: 24 sessions, 12/12 by map", len(sel) == 24 and sum(r["swap"] for r in sel) == 12, how)
    print(f"\n  {sum(ok)}/{len(ok)} selftest checks pass")
    return all(ok)


# --- §2 timing -------------------------------------------------------------
def stage_timing(adapter, rows, tasks, axis, rand, out_path):
    valid = valid_reward(rows)
    lens = [(len(adapter.encode(r["transcript"])), r["session"]) for r in valid]
    n_tok, sid = max(lens)
    row = next(r for r in valid if r["session"] == sid)
    tag_ids = tag_ids_for(adapter)
    full = row["transcript"]
    cs = round_char_spans(row, tasks)
    ts_full = token_spans(adapter, full, cs)
    ts_first = token_spans(adapter, choice_prefix(full, 0), cs)
    a, b = row["choices"][0]["menu_a"], row["choices"][0]["menu_b"]
    all64 = list(range(adapter.n_layers))
    above = [l for l in all64 if l > LAYER]
    res = {"session": sid, "n_tokens_full": n_tok,
           "n_tokens_first_choice_prefix": len(adapter.encode(choice_prefix(full, 0))),
           "n_rounds_steered_full": len(ts_full), "n_steered_tokens_full": sum(t["n_tokens"] for t in ts_full),
           "timings_s": {}}

    def timed(name, fn):
        t0 = time.time(); r_ = fn(); dt = time.time() - t0
        res["timings_s"][name] = dt
        print(f"  {name:<58} {dt:7.2f} s", flush=True)
        return r_

    ids_full = adapter.encode(full)
    placed_full = [(s, e, inj, tg) for s, e, inj, tg in spans_with_injections(ts_full, "M1", axis, rand)]
    # full session, hook on every round span, capture all 64 layers at the last position
    from valence_core.adapters.base import PositionSpec
    injs = [inj.with_positions(PositionSpec.spans((s, e))) for s, e, inj, _ in placed_full]
    timed("full session: steered forward, capture 64 layers", lambda: adapter.forward_last(ids_full, all64, injs))
    timed("full session: mask-off forward, capture 64 layers", lambda: adapter.forward_last(ids_full, all64, ()))
    timed("full session: steered forward, capture 15 layers above 48", lambda: adapter.forward_last(ids_full, above, injs))
    timed("full session: steered forward, no capture", lambda: adapter.forward_last(ids_full, (), injs))
    timed("full session: mask-off forward, no capture", lambda: adapter.forward_last(ids_full, (), ()))
    # the Stage A read itself: first-choice prefix through the primitive (state + shadow + choice_read verify)
    prefix = choice_prefix(full, 0)
    timed("first-choice prefix: echo primitive M1 (state+shadow+choice_read x2)",
          lambda: read_choice_maskedprefix(adapter, prefix, a, b, tag_ids,
                                           spans_with_injections(ts_first, "M1", axis, rand), all64, str(sid), "timing"))
    t = res["timings_s"]
    per_mask = t["first-choice prefix: echo primitive M1 (state+shadow+choice_read x2)"]
    res["projection"] = {
        "stage_a_reads": N_STAGE_A * len(MASKS),
        "stage_a_hours_at_measured_rate": N_STAGE_A * len(MASKS) * per_mask / 3600,
        "stage_a_hours_throttled_1.7x": N_STAGE_A * len(MASKS) * per_mask * 1.7 / 3600,
        "stage_b_reads_first_choice": 102 * 11,
        "stage_b_hours_first_choice_only": 102 * 11 * per_mask / 3600,
        "stage_b_hours_full_session_upper_bound": 102 * 11 * (t["full session: steered forward, capture 64 layers"] + t["full session: mask-off forward, capture 64 layers"] + 2 * t["full session: mask-off forward, no capture"]) / 3600,
        "note": ("Stage A reads at the FIRST free choice, so its forwards are over the first-choice prefix "
                 "(~200 tokens), not the full session; the full-session figures bound Stage B's later positions."),
    }
    print(json.dumps(res["projection"], indent=1))
    atomic_json(out_path, res)
    return res


# --- §3.1 Stage A ----------------------------------------------------------
def stage_a(adapter, rows, tasks, axis, rand, R48, frac, resume):
    os.makedirs(OUT, exist_ok=True)
    valid = valid_reward(rows)
    sel, how = stage_a_sessions(valid)
    tag_ids = tag_ids_for(adapter)
    all64 = list(range(adapter.n_layers))
    meta_path = os.path.join(OUT, "stageA_reads.json")
    meta = {"stage": "A", "block": "RECON BLOCK 2026-09-05 §3.1", "roster": how,
            "sessions": [r["session"] for r in sel],
            "read_position": "first free choice (e2a primary position); text = transcript prefix through the first 'Config choice (one word):'",
            "config_of_record": {"layer": LAYER, "frac": frac, "alpha": axis.alpha, "R_48": R48,
                                 "axis_direction_sha_f64": axis.direction_sha,
                                 "random_direction": f"e0_random_dirs.npz[{RAND_KEY}]",
                                 "random_direction_sha": rand.direction_sha},
            "masks": {"M0": "off (the shadow of every pair; identity vs the archived read)",
                      "M1": "as-generated polarity: + on pos-pole rounds, - on neg-pole rounds (reward axis)",
                      "M2": "flipped polarity, same spans, same text (reward axis)",
                      "M3": "random direction r with M1's sign pattern",
                      "M4": "random direction r with M2's sign pattern"},
            "capture_layers": all64,
            "provenance": adapter.provenance(),
            "round_path_note": ("archived texts were generated on the cached path (first-token licence); "
                                "every recon forward is uncached"),
            "per_session": {}}
    if resume and os.path.exists(meta_path):
        old = json.load(open(meta_path))
        if old.get("sessions") != meta["sessions"] or old["config_of_record"]["alpha"] != axis.alpha:
            raise SystemExit("resume refused: a different roster or dose is on disk")
        meta["per_session"] = old["per_session"]
    t_start = time.time()
    for k, row in enumerate(sel):
        sid = str(row["session"])
        npz_path = os.path.join(OUT, f"stageA_resid_s{sid}.npz")
        if sid in meta["per_session"] and os.path.exists(npz_path):
            print(f"  s{sid}: on disk, skipped", flush=True)
            continue
        prefix = choice_prefix(row["transcript"], 0)
        ts = token_spans(adapter, prefix, round_char_spans(row, tasks))
        if len(ts) != 4:
            raise AssertionError(f"s{sid}: expected 4 forced spans, got {len(ts)}")
        ch = row["choices"][0]
        a, b = ch["menu_a"], ch["menu_b"]
        rec = {"session": row["session"], "swap": row["swap"], "tag_plus": row["tag_plus"],
               "pair": row["pair"], "start_plus": row["start_plus"], "menu_a": a, "menu_b": b,
               "archived_read": {"pick": ch["pick"], "p_a": ch["p_a"], "label_mass": ch["label_mass"],
                                 "verify_kl": ch["verify_kl"], "picked_pole": ch["picked_pole"]},
               "spans": ts, "masks": {}}
        arrays = {"layers": np.array(all64, dtype=np.int32)}
        t0 = time.time()
        for mask in MASKS:
            pair = read_choice_maskedprefix(adapter, prefix, a, b, tag_ids,
                                            spans_with_injections(ts, mask, axis, rand),
                                            all64, sid, mask)
            d = pair.as_dict()
            # IDENTITY ASSERTION: the shadow must reproduce the archived vanilla read.
            dpa = abs(pair.shadow.p_a - ch["p_a"]); dmass = abs(pair.shadow.label_mass - ch["label_mass"])
            d["identity"] = {"shadow_p_a_vs_archived_abs": dpa, "shadow_mass_vs_archived_abs": dmass,
                             "shadow_pick_eq_archived": pair.shadow.pick == ch["pick"],
                             "choice_read_verify_kl": pair.shadow_choice_read.verify_kl,
                             "shadow_forward_vs_choice_read_abs_dpa": pair.shadow_vs_choice_read_abs_dpa,
                             "archive_precision": "4 decimals (p_a, label_mass); logits not archived",
                             "ok": bool(dpa <= 5e-4 and dmass <= 5e-4 and pair.shadow.pick == ch["pick"]
                                        and pair.shadow_choice_read.verify_kl == 0.0
                                        and pair.shadow_vs_choice_read_abs_dpa <= 1e-6)}
            rec["masks"][mask] = d
            arrays[f"{mask}|state"] = np.stack([pair.state.resid_last[l] for l in all64]).astype(np.float32)
            arrays[f"{mask}|shadow"] = np.stack([pair.shadow.resid_last[l] for l in all64]).astype(np.float32)
            if not d["identity"]["ok"]:
                atomic_json(meta_path, meta)
                raise SystemExit(f"STOP: identity assertion failed at s{sid} {mask}: {d['identity']}")
        atomic_npz(npz_path, **arrays)
        rec["npz"] = os.path.relpath(npz_path, REPO)
        rec["npz_sha16_by_key"] = {k: sha16_arr(v) for k, v in arrays.items() if k != "layers"}
        rec["seconds"] = time.time() - t0
        meta["per_session"][sid] = rec
        atomic_json(meta_path, meta)
        el = time.time() - t_start
        print(f"  s{sid:>3} ({k + 1}/{len(sel)}) n={pair.n_positions} steered={pair.n_steered} "
              f"identity ok  {rec['seconds']:.0f}s  elapsed {el / 60:.1f} min", flush=True)
    meta["wall_clock_s"] = time.time() - t_start
    atomic_json(meta_path, meta)
    print(f"Stage A reads complete: {len(meta['per_session'])} sessions, {meta['wall_clock_s'] / 60:.1f} min")


# --- §3.1 analysis (model-free) --------------------------------------------
def _layer_job(args):
    l, XA, XB, groups, n_shuffles, seed = args
    X = np.concatenate([XA, XB]); y = np.r_[np.ones(len(XA)), np.zeros(len(XB))]
    g = np.r_[groups, groups]
    auc = PR.loso_auc(X, y, g)
    null = PR.shuffle_null(X, y, g, n_shuffles=n_shuffles, seed=seed + l)
    return l, auc, float(np.percentile(null, 95)), float(np.mean(null)), float(np.max(null))


def analyze_a(n_shuffles, workers, workspace_layers):
    from concurrent.futures import ProcessPoolExecutor
    meta = json.load(open(os.path.join(OUT, "stageA_reads.json")))
    sess = sorted(meta["per_session"].values(), key=lambda r: r["session"])
    layers = None; resid = {}
    for r in sess:
        z = np.load(os.path.join(REPO, r["npz"]))
        if layers is None:
            layers = [int(x) for x in z["layers"]]
        for k in z.files:
            if k != "layers":
                if sha16_arr(z[k]) != r["npz_sha16_by_key"][k]:
                    raise SystemExit(f"fingerprint mismatch s{r['session']} {k}")
                resid[(r["session"], k)] = z[k]
    groups = np.array([r["session"] for r in sess])
    alpha = meta["config_of_record"]["alpha"]
    rw, _ = load_axis(LAYER); d = rw / np.linalg.norm(rw)
    out = {"n_sessions": len(sess), "n_shuffles": n_shuffles, "alpha": alpha,
           "probe": "standardized L2 logistic regression (discrim.logistic_auc hyperparameters), leave-one-session-out, both rows of a session held out together; target = M1 (as-generated polarity) vs M2 (flipped); comparator = M3 vs M4",
           "per_layer": {}, "stop_clause": {}, "leak": {}, "pseudo_shift": {}}
    li = {l: i for i, l in enumerate(layers)}

    def stack(mask, which):
        return np.stack([resid[(r["session"], f"{mask}|{which}")] for r in sess])   # [N, L, D]
    M = {m: stack(m, "state") for m in MASKS}
    jobs = []
    for l in layers:
        jobs.append((l, M["M1"][:, li[l], :], M["M2"][:, li[l], :], groups, n_shuffles, 20260905))
    jobs_r = [(l, M["M3"][:, li[l], :], M["M4"][:, li[l], :], groups, n_shuffles, 30260905) for l in layers]
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res_m = {r[0]: r for r in ex.map(_layer_job, jobs)}
        res_r = {r[0]: r for r in ex.map(_layer_job, jobs_r)}
    print(f"  probes done in {(time.time() - t0) / 60:.1f} min", flush=True)
    print(f"  {'layer':>5} {'type':>6} {'AUC_reward':>10} {'AUC_random':>10} {'shuffle95':>9} {'surv.frac':>9} {'cos(d)':>7} {'pairnorm/2a':>11}")
    for l in layers:
        _, auc, p95, nmean, nmax = res_m[l]
        _, auc_r, p95_r, _, _ = res_r[l]
        sf = PR.surviving_fraction(M["M1"][:, li[l], :], M["M2"][:, li[l], :], alpha, d)
        pair_norm = float(np.mean(np.linalg.norm(M["M1"][:, li[l], :] - M["M2"][:, li[l], :], axis=1)) / (2 * alpha))
        sf_r = PR.surviving_fraction(M["M3"][:, li[l], :], M["M4"][:, li[l], :], alpha, d)
        row = {"auc_reward_M1vM2": auc, "shuffle95_reward": p95, "shuffle_mean_reward": nmean, "shuffle_max_reward": nmax,
               "auc_random_M3vM4": auc_r, "shuffle95_random": p95_r,
               "surviving_fraction": sf["surviving_fraction"], "norm_diff": sf["norm_diff"], "cosine_with_axis": sf["cosine_with_axis"],
               "beside_mean_pairwise_norm_over_2alpha": pair_norm,
               "random_surviving_fraction": sf_r["surviving_fraction"], "random_cosine_with_axis": sf_r["cosine_with_axis"],
               "above_steering_layer": l > LAYER, "workspace": l in workspace_layers,
               "reward_above_shuffle95": auc > p95}
        out["per_layer"][str(l)] = row
        flag = " <-- above null" if auc > p95 else ""
        print(f"  {l:>5} {'above' if l > LAYER else ('steer' if l == LAYER else 'below'):>6} {auc:10.3f} {auc_r:10.3f} {p95:9.3f} {sf['surviving_fraction']:9.4f} {sf['cosine_with_axis']:7.3f} {pair_norm:11.4f}{flag}")
    below = [l for l in layers if l <= LAYER and out["per_layer"][str(l)]["reward_above_shuffle95"]]
    out["stop_clause"] = {"layers_le_48_above_null": below, "fired": bool(below),
                          "rule": "any layer <= the steering layer with M1/M2 AUC above its shuffle 95th percentile -> STOP (hook placement or mask leak)"}
    # LEAK (unsigned only on reward masks)
    for m in ("M1", "M2"):
        flips = []; shifts = []
        for r in sess:
            st, sh = r["masks"][m]["state"], r["masks"][m]["shadow"]
            flips.append(int(st["pick"] != sh["pick"]))
            shifts.append(abs((st["logit_a"] - st["logit_b"]) - (sh["logit_a"] - sh["logit_b"])))
        s = np.array(shifts)
        out["leak"][m] = {"pi_d": float(np.mean(flips)), "n_flips": int(np.sum(flips)), "n": len(flips),
                          "abs_logit_diff_shift": {"min": float(s.min()), "median": float(np.median(s)), "mean": float(s.mean()), "max": float(s.max()),
                                                   "values": [float(x) for x in s]}}
        print(f"  LEAK {m}: pi_d = {np.sum(flips)}/{len(flips)} = {np.mean(flips):.3f}; |logit-diff shift| median {np.median(s):.4f} mean {s.mean():.4f} max {s.max():.4f}")
    # SIGNED pseudo-shift, random masks only
    for m in ("M3", "M4"):
        vals = []
        for r in sess:
            st, sh = r["masks"][m]["state"], r["masks"][m]["shadow"]
            tag_plus_is_a = (r["menu_a"] == r["tag_plus"])
            plus_on_tag_plus = (m == "M3")     # M3: r+ on tag_plus's rounds; M4: r+ on tag_minus's rounds
            vals.append(signed_pseudo_shift(m, st, sh, tag_plus_is_a, plus_on_tag_plus))
        v = np.array(vals)
        out["pseudo_shift"][m] = {"mean": float(v.mean()), "sd": float(v.std(ddof=1)), "n_pos": int(np.sum(v > 0)), "n_neg": int(np.sum(v < 0)), "n": len(v),
                                  "values": [float(x) for x in v],
                                  "definition": "shift of logit(label whose rounds carried r+) - logit(other) relative to the shadow"}
        print(f"  PSEUDO-SHIFT {m} (toward the r+ label): mean {v.mean():+.4f} sd {v.std(ddof=1):.4f} pos/neg {np.sum(v > 0)}/{np.sum(v < 0)}")
    # identity summary
    idn = [r["masks"][m]["identity"] for r in sess for m in MASKS]
    out["identity"] = {"n_pairs": len(idn), "all_ok": all(i["ok"] for i in idn),
                       "max_shadow_p_a_vs_archived": max(i["shadow_p_a_vs_archived_abs"] for i in idn),
                       "max_shadow_mass_vs_archived": max(i["shadow_mass_vs_archived_abs"] for i in idn),
                       "max_choice_read_verify_kl": max(i["choice_read_verify_kl"] for i in idn),
                       "max_shadow_forward_vs_choice_read_abs_dpa": max(i["shadow_forward_vs_choice_read_abs_dpa"] for i in idn)}
    print(f"  IDENTITY: {out['identity']}")
    print(f"  STOP CLAUSE: {out['stop_clause']}")
    if out["stop_clause"]["fired"]:
        print("  FLAG: STOP CLAUSE FIRED -- a layer at or below the steering layer reads the mask")
    atomic_json(os.path.join(OUT, "stageA_analysis.json"), out)
    return out


# --- §3b Stage B ----------------------------------------------------------
def stage_b(adapter, rows, tasks, axis, rand, R48, frac, resume, limit=0):
    """All valid reward sessions, first free choice only (design block
    2026-09-05 §3b: the archived free3-free5 spans are the whole tail window,
    so later-position reads are withdrawn). Masks MASKS_B, each with its
    mandatory shadow; identity assertion per read; checkpointed per session;
    resume skip-only; refuses a foreign roster or dose."""
    os.makedirs(OUT, exist_ok=True)
    sel = valid_reward(rows)
    tag_ids = tag_ids_for(adapter)
    all64 = list(range(adapter.n_layers))
    meta_path = os.path.join(OUT, "stageB_reads.json")
    meta = {"stage": "B", "block": "design block 2026-09-05 §3b (RECON BLOCK §3.2, amended: first free choice only)",
            "sessions": [r["session"] for r in sel], "n_sessions": len(sel),
            "read_position": "first free choice (e2a primary position); text = transcript prefix through the first 'Config choice (one word):'",
            "config_of_record": {"layer": LAYER, "frac": frac, "alpha": axis.alpha, "R_48": R48,
                                 "axis_direction_sha_f64": axis.direction_sha,
                                 "random_direction": f"e0_random_dirs.npz[{RAND_KEY}]",
                                 "random_direction_sha": rand.direction_sha},
            "masks": {"M0": "off (the shadow of every pair)",
                      "M1": "as-generated polarity (axis)", "M2": "flipped (axis)",
                      "M3": "random direction, M1's sign pattern", "M4": "random direction, M2's sign pattern",
                      "M5": "same-pole ++ (axis, every forced round +)", "M6": "same-pole -- (axis)",
                      "M5x": "same-pole ++ (random direction)", "M6x": "same-pole -- (random direction)",
                      "R1..R4": "single round r steered at its as-generated pole (axis); the other rounds unsteered",
                      "R1x..R4x": "the same with the random direction"},
            "capture_layers": all64, "provenance": adapter.provenance(),
            "round_path_note": "archived texts were generated on the cached path (first-token licence); every recon forward is uncached",
            "per_session": {}}
    if resume and os.path.exists(meta_path):
        old = json.load(open(meta_path))
        if old.get("sessions") != meta["sessions"] or old["config_of_record"]["alpha"] != axis.alpha:
            raise SystemExit("resume refused: a different roster or dose is on disk")
        meta["per_session"] = old["per_session"]
    t_start = time.time()
    for k, row in enumerate(sel):
        sid = str(row["session"])
        npz_path = os.path.join(OUT, f"stageB_resid_s{sid}.npz")
        if sid in meta["per_session"] and os.path.exists(npz_path):
            continue
        prefix = choice_prefix(row["transcript"], 0)
        ts = token_spans(adapter, prefix, round_char_spans(row, tasks))
        if len(ts) != 4:
            raise AssertionError(f"s{sid}: expected 4 forced spans, got {len(ts)}")
        ch = row["choices"][0]
        a, b = ch["menu_a"], ch["menu_b"]
        n_tok = len(adapter.encode(prefix))
        rec = {"session": row["session"], "swap": row["swap"], "tag_plus": row["tag_plus"],
               "pair": row["pair"], "start_plus": row["start_plus"], "menu_a": a, "menu_b": b,
               "archived_read": {"pick": ch["pick"], "p_a": ch["p_a"], "label_mass": ch["label_mass"],
                                 "verify_kl": ch["verify_kl"], "picked_pole": ch["picked_pole"]},
               "spans": ts, "n_positions": n_tok, "read_position": n_tok - 1,
               "distance_to_read": {f"R{i + 1}": n_tok - t["tok_end"] for i, t in enumerate(ts)},
               "masks": {}}
        arrays = {"layers": np.array(all64, dtype=np.int32)}
        t0 = time.time()
        for mask in MASKS_B:
            pair = read_choice_maskedprefix(adapter, prefix, a, b, tag_ids,
                                            spans_with_injections(ts, mask, axis, rand),
                                            all64, sid, mask)
            d = pair.as_dict()
            dpa = abs(pair.shadow.p_a - ch["p_a"]); dmass = abs(pair.shadow.label_mass - ch["label_mass"])
            d["identity"] = {"shadow_p_a_vs_archived_abs": dpa, "shadow_mass_vs_archived_abs": dmass,
                             "shadow_pick_eq_archived": pair.shadow.pick == ch["pick"],
                             "choice_read_verify_kl": pair.shadow_choice_read.verify_kl,
                             "shadow_forward_vs_choice_read_abs_dpa": pair.shadow_vs_choice_read_abs_dpa,
                             "ok": bool(dpa <= 5e-4 and dmass <= 5e-4 and pair.shadow.pick == ch["pick"]
                                        and pair.shadow_choice_read.verify_kl == 0.0
                                        and pair.shadow_vs_choice_read_abs_dpa <= 1e-6)}
            rec["masks"][mask] = d
            arrays[f"{mask}|state"] = np.stack([pair.state.resid_last[l] for l in all64]).astype(np.float32)
            if mask == "M1":
                arrays["M0|shadow"] = np.stack([pair.shadow.resid_last[l] for l in all64]).astype(np.float32)
            else:
                # every shadow must equal M1's (identical ids, vanilla path)
                sh = np.stack([pair.shadow.resid_last[l] for l in all64]).astype(np.float32)
                if not np.array_equal(sh, arrays["M0|shadow"]):
                    atomic_json(meta_path, meta)
                    raise SystemExit(f"STOP: shadow residuals differ between masks at s{sid} {mask}")
            if not d["identity"]["ok"]:
                atomic_json(meta_path, meta)
                raise SystemExit(f"STOP: identity assertion failed at s{sid} {mask}: {d['identity']}")
        atomic_npz(npz_path, **arrays)
        rec["npz"] = os.path.relpath(npz_path, REPO)
        rec["npz_sha16_by_key"] = {kk: sha16_arr(v) for kk, v in arrays.items() if kk != "layers"}
        rec["seconds"] = time.time() - t0
        meta["per_session"][sid] = rec
        atomic_json(meta_path, meta)
        el = time.time() - t_start
        done = len(meta["per_session"])
        print(f"  s{sid:>3} ({done}/{len(sel)}) n={n_tok} identity ok  {rec['seconds']:.0f}s  elapsed {el / 60:.1f} min  "
              f"eta {(len(sel) - done) * rec['seconds'] / 60:.0f} min", flush=True)
        if limit and done >= limit:
            print(f"  --limit {limit} reached; stopping (resume continues skip-only)", flush=True)
            break
    meta["wall_clock_s"] = time.time() - t_start
    atomic_json(meta_path, meta)
    print(f"Stage B reads complete: {len(meta['per_session'])} sessions, {meta['wall_clock_s'] / 3600:.2f} h")


def _b_job(args):
    """One (family, layer): grouped 10-fold AUC + its shuffle null (same
    folds), LOSO point estimate beside."""
    name, l, X, y, g, n_shuffles, seed, k = args
    auc_k = PR.kfold_auc(X, y, g, k, seed)
    null = PR.kfold_shuffle_null(X, y, g, n_shuffles=n_shuffles, k=k, seed=seed + l)
    auc_loso = PR.loso_auc(X, y, g)
    return name, l, auc_k, float(np.percentile(null, 95)), float(np.mean(null)), float(np.max(null)), auc_loso


def analyze_b(n_shuffles, workers, workspace_layers, k=10):
    from concurrent.futures import ProcessPoolExecutor
    meta = json.load(open(os.path.join(OUT, "stageB_reads.json")))
    sess = sorted(meta["per_session"].values(), key=lambda r: r["session"])
    N = len(sess)
    layers_all = None
    probe_layers = sorted(set(workspace_layers) | set(range(LAYER, 64)))
    # one pass over the per-session files: per-layer stacks for the probe layers,
    # and the exact <=48 identity check on every layer.
    stacks = {}          # (mask, l) -> [N, D]
    le48_identical = True; le48_cells = 0; le48_bad = []
    for r in sess:
        z = np.load(os.path.join(REPO, r["npz"]))
        if layers_all is None:
            layers_all = [int(x) for x in z["layers"]]
        keys = [kk for kk in z.files if kk != "layers"]
        arr = {kk: z[kk] for kk in keys}
        for kk in keys:
            if sha16_arr(arr[kk]) != r["npz_sha16_by_key"][kk]:
                raise SystemExit(f"fingerprint mismatch s{r['session']} {kk}")
        sh = arr["M0|shadow"]
        for i, l in enumerate(layers_all):
            if l <= LAYER:
                for kk in keys:
                    le48_cells += 1
                    if not np.array_equal(arr[kk][i], sh[i]):
                        le48_identical = False; le48_bad.append((r["session"], kk, l))
            if l in probe_layers:
                for kk in keys:
                    stacks.setdefault((kk, l), []).append(arr[kk][i])
    stacks = {kk: np.stack(v) for kk, v in stacks.items()}
    groups = np.array([r["session"] for r in sess])
    forced_end_pos = np.array([1 if r["spans"][-1]["pole"] == "pos" else 0 for r in sess])
    a_is_plus = np.array([1 if r["menu_a"] == r["tag_plus"] else 0 for r in sess])
    round_pole = {rr: np.array([1 if r["spans"][rr]["pole"] == "pos" else 0 for r in sess]) for rr in range(4)}
    alpha = meta["config_of_record"]["alpha"]
    rw, _ = load_axis(LAYER); d = rw / np.linalg.norm(rw)
    two = lambda ma, mb, l: (np.concatenate([stacks[(f"{ma}|state", l)], stacks[(f"{mb}|state", l)]]), np.r_[groups, groups])
    fams = {}
    # (a) PRIMARY: sign injected on the last forced round
    fams["a1_lastsign_M1M2"] = lambda l: (*two("M1", "M2", l), np.r_[forced_end_pos, 1 - forced_end_pos])
    fams["a1c_lastsign_M3M4_random"] = lambda l: (*two("M3", "M4", l), np.r_[forced_end_pos, 1 - forced_end_pos])
    fams["a2_lastsign_M5M6"] = lambda l: (*two("M5", "M6", l), np.r_[np.ones(N), np.zeros(N)])
    fams["a2c_lastsign_M5xM6x_random"] = lambda l: (*two("M5x", "M6x", l), np.r_[np.ones(N), np.zeros(N)])
    # (b) label-bound polarity: pole of label_a under the mask
    fams["b_labelpole_M1M2"] = lambda l: (*two("M1", "M2", l), np.r_[a_is_plus, 1 - a_is_plus])
    fams["bc_labelpole_M3M4_random"] = lambda l: (*two("M3", "M4", l), np.r_[a_is_plus, 1 - a_is_plus])
    # (c) retention: R_r rows, target = that round's pole; random comparator; text-only baseline on the shadow rows
    for rr in range(4):
        fams[f"c_R{rr + 1}_roundpole"] = (lambda rr: (lambda l: (stacks[(f"R{rr + 1}|state", l)], groups, round_pole[rr])))(rr)
        fams[f"cc_R{rr + 1}x_roundpole_random"] = (lambda rr: (lambda l: (stacks[(f"R{rr + 1}x|state", l)], groups, round_pole[rr])))(rr)
        fams[f"cb_R{rr + 1}_roundpole_TEXTONLY_shadow"] = (lambda rr: (lambda l: (stacks[("M0|shadow", l)], groups, round_pole[rr])))(rr)
    jobs = []
    for fi, (name, fn) in enumerate(fams.items()):
        for l in probe_layers:
            X, g, y = fn(l)
            jobs.append((name, l, X, y, g, n_shuffles, 80260905 + 1000 * fi, k))
    t0 = time.time()
    res = {}
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for name, l, auc_k, p95, nm, nx, auc_loso in ex.map(_b_job, jobs, chunksize=1):
            res[(name, l)] = {"auc_kfold": auc_k, "shuffle95": p95, "shuffle_mean": nm, "shuffle_max": nx, "auc_loso": auc_loso, "above_null": auc_k > p95}
    print(f"  probes done in {(time.time() - t0) / 60:.1f} min ({len(jobs)} (family, layer) jobs; grouped {k}-fold, {n_shuffles} shuffles; LOSO beside)", flush=True)
    out = {"n_sessions": N, "n_shuffles": n_shuffles, "kfold": k, "alpha": alpha, "probe_layers": probe_layers,
           "procedure": f"standardized L2 logistic regression (discrim.logistic_auc hyperparameters); statistic and null under grouped {k}-fold CV (both rows of a session in one fold, seeded); leave-one-session-out point estimate beside",
           "le48_control": {"cells_checked": le48_cells, "all_identical_to_shadow": le48_identical, "first_bad": le48_bad[:5]},
           "families": {}, "per_session_geometry": {}, "leak": {}, "pseudo_shift": {}, "label_differential": {}, "retention": {}}
    for name in fams:
        out["families"][name] = {str(l): res[(name, l)] for l in probe_layers}
    # tables
    def table(names, title):
        print(f"\n  {title}")
        print("  " + "layer".rjust(6) + "".join(n[:22].rjust(24) for n in names))
        for l in probe_layers:
            cells = []
            for n in names:
                r = res[(n, l)]
                cells.append(f"{r['auc_kfold']:.3f}/{r['shuffle95']:.2f}{'*' if r['above_null'] else ' '}".rjust(24))
            print("  " + str(l).rjust(6) + "".join(cells))
    table(["a1_lastsign_M1M2", "a1c_lastsign_M3M4_random", "a2_lastsign_M5M6", "a2c_lastsign_M5xM6x_random"], "(a) LAST-ROUND SIGN: AUC(10-fold)/shuffle95, * = above null")
    table(["b_labelpole_M1M2", "bc_labelpole_M3M4_random"], "(b) LABEL-BOUND POLARITY (pole of label_a)")
    for rr in range(4):
        table([f"c_R{rr + 1}_roundpole", f"cc_R{rr + 1}x_roundpole_random", f"cb_R{rr + 1}_roundpole_TEXTONLY_shadow"], f"(c) RETENTION R{rr + 1}: that round's pole")
    # retention distances
    for rr in range(4):
        dist = np.array([r["distance_to_read"][f"R{rr + 1}"] for r in sess])
        out["retention"][f"R{rr + 1}"] = {"tokens_last_steered_to_read": {"mean": float(dist.mean()), "min": int(dist.min()), "max": int(dist.max()), "median": float(np.median(dist))},
                                          "round_pole_balance": {"pos": int(round_pole[rr].sum()), "neg": int(N - round_pole[rr].sum())}}
        print(f"  R{rr + 1}: tokens from last steered position to read: mean {dist.mean():.1f} (min {dist.min()}, max {dist.max()}); pole balance {out['retention'][f'R{rr + 1}']['round_pole_balance']}")
    # per-session geometry: M1-M2 and M5-M6 paired norm/2a and cos(d), per layer
    print("\n  per-session paired geometry (mean +/- sd over sessions): norm/2a, cos(d)")
    for pair_name, (ma, mb) in (("M1-M2", ("M1", "M2")), ("M5-M6", ("M5", "M6"))):
        out["per_session_geometry"][pair_name] = {}
        for l in probe_layers:
            V = stacks[(f"{ma}|state", l)].astype(np.float64) - stacks[(f"{mb}|state", l)].astype(np.float64)
            nrm = np.linalg.norm(V, axis=1)
            cos = (V @ d) / np.where(nrm > 0, nrm, 1.0)
            out["per_session_geometry"][pair_name][str(l)] = {"norm_over_2alpha_mean": float(nrm.mean() / (2 * alpha)), "norm_over_2alpha_sd": float(nrm.std(ddof=1) / (2 * alpha)),
                                                              "cos_d_mean": float(cos.mean()), "cos_d_sd": float(cos.std(ddof=1)),
                                                              "classmean_norm_over_2alpha": float(np.linalg.norm(V.mean(0)) / (2 * alpha))}
        line = " ".join(f"L{l}:{out['per_session_geometry'][pair_name][str(l)]['norm_over_2alpha_mean']:.3f}/{out['per_session_geometry'][pair_name][str(l)]['cos_d_mean']:+.3f}" for l in probe_layers if l > LAYER)
        print(f"  {pair_name}: {line}")
    # LEAK (unsigned) on M1, M2, M5, M6, R1..R4
    for m in ("M1", "M2", "M5", "M6", "R1", "R2", "R3", "R4"):
        flips = []; shifts = []
        for r in sess:
            st, sh = r["masks"][m]["state"], r["masks"][m]["shadow"]
            flips.append(int(st["pick"] != sh["pick"]))
            shifts.append(abs((st["logit_a"] - st["logit_b"]) - (sh["logit_a"] - sh["logit_b"])))
        s_ = np.array(shifts)
        out["leak"][m] = {"pi_d": float(np.mean(flips)), "n_flips": int(np.sum(flips)), "n": len(flips),
                          "abs_logit_diff_shift": {"min": float(s_.min()), "median": float(np.median(s_)), "mean": float(s_.mean()), "max": float(s_.max()), "values": [float(x) for x in s_]}}
        print(f"  LEAK {m}: pi_d = {np.sum(flips)}/{len(flips)} = {np.mean(flips):.3f}; |logit-diff shift| median {np.median(s_):.4f} mean {s_.mean():.4f} max {s_.max():.4f}")
    # SIGNED pseudo-shift, random masks (toward the r+ label)
    for m in ("M3", "M4"):
        vals = np.array([signed_pseudo_shift(m, r["masks"][m]["state"], r["masks"][m]["shadow"], r["menu_a"] == r["tag_plus"], m == "M3") for r in sess])
        out["pseudo_shift"][m] = {"mean": float(vals.mean()), "sd": float(vals.std(ddof=1)), "n_pos": int(np.sum(vals > 0)), "n_neg": int(np.sum(vals < 0)), "n": len(vals), "values": [float(x) for x in vals]}
        print(f"  PSEUDO-SHIFT {m} (toward the r+ label): mean {vals.mean():+.4f} sd {vals.std(ddof=1):.4f} pos/neg {np.sum(vals > 0)}/{np.sum(vals < 0)}")
    # SIGNED label-differential on M5/M6 (toward label_a; no contrast -> arithmetic + label artifact)
    for m in ("M5", "M6", "M5x", "M6x"):
        vals = np.array([(r["masks"][m]["state"]["logit_a"] - r["masks"][m]["state"]["logit_b"]) - (r["masks"][m]["shadow"]["logit_a"] - r["masks"][m]["shadow"]["logit_b"]) for r in sess])
        out["label_differential"][m] = {"definition": "shift of logit(label_a) - logit(label_b) relative to the shadow (toward the first-listed menu label)", "mean": float(vals.mean()), "sd": float(vals.std(ddof=1)), "n_pos": int(np.sum(vals > 0)), "n_neg": int(np.sum(vals < 0)), "n": len(vals), "values": [float(x) for x in vals]}
        print(f"  LABEL-DIFFERENTIAL {m} (toward label_a): mean {vals.mean():+.4f} sd {vals.std(ddof=1):.4f} pos/neg {np.sum(vals > 0)}/{np.sum(vals < 0)}")
    idn = [r["masks"][m]["identity"] for r in sess for m in MASKS_B]
    out["identity"] = {"n_pairs": len(idn), "all_ok": all(i["ok"] for i in idn),
                       "max_shadow_p_a_vs_archived": max(i["shadow_p_a_vs_archived_abs"] for i in idn),
                       "max_shadow_mass_vs_archived": max(i["shadow_mass_vs_archived_abs"] for i in idn),
                       "max_choice_read_verify_kl": max(i["choice_read_verify_kl"] for i in idn),
                       "max_shadow_forward_vs_choice_read_abs_dpa": max(i["shadow_forward_vs_choice_read_abs_dpa"] for i in idn)}
    below_bad = [l for l in probe_layers if l <= LAYER and any(res[(n, l)]["above_null"] for n in fams)]
    out["stop_clause"] = {"le48_bit_identical_to_shadow_all_masks": le48_identical, "cells": le48_cells,
                          "probe_layers_le48_above_null": below_bad, "fired": (not le48_identical) or bool(below_bad)}
    print(f"  IDENTITY: {out['identity']}")
    print(f"  STOP CLAUSE: {out['stop_clause']}")
    if out["stop_clause"]["fired"]:
        print("  FLAG: STOP CLAUSE FIRED")
    atomic_json(os.path.join(OUT, "stageB_analysis.json"), out)
    return out


def analyze_a_posthoc(n_shuffles, workers, layers_wanted):
    """POST-HOC, DESCRIPTIVE, NOT PART OF §3.1's REGISTERED READOUTS (rule 11:
    licenses a pre-registration, never a verdict). Prompted by a structural
    observation on the Stage A result: under e2a's alternating forced order
    [f, -f, f, -f] an additive echo whose sign tracks the nearest steered
    round flips sign between start-pole halves of the roster, so the
    registered M1-vs-M2 target cannot see it by construction. The one extra
    probe that can: target = the INJECTED SIGN OF THE LAST FORCED ROUND
    (= forced_end pole under M1, its negation under M2), examples = the same
    M1 and M2 rows (texts identical within a session, labels opposite within
    a session, balanced across sessions). It is a relabelling of the same
    rows -- no new forward, no reward-mask DV, nothing signed toward a label.
    Comparator: the same relabelling on M3/M4."""
    from concurrent.futures import ProcessPoolExecutor
    meta = json.load(open(os.path.join(OUT, "stageA_reads.json")))
    sess = sorted(meta["per_session"].values(), key=lambda r: r["session"])
    layers = None; resid = {}
    for r in sess:
        z = np.load(os.path.join(REPO, r["npz"]))
        if layers is None:
            layers = [int(x) for x in z["layers"]]
        for k in z.files:
            if k != "layers":
                resid[(r["session"], k)] = z[k]
    li = {l: i for i, l in enumerate(layers)}
    groups = np.array([r["session"] for r in sess])
    last_pos = np.array([1 if r["spans"][-1]["pole"] == "pos" else 0 for r in sess])   # forced_end pole
    out = {"post_hoc": True, "rule_11": "post-hoc descriptive relabelling of the Stage A rows; licenses a pre-registration, never a verdict",
           "target": "injected sign of the LAST forced round: +1 for (M1, forced_end=pos) and (M2, forced_end=neg), else -1; identical text within a session, opposite labels within a session",
           "forced_end_balance": {"pos": int(last_pos.sum()), "neg": int(len(last_pos) - last_pos.sum())},
           "n_shuffles": n_shuffles, "per_layer": {}}
    sel = [l for l in layers if l in layers_wanted]

    def job(l, ma, mb, seed):
        XA = np.stack([resid[(r["session"], f"{ma}|state")][li[l]] for r in sess])
        XB = np.stack([resid[(r["session"], f"{mb}|state")][li[l]] for r in sess])
        # relabel: rows of A get last_pos, rows of B get 1 - last_pos
        X = np.concatenate([XA, XB]); y = np.r_[last_pos, 1 - last_pos]; g = np.r_[groups, groups]
        return (l, X, y, g, n_shuffles, seed)
    jobs_r = [job(l, "M1", "M2", 40260905) for l in sel]
    jobs_c = [job(l, "M3", "M4", 50260905) for l in sel]
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res_r = {r[0]: r for r in ex.map(_relabel_job, jobs_r)}
        res_c = {r[0]: r for r in ex.map(_relabel_job, jobs_c)}
    print(f"  post-hoc probes done in {(time.time() - t0) / 60:.1f} min", flush=True)
    print(f"  POST-HOC target = injected sign of the LAST forced round (forced_end {out['forced_end_balance']})")
    print(f"  {'layer':>5} {'type':>6} {'AUC_reward':>10} {'shuffle95':>9} {'AUC_random':>10} {'shuffle95r':>10}")
    for l in sel:
        _, a, p95, nm, nx = res_r[l]; _, ac, p95c, _, _ = res_c[l]
        out["per_layer"][str(l)] = {"auc_reward_lastround_sign": a, "shuffle95_reward": p95, "shuffle_mean_reward": nm, "shuffle_max_reward": nx,
                                    "auc_random_lastround_sign": ac, "shuffle95_random": p95c,
                                    "reward_above_shuffle95": a > p95, "random_above_shuffle95": ac > p95c}
        flag = " <-- above null" if a > p95 else ""
        print(f"  {l:>5} {'above' if l > LAYER else ('steer' if l == LAYER else 'below'):>6} {a:10.3f} {p95:9.3f} {ac:10.3f} {p95c:10.3f}{flag}")
    atomic_json(os.path.join(OUT, "stageA_posthoc_lastround.json"), out)
    return out


def analyze_a_posthoc2(n_shuffles, workers, layers_wanted):
    """POST-HOC #2 (design block 2026-09-05 §3a; rule 11, flagged): target =
    the POLE OF label_a UNDER THE MASK -- the well-posed label-bound polarity.
    Under M1 label_a's rounds carry + iff label_a == tag_plus; under M2 the
    reverse. Same rows, no new forward. Comparator: M3/M4 with r+ as '+'."""
    from concurrent.futures import ProcessPoolExecutor
    meta = json.load(open(os.path.join(OUT, "stageA_reads.json")))
    sess = sorted(meta["per_session"].values(), key=lambda r: r["session"])
    layers = None; resid = {}
    for r in sess:
        z = np.load(os.path.join(REPO, r["npz"]))
        if layers is None:
            layers = [int(x) for x in z["layers"]]
        for k in z.files:
            if k != "layers":
                resid[(r["session"], k)] = z[k]
    li = {l: i for i, l in enumerate(layers)}
    groups = np.array([r["session"] for r in sess])
    a_is_plus = np.array([1 if r["menu_a"] == r["tag_plus"] else 0 for r in sess])
    out = {"post_hoc": True, "rule_11": "post-hoc descriptive relabelling of the Stage A rows (design block 2026-09-05 §3a); licenses a pre-registration, never a verdict",
           "target": "pole of label_a under the mask: +1 iff label_a's rounds carried the + pole (M1: label_a == tag_plus; M2: label_a == tag_minus); comparator M3/M4 with r+ as '+'",
           "label_a_is_tag_plus_balance": {"yes": int(a_is_plus.sum()), "no": int(len(a_is_plus) - a_is_plus.sum())},
           "n_shuffles": n_shuffles, "per_layer": {}}
    sel = [l for l in layers if l in layers_wanted]

    def job(l, ma, mb, seed):
        XA = np.stack([resid[(r["session"], f"{ma}|state")][li[l]] for r in sess])
        XB = np.stack([resid[(r["session"], f"{mb}|state")][li[l]] for r in sess])
        X = np.concatenate([XA, XB]); y = np.r_[a_is_plus, 1 - a_is_plus]; g = np.r_[groups, groups]
        return (l, X, y, g, n_shuffles, seed)
    jobs_r = [job(l, "M1", "M2", 60260905) for l in sel]
    jobs_c = [job(l, "M3", "M4", 70260905) for l in sel]
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res_r = {r[0]: r for r in ex.map(_relabel_job, jobs_r)}
        res_c = {r[0]: r for r in ex.map(_relabel_job, jobs_c)}
    print(f"  post-hoc #2 probes done in {(time.time() - t0) / 60:.1f} min", flush=True)
    print(f"  POST-HOC #2 target = pole of label_a under the mask (label_a is tag_plus: {out['label_a_is_tag_plus_balance']})")
    print(f"  {'layer':>5} {'type':>6} {'AUC_reward':>10} {'shuffle95':>9} {'AUC_random':>10} {'shuffle95r':>10}")
    for l in sel:
        _, a, p95, nm, nx = res_r[l]; _, ac, p95c, _, _ = res_c[l]
        out["per_layer"][str(l)] = {"auc_reward_labelpole": a, "shuffle95_reward": p95, "shuffle_mean_reward": nm, "shuffle_max_reward": nx,
                                    "auc_random_labelpole": ac, "shuffle95_random": p95c,
                                    "reward_above_shuffle95": a > p95, "random_above_shuffle95": ac > p95c}
        flag = " <-- above null" if a > p95 else ""
        print(f"  {l:>5} {'above' if l > LAYER else ('steer' if l == LAYER else 'below'):>6} {a:10.3f} {p95:9.3f} {ac:10.3f} {p95c:10.3f}{flag}")
    atomic_json(os.path.join(OUT, "stageA_posthoc2_labelpole.json"), out)
    return out


def _relabel_job(args):
    l, X, y, g, n_shuffles, seed = args
    auc = PR.loso_auc(X, y, g)
    null = PR.shuffle_null(X, y, g, n_shuffles=n_shuffles, seed=seed + l)
    return l, auc, float(np.percentile(null, 95)), float(np.mean(null)), float(np.max(null))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--stage", choices=["timing", "a", "b"])
    ap.add_argument("--analyze", choices=["a", "a-posthoc", "a-posthoc2", "b"])
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--workspace-layers", default="", help="comma-separated (from the recon §1a read)")
    ap.add_argument("--limit", type=int, default=0, help="stage b: stop after this many NEW sessions (smoke); resume continues")
    args = ap.parse_args()
    if args.selftest:
        return 0 if selftest() else 1
    if args.analyze == "a":
        ws = {int(x) for x in args.workspace_layers.split(",") if x.strip()}
        analyze_a(args.shuffles, args.workers, ws)
        return 0
    if args.analyze == "a-posthoc":
        ws = {int(x) for x in args.workspace_layers.split(",") if x.strip()}
        analyze_a_posthoc(args.shuffles, args.workers, ws | set(range(LAYER, 64)))
        return 0
    if args.analyze == "b":
        ws = {int(x) for x in args.workspace_layers.split(",") if x.strip()}
        analyze_b(args.shuffles, args.workers, ws)
        return 0
    if args.analyze == "a-posthoc2":
        ws = {int(x) for x in args.workspace_layers.split(",") if x.strip()}
        analyze_a_posthoc2(args.shuffles, args.workers, ws | set(range(LAYER, 64)))
        return 0
    rows = load_rows()
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    frac = dose_of_record(rows)
    axis, rand, R48 = make_injections(frac)
    print(f"config of record: L{LAYER} frac {frac} alpha {axis.alpha:.4f} (R_48 {R48:.2f}); "
          f"axis sha {axis.direction_sha}; random {RAND_KEY} sha {rand.direction_sha}", flush=True)
    adapter = load_adapter()
    if args.stage == "timing":
        os.makedirs(OUT, exist_ok=True)
        stage_timing(adapter, rows, tasks, axis, rand, os.path.join(OUT, "timing.json"))
    elif args.stage == "a":
        stage_a(adapter, rows, tasks, axis, rand, R48, frac, args.resume)
    elif args.stage == "b":
        stage_b(adapter, rows, tasks, axis, rand, R48, frac, args.resume, args.limit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
