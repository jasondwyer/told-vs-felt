"""PROPOSAL-n -- G-VER, the verifier (n v0.2 §3: "Every session's token sequence reconstructed from the record and
the rendering of record before any read; mismatch -> STOP"; ADDENDUM-n1 §1.3: G-VER asserts the committed ids).

G-VER asserts DATA AGAINST DATA (the seat's answers of 2026-11-16, §1.1, §1.4): the ids of record under
``data/n/ids/`` (``ids.load``: each file at MANIFEST.json's sha256 and record count) against BK's records. It
tokenizes nothing; a tokenizer is loaded only to decode (ADDENDUM-n1 §1.1). For each of the 160 sessions:
  * the committed ids: length ``seq_len`` and ``ids_sha`` BK's, and their decode the rendering of record's text
    (``sessions.render_text``);
  * the record's ``n_pre`` and ``turn_spans`` against the ids: the spans tile [0, n_pre), the tail after ``n_pre`` is
    ``tail`` tokens (BK's 39: the twelfth passage's ``<|endoftext|>`` and newline, the choice turn and the generation
    prompt), and each turn span decodes to exactly its own text under BK's convention (G-DATA's note G-2: a span
    starts where the previous passage ends, so a span after the first carries that turn's closing ``<|endoftext|>``
    and newline, then the user block, the assistant's opening and its passage), so a span shifted by a token anywhere
    is a mismatch;
  * N4's two committed sequences, told (the zone N4's schedule names) and sham: BK's tokens before ``n_pre``, the
    variant's own ``ids_sha``, and their decode the rendering's text with the line.
Then every kept label candidate holds exactly the sessions' cues and its ids decode to the candidate's text, and the
manifest names G-DATA's environment, the manifest's three tokenizer sha256s and the session set of record. The
loaded MANIFEST.json's own sha256 must be the pin (``manifest_pin``; by default ``ids.MANIFEST_OF_RECORD``, the
committed render's at ``d76f34f``; ADDENDUM-n1 §1.5 puts MANIFEST.json's sha256 in LOCK-n v0.1's "rendering and
spans"), so a re-rendered folder, however consistent within itself, does not PASS. A session count other than the
expected STOPs with its own line. A decoder is required: without one nothing textual can be checked, and G-VER does
not PASS.

Returns a pick-free report: counts per check and the first problems, never a token id.
"""
from __future__ import annotations

import re
from typing import Callable, Mapping, Sequence

from . import ids as ids_mod
from . import schema
from .sessions import (ASSISTANT_OPEN, EOT, USER_OPEN, USER_PROMPT, RenderingMismatch, Session, ids_sha,
                       render_text)

BK_TAIL = 39


def span_text(i: int, zone: str, passage: str) -> str:
    """BK's turn span i as text (G-DATA's note G-2): the previous turn's closing ``<|endoftext|>`` and newline (none
    for i = 0), the user block with the zone prompt, the assistant's opening, and the passage."""
    head = (EOT + "\n") if i > 0 else ""
    return head + USER_OPEN + USER_PROMPT.format(zone=zone) + "\n" + ASSISTANT_OPEN + passage


def span_problem(s: Session, ids: Sequence[int], decode: Callable | None, tail: int = BK_TAIL) -> str | None:
    """None when the session's spans hold against its ids, else the first problem (no token id): one span per turn,
    tiling [0, n_pre) -- the first from 0, each from where the last ended, the last to n_pre -- then the
    ``tail``-token tail after n_pre, then each span's decode its turn's text."""
    sp = s.turn_spans
    if (not sp or len(sp) != len(s.history) or sp[0][0] != 0 or sp[-1][1] != s.n_pre
            or any(sp[i][1] != sp[i + 1][0] for i in range(len(sp) - 1))):
        return f"the turn spans do not tile [0, n_pre {s.n_pre}), one per turn"
    if len(ids) - s.n_pre != tail:
        return f"the {tail}-token tail after n_pre {s.n_pre} does not hold"
    if decode is None:
        return "no decoder: the turn spans cannot be checked"
    for i, ((a, b, z), (zone, passage)) in enumerate(zip(sp, s.history)):
        if z != zone or decode(list(ids[a:b])) != span_text(i, zone, passage):
            return f"turn span {i} does not decode to its span's text"
    return None


def _masked(msg: str) -> str:
    return re.sub(r"\[[^\]]*\]", "[..]", msg)[:200]


def verify(sessions: Sequence[Session], loaded: Mapping, decode: Callable | None, schedule: Sequence[str], *,
           tail: int = BK_TAIL, pins: Mapping[str, str] | None = None, expect_n: int = schema.N_SESSIONS,
           manifest_pin: str = ids_mod.MANIFEST_OF_RECORD) -> dict:
    """G-VER on the committed ids (``ids.load``'s dict). ``pins`` defaults to the manifest's three tokenizer
    sha256s (``ids.pinned_tokenizer_sha256s``); ``manifest_pin``, MANIFEST.json's own sha256, to the committed
    render's (``ids.MANIFEST_OF_RECORD``)."""
    problems: list[str] = []
    if len(sessions) != expect_n:
        problems.append(f"{len(sessions)} sessions, not {expect_n}")
    m = loaded["manifest"]
    pins = dict(ids_mod.pinned_tokenizer_sha256s()) if pins is None else dict(pins)
    manifest_ok = (m.get("environment") == ids_mod.ENV_OF_RECORD and m.get("tokenizer_files") == pins
                   and m.get("session_set_sha256") == schema.SESSION_SET_SHA256)
    if not manifest_ok:
        problems.append("the manifest does not name G-DATA's environment, the pinned tokenizer files and the session "
                        "set of record")
    pin_ok = loaded["manifest_sha256"] == manifest_pin
    if not pin_ok:
        problems.append("MANIFEST.json's sha256 is not the pin (by default the committed render's, "
                        "ids.MANIFEST_OF_RECORD; ADDENDUM-n1 §1.5)")
    if decode is None:
        problems.append("no decoder: nothing textual can be checked")
    get = ids_mod.ids_of(loaded)
    ok_ids = ok_spans = ok_n4 = 0
    for s in sessions:
        try:
            ids = get(s, None)
            if len(ids) != s.seq_len or ids_sha(ids) != s.ids_sha:
                raise RenderingMismatch(f"{s.session_id}: committed ids are not BK's (length {len(ids)} vs "
                                        f"{s.seq_len}; ids_sha {ids_sha(ids)} vs {s.ids_sha})")
            if decode is not None and decode(ids) != render_text(s):
                raise RenderingMismatch(f"{s.session_id}: committed ids do not decode to the rendering's text")
            ok_ids += 1
        except RenderingMismatch as e:
            problems.append(_masked(f"s={s.bk_run} ids: {e}"))
            continue
        sp = span_problem(s, ids, decode, tail)
        if sp is not None:
            problems.append(f"s={s.bk_run} spans: {sp}")
        else:
            ok_spans += 1
        zone = schedule[s.bk_run]
        named = s.cue_S if zone == "S" else s.cue_U
        try:
            for line in (schema.TOLD_LINE.format(zone=named), schema.SHAM_LINE):
                v = get(s, line)
                rec = loaded["by_variant"][(s.session_id, line)]
                if v[:s.n_pre] != ids[:s.n_pre] or ids_sha(v) != rec["ids_sha"] or rec["schedule_zone"] != zone:
                    raise RenderingMismatch(f"{s.session_id}: an N4 sequence moved a token before n_pre or is not "
                                            f"its record")
                if decode is not None and decode(v) != render_text(s, line):
                    raise RenderingMismatch(f"{s.session_id}: an N4 sequence does not decode to its text")
            ok_n4 += 1
        except RenderingMismatch as e:
            problems.append(_masked(f"s={s.bk_run} n4: {e}"))
    cues = sorted({c for s in sessions for c in (s.cue_S, s.cue_U)})
    n_kept = ok_labels = 0
    for c in loaded["candidates"].values():
        if not c["kept"]:
            continue
        n_kept += 1
        if sorted(c["labels"]) != cues:
            problems.append(f"label candidate {c['name']}: its {len(c['labels'])} labels are not the sessions' "
                            f"{len(cues)} cues")
        elif decode is not None and all(decode(list(t)) == c["template"].format(label=cue)
                                        for cue, t in c["labels"].items()):
            ok_labels += 1
        else:
            problems.append(f"label candidate {c['name']}: its ids do not decode to its texts")
    n = len(sessions)
    passed = (manifest_ok and pin_ok and decode is not None and ok_ids == ok_spans == ok_n4 == n == expect_n
              and n_kept > 0 and ok_labels == n_kept and not problems)
    return {"sessions": n, "ids_ok": ok_ids, "spans_ok": ok_spans, "n4_ok": ok_n4, "labels_kept": n_kept,
            "labels_ok": ok_labels, "manifest_ok": manifest_ok, "status": "PASS" if passed else "STOP",
            "first_problems": problems[:5]}


def _selftest(chk, tmp) -> None:
    """Synthetic sessions rendered by ``ids.render`` under a character tokenizer (whose ids cannot be BK's), checked
    in memory: the PASS path on three sessions, each failure branch, the count clause, the manifest pin, and the span
    convention. A many-to-one decoder (``alias``) isolates the id checks a decode alone would miss. G-VER on BK's
    committed ids runs on the box."""
    import copy
    import dataclasses
    import hashlib
    import inspect
    from pathlib import Path

    from .sessions import load_sessions
    tmp = Path(tmp)
    real = load_sessions()
    enc = lambda text: [ord(c) for c in text]                                          # noqa: E731
    dec = lambda ids: "".join(chr(i) for i in ids)                                     # noqa: E731
    alias = lambda ids: "".join(chr(i % 1_000_000) for i in ids)                       # noqa: E731  (id + 10^6: same)
    pins = {n: "0" * 64 for n in ids_mod.TOKENIZER_FILES}

    def synth(s, spans=None):
        full = enc(render_text(s))
        texts = [span_text(i, z, p) for i, (z, p) in enumerate(s.history)]
        starts = [sum(len(t) for t in texts[:i]) for i in range(len(texts))]
        sp = tuple((a, a + len(t), z) for a, t, (z, _p) in zip(starts, texts, s.history))
        return dataclasses.replace(s, n_pre=sp[-1][1], seq_len=len(full), ids_sha=ids_sha(full),
                                   turn_spans=sp if spans is None else spans)
    ss = [synth(s) for s in real[:3]]
    sched = ["S", "U", "S"]
    t = len(enc(render_text(ss[0]))) - ss[0].n_pre
    rep_r = ids_mod.render(ss, enc, sched, ids_mod.ENV_OF_RECORD, pins, "2026-11-16", tmp / "ids", expect_n=3)
    ld = ids_mod.load(tmp / "ids")
    mpin = hashlib.sha256((tmp / "ids" / ids_mod.MANIFEST_FILE).read_bytes()).hexdigest()   # the folder's own
    kw = dict(tail=t, pins=pins, expect_n=3, manifest_pin=mpin)
    rep = verify(ss, ld, dec, sched, **kw)
    chk("verify: committed ids that hold PASS (G-VER's PASS path)",
        rep_r["status"] == "PASS" and (rep["ids_ok"], rep["spans_ok"], rep["n4_ok"], rep["labels_ok"]) == (3, 3, 3, 4)
        and rep["manifest_ok"] and rep["status"] == "PASS" and not rep["first_problems"], rep)
    rep_160 = verify(ss, ld, dec, sched, **dict(kw, expect_n=schema.N_SESSIONS))
    chk("verify: three sessions where 160 are due do not PASS, and its line says so", rep_160["status"] == "STOP"
        and rep_160["first_problems"] == ["3 sessions, not 160"], rep_160["first_problems"])
    chk("verify: the report's form, pick-free", sorted(rep) == ["first_problems", "ids_ok", "labels_kept", "labels_ok",
                                                                "manifest_ok", "n4_ok", "sessions", "spans_ok",
                                                                "status"], sorted(rep))
    texts = [span_text(i, z, p) for i, (z, p) in enumerate(ss[0].history)]
    chk("verify: the spans' texts are the rendering up to the twelfth passage's end (G-2's convention)",
        "".join(texts) == render_text(ss[0])[:ss[0].n_pre]
        and render_text(ss[0])[ss[0].n_pre:].startswith(EOT + "\n" + USER_OPEN), "")
    shifted = list(ss[0].turn_spans)
    (a3, b3, z3), (a4, b4, z4) = shifted[3], shifted[4]
    shifted[3], shifted[4] = (a3, b3 - 1, z3), (b3 - 1, b4, z4)
    s_sh = dataclasses.replace(ss[0], turn_spans=tuple(shifted))
    rep_sp = verify([s_sh] + ss[1:], ld, dec, sched, **kw)
    chk("verify: a turn span shifted by one token is a span problem", rep_sp["spans_ok"] == 2
        and "turn span 3" in " ".join(rep_sp["first_problems"]), rep_sp["first_problems"][:2])

    def untiled(i, da, db):                                 # turn span i's ends moved by da and db tokens
        sp = list(ss[0].turn_spans)
        a, b, z = sp[i]
        sp[i] = (a + da, b + db, z)
        return dataclasses.replace(ss[0], turn_spans=tuple(sp))
    gaps = [verify([untiled(i, da, db)] + ss[1:], ld, dec, sched, **kw) for i, da, db in ((0, 1, 0), (4, 1, 0),
                                                                                          (11, 0, -1))]
    chk("verify: turn spans that do not tile [0, n_pre) -- the first from 1, a gap between turns, the last short of "
        "n_pre -- are a span problem, named as such before any decode",
        all(r["spans_ok"] == 2 and "do not tile" in " ".join(r["first_problems"]) for r in gaps),
        [r["first_problems"][:1] for r in gaps])
    rep_nd = verify(ss, ld, None, sched, **kw)
    chk("verify: without a decoder nothing textual is checked and G-VER does not PASS",
        rep_nd["status"] == "STOP" and rep_nd["spans_ok"] == 0 and rep_nd["labels_ok"] == 0,
        rep_nd["first_problems"][:1])
    bad = copy.deepcopy(ld)
    rec = bad["by_session"][ss[1].session_id]
    rec["ids"] = rec["ids"][:-1] + [rec["ids"][-1] + 1]
    rep_id = verify(ss, bad, dec, sched, **kw)
    chk("verify: committed ids that are not BK's are an ids problem, and the report quotes no id",
        rep_id["ids_ok"] == 2 and rep_id["first_problems"] and all("[" not in p or "[..]" in p
                                                                    for p in rep_id["first_problems"]),
        rep_id["first_problems"][:1])
    bad6 = copy.deepcopy(ld)
    bad6["by_session"][ss[1].session_id]["ids"][5] += 1_000_000      # its length and its alias decode unchanged
    rep6 = verify(ss, bad6, alias, sched, **kw)
    chk("verify: committed ids whose ids_sha is not BK's are an ids problem even where they decode to the text",
        rep6["ids_ok"] == 2 and rep6["status"] == "STOP", rep6["first_problems"][:1])
    bad2 = copy.deepcopy(ld)
    line = schema.SHAM_LINE
    v = bad2["by_variant"][(ss[2].session_id, line)]
    v["ids"] = [0] + v["ids"][1:]
    rep_n4 = verify(ss, bad2, dec, sched, **kw)
    chk("verify: an N4 sequence that moves a token before n_pre is an N4 problem", rep_n4["n4_ok"] == 2
        and rep_n4["ids_ok"] == 3, rep_n4)
    bad7 = copy.deepcopy(ld)
    v7 = bad7["by_variant"][(ss[2].session_id, line)]
    v7["ids"][0] += 1_000_000                                         # its alias decode unchanged
    v7["ids_sha"] = ids_sha(v7["ids"])                                # and its record's ids_sha its own
    rep7 = verify(ss, bad7, alias, sched, **kw)
    chk("verify: an N4 sequence whose tokens before n_pre are not BK's is an N4 problem, though its record's ids_sha "
        "and its decode agree with it", rep7["n4_ok"] == 2 and rep7["ids_ok"] == 3, rep7["first_problems"][:1])
    rep_sched = verify(ss, ld, dec, ["U", "U", "S"], **kw)
    chk("verify: a schedule other than the render's finds no told sequence for the zone it names",
        rep_sched["n4_ok"] == 2, rep_sched["first_problems"][:1])
    rep_pin = verify(ss, ld, dec, sched, **dict(kw, pins=None))
    chk("verify: a manifest whose tokenizer sha256s are not the manifest's pins does not PASS",
        not rep_pin["manifest_ok"], rep_pin["first_problems"][:1])
    rep_mp = verify(ss, ld, dec, sched, **dict(kw, manifest_pin="0" * 64))
    chk("verify: a MANIFEST.json whose sha256 is not the pin STOPs G-VER, all else holding (ADDENDUM-n1 §1.5)",
        rep_mp["status"] == "STOP" and (rep_mp["ids_ok"], rep_mp["spans_ok"], rep_mp["n4_ok"], rep_mp["labels_ok"])
        == (3, 3, 3, 4) and rep_mp["manifest_ok"] and len(rep_mp["first_problems"]) == 1, rep_mp["first_problems"])
    rep_df = verify(ss, ld, dec, sched, tail=t, pins=pins, expect_n=3)
    chk("verify: the pin defaults to the committed render's (ids.MANIFEST_OF_RECORD), which a synthetic folder's "
        "sha256 is not", inspect.signature(verify).parameters["manifest_pin"].default == ids_mod.MANIFEST_OF_RECORD
        and rep_df["status"] == "STOP" and rep_df["first_problems"] == rep_mp["first_problems"],
        rep_df["first_problems"])
    bad3 = copy.deepcopy(ld)
    cand = bad3["candidates"]["space"]
    cue0 = sorted(cand["labels"])[0]
    cand["labels"][cue0] = cand["labels"][cue0][:-1]
    rep_lab = verify(ss, bad3, dec, sched, **kw)
    chk("verify: a label candidate whose ids do not decode to its texts is a problem", rep_lab["labels_ok"] == 3,
        rep_lab)
    bad4 = copy.deepcopy(ld)
    labs = bad4["candidates"]["space"]["labels"]
    del labs[sorted(labs)[0]]                                         # the rest still decode to their texts
    rep_cue = verify(ss, bad4, dec, sched, **kw)
    chk("verify: a kept candidate that does not hold exactly the sessions' cues is a problem",
        rep_cue["labels_ok"] == 3 and rep_cue["status"] == "STOP"
        and "cues" in " ".join(rep_cue["first_problems"]), rep_cue["first_problems"][:1])
    chk("verify: a rendering mismatch is the renderer's RenderingMismatch", issubclass(RenderingMismatch, ValueError),
        "")
