"""Content-shaped degeneracy — a CLASS-level spec draft. NOT ADOPTED.

PROPOSAL-j v1.2 AMENDMENT 2 (iii) and disposition-2 item 5. This is the draft
Code owes before LOCK-j: a candidate specification for scorer_v3's content
class, to be screened for overbreadth and then adjudicated. **Nothing here is
the audit of record, and nothing here may exclude a session.** The rule-25
read remains the arbiter wherever the two disagree.

## Why this is written over CLASSES and not over the strings that were seen

`data/configs/scorer_v3_spec.json` carries the standing instruction, and it is
the whole design constraint here: negation-safety was specified over
*observed constructions* twice, and **v1 and v2 each fixed the instance and
missed the class**. Audit v2 repeated the pattern in another register — its
four patterns are all SCAFFOLD-shaped (banner terminators, bracketless
headers, config-role phrases), so it caught 25 rounds across three e2d tiers
while the read marked 81, with **zero overlap**.

So each class below is defined by what the response FAILS TO DO, and the
detector is a consequence of that definition rather than a list of the
phrasings that happened to appear:

  TASK_ECHO      reproduces the instruction instead of performing it
  PREAMBLE       announces an answer and terminates before delivering one
  WRONG_TASK     performs a different task than the one posed
  STUCK_ATTRACTOR repeats an earlier response rather than answering
  NULL_RESPONSE  carries no propositional content at all   [CANDIDATE, new]

NULL_RESPONSE is the fifth class disposition-2 banked. It has three observed
forms -- `[MENTAL_BLOCK]`, the literal word `None`, and a bare ``` fence --
and it is defined as *content-free response*, not as those three strings,
precisely so a fourth form is caught rather than becoming a sixth class.

## What a detector cannot settle

Two of these classes are semantic. WRONG_TASK needs to know which task was
posed and what a right answer looks like; the e2a corpus makes the first half
tractable (16 known tasks, so a response matching a DIFFERENT task's
instruction is detectable) and leaves the second half open. The detector below
is deliberately conservative there. Where it and the read disagree, the
disagreement is the output.
"""

from __future__ import annotations

import re
from typing import Iterable, Mapping, Sequence

SPEC_VERSION = "content-class-draft-v3"

CLASSES = ("task_echo", "preamble_without_content", "wrong_task",
           "stuck_attractor", "null_response")

#: The e2a task pool's instruction verbs. Not a phrase list -- the class is
#: "the response reproduces the INSTRUCTION", and in this corpus instructions
#: are imperative openers. A response that performs the instruction does not
#: name it; one that reproduces it does.
_IMPERATIVE = re.compile(
    r"^\s*[\"'“‘]?\s*(?:prompt\s*:\s*)?"
    r"(write|describe|compose|give|suggest|offer|propose|caption|draft|"
    r"rewrite|reword|soften|make this|in one|in a single|one sentence|"
    r"what would you|what subject|what slogan)\b", re.I)

#: Announcement without delivery. The class is "meta-statement about the
#: answer in place of the answer", so the test is an announcement opener AND
#: no delivered content after it.
_ANNOUNCE = re.compile(
    r"^\s*[\"'“‘]?\s*(here (is|are)|sure|great|certainly|okay|ok|"
    r"of course|good[!,]|i'?ll\b|i will\b|let me\b)", re.I)

#: A FIRST-PERSON COMMITMENT to perform the task. Split out from the general
#: announcement because the class rule is sharper and does not depend on what
#: follows: **a commitment to answer is not an answer**, however much text
#: comes after it. "Great, I'll write one sentence to welcome readers ..."
#: never welcomes anyone.
_COMMITMENT = re.compile(
    r"^\s*[\"'“‘]?\s*(?:great|sure|okay|ok|certainly|of course)?[,!]?\s*"
    r"(i'?ll|i will|let me|i'?m going to|i can)\b", re.I)

#: A response that is structurally empty once markup is removed.
_MARKUP_ONLY = re.compile(r"^[\s`~*_\-\[\]\(\)<>\"'“”]*$")
_BRACKET_TOKEN = re.compile(
    r"^\s*[\[\(<`]{1,3}\s*[A-Za-z_][A-Za-z_ ]{0,24}\s*[\]\)>`]{1,3}\s*$")
_NULL_WORDS = {"none", "n/a", "na", "null", "nil", "todo", "tbd", "-", "—"}


def _words(s: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", s.lower())


#: A rewrite-family task embeds the PAYLOAD the answer must operate on:
#: "Make this sound friendlier: The meeting has been moved to 3pm." A correct
#: answer necessarily reproduces most of that payload, so comparing the
#: response against the whole task text catches good answers. The class is
#: "reproduces the INSTRUCTION", and the instruction is the part before the
#: colon. Screening the first draft against 912 rounds, this single confusion
#: produced most of its false positives.
def instruction_only(task_text: str) -> str:
    t = (task_text or "")
    return t.split(":", 1)[0] if ":" in t else t


def _longest_common_run(a: Sequence[str], b: Sequence[str]) -> int:
    """Longest run of consecutive words shared by a and b."""
    if not a or not b:
        return 0
    best = 0
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best


def is_null_response(text: str) -> bool:
    """No propositional content at all, however it is dressed."""
    t = (text or "").strip()
    if not t:
        return True
    if _MARKUP_ONLY.match(t):
        return True
    if t.strip("`* _\"'").strip().lower() in _NULL_WORDS:
        return True
    if _BRACKET_TOKEN.match(t) and len(_words(t)) <= 3:
        return True
    return False


def is_task_echo(text: str, task_text: str, run: int = 5) -> bool:
    """Reproduces the instruction rather than performing it.

    Two independent routes, because the class has two surface forms: the
    response opens with the task's own imperative frame, or it shares a long
    verbatim run with the task. The run threshold is on CONSECUTIVE words, not
    on bag overlap -- a legitimate answer to "Rewrite this more gently: Do not
    leave dishes in the sink" reuses 'dishes' and 'sink' and must not be
    caught for it.
    """
    t, q = (text or "").strip(), (task_text or "").strip()
    if not t or not q:
        return False
    if is_null_response(t):
        return False
    if _IMPERATIVE.match(t) and _IMPERATIVE.match(q):
        return True
    # THE RUN MUST CONTAIN AN INSTRUCTION VERB.
    #
    # Screening v2 against 3,601 archived rounds showed the run test alone is
    # confounded at the root: a task NAMES ITS OBJECT ("Give a one-sentence
    # description of footsteps on a gravel path"), and a correct answer that
    # describes that object necessarily reuses the noun phrase -- "Footsteps
    # on a gravel path crunch and scatter like brittle leaves" shares five
    # consecutive words with its own task and is a good answer. Most of v2's
    # 209 archive hits were exactly this.
    #
    # The class is "reproduces the INSTRUCTION", and only the instruction verb
    # separates the two: a good answer never says "give a one-sentence
    # description of"; an echo does. So a shared run counts only if it
    # carries one.
    tw, qw = _words(t), _words(instruction_only(q))
    n = _longest_common_run(tw, qw)
    if n < run:
        return False
    return _shared_run_has_instruction_verb(tw, qw, run)


_VERBS = {"write", "describe", "compose", "give", "suggest", "offer",
          "propose", "caption", "draft", "rewrite", "reword", "soften",
          "make", "title", "name", "invite", "thank", "ask", "request"}


def _shared_run_has_instruction_verb(tw, qw, run) -> bool:
    """Does any shared run of >= `run` words contain an instruction verb?"""
    qset = set()
    for i in range(len(qw)):
        for j in range(i + run, len(qw) + 1):
            qset.add(tuple(qw[i:j]))
    for i in range(len(tw)):
        for j in range(i + run, len(tw) + 1):
            seg = tuple(tw[i:j])
            if seg in qset and any(w in _VERBS for w in seg):
                return True
    return False


def is_preamble(text: str, task_text: str = "") -> bool:
    """Announces an answer and stops before giving one.

    An announcement that IS followed by content is not this class -- which is
    why a trailing colon, or an announcement with nothing after its first
    clause, is required rather than the opener alone.
    """
    t = (text or "").strip()
    if not t or is_null_response(t):
        return False
    # a commitment to perform is never a performance, whatever follows it
    if _COMMITMENT.match(t):
        return True
    if not _ANNOUNCE.match(t):
        return False
    # an announcement that never reaches terminal punctuation was cut off
    # before delivering anything
    if not re.search(r"[.!?][\"'”’]?\s*$", t):
        return True
    body = re.sub(r"^\s*[^:.!?]*[:]", "", t).strip()   # drop the announcement
    if not body:
        return True
    # an announcement followed only by a restatement is still undelivered
    return bool(task_text) and is_task_echo(body, task_text)


def is_wrong_task(text: str, task_text: str, other_tasks: Iterable[str],
                  run: int = 5) -> bool:
    """Performs, or restates, a DIFFERENT task than the one posed.

    Conservative by construction: it fires only when the response matches
    another known task's wording more strongly than this one's. Semantic
    wrong-task answers that share no wording are not detectable here and are
    left to the read, which is stated rather than hidden.
    """
    t = (text or "").strip()
    if not t or is_null_response(t):
        return False
    tw = _words(t)
    mine = _longest_common_run(tw, _words(task_text))
    best_other = max((_longest_common_run(tw, _words(o))
                      for o in other_tasks), default=0)
    return best_other >= run and best_other > mine


def is_stuck_attractor(text: str, earlier: Sequence[str]) -> bool:
    """Repeats an earlier response in the same session."""
    t = (text or "").strip()
    if not t or is_null_response(t):
        return False
    norm = " ".join(_words(t))
    if not norm:
        return False
    return any(" ".join(_words(e)) == norm for e in earlier if e)


def classify(text: str, task_text: str, earlier: Sequence[str] = (),
             other_tasks: Iterable[str] = ()) -> str | None:
    """One label or None. Precedence is part of the spec.

    NULL first (it is the most specific and the others exclude it), then
    STUCK (a repeat is a repeat whatever it repeats), then PREAMBLE, then
    ECHO, then WRONG_TASK -- most-specific to least, so a round is described
    by the tightest class that fits rather than the first that happens to
    match.
    """
    if is_null_response(text):
        return "null_response"
    if is_stuck_attractor(text, earlier):
        return "stuck_attractor"
    if is_preamble(text, task_text):
        return "preamble_without_content"
    if is_task_echo(text, task_text):
        return "task_echo"
    if is_wrong_task(text, task_text, other_tasks):
        return "wrong_task"
    return None


__all__ = ["SPEC_VERSION", "CLASSES", "classify", "instruction_only",
           "is_null_response",
           "is_task_echo", "is_preamble", "is_wrong_task",
           "is_stuck_attractor"]
