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
  (e) as amended by the seat's ruling of 2026-11-07 (``38f9974``, §4), the register's text at LOCK-p v0.1: a site not
      in the register is a STOP, never an unpinned copy; a restated fragment is admitted only where m's code is an
      inline fragment of a function that cannot run for p, and only with an AST-level equality assertion to m's
      fragment in p's self-test and a dynamic check that every call carries m's procedure, so that a later m edit
      breaks p's self-test before it changes p's behaviour. ``substituted`` refuses any (module, attributes) pair that
      is not an entry built at this step; a pinned restatement (entry (5)) is never substituted.

PIN (Code, declared at the p BUILD): "single-threaded" is asserted as: the calling thread is the main thread and
no other Python thread is alive (``threading.active_count() == 1``); every site runs before any model load, so a
library's background thread cannot be present at a site of record.

AT STEP 6 (the design seat's answer of 2026-11-08, ``de729c4``): entry (3) is built at its two sites (the Clock and
the v2 resolution; the roots are parameters, no site, Q9 (b)); entries (6)-(8) are built as declared (Q1-Q3); entry
(9) is built on ``resume.Identity``, the site the seat's answer to Code's entry (9) block declares (§2, ``6b63973``,
routed by the PI on 2026-11-09) -- the site first declared, ``stages._identity``, cannot run -- and is entered and
restored with entry (8) (``PAIRED_AFTER``). At a gate stage the substitutions are entered before the load and held to
the stage's end (the seat's Q4): the assertion runs at each entry, and term (d)'s state at the stage's end, before
restoration, is recorded (``single_thread_state``), never raised.
"""
from __future__ import annotations

import contextlib
import threading
from dataclasses import dataclass
from types import ModuleType
from typing import Any, Iterator, Mapping

KINDS = ("eligibility", "keys", "pins", "clock", "roots")
#: Entry (5)'s kind: an admitted, pinned restatement of an inline m fragment -- not a substitution (term (e) amended).
RESTATEMENT = "pinned restatement"
ADMITTED = "admitted by the seat's ruling of 2026-11-07 (38f9974, §4); a restatement, never substituted"


class RegisterStop(SystemExit):
    """A substitution outside the register, or one whose restoration failed: a STOP, never an unpinned copy."""


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
BUILT_STEP6 = "built at p §8 step 6 (the seat's answer of 2026-11-08, de729c4)"
#: The register's entries as ans2 Q0 declares them (p §4.2), with the seat's ruling of 2026-11-07 (38f9974, §4):
#: entry (4), declared and never exercised, is struck; entry (5) is G-CAL-p's pinned restatement of m's generation
#: call. The seat's answer of 2026-11-08 (de729c4, results/raw/2026-11-08_p-step6_design-to-code_answers.md) makes
#: entry (3) concrete (Q9: the Clock and the v2 resolution are sites; the roots are parameters, no site) and declares
#: entries (6)-(9) for p's gate stages and campaign (Q1-Q3); its answer to Code's entry (9) block (6b63973, §2,
#: results/raw/2026-11-08_open50-entry9_design-to-code_answers.md) moves entry (9) to resume.Identity.
#: PIN (Code, declared at step 6): entry (3)'s module is ``m_analyze``, the name scripts/p_analyze.py imports
#: scripts/m_analyze.py under (scripts/ on sys.path; the import system registers it).
ENTRIES: tuple[Entry, ...] = (
    Entry(1, "valence_core.m.corr", ("_eligible_m",), "valence_core.p.corrupt.eligible_p", ("eligibility",),
          "p §1.4: corrupt_p is corr.corrupt_m with the frame-word eligible set (p §1.1)", BUILT,
          (("_eligible_m", "valence_core.p.corrupt.eligible_p"),)),
    Entry(2, "valence_core.m.keys", ("item_key", "arm_key", "sched_key", "gate_sched_key"),
          "valence_core.p.keys.{item_key, arm_key, sched_key, gate_sched_key}", ("keys",),
          "p §4.1: the six OLMo key families under p's prefix, for the schedule builder, the arm streams and the "
          "item streams, so that no p stream coincides with an m stream", BUILT,
          tuple((a, f"valence_core.p.keys.{a}") for a in ("item_key", "arm_key", "sched_key", "gate_sched_key"))),
    Entry(3, "m_analyze", ("clock_of_record", "crosscheck_coordinate"),
          "valence_core.p.analysis.{clock_of_record_p, crosscheck_coordinate_p}", ("clock", "roots"),
          "p §4.4: p's outputs through m's analyzer (scripts/m_analyze.py, imported by scripts/p_analyze.py), the "
          "proposal pin kept m's (proposal_p_sha256 beside it): (a) the Clock -- D_p for the OLMo units, m's own for "
          "Q-F0 and Q-F3; (c) the v2 posting's per-unit verdicts-dir resolution -- data/p/verdicts for the OLMo "
          "units, data/m/verdicts for Q-F0. (b) The roots are parameters wherever m takes them, not a site (the "
          "seat's Q9 (b))", BUILT_STEP6,
          (("clock_of_record", "valence_core.p.analysis.clock_of_record_p"),
           ("crosscheck_coordinate", "valence_core.p.analysis.crosscheck_coordinate_p"))),
    Entry(5, "valence_core.m.gcal",
          ("run_completability's segment and generation call (gcal.py:1155, :1164; the OLMo branch's temp, cap at "
           ":1104)",),
          "valence_core.p.gcal.run's restated segment (m's SEGMENT_FORM) and call, pinned by gcal._call_pin_problems "
          "(an AST comparison, also run in G-CAL-p's precheck) and the self-test's dynamic check of all 128 calls",
          (RESTATEMENT,),
          "p §3.1, P21: m's call is an inline fragment of run_completability, which cannot run for p (its precheck, "
          "roots and identity, and no hair trigger)", ADMITTED),
    Entry(6, "valence_core.m.stages", ("DEFAULT_OUT",), "valence_core.p.stage.DEFAULT_OUT_P (REPO/data/p)", ("roots",),
          "the seat's Q1: p's gate stages and campaign write under data/p; m's out-root guard reads DEFAULT_OUT at "
          "call time (stages.py:309) and so admits data/p and refuses data/m for p", BUILT_STEP6,
          (("DEFAULT_OUT", "valence_core.p.stage.DEFAULT_OUT_P"),)),
    Entry(7, "valence_core.m.schedule", ("verify_schedule_dir",), "valence_core.p.schedule.verify_schedule_dir",
          ("roots",),
          "the seat's Q2: m's load_committed runs m's verifier, which regenerates all four units' files and m's "
          "manifest and so refuses data/p/schedules; p's is m's check over p's eighteen files and p's manifest, "
          "regenerated by p's builder under entry (2)", BUILT_STEP6,
          (("verify_schedule_dir", "valence_core.p.schedule.verify_schedule_dir"),)),
    Entry(8, "valence_core.m.resume", ("IDENTITY_KEYS_OLMO",),
          "valence_core.p.identity.IDENTITY_KEYS_OLMO_P (m's key set + proposal, proposal_p_sha256, p_package_sha256, "
          "renders_sha256_p)", ("pins",),
          "the seat's Q3 (a): p's four identity fields in every p gate-stage and campaign checkpoint's identity, as "
          "F-p8 ruled for checkpoints and p:84 asks", BUILT_STEP6,
          (("IDENTITY_KEYS_OLMO", "valence_core.p.identity.IDENTITY_KEYS_OLMO_P"),)),
    Entry(9, "valence_core.m.resume", ("Identity",), "valence_core.p.identity.identity_p (m's builder, wrapped)",
          ("pins",),
          "the seat's Q3 (a): p's four fields added to m's identity by m's own builder, wrapped -- the stage's build "
          "(stages._identity, stages.py:1106) and m's rebuild in _validated (resume.py:507) both resolve "
          "resume.Identity at call time. Declared at de729c4 on stages._identity, which cannot run (Code's block of "
          "2026-11-08, 9624f70); on resume.Identity by the seat's answer to that block (6b63973, §2), entered and "
          "restored with entry (8)", BUILT_STEP6,
          (("Identity", "valence_core.p.identity.identity_p"),)),
)
BY_N = {e.n: e for e in ENTRIES}
#: The statuses ``substituted`` admits.
SUBSTITUTABLE = (BUILT, BUILT_STEP6)
#: PIN (Code, declared at step 6): an entry entered only while another is in force on the same module -- (9) with
#: (8), as the seat's answer on entry (9) has them entered and restored together. ``active`` is the register's own
#: count of the entries in force, per entry and module object (by ``substituted`` alone; a hand-set attribute is not
#: an entry in force, and an entry on a stand-in module is not one on m's).
PAIRED_AFTER = {9: 8}
_ACTIVE: dict[tuple[int, int], int] = {}


def active(n: int, module: ModuleType | None = None) -> bool:
    """True while register entry ``n`` is in force through ``substituted`` -- on ``module`` (that very object) when
    one is given, on any module otherwise."""
    if module is not None:
        return _ACTIVE.get((n, id(module)), 0) > 0
    return any(c > 0 for (k, _), c in _ACTIVE.items() if k == n)


def assert_single_threaded(site: str) -> None:
    """Term (d): the site runs on the main thread with no other Python thread alive."""
    if threading.current_thread() is not threading.main_thread() or threading.active_count() != 1:
        raise RegisterStop(f"REGISTER STOP: {site} runs only in single-threaded stage code (term (d)); "
                           f"{threading.active_count()} threads alive, current {threading.current_thread().name!r}")


def single_thread_state() -> dict:
    """Term (d) at a stage's end, before restoration (the seat's answer of 2026-11-08, Q4): the same test as
    ``assert_single_threaded``, RECORDED, never raised -- a library thread alive after the load (the loader's progress
    bar) does not run m's code; a failure is recorded in the stage's entry."""
    names = sorted(t.name for t in threading.enumerate())
    main = threading.current_thread() is threading.main_thread()
    return {"single_threaded": main and threading.active_count() == 1, "on_main_thread": main,
            "active_count": threading.active_count(), "threads": names}


@contextlib.contextmanager
def substituted(n: int, module: ModuleType, values: Mapping[str, Any]) -> Iterator[None]:
    """Register entry ``n``: ``module``'s named attributes replaced by ``values`` for the duration of the block and
    restored in a ``finally``; anything not an entry built at this step is a STOP (term (e))."""
    e = BY_N.get(n)
    if e is None or e.status not in SUBSTITUTABLE or RESTATEMENT in e.kinds:
        raise RegisterStop(f"REGISTER STOP: entry ({n}) is not a substitution site built at this step (term (e))"
                           + (f": {e.status}" if e is not None else ""))
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
    if n in PAIRED_AFTER and not active(PAIRED_AFTER[n], module):
        raise RegisterStop(f"REGISTER STOP: entry ({n}) is entered only with entry ({PAIRED_AFTER[n]}) in force (the "
                           f"seat's answer of 2026-11-08 on entry (9), §2: (8) and (9) are entered and restored together)")
    assert_single_threaded(f"register entry ({n})")
    saved = {a: getattr(module, a) for a in e.attrs}
    key = (n, id(module))
    counted = False
    try:
        for a, v in values.items():
            setattr(module, a, v)
        _ACTIVE[key] = _ACTIVE.get(key, 0) + 1
        counted = True
        yield
    finally:
        if counted:                                 # the count falls before the restoration (round 3's NOTE 1)
            _ACTIVE[key] -= 1
            if not _ACTIVE[key]:
                del _ACTIVE[key]
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
    chk("register: eight entries -- (1)-(3) as ans2 Q0 declares them, (3) made concrete by the seat's Q9, (5) the "
        "pinned restatement admitted on 2026-11-07, (4) struck, (6)-(9) declared by the seat's answer of 2026-11-08, "
        "(9) on resume.Identity by its answer to Code's entry (9) block (6b63973); (1) and (2) built at the BUILD, (3) "
        "and (6)-(9) at step 6, (5) admitted",
        [e.n for e in ENTRIES] == [1, 2, 3, 5, 6, 7, 8, 9]
        and [e.status for e in ENTRIES] == [BUILT, BUILT, BUILT_STEP6, ADMITTED, BUILT_STEP6, BUILT_STEP6,
                                           BUILT_STEP6, BUILT_STEP6]
        and (BY_N[9].module, BY_N[9].attrs, BY_N[9].allowed) == ("valence_core.m.resume", ("Identity",),
                                                                 (("Identity", "valence_core.p.identity.identity_p"),))
        and BY_N[5].kinds == (RESTATEMENT,)
        and [BY_N[n].kinds for n in (3, 6, 7, 8, 9)] == [("clock", "roots"), ("roots",), ("roots",), ("pins",),
                                                         ("pins",)])
    chk("register: every substitution entry's kinds are among eligibility, keys, pins, Clock and roots (term (b)), "
        "entry (5)'s the pinned restatement; each built entry admits exactly one replacement per attribute",
        all(e.kinds and all(k in KINDS for k in e.kinds) for e in ENTRIES if e.n != 5)
        and all(sorted(dict(e.allowed)) == sorted(e.attrs) for e in ENTRIES if e.status in SUBSTITUTABLE),
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
    from . import analysis, identity, schedule as p_schedule, stage
    for n, m, v in ((3, mod, {"clock_of_record": None, "crosscheck_coordinate": None}), (5, mod, {"x": None}),
                    (4, mod, {}), (1, mod, {"_k_m": None}),
                    (1, types.ModuleType("valence_core.m.keys"), {"_eligible_m": None}),
                    (1, mod, {"_eligible_m": (lambda t: [1])}), (1, mod, {"_eligible_m": _named_like_eligible_p()})):
        try:
            with substituted(n, m, v):
                outs.append("ran")
        except RegisterStop as e:
            outs.append("stop" if "REGISTER STOP" in str(e) else "other")
    chk("register: entry (3) on a module other than m_analyze, entry (5) (a restatement, never substituted), struck "
        "entry (4), an undeclared attribute, a wrong module, a replacement other than the declared one and a stand-in "
        "carrying its qualified name are each a STOP (terms (a), (e))",
        outs == ["stop"] * 7 and mod._eligible_m is orig, outs)
    ma = types.ModuleType("m_analyze")
    ma.clock_of_record, ma.crosscheck_coordinate = c_orig, x_orig = (lambda u: "m"), (lambda *a, **k: None)
    seen3 = []
    with substituted(3, ma, {"clock_of_record": analysis.clock_of_record_p,
                             "crosscheck_coordinate": analysis.crosscheck_coordinate_p}):
        seen3.append(ma.clock_of_record is analysis.clock_of_record_p
                     and ma.crosscheck_coordinate is analysis.crosscheck_coordinate_p)
    sm, sc, rm = (types.ModuleType("valence_core.m.stages"), types.ModuleType("valence_core.m.schedule"),
                  types.ModuleType("valence_core.m.resume"))
    sm.DEFAULT_OUT, sc.verify_schedule_dir, rm.IDENTITY_KEYS_OLMO = d0, v0, k0 = object(), (lambda d=None: []), ("a",)
    seen68 = []
    with substituted(6, sm, {"DEFAULT_OUT": stage.DEFAULT_OUT_P}), \
            substituted(7, sc, {"verify_schedule_dir": p_schedule.verify_schedule_dir}), \
            substituted(8, rm, {"IDENTITY_KEYS_OLMO": identity.IDENTITY_KEYS_OLMO_P}):
        seen68.append(sm.DEFAULT_OUT is stage.DEFAULT_OUT_P and sc.verify_schedule_dir is p_schedule.verify_schedule_dir
                      and rm.IDENTITY_KEYS_OLMO is identity.IDENTITY_KEYS_OLMO_P)
    chk("register: entries (3), (6), (7) and (8) substitute their declared replacements on their declared modules for "
        "the block and restore every attribute after it",
        seen3 == [True] and seen68 == [True] and ma.clock_of_record is c_orig and ma.crosscheck_coordinate is x_orig
        and sm.DEFAULT_OUT is d0 and sc.verify_schedule_dir is v0 and rm.IDENTITY_KEYS_OLMO is k0)
    rm2 = types.ModuleType("valence_core.m.resume")
    rm2.IDENTITY_KEYS_OLMO, rm2.Identity = k2, b2 = ("a",), (lambda **kw: kw)
    try:
        with substituted(9, rm2, {"Identity": identity.identity_p}):
            alone = "ran"
    except RegisterStop as e:
        alone = "stop" if "entered only with entry (8)" in str(e) else f"other: {e}"
    with substituted(8, rm2, {"IDENTITY_KEYS_OLMO": identity.IDENTITY_KEYS_OLMO_P}):
        in8 = active(8)
        with substituted(9, rm2, {"Identity": identity.identity_p}):
            both = (active(8), active(9), rm2.Identity is identity.identity_p
                    and rm2.IDENTITY_KEYS_OLMO is identity.IDENTITY_KEYS_OLMO_P)
    after = (active(8), active(9), rm2.Identity is b2 and rm2.IDENTITY_KEYS_OLMO is k2)
    rm3 = types.ModuleType("valence_core.m.resume")
    rm3.IDENTITY_KEYS_OLMO, rm3.Identity = ("a",), (lambda **kw: kw)
    with substituted(8, rm3, {"IDENTITY_KEYS_OLMO": identity.IDENTITY_KEYS_OLMO_P}):
        try:
            with substituted(9, rm2, {"Identity": identity.identity_p}):
                cross = "ran"
        except RegisterStop:
            cross = "stop"
        on_other = (active(8), active(8, rm3), active(8, rm2))
    chk("register: entry (9) -- on resume.Identity, as the seat's answer to Code's entry (9) block declares it "
        "(6b63973, §2) -- is refused unless entry (8) is in force on the same module, and enters with it, its declared "
        "replacement in force for the block and m's attributes restored after; the register's count of the entries in "
        "force, per entry and module, rises and falls with each block (N-2, N-7; round 3's NOTE 1)",
        alone == "stop" and in8 is True and both == (True, True, True) and after == (False, False, True)
        and cross == "stop" and on_other == (True, True, False) and not _ACTIVE,
        (alone, both, after, cross, on_other, dict(_ACTIVE)))
    st = single_thread_state()
    chk("register: the stage-end state records term (d)'s test without raising (the seat's Q4)",
        st["single_threaded"] is True and st["on_main_thread"] is True and st["active_count"] == 1, st)
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
