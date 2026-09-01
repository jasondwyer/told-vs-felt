"""Ledger 26, oracle tier: the three acceptance criteria that require the
laptop Qwen model, run through `valence_core` end to end.

    uv run python -m valence_core.regression.oracle [--check all|kernel|b2b|choiceread]

CLAUDE.md §Phase 0 step 1: "Acceptance = rule 26: through the new core,
reproduce (i) the g1r kernel-gate KLs (7.11e-4 / 7.39e-4 +/- tolerance),
(ii) a 128-context B2b subsample (delta+/delta- within CI), (iii) e2a
choice-read construction KL = 0.0 exactly on archived session texts."

Every number below is compared against an artifact committed to the repo.
Rule 26's disposition clause governs the reading: **a mismatch is a refactor
bug until proven otherwise.** This script never explains a difference away;
it prints it.

Criterion (iii) is stronger here than the letter requires. The archived
sessions store `p_a`, `label_mass`, `pick` and `top1_is_label` alongside
`verify_kl`, so rather than only checking that a re-forward is self-
consistent, the port is checked against the *recorded DV* of every sampled
choice. A construction that drifted would show up as a changed p_a even if
its verify KL were a clean zero.

Every input now lives in the record (2026-08-20): the e2a/e0 task corpora,
the e0 probe set, and the B1 marker artifact were pulled out of the
gitignored clone so this tier is reproducible from the repo alone. Only the
Qwen weights themselves come from outside it. A missing input is still
reported as SKIP with its reason, never as a pass.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass

import numpy as np

from ..adapters.base import Injection, PositionSpec
from ..readout import choice_read, softmax, symmetric_kl

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(REPO, "data")

LAYER = 48
KERNEL_FRACS = (0.10, 0.20)
KERNEL_REF = {"0.1": 7.106405682861805e-04, "0.2": 7.390632526949048e-04}
KERNEL_TOL = 0.02                      # 2% relative
B2B_LAYER, B2B_FRAC = 48, 0.10
VAL_TASKS_B2B = [f"e{i:02d}" for i in range(25, 49)]
SEL = 256
G_EXPECTED = 0.3156
N_CHOICE_READS = 48

# --- criterion (ii), TIGHTENED. Pre-registered 2026-08-12, committed
# --- before the run that evaluates it. -----------------------------------
#
# The original form ("a 128-context B2b subsample, delta+/delta- within CI")
# was under-powered, and its own first run showed why: the 90% interval came
# out at +/-0.359 against an effect of +0.295, so it was wider than the
# quantity it tested and would have accepted almost any same-sign result.
#
# The defect was NOT sample size -- it was that the interval was *unpaired*.
# It was built from the spread of the 12 per-probe deltas, which are
# enormously heterogeneous by construction (published axis_pos per_probe
# runs +2.481 down to -0.4163). That between-probe spread is a property of
# the instrument battery, is shared by both measurements, and cancels
# exactly when the comparison is paired probe-to-probe.
#
# Three changes, in increasing order of importance:
#
#   1. STRATIFIED sampling -- equal contexts per probe, so "which probes got
#      sampled" stops being a noise source. N_PER_PROBE = None runs the full
#      96/probe (1152/arm), i.e. an exact reproduction with no subsampling
#      noise at all.
#   2. PAIRED per-probe equivalence via TOST against the published
#      per_probe vector. This inverts the burden of proof, which is the
#      real point: the old test failed only if the reproduction was wildly
#      off, so noise helped it pass. An equivalence test can only pass by
#      being *close*. Margin = 0.5*G = 0.1578, the pre-registered V1 bar
#      quantity -- a per-probe reproduction error smaller than this cannot
#      move any verdict conjunct.
#   3. VERDICT PRESERVATION -- re-evaluate the original pre-registered V1
#      PASS rule (D+ >= 0.5G AND D- <= -0.5G AND min(D+,|D-|) > 2*max|D_rand|)
#      on the reproduced arms, which requires the random arms too. This is
#      the conjunct that actually matters to a reader: not "do the numbers
#      look similar" but "would the refactored core have produced the same
#      published verdict".
#
# Acceptance = all three conjuncts, for axis_pos and axis_neg.
N_PER_PROBE: int | None = None      # None = full 96/probe = exact reproduction
B2B_TOST_MARGIN = 0.1578            # 0.5 * G
B2B_POINT_TOL = 0.05                # sigma units, scalar |delta| deviation
B2B_VERDICT_ARMS = ("axis_pos", "axis_neg", "rand_pos", "rand_neg")


@dataclass
class Result:
    name: str
    expected: str
    got: str
    ok: bool
    note: str = ""


def _banner(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def load_axis(layer: int = LAYER):
    """Frozen reward axis + R_l from the committed artifacts (sha-verified
    inside `Injection.at_frac` via `expect_sha`)."""
    Z = np.load(os.path.join(DATA, "e0/e0_axes.npz"))
    meta = json.load(open(os.path.join(DATA, "e0/e0_axes.meta.json")))
    layers = [int(x) for x in Z["layers"]]
    rw = Z["span_reward"][layers.index(layer)].astype(np.float64)
    R = {int(k): float(v) for k, v in meta["R_per_layer_spanmean"].items()}
    return rw, R


# --- (i) kernel gate ------------------------------------------------------
def check_kernel(adapter, tasks, tag_ids) -> list[Result]:
    """32 probes/frac (16 session-style prefixes x 2 poles): first-response-
    token distribution from the cached O(T) stream vs the uncached positional
    re-forward. The gate is symmetric KL <= 1e-3 nats; the published maxima
    are the numbers being reproduced."""
    from ..session import DEFAULT_SCAFFOLD_STRINGS  # noqa: F401  (documented dep)

    ROUND_TEMPLATES = [
        "[round {n} | config: {tag}]\nTask: {task}\nResponse:",
        "[round {n} — active config: {tag}]\nTask: {task}\nResponse:",
        "[round {n} | running config: {tag}]\nTask: {task}\nResponse:",
        "[round {n} — config in use: {tag}]\nTask: {task}\nResponse:",
    ]
    BANNER = "=== Config evaluation session ===\n"
    rw, R = load_axis(LAYER)
    tags_flat = list(tag_ids)[:8]

    probes = [ROUND_TEMPLATES[i % 4].format(
        n=1, tag=tags_flat[i % 8], task=tasks[i]["paraphrases"][0])
        for i in range(16)]

    out = []
    for frac in KERNEL_FRACS:
        worst = 0.0
        t0 = time.time()
        for sign, pole in ((+1, "pos"), (-1, "neg")):
            inj = Injection.at_frac(rw, LAYER, sign * frac, R)
            for pi, seg in enumerate(probes):
                dists = {}
                for cached in (True, False):
                    g = adapter.generate(BANNER, seg, injections=[inj],
                                         seed=1000 + pi, temp=0.7,
                                         max_tokens=1, cached=cached)
                    dists[cached] = softmax(g.first_logits)
                worst = max(worst, symmetric_kl(dists[True], dists[False]))
        ref = KERNEL_REF[str(frac)]
        rel = abs(worst - ref) / ref
        print(f"  frac {frac}: max symmetric KL {worst:.4e}  "
              f"(published {ref:.4e}, rel {rel:+.2%})  "
              f"[{time.time() - t0:.0f}s]", flush=True)
        out.append(Result(
            f"g1r kernel-gate max KL @ frac {frac}", f"{ref:.4e}",
            f"{worst:.4e}", rel <= KERNEL_TOL,
            note=f"rel {rel:+.2%}, gate bar 1e-3 "
                 f"{'held' if worst <= 1e-3 else 'BREACHED'}"))
    return out


# --- (ii) B2b subsample ---------------------------------------------------
def build_instruments():
    """The 12 locked per-probe instruments, recomputed from the frozen B1
    artifact exactly as `e0_v1_hijack_b2.build_instruments` does. G is
    asserted against its pre-registered value -- if G drifts, nothing
    downstream is comparable."""
    b1 = os.path.join(DATA, "e0/e0_b1_markers.npz")
    if not os.path.exists(b1):
        return None, None
    Z = np.load(b1)
    top_ids, top_vals = Z["top_ids"], Z["top_vals"]
    tid, cond, qidx = Z["task_id"], Z["cond"], Z["probe"]
    fit_ids = sorted({f"e{i:02d}" for i in range(1, 25)})
    in_fit = np.isin(tid, fit_ids)
    is_pos = cond == "self_pos"
    floor = top_vals.min(axis=1) - 2.0
    instruments, g_list = [], []
    for qi in range(int(qidx.max()) + 1):
        qm = qidx == qi
        halves = {}
        for label, mask in (("p", qm & in_fit & is_pos),
                            ("n", qm & in_fit & ~is_pos)):
            rows = np.where(mask)[0]
            a = {}
            for i in rows:
                for j, v in zip(top_ids[i], top_vals[i]):
                    a[j] = a.get(j, 0.0) + v
            halves[label] = (a, len(rows), float(floor[mask].mean()))
        (ap, n_p, flp), (an, n_n, fln) = halves["p"], halves["n"]
        keys = set(ap) | set(an)
        diffs = {k: ap.get(k, flp * n_p) / n_p - an.get(k, fln * n_n) / n_n
                 for k in keys}
        sel = sorted(diffs, key=lambda k: -abs(diffs[k]))[:SEL]
        w = np.array([diffs[k] for k in sel], dtype=np.float64)
        w /= np.linalg.norm(w) + 1e-12

        def scores_for(mask, sel=sel):
            pos_of = {k: t for t, k in enumerate(sel)}
            out = []
            for i in np.where(mask)[0]:
                x = np.full(len(sel), floor[i])
                for j, v in zip(top_ids[i], top_vals[i]):
                    if j in pos_of:
                        x[pos_of[j]] = v
                out.append(float(w @ x))
            return np.array(out)

        sp = scores_for(qm & ~in_fit & is_pos)
        sn = scores_for(qm & ~in_fit & ~is_pos)
        sd = float(np.sqrt((sp.var(ddof=1) + sn.var(ddof=1)) / 2))
        g_list.append(float((sp.mean() - sn.mean()) / (sd + 1e-12)))
        instruments.append({"sel_ids": np.array(sel, dtype=np.int64),
                            "w": w, "sigma": sd})
    return instruments, float(np.mean(g_list))


def check_b2b(adapter) -> list[Result]:
    instruments, G = build_instruments()
    if instruments is None:
        return [Result("B2b reproduction", "delta +.2848/-.3946",
                       "SKIP", False,
                       note="e0_b1_markers.npz absent from the record")]
    if abs(G - G_EXPECTED) > 1e-3:
        return [Result("B2b instrument G", f"{G_EXPECTED}", f"{G:.6f}", False,
                       note="instrument drift -- nothing downstream comparable")]
    print(f"  instruments rebuilt: G = {G:.6f} (expected {G_EXPECTED})",
          flush=True)

    tasks_p = os.path.join(DATA, "corpus/e0_tasks.jsonl")
    probes_p = os.path.join(DATA, "configs/e0_probes.json")
    if not (os.path.exists(tasks_p) and os.path.exists(probes_p)):
        return [Result("B2b reproduction", "delta +.2848/-.3946",
                       "SKIP", False, note="e0 corpus absent from the record")]
    tasks = {json.loads(l)["id"]: json.loads(l)
             for l in open(tasks_p) if l.strip()}
    probes = json.load(open(probes_p))["probes"]

    contexts = []
    for t_id in VAL_TASKS_B2B:
        t = tasks[t_id]
        for _pi in range(4):
            for qi, probe in enumerate(probes):
                contexts.append((qi, f"Task: {t['task']}\n"
                                     f"Response: {t['completion']}\n"
                                     f"Task: {probe}\nResponse:"))
    print(f"  full val-half contexts: {len(contexts)} (published arm size 1152)",
          flush=True)

    # Stratified: equal contexts per probe. N_PER_PROBE None -> take all,
    # which makes this an exact reproduction rather than a subsample.
    by_probe: dict[int, list] = {}
    for qi, text in contexts:
        by_probe.setdefault(qi, []).append((qi, text))
    rng = np.random.default_rng(26)               # declared sampling seed
    sub = []
    for qi in sorted(by_probe):
        pool = by_probe[qi]
        if N_PER_PROBE is None or N_PER_PROBE >= len(pool):
            sub.extend(pool)
        else:
            idx = sorted(rng.choice(len(pool), size=N_PER_PROBE, replace=False))
            sub.extend(pool[i] for i in idx)
    per_probe_n = len(sub) // len(by_probe)
    print(f"  stratified: {len(sub)} contexts/arm, {per_probe_n}/probe "
          f"across {len(by_probe)} probes"
          + ("  [FULL -- exact reproduction, no subsampling noise]"
             if N_PER_PROBE is None else ""), flush=True)

    rw, R = load_axis(B2B_LAYER)
    Rz = np.load(os.path.join(DATA, "e0/e0_random_dirs.npz"))
    rand_u = Rz[f"L{B2B_LAYER}"].astype(np.float64)

    def arm_scores(injections, tag):
        scores = [[] for _ in instruments]
        t0 = time.time()
        for n, (qi, text) in enumerate(sub, start=1):
            res = adapter.forward(adapter.encode(text), capture_layers=(),
                                  injections=injections)
            lg = res.logits.astype(np.float64)
            lp = lg - (np.log(np.exp(lg - lg.max()).sum()) + lg.max())
            inst = instruments[qi]
            scores[qi].append(float(inst["w"] @ lp[inst["sel_ids"]]))
            if n % 32 == 0:
                print(f"    [{tag}] {n}/{len(sub)} "
                      f"{time.time() - t0:.0f}s", flush=True)
        return scores

    def delta(arm, base):
        ds = []
        for qi, inst in enumerate(instruments):
            if not arm[qi]:
                continue
            ds.append((np.mean(arm[qi]) - np.mean(base[qi])) /
                      (inst["sigma"] + 1e-12))
        return float(np.mean(ds)), np.array(ds)

    from ..stats import paired_tost

    base = arm_scores([], "base")
    arms = {}
    for name, u, sign in (("axis_pos", rw, +1), ("axis_neg", rw, -1),
                          ("rand_pos", rand_u, +1), ("rand_neg", rand_u, -1)):
        inj = Injection.at_frac(u, B2B_LAYER, sign * B2B_FRAC, R)
        arms[name] = delta(arm_scores([inj], name), base)

    ref = json.load(open(os.path.join(DATA, "e0/e0_b2_b2b.json")))
    ref_arms, published_crit = ref["arms"], ref["criterion"]
    out = []

    # --- conjunct 1: paired per-probe equivalence (TOST) ------------------
    for name in ("axis_pos", "axis_neg"):
        d, per = arms[name]
        pub_per = np.array(ref_arms[name]["per_probe"], dtype=np.float64)
        t = paired_tost(per, pub_per, B2B_TOST_MARGIN)
        lo, hi = t.ci
        print(f"  {name}: paired per-probe mean diff {t.mean_diff:+.4f}  "
              f"90% CI [{lo:+.4f}, {hi:+.4f}]  margin +/-{t.margin}  -> "
              f"{'EQUIVALENT' if t.equivalent else 'NOT equivalent'}",
              flush=True)
        # Full precision into the note: the published `per_probe` is stored
        # rounded to 4dp, so 4dp is the ceiling of what this comparison can
        # *claim*, but the reproduced side's own magnitudes are worth having
        # in the record rather than rounded away (ledger 27).
        out.append(Result(
            f"B2b {name} paired per-probe TOST",
            f"CI within +/-{t.margin}", f"[{lo:+.4f}, {hi:+.4f}]",
            t.equivalent,
            note=f"mean diff {t.mean_diff:+.3e}, max|per-probe diff| "
                 f"{float(np.max(np.abs(per - pub_per))):.3e}, "
                 f"n={t.n} probes, half-width {t.half_width:.3e} "
                 f"(published per_probe is 4dp-rounded: that is the "
                 f"precision ceiling of this comparison)"))

    # --- conjunct 2: scalar point estimate --------------------------------
    for name in ("axis_pos", "axis_neg"):
        d, _ = arms[name]
        pub = ref_arms[name]["delta"]
        dev = abs(d - pub)
        print(f"  {name}: delta {d:+.4f}  published {pub:+.4f}  "
              f"|dev| {dev:.4f} vs tol {B2B_POINT_TOL}  -> "
              f"{'ok' if dev <= B2B_POINT_TOL else 'OUT OF TOLERANCE'}",
              flush=True)
        out.append(Result(f"B2b {name} point estimate", f"{pub:+.4f}",
                          f"{d:+.4f}", dev <= B2B_POINT_TOL,
                          note=f"|dev| {dev:.4f} <= {B2B_POINT_TOL}"))

    # --- conjunct 3: verdict preservation ---------------------------------
    half_g = 0.5 * G
    d_pos, d_neg = arms["axis_pos"][0], arms["axis_neg"][0]
    max_rand = max(abs(arms["rand_pos"][0]), abs(arms["rand_neg"][0]))
    v1 = (d_pos >= half_g and d_neg <= -half_g
          and min(d_pos, abs(d_neg)) > 2 * max_rand)
    print(f"  V1 rule: D+ {d_pos:+.4f} >= {half_g:.4f} AND "
          f"D- {d_neg:+.4f} <= {-half_g:.4f} AND "
          f"min {min(d_pos, abs(d_neg)):.4f} > 2*max|D_rand| "
          f"{2 * max_rand:.4f}  -> {'PASS' if v1 else 'FAIL'}", flush=True)
    print(f"    (published: D+ {published_crit['D_pos']:+.4f}, "
          f"D- {published_crit['D_neg']:+.4f}, "
          f"max|D_rand| {published_crit['max_abs_D_rand']:.4f}, "
          f"V1_PASS {published_crit['V1_PASS']})", flush=True)
    out.append(Result(
        "B2b V1 verdict preserved", f"PASS (published {published_crit['V1_PASS']})",
        "PASS" if v1 else "FAIL", v1 == bool(published_crit["V1_PASS"]),
        note=f"D+ {d_pos:+.4f}, D- {d_neg:+.4f}, "
             f"max|D_rand| {max_rand:.4f} (published {published_crit['max_abs_D_rand']:.4f})"))
    return out


# --- (iii) choice-read construction ---------------------------------------
CHOICE_MARKER = "Config choice (one word):"


def check_choiceread(adapter, tag_ids) -> list[Result]:
    """Replay archived choice points through the ported `choice_read`.

    The text passed to the original was the session transcript prefix ending
    at the i-th `Config choice (one word):`, so the prefix is recoverable
    exactly from the stored transcript -- no template guessing.
    """
    path = os.path.join(DATA, "e2a/sessions.jsonl")
    rows = [json.loads(l) for l in open(path) if l.strip()]
    cases = []
    for r in rows:
        tx = r.get("transcript") or ""
        idx, start = [], 0
        while (k := tx.find(CHOICE_MARKER, start)) != -1:
            idx.append(k + len(CHOICE_MARKER))
            start = k + 1
        for ci, ch in enumerate(r.get("choices", [])):
            if ci < len(idx):
                cases.append((tx[:idx[ci]], ch))
    print(f"  recovered {len(cases)} archived choice points from "
          f"{len(rows)} sessions", flush=True)

    rng = np.random.default_rng(26)
    pick = sorted(rng.choice(len(cases), size=min(N_CHOICE_READS, len(cases)),
                             replace=False))
    n_kl_nonzero = n_pick_diff = n_pa_diff = n_mass_diff = 0
    worst_pa = worst_mass = 0.0
    t0 = time.time()
    for n, i in enumerate(pick, start=1):
        text, ch = cases[i]
        a, b = ch["menu_a"], ch["menu_b"]
        read = choice_read(adapter, text, a, b, tag_ids, verify=True)
        if read.verify_kl != 0.0:
            n_kl_nonzero += 1
        if read.pick != ch["pick"]:
            n_pick_diff += 1
        dpa = abs(read.p_a - ch["p_a"])
        dmass = abs(read.label_mass - ch["label_mass"])
        worst_pa, worst_mass = max(worst_pa, dpa), max(worst_mass, dmass)
        if dpa > 5e-4:
            n_pa_diff += 1
        if dmass > 5e-4:
            n_mass_diff += 1
        if n % 16 == 0:
            print(f"    {n}/{len(pick)} replayed "
                  f"{time.time() - t0:.0f}s", flush=True)

    n = len(pick)
    return [
        Result("e2a choice-read verify KL", "0.0 on every read",
               f"{n_kl_nonzero}/{n} nonzero", n_kl_nonzero == 0),
        Result("archived pick reproduced", f"{n}/{n}",
               f"{n - n_pick_diff}/{n}", n_pick_diff == 0),
        Result("archived p_a reproduced", "max |diff| <= 5e-4",
               f"{worst_pa:.2e}", n_pa_diff == 0),
        Result("archived label_mass reproduced", "max |diff| <= 5e-4",
               f"{worst_mass:.2e}", n_mass_diff == 0),
    ]


# --- driver ---------------------------------------------------------------
def check_e2d_construction(adapter, tag_ids) -> list[Result]:
    """(iv) e2d D1: choice-read construction KL = 0.0 on the committed D1
    session texts, and the recorded reads reproduced from text alone.

    The D1 run asserted this live, 42/42. That is a claim about a process
    that has since ended; this is the claim about the ARTIFACT, and it is the
    stronger one -- it says the committed transcript is sufficient to
    regenerate the committed reads. A session file whose reads cannot be
    rebuilt from its own text is not a record of anything.

    NOTE ON THE ADAPTER. This check must NOT run on the rule-26 oracle's
    `legacy_truncate=True` adapter. That flag exists to reproduce PUBLISHED
    numbers, every one of which went through the 512-token tail window; e2d
    runs full-session under CHOICE_WINDOW. Replaying e2d reads through the
    legacy window would compare two different constructions and call the
    difference a failure.
    """
    path = os.path.join(DATA, "e2d/d1_sessions.json")
    if not os.path.exists(path):
        return [Result("e2d D1 construction", "KL 0.0", "SKIP", False,
                       note="data/e2d/d1_sessions.json absent -- a skip is a "
                            "FAILURE, not a pass (trap 5)")]
    art = json.load(open(path))
    cases = []
    for sess in art["sessions"]:
        tx = sess["transcript"]
        idx, start = [], 0
        while (k := tx.find(CHOICE_MARKER, start)) != -1:
            idx.append(k + len(CHOICE_MARKER))
            start = k + 1
        for ci, ch in enumerate(sess["choices"]):
            if ci < len(idx):
                cases.append((tx[:idx[ci]], ch))
    n_expected = sum(len(s["choices"]) for s in art["sessions"])
    print(f"  recovered {len(cases)} D1 choice points "
          f"(artifact records {n_expected} reads)", flush=True)

    n_kl_nonzero = n_pick_diff = 0
    worst_pa = 0.0
    for text, ch in cases:
        read = choice_read(adapter, text, ch["menu_a"], ch["menu_b"], tag_ids,
                           verify=True)
        if read.verify_kl != 0.0:
            n_kl_nonzero += 1
        if read.pick != ch["pick"]:
            n_pick_diff += 1
        worst_pa = max(worst_pa, abs(read.p_a - ch["read"]["p_a"]))

    n = len(cases)
    return [
        Result("e2d D1 choice-read verify KL", "0.0 on every read",
               f"{n_kl_nonzero}/{n} nonzero", n_kl_nonzero == 0 and n > 0),
        Result("e2d D1 every recorded read recovered", f"{n_expected}/{n_expected}",
               f"{n}/{n_expected}", n == n_expected and n > 0),
        Result("e2d D1 pick reproduced from text", f"{n}/{n}",
               f"{n - n_pick_diff}/{n}", n_pick_diff == 0 and n > 0),
        Result("e2d D1 p_a reproduced", "max |diff| <= 5e-4",
               f"{worst_pa:.2e}", worst_pa <= 5e-4 and n > 0),
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", default="all",
                    choices=["all", "kernel", "b2b", "choiceread", "e2d"])
    args = ap.parse_args()

    _banner("LEDGER 26 -- oracle-tier regression (Qwen, laptop)")
    t0 = time.time()
    from ..adapters.qwen_mlx import QwenMLXAdapter
    # legacy_truncate=True is REQUIRED here and only here: rule 26 reproduces
    # published numbers, and every published choice read went through the
    # 512-token tail window. New work runs full-session (CHOICE_WINDOW).
    # Clipped encodes are counted and reported in provenance.
    adapter = QwenMLXAdapter(legacy_truncate=True)
    print(f"model loaded in {time.time() - t0:.0f}s")
    print(f"provenance: {json.dumps(adapter.provenance())}", flush=True)

    tasks_p = os.path.join(DATA, "corpus/e2a_tasks.jsonl")
    tasks = ([json.loads(l) for l in open(tasks_p) if l.strip()]
             if os.path.exists(tasks_p) else [])
    tag_ids = {}
    # e2a's eight, plus the three h-roster tags e2a never used. e2d runs on
    # the h-roster (AMENDMENT 1 (i)), so a list frozen at e2a's roster would
    # KeyError on the first ridge/saddle read rather than checking it.
    for w in ["slate", "prism", "maple", "cedar", "granite", "lattice",
              "plaza", "saddle", "velvet", "walnut", "ridge"]:
        enc = adapter.encode(" " + w, add_special_tokens=False)
        if len(enc) == 1:
            tag_ids[w] = enc[0]
    print(f"single-token tags: {len(tag_ids)}/11  "
          f"e2a tasks: {len(tasks)}", flush=True)

    results: list[Result] = []
    if args.check in ("all", "choiceread"):
        _banner("(iii) e2a choice-read construction on archived session texts")
        results += check_choiceread(adapter, tag_ids)
    if args.check in ("all", "kernel"):
        _banner("(i) g1r kernel-gate KLs")
        if not tasks:
            results.append(Result("g1r kernel gate", "KLs", "SKIP", False,
                                  note="e2a_tasks.jsonl absent from the record"))
        else:
            results += check_kernel(adapter, tasks, tag_ids)
    if args.check in ("all", "b2b"):
        _banner("(ii) B2b reproduction -- paired per-probe TOST + verdict preservation")
        results += check_b2b(adapter)
    if args.check in ("all", "e2d"):
        _banner("(iv) e2d D1 construction on the committed session texts")
        # Its own adapter, deliberately: see check_e2d_construction's docstring.
        e2d_adapter = QwenMLXAdapter()
        results += check_e2d_construction(e2d_adapter, tag_ids)

    _banner("RULE 26 VERDICT")
    width = max(len(r.name) for r in results) + 2
    for r in results:
        print(f"  [{'PASS' if r.ok else 'FAIL'}] {r.name:<{width}} "
              f"expected {r.expected:>14}  got {r.got:>14}"
              + (f"   ({r.note})" if r.note else ""))
    n_fail = sum(1 for r in results if not r.ok)
    print("-" * 78)
    print(f"  {len(results) - n_fail}/{len(results)} criteria reproduced "
          f"through valence_core   [total {time.time() - t0:.0f}s]")
    if n_fail:
        print("  RULE 26: a mismatch is a refactor bug until proven "
              "otherwise. No Phase-1 work on an unverified core.")

    os.makedirs(os.path.join(DATA, "regression"), exist_ok=True)
    with open(os.path.join(DATA, "regression/oracle_rule26.json"), "w") as f:
        json.dump({"provenance": adapter.provenance(),
                   "results": [r.__dict__ for r in results],
                   "n_fail": n_fail}, f, indent=1)
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
