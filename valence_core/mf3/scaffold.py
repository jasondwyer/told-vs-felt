"""Q-F3's session scaffold and record -- ONE code path for the F3 runner and its verifier
(PROPOSAL-m v1.11 §2.1 m:159; §2.2 m:174; §2.6 m:265; §4 m:308).

THE SCAFFOLD is ``valence_core.m.scaffold.SessionScaffold``, imported and subclassed, never copied:
``_round``, ``forced``, ``chosen``, ``label_of`` and ``role_of`` are m's. F3 differs in two places:

  order       F2 block order (m:174, "first, first, second, second; start counterbalanced"): start 0
              -> P P Q Q, start 1 -> Q Q P P (m's alternating P Q P Q is F0m's);
  reasoning   per free choice, m:159's "one reasoning-line seed ``int(rng.integers(2**31))``, then the
              menu order ``rng.integers(2)`` ... then one generation seed": ``reasoning(ci)`` draws the
              seed and returns the reasoning block (m:174) at the menu's n; ``menu(ci)`` refuses to
              run before it. Calls out of that order are refused (a harness bug, not a session).

THE RECORD is m-session-v1's (``SessionLog``, imported and subclassed) with ``"format": "F3"``, the
reasoning-line cap and the reasoning lines (``"reasoning"``: one entry per line), and three more
piece kinds -- ``reasoning`` (the block's harness bytes), ``reasoning_text`` (the generation),
``reasoning_joiner`` ("\\n") -- before each free choice's ``menu, pick, round, generation, joiner``.
Every m consumer refuses a Q-F3 record by its unit; every mf3 consumer requires format F3.

DOMAIN (m:308): no exclusion-bearing event before the first read -- forced rounds pass the audit,
echo and lexical classes, and "no hair trigger fired up to and including the first reasoning line";
the binomial defect classes on the first line remove nothing. A ``scaffold_absorption`` fire on a
reasoning line is an exclusion event that ends the session there (the seat's Q8), pre-pick on line
1; after the first pick nothing removes a session from the domain.
"""
from __future__ import annotations

import json
import unicodedata
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

import numpy as np

from valence_core.m import corr as m_corr
from valence_core.m import scaffold as m_scaffold
from valence_core.session_e2a import N_FREE, STOP_CAP

from . import banner, keys, lines, schedule

SCHEMA = m_scaffold.SCHEMA                    # "m-session-v1"
FORMAT = "F3"
N_FORCED = m_scaffold.N_FORCED                # 4 (recon.py:121's N_FORCED, m:174)
REASONING_CAPS = (STOP_CAP, 2 * STOP_CAP)     # 60, or 120 after G-TIME-F3's cap trigger (m:174)
F3_PIECE_KINDS = ("reasoning", "reasoning_text", "reasoning_joiner")
PIECE_KINDS = ("banner", "round", "generation", "joiner", "menu", "pick") + F3_PIECE_KINDS
FREE_GROUP = F3_PIECE_KINDS + ("menu", "pick", "round", "generation", "joiner")
FORCED_GROUP = ("round", "generation", "joiner")
_CELL_KEYS = ("pair_index", "pair", "map", "start", "clause", "P", "Q")
ScaffoldOrderError = m_scaffold.ScaffoldOrderError
pool_and_renders = m_scaffold.pool_and_renders
load_term_rx = m_scaffold.load_term_rx
termination = m_scaffold.termination
assert_native = m_scaffold.assert_native
TranscriptBuilder = m_scaffold.TranscriptBuilder


@dataclass(frozen=True)
class ReasoningSpec:
    ci: int
    n: int                 # the menu's n (m:174)
    seg: str               # banner.reasoning_block(n)
    seed: int
    cap: int               # the reasoning-line cap (60 / 120)


class F3Scaffold(m_scaffold.SessionScaffold):
    """The stateful harness of one F3 session (the module docstring)."""

    def __init__(self, *, reasoning_cap: int, **kw) -> None:
        super().__init__(**kw)
        if type(reasoning_cap) is not int or reasoning_cap not in REASONING_CAPS:
            raise ValueError(f"reasoning_cap must be one of {REASONING_CAPS} (m:174), got {reasoning_cap!r}")
        first, second = ("P", "Q") if self.start == 0 else ("Q", "P")
        # m:174: F2 block order, first first second second (recon.py:116-118's literal).
        self.order = tuple(first if i < self.n_forced // 2 else second for i in range(self.n_forced))
        self.reasoning_cap = reasoning_cap
        self._reasoned: int | None = None

    def reasoning(self, ci: int) -> ReasoningSpec:
        if (self._ri != self.n_forced or ci != self._ci or ci >= self.n_free or self._menu is not None
                or self._reasoned == ci):
            raise ScaffoldOrderError(f"reasoning({ci}) out of order")
        seed = int(self.arm_rng.integers(2**31))       # m:159: before the menu order
        self._reasoned = ci
        n = self.n_forced + 1 + ci
        return ReasoningSpec(ci=ci, n=n, seg=banner.reasoning_block(n), seed=seed, cap=self.reasoning_cap)

    def menu(self, ci: int):
        if self._reasoned != ci:
            raise ScaffoldOrderError(f"menu({ci}) before its reasoning line's seed (m:159)")
        return super().menu(ci)


def check_cell(template: str, cell: Mapping[str, Any]) -> dict:
    """A cell of Q-F3's roster of record in m:159's form (clause None on A2-A3s), or ValueError."""
    if not isinstance(cell, Mapping) or tuple(sorted(cell)) != tuple(sorted(_CELL_KEYS)):
        raise ValueError(f"cell keys must be exactly {_CELL_KEYS}")
    r = schedule.roster()
    pi, mp, st = cell["pair_index"], cell["map"], cell["start"]
    for nm, v in (("pair_index", pi), ("map", mp), ("start", st)):
        if type(v) is not int:
            raise ValueError(f"cell {nm} must be an int, got {v!r}")
    if not 0 <= pi < len(r) or mp not in (0, 1) or st not in (0, 1):
        raise ValueError("cell factor out of range")
    banner.check_clause(template, cell["clause"])
    pair = list(r[pi])
    if list(cell["pair"]) != pair or cell["P"] != pair[mp] or cell["Q"] != pair[1 - mp]:
        raise ValueError("cell pair / P / Q disagree with the roster of record and the map")
    return m_scaffold._copy_cell(cell)


def f3_config(stage: str, template: str, s: int, cell: Mapping[str, Any], path: str, *,
              reasoning_cap: int, pool: Sequence[dict] | None = None,
              renders: Sequence[str] | None = None) -> F3Scaffold:
    """Q-F3's scaffold for one session: split streams, the scheduled cell, §2.5's banner."""
    keys.check_template(template)
    if stage not in keys.STAGES:
        raise ValueError(f"unknown Q-F3 stage {stage!r}")
    if type(s) is not int or s < 0:
        raise ValueError(f"s must be a non-negative int, got {s!r}")
    # PIN (Code, declared at LOCK-m-F3 v0.1): the path is "cached" or "uncached" per session;
    # G-TIME-F3 is uncached by spec (m:293); G-ID-F3 runs both (m:295); the runner's cached
    # argument must agree with the scaffold's path.
    if path not in ("cached", "uncached") or (path == "cached" and stage == "time"):
        raise ValueError(f"path {path!r} not allowed for Q-F3 {stage}")
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:174): G-TIME-F3 generates its reasoning lines at
    # STOP_CAP 60 -- the cap trigger is counted over them -- and every later stage at the cap
    # G-TIME-F3's trigger fixes (60 or 120; m:294-295), checked by stages.prior_gate (F6) and recorded
    # at LOCK-m-F3 v0.2 (m:296).
    if stage == "time" and reasoning_cap != STOP_CAP:
        raise ValueError(f"G-TIME-F3 generates its reasoning lines at {STOP_CAP} (m:174), not {reasoning_cap!r}")
    if stage == "id" and template not in keys.GID_TEMPLATES:
        raise ValueError(f"G-ID-F3 runs {keys.GID_TEMPLATES} only (m:295)")
    c = check_cell(template, cell)
    arm_key = keys.arm_key(stage, template, s)
    item_key = keys.item_key(s, keys.item_gate(stage))
    if pool is None or renders is None:
        p0, r0 = pool_and_renders()
        pool = p0 if pool is None else pool
        renders = r0 if renders is None else renders
    contrast = keys.is_contrast(template)
    text, note_lines = banner.build_banner(template, c["P"], c["Q"], c["clause"])
    # PIN (Code, declared at LOCK-m-F3 v0.1): j = s at gate stages (session j of the sixteen-row
    # table is the template's s-th launch, m:159), None in the campaign -- m's convention.
    meta = {"substrate": "qwen", "unit": keys.UNIT, "stage": stage, "template": template,
            "contrast": contrast, "path": path, "j": None if stage == "campaign" else s,
            "keys": {"arm": arm_key, "items": item_key}, "format": FORMAT}
    return F3Scaffold(reasoning_cap=reasoning_cap, banner=text, cell=c, s=s,
                      arm_rng=keys.stream(arm_key), items=m_corr.ItemStreams(keys.stream(item_key)),
                      delivery=m_corr.Delivery(pool, renders, contrast=contrast),
                      note_lines=note_lines, meta=meta)


def assert_boundary(adapter, prefix: str, seg: str) -> int:
    """Rule 28(d)(a) at every F3 generation, both forms (the seat's Q8; Code's dated note N6)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8 on the "\n\n" after the reasoning segment,
    # N6): the token-comparison form is valence_core.m.scaffold.assert_boundary (the adapters' own
    # comparison; the boundary must be the prefix token count); the character-offset form decodes the
    # first k tokens of the UNTRUNCATED joint encode, k the prefix token count, and requires exactly the
    # prefix's characters (NFC-normalised, the Qwen tokenizer's own normaliser; identity on ASCII and on
    # the stub). Every generation's prefix is the whole transcript so far, so an empty or newline-led
    # reasoning line and its "\n\n" lie inside a later prefix and the assertion is exact over them.
    # Either form failing is a BOUNDARY INCIDENT: HALT before the generation, escalate.
    k = m_scaffold.assert_boundary(adapter, prefix, seg)
    joint = adapter.encode(prefix + seg)
    got = adapter.decode(joint[:k])
    if got != unicodedata.normalize("NFC", prefix):
        raise SystemExit("BOUNDARY INCIDENT (rule 28(d)(a), by character offset): the first "
                         f"{k} tokens of the untruncated joint encode do not decode to exactly the prefix's "
                         "characters; positional delivery geometry is undefined here -- HALT, escalate")
    return k


class F3Log(m_scaffold.SessionLog):
    """One F3 session's record (m-session-v1 + format F3 + the reasoning lines)."""

    def __init__(self, sc: F3Scaffold) -> None:
        if not isinstance(sc, F3Scaffold):
            raise TypeError("F3Log takes an F3Scaffold")
        super().__init__(sc, "qwen")
        self.reasoning: list[dict] = []

    def add_reasoning(self, spec: ReasoningSpec, g, la: lines.LineAudit) -> dict:
        x = {"ci": spec.ci, "n": spec.n, "seed": spec.seed, "cap": spec.cap, "text": str(g.text),
             "n_tok": int(len(g.token_ids)), "cap_hit": bool(g.cap_hit),
             "stop_reason": str(g.stop_reason), "audit": la.as_dict()}
        self.reasoning.append(x)
        return x

    def reasoning_hair(self, la: lines.LineAudit, ci: int) -> None:
        # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "the fire is an exclusion event and ends
        # the session at that point ... the guard's pre-pick count includes it"): a reasoning line's
        # scaffold_absorption fire is recorded as the hair trigger {name, phase "reasoning", ci, detail}
        # and as the session's exclusion {class "scaffold", phase "reasoning", ci, detail} unless an
        # earlier exclusion stands; the strict scope (task-round claims) is unchanged. On line 1 (ci 0)
        # it is pre-pick: the session never reaches a read and leaves the domain (m:308); on a later
        # line the domain stands and whole-session validity is false.
        det = "|".join(la.scaffold)
        self.hair.append({"name": "scaffold_absorption", "phase": "reasoning", "ci": int(ci), "detail": det})
        if self.exclusion is None:
            self.exclusion = {"class": "scaffold", "phase": "reasoning", "ci": int(ci), "detail": det}

    def record(self, seconds: float) -> dict:
        sc = self.sc
        forced = [r for r in self.rounds if r["phase"] == "forced"]
        free = [r for r in self.rounds if r["phase"] == "free"]
        pre_stop = any(h["phase"] == "forced" or (h["phase"] == "reasoning" and h.get("ci") == 0)
                       for h in self.hair)
        exc = self.exclusion
        pre_exc = bool(exc) and (exc["phase"] == "forced" or (exc["phase"] == "reasoning" and exc.get("ci") == 0))
        domain = (len(forced) == sc.n_forced and all(r["audit"]["claim"] is None for r in forced)
                  and not pre_stop and not pre_exc)
        if domain != bool(self.choices):
            raise AssertionError("domain must be exactly 'reached the first read' (m:308)")
        # PIN (Code, declared at LOCK-m-F3 v0.1): complete = 2F forced rounds and N_FREE x (reasoning
        # line, read, chosen round) -- the sixth chosen round present; an exclusion at the last free
        # round leaves it complete (m's convention, the reasoning lines added).
        complete = (len(forced) == sc.n_forced and len(self.reasoning) == sc.n_free
                    and len(self.choices) == sc.n_free and len(free) == sc.n_free)
        rec = {"schema": SCHEMA, "format": FORMAT, "substrate": self.substrate, "unit": sc.unit,
               "stage": sc.stage, "template": sc.template, "contrast": sc.contrast, "s": sc.s, "j": sc.j,
               "keys": dict(sc.keys), "cell": m_scaffold._copy_cell(sc.cell), "banner": sc.banner,
               "note_lines": list(sc.note_lines), "path": sc.path, "reasoning_cap": sc.reasoning_cap,
               "rounds": self.rounds, "reasoning": self.reasoning, "choices": self.choices,
               "pieces": self.tb.pieces, "transcript": self.tb.text,
               "excluded": exc is not None, "exclusion": exc, "strict_exclusion": self.strict,
               "domain": domain,
               "first_free_pick_P": (self.choices[0]["pick"] == sc.P) if domain else None,
               "hair_triggers": self.hair, "complete": complete,
               "seconds": float(seconds), "verified": False}
        rec = json.loads(json.dumps(rec, allow_nan=False))
        assert_native(rec)
        return rec


def prepick_excluded(rec: Mapping[str, Any]) -> bool:
    """m:308's "sessions that never reached a pick": excluded at a forced round or at reasoning line 1."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8): the guard's and the counters' pre-pick
    # exclusion = an exclusion whose phase is "forced", or "reasoning" with ci 0.
    exc = rec.get("exclusion")
    return bool(exc) and (exc.get("phase") == "forced"
                          or (exc.get("phase") == "reasoning" and exc.get("ci") == 0))


def _selftest(chk) -> None:
    import zlib

    pool, renders = pool_and_renders()
    cell = schedule.gate_schedule("qual", "A2", 4)[2]          # start 1
    sc = f3_config("qual", "A2", 2, cell, "uncached", reasoning_cap=60, pool=pool, renders=renders)
    specs = [sc.forced(ri) for ri in range(4)]
    chk("mf3.scaffold: F2 block order -- start 1 gives Q Q P P (m:174), start 0 P P Q Q",
        cell["start"] == 1 and [s.role for s in specs] == ["Q", "Q", "P", "P"]
        and f3_config("qual", "A2", 0, schedule.gate_schedule("qual", "A2", 4)[0], "uncached",
                      reasoning_cap=60).order == ("P", "P", "Q", "Q"))
    r0 = sc.reasoning(0)
    m0 = sc.menu(0)
    ch0 = sc.chosen(0, m0.a)
    r1 = sc.reasoning(1)
    rng = np.random.default_rng(zlib.crc32(b"m-f3|A2|2") % 2**31)
    seeds = [int(rng.integers(2**31)) for _ in range(4)]
    rs0 = int(rng.integers(2**31))
    o0 = int(rng.integers(2))
    cs0 = int(rng.integers(2**31))
    rs1 = int(rng.integers(2**31))
    chk("mf3.scaffold: arm-rng draw order (m:159) -- 4 forced seeds, then per choice the reasoning seed, "
        "the menu order, the chosen seed; recomputed independently from the key",
        [s.seed for s in specs] == seeds and r0.seed == rs0 and (m0.a == sc.P) == (o0 == 0)
        and ch0.seed == cs0 and r1.seed == rs1)
    chk("mf3.scaffold: the reasoning block at the menu's n (5, then 6), cap carried; the chosen round "
        "shares n with its menu",
        (r0.n, r1.n, m0.n, ch0.n) == (5, 6, 5, 5) and r0.seg == "[round 5 | reasoning]\nReasoning (one line):\n"
        and r0.cap == 60)
    order_err = []
    sc2 = f3_config("qual", "A2", 2, cell, "uncached", reasoning_cap=120, pool=pool, renders=renders)
    for fn in (lambda: sc2.reasoning(0), lambda: [sc2.forced(i) for i in range(4)] and sc2.menu(0),
               lambda: sc2.reasoning(1)):
        try:
            fn()
            order_err.append(False)
        except ScaffoldOrderError:
            order_err.append(True)
    sc2.reasoning(0)
    try:
        sc2.reasoning(0)
        order_err.append(False)
    except ScaffoldOrderError:
        order_err.append(True)
    chk("mf3.scaffold: out-of-order calls refused (reasoning before the forced rounds; a menu before its "
        "reasoning seed; a skipped index; a reasoning seed drawn twice)", all(order_err), order_err)
    refused = []
    for fn in (lambda: f3_config("time", "A1", 0, schedule.gate_schedule("time", "A1", 1)[0], "cached",
                                 reasoning_cap=60),
               lambda: f3_config("time", "A1", 0, schedule.gate_schedule("time", "A1", 1)[0], "uncached",
                                 reasoning_cap=120),
               lambda: f3_config("qual", "A1", 0, schedule.gate_schedule("qual", "A1", 4)[0], "uncached",
                                 reasoning_cap=90),
               lambda: f3_config("id", "A2", 0, schedule.gate_schedule("qual", "A2", 4)[0], "uncached",
                                 reasoning_cap=60),
               lambda: f3_config("qual", "A2", 0, {**schedule.gate_schedule("qual", "A2", 4)[0], "clause": 0},
                                 "uncached", reasoning_cap=60),
               lambda: f3_config("qual", "A1", 0, {**schedule.gate_schedule("qual", "A1", 4)[0], "clause": None},
                                 "uncached", reasoning_cap=60),
               lambda: f3_config("qual", "A1", 0, {**schedule.gate_schedule("qual", "A1", 4)[0], "P": "slate"},
                                 "uncached", reasoning_cap=60)):
        try:
            fn()
            refused.append(False)
        except ValueError:
            refused.append(True)
    chk("mf3.scaffold: f3_config refuses G-TIME cached or at cap 120, a cap outside 60/120, G-ID on A2, a "
        "clause on A2 or none on A1, a P off the map", all(refused), refused)
    kq = f3_config("campaign", "A3s", 5, campaign := schedule.campaign_schedule("A3s", 1)[5], "cached",
                   reasoning_cap=60)
    chk("mf3.scaffold: keys and meta -- campaign m|A3s|5 / m-f3-items|5, j None, format F3, unit Q-F3",
        kq.keys == {"arm": "m|A3s|5", "items": "m-f3-items|5"} and kq.j is None and kq.format == "F3"
        and kq.unit == "Q-F3" and kq.contrast is False and campaign["clause"] is None)
    # deliveries: a contrast arm's Q role gets the render; A2s (sham) the clean text; items per role
    c_sc = f3_config("qual", "A3", 1, schedule.gate_schedule("qual", "A3", 8)[1], "uncached", reasoning_cap=60)
    s_sc = f3_config("qual", "A3s", 1, schedule.gate_schedule("qual", "A3s", 8)[1], "uncached", reasoning_cap=60)
    cs = [c_sc.forced(i) for i in range(4)]
    ss = [s_sc.forced(i) for i in range(4)]
    perm = np.random.default_rng(zlib.crc32(b"m-f3-items-qual|1") % 2**31).permutation(16)
    want = {"P": [int(x) for x in perm[:8]], "Q": [int(x) for x in perm[8:]]}

    def drawn(specs):
        got = {"P": [], "Q": []}
        for x in specs:
            got[x.role].append(x.item)
        return all(got[r] == want[r][:len(got[r])] for r in "PQ")

    chk("mf3.scaffold: contrast Q rounds deliver the corrupt_m render and P rounds clean text; the sham's "
        "are all clean; both templates draw from m-f3-items-qual|1's [:8] P / [8:] Q split in order",
        all((x.property == "corrupted") == (x.role == "Q") for x in cs) and all(x.property == "clean" for x in ss)
        and all(x.task_text == (renders[x.item] if x.role == "Q" else pool[x.item]["task"]) for x in cs)
        and drawn(cs) and drawn(ss))
    log = F3Log(f3_config("qual", "A2s", 0, schedule.gate_schedule("qual", "A2s", 8)[0], "uncached",
                          reasoning_cap=60))
    try:
        log.record(0.0)
        bad_domain = False
    except AssertionError:
        bad_domain = True
    chk("mf3.scaffold: an empty record (no forced round) is out of the domain and records without error",
        not bad_domain)
    chk("mf3.scaffold: pre-pick = forced, or reasoning line 1 (the seat's Q8)",
        prepick_excluded({"exclusion": {"phase": "forced"}})
        and prepick_excluded({"exclusion": {"phase": "reasoning", "ci": 0}})
        and not prepick_excluded({"exclusion": {"phase": "reasoning", "ci": 1}})
        and not prepick_excluded({"exclusion": {"phase": "free"}}) and not prepick_excluded({"exclusion": None}))
