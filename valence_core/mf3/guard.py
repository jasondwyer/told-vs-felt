"""Q-F3's cached-path source guard and the C2 licence's module set (PROPOSAL-m v1.11 §2.7 m:267;
m:48; the design seat's prebuild answers of 2026-11-06, Q1; Code's dated note N1).

INSULATION is ``valence_core.m.guard``'s, imported unchanged: ``assert_insulated`` (the quarantined
state-present module absent from sys.modules, at startup and before every read, m:48),
``insulated_read`` (``readout.choice_read(verify=True)`` with ``assert_construction_stable``, KL
exactly 0.0; m:172), ``label_ids`` and the laptop checklist ``preflight_laptop`` (m:267).

THE CACHED-PATH LICENCE is Q-F3's own (m:267: "Q-F0's G-ID licenses nothing for F3"): ``cached=True``
only where Q-F3's G-ID-F3 artifact (``data/mf3/gates/Q-F3_G-ID.json``) is on disk with PASS, produced
on the asking backend AT THE ASKING REASONING-LINE CAP (the cap is an identity input, m:174, m:295);
G-ID-F3 itself runs both paths from ``gid_paths()``; G-TIME-F3 is uncached (m:293).
``check_call_sites`` is the static half: valence_core.m.guard's hardened scanner, subclassed with
Q-F3's names (mf3's guard the one licensed binding, ``run_gid_pair_f3`` the one exemption), checks
over mf3's sources and its driver that every path argument comes from those sources only. Its
declared limits are m's (a name computed at run time, an alias of the module dict, exec), kept by
the package containing no such code; ``run_session_f3`` re-checks the licence at run time.

THE LICENCE'S MODULE SET (Q1 (C2) part (b); N1): ``M_MODULES`` is the transitive set of
``valence_core.m`` modules mf3's production code imports, at module level or lazily (a ``_selftest``
body and mf3's test double, ``testing.py``, are outside it); ``import_problems`` asserts it by a
static scan and in a fresh interpreter, with ``ABSENT_MODULES`` -- stages, gshape, gcal, both
runners, verify and testing -- never reached.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Mapping

from valence_core.m import guard as m_guard
from valence_core.m import resume as m_resume

REPO = Path(__file__).resolve().parents[2]
PACKAGE_DIR = Path(__file__).resolve().parent
M_PACKAGE_DIR = REPO / "valence_core" / "m"
GATES_DIR = REPO / "data" / "mf3" / "gates"
UNIT = "Q-F3"
# PIN (the seat's F-7, 2026-11-06): m:281's 2/2 criterion, which m:295 carries ("as above"), and per reasoning line
# an identical (n_tok, cap_hit, stop_reason) triple.
GID_CRITERION = (m_guard.GID_CRITERION + " and, per reasoning line, an identical (n_tok, cap_hit, stop_reason) "
                 "triple (the seat's F-7)")
STAGES = ("time", "id", "qual", "campaign")
assert_insulated = m_guard.assert_insulated
insulated_read = m_guard.insulated_read
label_ids = m_guard.label_ids
preflight_laptop = m_guard.preflight_laptop
FORBIDDEN_MODULES = m_guard.FORBIDDEN_MODULES

# PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q1 (C2) part (b); N1): the valence_core.m modules
# mf3 imports, closure-style. Q1's list (corr with corrupt_m, the audit's task-round classes, bars,
# the banner constants, schedule's cells, keys.stream) plus four the build reuses rather than copy:
# guard (the insulated read and the laptop checklist; and, since the build review's finding 1, its
# call-site scanner: _CallSiteScan subclassed, _bindings, _guarded_defs, _LICENSED_FNS and
# _GUARDED_CALLEES), resume (the checkpoint machinery, the package
# hash's formula, the backend identifier), scaffold (SessionScaffold / SessionLog, the boundary
# assertion, the renders of record) and readrule (the blinding helpers). LOCK-m-F3 v0.1 names each
# file's sha256; a stage refuses when one differs (stages.licence_problems).
M_MODULES = ("audit", "banner", "bars", "corr", "guard", "keys", "readrule", "resume", "scaffold", "schedule")
ABSENT_MODULES = ("gcal", "gshape", "runner_olmo", "runner_qwen", "stages", "testing", "verify")
# PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 7): the licence's part (b) hashes the
# package's own __init__.py beside the ten modules -- importing any valence_core.m module executes it first
# -- so it names eleven files, M_HASHED; the import set M_MODULES is unchanged.
M_HASHED = M_MODULES + ("__init__",)
#: mf3's production modules (every *.py of the package but its test double).
TEST_DOUBLE = "testing"


def gid_artifact_path() -> Path:
    return GATES_DIR / f"{UNIT}_G-ID.json"


def gid_paths() -> tuple[bool, bool]:
    """The two paths G-ID-F3 runs per index -- the one licensed source of a True (uncached first)."""
    return (False, True)


def _gid_pass(path: Path, backend_identifier: str, reasoning_cap: int) -> bool:
    try:
        g = json.loads(Path(path).read_bytes().decode("utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    if not isinstance(g, dict):
        return False
    pairs, ident = g.get("pairs_identical"), g.get("identity")
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:174 "the cap enters the resume identity", m:295 "G-ID-F3,
    # at the fixed cap"): m's licence form (unit, criterion, PASS, 2 pairs both identical, this backend)
    # plus the reasoning-line cap -- an artifact produced at another cap licenses nothing; a cap change
    # sets it aside and G-ID-F3 re-runs (stages' PIN).
    return (g.get("unit") == UNIT and g.get("criterion") == GID_CRITERION and g.get("verdict") == "PASS"
            and type(g.get("n_pairs")) is int and g["n_pairs"] == 2
            and type(pairs) is list and len(pairs) == 2 and all(x is True for x in pairs)
            and isinstance(ident, dict) and type(ident.get("backend_identifier")) is str
            and ident["backend_identifier"] == backend_identifier
            and type(ident.get("reasoning_cap")) is int and ident["reasoning_cap"] == reasoning_cap)


def cached_path_admitted(stage: str, *, backend_identifier: str, reasoning_cap: int) -> bool:
    """Is ``cached=True`` licensed for this Q-F3 stage on this backend at this cap? (m:267, m:295)"""
    if stage not in STAGES:
        raise ValueError(f"unknown Q-F3 stage {stage!r}")
    if stage == "id":
        raise ValueError("G-ID-F3 runs both paths itself (gid_paths); it never asks for a licence it is the gate of")
    if type(backend_identifier) is not str or not backend_identifier:
        raise TypeError("backend_identifier must be resume.backend_identifier(adapter.provenance())")
    if type(reasoning_cap) is not int:
        raise TypeError("reasoning_cap must be an int")
    if stage == "time":
        return False                     # "G-TIME-F3 (Qwen, uncached)", m:293
    return _gid_pass(gid_artifact_path(), backend_identifier, reasoning_cap)


# --- the licence's hashes ---------------------------------------------------------------
def package_sha256_of(root) -> str:
    """Q1 (C2) part (a): computed as m's (valence_core.m.resume.package_sha256_of, imported)."""
    return m_resume.package_sha256_of(root)


@lru_cache(maxsize=1)
def package_sha256() -> str:
    """mf3's sources (valence_core/mf3/*.py), hashed once per process (m's PIN, carried)."""
    return package_sha256_of(PACKAGE_DIR)


def m_module_sha256s(root: Path | None = None) -> dict[str, str]:
    """Q1 (C2) part (b): {name: sha256 of valence_core/m/{name}.py's bytes} over M_HASHED (the ten
    modules and the package's __init__.py)."""
    d = Path(M_PACKAGE_DIR if root is None else root)
    return {m: hashlib.sha256((d / f"{m}.py").read_bytes()).hexdigest() for m in M_HASHED}


# --- the import set (N1) -----------------------------------------------------------------
def _m_imports(tree: ast.AST, package: str) -> set[str]:
    """valence_core.m modules a module's code imports, outside any _selftest body. ``package`` is
    the dotted package the module lives in (for relative imports)."""
    out: set[str] = set()

    class V(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            if node.name == "_selftest":
                return
            self.generic_visit(node)

        visit_AsyncFunctionDef = visit_FunctionDef

        def visit_Import(self, node):
            for a in node.names:
                if a.name.startswith("valence_core.m."):
                    out.add(a.name.split(".")[2])
                elif a.name == "valence_core.m":
                    out.add("__init__")

        def visit_ImportFrom(self, node):
            if node.level:
                base = package.split(".")
                base = base[:len(base) - node.level + 1]
                mod = ".".join(base + ([node.module] if node.module else []))
            else:
                mod = node.module or ""
            if mod == "valence_core.m":
                out.update(a.name for a in node.names)
            elif mod.startswith("valence_core.m."):
                out.add(mod.split(".")[2])

    V().visit(tree)
    return out


def production_files(root: Path | None = None) -> list[Path]:
    d = Path(PACKAGE_DIR if root is None else root)
    return sorted(p for p in d.glob("*.py") if p.stem != TEST_DOUBLE)


def static_import_closure(files: Iterable[Path] | None = None) -> tuple[list[str], set[str]]:
    """(problems, closure): the valence_core.m modules mf3's production code reaches, following each
    m module's own imports outside its _selftest body, module-level and lazy alike."""
    probs: list[str] = []
    direct: set[str] = set()
    for p in (production_files() if files is None else files):
        try:
            direct |= _m_imports(ast.parse(Path(p).read_text(encoding="utf-8")), "valence_core.mf3")
        except (OSError, SyntaxError) as e:
            probs.append(f"{p}: unreadable ({type(e).__name__})")
    seen: set[str] = set()
    todo = sorted(direct)
    while todo:
        m = todo.pop()
        if m in seen or m == "__init__":
            continue
        seen.add(m)
        src = M_PACKAGE_DIR / f"{m}.py"
        try:
            sub = _m_imports(ast.parse(src.read_text(encoding="utf-8")), "valence_core.m")
        except (OSError, SyntaxError) as e:
            probs.append(f"valence_core/m/{m}.py: unreadable ({type(e).__name__})")
            continue
        todo.extend(sorted(sub - seen))
    return probs, seen


def runtime_import_set(python: str | None = None) -> tuple[list[str], set[str]]:
    """(problems, set): the valence_core.m modules a fresh interpreter (-I -B) holds after importing
    every mf3 production module."""
    mods = [f"valence_core.mf3.{p.stem}" for p in production_files() if p.stem != "__init__"]
    code = ("import json, sys; sys.path.insert(0, %r)\n" % str(REPO)
            + "".join(f"import {m}\n" for m in mods)
            + "print(json.dumps(sorted(k.split('.')[2] for k in sys.modules if k.startswith('valence_core.m.'))))")
    r = subprocess.run([python or sys.executable, "-I", "-B", "-c", code], capture_output=True, text=True,
                       cwd=str(REPO))
    if r.returncode != 0:
        return [f"fresh-interpreter import failed: {(r.stderr or '').strip().splitlines()[-1:]}"], set()
    return [], set(json.loads(r.stdout.strip().splitlines()[-1]))


def import_problems(*, runtime: bool = True, python: str | None = None) -> list[str]:
    """[] iff the static closure is exactly M_MODULES, no ABSENT module is reached (static or at
    run time), and the fresh interpreter loads no m module outside M_MODULES."""
    probs, closure = static_import_closure()
    if closure != set(M_MODULES):
        probs.append(f"static closure {sorted(closure)} != M_MODULES {list(M_MODULES)}")
    if closure & set(ABSENT_MODULES):
        probs.append(f"static closure reaches {sorted(closure & set(ABSENT_MODULES))}")
    if runtime:
        rp, loaded = runtime_import_set(python)
        probs += rp
        if loaded - set(M_MODULES):
            probs.append(f"a fresh interpreter loads {sorted(loaded - set(M_MODULES))} beyond M_MODULES")
        if loaded & set(ABSENT_MODULES):
            probs.append(f"a fresh interpreter loads {sorted(loaded & set(ABSENT_MODULES))}")
    return probs


# --- the static call-site check (m:267's source guard, Q-F3's form) -----------------------
# PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 1): the check IS
# valence_core.m.guard's hardened scanner (``_CallSiteScan`` with its findings 20, N15 and R7: the
# licence resolved by BINDING, attribute rebinds and monkeypatch forms, ``.generate`` aliases,
# ``forward``, dict literals, any call's cached= keywords, match / import / except rebinds),
# imported and subclassed: the scanner is inherited, and six methods are overridden, each restating
# m's with Q-F3's names (``_OVERRIDES``; the self-test asserts the set) -- the four that bind m's guard
# module or file (``__init__``, ``_flag_licensed_bindings``, ``_is_guard_alias``, ``_licensed``),
# ``in_gid`` (m's G-ID function name) and ``flag`` (renaming m's names in every inherited message,
# among them ``_true_into``'s, ``visit_Dict``'s and ``_check_cached_value``'s):
#   * the licensed sources bind only from mf3's own guard (``from valence_core.mf3.guard import
#     cached_path_admitted`` / ``gid_paths``, or a module alias of valence_core.mf3.guard), so
#     Q-F0's licence -- valence_core.m.guard's -- licenses nothing here (m:267: "Q-F0's G-ID
#     licenses nothing for F3");
#   * the G-ID exemption is the body of a module-level def named ``run_gid_pair_f3``;
#   * ``run_session_f3`` is a guarded callee, and a file outside the repository (a self-test's temp
#     copy) resolves its relative imports as a member of valence_core.mf3;
#   * its messages name mf3's guard and run_gid_pair_f3.
# The self-test runs m's whole checker battery (_CLEAN_SRC, _SMUGGLES, _GAPS) through this
# subclass under ``_battery_map`` -- m's names mapped to mf3's -- and m's verdict must be
# reproduced on every source; Q-F3's own cases are added beside it.
GUARD_MODULE = "valence_core.mf3.guard"
_GID_STAGE_FN = "run_gid_pair_f3"
_UNANCHORED_PACKAGE = "valence_core.mf3"
_LICENSED_FNS = m_guard._LICENSED_FNS             # ("cached_path_admitted", "gid_paths"): the same names
_GUARDED_CALLEES = m_guard._GUARDED_CALLEES + ("run_session_f3",)
_OVERRIDES = frozenset({"__init__", "_flag_licensed_bindings", "_is_guard_alias", "_licensed", "in_gid", "flag"})
_SP = "state" + "present"


def _package_of(fname: str) -> str:
    """m's ``_package_of`` with mf3 as the unanchored package."""
    try:
        rel = Path(fname).resolve().relative_to(REPO)
    except ValueError:
        return _UNANCHORED_PACKAGE
    return ".".join(rel.parent.parts)


def _f3_names(text: str) -> str:
    """m's names in a checker message, as mf3's (the scanner's inherited messages)."""
    text = re.sub(r"\bvalence_core\.m\.guard\b", GUARD_MODULE, text)
    return re.sub(r"\brun_gid_pair\b", _GID_STAGE_FN, text)


class _F3CallSiteScan(m_guard._CallSiteScan):
    def __init__(self, fname: str, tree: ast.Module, guarded: frozenset[str] = frozenset()) -> None:
        # m's __init__ with mf3's guarded callees, guard file and package resolution.
        self.fname = fname
        self.tree = tree
        self.guarded = frozenset(_GUARDED_CALLEES) | guarded
        self.problems: list[str] = []
        self.scopes: list[ast.AST] = []
        self.parent: dict[ast.AST, ast.AST] = {}
        for p in ast.walk(tree):
            for c in ast.iter_child_nodes(p):
                self.parent[c] = p
        try:
            self.is_guard = Path(fname).resolve() == Path(__file__).resolve()
        except OSError:
            self.is_guard = False
        self.binds = m_guard._bindings(tree, _package_of(fname))
        self._flag_licensed_bindings()

    def _flag_licensed_bindings(self) -> None:
        # m's, with mf3's guard as the one licensed binding.
        for name in _LICENSED_FNS:
            for kind, target, line in self.binds.get(name, ()):
                if self.is_guard and kind == "def":
                    continue
                if kind == "from" and target == f"{GUARD_MODULE}.{name}":
                    continue
                self.problems.append(f"{self.fname}:{line}: {name!r} bound by {kind}"
                                     + (f" ({target})" if target else "")
                                     + f" outside mf3's guard.py (only `from {GUARD_MODULE} import "
                                       f"{name}` may bind it)")

    def _is_guard_alias(self, name: str) -> bool:
        # m's, with mf3's guard module.
        b = self.binds.get(name, ())
        return bool(b) and all(k in ("import", "from") and t == GUARD_MODULE for k, t, _ in b)

    def _licensed(self, call: ast.AST) -> str | None:
        # m's, with mf3's guard module: a licensed name bound from valence_core.m.guard is NOT one.
        if not isinstance(call, ast.Call):
            return None
        f = call.func
        if isinstance(f, ast.Name):
            b = [(k, t) for k, t, _ in self.binds.get(f.id, ())]
            if self.is_guard and f.id in _LICENSED_FNS and b == [("def", None)]:
                return f.id
            for name in _LICENSED_FNS:
                if b and all(k == "from" and t == f"{GUARD_MODULE}.{name}" for k, t in b):
                    return name
            return None
        if isinstance(f, ast.Attribute) and f.attr in _LICENSED_FNS:
            v = f.value
            if isinstance(v, ast.Name) and self._is_guard_alias(v.id):
                return f.attr
            if ast.unparse(v) == GUARD_MODULE:
                root = GUARD_MODULE.split(".")[0]
                b = self.binds.get(root, ())
                if b and all(k == "import_root" for k, _, _ in b) and any(t == GUARD_MODULE for _, t, _ in b):
                    return f.attr
        return None

    def in_gid(self) -> bool:
        # m's rule (the BODY of a module-level def only), for run_gid_pair_f3.
        if not self.scopes:
            return False
        sc = self.scopes[-1]
        return (isinstance(sc, (ast.FunctionDef, ast.AsyncFunctionDef)) and sc.name == _GID_STAGE_FN
                and self.parent.get(sc) is self.tree)

    def flag(self, node: ast.AST, msg: str) -> None:
        self.problems.append(f"{self.fname}:{getattr(node, 'lineno', '?')}: {_f3_names(msg)}")


def check_call_sites(paths: Iterable[str | os.PathLike]) -> list[str]:
    """Static half of Q-F3's cached-path guard ([] = clean): m's ``check_call_sites`` driven
    through ``_F3CallSiteScan``. A directory argument is expanded to its *.py files (``__pycache__``
    skipped); an unreadable or unparsable file is a problem, never a pass (m's PIN, carried)."""
    files: list[Path] = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files += sorted(f for f in p.rglob("*.py") if "__pycache__" not in f.parts)
        else:
            files.append(p)
    problems: list[str] = []
    trees: list[tuple[Path, ast.Module]] = []
    for f in files:
        try:
            trees.append((f, ast.parse(f.read_text(encoding="utf-8"), filename=str(f))))
        except (OSError, UnicodeDecodeError, SyntaxError, ValueError) as e:
            problems.append(f"{f}: cannot be checked ({type(e).__name__}: {e})")
    guarded = frozenset(n for _, tree in trees for n in m_guard._guarded_defs(tree))
    for f, tree in trees:
        scan = _F3CallSiteScan(str(f), tree, guarded)
        scan.visit(tree)
        problems += scan.problems
    return problems


def _battery_map(src: str) -> str:
    """m's checker battery as Q-F3's: m's guard module -> mf3's, run_gid_pair -> run_gid_pair_f3,
    run_session_qwen -> run_session_f3 (self-test only)."""
    src = re.sub(r"\bvalence_core\.m\.guard\b", GUARD_MODULE, src)
    src = re.sub(r"\bfrom valence_core\.m import guard\b", "from valence_core.mf3 import guard", src)
    src = re.sub(r"\brun_gid_pair\b", _GID_STAGE_FN, src)
    return re.sub(r"\brun_session_qwen\b", "run_session_f3", src)


# --- forbidden literals ------------------------------------------------------------------
def forbidden_literals() -> tuple[str, ...]:
    # m's three (m_sessions._forbidden), built split so no line of this file holds one
    return ("choice_read_" + "state" + "present", "(10)" + " the", "slip" + " (10)")


def forbidden_hits(paths: Iterable[str | os.PathLike]) -> list[str]:
    out = []
    for p in paths:
        try:
            t = Path(p).read_text(encoding="utf-8")
        except OSError:
            out.append(f"{p}: unreadable")
            continue
        out += [f"{p}: {x!r}" for x in forbidden_literals() if x in t]
    return out


def _selftest(chk) -> None:
    import tempfile
    from unittest import mock

    chk("mf3.guard: insulation, the read, label ids and the laptop checklist are valence_core.m.guard's",
        assert_insulated is m_guard.assert_insulated and insulated_read is m_guard.insulated_read
        and label_ids is m_guard.label_ids and preflight_laptop is m_guard.preflight_laptop
        and GID_CRITERION == ("2/2 byte-identical cached/uncached transcript pairs and, per reasoning line, an "
                              "identical (n_tok, cap_hit, stop_reason) triple (the seat's F-7)"))
    probs = import_problems()
    chk("mf3.guard: the licence's module set -- the static closure of mf3's production imports is exactly "
        "M_MODULES, no stages/gshape/gcal/runner/verify/testing reached, and a fresh interpreter loads none "
        "beyond M_MODULES (N1)", probs == [], probs[:3])
    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "x.py"
        bad.write_text("from valence_core.m import stages\n")
        _, cl = static_import_closure([bad])
        bad.write_text("def f():\n    from valence_core.m.runner_qwen import qwen_startup\n")
        _, cl2 = static_import_closure([bad])
        bad.write_text("def _selftest(chk):\n    from valence_core.m import testing\n")
        _, cl3 = static_import_closure([bad])
    chk("mf3.guard: the static scan catches a module-level stages import and a lazy runner import (with their "
        "closures), and ignores a _selftest-only import",
        {"stages", "runner_qwen", "runner_olmo", "verify"} <= cl and "runner_qwen" in cl2 and cl3 == set())
    shas = m_module_sha256s()
    chk("mf3.guard: m_module_sha256s hashes each licensed module's file and the package's __init__.py (11); "
        "package_sha256 is m's formula over valence_core/mf3",
        sorted(shas) == sorted(M_HASHED) and len(shas) == 11 and all(len(v) == 64 for v in shas.values())
        and package_sha256() == m_resume.package_sha256_of(PACKAGE_DIR) != m_resume.package_sha256())
    bid = "0123456789abcdef"
    art = {"unit": UNIT, "criterion": GID_CRITERION, "verdict": "PASS", "n_pairs": 2,
           "pairs_identical": [True, True], "identity": {"backend_identifier": bid, "reasoning_cap": 60}}
    got = {}
    with tempfile.TemporaryDirectory() as td:
        with mock.patch(f"{__name__}.GATES_DIR", Path(td)):
            got["absent"] = cached_path_admitted("qual", backend_identifier=bid, reasoning_cap=60)
            for nm, a in (("pass", art), ("other cap", art), ("other backend", art),
                          ("fail", {**art, "verdict": "FAIL"}), ("Q-F0's", {**art, "unit": "Q-F0"}),
                          ("one pair", {**art, "n_pairs": 1, "pairs_identical": [True]})):
                gid_artifact_path().write_text(json.dumps(a))
                cap = 120 if nm == "other cap" else 60
                b = "fedcba9876543210" if nm == "other backend" else bid
                got[nm] = cached_path_admitted("campaign", backend_identifier=b, reasoning_cap=cap)
            gid_artifact_path().write_text(json.dumps(art))
            got["time"] = cached_path_admitted("time", backend_identifier=bid, reasoning_cap=60)
    chk("mf3.guard: cached_path_admitted -- PASS on this backend at this cap only; absent, another cap, another "
        "backend, FAIL, Q-F0's artifact, one pair and G-TIME-F3 all give uncached",
        got == {"absent": False, "pass": True, "other cap": False, "other backend": False, "fail": False,
                "Q-F0's": False, "one pair": False, "time": False}, got)
    try:
        cached_path_admitted("id", backend_identifier=bid, reasoning_cap=60)
        ok = False
    except ValueError:
        ok = True
    chk("mf3.guard: G-ID-F3 never asks for the licence it is the gate of; gid_paths is (False, True)",
        ok and gid_paths() == (False, True))
    own = {k for k, v in vars(_F3CallSiteScan).items() if callable(v)}
    chk("mf3.guard: the call-site scanner is valence_core.m.guard's _CallSiteScan, subclassed; six methods are "
        "overridden -- the four that bind m's guard module or file (__init__, _flag_licensed_bindings, "
        "_is_guard_alias, _licensed), in_gid (m's G-ID function name) and flag (m's names in every inherited "
        "message)",
        issubclass(_F3CallSiteScan, m_guard._CallSiteScan) and own == set(_OVERRIDES), sorted(own))
    # m's whole checker battery through the subclass, m's names mapped to mf3's (_battery_map)
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        def scan(tag: str, src) -> list[str]:
            fs = []
            for j, one in enumerate((src,) if isinstance(src, str) else src):
                fs.append(td / f"{tag}_{j}.py")
                fs[-1].write_text(_battery_map(one))
            return check_call_sites(fs)

        def fired(hits: list[str], needle: str) -> bool:
            return any(_battery_map(needle) in h or needle in h for h in hits)

        m_clean = scan("m_clean", m_guard._CLEAN_SRC)
        m_missed = [nm for i, (nm, src, needle) in enumerate(m_guard._SMUGGLES)
                    if not fired(scan(f"m_smuggle{i}", src), needle)]
        g_missed, g_noisy, n_fire, n_clean = [], [], 0, 0
        for gi, (label, fires, cleans) in enumerate(m_guard._GAPS):
            for k, (src, needle) in enumerate(fires):
                n_fire += 1
                if not fired(scan(f"gap{gi}_fire{k}", src), needle):
                    g_missed.append((label, k))
            for k, src in enumerate(cleans):
                n_clean += 1
                if scan(f"gap{gi}_clean{k}", src):
                    g_noisy.append((label, k))
    chk(f"mf3.guard: m's checker battery reproduces through the subclass under the name map -- _CLEAN_SRC "
        f"silent, every one of m's {len(m_guard._SMUGGLES)} smuggles fires with its needle, and m's "
        f"{len(m_guard._GAPS)} gap groups ({n_fire} must-fire, {n_clean} must-not-fire) hold",
        m_clean == [] and not m_missed and not g_missed and not g_noisy,
        {"clean": m_clean[:2], "smuggles": m_missed, "missed": g_missed[:5], "noisy": g_noisy[:5]})
    clean = """
from valence_core.mf3 import guard
from valence_core.mf3.guard import cached_path_admitted

def run_session_f3(adapter, sc, *, path_cached: bool, temp=0.7):
    return adapter.generate("p", "s", injections=(), seed=1, cached=path_cached)

def stage(adapter, bid):
    path_cached = guard.cached_path_admitted("qual", backend_identifier=bid, reasoning_cap=60)
    return _launch(adapter, path_cached=path_cached)

def stage_direct(adapter, bid):
    return run_session_f3(adapter, None,
                          path_cached=cached_path_admitted("qual", backend_identifier=bid, reasoning_cap=60))

def _launch(adapter, *, path_cached):
    return run_session_f3(adapter, None, path_cached=path_cached)

def run_gid_pair_f3(adapter):
    for path_cached in guard.gid_paths():
        _launch(adapter, path_cached=path_cached)

def plain(adapter):
    return adapter.generate("p", "s", injections=(), cached=False)

def withbody(adapter, cm, *, path_cached):
    with cm:
        return run_session_f3(adapter, None, path_cached=path_cached)
"""
    imp = "from valence_core.mf3 import guard\n"
    smuggles = {
        "literal True": "def f(a):\n    return a.generate('p', 's', injections=(), cached=True)\n",
        "no cached=": "def f(a):\n    return a.generate('p', 's', injections=())\n",
        "injections": "def f(a, i):\n    return a.generate('p', 's', injections=i, cached=False)\n",
        "positional injections": "def f(a, i):\n    return a.generate('p', 's', i, cached=False)\n",
        "rebound param": "def f(a, *, path_cached):\n    path_cached = True\n    return a.generate('p','s', injections=(), cached=path_cached)\n",
        "positional param": "def g(a, path_cached):\n    return 1\n",
        "True default": "def g(a, *, cached=True):\n    return 1\n",
        "gid_paths outside run_gid_pair_f3": imp + "def f(a):\n    for path_cached in guard.gid_paths():\n        run_session_f3(a, None, path_cached=path_cached)\n",
        "unlicensed name": "def f(a, x):\n    path_cached = x\n    return run_session_f3(a, None, path_cached=path_cached)\n",
        "kwargs": "def f(a, kw):\n    return run_session_f3(a, None, **kw)\n",
        "own licence": "def cached_path_admitted(*a, **k):\n    return True\n",
        "state-present": f"import valence_core.e2b.{_SP}\n",
        "getattr": "def f(a):\n    return getattr(a, 'generate')('p', 's', injections=(), cached=False)\n",
        "with-bound": "def f(a, cm):\n    with cm as path_cached:\n        return run_session_f3(a, None, path_cached=path_cached)\n",
        "walrus": "def f(a, x):\n    if (path_cached := x):\n        return run_session_f3(a, None, path_cached=path_cached)\n",
        # Q-F0's licence is not Q-F3's (m:267), in each binding form
        "Q-F0's licence by from-import": "from valence_core.m.guard import cached_path_admitted\n",
        "Q-F0's licence by module alias": "from valence_core.m import guard as m_guard\ndef f(a, bid):\n    return a.generate('p', 's', injections=(), cached=m_guard.cached_path_admitted('Q-F0', 'qual', backend_identifier=bid))\n",
        "Q-F0's licence by dotted import": "import valence_core.m.guard\ndef f(a, bid):\n    return a.generate('p', 's', injections=(), cached=valence_core.m.guard.cached_path_admitted('Q-F0', 'qual', backend_identifier=bid))\n",
        "m's gid_paths in run_gid_pair_f3": "from valence_core.m import guard as m_guard\ndef run_gid_pair_f3(a):\n    for path_cached in m_guard.gid_paths():\n        a.generate('p', 's', injections=(), cached=path_cached)\n",
        # the build review's forms (finding 1)
        "any object's licence": "def f(a, obj):\n    return a.generate('p', 's', injections=(), cached=obj.cached_path_admitted())\n",
        "a parameter named as the licence": "def f(a, cached_path_admitted):\n    return a.generate('p', 's', injections=(), cached=cached_path_admitted())\n",
        "a lambda parameter named as the licence": "g = lambda a, cached_path_admitted: a.generate('p', 's', injections=(), cached=cached_path_admitted())\n",
        "alias of .generate": "def f(a):\n    g = a.generate\n    return g('p', 's', injections=(), cached=True)\n",
        "a class-attribute alias of .generate": "class R:\n    gen = None\ndef f(a):\n    R.gen = a.generate\n    return R.gen('p', 's', injections=(), cached=True)\n",
        "functools.partial": "import functools\ndef f(a, sc):\n    p = functools.partial(run_session_f3, path_cached=True)\n    return p(a, sc)\n",
        "nested def named run_gid_pair_f3": "def stage(a):\n    def run_gid_pair_f3():\n        return a.generate('p', 's', injections=(), cached=True)\n    return run_gid_pair_f3()\n",
        "method named run_gid_pair_f3": "class X:\n    def run_gid_pair_f3(self, a):\n        return a.generate('p', 's', injections=(), cached=True)\n",
        "setattr of the licence": imp + "def f():\n    setattr(guard, 'cached_path_admitted', lambda *a, **k: True)\n",
        "a {'cached': True} literal": "def f(a):\n    opts = {'cached': True}\n    return opts\n",
        "forward with injections": "def f(a, inj):\n    return a.forward('p', injections=inj)\n",
        "a match capture rebinds the parameter": "def f(a, x, *, path_cached):\n    match x:\n        case path_cached:\n            pass\n    return a.generate('p', 's', injections=(), cached=path_cached)\n",
        "an import rebinds the parameter": "def f(a, *, path_cached):\n    import builtins as path_cached\n    return a.generate('p', 's', injections=(), cached=path_cached)\n",
        "an or-chain with True": imp + "def f(a, bid):\n    return a.generate('p', 's', injections=(), cached=guard.cached_path_admitted('qual', backend_identifier=bid, reasoning_cap=60) or True)\n",
    }
    silent = []
    with tempfile.TemporaryDirectory() as td:
        c = Path(td) / "clean.py"
        c.write_text(clean)
        clean_probs = check_call_sites([c])
        for nm, src in smuggles.items():
            p = Path(td) / "smuggle.py"
            p.write_text(src)
            if not check_call_sites([p]):
                silent.append(nm)
        (Path(td) / "broken.py").write_text("def f(:\n")
        broken = check_call_sites([Path(td) / "broken.py"])
    chk("mf3.guard: check_call_sites is clean on Q-F3's licensed shapes (a keyword-only path_cached threaded "
        "from mf3's cached_path_admitted, by alias or by name; gid_paths inside run_gid_pair_f3; a literal False)",
        clean_probs == [], clean_probs[:2])
    chk(f"mf3.guard: check_call_sites fires on every Q-F3 smuggle ({len(smuggles)}: Q-F0's licence in three "
        f"binding forms and m's gid_paths among them) and on an unparsable file (fails closed)",
        not silent and any("cannot be checked" in b for b in broken), silent)
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "a.py"
        p.write_text("x = 'see decision " + "(10)" + " the rest'\n")
        hit = forbidden_hits([p])
        p.write_text("x = 'clean'\n")
        miss = forbidden_hits([p])
    chk("mf3.guard: the forbidden-literal scan fires on m's literals, clean otherwise", hit != [] and miss == [])
