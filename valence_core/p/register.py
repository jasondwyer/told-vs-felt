"""PROPOSAL-p's substitution register (p v0.2 §4.2; the design seat's answers of 2026-11-07, Q0).

THE FORM. Where m's code must run with a named attribute of an m module changed, p uses one declared form:
the attribute replaced for the duration of one call and restored in a ``finally`` (``substituted``). The seat's
five terms (ans2 Q0):

  (a) every site is named -- attribute, replacement, reason -- here (``ENTRIES``), in the BUILD entry and in
      LOCK-p v0.1, beside the imported files' sha256s;
  (b) only eligibility, keys, pins, Clock dates and data roots are ever substituted (``KINDS``) -- never a
      function that computes a bar, a DV, a verdict or an outcome order;
  (c) a self-test per site asserts equality with m where p must equal m, and restoration after the call, an
      exception included (each site's module carries its own; this module tests the form);
  (d) single-threaded stage code at every site, asserted at the site (``assert_single_threaded``);
  (e) a site not in the register is a STOP, never a copy: ``substituted`` refuses any (module, attributes) pair
      that is not an entry built at this step.

PIN (Code, declared at the p BUILD): "single-threaded" is asserted as: the calling thread is the main thread and
no other Python thread is alive (``threading.active_count() == 1``); every site runs before any model load, so a
library's background thread cannot be present at a site of record.
"""
from __future__ import annotations

import contextlib
import threading
from dataclasses import dataclass
from types import ModuleType
from typing import Any, Iterator, Mapping

KINDS = ("eligibility", "keys", "pins", "clock", "roots")


class RegisterStop(SystemExit):
    """A substitution outside the register, or one whose restoration failed: a STOP, never a copy."""


@dataclass(frozen=True)
class Entry:
    n: int
    module: str
    attrs: tuple[str, ...]
    replacement: str
    kinds: tuple[str, ...]
    reason: str
    status: str
    #: For a built entry, each attribute's one admitted replacement, by qualified name (term (a)'s "its
    #: replacement", enforced: ``substituted`` refuses any other value).
    allowed: tuple[tuple[str, str], ...] = ()

    def as_dict(self) -> dict:
        return {"n": self.n, "module": self.module, "attrs": list(self.attrs), "replacement": self.replacement,
                "kind": "; ".join(self.kinds), "reason": self.reason, "status": self.status}


BUILT = "built at the p BUILD (p §8 step 4)"
#: The register's entries as ans2 Q0 declares them (p §4.2). Entries (3) and (4) are declared; (3) is built with
#: scripts/p_analyze.py at p §8 step 6; (4) is not exercised -- G-CAL-p passes p's renders to m's functions as an
#: argument (``valence_core.m.gcal._task_of``), so no attribute of ``gcal`` is replaced.
ENTRIES: tuple[Entry, ...] = (
    Entry(1, "valence_core.m.corr", ("_eligible_m",), "valence_core.p.corrupt.eligible_p", ("eligibility",),
          "p §1.4: corrupt_p is corr.corrupt_m with the frame-word eligible set (p §1.1)", BUILT,
          (("_eligible_m", "valence_core.p.corrupt.eligible_p"),)),
    Entry(2, "valence_core.m.keys", ("item_key", "arm_key", "sched_key", "gate_sched_key"),
          "valence_core.p.keys.{item_key, arm_key, sched_key, gate_sched_key}", ("keys",),
          "p §4.1: the six OLMo key families under p's prefix, for the schedule builder, the arm streams and the "
          "item streams, so that no p stream coincides with an m stream", BUILT,
          tuple((a, f"valence_core.p.keys.{a}") for a in ("item_key", "arm_key", "sched_key", "gate_sched_key"))),
    Entry(3, "scripts/m_analyze.py (through scripts/p_analyze.py)",
          ("clock_of_record (OLMo units)", "the data/m/... root defaults (run_not_run's ckpt_dir included)",
           "the v2 posting's per-unit verdicts-dir resolution"),
          "D_p; data/p/...; data/p/verdicts for the OLMo coordinates", ("clock", "roots"),
          "p §4.4: p's outputs through m's analyzer, the proposal pin kept m's (proposal_p_sha256 beside it)",
          "declared; built with scripts/p_analyze.py at p §8 step 6"),
    Entry(4, "valence_core.m.gcal", ("the renders source",), "p's renders of record (valence_core.p.corrupt)",
          ("eligibility",), "p §3.1: the prompt, seeds, grader and generation call at p's renders",
          "declared; not exercised -- G-CAL-p does not call m's run_completability (p's own loop calls m's pieces, "
          "p's renders an argument of gcal._task_of), so no attribute of gcal is replaced"),
)
BY_N = {e.n: e for e in ENTRIES}


def assert_single_threaded(site: str) -> None:
    """Term (d): the site runs on the main thread with no other Python thread alive."""
    if threading.current_thread() is not threading.main_thread() or threading.active_count() != 1:
        raise RegisterStop(f"REGISTER STOP: {site} runs only in single-threaded stage code (term (d)); "
                           f"{threading.active_count()} threads alive, current {threading.current_thread().name!r}")


@contextlib.contextmanager
def substituted(n: int, module: ModuleType, values: Mapping[str, Any]) -> Iterator[None]:
    """Register entry ``n``: ``module``'s named attributes replaced by ``values`` for the duration of the block and
    restored in a ``finally``; anything not an entry built at this step is a STOP (term (e))."""
    e = BY_N.get(n)
    if e is None or e.status != BUILT:
        raise RegisterStop(f"REGISTER STOP: entry ({n}) is not a site built at this step (term (e))")
    if getattr(module, "__name__", None) != e.module or tuple(sorted(values)) != tuple(sorted(e.attrs)):
        raise RegisterStop(f"REGISTER STOP: ({getattr(module, '__name__', module)!r}, {sorted(values)}) is not "
                           f"entry ({n}) ({e.module}, {list(e.attrs)}) (term (e))")
    if not e.kinds or any(k not in KINDS for k in e.kinds):
        raise RegisterStop(f"REGISTER STOP: entry ({n})'s kinds {e.kinds!r} are not among {KINDS} (term (b))")
    allowed = dict(e.allowed)
    wrong = [a for a, v in values.items() if a not in allowed or v is not _resolve(allowed[a])]
    if wrong:
        raise RegisterStop(f"REGISTER STOP: entry ({n})'s replacement for {wrong} is not the declared one "
                           f"({[allowed.get(a) for a in wrong]}) (term (a))")
    assert_single_threaded(f"register entry ({n})")
    saved = {a: getattr(module, a) for a in e.attrs}
    try:
        for a, v in values.items():
            setattr(module, a, v)
        yield
    finally:
        for a, v in saved.items():
            setattr(module, a, v)
    bad = [a for a in e.attrs if getattr(module, a) is not saved[a]]
    if bad:                                     # unreachable while the finally holds; asserted anyway
        raise RegisterStop(f"REGISTER STOP: entry ({n}) left {bad} substituted after the call (term (c))")


_BOUND: dict[str, Any] = {}


def _resolve(qualified: str) -> Any:
    """The object a declared replacement names (``module.attr``), bound at its first use in the process and kept, so
    the check is identity with that object -- a later rebinding of the name does not pass."""
    import importlib
    if qualified not in _BOUND:
        mod, _, attr = qualified.rpartition(".")
        try:
            _BOUND[qualified] = getattr(importlib.import_module(mod), attr)
        except (ImportError, AttributeError):
            return object()                         # never identical to a value: the substitution is refused
    return _BOUND[qualified]


def table() -> list[dict]:
    """The register as the BUILD entry and LOCK-p v0.1 name it."""
    return [e.as_dict() for e in ENTRIES]


def _selftest(chk) -> None:
    import types
    from . import corrupt
    chk("register: four entries, numbered 1-4 as ans2 Q0 declares them; (1) and (2) built, (3) and (4) declared",
        [e.n for e in ENTRIES] == [1, 2, 3, 4] and [e.status == BUILT for e in ENTRIES] == [True, True, False, False])
    chk("register: every entry's kinds are among eligibility, keys, pins, Clock and roots (term (b)); each built "
        "entry admits exactly one replacement per attribute",
        all(e.kinds and all(k in KINDS for k in e.kinds) for e in ENTRIES)
        and all(sorted(dict(e.allowed)) == sorted(e.attrs) for e in ENTRIES if e.status == BUILT),
        [e.kinds for e in ENTRIES])
    mod = types.ModuleType("valence_core.m.corr")
    mod._eligible_m = orig = (lambda t: [0])
    seen = []
    with substituted(1, mod, {"_eligible_m": corrupt.eligible_p}):
        seen.append(mod._eligible_m is corrupt.eligible_p)
    chk("register: a built entry substitutes its declared replacement for the block and restores after it",
        seen == [True] and mod._eligible_m is orig)
    try:
        with substituted(1, mod, {"_eligible_m": corrupt.eligible_p}):
            raise ValueError("planted")
    except ValueError:
        pass
    chk("register: restoration holds after an exception inside the block (term (c))", mod._eligible_m is orig)
    outs = []
    for n, m, v in ((3, mod, {"clock_of_record": None}), (4, mod, {"x": None}), (9, mod, {}),
                    (1, mod, {"_k_m": None}), (1, types.ModuleType("valence_core.m.keys"), {"_eligible_m": None}),
                    (1, mod, {"_eligible_m": (lambda t: [1])}), (1, mod, {"_eligible_m": _named_like_eligible_p()})):
        try:
            with substituted(n, m, v):
                outs.append("ran")
        except RegisterStop as e:
            outs.append("stop" if "REGISTER STOP" in str(e) else "other")
    chk("register: entries (3) and (4), an unknown entry, an undeclared attribute, a wrong module, a replacement other "
        "than the declared one and a stand-in carrying its qualified name are each a STOP (terms (a), (e))",
        outs == ["stop"] * 7 and mod._eligible_m is orig, outs)
    box: list = []
    t = threading.Thread(target=lambda: box.append(_thread_site(mod)))
    t.start()
    t.join()
    chk("register: a site off the main thread is a STOP (term (d))", box == ["stop"], box)


def _named_like_eligible_p():
    """A stand-in wearing the declared replacement's qualified name (functools.wraps's effect)."""
    def f(text):
        return []
    f.__module__, f.__qualname__ = "valence_core.p.corrupt", "eligible_p"
    return f


def _thread_site(mod) -> str:
    try:
        from . import corrupt
        with substituted(1, mod, {"_eligible_m": corrupt.eligible_p}):
            return "ran"
    except RegisterStop:
        return "stop"
