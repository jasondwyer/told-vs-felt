"""e2d marker readout -- V1's instrument, through the oracle path (rule 26).

PROPOSAL-j §2 Q3, "the one-pole variant of V1's (ii-c) rule, declared here".

WHAT THE INSTRUMENT IS. `regression.oracle.build_instruments()` rebuilds the
twelve locked per-probe instruments from the frozen B1 artifact and asserts
G against its pre-registered 0.3156 -- if G drifts, nothing downstream is
comparable, so this module refuses to score rather than scoring against a
moved ruler. Each instrument is a weight vector over selected vocabulary ids
plus a sigma; a score is `w @ logprobs[sel_ids]`, and a delta is reported in
sigma units, which is what makes 0.5*G = 0.158 a meaningful bar.

WHAT IS BEING SCORED, AND WHY IT IS NOT V1's GRID. V1 measured the state
live at the probe: `arm_scores([inj])` vs `arm_scores([])`, short contexts.
e2d measures the state's RESIDUE IN THE RECORD: each generated round becomes
a context, twelve probes are appended to it, and the forward carries NO
injection at all. That is the session-scale reading the proposal asks for
("all 480 D2 generations scored, 12 probe forwards each"), and it is the
informational channel -- state -> generated text -> comprehension -- rather
than the mechanical one.

THE ONE-POLE VARIANT. V1's rule had a Delta- clause; there is no negative
pole in e2d, so the clause is inapplicable BY DESIGN and is dropped, not
waived. What remains: Delta+ >= 0.158, and Delta+ > 2*|Delta_R|. A sign flip
(Delta+ < 0) is V1's overdose signature and fails the rung.

## The contrast, SETTLED by AMENDMENT 2 (iv)

PROPOSAL-j said "+axis rounds vs sham rounds" while §7 budgeted "480 D2
generations" -- arms M and R only, excluding S. Those are two different
contrasts, and at D1 they disagreed IN SIGN: within-M -0.239, against the
S arm +1.499. AMENDMENT 2 (iv) settles it: **"+axis rounds vs sham rounds"
= WITHIN-M, PAIRED BY SESSION** -- per M session, the mean readout over its
+axis rounds minus the mean over its own sham rounds, with Delta+ the mean
of those per-session differences and a paired test over sessions. Delta_R
likewise within R. `paired_by_session()` is that estimator and is Q3's
primary; `deltas()` keeps the pooled and across-arm forms, now explicitly
secondary and labelled, because a number that disagreed in sign once should
stay visible rather than disappear into a decision.
"""

from __future__ import annotations

import re
import time
from typing import Sequence

import numpy as np

from ..regression.oracle import G_EXPECTED, build_instruments

#: PROPOSAL-j §2 Q3. 0.5 * G, the pre-registered V1 effect-size bar --
#: identical in form to the rule-26 B2b TOST margin, and for the same reason.
def bar_from(g: float) -> float:
    return 0.5 * g


#: The instrument's own context shape. `check_b2b` builds
#: "Task: ...\nResponse: ...\nTask: {probe}\nResponse:", and the twelve
#: instruments were fit on that shape -- scoring a differently-shaped context
#: would put the instrument out of distribution and the sigma units would
#: stop meaning what they mean.
CONTEXT_FMT = "Task: {task}\nResponse: {response}\nTask: {probe}\nResponse:"


def score_generation(adapter, instruments, probes: Sequence[str],
                     task_text: str, response: str) -> list[float]:
    """Twelve probe forwards over one generation; one score per instrument.

    No injection anywhere: the state that produced `response` is long gone,
    and what is being asked is whether it left a mark on the text.
    """
    out = []
    for qi, probe in enumerate(probes):
        text = CONTEXT_FMT.format(task=task_text, response=response,
                                  probe=probe)
        res = adapter.forward(adapter.encode(text), capture_layers=())
        lg = res.logits.astype(np.float64)
        lp = lg - (np.log(np.exp(lg - lg.max()).sum()) + lg.max())
        inst = instruments[qi]
        out.append(float(inst["w"] @ lp[inst["sel_ids"]]))
    return out


def collect(adapter, instruments, probes, sessions, task_text_of,
            progress=None) -> list[dict]:
    """Score every generation in `sessions`. 12 forwards each.

    Rounds whose text is empty are skipped and COUNTED as skipped: trap 5,
    a case that never ran must not read as a case that passed.
    """
    rows = []
    n_forward = 0
    t0 = time.time()
    for s in sessions:
        for r in list(s["rounds"]) + list(s["choices"]):
            if not r["text"].strip():
                rows.append({"arm": s["arm"], "session": s["session"],
                             "phase": r["phase"], "steered": bool(r["steered"]),
                             "scores": None, "skipped": "empty text"})
                continue
            sc = score_generation(adapter, instruments, probes,
                                  task_text_of(r["task"]), r["text"])
            n_forward += len(probes)
            rows.append({"arm": s["arm"], "session": s["session"],
                         "phase": r["phase"], "task": r["task"],
                         "steered": bool(r["steered"]),
                         "degen": r["degen"], "lexical": r.get("lexical"),
                         "scores": sc, "skipped": None})
            if progress and n_forward % 120 == 0:
                progress(f"      marker: {n_forward} forwards "
                         f"{time.time() - t0:.0f}s")
    return rows


def _delta(rows_a, rows_b, instruments) -> tuple[float | None, list, int, int]:
    """Mean over probes of (mean_a - mean_b) / sigma_probe.

    Per-probe before pooling, exactly as `oracle.check_b2b.delta` does: the
    twelve instruments have enormously heterogeneous scales, and pooling raw
    scores across them would let one probe carry the number.
    """
    A = [r["scores"] for r in rows_a if r["scores"]]
    B = [r["scores"] for r in rows_b if r["scores"]]
    if not A or not B:
        return None, [], len(A), len(B)
    A, B = np.array(A), np.array(B)
    ds = [(A[:, qi].mean() - B[:, qi].mean()) / (inst["sigma"] + 1e-12)
          for qi, inst in enumerate(instruments)]
    return float(np.mean(ds)), [float(d) for d in ds], len(A), len(B)


def deltas(rows: Sequence[dict], instruments, clean_only: bool = True) -> dict:
    """Delta+ and Delta_R, under both readings of "sham rounds".

    `clean_only` drops audit-degenerate and lexical rounds before the
    contrast, matching Q2's clean-round evaluation (rule 28b) -- a delta
    driven by junk text is a delta about junk text. Both are reported.
    """
    def sel(arm, steered, clean):
        return [r for r in rows
                if r["arm"] == arm and r["scores"]
                and bool(r["steered"]) == steered
                and (not clean or not (r.get("degen") or r.get("lexical")))]

    out = {"clean_only": clean_only, "G_expected": G_EXPECTED}
    for label, clean in (("clean", True), ("all_rounds", False)):
        if clean != clean_only and label == "clean":
            pass
        d = {}
        # PRIMARY READING: within-arm, steered vs that arm's own unsteered.
        dp, per_p, na, nb = _delta(sel("M", True, clean), sel("M", False, clean),
                                   instruments)
        d["delta_plus_within_M"] = {"delta": dp, "per_probe": per_p,
                                    "n_steered": na, "n_unsteered": nb}
        dr, per_r, na, nb = _delta(sel("R", True, clean), sel("R", False, clean),
                                   instruments)
        d["delta_R_within_R"] = {"delta": dr, "per_probe": per_r,
                                 "n_steered": na, "n_unsteered": nb}
        # ALTERNATIVE READING: against the S arm.
        s_rows = sel("S", True, clean) + sel("S", False, clean)
        dps, per_ps, na, nb = _delta(sel("M", True, clean), s_rows, instruments)
        d["delta_plus_vs_S_arm"] = {"delta": dps, "per_probe": per_ps,
                                    "n_steered": na, "n_sham": nb}
        drs, per_rs, na, nb = _delta(sel("R", True, clean), s_rows, instruments)
        d["delta_R_vs_S_arm"] = {"delta": drs, "per_probe": per_rs,
                                 "n_steered": na, "n_sham": nb}
        out[label] = d
    return out


# --- ADDENDUM-j1 (a): the SAME readout in the live session context --------
#: The probe appended to the session transcript as it stood at the end of the
#: round, keeping the probe in the instrument's own Task/Response idiom. The
#: excised form (CONTEXT_FMT) strips the session away and leaves one
#: task+response pair; this keeps everything the model had actually written.
IN_SITU_SUFFIX = "Task: {probe}\nResponse:"

_HDR = re.compile(r'^\[round .*\]$', re.M)
_MENU_PREFIXES = ("Configs available", "Options:", "Configs on offer",
                  "Available configs")


def in_situ_prefixes(session: dict) -> list[str]:
    """Transcript prefix through the end of each generated round, in order.

    Cut from the STORED transcript rather than rebuilt from templates: the
    transcript is what the model actually read, and reconstructing it from
    round records would be a second implementation of the runner that could
    drift from it silently.

    A '[round ...]' line counts as a header only when the next line is a
    Task: or a menu line -- the model sometimes emits a header-shaped
    response, and treating that as scaffolding would cut the prefix in the
    wrong place.
    """
    t = session["transcript"]
    lines = t.split("\n")
    # byte offset of the start of each line
    starts, off = [], 0
    for ln in lines:
        starts.append(off)
        off += len(ln) + 1

    prefixes: list[str] = []
    i = 0
    while i < len(lines):
        if re.match(r'^\[round .*\]$', lines[i]):
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt.startswith("Task:"):
                j = i + 2
                if j >= len(lines) or not lines[j].startswith("Response:"):
                    raise AssertionError(
                        f"malformed round block at line {i} in "
                        f"{session['arm']} s{session['session']}")
                j += 1
                while j < len(lines):
                    if re.match(r'^\[round .*\]$', lines[j]):
                        n2 = lines[j + 1] if j + 1 < len(lines) else ""
                        if n2.startswith("Task:") or any(
                                n2.startswith(p) for p in _MENU_PREFIXES):
                            break
                    j += 1
                end = starts[j] if j < len(lines) else len(t)
                prefixes.append(t[:end])
                i = j
                continue
            if any(nxt.startswith(p) for p in _MENU_PREFIXES):
                j = i + 1
                while j < len(lines) and not re.match(r'^\[round .*\]$', lines[j]):
                    j += 1
                i = j
                continue
        i += 1
    return prefixes


def collect_in_situ(adapter, instruments, probes, sessions, progress=None
                    ) -> list[dict]:
    """ADDENDUM-j1 (a)'s second context: the probe on the live transcript.

    Same instruments, same probes, same no-injection forward. The only thing
    that changes is how much of the session the probe can see, which is the
    whole question the two-context comparison asks.
    """
    rows = []
    n_forward = 0
    t0 = time.time()
    for s in sessions:
        rounds = list(s["rounds"]) + list(s["choices"])
        prefixes = in_situ_prefixes(s)
        if len(prefixes) != len(rounds):
            raise AssertionError(
                f"{s['arm']} s{s['session']}: parsed {len(prefixes)} round "
                f"prefixes but the record has {len(rounds)} rounds -- refusing "
                f"to score a misaligned context")
        for r, pre in zip(rounds, prefixes):
            if not r["text"].strip():
                rows.append({"arm": s["arm"], "session": s["session"],
                             "phase": r["phase"], "steered": bool(r["steered"]),
                             "scores": None, "skipped": "empty text"})
                continue
            sc = []
            for qi, probe in enumerate(probes):
                text = pre + IN_SITU_SUFFIX.format(probe=probe)
                res = adapter.forward(adapter.encode(text), capture_layers=())
                lg = res.logits.astype(np.float64)
                lp = lg - (np.log(np.exp(lg - lg.max()).sum()) + lg.max())
                inst = instruments[qi]
                sc.append(float(inst["w"] @ lp[inst["sel_ids"]]))
            n_forward += len(probes)
            rows.append({"arm": s["arm"], "session": s["session"],
                         "phase": r["phase"], "task": r["task"],
                         "steered": bool(r["steered"]),
                         "degen": r["degen"], "lexical": r.get("lexical"),
                         "scores": sc, "skipped": None})
            if progress and n_forward % 120 == 0:
                progress(f"      in-situ: {n_forward} forwards "
                         f"{time.time() - t0:.0f}s")
    return rows


# --- AMENDMENT 2 (iv): the within-arm contrast, PAIRED BY SESSION ---------
def paired_by_session(rows: Sequence[dict], instruments, arm: str,
                      clean_only: bool = True,
                      marked: set | None = None) -> dict:
    """Per session: mean marker readout over its STEERED rounds minus the mean
    over its OWN unsteered rounds. Delta = mean of those per-session
    differences.

    RATIFIED as Q3's primary by AMENDMENT 2 (iv). The pooled contrast this
    replaces is not the same estimator: pooling lets a session with many
    surviving rounds dominate, and after exclusions and clean-round filtering
    the surviving counts are exactly the thing that varies between sessions.
    Pairing inside the session also removes the session-level nuisance --
    task draw, label map, forced-end phase -- which is what made D1's
    across-arm reading (+1.499) disagree in SIGN with the within-arm one
    (-0.239).

    Per-probe sigma normalisation happens BEFORE the session mean, as
    `oracle.check_b2b.delta` does it: the twelve instruments have
    heterogeneous scales and pooling raw scores across them lets one probe
    carry the number.

    `marked` is the AMENDMENT 2 (iii) read-marks key set; when supplied,
    read-marked rounds are dropped alongside audit-degenerate ones.
    """
    from .marks import is_marked

    def usable(r):
        if not r["scores"]:
            return False
        if clean_only and (r.get("degen") or r.get("lexical")):
            return False
        if marked is not None and is_marked(marked, r["arm"], r["session"],
                                            r["phase"]):
            return False
        return True

    by_session: dict[int, dict[str, list]] = {}
    for r in rows:
        if r["arm"] != arm or not usable(r):
            continue
        d = by_session.setdefault(r["session"], {"pos": [], "neg": []})
        d["pos" if r["steered"] else "neg"].append(r["scores"])

    per_session = []
    for sid in sorted(by_session):
        P, N = by_session[sid]["pos"], by_session[sid]["neg"]
        if not P or not N:
            per_session.append({"session": sid, "diff": None,
                                "n_steered": len(P), "n_unsteered": len(N),
                                "why": "one side empty after filtering"})
            continue
        P, N = np.array(P), np.array(N)
        ds = [(P[:, qi].mean() - N[:, qi].mean()) / (inst["sigma"] + 1e-12)
              for qi, inst in enumerate(instruments)]
        per_session.append({"session": sid, "diff": float(np.mean(ds)),
                            "per_probe": [float(x) for x in ds],
                            "n_steered": len(P), "n_unsteered": len(N)})

    diffs = [p["diff"] for p in per_session if p["diff"] is not None]
    return {"arm": arm, "clean_only": clean_only,
            "read_marks_applied": marked is not None,
            "n_sessions_total": len(per_session),
            "n_sessions_decidable": len(diffs),
            "delta": float(np.mean(diffs)) if diffs else None,
            "sd": float(np.std(diffs, ddof=1)) if len(diffs) > 1 else None,
            "per_session": per_session}


def sign_test(diffs: Sequence[float], alternative: str = "greater") -> dict:
    """Exact paired sign test. No scipy (trap 1); math.comb is exact and n is
    at most a few dozen. Zeros are dropped, and the DROPPED COUNT is
    reported -- a sign test that silently discards ties reports a different n
    from the one it was powered for."""
    from math import comb
    nz = [d for d in diffs if d != 0]
    n, k = len(nz), sum(1 for d in nz if d > 0)
    if n == 0:
        return {"n": 0, "k": 0, "p": None, "why": "all differences are zero",
                "n_ties_dropped": len(diffs)}
    if alternative == "greater":
        p = sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n
    elif alternative == "less":
        p = sum(comb(n, i) for i in range(0, k + 1)) / 2 ** n
    else:
        raise ValueError(alternative)
    return {"n": n, "k_positive": k, "p": float(p),
            "alternative": alternative, "n_ties_dropped": len(diffs) - n}


def sign_flip_test(diffs: Sequence[float], b: int = 10000,
                   seed: int = 20260902) -> dict:
    """Paired sign-flip permutation test on the mean difference.

    Exact enumeration is 2^n and n = 32 is 4.3e9, so this is a seeded Monte
    Carlo over sign assignments -- the standard paired-permutation null, and
    the seed is recorded so the p-value is reproducible.
    """
    d = np.asarray([x for x in diffs], dtype=np.float64)
    if not len(d):
        return {"n": 0, "p": None, "why": "no decidable sessions"}
    obs = float(d.mean())
    rng = np.random.default_rng(seed)
    signs = rng.choice((-1.0, 1.0), size=(b, len(d)))
    null = (signs * d).mean(axis=1)
    p = float((np.sum(null >= obs) + 1) / (b + 1))     # add-one, one-sided
    return {"n": len(d), "observed_mean": obs, "p": p, "b": b, "seed": seed,
            "alternative": "greater", "null_sd": float(null.std())}


def task_matched(rows: Sequence[dict], instruments, arm: str,
                 clean_only: bool = True, marked: set | None = None) -> dict:
    """AMENDMENT 2 (iv)'s third reported figure: pairs where a steered and an
    unsteered round in the SAME arm share a task_id.

    The tightest available control for content: the same task, answered once
    with the state live and once without. It is also the sparsest -- e2a's
    task sequence draws without replacement within a session, so matches come
    from ACROSS sessions and there may be few. The decidable n is reported
    beside the number for exactly that reason (rule 28a's habit, applied to a
    descriptive figure).
    """
    from .marks import is_marked

    def usable(r):
        if not r["scores"]:
            return False
        if clean_only and (r.get("degen") or r.get("lexical")):
            return False
        if marked is not None and is_marked(marked, r["arm"], r["session"],
                                            r["phase"]):
            return False
        return True

    pos: dict[str, list] = {}
    neg: dict[str, list] = {}
    for r in rows:
        if r["arm"] != arm or not usable(r) or not r.get("task"):
            continue
        (pos if r["steered"] else neg).setdefault(r["task"], []).append(
            r["scores"])
    shared = sorted(set(pos) & set(neg))
    if not shared:
        return {"arm": arm, "n_tasks_matched": 0, "delta": None,
                "why": "no task_id has both a steered and an unsteered round"}
    ds = []
    for t in shared:
        P, N = np.array(pos[t]), np.array(neg[t])
        d = [(P[:, qi].mean() - N[:, qi].mean()) / (inst["sigma"] + 1e-12)
             for qi, inst in enumerate(instruments)]
        ds.append(float(np.mean(d)))
    return {"arm": arm, "n_tasks_matched": len(shared),
            "tasks": shared, "per_task": ds,
            "delta": float(np.mean(ds)),
            "sd": float(np.std(ds, ddof=1)) if len(ds) > 1 else None}


def q3(delta_plus: float | None, delta_R: float | None, g: float) -> dict:
    """PROPOSAL-j §2 Q3, computed. Returns; writes nothing (trap 6)."""
    bar = bar_from(g)
    if delta_plus is None:
        return {"passes": False, "why": "Delta+ not evaluable", "bar": bar}
    sign_flip = delta_plus < 0
    ok_mag = delta_plus >= bar
    ok_vs_r = (delta_R is not None) and (delta_plus > 2 * abs(delta_R))
    return {"passes": bool(ok_mag and ok_vs_r and not sign_flip),
            "delta_plus": delta_plus, "bar": bar,
            "magnitude_ok": bool(ok_mag),
            "delta_R": delta_R, "beats_2x_random": bool(ok_vs_r),
            "sign_flip": bool(sign_flip),
            "note": ("a sign flip is V1's overdose signature and fails the "
                     "rung" if sign_flip else "")}


def instruments_or_stop():
    """The instruments, with G asserted. Refuse rather than score against a
    moved ruler."""
    instruments, g = build_instruments()
    if instruments is None:
        raise SystemExit("e2d marker: e0_b1_markers.npz absent from the "
                         "record -- the V1 instrument cannot be rebuilt")
    if abs(g - G_EXPECTED) > 1e-3:
        raise SystemExit(f"e2d marker: instrument drift, G = {g:.6f} vs "
                         f"expected {G_EXPECTED} -- nothing downstream is "
                         f"comparable (rule 26)")
    return instruments, float(g)


__all__ = ["CONTEXT_FMT", "IN_SITU_SUFFIX", "in_situ_prefixes",
           "collect_in_situ", "bar_from", "score_generation", "collect",
           "deltas", "q3", "instruments_or_stop", "paired_by_session",
           "sign_test", "sign_flip_test", "task_matched"]
