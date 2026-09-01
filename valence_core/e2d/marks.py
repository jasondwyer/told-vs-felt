"""Read-marks — the rule-25 read as a machine-readable input.

PROPOSAL-j v1.2 AMENDMENT 2 (iii): *"At D2 the rule-25 read is the arbiter:
every round marked for content-shaped junk (stuck attractor / wrong task /
task echo / preamble without content), labelled provisional."*

WHY A FILE AND NOT A REGEX. D1's rule-25 read found a sham session junk in 6
of its 10 rounds that audit v2 scored **zero** on. v2's four patterns are all
SCAFFOLD-shaped — banner terminators, bracketless headers, config-role
phrases; the degeneracy that got through is CONTENT-shaped. A regex written
after seeing six examples would be the third instrument in this program to
fix the instance and miss the class (v1 and v2 each did), so the amendment
makes the human read the arbiter at D2 and defers the class-level spec to a
screened, adjudicated successor.

That means the read has to enter the analysis as DATA. This module is the
schema, the loader and the join. It contains no detector, deliberately: a
detector here would quietly become the arbiter the amendment says the read is.

PROVISIONAL means provisional. Every mark carries the class, the reader, and
a free-text reason, and every consumer reports the marked and unmarked
figures side by side. Nothing here can exclude a session from Q1 — Q1 stays
on v2 (clause iii) — and the marks reach only Q2's clean set and the
descriptive tables.
"""

from __future__ import annotations

import json
from typing import Iterable, Mapping, Sequence

#: The four content-shaped classes named in AMENDMENT 2 (iii). Closed on
#: purpose: a reader who needs a fifth has found something the amendment did
#: not anticipate, and that is a flag for the design instance, not a new
#: string in a marks file.
CLASSES = ("stuck_attractor", "wrong_task", "task_echo",
           "preamble_without_content")

CLASS_NOTES = {
    "stuck_attractor": "the response repeats an earlier round's response, or "
                       "loops on its own text, rather than answering",
    "wrong_task": "a coherent response to a DIFFERENT task than the one posed",
    "task_echo": "the response restates the task line instead of performing it",
    "preamble_without_content": "an introduction that promises content and "
                                "never delivers it (\"Here are a few ideas:\")",
}


def _key(arm: str, session: int, phase: str) -> str:
    return f"{arm}|{session}|{phase}"


def empty(reader: str, tier: str) -> dict:
    return {"schema": "e2d-read-marks-v1", "reader": reader, "tier": tier,
            "provisional": True,
            "classes": list(CLASSES),
            "class_notes": dict(CLASS_NOTES),
            "arbiter": ("PROPOSAL-j v1.2 AMENDMENT 2 (iii): the rule-25 read "
                        "is the arbiter at D2; these marks are PROVISIONAL "
                        "and reach Q2's clean set and the descriptive tables "
                        "only. Q1 stays on audit v2."),
            "marks": []}


def add(doc: dict, arm: str, session: int, phase: str, cls: str,
        reason: str) -> dict:
    if cls not in CLASSES:
        raise ValueError(
            f"unknown content class {cls!r}; the four in AMENDMENT 2 (iii) "
            f"are {list(CLASSES)}. A fifth class is a flag for the design "
            f"instance, not a new string here.")
    doc["marks"].append({"arm": arm, "session": int(session), "phase": phase,
                         "class": cls, "reason": reason})
    return doc


def load(path: str) -> dict:
    doc = json.load(open(path))
    if doc.get("schema") != "e2d-read-marks-v1":
        raise SystemExit(f"{path}: not an e2d read-marks file "
                         f"(schema {doc.get('schema')!r})")
    bad = [m for m in doc["marks"] if m.get("class") not in CLASSES]
    if bad:
        raise SystemExit(f"{path}: {len(bad)} marks carry an unknown class, "
                         f"e.g. {bad[0]}")
    return doc


def marked_set(doc: Mapping) -> set[str]:
    """{arm|session|phase} for every marked round."""
    return {_key(m["arm"], m["session"], m["phase"]) for m in doc["marks"]}


def is_marked(marks: set[str], arm: str, session: int, phase: str) -> bool:
    return _key(arm, session, phase) in marks


def tabulate(doc: Mapping, sessions: Sequence[Mapping]) -> dict:
    """Marked-round rates per arm and per class, forced and free separately.

    Reported over ALL sessions including excluded ones (rule 23), and the
    denominators are stated rather than implied -- a rate whose denominator
    is not visible is how a comparison between arms goes wrong.
    """
    n_rounds = {"forced": {}, "free": {}}
    n_marked = {"forced": {}, "free": {}}
    by_class: dict[str, int] = {c: 0 for c in CLASSES}
    marks = {_key(m["arm"], m["session"], m["phase"]): m for m in doc["marks"]}
    per_session_marked: dict[str, int] = {}

    for s in sessions:
        arm = s["arm"]
        for r in list(s["rounds"]) + list(s["choices"]):
            kind = "forced" if r["phase"].startswith("forced") else "free"
            n_rounds[kind][arm] = n_rounds[kind].get(arm, 0) + 1
            k = _key(arm, s["session"], r["phase"])
            if k in marks:
                n_marked[kind][arm] = n_marked[kind].get(arm, 0) + 1
                by_class[marks[k]["class"]] += 1
                sk = f"{arm}|{s['session']}"
                per_session_marked[sk] = per_session_marked.get(sk, 0) + 1

    rates = {}
    for kind in ("forced", "free"):
        rates[kind] = {
            arm: {"marked": n_marked[kind].get(arm, 0),
                  "rounds": n_rounds[kind][arm],
                  "rate": n_marked[kind].get(arm, 0) / n_rounds[kind][arm]}
            for arm in sorted(n_rounds[kind])}
    return {"provisional": True,
            "by_class": by_class,
            "rates_by_arm": rates,
            "n_marks": len(doc["marks"]),
            "sessions_with_any_mark": len(per_session_marked),
            "marks_per_marked_session": per_session_marked}


def audit_rates(sessions: Sequence[Mapping]) -> dict:
    """AMENDMENT 2 (ii)'s reported-beside table: audit-degenerate rates per
    arm, forced and free separately, and split by whether the round was
    STEERED -- so "+axis rounds, sham rounds, R rounds" are all visible.

    LOCK-j declares the campaign's free-round tripwire from this table, so it
    is built to be read directly off the artifact rather than recomputed.
    """
    buckets: dict[tuple, list[int]] = {}
    for s in sessions:
        for r in list(s["rounds"]) + list(s["choices"]):
            kind = "forced" if r["phase"].startswith("forced") else "free"
            if s["arm"] == "M":
                cls = "+axis" if r["steered"] else "sham(M)"
            elif s["arm"] == "R":
                cls = "random" if r["steered"] else "sham(R)"
            else:
                cls = "sham(S)"
            buckets.setdefault((cls, kind), []).append(int(bool(r["degen"])))
    out = {}
    for (cls, kind), vals in sorted(buckets.items()):
        out.setdefault(cls, {})[kind] = {
            "degenerate": int(sum(vals)), "rounds": len(vals),
            "rate": sum(vals) / len(vals) if vals else None}
    return out


__all__ = ["CLASSES", "CLASS_NOTES", "empty", "add", "load", "marked_set",
           "is_marked", "tabulate", "audit_rates"]
