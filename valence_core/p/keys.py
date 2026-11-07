"""PROPOSAL-p's keys: the six OLMo key families under p's prefix (p v0.2 §4.1; ans2 Q4 (i); register entry (2)).

All six of m's OLMo families take p's prefix -- ``p-sched|...`` (the schedule permutation and the gate pi),
``p-olmo|...``, ``p-olmo-time|...``, ``p-olmo-qual|...`` (the arm streams), ``p-olmo-items|...`` and
``p-olmo-items-{gate}|...`` (the item streams) -- so no p stream coincides with an m stream. G-CAL-p's seeds alone stay
``m-cal|...`` (p §3.1; ``valence_core.m.keys.cal_seed``, unchanged).

PIN (Code, declared at the p BUILD): each p key is m's own key function's result with its leading ``m-`` replaced by
``p-`` -- m's validation and m's construction run unchanged (m's originals are captured at import, ``_M``), and only
the prefix differs; a unit outside the three OLMo units passes through to m's function unchanged (m's schedule
builder iterates every built unit, Q-F0 included, under the substitution; p writes the OLMo files only). Under
``substituted_keys`` (register entry (2)) m's four key functions are p's for the duration of one call.
"""
from __future__ import annotations

import contextlib
from typing import Iterator

from ..m import keys as m_keys
from . import register

CKPTS = m_keys.CKPTS
OLMO_UNITS = tuple(f"OLMo-{c}" for c in CKPTS)
FAMILIES = ("p-sched|", "p-olmo|", "p-olmo-time|", "p-olmo-qual|", "p-olmo-items|", "p-olmo-items-{gate}|")
_NAMES = ("item_key", "arm_key", "sched_key", "gate_sched_key")
_M = {n: getattr(m_keys, n) for n in _NAMES}      # m's originals, captured at import


class KeysStop(SystemExit):
    pass


def _p(m_key: str) -> str:
    if not m_key.startswith("m-"):
        raise KeysStop(f"KEYS STOP: m's OLMo key {m_key!r} does not begin 'm-' (p §4.1's rule cannot apply)")
    return "p-" + m_key[2:]


def item_key(unit: str, s, gate: str | None = None) -> str:
    k = _M["item_key"](unit, s, gate)
    return _p(k) if unit in OLMO_UNITS else k


def arm_key(unit: str, stage: str, template: str, s) -> str:
    k = _M["arm_key"](unit, stage, template, s)
    return _p(k) if unit in OLMO_UNITS else k


def sched_key(unit: str, arm: str, b) -> str:
    k = _M["sched_key"](unit, arm, b)
    return _p(k) if unit in OLMO_UNITS else k


def gate_sched_key(unit: str, gate: str, template: str) -> str:
    k = _M["gate_sched_key"](unit, gate, template)
    return _p(k) if unit in OLMO_UNITS else k


P_FUNCS = {"item_key": item_key, "arm_key": arm_key, "sched_key": sched_key, "gate_sched_key": gate_sched_key}


@contextlib.contextmanager
def substituted_keys() -> Iterator[None]:
    """Register entry (2): m's four key functions are p's for the block."""
    with register.substituted(2, m_keys, P_FUNCS):
        yield


def all_olmo_keys(funcs=None) -> list[str]:
    """Every OLMo key template of the six families as ``funcs`` (default p's) build them, ``s`` and ``b`` left as
    literals -- the comparison set of the self-test."""
    f = P_FUNCS if funcs is None else funcs
    out = []
    for u in OLMO_UNITS:
        out.append(f["item_key"](u, "{s}"))
        for g in m_keys.GATES_OLMO:
            out.append(f["item_key"](u, "{s}", g))
        for t in m_keys.templates(u):
            out.append(f["sched_key"](u, t, "{b}"))
            for stage in ("campaign",) + m_keys.GATES_OLMO:
                out.append(f["arm_key"](u, stage, t, "{s}"))
            for g in m_keys.GATES_OLMO:
                out.append(f["gate_sched_key"](u, g, t))
    return out


def _selftest(chk) -> None:
    pk, mk = all_olmo_keys(), all_olmo_keys(_M)
    chk("keys: every p OLMo key is m's key with 'm-' replaced by 'p-' (m's construction, p's prefix)",
        len(pk) == len(mk) == 45 and all(p == "p-" + m[2:] and m.startswith("m-") for p, m in zip(pk, mk)), len(pk))
    fam = {k.split("|")[0] + "|" for k in pk}
    chk("keys: the six families are p §4.1's (p-sched, p-olmo, p-olmo-time, p-olmo-qual, p-olmo-items, "
        "p-olmo-items-{gate})",
        fam == {"p-sched|", "p-olmo|", "p-olmo-time|", "p-olmo-qual|", "p-olmo-items|", "p-olmo-items-time|",
                "p-olmo-items-qual|"}, sorted(fam))
    chk("keys: no p key equals any m key (no p stream coincides with an m stream)", not (set(pk) & set(mk)))
    q = [(item_key("Q-F0", 3), _M["item_key"]("Q-F0", 3)), (arm_key("Q-F0", "time", "A0", 1),
                                                           _M["arm_key"]("Q-F0", "time", "A0", 1)),
         (sched_key("Q-F0", "A0s", 2), _M["sched_key"]("Q-F0", "A0s", 2))]
    chk("keys: a non-OLMo unit passes through to m's function unchanged", all(a == b for a, b in q), q)
    chk("keys: G-CAL-p's seeds stay m-cal (keys.cal_seed is m's, unsubstituted)",
        m_keys.cal_seed("CORR_clean", 0, 0) == __import__("zlib").crc32(b"m-cal|CORR_clean|0|0") % 2**31)
    with substituted_keys():
        inside = (m_keys.sched_key("OLMo-sft", "A0-OLMo-sft", 0), m_keys.item_key("OLMo-dpo", 4, "qual"))
    chk("keys: under register entry (2) m's key functions are p's for the block",
        inside == ("p-sched|OLMo-sft|A0-OLMo-sft|0", "p-olmo-items-qual|dpo|4"), inside)
    try:
        with substituted_keys():
            raise RuntimeError("planted")
    except RuntimeError:
        pass
    chk("keys: m's four key functions are m's own after the block, an exception included (term (c))",
        all(getattr(m_keys, n) is _M[n] for n in _NAMES))
