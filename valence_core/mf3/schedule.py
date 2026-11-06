"""Q-F3's schedules: campaign balance units, gate-stage schedules, the gate-stage launch order and
the six-arm interleave (PROPOSAL-m v1.11 §2.1 m:159-172; §2.4 m:184-192, m:216-243; §3.2 m:293-297).

The CONSTRUCTION is ``valence_core.m.schedule``'s, imported: ``campaign_cells`` (pair x map x start
x clause, clause only where the TOLD line names labels -- A1/A1s; A2-A3s have no clause factor, so
16 cells), the sixteen-row ``GATE_TABLE`` (m:161-170), ``balance_report``, ``cells_sha256``, the
file layout ``dumps_schedule`` and the launch rule ``_n90_launch``. m's ``campaign_schedule``,
``gate_schedule``, ``interleave`` and file writers refuse Q-F3 (they key on keys.UNITS_BUILT), so
the Q-F3 forms are here, keyed by ``mf3.keys``.

FILES under ``data/mf3/schedules/`` with their own ``manifest.json`` -- ``data/m/schedules/`` and
its manifest are untouched (the seat's Q1). Six campaign files (one per arm), six G-TIME-F3 files
(n 1), two G-ID-F3 files (A2s, A3s; sixteen rows available) and six G-F3 files (A1 4, A1s 8, A2 4,
A2s 8, A3 8, A3s 8; m:297): 20 files plus the manifest.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Callable, Iterator, Mapping, Sequence

from valence_core.m import schedule as m_schedule

from . import keys

REPO = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO / "data" / "mf3" / "schedules"
SCHEMA = m_schedule.SCHEMA                      # "m-schedule-v1"
MANIFEST_SCHEMA = m_schedule.MANIFEST_SCHEMA
MANIFEST_NAME = m_schedule.MANIFEST_NAME
CONSTRUCTION = "PROPOSAL-m v1.11 m:159-172 (Q-F3)"
GATE_TABLE = m_schedule.GATE_TABLE
GATE_MAX = m_schedule.GATE_MAX
N_PAIRS = m_schedule.N_PAIRS
balance_report = m_schedule.balance_report
cells_sha256 = m_schedule.cells_sha256
dumps_schedule = m_schedule.dumps_schedule

#: §2.4's balance units (m:184-186): 32 where the clause factor exists, else 16.
UNIT_SIZE = {"A1": 32, "A1s": 32, "A2": 16, "A2s": 16, "A3": 16, "A3s": 16}
#: §2.4's floors (m:184-186), counted in the primary's domain per arm (m:247).
FLOORS = {"A1": {"cached": 96, "uncached": 80}, "A1s": 32, "A2": 144, "A2s": 56, "A3": 144, "A3s": 56}
N_Q = 40                                        # Q-F3's qualification sessions (m:192, m:297)

# PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's materialization PIN carried to Q-F3 -- each campaign
# file holds the k = 1 row of §2.4's launch rule (r = 1/40, the largest L the rule yields above k = 0,
# m:192), so the committed files bound the launches: A1 4352 (136 units of 32; the uncached k = 1 row's
# 3680 is its prefix), A1s 1600 (50), A2 = A3 6384 (399 units of 16), A2s = A3s 2640 (165). The row
# totals are m:228's "1: 24,000" (cached) and m:243's "1: 23,328" (uncached), re-derived in the
# self-test. LOCK-m-F3 v1.0's launch counts are a projection, not a bound (m:192); an arm that needs
# more than its file holds is a schedule-exhausted pause for the PI (Q-F0's PIN, stages).
L_MAX_K1 = {"A1": 4352, "A1s": 1600, "A2": 6384, "A2s": 2640, "A3": 6384, "A3s": 2640}
MAX_UNITS = {a: L_MAX_K1[a] // UNIT_SIZE[a] for a in keys.TEMPLATES}


def _n90_exact(floor: int, k: int, n_q: int = N_Q, unit: int = 16) -> int:
    """§2.4's launch rule, m.schedule._n90_launch's form (L = ceil_unit(max(ceil(1.15 floor),
    N90(k/n_q))), N90 the smallest N with n_q^N >= 10 * sum_{x<floor} C(N,x) k^x (n_q-k)^(N-x)) with
    the binomial terms built by their exact integer recurrence, so the k = 1 rows run in seconds.
    Self-test only; asserted equal to m's on the cases m's own form computes quickly."""
    a, b = k, n_q - k

    def ok(n: int) -> bool:
        if b == 0:
            return n >= floor
        t, s = b ** n, 0
        for x in range(min(floor, n + 1)):
            s += t
            t = t * (n - x) * a // ((x + 1) * b)      # exact: t_{x+1} = t_x (n-x)/(x+1) a/b
        return n_q ** n >= 10 * s

    lo = hi = floor
    while not ok(hi):
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return -(-max((115 * floor + 99) // 100, lo) // unit) * unit


def _l_k1(arm: str, path: str | None = None) -> int:
    fl = FLOORS[arm]
    floors = ([fl[path]] if path else [fl["cached"], fl["uncached"]]) if isinstance(fl, dict) else [fl]
    return max(_n90_exact(f, 1, N_Q, UNIT_SIZE[arm]) for f in floors)

# PIN (Code, declared at LOCK-m-F3 v0.1): the gate-stage plan -- G-TIME-F3 one session per arm
# (m:293); G-ID-F3 the A2s and A3s templates, sixteen rows available each (m:295, "A2s and A3s once
# each"; indices advance as G-ID-F0m's, m:281, so up to sixteen per template); G-F3 the counts of
# m:297, the first m rows of the sixteen-row table (m = 4: the four pairs once each, map, start and
# clause 2/2; m = 8: every pair x map once -- "pairs x maps as evenly as the count allows").
GATE_PLAN = tuple([("time", t, 1) for t in keys.TEMPLATES]
                  + [("id", t, GATE_MAX) for t in keys.GID_TEMPLATES]
                  + [("qual", "A1", 4), ("qual", "A1s", 8), ("qual", "A2", 4), ("qual", "A2s", 8),
                     ("qual", "A3", 8), ("qual", "A3s", 8)])
GATE_PLAN_COUNTS = {(g, t): m for g, t, m in GATE_PLAN}


def roster():
    """Q-F3's roster: Qwen's of record, e2d.config.ROSTER (m:172), as m's schedule reads it."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): Q-F3 is a Qwen unit, so its roster is Q-F0's -- read
    # through valence_core.m.schedule.roster_for("Q-F0"), never re-literalled.
    return m_schedule.roster_for("Q-F0")


def campaign_cells(template: str) -> list[dict]:
    return m_schedule.campaign_cells(roster(), keys.names_labels(template))


def campaign_schedule(arm: str, n_units: int) -> list[dict]:
    """``n_units`` balance units; the b-th a permutation of the cells from
    ``stream(sched_key(arm, b))`` (m:159; m's index form, carried)."""
    if not isinstance(n_units, int) or isinstance(n_units, bool) or n_units < 1:
        raise ValueError(f"n_units must be a positive int, got {n_units!r}")
    cells = campaign_cells(arm)
    if len(cells) != UNIT_SIZE[arm]:
        raise AssertionError(f"{arm}: {len(cells)} cells, balance unit {UNIT_SIZE[arm]}")
    out: list[dict] = []
    for b in range(n_units):
        perm = keys.stream(keys.sched_key(arm, b)).permutation(len(cells))
        out.extend(m_schedule._copy_cell(cells[int(k)]) for k in perm)
    return out


def gate_pi(gate: str, template: str) -> list[int]:
    return [int(x) for x in keys.stream(keys.gate_sched_key(gate, template)).permutation(N_PAIRS)]


def gate_schedule(gate: str, template: str, m: int) -> list[dict]:
    """The first m sessions of a gate-stage template: session j takes pair pi[slot_j] and row j's
    map, start and clause, the clause ignored (None) where the TOLD line names no labels (m:159)."""
    if not isinstance(m, int) or isinstance(m, bool) or not 1 <= m <= GATE_MAX:
        raise ValueError(f"gate-stage m must be an int in 1..{GATE_MAX}, got {m!r}")
    pi = gate_pi(gate, template)
    names = keys.names_labels(template)
    r = roster()
    return [m_schedule._cell(r, pi[slot], mp, st, cl if names else None)
            for (_j, slot, mp, st, cl) in GATE_TABLE[:m]]


def _all_equal(d: Mapping[str, int], want: int) -> bool:
    return all(v == want for v in d.values())


def gate_balance_problems(cells: Sequence[Mapping]) -> list[str]:
    """m:172's claims at m = 4, 8, 16 on a sixteen-row gate schedule. With a clause factor they are
    m's own check; without one (A2-A3s), the same claims over pair, map and start."""
    if len(cells) < GATE_MAX:
        return [f"gate balance needs {GATE_MAX} sessions, got {len(cells)}"]
    if all(c["clause"] is not None for c in cells):
        return m_schedule._gate_balance_problems(cells)
    if any(c["clause"] is not None for c in cells):
        return ["gate balance: cells mix clause None with clause 0/1"]
    probs: list[str] = []
    r4, r8, r16 = (balance_report(cells[:m]) for m in (4, 8, 16))
    if not _all_equal(r4["factors"]["pair"], 1):
        probs.append(f"m=4: pairs not once each {r4['factors']['pair']}")
    for f in ("map", "start"):
        if not _all_equal(r4["factors"][f], 2):
            probs.append(f"m=4: {f} not 2/2 {r4['factors'][f]}")
    if not _all_equal(r8["pairwise"]["pair*map"], 1):
        probs.append(f"m=8: pair x map not once each {r8['pairwise']['pair*map']}")
    if not _all_equal(r8["factors"]["start"], 4):
        probs.append(f"m=8: start not 4/4 {r8['factors']['start']}")
    for pi, w in r8["within_pair"].items():
        if not _all_equal(w["start"], 1):
            probs.append(f"m=8: start not 1/1 within pair {pi}")
    if not _all_equal(r8["pairwise"]["map*start"], 2):
        probs.append(f"m=8: map*start not 2/2/2/2 {r8['pairwise']['map*start']}")
    for cell, w in r16["within_pair_map"].items():
        if w["n"] != 2 or not _all_equal(w["start"], 1):
            probs.append(f"m=16: pair x map cell {cell}: n {w['n']}, start {w['start']}")
    if not _all_equal(r16["pairwise"]["map*start"], 4):
        probs.append(f"m=16: map*start not 4/4/4/4 {r16['pairwise']['map*start']}")
    if r16["duplicates"]:
        probs.append(f"m=16: {r16['duplicates']} duplicate (pair, map, start) rows")
    return probs


# --- launch order and interleave ---------------------------------------------------------
def gate_launch_order(templates_with_counts: Sequence[tuple[str, int]]) -> list[tuple[str, int]]:
    """(template, j) launch list for a multi-template gate stage: strict rotation in §2.4's table
    order, a template leaving the rotation at its count."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's launch-order PIN carried to six templates --
    # the cross-template order is §2.4's table order (A1, A1s, A2, A2s, A3, A3s; G-ID-F3: A2s, A3s);
    # any other order given is refused, not re-sorted; within a template the table's order (m:159).
    names = [t for t, _ in templates_with_counts]
    if not names or len(set(names)) != len(names):
        raise ValueError(f"gate launch order needs distinct templates, got {names}")
    order = [t for t in keys.TEMPLATES if t in names]
    if names != order:
        raise ValueError(f"gate launch order must follow §2.4's table order {order}, got {names}")
    counts = []
    for t, m in templates_with_counts:
        if not isinstance(m, int) or isinstance(m, bool) or not 1 <= m <= GATE_MAX:
            raise ValueError(f"gate-stage count for {t} must be an int in 1..{GATE_MAX}, got {m!r}")
        counts.append(int(m))
    return [(t, j) for j in range(max(counts)) for t, m in zip(names, counts) if j < m]


def interleave(arms_in_order: Sequence[str], done: Callable[[str], bool],
               start_counts: Mapping[str, int] | None = None) -> Iterator[str]:
    """The next arm to launch: strict rotation by launch index in §2.4's order (A1, A1s, A2, A2s,
    A3, A3s), an arm at its floor leaving the rotation for good (m:172); ``done`` evaluated lazily
    before each yield."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's interleave PIN carried to six arms -- next = the
    # live arm with the fewest launches, ties to table order (m.schedule._rotation, imported); the
    # resume counts are validated pairwise exactly as Q-F0's two-arm rule (a precedes b in table
    # order: both live -> b <= a <= b + 1; only a live -> a >= b; only b live -> b >= a - 1).
    arms = list(arms_in_order)
    if tuple(arms) != keys.TEMPLATES:
        raise ValueError(f"interleave arms must be Q-F3's six arms in §2.4's order, got {arms}")
    counts = {a: 0 for a in arms}
    if start_counts is not None:
        if set(start_counts) - set(arms):
            raise ValueError(f"start_counts names arms outside {arms}: {sorted(start_counts)}")
        for a in arms:
            v = start_counts.get(a, 0)
            if not isinstance(v, int) or isinstance(v, bool) or v < 0:
                raise ValueError(f"start count for {a} must be a non-negative int, got {v!r}")
            counts[a] = int(v)
    out_of_rotation = {a for a in arms if done(a)}
    live = [a for a in arms if a not in out_of_rotation]
    for i, a in enumerate(arms):
        for b in arms[i + 1:]:
            if a in live and b in live:
                ok = counts[b] <= counts[a] <= counts[b] + 1
            elif a in live:
                ok = counts[a] >= counts[b]
            elif b in live:
                ok = counts[b] >= counts[a] - 1
            else:
                ok = True
            if not ok:
                raise ValueError(f"interleave: launch counts {counts} are inconsistent with a strict "
                                 f"rotation (out of rotation: {sorted(out_of_rotation)})")
    return m_schedule._rotation(arms, counts, out_of_rotation, done)


# --- files ----------------------------------------------------------------------------------
def schedule_filename(kind: str, template: str) -> str:
    """``Q-F3_campaign_{arm}.json`` or ``Q-F3_{gate}_{template}.json``."""
    if kind == "campaign":
        keys.sched_key(template, 0)
    else:
        keys.gate_sched_key(kind, template)
    return f"{keys.UNIT}_{kind}_{template}.json"


def _session_keys(stage: str, template: str) -> dict[str, str]:
    return {"arm": keys.arm_key(stage, template, "{s}"), "items": keys.item_key("{s}", keys.item_gate(stage))}


def _campaign_obj(arm: str) -> dict:
    n_units = MAX_UNITS[arm]
    cells = campaign_schedule(arm, n_units)
    return {"schema": SCHEMA, "unit": keys.UNIT, "kind": "campaign", "arm": arm, "template": arm,
            "key_template": f"m-sched|{keys.UNIT}|{arm}|{{b}}", "balance_unit": UNIT_SIZE[arm],
            "n_units": n_units, "n": len(cells), "session_keys": _session_keys("campaign", arm),
            "cells": cells, "sha256_of_cells": cells_sha256(cells)}


def _gate_obj(gate: str, template: str, m: int) -> dict:
    cells = gate_schedule(gate, template, m)
    return {"schema": SCHEMA, "unit": keys.UNIT, "kind": "gate", "gate": gate, "template": template,
            "key_template": keys.gate_sched_key(gate, template), "pi": gate_pi(gate, template),
            "table": "m:161-170", "n": len(cells), "session_keys": _session_keys(gate, template),
            "cells": cells, "sha256_of_cells": cells_sha256(cells)}


def build_schedule_objects() -> dict[str, dict]:
    """Every Q-F3 schedule file's content, keyed by file name; every gate schedule's sixteen-row
    form is balance-checked (m:172) and each shorter one asserted its prefix."""
    objs: dict[str, dict] = {}
    for arm in keys.TEMPLATES:
        objs[schedule_filename("campaign", arm)] = _campaign_obj(arm)
    for gate, template, m in GATE_PLAN:
        full = gate_schedule(gate, template, GATE_MAX)
        probs = gate_balance_problems(full)
        if probs:
            raise AssertionError(f"gate schedule {gate}/{template}: {probs}")
        o = _gate_obj(gate, template, m)
        if full[:m] != o["cells"]:
            raise AssertionError(f"gate schedule {gate}/{template} is not a prefix of its sixteen rows")
        objs[schedule_filename(gate, template)] = o
    return objs


def _file_blobs() -> dict[str, bytes]:
    blobs = {name: dumps_schedule(o).encode("utf-8") for name, o in build_schedule_objects().items()}
    # PIN (Code, declared at LOCK-m-F3 v0.1): m's manifest form, its construction line naming Q-F3;
    # nothing machine-specific, so a regeneration anywhere is byte-identical iff the schedules are.
    manifest = {"schema": MANIFEST_SCHEMA, "construction": CONSTRUCTION,
                "files": {n: hashlib.sha256(b).hexdigest() for n, b in sorted(blobs.items())}}
    blobs[MANIFEST_NAME] = (json.dumps(manifest, sort_keys=True, indent=1) + "\n").encode("utf-8")
    return blobs


def write_schedule_files(out_dir: str | os.PathLike | None = None, *, overwrite: bool = False) -> dict[str, str]:
    """Write every Q-F3 schedule file plus manifest.json into out_dir (default
    REPO/data/mf3/schedules); an existing differing file is refused unless overwrite=True."""
    out = Path(out_dir) if out_dir is not None else DEFAULT_OUT
    blobs = _file_blobs()
    clash = [n for n, b in blobs.items() if (out / n).exists() and (out / n).read_bytes() != b]
    if clash and not overwrite:
        raise RuntimeError(f"SCHEDULE MISMATCH: {len(clash)} existing file(s) in {out} differ from the "
                           f"regeneration ({clash[:3]}...); refusing to overwrite")
    out.mkdir(parents=True, exist_ok=True)
    for name, b in blobs.items():
        p = out / name
        if p.exists() and p.read_bytes() == b:
            continue
        tmp = p.with_name(p.name + ".tmp")
        with open(tmp, "wb") as f:
            f.write(b)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, p)
    return {n: hashlib.sha256(b).hexdigest() for n, b in blobs.items()}


def verify_schedule_dir(out_dir: str | os.PathLike | None = None) -> list[str]:
    """Problems ([] = clean): every file present and byte-identical to this machine's regeneration,
    its sha256 the manifest's and its cells' sha its sha256_of_cells; no unlisted file."""
    d = Path(out_dir) if out_dir is not None else DEFAULT_OUT
    blobs = _file_blobs()
    probs: list[str] = []
    for name, b in sorted(blobs.items()):
        p = d / name
        if not p.exists():
            probs.append(f"missing {name}")
        elif p.read_bytes() != b:
            probs.append(f"{name} differs from the regeneration")
    try:
        man = json.loads((d / MANIFEST_NAME).read_text(encoding="utf-8"))
        for name, sha in man.get("files", {}).items():
            p = d / name
            if p.exists():
                if hashlib.sha256(p.read_bytes()).hexdigest() != sha:
                    probs.append(f"{name} sha256 != manifest")
                o = json.loads(p.read_text(encoding="utf-8"))
                if cells_sha256(o["cells"]) != o["sha256_of_cells"]:
                    probs.append(f"{name} cells sha != sha256_of_cells")
    except (OSError, ValueError, KeyError) as e:
        probs.append(f"manifest unreadable: {type(e).__name__}")
    extra = sorted(p.name for p in d.glob("*.json") if p.name not in blobs) if d.exists() else []
    probs += [f"unlisted file {n}" for n in extra]
    return probs


def _selftest(chk) -> None:
    import tempfile

    import numpy as np

    from valence_core.e2d import config as e2d_config

    chk("mf3.schedule: Q-F3's roster is Qwen's of record (e2d.config.ROSTER, via m.schedule)",
        roster() == tuple(tuple(p) for p in e2d_config.ROSTER) and len(roster()) == 4)
    # the launch rule (m:192, m:216-243) re-derived for Q-F3, exact integers
    cross = [((96, 24, 24, 32), None), ((32, 12, 24, 32), None), ((144, 35, 40, 16), None),
             ((56, 30, 40, 16), None), ((96, 31, 40, 32), None), ((144, 24, 40, 16), None)]
    cross = [(c, (m_schedule._n90_launch(c[0], c[1], n_q=c[2], unit=c[3]), _n90_exact(*c))) for c, _ in cross]
    chk("mf3.schedule: the exact-recurrence launch rule equals m.schedule._n90_launch on six cases (Q-F0's "
        "n_q 24 and Q-F3's 40)", all(x == y for _, (x, y) in cross), cross)

    def total(k: int, path: str) -> int:
        return sum(_n90_exact(FLOORS[a][path] if isinstance(FLOORS[a], dict) else FLOORS[a],
                              k, N_Q, UNIT_SIZE[a]) for a in keys.TEMPLATES)
    cached = {40: 704, 35: 704, 34: 736, 32: 736, 31: 800, 30: 832, 29: 864, 28: 864, 27: 896, 26: 896,
              25: 992, 24: 992, 23: 1024, 22: 1120, 21: 1184, 20: 1216, 1: 24000}
    uncached = {40: 672, 35: 672, 34: 736, 32: 736, 31: 768, 30: 800, 29: 832, 28: 832, 27: 864, 26: 896,
                25: 960, 24: 960, 23: 992, 22: 1088, 21: 1152, 20: 1184, 1: 23328}
    got_c = {k: total(k, "cached") for k in cached}
    got_u = {k: total(k, "uncached") for k in uncached}
    chk("mf3.schedule: the launch rule reproduces m:218-228 (cached) and m:232-243 (uncached) row totals, "
        "k = 1 included (24,000 / 23,328)", got_c == cached and got_u == uncached,
        {k: (got_c[k], cached[k]) for k in cached if got_c[k] != cached[k]})
    chk("mf3.schedule: k = 1 materialization (the PIN) -- A1 4352 (136 units; uncached 3680 a prefix), A1s "
        "1600 (50), A2 = A3 6384 (399), A2s = A3s 2640 (165)",
        L_MAX_K1 == {"A1": 4352, "A1s": 1600, "A2": 6384, "A2s": 2640, "A3": 6384, "A3s": 2640}
        and MAX_UNITS == {"A1": 136, "A1s": 50, "A2": 399, "A2s": 165, "A3": 399, "A3s": 165}
        and _l_k1("A1", "uncached") == 3680)
    # campaign construction
    c3 = campaign_schedule("A3", 3)
    c1 = campaign_schedule("A1", 2)
    rep = balance_report(c3[:16])
    chk("mf3.schedule: A3's balance unit is 16 clause-free cells, A1's 32 with clause; each unit balanced; "
        "a prefix is a prefix of whole units (extending changes no earlier cell)",
        len(c3) == 48 and all(c["clause"] is None for c in c3) and len(c1) == 64
        and {c["clause"] for c in c1} == {0, 1} and rep["duplicates"] == 0
        and _all_equal(rep["factors"]["pair"], 4) and campaign_schedule("A3", 2) == c3[:32])
    perm = np.random.default_rng(__import__("zlib").crc32(b"m-sched|Q-F3|A2s|0") % 2**31).permutation(16)
    chk("mf3.schedule: a campaign unit = cells[k] for k in stream('m-sched|Q-F3|{arm}|{b}').permutation, "
        "recomputed independently", campaign_schedule("A2s", 1) == [campaign_cells("A2s")[int(k)] for k in perm])
    # gate schedules and balance
    bal = {(g, t): gate_balance_problems(gate_schedule(g, t, GATE_MAX)) for g, t, _ in GATE_PLAN}
    chk("mf3.schedule: every gate template's sixteen rows meet m:172's balance claims (clause-free form "
        "for A2-A3s)", all(v == [] for v in bal.values()), {k: v[:1] for k, v in bal.items() if v})
    g = gate_schedule("time", "A2", 1)[0]
    chk("mf3.schedule: gate cells -- clause None where the TOLD line names no labels, the table's clause "
        "on A1/A1s; G-TIME-F3 = row j = 0",
        g["clause"] is None and g["map"] == 0 and g["start"] == 0
        and gate_schedule("time", "A1s", 1)[0]["clause"] == 0
        and gate_schedule("qual", "A1", 4)[1]["clause"] == 1)
    broken = [dict(c) for c in gate_schedule("qual", "A3", GATE_MAX)]
    broken[1]["start"] = 1 - broken[1]["start"]
    mixed = [dict(c) for c in gate_schedule("qual", "A3", GATE_MAX)]
    mixed[0]["clause"] = 0
    chk("mf3.schedule: the clause-free balance check fires on a flipped start and on mixed clauses",
        gate_balance_problems(broken) != [] and gate_balance_problems(mixed) != [])
    # launch order and interleave
    lo = gate_launch_order([("A1", 4), ("A1s", 8), ("A2", 4), ("A2s", 8), ("A3", 8), ("A3s", 8)])
    chk("mf3.schedule: G-F3's launch order -- strict rotation in table order, a template leaving at its "
        "count (40 launches)",
        len(lo) == 40 and lo[:6] == [(t, 0) for t in keys.TEMPLATES]
        and lo[24:28] == [("A1s", 4), ("A2s", 4), ("A3", 4), ("A3s", 4)])
    refused = []
    for fn in (lambda: gate_launch_order([("A1s", 1), ("A1", 1)]),
               lambda: gate_launch_order([("A2", 17)]),
               lambda: interleave(["A1", "A1s"], lambda a: False),
               lambda: interleave(list(keys.TEMPLATES), lambda a: False, {"A1": 2}),
               lambda: gate_schedule("id", "A2", 1), lambda: campaign_schedule("A1", 0)):
        try:
            fn()
            refused.append(False)
        except ValueError:
            refused.append(True)
    chk("mf3.schedule: refusals (order out of table order; m > 16; a two-arm interleave; resume counts "
        "inconsistent with a rotation; G-ID on A2; zero units)", all(refused), refused)
    floors = {"A1": 3, "A1s": 1, "A2": 2, "A2s": 1, "A3": 2, "A3s": 1}
    n = {a: 0 for a in keys.TEMPLATES}
    seq = []
    for a in interleave(list(keys.TEMPLATES), lambda a: n[a] >= floors[a]):
        n[a] += 1
        seq.append(a)
    import itertools
    resumed = list(itertools.islice(interleave(list(keys.TEMPLATES), lambda a: False,
                                               {"A1": 1, "A1s": 1, "A2": 1, "A2s": 0, "A3": 0, "A3s": 0}), 5))
    chk("mf3.schedule: the six-arm rotation from zero, arms leaving at their floors; a resume continues "
        "where the rotation stopped",
        seq == ["A1", "A1s", "A2", "A2s", "A3", "A3s", "A1", "A2", "A3", "A1"]
        and resumed == ["A2s", "A3", "A3s", "A1", "A1s"], (seq, resumed))
    # files
    with tempfile.TemporaryDirectory() as td:
        shas = write_schedule_files(td)
        names = sorted(p.name for p in Path(td).iterdir())
        clean = verify_schedule_dir(td)
        (Path(td) / "Q-F3_time_A3.json").write_text("{}")
        dirty = verify_schedule_dir(td)
        (Path(td) / "Q-F3_time_A3.json").write_bytes(_file_blobs()["Q-F3_time_A3.json"])
        (Path(td) / "extra.json").write_text("{}")
        extra = verify_schedule_dir(td)
        try:
            (Path(td) / "Q-F3_time_A1.json").write_text("{}")
            write_schedule_files(td)
            refused_w = False
        except RuntimeError:
            refused_w = True
    chk("mf3.schedule: 20 schedule files + manifest; verify clean, fires on a changed file and an unlisted "
        "one; the writer refuses to overwrite a differing file",
        len(names) == 21 and MANIFEST_NAME in names and clean == [] and dirty and extra == ["unlisted file extra.json"]
        and refused_w and len(shas) == 21, (len(names), clean[:1], dirty[:1], extra))
    objs = build_schedule_objects()
    chk("mf3.schedule: file objects -- campaign n = the k = 1 row; G-TIME n 1 x 6; G-ID A2s/A3s n 16; G-F3 "
        "4/8/4/8/8/8 (m:293-297)",
        {a: objs[f"Q-F3_campaign_{a}.json"]["n"] for a in keys.TEMPLATES} == L_MAX_K1
        and all(objs[f"Q-F3_time_{t}.json"]["n"] == 1 for t in keys.TEMPLATES)
        and [objs[f"Q-F3_id_{t}.json"]["n"] for t in keys.GID_TEMPLATES] == [16, 16]
        and [objs[f"Q-F3_qual_{t}.json"]["n"] for t in keys.TEMPLATES] == [4, 8, 4, 8, 8, 8])
    sp_at, sp_rows = m_schedule._parse_spec_gate_table()
    chk("mf3.schedule: GATE_TABLE is m's, which equals the spec's sixteen rows (m:161-170)",
        GATE_TABLE is m_schedule.GATE_TABLE and sp_rows == list(GATE_TABLE))
