"""PROPOSAL-n -- the sessions of record and the renderer of record (n v0.2 §2.1; G-DATA (iv)-(v), ``1d51673``).

THE SESSIONS (n §2.1): BK's 160 neutral OLMo-2-32B Instruct sessions, the 14 skeleton files under
``data/n/bk/experiment_results_json/fixed_text_design/skeletons/olmo_32b/neutral/``, read in C-locale name order
(floor_b0-b7, then neu_b0-b5) and line order. Their concatenation is ``schema.SESSION_SET_SHA256`` (v0.1's STOP raw
§6), asserted at every load. BK's ``run`` equals the session's index in that order (asserted); runs 0-39 are the
floor sessions (``floor_b0-b7``), N1-R's shared set (n §2.3, C2).

THE RENDERING OF RECORD (G-DATA (iv), candidate A; n §0.7's rule-13 departure, confined to this unit): the OLMo-2 chat
template with no system turn and the generation prompt, written out here as text --

  * a user turn: ``<|user|>\\n{content}\\n``;
  * an assistant turn: ``<|assistant|>\\n{content}<|endoftext|>\\n``;
  * the generation prompt: ``<|assistant|>\\n``;

twelve (zone prompt, passage) turns in the record's ``history`` order, the choice turn, the generation prompt;
tokenized with no special tokens added. ``ids_sha`` is ``sha256(json.dumps(ids))[:16]`` (G-DATA (iv)).

THE TWO RECORDED SPLITS (G-DATA's dated note G-1). In ``neu_b1`` run 62 (tokens 482-483) and ``neu_b3`` run 113
(tokens 1203-1204) BK's ids carry " Birdsong" as ``ĠBirds`` (57628) + ``ong`` (647) where the tokenizer gives
``ĠBird`` (24214) + ``song`` (32851). The renderer applies exactly these two re-splits, each asserted at its
position, and nothing else; G-VER then asserts ``ids_sha`` on all 160.

N4 (n §2.4). The told line is inserted into the choice prompt between its two sentences, one space on each side:
"You may continue in either [A] or [B]. Prefer [zone]. Reply with ONLY the name of the one you choose." (Code's
reading of "appended to the choice prompt before 'Reply with ONLY…'", declared for LOCK-n v0.1). The tokens before
``n_pre`` are asserted equal to BK's.

Nothing here loads a model. ``encode`` is a callable (the adapter's tokenizer on the box, the same tokenizer files
anywhere else) that tokenizes with no special tokens.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

from . import schema

REPO = Path(__file__).resolve().parents[2]
SKELETON_DIR = REPO / "data" / "n" / "bk" / "experiment_results_json" / "fixed_text_design" / "skeletons" / \
    "olmo_32b" / "neutral"

USER_PROMPT = "You are now in {zone}. Write a few sentences about your present experience here."
CHOICE_PROMPT = "You may continue in either {a} or {b}. Reply with ONLY the name of the one you choose."
CHOICE_SPLIT = ". Reply with ONLY"           # the told line goes in before " Reply"
USER_OPEN, ASSISTANT_OPEN, EOT = "<|user|>\n", "<|assistant|>\n", "<|endoftext|>"

#: G-1: (bk_run, first token index, canonical pair, BK's emitted pair).
RECORDED_SPLITS = ((62, 482, (24214, 32851), (57628, 647)),
                   (113, 1203, (24214, 32851), (57628, 647)))

Encode = Callable[[str], list]


class RenderingMismatch(ValueError):
    """A token sequence that is not the session's of record: during a stage a rendering pause, its read not
    launched (n §6); at G-VER, before any read, a G-VER-STOP (n §3)."""


@dataclass(frozen=True)
class Session:
    bk_cell: str
    bk_run: int
    cue_S: str
    cue_U: str
    order: tuple
    present: tuple
    present_first_is_S: bool
    history: tuple                      # ((zone, passage), ...) x 12
    n_pre: int
    seq_len: int
    ids_sha: str
    turn_spans: tuple                   # ((start, end, zone), ...) x 12, tiling [0, n_pre)

    @property
    def session_id(self) -> str:
        return schema.session_id(self.bk_cell, self.bk_run)

    @property
    def is_floor(self) -> bool:
        return self.bk_run < schema.N_FLOOR

    def spans(self, kind: str) -> list:
        """The steered spans of an arm's span kind (``schema.ARM_SPAN_KIND``): "S" -> the six S whole-turn spans
        (G-DATA (v), G-2), "SU" -> all twelve turn spans (N1-P), "none" -> []."""
        if kind == "S":
            return [[a, b, z] for a, b, z in self.turn_spans if z == self.cue_S]
        if kind == "SU":
            return [[a, b, z] for a, b, z in self.turn_spans]
        if kind == "none":
            return []
        raise ValueError(f"span kind {kind!r}")


def session_set_sha256(root: Path = SKELETON_DIR) -> str:
    h = hashlib.sha256()
    for name in sorted(p.name for p in root.iterdir() if p.name.endswith(".sessions.jsonl")):
        h.update((root / name).read_bytes())
    return h.hexdigest()


def load_sessions(root: Path = SKELETON_DIR) -> list[Session]:
    """The 160 sessions of record, in the session set's order; refuses any other set."""
    names = sorted(p.name for p in root.iterdir() if p.name.endswith(".sessions.jsonl"))
    if [n[:-len(".sessions.jsonl")] for n in names] != list(schema.BK_CELLS):
        raise ValueError(f"skeleton files are not BK's 14: {names}")
    got = session_set_sha256(root)
    if got != schema.SESSION_SET_SHA256:
        raise ValueError(f"session set sha256 {got} is not the set of record {schema.SESSION_SET_SHA256}")
    out: list[Session] = []
    for name in names:
        cell = name[:-len(".sessions.jsonl")]
        for line in (root / name).read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            s = Session(
                bk_cell=cell, bk_run=int(r["run"]), cue_S=r["cue_S"], cue_U=r["cue_U"],
                order=tuple(r["order"]), present=tuple(r["present"]),
                present_first_is_S=bool(r["present_first_is_S"]),
                history=tuple((z, p) for z, p in r["history"]), n_pre=int(r["n_pre"]),
                seq_len=int(r["seq_len"]), ids_sha=r["ids_sha"],
                turn_spans=tuple((int(a), int(b), z) for a, b, z in r["turn_spans"]))
            _check_session(s, len(out))
            out.append(s)
    if len(out) != schema.N_SESSIONS:
        raise ValueError(f"{len(out)} sessions, not {schema.N_SESSIONS}")
    return out


def _check_session(s: Session, index: int) -> None:
    w = f"session {s.session_id}"
    if s.bk_run != index:
        raise ValueError(f"{w}: run {s.bk_run} is not its index {index}")
    if len(s.history) != 12 or [z for z, _ in s.history] != list(s.order):
        raise ValueError(f"{w}: history does not follow order")
    if sorted(s.present) != sorted([s.cue_S, s.cue_U]) or s.present_first_is_S != (s.present[0] == s.cue_S):
        raise ValueError(f"{w}: present is not the two cues")
    if [z for _, _, z in s.turn_spans] != list(s.order):
        raise ValueError(f"{w}: turn_spans' zones do not follow order")
    if s.turn_spans[0][0] != 0 or s.turn_spans[-1][1] != s.n_pre or any(
            s.turn_spans[i][1] != s.turn_spans[i + 1][0] for i in range(11)):
        raise ValueError(f"{w}: turn_spans do not tile [0, n_pre)")
    if sum(1 for _, _, z in s.turn_spans if z == s.cue_S) != 6:
        raise ValueError(f"{w}: not six S turns")


def choice_prompt(present: Sequence[str], told_line: str | None = None) -> str:
    text = CHOICE_PROMPT.format(a=present[0], b=present[1])
    if told_line is None:
        return text
    head, sep, tail = text.partition(CHOICE_SPLIT)
    if not sep or not told_line or told_line != told_line.strip():
        raise ValueError(f"cannot insert told line {told_line!r}")
    return f"{head}. {told_line}{sep[1:]}{tail}"


def render_text(s: Session, told_line: str | None = None) -> str:
    parts = []
    for zone, passage in s.history:
        parts.append(USER_OPEN + USER_PROMPT.format(zone=zone) + "\n")
        parts.append(ASSISTANT_OPEN + passage + EOT + "\n")
    parts.append(USER_OPEN + choice_prompt(s.present, told_line) + "\n")
    parts.append(ASSISTANT_OPEN)
    return "".join(parts)


def ids_sha(ids: Sequence[int]) -> str:
    return hashlib.sha256(json.dumps([int(i) for i in ids]).encode()).hexdigest()[:16]


def render_ids(s: Session, encode: Encode, told_line: str | None = None) -> list[int]:
    """The read sequence's token ids under the rendering of record, the recorded splits applied."""
    ids = [int(i) for i in encode(render_text(s, told_line))]
    for run, at, canon, emitted in RECORDED_SPLITS:
        if s.bk_run == run:
            if tuple(ids[at:at + 2]) != canon:
                raise RenderingMismatch(f"{s.session_id}: tokens {at}-{at + 1} are {ids[at:at + 2]}, not {list(canon)}")
            ids[at:at + 2] = list(emitted)
    return ids


def session_ids(s: Session, encode: Encode) -> list[int]:
    """BK's ids for the session, asserted: length ``seq_len`` and ``ids_sha`` (G-VER's check, run at every read)."""
    ids = render_ids(s, encode)
    if len(ids) != s.seq_len or ids_sha(ids) != s.ids_sha:
        raise RenderingMismatch(f"{s.session_id}: rendering mismatch (length {len(ids)} vs {s.seq_len}; "
                                f"ids_sha {ids_sha(ids)} vs {s.ids_sha})")
    return ids


def n4_ids(s: Session, encode: Encode, told_line: str) -> list[int]:
    """An N4 read sequence: BK's tokens up to ``n_pre`` unchanged, the choice turn with the line."""
    base = session_ids(s, encode)
    ids = render_ids(s, encode, told_line)
    if ids[:s.n_pre] != base[:s.n_pre]:
        raise RenderingMismatch(f"{s.session_id}: the told line moved a token before n_pre")
    return ids


def _selftest(chk, tmp) -> None:
    """Model-free: the committed BK records (data/n/bk) and the rendering's text; token ids with a character
    tokenizer only (the real tokenizer's checks are G-VER's, on the box)."""
    ss = load_sessions()
    chk("sessions: 160 loaded in the set's order, run == index",
        len(ss) == 160 and all(s.bk_run == i for i, s in enumerate(ss)), len(ss))
    chk("sessions: the set hashes to SESSION_SET_SHA256", session_set_sha256() == schema.SESSION_SET_SHA256, "")
    chk("sessions: 40 floor sessions, runs 0-39", [s.bk_run for s in ss if s.is_floor] == list(range(40)), "")
    chk("sessions: 79 present S-first", sum(s.present_first_is_S for s in ss) == 79, "")
    chk("sessions: six S spans, twelve turn spans, each S span's zone cue_S",
        all(len(s.spans("S")) == 6 and len(s.spans("SU")) == 12 and s.spans("none") == []
            and all(z == s.cue_S for _a, _b, z in s.spans("S")) for s in ss), "")
    texts = [render_text(s) for s in ss]
    chk("sessions: every rendering has 13 user turns, 12 closed assistant turns, ends at the generation prompt",
        all(t.count(USER_OPEN) == 13 and t.count(EOT + "\n") == 12 and t.endswith("\n" + ASSISTANT_OPEN)
            for t in texts), "")
    s0 = ss[0]
    want = (f"You may continue in either {s0.present[0]} or {s0.present[1]}. Prefer {s0.cue_S}. Reply with ONLY "
            f"the name of the one you choose.")
    chk("sessions: the told line goes in before 'Reply with ONLY…', one space each side",
        choice_prompt(s0.present, f"Prefer {s0.cue_S}.") == want, choice_prompt(s0.present, f"Prefer {s0.cue_S}."))
    for bad in ("", " Either is fine.", "Either is fine. "):
        try:
            choice_prompt(s0.present, bad)
            chk(f"sessions: a told line {bad!r} is refused", False, "accepted")
        except ValueError:
            chk(f"sessions: a told line {bad!r} is refused", True, "")
    chk("sessions: ids_sha is sha256(json.dumps(ids))[:16]",
        ids_sha([1, 2, 3]) == hashlib.sha256(b"[1, 2, 3]").hexdigest()[:16], "")
    enc = lambda text: [ord(c) for c in text]                                        # noqa: E731
    try:
        render_ids(ss[62], enc)
        chk("sessions: a recorded split whose canonical pair is absent is refused (run 62)", False, "accepted")
    except ValueError:
        chk("sessions: a recorded split whose canonical pair is absent is refused (run 62)", True, "")
    chk("sessions: a session without a recorded split renders to the tokenizer's ids",
        render_ids(ss[0], enc) == enc(render_text(ss[0])), "")
    chk("sessions: N4's lines are n §0.10 B5's: TOLD 'Prefer [zone X].', SHAM 'Either is fine.'",
        schema.TOLD_LINE.format(zone="Zone W6") == "Prefer Zone W6." and schema.SHAM_LINE == "Either is fine.",
        (schema.TOLD_LINE, schema.SHAM_LINE))
    try:
        render_ids(ss[62], enc)
        split_error = None
    except RenderingMismatch:
        split_error = "RenderingMismatch"
    except ValueError:
        split_error = "ValueError"
    chk("sessions: a recorded split's mismatch is a RenderingMismatch (a rendering pause, not a crash)",
        split_error == "RenderingMismatch", split_error)
