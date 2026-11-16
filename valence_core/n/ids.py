"""PROPOSAL-n -- the ids of record (ADDENDUM-n1 §1; the seat's answers of 2026-11-16, §1.2-§1.5).

THE RULE (ADDENDUM-n1 §1.1). n's tokenizer of record is G-DATA's environment on the laptop -- the jlens venv: Python
3.12.9, transformers 5.5.0, tokenizers 0.22.2, and the three tokenizer files at the manifest's sha256s
(``data/olmo/manifest.json``, entry ``olmo2_instruct``). Every input id n uses is rendered there once and committed
under ``data/n/ids/`` with ``MANIFEST.json``. The box tokenizes nothing for n's inputs: it loads a tokenizer to
decode, never to produce an input id.

THE FILES (§1.2):
  (i)   ``sessions.jsonl`` -- the 160 sessions' ids, G-DATA's two recorded re-splits applied, each record asserting
        that ``seq_len`` and ``ids_sha`` reproduce. 160 of 160 or STOP; on a STOP nothing is written.
  (ii)  ``n4_variants.jsonl`` -- the 320 told and sham sequences, the line between the choice prompt's two sentences
        (``sessions.choice_prompt``; the join ADDENDUM-n1 §1.2 (ii) fixes), the told zone by N4's schedule
        (``keys.n4_schedule``), each with BK's tokens before ``n_pre`` asserted (``sessions.n4_ids``).
  (iii) ``labels.json`` -- for each of the 12 labels and each of the four candidate conventions of ADDENDUM-n1 §2
        (the bare label after the generation prompt; the label with a leading space; each followed by the end-of-turn
        token), the candidate's ids as the tail of the full sequence after the context's ids, those ids asserted a
        prefix of it (G-DATA's recorded splits applied to the full sequence as to the session's). A candidate is kept
        only if the prefix holds, with the same tail per label, in every context where the label is one of the two
        cues: the 160 sessions and -- Code's reading, beyond §1.2's words, since N4's reads use the same label ids --
        the 320 N4 sequences. Otherwise it is reported and dropped -- a context whose full sequence lacks a recorded
        split's pair counted a prefix failure. No candidate kept is a STOP.
  ``MANIFEST.json`` -- each file's sha256 and record count, the environment, the tokenizer files' sha256s, the
        session set's sha256 (measured from the skeleton files), N4's schedule's sha256, the PI date.
(iv) and (v) are rendered when their texts exist, by the same procedure.

The render's report and the driver print versions, sha256s and counts, never an id; the report keeps its first
``FIRST_PROBLEMS`` problem lines. ``load`` reads the files back for G-VER and the runner, each file's sha256 and record
count checked against ``MANIFEST.json``; ``ids_of`` and ``label_ids`` serve them, and a sequence the files do not hold
is a ``RenderingMismatch``. ``MANIFEST_OF_RECORD`` is the committed render's MANIFEST.json sha256, G-VER's pin
(``verify.verify``'s ``manifest_pin``; ADDENDUM-n1 §1.5).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path
from typing import Callable, Mapping, Sequence

from . import schema
from .sessions import (EOT, RECORDED_SPLITS, RenderingMismatch, Session, ids_sha, n4_ids, render_text,
                       session_ids, session_set_sha256)

REPO = Path(__file__).resolve().parents[2]
IDS_DIR = REPO / "data" / "n" / "ids"
OLMO_MANIFEST = REPO / "data" / "olmo" / "manifest.json"
MANIFEST_ENTRY = "olmo2_instruct"
IDS_SCHEMA = "n-ids-v1"
ENV_OF_RECORD = {"python": "3.12.9", "transformers": "5.5.0", "tokenizers": "0.22.2"}
TOKENIZER_FILES = ("special_tokens_map.json", "tokenizer.json", "tokenizer_config.json")
SESSIONS_FILE, N4_FILE, LABELS_FILE, MANIFEST_FILE = ("sessions.jsonl", "n4_variants.jsonl", "labels.json",
                                                      "MANIFEST.json")
#: The committed render's MANIFEST.json sha256 (``data/n/ids/`` at ``d76f34f``, the ids of record's commit): G-VER's
#: pin (``verify.verify``'s ``manifest_pin``); ADDENDUM-n1 §1.5 puts it in LOCK-n v0.1's "rendering and spans".
MANIFEST_OF_RECORD = "7f51bd914eb03510442f01bfbf7cad7ba74c7e9fb98edb307db350d9772a821d"
#: The render report's problem lines, at most (a full STOP would carry about 480).
FIRST_PROBLEMS = 20
#: ADDENDUM-n1 §2's four candidates, in this order: name -> the text after the generation prompt.
CANDIDATES = (("bare", "{label}"), ("space", " {label}"), ("bare+eot", "{label}" + EOT),
              ("space+eot", " {label}" + EOT))
N_LABELS = 12

Encode = Callable[[str], list]


def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _dumps(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def check_environment(env: Mapping[str, str]) -> None:
    """Refuse any environment but G-DATA's (ADDENDUM-n1 §1.1)."""
    if dict(env) != ENV_OF_RECORD:
        raise SystemExit(f"the render runs only in G-DATA's environment {ENV_OF_RECORD}, not {dict(env)}")


def pinned_tokenizer_sha256s(manifest: Path = OLMO_MANIFEST) -> dict:
    files = json.loads(Path(manifest).read_text(encoding="utf-8"))[MANIFEST_ENTRY]["files"]
    return {name: files[name]["sha256"] for name in TOKENIZER_FILES}


def check_tokenizer_dir(d, manifest: Path = OLMO_MANIFEST) -> dict:
    """The tokenizer folder holds exactly the three files, each at the manifest's sha256 (ADDENDUM-n1 §1.5)."""
    d = Path(d)
    names = sorted(p.name for p in d.iterdir())
    if names != sorted(TOKENIZER_FILES):
        raise SystemExit(f"the tokenizer folder must hold exactly {sorted(TOKENIZER_FILES)}, not {names}")
    pins = pinned_tokenizer_sha256s(manifest)
    got = {name: _sha256_bytes((d / name).read_bytes()) for name in TOKENIZER_FILES}
    bad = [name for name in TOKENIZER_FILES if got[name] != pins[name]]
    if bad:
        raise SystemExit(f"not at the manifest's {MANIFEST_ENTRY} sha256: {bad} -- a failed check goes to the PI")
    return got


def _with_splits(s: Session, ids: list) -> list:
    """G-DATA's recorded re-splits applied to a sequence that begins with the session's tokens (sessions.render_ids'
    rule, for a sequence that runs past it)."""
    ids = list(ids)
    for run, at, canon, emitted in RECORDED_SPLITS:
        if s.bk_run == run:
            if tuple(ids[at:at + 2]) != canon:
                raise RenderingMismatch(f"{s.session_id}: tokens {at}-{at + 1} are not the recorded split's")
            ids[at:at + 2] = list(emitted)
    return ids


def _problem(e: Exception, head: str) -> str:
    """A problem line: the error's text with any bracketed list (a token pair) masked, at most 200 characters."""
    msg = re.sub(r"\[[^\]]*\]", "[..]", str(e))
    return f"{head}: {msg}"[:200]


def _contexts(sessions: Sequence[Session], schedule: Sequence[str]):
    """(session, arm, told_line) for the 160 sessions (arm None) and the 320 N4 sequences."""
    for s in sessions:
        yield s, None, None
    for s in sessions:
        zone = schedule[s.bk_run]
        named = s.cue_S if zone == "S" else s.cue_U
        yield s, "N4-T", schema.TOLD_LINE.format(zone=named)
        yield s, "N4-Ts", schema.SHAM_LINE


def render(sessions: Sequence[Session], encode: Encode, schedule: Sequence[str], env: Mapping[str, str],
           tokenizer_sha256s: Mapping[str, str], pi_date: str, out_dir, *, expect_n: int = schema.N_SESSIONS) -> dict:
    """Render (i)-(iii) and the manifest into ``out_dir``. Returns the report (counts and sha256s, no id; its first
    ``FIRST_PROBLEMS`` problem lines); writes nothing unless the report's status is PASS."""
    problems: list = []
    rep: dict = {"status": "STOP", "sessions": {"n": len(sessions), "ok": 0}, "n4": {"n": 0, "ok": 0},
                 "candidates": {}, "files": {}, "first_problems": problems}

    def note(line: str) -> None:
        if len(problems) < FIRST_PROBLEMS:
            problems.append(line)
    if len(sessions) != expect_n:
        note(f"{len(sessions)} sessions, not {expect_n}")
        return rep
    if len(schedule) != len(sessions) or any(z not in ("S", "U") for z in schedule):
        note("N4's schedule is not one zone per session")
        return rep
    sess_recs, base_ids = [], {}
    for s in sessions:
        try:
            ids = session_ids(s, encode)
        except RenderingMismatch as e:
            note(_problem(e, f"s={s.bk_run}"))
            continue
        base_ids[(s.session_id, None)] = ids
        sess_recs.append({"session_id": s.session_id, "bk_run": s.bk_run, "seq_len": len(ids), "ids_sha": ids_sha(ids),
                          "asserted": {"seq_len": True, "ids_sha": True}, "ids": ids})
    rep["sessions"]["ok"] = len(sess_recs)
    n4_recs = []
    for s, arm, line in _contexts(sessions, schedule):
        if arm is None:
            continue
        rep["n4"]["n"] += 1
        try:
            ids = n4_ids(s, encode, line)
        except RenderingMismatch as e:
            note(_problem(e, f"s={s.bk_run} {arm}"))
            continue
        base_ids[(s.session_id, arm)] = ids
        n4_recs.append({"session_id": s.session_id, "bk_run": s.bk_run, "arm": arm, "line": line,
                        "schedule_zone": schedule[s.bk_run], "n_pre": s.n_pre, "seq_len": len(ids),
                        "ids_sha": ids_sha(ids), "asserted": {"prefix_n_pre": True}, "ids": ids})
    rep["n4"]["ok"] = len(n4_recs)
    if rep["sessions"]["ok"] != len(sessions) or rep["n4"]["ok"] != 2 * len(sessions):
        return rep
    labels = sorted({c for s in sessions for c in (s.cue_S, s.cue_U)})
    if expect_n == schema.N_SESSIONS and len(labels) != N_LABELS:
        note(f"{len(labels)} labels, not {N_LABELS}")
        return rep
    cand_out = []
    for name, tmpl in CANDIDATES:
        tails: dict = {}
        n_ctx = n_prefix = n_equal = 0
        for s, arm, line in _contexts(sessions, schedule):
            base = base_ids[(s.session_id, arm)]
            for cue in (s.cue_S, s.cue_U):
                n_ctx += 1
                try:
                    full = _with_splits(s, [int(i) for i in encode(render_text(s, line) + tmpl.format(label=cue))])
                except RenderingMismatch:           # a recorded split's pair is not where it falls: no prefix kept
                    continue
                if full[:len(base)] != base or len(full) == len(base):
                    continue
                n_prefix += 1
                tail = full[len(base):]
                if tails.setdefault(cue, tail) == tail:
                    n_equal += 1
        kept = n_prefix == n_ctx and n_equal == n_ctx and sorted(tails) == labels
        rep["candidates"][name] = {"kept": kept, "contexts": n_ctx, "prefix_kept": n_prefix, "tail_equal": n_equal}
        cand_out.append({"name": name, "template": tmpl, "kept": kept, "contexts": n_ctx, "prefix_kept": n_prefix,
                         "tail_equal": n_equal, "labels": {c: tails[c] for c in labels} if kept else None})
    if not any(c["kept"] for c in cand_out):
        note("no candidate convention keeps the prefix in every context")
        return rep
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    targets = (SESSIONS_FILE, N4_FILE, LABELS_FILE, MANIFEST_FILE)
    if any((out / t).exists() for t in targets):
        raise SystemExit(f"{out}: the ids files exist already -- the render writes once")
    blobs = {SESSIONS_FILE: ("".join(_dumps(r) + "\n" for r in sess_recs), len(sess_recs)),
             N4_FILE: ("".join(_dumps(r) + "\n" for r in n4_recs), len(n4_recs)),
             LABELS_FILE: (_dumps({"schema": IDS_SCHEMA, "candidates": cand_out}) + "\n", len(cand_out))}
    files = {}
    for fname, (text, count) in blobs.items():
        data = text.encode("utf-8")
        _atomic_write(out / fname, data)
        files[fname] = {"sha256": _sha256_bytes(data), "records": count}
    manifest = {"schema": IDS_SCHEMA, "pi_date": pi_date, "environment": dict(env),
                "tokenizer_files": dict(tokenizer_sha256s), "session_set_sha256": session_set_sha256(),   # measured
                "n4_schedule_sha256": _sha256_bytes(_dumps(list(schedule)).encode()), "files": files}
    mdata = (_dumps(manifest) + "\n").encode("utf-8")
    _atomic_write(out / MANIFEST_FILE, mdata)
    files_rep = dict(files)
    files_rep[MANIFEST_FILE] = {"sha256": _sha256_bytes(mdata), "records": len(files)}
    rep.update(status="PASS", files=files_rep)
    return rep


def _atomic_write(path: Path, data: bytes) -> None:
    """``path.tmp`` written, flushed and fsynced, then renamed over ``path``."""
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def printable(rep: Mapping) -> dict:
    """The report as the driver prints it: it holds no id by construction; asserted here."""
    text = _dumps(rep)
    if '"ids"' in text or '"labels"' in text:
        raise AssertionError("a render report never carries ids")
    return dict(rep)


def load(ids_dir=IDS_DIR) -> dict:
    """The committed files, each checked against MANIFEST.json (sha256 and record count)."""
    d = Path(ids_dir)
    manifest = json.loads((d / MANIFEST_FILE).read_text(encoding="utf-8"))
    if manifest.get("schema") != IDS_SCHEMA or sorted(manifest.get("files", {})) != sorted(
            (SESSIONS_FILE, N4_FILE, LABELS_FILE)):
        raise SystemExit(f"{MANIFEST_FILE}: not an {IDS_SCHEMA} manifest of the three files")
    out: dict = {"manifest": manifest, "manifest_sha256": _sha256_bytes((d / MANIFEST_FILE).read_bytes())}
    for fname, meta in manifest["files"].items():
        data = (d / fname).read_bytes()
        if _sha256_bytes(data) != meta["sha256"]:
            raise SystemExit(f"{fname}: its sha256 is not the manifest's")
        text = data.decode("utf-8")
        recs = [json.loads(x) for x in text.splitlines()] if fname.endswith(".jsonl") else [json.loads(text)]
        n = len(recs) if fname.endswith(".jsonl") else len(recs[0]["candidates"])
        if n != meta["records"]:
            raise SystemExit(f"{fname}: {n} records, the manifest says {meta['records']}")
        out[fname] = recs
    out["by_session"] = {r["session_id"]: r for r in out[SESSIONS_FILE]}
    out["by_variant"] = {(r["session_id"], r["line"]): r for r in out[N4_FILE]}
    out["candidates"] = {c["name"]: c for c in out[LABELS_FILE][0]["candidates"]}
    return out


def ids_of(loaded: Mapping) -> Callable:
    """The runner's ``ids_of``: (session, told_line | None) -> the committed ids; anything else a RenderingMismatch."""
    def get(s: Session, told_line: str | None) -> list:
        rec = (loaded["by_session"].get(s.session_id) if told_line is None
               else loaded["by_variant"].get((s.session_id, told_line)))
        if rec is None:
            raise RenderingMismatch(f"{s.session_id}: no committed sequence for line {told_line!r}")
        return list(rec["ids"])
    return get


def label_ids(loaded: Mapping, convention: str) -> Callable:
    """The runner's ``label_ids`` under the convention of record (ADDENDUM-n1 §2, named in LOCK-n v0.1)."""
    c = loaded["candidates"].get(convention)
    if c is None or not c["kept"]:
        raise SystemExit(f"label convention {convention!r} is not a kept candidate")

    def get(cue: str) -> list:
        if cue not in c["labels"]:
            raise SystemExit(f"no label ids for {cue!r}")
        return list(c["labels"][cue])
    return get


def _selftest(chk, tmp) -> None:
    """Synthetic sessions under a character tokenizer (whose ids cannot be BK's): the PASS path, the STOP path that
    writes nothing, dropped candidates (a broken prefix, a tail that differs between contexts), the N4 clause, a
    recorded split in the label loop (patched in for a synthetic run, restored after), the manifest's checks, the
    problem bound, the environment and tokenizer-folder refusals, and the runner's lookups. The render of record needs
    G-DATA's environment and runs in its own window."""
    import dataclasses
    import sys

    from . import sessions as sessions_mod
    from .sessions import ASSISTANT_OPEN, USER_OPEN, load_sessions
    tmp = Path(tmp)
    real = load_sessions()
    enc = lambda text: [ord(ch) for ch in text]                                        # noqa: E731
    env = dict(ENV_OF_RECORD)
    shas = {n: "0" * 64 for n in TOKENIZER_FILES}

    def synth(s: Session) -> Session:
        ids = enc(render_text(s))
        return dataclasses.replace(s, seq_len=len(ids), ids_sha=ids_sha(ids))
    ss = [synth(s) for s in real[:3]]
    sched = ["S", "U", "S"]
    rep = render(ss, enc, sched, env, shas, "2026-11-16", tmp / "ok", expect_n=3)
    written = sorted(p.name for p in (tmp / "ok").iterdir()) if (tmp / "ok").exists() else []
    chk("ids: a render whose sessions all reproduce PASSes and writes the four files", rep["status"] == "PASS"
        and written == sorted((SESSIONS_FILE, N4_FILE, LABELS_FILE, MANIFEST_FILE)), (rep["status"], written))
    chk("ids: the report carries counts and sha256s, no id", '"ids"' not in _dumps(rep)
        and rep["sessions"] == {"n": 3, "ok": 3} and rep["n4"] == {"n": 6, "ok": 6}, rep["sessions"])
    chk("ids: under a prefix-stable tokenizer every candidate is kept",
        all(v["kept"] and v["contexts"] == 18 == v["prefix_kept"] == v["tail_equal"]
            for v in rep["candidates"].values()), rep["candidates"])
    ld = load(tmp / "ok")
    chk("ids: load checks the manifest and returns the committed ids",
        ids_of(ld)(ss[0], None) == session_ids(ss[0], enc)
        and ids_of(ld)(ss[1], schema.SHAM_LINE) == n4_ids(ss[1], enc, schema.SHAM_LINE), "")
    told1 = schema.TOLD_LINE.format(zone=ss[1].cue_U)
    chk("ids: N4-T's line names the scheduled zone (U for session 1 here)",
        ids_of(ld)(ss[1], told1) == n4_ids(ss[1], enc, told1), "")
    try:
        ids_of(ld)(ss[0], "Prefer nothing.")
        chk("ids: a sequence the files do not hold is a rendering mismatch", False, "no raise")
    except RenderingMismatch:
        chk("ids: a sequence the files do not hold is a rendering mismatch", True, "")
    lab = label_ids(ld, "space")
    chk("ids: label ids are the candidate's text after the generation prompt",
        lab(ss[0].cue_S) == enc(" " + ss[0].cue_S), "")
    try:
        render(ss, enc, sched, env, shas, "2026-11-16", tmp / "ok", expect_n=3)
        chk("ids: the render writes once", False, "no refusal")
    except SystemExit:
        chk("ids: the render writes once", True, "")
    rep_stop = render(real[:3], enc, sched, env, shas, "2026-11-16", tmp / "stop", expect_n=3)
    chk("ids: sessions that do not reproduce STOP the render, and nothing is written",
        rep_stop["status"] == "STOP" and rep_stop["sessions"]["ok"] == 0 and not (tmp / "stop").exists()
        and rep_stop["first_problems"] and all("[" not in p for p in rep_stop["first_problems"]),
        rep_stop["first_problems"][:1])
    chk("ids: a session count other than the expected STOPs, and nothing is written",
        render(ss, enc, sched, env, shas, "d", tmp / "n", expect_n=4)["status"] == "STOP" and not (tmp / "n").exists(),
        "")
    chk("ids: a problem line never quotes a token id", _problem(RenderingMismatch("x: tokens 482-483 are [1, 2], not "
                                                                               "[3, 4]"), "s=62") == "s=62: x: tokens "
        "482-483 are [..], not [..]", _problem(RenderingMismatch("[1]"), "s"))

    def enc_merge(text):                    # merges a newline into a following letter: breaks the bare candidates
        out, i = [], 0
        while i < len(text):
            if text[i] == "\n" and i + 1 < len(text) and text[i + 1].isalpha():
                out.append(100000 + ord(text[i + 1]))
                i += 2
            else:
                out.append(ord(text[i]))
                i += 1
        return out

    def synth_m(s):
        ids = enc_merge(render_text(s))
        return dataclasses.replace(s, seq_len=len(ids), ids_sha=ids_sha(ids))
    ssm = [synth_m(s) for s in real[:3]]
    rep_m = render(ssm, enc_merge, sched, env, shas, "2026-11-16", tmp / "merge", expect_n=3)
    cm = rep_m["candidates"]
    chk("ids: a candidate that breaks the prefix is reported and dropped; the others are kept",
        rep_m["status"] == "PASS" and not cm["bare"]["kept"] and not cm["bare+eot"]["kept"] and cm["space"]["kept"]
        and cm["space+eot"]["kept"] and cm["bare"]["prefix_kept"] == 0, cm)
    ldm = load(tmp / "merge")
    try:
        label_ids(ldm, "bare")
        chk("ids: a dropped candidate cannot be the convention", False, "no refusal")
    except SystemExit:
        chk("ids: a dropped candidate cannot be the convention", True, "")
    mp = tmp / "merge" / MANIFEST_FILE
    man = json.loads(mp.read_text(encoding="utf-8"))
    man["files"][SESSIONS_FILE]["records"] += 1             # the count alone: every file's sha256 unchanged
    mp.write_text(_dumps(man) + "\n", encoding="utf-8")
    try:
        load(tmp / "merge")
        chk("ids: a manifest whose record count is not its file's is refused, every sha256 unchanged", False,
            "no refusal")
    except SystemExit as e:
        chk("ids: a manifest whose record count is not its file's is refused, every sha256 unchanged",
            "records" in str(e), str(e)[:80])

    def n4_text(text):                      # the choice turn (the last user turn) holds a told or sham line
        last = text[text.rfind(USER_OPEN):]
        return schema.SHAM_LINE in last or "Prefer " in last

    def enc_n4(text):                       # moves token 0 whenever a told or sham line is present
        out = enc(text)
        if n4_text(text):
            out[0] += 1
        return out
    try:
        rep_n4 = render(ss, enc_n4, sched, env, shas, "2026-11-16", tmp / "n4", expect_n=3)
        ok_n4 = (rep_n4["status"] == "STOP" and rep_n4["sessions"] == {"n": 3, "ok": 3}
                 and rep_n4["n4"] == {"n": 6, "ok": 0} and not (tmp / "n4").exists())
        d_n4 = rep_n4["n4"]
    except Exception as e:                  # noqa: BLE001 -- past the N4 clause, the label loop lacks N4's bases
        ok_n4, d_n4 = False, type(e).__name__
    chk("ids: N4 sequences that move a token before n_pre STOP the render (n4 ok 0), and nothing is written",
        ok_n4, d_n4)

    def enc_tail(text):                     # after an N4 choice turn a leading-space label takes other ids, while
        head, sep, tail = text.rpartition(ASSISTANT_OPEN)   # the prefix holds in every context
        shift = 300000 if n4_text(text) and tail.startswith(" ") else 0
        return enc(head + sep) + [ord(ch) + shift for ch in tail]
    rep_t = render(ss, enc_tail, sched, env, shas, "2026-11-16", tmp / "tail", expect_n=3)
    ct = rep_t["candidates"]
    chk("ids: a candidate whose tail differs between contexts, its prefix kept in all, is reported and dropped "
        "(tail_equal < contexts); the others are kept",
        rep_t["status"] == "PASS" and ct["bare"]["kept"] and ct["bare+eot"]["kept"]
        and all(not ct[x]["kept"] and ct[x]["prefix_kept"] == ct[x]["contexts"] == 18 and ct[x]["tail_equal"] < 18
                for x in ("space", "space+eot")), ct)
    me = sys.modules[__name__]
    raw2, at = enc(render_text(ss[2])), 10                  # a recorded split for synthetic run 2, at chars 10-11
    canon = (raw2[at], raw2[at + 1])
    emitted = (canon[0] + 400000, canon[1] + 400000)
    split_ids = raw2[:at] + list(emitted) + raw2[at + 2:]
    ss_sp = ss[:2] + [dataclasses.replace(ss[2], seq_len=len(split_ids), ids_sha=ids_sha(split_ids))]
    saved = (sessions_mod.RECORDED_SPLITS, me.RECORDED_SPLITS)
    sessions_mod.RECORDED_SPLITS = me.RECORDED_SPLITS = ((ss[2].bk_run, at, canon, emitted),)
    try:
        rep_sp = render(ss_sp, enc, sched, env, shas, "2026-11-16", tmp / "split", expect_n=3)
        enc_shift = lambda text: enc(text) if text.endswith(ASSISTANT_OPEN) else [7] + enc(text)   # noqa: E731
        try:
            rep_sm = render(ss_sp, enc_shift, sched, env, shas, "2026-11-16", tmp / "splitmiss", expect_n=3)
        except RenderingMismatch:
            rep_sm = {"status": "raised RenderingMismatch", "candidates": {}}
    finally:
        sessions_mod.RECORDED_SPLITS, me.RECORDED_SPLITS = saved
    chk("ids: a recorded split applies to the label loop's full sequences as to the session's (patched in for run "
        "2): the render PASSes, every candidate kept", rep_sp["status"] == "PASS" and len(rep_sp["candidates"]) == 4
        and all(v["kept"] and v["contexts"] == v["prefix_kept"] == v["tail_equal"] == 18
                for v in rep_sp["candidates"].values()), rep_sp["candidates"] or rep_sp["first_problems"][:2])
    chk("ids: a full sequence without a recorded split's pair is a prefix failure, reported and dropped, not a crash; "
        "none kept, the render STOPs and writes nothing", rep_sm["status"] == "STOP"
        and len(rep_sm["candidates"]) == 4 and all(not v["kept"] and v["prefix_kept"] == 0
                                                    for v in rep_sm["candidates"].values())
        and not (tmp / "splitmiss").exists(), rep_sm["status"])
    rep_many = render(real[:8], enc, ["S", "U"] * 4, env, shas, "2026-11-16", tmp / "many", expect_n=8)
    chk("ids: the report keeps at most FIRST_PROBLEMS (20) problem lines: here of 24, 8 sessions' and 16 N4 "
        "sequences'", rep_many["status"] == "STOP" and FIRST_PROBLEMS == 20
        and len(rep_many["first_problems"]) == 20 and not (tmp / "many").exists(), len(rep_many["first_problems"]))
    p = tmp / "ok" / SESSIONS_FILE
    data = bytearray(p.read_bytes())
    data[10] = ord("9") if data[10] != ord("9") else ord("8")
    p.write_bytes(bytes(data))
    try:
        load(tmp / "ok")
        chk("ids: a file whose sha256 is not the manifest's is refused", False, "no refusal")
    except SystemExit:
        chk("ids: a file whose sha256 is not the manifest's is refused", True, "")
    try:
        check_environment({**ENV_OF_RECORD, "transformers": "5.15.0"})
        chk("ids: an environment other than G-DATA's is refused", False, "no refusal")
    except SystemExit:
        chk("ids: an environment other than G-DATA's is refused", True, "")
    td = tmp / "tok"
    td.mkdir()
    for n in TOKENIZER_FILES:
        (td / n).write_text("{}", encoding="utf-8")
    try:
        check_tokenizer_dir(td)
        chk("ids: tokenizer files not at the manifest's sha256s are refused", False, "no refusal")
    except SystemExit:
        chk("ids: tokenizer files not at the manifest's sha256s are refused", True, "")
    (td / "vocab.json").write_text("{}", encoding="utf-8")
    try:
        check_tokenizer_dir(td)
        chk("ids: a tokenizer folder with a fourth file is refused", False, "no refusal")
    except SystemExit as e:
        chk("ids: a tokenizer folder with a fourth file is refused", "exactly" in str(e), str(e)[:80])
    pins = pinned_tokenizer_sha256s()
    chk("ids: the pins are the manifest's olmo2_instruct entry (G-DATA's three)",
        (pins["tokenizer.json"][:8], pins["tokenizer_config.json"][:8], pins["special_tokens_map.json"][:8])
        == ("73fd5254", "fff5b944", "78afb564"), "")
