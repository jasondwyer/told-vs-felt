"""PROPOSAL-n's guard: the package hash, the import closure's file sha256s, the roots n writes, and the test-double
rule (n v0.2 §8 step 6: "its own package hash bound in LOCK-n, closure-style on the m modules it imports").

THE PACKAGE HASH is m's form, imported unchanged: ``valence_core.m.resume.package_sha256_of`` over every ``*.py``
directly in ``valence_core/n/``.

THE CLOSURE is every ``valence_core`` module outside ``valence_core.n`` that a fresh interpreter holds after the
driver imports every n production module (``PRODUCTION``), with each package's ``__init__.py`` on the way, each by
its repository path and file sha256. It is measured by the driver in a child process (``scripts/n_sessions.py
hashes``), because the 5(f) primitive's import guard admits only n's own modules and n's drivers.

THE ROOTS. n writes its records under ``data/n/`` only; ``refuse_out`` refuses every other data root and the box's
model volume for any n output, and ``refuse_test_out`` refuses the whole repository for a test output.

THE TEST DOUBLES (``testing``, ``hftiny``) are imported by no production module at module level (checked on the
modules' syntax trees).
"""
from __future__ import annotations

import ast
import hashlib
from pathlib import Path

from ..m import resume as m_resume

REPO = Path(__file__).resolve().parents[2]
PACKAGE_DIR = Path(__file__).resolve().parent
DATA_DIR = REPO / "data"
N_ROOT = DATA_DIR / "n"
REFUSED_ROOTS = (DATA_DIR / "m", DATA_DIR / "mf3", DATA_DIR / "p", DATA_DIR / "olmo", Path("/workspace/models"))
PRODUCTION = ("schema", "sessions", "ids", "keys", "cells", "directions", "primitive", "runner", "verify", "probe",
              "guard")
SELFTEST_ONLY = ("testing", "hftiny")


class GuardStop(SystemExit):
    pass


def package_sha256() -> str:
    return m_resume.package_sha256_of(PACKAGE_DIR)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def closure_from_modules(modules: dict) -> dict[str, str]:
    """{repo-relative path: sha256} for the given ``sys.modules`` snapshot's valence_core modules outside n."""
    out = {}
    for name, mod in sorted(modules.items()):
        if not (name == "valence_core" or name.startswith("valence_core.")) or name.startswith("valence_core.n"):
            continue
        f = getattr(mod, "__file__", None)
        if not f:
            continue
        p = Path(f).resolve()
        try:
            rel = p.relative_to(REPO).as_posix()
        except ValueError:
            raise GuardStop(f"{name} is imported from outside the repository")
        out[rel] = sha256_file(p)
    return out


def _within(p: Path, root: Path) -> bool:
    try:
        p.relative_to(root)
        return True
    except ValueError:
        return False


def refuse_out(path) -> Path:
    p = Path(path).resolve()
    for r in REFUSED_ROOTS:
        if _within(p, r.resolve() if r.exists() else r):
            raise GuardStop(f"n writes nothing under {r}")
    if _within(p, REPO) and not _within(p, N_ROOT):
        raise GuardStop(f"n writes its records under data/n/ only, not {p}")
    return p


def refuse_test_out(path) -> Path:
    p = Path(path).resolve()
    if _within(p, REPO):
        raise GuardStop("a test output is never written inside the repository")
    return refuse_out(p)


def testing_import_problems() -> list[str]:
    """Module-level imports of a test double by a production module."""
    probs = []
    for m in PRODUCTION:
        tree = ast.parse((PACKAGE_DIR / f"{m}.py").read_text(encoding="utf-8"))
        for node in tree.body:
            names = []
            if isinstance(node, ast.ImportFrom):
                names = [node.module or ""] + [a.name for a in node.names]
            elif isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            for nm in names:
                if any(nm == d or nm.endswith("." + d) for d in SELFTEST_ONLY):
                    probs.append(f"{m}.py imports {nm} at module level")
    return probs


def _selftest(chk, tmp) -> None:
    import sys
    chk("guard: the package hash is m's form and deterministic", package_sha256() == package_sha256(), "")
    for bad in (DATA_DIR / "m" / "x.json", DATA_DIR / "mf3" / "x.json", DATA_DIR / "p" / "x.json",
                DATA_DIR / "olmo" / "x.json", REPO / "RESULTS.md"):
        try:
            refuse_out(bad)
            chk(f"guard: n refuses to write {bad.relative_to(REPO)}", False, "accepted")
        except GuardStop:
            chk(f"guard: n refuses to write {bad.relative_to(REPO)}", True, "")
    chk("guard: n writes under data/n", refuse_out(N_ROOT / "ckpt" / "x.json") == (N_ROOT / "ckpt" / "x.json").resolve(),
        "")
    try:
        refuse_test_out(N_ROOT / "x.json")
        chk("guard: a test output inside the repository is refused", False, "accepted")
    except GuardStop:
        chk("guard: a test output inside the repository is refused", True, "")
    chk("guard: a test output outside the repository is admitted", refuse_test_out(tmp) == Path(tmp).resolve(), "")
    clo = closure_from_modules(dict(sys.modules))
    want = ("valence_core/__init__.py", "valence_core/adapters/base.py", "valence_core/adapters/olmo_hf.py",
            "valence_core/m/resume.py", "valence_core/m/keys.py", "valence_core/echo/probe.py",
            "valence_core/discrim.py")
    chk("guard: the closure holds the modules n imports unchanged", all(w in clo for w in want),
        [w for w in want if w not in clo])
    chk("guard: the closure holds no valence_core.n module", not any(r.startswith("valence_core/n/") for r in clo), "")
