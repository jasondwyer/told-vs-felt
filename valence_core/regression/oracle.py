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

Some inputs (the e2a/e0 task corpora, the B1 marker artifact) remain in the
gitignored clone; they are read-only here and their absence is reported as
SKIP with the reason, never as a pass.
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
from ..stats import Z90

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(REPO, "data")
CLONE = os.path.join(REPO, "jlens-qwen36")

LAYER = 48
KERNEL_FRACS = (0.10, 0.20)
KERNEL_REF = {"0.1": 7.106405682861805e-04, "0.2": 7.390632526949048e-04}
KERNEL_TOL = 0.02                      # 2% relative
B2B_LAYER, B2B_FRAC = 48, 0.10
VAL_TASKS_B2B = [f"e{i:02d}" for i in range(25, 49)]
SEL = 256
G_EXPECTED = 0.3156
N_B2B_CONTEXTS = 128
N_CHOICE_READS = 48


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
    b1 = os.path.join(CLONE, "data/e0/e0_b1_markers.npz")
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
        return [Result("B2b 128-context subsample", "delta +.2848/-.3946",
                       "SKIP", False,
                       note="e0_b1_markers.npz absent (clone-only artifact)")]
    if abs(G - G_EXPECTED) > 1e-3:
        return [Result("B2b instrument G", f"{G_EXPECTED}", f"{G:.6f}", False,
                       note="instrument drift -- nothing downstream comparable")]
    print(f"  instruments rebuilt: G = {G:.6f} (expected {G_EXPECTED})",
          flush=True)

    tasks_p = os.path.join(CLONE, "data/corpus/e0_tasks.jsonl")
    probes_p = os.path.join(CLONE, "data/configs/e0_probes.json")
    if not (os.path.exists(tasks_p) and os.path.exists(probes_p)):
        return [Result("B2b 128-context subsample", "delta +.2848/-.3946",
                       "SKIP", False, note="e0 corpus absent (clone-only)")]
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
    rng = np.random.default_rng(26)               # declared subsample seed
    pick = sorted(rng.choice(len(contexts), size=N_B2B_CONTEXTS, replace=False))
    sub = [contexts[i] for i in pick]

    rw, R = load_axis(B2B_LAYER)

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

    base = arm_scores([], "base")
    pos = arm_scores([Injection.at_frac(rw, B2B_LAYER, +B2B_FRAC, R)], "axis_pos")
    neg = arm_scores([Injection.at_frac(rw, B2B_LAYER, -B2B_FRAC, R)], "axis_neg")

    ref = json.load(open(os.path.join(DATA, "e0/e0_b2_b2b.json")))["arms"]
    out = []
    for name, arm, published in (("axis_pos", pos, ref["axis_pos"]["delta"]),
                                 ("axis_neg", neg, ref["axis_neg"]["delta"])):
        d, per = delta(arm, base)
        # per-probe SE across the 12 instruments -> 90% interval, the same
        # convention the program's TOST intervals use (Z90).
        half = Z90 * float(np.std(per, ddof=1) / np.sqrt(len(per)))
        within = abs(d - published) <= half
        print(f"  {name}: delta {d:+.4f}  published {published:+.4f}  "
              f"90% half-width {half:.4f}  -> "
              f"{'within' if within else 'OUTSIDE'}", flush=True)
        out.append(Result(f"B2b {name} (128-ctx subsample)",
                          f"{published:+.4f}", f"{d:+.4f}", within,
                          note=f"+/-{half:.4f} (90%, 12 probes); "
                               f"sign {'ok' if np.sign(d) == np.sign(published) else 'FLIPPED'}"))
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
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", default="all",
                    choices=["all", "kernel", "b2b", "choiceread"])
    args = ap.parse_args()

    _banner("LEDGER 26 -- oracle-tier regression (Qwen, laptop)")
    t0 = time.time()
    from ..adapters.qwen_mlx import QwenMLXAdapter
    adapter = QwenMLXAdapter()
    print(f"model loaded in {time.time() - t0:.0f}s")
    print(f"provenance: {json.dumps(adapter.provenance())}", flush=True)

    tasks_p = os.path.join(CLONE, "data/corpus/e2a_tasks.jsonl")
    tasks = ([json.loads(l) for l in open(tasks_p) if l.strip()]
             if os.path.exists(tasks_p) else [])
    tag_ids = {}
    for w in ["slate", "prism", "maple", "cedar", "granite", "lattice",
              "plaza", "saddle"]:
        enc = adapter.encode(" " + w, add_special_tokens=False)
        if len(enc) == 1:
            tag_ids[w] = enc[0]
    print(f"single-token tags: {len(tag_ids)}/8  "
          f"e2a tasks: {len(tasks)}", flush=True)

    results: list[Result] = []
    if args.check in ("all", "choiceread"):
        _banner("(iii) e2a choice-read construction on archived session texts")
        results += check_choiceread(adapter, tag_ids)
    if args.check in ("all", "kernel"):
        _banner("(i) g1r kernel-gate KLs")
        if not tasks:
            results.append(Result("g1r kernel gate", "KLs", "SKIP", False,
                                  note="e2a_tasks.jsonl absent (clone-only)"))
        else:
            results += check_kernel(adapter, tasks, tag_ids)
    if args.check in ("all", "b2b"):
        _banner("(ii) B2b 128-context subsample")
        results += check_b2b(adapter)

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
