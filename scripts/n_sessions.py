#!/usr/bin/env python3
"""PROPOSAL-n driver (n v0.2 §8 step 6; the seat's answers of 2026-11-15, §5).

At the n BUILD it wires:

  --selftest   every valence_core.n module's model-free self-test and this driver's checks; "  N/N n selftest checks
               pass", exit 0 iff all pass. Dispatched before any command. The HF backend's cases
               (``valence_core.n.hftiny``: a tiny OLMo-2 built from a config, no weights) run where torch and
               transformers are present -- the box -- and are skipped, and counted as skipped, elsewhere. It writes
               only under a fresh temporary directory outside the repository and reads only the committed BK files
               under data/n/bk; nothing under data/mf3 or any ckpt or reports directory.
  hashes       the licence lines: n's package_sha256 and the import closure's file sha256s (``guard``), measured in
               this process after importing every n production module.
  gver-trial   G-VER (``valence_core.n.verify``) on the 160 sessions' committed ids (``--ids-dir``, default
               data/n/ids/), MANIFEST.json pinned to the committed render's (``ids.MANIFEST_OF_RECORD``), the tokenizer
               loaded from ``--model-dir`` -- an existing folder, local files only, never a hub id -- to decode only
               (tokenizer files, no weights): the BUILD's site-check trial, never of record. Prints the pick-free
               report; exit 0 iff PASS.
  render-ids   the ids of record (``valence_core.n.ids``; ADDENDUM-n1 §1.2 (i)-(iii)), on the laptop only, in G-DATA's
               environment (refused in any other), from ``--tokenizer-dir`` holding exactly the three tokenizer files at
               the manifest's sha256s, into ``--out`` (a new folder outside the repository, or data/n/ids/ or under it:
               anywhere else in the repository is refused, and ``guard.refuse_out``'s roots), with ``--pi-date``.
               Prints the versions, the tokenizer files' sha256s and the report -- counts and sha256s, never an id;
               exit 0 iff PASS, and on a STOP nothing is written.
  render-ids-iv  ADDENDUM-n1 §1.2 (iv) (``ids.render_iv``; the seat's answers of 2026-11-18, §3 item 3), under the
               same environment and tokenizer checks, in Python's UTF-8 mode (PYTHONUTF8=1, so A3's files decode as
               UTF-8): the corpus of record (``data/n/passages.jsonl``, its sha256 asserted) and A3's frozen 1,344
               contexts (``scripts/box_e0_corpus.py``, its inputs asserted frozen, in its order;
               ``extract.span_start``'s boundary for each, under the adapter's encode), extending the committed
               (i)-(iii) under data/n/ids/ into
               ``--out``, a new folder outside the repository that must not exist: (i)-(iii) copied, the two (iv)
               files, the extended MANIFEST.json (A3's input digests, the sha256s of the two files that build its
               texts, and the contexts' digest in its iv block), built in a staging folder, read back, then renamed
               into place. The tokenizer loads from local files only. Prints as render-ids does, with A3's provenance;
               exit 0 iff PASS, and on a STOP or any failure nothing is left.

Stages (the BACKEND extension, G-VEC, G-CAL-n, G-TIME-n, G-VER, the campaign, G-READ-n) are wired at their own steps.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))


def _import_production():
    import importlib

    from valence_core.n import guard
    return {m: importlib.import_module(f"valence_core.n.{m}") for m in guard.PRODUCTION}


def _within(p: Path, root: Path) -> bool:
    try:
        p.relative_to(root)
        return True
    except ValueError:
        return False


def render_out(out: str) -> Path:
    """render-ids' ``--out``: a folder outside the repository, or data/n/ids/ or one under it (ADDENDUM-n1 §1.2);
    anywhere else in the repository is refused (data/n/bk among them), and ``guard.refuse_out`` refuses its roots."""
    from valence_core.n import guard, ids
    p = Path(out).resolve()
    if _within(p, REPO.resolve()) and not _within(p, ids.IDS_DIR.resolve()):
        raise SystemExit(f"render-ids writes inside the repository only under data/n/ids/, not {p}")
    return guard.refuse_out(p)


def cmd_hashes() -> int:
    mods = _import_production()
    guard = mods["guard"]
    print(f"package_sha256 valence_core/n {guard.package_sha256()}")
    for rel, sha in guard.closure_from_modules(dict(sys.modules)).items():
        print(f"imported_sha256 {rel} {sha}")
    return 0


def cmd_selftest() -> int:
    results: list[tuple[str, bool, object]] = []

    def chk(name: str, ok: bool, detail: object = "") -> None:
        results.append((name, bool(ok), detail))
        if not ok:
            print(f"FAIL {name}: {detail}"[:400])

    mods = _import_production()
    from valence_core.n import hftiny, testing    # noqa: F401  (selftest-only modules, imported here only)
    passed, total = mods["schema"]._selftest()
    chk(f"schema: its own self-test {passed}/{total}", passed == total, f"{passed}/{total}")
    with tempfile.TemporaryDirectory(prefix="n-selftest-") as tmp:
        tmp = Path(tmp)
        if str(tmp.resolve()).startswith(str(REPO.resolve())):
            raise SystemExit("the self-test's temporary directory is inside the repository")
        for name in ("sessions", "ids", "keys", "cells", "directions", "primitive", "runner", "verify", "probe",
                     "guard"):
            fn = getattr(mods[name], "_selftest", None)
            if fn is None:
                chk(f"{name}: has a self-test", False, "missing")
                continue
            try:
                fn(chk, tmp / name)
            except BaseException as e:                  # noqa: BLE001 -- a raise inside a self-test is a failure
                chk(f"{name}: its self-test ran to its end", False, f"{type(e).__name__}: {e}"[:300])

        def refused(fn) -> bool:                        # the driver's own refusals: nothing is read or written
            try:
                fn()
            except SystemExit:
                return True
            return False
        chk("driver: render-ids refuses an --out in the repository outside data/n/ids/ (data/n/bk here)",
            refused(lambda: render_out(str(REPO / "data" / "n" / "bk" / "x"))), "")
        ids_dir = mods["ids"].IDS_DIR
        chk("driver: render-ids admits data/n/ids/ and a folder outside the repository",
            not refused(lambda: render_out(str(ids_dir))) and not refused(lambda: render_out(str(tmp / "out"))), "")
        chk("driver: gver-trial refuses a --model-dir that is not an existing folder, before a tokenizer loads",
            refused(lambda: cmd_gver_trial(str(tmp / "no-such-folder"), None)), "")
        def refusal(fn) -> tuple:                       # (refused, its text); any other raise is not a refusal
            try:
                fn()
            except SystemExit as e:
                return True, str(e)
            except BaseException as e:                  # noqa: BLE001
                return False, f"{type(e).__name__}: {e}"[:200]
            return False, "no refusal"
        libs = ("transformers", "tokenizers")
        loaded_before = [m for m in libs if m in sys.modules]
        r_ids = refusal(lambda: cmd_render_ids_iv(str(tmp / "no-tok"), str(ids_dir / "iv"), "2026-11-18"))
        r_bk = refusal(lambda: cmd_render_ids_iv(str(tmp / "no-tok"), str(REPO / "data" / "n" / "bk" / "x"),
                                                 "2026-11-18"))
        loaded_after = [m for m in libs if m in sys.modules]
        chk("driver: render-ids-iv refuses an --out inside the repository, data/n/ids/ included, with its own message, "
            "before the tokenizer libraries are imported", r_ids[0] and r_bk[0]
            and "render-ids-iv writes into a new folder outside the repository" in r_ids[1] + "|" + r_bk[1]
            and r_ids[1] == r_bk[1] and not loaded_before and not loaded_after, (r_ids, r_bk, loaded_after))
        r_d1 = refusal(lambda: cmd_render_ids_iv(str(tmp / "no-tok"), str(tmp / "iv-out"), "Nov 18"))
        r_d2 = refusal(lambda: cmd_render_ids_iv(str(tmp / "no-tok"), str(tmp / "iv-out"), "2026-13-45"))
        r_d3 = refusal(lambda: cmd_render_ids_iv(str(tmp / "no-tok"), str(tmp / "iv-out"), "20261118"))
        chk("driver: render-ids-iv refuses a --pi-date that is not a calendar date written YYYY-MM-DD",
            all(r[0] and "YYYY-MM-DD" in r[1] for r in (r_d1, r_d2, r_d3)), (r_d1, r_d2, r_d3))

        class StubTok:                                  # records the special-token flag of each call
            def __init__(self):
                self.calls = []

            def __call__(self, text, add_special_tokens):
                self.calls.append(("call", add_special_tokens))
                return {"input_ids": [len(text)]}

            def encode(self, text, add_special_tokens):
                self.calls.append(("encode", add_special_tokens))
                return [len(text), 0]
        st = StubTok()
        e_plain, e_spec = _encoders(st)
        chk("driver: render-ids-iv's encoders: (i)-(iii)'s call without special tokens; the adapter's encode with them",
            e_plain("abc") == [3] and e_spec("abc") == [3, 0] and st.calls == [("call", False), ("encode", True)],
            st.calls)
        import hashlib
        import types
        (tmp / "e0stub.py").write_text("# stub\n", encoding="utf-8")
        (tmp / "exstub.py").write_text("# stub\n", encoding="utf-8")
        ctxs = [types.SimpleNamespace(prefix=f"P{i}", full=f"P{i}F{i}", condition=c, item_id=f"e{i:02d}", variant=i)
                for i, c in enumerate(("self_neg", "char_pos", "self_pos"))]
        e0_stub = types.SimpleNamespace(__file__=str(tmp / "e0stub.py"), e0_contexts=lambda: list(ctxs),
                                        assert_frozen_inputs=lambda: {"corpus_sha": "c" * 16})
        seen = []

        def span_stub(adapter, prefix, full):
            seen.append(adapter.encode(prefix))
            return len(prefix) + 1
        ex_stub = types.SimpleNamespace(__file__=str(tmp / "exstub.py"), span_start=span_stub)
        rows, starts, prov = _a3_inputs(e0_stub, ex_stub, lambda t: [7])
        chk("driver: _a3_inputs keeps e0_contexts' order and fields, takes each boundary from span_start under the "
            "given encode, and records the frozen digests and the two files' sha256s",
            rows == [(c.prefix, c.full, c.condition, c.item_id, c.variant) for c in ctxs]
            and starts == [3, 3, 3] and seen == [[7], [7], [7]]
            and prov["input_shas"] == {"corpus_sha": "c" * 16}
            and prov["code_sha256"] == {"e0stub.py": hashlib.sha256(b"# stub\n").hexdigest(),
                                        "exstub.py": hashlib.sha256(b"# stub\n").hexdigest()}, (rows[:1], prov))
    try:
        hftiny.run(chk)
    except BaseException as e:                          # noqa: BLE001
        chk("hftiny: its self-test ran to its end", False, f"{type(e).__name__}: {e}"[:300])
    chk("guard: no production module imports a test double at module level",
        not mods["guard"].testing_import_problems(), mods["guard"].testing_import_problems())
    n_ok = sum(1 for _n, ok, _d in results if ok)
    print(f"  {n_ok}/{len(results)} n selftest checks pass")
    return 0 if n_ok == len(results) else 1


def cmd_gver_trial(model_dir: str, ids_dir: str | None) -> int:
    md = Path(model_dir)
    if not md.is_dir():
        raise SystemExit(f"--model-dir {model_dir!r} is not an existing folder: the tokenizer loads from local files "
                         f"only, never by a hub id")
    from transformers import AutoTokenizer

    from valence_core.n import ids, keys, sessions, verify
    tok = AutoTokenizer.from_pretrained(str(md), local_files_only=True)     # to decode only (ADDENDUM-n1 §1.1)

    def dec(token_ids) -> str:
        return tok.decode(list(token_ids), skip_special_tokens=False, clean_up_tokenization_spaces=False)
    ss = sessions.load_sessions()
    loaded = ids.load(ids_dir or ids.IDS_DIR)
    rep = verify.verify(ss, loaded, dec, keys.n4_schedule([s.present_first_is_S for s in ss]))
    print("G-VER trial (the BUILD's site check; never of record):")
    print(json.dumps(rep, sort_keys=True))
    return 0 if rep["status"] == "PASS" else 1


def cmd_render_ids(tokenizer_dir: str, out: str, pi_date: str) -> int:
    import platform
    import re

    import tokenizers
    import transformers
    from transformers import AutoTokenizer

    from valence_core.n import ids, keys, sessions
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", pi_date or "") is None:
        raise SystemExit("--pi-date is the PI's calendar date, YYYY-MM-DD")
    env = {"python": platform.python_version(), "transformers": transformers.__version__,
           "tokenizers": tokenizers.__version__}
    print(f"environment: python {env['python']} | transformers {env['transformers']} | tokenizers {env['tokenizers']}")
    ids.check_environment(env)
    shas = ids.check_tokenizer_dir(tokenizer_dir)
    for name in ids.TOKENIZER_FILES:
        print(f"tokenizer file {name} {shas[name]} = the manifest's {ids.MANIFEST_ENTRY}")
    out_dir = render_out(out)
    tok = AutoTokenizer.from_pretrained(tokenizer_dir)

    def enc(text: str) -> list:                     # G-DATA (iv)'s call
        return list(tok(text, add_special_tokens=False)["input_ids"])
    ss = sessions.load_sessions()
    schedule = keys.n4_schedule([s.present_first_is_S for s in ss])
    rep = ids.render(ss, enc, schedule, env, shas, pi_date, out_dir)
    print("render-ids (ADDENDUM-n1 §1.2 (i)-(iii)):")
    print(json.dumps(ids.printable(rep), sort_keys=True))
    return 0 if rep["status"] == "PASS" else 1


def _e0_corpus():
    """``scripts/box_e0_corpus.py``, loaded by its path (scripts/ is not a package): A3's frozen contexts."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("box_e0_corpus", REPO / "scripts" / "box_e0_corpus.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _encoders(tok):
    """render-ids-iv's two encoders: (i)-(iii)'s call, no special tokens (G-DATA (iv)'s), and the adapter's ``encode``
    at its default, special tokens added (``tok.encode(text, add_special_tokens=True)``), the call A3's capture made."""
    def enc(text: str) -> list:
        return list(tok(text, add_special_tokens=False)["input_ids"])

    def enc_special(text: str) -> list:
        return list(tok.encode(text, add_special_tokens=True))
    return enc, enc_special


def _a3_inputs(e0, extract_mod, encode_special):
    """A3's contexts as ``e0.e0_contexts()`` gives them, in its order; ``extract_mod.span_start``'s boundary for each,
    under ``encode_special``; and their provenance: the frozen inputs' digests as ``e0.assert_frozen_inputs()``
    returns them, and the sha256 of each of the two files that build the texts, as loaded."""
    import hashlib
    import types
    frozen = e0.assert_frozen_inputs()
    rows = [(c.prefix, c.full, c.condition, c.item_id, c.variant) for c in e0.e0_contexts()]
    shim = types.SimpleNamespace(encode=encode_special)
    starts = [int(extract_mod.span_start(shim, p, f)) for p, f, _c, _i, _v in rows]
    code = {}
    for mod in (e0, extract_mod):
        path = Path(mod.__file__).resolve()
        rel = path.relative_to(REPO.resolve()).as_posix() if _within(path, REPO.resolve()) else path.name
        code[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return rows, starts, {"input_shas": dict(frozen), "code_sha256": code}


def cmd_render_ids_iv(tokenizer_dir: str, out: str, pi_date: str) -> int:
    import datetime
    import platform
    import re

    from valence_core.n import guard, ids
    try:
        ok_date = re.fullmatch(r"\d{4}-\d{2}-\d{2}", pi_date or "") is not None \
            and datetime.date.fromisoformat(pi_date).isoformat() == pi_date
    except ValueError:
        ok_date = False
    if not ok_date:
        raise SystemExit("--pi-date is the PI's calendar date, YYYY-MM-DD")
    p = Path(out).resolve()
    if _within(p, REPO.resolve()):
        raise SystemExit("render-ids-iv writes into a new folder outside the repository; the commit copies from it")
    out_dir = guard.refuse_out(p)
    if not sys.flags.utf8_mode:
        raise SystemExit("render-ids-iv runs in Python's UTF-8 mode (PYTHONUTF8=1), so A3's files decode as UTF-8")
    import tokenizers
    import transformers
    from transformers import AutoTokenizer
    env = {"python": platform.python_version(), "transformers": transformers.__version__,
           "tokenizers": tokenizers.__version__}
    print(f"environment: python {env['python']} | transformers {env['transformers']} | tokenizers {env['tokenizers']}")
    ids.check_environment(env)
    shas = ids.check_tokenizer_dir(tokenizer_dir)
    for name in ids.TOKENIZER_FILES:
        print(f"tokenizer file {name} {shas[name]} = the manifest's {ids.MANIFEST_ENTRY}")
    tok = AutoTokenizer.from_pretrained(tokenizer_dir, local_files_only=True)
    enc, enc_special = _encoders(tok)
    import valence_core.extract as extract_mod
    contexts, starts, prov = _a3_inputs(_e0_corpus(), extract_mod, enc_special)
    print(f"A3's inputs frozen: {json.dumps(prov['input_shas'], sort_keys=True)}; the files that build its texts: "
          f"{json.dumps(prov['code_sha256'], sort_keys=True)}; {len(contexts)} contexts")
    passages = ids.PASSAGES_FILE.read_bytes()
    rep = ids.render_iv(passages, contexts, enc, enc_special, env, shas, pi_date, ids.IDS_DIR, out_dir,
                        a3_provenance=prov, span_starts=starts)
    print("render-ids-iv (ADDENDUM-n1 §1.2 (iv)):")
    print(json.dumps(ids.printable(rep), sort_keys=True))
    return 0 if rep["status"] == "PASS" else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("command", nargs="?", choices=("hashes", "gver-trial", "render-ids", "render-ids-iv"))
    ap.add_argument("--model-dir", default=None)
    ap.add_argument("--tokenizer-dir", default=None)
    ap.add_argument("--ids-dir", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--pi-date", default=None)
    a = ap.parse_args(argv)
    if a.selftest:
        return cmd_selftest()
    if a.command == "render-ids":
        if not (a.tokenizer_dir and a.out and a.pi_date):
            ap.error("render-ids needs --tokenizer-dir, --out and --pi-date")
        return cmd_render_ids(a.tokenizer_dir, a.out, a.pi_date)
    if a.command == "render-ids-iv":
        if not (a.tokenizer_dir and a.out and a.pi_date):
            ap.error("render-ids-iv needs --tokenizer-dir, --out and --pi-date")
        return cmd_render_ids_iv(a.tokenizer_dir, a.out, a.pi_date)
    if a.command == "hashes":
        return cmd_hashes()
    if a.command == "gver-trial":
        if not a.model_dir:
            ap.error("gver-trial needs --model-dir")
        return cmd_gver_trial(a.model_dir, a.ids_dir)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
