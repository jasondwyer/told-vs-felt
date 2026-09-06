"""Content class, version 4 -- the ADOPTED spec (design adjudication of
2026-09-05, PI-ratified; AMENDMENT 2 (iii)). PROSPECTIVE ONLY.

`contentclass.py` (draft v3) scored a committed artifact and stays frozen;
this module builds on its detectors without modifying them. Every archive's
audit of record stands unchanged; the overbreadth figures are a methods
disclosure (review card 11).

Standing of each class, per the adjudication:

  EXCLUSION-BEARING
    stuck_attractor          repeats an earlier response          (1b, as v3)
    preamble_without_content announces and never delivers          (1b, as v3)
    null_response            NO CONTENT ADDRESSING THE TASK        (1c, widened)
  ADVISORY -- routed to the rule-25 read, never excludes
    task_echo                reproduces the instruction, GUARDED   (2a, pending
                             a fresh 14 + 14 eyeballing of v4's hits)
    wrong_task               performs/restates a different task    (2b, indefinitely)

1c. `null_response` is widened AT THE CLASS LEVEL from "content-free" to "no
content addressing the task": a content-free string ("* * *", "<answer>", a
bare fence, "None", "[MENTAL_BLOCK]") and a refusal ("Sorry, I can't help
with that") are ONE failure, not five strings and a sixth class. The rule:
v3's content-free test, OR a refusal-shaped clause -- a first-person
DECLINING PREDICATE ("I can't / cannot / won't / am unable to ... help / do /
write / that"); an apology alone is not a refusal -- removed together with
any first-person self-description clause ("I am a large language model"),
after whose removal fewer than `NULL_RESIDUAL_WORDS` content words remain.
Only the predicate is removed, never its clause or sentence, so a refusal
followed or accompanied by delivered content is not null. KNOWN MISSES,
declared: third-person capability disclaimers ("Sorry, creative tasks require
a LLM with more creative capabilities") and a bare "No." carry no declining
predicate and are not caught; they go to the read. The rationale sentence "all observed instances are in UNSTEERED
rounds" is WITHDRAWN (4 of 13 e2d hits are steered rounds of D3 session 12).

2a. `task_echo` gains a class-level GUARD: it fires only when the response's
content beyond the shared instruction run falls below a declared novelty
floor -- `NOVELTY_FLOOR` distinct content words of the response that do not
occur in the task -- and a leading "<Word>:" label is never itself echo (it is
stripped before the test). The guard is a rule, not a string list.

1d. Thresholds are FROZEN as declared: run = 5 and the verb lexicon (v3,
unchanged), NOVELTY_FLOOR = 4 and NULL_RESIDUAL_WORDS = 3 (declared here,
before the v4 blind re-screen). Any change is a new version with a blind
re-screen.

1e. Precedence NULL -> STUCK -> PREAMBLE -> ECHO -> WRONG_TASK, kept; labels may
swap in places (a refusal may land in preamble/stuck), exclusion is on the
union, so that is a reporting note, not a defect.
"""

from __future__ import annotations

import re
from typing import Iterable, Sequence

from . import contentclass as V3

SPEC_VERSION = "content-class-v4 rev 3 (adopted 2026-09-05; echo guard advisory pending re-eyeball; declining-predicate refusal shape, predicate-only removal)"

EXCLUSION_BEARING = ("null_response", "stuck_attractor", "preamble_without_content")
ADVISORY = ("task_echo", "wrong_task")
CLASSES = EXCLUSION_BEARING + ADVISORY

#: Declared before the v4 blind re-screen. FROZEN (1d).
NOVELTY_FLOOR = 4          # distinct content words beyond the task; fewer -> echo may fire
NULL_RESIDUAL_WORDS = 3    # content words left after a refusal clause; fewer -> null

#: A leading single-word label ("Caption:", "Slogan:", "Response:") -- never
#: itself echo; stripped before any test.
_LEADING_LABEL = re.compile(r"^\s*[\"'“‘]?\s*[A-Za-z][A-Za-z\-]{0,24}\s*:\s*")

#: The refusal SHAPE: a DECLINING PREDICATE -- first person ("I can't /
#: cannot / won't / am unable to / must decline / refuse"), or the passive
#: "(this request / that) cannot be fulfilled". An apology alone ("I'm sorry
#: for the inconvenience") is not a refusal, and "as an AI" alone is not one
#: either. A shape, not a list of the sentences that happened to appear.
#: rev 2: required the predicate (the first form matched a bare "I'm sorry"
#: and flagged a delivered rewrite). rev 3: only the PREDICATE is removed
#: before counting the residual, never its clause -- rev 2's clause removal
#: swallowed content delivered in the same clause ("I can't offer a better
#: name than 'Roast & Roll'") -- the complement is optional so a bare
#: "Sorry, I can't." counts, and decline/refuse and the passive form are
#: declining shapes too. Both found by the pre-commit values-check,
#: corrected and re-screened blind before anything was committed.
_REFUSAL = re.compile(
    r"\b(?:i\s*(?:'m|am|'ve been|have been)?\s*(?:really\s+|truly\s+|so\s+)?"
    r"(?:can(?:no|')t|cannot|can not|won(?:'|no)t|will not|shall not|do not|don't|"
    r"must decline|decline to|refuse to|refuse|"
    r"(?:am|'m)\s+(?:unable|not able|not permitted|not allowed|not going|afraid i can(?:no|')t))"
    r"(?:\s+to)?(?:\s+(?:help|assist|do|provide|comply|write|generate|answer|fulfil|fulfill|"
    r"complete|produce|create|offer|give|make))?"
    r"|(?:this|that|the|your)\s+(?:request|task)?\s*(?:can(?:no|')t|cannot|can not)\s+be\s+"
    r"(?:fulfilled|completed|done|answered|met|honou?red))\b", re.I)
#: A first-person self-description clause ("I am a large language model") --
#: meta, not task content; removed with the predicate before counting.
_META = re.compile(
    r"\bi\s*(?:'m|am)\s+(?:a|an)\s+(?:large\s+)?(?:language model|ai(?: model)?|"
    r"assistant|model|chatbot|bot)\b", re.I)
#: Function words, for the novelty count and the residual count. A rule-level
#: list of the closed class, not of observed phrasings.
_STOP = set("""a an the and or but if then than so of to in on at by for with from as into onto
over under about above below between through during before after this that these those it its
is are was were be been being am do does did have has had having not no nor yes you your yours
we our ours they them their theirs he she him her his hers i me my mine one ones very just also
too more most much many any some such only own same other another each every all both few
here there where when why how what which who whom whose will would can could may might shall
should must up down out off again further once s t ll re ve d m""".split())


def strip_leading_label(text: str) -> str:
    t = (text or "").strip()
    m = _LEADING_LABEL.match(t)
    return t[m.end():].strip() if m else t


def _content_words(s: str) -> list[str]:
    return [w for w in V3._words(s) if w not in _STOP and len(w) > 2]


def _strip_matches(body: str, patterns) -> str:
    """Remove each matched PREDICATE (only the matched span) and return what
    is left -- never the clause, never the sentence: "I can't help with that,
    but here is a poem ..." keeps its poem, and "I can't offer a better name
    than 'Roast & Roll'" keeps its name."""
    out = body
    for pat in patterns:
        out = pat.sub(" ", out)
    return out


def is_null_response_v4(text: str, task_text: str = "") -> bool:
    """No content addressing the task: content-free (v3) OR a declining
    predicate (self-description clauses removed with it) after whose removal
    fewer than NULL_RESIDUAL_WORDS content words remain."""
    t = (text or "").strip()
    if V3.is_null_response(t):
        return True
    body = strip_leading_label(t)
    if V3.is_null_response(body):
        return True
    if not _REFUSAL.search(body):
        return False
    rest = _strip_matches(body, (_REFUSAL, _META))
    return len(_content_words(rest)) < NULL_RESIDUAL_WORDS


def novelty(text: str, task_text: str) -> int:
    """Distinct content words of the response (leading label stripped) that
    do not occur anywhere in the task text."""
    task_words = set(V3._words(task_text or ""))
    return len({w for w in _content_words(strip_leading_label(text)) if w not in task_words})


def is_task_echo_v4(text: str, task_text: str, run: int = 5) -> bool:
    """v3's echo test on the label-stripped response, guarded: fires only if
    the response carries fewer than NOVELTY_FLOOR content words beyond the
    task. ADVISORY (2a) until the design seat re-eyeballs v4's hits."""
    body = strip_leading_label(text)
    if not V3.is_task_echo(body, task_text, run=run):
        return False
    return novelty(body, task_text) < NOVELTY_FLOOR


def classify_v4(text: str, task_text: str, earlier: Sequence[str] = (),
                other_tasks: Iterable[str] = ()) -> tuple[str | None, str | None]:
    """(label, standing) with standing 'exclusion' | 'advisory' | None.
    Precedence as v3 (1e); null uses the widened rule; echo uses the guard."""
    if is_null_response_v4(text, task_text):
        return "null_response", "exclusion"
    if V3.is_stuck_attractor(text, earlier):
        return "stuck_attractor", "exclusion"
    if V3.is_preamble(text, task_text):
        return "preamble_without_content", "exclusion"
    if is_task_echo_v4(text, task_text):
        return "task_echo", "advisory"
    if V3.is_wrong_task(text, task_text, other_tasks):
        return "wrong_task", "advisory"
    return None, None


__all__ = ["SPEC_VERSION", "CLASSES", "EXCLUSION_BEARING", "ADVISORY",
           "NOVELTY_FLOOR", "NULL_RESIDUAL_WORDS", "strip_leading_label",
           "is_null_response_v4", "novelty", "is_task_echo_v4", "classify_v4"]
