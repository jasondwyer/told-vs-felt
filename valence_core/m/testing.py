"""PROPOSAL-m test doubles (build design §3; v1.11 §3.1 G-VER m:284, §8 step 4).

SELFTEST-ONLY. No production module of the m package imports this file at module
level; the runners, the scaffold and the verifier import it inside their own
``_selftest`` functions only. It loads ``scripts/box_selftest_stub.py`` (a script,
not a package module) by a ``sys.path`` insert that is undone at once.

``ScriptedAdapter`` is ``box_selftest_stub.SelfTestAdapter`` (word-hash tokenizer,
the REAL ``readout.choice_read`` path, ``choice_window = 8192``) with:

  * ``generate`` returning the texts of a per-session script, in call order, and
    recording every call's ``prefix``, ``segment``, ``seed``, ``cached`` and
    ``injections`` (``calls``); with no script loaded it delegates to the stub
    and strips the text, as both real adapters do (qwen_mlx.py:343,
    olmo_hf.py:286);
  * ``forward`` adding a fixed bias to one planned label's logit, so a selftest
    drives picks deterministically through the frozen read itself. The plan is
    consumed once per DISTINCT read context (memoised by token ids), so the
    read's verify re-forward sees identical logits and its KL is exactly 0.0;
  * an ``encode`` that is the stub's (prefix-stable on every m join shape: each
    generation prefix ends in "\\n", which the word tokenizer never merges), except
    that a text that IS one of the frozen e2a ban-list strings encodes to one id of
    that file (``QWEN_BAN_MAP``) and ``special_token_strings`` are the file's twelve,
    so ``session.build_ban_list(adapter)`` rebuilds the frozen list exactly (the
    real Qwen tokenizer does, maps/e2a.md [tok]) and ``runner_qwen.qwen_ban_list``'s
    live-rebuild comparison passes on the stub and fires on a stub whose map differs;
  * a pick-plan entry ``LOW_MASS + label`` that wins the read for ``label`` while
    a non-label decoy token takes the top-1 and nearly all the mass (label mass
    far below e2d's .20): the low_label_mass / top1_not_label fields' must-fire read.

``OLMoScriptedAdapter`` declares ``<|endoftext|>`` and ``<|pad|>`` as special
tokens, so ``session.build_ban_list`` returns OLMo's six strings exactly
(data/olmo/scaffold_{ckpt}.json); the stub's word tokenizer encodes each string
as ONE id, so its six ids can never match b3's nine-id sha16 ``2dd86a453a2275ef``
and ``audit.assert_olmo_scaffold`` refuses them (the real accept path runs on the
box with the OLMo tokenizer; maps/olmo.md §4.1).

The scenario helpers at the bottom (``qwen_kit``, ``olmo_kit``, ``CASES_*``,
``run_case``, ``suite``) build gate-stage sessions from the committed-schedule
construction and are shared by the runner and verifier selftests.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Sequence

import numpy as np

from ..adapters.base import ForwardResult, GenerateResult

REPO = Path(__file__).resolve().parents[2]
PICK_BIAS = 60.0               # logit bias on a planned label; dwarfs the stub's ~N(0, 2) logits
LOW_MASS = "~"                 # pick-plan prefix: the label wins, a decoy takes the mass
LOW_MASS_LABEL_BIAS = 30.0     # the label's bias under LOW_MASS (beats the other label)
LOW_MASS_DECOY = "zz-decoy-token"
OLMO_EXTRA_SPECIALS = ("<|endoftext|>", "<|pad|>")


def _qwen_ban_map() -> dict[str, int]:
    """The frozen e2a ban list's twelve strings onto its twelve ids (sorted onto sorted:
    build_ban_list returns both sorted, so any bijection reproduces the file; this is a
    stub map, not the Qwen tokenizer's own pairing)."""
    import json
    cfg = json.loads((REPO / "data" / "configs" / "e2a_ban_list.json").read_text())
    strings, ids = sorted(cfg["strings"]), sorted(int(i) for i in cfg["ids"])
    if len(strings) != len(ids) or len(set(ids)) != len(ids):
        raise AssertionError("e2a ban list: strings and ids do not pair one to one")
    return dict(zip(strings, ids))


QWEN_BAN_MAP = _qwen_ban_map()


def _load_stub():
    saved = list(sys.path)
    try:
        for p in (str(REPO), str(REPO / "scripts")):
            if p not in sys.path:
                sys.path.insert(0, p)
        import box_selftest_stub as stub
        return stub
    finally:
        sys.path[:] = saved


_stub = _load_stub()
SelfTestAdapter = _stub.SelfTestAdapter
STUB_TAG = _stub.STUB_TAG


class ScriptExhausted(AssertionError):
    """A scripted session asked for more generations than its script holds."""


class ScriptedAdapter(SelfTestAdapter):
    """SelfTestAdapter with scripted generations and scripted picks."""

    def __init__(self, stage: str = "m-scripted", *,
                 special_strings: Sequence[str] | None = None,
                 ban_map: dict[str, int] | None = QWEN_BAN_MAP) -> None:
        super().__init__(stage)
        self.calls: list[dict] = []
        self.read_texts: list[str | None] = []
        self._texts: dict[tuple, str] = {}
        self._ban_map = None if ban_map is None else dict(ban_map)
        if special_strings is None and self._ban_map is not None:
            special_strings = sorted(self._ban_map)
        self._special = None if special_strings is None else list(special_strings)
        self.load()

    # --- scripting ---------------------------------------------------------
    def load(self, texts: Sequence[Any] | Callable[[dict], Any] | None = None,
             picks: Sequence[str] | Callable[[str | None], str | None] | None = None) -> None:
        """Arm one session: generations in call order, picks per distinct read."""
        self._script = texts if (texts is None or callable(texts)) else list(texts)
        self._script_pos = 0
        self._picks = picks if (picks is None or callable(picks)) else list(picks)
        self._pick_pos = 0
        self._pick_memo: dict[tuple, str | None] = {}

    def script_left(self) -> int:
        if self._script is None or callable(self._script):
            return 0
        return len(self._script) - self._script_pos

    def _next_script(self, call: dict) -> dict | None:
        if self._script is None:
            return None
        if callable(self._script):
            spec = self._script(call)
        else:
            if self._script_pos >= len(self._script):
                raise ScriptExhausted(f"script exhausted at generate call {call['index']}")
            spec = self._script[self._script_pos]
            self._script_pos += 1
        if spec is None:
            return None
        if isinstance(spec, str):
            spec = {"text": spec}
        return dict(spec)

    def _planned_pick(self, key: tuple) -> str | None:
        if key in self._pick_memo:
            return self._pick_memo[key]
        text = self._texts.get(key)
        if self._picks is None:
            label = None
        elif callable(self._picks):
            label = self._picks(text)
        elif self._pick_pos < len(self._picks):
            label = self._picks[self._pick_pos]
            self._pick_pos += 1
        else:
            raise ScriptExhausted("pick plan exhausted")
        self._pick_memo[key] = label
        self.read_texts.append(text)
        return label

    # --- adapter surface -----------------------------------------------------
    @property
    def special_token_strings(self) -> list[str]:
        return list(self._special) if self._special is not None else super().special_token_strings

    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        if self._ban_map is not None and text in self._ban_map:
            return [self._ban_map[text]]          # a scaffold string is one special id
        ids = super().encode(text, add_special_tokens)
        self._texts[tuple(ids)] = text
        return ids

    def label_token(self, label: str) -> int:
        ids = super().encode(" " + label, add_special_tokens=False)
        if len(ids) != 1:
            raise AssertionError(f"stub label {label!r} is not one token")
        return int(ids[0])

    def forward(self, ids, capture_layers=(), injections=()):
        if tuple(injections):
            raise AssertionError("ScriptedAdapter: an m read never carries an injection")
        fr = super().forward(ids, capture_layers)
        label = self._planned_pick(tuple(int(i) for i in ids))
        if label is None:
            return fr
        logits = np.array(fr.logits, dtype=np.float32, copy=True)
        if label.startswith(LOW_MASS):
            lab = self.label_token(label[len(LOW_MASS):])
            decoy = self.label_token(LOW_MASS_DECOY)
            if decoy == lab:
                raise AssertionError("the low-mass decoy shares the label's token id")
            logits[lab] += np.float32(LOW_MASS_LABEL_BIAS)
            logits[decoy] += np.float32(PICK_BIAS)
        else:
            logits[self.label_token(label)] += np.float32(PICK_BIAS)
        return ForwardResult(logits=logits, acts=fr.acts, n_positions=fr.n_positions)

    def generate(self, prefix_text: str, segment_text: str, injections=(), *,
                 seed: int | None = None, temp: float = 0.0, max_tokens: int = 60,
                 stop_newline: bool = True, ban_ids=(), cached: bool = False) -> GenerateResult:
        call = {"index": len(self.calls), "prefix": prefix_text, "segment": segment_text,
                "injections": tuple(injections), "seed": seed, "temp": temp,
                "max_tokens": max_tokens, "stop_newline": stop_newline,
                "ban_ids": tuple(ban_ids), "cached": cached}
        self.calls.append(call)
        spec = self._next_script(call)
        if spec is None:
            g = super().generate(prefix_text, segment_text, injections=injections, seed=seed,
                                 temp=temp, max_tokens=max_tokens, stop_newline=stop_newline,
                                 ban_ids=ban_ids, cached=cached)
            text = g.text.strip()
            return GenerateResult(text=text, token_ids=super().encode(text, add_special_tokens=False),
                                  first_logits=g.first_logits, cap_hit=g.cap_hit,
                                  stop_reason=g.stop_reason)
        text = spec["text"]
        toks = super().encode(text, add_special_tokens=False)
        n_tok = int(spec.get("n_tok", len(toks)))
        return GenerateResult(text=text, token_ids=list(toks)[:n_tok] + [0] * max(0, n_tok - len(toks)),
                              first_logits=np.zeros(8, dtype=np.float32),
                              cap_hit=bool(spec.get("cap_hit", False)),
                              stop_reason=str(spec.get("stop_reason", "newline")))


class OLMoScriptedAdapter(ScriptedAdapter):
    """ScriptedAdapter whose build_ban_list strings are OLMo's six (ids cannot match b3's)."""

    def __init__(self, stage: str = "m-scripted-olmo") -> None:
        super().__init__(stage, special_strings=OLMO_EXTRA_SPECIALS, ban_map=None)


class MergingAdapter(ScriptedAdapter):
    """A tokenizer under which a joined text shares no token prefix with its newline-
    ended prefix: the boundary collapses to 0, rule 28(d)'s instance (testing only)."""

    def encode(self, text: str, add_special_tokens: bool = True) -> list[int]:
        ids = super().encode(text, add_special_tokens)
        if text.endswith("\n") or not ids:
            return ids
        return [(ids[0] * 7 + 1) % 4096] + ids[1:]


# --- scenario helpers (shared by the runner and verifier selftests) ----------------
@lru_cache(maxsize=None)
def pool_and_renders() -> tuple[tuple[dict, ...], tuple[str, ...]]:
    from . import corr
    pool = corr.load_pool()
    return tuple(pool), tuple(corr.renders_m(pool, corr.ROSTERS_OF_RECORD))


@lru_cache(maxsize=None)
def qwen_kit():
    from . import runner_qwen
    pool, _ = pool_and_renders()
    return runner_qwen.qwen_startup(ScriptedAdapter("m-kit-probe"), pool=list(pool))


@lru_cache(maxsize=None)
def olmo_kit():
    from . import audit, scaffold
    from ..session import build_ban_list
    ids, strings = build_ban_list(OLMoScriptedAdapter("m-kit-probe"))
    return {"audit": audit.OLMoTaskRoundAudit(), "ban_ids": tuple(ids), "ban_strings": tuple(strings),
            "term_rx": scaffold.load_term_rx()}


#: Clean answers (no roster word, no frame fragment, no content class).
CLEAN = ("Seventy-seven.", "Seven.", "March.", "Twelve.", "Three.", "Cold.", "Twenty-eight.",
         "Iron.", "January.", "Forty-five.", "Two.", "Down.")


@dataclass(frozen=True)
class Case:
    """One scripted session. ``texts``: per generate call, formatted with Pc/Qc
    (capitalised labels), TOLD and COMMON, and TOLD_np / COMMON_np (the line without
    its final period, as OLMo's newline stop stores a copied line: the fused ".\\n"
    token is the stop and is dropped, finding 5 -- an OLMo echo; on Qwen, whose stop
    never takes the period, not an echo, finding N6); ``picks``: roles per read ("P"/"Q";
    lower-case "p"/"q" = that role's label at low label mass, ``LOW_MASS``);
    ``want``: expected outcome fields."""

    name: str
    contrast: bool
    s: int
    texts: tuple[str, ...]
    picks: str = ""
    want: dict = field(default_factory=dict)


def _clean(n: int, off: int = 0) -> tuple[str, ...]:
    return tuple(CLEAN[(off + i) % len(CLEAN)] for i in range(n))


def _w(**kw) -> dict:
    base = {"excluded": None, "n_forced": 4, "n_free": 6, "hair": None, "complete": True,
            "domain": True}
    base.update(kw)
    return base


CASES_QWEN: tuple[Case, ...] = (
    # clean sessions: both templates x the four (start, clause) combinations of rows 0-3
    *(Case(f"qwen clean {'A0' if c else 'A0s'} s{s}", c, s, _clean(10, s), "PQPPQQ"[s:] + "PQPPQQ"[:s],
           _w()) for c in (True, False) for s in range(4)),
    Case("qwen forced v2 ends (no read)", True, 4, ("Seven.", "Config choice one."), "",
         _w(excluded=("v2", "forced"), n_forced=2, n_free=0, complete=False, domain=False)),
    Case("qwen forced echo of the TOLD line ends", False, 4, ("Seven.", "March.", "{TOLD}"), "",
         _w(excluded=("echo", "forced"), n_forced=3, n_free=0, complete=False, domain=False)),
    Case("qwen forced content claim ends", True, 5, ("* * *",), "",
         _w(excluded=("content", "forced"), n_forced=1, n_free=0, complete=False, domain=False)),
    Case("qwen forced lexical ends", False, 5, _clean(3) + ("{Qc} is the answer.",), "",
         _w(excluded=("lexical", "forced"), n_forced=4, n_free=0, complete=False, domain=False)),
    Case("qwen free v2/echo(TOLD)/content claims end nothing (contrast)", True, 6,
         _clean(4) + ("Config choice one.", "{TOLD}", "* * *", "Two.", "Down.", "Iron."), "PQQPPQ",
         _w()),
    Case("qwen free v2/echo(COMMON)/content claims end nothing (sham)", False, 6,
         _clean(4) + ("* * *", "Config choice one.", "{COMMON}", "Two.", "Down.", "Iron."), "QPPQQP",
         _w()),
    Case("qwen free lexical ends after its round (contrast)", True, 7,
         _clean(4) + ("Two.", "Down.", "Iron.", "{Pc} it is."), "PQPP",
         _w(excluded=("lexical", "free"), n_free=4, complete=False)),
    Case("qwen free lexical at the last round (sham)", False, 7,
         _clean(4) + ("Two.", "Down.", "Iron.", "Cold.", "Seven.", "{Qc}."), "QQPPQP",
         _w(excluded=("lexical", "free"), n_free=6, complete=True)),
    Case("qwen forced scaffold string: v2 exclusion + hair trigger, stop", False, 8,
         ("Seven.", "March.", "<|im_end|>"), "",
         _w(excluded=("v2", "forced"), n_forced=3, n_free=0, hair="forced", complete=False,
            domain=False)),
    Case("qwen free scaffold string: hair trigger stops, no exclusion", False, 9,
         _clean(4) + ("Two.", "<|im_end|>"), "PQ",
         _w(n_free=2, hair="free", complete=False)),
    # finding N6: on Qwen a Note line without its final period is NOT an echo (m:261's
    # "complete" line; the period-less form is OLMo's only); it falls to m:261's later
    # classes -- a TOLD copy names the own pair (lexical), a bare COMMON copy is unclaimed
    Case("qwen forced TOLD line without its final period: lexical (not echo) ends", False, 10,
         ("Seven.", "{TOLD_np}"), "",
         _w(excluded=("lexical", "forced"), n_forced=2, n_free=0, complete=False, domain=False)),
    Case("qwen forced COMMON without its final period: no class, the session runs on", False, 11,
         ("{COMMON_np}",) + _clean(9, 2), "QPQPPQ", _w()),
    Case("qwen free COMMON without its final period: no class; free TOLD without it: lexical ends",
         False, 12, _clean(4) + ("{COMMON_np}", "Two.", "{TOLD_np}"), "PQQ",
         _w(excluded=("lexical", "free"), n_free=3, complete=False)),
    # finding 33 / N16: the runner feeds every task-round response, forced and free,
    # into audit v3's `earlier`
    Case("qwen forced round 3 repeats round 1: content (stuck_attractor) ends", False, 13,
         ("Seven.", "March.", "Seven."), "",
         _w(excluded=("content", "forced"), n_forced=3, n_free=0, complete=False, domain=False)),
    Case("qwen free round repeats a forced answer: content claim, no end", False, 14,
         ("Seven.", "March.", "Twelve.", "Three.", "Two.", "March.", "Down.", "Iron.", "Cold.",
          "Forty-five."), "QPPQQP", _w()),
    Case("qwen free round repeats an earlier FREE answer: content claim, no end", False, 15,
         _clean(4) + ("Two.", "Down.", "Two.", "Iron.", "Cold.", "Forty-five."), "PQPQQP", _w()),
)

CASES_OLMO: tuple[Case, ...] = (
    *(Case(f"olmo clean {'A0' if c else 'A0s'} s{s}", c, s, _clean(10, s + 3), "QPPQPQ"[s:] + "QPPQPQ"[:s],
           _w()) for c in (True, False) for s in range(4)),
    Case("olmo forced AuditSpec claim ends", True, 4, ("Seven.", "Config choice one."), "",
         _w(excluded=("audit", "forced"), n_forced=2, n_free=0, complete=False, domain=False)),
    Case("olmo forced echo of the TOLD line ends", False, 4, ("{TOLD}",), "",
         _w(excluded=("echo", "forced"), n_forced=1, n_free=0, complete=False, domain=False)),
    Case("olmo forced lexical ends", True, 5, _clean(2) + ("{Pc}.",), "",
         _w(excluded=("lexical", "forced"), n_forced=3, n_free=0, complete=False, domain=False)),
    Case("olmo '* * *' is no OLMo class (session continues)", False, 5,
         ("Seven.", "* * *") + _clean(8, 2), "PPQQPQ", _w()),
    Case("olmo free echo ends", True, 6, _clean(4) + ("Two.", "Down.", "{COMMON}"), "PQP",
         _w(excluded=("echo", "free"), n_free=3, complete=False)),
    Case("olmo free AuditSpec claim ends", False, 6, _clean(4) + ("Config choice one.",), "Q",
         _w(excluded=("audit", "free"), n_free=1, complete=False)),
    Case("olmo free lexical ends", True, 7, _clean(4) + ("Two.", "Down.", "Iron.", "Cold.", "{Qc}."),
         "PQQPQ", _w(excluded=("lexical", "free"), n_free=5, complete=False)),
    Case("olmo forced <|pad|>: hair trigger, no claim, stop", False, 7, ("Seven.", "<|pad|>"), "",
         _w(n_forced=2, n_free=0, hair="forced", complete=False, domain=False)),
    Case("olmo free <think>: AuditSpec claim + hair trigger, stop", False, 8,
         _clean(4) + ("Two.", "Down.", "Iron.", "<think>"), "PQPQ",
         _w(excluded=("audit", "free"), n_free=4, hair="free", complete=False)),
    # finding 5: OLMo's newline stop drops the fused ".\n" token, so a copied line is
    # stored without its final period; it is still an echo and still ends the session
    Case("olmo forced echo of the TOLD line without its final period ends", False, 9,
         ("Seven.", "March.", "{TOLD_np}"), "",
         _w(excluded=("echo", "forced"), n_forced=3, n_free=0, complete=False, domain=False)),
    Case("olmo forced echo of COMMON without its final period ends", False, 10,
         ("{COMMON_np}",), "",
         _w(excluded=("echo", "forced"), n_forced=1, n_free=0, complete=False, domain=False)),
    Case("olmo free echo of the TOLD line without its final period ends", False, 11,
         _clean(4) + ("Two.", "{TOLD_np}"), "QP",
         _w(excluded=("echo", "free"), n_free=2, complete=False)),
    Case("olmo free echo of COMMON without its final period ends", False, 12,
         _clean(4) + ("{COMMON_np}",), "P",
         _w(excluded=("echo", "free"), n_free=1, complete=False)),
)

QWEN_UNIT, OLMO_UNIT = "Q-F0", "OLMo-sft"
STAGE = "qual"


def case_template(substrate: str, contrast: bool) -> str:
    from . import keys
    return keys.templates(QWEN_UNIT if substrate == "qwen" else OLMO_UNIT)[0 if contrast else 1]


def case_cell(substrate: str, template: str, s: int) -> dict:
    from . import schedule
    unit = QWEN_UNIT if substrate == "qwen" else OLMO_UNIT
    return schedule.gate_schedule(unit, STAGE, template, schedule.roster_for(unit), 16)[s]


def _no_final_period(line: str) -> str:
    if not line.endswith("."):
        raise AssertionError(f"a Note line ends in '.': {line!r}")
    return line[:-1]


def script_for(case: Case, P: str, Q: str, note_lines: Sequence[str]) -> list[str]:
    fill = {"Pc": P.capitalize(), "Qc": Q.capitalize(), "COMMON": note_lines[0], "TOLD": note_lines[1],
            "COMMON_np": _no_final_period(note_lines[0]), "TOLD_np": _no_final_period(note_lines[1])}
    return [t.format(**fill) for t in case.texts]


def plan_picks(roles: str, P: str, Q: str) -> tuple[list[str], list[str]]:
    """(the adapter's pick plan, the labels the reads must return) for a roles string."""
    plan, want = [], []
    for r in roles:
        if r not in "PQpq":
            raise ValueError(f"pick role must be one of P, Q, p, q: {r!r}")
        label = P if r in "Pp" else Q
        plan.append(label if r.isupper() else LOW_MASS + label)
        want.append(label)
    return plan, want


def run_case(case: Case, substrate: str, *, path_cached: bool = False, adapter=None):
    """(record, the adapter's calls for this session) for one scripted case."""
    from . import runner_olmo, runner_qwen, scaffold
    template = case_template(substrate, case.contrast)
    unit = QWEN_UNIT if substrate == "qwen" else OLMO_UNIT
    cell = case_cell(substrate, template, case.s)
    pool, renders = pool_and_renders()
    path = "cached" if path_cached else "uncached"
    sc = scaffold.m_config(unit, STAGE, template, case.s, cell, path,
                           pool=list(pool), renders=list(renders))
    if adapter is None:
        adapter = ScriptedAdapter() if substrate == "qwen" else OLMoScriptedAdapter()
    plan, picks = plan_picks(case.picks, sc.P, sc.Q)
    adapter.load(script_for(case, sc.P, sc.Q, sc.note_lines), plan)
    n0 = len(adapter.calls)
    if substrate == "qwen":
        kit = qwen_kit()
        rec = runner_qwen.run_session_qwen(adapter, sc, kit.audit, kit.ban_ids,
                                           path_cached=path_cached, term_rx=kit.term_rx)
    else:
        kit = olmo_kit()
        rec = runner_olmo.run_session_olmo(adapter, sc, kit["audit"], kit["ban_ids"],
                                           term_rx=kit["term_rx"])
    if adapter.script_left():
        raise AssertionError(f"{case.name}: {adapter.script_left()} scripted texts unused")
    return rec, adapter.calls[n0:], picks


@lru_cache(maxsize=None)
def suite(substrate: str) -> tuple:
    """Every case of a substrate run once: ((case, record, calls, picks), ...)."""
    cases = CASES_QWEN if substrate == "qwen" else CASES_OLMO
    adapter = ScriptedAdapter() if substrate == "qwen" else OLMoScriptedAdapter()
    out = []
    for c in cases:
        rec, calls, picks = run_case(c, substrate, adapter=adapter)
        out.append((c, rec, tuple(calls), tuple(picks)))
    return tuple(out)


def outcome(rec: dict) -> dict:
    """The fields a Case's ``want`` names, read off a record."""
    exc = rec["exclusion"]
    hair = rec["hair_triggers"]
    return {"excluded": None if exc is None else (exc["class"], exc["phase"]),
            "n_forced": sum(r["phase"] == "forced" for r in rec["rounds"]),
            "n_free": sum(r["phase"] == "free" for r in rec["rounds"]),
            "hair": hair[0]["phase"] if hair else None, "complete": rec["complete"],
            "domain": rec["domain"]}


# --- self-test -------------------------------------------------------------------
def _selftest(chk) -> None:
    import json

    from ..readout import choice_read
    from ..session import DEFAULT_SCAFFOLD_STRINGS as DEFAULT_SCAFFOLD
    from ..session import build_ban_list
    from . import audit, guard

    a = ScriptedAdapter()
    chk("testing: ScriptedAdapter is a SelfTestAdapter with the declared 8192 window",
        isinstance(a, SelfTestAdapter) and a.choice_window == 8192
        and a.provenance()["adapter"] == STUB_TAG)
    pre = "=== Config evaluation session ===\nNote: x y.\n[round 1 | config: prism]\nTask: T.\nResponse:Seven.\n"
    seg = "[round 2 — active config: slate]\nTask: U.\nResponse:"
    e1, e2 = a.encode(pre), a.encode(pre + seg)
    chk("testing: encode is prefix-stable across a newline-ended prefix (and not trivially)",
        e2[:len(e1)] == e1 and len(e2) > len(e1), (len(e1), len(e2)))
    a.load(["One.", {"text": "Two.", "cap_hit": True, "stop_reason": "cap"}])
    g1 = a.generate("p\n", "s", injections=(), seed=11, temp=0.7, cached=False)
    g2 = a.generate("p\nq\n", "s2", injections=(), seed=12, temp=0.7, cached=False)
    chk("testing: generate returns the script in call order with its cap/stop fields",
        (g1.text, g2.text, g1.cap_hit, g2.cap_hit, g2.stop_reason) == ("One.", "Two.", False, True, "cap"))
    chk("testing: every call's prefix/segment/seed/cached/injections is recorded",
        [(c["prefix"], c["segment"], c["seed"], c["cached"], c["injections"]) for c in a.calls[-2:]]
        == [("p\n", "s", 11, False, ()), ("p\nq\n", "s2", 12, False, ())])
    try:
        a.generate("p\n", "s", injections=(), seed=1, cached=False)
        ok = False
    except ScriptExhausted:
        ok = True
    chk("testing: an exhausted script raises (a session never silently falls back)", ok)
    a.load(None)
    g3 = a.generate("p\n", "s", injections=(), seed=5, cached=False)
    chk("testing: with no script, generate delegates to the stub and strips its text",
        g3.text == g3.text.strip() and len(g3.text.split()) >= 4, g3.text)
    labels = ("prism", "slate")
    lids = guard.label_ids(a, labels)
    text = pre + "[round 5 | choice]\nAvailable configs: prism, slate\nConfig choice (one word):"
    reads = {}
    for want in labels:
        a.load(None, [want])
        reads[want] = choice_read(a, text, "prism", "slate", lids, verify=True)
    chk("testing: a pick plan drives the REAL choice_read both ways, verify KL exactly 0.0",
        all(reads[w].pick == w and reads[w].verify_kl == 0.0 and reads[w].top1_is_label for w in labels),
        {w: (r.pick, r.verify_kl) for w, r in reads.items()})
    a.load(None, None)
    r0 = choice_read(a, text, "prism", "slate", lids, verify=True)
    r1 = choice_read(a, text, "prism", "slate", lids, verify=True)
    chk("testing: unplanned reads run the stub's own logits, reproducibly",
        r0.verify_kl == 0.0 and r0.as_dict() == r1.as_dict() and r0.pick in labels)
    a.load(None, ["slate"])
    ra = choice_read(a, text, "prism", "slate", lids, verify=True)
    rb = choice_read(a, text, "prism", "slate", lids, verify=True)   # same context: memoised
    chk("testing: the plan is consumed once per distinct read context (verify re-forward agrees)",
        ra.pick == rb.pick == "slate" and a._pick_pos == 1)
    # (forward's refusal of a non-empty injections argument is not exercised here: any such
    # call is itself flagged by guard.check_call_sites, which scans this file too.)
    o = OLMoScriptedAdapter()
    ids, strings = build_ban_list(o)
    with open(REPO / "data" / "olmo" / "scaffold_sft.json") as f:
        file_strings = sorted(json.load(f)["ban_strings"])
    chk("testing: OLMo variant's build_ban_list yields OLMo's six strings (scaffold_sft.json)",
        strings == file_strings == sorted(audit.OLMO_SCAFFOLD_STRINGS), strings)
    try:
        audit.assert_olmo_scaffold(ids, strings, "sft")
        ok = False
    except SystemExit:
        ok = True
    chk("testing: the stub's six ids cannot match b3's nine-id sha16 (assert_olmo_scaffold refuses)",
        ok and len(ids) == 6, len(ids))
    # the Qwen ban map (finding 6's must-not-fire stub) and its must-fire variants
    with open(REPO / "data" / "configs" / "e2a_ban_list.json") as f:
        frozen = json.load(f)
    qa = ScriptedAdapter()
    qids, qstrings = build_ban_list(qa)
    moved = dict(QWEN_BAN_MAP)
    moved["<|im_end|>"] = 11
    mids, _ = build_ban_list(ScriptedAdapter(ban_map=moved))
    pids, pstrings = build_ban_list(ScriptedAdapter(ban_map=None))
    chk("testing: ScriptedAdapter's live build_ban_list reproduces the frozen e2a file (12 strings -> "
        "12 ids); a moved id or the plain stub tokenizer does not; OLMo's variant keeps the stub map",
        (qids, qstrings) == (sorted(frozen["ids"]), sorted(frozen["strings"]))
        and mids != qids and pstrings == sorted(set(DEFAULT_SCAFFOLD) | {"<|stub_end|>"})
        and pids != qids and o.encode("<think>", add_special_tokens=False) != [QWEN_BAN_MAP["<think>"]]
        and qa.encode("x <think>") != [QWEN_BAN_MAP["<think>"]], (len(qids), len(qstrings)))
    # LOW_MASS reads and the role plan
    la = ScriptedAdapter()
    lid = guard.label_ids(la, labels)
    la.load(None, [LOW_MASS + "slate"])
    low = choice_read(la, text, "prism", "slate", lid, verify=True)
    la.load(None, ["slate"])
    high = choice_read(la, text, "prism", "slate", lid, verify=True)
    chk("testing: a LOW_MASS plan entry wins the read for its label with label mass < .20 and a "
        "non-label top-1; a plain entry wins it with mass > .20 and a label top-1 (verify KL 0.0 both)",
        low.pick == high.pick == "slate" and low.label_mass < 0.2 < high.label_mass
        and not low.top1_is_label and high.top1_is_label and low.verify_kl == high.verify_kl == 0.0,
        (low.label_mass, high.label_mass))
    plan, want = plan_picks("PqQp", "maple", "cedar")
    try:
        plan_picks("PX", "maple", "cedar")
        bad_role = False
    except ValueError:
        bad_role = True
    chk("testing: plan_picks maps P/Q to labels and p/q to LOW_MASS labels; refuses another role",
        plan == ["maple", "~cedar", "cedar", "~maple"] and want == ["maple", "cedar", "cedar", "maple"]
        and bad_role)
    ma = MergingAdapter()
    chk("testing: MergingAdapter breaks prefix stability (the rule 28(d)(a) negative control)",
        ma.encode(pre)[0] != ma.encode(pre + seg)[0] and a.encode(pre)[0] == a.encode(pre + seg)[0])
