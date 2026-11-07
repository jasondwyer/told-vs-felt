"""PROPOSAL-p's dose -- ``corrupt_p``, m:176 with the eligible set restricted to the frame (p v0.2 §1; ans2 Q0).

THE RULE (p §1.1). An item's frame words are its first word and every word of the closed list ``FUNCTION_WORDS``,
a word being a maximal run of ASCII letters, matched case-insensitively; words inside a single-quoted span are never
frame words. Eligible positions = m:176's eligible positions (``corr._eligible_m``: non-word-initial ASCII letters
outside the single-quoted span) that lie inside a frame word. Everything else is m:176 unchanged.

THE FORM (p §1.4; register entry (1)). ``corrupt_p`` is ``corr.corrupt_m`` run with ``corr._eligible_m`` replaced,
for the duration of the call, by ``eligible_p`` -- so the walk, the per-slot draw, the replacement expression (inline
at corr.py:236), the roster skip and ``_k_m`` are m's code, run by import and never copied. ``eligible_p`` calls m's
own rule through ``_M_ELIGIBLE``, the function object captured at import (inside the call ``corr._eligible_m`` is
``eligible_p`` itself). ``valence_core/m/corr.py`` is not edited.

THE RENDERS OF RECORD (p §1.2; the seat's read of record, ans2 §0). Two identifications: p's convention,
``sha256(json.dumps(renders).encode())`` (first 16 hex ``1551c19997dc4541``), and m's, ``corr.renders_sha`` (the
newline-joined renders, whose full sha256 G-CAL artifacts record as ``renders_sha256``; ``6baf494960da4589``).
"""
from __future__ import annotations

import hashlib
import json
from typing import Sequence

from ..m import corr, keys as m_keys
from . import register

FUNCTION_WORDS = frozenset({"a", "an", "the", "of", "in", "on", "is", "are", "does", "do", "has", "have", "many",
                            "or", "than", "by", "to", "and", "which", "what", "how"})
_M_ELIGIBLE = corr._eligible_m                   # m's rule, captured at import (register entry (1))

#: p §1.2's sixteen renders of record, in item order.
RENDERS_OF_RECORD = (
    "Clopuie 31 + 46.",
    "Stane the number op days ig a week.",
    "Niye the third month of thj year.",
    "Conppte 60 divided bh 5.",
    "Srlie the number of sides of a triangle.",
    "Wrize tcg opposite of 'hot'.",
    "Cpmpuvn 14 times 2.",
    "State wsbch ix heavier: a kilogram of iron or half a kilogram of feathers.",
    "Name ttf first month oe the year.",
    "Cumkuta 90 minus 45.",
    "Smaje the number og wheels on a bicycle.",
    "Writk thn opposite ob 'up'.",
    "Cnmzote 11 + 33.",
    "Stkth the number oq hours in a day.",
    "Comkuva 8 times 8.",
    "Wzite thj opposite oj 'open'.",
)
RENDERS_SHA256_P = "1551c19997dc45419c496d7f64a61711735672f9388bab4be2e2c1a450f85722"
RENDERS_SHA256_M = "6baf494960da45896206f7eaadbc6b158642a42e09e1d11f70812959e3673c4c"
#: p §1.2's table: frame words, n_eligible under m and under p.
SPEC_FRAME = (("Compute",), ("State", "the", "of", "in", "a"), ("Name", "the", "of", "the"), ("Compute", "by"),
              ("State", "the", "of", "of", "a"), ("Write", "the", "of"), ("Compute",),
              ("State", "which", "is", "a", "of", "or", "a", "of"), ("Name", "the", "of", "the"), ("Compute",),
              ("State", "the", "of", "on", "a"), ("Write", "the", "of"), ("Compute",), ("State", "the", "of", "in", "a"),
              ("Compute",), ("Write", "the", "of"))
SPEC_N_M = (6, 19, 19, 13, 24, 14, 10, 45, 19, 10, 24, 14, 6, 19, 10, 14)
SPEC_N_P = (6, 8, 8, 7, 8, 7, 6, 12, 8, 6, 8, 7, 6, 8, 6, 7)
SPEC_K_SUM = 48
#: The renders' record and the seat's read of record (p §1.2-§1.3; ans2 §0), both committed; their sha256 pinned.
RENDERS_RAW_REL = "results/raw/2026-11-06_p_preread_renders.txt"
RENDERS_RAW_SHA256 = "25bd3d012a1c47867c45bb7cec4cfd30397104975dbc0456a8bcd210583eb895"
RENDERS_LINE = "json.dumps(renders): "
ANSWERS_REL = "results/raw/2026-11-07_p-preread_design-to-code_answers.md"
ANSWERS_SHA256 = "ab40f470b93a7eae58a9f1552eab17e166d6159c3f0bdac917627fc7385cb08b"
SEAT_READ_LINE = "16 of 16 instructions and golds recoverable"


def _is_letter(ch: str) -> bool:
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def frame_word_spans(text: str) -> list[tuple[int, int]]:
    """(start, end) of each frame word of ``text`` (p §1.1), in text order."""
    # PIN (Code, declared at the p BUILD): the quote rule is m's (each "'" toggles the span; an odd count is
    # refused, as corr._eligible_m refuses it); "its first word" is the text's first maximal letter run -- a frame
    # word unless it lies inside a quoted span, which no CORR item's does.
    if text.count("'") % 2:
        raise ValueError(f"unbalanced single quotes, operand span undefined: {text!r}")
    spans: list[tuple[int, int]] = []
    in_quote, first, i, n = False, True, 0, len(text)
    while i < n:
        if text[i] == "'":
            in_quote = not in_quote
            i += 1
            continue
        if _is_letter(text[i]):
            j = i
            while j < n and _is_letter(text[j]):
                j += 1
            if not in_quote and (first or text[i:j].lower() in FUNCTION_WORDS):
                spans.append((i, j))
            first, i = False, j
            continue
        i += 1
    return spans


def frame_words(text: str) -> list[str]:
    return [text[s:e] for s, e in frame_word_spans(text)]


def eligible_p(text: str) -> list[int]:
    """p §1.1's eligible positions: m:176's (``_M_ELIGIBLE``) that lie inside a frame word."""
    spans = frame_word_spans(text)
    return [pos for pos in _M_ELIGIBLE(text) if any(s <= pos < e for s, e in spans)]


def corrupt_p(text: str, i: int, rosters) -> tuple[str, dict]:
    """``corr.corrupt_m`` under register entry (1): (render, meta)."""
    with register.substituted(1, corr, {"_eligible_m": eligible_p}):
        return corr.corrupt_m(text, i, rosters)


def renders_p(pool: Sequence[dict] | None = None, rosters=None) -> list[str]:
    """The sixteen renders under ``corrupt_p``, roster-asserted as ``corr.renders_m`` asserts m's."""
    pool = corr.load_pool() if pool is None else pool
    rosters = corr.ROSTERS_OF_RECORD if rosters is None else rosters
    if len(pool) != corr.N_ITEMS:
        raise corr.CorrStop(f"RENDERS STOP: pool has {len(pool)} items, expected {corr.N_ITEMS}")
    out = [corrupt_p(it["task"], i, rosters)[0] for i, it in enumerate(pool)]
    words = corr._roster_words(rosters)
    bad = [(j, w) for j, r in enumerate(out) for w in words if w in r.lower()]
    if bad:
        raise corr.CorrStop(f"RENDERS STOP: roster substring in a render: {bad[:3]}")
    return out


def conditions_1_2(pool: Sequence[dict] | None = None, rosters=None) -> list[dict]:
    """m:176's structural conditions on p's renders, per item (p §3.2 (1)-(2)): (1) at least 3 changed positions,
    (2) k <= floor(n_eligible / 2); the walk is corrupt_p's own (register entry (1))."""
    pool = corr.load_pool() if pool is None else pool
    rosters = corr.ROSTERS_OF_RECORD if rosters is None else rosters
    out = []
    for i, it in enumerate(pool):
        _r, meta = corrupt_p(it["task"], i, rosters)
        n, k, ch = meta["n_eligible"], meta["k"], len(meta["changed_positions"])
        out.append({"i": i, "n_eligible": n, "k": k, "changed": ch, "skips": meta["n_skips"],
                    "c1_at_least_3_changed": ch >= 3, "c2_k_at_most_half": k <= n // 2})
    return out


def sha_p(renders: Sequence[str]) -> str:
    """p's convention (p §1.2): sha256 of ``json.dumps(renders)``."""
    return hashlib.sha256(json.dumps(list(renders)).encode()).hexdigest()


def sha_m(renders: Sequence[str]) -> str:
    """m's convention: sha256 of the newline-joined renders (``corr.renders_sha`` is its first 16 hex)."""
    return hashlib.sha256("\n".join(renders).encode()).hexdigest()


def renders_problems(renders: Sequence[str] | None = None) -> list[str]:
    """[] iff the renders are the record's: recomputed equal, both shas pinned, numpy's stream known answer clean."""
    probs = list(m_keys.stream_known_answer())
    try:
        got = list(renders_p()) if renders is None else list(renders)
    except (corr.CorrStop, ValueError) as e:
        return probs + [f"renders: {e}"]
    if got != list(RENDERS_OF_RECORD):
        probs.append("renders: not p §1.2's sixteen renders of record")
    if sha_p(got) != RENDERS_SHA256_P:
        probs.append(f"renders: p-convention sha256 {sha_p(got)[:16]} != {RENDERS_SHA256_P[:16]}")
    if sha_m(got) != RENDERS_SHA256_M or corr.renders_sha(got) != RENDERS_SHA256_M[:16]:
        probs.append(f"renders: m-convention sha256 {sha_m(got)[:16]} != {RENDERS_SHA256_M[:16]}")
    return probs


def _selftest(chk) -> None:
    pool = corr.load_pool()
    ros = corr.ROSTERS_OF_RECORD
    metas = [corrupt_p(it["task"], i, ros)[1] for i, it in enumerate(pool)]
    chk("corrupt: numpy's stream known answer is clean (every render rests on it)", m_keys.stream_known_answer() == [])
    chk("corrupt: each item's frame words are p §1.2's (first word + FUNCTION_WORDS, quotes excluded)",
        tuple(tuple(frame_words(it["task"])) for it in pool) == SPEC_FRAME,
        [i for i, it in enumerate(pool) if tuple(frame_words(it["task"])) != SPEC_FRAME[i]])
    chk("corrupt: n_eligible under m and under p are p §1.2's (m -> p)",
        tuple(len(_M_ELIGIBLE(it["task"])) for it in pool) == SPEC_N_M
        and tuple(m["n_eligible"] for m in metas) == SPEC_N_P, [m["n_eligible"] for m in metas])
    chk("corrupt: k = 3 on every item (the floor governs), k sums to 48, no roster skip",
        all(m["k"] == 3 for m in metas) and sum(m["k"] for m in metas) == SPEC_K_SUM
        and all(m["n_skips"] == 0 for m in metas))
    chk("corrupt: every changed position lies inside a frame word (and only there)",
        all(all(any(s <= p < e for s, e in frame_word_spans(it["task"])) for p in m["changed_positions"])
            for it, m in zip(pool, metas)))
    rp = renders_p()
    chk("corrupt: corrupt_p reproduces p §1.2's sixteen renders of record", rp == list(RENDERS_OF_RECORD),
        [i for i, (a, b) in enumerate(zip(rp, RENDERS_OF_RECORD)) if a != b])
    chk("corrupt: both identifications hold (p's 1551c19997dc4541, m's 6baf494960da4589)",
        sha_p(rp) == RENDERS_SHA256_P and sha_m(rp) == RENDERS_SHA256_M and renders_problems() == [],
        (sha_p(rp)[:16], sha_m(rp)[:16]))
    rm = corr.renders_m(pool, ros)
    chk("corrupt: equality with m where p must equal m -- items 0 and 12 are m's renders (term (c))",
        rp[0] == rm[0] and rp[12] == rm[12] and [i for i in range(16) if rp[i] == rm[i]] == [0, 12])
    chk("corrupt: corr._eligible_m is m's own after every call (restoration, term (c))", corr._eligible_m is _M_ELIGIBLE)
    try:
        corrupt_p("Writé the opposite.", 0, ros)          # corrupt_m refuses non-ASCII inside the window
        raised = False
    except ValueError:
        raised = True
    chk("corrupt: restoration holds after an exception inside the substitution (term (c))",
        raised and corr._eligible_m is _M_ELIGIBLE)
    chk("corrupt: m's renders are unchanged by p (corr.renders_m still gives m's sha a04f67b0e5105a05)",
        corr.renders_sha(corr.renders_m(pool, ros)) == "a04f67b0e5105a05")
    chk("corrupt: no roster word occurs in any render (both rosters, case-insensitive)",
        not any(w in r.lower() for r in rp for w in corr._roster_words(ros)))
