"""PROPOSAL-m exact bars: a bar fires iff its exact one-sided P <= alpha
(v1.11 §3 m:271, m:72; §4 m:316; §6 m:330; build pin 1 "P <= alpha implemented
explicitly").

WHY A NEW MODULE. Every operational bar in the repo fires on ``p < alpha``
(``session.Tripwire`` session.py:211; f1's guard f_sessions.py:412-415; b3; e2d),
and ``stats.CheckpointedBinomialMonitor`` uses ``<=`` but in floats, overflowing
for n >= 1030. m's convention is ``<=`` "at every boundary" (m:271, STOP-8 §C
item 123), and the disclosed boundary is a tie: G-TIME-F0's sham session with a
round-1 claim, n = 1, P = .05 = alpha, fires (m:271). ``Tripwire.check(1, 1)``
returns None there. So decisions here are exact rationals over integers:
``q()`` builds every p0/alpha from a str, int or Fraction and refuses a float
(``Fraction(0.05) != 1/20``: a float p0 silences the n = 1 tie). Neither
session.py nor stats.py is edited (rule 26: their consumers are frozen); stats.py
is used only as a descriptive cross-check in the self-test.

DECLARED BARS (m:279: LOCK v0.1 declares every bar of every later stage with
class, unit, p0, alpha, domain and cadence).
- Hair triggers, unit session/round, domain every session, both templates; a fire
  anywhere stops the stage (m:271): ``scaffold_absorption`` (the substrate's ban
  set: Qwen's e2a ban list via e2d.config, m:261; OLMo's six b3 strings, m:262),
  ``template_breakage`` (G-VER, m:284), ``schedule_mismatch`` (m:271, m:253).
  G-ID-F0m's 2/2 byte-identity criterion is "a hair trigger" (m:281).
- ``round_degeneracy`` binomial bars, evaluated once at stage end on the
  realised n, domain the sham-template sessions only, contrast sessions reported
  beside (m:271, rule 21): G-TIME-F0 (n <= 10, p0 .05, critical 3, m:280),
  G-F0m-Qwen (<= 160, .05, 14, m:283), G-TIME-OLMo-{ckpt} (<= 10, .02, 2, m:302),
  G-F0m-OLMo-{ckpt} (<= 160, .02, 7, m:302). Numerator: Qwen rounds claimed by v2
  or echo (m:261); OLMo rounds claimed by b3's AuditSpec or echo (m:262).
- The OLMo G-TIME pause: any AuditSpec- or echo-claimed round of that stage's sham
  session pauses for the seat (m:271, m:302); on Qwen no such pause exists.
- Campaign (§6, m:330): ``round_degeneracy`` looks every 40 launches and at the
  end on the unit's sham arm, cumulative, alpha .05 per look, a fire pauses; no
  lexical bar in Q-F0 or on OLMo (every banner names labels). Exclusion guard
  (m:316): per contrast arm at every look, one-sided Fisher vs the matched sham
  (binding on both substrates) and exact binomial vs an absolute .20 (binding on
  Qwen, reported only on OLMo).

Realised-n critical tables (``realised_table``) are what the stage-end
evaluation actually uses, so the LOCK declares them beside the planned-n figure
(maps/stats.md §5-§6 item 3). ``seq_false_pause`` is §6's exact sequential
false-pause programme for G-PWR (m:285); built, not used at step 4.

Messages (``BarResult.message``) carry only the bar name, template, phase and
look words and numbers -- never a tag, label, render or round index (m:263,
m:318); a hair trigger's message carries no count at all.
"""
from __future__ import annotations

import operator
from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Any, Callable, Iterable, Sequence

from valence_core.m import keys

KINDS = ("hair_trigger", "binomial_stage_end", "binomial_look", "guard_fisher",
         "guard_abs", "pause")
_BINOMIAL = ("binomial_stage_end", "binomial_look", "guard_abs")
_ONE_CLAIM = ("hair_trigger", "pause")

#: Domain codes (enforced) and the words a LOCK prints for them.
DOMAINS = {
    "every": "every session, both templates (m:271)",
    "sham": "sham-template sessions only; contrast sessions reported beside, not "
            "bound (m:271, rule 21)",
    "contrast_arm": "per contrast arm against its matched sham arm (m:316)",
    "pairs": "complete cached/uncached A0s session pairs (m:281)",
}
_KIND_DOMAINS = {
    "hair_trigger": ("every", "pairs"),
    "binomial_stage_end": ("sham",),
    "binomial_look": ("sham",),
    "pause": ("sham",),
    "guard_fisher": ("contrast_arm",),
    "guard_abs": ("contrast_arm",),
}
STAGES = ("time", "id", "qual", "campaign", "every")   # keys.arm_key's vocabulary

#: Claim vocabulary per substrate (audit wrapper, maps/audit.md §7) and the
#: round_degeneracy numerator (m:261, m:262).
CLAIMS = {"qwen": frozenset({"v2", "echo", "content", "lexical", None}),
          "olmo": frozenset({"audit", "echo", "lexical", None})}
DEGEN_CLAIMS = {"qwen": frozenset({"v2", "echo"}), "olmo": frozenset({"audit", "echo"})}
MAX_ROUNDS = 10   # 4 forced + 6 free task rounds per session (session_e2a.N_FREE = 6)


# --- exact arithmetic ----------------------------------------------------------
def q(x: Any) -> Fraction:
    """A declared p0 or alpha as an exact Fraction, from str, int or Fraction.

    Floats are refused: ``Fraction(0.05)`` is 3602879701896397/72057594037927936,
    not 1/20, and with it the n = 1 tie of m:271 stops firing."""
    if isinstance(x, bool):
        raise TypeError("p0/alpha must be str, int or Fraction, not bool")
    if isinstance(x, Fraction):
        return x
    if isinstance(x, int):
        return Fraction(x)
    if isinstance(x, str):
        return Fraction(x)
    raise TypeError(f"p0/alpha must be str, int or Fraction, not {type(x).__name__} "
                    "(Fraction(0.05) != 1/20; declare '0.05')")


def _prob(x: Any, what: str) -> Fraction:
    v = q(x)
    if not 0 <= v <= 1:
        raise ValueError(f"{what} out of [0, 1]: {v}")
    return v


def _int(x: Any, what: str) -> int:
    # PIN (Code, declared at LOCK v0.1): counts are exact integers; Python ints
    # and numpy integers are accepted (both exact via operator.index), bool and
    # float refused -- a float count is a bookkeeping defect, not a count.
    if isinstance(x, (bool, float)):
        raise TypeError(f"{what} must be an integer count, not {type(x).__name__}")
    return operator.index(x)


def _count(x: Any, what: str) -> int:
    v = _int(x, what)
    if v < 0:
        raise ValueError(f"{what} must be >= 0, got {v}")
    return v


def _pmf_num(i: int, n: int, a: int, b: int) -> int:
    # numerator of P(X = i) over b**n, p = a/b
    return comb(n, i) * a ** i * (b - a) ** (n - i)


def binom_sf(k: int, n: int, p: Any) -> Fraction:
    """Exact P(X >= k), X ~ Binomial(n, p). k <= 0 gives 1, k > n gives 0."""
    p = _prob(p, "p")
    n = _count(n, "n")
    k = _int(k, "k")
    if k <= 0:
        return Fraction(1)
    if k > n:
        return Fraction(0)
    a, b = p.numerator, p.denominator
    bn = b ** n
    if k < n - k + 1:   # the lower tail has fewer terms: 1 - P(X <= k - 1)
        return Fraction(bn - sum(_pmf_num(i, n, a, b) for i in range(0, k)), bn)
    return Fraction(sum(_pmf_num(i, n, a, b) for i in range(k, n + 1)), bn)


def _check_kn(k: Any, n: Any) -> tuple[int, int]:
    k, n = _count(k, "k"), _count(n, "n")
    if k > n:
        raise ValueError(f"count {k} exceeds its denominator {n}")
    return k, n


def fires(k: int, n: int, p0: Any, alpha: Any) -> bool:
    """The firing rule of m:271: exact one-sided P(X >= k | n, p0) <= alpha."""
    k, n = _check_kn(k, n)
    return binom_sf(k, n, p0) <= _prob(alpha, "alpha")


def critical_k(n: int, p0: Any, alpha: Any) -> int | None:
    """Smallest k with P(X >= k | n, p0) <= alpha; None if no k <= n fires.

    Ascending pass on the CDF (O(crit) terms): crit = j + 1 for the first j with
    P(X <= j) >= 1 - alpha, all in integers over b**n."""
    n = _count(n, "n")
    p, al = _prob(p0, "p0"), _prob(alpha, "alpha")
    a, b = p.numerator, p.denominator
    bn, ad, an = b ** n, al.denominator, al.numerator
    s = 0
    for j in range(0, n + 1):
        s += _pmf_num(j, n, a, b)
        if s * ad >= (ad - an) * bn:
            return j + 1 if j + 1 <= n else None
    return None


def realised_table(p0: Any, alpha: Any, n_max: int) -> list[tuple[int, int, int | None]]:
    """Critical count by realised n, 1..n_max, merged into (n_lo, n_hi, crit) runs
    (crit None = unreachable). The table a LOCK declares beside the planned n."""
    n_max = _count(n_max, "n_max")
    if n_max < 1:
        raise ValueError("n_max must be >= 1")
    out: list[tuple[int, int, int | None]] = []
    lo, cur = 1, critical_k(1, p0, alpha)
    for n in range(2, n_max + 1):
        c = critical_k(n, p0, alpha)
        if c != cur:
            out.append((lo, n - 1, cur))
            lo, cur = n, c
    out.append((lo, n_max, cur))
    return out


def fisher_sf(a: int, n1: int, c: int, n2: int) -> Fraction:
    """One-sided Fisher exact, excess in the first group, (successes, total) form:
    P(X >= a) under the hypergeometric with margins n1, n2 and a + c successes.
    Same quantity as ``session.fisher_two_groups(a, n1, c, n2)`` and f1's
    ``fisher_one_sided(a, n1, c, n2)`` (f_sessions.py:154-159), exactly."""
    a, n1 = _check_kn(a, n1)
    c, n2 = _check_kn(c, n2)
    k = a + c
    return Fraction(sum(comb(n1, i) * comb(n2, k - i) for i in range(a, min(n1, k) + 1)),
                    comb(n1 + n2, k))


def fisher_fires(a: int, n1: int, c: int, n2: int, alpha: Any) -> bool:
    return fisher_sf(a, n1, c, n2) <= _prob(alpha, "alpha")


def _dec(x: Fraction, places: int = 4) -> str:
    """Exact half-up decimal display of a non-negative Fraction (no float even
    for printing)."""
    # PIN (Code, declared at LOCK v0.1): printed P values are the exact Fraction
    # rounded half-up to 4 places; the comparison itself is always exact.
    scale = 10 ** places
    v = (x * scale * 2 + 1) // 2
    whole, frac = divmod(int(v), scale)
    return f"{whole}.{frac:0{places}d}"


# --- sequential false pause (§6, G-PWR) ---------------------------------------
def seq_false_pause(ns: Sequence[int], p0: Any, alpha: Any) -> Fraction:
    """Exact P(some look j has cumulative count >= crit(n_j)) under Binomial
    increments at p = p0, looks at cumulative n_1 <= n_2 <= ... (m:330, m:285).

    Dynamic programme over the surviving cumulative counts in integers over
    b**n; each look truncates the mass at or above its own critical count."""
    # PIN (Code, declared at LOCK v0.1): n_j is the caller's input. The spec gives
    # no model for the realised rounds per look (sessions end early; the sham arm
    # leaves the rotation at its floor: maps/stats.md §6 item 9), so G-PWR states
    # its n_j assumption beside the figure. A repeated n_j (an end look that
    # coincides with a 40-multiple) is allowed and adds nothing.
    looks = [_count(x, "n_j") for x in ns]
    if not looks:
        raise ValueError("seq_false_pause needs at least one look")
    if any(y < x for x, y in zip(looks, looks[1:])):
        raise ValueError(f"looks must be non-decreasing cumulative n: {looks}")
    p, al = _prob(p0, "p0"), _prob(alpha, "alpha")
    a, b = p.numerator, p.denominator
    dist: dict[int, int] = {0: 1}
    prev = 0
    for n in looks:
        crit = critical_k(n, p, al)
        m = n - prev
        if m:
            inc = [_pmf_num(i, m, a, b) for i in range(m + 1)]
            nd: dict[int, int] = {}
            for s, w in dist.items():
                for i, wi in enumerate(inc):
                    t = s + i
                    if crit is not None and t >= crit:
                        continue
                    nd[t] = nd.get(t, 0) + w * wi
            dist = nd
        elif crit is not None:
            dist = {s: w for s, w in dist.items() if s < crit}
        prev = n
    return 1 - Fraction(sum(dist.values()), b ** prev)


# --- bars ---------------------------------------------------------------------
@dataclass(frozen=True)
class BarResult:
    name: str
    fired: bool                  # the binding decision (False always on a reported-only bar)
    k: int
    n: int
    p: Fraction | None
    crit: int | None
    message: str
    binding: bool = True
    exceeds: bool = False        # the P <= alpha (or k >= 1) outcome, recorded either way

    def as_dict(self) -> dict:
        return {"name": self.name, "fired": self.fired, "k": self.k, "n": self.n,
                "p": None if self.p is None else f"{self.p.numerator}/{self.p.denominator}",
                "crit": self.crit, "message": self.message, "binding": self.binding,
                "exceeds": self.exceeds}


@dataclass(frozen=True)
class Bar:
    """One declared bar. DESIGN.md §1.6's eight fields first (positional form
    kept); the rest are m's declaration fields, all defaulted."""
    name: str
    kind: str
    p0: str | Fraction | None = None
    alpha: str | Fraction = "0.05"
    domain: str = ""
    unit: str = ""
    cadence: str = ""
    justification: str = ""
    # PIN (Code, declared at LOCK v0.1): declaration fields beyond DESIGN.md's
    # eight -- stage (keys' vocabulary), scope (the m unit), substrate, numerator
    # (what k counts), binding (False = reported only), on_fire, planned_n and
    # planned_crit (asserted at declaration against the exact critical count).
    stage: str = ""
    scope: str = ""
    substrate: str = ""
    numerator: str = ""
    binding: bool = True
    on_fire: str = ""
    planned_n: int | None = None
    planned_crit: int | None = None

    def __post_init__(self) -> None:
        if self.kind not in KINDS:
            raise ValueError(f"{self.name}: unknown bar kind {self.kind!r}")
        if self.domain not in DOMAINS:
            raise ValueError(f"{self.name}: unknown domain {self.domain!r}; one of {tuple(DOMAINS)}")
        if self.domain not in _KIND_DOMAINS[self.kind]:
            raise ValueError(f"{self.name}: a {self.kind} bar's domain must be one of "
                             f"{_KIND_DOMAINS[self.kind]}, got {self.domain!r}")
        if self.kind in _ONE_CLAIM and not self.justification.strip():
            # mirrors session.Tripwire; PIN (Code, declared at LOCK v0.1): the pause
            # is a one-claim trigger too, so it carries the same refusal (m:271
            # licenses it only because both classes are ~zero-base-rate there).
            raise ValueError(
                f"{self.name}: hair-trigger bars are licensed only for "
                f"~zero-base-rate defect classes (rule 21) -- state the "
                f"justification at declaration")
        if self.kind == "hair_trigger" and not self.binding:
            raise ValueError(f"{self.name}: a hair trigger that does not stop is not a hair trigger")
        if self.kind in _BINOMIAL:
            if self.p0 is None:
                raise ValueError(f"{self.name}: binomial bar needs a declared p0")
            _prob(self.p0, f"{self.name} p0")
        elif self.p0 is not None:
            raise ValueError(f"{self.name}: a {self.kind} bar takes no p0")
        _prob(self.alpha, f"{self.name} alpha")
        if self.stage not in STAGES:
            raise ValueError(f"{self.name}: stage must be one of {STAGES}, got {self.stage!r}")
        if self.substrate not in ("qwen", "olmo"):
            raise ValueError(f"{self.name}: substrate must be qwen or olmo")
        if self.scope not in keys.UNITS_BUILT or (self.scope == "Q-F0") != (self.substrate == "qwen"):
            raise ValueError(f"{self.name}: scope {self.scope!r} does not fit substrate {self.substrate!r}")
        if self.planned_n is not None:
            want = (critical_k(self.planned_n, self.p0, self.alpha) if self.kind in _BINOMIAL
                    else (1 if self.planned_n >= 1 else None))
            if self.planned_crit != want:
                raise ValueError(f"{self.name}: declared critical {self.planned_crit} at n = "
                                 f"{self.planned_n}, exact critical is {want}")
        elif self.planned_crit is not None:
            raise ValueError(f"{self.name}: a planned critical count needs its planned n")

    @property
    def cls(self) -> str:
        return self.name.split("@", 1)[0]

    @property
    def p0q(self) -> Fraction | None:
        return None if self.p0 is None else q(self.p0)

    @property
    def alphaq(self) -> Fraction:
        return q(self.alpha)

    def as_dict(self) -> dict:
        """The LOCK declaration row (m:279): class, unit, p0, alpha, domain, cadence."""
        d = {"name": self.name, "class": self.cls, "kind": self.kind, "stage": self.stage,
             "scope": self.scope, "substrate": self.substrate,
             "p0": None if self.p0 is None else str(self.p0), "alpha": str(self.alpha),
             "domain": self.domain, "domain_text": DOMAINS[self.domain], "unit": self.unit,
             "cadence": self.cadence, "numerator": self.numerator, "binding": self.binding,
             "on_fire": self.on_fire, "justification": self.justification,
             "planned_n": self.planned_n, "planned_crit": self.planned_crit}
        if self.kind == "binomial_stage_end" and self.planned_n:
            d["realised_table"] = [list(r) for r in realised_table(self.p0, self.alpha, self.planned_n)]
        return d

    def _check_ctx(self, ctx: dict) -> tuple[str | None, str | None, Any]:
        extra = set(ctx) - {"template", "phase", "look", "sham_k", "sham_n"}
        if extra:
            raise TypeError(f"{self.name}: unknown evaluation context {sorted(extra)}")
        if self.kind != "guard_fisher" and ({"sham_k", "sham_n"} & set(ctx)):
            raise TypeError(f"{self.name}: sham counts are the Fisher guard's only")
        template, phase, look = ctx.get("template"), ctx.get("phase"), ctx.get("look")
        if template is not None:
            if template not in keys.templates(self.scope):
                raise ValueError(f"{self.name}: template {template!r} is not a {self.scope} template")
            contrast = keys.is_contrast(template)
            if self.domain in ("sham", "pairs") and contrast:
                raise ValueError(f"{self.name}: DOMAIN VIOLATION: a contrast-template session "
                                 f"on a sham-only bar (m:271)")
            if self.domain == "contrast_arm" and not contrast:
                raise ValueError(f"{self.name}: the guard is evaluated per contrast arm (m:316)")
        if phase is not None:
            if self.kind not in _ONE_CLAIM:
                raise ValueError(f"{self.name}: a {self.kind} bar is evaluated over a domain, not a phase")
            if phase not in ("forced", "free"):
                raise ValueError(f"{self.name}: phase must be forced or free, got {phase!r}")
        if look is not None:
            if self.kind not in ("binomial_look", "guard_fisher", "guard_abs"):
                raise ValueError(f"{self.name}: a {self.kind} bar has no looks")
            if look != "end" and not (isinstance(look, int) and not isinstance(look, bool) and look >= 1):
                raise ValueError(f"{self.name}: look must be an int >= 1 or 'end', got {look!r}")
        return template, phase, look

    def evaluate(self, k: int, n: int, **ctx) -> BarResult:
        """Evaluate on (k, n). ctx: template, phase (hair/pause only), look (look
        and guard bars), sham_k and sham_n (Fisher guard: the matched sham arm's
        pre-pick exclusions and launches)."""
        template, phase, look = self._check_ctx(ctx)
        k, n = _check_kn(k, n)
        p: Fraction | None = None
        crit: int | None = None
        c = n2 = None
        if self.kind in _ONE_CLAIM:
            # PIN (Code, declared at LOCK v0.1): fires iff k >= 1 (e2d's threshold
            # 0.0 form, k/n > 0); n is the units observed.
            exceeds, crit = k >= 1, 1
        elif self.kind == "guard_fisher":
            if "sham_k" not in ctx or "sham_n" not in ctx:
                raise TypeError(f"{self.name}: the Fisher guard needs sham_k and sham_n")
            c, n2 = _check_kn(ctx["sham_k"], ctx["sham_n"])
            # PIN (Code, declared at LOCK v0.1): armed at every look with no minimum
            # sham n (m:316 "at every look"; f1's sh_n >= 12, f_sessions.py:408, is
            # not carried); n = sessions launched in the arm through the look, k =
            # its pre-pick exclusions; excess tested in the contrast arm; no single
            # critical count exists (it moves with the sham count), so crit is None.
            p = fisher_sf(k, n, c, n2)
            exceeds = p <= self.alphaq
        else:
            p = binom_sf(k, n, self.p0q)
            exceeds = p <= self.alphaq
            crit = critical_k(n, self.p0q, self.alphaq)
        fired = bool(exceeds and self.binding)
        return BarResult(self.name, fired, k, n, p, crit,
                         self._message(fired, exceeds, k, n, p, crit, c, n2, template, phase, look),
                         binding=self.binding, exceeds=bool(exceeds))

    def _message(self, fired, exceeds, k, n, p, crit, c, n2, template, phase, look) -> str:
        if self.binding:
            status = "FIRED" if fired else "silent"
        else:
            status = "reported (exceeds; not binding)" if exceeds else "reported (silent; not binding)"
        parts = [f"BAR {self.name} {status}"]
        if template is not None:
            parts.append(f"template={template}")
        if phase is not None:
            parts.append(f"phase={phase}")
        if look is not None:
            parts.append(f"look={look}")
        cmp = "<=" if exceeds else ">"
        if self.kind in _ONE_CLAIM:
            # PIN (Code, declared at LOCK v0.1): a hair trigger's or the pause's
            # message carries no count -- a count or n fired in a contrast free round
            # could locate the round (m:263, m:271; maps/stats.md §6 item 6).
            pass
        elif self.kind == "guard_fisher":
            parts.append(f"contrast {k}/{n} vs sham {c}/{n2} one-sided Fisher P={_dec(p)} "
                         f"{cmp} alpha {self.alpha}")
        else:
            parts.append(f"{k}/{n} exact one-sided P={_dec(p)} {cmp} alpha {self.alpha} "
                         f"vs p0 {self.p0}; critical "
                         f"{'unreachable' if crit is None else crit} at n={n}")
        return " ".join(parts)


# --- the declarations ------------------------------------------------------------
_CADENCE_HAIR = ("evaluated as each generation / session is recorded; a fire anywhere "
                 "stops the stage (m:271)")
_CADENCE_END = "once at stage end on the realised n; no mid-stage evaluation (m:271)"
_CADENCE_LOOK = ("every 40 launches and at the end, cumulative count, alpha .05 per look, "
                 "no alpha spending; look index in the resume identity (m:330)")
_CADENCE_GUARD = "at every look, per contrast arm (m:316)"
_STOP = "STOP the stage (m:271)"
_PAUSE = "PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316)"

_JUST_SCAFFOLD = {
    "qwen": "A string of Qwen's scaffold set (the e2a ban list as e2d.config loads it, m:261; "
            "pinned by sha at LOCK-m-F0 v0.1) in model-generated text means the ban did not apply "
            "at generation; the tokens are suppressed in the sampler, so the base rate is "
            "structurally zero (e2d.config.declared_bars' justification, carried).",
    "olmo": "A case-sensitive match of one of the six strings of b3's ban list (m:262), asserted "
            "equal to the ban-list strings and to b3's id sha16 at startup, in model-generated "
            "text; the sampler's ban suppresses them, so the base rate is ~zero.",
}
_JUST_BREAKAGE = ("Harness bytes that fail G-VER (m:284): the harness writes every scaffold byte "
                  "itself, so a session whose bytes do not reconstruct from its recorded fields, "
                  "the committed schedule and the rng streams is a build defect; base rate zero "
                  "by construction.")
_JUST_MISMATCH = ("Pair, map, start order, clause order, banner bytes or item stream differing "
                  "from the committed schedule (m:271, m:253): the schedule is a committed file "
                  "and every stream a deterministic key, so the base rate is zero by construction.")
_JUST_GID = ("G-ID's criterion is 2/2 byte-identical cached/uncached transcript pairs, declared a "
             "hair trigger at m:281: identity is the criterion itself, so no divergence rate is "
             "tolerated.")
_JUST_PAUSE = ("On OLMo a session ends at its first claim (m:262), so the one-session G-TIME bar's "
               "critical 2 is unreachable past round 2 (STOP-7 A'3); both numerator classes are "
               "~zero-base-rate there (AuditSpec 0/756 on b3's shams; echo a verbatim reproduction "
               "of a harness line, its final period aside where OLMo's newline stop drops it -- "
               "audit.harness_echo's PIN), which licenses a one-claim pause (m:271, m:302).")
_JUST_DEGEN = {
    "qwen": "Measured class: v2-or-echo has a measured rate (v2 17/597 on f1's CORR rounds, 11/351 "
            "on its SHAM pool [C]), so rule 21 binds it by exact binomial; p0 .05 is a declared "
            "tolerance at a named, changed contrast (m:271).",
    "olmo": "b3's declared p0 .02 on its AuditSpec-only numerator (0/756 on b3's shams [C]); m adds "
            "the echo class, so p0 is a declared tolerance at a named, changed contrast (m:271, "
            "m:262).",
}
_UNIT_ROUNDS = "task round generated (<= 10 per session: 4 forced + 6 free)"
_NUM_DEGEN = {"qwen": "rounds claimed by audit v2 or m's harness-echo class (m:261)",
              "olmo": "rounds claimed by b3's AuditSpec or m's harness-echo class (m:262)"}
_UNIT_GUARD = "session launched in the arm through the look (pre-pick exclusion)"
_NUM_GUARD = "pre-pick exclusions (sessions excluded before their first read, m:308)"


def _hair_triggers(scope: str, substrate: str) -> list[Bar]:
    return [
        Bar("scaffold_absorption", "hair_trigger", domain="every",
            unit="model generation (round)", cadence=_CADENCE_HAIR,
            justification=_JUST_SCAFFOLD[substrate], stage="every", scope=scope,
            substrate=substrate, numerator="generations containing a scaffold-set string",
            on_fire=_STOP),
        Bar("template_breakage", "hair_trigger", domain="every", unit="session",
            cadence=_CADENCE_HAIR, justification=_JUST_BREAKAGE, stage="every", scope=scope,
            substrate=substrate, numerator="sessions failing G-VER", on_fire=_STOP),
        Bar("schedule_mismatch", "hair_trigger", domain="every", unit="session",
            cadence=_CADENCE_HAIR, justification=_JUST_MISMATCH, stage="every", scope=scope,
            substrate=substrate, numerator="sessions differing from the committed schedule",
            on_fire=_STOP),
    ]


def _degen(stage_word: str, stage_name: str, scope: str, substrate: str, p0: str,
           planned_n: int, planned_crit: int, on_fire: str) -> Bar:
    return Bar(f"round_degeneracy@{stage_name}", "binomial_stage_end", p0=p0, alpha="0.05",
               domain="sham", unit=_UNIT_ROUNDS, cadence=_CADENCE_END,
               justification=_JUST_DEGEN[substrate], stage=stage_word, scope=scope,
               substrate=substrate, numerator=_NUM_DEGEN[substrate], on_fire=on_fire,
               planned_n=planned_n, planned_crit=planned_crit)


def _campaign(scope: str, substrate: str, p0: str, abs_binding: bool) -> list[Bar]:
    tag = f"campaign-{scope}"
    return [
        Bar(f"round_degeneracy@{tag}", "binomial_look", p0=p0, alpha="0.05", domain="sham",
            unit=_UNIT_ROUNDS, cadence=_CADENCE_LOOK, justification=_JUST_DEGEN[substrate],
            stage="campaign", scope=scope, substrate=substrate, numerator=_NUM_DEGEN[substrate],
            on_fire=_PAUSE),
        Bar(f"exclusion_guard_fisher@{tag}", "guard_fisher", alpha="0.05", domain="contrast_arm",
            unit=_UNIT_GUARD, cadence=_CADENCE_GUARD,
            justification="Adapted from f1's guard (archive:400-402): pre-pick exclusion rate vs "
                          "the matched sham by one-sided Fisher exact, binding on both substrates "
                          "(m:316).",
            stage="campaign", scope=scope, substrate=substrate, numerator=_NUM_GUARD,
            on_fire=_PAUSE),
        # PIN (Code, declared at LOCK v0.1): on OLMo the absolute bar is declared with
        # binding=False -- evaluated against the same .20 and recorded (exceeds), its
        # `fired` always False (m:316 "reported only").
        Bar(f"exclusion_guard_abs@{tag}", "guard_abs", p0="0.20", alpha="0.05",
            domain="contrast_arm", unit=_UNIT_GUARD, cadence=_CADENCE_GUARD,
            justification=("f1's whole-session reference .20 at F0 (archive:400-402) carried to "
                           "m's pre-pick unit: a declared tolerance at a named, changed contrast "
                           "(m:316)." + ("" if abs_binding else " Reported only on OLMo: b3's "
                                         "exclusions are dominated by the lexical class m "
                                         "declines to bar.")),
            stage="campaign", scope=scope, substrate=substrate, numerator=_NUM_GUARD,
            binding=abs_binding, on_fire=_PAUSE if abs_binding else "none (reported only, m:316)"),
    ]


def _qf0_bars() -> tuple[Bar, ...]:
    s, sub = "Q-F0", "qwen"
    return tuple(_hair_triggers(s, sub) + [
        _degen("time", "G-TIME-F0", s, sub, "0.05", 10, 3,
               "STOP before G-ID-F0m (m:280). One-session boundary disclosed: a forced claim at "
               "rounds 2-4 ends the session at n 2-4 (critical 2) and is reported, not fired; a "
               "round-1 claim fires at P = .05 = alpha (m:271)"),
        # PIN (Code, declared at LOCK v0.1): G-ID-F0m's 2/2 criterion, which m:281
        # calls a hair trigger, is declared as `gid_divergence` (unit: a complete
        # cached/uncached pair); a fire ends G-ID with FAIL and sends Q-F0 uncached
        # (its floors to the uncached column) -- not a STOP of the unit.
        Bar("gid_divergence@G-ID-F0m", "hair_trigger", domain="pairs",
            unit="complete cached/uncached A0s pair (4 forced rounds + 6 reads each)",
            cadence="per complete pair, uncached first; stops at the first divergence (m:281)",
            justification=_JUST_GID, stage="id", scope=s, substrate=sub,
            numerator="complete pairs whose transcripts differ in any byte",
            on_fire="G-ID FAIL: Q-F0 runs uncached (m:281)"),
        _degen("qual", "G-F0m-Qwen", s, sub, "0.05", 160, 14,
               "STOP: Q-F0 does not run until the seat re-specifies (m:283)"),
    ] + _campaign(s, sub, "0.05", abs_binding=True))


#: Q-F0's declared bars (m:271, m:280, m:281, m:283, m:316, m:330).
QF0_BARS: tuple[Bar, ...] = _qf0_bars()


def OLMO_BARS(ckpt: str) -> tuple[Bar, ...]:
    """One OLMo checkpoint's declared bars (m:271, m:262, m:302, m:316, m:330)."""
    if ckpt not in keys.CKPTS:
        raise ValueError(f"OLMo checkpoint must be one of {keys.CKPTS} (base has no told control, "
                         f"decision (7')), got {ckpt!r}")
    s, sub = f"OLMo-{ckpt}", "olmo"
    t = f"G-TIME-OLMo-{ckpt}"
    return tuple(_hair_triggers(s, sub) + [
        # m:302 says "critical 2, reachable only at a realised n <= 2"; exactly, the
        # critical count is 1 at n <= 2 and 2 from n = 3, where one claim cannot
        # reach it (maps/stats.md §6 item 4): one claim in round 1 or 2 fires.
        _degen("time", t, s, sub, "0.02", 10, 2,
               f"STOP before G-F0m-OLMo-{ckpt} (m:302). Fires only on a claim in round 1 or 2 "
               "(critical 1 at n <= 2)"),
        # PIN (Code, declared at LOCK v0.1): a round-1 or round-2 claim fires both the
        # bar (STOP) and the pause; both are recorded, the STOP governs (maps/stats.md
        # §6 item 5). The pause is evaluated at stage end, before G-F0m-OLMo.
        Bar(f"gtime_pause@{t}", "pause", domain="sham",
            unit="task round of the G-TIME-OLMo sham session",
            cadence="at stage end, before that checkpoint's qualification (m:302)",
            justification=_JUST_PAUSE, stage="time", scope=s, substrate=sub,
            numerator=_NUM_DEGEN[sub],
            on_fire="PAUSE for the seat's adjudication before G-F0m-OLMo; recorded, not a "
                    "verdict (m:271)"),
        _degen("qual", f"G-F0m-OLMo-{ckpt}", s, sub, "0.02", 160, 7,
               f"STOP: OLMo-{ckpt} does not run until the seat re-specifies (m:302)"),
    ] + _campaign(s, sub, "0.02", abs_binding=False))


def _all_declared() -> dict[str, Bar]:
    out = {b.name: b for b in QF0_BARS}
    for c in keys.CKPTS:
        out.update({b.name: b for b in OLMO_BARS(c)})
    return out


# --- firing cases (rule 21; trap 5) --------------------------------------------------
# A case is (target, k, n, should, extra). target: a bar name (evaluated through
# Bar.evaluate with extra["ctx"]; `should` is the P <= alpha / k >= 1 outcome,
# i.e. BarResult.exceeds), ("exact", p0, alpha), ("fisher", alpha) with
# extra {"c", "n2"}, or ("refuse", p0, alpha) where `should` = must raise
# TypeError. extra may carry "p" (exact "num/den"), "p4" (4-place display) and
# "crit" (expected critical count, None = unreachable).

def _hair_cases() -> list[tuple]:
    return [("scaffold_absorption", 1, 1, True, {}), ("scaffold_absorption", 0, 1, False, {}),
            ("scaffold_absorption", 1, 80, True, {}), ("scaffold_absorption", 0, 80, False, {}),
            ("template_breakage", 1, 8, True, {}), ("template_breakage", 0, 8, False, {}),
            ("schedule_mismatch", 1, 1, True, {}), ("schedule_mismatch", 0, 24, False, {})]


def _guard_cases(tag: str, abs_names: str) -> list[tuple]:
    f = f"exclusion_guard_fisher@{tag}"
    return [
        (f, 3, 3, True, {"ctx": {"sham_k": 0, "sham_n": 3}, "p": "1/20"}),
        (f, 1, 1, True, {"ctx": {"sham_k": 0, "sham_n": 19}, "p": "1/20"}),
        (f, 2, 3, False, {"ctx": {"sham_k": 0, "sham_n": 3}, "p": "1/5"}),
        (f, 5, 20, True, {"ctx": {"sham_k": 0, "sham_n": 20}, "p4": "0.0236"}),
        (f, 4, 20, False, {"ctx": {"sham_k": 0, "sham_n": 20}, "p4": "0.0530"}),
        (abs_names, 2, 2, True, {"p": "1/25", "crit": 2}),
        (abs_names, 1, 2, False, {"crit": 2}),
        (abs_names, 5, 10, True, {"p4": "0.0328", "crit": 5}),
        (abs_names, 4, 10, False, {"p4": "0.1209", "crit": 5}),
    ]


def _qf0_cases() -> list[tuple]:
    t, g, c = "round_degeneracy@G-TIME-F0", "round_degeneracy@G-F0m-Qwen", "campaign-Q-F0"
    return _hair_cases() + [
        ("gid_divergence@G-ID-F0m", 1, 1, True, {}), ("gid_divergence@G-ID-F0m", 0, 2, False, {}),
        (t, 1, 1, True, {"p": "1/20", "crit": 1}),          # the disclosed n = 1 tie (m:271)
        (t, 0, 1, False, {}),
        (t, 1, 2, False, {"crit": 2}), (t, 1, 4, False, {"crit": 2}),   # rounds 2-4: reported
        (t, 2, 7, True, {"crit": 2}), (t, 2, 8, False, {"crit": 3}),
        (t, 3, 10, True, {"p4": "0.0115", "crit": 3}), (t, 2, 10, False, {"p4": "0.0861"}),
        (g, 14, 160, True, {"p4": "0.0305", "crit": 14}), (g, 13, 160, False, {"p4": "0.0589"}),
        (g, 13, 155, True, {"crit": 13}),
        (f"round_degeneracy@{c}", 16, 200, True, {"crit": 16}),
        (f"round_degeneracy@{c}", 15, 200, False, {}),
        (f"round_degeneracy@{c}", 117, 2000, True, {"crit": 117}),
        (f"round_degeneracy@{c}", 116, 2000, False, {}),
    ] + _guard_cases(c, f"exclusion_guard_abs@{c}")


def _olmo_cases(ckpt: str) -> list[tuple]:
    t = f"round_degeneracy@G-TIME-OLMo-{ckpt}"
    pz = f"gtime_pause@G-TIME-OLMo-{ckpt}"
    g = f"round_degeneracy@G-F0m-OLMo-{ckpt}"
    c = f"campaign-OLMo-{ckpt}"
    return [
        (t, 1, 1, True, {"p": "1/50", "crit": 1}), (t, 1, 2, True, {"p4": "0.0396", "crit": 1}),
        (t, 1, 3, False, {"p4": "0.0588", "crit": 2}), (t, 1, 10, False, {"crit": 2}),
        (t, 2, 10, True, {"p4": "0.0162", "crit": 2}), (t, 0, 2, False, {}),
        (pz, 1, 3, True, {}), (pz, 1, 10, True, {}), (pz, 0, 10, False, {}), (pz, 0, 1, False, {}),
        (g, 7, 160, True, {"p4": "0.0429", "crit": 7}), (g, 6, 160, False, {"p4": "0.1033"}),
        (f"round_degeneracy@{c}", 8, 200, True, {"crit": 8}),
        (f"round_degeneracy@{c}", 7, 200, False, {}),
        (f"round_degeneracy@{c}", 52, 2000, True, {"crit": 52}),
        (f"round_degeneracy@{c}", 51, 2000, False, {}),
    ] + _guard_cases(c, f"exclusion_guard_abs@{c}")


def _exact(p0, k, n, should, alpha="0.05", **extra) -> tuple:
    return (("exact", p0, alpha), k, n, should, extra)


#: The mandatory verify table of maps/stats.md §8 (and its n = 2000 / float rows).
MANDATORY_CASES: tuple[tuple, ...] = (
    _exact("0.05", 1, 1, True, p="1/20", crit=1),
    _exact("0.05", 0, 1, False),
    _exact("0.10", 1, 1, False, crit=None),
    _exact("0.02", 1, 2, True, p4="0.0396"),
    _exact("0.02", 1, 3, False, p4="0.0588"),
    _exact("0.05", 3, 10, True, p4="0.0115"),
    _exact("0.05", 2, 10, False, p4="0.0861"),
    _exact("0.05", 2, 7, True),
    _exact("0.05", 2, 8, False),
    _exact("0.05", 14, 160, True, p4="0.0305"),
    _exact("0.05", 13, 160, False, p4="0.0589"),
    _exact("0.05", 13, 155, True),
    _exact("0.02", 7, 160, True, p4="0.0429"),
    _exact("0.02", 6, 160, False),
    (("fisher", "0.05"), 3, 3, True, {"c": 0, "n2": 3, "p": "1/20"}),
    (("fisher", "0.05"), 1, 1, True, {"c": 0, "n2": 19, "p": "1/20"}),
    _exact("0.05", 117, 2000, True, crit=117),       # n = 2,000: exact, no overflow
    _exact("0.05", 116, 2000, False),
    (("refuse", 0.05, "0.05"), 1, 1, True, {}),     # float p0 -> TypeError
    (("refuse", "0.05", 0.05), 1, 1, True, {}),     # float alpha -> TypeError
    (("refuse", "0.05", "0.05"), 1, 1, False, {}),  # declared strings accepted
)

#: m:271's eight critical counts for the planned sham domains (P at crit and at
#: crit - 1), and the verdict counts at p0 .5 (maps/stats.md §5).
SPEC_COUNT_CASES: tuple[tuple, ...] = (
    _exact("0.05", 14, 160, True, p4="0.0305", crit=14), _exact("0.05", 13, 160, False, p4="0.0589"),
    _exact("0.02", 7, 160, True, p4="0.0429", crit=7), _exact("0.02", 6, 160, False, p4="0.1033"),
    _exact("0.05", 19, 240, True, p4="0.0336", crit=19), _exact("0.05", 18, 240, False, p4="0.0581"),
    _exact("0.10", 22, 144, True, p4="0.0296", crit=22), _exact("0.10", 21, 144, False, p4="0.0507"),
    _exact("0.05", 3, 10, True, p4="0.0115", crit=3), _exact("0.05", 2, 10, False, p4="0.0861"),
    _exact("0.02", 2, 10, True, p4="0.0162", crit=2), _exact("0.02", 1, 10, False, p4="0.1829"),
    _exact("0.05", 5, 30, True, p4="0.0156", crit=5), _exact("0.05", 4, 30, False, p4="0.0608"),
    _exact("0.10", 5, 18, True, p4="0.0282", crit=5), _exact("0.10", 4, 18, False, p4="0.0982"),
    _exact("0.5", 87, 144, True, alpha="0.01", crit=87), _exact("0.5", 86, 144, False, alpha="0.01"),
    _exact("0.5", 83, 144, True, crit=83), _exact("0.5", 82, 144, False),
    _exact("0.5", 60, 96, True, alpha="0.01", crit=60), _exact("0.5", 59, 96, False, alpha="0.01"),
    _exact("0.5", 51, 80, True, alpha="0.01", crit=51), _exact("0.5", 50, 80, False, alpha="0.01"),
)

#: Every bar of every built unit in both directions, plus the mandatory table and
#: the spec's counts.
FIRING_CASES: tuple[tuple, ...] = tuple(
    _qf0_cases() + [cs for ck in keys.CKPTS for cs in _olmo_cases(ck)]
    + list(MANDATORY_CASES) + list(SPEC_COUNT_CASES))


def _unpack(case: tuple) -> tuple[Any, int, int, bool, dict]:
    if len(case) == 4:
        target, k, n, should = case
        return target, k, n, bool(should), {}
    if len(case) == 5:
        target, k, n, should, extra = case
        return target, k, n, bool(should), dict(extra)
    raise ValueError(f"a firing case is (target, k, n, should[, extra]): {case!r}")


def _expect(tag: str, extra: dict, p: Fraction | None, crit: Any, has_crit: bool) -> list[str]:
    out = []
    if "p" in extra and (p is None or p != Fraction(extra["p"])):
        out.append(f"{tag}: P = {p}, expected {extra['p']}")
    if "p4" in extra and (p is None or _dec(p) != extra["p4"]):
        out.append(f"{tag}: P = {None if p is None else _dec(p)}, expected {extra['p4']}")
    if has_crit and "crit" in extra and crit != extra["crit"]:
        out.append(f"{tag}: critical {crit}, expected {extra['crit']}")
    return out


def verify_firing(bars: Iterable[Bar], cases: Iterable[tuple]) -> list[str]:
    """No-model firing check (rule 21). Returns failures; [] = every case behaved.

    A case naming a bar of another built unit is skipped (it is that unit's); a
    case naming a bar declared nowhere is a failure; arithmetic cases always run."""
    bars = tuple(bars)
    by_name = {b.name: b for b in bars}
    fails: list[str] = []
    if len(by_name) != len(bars):
        fails.append("duplicate bar names in the declared set")
    known = _all_declared()
    for case in cases:
        target, k, n, should, extra = _unpack(case)
        tag = f"{target} {k}/{n}"
        try:
            if isinstance(target, str):
                if target not in by_name:
                    if target not in known:
                        fails.append(f"{target}: no such bar declared")
                    continue
                bar = by_name[target]
                r = bar.evaluate(k, n, **extra.get("ctx", {}))
                if r.exceeds != should:
                    fails.append(f"{tag}: {'exceeded' if r.exceeds else 'stayed silent'}, "
                                 f"expected {'fire' if should else 'no fire'}")
                if r.fired != (r.exceeds and bar.binding):
                    fails.append(f"{tag}: fired={r.fired} on a bar with binding={bar.binding}")
                fails += _expect(tag, extra, r.p, r.crit, bar.kind in _BINOMIAL or bar.kind in _ONE_CLAIM)
            elif target[0] == "exact":
                _, p0, alpha = target
                got = fires(k, n, p0, alpha)
                if got != should:
                    fails.append(f"exact p0 {p0} {tag}: fires={got}, expected {should}")
                fails += _expect(f"exact p0 {p0} {k}/{n}", extra, binom_sf(k, n, p0),
                                 critical_k(n, p0, alpha), True)
            elif target[0] == "fisher":
                _, alpha = target
                got = fisher_fires(k, n, extra["c"], extra["n2"], alpha)
                if got != should:
                    fails.append(f"fisher {tag} vs {extra['c']}/{extra['n2']}: fires={got}, "
                                 f"expected {should}")
                fails += _expect(f"fisher {tag}", extra, fisher_sf(k, n, extra["c"], extra["n2"]),
                                 None, False)
            elif target[0] == "refuse":
                _, p0, alpha = target
                try:
                    fires(k, n, p0, alpha)
                    raised = False
                except TypeError:
                    raised = True
                if raised != should:
                    fails.append(f"refuse p0={p0!r} alpha={alpha!r}: raised={raised}, expected {should}")
            else:
                fails.append(f"unknown case target {target!r}")
        except Exception as e:   # a case that cannot run is a failure, never a pass (trap 5)
            fails.append(f"{tag}: raised {type(e).__name__}: {e}")
    return fails


def assert_firing_complete(bars: Iterable[Bar], cases: Iterable[tuple]) -> tuple[Bar, ...]:
    """format_recon's ``bars_or_stop`` pattern (scripts/format_recon.py:171-182):
    every case behaves, and every declared bar is exercised firing AND silent."""
    bars, cases = tuple(bars), tuple(cases)
    fails = verify_firing(bars, cases)
    if fails:
        raise SystemExit("DECLARED BARS MISBEHAVE (rule 21):\n  " + "\n  ".join(fails))
    dirs: dict[str, set] = {b.name: set() for b in bars}
    for case in cases:
        target, _, _, should, _ = _unpack(case)
        if isinstance(target, str) and target in dirs:
            dirs[target].add(should)
    missing = [nm for nm, d in dirs.items() if d != {True, False}]
    if missing:
        raise SystemExit(f"FIRING CHECK INCOMPLETE (trap 5): {missing}")
    return bars


# --- stage-end evaluation on the realised n -------------------------------------------
def sham_domain(rec: dict) -> bool:
    """The default domain selector: sham-template sessions (m:271)."""
    return keys.is_sham(rec["template"])


def stage_end_eval(records: Iterable[dict], bar: Bar,
                   domain_selector: Callable[[dict], bool] | None = None, *,
                   look: Any = None) -> BarResult:
    """k = task rounds claimed in the bar's class over the domain's sessions; n =
    task rounds generated over them (the realised n, m:271). Records follow
    DESIGN.md §2's schema."""
    # PIN (Code, declared at LOCK v0.1): the domain is every selected session,
    # excluded ones included (they generated their rounds); n counts every
    # recorded task round (<= 10 per session, asserted); k counts rounds whose
    # audit claim is v2 or echo (Qwen) / AuditSpec or echo (OLMo) -- content and
    # lexical claims never count. The selector defaults to the sham template; a
    # selector admitting a contrast session for a sham-only bar is refused, as is
    # a record of another substrate, unit or stage.
    if bar.kind not in ("binomial_stage_end", "binomial_look", "pause"):
        raise ValueError(f"{bar.name}: stage_end_eval serves the round-degeneracy bars and the "
                         f"pause, not a {bar.kind} bar")
    sel = domain_selector if domain_selector is not None else sham_domain
    dom = [r for r in records if sel(r)]
    seen: set = set()
    k = n = 0
    for r in dom:
        if bar.domain == "sham" and not keys.is_sham(r["template"]):
            raise ValueError(f"{bar.name}: DOMAIN VIOLATION: the selector admitted a "
                             f"contrast-template session for a sham-only bar (m:271)")
        if r["substrate"] != bar.substrate:
            raise ValueError(f"{bar.name}: a {r['substrate']} record on a {bar.substrate} bar")
        if r["template"] not in keys.templates(bar.scope):
            raise ValueError(f"{bar.name}: template {r['template']!r} is not a {bar.scope} template")
        if "unit" in r and r["unit"] != bar.scope:
            raise ValueError(f"{bar.name}: a {r['unit']} record on a {bar.scope} bar")
        stage_name = bar.name.split("@", 1)[1] if "@" in bar.name else bar.stage
        if "stage" in r and r["stage"] not in (bar.stage, stage_name):
            raise ValueError(f"{bar.name}: a {r['stage']!r}-stage record on a {bar.stage} bar")
        ident = (r["template"], r["s"], r.get("j"), r.get("path"))
        if ident in seen:
            raise ValueError(f"{bar.name}: a session appears twice in the domain")
        seen.add(ident)
        rounds = r["rounds"]
        if len(rounds) > MAX_ROUNDS:
            raise ValueError(f"{bar.name}: a session records more than {MAX_ROUNDS} task rounds")
        for rd in rounds:
            claim = rd["audit"]["claim"]
            if claim not in CLAIMS[bar.substrate]:
                raise ValueError(f"{bar.name}: claim {claim!r} is not a {bar.substrate} class")
            k += claim in DEGEN_CLAIMS[bar.substrate]
        n += len(rounds)
    tpls = {r["template"] for r in dom}
    ctx: dict = {"template": tpls.pop()} if len(tpls) == 1 else {}
    if look is not None:
        ctx["look"] = look
    return bar.evaluate(k, n, **ctx)


# --- self-test -------------------------------------------------------------------------
def _rec(substrate: str, template: str, claims: Sequence, *, unit: str, stage: str, s: int = 0,
         phases: Sequence[str] | None = None) -> dict:
    phases = phases or ["forced"] * min(4, len(claims)) + ["free"] * max(0, len(claims) - 4)
    return {"schema": "m-session-v1", "substrate": substrate, "unit": unit, "stage": stage,
            "template": template, "contrast": keys.is_contrast(template), "s": s, "j": s,
            "path": "uncached",
            "rounds": [{"phase": ph, "audit": {"substrate": substrate, "phase": ph, "claim": cl}}
                       for cl, ph in zip(claims, phases)]}


def _raises(fn, exc) -> bool:
    try:
        fn()
    except exc:
        return True
    except Exception:
        return False
    return False


def _selftest(chk) -> None:
    import itertools
    import json
    import re
    import sys
    from pathlib import Path

    import numpy as np

    from valence_core import session, stats

    # q() and the float trap
    chk("bars: q accepts str, int and Fraction exactly",
        q("0.05") == Fraction(1, 20) and q("1/50") == Fraction(1, 50) and q(1) == 1
        and q(Fraction(1, 5)) == Fraction(1, 5))
    chk("bars: q refuses float, numpy float, bool and None (TypeError)",
        all(_raises(lambda x=x: q(x), TypeError) for x in (0.05, np.float64(0.05), True, None)))
    chk("bars: the float trap q exists for (Fraction(0.05) != 1/20, Fraction('0.05') == 1/20)",
        Fraction(0.05) != Fraction(1, 20) and q("0.05") == Fraction(1, 20)
        and not (Fraction(0.05) <= q("0.05")), str(Fraction(0.05)))
    chk("bars: counts refuse float and bool, accept numpy ints exactly",
        _raises(lambda: fires(1.0, 1, "0.05", "0.05"), TypeError)
        and _raises(lambda: fires(True, 1, "0.05", "0.05"), TypeError)
        and fires(np.int64(1), np.int64(1), "0.05", "0.05") is True)
    chk("bars: fires refuses k > n and negative counts; binom_sf refuses p outside [0, 1]",
        _raises(lambda: fires(3, 2, "0.05", "0.05"), ValueError)
        and _raises(lambda: fires(-1, 2, "0.05", "0.05"), ValueError)
        and _raises(lambda: binom_sf(1, 2, "1.5"), ValueError))

    # binom_sf exactness
    ok = True
    for n in range(0, 25):
        for k in range(-1, n + 2):
            direct = (Fraction(1) if k <= 0 else
                      sum((Fraction(comb(n, i)) * Fraction(1, 20) ** i * Fraction(19, 20) ** (n - i)
                           for i in range(k, n + 1)), Fraction(0)))
            ok &= binom_sf(k, n, "0.05") == direct
    chk("bars: binom_sf (both tail paths) == the direct rational sum, n <= 24", ok)
    worst = max(abs(float(binom_sf(k, n, str(p))) - stats.binom_sf_inclusive(k, n, p))
                for p in (0.05, 0.02, 0.10, 0.20) for n in range(1, 61) for k in range(0, n + 1))
    chk("bars: binom_sf agrees with stats.binom_sf_inclusive to 1e-12, n <= 60 (descriptive)",
        worst < 1e-12, f"max |diff| {worst:.2e}")

    # the mandatory verify table, case by case
    for case in MANDATORY_CASES:
        target, k, n, should, extra = _unpack(case)
        if target[0] == "refuse":
            label = f"refuse p0={target[1]!r} alpha={target[2]!r} -> {'TypeError' if should else 'accepted'}"
        elif target[0] == "fisher":
            label = f"Fisher ({k},{n},{extra['c']},{extra['n2']}) {'fires' if should else 'silent'}"
        else:
            label = f"({k}/{n}, p0 {target[1]}) {'fires' if should else 'silent'}"
        f = verify_firing((), [case])
        chk(f"bars: mandatory {label}", f == [], f)
    chk("bars: every mandatory case is in FIRING_CASES",
        all(c in FIRING_CASES for c in MANDATORY_CASES))
    def _of():
        stats.binom_sf_inclusive(117, 2000, 0.05)
    chk("bars: n = 2000 exact here while stats' float path overflows there",
        fires(117, 2000, "0.05", "0.05") and not fires(116, 2000, "0.05", "0.05")
        and _raises(_of, OverflowError))

    # critical_k against stats' monitor (rule-26-style cross-check), and minimality
    for p0 in ("0.05", "0.02", "0.10", "0.20"):
        mon = stats.CheckpointedBinomialMonitor("x", float(p0))
        bad = [n for n in range(1, 301) if critical_k(n, p0, "0.05") != mon.critical_k(n)]
        chk(f"bars: critical_k == stats.CheckpointedBinomialMonitor.critical_k, n 1..300, p0 {p0}",
            bad == [], bad[:5])
    ok = True
    for p0 in ("0.05", "0.02", "0.10", "0.20"):
        for n in range(1, 301):
            c = critical_k(n, p0, "0.05")
            if c is None:
                ok &= not fires(n, n, p0, "0.05")
            else:
                ok &= fires(c, n, p0, "0.05") and (c == 0 or not fires(c - 1, n, p0, "0.05"))
    chk("bars: critical_k fires at crit and is silent at crit - 1 (n 1..300, four p0)", ok)
    chk("bars: critical_k edge cases (n = 0 None; p0 0 -> 1; p0 1 -> None)",
        critical_k(0, "0.05", "0.05") is None and critical_k(5, "0", "0.05") == 1
        and critical_k(5, "1", "0.05") is None)

    # realised-n tables (maps/stats.md §5)
    want05 = [(1, 1, 1), (2, 7, 2), (8, 16, 3), (17, 28, 4), (29, 40, 5), (41, 53, 6), (54, 67, 7),
              (68, 81, 8), (82, 95, 9), (96, 110, 10), (111, 125, 11), (126, 140, 12),
              (141, 155, 13), (156, 160, 14)]
    want02 = [(1, 2, 1), (3, 18, 2), (19, 41, 3), (42, 69, 4), (70, 99, 5), (100, 131, 6),
              (132, 160, 7)]
    t05, t02 = realised_table("0.05", "0.05", 160), realised_table("0.02", "0.05", 160)
    chk("bars: realised table p0 .05, n 1..160 == stats.md §5", t05 == want05, t05[-3:])
    chk("bars: realised table p0 .02, n 1..160 == stats.md §5", t02 == want02, t02)
    t10 = realised_table("0.10", "0.05", 144)
    chk("bars: realised table p0 .10 (lines) head [1]:None [2-3]:2 [4-8]:3 [9-14]:4 [15-20]:5, "
        "n = 144 -> 22",
        t10[:5] == [(1, 1, None), (2, 3, 2), (4, 8, 3), (9, 14, 4), (15, 20, 5)]
        and t10[-1][1:] == (144, 22), t10[-1])
    t20 = realised_table("0.20", "0.05", 240)
    chk("bars: realised table p0 .20 (guard) head [1]:None [2]:2 [3-4]:3 [5-7]:4 [8-10]:5, "
        "tail [237-240]:59",
        t20[:5] == [(1, 1, None), (2, 2, 2), (3, 4, 3), (5, 7, 4), (8, 10, 5)]
        and t20[-1] == (237, 240, 59), t20[-1])
    chk("bars: realised_table refuses a float p0", _raises(lambda: realised_table(0.05, "0.05", 5),
                                                          TypeError))

    # m:271's eight counts and the verdict counts
    rows = [SPEC_COUNT_CASES[i:i + 2] for i in range(0, 16, 2)]
    names = ("G-F0m-Qwen 160 .05 -> 14", "G-F0m-OLMo 160 .02 -> 7", "G-F3 rounds 240 .05 -> 19",
             "G-F3 lines 144 .10 -> 22", "G-TIME-F0 10 .05 -> 3", "G-TIME-OLMo 10 .02 -> 2",
             "G-TIME-F3 rounds 30 .05 -> 5", "G-TIME-F3 lines 18 .10 -> 5")
    for nm, pair in zip(names, rows):
        f = verify_firing((), pair)
        chk(f"bars: m:271 critical count {nm} (P at crit and crit - 1)", f == [], f)
    f = verify_firing((), SPEC_COUNT_CASES[16:])
    chk("bars: verdict counts at p0 .5 (144@.01 87, 144@.05 83, 96@.01 60, 80@.01 51)", f == [], f)

    # Fisher
    ties = [(1, 1, 0, 19), (3, 3, 0, 3), (2, 4, 0, 12), (2, 6, 0, 19), (2, 2, 2, 14), (12, 12, 2, 4)]
    chk("bars: Fisher ties at exactly 1/20 fire under <= (stats.md §5's six), not under f1's <",
        all(fisher_sf(*t) == Fraction(1, 20) and fisher_fires(*t, "0.05") for t in ties)
        and not any(session.fisher_two_groups(*t) < 0.05 for t in ties))

    def f1_fisher(a, n1, c, n2):   # f1's formula (f_sessions.py:154-159), exact
        k, n = a + c, n1 + n2
        return Fraction(sum(comb(k, x) * comb(n - k, n1 - x) for x in range(a, min(k, n1) + 1)),
                        comb(n, n1))
    ok, worst = True, 0.0
    for n1, n2 in itertools.product(range(0, 9), repeat=2):
        for a in range(n1 + 1):
            for c in range(n2 + 1):
                e = fisher_sf(a, n1, c, n2)
                ok &= e == f1_fisher(a, n1, c, n2)
                worst = max(worst, abs(float(e) - session.fisher_two_groups(a, n1, c, n2)))
    chk("bars: fisher_sf == f1's formula exactly and session.fisher_two_groups to 1e-12 "
        "(n1, n2 <= 8)", ok and worst < 1e-12, f"{worst:.1e}")
    chk("bars: fisher_sf silent case (2,3,0,3) = 1/5 and refusals (a > n1, float alpha)",
        fisher_sf(2, 3, 0, 3) == Fraction(1, 5) and not fisher_fires(2, 3, 0, 3, "0.05")
        and _raises(lambda: fisher_sf(4, 3, 0, 3), ValueError)
        and _raises(lambda: fisher_fires(3, 3, 0, 3, 0.05), TypeError))

    # why not session.Tripwire (descriptive)
    tw = session.Tripwire("x", "binomial", p0=0.05)
    chk("bars: session.Tripwire (<) is silent at the n = 1 tie that m's <= fires (m:271)",
        tw.check(1, 1) is None and fires(1, 1, "0.05", "0.05"))

    # Bar declaration refusals and acceptances
    base = dict(stage="time", scope="Q-F0", substrate="qwen")
    refusals = [
        lambda: Bar("h", "hair_trigger", domain="every", **base),                        # unjustified
        lambda: Bar("pz", "pause", domain="sham", **base),                               # unjustified pause
        lambda: Bar("b", "binomial_stage_end", p0=0.05, domain="sham", **base),          # float p0
        lambda: Bar("b", "binomial_stage_end", p0="0.05", alpha=0.05, domain="sham", **base),
        lambda: Bar("b", "binomial_stage_end", domain="sham", **base),                   # no p0
        lambda: Bar("b", "binomial_stage_end", p0="0.05", domain="every", **base),       # wrong domain
        lambda: Bar("b", "binomial_stage_end", p0="0.05", domain="sham", planned_n=160,
                    planned_crit=13, **base),                                            # wrong crit
        lambda: Bar("h", "hair_trigger", domain="every", justification="j", binding=False, **base),
        lambda: Bar("x", "tripwire", domain="every", **base),                            # unknown kind
        lambda: Bar("b", "binomial_stage_end", p0="0.05", domain="sham", stage="time",
                    scope="OLMo-sft", substrate="qwen"),                                 # scope/substrate
    ]
    res = [_raises(fn, (ValueError, TypeError)) for fn in refusals]
    chk("bars: declaration refusals (unjustified hair/pause, float p0/alpha, no p0, domain, "
        "planned crit, non-binding hair, kind, scope)", all(res), res)
    chk("bars: a float p0 at declaration is a TypeError, not a ValueError",
        _raises(refusals[2], TypeError))
    try:
        Bar("h", "hair_trigger", domain="every", justification="zero by construction", **base)
        Bar("b", "binomial_stage_end", p0="0.05", domain="sham", planned_n=160, planned_crit=14,
            **base)
        acc = True
    except Exception as e:   # pragma: no cover - reported through chk
        acc = repr(e)
    chk("bars: declaration accepts a justified hair trigger and a correct planned crit", acc is True,
        acc)

    # the declared sets
    qn = {b.name for b in QF0_BARS}
    want_q = {"scaffold_absorption", "template_breakage", "schedule_mismatch",
              "round_degeneracy@G-TIME-F0", "gid_divergence@G-ID-F0m", "round_degeneracy@G-F0m-Qwen",
              "round_degeneracy@campaign-Q-F0", "exclusion_guard_fisher@campaign-Q-F0",
              "exclusion_guard_abs@campaign-Q-F0"}
    bq = {b.name: b for b in QF0_BARS}
    chk("bars: QF0_BARS names (m:271, m:280, m:281, m:283, m:316, m:330)", qn == want_q,
        sorted(qn ^ want_q))
    chk("bars: QF0_BARS p0 .05 (degeneracy), .20 (guard abs), alpha .05, crits 3 and 14, all binding",
        bq["round_degeneracy@G-TIME-F0"].p0 == "0.05" and bq["round_degeneracy@G-TIME-F0"].planned_crit == 3
        and bq["round_degeneracy@G-F0m-Qwen"].planned_crit == 14
        and bq["round_degeneracy@campaign-Q-F0"].p0 == "0.05"
        and bq["exclusion_guard_abs@campaign-Q-F0"].p0 == "0.20"
        and all(b.alpha == "0.05" and b.binding for b in QF0_BARS))
    okc = True
    for ck in keys.CKPTS:
        bo = {b.name: b for b in OLMO_BARS(ck)}
        t, g, c = f"G-TIME-OLMo-{ck}", f"G-F0m-OLMo-{ck}", f"campaign-OLMo-{ck}"
        okc &= (set(bo) == {"scaffold_absorption", "template_breakage", "schedule_mismatch",
                            f"round_degeneracy@{t}", f"gtime_pause@{t}", f"round_degeneracy@{g}",
                            f"round_degeneracy@{c}", f"exclusion_guard_fisher@{c}",
                            f"exclusion_guard_abs@{c}"}
                and bo[f"round_degeneracy@{t}"].p0 == "0.02"
                and bo[f"round_degeneracy@{t}"].planned_crit == 2
                and bo[f"round_degeneracy@{g}"].planned_crit == 7
                and bo[f"round_degeneracy@{c}"].p0 == "0.02"
                and bo[f"gtime_pause@{t}"].kind == "pause"
                and bo[f"exclusion_guard_fisher@{c}"].binding
                and not bo[f"exclusion_guard_abs@{c}"].binding
                and all(b.scope == f"OLMo-{ck}" and b.substrate == "olmo" for b in bo.values()))
    chk("bars: OLMO_BARS(ckpt) for sft/dpo/instruct (p0 .02; crits 2 and 7; pause; guard abs "
        "reported only)", okc)
    chk("bars: OLMO_BARS refuses base and an unknown checkpoint",
        _raises(lambda: OLMO_BARS("base"), ValueError) and _raises(lambda: OLMO_BARS("OLMo-sft"),
                                                                  ValueError))
    sets = [QF0_BARS] + [OLMO_BARS(ck) for ck in keys.CKPTS]
    chk("bars: every hair trigger and the pause carry a justification; no Q-F0 pause exists",
        all(b.justification.strip() for st in sets for b in st if b.kind in _ONE_CLAIM)
        and not any(b.kind == "pause" for b in QF0_BARS))
    rows_ok = all(all(d[f] not in (None, "") for f in ("class", "unit", "alpha", "domain", "cadence"))
                  and (d["p0"] is not None or d["kind"] in ("hair_trigger", "pause", "guard_fisher"))
                  for st in sets for d in (b.as_dict() for b in st))
    rt = bq["round_degeneracy@G-TIME-F0"].as_dict()["realised_table"]
    chk("bars: LOCK rows carry class, unit, p0, alpha, domain, cadence; stage-end rows carry "
        "their realised table", rows_ok and rt == [[1, 1, 1], [2, 7, 2], [8, 10, 3]], rt)
    json.dumps([b.as_dict() for st in sets for b in st])

    # firing cases over the declared sets
    for st, nm in zip(sets, ("Q-F0",) + tuple(f"OLMo-{c}" for c in keys.CKPTS)):
        f = verify_firing(st, FIRING_CASES)
        try:
            assert_firing_complete(st, FIRING_CASES)
            comp = True
        except SystemExit as e:
            comp = str(e)
        chk(f"bars: FIRING_CASES verify clean and complete on {nm}", f == [] and comp is True,
            f[:3] or comp)
    hb = Bar("one_way", "hair_trigger", domain="every", justification="zero", **base)
    msg = ""
    try:
        assert_firing_complete(QF0_BARS + (hb,), FIRING_CASES + (("one_way", 1, 1, True, {}),))
    except SystemExit as e:
        msg = str(e)
    chk("bars: assert_firing_complete refuses a bar exercised in one direction only (trap 5)",
        "FIRING CHECK INCOMPLETE" in msg and "one_way" in msg, msg[:80])
    msg = ""
    try:
        assert_firing_complete(QF0_BARS + (hb,), FIRING_CASES)
    except SystemExit as e:
        msg = str(e)
    chk("bars: assert_firing_complete refuses a declared bar never exercised",
        "FIRING CHECK INCOMPLETE" in msg, msg[:80])
    msg = ""
    try:
        assert_firing_complete(QF0_BARS, FIRING_CASES + (("round_degeneracy@G-TIME-F0", 1, 2, True,
                                                          {}),))
    except SystemExit as e:
        msg = str(e)
    chk("bars: assert_firing_complete refuses a misbehaving case (n = 2, one claim cannot fire)",
        "MISBEHAVE" in msg, msg[:80])
    f = verify_firing(QF0_BARS, [("round_degeneracy@G-TIME-F9", 1, 1, True, {}),
                                 (("exact", "0.05", "0.05"), 1, 1, False, {})])
    chk("bars: verify_firing reports an undeclared bar name and a wrong arithmetic expectation",
        len(f) == 2 and "no such bar" in f[0], f)
    chk("bars: verify_firing skips another unit's bar but runs its own (no silent pass)",
        verify_firing(QF0_BARS, [("round_degeneracy@G-TIME-OLMo-sft", 1, 3, True, {})]) == []
        and verify_firing(OLMO_BARS("sft"), [("round_degeneracy@G-TIME-OLMo-sft", 1, 3, True, {})])
        != [])

    # evaluate: domains, context, binding
    gt = bq["round_degeneracy@G-TIME-F0"]
    fq = bq["exclusion_guard_fisher@campaign-Q-F0"]
    chk("bars: a sham-only bar refuses a contrast template and accepts the sham one",
        _raises(lambda: gt.evaluate(3, 10, template="A0"), ValueError)
        and gt.evaluate(3, 10, template="A0s").fired)
    chk("bars: the guard refuses a sham template, a missing sham count, sham counts elsewhere",
        _raises(lambda: fq.evaluate(3, 3, template="A0s", sham_k=0, sham_n=3), ValueError)
        and _raises(lambda: fq.evaluate(3, 3), TypeError)
        and _raises(lambda: gt.evaluate(3, 10, sham_k=0, sham_n=3), TypeError)
        and fq.evaluate(3, 3, template="A0", sham_k=0, sham_n=3, look=1).fired)
    chk("bars: evaluate refuses unknown context, a phase on a domain bar, a look on a stage-end bar, "
        "another unit's template",
        _raises(lambda: gt.evaluate(1, 1, tag="granite"), TypeError)
        and _raises(lambda: gt.evaluate(1, 1, phase="free"), ValueError)
        and _raises(lambda: gt.evaluate(1, 1, look=1), ValueError)
        and _raises(lambda: gt.evaluate(1, 1, template="A0s-OLMo-sft"), ValueError))
    ga_o = {b.name: b for b in OLMO_BARS("dpo")}["exclusion_guard_abs@campaign-OLMo-dpo"]
    ro, rq = ga_o.evaluate(5, 10), bq["exclusion_guard_abs@campaign-Q-F0"].evaluate(5, 10)
    chk("bars: OLMo's absolute guard is reported only (exceeds, never fires); Qwen's binds",
        ro.exceeds and not ro.fired and not ro.binding and rq.fired and rq.exceeds
        and "not binding" in ro.message, ro.message)
    chk("bars: BarResult carries an exact Fraction and a JSON-safe dict (no float)",
        isinstance(gt.evaluate(1, 1).p, Fraction)
        and json.loads(json.dumps(gt.evaluate(1, 1).as_dict()))["p"] == "1/20")

    # messages: bar name, template/phase/look words and numbers only
    roster = {w for pr in __import__("valence_core.e2d.config", fromlist=["ROSTER"]).ROSTER for w in pr}
    rp = Path(__file__).resolve().parents[2] / "data" / "olmo" / "a1_repair_roster.json"
    roster |= {w for pr in json.loads(rp.read_text())["selected_tags"] for w in pr}
    msgs, ok = [], True
    for st in sets:
        tpls = keys.templates(st[0].scope)
        for b in st:
            for tpl in (None,) + tpls:
                for ph in ((None, "forced", "free") if b.kind in _ONE_CLAIM else (None,)):
                    for kk in (0, 1):
                        ctx = {"template": tpl, "phase": ph}
                        if b.kind == "guard_fisher":
                            ctx.update(sham_k=0, sham_n=3)
                        try:
                            m = b.evaluate(kk, 3, **{x: v for x, v in ctx.items() if v is not None}).message
                        except ValueError:
                            continue
                        msgs.append(m)
                        ok &= m.startswith(f"BAR {b.name} ")
                        if b.kind in _ONE_CLAIM:
                            rest = m.replace(b.name, "").replace(f"template={tpl}", "")
                            ok &= not re.search(r"\d", rest)
    low = " ".join(msgs).lower()
    chk("bars: messages name the bar, carry no roster word, and a hair/pause message no number",
        ok and not any(re.search(rf"\b{w}\b", low) for w in roster) and len(msgs) > 100,
        f"{len(msgs)} messages")
    m = QF0_BARS[0].evaluate(1, 1, template="A0", phase="free").message
    chk("bars: a contrast free-round hair trigger prints name, template and phase only",
        m == "BAR scaffold_absorption FIRED template=A0 phase=free", m)

    # stage_end_eval on the realised n
    Q, U = "qwen", "Q-F0"
    sham3 = _rec(Q, "A0s", ["v2", None, "echo", None, None, None, "v2", None, None, None],
                 unit=U, stage="time")
    sham2 = _rec(Q, "A0s", ["v2", "content", "echo", "lexical", None, None, None, None, None, None],
                 unit=U, stage="time")
    con = _rec(Q, "A0", ["v2"] * 4 + ["echo"] * 6, unit=U, stage="time")
    r3, r2 = stage_end_eval([sham3, con], gt), stage_end_eval([sham2, con], gt)
    chk("bars: stage_end_eval G-TIME-F0: 3 v2/echo claims in 10 sham rounds fire; 2 (content and "
        "lexical not counted) stay silent", r3.fired and (r3.k, r3.n) == (3, 10)
        and not r2.fired and (r2.k, r2.n) == (2, 10), (r3.k, r3.n, r2.k, r2.n))
    chk("bars: stage_end_eval: a contrast session's claims never enter the sham domain",
        stage_end_eval([con], gt).n == 0 and not stage_end_eval([con], gt).fired)
    chk("bars: stage_end_eval refuses a selector admitting a contrast session",
        _raises(lambda: stage_end_eval([sham3, con], gt, lambda r: True), ValueError))
    one = _rec(Q, "A0s", ["v2"], unit=U, stage="time")
    three = _rec(Q, "A0s", [None, None, "echo"], unit=U, stage="time")
    chk("bars: stage_end_eval one-session boundary: a round-1 claim fires (P = 1/20); a round-3 "
        "claim ending the session is reported, not fired",
        stage_end_eval([one], gt).fired and stage_end_eval([one], gt).p == Fraction(1, 20)
        and not stage_end_eval([three], gt).fired)
    bogus = _rec(Q, "A0s", ["audit"], unit=U, stage="time")
    dup = [sham3, dict(sham3)]
    many = _rec(Q, "A0s", [None] * 11, unit=U, stage="time")
    wrong_unit = _rec("olmo", "A0s-OLMo-sft", ["audit"], unit="OLMo-sft", stage="time")
    wrong_stage = _rec(Q, "A0s", ["v2"], unit=U, stage="qual")
    res = [_raises(lambda: stage_end_eval([bogus], gt), ValueError),
           _raises(lambda: stage_end_eval(dup, gt), ValueError),
           _raises(lambda: stage_end_eval([many], gt), ValueError),
           _raises(lambda: stage_end_eval([wrong_unit], gt, lambda r: True), ValueError),
           _raises(lambda: stage_end_eval([wrong_stage], gt), ValueError),
           _raises(lambda: stage_end_eval([sham3], fq), ValueError)]
    chk("bars: stage_end_eval refuses a foreign claim class, a duplicate session, > 10 rounds, "
        "another substrate, another stage, a guard bar", all(res), res)
    gq = bq["round_degeneracy@G-F0m-Qwen"]
    # free-round v2 claims end nothing on Qwen (m:271), so a sham session can carry several
    qual = [_rec(Q, "A0s", ["v2" if (s == 0 and 4 <= i < 8) or (0 < s < 10 and i == 9) else None
                            for i in range(10)], unit=U, stage="qual", s=s) for s in range(16)]
    rq = stage_end_eval(qual, gq)
    chk("bars: stage_end_eval G-F0m-Qwen: 13 claims over 160 sham rounds silent, crit 14",
        (rq.k, rq.n, rq.crit, rq.fired) == (13, 160, 14, False), (rq.k, rq.n, rq.crit))
    bo = {b.name: b for b in OLMO_BARS("sft")}
    ob, op = bo["round_degeneracy@G-TIME-OLMo-sft"], bo["gtime_pause@G-TIME-OLMo-sft"]
    O, UO = "olmo", "OLMo-sft"
    r3o = _rec(O, "A0s-OLMo-sft", [None, None, "echo"], unit=UO, stage="time")
    r2o = _rec(O, "A0s-OLMo-sft", [None, "audit"], unit=UO, stage="time")
    lexo = _rec(O, "A0s-OLMo-sft", [None, None, "lexical"], unit=UO, stage="time")
    chk("bars: OLMo G-TIME: a round-3 echo claim pauses where the bar cannot fire (STOP-7 A'3)",
        stage_end_eval([r3o], op).fired and not stage_end_eval([r3o], ob).fired)
    chk("bars: OLMo G-TIME: a round-2 AuditSpec claim fires the bar AND the pause (STOP governs)",
        stage_end_eval([r2o], ob).fired and stage_end_eval([r2o], op).fired)
    chk("bars: OLMo G-TIME: a lexical-only session neither fires nor pauses; Qwen's v2 is foreign",
        not stage_end_eval([lexo], ob).fired and not stage_end_eval([lexo], op).fired
        and _raises(lambda: stage_end_eval([_rec(O, "A0s-OLMo-sft", ["v2"], unit=UO, stage="time")],
                                           op), ValueError))
    look_bar = bq["round_degeneracy@campaign-Q-F0"]
    rl = stage_end_eval([_rec(Q, "A0s", ["v2"] * 2 + [None] * 8, unit=U, stage="campaign", s=s)
                         for s in range(8)] + [con | {"stage": "campaign"}], look_bar, look=2)
    chk("bars: stage_end_eval serves a campaign look (cumulative sham rounds; look printed)",
        rl.fired and (rl.k, rl.n) == (16, 80) and "look=2" in rl.message, rl.message)

    # sequential false pause
    def brute(ns, p0):
        p = q(p0)
        cs = [critical_k(n, p, "0.05") for n in ns]
        tot = Fraction(0)
        for seq in itertools.product((0, 1), repeat=ns[-1]):
            if any(c is not None and sum(seq[:n]) >= c for n, c in zip(ns, cs)):
                kk = sum(seq)
                tot += p ** kk * (1 - p) ** (ns[-1] - kk)
        return tot
    chk("bars: seq_false_pause == brute-force enumeration on looks [4, 8] at p0 .20 and [3, 6, 10] "
        "at .10", seq_false_pause([4, 8], "0.20", "0.05") == brute([4, 8], "0.20")
        and seq_false_pause([3, 6, 10], "0.10", "0.05") == brute([3, 6, 10], "0.10"))
    chk("bars: seq_false_pause small exact cases ([1, 2] at .05 = 1/20; one look = P(X >= crit))",
        seq_false_pause([1, 2], "0.05", "0.05") == Fraction(1, 20)
        and seq_false_pause([160], "0.05", "0.05") == binom_sf(14, 160, "0.05"))
    ill = [(seq_false_pause([200, 400, 600, 640, 640], "0.05", "0.05"),
            [critical_k(n, "0.05", "0.05") for n in (200, 400, 600, 640)]),
           (seq_false_pause([200, 400, 600, 640], "0.02", "0.05"),
            [critical_k(n, "0.02", "0.05") for n in (200, 400, 600, 640)]),
           (seq_false_pause([640], "0.05", "0.05"), [])]
    chk("bars: seq_false_pause reproduces stats.md §5's illustrative figures under ITS n_j "
        "assumption (.0976 crits 16/28/40/42; .0863 crits 8/14/19/20; one look .0468)",
        [_dec(f) for f, _ in ill] == ["0.0976", "0.0863", "0.0468"]
        and ill[0][1] == [16, 28, 40, 42] and ill[1][1] == [8, 14, 19, 20],
        [_dec(f) for f, _ in ill])
    chk("bars: seq_false_pause refuses decreasing looks, no looks and a float p0",
        _raises(lambda: seq_false_pause([10, 5], "0.05", "0.05"), ValueError)
        and _raises(lambda: seq_false_pause([], "0.05", "0.05"), ValueError)
        and _raises(lambda: seq_false_pause([10], 0.05, "0.05"), TypeError))
    chk("bars: _dec is exact half-up (1/20 -> 0.0500, 1/8 -> 0.1250, 0.00005 -> 0.0001)",
        _dec(Fraction(1, 20)) == "0.0500" and _dec(Fraction(1, 8)) == "0.1250"
        and _dec(Fraction(1, 20000)) == "0.0001" and _dec(Fraction(1)) == "1.0000")

    # insulation and forbidden literals
    chk("bars: importing bars leaves the quarantined state-present module out of sys.modules",
        "valence_core.e2b" + ".statepresent" not in sys.modules)
    src = Path(__file__).read_text()
    forbidden = ["choice_read_" + "statepresent", "(10)" + " the", "slip " + "(10)",
                 "_new_qwen" + "_adapter", "def qwen_or" + "_explain", "adapters.base import " + "Injection"]
    chk("bars: source carries none of the forbidden literals", not any(x in src for x in forbidden))
