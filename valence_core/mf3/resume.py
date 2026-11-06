"""Q-F3's resume identity (PROPOSAL-m v1.11 §2.7 m:267; §2.2 m:174; the design seat's prebuild answers
of 2026-11-06, Q1 and Q6).

THE CHECKPOINT MACHINERY is ``valence_core.m.resume``'s, imported unchanged: the atomic JSON write
(temp file, fsync, rename, directory fsync), the checkpoint body and its invariants
(``_check_state``: sessions verified, unique, inside the identity's templates and n; the hour-cap
milliseconds, its CHECKPOINT STATE INCONSISTENT line sealed (``TOTALS_SEALED``, the step-14 read's Q3,
carried by Q6); the look-index invariant), the three-step finish (``set_end_pending`` /
``apply_end`` / ``persist_end``), ``refuse_ended``, ``record_session`` (only a G-VER-verified record),
``done_ids`` (skip-only), the provenance list and the hour cap. m's ``Identity`` refuses Q-F3
(keys.templates), so Q-F3's identity and the load that validates it are here.

THE IDENTITY (m:267): Q-F0's keys, with Q-F3's values (mf3's own ``package_sha256``), plus
  reasoning_cap       the reasoning-line cap (m:174: "the cap enters the resume identity"): 60 at
                      G-TIME-F3, the fixed cap after it;
  m_module_sha256     the C2 licence's part (b): each imported valence_core.m module's file sha256,
                      with the package's __init__.py (guard.M_HASHED);
  weights_revision,   the weights-snapshot binding (Q6: "mf3's at the F3 build"): the Qwen snapshot's
  weights_sha256      revision -- which the hub cache's refs/main must name at stage start, offline
                      (the licence's part (g)) -- and the sha256 of its load files' content addresses.
A resume across any change of them is refused (m:267: "a resume refuses any change of seed or n").
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any, Mapping

from valence_core.m import corr as m_corr
from valence_core.m import resume as m_resume
from valence_core.session_e2a import STOP_CAP

from . import guard, keys
from . import scaffold as sc_mod

REPO = Path(__file__).resolve().parents[2]
SCHEMA = m_resume.SCHEMA
SESSION_SCHEMA = m_resume.SESSION_SCHEMA
LOOK_EVERY = m_resume.LOOK_EVERY
CANONICAL_ROOTS = (REPO / "data" / "mf3",) + tuple(m_resume.CANONICAL_ROOTS)
IDENTITY_KEYS = tuple(m_resume.IDENTITY_KEYS) + ("reasoning_cap", "m_module_sha256", "weights_revision",
                                                 "weights_sha256")
_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_HEX40 = re.compile(r"^[0-9a-f]{40}$")
_HEX16 = re.compile(r"^[0-9a-f]{16}$")
_AUTO = object()

# re-exported machinery (imported, never copied)
atomic_write_json = m_resume.atomic_write_json
json_text = m_resume.json_text
backend_identifier = m_resume.backend_identifier
read_checkpoint = m_resume.read_checkpoint
write_checkpoint = m_resume.write_checkpoint
assert_writable = m_resume.assert_writable
record_session = m_resume.record_session
done_ids = m_resume.done_ids
refuse_ended = m_resume.refuse_ended
ended_status = m_resume.ended_status
pending_end = m_resume.pending_end
pending_at = m_resume.pending_at
set_end_pending = m_resume.set_end_pending
apply_end = m_resume.apply_end
persist_end = m_resume.persist_end
same_json = m_resume.same_json
append_provenance = m_resume.append_provenance
note_launch = m_resume.note_launch
report_provenance = m_resume.report_provenance
provenance_record = m_resume.provenance_record
hour_cap_exceeded = m_resume.hour_cap_exceeded
session_ms = m_resume.session_ms
pool_sha16 = m_resume.pool_sha16
TOTALS_SEALED = m_resume.TOTALS_SEALED


def refuse_canonical_out(path) -> Path:
    """m's refusal (data/m, /workspace/models, data/olmo) and data/mf3 too: a stub or self-test run never
    lands where a Q-F3 measurement is stored (ledger 27). Returns the resolved path."""
    p = m_resume.refuse_canonical_out(path)
    r = CANONICAL_ROOTS[0].resolve()
    if p == r or r in p.parents:
        raise SystemExit(f"SELFTEST REFUSED: {path} resolves to {p}, under the canonical location {r} (ledger 27)")
    return p


# --- the weights of record (Q6) --------------------------------------------------------------
WEIGHTS_FILES = ("config.json", "tokenizer.json", "model.safetensors.index.json")
QWEN_MODEL_ID = "mlx-community/Qwen3.6-27B-4bit"          # the model of record (LOCK-m-F0 v0.2)


def hub_repo_dir(cache_dir=None) -> Path:
    """The model of record's repository directory in the hub cache (huggingface_hub's HF_HUB_CACHE
    layout: refs/main, snapshots/<revision>, blobs)."""
    if cache_dir is None:
        from huggingface_hub import constants as hf_constants
        cache_dir = hf_constants.HF_HUB_CACHE
    return Path(cache_dir) / ("models--" + QWEN_MODEL_ID.replace("/", "--"))


def weights_binding(snapshot_dir) -> dict:
    """{revision, sha256}: the snapshot directory's name (its revision) and the sha256 of
    the compact sort-keyed JSON {file: content address} over config.json, tokenizer.json,
    model.safetensors.index.json and every weight file the index names."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q6, "The weights-snapshot binding in the identity
    # goes into each unit's identity at its own build: mf3's at the F3 build", carrying the step-10 read's
    # Q5): a file's content address is the hub cache's blob name its snapshot link resolves to (for the
    # LFS weight files their sha256, else the git blob id); a file that is not such a link is hashed
    # (sha256 of its bytes). No full re-hash of the weights at stage start (the offline load reads the
    # cache's blobs); the revision is the snapshot directory's 40-hex name.
    d = Path(snapshot_dir)
    rev = d.name
    if not _HEX40.match(rev):
        raise ValueError(f"weights: {d} is not a hub snapshot directory (40-hex name)")
    index = json.loads((d / "model.safetensors.index.json").read_text(encoding="utf-8"))
    weights = sorted(set(index["weight_map"].values()))
    addr = {}
    for f in WEIGHTS_FILES + tuple(weights):
        p = d / f
        if p.is_symlink() and Path(os.readlink(p)).parent.name == "blobs":
            if not p.is_file():
                raise ValueError(f"weights: {f} links to an absent blob in {d}")
            addr[f] = Path(os.readlink(p)).name
        elif p.is_file():
            addr[f] = hashlib.sha256(p.read_bytes()).hexdigest()
        else:
            raise ValueError(f"weights: {f} absent from {d}")
    blob = json.dumps(addr, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {"revision": rev, "sha256": hashlib.sha256(blob).hexdigest(), "files": addr}


# --- the identity -----------------------------------------------------------------------------
def _canon(x: Any) -> str:
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def _of_record() -> tuple[str, str]:
    pool, renders = sc_mod.pool_and_renders()
    return m_resume.pool_sha16(pool), m_corr.renders_sha(renders)


def Identity(*, stage: str, template_set, lock_sha256: str, schedule_sha256: str, path: str, hour_cap,
             n: Mapping[str, int], audit_v2_sha16: str, ban_sha: str, backend_identifier: str,
             proposal_sha256: str, reasoning_cap: int, weights_revision: str, weights_sha256: str,
             unit: str = keys.UNIT, stop_cap: int = STOP_CAP, key_templates: Mapping | None = None,
             pod_id: Any = None, package_sha256: Any = _AUTO, m_module_sha256: Any = _AUTO,
             pool_sha16: Any = _AUTO, renders_sha16: Any = _AUTO) -> dict:
    """Build and validate a Q-F3 resume identity; a plain JSON-native dict."""
    if unit != keys.UNIT:
        raise ValueError(f"a Q-F3 identity's unit is {keys.UNIT!r}")
    if stage not in keys.STAGES:
        raise ValueError(f"stage {stage!r} is not a Q-F3 stage")
    ts = list(template_set)
    if not ts or len(set(ts)) != len(ts) or any(t not in keys.TEMPLATES for t in ts):
        raise ValueError(f"template_set {ts!r} must be distinct Q-F3 templates")
    ts = [t for t in keys.TEMPLATES if t in ts]       # §2.4's table order, as m's PIN
    if stage == "id" and ts != list(keys.GID_TEMPLATES):
        raise ValueError(f"G-ID-F3 runs {keys.GID_TEMPLATES} (m:295)")
    if type(lock_sha256) is not str or not _HEX64.match(lock_sha256):
        raise ValueError("lock_sha256 must be a sha256 hex digest: every Q-F3 stage follows its lock")
    if package_sha256 is _AUTO:
        package_sha256 = guard.package_sha256()
    if m_module_sha256 is _AUTO:
        m_module_sha256 = guard.m_module_sha256s()
    if pool_sha16 is _AUTO or renders_sha16 is _AUTO:
        p16, r16 = _of_record()
        pool_sha16 = p16 if pool_sha16 is _AUTO else pool_sha16
        renders_sha16 = r16 if renders_sha16 is _AUTO else renders_sha16
    for nm, v, rx in (("schedule_sha256", schedule_sha256, _HEX64), ("proposal_sha256", proposal_sha256, _HEX64),
                      ("audit_v2_sha16", audit_v2_sha16, _HEX16), ("backend_identifier", backend_identifier, _HEX16),
                      ("package_sha256", package_sha256, _HEX64), ("pool_sha16", pool_sha16, _HEX16),
                      ("renders_sha16", renders_sha16, _HEX16), ("ban_sha", ban_sha, _HEX16),
                      ("weights_revision", weights_revision, _HEX40), ("weights_sha256", weights_sha256, _HEX64)):
        if type(v) is not str or not rx.match(v):
            raise ValueError(f"{nm} must be a lower-case hex digest ({rx.pattern})")
    if (not isinstance(m_module_sha256, Mapping) or sorted(m_module_sha256) != sorted(guard.M_HASHED)
            or any(type(v) is not str or not _HEX64.match(v) for v in m_module_sha256.values())):
        raise ValueError(f"m_module_sha256 must map each of {guard.M_HASHED} to its file sha256")
    # PIN (Code, declared at LOCK-m-F3 v0.1): m's path rules for Q-F3 -- G-ID-F3 "cached+uncached";
    # G-TIME-F3 "uncached" (m:293); G-F3 and the campaign the path LOCK-m-F3 v0.2 records.
    allowed = ("cached+uncached",) if stage == "id" else ("uncached",) if stage == "time" else ("cached", "uncached")
    if path not in allowed:
        raise ValueError(f"path {path!r} not allowed for Q-F3 {stage}; allowed {allowed}")
    if type(stop_cap) is not int or stop_cap != STOP_CAP:
        raise ValueError(f"stop_cap must be session_e2a.STOP_CAP = {STOP_CAP} (task rounds stay at 60, m:174)")
    if type(reasoning_cap) is not int or reasoning_cap not in sc_mod.REASONING_CAPS or (
            stage == "time" and reasoning_cap != STOP_CAP):
        raise ValueError(f"reasoning_cap must be one of {sc_mod.REASONING_CAPS} ({STOP_CAP} at G-TIME-F3, m:174)")
    if hour_cap is None:
        if stage == "campaign":
            raise ValueError("a campaign identity carries the PI's hour cap (LOCK-m-F3 v1.0)")
    elif type(hour_cap) not in (int, float) or not hour_cap > 0:
        raise ValueError(f"hour_cap must be a positive int/float or None, got {hour_cap!r}")
    if not isinstance(n, Mapping) or sorted(n) != sorted(ts) or any(type(v) is not int or v < 1 for v in n.values()):
        raise ValueError(f"n must map each template of {ts} to a positive int, got {n!r}")
    kt = keys.key_templates(stage, ts)
    if key_templates is not None and _canon(key_templates) != _canon(kt):
        raise ValueError("key_templates differ from m:159's")
    if pod_id is not None:
        raise ValueError("a Q-F3 identity carries no pod id (a laptop unit; m:267's pod id is an OLMo campaign's)")
    ident = {"unit": unit, "stage": stage, "template_set": ts, "lock_sha256": lock_sha256,
             "schedule_sha256": schedule_sha256, "path": path, "stop_cap": stop_cap, "hour_cap": hour_cap,
             "n": {t: n[t] for t in ts}, "key_templates": kt, "audit_v2_sha16": audit_v2_sha16, "ban_sha": ban_sha,
             "backend_identifier": backend_identifier, "pod_id": None, "proposal_sha256": proposal_sha256,
             "package_sha256": package_sha256, "pool_sha16": pool_sha16, "renders_sha16": renders_sha16,
             "reasoning_cap": reasoning_cap, "m_module_sha256": dict(sorted(m_module_sha256.items())),
             "weights_revision": weights_revision, "weights_sha256": weights_sha256}
    return json.loads(_canon(ident))


def _validated(identity: Mapping) -> dict:
    if not isinstance(identity, Mapping) or tuple(sorted(identity)) != tuple(sorted(IDENTITY_KEYS)):
        raise ValueError(f"a Q-F3 identity's keys are exactly {IDENTITY_KEYS}")
    rebuilt = Identity(**dict(identity))
    if _canon(rebuilt) != _canon(dict(identity)):
        raise ValueError("identity is not in Identity()'s canonical form")
    return rebuilt


def load_or_init(path, identity: Mapping, resume: bool) -> dict:
    """The checkpoint to continue, or a new one (m:267's refusals; m.resume.load_or_init's order with
    Q-F3's identity check)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): m's load_or_init, step for step, its identity validation
    # Q-F3's: an ENDED checkpoint refused first; an end pending re-finished under its own design (the
    # backend identifier may differ: a re-finish generates nothing); without --resume an existing
    # checkpoint refused; with it, any identity difference refused. Q-F3 runs on the laptop with no pod
    # id, so m's pod-change set-aside never arises (pod_id_seen None at every write; a set-aside on a
    # pod change would follow m's rule if one did).
    ident = _validated(identity)
    p = Path(path)
    if not p.exists():
        return m_resume._fresh(ident)
    refuse_ended(p)
    if pending_at(p):
        ck = read_checkpoint(p)
        if pending_end(ck) is not None:
            design = {k: v for k, v in m_resume._identity_diff(ck["identity"], ident).items()
                      if k not in ("backend_identifier", "pod_id")}
            if design:
                raise SystemExit(f"CHECKPOINT MISMATCH: {p} carries an end pending and differs on {sorted(design)}; "
                                 f"a pending end re-finishes only under its own design -- refusing.")
            return ck
    if not resume:
        raise SystemExit(f"CHECKPOINT EXISTS at {p}; pass --resume to continue it or move it aside. A run never "
                         f"silently overwrites one (trap 22).")
    ck = read_checkpoint(p)
    status = ended_status(ck)
    if status is not None:
        raise SystemExit(m_resume._ended_message(p, ck, status))
    if ck["state"]["pod_id_seen"] != m_resume._env_pod():
        raise SystemExit(f"POD CHANGE at {p}: a Q-F3 checkpoint is written on the laptop with no pod id -- refusing")
    diff = m_resume._identity_diff(ck["identity"], ident)
    if diff:
        raise SystemExit(f"CHECKPOINT MISMATCH: {p} differs on {sorted(diff)} (recorded, this run: {diff}). "
                         f"Resuming across a different design would splice two designs -- refusing.")
    return ck


def _selftest(chk) -> None:
    import tempfile

    from . import testing

    base = dict(stage="qual", template_set=["A3s", "A1"], lock_sha256="1" * 64, schedule_sha256="2" * 64,
                path="uncached", hour_cap=None, n={"A1": 4, "A3s": 8}, audit_v2_sha16="7aa235d25eeb66dc",
                ban_sha="3" * 16, backend_identifier="4" * 16, proposal_sha256="5" * 64, reasoning_cap=120,
                weights_revision="6" * 40, weights_sha256="7" * 64)
    ident = Identity(**base)
    chk("mf3.resume: the identity -- Q-F0's keys plus reasoning_cap, m_module_sha256 and the weights binding; "
        "templates in table order; mf3's own package hash",
        tuple(sorted(ident)) == tuple(sorted(IDENTITY_KEYS)) and ident["template_set"] == ["A1", "A3s"]
        and ident["package_sha256"] == guard.package_sha256() and ident["reasoning_cap"] == 120
        and sorted(ident["m_module_sha256"]) == sorted(guard.M_HASHED) and _validated(ident) == ident)
    refused = []
    for kw in ({"reasoning_cap": 90}, {"stage": "time", "path": "uncached", "reasoning_cap": 120},
               {"stage": "time", "path": "cached"}, {"stage": "id", "template_set": ["A2s"], "n": {"A2s": 16},
                                                     "path": "cached+uncached"},
               {"lock_sha256": "pre-lock"}, {"weights_revision": "abc"}, {"pod_id": "pod"},
               {"stage": "campaign", "hour_cap": None}, {"template_set": ["A0"], "n": {"A0": 1}},
               {"stop_cap": 120}):
        try:
            Identity(**{**base, **kw})
            refused.append(False)
        except ValueError:
            refused.append(True)
    chk("mf3.resume: refuses a cap outside 60/120, G-TIME at 120 or cached, G-ID without both templates, a "
        "pre-lock hash, a malformed weights binding, a pod id, a campaign without its hour cap, a Q-F0 "
        "template, a task-round cap other than 60", all(refused), refused)
    with tempfile.TemporaryDirectory() as td:
        cp = Path(td) / "Q-F3_qual.json"
        ck = load_or_init(cp, ident, resume=False)
        recs = [r for c, r, _ in testing.suite() if c.template in ("A1", "A3s")][:1]
        r = json.loads(json.dumps(recs[0]))
        r["verified"] = True
        r["s"] = 0 if r["template"] == "A1" else r["s"]
        ck["provenance"] = [{"stamp": "x", "record": {"adapter": "stub"}, "launched": 1}]
        record_session(ck, r)
        write_checkpoint(cp, ck)
        back = load_or_init(cp, ident, resume=True)
        try:
            load_or_init(cp, ident, resume=False)
            exists = False
        except SystemExit as e:
            exists = "CHECKPOINT EXISTS" in str(e)
        try:
            load_or_init(cp, Identity(**{**base, "reasoning_cap": 60}), resume=True)
            capmove = False
        except SystemExit as e:
            capmove = "reasoning_cap" in str(e)
        try:
            load_or_init(cp, Identity(**{**base, "m_module_sha256": {**ident["m_module_sha256"], "audit": "8" * 64}}),
                         resume=True)
            modmove = False
        except SystemExit as e:
            modmove = "m_module_sha256" in str(e)
    chk("mf3.resume: m's checkpoint machinery on a Q-F3 identity -- a verified F3 record recorded and re-read "
        "skip-only; an existing checkpoint refused without --resume; a resume across a cap change or an m "
        "module change refused", done_ids(back) == {(r["template"], r["s"])} and exists and capmove and modmove)
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / ("c" * 40)
        (d.parent / "blobs").mkdir(parents=True)
        d.mkdir()
        files = {"config.json": "{}", "tokenizer.json": "{}",
                 "model.safetensors.index.json": json.dumps({"weight_map": {"a": "m-1.safetensors"}}),
                 "m-1.safetensors": "w"}
        for f, txt in files.items():
            b = d.parent / "blobs" / hashlib.sha256(txt.encode()).hexdigest()
            b.write_text(txt)
            os.symlink(f"../blobs/{b.name}", d / f)
        wb = weights_binding(d)
        (d.parent / "blobs" / ("e" * 64)).write_text("w2")
        os.remove(d / "m-1.safetensors")
        os.symlink("../blobs/" + "e" * 64, d / "m-1.safetensors")
        wb2 = weights_binding(d)
        os.remove(d / "m-1.safetensors")
        os.symlink("../blobs/" + "f" * 64, d / "m-1.safetensors")
        try:
            weights_binding(d)
            dangling = False
        except ValueError:
            dangling = True
    chk("mf3.resume: the weights binding is the snapshot's revision and the sha256 of its load files' content "
        "addresses; a weight file re-pointed at another blob moves it; a link to an absent blob is refused",
        wb["revision"] == "c" * 40 and len(wb["sha256"]) == 64 and sorted(wb["files"]) == sorted(files)
        and wb2["sha256"] != wb["sha256"] and dangling)
    try:
        refuse_canonical_out(REPO / "data" / "mf3" / "ckpt" / "x.json")
        canon = False
    except SystemExit:
        canon = True
    chk("mf3.resume: a stub run is refused under data/mf3 (and m's canonical roots)", canon)
