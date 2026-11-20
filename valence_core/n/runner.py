"""PROPOSAL-n -- the read runner (n v0.2 §2.1, §2.4, §2.8, §4's blinding, §6's monitoring).

Runs a stage's planned reads through the 5(f) primitive, writes each as a checked record into its cell
(``cells.append_record``), stops at the first monitor that fires, and ends every invocation by writing the stage
report (``schema.check_report``'s ``n-report-v1``). It decides nothing: a pause ends the invocation and is reported;
the seat adjudicates (rule 21; §6: "Code never self-adjudicates").

BLINDING (n §4): "stdout prints session index, arm, dose, the fidelity value against TAU, timing -- never a margin".
The per-read line is exactly that; the stage report carries counts, states and sha256s, never a margin, a
log-probability or a pick.

THE RECORDS ARE THE RECORD. Every invocation rebuilds the monitors by replaying the records on disk in launch order.
The prior report gives only what no record holds: the rendering pauses, whose reads were not launched, and each
pause's adjudication. A fire the replay finds that the prior report does not hold (an invocation that ended before
its report was written) is a pause now, and nothing is launched.

PINs (Code, declared at the BUILD; each is LOCK-n v0.1's to pin, and the BUILD entry lists them for the seat):
  * ORDER -- the campaign's launch order is arm-major in ``schema.ARMS`` order with N1-V's 160 d = 0 reads (the
    shadows) first; within an arm, cells in ``schema.arm_cells`` order (``ARM_CELLS``' directions and listed labels,
    each label read under its keeper, a merged point once: ADDENDUM-n1 §5.1); within a cell, sessions in the session
    set's order. So the primary arm completes first if the cap binds, and every shadow is on disk before any steered
    read.
  * PAUSE -- a fired monitor ends the invocation, all arms with it (n §6: "Every pause STOPs the arm's launches until
    adjudicated"; stopping all is the conservative reading). The read that fired is on disk, except at a rendering
    pause, whose read is not launched. A resume needs a ruling for every standing pause, given as the ruling raw's
    path; its sha256 is the pause's ``ruling_sha256``. A resume skips every read on disk. A pause's
    ``resumed_at_launch_index`` is the first read attempted after its own (at its own place, for a rendering pause):
    launched, or refused as a rendering mismatch. The runner halts at a pause, so every such attempt came after the
    ruling.
  * SCOPE -- a pause stands on the arm of the read that fired it (n §6's "the arm's launches"), and a binomial fire
    on the arms with a trial in its tile. A pause on a shadow (N1-V's d = 0 read) also stands on every arm whose
    steered reads of that session pair with it (5(f)(i)): their margins are read against it. A binomial fire at a
    read with no re-computation stands on that read's arm too, though it had no trial in the tile (the schema holds
    a pause's read's arm in its scope; for the seat).
  * FIDELITY BINOMIAL -- trials are the reads that carry a re-computation. The binomial's window is the tile (the
    seat's answers of 2026-11-19, first sitting, §3, R12): the reads launched since the previous evaluation, in
    launch order, ``cadence`` of them (n §2.1: "cadence every 160 reads"; the identity's ``cadence``). A tile is
    evaluated at its cadence-th read, a trial or not: its k exceedances at TAU among its n trials, the exact tail
    P(X >= k | n trials, p0) against the alpha. A fire's batch is the tile, its first and last reads, and it ends at
    the read that fired it. The next tile starts at the next read, after a fire as after none, so that every read
    lies in exactly one tile and a ruling clears nothing. The records on disk are the plan's first reads, 0..M-1
    (every pause halts the invocation, a rendering pause's place is attempted first on the resume, and a CAP ends
    the stage), and any other set is refused before a launch: so tile j is reads j * cadence through
    (j + 1) * cadence - 1, and the tail starts at a multiple of the cadence. A tile with no trial is evaluated too,
    and cannot fire (Code's reading, for the seat).
    The alpha is the identity's ``fidelity_rule.alpha``, and a stage whose inputs carry another is refused before
    any read. Its value is the seat's: 0.01, one-sided, "at each evaluation" (the answers of 2026-11-18, fourth
    sitting, §4). ``p0 = 0`` makes any exceedance fire at its tile's evaluation (rule 21's zero-base-rate form); the
    lock's p0 is the box's (ADDENDUM-n2 §1.1), at least 1 of 3 by Laplace's rule (F5, the schema's). A ruling on a
    fidelity-ceiling pause clears nothing: its read stays in its tile as a trial, and as an exceedance where its rel
    is above TAU (R13). When no read remains to launch (the plan done, or the cap spent), the stage's tail, the
    reads since the last evaluation where there are any, however few and whatever their trials, is evaluated once
    (Code's reading, for the seat): the end-of-run evaluation, whose fire has no read. A resume keeps the stage's cap
    and alpha: a report on disk under another is refused.
  * NON-FINITE, CEILING and IDENTITY -- a non-finite read; a re-computed read, at any dose, whose |cached margin -
    fresh margin| is above the identity's ``fidelity_rule.ceiling`` (ADDENDUM-n2 §2.1: "pauses at once"; none where
    no ceiling is set, at backend-ext); or an unsteered read whose identity check is not within the bound, pauses at
    once (§6: "NaN/inf; the identity bound exceeded at d = 0"). Every kind a read fires is recorded: the first in
    ``schema.PAUSE_KINDS``' order is the pause's kind, the rest are ``also_fired``. The ceiling binds at G-TIME-n as
    at the campaign: the identity sets it at every stage but backend-ext, so a timing re-computation above it pauses
    G-TIME-n (Code's reading, for the seat). With the identity bound equal to the ceiling (ADDENDUM-n2 §2.2), a
    finite d = 0 read above it fires fidelity-ceiling first and identity-bound after it.
  * RENDERING -- a token sequence that is not the session's of record (``sessions.RenderingMismatch`` from the
    renderer, or an ``ids_sha`` other than BK's) is a rendering pause before the read, which is not launched (§6's
    "a rendering mismatch"; G-VER's check, repeated per read).
  * CAP -- before each launch, the sum of the stage's records' ``duration_ms`` against the lock's cap. Each
    invocation's model load (``StageInputs.load_ms``) is reported beside the cap and outside it: ``loads_ms`` holds
    the invocations that wrote a report, in order (the prior report's list, then this one's). An invocation that ends
    without one -- an exception, a refusal, a kill -- is absent from it; its records, on disk, still count in
    ``used_ms``.
"""
from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Mapping, Sequence

import numpy as np

from ..adapters.base import Injection
from ..m import resume as m_resume
from ..m.keys import stream_known_answer
from . import cells, keys, schema
from .sessions import RenderingMismatch, Session, ids_sha


def binom_tail(x: int, n: int, p0: float) -> float:
    """P(X >= x) for X ~ Binomial(n, p0): the exact distribution, its terms in log space (no overflow at any n), summed
    on the smaller side -- the upper tail itself when x is above the mean, else one minus the lower tail. x <= 0 -> 1.
    """
    if x <= 0:
        return 1.0
    if x > n or p0 <= 0.0:
        return 0.0
    if p0 >= 1.0:
        return 1.0
    lp, lq = math.log(p0), math.log1p(-p0)

    def side(ks) -> float:
        logs = [math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1) + k * lp + (n - k) * lq for k in ks]
        top = max(logs)
        return math.exp(top) * math.fsum(math.exp(v - top) for v in logs)
    if x > n * p0:
        return min(1.0, side(range(x, n + 1)))
    return max(0.0, 1.0 - side(range(0, x)))


@dataclass(frozen=True)
class PlannedRead:
    launch_index: int
    session: Session
    arm: str
    direction_id: str
    dose_label: str
    dose_value: float
    fidelity_reason: str | None
    schedule_zone: str | None

    @property
    def read_id(self) -> str:
        return schema.read_id(self.arm, self.direction_id, self.dose_label, self.session.session_id)


def check_schedule(sessions: Sequence[Session], schedule: Sequence[str]) -> None:
    """N4's schedule as the schema's docstring has it checked by the runner: one zone per session, 80 told-S of 160,
    40 in each present-order group (keys' PIN). Raises SystemExit otherwise."""
    if len(schedule) != len(sessions) or any(z not in ("S", "U") for z in schedule):
        raise SystemExit("N4's schedule is not one zone per session")
    if len(sessions) == schema.N_SESSIONS:
        by_group = {True: 0, False: 0}
        for s in sessions:
            by_group[s.present_first_is_S] += schedule[s.bk_run] == "S"
        if sum(by_group.values()) != 80 or by_group != {True: keys.N4_TOLD_S_PER_GROUP,
                                                        False: keys.N4_TOLD_S_PER_GROUP}:
            raise SystemExit(f"N4's schedule is not 80/80 with 40 told-S per present-order group: {by_group}")


def campaign_order(identity: Mapping, sessions: Sequence[Session], schedule: Sequence[str]) -> list[PlannedRead]:
    """The campaign's reads in launch order (ORDER above), each with its fidelity rule (keys' PIN) and N4 zone."""
    check_schedule(sessions, schedule)
    kept = schema.dose_point_values(identity)
    out: list[PlannedRead] = []

    def add(arm, did, dl, s):
        reason = "dose-rule" if dl in ("0", "+1", "-1") else ("sample" if keys.fid_sampled(s.bk_run) else None)
        zone = schedule[s.bk_run] if arm in schema.TOLD_VARIANT else None
        out.append(PlannedRead(len(out), s, arm, did, dl, kept[dl], reason, zone))

    for s in sessions:                                          # the shadows first
        add(schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE, s)
    for arm in schema.ARMS:
        pool = [s for s in sessions if s.is_floor] if arm == "N1-R" else list(sessions)
        for did, labels in schema.arm_cells(arm, identity):        # each listed label's keeper (ADDENDUM-n1 §5.1)
            for dl in labels:
                if (arm, did, dl) == (schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE):
                    continue
                for s in pool:
                    add(arm, did, dl, s)
    got = sorted(p.read_id for p in out)
    if got != schema.read_plan(identity):
        raise AssertionError("the launch order does not cover the declared read plan exactly")
    return out


@dataclass
class Monitors:
    """n §6's monitors over the records, in launch order (PINs above)."""
    cadence: int
    p0_count: int
    p0_n: int
    alpha: float
    ceiling: float | None = None            # ADDENDUM-n2 §2.1's C, nats; None where the identity sets none
    trials: int = 0                         # the stage's, cumulative: binomial_state
    exceed: int = 0
    evaluations: int = 0
    fires: int = 0
    tile_reads: int = 0                     # the tile: the reads since the last evaluation (FIDELITY BINOMIAL above)
    tile_trials: int = 0
    tile_exceed: int = 0
    tile_first: int | None = None           # its first and last reads' launch indices
    tile_last: int | None = None
    tile_arms: set = field(default_factory=set)          # the arms with a trial in it
    by_cell: dict = field(default_factory=dict)          # 'arm|dose' -> [trials, exceed_tau, exceed_tau4]
    nonfinite: int = 0
    ceiling_exceeded: int = 0
    identity_out: int = 0

    def __post_init__(self) -> None:
        if int(self.cadence) <= 0 or not 0 <= int(self.p0_count) <= int(self.p0_n) or int(self.p0_n) <= 0:
            raise ValueError("the binomial needs a positive cadence and 0 <= p0_count <= p0_n, p0_n > 0")
        if self.ceiling is not None and not float(self.ceiling) > 0.0:
            raise ValueError("the fidelity ceiling, where set, is positive")

    def observe(self, rec: Mapping) -> tuple[list, dict | None, list]:
        """Count one record. Returns the kinds it fires, in PAUSE_KINDS' order; the binomial's batch (its tile), if
        the tile's evaluation at this read fired; and that fire's arms."""
        kinds: list = []
        f = rec["fidelity"]
        if not rec["finite"] or (f is not None and not f["finite"]):
            self.nonfinite += 1
            kinds.append("nonfinite")
        if (self.ceiling is not None and f is not None and f["absdiff"] is not None
                and f["absdiff"] > self.ceiling):            # ADDENDUM-n2 §2.1: at any dose, at once
            self.ceiling_exceeded += 1
            kinds.append("fidelity-ceiling")
        if rec["identity"] is not None and not rec["identity"]["within"]:
            self.identity_out += 1
            kinds.append("identity-bound")
        self.tile_reads += 1
        if self.tile_first is None:
            self.tile_first = rec["launch_index"]
        self.tile_last = rec["launch_index"]
        if f is not None:
            self.trials += 1
            self.tile_trials += 1
            self.tile_arms.add(rec["arm"])
            c = self.by_cell.setdefault(f"{rec['arm']}|{rec['dose_label']}", [0, 0, 0])
            c[0] += 1
            if f["exceeds_tau"] is True:
                self.exceed += 1
                self.tile_exceed += 1
                c[1] += 1
            if f["exceeds_tau4"] is True:
                c[2] += 1
        batch, arms = None, []
        if self.tile_reads >= int(self.cadence):           # the tile's cadence-th read, a trial or not
            batch, arms = self.evaluate()
            if batch is not None:
                kinds.append("fidelity-binomial")
        return kinds, batch, arms

    def evaluate(self) -> tuple[dict | None, list]:
        """One evaluation of the tile: its batch and arms if it fires, else (None, []). The next tile starts at the
        next read, after a fire as after none (PIN above)."""
        self.evaluations += 1
        batch, arms = None, []
        if binom_tail(self.tile_exceed, self.tile_trials, self.p0_count / self.p0_n) <= self.alpha:
            self.fires += 1
            batch = {"first_launch_index": self.tile_first, "last_launch_index": self.tile_last,
                     "k": self.tile_exceed, "n": self.tile_trials, "p0_count": self.p0_count, "p0_n": self.p0_n,
                     "alpha": self.alpha}
            arms = sorted(self.tile_arms)
        self.tile_reads = self.tile_trials = self.tile_exceed = 0
        self.tile_first = self.tile_last = None
        self.tile_arms = set()
        return batch, arms

    def pending(self) -> bool:
        """Reads in the tile since the last evaluation: at the stage's end, its tail."""
        return self.tile_reads > 0


@dataclass
class StageInputs:
    root: Path                            # the stage's cells
    report_path: Path                     # the stage's report, rewritten at every invocation's end
    identity: dict
    sessions: list
    ids_of: Callable                      # (Session, told_line | None) -> list[int]; may raise RenderingMismatch
    label_ids: Callable                   # cue -> list[int]
    backend: object
    directions: Mapping[str, np.ndarray]  # direction_id -> unit vector [d_model]
    alpha: float                          # the binomial's: the identity's fidelity_rule.alpha; run() refuses another
    hour_cap_ms: int | None
    load_ms: int                          # this invocation's model load, wall-clock ms, as the driver measured it;
                                          # required: no default stands in for a measurement. Reported beside the cap,
                                          # outside it (the lock's cap clause; the seat's answers of 2026-11-16, §3):
                                          # loads_ms holds the invocations that wrote a report -- one that ends
                                          # without one is absent there, its records still in used_ms (CAP above)
    rulings: Mapping = field(default_factory=dict)    # pause_id -> the ruling raw's path, for a resume
    printer: Callable = print
    clock: Callable | None = None         # the primitive's timer (time.perf_counter when None)


def _injection(inputs: StageInputs, pr: PlannedRead) -> Injection | None:
    """``Injection.at_frac``, the adapter's sanctioned constructor (rule 1), against the dose map's norm: frac =
    |d| * rho of R on BK's scale, f of R_ell on the program's; the direction verified against the stage's sha before
    any dose is computed; the sign applied after. Its alpha is ``schema.expected_alpha``'s, by the same arithmetic."""
    scale, sign, _ = schema.DOSES[pr.dose_label]
    if sign == 0:
        return None
    ident = inputs.identity
    dm = ident["dose_map"]
    layer = int(ident["layer"])
    u = np.asarray(inputs.directions[pr.direction_id], dtype=np.float64)
    if scale == "bk":
        frac, table = abs(float(pr.dose_value)) * float(dm["rho"]), {layer: float(dm["R"])}
    else:
        frac, table = float(pr.dose_value), {layer: float(dm["R_ell"])}
    try:
        inj = Injection.at_frac(u, layer, frac, table, expect_sha=ident["directions"][pr.direction_id])
    except ValueError as e:
        raise SystemExit(f"direction {pr.direction_id}: {e}")
    inj = inj.with_sign(sign)
    if abs(inj.alpha) != schema.expected_alpha(pr.dose_label, pr.dose_value, dm):
        raise SystemExit(f"{pr.read_id}: alpha {abs(inj.alpha)!r} is not the dose map's")
    return inj


def _pause(n: int, kind: str, read_id: str | None, launch_index: int | None, arms, *, also=(),
           binomial: dict | None = None) -> dict:
    return {"pause_id": f"p{n:02d}", "kind": kind, "read_id": read_id, "launch_index": launch_index,
            "arms_in_scope": sorted(set(arms)), "adjudicated": False, "ruling_sha256": None, "binomial": binomial,
            "also_fired": list(also), "resumed_at_launch_index": None}


def _scope(arm: str, dose_label: str, session_id: str, plan: Sequence[PlannedRead], extra=()) -> list:
    """SCOPE (PIN above): the read's arm and the binomial batch's arms; for a shadow, also every arm whose steered
    reads of that session pair with it."""
    arms = {arm, *extra}
    if arm == schema.SHADOW_ARM and dose_label == schema.SHADOW_DOSE:
        arms |= {p.arm for p in plan if p.session.session_id == session_id and schema.DOSES[p.dose_label][1] != 0}
    return sorted(arms)


def _prior_report(inputs: StageInputs, ident: Mapping) -> dict | None:
    """The stage's last report, checked, its identity this stage's; None if the stage has none."""
    rp = Path(inputs.report_path)
    if not rp.exists():
        return None
    rep = cells.read_json(rp)
    try:
        schema.check_report(rep, where=rp.name)
    except schema.SchemaError as e:
        raise SystemExit(f"{rp.name}: not a valid report: {e}"[:400])
    if rep["stage_identity_sha256"] != schema.identity_sha256(ident):
        raise SystemExit(f"{rp.name}: the report's stage identity is not this run's -- a resume is refused")
    if rep["end_state"] in schema.STOP_KINDS:
        raise SystemExit(f"{rp.name}: the stage ended {rep['end_state']}; nothing resumes after a STOP")
    return rep


def _report(inputs: StageInputs, ident: Mapping, plan: Sequence[PlannedRead], pauses: list, end: str,
            used_ms: int, mon: Monitors, loads_ms: Sequence[int] = ()) -> dict:
    """The stage report (n-report-v1) from the files on disk and the monitors."""
    root = Path(inputs.root)
    planned: dict = {}
    for p in plan:
        planned[p.arm] = planned.get(p.arm, 0) + 1
    obtained: dict = {}
    entries: dict = {}
    for key in sorted({(p.arm, p.direction_id, p.dose_label) for p in plan}):
        jp = cells.cell_path(root, *key)
        if not jp.exists():
            continue
        data = jp.read_bytes()
        cell = cells.json_bytes(data, jp.name)               # the bytes parsed are the bytes hashed
        entries[jp.name] = {"json_sha256": hashlib.sha256(data).hexdigest(),
                            "capture_sha256": cell["capture_sha256"], "records": len(cell["records"])}
        obtained[key[0]] = obtained.get(key[0], 0) + len(cell["records"])
    per_arm = {a: {"planned": n, "obtained": obtained.get(a, 0), "complete": obtained.get(a, 0) == n}
               for a, n in sorted(planned.items())}
    cap = inputs.hour_cap_ms
    return {
        "schema": schema.REPORT_SCHEMA, "stage_identity": dict(ident),
        "stage_identity_sha256": schema.identity_sha256(ident),
        "read_plan_sha256": schema.read_plan_sha256(ident) if ident["stage"] == "campaign" else None,
        "end_state": end, "per_arm": per_arm, "cells": entries, "pauses": pauses,
        "binomial_state": {"trials": mon.trials, "exceed_tau": mon.exceed, "evaluations": mon.evaluations,
                           "fires": mon.fires},
        "stop": None,
        "cap": {"hour_cap_ms": cap, "used_ms": int(used_ms), "hit": cap is not None and used_ms >= cap,
                "loads_ms": [int(x) for x in loads_ms]},
        "counters": {"fidelity": {k: {"trials": v[0], "exceed_tau": v[1], "exceed_tau4": v[2]}
                                  for k, v in sorted(mon.by_cell.items())},
                     "nonfinite_reads": mon.nonfinite,
                     "fidelity_ceiling_exceeded": None if mon.ceiling is None else mon.ceiling_exceeded,
                     "identity_out_of_bound": mon.identity_out,
                     "rendering_mismatches": sum(1 for p in pauses if p["kind"] == "rendering"),
                     "label_mass_below_floor": None},
    }


def run(inputs: StageInputs, plan: Sequence[PlannedRead], *, resume: bool) -> dict:
    """One invocation: replay, launch, report. Returns the report written."""
    from . import primitive
    ident = inputs.identity
    schema.check_stage_identity(ident)
    ka = stream_known_answer()
    if ka:
        raise SystemExit(ka[0])
    if [p.launch_index for p in plan] != list(range(len(plan))) or len({p.read_id for p in plan}) != len(plan):
        raise SystemExit("the plan's launch indices are not 0, 1, ... in order, or a read repeats")
    fr = ident["fidelity_rule"]
    if float(inputs.alpha) != float(fr["alpha"]):
        raise SystemExit(f"the stage's alpha {float(inputs.alpha)!r} is not its identity's fidelity_rule.alpha "
                         f"{float(fr['alpha'])!r} -- refusing (a batch the schema refuses is never written)")
    mon = Monitors(cadence=int(fr["cadence"]), p0_count=int(fr["p0_count"]), p0_n=int(fr["p0_n"]),
                   alpha=float(inputs.alpha), ceiling=None if fr["ceiling"] is None else float(fr["ceiling"]))
    root = Path(inputs.root)
    root.mkdir(parents=True, exist_ok=True)
    cell_keys = sorted({(p.arm, p.direction_id, p.dose_label) for p in plan})
    done = cells.done_read_ids(root, cell_keys)
    prior = _prior_report(inputs, ident)
    if (done or prior is not None) and not resume:
        raise SystemExit("records or a report are on disk for this stage; run with --resume (skip-only) or another "
                         "root")
    open_cells = {key: cells.load_cell(root, *key, identity=ident) for key in cell_keys}
    on_disk = sorted((r for (c, _a) in open_cells.values() for r in c["records"]), key=lambda r: r["launch_index"])
    if len({r["launch_index"] for r in on_disk}) != len(on_disk):
        raise SystemExit("two records on disk share a launch index -- refusing")
    plan_ids = [p.read_id for p in plan]
    for r in on_disk:
        if not 0 <= r["launch_index"] < len(plan) or plan_ids[r["launch_index"]] != r["read_id"]:
            raise SystemExit(f"read {r['launch_index']} on disk is not the plan's read at that place -- refusing")
    if [r["launch_index"] for r in on_disk] != list(range(len(on_disk))):
        raise SystemExit("the records on disk are not the plan's first reads, 0..M-1 -- refusing (the tiles are the "
                         "plan's reads in order: FIDELITY BINOMIAL above)")
    used_ms = sum(r["duration_ms"] for r in on_disk)
    if prior is not None:
        if prior["cap"]["hour_cap_ms"] != inputs.hour_cap_ms:
            raise SystemExit("the stage's report on disk has another cap: a resume keeps the stage's cap")
        if any(p["binomial"] is not None and p["binomial"]["alpha"] != float(inputs.alpha) for p in prior["pauses"]):
            raise SystemExit("the stage's report on disk has another alpha: a resume keeps the stage's alpha")

    # the prior pauses and this resume's rulings (every standing pause needs one; the seat adjudicates)
    pauses = [dict(p) for p in (prior["pauses"] if prior is not None else [])]
    rulings = {str(pid): hashlib.sha256(Path(path).read_bytes()).hexdigest()
               for pid, path in dict(inputs.rulings).items()}
    for p in pauses:
        if not p["adjudicated"]:
            if p["pause_id"] not in rulings:
                raise SystemExit(f"pause {p['pause_id']} ({p['kind']}) stands: a resume needs its ruling (rule 21)")
            p.update(adjudicated=True, ruling_sha256=rulings.pop(p["pause_id"]))
    if rulings:
        raise SystemExit(f"rulings name no standing pause: {sorted(rulings)}")

    # replay: the records reproduce every prior pause that has a read; an unreported fire is a pause now
    prior_at = {p["launch_index"]: p for p in pauses if p["launch_index"] is not None and p["kind"] != "rendering"}
    matched: set = set()
    halted = False
    for i, r in enumerate(on_disk):
        kinds, batch, arms = mon.observe(r)
        p = prior_at.get(r["launch_index"])
        if not kinds:
            if p is not None:
                raise SystemExit(f"pause {p['pause_id']}: its read does not fire on replay -- refusing")
            continue
        if p is None:
            if i != len(on_disk) - 1:
                raise SystemExit(f"read {r['launch_index']} fired {kinds} with reads after it and no pause -- refusing")
            pauses.append(_pause(len(pauses) + 1, kinds[0], r["read_id"], r["launch_index"],
                                 _scope(r["arm"], r["dose_label"], r["session_id"], plan, arms), also=kinds[1:],
                                 binomial=batch))
            halted = True
            continue
        if (p["read_id"], p["kind"], p["also_fired"], p["binomial"]) != (r["read_id"], kinds[0], kinds[1:], batch):
            raise SystemExit(f"pause {p['pause_id']}: the records do not reproduce it -- refusing")
        matched.add(p["pause_id"])
    missing = sorted(p["pause_id"] for p in prior_at.values() if p["pause_id"] not in matched)
    if missing:
        raise SystemExit(f"pauses {missing}: no record on disk reproduces them -- refusing")
    closed = next((p for p in pauses if p["launch_index"] is None), None)
    if closed is not None and not (inputs.hour_cap_ms is not None and used_ms >= inputs.hour_cap_ms) and any(
            pr.read_id not in done for pr in plan):
        raise SystemExit(f"pause {closed['pause_id']} fired at the run's end: no read is launched after it")

    # launch
    shadows = {r["read_id"]: r for r in on_disk if r["dose_label"] == "0" and r["arm"] == schema.SHADOW_ARM}
    end = "PAUSE" if halted else "COMPLETE"
    labels: dict = {}
    for pr in ([] if halted else plan):
        if pr.read_id in done:
            continue
        if inputs.hour_cap_ms is not None and used_ms >= inputs.hour_cap_ms:
            end = "CAP"
            break
        s = pr.session
        told = None
        if pr.arm in schema.TOLD_VARIANT:
            named = s.cue_S if pr.schedule_zone == "S" else s.cue_U
            told = schema.TOLD_LINE.format(zone=named) if pr.arm == "N4-T" else schema.SHAM_LINE
        head = f"read {pr.launch_index} s={s.bk_run} {pr.arm} {pr.direction_id} {pr.dose_label}"
        try:
            ids = [int(x) for x in inputs.ids_of(s, told)]
            if told is None and ids_sha(ids) != s.ids_sha:
                raise RenderingMismatch(f"{s.session_id}: ids_sha {ids_sha(ids)} is not BK's {s.ids_sha}")
        except RenderingMismatch:
            pauses.append(_pause(len(pauses) + 1, "rendering", pr.read_id, pr.launch_index,
                                 _scope(pr.arm, pr.dose_label, s.session_id, plan)))
            inputs.printer(f"{head} RENDERING MISMATCH: not launched; PAUSE")
            end = "PAUSE"
            break
        for cue in (s.cue_S, s.cue_U):
            if cue not in labels:
                labels[cue] = [int(x) for x in inputs.label_ids(cue)]
        need = len(ids) + max(len(labels[s.cue_S]), len(labels[s.cue_U])) - 1
        if need > int(ident["read_window"]):
            raise SystemExit(f"{head}: a forward of {need} tokens exceeds the stage's read_window -- refusing")
        spec = primitive.ReadSpec(arm=pr.arm, direction_id=pr.direction_id, dose_label=pr.dose_label,
                                  dose_value=pr.dose_value, injection=_injection(inputs, pr), told_line=told,
                                  schedule_zone=pr.schedule_zone)
        key = (pr.arm, pr.direction_id, pr.dose_label)
        cell, arr = open_cells[key]
        rec, caps = primitive.read(
            inputs.backend, s, ids, None if told is not None else s.ids_sha, spec, labels[s.cue_S], labels[s.cue_U],
            ident["capture_layers"], fidelity_reason=pr.fidelity_reason,
            shadow=shadows.get(schema.shadow_read_id(s.session_id)),
            identity_bound=ident["identity_bound"], launch_index=pr.launch_index, capture_row=len(cell["records"]),
            clock=inputs.clock)
        cell, arr = cells.append_record(root, cell, arr, rec, caps)
        open_cells[key] = (cell, arr)
        used_ms += rec["duration_ms"]
        if pr.arm == schema.SHADOW_ARM and pr.dose_label == "0":
            shadows[rec["read_id"]] = rec
        f = rec["fidelity"]
        fid = "-" if f is None else ("nonfinite" if f["rel"] is None else
                                     f"{f['rel']:.6f} {'>' if f['exceeds_tau'] else '<='} TAU")
        inputs.printer(f"{head} fid={fid} ms={rec['duration_ms']}")
        kinds, batch, arms = mon.observe(rec)
        if kinds:
            pauses.append(_pause(len(pauses) + 1, kinds[0], rec["read_id"], pr.launch_index,
                                 _scope(pr.arm, pr.dose_label, s.session_id, plan, arms), also=kinds[1:],
                                 binomial=batch))
            inputs.printer(f"PAUSE {kinds[0]} at read {pr.launch_index}")
            end = "PAUSE"
            break

    # the end-of-run evaluation: no read remains to launch
    prior_end = next((p for p in pauses if p["launch_index"] is None), None)
    if end in ("COMPLETE", "CAP"):
        if mon.pending():
            batch, arms = mon.evaluate()
            if prior_end is not None:
                if batch != prior_end["binomial"]:
                    raise SystemExit(f"pause {prior_end['pause_id']}: the end-of-run evaluation does not reproduce "
                                     f"it -- refusing")
            elif batch is not None:
                pauses.append(_pause(len(pauses) + 1, "fidelity-binomial", None, None, arms, binomial=batch))
                inputs.printer("PAUSE fidelity-binomial at the run's end")
                end = "PAUSE"
        elif prior_end is not None:
            raise SystemExit(f"pause {prior_end['pause_id']}: no end-of-run evaluation reproduces it -- refusing")
    if end == "COMPLETE" and inputs.hour_cap_ms is not None and used_ms >= inputs.hour_cap_ms:
        end = "CAP"

    # each adjudicated pause resumed at the first read attempted after its own: launched (a record on disk) or refused
    # as a rendering mismatch (a later rendering pause's place); at its own place, for a rendering pause
    launched = [r["launch_index"] for (c, _a) in open_cells.values() for r in c["records"]]
    for i, p in enumerate(pauses):
        li = p["launch_index"]
        if p["adjudicated"] and li is not None:
            attempts = launched + [q["launch_index"] for q in pauses[i + 1:] if q["kind"] == "rendering"]
            later = sorted(x for x in attempts if x > li or (x == li and p["kind"] == "rendering"))
            p["resumed_at_launch_index"] = later[0] if later else None
    loads_ms = (list(prior["cap"]["loads_ms"]) if prior is not None else []) + [int(inputs.load_ms)]
    report = _report(inputs, ident, plan, pauses, end, used_ms, mon, loads_ms)
    schema.check_report(report)
    Path(inputs.report_path).parent.mkdir(parents=True, exist_ok=True)
    m_resume.atomic_write_json(Path(inputs.report_path), report)
    obtained = sum(x["obtained"] for x in report["per_arm"].values())
    inputs.printer(f"end {end}: {obtained}/{len(plan)} reads; report {Path(inputs.report_path).name}")
    return report


def _selftest(chk, tmp) -> None:
    from fractions import Fraction

    from .primitive import test_identity
    from .sessions import load_sessions
    from .testing import CausalDouble, toy_session
    tmp = Path(tmp)
    chk("runner: binom_tail(1, 160, 0) = 0 (p0 = 0 fires at the first exceedance)", binom_tail(1, 160, 0.0) == 0.0, "")
    chk("runner: binom_tail(0, n, p) = 1", binom_tail(0, 160, 0.3) == 1.0, "")
    chk("runner: binom_tail(2, 4, 0.5) = 11/16", abs(binom_tail(2, 4, 0.5) - float(Fraction(11, 16))) < 1e-12, "")
    chk("runner: binom_tail(1, 3200, 1/2400) = 1 - (2399/2400)^3200, with no overflow at a campaign's n",
        abs(binom_tail(1, 3200, 1 / 2400) - (1.0 - (2399 / 2400) ** 3200)) < 1e-12, binom_tail(1, 3200, 1 / 2400))
    chk("runner: binom_tail(40, 7360, 0.001) is a probability (no overflow)",
        0.0 <= binom_tail(40, 7360, 0.001) <= 1.0, "")
    ident0 = schema.example_identity()
    ss = load_sessions()
    sch = keys.n4_schedule([s.present_first_is_S for s in ss])
    bad_sch = list(sch)
    bad_sch[0] = "U" if bad_sch[0] == "S" else "S"
    try:
        check_schedule(ss, bad_sch)
        sched_refused = False
    except SystemExit:
        sched_refused = True
    chk("runner: an N4 schedule off 80/80, or off 40 told-S per present-order group, is refused", sched_refused, "")
    order = campaign_order(ident0, ss, sch)
    chk("runner: the campaign order covers the declared plan (7,680 reads, N1-P's four points: ADDENDUM-n1 §5.2)",
        len(order) == 7680, len(order))
    chk("runner: the 160 shadows come first", all(p.arm == "N1-V" and p.dose_label == "0" for p in order[:160]), "")
    arms_seen = []
    for p in order[160:]:
        if not arms_seen or arms_seen[-1] != p.arm:
            arms_seen.append(p.arm)
    chk("runner: then arm-major in ARMS order", arms_seen == list(schema.ARMS), arms_seen)
    chk("runner: every read at 0, +1, -1 takes the dose-rule re-computation",
        all(p.fidelity_reason == "dose-rule" for p in order if p.dose_label in schema.DOSE_RULE_LABELS), "")
    chk("runner: the other points take the keyed sample, and only it",
        all(p.fidelity_reason == ("sample" if keys.fid_sampled(p.session.bk_run) else None)
            for p in order if p.dose_label not in schema.DOSE_RULE_LABELS), "")
    chk("runner: N4 reads carry the schedule's zone; others none",
        all((p.schedule_zone == sch[p.session.bk_run]) if p.arm in schema.TOLD_VARIANT else p.schedule_zone is None
            for p in order), "")
    try:                                                    # the counts are literals: independent of read_plan
        o50 = campaign_order(schema.example_identity(R_ell=50.0), ss, sch)
        o40 = campaign_order(schema.example_identity(R_ell=40.0), ss, sch)
        merged_ok = ((len(o50), len(o40)) == (6400, 5280)
                     and sum(1 for p in o40 if (p.arm, p.dose_label) == ("N1-P", "+1/2")) == 160
                     and not any(p.dose_label in ("+d_20", "+d_eq") for p in o40)
                     and not any(p.dose_label == "+d_20" for p in o50))
        merged_detail = (len(o50), len(o40))
    except (KeyError, AssertionError) as e:
        merged_ok, merged_detail = False, f"{type(e).__name__}: {e}"[:120]
    chk("runner: under merged dose maps each merged point is read once under its keeper: 6,400 reads with +d_20 in "
        "+1 (R_ell 50.0), 5,280 with +d_eq also in +1/2 (R_ell 40.0), N1-P's 160 +1/2 reads among them",
        merged_ok, merged_detail)

    # the monitors: the tile (R12), its evaluation, kinds in precedence order
    def rec_at(i, **kw):
        return schema.example_record(ident0, "N1-V", "valence", "+1", 3, launch=i, **kw)
    m = Monitors(cadence=4, p0_count=0, p0_n=2400, alpha=0.01)
    fired = [m.observe(r) for r in (rec_at(0), rec_at(1, fresh_shift=0.5), rec_at(2), rec_at(3))]
    chk("runner: an exceedance fires the binomial at its tile's evaluation, the tile's cadence-th read, not before",
        [k for k, _b, _a in fired] == [[], [], [], ["fidelity-binomial"]], [k for k, _b, _a in fired])
    b = fired[3][1]
    chk("runner: the fire's batch is its tile, reads 0-3, 1 of 4, under the monitors' p0",
        b is not None and (b["first_launch_index"], b["last_launch_index"], b["k"], b["n"]) == (0, 3, 1, 4)
        and (b["p0_count"], b["p0_n"]) == (0, 2400), b)
    again = [m.observe(rec_at(i))[0] for i in range(4, 8)]
    chk("runner: the next tile starts at the next read, without the earlier exceedance: four clean trials fire "
        "nothing (R12: every read in exactly one tile)", again == [[], [], [], []], again)
    after = [m.observe(rec_at(i, fresh_shift=0.5 if i == 9 else 0.0)) for i in range(8, 12)]
    b_after = after[3][1]
    chk("runner: ...and a third tile fires on its own exceedance alone, its batch reads 8-11, 1 of 4",
        [k for k, _b, _a in after] == [[], [], [], ["fidelity-binomial"]] and b_after is not None
        and (b_after["first_launch_index"], b_after["last_launch_index"], b_after["k"], b_after["n"])
        == (8, 11, 1, 4), after[3])
    chk("runner: evaluations and fires counted: three tiles, two fires", (m.evaluations, m.fires) == (3, 2),
        (m.evaluations, m.fires))
    m2 = Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01)
    nf = schema.example_record(ident0, "N1-V", "none", "0", 3, finite=False)
    k_nf = m2.observe(nf)[0]
    chk("runner: a non-finite d = 0 read fires nonfinite first, identity-bound after it", k_nf == ["nonfinite",
        "identity-bound"], k_nf)
    out_b = schema.example_record(ident0, "N1-V", "none", "0", 3, fresh_shift=0.5)
    chk("runner: an identity check outside the bound (0.5 against 0.25) fires identity-bound alone, where the "
        "monitors hold no ceiling", m2.observe(out_b)[0] == ["identity-bound"], "")
    # the fidelity ceiling (ADDENDUM-n2 §2.1): at any dose, at once, after nonfinite in PAUSE_KINDS' order
    m6 = Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01, ceiling=0.25)
    k_c = m6.observe(rec_at(20, fresh_shift=0.5))[0]
    chk("runner: a re-computed +1 read whose |cached - fresh margin| is above the ceiling (0.5 > 0.25) fires "
        "fidelity-ceiling at once, counted", k_c == ["fidelity-ceiling"] and m6.ceiling_exceeded == 1, k_c)
    k_below = m6.observe(rec_at(21, fresh_shift=0.2))[0]
    chk("runner: ...one below the ceiling (0.2) fires nothing", k_below == [] and m6.ceiling_exceeded == 1, k_below)
    k_d0 = m6.observe(schema.example_record(ident0, "N1-V", "none", "0", 3, fresh_shift=0.5))[0]
    chk("runner: ...a d = 0 read above it fires fidelity-ceiling, then identity-bound (the bound is C), in that order",
        k_d0 == ["fidelity-ceiling", "identity-bound"] and m6.ceiling_exceeded == 2, k_d0)
    k_eq = m6.observe(rec_at(22, fresh_shift=0.25))[0]
    chk("runner: ...one exactly at the ceiling (|2.125 - 1.875| = 0.25) fires nothing: \"above C\" (ADDENDUM-n2 §2.1)",
        k_eq == [] and m6.ceiling_exceeded == 2, k_eq)
    m8 = Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01, ceiling=0.25)
    k_reach = [m8.observe(schema.example_record(ident0, "N1-V", "valence", "+1/2", 3, launch=40 + j, fidelity=fr_,
                                                fresh_shift=0.5))[0] for j, fr_ in enumerate(("sample", "timing"))]
    chk("runner: ...a keyed-sample and a timing re-computation above it fire it too (every re-computed read, at any "
        "dose)", k_reach == [["fidelity-ceiling"], ["fidelity-ceiling"]] and m8.ceiling_exceeded == 2, k_reach)
    k_nf6 = Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01, ceiling=0.25).observe(nf)[0]
    chk("runner: ...a non-finite read fires nonfinite, never the ceiling (no finite discordance to compare)",
        k_nf6 == ["nonfinite", "identity-bound"], k_nf6)
    m7 = Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01)
    k_none = m7.observe(rec_at(30, fresh_shift=5.0))[0]
    chk("runner: ...with no ceiling (backend-ext) a discordance of 5 nats fires no fidelity-ceiling",
        k_none == [] and m7.ceiling_exceeded == 0, k_none)
    try:
        Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01, ceiling=0.0)
        bad_ceiling = False
    except ValueError:
        bad_ceiling = True
    chk("runner: ...a ceiling that is not positive is refused", bad_ceiling, "")

    # the tile is in reads: evaluated at its cadence-th read, a trial or not; a tile with no trial; the tail
    def plain_at(i):
        return schema.example_record(ident0, "N1-V", "valence", "+1/2", 3, launch=i)      # no re-computation

    def n2_at(i):
        return schema.example_record(ident0, "N2-E", "span_reward", "f0.10", 3, launch=i)  # no re-computation
    m3 = Monitors(cadence=4, p0_count=0, p0_n=2400, alpha=0.01)
    k3 = [m3.observe(r) for r in (rec_at(0, fresh_shift=0.5), n2_at(1), n2_at(2), n2_at(3), rec_at(4))]
    b3 = k3[3][1]
    chk("runner: a tile is evaluated at its cadence-th read though that read has no re-computation; the batch's first "
        "and last are the tile's reads (0, 3), 1 of its 1 trial, and the fire's arms the trials' alone (N1-V, not the "
        "N2-E reads without one)",
        [k for k, _b, _a in k3] == [[], [], [], ["fidelity-binomial"], []] and b3 is not None
        and (b3["first_launch_index"], b3["last_launch_index"], b3["k"], b3["n"]) == (0, 3, 1, 1)
        and k3[3][2] == ["N1-V"], k3[3])
    m3e = Monitors(cadence=4, p0_count=0, p0_n=2400, alpha=0.01)
    k3e = [m3e.observe(r) for r in (plain_at(0), rec_at(1, fresh_shift=0.5), plain_at(2), plain_at(3))]
    b3e = k3e[3][1]
    chk("runner: a tile that opens on a read with no re-computation begins there: its batch is (0, 3), 1 of 1, not "
        "from its first trial",
        b3e is not None and (b3e["first_launch_index"], b3e["last_launch_index"], b3e["k"], b3e["n"]) == (0, 3, 1, 1),
        b3e)
    m3b = Monitors(cadence=4, p0_count=0, p0_n=2400, alpha=0.01)
    k3b = [m3b.observe(plain_at(i)) for i in range(4)]
    chk("runner: a tile with no trial is evaluated at its cadence-th read and cannot fire",
        [k for k, _b, _a in k3b] == [[], [], [], []] and (m3b.evaluations, m3b.fires) == (1, 0)
        and not m3b.pending(), (m3b.evaluations, m3b.fires))

    def pole_at(i, **kw):
        return schema.example_record(ident0, "N1-P", "valence", "+1", 3, launch=i, **kw)
    m3c = Monitors(cadence=4, p0_count=0, p0_n=2400, alpha=0.01)
    k3c = [m3c.observe(pole_at(i, fresh_shift=0.5 if i == 2 else 0.0) if i < 4
                       else rec_at(i, fresh_shift=0.5 if i == 9 else 0.0)) for i in range(10)]
    tail_due = m3c.pending()
    b_tail, a_tail = m3c.evaluate()
    chk("runner: ten reads at cadence 4 are evaluated at reads 3 and 7, the tail (reads 8-9) pending after them; the "
        "first tile (N1-P's reads) fires on N1-P alone, and the end-of-run evaluation on the tail's own exceedance, "
        "its batch the tail's reads, 1 of 2, its arms the tail's (N1-V), none carried from an earlier tile",
        [i for i, (k, _b, _a) in enumerate(k3c) if k] == [3] and k3c[3][2] == ["N1-P"] and tail_due
        and (m3c.evaluations, m3c.fires) == (3, 2) and b_tail is not None
        and (b_tail["first_launch_index"], b_tail["last_launch_index"], b_tail["k"], b_tail["n"]) == (8, 9, 1, 2)
        and a_tail == ["N1-V"] and not m3c.pending(), (b_tail, a_tail, m3c.evaluations, m3c.fires))
    m3d = Monitors(cadence=4, p0_count=0, p0_n=2400, alpha=0.01)
    m3d.observe(plain_at(0))
    chk("runner: a tail of one read with no trial is pending, and its evaluation fires nothing",
        m3d.pending() and m3d.evaluate() == (None, []) and m3d.evaluations == 1 and not m3d.pending(), "")
    m9 = Monitors(cadence=4, p0_count=0, p0_n=2400, alpha=0.01, ceiling=0.25)
    k9 = [m9.observe(rec_at(i, fresh_shift=0.5 if i == 0 else 0.0)) for i in range(4)]
    b9 = k9[3][1]
    chk("runner: a ceiling read stays in its tile as a trial and, its rel above TAU, as an exceedance (R13): the "
        "ceiling fires at read 0 and the tile, 1 of 4, at read 3",
        [k for k, _b, _a in k9] == [["fidelity-ceiling"], [], [], ["fidelity-binomial"]] and b9 is not None
        and (b9["k"], b9["n"]) == (1, 4), [k for k, _b, _a in k9])
    m160 = Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01)
    k160 = [m160.observe(rec_at(i, fresh_shift=0.5 if i == 0 else 0.0))[0] for i in range(160)]
    m160b = Monitors(cadence=160, p0_count=1, p0_n=2400, alpha=0.01)
    k160b = [m160b.observe(rec_at(i, fresh_shift=0.5 if i == 0 else 0.0))[0] for i in range(160)]
    chk("runner: under p0 = 0 one exceedance in 160 fires at the cadence; under p0 = 1/2400 it does not",
        k160[-1] == ["fidelity-binomial"] and not any(k160[:-1]) and not any(k160b), (k160[-1], k160b[-1]))
    m4 = Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01)
    m4.observe(rec_at(0, fresh_shift=0.04))                 # rel 0.0107: above TAU/4, below TAU
    chk("runner: a re-computation above TAU/4 and below TAU is no exceedance; it counts in the TAU/4 row",
        m4.exceed == 0 and m4.by_cell["N1-V|+1"] == [1, 0, 1], (m4.exceed, m4.by_cell))
    fresh_nf = rec_at(0)
    fresh_nf["fidelity"] = dict(fresh_nf["fidelity"], finite=False, fresh_margin=None, rel=None, exceeds_tau=None,
                                exceeds_tau4=None)
    m5 = Monitors(cadence=160, p0_count=0, p0_n=2400, alpha=0.01)
    chk("runner: a finite read whose re-computation is not finite fires nonfinite",
        m5.observe(fresh_nf)[0][:1] == ["nonfinite"], "")
    rep_sc = schema.example_report(ident0, end_state="COMPLETE", pauses=[schema.example_pause(1)])
    try:
        schema.check_report(rep_sc)
        sc = "accepted"
    except schema.SchemaError as e:
        sc = str(e)
    chk("runner: a COMPLETE report over a standing pause, every arm complete, is refused by the standing rule",
        "a standing pause ends only by a ruling or under PI-STOP" in sc, sc[:160])

    # small runs through the numpy double, at the time stage (its per-arm counts are the plan's)
    be = CausalDouble()
    u = np.random.default_rng(7).standard_normal(be.d_model)
    ident, dirs = test_identity(u, n_layers=be.n_layers, d_model=be.d_model)
    ident = dict(ident, stage="time")
    toys = [toy_session(r)[0] for r in (3, 4)]
    toy_ids = {s.bk_run: toy_session(s.bk_run)[1] for s in toys}
    kept = schema.dose_point_values(ident)
    plan = []
    for arm, did, dl in (("N1-V", "none", "0"), ("N1-V", "valence", "+1"), ("N1-V", "valence", "+1/2")):
        for s in toys:
            plan.append(PlannedRead(len(plan), s, arm, did, dl, kept[dl],
                                    "dose-rule" if dl in schema.DOSE_RULE_LABELS else None, None))

    def fake_clock():
        t = {"v": 0.0}

        def clock():
            t["v"] += 0.25
            return t["v"]
        return clock

    def inputs_for(name, backend=be, ids_of=None, cap=None, rulings=None, printer=None, identity=None, load_ms=5000):
        return StageInputs(root=tmp / name / "cells", report_path=tmp / name / "report.json",
                           identity=identity or ident,
                           sessions=toys, ids_of=ids_of or (lambda s, told: toy_ids[s.bk_run]),
                           label_ids=lambda cue: [5, 9, 17] if cue == "Zone W6" else [5, 11, 2], backend=backend,
                           directions=dirs, alpha=0.01, hour_cap_ms=cap, load_ms=load_ms, rulings=rulings or {},
                           printer=printer or (lambda *_: None), clock=fake_clock())

    def obtained(rep):
        return sum(x["obtained"] for x in rep["per_arm"].values())

    def refused(fn):
        try:
            fn()
            return False
        except SystemExit:
            return True

    lines: list = []
    rep = run(inputs_for("ok", printer=lines.append), plan, resume=False)
    chk("runner: a small run completes and obtains its plan", rep["end_state"] == "COMPLETE" and obtained(rep) == 6,
        rep["end_state"])
    chk("runner: its report is written and passes check_report", schema.check_report(
        cells.read_json(tmp / "ok" / "report.json")) is None, "")
    chk("runner: stdout lines name index, session, arm, dose, fidelity and ms -- never a margin",
        len(lines) == 7 and all("margin" not in x and "logprob" not in x for x in lines), lines[:2])
    chk("runner: the report's cell sha256s are the files'", all(
        rep["cells"][n]["json_sha256"] == hashlib.sha256((tmp / "ok" / "cells" / n).read_bytes()).hexdigest()
        for n in rep["cells"]), "")
    rep2 = run(inputs_for("ok", printer=lines.append), plan, resume=True)
    chk("runner: a resume skips every read on disk", obtained(rep2) == 6 and len(lines) == 8 and
        rep2["end_state"] == "COMPLETE", len(lines))
    rep_la = run(inputs_for("loads", load_ms=111), plan, resume=False)
    rep_lb = run(inputs_for("loads", load_ms=222), plan, resume=True)
    chk("runner: loads_ms lists each reporting invocation's load in order, beside the cap and outside used_ms",
        rep_la["cap"]["loads_ms"] == [111] and rep_lb["cap"]["loads_ms"] == [111, 222]
        and rep_lb["cap"]["used_ms"] == rep_la["cap"]["used_ms"], (rep_la["cap"], rep_lb["cap"]))
    chk("runner: a fresh run over records on disk is refused", refused(lambda: run(inputs_for("ok"), plan,
                                                                                   resume=False)), "")
    ident_a = dict(ident, fidelity_rule=dict(ident["fidelity_rule"], alpha=0.05))
    chk("runner: a stage whose inputs' alpha (0.01) is not its identity's fidelity_rule.alpha (0.05) is refused before "
        "any read, with nothing written", refused(lambda: run(inputs_for("alpha", identity=ident_a), plan,
                                                              resume=False)) and not (tmp / "alpha").exists(), "")
    from .primitive import _logp
    shadow3 = cells.load_cell(tmp / "ok" / "cells", "N1-V", "none", "0", identity=ident)[0]["records"][0]
    rows3, _caps3 = be.full(toy_ids[3], [5, 9, 17], [], ident["capture_layers"])
    lp_S = math.fsum(_logp(rows3[i], t) for i, t in enumerate([5, 9, 17]))
    chk("runner: a record's logprob_S is its cue_S label's (a known answer on the double: labels bound to cues)",
        shadow3["session_id"] == toys[0].session_id and abs(shadow3["logprob_S"] - lp_S) < 1e-9,
        (shadow3["logprob_S"], lp_S))
    chk("runner: a resume under another cap than the stage's is refused",
        refused(lambda: run(inputs_for("ok", cap=10 ** 9), plan, resume=True)), "")
    gap = [PlannedRead(i + 1, p.session, p.arm, p.direction_id, p.dose_label, p.dose_value, p.fidelity_reason,
                       p.schedule_zone) for i, p in enumerate(plan)]
    chk("runner: a plan whose launch indices are not 0, 1, ... is refused",
        refused(lambda: run(inputs_for("gap"), gap, resume=False)), "")

    # the other arms and doses: -1, N1-P's twelve turns, N2-E on the program's scale, N4's told and sham lines
    wide: list = []

    def addw(arm, did, dl, s, zone=None):
        wide.append(PlannedRead(len(wide), s, arm, did, dl, kept[dl],
                                "dose-rule" if dl in schema.DOSE_RULE_LABELS else None, zone))
    for s in toys:
        addw("N1-V", "none", "0", s)
    for s in toys:
        addw("N1-P", "valence", "+1", s)
        addw("N1-V", "valence", "-1", s)
    for s in toys:
        addw("N2-E", "span_reward", "f0.10", s)
    for s, z in zip(toys, ("S", "U")):
        addw("N4-T", "none", "0", s, z)
        addw("N4-Ts", "none", "0", s, z)
    repw = run(inputs_for("wide"), wide, resume=False)

    def recs(name, arm, did, dl):
        return cells.load_cell(tmp / name / "cells", arm, did, dl, identity=ident)[0]["records"]
    neg = recs("wide", "N1-V", "valence", "-1")
    pole = recs("wide", "N1-P", "valence", "+1")
    n2 = recs("wide", "N2-E", "span_reward", "f0.10")
    n4 = recs("wide", "N4-T", "none", "0") + recs("wide", "N4-Ts", "none", "0")
    chk("runner: -1, N1-P, N2-E and N4 reads complete through the runner, each record checked",
        repw["end_state"] == "COMPLETE" and obtained(repw) == 12, repw["end_state"])
    chk("runner: a -1 read injects with sign -1", len(neg) == 2 and all(r["sign"] == -1 for r in neg), "")
    chk("runner: N1-P steers all twelve turns; N1-V the six S turns",
        all(len(r["steered_spans"]) == 12 for r in pole) and all(len(r["steered_spans"]) == 6 for r in neg), "")
    chk("runner: N2-E's alpha is f * R_ell, the program's scale",
        len(n2) == 2 and all(r["alpha"] == r["dose_value"] * ident["dose_map"]["R_ell"] for r in n2), "")
    chk("runner: N4-T names the schedule's zone in its told line; N4-Ts carries the sham line",
        [r["told_line"] for r in n4] == [schema.TOLD_LINE.format(zone=toys[0].cue_S),
                                         schema.TOLD_LINE.format(zone=toys[1].cue_U), schema.SHAM_LINE,
                                         schema.SHAM_LINE], [r["told_line"] for r in n4])
    fb_w = CausalDouble()
    orig_fw = fb_w.full

    def biased_full_w(ids, label_ids, injections, capture_layers):
        rows, caps = orig_fw(ids, label_ids, injections, capture_layers)
        if injections:
            rows = rows.copy()
            rows[:, 9] += np.float32(2.0)
        return rows, caps
    fb_w.full = biased_full_w
    # the binomial's tests run under a ceiling above their injected discordance (+2.0 on a logit, about 2 nats), the
    # bound with it, so that the binomial alone is under test; the ceiling's own run-level case is below. Under the
    # example identity's p0 = 1/26 (F5), 2 exceedances of 4 trials fire at P = 0.00843 and 2 of 2 at 0.00148, against
    # alpha 0.01; one of 4 would not (P = 0.145)
    ident4 = dict(ident, identity_bound=10.0, fidelity_rule=dict(ident["fidelity_rule"], cadence=4, ceiling=10.0))
    rep_wb = run(inputs_for("wbinom", backend=fb_w, identity=ident4), wide, resume=False)
    pw = rep_wb["pauses"]
    chk("runner: a binomial fire at a tile's cadence-th read stands on its tile's arms",
        rep_wb["end_state"] == "PAUSE" and len(pw) == 1 and pw[0]["kind"] == "fidelity-binomial"
        and pw[0]["launch_index"] == 3 and pw[0]["arms_in_scope"] == ["N1-P", "N1-V"], pw)
    ruling_wb = tmp / "ruling_wbinom.md"
    ruling_wb.write_text("binomial tile ruling\n")
    rep_wb2 = run(inputs_for("wbinom", backend=fb_w, identity=ident4, rulings={"p01": ruling_wb}), wide, resume=True)
    pw2 = rep_wb2["pauses"]
    b_w2 = pw2[1]["binomial"] if len(pw2) == 2 else None
    chk("runner: after its ruling the tile's fire is reproduced, and the resume's next tile, reads 4-7, fires at "
        "read 7 (a read with no re-computation) on its own two exceedances: its batch (4, 7, 2, 2), on the read's "
        "arm and the tile's",
        rep_wb2["end_state"] == "PAUSE" and len(pw2) == 2 and pw2[0]["adjudicated"]
        and pw2[0]["resumed_at_launch_index"] == 4 and pw2[1]["kind"] == "fidelity-binomial"
        and pw2[1]["launch_index"] == 7 and b_w2 is not None
        and (b_w2["first_launch_index"], b_w2["last_launch_index"], b_w2["k"], b_w2["n"]) == (4, 7, 2, 2)
        and pw2[1]["arms_in_scope"] == ["N1-P", "N1-V", "N2-E"]
        and (rep_wb2["binomial_state"]["evaluations"], rep_wb2["binomial_state"]["fires"]) == (2, 2), pw2)
    sh_be = CausalDouble()
    orig_sh = sh_be.prefill

    def nan_shadow4(ids, injections, capture_layers):
        pre = orig_sh(ids, injections, capture_layers)
        if not injections and list(ids) == toy_ids[4]:
            pre.logits_last = pre.logits_last.copy()
            pre.logits_last[0] = np.float32("nan")
        return pre
    sh_be.prefill = nan_shadow4
    rep_ws = run(inputs_for("wshadow", backend=sh_be), wide, resume=False)
    pws = rep_ws["pauses"]
    chk("runner: a pause on a shadow stands on every arm whose steered reads of that session pair with it",
        rep_ws["end_state"] == "PAUSE" and len(pws) == 1 and pws[0]["launch_index"] == 1
        and pws[0]["arms_in_scope"] == ["N1-P", "N1-V", "N2-E"], pws)

    # a non-finite steered read pauses; a resume needs its ruling, and its next read pauses again
    nan_be = CausalDouble()
    orig = nan_be.prefill

    def nan_prefill(ids, injections, capture_layers):
        pre = orig(ids, injections, capture_layers)
        if injections:
            pre.logits_last = pre.logits_last.copy()
            pre.logits_last[0] = np.float32("nan")
        return pre
    nan_be.prefill = nan_prefill
    rep3 = run(inputs_for("nan", backend=nan_be, load_ms=31), plan, resume=False)     # "nan"'s loads: 31, 32, ...
    p3 = rep3["pauses"]
    chk("runner: a non-finite steered read pauses the invocation, the read on disk",
        rep3["end_state"] == "PAUSE" and len(p3) == 1 and p3[0]["kind"] == "nonfinite" and p3[0]["launch_index"] == 2
        and p3[0]["arms_in_scope"] == ["N1-V"] and obtained(rep3) == 3, p3)
    chk("runner: a resume without the pause's ruling is refused",
        refused(lambda: run(inputs_for("nan", backend=nan_be, load_ms=32), plan, resume=True)), "")
    ruling = tmp / "ruling_p01.md"
    ruling.write_text("a ruling\n")
    rep4 = run(inputs_for("nan", backend=nan_be, rulings={"p01": ruling}, load_ms=33), plan, resume=True)
    p4 = rep4["pauses"]
    chk("runner: after the ruling, p01 is adjudicated, cites the ruling, resumed at the next read; p02 stands",
        [p["pause_id"] for p in p4] == ["p01", "p02"] and p4[0]["adjudicated"]
        and p4[0]["ruling_sha256"] == hashlib.sha256(b"a ruling\n").hexdigest()
        and p4[0]["resumed_at_launch_index"] == 3 and not p4[1]["adjudicated"] and p4[1]["launch_index"] == 3, p4)
    chk("runner: a ruling for no standing pause is refused", refused(lambda: run(
        inputs_for("nan", backend=nan_be, rulings={"p01": ruling, "p02": ruling, "p09": ruling}, load_ms=34), plan,
        resume=True)), "")

    # a rendering mismatch: a pause before the read, not launched; after the ruling the read launches at its place
    bad = {"on": True}

    def ids_render(s, told):
        if bad["on"] and s.bk_run == 4:
            raise RenderingMismatch("toy mismatch")
        return toy_ids[s.bk_run]
    rep5 = run(inputs_for("render", ids_of=ids_render), plan, resume=False)
    p5 = rep5["pauses"]
    chk("runner: a rendering mismatch pauses before its read, which is not launched",
        rep5["end_state"] == "PAUSE" and p5[0]["kind"] == "rendering" and p5[0]["launch_index"] == 1
        and obtained(rep5) == 1 and rep5["counters"]["rendering_mismatches"] == 1, p5)
    bad["on"] = False
    ruling_r = tmp / "ruling_render.md"
    ruling_r.write_text("rendering ruling\n")
    rep6 = run(inputs_for("render", ids_of=ids_render, rulings={"p01": ruling_r}), plan, resume=True)
    chk("runner: after its ruling the read launches at its own place, which is its resumed_at",
        rep6["end_state"] == "COMPLETE" and rep6["pauses"][0]["resumed_at_launch_index"] == 1 and obtained(rep6) == 6,
        rep6["pauses"])

    def ids_tok(s, told):                                   # no RenderingMismatch raised: one token of session 4's
        ids = list(toy_ids[s.bk_run])                       # ids changed, so its ids_sha is not BK's
        if s.bk_run == 4:
            ids[7] = 3 if ids[7] != 3 else 4
        return ids
    try:
        rep_tk = run(inputs_for("tok", ids_of=ids_tok), plan, resume=False)
        ptk = rep_tk["pauses"]
        ok_tk = (rep_tk["end_state"] == "PAUSE" and len(ptk) == 1 and ptk[0]["kind"] == "rendering"
                 and ptk[0]["launch_index"] == 1 and obtained(rep_tk) == 1
                 and rep_tk["counters"]["rendering_mismatches"] == 1)
    except SystemExit as e:
        ok_tk, ptk = False, str(e)[:120]
    chk("runner: ids whose ids_sha is not BK's are a rendering pause before the read, which is not launched",
        ok_tk, ptk)

    # two fidelity exceedances in a tail shorter than a tile: the end-of-run evaluation fires a read-less pause, which
    # its ruling adjudicates (a ruling clears nothing)
    fb_be = CausalDouble()
    orig_full = fb_be.full

    def biased_full(ids, label_ids, injections, capture_layers):     # steered re-computations only: the shadows'
        rows, caps = orig_full(ids, label_ids, injections, capture_layers)   # identity checks stay within bound
        if injections:
            rows = rows.copy()
            rows[:, 9] += np.float32(2.0)
        return rows, caps
    fb_be.full = biased_full
    rep_c = run(inputs_for("ceil", backend=fb_be), plan, resume=False)
    pc = rep_c["pauses"]
    chk("runner: that steered discordance (about 2 nats) under the example ceiling (C = 0.25) pauses at once as "
        "fidelity-ceiling at its read, counted, before any binomial evaluation (ADDENDUM-n2 §2.1)",
        rep_c["end_state"] == "PAUSE" and len(pc) == 1 and pc[0]["kind"] == "fidelity-ceiling"
        and pc[0]["launch_index"] == 2 and pc[0]["binomial"] is None and pc[0]["also_fired"] == []
        and pc[0]["arms_in_scope"] == ["N1-V"]
        and rep_c["counters"]["fidelity_ceiling_exceeded"] == 1 and rep_c["binomial_state"]["evaluations"] == 0, pc)
    ruling_c = tmp / "ruling_ceil.md"
    ruling_c.write_text("ceiling ruling\n")
    rep_c2 = run(inputs_for("ceil", backend=fb_be, rulings={"p01": ruling_c}), plan, resume=True)
    pc2 = rep_c2["pauses"]
    chk("runner: after its ruling the fidelity-ceiling pause is reproduced on replay and adjudicated, and the next "
        "steered re-computation above C pauses again, the counter at 2",
        rep_c2["end_state"] == "PAUSE" and len(pc2) == 2 and pc2[0]["adjudicated"]
        and pc2[0]["resumed_at_launch_index"] == 3 and pc2[1]["kind"] == "fidelity-ceiling"
        and pc2[1]["launch_index"] == 3 and not pc2[1]["adjudicated"]
        and rep_c2["counters"]["fidelity_ceiling_exceeded"] == 2, pc2)
    ident_hi = dict(ident, identity_bound=10.0, fidelity_rule=dict(ident["fidelity_rule"], ceiling=10.0))
    rep7 = run(inputs_for("binom", backend=fb_be, identity=ident_hi), plan, resume=False)
    p7 = rep7["pauses"]
    chk("runner: two exceedances in a tail shorter than a tile (2 of its 4 trials) fire at the run's end, a read-less "
        "pause on the tail's arms",
        rep7["end_state"] == "PAUSE" and len(p7) == 1 and p7[0]["kind"] == "fidelity-binomial"
        and p7[0]["launch_index"] is None and p7[0]["binomial"]["n"] == 4 and obtained(rep7) == 6
        and rep7["binomial_state"]["evaluations"] == 1, p7)
    ruling_b = tmp / "ruling_binom.md"
    ruling_b.write_text("binomial ruling\n")
    rep8 = run(inputs_for("binom", backend=fb_be, identity=ident_hi, rulings={"p01": ruling_b}), plan, resume=True)
    chk("runner: after its ruling the end-of-run fire is reproduced, adjudicated, not re-fired; the stage COMPLETE",
        rep8["end_state"] == "COMPLETE" and len(rep8["pauses"]) == 1 and rep8["pauses"][0]["adjudicated"]
        and rep8["pauses"][0]["resumed_at_launch_index"] is None
        and (rep8["binomial_state"]["evaluations"], rep8["binomial_state"]["fires"]) == (1, 1), rep8["pauses"])

    # an invocation that ends after a read is on disk and before its report: the replay finds the fire and pauses
    ruling2 = tmp / "ruling_p02.md"
    ruling2.write_text("second ruling\n")

    class _Crash(Exception):
        pass

    def crash_on_read_4(line):
        if line.startswith("read 4 "):
            raise _Crash()
    try:
        run(inputs_for("nan", backend=nan_be, rulings={"p02": ruling2}, printer=crash_on_read_4, load_ms=35), plan,
            resume=True)
        crashed = False
    except _Crash:
        crashed = True
    rep9 = run(inputs_for("nan", backend=nan_be, rulings={"p02": ruling2}, load_ms=36), plan, resume=True)
    p9 = rep9["pauses"]
    chk("runner: a fire whose invocation ended before its report is a pause found on replay; nothing launched",
        crashed and rep9["end_state"] == "PAUSE" and [p["pause_id"] for p in p9] == ["p01", "p02", "p03"]
        and p9[2]["launch_index"] == 4 and not p9[2]["adjudicated"] and p9[1]["resumed_at_launch_index"] == 4
        and obtained(rep9) == 5, p9)
    nan_recs = [r for key in sorted({(p.arm, p.direction_id, p.dose_label) for p in plan})
                for r in cells.load_cell(tmp / "nan" / "cells", *key, identity=ident)[0]["records"]]
    chk("runner: loads_ms holds the invocations that wrote a report (three of \"nan\"'s six): one that ended without "
        "one is absent, its records still in used_ms",
        rep9["cap"]["loads_ms"] == [31, 33, 36] and len(nan_recs) == 5
        and rep9["cap"]["used_ms"] == sum(r["duration_ms"] for r in nan_recs), rep9["cap"])

    # a ruling whose resume's first attempt is a rendering refusal: the pause resumed at the refused read's place
    refuse_s4 = {"on": False}

    def ids_nanr(s, told):
        if refuse_s4["on"] and s.bk_run == 4:
            raise RenderingMismatch("toy mismatch")
        return toy_ids[s.bk_run]
    rep13 = run(inputs_for("nanr", backend=nan_be, ids_of=ids_nanr), plan, resume=False)
    refuse_s4["on"] = True
    rep14 = run(inputs_for("nanr", backend=nan_be, ids_of=ids_nanr, rulings={"p01": ruling}), plan, resume=True)
    p14 = rep14["pauses"]
    chk("runner: a resume whose first attempt is refused as a rendering mismatch resumes its pause at that place",
        rep13["pauses"][0]["launch_index"] == 2 and [p["kind"] for p in p14] == ["nonfinite", "rendering"]
        and p14[1]["launch_index"] == 3 and p14[0]["resumed_at_launch_index"] == 3 and obtained(rep14) == 3, p14)

    # the cap: spent before any read, or reached by the last read
    rep10 = run(inputs_for("cap0", cap=0), plan, resume=False)
    chk("runner: a spent cap ends the invocation as CAP before any read, and with no read there is no tail to "
        "evaluate", rep10["end_state"] == "CAP" and obtained(rep10) == 0 and rep10["cap"]["hit"]
        and rep10["binomial_state"]["evaluations"] == 0, (rep10["end_state"], rep10["binomial_state"]))
    total_ms = rep["cap"]["used_ms"]
    chk("runner: the fake clock: 4 reads with a re-computation at 750 ms, 2 without at 250", total_ms == 3500,
        total_ms)
    rep11 = run(inputs_for("cap1", cap=3500), plan, resume=False)
    chk("runner: a cap reached by the last read ends the stage as CAP, its arms complete",
        rep11["end_state"] == "CAP" and rep11["cap"]["hit"] and obtained(rep11) == 6, (rep11["end_state"],
                                                                                     obtained(rep11)))
    rep12 = run(inputs_for("cap2", cap=3250), plan, resume=False)
    chk("runner: a cap spent before the last read ends as CAP, that read not launched",
        rep12["end_state"] == "CAP" and obtained(rep12) == 5 and rep12["cap"]["hit"], obtained(rep12))

    # the tail: reads with no re-computation are still a tail, evaluated at the run's end (Code's reading, for the
    # seat); and the tiles' premise, the records on disk the plan's first reads 0..M-1, asserted before any launch
    ident_c4 = dict(ident, fidelity_rule=dict(ident["fidelity_rule"], cadence=4))
    rep_t = run(inputs_for("tail", identity=ident_c4), plan, resume=False)
    chk("runner: a tail whose reads carry no re-computation (reads 4-5, at +1/2) is evaluated at the run's end: "
        "COMPLETE with two evaluations, the tile 0-3 and the tail, and no fire",
        rep_t["end_state"] == "COMPLETE" and obtained(rep_t) == 6
        and (rep_t["binomial_state"]["evaluations"], rep_t["binomial_state"]["fires"]) == (2, 0),
        rep_t["binomial_state"])
    import shutil
    shutil.copytree(tmp / "ok", tmp / "holes")
    hole = cells.cell_path(tmp / "holes" / "cells", "N1-V", "valence", "+1")
    hole.unlink()                                           # reads 2 and 3 gone: 0, 1, 4 and 5 on disk
    chk("runner: records on disk that are not the plan's first reads, 0..M-1 (reads 2 and 3 missing), are refused "
        "before any launch", refused(lambda: run(inputs_for("holes"), plan, resume=True)) and not hole.exists(), "")
