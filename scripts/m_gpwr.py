#!/usr/bin/env python3
"""G-PWR for Q-F0 (PROPOSAL-m v1.11 m:285, step 15 of m:358), on the methods of the seat's step-15 answers, Q7.

    python scripts/m_gpwr.py --selftest
    python scripts/m_gpwr.py --lock-draft <the LOCK v1.0 draft> --record data/m/gates/Q-F0_G-PWR.json

m:285: "§2.4's power with planned floors; any n raised; launch counts from the unit's k; the unit's look count and
the exact sequential false-pause probabilities of §6 for that look count; the exclusion guard's false-pause figure."
Model-free and exact (Fractions throughout; no float enters a comparison). Not a stages.py stage (the answers' "The
not-questions": "G-PWR is not a `stages.py` stage"): it reads no checkpoint, report or session record, and it moves
neither the analyzer's sha256 nor the package's (it lives outside valence_core/m and is not the analyzer).

Inputs of record (each named where it is printed):
  - k = 18 of n_q = 24 on the uncached path: the G-F0m-Qwen entry ("r for Q-F0's launch rule is 18/24 (A0 7/8, A0s
    11/16)", its bold markers dropped), the answers' item 5 ("G-PWR on the uncached path with r = 18/24") and Q7;
  - the floors A0 80, A0s 32 (uncached; schedule.FLOORS), the balance unit 32 (schedule.UNIT_SIZE), a look every 40
    launches and at the end (resume.LOOK_EVERY);
  - the bars of lock §8.2 rows 7-9 (bars._campaign): round_degeneracy p0 .05 alpha .05 on the sham arm's rounds; the
    guard's Fisher half (one-sided, alpha .05, vs the matched sham) and absolute half (p0 .20, alpha .05), both on the
    contrast arm's launches;
  - the sham's realised rounds at G-F0m-Qwen, 136 of 160 (the G-F0m-Qwen entry: "silent at 2/136"; "five sham
    sessions ended early at an exclusion"), for Q7 (a)'s second case beside.
"""
from __future__ import annotations

import sys
import os
if __name__ == "__main__" and not sys.flags.isolated:      # before any import a script directory could shadow
    raise SystemExit("REFUSED: a run of record runs in isolated mode (python -I): no script directory, user site or "
                     "environment path enters the import path")
if __name__ == "__main__" and (not sys.pycache_prefix or os.path.exists(sys.pycache_prefix)):
    raise SystemExit("REFUSED: a run of record reads no cached bytecode: run with -X pycache_prefix=<a path that does "
                     "not exist>, so every module is compiled from the bytes provenance binds")

import argparse
import hashlib
import importlib.abc
import importlib.machinery
import importlib.util
import itertools
import io
import json
import subprocess
from fractions import Fraction
from math import ceil, comb
from contextlib import redirect_stdout
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.append(str(REPO))          # appended: no file under REPO can shadow a module found earlier on the path


GIT = ("git", "--no-replace-objects", "-C", str(REPO))   # no replace ref can stand another object in for a bound one
_GIT_ENV = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}   # no GIT_DIR, index or object store


class _GitFailed(Exception):
    """A git read that failed (a missing, corrupt or forged object among them): the run refuses, stating it."""


def _gitrun(*args, check: bool = False, **kw) -> subprocess.CompletedProcess:
    r = subprocess.run([*GIT, *args], env=_GIT_ENV, capture_output=True, **kw)
    if check and r.returncode != 0:
        err = r.stderr if isinstance(r.stderr, str) else r.stderr.decode("utf-8", "replace")
        raise _GitFailed(f"git {' '.join(args)} exited {r.returncode}: {err.strip()[:300]}")
    return r


_PINNED = globals().get("_GPWR_COMMIT")             # set only by the self-test child's bootstrap (main(), _CHILD_BOOT)
try:
    _LOAD_COMMIT = _gitrun("rev-parse", "--verify", f"{_PINNED or 'HEAD'}^{{commit}}", text=True,
                           check=True).stdout.strip()
except _GitFailed as e:
    if __name__ == "__main__":
        raise SystemExit(f"REFUSED: {e}")
    raise
if _PINNED and _LOAD_COMMIT != _PINNED:
    raise SystemExit(f"REFUSED: the self-test's commit {_PINNED!r} does not resolve to itself")
_LOADED: dict = {}                     # rel -> the blob id of the bytes executed, from the commit HEAD named at startup


def _blob_id(data: bytes, like: str) -> str:
    """The git object id of a blob holding data, in the repository's hash (by the length of a known id)."""
    return hashlib.new("sha1" if len(like) == 40 else "sha256", b"blob %d\0" % len(data) + data).hexdigest()


def _head_blob(rel: str) -> bytes:
    """The bytes of rel in the tree of the commit HEAD named at startup, never the working tree's; the bytes are
    checked to hash to the tree's blob id, and the id is recorded for provenance."""
    r = _gitrun("rev-parse", "--verify", "--quiet", f"{_LOAD_COMMIT}:{rel}", text=True)
    oid = r.stdout.strip()
    if r.returncode != 0 or not oid:
        raise ImportError(f"{rel} is not in HEAD's tree: a run executes committed bytes only")
    try:
        data = _gitrun("cat-file", "blob", oid, check=True).stdout
    except _GitFailed as e:
        raise ImportError(f"{rel}: {e}")
    if _blob_id(data, oid) != oid:
        raise ImportError(f"{rel}: the bytes read do not hash to HEAD's blob {oid}")
    _LOADED[rel] = oid
    return data


class _HeadBlobLoader(importlib.abc.Loader):
    """Executes a module's source from HEAD's blob, so the bytes that run are the bytes provenance binds (a working-
    tree file read after import, rewritten or swapped, cannot change what ran)."""

    def __init__(self, rel: str, origin: str):
        self.rel, self.origin = rel, origin

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        code = compile(_head_blob(self.rel), self.origin, "exec", dont_inherit=True)
        exec(code, module.__dict__)


def _repo_rel(path: str):
    """path relative to REPO (as given, then as resolved), or None outside it."""
    for cand, root in ((os.path.abspath(path), os.path.abspath(REPO)), (os.path.realpath(path), os.path.realpath(REPO))):
        try:
            return Path(cand).relative_to(root).as_posix()
        except ValueError:
            continue
    return None


class _HeadBlobFinder(importlib.abc.MetaPathFinder):
    """Stands just before the path finder (built-in and frozen modules keep their precedence) and locates every
    module as the path finder does. valence_core is located under REPO only, and each of its modules is executed from
    HEAD's blob: it must be a .py source in HEAD's tree (anything else, an extension module, a package directory HEAD
    lacks, a namespace package, is refused). Any other name located inside the repository (outside the gitignored
    jlens-qwen36 clone and its environment) is absent: the run imports nothing else from it."""

    def find_spec(self, name, path, target=None):
        top = name == "valence_core" or name.startswith("valence_core.")
        spec = importlib.machinery.PathFinder.find_spec(name, [str(REPO)] if top and path is None else path, target)
        if spec is None:
            return None
        where = spec.origin if spec.has_location and spec.origin else next(iter(spec.submodule_search_locations or []),
                                                                         "")
        rel = _repo_rel(where) if where else None
        if rel is None or rel.startswith("jlens-qwen36/"):
            if top:
                raise ImportError(f"{name} resolves outside the repository: {where!r}")
            return spec
        if not top:                                    # a name found only at the repository's root, committed or not,
            raise ModuleNotFoundError(f"{name} resolves to {rel} in the repository: only valence_core is imported "
                                      f"from it", name=name)   # is absent, as on a clean interpreter
        if not (spec.has_location and spec.origin and spec.origin.endswith(".py")):
            raise ImportError(f"{name} resolves to {rel} in the repository, not a .py source: refused")
        spec.loader = _HeadBlobLoader(rel, spec.origin)
        spec.cached = None
        return spec


sys.meta_path.insert(sys.meta_path.index(importlib.machinery.PathFinder), _HeadBlobFinder())

try:
    from valence_core.m import bars, resume, schedule  # noqa: E402
except ImportError as e:                               # a module HEAD's tree lacks, or not a .py source: nothing ran
    if __name__ == "__main__":
        raise SystemExit(f"REFUSED: {e}")
    raise

SCHEMA = "m-gpwr-v1"
UNIT = "Q-F0"
PATH = "uncached"
K, N_Q = 18, schedule.N_Q
PER_TEMPLATE = {"A0": (7, 8), "A0s": (11, 16)}         # beside only (m:192: "reported per template beside")
ARMS = ("A0", "A0s")                                   # §2.4's table order; contrast first
FLOOR = {"A0": schedule.FLOORS["A0"][PATH], "A0s": schedule.FLOORS["A0s"]}
POWER_FLOOR = Fraction(85, 100)                        # m:190: "every control ≥ .85 at P = .70"
DEGEN_P0, ALPHA = Fraction(5, 100), Fraction(5, 100)   # lock §8.2 row 7 (Qwen p0 .05; alpha .05 per look, m:330)
GUARD_ABS_P0 = Fraction(20, 100)                       # lock §8.2 row 9 (m:316: ".20 on Qwen")
SHAM_ROUNDS_REALISED = (136, 160)                      # G-F0m-Qwen's sham arm: realised / planned task rounds
GRID = [Fraction(j, 100) for j in range(1, 100)]       # the Fisher half's grid of common null rates
REFINE_STEP, REFINE_HALF = Fraction(1, 1000), 10       # the grid refined around its maximum: +/- 10 steps of .001
N90_CAP = 100_000                                      # n90's scan bound (k = 1 at floor 96 needs about 2,600)
DRAFT_HEAD = "# LOCK-m-F0.md — v1.0"                   # the LOCK v1.0 draft's first line begins so
_IN_SETUP_PROBE = False                                # the self-test's setup-guard check is running


def _bar(name: str):
    return {b.name: b for b in bars.QF0_BARS}[name]


DEGEN_BAR, FISHER_BAR, ABS_BAR = ("round_degeneracy@campaign-Q-F0", "exclusion_guard_fisher@campaign-Q-F0",
                                  "exclusion_guard_abs@campaign-Q-F0")


def bar_problems() -> list[str]:
    """The constants this program computes with, against the bars of record (lock §8.2 rows 7-9)."""
    out = []
    d, f, a = _bar(DEGEN_BAR), _bar(FISHER_BAR), _bar(ABS_BAR)
    if (d.kind, d.p0q, d.alphaq, d.domain, d.binding) != ("binomial_look", DEGEN_P0, ALPHA, "sham", True):
        out.append(f"{DEGEN_BAR}: {(d.kind, d.p0q, d.alphaq, d.domain, d.binding)}")
    if (f.kind, f.alphaq, f.domain, f.binding) != ("guard_fisher", ALPHA, "contrast_arm", True):
        out.append(f"{FISHER_BAR}: {(f.kind, f.alphaq, f.domain, f.binding)}")
    if (a.kind, a.p0q, a.alphaq, a.domain, a.binding) != ("guard_abs", GUARD_ABS_P0, ALPHA, "contrast_arm", True):
        out.append(f"{ABS_BAR}: {(a.kind, a.p0q, a.alphaq, a.domain, a.binding)}")
    return out


def region_problems(n1: int, n2: int) -> list[str]:
    """guard_regions at one look against the bars' own evaluate(): every (a, c) cell of the Fisher set and the abs
    half's critical count."""
    reg = guard_regions([(n1, n2)])[0]
    f, a = _bar(FISHER_BAR), _bar(ABS_BAR)
    out = [f"fisher cell {(x, y)}" for x in range(n1 + 1) for y in range(n2 + 1)
           if ((x, y) in reg["fisher"]) != f.evaluate(x, n1, sham_k=y, sham_n=n2).exceeds]
    if reg["abs_crit"] != a.evaluate(0, n1).crit:
        out.append(f"abs crit {reg['abs_crit']} vs the bar's {a.evaluate(0, n1).crit}")
    return out


def _analyzer():
    """The analyzer, executed from HEAD's blob (as valence_core is)."""
    origin = str(REPO / "scripts" / "m_analyze.py")
    spec = importlib.util.spec_from_loader("m_analyze_gpwr", _HeadBlobLoader("scripts/m_analyze.py", origin),
                                           origin=origin)
    m = importlib.util.module_from_spec(spec)
    m.__file__ = origin
    sys.modules["m_analyze_gpwr"] = m
    spec.loader.exec_module(m)
    return m


def fs(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def dec(x: Fraction, places: int = 4) -> str:
    """Exact half-up decimal (bars._dec's rule, any number of places)."""
    scale = 10 ** places
    v = (x * scale * 2 + 1) // 2
    whole, frac = divmod(int(v), scale)
    return f"{whole}.{frac:0{places}d}"


def rec(x: Fraction, places: int = 4) -> dict:
    return {"exact": fs(x), "display": dec(x, places)}


# --- §2.4: power at the floors, the launch rule, the looks ---------------------------------------
def n90(floor: int, r: Fraction) -> int:
    """The smallest N with P(Bin(N, r) >= floor) >= .90 (m:192), by ascending scan from N = floor."""
    if not 0 < r <= 1:
        raise ValueError(f"r must be in (0, 1] (m:192: at k = 0 the rule yields no launch count), got {r}")
    n = floor
    while bars.binom_sf(floor, n, r) < Fraction(9, 10):
        n += 1
        if n > N90_CAP:
            raise ValueError(f"N90 past {N90_CAP} at floor {floor}, r {r}: refused rather than scanned further")
    return n


def launch_count(floor: int, r: Fraction, unit: int = schedule.UNIT_SIZE) -> dict:
    """m:192: L = ceil_unit(max(ceil(1.15 floor), N90(r)))."""
    up = ceil(Fraction(115, 100) * floor)
    nn = n90(floor, r)
    return {"floor": floor, "ceil_1.15_floor": up, "N90": nn, "L": -(-max(up, nn) // unit) * unit}


def looks_for(total: int) -> int:
    return -(-total // resume.LOOK_EVERY)


def project(stop: dict) -> list[dict]:
    """The launch sequence under schedule.interleave (fewest launches, ties to table order; an arm out of the
    rotation for good once done), each arm launching until it has launched stop[arm] times. Looks fall at every
    LOOK_EVERY-th launch and at the end (m:330); an end on a multiple adds no look. Returns the looks with the
    cumulative launches per arm."""
    if not all(type(stop[a]) is int and stop[a] >= 1 for a in ARMS):
        raise ValueError(f"project: every arm launches at least once, got {stop}")
    counts = {a: 0 for a in ARMS}
    it = schedule.interleave(list(ARMS), lambda a: counts[a] >= stop[a])
    looks, total = [], 0
    for arm in it:
        counts[arm] += 1
        total += 1
        if total % resume.LOOK_EVERY == 0:
            looks.append({"look": len(looks) + 1, "launches": total, **{a: counts[a] for a in ARMS}})
        if all(counts[a] >= stop[a] for a in ARMS):
            break
    if not looks or looks[-1]["launches"] != total:
        looks.append({"look": len(looks) + 1, "launches": total, **{a: counts[a] for a in ARMS}, "end": True})
    else:
        looks[-1]["end"] = True
    return looks


# --- §6: the sequential false-pause figures ------------------------------------------------------
def _binom_row(m: int, a: int, b: int) -> list[int]:
    return [comb(m, i) * a ** i * (b - a) ** (m - i) for i in range(m + 1)]


def guard_regions(looks: list[tuple[int, int]], alpha: Fraction = ALPHA, abs_p0: Fraction = GUARD_ABS_P0) -> list[dict]:
    """Per look (n1 contrast launches, n2 sham launches): the absolute half's critical count and the Fisher half's
    firing set {(a, c): fisher_sf(a, n1, c, n2) <= alpha}, a the contrast's and c the sham's pre-pick exclusions."""
    out = []
    for n1, n2 in looks:
        fis = {(a, c) for a in range(n1 + 1) for c in range(n2 + 1) if bars.fisher_sf(a, n1, c, n2) <= alpha}
        out.append({"n1": n1, "n2": n2, "abs_crit": bars.critical_k(n1, abs_p0, alpha), "fisher": fis})
    return out


def guard_false_pause(regions: list[dict], p: Fraction, halves: tuple[str, ...]) -> Fraction:
    """P(some look fires) when every session of both arms is excluded before its first pick independently at the
    common rate p, the guard firing at a look iff one of `halves` ('abs', 'fisher') fires there. Exact dynamic
    programme over the joint surviving counts (a, c), in integers over b**(n1 + n2); each look's new launches are
    convolved one arm at a time, then the look's firing set is removed."""
    p = Fraction(p)
    if not 0 <= p <= 1:
        raise ValueError(f"p out of [0, 1]: {p}")
    if not halves or set(halves) - {"abs", "fisher"}:
        raise ValueError(f"halves must be drawn from ('abs', 'fisher'), got {halves}")
    a_, b_ = p.numerator, p.denominator
    dist = {(0, 0): 1}
    p1 = p2 = 0
    for reg in regions:
        n1, n2 = reg["n1"], reg["n2"]
        if n1 < p1 or n2 < p2:
            raise ValueError(f"looks must be non-decreasing cumulative launches: {(p1, p2)} -> {(n1, n2)}")
        r1, r2 = _binom_row(n1 - p1, a_, b_), _binom_row(n2 - p2, a_, b_)
        mid: dict[tuple[int, int], int] = {}
        for (a, c), w in dist.items():
            for i, wi in enumerate(r1):
                key = (a + i, c)
                mid[key] = mid.get(key, 0) + w * wi
        nd: dict[tuple[int, int], int] = {}
        for (a, c), w in mid.items():
            for j, wj in enumerate(r2):
                key = (a, c + j)
                nd[key] = nd.get(key, 0) + w * wj
        crit, fis = reg["abs_crit"], reg["fisher"]
        dist = {}
        for (a, c), w in nd.items():
            fired = ("abs" in halves and crit is not None and a >= crit) or ("fisher" in halves and (a, c) in fis)
            if not fired and w:
                dist[(a, c)] = w
        p1, p2 = n1, n2
    return 1 - Fraction(sum(dist.values()), b_ ** (p1 + p2))


def degeneracy(rounds: list[int]) -> dict:
    return {"n_j": rounds, "crit_j": [bars.critical_k(n, DEGEN_P0, ALPHA) for n in rounds],
            "false_pause": rec(bars.seq_false_pause(rounds, DEGEN_P0, ALPHA))}


def grid_max(regions, halves, rates) -> tuple[Fraction, Fraction]:
    """The maximum over the rates, and its rate; an exact tie goes to the smaller rate."""
    best = (Fraction(-1), Fraction(0))
    for p in rates:
        v = guard_false_pause(regions, p, halves)
        if v > best[0]:
            best = (v, p)
    return best


def guard_block(looks: list[dict], with_grid: bool) -> dict:
    pairs = [(lk["A0"], lk["A0s"]) for lk in looks]
    regions = guard_regions(pairs)
    out = {"looks_n1_n2": [list(x) for x in pairs], "abs_crit_j": [r["abs_crit"] for r in regions],
           "fisher_cells_j": [len(r["fisher"]) for r in regions],
           "at_common_rate_p0": {"p": fs(GUARD_ABS_P0),
                                 "abs": rec(guard_false_pause(regions, GUARD_ABS_P0, ("abs",))),
                                 "fisher": rec(guard_false_pause(regions, GUARD_ABS_P0, ("fisher",))),
                                 "union": rec(guard_false_pause(regions, GUARD_ABS_P0, ("abs", "fisher")))}}
    if with_grid:
        grid = [{"p": fs(p), "fisher": rec(guard_false_pause(regions, p, ("fisher",)))} for p in GRID]
        vmax, pmax = Fraction(-1), Fraction(0)
        for g_ in grid:                             # the same tie rule as grid_max: the smaller rate
            if Fraction(g_["fisher"]["exact"]) > vmax:
                vmax, pmax = Fraction(g_["fisher"]["exact"]), Fraction(g_["p"])
        fine = [q for q in (pmax + (i - REFINE_HALF) * REFINE_STEP for i in range(2 * REFINE_HALF + 1)) if 0 < q < 1]
        fmax, fp = grid_max(regions, ("fisher",), fine)
        umax, up = grid_max(regions, ("abs", "fisher"), [p for p in GRID if p <= GUARD_ABS_P0])
        out["fisher_grid"] = grid
        out["fisher_grid_max"] = {"p": fs(pmax), **rec(vmax)}
        out["fisher_grid_max_refined"] = {"p": fs(fp), **rec(fmax), "rates": [fs(min(fine)), fs(max(fine))]}
        out["union_grid_max_p_le_p0"] = {"p": fs(up), **rec(umax)}
    return out


# --- the run --------------------------------------------------------------------------------------
READINGS = [
    "The seat's step-15 answers, Q7, verbatim: \"Code's defaults are the seat's, declared at G-PWR on Q1's terms "
    "(strikable until v1.0's commit; a strike recomputes figures only)\".",
    "Q7 (a), verbatim: \"n_j at each look from the projection \u2014 each arm launches to its L, interleaved by the "
    "campaign rule, every sham session running its 10 rounds \u2014 with two cases beside: the sham arm leaving the "
    "rotation at its floor; the sham arm at G-F0m-Qwen's measured 136 of 160 realised rounds.\"",
    "Code's reading inside Q7 (a): 'the sham arm leaving the rotation at its floor' is computed at two launch counts: "
    "ceil(32 / r) = 43, at the unit's one rate r = 18/24 (m:192), and 32, the fewest at which the sham can reach its "
    "floor. A0 launches to its L in both. Both floor cases keep 10 rounds per sham launch; in the 43 case that "
    "over-counts the rounds of the about 11 sessions it assumes end early at an exclusion. The guard's figures move "
    "with the sham's launches. The 136-of-160 case changes rounds only, so only round_degeneracy is recomputed there, "
    "at 136/16 = 17/2 rounds per sham launch.",
    "Q7 (b), verbatim: \"the absolute half exact at p0 = .20 over the contrast arm's launches per look; the Fisher "
    "half under a common null rate equal to the absolute p0, with a grid of rates and the supremum beside; the "
    "guard's false-pause figure as the union \u2014 the probability that either half fires at some look \u2014 "
    "computed jointly over the contrast and sham counts under the common null rate, each half's own figure "
    "beside.\"",
    "Code's reading inside Q7 (b): 'the supremum' is reported as the maximum over the grid j/100 (j = 1..99), refined "
    "to .001 within +/- .01 of that maximum; a grid maximum bounds the supremum over (0, 1) from below. The union is "
    "also reported at its grid maximum over common rates p <= .20, where neither half's pause is a true one. Every "
    "session of both arms is excluded before its first pick independently at the common rate, and both halves count "
    "sessions launched in the arm through the look (bars.py:509). The grid, its maximum and the union's maximum are "
    "figured on the projection only; the cases beside carry the figures at the common rate .20. An exact tie between "
    "rates goes to the smaller rate (no tie occurs on any grid computed here).",
    "Q7 (c), verbatim: \"the joint figure is `round_degeneracy`'s own, with the guard's beside; the non-separable "
    "joint over the bar and the guard is not computed, and G-PWR says why in one sentence.\" The hair triggers "
    "carry no p0, and the lexical bar has no domain in Q-F0 (m:330), so neither has a figure.",
    "m:190's raise is not triggered: power at the floors is at least .85. Had it been below, this program would stop "
    "and escalate rather than apply the raise, whose 'sham in proportion' clause it does not settle.",
    "The planning row, Q7 verbatim: \"The planning row stands as the input (m:210: k = 18 of 24 uncached \u2192 L = "
    "128 and 64, total 192, 5 looks; power at the floors .878 \u2265 .85, no n raised), recomputed at G-PWR with "
    "PIN-3's base case re-derived at the planned floors (R1 C6).\"",
]
JOINT_SENTENCE = ("The joint over round_degeneracy and the guard is not computed: a sham session that ends early at "
                  "a pre-pick exclusion enters the guard's sham count and cuts its own rounds in the bar's n, and a "
                  "round the bar counts can be what excludes it, so the two are dependent through a model of "
                  "exclusion and round-claim co-occurrence that no record gives.")


def compute(m) -> dict:
    bp = bar_problems()
    if bp:
        raise SystemExit(f"STOP: this program's constants differ from the bars of record: {bp}")
    r = Fraction(K, N_Q)
    pwr = m.power_exact(FLOOR["A0"] // 2, FLOOR["A0"] - FLOOR["A0"] // 2, FLOOR["A0s"])
    if pwr < POWER_FLOOR:
        raise SystemExit("STOP: power at the floors is below .85; m:190 raises n in whole units, a rule this "
                         "program does not apply -- escalate (Code never self-adjudicates)")
    pin3 = dict(m.power_block(FLOOR["A0"] // 2, FLOOR["A0"] - FLOOR["A0"] // 2, FLOOR["A0s"])["of_record"])
    pin3["basis"] = ("PIN-3's base case re-derived at the planned floors (Q7; R1 C6): the analyzer's power_block at n = "
                     "80 split [40, 40] at clean share .70, the sham pooled at mS = 32 at .5, alpha .01. A planning "
                     "figure; the figure of record for the verdict sentences is the attained power at the realised n, "
                     "reported in VERDICTS (m:190).")
    try:
        launch = {a: launch_count(FLOOR[a], r) for a in ARMS}
    except ValueError as e:      # k = 0 (m:192): checked before schedule._n90_launch, whose search does not end at k = 0
        if "r must be in (0, 1]" not in str(e):
            raise
        raise SystemExit(f"STOP: {e} -- m:192: G-PWR cannot run, LOCK v1.0 cannot be committed")
    for a in ARMS:
        if launch[a]["L"] != schedule._n90_launch(FLOOR[a], K):
            raise SystemExit(f"STOP: the launch rule disagrees with schedule._n90_launch for {a}")
    L = {a: launch[a]["L"] for a in ARMS}
    total = sum(L.values())
    n_looks = looks_for(total)
    rows = {}
    for k in range(1, N_Q + 1):
        lk = {a: launch_count(FLOOR[a], Fraction(k, N_Q))["L"] for a in ARMS}
        t = sum(lk.values())
        rows[str(k)] = {**lk, "total": t, "looks": looks_for(t)}
    same_row = [int(k) for k in rows if (rows[k]["A0"], rows[k]["A0s"]) == (L["A0"], L["A0s"])]

    floor_r = ceil(Fraction(FLOOR["A0s"]) / r)
    cases = {
        "projection": {"stop": dict(L), "rounds_per_sham_launch": "10"},
        "sham_at_floor_r": {"stop": {"A0": L["A0"], "A0s": floor_r}, "rounds_per_sham_launch": "10"},
        "sham_at_floor_min": {"stop": {"A0": L["A0"], "A0s": FLOOR["A0s"]}, "rounds_per_sham_launch": "10"},
        "sham_realised_rounds": {"stop": dict(L), "rounds_per_sham_launch":
                                 fs(Fraction(SHAM_ROUNDS_REALISED[0], SHAM_ROUNDS_REALISED[1]) * bars.MAX_ROUNDS)},
    }
    rounds = {}
    for name, cs in cases.items():          # the cheap pass: every case's looks and rounds, checked before any figure
        lks = project(cs["stop"])
        per = Fraction(cs["rounds_per_sham_launch"])
        rounds[name] = [lk["A0s"] * per for lk in lks]
        if any(x.denominator != 1 for x in rounds[name]):
            raise SystemExit(f"STOP: case {name}: non-integer sham rounds {rounds[name]}")
        cs["looks"] = lks
        cs["n_looks"] = len(lks)
    proj = cases["projection"]
    if proj["n_looks"] != n_looks:
        raise SystemExit(f"STOP: the projection's looks {proj['n_looks']} differ from ceil(total/40) = {n_looks}")
    for name, cs in cases.items():
        cs["round_degeneracy"] = degeneracy([int(x) for x in rounds[name]])
        if name != "sham_realised_rounds":
            cs["guard"] = guard_block(cs["looks"], with_grid=(name == "projection"))
    return {
        "schema": SCHEMA, "unit": UNIT, "path": PATH,
        "inputs": {"k": K, "n_q": N_Q, "r": fs(r), "per_template_beside": {a: fs(Fraction(*PER_TEMPLATE[a]))
                                                                           for a in ARMS},
                   "floors": dict(FLOOR), "balance_unit": schedule.UNIT_SIZE, "look_every": resume.LOOK_EVERY,
                   "round_degeneracy": {"p0": fs(DEGEN_P0), "alpha": fs(ALPHA), "domain": "sham rounds"},
                   "guard": {"abs_p0": fs(GUARD_ABS_P0), "alpha": fs(ALPHA), "unit": "sessions launched"},
                   "sham_rounds_realised_at_G-F0m-Qwen": list(SHAM_ROUNDS_REALISED)},
        "power": {"at_floors": {"A0": FLOOR["A0"], "A0s": FLOOR["A0s"], **rec(pwr, 3), "exact4": dec(pwr),
                                "basis": "m:190's base case: A0 split n/2 per map at clean share .70, the sham "
                                         "pooled at .5, alpha .01 (m_analyze.power_exact)"},
                  "power_floor": fs(POWER_FLOOR), "n_raised": False,
                  "pin3_of_record_at_floors": pin3},
        "launch": {"rule": launch, "L": L, "total": total, "looks": n_looks,
                   "k_with_this_row": same_row, "rows_by_k": rows},
        "cases": cases,
        "joint": {"figure": "round_degeneracy's own (projection case)",
                  "value": proj["round_degeneracy"]["false_pause"],
                  "guard_beside": proj["guard"]["at_common_rate_p0"]["union"],
                  "not_computed": JOINT_SENTENCE},
        "not_figured": {"hair_triggers": "no p0: a ~zero-base-rate class whose fire stops the stage (m:271)",
                        "lexical": "no domain in Q-F0: every banner names labels; reported only (m:330)"},
        "readings": READINGS,
    }


# --- self-test ------------------------------------------------------------------------------------
def inputs_problems(res: dict) -> list[str]:
    """The record's inputs block and power floor against the bars of record (p0s, alphas) and literals."""
    d, f, a = _bar(DEGEN_BAR), _bar(FISHER_BAR), _bar(ABS_BAR)
    want = {"k": 18, "n_q": 24, "r": "3/4", "per_template_beside": {"A0": "7/8", "A0s": "11/16"},
            "floors": {"A0": 80, "A0s": 32}, "balance_unit": 32, "look_every": 40,
            "round_degeneracy": {"p0": fs(d.p0q), "alpha": fs(d.alphaq), "domain": "sham rounds"},
            "guard": {"abs_p0": fs(a.p0q), "alpha": fs(a.alphaq), "unit": "sessions launched"},
            "sham_rounds_realised_at_G-F0m-Qwen": [136, 160]}
    out = [f"inputs.{k_}" for k_ in sorted(set(want) | set(res["inputs"])) if res["inputs"].get(k_) != want.get(k_)]
    if res["power"]["power_floor"] != "17/20":
        out.append("power.power_floor")
    if f.alphaq != a.alphaq:
        out.append("the guard's two alphas differ")
    return out


def display_problems(res: dict) -> list[str]:
    """Every {exact, display} pair, at any depth (dicts and lists), displays its exact value half-up: four places, the
    power three."""
    bad = []

    def walk(x, path):
        if isinstance(x, dict):
            if "exact" in x and "display" in x and isinstance(x["exact"], str):
                places = 3 if path.endswith("power.at_floors") or path.endswith("pin3_of_record_at_floors") else 4
                if x["display"] != dec(Fraction(x["exact"]), places):
                    bad.append(path)
            for k_, v_ in x.items():
                walk(v_, f"{path}.{k_}")
        elif isinstance(x, list):
            for i_, v_ in enumerate(x):
                walk(v_, f"{path}[{i_}]")
    walk(res, "$")
    return bad


def line_problems(res: dict, so: str) -> list[str]:
    """report()'s labelled lines, each rebuilt from the record and required as a whole line: the launch and joint lines
    in the whole stdout, each case's lines within that case's own section (from its CASE line to the next)."""
    got = so.splitlines()
    out = [w for w in [f"LAUNCH {a_}: floor {lr['floor']}, ceil(1.15 floor) {lr['ceil_1.15_floor']}, N90 {lr['N90']} "
                       f"-> L {lr['L']}" for a_, lr in res["launch"]["rule"].items()] if w not in got]
    starts = [i for i, ln in enumerate(got) if ln.startswith("CASE ")] + [len(got)]
    sections = {got[s].split(":")[0][5:]: got[s:e] for s, e in zip(starts, starts[1:])}
    for name, cs_ in res["cases"].items():
        sec = sections.get(name, [])
        want = []
        want += [f"  look {lk['look']}: launches {lk['launches']} (A0 {lk['A0']}, A0s {lk['A0s']})"
                 f"{' end' if lk.get('end') else ''}" for lk in cs_["looks"]]
        rd_ = cs_["round_degeneracy"]
        want.append(f"  round_degeneracy: n_j {rd_['n_j']} crit_j {rd_['crit_j']} false pause "
                    f"{rd_['false_pause']['display']}")
        if "guard" in cs_:
            g_ = cs_["guard"]
            want.append(f"  guard: (n1, n2)_j {g_['looks_n1_n2']} abs crit_j {g_['abs_crit_j']} Fisher cells_j "
                        f"{g_['fisher_cells_j']}")
            if "fisher_grid" in g_:
                want.append(f"  Fisher grid max {g_['fisher_grid_max']['display']} at p {g_['fisher_grid_max']['p']}; "
                            f"refined {g_['fisher_grid_max_refined']['display']} at p "
                            f"{g_['fisher_grid_max_refined']['p']} (rates {g_['fisher_grid_max_refined']['rates']})")
                want.append(f"  union grid max over p <= 1/5: {g_['union_grid_max_p_le_p0']['display']} at p "
                            f"{g_['union_grid_max_p_le_p0']['p']}")
        n_look_lines = sum(1 for ln in sec if ln.startswith("  look "))
        out += [f"{name}: {w}" for w in want if w not in sec]
        if n_look_lines != len(cs_["looks"]):
            out.append(f"{name}: {n_look_lines} look lines for {len(cs_['looks'])} looks")
    jj = res["joint"]
    jl = (f"JOINT: {jj['figure']}: {jj['value']['display']}; the guard's beside (union at .20): "
          f"{jj['guard_beside']['display']}")
    return out + ([] if jl in got else [jl])


def reference_report(res: dict) -> list[str]:
    """The report's lines, rendered from the record independently of report(): the raw of record must equal it."""
    L_ = []
    inp, pw = res["inputs"], res["power"]
    L_.append(f"G-PWR {res['unit']} ({res['path']}); k = {inp['k']} of {inp['n_q']}, r = {inp['r']} (A0 "
              f"{inp['per_template_beside']['A0']}, A0s {inp['per_template_beside']['A0s']} beside)")
    af = pw["at_floors"]
    L_.append(f"POWER at the floors (A0 {af['A0']}, A0s {af['A0s']}): {af['display']} ({af['exact4']}) >= .85; "
              f"no n raised")
    p3 = pw["pin3_of_record_at_floors"]
    L_.append(f"PIN-3 of record at the floors: {p3['display']} split {p3['split']} mS {p3['mS']}")
    for arm, lr in res["launch"]["rule"].items():
        L_.append(f"LAUNCH {arm}: floor {lr['floor']}, ceil(1.15 floor) {lr['ceil_1.15_floor']}, N90 {lr['N90']} -> "
                  f"L {lr['L']}")
    la = res["launch"]
    L_.append(f"TOTAL {la['total']}; LOOKS {la['looks']}; the same row at k = {la['k_with_this_row']}")
    for name, cs_ in res["cases"].items():
        L_ += ["", f"CASE {name}: stop {cs_['stop']}, rounds per sham launch {cs_['rounds_per_sham_launch']}, "
                   f"{cs_['n_looks']} looks"]
        L_ += [f"  look {lk['look']}: launches {lk['launches']} (A0 {lk['A0']}, A0s {lk['A0s']})"
               f"{' end' if lk.get('end') else ''}" for lk in cs_["looks"]]
        rd_ = cs_["round_degeneracy"]
        L_.append(f"  round_degeneracy: n_j {rd_['n_j']} crit_j {rd_['crit_j']} false pause "
                  f"{rd_['false_pause']['display']}")
        if "guard" in cs_:
            g_ = cs_["guard"]
            at = g_["at_common_rate_p0"]
            L_.append(f"  guard: (n1, n2)_j {g_['looks_n1_n2']} abs crit_j {g_['abs_crit_j']} Fisher cells_j "
                      f"{g_['fisher_cells_j']}")
            L_.append(f"  guard at the common rate {at['p']}: abs {at['abs']['display']}, Fisher "
                      f"{at['fisher']['display']}, union {at['union']['display']}")
            if "fisher_grid" in g_:
                L_.append("  Fisher half on the grid: " + ", ".join(f"{x['p']}:{x['fisher']['display']}"
                                                                for x in g_["fisher_grid"]))
                L_.append(f"  Fisher grid max {g_['fisher_grid_max']['display']} at p {g_['fisher_grid_max']['p']}; "
                          f"refined {g_['fisher_grid_max_refined']['display']} at p "
                          f"{g_['fisher_grid_max_refined']['p']} (rates {g_['fisher_grid_max_refined']['rates']})")
                L_.append(f"  union grid max over p <= 1/5: {g_['union_grid_max_p_le_p0']['display']} at p "
                          f"{g_['union_grid_max_p_le_p0']['p']}")
    jj = res["joint"]
    L_ += ["", f"JOINT: {jj['figure']}: {jj['value']['display']}; the guard's beside (union at .20): "
               f"{jj['guard_beside']['display']}", f"  {jj['not_computed']}"]
    L_.append("NOT FIGURED: " + "; ".join(f"{k_}: {v_}" for k_, v_ in res["not_figured"].items()))
    L_.append("READINGS:")
    L_ += [f"  - {x}" for x in res["readings"]]
    return L_


def report_problems(res: dict, so: str) -> list[str]:
    """The stdout of report() against the reference rendering, line by line."""
    want, got = reference_report(res), so.splitlines()
    out = [f"line {i + 1}: {g!r} for {w!r}" for i, (w, g) in enumerate(zip(want, got)) if w != g]
    if len(want) != len(got):
        out.append(f"{len(got)} lines for {len(want)}")
    return out


def fixed_problems(res: dict) -> list[str]:
    """The record's fields that no figure moves, against literals of record."""
    want = {("schema",): "m-gpwr-v1", ("unit",): "Q-F0", ("path",): "uncached",
            ("power", "at_floors", "A0"): 80, ("power", "at_floors", "A0s"): 32, ("power", "n_raised"): False,
            ("joint", "figure"): "round_degeneracy's own (projection case)", ("joint", "not_computed"): JOINT_SENTENCE,
            ("not_figured",): {"hair_triggers": "no p0: a ~zero-base-rate class whose fire stops the stage (m:271)",
                               "lexical": "no domain in Q-F0: every banner names labels; reported only (m:330)"}}
    out = []
    for path, val in want.items():
        x = res
        for k_ in path:
            x = x.get(k_) if isinstance(x, dict) else None
        if x != val:
            out.append(".".join(path))
    h = lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest()  # noqa: E731
    pins = {"readings": (lambda r_: h(json.dumps(r_["readings"], ensure_ascii=False)),
                         "526fcfcb79d28bc2c1adeb9abee162cd15f368202f1346d82cee9dda642d0955"),
            "joint.not_computed": (lambda r_: h(r_["joint"]["not_computed"]),
                                   "ad6bae81f5d85491886e9cafaee2468b30179d71d3734fe0bbc08d753764e3a5"),
            "power.at_floors.basis": (lambda r_: h(r_["power"]["at_floors"]["basis"]),
                                      "23c71f8943dcc92c164ea30b3cbb0153909f45210e1d76798ecedd0a3115b56e"),
            "power.pin3_of_record_at_floors.basis": (lambda r_: h(r_["power"]["pin3_of_record_at_floors"]["basis"]),
                                                     "cdc4fe0dc6535e6746cba60a8c12ac3ab0fcd75c5547dcd9d2a48b0859b983e5"),
            "power.at_floors.exact": (lambda r_: h(r_["power"]["at_floors"]["exact"]),
                                      "cf7dd3ea9f9c040c7a1d2bea711764088948654b9316ecd47e40ec1d575d4346"),
            "power.pin3_of_record_at_floors.exact": (lambda r_: h(r_["power"]["pin3_of_record_at_floors"]["exact"]),
                                                     "cf7dd3ea9f9c040c7a1d2bea711764088948654b9316ecd47e40ec1d575d4346"),
            "the record's key paths": (lambda r_: h(json.dumps(_key_paths(r_))),
                                       "1a8e1176bda7e21d7e23156cb580dda7bd9bfccbae32346bf3203ff9f377d7c8"),
            "the record's figures": (lambda r_: h(json.dumps({k_: v_ for k_, v_ in r_.items() if k_ != "provenance"},
                                                             sort_keys=True)),
                                     "a5aaea473b3f940d6b0c92fea745028b36fae87ace4263501de05e12deb7337c")}
    for name_, (f_, want_) in pins.items():           # PIN: the reviewed texts and shape, by sha256 literal
        try:
            if f_(res) != want_:
                out.append(name_)
        except (KeyError, TypeError):
            out.append(name_)
    if not (isinstance(res.get("readings"), list) and len(res["readings"]) == 8):
        out.append("readings")
    return out


def _key_paths(x, p: str = "") -> list[str]:
    """The record's key paths, list indices collapsed: its shape."""
    out = set()
    if isinstance(x, dict):
        for k_, v_ in x.items():
            out.add(p + "/" + k_)
            out |= set(_key_paths(v_, p + "/" + k_))
    elif isinstance(x, list):
        for v_ in x:
            out |= set(_key_paths(v_, p + "[]"))
    return sorted(out)


def _stop_probe(m) -> tuple[bool, list]:
    """compute()'s STOP branches, each provoked by one stub, must stop the run (SystemExit beginning 'STOP')."""
    g = globals()
    missed = []

    def stops() -> bool:
        try:
            compute(m)
        except SystemExit as e:
            return str(e).startswith("STOP")
        return False
    for name, key, val in (("bars", "bar_problems", lambda: ["stub"]), ("power floor", "POWER_FLOOR", Fraction(9, 10)),
                           ("k = 0", "K", 0), ("rounds", "SHAM_ROUNDS_REALISED", (135, 160)),
                           ("looks", "looks_for", lambda total: 99)):
        keep = g[key]
        g[key] = val
        try:
            if not stops():
                missed.append(name)
        finally:
            g[key] = keep
    keep = schedule._n90_launch
    schedule._n90_launch = lambda floor, k, *a, **kw: 0
    try:
        if not stops():
            missed.append("launch cross-check")
    finally:
        schedule._n90_launch = keep
    return not missed, missed


def _record_check_probe(res: dict, so: str) -> tuple[bool, list]:
    """The record checks, each given a record or stdout with one known defect, must report it; the record itself is
    left unchanged."""
    import copy
    before = json.dumps(res, sort_keys=True)
    bad = []
    r_ = copy.deepcopy(res)
    r_["inputs"]["power_alpha"] = "1/100"
    if not inputs_problems(r_):
        bad.append("an extra inputs key")
    global POWER_FLOOR
    keep = POWER_FLOOR
    r_ = copy.deepcopy(res)
    r_["power"]["power_floor"] = "1/2"
    POWER_FLOOR = Fraction(1, 2)
    try:
        if not inputs_problems(r_):
            bad.append("a power floor of 1/2 recorded with the constant set so")
    finally:
        POWER_FLOOR = keep
    r_ = copy.deepcopy(res)
    r_["cases"]["projection"]["guard"]["fisher_grid"][0]["fisher"]["display"] += "0"
    if not display_problems(r_):
        bad.append("a trailing zero")
    last = res["cases"]["projection"]["looks"][-1]
    last_line = (f"  look {last['look']}: launches {last['launches']} (A0 {last['A0']}, A0s {last['A0s']})"
                 f"{' end' if last.get('end') else ''}\n")
    if so.count(last_line) < 1 or not line_problems(res, so.replace(last_line, last_line + last_line, 1)) \
            or not report_problems(res, so.replace(last_line, last_line + last_line, 1)):
        bad.append("a doubled look line")
    for name, path, val in (("degeneracy p0", ("inputs", "round_degeneracy", "p0"), "1/5"),
                            ("look_every", ("inputs", "look_every"), 32)):
        r_ = copy.deepcopy(res)
        x = r_
        for k_ in path[:-1]:
            x = x[k_]
        x[path[-1]] = val
        if not inputs_problems(r_):
            bad.append(name)
    r_ = copy.deepcopy(res)
    r_["power"]["power_floor"] = "1/20"
    if not inputs_problems(r_):
        bad.append("power floor")
    g_ = res["cases"]["projection"]["guard"]
    r_ = copy.deepcopy(res)
    r_["cases"]["projection"]["guard"]["fisher_grid"][0]["fisher"]["display"] = dec(
        Fraction(g_["fisher_grid"][0]["fisher"]["exact"]), 3)
    if not display_problems(r_):
        bad.append("grid entry display")
    r_ = copy.deepcopy(res)
    r_["cases"]["projection"]["guard"]["fisher_grid_max"]["display"] = dec(Fraction(g_["fisher_grid_max"]["exact"]), 3)
    if not display_problems(r_):
        bad.append("grid maximum display")
    lk = res["cases"]["projection"]["looks"][0]
    look_line = f"  look {lk['look']}: launches {lk['launches']} (A0 {lk['A0']}, A0s {lk['A0s']})"
    guard_line = (f"  guard: (n1, n2)_j {g_['looks_n1_n2']} abs crit_j {g_['abs_crit_j']} Fisher cells_j "
                  f"{g_['fisher_cells_j']}")
    jj = res["joint"]
    joint_line = (f"JOINT: {jj['figure']}: {jj['value']['display']}; the guard's beside (union at .20): "
                  f"{jj['guard_beside']['display']}")
    fl = res["cases"]["sham_at_floor_r"]["looks"][2]
    floor_line = f"  look {fl['look']}: launches {fl['launches']} (A0 {fl['A0']}, A0s {fl['A0s']})"
    for name, old, new in (("look suffix", look_line + "\n", look_line + " end\n"),
                           ("guard abs crits", guard_line, guard_line.replace(f"abs crit_j {g_['abs_crit_j']}",
                                                                              f"abs crit_j {g_['fisher_cells_j']}")),
                           ("joint", joint_line, joint_line.replace(f"(union at .20): {jj['guard_beside']['display']}",
                                                                   f"(union at .20): {jj['value']['display']}")),
                           ("floor looks", floor_line, floor_line.replace(f"(A0 {fl['A0']},", "(A0 0,"))):
        if so.count(old) < 1 or not line_problems(res, so.replace(old, new, 1)):
            bad.append(name)
        if so.count(old) < 1 or not report_problems(res, so.replace(old, new, 1)):
            bad.append(name + " (whole report)")
    for name, old, new in (("power line", f"): {res['power']['at_floors']['display']} (", "): 0.8784 ("),
                           ("total line", f"TOTAL {res['launch']['total']};", "TOTAL 191;")):
        if so.count(old) != 1 or not report_problems(res, so.replace(old, new, 1)):
            bad.append(name)
    for name, path, val in (("path", ("path",), "cached"), ("A0 floor", ("power", "at_floors", "A0"), 32),
                            ("readings", ("readings",), READINGS[:-1])):
        r_ = copy.deepcopy(res)
        x = r_
        for k_ in path[:-1]:
            x = x[k_]
        x[path[-1]] = val
        if not fixed_problems(r_):
            bad.append(name)
    if json.dumps(res, sort_keys=True) != before:
        bad.append("the probe changed the record")
    return not bad, bad


def selftest(m) -> int:
    """Every check is guarded (an exception is a FAIL and the rest still run), and so is the shared setup (a failure
    there is a FAIL and ends the self-test). The oracles are literals from the record
    (m:209-214's planning rows, Q7's arithmetic, the floor cases' looks), the bars of record (bars.QF0_BARS'
    evaluate(), critical_k, fisher_sf), brute-force enumeration and independent recomputes; some checks pin the wiring
    only (a figure against the same library call compute() makes), and the PIN displays are regression pins of the
    reviewed run (marked so)."""
    fails = []

    def chk(name, fn):
        ok, detail = _run_check(fn)
        print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  [{str(detail)[:300]!r}]" if detail and not ok else ""))
        if not ok:
            fails.append(name)

    try:                         # the setup the checks share; a failure here is a FAIL, reported, not an abort
        FB, AB, FB_D = _bar(FISHER_BAR), _bar(ABS_BAR), _bar(DEGEN_BAR)
        proj = project({"A0": 128, "A0s": 64})
        pairs = [(lk["A0"], lk["A0s"]) for lk in proj]
        regs = guard_regions(pairs)
        sha = hashlib.sha256((REPO / "scripts" / "m_analyze.py").read_bytes()).hexdigest()
    except Exception as e:  # noqa: BLE001
        print(f"FAIL  the self-test's setup (the bars, the projection, its regions, the analyzer's sha256)  "
              f"[raised {type(e).__name__}: {e}]")
        print("selftest: FAIL (setup failed; no check ran)")
        return 1

    def bar_cells(n1, n2):
        return {(a, c) for a in range(n1 + 1) for c in range(n2 + 1)
                if FB.evaluate(a, n1, sham_k=c, sham_n=n2).exceeds}

    def brute(looks, p, halves, alpha):
        """Every exclusion sequence of both arms, session by session; firing read from bars directly."""
        n1f, n2f = looks[-1]
        tot = Fraction(0)
        for s1 in itertools.product((0, 1), repeat=n1f):
            for s2 in itertools.product((0, 1), repeat=n2f):
                for n1, n2 in looks:
                    a, c = sum(s1[:n1]), sum(s2[:n2])
                    cr = bars.critical_k(n1, GUARD_ABS_P0, alpha)
                    if ("abs" in halves and cr is not None and a >= cr) or \
                            ("fisher" in halves and bars.fisher_sf(a, n1, c, n2) <= alpha):
                        kk = sum(s1) + sum(s2)
                        tot += p ** kk * (1 - p) ** (n1f + n2f - kk)
                        break
        return tot

    # the guard's dynamic programme
    cases = [([(2, 1), (4, 3)], Fraction(1, 5), Fraction(3, 10)),
             ([(1, 1), (3, 2), (3, 2), (5, 4)], Fraction(1, 3), Fraction(1, 4)),
             ([(4, 4)], Fraction(1, 2), Fraction(1, 20)),
             ([(0, 1), (2, 2)], Fraction(1, 5), Fraction(3, 10)),
             ([(3, 3)], Fraction(1, 5), Fraction(1, 20))]          # fisher_sf(3, 3, 0, 3) = 1/20 = alpha: a tie
    for looks, p, al in cases:
        for halves in (("abs",), ("fisher",), ("abs", "fisher")):
            chk(f"guard DP == brute force from bars: looks {looks}, p {p}, alpha {al}, {'+'.join(halves)}",
                lambda: (lambda d, b: (d == b, f"{d} vs {b}"))(guard_false_pause(guard_regions(looks, al), p, halves),
                                                               brute(looks, p, halves, al)))
    chk("brute-force cases include a non-empty Fisher set, an abs fire and an unreachable abs crit",
        lambda: any(len(rg["fisher"]) for rg in guard_regions(cases[0][0], cases[0][2]))
        and any(rg["abs_crit"] is not None for rg in guard_regions(cases[0][0], cases[0][2]))
        and guard_regions(cases[3][0], cases[3][2])[0]["abs_crit"] is None)
    chk("guard regions == the bars' evaluate() at every projection look, at (128, 43), and at the tie look (3, 3) "
        "where fisher_sf(3, 3, 0, 3) = 1/20 = alpha fires",
        lambda: (lambda pr: (not pr, pr))([x for n1, n2 in pairs + [(128, 43), (3, 3)] for x in region_problems(n1, n2)])
        if bars.fisher_sf(3, 3, 0, 3) == Fraction(1, 20) and (3, 0) in bar_cells(3, 3) else (False, "tie case"))
    chk("guard_block: looks, abs crits and Fisher cell counts read from the bars at each projection look",
        lambda: (lambda gb: gb["looks_n1_n2"] == [list(x) for x in pairs]
                 and gb["abs_crit_j"] == [AB.evaluate(0, n1).crit for n1, _ in pairs]
                 and gb["fisher_cells_j"] == [len(bar_cells(n1, n2)) for n1, n2 in pairs])(guard_block(proj, False)))

    def f3():
        at = guard_block(proj, False)["at_common_rate_p0"]
        a_, f_, u = (Fraction(at[k]["exact"]) for k in ("abs", "fisher", "union"))
        return (at["p"] == "1/5" and a_ == bars.seq_false_pause([n1 for n1, _ in pairs], "0.20", "0.05")
                and max(a_, f_) < u <= a_ + f_), at
    chk("guard at .20: the abs half == bars.seq_false_pause on the contrast launches; max(halves) < union <= sum", f3)
    chk("guard DP: p = 0 never fires; a repeated look adds nothing",
        lambda: guard_false_pause(regs, Fraction(0), ("abs", "fisher")) == 0
        and guard_false_pause(guard_regions([(2, 1), (4, 3), (4, 3)], Fraction(3, 10)), Fraction(1, 5), ("abs", "fisher"))
        == guard_false_pause(guard_regions([(2, 1), (4, 3)], Fraction(3, 10)), Fraction(1, 5), ("abs", "fisher")))
    chk("guard DP refuses decreasing looks (both arms or one), an empty or unknown half, p outside [0, 1]",
        lambda: all(_raises(f) for f in (
            lambda: guard_false_pause(guard_regions([(4, 3), (2, 1)]), Fraction(1, 5), ("abs",)),
            lambda: guard_false_pause(guard_regions([(4, 3), (5, 2)]), Fraction(1, 5), ("abs",)),
            lambda: guard_false_pause(guard_regions([(4, 3), (3, 4)]), Fraction(1, 5), ("abs",)),
            lambda: guard_false_pause(regs, Fraction(1, 5), ()),
            lambda: guard_false_pause(regs, Fraction(1, 5), ("lexical",)),
            lambda: guard_false_pause(regs, Fraction(3, 2), ("abs",)))))

    def f9(n1=6, n2=4):
        lk = [{"A0": n1, "A0s": n2}]
        gb = guard_block(lk, with_grid=True)
        rg = [{"n1": n1, "n2": n2, "abs_crit": bars.critical_k(n1, GUARD_ABS_P0, ALPHA), "fisher": bar_cells(n1, n2)}]
        grid = [Fraction(j, 100) for j in range(1, 100)]
        vals = [(guard_false_pause(rg, p, ("fisher",)), p) for p in grid]
        vmax = max(v for v, _ in vals)
        pm = min(p for v, p in vals if v == vmax)
        fine = [q for q in (pm + Fraction(i - 10, 1000) for i in range(21)) if 0 < q < 1]
        fv = [(guard_false_pause(rg, q, ("fisher",)), q) for q in fine]
        fmax = max(v for v, _ in fv)
        ug = [(guard_false_pause(rg, p, ("abs", "fisher")), p) for p in grid if p <= GUARD_ABS_P0]
        um = max(v for v, _ in ug)
        ok = ([x["p"] for x in gb["fisher_grid"]] == [fs(p) for p in grid]
              and Fraction(gb["fisher_grid_max"]["exact"]) == vmax and gb["fisher_grid_max"]["p"] == fs(pm)
              and gb["fisher_grid_max_refined"]["rates"] == [fs(min(fine)), fs(max(fine))]
              and Fraction(gb["fisher_grid_max_refined"]["exact"]) == fmax
              and gb["fisher_grid_max_refined"]["p"] == fs(min(q for v, q in fv if v == fmax))
              and Fraction(gb["union_grid_max_p_le_p0"]["exact"]) == um
              and gb["union_grid_max_p_le_p0"]["p"] == fs(min(p for v, p in ug if v == um)))
        return ok, {k: gb[k] for k in ("fisher_grid_max", "fisher_grid_max_refined", "union_grid_max_p_le_p0")}
    chk("the grid: j/100 for j = 1..99, its maximum, its refinement +/- .01 by .001, the union's maximum over p <= .20, "
        "ties to the smaller rate (two tiny cases, (6, 4) and the all-tie (1, 1), recomputed independently)",
        lambda: (lambda a_, b_: (a_[0] and b_[0], [a_[1], b_[1]]))(f9(), f9(1, 1)))
    chk("ties go to the smaller rate: at looks (1, 1) neither half can fire, every rate ties at 0, and the grid, the "
        "refinement and the union report 1/100, 1/1000 and 1/100",
        lambda: (lambda gb: (gb["fisher_grid_max"]["p"], gb["fisher_grid_max_refined"]["p"],
                             gb["fisher_grid_max_refined"]["rates"], gb["union_grid_max_p_le_p0"]["p"])
                 == ("1/100", "1/1000", ["1/1000", "1/50"], "1/100"))(guard_block([{"A0": 1, "A0s": 1}], True)))

    # the projection and the looks
    chk("the projection: looks at 40, 80, 120, 160 and the end 192; A0 [20, 40, 60, 96, 128], A0s [20, 40, 60, 64, 64]",
        lambda: [lk["launches"] for lk in proj] == [40, 80, 120, 160, 192]
        and [lk["A0"] for lk in proj] == [20, 40, 60, 96, 128] and [lk["A0s"] for lk in proj] == [20, 40, 60, 64, 64])
    chk("the projection: an end on a multiple of 40 adds no look and is flagged the end, once",
        lambda: [(lk["launches"], bool(lk.get("end"))) for lk in project({"A0": 100, "A0s": 60})]
        == [(40, False), (80, False), (120, False), (160, True)])
    chk("the projection refuses an arm with no launch (either arm, or both) and a bool stop",
        lambda: all(_raises(lambda s=s: project(s)) for s in ({"A0": 0, "A0s": 0}, {"A0": 1, "A0s": 0},
                                                              {"A0": 0, "A0s": 1}, {"A0": True, "A0s": 5})))
    chk("looks = ceil(total / 40): 160 -> 4, 192 -> 5, 224 -> 6, 288 -> 8 (m:330, uncached)",
        lambda: [looks_for(t) for t in (160, 192, 224, 288)] == [4, 5, 6, 8])
    chk("round_degeneracy on the projection reproduces bars' self-test figure (.0976, crits 16/28/40/42/42)",
        lambda: degeneracy([200, 400, 600, 640, 640]) == {
            "n_j": [200, 400, 600, 640, 640], "crit_j": [16, 28, 40, 42, 42],
            "false_pause": rec(bars.seq_false_pause([200, 400, 600, 640, 640], "0.05", "0.05"))}
        and degeneracy([200, 400, 600, 640, 640])["false_pause"]["display"] == "0.0976")

    # the launch rule
    def f5():
        bad = [(f, k) for f in (32, 80, 96) for k in range(1, N_Q + 1)
               if not (lambda r, n: bars.binom_sf(f, n, r) >= Fraction(9, 10)
                       and (n == f or bars.binom_sf(f, n - 1, r) < Fraction(9, 10)))(Fraction(k, N_Q),
                                                                                    n90(f, Fraction(k, N_Q)))]
        return not bad, bad[:4]
    chk("n90 is the smallest N with P(Bin(N, r) >= floor) >= .90, floors 32/80/96, r = k/24 for k = 1..24", f5)
    chk("the launch rule == schedule._n90_launch at floors 80, 32 and 96 for k = 1..24",
        lambda: all(launch_count(f, Fraction(k, N_Q))["L"] == schedule._n90_launch(f, k)
                    for f in (80, 32, 96) for k in range(1, N_Q + 1)))
    chk("launch_count's fields at r = 3/4: A0 80/92/114/128, A0s 32/37/48/64 (m:192, m:210)",
        lambda: launch_count(80, Fraction(3, 4)) == {"floor": 80, "ceil_1.15_floor": 92, "N90": 114, "L": 128}
        and launch_count(32, Fraction(3, 4)) == {"floor": 32, "ceil_1.15_floor": 37, "N90": 48, "L": 64})
    spec = {24: 160, 21: 160, 20: 192, 17: 192, 16: 224, 14: 224, 13: 288, 12: 288, 11: 320, 10: 320, 9: 384,
            8: 416, 7: 480, 6: 544, 5: 640, 1: 3168}
    chk("the launch rule reproduces the uncached totals of m:209-214 (24-21: 160; 20-17: 192; 16-14: 224; 13-12: 288; "
        "11-10: 320; 9: 384; 8: 416; 7: 480; 6: 544; 5: 640; 1: 3,168)",
        lambda: all(launch_count(80, Fraction(k, N_Q))["L"] + launch_count(32, Fraction(k, N_Q))["L"] == v
                    for k, v in spec.items()))
    chk("the uncached rows by arm: 24-21 96/64, 20-17 128/64, 16-14 160/64, 13-12 192/96 (m:209-212)",
        lambda: all((launch_count(80, Fraction(k, N_Q))["L"], launch_count(32, Fraction(k, N_Q))["L"]) == v
                    for k, v in {24: (96, 64), 21: (96, 64), 20: (128, 64), 17: (128, 64), 16: (160, 64),
                                 14: (160, 64), 13: (192, 96), 12: (192, 96)}.items()))
    chk("the launch rule refuses k = 0 at its domain guard (m:192), and n90 refuses past its scan bound",
        lambda: "r must be in (0, 1]" in _message(lambda: n90(80, Fraction(0))) and _cap_refuses())
    chk("dec is exact half-up", lambda: dec(Fraction(1, 20)) == "0.0500" and dec(Fraction(5, 10000), 3) == "0.001"
        and dec(Fraction(4999, 10000), 3) == "0.500")
    chk("the constants equal the bars of record (lock §8.2 rows 7-9: p0, alpha, kind, domain, binding)",
        lambda: (not bar_problems(), bar_problems()))
    chk("bar_problems reports each perturbed field of each bar (kind, p0, alpha, domain, binding)", _bar_probe)
    chk("region_problems reports a dropped tie cell, a dropped a = n1 row and an abs crit moved by one", _region_probe)
    chk("the probes themselves detect a blind check: _bar_probe fails against a bar_problems blind to row 7's binding "
        "or cross-wiring rows 7 and 9, _region_probe against a region_problems that reports nothing", _probe_meta)

    # the run path's guards
    chk("draft_problems: the v1.0 draft naming the analyzer passes; another file naming it, or the draft without it, "
        "is refused (R2 3)",
        lambda: draft_problems(f"{DRAFT_HEAD} (x)\n{sha}\n", sha) == ""
        and draft_problems(f"# RESULTS\n{sha}\n", sha) != "" and draft_problems(f"{DRAFT_HEAD}\n", sha) != ""
        and draft_problems(f"# notes\n{DRAFT_HEAD}\n{sha}\n", sha) != ""
        and draft_problems(f"# LOCK-m-F0.md \u2014 v0.3 (draft)\n{sha}\n", sha) != ""
        and draft_problems(f"{DRAFT_HEAD} (x)\n{sha[:16]}\n", sha) != ""
        and draft_problems(f"# LOCK-m-F0.md \u2014 v1.0.1 (d)\n{sha}\n", sha) != ""
        and draft_problems(f"# LOCK-m-F0.md \u2014 v1.0 (draft)\n{sha}\n", sha) == ""
        and draft_problems(f"{DRAFT_HEAD}\n{sha}\n", sha) == ""
        and draft_problems(f"{DRAFT_HEAD} \u2014 x\n{sha}\n", sha) == ""
        and draft_problems(f"\n{DRAFT_HEAD} (x)\n{sha}\n", sha) != ""
        and DRAFT_HEAD == "# LOCK-m-F0.md \u2014 v1.0")
    chk("selftest_refusal passes 0 only, and refuses 1",
        lambda: selftest_refusal(0) == "" and selftest_refusal(1) != "" and selftest_refusal(-1) != "")
    chk("bound_paths binds the script, the analyzer and the package's files",
        lambda: bound_paths(["valence_core/m/bars.py"]) == ["scripts/m_gpwr.py", "scripts/m_analyze.py",
                                                             "valence_core/m/bars.py"])

    def wr():
        import stat
        import tempfile
        kinds = []
        real_fsync = os.fsync
        with tempfile.TemporaryDirectory() as d:
            pth = Path(d) / "r.json"
            (Path(d) / ".r.json.tmp").write_text("stale\n")          # a stale temporary without the pid: no obstacle
            os.fsync = lambda fd: (kinds.append(stat.S_IFMT(os.fstat(fd).st_mode)), real_fsync(fd))[1]
            try:
                write_record(pth, "x\n")
            finally:
                os.fsync = real_fsync
            ok = (pth.read_text() == "x\n" and kinds == [stat.S_IFREG, stat.S_IFDIR]
                  and sorted(os.listdir(d)) == [".r.json.tmp", "r.json"]
                  and _raises(lambda: write_record(pth, "y\n"), (FileExistsError,)) and pth.read_text() == "x\n")
            victim = Path(d) / "victim.txt"
            victim.write_text("intact\n")
            q = Path(d) / "q.json"
            os.symlink(victim, Path(d) / f".q.json.tmp-{os.getpid()}")   # a planted temporary is refused, not followed
            ok = ok and _raises(lambda: write_record(q, "z\n"), (FileExistsError,)) and victim.read_text() == "intact\n" \
                and not q.exists()
            return ok
    chk("write_record writes once (the file, then its directory, fsynced; no temporary left; a stale temporary is no "
        "obstacle), refuses an existing file, and refuses rather than follows a planted temporary", wr)

    def setup_guard():
        global project, _IN_SETUP_PROBE
        if _IN_SETUP_PROBE:          # a re-entry means the inner self-test ran past its failed setup
            return False, "re-entered: the inner self-test ran checks after its setup failed"

        class _SetupProbe(Exception):
            pass
        real = project
        buf = io.StringIO()

        def boom(stop):
            raise _SetupProbe("setup probe")
        project = boom
        _IN_SETUP_PROBE = True
        try:
            with redirect_stdout(buf):
                rc = selftest(m)
        finally:
            project = real
            _IN_SETUP_PROBE = False
        out = buf.getvalue()
        return (rc == 1 and out.count("FAIL") == 2 and "[raised _SetupProbe: setup probe]" in out
                and out.rstrip().endswith("selftest: FAIL (setup failed; no check ran)")
                and "PASS" not in out), out[-300:]
    chk("a failure in the self-test's setup is one FAIL, a FAIL verdict and a non-zero result, and no check runs",
        setup_guard)

    def pv():
        hp = ["valence_core/m/a.py", "valence_core/m/b.py"]
        paths = bound_paths(hp)
        same = {p: "h" + str(i) for i, p in enumerate(paths)}
        ok = provenance_problems(hp, list(hp), same, dict(same)) == []
        bad_hash = dict(same, **{"scripts/m_analyze.py": "x"})
        no_blob = dict(same, **{"valence_core/m/b.py": ""})
        no_disk = dict(same, **{"scripts/m_gpwr.py": ""})
        nc = "not committed at HEAD with identical working-tree bytes"
        return (ok and provenance_problems(hp, hp, same, bad_hash) == [f"scripts/m_analyze.py: {nc}"]
                and provenance_problems(hp, hp, no_blob, same) == [f"valence_core/m/b.py: {nc}"]
                and provenance_problems(hp, hp, same, no_disk) == [f"scripts/m_gpwr.py: {nc}"]
                and provenance_problems(hp, hp + ["valence_core/m/c.py"], same, same)
                == ["valence_core/m/*.py differ from HEAD's tree: ['valence_core/m/c.py']"]
                and provenance_problems(hp, hp[:1], same, same)
                == ["valence_core/m/*.py differ from HEAD's tree: ['valence_core/m/b.py']"]
                and provenance_problems(hp, hp, same, same, ["valence_core/session.py"])
                == [f"valence_core/session.py: {nc}"])
    chk("provenance_problems refuses a differing hash, a missing blob, a missing file, an extra and a missing package "
        "file, and passes an identical set", pv)
    chk("loaded_problems refuses a moved HEAD, an executed blob that is not HEAD's, an executed file not bound and a "
        "module executed from the working tree, and passes executed blobs equal to the bound ones",
        lambda: loaded_problems({"scripts/m_analyze.py": "a1"}, {"scripts/m_analyze.py": "a1"}, "c1", "c1", []) == []
        and loaded_problems({}, {}, "c2", "c1", []) == ["HEAD moved during the run: loaded from c1, now c2"]
        and loaded_problems({"scripts/m_analyze.py": "a2"}, {"scripts/m_analyze.py": "a1"}, "c1", "c1", [])
        == ["scripts/m_analyze.py: executed blob a2 is not HEAD's a1"]
        and loaded_problems({"valence_core/x.py": "x"}, {}, "c1", "c1", [])
        == ["valence_core/x.py: executed but not bound"]
        and loaded_problems({}, {}, "c1", "c1", ["valence_core/x.py"])
        == ["repository modules executed from the working tree, not HEAD's blobs: ['valence_core/x.py']"])
    chk("path_problems requires the repository once, last, with only jlens-qwen36's environment inside it earlier",
        lambda: path_problems([None, "jlens-qwen36/.venv/lib/python3.12/site-packages", "."]) == []
        and path_problems([".", None, "."]) == ["the import path holds repository paths before its last entry: ['.']"]
        and path_problems([None, "scripts"]) == ["the repository is not the import path's last entry"]
        and path_problems([None, "scripts", "."]) == [
            "the import path holds repository paths before its last entry: ['scripts']"]
        and path_problems([_repo_rel(x) for x in sys.path]) == [])

    def pkg_formula():
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            d = Path(td) / "m"
            d.mkdir()
            files = {"m/b.py": b"b = 2\n", "m/a.py": b"a = 1\n", "m/c.py": b""}
            for rel, b in files.items():
                (Path(td) / rel).write_bytes(b)
            (d / "x.txt").write_bytes(b"not a module")
            return _pkg_sha256(list(files.items())) == resume.package_sha256_of(d)
    chk("_pkg_sha256 is resume.package_sha256_of's formula (a scratch package of three files, one empty)", pkg_formula)
    chk("this process executed every repository module it loaded from HEAD's blobs, each blob checked against its id",
        lambda: _from_tree() == [] and "scripts/m_analyze.py" in _LOADED and "valence_core/m/bars.py" in _LOADED
        and all(_blob_id(_head_blob(r), o) == o for r, o in list(_LOADED.items())))
    chk("tree_problems refuses a file HEAD's tree lacks and a symlink, and passes an identical tree",
        lambda: tree_problems(["valence_core/a.py"], ["valence_core/a.py"], []) == []
        and tree_problems(["valence_core/a.py"], ["valence_core/a.py", "valence_core/m/resume/__init__.py"], [])
        == ["valence_core/ holds files HEAD's tree does not: ['valence_core/m/resume/__init__.py']"]
        and tree_problems(["valence_core/a.py"], ["valence_core/a.py"], ["valence_core/stats.py"])
        == ["valence_core/ holds symlinks: ['valence_core/stats.py']"])
    chk("the package tree on disk equals HEAD's here (no extra file, no symlink)",
        lambda: (lambda pr: (not pr, pr))(tree_problems(
            _git("ls-tree", "-r", "--name-only", _LOAD_COMMIT, "valence_core/").split(), *_tree_on_disk())))

    # compute() itself, against the oracles
    try:
        res = compute(m)
        buf = io.StringIO()
        with redirect_stdout(buf):
            report(res)
        so = buf.getvalue()
    except BaseException as e:  # noqa: BLE001 -- includes compute()'s SystemExit STOPs
        res, so = None, f"{type(e).__name__}: {e}"
    chk("compute() completes and report() prints", lambda: (res is not None, so[:300]))
    if res is not None:
        cs = res["cases"]
        chk("the record's JSON form (resume.json_text) accepts compute()'s result",
            lambda: json.loads(resume.json_text(res, indent=1))["unit"] == "Q-F0")
        chk("inputs: k 18 of 24, r 3/4, floors 80/32 (the G-F0m-Qwen entry; v0.2 §1)",
            lambda: (res["inputs"]["k"], res["inputs"]["n_q"], res["inputs"]["r"], res["inputs"]["floors"])
            == (18, 24, "3/4", {"A0": 80, "A0s": 32}))
        chk("power at the floors .878 (.8784) by the analyzer's power_exact; PIN-3 split [40, 40], mS 32 (m:190)",
            lambda: res["power"]["at_floors"]["display"] == "0.878" and res["power"]["at_floors"]["exact4"] == "0.8784"
            and Fraction(res["power"]["at_floors"]["exact"]) == m.power_exact(40, 40, 32) >= POWER_FLOOR
            and res["power"]["pin3_of_record_at_floors"]["split"] == [40, 40]
            and res["power"]["pin3_of_record_at_floors"]["mS"] == 32 and res["power"]["n_raised"] is False)
        chk("the planning row of m:210: L 128/64, total 192, 5 looks, the same row at k = 17..20",
            lambda: res["launch"]["L"] == {"A0": 128, "A0s": 64} and res["launch"]["total"] == 192
            and res["launch"]["looks"] == 5 and res["launch"]["k_with_this_row"] == [17, 18, 19, 20]
            and res["launch"]["rule"] == {"A0": launch_count(80, Fraction(3, 4)), "A0s": launch_count(32, Fraction(3, 4))})
        chk("rows_by_k: k = 1..24, each with m:209-214's total where the proposal gives one, and m:209-212's looks "
            "(4 at 24-21, 5 at 20-17, 6 at 16-14, 8 at 13-12)",
            lambda: sorted(int(k) for k in res["launch"]["rows_by_k"]) == list(range(1, 25))
            and all(res["launch"]["rows_by_k"][str(k)]["total"] == v for k, v in spec.items())
            and all(res["launch"]["rows_by_k"][str(k)]["looks"] == lk for ks, lk in
                    ((range(21, 25), 4), (range(17, 21), 5), (range(14, 17), 6), (range(12, 14), 8)) for k in ks))
        chk("rows_by_k: every k = 1..24 is {A0: _n90_launch(80, k), A0s: _n90_launch(32, k), total, ceil(total/40)}",
            lambda: all(res["launch"]["rows_by_k"][str(k)] == {
                "A0": schedule._n90_launch(80, k), "A0s": schedule._n90_launch(32, k),
                "total": schedule._n90_launch(80, k) + schedule._n90_launch(32, k),
                "looks": -(-(schedule._n90_launch(80, k) + schedule._n90_launch(32, k)) // 40)} for k in range(1, 25)))
        chk("per-template rates beside: A0 7/8, A0s 11/16, pooling to 18 of 24 (the G-F0m-Qwen entry)",
            lambda: res["inputs"]["per_template_beside"] == {"A0": "7/8", "A0s": "11/16"} and 7 + 11 == 18 and 8 + 16 == 24)
        chk("the inputs block and the power floor, whole: p0s and alphas from the bars of record, the rest literal",
            lambda: (lambda pr: (not pr, pr))(inputs_problems(res)))
        chk("every {exact, display} pair in the record displays its exact value half-up (4 places; power 3)",
            lambda: (lambda pr: (not pr, pr[:5]))(display_problems(res)))
        chk("report()'s labelled lines carry the record's values in their places (launch, looks, round_degeneracy, "
            "guard, grid maxima, joint), each as a whole line", lambda: (lambda pr: (not pr, pr[:3]))(line_problems(res, so)))
        chk("report()'s whole stdout equals the reference rendering of the record, line by line",
            lambda: (lambda pr: (not pr, pr[:3]))(report_problems(res, so)))
        chk("the record's fixed fields (schema, unit, path, the floors in the power block, n_raised, the joint's figure "
            "and sentence, not_figured, the power basis, READINGS) equal their literals of record",
            lambda: (lambda pr: (not pr, pr))(fixed_problems(res)))
        chk("compute() stops at each of its STOP branches (bars, power floor, k = 0, the launch cross-check, "
            "non-integer rounds, the look count)", lambda: _stop_probe(m))
        chk("the three record checks report a perturbed record: inputs (degeneracy p0, power floor, look_every), "
            "displays (a grid entry, the grid maximum), lines (a look line's suffix, the guard's abs crits, the joint, "
            "a floor case's looks)", lambda: _record_check_probe(res, so))
        chk("the floor cases' looks, literally (Q7 (a)): at 43, A0 [20, 40, 77, 117, 128] and A0s [20, 40, 43, 43, 43]; "
            "at 32, A0 [20, 48, 88, 128] and A0s [20, 32, 32, 32]",
            lambda: [(lk["A0"], lk["A0s"]) for lk in cs["sham_at_floor_r"]["looks"]]
            == [(20, 20), (40, 40), (77, 43), (117, 43), (128, 43)]
            and [(lk["A0"], lk["A0s"]) for lk in cs["sham_at_floor_min"]["looks"]] == [(20, 20), (48, 32), (88, 32), (128, 32)])
        chk("PIN-3 at the floors is labelled a planning figure, not the VERDICTS figure of record",
            lambda: "planned floors" in res["power"]["pin3_of_record_at_floors"]["basis"]
            and "VERDICTS" in res["power"]["pin3_of_record_at_floors"]["basis"])
        chk("the cases' stops and rounds per sham launch (Q7 (a): L; ceil(32/r) = 43; 32; 136/160 x 10 = 17/2)",
            lambda: [cs[k]["stop"] for k in ("projection", "sham_at_floor_r", "sham_at_floor_min",
                                             "sham_realised_rounds")]
            == [{"A0": 128, "A0s": 64}, {"A0": 128, "A0s": 43}, {"A0": 128, "A0s": 32}, {"A0": 128, "A0s": 64}]
            and [cs[k]["rounds_per_sham_launch"] for k in cs] == ["10", "10", "10", "17/2"])
        chk("n_j = sham launches x rounds per launch at every look of every case; the end flagged once, last",
            lambda: all(cs[k]["round_degeneracy"]["n_j"] == [int(lk["A0s"] * Fraction(cs[k]["rounds_per_sham_launch"]))
                                                             for lk in cs[k]["looks"]]
                        and [bool(lk.get("end")) for lk in cs[k]["looks"]]
                        == [False] * (len(cs[k]["looks"]) - 1) + [True]
                        and cs[k]["looks"] == project(cs[k]["stop"]) for k in cs))
        chk("round_degeneracy per case == bars.seq_false_pause on its n_j at p0 .05, alpha .05",
            lambda: all(Fraction(cs[k]["round_degeneracy"]["false_pause"]["exact"])
                        == bars.seq_false_pause(cs[k]["round_degeneracy"]["n_j"], "0.05", "0.05") for k in cs))
        chk("the guard in the three launch cases, the grid in the projection only; looks (A0, A0s); abs == "
            "bars.seq_false_pause on A0's launches",
            lambda: [("guard" in cs[k], "fisher_grid" in cs[k].get("guard", {})) for k in cs]
            == [(True, True), (True, False), (True, False), (False, False)]
            and all(cs[k]["guard"]["looks_n1_n2"] == [[lk["A0"], lk["A0s"]] for lk in cs[k]["looks"]]
                    and Fraction(cs[k]["guard"]["at_common_rate_p0"]["abs"]["exact"])
                    == bars.seq_false_pause([lk["A0"] for lk in cs[k]["looks"]], "0.20", "0.05")
                    for k in cs if "guard" in cs[k]))
        def at_rate():
            bad = []
            for name_, cs_ in cs.items():
                if "guard" not in cs_:
                    continue
                pr_ = [(lk["A0"], lk["A0s"]) for lk in cs_["looks"]]
                rg_ = [{"n1": n1, "n2": n2, "abs_crit": AB.evaluate(0, n1).crit, "fisher": bar_cells(n1, n2)}
                       for n1, n2 in pr_]
                at_ = cs_["guard"]["at_common_rate_p0"]
                for half, hs in (("abs", ("abs",)), ("fisher", ("fisher",)), ("union", ("abs", "fisher"))):
                    if Fraction(at_[half]["exact"]) != guard_false_pause(rg_, GUARD_ABS_P0, hs):
                        bad.append(f"{name_}.{half}")
            grid_20 = [x for x in cs["projection"]["guard"]["fisher_grid"] if x["p"] == "1/5"]
            if not grid_20 or grid_20[0]["fisher"] != cs["projection"]["guard"]["at_common_rate_p0"]["fisher"]:
                bad.append("projection: the Fisher half at .20 differs from its grid entry at 1/5")
            return not bad, bad
        chk("the guard at .20 in every case: abs, Fisher and union each equal the DP on regions read from the bars, with "
            "their own halves; the projection's Fisher half equals its grid entry at 1/5", at_rate)
        chk("every case records as many looks as it lists (n_looks), numbered 1..n; literally 5, 5, 4 and 5 looks",
            lambda: all(cs_["n_looks"] == len(cs_["looks"]) and [lk["look"] for lk in cs_["looks"]]
                        == list(range(1, len(cs_["looks"]) + 1)) for cs_ in cs.values())
            and [cs_["n_looks"] for cs_ in cs.values()] == [5, 5, 4, 5])
        chk("the joint is the projection's round_degeneracy, the guard's union beside",
            lambda: res["joint"]["value"] == cs["projection"]["round_degeneracy"]["false_pause"]
            and res["joint"]["guard_beside"] == cs["projection"]["guard"]["at_common_rate_p0"]["union"])
        chk("PIN (regression, the reviewed run's displays): round_degeneracy .0976/.0797/.0593/.0890; guard union "
            ".1496/.1461/.1343",
            lambda: [cs[k]["round_degeneracy"]["false_pause"]["display"] for k in cs]
            == ["0.0976", "0.0797", "0.0593", "0.0890"]
            and [cs[k]["guard"]["at_common_rate_p0"]["union"]["display"] for k in cs if "guard" in cs[k]]
            == ["0.1496", "0.1461", "0.1343"])
        chk("report() prints every case's figures as recorded",
            lambda: all(f"false pause {cs[k]['round_degeneracy']['false_pause']['display']}" in so for k in cs)
            and all(f"abs {cs[k]['guard']['at_common_rate_p0']['abs']['display']}, Fisher "
                    f"{cs[k]['guard']['at_common_rate_p0']['fisher']['display']}, union "
                    f"{cs[k]['guard']['at_common_rate_p0']['union']['display']}" in so for k in cs if "guard" in cs[k])
            and f"L {res['launch']['L']['A0']}" in so and f"TOTAL {res['launch']['total']}; LOOKS 5" in so)
    chk("the harness counts a check that raises, or returns a false value, as a FAIL",
        lambda: _run_check(lambda: 1 / 0)[0] is False and _run_check(lambda: (False, "x"))[0] is False
        and _run_check(lambda: 0)[0] is False and _run_check(lambda: True)[0] is True)
    print(f"selftest: {'PASS' if not fails else 'FAIL'} ({len(fails)} failed)")
    return 0 if not fails else 1


def _run_check(fn) -> tuple[bool, str]:
    """A check's verdict: a raised exception is a FAIL with its message, not an abort."""
    try:
        r = fn()
        ok, detail = r if isinstance(r, tuple) else (r, "")
    except Exception as e:  # noqa: BLE001
        ok, detail = False, f"raised {type(e).__name__}: {e}"
    return bool(ok), detail


def _bar_probe() -> tuple[bool, list]:
    """bar_problems against stand-in bars (plain records of the compared fields), each with one field perturbed."""
    from types import SimpleNamespace
    global _bar
    real = _bar
    bad = []
    try:
        for name, fields in ((DEGEN_BAR, ("kind", "p0q", "alphaq", "domain", "binding")),
                             (FISHER_BAR, ("kind", "alphaq", "domain", "binding")),
                             (ABS_BAR, ("kind", "p0q", "alphaq", "domain", "binding"))):
            for fld in fields:
                orig = real(name)
                base = {k: getattr(orig, k) for k in ("kind", "p0q", "alphaq", "domain", "binding")}
                val = {"kind": "hair_trigger", "p0q": Fraction(1, 2), "alphaq": Fraction(1, 2), "domain": "every",
                       "binding": not orig.binding}[fld]
                pert = SimpleNamespace(**dict(base, **{fld: val}))
                _bar = (lambda n, _p=pert, _n=name: _p if n == _n else real(n))  # noqa: E731
                if not any(pr.startswith(name + ":") for pr in bar_problems()):
                    bad.append((name, fld))
    finally:
        _bar = real
    return not bad, bad


def _probe_meta() -> tuple[bool, list]:
    """_bar_probe and _region_probe, each run against a defective check, must report failure."""
    global bar_problems, region_problems
    real_bp, real_rp = bar_problems, region_problems
    bad = []

    def blind_binding():
        return [p for p in real_bp() if not p.startswith(DEGEN_BAR)] + (
            [f"{DEGEN_BAR}: x"] if _bar(DEGEN_BAR).p0q != DEGEN_P0 or _bar(DEGEN_BAR).kind != "binomial_look"
            or _bar(DEGEN_BAR).alphaq != ALPHA or _bar(DEGEN_BAR).domain != "sham" else [])

    def cross_wired():
        a = _bar(ABS_BAR)
        out = [p for p in real_bp() if not p.startswith(ABS_BAR)]
        if (a.kind, a.p0q, a.alphaq, a.domain, _bar(DEGEN_BAR).binding) != ("guard_abs", GUARD_ABS_P0, ALPHA,
                                                                              "contrast_arm", True):
            out.append(f"{ABS_BAR}: x")
        return out
    try:
        for name, stub in (("blind to row 7's binding", blind_binding), ("rows 7 and 9 cross-wired", cross_wired)):
            bar_problems = stub
            if _bar_probe()[0]:
                bad.append(name)
        bar_problems = real_bp
        region_problems = lambda n1, n2: []  # noqa: E731
        if _region_probe()[0]:
            bad.append("region_problems reporting nothing")
    finally:
        bar_problems, region_problems = real_bp, real_rp
    return not bad, bad


def _region_probe() -> tuple[bool, list]:
    """region_problems against guard_regions with one defect each."""
    global guard_regions
    real = guard_regions
    bad = []

    def drop_tie(looks, alpha=ALPHA, abs_p0=GUARD_ABS_P0):
        out = real(looks, alpha, abs_p0)
        for r in out:
            r["fisher"] = r["fisher"] - {(3, 0)}
        return out

    def drop_top(looks, alpha=ALPHA, abs_p0=GUARD_ABS_P0):
        out = real(looks, alpha, abs_p0)
        for r in out:
            r["fisher"] = {(a, c) for a, c in r["fisher"] if a != r["n1"]}
        return out

    def crit_up(looks, alpha=ALPHA, abs_p0=GUARD_ABS_P0):
        out = real(looks, alpha, abs_p0)
        for r in out:
            r["abs_crit"] = None if r["abs_crit"] is None else r["abs_crit"] + 1
        return out
    try:
        for name, f, look in (("tie", drop_tie, (3, 3)), ("a = n1", drop_top, (20, 20)), ("abs crit", crit_up, (20, 20))):
            guard_regions = f
            if not region_problems(*look):
                bad.append(name)
    finally:
        guard_regions = real
    return not bad, bad


def _message(f) -> str:
    try:
        f()
    except ValueError as e:
        return str(e)
    return ""


def _cap_refuses() -> bool:
    global N90_CAP
    keep = N90_CAP
    try:
        N90_CAP = 100
        return "past 100" in _message(lambda: n90(80, Fraction(1, 24)))
    finally:
        N90_CAP = keep


def _raises(f, kinds=(ValueError, TypeError)) -> bool:
    try:
        f()
    except kinds:
        return True
    return False


# --- provenance and output ------------------------------------------------------------------------
def _git(*args) -> str:
    return _gitrun(*args, text=True, check=True).stdout


def draft_problems(text: str, analyzer_sha256: str) -> str:
    """R2 3's order: the file offered is the LOCK v1.0 draft, and it names the analyzer's sha256 in full."""
    first = text.split("\n", 1)[0]
    if not (first == DRAFT_HEAD or first.startswith(DRAFT_HEAD + " ")):
        return f"the --lock-draft file does not begin {DRAFT_HEAD!r}: it is not the LOCK v1.0 draft (R2 3)"
    if analyzer_sha256 not in text:
        return "the LOCK v1.0 draft does not name the analyzer's sha256 in full (R2 3)"
    return ""


def selftest_refusal(rc: int) -> str:
    """The run of record's gate: any non-zero self-test result refuses the run."""
    return "" if rc == 0 else "REFUSED: the self-test failed"


def write_record(path: Path, text: str) -> None:
    """Write-once, atomic and durable: the text goes to a temporary file in the same directory, fsynced, then is
    hard-linked to the path (refused if the path exists), the temporary file removed and the directory fsynced."""
    path = Path(path)
    tmp = path.parent / f".{path.name}.tmp-{os.getpid()}"
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.link(tmp, path)
    finally:
        os.unlink(tmp)
    dfd = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(dfd)
    finally:
        os.close(dfd)


def bound_paths(head_pkg: list[str]) -> list[str]:
    """The files the run of record binds: the script, the analyzer and the package's files in HEAD's tree."""
    return ["scripts/m_gpwr.py", "scripts/m_analyze.py"] + list(head_pkg)


def closure_files() -> list[str]:
    """The repository's own modules loaded in this process, as paths relative to REPO, other than the script, the
    analyzer and valence_core/m (bound by name): valence_core's other modules and anything else under REPO, the
    gitignored jlens-qwen36 clone and its environment excluded."""
    roots = (REPO.resolve(), Path(os.path.abspath(REPO)))
    bound_pkg = {p.relative_to(REPO).as_posix() for p in (REPO / "valence_core" / "m").glob("*.py")
                 if not p.is_symlink()}
    out = set()
    for mod in list(sys.modules.values()):
        f = getattr(mod, "__file__", None)
        if not f:
            continue
        rel = None
        for cand in (Path(os.path.abspath(f)), Path(f).resolve()):   # the path as loaded, and where it resolves
            for root in roots:
                try:
                    rel = cand.relative_to(root).as_posix()
                    break
                except ValueError:
                    continue
            if rel is not None:
                break
        if rel is None:
            continue
        if rel.startswith("jlens-qwen36/") or rel in ("scripts/m_gpwr.py", "scripts/m_analyze.py") or rel in bound_pkg:
            continue
        out.add(rel)
    return sorted(out)


def tree_problems(head_files: list[str], disk_files: list[str], symlinks: list[str]) -> list[str]:
    """The importable package tree, valence_core/, on disk against HEAD's: no file HEAD's tree lacks (bytecode caches
    aside, which a run of record never reads), and no symlink. A module can disguise its own __file__ and __spec__; the
    tree cannot."""
    extra = sorted(set(disk_files) - set(head_files))
    out = [f"valence_core/ holds files HEAD's tree does not: {extra}"] if extra else []
    if symlinks:
        out.append(f"valence_core/ holds symlinks: {sorted(symlinks)}")
    return out


def _tree_on_disk() -> tuple[list[str], list[str]]:
    files, links = [], []
    for dirpath, dirnames, filenames in os.walk(REPO / "valence_core", followlinks=False):
        dirnames[:] = [d for d in dirnames if d != "__pycache__" or os.path.islink(os.path.join(dirpath, d))]
        for name in dirnames + filenames:
            full = os.path.join(dirpath, name)
            if os.path.islink(full):
                links.append(Path(full).relative_to(REPO).as_posix())
        files += [Path(dirpath, f).relative_to(REPO).as_posix() for f in filenames]
    return sorted(files), sorted(links)


def provenance_problems(head_pkg: list[str], disk_pkg: list[str], blobs: dict, disk: dict,
                        closure: list[str] = ()) -> list[str]:
    """The run of record's binding decision on its inputs: the package's file list in HEAD's tree equals the one on
    disk, and every bound file -- the script, the analyzer, the package, and the closure of other repository modules
    the process loaded -- has a HEAD blob equal to its working-tree hash ("" = absent)."""
    probs = [] if sorted(head_pkg) == sorted(disk_pkg) else [
        f"valence_core/m/*.py differ from HEAD's tree: {sorted(set(head_pkg) ^ set(disk_pkg))}"]
    for rel in bound_paths(sorted(head_pkg)) + list(closure):
        if not blobs.get(rel) or blobs.get(rel) != disk.get(rel):
            probs.append(f"{rel}: not committed at HEAD with identical working-tree bytes")
    return probs


def loaded_problems(loaded: dict, blobs: dict, head_now: str, head_at_load: str, from_tree: list[str]) -> list[str]:
    """The bytes executed are the bytes bound: HEAD has not moved since the modules were loaded; every repository
    module this process executed from a blob is a bound file whose HEAD blob is that blob; no repository module
    (the script aside, which Python reads at launch) was executed from the working tree."""
    out = [] if head_now == head_at_load else [f"HEAD moved during the run: loaded from {head_at_load}, now {head_now}"]
    for rel, oid in sorted(loaded.items()):
        if rel not in blobs:
            out.append(f"{rel}: executed but not bound")
        elif blobs[rel] != oid:
            out.append(f"{rel}: executed blob {oid} is not HEAD's {blobs[rel]}")
    if from_tree:
        out.append(f"repository modules executed from the working tree, not HEAD's blobs: {sorted(from_tree)}")
    return out


def _from_tree() -> list[str]:
    """The repository's modules (the jlens-qwen36 clone and the script itself aside) not executed from a blob."""
    out = []
    for name, mod in list(sys.modules.items()):
        f = getattr(mod, "__file__", None)
        if not f or name == "__main__" or isinstance(getattr(mod, "__loader__", None), _HeadBlobLoader):
            continue
        for cand in (Path(os.path.abspath(f)), Path(f).resolve()):
            try:
                rel = cand.relative_to(Path(os.path.abspath(REPO))).as_posix()
            except ValueError:
                try:
                    rel = cand.relative_to(REPO.resolve()).as_posix()
                except ValueError:
                    continue
            if not rel.startswith("jlens-qwen36/") and rel != "scripts/m_gpwr.py":
                out.append(rel)
            break
    return sorted(set(out))


def path_problems(rels: list) -> list[str]:
    """The import path's entries, each relative to REPO (None outside it): the repository enters once, as the last
    entry, and nothing else inside it does but the jlens-qwen36 environment's site-packages."""
    out = [] if rels and rels[-1] == "." else ["the repository is not the import path's last entry"]
    early = [r for r in rels[:-1] if r is not None and not r.startswith("jlens-qwen36/")]
    if early:
        out.append(f"the import path holds repository paths before its last entry: {early}")
    return out


def _pkg_sha256(entries: list) -> str:
    """resume.package_sha256_of's formula (its PIN, LOCK v0.1) over (rel, bytes) pairs: sorted, each contributing
    "{rel}\\n{len}\\n" and its bytes."""
    h = hashlib.sha256()
    for rel, data in sorted(entries):
        h.update(f"{rel}\n{len(data)}\n".encode("utf-8"))
        h.update(data)
    return h.hexdigest()


def _blob_bytes(oid: str) -> bytes:
    data = _gitrun("cat-file", "blob", oid, check=True).stdout
    if _blob_id(data, oid) != oid:
        raise SystemExit(f"REFUSED: the bytes read do not hash to the blob {oid}")
    return data


def provenance(lock_draft: Path, draft_bytes: bytes) -> dict:
    """The run of record binds committed blobs only: the script, the analyzer and every valence_core/m/*.py in HEAD's
    tree, each with working-tree bytes equal to its blob, and no other .py file in valence_core/m; every repository
    module executed was executed from those blobs. The sha256 recorded are of HEAD's blob bytes (the package's by
    its own formula, and equal to its value on disk); the draft's is of the bytes draft_problems reads."""
    head_pkg = sorted(p for p in _git("ls-tree", "--name-only", _LOAD_COMMIT, "valence_core/m/").split()
                      if p.endswith(".py"))
    disk_pkg = sorted(str(p.relative_to(REPO)) for p in (REPO / "valence_core" / "m").glob("*.py"))
    closure = closure_files()
    blobs, disk = {}, {}
    for rel in bound_paths(head_pkg) + closure:
        blobs[rel] = _gitrun("rev-parse", f"{_LOAD_COMMIT}:{rel}", text=True).stdout.strip()
        disk[rel] = (_gitrun("hash-object", "--no-filters", "--", rel, text=True).stdout.strip()
                     if (REPO / rel).is_file() and not (REPO / rel).is_symlink() else "")
    probs = provenance_problems(head_pkg, disk_pkg, blobs, disk, closure)
    probs += loaded_problems(_LOADED, blobs, _git("rev-parse", "HEAD").strip(), _LOAD_COMMIT, _from_tree())
    head_tree = _git("ls-tree", "-r", "--name-only", _LOAD_COMMIT, "valence_core/").split()
    probs += tree_problems(head_tree, *_tree_on_disk())
    probs += path_problems([_repo_rel(x) for x in sys.path])
    if os.environ.get("PYTHONPATH"):
        probs.append(f"PYTHONPATH is set ({os.environ['PYTHONPATH']!r}): the run of record loads nothing from outside the "
                     f"repository and its environment")
    if probs:
        raise SystemExit("REFUSED: G-PWR of record binds committed blobs only:\n  " + "\n  ".join(probs))
    data = {rel: _blob_bytes(blobs[rel]) for rel in bound_paths(head_pkg) + closure}
    sha = lambda rel: hashlib.sha256(data[rel]).hexdigest()  # noqa: E731
    pkg = _pkg_sha256([(rel, data[rel]) for rel in head_pkg])
    if pkg != resume.package_sha256():
        raise SystemExit(f"REFUSED: the package's sha256 over HEAD's blobs {pkg} is not its value on disk "
                         f"{resume.package_sha256()}")
    return {"head": _LOAD_COMMIT, "script_sha256": sha("scripts/m_gpwr.py"),
            "analyzer_sha256": sha("scripts/m_analyze.py"), "package_sha256": pkg,
            "lock_draft": {"path": str(lock_draft), "sha256": hashlib.sha256(draft_bytes).hexdigest()},
            "closure": {rel: sha(rel) for rel in closure}, "isolated": bool(sys.flags.isolated),
            "pycache_prefix": sys.pycache_prefix,
            "python": sys.version.split()[0]}


def report(res: dict) -> None:
    p = res["power"]["at_floors"]
    print(f"G-PWR {res['unit']} ({res['path']}); k = {res['inputs']['k']} of {res['inputs']['n_q']}, r = "
          f"{res['inputs']['r']} (A0 {res['inputs']['per_template_beside']['A0']}, A0s "
          f"{res['inputs']['per_template_beside']['A0s']} beside)")
    print(f"POWER at the floors (A0 {p['A0']}, A0s {p['A0s']}): {p['display']} ({p['exact4']}) >= .85; no n raised")
    print(f"PIN-3 of record at the floors: {res['power']['pin3_of_record_at_floors']['display']} "
          f"split {res['power']['pin3_of_record_at_floors']['split']} mS {res['power']['pin3_of_record_at_floors']['mS']}")
    for a, lr in res["launch"]["rule"].items():
        print(f"LAUNCH {a}: floor {lr['floor']}, ceil(1.15 floor) {lr['ceil_1.15_floor']}, N90 {lr['N90']} -> L {lr['L']}")
    print(f"TOTAL {res['launch']['total']}; LOOKS {res['launch']['looks']}; the same row at k = "
          f"{res['launch']['k_with_this_row']}")
    for name, cs in res["cases"].items():
        print(f"\nCASE {name}: stop {cs['stop']}, rounds per sham launch {cs['rounds_per_sham_launch']}, "
              f"{cs['n_looks']} looks")
        for lk in cs["looks"]:
            print(f"  look {lk['look']}: launches {lk['launches']} (A0 {lk['A0']}, A0s {lk['A0s']})"
                  f"{' end' if lk.get('end') else ''}")
        rd = cs["round_degeneracy"]
        print(f"  round_degeneracy: n_j {rd['n_j']} crit_j {rd['crit_j']} false pause {rd['false_pause']['display']}")
        if "guard" in cs:
            g = cs["guard"]
            at = g["at_common_rate_p0"]
            print(f"  guard: (n1, n2)_j {g['looks_n1_n2']} abs crit_j {g['abs_crit_j']} Fisher cells_j {g['fisher_cells_j']}")
            print(f"  guard at the common rate {at['p']}: abs {at['abs']['display']}, Fisher {at['fisher']['display']}, "
                  f"union {at['union']['display']}")
            if "fisher_grid" in g:
                print("  Fisher half on the grid: " + ", ".join(f"{x['p']}:{x['fisher']['display']}"
                                                            for x in g["fisher_grid"]))
                print(f"  Fisher grid max {g['fisher_grid_max']['display']} at p {g['fisher_grid_max']['p']}; refined "
                      f"{g['fisher_grid_max_refined']['display']} at p {g['fisher_grid_max_refined']['p']} "
                      f"(rates {g['fisher_grid_max_refined']['rates']})")
                print(f"  union grid max over p <= 1/5: {g['union_grid_max_p_le_p0']['display']} at p "
                      f"{g['union_grid_max_p_le_p0']['p']}")
    j = res["joint"]
    print(f"\nJOINT: {j['figure']}: {j['value']['display']}; the guard's beside (union at .20): {j['guard_beside']['display']}")
    print(f"  {j['not_computed']}")
    print("NOT FIGURED: " + "; ".join(f"{k}: {v}" for k, v in res["not_figured"].items()))
    print("READINGS:")
    for x in res["readings"]:
        print(f"  - {x}")


_CHILD_BOOT = """\
import hashlib, os, subprocess, sys, types
repo, commit = sys.argv[1], sys.argv[2]
env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
g = ["git", "--no-replace-objects", "-C", repo]
oid = subprocess.run(g + ["rev-parse", "--verify", commit + ":scripts/m_gpwr.py"], env=env, capture_output=True,
                     text=True, check=True).stdout.strip()
src = subprocess.run(g + ["cat-file", "blob", oid], env=env, capture_output=True, check=True).stdout
if hashlib.new("sha1" if len(oid) == 40 else "sha256", b"blob %d\\0" % len(src) + src).hexdigest() != oid:
    raise SystemExit("REFUSED: the self-test's script does not hash to its blob")
path = os.path.join(repo, "scripts", "m_gpwr.py")
mod = types.ModuleType("__main__")
mod.__file__, mod._GPWR_COMMIT = path, commit
sys.modules["__main__"], sys.argv = mod, [path, "--selftest"]
exec(compile(src, path, "exec", dont_inherit=True), mod.__dict__)
"""                                                    # the self-test runs the script's blob at the load commit


def main(argv=None) -> int:
    try:
        return _main(argv)
    except _GitFailed as e:                             # stated, not a traceback: nothing is written
        raise SystemExit(f"REFUSED: {e}")


def _main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--lock-draft", type=Path, help="the LOCK v1.0 draft that names the analyzer (R2 3's order)")
    ap.add_argument("--record", type=Path, help="write the G-PWR JSON here (required for a run; refused if it exists)")
    a = ap.parse_args(argv)
    try:
        m = _analyzer()
    except ImportError as e:
        raise SystemExit(f"REFUSED: {e}")
    if a.selftest:
        return selftest(m)
    if a.lock_draft is None or a.record is None:
        ap.error("a run of record needs --lock-draft (R2 3: the draft names the analyzer before G-PWR runs) and "
                 "--record (rule 27: the record is committed)")
    if a.record.exists() or a.record.is_symlink():
        raise SystemExit(f"REFUSED: {a.record} exists (write-once)")
    if not (a.record.parent.is_dir() and os.access(a.record.parent, os.W_OK)):
        raise SystemExit(f"REFUSED: {a.record.parent} is not a writable directory")
    name_max = os.pathconf(a.record.parent, "PC_NAME_MAX")
    if len(f".{a.record.name}.tmp-{os.getpid()}".encode()) > name_max:
        raise SystemExit(f"REFUSED: the record's name is too long for its temporary file (limit {name_max} bytes)")
    if not sys.flags.isolated:
        raise SystemExit("REFUSED: a run of record runs in isolated mode (python -I): no script directory, user site or "
                         "environment path enters the import path")
    if not sys.pycache_prefix or os.path.exists(sys.pycache_prefix):
        raise SystemExit("REFUSED: a run of record reads no cached bytecode: run with -X pycache_prefix=<a path that "
                         "does not exist>, so every module is compiled from the bytes provenance binds")
    draft_bytes = a.lock_draft.read_bytes()         # read once: the sha256 recorded is of the text checked
    prov = provenance(a.lock_draft, draft_bytes)
    loaded_at_prov = dict(_LOADED)
    dp = draft_problems(draft_bytes.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n"),
                        prov["analyzer_sha256"])
    if dp:
        raise SystemExit(f"REFUSED: {dp}")
    print(f"PROVENANCE {json.dumps(prov)}")
    st = subprocess.run([sys.executable, "-I", "-B", "-X", f"pycache_prefix={sys.pycache_prefix}", "-c", _CHILD_BOOT,
                         str(REPO), _LOAD_COMMIT],
                        capture_output=True, text=True)          # its own process, on the commit and bytes this run
    #                                                              executes: nothing it stubs reaches the record
    print(st.stdout, end="")
    if st.stderr:
        print(st.stderr, end="")
    refusal = selftest_refusal(st.returncode)
    if refusal:
        raise SystemExit(refusal)
    res = compute(m)
    own = inputs_problems(res) + display_problems(res) + fixed_problems(res)
    if own:                                         # this process's own figures, checked as the self-test checks its
        raise SystemExit(f"REFUSED: the record fails its own checks: {own[:5]}")
    res["provenance"] = prov
    text = resume.json_text(res, indent=1)          # built, and the report rendered, before anything is reported: a
    shown = io.StringIO()                           # run that cannot be recorded refuses before it reports
    with redirect_stdout(shown):
        report(res)
    late = ([f"the run loaded repository modules after provenance: "
             f"{sorted(set(closure_files()) - set(prov['closure']))}"] if closure_files() != sorted(prov["closure"])
            else [])
    late += [] if _LOADED == loaded_at_prov else [f"the run executed repository blobs after provenance: "
                                                  f"{sorted(set(_LOADED) - set(loaded_at_prov))}"]
    late += [f"modules executed from the working tree: {_from_tree()}"] if _from_tree() else []
    head_now = _git("rev-parse", "HEAD").strip()
    late += [] if head_now == _LOAD_COMMIT else [f"HEAD moved during the run: loaded from {_LOAD_COMMIT}, now {head_now}"]
    late += path_problems([_repo_rel(x) for x in sys.path])
    if late:
        raise SystemExit(f"REFUSED: {late}")
    print(shown.getvalue(), end="")
    write_record(a.record, text)
    print(f"\nWROTE {a.record} sha256 {hashlib.sha256(a.record.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
