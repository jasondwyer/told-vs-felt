"""Q-F3's bar table (PROPOSAL-m v1.11 §3 m:271; §3.2 m:293, m:295, m:297; §4 m:316; §6 m:330).

The ARITHMETIC is ``valence_core.m.bars``'s, imported unchanged: exact Fractions (``q``; floats
refused), ``binom_sf``, ``fires`` (P <= alpha), ``critical_k``, ``realised_table``, ``fisher_sf``,
``seq_false_pause``, ``BarResult``, ``Bar.evaluate`` and its blinded messages, ``verify_firing`` and
``assert_firing_complete`` (rule 21: every declared bar exercised firing AND silent). m's ``Bar``
refuses a Q-F3 scope (keys.UNITS_BUILT) and knows four domains; ``F3Bar`` subclasses it with Q-F3's
vocabulary -- its validation and context check -- and one more domain, the pooled lexical bar's
A2s + A3s (m:330). Every evaluation runs through m's ``Bar.evaluate``.

THE TABLE (every bar of Q-F3's later stages with class, unit, p0, alpha, domain and cadence, m:292):
hair triggers (``scaffold_absorption`` -- task rounds AND reasoning lines --, ``template_breakage``,
``schedule_mismatch``); G-TIME-F3's ``round_degeneracy`` (sham rounds <= 30, p0 .05, critical 5)
and ``reasoning_line_defect`` (sham lines <= 18, p0 .10, critical 5); G-ID-F3's 2/2 criterion
(``gid_divergence``); G-F3's ``round_degeneracy`` (<= 240, .05, 19) and ``reasoning_line_defect``
(<= 144, .10, 22); the campaign's looks -- ``round_degeneracy`` (p0 .05, the three sham arms),
``reasoning_line_defect`` (p0 .10, the three sham arms), ``own_pair_lexical`` (p0 .02 per task round,
A2s and A3s) -- and the exclusion guard per contrast arm (Fisher vs its matched sham and absolute
.20, both binding on Qwen).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterable, Mapping, Sequence

from valence_core.m import bars as m_bars

from . import keys, lines

KINDS = m_bars.KINDS
q, binom_sf, fires, critical_k = m_bars.q, m_bars.binom_sf, m_bars.fires, m_bars.critical_k
seq_false_pause, BarResult = m_bars.seq_false_pause, m_bars.BarResult
STAGES = ("time", "id", "qual", "campaign", "every")
#: Q-F3's domain codes: m's four, re-worded for Q-F3, and the pooled lexical bar's domain.
DOMAINS = {
    "every": "every session, every template (m:271)",
    "sham": "sham-template sessions only (A1s, A2s, A3s); contrast sessions reported beside, not bound "
            "(m:271, rule 21)",
    "lexical_sham": "A2s and A3s sessions' task rounds (m:330: the arms whose banners name no labels)",
    "contrast_arm": "per contrast arm against its matched sham arm (m:316)",
    "pairs": "complete cached/uncached A2s and A3s session pairs (m:295)",
}
_KIND_DOMAINS = {"hair_trigger": ("every", "pairs"), "binomial_stage_end": ("sham",),
                 "binomial_look": ("sham", "lexical_sham"), "pause": ("sham",),
                 "guard_fisher": ("contrast_arm",), "guard_abs": ("contrast_arm",)}
LEXICAL_SHAM = ("A2s", "A3s")
DEGEN_CLAIMS = m_bars.DEGEN_CLAIMS["qwen"]
CLAIMS = m_bars.CLAIMS["qwen"]
MAX_ROUNDS = m_bars.MAX_ROUNDS                 # 4 forced + 6 free task rounds
MAX_LINES = 6                                  # one reasoning line per free choice (N_FREE)


@dataclass(frozen=True)
class F3Bar(m_bars.Bar):
    """m's Bar with Q-F3's vocabulary (scope Q-F3, substrate qwen, F3's domains and templates)."""

    def __post_init__(self) -> None:
        if self.kind not in KINDS:
            raise ValueError(f"{self.name}: unknown bar kind {self.kind!r}")
        if self.domain not in DOMAINS or self.domain not in _KIND_DOMAINS[self.kind]:
            raise ValueError(f"{self.name}: a {self.kind} bar's domain must be one of {_KIND_DOMAINS[self.kind]}")
        if self.kind in ("hair_trigger", "pause") and not self.justification.strip():
            raise ValueError(f"{self.name}: a one-claim trigger is licensed only for ~zero-base-rate classes "
                             f"(rule 21) -- state the justification")
        if self.kind == "hair_trigger" and not self.binding:
            raise ValueError(f"{self.name}: a hair trigger that does not stop is not a hair trigger")
        if self.kind in ("binomial_stage_end", "binomial_look", "guard_abs"):
            if self.p0 is None:
                raise ValueError(f"{self.name}: binomial bar needs a declared p0")
            m_bars._prob(self.p0, f"{self.name} p0")
        elif self.p0 is not None:
            raise ValueError(f"{self.name}: a {self.kind} bar takes no p0")
        m_bars._prob(self.alpha, f"{self.name} alpha")
        if self.stage not in STAGES or self.scope != keys.UNIT or self.substrate != "qwen":
            raise ValueError(f"{self.name}: stage / scope / substrate must be Q-F3's (qwen)")
        if self.planned_n is not None:
            want = (critical_k(self.planned_n, self.p0, self.alpha)
                    if self.kind in ("binomial_stage_end", "binomial_look", "guard_abs")
                    else (1 if self.planned_n >= 1 else None))
            if self.planned_crit != want:
                raise ValueError(f"{self.name}: declared critical {self.planned_crit} at n = {self.planned_n}, "
                                 f"exact critical is {want}")
        elif self.planned_crit is not None:
            raise ValueError(f"{self.name}: a planned critical count needs its planned n")

    def _check_ctx(self, ctx: dict):
        extra = set(ctx) - {"template", "phase", "look", "sham_k", "sham_n"}
        if extra:
            raise TypeError(f"{self.name}: unknown evaluation context {sorted(extra)}")
        if self.kind != "guard_fisher" and ({"sham_k", "sham_n"} & set(ctx)):
            raise TypeError(f"{self.name}: sham counts are the Fisher guard's only")
        template, phase, look = ctx.get("template"), ctx.get("phase"), ctx.get("look")
        if template is not None:
            keys.check_template(template)
            c = keys.is_contrast(template)
            if self.domain in ("sham", "pairs") and c:
                raise ValueError(f"{self.name}: DOMAIN VIOLATION: a contrast-template session on a sham-only bar")
            if self.domain == "lexical_sham" and template not in LEXICAL_SHAM:
                raise ValueError(f"{self.name}: DOMAIN VIOLATION: {template} is outside A2s / A3s (m:330)")
            if self.domain == "pairs" and template not in keys.GID_TEMPLATES:
                raise ValueError(f"{self.name}: G-ID-F3 runs A2s and A3s only (m:295)")
            if self.domain == "contrast_arm" and not c:
                raise ValueError(f"{self.name}: the guard is evaluated per contrast arm (m:316)")
        if phase is not None:
            if self.kind not in ("hair_trigger", "pause"):
                raise ValueError(f"{self.name}: a {self.kind} bar is evaluated over a domain, not a phase")
            if phase not in ("forced", "free", "reasoning"):
                raise ValueError(f"{self.name}: phase must be forced, free or reasoning, got {phase!r}")
        if look is not None:
            if self.kind not in ("binomial_look", "guard_fisher", "guard_abs"):
                raise ValueError(f"{self.name}: a {self.kind} bar has no looks")
            if look != "end" and not (isinstance(look, int) and not isinstance(look, bool) and look >= 1):
                raise ValueError(f"{self.name}: look must be an int >= 1 or 'end', got {look!r}")
        return template, phase, look

    def as_dict(self) -> dict:
        d = {"name": self.name, "class": self.cls, "kind": self.kind, "stage": self.stage, "scope": self.scope,
             "substrate": self.substrate, "p0": None if self.p0 is None else str(self.p0), "alpha": str(self.alpha),
             "domain": self.domain, "domain_text": DOMAINS[self.domain], "unit": self.unit,
             "cadence": self.cadence, "numerator": self.numerator, "binding": self.binding,
             "on_fire": self.on_fire, "justification": self.justification, "planned_n": self.planned_n,
             "planned_crit": self.planned_crit}
        if self.kind == "binomial_stage_end" and self.planned_n:
            d["realised_table"] = [list(r) for r in m_bars.realised_table(self.p0, self.alpha, self.planned_n)]
        return d


# --- the declarations --------------------------------------------------------------------
S, SUB = keys.UNIT, "qwen"
_HAIR = ("evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271)")
_END = "once at stage end on the realised n; no mid-stage evaluation (m:271)"
_LOOK = ("every 40 launches and at the end, cumulative count, alpha .05 per look, no alpha spending; look "
         "index in the resume identity (m:330)")
_GUARD = "at every look, per contrast arm (m:316)"
_PAUSE = "PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316)"
_JUST_SCAFFOLD = ("A string of Qwen's scaffold set (the e2a ban list as e2d.config loads it, m:261; pinned by sha) "
                  "in model-generated text -- a task round or a reasoning line, whose generation carries the same "
                  "ban (m:265) -- means the ban did not apply; the tokens are suppressed in the sampler, so the base "
                  "rate is structurally zero.")
_JUST_BREAK = ("Harness bytes that fail G-VER (m:284): the harness writes every scaffold byte itself, reasoning "
               "blocks included; base rate zero by construction.")
_JUST_MISMATCH = ("Pair, map, start order, clause order, banner bytes, item stream or the template's role on a "
                  "shared banner differing from the committed schedule (m:271, m:253): zero by construction.")
_JUST_GID = ("G-ID's criterion is 2/2 byte-identical cached/uncached transcript pairs (m:281, carried by m:295): "
             "identity is the criterion itself, so no divergence rate is tolerated.")
_JUST_DEGEN = ("Measured class: v2-or-echo has a measured rate (v2 17/597 on f1's CORR rounds, 11/351 on its SHAM "
               "pool [C]), so rule 21 binds it by exact binomial; p0 .05 is a declared tolerance at a named, changed "
               "contrast (m:271).")
_JUST_LINES = ("m's own declared tolerance, p0 .10 -- no reference rate exists for the class (m:271, v1.3's "
               "label); the numerator is the union of m:265's three classes, once per line (m:293).")
_JUST_LEX = ("Adapted from f1's session-unit monitor (archive:403) to the round unit: p0 .02 per task round, f1's "
             "per-round reference ~19/3074 ~.006 [C], ~3x headroom because the F3 domain's rounds sit beside "
             "reasoning lines the reference did not have (m:330).")
_U_ROUNDS = "task round generated (<= 10 per session: 4 forced + 6 free)"
_U_LINES = "reasoning line generated (<= 6 per session, one per free choice)"
_N_DEGEN = "rounds claimed by audit v2 or m's harness-echo class (m:261)"
_N_LINES = "reasoning lines with any of m:265's three classes (empty, cap without newline, reasoning-line echo)"
_N_LEX = "task rounds claimed lexical under m:261's claiming order, forced and free"
_U_GUARD = "session launched in the arm through the look (pre-pick exclusion)"
_N_GUARD = ("pre-pick exclusions (sessions excluded before their first read: at a forced round or at reasoning "
            "line 1, m:308; the seat's Q8)")


def _degen(stage: str, name: str, n: int, crit: int, on_fire: str) -> F3Bar:
    return F3Bar(f"round_degeneracy@{name}", "binomial_stage_end", p0="0.05", alpha="0.05", domain="sham",
                 unit=_U_ROUNDS, cadence=_END, justification=_JUST_DEGEN, stage=stage, scope=S, substrate=SUB,
                 numerator=_N_DEGEN, on_fire=on_fire, planned_n=n, planned_crit=crit)


def _lines_bar(stage: str, name: str, n: int, crit: int, on_fire: str) -> F3Bar:
    return F3Bar(f"reasoning_line_defect@{name}", "binomial_stage_end", p0="0.10", alpha="0.05", domain="sham",
                 unit=_U_LINES, cadence=_END, justification=_JUST_LINES, stage=stage, scope=S, substrate=SUB,
                 numerator=_N_LINES, on_fire=on_fire, planned_n=n, planned_crit=crit)


def _qf3_bars() -> tuple[F3Bar, ...]:
    tag = f"campaign-{S}"
    # PIN (Code, declared at LOCK-m-F3 v0.1; m:271 "unit session/round"): scaffold_absorption's unit is
    # the model generation -- a task round or a reasoning line (m:265, "the one hair trigger that reads
    # it"); G-ID-F3's criterion is declared gid_divergence as Q-F0's was, its unit the complete pair.
    return (
        F3Bar("scaffold_absorption", "hair_trigger", domain="every",
              unit="model generation (a task round or a reasoning line)", cadence=_HAIR,
              justification=_JUST_SCAFFOLD, stage="every", scope=S, substrate=SUB,
              numerator="generations containing a scaffold-set string", on_fire="STOP the stage (m:271)"),
        F3Bar("template_breakage", "hair_trigger", domain="every", unit="session", cadence=_HAIR,
              justification=_JUST_BREAK, stage="every", scope=S, substrate=SUB, numerator="sessions failing G-VER",
              on_fire="STOP the stage (m:271)"),
        F3Bar("schedule_mismatch", "hair_trigger", domain="every", unit="session", cadence=_HAIR,
              justification=_JUST_MISMATCH, stage="every", scope=S, substrate=SUB,
              numerator="sessions differing from the committed schedule", on_fire="STOP the stage (m:271)"),
        # PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B17): if G-TIME-F3's line bar fires the
        # stage STOPs and the seat re-specifies; the cap-trigger count is reported in the stop record and
        # applied by nobody until then.
        _degen("time", "G-TIME-F3", 30, 5, "STOP before G-ID-F3 (m:293; the bars bind alone, m:271)"),
        _lines_bar("time", "G-TIME-F3", 18, 5, "STOP before G-ID-F3; the seat re-specifies (m:293)"),
        F3Bar("gid_divergence@G-ID-F3", "hair_trigger", domain="pairs",
              unit="complete cached/uncached pair (4 forced rounds + 6 x (reasoning line, read, chosen round) each)",
              cadence="per complete pair, uncached first, A2s then A3s; stops at the first divergence (m:281, m:295)",
              justification=_JUST_GID, stage="id", scope=S, substrate=SUB,
              numerator="complete pairs whose transcripts differ in any byte",
              on_fire="G-ID-F3 FAIL: Q-F3 runs uncached (m:295)"),
        _degen("qual", "G-F3", 240, 19, "STOP: Q-F3 does not run until the seat re-specifies (m:297, m:271)"),
        _lines_bar("qual", "G-F3", 144, 22, "STOP: Q-F3 does not run until the seat re-specifies (m:297, m:271)"),
        F3Bar(f"round_degeneracy@{tag}", "binomial_look", p0="0.05", alpha="0.05", domain="sham", unit=_U_ROUNDS,
              cadence=_LOOK, justification=_JUST_DEGEN, stage="campaign", scope=S, substrate=SUB,
              numerator=_N_DEGEN, on_fire=_PAUSE),
        F3Bar(f"reasoning_line_defect@{tag}", "binomial_look", p0="0.10", alpha="0.05", domain="sham",
              unit=_U_LINES, cadence=_LOOK, justification=_JUST_LINES, stage="campaign", scope=S, substrate=SUB,
              numerator=_N_LINES, on_fire=_PAUSE),
        F3Bar(f"own_pair_lexical@{tag}", "binomial_look", p0="0.02", alpha="0.05", domain="lexical_sham",
              unit="task round generated in A2s / A3s", cadence=_LOOK, justification=_JUST_LEX, stage="campaign",
              scope=S, substrate=SUB, numerator=_N_LEX, on_fire=_PAUSE),
        F3Bar(f"exclusion_guard_fisher@{tag}", "guard_fisher", alpha="0.05", domain="contrast_arm",
              unit=_U_GUARD, cadence=_GUARD,
              justification="Adapted from f1's guard (archive:400-402): each contrast arm's pre-pick exclusion rate "
                            "vs its matched sham by one-sided Fisher exact, binding (m:316).",
              stage="campaign", scope=S, substrate=SUB, numerator=_N_GUARD, on_fire=_PAUSE),
        F3Bar(f"exclusion_guard_abs@{tag}", "guard_abs", p0="0.20", alpha="0.05", domain="contrast_arm",
              unit=_U_GUARD, cadence=_GUARD,
              justification="f1's whole-session reference .20 at F0 carried to m's pre-pick unit and, in Q-F3, to F3 "
                            "without re-derivation: a declared tolerance at a named, changed contrast (m:316).",
              stage="campaign", scope=S, substrate=SUB, numerator=_N_GUARD, on_fire=_PAUSE),
    )


QF3_BARS: tuple[F3Bar, ...] = _qf3_bars()


def bar(name: str) -> F3Bar:
    return {b.name: b for b in QF3_BARS}[name]


def _crit_cases(name: str, n: int, p0: str) -> list[tuple]:
    c = critical_k(n, p0, "0.05")
    return [(name, c, n, True, {"crit": c}), (name, c - 1, n, False, {"crit": c})]


def _qf3_cases() -> list[tuple]:
    tag = f"campaign-{S}"
    rt, lt, rq, lq = ("round_degeneracy@G-TIME-F3", "reasoning_line_defect@G-TIME-F3", "round_degeneracy@G-F3",
                      "reasoning_line_defect@G-F3")
    return (m_bars._hair_cases() + [
        ("gid_divergence@G-ID-F3", 1, 1, True, {}), ("gid_divergence@G-ID-F3", 0, 2, False, {}),
        (rt, 5, 30, True, {"p4": "0.0156", "crit": 5}), (rt, 4, 30, False, {"p4": "0.0608"}),
        (rt, 1, 1, True, {"p": "1/20", "crit": 1}), (rt, 1, 2, False, {"crit": 2}),
        (lt, 5, 18, True, {"p4": "0.0282", "crit": 5}), (lt, 4, 18, False, {"p4": "0.0982"}),
        (lt, 1, 1, False, {"crit": None}), (lt, 2, 2, True, {"p": "1/100", "crit": 2}),
        (lt, 2, 3, True, {"p4": "0.0280", "crit": 2}),
        (rq, 19, 240, True, {"p4": "0.0336", "crit": 19}), (rq, 18, 240, False, {"p4": "0.0581"}),
        (lq, 22, 144, True, {"p4": "0.0296", "crit": 22}), (lq, 21, 144, False, {"p4": "0.0507"}),
    ] + _crit_cases(f"round_degeneracy@{tag}", 2000, "0.05") + _crit_cases(f"reasoning_line_defect@{tag}", 600, "0.10")
        + _crit_cases(f"own_pair_lexical@{tag}", 500, "0.02")
        + m_bars._guard_cases(tag, f"exclusion_guard_abs@{tag}"))


#: Every Q-F3 bar in both directions, plus m's mandatory table and the spec's counts.
FIRING_CASES: tuple[tuple, ...] = tuple(_qf3_cases() + list(m_bars.MANDATORY_CASES) + list(m_bars.SPEC_COUNT_CASES))


def assert_firing_complete() -> tuple[F3Bar, ...]:
    """m's firing check over Q-F3's bars and cases (SystemExit on any misbehaviour or gap)."""
    return m_bars.assert_firing_complete(QF3_BARS, FIRING_CASES)


# --- evaluation on the realised n ----------------------------------------------------------
def _domain(records: Iterable[Mapping], b: F3Bar, stage_names: Sequence[str]) -> list[Mapping]:
    seen: set = set()
    out = []
    for r in records:
        t = r["template"]
        if b.domain == "sham" and not keys.is_sham(t):
            continue
        if b.domain == "lexical_sham" and t not in LEXICAL_SHAM:
            continue
        if r.get("unit") != keys.UNIT or r.get("substrate") != "qwen" or r.get("format") != "F3":
            raise ValueError(f"{b.name}: a non-Q-F3 record on a Q-F3 bar")
        if r.get("stage") not in stage_names:
            raise ValueError(f"{b.name}: a {r.get('stage')!r}-stage record on a {b.stage} bar")
        ident = (t, r["s"], r.get("j"), r.get("path"))
        if ident in seen:
            raise ValueError(f"{b.name}: a session appears twice in the domain")
        seen.add(ident)
        if len(r["rounds"]) > MAX_ROUNDS or len(r.get("reasoning") or []) > MAX_LINES:
            raise ValueError(f"{b.name}: a session records more task rounds or lines than F3 has")
        out.append(r)
    return out


def counts(records: Iterable[Mapping], b: F3Bar) -> tuple[int, int]:
    """(k, n) of a binomial bar over its domain: rounds claimed v2/echo (round_degeneracy), lines with
    any class (reasoning_line_defect) or rounds claimed lexical (own_pair_lexical) over the units
    generated, every domain session counted (excluded ones included: they generated their units)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): m's stage_end_eval PIN carried -- the domain is every
    # selected session, excluded included; n counts every recorded unit; the numerator by claim (rounds)
    # or by the union of classes (lines); content and lexical claims never count toward round_degeneracy.
    stage_names = (b.stage, b.name.split("@", 1)[1]) if "@" in b.name else (b.stage,)
    dom = _domain(records, b, stage_names)
    if b.cls == "reasoning_line_defect":
        ls = [x for r in dom for x in r.get("reasoning") or []]
        return sum(bool(x["audit"]["classes"]) for x in ls), len(ls)
    rounds = [rd for r in dom for rd in r["rounds"]]
    for rd in rounds:
        if rd["audit"]["claim"] not in CLAIMS:
            raise ValueError(f"{b.name}: claim {rd['audit']['claim']!r} is not a Qwen class")
    if b.cls == "own_pair_lexical":
        return sum(rd["audit"]["claim"] == "lexical" for rd in rounds), len(rounds)
    if b.cls == "round_degeneracy":
        return sum(rd["audit"]["claim"] in DEGEN_CLAIMS for rd in rounds), len(rounds)
    raise ValueError(f"{b.name}: counts() serves the binomial bars")


def evaluate(records: Iterable[Mapping], b: F3Bar, *, look: Any = None) -> BarResult:
    """A binomial bar on the realised n (a stage-end bar once at stage end; a look bar at a look)."""
    if b.kind not in ("binomial_stage_end", "binomial_look"):
        raise ValueError(f"{b.name}: evaluate() serves the binomial bars")
    k, n = counts(list(records), b)
    ctx = {} if look is None else {"look": look}
    return b.evaluate(k, n, **ctx)


def no_test(res: BarResult) -> bool:
    """B30's reading: a stage-end bar at realised n = 0 is no test -- reported, not fired (by analogy with m:271)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B30, revised on the build review's finding 6):
    # at a gate stage a binomial bar whose realised n is 0 (every sham session ended before its first
    # reasoning line, say) is reported as no test and not fired, and the stage ends on its other bars. This is
    # Code's reading by analogy with m:271's Qwen rule, which says "reported, not fired" of G-TIME-F0's realised
    # n of 2-4 and "on Qwen no such pause exists" of OLMo's G-TIME pause; m:271 says nothing of n = 0. At a
    # campaign look n = 0 is silent (the count is cumulative).
    return res.n == 0


def _selftest(chk) -> None:
    from . import testing

    try:
        assert_firing_complete()
        ok, msg = True, ""
    except SystemExit as e:
        ok, msg = False, str(e)[:300]
    chk(f"mf3.bars: every declared Q-F3 bar ({len(QF3_BARS)}) fires and stays silent on its cases (rule 21); m's "
        "mandatory and spec-count tables pass on m's arithmetic", ok, msg)
    want = {"round_degeneracy@G-TIME-F3": (30, 5, "0.05"), "reasoning_line_defect@G-TIME-F3": (18, 5, "0.10"),
            "round_degeneracy@G-F3": (240, 19, "0.05"), "reasoning_line_defect@G-F3": (144, 22, "0.10")}
    got = {n: (bar(n).planned_n, bar(n).planned_crit, str(bar(n).p0)) for n in want}
    chk("mf3.bars: the four planned critical counts are m:271's (G-TIME-F3 5 and 5; G-F3 19 and 22)", got == want, got)
    refused = []
    for fn in (lambda: F3Bar("x", "binomial_stage_end", p0="0.05", domain="sham", stage="qual", scope="Q-F0",
                             substrate="qwen"),
               lambda: F3Bar("x", "binomial_look", p0=0.05, domain="sham", stage="campaign", scope="Q-F3",
                             substrate="qwen"),
               lambda: F3Bar("x", "hair_trigger", domain="every", stage="every", scope="Q-F3", substrate="qwen"),
               lambda: F3Bar("x", "binomial_stage_end", p0="0.05", domain="sham", stage="qual", scope="Q-F3",
                             substrate="qwen", planned_n=240, planned_crit=18),
               lambda: bar("own_pair_lexical@campaign-Q-F3").evaluate(1, 10, template="A1s"),
               lambda: bar("round_degeneracy@G-F3").evaluate(1, 10, template="A3"),
               lambda: bar("exclusion_guard_abs@campaign-Q-F3").evaluate(1, 10, template="A2s")):
        try:
            fn()
            refused.append(False)
        except (ValueError, TypeError):
            refused.append(True)
    chk("mf3.bars: refuses a Q-F0 scope, a float p0, a justification-less hair trigger, a wrong planned "
        "critical count, the lexical bar on A1s, a sham bar on a contrast template, the guard on a sham",
        all(refused), refused)
    recs = list({(r["template"], r["s"]): r for _, r, _ in testing.suite()}.values())
    k, n = counts(recs, bar("reasoning_line_defect@G-F3"))
    sham_lines = sum(len(r["reasoning"]) for r in recs if keys.is_sham(r["template"]))
    defect = sum(bool(x["audit"]["classes"]) for r in recs if keys.is_sham(r["template"]) for x in r["reasoning"])
    kr, nr = counts(recs, bar("round_degeneracy@G-F3"))
    kl, nl = counts([{**r, "stage": "campaign"} for r in recs], bar("own_pair_lexical@campaign-Q-F3"))
    try:
        counts(recs, bar("own_pair_lexical@campaign-Q-F3"))
        stage_ok = False
    except ValueError:
        stage_ok = True
    chk("mf3.bars: counts over the sham domain -- lines with any class over lines generated; v2/echo rounds over "
        "rounds; lexical rounds over A2s + A3s rounds",
        (k, n) == (defect, sham_lines) and k == 4 and nr == sum(len(r["rounds"]) for r in recs if keys.is_sham(r["template"]))
        and kr == sum(rd["audit"]["claim"] in ("v2", "echo") for r in recs if keys.is_sham(r["template"]) for rd in r["rounds"])
        and nl == sum(len(r["rounds"]) for r in recs if r["template"] in LEXICAL_SHAM) and kl == 1 and stage_ok,
        (k, n, kr, nr, kl, nl, stage_ok))
    res0 = bar("reasoning_line_defect@G-TIME-F3").evaluate(0, 0)
    chk("mf3.bars: a stage-end bar at realised n = 0 is no test (B30), never a fire", no_test(res0) and not res0.fired)
    d = bar("own_pair_lexical@campaign-Q-F3").as_dict()
    chk("mf3.bars: declaration rows carry class, unit, p0, alpha, domain (with its text) and cadence (m:292)",
        d["domain"] == "lexical_sham" and "A2s and A3s" in d["domain_text"] and d["p0"] == "0.02"
        and all(set(b.as_dict()) >= {"class", "unit", "p0", "alpha", "domain", "cadence"} for b in QF3_BARS))
