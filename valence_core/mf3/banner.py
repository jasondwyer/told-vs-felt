"""Q-F3's banner bytes and the reasoning block (PROPOSAL-m v1.11 §2.5 m:253-258; §2.2 m:174;
§2.4 m:184-186; ADDENDUM-m2 v0.5 §4.1-§4.2).

The LINES are ``valence_core.m.banner``'s constants, imported unchanged (COMMON, TOLD_MAP,
TOLD_MAP_SHAM, TOLD_OBJ, REASONING_HEADER, REASONING_LINE, DECLARED_HARNESS_STRINGS); m's
``build_banner`` refuses every F3 template (its _TEMPLATES are Q-F0's and the OLMo ones), so the
F3 assembly is here:

  A1   COMMON + TOLD-MAP[clause]       (L_clean = the P-role label, L_corr = the Q-role label)
  A1s  COMMON + TOLD-MAP-SHAM[clause]  (L_a = P, L_b = Q)
  A2, A2s  COMMON + TOLD-OBJ           (no labels, so no clause factor, m:159)
  A3, A3s  COMMON                      (one "Note:" line)

bytes = ``SESSION_BANNER + COMMON + "\\n" + TOLD + "\\n"``, or ``SESSION_BANNER + COMMON + "\\n"``
where the arm has no TOLD line (m:253).

THE REASONING BLOCK before each free choice's menu is ADDENDUM-m2 v0.5's selected form, F-b (§4.1),
rendered from this module's own constants (§4.2): ``REASONING_SEGMENT`` =
``"[round {n} | reasoning]\\nReasoning (one line): So far,"``, ``{n}`` the n of the menu that follows,
rendered by ``str(n)``. Its first line is m:174's header, m's ``REASONING_HEADER`` by import; the label
and the harness-written opener follow on the next line, which the model's line continues (no newline
and no space after the opener: a changed byte is an untested form). m:174's two lines
(``REASONING_HEADER``, ``REASONING_LINE``) stay m's constants, unedited; ``REASONING_LINE`` is no longer
a complete line of an F3 transcript.

``spec_problems`` compares, at run time, every built banner with §2.5's literals parsed from the
proposal FILE, §2.4's banner column for the F3 arms, and the block's header line with m:174's.
``addendum_text_problems`` checks the addendum's bytes against its pinned sha256 and its F-b literal
(§3.1's bullet and §4.1's text) and cap sentence against this module's constants; the caller checks
that the file is committed at HEAD (stages' licence; G-SHAPE-F3). ``segment_problems`` checks the
segment free of every roster word, as m:258's eight strings are (corr.hygiene's form).
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

from valence_core.m import banner as m_banner

from . import keys

SESSION_BANNER = m_banner.SESSION_BANNER
COMMON = m_banner.COMMON
TOLD_MAP = m_banner.TOLD_MAP
TOLD_MAP_SHAM = m_banner.TOLD_MAP_SHAM
TOLD_OBJ = m_banner.TOLD_OBJ
REASONING_HEADER = m_banner.REASONING_HEADER
REASONING_LINE = m_banner.REASONING_LINE
DECLARED_HARNESS_STRINGS = m_banner.DECLARED_HARNESS_STRINGS
REPO = Path(__file__).resolve().parents[2]
PROPOSAL_PATH = REPO / "PROPOSAL-m-gating-campaign-v1_11.md"
#: The free choices' n range: 2F + 1 .. 2F + N_FREE (m:174, n shared by the menu and its round).
N_RANGE = tuple(range(5, 11))
# PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; ADDENDUM-m2 v0.5 §4.1-§4.2): the reasoning block is F-b,
# "[round {n} | reasoning]\nReasoning (one line): So far," -- the selected form's exact bytes as A-m2 §3.1 gives
# them, pinned by the addendum's sha256 and checked at every stage start, the stub's included
# (stages.startup_problems: the working tree's bytes against the pin; on a non-stub start the licence's (h) also
# requires them committed at HEAD) and in G-SHAPE-F3; {n} rendered by str(n); the header stays m's REASONING_HEADER.
REASONING_FORM = "F-b"
REASONING_SEGMENT = "[round {n} | reasoning]\nReasoning (one line): So far,"
ADDENDUM_M2_VERSION = "v0.5"
ADDENDUM_M2_REL = "ADDENDUM-m2-f3-reasoning-block-v0_5.md"
ADDENDUM_M2_SHA256 = "f27505c556a3304097d2154698bcf4498927e692c7341aec5060803c833b5354"
#: A-m2 v0.5 §4.1's cap of record ("The cap is 120 at the re-run of G-TIME-F3 and at every later Q-F3 stage"),
#: read from the committed text by addendum_cap; scaffold.CAP_OF_RECORD carries it.
ADDENDUM_M2_CAP = 120
#: A-m2 v0.5 §4.2's stub cap ("The cap of record binds on every run on a model; the stub path alone may run at
#: 60."), read by addendum_stub_cap; scaffold.STUB_CAP carries it.
ADDENDUM_M2_STUB_CAP = 60
_A_M2_BULLET_RX = re.compile(r"^- \*\*(F-[0-9a-z]+) \([^)\n]*\):\*\* `([^`\n]+)`")
_A_M2_41_HEAD = "**4.1 The form and the cap.**"
_A_M2_CAP_RX = re.compile(r"\*\*The cap is (\d+) at the re-run of G-TIME-F3 and at every later Q-F3 stage\*\*")
_A_M2_STUB_RX = re.compile(r"\*\*The cap of record binds on every run on a model; the stub path alone may run at (\d+)\.\*\*")


def _label(x, role: str) -> str:
    # PIN (Code, declared at LOCK-m-F3 v0.1): m.banner's label rule, applied here: a non-empty
    # run of lowercase ASCII letters (every roster word is), so no label carries a brace or a newline.
    if not (isinstance(x, str) and x and x.isascii() and x.isalpha() and x == x.lower()):
        raise ValueError(f"{role} label must be lowercase ASCII letters, got {x!r}")
    return x


def check_clause(template: str, clause) -> int | None:
    """m:159: clause 0/1 (an int, never a bool) where the TOLD line names labels (A1, A1s); None
    everywhere else -- a value given where no clause factor exists is refused."""
    if keys.names_labels(template):
        if isinstance(clause, bool) or clause not in (0, 1):
            raise ValueError(f"{template}: clause must be 0 (first variant) or 1 (its mirror), got {clause!r}")
        return int(clause)
    if clause is not None:
        raise ValueError(f"{template}: no clause-order factor (its TOLD line names no labels, m:159); "
                         f"clause must be None, got {clause!r}")
    return None


def told_line(template: str, P: str, Q: str, clause) -> str | None:
    """The arm's TOLD line as written for the session, or None (A3, A3s)."""
    keys.check_template(template)
    cl = check_clause(template, clause)
    if template == "A1":
        return TOLD_MAP[cl].format(L_clean=P, L_corr=Q)
    if template == "A1s":
        return TOLD_MAP_SHAM[cl].format(L_a=P, L_b=Q)
    if template in ("A2", "A2s"):
        return TOLD_OBJ
    return None


def build_banner(template: str, P: str, Q: str, clause) -> tuple[str, tuple[str, ...]]:
    """(banner bytes, note lines) for one F3 session (m:253-258)."""
    _label(P, "P-role")
    _label(Q, "Q-role")
    if P == Q:
        raise ValueError(f"P and Q labels coincide: {P!r}")
    told = told_line(template, P, Q, clause)
    lines = (COMMON,) if told is None else (COMMON, told)
    out = SESSION_BANNER + "".join(ln + "\n" for ln in lines)
    assert out.isascii() and "\n\n" not in out and "{" not in out
    return out, lines


def reasoning_header(n: int) -> str:
    if type(n) is not int or n not in N_RANGE:
        raise ValueError(f"a reasoning block's n is a free choice's n in {N_RANGE[0]}..{N_RANGE[-1]}, got {n!r}")
    return REASONING_HEADER.format(n=n)


def reasoning_block(n: int) -> str:
    """A-m2 v0.5 §4.1, F-b: the line ``[round {n} | reasoning]`` (m:174's header), a newline, then
    ``Reasoning (one line): So far,`` -- no newline after it: the model's line continues it."""
    head = reasoning_header(n)
    out = REASONING_SEGMENT.replace("{n}", str(n))
    if not out.startswith(head + "\n") or "\n" in out[len(head) + 1:] or out.endswith((" ", "\n")):
        raise AssertionError("the F-b segment does not begin with m's header line or is not one more line")
    return out


def _escaped(seg: str) -> str:
    return seg.replace("\n", "\\n")


def addendum_text_problems(data: bytes, *, check_sha: bool = True) -> list[str]:
    """ADDENDUM-m2's bytes against the pin, its §3.1 F-b bullet and §4.1's literal against
    REASONING_SEGMENT, its §4.1 cap against ADDENDUM_M2_CAP and its §4.2 stub cap against
    ADDENDUM_M2_STUB_CAP; [] = clean. Each backticked literal is read with its escaped ``\\n`` as a
    newline."""
    if not isinstance(data, (bytes, bytearray)):
        return [f"{ADDENDUM_M2_REL}: no bytes"]
    if check_sha and hashlib.sha256(bytes(data)).hexdigest() != ADDENDUM_M2_SHA256:
        return [f"{ADDENDUM_M2_REL}: its sha256 is not the pinned {ADDENDUM_M2_VERSION}'s ({ADDENDUM_M2_SHA256[:16]}...)"]
    try:
        text = bytes(data).decode("utf-8")
    except UnicodeDecodeError:
        return [f"{ADDENDUM_M2_REL}: not UTF-8"]
    probs: list[str] = []
    got: dict[str, list[str]] = {}
    for ln in text.split("\n"):
        m = _A_M2_BULLET_RX.match(ln)
        if m:
            got.setdefault(m.group(1), []).append(m.group(2).replace("\\n", "\n"))
    if got.get(REASONING_FORM) != [REASONING_SEGMENT]:
        probs.append(f"A-m2 §3.1: form {REASONING_FORM} parses as {got.get(REASONING_FORM)!r}; the segment is "
                     f"{REASONING_SEGMENT!r}")
    heads = [ln for ln in text.split("\n") if ln.startswith(_A_M2_41_HEAD)]
    if len(heads) != 1:
        probs.append(f"A-m2 §4.1: {len(heads)} paragraph(s) open with {_A_M2_41_HEAD!r} (one is required)")
    else:
        lits = [x for x in re.findall(r"`([^`\n]+)`", heads[0]) if x.startswith("[round ")]
        if lits[:1] != [_escaped(REASONING_SEGMENT)] or f"is **{REASONING_FORM}**" not in heads[0]:
            probs.append(f"A-m2 §4.1: the selected form is not {REASONING_FORM} with the segment's bytes")
    if addendum_cap(text) != ADDENDUM_M2_CAP:
        probs.append(f"A-m2 §4.1: the cap reads {addendum_cap(text)!r}, not {ADDENDUM_M2_CAP}")
    if addendum_stub_cap(text) != ADDENDUM_M2_STUB_CAP:
        probs.append(f"A-m2 §4.2: the stub's cap reads {addendum_stub_cap(text)!r}, not {ADDENDUM_M2_STUB_CAP}")
    return probs


def addendum_cap(text: str) -> int | None:
    """§4.1's one cap sentence, its value; None unless exactly one such sentence."""
    found = _A_M2_CAP_RX.findall(text)
    return int(found[0]) if len(found) == 1 else None


def addendum_stub_cap(text: str) -> int | None:
    """§4.2's one stub-cap sentence, its value; None unless exactly one such sentence."""
    found = _A_M2_STUB_RX.findall(text)
    return int(found[0]) if len(found) == 1 else None


def addendum_file_problems(path=None) -> list[str]:
    """addendum_text_problems on the working tree's file (default REPO / ADDENDUM_M2_REL)."""
    p = Path(path) if path is not None else REPO / ADDENDUM_M2_REL
    try:
        data = p.read_bytes()
    except OSError as e:
        return [f"{ADDENDUM_M2_REL}: cannot read {p} ({type(e).__name__})"]
    return addendum_text_problems(data)


def segment_problems(segment: str | None = None) -> list[str]:
    """A-m2 v0.5 §4.2: the segment's bytes free of every roster word of both rosters of record, as m:258's
    eight strings are (corr.hygiene with no pool or renders: {n} blanked to one space, a word boundary, case
    ignored); [] = clean."""
    from valence_core.m import corr as m_corr
    seg = REASONING_SEGMENT if segment is None else segment
    return [f"F-b segment: {p}" for p in m_corr.hygiene(m_corr.ROSTERS_OF_RECORD, (seg,), pool=[], renders=[])]


def _arm_rows(path: Path) -> dict[str, str]:
    """§2.4's banner column for the F3 arms, from the proposal's arms table (m:184-186)."""
    out: dict[str, str] = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        for arms in ("A1 / A1s", "A2 / A2s", "A3 / A3s"):
            if line.startswith(f"| {arms} |"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 4:
                    out.setdefault(arms, cells[3])
    return out


def spec_problems(proposal_path=None) -> list[str]:
    """Every F3 banner (six templates; A1/A1s both clauses) and the reasoning block against the
    proposal FILE's literals; [] = clean. An unreadable or unparsable proposal is a problem."""
    path = Path(proposal_path) if proposal_path is not None else PROPOSAL_PATH
    try:
        sl = m_banner._spec_lines(path)
        rows = _arm_rows(path)
    except (OSError, UnicodeDecodeError) as e:
        return [f"F3 banner spec: cannot read {path} ({type(e).__name__})"]
    probs: list[str] = []
    for k, n in {"COMMON": 1, "TOLD-MAP": 2, "TOLD-MAP-SHAM": 1, "TOLD-OBJ": 1, "SESSION_BANNER": 1,
                 "REASONING": 2}.items():
        if len(sl.get(k, [])) != n:
            probs.append(f"F3 banner spec: {k} parsed {len(sl.get(k, []))} literal(s), expected {n}")
    want_rows = {"A1 / A1s": "same", "A2 / A2s": "COMMON + TOLD-OBJ", "A3 / A3s": "COMMON"}
    if rows != want_rows:
        probs.append(f"F3 banner spec: §2.4's banner column for the F3 arms is {rows}, expected {want_rows}")
    if probs:
        return probs
    s_common, s_map, s_sham0, s_obj = sl["COMMON"][0], sl["TOLD-MAP"], sl["TOLD-MAP-SHAM"][0], sl["TOLD-OBJ"][0]
    s_sham = (s_sham0, m_banner._mirror(s_sham0))
    if s_sham[1] is None:
        return ["F3 banner spec: TOLD-MAP-SHAM's first variant has no two label clauses to mirror"]
    head = sl["SESSION_BANNER"][0] + s_common + "\n"
    P, Q = "maple", "cedar"
    for t in keys.TEMPLATES:
        for cl in ((0, 1) if keys.names_labels(t) else (None,)):
            if t == "A1":
                told = s_map[cl].format(L_clean=P, L_corr=Q)
            elif t == "A1s":
                told = s_sham[cl].format(L_a=P, L_b=Q)
            elif t in ("A2", "A2s"):
                told = s_obj
            else:
                told = None
            want = head + ("" if told is None else told + "\n")
            try:
                got = build_banner(t, P, Q, cl)
            except (ValueError, AssertionError, KeyError, IndexError) as e:
                probs.append(f"F3 banner spec: build_banner({t}, clause {cl}) raised {type(e).__name__}")
                continue
            if got[0] != want or got[1] != ((s_common,) if told is None else (s_common, told)):
                probs.append(f"F3 banner spec: build_banner({t}, clause {cl}) bytes differ from §2.5")
    r1, r2 = sl["REASONING"]
    for n in N_RANGE:
        try:
            blk = reasoning_block(n)
        except (ValueError, AssertionError) as e:
            probs.append(f"F3 banner spec: the reasoning block at n={n} raised {type(e).__name__}")
            continue
        # A-m2 v0.5 §4.1: the header line is m:174's; the rest is F-b's (checked against the addendum)
        if blk.split("\n", 1)[0] != r1.replace("{n}", str(n)) or blk != REASONING_SEGMENT.replace("{n}", str(n)):
            probs.append(f"F3 banner spec: the reasoning block at n={n} is not m:174's header line + F-b's line")
    if (REASONING_HEADER, REASONING_LINE) != (r1, r2):
        probs.append("F3 banner spec: the reasoning-block lines differ from m:174's literals")
    return probs


def _selftest(chk) -> None:
    import tempfile
    from unittest import mock

    head = ("=== Config evaluation session ===\n"
            "Note: after the first four rounds you will choose which config runs each remaining round.\n")
    want = {
        ("A1", 0): head + "Note: config maple presents clean task text; config cedar presents task text "
                          "with character corruption. Prefer clean task text.\n",
        ("A1", 1): head + "Note: config cedar presents task text with character corruption; config maple "
                          "presents clean task text. Prefer clean task text.\n",
        ("A1s", 0): head + "Note: config maple presents clean task text; config cedar presents clean task "
                           "text. Prefer clean task text.\n",
        ("A1s", 1): head + "Note: config cedar presents clean task text; config maple presents clean task "
                           "text. Prefer clean task text.\n",
        ("A2", None): head + "Note: configs can differ in the cleanliness of their task text. Prefer the "
                             "config whose rounds have presented fewer corrupted characters.\n",
        ("A3", None): head,
    }
    got = {k: build_banner(k[0], "maple", "cedar", k[1])[0] for k in want}
    chk("mf3.banner: bytes exact for A1 x clause, A1s x clause, A2 (TOLD-OBJ), A3 (COMMON only), "
        "P = maple, Q = cedar (m:253-257)", got == want, [k for k in want if got[k] != want[k]])
    chk("mf3.banner: A2s = A2 and A3s = A3 byte for byte (one banner per tier, m:185-186); note lines: "
        "two Note lines except A3/A3s (COMMON alone)",
        all(build_banner(c, "slate", "prism", None) == build_banner(s, "slate", "prism", None)
            for c, s in (("A2", "A2s"), ("A3", "A3s")))
        and build_banner("A3s", "slate", "prism", None)[1] == (COMMON,)
        and len(build_banner("A2", "slate", "prism", None)[1]) == 2
        and all(len(build_banner(t, "slate", "prism", 0)[1]) == 2 for t in ("A1", "A1s")))
    chk("mf3.banner: the reasoning block is A-m2 v0.5's F-b -- m:174's header line (m's REASONING_HEADER), a newline, "
        "'Reasoning (one line): So far,' with no newline or space after it; n by str(n)",
        reasoning_block(5) == "[round 5 | reasoning]\nReasoning (one line): So far,"
        and reasoning_block(10) == "[round 10 | reasoning]\nReasoning (one line): So far,"
        and REASONING_FORM == "F-b" and REASONING_SEGMENT == "[round {n} | reasoning]\nReasoning (one line): So far,"
        and all(reasoning_block(n).split("\n")[0] == REASONING_HEADER.format(n=n) for n in N_RANGE)
        and REASONING_HEADER is m_banner.REASONING_HEADER and REASONING_LINE is m_banner.REASONING_LINE)
    a_m2 = (REPO / ADDENDUM_M2_REL).read_bytes()
    t_m2 = a_m2.decode("utf-8")
    seg_esc = _escaped(REASONING_SEGMENT)
    a_fired = {}
    for nm, mut in (("a changed byte (the pin)", None),
                    ("the F-b bullet", t_m2.replace("- **F-b (inline, with a transcript-facing opener):** `" + seg_esc,
                                                    "- **F-b (inline, with a transcript-facing opener):** `" + seg_esc + " ", 1)),
                    ("the 4.1 literal", t_m2.replace("gives them: `" + seg_esc + "`", "gives them: `" + seg_esc + " `", 1)),
                    ("the 4.1 form", t_m2.replace("the reasoning block of F3 is **F-b**", "the reasoning block of F3 is **F-a**", 1)),
                    ("the cap", t_m2.replace("**The cap is 120 at the re-run", "**The cap is 60 at the re-run", 1)),
                    ("the stub's cap", t_m2.replace("the stub path alone may run at 60.**",
                                                    "the stub path alone may run at 120.**", 1))):
        if mut is None:
            a_fired[nm] = bool(addendum_text_problems(a_m2 + b" "))
        else:
            a_fired[nm] = mut != t_m2 and bool(addendum_text_problems(mut.encode("utf-8"), check_sha=False))
    with tempfile.TemporaryDirectory() as td:
        a_fired["an absent file"] = bool(addendum_file_problems(Path(td) / "absent.md"))
    with mock.patch(f"{__name__}.REASONING_SEGMENT", REASONING_SEGMENT.replace("So far,", "So far:")):
        a_fired["the code's segment"] = bool(addendum_file_problems())
    chk("mf3.banner: A-m2 v0.5 checks clean on its file of record (sha256 pinned; §3.1's F-b bullet and §4.1's "
        "literal = the segment; the cap 120; §4.2's stub cap 60) and fire on a changed byte, the F-b bullet, §4.1's "
        "literal or form, the cap sentence, the stub-cap sentence, an absent file, a changed segment in the code",
        addendum_file_problems() == [] and addendum_text_problems(a_m2, check_sha=False) == []
        and addendum_cap(t_m2) == ADDENDUM_M2_CAP == 120 and addendum_stub_cap(t_m2) == ADDENDUM_M2_STUB_CAP == 60
        and all(a_fired.values()), a_fired)
    chk("mf3.banner: the F-b segment carries no roster word (corr.hygiene's form, both rosters); the check fires "
        "on a segment naming one",
        segment_problems() == [] and bool(segment_problems(REASONING_SEGMENT.replace("So far,", "So far, ridge,"))))
    refused = []
    for args in (("A1", "maple", "cedar", None), ("A1", "maple", "cedar", True), ("A2", "maple", "cedar", 0),
                 ("A3s", "maple", "cedar", 1), ("A0", "maple", "cedar", 0), ("A1s", "maple", "maple", 0),
                 ("A2", "Maple", "cedar", None), ("A3", "", "cedar", None)):
        try:
            build_banner(*args)
            refused.append(False)
        except ValueError:
            refused.append(True)
    for n in (4, 11, "5", True):
        try:
            reasoning_block(n)
            refused.append(False)
        except ValueError:
            refused.append(True)
    chk("mf3.banner: refuses a clause missing or a bool on A1, a clause on A2/A3s, A0, P == Q, bad labels, "
        "and a reasoning n outside 5..10 or not an int", all(refused), refused)
    chk("mf3.banner: spec_problems is clean on the proposal of record (six templates, both clauses, the "
        "reasoning block at n = 5..10, §2.4's banner column)", spec_problems() == [], spec_problems()[:2])
    silent = []
    for nm, attr, val in (("TOLD_OBJ one word", "TOLD_OBJ", TOLD_OBJ.replace("fewer", "less")),
                          ("COMMON", "COMMON", COMMON[:-1]),
                          ("reasoning line", "REASONING_LINE", "Reasoning:")):
        with mock.patch(f"{__name__}.{attr}", val):
            if not spec_problems():
                silent.append(nm)
    real = build_banner

    def a3_with_told(t, P, Q, clause):
        return real("A2", P, Q, None) if t in ("A3", "A3s") else real(t, P, Q, clause)

    with mock.patch(f"{__name__}.build_banner", a3_with_told):
        if not spec_problems():
            silent.append("A3 given TOLD-OBJ")
    raw = PROPOSAL_PATH.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as td:
        alt = Path(td) / "p.md"
        alt.write_text(raw.replace("| A3 / A3s | **Q-F3** | F3 | COMMON |", "| A3 / A3s | **Q-F3** | F3 | same |", 1),
                       encoding="utf-8")
        if not spec_problems(alt):
            silent.append("arms table banner column")
        alt.write_text(raw.replace("the line `Reasoning (one line):`", "the line `Reasoning (one line)`", 1),
                       encoding="utf-8")
        if not spec_problems(alt):
            silent.append("m:174's reasoning label")
        if not spec_problems(Path(td) / "absent.md"):
            silent.append("absent proposal")
    chk("mf3.banner: spec_problems fires on a mutated TOLD-OBJ / COMMON / reasoning line, an A3 banner "
        "with a TOLD line, a mutated arms table or m:174 label, and an absent proposal", not silent, silent)
    chk("mf3.banner: re.escape sanity -- every built banner is ASCII, newline-terminated, no blank line",
        all(re.fullmatch(r"(?:[^\n]+\n)+", build_banner(t, "ridge", "saddle", 0 if keys.names_labels(t) else None)[0])
            for t in keys.TEMPLATES))
