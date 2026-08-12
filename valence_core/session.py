"""The v3 session harness -- monitoring, audit, and bar machinery, ported
from `scripts/f_sessions.py` (the run that produced 344/344 sessions with
zero checkpoint pauses).

Round generation and stop discipline live on the adapter; what lives here is
everything that decides whether a session *counts*, and the tripwire theory
that decides whether a run continues.

Rule 21, in its finished form, is the organizing idea:

  * **Hair-trigger bars only for defect classes whose healthy base rate is
    ~zero.** A ratio threshold on a class that legitimately occurs 3-5% of
    the time is not a monitor, it is a coin flip that pauses your run.
  * **Measured-base-rate classes bind by exact binomial against a declared
    p0, at every scale.** The lexical bar is the worked example: it fired on
    a true header-to-prose priming specimen at 1/12 under a ratio form, and
    the binomial form correctly does not.
  * **Stimulus-provoked degeneracy gates on unprovoked domains.** A bar
    whose stimulus deliberately provokes junk must be evaluated where the
    provocation is absent, or it measures the stimulus.
  * **Verdict criteria are untouchable by any of this.** A monitor pauses a
    run; it never edits a criterion. Nothing in this module returns a
    verdict.

Attribution precedence is load-bearing and easy to get backwards: the audit
evaluates FIRST, so property-provoked junk is routed to the tolerant audit
counter rather than spuriously tripping the strict lexical one.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from typing import Iterable, Mapping, Sequence

from .stats import binom_test_exact, fisher_one_sided


# --- structural guarantees ------------------------------------------------
def assert_modules_absent(forbidden: Sequence[str],
                          modules: Mapping[str, object] | None = None) -> None:
    """Startup assertion that no steering/conditioning machinery is even
    imported.

    The f screen's central claim was that the channel was open and *nothing*
    was injected. "We didn't call it" is a promise; "it isn't loaded" is a
    fact, and this is how that fact was made checkable. Any drug-free arm
    should call this before generating a token.
    """
    loaded = sys.modules if modules is None else modules
    hits = [m for m in forbidden if m in loaded]
    if hits:
        raise SystemExit(
            f"STRUCTURAL VIOLATION: drug-free run has steering machinery "
            f"imported: {hits}")


# --- text handling --------------------------------------------------------
def normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9/ ]", " ", s.lower()).strip()


def grade(response: str, gold_list: Sequence[str]) -> bool:
    """Word-boundary-safe containment grading. Boundaries are checked against
    alphanumerics rather than \\b so that gold answers containing '/' or
    digits grade correctly."""
    r = " " + normalize(response) + " "
    for g in gold_list:
        if re.search(rf"(?<![a-z0-9]){re.escape(normalize(g))}(?![a-z0-9])", r):
            return True
    return False


def lexical_hit(text: str, tags: Sequence[str]) -> str | None:
    """Word-boundary roster-tag appearance in generated text. Rule 18's
    runtime half: the roster is asserted disjoint from every pool at startup,
    and this catches the model *producing* a tag it should have no reason to
    produce."""
    low = text.lower()
    for t in tags:
        if re.search(rf"\b{re.escape(t)}\b", low):
            return t
    return None


DEFAULT_SCAFFOLD_STRINGS = ("<think>", "</think>", "<|im_start|>", "<|im_end|>")


def build_ban_list(adapter, extra_strings: Iterable[str] = (),
                   path: str | None = None) -> tuple[list[int], list[str]]:
    """Frozen chat-scaffold ban list: the token ids that are suppressed at
    ROUND GENERATION ONLY, and never at a choice forward.

    Rule 13's enforcement arm. Completion-style prompting keeps the `<think>`
    scaffold out of the framing; this keeps it out of the *sampling*, which
    matters because a scaffold token mid-response turns a round into junk and
    the junk is not randomly distributed.

    Applying a ban at a choice forward would edit the DV, so callers pass
    `ban_ids` to `generate` and never to `choice_read` -- the two functions
    have deliberately different signatures to make that hard to get wrong.

    Freezing to `path` (when given) makes the list an artifact with a sha,
    so a later run can prove it banned the same set.
    """
    import json
    import os

    if path and os.path.exists(path):
        cfg = json.load(open(path))
        return list(cfg["ids"]), list(cfg["strings"])

    strings = set(DEFAULT_SCAFFOLD_STRINGS) | set(extra_strings)
    strings |= set(adapter.special_token_strings)
    ids: set[int] = set()
    for s in sorted(strings):
        for tok in adapter.encode(s, add_special_tokens=False):
            ids.add(int(tok))
    out_ids, out_strings = sorted(ids), sorted(strings)
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump({"strings": out_strings, "ids": out_ids}, f, indent=1)
    return out_ids, out_strings


@dataclass(frozen=True)
class AuditSpec:
    """The frozen degeneracy audit. Frozen means frozen: fragments and
    regexes are fixed before the run and no post-data additions are made,
    because an audit widened after seeing the data is a filter, not a
    monitor."""

    ban_strings: tuple[str, ...] = ()
    frame_fragments: tuple[str, ...] = ()
    junk_regex: tuple[str, ...] = ()

    def check(self, text: str) -> str | None:
        """Returns a reason string or None. Precedence is part of the spec:
        empty -> special token -> frame fragment -> junk regex."""
        if not text.strip():
            return "empty"
        for s in self.ban_strings:
            if s in text:
                return f"special:{s}"
        for frag in self.frame_fragments:
            if frag in text:
                return f"frame:{frag}"
        for rx in self.junk_regex:
            if re.search(rx, text):
                return f"junk:{rx}"
        return None


def classify_response(text: str, audit: AuditSpec,
                      tags: Sequence[str]) -> tuple[str | None, str | None]:
    """Returns (audit_reason, lexical_tag) with the amended precedence:
    **audit first**. A response that is audit-degenerate is not also counted
    as a lexical hit -- otherwise property-provoked junk trips the strict
    counter and the run pauses on its own stimulus.
    """
    reason = audit.check(text)
    if reason is not None:
        return reason, None
    return None, lexical_hit(text, tags)


# --- tripwires (rule 21) --------------------------------------------------
@dataclass(frozen=True)
class Tripwire:
    """One declared bar. `kind` forces the rule-21 distinction to be made
    explicitly at declaration time rather than implicitly in an if-statement.

    `domain` records which sessions the bar is evaluated over (e.g.
    "sham+P" for an unprovoked domain) -- descriptive, but it is the field
    that makes a stimulus-provoked misfire visible in review.
    """

    name: str
    kind: str                       # "binomial" | "hair_trigger"
    domain: str = "all"
    p0: float | None = None         # binomial: declared healthy base rate
    alpha: float = 0.05
    threshold: float | None = None  # hair_trigger: max tolerated ratio
    min_n: int = 1
    justification: str = ""

    def __post_init__(self) -> None:
        if self.kind == "binomial" and self.p0 is None:
            raise ValueError(f"{self.name}: binomial bar needs a declared p0")
        if self.kind == "hair_trigger":
            if self.threshold is None:
                raise ValueError(f"{self.name}: hair-trigger bar needs a threshold")
            if not self.justification:
                raise ValueError(
                    f"{self.name}: hair-trigger bars are licensed only for "
                    f"~zero-base-rate defect classes (rule 21) -- state the "
                    f"justification at declaration")
        if self.kind not in ("binomial", "hair_trigger"):
            raise ValueError(f"{self.name}: unknown bar kind {self.kind!r}")

    def check(self, k: int, n: int) -> str | None:
        """Pause message, or None. Binomial bars bind at every scale; ratio
        bars wait for min_n."""
        if n < self.min_n or n <= 0:
            return None
        if self.kind == "binomial":
            p = binom_test_exact(k, n, self.p0, alternative="greater")
            if p < self.alpha:
                return (f"BAR {self.name} {k}/{n} binom p={p:.4f} < "
                        f"{self.alpha} vs p0={self.p0}")
            return None
        if k / n > self.threshold:
            return (f"BAR {self.name} {k}/{n} > {self.threshold:.0%} "
                    f"({self.domain})")
        return None


def check_bars(bars: Sequence[Tripwire],
               counts: Mapping[str, tuple[int, int]]) -> list[str]:
    """Evaluate declared bars against {bar_name: (k, n)}. Returns every pause
    message, not the first -- a run that trips two bars should say so."""
    out = []
    for bar in bars:
        if bar.name in counts:
            k, n = counts[bar.name]
            msg = bar.check(k, n)
            if msg:
                out.append(msg)
    return out


def verify_firing(bars: Sequence[Tripwire],
                  cases: Sequence[tuple[str, int, int, bool]]) -> list[str]:
    """Pre-committed no-model check that declared bars fire where they should
    and stay silent where they should not.

    `cases` are (bar_name, k, n, should_fire). Returns failures. Run this
    before a run, not after: a bar whose firing behavior was never checked
    is not a pre-registration, and the f2 smoke adjudication exists because
    a bar's *form* was wrong, not its threshold.
    """
    by_name = {b.name: b for b in bars}
    failures = []
    for name, k, n, should in cases:
        if name not in by_name:
            failures.append(f"{name}: no such bar declared")
            continue
        fired = by_name[name].check(k, n) is not None
        if fired != should:
            failures.append(
                f"{name}: {k}/{n} {'fired' if fired else 'did not fire'}, "
                f"expected {'fire' if should else 'no fire'}")
    return failures


def fisher_two_groups(a: int, n1: int, c: int, n2: int) -> float:
    """One-sided Fisher in the harness's (successes, total) form -- the shape
    a sham-relative guard is naturally expressed in."""
    return fisher_one_sided(a, n1 - a, c, n2 - c)


# --- descriptive counters (rule 23) ---------------------------------------
@dataclass
class DescriptiveCounters:
    """Anecdote governance: an observation becomes a pre-declared counter
    *before* the run, tabulates over ALL sessions including excluded ones,
    and appears in the verdict entry.

    The termination-attempt table is the template -- one striking smoke
    observation, counted at scale, turned out to run at ~1% across every arm
    including sham, and so was not a signature of anything.
    """

    declared: tuple[str, ...] = ()
    counts: Counter = field(default_factory=Counter)
    n_sessions: int = 0
    n_excluded_included: int = 0

    def __post_init__(self) -> None:
        self.declared = tuple(self.declared)

    def note(self, name: str, *key: object, excluded: bool = False) -> None:
        if name not in self.declared:
            raise KeyError(
                f"counter {name!r} was not pre-declared (rule 23); declared: "
                f"{list(self.declared)}")
        self.counts[(name, *key)] += 1
        if excluded:
            self.n_excluded_included += 1

    def table(self, name: str) -> dict[tuple, int]:
        return {k[1:]: v for k, v in self.counts.items() if k[0] == name}

    def total(self, name: str) -> int:
        return sum(v for k, v in self.counts.items() if k[0] == name)

    def report(self) -> dict:
        return {"n_sessions": self.n_sessions,
                "tabulated_over_excluded_too": True,
                "counters": {name: {"total": self.total(name),
                                    "by_key": {"|".join(map(str, k)): v
                                               for k, v in self.table(name).items()}}
                             for name in self.declared}}


__all__ = ["assert_modules_absent", "normalize", "grade", "lexical_hit",
           "DEFAULT_SCAFFOLD_STRINGS", "build_ban_list",
           "AuditSpec", "classify_response", "Tripwire", "check_bars",
           "verify_firing", "fisher_two_groups", "DescriptiveCounters"]
