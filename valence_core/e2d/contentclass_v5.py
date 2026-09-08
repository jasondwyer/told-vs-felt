"""Content class, version 5 -- CANDIDATE (design dispositions 2026-09-08,
item 2, PI stamp). Builds on the frozen v3 draft and the adopted v4 without
modifying either; audit v3 (the audit of record) still routes through v4
until the design seat adopts from the screen. PROSPECTIVE ONLY.

Two rules, BOTH ADVISORY; nothing exclusion-bearing changes:

  (a) `wrong_task`'s comparison pool excludes the current task's OWN
      paraphrases, by task id. The format recon's two v4 `wrong_task`
      advisories (F2 s2 forced1, s18 forced0) answered their own task and
      fired only because the task's sibling paraphrases sat in the pool;
      v4's screen used the same pool construction (every paraphrase but the
      current one). The pool is now "every paraphrase of every OTHER task".

  (b) `payload_echo`, a new advisory class: a TRANSFORM task (rewrite /
      reword / rephrase / restate / soften; or make ... friendlier / kinder /
      warmer / gentler / softer / nicer / politer -- a lexicon WIDER than the
      disposition's "(rewrite/reword/soften)", declared) whose instruction carries a payload after
      the colon, answered with that payload UNCHANGED, quotation marks
      aside. The v3 echo rule compares against the instruction only (the
      v1 -> v2 confound fix), so a payload returned with no rewrite passes
      as content; the format recon's read found three (F1 s22 forced0, F2
      s5 free4, F2 s8 forced2). Exact word-sequence identity (case and
      punctuation ignored -- so '3pm!' for '3pm.' and **bold** count) after
      stripping a leading "<Word>:" label and quotation marks -- wider than
      the disposition's "quotation marks aside", declared; a partial rewrite
      is not an echo. The screen flags each hit's byte-level verbatimness.

Precedence: NULL -> STUCK -> PREAMBLE -> ECHO -> PAYLOAD_ECHO -> WRONG_TASK
(the two advisory classes last; payload_echo before wrong_task so a payload
returned verbatim is named for what it is). Thresholds of v4 untouched.
"""

from __future__ import annotations

import re
from typing import Iterable, Mapping, Sequence

from . import contentclass as V3
from . import contentclass_v4 as V4

SPEC_VERSION = "content-class-v5 CANDIDATE (design dispositions 2026-09-08 item 2): wrong_task pool by task id; payload_echo advisory"

EXCLUSION_BEARING = V4.EXCLUSION_BEARING
ADVISORY = ("task_echo", "payload_echo", "wrong_task")
CLASSES = EXCLUSION_BEARING + ADVISORY

#: The transform-task family, by rule: an instruction (before the colon) with
#: a transform verb, and a non-empty payload after the colon. Declared, not
#: tuned: the corpus's t06 (meeting notice) and t14 (dishes notice) fall in;
#: the caption tasks with a colon (t01, t09) do not.
_TRANSFORM_VERB = re.compile(r"\b(rewrite|reword|rephrase|restate|soften)\b", re.I)
_MAKE_TARGET = re.compile(r"\bmake\b.*\b(friendlier|kinder|warmer|gentler|softer|nicer|politer)\b", re.I)
_QUOTES = "\"'“”‘’«»`"


def payload_of(task_text: str) -> str | None:
    """The text after the first colon, or None if the task has none."""
    t = task_text or ""
    if ":" not in t:
        return None
    payload = t.split(":", 1)[1].strip()
    return payload or None


def is_transform_task(task_text: str) -> bool:
    if payload_of(task_text) is None:
        return False
    instr = V3.instruction_only(task_text)
    return bool(_TRANSFORM_VERB.search(instr) or _MAKE_TARGET.search(instr))


def _strip_quotes(s: str) -> str:
    return (s or "").strip().strip(_QUOTES).strip()


def is_payload_echo(text: str, task_text: str) -> bool:
    """Transform task answered with its payload unchanged (quotation marks
    and a leading label aside). Exact word-sequence identity."""
    if not is_transform_task(task_text):
        return False
    body = _strip_quotes(V4.strip_leading_label(text))
    if not body:
        return False
    return V3._words(body) == V3._words(payload_of(task_text))


def others_by_task_id(task_text: str, pool_by_id: Mapping[str, Sequence[str]],
                      id_of: Mapping[str, str]) -> list[str]:
    """Every paraphrase of every OTHER task. `id_of` maps a paraphrase text
    to its task id; a task text not in the corpus keeps the whole pool
    (reported by the caller, never silently)."""
    tid = id_of.get(task_text)
    return [p for k, ps in pool_by_id.items() if k != tid for p in ps]


def classify_v5(text: str, task_text: str, earlier: Sequence[str] = (),
                other_tasks: Iterable[str] = ()) -> tuple[str | None, str | None]:
    """(label, standing). `other_tasks` MUST already exclude the current
    task's own paraphrases (use `others_by_task_id`); this function does not
    know task ids."""
    if V4.is_null_response_v4(text, task_text):
        return "null_response", "exclusion"
    if V3.is_stuck_attractor(text, earlier):
        return "stuck_attractor", "exclusion"
    if V3.is_preamble(text, task_text):
        return "preamble_without_content", "exclusion"
    if V4.is_task_echo_v4(text, task_text):
        return "task_echo", "advisory"
    if is_payload_echo(text, task_text):
        return "payload_echo", "advisory"
    if V3.is_wrong_task(text, task_text, other_tasks):
        return "wrong_task", "advisory"
    return None, None


__all__ = ["SPEC_VERSION", "CLASSES", "EXCLUSION_BEARING", "ADVISORY", "payload_of",
           "is_transform_task", "is_payload_echo", "others_by_task_id", "classify_v5"]
