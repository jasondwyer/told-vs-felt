"""PROPOSAL-m schedules: campaign balance units, gate-stage schedules, the
gate-stage launch order and the campaign interleave (v1.11 §2.1, m:159-172;
§2.4, m:188, m:192-214; §3.1, m:280-286; §3.3, m:302).

CAMPAIGN CELLS (m:159). Per arm, the Cartesian product in this fixed order:
roster pair (4, roster order) x map (2; 0 = the pair's first label holds the P
role, 1 = its second) x start (2; 0 = the P-role label's round first, i.e.
P Q P Q; 1 = Q P Q P) x clause (2, only where the arm's TOLD line names
labels; 0 = the first §2.5 variant, 1 = its mirror). Every Q-F0 and OLMo
template names labels (A0, A0s and their OLMo counterparts), so every built
balance unit has 32 cells; the clause-free 16-cell form exists for Q-F3's A2/A3
and is constructible here but not scheduled at step 4. A cell is the dict
``{pair_index, pair, map, start, clause, P, Q}`` with ``P = pair[map]``,
``Q = pair[1 - map]`` (b3's strata convention), Python ints only.

CAMPAIGN SCHEDULE (m:159). The b-th balance unit (b = 0, 1, ...) is a
permutation of the cells drawn from ``stream(f"m-sched|{unit}|{arm}|{b}")``;
each unit has its own key, so a prefix of the schedule is a prefix of whole
balance units and extending it changes no earlier cell (m:159's prefix
property, asserted in the self-test). Materialized to the k = 1 row of §2.4's
launch tables (m:203, m:214) -- the largest launch count the launch rule can
yield -- and committed, hashed: the committed schedules bound the launches (an
arm draws its cells in order and never more than its file holds). LOCK v1.0's
launch counts L are a projection recorded beside them, not a bound (m:192):
``stages.run_campaign`` launches each arm until its DOMAIN count reaches its
floor, the hour cap, a PI stop, or the end of its committed schedule (a PAUSE
for the PI). The laptop runs numpy 2.5.1 and the box's provenance records
2.1.2 (e.g. data/olmo/b3_screen_base.json), so both runners load the committed
file and ``verify_schedule_dir`` asserts their regeneration matches it.

GATE-STAGE SCHEDULE (m:159, table m:161-170). One ``permutation(4)`` of the
roster pairs, pi, from ``stream(f"m-sched|{unit}|{gate}|{template}|0")``; the
j-th session of the template takes pair pi[slot_j] and row j's map, start and
clause. m:172's balance claims at m = 4, 8, 16 are verified by
``assert_gate_balance`` at the schedule build (and in the self-test, on the
table and on every materialized gate schedule).

LAUNCH ORDER. Within a gate-stage template the order is the table's; across
templates it is a strict rotation in §2.4's table order, contrast first
(build pin 3, ``gate_launch_order``). The campaign interleave (m:172) is the
same strict rotation by launch index, an arm at its floor leaving the
rotation (``interleave``).

Rosters: Qwen ``e2d.config.ROSTER`` (imported, not re-literalled); OLMo
``data/olmo/a1_repair_roster.json["selected_tags"]`` (m:172). Nothing here is
pick-bearing; a schedule names labels, never outcomes.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from math import comb
from pathlib import Path
from typing import Callable, Iterator, Mapping, Sequence

import numpy as np

from valence_core.e2d import config as _e2d_config
from valence_core.m import keys

REPO = Path(__file__).resolve().parents[2]
SPEC_PATH = REPO / "PROPOSAL-m-gating-campaign-v1_11.md"
OLMO_ROSTER_PATH = REPO / "data" / "olmo" / "a1_repair_roster.json"
DEFAULT_OUT = REPO / "data" / "m" / "schedules"

SCHEMA = "m-schedule-v1"
MANIFEST_SCHEMA = "m-schedules-manifest-v1"
MANIFEST_NAME = "manifest.json"

UNIT_SIZE = 32          # §2.4's balance unit for A0/A0s and the OLMo arms (m:182-183)
N_PAIRS = 4             # gate-stage pi is a permutation(4) of the roster pairs (m:159)
GATE_MAX = 16           # sixteen rows, m:161-170

#: The sixteen rows of m:161-170, verbatim: (j, slot, map, start, clause).
#: The self-test re-parses the table from the spec file and asserts equality.
GATE_TABLE: tuple[tuple[int, int, int, int, int], ...] = (
    (0, 0, 0, 0, 0),
    (1, 1, 1, 0, 1),
    (2, 2, 0, 1, 1),
    (3, 3, 1, 1, 0),
    (4, 0, 1, 1, 1),
    (5, 1, 0, 1, 0),
    (6, 2, 1, 0, 0),
    (7, 3, 0, 0, 1),
    (8, 0, 1, 0, 0),
    (9, 1, 0, 0, 1),
    (10, 2, 1, 1, 1),
    (11, 3, 0, 1, 0),
    (12, 0, 0, 1, 1),
    (13, 1, 1, 1, 0),
    (14, 2, 0, 0, 0),
    (15, 3, 1, 0, 1),
)

#: §2.4's floors (m:182-183): Q-F0 A0 96 cached / 80 uncached, A0s 32; OLMo
#: A0-OLMo 80 (uncached, m:267), A0s-OLMo 32.
FLOORS = {"A0": {"cached": 96, "uncached": 80}, "A0s": 32, "A0-OLMo": 80, "A0s-OLMo": 32}
N_Q = 24                # qualification sessions per unit, Q-F0 and each OLMo ckpt (m:192)

# PIN (Code, declared at LOCK v0.1): the campaign schedule is materialized to
# the k = 1 row of §2.4's launch tables (r = 1/24, the largest L the launch rule
# yields above k = 0): Q-F0 cached A0 2624 (82 units), Q-F0 uncached and OLMo
# A0 2208 (69 units), every sham 960 (30 units); the row totals are m:203's
# "1: 3,584" and m:214's "1: 3,168". Q-F0's A0 file carries 82 units, which
# covers both paths (the uncached k = 1 row's 69 is its prefix). The committed
# files bound the launches -- a campaign draws at most a file's n cells, on
# either path; LOCK v1.0's launch counts L are a projection, not a bound
# (m:192): stages.run_campaign launches each arm until its DOMAIN count reaches
# its floor, the hour cap, a PI stop, or the schedule's end (a PAUSE for the
# PI). The self-test re-derives each L from the launch rule in exact integer
# arithmetic.
L_MAX_K1 = {("Q-F0", "A0", "cached"): 2624, ("Q-F0", "A0", "uncached"): 2208,
            ("Q-F0", "A0s", None): 960, ("OLMo", "A0-OLMo", None): 2208,
            ("OLMo", "A0s-OLMo", None): 960}


def _ceil_div(a: int, b: int) -> int:
    return -(-a // b)


def _arm_family(arm: str) -> str:
    """'A0' | 'A0s' | 'A0-OLMo' | 'A0s-OLMo' (raises outside Q-F0/OLMo)."""
    contrast = keys.is_contrast(arm)
    if arm in ("A0", "A0s"):
        return arm
    return "A0-OLMo" if contrast else "A0s-OLMo"


def max_units(unit: str, arm: str) -> int:
    """Balance units materialized per arm (the PIN above)."""
    keys.sched_key(unit, arm, 0)          # validates unit and arm together
    fam = _arm_family(arm)
    if unit == "Q-F0":
        L = L_MAX_K1[("Q-F0", "A0", "cached")] if fam == "A0" else L_MAX_K1[("Q-F0", "A0s", None)]
    else:
        L = L_MAX_K1[("OLMo", fam, None)]
    return _ceil_div(L, UNIT_SIZE)


MAX_UNITS = {(u, a): max_units(u, a) for u in keys.UNITS_BUILT for a in keys.templates(u)}


# --- rosters ------------------------------------------------------------------
_OLMO_ROSTER_CACHE: tuple[tuple[str, str], ...] | None = None


def _norm_roster(roster: Sequence[Sequence[str]]) -> tuple[tuple[str, str], ...]:
    if any(len(p) != 2 for p in roster):
        raise ValueError("roster pairs must have exactly two labels")
    out = tuple((str(p[0]), str(p[1])) for p in roster)
    labels = [t for p in out for t in p]
    if len(set(labels)) != len(labels):
        raise ValueError(f"roster labels must be distinct: {labels}")
    return out


def olmo_roster() -> tuple[tuple[str, str], ...]:
    """OLMo roster of record (m:172). Replicates corr.olmo_roster's load (that
    module is built in parallel; the two are compared at the driver's
    integration self-test)."""
    global _OLMO_ROSTER_CACHE
    if _OLMO_ROSTER_CACHE is None:
        with open(OLMO_ROSTER_PATH, encoding="utf-8") as f:
            tags = json.load(f)["selected_tags"]
        r = _norm_roster(tags)
        if len(r) != N_PAIRS:
            raise ValueError(f"OLMo roster must have {N_PAIRS} pairs, got {len(r)}")
        _OLMO_ROSTER_CACHE = r
    return _OLMO_ROSTER_CACHE


def roster_for(unit: str) -> tuple[tuple[str, str], ...]:
    keys.templates(unit)                  # validates the unit (refuses Q-F3, base)
    if unit == "Q-F0":
        return _norm_roster(_e2d_config.ROSTER)
    return olmo_roster()


def _check_roster(unit: str, roster: Sequence[Sequence[str]]) -> tuple[tuple[str, str], ...]:
    # PIN (Code, declared at LOCK v0.1): a schedule is built only on its unit's
    # roster of record (Qwen e2d.config.ROSTER; OLMo a1_repair_roster.json); any
    # other roster is refused, so a Qwen roster can never key an OLMo schedule.
    r = _norm_roster(roster)
    if r != roster_for(unit):
        raise ValueError(f"roster {r} is not the roster of record for {unit!r}")
    return r


def _names_labels(template: str) -> bool:
    """m:159: the clause factor exists only where the TOLD line names labels --
    A0, A0s, A1, A1s and their OLMo counterparts. Only Q-F0/OLMo are built."""
    keys.is_contrast(template)            # raises outside the built templates
    return True


# --- cells and campaign schedules ---------------------------------------------
def _cell(roster: tuple[tuple[str, str], ...], pi: int, mp: int, st: int,
          cl: int | None) -> dict:
    pair = roster[pi]
    return {"pair_index": int(pi), "pair": [pair[0], pair[1]], "map": int(mp),
            "start": int(st), "clause": None if cl is None else int(cl),
            "P": pair[mp], "Q": pair[1 - mp]}


def campaign_cells(roster: Sequence[Sequence[str]], names_labels: bool) -> list[dict]:
    """One balance unit's cells in m:159's fixed product order: pair (roster
    order) x map x start x clause (clause only where the TOLD line names labels;
    else clause None and 16 cells)."""
    r = _norm_roster(roster)
    clauses: tuple[int | None, ...] = (0, 1) if names_labels else (None,)
    return [_cell(r, pi, mp, st, cl)
            for pi in range(len(r)) for mp in (0, 1) for st in (0, 1) for cl in clauses]


def campaign_schedule(unit: str, arm: str, roster: Sequence[Sequence[str]],
                      n_units: int) -> list[dict]:
    """``n_units`` balance units; the b-th is a permutation of the cells drawn
    from ``stream(sched_key(unit, arm, b))``."""
    r = _check_roster(unit, roster)
    if not isinstance(n_units, int) or isinstance(n_units, bool) or n_units < 1:
        raise ValueError(f"n_units must be a positive int, got {n_units!r}")
    cells = campaign_cells(r, _names_labels(arm))
    out: list[dict] = []
    for b in range(n_units):
        # PIN (Code, declared at LOCK v0.1): m:159's "permutation(cells)" is
        # taken in index form, cells[k] for k in rng.permutation(len(cells));
        # the self-test shows it equals the object-array permutation on this numpy.
        perm = keys.stream(keys.sched_key(unit, arm, b)).permutation(len(cells))
        out.extend(_copy_cell(cells[int(k)]) for k in perm)
    return out


def _copy_cell(c: Mapping) -> dict:
    d = dict(c)
    d["pair"] = list(c["pair"])
    return d


# --- gate-stage schedules -----------------------------------------------------
def gate_pi(unit: str, gate: str, template: str) -> list[int]:
    """pi: one permutation(4) of the roster pairs (m:159)."""
    return [int(x) for x in keys.stream(keys.gate_sched_key(unit, gate, template)).permutation(N_PAIRS)]


def gate_schedule(unit: str, gate: str, template: str, roster: Sequence[Sequence[str]],
                  m: int) -> list[dict]:
    """The first m sessions of a gate-stage template: session j takes pair
    pi[slot_j] and row j's map, start and clause (m:159, m:161-170)."""
    r = _check_roster(unit, roster)
    if len(r) != N_PAIRS:
        raise ValueError(f"gate schedules need {N_PAIRS} roster pairs, got {len(r)}")
    if gate == "id" and template != "A0s":
        raise ValueError("G-ID-F0m runs the A0s template only (m:281)")
    # PIN (Code, declared at LOCK v0.1): no row beyond j = 15; a gate stage that
    # would need a seventeenth session (G-ID past sixteen indices) STOPs.
    if not isinstance(m, int) or isinstance(m, bool) or not 1 <= m <= GATE_MAX:
        raise ValueError(f"gate-stage m must be an int in 1..{GATE_MAX}, got {m!r}")
    pi = gate_pi(unit, gate, template)
    names = _names_labels(template)
    return [_cell(r, pi[slot], mp, st, cl if names else None)
            for (_j, slot, mp, st, cl) in GATE_TABLE[:m]]


# --- balance ------------------------------------------------------------------
def _levels(cells: Sequence[Mapping], n_pairs: int) -> dict[str, tuple]:
    cls = {c["clause"] for c in cells}
    if None in cls and len(cls) > 1:
        raise ValueError("cells mix clause None with clause 0/1")
    lv: dict[str, tuple] = {"pair": tuple(range(n_pairs)), "map": (0, 1), "start": (0, 1)}
    if None not in cls:
        lv["clause"] = (0, 1)
    return lv


def _count(cells: Sequence[Mapping], fs: Sequence[str], lv: Mapping[str, tuple]) -> dict[str, int]:
    out = {",".join(str(x) for x in combo): 0
           for combo in itertools.product(*(lv[f] for f in fs))}
    for c in cells:
        out[",".join(str(c[f if f != "pair" else "pair_index"]) for f in fs)] += 1
    return out


def balance_report(cells: Sequence[Mapping], n_pairs: int = N_PAIRS) -> dict:
    """Counts per factor, pairwise, within pair and within pair x map, plus the
    number of duplicate (pair, map, start, clause) cells. JSON-ready (string
    keys, Python ints); every level is listed, zeros included."""
    lv = _levels(cells, n_pairs)
    fs = list(lv)
    rep: dict = {"n": len(cells), "factors": {f: _count(cells, [f], lv) for f in fs},
                 "pairwise": {}, "within_pair": {}, "within_pair_map": {}}
    for i, a in enumerate(fs):
        for b in fs[i + 1:]:
            rep["pairwise"][f"{a}*{b}"] = _count(cells, [a, b], lv)
    inner = [f for f in fs if f not in ("pair",)]
    for pi in lv["pair"]:
        sub = [c for c in cells if c["pair_index"] == pi]
        rep["within_pair"][str(pi)] = {f: _count(sub, [f], lv) for f in inner}
        for mp in (0, 1):
            sub2 = [c for c in sub if c["map"] == mp]
            rep["within_pair_map"][f"{pi},{mp}"] = {
                "n": len(sub2), **{f: _count(sub2, [f], lv) for f in inner if f != "map"}}
    seen: dict[tuple, int] = {}
    for c in cells:
        t = (c["pair_index"], c["map"], c["start"], c["clause"])
        seen[t] = seen.get(t, 0) + 1
    rep["duplicates"] = sum(v - 1 for v in seen.values())
    return rep


def _all_equal(d: Mapping[str, int], want: int) -> bool:
    return all(v == want for v in d.values())


def _gate_balance_problems(cells: Sequence[Mapping]) -> list[str]:
    """m:172's claims, checked on the m = 4, 8 and 16 prefixes."""
    probs: list[str] = []
    if len(cells) < GATE_MAX:
        return [f"gate balance needs {GATE_MAX} sessions, got {len(cells)}"]
    r4, r8, r16 = (balance_report(cells[:m]) for m in (4, 8, 16))
    if "clause" not in r16["factors"]:
        probs.append("gate balance: clause factor absent (every built template names labels)")
        return probs
    # m = 4: the four pairs once each; map, start and clause 2/2.
    if not _all_equal(r4["factors"]["pair"], 1):
        probs.append(f"m=4: pairs not once each {r4['factors']['pair']}")
    for f in ("map", "start", "clause"):
        if not _all_equal(r4["factors"][f], 2):
            probs.append(f"m=4: {f} not 2/2 {r4['factors'][f]}")
    # m = 8: every pair x map once; start and clause 4/4 overall and 1/1 within
    # each pair; map, start, clause each balanced 2/2/2/2 against the other two.
    if not _all_equal(r8["pairwise"]["pair*map"], 1):
        probs.append(f"m=8: pair x map not once each {r8['pairwise']['pair*map']}")
    for f in ("start", "clause"):
        if not _all_equal(r8["factors"][f], 4):
            probs.append(f"m=8: {f} not 4/4 {r8['factors'][f]}")
        for pi, w in r8["within_pair"].items():
            if not _all_equal(w[f], 1):
                probs.append(f"m=8: {f} not 1/1 within pair {pi} {w[f]}")
    for pw in ("map*start", "map*clause", "start*clause"):
        if not _all_equal(r8["pairwise"][pw], 2):
            probs.append(f"m=8: {pw} not 2/2/2/2 {r8['pairwise'][pw]}")
    # m = 16: two sessions per pair x map cell, start and clause 1/1 within every
    # cell, and all three pairwise balances held (4/4/4/4).
    for cell, w in r16["within_pair_map"].items():
        if w["n"] != 2:
            probs.append(f"m=16: pair x map cell {cell} has {w['n']} sessions, not 2")
        for f in ("start", "clause"):
            if not _all_equal(w[f], 1):
                probs.append(f"m=16: {f} not 1/1 within pair x map cell {cell} {w[f]}")
    for pw in ("map*start", "map*clause", "start*clause"):
        if not _all_equal(r16["pairwise"][pw], 4):
            probs.append(f"m=16: {pw} not 4/4/4/4 {r16['pairwise'][pw]}")
    if r16["duplicates"]:
        probs.append(f"m=16: {r16['duplicates']} duplicate (pair, map, start, clause) rows")
    return probs


def _table_cells() -> list[dict]:
    """GATE_TABLE as pseudo-cells, slot standing for the pair (balance in pair
    terms is invariant under pi, a relabelling of slots)."""
    r = tuple((f"s{k}a", f"s{k}b") for k in range(N_PAIRS))
    return [_cell(r, slot, mp, st, cl) for (_j, slot, mp, st, cl) in GATE_TABLE]


def assert_gate_balance(cells: Sequence[Mapping] | None = None) -> dict:
    """Verify m:172's balance claims at m = 4, 8, 16 (and no duplicate
    (slot, map, start, clause) rows) on the table itself (cells None) or on a
    materialized 16-session gate schedule. Raises AssertionError listing every
    failed claim; returns the three balance reports on success."""
    cs = _table_cells() if cells is None else list(cells)
    if cells is None:
        js = [row[0] for row in GATE_TABLE]
        if js != list(range(GATE_MAX)):
            raise AssertionError(f"GATE_TABLE j column is not 0..15: {js}")
    probs = _gate_balance_problems(cs)
    if probs:
        raise AssertionError("gate-stage balance (m:172) fails: " + "; ".join(probs))
    return {f"m={m}": balance_report(cs[:m]) for m in (4, 8, 16)}


# --- launch order and interleave ----------------------------------------------
def _unit_of_templates(names: Sequence[str]) -> str:
    for u in keys.UNITS_BUILT:
        if all(t in keys.templates(u) for t in names):
            return u
    raise ValueError(f"templates {list(names)} do not belong to one built unit")


def gate_launch_order(templates_with_counts: Sequence[tuple[str, int]]) -> list[tuple[str, int]]:
    """(template, j) launch list for a multi-template gate stage: strict
    rotation in the order given, a template leaving the rotation at its count
    (build pin 3)."""
    names = [t for t, _ in templates_with_counts]
    if not names or len(set(names)) != len(names):
        raise ValueError(f"gate launch order needs distinct templates, got {names}")
    unit = _unit_of_templates(names)
    # PIN (Code, declared at LOCK v0.1): the cross-template order is §2.4's
    # table order, contrast template first (A0 then A0s; A0-OLMo-{ckpt} then
    # A0s-OLMo-{ckpt}); any other order given is refused, not re-sorted.
    order = [t for t in keys.templates(unit) if t in names]
    if names != order:
        raise ValueError(f"gate launch order must follow §2.4's table order {order}, got {names}")
    counts = []
    for t, m in templates_with_counts:
        if not isinstance(m, int) or isinstance(m, bool) or not 1 <= m <= GATE_MAX:
            raise ValueError(f"gate-stage count for {t} must be an int in 1..{GATE_MAX}, got {m!r}")
        counts.append(int(m))
    out: list[tuple[str, int]] = []
    for j in range(max(counts)):
        for t, m in zip(names, counts):
            if j < m:
                out.append((t, j))
    return out


def interleave(arms_in_order: Sequence[str], done: Callable[[str], bool],
               start_counts: Mapping[str, int] | None = None) -> Iterator[str]:
    """Yield the next arm to launch: strict rotation by launch index in §2.4's
    order (A0, A0s; A0-OLMo-{ckpt}, A0s-OLMo-{ckpt}), an arm that has reached its
    floor leaving the rotation for good (m:172). ``done(arm)`` is evaluated
    lazily, immediately before each yield, so the caller launches the yielded
    arm and updates its floor count before asking for the next."""
    arms = list(arms_in_order)
    unit = _unit_of_templates(arms) if arms else None
    if unit is None or tuple(arms) != keys.templates(unit):
        raise ValueError(f"interleave arms must be a unit's two arms in §2.4's order, got {arms}")
    # PIN (Code, declared at LOCK v0.1): "strict rotation by launch index" is
    # implemented as: next = the live arm with the fewest launches, ties to
    # table order. From zero this is A0, A0s, A0, A0s, ...; on resume the
    # caller passes the on-disk launch counts and the rotation continues where
    # it stopped. Counts inconsistent with a strict rotation are refused.
    counts = {a: 0 for a in arms}
    if start_counts is not None:
        if set(start_counts) - set(arms):
            raise ValueError(f"start_counts names arms outside {arms}: {sorted(start_counts)}")
        for a in arms:
            v = start_counts.get(a, 0)
            if not isinstance(v, int) or isinstance(v, bool) or v < 0:
                raise ValueError(f"start count for {a} must be a non-negative int, got {v!r}")
            counts[a] = int(v)
    out_of_rotation: set[str] = set()
    for a in arms:
        if done(a):
            out_of_rotation.add(a)
    live = [a for a in arms if a not in out_of_rotation]
    for i, a in enumerate(arms):
        for b in arms[i + 1:]:
            # a precedes b in table order: while both were live a led by at most
            # one and never trailed; after one left, only the live one grew.
            ok = True
            if a in live and b in live:
                ok = counts[b] <= counts[a] <= counts[b] + 1
            elif a in live:
                ok = counts[a] >= counts[b]
            elif b in live:
                ok = counts[b] >= counts[a] - 1
            if not ok:
                raise ValueError(f"interleave: launch counts {counts} are inconsistent with a "
                                 f"strict rotation (out of rotation: {sorted(out_of_rotation)})")
    # Validation above runs eagerly (a bad order or resume state is refused at
    # the call, not at the first launch); the rotation itself is lazy.
    return _rotation(arms, counts, out_of_rotation, done)


def _rotation(arms: list[str], counts: dict[str, int], out_of_rotation: set[str],
              done: Callable[[str], bool]) -> Iterator[str]:
    while True:
        for a in arms:
            if a not in out_of_rotation and done(a):
                out_of_rotation.add(a)
        live = [a for a in arms if a not in out_of_rotation]
        if not live:
            return
        nxt = min(live, key=lambda a: (counts[a], arms.index(a)))
        counts[nxt] += 1
        yield nxt


# --- schedule files -----------------------------------------------------------
def cells_sha256(cells: Sequence[Mapping]) -> str:
    """sha256 hex of the cells' canonical JSON (compact, sort-keyed)."""
    # PIN (Code, declared at LOCK v0.1): sha256_of_cells is computed over
    # json.dumps(cells, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    # encoded UTF-8 -- independent of the file's layout.
    blob = json.dumps(list(cells), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def schedule_filename(unit: str, kind: str, template: str) -> str:
    """``{unit}_campaign_{arm}.json`` or ``{unit}_{gate}_{template}.json``."""
    # PIN (Code, declared at LOCK v0.1): file names as above, under
    # data/m/schedules/, plus manifest.json.
    if kind != "campaign":
        keys.gate_sched_key(unit, kind, template)
    else:
        keys.sched_key(unit, template, 0)
    return f"{unit}_{kind}_{template}.json"


def _session_key_templates(unit: str, stage: str, template: str) -> dict[str, str]:
    # keys' builders format s with an f-string, so the literal "{s}" renders the template
    return {"arm": keys.arm_key(unit, stage, template, "{s}"),  # type: ignore[arg-type]
            "items": keys.item_key(unit, "{s}", keys.item_gate(stage))}  # type: ignore[arg-type]


def _campaign_obj(unit: str, arm: str) -> dict:
    n_units = MAX_UNITS[(unit, arm)]
    cells = campaign_schedule(unit, arm, roster_for(unit), n_units)
    return {"schema": SCHEMA, "unit": unit, "kind": "campaign", "arm": arm, "template": arm,
            "key_template": f"m-sched|{unit}|{arm}|{{b}}", "balance_unit": UNIT_SIZE,
            "n_units": n_units, "n": len(cells),
            "session_keys": _session_key_templates(unit, "campaign", arm),
            "cells": cells, "sha256_of_cells": cells_sha256(cells)}


def _gate_obj(unit: str, gate: str, template: str, m: int) -> dict:
    cells = gate_schedule(unit, gate, template, roster_for(unit), m)
    return {"schema": SCHEMA, "unit": unit, "kind": "gate", "gate": gate, "template": template,
            "key_template": keys.gate_sched_key(unit, gate, template),
            "pi": gate_pi(unit, gate, template), "table": "m:161-170", "n": len(cells),
            "session_keys": _session_key_templates(unit, gate, template),
            "cells": cells, "sha256_of_cells": cells_sha256(cells)}


def _gate_plan(unit: str) -> list[tuple[str, str, int]]:
    """(gate, template, m) per unit: G-TIME one session per arm (m:280, m:302);
    G-ID-F0m the A0s template, sixteen rows available (m:281); qualification
    8 contrast + 16 sham (m:283, m:302)."""
    c, s = keys.templates(unit)
    plan = [("time", c, 1), ("time", s, 1)]
    if unit == "Q-F0":
        plan.append(("id", s, GATE_MAX))
    plan += [("qual", c, 8), ("qual", s, 16)]
    return plan


def build_schedule_objects() -> dict[str, dict]:
    """Every schedule file's content, in memory, keyed by file name."""
    objs: dict[str, dict] = {}
    for unit in keys.UNITS_BUILT:
        for arm in keys.templates(unit):
            objs[schedule_filename(unit, "campaign", arm)] = _campaign_obj(unit, arm)
        for gate, template, m in _gate_plan(unit):
            o = _gate_obj(unit, gate, template, m)
            if m == GATE_MAX:
                assert_gate_balance(o["cells"])
            elif m >= 4:
                # 8-session prefixes: the m = 4 and m = 8 claims of m:172, on the
                # materialized cells (the full schedule is checked at 16 below).
                full = gate_schedule(unit, gate, template, roster_for(unit), GATE_MAX)
                assert_gate_balance(full)
                if full[:m] != o["cells"]:
                    raise AssertionError(f"gate schedule {unit}/{gate}/{template} is not a prefix")
            objs[schedule_filename(unit, gate, template)] = o
    return objs


def dumps_schedule(obj: Mapping) -> str:
    """Deterministic layout: sort-keyed, one cell per line (readable diffs)."""
    items = sorted(obj.items())
    lines = ["{"]
    for i, (k, v) in enumerate(items):
        comma = "," if i < len(items) - 1 else ""
        if k == "cells":
            lines.append(f" {json.dumps(k)}: [")
            for ci, c in enumerate(v):
                tail = "," if ci < len(v) - 1 else ""
                lines.append("  " + json.dumps(c, sort_keys=True, ensure_ascii=False) + tail)
            lines.append(" ]" + comma)
        else:
            lines.append(f" {json.dumps(k)}: {json.dumps(v, sort_keys=True, ensure_ascii=False)}{comma}")
    lines.append("}")
    return "\n".join(lines) + "\n"


def _file_blobs() -> dict[str, bytes]:
    blobs = {name: dumps_schedule(o).encode("utf-8") for name, o in build_schedule_objects().items()}
    # PIN (Code, declared at LOCK v0.1): the manifest records each file's
    # sha256 (of its bytes) and nothing machine-specific (no numpy version, no
    # time), so a regeneration on the box is byte-identical iff the schedules are.
    manifest = {"schema": MANIFEST_SCHEMA, "construction": "PROPOSAL-m v1.11 m:159-172",
                "files": {n: hashlib.sha256(b).hexdigest() for n, b in sorted(blobs.items())}}
    blobs[MANIFEST_NAME] = (json.dumps(manifest, sort_keys=True, indent=1) + "\n").encode("utf-8")
    return blobs


def write_schedule_files(out_dir: str | os.PathLike | None = None, *,
                         overwrite: bool = False) -> dict[str, str]:
    """Write every Q-F0 and OLMo schedule file plus manifest.json into out_dir
    (default REPO/data/m/schedules). Returns {file name: sha256 of its bytes}."""
    out = Path(out_dir) if out_dir is not None else DEFAULT_OUT
    blobs = _file_blobs()
    # PIN (Code, declared at LOCK v0.1): an existing file whose bytes differ is a
    # schedule change and is refused unless overwrite=True; identical files are
    # left untouched.
    clash = []
    for name, b in blobs.items():
        p = out / name
        if p.exists() and p.read_bytes() != b:
            clash.append(name)
    if clash and not overwrite:
        raise RuntimeError(f"SCHEDULE MISMATCH: {len(clash)} existing file(s) in {out} differ "
                           f"from the regeneration ({clash[:3]}...); refusing to overwrite")
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
    """Problems ([] = clean): every file present, byte-identical to this
    machine's regeneration, its sha256 in the manifest, and its cells' sha
    matching sha256_of_cells; no unlisted schedule file."""
    d = Path(out_dir) if out_dir is not None else DEFAULT_OUT
    blobs = _file_blobs()
    probs: list[str] = []
    for name, b in sorted(blobs.items()):
        p = d / name
        if not p.exists():
            probs.append(f"missing {name}")
            continue
        got = p.read_bytes()
        if got != b:
            probs.append(f"{name} differs from the regeneration")
    try:
        man = json.loads((d / MANIFEST_NAME).read_text(encoding="utf-8"))
        for name, sha in man.get("files", {}).items():
            p = d / name
            if p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() != sha:
                probs.append(f"{name} sha256 != manifest")
            if p.exists():
                o = json.loads(p.read_text(encoding="utf-8"))
                if cells_sha256(o["cells"]) != o["sha256_of_cells"]:
                    probs.append(f"{name} cells sha != sha256_of_cells")
    except (OSError, ValueError, KeyError) as e:
        probs.append(f"manifest unreadable: {type(e).__name__}")
    extra = sorted(p.name for p in d.glob("*.json") if p.name not in blobs) if d.exists() else []
    probs += [f"unlisted file {n}" for n in extra]
    return probs


# --- self-test helpers --------------------------------------------------------
def _parse_spec_gate_table(path: Path = SPEC_PATH) -> tuple[int, list[tuple[int, ...]]]:
    """(1-based header line, rows sorted by j) parsed from the spec's table."""
    lines = path.read_text(encoding="utf-8").splitlines()
    hdr = "| j | slot | map | start | clause | j | slot | map | start | clause |"
    at = lines.index(hdr)
    rows: list[tuple[int, ...]] = []
    for ln in lines[at + 2: at + 10]:
        nums = [int(x) for x in ln.strip().strip("|").split("|")]
        if len(nums) != 10:
            raise ValueError(f"spec gate-table row malformed: {ln!r}")
        rows.append(tuple(nums[:5]))
        rows.append(tuple(nums[5:]))
    return at + 1, sorted(rows)


def _n90_launch(floor: int, k: int, n_q: int = N_Q, unit: int = UNIT_SIZE) -> int:
    """§2.4's launch rule in exact integers: L = ceil_unit(max(ceil(1.15 floor),
    N90(k/n_q))), N90 the smallest N with P(Bin(N, k/n_q) >= floor) >= .90."""
    def ok(n: int) -> bool:     # n_q^N >= 10 * sum_{x<floor} C(N,x) k^x (n_q-k)^(N-x)
        lo = sum(comb(n, x) * k**x * (n_q - k)**(n - x) for x in range(min(floor, n + 1)))
        return n_q**n >= 10 * lo
    lo = hi = floor
    while not ok(hi):
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return _ceil_div(max((115 * floor + 99) // 100, lo), unit) * unit


def _only_ints(cells: Sequence[Mapping]) -> bool:
    for c in cells:
        for f in ("pair_index", "map", "start", "clause"):
            if type(c[f]) is not int:
                return False
        if not (type(c["P"]) is str and type(c["Q"]) is str and type(c["pair"]) is list):
            return False
    return True


def _refuses(fn: Callable[[], object], exc: type | tuple = (ValueError,)) -> bool:
    try:
        fn()
    except exc:
        return True
    return False


def _selftest(chk) -> None:
    import sys
    import tempfile

    # 1. GATE_TABLE verbatim against the spec file.
    try:
        at, spec_rows = _parse_spec_gate_table()
        chk("schedule: GATE_TABLE == spec's sixteen rows (m:161-170)",
            spec_rows == list(GATE_TABLE), f"header at m:{at}")
    except (OSError, ValueError) as e:
        chk("schedule: GATE_TABLE == spec's sixteen rows (m:161-170)", False, repr(e))

    # 2. Gate balance on the table: accepts it; fires on three mutations, each
    #    caught at the m it breaks (m=4, m=8 within-pair only, m=16 within-cell).
    try:
        rep = assert_gate_balance()
        ok = rep["m=16"]["duplicates"] == 0 and rep["m=8"]["n"] == 8
    except AssertionError as e:
        ok, rep = False, repr(e)
    chk("schedule: assert_gate_balance accepts the m:161-170 table (m:172 at 4/8/16)", ok)

    def mutated(fn) -> list[str]:
        cs = _table_cells()
        fn(cs)
        return _gate_balance_problems(cs)

    p_a = mutated(lambda cs: cs[3].update(clause=1 - cs[3]["clause"]))
    p_b = mutated(lambda cs: (cs[0].update(start=1), cs[2].update(start=0)))
    p_c = mutated(lambda cs: (cs[8].update(start=1), cs[12].update(start=0)))
    p_d = mutated(lambda cs: cs[12].update(start=0, clause=0, map=0))
    chk("schedule: gate balance fires at m=4 on a flipped clause (row 3)",
        any(p.startswith("m=4: clause") for p in p_a), p_a[:1])
    chk("schedule: gate balance fires on start not 1/1 within pair at m=8, m=4 silent",
        any("within pair 0" in p and p.startswith("m=8") for p in p_b)
        and not any(p.startswith("m=4") for p in p_b), p_b[:2])
    chk("schedule: gate balance fires only at m=16 on a within-cell start swap",
        bool(p_c) and all(p.startswith("m=16") for p in p_c), p_c[:1])
    chk("schedule: gate balance fires on a duplicate (slot,map,start,clause) row",
        any("duplicate" in p for p in p_d), p_d[-1:])
    chk("schedule: assert_gate_balance raises on a 15-row schedule",
        _refuses(lambda: assert_gate_balance(_table_cells()[:15]), AssertionError))

    # 3. Rosters of record (m:172).
    qr, orr = roster_for("Q-F0"), roster_for("OLMo-dpo")
    chk("schedule: Qwen roster is e2d.config.ROSTER (granite plaza prism slate velvet walnut ridge saddle)",
        qr is not None and [t for p in qr for t in p]
        == "granite plaza prism slate velvet walnut ridge saddle".split(), qr)
    chk("schedule: OLMo roster quartz/velvet, copper/walnut, maple/saddle, amber/granite",
        orr == (("quartz", "velvet"), ("copper", "walnut"), ("maple", "saddle"), ("amber", "granite")), orr)
    chk("schedule: roster normalization refuses a one-label pair and a repeated label",
        _refuses(lambda: _norm_roster([("a",), ("b", "c")]))
        and _refuses(lambda: _norm_roster([("a", "b"), ("b", "c")]))
        and _norm_roster([["a", "b"], ["c", "d"]]) == (("a", "b"), ("c", "d")))
    chk("schedule: a foreign roster is refused (Qwen roster on an OLMo unit)",
        _refuses(lambda: campaign_schedule("OLMo-sft", "A0-OLMo-sft", qr, 1))
        and _refuses(lambda: gate_schedule("Q-F0", "qual", "A0", orr, 8)))

    # 4. Campaign cells: product order, P/Q convention, 32 / 16 cells, ints.
    cc = campaign_cells(qr, True)
    order_ok = [(c["pair_index"], c["map"], c["start"], c["clause"]) for c in cc] == [
        (p, m, s, c) for p in range(4) for m in (0, 1) for s in (0, 1) for c in (0, 1)]
    pq_ok = all(c["P"] == c["pair"][c["map"]] and c["Q"] == c["pair"][1 - c["map"]] for c in cc)
    chk("schedule: campaign_cells is pair x map x start x clause in fixed order, 32 cells",
        len(cc) == 32 and order_ok and pq_ok and _only_ints(cc))
    c16 = campaign_cells(qr, False)
    chk("schedule: campaign_cells without a label-naming TOLD line has 16 cells, clause None",
        len(c16) == 16 and all(c["clause"] is None for c in c16)
        and "clause" not in balance_report(c16)["factors"])

    # 5. Campaign schedule: each unit a permutation of the 32 cells; prefix
    #    property; index form == object-array permutation; ints only; refusals.
    sch = campaign_schedule("Q-F0", "A0", qr, 6)
    full = sorted((c["pair_index"], c["map"], c["start"], c["clause"]) for c in cc)
    units_ok = len(sch) == 6 * 32
    for b in range(6):
        u = sch[32 * b: 32 * (b + 1)]
        r = balance_report(u)
        tuples = sorted((c["pair_index"], c["map"], c["start"], c["clause"]) for c in u)
        # m:188: within every pair the maps split exactly, start within each
        # pair x map cell, clause within cell.
        units_ok = (units_ok and tuples == full and r["duplicates"] == 0
                    and all(w["n"] == 4 and _all_equal(w["start"], 2) and _all_equal(w["clause"], 2)
                            for w in r["within_pair_map"].values()))
    chk("schedule: every balance unit is a permutation of the 32 cells, each "
        "pair x map x start x clause once", units_ok)
    bad = list(sch[:32])
    bad[5] = _copy_cell(bad[6])
    rb = balance_report(bad)
    chk("schedule: the balance-unit check fires on a unit with one cell doubled",
        rb["duplicates"] == 1 and not all(w["n"] == 4 and _all_equal(w["start"], 2)
                                          and _all_equal(w["clause"], 2)
                                          for w in rb["within_pair_map"].values())
        or sorted((c["pair_index"], c["map"], c["start"], c["clause"]) for c in bad) != full)
    longer = campaign_schedule("Q-F0", "A0", qr, 9)
    chk("schedule: campaign prefix property (6 units == first 6 of 9)",
        longer[:len(sch)] == sch and len(longer) == 9 * 32)
    chk("schedule: different arms / units give different unit orders",
        campaign_schedule("Q-F0", "A0s", qr, 1) != sch[:32]
        and campaign_schedule("OLMo-sft", "A0-OLMo-sft", orr, 1)
        != campaign_schedule("OLMo-dpo", "A0-OLMo-dpo", orr, 1))
    key = keys.sched_key("Q-F0", "A0", 2)
    arr = np.empty(len(cc), dtype=object)
    for i, c in enumerate(cc):
        arr[i] = c
    via_obj = list(keys.stream(key).permutation(arr))
    chk("schedule: index-form permutation == permutation(object array of cells) (PIN)",
        [_copy_cell(c) for c in via_obj] == sch[64:96], f"numpy {np.__version__}")
    chk("schedule: campaign cells carry Python ints only", _only_ints(longer))
    chk("schedule: campaign_schedule refuses n_units 0, a bool, a Q-F3 unit, base, a cross-unit arm",
        _refuses(lambda: campaign_schedule("Q-F0", "A0", qr, 0))
        and _refuses(lambda: campaign_schedule("Q-F0", "A0", qr, True))
        and _refuses(lambda: campaign_schedule("Q-F3", "A1", qr, 1), (ValueError, NotImplementedError))
        and _refuses(lambda: roster_for("OLMo-base"))
        and _refuses(lambda: campaign_schedule("Q-F0", "A0-OLMo-sft", qr, 1)))

    # 6. Gate schedules: pi a permutation of 4; rows follow the table; balance
    #    on materialized cells; prefix; m bounds; G-ID on A0 refused.
    g16 = gate_schedule("Q-F0", "qual", "A0s", qr, 16)
    pi = gate_pi("Q-F0", "qual", "A0s")
    rows_ok = all(c["pair_index"] == pi[slot] and (c["map"], c["start"], c["clause"]) == (mp, st, cl)
                  for c, (_j, slot, mp, st, cl) in zip(g16, GATE_TABLE))
    chk("schedule: gate_schedule takes pair pi[slot_j] and row j's map/start/clause",
        sorted(pi) == [0, 1, 2, 3] and rows_ok and _only_ints(g16), pi)
    try:
        assert_gate_balance(g16)
        assert_gate_balance(gate_schedule("OLMo-instruct", "qual", "A0s-OLMo-instruct", orr, 16))
        ok = True
    except AssertionError:
        ok = False
    chk("schedule: materialized 16-session gate schedules pass m:172 (Q-F0, OLMo)", ok)
    chk("schedule: an 8-session gate schedule is the 16's prefix (qual A0's 8)",
        gate_schedule("Q-F0", "qual", "A0", qr, 8) == gate_schedule("Q-F0", "qual", "A0", qr, 16)[:8])
    chk("schedule: gate_schedule refuses m = 17, m = 0 and G-ID on A0; accepts m = 16",
        _refuses(lambda: gate_schedule("Q-F0", "id", "A0s", qr, 17))
        and _refuses(lambda: gate_schedule("Q-F0", "qual", "A0s", qr, 0))
        and _refuses(lambda: gate_schedule("Q-F0", "id", "A0", qr, 2))
        and _refuses(lambda: gate_schedule("OLMo-sft", "id", "A0s-OLMo-sft", orr, 2))
        and len(gate_schedule("Q-F0", "id", "A0s", qr, 16)) == 16)

    # 7. balance_report: fields; a 32-cell unit is fully balanced, a lopsided
    #    list is not.
    br = balance_report(cc)
    chk("schedule: balance_report on one balance unit (all pair x map cells 4, no duplicates)",
        br["n"] == 32 and br["duplicates"] == 0
        and all(w["n"] == 4 and set(w["start"].values()) == {2} for w in br["within_pair_map"].values())
        and set(br["pairwise"]["start*clause"].values()) == {8})
    lop = balance_report(cc[:8])
    chk("schedule: balance_report shows a lopsided prefix (8 cells of pair 0 only)",
        lop["factors"]["pair"] == {"0": 8, "1": 0, "2": 0, "3": 0} and lop["duplicates"] == 0)

    # 8. Launch order and interleave.
    lo = gate_launch_order([("A0", 8), ("A0s", 16)])
    chk("schedule: gate_launch_order rotates A0, A0s, then A0s alone past 8",
        lo[:4] == [("A0", 0), ("A0s", 0), ("A0", 1), ("A0s", 1)] and len(lo) == 24
        and lo[16:] == [("A0s", j) for j in range(8, 16)]
        and gate_launch_order([("A0-OLMo-sft", 1), ("A0s-OLMo-sft", 1)])
        == [("A0-OLMo-sft", 0), ("A0s-OLMo-sft", 0)]
        and gate_launch_order([("A0s", 16)]) == [("A0s", j) for j in range(16)])
    chk("schedule: gate_launch_order refuses sham-first, mixed units, duplicates, count 17",
        _refuses(lambda: gate_launch_order([("A0s", 16), ("A0", 8)]))
        and _refuses(lambda: gate_launch_order([("A0", 8), ("A0s-OLMo-sft", 16)]))
        and _refuses(lambda: gate_launch_order([("A0", 8), ("A0", 8)]))
        and _refuses(lambda: gate_launch_order([("A0", 17)])))

    floor = {"A0": 5, "A0s": 2}
    got: dict[str, int] = {"A0": 0, "A0s": 0}
    seq = []
    for a in interleave(("A0", "A0s"), lambda a: got[a] >= floor[a]):
        seq.append(a)
        got[a] += 1
        if len(seq) > 50:
            break
    chk("schedule: interleave is strict rotation, an arm at floor leaving",
        seq == ["A0", "A0s", "A0", "A0s", "A0", "A0", "A0"], seq)
    got2 = {"A0": 3, "A0s": 2}
    seq2 = []
    for a in interleave(("A0", "A0s"), lambda a: got2[a] >= floor[a], start_counts={"A0": 3, "A0s": 2}):
        seq2.append(a)
        got2[a] += 1
        if len(seq2) > 50:
            break
    chk("schedule: interleave resumes the rotation from on-disk launch counts",
        seq2 == ["A0", "A0"] and got2 == {"A0": 5, "A0s": 2}, seq2)
    seq3 = []
    g3 = {"A0": 3, "A0s": 3}
    for a in interleave(("A0", "A0s"), lambda a: g3[a] >= 99, start_counts=dict(g3)):
        seq3.append(a)
        g3[a] += 1
        if len(seq3) >= 3:
            break
    chk("schedule: interleave at equal counts resumes with the contrast arm",
        seq3 == ["A0", "A0s", "A0"], seq3)
    chk("schedule: interleave refuses sham-first order, counts off-rotation, foreign arms",
        _refuses(lambda: interleave(("A0s", "A0"), lambda a: False))
        and _refuses(lambda: interleave(("A0", "A0s"), lambda a: False,
                                        start_counts={"A0": 7, "A0s": 3}))
        and _refuses(lambda: interleave(("A0", "A0s"), lambda a: False,
                                        start_counts={"A0": 3, "A0s": 4}))
        and _refuses(lambda: interleave(("A0", "A0s"), lambda a: False, start_counts={"A1": 1}))
        and _refuses(lambda: interleave(("A0", "A0s"), lambda a: a == "A0",
                                        start_counts={"A0": 50, "A0s": 20}))
        and _refuses(lambda: interleave(("A0", "A0s-OLMo-sft"), lambda a: False)))
    chk("schedule: interleave accepts counts where the sham left at its floor earlier",
        next(interleave(("A0", "A0s"), lambda a: a == "A0s", start_counts={"A0": 70, "A0s": 40})) == "A0")
    chk("schedule: interleave ends when every arm is at floor",
        list(interleave(("A0-OLMo-dpo", "A0s-OLMo-dpo"), lambda a: True)) == [])

    # 9. MAX_UNITS re-derived from §2.4's launch rule at k = 1 (exact), the
    #    k = 24 rows as a cross-check, and m:203 / m:214's k = 1 totals.
    fc, fu, fs = FLOORS["A0"]["cached"], FLOORS["A0"]["uncached"], FLOORS["A0s"]
    L = {f: _n90_launch(f, 1) for f in (fc, fu, fs)}
    spec_txt = SPEC_PATH.read_text(encoding="utf-8") if SPEC_PATH.exists() else ""
    chk("schedule: k = 1 launch counts from the launch rule (2624 / 2208 / 960)",
        (L[fc], L[fu], L[fs]) == (L_MAX_K1[("Q-F0", "A0", "cached")],
                                  L_MAX_K1[("Q-F0", "A0", "uncached")], L_MAX_K1[("Q-F0", "A0s", None)])
        and _n90_launch(FLOORS["A0-OLMo"], 1) == L_MAX_K1[("OLMo", "A0-OLMo", None)]
        and _n90_launch(FLOORS["A0s-OLMo"], 1) == L_MAX_K1[("OLMo", "A0s-OLMo", None)], L)
    chk("schedule: launch-rule cross-check on the k = 24 / 19 / 12 table rows (m:198-201, m:209-212)",
        [_n90_launch(f, k) for f, k in ((96, 24), (32, 24), (96, 19), (96, 12), (32, 12),
                                       (80, 24), (80, 20), (80, 12))]
        == [128, 64, 160, 224, 96, 96, 128, 192])
    chk("schedule: k = 1 totals are the spec's '1: 3,584' and '1: 3,168'",
        L[fc] + L[fs] == 3584 and L[fu] + L[fs] == 3168
        and "1: 3,584" in spec_txt and "1: 3,168" in spec_txt)
    chk("schedule: MAX_UNITS = Q-F0 A0 82, A0s 30; OLMo A0 69, A0s 30",
        MAX_UNITS[("Q-F0", "A0")] == 82 and MAX_UNITS[("Q-F0", "A0s")] == 30
        and all(MAX_UNITS[(f"OLMo-{c}", f"A0-OLMo-{c}")] == 69
                and MAX_UNITS[(f"OLMo-{c}", f"A0s-OLMo-{c}")] == 30 for c in keys.CKPTS)
        and _ceil_div(L_MAX_K1[("Q-F0", "A0", "uncached")], UNIT_SIZE) == 69, MAX_UNITS)

    # 10. Files: deterministic (two temp dirs, byte-identical), manifest shas,
    #     sha256_of_cells, refusal on a differing file, verify_schedule_dir both ways.
    with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
        m1 = write_schedule_files(t1)
        m2 = write_schedule_files(t2)
        n1 = sorted(os.listdir(t1))
        same = n1 == sorted(os.listdir(t2)) and all(
            (Path(t1) / n).read_bytes() == (Path(t2) / n).read_bytes() for n in n1)
        chk("schedule: write_schedule_files is byte-identical across two writes", same and m1 == m2,
            f"{len(n1)} files")
        want = {schedule_filename("Q-F0", "campaign", "A0"), schedule_filename("Q-F0", "campaign", "A0s"),
                schedule_filename("Q-F0", "time", "A0"), schedule_filename("Q-F0", "time", "A0s"),
                schedule_filename("Q-F0", "id", "A0s"), schedule_filename("Q-F0", "qual", "A0"),
                schedule_filename("Q-F0", "qual", "A0s"), MANIFEST_NAME}
        for c in keys.CKPTS:
            u, (a, s) = f"OLMo-{c}", keys.templates(f"OLMo-{c}")
            want |= {schedule_filename(u, "campaign", a), schedule_filename(u, "campaign", s),
                     schedule_filename(u, "time", a), schedule_filename(u, "time", s),
                     schedule_filename(u, "qual", a), schedule_filename(u, "qual", s)}
        chk("schedule: file set = Q-F0 (2 campaign + 5 gate) + 3 OLMo x (2 + 4) + manifest",
            set(n1) == want and len(n1) == 26, len(n1))
        man = json.loads((Path(t1) / MANIFEST_NAME).read_text())
        o_a0 = json.loads((Path(t1) / schedule_filename("Q-F0", "campaign", "A0")).read_text())
        o_id = json.loads((Path(t1) / schedule_filename("Q-F0", "id", "A0s")).read_text())
        o_oq = json.loads((Path(t1) / schedule_filename("OLMo-sft", "qual", "A0-OLMo-sft")).read_text())
        chk("schedule: file contents (n, units, keys, cells sha, manifest sha)",
            o_a0["n"] == 82 * 32 and o_a0["n_units"] == 82 and o_a0["kind"] == "campaign"
            and o_a0["key_template"] == "m-sched|Q-F0|A0|{b}"
            and o_a0["session_keys"] == {"arm": "m|A0|{s}", "items": "m-items|{s}"}
            and o_a0["sha256_of_cells"] == cells_sha256(o_a0["cells"])
            and o_a0["cells"] == campaign_schedule("Q-F0", "A0", qr, 82)
            and o_id["n"] == 16 and o_id["gate"] == "id"
            and o_id["key_template"] == "m-sched|Q-F0|id|A0s|0"
            and o_id["session_keys"] == {"arm": "m-id|F0m|A0s|{s}", "items": "m-items-id|{s}"}
            and o_oq["n"] == 8 and o_oq["session_keys"]["arm"] == "m-olmo-qual|sft|A0-OLMo-sft|{s}"
            and json.loads((Path(t1) / schedule_filename("OLMo-dpo", "campaign", "A0-OLMo-dpo"))
                           .read_text())["n"] == 69 * 32
            and all(hashlib.sha256((Path(t1) / n).read_bytes()).hexdigest() == man["files"][n]
                    for n in n1 if n != MANIFEST_NAME)
            and json.loads(dumps_schedule(o_id)) == o_id)
        chk("schedule: verify_schedule_dir is clean on a fresh write", verify_schedule_dir(t1) == [],
            verify_schedule_dir(t1)[:2])
        victim = Path(t1) / schedule_filename("Q-F0", "qual", "A0s")
        o = json.loads(victim.read_text())
        o["cells"][0]["start"] = 1 - o["cells"][0]["start"]
        victim.write_text(dumps_schedule(o))
        probs = verify_schedule_dir(t1)
        chk("schedule: verify_schedule_dir fires on a tampered cell (regen, manifest, cells sha)",
            any("differs" in p for p in probs) and any("manifest" in p for p in probs)
            and any("cells sha" in p for p in probs), probs[:3])
        chk("schedule: write_schedule_files refuses to overwrite a differing file",
            _refuses(lambda: write_schedule_files(t1), RuntimeError))
        write_schedule_files(t1, overwrite=True)
        chk("schedule: overwrite=True restores the regeneration",
            verify_schedule_dir(t1) == [] and victim.read_bytes() == (Path(t2) / victim.name).read_bytes())

    chk("schedule: the quarantined state-present module is not imported",
        "valence_core.e2b.statepresent" not in sys.modules)
