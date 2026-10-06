"""PROPOSAL-m source guard, insulated read and cached-path licence (v1.11 §0.4 m:48;
§2.7 m:267; §3.1 G-TIME-F0 / G-ID-F0m m:280-281; §8 step 4's build pins).

INSULATION (m:48). "The quarantined state-present primitive (rule 5(e)) is asserted
absent from ``sys.modules`` at startup and before every read by the m package's
runners on both substrates." ``assert_insulated`` is that assertion (session.py:42-57,
e2d/runner.py:53's tuple); ``insulated_read`` is recon's ``_insulated_read``
(recon.py:259-263) plus one clause: the verify KL must be ``== 0.0`` exactly, because
``readout.assert_construction_stable`` compares ``> 0.0`` and so lets a NaN or a
negative float through (maps/e2a.md §3). The read itself is ``readout.choice_read``,
frozen, which takes no injections by construction.

CACHED-PATH LICENCE (m:267). "The m package's cached-path source guard permits
``cached=True`` only when the unit's G-ID artifact is on disk with PASS, and exempts
only the G-ID stage." Two halves:
  * runtime -- ``cached_path_admitted(unit, stage, *, backend_identifier)`` reads
    ``data/m/gates/{unit}_G-ID.json`` structurally, in e2d_tstep_check.py's stance
    (:58-87): anything short of a well-formed PASS for this unit, produced on THIS
    backend (``identity.backend_identifier`` == the caller's
    ``resume.backend_identifier(adapter.provenance())``; rule 2, gates per backend),
    means uncached -- an undetermined licence is not a granted one. OLMo is uncached by
    spec (m:267); G-TIME-F0 is uncached by spec (m:280); G-ID never asks, it runs both
    paths (``gid_paths``).
  * static -- ``check_call_sites(paths)`` walks the AST of m's sources: every
    ``cached=`` / ``path_cached=`` value must be the literal ``False``, a call of
    ``cached_path_admitted``, or a name bound only from those (or a keyword-only
    parameter, whose caller is checked in turn); a literal ``True`` (and ``gid_paths``)
    only in the body of a module-level ``run_gid_pair``. The two licensed functions are
    resolved by BINDING: a call counts only if its name was bound by ``from
    valence_core.m.guard import ...`` or is an attribute of a module alias bound only by
    importing ``valence_core.m.guard``; any other binding of either name outside this
    file is itself flagged, and so, in any file, is a rebinding of either name as an
    ATTRIBUTE in one of these static forms: an assignment, augmented or annotated
    assignment, ``del``, ``for`` / ``async for``, ``with ... as`` or comprehension target
    ``<expr>.<name>`` or ``<expr>["<name>"]``; ``setattr`` / ``delattr`` naming it as a
    string constant (slot 1) or as the last component of a dotted string (pytest's
    ``monkeypatch.setattr("pkg.mod.<name>", ...)``); ``__setattr__`` / ``__delattr__`` /
    ``__setitem__`` / ``__delitem__`` naming it as a string constant in slot 0 (bound) or
    slot 1 (``object.__setattr__(mod, ...)``); ``patch.object`` (slot 1), ``patch``
    (a dotted string), ``patch.multiple`` and ``patch.dict`` naming it as a keyword or a
    dict-literal key; ``<x>.__dict__.update`` / ``vars(<x>).update`` naming it likewise.
    Any other rebinding -- a name computed at run time (``setattr(obj, attr, value)``),
    an alias of the module's dict, ``exec`` -- is beyond this static check AND defeats
    the runtime licence too (runner_qwen re-checks through the same module attribute):
    the declared limit. A ``cached`` / ``path_cached`` parameter defaults to
    nothing or to the literal ``False``. It also refuses any ``Injection`` or
    statepresent import, any non-empty ``injections=`` (test code included),
    ``**``-unpacking into a guarded callee unless the mapping is a dict literal it can
    inspect entry by entry as keywords, the unbound-method form ``Cls.generate(obj,
    ...)`` (its positional slots are shifted), and aliasing of ``.generate``. Guarded
    callees: ``generate``, ``forward``, the two runners, and every function defined in
    the scanned files with a ``cached`` / ``path_cached`` / ``injections`` parameter
    (collected in a first pass over all files). recon's grep guard (format_recon.py:494-499) is
    defeated by ``cached=cached`` and ``**{"cached": True}`` (maps/runner.md §2); this is
    the call-site form maps/runner.md §10 item 9 recommends.

LAPTOP PREFLIGHT (m:267's checklist, v1.3's restored): power adapter >= 96 W on AC;
one process -- no other model process running; disk headroom checked.
"""
from __future__ import annotations

import ast
import dataclasses
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from ..readout import ChoiceRead, assert_construction_stable, choice_read
from ..session import assert_modules_absent
from . import keys

REPO = Path(__file__).resolve().parents[2]
FORBIDDEN_MODULES = ("valence_core.e2b.statepresent",)   # == e2d/runner.py:53 (selftest)
GATES_DIR = REPO / "data" / "m" / "gates"
GID_CRITERION = "2/2 byte-identical cached/uncached transcript pairs"   # m:281 verbatim
STAGES = ("time", "id", "qual", "campaign")

# PIN (Code, declared at LOCK v0.1): laptop preflight thresholds -- adapter wattage
# >= 96 W read from `pmset -g adapter`, AC from `pmset -g ps` ("Now drawing from 'AC
# Power'"), disk headroom >= 5 GiB free on the volume holding REPO.
MIN_ADAPTER_WATTS = 96
DISK_HEADROOM_BYTES = 5 * 1024 ** 3
# PIN (Code, declared at LOCK v0.1): a "model process" is a python process (pgrep -ifl
# python) -- its EXECUTABLE, argv[0]'s basename, contains "python" (finding 23: a shell
# wrapper such as `/bin/zsh -c "... jlens-qwen36/.venv/bin/python ..."` or a viewer whose
# arguments name the venv is not one) -- whose command line names any of these,
# case-insensitively, other than this process and its ancestors (the caffeinate/nohup
# wrappers). The jlens venv's python path carries "jlens", so every process on the
# laptop's model stack matches; a live notebook kernel is counted because it can hold a
# loaded model invisibly.
MODEL_PROCESS_MARKERS = ("mlx", "jlens", "qwen", "olmo", "ipykernel")

_CACHED_KW = ("cached", "path_cached")
_ADMIT_FN = "cached_path_admitted"
_GID_FN = "gid_paths"
_LICENSED_FNS = (_ADMIT_FN, _GID_FN)
_GID_STAGE_FN = "run_gid_pair"
GUARD_MODULE = "valence_core.m.guard"
# PIN (Code, declared at LOCK v0.1): a scanned file outside REPO/valence_core (a selftest's
# temp copy) resolves its relative imports as a member of valence_core.m, the package
# whose sources the check exists for; a file under REPO resolves them from its own path.
_UNANCHORED_PACKAGE = "valence_core.m"
# Callees whose keyword arguments the check must see: "**mapping" into one of them
# is refused unless the mapping is a dict literal inspected entry by entry.
# PIN (Code, declared at LOCK v0.1): beyond generate and the two runners, ``forward``
# (it takes injections= exactly as generate does) and every function defined in the
# scanned files with an ``injections`` parameter, besides a cached/path_cached one,
# are guarded.
_GUARDED_CALLEES = ("generate", "forward", "run_session_qwen", "run_session_olmo")
_GUARD_PARAMS = _CACHED_KW + ("injections",)
_SLOT_CALLS = ("generate", "forward")       # adapter calls checked by positional slot


# --- insulation and the read ----------------------------------------------------
def assert_insulated() -> None:
    """m:48: the quarantined primitive is not loaded (startup and before every read)."""
    assert_modules_absent(FORBIDDEN_MODULES)


def insulated_read(adapter, prefix: str, a: str, b: str,
                   label_ids: Mapping[str, int]) -> ChoiceRead:
    """The only choice read m makes: vanilla, verified, exactly reproducible."""
    assert_insulated()
    if a == b:
        raise ValueError("a choice read needs two distinct menu labels")
    cr = choice_read(adapter, prefix, a, b, label_ids, verify=True)
    assert_construction_stable(cr)               # halts on verify KL > 0.0
    kl = cr.verify_kl
    # assert_construction_stable passes NaN and negative floats; the operative form
    # of g3' clause 1 is KL = 0.0 exactly (readout.py:34-38).
    if not (type(kl) is float and kl == 0.0):
        raise SystemExit(f"CONSTRUCTION INCIDENT (m read guard): verify KL {kl!r} is not "
                         f"exactly 0.0 on an identical code path -- HALT")
    return cr


def label_ids(adapter, labels: Sequence[str]) -> dict[str, int]:
    """Single-token label ids (recon.py:284-289's check, plus distinctness)."""
    labels = tuple(labels)
    if len(set(labels)) != len(labels):
        raise SystemExit("STOP: duplicate menu labels; the read needs two distinct labels")
    out: dict[str, int] = {}
    for t in labels:
        enc = adapter.encode(" " + t, add_special_tokens=False)
        if len(enc) != 1:
            raise SystemExit(f"STOP: label {t!r} is {len(enc)} tokens; the read needs "
                             f"single-token labels")
        out[t] = int(enc[0])
    if len(set(out.values())) != len(out):
        raise SystemExit("STOP: two menu labels share one token id; the read cannot "
                         "tell them apart")
    return out


# --- the cached-path licence ----------------------------------------------------
def _substrate(unit: str) -> str:
    keys.templates(unit)                   # ValueError unknown / NotImplementedError Q-F3
    return "qwen" if unit == "Q-F0" else "olmo"


def gid_artifact_path(unit: str) -> Path:
    # PIN (Code, declared at LOCK v0.1): OLMo units have no G-ID artifact (no G-ID on
    # OLMo, m:267) and asking for one is an error, not a path.
    if _substrate(unit) != "qwen":
        raise ValueError(f"no G-ID on OLMo (uncached path, m:267): {unit!r}")
    return GATES_DIR / f"{unit}_G-ID.json"


def gid_paths() -> tuple[bool, bool]:
    """The two paths G-ID-F0m runs per index -- the one licensed source of a True.

    PIN (Code, declared at LOCK v0.1): uncached first, then cached, at every index.
    """
    return (False, True)


def _gid_pass(path: Path, unit: str, backend_identifier: str) -> bool:
    """Structural read of a G-ID artifact: True only for a well-formed PASS produced on
    this backend."""
    try:
        g = json.loads(Path(path).read_bytes().decode("utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    if not isinstance(g, dict):
        return False
    pairs = g.get("pairs_identical")
    ident = g.get("identity")
    # PIN (Code, declared at LOCK v0.1): the licence is per backend (CLAUDE.md rule 2,
    # "gates re-validated per backend"; its annotation "T-step identity is its own
    # gate"): the artifact's identity.backend_identifier -- resume.backend_identifier of
    # the adapter G-ID ran on -- must equal the asking run's. A different, missing or
    # malformed backend is an undetermined licence, i.e. uncached; a new G-ID on the new
    # backend is the seat's to order (resume.py's backend PIN: an OS or mlx update on
    # the laptop is a backend change).
    return (type(g.get("unit")) is str and g["unit"] == unit
            and g.get("criterion") == GID_CRITERION
            and g.get("verdict") == "PASS"
            and type(g.get("n_pairs")) is int and g["n_pairs"] == 2
            and type(pairs) is list and len(pairs) == 2 and all(x is True for x in pairs)
            and isinstance(ident, dict) and type(ident.get("backend_identifier")) is str
            and ident["backend_identifier"] == backend_identifier)


def cached_path_admitted(unit: str, stage: str, *, backend_identifier: str) -> bool:
    """Is ``cached=True`` licensed for this unit's stage on this backend? (m:267,
    m:280-281; rule 2). ``backend_identifier`` is
    ``resume.backend_identifier(adapter.provenance())`` of the run asking."""
    sub = _substrate(unit)
    if stage not in STAGES:
        raise ValueError(f"unknown stage {stage!r}; stages are {STAGES}")
    if stage == "id":
        raise ValueError("G-ID runs both paths itself and must call gid_paths(); it never "
                         "asks for a licence it is the gate of")
    if type(backend_identifier) is not str or not backend_identifier:
        raise TypeError("backend_identifier must be resume.backend_identifier(adapter."
                        f"provenance()) (a non-empty str), got {backend_identifier!r}")
    if sub == "olmo":
        return False                       # OLMo uncached (Phase B's path), m:267
    # PIN (Code, declared at LOCK v0.1): G-TIME-F0 is uncached whatever is on disk
    # ("G-TIME-F0 (Qwen, uncached)", m:280); only qual and campaign read the artifact.
    if stage == "time":
        return False
    return _gid_pass(gid_artifact_path(unit), unit, backend_identifier)


# --- the static call-site check -------------------------------------------------
def _callee(node: ast.AST) -> str | None:
    f = node.func if isinstance(node, ast.Call) else None
    if isinstance(f, ast.Name):
        return f.id
    if isinstance(f, ast.Attribute):
        return f.attr
    return None


def _is_const(node: ast.AST | None, value: bool) -> bool:
    return isinstance(node, ast.Constant) and node.value is value


def _is_empty_literal(node: ast.AST) -> bool:
    if isinstance(node, (ast.Tuple, ast.List)) and not node.elts:
        return True
    return (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id in ("tuple", "list") and not node.args and not node.keywords)


def _params(fn: ast.AST) -> list[tuple[ast.arg, ast.AST | None, bool]]:
    """(arg, default, keyword_only) for every parameter of a def or lambda."""
    a = fn.args
    pos = list(a.posonlyargs) + list(a.args)
    defaults = [None] * (len(pos) - len(a.defaults)) + list(a.defaults)
    out = [(p, d, False) for p, d in zip(pos, defaults)]
    out += [(p, d, True) for p, d in zip(a.kwonlyargs, a.kw_defaults)]
    out += [(p, None, False) for p in (a.vararg, a.kwarg) if p is not None]
    return out


def _local_nodes(scope: ast.AST) -> Iterable[ast.AST]:
    """Nodes of one scope's body, not descending into nested defs/lambdas/classes."""
    stack = list(ast.iter_child_nodes(scope))
    while stack:
        n = stack.pop()
        yield n
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
            continue
        stack.extend(ast.iter_child_nodes(n))


def _target_names(t: ast.AST) -> list[str]:
    if isinstance(t, ast.Name):
        return [t.id]
    if isinstance(t, (ast.Tuple, ast.List)):
        return [n for e in t.elts for n in _target_names(e)]
    if isinstance(t, ast.Starred):
        return _target_names(t.value)
    return []


def _licensed_attr_targets(t: ast.AST) -> list[str]:
    """The licensed names an assignment / del target rebinds as an attribute:
    ``<expr>.<name>`` or the module-dict form ``<expr>["<name>"]``, through tuple,
    list and starred targets."""
    if isinstance(t, ast.Attribute):
        return [t.attr] if t.attr in _LICENSED_FNS else []
    if isinstance(t, ast.Subscript):
        sl = t.slice
        return [sl.value] if isinstance(sl, ast.Constant) and sl.value in _LICENSED_FNS else []
    if isinstance(t, (ast.Tuple, ast.List)):
        return [n for e in t.elts for n in _licensed_attr_targets(e)]
    if isinstance(t, ast.Starred):
        return _licensed_attr_targets(t.value)
    return []


def _call_arg(node: ast.Call, pos: int, kw: str) -> ast.AST | None:
    if len(node.args) > pos and not any(isinstance(a, ast.Starred) for a in node.args[:pos + 1]):
        return node.args[pos]
    return next((k.value for k in node.keywords if k.arg == kw), None)


def _guarded_defs(tree: ast.AST) -> set[str]:
    """Names of the functions (defs, and lambdas bound to a name) defined in one
    module that take a cached / path_cached / injections parameter."""
    out: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if any(p.arg in _GUARD_PARAMS for p, _, _ in _params(n)):
                out.add(n.name)
        elif isinstance(n, (ast.Assign, ast.AnnAssign)) and isinstance(n.value, ast.Lambda):
            if any(p.arg in _GUARD_PARAMS for p, _, _ in _params(n.value)):
                tgts = n.targets if isinstance(n, ast.Assign) else [n.target]
                for t in tgts:
                    out.update(_target_names(t))
                    if isinstance(t, ast.Attribute):
                        out.add(t.attr)
    return out


def _dict_literal_keywords(v: ast.AST) -> list[ast.keyword] | None:
    """A ``**{...}`` mapping as the keywords it passes, or None when the checker
    cannot see every entry (not a dict literal, a nested ``**``, a non-str key)."""
    if not isinstance(v, ast.Dict):
        return None
    out: list[ast.keyword] = []
    for k, val in zip(v.keys, v.values):
        if not (isinstance(k, ast.Constant) and type(k.value) is str):
            return None
        out.append(ast.copy_location(ast.keyword(arg=k.value, value=val), val))
    return out


def _package_of(fname: str) -> str:
    """The dotted package a scanned file's relative imports resolve against."""
    try:
        rel = Path(fname).resolve().relative_to(REPO)
    except ValueError:
        return _UNANCHORED_PACKAGE
    return ".".join(rel.parent.parts)


def _resolve_from(node: ast.ImportFrom, package: str) -> str:
    if not node.level:
        return node.module or ""
    parts = package.split(".") if package else []
    base = parts[:len(parts) - (node.level - 1)] if node.level - 1 <= len(parts) else []
    return ".".join(base + ([node.module] if node.module else []))


def _bindings(tree: ast.Module, package: str) -> dict[str, list[tuple[str, str | None, int]]]:
    """Every binding of every name anywhere in a module (all scopes): name -> [(kind,
    target)]. Imports carry what they bind ("import" a module under an alias,
    "import_root" the root of a dotted ``import a.b.c``, "from" ``module.attr``); every
    other binding (def, class, assignment, parameter, loop / comprehension / with / except
    / match target, global, del) carries None; the third field is the line. The licence is
    read off these, so a name is trusted only when EVERY binding of it in the module is
    the licensed import."""
    out: dict[str, list[tuple[str, str | None, int]]] = {}
    line = 0

    def add(name: str | None, kind: str, target: str | None = None) -> None:
        if name:
            out.setdefault(name, []).append((kind, target, line))

    def targets(t: ast.AST, kind: str) -> None:
        for n in _target_names(t):
            add(n, kind)

    for n in ast.walk(tree):
        line = getattr(n, "lineno", 0)
        if isinstance(n, ast.Import):
            for a in n.names:
                if a.asname:
                    add(a.asname, "import", a.name)
                else:
                    add(a.name.split(".")[0], "import_root", a.name)
        elif isinstance(n, ast.ImportFrom):
            mod = _resolve_from(n, package)
            for a in n.names:
                add(a.asname or a.name, "from", f"{mod}.{a.name}")
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            add(n.name, "def")
            if not isinstance(n, ast.ClassDef):
                for arg, _, _ in _params(n):
                    add(arg.arg, "param")
        elif isinstance(n, ast.Lambda):
            for arg, _, _ in _params(n):
                add(arg.arg, "param")
        elif isinstance(n, ast.Assign):
            for t in n.targets:
                targets(t, "assign")
        elif isinstance(n, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            targets(n.target, "assign")
        elif isinstance(n, (ast.For, ast.AsyncFor, ast.comprehension)):
            targets(n.target, "loop")
        elif isinstance(n, (ast.With, ast.AsyncWith)):
            for i in n.items:
                if i.optional_vars is not None:
                    targets(i.optional_vars, "with")
        elif isinstance(n, ast.ExceptHandler):
            add(n.name, "except")
        elif isinstance(n, (ast.MatchAs, ast.MatchStar)):
            add(n.name, "match")
        elif isinstance(n, ast.MatchMapping):
            add(n.rest, "match")
        elif isinstance(n, (ast.Global, ast.Nonlocal)):
            for nm in n.names:
                add(nm, "global")
        elif isinstance(n, ast.Delete):
            for t in n.targets:
                targets(t, "del")
    return out


def _binds_name(n: ast.AST, name: str) -> bool:
    """Does this node (in one scope's local nodes) rebind ``name`` other than by the
    assignment / for / with forms _name_ok judges itself?"""
    if isinstance(n, ast.comprehension):
        return name in _target_names(n.target)
    if isinstance(n, ast.ExceptHandler):
        return n.name == name
    if isinstance(n, (ast.MatchAs, ast.MatchStar)):
        return n.name == name
    if isinstance(n, ast.MatchMapping):
        return n.rest == name
    if isinstance(n, (ast.Import, ast.ImportFrom)):
        return any((a.asname or a.name.split(".")[0]) == name for a in n.names)
    if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return n.name == name
    if isinstance(n, ast.Delete):
        return any(name in _target_names(t) for t in n.targets)
    return False


class _CallSiteScan(ast.NodeVisitor):
    def __init__(self, fname: str, tree: ast.Module, guarded: frozenset[str] = frozenset()) -> None:
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
        self.binds = _bindings(tree, _package_of(fname))
        self._flag_licensed_bindings()

    # PIN (Code, declared at LOCK v0.1; finding 20): the licensed sources are resolved by
    # BINDING, not spelling. Outside guard.py the names cached_path_admitted / gid_paths
    # may be bound only by ``from valence_core.m.guard import <name>``; any other binding
    # (def -- a method included --, lambda or other assignment, an import from elsewhere,
    # a parameter, a loop, with, except or match target) is flagged wherever it stands.
    def _flag_licensed_bindings(self) -> None:
        for name in _LICENSED_FNS:
            for kind, target, line in self.binds.get(name, ()):
                if self.is_guard and kind == "def":
                    continue
                if kind == "from" and target == f"{GUARD_MODULE}.{name}":
                    continue
                self.problems.append(f"{self.fname}:{line}: {name!r} bound by {kind}"
                                     + (f" ({target})" if target else "")
                                     + f" outside guard.py (only `from {GUARD_MODULE} import "
                                       f"{name}` may bind it)")

    # PIN (Code, declared at LOCK v0.1; findings N15, R7): a licensed name rebound as an
    # ATTRIBUTE is flagged in every scanned file, guard.py included, in these static forms
    # only: an assignment, augmented or annotated assignment, del, for / async for, with
    # ... as, or comprehension target ``<expr>.<name>`` / ``<expr>["<name>"]``; setattr /
    # delattr with the name as a string constant in slot 1 or as the last component of a
    # dotted string in slot 0 (pytest's monkeypatch form); a bound or unbound
    # __setattr__ / __delattr__ / __setitem__ / __delitem__ with it as a string constant
    # in slot 0 or 1; patch.object (slot 1), patch (a dotted string ending in it),
    # patch.multiple and patch.dict with it as a keyword or a dict-literal key; and
    # ``<x>.__dict__.update`` / ``vars(<x>).update`` likewise. Anything else -- a name
    # computed at run time (a helper's ``setattr(obj, attr, value)``), an alias of the
    # module dict, exec -- escapes this check, and it defeats the runtime licence as well
    # (runner_qwen's re-check calls the same module attribute): the declared limit, kept
    # by the package containing no such code (check_call_sites over it is []).
    def _flag_attr_rebind(self, targets: Sequence[ast.AST], node: ast.AST, how: str) -> None:
        for t in targets:
            for name in _licensed_attr_targets(t):
                self.flag(node, f"{name!r} rebound as an attribute ({how}): a monkeypatch of the "
                                f"guard's licence")

    def _flag_attr_rebind_call(self, node: ast.Call, name: str | None) -> None:
        hits: list[str] = []

        def const_name(a: ast.AST | None) -> str | None:
            return a.value if isinstance(a, ast.Constant) and a.value in _LICENSED_FNS else None

        def dotted_name(a: ast.AST | None) -> str | None:
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                last = a.value.rsplit(".", 1)[-1]
                return last if last in _LICENSED_FNS else None
            return None

        def mapping_names(call: ast.Call, positional_from: int) -> list[str]:
            out = [k.arg for k in call.keywords if k.arg in _LICENSED_FNS]
            for a in call.args[positional_from:]:
                if isinstance(a, ast.Dict):
                    out += [k.value for k in a.keys if isinstance(k, ast.Constant) and k.value in _LICENSED_FNS]
            return out
        f = node.func
        if name in ("setattr", "delattr"):
            hits += [x for x in (const_name(_call_arg(node, 1, "name")), const_name(_call_arg(node, 1, "attribute")),
                                 dotted_name(node.args[0] if node.args else _call_arg(node, 0, "target")))
                     if x]
        elif name in ("__setattr__", "__delattr__", "__setitem__", "__delitem__"):
            hits += [x for x in (const_name(node.args[0] if len(node.args) > 0 else None),
                                 const_name(node.args[1] if len(node.args) > 1 else None)) if x]
        elif name == "object":
            hits += [x for x in (const_name(_call_arg(node, 1, "attribute")),) if x]
        elif name == "patch":
            hits += [x for x in (dotted_name(_call_arg(node, 0, "target")),) if x]
        elif name in ("multiple", "dict") and isinstance(f, ast.Attribute) and (
                (isinstance(f.value, ast.Name) and f.value.id == "patch")
                or (isinstance(f.value, ast.Attribute) and f.value.attr == "patch")):
            hits += mapping_names(node, 1)
        elif name == "update" and isinstance(f, ast.Attribute) and (
                (isinstance(f.value, ast.Attribute) and f.value.attr == "__dict__")
                or (isinstance(f.value, ast.Call) and _callee(f.value) == "vars")):
            hits += mapping_names(node, 0)
        for hit in dict.fromkeys(hits):
            self.flag(node, f"{hit!r} rebound as an attribute ({name}(...)): a monkeypatch of the "
                            f"guard's licence")

    def _is_guard_alias(self, name: str) -> bool:
        b = self.binds.get(name, ())
        return bool(b) and all(k in ("import", "from") and t == GUARD_MODULE for k, t, _ in b)

    def _licensed(self, call: ast.AST) -> str | None:
        """cached_path_admitted / gid_paths when ``call`` calls the guard's own function
        through a binding the module cannot have redirected; else None."""
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
            # the dotted form valence_core.m.guard.<fn> after `import valence_core.m.guard`
            if ast.unparse(v) == GUARD_MODULE:
                root = GUARD_MODULE.split(".")[0]
                b = self.binds.get(root, ())
                if b and all(k == "import_root" for k, _, _ in b) and any(t == GUARD_MODULE
                                                                       for _, t, _ in b):
                    return f.attr
        return None

    def flag(self, node: ast.AST, msg: str) -> None:
        self.problems.append(f"{self.fname}:{getattr(node, 'lineno', '?')}: {msg}")

    def in_gid(self) -> bool:
        # PIN (Code, declared at LOCK v0.1; finding 20): the G-ID exemption covers the BODY
        # of a module-level function named run_gid_pair only -- not a scope nested in it,
        # and not a def of that name nested in other code or in a class.
        if not self.scopes:
            return False
        sc = self.scopes[-1]
        return (isinstance(sc, (ast.FunctionDef, ast.AsyncFunctionDef)) and sc.name == _GID_STAGE_FN
                and self.parent.get(sc) is self.tree)

    def scope(self) -> ast.AST:
        return self.scopes[-1] if self.scopes else self.tree

    # scopes and parameters
    def _enter(self, node: ast.AST) -> None:
        for arg, default, kwonly in _params(node):
            if arg.arg not in _CACHED_KW:
                continue
            # PIN (Code, declared at LOCK v0.1): a cached/path_cached parameter is
            # keyword-only, so every caller names it and its value is checked here.
            if not kwonly:
                self.flag(arg, f"parameter {arg.arg!r} must be keyword-only (a positional "
                               f"path argument escapes the call-site check)")
            # PIN (Code, declared at LOCK v0.1): its default is absent or the literal
            # False -- anything else (1, True, None, a name) can reach generate as an
            # unchecked path when a caller omits the keyword. No run_gid_pair
            # exemption: G-ID passes its True at the call, never by default.
            if default is not None and not _is_const(default, False):
                self.flag(arg, f"parameter {arg.arg!r} defaults to {ast.unparse(default)} "
                               f"(only no default or the literal False is allowed)")
        self.scopes.append(node)
        self.generic_visit(node)
        self.scopes.pop()

    visit_FunctionDef = _enter
    visit_AsyncFunctionDef = _enter
    visit_Lambda = _enter

    # imports and names
    def visit_Import(self, node: ast.Import) -> None:
        for a in node.names:
            if "statepresent" in a.name:
                self.flag(node, f"statepresent import ({a.name})")
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        mod = node.module or ""
        if "statepresent" in mod:
            self.flag(node, f"statepresent import (from {mod})")
        for a in node.names:
            if a.name == "*":
                self.flag(node, f"star import from {mod or '.'} (imported names cannot be checked)")
            if "statepresent" in a.name:
                self.flag(node, f"statepresent import ({a.name})")
            if a.name == "Injection":
                self.flag(node, f"Injection import (from {mod or '.'})")
        self.generic_visit(node)

    def visit_Name(self, node: ast.Name) -> None:
        if node.id == "Injection":
            self.flag(node, "Injection referenced")
        if "statepresent" in node.id:
            self.flag(node, f"statepresent name {node.id!r}")
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if node.attr == "Injection":
            self.flag(node, "Injection referenced")
        if "statepresent" in node.attr:
            self.flag(node, f"statepresent attribute {node.attr!r}")
        par = self.parent.get(node)
        if node.attr == "generate" and not (isinstance(par, ast.Call) and par.func is node):
            self.flag(node, ".generate referenced without being called (an alias escapes the "
                            "call-site check)")
        self.generic_visit(node)

    # literal-True smuggles
    def _true_into(self, targets: Sequence[ast.AST], value: ast.AST | None, node: ast.AST) -> None:
        if not _is_const(value, True) or self.in_gid():
            return
        for t in targets:
            names = _target_names(t)
            if isinstance(t, ast.Attribute):
                names = [t.attr]
            if (isinstance(t, ast.Subscript) and isinstance(t.slice, ast.Constant)
                    and t.slice.value in _CACHED_KW):
                names = [t.slice.value]
            for n in names:
                if n in _CACHED_KW:
                    self.flag(node, f"{n} = True outside {_GID_STAGE_FN}")

    def visit_Assign(self, node: ast.Assign) -> None:
        self._true_into(node.targets, node.value, node)
        self._flag_attr_rebind(node.targets, node, "assignment")
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        self._true_into([node.target], node.value, node)
        self._flag_attr_rebind([node.target], node, "annotated assignment")
        self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        self._flag_attr_rebind([node.target], node, "augmented assignment")
        self.generic_visit(node)

    def visit_Delete(self, node: ast.Delete) -> None:
        self._flag_attr_rebind(node.targets, node, "del")
        self.generic_visit(node)

    def visit_For(self, node: ast.For | ast.AsyncFor) -> None:
        self._flag_attr_rebind([node.target], node, "for target")
        self.generic_visit(node)

    visit_AsyncFor = visit_For

    def visit_With(self, node: ast.With | ast.AsyncWith) -> None:
        self._flag_attr_rebind([i.optional_vars for i in node.items if i.optional_vars is not None],
                               node, "with target")
        self.generic_visit(node)

    visit_AsyncWith = visit_With

    def visit_comprehension(self, node: ast.comprehension) -> None:
        self._flag_attr_rebind([node.target], node.target, "comprehension target")
        self.generic_visit(node)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self._true_into([node.target], node.value, node)
        self.generic_visit(node)

    def visit_Dict(self, node: ast.Dict) -> None:
        if not self.in_gid():
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and k.value in _CACHED_KW and _is_const(v, True):
                    self.flag(node, f"{{{k.value!r}: True}} outside {_GID_STAGE_FN}")
        self.generic_visit(node)

    # value provenance of a cached/path_cached argument
    # PIN (Code, declared at LOCK v0.1): beyond DESIGN's "a name bound from the guard or
    # the literal False", a direct cached_path_admitted(...) call, an IfExp whose two
    # branches are licensed, and an `and` whose last operand is licensed are accepted:
    # none of them can yield True except through the guard.
    def _source_ok(self, v: ast.AST, gid: bool) -> bool:
        if _is_const(v, False):
            return True
        if _is_const(v, True):
            return gid
        if isinstance(v, ast.Call):
            c = self._licensed(v)
            return c == _ADMIT_FN or (gid and c == _GID_FN)
        if isinstance(v, ast.IfExp):
            return self._source_ok(v.body, gid) and self._source_ok(v.orelse, gid)
        if isinstance(v, ast.BoolOp):
            # `x and admitted(...)` is True only through its last operand; `or` can
            # return any truthy operand, so every operand must be a licensed source.
            if isinstance(v.op, ast.And):
                return self._source_ok(v.values[-1], gid)
            return all(self._source_ok(x, gid) for x in v.values)
        return False

    def _name_ok(self, name: str, at: ast.AST) -> bool:
        gid = self.in_gid()
        sc = self.scope()
        bound = False
        if not isinstance(sc, ast.Module):
            if any(p.arg == name for p, _, _ in _params(sc)):
                bound = True               # the caller's keyword is checked at its site
        for n in _local_nodes(sc):
            if isinstance(n, (ast.Global, ast.Nonlocal)) and name in n.names:
                self.flag(at, f"{name!r} declared global/nonlocal (unbound provenance)")
                return False
            # finding 20: a comprehension target, an except-as name, a match capture, an
            # import, a nested def/class of the name, or a del rebinds it unprovably.
            if _binds_name(n, name):
                return False
            if isinstance(n, ast.Assign) and any(name in _target_names(t) for t in n.targets):
                bound = True
                if not all(isinstance(t, ast.Name) for t in n.targets if name in _target_names(t)):
                    if not gid:
                        return False       # unpacked from a tuple: provenance unprovable
                elif not self._source_ok(n.value, gid):
                    return False
            elif isinstance(n, (ast.AnnAssign, ast.NamedExpr)) and name in _target_names(n.target):
                bound = True
                if n.value is None or not self._source_ok(n.value, gid):
                    return False
            elif isinstance(n, ast.AugAssign) and name in _target_names(n.target):
                return False
            elif isinstance(n, (ast.For, ast.AsyncFor)) and name in _target_names(n.target):
                bound = True
                it = n.iter
                lit = (isinstance(it, (ast.Tuple, ast.List)) and it.elts
                       and all(isinstance(e, ast.Constant) and type(e.value) is bool for e in it.elts))
                if not (gid and isinstance(n.target, ast.Name)
                        and (self._licensed(it) == _GID_FN or lit)):
                    return False
            elif isinstance(n, (ast.With, ast.AsyncWith)) and any(
                    i.optional_vars is not None and name in _target_names(i.optional_vars)
                    for i in n.items):
                return False
        return bound

    def _check_cached_value(self, kw: ast.keyword, via: str = "") -> None:
        v, gid = kw.value, self.in_gid()
        if isinstance(v, ast.Name):
            if v.id not in _CACHED_KW:
                self.flag(kw.value, f"{kw.arg}= takes a name other than cached/path_cached ({v.id!r}){via}")
            elif not self._name_ok(v.id, kw.value):
                self.flag(kw.value, f"{kw.arg}={v.id} is not bound only from {_ADMIT_FN}(...), "
                                    f"the literal False, or a keyword-only parameter"
                                    + ("" if gid else f" (or True / {_GID_FN}() inside {_GID_STAGE_FN})")
                                    + via)
            return
        if not self._source_ok(v, gid):
            what = "literal True" if _is_const(v, True) else type(v).__name__
            self.flag(kw.value, f"{kw.arg}= is a {what} outside the licensed sources "
                                f"({_ADMIT_FN}(...) / False; True and {_GID_FN}() only in "
                                f"{_GID_STAGE_FN}){via}")

    def _delegating_param(self, node: ast.Call, v: ast.AST, pname: str) -> bool:
        """``super().generate(..., injections=injections)`` inside an adapter's own
        ``generate`` forwards its caller's argument; the caller is checked instead."""
        sc = self.scope()
        f = node.func
        return (isinstance(sc, (ast.FunctionDef, ast.AsyncFunctionDef)) and sc.name == "generate"
                and isinstance(f, ast.Attribute) and isinstance(f.value, ast.Call)
                and isinstance(f.value.func, ast.Name) and f.value.func.id == "super"
                and isinstance(v, ast.Name) and v.id == pname
                and any(p.arg == pname for p, _, _ in _params(sc)))

    def visit_Call(self, node: ast.Call) -> None:
        name = _callee(node)
        if name in ("import_module", "__import__"):
            for a in node.args:
                if isinstance(a, ast.Constant) and isinstance(a.value, str) and "statepresent" in a.value:
                    self.flag(node, f"statepresent import ({name}({a.value!r}))")
        if name == "getattr" and len(node.args) >= 2 and isinstance(node.args[1], ast.Constant) \
                and node.args[1].value == "generate":
            self.flag(node, "getattr(..., 'generate') escapes the call-site check")
        self._flag_attr_rebind_call(node, name)
        if name in _SLOT_CALLS:
            f = node.func
            if any(isinstance(a, ast.Starred) for a in node.args):
                self.flag(node, f"*-unpacking into {name}( (arguments cannot be checked)")
            if (isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name)
                    and f.value.id[:1].isupper()):
                # Cls.generate(obj, prefix, seg, inj, ...) shifts every positional
                # slot by one; the form is refused, its slots never guessed.
                # PIN (Code, declared at LOCK v0.1): forward is held to the same rule.
                self.flag(node, f"unsupported form {f.value.id}.{name}( (an unbound-method call "
                                f"shifts the positional slots; call it on the instance)")
            elif len(node.args) > 3:
                # PIN (Code, declared at LOCK v0.1): no bound adapter generate/forward
                # takes more than three positional arguments, so a fourth means shifted
                # slots under some other unbound form (type(a).generate(a, ...)).
                self.flag(node, f"{name}( with more than three positional arguments (shifted "
                                f"slots: an unbound-method form)")
            elif len(node.args) >= 3 and not (_is_empty_literal(node.args[2])
                                              or self._delegating_param(node, node.args[2], "injections")):
                self.flag(node, f"non-empty or unprovable positional injections in {name}(")
        # Keyword arguments, with any **{...} dict literal into a guarded callee read
        # entry by entry exactly as keywords; any other ** into one is refused.
        kws: list[tuple[ast.keyword, str]] = []
        opaque = False
        for kw in node.keywords:
            if kw.arg is not None:
                kws.append((kw, ""))
                continue
            if name not in self.guarded:
                continue
            entries = _dict_literal_keywords(kw.value)
            if entries is None:
                opaque = True
                self.flag(kw.value, f"**-unpacking into {name}( of a mapping that is not a dict "
                                    f"literal with str keys (cached/injections cannot be checked)")
            else:
                kws += [(e, " (via a **-unpacked dict literal)") for e in entries]
        # PIN (Code, declared at LOCK v0.1): the path is declared at every generate
        # call -- an absent cached= is flagged, never read as the adapter's default.
        if name == "generate" and not opaque and not any(kw.arg == "cached" for kw, _ in kws):
            self.flag(node, "generate( without an explicit cached=")
        for kw, via in kws:
            # No exemption for test code: m's tests prove injections=() at runtime
            # (ScriptedAdapter.calls) and never pass a non-empty one.
            if kw.arg == "injections" and not (_is_empty_literal(kw.value)
                                               or self._delegating_param(node, kw.value, "injections")):
                self.flag(kw.value, f"non-empty or unprovable injections= argument{via}")
            if kw.arg in _CACHED_KW:
                self._check_cached_value(kw, via)
        self.generic_visit(node)


def check_call_sites(paths: Iterable[str | os.PathLike]) -> list[str]:
    """Static half of the cached-path guard over m's sources; [] = clean.

    PIN (Code, declared at LOCK v0.1): a directory argument is expanded to its *.py
    files (``__pycache__`` skipped); an unreadable or unparsable file is a problem,
    never a pass.
    """
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
            src = f.read_text(encoding="utf-8")
            trees.append((f, ast.parse(src, filename=str(f))))
        except (OSError, UnicodeDecodeError, SyntaxError, ValueError) as e:
            problems.append(f"{f}: cannot be checked ({type(e).__name__}: {e})")
    # First pass: every function in the scanned files that takes a path or an
    # injections argument is a guarded callee in every file.
    guarded = frozenset(n for _, tree in trees for n in _guarded_defs(tree))
    for f, tree in trees:
        scan = _CallSiteScan(str(f), tree, guarded)
        scan.visit(tree)
        problems += scan.problems
    return problems


# --- laptop preflight -----------------------------------------------------------
def _run(cmd: Sequence[str]) -> str | None:
    try:
        return subprocess.run(list(cmd), capture_output=True, text=True, timeout=15).stdout
    except (OSError, subprocess.SubprocessError):
        return None


def _adapter_watts(out: str) -> int | None:
    m = re.search(r"^\s*Wattage\s*=\s*(\d+)\s*W\b", out, re.M)
    return int(m.group(1)) if m else None


def _on_ac(out: str) -> bool:
    return re.search(r"^Now drawing from 'AC Power'", out, re.M) is not None


def _model_processes(out: str, exclude: set[int]) -> list[str]:
    hits = []
    for line in out.splitlines():
        pid_s, _, cmd = line.strip().partition(" ")
        if not pid_s.isdigit() or int(pid_s) in exclude:
            continue
        argv = cmd.split()
        exe = os.path.basename(argv[0]).lower() if argv else ""
        low = cmd.lower()
        if "python" in exe and any(m in low for m in MODEL_PROCESS_MARKERS):
            hits.append(f"{pid_s} {cmd[:160]}")
    return hits


def _self_and_ancestors() -> set[int]:
    pids, pid = {os.getpid()}, os.getpid()
    for _ in range(32):
        out = (_run(["ps", "-o", "ppid=", "-p", str(pid)]) or "").strip()
        if not out.isdigit() or int(out) <= 1:
            break
        pid = int(out)
        pids.add(pid)
    return pids


def preflight_laptop(*, pmset_adapter: str | None = None, pmset_ps: str | None = None,
                     pgrep: str | None = None, free_bytes: int | None = None,
                     exclude_pids: set[int] | None = None) -> list[str]:
    """m:267's laptop checklist before a detached Qwen run; [] = clear to launch.

    The keyword arguments exist for the model-free self-test (canned command output);
    a stage driver calls it with none, and the commands run.
    """
    problems: list[str] = []
    ad = _run(["pmset", "-g", "adapter"]) if pmset_adapter is None else pmset_adapter
    ps = _run(["pmset", "-g", "ps"]) if pmset_ps is None else pmset_ps
    if ad is None or ps is None:
        problems.append("POWER UNKNOWN: pmset unavailable (this is the laptop's preflight)")
    else:
        w = _adapter_watts(ad)
        if w is None:
            problems.append("POWER: no adapter wattage reported (no adapter attached?)")
        elif w < MIN_ADAPTER_WATTS:
            problems.append(f"POWER: adapter {w} W < {MIN_ADAPTER_WATTS} W")
        if not _on_ac(ps):
            problems.append("POWER: not drawing from AC power")
    pg = _run(["pgrep", "-ifl", "python"]) if pgrep is None else pgrep
    if pg is None:
        problems.append("PROCESSES UNKNOWN: pgrep unavailable")
    else:
        mine = _self_and_ancestors() if exclude_pids is None else set(exclude_pids)
        for h in _model_processes(pg, mine):
            problems.append(f"ONE PROCESS: another model process is running: {h}")
    free = shutil.disk_usage(REPO).free if free_bytes is None else free_bytes
    if free < DISK_HEADROOM_BYTES:
        problems.append(f"DISK: {free / 1024 ** 3:.1f} GiB free < "
                        f"{DISK_HEADROOM_BYTES // 1024 ** 3} GiB headroom")
    return problems


# --- self-test -------------------------------------------------------------------
_CLEAN_SRC = '''
from valence_core.m import guard

def run_session_x(adapter, prefix, seg, *, path_cached: bool, seed):
    return adapter.generate(prefix, seg, injections=(), seed=seed, cached=path_cached)

def run_olmo_x(adapter, prefix, seg, seed):
    return adapter.generate(prefix, seg, injections=(), seed=seed, cached=False)

def stage_x(adapter, unit, gate, bid):
    path_cached = (guard.cached_path_admitted(unit, gate, backend_identifier=bid) if gate == "qual"
                   else False)
    return run_session_x(adapter, "p", "s", path_cached=path_cached, seed=1)

def stage_direct(adapter, unit, bid):
    return run_session_x(adapter, "p", "s",
                         path_cached=guard.cached_path_admitted(unit, "qual", backend_identifier=bid), seed=2)

def run_gid_pair(adapter, unit):
    out = []
    for path_cached in guard.gid_paths():
        out.append(run_session_x(adapter, "p", "s", path_cached=path_cached, seed=3))
    out.append(adapter.generate("p", "s", injections=(), seed=4, cached=True))
    return out

class Scripted:
    def generate(self, prefix_text, segment_text, injections=(), *, seed=None, cached=False):
        return super().generate(prefix_text, segment_text, injections, seed=seed, cached=cached)
'''

# Each smuggle: (name, source, a substring the flag must carry).
_SP = "state" + "present"          # kept split so no line of this file reads as an import
_SMUGGLES = (
    ("literal cached=True outside run_gid_pair",
     "def f(a):\n    return a.generate('p', 's', injections=(), cached=True)\n", "literal True"),
    ("**{'cached': True} into generate",
     "def f(a):\n    return a.generate('p', 's', injections=(), **{'cached': True})\n",
     "literal True outside the licensed sources (cached_path_admitted(...) / False; True and "
     "gid_paths() only in run_gid_pair) (via a **-unpacked dict literal)"),
    ("injections=(x,)",
     "def f(a, x):\n    return a.generate('p', 's', injections=(x,), cached=False)\n", "injections="),
    ("positional injections",
     "def f(a, x):\n    return a.generate('p', 's', (x,), cached=False)\n", "positional injections"),
    ("Injection import",
     "from valence_core.adapters.base import Injection\n", "Injection import"),
    ("statepresent import (from-import)",
     f"from valence_core.e2b import {_SP}\n", "statepresent import"),
    ("statepresent import (module import)",
     f"import valence_core.e2b.{_SP} as sp\n", "statepresent import"),
    ("statepresent import (importlib)",
     f"import importlib\nm = importlib.import_module('valence_core.e2b.{_SP}')\n", "statepresent import"),
    ("cached = True, then cached=cached",
     "def f(a):\n    cached = True\n    return a.generate('p', 's', injections=(), cached=cached)\n",
     "cached = True"),
    ("parameter default path_cached=True",
     "def f(a, *, path_cached=True):\n    return a.generate('p', 's', injections=(), cached=path_cached)\n",
     "defaults to True"),
    ("positional path parameter",
     "def f(a, path_cached):\n    return a.generate('p', 's', injections=(), cached=path_cached)\n",
     "keyword-only"),
    ("cached from another name",
     "def f(a, flag):\n    return a.generate('p', 's', injections=(), cached=flag)\n", "other than"),
    ("generate aliased",
     "def f(a):\n    g = a.generate\n    return g('p', 's')\n", "without being called"),
    ("runner called with path_cached=True",
     "def f(a):\n    return run_session_x(a, 'p', 's', path_cached=True, seed=1)\n", "literal True"),
    ("gid_paths() iterated outside run_gid_pair",
     "def f(a):\n    for cached in gid_paths():\n        a.generate('p', 's', injections=(), cached=cached)\n",
     "not bound only"),
    ("generate without cached=",
     "def f(a):\n    return a.generate('p', 's', injections=())\n", "without an explicit cached="),
    ("`or` with a non-licensed operand",
     "def f(a, x):\n    cached = x or cached_path_admitted('Q-F0', 'qual')\n"
     "    return a.generate('p', 's', injections=(), cached=cached)\n", "not bound only"),
)

# Gaps (a)-(f): per gap, (label, must-fire sources with the flag's needle, must-not-fire
# sources). A tuple of sources is several files scanned together in one call.
_VIA = "(via a **-unpacked dict literal)"
_LIC = ("outside the licensed sources (cached_path_admitted(...) / False; True and gid_paths() "
        "only in run_gid_pair)")
_OPAQ = "**-unpacking into run_session_qwen( of a mapping"
_RUN_Q = "def f(a, sc, au, b{extra}):\n    return run_session_qwen(a, sc, au, b, {kw})\n"
_GAPS = (
    ("(a) a cached/path_cached default other than absent or the literal False",
     (("def f(a, *, cached=1):\n    return a.generate('p', 's', injections=(), cached=cached)\n",
       "'cached' defaults to 1"),
      ("def f(a, *, cached=True):\n    return a.generate('p', 's', injections=(), cached=cached)\n",
       "'cached' defaults to True"),
      ("def f(a, *, path_cached=None):\n    return run_session_qwen(a, 1, 2, 3, path_cached=path_cached)\n",
       "'path_cached' defaults to None"),
      ("FLAG = True\ndef f(a, *, path_cached=FLAG):\n"
       "    return run_session_qwen(a, 1, 2, 3, path_cached=path_cached)\n", "'path_cached' defaults to FLAG"),
      ("g = lambda a, *, cached=0: a.generate('p', 's', injections=(), cached=cached)\n",
       "'cached' defaults to 0"),
      ("def run_gid_pair(a, *, cached=True):\n    return a.generate('p', 's', injections=(), cached=cached)\n",
       "'cached' defaults to True")),
     ("def f(a, *, cached):\n    return a.generate('p', 's', injections=(), cached=cached)\n"
      "def g(a, *, path_cached=False):\n    return run_session_qwen(a, 1, 2, 3, path_cached=path_cached)\n"
      "h = lambda a, *, cached=False: a.generate('p', 's', injections=(), cached=cached)\n",)),
    ("(b) **mapping into a guarded callee unless a dict literal inspected as keywords",
     ((_RUN_Q.format(extra=", opts", kw="**opts"), _OPAQ),
      ("def f(m, a, opts):\n    return m.run_session_olmo(a, 1, 2, 3, **opts)\n",
       "**-unpacking into run_session_olmo( of a mapping"),
      ("def f(a, opts):\n    return a.generate('p', 's', **opts)\n",
       "**-unpacking into generate( of a mapping"),
      (("def stage_y(a, *, path_cached=False):\n"
        "    return a.generate('p', 's', injections=(), cached=path_cached)\n",
        "def f(a, opts):\n    return stage_y(a, **opts)\n"), "**-unpacking into stage_y( of a mapping"),
      (_RUN_Q.format(extra=", opts", kw="**{**opts}"), _OPAQ),
      (_RUN_Q.format(extra=", k", kw="**{k: False}"), _OPAQ),
      (_RUN_Q.format(extra="", kw="**dict(path_cached=False)"), _OPAQ),
      (_RUN_Q.format(extra="", kw="**{'path_cached': 1}"), f"path_cached= is a Constant {_LIC} {_VIA}"),
      (_RUN_Q.format(extra="", kw="**{'path_cached': True}"), f"literal True {_LIC} {_VIA}"),
      ("def f(a, flag):\n    return a.generate('p', 's', **{'injections': (), 'cached': flag})\n",
       f"other than cached/path_cached ('flag') {_VIA}"),
      ("def f(a, x):\n    return a.generate('p', 's', **{'injections': (x,), 'cached': False})\n",
       f"non-empty or unprovable injections= argument {_VIA}"),
      ("def f(a, x):\n    return a.forward([1], **{'injections': (x,)})\n",
       f"non-empty or unprovable injections= argument {_VIA}"),
      ("def f(a):\n    return a.generate('p', 's', **{'injections': ()})\n",
       "without an explicit cached=")),
     (_RUN_Q.format(extra=", rx", kw="**{'path_cached': False, 'term_rx': rx}")
      + "def g(a):\n    return a.generate('p', 's', **{'injections': (), 'cached': False})\n"
      + "from valence_core.m import guard\n"
      + "def h(a, unit, sc, au, b):\n    path_cached = guard.cached_path_admitted(unit, 'qual')\n"
      + "    return run_session_qwen(a, sc, au, b, **{'path_cached': path_cached})\n"
      + "def k(rec, kw):\n    return verify_session(rec, **kw)\n",
      ("def stage_y(a, *, path_cached=False):\n"
       "    return a.generate('p', 's', injections=(), cached=path_cached)\n",
       "def f(a, opts):\n    return other_fn(a, **opts)\n"
       "def g(a):\n    return stage_y(a, **{'path_cached': False})\n"),
      "def f(a, opts):\n    return stage_y(a, **opts)\n")),       # stage_y not defined in the scan
    ("(c) the unbound-method form Name.generate(...) (shifted positional slots)",
     (("def f(obj, x):\n    return Adapter.generate(obj, 'p', (), (x,), cached=False)\n",
       "unsupported form Adapter.generate("),
      ("def f(self):\n    return SelfTestAdapter.generate(self, 'p', 's', cached=False)\n",
       "unsupported form SelfTestAdapter.generate("),
      ("def f(obj, x):\n    return Adapter.forward(obj, [1], (), (x,))\n",
       "unsupported form Adapter.forward("),
      ("def f(a, x):\n    return type(a).generate(a, 'p', (), (x,), cached=False)\n",
       "more than three positional arguments"),
      ("def f(a, x):\n    return _Ad.generate(a, 'p', (), (x,), cached=False)\n",
       "more than three positional arguments")),
     ("def f(a):\n    return a.generate('p', 's', (), cached=False)\n"
      "def g(adapter, ids):\n    return adapter.forward(ids, (), ())\n"
      "class S(Base):\n    def generate(self, p, s, injections=(), *, cached=False):\n"
      "        return super().generate(p, s, injections, cached=cached)\n",)),
    ("(e) licensed sources resolved by binding, not spelling (finding 20)",
     (("def cached_path_admitted(*a):\n    return True\n"
       "def f(a):\n    return a.generate('p', 's', injections=(), cached=cached_path_admitted('Q-F0', 'qual'))\n",
       "'cached_path_admitted' bound by def"),
      ("cached_path_admitted = lambda *a: not False\n"
       "def f(a):\n    cached = cached_path_admitted('Q-F0', 'qual')\n"
       "    return a.generate('p', 's', injections=(), cached=cached)\n",
       "'cached_path_admitted' bound by assign"),
      ("class X:\n    @staticmethod\n    def cached_path_admitted(*a):\n        return 1 == 1\n"
       "def f(a):\n    return a.generate('p', 's', injections=(), cached=X.cached_path_admitted())\n",
       "'cached_path_admitted' bound by def"),
      ("class X:\n    @staticmethod\n    def cached_path_admitted(*a):\n        return 1 == 1\n"
       "def f(a):\n    return a.generate('p', 's', injections=(), cached=X.cached_path_admitted())\n",
       "cached= is a Call outside the licensed sources"),
      ("from valence_core.m import keys as guard\n"
       "def f(a):\n    return a.generate('p', 's', injections=(), cached=guard.cached_path_admitted('Q-F0', 'q'))\n",
       "cached= is a Call outside the licensed sources"),
      ("from valence_core.m import guard\nguard = object()\n"
       "def f(a):\n    return a.generate('p', 's', injections=(), cached=guard.cached_path_admitted('Q-F0', 'q'))\n",
       "cached= is a Call outside the licensed sources"),
      ("from somewhere_else import cached_path_admitted\n"
       "def f(a):\n    return a.generate('p', 's', injections=(), cached=cached_path_admitted('Q-F0', 'q'))\n",
       "bound by from (somewhere_else.cached_path_admitted)"),
      ("from valence_core.m.guard import gid_paths as cached_path_admitted\n"
       "def f(a):\n    return a.generate('p', 's', injections=(), cached=cached_path_admitted())\n",
       "bound by from (valence_core.m.guard.gid_paths)"),
      ("import os as gid_paths\n", "'gid_paths' bound by import"),
      ("def f(a, *, cached=False):\n"
       "    return [a.generate('p', 's', injections=(), cached=cached) for cached in (True,)]\n",
       "cached=cached is not bound only"),
      ("def f(a, sc, au, b, *, path_cached=False):\n"
       "    return [run_session_qwen(a, sc, au, b, path_cached=path_cached, term_rx=()) "
       "for path_cached in (1 == 1,)]\n", "path_cached=path_cached is not bound only"),
      ("def f(a, *, cached=False):\n    try:\n        raise ValueError\n"
       "    except ValueError as cached:\n        return a.generate('p', 's', injections=(), cached=cached)\n",
       "cached=cached is not bound only"),
      ("def f(a, *, cached=False):\n    match not False:\n        case cached:\n"
       "            return a.generate('p', 's', injections=(), cached=cached)\n",
       "cached=cached is not bound only"),
      ("def f(a, *, cached=False):\n    import builtins as cached\n"
       "    return a.generate('p', 's', injections=(), cached=cached)\n", "cached=cached is not bound only"),
      ("def run_campaign(a):\n    def run_gid_pair():\n"
       "        return a.generate('p', 's', injections=(), cached=True)\n    return run_gid_pair()\n",
       "literal True outside the licensed sources"),
      ("from valence_core.m import guard\n"
       "def run_gid_pair(a):\n    def inner():\n"
       "        for cached in guard.gid_paths():\n"
       "            a.generate('p', 's', injections=(), cached=cached)\n    return inner()\n",
       "cached=cached is not bound only"),
      ("class G:\n    def run_gid_pair(self, a):\n"
       "        return a.generate('p', 's', injections=(), cached=True)\n",
       "literal True outside the licensed sources")),
     ("from valence_core.m import guard\n"
      "from valence_core.m.guard import cached_path_admitted, gid_paths\n"
      "from valence_core.m.guard import cached_path_admitted as cpa\n"
      "from valence_core.m import guard as g2\n"
      "import valence_core.m.guard as g3\n"
      "def f(a, u):\n    return a.generate('p', 's', injections=(), cached=cached_path_admitted(u, 'qual'))\n"
      "def f2(a, u):\n    return a.generate('p', 's', injections=(), cached=cpa(u, 'qual'))\n"
      "def f3(a, u):\n    path_cached = g2.cached_path_admitted(u, 'qual')\n"
      "    return run_session_qwen(a, 1, 2, 3, path_cached=path_cached)\n"
      "def f4(a, u):\n    return a.generate('p', 's', injections=(), cached=g3.cached_path_admitted(u, 'campaign'))\n"
      "def run_gid_pair(a):\n    for cached in gid_paths():\n"
      "        a.generate('p', 's', injections=(), cached=cached)\n"
      "    for path_cached in guard.gid_paths():\n"
      "        run_session_qwen(a, 1, 2, 3, path_cached=path_cached)\n",
      "from . import guard\nfrom .guard import cached_path_admitted\n"
      "def f(a, u):\n    cached = guard.cached_path_admitted(u, 'qual') and cached_path_admitted(u, 'qual')\n"
      "    return a.generate('p', 's', injections=(), cached=cached)\n",
      "import valence_core.m.guard\n"
      "def f(a, u):\n    return a.generate('p', 's', injections=(), "
      "cached=valence_core.m.guard.cached_path_admitted(u, 'qual'))\n",
      "def f(a, *, cached=False):\n    xs = [c for c in (1, 2)]\n"
      "    return a.generate('p', 's', injections=(), cached=cached)\n")),
    ("(d) a non-empty injections= in test code (no exemption)",
     (("def _selftest(chk):\n    ad = ScriptedAdapter()\n"
       "    ad.generate('p', 's', injections=(object(),), cached=False)\n",
       "non-empty or unprovable injections="),
      ("class ScriptedAdapter(SelfTestAdapter):\n"
       "    def generate(self, p, s, injections=(), *, cached=False):\n"
       "        return super().generate(p, s, injections=(1,), cached=cached)\n",
       "non-empty or unprovable injections="),
      ("def test_refusal(ad, x):\n    return ad.forward([1], injections=[x])\n",
       "non-empty or unprovable injections=")),
     ("def _selftest(chk):\n    ad = ScriptedAdapter()\n"
      "    ad.generate('p', 's', injections=(), cached=False)\n"
      "    chk('x', ad.calls[-1]['injections'] == ())\n",)),
    ("(f) a licensed name rebound as an attribute (finding N15)",
     (("from . import guard\nguard.cached_path_admitted = lambda *a, **k: True\n"
       "def f(a):\n    return a.generate('p', 's', injections=(), "
       "cached=guard.cached_path_admitted('Q-F0', 'qual', backend_identifier='x'))\n",
       f"'{_ADMIT_FN}' rebound as an attribute (assignment)"),
      ("from valence_core.m import guard\nguard.gid_paths = lambda: (True, True)\n",
       "'gid_paths' rebound as an attribute (assignment)"),
      ("import valence_core.m.guard\nvalence_core.m.guard.cached_path_admitted = print\n",
       f"'{_ADMIT_FN}' rebound as an attribute (assignment)"),
      ("def f(m):\n    m.x, m.cached_path_admitted = 1, (lambda *a, **k: True)\n",
       f"'{_ADMIT_FN}' rebound as an attribute (assignment)"),
      ("from . import guard\nguard.cached_path_admitted: object = lambda *a, **k: True\n",
       f"'{_ADMIT_FN}' rebound as an attribute (annotated assignment)"),
      ("from . import guard\nguard.gid_paths |= print\n",
       "'gid_paths' rebound as an attribute (augmented assignment)"),
      ("from . import guard\ndel guard.gid_paths\n", "'gid_paths' rebound as an attribute (del)"),
      ("from . import guard\nvars(guard)['cached_path_admitted'] = print\n",
       f"'{_ADMIT_FN}' rebound as an attribute (assignment)"),
      ("from . import guard\nsetattr(guard, 'cached_path_admitted', lambda *a, **k: True)\n",
       f"'{_ADMIT_FN}' rebound as an attribute (setattr(...))"),
      ("def f(m):\n    setattr(m, \"gid_paths\", lambda: (True, True))\n",
       "'gid_paths' rebound as an attribute (setattr(...))"),
      ("from . import guard\ndelattr(guard, 'gid_paths')\n",
       "'gid_paths' rebound as an attribute (delattr(...))"),
      ("import sys\nobject.__setattr__(sys.modules['valence_core.m.guard'], 'cached_path_admitted', print)\n",
       f"'{_ADMIT_FN}' rebound as an attribute (__setattr__(...))"),
      ("from unittest import mock\nfrom . import guard\n"
       "with mock.patch.object(guard, 'cached_path_admitted', lambda *a, **k: True):\n    pass\n",
       f"'{_ADMIT_FN}' rebound as an attribute (object(...))"),
      ("from unittest import mock\nfrom . import guard\n"
       "with mock.patch.object(guard, attribute='gid_paths', new=print):\n    pass\n",
       "'gid_paths' rebound as an attribute (object(...))"),
      ("from unittest import mock\n"
       "with mock.patch('valence_core.m.guard.gid_paths', lambda: (True, True)):\n    pass\n",
       "'gid_paths' rebound as an attribute (patch(...))"),
      # finding R7: loop, with and comprehension targets; bound dunders; patch.multiple /
      # patch.dict; the module dict's update; pytest's dotted setattr / delattr
      ("from . import guard\nfor guard.cached_path_admitted in (lambda *a, **k: True,):\n    pass\n",
       f"'{_ADMIT_FN}' rebound as an attribute (for target)"),
      ("from . import guard\nasync def f(xs):\n    async for guard.gid_paths in xs:\n        pass\n",
       "'gid_paths' rebound as an attribute (for target)"),
      ("from . import guard\nwith open('x') as guard.cached_path_admitted:\n    pass\n",
       f"'{_ADMIT_FN}' rebound as an attribute (with target)"),
      ("from . import guard\nasync def f(cm):\n    async with cm as (x, guard.gid_paths):\n        pass\n",
       "'gid_paths' rebound as an attribute (with target)"),
      ("from . import guard\nxs = [0 for guard.cached_path_admitted in (print,)]\n",
       f"'{_ADMIT_FN}' rebound as an attribute (comprehension target)"),
      ("from . import guard\nxs = {0: 1 for vars(guard)['gid_paths'] in (print,)}\n",
       "'gid_paths' rebound as an attribute (comprehension target)"),
      ("from . import guard\nguard.__setattr__('cached_path_admitted', lambda *a, **k: True)\n",
       f"'{_ADMIT_FN}' rebound as an attribute (__setattr__(...))"),
      ("from . import guard\nguard.__delattr__('gid_paths')\n",
       "'gid_paths' rebound as an attribute (__delattr__(...))"),
      ("from . import guard\nguard.__dict__.__setitem__('gid_paths', print)\n",
       "'gid_paths' rebound as an attribute (__setitem__(...))"),
      ("from . import guard\nguard.__dict__.update(cached_path_admitted=print)\n",
       f"'{_ADMIT_FN}' rebound as an attribute (update(...))"),
      ("from . import guard\nvars(guard).update({'gid_paths': print})\n",
       "'gid_paths' rebound as an attribute (update(...))"),
      ("from unittest import mock\nfrom . import guard\n"
       "with mock.patch.multiple(guard, cached_path_admitted=print):\n    pass\n",
       f"'{_ADMIT_FN}' rebound as an attribute (multiple(...))"),
      ("from unittest.mock import patch\nfrom . import guard\n"
       "with patch.dict(guard.__dict__, {'gid_paths': print}):\n    pass\n",
       "'gid_paths' rebound as an attribute (dict(...))"),
      ("from unittest import mock\nfrom . import guard\n"
       "with mock.patch.dict(guard.__dict__, gid_paths=print):\n    pass\n",
       "'gid_paths' rebound as an attribute (dict(...))"),
      ("def test_x(monkeypatch):\n"
       "    monkeypatch.setattr('valence_core.m.guard.cached_path_admitted', lambda *a, **k: True)\n",
       f"'{_ADMIT_FN}' rebound as an attribute (setattr(...))"),
      ("def test_x(monkeypatch):\n    monkeypatch.delattr('valence_core.m.guard.gid_paths')\n",
       "'gid_paths' rebound as an attribute (delattr(...))")),
     ("from unittest import mock\nfrom . import guard\n"
      "guard.GATES_DIR = None\nguard.cached_path_admitted_count = 3\nguard.gates['gid'] = 1\n"
      "setattr(guard, 'GATES_DIR', None)\ndelattr(guard, 'GATES_DIR')\n"
      "def patched(obj, attr, value):\n    setattr(obj, attr, value)\n"
      "def f(a, u):\n    cached = guard.cached_path_admitted(u, 'qual', backend_identifier='x')\n"
      "    return a.generate('p', 's', injections=(), cached=cached)\n"
      "with mock.patch.object(guard, 'GATES_DIR', None), mock.patch(f'{__name__}.gid_artifact_path'):\n"
      "    pass\n"
      "with mock.patch('valence_core.m.guard.gid_paths_note'):\n    pass\n"
      # the R7 forms on other names are not monkeypatches of the licence
      "import os\n"
      "for guard.other in (1,):\n    pass\n"
      "with open('x') as fh:\n    pass\n"
      "ys = [y for y in (1, 2)]\n"
      "guard.__setattr__('GATES_DIR', None)\n"
      "guard.__dict__.update(GATES_DIR=None)\n"
      "vars(guard).update({'GATES_DIR': None})\n"
      "with mock.patch.dict(os.environ, {'X': '1'}), mock.patch.multiple(guard, GATES_DIR=None):\n"
      "    pass\n"
      "def test_x(monkeypatch):\n    monkeypatch.setattr('valence_core.m.guard.GATES_DIR', None)\n",)),
)


def _selftest(chk) -> None:
    import contextlib
    import sys
    import tempfile
    import types
    from unittest import mock

    import numpy as np

    from valence_core.e2d.runner import FORBIDDEN_MODULES as E2D_FORBIDDEN

    chk("guard: FORBIDDEN_MODULES == e2d/runner.py:53's tuple", FORBIDDEN_MODULES == E2D_FORBIDDEN,
        FORBIDDEN_MODULES)
    sp = FORBIDDEN_MODULES[0]

    @contextlib.contextmanager
    def planted():
        """A dummy module under the quarantined name, restored exactly afterwards."""
        had, prev = sp in sys.modules, sys.modules.get(sp)
        sys.modules[sp] = types.ModuleType(sp)
        try:
            yield
        finally:
            if had:
                sys.modules[sp] = prev
            else:
                del sys.modules[sp]

    # insulation
    try:
        assert_insulated()
        ok = True
    except SystemExit:
        ok = False
    chk("guard: assert_insulated passes with the primitive absent", ok and sp not in sys.modules)
    with planted():
        try:
            assert_insulated()
            fired = False
        except SystemExit as e:
            fired = "STRUCTURAL VIOLATION" in str(e)
    chk("guard: assert_insulated fires when the primitive is in sys.modules", fired)

    # the read, driving the REAL readout.choice_read through the stub adapter
    scripts = str(REPO / "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    from box_selftest_stub import SelfTestAdapter

    class _Drift(SelfTestAdapter):
        """Second forward of each read differs: construction drift."""
        def __init__(self, nan: bool = False) -> None:
            super().__init__("m-guard-drift")
            self._k, self._nan = 0, nan

        def forward(self, ids, capture_layers=(), injections=()):
            r = super().forward(ids, capture_layers=capture_layers)
            self._k += 1
            if self._k % 2 == 0:
                lg = r.logits.copy()
                if self._nan:
                    lg[0] = np.nan
                else:
                    lg = lg + np.linspace(0.0, 1.0, lg.shape[0], dtype=np.float32)
                r = dataclasses.replace(r, logits=lg)
            return r

    ad = SelfTestAdapter("m-guard")
    lids = label_ids(ad, ("slate", "prism"))
    chk("guard: label_ids accepts single-token labels (ints, distinct)",
        sorted(lids) == ["prism", "slate"] and all(type(v) is int for v in lids.values())
        and len(set(lids.values())) == 2, lids)
    for nm, labs in (("a two-token label", ("slate", "two words")), ("duplicate labels", ("slate", "slate"))):
        try:
            label_ids(ad, labs)
            ok = False
        except SystemExit:
            ok = True
        chk(f"guard: label_ids refuses {nm}", ok)

    prefix = "Session banner.\nRound 1 [slate]\nTask: name a colour.\nResponse: blue\nNext config:"
    cr = insulated_read(ad, prefix, "slate", "prism", lids)
    chk("guard: insulated_read accepts a reproducible read (verify KL exactly 0.0, real choice_read)",
        isinstance(cr, ChoiceRead) and cr.verify_kl == 0.0 and cr.pick in ("slate", "prism"),
        {"kl": cr.verify_kl, "has_pick": cr.pick in ("slate", "prism")})

    def _refuses(fn, exc=SystemExit, needle: str = "") -> bool:
        try:
            fn()
            return False
        except exc as e:
            return needle in str(e)

    with planted():
        ok = _refuses(lambda: insulated_read(ad, prefix, "slate", "prism", lids),
                      needle="STRUCTURAL VIOLATION")
    chk("guard: insulated_read refuses before reading when the primitive is loaded", ok)
    chk("guard: insulated_read halts on construction drift (KL > 0)",
        _refuses(lambda: insulated_read(_Drift(), prefix, "slate", "prism", lids),
                 needle="CONSTRUCTION INCIDENT"))
    nan_ad = _Drift(nan=True)
    direct = choice_read(nan_ad, prefix, "slate", "prism", lids, verify=True)
    try:
        assert_construction_stable(direct)
        frozen_passes = True
    except SystemExit:
        frozen_passes = False
    chk("guard: a NaN verify KL passes the frozen assert but insulated_read halts on it",
        frozen_passes and _refuses(lambda: insulated_read(_Drift(nan=True), prefix, "slate",
                                                          "prism", lids), needle="not exactly 0.0"),
        repr(direct.verify_kl))
    real = choice_read(ad, prefix, "slate", "prism", lids, verify=True)

    def _with_kl(kl):
        def fake(*a, **k):
            return dataclasses.replace(real, verify_kl=kl)
        return fake
    halted, passed = [], []
    for kl in (-1e-12, -5e-324, -0.5, 1e-300, float("inf")):
        with mock.patch(f"{__name__}.choice_read", _with_kl(kl)):
            halted.append(_refuses(lambda: insulated_read(ad, prefix, "slate", "prism", lids),
                                   needle="CONSTRUCTION INCIDENT"))
    with mock.patch(f"{__name__}.choice_read", _with_kl(0.0)):
        passed.append(insulated_read(ad, prefix, "slate", "prism", lids).verify_kl == 0.0)
    with mock.patch(f"{__name__}.choice_read", _with_kl(None)):
        passed.append(_refuses(lambda: insulated_read(ad, prefix, "slate", "prism", lids),
                               exc=(ValueError, SystemExit)))
    chk("guard: insulated_read halts on a NEGATIVE verify KL (which the frozen assert passes) and on "
        "any nonzero one, and accepts exactly 0.0 (finding 38)", all(halted) and all(passed),
        (halted, passed))
    chk("guard: insulated_read halts on a window overflow (8192)",
        _refuses(lambda: insulated_read(ad, "w " * 9000, "slate", "prism", lids), needle="WINDOW"))
    chk("guard: insulated_read refuses a == b",
        _refuses(lambda: insulated_read(ad, prefix, "slate", "slate", lids), exc=ValueError))

    # the cached-path licence
    chk("guard: gid_artifact_path is REPO/data/m/gates/{unit}_G-ID.json",
        gid_artifact_path("Q-F0") == REPO / "data" / "m" / "gates" / "Q-F0_G-ID.json")
    chk("guard: gid_artifact_path refuses an OLMo unit",
        _refuses(lambda: gid_artifact_path("OLMo-dpo"), exc=ValueError))
    chk("guard: gid_paths is (uncached, cached)", gid_paths() == (False, True))
    BX, BY = "d21ab386dd82282e", "efed3a541403edbb"       # two backends (finding 19's pair)
    good = {"unit": "Q-F0", "criterion": GID_CRITERION, "verdict": "PASS", "n_pairs": 2,
            "pairs_identical": [True, True], "identity": {"backend_identifier": BX}}
    variants = {
        "missing file": None, "not JSON": b"{not json", "not UTF-8": b"\xff\xfe",
        "a JSON list": [good], "unit mismatch": {**good, "unit": "Q-F3"},
        "criterion differs": {**good, "criterion": "2/2 identical"},
        "verdict FAIL": {**good, "verdict": "FAIL"}, "verdict lower-case": {**good, "verdict": "pass"},
        "n_pairs 1": {**good, "n_pairs": 1}, "n_pairs '2'": {**good, "n_pairs": "2"},
        "n_pairs 2.0": {**good, "n_pairs": 2.0},
        "pairs [true,false]": {**good, "pairs_identical": [True, False]},
        "pairs [true]": {**good, "pairs_identical": [True]},
        "pairs [1,1]": {**good, "pairs_identical": [1, 1]},
        "pairs [true,true,true]": {**good, "pairs_identical": [True, True, True]},
        "pairs missing": {k: v for k, v in good.items() if k != "pairs_identical"},
        "verdict missing": {k: v for k, v in good.items() if k != "verdict"},
        "identity missing": {k: v for k, v in good.items() if k != "identity"},
        "identity without backend_identifier": {**good, "identity": {"path": "cached+uncached"}},
        "identity not a dict": {**good, "identity": [BX]},
        "backend_identifier null": {**good, "identity": {"backend_identifier": None}},
        "backend_identifier another backend": {**good, "identity": {"backend_identifier": BY}},
        "backend_identifier at the top level only": {**{k: v for k, v in good.items() if k != "identity"},
                                                      "backend_identifier": BX},
    }
    with tempfile.TemporaryDirectory() as td:
        art = Path(td) / "Q-F0_G-ID.json"

        def put(content) -> None:
            if art.exists():
                art.unlink()
            if content is None:
                return
            art.write_bytes(content if isinstance(content, bytes) else json.dumps(content).encode())

        with mock.patch(f"{__name__}.gid_artifact_path", lambda unit: art):
            put(good)
            chk("guard: cached_path_admitted True on a well-formed PASS from this backend (Q-F0 qual, "
                "campaign)",
                cached_path_admitted("Q-F0", "qual", backend_identifier=BX)
                and cached_path_admitted("Q-F0", "campaign", backend_identifier=BX))
            chk("guard: a PASS produced on backend X licenses X and refuses Y (rule 2, per backend)",
                cached_path_admitted("Q-F0", "qual", backend_identifier=BX) is True
                and cached_path_admitted("Q-F0", "qual", backend_identifier=BY) is False
                and cached_path_admitted("Q-F0", "campaign", backend_identifier=BY) is False)
            chk("guard: backend_identifier is required, keyword-only, a non-empty str",
                _refuses(lambda: cached_path_admitted("Q-F0", "qual"), exc=TypeError)
                and _refuses(lambda: cached_path_admitted("Q-F0", "qual", BX), exc=TypeError)
                and _refuses(lambda: cached_path_admitted("Q-F0", "qual", backend_identifier=None),
                             exc=TypeError)
                and _refuses(lambda: cached_path_admitted("Q-F0", "qual", backend_identifier=""),
                             exc=TypeError))
            chk("guard: cached_path_admitted False at G-TIME-F0 even with a PASS on disk (m:280)",
                cached_path_admitted("Q-F0", "time", backend_identifier=BX) is False)
            chk("guard: cached_path_admitted False on OLMo whatever is on disk (m:267)",
                not any(cached_path_admitted(f"OLMo-{c}", st, backend_identifier=BX) for c in keys.CKPTS
                        for st in ("time", "qual", "campaign")))
            chk("guard: cached_path_admitted raises at stage 'id' (G-ID uses gid_paths)",
                _refuses(lambda: cached_path_admitted("Q-F0", "id", backend_identifier=BX), exc=ValueError,
                         needle="gid_paths"))
            chk("guard: cached_path_admitted refuses an unknown stage / a Q-F3 unit",
                _refuses(lambda: cached_path_admitted("Q-F0", "launch", backend_identifier=BX),
                         exc=ValueError)
                and _refuses(lambda: cached_path_admitted("Q-F3", "qual", backend_identifier=BX),
                             exc=NotImplementedError))
            granted = []
            for nm, content in variants.items():
                put(content)
                if cached_path_admitted("Q-F0", "qual", backend_identifier=BX):
                    granted.append(nm)
            chk(f"guard: every malformed or other-backend G-ID artifact -> uncached ({len(variants)} "
                f"variants)", not granted, granted)

    # the static call-site check
    with tempfile.TemporaryDirectory() as td:
        clean = Path(td) / "clean.py"
        clean.write_text(_CLEAN_SRC)
        got = check_call_sites([clean])
        chk("guard: check_call_sites passes a clean example (param, False, admitted, IfExp, "
            "run_gid_pair, super() delegation)", got == [], got)
        missed = []
        for i, (nm, src, needle) in enumerate(_SMUGGLES):
            f = Path(td) / f"smuggle_{i}.py"
            f.write_text(src)
            hits = check_call_sites([f])
            if not any(needle in h for h in hits):
                missed.append((nm, hits))
        chk(f"guard: check_call_sites fires on every smuggled copy ({len(_SMUGGLES)})",
            not missed, missed)

        def scan_src(tag: str, src) -> list[str]:
            fs = []
            for j, s in enumerate((src,) if isinstance(src, str) else src):
                fs.append(Path(td) / f"{tag}_{j}.py")
                fs[-1].write_text(s)
            return check_call_sites(fs)

        for gi, (label, fires, cleans) in enumerate(_GAPS):
            missed, noisy = [], []
            for k, (src, needle) in enumerate(fires):
                hits = scan_src(f"gap{gi}_fire{k}", src)
                if not any(needle in h for h in hits):
                    missed.append((k, hits))
            chk(f"guard: {label}: fires on every must-fire source ({len(fires)})", not missed, missed)
            for k, src in enumerate(cleans):
                hits = scan_src(f"gap{gi}_clean{k}", src)
                if hits:
                    noisy.append((k, hits))
            chk(f"guard: {label}: silent on every must-not-fire source ({len(cleans)})", not noisy, noisy)
        bad = Path(td) / "broken.py"
        bad.write_text("def f(:\n")
        chk("guard: check_call_sites reports an unparsable file (fails closed)",
            any("cannot be checked" in h for h in check_call_sites([bad])))
        sub = Path(td) / "pkg"
        sub.mkdir()
        (sub / "a.py").write_text(_SMUGGLES[0][1])
        chk("guard: check_call_sites expands a directory", len(check_call_sites([sub])) >= 1)
    here = Path(__file__).resolve().parent
    own = [here / n for n in ("guard.py", "resume.py", "keys.py", "__init__.py") if (here / n).exists()]
    got = check_call_sites(own)
    chk("guard: check_call_sites is clean on guard/resume/keys/__init__", got == [],
        got or [p.name for p in own])

    # laptop preflight, on canned command output only
    AD_OK = " Wattage = 140W\n Current = 4990mA\n Adapter Name = 140W USB-C Power Adapter\n"
    PS_AC = "Now drawing from 'AC Power'\n -InternalBattery-0 (id=1)\t80%; AC attached;\n"
    PS_BATT = "Now drawing from 'Battery Power'\n -InternalBattery-0 (id=1)\t80%; discharging;\n"
    PG_OK = ("1040 /Users/u/.vscode/extensions/ms-python.python/python-env-tools/bin/pet server\n"
             "1074 /opt/homebrew/Cellar/python@3.14/Python /u/.vscode/black/lsp_server.py\n")
    PG_ME = PG_OK + "777 /r/jspace-lab/jlens-qwen36/.venv/bin/python scripts/m_sessions.py\n"
    PG_OTHER = PG_OK + "888 /r/jspace-lab/jlens-qwen36/.venv/bin/python scripts/e2d_sessions.py\n"
    PG_KERNEL = PG_OK + "999 /u/miniconda3/envs/x/bin/python -m ipykernel_launcher --f=k.json\n"
    base = dict(pmset_adapter=AD_OK, pmset_ps=PS_AC, pgrep=PG_ME, free_bytes=50 * 1024 ** 3,
                exclude_pids={777})
    got = preflight_laptop(**base)
    chk("guard: preflight_laptop clear on 140 W AC, only self running, 50 GiB free", got == [], got)
    cases = {
        "a 60 W adapter": dict(pmset_adapter=" Wattage = 60W\n"),
        "no adapter attached": dict(pmset_adapter="No adapter attached.\n"),
        "battery power": dict(pmset_ps=PS_BATT),
        "another model process": dict(pgrep=PG_OTHER),
        "a live notebook kernel": dict(pgrep=PG_KERNEL),
        "self not excluded": dict(exclude_pids=set()),
        "1 GiB free": dict(free_bytes=1024 ** 3),
    }
    silent = [nm for nm, over in cases.items() if not preflight_laptop(**{**base, **over})]
    chk(f"guard: preflight_laptop fires on each failing condition ({len(cases)})", not silent, silent)
    PG_WRAP = PG_OK + (
        "22271 /bin/zsh -c source /u/.zsh/snapshot-zsh-1.sh && eval '/r/jspace-lab/jlens-qwen36/.venv/"
        "bin/python scripts/m_sessions.py --selftest' < /dev/null\n"
        "22280 /bin/zsh -c until pgrep -f jlens-qwen36/.venv/bin/python; do sleep 5; done\n"
        "22290 less /r/jspace-lab/jlens-qwen36/notes_python.txt\n"
        "22300 tail -f /r/jspace-lab/results/raw/qwen_python_run.txt\n")
    PG_REAL = PG_OK + (
        "31000 /r/jspace-lab/jlens-qwen36/.venv/bin/python3.12 scripts/e2d_sessions.py\n"
        "31010 /opt/homebrew/bin/Python -m mlx_lm.generate --model q\n"
        "31020 python3 -m ipykernel_launcher -f k.json\n")
    wrap_hits = _model_processes(PG_WRAP, set())
    real_hits = [h.split(" ", 1)[0] for h in _model_processes(PG_REAL, set())]
    chk("guard: a model process is matched on its executable -- shell wrappers and viewers whose "
        "arguments name the jlens python are not model processes (finding 23); python3.12 / Python "
        "/ python3 executables running the model stack are",
        wrap_hits == [] and real_hits == ["31000", "31010", "31020"]
        and preflight_laptop(**{**base, "pgrep": PG_WRAP}) == []
        and len(preflight_laptop(**{**base, "pgrep": PG_REAL})) == 3, (wrap_hits, real_hits))
    chk("guard: preflight parsers (wattage, AC, process list)",
        _adapter_watts(AD_OK) == 140 and _adapter_watts("No adapter attached.") is None
        and _on_ac(PS_AC) and not _on_ac(PS_BATT)
        and _model_processes(PG_OTHER, set()) and not _model_processes(PG_OK, set()))
    chk("guard: the quarantined primitive is still absent after the self-test", sp not in sys.modules)
