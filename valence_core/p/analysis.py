"""PROPOSAL-p's analyzer path through m's (p v0.2 §4.4; register entry (3); the design seat's answer of 2026-11-08,
``de729c4``, §2, Q6-Q9).

scripts/p_analyze.py imports scripts/m_analyze.py unchanged (module ``m_analyze``) and runs m's functions under entry
(3), whose two sites are this module's:

  (a) ``m_analyze.clock_of_record`` -> ``clock_of_record_p``: D_p for the OLMo units (p §5.3, p:100), m's own for
      Q-F0 and Q-F3; D_p is verified at every run against PROPOSAL-p's committed bytes (``d_p_problems``; p:86);
      m's ``clock_problems`` runs unchanged;
  (c) ``m_analyze.crosscheck_coordinate`` -> ``crosscheck_coordinate_p``: the v2 posting's per-unit resolution --
      the OLMo units' outputs read from p's verdicts directory, Q-F0's from m's (Q-F3's are m's own parameter,
      ``f3_dir``) -- by calling m's own function with that directory.

(b) The roots are parameters wherever m takes them -- never a site (the seat's Q9 (b)).

PIN (Code, declared at step 6): m's two functions are bound once per process (``bind``), before any substitution, so
the replacements call m's originals; the directories the resolution uses are bound with them (the canonical ones in a
production run, temp directories in G-ANL-p's cases).

PIN (Code, declared at step 6): D_p's check reads the value the Clock returns -- ``d_p_problems`` builds p:100's
sentence from ``D_P`` at call time, so the date in use and the date verified are one value.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from types import ModuleType
from typing import Any

from ..m import stages as m_stages
from . import gcal

REPO = Path(__file__).resolve().parents[2]
OLMO_UNITS = ("OLMo-sft", "OLMo-dpo", "OLMo-instruct")
#: D_p (p §5.3, p:100): "each LOCK-p-OLMo-{ckpt} v1.0 is committed by 2026-12-15".
D_P = "2026-12-15"
#: p:100's sentence with D_p's slot (the module docstring's second PIN).
D_P_SENTENCE_FORM = "**D_p: each `LOCK-p-OLMo-{{ckpt}} v1.0` is committed by {d}**"
D_P_LINE = 100
P_VERDICTS = REPO / "data" / "p" / "verdicts"
M_VERDICTS = REPO / "data" / "m" / "verdicts"

_BOUND: dict[str, Any] = {}


class AnalysisRefusal(SystemExit):
    pass


def bind(mod: ModuleType, *, p_verdicts: Path = P_VERDICTS, m_verdicts: Path = M_VERDICTS) -> None:
    """m's originals and the resolution's directories, bound before any substitution (the module docstring's PIN)."""
    if mod.clock_of_record is clock_of_record_p or mod.crosscheck_coordinate is crosscheck_coordinate_p:
        raise AnalysisRefusal("ANALYSIS REFUSED: bind() while entry (3) is substituted -- m's originals cannot be read")
    _BOUND.update({"clock_of_record": mod.clock_of_record, "crosscheck_coordinate": mod.crosscheck_coordinate,
                   "p_verdicts": Path(p_verdicts), "m_verdicts": Path(m_verdicts), "module": mod})


def _orig(name: str) -> Any:
    if name not in _BOUND:
        raise AnalysisRefusal(f"ANALYSIS REFUSED: m_analyze is not bound (bind() first); {name} has no original")
    return _BOUND[name]


def clock_of_record_p(unit: str) -> str:
    """Entry (3) (a): D_p for p's OLMo units, m's own Clock for Q-F0 and Q-F3."""
    return D_P if unit in OLMO_UNITS else _orig("clock_of_record")(unit)


def crosscheck_coordinate_p(u: str, x: str, reason: str | None, pend: Any, out_dir: Path, v2: bool = False) -> None:
    """Entry (3) (c): m's cross-check with the unit's own verdicts directory -- p's for the OLMo units, m's for Q-F0."""
    d = _orig("p_verdicts") if u in OLMO_UNITS else _orig("m_verdicts")
    return _orig("crosscheck_coordinate")(u, x, reason, pend, d, v2=v2)


def d_p_sentence() -> str:
    """p:100's sentence for the D_P in use (read at call time)."""
    return D_P_SENTENCE_FORM.format(d=D_P)


def d_p_problems() -> list[str]:
    """[] iff PROPOSAL-p is committed at HEAD at v0.2's sha256 and its line 100 states the D_P in use (``d_p_sentence``)."""
    cp, data = m_stages._committed(gcal.PROPOSAL_P_REL)
    if cp or data is None:
        return [f"{gcal.PROPOSAL_P_REL}: {x}" for x in (cp or ["unreadable"])]
    if hashlib.sha256(data).hexdigest() != gcal.PROPOSAL_P_SHA256:
        return [f"{gcal.PROPOSAL_P_REL} is not p v0.2 at its committed sha256"]
    lines = data.decode("utf-8").split("\n")
    want = d_p_sentence()
    if len(lines) < D_P_LINE or want not in lines[D_P_LINE - 1]:
        return [f"p:{D_P_LINE} does not state D_p as {want!r}"]
    return []


# --- the output form (the seat's Q7: staged, in-file) ------------------------------------------------------------
#: m's three OLMo NOT-RUN outputs (0f35954): beside m's decisions list in every p output's p block (the seat's Q6).
M_NOT_RUN_REL = "data/m/verdicts/OLMo-{ckpt}_NOT-RUN.json"
STAGING_NOTE = ("m's function wrote this output into a staging directory seeded with copies of the final directory's "
                "files (so its refusals saw p's state); p added proposal_p_sha256 and this block and wrote the file "
                "once (the seat's Q7, 2026-11-08); every occurrence of the staging directory m recorded names the "
                "final directory instead (a seeded copy's source). A p command re-run on unchanged inputs is refused "
                "(write-once), where m's own reports 'identical' (PIN-37): the seeded copy is p's file, with its two "
                "added keys, which m compares with its own form")
#: The staging directory's name prefix: no committed p output may carry it (``run_staged``'s check).
STAGING_PREFIX = "p_analyze_staging_"


def decisions_beside() -> list[dict]:
    """The seat's Q6: m's three NOT-RUNs, named PROPOSAL-m OLMo-{ckpt}, each with its reason and output sha256 --
    beside m's validated list, which refuses a unit naming itself (p keeps m's unit strings)."""
    import json
    out = []
    for u in OLMO_UNITS:
        rel = M_NOT_RUN_REL.format(ckpt=u[len("OLMo-"):])
        cp, data = m_stages._committed(rel)
        if cp or data is None:
            raise AnalysisRefusal(f"ANALYSIS REFUSED: {rel}: {cp or ['unreadable']} (the seat's Q6 needs it)")
        doc = json.loads(data.decode("utf-8"))
        out.append({"unit": f"PROPOSAL-m {u}", "state": doc.get("state"), "reason": doc.get("reason"),
                    "output": {"path": rel, "sha256": hashlib.sha256(data).hexdigest()}})
    return out


def map_staging_paths(obj: Any, staging: Path, final_rel: str) -> Any:
    """Every occurrence of ``staging`` (as given and resolved) in every string of ``obj`` -- values, keys and text
    alike -- names ``final_rel`` instead (STAGING_NOTE: the seeded copy's source); everything else unchanged."""
    s_abs = sorted({str(staging), str(Path(staging).resolve())}, key=len, reverse=True)
    if isinstance(obj, dict):
        return {map_staging_paths(k, staging, final_rel): map_staging_paths(v, staging, final_rel)
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [map_staging_paths(v, staging, final_rel) for v in obj]
    if isinstance(obj, str):
        for a in s_abs:
            obj = obj.replace(a, final_rel)
    return obj


def _strings(obj: Any):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _strings(k)
            yield from _strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _strings(v)
    elif isinstance(obj, str):
        yield obj


def p_block(*, unit: str | None, analyzers: dict, register_rows: list, d_p: list[str]) -> dict:
    """The p block every p output carries (the seat's Q7)."""
    from . import report
    units = OLMO_UNITS if unit is None else (unit,)
    return {"proposal": "PROPOSAL-p", "register": register_rows,
            "roots": "parameters wherever m takes them -- not a site (the seat's Q9 (b))",
            "analyzers": analyzers, "d_p": {"date": D_P, "where": f"p:{D_P_LINE}", "problems": d_p},
            "disclosure": gcal.DISCLOSURE, "decisions_beside": decisions_beside(),
            "declared_sentences": {u: report.declared_sentences(u) for u in units if report.declared_sentences(u)},
            "staging": STAGING_NOTE}


def augment(doc: Any, block: dict) -> Any:
    """m's output with ``proposal_p_sha256`` beside its ``proposal_sha256`` and the p block (the seat's Q7)."""
    if not isinstance(doc, dict):
        raise AnalysisRefusal("ANALYSIS REFUSED: an m output that is not a JSON object cannot carry p's fields")
    if "proposal_p_sha256" in doc or "p" in doc:
        raise AnalysisRefusal("ANALYSIS REFUSED: m's output already carries proposal_p_sha256 or a p block")
    return {**doc, "proposal_p_sha256": gcal.PROPOSAL_P_SHA256, "p": block}


def run_staged(fn, final_dir: Path, *, block: dict | None):
    """Q7's form: ``fn(staging_dir)`` -> (status, lines, written paths) runs m's function into a staging directory
    seeded with ``final_dir``'s files; each written output, its staging paths mapped (``map_staging_paths``) and, with
    a ``block``, augmented (``augment``), is written once into ``final_dir``. ``block`` None is the regression's form:
    m's bytes, unchanged."""
    import json
    import shutil
    import tempfile
    from ..m import resume as m_resume
    from . import guard
    final_dir = Path(final_dir)
    try:
        final_rel = final_dir.resolve().relative_to(REPO.resolve()).as_posix()
    except ValueError:
        final_rel = str(final_dir)
    with tempfile.TemporaryDirectory(prefix=STAGING_PREFIX) as td:
        st = Path(td) / final_dir.name
        st.mkdir()
        seeds: dict[str, bytes] = {}
        if final_dir.is_dir():
            for f in sorted(final_dir.glob("*.json")):
                if f.is_file() and not f.is_symlink():
                    shutil.copyfile(f, st / f.name)
                    seeds[f.name] = (st / f.name).read_bytes()
        try:
            status, lines, written = fn(st)
        except BaseException as e:                  # an m exception carrying printed lines (a posting FAIL): mapped
            if isinstance(getattr(e, "lines", None), list):
                e.lines = [map_staging_paths(ln, st, final_rel) if isinstance(ln, str) else ln for ln in e.lines]
            msg = str(e)
            if isinstance(e, SystemExit) and "exists with different bytes -- write-once" in msg:
                hit = [n for n, b in seeds.items() if n in msg and _is_p_output(b)]
                if hit:                             # N-9: p's own output, already written once
                    tmps = sorted(x.name for x in final_dir.glob("*.tmp"))
                    raise AnalysisRefusal(
                        f"ANALYSIS REFUSED: {hit[0]} is a p output, already written once. m compared its own form with "
                        f"p's file, which carries p's two added keys, so a p command re-run is refused whether or not "
                        f"its inputs changed (STAGING_NOTE). "
                        + (f"Temp files of an interrupted write are present ({tmps}): the set may be part-written -- "
                           f"the seat rules on it. " if tmps else "The record stands; nothing is to be moved aside. ")
                        + "Nothing written.") from None
            raise
        stray = [str(w) for w in written if Path(w).resolve().parent != st.resolve() or Path(w).is_symlink()]
        if stray:
            raise AnalysisRefusal(f"ANALYSIS REFUSED: m reported {len(stray)} output(s) outside the staging directory "
                                  f"(nothing written)")
        reported = {Path(w).name for w in written}
        left = sorted(f.name for f in st.iterdir() if f.name not in reported
                      and (f.name not in seeds or not f.is_file() or f.read_bytes() != seeds[f.name]))
        if left:                                    # N-1: m wrote, or changed, a file it did not report
            raise AnalysisRefusal(f"ANALYSIS REFUSED: the staging directory holds {len(left)} file(s) m did not report "
                                  f"as written ({left[:3]}) (nothing written)")
        prepared = []
        for w in written:
            w = Path(w)
            if block is None:
                data = w.read_bytes()
            else:
                doc = map_staging_paths(json.loads(w.read_text(encoding="utf-8")), st, final_rel)
                aug = augment(doc, block)
                if any(STAGING_PREFIX in x or td in x for x in _strings(aug)):
                    raise AnalysisRefusal(f"ANALYSIS REFUSED: {w.name} still names the staging directory after the "
                                          f"mapping (nothing written)")
                data = m_resume.json_text(aug, indent=1).encode("utf-8")
            prepared.append((final_dir / w.name, data))
        try:                                        # every target checked, then two-phase writes (guard.write_once_all)
            hows = guard.write_once_all(prepared, what="p output")
        except guard.GuardStop as e:
            raise AnalysisRefusal(f"ANALYSIS REFUSED: {e} -- write-once; nothing written") from None
        finals = [target for target, _ in prepared]
        lines = [map_staging_paths(ln, st, final_rel) if isinstance(ln, str) else ln for ln in lines]
    return status, lines, finals, hows


def _is_p_output(data: bytes) -> bool:
    """A p output: a JSON object carrying proposal_p_sha256 and a p block (``augment``'s two keys)."""
    try:
        doc = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return False
    return isinstance(doc, dict) and "proposal_p_sha256" in doc and isinstance(doc.get("p"), dict)


def _selftest(chk) -> None:
    import types
    from . import register
    ma = types.ModuleType("m_analyze")
    calls = []
    ma.clock_of_record = lambda u: {"Q-F0": "2026-10-30", "Q-F3": "2026-12-22"}.get(u, "2026-11-30")
    ma.crosscheck_coordinate = lambda u, x, reason, pend, out_dir, v2=False: calls.append((u, out_dir, v2))
    saved = dict(_BOUND)
    try:
        bind(ma, p_verdicts=Path("/p-dir"), m_verdicts=Path("/m-dir"))
        with register.substituted(3, ma, {"clock_of_record": clock_of_record_p,
                                          "crosscheck_coordinate": crosscheck_coordinate_p}):
            clocks = {u: ma.clock_of_record(u) for u in ("OLMo-sft", "OLMo-dpo", "OLMo-instruct", "Q-F0", "Q-F3")}
            for u in ("Q-F0", "OLMo-sft", "OLMo-dpo", "OLMo-instruct"):
                ma.crosscheck_coordinate(u, "PASS", None, None, Path("/given"), v2=True)
            try:
                bind(ma)
                rebind = "bound"
            except AnalysisRefusal:
                rebind = "refused"
        restored = ma.clock_of_record("OLMo-sft") == "2026-11-30"
    finally:
        _BOUND.clear()
        _BOUND.update(saved)
    chk("analysis: entry (3) (a) -- D_p for p's three OLMo units, m's own Clock for Q-F0 and Q-F3 -- and (c) -- the "
        "v2 cross-check reads the OLMo units from p's directory and Q-F0 from m's, whatever directory m passes -- under "
        "the register; a bind while substituted is refused; m's functions restored",
        clocks == {"OLMo-sft": D_P, "OLMo-dpo": D_P, "OLMo-instruct": D_P, "Q-F0": "2026-10-30", "Q-F3": "2026-12-22"}
        and calls == [("Q-F0", Path("/m-dir"), True), ("OLMo-sft", Path("/p-dir"), True),
                      ("OLMo-dpo", Path("/p-dir"), True), ("OLMo-instruct", Path("/p-dir"), True)]
        and rebind == "refused" and restored, (clocks, calls, rebind))
    chk("analysis: D_p is verified against PROPOSAL-p's committed bytes (p:100's sentence, v0.2's sha256)",
        d_p_problems() == [], d_p_problems())
    st = Path("/tmp/p_analyze_staging_x/verdicts")
    doc = {"a": str(st / "POSTING-v2_outputs.of-record.json"), "b": ["data/m/x", str(st)], "c": 3,
           str(st / "k.json"): f"wrote {st}/y.json (sha256 0)"}
    mapped = map_staging_paths(doc, st, "data/p/verdicts")
    chk("analysis: every occurrence of the staging directory -- a value, a key, mid-text -- names the final directory; "
        "other values unchanged (N10)",
        mapped == {"a": "data/p/verdicts/POSTING-v2_outputs.of-record.json", "b": ["data/m/x", "data/p/verdicts"],
                   "c": 3, "data/p/verdicts/k.json": "wrote data/p/verdicts/y.json (sha256 0)"}, mapped)
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        fin = Path(td) / "fin"

        def outside(stg):
            o = Path(td) / "elsewhere.json"
            o.write_text("{}", encoding="utf-8")
            return "written", [], [o]

        def leaks(stg):
            (stg / "x.json").write_text('{"note": "' + STAGING_PREFIX + 'zz/x"}', encoding="utf-8")
            return "written", [], [stg / "x.json"]

        def unreported(stg):
            (stg / "a.json").write_text("{}", encoding="utf-8")
            (stg / "b.json").write_text("{}", encoding="utf-8")
            return "written", [], [stg / "a.json"]
        got = []
        for f in (outside, leaks, unreported):
            try:
                run_staged(f, fin, block={"proposal": "PROPOSAL-p"})
                got.append("written")
            except AnalysisRefusal:
                got.append("refused")
        none_written = not fin.exists() or not any(fin.iterdir())
    with tempfile.TemporaryDirectory() as td:
        fin2 = Path(td) / "fin2"
        fin2.mkdir()
        (fin2 / "b.json").symlink_to(Path(td) / "victim.json")

        def two(stg):
            for n in ("a.json", "b.json"):
                if (stg / n).is_symlink() or (stg / n).exists():
                    continue
                (stg / n).write_text('{"proposal_sha256": "x"}', encoding="utf-8")
            return "written", [], [stg / "a.json", stg / "b.json"]
        try:
            run_staged(two, fin2, block={"proposal": "PROPOSAL-p"})
            all_or_none = "written"
        except AnalysisRefusal:
            all_or_none = "refused"
        a_written = (fin2 / "a.json").exists()
        victim = (Path(td) / "victim.json").exists()

        def rerun(stg):
            raise SystemExit(f"REFUSED: {seeded} exists with different bytes -- write-once (move it aside by hand on "
                             f"the seat's ruling, PIN-37)")
        fin3 = Path(td) / "fin3"
        fin3.mkdir()
        seeded = "OLMo-sft_NOT-RUN.json"
        (fin3 / seeded).write_text(json.dumps({"proposal_p_sha256": "p" * 64, "p": {}}), encoding="utf-8")
        try:
            run_staged(rerun, fin3, block={"proposal": "PROPOSAL-p"})
            rr = "ran"
        except AnalysisRefusal as e:
            rr = "p's wording" if "already written once" in str(e) and "nothing is to be moved aside" in str(e) else str(e)
        (fin3 / "OLMo-sft_secondary.json.tmp").write_text("{", encoding="utf-8")   # a crash's left-over
        try:
            run_staged(rerun, fin3, block={"proposal": "PROPOSAL-p"})
            rr2 = "ran"
        except AnalysisRefusal as e:
            rr2 = "part-written" if "part-written" in str(e) and "seat rules" in str(e) else str(e)
    chk("analysis: run_staged refuses an output m reports outside the staging directory, one that still names a "
        "staging directory after the mapping, and a file m wrote without reporting it -- nothing written (N10, N-1); a "
        "link at a later target refuses the whole set before the first write (N-1); m's write-once refusal of a seeded "
        "p output is restated in p's words (N-9)",
        got == ["refused"] * 3 and none_written and all_or_none == "refused" and not a_written and not victim
        and rr == "p's wording" and rr2 == "part-written", (got, all_or_none, a_written, victim, rr, rr2))
    saved_dp = D_P
    try:
        globals()["D_P"] = "2026-12-31"
        moved = (d_p_problems(), clock_of_record_p.__globals__["D_P"])
    finally:
        globals()["D_P"] = saved_dp
    chk("analysis: D_p's check reads the D_P the Clock returns (a moved D_P fails it; MINOR 7)",
        bool(moved[0]) and moved[1] == "2026-12-31" and d_p_problems() == [], moved)
    aug = augment({"proposal_sha256": "m" * 64, "unit": "OLMo-sft"}, {"proposal": "PROPOSAL-p"})
    try:
        augment(aug, {})
        twice = "accepted"
    except AnalysisRefusal:
        twice = "refused"
    chk("analysis: augmentation keeps m's fields and adds proposal_p_sha256 beside m's proposal_sha256 and the p block; "
        "an output carrying either already is refused",
        aug == {"proposal_sha256": "m" * 64, "unit": "OLMo-sft", "proposal_p_sha256": gcal.PROPOSAL_P_SHA256,
                "p": {"proposal": "PROPOSAL-p"}} and twice == "refused")
    db = decisions_beside()
    chk("analysis: the seat's Q6 -- m's three NOT-RUNs named PROPOSAL-m OLMo-{ckpt}, each with its reason and the "
        "committed output's sha256",
        [d["unit"] for d in db] == ["PROPOSAL-m OLMo-sft", "PROPOSAL-m OLMo-dpo", "PROPOSAL-m OLMo-instruct"]
        and all(d["state"] == "NOT-RUN" and d["reason"] and len(d["output"]["sha256"]) == 64 for d in db), db)
