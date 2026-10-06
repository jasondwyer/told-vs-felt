"""PROPOSAL-m banner lines (v1.11 §2.5, m:253-258), Q-F0 and OLMo templates.

BYTES (m:253). `SESSION_BANNER + COMMON + "\\n" + TOLD + "\\n"`, every line
newline-terminated, no blank line, round 1's header immediately after;
`SESSION_BANNER` is session_e2a's (session_e2a.py:69), which b3 imports on
OLMo, so one constant serves both substrates. `{L_clean}` / `{L_a}` = the
P-role label, `{L_corr}` / `{L_b}` = the Q-role label, from the session's
scheduled pair and map. Clause 0 = the first variant of m:255-256, clause 1 =
its mirror, "the same sentence with the two label clauses in the other
order" (m:253).

LINES (m:254-257, verbatim). COMMON (every arm); TOLD-MAP (A0, A0-OLMo-*),
two variants; TOLD-MAP-SHAM (A0s, A0s-OLMo-*), the first variant quoted and
its mirror built by swapping the clauses; TOLD-OBJ (A2, A2s) is defined for
the record and never used here: "Q-F0 and the OLMo units use five of the six
(all but TOLD-OBJ) and neither reasoning-block line" (m:258). A Q-F0 or OLMo
session's banner carries two "Note:" lines, COMMON and its TOLD line; they
are returned as `note_lines` for the audit's echo class (m:261-262).

`build_banner` is the one constructor; the runners write its bytes and the
verifier rebuilds them (byte-equality is part of `schedule_mismatch`, m:253).
`spec_problems()` compares, at run time, build_banner's bytes for every built
template and clause with §2.5's literals parsed from the proposal file itself.
`DECLARED_HARNESS_STRINGS` are m:258's eight (the six lines and F3's two
reasoning-block lines, m:174, as data) for roster admissibility.
"""
from __future__ import annotations

from ..session_e2a import SESSION_BANNER
from . import keys

COMMON = "Note: after the first four rounds you will choose which config runs each remaining round."

TOLD_MAP = (
    "Note: config {L_clean} presents clean task text; config {L_corr} presents task text with "
    "character corruption. Prefer clean task text.",
    "Note: config {L_corr} presents task text with character corruption; config {L_clean} "
    "presents clean task text. Prefer clean task text.",
)

# PIN (Code, declared at LOCK v0.1): m:256 quotes only the first TOLD-MAP-SHAM variant; the
# second is its mirror built by m:253's definition (the two label clauses swapped), i.e.
# {L_b}'s clause first.
TOLD_MAP_SHAM = (
    "Note: config {L_a} presents clean task text; config {L_b} presents clean task text. "
    "Prefer clean task text.",
    "Note: config {L_b} presents clean task text; config {L_a} presents clean task text. "
    "Prefer clean task text.",
)

#: TOLD-OBJ (A2, A2s; Q-F3 only). Defined, never used by any Q-F0 or OLMo template.
TOLD_OBJ = ("Note: configs can differ in the cleanliness of their task text. Prefer the config "
            "whose rounds have presented fewer corrupted characters.")

#: The five harness strings Q-F0 and the OLMo units use (m:258).
HARNESS_STRINGS_QF0 = (COMMON, TOLD_MAP[0], TOLD_MAP[1], TOLD_MAP_SHAM[0], TOLD_MAP_SHAM[1])

#: F3's reasoning-block lines (m:174, named at m:258 and m:261), DATA ONLY: no Q-F0 or
#: OLMo session writes them and no F3 code is built here (step 19's, m:363); they exist so
#: m:258's roster admissibility runs on all eight declared strings.
REASONING_HEADER = "[round {n} | reasoning]"
REASONING_LINE = "Reasoning (one line):"

#: m:258's "eight declared harness strings": the six banner lines (COMMON; TOLD-MAP x2;
#: TOLD-MAP-SHAM x2; TOLD-OBJ) and the two reasoning-block lines. Roster admissibility
#: (corr.startup_hygiene) runs on these eight; HARNESS_STRINGS_QF0 stays the five used.
DECLARED_HARNESS_STRINGS = (HARNESS_STRINGS_QF0 + (TOLD_OBJ,)
                            + (REASONING_HEADER, REASONING_LINE))

# PIN (Code, declared at LOCK v0.1): the templates built here are Q-F0's A0/A0s and the OLMo
# A0/A0s per checkpoint in keys.CKPTS; base templates are refused (decision (7'), no told
# control on base) and every other arm (A1-A3s) is step 19's.
_TEMPLATES = tuple(keys.QF0_TEMPLATES) + tuple(
    t for c in keys.CKPTS for t in (f"A0-OLMo-{c}", f"A0s-OLMo-{c}"))


def _check_label(x, role: str) -> str:
    # PIN (Code, declared at LOCK v0.1): a label is a non-empty run of lowercase ASCII letters
    # (every roster word is), so no label can carry a brace, a newline or a second clause.
    if not (isinstance(x, str) and x and x.isascii() and x.isalpha() and x == x.lower()):
        raise ValueError(f"{role} label must be lowercase ASCII letters, got {x!r}")
    return x


def build_banner(template: str, P: str, Q: str, clause: int) -> tuple[str, tuple[str, ...]]:
    """(banner bytes, (COMMON, TOLD)) for one session (m:253-258)."""
    if template not in _TEMPLATES:
        raise ValueError(f"no Q-F0/OLMo banner for template {template!r}; built: {_TEMPLATES}")
    _check_label(P, "P-role")
    _check_label(Q, "Q-role")
    if P == Q:
        raise ValueError(f"P and Q labels coincide: {P!r}")
    # PIN (Code, declared at LOCK v0.1): clause is the int 0 or 1 (a bool is refused).
    if isinstance(clause, bool) or clause not in (0, 1):
        raise ValueError(f"clause must be 0 (first variant) or 1 (its mirror), got {clause!r}")
    if keys.is_contrast(template):
        src = TOLD_MAP[clause]
        told = src.format(L_clean=P, L_corr=Q)
    else:
        src = TOLD_MAP_SHAM[clause]
        told = src.format(L_a=P, L_b=Q)
    assert src in TOLD_MAP + TOLD_MAP_SHAM and src != TOLD_OBJ   # m:258: five of the six
    out = SESSION_BANNER + COMMON + "\n" + told + "\n"
    assert out.isascii() and "\n\n" not in out and "{" not in out
    return out, (COMMON, told)


def _spec_lines(path) -> dict[str, list[str]]:
    """The backticked strings of §2.5's four bullets (m:254-257), plus m:253's
    SESSION_BANNER literal and m:174's two reasoning-block lines."""
    import re

    out: dict[str, list[str]] = {}
    for line in open(path, encoding="utf-8"):
        for name in ("COMMON", "TOLD-MAP-SHAM", "TOLD-MAP", "TOLD-OBJ"):
            if line.startswith(f"- {name} ") or line.startswith(f"- {name}("):
                out.setdefault(name, re.findall(r"`([^`]*)`", line))
                break
        if line.startswith("**2.5 Banner lines, verbatim.**"):
            m = re.search(r'`SESSION_BANNER` being `"([^`"]*)"`', line)
            if m:
                out.setdefault("SESSION_BANNER", [m.group(1).replace("\\n", "\n")])
        if line.startswith("**2.2 Formats.**"):
            m = re.search(r"the line `([^`]*)`, a newline, the line `([^`]*)`", line)
            if m:
                out.setdefault("REASONING", [m.group(1), m.group(2)])
    return out


def _mirror(line: str) -> str | None:
    """m:253's "the mirror": the two label clauses of a TOLD line in the other order."""
    head, tail = "Note: ", ". Prefer clean task text."
    if not (line.startswith(head) and line.endswith(tail)):
        return None
    parts = line[len(head):-len(tail)].split("; ")
    return f"{head}{parts[1]}; {parts[0]}{tail}" if len(parts) == 2 else None


def spec_problems(proposal_path=None) -> list[str]:
    """build_banner's bytes for every built template and clause against §2.5's literals
    parsed from the proposal file (m:253-258; and m:174's reasoning lines against
    DECLARED_HARNESS_STRINGS); [] = clean. A run-time check, not only a selftest one:
    every banner a session writes is compared, through build_banner, with the spec's
    own text (an unreadable or unparsable proposal is a problem, never a pass)."""
    from pathlib import Path

    path = Path(proposal_path) if proposal_path is not None else (
        Path(__file__).resolve().parents[2] / "PROPOSAL-m-gating-campaign-v1_11.md")
    try:
        sl = _spec_lines(path)
    except (OSError, UnicodeDecodeError) as e:
        return [f"banner spec: cannot read {path} ({type(e).__name__})"]
    probs: list[str] = []
    want_n = {"COMMON": 1, "TOLD-MAP": 2, "TOLD-MAP-SHAM": 1, "TOLD-OBJ": 1, "SESSION_BANNER": 1,
              "REASONING": 2}
    for k, n in want_n.items():
        if len(sl.get(k, [])) != n:
            probs.append(f"banner spec: {k} parsed {len(sl.get(k, []))} literal(s), expected {n}")
    if probs:
        return probs
    s_common, s_map, s_sham0 = sl["COMMON"][0], sl["TOLD-MAP"], sl["TOLD-MAP-SHAM"][0]
    s_sham = (s_sham0, _mirror(s_sham0))
    if s_sham[1] is None:
        return ["banner spec: TOLD-MAP-SHAM's first variant has no two label clauses to mirror"]
    for nm, got, want in (("SESSION_BANNER", SESSION_BANNER, sl["SESSION_BANNER"][0]),
                          ("COMMON", COMMON, s_common), ("TOLD_MAP", tuple(TOLD_MAP), tuple(s_map)),
                          ("TOLD_MAP_SHAM", tuple(TOLD_MAP_SHAM), s_sham),
                          ("TOLD_OBJ", TOLD_OBJ, sl["TOLD-OBJ"][0]),
                          ("reasoning lines", DECLARED_HARNESS_STRINGS[6:], tuple(sl["REASONING"])),
                          ("DECLARED_HARNESS_STRINGS", DECLARED_HARNESS_STRINGS,
                           (s_common,) + tuple(s_map) + s_sham + (sl["TOLD-OBJ"][0],)
                           + tuple(sl["REASONING"]))):
        if got != want:
            probs.append(f"banner spec: {nm} differs from the proposal's literal")
    # Every built template x clause, against bytes assembled from the spec's text alone.
    P, Q = "maple", "cedar"
    head = sl["SESSION_BANNER"][0] + s_common + "\n"
    for t in _TEMPLATES:
        for cl in (0, 1):
            told = (s_map[cl].format(L_clean=P, L_corr=Q) if keys.is_contrast(t)
                    else s_sham[cl].format(L_a=P, L_b=Q))
            try:
                got = build_banner(t, P, Q, cl)
            except (ValueError, AssertionError, KeyError, IndexError) as e:
                probs.append(f"banner spec: build_banner({t}, clause {cl}) raised {type(e).__name__}")
                continue
            if got != (head + told + "\n", (s_common, told)):
                probs.append(f"banner spec: build_banner({t}, clause {cl}) bytes differ from §2.5")
    return probs


def _selftest(chk) -> None:
    from pathlib import Path

    from .. import session_e2a

    chk("banner: SESSION_BANNER is session_e2a's (imported)",
        SESSION_BANNER is session_e2a.SESSION_BANNER
        and SESSION_BANNER == "=== Config evaluation session ===\n")

    spec = Path(__file__).resolve().parents[2] / "PROPOSAL-m-gating-campaign-v1_11.md"
    sl = _spec_lines(spec)
    chk("banner: COMMON / TOLD_MAP x2 / TOLD_MAP_SHAM[0] / TOLD_OBJ verbatim from m:254-257",
        sl.get("COMMON") == [COMMON] and sl.get("TOLD-MAP") == list(TOLD_MAP)
        and sl.get("TOLD-MAP-SHAM") == [TOLD_MAP_SHAM[0]] and sl.get("TOLD-OBJ") == [TOLD_OBJ],
        {k: len(v) for k, v in sl.items()})
    a, b = TOLD_MAP_SHAM[0][len("Note: "):].split(". Prefer")[0].split("; ")
    chk("banner: TOLD_MAP_SHAM[1] is the mirror (label clauses swapped, m:253)",
        TOLD_MAP_SHAM[1] == f"Note: {b}; {a}. Prefer clean task text."
        and TOLD_MAP[1].startswith("Note: config {L_corr}"), TOLD_MAP_SHAM[1])

    head = ("=== Config evaluation session ===\n"
            "Note: after the first four rounds you will choose which config runs each remaining round.\n")
    want = {
        ("A0", 0): head + "Note: config maple presents clean task text; config cedar presents task "
                          "text with character corruption. Prefer clean task text.\n",
        ("A0", 1): head + "Note: config cedar presents task text with character corruption; config "
                          "maple presents clean task text. Prefer clean task text.\n",
        ("A0s", 0): head + "Note: config maple presents clean task text; config cedar presents clean "
                           "task text. Prefer clean task text.\n",
        ("A0s", 1): head + "Note: config cedar presents clean task text; config maple presents clean "
                           "task text. Prefer clean task text.\n",
    }
    got = {k: build_banner(k[0], "maple", "cedar", k[1]) for k in want}
    chk("banner: bytes exact for contrast/sham x clause 0/1 (P = maple, Q = cedar)",
        all(got[k][0] == want[k] for k in want), [k for k in want if got[k][0] != want[k]])
    chk("banner: note_lines = (COMMON, TOLD) without newlines; bytes = banner + lines + \\n each",
        all(got[k][1][0] == COMMON and got[k][0] == SESSION_BANNER + "\n".join(got[k][1]) + "\n"
            and "\n" not in "".join(got[k][1]) for k in want))
    olmo_same = all(build_banner(f"{kind}-OLMo-{c}", "quartz", "velvet", cl)
                    == build_banner(kind, "quartz", "velvet", cl)
                    for kind in ("A0", "A0s") for c in keys.CKPTS for cl in (0, 1))
    chk("banner: OLMo templates take the Q-F0 lines of their kind (TOLD-MAP / TOLD-MAP-SHAM)",
        olmo_same)
    chk("banner: P/Q fill L_clean/L_a and L_corr/L_b (swapping P,Q moves the labels)",
        build_banner("A0", "cedar", "maple", 0)[0] != want[("A0", 0)]
        and "config cedar presents clean" in build_banner("A0", "cedar", "maple", 0)[0])
    every = [build_banner(t, "slate", "prism", cl)[0] for t in _TEMPLATES for cl in (0, 1)]
    chk("banner: TOLD_OBJ never used; HARNESS_STRINGS_QF0 is the five of m:258",
        not any(TOLD_OBJ in x or "cleanliness" in x for x in every)
        and HARNESS_STRINGS_QF0 == (COMMON,) + TOLD_MAP + TOLD_MAP_SHAM
        and TOLD_OBJ not in HARNESS_STRINGS_QF0 and len(set(HARNESS_STRINGS_QF0)) == 5)
    refused = []
    for args in (("A0", "maple", "cedar", 2), ("A0", "maple", "cedar", True),
                 ("A1", "maple", "cedar", 0), ("A0-OLMo-base", "maple", "cedar", 0),
                 ("A0s", "maple", "maple", 0), ("A0", "Maple", "cedar", 0),
                 ("A0", "maple", "ce{dar}", 0), ("A0", "", "cedar", 0)):
        try:
            build_banner(*args)
            refused.append(False)
        except ValueError:
            refused.append(True)
    chk("banner: refuses clause 2/bool, A1, base, P == Q, non-lowercase/brace/empty labels",
        all(refused), refused)

    # DECLARED_HARNESS_STRINGS (m:258's eight) and spec_problems (C5), both directions
    import tempfile
    from unittest import mock

    from . import audit as _audit
    chk("banner: DECLARED_HARNESS_STRINGS = the five + TOLD_OBJ + the two reasoning-block lines "
        "(m:258's eight; m:174's literals; audit's reasoning label is the same string)",
        len(DECLARED_HARNESS_STRINGS) == len(set(DECLARED_HARNESS_STRINGS)) == 8
        and DECLARED_HARNESS_STRINGS[:5] == HARNESS_STRINGS_QF0
        and DECLARED_HARNESS_STRINGS[5:] == (TOLD_OBJ, "[round {n} | reasoning]", "Reasoning (one line):")
        and sl.get("REASONING") == list(DECLARED_HARNESS_STRINGS[6:])
        and _audit.REASONING_LABEL == REASONING_LINE)
    got = spec_problems(spec)
    chk("banner: spec_problems is clean -- every template x clause built bytes = §2.5's literals",
        got == [] and spec_problems() == [], got[:2])
    mutated = {
        "TOLD_MAP[1] one word": ("TOLD_MAP", (TOLD_MAP[0], TOLD_MAP[1].replace("presents clean", "shows clean"))),
        "COMMON period dropped": ("COMMON", COMMON[:-1]),
        "TOLD_MAP_SHAM mirror wrong": ("TOLD_MAP_SHAM", (TOLD_MAP_SHAM[0], TOLD_MAP_SHAM[0])),
        "SESSION_BANNER": ("SESSION_BANNER", "=== Config evaluation session ===\n\n"),
        "reasoning line": ("DECLARED_HARNESS_STRINGS", DECLARED_HARNESS_STRINGS[:7] + ("Reasoning:",)),
    }
    silent = []
    for nm, (attr, val) in mutated.items():
        with mock.patch(f"{__name__}.{attr}", val):
            if not spec_problems(spec):
                silent.append(nm)
    real_build = build_banner

    def clause_ignored(t, P, Q, clause):          # every session gets the first variant
        return real_build(t, P, Q, 0)

    def labels_swapped(t, P, Q, clause):          # L_clean / L_corr filled the wrong way round
        return real_build(t, Q, P, clause)

    def no_newline(t, P, Q, clause):              # the TOLD line not newline-terminated
        b, lines = real_build(t, P, Q, clause)
        return b[:-1], lines
    assembly = {"clause ignored": clause_ignored, "labels swapped": labels_swapped,
                "TOLD line unterminated": no_newline}
    for nm, fn in assembly.items():
        with mock.patch(f"{__name__}.build_banner", fn):
            if not spec_problems(spec):
                silent.append(f"build_banner: {nm}")
    raw = spec.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as td:
        alt = Path(td) / "proposal.md"
        alt.write_text(raw.replace("character corruption; config {L_clean}",
                                   "character corruption;  config {L_clean}", 1), encoding="utf-8")
        if not spec_problems(alt):
            silent.append("a mutated proposal literal")
        if not spec_problems(Path(td) / "absent.md"):
            silent.append("an absent proposal")
        alt.write_text(raw.replace("- TOLD-OBJ (A2, A2s)", "- TOLD OBJ (A2, A2s)", 1), encoding="utf-8")
        if not spec_problems(alt):
            silent.append("an unparsable TOLD-OBJ bullet")
    chk(f"banner: spec_problems fires on every mutated banner line, build_banner assembly or proposal "
        f"({len(mutated) + len(assembly) + 3})",
        not silent, silent)
