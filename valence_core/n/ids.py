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
  (iv)  ``gvec_passages.jsonl`` and ``a3_contexts.jsonl`` (``render_iv``; the seat's answers of 2026-11-18, §3 item
        3), rendered by the same procedure once the corpus of record was committed: the 544 passages of
        ``data/n/passages.jsonl`` (its adopted sha256 asserted), each encoded alone with no special tokens and no
        template (directions.py's reading), and A3's frozen 1,344 contexts (``scripts/box_e0_corpus.py``'s
        ``e0_contexts``, its inputs asserted frozen), each ``full`` encoded whole with the span starting at the first id
        where it leaves ``prefix``'s ids (``extract.span_start``'s rule), the prefix's own count beside it. Special
        tokens: A3 ran through the adapter's ``encode``, whose default adds them; the render asserts on every text
        that adding them changes no id, so the two conventions coincide here (a difference is a STOP). The render
        extends (i)-(iii)'s manifest (``MANIFEST_I_III``): its fields unchanged, the two files added to ``files``,
        and an ``iv`` block (its PI date, the base manifest's sha256, the inputs' sha256s, the conventions).
(v) is rendered when its texts exist, by the same procedure.

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
GVEC_FILE, A3_FILE = "gvec_passages.jsonl", "a3_contexts.jsonl"
FILES_I_III = (SESSIONS_FILE, N4_FILE, LABELS_FILE)
FILES_IV = (GVEC_FILE, A3_FILE)
#: (i)-(iii)'s MANIFEST.json sha256 (``data/n/ids/`` at ``d76f34f``, the ids of record's first commit): the manifest
#: ``render_iv`` extends.
MANIFEST_I_III = "7f51bd914eb03510442f01bfbf7cad7ba74c7e9fb98edb307db350d9772a821d"
#: The committed MANIFEST.json's sha256: (i)-(iv)'s, as (iv)'s render wrote it (the ids of record's second commit;
#: (i)-(iii)'s, ``MANIFEST_I_III``, before it). G-VER's pin (``verify.verify``'s ``manifest_pin``); ADDENDUM-n1 §1.5
#: puts it in LOCK-n v0.1's "rendering and spans".
MANIFEST_OF_RECORD = "fdf73d854ebd6fbe02ced28a0c49af1c9658763627aaaa55afd781084f80ef38"
#: The corpus of record (the seat's answers of 2026-11-18, §0): its file, sha256 and passage count, and A3's frozen
#: context count (``scripts/box_e0_corpus.py``: 48 tasks x 7 conditions x 4 paraphrases).
PASSAGES_FILE = REPO / "data" / "n" / "passages.jsonl"
PASSAGES_SHA256 = "ef6b00dc56f28678dce0cf7f81b2ae198862e5a83120037cca37f3c8fc533cc3"
N_PASSAGES, N_A3_CONTEXTS = 544, 1344
PASSAGE_KEYS = ["id", "state", "pole", "text"]
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


def _base_of(manifest: Mapping) -> bytes:
    """The (i)-(iii) manifest an (i)-(iv) manifest extends, as ``render`` wrote it: its fields without ``iv``, its files
    without (iv)'s, in ``_dumps`` form with the trailing newline (``_dumps`` is canonical, so these are its bytes)."""
    base = {k: v for k, v in manifest.items() if k != "iv"}
    base["files"] = {k: v for k, v in manifest["files"].items() if k in FILES_I_III}
    return (_dumps(base) + "\n").encode("utf-8")


def load(ids_dir=IDS_DIR) -> dict:
    """The committed files, each checked against MANIFEST.json (sha256 and record count): (i)-(iii), or (i)-(iii) and
    (iv) under an ``iv`` block whose base is the manifest's own (i)-(iii) part, byte for byte."""
    d = Path(ids_dir)
    manifest = json.loads((d / MANIFEST_FILE).read_text(encoding="utf-8"))
    names = sorted(manifest.get("files", {}))
    if manifest.get("schema") != IDS_SCHEMA or names not in (sorted(FILES_I_III), sorted(FILES_I_III + FILES_IV)) \
            or (names == sorted(FILES_I_III + FILES_IV)) != ("iv" in manifest):
        raise SystemExit(f"{MANIFEST_FILE}: not an {IDS_SCHEMA} manifest of (i)-(iii), or of (i)-(iv) with its iv "
                         f"block")
    if "iv" in manifest and _sha256_bytes(_base_of(manifest)) != manifest["iv"].get("base_manifest_sha256"):
        raise SystemExit(f"{MANIFEST_FILE}: its (i)-(iii) part is not the base manifest its iv block names")
    out: dict = {"manifest": manifest, "manifest_sha256": _sha256_bytes((d / MANIFEST_FILE).read_bytes())}
    for fname, meta in manifest["files"].items():
        if not (d / fname).is_file():
            raise SystemExit(f"{fname}: listed in {MANIFEST_FILE} but absent")
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
    if GVEC_FILE in out:
        out["by_passage"] = {r["id"]: r for r in out[GVEC_FILE]}
    return out


def a3_digest(contexts: Sequence[tuple]) -> str:
    """sha256 of A3's contexts as rendered, in their order: ``_dumps`` of the rows [prefix, full, condition, item_id,
    variant]."""
    return _sha256_bytes(_dumps([[p, f, c, i, int(v)] for p, f, c, i, v in contexts]).encode("utf-8"))


def render_iv(passages_bytes: bytes, contexts: Sequence[tuple], encode: Encode, encode_special: Encode,
              env: Mapping[str, str], tokenizer_sha256s: Mapping[str, str], pi_date: str, base_dir, out_dir, *,
              a3_provenance: Mapping, span_starts: Sequence[int] | None = None,
              passages_sha256: str = PASSAGES_SHA256, expect_passages: int = N_PASSAGES,
              expect_contexts: int = N_A3_CONTEXTS, base_pin: str = MANIFEST_I_III) -> dict:
    """Render (iv) into ``out_dir``, a folder that must not exist yet, as a complete ids folder. It is built in a
    staging folder beside it: (i)-(iii)'s three files copied from ``base_dir`` (their manifest at ``base_pin``, each
    file's bytes re-checked against it as copied), the two (iv) files, and the extended MANIFEST.json. The staging
    folder is read back by ``load`` (every (iv) record's ``ids_sha`` re-derived, the base re-derived from the new
    manifest) and then renamed into place; on any failure it is removed, and nothing is left. ``contexts`` are
    (prefix, full, condition, item_id, variant) in A3's order; ``span_starts``, when given, are
    ``extract.span_start``'s own boundaries, each asserted equal to the render's. ``a3_provenance`` (A3's input
    digests, and the code that builds its texts) goes into the ``iv`` block with the contexts' digest
    (``a3_digest``). Returns the report: counts and sha256s, no id, and its first ``FIRST_PROBLEMS`` problem lines. A
    STOP writes nothing."""
    import shutil
    problems: list = []
    rep: dict = {"status": "STOP", "passages": {"n": 0, "ok": 0}, "a3_contexts": {"n": len(contexts), "ok": 0,
                 "prefix_differs": 0}, "special_tokens_differ": 0, "files": {}, "first_problems": problems}

    def note(line: str) -> None:
        if len(problems) < FIRST_PROBLEMS:
            problems.append(line)
    out = Path(out_dir)
    stage = out.with_name(out.name + ".staging")
    if out.exists() or stage.exists():
        raise SystemExit(f"{out.name}: it or its staging folder exists -- the render writes once, into a new folder")
    base = load(base_dir)
    bman = base["manifest"]
    if base["manifest_sha256"] != base_pin or sorted(bman["files"]) != sorted(FILES_I_III):
        note(f"the base manifest is not (i)-(iii)'s of record ({base['manifest_sha256'][:8]})")
        return rep
    if bman["environment"] != dict(env) or bman["tokenizer_files"] != dict(tokenizer_sha256s):
        note("the environment or the tokenizer files are not the base manifest's")
        return rep
    if _sha256_bytes(passages_bytes) != passages_sha256:
        note("the passages file is not the corpus of record")
        return rep
    lines = passages_bytes.decode("utf-8").splitlines()
    rep["passages"]["n"] = len(lines)
    if len(lines) != expect_passages or len(contexts) != expect_contexts:
        note(f"{len(lines)} passages and {len(contexts)} contexts, not {expect_passages} and {expect_contexts}")
        return rep
    if span_starts is not None and len(span_starts) != len(contexts):
        note(f"{len(span_starts)} span starts for {len(contexts)} contexts")
        return rep

    def ids_both(text: str, where: str):
        ids = [int(x) for x in encode(text)]
        if [int(x) for x in encode_special(text)] != ids:
            rep["special_tokens_differ"] += 1
            note(f"{where}: special tokens change its ids")
            return None
        return ids
    p_recs = []
    for i, line in enumerate(lines):
        try:
            r = json.loads(line)
        except ValueError:
            note(f"passage line {i + 1}: not JSON")
            continue
        if not isinstance(r, dict) or list(r) != PASSAGE_KEYS or not all(isinstance(r[k], str) for k in PASSAGE_KEYS):
            note(f"passage line {i + 1}: not a record of exactly {PASSAGE_KEYS}, all strings")
            continue
        ids = ids_both(r["text"], r["id"])
        if ids is None:
            continue
        if not ids:
            note(f"{r['id']}: no tokens")
            continue
        p_recs.append({"index": i, "id": r["id"], "state": r["state"], "pole": r["pole"],
                       "text_sha256": _sha256_bytes(r["text"].encode("utf-8")), "n_tokens": len(ids),
                       "ids_sha": ids_sha(ids), "ids": ids})
    rep["passages"]["ok"] = len(p_recs)
    if len({r["id"] for r in p_recs}) != len(p_recs):
        note("passage ids are not unique")
        return rep
    c_recs = []
    for j, (prefix, full, condition, item_id, variant) in enumerate(contexts):
        where = f"context {j} ({item_id}/{condition}/{variant})"
        if not full.startswith(prefix) or full == prefix:
            note(f"{where}: full does not extend prefix")
            continue
        a, b = ids_both(prefix, where + " prefix"), ids_both(full, where)
        if a is None or b is None:
            continue
        k = 0                                           # extract.span_start's rule, on these ids
        while k < len(a) and k < len(b) and a[k] == b[k]:
            k += 1
        if not 0 < k < len(b):
            note(f"{where}: degenerate span, boundary {k} of {len(b)} tokens")
            continue
        if span_starts is not None and int(span_starts[j]) != k:
            note(f"{where}: extract.span_start gives {int(span_starts[j])}, the render {k}")
            continue
        if k != len(a):
            rep["a3_contexts"]["prefix_differs"] += 1
        c_recs.append({"index": j, "item_id": item_id, "condition": condition, "variant": int(variant),
                       "prefix_sha256": _sha256_bytes(prefix.encode("utf-8")),
                       "full_sha256": _sha256_bytes(full.encode("utf-8")), "seq_len": len(b), "span_start": k,
                       "prefix_tokens": len(a), "ids_sha": ids_sha(b), "ids": b})
    rep["a3_contexts"]["ok"] = len(c_recs)
    if rep["passages"]["ok"] != expect_passages or rep["a3_contexts"]["ok"] != expect_contexts:
        return rep
    by_state: dict = {}
    for r in p_recs:
        by_state.setdefault(r["state"], []).append(r["n_tokens"])
    rep["passages"]["n_tokens"] = {s: [min(v), round(sum(v) / len(v), 1), max(v)] for s, v in by_state.items()}
    spans = [r["seq_len"] - r["span_start"] for r in c_recs]
    rep["a3_contexts"]["seq_len"] = [min(r["seq_len"] for r in c_recs), max(r["seq_len"] for r in c_recs)]
    rep["a3_contexts"]["span_len"] = [min(spans), round(sum(spans) / len(spans), 2), max(spans)]
    digest = a3_digest(contexts)
    rep["a3_contexts"]["contexts_sha256"] = digest
    blobs = {fname: "".join(_dumps(r) + "\n" for r in recs).encode("utf-8")
             for fname, recs in ((GVEC_FILE, p_recs), (A3_FILE, c_recs))}
    manifest = dict(bman)
    manifest["files"] = {**bman["files"], **{f: {"sha256": _sha256_bytes(b), "records": len(b.splitlines())}
                                            for f, b in blobs.items()}}
    manifest["iv"] = {"pi_date": pi_date, "base_manifest_sha256": base["manifest_sha256"],
                      "passages_sha256": passages_sha256,
                      "a3": {**dict(a3_provenance), "contexts_sha256": digest, "contexts": len(contexts)},
                      "conventions": {"passages": "each passage alone; no special tokens; no template",
                                      "a3_contexts": "full encoded whole; span_start = the first id where full's ids "
                                                     "leave prefix's (extract.span_start); prefix_tokens beside it",
                                      "special_tokens_change_no_id": True}}
    mdata = (_dumps(manifest) + "\n").encode("utf-8")
    stage.mkdir(parents=True)
    try:
        for fname in FILES_I_III:
            data = (Path(base_dir) / fname).read_bytes()
            if _sha256_bytes(data) != bman["files"][fname]["sha256"]:
                raise SystemExit(f"{fname}: not the base manifest's bytes as copied")
            _atomic_write(stage / fname, data)
        for fname, data in blobs.items():
            _atomic_write(stage / fname, data)
        _atomic_write(stage / MANIFEST_FILE, mdata)
        back = load(stage)
        bad = sum(1 for f in FILES_IV for r in back[f] if ids_sha(r["ids"]) != r["ids_sha"])
        if bad or _sha256_bytes(_base_of(back["manifest"])) != base_pin:
            raise SystemExit(f"{out.name}: the staging folder does not read back as rendered")
        os.replace(stage, out)
    except BaseException:
        shutil.rmtree(stage, ignore_errors=True)
        raise
    files_rep = {fname: dict(back["manifest"]["files"][fname]) for fname in FILES_I_III + FILES_IV}
    files_rep[MANIFEST_FILE] = {"sha256": _sha256_bytes(mdata), "records": len(manifest["files"])}
    rep.update(status="PASS", files=files_rep)
    return rep


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

    # (iv): render_iv on a synthetic (i)-(iii) folder under the character tokenizer
    import shutil
    base_iv = tmp / "base_iv"
    render(ss, enc, sched, env, shas, "2026-11-16", base_iv, expect_n=3)
    bpin = _sha256_bytes((base_iv / MANIFEST_FILE).read_bytes())
    plines = [{"id": f"s-{i:02d}", "state": "s", "pole": "+", "text": f"I walk to stop {i}. I wait. I go home{'.' * i}"}
              for i in range(3)]

    def pb(rows) -> bytes:
        return "".join(json.dumps(p) + "\n" for p in rows).encode("utf-8")
    pbytes = pb(plines)
    psha = _sha256_bytes(pbytes)
    pre = "Task: t\nResponse: r\n"
    ctx = [(pre, pre + "Reviewer: good.\n", "self_pos", "e01", 0),
           (pre, pre + "Reviewer: bad.\n", "self_neg", "e01", 1)]
    prov = {"input_shas": {"corpus_sha": "c" * 16}, "code_sha256": {"scripts/box_e0_corpus.py": "d" * 64}}
    kw_iv = dict(a3_provenance=prov, passages_sha256=psha, expect_passages=3, expect_contexts=2, base_pin=bpin)

    def run_iv(name, pbytes_=None, ctx_=None, enc_=enc, encs_=None, env_=None, shas_=None, base=None, **over):
        return render_iv(pbytes if pbytes_ is None else pbytes_, ctx if ctx_ is None else ctx_, enc_,
                         enc_ if encs_ is None else encs_, env if env_ is None else env_,
                         shas if shas_ is None else shas_, "2026-11-18", base or base_iv, tmp / name,
                         **dict(kw_iv, **over))

    def stops(name, *a, **k):
        r = run_iv(name, *a, **k)
        return (r["status"] == "STOP" and not (tmp / name).exists() and not (tmp / (name + ".staging")).exists(),
                r["first_problems"][:1], r)
    k_pre = len(enc(pre))
    rep_iv = run_iv("iv_ok", span_starts=[k_pre, k_pre])
    ok_dir = tmp / "iv_ok"
    written = sorted(p.name for p in ok_dir.iterdir()) if ok_dir.exists() else []
    chk("ids (iv): a render whose passages and contexts all render (extract.span_start's boundaries given, and equal) "
        "PASSes and writes a complete ids folder of six files, its staging folder gone",
        rep_iv["status"] == "PASS" and written == sorted(FILES_I_III + FILES_IV + (MANIFEST_FILE,))
        and not (tmp / "iv_ok.staging").exists(), (rep_iv["status"], written, rep_iv["first_problems"][:2]))
    ld_iv = load(ok_dir)
    man_iv = ld_iv["manifest"]
    bman = json.loads((base_iv / MANIFEST_FILE).read_text(encoding="utf-8"))
    chk("ids (iv): the extended manifest keeps (i)-(iii)'s fields and file entries, adds the two files and the iv "
        "block (its date, base, corpus, A3's provenance with the contexts' digest and count, the conventions)",
        {k: v for k, v in man_iv.items() if k not in ("files", "iv")} == {k: v for k, v in bman.items() if k != "files"}
        and {k: man_iv["files"][k] for k in FILES_I_III} == bman["files"]
        and sorted(man_iv["files"]) == sorted(FILES_I_III + FILES_IV) and man_iv["iv"]["base_manifest_sha256"] == bpin
        and man_iv["iv"]["passages_sha256"] == psha and man_iv["iv"]["pi_date"] == "2026-11-18"
        and man_iv["iv"]["a3"] == {**prov, "contexts_sha256": a3_digest(ctx), "contexts": 2}
        and man_iv["iv"]["conventions"]["special_tokens_change_no_id"] is True and man_iv["pi_date"] == "2026-11-16",
        man_iv.get("iv"))
    chk("ids (iv): the new manifest's (i)-(iii) part is the base manifest byte for byte",
        _sha256_bytes(_base_of(man_iv)) == bpin and _base_of(man_iv) == (base_iv / MANIFEST_FILE).read_bytes(), "")
    chk("ids (iv): (i)-(iii)'s files are copied byte for byte",
        all((ok_dir / f).read_bytes() == (base_iv / f).read_bytes() for f in FILES_I_III), "")
    p0, c1 = ld_iv[GVEC_FILE][0], ld_iv[A3_FILE][1]
    chk("ids (iv): a passage's ids are its text alone; its record carries index, id, state, pole, the text's sha256, "
        "the token count and ids_sha", p0["ids"] == enc(plines[0]["text"]) and p0["n_tokens"] == len(p0["ids"])
        and p0["ids_sha"] == ids_sha(p0["ids"]) and p0["text_sha256"] == _sha256_bytes(plines[0]["text"].encode())
        and (p0["index"], p0["id"], p0["state"], p0["pole"]) == (0, "s-00", "s", "+")
        and ld_iv["by_passage"]["s-02"]["index"] == 2, "")
    chk("ids (iv): a context's ids are full's, its span starts where full leaves prefix (here at the prefix's own "
        "count), and it carries the prefix's and the full's sha256",
        c1["ids"] == enc(ctx[1][1]) and c1["span_start"] == c1["prefix_tokens"] == k_pre
        and (c1["index"], c1["item_id"], c1["condition"], c1["variant"], c1["seq_len"])
        == (1, "e01", "self_neg", 1, len(enc(ctx[1][1])))
        and c1["prefix_sha256"] == _sha256_bytes(pre.encode())
        and c1["full_sha256"] == _sha256_bytes(ctx[1][1].encode())
        and rep_iv["a3_contexts"]["prefix_differs"] == 0, "")
    chk("ids (iv): every record of both (iv) files carries the ids_sha of its own ids",
        all(ids_sha(r["ids"]) == r["ids_sha"] for f in FILES_IV for r in ld_iv[f]) and len(ld_iv[A3_FILE]) == 2, "")
    lens = [len(enc(c[1])) for c in ctx]
    spans = [n - k_pre for n in lens]
    chk("ids (iv): the report carries counts, figures and sha256s, no id: the token counts per state, seq_len and "
        "span_len (min, mean, max), the contexts' digest, no special-token difference",
        '"ids"' not in _dumps(rep_iv) and printable(rep_iv) == rep_iv
        and rep_iv["passages"]["n_tokens"]["s"] == [len(plines[0]["text"]), round(sum(len(p["text"]) for p in plines)
                                                                                  / 3, 1), len(plines[2]["text"])]
        and rep_iv["a3_contexts"]["seq_len"] == [min(lens), max(lens)]
        and rep_iv["a3_contexts"]["span_len"] == [min(spans), round(sum(spans) / 2, 2), max(spans)]
        and rep_iv["a3_contexts"]["contexts_sha256"] == a3_digest(ctx) and rep_iv["special_tokens_differ"] == 0,
        (rep_iv["passages"], rep_iv["a3_contexts"]))
    chk("ids (iv): the report's files are the six files on disk, each sha256 and count (MANIFEST.json's its own)",
        all(rep_iv["files"][f]["sha256"] == _sha256_bytes((ok_dir / f).read_bytes())
            for f in FILES_I_III + FILES_IV + (MANIFEST_FILE,))
        and rep_iv["files"][MANIFEST_FILE]["records"] == 5 and rep_iv["files"][A3_FILE]["records"] == 2, "")
    try:
        run_iv("iv_ok")
        chk("ids (iv): the render writes once, into a new folder", False, "no refusal")
    except SystemExit:
        chk("ids (iv): the render writes once, into a new folder", True, "")
    (tmp / "iv_st.staging").mkdir()
    try:
        run_iv("iv_st")
        chk("ids (iv): a leftover staging folder is refused", False, "no refusal")
    except SystemExit:
        chk("ids (iv): a leftover staging folder is refused", True, "")
    me = sys.modules[__name__]
    saved_w = me._atomic_write

    def boom(path, data):
        if path.name == MANIFEST_FILE:
            raise OSError("synthetic write failure")
        saved_w(path, data)
    me._atomic_write = boom
    try:
        try:
            run_iv("iv_boom")
            raised = False
        except OSError:
            raised = True
    finally:
        me._atomic_write = saved_w
    chk("ids (iv): a failure after the first write leaves nothing: no folder and no staging folder",
        raised and not (tmp / "iv_boom").exists() and not (tmp / "iv_boom.staging").exists(), raised)

    def chk_stop(name, label, *a, problem=None, **k):
        ok, first, r = stops(name, *a, **k)
        chk(f"ids (iv): {label} STOPs, and nothing is written", ok and (problem is None or (first and problem
                                                                                              in first[0])), first)
        return r
    chk_stop("iv_sha", "a passages file that is not the corpus of record", passages_sha256="0" * 64)
    chk_stop("iv_pin", "a base manifest that is not (i)-(iii)'s of record", base_pin="0" * 64)
    chk_stop("iv_five", "a base folder of (i)-(iv), its own manifest given as the pin", base=ok_dir,
             base_pin=_sha256_bytes((ok_dir / MANIFEST_FILE).read_bytes()))
    chk_stop("iv_env", "an environment other than the base manifest's", env_={**env, "transformers": "5.15.0"})
    chk_stop("iv_tok", "a tokenizer file other than the base manifest's", shas_={**shas, TOKENIZER_FILES[0]: "1" * 64})
    ptexts = {p["text"] for p in plines}
    r_all = chk_stop("iv_spec", "special tokens that change every text's ids", encs_=lambda t: [1] + enc(t))
    chk("ids (iv): ...and the count is every encode that differs: three passages, two prefixes, two fulls",
        r_all["special_tokens_differ"] == 7, r_all["special_tokens_differ"])
    for nm, f_, n_ in (("passages", lambda t: [1] + enc(t) if t in ptexts else enc(t), 3),
                       ("prefixes", lambda t: [1] + enc(t) if t == pre else enc(t), 2),
                       ("fulls", lambda t: [1] + enc(t) if t != pre and t.startswith(pre) else enc(t), 2)):
        r_c = chk_stop(f"iv_spec_{nm}", f"special tokens that change the {nm}' ids alone", encs_=f_)
        chk(f"ids (iv): ...the {nm} alone counted ({n_})", r_c["special_tokens_differ"] == n_,
            r_c["special_tokens_differ"])
    chk_stop("iv_noext", "a context whose full does not start with its prefix",
             ctx_=[ctx[0], (pre, "Task: u\nResponse: r\nReviewer: x.\n", "self_neg", "e01", 1)], problem="extend")
    chk_stop("iv_same", "a context whose full is its prefix", ctx_=[ctx[0], (pre, pre, "self_neg", "e01", 1)],
             problem="extend")
    k0 = lambda t: [999] + enc(t) if t == ctx[1][1] else enc(t)                     # noqa: E731
    chk_stop("iv_k0", "a span that would start at token 0", enc_=k0, problem="degenerate")
    kf = lambda t: enc(pre) if t == ctx[1][1] else enc(t)                           # noqa: E731
    chk_stop("iv_kfull", "a span that would start at the full's end", enc_=kf, problem="degenerate")
    chk_stop("iv_count", "a context count other than the expected", expect_contexts=3, problem="2 contexts")
    chk_stop("iv_starts", "an extract.span_start boundary other than the render's", span_starts=[k_pre, k_pre + 1],
             problem="extract.span_start gives")
    chk_stop("iv_nstarts", "a span-start list of the wrong length", span_starts=[k_pre], problem="span starts")
    for nm, old, new in (("missing", b'"pole": "+", ', b""), ("extra", b'"text": ', b'"x": "y", "text": '),
                         ("nonstr", b'"pole": "+"', b'"pole": 1')):
        b_ = pbytes.replace(old, new, 1)
        chk_stop(f"iv_keys_{nm}", f"a passage line with a {nm} key or value", pbytes_=b_,
                 passages_sha256=_sha256_bytes(b_), problem="not a record")
    b_ = b"not json\n" + b"".join(pbytes.splitlines(keepends=True)[1:])
    chk_stop("iv_json", "a passage line that is not JSON", pbytes_=b_, passages_sha256=_sha256_bytes(b_),
             problem="not JSON")
    b_ = pb([plines[0], dict(plines[1], id="s-00"), plines[2]])
    chk_stop("iv_dup", "two passages with one id", pbytes_=b_, passages_sha256=_sha256_bytes(b_), problem="unique")
    b_ = pb([plines[0], dict(plines[1], text=""), plines[2]])
    chk_stop("iv_empty", "a passage with no tokens", pbytes_=b_, passages_sha256=_sha256_bytes(b_), problem="no tokens")
    rep_mg = run_iv("iv_merge", enc_=enc_merge)
    cmg = load(tmp / "iv_merge")[A3_FILE][0] if rep_mg["status"] == "PASS" else {}
    chk("ids (iv): a merge across the boundary starts the span at the first divergent id, one before the prefix's own "
        "count, and is counted (prefix_differs)", rep_mg["status"] == "PASS"
        and rep_mg["a3_contexts"]["prefix_differs"] == 2 and cmg.get("span_start") == cmg.get("prefix_tokens", 0) - 1,
        (rep_mg["a3_contexts"], cmg.get("span_start"), cmg.get("prefix_tokens")))

    def refused_load(folder, edit, label, word):
        dst = tmp / ("load_" + folder)
        shutil.copytree(ok_dir, dst)
        edit(dst)
        try:
            load(dst)
            chk(f"ids (iv): {label} is refused", False, "no refusal")
        except SystemExit as e:
            chk(f"ids (iv): {label} is refused", word in str(e), str(e)[:100])

    def man_edit(fn):
        def go(dst):
            m = json.loads((dst / MANIFEST_FILE).read_text(encoding="utf-8"))
            fn(m)
            (dst / MANIFEST_FILE).write_text(_dumps(m) + "\n", encoding="utf-8")
        return go
    refused_load("noiv", man_edit(lambda m: m.pop("iv")), "a manifest of the five files without its iv block",
                 "iv block")
    refused_load("four", man_edit(lambda m: (m.pop("iv"), m["files"].pop(A3_FILE))),
                 "a manifest of (i)-(iii) and one (iv) file, no iv block", "iv block")
    refused_load("threeiv", man_edit(lambda m: [m["files"].pop(f) for f in FILES_IV]),
                 "a manifest of (i)-(iii) with an iv block", "iv block")
    refused_load("absent", lambda dst: (dst / A3_FILE).unlink(), "a listed file that is absent", "absent")
    refused_load("basebad", man_edit(lambda m: m.update(pi_date="2026-11-17")),
                 "a manifest whose (i)-(iii) part is not the base its iv block names", "base manifest")
    chk("ids (iv): the pins: (iv)'s two file names; (i)-(iii)'s manifest the one (iv) extends; the corpus the one "
        "adopted", FILES_IV == ("gvec_passages.jsonl", "a3_contexts.jsonl") and MANIFEST_I_III.startswith("7f51bd91")
        and PASSAGES_SHA256.startswith("ef6b00dc") and (N_PASSAGES, N_A3_CONTEXTS) == (544, 1344), "")
    try:
        ld_rec = load(IDS_DIR)
        rec_ok = (ld_rec["manifest_sha256"] == MANIFEST_OF_RECORD != MANIFEST_I_III
                  and sorted(ld_rec["manifest"]["files"]) == sorted(FILES_I_III + FILES_IV)
                  and ld_rec["manifest"]["iv"]["base_manifest_sha256"] == MANIFEST_I_III
                  and len(ld_rec[GVEC_FILE]) == N_PASSAGES and len(ld_rec[A3_FILE]) == N_A3_CONTEXTS)
        rec_d = ld_rec["manifest_sha256"][:8]
    except SystemExit as e:
        rec_ok, rec_d = False, str(e)[:80]
    chk("ids: the committed data/n/ids/ is (i)-(iv), its MANIFEST.json at MANIFEST_OF_RECORD, extending (i)-(iii)'s",
        rec_ok, rec_d)
