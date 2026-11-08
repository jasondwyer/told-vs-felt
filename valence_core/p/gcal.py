"""G-CAL-p -- completability at the frame-word dose, per checkpoint, once (p v0.2 §3; ans2 Q2, Q3 (b), (c)).

PROCEDURE (p §3.1): m:176's, pinned, with p's renders. 128 generations per checkpoint -- the clean pool (64) and the
corrupted pool (64) under ``SESSION_BANNER + "Task: {task}\\nResponse:"`` with no round header; uncached, injections
none, newline stop through §2.2's proxy, the checkpoint's ban list, ``STOP_CAP`` 60, TEMP 0.7, rule 28(d)(a)'s
boundary assertion before every generation; seeds ``crc32("m-cal|{pool}|{i}|{seed}") % 2**31`` unchanged.

WHAT IS m's, BY IMPORT: the key set and seeds (``key_set``), the task of a key (``_task_of``), the segment form
(``SEGMENT_FORM``), the startup (``_startup_olmo``: insulation, base and cross-checkpoint refusal, the 8192 window,
b3's ban list, the weights path, TEMP and cap, the tokenizer probe), f0's grader (``grade``) and its honesty asserts
(``_grader_honesty``), the identity (``_identity_olmo``), the gate line (``gate_line``), condition (4)
(``condition_4``), the weights of record (``weights_of_record``), the boundary assertion (``scaffold.assert_boundary``)
and the fields of m's artifact schema (``completability_artifact``, a pure function of the checkpoint that reads no
renders). WHAT IS p's OWN (ans2 Q3 (b); p §3.1 "the artifact builder is p's"): the precheck, the loop, the
checkpoint (``p-gcal-checkpoint-v1``: m's checkpoint keys plus the proxy's ``cuts`` and a ``stop`` field, every m
load check mirrored), the hair trigger, the link-safe writes, and the artifact (m's schema with ``proposal_p_sha256`` and the ``p`` block; m's gate-line record stored
under p's field names, ``gate_record``). m's ``run_completability`` is not called: its precheck reads a model-free
artifact on m's renders and writes m's roots, and its identity carries no p field. So the generation call -- inline
in m's loop, not importable alone -- is restated here, and the self-test pins it to m's: an AST comparison with
``run_completability``'s call, segment and record literal, and a dynamic check of every call p makes (PIN P21) --
the register's pinned-restatement exception, entry (5), admitted by the seat's ruling of 2026-11-07 (``38f9974``),
entry (4) struck.
Files: ``data/p/gates/G-CAL_completability_olmo-{ckpt}.json`` and ``data/p/ckpt/G-CAL_olmo-{ckpt}.json``.

ORDER. Every refusal of p's own that needs no adapter runs before the load: the unit, the seams, the paths (no link on
the way), the proposal, an existing checkpoint without ``--resume`` or an artifact without its checkpoint, the
renders, the reference artifact, the seat's read of record, PROPOSAL-m committed at its sha256 (F-p8), the disclosure
against the ruling's bytes (F-p3), the generation call's pin (P21), §3.2's conditions (1)-(3) (register entry (1)'s
site), the weights of record and, on the box, the pod id, the gate line and the code of record committed (m's package
entire, its hash being the identity's); then the key set, f0's honesty asserts and, on a ``--resume``, the
checkpoint's own validity (schema, no STOP recorded, every record keyed, typed, graded and line-break free, the cuts),
every identity field the adapter does not give, and the pod change. After the load and before any generation: m's
startup (its adapter checks, and with them two model-free asserts of m's own -- insulation, TEMP and cap), the
provenance and the comparison of the two identity fields the loaded adapter gives (the backend identifier, the ban
ids).

PINs (Code, declared at the p BUILD; the design raw's register):
  - Identity (the seat's ruling of 2026-11-07, F-p8: in every p artifact ``proposal_sha256`` is m's, the rules the
    output is computed under, and ``proposal_p_sha256`` p's, the document the stage runs under): ``_identity_olmo``'s
    keys as m writes them -- ``proposal_sha256`` PROPOSAL-m v1.11's (checked committed at its sha256), ``renders_sha256``
    p's renders by m's convention (p §1.2, ans2 Q3 (c)),
    ``package_sha256`` m's package (the code that runs) -- plus ``proposal`` ("PROPOSAL-p"), ``proposal_p_sha256``,
    ``p_stage``, ``p_package_sha256``, ``renders_sha256_p``, ``proxy``, ``olmo_hf_sha256`` and ``driver_sha256`` (a
    resume never splices two adapters or drivers). m's strings stay as m writes them (``stage`` "G-CAL-OLMo", the
    artifact's ``procedure`` and ``on_fail``); p's stage name, its procedure difference (the proxy) and its failure
    consequence are in the ``p`` block, ``proposal_p_sha256`` at the top level.
  - The strict grade: p §3.1's "a hit iff the first word of the normalized text is a gold variant", read for a gold
    variant that f0's ``normalize`` turns into several words (``twenty-four`` -> ``twenty four``) as the text's
    leading words being that variant's words; for a one-word variant it is the first word, as written.
  - The clean-pool identity compares, per clean key, the fields seed, task, text, n_tok, cap_hit, stop_reason and hit
    with G-CAL-OLMo's committed gate artifact (``data/m/gates/G-CAL_completability_olmo-{ckpt}.json``, read from its
    blob at HEAD), and records the two identities' generation-path fields side by side.
  - Every STOP in the loop -- the hair trigger, rule 28(d)(a)'s boundary, the proxy's, the insulation guard's -- is
    recorded in the checkpoint's ``stop`` field with its key before the stage exits, no record is appended for that
    key, and a stopped checkpoint is never resumed.
  - Seams (``startup``, ``wrap``) are refused on a canonical run.
  - A non-stub run requires p's package files, m's whole package (every ``valence_core/m/*.py``, its hash being the
    identity's), ``olmo_hf.py`` and the driver committed at HEAD with identical working-tree bytes (rule 27); the
    licence's values are recorded in the artifact (``licence_at_run``).
  - The PROVENANCE line prints m's fields and the pod id. Conditions (1)-(2) of §3.2 (structural, per item) and (3)
    (the seat's read of record, ans2 §0) are recorded in the artifact's ``p`` block.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from ..m import corr
from ..m import gcal as m_gcal
from ..m import guard as m_guard
from ..m import keys as m_keys
from ..m import resume as m_resume
from ..m import runner_olmo as m_ro
from ..m import scaffold as m_sc
from ..m import stages as m_stages
from ..session_e2a import SESSION_BANNER
from . import corrupt, guard, report
from . import proxy as p_proxy

REPO = Path(__file__).resolve().parents[2]
GATES_DIR = REPO / "data" / "p" / "gates"
CKPT_DIR = REPO / "data" / "p" / "ckpt"
REF_REL = "data/m/gates/G-CAL_completability_olmo-{ckpt}.json"
STAGE = "G-CAL-p"
PROPOSAL_P_REL = "PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md"
PROPOSAL_P_SHA256 = "42f2977b941bc016d3155ba9e34828f1b050121d9f18a9e3307e3f7023cf3b32"
CKPT_SCHEMA = "p-gcal-checkpoint-v1"
CKPT_KEYS = ("cuts", "identity", "n_writes", "provenance", "records", "schema", "stop")
RECORD_KEYS = m_gcal.RECORD_KEYS
P_IDENTITY = ("proposal", "proposal_p_sha256", "p_stage", "p_package_sha256", "renders_sha256_p", "proxy",
              "olmo_hf_sha256", "driver_sha256")
CLEAN_FIELDS = ("seed", "task", "text", "n_tok", "cap_hit", "stop_reason", "hit")
#: The identity fields only the loaded adapter gives; every other field is compared before the load on a --resume.
ADAPTER_FIELDS = ("backend_identifier", "ban_ids_sha16")
PATH_FIELDS = ("backend_identifier", "banner_sha256", "ban_sha256", "ban_ids_sha16", "weights_repo",
               "weights_revision", "weights_sha256", "temp", "stop_cap", "path", "pool_sha16", "segment_form",
               "key_set_sha256")
M_COVARIATES = {"sft": "+5/16", "dpo": "+17/64", "instruct": "+17/64"}
BINDING_BARS = {"sft": "47/64", "dpo": "46/64", "instruct": "45/64"}
#: The artifacts' disclosure sentence, verbatim from the seat's ruling of 2026-11-07 (F-p3, §1; ``38f9974``).
DISCLOSURE = ("pre-registered on 2026-11-07 (PROPOSAL-p v0.2, `18b0111`; v0.1 routed 2026-11-06), after the shared dose "
              "of PROPOSAL-m failed completability on this lineage at G-CAL-OLMo on 2026-11-06; the corruption rule "
              "changed once, from the gate's read, before any session ran.")
#: The seat's ruling of 2026-11-07 (committed at 38f9974): DISCLOSURE is its §1 sentence, asserted against these bytes.
RULING_REL = "results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md"
RULING_SHA256 = "e3de1c0316c95701e627fb89596c50b0cf0596f31c352ed6ee9a8daca5d1e006"
#: PROPOSAL-m v1.11, the rules p's outputs are computed under: ``proposal_sha256`` in every p artifact (F-p8).
M_PROPOSAL_REL = m_stages.PROPOSAL_REL
M_PROPOSAL_SHA256 = "42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b"
#: The diagnostic fields of the cut log and of a STOP record (F-p10), never stored text.
DIAGNOSTIC_FIELDS = p_proxy.DIAGNOSTIC_FIELDS


class GcalPRefusal(SystemExit):
    """A refusal, decided before the generation it would govern (the driver's exit 2); the artifact's write
    refusal comes after the generations, before anything is written over."""


class GcalPStop(SystemExit):
    """A delivery-geometry assertion, a guard or the hair trigger (the driver's exit 4)."""


def unit_ckpt(unit: str) -> str:
    try:
        ck = m_gcal.unit_ckpt(unit)
    except SystemExit as e:
        raise GcalPRefusal(f"G-CAL-p REFUSED: {e}") from None
    if ck is None:
        raise GcalPRefusal("G-CAL-p REFUSED: Q-F0 is not a p unit; p's units are OLMo-{sft,dpo,instruct}")
    return ck


def stage_label(unit: str) -> str:
    return f"{STAGE}-{unit_ckpt(unit)}"


def paths(unit: str, out_dir=None, *, stub: bool) -> dict[str, Path]:
    """The artifact and the checkpoint, absolute and NOT resolved (a link is refused, never followed): canonical
    under data/p, a stub run's under its scratch directory (``guard.refuse_test_out``: never inside the repository)."""
    art, ckn = m_gcal._names(unit)
    if out_dir is None or str(out_dir).strip() == "":
        if stub:
            raise GcalPRefusal("G-CAL-p REFUSED: a stub run needs a scratch out directory")
        out, ck, top = Path(os.path.abspath(GATES_DIR / art)), Path(os.path.abspath(CKPT_DIR / ckn)), GATES_DIR.parent
    else:
        if not stub:
            raise GcalPRefusal("G-CAL-p REFUSED: a non-stub run writes data/p/gates and data/p/ckpt only (ledger 27)")
        try:
            d = guard.refuse_test_out(out_dir)
        except guard.GuardStop as e:
            raise GcalPRefusal(f"G-CAL-p REFUSED: {e}") from None
        out, ck, top = d / art, d / "ckpt" / ckn, d
    lp = guard.no_link_problems(out, top) + guard.no_link_problems(ck, top)
    for p in (out, ck):
        tmp = p.with_name(p.name + ".tmp")
        if tmp.is_symlink() or (tmp.exists() and not tmp.is_file()):
            lp.append(f"{tmp} is a symlink or a non-file")
        if p.exists() and not p.is_file():
            lp.append(f"{p} is not a regular file")
    if lp:
        raise GcalPRefusal(f"G-CAL-p REFUSED: a link on the artifact's or the checkpoint's path ({lp}); a record is "
                           f"never written through a link")
    return {"out": out, "ckpt": ck}


def committed_problems() -> list[str]:
    """p's package files, m's whole package (every valence_core/m/*.py, its hash being the identity's), olmo_hf.py and
    the driver, each committed at HEAD with identical working-tree bytes."""
    rels = [f.relative_to(REPO).as_posix() for f in sorted(guard.PACKAGE_DIR.glob("*.py"))]
    rels += [f.relative_to(REPO).as_posix() for f in sorted(guard.M_PACKAGE_DIR.glob("*.py"))]  # m's package hash
    rels += [guard.OLMO_HF_REL, guard.DRIVER_REL]
    probs = []
    for rel in rels:
        cp, _ = m_stages._committed(rel)
        probs += [f"{rel}: {x}" for x in cp]
    return probs


def reference(ckpt: str) -> tuple[list[str], dict | None, str | None]:
    """(problems, G-CAL-OLMo's committed gate artifact, its sha256)."""
    rel = REF_REL.format(ckpt=ckpt)
    cp, data = m_stages._committed(rel)
    if cp or data is None:
        return [f"{rel}: {x}" for x in (cp or ["unreadable"])], None, None
    try:
        art = json.loads(data.decode("utf-8"))
        assert art["schema"] == m_gcal.ART_SCHEMA and art["unit"] == f"OLMo-{ckpt}" and len(art["records"]) == 128
    except (ValueError, UnicodeDecodeError, KeyError, TypeError, AssertionError):
        return [f"{rel}: not G-CAL-OLMo-{ckpt}'s completability artifact"], None, None
    return [], art, hashlib.sha256(data).hexdigest()


def seat_read_problems() -> list[str]:
    cp, data = m_stages._committed(corrupt.ANSWERS_REL)
    if cp or data is None:
        return [f"{corrupt.ANSWERS_REL}: {x}" for x in (cp or ["unreadable"])]
    if hashlib.sha256(data).hexdigest() != corrupt.ANSWERS_SHA256 or \
            corrupt.SEAT_READ_LINE not in data.decode("utf-8", "replace"):
        return [f"{corrupt.ANSWERS_REL} is not the seat's answers of record carrying the read of record"]
    return []


def precheck(unit: str, *, stub: bool, out_dir=None, resume: bool = False) -> dict:
    """Every refusal that needs no adapter and no checkpoint read; GcalPRefusal on the first set of problems."""
    ck = unit_ckpt(unit)
    pa = paths(unit, out_dir, stub=stub)
    try:
        got = hashlib.sha256((REPO / PROPOSAL_P_REL).read_bytes()).hexdigest()
    except OSError:
        got = None
    if got != PROPOSAL_P_SHA256:
        raise GcalPRefusal(f"G-CAL-p REFUSED: {PROPOSAL_P_REL} hashes to {str(got)[:16]}, not p v0.2's "
                           f"{PROPOSAL_P_SHA256[:16]}")
    ck_on_disk = pa["ckpt"].exists()
    if ck_on_disk and not resume:
        raise GcalPRefusal(f"G-CAL-p REFUSED: CHECKPOINT EXISTS at {pa['ckpt']}; pass --resume to continue it "
                           f"(skip-only); never overwritten")
    if not ck_on_disk and pa["out"].exists():
        raise GcalPRefusal(f"G-CAL-p REFUSED: COMPLETABILITY ARTIFACT EXISTS at {pa['out']} with no checkpoint; never "
                           f"overwritten")
    rp0 = corrupt.renders_problems()                 # a register or keys STOP propagates (the driver's exit 4)
    if rp0:
        raise GcalPStop(f"G-CAL-p STOP: the renders of record do not reproduce: {rp0} (a pinned figure, m's "
                        f"G-CAL taxonomy: a STOP, not a refusal)")
    probs = [f"the generation call (P21): {p}" for p in _call_pin_problems()]
    rp, ref, ref_sha = reference(ck)
    probs += [f"reference: {p}" for p in rp]
    probs += [f"seat's read: {p}" for p in seat_read_problems()]
    mcp, mdata = m_stages._committed(M_PROPOSAL_REL)
    if mcp or mdata is None:
        probs.append(f"{M_PROPOSAL_REL} (the identity's proposal_sha256, F-p8): {mcp or ['unreadable']}")
    elif hashlib.sha256(mdata).hexdigest() != M_PROPOSAL_SHA256:
        probs.append(f"{M_PROPOSAL_REL} hashes to {hashlib.sha256(mdata).hexdigest()[:16]}, not PROPOSAL-m v1.11's "
                     f"{M_PROPOSAL_SHA256[:16]} (the identity's proposal_sha256, F-p8)")
    probs += [f"disclosure (F-p3): {p}" for p in disclosure_problems()]
    wp, weights = m_gcal.weights_of_record(ck)
    probs += [f"weights of record: {p}" for p in wp]
    gate = None
    if not stub:
        if m_resume.pod_id() is None:
            probs.append(f"POD ID ABSENT: {stage_label(unit)} runs on the box only with its pod instance id "
                         f"(${m_resume.POD_ENV}), as every OLMo stage")
        gate, gp = m_gcal.gate_line(PROPOSAL_P_REL, PROPOSAL_P_SHA256, stage=stage_label(unit))
        probs += [f"gate line: {p}" for p in gp]
        probs += [f"committed: {p}" for p in committed_problems()]
    if probs:
        raise GcalPRefusal(f"G-CAL-p REFUSED: {probs}")
    pool = corr.load_pool()
    return {"unit": unit, "ckpt": ck, "paths": pa, "pool": pool, "renders": list(corrupt.RENDERS_OF_RECORD),
            "weights": weights, "gate": gate, "reference": ref, "reference_sha256": ref_sha,
            "conditions": conditions(pool)}                # register entry (1)'s site: before any model load (P1)


def disclosure_problems() -> list[str]:
    """[] iff DISCLOSURE is the ruling's §1 sentence, read from the ruling's committed bytes (F-p3)."""
    cp, data = m_stages._committed(RULING_REL)
    if cp or data is None or hashlib.sha256(data).hexdigest() != RULING_SHA256:
        return [f"{RULING_REL} is not the seat's ruling committed at its sha256 {RULING_SHA256[:16]} {cp or ''}".rstrip()]
    m = re.search(r"The artifacts' disclosure sentence reads: \*(.+?)\* p §5\.4", data.decode("utf-8"), flags=re.S)
    if m is None:
        return [f"{RULING_REL}: its §1 sentence was not found"]
    return [] if " ".join(m.group(1).split()) == DISCLOSURE else ["DISCLOSURE is not the ruling's §1 sentence"]


GATE_RENAMES = {"proposal_file": "proposal_p_file", "proposal_sha256": "proposal_p_sha256"}


def gate_record(gate: Mapping[str, Any] | None) -> dict | None:
    """m's gate-line record as p stores it (PIN, declared at the rulings' commit): its two proposal fields -- the file
    and the sha256 the gate line checks, p's -- under p's names (``proposal_p_file``, ``proposal_p_sha256``), so that
    ``proposal_sha256`` and ``proposal_file`` keep m's meaning alone in every p artifact (F-p8; m's licence pairs the
    two). The ``line`` text is m's, unchanged."""
    if gate is None:
        return None
    return {GATE_RENAMES.get(k, k): v for k, v in gate.items()}


def identity(*, ks, unit: str, backend_id: str, pool, ban_ids, weights) -> dict:
    ident = m_gcal._identity_olmo(ks=ks, unit=unit, proposal_sha256=M_PROPOSAL_SHA256,
                                  renders_sha256=corrupt.RENDERS_SHA256_M, backend_id=backend_id, pool=pool,
                                  ban_ids=ban_ids, weights=weights)
    ident.update({"proposal": "PROPOSAL-p", "proposal_p_sha256": PROPOSAL_P_SHA256, "p_stage": STAGE,
                  "p_package_sha256": guard.package_sha256(), "renders_sha256_p": corrupt.RENDERS_SHA256_P,
                  "proxy": p_proxy.PROXY_ID, "olmo_hf_sha256": guard.olmo_hf_sha256(),
                  "driver_sha256": guard.driver_sha256()})
    return ident


def fresh_checkpoint(ident: dict) -> dict:
    return {"schema": CKPT_SCHEMA, "identity": ident, "records": [], "provenance": [], "n_writes": 0, "cuts": [],
            "stop": None}


def read_checkpoint(path: Path, resume: bool, ks, pool, renders) -> dict | None:
    """The checkpoint on disk, validated without the identity (which needs the loaded adapter), or None: m's
    ``_load_ckpt`` checks on p's schema, plus p's (no STOP recorded; no stored line break; the cuts)."""
    if not path.exists():
        return None
    if not resume:
        raise GcalPRefusal(f"G-CAL-p REFUSED: CHECKPOINT EXISTS at {path}; pass --resume")
    try:
        ck = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        raise GcalPRefusal(f"G-CAL-p REFUSED: checkpoint {path} unreadable") from None
    if not isinstance(ck, dict) or tuple(sorted(ck)) != CKPT_KEYS or ck.get("schema") != CKPT_SCHEMA:
        raise GcalPRefusal(f"G-CAL-p REFUSED: {path} is not a {CKPT_SCHEMA} checkpoint")
    if ck["stop"] is not None:
        raise GcalPRefusal(f"G-CAL-p REFUSED: {path} records a STOP ({ck['stop']}); a stopped stage is never resumed")
    if not isinstance(ck["identity"], dict):
        raise GcalPRefusal(f"G-CAL-p REFUSED: {path}'s identity is malformed")
    recs = ck["records"]
    if not isinstance(recs, list) or len(recs) > len(ks):
        raise GcalPRefusal(f"G-CAL-p REFUSED: {path} holds a malformed record list")
    for j, r in enumerate(recs):
        k = ks[j]
        if not isinstance(r, dict) or tuple(sorted(r)) != tuple(sorted(RECORD_KEYS)):
            raise GcalPRefusal(f"G-CAL-p REFUSED: record {j} of {path} is malformed")
        want = {"pool": k["pool"], "i": k["i"], "seed_index": k["s"], "seed": k["seed"],
                "task": m_gcal._task_of(k, pool, renders)}
        if any(r[f] != v for f, v in want.items()):
            raise GcalPRefusal(f"G-CAL-p REFUSED: record {j} of {path} is not key {j} of the key set")
        if type(r["text"]) is not str or type(r["hit"]) is not bool or type(r["n_tok"]) is not int \
                or type(r["cap_hit"]) is not bool or type(r["stop_reason"]) is not str:
            raise GcalPRefusal(f"G-CAL-p REFUSED: record {j} of {path} has a mistyped field")
        if r["hit"] is not m_gcal.grade(r["text"], pool[k["i"]]["gold"]):
            raise GcalPRefusal(f"G-CAL-p REFUSED: record {j} of {path} is not graded as f0's grader grades its text")
        if report.line_break_in_stored_text(r["text"]):
            raise GcalPRefusal(f"G-CAL-p REFUSED: record {j} of {path} stores a line break (p §2.2)")
    cuts = ck["cuts"]
    if not isinstance(cuts, list) or not isinstance(ck["provenance"], list) or any(
            not isinstance(c, dict) or type(c.get("record")) is not int or not 0 <= c["record"] < len(recs)
            or c.get("stored_text") != recs[c["record"]]["text"] for c in cuts):
        raise GcalPRefusal(f"G-CAL-p REFUSED: {path}'s cuts or provenance are malformed")
    return ck


def identity_problems(ck: Mapping[str, Any], ident: Mapping[str, Any]) -> list[str]:
    rid = ck["identity"]
    return sorted(k for k in set(rid) | set(ident) if rid.get(k) != ident.get(k))


def _write(path: Path, ck: dict) -> None:
    ck["n_writes"] += 1
    try:
        guard.atomic_write_nofollow(path, m_resume.json_text(ck).encode("utf-8"))
    except guard.GuardStop as e:
        raise GcalPStop(f"G-CAL-p STOP: {e}") from None


def strict_hit(text: str, gold: Sequence[str]) -> bool:
    words = m_gcal.normalize(text).split()
    return any(v and words[:len(v)] == v for v in (m_gcal.normalize(g).split() for g in gold))


def strict_grade(records: Sequence[Mapping[str, Any]], pool) -> dict:
    """p §3.1's second grade, reported beside and deciding nothing."""
    acc = {}
    for p in m_keys.CAL_POOLS:
        rs = [r for r in records if r["pool"] == p]
        acc[p] = {"hits": sum(1 for r in rs if strict_hit(r["text"], pool[r["i"]]["gold"])), "n": len(rs)}
    lax = [f"{r['pool']} i={r['i']} s={r['seed_index']}" for r in records
           if r["hit"] and not strict_hit(r["text"], pool[r["i"]]["gold"])]
    return {"rule": "a hit iff the first word of the normalized text is a gold variant (p §3.1); a variant that "
                    "normalizes to several words, as the text's leading words (Code's PIN)",
            "decides": "nothing (reported beside the grade of record)", "accuracy": acc,
            "graded_hit_strict_miss": lax}


def clean_identity(records: Sequence[Mapping[str, Any]], ident: Mapping[str, Any], ref: Mapping[str, Any],
                   ref_sha: str, ckpt: str) -> dict:
    """The clean pool's 64 generations against G-CAL-OLMo's of record (p §3.1): a flag, not a bar."""
    by = {(r["i"], r["seed_index"]): r for r in ref["records"] if r["pool"] == "CORR_clean"}
    clean = [r for r in records if r["pool"] == "CORR_clean"]
    miss = object()
    diff = [f"i={r['i']} s={r['seed_index']}" for r in clean
            if any(r[f] != by.get((r["i"], r["seed_index"]), {}).get(f, miss) for f in CLEAN_FIELDS)]
    path = {f: {"G-CAL-OLMo": ref["identity"].get(f), "G-CAL-p": ident.get(f),
                "equal": ref["identity"].get(f) == ident.get(f)} for f in PATH_FIELDS}
    return {"reference": {"path": REF_REL.format(ckpt=ckpt), "sha256": ref_sha}, "fields": list(CLEAN_FIELDS),
            "n": len(clean), "identical": len(clean) - len(diff), "differing": diff, "generation_path": path,
            "rule": "a non-identity on any clean generation is a flag to the seat (adjudication), not a bar (p §3.1)"}


def licence_at_run() -> dict:
    return {"p_package_sha256": guard.package_sha256(), "m_modules_sha256": guard.m_module_sha256s(),
            "olmo_hf_sha256": guard.olmo_hf_sha256(), "driver_sha256": guard.driver_sha256()}


def conditions(pool) -> dict:
    items = corrupt.conditions_1_2(pool)
    return {"rule": "p §3.2: (1) every item >= 3 changed positions and (2) k <= floor(n/2) -- structural, from §1.2, "
                    "reported; (3) the seat's read of record (§1.3)",
            "items": items, "c1": all(x["c1_at_least_3_changed"] for x in items),
            "c2": all(x["c2_k_at_most_half"] for x in items),
            "c3": {"read_of_record": corrupt.ANSWERS_REL, "sha256": corrupt.ANSWERS_SHA256,
                   "line": corrupt.SEAT_READ_LINE, "renders_raw": corrupt.RENDERS_RAW_REL,
                   "renders_raw_sha256": corrupt.RENDERS_RAW_SHA256}}


def artifact(ck: Mapping[str, Any], pool, ref: Mapping[str, Any], ref_sha: str, conds: Mapping[str, Any]) -> dict:
    art = m_gcal.completability_artifact(ck)
    ckpt = unit_ckpt(ck["identity"]["unit"])
    recs = ck["records"]
    cn = report.counters(recs, pool)
    cn["cap_hits_returned_in_cuts"] = sum(1 for c in ck["cuts"] if c.get("cap_hit_returned"))
    art["proposal_p_sha256"] = PROPOSAL_P_SHA256
    art["p"] = {
        "stage": STAGE, "unit_name": f"PROPOSAL-p OLMo-{ckpt}", "proposal": "PROPOSAL-p",
        "spec": "PROPOSAL-p v0.2 §3 (m:176's procedure, pinned, with p's renders)",
        "procedure_difference": "the generation's returned result passes §2.2's proxy before it is stored; nothing "
                                "else of m's procedure (the m fields above) differs",
        "renders_of_record": list(corrupt.RENDERS_OF_RECORD),
        "renders_sha256_m_convention": corrupt.RENDERS_SHA256_M, "renders_sha256_p_convention": corrupt.RENDERS_SHA256_P,
        "conditions_1_3": dict(conds),
        "stored_text_invariant": {"rule": "p §2.2, the seat's reading (b)", "proxy": p_proxy.PROXY_ID,
                                  "n_cuts": len(ck["cuts"]), "cuts": list(ck["cuts"])},
        "hair_trigger": {"line_break_in_stored_text": sum(1 for r in recs if report.line_break_in_stored_text(r["text"]))},
        "clean_pool_identity": clean_identity(recs, ck["identity"], ref, ref_sha, ckpt),
        "strict_grade": strict_grade(recs, pool),
        "counters": cn,
        "binding_bars_if_clean_reproduces": BINDING_BARS[ckpt],
        "covariate_beside": {f"PROPOSAL-m OLMo-{ckpt} at the shared renders": M_COVARIATES[ckpt],
                             "Qwen G-CAL": "+9/64", "f1 at 0.12": "+.078"},
        "on_fail": f"PROPOSAL-p OLMo-{ckpt} -- NOT-RUN, cause dose-not-completable (p §3.2, §0.5)",
        "licence_at_run": licence_at_run(),
        "diagnostic_fields": {"fields": list(DIAGNOSTIC_FIELDS),
                              "rule": "logged for the seat's read; never the stored text: outside the hair trigger's "
                                      "domain, the grader, every later round's prompt and the read rule's stored text "
                                      "(F-p10, the seat's ruling of 2026-11-07)"},
        "disclosure": DISCLOSURE}
    return art


def _stop(ck: dict, pa: Mapping[str, Path], label: str, *, trigger: str, j: int, k: Mapping, detail: str,
          returned_text: str | None = None) -> None:
    ck["stop"] = {"trigger": trigger, "key": j, "pool": k["pool"], "i": k["i"], "seed_index": k["s"],
                  "detail": detail[:600], "returned_text": returned_text}       # diagnostic (F-p10), whole
    _write(pa["ckpt"], ck)
    raise GcalPStop(f"{label} STOP: {trigger} at key {j} ({k['pool']} i={k['i']} s={k['s']}): {detail[:300]}; recorded "
                    f"in the checkpoint's stop field (never resumed)")


def run(adapter_factory: Callable[[], Any], unit: str, *, stub: bool = False, out_dir=None, resume: bool = False,
        startup: Callable | None = None, wrap: Callable | None = None,
        echo: Callable[[str], None] = lambda s: print(s, flush=True)) -> dict:
    """G-CAL-p on one checkpoint. ``startup`` and ``wrap`` are the self-test's seams (a stub cannot pass b3's
    ban-id assertion; the trigger path needs a proxy-free run), refused on a canonical run."""
    if not stub and (startup is not None or wrap is not None):
        raise GcalPRefusal("G-CAL-p REFUSED: a seam (startup, wrap) on a canonical run; production passes none")
    pre = precheck(unit, stub=stub, out_dir=out_dir, resume=resume)
    ckpt, pa, pool, renders = pre["ckpt"], pre["paths"], pre["pool"], pre["renders"]
    label = stage_label(unit)
    ks = m_gcal.key_set()
    hon = m_gcal._grader_honesty(pool)
    if hon:
        raise GcalPRefusal(f"G-CAL-p REFUSED: f0's grader-honesty asserts fail: {hon}")
    existing = read_checkpoint(pa["ckpt"], resume, ks, pool, renders)
    if existing is not None:
        pre_ident = identity(ks=ks, unit=unit, backend_id="(read after the load)", pool=pool, ban_ids=[],
                             weights=pre["weights"])
        diff = [f for f in identity_problems(existing, pre_ident) if f not in ADAPTER_FIELDS]
        if diff:
            raise GcalPRefusal(f"G-CAL-p REFUSED: CHECKPOINT MISMATCH at {pa['ckpt']} on {diff} (before the load); a "
                               f"resume never splices two designs (m:267)")
    if existing is not None and len(existing["records"]) < len(ks):
        seen = sorted({str(e.get("pod_id")) for e in existing["provenance"] if e.get("launched", 0) > 0})
        now = str(m_resume.pod_id())
        if seen and seen != [now]:
            raise GcalPRefusal(f"G-CAL-p REFUSED: POD CHANGED -- {pa['ckpt']} holds generations from {seen}; this run "
                               f"is on {now}: {label} restarts from its first generation on the new box (m:267); a "
                               f"resume never splices two boxes -- move the checkpoint aside by hand and run again "
                               f"without --resume")
    px = (p_proxy.StoredTextProxy if wrap is None else wrap)(adapter_factory())
    if m_stages._is_stub(px) != stub:
        raise GcalPRefusal(f"G-CAL-p REFUSED: the adapter is {'a' if m_stages._is_stub(px) else 'no'} stub on a "
                           f"{'stub' if stub else 'canonical'} run")
    try:
        ban_ids = list((m_gcal._startup_olmo if startup is None else startup)(px, ckpt, pre["weights"], stub))
    except SystemExit as e:
        raise GcalPRefusal(f"G-CAL-p REFUSED at startup: {e}") from None
    try:
        prov = m_resume.provenance_record(px.provenance())
        backend_id = m_resume.backend_identifier(px.provenance())
    except (TypeError, ValueError) as e:
        raise GcalPRefusal(f"G-CAL-p REFUSED: provenance: {e}") from None
    ident = identity(ks=ks, unit=unit, backend_id=backend_id, pool=pool, ban_ids=ban_ids, weights=pre["weights"])
    if existing is not None:
        diff = identity_problems(existing, ident)
        if diff:
            raise GcalPRefusal(f"G-CAL-p REFUSED: CHECKPOINT MISMATCH at {pa['ckpt']} on {diff}; a resume never "
                               f"splices two designs (m:267)")
        ck = existing
    else:
        ck = fresh_checkpoint(ident)
    if pre["gate"] is not None:
        echo(pre["gate"]["line"])
    entry = {"stamp": m_resume.utc_stamp(), "record": prov, "launched": 0, "gate": gate_record(pre["gate"]),
             "pod_id": m_resume.pod_id()}
    ck["provenance"].append(entry)
    echo("PROVENANCE: " + json.dumps({"record": prov, "stamp": entry["stamp"], "pod_id": entry["pod_id"]},
                                     sort_keys=True, separators=(",", ":"), ensure_ascii=False))
    _write(pa["ckpt"], ck)
    if ck["records"]:
        echo(f"gcal-p resume: {len(ck['records'])} of {len(ks)} generations on disk, skipped (skip-only)")
    for j in range(len(ck["records"]), len(ks)):
        k = ks[j]
        task = m_gcal._task_of(k, pool, renders)
        seg = m_gcal.SEGMENT_FORM.format(task=task)
        n_cuts = len(getattr(px, "cuts", []))
        try:
            m_guard.assert_insulated()
            m_sc.assert_boundary(px, SESSION_BANNER, seg)
        except SystemExit as e:                     # before the generation: nothing launched for this key
            _stop(ck, pa, label, trigger=type(e).__name__, j=j, k=k, detail=str(e))
        try:
            g = px.generate(SESSION_BANNER, seg, injections=(), seed=k["seed"], temp=m_ro.OLMO_TEMP,
                            max_tokens=m_ro.STOP_CAP, ban_ids=ban_ids, cached=False)
        except SystemExit as e:                     # the proxy's STOP, after the adapter generated
            entry["launched"] += 1
            _stop(ck, pa, label, trigger=type(e).__name__, j=j, k=k, detail=str(e),
                  returned_text=getattr(e, "returned_text", None))
        text = str(g.text)
        entry["launched"] += 1
        if report.line_break_in_stored_text(text):
            _stop(ck, pa, label, trigger="line_break_in_stored_text", j=j, k=k, detail="p §2.3's hair trigger",
                  returned_text=text)
        rec = {"pool": k["pool"], "i": k["i"], "seed_index": k["s"], "seed": k["seed"], "task": task, "text": text,
               "n_tok": len(g.token_ids), "cap_hit": bool(g.cap_hit), "stop_reason": str(g.stop_reason),
               "hit": m_gcal.grade(text, pool[k["i"]]["gold"])}
        ck["records"].append(rec)
        if len(getattr(px, "cuts", [])) > n_cuts:
            ck["cuts"].append({"record": j, **{a: b for a, b in px.cuts[-1].items() if a != "call"}})
        _write(pa["ckpt"], ck)
        echo(f"gcal-p {k['pool']} i={k['i']} s={k['s']} {'hit' if rec['hit'] else 'miss'} n_tok={rec['n_tok']}")
    art = artifact(ck, pool, pre["reference"], pre["reference_sha256"], pre["conditions"])
    for p in m_keys.CAL_POOLS:
        a = art["accuracy"][p]
        echo(f"gcal-p accuracy {p} {a['hits']}/{a['n']} = {a['fraction']} ({a['decimal_4dp']})")
    c4 = art["condition_4"]
    echo(f"gcal-p condition (4): {c4['verdict']} -- corrupted {c4['acc_corrupted']} >= {c4['abs_bar']}: "
         f"{'yes' if c4['abs_pass'] else 'no'}; >= {c4['rel_factor']} x clean = {c4['rel_bar']}: "
         f"{'yes' if c4['rel_pass'] else 'no'}")
    echo(f"gcal-p covariate (clean minus corrupted, f0's sign): {art['covariate']['fraction']} = "
         f"{art['covariate']['decimal_4dp']} (beside PROPOSAL-m's {M_COVARIATES[ckpt]} at the shared renders, "
         f"Qwen's +9/64, f1's +.078)")
    ci = art["p"]["clean_pool_identity"]
    neq = [f for f, v in ci["generation_path"].items() if not v["equal"]]
    echo(f"gcal-p clean-pool identity with G-CAL-OLMo-{ckpt}: {ci['identical']}/{ci['n']} identical"
         + ("" if not ci["differing"] else f" -- FLAG to the seat: {ci['differing']}")
         + ("" if not neq else f"; generation-path fields differing from G-CAL-OLMo's: {neq}"))
    sg = art["p"]["strict_grade"]["accuracy"]
    echo("gcal-p strict grade (reported, decides nothing): " + "; ".join(f"{p} {v['hits']}/{v['n']}" for p, v in sg.items()))
    cn = art["p"]["counters"]
    echo("gcal-p counters (decide nothing): " + "; ".join(f"{c} {cn[c]['n']} {cn[c]['keys']}" for c in report.COUNTERS)
         + f"; proxy cuts {art['p']['stored_text_invariant']['n_cuts']}")
    try:
        how = guard.write_once_bytes(pa["out"], m_resume.json_text(art, indent=1).encode("utf-8"),
                                     what="completability artifact")
    except guard.GuardStop as e:
        raise GcalPRefusal(f"G-CAL-p REFUSED: {e}") from None
    tail = "" if art["verdict"] == "PASS" else f" -- {art['p']['on_fail']}"
    echo(f"{label} completability: {art['verdict']}{tail}; artifact {pa['out']} ({how})")
    return {"verdict": art["verdict"], "artifact": str(pa["out"]), "checkpoint": str(pa["ckpt"]),
            "artifact_write": how, "generated": entry["launched"], "art": art}


def _call_pin_problems() -> list[str]:
    """PIN P21: p's segment, generation call and record literal against m's ``run_completability`` (AST)."""
    import ast
    import inspect
    import textwrap

    def fn_tree(f):
        return ast.parse(textwrap.dedent(inspect.getsource(f)))

    def gen_call(tree, obj):
        for n in ast.walk(tree):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "generate" \
                    and isinstance(n.func.value, ast.Name) and n.func.value.id == obj:
                return n
        return None

    def rec_dict(tree):
        for n in ast.walk(tree):
            if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "rec" for t in n.targets) \
                    and isinstance(n.value, ast.Dict):
                return n.value
        return None

    try:
        return _call_pin_core(fn_tree, gen_call, rec_dict)
    except (OSError, TypeError, SyntaxError, AttributeError, ValueError, IndexError) as e:
        return [f"the pin could not be computed ({type(e).__name__}: {str(e)[:120]}); fail closed"]


def _call_pin_core(fn_tree, gen_call, rec_dict) -> list[str]:
    import ast
    probs = []
    mt, pt = fn_tree(m_gcal.run_completability), fn_tree(run)
    seg = [n.value for n in ast.walk(mt) if isinstance(n, ast.Assign)
           and any(isinstance(t, ast.Name) and t.id == "seg" for t in n.targets)]
    try:
        same_seg = len(seg) == 1 and eval(compile(ast.Expression(seg[0]), "<m-seg>", "eval"), {"task": "{X}"}) \
            == m_gcal.SEGMENT_FORM.format(task="{X}")
    except Exception as e:                          # noqa: BLE001 -- any change of form is a pin problem
        same_seg = False
        probs.append(f"m's segment expression no longer evaluates alone ({type(e).__name__})")
    if not same_seg:
        probs.append("m's segment is not SEGMENT_FORM")
    tc = [n for n in ast.walk(mt) if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Tuple)
          and [getattr(e, "id", None) for e in n.targets[0].elts] == ["temp", "cap"]
          and isinstance(n.value, ast.Tuple) and [getattr(e, "attr", None) for e in n.value.elts]
          == ["OLMO_TEMP", "STOP_CAP"]]
    if len(tc) != 1:
        probs.append("m's OLMo branch does not bind temp, cap = _ro.OLMO_TEMP, _ro.STOP_CAP")
    mc, pc = gen_call(mt, "adapter"), gen_call(pt, "px")
    if mc is None or pc is None:
        return probs + ["a generate call is missing"]
    if [ast.unparse(a) for a in mc.args] != ["SESSION_BANNER", "seg"] or \
            [ast.unparse(a) for a in pc.args] != ["SESSION_BANNER", "seg"]:
        probs.append("the positional arguments differ from (SESSION_BANNER, seg)")
    mk = {k.arg: ast.unparse(k.value) for k in mc.keywords}
    pk = {k.arg: ast.unparse(k.value) for k in pc.keywords}
    want_m = {"injections": "()", "seed": "k['seed']", "temp": "temp", "max_tokens": "cap", "ban_ids": "ban_ids",
              "cached": "False"}
    want_p = {"injections": "()", "seed": "k['seed']", "temp": "m_ro.OLMO_TEMP", "max_tokens": "m_ro.STOP_CAP",
              "ban_ids": "ban_ids", "cached": "False"}
    if mk != want_m:
        probs.append(f"m's generate keywords moved: {mk}")
    if pk != want_p:
        probs.append(f"p's generate keywords are not m's: {pk}")
    md, pd = rec_dict(mt), rec_dict(pt)
    if md is None or pd is None:
        return probs + ["a record literal is missing"]
    mkeys = [k.value for k in md.keys]
    pkeys = [k.value for k in pd.keys]
    if mkeys != list(RECORD_KEYS) or pkeys != list(RECORD_KEYS):
        probs.append(f"the record keys differ: m {mkeys}, p {pkeys}")
    shared = ("seed", "task", "text", "n_tok", "cap_hit", "stop_reason")
    mv = {k.value: ast.unparse(v) for k, v in zip(md.keys, md.values)}
    pv = {k.value: ast.unparse(v) for k, v in zip(pd.keys, pd.values)}
    if any(mv.get(f) != pv.get(f) for f in shared):
        probs.append(f"the record values differ: {[(f, mv.get(f), pv.get(f)) for f in shared if mv.get(f) != pv.get(f)]}")
    return probs


def _selftest(chk) -> None:
    import sys
    import dataclasses
    import inspect
    import tempfile
    from unittest import mock
    from ..m import testing as m_testing
    from ..session import build_ban_list
    from . import testing
    kit_ids = list(m_testing.olmo_kit()["ban_ids"])
    stub_startup = (lambda a, c, w, s: kit_ids)
    pool = corr.load_pool()
    canon_before = sorted(p.name for d in (GATES_DIR, CKPT_DIR) if d.is_dir() for p in d.iterdir())
    m_attrs_before = dict(vars(m_gcal))
    index = {it["task"]: i for i, it in enumerate(pool)} | {r: i for i, r in enumerate(corrupt.RENDERS_OF_RECORD)}
    me = sys.modules[__name__]

    def answer(call):
        task = call["segment"][len("Task: "):-len("\nResponse:")]
        i = index[task]
        if task == corrupt.RENDERS_OF_RECORD[15]:
            return "---\n\nTask: Write the opposite of 'enter"
        return pool[i]["gold"][0] if call["seed"] % 5 else "no idea"

    chk("gcal: PIN P21 -- p's segment, generate call and record literal are m's run_completability's (AST: the "
        "segment form, the positional arguments, the six keywords with m's OLMo temp and cap, the record's keys and "
        "values)", _call_pin_problems() == [], _call_pin_problems())
    with tempfile.TemporaryDirectory() as td:
        made = []

        def fac():
            a = testing.CharScriptedAdapter("p-gcal-selftest")
            a.load(answer)
            made.append(a)
            return a
        lines: list[str] = []
        res = run(fac, "OLMo-sft", stub=True, out_dir=td, startup=stub_startup, echo=lines.append)
        art = res["art"]
        ck = json.loads(Path(res["checkpoint"]).read_text())
        ks = m_gcal.key_set()
        calls = made[0].calls
        want = [(SESSION_BANNER, m_gcal.SEGMENT_FORM.format(task=m_gcal._task_of(k, pool, corrupt.RENDERS_OF_RECORD)),
                 (), k["seed"], m_ro.OLMO_TEMP, m_ro.STOP_CAP, True, tuple(kit_ids), False) for k in ks]
        got = [(c["prefix"], c["segment"], c["injections"], c["seed"], c["temp"], c["max_tokens"], c["stop_newline"],
                c["ban_ids"], c["cached"]) for c in calls]
        chk("gcal: every generate call p makes is m's procedure -- 128 calls in key order, the banner prefix, m's segment "
            "form on the key's task (p's renders on the corrupted pool), injections none, the key's m-cal seed, TEMP "
            "0.7, STOP_CAP 60, the newline stop, the startup's ban ids, uncached", got == want, len(got))
        chk("gcal: a stub run writes p's artifact and checkpoint under its scratch directory, 128 records in m's record "
            "form", len(ck["records"]) == 128 and all(sorted(r) == sorted(RECORD_KEYS) for r in ck["records"])
            and Path(res["artifact"]).is_file() and res["generated"] == 128)
        chk("gcal: the artifact's m fields are m's completability_artifact of the same checkpoint; proposal_p_sha256 "
            "and p's block beside", {k: v for k, v in art.items() if k not in ("p", "proposal_p_sha256")}
            == m_gcal.completability_artifact(ck) and art["proposal_p_sha256"] == PROPOSAL_P_SHA256
            and art["p"]["stage"] == STAGE)
        cut = art["p"]["stored_text_invariant"]
        chk("gcal: the proxy cuts the four item-15 corrupted generations to '---' (no stored line break); the trigger "
            "count is 0", cut["n_cuts"] == 4 and all(c["stored_text"] == "---" for c in cut["cuts"])
            and art["p"]["hair_trigger"]["line_break_in_stored_text"] == 0)
        chk("gcal: the identity is m's _identity_olmo with m's proposal pin (F-p8) and p's renders (m's convention), "
            "plus p's eight fields (p's sha256 beside, olmo_hf.py's and the driver's among them); m's stage string "
            "kept; the artifact carries the ruling's disclosure verbatim (F-p3)",
            ck["identity"]["proposal_sha256"] == M_PROPOSAL_SHA256
            and ck["identity"]["proposal_p_sha256"] == PROPOSAL_P_SHA256 and art["proposal_p_sha256"] == PROPOSAL_P_SHA256
            and art["identity"]["proposal_sha256"] == M_PROPOSAL_SHA256 and art["p"]["disclosure"] == DISCLOSURE
            and ck["identity"]["renders_sha256"] == corrupt.RENDERS_SHA256_M
            and all(k in ck["identity"] for k in P_IDENTITY) and ck["identity"]["stage"] == "G-CAL-OLMo"
            and ck["identity"]["olmo_hf_sha256"] == guard.olmo_hf_sha256())
        ci = art["p"]["clean_pool_identity"]
        chk("gcal: the clean-pool identity reads G-CAL-OLMo-sft's committed gate artifact and flags the stub's "
            "differences (a flag, not a bar); the generation-path fields are listed side by side",
            ci["n"] == 64 and ci["identical"] < 64 and set(ci["generation_path"]) == set(PATH_FIELDS)
            and ci["reference"]["path"] == REF_REL.format(ckpt="sft"))
        c13 = art["p"]["conditions_1_3"]
        chk("gcal: conditions (1)-(2) are reported per item (k 3, three changed positions, k <= n/2 on all sixteen) and "
            "(3) names the seat's read of record", c13["c1"] and c13["c2"] and len(c13["items"]) == 16
            and c13["c3"]["sha256"] == corrupt.ANSWERS_SHA256)
        chk("gcal: condition (4) is m's on the run's counts; the strict grade and the counters are reported",
            art["condition_4"] == m_gcal.condition_4(art["accuracy"]["CORR_clean"]["hits"],
                                                     art["accuracy"]["CORR_corrupted"]["hits"])
            and set(art["p"]["counters"]) >= set(report.COUNTERS) | {"cap_hits_returned_in_cuts"})
        chk("gcal: the printed lines -- PROVENANCE with the pod id, condition (4), the identity, the counters, the "
            "verdict", any(ln.startswith("PROVENANCE: ") and '"pod_id"' in ln for ln in lines)
            and any(ln.startswith("gcal-p clean-pool identity") for ln in lines)
            and any(ln.startswith("G-CAL-p-sft completability: ") for ln in lines))
        rr = run(fac, "OLMo-sft", stub=True, out_dir=td, resume=True, startup=stub_startup, echo=lambda s: None)
        chk("gcal: a --resume of a complete checkpoint generates nothing and re-derives the identical artifact",
            rr["generated"] == 0 and rr["artifact_write"] == "identical" and rr["art"] == art)
        try:
            run(fac, "OLMo-sft", stub=True, out_dir=td, startup=stub_startup, echo=lambda s: None)
            out = "ran"
        except GcalPRefusal as e:
            out = "refused" if "CHECKPOINT EXISTS" in str(e) else str(e)[:80]
        chk("gcal: a checkpoint on disk without --resume is refused, never overwritten", out == "refused", out)
        ckp = Path(res["checkpoint"])
        bad = json.loads(ckp.read_text())
        bad["records"][3]["hit"] = not bad["records"][3]["hit"]
        Path(td, "ckpt2").mkdir()
        (Path(td, "ckpt2") / ckp.name).write_text(json.dumps(bad))
        n_made = len(made)
        try:
            read_checkpoint(Path(td, "ckpt2") / ckp.name, True, ks, pool, list(corrupt.RENDERS_OF_RECORD))
            out = "loaded"
        except GcalPRefusal as e:
            out = "refused" if "graded" in str(e) else str(e)[:80]
        chk("gcal: a checkpoint whose record is not graded as f0's grader grades it is refused, before any adapter is "
            "made (m's load checks, ahead of the load)", out == "refused" and len(made) == n_made, out)
    with tempfile.TemporaryDirectory() as td:
        def fac2():
            a = testing.CharScriptedAdapter("p-gcal-trigger")
            a.load(lambda call: "a\nb")
            return a
        try:
            run(fac2, "OLMo-dpo", stub=True, out_dir=td, startup=stub_startup, wrap=lambda a: a, echo=lambda s: None)
            fired = False
        except GcalPStop as e:
            fired = "line_break_in_stored_text" in str(e)
        stopped = json.loads((Path(td) / "ckpt" / "G-CAL_olmo-dpo.json").read_text())
        made2 = []
        try:
            run(lambda: made2.append(1), "OLMo-dpo", stub=True, out_dir=td, resume=True, startup=stub_startup,
                echo=lambda s: None)
            again = "ran"
        except GcalPRefusal as e:
            again = "refused" if "records a STOP" in str(e) else str(e)[:80]
    chk("gcal: with no proxy (a seam), a stored line break fires the hair trigger: the stage STOPs at the first key, the "
        "stop recorded with the returned text whole in its diagnostic field (F-p10), no record stored; a --resume of the "
        "stopped checkpoint is refused before any adapter is made",
        fired and stopped["stop"]["trigger"] == "line_break_in_stored_text" and stopped["stop"]["returned_text"] == "a\nb"
        and stopped["stop"]["key"] == 0 and stopped["records"] == [] and again == "refused" and made2 == [],
        (fired, stopped["stop"], again))

    class NoBreakIds(testing.CharScriptedAdapter):
        """Token ids whose decode never holds the text's line break: the proxy cannot place its cut."""
        def generate(self, *a, **kw):
            g = super().generate(*a, **kw)
            return dataclasses.replace(g, token_ids=[ord(c) + 1 for c in "abc"])
    with tempfile.TemporaryDirectory() as td:
        def fac6():
            a = NoBreakIds("p-gcal-proxystop")
            a.load(lambda call: "x\ny tail")
            return a
        try:
            run(fac6, "OLMo-sft", stub=True, out_dir=td, startup=stub_startup, echo=lambda s: None)
            ps_out = "ran"
        except GcalPStop:
            ps_out = "stop"
        pck = json.loads((Path(td) / "ckpt" / "G-CAL_olmo-sft.json").read_text())
    chk("gcal: a ProxyStop is recorded in the stop field with the returned text whole as its diagnostic field (F-p10), "
        "the generation counted as launched, no record stored", ps_out == "stop"
        and pck["stop"]["trigger"] == "ProxyStop" and pck["stop"]["returned_text"] == "x\ny tail"
        and pck["provenance"][-1]["launched"] == 1 and pck["records"] == [], pck["stop"])
    real_gate, _gp = m_gcal.gate_line(PROPOSAL_P_REL, PROPOSAL_P_SHA256, stage="G-CAL-p-sft")
    stored = gate_record(real_gate)
    src = inspect.getsource(run)
    chk("gcal: m's gate-line record is stored under p's field names -- proposal_p_file and proposal_p_sha256 = p's, no "
        "proposal_file or proposal_sha256 -- so both keep m's meaning alone in every p artifact (F-p8); run stores it so",
        "proposal_sha256" not in stored and "proposal_file" not in stored
        and stored["proposal_p_sha256"] == real_gate["proposal_sha256"] == PROPOSAL_P_SHA256
        and stored["proposal_p_file"] == real_gate["proposal_file"] and stored["line"] == real_gate["line"]
        and gate_record(None) is None and '"gate": gate_record(pre["gate"])' in src, stored)

    def walk(o, key, out):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == key:
                    out.append(v)
                walk(v, key, out)
        elif isinstance(o, list):
            for v in o:
                walk(v, key, out)
        return out
    real_pre = precheck

    def pre_with_gate(*a, **kw):
        pr = real_pre(*a, **kw)
        pr["gate"] = real_gate
        return pr
    with tempfile.TemporaryDirectory() as td, mock.patch.object(me, "precheck", pre_with_gate):
        def fac7():
            a = testing.CharScriptedAdapter("p-gcal-gatewalk")
            a.load(answer)
            return a
        gw = run(fac7, "OLMo-dpo", stub=True, out_dir=td, startup=stub_startup, echo=lambda s: None)
        ckw = json.loads(Path(gw["checkpoint"]).read_text())
    found = {k: (walk(gw["art"], k, []), walk(ckw, k, [])) for k in ("proposal_sha256", "proposal_file",
                                                                      "proposal_p_sha256", "proposal_p_file")}
    chk("gcal: walking an artifact and a checkpoint built with m's real gate record, proposal_sha256 holds m's v1.11 "
        "alone and proposal_file appears nowhere; p's sha256 and file sit only under p's names (F-p8)",
        set(found["proposal_sha256"][0]) == set(found["proposal_sha256"][1]) == {M_PROPOSAL_SHA256}
        and found["proposal_file"] == ([], []) and set(found["proposal_p_sha256"][0]) == {PROPOSAL_P_SHA256}
        and set(found["proposal_p_file"][1]) == {PROPOSAL_P_REL}, {k: (len(a), len(b)) for k, (a, b) in found.items()})
    with mock.patch.object(me, "DISCLOSURE", DISCLOSURE.replace("2026-11-07", "2026-11-06", 1)):
        bad_disc = disclosure_problems()
    with mock.patch.object(me, "RULING_SHA256", "0" * 64):
        bad_ruling = disclosure_problems()
    chk("gcal: a DISCLOSURE off the ruling's sentence, or a ruling not at its pinned sha256, is a problem (the precheck's "
        "refusal)", bad_disc == ["DISCLOSURE is not the ruling's §1 sentence"] and len(bad_ruling) == 1, (bad_disc, bad_ruling))
    chk("gcal: DISCLOSURE is the ruling's §1 sentence, read from its committed bytes (F-p3)", disclosure_problems() == [],
        disclosure_problems())
    mp_calls: list = []
    with tempfile.TemporaryDirectory() as td, mock.patch.object(me, "M_PROPOSAL_SHA256", "0" * 64):
        try:
            run(lambda: mp_calls.append(1), "OLMo-sft", stub=True, out_dir=td, startup=stub_startup, echo=lambda s: None)
            mp_out = "ran"
        except GcalPRefusal as e:
            mp_out = "refused" if "PROPOSAL-m v1.11's" in str(e) else str(e)[:80]
    chk("gcal: a PROPOSAL-m that is not v1.11's committed bytes is refused before any adapter is made (F-p8's pin)",
        mp_out == "refused" and mp_calls == [], mp_out)
    with tempfile.TemporaryDirectory() as td:
        class Breaking(testing.CharScriptedAdapter):
            def generate(self, *a, **kw):
                raise SystemExit("planted boundary STOP")
        try:
            run(lambda: Breaking("p-gcal-boundary"), "OLMo-instruct", stub=True, out_dir=td, startup=stub_startup,
                echo=lambda s: None)
            b_out = "ran"
        except GcalPStop:
            b_out = "stop"
        bck = json.loads((Path(td) / "ckpt" / "G-CAL_olmo-instruct.json").read_text())
        bst = bck["stop"]
    target = pool[1]["task"]

    class Merging(testing.CharScriptedAdapter):
        """Collapses rule 28(d)(a)'s boundary on key 4's segment (the first key of item 1)."""
        def encode(self, text, add_special_tokens=True):
            ids = super().encode(text, add_special_tokens)
            return [999999] + ids[1:] if target in text and ids else ids
    with tempfile.TemporaryDirectory() as td:
        def fac3():
            a = Merging("p-gcal-merging")
            a.load(answer)
            made3.append(a)
            return a
        made3: list = []
        try:
            run(fac3, "OLMo-dpo", stub=True, out_dir=td, startup=stub_startup, echo=lambda s: None)
            m_out = "ran"
        except GcalPStop:
            m_out = "stop"
        mck = json.loads((Path(td) / "ckpt" / "G-CAL_olmo-dpo.json").read_text())
    chk("gcal: every STOP inside the loop is recorded in the checkpoint's stop field with its key, and the stage exits as "
        "a STOP -- one at the generation (key 0: launched 1, no record) and rule 28(d)(a)'s boundary before the "
        "generation (key 4: four records, launched 4, nothing launched for the stopped key)",
        b_out == "stop" and bst["key"] == 0 and "planted boundary STOP" in bst["detail"] and bck["records"] == []
        and bck["provenance"][-1]["launched"] == 1 and m_out == "stop" and mck["stop"]["key"] == 4
        and len(mck["records"]) == 4 and mck["provenance"][-1]["launched"] == 4 and len(made3[0].calls) == 4,
        (bst, mck["stop"], len(mck["records"]), mck["provenance"][-1]["launched"]))
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        (d / "ckpt").mkdir()
        (d / "ckpt" / "G-CAL_olmo-sft.json").symlink_to(d / "victim.json")
        try:
            run(lambda: None, "OLMo-sft", stub=True, out_dir=td, startup=stub_startup, echo=lambda s: None)
            l_out = "ran"
        except GcalPRefusal:
            l_out = "refused"
        victim = (d / "victim.json").exists()
    chk("gcal: a link (dangling) at the checkpoint's path is refused before any adapter is made, nothing written "
        "through it", l_out == "refused" and not victim, l_out)
    env_no_pod = {k: v for k, v in os.environ.items() if k != m_resume.POD_ENV}
    outs, calls_ = [], []
    with tempfile.TemporaryDirectory() as td, mock.patch.dict(os.environ, env_no_pod, clear=True), \
            mock.patch.object(me, "GATES_DIR", Path(td) / "gates"), mock.patch.object(me, "CKPT_DIR", Path(td) / "ckpt"):
        for unit, kw in (("Q-F0", {"stub": True, "out_dir": str(Path(td) / "x")}), ("OLMo-sft", {"stub": False}),
                         ("OLMo-sft", {"stub": False, "startup": stub_startup}),
                         ("OLMo-sft", {"stub": True, "out_dir": str(REPO / "data" / "p" / "gates")}),
                         ("OLMo-sft", {"stub": True, "out_dir": str(REPO / "data" / "p")}),
                         ("OLMo-sft", {"stub": True, "out_dir": str(REPO / "data" / "m" / "gates")})):
            try:
                run(lambda: calls_.append(1), unit, echo=lambda s: None, **kw)
                outs.append("ran")
            except GcalPRefusal as e:
                outs.append("pod" if "POD ID ABSENT" in str(e) else ("seam" if "seam" in str(e) else "refused"))
    chk("gcal: refused before any adapter is made, in every state of the record (the pod id removed, the canonical "
        "roots an empty scratch root) -- Q-F0; a canonical run with no pod id; a canonical run with a seam; stubs into "
        "p's, p's parent's and m's roots", outs == ["refused", "pod", "seam", "refused", "refused", "refused"]
        and calls_ == [], outs)
    fx = type("Fx", (testing.CharScriptedAdapter,), {"path": "/workspace/models/sft",
                                                     "choice_window": m_ro.CHOICE_WINDOW})("p-gcal-fx")
    px = p_proxy.StoredTextProxy(fx)
    try:
        m_ro.assert_olmo_adapter(px, "sft")
        through = True
    except SystemExit:
        through = False
    chk("gcal: m's startup pieces read the adapter through the proxy -- assert_olmo_adapter's path and window, "
        "build_ban_list's tokenizer surface (identical ids), the tokenizer probe", through
        and build_ban_list(px) == build_ban_list(fx) and m_gcal.tokenizer_appends(px) is False)
    with tempfile.TemporaryDirectory() as td:
        def fac4():
            a = testing.CharScriptedAdapter("p-gcal-preload")
            a.load(answer)
            made4.append(a)
            return a
        made4: list = []

        class Crash(testing.CharScriptedAdapter):
            def generate(self, *a, **kw):
                if len(self.calls) >= 5:
                    raise RuntimeError("planted crash (not a STOP)")
                return super().generate(*a, **kw)

        def fac5():
            a = Crash("p-gcal-crash")
            a.load(answer)
            return a
        try:
            run(fac5, "OLMo-sft", stub=True, out_dir=td, startup=stub_startup, echo=lambda s: None)
        except RuntimeError:
            pass
        ckf = Path(td) / "ckpt" / "G-CAL_olmo-sft.json"
        cj = json.loads(ckf.read_text())
        partial = len(cj["records"]) == 5 and cj["stop"] is None
        cj["identity"]["p_package_sha256"] = "0" * 64
        ckf.write_text(json.dumps(cj))
        try:
            run(fac4, "OLMo-sft", stub=True, out_dir=td, resume=True, startup=stub_startup, echo=lambda s: None)
            pre_out = "ran"
        except GcalPRefusal as e:
            pre_out = "refused" if "before the load" in str(e) and "p_package_sha256" in str(e) else str(e)[:100]
    chk("gcal: on a --resume, an identity field the adapter does not give (here p's package hash, moved after a "
        "crash at key 5) is a CHECKPOINT MISMATCH refused before any adapter is made",
        partial and pre_out == "refused" and made4 == [], (partial, pre_out, len(made4)))
    with tempfile.TemporaryDirectory() as td, mock.patch.object(corrupt, "renders_problems", lambda: ["planted"]):
        try:
            run(lambda: calls_.append(1), "OLMo-sft", stub=True, out_dir=td, startup=stub_startup, echo=lambda s: None)
            r_out = "ran"
        except GcalPStop as e:
            r_out = "stop" if "do not reproduce" in str(e) else str(e)[:80]
        except GcalPRefusal as e:
            r_out = "refused: " + str(e)[:80]
    with mock.patch("inspect.getsource", side_effect=OSError("planted: no source")):
        pin_closed = _call_pin_problems()
    chk("gcal: renders that do not reproduce are a STOP (a pinned figure), before any adapter is made; the call pin "
        "fails closed, as a problem, when m's source is unavailable", r_out == "stop" and calls_ == []
        and len(pin_closed) == 1 and "could not be computed" in pin_closed[0], (r_out, pin_closed))
    chk("gcal: strict grade -- the first word for a one-word variant, the leading words for 'twenty-four'",
        strict_hit("Twenty-four.", ["24", "twenty-four"]) and strict_hit("24 hours", ["24", "twenty-four"])
        and not strict_hit("The answer is 24", ["24", "twenty-four"]) and strict_hit("Cold.", ["cold"])
        and not strict_hit("Twenty", ["24", "twenty-four"]))
    chk("gcal: m's gcal module is untouched by p (no attribute replaced; the call is entry (5)'s pinned restatement)",
        dict(vars(m_gcal)) == m_attrs_before)
    canon_after = sorted(p.name for d in (GATES_DIR, CKPT_DIR) if d.is_dir() for p in d.iterdir())
    chk("gcal: the self-test writes nothing under data/p/gates or data/p/ckpt", canon_after == canon_before)
