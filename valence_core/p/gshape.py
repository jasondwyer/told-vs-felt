"""G-SHAPE-p -- scoring-scope plumbing for PROPOSAL-p's OLMo units, model-free (p v0.2 §4.2; m:277 by reference).

p §4.2: "**G-SHAPE-p**, model-free, before LOCK-p v0.1: G-SHAPE-F0's layers over p's sources map and the OLMo
templates with p's renders in m's place; PASS required."

G-SHAPE-F0's layers are m's functions, imported unchanged (``valence_core.m.gshape``), run with p's renders of
record in m's place over the three OLMo units:

  Layer A + C  ``m_gshape.grid`` over OLMo-{sft,dpo,instruct}: m's placements (each unit's 16 contrast banners x
               ROUND_TEMPLATES[0..3] x the 16 renders x the 22 gold variants x both phases, the render under the Q
               role -- 2,816 per unit, 8,448 in all), each gold scored by m's OLMo stack (``m_gshape.olmo_stack``) as
               m's OLMo runner calls it; m's fire predicate (any field of ROUND_FIRE_FIELDS); m's controls,
               ``seg+gold`` required to fire on 100% of placements, ``render-as-response`` reported.
  Shape        ``m_gshape.template_shape_problems`` with p's renders: every template, n 1..10, every render and
               every Q label is [a bracketed header naming round n, 'Task: ' + render, 'Response:'].
  Layer S      ``m_gshape.runner_scope_problems`` over m's package sources, as written (its Qwen half included):
               the runners hand classify the generation's text alone. p runs m's OLMo runner unchanged; what reaches
               it is the proxy's stored result (p §2.2), which the proxy's own self-test covers.
  Layer P      p's guard (``guard.import_problems``): the p production modules import exactly the licence's m
               modules (a fresh interpreter), import no test double at module level, assign no m attribute and call
               no setattr outside the register, and call no classify (term (e)'s static form).

THE VERDICT: m's ``_stop_reasons`` over the OLMo units' grid, the shape problems, Layer S and the OLMo identity,
with exactly one reason removed -- ``coverage:Q-F0``, which m's function adds for every built unit absent from the
grid (p places no Q-F0 render; ans2 Q4 (ii)) -- plus ``p-guard`` when Layer P has a problem. PASS iff none.

INPUTS OF RECORD, in order (a refusal or a STOP before anything is scored): numpy's stream known answer; p v0.2 (the
committed blob on the canonical run), its sha256 the routed figure, carrying §4.2's G-SHAPE-p sentence once;
PROPOSAL-m (committed, at its pinned sha256 -- the artifact's proposal_sha256, F-p8) carrying m:277's criterion, and
§2.5's banner bytes (``banner.spec_problems``); p's renders READ from the committed renders raw's
``json.dumps(renders)`` line (the file of the seat's read of record, ans2 §0; sha256 pinned), asserted equal to
``corrupt.RENDERS_OF_RECORD`` and to ``corrupt_p``'s recomputation under both sha conventions
(``corrupt.renders_problems``); the seat's answers raw (committed, sha256 pinned) carrying the read of record's line;
the pool of record (the pools file's sha256 prefix ``8547d9a11ba55b95``; 22 distinct gold variants; the 16 renders and
the 16 clean tasks 32 distinct single lines); m's OLMo stack and termination patterns.

THE ARTIFACT (``data/p/gates/G-SHAPE-p.json``, schema ``p-gshape-v1``, write-once through m's G-SHAPE writer): the
inputs, the OLMo stack record, the grid and controls per unit, the OLMo identity, the shape problems, Layers S and P,
the verdict and its reasons, each unit's placement keys against G-SHAPE-F0's committed artifact (the keys carry no
render, so p's enumeration is m's key for key; descriptive), the disclosure (p §5.4), and the provenance: p's and
m's package sha256, the sources map (p's package, the licence's m modules, G-SHAPE-F0's scoring stack, olmo_hf.py
and p's tooling) and the import closure outside both packages -- committed blobs on the canonical run.

PINs (Code, declared at the p BUILD): the stop-reason rule above -- m's function by import with one inapplicable
reason removed, never a copy; Layer S is m's check as written; the renders' source is the renders raw (p has no
model-free G-CAL artifact: condition (3) is the seat's read, ans2 §0); a canonical run requires every file of the
sources map and of the import closure committed at HEAD and unedited, and p's package hash equal to the hash of its
committed blobs and m's package hash equal to the hash of m's committed blobs, as G-SHAPE-F0's does; an ``--out``
run (refused anywhere inside the repository, ``guard.refuse_test_out``) skips that check and is never of
record; a run with any seam set never writes the canonical path.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..m import banner as m_banner
from ..m import corr
from ..m import gshape as m_gshape
from ..m import keys as m_keys
from ..m import resume as m_resume
from ..m import scaffold as m_sc
from ..m import schedule as m_schedule
from ..m import stages as m_stages
from ..session_e2a import ROUND_TEMPLATES, SESSION_BANNER
from . import corrupt, gcal, guard

REPO = Path(__file__).resolve().parents[2]
GATES_DIR = REPO / "data" / "p" / "gates"
SCHEMA = "p-gshape-v1"
STAGE = "G-SHAPE-p"
ARTIFACT_NAME = "G-SHAPE-p.json"
SPEC_REF = "PROPOSAL-p v0.2 §4.2 (G-SHAPE-p) and §8 step 4; G-SHAPE-F0's layers, PROPOSAL-m v1.11 m:277"
P_CRITERION = ("**G-SHAPE-p**, model-free, before LOCK-p v0.1: G-SHAPE-F0's layers over p's sources map and the "
               "OLMo templates with p's renders in m's place; PASS required.")
UNITS = tuple(m_gshape.OLMO_UNITS)
RENDERS_RAW_REL = corrupt.RENDERS_RAW_REL
RENDERS_RAW_SHA256 = corrupt.RENDERS_RAW_SHA256
RENDERS_LINE = corrupt.RENDERS_LINE
ANSWERS_REL = corrupt.ANSWERS_REL
ANSWERS_SHA256 = corrupt.ANSWERS_SHA256
SEAT_READ_LINE = corrupt.SEAT_READ_LINE
POOLS_SHA16 = "8547d9a11ba55b95"
F0_ARTIFACT_REL = "data/m/gates/G-SHAPE-F0.json"
TOOLING_FILES = ("valence_core/p/gshape.py", "scripts/p_sessions.py")
REMOVED_REASON = "coverage:Q-F0"
EXIT = {"PASS": 0, "STOP": 4}
SEAMS = ("inputs", "scorer", "controls", "templates", "sources", "drop", "units", "guard_problems")


class GshapePRefusal(SystemExit):
    """Decided before scoring (paths, inputs, the committed sources); nothing written (exit 2)."""


class GshapePStop(SystemExit):
    """A pinned figure that does not reproduce; nothing scored or written (exit 4)."""


def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _json_sha256(obj: Any) -> str:
    return _sha256(m_resume.json_text(obj).encode("utf-8"))


def _bytes(rel: str, *, committed: bool) -> bytes:
    if committed:
        probs, data = m_stages._committed(rel)
        if probs or data is None:
            raise GshapePRefusal(f"G-SHAPE-p REFUSED: {rel}: {probs or ['no bytes']} (every input of record is "
                                 f"committed at HEAD, rule 27)")
        return data
    try:
        return (REPO / rel).read_bytes()
    except OSError as e:
        raise GshapePRefusal(f"G-SHAPE-p REFUSED: {rel} unreadable ({e.strerror})") from None


def renders_from_raw(text: str) -> list[str]:
    """The sixteen strings of the renders raw's one ``json.dumps(renders): [...]`` line; a STOP otherwise."""
    lines = [ln for ln in text.splitlines() if ln.startswith(RENDERS_LINE)]
    if len(lines) != 1:
        raise GshapePStop(f"G-SHAPE-p STOP: {RENDERS_RAW_REL} carries {len(lines)} '{RENDERS_LINE.strip()}' lines, "
                          f"not one")
    try:
        r = json.loads(lines[0][len(RENDERS_LINE):])
    except ValueError:
        raise GshapePStop(f"G-SHAPE-p STOP: {RENDERS_RAW_REL}'s renders line is not JSON") from None
    if not (isinstance(r, list) and len(r) == m_gshape.N_ITEMS and all(isinstance(x, str) for x in r)):
        raise GshapePStop(f"G-SHAPE-p STOP: {RENDERS_RAW_REL}'s renders line is not sixteen strings")
    return r


def source_files() -> list[str]:
    """Every file the sources map records."""
    pkg = [f.relative_to(REPO).as_posix() for f in sorted(guard.PACKAGE_DIR.glob("*.py"))]
    mm = [f"valence_core/m/{m}.py" for m in guard.M_HASHED]
    return sorted(set(pkg + mm + list(m_gshape.SCORING_STACK_FILES) + [guard.OLMO_HF_REL] + list(TOOLING_FILES)))


def sources_map(*, committed: bool) -> tuple[list[str], dict]:
    """(problems, {rel: sha256}): the committed blobs' sha256 (problems name any file not committed and unedited),
    or the working tree's."""
    probs: list[str] = []
    out: dict = {}
    for rel in source_files():
        if committed:
            p, data = m_stages._committed(rel)
            if p or data is None:
                probs += [f"{rel}: {x}" for x in (p or ["no bytes"])]
                out[rel] = None
            else:
                out[rel] = _sha256(data)
        else:
            try:
                out[rel] = _sha256((REPO / rel).read_bytes())
            except OSError:
                out[rel] = None
    return probs, out


def import_closure(*, committed: bool) -> tuple[list[str], dict]:
    """(problems, {rel: sha256}) over the __file__ of every loaded valence_core.* module outside valence_core/p and
    valence_core/m (both are in the sources map)."""
    probs: list[str] = []
    out: dict = {}
    roots = (guard.PACKAGE_DIR.resolve(), guard.M_PACKAGE_DIR.resolve())
    repo = REPO.resolve()
    for name, mod in sorted(list(sys.modules.items()), key=lambda kv: kv[0]):
        if not (name == "valence_core" or name.startswith("valence_core.")):
            continue
        f = getattr(mod, "__file__", None)
        if not f:
            continue
        p = Path(f).resolve()
        if any(r in p.parents for r in roots):
            continue
        if repo not in p.parents or not p.is_file():
            probs.append(f"{name}: {f} is not a regular file in the repo (import closure)")
            continue
        rel = p.relative_to(repo).as_posix()
        if committed:
            cp, data = m_stages._committed(rel)
            if cp or data is None:
                probs += [f"{rel}: {x}" for x in (cp or ["no bytes"])]
                out[rel] = None
                continue
            out[rel] = _sha256(data)
        else:
            out[rel] = _sha256(p.read_bytes())
    return probs, dict(sorted(out.items()))


def _package_blobs_sha256() -> tuple[list[str], str | None]:
    blobs, probs = {}, []
    for f in sorted(guard.PACKAGE_DIR.glob("*.py")):
        rel = f.relative_to(REPO).as_posix()
        cp, data = m_stages._committed(rel)
        if cp or data is None:
            probs += [f"{rel}: {x}" for x in (cp or ["no bytes"])]
        else:
            blobs[rel] = data
    return probs, (None if probs else m_gshape.package_sha256_of_blobs(blobs))


def _m_package_blobs_sha256() -> tuple[list[str], str | None]:
    """m's package hash over its committed blobs (every valence_core/m/*.py, testing.py included), so the hash the
    artifact records is a committed tree's (G-SHAPE-F0's rule)."""
    blobs, probs = {}, []
    for f in sorted(guard.M_PACKAGE_DIR.glob("*.py")):
        rel = f.relative_to(REPO).as_posix()
        cp, data = m_stages._committed(rel)
        if cp or data is None:
            probs += [f"{rel}: {x}" for x in (cp or ["no bytes"])]
        else:
            blobs[rel] = data
    return probs, (None if probs else m_gshape.package_sha256_of_blobs(blobs))


def _head_blob(rel: str) -> bytes | None:
    """HEAD's blob at ``rel`` (read only), or None -- the committed record, whatever the working tree holds."""
    r = subprocess.run(["git", "cat-file", "blob", f"HEAD:{rel}"], cwd=str(REPO), capture_output=True)
    return r.stdout if r.returncode == 0 else None


def inputs_of_record(*, canonical: bool) -> dict:
    """Every precondition, in order; GshapePRefusal (exit 2) or GshapePStop (exit 4) on the first failure."""
    kp = m_keys.stream_known_answer()
    if kp:
        raise GshapePStop(f"G-SHAPE-p STOP: {kp} -- every render, key and roster rests on numpy's stream")
    pdata = _bytes(gcal.PROPOSAL_P_REL, committed=canonical)
    psha = _sha256(pdata)
    if psha != gcal.PROPOSAL_P_SHA256:
        raise GshapePRefusal(f"G-SHAPE-p REFUSED: {gcal.PROPOSAL_P_REL} hashes to {psha[:16]}, not p v0.2's "
                             f"{gcal.PROPOSAL_P_SHA256[:16]}")
    dp = gcal.disclosure_problems()
    if dp:
        raise GshapePRefusal(f"G-SHAPE-p REFUSED: the disclosure it writes is not the seat's ruled sentence: {dp} (F-p3)")
    if pdata.decode("utf-8", "replace").count(P_CRITERION) != 1:
        raise GshapePRefusal("G-SHAPE-p REFUSED: p v0.2 does not carry §4.2's G-SHAPE-p sentence exactly once")
    mdata = _bytes(m_stages.PROPOSAL_REL, committed=True)
    if _sha256(mdata) != gcal.M_PROPOSAL_SHA256:
        raise GshapePRefusal(f"G-SHAPE-p REFUSED: {m_stages.PROPOSAL_REL} hashes to {_sha256(mdata)[:16]}, not "
                             f"PROPOSAL-m v1.11's {gcal.M_PROPOSAL_SHA256[:16]} (the artifact's proposal_sha256, F-p8)")
    cp = m_gshape.criterion_problems(mdata.decode("utf-8", "replace"))
    if cp:
        raise GshapePRefusal(f"G-SHAPE-p REFUSED: {m_stages.PROPOSAL_REL} does not carry m:277's criterion: {cp}")
    bp = m_banner.spec_problems(REPO / m_stages.PROPOSAL_REL)
    if bp:
        raise GshapePStop(f"G-SHAPE-p STOP: the banners placed are not m §2.5's bytes: {bp}")
    rdata = _bytes(RENDERS_RAW_REL, committed=True)
    if _sha256(rdata) != RENDERS_RAW_SHA256:
        raise GshapePStop(f"G-SHAPE-p STOP: {RENDERS_RAW_REL} hashes to {_sha256(rdata)[:16]}, not the pinned "
                          f"{RENDERS_RAW_SHA256[:16]}")
    renders = renders_from_raw(rdata.decode("utf-8"))
    if renders != list(corrupt.RENDERS_OF_RECORD):
        raise GshapePStop("G-SHAPE-p STOP: the renders raw's strings are not corrupt.RENDERS_OF_RECORD")
    rp = corrupt.renders_problems()
    if rp:
        raise GshapePStop(f"G-SHAPE-p STOP: the renders of record do not reproduce: {rp}")
    adata = _bytes(ANSWERS_REL, committed=True)
    if _sha256(adata) != ANSWERS_SHA256 or SEAT_READ_LINE not in adata.decode("utf-8", "replace"):
        raise GshapePRefusal(f"G-SHAPE-p REFUSED: {ANSWERS_REL} is not the seat's answers of record carrying the read "
                             f"of record ({SEAT_READ_LINE!r})")
    pool = corr.load_pool()
    pools_sha = _sha256(corr.POOLS_PATH.read_bytes())
    if pools_sha[:16] != POOLS_SHA16:
        raise GshapePStop(f"G-SHAPE-p STOP: the pools file hashes to {pools_sha[:16]}, not {POOLS_SHA16}")
    clean = [it["task"] for it in pool]
    flat = [g for it in pool for g in it["gold"]]
    if (len(set(renders) | set(clean)) != 2 * m_gshape.N_ITEMS or any("\n" in t or "\r" in t for t in renders)
            or len(flat) != m_gshape.N_GOLD_VARIANTS or len(set(flat)) != m_gshape.N_GOLD_VARIANTS):
        raise GshapePStop("G-SHAPE-p STOP: the renders and clean tasks are not 32 distinct single lines, or the golds "
                          f"are not {m_gshape.N_GOLD_VARIANTS} distinct variants")
    try:
        ostack, orec = m_gshape.olmo_stack()
        term_rx = m_sc.load_term_rx()
    except SystemExit as e:
        raise GshapePStop(f"G-SHAPE-p STOP: m's OLMo stack did not build: {e}") from None
    except (ValueError, TypeError, KeyError, OSError) as e:
        raise GshapePStop(f"G-SHAPE-p STOP: m's OLMo stack did not build: {type(e).__name__}: {e}") from None
    sp, smap = sources_map(committed=canonical)
    clp, cmap = import_closure(committed=canonical)
    ppkg = guard.package_sha256()
    if canonical:
        bp2, blob_sha = _package_blobs_sha256()
        allp = sp + clp + bp2
        if allp:
            raise GshapePRefusal(f"G-SHAPE-p REFUSED: the sources map, p's package and the import closure must be "
                                 f"committed at HEAD and unedited for the run of record: {allp[:4]}"
                                 + (f" (+{len(allp) - 4} more)" if len(allp) > 4 else ""))
        if blob_sha != ppkg:
            raise GshapePRefusal(f"G-SHAPE-p REFUSED: p's committed blobs hash to {str(blob_sha)[:16]}, not the "
                                 f"package_sha256 {ppkg[:16]} this run would record")
        mp, m_blob_sha = _m_package_blobs_sha256()
        m_fresh = m_resume.package_sha256_of(guard.M_PACKAGE_DIR)
        if mp or m_blob_sha != m_fresh or m_fresh != m_resume.package_sha256():
            raise GshapePRefusal(f"G-SHAPE-p REFUSED: m's package must be committed at HEAD and unedited, every file "
                                 f"(testing.py included), for the run of record to record its hash: {mp[:3]}")
    return {"proposal_p_sha256": psha, "proposal_m_sha256": _sha256(mdata), "renders": renders, "pool": pool,
            "renders_raw_sha256": _sha256(rdata), "answers_sha256": _sha256(adata), "pools_file_sha256": pools_sha,
            "olmo_stack": ostack, "olmo_rec": orec, "term_rx": term_rx, "canonical": canonical, "sources_map": smap,
            "import_closure": cmap, "p_package_sha256": ppkg, "m_package_sha256": m_resume.package_sha256()}


def compare_f0(g: Mapping[str, Any]) -> dict:
    """Each unit's placement keys against G-SHAPE-F0's committed artifact (descriptive; the keys carry no render)."""
    data = _head_blob(F0_ARTIFACT_REL)
    if data is None:
        return {"path": F0_ARTIFACT_REL, "readable": False, "problems": ["no blob at HEAD"]}
    try:
        f0 = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return {"path": F0_ARTIFACT_REL, "readable": False, "problems": ["HEAD's blob is not JSON"]}
    per = {u: {"G-SHAPE-F0": (f0.get("grid") or {}).get(u, {}).get("placements_sha256"),
               "G-SHAPE-p": g[u]["grid"]["placements_sha256"]} for u in g}
    for v in per.values():
        v["equal"] = v["G-SHAPE-F0"] == v["G-SHAPE-p"]
    return {"path": F0_ARTIFACT_REL, "source": "HEAD's blob", "sha256": _sha256(data), "readable": True, "per_unit": per,
            "rule": "descriptive: a placement key is [unit, pair, map, clause, template, n, item, gold, phase] -- no "
                    "render -- so p's enumeration equals m's key for key; it decides nothing"}


def stop_reasons(g, shape, layer_s, identical, layer_p) -> list[str]:
    """m's ``_stop_reasons`` by import, ``coverage:Q-F0`` removed, ``p-guard`` added on a Layer P problem."""
    if "Q-F0" in g:
        raise ValueError("G-SHAPE-p places no Q-F0 render")
    reasons = [r for r in m_gshape._stop_reasons(g, shape, layer_s, identical) if r != REMOVED_REASON]
    if layer_p:
        reasons.append("p-guard")
    return sorted(set(reasons))


def evaluate(*, canonical: bool = False, inputs: Mapping[str, Any] | None = None, scorer=None, controls=None,
             templates: Sequence[str] | None = None, sources: Mapping[str, str] | None = None, drop=None,
             units: Sequence[str] | None = None, guard_problems: Sequence[str] | None = None) -> dict:
    """The artifact dict (verdict included). Every keyword but ``canonical`` is a self-test seam."""
    ins = inputs_of_record(canonical=canonical) if inputs is None else inputs
    us = UNITS if units is None else tuple(units)
    if any(u not in UNITS for u in us):
        raise ValueError(f"G-SHAPE-p's units are {UNITS}")
    shape = m_gshape.template_shape_problems(ROUND_TEMPLATES if templates is None else templates, ins["renders"])
    g = m_gshape.grid(ins, us, scorer=scorer, controls=controls, templates=templates, drop=drop)
    present = [u for u in UNITS if u in g]
    rows = sorted({g[u]["grid"]["rows_sha256"] for u in present})
    identical = (len(rows) == 1) if len(present) == len(UNITS) else None
    ls = m_gshape.runner_scope_problems(sources)
    lp = guard.import_problems(runtime=True) if guard_problems is None else list(guard_problems)
    reasons = stop_reasons(g, shape, ls, identical, lp)
    pool, renders = ins["pool"], ins["renders"]
    ro = m_schedule.roster_for(UNITS[0])
    art = {
        "schema": SCHEMA, "stage": STAGE, "spec": SPEC_REF, "criterion": P_CRITERION,
        "criterion_f0": m_gshape.CRITERION, "proposal": "PROPOSAL-p", "proposal_sha256": ins["proposal_m_sha256"],
        "proposal_p_sha256": ins["proposal_p_sha256"],
        "inputs": {
            "renders_source": f"{RENDERS_RAW_REL} (its json.dumps(renders) line; the file of the seat's read of "
                              f"record, ans2 §0), asserted equal to corrupt.RENDERS_OF_RECORD and to corrupt_p's "
                              f"recomputation",
            "renders_raw_sha256": ins["renders_raw_sha256"], "n_renders": len(renders),
            "renders_sha256_m_convention": corrupt.RENDERS_SHA256_M,
            "renders_sha256_p_convention": corrupt.RENDERS_SHA256_P,
            "seat_read": {"path": ANSWERS_REL, "sha256": ins["answers_sha256"], "line": SEAT_READ_LINE},
            "proposal_m": {"path": m_stages.PROPOSAL_REL, "sha256": ins["proposal_m_sha256"]},
            "pools_file": corr.POOLS_PATH.relative_to(REPO).as_posix(), "pools_file_sha256": ins["pools_file_sha256"],
            "pool_sha16": m_resume.pool_sha16(pool),
            "golds": {"n_items": len(pool), "n_variants": sum(len(it["gold"]) for it in pool),
                      "sha256": _json_sha256([list(it["gold"]) for it in pool])},
            "round_templates_sha256": _json_sha256(list(ROUND_TEMPLATES)),
            "session_banner_sha256": hashlib.sha256(SESSION_BANNER.encode("utf-8")).hexdigest(),
            "roster_sha256_olmo": _json_sha256([list(p) for p in ro])},
        "stacks": {"olmo": ins["olmo_rec"]},
        "fire_predicate": {"round": list(m_gshape.ROUND_FIRE_FIELDS),
                           "rule": "a placement fires iff any field fires (m's PIN-S3); any fire is a STOP"},
        "grid": {u: g[u]["grid"] for u in g},
        "grid_total": sum(g[u]["grid"]["n"] for u in g),
        "controls": {u: g[u]["controls"] for u in g},
        "olmo_grids_identical": identical, "olmo_rows_sha256": rows,
        "template_shape": {"n_problems": len(shape), "problems": shape[:m_gshape.SHAPE_LISTED_MAX],
                           "n_range": [1, m_gshape.N_ROUNDS], "n_labels": len(m_gshape.shape_labels())},
        "layer_s": ls,
        "runner_dynamic_evidence": {
            "where": ("m's self-test (scripts/m_sessions.py --selftest) at the m package_sha256 recorded here, for m's "
                      "runners; p's proxy self-test (valence_core/p/proxy.py, in scripts/p_sessions.py --selftest) at "
                      "the p package_sha256 recorded here, for the stored result the OLMo runner receives (p §2.2)"),
            "existing_checks": [{"module": m, "evidences": k, "check": c}
                                for m, k, c in m_gshape.RUNNER_DYNAMIC_EVIDENCE],
            "gshape_check": m_gshape.RUNNER_IDENTITY_CHECK},
        "layer_p": {"problems": lp, "m_imported": list(guard.M_IMPORTED),
                    "rule": "guard.import_problems: the fresh-interpreter import set equals the licence's; no test "
                            "double at module level; no m attribute assigned and no setattr outside the register; "
                            "no classify call (term (e)'s static form)"},
        "g_shape_f0_placements": compare_f0(g),
        "verdict": "PASS" if not reasons else "STOP", "stop_reasons": reasons,
        "stop_reason_rule": ("m's gshape._stop_reasons over the OLMo units' grid, by import, with 'coverage:Q-F0' "
                             "removed (p places no Q-F0 render), plus 'p-guard' on a Layer P problem"),
        "disclosure": gcal.DISCLOSURE,
        "provenance": {"p_package_sha256": ins["p_package_sha256"], "m_package_sha256": ins["m_package_sha256"],
                       "sources": ins["sources_map"], "sources_digest": _json_sha256(ins["sources_map"]),
                       "import_closure": ins["import_closure"],
                       "import_closure_digest": _json_sha256(ins["import_closure"]),
                       "committed": bool(ins["canonical"]), "numpy": _numpy_version(),
                       "numpy_stream_known_answer": "clean (f|CORR|0 permutation)"}}
    m_resume.json_text(art)
    return art


def _numpy_version() -> str:
    import numpy as np
    return np.__version__


def write(out_dir=None, **seams) -> dict:
    """Evaluate and write the artifact once: {"artifact", "path", "how", "canonical"}; a STOP verdict is written too
    (the driver's exit 4)."""
    unknown = sorted(set(seams) - set(SEAMS))
    if unknown:
        raise ValueError(f"unknown seams {unknown}")
    if out_dir is None or str(out_dir).strip() == "":
        if seams:
            raise GshapePRefusal("G-SHAPE-p REFUSED: a run with a seam set never writes the canonical artifact")
        path, canonical = GATES_DIR / ARTIFACT_NAME, True
    else:
        try:
            d = guard.refuse_test_out(out_dir)
        except guard.GuardStop as e:
            raise GshapePRefusal(f"G-SHAPE-p REFUSED: {e}") from None
        path, canonical = d / ARTIFACT_NAME, False
    tmp = path.with_name(path.name + ".tmp")
    lp = guard.no_link_problems(path, guard.P_ROOT if canonical else path.parent)
    if lp or tmp.is_symlink() or (tmp.exists() and not tmp.is_file()):
        raise GshapePRefusal(f"G-SHAPE-p REFUSED: {path}, a directory on its way or its temp name is a link or a "
                             f"non-file ({lp})")
    art = evaluate(canonical=canonical, **seams)
    if canonical:
        sp, smap = sources_map(committed=True)
        clp, cmap = import_closure(committed=True)
        if sp or clp or smap != art["provenance"]["sources"] or cmap != art["provenance"]["import_closure"]:
            raise GshapePRefusal("G-SHAPE-p REFUSED: the sources or the import closure changed during the run (drift)")
    try:
        how = guard.write_once_bytes(path, m_resume.json_text(art, indent=1).encode("utf-8"), what="G-SHAPE-p artifact")
    except guard.GuardStop as e:
        raise GshapePRefusal(f"G-SHAPE-p REFUSED: {e}") from None
    return {"artifact": art, "path": path, "how": how, "canonical": canonical}


def summary_lines(res: Mapping[str, Any]) -> list[str]:
    a = res["artifact"]
    out = [f"G-SHAPE-p {'(the run of record; committed sources)' if res['canonical'] else '(an --out run; never of record)'}"]
    for u, gu in a["grid"].items():
        c = a["controls"][u]
        out.append(f"gshape-p {u}: {gu['n']} placements, {gu['n_fired']} fired, {gu['n_misplaced']} misplaced; "
                   + "; ".join(f"{k} {v['n_fired']}/{v['n']}{' (required)' if v['required'] else ' (reported)'}"
                               for k, v in sorted(c.items())))
    f0 = a["g_shape_f0_placements"]
    out.append(f"gshape-p OLMo grids identical: {a['olmo_grids_identical']}; total {a['grid_total']}; template shape "
               f"problems {a['template_shape']['n_problems']}; Layer S problems {len(a['layer_s']['problems'])}; "
               f"Layer P problems {len(a['layer_p']['problems'])}")
    if f0.get("readable"):
        out.append("gshape-p placement keys vs G-SHAPE-F0's committed artifact: "
                   + "; ".join(f"{u} {'equal' if v['equal'] else 'DIFFERENT'}" for u, v in f0["per_unit"].items()))
    out.append(f"gshape-p provenance: p package {a['provenance']['p_package_sha256'][:16]}, m package "
               f"{a['provenance']['m_package_sha256'][:16]}, sources {a['provenance']['sources_digest'][:16]}, "
               f"closure {a['provenance']['import_closure_digest'][:16]}")
    out.append(f"G-SHAPE-p: {a['verdict']}" + (f" -- {a['stop_reasons']}" if a["stop_reasons"] else "")
               + f"; artifact {res['path']} ({res['how']})")
    return out


def _selftest(chk) -> None:
    import tempfile
    canon = GATES_DIR / ARTIFACT_NAME
    canon_before = canon.exists()
    ins = inputs_of_record(canonical=False)
    chk("gshape-p: the inputs of record build off the committed renders raw, the answers raw and both proposals; the "
        "renders read are corrupt.RENDERS_OF_RECORD", ins["renders"] == list(corrupt.RENDERS_OF_RECORD)
        and ins["renders_raw_sha256"] == RENDERS_RAW_SHA256 and ins["answers_sha256"] == ANSWERS_SHA256)
    a0 = evaluate(inputs=ins, units=(UNITS[0],), drop=(lambda pl: pl.t != 0 or pl.i != 0 or pl.pi != 0))
    from unittest import mock
    with mock.patch.object(gcal, "M_PROPOSAL_SHA256", "0" * 64):
        try:
            inputs_of_record(canonical=False)
            mp = "built"
        except GshapePRefusal as e:
            mp = "refused" if "PROPOSAL-m v1.11's" in str(e) else str(e)[:80]
    chk("gshape-p: a PROPOSAL-m that is not v1.11's committed bytes is refused (the artifact's proposal_sha256, F-p8)",
        mp == "refused", mp)
    chk("gshape-p: the artifact carries m's pin in proposal_sha256 and p's in proposal_p_sha256 (the seat's ruling of "
        "2026-11-07, F-p8), and the ruling's disclosure sentence (F-p3)",
        a0["proposal_sha256"] == gcal.M_PROPOSAL_SHA256 and a0["proposal_p_sha256"] == gcal.PROPOSAL_P_SHA256
        and a0["disclosure"] == gcal.DISCLOSURE, (a0["proposal_sha256"][:16], a0["proposal_p_sha256"][:16]))
    art = evaluate(inputs=ins)
    gt = {u: art["grid"][u]["n"] for u in UNITS}
    sg = {u: (art["controls"][u]["seg+gold"]["n_fired"], art["controls"][u]["seg+gold"]["n"]) for u in UNITS}
    chk("gshape-p: the full run PASSes -- 2,816 placements per OLMo unit (8,448), none fired or misplaced, seg+gold "
        "firing on every placement, the three grids identical, no shape, Layer S or Layer P problem",
        art["verdict"] == "PASS" and art["stop_reasons"] == [] and gt == {u: m_gshape.N_PER_UNIT for u in UNITS}
        and art["grid_total"] == 3 * m_gshape.N_PER_UNIT and all(a == b for a, b in sg.values())
        and art["olmo_grids_identical"] is True, (art["stop_reasons"], gt, sg))
    m_renders = list(m_sc.pool_and_renders()[1])
    m_keys_sha = {u: m_gshape._json_sha256([pl.key() for pl in m_gshape.placements(u, m_renders, ins["pool"])])
                  for u in UNITS}
    chk("gshape-p: each unit's placement keys equal m's own enumeration with m's renders, key for key (a key carries "
        "no render; computed here, in every state of the record)",
        all(art["grid"][u]["placements_sha256"] == m_keys_sha[u] for u in UNITS), m_keys_sha)
    f0 = art["g_shape_f0_placements"]
    chk("gshape-p: the comparison with G-SHAPE-F0's artifact reads HEAD's blob, and where HEAD carries it the three "
        "units' placement keys are equal (descriptive; the record says why where it is absent)",
        (f0.get("readable") and f0.get("source") == "HEAD's blob" and len(f0["per_unit"]) == 3
         and all(v["equal"] for v in f0["per_unit"].values())) or (f0.get("readable") is False and f0.get("problems")),
        f0)
    chk("gshape-p: the artifact points at the runners' dynamic evidence (m's self-test, p's proxy self-test)",
        art["runner_dynamic_evidence"]["existing_checks"] and "proxy" in art["runner_dynamic_evidence"]["where"])
    one = (UNITS[0],)
    small = (lambda pl: not (pl.t == 0 and pl.i in (0, 9) and pl.pi == 0))
    m_only = m_gshape._stop_reasons(m_gshape.grid(ins, one, drop=small), [], {"problems": []}, None)
    p_only = evaluate(inputs=ins, units=one, drop=small)["stop_reasons"]
    chk("gshape-p: the verdict is m's _stop_reasons with exactly 'coverage:Q-F0' removed -- on a dropped grid m's "
        "function gives coverage:Q-F0 and the dropped units' coverage; p's keeps the latter only",
        REMOVED_REASON in m_only and REMOVED_REASON not in p_only
        and sorted(set(m_only) - {REMOVED_REASON}) == p_only, (m_only, p_only))
    fired = evaluate(inputs=ins, units=one, drop=small, scorer=lambda pl: pl.seg + pl.gold)["stop_reasons"]
    silent = evaluate(inputs=ins, units=one, drop=small,
                      controls={"seg+gold": lambda pl: pl.gold, "render-as-response": lambda pl: pl.render})
    broken = evaluate(inputs=ins, units=one, drop=small,
                      templates=[t.replace("Response:", "Answer:") for t in ROUND_TEMPLATES])["stop_reasons"]
    pg = evaluate(inputs=ins, units=one, drop=small, guard_problems=["planted"])["stop_reasons"]
    chk("gshape-p: a scorer handed harness bytes fires (fire:<unit>), a silenced seg+gold control is a STOP, a broken "
        "template is a shape STOP, a Layer P problem is p-guard",
        f"fire:{UNITS[0]}" in fired and f"control-silent:{UNITS[0]}:seg+gold" in silent["stop_reasons"]
        and "shape" in broken and "p-guard" in pg, (fired, silent["stop_reasons"], broken, pg))
    raw = (REPO / RENDERS_RAW_REL).read_text(encoding="utf-8")
    planted = "\n".join(ln.replace("Stane the number op days", "Stane the number op dsys", 1)
                         if ln.startswith(RENDERS_LINE) else ln for ln in raw.splitlines())
    chk("gshape-p: the renders are read from the raw's json.dumps line; a changed string is no longer the record",
        renders_from_raw(raw) == list(corrupt.RENDERS_OF_RECORD)
        and renders_from_raw(planted) != list(corrupt.RENDERS_OF_RECORD))
    try:
        renders_from_raw(raw + "\n" + raw.splitlines()[[i for i, ln in enumerate(raw.splitlines())
                                                         if ln.startswith(RENDERS_LINE)][0]])
        twice = "read"
    except GshapePStop:
        twice = "stop"
    chk("gshape-p: a raw with two renders lines is a STOP", twice == "stop")
    with tempfile.TemporaryDirectory() as td:
        res = write(td, inputs=ins, units=one, drop=small)
        again = write(td, inputs=ins, units=one, drop=small)
        Path(td, "other").mkdir()
        Path(td, "other", ARTIFACT_NAME).write_text("{}")
        try:
            write(Path(td, "other"), inputs=ins, units=one, drop=small)
            diff = "written"
        except GshapePRefusal:
            diff = "refused"
        chk("gshape-p: an --out run writes once; a re-run with the same inputs is identical; a different file there "
            "is refused, never overwritten", res["how"] == "written" and again["how"] == "identical"
            and diff == "refused" and res["canonical"] is False)
    outs = []
    for od, kw in ((None, {"units": one}), (str(GATES_DIR), {}), (str(REPO / "data" / "p"), {}),
                   (str(REPO / "data" / "p" / "schedules"), {}), (str(REPO / "data" / "olmo"), {}),
                   (str(REPO / "data" / "m" / "gates"), {}), (str(REPO / "data" / "mf3"), {})):
        try:
            write(od, **kw)
            outs.append("written")
        except GshapePRefusal:
            outs.append("refused")
    chk("gshape-p: refused before evaluating -- a seamed run to the canonical path; an --out run inside the repository "
        "(p's gates, p's root, p's schedules, data/olmo, m's and mf3's roots)", outs == ["refused"] * 7, outs)
    chk("gshape-p: the self-test writes no canonical artifact", canon.exists() == canon_before)
