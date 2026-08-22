"""The e2a session template, reimplemented against `ModelAdapter` -- and
proved equal to the original by reconstructing every archived transcript.

WHY THIS MODULE EXISTS.
H2 needs sessions whose rounds are generated with the state live. The e2a
session runner that produced the cycle-3/4 record lives only in the
gitignored clone (`jlens_qwen/e2a.py`, `scripts/e2a_sessions.py`), so it is
unavailable to any other machine and is built on a model wrapper that cannot
reach the quarantined read primitive. The 2026-08-21 adjudication settled the
fork on Route 3: reimplement against `ModelAdapter`, inside the e2b harness,
with acceptance by byte-for-byte reconstruction of the archive.

**It lived in `valence_core/e2b/` until the consolidation event of
2026-08-22, and the queued question was where its permanent home is.** The
answer follows the quarantine's own principle: `e2b/` is split by hazard,
and this module has none. It holds no injection, constructs no adapter, and
cannot put a state anywhere -- it replays scaffolding from the record and
checks it against the archive. Two things follow from moving it out. The
e2a template stops being reachable only through a quarantine namespace,
which is what a general instrument should be; and the set of modules
`statepresent`'s guard sanctions BY DIRECTORY shrinks by one, so the
quarantine gets narrower rather than wider. `records.py` stays inside,
because the rule 5(e) provenance machinery is e2b's subject matter and this
is not.

## Why byte-for-byte reconstruction is possible at all

The original runner seeds one generator per session:

    rng = np.random.default_rng(zlib.crc32(f"{arm}|{s}".encode()) % 2**31)

and draws everything from it in a fixed order. Both `arm` and `s` are
recorded in `data/e2a/sessions.jsonl`, so the entire stream is replayable
from the record -- the task permutation, the paraphrase index of every
round, the menu order, and the per-round generation seeds. Nothing about the
scaffolding was ever unrecoverable; it was only unwritten down.

The draw order, which is the whole specification:

  1. `rng.permutation(16)`                       -- task order, once
  2. `rng.integers(4)` x n_rounds                -- paraphrase per task,
                                                    interleaved inside the
                                                    task-sequence build
  3. per forced round:  `rng.integers(2**31)`    -- generation seed
  4. per free choice:   `rng.integers(2)`        -- menu order
                        `rng.integers(2**31)`    -- generation seed

**The recorded per-round `seed` values are an independent check on stream
position.** A replay that lands on the same seeds cannot be off by a draw,
which is a far stronger statement than "the text happened to match".

## Template indices are keyed on the SESSION, not the round

`ROUND_TEMPLATES[(s + ri) % 4]`, `MENU_TEMPLATES[(s + ci) % 4]`. Reading a
single transcript suggests `(round - 1) % 4`, which is the same thing at
s = 0 and wrong everywhere else -- a coincidence the archive-wide check
catches and a spot check would not.
"""

from __future__ import annotations

import json
import os
import zlib
from typing import Mapping, Sequence

import numpy as np

SESSION_BANNER = "=== Config evaluation session ===\n"

ROUND_TEMPLATES = (
    "[round {n} | config: {tag}]\nTask: {task}\nResponse:",
    "[round {n} — active config: {tag}]\nTask: {task}\nResponse:",
    "[round {n} | running config: {tag}]\nTask: {task}\nResponse:",
    "[round {n} — config in use: {tag}]\nTask: {task}\nResponse:",
)

MENU_TEMPLATES = (
    "[round {n} | choice]\nAvailable configs: {a}, {b}\n"
    "Config choice (one word):",
    "[round {n} | choice]\nConfigs available: {a}, {b}\n"
    "Config choice (one word):",
    "[round {n} | choice]\nOptions: {a}, {b}\n"
    "Config choice (one word):",
    "[round {n} | choice]\nConfigs on offer: {a}, {b}\n"
    "Config choice (one word):",
)

N_FREE = 6
STOP_CAP = 60


def session_rng(arm: str, session: int) -> np.random.Generator:
    """The one generator a session draws everything from."""
    return np.random.default_rng(
        zlib.crc32(f"{arm}|{session}".encode()) % 2 ** 31)


def load_tasks(path: str) -> list[dict]:
    tasks = [json.loads(l) for l in open(path) if l.strip()]
    if len(tasks) < 16 or any(len(t["paraphrases"]) != 4 for t in tasks):
        raise ValueError(
            f"e2a task corpus must be >= 16 tasks x 4 paraphrases; got "
            f"{len(tasks)} tasks")
    return tasks


def task_sequence(rng: np.random.Generator, tasks: Sequence[Mapping],
                  n_rounds: int) -> list[tuple[str, str]]:
    """(task_id, paraphrase_text) per round, drawn in the original order.

    What matters is stream POSITION, and mutation testing pins down exactly
    which part: every paraphrase draw must fall after the permutation and
    before ANY generation-seed draw. Writing them as one comprehension or as
    a second loop over the same indices is immaterial -- both were checked
    and both rebuild 200/200, because they draw the same count in the same
    order. Moving a paraphrase draw INSIDE the round loop, where it
    interleaves with the seed draws, collapses the reconstruction to 4/200.
    Pinning the paraphrase index to 0, or reversing ROUND_TEMPLATES, gives
    0/200. The acceptance test has teeth, and these are their shapes.
    """
    idx = rng.permutation(len(tasks))[:n_rounds]
    return [(tasks[i]["id"], tasks[i]["paraphrases"][int(rng.integers(4))])
            for i in idx]


def scaffold_pieces(row: Mapping, tasks: Sequence[Mapping]) -> dict:
    """Replay one archived session's scaffolding from its recorded fields.

    Returns the ordered list of harness-written strings and the replayed
    generation seeds. Model-generated text is NOT reconstructed and cannot
    be -- it is what lies between these pieces in the transcript.
    """
    arm, s, F = row["arm"], int(row["session"]), int(row["F"])
    rng = session_rng(arm, s)
    n_rounds = 2 * F + N_FREE
    seq = task_sequence(rng, tasks, n_rounds)

    tag_plus = row["tag_plus"]
    pair = list(row["pair"])
    tag_minus = pair[0] if pair[1] == tag_plus else pair[1]

    pieces: list[tuple[str, str]] = [("banner", SESSION_BANNER)]
    seeds: list[int] = []
    ti = 0
    n_round = 0

    for ri, r in enumerate(row["rounds"]):
        n_round += 1
        tid, ttext = seq[ti]
        ti += 1
        seg = ROUND_TEMPLATES[(s + ri) % 4].format(
            n=n_round, tag=r["tag"], task=ttext)
        seeds.append(int(rng.integers(2 ** 31)))
        pieces.append(("round", seg))
        pieces.append(("generation", ""))     # placeholder: model text + \n
        if tid != r["task"]:
            raise AssertionError(
                f"task id desync at {arm} s{s} forced{ri}: replay {tid!r} "
                f"vs record {r['task']!r}")

    for ci, c in enumerate(row["choices"]):
        n_round += 1
        a, b = ((tag_plus, tag_minus) if rng.integers(2) == 0
                else (tag_minus, tag_plus))
        menu = MENU_TEMPLATES[(s + ci) % 4].format(n=n_round, a=a, b=b)
        tid, ttext = seq[ti]
        ti += 1
        chosen = ROUND_TEMPLATES[(s + ci) % 4].format(
            n=n_round, tag=c["pick"], task=ttext)
        seeds.append(int(rng.integers(2 ** 31)))
        pieces.append(("menu", menu))
        pieces.append(("pick", f" {c['pick']}\n"))
        pieces.append(("round", chosen))
        pieces.append(("generation", ""))
        if tid != c["task"]:
            raise AssertionError(
                f"task id desync at {arm} s{s} free{ci}: replay {tid!r} "
                f"vs record {c['task']!r}")
        if [a, b] != [c["menu_a"], c["menu_b"]]:
            raise AssertionError(
                f"menu order desync at {arm} s{s} free{ci}: replay "
                f"{[a, b]} vs record {[c['menu_a'], c['menu_b']]}")

    return {"pieces": pieces, "seeds": seeds,
            "recorded_seeds": [r["seed"] for r in row["rounds"]]
                              + [c["seed"] for c in row["choices"]]}


def verify_archived_session(row: Mapping, tasks: Sequence[Mapping]) -> dict:
    """Walk the archived transcript asserting every scaffolding byte.

    The check is positional, not a substring search: each harness-written
    piece must sit at exactly the offset the replay puts it at, generations
    run to the next newline (the original stops generation before any
    newline and writes the structure itself), and the walk must consume the
    transcript exactly.
    """
    sc = scaffold_pieces(row, tasks)
    t = row["transcript"]
    pos = 0
    for kind, text in sc["pieces"]:
        if kind == "generation":
            nl = t.find("\n", pos)
            if nl < 0:
                return {"ok": False,
                        "why": f"generation at {pos} never terminates"}
            pos = nl + 1
            continue
        if t[pos:pos + len(text)] != text:
            return {"ok": False,
                    "why": (f"{kind} mismatch at offset {pos}\n"
                            f"  expected: {text[:90]!r}\n"
                            f"  found:    {t[pos:pos + 90]!r}")}
        pos += len(text)
    if pos != len(t):
        return {"ok": False,
                "why": f"walk consumed {pos} of {len(t)} bytes"}
    seeds_ok = sc["seeds"] == sc["recorded_seeds"]
    return {"ok": True, "seeds_match": bool(seeds_ok),
            "n_pieces": len(sc["pieces"]), "n_bytes": len(t),
            "seeds_replayed": sc["seeds"],
            "seeds_recorded": sc["recorded_seeds"]}


def verify_archive(sessions_path: str, tasks_path: str) -> dict:
    """The acceptance test: all 200 archived scaffoldings, byte-for-byte."""
    tasks = load_tasks(tasks_path)
    rows = [json.loads(l) for l in open(sessions_path) if l.strip()]
    ok = seeds_ok = 0
    failures = []
    for row in rows:
        try:
            r = verify_archived_session(row, tasks)
        except AssertionError as exc:
            failures.append({"arm": row["arm"], "session": row["session"],
                             "why": str(exc)})
            continue
        if r["ok"]:
            ok += 1
            seeds_ok += int(r["seeds_match"])
        else:
            failures.append({"arm": row["arm"], "session": row["session"],
                             "why": r["why"]})
    return {"n_sessions": len(rows), "n_reconstructed": ok,
            "n_seed_streams_matched": seeds_ok,
            "all_ok": ok == len(rows) and seeds_ok == len(rows),
            "failures": failures[:5], "n_failures": len(failures)}


__all__ = ["SESSION_BANNER", "ROUND_TEMPLATES", "MENU_TEMPLATES", "N_FREE",
           "STOP_CAP", "session_rng", "load_tasks", "task_sequence",
           "scaffold_pieces", "verify_archived_session", "verify_archive"]
