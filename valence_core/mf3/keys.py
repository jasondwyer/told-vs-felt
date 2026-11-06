"""Q-F3's keys, streams and template vocabulary (PROPOSAL-m v1.11 §2.1 m:159; §2.4 m:184-186).

Every stream is ``valence_core.m.keys.stream`` -- ``default_rng(crc32(key.encode()) % 2**31)``,
imported, never re-implemented. m's ``keys.py`` refuses Q-F3 (``_unit_parts``); that refusal stays
as it is (the seat's Q1), and Q-F3's key builders live here:

  items      campaign ``m-f3-items|{s}`` (shared across the six arms, so sham session s sees
             contrast session s's items uncorrupted); gates ``m-f3-items-{time|id|qual}|{s}``;
  arm rngs   campaign ``m|{arm}|{s}``; G-TIME-F3 ``m-time|{arm}|{s}``; G-ID-F3
             ``m-id|F3|{template}|{s}`` (A2s, A3s); G-F3 ``m-f3|{template}|{s}``;
  schedules  ``m-sched|Q-F3|{arm}|{b}``; gate stages ``m-sched|Q-F3|{gate}|{template}|0``.

``{template}`` is the arm name of §2.4's table (m:159); A2 and A2s, and A3 and A3s, carry identical
banner bytes, so the contrast/sham role is the template name's (``is_contrast``) and is asserted on
the delivery by the verifier (G-VER). Every Q-F3 key differs from every Q-F0 and OLMo key by its arm
name or prefix (asserted in the self-test).
"""
from __future__ import annotations

from valence_core.m import keys as m_keys

UNIT = "Q-F3"
#: §2.4's table order (m:184-186): contrast, then its sham, per tier.
TEMPLATES = ("A1", "A1s", "A2", "A2s", "A3", "A3s")
CONTRAST = ("A1", "A2", "A3")
SHAM = ("A1s", "A2s", "A3s")
PAIRS = (("A1", "A1s"), ("A2", "A2s"), ("A3", "A3s"))
GATES = ("time", "id", "qual")
STAGES = GATES + ("campaign",)
#: m:295: "A2s and A3s once each".
GID_TEMPLATES = ("A2s", "A3s")
#: m:159: the clause factor exists only where the TOLD line names labels (A1, A1s).
LABEL_NAMING = ("A1", "A1s")

stream = m_keys.stream


def check_template(template: str) -> str:
    if template not in TEMPLATES:
        raise ValueError(f"not a Q-F3 template: {template!r}; Q-F3's are {TEMPLATES}")
    return template


def is_contrast(template: str) -> bool:
    return check_template(template) in CONTRAST


def is_sham(template: str) -> bool:
    return not is_contrast(template)


def sham_of(template: str) -> str:
    """A contrast arm's matched sham (m:310: A1-A1s, A2-A2s, A3-A3s)."""
    for c, s in PAIRS:
        if template == c:
            return s
    raise ValueError(f"{template!r} is not a Q-F3 contrast arm")


def names_labels(template: str) -> bool:
    """m:159: does the arm's TOLD line name labels (the clause-order factor exists)?"""
    return check_template(template) in LABEL_NAMING


def _check_stage(stage: str) -> str:
    if stage not in STAGES:
        raise ValueError(f"unknown Q-F3 stage {stage!r}; stages are {STAGES}")
    return stage


def item_gate(stage: str) -> str | None:
    """The gate tag of a stage's item stream (the campaign has none)."""
    return None if _check_stage(stage) == "campaign" else stage


def item_key(s, gate: str | None = None) -> str:
    """m:159: ``m-f3-items|{s}`` (campaign) / ``m-f3-items-{gate}|{s}`` (gate stages)."""
    if gate is None:
        return f"m-f3-items|{s}"
    if gate not in GATES:
        raise ValueError(f"Q-F3 gate must be one of {GATES}, got {gate!r}")
    return f"m-f3-items-{gate}|{s}"


def arm_key(stage: str, template: str, s) -> str:
    """m:159's arm rngs (seeds, reasoning seeds, menu orders)."""
    check_template(template)
    _check_stage(stage)
    if stage == "campaign":
        return f"m|{template}|{s}"
    if stage == "time":
        return f"m-time|{template}|{s}"
    if stage == "id":
        if template not in GID_TEMPLATES:
            raise ValueError(f"G-ID-F3 runs {GID_TEMPLATES} only (m:295), not {template!r}")
        return f"m-id|F3|{template}|{s}"
    return f"m-f3|{template}|{s}"


def sched_key(arm: str, b) -> str:
    """m:159: the b-th campaign balance unit's permutation key."""
    check_template(arm)
    return f"m-sched|{UNIT}|{arm}|{b}"


def gate_sched_key(gate: str, template: str) -> str:
    """m:159: a gate-stage template's pi key."""
    if gate not in GATES:
        raise ValueError(f"Q-F3 gate must be one of {GATES}, got {gate!r}")
    check_template(template)
    if gate == "id" and template not in GID_TEMPLATES:
        raise ValueError(f"G-ID-F3 runs {GID_TEMPLATES} only (m:295), not {template!r}")
    return f"m-sched|{UNIT}|{gate}|{template}|0"


def key_templates(stage: str, template_set) -> dict:
    """m:159's key templates for a stage, rendered with literal {s}/{b} fields (the identity's)."""
    gate = item_gate(stage)
    return {t: {"arm": arm_key(stage, t, "{s}"), "items": item_key("{s}", gate),
                "sched": sched_key(t, "{b}") if stage == "campaign" else gate_sched_key(gate, t)}
            for t in template_set}


def _selftest(chk) -> None:
    import zlib

    import numpy as np

    chk("mf3.keys: stream is valence_core.m.keys.stream (imported, the one key-to-generator function)",
        stream is m_keys.stream
        and stream("m-f3-items|3").integers(2**31, size=3).tolist()
        == np.random.default_rng(zlib.crc32(b"m-f3-items|3") % 2**31).integers(2**31, size=3).tolist())
    chk("mf3.keys: item keys -- campaign m-f3-items|{s}; gates m-f3-items-{time|id|qual}|{s} (m:159)",
        [item_key(5), item_key(5, "time"), item_key(5, "id"), item_key(5, "qual")]
        == ["m-f3-items|5", "m-f3-items-time|5", "m-f3-items-id|5", "m-f3-items-qual|5"])
    chk("mf3.keys: arm keys -- campaign m|{arm}|{s}, time m-time|{arm}|{s}, id m-id|F3|{t}|{s}, qual "
        "m-f3|{t}|{s} (m:159, m:295, m:297)",
        [arm_key("campaign", "A2", 7), arm_key("time", "A1s", 0), arm_key("id", "A3s", 2),
         arm_key("qual", "A3", 4)] == ["m|A2|7", "m-time|A1s|0", "m-id|F3|A3s|2", "m-f3|A3|4"])
    chk("mf3.keys: schedule keys m-sched|Q-F3|{arm}|{b} and m-sched|Q-F3|{gate}|{template}|0",
        (sched_key("A3s", 9), gate_sched_key("qual", "A1"), gate_sched_key("id", "A2s"))
        == ("m-sched|Q-F3|A3s|9", "m-sched|Q-F3|qual|A1|0", "m-sched|Q-F3|id|A2s|0"))
    refused = []
    for fn in (lambda: arm_key("id", "A2", 0), lambda: arm_key("id", "A1s", 0),
               lambda: gate_sched_key("id", "A3", ), lambda: arm_key("campaign", "A0", 0),
               lambda: item_key(0, "campaign"), lambda: arm_key("pilot", "A1", 0),
               lambda: sched_key("A0s", 0), lambda: is_contrast("A0"), lambda: sham_of("A1s")):
        try:
            fn()
            refused.append(False)
        except (ValueError, TypeError):
            refused.append(True)
    chk("mf3.keys: refusals (G-ID on A2, A1s; id schedule on A3; a Q-F0 template; a gate word 'campaign'; "
        "an unknown stage; A0s schedule; A0's role; a sham's sham)", all(refused), refused)
    chk("mf3.keys: contrast / sham / matched pairs / clause factor (m:159, m:184-186, m:310)",
        [is_contrast(t) for t in TEMPLATES] == [True, False, True, False, True, False]
        and [sham_of(c) for c in CONTRAST] == list(SHAM)
        and [names_labels(t) for t in TEMPLATES] == [True, True, False, False, False, False])
    # no Q-F3 key string can equal a Q-F0 or OLMo one (arm names and prefixes differ)
    f3 = {arm_key(st, t, s) for st in ("campaign", "time", "qual") for t in TEMPLATES for s in range(3)}
    f3 |= {arm_key("id", t, s) for t in GID_TEMPLATES for s in range(3)}
    f3 |= {item_key(s, g) for s in range(3) for g in (None,) + GATES}
    f3 |= {sched_key(t, b) for t in TEMPLATES for b in range(3)}
    f3 |= {gate_sched_key(g, t) for g in ("time", "qual") for t in TEMPLATES}
    f3 |= {gate_sched_key("id", t) for t in GID_TEMPLATES}
    other = set()
    for u in m_keys.UNITS_BUILT:
        for t in m_keys.templates(u):
            for s in range(3):
                for st in ("campaign", "time", "qual") + (("id",) if u == "Q-F0" and t == "A0s" else ()):
                    other.add(m_keys.arm_key(u, st, t, s))
                other.add(m_keys.sched_key(u, t, s))
            for g in (m_keys.GATES_QF0 if u == "Q-F0" else m_keys.GATES_OLMO):
                if g == "id" and t != "A0s":
                    continue
                other.add(m_keys.gate_sched_key(u, g, t))
        for s in range(3):
            for g in (None,) + (m_keys.GATES_QF0 if u == "Q-F0" else m_keys.GATES_OLMO):
                other.add(m_keys.item_key(u, s, g))
    chk("mf3.keys: no Q-F3 key string equals a Q-F0 or OLMo key string (disjoint streams)",
        not (f3 & other) and len(f3) > 100 and len(other) > 100, sorted(f3 & other)[:3])
    kt = key_templates("qual", ["A1", "A2s"])
    chk("mf3.keys: key templates render literal {s}/{b} fields",
        kt == {"A1": {"arm": "m-f3|A1|{s}", "items": "m-f3-items-qual|{s}", "sched": "m-sched|Q-F3|qual|A1|0"},
               "A2s": {"arm": "m-f3|A2s|{s}", "items": "m-f3-items-qual|{s}", "sched": "m-sched|Q-F3|qual|A2s|0"}}
        and key_templates("campaign", ["A3"])["A3"]["sched"] == "m-sched|Q-F3|A3|{b}")
