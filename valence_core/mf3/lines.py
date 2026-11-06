"""The reasoning line's classes (PROPOSAL-m v1.11 §2.6 m:265, §3.2 m:293, §4 m:308, m:312 (f),
m:314; the design seat's prebuild answers of 2026-11-06, Q4 and Q8).

m:265: "The reasoning line is not a round (Q-F3). Scored only by its defect bar, counter (c), and the
`scaffold_absorption` hair trigger (the one hair trigger that reads it and can remove a session from
the primary's domain; the runner ends the session at that fire). Its defect classes: empty line; cap
reached without a newline; reasoning-line echo = a verbatim, whitespace-normalized reproduction of
any complete harness-written line of the session (v1.3's definition). Exempt from v2/v3, the
task-round echo class, lexical, and `earlier`; the frozen ban list applies to its generation."

So nothing here calls the task-round audit: a reasoning line never reaches v2, v3, the task-round
echo class or lexical, and never enters ``earlier`` (the runner's PIN). ``classify_line`` returns its
three defect classes (``reasoning_line_defect``'s numerator is their union, m:293) and its
``scaffold_absorption`` hits, beside the echo's matched line index.

The Q4 counter (the seat's answer: the three strings from Q-F0's VERDICTS read, declared as one
descriptive rule-23 counter, deciding nothing) is ``review_counter``, a pure function of the
records' generated texts, tabulated over all sessions, excluded included.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from valence_core.m import audit as m_audit

from . import banner

CLASSES = ("empty", "cap_no_newline", "echo")
#: The Q4 descriptive counter's strings (the seat's answers §4; Q-F0's VERDICTS read §5 item 2).
REVIEW_STRINGS = ("You are a helpful assistant.", "4assistant", "<|end|>")


def echo_lines(P: str, Q: str, n: int) -> tuple[str, ...]:
    """The reasoning-line echo set for the line at round ``n`` of a session with P-role label ``P``
    and Q-role label ``Q`` (the seat's Q8 ruling; Code's dated note N4)."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "which harness lines count is the declared
    # set of eight strings (m:258) plus the reasoning-block lines"; N4): the set is m:258's eight
    # strings, each as rendered for the session -- COMMON; TOLD-MAP's two variants with L_clean = P and
    # L_corr = Q; TOLD-MAP-SHAM's two with L_a = P and L_b = Q; TOLD-OBJ; "Reasoning (one line):"; and
    # the header "[round {k} | reasoning]" for every k the session has written up to this line's own n
    # (5..n) -- in that order, first match reported. A line the session never wrote (TOLD-OBJ in an A3
    # session, say) is in the set as the ruling's "declared set" has it.
    if type(n) is not int or n not in banner.N_RANGE:
        raise ValueError(f"a reasoning line's n is in {banner.N_RANGE[0]}..{banner.N_RANGE[-1]}, got {n!r}")
    told = tuple(t.format(L_clean=P, L_corr=Q) for t in banner.TOLD_MAP) + tuple(
        t.format(L_a=P, L_b=Q) for t in banner.TOLD_MAP_SHAM)
    return ((banner.COMMON,) + told + (banner.TOLD_OBJ, banner.REASONING_LINE)
            + tuple(banner.reasoning_header(k) for k in range(banner.N_RANGE[0], n + 1)))


@dataclass(frozen=True)
class LineAudit:
    """One reasoning line's classes (m:265) and scaffold hits."""
    classes: tuple[str, ...]
    echo_line: int | None = None
    scaffold: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        cl = tuple(self.classes)
        if any(c not in CLASSES for c in cl) or list(cl) != [c for c in CLASSES if c in cl]:
            raise ValueError(f"line classes must be a subset of {CLASSES} in that order, got {cl!r}")
        if ("echo" in cl) != (self.echo_line is not None):
            raise ValueError("the echo class and echo_line are both set or both absent")
        object.__setattr__(self, "classes", cl)
        object.__setattr__(self, "scaffold", tuple(self.scaffold))

    @property
    def defect(self) -> bool:
        """``reasoning_line_defect``'s numerator: the union of the three classes, once per line."""
        return bool(self.classes)

    def as_dict(self) -> dict:
        return {"classes": list(self.classes), "echo_line": self.echo_line,
                "scaffold": list(self.scaffold), "defect": self.defect}

    @classmethod
    def from_dict(cls, d: Mapping[str, Any]) -> "LineAudit":
        la = cls(classes=tuple(d["classes"]), echo_line=d["echo_line"], scaffold=tuple(d["scaffold"]))
        if "defect" in d and bool(d["defect"]) != la.defect:
            raise ValueError("record's defect flag disagrees with its classes")
        return la


def classify_line(text: str, *, n_tok: int, cap: int, stop_reason: str, cap_hit: bool,
                  echo_set: Sequence[str], scaffold_strings: Sequence[str]) -> LineAudit:
    """m:265's classes for one generated reasoning line."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): "empty line" = the text is empty after whitespace
    # normalization (audit.ws_norm): zero-length and whitespace-only alike. Both of Qwen's end-of-text
    # strings are in the frozen ban list, so a reasoning generation stops only on a newline after
    # content or at its cap; a whitespace-only line therefore runs to its cap (leading whitespace is
    # template whitespace, never a stop: qwen_mlx's content_seen rule) and is also cap_no_newline.
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "the cap-length prefix is the line as
    # generated, kept; it counts as cap-reach"): "cap reached without a newline" = the generator
    # stopped on its token cap (stop_reason "cap", cap_hit True), which on the adapters means n_tok ==
    # cap; a line whose newline arrives as its cap-th sampled token stopped on the newline (the stop
    # token is not kept), so it is not cap-reach. A record whose cap fields disagree is refused.
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: containment, "since equality misses prefixed
    # echoes"): echo = audit.harness_echo's Qwen form over echo_lines(...) -- the ws-normalised complete
    # line contained in the ws-normalised text, case-sensitive, first match by the set's order.
    if not isinstance(text, str):
        raise TypeError("a reasoning line's text is a str")
    if type(n_tok) is not int or n_tok < 0 or type(cap) is not int or cap <= 0 or type(cap_hit) is not bool:
        raise ValueError("n_tok, cap and cap_hit must be a non-negative int, a positive int and a bool")
    if stop_reason not in ("newline", "cap", "eos"):
        raise ValueError(f"stop_reason must be newline / cap / eos, got {stop_reason!r}")
    if cap_hit != (stop_reason == "cap") or (cap_hit and n_tok != cap) or n_tok > cap:
        raise ValueError(f"the generation's cap fields disagree (n_tok {n_tok}, cap {cap}, cap_hit {cap_hit}, "
                         f"stop_reason {stop_reason!r})")
    classes = []
    if m_audit.ws_norm(text) == "":
        classes.append("empty")
    if cap_hit:
        classes.append("cap_no_newline")
    echo = m_audit.harness_echo(text, tuple(echo_set), substrate="qwen")
    if echo is not None:
        classes.append("echo")
    return LineAudit(classes=tuple(classes), echo_line=echo,
                     scaffold=m_audit._scaffold_hits(text, tuple(scaffold_strings)))


def review_hits(text: str) -> tuple[str, ...]:
    """The Q4 counter's case-sensitive substring hits in one generated text, in declared order."""
    return tuple(s for s in REVIEW_STRINGS if s in text)


def review_counter(records: Sequence[Mapping[str, Any]]) -> dict:
    """The Q4 descriptive counter (rule 23): per template and string, the generations (task rounds
    and reasoning lines) whose text contains the string, over ALL sessions, excluded included.
    Reported in VERDICTS; it decides nothing."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q4): the unit is the generation (a task round
    # or a reasoning line), keyed (template, kind, string); a generation containing two of the strings
    # counts once under each. Its home is this module; the analyzer reads it at VERDICTS (G-ANL-F3).
    out: dict = {}
    for rec in records:
        t = str(rec["template"])
        gens = ([("round", r["text"]) for r in rec.get("rounds") or []]
                + [("line", x["text"]) for x in rec.get("reasoning") or []])
        for kind, text in gens:
            for s in review_hits(text):
                out.setdefault(t, {}).setdefault(kind, {}).setdefault(s, 0)
                out[t][kind][s] += 1
    return out


def _selftest(chk) -> None:
    from valence_core.m import audit as A

    ss = A.qwen_audit_of_record()[0].v2.ban_strings
    el = echo_lines("granite", "plaza", 7)

    def cl(text, n_tok=5, cap=60, stop="newline", hit=False, es=el):
        return classify_line(text, n_tok=n_tok, cap=cap, stop_reason=stop, cap_hit=hit, echo_set=es,
                             scaffold_strings=ss)

    chk("mf3.lines: the echo set -- m:258's eight strings as rendered for the session plus the headers "
        "written so far (N4)",
        len(el) == 7 + 3 and el[0] == banner.COMMON and el[5] == banner.TOLD_OBJ
        and el[6] == "Reasoning (one line):"
        and el[7:] == ("[round 5 | reasoning]", "[round 6 | reasoning]", "[round 7 | reasoning]")
        and "config granite presents clean task text; config plaza presents task text with" in el[1]
        and "config granite presents clean task text; config plaza presents clean task text." in el[3])
    clean = ["Both configs gave answerable tasks so far.", "The tasks look fine.", "Seven."]
    chk("mf3.lines: clean lines carry no class and no scaffold hit", all(cl(x).classes == () and
                                                                         cl(x).scaffold == () for x in clean))
    e = cl("  \t ", n_tok=60, stop="cap", hit=True)
    e2 = cl("\n\n\n", n_tok=60, stop="cap", hit=True)
    chk("mf3.lines: empty = whitespace-only after ws_norm (with the cap reached it is also cap_no_newline)",
        e.classes == ("empty", "cap_no_newline") and e2.classes == ("empty", "cap_no_newline")
        and cl("", n_tok=0, stop="eos").classes == ("empty",))
    c = cl("x " * 30, n_tok=60, stop="cap", hit=True)
    nl = cl("x " * 29, n_tok=59, stop="newline")
    chk("mf3.lines: cap_no_newline = stopped on the cap (n_tok == cap); a newline as the cap-th sampled "
        "token is a newline stop, not cap-reach; also at cap 120",
        c.classes == ("cap_no_newline",) and nl.classes == ()
        and cl("y", n_tok=120, cap=120, stop="cap", hit=True).classes == ("cap_no_newline",))
    echoes = {"COMMON": banner.COMMON, "told": el[1], "obj": banner.TOLD_OBJ,
              "label": "Reasoning (one line):", "header5": "[round 5 | reasoning]",
              "prefixed": "As the note says: " + el[3] + " So I pick one."}
    got = {k: cl(v).classes for k, v in echoes.items()}
    chk("mf3.lines: echo fires on COMMON, a TOLD line as rendered, TOLD-OBJ, the label, a header written so "
        "far, and a prefixed reproduction (containment, the seat's Q8)",
        all(v == ("echo",) for v in got.values()), got)
    nots = {"later header": "[round 9 | reasoning]", "lower case": banner.COMMON.lower(),
            "no period": banner.COMMON[:-1], "other labels": el[1].replace("granite", "ridge"),
            "label without colon": "Reasoning (one line)"}
    got_n = {k: cl(v).classes for k, v in nots.items()}
    chk("mf3.lines: no echo for a header not yet written, a case change, a line without its final period, "
        "another pair's labels, the label without its colon (complete-line, case-sensitive)",
        all(v == () for v in got_n.values()), got_n)
    sc = cl("fine <|im_end|> here")
    chk("mf3.lines: scaffold hits are the Qwen scaffold set's case-sensitive substrings (no class)",
        sc.scaffold == ("<|im_end|>",) and sc.classes == ())
    multi = cl(banner.COMMON + " " * 3, n_tok=60, stop="cap", hit=True)
    chk("mf3.lines: classes are a set in declared order; the defect is their union once per line",
        multi.classes == ("cap_no_newline", "echo") and multi.defect
        and LineAudit.from_dict(multi.as_dict()) == multi)
    refused = []
    for fn in (lambda: cl("x", n_tok=60, stop="newline", hit=True), lambda: cl("x", n_tok=59, stop="cap", hit=True),
               lambda: cl("x", n_tok=61, stop="newline"), lambda: cl("x", stop="stop"),
               lambda: echo_lines("a", "b", 4), lambda: LineAudit(classes=("echo",)),
               lambda: LineAudit(classes=("echo", "empty"), echo_line=1),
               lambda: LineAudit.from_dict({"classes": [], "echo_line": None, "scaffold": [], "defect": True})):
        try:
            fn()
            refused.append(False)
        except (ValueError, TypeError):
            refused.append(True)
    chk("mf3.lines: refuses inconsistent cap fields, an unknown stop, n out of 5..10, malformed audits",
        all(refused), refused)
    recs = [{"template": "A3", "rounds": [{"text": "You are a helpful assistant. Seven."}],
             "reasoning": [{"text": "4assistant <|end|>"}]},
            {"template": "A3s", "rounds": [{"text": "Seven."}], "reasoning": []}]
    chk("mf3.lines: the Q4 review counter tabulates the three strings per template and kind",
        review_counter(recs) == {"A3": {"round": {"You are a helpful assistant.": 1},
                                        "line": {"4assistant": 1, "<|end|>": 1}}}
        and review_hits("nothing") == ())
