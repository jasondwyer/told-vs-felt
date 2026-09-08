"""FORMAT RECON -- sham-only session generation in three candidate
forced-phase formats, under audit v3 (design block 2026-09-06 §4; PI go
"Go format recon"). PROPOSAL-k candidate; template recalibration.

PURPOSE. Measure the first-free-choice habit and its break rate in three
formats, so LOCK-k can size a break-rate DV against a REALISED floor rather
than e2a's .17 or e2d's .03. Descriptive only; no bar; nothing here licenses
a verdict.

  F0  e2a format of record: strict alternation, two rounds per label
      (A B A B) -- the continuity anchor; expect ~.83 strict alternation.
  F1  neutral-start (the drawer's variant): the forced phase runs under a
      NEUTRAL third label for its first two rounds, then one round per menu
      label, then the free choice (N N A B) -- the alternation habit is not
      installed between the two menu labels.
  F2  block order (A A B B / B B A A, start counterbalanced): decorrelates
      round position from label parity (the Stage B/C confound).

SHAM ONLY, structurally. No steering, no axis, no random direction: this
module never imports `Injection`, `load_axis` or anything under
`valence_core.e2b`; `adapter.generate` is called with `injections=()` and
`cached=False` (the uncached path of record) at every round; the quarantined
primitive is asserted absent from `sys.modules` at startup and before every
read (rule 5(a), e2d's discipline, kept); every choice read is
`readout.choice_read(verify=True)` + `assert_construction_stable`, which take
no injections by construction. The self-test greps this module's source for
the forbidden names.

FORMAT = SCAFFOLDING, NOT A NEW TEMPLATE FAMILY. Every harness-written byte is
e2a's (`session_e2a.ROUND_TEMPLATES` / `MENU_TEMPLATES`, indexed on the
session as the archive is), and the rng draw order is e2a's exactly -- task
permutation, paraphrase draws, then per-round generation seeds interleaved
with menu-order draws -- so `session_e2a.verify_archived_session` walks every
session here byte-for-byte, whichever labels the forced rounds carry. That is
the acceptance check, per session, before any artifact is written (trap 6).

CELLS AND COUNTERBALANCING. 8 cells per format = 4 roster pairs x 2 "which
label is first" assignments; the allocation (design patch 2026-09-06 §2) is
F0 8 = 1 whole block, F1 24 and F2 24 = 3 whole blocks, so every prefix of
8 is balanced and each format is exactly balanced at its n. There is
no + pole: `tag_plus` is the NOMINAL first label (the label the alternation
habit predicts for the first pick), `tag_minus` the second/last. In every
format the last forced label is `tag_minus`, so "first-pick break" has one
definition across formats: the first free pick IS the last forced label
(habit.follows_habit == False). Session-share is the share of free picks on
`tag_plus`, e2a's `share_all_choices` with the nominal pole.

THE NEUTRAL LABEL (F1): `timber` (id 43299), re-selected 2026-09-06 under
the design patch's assertion -- absent from EVERY roster and from H3's
sixteen tags -- which the first choice `cedar` failed (see `NEUTRAL_LABEL`).
One fixed label for every F1 session; it never appears on a menu; it is added
to the lexical-hit set of F1 sessions so a response that produces it is
caught. F1's two `cedar` timing sessions were set aside (their checkpoint
renamed, ignored; the sessions stay in the timing artifact as the cost
measurement they were) and F1 starts from index 0 under `timber`.

AUDIT V3 is the audit of record (AMENDMENT 2 (iii) §3): v2 first (rule 28b),
then the exclusion-bearing content classes, then advisory flags routed to the
record. Lexical hits are checked only on rounds audit v3 did not claim (the
tolerant counter attributes first). Exclusion SCOPE runs lenient ("e2a":
audit/content exclusions on forced rounds only, lexical on any round), which
is information-preserving; the strict ("e2b") count is recovered from the
same records and reported beside, as e2d did.

BARS. e2d's three declared acceptance bars are carried verbatim
(`e2d.config.declared_bars`): two hair triggers on ~zero-base-rate classes
and the exact-binomial round-degeneracy bar on the v2 audit class at its
declared p0. No new bar is declared for the content classes -- this recon
declares no bar of its own; their rates are reported beside the archive
base rates. A fired acceptance bar stops the run; Code does not
self-adjudicate it.

THE TIMING GATE is structural (trap 32). `--stage time` runs schedule
indices until ONE COMPLETE session per format is on disk and writes the
timing artifact; `--stage run` refuses to start unless that artifact exists,
every timed session passed acceptance, and the projection under the current
allocation is at or under `GATE_HOURS` (8.0, design patch 2026-09-06 §2,
raised from the block's 4.0 after the timing came in at 8.96 h for 24 x 3).
Overriding the gate takes an explicit `--gate-hours`, written into the run
header and the artifact as a declared deviation.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from typing import Callable, Iterable, Mapping, Sequence

import numpy as np

from ..e2d import habit as H
from ..e2d.audit_v3 import AUDIT_VERSION, AuditV3
from ..e2d.config import (DATA, FIRING_CASES, REPO, ROSTER, TEMP,
                          declared_bars, load_audit)
from ..e2d.runner import FORBIDDEN_MODULES, LOW_LABEL_MASS
from ..readout import assert_construction_stable, choice_read
from ..session import (DescriptiveCounters, FeatureSpec, assert_modules_absent,
                       check_feature_defined, lexical_hit)
from ..session_e2a import (MENU_TEMPLATES, N_FREE, ROUND_TEMPLATES,
                           SESSION_BANNER, STOP_CAP, session_rng,
                           task_sequence, verify_archived_session)

# --- the three formats (design block 2026-09-06 §4) -------------------------
FORMATS: dict[str, dict] = {
    "F0": {"title": "e2a format of record -- strict alternation, two rounds per label (A B A B)",
           "order": ("first", "second", "first", "second"),
           "purpose": "continuity anchor; e2a strict alternation .840 pooled / .827 reward arm",
           "status": "RETAINED as the continuity anchor (8-session set; design disposition 2026-09-08 item 3)"},
    "F1": {"title": "neutral-start -- two rounds under a neutral third label, then one round per menu label (N N A B)",
           "order": ("neutral", "neutral", "first", "second"),
           "purpose": "the alternation habit is not installed between the two menu labels",
           "status": "RETIRED for the PROPOSAL-k campaign: scaffold-register breakage 5/24 (design disposition 2026-09-08 item 3); the neutral label is not used"},
    "F2": {"title": "block order -- A A B B / B B A A, start counterbalanced",
           "order": ("first", "first", "second", "second"),
           "purpose": "decorrelates round position from label parity (the Stage B/C confound)",
           "status": "FORMAT OF RECORD for PROPOSAL-k Stage 2 (design disposition 2026-09-08 item 3); LOCK-k sets n and the bar"},
}
N_FORCED = 4                 # every format: 4 forced rounds, then N_FREE = 6 free choices
F_FOR_WALK = N_FORCED // 2   # session_e2a's F: n_rounds = 2F + N_FREE = 10
#: Design patch 2026-09-06 §2: the 4 h cap was the wrong cap; raised to 8 h
#: under the long-run checklist (adapter >= 96 W, AC, one process), and the
#: allocation set per format -- F0 is the continuity anchor only (the archive
#: already gives its habit at n = 187 / 102), F1 and F2 carry the question.
#: The design block's 24 x 3 and its 4 h gate are superseded by this patch.
N_PER_FORMAT = {"F0": 8, "F1": 24, "F2": 24}
GATE_HOURS = 8.0
DRAW_SEED = 20260906         # cell assignment only; per-session content is keyed on the index

#: The neutral third label for F1. `cedar` (the first choice) FAILED the
#: design patch's assertion -- it is one of H3's sixteen tags and an e2a
#: archive pair tag -- so the label was re-selected 2026-09-06 under a
#: declared procedure (data/format/neutral_label_selection.json): a fixed
#: candidate order, first to pass (i) single token with a leading space on
#: this tokenizer, (ii) in NO roster (e2d roster of record, H3's sixteen, the
#: h3/a1 candidate rosters, the e2a archive pairs, the e2b campaigns), (iii)
#: word-boundary absent from every pool (the 64 e2a paraphrases, every
#: data/corpus jsonl, e0 frames/probes, s2 frames, b2 framing) and (iv) from
#: the wrapper (rule 28c). `timber`, id 43299, is that candidate. The script
#: re-asserts (i)-(iv) at startup against the live tokenizer and rosters.
NEUTRAL_LABEL = "timber"
NEUTRAL_TOKEN_ID = 43299
NEUTRAL_SELECTION = "data/format/neutral_label_selection.json"

ROLE_POLE = {"first": "pos", "second": "neg", "neutral": "neutral"}

#: Rule 23: declared before the run; tabulated over ALL sessions incl. excluded.
DECLARED_COUNTERS = ("termination", "cap_hit", "audit_degenerate",
                     "content_exclusion", "content_advisory", "lexical",
                     "post_choice_degeneracy", "low_label_mass")

#: A timed session must be COMPLETE -- every forced round generated and every
#: free choice read -- before its wall-clock may enter the projection: a
#: session excluded at forced0 costs ~1/10 of a full one and would let the
#: gate read GO where the true cost is STOP (review finding, 2026-09-06).
#: `--stage time` runs schedule indices in order until one complete session
#: per format is on disk, up to this many attempts, then STOPs.
MAX_TIMING_ATTEMPTS = 4

#: Rule 28(a): each reported feature declared against the sample it is
#: defined ON, with the decidable-n it needs there, BEFORE the run. Code
#: choice, flagged: 16 of 24 (two thirds) -- a break-rate floor sized to be
#: read against, not a bar; below it the figure is reported WITH its
#: diagnosis, never suppressed. Domains: "all" = every session with a first
#: pick (the rule-23 secondaries domain, as e2d's habit secondaries); "valid"
#: = not excluded under the run scope.
FEATURE_FLOOR_FRACTION = 2 / 3     # of the format's registered n; F1/F2 -> 16, F0 -> 6


def feature_floor(fmt: str) -> int:
    import math
    return int(math.ceil(FEATURE_FLOOR_FRACTION * N_PER_FORMAT[fmt]))


def declared_features(fmt: str = "F1") -> list[FeatureSpec]:
    f = feature_floor(fmt)
    return [FeatureSpec(name="first_pick_break", domain="all", min_decidable=f),
            FeatureSpec(name="strict_alternation", domain="valid", min_decidable=f),
            FeatureSpec(name="session_share", domain="valid", min_decidable=f)]


def is_complete(rec: Mapping) -> bool:
    """Every forced round generated and every free choice read."""
    return len(rec["rounds"]) == N_FORCED and rec["n_reads"] == N_FREE


# --- cells, schedule, forced order ------------------------------------------
def cells() -> list[dict]:
    """8 cells: 4 roster pairs x which label is FIRST (nominal plus)."""
    out = []
    for pair in ROSTER:
        for first in (0, 1):
            out.append({"pair": list(pair), "first_index": first,
                        "tag_plus": pair[first], "tag_minus": pair[1 - first]})
    return out


def build_schedule(n: int, rng: np.random.Generator) -> list[dict]:
    """`n` sessions over the 8 cells, whole blocks first (balanced at every
    prefix of 8; exactly balanced at 24). e2d's device."""
    cs = cells()
    sched: list[dict] = []
    while len(sched) < n:
        idx = rng.permutation(len(cs))
        sched += [dict(cs[i]) for i in idx]
    return sched[:n]


def forced_order(fmt: str, cell: Mapping) -> list[tuple[str, str]]:
    """[(tag, role)] for the forced phase of `fmt` in `cell`."""
    tags = {"first": cell["tag_plus"], "second": cell["tag_minus"],
            "neutral": NEUTRAL_LABEL}
    return [(tags[r], r) for r in FORMATS[fmt]["order"]]


def rng_key(fmt: str) -> str:
    return f"fmt-{fmt}"


def round_segment(idx: int, ri: int, n_round: int, tag: str, ttext: str) -> str:
    return ROUND_TEMPLATES[(idx + ri) % 4].format(n=n_round, tag=tag, task=ttext)


def menu_segment(idx: int, ci: int, n_round: int, a: str, b: str) -> str:
    return MENU_TEMPLATES[(idx + ci) % 4].format(n=n_round, a=a, b=b)


# --- audit v3 + lexical, with rule-28(b) precedence ---------------------------
def classify_v3(text: str, task_text: str, earlier: Sequence[str],
                others: Iterable[str], audit3: AuditV3,
                own_tags: Sequence[str]) -> tuple[str | None, list[str], str | None, str | None]:
    """(exclusion, advisory, lexical, content_label). Audit v3 first; the
    lexical check runs only on a response the audit did not claim."""
    r = audit3.check(text, task_text, earlier, others)
    lex = None if r.exclusion else lexical_hit(text, own_tags)
    return r.exclusion, list(r.advisory), lex, r.content_label


def excludes(excl: str | None, lex: str | None, forced: bool, scope: str) -> bool:
    if lex:
        return True
    if not excl:
        return False
    return True if scope == "e2b" else bool(forced)


def strict_exclusion(rec: Mapping) -> tuple[bool, str | None]:
    for r in rec["rounds"] + rec["choices"]:
        if excludes(r["degen"], r.get("lexical"), r["kind"] == "forced", "e2b"):
            return True, f"{r['degen'] or 'lexical:' + r['lexical']}@{r['phase']}"
    return False, None


# --- one session ---------------------------------------------------------------
def _insulated_read(adapter, prefix: str, a: str, b: str, label_ids: Mapping[str, int]):
    assert_modules_absent(FORBIDDEN_MODULES)
    cr = choice_read(adapter, prefix, a, b, label_ids, verify=True)
    assert_construction_stable(cr)               # halts on any nonzero KL
    return cr.pick, cr.as_dict()


def run_session(adapter, fmt: str, idx: int, cell: Mapping, tasks: Sequence[Mapping],
                audit3: AuditV3, ban_ids: Sequence[int], term_rx: Sequence[str],
                others_of: Callable[[str], list[str]], *, temp: float = TEMP,
                scope: str = "e2a",
                _read_override: Callable | None = None) -> dict:
    """One sham session in format `fmt`. Draw order is e2a's exactly.

    `_read_override` exists ONLY for the model-free self-test (a scripted
    pick in place of the forward); the script asserts it is None.
    """
    if fmt not in FORMATS:
        raise ValueError(f"unknown format {fmt!r}")
    rng = session_rng(rng_key(fmt), idx)
    seq = task_sequence(rng, tasks, N_FORCED + N_FREE)
    tp, tm = cell["tag_plus"], cell["tag_minus"]
    order = forced_order(fmt, cell)
    own = (tp, tm)
    lex_tags = own + ((NEUTRAL_LABEL,) if fmt == "F1" else ())
    label_ids = {}
    for t in own:
        enc = adapter.encode(" " + t, add_special_tokens=False)
        if len(enc) != 1:
            raise SystemExit(f"STOP: label {t!r} is {len(enc)} tokens; the read needs single-token labels")
        label_ids[t] = int(enc[0])
    read = _read_override or (lambda prefix, a, b: _insulated_read(adapter, prefix, a, b, label_ids))

    transcript = SESSION_BANNER
    rounds: list[dict] = []
    choices: list[dict] = []
    terms: list[dict] = []
    earlier: list[str] = []
    excluded, reason = False, None
    ti = n_round = 0

    def note_term(text: str, tag: str, pos: str) -> bool:
        if any(re.search(r, text) for r in term_rx):
            terms.append({"format": fmt, "config": tag, "round_pos": pos})
            return True
        return False

    def gen(prefix: str, seg: str, seed: int):
        # SHAM ONLY, UNCACHED: no injections object is ever built here. The
        # arguments actually passed are returned beside the result so the
        # record's `steered` / `round_path_cached` are derived from the call,
        # not asserted (review finding, 2026-09-06).
        injs: tuple = ()
        cached = False
        g = adapter.generate(prefix, seg, injections=injs, seed=seed, temp=temp,
                             max_tokens=STOP_CAP, ban_ids=ban_ids, cached=cached)
        return g, {"steered": bool(injs), "cached": bool(cached), "n_injections": len(injs)}

    for ri, (tag, role) in enumerate(order):
        n_round += 1
        tid, ttext = seq[ti]; ti += 1
        seg = round_segment(idx, ri, n_round, tag, ttext)
        seed = int(rng.integers(2 ** 31))
        g, call = gen(transcript, seg, seed)
        excl, adv, lex, clabel = classify_v3(g.text, ttext, earlier, others_of(ttext), audit3, lex_tags)
        t = note_term(g.text, tag, f"forced{ri}")
        transcript += seg + g.text + "\n"
        rounds.append({"phase": f"forced{ri}", "kind": "forced", "round": ri,
                       "pole": ROLE_POLE[role], "role": role, "tag": tag,
                       "task": tid, "seed": seed, "task_text": ttext,
                       "text": g.text, "n_tok": len(g.token_ids),
                       "cap_hit": bool(g.cap_hit), "stop_reason": g.stop_reason,
                       "steered": call["steered"], "round_path_cached": call["cached"],
                       "degen": excl, "advisory": adv,
                       "content_label": clabel, "lexical": lex, "termination": t,
                       "transcript_tokens_after": len(adapter.encode(transcript))})
        earlier.append(g.text)
        if excludes(excl, lex, True, scope):
            excluded, reason = True, f"{excl or 'lexical:' + lex}@forced{ri}"
            break

    for ci in range(N_FREE):
        if excluded:
            break
        n_round += 1
        a, b = ((tp, tm) if rng.integers(2) == 0 else (tm, tp))
        menu = menu_segment(idx, ci, n_round, a, b)
        prefix_tokens = len(adapter.encode(transcript + menu))
        pick, read_rec = read(transcript + menu, a, b)
        picked = "pos" if pick == tp else "neg"
        tid, ttext = seq[ti]; ti += 1
        chosen = round_segment(idx, ci, n_round, pick, ttext)
        seed = int(rng.integers(2 ** 31))
        prefix = transcript + menu + f" {pick}\n"
        g, call = gen(prefix, chosen, seed)
        excl, adv, lex, clabel = classify_v3(g.text, ttext, earlier, others_of(ttext), audit3, lex_tags)
        t = note_term(g.text, pick, f"free{ci}")
        transcript += menu + f" {pick}\n" + chosen + g.text + "\n"
        choices.append({"phase": f"free{ci}", "kind": "free", "round": ci,
                        "menu_a": a, "menu_b": b, "pick": pick,
                        "picked_pole": picked,
                        "picked_role": "first" if picked == "pos" else "second",
                        "read": read_rec, "prefix_tokens_at_read": prefix_tokens,
                        "task": tid, "seed": seed, "task_text": ttext,
                        "text": g.text, "n_tok": len(g.token_ids),
                        "cap_hit": bool(g.cap_hit), "stop_reason": g.stop_reason,
                        "steered": call["steered"], "round_path_cached": call["cached"],
                        "degen": excl, "advisory": adv,
                        "content_label": clabel, "lexical": lex, "termination": t,
                        "low_label_mass": bool(read_rec["label_mass"] < LOW_LABEL_MASS),
                        "transcript_tokens_after": len(adapter.encode(transcript))})
        earlier.append(g.text)
        if excludes(excl, lex, False, scope):
            excluded, reason = True, f"{excl or 'lexical:' + lex}@free{ci}"

    last_forced_tag = rounds[-1]["tag"] if rounds else None
    first_pick = choices[0]["pick"] if choices else None
    retention = None
    if choices:
        p0 = choices[0]["prefix_tokens_at_read"]
        retention = {r["phase"]: p0 - r["transcript_tokens_after"] for r in rounds}
    rec = {"format": fmt, "session": idx, "cell": dict(cell),
           "tag_plus": tp, "tag_minus": tm, "pair": list(cell["pair"]),
           "neutral_label": NEUTRAL_LABEL if fmt == "F1" else None,
           "forced_tags": [t for t, _ in order], "forced_roles": [r for _, r in order],
           "F": F_FOR_WALK, "n_forced": N_FORCED,
           "excluded": bool(excluded), "exclude_reason": reason,
           "exclusion_scope": scope, "temp": temp,
           "round_path_cached": any(x["round_path_cached"] for x in rounds + choices),
           "sham_only": not any(x["steered"] for x in rounds + choices),
           "rounds": rounds, "choices": choices, "terminations": terms,
           "transcript": transcript,
           "n_rounds_generated": len(rounds) + len(choices),
           "first_free_pick_pos": (choices[0]["picked_pole"] == "pos") if choices else None,
           "first_pick_is_last_forced_label": (first_pick == last_forced_tag) if choices else None,
           "tokens_forced_end_to_first_read": retention,
           "n_reads": len(choices)}
    rec["complete"] = is_complete(rec)
    rec["strict_excluded"], rec["strict_exclude_reason"] = strict_exclusion(rec)
    return rec


def tally(counters: DescriptiveCounters, rec: Mapping) -> None:
    """Rule 23: over ALL sessions, excluded included."""
    counters.n_sessions += 1
    ex = rec["excluded"]
    for r in rec["rounds"] + rec["choices"]:
        d = r["degen"]
        if d and d.startswith("audit:"):
            counters.note("audit_degenerate", d.split(":", 2)[1], excluded=ex)
        elif d and d.startswith("content:"):
            counters.note("content_exclusion", d.split(":", 1)[1], excluded=ex)
        for a in r.get("advisory", ()):
            counters.note("content_advisory", a.split(":", 1)[1], excluded=ex)
        if d and r["kind"] == "free":
            counters.note("post_choice_degeneracy", rec["format"], excluded=ex)
        if r.get("lexical"):
            counters.note("lexical", r["lexical"], excluded=ex)
        if r["cap_hit"]:
            counters.note("cap_hit", r["phase"], excluded=ex)
        if r["termination"]:
            counters.note("termination", rec["format"], excluded=ex)
        if r.get("low_label_mass"):
            counters.note("low_label_mass", rec["format"], excluded=ex)


# --- checkpointed campaign, per format ----------------------------------------
def run_identity(fmt: str, seed: int, scope: str, temp: float,
                 audit_sha16: str) -> dict:
    """Everything a resume must match: the design of every SESSION. temp is
    this recon's dose; the audit sha, the roster and the neutral label are
    the instrument (trap 36's guard, generalised). The registered n is NOT
    part of it: n is a count over a schedule that is built whole-blocks-first
    from the pinned seed, so the first k sessions of an n-schedule are the
    first k of any larger n-schedule -- a reallocation before the run
    (design patch 2026-09-06 §2: F0 24 -> 8) changes how many sessions run,
    never which. `load_checkpoint` pins the SCHEDULE PREFIX instead and
    refuses a shrink that would orphan a session already on disk."""
    ident = {"format": fmt, "seed": seed, "scope": scope, "temp": float(temp),
             "audit_v2_sha16": audit_sha16, "roster": [list(p) for p in ROSTER],
             "n_forced": N_FORCED, "n_free": N_FREE}
    # The neutral label is part of a session's design ONLY where a neutral
    # round is generated (F1). F0 and F2 never see it, so their sessions are
    # identical under any declared neutral label -- pinning it for them
    # refused the timing checkpoints for nothing (launch of 2026-09-06 16:13
    # UTC, refused at F0 on cedar -> timber; see the log).
    if "neutral" in FORMATS[fmt]["order"]:
        ident["neutral_label"] = NEUTRAL_LABEL
    return ident


def _cell_key(c: Mapping) -> tuple:
    return (tuple(c["pair"]), c["tag_plus"], c["tag_minus"])


def load_checkpoint(path: str, identity: Mapping, n: int, sched: Sequence[Mapping]) -> dict:
    ck = json.load(open(path))
    got = {k: ck.get("identity", {}).get(k) for k in identity}
    if got != dict(identity):
        diff = {k: (got[k], identity[k]) for k in identity if got[k] != identity[k]}
        raise SystemExit(f"CHECKPOINT MISMATCH: {path} differs on {diff} (recorded, this run). "
                         f"Resuming across a different design would splice two designs -- refusing.")
    if not ck.get("sham_only", False):
        raise SystemExit(f"CHECKPOINT {path} is not marked sham_only -- refusing.")
    on_disk = [r["session"] for r in ck["sessions"]]
    beyond = [i for i in on_disk if i >= n]
    if beyond:
        raise SystemExit(f"CHECKPOINT {path} holds sessions {beyond} at or beyond the registered n = {n}; "
                         f"a shrink that orphans sessions on disk is a cut, not a reallocation -- refusing.")
    for r in ck["sessions"]:
        if _cell_key(r["cell"]) != _cell_key(sched[r["session"]]):
            raise SystemExit(f"CHECKPOINT {path}: session {r['session']} was run in cell {_cell_key(r['cell'])} "
                             f"but this schedule puts {_cell_key(sched[r['session']])} there -- refusing.")
    return ck


def run_format(adapter, fmt: str, n: int, tasks, audit3: AuditV3, ban_ids, term_rx,
               others_of, *, temp: float = TEMP, scope: str = "e2a", seed: int = DRAW_SEED,
               audit_sha16: str = "", checkpoint_path: str, resume: bool = False,
               limit: int = 0, progress: Callable[[str], None] = print,
               _read_override: Callable | None = None) -> dict:
    """The registered n for one format, checkpointed after every session.

    Resume is skip-only (completes the schedule, never extends it). `limit`
    stops once `limit` sessions are ON DISK, resumed ones included (trap 36).
    An existing checkpoint without `--resume` is a refusal, never an
    overwrite (trap 22). `_read_override` is the self-test's scripted read
    only; the script never passes it.
    """
    assert_modules_absent(FORBIDDEN_MODULES)
    counters = DescriptiveCounters(declared=DECLARED_COUNTERS)
    identity = run_identity(fmt, seed, scope, temp, audit_sha16)
    sched = build_schedule(n, np.random.default_rng(seed))
    sessions: list[dict] = []
    kls: list[float] = []
    secs: list[float] = []
    done: set[int] = set()
    n_history: list[dict] = [{"n": n, "note": "this run"}]
    if os.path.exists(checkpoint_path):
        if not resume:
            raise SystemExit(f"CHECKPOINT EXISTS at {checkpoint_path}; pass --resume to continue it "
                             f"or move it aside. A run never silently overwrites one (trap 22).")
        ck = load_checkpoint(checkpoint_path, identity, n, sched)
        prev = ck.get("n_history", [{"n": ck.get("n"), "note": "recorded"}])
        n_history = prev + ([] if prev and prev[-1].get("n") == n else [{"n": n, "note": "reallocated before resume"}])
        sessions, kls, secs = ck["sessions"], ck.get("verify_kls", []), ck.get("per_session_seconds", [])
        for rec in sessions:
            done.add(rec["session"])
            tally(counters, rec)
        progress(f"    [{fmt}] RESUMED from {checkpoint_path}: {len(sessions)} sessions on disk, {len(kls)} reads")

    def checkpoint():
        tmp = checkpoint_path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump({"identity": identity, "format": fmt, "seed": seed, "n": n, "n_history": n_history,
                       "scope": scope, "temp": temp, "sham_only": all(r["sham_only"] for r in sessions),
                       "round_path_cached": any(r["round_path_cached"] for r in sessions),
                       "sessions": sessions, "verify_kls": kls,
                       "per_session_seconds": secs}, fh, default=float)
        os.replace(tmp, checkpoint_path)

    for i, cell in enumerate(sched):
        if limit and len(sessions) >= limit:
            progress(f"    [{fmt}] --limit {limit}: {len(sessions)} sessions on disk, stopping")
            break
        if i in done:
            continue
        ts = time.time()
        rec = run_session(adapter, fmt, i, cell, tasks, audit3, ban_ids, term_rx, others_of,
                          temp=temp, scope=scope, _read_override=_read_override)
        dt = time.time() - ts
        rec["seconds"] = dt
        for c in rec["choices"]:
            kls.append(c["read"]["verify_kl"])
        secs.append(dt)
        tally(counters, rec)
        sessions.append(rec)
        checkpoint()
        fp = rec["first_pick_is_last_forced_label"]
        progress(f"    [{fmt}] s{i} {cell['tag_plus']}>{cell['tag_minus']} "
                 f"{'EXCLUDED ' + str(rec['exclude_reason']) if rec['excluded'] else 'valid'}  "
                 f"{rec['n_reads']} reads  first-pick {'n/a' if fp is None else ('BREAK' if fp else 'follows')}  "
                 f"{'complete' if rec['complete'] else 'TRUNCATED'}  {dt:.0f}s")
        sys.stdout.flush()
    return {"format": fmt, "sessions": sessions, "counters": counters, "verify_kls": kls,
            "per_session_seconds": secs, "schedule_n": n, "n_history": n_history, "seed": seed,
            "scope": scope, "identity": identity}


# --- acceptance (computed before any artifact is written, trap 6) --------------
def as_e2a_row(rec: Mapping) -> dict:
    return {"arm": rng_key(rec["format"]), "session": rec["session"], "F": rec["F"],
            "pair": rec["pair"], "tag_plus": rec["tag_plus"],
            "rounds": [{"tag": r["tag"], "seed": r["seed"], "task": r["task"]} for r in rec["rounds"]],
            "choices": [{"pick": c["pick"], "seed": c["seed"], "task": c["task"],
                         "menu_a": c["menu_a"], "menu_b": c["menu_b"]} for c in rec["choices"]],
            "transcript": rec["transcript"]}


def verify_format_walk(recs: Sequence[Mapping], tasks) -> dict:
    """Every session through `session_e2a.verify_archived_session`; reports
    walked beside passed (trap 5)."""
    walked = ok = seeds_ok = 0
    failures = []
    for rec in recs:
        walked += 1
        try:
            r = verify_archived_session(as_e2a_row(rec), tasks)
        except AssertionError as exc:
            failures.append({"format": rec["format"], "session": rec["session"], "why": str(exc)})
            continue
        if r["ok"]:
            ok += 1
            seeds_ok += int(r["seeds_match"])
        else:
            failures.append({"format": rec["format"], "session": rec["session"], "why": r["why"]})
    return {"check": "session_e2a.verify_archived_session", "n_walked": walked,
            "n_reconstructed": ok, "n_seed_streams_matched": seeds_ok,
            "all_ok": walked > 0 and ok == walked and seeds_ok == walked,
            "failures": failures[:5]}


# --- the timing gate (trap 32: structural) --------------------------------------
def projection(timed: Mapping[str, Mapping], n_per_format: Mapping[str, int] | None = None,
               gate_hours: float = GATE_HOURS) -> dict:
    """`timed` = {fmt: {"seconds": [...], "complete": [...]}} for the timed
    session(s) per format. ONLY COMPLETE sessions enter the projection; a
    format with none is a refusal, not a pass (trap 5)."""
    n_per_format = dict(N_PER_FORMAT if n_per_format is None else n_per_format)
    per = {}
    total_s = 0.0
    for fmt in FORMATS:
        row = timed.get(fmt, {})
        s_all = list(row.get("seconds", []))
        comp = list(row.get("complete", []))
        if len(comp) != len(s_all):
            raise SystemExit(f"TIMING MALFORMED for {fmt}: {len(s_all)} seconds vs {len(comp)} complete flags")
        s = [x for x, c in zip(s_all, comp) if c]
        if not s:
            raise SystemExit(f"TIMING INCOMPLETE: no COMPLETE timed session for {fmt} "
                             f"({len(s_all)} timed, all truncated); the gate needs one complete session per format")
        mean = float(np.mean(s))
        nf = n_per_format[fmt]
        per[fmt] = {"n": nf, "n_timed": len(s_all), "n_complete": len(s), "mean_session_s_complete": mean,
                    "truncated_seconds_excluded_from_projection": [x for x, c in zip(s_all, comp) if not c],
                    "projected_s": mean * nf, "projected_h": mean * nf / 3600}
        total_s += mean * nf
    verdict = "GO" if total_s / 3600 <= gate_hours else "STOP"
    return {"per_format": per, "n_per_format": n_per_format, "projected_total_s": total_s,
            "projected_total_h": total_s / 3600, "gate_hours": gate_hours, "verdict": verdict,
            "rule": "design block 2026-09-06 §4 as amended by the design patch 2026-09-06 §2: STOP if the formats project past the gate (8 h)"}


def assert_gate_admits(timing_path: str, gate_hours: float = GATE_HOURS) -> dict:
    """The structural gate on --stage run: a timing artifact must exist, every
    format's timed sessions must have PASSED acceptance (a fired bar, a
    nonzero KL or a failed walk on a timed session is an escalation, never
    something the run absorbs), and the projection from COMPLETE sessions
    must be at or under the gate."""
    if not os.path.exists(timing_path):
        raise SystemExit(f"NO TIMING ARTIFACT at {timing_path}: --stage time runs first and reports "
                         f"before anything runs (design block §4; trap 32).")
    t = json.load(open(timing_path))
    acc = t.get("acceptance_on_timed_sessions")
    if not acc or set(acc) != set(FORMATS):
        raise SystemExit(f"TIMING ARTIFACT carries no per-format acceptance for all of {list(FORMATS)}; refusing.")
    failed = {f: a for f, a in acc.items() if not a.get("PASS")}
    if failed:
        raise SystemExit(f"TIMING ACCEPTANCE FAILED on {sorted(failed)}: "
                         f"{ {f: (a.get('bars_fired'), a.get('kl_all_exact'), a.get('format_walk', {}).get('all_ok')) for f, a in failed.items()} }. "
                         f"A fired bar or a broken read on a timed session is escalated, never absorbed; Code does not self-adjudicate.")
    p = projection({f: {"seconds": v["seconds"], "complete": v["complete"]} for f, v in t["timed"].items()},
                   gate_hours=gate_hours)
    if p["verdict"] != "GO":
        raise SystemExit(f"TIMING GATE STOP: projected {p['projected_total_h']:.2f} h for "
                         f"{p['n_per_format']} sessions > {gate_hours} h. The design seat decides; "
                         f"Code does not run past its own STOP.")
    return p


def refuse_overwrite(path: str, new_complete: bool, new_n: int) -> None:
    """Trap 22 (PERMANENT): a subset or partial run never overwrites a
    complete canonical artifact. Refuses; the caller passes --out-name."""
    if not os.path.exists(path):
        return
    try:
        old = json.load(open(path))
    except Exception:
        old = {}
    if old.get("complete") and (not new_complete or new_n < old.get("n_on_disk", 0)):
        raise SystemExit(f"REFUSING TO OVERWRITE {path}: it holds a COMPLETE run ({old.get('n_on_disk')} sessions) "
                         f"and this run is {'partial' if not new_complete else 'smaller'} ({new_n}). "
                         f"Pass --out-name for a subset artifact (trap 22).")


# --- analysis (descriptive; no bar) -------------------------------------------
def _rate(k, n):
    return (k / n) if n else None


def analyze_format(recs: Sequence[Mapping]) -> dict:
    valid = [r for r in recs if not r["excluded"]]
    with_pick = [r for r in recs if r["choices"]]
    six = [r for r in valid if len(r["choices"]) == N_FREE]
    alt_valid = [r for r in valid if H.strictly_alternates(r) is not None]
    alt_all = [r for r in recs if H.strictly_alternates(r) is not None]
    brk_all = [r for r in with_pick if r["first_pick_is_last_forced_label"] is not None]
    brk_valid = [r for r in valid if r["first_pick_is_last_forced_label"] is not None]
    picks_valid = [c for r in valid for c in r["choices"]]
    per_session_share = [np.mean([c["picked_pole"] == "pos" for c in r["choices"]]) for r in valid if r["choices"]]
    # audit v3 counts over ALL rounds (rule 23)
    rounds = [(r, x) for r in recs for x in r["rounds"] + r["choices"]]
    def count(pred):
        out: dict[str, int] = {}
        for _, x in rounds:
            for k in pred(x):
                out[k] = out.get(k, 0) + 1
        return dict(sorted(out.items()))
    v2 = count(lambda x: [x["degen"].split(":", 2)[1]] if x["degen"] and x["degen"].startswith("audit:") else [])
    cexcl = count(lambda x: [x["degen"].split(":", 1)[1]] if x["degen"] and x["degen"].startswith("content:") else [])
    cadv = count(lambda x: [a.split(":", 1)[1] for a in x.get("advisory", ())])
    lex = count(lambda x: [x["lexical"]] if x.get("lexical") else [])
    by_phase = {}
    for _, x in rounds:
        ph = by_phase.setdefault(x["phase"], {"n": 0, "n_tok": [], "v2": 0, "content_excl": 0, "advisory": 0, "cap_hit": 0})
        ph["n"] += 1; ph["n_tok"].append(x["n_tok"])
        ph["v2"] += int(bool(x["degen"] and x["degen"].startswith("audit:")))
        ph["content_excl"] += int(bool(x["degen"] and x["degen"].startswith("content:")))
        ph["advisory"] += int(bool(x.get("advisory")))
        ph["cap_hit"] += int(bool(x["cap_hit"]))
    tok = {ph: {"n": v["n"], "mean": float(np.mean(v["n_tok"])), "min": int(min(v["n_tok"])), "max": int(max(v["n_tok"])),
                "sd": float(np.std(v["n_tok"], ddof=1)) if len(v["n_tok"]) > 1 else None,
                "v2_audit": v["v2"], "content_exclusion": v["content_excl"], "advisory": v["advisory"], "cap_hit": v["cap_hit"]}
           for ph, v in sorted(by_phase.items())}
    ret = {}
    for r in with_pick:
        for ph, d in (r["tokens_forced_end_to_first_read"] or {}).items():
            ret.setdefault(ph, []).append(d)
    retention = {ph: {"mean": float(np.mean(v)), "min": int(min(v)), "max": int(max(v)), "n": len(v)} for ph, v in sorted(ret.items())}
    prefix_at_reads = {}
    for r in with_pick:
        for c in r["choices"]:
            prefix_at_reads.setdefault(c["phase"], []).append(c["prefix_tokens_at_read"])
    kls = [c["read"]["verify_kl"] for r in recs for c in r["choices"]]
    scopes = sorted({r.get("exclusion_scope") for r in recs})
    fmt = recs[0]["format"] if recs else "F1"
    feats = {}
    for spec in declared_features(fmt):
        k, n_dom = {"first_pick_break": (len(brk_all), len(with_pick)),
                    "strict_alternation": (len(alt_valid), len(valid)),
                    "session_share": (len(per_session_share), len(valid))}[spec.name]
        feats[spec.name] = {"domain": spec.domain, "decidable": k, "domain_n": n_dom, "floor": spec.min_decidable,
                            "diagnosis": check_feature_defined(spec, k, n_dom) if n_dom else f"{spec.name}: empty domain",
                            "reported_regardless": True}
    return {
        "n_sessions": len(recs), "exclusion_scope_of_run": scopes[0] if len(scopes) == 1 else scopes,
        "n_valid_run_scope": len(valid),
        "n_excluded_run_scope": sum(1 for r in recs if r["excluded"]),
        "n_excluded_strict": sum(1 for r in recs if r["strict_excluded"]),
        "n_complete": sum(1 for r in recs if r.get("complete", is_complete(r))),
        "exclusion_reasons_run_scope": [r["exclude_reason"] for r in recs if r["excluded"]],
        "exclusion_reasons_strict": [r["strict_exclude_reason"] for r in recs if r["strict_excluded"]],
        "features_rule28a": feats,
        "refusals": refusal_counts(recs),
        "strict_alternation": {"valid": {"k": sum(1 for r in alt_valid if H.strictly_alternates(r)), "n": len(alt_valid),
                                         "rate": _rate(sum(1 for r in alt_valid if H.strictly_alternates(r)), len(alt_valid))},
                               "all_with_2plus_picks": {"k": sum(1 for r in alt_all if H.strictly_alternates(r)), "n": len(alt_all),
                                                        "rate": _rate(sum(1 for r in alt_all if H.strictly_alternates(r)), len(alt_all))},
                               "valid_with_six_picks": {"k": sum(1 for r in six if H.strictly_alternates(r)), "n": len(six),
                                                        "rate": _rate(sum(1 for r in six if H.strictly_alternates(r)), len(six))}},
        "first_pick_break": {"definition": "first free pick IS the last forced label (the alternation habit broken); in F2 this is also the 'stay' rate",
                             "all_with_a_pick": {"k": sum(1 for r in brk_all if r["first_pick_is_last_forced_label"]), "n": len(brk_all),
                                                 "rate": _rate(sum(1 for r in brk_all if r["first_pick_is_last_forced_label"]), len(brk_all))},
                             "valid": {"k": sum(1 for r in brk_valid if r["first_pick_is_last_forced_label"]), "n": len(brk_valid),
                                       "rate": _rate(sum(1 for r in brk_valid if r["first_pick_is_last_forced_label"]), len(brk_valid))}},
        "session_share_on_first_label": {"definition": "share of free picks on tag_plus (the nominal first label), valid sessions; e2a's share_all_choices with the nominal pole",
                                          "pooled_over_choices": _rate(sum(1 for c in picks_valid if c["picked_pole"] == "pos"), len(picks_valid)),
                                          "n_choices": len(picks_valid),
                                          "mean_of_per_session": float(np.mean(per_session_share)) if per_session_share else None,
                                          "n_sessions": len(per_session_share)},
        "audit_v3": {"version": AUDIT_VERSION, "n_rounds": len(rounds),
                     "v2_audit_by_category": v2, "content_exclusion_by_class": cexcl,
                     "content_advisory_by_class": cadv, "lexical_by_tag": lex,
                     "rounds_with_any_exclusion_bearing_hit": sum(1 for _, x in rounds if x["degen"]),
                     "rounds_with_advisory": sum(1 for _, x in rounds if x.get("advisory"))},
        "per_round": tok,
        "tokens_forced_end_to_first_read": retention,
        "prefix_tokens_at_read": {ph: {"mean": float(np.mean(v)), "min": int(min(v)), "max": int(max(v))} for ph, v in sorted(prefix_at_reads.items())},
        "reads": {"n": len(kls), "kl_exactly_zero": sum(1 for k in kls if k == 0.0), "kl_max": max(kls) if kls else None},
        "low_label_mass": sum(1 for r in recs for c in r["choices"] if c["low_label_mass"]),
        "terminations": sum(len(r["terminations"]) for r in recs),
        "cap_hits": sum(1 for _, x in rounds if x["cap_hit"]),
        "seconds": {"mean": float(np.mean([r["seconds"] for r in recs if "seconds" in r])) if any("seconds" in r for r in recs) else None,
                    "total": float(sum(r.get("seconds", 0.0) for r in recs))},
    }


def refusal_counts(recs: Sequence[Mapping]) -> dict:
    """Design patch 2026-09-06 §2: refusal counts per format and per round
    position. Two countable things, both declared: (a) `null_response`
    exclusions (the adopted rule: content-free OR a declining predicate with
    < 3 content words left); (b) rounds whose text matches the adopted
    rule's DECLINING-PREDICATE shape at all, residual ignored -- a refusal
    with delivered content beside it. The imperative shape ('Please don't
    ask me to do that.') is a declared miss and is countable only by the
    rule-25 read; it is NOT counted here."""
    from ..e2d import contentclass_v4 as V4
    by_phase: dict[str, dict] = {}
    for r in recs:
        for x in r["rounds"] + r["choices"]:
            ph = by_phase.setdefault(x["phase"], {"n": 0, "null_response": 0, "declining_predicate_any": 0})
            ph["n"] += 1
            ph["null_response"] += int(x["degen"] == "content:null_response")
            ph["declining_predicate_any"] += int(bool(V4._REFUSAL.search(V4.strip_leading_label(x["text"]))))
    tot = {"n": sum(v["n"] for v in by_phase.values()),
           "null_response": sum(v["null_response"] for v in by_phase.values()),
           "declining_predicate_any": sum(v["declining_predicate_any"] for v in by_phase.values())}
    return {"by_round_position": dict(sorted(by_phase.items())), "total": tot,
            "not_counted": "imperative refusals without a declining predicate (declared miss; the read counts them)"}


def anchors() -> dict:
    """The archives the formats are read against, through the same functions.
    Every block carries BOTH domains: `all` (every session, the rule-23
    secondaries domain) and `valid` (not excluded), so a format row's
    valid-domain alternation and all-with-a-pick break rate each have a
    like-for-like anchor."""
    out = {}
    e2a = [json.loads(l) for l in open(os.path.join(DATA, "e2a/sessions.jsonl")) if l.strip()]
    def dom(rows):
        alt = [r for r in rows if H.strictly_alternates(r) is not None]
        brk = [r for r in rows if H.follows_habit(r) is not None]
        return {"n": len(rows),
                "strict_alternation": {"k": sum(1 for r in alt if H.strictly_alternates(r)), "n": len(alt), "rate": _rate(sum(1 for r in alt if H.strictly_alternates(r)), len(alt))},
                "first_pick_break": {"k": sum(1 for r in brk if not H.follows_habit(r)), "n": len(brk), "rate": _rate(sum(1 for r in brk if not H.follows_habit(r)), len(brk))}}
    def block(rows):
        return {"all": dom(rows), "valid": dom([r for r in rows if not r["excluded"]])}
    out["e2a_all_arms"] = block(e2a)
    out["e2a_reward_arm"] = block([r for r in e2a if r["arm"] == "reward"])
    out["e2a_sham_arm"] = block([r for r in e2a if r["arm"] == "sham"])
    for tier in ("d2", "d3"):
        p = os.path.join(DATA, f"e2d/{tier}_sessions.json")
        if os.path.exists(p):
            ss = json.load(open(p))["sessions"]
            for arm in sorted(set(s["arm"] for s in ss)):
                out[f"e2d_{tier}_{arm}"] = block([s for s in ss if s["arm"] == arm])
    return out


__all__ = ["FORMATS", "N_FORCED", "N_PER_FORMAT", "GATE_HOURS", "DRAW_SEED", "NEUTRAL_LABEL",
           "NEUTRAL_TOKEN_ID", "NEUTRAL_SELECTION", "ROLE_POLE", "DECLARED_COUNTERS", "MAX_TIMING_ATTEMPTS",
           "FEATURE_FLOOR_FRACTION", "feature_floor", "declared_features", "is_complete", "cells", "build_schedule",
           "forced_order", "rng_key", "round_segment", "menu_segment", "classify_v3", "excludes",
           "strict_exclusion", "run_session", "tally", "run_identity", "load_checkpoint",
           "run_format", "as_e2a_row", "verify_format_walk", "projection", "assert_gate_admits",
           "refuse_overwrite", "analyze_format", "refusal_counts", "anchors"]
