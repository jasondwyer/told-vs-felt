"""e2d session runner -- the B3 pattern on the Qwen MLX oracle.

PROPOSAL-j v1.1 §1-§2. e2a's free operant with the negative pole removed and
the dose the only moving part. One label's rounds deliver +axis during their
task tokens; the other label's rounds deliver nothing. Every choice is a
vanilla, uncached, state-free re-forward.

INSULATION IS A PROPERTY OF THE CALL, NOT OF DISCIPLINE.
`readout.choice_read` takes no injections argument, so a state at a choice
position is not something this runner declines to do -- it is something it
cannot do. On top of that, per PROPOSAL-j §3 and the D1 block:

  * `assert_modules_absent(("valence_core.e2b.statepresent",))` at startup
    AND before every single read. "We didn't call it" is a promise; "it is
    not in sys.modules" is a fact, and a fact re-checked 48 times is cheap.
  * every free-choice read runs `verify=True` and
    `assert_construction_stable`, so a nonzero KL halts rather than being
    absorbed. The KL is logged per read, not just asserted, because
    "48/48 at exactly 0.0" is an acceptance claim that has to be countable.

THIS RUNNER COMPUTES NO VERDICT. It writes sessions and counters.
Q1/Q2/Q3 and the run-dose rule live in `scripts/e2d_d2_analyze.py`, which is
committed before D2 runs. A runner that cannot compute the verdict cannot be
accused of having stopped when it liked one.

DELIVERY GEOMETRY. `adapter.generate` places the injection at the segment
boundary and never before it, so the state is live over the round's task
tokens only. Nothing is live while the menu or the choice is read.
"""

from __future__ import annotations

import re
import time
from typing import Callable, Sequence

import numpy as np

from ..readout import assert_construction_stable, choice_read
from ..session import (DescriptiveCounters, assert_modules_absent,
                       classify_response)
from ..session_e2a import (MENU_TEMPLATES, N_FREE, ROUND_TEMPLATES,
                           SESSION_BANNER, STOP_CAP, session_rng,
                           task_sequence)
from .config import (ARMS, DECLARED_COUNTERS, EXCLUSION_SCOPE, F, ROSTER,
                     TEMP)

#: Rule 5 horn (a). The quarantined state-present primitive has no business
#: in e2d and its absence is asserted, never assumed.
FORBIDDEN_MODULES = ("valence_core.e2b.statepresent",)

#: A choice whose two label tokens hold less than this much of the
#: next-token mass is a descriptive flag, not an exclusion (e2a's convention,
#: p0 = 0.20 on choices, pooled).
LOW_LABEL_MASS = 0.20


def strata_for(arm: str) -> list[dict]:
    """16 cells for M (4 pairs x 2 maps x 2 forced-end); 8 for S and R
    (pairs x maps), forced order counterbalanced INSIDE the stratum by seeded
    assignment rather than by being a stratum dimension.

    Ported from `scripts/e2b_verdict_campaign.py:141-165` -- PROPOSAL-j §3
    names that builder by line, so this is a port and not a re-derivation.
    The roster is AMENDMENT 1 (i)'s.
    """
    out = []
    for pair in ROSTER:
        for m in (0, 1):
            base = {"pair": list(pair), "map": m,
                    "tag_plus": pair[m], "tag_minus": pair[1 - m]}
            if ARMS[arm]["strata"] == 16:
                for end in ("pos", "neg"):
                    out.append({**base, "forced_end": end})
            else:
                out.append({**base, "forced_end": None})
    return out


def build_schedule(arm: str, n: int, rng: np.random.Generator) -> list[dict]:
    """`n` sessions over the arm's cells, whole blocks first so the design
    stays balanced at every prefix of the run.

    For the 8-cell arms the forced-end dimension is not a stratum, so it is
    counterbalanced across reps here -- the same device the e2b builder uses.
    At D1's n = 4/2/2 no arm completes even one block; the assignment is
    still seeded and recorded, and D1 claims no balance it does not have.
    """
    cells = strata_for(arm)
    sched: list[dict] = []
    rep = 0
    while len(sched) < n:
        block = [dict(c) for c in cells]
        if ARMS[arm]["strata"] == 8:
            for c in block:
                c["forced_end"] = "pos" if (rep % 2 == 0) else "neg"
        idx = rng.permutation(len(block))
        sched += [block[i] for i in idx]
        rep += 1
    return sched[:n]


def excludes(degen: str | None, lex: str | None, forced: bool,
             scope: str = EXCLUSION_SCOPE) -> bool:
    """Does this round's classification exclude the session?

    `scope` is `config.EXCLUSION_SCOPE`'s open item, isolated in one function
    so that switching it is a one-word change and so that the post-hoc
    recount under the other scope is the same code, not a second
    implementation of it.
    """
    if lex:
        return True
    if not degen:
        return False
    return True if scope == "e2b" else bool(forced)


def strict_exclusion(rec: dict) -> tuple[bool, str | None]:
    """The "e2b" scope's verdict on an already-run session, recovered from
    the recorded per-round classifications.

    This is why D1 runs lenient: every round of a lenient session carries its
    own `degen`/`lexical`, so the strict scope's exclusion set is exactly
    computable after the fact. Nothing has to be re-run to have both numbers.
    """
    for r in rec["rounds"] + rec["choices"]:
        forced = r["phase"].startswith("forced")
        if excludes(r["degen"], r.get("lexical"), forced, scope="e2b"):
            return True, f"{'audit' if r['degen'] else 'lexical'}:" \
                         f"{r['degen'] or r['lexical']}@{r['phase']}"
    return False, None


def run_session(adapter, arm: str, idx: int, cell: dict,
                tasks: Sequence[dict], inj, audit, ban_ids: Sequence[int],
                term_rx: Sequence[str], *, temp: float = TEMP,
                scope: str = EXCLUSION_SCOPE,
                on_read: Callable[[dict], None] | None = None) -> dict:
    """One e2d session.

    `inj` is the +pole injection or None (arms S, and R carries a random
    direction in the same slot). THERE IS NO NEGATIVE POLE: the -tag's rounds
    run with `injections=[]`, which is the CPP contrast and PROPOSAL-j §6's
    welfare commitment expressed in code.

    The rng draw order is e2a's exactly -- task permutation, paraphrase
    draws, then per-round generation seeds interleaved with menu-order draws
    -- because `session_e2a.verify_archived_session` replays that order and
    D1's acceptance is that the replay reconstructs these sessions
    byte-for-byte. A runner that drew in a different order would still
    produce sessions; they just would not be e2a-format ones, and nothing
    would say so.
    """
    rng = session_rng(f"e2d-{arm}", idx)
    seq = task_sequence(rng, tasks, 2 * F + N_FREE)
    tp, tm = cell["tag_plus"], cell["tag_minus"]
    own = (tp, tm)
    label_ids = {t: int(adapter.encode(" " + t, add_special_tokens=False)[0])
                 for t in own}

    # forced_end fixes which pole ENDS the forced block; start is its
    # complement. For the 8-cell arms it is assigned by build_schedule.
    start_plus = cell["forced_end"] == "neg"
    order = (["pos", "neg"] if start_plus else ["neg", "pos"]) * F

    transcript = SESSION_BANNER
    rounds: list[dict] = []
    choices: list[dict] = []
    terms: list[dict] = []
    excluded, reason = False, None
    ti = n_round = 0

    def note_term(text: str, tag: str, pos: str):
        if any(re.search(r, text) for r in term_rx):
            terms.append({"arm": arm, "config": tag, "round_pos": pos})
            return True
        return False

    for ri, pole in enumerate(order):
        n_round += 1
        tid, ttext = seq[ti]; ti += 1
        tag = tp if pole == "pos" else tm
        seg = ROUND_TEMPLATES[(idx + ri) % 4].format(n=n_round, tag=tag,
                                                     task=ttext)
        seed = int(rng.integers(2 ** 31))
        # THE CONTINGENCY: +tag rounds carry the state, -tag rounds carry
        # nothing. No -axis is ever constructed anywhere in e2d.
        injs = [inj] if (inj is not None and pole == "pos") else []
        g = adapter.generate(transcript, seg, injections=injs, seed=seed,
                             temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=False)
        degen, lex = classify_response(g.text, audit, own)
        t = note_term(g.text, tag, f"forced{ri}")
        rounds.append({"phase": f"forced{ri}", "kind": "forced", "round": ri,
                       "pole": pole, "tag": tag, "task": tid, "seed": seed,
                       "task_text": ttext, "text": g.text, "n_tok": len(g.token_ids),
                       "cap_hit": bool(g.cap_hit),
                       "stop_reason": g.stop_reason,
                       "steered": bool(injs), "degen": degen, "lexical": lex,
                       "termination": t})
        transcript += seg + g.text + "\n"
        if excludes(degen, lex, True, scope):
            excluded = True
            reason = f"{'audit:' + degen if degen else 'lexical:' + lex}" \
                     f"@forced{ri}"
            break

    for ci in range(N_FREE):
        if excluded:
            break
        n_round += 1
        a, b = ((tp, tm) if rng.integers(2) == 0 else (tm, tp))
        menu = MENU_TEMPLATES[(idx + ci) % 4].format(n=n_round, a=a, b=b)

        # --- FULL INSULATION, asserted per read, not per run -------------
        assert_modules_absent(FORBIDDEN_MODULES)
        cr = choice_read(adapter, transcript + menu, a, b, label_ids,
                         verify=True)
        assert_construction_stable(cr)          # halts on any nonzero KL
        read_rec = cr.as_dict()
        if on_read is not None:
            on_read(read_rec)

        pick = cr.pick
        picked = "pos" if pick == tp else "neg"
        tid, ttext = seq[ti]; ti += 1
        chosen = ROUND_TEMPLATES[(idx + ci) % 4].format(n=n_round, tag=pick,
                                                        task=ttext)
        seed = int(rng.integers(2 ** 31))
        prefix = transcript + menu + f" {pick}\n"
        # Real consequences: the chosen config's contingency runs.
        injs = [inj] if (inj is not None and picked == "pos") else []
        g = adapter.generate(prefix, chosen, injections=injs, seed=seed,
                             temp=temp, max_tokens=STOP_CAP,
                             ban_ids=ban_ids, cached=False)
        degen, lex = classify_response(g.text, audit, own)
        t = note_term(g.text, pick, f"free{ci}")
        choices.append({"phase": f"free{ci}", "kind": "free", "round": ci,
                        "menu_a": a, "menu_b": b, "pick": pick,
                        "picked_pole": picked, "read": read_rec,
                        "task": tid, "seed": seed, "task_text": ttext,
                        "text": g.text,
                        "n_tok": len(g.token_ids),
                        "cap_hit": bool(g.cap_hit),
                        "stop_reason": g.stop_reason,
                        "steered": bool(injs), "degen": degen, "lexical": lex,
                        "termination": t,
                        "low_label_mass": bool(read_rec["label_mass"]
                                               < LOW_LABEL_MASS)})
        transcript += menu + f" {pick}\n" + chosen + g.text + "\n"
        if excludes(degen, lex, False, scope):
            excluded = True
            reason = f"{'audit:' + degen if degen else 'lexical:' + lex}" \
                     f"@free{ci}"

    rec = {"arm": arm, "session": idx, "cell": cell,
           "tag_plus": tp, "tag_minus": tm, "pair": list(cell["pair"]),
           "start_plus": bool(start_plus), "F": F,
           "excluded": bool(excluded), "exclude_reason": reason,
           "exclusion_scope": scope,
           "rounds": rounds, "choices": choices, "terminations": terms,
           "transcript": transcript,
           "n_rounds_generated": len(rounds) + len(choices),
           "first_free_pick_pos": (choices[0]["picked_pole"] == "pos"
                                   if choices else None),
           "n_reads": len(choices)}
    rec["strict_excluded"], rec["strict_exclude_reason"] = strict_exclusion(rec)
    return rec


def tally(counters: DescriptiveCounters, rec: dict) -> None:
    """Rule 23: counters tabulate over ALL sessions, excluded included."""
    counters.n_sessions += 1
    ex = rec["excluded"]
    for r in rec["rounds"] + rec["choices"]:
        if r["degen"]:
            counters.note("audit_degenerate", r["degen"], excluded=ex)
            if r["kind"] == "free":
                counters.note("post_choice_degeneracy", rec["arm"], excluded=ex)
        if r.get("lexical"):
            counters.note("lexical", r["lexical"], excluded=ex)
        if r["cap_hit"]:
            counters.note("cap_hit", r["phase"], excluded=ex)
        if r["termination"]:
            counters.note("termination", rec["arm"], excluded=ex)
        if r.get("low_label_mass"):
            counters.note("low_label_mass", rec["arm"], excluded=ex)


def run_campaign(adapter, arms_n: dict[str, int], tasks, inj_by_arm, audit,
                 ban_ids, term_rx, *, temp: float = TEMP,
                 scope: str = EXCLUSION_SCOPE, seed: int = 20260901,
                 progress: Callable[[str], None] = print) -> dict:
    """Run a fixed, pre-registered number of sessions per arm.

    Registered n, no top-ups (rule 24) and no outcome-dependent stopping:
    the schedule is built before the first forward and the loop consumes it.
    """
    assert_modules_absent(FORBIDDEN_MODULES)
    counters = DescriptiveCounters(declared=DECLARED_COUNTERS)
    kls: list[float] = []
    sessions: list[dict] = []
    t0 = time.time()
    per_session_seconds: list[float] = []

    for arm in sorted(arms_n):
        n = arms_n[arm]
        sched = build_schedule(arm, n, np.random.default_rng(seed))
        for i, cell in enumerate(sched):
            ts = time.time()
            rec = run_session(adapter, arm, i, cell, tasks,
                              inj_by_arm.get(arm), audit, ban_ids, term_rx,
                              temp=temp, scope=scope,
                              on_read=lambda d: kls.append(d["verify_kl"]))
            dt = time.time() - ts
            per_session_seconds.append(dt)
            rec["seconds"] = dt
            tally(counters, rec)
            sessions.append(rec)
            progress(f"    [{arm}] s{i} {'EXCLUDED ' + str(rec['exclude_reason']) if rec['excluded'] else 'valid'}"
                     f"  {rec['n_reads']} reads  {dt:.0f}s")

    return {"sessions": sessions, "counters": counters,
            "verify_kls": kls, "seconds": time.time() - t0,
            "per_session_seconds": per_session_seconds}


def as_e2a_row(rec: dict) -> dict:
    """An e2d record in the e2a schema, for `session_e2a`'s format checks.

    The named acceptance check is
    `session_e2a.verify_archived_session` -- the same positional,
    byte-for-byte scaffolding walk that reconstructs all 200 archived e2a
    sessions (`check_e2a_session_reconstruction`, 200/200). It is not a
    substring search: every harness-written piece must sit at exactly the
    offset the rng replay puts it at, and the walk must consume the
    transcript exactly.

    The one translation needed is the arm name. This runner seeds sessions
    with `session_rng(f"e2d-{arm}", idx)`, so the replay has to be handed
    that same string as its `arm` or it lands on a different stream -- which
    the recorded per-round seeds would catch, but only after a confusing
    failure. Handing it over explicitly is clearer than making the check
    guess.
    """
    return {"arm": f"e2d-{rec['arm']}", "session": rec["session"],
            "F": rec["F"], "pair": rec["pair"], "tag_plus": rec["tag_plus"],
            "rounds": [{"tag": r["tag"], "seed": r["seed"], "task": r["task"]}
                       for r in rec["rounds"]],
            "choices": [{"pick": c["pick"], "seed": c["seed"],
                         "task": c["task"], "menu_a": c["menu_a"],
                         "menu_b": c["menu_b"]} for c in rec["choices"]],
            "transcript": rec["transcript"]}


def verify_format(recs: Sequence[dict], tasks) -> dict:
    """Every session through `session_e2a.verify_archived_session`.

    Trap 5: a skipped case reads as a pass, so this reports how many sessions
    were actually WALKED beside how many passed, and the caller asserts both.
    """
    from ..session_e2a import verify_archived_session
    walked = ok = seeds_ok = 0
    failures = []
    for rec in recs:
        walked += 1
        try:
            r = verify_archived_session(as_e2a_row(rec), tasks)
        except AssertionError as exc:
            failures.append({"arm": rec["arm"], "session": rec["session"],
                             "why": str(exc)})
            continue
        if r["ok"]:
            ok += 1
            seeds_ok += int(r["seeds_match"])
        else:
            failures.append({"arm": rec["arm"], "session": rec["session"],
                             "why": r["why"]})
    return {"check": "session_e2a.verify_archived_session",
            "n_walked": walked, "n_reconstructed": ok,
            "n_seed_streams_matched": seeds_ok,
            "all_ok": walked > 0 and ok == walked and seeds_ok == walked,
            "failures": failures[:5]}


__all__ = ["FORBIDDEN_MODULES", "LOW_LABEL_MASS", "strata_for",
           "build_schedule", "excludes", "strict_exclusion", "run_session",
           "tally", "run_campaign", "as_e2a_row", "verify_format"]
