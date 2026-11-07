"""PROPOSAL-p's guard: the package hash, the licence's file sha256s, the import set, the roots p refuses, the
link-safe writer, and the static form of the register's term (e) (p v0.2 §4.2; ans2 Q0, Q3, Q4 (ii)).

THE LICENCE (p §4.2, C2's form). LOCK-p v0.1 names this package's ``package_sha256`` (computed as
``valence_core.m.resume.package_sha256_of`` computes m's: every ``*.py`` directly in the package), the file sha256
of each ``valence_core.m`` module p imports -- the modules a fresh interpreter holds after importing every p
production module (``M_IMPORTED``, measured), with the package's ``__init__.py`` -- and of
``valence_core/adapters/olmo_hf.py``, each by name on one lock line, and the register. The BUILD entry prints them
(``licence_lines``); every non-stub p stage checks them at start once a lock names them.

THE ROOTS (ans2 Q4 (ii)). p writes its records under ``data/p/...`` only. ``refuse_out`` refuses m's (``data/m``),
mf3's (``data/mf3``) and the OLMo data root (``data/olmo``) and ``/workspace/models`` for any p output;
``refuse_test_out`` also refuses the whole repository for a test or stub output (p's own roots included), so a
never-of-record file cannot land in any directory git admits.

THE WRITER (``write_once_bytes``). Write-once: identical bytes are accepted as they are, anything else is refused and
left untouched; atomic (temp file, fsync, rename, directory fsync); never through a link -- the path and its temp
name must not be links (or, for the temp name, a non-file), and the temp file is opened with ``O_NOFOLLOW``.

TERM (e), STATICALLY (``substitution_problems``). In every p production module and in p's drivers, outside the
bodies of the self-test functions: no assignment, augmented assignment or deletion whose target reaches an object
imported from ``valence_core.m`` (bound by ``from ... import``, relative or absolute, by ``import ... as``, by a dotted
``import``, or by an alias assignment in any scope; through a tuple target, a ``vars(...)`` subscript or a
``.__dict__`` subscript); no call named ``setattr``/``delattr``/``__setattr__``/``__delattr__`` with anything but
``self`` first, outside ``register.py``; no ``vars()`` call on an m name and no ``.__dict__`` read of an m name; no
assignment into ``sys.modules``; no
``unittest.mock``; no import of a test double (``testing``), in any statement form or through ``importlib`` /
``__import__``; no ``classify`` call (the scoring stack is called only by m's runner, which p runs unchanged). A
static check of these forms, not a proof against every rewrite; the runtime import set and the register's own
restoration checks stand beside it. Forms it does not follow (an m object passed as a function argument, the result
of ``importlib.import_module`` or ``__import__`` bound to a name, a write through a ``sys.modules[...]`` lookup or
through a container, an alias made by an annotation, a walrus or a ``for`` target, ``getattr(x, '__dict__')``, a
``setattr`` bound to another name, a bare-name ``classify``) are outside its reach.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

from ..m import guard as m_guard
from ..m import resume as m_resume

REPO = Path(__file__).resolve().parents[2]
PACKAGE_DIR = Path(__file__).resolve().parent
M_PACKAGE_DIR = REPO / "valence_core" / "m"
OLMO_HF_REL = "valence_core/adapters/olmo_hf.py"
DRIVER_REL = "scripts/p_sessions.py"
DRIVER_RELS = ("scripts/p_sessions.py", "scripts/p_analyze.py")
TEST_DOUBLES = ("testing",)
DATA_DIR = REPO / "data"
P_ROOT = DATA_DIR / "p"
REFUSED_ROOTS = (DATA_DIR / "m", DATA_DIR / "mf3", DATA_DIR / "olmo", Path("/workspace/models"))
FORBIDDEN_MODULES = m_guard.FORBIDDEN_MODULES
EXEMPT_FUNCS = ("_selftest", "run_selftest")
#: The valence_core.m modules a fresh interpreter holds after importing every p production module (measured at
#: the p BUILD and asserted by the self-test; a change is a licence change).
M_IMPORTED = ("audit", "bars", "banner", "corr", "gcal", "gshape", "guard", "keys", "readrule", "resume",
              "runner_olmo", "runner_qwen", "scaffold", "schedule", "stages", "verify")
M_HASHED = M_IMPORTED + ("__init__",)


class GuardStop(SystemExit):
    pass


def package_sha256() -> str:
    return m_resume.package_sha256_of(PACKAGE_DIR)


def _sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def m_module_sha256s() -> dict[str, str]:
    return {m: _sha256_file(M_PACKAGE_DIR / f"{m}.py") for m in M_HASHED}


def olmo_hf_sha256() -> str:
    return _sha256_file(REPO / OLMO_HF_REL)


def driver_sha256() -> str | None:
    p = REPO / DRIVER_REL
    return _sha256_file(p) if p.is_file() else None


def licence_lines() -> list[str]:
    out = [f"LICENCE valence_core/p package_sha256 {package_sha256()} "
           f"({len(list(PACKAGE_DIR.glob('*.py')))} files, valence_core/p/*.py)"]
    out += [f"LICENCE valence_core/m/{m}.py sha256 {v}" for m, v in m_module_sha256s().items()]
    out.append(f"LICENCE {OLMO_HF_REL} sha256 {olmo_hf_sha256()}")
    return out


def production_files() -> list[Path]:
    return sorted(p for p in PACKAGE_DIR.glob("*.py") if p.stem not in TEST_DOUBLES)


def scanned_files() -> list[Path]:
    """The files term (e)'s static check reads: p's production modules and p's drivers (those that exist)."""
    return production_files() + [REPO / r for r in DRIVER_RELS if (REPO / r).is_file()]


def _under(p: Path, root: Path) -> bool:
    """True iff ``p`` is ``root`` or lies under it, compared case-insensitively (the laptop's volume is
    case-insensitive: ``Data/m`` is ``data/m`` there), so the check only ever refuses more."""
    r = root.resolve() if root.exists() else root
    pc, rc = str(p).casefold().rstrip("/"), str(r).casefold().rstrip("/")
    return pc == rc or pc.startswith(rc + "/")


def refuse_out(path) -> Path:
    """The resolved path, or GuardStop when it lies under m's, mf3's or the OLMo data root or the weights' root."""
    p = Path(path).expanduser().resolve()
    for r in REFUSED_ROOTS:
        if _under(p, r):
            raise GuardStop(f"GUARD STOP: {p} lies under {r}; p writes under data/p/... only (ans2 Q4 (ii))")
    return p


def refuse_test_out(path) -> Path:
    """``refuse_out`` and, for a test or stub output, nothing inside the repository (p's roots included)."""
    if path is None or str(path).strip() == "":
        raise GuardStop("GUARD STOP: a test or stub output needs a scratch directory (an empty path resolves to the "
                        "working directory)")
    p = refuse_out(path)
    if _under(p, REPO):
        raise GuardStop(f"GUARD STOP: {p} lies inside the repository; a test or stub output goes to a scratch "
                        f"directory, never where a record could be committed (ledger 27)")
    return p


def no_link_problems(path: Path, upto: Path) -> list[str]:
    """Problems if ``path`` or any directory between it and ``upto`` (inclusive) is a symlink."""
    out, p = [], Path(os.path.abspath(path))
    stop = Path(os.path.abspath(upto))
    while True:
        if p.is_symlink():
            out.append(f"{p} is a symlink")
        if p == stop or p.parent == p:
            break
        p = p.parent
    return out


def write_once_bytes(path: Path, data: bytes, *, what: str = "file") -> str:
    """'written' or 'identical'; GuardStop if a different file, a non-file or a link is there."""
    p = Path(path)
    tmp = p.with_name(p.name + ".tmp")
    if p.is_symlink() or tmp.is_symlink() or (tmp.exists() and not tmp.is_file()):
        raise GuardStop(f"GUARD STOP: {p} or its temp name is a link or a non-file; a {what} is never written "
                        f"through a link")
    if p.exists():
        try:
            same = p.is_file() and p.read_bytes() == data
        except OSError:
            same = False
        if not same:
            raise GuardStop(f"GUARD STOP: {what} EXISTS at {p} with different bytes; it is never overwritten")
        return "identical"
    p.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o666)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, p)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    m_resume._fsync_dir(p.parent)
    return "written"


def atomic_write_nofollow(path: Path, data: bytes, *, what: str = "checkpoint") -> None:
    """A checkpoint's rewrite: atomic (temp file opened ``O_NOFOLLOW``, fsync, rename, directory fsync), refused when
    the path or its temp name is a link (or the temp name a non-file); an existing regular file is replaced."""
    p = Path(path)
    tmp = p.with_name(p.name + ".tmp")
    if p.is_symlink() or tmp.is_symlink() or (tmp.exists() and not tmp.is_file()) or (p.exists() and not p.is_file()):
        raise GuardStop(f"GUARD STOP: {p} or its temp name is a link or a non-file; a {what} is never written "
                        f"through a link")
    p.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o666)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, p)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    m_resume._fsync_dir(p.parent)


def runtime_import_set(python: str | None = None) -> tuple[list[str], set[str]]:
    mods = [f"valence_core.p.{p.stem}" for p in production_files() if p.stem != "__init__"]
    code = ("import json, sys; sys.path.insert(0, %r)\n" % str(REPO) + "".join(f"import {m}\n" for m in mods)
            + "print(json.dumps(sorted(k.split('.')[2] for k in sys.modules if k.startswith('valence_core.m.'))))")
    r = subprocess.run([python or sys.executable, "-I", "-B", "-c", code], capture_output=True, text=True,
                       cwd=str(REPO))
    if r.returncode != 0:
        return [f"fresh-interpreter import failed: {(r.stderr or '').strip().splitlines()[-1:]}"], set()
    return [], set(json.loads(r.stdout.strip().splitlines()[-1]))


# --- term (e)'s static check -------------------------------------------------------------------------------
def _is_m_from(node: ast.ImportFrom, pkg: str) -> bool:
    """True iff ``from X import ...`` imports from valence_core.m (or a module under it), relative or absolute."""
    mod = node.module or ""
    if node.level == 0:
        return mod == "valence_core.m" or mod.startswith("valence_core.m.")
    parts = pkg.split(".")
    if node.level > len(parts):
        return False
    full = ".".join(parts[:len(parts) - node.level] + ([mod] if mod else []))
    return full == "valence_core.m" or full.startswith("valence_core.m.")


def _root(e: ast.AST) -> str | None:
    while isinstance(e, (ast.Attribute, ast.Subscript)):
        e = e.value
    return e.id if isinstance(e, ast.Name) else None


def _target_names(t: ast.AST) -> list[str]:
    if isinstance(t, ast.Name):
        return [t.id]
    if isinstance(t, (ast.Tuple, ast.List)):
        return [x for e in t.elts for x in _target_names(e)]
    if isinstance(t, ast.Starred):
        return _target_names(t.value)
    return []


def _flat_targets(t: ast.AST) -> list[ast.AST]:
    if isinstance(t, (ast.Tuple, ast.List)):
        return [x for e in t.elts for x in _flat_targets(e)]
    if isinstance(t, ast.Starred):
        return _flat_targets(t.value)
    return [t]


def _m_names(tree: ast.AST, pkg: str) -> set[str]:
    """Every local name bound to an object of valence_core.m (or to the dotted root of an ``import valence_core.m``)."""
    names: set[str] = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.ImportFrom):
            if _is_m_from(n, pkg):
                names.update(a.asname or a.name for a in n.names)
            elif (n.level == 0 and n.module == "valence_core") or (n.level and not n.module):
                names.update(a.asname or a.name for a in n.names if a.name == "m")
        elif isinstance(n, ast.Import):
            for a in n.names:
                if a.name == "valence_core.m" or a.name.startswith("valence_core.m."):
                    names.add(a.asname or a.name.split(".")[0])
    changed = True
    while changed:                                  # local aliases: c = corr; c2 = c
        changed = False
        for n in ast.walk(tree):
            if isinstance(n, ast.Assign) and _root(n.value) in names:
                for t in n.targets:
                    for nm in _target_names(t):
                        if nm not in names:
                            names.add(nm)
                            changed = True
    return names


def _reaches_m(t: ast.AST, names: set[str]) -> bool:
    """A target writing into an m object: an attribute chain or subscript rooted at an m name, or a subscript of
    vars(...), of an object's __dict__ or of sys.modules."""
    if isinstance(t, ast.Subscript):
        v = t.value
        if isinstance(v, ast.Call) and isinstance(v.func, ast.Name) and v.func.id == "vars":
            return True
        if isinstance(v, ast.Attribute) and v.attr in ("__dict__", "modules"):
            return True
    if isinstance(t, (ast.Attribute, ast.Subscript)):
        return _root(t) in names
    return False


def _exempt_ranges(tree: ast.AST) -> list[tuple[int, int]]:
    return [(n.lineno, n.end_lineno or n.lineno) for n in ast.walk(tree)
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name in EXEMPT_FUNCS]


def substitution_problems(files=None) -> list[str]:
    probs: list[str] = []
    for f in (scanned_files() if files is None else [Path(x) for x in files]):
        f = Path(f)
        tree = ast.parse(f.read_text(encoding="utf-8"))
        pkg = "valence_core.p.x"                  # p's modules; the drivers import absolutely
        names = _m_names(tree, pkg)
        ex = _exempt_ranges(tree)
        is_register = f.name == "register.py" and f.parent.resolve() == PACKAGE_DIR

        def exempt(n) -> bool:
            ln = getattr(n, "lineno", None)
            return ln is not None and any(a <= ln <= b for a, b in ex)

        for n in ast.walk(tree):
            if exempt(n):
                continue
            where = f"{f.name}:{getattr(n, 'lineno', '?')}"
            tgts: list = []
            if isinstance(n, ast.Assign):
                tgts = n.targets
            elif isinstance(n, (ast.AugAssign, ast.AnnAssign)):
                tgts = [n.target]
            elif isinstance(n, ast.Delete):
                tgts = n.targets
            for t in (x for tt in tgts for x in _flat_targets(tt)):
                if _reaches_m(t, names):
                    probs.append(f"{where}: writes into an m object outside register.substituted")
            if isinstance(n, ast.Call):
                fn = n.func
                fname = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else None)
                if fname in ("setattr", "delattr", "__setattr__", "__delattr__") and not is_register:
                    first = n.args[0] if n.args else None
                    if not (isinstance(first, ast.Name) and first.id == "self"):
                        probs.append(f"{where}: {fname} on something other than self, outside register.substituted")
                if fname == "vars" and n.args and _root(n.args[0]) in names:
                    probs.append(f"{where}: vars() of an m object")
                if fname in ("import_module", "__import__") and any(
                        isinstance(a, ast.Constant) and isinstance(a.value, str)
                        and a.value.split(".")[-1] in TEST_DOUBLES for a in n.args):
                    probs.append(f"{where}: imports a test double dynamically")
                if fname == "classify" and isinstance(fn, ast.Attribute):
                    probs.append(f"{where}: calls classify (m's runner alone scores)")
            if isinstance(n, ast.Attribute) and n.attr == "__dict__" and _root(n.value) in names:
                probs.append(f"{where}: __dict__ of an m object")
            if isinstance(n, (ast.Import, ast.ImportFrom)):
                mods = [a.name for a in n.names] + ([n.module] if isinstance(n, ast.ImportFrom) and n.module else [])
                if any(x.split(".")[-1] in TEST_DOUBLES for x in mods):
                    probs.append(f"{where}: imports a test double outside a self-test")
                if any(x == "unittest.mock" or x.split(".")[0] == "mock" for x in mods) or (
                        isinstance(n, ast.ImportFrom) and n.module == "unittest"
                        and any(a.name == "mock" for a in n.names)):
                    probs.append(f"{where}: imports unittest.mock outside a self-test")
    return sorted(set(probs))


def import_problems(*, runtime: bool = True) -> list[str]:
    probs = substitution_problems()
    if runtime:
        rp, got = runtime_import_set()
        probs += rp
        if not rp and got != set(M_IMPORTED):
            probs.append(f"import set: {sorted(got)} != M_IMPORTED {sorted(M_IMPORTED)} (a licence change)")
    return probs


#: The planted forms the self-test asserts the static check catches (the review's round-1 probe set, m3, and more).
PLANTED = {
    "baseline": "from ..m import corr\ncorr._eligible_m = None\n",
    "import-as": "import valence_core.m.corr as c\nc._eligible_m = None\n",
    "dotted-import": "import valence_core.m.corr\nvalence_core.m.corr._eligible_m = None\n",
    "package-alias": "from .. import m\nm.corr._eligible_m = None\n",
    "tuple-target": "from ..m import corr\ncorr._eligible_m, y = None, 1\n",
    "vars": "from ..m import corr\nvars(corr)['_eligible_m'] = None\n",
    "dunder-dict": "from ..m import corr\ncorr.__dict__['_eligible_m'] = None\n",
    "mock": "from unittest import mock\n",
    "builtins-setattr": "import builtins\nfrom ..m import corr\nbuiltins.setattr(corr, '_eligible_m', None)\n",
    "object-setattr": "from ..m import corr\nobject.__setattr__(corr, '_eligible_m', None)\n",
    "local-alias": "from ..m import corr\nc = corr\nc._eligible_m = None\n",
    "del": "from ..m import corr\ndel corr._eligible_m\n",
    "try-import": "try:\n    from ..m import testing\nexcept ImportError:\n    pass\n",
    "importlib": "import importlib\nt = importlib.import_module('valence_core.m.testing')\n",
    "sys-modules": "import sys\nsys.modules['valence_core.m.corr'] = None\n",
    "classify": "def g(a):\n    return a.classify('t')\n",
}


def _selftest(chk) -> None:
    import tempfile
    ip = import_problems(runtime=True)
    chk("guard: p's production modules and driver pass term (e)'s static check, and import exactly M_IMPORTED of "
        "valence_core.m (a fresh interpreter)", ip == [], ip[:3])
    caught, missed = [], []
    with tempfile.TemporaryDirectory() as td:
        for name, src in PLANTED.items():
            f = Path(td) / f"{name.replace('-', '_')}.py"
            f.write_text(src)
            (caught if substitution_problems([f]) else missed).append(name)
        ok = Path(td) / "ok.py"
        ok.write_text("from ..m import corr\nx = corr._k_m(6)\nclass P:\n    def __init__(self, a):\n"
                      "        object.__setattr__(self, '_a', a)\ndef _selftest(chk):\n    from . import testing\n"
                      "    corr._eligible_m = None\n")
        clean = substitution_problems([ok])
    chk("guard: term (e)'s static check catches every planted form (the review's eleven and more), and passes a read "
        "of m, a setattr on self and a self-test body", missed == [] and clean == [], (missed, clean))
    outs = []
    for p in (REPO / "data" / "m" / "gates" / "x.json", REPO / "data" / "mf3" / "x.json",
              REPO / "data" / "olmo" / "x.json", Path("/workspace/models/sft")):
        try:
            refuse_out(p)
            outs.append("ok")
        except GuardStop:
            outs.append("stop")
    touts = []
    for p in (REPO / "data" / "p" / "schedules", REPO / "data" / "p" / "verdicts", REPO / "data", "",
              REPO / "results" / "raw", REPO, REPO / "Data" / "m"):
        try:
            refuse_test_out(p)
            touts.append("ok")
        except GuardStop:
            touts.append("stop")
    with tempfile.TemporaryDirectory() as td:
        scratch_ok = refuse_test_out(td) == Path(td).resolve()
    chk("guard: p refuses m's, mf3's and the OLMo data root and the weights' root for any output, and anything inside "
        "the repository (data/, p's roots, results/raw, the root itself, a case variant) or an empty path for a test "
        "output; a scratch directory passes", outs == ["stop"] * 4 and touts == ["stop"] * 7 and scratch_ok,
        (outs, touts))
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        w1 = write_once_bytes(d / "a.json", b"x")
        w2 = write_once_bytes(d / "a.json", b"x")
        res = []
        for case in ("differ", "link", "tmp-link"):
            try:
                if case == "differ":
                    write_once_bytes(d / "a.json", b"y")
                elif case == "link":
                    (d / "l.json").symlink_to(d / "victim.json")
                    write_once_bytes(d / "l.json", b"x")
                else:
                    (d / "t.json.tmp").symlink_to(d / "victim2.json")
                    write_once_bytes(d / "t.json", b"x")
                res.append("ran")
            except GuardStop:
                res.append("refused")
        (d / "real").mkdir()
        (d / "pl").symlink_to(d / "real")
        linked_parent = bool(no_link_problems(d / "pl" / "f.json", d)) and not no_link_problems(d / "real" / "f", d)
        victims = [(d / v).exists() for v in ("victim.json", "victim2.json")]
    chk("guard: the writer writes once, accepts identical bytes, and refuses different bytes, a link at the path and a "
        "link at the temp name, writing nothing through either; a linked parent directory is a problem",
        w1 == "written" and w2 == "identical" and res == ["refused"] * 3 and linked_parent
        and victims == [False, False], (res, victims))
    lines = licence_lines()
    chk("guard: the licence lines name p's package hash, the seventeen m files (sixteen modules and __init__.py) and "
        "olmo_hf.py, each by name", len(lines) == 1 + len(M_HASHED) + 1 and len(M_HASHED) == 17
        and lines[-1].startswith(f"LICENCE {OLMO_HF_REL} sha256 "), len(lines))
    chk("guard: the quarantined state-present module is not loaded", not any(m in sys.modules for m in FORBIDDEN_MODULES))
