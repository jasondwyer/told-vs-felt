"""PROPOSAL-m resume identity and atomic checkpoints (v1.11 §2.7 m:267; §2.4's units
and pod sessions, m:250-251).

RESUME IDENTITY (m:267). "Resume identity (every campaign and gate stage): the unit's
lock hash, schedule hash, path (cached/uncached), cap, look index, backend identifier
and, for an OLMo campaign, the pod instance id ... a resume refuses any change of seed
or n and only skips sessions already complete on disk ('skip-only'); checkpoints are
written atomically (temp file, fsync, rename)." Departures from recon's checkpoint
(recon.py:427-547, frozen; maps/runner.md §1, §9): n IS in the identity (recon
excludes it by design); equality is exact and two-way with no legacy defaults; the
write fsyncs the file and its directory; the JSON encoder refuses every non-native
object instead of ``default=float`` (which turned numpy ints into floats silently).

THE LOOK INDEX is state, not identity: it changes during a run, so it is stored beside
the identity and verified as ``look_index == completed_launches // 40`` on every load
and write (maps/runner.md §10 item 5). A campaign records the look due at a multiple
of 40 in the same atomic write as the session that made it due, so the invariant
holds on disk at every instant.

PODS (m:251, m:267). The backend identifier is a projection of the adapter's
provenance record; it cannot tell two boxes of one class apart, so an OLMo campaign
carries the pod instance id IN its identity and a resume on another pod is a hard
refusal (the campaign restarts under its lock on the new box, at a new checkpoint path
the operator chooses -- never spliced, CLAUDE.md's consistency clause). A gate stage
carries no pod id; its checkpoint records ``pod_id_seen`` at every write, and a resume
of an UNFINISHED, UNSTOPPED gate stage on another pod sets the old checkpoint aside
(renamed, never deleted -- recon's ``.cedar-timing`` precedent) and restarts the stage
from its first session under its deterministic keys (build pin 2). Every OLMo stage
requires the pod id at its start (stages.py).

HOUR CAP (m:251): wall-clock of detached generation time, accumulated per session in
integer milliseconds and persisted in the checkpoint, so time spent before a resume
counts after it.

ENDED STAGES (m:267 restarts a gate stage only when a pod change INTERRUPTS it; m:271,
m:302: a fire stops, a pause waits for the seat). A gate stage persists its end
(``stage_end``: PASS / STOP / PAUSE / FAIL / NOT-DETERMINED) and any hair-trigger
``stop`` in its checkpoint; a campaign its ``campaign.terminal`` (or a ``stop``, or the
pause that ends an invocation). EVERY finish takes three steps (finding R1): FIRST the
end computed in memory is written as ``end_pending`` (status, fired bars, the stop with
the fired session's identifiers or the G-VER-quarantined record; a campaign's terminal
state, end look and pause) in the same atomic write as every session the invocation
recorded -- the fired one included; THEN the stage's pick-free outputs are written;
THEN ``persist_end`` flips the pending end into its final form (``apply_end``) and
clears it. A checkpoint carrying ``end_pending`` is RE-FINISH-ONLY: ``load_or_init``
returns it on any pod, with or without --resume (its design must be the recorded one;
the backend identifier and the pod id may differ -- nothing generates), never sets it
aside, and the driver re-derives its outputs from the checkpoint byte-identically and
persists the end; ``record_session`` records nothing past it, and a write on another
pod is admitted only when it records no session (``_finish_only``). A checkpoint that
carries a persisted end is never resumed, re-run or set aside on another pod: the
refusal names its status (``refuse_ended``) and, for a STOP, only the stop's BLINDED
class -- a contrast session's free-phase trigger by phase alone (m:318 exception (1)),
exactly as its announcement. Only a FINISHED, VERIFIED session is recorded
(``record_session`` refuses a record whose ``verified`` is not exactly True, m:284).

PROVENANCE (CLAUDE.md ledger 27). ``adapter.provenance()`` (pick-free: library
versions, device, determinism flags) is recorded VERBATIM in the checkpoint's
``provenance`` list, outside the identity, one entry per invocation with its UTC stamp
and ``launched``: the sessions launched and recorded (or quarantined) by this
invocation; a session interrupted mid-generation is not counted (its launch never
reaches disk -- ``append_provenance`` / ``note_launch``; finding R5).

CODE AND RENDERS (m:267's lock hash binds them through the lock; the identity binds
them directly too): the identity carries ``package_sha256`` (the m package's sources)
and the pool's and renders' sha16, so a code or render change between invocations
refuses a resume.
"""
from __future__ import annotations

import copy
import errno
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

from ..session_e2a import STOP_CAP
from . import keys

REPO = Path(__file__).resolve().parents[2]
SCHEMA = "m-checkpoint-v1"
SESSION_SCHEMA = "m-session-v1"
GATE_STAGES = ("time", "id", "qual")
STAGES = GATE_STAGES + ("campaign",)
LOOK_EVERY = 40                                  # looks every 40 launches (§6)
POD_ENV = "RUNPOD_POD_ID"
IDENTITY_KEYS = ("unit", "stage", "template_set", "lock_sha256", "schedule_sha256", "path",
                 "stop_cap", "hour_cap", "n", "key_templates", "audit_v2_sha16", "ban_sha",
                 "backend_identifier", "pod_id", "proposal_sha256", "package_sha256",
                 "pool_sha16", "renders_sha16")
# PIN (Code, declared at LOCK v0.1): the statuses a gate stage's persisted end may
# carry (stage_end.status); G-ID's verdicts are its PASS / FAIL / NOT-DETERMINED.
STAGE_END_STATUSES = ("PASS", "STOP", "PAUSE", "FAIL", "NOT-DETERMINED")
# PIN (Code, declared at LOCK v0.1; finding R1): the pending end of a finish, written
# with every session before any output and cleared by persist_end. A gate stage's holds
# {status, fired, stop}; a campaign's also {terminal, end_look, pause} (the status of an
# invocation's end: STOP, PAUSE, or a terminal state).
END_PENDING = "end_pending"
PENDING_KEYS_GATE = ("fired", "status", "stop")
PENDING_KEYS_CAMPAIGN = ("end_look", "fired", "pause", "status", "stop", "terminal")
CAMPAIGN_END_STATUSES = ("STOP", "PAUSE", "COMPLETE", "CAP", "PI-STOP")
PACKAGE_DIR = Path(__file__).resolve().parent
# PIN (Code, declared at LOCK v0.1): the backend identifier is the sha16 of the
# compact sort-keyed JSON of adapter.provenance() minus these keys: the runtime
# counter n_encodes_clipped, the per-checkpoint weights path, and the seed (a run
# input, carried by the key templates). Everything else stays, the Qwen `platform`
# string (OS build) included: an OS update on the laptop is a backend change.
# Disclosed: it cannot tell two boxes of one class apart (m:267) -- hence the pod id.
BACKEND_DROP = ("n_encodes_clipped", "path", "seed")
# PIN (Code, declared at LOCK v0.1): stub/selftest output is refused under these
# roots, resolved (symlinks and '..' followed) and REPO-anchored; data/olmo is the
# precedent's own protected root (box_selftest_stub.py:171-182), kept.
CANONICAL_ROOTS = (REPO / "data" / "m", Path("/workspace/models"), REPO / "data" / "olmo")

_HEX64 = re.compile(r"^[0-9a-f]{64}$")
_HEX16 = re.compile(r"^[0-9a-f]{16}$")
_AUTO = object()


# --- JSON, strictly native ----------------------------------------------------------
def _assert_native(obj: Any, where: str = "$") -> None:
    """Exact JSON-native types only: no numpy scalars (np.float64 subclasses float and
    would pass json silently), no non-str dict keys (json coerces them)."""
    t = type(obj)
    if obj is None or t in (str, bool, int, float):
        return
    if t in (list, tuple):
        for i, x in enumerate(obj):
            _assert_native(x, f"{where}[{i}]")
        return
    if t is dict:
        for k, v in obj.items():
            if type(k) is not str:
                raise TypeError(f"{where}: dict key {k!r} ({type(k).__name__}) is not a str")
            _assert_native(v, f"{where}.{k}")
        return
    raise TypeError(f"{where}: {t.__module__}.{t.__name__} is not JSON-native; convert it "
                    f"explicitly in the builder (no silent float conversion)")


def _refuse(o: Any) -> Any:
    raise TypeError(f"{type(o).__module__}.{type(o).__name__} is not JSON-native")


def _canon(x: Any) -> str:
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                      default=_refuse, allow_nan=False)


def _fsync_dir(d: Path) -> None:
    fd = os.open(d, os.O_RDONLY)
    try:
        os.fsync(fd)
    except OSError as e:
        # PIN (Code, declared at LOCK v0.1): a filesystem that cannot sync a directory
        # (EINVAL / ENOTSUP, seen on some network volumes) is tolerated -- the rename is
        # still atomic and the file itself was fsynced; any other error raises. Verify
        # on the box's /workspace volume.
        if e.errno not in (errno.EINVAL, errno.ENOTSUP, getattr(errno, "EOPNOTSUPP", errno.ENOTSUP)):
            raise
    finally:
        os.close(fd)


def json_text(obj: Any, *, indent: int | None = None) -> str:
    """The exact text ``atomic_write_json`` writes for ``obj`` (native types checked), so
    a caller can compare an existing file with what a write would put there."""
    _assert_native(obj)
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, default=_refuse,
                      allow_nan=False, indent=indent) + "\n"


def atomic_write_json(path: str | os.PathLike, obj: Any, *, indent: int | None = None) -> None:
    """Write ``path.tmp``, flush, fsync, ``os.replace``, fsync the directory (m:267).

    Serialization happens before the disk is touched, so a refused object leaves the
    old file exactly as it was and no temp file behind.

    PIN (Code, declared at LOCK v0.1): exact JSON-native types only (np.float64 is
    refused although json would take it), str dict keys only, NaN/Infinity refused.
    """
    p = Path(path)
    data = json_text(obj, indent=indent)
    tmp = p.with_name(p.name + ".tmp")
    try:
        with open(tmp, "w", encoding="utf-8") as fh:
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
    _fsync_dir(p.parent)


# --- backend and pod ------------------------------------------------------------
def backend_identifier(provenance: Mapping[str, Any]) -> str:
    if not isinstance(provenance, Mapping) or not provenance:
        raise ValueError("backend_identifier needs the adapter's provenance record")
    body = {k: v for k, v in provenance.items() if k not in BACKEND_DROP}
    _assert_native(body)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()[:16]


def _env_pod() -> str | None:
    v = (os.environ.get(POD_ENV) or "").strip()
    return v or None


def pod_id() -> str | None:
    """The pod instance id, or None off a pod.

    PIN (Code, declared at LOCK v0.1): read from the RUNPOD_POD_ID environment variable
    (empty or whitespace = absent); verify on the box before the first OLMo stage.
    """
    return _env_pod()


# --- provenance (ledger 27) ------------------------------------------------------
PROVENANCE_ENTRY_KEYS = ("launched", "record", "stamp")


def utc_stamp() -> str:
    """An invocation's stamp: UTC, to the second (Code's stamp; the hash is the record)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def provenance_record(provenance: Mapping[str, Any]) -> dict:
    """``adapter.provenance()`` VERBATIM as a JSON-native dict (tuples become lists, as
    JSON has them); a non-native value refuses (TypeError) rather than being converted."""
    if not isinstance(provenance, Mapping) or not provenance:
        raise ValueError("provenance: the adapter's provenance record is required")
    return json.loads(_canon(dict(provenance)))


def append_provenance(ckpt: dict, provenance: Mapping[str, Any], *, stamp: str | None = None) -> dict:
    """Append this invocation's entry {stamp, record (verbatim), launched 0} to the
    checkpoint's ``provenance`` list (in memory; the next write persists it).

    PIN (Code, declared at LOCK v0.1): one entry per invocation that reaches its
    checkpoint (a start, every resume, a finish-only re-invocation), kept OUTSIDE the
    identity, never edited afterwards except its own ``launched`` counter -- the
    sessions launched and recorded (or quarantined) by this invocation; a session
    interrupted mid-generation is not counted (finding R5). A gate stage restarted after
    a pod change starts a new list (the set-aside file keeps the old).
    """
    if "provenance" not in ckpt and ckpt.get("sessions"):
        raise ValueError("append_provenance: a checkpoint with sessions and no provenance list "
                         "was not written by this package's drivers -- refusing")
    entry = {"stamp": stamp if stamp is not None else utc_stamp(),
             "record": provenance_record(provenance), "launched": 0}
    ckpt.setdefault("provenance", []).append(entry)
    return entry


def note_launch(ckpt: dict) -> None:
    """Count one session launch against this invocation's provenance entry, in memory.

    PIN (Code, declared at LOCK v0.1; finding R5): the count reaches disk with the next
    write -- the session's record, or the end pending that quarantines a G-VER record --
    so ``launched`` means "sessions launched and recorded (or quarantined) by this
    invocation"; a session interrupted mid-generation is not counted.
    """
    prov = ckpt.get("provenance")
    if not prov:
        raise ValueError("note_launch: no provenance entry for this invocation (append_provenance "
                         "runs at every stage start)")
    prov[-1]["launched"] += 1


def report_provenance(ckpt: Mapping) -> list[dict]:
    """The provenance a stage report copies.

    PIN (Code, declared at LOCK v0.1): the entries of the invocations that launched and
    recorded (or quarantined) at least one session -- the backends that produced the
    stage's records and stops. An invocation that recorded nothing (a finish-only
    re-invocation, a PI stop, one whose only session was interrupted mid-generation --
    finding R5) stays in the checkpoint's list only, so a re-finish re-derives a
    byte-identical report.
    """
    return [json.loads(_canon(e)) for e in ckpt.get("provenance") or [] if e["launched"] > 0]


# --- code, pool and renders bound into the identity -----------------------------
def package_sha256_of(root: str | os.PathLike) -> str:
    """sha256 over the sorted (relative path, bytes) of ``root``'s ``*.py`` files.

    PIN (Code, declared at LOCK v0.1): each file contributes ``{rel path}\\n{len}\\n``
    then its bytes, rel path relative to REPO (posix form) where the file lies under
    REPO, else to ``root``'s parent; files sorted by that path; ``__pycache__`` is not
    a ``*.py`` file of the directory and never enters.
    """
    d = Path(root).resolve()
    h = hashlib.sha256()
    entries = []
    for f in sorted(d.glob("*.py")):
        try:
            rel = f.relative_to(REPO).as_posix()
        except ValueError:
            rel = f.relative_to(d.parent).as_posix()
        entries.append((rel, f.read_bytes()))
    if not entries:
        raise ValueError(f"package_sha256: no *.py file under {d}")
    for rel, data in sorted(entries):
        h.update(f"{rel}\n{len(data)}\n".encode("utf-8"))
        h.update(data)
    return h.hexdigest()


@lru_cache(maxsize=1)
def package_sha256() -> str:
    """The m package's sources (valence_core/m/*.py), hashed once per process.

    PIN (Code, declared at LOCK v0.1): computed at its first call in a process and
    cached, so one invocation binds one value; a change between invocations moves it.
    """
    return package_sha256_of(PACKAGE_DIR)


_package_sha256 = package_sha256                 # Identity's parameter shadows the name


def pool_sha16(pool) -> str:
    """sha16 of the served pool items (compact sort-keyed JSON of the list).

    PIN (Code, declared at LOCK v0.1): computed over the items a stage serves (not the
    pools file, whose sha prefix corr.load_pool already pins).
    """
    return hashlib.sha256(json.dumps(list(pool), sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()[:16]


_pool_sha16 = pool_sha16


def _of_record_shas() -> tuple[str, str]:
    from . import corr, scaffold                 # lazy: no import cycle at module load
    pool, renders = scaffold.pool_and_renders()
    return _pool_sha16(pool), corr.renders_sha(renders)


# --- identity -------------------------------------------------------------------
def _key_templates(unit: str, stage: str, template_set: list[str]) -> dict:
    """m:159's key templates for this stage, rendered with literal {s}/{b} fields."""
    gate = keys.item_gate(stage)
    out = {}
    for t in template_set:
        out[t] = {"arm": keys.arm_key(unit, stage, t, "{s}"),
                  "items": keys.item_key(unit, "{s}", gate),
                  "sched": (keys.sched_key(unit, t, "{b}") if stage == "campaign"
                            else keys.gate_sched_key(unit, gate, t))}
    return out


def _num_ok(x: Any) -> bool:
    return type(x) in (int, float) and x > 0


def Identity(*, unit: str, stage: str, template_set, lock_sha256: str, schedule_sha256: str,
             path: str, hour_cap, n: Mapping[str, int], audit_v2_sha16: str, ban_sha: str,
             backend_identifier: str, proposal_sha256: str, stop_cap: int = STOP_CAP,
             key_templates: Mapping | None = None, pod_id: Any = _AUTO,
             package_sha256: Any = _AUTO, pool_sha16: Any = _AUTO,
             renders_sha16: Any = _AUTO) -> dict:
    """Build and validate a resume identity (DESIGN §1.9's keys, m:267's contents).

    Returns a plain JSON-native dict, so a recorded identity and a rebuilt one compare
    exactly. ``key_templates`` is derived from m:159 through ``keys``; a supplied value
    must equal the derivation. ``pod_id`` defaults to the environment's for an OLMo
    campaign (required there) and to None everywhere else (forbidden there).
    ``package_sha256`` / ``pool_sha16`` / ``renders_sha16`` default to this process's
    package and the pool and renders of record (a stage passes the values it serves).
    """
    tpls = keys.templates(unit)                  # ValueError unknown, NotImplementedError Q-F3
    sub = "qwen" if unit == "Q-F0" else "olmo"
    if stage not in STAGES or (sub == "olmo" and stage == "id"):
        raise ValueError(f"stage {stage!r} is not a stage of {unit!r}")
    ts = list(template_set)
    if not ts or len(set(ts)) != len(ts) or any(t not in tpls for t in ts):
        raise ValueError(f"template_set {ts!r} must be distinct templates of {unit!r} {tpls}")
    # PIN (Code, declared at LOCK v0.1): template_set is stored in §2.4's table order
    # (contrast first), whatever order the caller lists it in.
    ts = [t for t in tpls if t in ts]
    if stage == "id" and ts != ["A0s"]:
        raise ValueError("G-ID-F0m runs the A0s template only (m:281)")
    # PIN (Code, declared at LOCK v0.1): the identity machinery keeps DESIGN §1.9's
    # "pre-lock" for a stage run before its governing lock; every stage stages.py
    # builds follows its lock (m:279-286, m:302) and refuses "pre-lock" itself.
    if not (lock_sha256 == "pre-lock" or (type(lock_sha256) is str and _HEX64.match(lock_sha256))):
        raise ValueError("lock_sha256 must be a sha256 hex digest or 'pre-lock'")
    if package_sha256 is _AUTO:
        package_sha256 = _package_sha256()
    if pool_sha16 is _AUTO or renders_sha16 is _AUTO:
        p16, r16 = _of_record_shas()
        pool_sha16 = p16 if pool_sha16 is _AUTO else pool_sha16
        renders_sha16 = r16 if renders_sha16 is _AUTO else renders_sha16
    for nm, v, rx in (("schedule_sha256", schedule_sha256, _HEX64),
                      ("proposal_sha256", proposal_sha256, _HEX64),
                      ("audit_v2_sha16", audit_v2_sha16, _HEX16),
                      ("backend_identifier", backend_identifier, _HEX16),
                      ("package_sha256", package_sha256, _HEX64),
                      ("pool_sha16", pool_sha16, _HEX16),
                      ("renders_sha16", renders_sha16, _HEX16)):
        if type(v) is not str or not rx.match(v):
            raise ValueError(f"{nm} must be a lower-case hex digest ({rx.pattern})")
    if type(ban_sha) is not str or not (_HEX16.match(ban_sha) or _HEX64.match(ban_sha)):
        raise ValueError("ban_sha must be a sha16 or sha256 hex digest")
    # PIN (Code, declared at LOCK v0.1): G-ID's path is "cached+uncached" (it runs both
    # at every index); OLMo and G-TIME-F0 are "uncached" by spec (m:267, m:280).
    allowed = (("cached+uncached",) if stage == "id"
               else ("uncached",) if sub == "olmo" or stage == "time"
               else ("cached", "uncached"))
    if path not in allowed:
        raise ValueError(f"path {path!r} not allowed for {unit} {stage}; allowed {allowed}")
    if type(stop_cap) is not int or stop_cap != STOP_CAP:
        raise ValueError(f"stop_cap must be session_e2a.STOP_CAP = {STOP_CAP}")
    # PIN (Code, declared at LOCK v0.1): a campaign carries the PI's hour cap from its
    # LOCK v1.0 (required); a gate stage may carry none.
    if hour_cap is None:
        if stage == "campaign":
            raise ValueError("a campaign identity carries the PI's hour cap (LOCK v1.0)")
    elif not _num_ok(hour_cap):
        raise ValueError(f"hour_cap must be a positive int/float or None, got {hour_cap!r}")
    if not isinstance(n, Mapping) or sorted(n) != sorted(ts) or any(
            type(v) is not int or v < 1 for v in n.values()):
        raise ValueError(f"n must map each template of {ts} to a positive int, got {n!r}")
    kt = _key_templates(unit, stage, ts)
    if key_templates is not None and _canon(key_templates) != _canon(kt):
        raise ValueError(f"key_templates differ from m:159's: {key_templates!r} != {kt!r}")
    olmo_campaign = sub == "olmo" and stage == "campaign"
    if pod_id is _AUTO:
        pod_id = _env_pod() if olmo_campaign else None
    if olmo_campaign:
        if type(pod_id) is not str or not pod_id:
            raise SystemExit(f"POD ID ABSENT: an OLMo campaign cannot start or resume without "
                             f"its pod instance id (${POD_ENV}); m:267")
    elif pod_id is not None:
        raise ValueError("only an OLMo campaign carries a pod id in its identity (m:267)")
    ident = {"unit": unit, "stage": stage, "template_set": ts, "lock_sha256": lock_sha256,
             "schedule_sha256": schedule_sha256, "path": path, "stop_cap": stop_cap,
             "hour_cap": hour_cap, "n": {t: n[t] for t in ts}, "key_templates": kt,
             "audit_v2_sha16": audit_v2_sha16, "ban_sha": ban_sha,
             "backend_identifier": backend_identifier, "pod_id": pod_id,
             "proposal_sha256": proposal_sha256, "package_sha256": package_sha256,
             "pool_sha16": pool_sha16, "renders_sha16": renders_sha16}
    return json.loads(_canon(ident))


def _validated(identity: Mapping) -> dict:
    if not isinstance(identity, Mapping) or tuple(sorted(identity)) != tuple(sorted(IDENTITY_KEYS)):
        got = sorted(identity) if isinstance(identity, Mapping) else type(identity).__name__
        raise ValueError(f"identity keys must be exactly {IDENTITY_KEYS}; got {got}")
    rebuilt = Identity(**dict(identity))
    if _canon(rebuilt) != _canon(dict(identity)):
        raise ValueError("identity is not in Identity()'s canonical form (template order, "
                         "key templates or value types differ)")
    return rebuilt


def _identity_diff(recorded: Mapping, current: Mapping) -> dict:
    """Two-way, exact: every key of either side, values compared as canonical JSON
    (so 8 and 8.0, or a list and a reordered list, differ)."""
    out = {}
    for k in sorted(set(recorded) | set(current)):
        a, b = recorded.get(k, "<absent>"), current.get(k, "<absent>")
        if k not in recorded or k not in current or _canon(a) != _canon(b):
            out[k] = (a, b)
    return out


# --- checkpoint body ------------------------------------------------------------
def _fresh(ident: dict) -> dict:
    return {"schema": SCHEMA, "identity": ident,
            "state": {"look_index": 0, "hour_cap_ms_used": 0, "pod_id_seen": _env_pod(),
                      "n_writes": 0, "set_aside": []},
            "looks": [], "sessions": []}


def _ms(seconds: Any) -> int:
    if type(seconds) not in (int, float) or not seconds >= 0:
        raise ValueError(f"session seconds must be a non-negative int/float, got {seconds!r}")
    return int(Fraction(seconds) * 1000 + Fraction(1, 2))     # half-up to the millisecond


def session_ms(rec: Mapping) -> int:
    """A finished session's generation time in integer ms, as the hour cap counts it."""
    return _ms(rec.get("seconds"))


def _rec_id(rec: Mapping, stage: str) -> tuple:
    t, s = rec.get("template"), rec.get("s")
    if type(t) is not str or type(s) is not int:
        raise ValueError("a session record carries template (str) and s (int)")
    if stage == "id":
        if rec.get("path") not in ("cached", "uncached"):
            raise ValueError("a G-ID session record carries path 'cached' or 'uncached'")
        return (t, s, rec["path"])
    return (t, s)


def _check_state(ck: Mapping, where: str = "checkpoint") -> None:
    """Every invariant a checkpoint holds on disk; SystemExit names the first broken."""
    def bad(msg: str) -> None:
        raise SystemExit(f"CHECKPOINT STATE INCONSISTENT ({where}): {msg} -- refusing")

    if ck.get("schema") != SCHEMA:
        bad(f"schema {ck.get('schema')!r} != {SCHEMA!r}")
    ident, st = ck.get("identity"), ck.get("state")
    sessions, looks = ck.get("sessions"), ck.get("looks")
    if not isinstance(ident, dict) or not isinstance(st, dict) or type(sessions) is not list \
            or type(looks) is not list:
        bad("identity/state/sessions/looks missing or mistyped")
    for k in ("look_index", "hour_cap_ms_used", "n_writes"):
        if type(st.get(k)) is not int or st[k] < 0:
            bad(f"state.{k} = {st.get(k)!r}")
    if "pod_id_seen" not in st or not (st["pod_id_seen"] is None or type(st["pod_id_seen"]) is str):
        bad("state.pod_id_seen missing or mistyped")
    stage = ident.get("stage")
    ids = set()
    ms = 0
    for i, rec in enumerate(sessions):
        if not isinstance(rec, dict) or rec.get("schema") != SESSION_SCHEMA:
            bad(f"session {i} is not an {SESSION_SCHEMA} record")
        if rec.get("unit") != ident.get("unit") or rec.get("stage") != stage:
            bad(f"session {i} belongs to {rec.get('unit')!r}/{rec.get('stage')!r}")
        try:
            rid = _rec_id(rec, stage)
            ms += _ms(rec.get("seconds"))
        except ValueError as e:
            bad(f"session {i}: {e}")
        if rid in ids:
            bad(f"session {i} is a duplicate of one already on disk")
        ids.add(rid)
        if rid[0] not in ident.get("template_set", ()) or not 0 <= rid[1] < ident["n"][rid[0]]:
            bad(f"session {i} lies outside the identity's templates or n (an orphan)")
        if rec.get("verified") is not True:
            bad(f"session {i} is not a verified record (G-VER runs before a record is written, m:284)")
    if ms != st["hour_cap_ms_used"]:
        bad(f"hour_cap_ms_used {st['hour_cap_ms_used']} != the sessions' {ms} ms")
    if "provenance" in ck:
        prov = ck["provenance"]
        if type(prov) is not list or not all(
                type(e) is dict and tuple(sorted(e)) == PROVENANCE_ENTRY_KEYS
                and type(e["stamp"]) is str and e["stamp"] and type(e["record"]) is dict and e["record"]
                and type(e["launched"]) is int and e["launched"] >= 0 for e in prov):
            bad("provenance is not a list of {stamp, record, launched} entries")
        # PIN (Code, declared at LOCK v0.1): every recorded session was launched by some
        # invocation on the list; the sum can exceed the sessions by the G-VER-quarantined
        # launches (counted, never recorded as sessions). A session interrupted
        # mid-generation is counted nowhere (finding R5).
        if sum(e["launched"] for e in prov) < len(sessions):
            bad(f"the provenance entries launched {sum(e['launched'] for e in prov)} sessions; "
                f"{len(sessions)} are recorded")
    end = ck.get("stage_end")
    if end is not None:
        if stage not in GATE_STAGES:
            bad("only a gate stage records a stage_end (a campaign records campaign.terminal)")
        if (not isinstance(end, dict) or sorted(end) != ["adjudication", "fired", "status"]
                or end["status"] not in STAGE_END_STATUSES or type(end["fired"]) is not list
                or not all(type(x) is str for x in end["fired"])
                or not (end["adjudication"] is None or type(end["adjudication"]) is str)):
            bad(f"stage_end malformed: {end!r}")
    if END_PENDING in ck:
        msg = _pending_problem(ck, stage)
        if msg:
            bad(msg)
    if stage == "campaign":
        # PIN (Code, declared at LOCK v0.1): look_index == completed_launches // 40,
        # with the look due at a multiple of 40 recorded in the same write.
        if st["look_index"] != len(sessions) // LOOK_EVERY or len(looks) != st["look_index"]:
            bad(f"look_index {st['look_index']} / {len(looks)} looks vs {len(sessions)} "
                f"launches (expected {len(sessions) // LOOK_EVERY})")
        for i, lk in enumerate(looks):
            if not isinstance(lk, dict) or lk.get("look_index") != i \
                    or lk.get("at_launches") != LOOK_EVERY * (i + 1):
                bad(f"look {i} is not the look at launch {LOOK_EVERY * (i + 1)}")
    elif st["look_index"] != 0 or looks:
        bad("a gate stage records no looks")


def _pending_problem(ck: Mapping, stage: Any) -> str | None:
    """What is wrong with a checkpoint's end_pending block (None = well formed)."""
    pe = ck.get(END_PENDING)
    gate = stage in GATE_STAGES
    want = PENDING_KEYS_GATE if gate else PENDING_KEYS_CAMPAIGN
    if not isinstance(pe, dict) or tuple(sorted(pe)) != want:
        return f"end_pending malformed (keys {sorted(pe) if isinstance(pe, dict) else type(pe).__name__})"
    if pe["status"] not in (STAGE_END_STATUSES if gate else CAMPAIGN_END_STATUSES):
        return f"end_pending status {pe['status']!r}"
    if type(pe["fired"]) is not list or not all(type(x) is str for x in pe["fired"]):
        return "end_pending fired is not a list of bar names"
    if not (pe["stop"] is None or (type(pe["stop"]) is dict and type(pe["stop"].get("bar")) is str)):
        return "end_pending stop malformed"
    if pe["stop"] is not None and pe["status"] != "STOP":
        return "end_pending carries a stop under a status other than STOP"
    if not gate and pe["status"] == "STOP" and pe["stop"] is None:
        return "a campaign's STOP pending without its stop (a campaign stops on a hair trigger or G-VER only)"
    if ck.get("stage_end") is not None or ck.get("stop"):
        return "an end pending beside a persisted end"
    if not gate:
        camp = ck.get("campaign")
        if not isinstance(camp, dict) or camp.get("terminal") is not None:
            return "a campaign's end pending beside a persisted terminal state (or no campaign block)"
        for k in ("terminal", "end_look", "pause"):
            if not (pe[k] is None or type(pe[k]) is dict):
                return f"end_pending {k} malformed"
    return None


def _read(p: Path) -> dict:
    try:
        ck = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError) as e:
        raise SystemExit(f"CHECKPOINT UNREADABLE at {p} ({type(e).__name__}); it is left "
                         f"untouched -- refusing (never overwrite what cannot be read)")
    if not isinstance(ck, dict):
        raise SystemExit(f"CHECKPOINT UNREADABLE at {p} (not a JSON object) -- refusing")
    _check_state(ck, str(p))
    return ck


def read_checkpoint(path: str | os.PathLike) -> dict:
    """A checkpoint on disk, its invariants checked (SystemExit when unreadable)."""
    return _read(Path(path))


def ended_status(ck: Mapping) -> str | None:
    """The status a checkpoint ENDED with, or None for an unfinished one.

    A hair-trigger ``stop`` -> "STOP"; a gate stage's ``stage_end`` -> its status; a
    campaign's ``campaign.terminal`` -> its status (COMPLETE, CAP, PI-STOP). An end that
    is only PENDING (``end_pending``) has not ended: it is re-finished, never refused
    (``pending_end``; finding R1).
    """
    if ck.get("stop"):
        return "STOP"
    end = ck.get("stage_end")
    if isinstance(end, Mapping) and end.get("status"):
        return str(end["status"])
    camp = ck.get("campaign")
    if isinstance(camp, Mapping) and isinstance(camp.get("terminal"), Mapping):
        return str(camp["terminal"].get("status"))
    return None


def pending_end(ck: Mapping) -> dict | None:
    """The end a finish computed and wrote with its sessions before any output, or None
    (finding R1): a checkpoint carrying one is re-finish-only."""
    pe = ck.get(END_PENDING) if isinstance(ck, Mapping) else None
    return pe if isinstance(pe, dict) else None


def pending_at(path: str | os.PathLike) -> bool:
    """Does the checkpoint at ``path`` carry an end pending? Read tolerantly: an absent or
    unreadable file is False (load_or_init refuses the unreadable one itself)."""
    p = Path(path)
    if not p.is_file():
        return False
    try:
        ck = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    return pending_end(ck) is not None


def set_end_pending(ckpt: dict, pending: Mapping) -> None:
    """Record a finish's computed end in memory; the next write persists it in the same
    atomic write as every session the invocation recorded (finding R1)."""
    if pending_end(ckpt) is not None or ended_status(ckpt) is not None:
        raise ValueError("set_end_pending: the checkpoint already carries an end (pending or persisted)")
    ckpt[END_PENDING] = json.loads(_canon(dict(pending)))
    msg = _pending_problem(ckpt, ckpt["identity"]["stage"])
    if msg:
        del ckpt[END_PENDING]
        raise ValueError(f"set_end_pending: {msg}")


def apply_end(ckpt: dict) -> dict:
    """The pending end in its persisted form, applied in place (returns ``ckpt``).

    PIN (Code, declared at LOCK v0.1; finding R1): a gate stage gains ``stage_end``
    {status, fired, adjudication None} and the ``stop`` (hair trigger: the fired round's
    identifiers; G-VER: the quarantined record); a campaign gains the ``stop``, its
    ``terminal`` state, its ``end_look`` and the pause that ended the invocation
    (appended to ``campaign.pauses``). ``end_pending`` is removed. Deterministic, so a
    re-finish applies the same block to the same checkpoint and re-derives the same
    outputs.
    """
    pe = pending_end(ckpt)
    if pe is None:
        raise ValueError("apply_end: no end pending")
    del ckpt[END_PENDING]
    if pe["stop"] is not None:
        ckpt["stop"] = copy.deepcopy(pe["stop"])
    if ckpt["identity"]["stage"] in GATE_STAGES:
        ckpt["stage_end"] = {"status": pe["status"], "fired": list(pe["fired"]), "adjudication": None}
    else:
        camp = ckpt["campaign"]
        for k in ("terminal", "end_look"):
            if pe[k] is not None:
                camp[k] = copy.deepcopy(pe[k])
        if pe["pause"] is not None:
            camp["pauses"].append(copy.deepcopy(pe["pause"]))
    return ckpt


def persist_end(path: str | os.PathLike, final: dict) -> None:
    """A finish's LAST write: ``final`` must be exactly ``apply_end`` of the checkpoint
    on disk, which must carry the end pending -- the write flips the pending end into
    its persisted form and changes nothing else (no session, no look)."""
    p = Path(path)
    disk = _read(p)
    if pending_end(disk) is None:
        raise ValueError(f"persist_end: {p} carries no end pending")
    if _canon(apply_end(copy.deepcopy(disk))) != _canon(final):
        raise ValueError(f"persist_end: the checkpoint offered is not the persisted form of the end "
                         f"pending at {p} -- refusing")
    write_checkpoint(p, final)


def same_json(a: Any, b: Any) -> bool:
    """Equal as canonical JSON (a pending end recorded vs one re-derived)."""
    return _canon(a) == _canon(b)


def _stop_words(ck: Mapping) -> str:
    """A stored stop as its announcement printed it: the BLINDED class only.

    PIN (Code, declared at LOCK v0.1): a refusal names a stop's class from the stop's
    blinded block alone. Where the blinded class differs from the recorded one (a
    contrast session's free-phase hair trigger), the stop is named by phase alone --
    template and s, as the STOP announcement printed them, never the class, round, n or
    index (m:318 exception (1)); a stop with no blinded block names no class at all.
    """
    stop = ck.get("stop")
    bl = stop.get("blinded") if isinstance(stop, Mapping) else None
    if not isinstance(bl, Mapping) or not bl.get("bar"):
        return "STOP"
    if bl.get("bar") != stop.get("bar"):
        return (f"STOP: a hair trigger fired in the free phase of a contrast session "
                f"({bl.get('template')} s={bl.get('s')}); its class is withheld (m:318 exception (1))")
    return f"STOP, {bl['bar']}"


def _ended_message(p: Path, ck: Mapping, status: str) -> str:
    stage = (ck.get("identity") or {}).get("stage")
    if status == "STOP":
        return (f"STAGE ENDED at {p} ({_stop_words(ck)}): a resume never lifts a "
                f"STOP -- the seat adjudicates and re-specifies (m:271); it is never resumed, "
                f"re-run or restarted on another pod or path")
    if stage == "campaign":
        return (f"CAMPAIGN ENDED at {p} ({status}); terminal (m:247) -- it is never resumed, "
                f"re-run or restarted on another pod or path")
    return (f"STAGE ENDED at {p} ({status}): a finished gate stage is never resumed, re-run or "
            f"set aside on another pod (m:267 restarts only an interrupted one); its end is the "
            f"seat's record")


def refuse_ended(path: str | os.PathLike) -> None:
    """SystemExit naming the status when the checkpoint at ``path`` has ENDED (stopped,
    finished gate stage, terminal campaign); nothing when it is absent or unfinished.

    PIN (Code, declared at LOCK v0.1): read tolerantly here (an unreadable file is left
    to load_or_init's own refusal); the refusal never suggests a restart. An end that is
    only pending is not refused: it is re-finished (finding R1).
    """
    p = Path(path)
    if not p.is_file():
        return
    try:
        ck = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return
    if isinstance(ck, dict):
        status = ended_status(ck)
        if status is not None:
            raise SystemExit(_ended_message(p, ck, status))


def _set_aside(p: Path) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    aside = p.with_name(f"{p.name}.podchange-{stamp}")
    k = 1
    while aside.exists():
        aside = p.with_name(f"{p.name}.podchange-{stamp}-{k}")
        k += 1
    os.rename(p, aside)                            # renamed, never deleted
    _fsync_dir(p.parent)
    return aside


def load_or_init(path: str | os.PathLike, identity: Mapping, resume: bool) -> dict:
    """The checkpoint to continue, or a new one (m:267's refusals)."""
    ident = _validated(identity)
    p = Path(path)
    if not p.exists():
        return _fresh(ident)
    # An ENDED checkpoint (stopped, finished gate stage, terminal campaign) is refused
    # before anything else -- with or without --resume, on this pod or another: only an
    # unfinished, unstopped gate stage is ever set aside and restarted (m:267, m:271).
    refuse_ended(p)
    # PIN (Code, declared at LOCK v0.1; findings R1, R2): a checkpoint carrying an end
    # pending is returned for its re-finish on ANY pod and with or without --resume --
    # never set aside, never refused as existing. Its design must be the recorded one;
    # the backend identifier and the pod id may differ (a re-finish generates nothing:
    # its outputs are re-derived from the checkpoint under the RECORDED identity).
    if pending_at(p):
        ck = _read(p)
        if pending_end(ck) is not None:
            design = {k: v for k, v in _identity_diff(ck["identity"], ident).items()
                      if k not in ("backend_identifier", "pod_id")}
            if design:
                raise SystemExit(f"CHECKPOINT MISMATCH: {p} carries an end pending and differs on "
                                 f"{sorted(design)} (recorded, this run: {design}); a pending end "
                                 f"re-finishes only under its own design -- refusing.")
            return ck
    if not resume:
        raise SystemExit(f"CHECKPOINT EXISTS at {p}; pass --resume to continue it or move it "
                         f"aside. A run never silently overwrites one (trap 22).")
    ck = _read(p)
    status = ended_status(ck)
    if status is not None:
        raise SystemExit(_ended_message(p, ck, status))
    diff = _identity_diff(ck["identity"], ident)
    if ident["stage"] in GATE_STAGES:
        seen, now = ck["state"]["pod_id_seen"], _env_pod()
        if seen != now:
            # A new box: the backend identifier may move with it; nothing else may.
            design = {k: v for k, v in diff.items() if k != "backend_identifier"}
            if design:
                raise SystemExit(f"CHECKPOINT MISMATCH: {p} differs on {sorted(design)} "
                                 f"(recorded, this run: {design}) as well as the pod -- a "
                                 f"design change, not a pod change; refusing.")
            aside = _set_aside(p)
            new = _fresh(ident)
            new["state"]["set_aside"] = list(ck["state"].get("set_aside", [])) + [aside.name]
            write_checkpoint(p, new)
            print(f"POD CHANGE: {p.name} was written on pod {seen!r}, this is pod {now!r}; set "
                  f"aside as {aside.name}; the stage restarts from its first session under "
                  f"its deterministic keys (m:267).")
            return new
    if diff:
        pod_note = ""
        if "pod_id" in diff:
            pod_note = (" An OLMo campaign never resumes on another pod: it restarts under "
                        "its lock on the new box at a NEW checkpoint path (never spliced).")
        raise SystemExit(f"CHECKPOINT MISMATCH: {p} differs on {sorted(diff)} (recorded, "
                         f"this run: {diff}). Resuming across a different design would "
                         f"splice two designs -- refusing.{pod_note}")
    return ck


def _finish_only(path: str | os.PathLike, ckpt: Mapping) -> bool:
    """Is this write part of re-finishing an end pending -- the checkpoint on disk carries
    it, and the write records no session and no look beyond it?

    PIN (Code, declared at LOCK v0.1; finding R1): an OLMo campaign's checkpoint is
    written on its own pod only, EXCEPT to re-finish an end pending (a provenance entry,
    the end's persisted form): a re-finish generates nothing, so no session from another
    box can enter -- the "never spliced" rule holds by construction.
    """
    try:
        disk = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError):
        return False
    return (isinstance(disk, dict) and pending_end(disk) is not None
            and _canon(disk.get("sessions")) == _canon(ckpt.get("sessions"))
            and _canon(disk.get("looks")) == _canon(ckpt.get("looks")))


def _refuse_pod(path: str | os.PathLike, ckpt: Mapping) -> None:
    now = _env_pod()
    pid = ckpt.get("identity", {}).get("pod_id")
    if pid is not None and pid != now and not _finish_only(path, ckpt):
        raise SystemExit(f"POD MISMATCH: this OLMo campaign checkpoint belongs to pod {pid!r}; "
                         f"this is pod {now!r} -- refusing to write (m:267)")


def assert_writable(path: str | os.PathLike, ckpt: dict) -> None:
    """Every check ``write_checkpoint`` runs (pod, invariants, JSON-native types), with
    nothing written -- so a driver can prove a state persistable before it writes."""
    _refuse_pod(path, ckpt)
    _check_state(ckpt, str(path))
    _assert_native(ckpt)


def write_checkpoint(path: str | os.PathLike, ckpt: dict) -> None:
    """Atomic write after the invariants are re-checked; stamps ``pod_id_seen``."""
    now = _env_pod()
    _refuse_pod(path, ckpt)
    _check_state(ckpt, str(path))
    ckpt["state"]["pod_id_seen"] = now
    ckpt["state"]["n_writes"] += 1
    atomic_write_json(path, ckpt)


def record_session(ckpt: dict, rec: dict, *, look: Mapping | None = None) -> None:
    """Append one FINISHED session (in memory; ``write_checkpoint`` persists it).

    A campaign's look falls due when the launch count reaches a multiple of 40; it must
    be passed here, with the session that made it due, so both land in one write.
    """
    ident = ckpt["identity"]
    stage = ident["stage"]
    if rec.get("schema") != SESSION_SCHEMA or rec.get("unit") != ident["unit"] \
            or rec.get("stage") != stage:
        raise ValueError("record_session: not an m-session-v1 record of this unit and stage")
    # PIN (Code, declared at LOCK v0.1): the G-VER write gate is structural -- only a
    # record verify.verify_and_mark marked verified (exactly True) is ever recorded
    # (m:284 "before any artifact is written"); a failing one is quarantined by the
    # stage driver in its stop block, never here.
    if rec.get("verified") is not True:
        raise ValueError("record_session: the record is not verified (verified must be exactly "
                         "True; G-VER runs before any artifact is written, m:284)")
    if ended_status(ckpt) is not None:
        raise ValueError(f"record_session: the stage has ended ({ended_status(ckpt)}); no session "
                         f"is recorded after its end")
    if pending_end(ckpt) is not None:
        raise ValueError("record_session: an end is pending (re-finish-only); no session is "
                         "recorded past it")
    rid = _rec_id(rec, stage)
    if rid[0] not in ident["template_set"] or not 0 <= rid[1] < ident["n"][rid[0]]:
        raise ValueError("record_session: template or s outside the identity (n is fixed)")
    if rid in {_rec_id(r, stage) for r in ckpt["sessions"]}:
        raise ValueError("record_session: already on disk -- skip-only, a finished session "
                         "is never re-run")
    ms = _ms(rec.get("seconds"))
    _assert_native(rec)
    launches = len(ckpt["sessions"]) + 1
    due = stage == "campaign" and launches % LOOK_EVERY == 0
    if due and look is None:
        raise ValueError(f"record_session: the look at launch {launches} is due; record it "
                         f"in the same write")
    if look is not None and not due:
        raise ValueError(f"record_session: no look is due at launch {launches}")
    if look is not None:
        _assert_native(look)
    ckpt["sessions"].append(rec)
    ckpt["state"]["hour_cap_ms_used"] += ms
    if due:
        ckpt["looks"].append({"look_index": len(ckpt["looks"]), "at_launches": launches,
                              "result": dict(look)})
        ckpt["state"]["look_index"] += 1


def done_ids(ckpt: Mapping, *, by_path: bool = False) -> set[tuple]:
    """(template, s) of every FINISHED record on disk, excluded sessions included.

    PIN (Code, declared at LOCK v0.1): "finished" = present in the checkpoint (a
    record is appended only after its session ends and verifies); excluded and
    hair-trigger sessions count. At G-ID the unit is the pair: (template, s) is done
    only when both its uncached and cached records are on disk; ``by_path=True``
    returns the (template, s, path) halves instead.
    """
    stage = ckpt["identity"]["stage"]
    ids = [_rec_id(r, stage) for r in ckpt["sessions"]]
    if stage != "id":
        return set(ids)
    if by_path:
        return set(ids)
    halves = set(ids)
    return {(t, s) for t, s, _ in ids if (t, s, "cached") in halves and (t, s, "uncached") in halves}


def _q(x: Any) -> Fraction:
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    if type(x) is float:
        return Fraction(repr(x))                   # the decimal the lock wrote, not the binary
    if type(x) is str:
        return Fraction(x)
    raise TypeError(f"hour cap {x!r} is not an int/float/str/Fraction")


def hour_cap_exceeded(ckpt: Mapping, cap_hours: Any) -> bool:
    """Has the unit's generation wall-clock reached its cap? (m:251; terminal)

    PIN (Code, declared at LOCK v0.1): reached means used >= cap (no further launch);
    the cap passed must be the identity's (no override); time inside a session that was
    interrupted before its record was written is not counted.
    """
    if _canon(cap_hours) != _canon(ckpt["identity"]["hour_cap"]):
        raise ValueError(f"hour cap {cap_hours!r} is not the identity's "
                         f"{ckpt['identity']['hour_cap']!r} -- the cap is the lock's value")
    if cap_hours is None:
        return False
    return Fraction(ckpt["state"]["hour_cap_ms_used"]) >= _q(cap_hours) * 3_600_000


def refuse_canonical_out(path: str | os.PathLike | None) -> Path:
    """A selftest or stub run must not land where a measurement lands (ledger 27).

    Returns the RESOLVED path, which is the one the caller must write to -- the
    precedent checked one path and wrote another (maps/runner.md §4).
    """
    if path is None or str(path).strip() == "":
        raise SystemExit("SELFTEST REFUSED: no output path given (an empty path resolves "
                         "to the working directory) -- point it at a scratch path.")
    p = Path(path).expanduser().resolve()
    for root in CANONICAL_ROOTS:
        r = root.resolve()
        if p == r or r in p.parents:
            raise SystemExit(f"SELFTEST REFUSED: {path} resolves to {p}, under the canonical "
                             f"location {r}. A synthetic run must not be storable where a "
                             f"measurement is stored (ledger 27).")
    return p


# --- self-test -------------------------------------------------------------------
def _selftest(chk) -> None:
    import contextlib
    import io
    import tempfile

    import numpy as np

    @contextlib.contextmanager
    def env_pod(value: str | None):
        had, prev = POD_ENV in os.environ, os.environ.get(POD_ENV)
        if value is None:
            os.environ.pop(POD_ENV, None)
        else:
            os.environ[POD_ENV] = value
        try:
            yield
        finally:
            if had:
                os.environ[POD_ENV] = prev
            else:
                os.environ.pop(POD_ENV, None)

    def refuses(fn, exc=SystemExit, needle: str = "") -> bool:
        try:
            fn()
            return False
        except exc as e:
            return needle in str(e)

    H64, H16 = "a" * 64, "b" * 16

    def qf0(stage: str = "qual", **over) -> dict:
        kw = dict(unit="Q-F0", stage=stage, template_set=["A0s", "A0"], lock_sha256="pre-lock",
                  schedule_sha256=H64, path="uncached", hour_cap=None, n={"A0": 8, "A0s": 16},
                  audit_v2_sha16="7aa235d25eeb66dc", ban_sha="9a2f0744f81ac930" + "0" * 48,
                  backend_identifier=H16, proposal_sha256="c" * 64)
        kw.update(over)
        return Identity(**kw)

    def olmo_campaign(**over) -> dict:
        kw = dict(unit="OLMo-dpo", stage="campaign", template_set=["A0-OLMo-dpo", "A0s-OLMo-dpo"],
                  lock_sha256="d" * 64, schedule_sha256=H64, path="uncached", hour_cap=6.5,
                  n={"A0-OLMo-dpo": 96, "A0s-OLMo-dpo": 96}, audit_v2_sha16=H16,
                  ban_sha="2dd86a453a2275ef", backend_identifier=H16, proposal_sha256="c" * 64)
        kw.update(over)
        return Identity(**kw)

    def rec(ident: dict, template: str, s: int, seconds: float = 1.0, **extra) -> dict:
        return {"schema": SESSION_SCHEMA, "unit": ident["unit"], "stage": ident["stage"],
                "template": template, "s": s, "seconds": seconds, "excluded": False,
                "verified": True, **extra}

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        # atomic_write_json
        f = td / "a.json"
        fsyncs: list[bool] = []
        real = os.fsync

        def counting(fd: int) -> None:
            import stat
            fsyncs.append(stat.S_ISDIR(os.fstat(fd).st_mode))
            real(fd)

        os.fsync = counting
        try:
            atomic_write_json(f, {"b": 3, "a": ["é", (1, 2)], "c": 0.25})
        finally:
            os.fsync = real
        txt = f.read_text(encoding="utf-8")
        back = json.loads(txt)
        chk("resume: atomic_write_json round-trips sort-keyed, ensure_ascii off, ints stay ints",
            back == {"a": ["é", [1, 2]], "b": 3, "c": 0.25} and txt.index('"a"') < txt.index('"b"')
            and "é" in txt and type(back["b"]) is int and not (td / "a.json.tmp").exists(), txt.strip())
        chk("resume: atomic_write_json fsyncs the file and then its directory",
            fsyncs == [False, True], fsyncs)
        before = f.read_bytes()
        bad = {"numpy int64": {"n": np.int64(3)}, "numpy float64": {"x": np.float64(0.5)},
               "numpy bool": {"b": np.bool_(True)}, "a set": {"s": {1}}, "an int dict key": {1: "x"},
               "a Path": {"p": td}}
        accepted = [nm for nm, obj in bad.items() if not refuses(lambda o=obj: atomic_write_json(f, o),
                                                                  exc=TypeError)]
        chk(f"resume: atomic_write_json refuses non-native objects with TypeError ({len(bad)})",
            not accepted, accepted)
        chk("resume: atomic_write_json refuses NaN (ValueError)",
            refuses(lambda: atomic_write_json(f, {"x": float("nan")}), exc=ValueError))
        chk("resume: a refused write leaves the old file byte-identical and no temp file",
            f.read_bytes() == before and not (td / "a.json.tmp").exists())
        try:
            json.dumps({"n": np.int64(3)}, default=_refuse)
            dflt = False
        except TypeError:
            dflt = True
        chk("resume: the encoder's default= raises TypeError (no default=float conversion)", dflt)

        # backend_identifier and pod_id
        prov = {"adapter": "olmo_hf", "path": "/workspace/models/dpo", "dtype": "bfloat16",
                "gpu": "NVIDIA H100 80GB HBM3", "seed": 0, "n_encodes_clipped": 0,
                "library_versions": {"torch": "2.4.1", "numpy": "2.1.2"}}
        b0 = backend_identifier(prov)
        same = backend_identifier({**prov, "path": "/workspace/models/sft", "seed": 7,
                                   "n_encodes_clipped": 12})
        chk("resume: backend_identifier is sha16 and drops n_encodes_clipped, path, seed",
            bool(_HEX16.match(b0)) and same == b0, b0)
        chk("resume: backend_identifier moves with the GPU or a library version",
            backend_identifier({**prov, "gpu": "NVIDIA A100-SXM4-80GB"}) != b0
            and backend_identifier({**prov, "library_versions": {"torch": "2.5.0", "numpy": "2.1.2"}}) != b0)
        with env_pod(None):
            p_none = pod_id()
        with env_pod("  "):
            p_blank = pod_id()
        with env_pod("uimuzt7d890y5b"):
            p_set = pod_id()
        chk("resume: pod_id reads RUNPOD_POD_ID (unset/blank -> None)",
            p_none is None and p_blank is None and p_set == "uimuzt7d890y5b", (p_none, p_blank, p_set))

        # Identity
        i0 = qf0()
        chk("resume: Identity builds exact keys, §2.4 template order, m:159 key templates",
            tuple(sorted(i0)) == tuple(sorted(IDENTITY_KEYS)) and i0["template_set"] == ["A0", "A0s"]
            and i0["key_templates"]["A0"] == {"arm": "m-f0m|A0|{s}", "items": "m-items-qual|{s}",
                                              "sched": "m-sched|Q-F0|qual|A0|0"}
            and i0["pod_id"] is None, i0["key_templates"]["A0"])
        with env_pod("podA"):
            io_ = olmo_campaign()
        chk("resume: an OLMo campaign identity carries the pod id; campaign keys",
            io_["pod_id"] == "podA" and io_["key_templates"]["A0s-OLMo-dpo"]["arm"]
            == "m-olmo|dpo|A0s-OLMo-dpo|{s}" and io_["key_templates"]["A0s-OLMo-dpo"]["sched"]
            == "m-sched|OLMo-dpo|A0s-OLMo-dpo|{b}", io_["key_templates"]["A0s-OLMo-dpo"])
        bad_ids = {
            "OLMo campaign without a pod id": (lambda: olmo_campaign(), SystemExit),
            "a pod id on a Qwen gate stage": (lambda: qf0(pod_id="podA"), ValueError),
            "OLMo cached path": (lambda: olmo_campaign(path="cached", pod_id="p"), ValueError),
            "G-TIME-F0 cached": (lambda: qf0("time", path="cached"), ValueError),
            "G-ID on A0": (lambda: qf0("id", path="cached+uncached"), ValueError),
            "id stage on OLMo": (lambda: olmo_campaign(stage="id", pod_id=None), ValueError),
            "base checkpoint": (lambda: olmo_campaign(unit="OLMo-base", pod_id="p"), ValueError),
            "Q-F3": (lambda: qf0(unit="Q-F3"), NotImplementedError),
            "n missing a template": (lambda: qf0(n={"A0": 8}), ValueError),
            "n as a float": (lambda: qf0(n={"A0": 8.0, "A0s": 16}), ValueError),
            "campaign without an hour cap": (lambda: qf0("campaign", hour_cap=None), ValueError),
            "stop_cap 40": (lambda: qf0(stop_cap=40), ValueError),
            "a short lock hash": (lambda: qf0(lock_sha256="abc"), ValueError),
            "key_templates edited": (lambda: qf0(key_templates={"A0": {}, "A0s": {}}), ValueError),
            "a short package sha": (lambda: qf0(package_sha256="ab" * 8), ValueError),
            "an upper-case renders sha": (lambda: qf0(renders_sha16="A" * 16), ValueError),
            "a pool sha of 64 hex": (lambda: qf0(pool_sha16="a" * 64), ValueError),
        }
        accepted = []
        for nm, (fn, exc) in bad_ids.items():
            with env_pod(None):
                if not refuses(fn, exc=exc):
                    accepted.append(nm)
        chk(f"resume: Identity refuses each malformed identity ({len(bad_ids)})", not accepted, accepted)
        chk("resume: load_or_init refuses a hand-built identity with an extra or missing key",
            refuses(lambda: load_or_init(td / "x.json", {**i0, "seed": 1}, False), exc=ValueError)
            and refuses(lambda: load_or_init(td / "x.json", {k: v for k, v in i0.items()
                                                              if k != "n"}, False), exc=ValueError))

        # load_or_init: new, EXISTS, resume, MISMATCH
        cp = td / "gate.json"
        with env_pod(None):
            ck = load_or_init(cp, i0, resume=False)
            ck_r = load_or_init(cp, i0, resume=True)
            chk("resume: no file -> a new checkpoint (with or without --resume)",
                ck["sessions"] == [] and ck_r["sessions"] == [] and not cp.exists())
            record_session(ck, rec(i0, "A0s", 0, 2.5))
            record_session(ck, rec(i0, "A0", 0, 3.0, excluded=True))
            write_checkpoint(cp, ck)
            chk("resume: an existing checkpoint without --resume -> CHECKPOINT EXISTS",
                refuses(lambda: load_or_init(cp, i0, resume=False), needle="CHECKPOINT EXISTS"))
            ck2 = load_or_init(cp, i0, resume=True)
            chk("resume: --resume with the identical identity continues the sessions on disk",
                len(ck2["sessions"]) == 2 and ck2["state"]["hour_cap_ms_used"] == 5500)
            mism = {"n changed": qf0(n={"A0": 8, "A0s": 24}),
                    "lock hash changed": qf0(lock_sha256="e" * 64),
                    "path changed": qf0(path="cached"),
                    "backend changed (same pod)": qf0(backend_identifier="f" * 16),
                    "package code changed": qf0(package_sha256="e" * 64),
                    "renders changed": qf0(renders_sha16="e" * 16),
                    "pool changed": qf0(pool_sha16="e" * 16)}
            missed = []
            for nm, ident in mism.items():
                if not refuses(lambda i=ident: load_or_init(cp, i, resume=True),
                               needle="CHECKPOINT MISMATCH"):
                    missed.append(nm)
            chk("resume: --resume refuses any change of n, lock, path, backend (same pod), package "
                "code, renders or pool", not missed, missed)
            # two-way: a recorded identity carrying a key this build lacks
            raw = json.loads(cp.read_text())
            raw["identity"]["seed"] = 20260906
            atomic_write_json(td / "extra.json", raw)
            chk("resume: two-way equality -- an extra recorded identity key refuses",
                refuses(lambda: load_or_init(td / "extra.json", i0, resume=True),
                        needle="CHECKPOINT MISMATCH"))
            raw = json.loads(cp.read_text())
            del raw["identity"]["ban_sha"]
            atomic_write_json(td / "less.json", raw)
            chk("resume: two-way equality -- a missing recorded identity key refuses",
                refuses(lambda: load_or_init(td / "less.json", i0, resume=True),
                        needle="CHECKPOINT MISMATCH"))
            hc8, hc8f = qf0(hour_cap=8), qf0(hour_cap=8.0)
            c8 = td / "cap.json"
            write_checkpoint(c8, load_or_init(c8, hc8, resume=False))
            chk("resume: exact equality -- hour cap 8 recorded, 8.0 offered, refuses",
                refuses(lambda: load_or_init(c8, hc8f, resume=True), needle="CHECKPOINT MISMATCH")
                and load_or_init(c8, hc8, resume=True)["identity"]["hour_cap"] == 8)
            junk = td / "junk.json"
            junk.write_text("{truncated")
            chk("resume: an unreadable checkpoint refuses and is left untouched",
                refuses(lambda: load_or_init(junk, i0, resume=True), needle="UNREADABLE")
                and junk.read_text() == "{truncated")

            # skip-only
            done = done_ids(ck2)
            chk("resume: done_ids lists finished sessions, excluded ones included",
                done == {("A0s", 0), ("A0", 0)}, sorted(done))
            chk("resume: record_session refuses a session already on disk (never re-run)",
                refuses(lambda: record_session(ck2, rec(i0, "A0", 0)), exc=ValueError,
                        needle="skip-only"))
            chk("resume: record_session refuses s >= n and a foreign template",
                refuses(lambda: record_session(ck2, rec(i0, "A0", 8)), exc=ValueError)
                and refuses(lambda: record_session(ck2, rec(i0, "A0-OLMo-dpo", 1)), exc=ValueError))
            chk("resume: record_session refuses a record with a numpy int (no silent cast)",
                refuses(lambda: record_session(ck2, rec(i0, "A0", 1, extra=np.int64(1))),
                        exc=TypeError) and len(ck2["sessions"]) == 2)
            gid = qf0("id", template_set=["A0s"], path="cached+uncached", n={"A0s": 16})
            gk = _fresh(gid)
            record_session(gk, rec(gid, "A0s", 0, path="uncached"))
            half = done_ids(gk)
            record_session(gk, rec(gid, "A0s", 0, path="cached"))
            chk("resume: G-ID's unit is the pair (a half pair is not done; by_path shows halves)",
                half == set() and done_ids(gk) == {("A0s", 0)}
                and done_ids(gk, by_path=True) == {("A0s", 0, "uncached"), ("A0s", 0, "cached")})

        # gate-stage pod change: set aside (never delete), restart from the first session
        gp = td / "olmo_qual.json"
        oq = dict(unit="OLMo-sft", stage="qual", template_set=["A0-OLMo-sft", "A0s-OLMo-sft"],
                  lock_sha256="pre-lock", schedule_sha256=H64, path="uncached", hour_cap=None,
                  n={"A0-OLMo-sft": 8, "A0s-OLMo-sft": 16}, audit_v2_sha16=H16,
                  ban_sha="2dd86a453a2275ef", backend_identifier=H16, proposal_sha256="c" * 64)
        iq = Identity(**oq)
        with env_pod("podA"):
            g = load_or_init(gp, iq, resume=False)
            record_session(g, rec(iq, "A0s-OLMo-sft", 0))
            record_session(g, rec(iq, "A0-OLMo-sft", 0))
            write_checkpoint(gp, g)
            old_bytes = gp.read_bytes()
            same_pod = load_or_init(gp, iq, resume=True)
        chk("resume: gate stage, same pod -> resumes, nothing set aside",
            len(same_pod["sessions"]) == 2 and not list(td.glob("olmo_qual.json.podchange-*")))
        with env_pod("podB"):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                fresh = load_or_init(gp, Identity(**{**oq, "backend_identifier": "9" * 16}), resume=True)
            asides = list(td.glob("olmo_qual.json.podchange-*"))
            reloaded = json.loads(gp.read_text())
        line = out.getvalue()
        chk("resume: gate stage, new pod -> old checkpoint renamed aside byte-identical (never "
            "deleted), restart from the first session, one line printed",
            fresh["sessions"] == [] and len(asides) == 1 and asides[0].read_bytes() == old_bytes
            and reloaded["sessions"] == [] and reloaded["state"]["pod_id_seen"] == "podB"
            and reloaded["state"]["set_aside"] == [asides[0].name]
            and line.count("\n") == 1 and line.startswith("POD CHANGE"), line.strip())
        with env_pod("podC"):
            refused = refuses(lambda: load_or_init(gp, Identity(**{**oq, "n": {"A0-OLMo-sft": 8,
                                                                               "A0s-OLMo-sft": 24}}),
                                                   resume=True), needle="design change")
            n_asides = len(list(td.glob("olmo_qual.json.podchange-*")))
        chk("resume: gate stage, new pod AND a design change -> refused, nothing renamed",
            refused and n_asides == 1 and gp.exists())

        # ENDED gate stages: never resumed, re-run or set aside, on any pod
        def ended_gate(name: str, *, status: str, stop: bool = False) -> Path:
            pth = td / f"{name}.json"
            with env_pod("podA"):
                e = load_or_init(pth, iq, resume=False)
                record_session(e, rec(iq, "A0s-OLMo-sft", 0))
                if stop:
                    e["stop"] = {"kind": "hair_trigger", "bar": "scaffold_absorption"}
                e["stage_end"] = {"status": status, "fired": ["scaffold_absorption"] if stop else [],
                                  "adjudication": None}
                write_checkpoint(pth, e)
            return pth
        outcomes = {}
        for nm, kw, needle in (("ended_pass", {"status": "PASS"}, "(PASS)"),
                               ("ended_pause", {"status": "PAUSE"}, "(PAUSE)"),
                               ("ended_stop", {"status": "STOP", "stop": True}, "(STOP")):
            pth = ended_gate(nm, **kw)
            before_b = pth.read_bytes()
            ok_nm = True
            for pod, rs in (("podA", True), ("podA", False), ("podB", True), (None, True)):
                with env_pod(pod):
                    ok_nm &= refuses(lambda: load_or_init(pth, iq, resume=rs), needle="STAGE ENDED") \
                        and refuses(lambda: load_or_init(pth, iq, resume=rs), needle=needle)
            ok_nm &= pth.read_bytes() == before_b and not list(td.glob(f"{nm}.json.podchange-*"))
            outcomes[nm] = ok_nm
        chk("resume: a finished (PASS / PAUSE) or stopped gate stage is refused 'STAGE ENDED' naming its "
            "status, on its own pod or another, with or without --resume; never set aside",
            all(outcomes.values()), outcomes)
        with env_pod("podA"):
            un = load_or_init(td / "unfinished.json", iq, resume=False)
            record_session(un, rec(iq, "A0s-OLMo-sft", 0))
            write_checkpoint(td / "unfinished.json", un)
        with env_pod("podB"):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                restarted = load_or_init(td / "unfinished.json", iq, resume=True)
        chk("resume: an unfinished, unstopped gate stage on a new pod is the only one set aside and "
            "restarted", restarted["sessions"] == [] and "POD CHANGE" in out.getvalue()
            and len(list(td.glob("unfinished.json.podchange-*"))) == 1)
        with env_pod("podA"):
            ce = load_or_init(td / "camp_end.json", olmo_campaign(), resume=False)
            record_session(ce, rec(ce["identity"], "A0-OLMo-dpo", 0))
            ce["campaign"] = {"terminal": {"status": "COMPLETE", "at_launches": 1}}
            write_checkpoint(td / "camp_end.json", ce)
        with env_pod("podB"):
            msg = ""
            try:
                refuse_ended(td / "camp_end.json")
            except SystemExit as e:
                msg = str(e)
        chk("resume: refuse_ended on a terminal campaign names its status and never advises a restart "
            "on a new path; silent on an unfinished one",
            "CAMPAIGN ENDED" in msg and "(COMPLETE)" in msg and "NEW checkpoint" not in msg
            and refuse_ended(td / "unfinished.json") is None and refuse_ended(td / "absent.json") is None,
            msg[:80])

        # the G-VER write gate is structural; nothing is recorded after a stage's end
        with env_pod(None):
            vk = _fresh(i0)
            unverified = [nm for nm, r in (("verified False", rec(i0, "A0", 0, verified=False)),
                                           ("verified 1", rec(i0, "A0", 0, verified=1)),
                                           ("verified absent", {k: v for k, v in rec(i0, "A0", 0).items()
                                                                if k != "verified"}))
                          if not refuses(lambda r=r: record_session(vk, r), exc=ValueError,
                                         needle="not verified")]
            record_session(vk, rec(i0, "A0", 0))
            ok_ver = len(vk["sessions"]) == 1
            vk["stage_end"] = {"status": "PASS", "fired": [], "adjudication": None}
            after_end = refuses(lambda: record_session(vk, rec(i0, "A0", 1)), exc=ValueError,
                                needle="has ended")
            raw_v = _fresh(i0)
            raw_v["sessions"].append(rec(i0, "A0", 0, verified=False))
            raw_v["state"]["hour_cap_ms_used"] = 1000
            atomic_write_json(td / "unverified.json", raw_v)
            disk_unverified = refuses(lambda: load_or_init(td / "unverified.json", i0, resume=True),
                                      needle="not a verified record")
            raw_m = _fresh(i0)
            raw_m["stage_end"] = {"status": "OPEN", "fired": [], "adjudication": None}
            atomic_write_json(td / "bad_end.json", raw_m)
            bad_end = refuses(lambda: read_checkpoint(td / "bad_end.json"), needle="stage_end malformed")
        chk("resume: record_session refuses a record whose verified is not exactly True (False, 1, "
            "absent) and records a verified one",
            not unverified and ok_ver, unverified)
        chk("resume: nothing is recorded after a stage's end; an unverified session or a malformed "
            "stage_end on disk refuses the checkpoint", after_end and disk_unverified and bad_end)

        # package / pool / renders in the identity
        pk = package_sha256()
        pkg = td / "pkgcopy" / "m"
        pkg.mkdir(parents=True)
        for f in sorted(PACKAGE_DIR.glob("*.py"))[:3]:
            (pkg / f.name).write_bytes(f.read_bytes())
        h1, h2 = package_sha256_of(pkg), package_sha256_of(pkg)
        first = sorted(pkg.glob("*.py"))[0]
        body = first.read_bytes()
        first.write_bytes(body[:-1] + (b"#" if body[-1:] != b"#" else b"\n"))   # same length
        h3 = package_sha256_of(pkg)
        (pkg / "__pycache__").mkdir()
        (pkg / "__pycache__" / "x.py").write_text("x = 1\n")
        h4 = package_sha256_of(pkg)
        chk("resume: package_sha256 is a sha256 over the m sources, stable, moved by a one-byte edit, "
            "blind to __pycache__; an identity carries it with the pool and renders of record",
            bool(_HEX64.match(pk)) and package_sha256() == pk and h1 == h2 and h3 != h1 and h4 == h3
            and i0["package_sha256"] == pk and (i0["pool_sha16"], i0["renders_sha16"]) == _of_record_shas(),
            (pk[:16], i0["renders_sha16"]))

        # OLMo campaign: pod id in identity, hard refusal on change
        op = td / "olmo_campaign.json"
        with env_pod("podA"):
            ia = olmo_campaign()
            oc = load_or_init(op, ia, resume=False)
            record_session(oc, rec(ia, "A0-OLMo-dpo", 0))
            write_checkpoint(op, oc)
        with env_pod("podB"):
            ib = olmo_campaign()
            hard = refuses(lambda: load_or_init(op, ib, resume=True), needle="NEW checkpoint path")
            wrote = refuses(lambda: write_checkpoint(op, oc), needle="POD MISMATCH")
        chk("resume: OLMo campaign on another pod -> hard refusal, never set aside or spliced",
            hard and wrote and op.exists() and not list(td.glob("olmo_campaign.json.podchange-*")))
        with env_pod("podA"):
            cont = load_or_init(op, ia, resume=True)
        chk("resume: OLMo campaign on its own pod -> resumes", len(cont["sessions"]) == 1)

        # hour cap, persisted across resumes
        with env_pod("podA"):
            hp = td / "hours.json"
            ih = olmo_campaign(hour_cap=0.001)          # 3.6 s
            hk = load_or_init(hp, ih, resume=False)
            record_session(hk, rec(ih, "A0-OLMo-dpo", 0, 2.0))
            write_checkpoint(hp, hk)
            under = hour_cap_exceeded(load_or_init(hp, ih, resume=True), 0.001)
            hk = load_or_init(hp, ih, resume=True)
            record_session(hk, rec(ih, "A0s-OLMo-dpo", 0, 1.6))
            write_checkpoint(hp, hk)
            at = hour_cap_exceeded(load_or_init(hp, ih, resume=True), 0.001)
            over_ride = refuses(lambda: hour_cap_exceeded(hk, 1.0), exc=ValueError)
            tampered = json.loads(hp.read_text())
            tampered["state"]["hour_cap_ms_used"] = 0
            atomic_write_json(td / "hours_t.json", tampered)
            reset = refuses(lambda: load_or_init(td / "hours_t.json", ih, resume=True),
                            needle="hour_cap_ms_used")
        chk("resume: hour cap accumulates across resumes; silent below, fires at the cap (>=)",
            under is False and at is True and hk["state"]["hour_cap_ms_used"] == 3600, (under, at))
        chk("resume: hour cap refuses an override and a reset counter on disk", over_ride and reset)
        with env_pod(None):
            chk("resume: a stage with no cap is never capped",
                hour_cap_exceeded(ck2, None) is False)

        # look index
        with env_pod("podA"):
            lk = _fresh(olmo_campaign())
            for s in range(39):
                record_session(lk, rec(lk["identity"], "A0-OLMo-dpo" if s % 2 == 0 else
                                       "A0s-OLMo-dpo", s // 2))
            no_look = refuses(lambda: record_session(lk, rec(lk["identity"], "A0s-OLMo-dpo", 19)),
                              exc=ValueError, needle="due")
            early = refuses(lambda: record_session(_fresh(olmo_campaign()),
                                                   rec(lk["identity"], "A0-OLMo-dpo", 0),
                                                   look={"fired": []}), exc=ValueError)
            record_session(lk, rec(lk["identity"], "A0s-OLMo-dpo", 19), look={"fired": []})
            lp = td / "looks.json"
            write_checkpoint(lp, lk)
            ok_load = load_or_init(lp, lk["identity"], resume=True)["state"]["look_index"] == 1
            t = json.loads(lp.read_text())
            t["state"]["look_index"] = 0
            atomic_write_json(td / "looks_t.json", t)
            tampered_look = refuses(lambda: load_or_init(td / "looks_t.json", lk["identity"],
                                                         resume=True), needle="look_index")
        chk("resume: look index == completed_launches // 40 (due look required in the same "
            "write; none early; tampered index refused)",
            no_look and early and ok_load and tampered_look and lk["looks"][0]["at_launches"] == 40)

        # refuse_canonical_out
        link = td / "repo_data"
        link.symlink_to(REPO / "data")
        canon = {
            "REPO/data/m/x": REPO / "data" / "m" / "selftest.json",
            "REPO/data/m itself": REPO / "data" / "m",
            "/workspace/models/x": "/workspace/models/selftest.json",
            "REPO/data/olmo/x": REPO / "data" / "olmo" / "b3.json",
            "a symlink into REPO/data/m": link / "m" / "x.json",
            "a .. walk into REPO/data/m": REPO / "data" / "format" / ".." / "m" / "x.json",
            "the empty path": "",
        }
        let_through = [nm for nm, pth in canon.items()
                       if not refuses(lambda q=pth: refuse_canonical_out(q), needle="SELFTEST REFUSED")]
        chk(f"resume: refuse_canonical_out refuses canonical locations, resolved ({len(canon)})",
            not let_through, let_through)
        okp = refuse_canonical_out(td / "scratch" / "ck.json")
        chk("resume: refuse_canonical_out accepts a scratch path and returns it resolved",
            okp == (td / "scratch" / "ck.json").resolve())
        chk("resume: the self-test wrote nothing under REPO/data/m",
            not (REPO / "data" / "m" / "selftest.json").exists()
            and not (REPO / "data" / "m" / "x.json").exists())

        # the refusal of a STOPped checkpoint names only the stop's BLINDED class
        withheld = "withheld to the unit's VERDICTS entry (selftest)"
        stops = {
            "contrast free-phase": {"kind": "hair_trigger", "bar": "scaffold_absorption", "phase": "free",
                                    "round": {"phase": "free", "n": 6, "index": 1},
                                    "blinded": {"bar": withheld, "template": "A0", "s": 0, "phase": "free"}},
            "sham forced": {"kind": "hair_trigger", "bar": "scaffold_absorption", "phase": "forced",
                            "blinded": {"bar": "scaffold_absorption", "template": "A0s", "s": 0,
                                        "phase": "forced"}},
            "no blinded block": {"kind": "hair_trigger", "bar": "scaffold_absorption"},
        }
        msgs = {nm: _ended_message(Path("c.json"), {"identity": {"stage": "time"}, "stop": st}, "STOP")
                for nm, st in stops.items()}
        cf = msgs["contrast free-phase"]
        chk("resume: a STOP refusal names a contrast free-phase trigger by phase alone (template, s; "
            "never its class, round, n or index), a sham trigger by its class, an unblinded stop by none",
            "free phase of a contrast session (A0 s=0)" in cf and "class is withheld" in cf
            and "scaffold" not in cf and "n=6" not in cf and "index" not in cf and "round 6" not in cf
            and "(STOP, scaffold_absorption)" in msgs["sham forced"]
            and "(STOP)" in msgs["no blinded block"] and "scaffold" not in msgs["no blinded block"],
            cf[:110])

        # provenance: verbatim, outside the identity, one entry per invocation
        with env_pod(None):
            pv = _fresh(i0)
            prov_a = {"adapter": "olmo_hf", "capability": (9, 0), "library_versions": {"torch": "2.4.1"},
                      "deterministic": True, "gpu": None}
            e1 = append_provenance(pv, prov_a, stamp="2026-10-06T00:00:00Z")
            note_launch(pv)
            record_session(pv, rec(i0, "A0", 0))
            note_launch(pv)                          # a launch that recorded nothing (a G-VER stop)
            pp = td / "prov.json"
            write_checkpoint(pp, pv)
            pv2 = load_or_init(pp, i0, resume=True)
            e2 = append_provenance(pv2, {**prov_a, "gpu": "H100"}, stamp="2026-10-06T01:00:00Z")
            write_checkpoint(pp, pv2)
            back_p = read_checkpoint(pp)
            rp = report_provenance(back_p)
            nat = refuses(lambda: append_provenance(_fresh(i0), {"x": np.int64(1)}), exc=TypeError)
            orphan = _fresh(i0)
            record_session(orphan, rec(i0, "A0", 0))
            no_list = refuses(lambda: append_provenance(orphan, prov_a), exc=ValueError,
                              needle="no provenance list")
            no_entry = refuses(lambda: note_launch(_fresh(i0)), exc=ValueError)
            under = json.loads(pp.read_text())
            under["provenance"][0]["launched"] = 0
            atomic_write_json(td / "prov_under.json", under)
            under_ref = refuses(lambda: read_checkpoint(td / "prov_under.json"), needle="launched")
            badk = json.loads(pp.read_text())
            badk["provenance"][0]["extra"] = 1
            atomic_write_json(td / "prov_badk.json", badk)
            badk_ref = refuses(lambda: read_checkpoint(td / "prov_badk.json"), needle="provenance")
        chk("resume: provenance is recorded verbatim (tuples as JSON lists) outside the identity, one "
            "entry per invocation with its stamp; a resume appends; the report copies the entries that "
            "launched a session",
            [e["stamp"] for e in back_p["provenance"]] == ["2026-10-06T00:00:00Z", "2026-10-06T01:00:00Z"]
            and back_p["provenance"][0]["record"]["capability"] == [9, 0]
            and back_p["provenance"][0]["launched"] == 2 and back_p["provenance"][1]["launched"] == 0
            and back_p["provenance"][1]["record"]["gpu"] == "H100" and e1["record"]["gpu"] is None
            and e2["launched"] == 0 and "provenance" not in back_p["identity"]
            and "provenance" not in IDENTITY_KEYS and [e["stamp"] for e in rp] == ["2026-10-06T00:00:00Z"],
            [(e["stamp"], e["launched"]) for e in back_p["provenance"]])
        chk("resume: provenance refuses a non-native value, a list started on a checkpoint that already "
            "has sessions, a launch with no entry, fewer launches than recorded sessions and a malformed "
            "entry on disk", nat and no_list and no_entry and under_ref and badk_ref,
            (nat, no_list, no_entry, under_ref, badk_ref))

        # json_text is the exact text atomic_write_json writes; assert_writable writes nothing
        jt = td / "jt.json"
        obj = {"b": [1, "é"], "a": None}
        atomic_write_json(jt, obj, indent=1)
        with env_pod(None):
            aw = _fresh(i0)
            aw_ok = assert_writable(td / "aw.json", aw) is None and not (td / "aw.json").exists()
            aw["state"]["hour_cap_ms_used"] = 7
            aw_bad = refuses(lambda: assert_writable(td / "aw.json", aw), needle="hour_cap_ms_used")
            aw2 = _fresh(i0)
            aw2["stop"] = {"record": {"x": np.float64(0.5)}}
            aw_nat = refuses(lambda: assert_writable(td / "aw.json", aw2), exc=TypeError)
        chk("resume: json_text equals atomic_write_json's bytes; assert_writable passes a writable "
            "checkpoint without writing it and refuses a broken invariant and a non-native value",
            jt.read_text(encoding="utf-8") == json_text(obj, indent=1) and aw_ok and aw_bad and aw_nat
            and not (td / "aw.json").exists())

        # an end PENDING (finding R1): re-finish-only on any pod, at any invocation
        def gate_pending(name: str, *, pod: str | None, stop: bool = False) -> Path:
            pth = td / f"{name}.json"
            with env_pod(pod):
                g_ = load_or_init(pth, iq, resume=False)
                record_session(g_, rec(iq, "A0s-OLMo-sft", 0))
                set_end_pending(g_, {"status": "STOP" if stop else "PASS",
                                     "fired": ["scaffold_absorption"] if stop else [],
                                     "stop": {"bar": "scaffold_absorption", "blinded": {}} if stop else None})
                write_checkpoint(pth, g_)
            return pth
        pg_ = gate_pending("pend_gate", pod="podA", stop=True)
        pend_bytes = pg_.read_bytes()
        on_disk = read_checkpoint(pg_)
        pend_ok = {}
        for pod, rs in (("podA", True), ("podA", False), ("podB", True), ("podB", False)):
            with env_pod(pod):
                got_ck = load_or_init(pg_, Identity(**{**oq, "backend_identifier": "9" * 16}), resume=rs)
                pend_ok[(pod, rs)] = (pending_end(got_ck) is not None and len(got_ck["sessions"]) == 1
                                      and not list(td.glob("pend_gate.json.podchange-*")))
        with env_pod("podB"):
            pend_design = refuses(lambda: load_or_init(pg_, Identity(**{**oq, "n": {"A0-OLMo-sft": 8,
                                                                                 "A0s-OLMo-sft": 24}}),
                                                       resume=True), needle="end pending")
        chk("resume: a checkpoint carrying an end pending is returned for its re-finish on its own pod or "
            "another, with or without --resume, the backend identifier free to differ -- never set aside, "
            "never refused as existing; a design change is still refused",
            all(pend_ok.values()) and pend_design and pg_.read_bytes() == pend_bytes
            and ended_status(on_disk) is None and refuse_ended(pg_) is None and pending_at(pg_), pend_ok)
        with env_pod("podA"):
            no_rec = refuses(lambda: record_session(dict(on_disk, sessions=list(on_disk["sessions"])),
                                                    rec(iq, "A0-OLMo-sft", 0)), exc=ValueError, needle="pending")
            bad_pend = {
                "a stop under PASS": {"status": "PASS", "fired": [], "stop": {"bar": "x"}},
                "a status no gate stage ends with": {"status": "COMPLETE", "fired": [], "stop": None},
                "fired not a list": {"status": "STOP", "fired": "x", "stop": None},
                "a campaign key on a gate stage": {"status": "PASS", "fired": [], "stop": None, "pause": None}}
            let = []
            for nm, pe in bad_pend.items():
                fresh_ = load_or_init(td / "pend_bad.json", iq, resume=False)
                if not refuses(lambda f=fresh_, pe=pe: set_end_pending(f, pe), exc=ValueError):
                    let.append(nm)
            twice = load_or_init(td / "pend_twice.json", iq, resume=False)
            set_end_pending(twice, {"status": "PASS", "fired": [], "stop": None})
            again = refuses(lambda: set_end_pending(twice, {"status": "PASS", "fired": [], "stop": None}),
                            exc=ValueError, needle="already")
            raw_b = json.loads(pg_.read_text())
            raw_b["stage_end"] = {"status": "PASS", "fired": [], "adjudication": None}
            atomic_write_json(td / "pend_beside.json", raw_b)
            beside = refuses(lambda: read_checkpoint(td / "pend_beside.json"), needle="beside a persisted end")
        chk("resume: nothing is recorded past an end pending; a malformed pending end (a stop under PASS, a "
            "campaign status, fired not a list, a campaign key) is refused, a second one too, and one beside a "
            "persisted end refuses the checkpoint", no_rec and not let and again and beside, let)
        with env_pod("podA"):
            fin_ = apply_end(json.loads(pg_.read_text()))
            extra_ = json.loads(json.dumps(fin_))
            extra_["sessions"].append(rec(iq, "A0-OLMo-sft", 0))
            extra_["state"]["hour_cap_ms_used"] += 1000
            not_final = refuses(lambda: persist_end(pg_, extra_), exc=ValueError, needle="not the persisted form")
            untouched = pg_.read_bytes() == pend_bytes
            persist_end(pg_, fin_)
            done_ = read_checkpoint(pg_)
            no_pend = refuses(lambda: persist_end(pg_, fin_), exc=ValueError, needle="no end pending")
        chk("resume: apply_end turns a gate stage's pending end into stage_end and its stop; persist_end writes "
            "only that persisted form (a checkpoint with another session refused, the file untouched) and "
            "refuses where nothing is pending",
            not_final and untouched and no_pend and "end_pending" not in done_
            and done_["stage_end"] == {"status": "STOP", "fired": ["scaffold_absorption"], "adjudication": None}
            and done_["stop"]["bar"] == "scaffold_absorption" and ended_status(done_) == "STOP")
        # an OLMo campaign's checkpoint on another pod: written only to re-finish a pending end
        ocp = td / "pend_olmo_campaign.json"
        with env_pod("podA"):
            iac = olmo_campaign()
            oc_ = load_or_init(ocp, iac, resume=False)
            oc_["campaign"] = {"floors": {}, "launch_counts_projection": {}, "pauses": [], "terminal": None,
                               "end_look": None, "pi_stop": None}
            record_session(oc_, rec(iac, "A0-OLMo-dpo", 0))
            write_checkpoint(ocp, oc_)
            plain_ = json.loads(ocp.read_text())
            set_end_pending(oc_, {"status": "COMPLETE", "fired": [], "stop": None, "pause": None, "end_look": None,
                                  "terminal": {"status": "COMPLETE", "at_launches": 1}})
        with env_pod("podB"):
            no_pend_pod = refuses(lambda: write_checkpoint(ocp, plain_), needle="POD MISMATCH")
        with env_pod("podA"):
            write_checkpoint(ocp, oc_)
        with env_pod("podB"):
            back_oc = load_or_init(ocp, olmo_campaign(), resume=True)
            grow = json.loads(json.dumps(back_oc))
            grow["sessions"].append(rec(iac, "A0s-OLMo-dpo", 0))
            grow["state"]["hour_cap_ms_used"] += 1000
            grows = refuses(lambda: write_checkpoint(ocp, grow), needle="POD MISMATCH")
            write_checkpoint(ocp, back_oc)
            persist_end(ocp, apply_end(json.loads(json.dumps(back_oc))))
            end_oc = read_checkpoint(ocp)
        chk("resume: an OLMo campaign's checkpoint is written on another pod only to re-finish a pending end "
            "-- with nothing pending refused, a write adding a session refused (POD MISMATCH), the re-finish "
            "admitted and its terminal state persisted under the original pod id",
            no_pend_pod and grows and end_oc["campaign"]["terminal"]["status"] == "COMPLETE"
            and end_oc["identity"]["pod_id"] == "podA" and end_oc["state"]["pod_id_seen"] == "podB"
            and "end_pending" not in end_oc)
