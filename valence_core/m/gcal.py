"""PROPOSAL-m G-CAL -- the dose's calibration, §8 step 6 (v1.11 §2.3 m:176; §2.7 m:267;
§3.1 m:279; §8 m:358).

ORDER (m:358: "6. G-CAL: the 0.12 replay first; the renders of record and their sha; the
seat's read; completability; roster assertion"). ``model_free_artifact`` computes the 0.12
replay first (m:358); the remaining model-free items follow -- the roster assertion among
them, computed here, ahead of m:358's listed position, because it is model-free. In this
order: (a) f1's corruptor at 0.12 replayed against conditions (1)-(2)
(``corr.f1_012_replay`` as built at step 4, "computed first at step 6 because it is
model-free", m:176), calib.json's covariate quoted beside as stored (+.078 = 0.078125);
(b) the 16 renders of record under ``corrupt_m`` -- per item the clean task, the render,
n_eligible, k, the changed positions and their count, conditions (1)-(2) and the operand
span the walk excluded -- with the renders' sha256 and m:176's figures asserted
(n_eligible 6,19,19,13,24,14,10,45,19,10,24,14,6,19,10,14; k summing to 54; one roster
skip, at item 7); (c) the roster assertion on the renders, substring, both rosters (m:176
artifacts), with the clean tasks beside for reference; (d) the four conditions -- (1)-(2)
structural and reported, (3) the seat's read and (4) completability pending; (e)
provenance. Deterministic and JSON-native; it gates nothing by itself.

THE SEAT'S READ (condition (3), m:176: "the seat's legibility read of the 16 renders of
record finds every gold recoverable"). ``seat_read_request`` is the markdown the seat
reads, built for a BLIND read: the renders' sha256 at the top, then the recording
instruction (for each render, write down the task as read and its answer, before opening
section B), then the renders ALONE, numbered 0-15, so each render is read and its answer
written before its clean text is seen; then the key (render, clean task, gold list, k,
n_eligible, changed positions, operand span) with condition (3)'s criterion. The request
states no expected outcome. The read of record is the seat's; Code records it.

COMPLETABILITY (condition (4), m:176, "pinned to f0's procedure except the path") --
``run_completability``: prompt ``SESSION_BANNER`` + ``"Task: {task}\\nResponse:"`` with no
round header (f0_calibrate.py:141-143); e2a's session config (newline stop, the scaffold
ban, ``STOP_CAP = 60``, TEMP 0.7); UNCACHED valence_core generation (a literal
``cached=False``; f0 generated on jlens's cached path, :143); 4 seeds per item, the seed
``crc32(f"m-cal|{pool}|{i}|{seed}") % 2**31`` (``keys.cal_seed``; f0's form, :152, under
m's key; a direct seed, not a stream) with ``{pool}`` in {CORR_clean, CORR_corrupted}
(f0's literals, :184-186); f0's ``normalize`` / ``grade`` ported verbatim (:56-66); 128
generations. PASS iff the corrupted pool's accuracy is >= 7/10 AND >= 3/4 x the clean
pool's, both exact Fractions; covariate = clean minus corrupted (f0's sign); FAIL ->
"STOP and re-specify" (m:176).

G-CAL-OLMo-{ckpt} (m:176: "condition (4) per checkpoint (128 generations), before that
checkpoint's G-TIME-OLMo; failure -> that checkpoint NOT-RUN with reason 'dose not
completable'"; m:302; built by the OLMo track's build, the seat's prebuild answers §0,
2026-11-06) -- ``run_completability(..., unit="OLMo-{ckpt}")``: "on OLMo the same prompt form
under b3's banner and b3's generation path" (m:176). b3's banner is ``SESSION_BANNER``
itself (banner.py's docstring: session_e2a's constant, "which b3 imports on OLMo, so one
constant serves both substrates"), so the prompt bytes are Qwen's; the generation path is the
F0m-OLMo runner's (``runner_olmo.olmo_startup``: insulation, base and cross-checkpoint
refusal, the 8192 read window, b3's ban list asserted against data/olmo/scaffold_{ckpt}.json
and b3's ids sha16; the runner's ``adapter.generate`` call: injections=(), TEMP 0.7,
``STOP_CAP = 60``, newline stop, uncached). The same 128 keys and seeds (m:176's key carries
no checkpoint field), grader, bars and covariate. The identity adds the unit, the scaffold
file's and the ban ids' hashes and the weights of record (data/olmo/manifest.json's entry for
the checkpoint: repo, revision, files_aggregate_sha256 -- the prebuild answers' Q6: "the OLMo
identity at the wiring build"). FAIL -> that checkpoint NOT-RUN, "dose not completable",
never "STOP and re-specify". R1 A6's four descriptive tallies (count-only, no bar) are printed
for the G-CAL-OLMo-{ckpt} entry and written to no artifact ("They go in the entries, not in
any lock or analyzer"): (iii) and (iv) are computed (``olmo_tallies``), (i) and (ii) are
Code's read, their candidate keys printed.

IDENTITY AND RESUME (m:267: "G-CAL's identity is its key set and this document's hash";
"skip-only"; atomic checkpoints). The identity binds the 128 (pool, i, s, seed) tuples'
sha256, the proposal's sha256, the renders' sha256, the e2a ban list's sha256, the m
package's sha256, the backend identifier, the temperature and the cap; a resume with any
difference is refused, and a resume only skips generations already on disk -- which are
always the key order's prefix, each re-graded and re-keyed on load. ``adapter.provenance()``
is recorded verbatim per invocation (ledger 27). A stub run never writes under a canonical
root (``resume.refuse_canonical_out``); a non-stub run writes the canonical paths only,
passes m:267's laptop checklist (``guard.preflight_laptop``) and logs its gate line.

Nothing here touches steering machinery; every generation passes ``injections=()``.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import zlib
from fractions import Fraction
from math import floor
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..session_e2a import SESSION_BANNER
from . import audit as _audit
from . import corr, guard, keys
from . import resume as _resume
from . import runner_olmo as _ro
from . import runner_qwen as _rq
from . import scaffold as _sc
from . import stages as _stages
# PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1): G-CAL-OLMo's startup is the F0m-OLMo
# runner's own, called through this module-level name (stages.py's form) so the self-test can
# substitute testing.olmo_kit's setup for the stub, whose ban ids cannot match b3's; production
# code has no seam.
from .runner_olmo import olmo_startup

REPO = Path(__file__).resolve().parents[2]
GATES_DIR = guard.GATES_DIR                      # data/m/gates (beside G-PORT's artifact)
CKPT_DIR = REPO / "data" / "m" / "ckpt"
MODEL_FREE_NAME = "G-CAL_model-free.json"
SEAT_READ_NAME = "G-CAL_seat_read_request.md"
COMPLETABILITY_NAME = "G-CAL_completability_qwen.json"
CKPT_NAME = "G-CAL_qwen.json"
F0_PATH = REPO / "jlens-qwen36" / "scripts" / "f0_calibrate.py"   # read only, never imported
E2A_PATH = REPO / "jlens-qwen36" / "jlens_qwen" / "e2a.py"         # read only, never imported
# PIN (Code, declared at LOCK v0.1): on a site without the gitignored jlens clone (the box),
# the three selftest checks that compare the port with f0_calibrate.py / e2a.py pass on the
# port's pinned source hashes (F0_GRADER_SRC_SHA256; for the prompt check also session_e2a's
# banner literal and SEGMENT_FORM) and say so in their note -- they neither FAIL for the
# clone's absence nor disappear, so the check count is the same on every site.
F0_ABSENT_NOTE = "f0 source absent on this site; the port is verified by its pinned hash"

MODEL_FREE_SCHEMA = "m-gcal-model-free-v1"
CKPT_SCHEMA = "m-gcal-checkpoint-v1"
ART_SCHEMA = "m-gcal-completability-v1"

# m:176's figures, asserted on the renders of record ([C], STOP-6 §E).
SPEC_N_ELIGIBLE = (6, 19, 19, 13, 24, 14, 10, 45, 19, 10, 24, 14, 6, 19, 10, 14)
SPEC_K_SUM = 54
SPEC_SKIPS = {7: 1}                               # one roster-substring skip, item 7
SPEC_OPERAND_ITEMS = (5, 11, 15)                  # "no item other than 5, 11 and 15 carries an apostrophe"
F0_COVARIATE_012_STORED = "0.078125"              # data/f/calib.json CORR_delta_covariate
F0_COVARIATE_012_QUOTED = "+.078"                 # m:176 "its 0.12 figure of record is +.078"

N_ITEMS = 16
N_SEEDS = 4
N_PER_POOL = N_ITEMS * N_SEEDS                    # 64
N_GEN = len(keys.CAL_POOLS) * N_PER_POOL          # 128 (m:176)
ABS_BAR = Fraction(7, 10)                         # ">= .70 absolute"
REL_FACTOR = Fraction(3, 4)                       # ">= .75 x the clean pool's"
SEGMENT_FORM = "Task: {task}\nResponse:"          # f0_calibrate.py:141 (documentation; built by f-string)
COND3_PENDING = "pending -- the seat's legibility read of record at G-CAL"
COND4_PENDING = "pending -- completability"
# PIN (Code, declared at LOCK v0.1): G-CAL precedes the analyzer (G-ANL-F0 is §8 step 8);
# the G-CAL gate line logs the analyzer's absence (or, if a file is there, its sha16, not
# read by G-CAL) rather than refusing as the gate stages' gate line does.
ANALYZER_ABSENT = "absent -- G-ANL-F0 is §8 step 8, after G-CAL"
IDENTITY_KEYS = ("stage", "substrate", "n", "key_set_sha256", "proposal_sha256",
                 "renders_sha256", "ban_sha256", "package_sha256", "backend_identifier",
                 "temp", "stop_cap", "path", "pool_sha16", "banner_sha256", "segment_form")
RECORD_KEYS = ("pool", "i", "seed_index", "seed", "task", "text", "n_tok", "cap_hit",
               "stop_reason", "hit")
# PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1): G-CAL-OLMo-{ckpt}'s files sit beside
# Qwen's under the same two directories, one pair per checkpoint; the identity is Qwen's keys
# plus the unit, the ban ids' sha16 (stages' form, which olmo_startup has asserted equal to
# b3's) and the weights of record from the committed manifest. ``ban_sha256`` on OLMo is the
# committed data/olmo/scaffold_{ckpt}.json's sha256, the file the scaffold set is asserted
# against (Qwen's is the e2a ban list file's).
OLMO_UNITS = tuple(f"OLMo-{c}" for c in keys.CKPTS)
COMPLETABILITY_NAME_OLMO = "G-CAL_completability_olmo-{ckpt}.json"
CKPT_NAME_OLMO = "G-CAL_olmo-{ckpt}.json"
MANIFEST_REL = "data/olmo/manifest.json"
SCAFFOLD_REL = "data/olmo/scaffold_{ckpt}.json"
IDENTITY_KEYS_OLMO = IDENTITY_KEYS + ("unit", "ban_ids_sha16", "weights_repo", "weights_revision",
                                      "weights_sha256")
ON_FAIL = {"qwen": "STOP and re-specify (m:176)",
           "olmo": "that checkpoint NOT-RUN with reason \"dose not completable\" (m:176, m:302; §5)"}
# PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1; "For the box", RESULTS.md@9cbacdb:5680-5685):
# a tokenizer that APPENDS a token under the adapter's default encode collapses rule
# 28(d)(a)'s boundary on every join, a false halt; G-CAL-OLMo, the first stage on each
# checkpoint, probes it before any generation -- two texts ending in different words must not
# encode to the same last id -- and refuses with this name.
TOKENIZER_PROBE = ("x", "x y")


# PIN (Code, declared at LOCK v0.1): a refusal is anything decided before a generation it
# would govern (paths, proposal, checkpoint identity, model-free artifact, preflight, gate
# line, startup, an existing different artifact); a STOP is a spec figure that does not
# reproduce (m:176's n_eligible / k / skip / sha / covariate) or rule 28(d)(a)'s boundary.
class GcalRefusal(SystemExit):
    """A G-CAL refusal: nothing generated past it (the driver's exit 2)."""


class GcalStop(SystemExit):
    """A G-CAL STOP: a spec figure or a delivery-geometry assertion failed (exit 4)."""


# --- f0's grader, ported verbatim (f0_calibrate.py:56-66) ------------------------------------
# PIN (Code, declared at LOCK v0.1): the two definitions are f0's source text byte for byte
# (no type hints, no docstring), so the selftest compares their source segments and ASTs
# with f0's file as well as their outputs; F0_GRADER_SRC_SHA256 pins those segments.
def normalize(s):
    return re.sub(r"[^a-z0-9/ ]", " ", s.lower()).strip()


def grade(response, gold_list):
    r = " " + normalize(response) + " "
    for g in gold_list:
        if re.search(rf"(?<![a-z0-9]){re.escape(normalize(g))}(?![a-z0-9])",
                     r):
            return True
    return False


F0_GRADER_SRC_SHA256 = {
    "normalize": "77f3f860e6252298d78df718a739a2eea52f9c3b9e847ab21115e08e9f86c950",
    "grade": "07ac36e5060a30020d921eb75e4c6dd588e7ec8d510f95513f29f3f62bafc5d5",
}


# --- small helpers ---------------------------------------------------------------------------
def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _sha256_text(s: str) -> str:
    return _sha256_bytes(s.encode("utf-8"))


def dec4(q: Fraction, *, signed: bool = False) -> str:
    """A Fraction as a 4-dp decimal, half-up on the magnitude; display only, never decided on."""
    if not isinstance(q, Fraction):
        raise TypeError(f"dec4 takes a Fraction, got {type(q).__name__}")
    sign = "-" if q < 0 else ("+" if signed else "")
    n = floor(abs(q) * 10000 + Fraction(1, 2))
    return f"{sign}{n // 10000}.{n % 10000:04d}"


def _repo_rel(p: Path) -> str:
    try:
        return Path(p).resolve().relative_to(REPO.resolve()).as_posix()
    except ValueError:
        return str(p)


def _roster_words(roster) -> list[str]:
    return sorted({w for pair in roster for w in pair})


def roster_hits(texts: Sequence[str], roster) -> list[dict]:
    """Case-insensitive substring hits of each roster word in each text (m:176 artifacts)."""
    if isinstance(texts, str):
        raise TypeError("texts is a sequence of strings, not a string")
    words = _roster_words(roster)
    return [{"i": i, "word": w} for i, t in enumerate(texts) for w in words if w in t.lower()]


def operand_spans(text: str) -> list[dict]:
    """m:176's single-quoted spans (an opening ' to the next ', quote marks included):
    {start, end (exclusive), text}.

    PIN (Code, declared at LOCK v0.1): spans are half-open character offsets into the clean
    task; an odd number of quotes is refused, as corrupt_m refuses it."""
    q = [j for j, ch in enumerate(text) if ch == "'"]
    if len(q) % 2:
        raise ValueError(f"unbalanced single quotes: {text!r}")
    return [{"start": a, "end": b + 1, "text": text[a:b + 1]} for a, b in zip(q[::2], q[1::2])]


def _write_once_text(path: Path, text: str) -> str:
    """'written' or 'identical'; GcalRefusal if a different file (or a non-file) is there.

    PIN (Code, declared at LOCK v0.1): a G-CAL artifact is never overwritten -- identical
    bytes are accepted as they are, anything else is refused and left untouched (G-PORT's
    rule); the write is atomic (temp file, fsync, rename, directory fsync)."""
    p = Path(path)
    if p.exists() or p.is_symlink():
        try:
            same = p.is_file() and not p.is_symlink() and p.read_text(encoding="utf-8") == text
        except (OSError, UnicodeDecodeError):
            same = False
        if not same:
            raise GcalRefusal(f"G-CAL ARTIFACT EXISTS at {p} with different bytes -- it is never "
                              f"overwritten (move it aside by hand if it must be replaced)")
        return "identical"
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    try:
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, p)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    _resume._fsync_dir(p.parent)
    return "written"


def write_json_once(path: Path, obj: Any) -> str:
    return _write_once_text(path, _resume.json_text(obj, indent=1))


def write_text_once(path: Path, text: str) -> str:
    return _write_once_text(path, text)


def _write_artifact(paths: Mapping[str, Path], art: Any) -> str:
    """The completability artifact's write: refused when the artifact's path as named is a
    symlink (dangling or not), then written once at the resolved path.

    PIN (Code, declared at LOCK v0.1): precheck refuses a symlink at the artifact path when no
    checkpoint is on disk; this guard covers the remaining case (a complete checkpoint and a
    symlink placed at the artifact path before a --resume), so the artifact never lands
    through a link, inside or outside the repo."""
    if paths["out_link"].is_symlink():
        raise GcalRefusal(f"G-CAL REFUSED: the artifact path {paths['out_link']} is a symlink -- an "
                          f"artifact is never written through a link")
    return write_json_once(paths["out"], art)


# --- the canonical G-CAL paths' state (the selftests' no-write checks) -----------------------
def canonical_files() -> dict[str, Path]:
    """The canonical G-CAL paths, keyed gates/<name> and ckpt/<name>: the four named
    artifacts and any other ``G-CAL*`` entry in either directory (a stray temporary or a
    probe's file). GATES_DIR and CKPT_DIR are read at call time."""
    g, c = Path(GATES_DIR), Path(CKPT_DIR)
    out = {f"gates/{n}": g / n for n in (MODEL_FREE_NAME, SEAT_READ_NAME, COMPLETABILITY_NAME)}
    out[f"ckpt/{CKPT_NAME}"] = c / CKPT_NAME
    # G-CAL-OLMo-{ckpt}'s pairs are G-CAL* names: the glob below snapshots each one that exists,
    # so a file appearing under a canonical OLMo name is a change like any other.
    for tag, d in (("gates", g), ("ckpt", c)):
        if d.is_dir():
            out.update({f"{tag}/{p.name}": p for p in d.glob("G-CAL*")})
    return out


def _path_state(p: Path) -> Any:
    if p.is_symlink():
        return ("symlink", os.readlink(p))
    if p.is_file():
        return ("file", p.read_bytes())
    if p.exists():
        return ("not a regular file", None)
    return None


def canonical_snapshot() -> dict[str, Any]:
    """Each canonical G-CAL path's state: None when absent, else its bytes (a symlink by
    its target, any other entry by its kind).

    PIN (Code, declared at LOCK v0.1): the selftests' no-write checks compare a snapshot
    taken before their runs with one taken after (G-PORT's rule, byte-identical); they never
    require the canonical artifacts to be ABSENT, so they pass before and after step 6's own
    canonical run."""
    return {k: _path_state(p) for k, p in sorted(canonical_files().items())}


def snapshot_changes(before: Mapping[str, Any], after: Mapping[str, Any]) -> list[str]:
    """The keys whose state differs between two snapshots; [] = byte-identical."""
    return sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))


# --- (1) the model-free artifact -------------------------------------------------------------
def _covariate_quote(stored: str) -> dict:
    if stored != F0_COVARIATE_012_STORED:
        raise GcalStop(f"G-CAL STOP: calib.json's covariate reads {stored}, the figure of record is "
                       f"{F0_COVARIATE_012_STORED} (m:176's +.078)")
    q = Fraction(stored)
    milli = floor(q * 1000 + Fraction(1, 2))
    if f"+.{milli:03d}" != F0_COVARIATE_012_QUOTED:
        raise GcalStop(f"G-CAL STOP: {stored} does not round half-up to {F0_COVARIATE_012_QUOTED}")
    return {"stored": stored, "as_quoted_in_m176": F0_COVARIATE_012_QUOTED,
            "sign": "clean minus corrupted (f0's)",
            "source": "data/f/calib.json CORR_delta_covariate (calib2, pools 8547d9a11ba55b95)"}


def _renders_of_record(pool: Sequence[dict]) -> dict:
    items, renders = [], []
    for i, it in enumerate(pool):
        clean = it["task"]
        render, meta = corr.corrupt_m(clean, i, corr.ROSTERS_OF_RECORD)
        if len(render) != len(clean):
            raise GcalStop(f"G-CAL STOP: item {i}'s render changes the text's length")
        changed = [j for j, (a, b) in enumerate(zip(clean, render)) if a != b]
        if changed != meta["changed_positions"]:
            raise GcalStop(f"G-CAL STOP: item {i}'s byte diff {changed} is not corrupt_m's "
                           f"changed positions {meta['changed_positions']}")
        spans = operand_spans(clean)
        if any(s["start"] <= j < s["end"] for s in spans for j in changed):
            raise GcalStop(f"G-CAL STOP: item {i} changed a letter inside its operand span")
        # PIN (Code, declared at LOCK v0.1): each item also carries its gold list (not in
        # m:176's artifact list), so the seat's read request is a function of this artifact.
        items.append({"i": i, "clean": clean, "gold": list(it["gold"]), "render": render,
                      "n_eligible": meta["n_eligible"],
                      "k": meta["k"], "changed_positions": changed, "n_changed": len(changed),
                      "n_roster_skips": meta["n_skips"], "cond1": len(changed) >= 3,
                      "cond2": meta["k"] <= meta["n_eligible"] // 2, "operand_spans": spans})
        renders.append(render)
    if renders != corr.renders_m(pool, corr.ROSTERS_OF_RECORD):
        raise GcalStop("G-CAL STOP: the per-item renders are not corr.renders_m's")
    joined = "\n".join(renders).encode("utf-8")
    sha = _sha256_bytes(joined)
    if sha[:16] != corr.renders_sha(renders):
        raise GcalStop("G-CAL STOP: renders sha256's first 16 hex are not corr.renders_sha")
    n_el = [x["n_eligible"] for x in items]
    k = [x["k"] for x in items]
    skips = {x["i"]: x["n_roster_skips"] for x in items if x["n_roster_skips"]}
    ops = tuple(x["i"] for x in items if x["operand_spans"])
    probs = []
    if tuple(n_el) != SPEC_N_ELIGIBLE:
        probs.append(f"n_eligible {n_el} != m:176's {list(SPEC_N_ELIGIBLE)}")
    if sum(k) != SPEC_K_SUM:
        probs.append(f"k sums to {sum(k)}, m:176 says {SPEC_K_SUM}")
    if any(x["n_changed"] != x["k"] for x in items):
        probs.append("an item does not reach k (m:176: every item reaches k)")
    if skips != SPEC_SKIPS:
        probs.append(f"roster skips {skips} != m:176's one skip at item 7")
    if ops != SPEC_OPERAND_ITEMS:
        probs.append(f"operand items {list(ops)} != m:176's 5, 11, 15")
    if probs:
        raise GcalStop(f"G-CAL STOP: the renders of record disagree with m:176: {probs}")
    return {"rule": "corrupt_m at 0.15, operand excluded, roster skip (m:176)",
            "items": items, "n_eligible": n_el, "k": k, "k_sum": sum(k),
            "roster_skips": {str(i): n for i, n in sorted(skips.items())},
            "renders_sha256": sha, "renders_sha16": sha[:16]}


def _roster_assertion(pool: Sequence[dict], renders: Sequence[str]) -> dict:
    qwen, olmo = corr.ROSTERS_OF_RECORD
    rh = {"qwen": roster_hits(renders, qwen), "olmo": roster_hits(renders, olmo)}
    ch = {"qwen": roster_hits([it["task"] for it in pool], qwen),
          "olmo": roster_hits([it["task"] for it in pool], olmo)}
    ok = not rh["qwen"] and not rh["olmo"]
    if not ok:
        raise GcalStop(f"G-CAL STOP: a roster word is a substring of a render: {rh}")
    return {"rule": "case-insensitive substring of each roster word in each render (m:176 artifacts)",
            "rosters": {"qwen": _roster_words(qwen), "olmo": _roster_words(olmo)},
            "renders": rh, "clean_tasks_for_reference": ch, "pass": ok}


def _condition(items: Sequence[dict], key: str, rule: str) -> dict:
    failing = [x["i"] for x in items if not x[key]]
    return {"rule": rule, "verdict": "PASS" if not failing else "FAIL",
            "n_pass": len(items) - len(failing), "n": len(items), "failing_items": failing}


def model_free_artifact(pool: Sequence[dict] | None = None, *,
                        proposal_file: str | os.PathLike = _stages.PROPOSAL_PATH) -> dict:
    """G-CAL's model-free artifact (m:176, m:358): the 0.12 replay first (m:358); the remaining
    model-free items follow (the renders of record and their sha, the roster assertion, the
    conditions, provenance). The roster assertion is computed here, ahead of m:358's listed
    position (after the seat's read and completability), because it is model-free; the
    artifact's ``computation_order`` records the order as run."""
    import numpy as np

    kp = keys.stream_known_answer()
    if kp:
        raise GcalStop(f"G-CAL STOP: {kp} -- every render of record rests on numpy's stream")
    pool = corr.load_pool() if pool is None else [dict(it) for it in pool]
    order = []
    # (a) the 0.12 replay first (m:358)
    f1 = corr.f1_012_replay(pool)
    order.append("f1_012")
    if f1["renders_sha16"] != corr.F1_012_SHA16 or f1["renders_sha_matches_calib"] is not True:
        raise GcalStop(f"G-CAL STOP: f1's 0.12 renders sha16 {f1['renders_sha16']} is not calib's "
                       f"{corr.F1_012_SHA16}")
    quote = _covariate_quote(f1["covariate_of_record"])
    order.append("f1_012_covariate_quote")
    # (b) the renders of record and their sha
    ror = _renders_of_record(pool)
    order.append("renders_of_record")
    renders = [x["render"] for x in ror["items"]]
    # (c) the roster assertion on the renders -- m:358 lists it last (after the seat's read
    # and completability); it is computed here, ahead of that position, because it is
    # model-free
    ra = _roster_assertion(pool, renders)
    order.append("roster_assertion")
    # (d) conditions
    conds = {"1": _condition(ror["items"], "cond1", "every item >= 3 changed positions (structural, "
                                                    "reported)"),
             "2": _condition(ror["items"], "cond2", "k <= floor(n_eligible / 2) (structural, "
                                                    "reported)"),
             "3": COND3_PENDING, "4": COND4_PENDING}
    order.append("conditions")
    # (e) provenance
    # PIN (Code, declared at LOCK v0.1): provenance names the pools file's full sha256 and the
    # served items' sha16, the v1.11 proposal's sha256 and numpy's version (every render rests
    # on its stream); no timestamp, so a re-run on the same site and code is byte-identical.
    pf = Path(proposal_file)
    prov = {"package_sha256": _resume.package_sha256(),
            "pools_file": _repo_rel(corr.POOLS_PATH),
            "pools_file_sha256": _sha256_bytes(corr.POOLS_PATH.read_bytes()),
            "pool_sha16": _resume.pool_sha16(pool),
            "proposal_file": _repo_rel(pf), "proposal_sha256": _sha256_bytes(pf.read_bytes()),
            "numpy": np.__version__, "numpy_stream_known_answer": "clean (f|CORR|0 permutation)"}
    order.append("provenance")
    art = {"schema": MODEL_FREE_SCHEMA, "stage": "G-CAL (model-free)",
           "spec": "PROPOSAL-m v1.11 §2.3 (m:176), §8 step 6 (m:358)",
           "computation_order": order, "f1_012": f1, "f1_012_covariate_quote": quote,
           "renders_of_record": ror, "roster_assertion": ra, "conditions": conds,
           "provenance": prov}
    _resume.json_text(art)                       # JSON-native or TypeError, before anyone writes it
    return art


# --- (4) the seat's read request -------------------------------------------------------------
SEAT_INSTRUCTION_HEAD = "## How to read -- before section A"
SEAT_INSTRUCTION = ("For each render, write down the task as you read it and its answer, before "
                    "opening section B.")
SEAT_A = "## A. The 16 renders of record -- read these first, each alone"
SEAT_B = "## B. Key -- open only after section A"
COND3_WORDS = ("the seat's legibility read of the 16 renders of record finds every gold "
               "recoverable")


def seat_read_request(art: Mapping[str, Any]) -> str:
    """The markdown the seat reads for condition (3), built for a blind read: the renders'
    sha256, the recording instruction, the renders alone (section A), then the key (B).

    PIN (Code, declared at LOCK v0.1): the request's wording is Code's; it quotes m:176 only
    verbatim (the selftest checks each quoted phrase against m:176's line). The recording
    instruction -- for each render, the task as read and its answer, written down before
    section B is opened -- stands BEFORE section A, so the seat's answers exist before the
    key is seen; section B asks a yes/no per item against the answer written in A and shows
    each changed position as clean>rendered. The request states no expected outcome (the
    seat's provisional reads are m:176's record, not the request's)."""
    ror = art["renders_of_record"]
    items = ror["items"]
    for x in items:
        for t in [x["render"], x["clean"]] + list(x["gold"]):
            if "`" in t or "\n" in t:
                raise GcalStop(f"G-CAL STOP: item {x['i']} cannot be shown verbatim in a code span")
    lines = ["# G-CAL -- the seat's legibility read of record (condition (3))", "",
             f"renders_sha256: `{ror['renders_sha256']}`", "",
             f"Source: PROPOSAL-m v1.11 §2.3 (m:176); model-free artifact `{MODEL_FREE_NAME}` "
             f"(package_sha256 `{art['provenance']['package_sha256'][:16]}`, proposal_sha256 "
             f"`{art['provenance']['proposal_sha256'][:16]}`).", "",
             SEAT_INSTRUCTION_HEAD, "",
             f"{SEAT_INSTRUCTION} Read each render alone, in order, and record one line per "
             f"render number 0-15 (the task as you read it; its answer). Read section A before "
             f"section B.", "",
             SEAT_A, ""]
    lines += [f"{x['i']}. `{x['render']}`" for x in items]
    lines += ["", "---", "", SEAT_B, "",
              f"Condition (3) (m:176): \"{COND3_WORDS}\". For each item 0-15, compare the "
              f"answer you wrote down in section A with the item's gold below and record whether "
              f"the gold is recoverable from the render (yes or no, with the answer recovered). "
              f"Condition (3) passes iff all 16 are; \"(3) or (4) failing → STOP and "
              f"re-specify\" (m:176); \"the read of record is repeated at G-CAL on the renders "
              f"of record\" (m:176). Changed positions are 0-based character offsets into the "
              f"clean task (clean letter > rendered letter); the walk never touches a "
              f"word-initial letter or the single-quoted operand.", "",
              f"Reply with the renders_sha256 at the top and the 16 per-item records (the task as "
              f"read, its answer, recoverable yes or no). The read of record is recorded in the "
              f"G-CAL entry and carried into LOCK-m-F0 v0.1, whose calibration artifacts include "
              f"the seat's read (m:176).", ""]
    for x in items:
        gold = ", ".join(f"`{g}`" for g in x["gold"])
        pos = ", ".join(f"{j} ({x['clean'][j]}>{x['render'][j]})" for j in x["changed_positions"])
        span = ", ".join(f"`{s['text']}` [{s['start']}, {s['end']})" for s in x["operand_spans"]) \
            or "none"
        lines += [f"### Item {x['i']}", f"- render: `{x['render']}`", f"- clean task: `{x['clean']}`",
                  f"- gold: {gold}", f"- k: {x['k']} (n_eligible {x['n_eligible']})",
                  f"- changed positions: {pos}", f"- operand span excluded: {span}", ""]
    return "\n".join(lines)


# --- (3) completability ----------------------------------------------------------------------
def key_set() -> list[dict]:
    """G-CAL's key set: 128 (pool, i, s, seed) in f0's order -- pool, then item, then seed."""
    if tuple(keys.CAL_POOLS) != ("CORR_clean", "CORR_corrupted"):
        raise GcalRefusal(f"G-CAL REFUSED: keys.CAL_POOLS is {keys.CAL_POOLS}, not f0's literals")
    out = []
    for pool in keys.CAL_POOLS:
        for i in range(N_ITEMS):
            for s in range(N_SEEDS):
                seed = keys.cal_seed(pool, i, s)
                if seed != zlib.crc32(f"m-cal|{pool}|{i}|{s}".encode()) % 2**31:
                    raise GcalRefusal(f"G-CAL REFUSED: keys.cal_seed({pool}, {i}, {s}) is not "
                                      f"crc32('m-cal|{pool}|{i}|{s}') % 2**31 (m:176)")
                out.append({"pool": pool, "i": i, "s": s, "seed": seed})
    return out


def key_set_sha256(ks: Sequence[Mapping[str, Any]]) -> str:
    # PIN (Code, declared at LOCK v0.1): the key set's hash is sha256 of the compact JSON
    # list of [pool, i, s, seed] in generation order.
    return _sha256_text(json.dumps([[k["pool"], k["i"], k["s"], k["seed"]] for k in ks],
                                   separators=(",", ":")))


def condition_4(hits_clean: int, hits_corrupted: int, n: int = N_PER_POOL) -> dict:
    """m:176's condition (4) on exact Fractions, with f0's covariate (clean minus corrupted)."""
    for nm, v in (("hits_clean", hits_clean), ("hits_corrupted", hits_corrupted), ("n", n)):
        if type(v) is not int:
            raise TypeError(f"{nm} must be an int, got {v!r}")
    if n <= 0 or not 0 <= hits_clean <= n or not 0 <= hits_corrupted <= n:
        raise ValueError("hits must lie in 0..n, n > 0")
    acc_c, acc_x = Fraction(hits_clean, n), Fraction(hits_corrupted, n)
    rel_bar = REL_FACTOR * acc_c
    abs_pass, rel_pass = acc_x >= ABS_BAR, acc_x >= rel_bar
    cov = acc_c - acc_x
    return {"rule": "acc_corrupted >= 7/10 AND acc_corrupted >= 3/4 x acc_clean (exact; m:176)",
            "acc_clean": str(acc_c), "acc_corrupted": str(acc_x), "abs_bar": str(ABS_BAR),
            "rel_factor": str(REL_FACTOR), "rel_bar": str(rel_bar), "abs_pass": abs_pass,
            "rel_pass": rel_pass, "verdict": "PASS" if abs_pass and rel_pass else "FAIL",
            "covariate": {"definition": "clean-pool accuracy minus corrupted-pool accuracy (f0's sign)",
                          "fraction": str(cov), "decimal_4dp": dec4(cov, signed=True),
                          "f1_012_of_record": f"{F0_COVARIATE_012_STORED} ({F0_COVARIATE_012_QUOTED})"}}


def gate_line(proposal_file: str, proposal_sha256: str, *, repo: str | os.PathLike | None = None,
              analyzer_path: str | os.PathLike | None = None,
              stage: str = "G-CAL") -> tuple[dict, list[str]]:
    """m:267's gate line for G-CAL: proposal (committed at HEAD, sha256 as named), CLAUDE.md
    (committed), HEAD, and the analyzer's absence; (record, problems). ``stage`` names the
    line's stage: "G-CAL" (Qwen, the default, its bytes unchanged) or "G-CAL-OLMo-{ckpt}"."""
    rp = Path(REPO if repo is None else repo)
    ana = Path(_stages.ANALYZER_PATH if analyzer_path is None else analyzer_path)
    probs: list[str] = []
    head = _stages._git_head(rp)
    if head == "unknown":
        probs.append("HEAD unknown (git rev-parse --verify HEAD failed)")
    cp, pdata = _stages._committed(proposal_file, rp)
    probs += [f"proposal {x}" for x in cp]
    psha = _sha256_bytes(pdata) if pdata is not None else None
    if psha is not None and psha != proposal_sha256:
        probs.append(f"proposal {proposal_file}: committed sha256 {psha[:16]}... is not the run's "
                     f"{str(proposal_sha256)[:16]}...")
    cc, cdata = _stages._committed("CLAUDE.md", rp)
    probs += [f"CLAUDE.md {x}" for x in cc]
    csha = _sha256_bytes(cdata) if cdata is not None else None
    asha = _stages._sha16_file(ana)
    analyzer = ANALYZER_ABSENT if asha is None else f"present {asha} -- not read by G-CAL"
    line = (f"GATE {stage}: proposal {proposal_file} {(psha or 'ABSENT')[:16]}, CLAUDE.md "
            f"{(csha or 'ABSENT')[:16]}, analyzer {analyzer}, HEAD {head}")
    rec = {"line": line, "proposal_file": proposal_file, "proposal_sha256": psha,
           "claude_md_sha256": csha, "analyzer": analyzer, "head": head}
    return rec, probs


def unit_ckpt(unit: str) -> str | None:
    """None for Q-F0 (Qwen's G-CAL); the checkpoint for an OLMo unit; GcalRefusal otherwise."""
    if unit == "Q-F0":
        return None
    if unit in OLMO_UNITS:
        return unit[len("OLMo-"):]
    raise GcalRefusal(f"G-CAL REFUSED: unit {unit!r} is neither Q-F0 nor an OLMo unit {OLMO_UNITS} "
                      f"(base is never an m unit, decision (7'); Q-F3 does not recalibrate, m:176)")


def _names(unit: str) -> tuple[str, str]:
    """(artifact name, checkpoint name) of the unit's completability run."""
    ck = unit_ckpt(unit)
    if ck is None:
        return COMPLETABILITY_NAME, CKPT_NAME
    return COMPLETABILITY_NAME_OLMO.format(ckpt=ck), CKPT_NAME_OLMO.format(ckpt=ck)


def stage_label(unit: str) -> str:
    """"G-CAL" (Qwen) or "G-CAL-OLMo-{ckpt}" (m:302's name)."""
    ck = unit_ckpt(unit)
    return "G-CAL" if ck is None else f"G-CAL-OLMo-{ck}"


def _canonical(unit: str = "Q-F0") -> dict[str, Path]:
    out_name, ck_name = _names(unit)
    return {"out": Path(GATES_DIR) / out_name, "ckpt": Path(CKPT_DIR) / ck_name,
            "model_free": Path(GATES_DIR) / MODEL_FREE_NAME}


def _paths(out_path: str | os.PathLike | None, stub: bool, unit: str = "Q-F0") -> dict[str, Path]:
    """The completability run's three paths: artifact, checkpoint, model-free artifact (each
    resolved), and ``out_link``, the artifact's path as named, its leaf NOT resolved.

    PIN (Code, declared at LOCK v0.1): a non-stub run writes the canonical paths only
    (data/m/gates/G-CAL_completability_qwen.json, data/m/ckpt/G-CAL_qwen.json) and reads the
    canonical model-free artifact; a stub run's checkpoint is <out dir>/ckpt/G-CAL_qwen.json
    and its model-free artifact <out dir>/G-CAL_model-free.json, each through
    resume.refuse_canonical_out. ``out_link`` exists so precheck sees a symlink AT the
    artifact's path (resolving follows it, dangling or not, to its target). An OLMo unit's
    names are G-CAL_completability_olmo-{ckpt}.json and G-CAL_olmo-{ckpt}.json, by the same
    rule."""
    canon = {k: v.resolve() for k, v in _canonical(unit).items()}
    canon["out_link"] = Path(os.path.abspath(_canonical(unit)["out"]))
    ck_name = _names(unit)[1]
    if out_path is None or str(out_path).strip() == "":
        if stub:
            raise GcalRefusal("G-CAL REFUSED: a stub run needs a scratch out path")
        return canon
    if not stub:
        if Path(out_path).expanduser().resolve() != canon["out"]:
            raise GcalRefusal(f"G-CAL REFUSED: a non-stub run writes {canon['out']} only; {out_path} "
                              f"is elsewhere (ledger 27)")
        return canon
    try:
        out = _resume.refuse_canonical_out(out_path)
        d = out.parent
        return {"out": out, "ckpt": _resume.refuse_canonical_out(d / "ckpt" / ck_name),
                "model_free": _resume.refuse_canonical_out(d / MODEL_FREE_NAME),
                "out_link": Path(os.path.abspath(Path(out_path).expanduser()))}
    except GcalRefusal:
        raise
    except SystemExit as e:
        raise GcalRefusal(f"G-CAL REFUSED: {e}") from None


def _model_free_check(path: Path, renders_sha256: str, proposal_sha256: str) -> list[str]:
    """The 0.12 replay comes first (m:358): the model-free artifact must be on disk, on these
    renders and this proposal.

    PIN (Code, declared at LOCK v0.1): completability refuses unless the model-free artifact
    exists beside it with this run's renders sha256 and proposal sha256."""
    try:
        mf = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return [f"model-free artifact absent or unreadable at {path} (m:358: the 0.12 replay first)"]
    probs = []
    if not isinstance(mf, dict) or mf.get("schema") != MODEL_FREE_SCHEMA:
        return [f"model-free artifact at {path} is not {MODEL_FREE_SCHEMA}"]
    if (mf.get("renders_of_record") or {}).get("renders_sha256") != renders_sha256:
        probs.append("model-free artifact's renders_sha256 is not this run's renders")
    if (mf.get("provenance") or {}).get("proposal_sha256") != proposal_sha256:
        probs.append("model-free artifact's proposal_sha256 is not this run's proposal")
    return probs


def weights_of_record(ckpt: str, *, repo: str | os.PathLike | None = None) -> tuple[list[str], dict | None]:
    """(problems, weights) for an OLMo checkpoint: the committed data/olmo/manifest.json's entry
    -- {repo, revision, files_aggregate_sha256, path, n_files} -- read from its committed blob.

    PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1): the weights of record are the manifest
    entry the respawn protocol's step (i) re-hashes the volume against (CLAUDE.md's Respawn
    protocol; scripts/box_respawn_check.py); the identity binds its repo, revision and
    files_aggregate_sha256, and a non-stub run also requires the adapter's weights path to be
    the entry's path. The full re-hash of the bytes is step (i)'s, once per box, recorded in that
    box's BACKEND entry; nothing here re-hashes 64 GB."""
    rp = Path(REPO if repo is None else repo)
    cp, data = _stages._committed(MANIFEST_REL, rp)
    if cp or data is None:
        return [f"{MANIFEST_REL}: {x}" for x in (cp or ["unreadable"])], None
    try:
        man = json.loads(data.decode("utf-8"))
        e = man[ckpt]
        w = {"repo": e["repo"], "revision": e["revision"], "sha256": e["files_aggregate_sha256"],
             "path": e["path"], "n_files": e["n_files"]}
    except (ValueError, UnicodeDecodeError, KeyError, TypeError) as ex:
        return [f"{MANIFEST_REL}: no well-formed entry for {ckpt!r} ({type(ex).__name__}: {ex})"], None
    probs = []
    if type(w["repo"]) is not str or not w["repo"]:
        probs.append(f"{MANIFEST_REL}[{ckpt}].repo is not a non-empty string")
    if type(w["revision"]) is not str or not re.fullmatch(r"[0-9a-f]{12,40}", w["revision"]):
        probs.append(f"{MANIFEST_REL}[{ckpt}].revision is not 12-40 lower-case hex")
    if type(w["sha256"]) is not str or not re.fullmatch(r"[0-9a-f]{64}", w["sha256"]):
        probs.append(f"{MANIFEST_REL}[{ckpt}].files_aggregate_sha256 is not 64 lower-case hex")
    if type(w["path"]) is not str or os.path.basename(w["path"].rstrip("/")) != ckpt:
        probs.append(f"{MANIFEST_REL}[{ckpt}].path {w['path']!r} does not end in {ckpt!r}")
    return probs, (None if probs else w)


def precheck(*, out_path: str | os.PathLike | None, resume: bool, proposal_file: str,
             proposal_sha256: str, stub: bool, pool: Sequence[dict] | None = None,
             unit: str = "Q-F0") -> dict:
    """Every refusal that needs no adapter, in order; GcalRefusal on the first set of problems.

    The driver runs it before the model loads; ``run_completability`` runs it again.

    PIN (Code, declared at LOCK v0.1): order -- pool (non-stub: the pool of record only),
    paths, the proposal's working-tree bytes hashing to the run's proposal sha256 (every
    run, stub included), the checkpoint without --resume, an existing completability
    artifact with no checkpoint on disk, the model-free artifact, then on a non-stub run
    m:267's laptop checklist and the gate line (proposal committed at HEAD with that sha256,
    CLAUDE.md committed, HEAD known).

    PIN (Code, declared at LOCK v0.1): with NO checkpoint on disk, a completability artifact
    already at the out path (or a symlink there, dangling included) is refused here, before
    any load or generation, with --resume or without: the artifact is never overwritten,
    and only its own complete checkpoint re-derives it (a --resume that generates nothing).

    PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1): on an OLMo unit the same refusals run in
    the same order, then the weights of record are read from the committed manifest (every
    run, stub included, so the identity is built from them); on a non-stub OLMo run m:267's
    LAPTOP checklist is not run -- the box's respawn protocol governs there, as for every OLMo
    stage (stages._laptop_preflight's scope) -- and the pod instance id is required instead
    (stages._require_pod's rule: "an OLMo stage needs its pod id"); the gate line names the
    stage G-CAL-OLMo-{ckpt}."""
    ckpt = unit_ckpt(unit)
    if pool is not None and not stub:
        raise GcalRefusal("G-CAL REFUSED: a non-stub run serves the pool of record only (pool=None)")
    paths = _paths(out_path, stub, unit)
    pf = REPO / proposal_file
    try:
        got = _sha256_bytes(pf.read_bytes())
    except OSError:
        raise GcalRefusal(f"G-CAL REFUSED: proposal file {proposal_file} unreadable") from None
    if got != proposal_sha256:
        raise GcalRefusal(f"G-CAL REFUSED: {proposal_file} hashes to {got[:16]}..., not the run's "
                          f"{str(proposal_sha256)[:16]}...")
    ck_on_disk = paths["ckpt"].exists() or paths["ckpt"].is_symlink()
    if ck_on_disk and not resume:
        raise GcalRefusal(f"G-CAL REFUSED: CHECKPOINT EXISTS at {paths['ckpt']}; pass --resume to "
                          f"continue it (skip-only) or move it aside; never overwritten")
    if not ck_on_disk and any(q.exists() or q.is_symlink() for q in (paths["out"], paths["out_link"])):
        raise GcalRefusal(f"G-CAL REFUSED: COMPLETABILITY ARTIFACT EXISTS at {paths['out_link']} with no "
                          f"checkpoint at {paths['ckpt']}; it is never overwritten and only its own "
                          f"complete checkpoint re-derives it -- move it aside by hand")
    served =corr.load_pool() if pool is None else [dict(it) for it in pool]
    renders = corr.renders_m(served, corr.ROSTERS_OF_RECORD)
    rsha = _sha256_text("\n".join(renders))
    probs = _model_free_check(paths["model_free"], rsha, proposal_sha256)
    weights = None
    if ckpt is not None:
        wp, weights = weights_of_record(ckpt)
        probs += [f"weights of record: {p}" for p in wp]
    gate = None
    if not stub:
        if ckpt is None:
            probs += [f"preflight: {p}" for p in guard.preflight_laptop()]
        elif _resume.pod_id() is None:
            probs.append(f"POD ID ABSENT: {stage_label(unit)} runs on the box only with its pod instance "
                         f"id (${_resume.POD_ENV}), as every OLMo stage (stages._require_pod)")
        gate, gp = gate_line(proposal_file, proposal_sha256, stage=stage_label(unit))
        probs += [f"gate line: {p}" for p in gp]
    if probs:
        raise GcalRefusal(f"G-CAL REFUSED: {probs}")
    out = {"paths": paths, "pool": served, "renders": renders, "renders_sha256": rsha, "gate": gate}
    if ckpt is not None:
        out.update(unit=unit, ckpt=ckpt, weights=weights)
    return out


def _identity(*, ks, proposal_sha256: str, renders_sha256: str, backend_id: str, pool) -> dict:
    # PIN (Code, declared at LOCK v0.1): beyond m:267's key set and proposal hash and the
    # renders / ban list / package / backend / temp / cap, the identity also binds n, the
    # path ("uncached"), the served pool's sha16, the banner's sha256 and the segment form;
    # temp is recorded as repr ("0.7") so no float enters an equality.
    return {"stage": "G-CAL", "substrate": "qwen", "n": len(ks), "key_set_sha256": key_set_sha256(ks),
            "proposal_sha256": proposal_sha256, "renders_sha256": renders_sha256,
            "ban_sha256": _audit.E2A_BAN_LIST_SHA256, "package_sha256": _resume.package_sha256(),
            "backend_identifier": backend_id, "temp": repr(_rq.TEMP), "stop_cap": _rq.STOP_CAP,
            "path": "uncached", "pool_sha16": _resume.pool_sha16(pool),
            "banner_sha256": _sha256_text(SESSION_BANNER), "segment_form": SEGMENT_FORM}


def ban_ids_sha16(ban_ids: Sequence[int]) -> str:
    """stages._startup's form: sha16 of json.dumps(sorted ban ids) (on OLMo, b3's 2dd86a453a2275ef)."""
    return hashlib.sha256(json.dumps(sorted(int(i) for i in ban_ids)).encode()).hexdigest()[:16]


def _identity_olmo(*, ks, unit: str, proposal_sha256: str, renders_sha256: str, backend_id: str, pool,
                   ban_ids: Sequence[int], weights: Mapping[str, Any]) -> dict:
    # PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1): G-CAL-OLMo-{ckpt}'s identity is Qwen
    # G-CAL's keys under the same rule (m:267's key set and proposal hash, then the renders,
    # ban list, package, backend, temp, cap, path, pool, banner and segment form) plus
    # IDENTITY_KEYS_OLMO's five: a resume on another checkpoint, another scaffold set or other
    # weights of record is refused like any other identity difference.
    ckpt = unit_ckpt(unit)
    cp, sdata = _stages._committed(SCAFFOLD_REL.format(ckpt=ckpt))
    if cp or sdata is None:
        raise GcalRefusal(f"G-CAL REFUSED: {SCAFFOLD_REL.format(ckpt=ckpt)}: {cp or 'unreadable'} (the "
                          f"identity hashes the scaffold set's committed file)")
    return {"stage": "G-CAL-OLMo", "substrate": "olmo", "n": len(ks), "key_set_sha256": key_set_sha256(ks),
            "proposal_sha256": proposal_sha256, "renders_sha256": renders_sha256,
            "ban_sha256": _sha256_bytes(sdata), "package_sha256": _resume.package_sha256(),
            "backend_identifier": backend_id, "temp": repr(_ro.OLMO_TEMP), "stop_cap": _ro.STOP_CAP,
            "path": "uncached", "pool_sha16": _resume.pool_sha16(pool),
            "banner_sha256": _sha256_text(SESSION_BANNER), "segment_form": SEGMENT_FORM,
            "unit": unit, "ban_ids_sha16": ban_ids_sha16(ban_ids), "weights_repo": weights["repo"],
            "weights_revision": weights["revision"], "weights_sha256": weights["sha256"]}


def tokenizer_appends(adapter) -> bool:
    """True iff the adapter's default encode ends two texts that end in different words with
    the same id: an appended token (EOS or another), the boundary hazard TOKENIZER_PROBE names."""
    a, b = (adapter.encode(t) for t in TOKENIZER_PROBE)
    return bool(a) and bool(b) and int(a[-1]) == int(b[-1])


def _startup_olmo(adapter, ckpt: str, weights: Mapping[str, Any], stub: bool) -> list[int]:
    """runner_olmo.olmo_startup (insulation; base and cross-checkpoint refusal; the 8192
    window; b3's ban list asserted against the scaffold file and b3's ids sha16), then the
    weights path (non-stub), TEMP and cap, and the tokenizer probe; a refusal before any
    generation."""
    try:
        guard.assert_insulated()
        st = olmo_startup(adapter, ckpt)
    except GcalRefusal:
        raise
    except (SystemExit, AssertionError) as e:
        raise GcalRefusal(f"G-CAL REFUSED at startup: {e}") from None
    if Fraction(repr(_ro.OLMO_TEMP)) != Fraction(7, 10) or _ro.STOP_CAP != 60:
        raise GcalRefusal("G-CAL REFUSED: TEMP must be 0.7 and STOP_CAP 60 (m:176)")
    if not stub:
        path = getattr(adapter, "path", None)
        if path is None or str(path).rstrip("/") != str(weights["path"]).rstrip("/"):
            raise GcalRefusal(f"G-CAL REFUSED: the adapter's weights path {path!r} is not the manifest's "
                              f"{ckpt} entry {weights['path']!r} (the weights of record)")
    if tokenizer_appends(adapter):
        raise GcalRefusal(f"G-CAL REFUSED: TOKENIZER APPENDS A TOKEN -- {TOKENIZER_PROBE!r} encode to the "
                          f"same last id under the adapter's default (add_special_tokens=True); rule "
                          f"28(d)(a)'s boundary would collapse on every join (For the box, "
                          f"RESULTS.md@9cbacdb:5680-5685). Escalate; nothing generated.")
    return list(st.ban_ids)


def _task_of(key: Mapping[str, Any], pool: Sequence[dict], renders: Sequence[str]) -> str:
    return pool[key["i"]]["task"] if key["pool"] == "CORR_clean" else renders[key["i"]]


def _load_ckpt(path: Path, ident: dict, resume: bool, ks: Sequence[dict], pool: Sequence[dict],
               renders: Sequence[str]) -> dict:
    """The checkpoint to continue, or a fresh one (m:267's refusals, skip-only)."""
    # PIN (Code, declared at LOCK v0.1): --resume with no checkpoint on disk starts fresh
    # (resume.load_or_init's rule); without --resume an existing checkpoint is refused.
    if not (path.exists() or path.is_symlink()):
        return {"schema": CKPT_SCHEMA, "identity": ident, "records": [], "provenance": [],
                "n_writes": 0}
    if not resume:
        raise GcalRefusal(f"G-CAL REFUSED: CHECKPOINT EXISTS at {path}; pass --resume")
    try:
        ck = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        raise GcalRefusal(f"G-CAL REFUSED: checkpoint {path} unreadable") from None
    if not isinstance(ck, dict) or ck.get("schema") != CKPT_SCHEMA \
            or set(ck) != {"schema", "identity", "records", "provenance", "n_writes"}:
        raise GcalRefusal(f"G-CAL REFUSED: {path} is not a {CKPT_SCHEMA} checkpoint")
    rec_id = ck["identity"] if isinstance(ck["identity"], dict) else {}
    diff = {k: [rec_id.get(k), ident.get(k)] for k in sorted(set(rec_id) | set(ident))
            if rec_id.get(k) != ident.get(k)}
    if diff:
        raise GcalRefusal(f"G-CAL REFUSED: CHECKPOINT MISMATCH at {path} on {sorted(diff)} (recorded, "
                          f"this run: {diff}); a resume never splices two designs (m:267)")
    recs = ck["records"]
    # PIN (Code, declared at LOCK v0.1): the records on disk must be the key order's prefix
    # (generation is in key order and skip-only), each re-keyed and re-graded on load.
    if not isinstance(recs, list) or len(recs) > len(ks):
        raise GcalRefusal(f"G-CAL REFUSED: {path} holds a malformed record list")
    for j, r in enumerate(recs):
        k = ks[j]
        if not isinstance(r, dict) or tuple(sorted(r)) != tuple(sorted(RECORD_KEYS)):
            raise GcalRefusal(f"G-CAL REFUSED: record {j} of {path} is malformed")
        want = {"pool": k["pool"], "i": k["i"], "seed_index": k["s"], "seed": k["seed"],
                "task": _task_of(k, pool, renders)}
        if any(r[f] != v for f, v in want.items()):
            raise GcalRefusal(f"G-CAL REFUSED: record {j} of {path} is not key {j} of the key set "
                              f"(order, seed or task) -- skip-only resumes a prefix")
        if type(r["text"]) is not str or type(r["hit"]) is not bool or type(r["n_tok"]) is not int \
                or type(r["cap_hit"]) is not bool or type(r["stop_reason"]) is not str:
            raise GcalRefusal(f"G-CAL REFUSED: record {j} of {path} has a mistyped field")
        if r["hit"] is not grade(r["text"], pool[k["i"]]["gold"]):
            raise GcalRefusal(f"G-CAL REFUSED: record {j} of {path} is not graded as f0's grader "
                              f"grades its text")
    if not isinstance(ck["provenance"], list):
        raise GcalRefusal(f"G-CAL REFUSED: {path}'s provenance is not a list")
    return ck


def _startup(adapter) -> list[int]:
    """runner_qwen.qwen_startup where it applies: insulation, no encode limit, the frozen e2a
    ban list rebuilt from the live tokenizer; a refusal before any generation."""
    try:
        guard.assert_insulated()
        _rq.assert_qwen_adapter(adapter)
        ids, _strings = _rq.qwen_ban_list(adapter)
    except GcalRefusal:
        raise
    except (SystemExit, AssertionError) as e:
        raise GcalRefusal(f"G-CAL REFUSED at startup: {e}") from None
    if Fraction(repr(_rq.TEMP)) != Fraction(7, 10) or _rq.STOP_CAP != 60:
        raise GcalRefusal("G-CAL REFUSED: TEMP must be 0.7 and STOP_CAP 60 (m:176)")
    return ids


def _grader_honesty(pool: Sequence[dict]) -> list[str]:
    """f0's grader honesty asserts (f0_calibrate.py:124-130) on the served pool; [] = honest.

    PIN (Code, declared at LOCK v0.1): run at every completability start, on CORR_clean's
    golds -- grade(gold) correct and grade(non-answer) incorrect for every item, f0's two
    literal probe texts."""
    out = []
    for i, it in enumerate(pool):
        if not grade("The answer is " + it["gold"][0] + ".", it["gold"]):
            out.append(f"item {i}: its gold is not graded correct")
        if grade("I cannot determine that quantity at all.", it["gold"]):
            out.append(f"item {i}: the non-answer is graded correct")
    return out


def _accuracy(records: Sequence[Mapping[str, Any]], pool_name: str) -> dict:
    rs = [r for r in records if r["pool"] == pool_name]
    hits = sum(1 for r in rs if r["hit"] is True)
    q = Fraction(hits, len(rs))
    return {"hits": hits, "n": len(rs), "fraction": str(q), "decimal_4dp": dec4(q)}


def completability_artifact(ck: Mapping[str, Any]) -> dict:
    """The artifact, a pure function of a complete checkpoint (re-derived byte-identically)."""
    recs = ck["records"]
    if len(recs) != ck["identity"]["n"]:
        raise ValueError("completability_artifact needs a complete checkpoint")
    acc = {p: _accuracy(recs, p) for p in keys.CAL_POOLS}
    c4 = condition_4(acc["CORR_clean"]["hits"], acc["CORR_corrupted"]["hits"],
                     acc["CORR_clean"]["n"])
    # PIN (Code, declared at LOCK v0.1): the artifact copies the provenance entries of the
    # invocations that generated at least one record, so a finish-only re-invocation
    # re-derives identical bytes (resume.report_provenance's rule).
    prov = [e for e in ck["provenance"] if e["launched"] > 0]
    if ck["identity"].get("substrate") == "olmo":
        # PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1): the OLMo artifact is Qwen's form with
        # the unit named, the procedure stated for b3's banner and generation path, and the
        # OLMo failure consequence (m:176, m:302).
        return {"schema": ART_SCHEMA, "stage": "G-CAL-OLMo", "substrate": "olmo",
                "unit": ck["identity"]["unit"],
                "condition": "(4) completability per checkpoint (m:176, m:302)", "identity": ck["identity"],
                "procedure": {"prompt": "SESSION_BANNER (b3's banner) + 'Task: {task}\\nResponse:', no round "
                                        "header (f0_calibrate.py:141-143; m:176 'the same prompt form under "
                                        "b3's banner')",
                              "generation": (f"b3's generation path as the F0m-OLMo runner calls it: uncached "
                                             f"(cached=False), injections=(), newline stop, b3's ban list "
                                             f"({SCAFFOLD_REL.format(ckpt=unit_ckpt(ck['identity']['unit']))}, "
                                             f"ids sha16 {ck['identity']['ban_ids_sha16']}), STOP_CAP 60, TEMP 0.7"),
                              "seeds": "crc32('m-cal|{pool}|{i}|{seed}') % 2**31, seed 0..3 (m:176)",
                              "grader": "f0's normalize / grade, ported verbatim (f0_calibrate.py:56-66)",
                              "boundary": "rule 28(d)(a) asserted before every generation (f0 had none); "
                                          "the appended-token probe before the first"},
                "provenance": prov, "records": recs, "accuracy": acc, "condition_4": c4,
                "covariate": c4["covariate"], "verdict": c4["verdict"], "on_fail": ON_FAIL["olmo"]}
    return {"schema": ART_SCHEMA, "stage": "G-CAL", "substrate": "qwen",
            "condition": "(4) completability (m:176)", "identity": ck["identity"],
            "procedure": {"prompt": "SESSION_BANNER + 'Task: {task}\\nResponse:', no round header "
                                    "(f0_calibrate.py:141-143)",
                          "generation": "valence_core uncached (cached=False), injections=(), newline "
                                        "stop, e2a ban list, STOP_CAP 60, TEMP 0.7",
                          "seeds": "crc32('m-cal|{pool}|{i}|{seed}') % 2**31, seed 0..3 (m:176)",
                          "grader": "f0's normalize / grade, ported verbatim (f0_calibrate.py:56-66)",
                          "boundary": "rule 28(d)(a) asserted before every generation (f0 had none)"},
            "provenance": prov, "records": recs, "accuracy": acc, "condition_4": c4,
            "covariate": c4["covariate"], "verdict": c4["verdict"],
            "on_fail": ON_FAIL["qwen"]}


def corrupted_words(item: Mapping[str, Any]) -> list[str]:
    """The corrupted words of a render of record: each maximal [A-Za-z]+ run of the render that
    holds at least one of the model-free artifact's changed positions, in render order."""
    pos = set(item["changed_positions"])
    return [m.group(0) for m in re.finditer(r"[A-Za-z]+", item["render"])
            if any(p in pos for p in range(m.start(), m.end()))]


def mirrors(text: str, words: Sequence[str]) -> bool:
    """True iff ``text`` contains one of ``words`` as a whole word (letter boundaries), case as written."""
    return any(re.search(r"(?<![A-Za-z])" + re.escape(w) + r"(?![A-Za-z])", text) for w in words)


def olmo_tallies(records: Sequence[Mapping[str, Any]], items: Sequence[Mapping[str, Any]],
                 term_rx: Sequence[str]) -> dict:
    """R1 A6's four descriptive tallies for a G-CAL-OLMo-{ckpt} entry: count-only, no bar, no
    effect on condition (4), written to no artifact ("They go in the entries, not in any lock
    or analyzer"; RESULTS.md@9cbacdb:4104-4114).

    PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1): (iii) = the records whose text matches f's
    descriptive termination patterns as the runners test them (scaffold.termination); (iv) =
    the corrupted-pool records whose text contains, as a whole word and case as written, a
    corrupted word of their item's render (``corrupted_words``). Both definitions reproduce
    Code's Qwen observations of record exactly -- one termination echo (corrupted item 6, seed
    1) and 11 restatements of a corrupted word, 9 of them graded hits
    (RESULTS.md@9cbacdb:5032-5041) -- which the self-test checks on the committed Qwen artifact.
    (i) and (ii) are "by Code's read": the helper lists their candidates by key only -- the
    hits on items 7 and 9 (whether the text states the answer is the read), and the misses on
    item 15 (whether each is "close" is the read). (iv)'s limit (the build's review, finding 10):
    a corrupted word that is itself an English word ("on" in item 15's render, "thy" in item 2's)
    counts wherever an answer uses it in its own sense; the keys are printed so the entry can say
    which restatements are such."""
    by = {int(it["i"]): it for it in items}
    def key(r):
        return f"{r['pool']} i={r['i']} s={r['seed_index']}"
    term = [r for r in records if _sc.termination(r["text"], term_rx)]
    mirr = [r for r in records if r["pool"] == "CORR_corrupted"
            and mirrors(r["text"], corrupted_words(by[int(r["i"])]))]
    i_cand = [r for r in records if r["i"] in (7, 9) and r["hit"] is True]
    ii_cand = [r for r in records if r["i"] == 15 and r["hit"] is False]
    return {"iii_termination": {"n": len(term), "keys": [key(r) for r in term]},
            "iv_mirroring": {"n": len(mirr), "hits": sum(1 for r in mirr if r["hit"] is True),
                             "keys": [key(r) for r in mirr]},
            "i_candidates": {"n": len(i_cand), "keys": [key(r) for r in i_cand]},
            "ii_candidates": {"n": len(ii_cand), "keys": [key(r) for r in ii_cand]}}


def tally_lines(t: Mapping[str, Any]) -> list[str]:
    """The tallies as stdout lines: counts and keys, never a response's text."""
    return [f"gcal tally (iii) lines matching f's descriptive termination patterns: {t['iii_termination']['n']} "
            f"{t['iii_termination']['keys']}",
            f"gcal tally (iv) corrupted-pool answers restating a corrupted word of their render: "
            f"{t['iv_mirroring']['n']}, of them graded hits {t['iv_mirroring']['hits']} {t['iv_mirroring']['keys']}",
            f"gcal tally (i) for Code's read -- hits on items 7 and 9: {t['i_candidates']['n']} "
            f"{t['i_candidates']['keys']}",
            f"gcal tally (ii) for Code's read -- misses on item 15: {t['ii_candidates']['n']} "
            f"{t['ii_candidates']['keys']}"]


def run_completability(adapter, *, out_path: str | os.PathLike | None, resume: bool,
                       proposal_file: str, proposal_sha256: str,
                       pool: Sequence[dict] | None = None, unit: str = "Q-F0") -> dict:
    """Condition (4): 128 uncached generations, graded by f0's grader (m:176) -- on Qwen
    (unit Q-F0, G-CAL) or on one OLMo checkpoint (unit OLMo-{ckpt}, G-CAL-OLMo-{ckpt}, m:302)."""
    ckpt = unit_ckpt(unit)
    lab = stage_label(unit)
    stub = _stages._is_stub(adapter)
    pre = precheck(out_path=out_path, resume=resume, proposal_file=proposal_file,
                   proposal_sha256=proposal_sha256, stub=stub, pool=pool, unit=unit)
    paths, served, renders = pre["paths"], pre["pool"], pre["renders"]
    if ckpt is None:
        ban_ids = _startup(adapter)
        temp, cap = _rq.TEMP, _rq.STOP_CAP
    else:
        ban_ids = _startup_olmo(adapter, ckpt, pre["weights"], stub)
        temp, cap = _ro.OLMO_TEMP, _ro.STOP_CAP
    hon = _grader_honesty(served)
    if hon:
        raise GcalRefusal(f"G-CAL REFUSED: f0's grader-honesty asserts fail: {hon}")
    ks = key_set()
    try:
        prov_rec = _resume.provenance_record(adapter.provenance())
        backend_id = _resume.backend_identifier(adapter.provenance())
    except (TypeError, ValueError) as e:
        raise GcalRefusal(f"G-CAL REFUSED: provenance: {e}") from None
    if ckpt is None:
        ident = _identity(ks=ks, proposal_sha256=proposal_sha256, renders_sha256=pre["renders_sha256"],
                          backend_id=backend_id, pool=served)
    else:
        ident = _identity_olmo(ks=ks, unit=unit, proposal_sha256=proposal_sha256,
                               renders_sha256=pre["renders_sha256"], backend_id=backend_id, pool=served,
                               ban_ids=ban_ids, weights=pre["weights"])
    ck = _load_ckpt(paths["ckpt"], ident, resume, ks, served, renders)
    if ckpt is not None and len(ck["records"]) < len(ks):
        # PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1; the build's review, finding 1): m:267 -- "the backend
        # identifier cannot tell two boxes of one class apart ... a gate stage carries no pod id: interrupted by a pod
        # change, it restarts from its first session on the new box" -- applied to G-CAL-OLMo: a resume that would
        # generate on a pod other than the one(s) its recorded generations came from is refused (move the checkpoint
        # aside by hand and run again); a complete checkpoint re-derives its artifact anywhere (it generates nothing)
        seen = sorted({str(e.get("pod_id")) for e in ck["provenance"] if e.get("launched", 0) > 0})
        now = str(_resume.pod_id())
        if seen and seen != [now]:
            raise GcalRefusal(f"G-CAL REFUSED: POD CHANGED -- {paths['ckpt']} holds generations from pod(s) {seen}; "
                              f"this run is on {now}: {lab} restarts from its first generation on the new box (m:267); "
                              f"a resume never splices two boxes -- move the checkpoint aside by hand and run again "
                              f"without --resume")
    if pre["gate"] is not None:
        print(pre["gate"]["line"], flush=True)
    entry = {"stamp": _resume.utc_stamp(), "record": prov_rec, "launched": 0, "gate": pre["gate"]}
    if ckpt is not None:
        # PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1): an OLMo invocation also records its
        # pod instance id (ledger 27); it is provenance, not identity (only an OLMo campaign's
        # identity carries a pod id, resume.Identity).
        entry["pod_id"] = _resume.pod_id()
    ck["provenance"].append(entry)
    print("PROVENANCE: " + json.dumps({"record": prov_rec, "stamp": entry["stamp"]}, sort_keys=True,
                                      separators=(",", ":"), ensure_ascii=False), flush=True)
    paths["ckpt"].parent.mkdir(parents=True, exist_ok=True)
    ck["n_writes"] += 1
    _resume.atomic_write_json(paths["ckpt"], ck)
    done = len(ck["records"])
    if done:
        print(f"gcal resume: {done} of {len(ks)} generations on disk, skipped (skip-only)", flush=True)
    for j in range(done, len(ks)):
        k = ks[j]
        task = _task_of(k, served, renders)
        seg = f"Task: {task}\nResponse:"
        guard.assert_insulated()
        # PIN (Code, declared at LOCK v0.1): rule 28(d)(a)'s boundary is asserted before every
        # generation (a re-encode); f0 had no such assertion (f0_calibrate.py:140-145), so this
        # is a G-CAL addition to "f0's procedure", not a port of it.
        try:
            _sc.assert_boundary(adapter, SESSION_BANNER, seg)
        except SystemExit as e:
            raise GcalStop(f"{lab} STOP: {e}") from None
        g = adapter.generate(SESSION_BANNER, seg, injections=(), seed=k["seed"], temp=temp,
                             max_tokens=cap, ban_ids=ban_ids, cached=False)
        text = str(g.text)
        hit = grade(text, served[k["i"]]["gold"])
        rec = {"pool": k["pool"], "i": k["i"], "seed_index": k["s"], "seed": k["seed"], "task": task,
               "text": text, "n_tok": len(g.token_ids), "cap_hit": bool(g.cap_hit),
               "stop_reason": str(g.stop_reason), "hit": hit}
        ck["records"].append(rec)
        entry["launched"] += 1
        ck["n_writes"] += 1
        _resume.atomic_write_json(paths["ckpt"], ck)
        print(f"gcal {k['pool']} i={k['i']} s={k['s']} {'hit' if hit else 'miss'} n_tok={rec['n_tok']}",
              flush=True)
    art = completability_artifact(ck)
    for p in keys.CAL_POOLS:
        a = art["accuracy"][p]
        print(f"gcal accuracy {p} {a['hits']}/{a['n']} = {a['fraction']} ({a['decimal_4dp']})", flush=True)
    c4 = art["condition_4"]
    print(f"gcal condition (4): {c4['verdict']} -- corrupted {c4['acc_corrupted']} >= {c4['abs_bar']}: "
          f"{'yes' if c4['abs_pass'] else 'no'}; >= {c4['rel_factor']} x clean = {c4['rel_bar']}: "
          f"{'yes' if c4['rel_pass'] else 'no'}", flush=True)
    cv = art["covariate"]
    if ckpt is None:
        print(f"gcal covariate (clean minus corrupted, f0's sign): {cv['fraction']} = {cv['decimal_4dp']} "
              f"(f1's 0.12 figure of record {F0_COVARIATE_012_QUOTED})", flush=True)
    else:
        print(f"gcal covariate (clean minus corrupted, f0's sign): {cv['fraction']} = {cv['decimal_4dp']} "
              f"(LOCK-m-OLMo-{ckpt} v0.1 carries it, m:176)", flush=True)
    how = _write_artifact(paths, art)
    if ckpt is None:
        tail = "" if art["verdict"] == "PASS" else " -- STOP and re-specify (m:176)"
        print(f"G-CAL completability (Qwen): {art['verdict']}{tail}; artifact {paths['out']} ({how})",
              flush=True)
        tallies = None
    else:
        items = json.loads(Path(paths["model_free"]).read_text(encoding="utf-8"))["renders_of_record"]["items"]
        tallies = olmo_tallies(art["records"], items, _sc.load_term_rx())
        for ln in tally_lines(tallies):
            print(ln, flush=True)
        tail = "" if art["verdict"] == "PASS" else f" -- {ON_FAIL['olmo']}"
        print(f"{lab} completability: {art['verdict']}{tail}; artifact {paths['out']} ({how})", flush=True)
    out = {"verdict": art["verdict"], "artifact": str(paths["out"]), "artifact_write": how,
           "checkpoint": str(paths["ckpt"]), "accuracy": art["accuracy"], "condition_4": c4,
           "generated": entry["launched"]}
    if tallies is not None:
        out.update(unit=unit, tallies=tallies)
    return out


def write_model_free(out_dir: str | os.PathLike | None = None) -> dict:
    """The driver's model-free step: the artifact and the seat read request beside it."""
    if out_dir is None:
        d = Path(GATES_DIR)
    else:
        try:
            d = _resume.refuse_canonical_out(out_dir)
        except SystemExit as e:
            raise GcalRefusal(f"G-CAL REFUSED: {e}") from None
    art = model_free_artifact()
    req = seat_read_request(art)
    return {"artifact": art, "path": d / MODEL_FREE_NAME, "seat_path": d / SEAT_READ_NAME,
            "how": write_json_once(d / MODEL_FREE_NAME, art),
            "seat_how": write_text_once(d / SEAT_READ_NAME, req)}


# --- self-test -------------------------------------------------------------------------------
def _f0_defs(src: str) -> dict:
    import ast
    tree = ast.parse(src)
    return {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)
            and n.name in ("normalize", "grade")}


GRADER_BATTERY = (
    ("The answer is 77.", ["77"]), ("777", ["77"]), ("77.", ["77"]), ("Seventy-seven", ["77"]),
    ("March.", ["march"]), ("Marching on.", ["march"]), ("MARCH!", ["march"]),
    ("", ["77"]), ("   ", ["7", "seven"]), ("Seven.", ["7", "seven"]), ("17", ["7"]),
    ("7th", ["7"]), ("seven-day week", ["7", "seven"]), ("twenty-four hours", ["24", "twenty-four"]),
    ("twenty four", ["twenty-four"]), ("Cold.", ["cold"]), ("scold", ["cold"]),
    ("It is shut.", ["closed", "shut"]), ("closed/open", ["closed"]), ("1/2", ["1/2"]),
    ("1 / 2", ["1/2"]), ("Iron!", ["iron"]), ("ironic", ["iron"]), ("Down", ["down"]),
    ("downward", ["down"]), ("Twelve (12).", ["12", "twelve"]), ("x12y", ["12"]),
    ("I cannot determine that quantity at all.", ["77"]), ("2", ["2", "two"]),
    ("café 44", ["44"]), ("44\n45", ["45"]), ("Answer: 64", ["64"]))
GRADER_BATTERY_WANT = (True, False, True, False, True, False, True, False, False, True, False, False,
                       True, True, True, True, False, True, True, True, False, True, False, True,
                       False, True, False, False, True, True, True, True)
BANNER_LITERAL = "=== Config evaluation session ===\n"


def _f0_port_checks(f0_path: str | os.PathLike, e2a_path: str | os.PathLike) -> list[tuple[str, bool, str]]:
    """The three selftest checks comparing the grader port and the prompt form with
    f0_calibrate.py and e2a.py, as (name, ok, note); on a site where those files are absent,
    each passes on the port's pinned source hashes and its note says so (F0_ABSENT_NOTE's PIN).
    The names and the number of checks do not depend on the site."""
    import ast
    own_src = Path(__file__).read_text(encoding="utf-8")
    own = _f0_defs(own_src)
    own_seg = {k: ast.get_source_segment(own_src, v) for k, v in own.items()}
    pinned = set(own_seg) == {"normalize", "grade"} \
        and {k: _sha256_text(v) for k, v in own_seg.items()} == F0_GRADER_SRC_SHA256
    f0p, e2p = Path(f0_path), Path(e2a_path)
    f0_src = f0p.read_text(encoding="utf-8") if f0p.is_file() else None
    e2a_src = e2p.read_text(encoding="utf-8") if e2p.is_file() else None
    n_defs = ("gcal: f0_calibrate.py's two definitions (AST-extracted) are the port's text byte for byte "
              "and the same AST, and hash to the pins (on a site without f0's source: the port's pinned "
              "hashes)")
    n_bat = (f"gcal: the port and f0's exec'd grader agree on a {len(GRADER_BATTERY)}-case battery (gold "
             "variants, punctuation, numerals, case, word boundaries, empty response, gold inside a longer "
             "word -> no hit), the exec namespace holding only `re` (on a site without f0's source: the "
             "port's pinned hashes)")
    n_prompt = ("gcal: f0's prompt form and banner are the port's: f0 builds seg = f\"Task: {task}\\nResponse:\" "
                "on e2a.SESSION_BANNER (f0_calibrate.py:141-143), whose literal is session_e2a's (on a site "
                "without f0's source: the port's pinned hashes and the banner literal)")
    if f0_src is None:
        absent = f"{F0_ABSENT_NOTE} ({f0p})"
        prompt_ok = pinned and SESSION_BANNER == BANNER_LITERAL and SEGMENT_FORM == "Task: {task}\nResponse:"
        return [(n_defs, pinned, absent), (n_bat, pinned, absent), (n_prompt, prompt_ok, absent)]
    f0 = _f0_defs(f0_src)
    f0_seg = {k: ast.get_source_segment(f0_src, v) for k, v in f0.items()}
    defs_ok = (set(f0) == {"normalize", "grade"} and f0_seg == own_seg
               and all(ast.dump(f0[k]) == ast.dump(own[k]) for k in f0)
               and {k: _sha256_text(v) for k, v in f0_seg.items()} == F0_GRADER_SRC_SHA256)
    ns: dict = {"re": re}
    bat_ok = False
    if set(f0) == {"normalize", "grade"}:
        exec(compile(ast.Module(body=[f0["normalize"], f0["grade"]], type_ignores=[]),  # noqa: S102
                     str(f0p), "exec"), ns)
        got_port = [grade(r, g) for r, g in GRADER_BATTERY]
        got_f0 = [ns["grade"](r, g) for r, g in GRADER_BATTERY]
        same_norm = all(normalize(r) == ns["normalize"](r) for r, _ in GRADER_BATTERY)
        bat_ok = got_port == got_f0 and same_norm and set(ns) - {"__builtins__"} == {"re", "normalize", "grade"}
    if e2a_src is None:
        # the clone half-present: f0's form is read from f0; the banner rests on its literal
        prompt_ok = (pinned and 'seg = f"Task: {task}\\nResponse:"' in f0_src
                     and "e2a.SESSION_BANNER, seg" in f0_src and SESSION_BANNER == BANNER_LITERAL)
        p_note = f"e2a source absent on this site ({e2p}); the banner is verified by its pinned literal"
    else:
        prompt_ok = ('seg = f"Task: {task}\\nResponse:"' in f0_src and "e2a.SESSION_BANNER, seg" in f0_src
                     and 'SESSION_BANNER = "=== Config evaluation session ===\\n"' in e2a_src
                     and SESSION_BANNER == BANNER_LITERAL)
        p_note = ""
    return [(n_defs, defs_ok, ""), (n_bat, bat_ok, ""), (n_prompt, prompt_ok, p_note)]


def _selftest(chk) -> None:
    import ast
    import contextlib
    import copy
    import io
    import sys
    import tempfile
    import types
    from unittest import mock

    from . import testing

    def refuses(fn, exc=SystemExit, needle: str = "") -> bool:
        try:
            fn()
        except exc as e:
            return needle in str(e)
        return False

    pool = corr.load_pool()
    renders = corr.renders_m(pool, corr.ROSTERS_OF_RECORD)
    PROP_REL = _stages.PROPOSAL_REL
    PROP_SHA = _sha256_bytes(_stages.PROPOSAL_PATH.read_bytes())

    # the canonical G-CAL paths' state before any run of this selftest (compared at its end)
    snap0 = canonical_snapshot()

    # --- the grader port against f0's source (AST-extracted, exec'd with only `re`) -------------
    own_src = Path(__file__).read_text(encoding="utf-8")
    own = _f0_defs(own_src)
    own_seg = {k: ast.get_source_segment(own_src, v) for k, v in own.items()}
    chk("gcal: the port's normalize / grade source segments hash to F0_GRADER_SRC_SHA256",
        {k: _sha256_text(v) for k, v in own_seg.items()} == F0_GRADER_SRC_SHA256, sorted(own_seg))
    f0c = _f0_port_checks(F0_PATH, E2A_PATH)
    for name, ok, note in f0c[:2]:
        chk(name, ok, note)
    got_port = [grade(r, g) for r, g in GRADER_BATTERY]
    want = list(GRADER_BATTERY_WANT)
    chk("gcal: the battery's expected hits and misses (both directions of every case family)",
        len(want) == len(GRADER_BATTERY) and got_port == want and sum(want) and not all(want),
        [b[0] for b, g, w in zip(GRADER_BATTERY, got_port, want) if g != w])
    chk(*f0c[2])
    with tempfile.TemporaryDirectory() as tdf:
        gone = Path(tdf) / "no-jlens-clone"
        absent = _f0_port_checks(gone / "f0_calibrate.py", gone / "e2a.py")
        with mock.patch.dict(F0_GRADER_SRC_SHA256, {"grade": "0" * 64}):
            absent_bad = _f0_port_checks(gone / "f0_calibrate.py", gone / "e2a.py")
        # a synthetic f0 / e2a pair: the port's own two definitions and f0's two literal lines
        syn_f0, syn_e2a = Path(tdf) / "f0_calibrate.py", Path(tdf) / "e2a.py"
        body = ("import re\n\n\n" + own_seg["normalize"] + "\n\n\n" + own_seg["grade"] + "\n\n\n"
                "def one(task):\n    seg = f\"Task: {task}\\nResponse:\"\n"
                "    return gen(e2a.SESSION_BANNER, seg)\n")
        good_banner = 'SESSION_BANNER = "=== Config evaluation session ===\\n"\n'
        syn_f0.write_text(body, encoding="utf-8")
        syn_e2a.write_text(good_banner, encoding="utf-8")
        synth = _f0_port_checks(syn_f0, syn_e2a)
        half = _f0_port_checks(syn_f0, gone / "e2a.py")
        syn_e2a.write_text(good_banner.replace("evaluation ", ""), encoding="utf-8")
        bad_banner = _f0_port_checks(syn_f0, syn_e2a)
        syn_e2a.write_text(good_banner, encoding="utf-8")
        syn_f0.write_text(body.replace("(?![a-z0-9])", "(?![a-z])"), encoding="utf-8")
        bad_grader = _f0_port_checks(syn_f0, syn_e2a)
    oks = {nm: [ok for _, ok, _ in v] for nm, v in (("absent", absent), ("absent_bad", absent_bad),
                                                   ("synth", synth), ("half", half),
                                                   ("bad_banner", bad_banner), ("bad_grader", bad_grader))}
    chk("gcal: on a site without the jlens clone (f0 and e2a pointed at a missing temp path) the three f0 "
        "checks keep their names and count and pass on the port's pinned hashes, each noting 'f0 source "
        "absent on this site; the port is verified by its pinned hash'; they fail when the pin is broken; "
        "a synthetic faithful f0 / e2a passes in present mode, and a tampered grader (defs, battery) or "
        "banner (prompt) fails there",
        [n for n, _, _ in absent] == [n for n, _, _ in f0c] and len(absent) == 3
        and oks["absent"] == [True, True, True]
        and all(note.startswith(F0_ABSENT_NOTE) for _, _, note in absent)
        and oks["absent_bad"] == [False, False, False]
        and oks["synth"] == [True, True, True] and all(note == "" for _, _, note in synth)
        and oks["half"] == [True, True, True] and half[2][2].startswith("e2a source absent on this site")
        and oks["bad_banner"] == [True, True, False] and oks["bad_grader"] == [False, False, True], oks)

    # --- (1) the model-free artifact ----------------------------------------------------------
    art = model_free_artifact()
    chk("gcal: model_free_artifact computes the 0.12 replay first (m:358); the remaining model-free items "
        "follow (the roster assertion ahead of m:358's listed position, being model-free); JSON-native",
        art["computation_order"] == ["f1_012", "f1_012_covariate_quote", "renders_of_record",
                                     "roster_assertion", "conditions", "provenance"]
        and _resume.json_text(art) == _resume.json_text(model_free_artifact()), art["computation_order"])
    chk("gcal: (a) f1_012 is corr.f1_012_replay as is: sha16 2c2c227395ea9f2d, 31 changed, cond1 4/16, "
        "cond2 16/16; the covariate quoted as stored, 0.078125 = +.078",
        art["f1_012"] == corr.f1_012_replay(pool) and art["f1_012"]["renders_sha16"] == "2c2c227395ea9f2d"
        and art["f1_012"]["n_changed"] == 31 and art["f1_012"]["n_cond1"] == 4
        and art["f1_012"]["n_cond2"] == 16 and art["f1_012_covariate_quote"]["stored"] == "0.078125"
        and art["f1_012_covariate_quote"]["as_quoted_in_m176"] == "+.078",
        art["f1_012_covariate_quote"])
    chk("gcal: the covariate quote STOPs on any other stored figure (0.078 rounds to +.078 but is not "
        "the figure of record; 0.0785 rounds to +.079)",
        refuses(lambda: _covariate_quote("0.078"), GcalStop)
        and refuses(lambda: _covariate_quote("0.0785"), GcalStop)
        and _covariate_quote("0.078125")["stored"] == "0.078125")
    ror = art["renders_of_record"]
    its = ror["items"]
    chk("gcal: (b) n_eligible is m:176's list, k = [3,3,3,3,4,3,3,7,3,3,4,3,3,3,3,3] summing to 54, one "
        "roster skip at item 7",
        ror["n_eligible"] == list(SPEC_N_ELIGIBLE) and ror["k"] == [3, 3, 3, 3, 4, 3, 3, 7, 3, 3, 4, 3, 3,
                                                                     3, 3, 3]
        and ror["k_sum"] == 54 and ror["roster_skips"] == {"7": 1}, (ror["k"], ror["roster_skips"]))
    diffs_ok = all(x["changed_positions"] == [j for j, (a, b) in enumerate(zip(x["clean"], x["render"]))
                                              if a != b] and x["n_changed"] == len(x["changed_positions"])
                   == x["k"] and x["cond1"] and x["cond2"] and x["clean"] == pool[x["i"]]["task"]
                   for x in its)
    chk("gcal: (b) per item the clean task, the corrupt_m render, changed positions = the byte diff (count "
        "= k), cond1 and cond2 true; renders == corr.renders_m",
        diffs_ok and [x["render"] for x in its] == renders and len(its) == 16)
    chk("gcal: (b) items 5/11/15 render verbatim (m:176) and exclude their quoted operands; no other item "
        "has a span",
        (its[5]["render"], its[11]["render"], its[15]["render"])
        == ("Writa the oppcsite oc 'hot'.", "Writo the oppssitu of 'up'.", "Wtite thn opposite on 'open'.")
        and [x["operand_spans"] for x in its if x["operand_spans"]]
        == [[{"start": 22, "end": 27, "text": "'hot'"}], [{"start": 22, "end": 26, "text": "'up'"}],
            [{"start": 22, "end": 28, "text": "'open'"}]]
        and all(not x["operand_spans"] for x in its if x["i"] not in (5, 11, 15)))
    full = _sha256_text("\n".join(renders))
    chk("gcal: (b) renders_sha256 = sha256 of the newline-joined renders; its first 16 hex = "
        "corr.renders_sha", ror["renders_sha256"] == full and ror["renders_sha16"] == full[:16]
        == corr.renders_sha(renders), full)
    bad_pool = [dict(it) for it in pool]
    bad_pool[3] = {"task": "Compute sixty divided by 5.", "gold": ["12", "twelve"]}
    chk("gcal: the renders of record STOP when they disagree with m:176's figures (a pool whose item 3 "
        "has more eligible letters; model_free_artifact STOPs on it at the 0.12 replay, which comes "
        "first), and not on the pool of record; an unbalanced quote is refused",
        refuses(lambda: _renders_of_record(bad_pool), GcalStop, "disagree with m:176")
        and refuses(lambda: model_free_artifact(bad_pool), GcalStop, "0.12 renders sha16")
        and _renders_of_record(pool)["k_sum"] == 54
        and refuses(lambda: operand_spans("it's 'x'"), ValueError))
    ra = art["roster_assertion"]
    chk("gcal: (c) the roster assertion on the renders is clean for both rosters (substring, case-"
        "insensitive); the clean tasks beside are clean too",
        ra["pass"] is True and ra["renders"] == {"qwen": [], "olmo": []}
        and ra["clean_tasks_for_reference"] == {"qwen": [], "olmo": []}
        and ra["rosters"]["olmo"] == ["amber", "copper", "granite", "maple", "quartz", "saddle", "velvet",
                                      "walnut"], ra["rosters"])
    planted = list(renders)
    planted[4] = "State the PRISMatic number."
    hits = roster_hits(planted, corr.QWEN_ROSTER)
    chk("gcal: roster_hits fires on a planted roster substring (upper case, inside a word) and only "
        "there; _roster_assertion STOPs on it",
        hits == [{"i": 4, "word": "prism"}] and roster_hits(planted, corr.OLMO_ROSTER) == []
        and refuses(lambda: _roster_assertion(pool, planted), GcalStop, "roster word"), hits)
    cd = art["conditions"]
    chk("gcal: (d) conditions (1) and (2) PASS 16/16; (3) and (4) pending",
        cd["1"]["verdict"] == cd["2"]["verdict"] == "PASS" and cd["1"]["n_pass"] == cd["2"]["n_pass"] == 16
        and cd["3"] == COND3_PENDING and cd["4"] == COND4_PENDING, cd["1"])
    fake = [{"i": 0, "cond1": False, "cond2": True}, {"i": 1, "cond1": True, "cond2": False}]
    chk("gcal: (d) a condition FAILs naming its failing items (two changes; k above floor(n/2))",
        _condition(fake, "cond1", "")["failing_items"] == [0]
        and _condition(fake, "cond2", "")["verdict"] == "FAIL")
    pv = art["provenance"]
    chk("gcal: (e) provenance: package sha256, pools file sha256 (8547d9a11ba55b95...), served pool "
        "sha16, the v1.11 proposal's sha256",
        pv["package_sha256"] == _resume.package_sha256() and pv["pools_file_sha256"].startswith(
            corr.POOLS_SHA16) and pv["pool_sha16"] == _resume.pool_sha16(pool)
        and pv["proposal_file"] == PROP_REL and pv["proposal_sha256"] == PROP_SHA, pv["proposal_sha256"][:16])

    # --- (4) the seat read request ------------------------------------------------------------
    doc = seat_read_request(art)
    a_at, b_at = doc.index(SEAT_A), doc.index(SEAT_B)
    sec_a = doc[a_at:b_at]
    pos_a = [sec_a.index(f"{i}. `{r}`") for i, r in enumerate(renders)]
    count_rx = re.compile(r"\b\d+\s+of\s+16\b|provisional", re.I)

    def clean_before_key(text: str) -> list[int]:
        head = text[:text.index(SEAT_B)]
        return [i for i, it in enumerate(pool) if it["task"] in head]

    def blind_problems(text: str) -> list[str]:
        # the blind-read order: sha line, the recording instruction, section A, section B;
        # no clean task and no provisional / expected count before section B
        probs = []
        if text.splitlines()[2:3] != [f"renders_sha256: `{full}`"]:
            probs.append("renders_sha256 is not the third line")
        at = [text.find(x) for x in (SEAT_INSTRUCTION_HEAD, SEAT_INSTRUCTION, SEAT_A, SEAT_B)]
        if -1 in at or at != sorted(at) or text.find(f"renders_sha256: `{full}`") > at[0]:
            probs.append(f"order (sha, instruction head, instruction, A, B) broken: {at}")
        if -1 not in at:
            if clean_before_key(text):
                probs.append("a clean task precedes the key")
            hit = count_rx.search(text[:at[3]])
            if hit:
                probs.append(f"{hit.group(0)!r} precedes section B")
        return probs

    chk("gcal: the seat read request (blind read): the renders' sha256 first, then the recording instruction "
        "('For each render, write down the task as you read it and its answer, before opening section B.'), "
        "then the 16 renders ALONE numbered 0-15 in order, then the key; no clean task, no 'N of 16' and no "
        "'provisional' text before the key, and no '16 of 16' anywhere",
        blind_problems(doc) == [] and pos_a == sorted(pos_a) and len(pos_a) == 16 and sec_a.count("`") == 32
        and doc.index(SEAT_INSTRUCTION) < a_at < b_at and "16 of 16" not in doc
        and "provisional" not in doc.lower(), blind_problems(doc))
    swapped = doc[:a_at] + doc[b_at:] + "\n" + sec_a
    instr_after = doc.replace(SEAT_INSTRUCTION, "", 1).replace(SEAT_B, SEAT_B + "\n\n" + SEAT_INSTRUCTION, 1)
    told_in_a = doc.replace(SEAT_A + "\n", SEAT_A + "\nThe seat's provisional reads found 16 of 16.\n", 1)
    told_in_head = doc.replace(SEAT_INSTRUCTION_HEAD, "Expected: 16 of 16 recoverable.\n\n" + SEAT_INSTRUCTION_HEAD, 1)
    told_count = doc.replace(SEAT_A + "\n", SEAT_A + "\n(14 of 16 were recoverable before.)\n", 1)
    chk("gcal: the blind-read check fires on a request whose key precedes the renders, whose recording "
        "instruction sits after section A, or which states a count ('16 of 16', 'provisional', '14 of 16') "
        "in section A or above it",
        len(clean_before_key(swapped.replace(SEAT_B, "## B0", 1) + "\n" + SEAT_B)) == 16
        and all(blind_problems(t) for t in (instr_after, told_in_a, told_in_head, told_count))
        and len({doc, instr_after, told_in_a, told_in_head, told_count}) == 5)
    key = doc[b_at:]
    chk("gcal: the key carries each item's clean task, gold list, k and changed positions, and condition "
        "(3)'s instruction in m:176's words; no roster word anywhere",
        COND3_WORDS in key and all(f"- clean task: `{it['task']}`" in key and f"- k: {x['k']} " in key
                                   for it, x in zip(pool, its))
        and "- gold: `closed`, `shut`" in key and "- changed positions: " in key
        and not roster_hits([doc], corr.QWEN_ROSTER) and not roster_hits([doc], corr.OLMO_ROSTER))

    # the key's per-item lines, rebuilt independently: positions from a byte diff of the clean
    # task and corr.renders_m's render, n_eligible from m:176's literal list, k from m:176's
    # formula, the operand span from a regex over the clean task
    n_el_m176 = (6, 19, 19, 13, 24, 14, 10, 45, 19, 10, 24, 14, 6, 19, 10, 14)

    def key_lines(i: int) -> list[str]:
        clean, rend = pool[i]["task"], renders[i]
        cb, rb = clean.encode("ascii"), rend.encode("ascii")
        if len(cb) != len(rb):
            return ["length differs"]
        pos = ", ".join(f"{j} ({chr(cb[j])}>{chr(rb[j])})" for j in range(len(cb)) if cb[j] != rb[j])
        n = n_el_m176[i]
        k_ = min(max(floor(Fraction(15, 100) * n + Fraction(1, 2)), 3), n // 2)
        spans = ", ".join(f"`{m.group(0)}` [{m.start()}, {m.end()})" for m in re.finditer(r"'[^']*'", clean))
        return [f"### Item {i}", f"- render: `{rend}`", f"- clean task: `{clean}`",
                f"- k: {k_} (n_eligible {n})", f"- changed positions: {pos}",
                f"- operand span excluded: {spans or 'none'}"]

    def key_problems(text: str) -> list[str]:
        kt = text[text.index(SEAT_B):]
        probs = []
        for i in range(16):
            head = f"### Item {i}\n"
            if head not in kt:
                probs.append(f"item {i}: no section")
                continue
            sec = kt[kt.index(head):]
            nxt = sec.find("### Item ", len(head))
            sec_lines = (sec if nxt == -1 else sec[:nxt]).splitlines()
            probs += [f"item {i}: missing {ln!r}" for ln in key_lines(i) if ln not in sec_lines]
        return probs

    pos0 = key_lines(0)[4]
    pos0_shift = "- changed positions: " + ", ".join(
        f"{int(t.split(' ')[0]) + 1} {t.split(' ')[1]}" for t in pos0[len("- changed positions: "):].split(", "))
    pos0_swap = re.sub(r"\((\w)>(\w)\)", r"(\2>\1)", pos0)
    k3 = key_lines(3)[3]
    muts = {"render shows clean": doc.replace(f"- render: `{renders[0]}`", f"- render: `{pool[0]['task']}`", 1),
            "positions off by one": doc.replace(pos0, pos0_shift, 1),
            "positions render>clean": doc.replace(pos0, pos0_swap, 1),
            "n_eligible prints k": doc.replace(k3, f"- k: {its[3]['k']} (n_eligible {its[3]['k']})", 1),
            "operand span blank": doc.replace("- operand span excluded: `'hot'` [22, 27)",
                                              "- operand span excluded: none", 1)}
    chk("gcal: the key's per-item lines -- '- render:', the changed positions (built independently from a "
        "byte diff of clean vs render, clean>rendered), k and n_eligible (m:176's list), the operand span "
        "(items 5, 11, 15; 'none' elsewhere) -- are exact for all 16 items; the check fires on a render line "
        "showing the clean task, positions off by one or reversed, n_eligible printing k, a blank span",
        key_problems(doc) == [] and pos0 == "- changed positions: 1 (o>l), 2 (m>o), 5 (t>i)"
        and all(m != doc and key_problems(m) for m in muts.values()),
        (key_problems(doc)[:2], [n for n, m in muts.items() if m == doc or not key_problems(m)]))
    m176 = _stages.PROPOSAL_PATH.read_text(encoding="utf-8").splitlines()[175]
    quoted = (COND3_WORDS, "(3) or (4) failing → STOP and re-specify",
              "the read of record is repeated at G-CAL on the renders of record")
    chk("gcal: every phrase the request quotes from m:176 is m:176's own text (and appears in the key)",
        m176.startswith("**2.3 Dose") and all(q in m176 and f"\"{q}\"" in key for q in quoted)
        and "(3) or (4) failing -> STOP" not in m176, [q for q in quoted if q not in m176])

    # --- write-once -----------------------------------------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "a.json"
        w1 = write_json_once(p, art)
        w2 = write_json_once(p, copy.deepcopy(art))
        before = p.read_bytes()
        alt = copy.deepcopy(art)
        alt["conditions"]["3"] = "PASS"
        refused = refuses(lambda: write_json_once(p, alt), GcalRefusal, "never overwritten")
        chk("gcal: an artifact is written once, accepted when identical, refused (and left untouched) when "
            "different", (w1, w2) == ("written", "identical") and refused and p.read_bytes() == before
            and not list(Path(td).glob("*.tmp")))

    # --- condition (4) on exact Fractions -------------------------------------------------------
    c = {(hc, hx): condition_4(hc, hx) for hc, hx in ((60, 45), (60, 44), (52, 45), (52, 44), (64, 48),
                                                       (64, 47))}
    chk("gcal: condition (4) at its exact boundaries -- 45/64 passes .70 and 44/64 fails; 3/4 x 60/64 "
        "is met at equality by 45/64 and missed by 44/64; 3/4 x 64/64 met by 48/64, missed by 47/64",
        [c[k]["verdict"] for k in c] == ["PASS", "FAIL", "PASS", "FAIL", "PASS", "FAIL"]
        and [(c[k]["abs_pass"], c[k]["rel_pass"]) for k in c]
        == [(True, True), (False, False), (True, True), (False, True), (True, True), (True, False)]
        and c[(60, 45)]["rel_bar"] == "45/64" and c[(64, 48)]["rel_bar"] == "3/4",
        [c[k]["verdict"] for k in c])
    chk("gcal: the covariate is clean minus corrupted (f0's sign), exact, with a 4-dp half-up display",
        c[(52, 45)]["covariate"]["fraction"] == "7/64" and c[(52, 45)]["covariate"]["decimal_4dp"] == "+0.1094"
        and condition_4(44, 48)["covariate"]["decimal_4dp"] == "-0.0625"
        and dec4(Fraction(1, 20000)) == "0.0001" and dec4(Fraction(1, 20001)) == "0.0000"
        and dec4(Fraction(5, 64)) == "0.0781", c[(52, 45)]["covariate"])
    chk("gcal: condition (4)'s bars bind at exact equality and not one hit below (n = 100, where .70 and "
        ".75 are attainable): 70/100 passes .70, 69/100 fails; 3/4 x 96/100 = 72/100 met by 72, missed by 71",
        [condition_4(80, 70, 100)["verdict"], condition_4(80, 69, 100)["verdict"],
         condition_4(96, 72, 100)["verdict"], condition_4(96, 71, 100)["verdict"]]
        == ["PASS", "FAIL", "PASS", "FAIL"] and condition_4(80, 69, 100)["rel_pass"] is True
        and condition_4(96, 71, 100)["abs_pass"] is True)
    chk("gcal: condition_4 refuses floats, bools and out-of-range hits",
        refuses(lambda: condition_4(60.0, 45), TypeError) and refuses(lambda: condition_4(True, 45), TypeError)
        and refuses(lambda: condition_4(65, 45), ValueError))

    # --- key set --------------------------------------------------------------------------------
    ks = key_set()
    chk("gcal: the key set is 128 (pool, i, s, seed) in f0's order, seed = crc32('m-cal|pool|i|s') % 2**31 "
        "= keys.cal_seed, all distinct; CAL_POOLS is f0's two literals",
        len(ks) == N_GEN == 128 and [(k["pool"], k["i"], k["s"]) for k in ks]
        == [(p, i, s) for p in ("CORR_clean", "CORR_corrupted") for i in range(16) for s in range(4)]
        and all(k["seed"] == zlib.crc32(f"m-cal|{k['pool']}|{k['i']}|{k['s']}".encode()) % 2**31
                for k in ks) and len({k["seed"] for k in ks}) == 128, key_set_sha256(ks)[:16])
    with mock.patch.object(keys, "CAL_POOLS", ("CORR_clean", "CORR_corrupt")):
        a1 = refuses(key_set, GcalRefusal, "CAL_POOLS")
    with mock.patch.object(keys, "cal_seed", lambda p, i, s: 7):
        a2 = refuses(key_set, GcalRefusal, "crc32")
    chk("gcal: key_set refuses a pool literal other than f0's and a cal_seed that is not m:176's form",
        a1 and a2)

    # --- completability on the scripted stub ------------------------------------------------------
    seg_key = {(f"Task: {_task_of(k, pool, renders)}\nResponse:", k["seed"]): k for k in ks}

    def plan(h_clean: int, h_corr: int, *, boom_at: int | None = None):
        n = {"calls": 0}

        def f(call):
            n["calls"] += 1
            if boom_at is not None and n["calls"] == boom_at:
                raise KeyboardInterrupt("selftest: killed mid-run")
            k = seg_key[(call["segment"], call["seed"])]
            h = h_clean if k["pool"] == "CORR_clean" else h_corr
            if k["i"] * 4 + k["s"] < h:
                return {"text": f"Verily {pool[k['i']]['gold'][0]}.", "n_tok": 3}
            return {"text": "Zqxj unknown.", "n_tok": 2}
        return f

    def stub(h_clean=64, h_corr=64, **kw):
        ad = testing.ScriptedAdapter("m-gcal-stub")
        ad.load(plan(h_clean, h_corr, **kw))
        return ad

    def run(ad, out, *, resume=False, **kw):
        buf = io.StringIO()
        res = exc = None
        with contextlib.redirect_stdout(buf):
            try:
                res = run_completability(ad, out_path=out, resume=resume, proposal_file=PROP_REL,
                                         proposal_sha256=PROP_SHA, **kw)
            except (SystemExit, KeyboardInterrupt) as e:
                exc = e
        return res, exc, buf.getvalue()

    def scratch(td: str, name: str) -> Path:
        d = Path(td) / name
        d.mkdir()
        write_json_once(d / MODEL_FREE_NAME, art)
        return d / COMPLETABILITY_NAME

    line_rx = re.compile(r"gcal (CORR_clean|CORR_corrupted) i=(\d+) s=([0-3]) (hit|miss) n_tok=(\d+)")
    with tempfile.TemporaryDirectory() as td:
        outs = {}
        for nm, (hc, hx) in {"pass70": (52, 45), "fail70": (52, 44), "pass75": (64, 48),
                             "fail75": (64, 47)}.items():
            ad = stub(hc, hx)
            outs[nm] = (ad,) + run(ad, scratch(td, nm))
        verdicts = {nm: (o[1] or {}).get("verdict") for nm, o in outs.items()}
        def art_of(res) -> dict:
            # the artifact a run reported, or {} when the run returned nothing (a check fails)
            if not res or not Path(res.get("artifact", "")).is_file():
                return {}
            return json.loads(Path(res["artifact"]).read_text(encoding="utf-8"))

        a_pass = art_of(outs["pass70"][1])
        chk("gcal: four scripted 128-generation runs end at condition (4)'s boundaries -- corrupted 45/64 "
            "PASS vs 44/64 FAIL against .70 (clean 52/64); 48/64 PASS vs 47/64 FAIL against 3/4 x 64/64",
            verdicts == {"pass70": "PASS", "fail70": "FAIL", "pass75": "PASS", "fail75": "FAIL"}
            and a_pass["accuracy"]["CORR_clean"]["fraction"] == "13/16"
            and a_pass["accuracy"]["CORR_corrupted"]["fraction"] == "45/64"
            and a_pass["covariate"]["fraction"] == "7/64"
            and art_of(outs["fail75"][1]).get("condition_4", {}).get("rel_pass") is False,
            verdicts)
        ad, res, _exc, out = outs["pass70"]
        calls_ok = len(ad.calls) == 128 and all(
            c["prefix"] == SESSION_BANNER and c["injections"] == () and c["cached"] is False
            and c["temp"] == 0.7 and c["max_tokens"] == 60 and c["stop_newline"] is True
            and c["ban_ids"] == tuple(testing.qwen_kit().ban_ids) for c in ad.calls)
        segs_ok = [(c["segment"], c["seed"]) for c in ad.calls] == [
            (f"Task: {(pool[k['i']]['task'] if k['pool'] == 'CORR_clean' else renders[k['i']])}\nResponse:",
             k["seed"]) for k in ks]
        chk("gcal: every generation is SESSION_BANNER + 'Task: {task}\\nResponse:' (clean task / render of "
            "record), injections=(), cached=False, TEMP 0.7, STOP_CAP 60, newline stop, the frozen e2a ban "
            "ids, the key's seed, in key order", calls_ok and segs_ok)
        recs = a_pass.get("records", [])
        chk("gcal: each record is {pool, i, seed_index, seed, task, text, n_tok, cap_hit, stop_reason, hit} "
            "with hit = f0's grade of the text against the item's gold",
            len(recs) == 128 and all(tuple(sorted(r)) == tuple(sorted(RECORD_KEYS))
                                     and r["hit"] is grade(r["text"], pool[r["i"]]["gold"]) for r in recs)
            and sum(r["hit"] for r in recs) == 97)
        lines = out.splitlines()
        gl = [ln for ln in lines if ln.startswith("gcal ") and line_rx.fullmatch(ln)]
        chk("gcal: stdout -- one line per generation (no response text), then the per-pool accuracy, "
            "condition (4) and covariate lines and the verdict with the artifact path",
            len(gl) == 128 and "Verily" not in out and "Zqxj" not in out
            and "gcal accuracy CORR_clean 52/64 = 13/16 (0.8125)" in lines
            and "gcal accuracy CORR_corrupted 45/64 = 45/64 (0.7031)" in lines
            and any(ln.startswith("gcal condition (4): PASS -- corrupted 45/64 >= 7/10: yes; >= 3/4 x "
                                  "clean = 39/64: yes") for ln in lines)
            and any(ln.startswith("gcal covariate (clean minus corrupted, f0's sign): 7/64 = +0.1094")
                    for ln in lines) and lines[-1].startswith("G-CAL completability (Qwen): PASS; artifact ")
            and (outs["fail70"][3].splitlines() or [""])[-1].startswith(
                "G-CAL completability (Qwen): FAIL -- STOP and re-specify (m:176)"), (lines or [""])[-1][:70])
        prov = a_pass.get("provenance", [])
        idp = a_pass.get("identity", {})
        chk("gcal: the artifact carries the identity (key set, proposal, renders, ban list, package, "
            "backend, temp, cap), the adapter's provenance verbatim, no gate line on the stub",
            idp.get("key_set_sha256") == key_set_sha256(ks) and idp.get("proposal_sha256") == PROP_SHA
            and idp.get("renders_sha256") == full and idp.get("ban_sha256") == _audit.E2A_BAN_LIST_SHA256
            and idp.get("temp") == "0.7" and idp.get("stop_cap") == 60
            and len(prov) == 1 and prov[0]["record"] == _resume.provenance_record(ad.provenance())
            and prov[0]["launched"] == 128 and prov[0]["gate"] is None
            and tuple(sorted(idp)) == tuple(sorted(IDENTITY_KEYS)))

        # grader coverage: hits on a non-first gold variant (items with several), misses on items
        # 7 and 9 (whose gold sits inside the task text), a restatement of the task on 7 and 9,
        # graded as f0's grade grades it (True: the gold is a word of the task), exact hit counts
        multi, in_task = (1, 3, 4, 10, 13, 15), (7, 9)
        assert all(len(pool[i]["gold"]) > 1 for i in multi) and all(
            len(pool[i]["gold"]) == 1 for i in range(16) if i not in multi)

        def cov_kind(k: Mapping[str, Any]) -> str:
            i, s_ = k["i"], k["s"]
            if i in multi:
                return ("alt", "alt", "first", "miss")[s_]
            if i in in_task:
                return ("miss", "restate", "miss", "first")[s_]
            if k["pool"] == "CORR_corrupted" and i == 0 and s_ == 2:
                return "miss"
            return ("first", "first", "first", "miss")[s_]

        def cov_plan(call):
            k = seg_key[(call["segment"], call["seed"])]
            g = pool[k["i"]]["gold"]
            return {"text": {"alt": f"It is {g[-1]}.", "first": f"Verily {g[0]}.", "miss": "Zqxj unknown.",
                             "restate": _task_of(k, pool, renders)}[cov_kind(k)], "n_tok": 4}

        # f0's grade on a restated task, items 7 and 9, both pools: True (checked against
        # f0_calibrate.py's exec'd grade at the build; the port is f0's text byte for byte)
        want_hit = {"alt": True, "first": True, "miss": False, "restate": True}
        kinds = [cov_kind(k) for k in ks]

        def cov_problems(a: Mapping[str, Any]) -> list[str]:
            rs = a.get("records", [])
            if len(rs) != 128:
                return [f"{len(rs)} records"]
            probs = []
            hits = {p_: a["accuracy"][p_]["hits"] for p_ in keys.CAL_POOLS}
            if hits != {"CORR_clean": 46, "CORR_corrupted": 45}:
                probs.append(f"hits {hits}, want clean 46, corrupted 45")
            if [r["hit"] for r in rs] != [want_hit[x] for x in kinds]:
                probs.append("a record's hit is not its scripted kind's")
            if not all(r["hit"] is grade(r["text"], pool[r["i"]]["gold"]) for r in rs):
                probs.append("a record's hit is not f0's grade of its text")
            alt = [r for r, x in zip(rs, kinds) if x == "alt"]
            if len(alt) != 24 or not all(r["hit"] is True and not grade(r["text"], pool[r["i"]]["gold"][:1])
                                         for r in alt):
                probs.append("the non-first-variant hits")
            rst = [r for r, x in zip(rs, kinds) if x == "restate"]
            if [(r["i"], r["text"] == r["task"], r["hit"]) for r in rst] != [(7, True, True), (9, True, True)] * 2:
                probs.append("the restated tasks on items 7 and 9")
            if [r["hit"] for r, x in zip(rs, kinds) if x == "miss" and r["i"] in in_task] != [False] * 8:
                probs.append("the misses on items 7 and 9")
            if a.get("verdict") != "PASS" or a["covariate"]["fraction"] != "1/64":
                probs.append(f"verdict {a.get('verdict')}, covariate {a['covariate']['fraction']}")
            return probs

        ad_cov = testing.ScriptedAdapter("m-gcal-stub")
        ad_cov.load(cov_plan)
        r_cov, e_cov, _ = run(ad_cov, scratch(td, "grader_cov"))
        a_cov = art_of(r_cov)
        orig_grade = grade
        ad_first = testing.ScriptedAdapter("m-gcal-stub")
        ad_first.load(cov_plan)
        with mock.patch(f"{__name__}.grade", lambda t, g: orig_grade(t, g[:1])):
            r_first, e_first, _ = run(ad_first, scratch(td, "grader_first_only"))
        a_first = art_of(r_first)
        # the call-site mutation that grades the prompt's task with the text, re-derived on the
        # records (hits and per-pool counts recomputed)
        a_tt = copy.deepcopy(a_cov) if a_cov else {}
        if a_tt:
            for r in a_tt["records"]:
                r["hit"] = orig_grade(r["task"] + " " + r["text"], pool[r["i"]]["gold"])
            for p_ in keys.CAL_POOLS:
                a_tt["accuracy"][p_]["hits"] = sum(1 for r in a_tt["records"] if r["pool"] == p_ and r["hit"])
        chk("gcal: grader coverage on a scripted 128-generation run -- hits on a non-first gold variant "
            "('seven', 'twelve', 'three', 'two', 'twenty-four', 'shut': 24), misses on items 7 and 9 whose gold "
            "sits in the task text (8), a restatement of the task on 7 and 9 graded as f0's grade grades it "
            "(True, 4); exactly 46/64 clean and 45/64 corrupted hits; the check fires on a grader narrowed to the "
            "first gold (run through run_completability) and on one that grades the task with the text",
            e_cov is None and cov_problems(a_cov) == [] and len(ad_cov.calls) == 128
            and e_first is None and bool(a_first) and any("hits" in x for x in cov_problems(a_first))
            and a_first["accuracy"]["CORR_clean"]["hits"] == 34
            and bool(a_tt) and any("hits" in x for x in cov_problems(a_tt))
            and a_tt["accuracy"]["CORR_clean"]["hits"] == 50,
            (cov_problems(a_cov)[:2], (a_first.get("accuracy") or {}).get("CORR_clean")))

        # resume: killed at call 51, refused without --resume, skip-only with it
        o = scratch(td, "resume")
        ad1 = stub(52, 45, boom_at=51)
        _r1, e1, _ = run(ad1, o)
        ckp = o.parent / "ckpt" / CKPT_NAME
        mid = json.loads(ckp.read_text())
        ad2 = stub(52, 45)
        _r2, e2, _ = run(ad2, o)
        ad3 = stub(52, 45)
        r3, e3, out3 = run(ad3, o, resume=True)
        a3 = art_of(r3)
        chk("gcal: a run killed mid-generation keeps its 50 records on disk; a re-run without --resume is "
            "refused (no generation); --resume generates exactly the other 78 (skip-only) and reaches the "
            "uninterrupted run's records and verdict",
            isinstance(e1, KeyboardInterrupt) and len(mid["records"]) == 50
            and isinstance(e2, GcalRefusal) and "CHECKPOINT EXISTS" in str(e2) and not ad2.calls
            and e3 is None and len(ad3.calls) == 78
            and [c["seed"] for c in ad3.calls] == [k["seed"] for k in ks[50:]]
            and a3["records"] == recs and a3["verdict"] == "PASS"
            and [e["launched"] for e in a3["provenance"]] == [50, 78]
            and "gcal resume: 50 of 128 generations on disk, skipped (skip-only)" in out3, (e2, len(ad3.calls)))
        ad4 = stub(52, 45)
        r4, e4, _ = run(ad4, o, resume=True)
        ck_after = json.loads(ckp.read_text())
        chk("gcal: a resume of a complete checkpoint generates nothing and re-derives the identical artifact "
            "(its zero-launch provenance entry stays in the checkpoint only)",
            e4 is None and not ad4.calls and (r4 or {}).get("artifact_write") == "identical"
            and [e["launched"] for e in ck_after["provenance"]] == [50, 78, 0])

        # resume refusals: backend, proposal, a regraded record, an out-of-order record
        def tampered(mutate) -> tuple:
            d = Path(td) / f"t{len(list(Path(td).iterdir()))}"
            d.mkdir()
            write_json_once(d / MODEL_FREE_NAME, art)
            (d / "ckpt").mkdir()
            ck = copy.deepcopy(mid)
            mutate(ck)
            _resume.atomic_write_json(d / "ckpt" / CKPT_NAME, ck)
            ad = stub(52, 45)
            return ad, run(ad, d / COMPLETABILITY_NAME, resume=True)

        def other_backend():
            ad = stub(52, 45)
            real = ad.provenance
            ad.provenance = lambda: {**real(), "platform": "selftest-backend-Y"}
            return ad

        d5 = Path(td) / "backend"
        d5.mkdir()
        write_json_once(d5 / MODEL_FREE_NAME, art)
        (d5 / "ckpt").mkdir()
        _resume.atomic_write_json(d5 / "ckpt" / CKPT_NAME, mid)
        ad5 = other_backend()
        _r5, e5, _ = run(ad5, d5 / COMPLETABILITY_NAME, resume=True)
        cases = {
            "proposal": lambda ck: ck["identity"].__setitem__("proposal_sha256", "2" * 64),
            "renders": lambda ck: ck["identity"].__setitem__("renders_sha256", "3" * 64),
            "regraded": lambda ck: ck["records"][7].__setitem__("hit", not ck["records"][7]["hit"]),
            "out of order": lambda ck: ck["records"].__setitem__(slice(3, 5), ck["records"][4:2:-1]),
            "retexted": lambda ck: ck["records"][0].__setitem__("text", "Zqxj unknown."),
        }
        res_t = {nm: tampered(m) for nm, m in cases.items()}
        mm = {nm: (isinstance(r[1][1], GcalRefusal), str(r[1][1])[:60], len(r[0].calls)) for nm, r in res_t.items()}
        chk("gcal: a resume is refused on another backend, another proposal hash, other renders, a record "
            "whose grade disagrees with its text, and records out of key order -- nothing generated",
            isinstance(e5, GcalRefusal) and "backend_identifier" in str(e5) and not ad5.calls
            and all(ok and n == 0 for ok, _, n in mm.values())
            and "proposal_sha256" in mm["proposal"][1] + str(res_t["proposal"][1][1]), mm)

        def other_value(v: Any) -> Any:
            if type(v) is int:
                return v + 1
            if type(v) is str and v:
                return ("1" if v[0] != "1" else "2") + v[1:]
            raise AssertionError(f"selftest: no other value for {v!r}")

        def ident_case(key: str, how: str = "change"):
            def m(ck):
                if how == "change":
                    ck["identity"][key] = other_value(ck["identity"][key])
                elif how == "drop":
                    del ck["identity"][key]
                else:
                    ck["identity"][key] = 1
            return m

        id_cases = {k_: ident_case(k_) for k_ in IDENTITY_KEYS}
        id_res = {}
        for k_, m_ in id_cases.items():
            ad_, (_rr, e_, _oo) = tampered(m_)
            id_res[k_] = (isinstance(e_, GcalRefusal) and "CHECKPOINT MISMATCH" in str(e_)
                          and f"on ['{k_}']" in str(e_) and not ad_.calls)
        ad_x, (_rx, e_x, _ox) = tampered(ident_case("zzz_extra", "add"))
        ad_y, (_ry, e_y, _oy) = tampered(ident_case("segment_form", "drop"))
        chk(f"gcal: a resume is refused on a checkpoint whose identity differs in any ONE of its "
            f"{len(IDENTITY_KEYS)} keys (key_set_sha256 and package_sha256 among them), the message naming "
            f"exactly that key; and on an identity with an extra or a missing key -- nothing generated",
            len(IDENTITY_KEYS) == 15 and {"key_set_sha256", "package_sha256"} <= set(id_res)
            and all(id_res.values())
            and isinstance(e_x, GcalRefusal) and "on ['zzz_extra']" in str(e_x) and not ad_x.calls
            and isinstance(e_y, GcalRefusal) and "on ['segment_form']" in str(e_y) and not ad_y.calls,
            [k_ for k_, ok in id_res.items() if not ok])
        ad_s, (_rs, e_s, _os) = tampered(lambda ck: ck["records"][5].__setitem__("seed", ck["records"][5]["seed"] + 1))
        ad_k, (_rk, e_k, _ok) = tampered(lambda ck: ck["records"][9].__setitem__("task", renders[2]))
        seed_rec = copy.deepcopy(mid["records"][5])
        seed_rec["seed"] += 1
        task_rec = copy.deepcopy(mid["records"][9])
        task_rec["task"] = renders[2]
        chk("gcal: a record whose seed alone (record 5) or task alone (record 9: the render of its own item) is "
            "altered, its text still graded consistently, is refused by the key-prefix check -- 'record j of "
            "... is not key j of the key set' -- nothing generated",
            seed_rec["hit"] is grade(seed_rec["text"], pool[seed_rec["i"]]["gold"])
            and task_rec["hit"] is grade(task_rec["text"], pool[task_rec["i"]]["gold"])
            and mid["records"][9]["pool"] == "CORR_clean" and mid["records"][9]["i"] == 2
            and isinstance(e_s, GcalRefusal) and "record 5 of " in str(e_s)
            and "is not key 5 of the key set (order, seed or task)" in str(e_s) and not ad_s.calls
            and isinstance(e_k, GcalRefusal) and "record 9 of " in str(e_k)
            and "is not key 9 of the key set (order, seed or task)" in str(e_k) and not ad_k.calls,
            (str(e_s)[-90:], str(e_k)[-90:]))

        # an existing artifact with no checkpoint (refused before any generation); canonical out on
        # the stub; the model-free artifact first
        o6 = scratch(td, "conflict")
        o6.write_text("{}\n", encoding="utf-8")
        ad6 = stub()
        _r6, e6, _ = run(ad6, o6)
        ad6r = stub()
        _r6r, e6r, _ = run(ad6r, o6, resume=True)
        o6l = scratch(td, "conflict_link")
        os.symlink(Path(td) / "nowhere.json", o6l)
        ad6l = stub()
        _r6l, e6l, _ = run(ad6l, o6l)
        # the other direction: a complete checkpoint beside a DIFFERENT artifact still resumes
        # (nothing generated) and is refused only at the write, the artifact untouched
        d6c = Path(td) / "conflict_ck"
        d6c.mkdir()
        write_json_once(d6c / MODEL_FREE_NAME, art)
        (d6c / "ckpt").mkdir()
        (d6c / "ckpt" / CKPT_NAME).write_bytes(ckp.read_bytes())
        (d6c / COMPLETABILITY_NAME).write_text("{}\n", encoding="utf-8")
        ad6c = stub(52, 45)
        _r6c, e6c, _ = run(ad6c, d6c / COMPLETABILITY_NAME, resume=True)
        # the write-time guard (a complete checkpoint, then a symlink placed at the artifact path)
        with tempfile.TemporaryDirectory() as tdw:
            tw = Path(tdw)
            target = tw / "outside" / "landed.json"
            link = tw / "gates" / COMPLETABILITY_NAME
            link.parent.mkdir(parents=True)
            os.symlink(target, link)
            pw = {"out": target, "out_link": link}
            ref_w = refuses(lambda: _write_artifact(pw, {"x": 1}), GcalRefusal, "symlink")
            plain = tw / "plain" / COMPLETABILITY_NAME
            how_w = _write_artifact({"out": plain, "out_link": plain}, {"x": 1})
        chk("gcal: the artifact's final write is refused when its path as named is a symlink (dangling: "
            "nothing lands at the link's target) and written once on a plain path",
            ref_w and not target.exists() and how_w == "written", (ref_w, how_w))
        chk("gcal: with no checkpoint on disk an existing completability artifact (or a dangling symlink at "
            "its path) is refused before any generation or write, with --resume or without, the artifact "
            "untouched; with its complete checkpoint beside it, a resume generates nothing and is refused "
            "only at the write (never overwritten), the artifact untouched",
            all(isinstance(e, GcalRefusal) and "COMPLETABILITY ARTIFACT EXISTS" in str(e) for e in (e6, e6r, e6l))
            and not (ad6.calls or ad6r.calls or ad6l.calls) and o6.read_text() == "{}\n"
            and not (o6.parent / "ckpt").exists() and not (o6l.parent / "ckpt").exists()
            and o6l.is_symlink() and not o6l.exists()
            and isinstance(e6c, GcalRefusal) and "never overwritten" in str(e6c) and not ad6c.calls
            and (d6c / COMPLETABILITY_NAME).read_text() == "{}\n",
            (str(e6)[:70], str(e6c)[:70]))
        d7 = Path(td) / "nomf"
        d7.mkdir()
        ad7 = stub()
        _r7, e7, _ = run(ad7, d7 / COMPLETABILITY_NAME)
        d8 = Path(td) / "mfother"
        d8.mkdir()
        alt_mf = copy.deepcopy(art)
        alt_mf["renders_of_record"]["renders_sha256"] = "4" * 64
        write_json_once(d8 / MODEL_FREE_NAME, alt_mf)
        ad8 = stub()
        _r8, e8, _ = run(ad8, d8 / COMPLETABILITY_NAME)
        canon_out = Path(GATES_DIR) / "G-CAL_selftest_never.json"
        ad9 = stub()
        _r9, e9, _ = run(ad9, canon_out)
        chk("gcal: a stub run refuses a canonical out path, a missing model-free artifact and one on other "
            "renders -- before any generation or write",
            isinstance(e7, GcalRefusal) and "model-free artifact absent" in str(e7) and not ad7.calls
            and not (d7 / "ckpt").exists()
            and isinstance(e8, GcalRefusal) and "renders_sha256" in str(e8) and not ad8.calls
            and isinstance(e9, GcalRefusal) and "SELFTEST REFUSED" in str(e9) and not ad9.calls
            and not canon_out.exists(), (str(e7)[:60], str(e9)[:60]))

        # startup refusals and the boundary STOP
        d10 = Path(td) / "startup"
        d10.mkdir()
        write_json_once(d10 / MODEL_FREE_NAME, art)
        o10 = d10 / COMPLETABILITY_NAME
        win = stub()
        win.choice_window = 512
        moved = dict(testing.QWEN_BAN_MAP)
        moved["<think>"] = 7
        ban = testing.ScriptedAdapter("m-gcal-stub", ban_map=moved)
        ban.load(plan(64, 64))
        class Merging(testing.ScriptedAdapter):
            # a joined prompt shares no token prefix with the banner: the boundary collapses
            # to 0 (rule 28(d)'s instance); ban-list strings encode as the stub's
            def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
                ids = super().encode(text, add_special_tokens)
                if "Response:" in text and ids:
                    return [(ids[0] * 7 + 1) % 4096] + ids[1:]
                return ids

        merging = Merging("m-gcal-stub")
        merging.load(plan(64, 64))
        got = {}
        for nm, a_ in (("window", win), ("ban list", ban)):
            got[nm] = run(a_, o10)[1]
        sp_name = guard.FORBIDDEN_MODULES[0]
        insul = stub()
        prev_sp = sys.modules.get(sp_name)
        sys.modules[sp_name] = types.ModuleType(sp_name)
        try:
            got["insulation"] = run(insul, o10)[1]
        finally:
            if prev_sp is None:
                sys.modules.pop(sp_name, None)
            else:
                sys.modules[sp_name] = prev_sp
        got["boundary"] = run(merging, o10, resume=True)[1]
        bad_gold = [dict(it) for it in pool]
        bad_gold[0] = {"task": pool[0]["task"], "gold": ["cannot"]}
        hon = stub()
        d_hon = Path(td) / "honesty"
        d_hon.mkdir()
        write_json_once(d_hon / MODEL_FREE_NAME, art)
        got["honesty"] = run(hon, d_hon / COMPLETABILITY_NAME, pool=bad_gold)[1]
        chk("gcal: startup refuses a read window other than 8192, a live tokenizer whose ban list is not "
            "the frozen file's, a loaded state-present module, and f0's grader-honesty failure (on a fresh "
            "out dir with no checkpoint, the refusal naming the grader-honesty asserts) -- none generates or "
            "writes a checkpoint; a collapsed token boundary is a STOP before the first generation",
            all(isinstance(got[k], GcalRefusal) for k in ("window", "ban list", "insulation", "honesty"))
            and isinstance(got["boundary"], GcalStop) and "BOUNDARY INCIDENT" in str(got["boundary"])
            and "f0's grader-honesty asserts fail" in str(got["honesty"])
            and "item 0: the non-answer is graded correct" in str(got["honesty"])
            and not (d_hon / "ckpt").exists() and not (d_hon / COMPLETABILITY_NAME).exists()
            and not (win.calls or ban.calls or insul.calls or merging.calls or hon.calls),
            {k: type(v).__name__ for k, v in got.items()})
        chk("gcal: f0's grader-honesty asserts are clean on the pool of record and fire on a gold the "
            "non-answer contains", _grader_honesty(pool) == []
            and _grader_honesty(bad_gold) == ["item 0: the non-answer is graded correct"],
            _grader_honesty(bad_gold))

        # the non-stub path: canonical paths only, preflight, gate line (git and dirs patched)
        class Done:
            def __init__(self, rc: int, out: Any = "", err: Any = "") -> None:
                self.returncode, self.stdout, self.stderr = rc, out, err

        rp = Path(td) / "repo"
        rp.mkdir()
        (rp / "P.md").write_text("proposal\n", encoding="utf-8")
        (rp / "CLAUDE.md").write_text("claude\n", encoding="utf-8")
        psha = _sha256_bytes(b"proposal\n")

        def fake_git(missing=(), head_ok=True):
            def g(*args, repo=REPO, binary=False):
                rel = args[2].split(":", 1)[1] if args[:1] == ("cat-file",) else args[-1]
                gone = rel in missing or not (Path(repo) / rel).exists()
                if args[:2] == ("rev-parse", "--verify"):
                    return Done(0, "cd" * 20 + "\n") if head_ok else Done(128, "", "fatal: no HEAD")
                if args[:2] == ("cat-file", "-e"):
                    return Done(128, "", "fatal: path does not exist") if gone else Done(0)
                if args[:3] == ("ls-tree", "-z", "HEAD"):
                    return Done(0, "") if gone else Done(0, f"100644 blob {'0' * 40}\t{rel}\0")
                if args[:2] == ("cat-file", "blob"):
                    data = (Path(repo) / rel).read_bytes()
                    return Done(0, data if binary else data.decode("utf-8"))
                raise AssertionError(f"selftest: an unexpected git call {args}")
            return g

        gates, ckd = Path(td) / "cgates", Path(td) / "cckpt"
        gates.mkdir()
        write_json_once(gates / MODEL_FREE_NAME, {**art, "provenance": {**art["provenance"],
                                                                        "proposal_sha256": psha}})

        class NonStub(testing.ScriptedAdapter):
            def provenance(self) -> dict:
                return {"adapter": "m-gcal-nonstub-double", "backend": "selftest", "dtype": "none"}

        def nonstub(h_c=60, h_x=45):
            ad = NonStub("m-gcal-nonstub")
            ad.load(plan(h_c, h_x))
            return ad

        def run_ns(ad, out, *, prob=(), missing=(), head_ok=True, sha=psha, ana=None, **kw):
            with mock.patch.object(_stages, "_git", fake_git(missing, head_ok)), \
                    mock.patch.object(_stages, "ANALYZER_PATH", ana or (rp / "scripts" / "m_analyze.py")), \
                    mock.patch.object(guard, "preflight_laptop", lambda: list(prob)), \
                    mock.patch(f"{__name__}.REPO", rp), mock.patch(f"{__name__}.GATES_DIR", gates), \
                    mock.patch(f"{__name__}.CKPT_DIR", ckd):
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    try:
                        return run_completability(ad, out_path=out, resume=False, proposal_file="P.md",
                                                  proposal_sha256=sha, **kw), None, buf.getvalue()
                    except SystemExit as e:
                        return None, e, buf.getvalue()

        cout = gates / COMPLETABILITY_NAME
        ns_ref = {nm: run_ns(a_, o_, **kw)
                  for nm, (a_, o_, kw) in {
                      "preflight": (nonstub(), cout, {"prob": ("ONE PROCESS: another model process",)}),
                      "elsewhere": (nonstub(), Path(td) / "x" / COMPLETABILITY_NAME, {}),
                      "pool": (nonstub(), cout, {"pool": pool}),
                      "proposal sha": (nonstub(), cout, {"sha": "5" * 64}),
                      "CLAUDE.md": (nonstub(), cout, {"missing": ("CLAUDE.md",)}),
                      "HEAD": (nonstub(), cout, {"head_ok": False}),
                  }.items()}
        chk("gcal: a non-stub run is refused before any write or generation on a preflight problem, an out "
            "path other than the canonical one, a supplied pool, a proposal whose working-tree sha is not "
            "the run's, CLAUDE.md not committed, and HEAD unknown",
            all(isinstance(v[1], GcalRefusal) for v in ns_ref.values()) and not ckd.exists()
            and not cout.exists(), {k: str(v[1])[:50] for k, v in ns_ref.items()})
        ad_ns = nonstub()
        r_ns, e_ns, out_ns = run_ns(ad_ns, cout)
        a_ns = json.loads(cout.read_text()) if cout.exists() else {}
        g_ns = (a_ns.get("provenance") or [{}])[0].get("gate") or {}
        chk("gcal: a non-stub run with a clean preflight writes the canonical paths, prints and records the "
            "gate line -- proposal (committed, its sha), CLAUDE.md (committed), HEAD, and the analyzer "
            "'absent -- G-ANL-F0 is §8 step 8, after G-CAL'",
            e_ns is None and (r_ns or {}).get("verdict") == "PASS" and (ckd / CKPT_NAME).exists()
            and g_ns.get("analyzer") == ANALYZER_ABSENT and g_ns.get("proposal_sha256") == psha
            and g_ns.get("head") == "cd" * 20 and g_ns.get("claude_md_sha256") == _sha256_bytes(b"claude\n")
            and (out_ns.splitlines() or [""])[0] == g_ns.get("line")
            and (out_ns.splitlines() or [""])[0].startswith(f"GATE G-CAL: proposal P.md {psha[:16]}, CLAUDE.md "),
            (str(e_ns)[:80], g_ns.get("line")))
        (rp / "scripts").mkdir()
        (rp / "scripts" / "m_analyze.py").write_text("# analyzer\n", encoding="utf-8")
        with mock.patch.object(_stages, "_git", fake_git()):
            g_present, gp_present = gate_line("P.md", psha, repo=rp, analyzer_path=rp / "scripts" / "m_analyze.py")
            g_absent, gp_absent = gate_line("P.md", psha, repo=rp, analyzer_path=rp / "none.py")
            g_bad, gp_bad = gate_line("P.md", "6" * 64, repo=rp, analyzer_path=rp / "none.py")
            g_unc, gp_unc = gate_line("Q.md", psha, repo=rp, analyzer_path=rp / "none.py")
        chk("gcal: the gate line records an analyzer that is present by its sha16 (no refusal) and an absent "
            "one by the PIN's words; it fires on a proposal sha that is not the run's and on a proposal not "
            "committed",
            gp_present == [] and g_present["analyzer"].startswith(
                f"present {_sha256_bytes(b'# analyzer' + bytes([10]))[:16]}")
            and gp_absent == [] and g_absent["analyzer"] == ANALYZER_ABSENT
            and len(gp_bad) == 1 and "not the run's" in gp_bad[0]
            and any("not committed at HEAD" in x for x in gp_unc), (gp_bad, gp_unc[:1]))

    # the no-write check's logic on a temp "canonical" pair of directories, without and with
    # the canonical artifacts present (before and after step 6's own canonical run)
    with tempfile.TemporaryDirectory() as tdc:
        cg, cc = Path(tdc) / "gates", Path(tdc) / "ckpt"
        cg.mkdir()
        with mock.patch(f"{__name__}.GATES_DIR", cg), mock.patch(f"{__name__}.CKPT_DIR", cc):
            def old_rule() -> bool:     # the absence rule this check replaced
                return not any((Path(GATES_DIR) / n).exists() for n in
                               (MODEL_FREE_NAME, SEAT_READ_NAME, COMPLETABILITY_NAME)) \
                    and not (Path(CKPT_DIR) / CKPT_NAME).exists()

            empty0 = canonical_snapshot()
            sd = Path(tdc) / "scratch_run"
            sd.mkdir()
            write_model_free(sd)                           # a selftest-style run, elsewhere
            empty_same = snapshot_changes(empty0, canonical_snapshot())
            old_empty = old_rule()
            write_json_once(cg / MODEL_FREE_NAME, art)
            write_text_once(cg / SEAT_READ_NAME, seat_read_request(art))
            write_json_once(cg / COMPLETABILITY_NAME, {"schema": ART_SCHEMA})
            cc.mkdir()
            _resume.atomic_write_json(cc / CKPT_NAME, {"schema": CKPT_SCHEMA})
            appeared = snapshot_changes(empty0, canonical_snapshot())
            full0 = canonical_snapshot()
            write_model_free(Path(tdc) / "scratch_run2")   # the same run, artifacts present
            full_same = snapshot_changes(full0, canonical_snapshot())
            old_full = old_rule()
            (cg / SEAT_READ_NAME).write_bytes((cg / SEAT_READ_NAME).read_bytes() + b"x")
            edited = snapshot_changes(full0, canonical_snapshot())
            (cc / CKPT_NAME).unlink()
            removed = snapshot_changes(full0, canonical_snapshot())
            (cg / "G-CAL_stray.json.tmp").write_text("{}", encoding="utf-8")
            stray = snapshot_changes(full0, canonical_snapshot())
    names4 = ["ckpt/" + CKPT_NAME, "gates/" + COMPLETABILITY_NAME, "gates/" + MODEL_FREE_NAME,
              "gates/" + SEAT_READ_NAME]
    chk("gcal: the no-write check (snapshot before vs after, byte for byte) on a temp canonical pair passes "
        "with the canonical artifacts absent AND present (where the absence rule it replaced fails), and "
        "fires on a file appearing, an edited byte, a removed checkpoint and a stray G-CAL temporary",
        all(v is None for v in empty0.values()) and sorted(empty0) == names4 and empty_same == []
        and old_empty is True and appeared == names4 and full_same == [] and old_full is False
        and all(v is not None for v in full0.values())
        and edited == ["gates/" + SEAT_READ_NAME] and removed == ["ckpt/" + CKPT_NAME, "gates/" + SEAT_READ_NAME]
        and stray == sorted(["ckpt/" + CKPT_NAME, "gates/G-CAL_stray.json.tmp", "gates/" + SEAT_READ_NAME]),
        (empty_same, appeared, full_same, edited, removed, stray))
    # --- G-CAL-OLMo-{ckpt} (m:176, m:302; the OLMo track's build, the prebuild answers §0) ------
    o_mf = model_free_artifact()
    o_ks = key_set()
    o_kit = testing.olmo_kit()
    o_setup = _ro.OLMoSetup(audit=o_kit["audit"], ban_ids=tuple(o_kit["ban_ids"]),
                            ban_strings=tuple(o_kit["ban_strings"]), term_rx=tuple(o_kit["term_rx"]),
                            audit_sha16=_ro.olmo_audit_sha16())
    o_seg_key = {(f"Task: {_task_of(k, pool, renders)}\nResponse:", k["seed"]): k for k in o_ks}

    def o_plan(h_clean: int, h_corr: int):
        def f(call):
            k = o_seg_key[(call["segment"], call["seed"])]
            h = h_clean if k["pool"] == "CORR_clean" else h_corr
            if k["i"] * 4 + k["s"] < h:
                return {"text": f"Verily {pool[k['i']]['gold'][0]}.", "n_tok": 3}
            return {"text": "Zqxj unknown.", "n_tok": 2}
        return f

    def o_stub(h_clean=64, h_corr=64):
        ad = testing.OLMoScriptedAdapter("m-gcal-olmo-stub")
        ad.load(o_plan(h_clean, h_corr))
        return ad

    def o_run(ad, out, *, unit="OLMo-sft", resume=False):
        buf = io.StringIO()
        res = exc = None
        with contextlib.redirect_stdout(buf), mock.patch(f"{__name__}.olmo_startup", lambda a, c: o_setup):
            try:
                res = run_completability(ad, out_path=out, resume=resume, proposal_file=PROP_REL,
                                         proposal_sha256=PROP_SHA, unit=unit)
            except (SystemExit, KeyboardInterrupt) as e:
                exc = e
        return res, exc, buf.getvalue()

    def o_scratch(td: str, name: str, ckpt: str = "sft") -> Path:
        d = Path(td) / name
        d.mkdir()
        write_json_once(d / MODEL_FREE_NAME, o_mf)
        return d / COMPLETABILITY_NAME_OLMO.format(ckpt=ckpt)

    class AppendingOLMo(testing.OLMoScriptedAdapter):
        """A tokenizer that appends one id under the default encode (the For-the-box hazard)."""
        def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
            ids = super().encode(text, add_special_tokens)
            return ids + [0] if add_special_tokens else ids

    chk("gcal-olmo: unit names -- Q-F0 is G-CAL with Qwen's files; each OLMo unit is G-CAL-OLMo-{ckpt} with "
        "G-CAL_completability_olmo-{ckpt}.json and G-CAL_olmo-{ckpt}.json; base, Q-F3 and an unknown unit refused",
        unit_ckpt("Q-F0") is None and _names("Q-F0") == (COMPLETABILITY_NAME, CKPT_NAME)
        and stage_label("Q-F0") == "G-CAL" and OLMO_UNITS == ("OLMo-sft", "OLMo-dpo", "OLMo-instruct")
        and [unit_ckpt(u) for u in OLMO_UNITS] == ["sft", "dpo", "instruct"]
        and stage_label("OLMo-instruct") == "G-CAL-OLMo-instruct"
        and _names("OLMo-dpo") == ("G-CAL_completability_olmo-dpo.json", "G-CAL_olmo-dpo.json")
        and all(refuses(lambda u=u: unit_ckpt(u), GcalRefusal, "neither Q-F0 nor an OLMo unit")
                for u in ("OLMo-base", "Q-F3", "OLMo-SFT", "")))
    wp_ok = {c: weights_of_record(c) for c in keys.CKPTS}
    man = json.loads((REPO / MANIFEST_REL).read_text(encoding="utf-8"))
    with mock.patch.object(_stages, "_committed", lambda rel, rp=None: ([], b"{}")):
        bad_man = weights_of_record("sft")
    with mock.patch.object(_stages, "_committed", lambda rel, rp=None: (["not committed at HEAD"], None)):
        unc_man = weights_of_record("dpo")
    with mock.patch.object(_stages, "_committed", lambda rel, rp=None: (
            [], json.dumps({"sft": {**man["sft"], "path": "/workspace/models/dpo"}}).encode())):
        leaf_man = weights_of_record("sft")
    chk("gcal-olmo: the weights of record are the committed manifest's entry per checkpoint (repo, revision, "
        "files_aggregate_sha256, path ending in the checkpoint); a malformed or uncommitted manifest, or an "
        "entry whose path names another checkpoint, is a problem",
        all(p == [] and w == {"repo": man[c]["repo"], "revision": man[c]["revision"],
                              "sha256": man[c]["files_aggregate_sha256"], "path": man[c]["path"],
                              "n_files": man[c]["n_files"]} for c, (p, w) in wp_ok.items())
        and bad_man[1] is None and bad_man[0] != []
        and unc_man[1] is None and any("not committed" in x for x in unc_man[0])
        and leaf_man[1] is None and any("does not end in 'sft'" in x for x in leaf_man[0]),
        ({c: p for c, (p, w) in wp_ok.items()}, bad_man[0], unc_man[0], leaf_man[0]))
    with tempfile.TemporaryDirectory() as td:
        o_outs = {}
        for nm, (hc, hx) in {"pass70": (52, 45), "fail70": (52, 44)}.items():
            ad = o_stub(hc, hx)
            o_outs[nm] = (ad,) + o_run(ad, o_scratch(td, nm))
        o_art = (json.loads(Path(o_outs["pass70"][1]["artifact"]).read_text(encoding="utf-8"))
                 if o_outs["pass70"][1] else {})
        o_fail = (json.loads(Path(o_outs["fail70"][1]["artifact"]).read_text(encoding="utf-8"))
                  if o_outs["fail70"][1] else {})
        oid = o_art.get("identity", {})
        sc_sha = _sha256_bytes((REPO / SCAFFOLD_REL.format(ckpt="sft")).read_bytes())
        chk("gcal-olmo: two scripted 128-generation G-CAL-OLMo-sft runs end at condition (4)'s .70 boundary "
            "(45/64 PASS, 44/64 FAIL); the FAIL artifact's consequence is NOT-RUN 'dose not completable', never "
            "'STOP and re-specify'; stage, substrate and unit are named",
            (o_outs["pass70"][1] or {}).get("verdict") == "PASS" and (o_outs["fail70"][1] or {}).get("verdict") == "FAIL"
            and o_art.get("stage") == "G-CAL-OLMo" and o_art.get("substrate") == "olmo"
            and o_art.get("unit") == "OLMo-sft" and o_fail.get("on_fail") == ON_FAIL["olmo"]
            and "dose not completable" in ON_FAIL["olmo"] and "re-specify" not in ON_FAIL["olmo"]
            and o_art.get("covariate", {}).get("fraction") == "7/64",
            [(o[1] or {}).get("verdict") for o in o_outs.values()] + [str(o[2])[:120] for o in o_outs.values()])
        chk("gcal-olmo: the identity is Qwen's keys plus the unit, the ban ids' sha16, and the weights of record "
            "(repo, revision, files_aggregate_sha256); ban_sha256 is the committed scaffold_sft.json's sha256; "
            "TEMP 0.7, cap 60, uncached",
            tuple(sorted(oid)) == tuple(sorted(IDENTITY_KEYS_OLMO)) and oid.get("stage") == "G-CAL-OLMo"
            and oid.get("substrate") == "olmo" and oid.get("unit") == "OLMo-sft"
            and oid.get("ban_ids_sha16") == ban_ids_sha16(o_kit["ban_ids"]) and oid.get("ban_sha256") == sc_sha
            and oid.get("weights_repo") == man["sft"]["repo"] and oid.get("weights_revision") == man["sft"]["revision"]
            and oid.get("weights_sha256") == man["sft"]["files_aggregate_sha256"]
            and oid.get("temp") == "0.7" and oid.get("stop_cap") == 60 and oid.get("path") == "uncached"
            and oid.get("key_set_sha256") == key_set_sha256(o_ks), sorted(oid))
        oad = o_outs["pass70"][0]
        chk("gcal-olmo: every generation is SESSION_BANNER (b3's banner) + 'Task: {task}\\nResponse:', "
            "injections=(), cached=False, TEMP 0.7, STOP_CAP 60, newline stop, the OLMo kit's ban ids (the "
            "startup's), the key's seed, in key order -- Qwen's 128 keys",
            len(oad.calls) == 128 and all(
                c["prefix"] == SESSION_BANNER and c["injections"] == () and c["cached"] is False
                and c["temp"] == 0.7 and c["max_tokens"] == 60 and c["stop_newline"] is True
                and c["ban_ids"] == tuple(o_kit["ban_ids"]) for c in oad.calls)
            and [(c["segment"], c["seed"]) for c in oad.calls] == [
                (f"Task: {_task_of(k, pool, renders)}\nResponse:", k["seed"]) for k in o_ks])
        o_lines = o_outs["pass70"][3].splitlines()
        f_lines = o_outs["fail70"][3].splitlines()
        chk("gcal-olmo: stdout -- no response text; the four tally lines precede the last line, which names "
            "G-CAL-OLMo-sft and, on FAIL, the NOT-RUN consequence; the covariate line names LOCK-m-OLMo-sft v0.1",
            "Verily" not in o_outs["pass70"][3] and "Zqxj" not in o_outs["pass70"][3]
            and (o_lines or [""])[-1].startswith("G-CAL-OLMo-sft completability: PASS; artifact ")
            and (f_lines or [""])[-1].startswith('G-CAL-OLMo-sft completability: FAIL -- that checkpoint NOT-RUN '
                                                'with reason "dose not completable" (m:176, m:302; §5); artifact ')
            and [ln.split(" ")[2] for ln in o_lines[-5:-1]] == ["(iii)", "(iv)", "(i)", "(ii)"]
            and any("(LOCK-m-OLMo-sft v0.1 carries it, m:176)" in ln for ln in o_lines),
            o_lines[-6:])
        # a resume under another checkpoint's identity: the sft checkpoint placed at dpo's name
        dsrc = Path(o_outs["pass70"][1]["checkpoint"]) if o_outs["pass70"][1] else Path(td) / "none"
        dd = Path(td) / "cross"
        dd.mkdir()
        write_json_once(dd / MODEL_FREE_NAME, o_mf)
        (dd / "ckpt").mkdir()
        if dsrc.is_file():
            (dd / "ckpt" / CKPT_NAME_OLMO.format(ckpt="dpo")).write_bytes(dsrc.read_bytes())
        ad_x = o_stub()
        _r, exc_x, _o = o_run(ad_x, dd / COMPLETABILITY_NAME_OLMO.format(ckpt="dpo"), unit="OLMo-dpo", resume=True)
        chk("gcal-olmo: an sft checkpoint resumed as OLMo-dpo is refused as a CHECKPOINT MISMATCH naming the "
            "unit, the scaffold set and the weights of record; nothing generated",
            isinstance(exc_x, GcalRefusal) and "CHECKPOINT MISMATCH" in str(exc_x)
            and all(k in str(exc_x) for k in ("'unit'", "'ban_sha256'", "'weights_sha256'"))
            and len(ad_x.calls) == 0, str(exc_x)[:240])
        # a pod change mid-run: the checkpoint's generations came from pod A; a resume on pod B is refused (m:267)
        pc_out = o_scratch(td, "podchange")
        killer = {"n": 0}

        def boom(call):
            killer["n"] += 1
            if killer["n"] == 50:
                raise KeyboardInterrupt("selftest: pod A pre-empted mid-run")
            return o_plan(64, 64)(call)
        ad_a = testing.OLMoScriptedAdapter("m-gcal-olmo-stub")      # one backend identifier on both pods
        ad_a.load(boom)
        with mock.patch.dict(os.environ, {_resume.POD_ENV: "podA"}):
            _r, exc_a, _o = o_run(ad_a, pc_out)
        ck_pa = json.loads((pc_out.parent / "ckpt" / CKPT_NAME_OLMO.format(ckpt="sft")).read_text(encoding="utf-8"))
        ad_b = o_stub()
        with mock.patch.dict(os.environ, {_resume.POD_ENV: "podB"}):
            _r, exc_b, _o = o_run(ad_b, pc_out, resume=True)
        ad_a2 = o_stub()
        with mock.patch.dict(os.environ, {_resume.POD_ENV: "podA"}):
            res_a2, exc_a2, _o = o_run(ad_a2, pc_out, resume=True)
        ad_b2 = o_stub()
        with mock.patch.dict(os.environ, {_resume.POD_ENV: "podB"}):
            res_b2, exc_b2, _o = o_run(ad_b2, pc_out, resume=True)
        chk("gcal-olmo: a resume never splices two pods (m:267; the build's review, finding 1) -- 49 generations on pod A "
            "then a resume on pod B is refused (POD CHANGED, nothing generated); on pod A it completes the 128; the "
            "complete checkpoint then re-derives its artifact on pod B (nothing generated)",
            isinstance(exc_a, KeyboardInterrupt) and len(ck_pa["records"]) == 49
            and [e_["pod_id"] for e_ in ck_pa["provenance"]] == ["podA"]
            and isinstance(exc_b, GcalRefusal) and "POD CHANGED" in str(exc_b) and len(ad_b.calls) == 0
            and exc_a2 is None and (res_a2 or {}).get("generated") == 79 and len(ad_a2.calls) == 79
            and exc_b2 is None and (res_b2 or {}).get("generated") == 0 and len(ad_b2.calls) == 0
            and (res_b2 or {}).get("artifact_write") == "identical",
            (type(exc_a).__name__, len(ck_pa.get("records", [])), str(exc_b)[:120], (res_a2 or {}).get("generated"),
             str(exc_b2)[:120], (res_b2 or {}).get("artifact_write")))
        ad_ap = AppendingOLMo("m-gcal-olmo-appending")
        ad_ap.load(o_plan(64, 64))
        _r, exc_ap, _o = o_run(ad_ap, o_scratch(td, "appending"))
        chk("gcal-olmo: a tokenizer that appends a token under the default encode is refused before any "
            "generation (TOKENIZER APPENDS A TOKEN); the stub's own tokenizer passes the probe",
            isinstance(exc_ap, GcalRefusal) and "TOKENIZER APPENDS A TOKEN" in str(exc_ap)
            and len(ad_ap.calls) == 0 and tokenizer_appends(testing.OLMoScriptedAdapter()) is False
            and tokenizer_appends(AppendingOLMo()) is True, str(exc_ap)[:160])
        # non-stub refusals: the pod id (precheck) and the weights path (startup)
        env_no_pod = {k: v for k, v in os.environ.items() if k != _resume.POD_ENV}
        # The seat's N12 ruling (2026-11-07): the case holds in every state of the record. From 6ce8b9a on the
        # canonical G-CAL-OLMo checkpoints exist, and CHECKPOINT EXISTS rightly refuses first, so this call's
        # canonical artifact and checkpoint paths point at an empty temporary root; the model-free artifact stays
        # the canonical one precheck reads. Self-test only: the production paths are unchanged.
        empty_root = Path(td) / "empty-canonical-root"
        canonical_of_record = _canonical              # bound before the patch: the stand-in derives from it

        def empty_canonical(unit: str = "Q-F0") -> dict[str, Path]:
            out_name, ck_name = _names(unit)
            return {**canonical_of_record(unit), "out": empty_root / "gates" / out_name,
                    "ckpt": empty_root / "ckpt" / ck_name}
        with mock.patch.dict(os.environ, env_no_pod, clear=True), \
                mock.patch(f"{__name__}._canonical", empty_canonical):
            no_pod = refuses(lambda: precheck(out_path=None, resume=False, proposal_file=PROP_REL,
                                              proposal_sha256=PROP_SHA, stub=False, unit="OLMo-sft"),
                             GcalRefusal, "POD ID ABSENT")
        w_sft = wp_ok["sft"][1]
        wrong = testing.OLMoScriptedAdapter()
        wrong.path = "/workspace/models/dpo"
        right = testing.OLMoScriptedAdapter()
        right.path = w_sft["path"] + "/"
        with mock.patch(f"{__name__}.olmo_startup", lambda a, c: o_setup):
            wrong_ref = refuses(lambda: _startup_olmo(wrong, "sft", w_sft, False), GcalRefusal,
                                "is not the manifest's sft entry")
            right_ids = _startup_olmo(right, "sft", w_sft, False)
            nopath_ref = refuses(lambda: _startup_olmo(testing.OLMoScriptedAdapter(), "sft", w_sft, False),
                                 GcalRefusal, "is not the manifest's")
        chk("gcal-olmo: a non-stub precheck without the pod id is refused (POD ID ABSENT, no laptop checklist on "
            "OLMo); a non-stub startup refuses an adapter whose weights path is not the manifest entry's, or has none",
            no_pod and wrong_ref and nopath_ref and right_ids == list(o_kit["ban_ids"]))
    # R1 A6's tallies, on the committed Qwen artifact: Code's Qwen observations of record reproduced
    q_art = json.loads((Path(GATES_DIR) / COMPLETABILITY_NAME).read_text(encoding="utf-8"))
    q_t = olmo_tallies(q_art["records"], o_mf["renders_of_record"]["items"], _sc.load_term_rx())
    chk("gcal-olmo: R1 A6's (iii) and (iv) reproduce Code's Qwen observations of record on the committed "
        "G-CAL artifact -- one termination echo (corrupted item 6, seed 1); 11 restatements of a corrupted word, "
        "9 of them hits (RESULTS.md@9cbacdb:5032-5041); the tally lines carry counts and keys, no response text",
        q_t["iii_termination"] == {"n": 1, "keys": ["CORR_corrupted i=6 s=1"]}
        and q_t["iv_mirroring"]["n"] == 11 and q_t["iv_mirroring"]["hits"] == 9
        and corrupted_words({"render": "Clopuie 31 + 46.", "changed_positions": [1, 2, 5]}) == ["Clopuie"]
        and mirrors("It is Clopuie.", ["Clopuie"]) and not mirrors("Clopuies", ["Clopuie"])
        and not any(r["text"] in ln for ln in tally_lines(q_t) for r in q_art["records"] if len(r["text"]) > 8),
        q_t)
    chk("gcal: the selftest left every canonical G-CAL path under data/m as it found it (a snapshot of each "
        "path's bytes, or its absence, taken before the runs, compared after; existing artifacts allowed)",
        snapshot_changes(snap0, canonical_snapshot()) == [] and set(names4) <= set(snap0),
        snapshot_changes(snap0, canonical_snapshot()))
