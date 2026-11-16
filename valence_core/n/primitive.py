"""PROPOSAL-n -- THE OLMo 5(f) PRIMITIVE (n v0.2 §2.2; CLAUDE.md rule 5(f); k:111-127 the rule-level spec).

A memory-present, state-absent-at-read choice read: a state injected on declared earlier spans of one forward, the
read position and every non-span position unsteered by construction. QUARANTINED on the 5(e)/k pattern:

  * IMPORT GUARD -- importable only from inside ``valence_core/n/`` or a ``scripts/n_*.py`` driver;
  * ``valence_core.e2b.statepresent`` (5(e)) and ``valence_core.echo.maskedprefix`` (k's Qwen primitive) are asserted
    ABSENT from ``sys.modules`` at import and before every read: no two quarantined primitives in one process;
  * SPANS, PROVENANCE -- the spans come from the session record (``Session.spans``), never from a caller's numbers;
    the mask is built here; the read position and every position outside the spans are asserted zero before any
    forward, and every placed ``PositionSpec`` is checked against the mask position by position;
  * THE SHADOW, MANDATORY (5(f)(i)) -- the mask-off read over identical token ids is the N1-V d = 0 read of the
    session (n §2.4: "the 160 at d = 0 are the shadows for every arm"; §2.2: "the d = 0 cache"). ``read_steered``
    refuses to run without that read's record, and asserts its ``ids_sha`` equal to the steered read's;
  * RETENTION (5(f)(iii)) -- recorded per read; fixed by the skeleton.

``valence_core.adapters.olmo_hf`` is imported unchanged: the HF backend reaches the adapter's own hook plumbing
(``OLMoHFAdapter._make_hooks``, the validated injection site: the residual as it exits the decoder layer, the delta
in fp32 and cast at the add) and its loaded model. Nothing of k's Qwen primitive is modified or imported.

THE TWO PATHS are ``schema``'s (BK's ``prereg.precondition_cache``: "the prefill-plus-cached-continuation margin
against a fresh full forward over the identical ids under the identical additive mask"). A backend implements three
calls -- ``prefill``, ``continue_label``, ``full`` -- and nothing else; ``HFBackend`` is the box's, and the self-test
runs the same primitive over a numpy causal double.
"""
from __future__ import annotations

import hashlib
import inspect
import math
import os
import sys
import types
from dataclasses import dataclass
from typing import Mapping, Protocol, Sequence

import numpy as np

_PKG_DIR = os.path.dirname(os.path.abspath(__file__))
_THIS_FILE = os.path.abspath(__file__)

FORBIDDEN_MODULES = ("valence_core.e2b.statepresent", "valence_core.echo.maskedprefix")


def _importer_is_sanctioned() -> bool:
    for frame in inspect.stack():
        path = os.path.abspath(frame.filename or "")
        if path == _THIS_FILE or "importlib" in path or path.startswith("<frozen"):
            continue
        if frame.filename.startswith("<") and "importlib" in (frame.function or ""):
            continue
        if path.startswith(_PKG_DIR + os.sep):
            return True
        base = os.path.basename(path)
        return base.startswith("n_") and base.endswith(".py") and os.path.basename(os.path.dirname(path)) == \
            "scripts"
    return False


if not _importer_is_sanctioned():
    raise ImportError(
        "valence_core.n.primitive is quarantined (CLAUDE.md rule 5(f); PROPOSAL-n v0.2 §2.2). It may be imported "
        "only from inside valence_core/n/ or a scripts/n_*.py driver. A vanilla choice read is readout.choice_read; "
        "escalate to the design instance rather than widening this guard.")


def assert_quarantine() -> None:
    hits = [m for m in FORBIDDEN_MODULES if m in sys.modules]
    if hits:
        raise AssertionError(f"quarantine collision: {hits} loaded in the same process as n's 5(f) primitive")


assert_quarantine()

from ..adapters.base import Injection, PositionSpec, sha16_arr       # noqa: E402
from ..adapters.olmo_hf import OLMoHFAdapter                          # noqa: E402  (torch loads only in its __init__)
from . import schema                                                  # noqa: E402
from .sessions import Session                                         # noqa: E402


def mask_sha(mask: np.ndarray) -> str:
    """k's ``mask_sha`` form (echo/maskedprefix.py), restated: sha256 of the int8 mask's bytes, 16 hex."""
    return hashlib.sha256(np.ascontiguousarray(mask, dtype=np.int8).tobytes()).hexdigest()[:16]


def build_mask(n_positions: int, spans: Sequence[Sequence], sign: int) -> np.ndarray:
    """int8 over [0, n): ``sign`` on the spans, 0 elsewhere; spans ascending, disjoint, ending before the read."""
    n = int(n_positions)
    mask = np.zeros(n, dtype=np.int8)
    prev = 0
    for a, b, _z in spans:
        a, b = int(a), int(b)
        if not prev <= a < b <= n - 1:
            raise AssertionError(f"span [{a}, {b}) is unordered, overlaps, or reaches the read position {n - 1}")
        mask[a:b] = sign
        prev = b
    if mask[n - 1] != 0:
        raise AssertionError("the read position is steered")
    return mask


@dataclass
class Prefill:
    logits_last: np.ndarray              # float32 [V], the read position's next-token logits
    captures: dict                       # layer -> float32 [D] at the read position
    handle: object                       # the backend's cache, opaque here


class Backend(Protocol):
    def prefill(self, ids: Sequence[int], injections: Sequence[Injection],
                capture_layers: Sequence[int]) -> Prefill: ...

    def continue_label(self, pre: Prefill, label_ids: Sequence[int]) -> np.ndarray:
        """Logits [len(label_ids) - 1, V]: row j predicts label token j + 1, through the prefill's cache, no
        injection; the cache is left as the prefill made it."""

    def full(self, ids: Sequence[int], label_ids: Sequence[int], injections: Sequence[Injection],
             capture_layers: Sequence[int]) -> tuple[np.ndarray, dict]:
        """One uncached forward over ``ids + label_ids[:-1]``: logits [len(label_ids), V] at positions
        len(ids) - 1 ... (row i predicts label token i) and the captures at position len(ids) - 1."""


def _logp(logits_row: np.ndarray, tok: int) -> float:
    lg = np.asarray(logits_row, dtype=np.float64)
    mx = float(lg.max())
    return float(lg[int(tok)] - (mx + math.log(float(np.sum(np.exp(lg - mx))))))


def _finite(*arrs) -> bool:
    return all(bool(np.all(np.isfinite(np.asarray(a, dtype=np.float64)))) for a in arrs)


def score_cached(pre: Prefill, cont: np.ndarray, label_ids: Sequence[int]) -> list[float]:
    rows = [pre.logits_last] + [cont[j] for j in range(len(label_ids) - 1)]
    return [_logp(rows[i], label_ids[i]) for i in range(len(label_ids))]


def _sigmoid(x: float) -> float:
    if x >= 0.0:
        return 1.0 / (1.0 + math.exp(-x))
    e = math.exp(x)
    return e / (1.0 + e)


def restricted(rows_S: Sequence[np.ndarray], ls: Sequence[int], lu: Sequence[int], present_first_is_S: bool) -> dict:
    """The restricted two-label read at the labels' first divergent token: p_S and p_U from the two logits (a
    sigmoid of their difference, so no division by an underflowed mass), the mass under the full softmax."""
    k = schema.shared_prefix(list(ls), list(lu))
    row = np.asarray(rows_S[k], dtype=np.float64)
    mx = float(row.max())
    lse = mx + math.log(float(np.sum(np.exp(row - mx))))
    a, b = float(row[ls[k]]), float(row[lu[k]])
    p_s, p_u = _sigmoid(a - b), _sigmoid(b - a)
    mass = math.exp(a - lse) + math.exp(b - lse)
    tie = "S" if present_first_is_S else "U"
    top1 = int(np.argmax(row))
    return {"k": k, "tok_S": int(ls[k]), "tok_U": int(lu[k]), "p_S": p_s, "p_U": p_u, "label_mass": mass,
            "pick": "S" if p_s > p_u else "U" if p_u > p_s else tie, "top1_id": top1,
            "top1_is_label": top1 in (int(ls[k]), int(lu[k]))}


@dataclass(frozen=True)
class ReadSpec:
    """One read of n §2.4: everything but the numbers. Built by the runner from the lock; checked here."""
    arm: str
    direction_id: str
    dose_label: str
    dose_value: float
    injection: Injection | None          # None exactly when nothing is injected
    told_line: str | None = None
    schedule_zone: str | None = None


def _placed(spec: ReadSpec, session: Session, n: int):
    kind = schema.ARM_SPAN_KIND[spec.arm]
    sign = schema.DOSES[spec.dose_label][1]
    steered = sign != 0
    if steered != (spec.injection is not None):
        raise AssertionError(f"{spec.arm} {spec.dose_label}: an injection exactly when the dose is nonzero")
    spans = session.spans(kind) if steered else []
    mask = build_mask(n, spans, sign)
    placed = []
    if steered:
        inj = spec.injection
        if (inj.alpha > 0) != (sign > 0):
            raise AssertionError("the injection's sign is not the dose's")
        placed = [inj.with_positions(PositionSpec.spans(*[(a, b) for a, b, _ in spans]))]
        covered = np.zeros(n, dtype=np.int8)
        for p in range(n):
            if placed[0].positions.contains(p):
                covered[p] = sign
        if not np.array_equal(covered, mask) or placed[0].positions.touches_last(n):
            raise AssertionError("the placed PositionSpec disagrees with the mask")
    return spans, mask, placed


def read(backend: Backend, session: Session, ids: Sequence[int], ids_sha_bk: str | None, spec: ReadSpec,
         label_ids_S: Sequence[int], label_ids_U: Sequence[int], capture_layers: Sequence[int],
         *, fidelity_reason: str | None, shadow: Mapping | None, identity_bound: float | None,
         launch_index: int, capture_row: int, clock=None) -> tuple[dict, dict]:
    """One read: the cached path, the fresh re-computation if ``fidelity_reason``, the captures. Returns the record
    (``schema.RECORD_FIELDS``, not yet checked against a stage identity: the runner does that before the write) and
    the read position's residuals by layer for the cell's capture arrays."""
    assert_quarantine()
    import time
    clock = clock or time.perf_counter
    t0 = clock()
    n = len(ids)
    read_position = n - 1
    spans, mask, placed = _placed(spec, session, n)
    steered = bool(placed)
    sid = session.session_id
    if steered:
        if shadow is None or shadow.get("read_id") != schema.shadow_read_id(sid):
            raise AssertionError(f"{sid}: a steered read needs its shadow's record on disk (5(f)(i))")
        if shadow["ids_sha"] != _sha(ids):
            raise AssertionError(f"{sid}: the shadow's token ids are not this read's")
    ls, lu = [int(x) for x in label_ids_S], [int(x) for x in label_ids_U]
    pre = backend.prefill(ids, placed, capture_layers)
    cont_S = backend.continue_label(pre, ls)
    cont_U = backend.continue_label(pre, lu)
    rows_S = [pre.logits_last] + [cont_S[j] for j in range(len(ls) - 1)]
    finite = _finite(pre.logits_last, cont_S, cont_U)
    rec_nums = {"logprob_S_tokens": None, "logprob_U_tokens": None, "logprob_S": None, "logprob_U": None,
                "margin": None, "restricted": None}
    if finite:
        ts, tu = score_cached(pre, cont_S, ls), score_cached(pre, cont_U, lu)
        finite = _finite(ts, tu)
        if finite:
            lps, lpu = math.fsum(ts), math.fsum(tu)
            rec_nums = {"logprob_S_tokens": ts, "logprob_U_tokens": tu, "logprob_S": lps, "logprob_U": lpu,
                        "margin": lps - lpu,
                        "restricted": restricted(rows_S, ls, lu, session.present_first_is_S)}
    caps = {int(l): np.asarray(pre.captures[int(l)], dtype=np.float32) for l in capture_layers}
    fid = None
    dfr = None
    if fidelity_reason is not None:
        tf0 = clock()
        rows_fS, cap_f = backend.full(ids, ls, placed, capture_layers)
        rows_fU, cap_fU = backend.full(ids, lu, placed, capture_layers)
        dfr = max(0, int(round((clock() - tf0) * 1000)))
        f_finite = _finite(rows_fS, rows_fU)
        fid = {"reason": fidelity_reason, "finite": False, "fresh_logprob_S": None, "fresh_logprob_U": None,
               "fresh_margin": None, "absdiff": None, "scale": None, "rel": None, "exceeds_tau": None,
               "exceeds_tau4": None, "fresh_capture_sha16": None,
               "fresh_capture_sha16_U": None}
        if f_finite:
            fs = math.fsum(_logp(rows_fS[i], ls[i]) for i in range(len(ls)))
            fu = math.fsum(_logp(rows_fU[i], lu[i]) for i in range(len(lu)))
            if math.isfinite(fs) and math.isfinite(fu):
                fid.update(finite=True, fresh_logprob_S=fs, fresh_logprob_U=fu, fresh_margin=fs - fu,
                           fresh_capture_sha16={str(int(l)): sha16_arr(cap_f[int(l)]) for l in capture_layers},
                           fresh_capture_sha16_U={str(int(l)): sha16_arr(cap_fU[int(l)])
                                                  for l in capture_layers})
                if finite:
                    fid.update(schema.fidelity_numbers(rec_nums["margin"], rec_nums["logprob_S"],
                                                       rec_nums["logprob_U"], fs - fu))
    idc = None
    if not steered and fid is not None and identity_bound is not None:
        a = fid["absdiff"]
        idc = {"bound": float(identity_bound), "within": a is not None and a <= identity_bound}
    sign = schema.DOSES[spec.dose_label][1]
    inj = spec.injection
    rec = {
        "schema": schema.RECORD_SCHEMA,
        "read_id": schema.read_id(spec.arm, spec.direction_id, spec.dose_label, sid),
        "launch_index": int(launch_index), "arm": spec.arm, "session_id": sid, "bk_cell": session.bk_cell,
        "bk_run": session.bk_run, "cue_S": session.cue_S, "cue_U": session.cue_U, "present": list(session.present),
        "present_first_is_S": session.present_first_is_S, "direction_id": spec.direction_id,
        "direction_sha16": inj.direction_sha if steered else None, "dose_label": spec.dose_label,
        "dose_scale": schema.DOSES[spec.dose_label][0], "dose_value": float(spec.dose_value), "sign": sign,
        "alpha": abs(float(inj.alpha)) if steered else 0.0, "layer": int(inj.layer) if steered else None,
        "steered_spans": [[int(a), int(b), z] for a, b, z in spans], "n_steered": int(np.sum(mask != 0)),
        "mask_sha16": mask_sha(mask),
        "retention_interval": read_position - (int(spans[-1][1]) - 1) if steered else None,
        "shadow_read_id": schema.shadow_read_id(sid) if steered else None,
        "told_variant": schema.TOLD_VARIANT.get(spec.arm), "schedule_zone": spec.schedule_zone,
        "told_line": spec.told_line, "seq_len": n, "read_position": read_position, "ids_sha": _sha(ids),
        "ids_sha_bk": ids_sha_bk, "label_ids_S": ls, "label_ids_U": lu, "finite": finite, **rec_nums,
        "capture": {"row": int(capture_row), "sha16": {str(l): sha16_arr(v) for l, v in caps.items()}},
        "fidelity": fid, "identity": idc, "duration_ms": 0, "duration_ms_fresh": dfr,
    }
    total = max(0, int(round((clock() - t0) * 1000)))
    rec["duration_ms"] = max(total, dfr or 0)
    return rec, caps


def _sha(ids: Sequence[int]) -> str:
    from .sessions import ids_sha
    return ids_sha(ids)


class HFBackend:
    """The box's backend: an ``OLMoHFAdapter`` (unchanged) and its own hook plumbing.

    ``prefill``: one forward over the read sequence with ``use_cache=True`` under the adapter's hooks (offset 0), the
    read position's logits and captures kept; the cache is the adapter model's. ``continue_label``: the label's tokens
    but the last through that cache with no hook that injects (offset = the prefill's length), then the cache is
    cropped back to the prefill's length, so the next label continues from the same state. ``full``: one forward
    with ``use_cache=False`` over the read sequence and the label's tokens but the last, under the same hooks.
    PIN (Code, declared at the BUILD): the cache's ``crop`` is asserted present at construction; a backend without it
    is refused, never worked around."""

    def __init__(self, adapter) -> None:
        if not isinstance(adapter, OLMoHFAdapter):
            raise TypeError("HFBackend runs on OLMoHFAdapter only")
        self.a = adapter
        self.t = adapter._torch

    def _run(self, ids, injections, capture_layers, *, offset, past=None, use_cache, keep):
        t = self.t
        store: dict = {}
        off = [int(offset)]
        handles = self.a._make_hooks(list(injections), list(capture_layers), store, off)
        try:
            x = t.tensor([list(int(i) for i in ids)], device=self.a.device)
            with t.inference_mode():
                out = self.a._model(input_ids=x, past_key_values=past, use_cache=use_cache, logits_to_keep=keep)
        finally:
            for h in handles:
                h.remove()
        return out, store

    def prefill(self, ids, injections, capture_layers) -> Prefill:
        n = len(ids)
        out, store = self._run(ids, injections, capture_layers, offset=0, use_cache=True, keep=1)
        cache = out.past_key_values
        if not hasattr(cache, "crop"):
            raise RuntimeError("the model's KV cache has no crop(); the cached path is refused on this backend")
        caps = {int(l): store[int(l)][0, n - 1].to(self.t.float32).cpu().numpy() for l in capture_layers}
        return Prefill(logits_last=out.logits[0, -1, :].to(self.t.float32).cpu().numpy(), captures=caps,
                       handle=(cache, n))

    def continue_label(self, pre: Prefill, label_ids):
        cache, n = pre.handle
        L = len(label_ids)
        if L < 2:
            return np.zeros((0, pre.logits_last.shape[0]), dtype=np.float32)
        out, _ = self._run(list(label_ids)[:-1], (), (), offset=n, past=cache, use_cache=True, keep=L - 1)
        rows = out.logits[0, :, :].to(self.t.float32).cpu().numpy()
        cache.crop(n)
        if cache.get_seq_length() != n:
            raise RuntimeError("the cache did not crop back to the prefill's length")
        return rows

    def full(self, ids, label_ids, injections, capture_layers):
        n = len(ids)
        seq = list(ids) + list(label_ids)[:-1]
        L = len(label_ids)
        out, store = self._run(seq, injections, capture_layers, offset=0, use_cache=False, keep=L)
        rows = out.logits[0, :, :].to(self.t.float32).cpu().numpy()
        caps = {int(l): store[int(l)][0, n - 1].to(self.t.float32).cpu().numpy() for l in capture_layers}
        return rows, caps


def test_identity(u: np.ndarray, *, layer: int = 2, n_layers: int = 6, d_model: int = 12) -> tuple[dict, dict]:
    """SELFTEST-ONLY: a campaign identity for the numpy double (its geometry, the example dose map) and the unit
    directions by id ("valence" and the four others share ``u``'s sha for the N2/N1-P cases)."""
    ident = schema.example_identity()
    unit = np.asarray(u, np.float64) / np.linalg.norm(u)
    sha = sha16_arr(unit)
    dirs = {d: sha for d in ("valence", "span_reward", "span_sentiment", "span_character")}
    ident.update(layer=layer, capture_layers=list(range(layer + 1, n_layers)), n_layers=n_layers, d_model=d_model,
                 directions=dict(ident["directions"], **dirs))           # the band past the site (ADDENDUM-n1 §6.2)
    return ident, {d: unit for d in dirs}


def _selftest(chk, tmp) -> None:
    from .testing import CausalDouble, toy_session
    be = CausalDouble()
    s, ids = toy_session(3)
    u = np.random.default_rng(7).standard_normal(be.d_model)
    ident, dirs = test_identity(u, n_layers=be.n_layers, d_model=be.d_model)
    caps_l = ident["capture_layers"]
    LS, LU = [5, 9, 17], [5, 11, 2]

    def spec(arm, did, dl, sign=None, alpha=None):
        value = schema.dose_point_values(ident)[dl]
        if schema.DOSES[dl][1] == 0:
            return ReadSpec(arm, did, dl, value, None)
        a = schema.expected_alpha(dl, value, ident["dose_map"]) * schema.DOSES[dl][1]
        return ReadSpec(arm, did, dl, value, Injection(u=dirs.get(did, u), layer=ident["layer"], alpha=a))

    def rd(sp, shadow=None, reason="dose-rule", backend=be, sess=s, ii=ids):
        return read(backend, sess, ii, sess.ids_sha, sp, LS, LU, caps_l, fidelity_reason=reason, shadow=shadow,
                    identity_bound=ident["identity_bound"], launch_index=0, capture_row=0)

    def ok_record(name, rec):
        try:
            schema.check_record(rec, ident)
            chk(name, True, "")
        except schema.SchemaError as e:
            chk(name, False, str(e))

    sh, sh_caps = rd(spec("N1-V", "none", "0"))
    ok_record("primitive: the shadow's record passes check_record", sh)
    chk("primitive: the shadow carries the identity check, within the bound (cached == fresh in the double)",
        sh["identity"] == {"bound": 0.0, "within": True} and sh["fidelity"]["absdiff"] == 0.0, sh["identity"])
    chk("primitive: the shadow's mask is all zeros", sh["mask_sha16"] == mask_sha(np.zeros(len(ids), np.int8)), "")
    try:
        rd(spec("N1-V", "valence", "+1"))
        chk("primitive: a steered read without its shadow is refused (5(f)(i))", False, "accepted")
    except AssertionError:
        chk("primitive: a steered read without its shadow is refused (5(f)(i))", True, "")
    try:
        rd(spec("N1-V", "valence", "+1"), shadow=dict(sh, ids_sha="0" * 16))
        chk("primitive: a shadow over other token ids is refused", False, "accepted")
    except AssertionError:
        chk("primitive: a shadow over other token ids is refused", True, "")
    st, st_caps = rd(spec("N1-V", "valence", "+1"), shadow=sh)
    ok_record("primitive: a steered +1 record passes check_record", st)
    chk("primitive: the state moves the read position's margin (the channel exists in the double)",
        st["margin"] != sh["margin"], (st["margin"], sh["margin"]))
    chk("primitive: the captures are the band past the site (ADDENDUM-n1 §6.2)",
        list(caps_l) == list(range(ident["layer"] + 1, ident["n_layers"])) and sorted(st_caps) == list(caps_l), "")
    chk("primitive: the band's first layer (site + 1) carries the state: the read position's residual is not the "
        "shadow's there", not np.array_equal(st_caps[caps_l[0]], sh_caps[caps_l[0]]), "")
    chk("primitive: ...and at the last layer", not np.array_equal(st_caps[caps_l[-1]], sh_caps[caps_l[-1]]), "")
    site = ident["layer"]
    placed_st = _placed(spec("N1-V", "valence", "+1"), s, len(ids))[2]       # placed by read()'s own helper
    pre_st, pre_sh = be.prefill(ids, placed_st, [site]), be.prefill(ids, [], [site])
    chk("primitive: AT THE SITE the read position's residual is the shadow's (a state added at a layer's output on "
        "earlier positions reaches the read position only from the next layer on: why the band starts past it, "
        "ledger (77))", np.array_equal(pre_st.captures[site], pre_sh.captures[site]), "")
    S_spans = [list(x) for x in s.spans("S")]
    chk("primitive: the steered spans are the session's six S turns", st["steered_spans"] == S_spans, "")
    m = build_mask(len(ids), s.spans("S"), 1)
    chk("primitive: provenance: mask_sha16 of the S-span mask, n_steered, retention",
        st["mask_sha16"] == mask_sha(m) and st["n_steered"] == int(np.sum(m != 0))
        and st["retention_interval"] == (len(ids) - 1) - (S_spans[-1][1] - 1), st["retention_interval"])
    st_m, _ = rd(spec("N1-V", "valence", "-1"), shadow=sh)
    ok_record("primitive: a steered -1 record passes check_record", st_m)
    chk("primitive: the mask carries the sign", st_m["mask_sha16"] == mask_sha(build_mask(len(ids), s.spans("S"), -1)),
        "")
    p1, _ = rd(spec("N1-P", "valence", "+1"), shadow=sh)
    ok_record("primitive: an N1-P record (both zones' twelve turns) passes check_record", p1)
    chk("primitive: N1-P steers all twelve turn spans", len(p1["steered_spans"]) == 12, len(p1["steered_spans"]))
    e2, _ = rd(spec("N2-E", "span_reward", "f0.20"), shadow=sh, reason=None)
    ok_record("primitive: an N2-E f = 0.20 record (no re-computation) passes check_record", e2)
    chk("primitive: the restricted read sits at the first divergent label token (k = 1)",
        st["restricted"]["k"] == 1 and st["restricted"]["tok_S"] == 9 and st["restricted"]["tok_U"] == 11, "")
    bad = spec("N1-V", "valence", "+1")
    bad = ReadSpec(bad.arm, bad.direction_id, bad.dose_label, bad.dose_value, bad.injection.with_sign(-1))
    try:
        rd(bad, shadow=sh)
        chk("primitive: an injection whose sign is not the dose's is refused", False, "accepted")
    except AssertionError:
        chk("primitive: an injection whose sign is not the dose's is refused", True, "")
    try:
        build_mask(10, [[2, 10, "Zone W6"]], 1)
        chk("primitive: a span reaching the read position is refused", False, "accepted")
    except AssertionError:
        chk("primitive: a span reaching the read position is refused", True, "")
    biased = CausalDouble(fresh_bias=(9, 0.5))
    sh_b, _ = rd(spec("N1-V", "none", "0"), backend=biased)
    st_b, _ = rd(spec("N1-V", "valence", "+1"), shadow=sh_b, backend=biased)
    chk("primitive: a fresh path that differs is recorded as an exceedance, not refused",
        st_b["fidelity"]["exceeds_tau"] is True and st_b["fidelity"]["absdiff"] > 0, st_b["fidelity"]["rel"])
    ok_record("primitive: ...and its record passes check_record", st_b)
    chk("primitive: the shadow's identity check fails under a differing fresh path",
        sh_b["identity"]["within"] is False, sh_b["identity"])
    sys.modules["valence_core.e2b.statepresent"] = types.ModuleType("valence_core.e2b.statepresent")
    try:
        rd(spec("N1-V", "none", "0"))
        chk("primitive: the 5(e) primitive in the process is refused before a read", False, "accepted")
    except AssertionError:
        chk("primitive: the 5(e) primitive in the process is refused before a read", True, "")
    finally:
        del sys.modules["valence_core.e2b.statepresent"]

    # known answers: the restricted read's row, its stability, BK's fidelity criterion, the record's span bound
    r0 = np.zeros(97)
    r0[11] = 5.0                                            # row 0 would favour U's divergent token
    r1 = np.zeros(97)
    r1[9] = 5.0                                             # the first divergent token's row favours S's
    rr = restricted([r0, r1, np.zeros(97)], [5, 9, 17], [5, 11, 2], False)
    chk("primitive: the restricted read uses the first divergent token's row (a known answer)",
        rr["k"] == 1 and rr["pick"] == "S" and abs(rr["p_S"] - _sigmoid(5.0)) < 1e-12, rr)
    rz = np.zeros(97)
    rz[9], rz[11] = -2000.0, -2001.0
    ru = restricted([np.zeros(97), rz], [5, 9, 17], [5, 11, 2], False)
    chk("primitive: labels far below the softmax's mass still give p_S (no division by an underflowed mass)",
        abs(ru["p_S"] - _sigmoid(1.0)) < 1e-12 and ru["label_mass"] == 0.0 and ru["pick"] == "S", ru)
    fn = schema.fidelity_numbers(2.0, -1.0, -3.0, 2.05)
    chk("primitive: BK's fidelity criterion, a known answer: rel = |cached - fresh| / max(|lpS|, |lpU|) against "
        "TAU = 0.0178835444 (n §2.1)",
        f"{schema.TAU:.10f}" == "0.0178835444" and abs(fn["scale"] - 3.0) < 1e-12
        and abs(fn["rel"] - 0.05 / 3.0) < 1e-12 and fn["exceeds_tau"] is False and fn["exceeds_tau4"] is True
        and schema.fidelity_numbers(2.0, -1.0, -3.0, 2.06)["exceeds_tau"] is True, fn)
    ident0 = schema.example_identity()
    bad = schema.example_record(ident0, "N1-V", "valence", "+1", 3)
    sp = [list(x) for x in bad["steered_spans"]]
    sp[-1][1] = bad["seq_len"]
    bad.update(steered_spans=sp, n_steered=sum(b - a for a, b, _ in sp), retention_interval=0)
    try:
        schema.check_record(bad, ident0)
        msg = "accepted"
    except schema.SchemaError as e:
        msg = str(e)
    chk("primitive: a record whose span reaches the read position is refused by the span bound (5(f))",
        "reaches the read" in msg, msg[:160])
