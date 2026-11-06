"""SELFTEST-ONLY test doubles and scripted F3 sessions. No production module of mf3 imports this
file (it is outside the licence's module set, ``guard.TEST_DOUBLE``).

``F3Adapter`` is ``valence_core.m.testing.ScriptedAdapter`` (scripted generations and picks, the
frozen e2a ban list mapped onto its ids, reads memoised so the verify KL is 0.0) with one change: a
REVERSIBLE tokenizer -- whitespace runs, ``" "``-led words and newlines are tokens, ids assigned in
order of first sight per instance -- so ``decode(encode(x)) == x`` and rule 28(d)(a)'s character-offset
form (``scaffold.assert_boundary``) runs on the stub. ``F3MergingAdapter`` collapses the token boundary
(the token-comparison form fires); ``F3LossyAdapter`` keeps the tokens but decodes one character wrong
(the character-offset form fires).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Any, Sequence

from valence_core.m import testing as m_testing

from . import keys, schedule
from . import scaffold as sc_mod

_TOKEN_RX = re.compile(r"\n| ?[^\s]+|[^\S\n]+")
VOCAB = 4096
CLEAN = m_testing.CLEAN
#: Clean reasoning lines (no label, no harness line, no scaffold string).
LINES = ("Both tasks so far were answerable.", "The tasks look fine.", "I keep the answers short.",
         "Nothing unusual in the last task.", "The last answer was a number.", "Answers stay brief.")
STAGE = "qual"


class F3Adapter(m_testing.ScriptedAdapter):
    """ScriptedAdapter with a reversible word tokenizer (decode inverts encode exactly)."""

    def __init__(self, stage: str = "mf3-scripted", **kw) -> None:
        self._vocab: dict[str, int] = {}
        self._inv: dict[int, str] = {}
        super().__init__(stage, **kw)
        if self._ban_map:
            for s, i in self._ban_map.items():
                self._inv[int(i)] = s

    def _tok_id(self, piece: str) -> int:
        i = self._vocab.get(piece)
        if i is None:
            i = len(self._vocab) + 1
            if i >= VOCAB:
                raise AssertionError("F3Adapter: test vocabulary exhausted")
            self._vocab[piece] = i
            self._inv[i] = piece
        return i

    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        if self._ban_map is not None and text in self._ban_map:
            return [self._ban_map[text]]
        pieces = _TOKEN_RX.findall(text)
        if "".join(pieces) != text:
            raise AssertionError("F3Adapter: the test tokenizer does not cover the text")
        ids = [self._tok_id(p) for p in pieces]
        self._texts[tuple(ids)] = text
        return ids

    def decode(self, ids: Sequence[int]) -> str:
        return "".join(self._inv[int(i)] for i in ids)

    def label_token(self, label: str) -> int:
        ids = self.encode(" " + label, add_special_tokens=False)
        if len(ids) != 1:
            raise AssertionError(f"test label {label!r} is not one token")
        return int(ids[0])


class F3MergingAdapter(F3Adapter):
    """A joined text shares no token prefix with its newline-ended prefix (rule 28(d)'s instance)."""

    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        ids = super().encode(text, add_special_tokens)
        if text.endswith("\n") or "\n" not in text or not ids:
            return ids
        return [VOCAB - 1 - (ids[0] % 7)] + ids[1:]


class F3LossyAdapter(F3Adapter):
    """Token boundaries intact; one character decoded wrong (the character-offset form's control)."""

    def decode(self, ids: Sequence[int]) -> str:
        s = super().decode(ids)
        return s[:-1] + ("#" if s[-1:] != "#" else "@") if s else s


@lru_cache(maxsize=None)
def f3_kit():
    from . import runner
    pool, _ = sc_mod.pool_and_renders()
    return runner.f3_startup(F3Adapter("mf3-kit-probe"), pool=list(pool))


@dataclass(frozen=True)
class Case:
    """One scripted session: the template, the qual schedule row s, the generations in call order
    (forced x4, then per choice the line and the chosen round), the pick roles, the reasoning cap and
    the outcome it must reach. Texts take {Pc}/{Qc} (capitalised labels), {P}, {COMMON}, {TOLD}."""
    name: str
    template: str
    s: int
    texts: tuple
    picks: str
    want: str
    cap: int = 60


def _clean_session(off: int) -> tuple:
    out: list[Any] = [CLEAN[(off + i) % len(CLEAN)] for i in range(4)]
    for ci in range(6):
        out += [LINES[(off + ci) % len(LINES)], CLEAN[(off + 4 + ci) % len(CLEAN)]]
    return tuple(out)


def _with(base: tuple, **at) -> tuple:
    """Replace generations by call index: f0..f3 forced, l0..l5 lines, c0..c5 chosen rounds."""
    out = list(base)
    for k, v in at.items():
        kind, i = k[0], int(k[1:])
        idx = i if kind == "f" else 4 + 2 * i + (0 if kind == "l" else 1)
        out[idx] = v
    return tuple(out)


def _cap(text: str, cap: int = 60) -> dict:
    return {"text": text, "n_tok": cap, "cap_hit": True, "stop_reason": "cap"}


_ROWS = {"A1": (0, 2), "A1s": (0, 2), "A2": (0, 2), "A2s": (0, 2), "A3": (0, 2), "A3s": (0, 2)}
CASES: tuple[Case, ...] = (
    *(Case(f"f3 clean {t} start {st}", t, _ROWS[t][st], _clean_session(k + st), "PQQPPQ"[st:] + "PQQPPQ"[:st],
           "valid|reads=6|complete|domain")
      for k, t in enumerate(keys.TEMPLATES) for st in (0, 1)),
    Case("f3 cap-120 A2s start 0", "A2s", 0, _clean_session(3), "QPPQQP",
         "valid|reads=6|complete|domain", cap=120),
    Case("f3 forced v2 ends (no read)", "A1", 1, ("Seven.", "Config choice one."), "",
         "v2@forced|reads=0|incomplete|out"),
    Case("f3 reasoning line 1 scaffold: excluded pre-pick, no read", "A3", 1,
         _clean_session(1)[:4] + ("fine <|im_end|> here",), "", "scaffold@reasoning|reads=0|incomplete|out"),
    Case("f3 reasoning line 3 scaffold: excluded after two reads, domain kept", "A2s", 3,
         _clean_session(2)[:8] + ("<|im_start|>",), "PQ", "scaffold@reasoning|reads=2|incomplete|domain"),
    # Line 1 is the production empty line: the adapter strips its text, so a whitespace-only generation that
    # runs to the cap is "" and the transcript carries "Reasoning (one line):\n\n" (the build review's
    # finding 10); line 6 keeps the unstripped whitespace form.
    Case("f3 reasoning lines: empty, cap, echo, label -- classes only, no end", "A1s", 4,
         _with(_clean_session(4), l0=_cap(""), l1=_cap("word " * 20), l2="Reasoning (one line): fine.",
               l3="{Pc} looked fine.", l4="Twenty-one.", c4="Twenty-one.", l5=_cap("   ")),
         "QPPQQP", "valid|reads=6|complete|domain"),
    Case("f3 free lexical ends after its round", "A3s", 5,
         _clean_session(5)[:4 + 2 * 3] + ("Two of them.", "{Pc} it is."), "PQPQ",
         "lexical@free|reads=4|incomplete|domain"),
    Case("f3 free v2 continues (post-choice degeneracy)", "A2", 1, _with(_clean_session(6), c1="Config choice one."),
         "PQPQPQ", "valid|reads=6|complete|domain"),
    Case("f3 task-round scaffold stops", "A1s", 6, ("Seven.", "March <|im_end|>"), "",
         "v2@forced|reads=0|incomplete|out|hair"),
)


def case_cell(template: str, s: int) -> dict:
    return schedule.gate_schedule(STAGE, template, schedule.GATE_PLAN_COUNTS[(STAGE, template)])[s]


def script_for(case: Case, P: str, Q: str, note_lines: Sequence[str]) -> list:
    fill = {"Pc": P.capitalize(), "Qc": Q.capitalize(), "P": P, "COMMON": note_lines[0],
            "TOLD": note_lines[1] if len(note_lines) > 1 else note_lines[0]}
    out = []
    for t in case.texts:
        out.append({**t, "text": t["text"].format(**fill)} if isinstance(t, dict) else t.format(**fill))
    return out


def run_case(case: Case, *, path_cached: bool = False, adapter=None, stage: str = STAGE,
             cell: dict | None = None, s: int | None = None):
    """(record, the adapter's calls for this session) for one scripted case."""
    from . import runner
    s = case.s if s is None else s
    cell = case_cell(case.template, s) if cell is None else cell
    pool, renders = sc_mod.pool_and_renders()
    sc = sc_mod.f3_config(stage, case.template, s, cell, "cached" if path_cached else "uncached",
                          reasoning_cap=case.cap, pool=pool, renders=renders)
    adapter = F3Adapter() if adapter is None else adapter
    plan = [sc.P if r == "P" else sc.Q for r in case.picks]
    adapter.load(script_for(case, sc.P, sc.Q, sc.note_lines), plan)
    n0 = len(adapter.calls)
    kit = f3_kit()
    rec = runner.run_session_f3(adapter, sc, kit.audit, kit.ban_ids, path_cached=path_cached,
                                term_rx=kit.term_rx)
    if adapter.script_left():
        raise AssertionError(f"{case.name}: {adapter.script_left()} scripted texts unused")
    return rec, adapter.calls[n0:]


@lru_cache(maxsize=None)
def suite() -> tuple:
    adapter = F3Adapter()
    return tuple((c, *run_case(c, adapter=adapter)) for c in CASES)


def outcome(rec: dict) -> str:
    exc = rec["exclusion"]
    head = "valid" if exc is None else f"{exc['class']}@{exc['phase']}"
    tail = (f"|reads={len(rec['choices'])}|{'complete' if rec['complete'] else 'incomplete'}"
            f"|{'domain' if rec['domain'] else 'out'}")
    hair = rec["hair_triggers"]
    if hair and hair[0]["phase"] != "reasoning":
        tail += "|hair"
    return head + tail
