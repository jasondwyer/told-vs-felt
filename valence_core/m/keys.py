"""PROPOSAL-m keys, streams and direct seeds (v1.11 §2.1, m:159; §2.3, m:176).

Every stream is ``default_rng(crc32(key.encode()) % 2**31)`` -- f1's form
(f_sessions.py:107-108, :273-274) and e2a's ``session_rng`` (session_e2a.py:93-96,
frozen) applied to the whole key, so ``stream(f"{prefix}|{s}")`` is the stream
``session_rng(prefix, s)`` returns. The one key that is not a stream is G-CAL's
``m-cal|{pool}|{i}|{seed}``, used directly as a generation seed under f0's form
(f0_calibrate.py:152).

Only the Q-F0 and OLMo units are built at step 4 (§8 step 4, m:357); Q-F3's keys
(``m-f3-items|{s}`` and the rest) are written at step 19 and refused here.
"""
from __future__ import annotations

import zlib

import numpy as np

UNITS_BUILT = ("Q-F0", "OLMo-sft", "OLMo-dpo", "OLMo-instruct")
CKPTS = ("sft", "dpo", "instruct")          # base has no told control, decision (7')
CAL_POOLS = ("CORR_clean", "CORR_corrupted")  # f0's literals, f0_calibrate.py:184-186
QF0_TEMPLATES = ("A0", "A0s")               # §2.4's table order: contrast, then sham
GATES_QF0 = ("time", "id", "qual")
GATES_OLMO = ("time", "qual")               # no G-ID on OLMo (uncached path, m:267)


def stream(key: str) -> np.random.Generator:
    """The key-to-generator function of every m stream (m:159)."""
    return np.random.default_rng(zlib.crc32(key.encode()) % 2**31)


#: f1's ``f|CORR|0`` ``permutation(16)`` (maps/f1.md; DESIGN §1.2): numpy's stream
#: known answer, the one value every m stream's stability rests on.
F_CORR_0_PERMUTATION = (7, 9, 10, 1, 13, 12, 6, 2, 5, 8, 0, 11, 15, 3, 4, 14)


def stream_known_answer() -> list[str]:
    """The ``f|CORR|0`` permutation known answer at run time, on THIS site's numpy; [] =
    clean. PIN (Code, declared at LOCK v0.1): run at every stage's startup on both sites
    (rule 27; numpy promises no stream stability across versions), a mismatch being a
    STOP before any session -- every key, item stream and render of record rests on it."""
    try:
        got = tuple(int(x) for x in stream("f|CORR|0").permutation(16).tolist())
    except Exception as e:                      # noqa: BLE001 -- a broken stream is a problem
        return [f"numpy stream known answer: f|CORR|0 permutation raised {type(e).__name__}"]
    if got != F_CORR_0_PERMUTATION:
        return [f"numpy stream known answer: f|CORR|0 permutation(16) is {list(got)}, expected "
                f"{list(F_CORR_0_PERMUTATION)} (numpy {np.__version__})"]
    return []


def cal_seed(pool: str, i: int, seed: int) -> int:
    """G-CAL's direct generation seed (m:176): f0's form under m's key."""
    if pool not in CAL_POOLS:
        raise ValueError(f"G-CAL pool literal must be one of {CAL_POOLS}, got {pool!r}")
    if seed not in (0, 1, 2, 3):
        raise ValueError(f"G-CAL seed index must be 0..3, got {seed!r}")
    return zlib.crc32(f"m-cal|{pool}|{i}|{seed}".encode()) % 2**31


def _unit_parts(unit: str) -> tuple[str, str | None]:
    if unit == "Q-F0":
        return "qwen", None
    if unit.startswith("OLMo-") and unit[5:] in CKPTS:
        return "olmo", unit[5:]
    if unit.startswith("Q-F3"):
        raise NotImplementedError("Q-F3 keys are built at step 19 (decision (10)); not at step 4")
    raise ValueError(f"unknown unit {unit!r}; built units are {UNITS_BUILT}")


def templates(unit: str) -> tuple[str, str]:
    """(contrast, sham) template names of a unit, in §2.4's table order."""
    sub, ckpt = _unit_parts(unit)
    if sub == "qwen":
        return QF0_TEMPLATES
    return (f"A0-OLMo-{ckpt}", f"A0s-OLMo-{ckpt}")


def is_contrast(template: str) -> bool:
    if template == "A0" or template.startswith("A0-OLMo-"):
        return True
    if template == "A0s" or template.startswith("A0s-OLMo-"):
        return False
    raise ValueError(f"not a Q-F0 or OLMo template: {template!r}")


def is_sham(template: str) -> bool:
    return not is_contrast(template)


def _check_template(unit: str, template: str) -> None:
    if template not in templates(unit):
        raise ValueError(f"template {template!r} does not belong to unit {unit!r}")


def item_key(unit: str, s: int, gate: str | None = None) -> str:
    """Item stream, shared across a unit's templates at the same s (m:159)."""
    sub, ckpt = _unit_parts(unit)
    if sub == "qwen":
        if gate is None:
            return f"m-items|{s}"
        if gate not in GATES_QF0:
            raise ValueError(f"Q-F0 gate must be one of {GATES_QF0}, got {gate!r}")
        return f"m-items-{gate}|{s}"
    if gate is None:
        return f"m-olmo-items|{ckpt}|{s}"
    if gate not in GATES_OLMO:
        raise ValueError(f"OLMo gate must be one of {GATES_OLMO}, got {gate!r}")
    return f"m-olmo-items-{gate}|{ckpt}|{s}"


def arm_key(unit: str, stage: str, template: str, s: int) -> str:
    """Arm rng: seeds and menu orders only (m:159)."""
    sub, ckpt = _unit_parts(unit)
    _check_template(unit, template)
    if sub == "qwen":
        if stage == "campaign":
            return f"m|{template}|{s}"
        if stage == "time":
            return f"m-time|{template}|{s}"
        if stage == "id":
            if template != "A0s":
                raise ValueError("G-ID-F0m runs the A0s template only (m:281)")
            return f"m-id|F0m|{template}|{s}"
        if stage == "qual":
            return f"m-f0m|{template}|{s}"
        raise ValueError(f"unknown Q-F0 stage {stage!r}")
    if stage == "campaign":
        return f"m-olmo|{ckpt}|{template}|{s}"
    if stage == "time":
        return f"m-olmo-time|{ckpt}|{template}|{s}"
    if stage == "qual":
        return f"m-olmo-qual|{ckpt}|{template}|{s}"
    raise ValueError(f"unknown OLMo stage {stage!r} (no G-ID on OLMo)")


def item_gate(stage: str) -> str | None:
    """The gate tag of a stage's item stream (campaign has none)."""
    return None if stage == "campaign" else stage


def sched_key(unit: str, arm: str, b: int) -> str:
    _unit_parts(unit)
    _check_template(unit, arm)
    return f"m-sched|{unit}|{arm}|{b}"


def gate_sched_key(unit: str, gate: str, template: str) -> str:
    sub, _ = _unit_parts(unit)
    allowed = GATES_QF0 if sub == "qwen" else GATES_OLMO
    if gate not in allowed:
        raise ValueError(f"gate {gate!r} not in {allowed} for {unit!r}")
    _check_template(unit, template)
    return f"m-sched|{unit}|{gate}|{template}|0"


def _selftest(chk) -> None:
    from valence_core.session_e2a import session_rng

    a = stream("m|A0|3").integers(2**31, size=4).tolist()
    b = session_rng("m|A0", 3).integers(2**31, size=4).tolist()
    chk("keys: stream(prefix|s) == session_e2a.session_rng(prefix, s)", a == b, a[:2])
    perm = stream("f|CORR|0").permutation(16).tolist()
    want = [7, 9, 10, 1, 13, 12, 6, 2, 5, 8, 0, 11, 15, 3, 4, 14]
    chk("keys: numpy stream-stability known answer (f|CORR|0 permutation)", perm == want,
        perm, f"numpy {np.__version__}")
    chk("keys: stream_known_answer is clean on this numpy (the run-time form of the check)",
        stream_known_answer() == [] and list(F_CORR_0_PERMUTATION) == want, stream_known_answer())
    from unittest import mock

    def _philox(key: str) -> np.random.Generator:     # a different bit stream, same seed
        return np.random.Generator(np.random.Philox(zlib.crc32(key.encode()) % 2**31))

    def _broken(key: str):
        raise RuntimeError("no stream")

    fired = []
    for alt in (_philox, _broken):
        with mock.patch(f"{__name__}.stream", alt):
            fired.append(stream_known_answer())
    chk("keys: stream_known_answer fires on a mutated stream (a Philox stream; a raising stream)",
        all(len(f) == 1 and "known answer" in f[0] for f in fired), fired)
    chk("keys: cal_seed is crc32 % 2**31 of m-cal|pool|i|seed",
        cal_seed("CORR_clean", 3, 2) == zlib.crc32(b"m-cal|CORR_clean|3|2") % 2**31)
    try:
        cal_seed("CORR", 0, 0)
        ok = False
    except ValueError:
        ok = True
    chk("keys: cal_seed refuses a pool literal outside f0's two", ok)
    chk("keys: Q-F0 item / gate item keys",
        (item_key("Q-F0", 5), item_key("Q-F0", 5, "qual"))
        == ("m-items|5", "m-items-qual|5"))
    chk("keys: OLMo item keys carry {ckpt}",
        (item_key("OLMo-dpo", 2), item_key("OLMo-dpo", 2, "time"))
        == ("m-olmo-items|dpo|2", "m-olmo-items-time|dpo|2"))
    chk("keys: arm keys (campaign, time, id, qual; OLMo campaign/qual)",
        [arm_key("Q-F0", "campaign", "A0", 1), arm_key("Q-F0", "time", "A0s", 0),
         arm_key("Q-F0", "id", "A0s", 4), arm_key("Q-F0", "qual", "A0", 7),
         arm_key("OLMo-sft", "campaign", "A0-OLMo-sft", 2),
         arm_key("OLMo-sft", "qual", "A0s-OLMo-sft", 9)]
        == ["m|A0|1", "m-time|A0s|0", "m-id|F0m|A0s|4", "m-f0m|A0|7",
            "m-olmo|sft|A0-OLMo-sft|2", "m-olmo-qual|sft|A0s-OLMo-sft|9"])
    refused = []
    for fn in (lambda: arm_key("Q-F0", "id", "A0", 0), lambda: item_key("OLMo-sft", 0, "id"),
               lambda: arm_key("Q-F0", "campaign", "A0-OLMo-sft", 0),
               lambda: item_key("Q-F3", 0), lambda: templates("OLMo-base")):
        try:
            fn()
            refused.append(False)
        except (ValueError, NotImplementedError):
            refused.append(True)
    chk("keys: refusals (G-ID on A0; id on OLMo; cross-unit template; Q-F3; base)",
        all(refused), refused)
    chk("keys: schedule keys",
        (sched_key("Q-F0", "A0s", 3), gate_sched_key("OLMo-instruct", "qual", "A0-OLMo-instruct"))
        == ("m-sched|Q-F0|A0s|3", "m-sched|OLMo-instruct|qual|A0-OLMo-instruct|0"))
    chk("keys: contrast/sham classification",
        [is_contrast(t) for t in ("A0", "A0s", "A0-OLMo-dpo", "A0s-OLMo-dpo")]
        == [True, False, True, False])
