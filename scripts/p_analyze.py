#!/usr/bin/env python3
"""PROPOSAL-p's analyzer (p v0.2 §4.4; register entry (3); the design seat's answer of 2026-11-08, ``de729c4``, §2).

scripts/m_analyze.py is imported unchanged -- module ``m_analyze``, scripts/ on sys.path, the import system registering
it -- at its pinned sha256 (``M_ANALYZER_SHA256``, the analyzer LOCK-m-F3 v0.1 names), and m's functions compute every
p output under register entry (3) (``valence_core.p.analysis``): (a) the Clock -- D_p for the OLMo units, m's own for
Q-F0 and Q-F3 -- and (c) the v2 posting's per-unit verdicts-dir resolution -- p's directory for the OLMo units, m's for
Q-F0, mf3's for Q-F3 (m's own ``f3_dir`` parameter); (b) the roots are parameters wherever m takes them, never a site
(the seat's Q9). m's proposal pin is kept; ``proposal_p_sha256`` and a ``p`` block are added beside it in every output,
by the seat's Q7 form (``analysis.run_staged``): m's function writes into a staging directory seeded with the final
directory's files, and p writes each output once into the final directory with its fields added.

  ganl [--out DIR]    G-ANL-p (p §4.4; the seat's Q8): m's battery unchanged, its count and coverage asserted against
                      G-ANL-F3's artifact; p's own groups (``_selftest``); then data/p/gates/G-ANL-p.json, write-once,
                      against committed blobs (a --out test directory is never of record and never inside the repo).
  not-run --unit OLMo-{ckpt} --record R [--time T] [--qual Q] [--v2-closure --campaign C|none]
  verdicts --unit OLMo-{ckpt} --lock L --decisions D [--campaign C] [--time T] [--qual Q] [--adjudication A]
           [--pi-stop P]
  posting --posting v2 --tuple T --sentences S [--rewrites R] [--flag-source F]
                      each m's command for p's units, defaults under data/p (checkpoints data/p/ckpt, outputs
                      data/p/verdicts); the v2 posting reads Q-F0's outputs in data/m/verdicts and Q-F3's in
                      data/mf3/verdicts. v1 is m's posting (p's units enter none). Path arguments resolve against the
                      repository root when relative (m's ``_cli_path``, PIN-V2-8).

Every command first checks m's analyzer at its pin, both analyzers and the code of record committed at HEAD (p's
package, m's, olmo_hf.py and p's drivers), and D_p against PROPOSAL-p's committed bytes (exit 2 otherwise).

PIN (Code, declared at step 6): p's outputs are bound to p's code -- every p block names m's analyzer, p's analyzer and
p's package_sha256 (``analyzer_blobs``); a p-form VERDICTS also requires its lock to name p's analyzer's sha256 and p's
package_sha256 (m's PIN-14 binds m's analyzer, package and closure; p's are p's to bind). Exit codes are m's
(``m_analyze._exit_of``); p's own refusals (an analysis refusal, a write-once refusal) exit 2, as m's do.
"""
from __future__ import annotations

import argparse
import contextlib
import copy
import dataclasses
import hashlib
import json
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
for _p in (REPO, REPO / "scripts"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import m_analyze  # noqa: E402  (scripts/m_analyze.py, unchanged)
from valence_core.m import resume as m_resume  # noqa: E402
from valence_core.m import stages as m_stages  # noqa: E402
from valence_core.p import analysis, gcal, guard, register  # noqa: E402
from valence_core.p.stage import lock_names  # noqa: E402

M_ANALYZER_REL = "scripts/m_analyze.py"
#: The analyzer of record (10a2bbb; LOCK-m-F3 v0.1, 1e79955, names it).
M_ANALYZER_SHA256 = "d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48"
P_ANALYZER_REL = "scripts/p_analyze.py"
UNITS = analysis.OLMO_UNITS
P_CKPT = REPO / "data" / "p" / "ckpt"
P_VERDICTS = analysis.P_VERDICTS
M_VERDICTS = analysis.M_VERDICTS
F3_VERDICTS = REPO / m_analyze.F3_VERDICTS_REL
GANL_REL = "data/p/gates/G-ANL-p.json"
GANL_SCHEMA = "p-ganl-v1"
GANL_F3_REL = "data/m/gates/G-ANL-F3.json"
#: The NOT-RUN regression's bindings (the seat's Q8), in full: the analyzer, package and closure m's three OLMo NOT-RUN
#: outputs (0f35954) were written under (e0b4f2c's analyzer).
NOT_RUN_RECORD_ANALYZER_COMMIT = "e0b4f2c"
NOT_RUN_RECORD_ANALYZER_SHA256 = "6ec3222b54c78ea5107a5ef89f9ffd3dd2fc649394f0dc6180280023c82b93d9"
NOT_RUN_RECORD_PACKAGE_SHA256 = "60199b36557ac283771b83dcb4be101b5c56880dceacdecd05cce5a578e7feec"
NOT_RUN_RECORD_CLOSURE_SHA256 = "a3bc7bb9df3d8361bfa803238e61a61a7eef76a6d839540413e53cd7919cb22b"
#: The roots m's functions would read by default; on p's paths they are parameters, never read (the seat's Q9 (b)).
M_ROOT_NAMES = ("CKPT_REL", "VERDICTS_REL")
#: p's own refusals: exit 2, as m's refusals (N6).
P_REFUSALS = (analysis.AnalysisRefusal, guard.GuardStop)


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def binding_problems(*, canonical: bool) -> list[str]:
    """m's analyzer at its pin; canonically, both analyzers and the code of record (p's package, m's, olmo_hf.py and
    p_sessions.py: G-CAL-p's check) committed at HEAD; D_p against PROPOSAL-p."""
    probs = []
    got = _sha((REPO / M_ANALYZER_REL).read_bytes())
    if got != M_ANALYZER_SHA256:
        probs.append(f"{M_ANALYZER_REL} hashes to {got[:16]}, not the analyzer of record {M_ANALYZER_SHA256[:16]}")
    if canonical:
        for rel in (M_ANALYZER_REL, P_ANALYZER_REL):
            cp, _ = m_stages._committed(rel)
            probs += [f"{rel}: {x}" for x in cp]
        probs += [f"committed: {x}" for x in gcal.committed_problems()]
    probs += [f"D_p: {x}" for x in analysis.d_p_problems()]
    return probs


def analyzer_blobs() -> dict:
    """The code every p output names (the module docstring's PIN): both analyzers' sha256s and p's package_sha256."""
    out = {rel: {"sha256": _sha((REPO / rel).read_bytes())} for rel in (M_ANALYZER_REL, P_ANALYZER_REL)}
    out["valence_core/p"] = {"package_sha256": guard.package_sha256()}
    return out


def code_shas() -> dict:
    """G-ANL-p's code record (the stage's precheck compares it with the current code; MINOR 9)."""
    return {"p_package_sha256": guard.package_sha256(), "m_package_sha256": m_resume.package_sha256(),
            "m_analyzer_sha256": _sha((REPO / M_ANALYZER_REL).read_bytes()),
            "p_analyzer_sha256": _sha((REPO / P_ANALYZER_REL).read_bytes())}


def register_rows() -> list[dict]:
    return [e for e in register.table() if e["n"] == 3]


def entry3():
    """Register entry (3), (a) and (c) (the module docstring)."""
    return register.substituted(3, m_analyze, {"clock_of_record": analysis.clock_of_record_p,
                                               "crosscheck_coordinate": analysis.crosscheck_coordinate_p})


def _block(unit: str | None, *, resolution: dict | None = None) -> dict:
    b = analysis.p_block(unit=unit, analyzers=analyzer_blobs(), register_rows=register_rows(),
                         d_p=analysis.d_p_problems())
    if resolution is not None:
        b["resolution"] = resolution
    return b


def _named_dir(d: Path) -> str:
    """A directory as an output records it: repo-relative, or '(a test directory)' -- never a machine path."""
    try:
        return Path(d).resolve().relative_to(REPO.resolve()).as_posix()
    except ValueError:
        return "(a test directory)"


def run_not_run_p(unit, record, time_p=None, qual_p=None, *, v2_closure=False, campaign_p=None, out=P_VERDICTS,
                  ckpt=P_CKPT, env=None, p_mode=True):
    """m's ``not-run`` for p's unit: entry (3) in force, the roots p's (``out``, ``ckpt``), staged (Q7). ``p_mode``
    False is the regression's form: no substitution, no p field."""
    env = env or m_analyze.production_env()

    def fn(st):
        call = lambda: m_analyze.run_not_run(unit, record, time_p, qual_p, st, env, v2_closure=v2_closure,  # noqa: E731
                                             campaign_p=campaign_p, ckpt_dir=ckpt)
        if not p_mode:
            return call()
        with entry3():
            return call()
    return analysis.run_staged(fn, Path(out), block=_block(unit) if p_mode else None)


def lock_binding_problems(lock: Path) -> list[str]:
    """A p-form VERDICTS's lock names p's analyzer's sha256 and p's package_sha256 (the module docstring's PIN)."""
    try:
        text = Path(lock).read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return [f"the lock is unreadable ({type(e).__name__})"]
    blobs = analyzer_blobs()
    return [f"the lock does not name {what} {v[:16]}... (as a whole line or between backticks)" for what, v in
            (("p's analyzer sha256", blobs[P_ANALYZER_REL]["sha256"]),
             ("p's package_sha256", blobs["valence_core/p"]["package_sha256"])) if not lock_names(text, v)]


def run_verdicts_p(unit, lock, decisions, *, campaign=None, time=None, qual=None, adjudication=None, pi_stop=None,
                   out=P_VERDICTS, ckpt=P_CKPT, env=None, p_mode=True, inputs_extra=None):
    """m's ``verdicts`` for p's unit (``p_mode`` as in ``run_not_run_p``); ``inputs_extra``: any further
    ``VerdictInputs`` field (Q-F0's olmo_states, sentences and flag_source in the regression's form)."""
    env = env or m_analyze.production_env()
    if p_mode:
        lp = lock_binding_problems(Path(lock))
        if lp:
            raise analysis.AnalysisRefusal(f"ANALYSIS REFUSED: {unit}'s VERDICTS: {lp} (nothing written)")
    ck = Path(ckpt)
    base = m_analyze.VerdictInputs(
        unit=unit, lock=Path(lock), decisions=Path(decisions),
        campaign=Path(campaign) if campaign else ck / f"{unit}_campaign.json",
        time=Path(time) if time else ck / f"{unit}_time.json", qual=Path(qual) if qual else ck / f"{unit}_qual.json",
        out=Path(out), adjudication=Path(adjudication) if adjudication else None,
        pi_stop=Path(pi_stop) if pi_stop else None)
    base = dataclasses.replace(base, **(inputs_extra or {}))

    def fn(st):
        inp = dataclasses.replace(base, out=st)
        if not p_mode:
            return m_analyze.run_verdicts(inp, env)
        with entry3():
            return m_analyze.run_verdicts(inp, env)
    return analysis.run_staged(fn, Path(out), block=_block(unit) if p_mode else None)


def run_posting_p(tuple_p, sentences, *, flag_source=None, rewrites=None, out=P_VERDICTS, m_verdicts=M_VERDICTS,
                  f3_dir=F3_VERDICTS, env=None):
    """m's v2 posting with entry (3)'s resolution (OLMo units from the bound p directory, Q-F0 from the bound m
    directory, which ``m_verdicts`` must be: one directory, never two)."""
    env = env or m_analyze.production_env()
    if Path(m_verdicts).resolve() != Path(analysis._orig("m_verdicts")).resolve():
        raise analysis.AnalysisRefusal("ANALYSIS REFUSED: the posting's m directory is not the one entry (3)'s "
                                       "resolution is bound to (nothing written)")
    res = {**{u: _named_dir(analysis._orig("p_verdicts")) for u in UNITS}, "Q-F0": _named_dir(m_verdicts),
           "Q-F3": _named_dir(f3_dir)}

    def fn(st):
        with entry3():
            return m_analyze.run_posting_v2(Path(tuple_p), Path(sentences),
                                            Path(flag_source) if flag_source else REPO / m_analyze.FLAG_SOURCE_REL,
                                            Path(m_verdicts), Path(f3_dir), st, env,
                                            rewrites=Path(rewrites) if rewrites else None)
    return analysis.run_staged(fn, Path(out), block=_block(None, resolution=res))


# --- G-ANL-p (the seat's Q8) ------------------------------------------------------------------------------------
def _regression_qf0() -> dict:
    """Q-F0's two outputs through p's path (``run_verdicts_p``, m's form) on the G-ANL-F3 battery's identity binding,
    byte for byte, with m's own regression's checks (m's ``_bt_qf0_regression``: PIN-29's seven pins, the lock naming
    the identity of record, the preprint blob) taken from m's function."""
    mreg = m_analyze._bt_qf0_regression()
    out: dict = {"m": {k: mreg.get(k) for k in ("pins", "identity", "preprint", "status", "error")},
                 "m_outputs_identical": all(v.get("identical") for v in (mreg.get("outputs") or {}).values())
                 and len(mreg.get("outputs") or {}) == 2, "outputs": {}, "error": None}
    ablob = m_analyze._bt_git_blob(f"{m_analyze.RECORD_ANALYZER_COMMIT}:{M_ANALYZER_REL}")
    tab_p = REPO / "data" / "m" / "gates" / "m_posting_sentences.json"
    pre = json.loads(tab_p.read_text(encoding="utf-8"))["preprint"]
    pblob = m_analyze._bt_git_blob(f"{m_analyze.REGRESSION_PREPRINT_COMMIT}:{pre['path']}")
    if ablob is None or _sha(ablob) != m_analyze.RECORD_ANALYZER_SHA256 or pblob is None or _sha(pblob) != pre["sha256"]:
        out["error"] = "the record's analyzer or preprint blob is not the pinned one"
        return out
    apath = (REPO / M_ANALYZER_REL).resolve()
    env = m_analyze.Env(proposal_path=REPO / m_analyze.PROPOSAL_REL,
                        committed=lambda q: ([], ablob) if Path(q).resolve() == apath else m_analyze._prod_committed(Path(q)),
                        analyzer_path=apath, package_sha256=m_analyze.RECORD_PACKAGE_SHA256,
                        closure_sha256=m_analyze.RECORD_CLOSURE_SHA256, allow_stub=False,
                        gate_line=lambda name: (f"GATE {name} (the G-ANL-p regression; not logged)", []),
                        read_repo_file=lambda rel: pblob if rel == pre["path"] else m_analyze._prod_read(rel),
                        say=lambda line: None)
    ck, vd = REPO / m_analyze.CKPT_REL, REPO / m_analyze.VERDICTS_REL
    with tempfile.TemporaryDirectory(prefix="p_ganl_qf0_") as td:
        try:
            run_verdicts_p("Q-F0", REPO / "LOCK-m-F0.md", vd / "Q-F0_decisions.json", campaign=ck / "Q-F0_campaign.json",
                           time=ck / "Q-F0_time.json", qual=ck / "Q-F0_qual.json", out=Path(td) / "final", env=env,
                           p_mode=False, inputs_extra={"olmo_states": vd / "Q-F0_olmo-states.json", "sentences": tab_p,
                                                       "flag_source": REPO / m_analyze.FLAG_SOURCE_REL})
        except (m_analyze.AnlRefusal, m_analyze.AnlStop) as e:
            out["error"] = f"{type(e).__name__}: {e}"
            return out
        for rel in m_analyze.REGRESSION_OUTPUTS:
            got = (Path(td) / "final" / Path(rel).name).read_bytes()
            rec = (REPO / rel).read_bytes()
            out["outputs"][rel] = {"identical": got == rec, "sha256": _sha(got)}
    return out


def _regression_not_run() -> dict:
    """m's three OLMo NOT-RUN outputs (0f35954) through p's staged path in m's form, on the bindings they were written
    under (e0b4f2c's analyzer blob, its package and closure, each pinned in full here and equal to the record's)."""
    out: dict = {"outputs": {}, "error": None, "binding": None}
    ablob = m_analyze._bt_git_blob(f"{NOT_RUN_RECORD_ANALYZER_COMMIT}:{M_ANALYZER_REL}")
    if ablob is None or _sha(ablob) != NOT_RUN_RECORD_ANALYZER_SHA256:
        out["error"] = "the NOT-RUN outputs' analyzer blob is not the pinned one"
        return out
    apath = (REPO / M_ANALYZER_REL).resolve()
    out["binding"] = {"analyzer_sha256": NOT_RUN_RECORD_ANALYZER_SHA256, "package_sha256": NOT_RUN_RECORD_PACKAGE_SHA256,
                      "closure_sha256": NOT_RUN_RECORD_CLOSURE_SHA256}
    for ck in ("sft", "dpo", "instruct"):
        rec_out = REPO / m_analyze.VERDICTS_REL / f"OLMo-{ck}_NOT-RUN.json"
        doc = json.loads(rec_out.read_text(encoding="utf-8"))
        if {k: doc.get(k) for k in out["binding"]} != out["binding"]:
            out["error"] = f"OLMo-{ck}_NOT-RUN.json does not record the pinned bindings"
            return out
        env = m_analyze.Env(proposal_path=REPO / m_analyze.PROPOSAL_REL,
                            committed=lambda q: ([], ablob) if Path(q).resolve() == apath
                            else m_analyze._prod_committed(Path(q)),
                            analyzer_path=apath, package_sha256=NOT_RUN_RECORD_PACKAGE_SHA256,
                            closure_sha256=NOT_RUN_RECORD_CLOSURE_SHA256, allow_stub=False,
                            gate_line=lambda name: (f"GATE {name} (the G-ANL-p regression; not logged)", []),
                            read_repo_file=m_analyze._prod_read, say=lambda line: None)
        with tempfile.TemporaryDirectory(prefix="p_ganl_nr_") as td:
            record = REPO / m_analyze.VERDICTS_REL / f"OLMo-{ck}_not-run-record.json"
            try:
                run_not_run_p(f"OLMo-{ck}", record, out=Path(td) / "final", ckpt=REPO / m_analyze.CKPT_REL, env=env,
                              p_mode=False)
            except (m_analyze.AnlRefusal, m_analyze.AnlStop) as e:
                out["error"] = f"OLMo-{ck}: {type(e).__name__}: {e}"
                return out
            got = (Path(td) / "final" / rec_out.name).read_bytes()
            out["outputs"][rec_out.relative_to(REPO).as_posix()] = {"identical": got == rec_out.read_bytes(),
                                                                    "sha256": _sha(got)}
    return out


def _data_p_snapshot() -> dict:
    """data/p's state (N11): every file's sha256, the reports and checkpoints included."""
    root = REPO / "data" / "p"
    return {p.relative_to(REPO).as_posix(): _sha(p.read_bytes()) for p in sorted(root.rglob("*")) if p.is_file()}


def _selftest(chk) -> None:
    """G-ANL-p's battery (the seat's Q8): m's battery unchanged, then p's groups, then the regression."""
    def _verdicts_fixture(base: Path) -> dict:
        """SELF-TEST ONLY (m's own stub-startup seam, as m's battery uses it): a synthetic OLMo-sft campaign for p's
        VERDICTS group (MAJOR 5), built as m's battery builds its OLMo case (``_bt_reader``'s C3-OLMO-COMPLETE): m's
        ``_Camp`` (stages.run_campaign, the production writer, in a temp root), the OLMo gate checkpoints, a lock naming
        m's analyzer, package and closure and p's analyzer and package."""
        from valence_core.m import runner_olmo, stages, testing
        base.mkdir(parents=True, exist_ok=True)
        a_sha = _sha((REPO / M_ANALYZER_REL).read_bytes())
        pkg = m_resume.package_sha256()
        cl = m_analyze.closure_sha256(m_analyze.closure())
        blobs = analyzer_blobs()
        lock_text = (f"LOCK (G-ANL-p) analyzer {a_sha} package {pkg} closure {cl} p_analyzer "
                     f"`{blobs[P_ANALYZER_REL]['sha256']}` p_package `{blobs['valence_core/p']['package_sha256']}`\n")
        lock = base / "LOCK-pganl.md"
        lock.write_text(lock_text, encoding="utf-8")
        bare = base / "LOCK-pganl-m-only.md"
        bare.write_text(f"LOCK (G-ANL-p) analyzer {a_sha} package {pkg} closure {cl} embedded "
                        f"0{blobs[P_ANALYZER_REL]['sha256']}0 0{blobs['valence_core/p']['package_sha256']}0\n",
                        encoding="utf-8")
        C = m_analyze._Camp(base, _sha(lock_text.encode("utf-8")))
        dec = base / "decisions-OLMo-sft.json"
        dec.write_text(json.dumps({"schema": m_analyze.DECISIONS_SCHEMA, "unit": "OLMo-sft",
                                   "decisions_with_other_outcomes_known": []}), encoding="utf-8")
        kit = testing.olmo_kit()
        setup = runner_olmo.OLMoSetup(audit=kit["audit"], ban_ids=kit["ban_ids"], ban_strings=kit["ban_strings"],
                                      term_rx=kit["term_rx"], audit_sha16=runner_olmo.olmo_audit_sha16())
        r_o = C.root("olmo")
        counts = {"A0-OLMo-sft": 2, "A0s-OLMo-sft": 2}
        with m_analyze._bt_patched(stages, "olmo_startup", lambda adapter, ckpt: setup), m_analyze._bt_pod("pod-p-ganl"):
            res_o, exc_o = C.run("OLMo-sft", r_o, C.adapter("OLMo-sft", counts), counts)
        t_o, q_o = m_analyze._bt_olmo_gates(base, r_o)
        from valence_core.p import identity as p_identity
        for cpath in ([Path(res_o["checkpoint"])] if res_o else []) + [t_o, q_o]:
            ck_ = json.loads(cpath.read_text(encoding="utf-8"))
            ck_["identity"].update(p_identity.run_values())   # N-8: p's checkpoints carry p's four identity fields
            cpath.write_text(json.dumps(ck_), encoding="utf-8")
        env = m_analyze._bt_env(base, closure_sha256=cl, package_sha256=pkg)
        return {"lock": lock, "bare_lock": bare, "decisions": dec, "campaign": Path(res_o["checkpoint"]) if res_o else None,
                "campaign_error": None if exc_o is None else f"{type(exc_o).__name__}: {exc_o}", "time": t_o, "qual": q_o,
                "ckpt": r_o / "ckpt", "env": env}

    extra: dict = {}
    res = m_analyze.battery()
    try:
        f3 = json.loads((REPO / GANL_F3_REL).read_text(encoding="utf-8"))
        want_n, want_cov = f3["battery"]["checks_total"], len(f3["battery"]["coverage_ids"])
    except (OSError, ValueError, KeyError) as e:
        want_n = want_cov = None
        extra["f3_artifact_error"] = f"{type(e).__name__}: {e}"
    extra["m_battery"] = {"ok": res["ok"], "checks_pass": res["checks_pass"], "checks_total": res["checks_total"],
                          "coverage_ids": len(res["coverage_ids"]), "g_anl_f3": {"checks_total": want_n,
                                                                                 "coverage_ids": want_cov}}
    chk("ganl-p: m's battery runs unchanged and passes, its check count and coverage those of G-ANL-F3's artifact",
        res["ok"] and res["checks_total"] == want_n and len(res["coverage_ids"]) == want_cov, extra["m_battery"])
    chk("ganl-p: m's analyzer is the analyzer of record (its pin); D_p verifies against PROPOSAL-p's committed bytes",
        binding_problems(canonical=False) == [], binding_problems(canonical=False))
    snap0 = _data_p_snapshot()
    touched: list[str] = []

    class _Never:
        """N3's sentinel: any use of m's root constant (a path join, str, format, comparison) is recorded and raises."""

        def __init__(self, name: str) -> None:
            object.__setattr__(self, "_n", name)

        def _hit(self, *a, **k):
            touched.append(object.__getattribute__(self, "_n"))
            raise AssertionError(f"G-ANL-p: m_analyze.{object.__getattribute__(self, '_n')} read on p's path")
        __fspath__ = __str__ = __format__ = __add__ = __radd__ = __truediv__ = __rtruediv__ = __eq__ = __hash__ = _hit
        __len__ = __iter__ = __contains__ = __getitem__ = _hit

        def __repr__(self) -> str:
            return f"<never-read {object.__getattribute__(self, '_n')}>"

    @contextlib.contextmanager
    def sentinels():
        # SELF-TEST ONLY (the seat's Q9 (b)'s proof): m's root constants replaced for the block by sentinels that
        # record and raise on any use, restored in finally.
        saved = {n: getattr(m_analyze, n) for n in M_ROOT_NAMES}
        try:
            for n in M_ROOT_NAMES:
                setattr(m_analyze, n, _Never(n))
            yield
        finally:
            for n, v in saved.items():
                setattr(m_analyze, n, v)

    with tempfile.TemporaryDirectory(prefix="p_ganl_") as td:
        base = Path(td)
        pv, mv, f3d, out = base / "pv", base / "mv", base / "f3", base / "out"
        for d_ in (pv, mv, f3d, out):
            d_.mkdir()
        orig = (m_analyze.clock_of_record, m_analyze.crosscheck_coordinate)
        try:
            analysis.bind(m_analyze, p_verdicts=pv, m_verdicts=mv)
            with entry3():
                clocks = {u: m_analyze.clock_of_record(u) for u in ("OLMo-sft", "OLMo-dpo", "OLMo-instruct", "Q-F0",
                                                                        "Q-F3")}
            try:
                with entry3():
                    raise ValueError("planted")
            except ValueError:
                pass
            chk("ganl-p: entry (3) on the real m_analyze -- D_p for the three OLMo units, m's D1 and D2 for Q-F0 and "
                "Q-F3 -- and both functions restored after the block and after an exception inside it",
                clocks == {"OLMo-sft": analysis.D_P, "OLMo-dpo": analysis.D_P, "OLMo-instruct": analysis.D_P,
                           "Q-F0": m_analyze.D1, "Q-F3": m_analyze.D2}
                and (m_analyze.clock_of_record, m_analyze.crosscheck_coordinate) == orig, clocks)
            # a p NOT-RUN by its Clock (D_p), through p's path, under the sentinels (Q9 (b)'s proof)
            rec = {"schema": m_analyze.NOT_RUN_RECORD_SCHEMA, "unit": "OLMo-sft", "cause": "clock:no-box", "also": [],
                   "date": analysis.D_P, "detail": "G-ANL-p's case: p's OLMo-sft with no box at D_p (a synthetic record)",
                   "decisions_with_other_outcomes_known": [
                       {"decision": "PROPOSAL-p adopted (18b0111)", "date": "2026-11-07", "other_unit": "Q-F0",
                        "other_state": "PASS"}]}
            recp = base / "OLMo-sft_not-run-record.json"
            recp.write_text(json.dumps(rec), encoding="utf-8")
            env = m_analyze._bt_env(base)
            try:
                with sentinels():
                    st, lines, finals, hows = run_not_run_p("OLMo-sft", recp, out=pv, ckpt=base / "ck", env=env)
                nr = json.loads(finals[0].read_text(encoding="utf-8"))
                nr_err = None
            except (SystemExit, AssertionError) as e:
                nr, nr_err = None, f"{type(e).__name__}: {e}"
            text = json.dumps(nr) if nr is not None else ""
            chk("ganl-p: p's Clock NOT-RUN through p's path -- m's run_not_run under entry (3), the roots p's "
                "parameters, the record dated D_p the Clock of record -- with m's CKPT_REL and VERDICTS_REL sentinels "
                "that record and raise on any use, never used (the seat's Q9 (b); N3)",
                nr_err is None and nr["unit"] == "OLMo-sft" and nr["date_is_clock_of_record"] is True and touched == []
                and "never-read" not in text, nr_err or {k: nr.get(k) for k in ("cause", "date",
                                                                                "date_is_clock_of_record")})
            chk("ganl-p: the pin beside (the seat's Q7) -- the output keeps m's proposal_sha256 (v1.11's) and carries p's "
                "proposal_p_sha256 beside it and the p block: the register, both analyzer blobs and p's package_sha256 "
                "(MAJOR 6), D_p, the disclosure, m's three NOT-RUNs beside m's decisions, and OLMo-sft's at-the-bar "
                "sentence",
                nr is not None and nr["proposal_sha256"] == m_analyze.PROPOSAL_SHA256
                and nr["proposal_p_sha256"] == gcal.PROPOSAL_P_SHA256
                and nr["p"]["analyzers"] == analyzer_blobs()
                and nr["p"]["analyzers"]["valence_core/p"]["package_sha256"] == guard.package_sha256()
                and nr["p"]["d_p"]["problems"] == []
                and [d["unit"] for d in nr["p"]["decisions_beside"]] == [f"PROPOSAL-m {u}" for u in UNITS]
                and nr["p"]["declared_sentences"] == {"OLMo-sft": ["G-CAL-p passed at the bar, 47/64 against 47"]}
                and nr["p"]["disclosure"] == gcal.DISCLOSURE, nr and sorted(nr.get("p", {})))
            # the same run in m's form: m's bytes, no p field -- the two outputs differ by exactly the two added keys
            out_m = base / "pv-m"
            out_m.mkdir()
            st_m, _, finals_m, _ = run_not_run_p("OLMo-sft", recp, out=out_m, ckpt=base / "ck", env=env, p_mode=False)
            m_doc = json.loads(finals_m[0].read_text(encoding="utf-8"))
            chk("ganl-p: in m's form (no substitution, no p field) the output is m's own, and p's output is it with "
                "exactly proposal_p_sha256 and p added (the Clock aside: m's form reads D_O' as the Clock of record)",
                nr is not None and sorted(set(nr) - set(m_doc)) == ["p", "proposal_p_sha256"]
                and {k: v for k, v in nr.items() if k not in ("p", "proposal_p_sha256", "date_is_clock_of_record")}
                == {k: v for k, v in m_doc.items() if k != "date_is_clock_of_record"}
                and m_doc["date_is_clock_of_record"] is False, sorted(set(nr or {}) ^ set(m_doc)))
            # the seeded staging (the seat's Q7; MINOR 13): a re-run on unchanged inputs is refused, write-once, where
            # m's own reports 'identical' (STAGING_NOTE); a VERDICTS output seeded beside is seen by m's exclusivity
            try:
                run_not_run_p("OLMo-sft", recp, out=pv, ckpt=base / "ck", env=env)
                rerun = "ran"
            except (m_analyze.AnlRefusal, analysis.AnalysisRefusal) as e:
                rerun = "refused" if "already written once" in str(e) else f"other: {e}"
            m_again = run_not_run_p("OLMo-sft", recp, out=out_m, ckpt=base / "ck", env=env, p_mode=False)[3]
            # MAJOR 5: p's VERDICTS path on a synthetic OLMo-sft campaign, in p's form and in m's
            fx = _verdicts_fixture(base / "vfix")
            vp, vm = base / "vp", base / "vm"
            ver: dict = {"fixture_error": fx["campaign_error"]}
            try:
                with sentinels():
                    vst, vlines, vfin, _ = run_verdicts_p("OLMo-sft", fx["lock"], fx["decisions"], campaign=fx["campaign"],
                                                          time=fx["time"], qual=fx["qual"], out=vp, ckpt=fx["ckpt"],
                                                          env=fx["env"])
                ver["p"] = {f.name: json.loads(f.read_text(encoding="utf-8")) for f in vfin}
            except (SystemExit, AssertionError) as e:
                ver["p_error"] = f"{type(e).__name__}: {e}"
            try:
                _, _, vfin_m, _ = run_verdicts_p("OLMo-sft", fx["lock"], fx["decisions"], campaign=fx["campaign"],
                                                 time=fx["time"], qual=fx["qual"], out=vm, ckpt=fx["ckpt"],
                                                 env=fx["env"], p_mode=False)
                ver["m"] = {f.name: json.loads(f.read_text(encoding="utf-8")) for f in vfin_m}
            except SystemExit as e:
                ver["m_error"] = f"{type(e).__name__}: {e}"
            pd, md = ver.get("p") or {}, ver.get("m") or {}
            same_but = (sorted(pd) == sorted(md) and bool(pd)
                        and all(sorted(set(pd[n]) - set(md[n])) == ["p", "proposal_p_sha256"]
                                and {k: v for k, v in pd[n].items() if k not in ("p", "proposal_p_sha256")}
                                == md[n] for n in pd))
            diffs = {n: sorted(k for k in set(pd[n]) | set(md.get(n, {})) if pd[n].get(k) != md.get(n, {}).get(k))
                     for n in pd}
            chk("ganl-p: p's VERDICTS path (MAJOR 5) -- m's run_verdicts under entry (3) on a synthetic OLMo-sft "
                "campaign (m's _Camp, the production writer), its checkpoints carrying p's four identity fields as p's "
                "will (N-8: m's reader takes the identity as a dict), with m's root sentinels never used: each output is "
                "m's form on the same inputs with exactly proposal_p_sha256 and the p block added, the p block naming "
                "both analyzers and p's package",
                same_but and touched == [] and all(pd[n]["p"]["analyzers"] == analyzer_blobs() for n in pd),
                {k: v for k, v in ver.items() if k in ("fixture_error", "p_error", "m_error")} | {"diffs": diffs})
            try:
                run_verdicts_p("OLMo-sft", fx["bare_lock"], fx["decisions"], campaign=fx["campaign"], time=fx["time"],
                               qual=fx["qual"], out=base / "vp-bare", ckpt=fx["ckpt"], env=fx["env"])
                bare = "ran"
            except analysis.AnalysisRefusal as e:
                bare = "refused" if "p's package_sha256" in str(e) else f"other: {e}"
            (base / "vx").mkdir()
            for f in vp.glob("*.json"):
                (base / "vx" / f.name).write_bytes(f.read_bytes())
            try:
                run_not_run_p("OLMo-sft", recp, out=base / "vx", ckpt=base / "ck", env=env)
                excl = "ran"
            except m_analyze.AnlRefusal as e:
                excl = "refused" if "exclusive" in str(e) else f"other: {e}"
            chk("ganl-p: a p-form VERDICTS whose lock does not name p's analyzer and package -- as whole lines or "
                "between backticks, never inside a longer run (round 3's NOTE 3) -- is refused (MAJOR 6); the "
                "seeded staging (MINOR 13) -- m's exclusivity sees a p VERDICTS output seeded beside a NOT-RUN; a p re-run "
                "on unchanged inputs is refused write-once where m's own form reports identical (STAGING_NOTE)",
                bare == "refused" and excl == "refused" and rerun == "refused" and m_again == ["identical"],
                (bare, excl, rerun, m_again))
            # N-8 (b): the not-run --v2-closure branch (its canonical checkpoint path m builds from ckpt_dir, else
            # m's CKPT_REL) through p's path, under the sentinels
            rec_v2 = base / "OLMo-dpo_v2-closure-record.json"
            rec_v2.write_text(json.dumps({"schema": m_analyze.NOT_RUN_RECORD_SCHEMA, "unit": "OLMo-dpo",
                                          "cause": "pending-closed-at-v2", "also": [], "date": analysis.D_P,
                                          "detail": "G-ANL-p's case: a v2 closure with no campaign (synthetic)",
                                          "decisions_with_other_outcomes_known": []}), encoding="utf-8")
            (base / "v2c").mkdir()
            try:
                with sentinels():
                    _, _, fin_v2, _ = run_not_run_p("OLMo-dpo", rec_v2, v2_closure=True, campaign_p=Path("none"),
                                                    out=base / "v2c", ckpt=base / "ck-empty", env=env)
                v2c = json.loads(fin_v2[0].read_text(encoding="utf-8"))
                v2c_err = None
            except (SystemExit, AssertionError) as e:
                v2c, v2c_err = None, f"{type(e).__name__}: {e}"
            chk("ganl-p: the not-run --v2-closure branch (campaign 'none') through p's path, the roots p's parameters, "
                "under m's root sentinels, never used (N-8; Q9 (b))",
                v2c_err is None and v2c["unit"] == "OLMo-dpo" and v2c["proposal_p_sha256"] == gcal.PROPOSAL_P_SHA256
                and touched == [], v2c_err or sorted(v2c))
            # the v2 resolution case (the seat's Q9 (c)): OLMo outputs in p's directory, Q-F0's in m's
            recp2 = m_analyze._bt_v2_table_of_record(base)
            for u, st_ in (("OLMo-sft", "PASS"), ("OLMo-dpo", "DEAD")):
                (pv / f"{u}_VERDICTS.json").write_text(json.dumps({"schema": m_analyze.VERDICTS_SCHEMA, "unit": u,
                                                                   "arm": {"state": st_}}))
            (pv / "OLMo-instruct_NOT-RUN.json").write_text(json.dumps({"cause": "pending-closed-at-v2",
                                                                       "reason": "still pending at the v2 posting, with "
                                                                                 "no session"}))
            (pv / "OLMo-sft_NOT-RUN.json").unlink()
            (mv / "Q-F0_VERDICTS.json").write_text(json.dumps({"schema": m_analyze.VERDICTS_SCHEMA, "unit": "Q-F0",
                                                               "arm": {"state": "PASS"}}))
            (f3d / "Q-F3_VERDICTS.json").write_text(json.dumps({"coordinate": {"A1": "PASS", "A2": "PASS", "A3": "NULL"},
                                                                "inputs": {"sentences": {"path": "table-v2.json",
                                                                                         "sha256": _sha(
                                                                                             recp2.read_bytes())}}}))
            tp = base / "t.json"
            tp.write_text(json.dumps({"schema": m_analyze.TUPLE_SCHEMA_V2, "posting": "v2",
                                      "tuple": {"Q-F0": "PASS", "OLMo-sft": "PASS", "OLMo-dpo": "DEAD",
                                                "OLMo-instruct": "NOT-RUN",
                                                "Q-F3": {"A1": "PASS", "A2": "PASS", "A3": "NULL",
                                                         "f2": m_analyze.F2_NOT_REQUIRED, "f2_control": None}},
                                      "reasons": {"OLMo-instruct": "still pending at the v2 posting, with no session"}}))
            try:
                with sentinels():
                    st, lines, finals, _ = run_posting_p(tp, recp2, flag_source=base / "flag-absent.json", out=out,
                                                         m_verdicts=mv, f3_dir=f3d, env=env)
                post = json.loads(finals[0].read_text(encoding="utf-8"))
                post_err = None
            except (SystemExit, AssertionError) as e:
                post, post_err = None, f"{type(e).__name__}: {e}"
            try:
                run_posting_p(tp, recp2, flag_source=base / "flag-absent.json", out=base / "out-x", m_verdicts=base / "mv2",
                              f3_dir=f3d, env=env)
                two_dirs = "ran"
            except analysis.AnalysisRefusal:
                two_dirs = "refused"
            # the posted text's re-run reads its comparator from the seeded staging copy of p's of-record output
            posted = json.loads(recp2.read_text(encoding="utf-8"))
            posted["kind"] = "posted"
            ppt = base / "table-v2-posted.json"
            ppt.write_text(json.dumps(posted), encoding="utf-8")
            rwp = base / "rewrites.json"
            rwp.write_text(json.dumps({"schema": m_analyze.REWRITES_SCHEMA, "posting": "v2", "rows": []}))
            of_rec = out / m_analyze.posting_out_name_v2("of-record")
            of_sha = _sha(of_rec.read_bytes()) if of_rec.is_file() else None
            try:
                run_posting_p(tp, ppt, flag_source=base / "flag-absent.json", rewrites=rwp, out=out, m_verdicts=mv,
                              f3_dir=f3d, env=env)
                posted_run = ("ran", [])
            except m_analyze.AnlPostingFail as e:
                posted_run = ("fail", list(e.lines))
            except SystemExit as e:
                posted_run = (f"other: {e}", [])
            cmp_lines = [ln for ln in posted_run[1] if of_sha and of_sha[:16] in ln]
            chk("ganl-p: the seeded comparator (MINOR 13) -- the v2 posted text's re-run reads the comparator from the "
                "staging copy of p's of-record output: its FAIL (a posted copy still enumerates rows) names that file's "
                "sha256, and no printed line names the staging directory",
                posted_run[0] == "fail" and bool(cmp_lines)
                and not any(analysis.STAGING_PREFIX in ln for ln in posted_run[1]),
                (posted_run[0], len(cmp_lines), [ln[:120] for ln in posted_run[1][:2]]))
            (mv / "OLMo-dpo_VERDICTS.json").write_text((pv / "OLMo-dpo_VERDICTS.json").read_text())
            (pv / "OLMo-dpo_VERDICTS.json").unlink()
            try:
                run_posting_p(tp, recp2, flag_source=base / "flag-absent.json", out=base / "out2", m_verdicts=mv,
                              f3_dir=f3d, env=env)
                moved = "ran"
            except SystemExit as e:
                moved = "refused" if "OLMo-dpo" in str(e) else f"other: {e}"
            res_ = (post or {}).get("p", {}).get("resolution", {})
            chk("ganl-p: the v2 resolution (the seat's Q9 (c)) -- the posting reads the OLMo coordinates from p's directory "
                "and Q-F0's from m's, Q-F3's from mf3's parameter, under the sentinels; an OLMo output only in m's "
                "directory is refused; a posting m directory other than the bound one is refused; the output carries "
                "proposal_p_sha256, the resolution (no machine path: MINOR 11) and m's three NOT-RUN outputs' sha256s",
                post_err is None and moved == "refused" and two_dirs == "refused" and touched == []
                and post["proposal_p_sha256"] == gcal.PROPOSAL_P_SHA256
                and set(res_) == set(UNITS) | {"Q-F0", "Q-F3"} and set(res_.values()) == {"(a test directory)"}
                and len(post["p"]["decisions_beside"]) == 3, post_err or (moved, two_dirs, res_))
        finally:
            analysis.bind(m_analyze)                # the production binding again (N7)
    rq = _regression_qf0()
    mq = rq["m"]
    chk("ganl-p: the regression -- Q-F0's VERDICTS and secondary outputs through p's path (run_verdicts_p, m's form) on "
        "the G-ANL-F3 battery's identity binding, byte for byte, with m's own regression's checks: PIN-29's seven pins "
        "by blob, LOCK-m-F0 naming the identity of record, the preprint of record served by its blob (MAJOR 5)",
        rq["error"] is None and len(rq["outputs"]) == 2 and all(v["identical"] for v in rq["outputs"].values())
        and mq["error"] is None and len(mq["pins"] or {}) == 7 and all((mq["pins"] or {}).values())
        and (mq["identity"] or {}).get("lock_names_all_three") is True
        and (mq["identity"] or {}).get("analyzer_sha256") == m_analyze.RECORD_ANALYZER_SHA256
        and (mq["preprint"] or {}).get("blob_sha256") == (mq["preprint"] or {}).get("table_sha256")
        and rq["m_outputs_identical"] is True, {"error": rq["error"], "m_error": mq["error"]})
    rn = _regression_not_run()
    chk("ganl-p: the regression -- m's three OLMo NOT-RUN outputs (0f35954), through p's staged path in m's form on the "
        "bindings they were written under (e0b4f2c's analyzer, its package and closure, each pinned in full; N4), byte "
        "for byte", rn["error"] is None and len(rn["outputs"]) == 3 and all(v["identical"] for v in rn["outputs"].values()),
        rn)
    snap1 = _data_p_snapshot()
    chk("ganl-p: data/p is untouched by the battery -- every file's sha256 before and after (N11)", snap0 == snap1,
        sorted(set(snap0.items()) ^ set(snap1.items()))[:4])
    _BATTERY_EXTRA.clear()
    _BATTERY_EXTRA.update({**extra, "regression_qf0": rq, "regression_not_run": rn})


_BATTERY_EXTRA: dict = {}


def run_battery() -> dict:
    results: list[tuple[bool, str]] = []

    def chk(name, ok, got="", *rest) -> None:
        results.append((bool(ok), name))
        tail = "" if ok else f" {json.dumps(got, default=str)[:400]}"
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}{tail}", flush=True)
    analysis.bind(m_analyze)
    try:
        _selftest(chk)
    except (Exception, SystemExit) as e:                    # noqa: BLE001
        chk("ganl-p: the battery raised", False, f"{type(e).__name__}: {e}")
    n_ok = sum(1 for ok, _ in results if ok)
    print(f"  {n_ok}/{len(results)} G-ANL-p checks pass", flush=True)
    return {"ok": n_ok == len(results), "checks_pass": n_ok, "checks_total": len(results),
            "checks": [n for _, n in results], **copy.deepcopy(_BATTERY_EXTRA)}


def run_ganl(out: str | None) -> int:
    canonical = out is None
    probs = binding_problems(canonical=canonical)
    if probs:
        print(f"REFUSED: G-ANL-p: {probs[:4]}", file=sys.stderr, flush=True)
        return 2
    dest = REPO / GANL_REL if canonical else guard.refuse_test_out(out) / Path(GANL_REL).name
    blobs0, code0 = analyzer_blobs(), code_shas()          # m-4: the code of record, taken before the battery
    res = run_battery()
    if (analyzer_blobs(), code_shas()) != (blobs0, code0) or (canonical and binding_problems(canonical=True)):
        print("STOP: G-ANL-p: the code moved during the battery (or is no longer committed as it was) -- the battery "
              "did not run the code it would record; nothing written", file=sys.stderr, flush=True)
        return 4
    art = {"schema": GANL_SCHEMA, "stage": "G-ANL-p", "verdict": "PASS" if res["ok"] else "FAIL",
           "spec": "p §4.4; the seat's answer of 2026-11-08 (de729c4), Q8, Q9",
           "proposal_sha256": m_analyze.PROPOSAL_SHA256, "proposal_p_sha256": gcal.PROPOSAL_P_SHA256,
           "analyzers": blobs0, "code": code0, "register": register_rows(),
           "d_p": {"date": analysis.D_P, "problems": analysis.d_p_problems()},
           "battery": {k: res[k] for k in ("ok", "checks_pass", "checks_total", "checks")},
           "m_battery": res.get("m_battery"), "regression_qf0": res.get("regression_qf0"),
           "regression_not_run": res.get("regression_not_run"), "disclosure": gcal.DISCLOSURE}
    if not res["ok"]:
        print("STOP: G-ANL-p's battery did not pass; nothing written", file=sys.stderr, flush=True)
        return 4
    try:
        how = guard.write_once_bytes(dest, m_resume.json_text(art, indent=1).encode("utf-8"), what="G-ANL-p's artifact")
    except guard.GuardStop as e:
        print(f"REFUSED: {e}", file=sys.stderr, flush=True)
        return 2
    print(f"G-ANL-p: PASS: {m_stages._rel(dest, REPO)} ({how}; sha256 {_sha(dest.read_bytes())})"
          + ("" if canonical else " -- an --out run, never of record"), flush=True)
    return 0


def main(argv: list[str] | None = None) -> int:
    shown = sys.argv if argv is None else [sys.argv[0]] + list(argv)
    print("INVOCATION: " + " ".join([sys.executable] + shown), flush=True)
    ap = argparse.ArgumentParser(description="PROPOSAL-p's analyzer (G-ANL-p; p's verdicts, not-run and v2 posting "
                                             "through m's analyzer under register entry (3))")
    ap.add_argument("--selftest", action="store_true", help="G-ANL-p's battery (model-free), no artifact")
    sub = ap.add_subparsers(dest="cmd")
    g = sub.add_parser("ganl", help="G-ANL-p's battery, then data/p/gates/G-ANL-p.json (write-once)")
    g.add_argument("--out", default=None, help="a test directory (never of record; never inside the repository)")
    n = sub.add_parser("not-run", help="a p unit's Clock / dose NOT-RUN")
    n.add_argument("--unit", required=True)
    n.add_argument("--record", required=True)
    for a in ("time", "qual", "campaign"):
        n.add_argument(f"--{a}", default=None)
    n.add_argument("--v2-closure", action="store_true")
    v = sub.add_parser("verdicts", help="a p unit's VERDICTS")
    for a in ("unit", "lock", "decisions"):
        v.add_argument(f"--{a}", required=True)
    for a in ("campaign", "time", "qual", "adjudication", "pi-stop"):
        v.add_argument(f"--{a}", default=None)
    p = sub.add_parser("posting", help="the v2 posting (p §5.2)")
    p.add_argument("--posting", required=True, choices=["v2"])
    p.add_argument("--tuple", required=True)
    p.add_argument("--sentences", required=True)
    for a in ("rewrites", "flag-source"):
        p.add_argument(f"--{a}", default=None)
    a = ap.parse_args(argv)
    if a.selftest:
        return 0 if run_battery()["ok"] else 1
    if a.cmd is None:
        ap.print_usage(sys.stderr)
        return 2
    if a.cmd == "ganl":
        return run_ganl(a.out)
    probs = binding_problems(canonical=True)
    unit = getattr(a, "unit", None)
    if unit is not None and unit not in UNITS:
        probs.append(f"p's units are {UNITS}; Q-F0's and Q-F3's are m's analyzer's")
    if probs:
        print(f"REFUSED: {probs}", file=sys.stderr, flush=True)
        return 2
    analysis.bind(m_analyze)
    cli = m_analyze._cli_path
    try:
        if a.cmd == "not-run":
            camp = Path("none") if a.campaign == "none" else cli(a.campaign)
            st, lines, finals, hows = run_not_run_p(a.unit, cli(a.record, True), cli(a.time), cli(a.qual),
                                                    v2_closure=a.v2_closure, campaign_p=camp)
        elif a.cmd == "verdicts":
            st, lines, finals, hows = run_verdicts_p(a.unit, cli(a.lock, True), cli(a.decisions, True),
                                                     campaign=cli(a.campaign), time=cli(a.time), qual=cli(a.qual),
                                                     adjudication=cli(a.adjudication), pi_stop=cli(a.pi_stop))
        else:
            st, lines, finals, hows = run_posting_p(cli(a.tuple, True), cli(a.sentences, True),
                                                    flag_source=cli(a.flag_source), rewrites=cli(a.rewrites))
    except m_analyze.AnlPostingFail as e:
        for ln in e.lines:
            print(ln, flush=True)
        return m_analyze._exit_of(e)
    except P_REFUSALS as e:
        print(str(e), file=sys.stderr, flush=True)
        return 2
    except SystemExit as e:
        print(str(e.code if not isinstance(e, (m_analyze.AnlRefusal, m_analyze.AnlStop)) else e), file=sys.stderr,
              flush=True)
        return m_analyze._exit_of(e)
    for ln in lines:
        print(ln, flush=True)
    for f, h in zip(finals, hows):
        print(f"P-OUTPUT {m_stages._rel(f, REPO)} ({h}; sha256 {_sha(f.read_bytes())})", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
