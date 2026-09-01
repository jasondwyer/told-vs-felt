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

## A reading this module does not settle

PROPOSAL-j says "+axis rounds vs sham rounds" and separately budgets "all
480 D2 generations" -- which is arms M and R only (32*10 + 16*10), not the
S arm. Those two together mean the contrast is WITHIN each arm: M's steered
rounds against M's own unsteered rounds, and R's steered against R's own.
That is what `deltas()` computes as the primary reading. But "sham rounds"
can also name the S arm, so the across-arm reading is computed BESIDE it and
both are reported. At D1 this is descriptive and costs nothing; before D2,
where Q3 binds, the design instance names one.
"""

from __future__ import annotations

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


__all__ = ["CONTEXT_FMT", "bar_from", "score_generation", "collect",
           "deltas", "q3", "instruments_or_stop"]
