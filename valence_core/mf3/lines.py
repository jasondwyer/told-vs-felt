"""The reasoning line's classes (PROPOSAL-m v1.11 §2.6 m:265, §3.2 m:293, §4 m:308, m:312 (f),
m:314; the design seat's prebuild answers of 2026-11-06, Q4 and Q8; ADDENDUM-m2 v0.5 §1, §3.4).

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

THE ECHO CLASS (ADDENDUM-m2 v0.5 §1, which replaces Q8's echo-set sentence and re-declares F25 and F28):
its domain is m:265's -- every complete harness-written line of the session, as rendered up to the
reasoning line in question -- built by ``domain`` from the record's pieces (Code's P1); its match is
equality after whitespace normalization (``audit.ws_norm``), case-sensitive. The runner and the verifier
build the domain the same way (``domain_before_line`` on their own transcript builders); a record's
domain at a line is ``domain_of_record``. Q8's containment is counter (a), descriptive (§3.4).

THE COUNTERS (rule 23; descriptive, deciding nothing; A-m2 v0.5 §3.4): (a) ``counter_a``, a reasoning
line that contains a complete harness-written line of the session or keeps the banner's ``=== … ===``
frame; (b) Code's declared read over ``b_candidates`` -- the task responses no audit class claims --
tabulated by ``tabulate_b``. The Q4 counter (the seat's answer: the three strings from Q-F0's VERDICTS
read, declared as one descriptive rule-23 counter, deciding nothing) is ``review_counter``, a pure
function of the records' generated texts, tabulated over all sessions, excluded included.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

from valence_core.m import audit as m_audit

CLASSES = ("empty", "cap_no_newline", "echo")
#: The Q4 descriptive counter's strings (the seat's answers §4; Q-F0's VERDICTS read §5 item 2).
REVIEW_STRINGS = ("You are a helpful assistant.", "4assistant", "<|end|>")
#: The record's piece kinds (scaffold.PIECE_KINDS, partitioned; scaffold's self-test asserts the partition):
#: the model writes the generations and the reasoning lines; every other piece is the harness's.
MODEL_PIECE_KINDS = ("generation", "reasoning_text")
HARNESS_PIECE_KINDS = ("banner", "round", "joiner", "menu", "pick", "reasoning", "reasoning_joiner")
#: Counter (a)'s frame (A-m2 v0.5 §3.4: "keep the banner's `=== … ===` frame"; Code's P2 in the pre-read).
FRAME_RX = re.compile(r"=== .+? ===")


def domain(transcript: str, pieces: Sequence[Mapping[str, Any]], upto: int) -> tuple[str, ...]:
    """A-m2 v0.5 §1: the complete harness-written lines of the session, as rendered before offset ``upto``
    (the start of the reasoning line's own piece), distinct, in first-occurrence order."""
    # PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §1, m:265; Code's P1 of the A-m2 pre-read;
    # F25 re-declared): over the pieces, which tile the transcript, the span before ``upto`` splits into
    # newline-terminated lines; a line is in the domain iff no model-written piece (generation, reasoning_text)
    # touches it: none overlaps any of its characters, its newline included, and no zero-length one sits within
    # it. A model text can hold a newline, so overlap, not a piece's start, decides. Every other piece kind is the
    # harness's. An unterminated final fragment is not a complete line. Each line is kept as rendered (labels
    # included); distinct by its ws_norm form, first occurrence kept; each non-empty after ws_norm (asserted: no
    # harness line of F3 is blank). So the banner, its Note lines, every round header, every Task line, every menu
    # line and the pick line as rendered are in it; a Response line and, under F-b, the reasoning label line are
    # not (the model continues each).
    if not isinstance(transcript, str) or type(upto) is not int or not 0 <= upto <= len(transcript):
        raise ValueError("domain: a transcript and an offset inside it")
    kinds = {p.get("kind") for p in pieces}
    unknown = kinds - set(MODEL_PIECE_KINDS) - set(HARNESS_PIECE_KINDS)
    if unknown:
        raise ValueError(f"domain: unknown piece kinds {sorted(map(str, unknown))}")
    spans = [(int(p["start"]), int(p["end"])) for p in pieces if p.get("kind") in MODEL_PIECE_KINDS]
    out: list[str] = []
    seen: set[str] = set()
    a = 0
    while True:
        b = transcript.find("\n", a, upto)
        if b < 0:
            break
        if not any(ps <= b and (pe > a if pe > ps else ps >= a) for ps, pe in spans):
            k = m_audit.ws_norm(transcript[a:b])
            if not k:
                raise ValueError(f"domain: an empty harness line at offset {a}")
            if k not in seen:
                seen.add(k)
                out.append(transcript[a:b])
        a = b + 1
    return tuple(out)


def domain_before_line(transcript: str, pieces: Sequence[Mapping[str, Any]], seg: str) -> tuple[str, ...]:
    """The domain for the reasoning line generated after ``transcript`` + ``seg`` (its block, the harness's
    piece): the runner's and the verifier's one form, on their own transcript builders."""
    a = len(transcript)
    blk = {"kind": "reasoning", "phase": "free", "idx": None, "start": a, "end": a + len(seg)}
    return domain(transcript + seg, list(pieces) + [blk], a + len(seg))


def domain_of_record(rec: Mapping[str, Any], ci: int) -> tuple[str, ...]:
    """A record's domain at its reasoning line ``ci``: the lines before that line's reasoning_text piece."""
    texts = [p for p in rec["pieces"] if p.get("kind") == "reasoning_text"]
    if type(ci) is not int or not 0 <= ci < len(texts):
        raise ValueError(f"domain_of_record: no reasoning line {ci!r}")
    return domain(rec["transcript"], rec["pieces"], int(texts[ci]["start"]))


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


def echo_match(text: str, echo_set: Sequence[str]) -> int | None:
    """A-m2 v0.5 §1's match: the first line of ``echo_set`` equal to ``text`` after ws_norm; None if none."""
    t = m_audit.ws_norm(text)
    return next((i for i, ln in enumerate(echo_set) if m_audit.ws_norm(ln) == t), None)


def classify_line(text: str, *, n_tok: int, cap: int, stop_reason: str, cap_hit: bool,
                  echo_set: Sequence[str], scaffold_strings: Sequence[str]) -> LineAudit:
    """m:265's classes for one generated reasoning line; ``echo_set`` is the line's domain (A-m2 v0.5 §1)."""
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
    # PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §1: "equality after whitespace normalization
    # (runs of whitespace collapsed, ends stripped; case-sensitive)"; F28 re-declared): echo = the first line of
    # the domain (``echo_set``, domain order) whose ws_norm form equals the line's; Q8's containment is
    # withdrawn from the class and is counter (a)'s.
    if not isinstance(text, str):
        raise TypeError("a reasoning line's text is a str")
    if type(n_tok) is not int or n_tok < 0 or type(cap) is not int or cap <= 0 or type(cap_hit) is not bool:
        raise ValueError("n_tok, cap and cap_hit must be a non-negative int, a positive int and a bool")
    if stop_reason not in ("newline", "cap", "eos"):
        raise ValueError(f"stop_reason must be newline / cap / eos, got {stop_reason!r}")
    if cap_hit != (stop_reason == "cap") or (cap_hit and n_tok != cap) or n_tok > cap:
        raise ValueError(f"the generation's cap fields disagree (n_tok {n_tok}, cap {cap}, cap_hit {cap_hit}, "
                         f"stop_reason {stop_reason!r})")
    if isinstance(echo_set, str) or not all(isinstance(x, str) for x in echo_set):
        raise TypeError("echo_set is the line's domain, a sequence of str")
    classes = []
    if m_audit.ws_norm(text) == "":
        classes.append("empty")
    if cap_hit:
        classes.append("cap_no_newline")
    echo = echo_match(text, tuple(echo_set))
    if echo is not None:
        classes.append("echo")
    return LineAudit(classes=tuple(classes), echo_line=echo,
                     scaffold=m_audit._scaffold_hits(text, tuple(scaffold_strings)))


def counter_a(text: str, dom: Sequence[str]) -> bool:
    """A-m2 v0.5 §3.4's counter (a): the line contains a complete harness-written line of the session
    (ws_norm both, case-sensitive) or keeps the banner's ``=== … ===`` frame."""
    # PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §3.4, "Q8's containment, as a counter"; Code's
    # P2 of the pre-read, the smoke's form): containment over the line's domain, or FRAME_RX on the ws_norm
    # text. An echo line contains its domain line, so (a) counts every echo line too.
    t = m_audit.ws_norm(text)
    return any(m_audit.ws_norm(ln) in t for ln in dom) or bool(FRAME_RX.search(t))


def counter_a_of_record(rec: Mapping[str, Any]) -> list[bool]:
    """Counter (a) per reasoning line of a record, in line order, each over its own domain."""
    return [counter_a(x["text"], domain_of_record(rec, ci)) for ci, x in enumerate(rec.get("reasoning") or [])]


def b_candidates(rec: Mapping[str, Any]) -> list[dict]:
    """A-m2 v0.5 §3.4's counter (b), its domain: the record's task responses that no audit class claims,
    each with its phase, index and path (Code's declared read decides which attempt no task). ``rec`` is a
    full record, a stage's read of a sham session (its rounds keep their audit), a stage's read of a contrast
    session outside G-TIME-F3 (its forced rounds keep theirs), or G-TIME-F3's contrast read (ruling (h))."""
    # PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; the build review's findings 1 and 2): every task round
    # of a full record carries its audit (scaffold's round record), so a round with no audit mapping is refused
    # -- the domain fails closed -- except in G-TIME-F3's contrast read, whose rounds keep {phase, ri, n, text}
    # only (ruling (h); m.readrule.TIME_ROUND_KEEP). There the claimed round follows from m.audit.qwen_ends,
    # "forced -> any claim" under the lenient scope: a claimed forced round ends the session, so the one
    # claimed round is the last one generated when the read says excluded_at_forced, and no other (Code's
    # reading). Each candidate carries the record's path, which tells a G-ID-F3 pair's two members apart.
    rounds = list(rec.get("rounds") or [])
    time_contrast = (rec.get("stage") == "time" and rec.get("contrast") is True
                     and isinstance(rec.get("excluded_at_forced"), bool)
                     and all(r.get("phase") == "forced" and "audit" not in r for r in rounds))
    out = []
    for k, r in enumerate(rounds):
        ph = r.get("phase")
        if time_contrast:
            claimed = rec["excluded_at_forced"] and k == len(rounds) - 1
        elif not isinstance(r.get("audit"), Mapping):
            raise ValueError(f"b_candidates: a {ph} round carries no audit mapping (a redacted read outside "
                             f"G-TIME-F3's contrast form?); refused")
        else:
            claimed = r["audit"].get("claim") is not None
        if not claimed:
            out.append({"phase": ph, "idx": r.get("ri") if ph == "forced" else r.get("ci"), "n": r.get("n"),
                        "path": rec.get("path"), "text": r.get("text")})
    return out


def tabulate_b(records: Sequence[Mapping[str, Any]], items: Sequence[Mapping[str, Any]]) -> dict:
    """Counter (b)'s table from Code's declared read: ``items`` = [{stage, template, s, path, phase, idx}], each
    a candidate of its record (refused otherwise, and refused twice); per template and phase, over all sessions
    the records give, excluded included. Two records under one (stage, template, s, path) are refused."""
    cands: dict[tuple, Mapping] = {}
    rec_keys: set[tuple] = set()
    for rec in records:
        rk = (rec["stage"], rec["template"], rec["s"], rec.get("path"))
        if rk in rec_keys:
            raise ValueError(f"tabulate_b: two records under {rk}")
        rec_keys.add(rk)
        for c in b_candidates(rec):
            cands[rk + (c["phase"], c["idx"])] = c
    out: dict = {}
    seen: set[tuple] = set()
    for it in items:
        k = (it["stage"], it["template"], it["s"], it["path"], it["phase"], it["idx"])
        if k not in cands:
            raise ValueError(f"tabulate_b: {k} is not a response no audit class claims")
        if k in seen:
            raise ValueError(f"tabulate_b: {k} listed twice")
        seen.add(k)
        out.setdefault(it["template"], {}).setdefault(it["phase"], 0)
        out[it["template"]][it["phase"]] += 1
    return out


def review_hits(text: str) -> tuple[str, ...]:
    """The Q4 counter's case-sensitive substring hits in one generated text, in declared order."""
    return tuple(s for s in REVIEW_STRINGS if s in text)


def review_counter(records: Sequence[Mapping[str, Any]]) -> dict:
    """The Q4 descriptive counter (rule 23): per template and string, the generations (task rounds
    and reasoning lines) whose text contains the string, over ALL sessions, excluded included.
    Reported in VERDICTS; it decides nothing."""
    # PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q4): the unit is the generation (a task round
    # or a reasoning line), keyed (template, kind, string); a generation containing two of the strings
    # counts once under each. Its home is this module. At VERDICTS the analyzer is untouched: Code tabulates it
    # with this module's functions over the same records in its own step, reported in the VERDICTS entry beside the
    # analyzer's outputs (A-m2 v0.5 §3.4, which corrects F29's "the analyzer tabulates it" at the lock's re-issue).
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

    from . import banner

    ss = A.qwen_audit_of_record()[0].v2.ban_strings
    # a hand-built F3 transcript: banner, one forced round, the first reasoning block (F-b), its line, the menu,
    # the pick, the chosen round, then the second block (F-b) -- each piece as the runner adds it
    head = "=== Config evaluation session ===\n" + banner.COMMON + "\n"
    pieces: list[dict] = [{"kind": "banner", "start": 0, "end": len(head)}]
    t = head

    def add(kind: str, frag: str) -> None:
        nonlocal t
        pieces.append({"kind": kind, "start": len(t), "end": len(t) + len(frag)})
        t += frag

    add("round", "[round 1 | config: granite]\nTask: Compute 9 minus 4.\nResponse:")
    add("generation", " Five.")
    add("joiner", "\n")
    blk5 = banner.reasoning_block(5)
    dom5 = domain_before_line(t, pieces, blk5)
    add("reasoning", blk5)
    add("reasoning_text", "granite answered.")
    add("reasoning_joiner", "\n")
    add("menu", "[round 5 | choice]\nWhich config runs round 5? granite or plaza\nConfig choice (one word):")
    add("pick", " granite\n")
    add("round", "[round 5 | config: granite]\nTask: Name a color.\nResponse:")
    add("generation", " Blue.\n[round 6 | choice]")
    add("joiner", "\n")
    blk6 = banner.reasoning_block(6)
    dom6 = domain_before_line(t, pieces, blk6)
    chk("mf3.lines: the domain (A-m2 v0.5 §1; P1) -- the banner, its Note line, round headers, Task lines, the "
        "menu's lines and the pick line as rendered, the block's header; not a Response line, not F-b's label line, "
        "not a header inside a model text; distinct, in first-occurrence order",
        dom5 == ("=== Config evaluation session ===", banner.COMMON, "[round 1 | config: granite]",
                 "Task: Compute 9 minus 4.", "[round 5 | reasoning]")
        and dom6 == dom5 + ("[round 5 | choice]", "Which config runs round 5? granite or plaza",
                            "Config choice (one word): granite", "[round 5 | config: granite]", "Task: Name a color.",
                            "[round 6 | reasoning]")
        and not any(x.startswith(("Response:", "Reasoning (one line)")) for x in dom6), (dom5, dom6))
    rec = {"transcript": t + blk6 + "plaza next.\n", "pieces": pieces + [
        {"kind": "reasoning", "start": len(t), "end": len(t) + len(blk6)},
        {"kind": "reasoning_text", "start": len(t) + len(blk6), "end": len(t) + len(blk6) + len("plaza next.")},
        {"kind": "reasoning_joiner", "start": len(t) + len(blk6) + len("plaza next."),
         "end": len(t) + len(blk6) + len("plaza next.") + 1}],
        "reasoning": [{"text": "granite answered."}, {"text": "plaza next."}], "rounds": []}
    chk("mf3.lines: domain_of_record on the finished record equals domain_before_line at generation, line by line",
        domain_of_record(rec, 0) == dom5 and domain_of_record(rec, 1) == dom6)
    # zero-length model pieces: an empty response and an empty F-b line touch their lines
    t0 = "=== B ===\n"
    p0 = [{"kind": "banner", "start": 0, "end": len(t0)}]
    for kind, frag in (("round", "[round 1 | config: x]\nTask: T.\nResponse:"), ("generation", ""), ("joiner", "\n"),
                       ("reasoning", "[round 5 | reasoning]\nReasoning (one line): So far,"),
                       ("reasoning_text", ""), ("reasoning_joiner", "\n"), ("menu", "M\nlast")):
        p0.append({"kind": kind, "start": len(t0), "end": len(t0) + len(frag)})
        t0 += frag
    chk("mf3.lines: a zero-length model piece touches its line (an empty response, an empty F-b line); an "
        "unterminated final fragment is no line",
        domain(t0, p0, len(t0)) == ("=== B ===", "[round 1 | config: x]", "Task: T.", "[round 5 | reasoning]", "M"))
    refused = []
    for fn in (lambda: domain("a\n\nb\n", [{"kind": "banner", "start": 0, "end": 5}], 5),
               lambda: domain("a\n", [{"kind": "mystery", "start": 0, "end": 2}], 2),
               lambda: domain("a\n", [], 3), lambda: domain_of_record(rec, 2)):
        try:
            fn()
            refused.append(False)
        except ValueError:
            refused.append(True)
    chk("mf3.lines: refuses an empty harness line, an unknown piece kind, an offset outside the transcript, a "
        "line the record does not have", all(refused), refused)

    def cl(text, n_tok=5, cap=120, stop="newline", hit=False, es=dom6):
        return classify_line(text, n_tok=n_tok, cap=cap, stop_reason=stop, cap_hit=hit, echo_set=es,
                             scaffold_strings=ss)

    clean = ["Both configs gave answerable tasks so far.", "The tasks look fine.", "Seven."]
    chk("mf3.lines: clean lines carry no class and no scaffold hit",
        all(cl(x).classes == () and cl(x).scaffold == () for x in clean))
    e = cl("  \t ", n_tok=120, stop="cap", hit=True)
    e2 = cl("\n\n\n", n_tok=120, stop="cap", hit=True)
    chk("mf3.lines: empty = whitespace-only after ws_norm (with the cap reached it is also cap_no_newline)",
        e.classes == ("empty", "cap_no_newline") and e2.classes == ("empty", "cap_no_newline")
        and cl("", n_tok=0, stop="eos").classes == ("empty",))
    c = cl("x " * 60, n_tok=120, stop="cap", hit=True)
    nl = cl("x " * 59, n_tok=119, stop="newline")
    chk("mf3.lines: cap_no_newline = stopped on the cap (n_tok == cap); a newline as the cap-th sampled "
        "token is a newline stop, not cap-reach; also at cap 60",
        c.classes == ("cap_no_newline",) and nl.classes == ()
        and cl("y", n_tok=60, cap=60, stop="cap", hit=True).classes == ("cap_no_newline",))
    eq = {"banner": "=== Config evaluation session ===", "COMMON": banner.COMMON, "header": "[round 6 | reasoning]",
          "task": "Task: Name a color.", "pick line": "Config choice (one word): granite",
          "spaced": "  " + banner.COMMON.replace(" ", "   ") + " "}
    got = {k: (cl(v).classes, cl(v).echo_line) for k, v in eq.items()}
    chk("mf3.lines: echo fires on a domain line reproduced verbatim after ws_norm (the banner, COMMON, a header "
        "written so far, a Task line, the pick line as rendered, extra whitespace) and reports its domain index",
        all(v[0] == ("echo",) for v in got.values()) and got["COMMON"][1] == 1 and got["header"][1] == 10, got)
    nots = {"prefixed": "As the note says: " + banner.COMMON + " So I pick one.",
            "a header not yet written": "[round 7 | reasoning]", "lower case": banner.COMMON.lower(),
            "no period": banner.COMMON[:-1], "F-b's label line": "Reasoning (one line): So far,",
            "m:174's label": "Reasoning (one line):", "a TOLD line the session never wrote": banner.TOLD_OBJ,
            "a Response line": "Response: Blue."}
    got_n = {k: cl(v).classes for k, v in nots.items()}
    chk("mf3.lines: no echo for a containing line (Q8's containment withdrawn, A-m2 v0.5 §1), a header not yet "
        "written, a case change, a missing period, F-b's or m:174's label, a line the session never wrote, a "
        "Response line",
        all(v == () for v in got_n.values()), got_n)
    ca = {k: counter_a(v, dom6) for k, v in {**eq, **nots}.items()}
    want_a = {**{k: True for k in eq}, "prefixed": True, "a header not yet written": False, "lower case": False,
              "no period": False, "F-b's label line": False, "m:174's label": False,
              "a TOLD line the session never wrote": False, "a Response line": False}
    frames = {f: counter_a(f, ()) for f in ("=== Config selection ===", "x === y === z", "[=== a ===]", "=== ===")}
    chk("mf3.lines: counter (a) -- containment of a domain line (every echo line, the prefixed one) or the "
        "`=== … ===` frame (A-m2 v0.5 §3.4); not a line that contains no complete domain line",
        ca == want_a and frames == {"=== Config selection ===": True, "x === y === z": True, "[=== a ===]": True,
                                    "=== ===": False}, (ca, frames))
    chk("mf3.lines: counter_a_of_record recomputes each line over its own domain",
        counter_a_of_record(rec) == [False, False]
        and counter_a_of_record({**rec, "reasoning": [{"text": "x [round 5 | reasoning] y"},
                                                      {"text": "[round 5 | choice]"}]}) == [True, True])
    sc_ = cl("fine <|im_end|> here")
    chk("mf3.lines: scaffold hits are the Qwen scaffold set's case-sensitive substrings (no class)",
        sc_.scaffold == ("<|im_end|>",) and sc_.classes == ())
    multi = cl(banner.COMMON + " " * 3, n_tok=120, stop="cap", hit=True)
    chk("mf3.lines: classes are a set in declared order; the defect is their union once per line",
        multi.classes == ("cap_no_newline", "echo") and multi.defect
        and LineAudit.from_dict(multi.as_dict()) == multi)
    refused = []
    for fn in (lambda: cl("x", n_tok=120, stop="newline", hit=True), lambda: cl("x", n_tok=119, stop="cap", hit=True),
               lambda: cl("x", n_tok=121, stop="newline"), lambda: cl("x", stop="stop"),
               lambda: cl("x", es="[round 5 | reasoning]"), lambda: LineAudit(classes=("echo",)),
               lambda: LineAudit(classes=("echo", "empty"), echo_line=1),
               lambda: LineAudit.from_dict({"classes": [], "echo_line": None, "scaffold": [], "defect": True})):
        try:
            fn()
            refused.append(False)
        except (ValueError, TypeError):
            refused.append(True)
    chk("mf3.lines: refuses inconsistent cap fields, an unknown stop, a str as the domain, malformed audits",
        all(refused), refused)
    recs_b = [{"stage": "time", "template": "A2s", "s": 0, "path": "uncached",
               "rounds": [{"phase": "forced", "ri": 0, "n": 1, "text": "Five.", "audit": {"claim": None}},
                          {"phase": "forced", "ri": 1, "n": 2, "text": "Here is the evaluation:", "audit": {"claim": None}},
                          {"phase": "free", "ci": 0, "n": 5, "text": "x x x", "audit": {"claim": "v2"}},
                          {"phase": "free", "ci": 1, "n": 6, "text": "Perfect.", "audit": {"claim": None}}]}]
    bc = b_candidates(recs_b[0])
    it_ = lambda **k: {"stage": "time", "template": "A2s", "s": 0, "path": "uncached", **k}
    tb = tabulate_b(recs_b, [it_(phase="forced", idx=1), it_(phase="free", idx=1)])
    b_ref = []
    for items in ([it_(phase="free", idx=0)], [it_(phase="forced", idx=1)] * 2,
                  [it_(phase="forced", idx=1, path="cached")]):
        try:
            tabulate_b(recs_b, items)
            b_ref.append(False)
        except ValueError:
            b_ref.append(True)
    chk("mf3.lines: counter (b)'s candidates are the unclaimed task responses with phase, index and path; the table "
        "counts Code's declared items per template and phase, refusing a claimed response, a repeat and a path the "
        "records do not hold",
        [(c_["phase"], c_["idx"], c_["path"]) for c_ in bc] == [("forced", 0, "uncached"), ("forced", 1, "uncached"),
                                                                 ("free", 1, "uncached")]
        and tb == {"A2s": {"forced": 1, "free": 1}} and all(b_ref), (bc, tb, b_ref))
    # a G-ID-F3 pair: two members under one (stage, template, s), told apart by path (the build review's finding 1)
    pair = [{**recs_b[0], "stage": "id", "path": pth} for pth in ("uncached", "cached")]
    tb_pair = tabulate_b(pair, [{**it_(phase="free", idx=1), "stage": "id", "path": pth} for pth in ("uncached", "cached")])
    try:
        tabulate_b(pair + [pair[0]], [])
        twice = False
    except ValueError:
        twice = True
    # G-TIME-F3's contrast read (ruling (h): {phase, ri, n, text} only; the build review's finding 2)
    tr = {"stage": "time", "template": "A2", "s": 0, "path": "uncached", "contrast": True,
          "rounds": [{"phase": "forced", "ri": i, "n": i + 1, "text": f"Answer {i}."} for i in range(3)]}
    tc_ex, tc_ok = b_candidates({**tr, "excluded_at_forced": True}), b_candidates({**tr, "excluded_at_forced": False})
    redacted = []
    for bad in ({**recs_b[0], "rounds": [{"phase": "free", "ci": 0, "n": 5, "text": "x"}]},
                {**tr, "excluded_at_forced": True, "stage": "qual"}, {**tr}):
        try:
            b_candidates(bad)
            redacted.append(False)
        except ValueError:
            redacted.append(True)
    chk("mf3.lines: counter (b) keys a G-ID-F3 pair's members by path (both counted; two records under one key "
        "refused); on G-TIME-F3's contrast read the claimed round is the last forced round of a session excluded at "
        "forced (m.audit.qwen_ends: a forced claim ends the session) and none otherwise; a round with no audit "
        "mapping in any other form is refused (the domain fails closed)",
        tb_pair == {"A2s": {"free": 2}} and twice
        and [c_["idx"] for c_ in tc_ex] == [0, 1] and [c_["idx"] for c_ in tc_ok] == [0, 1, 2] and all(redacted),
        (tb_pair, twice, tc_ex, tc_ok, redacted))
    recs = [{"template": "A3", "rounds": [{"text": "You are a helpful assistant. Seven."}],
             "reasoning": [{"text": "4assistant <|end|>"}]},
            {"template": "A3s", "rounds": [{"text": "Seven."}], "reasoning": []}]
    chk("mf3.lines: the Q4 review counter tabulates the three strings per template and kind",
        review_counter(recs) == {"A3": {"round": {"You are a helpful assistant.": 1},
                                        "line": {"4assistant": 1, "<|end|>": 1}}}
        and review_hits("nothing") == ())
