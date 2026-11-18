#!/usr/bin/env python3
"""PROPOSAL-n driver (n v0.2 §8 step 6; the seat's answers of 2026-11-15, §5).

At the n BUILD it wires:

  --selftest   every valence_core.n module's model-free self-test and this driver's checks; "  N/N n selftest checks
               pass", exit 0 iff all pass. Dispatched before any command. The HF backend's cases
               (``valence_core.n.hftiny``: a tiny OLMo-2 built from a config, no weights) run where torch and
               transformers are present -- the box -- and are skipped, and counted as skipped, elsewhere. It writes
               only under a fresh temporary directory outside the repository and reads only committed files: BK's
               under data/n/bk, the ids under data/n/ids, the model manifest, and the box's characterization (its
               artifact data/olmo/determinism_base_h100-sxm.json and its raw); nothing under data/mf3 or any ckpt or
               reports directory.
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
  backend-ext  the BACKEND extension, on the box (n v0.2 §3 G-ACQ: "extended with the fresh-versus-cached discordance
               distribution over 24 reads (§2.1's identity bound)"; G-ACQ's dated note GA-5), then ADDENDUM-n1 §2's
               label-convention comparison in the same invocation (the seat's answers of 2026-11-16, second sitting,
               §2.4 and §5 step 4; on n's box by the box answers of 2026-11-18, §2 items 4-5, and with the medians of
               the corpus answers of 2026-11-18, §5.5). ``run_backend_ext``, one model load; everything that needs no
               model before it:
                 1. refusals: the stage's own root and report (data/n/ckpt/backend-ext, data/n/reports/
                    backend-ext.json) for a run of record, a smoke's (``--smoke N --root R --report P``) outside the
                    repository; $RUNPOD_POD_ID the characterized pod's; CUBLAS_WORKSPACE_CONFIG the characterized
                    setting (rule 2); numpy's stream known answer; each --ruling a file;
                 2. the weights of record: the committed model manifest's instruct entry (the working copy HEAD's
                    bytes), its folder holding exactly its files at their byte counts; a WEIGHTS line; and the driver
                    of record: a run of record runs only HEAD's committed bytes of this file (the box answers of
                    2026-11-18, §2 item 5), a smoke any, its sha256 printed either way; a DRIVER line;
                 3. the ids of record; the environment's provenance bridged to the characterization (R6) before the
                    load; the stage identity; what is on disk checked as the runner checks it (a resume's identity,
                    its pauses and rulings); BK's d = 0 floor table and every candidate's ids checked;
                 4. G-VER on the committed ids, the tokenizer alone loaded (local files only), decoding as
                    gver-trial does; a STOP returns 1 before the weights load (Code's reading: at backend-ext the
                    raw is the STOP's record; no stage report);
                 5. the load from the entry's path; the adapter's own provenance must hash as the environment's did;
                 6. the 24 reads: N1-V d = 0, each with its fresh re-computation (``dose-rule``), through the BUILD's
                    runner and 5(f) primitive into the stage's cells, the report at the end;
                 7. on COMPLETE: the distribution (``discordance``: |margin - fresh_margin|, its ratio to the scale,
                    and each label's |logprob - fresh_logprob| -- fidelity values, never a margin); the in-band
                    count (the floor reads' fresh values against the vanilla score: counts only); the comparison
                    (``label_counts``): per candidate, the floor sessions whose S and U values on the vanilla forward
                    both match BK's ``reduced.json`` within half a unit of BK's last decimal plus the bound (R3),
                    printed as one count of 40 per candidate with, beside it, the median absolute difference over
                    its 80 values (both labels, the 40 floor sessions; the seat's answers of 2026-11-18, §5.5),
                    and nothing else -- no value, no margin, nothing per session; nothing of it is written.
               Exit 0 iff the reads are COMPLETE and the comparison ran; a PAUSE ends the invocation with the report
               (the seat adjudicates; ``--resume`` with ``--ruling PAUSE_ID=PATH`` continues, skip-only).
               Code's readings, declared (each flagged in the stage's entry, pending the seat):
                 R1 the 24 sessions: m's key-to-generator function's permutation of the session set's order under
                    ``BEXT_KEY``, its first 24, launched in the set's order (n v0.2 names no set);
                 R2 the reads' label convention ``BEXT_CONVENTION`` ("bare", the first candidate): the reads come
                    before the comparison that settles the convention, whose tolerance needs their bound;
                 R3 the comparison's bound, before any lock states one: the largest per-label |logprob -
                    fresh_logprob| over the 24 reads (the comparison is per label; a shift common to both labels
                    cancels in the margin's |margin - fresh_margin|, which is printed beside it for the lock);
                 R4 the capture site declared at backend-ext ``BEXT_LAYER`` (= BK's 32), nothing injected, the band
                    past it captured (every read captures); the read window ``schema.MAX_WINDOW`` (GA-4), which
                    touches no read (BK's sequences run to 1,273 tokens, 1,276 with the longest label);
                 R5 no cap; the binomial's alpha ``BEXT_ALPHA`` (at p0 = 0 any exceedance fires whatever alpha is);
                 R6 BRIDGE (retargeted by the box answers of 2026-11-18, §2 item 4, not dropped): the stage
                    identity carries n's own ``backend_identifier`` (the adapter declares OLMo-2's
                    4,096-token window). The box's characterization (``CHARACTERIZED_*``: the BACKEND --
                    characterization entry d5d08fa, its pod, provenance and identifier) was taken under the adapter's
                    default window; the same provenance with ``choice_window_declared`` set to that default must hash
                    to its identifier -- the same GPU, CUDA, capability, flags, cuBLAS setting, libraries and Python
                    -- and the pod must be its pod. The field reset is a declaration, not a property of the backend.

Stages G-VEC, G-CAL-n, G-TIME-n, G-VER, the campaign and G-READ-n are wired at their own steps.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

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
        env0 = dict(os.environ)
        try:
            _bext_selftest(chk, tmp / "bext")
        except BaseException as e:                      # noqa: BLE001
            chk("driver: backend-ext's self-test ran to its end", False, f"{type(e).__name__}: {e}"[:300])
        chk("driver: backend-ext's self-test leaves the environment as it found it", dict(os.environ) == env0, "")
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
    ss = sessions.load_sessions()
    loaded = ids.load(ids_dir or ids.IDS_DIR)
    rep = verify.verify(ss, loaded, _decoder(tok), keys.n4_schedule([s.present_first_is_S for s in ss]))
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


# --- the BACKEND extension (n v0.2 §3 G-ACQ; GA-5; ADDENDUM-n1 §2; the seat's answers of 2026-11-16, §2.4, §5.4)

BEXT_STAGE = "backend-ext"
BEXT_KEY = "n-bext"                 # R1
BEXT_N = 24                         # n v0.2 §3 G-ACQ: "over 24 reads"
BEXT_CONVENTION = "bare"            # R2
BEXT_LAYER = 32                     # R4: the capture site declared at backend-ext (BK's 32); nothing is injected
BEXT_ALPHA = 0.01                   # R5
BEXT_SAMPLE_RULE = "every read is at d = 0 and re-computed (dose-rule); no sample"
BEXT_ROOT = REPO / "data" / "n" / "ckpt" / BEXT_STAGE
BEXT_REPORT = REPO / "data" / "n" / "reports" / f"{BEXT_STAGE}.json"
BK_REDUCED = (REPO / "data" / "n" / "bk" / "experiment_results_json" / "fixed_text_design" / "neutral_passages"
              / "reduced.json")
BK_MEMBER = "olmo_32b"
N_LAYERS, D_MODEL = 64, 5120

#: n's box's BACKEND -- characterization (``d5d08fa``; the box answers of 2026-11-18, §2 items 3-5): its pod (the
#: H100 SXM), the provenance its raw prints (``results/raw/2026-11-18_respawn_determinism.txt``) and the identifier it
#: records (R6, retargeted; respawn step (ii)). A new box is a new characterization and a change here.
CHARACTERIZED_POD = "emw1e4embiwe9b"
CHARACTERIZED_PROVENANCE = {
    "adapter": "olmo-hf", "path": "/workspace/models/base", "dtype": "bfloat16", "backend": "torch/cuda",
    "device": "cuda", "gpu": "NVIDIA H100 80GB HBM3", "cuda": "12.8", "capability": [9, 0], "deterministic": True,
    "cublas_workspace_config": ":4096:8", "seed": 20260818, "choice_window_declared": 8192, "n_layers": 64,
    "library_versions": {"torch": "2.8.0+cu128", "transformers": "5.15.0", "accelerate": "1.14.0",
                         "safetensors": "0.8.0", "huggingface_hub": "1.28.0", "numpy": "2.1.2"},
    "python": "3.12.3"}
CHARACTERIZED_IDENTIFIER = "4ed3f2c70fe8afbf"
#: The characterization's committed artifact and raw, which the self-test reads: the literal above is the artifact's
#: provenance, and the raw's BOX line names the pod.
CHARACTERIZED_ARTIFACT = REPO / "data" / "olmo" / "determinism_base_h100-sxm.json"
CHARACTERIZED_ARTIFACT_SHA256 = "1dd9199fb58c2d8e3f4a1830cd2d8345ae0db77e2d8629fe410288ed9955d3c1"
CHARACTERIZED_RAW = REPO / "results" / "raw" / "2026-11-18_respawn_determinism.txt"
#: R1's known answer: sha256 of the 24 drawn sessions' ids, joined by newlines, in the set's order.
BEXT_SESSIONS_SHA256 = "10f3a127fc11fd14e4fb891e9a0046148b88adc332c4814d4677bda1341b6b64"


def _decoder(tok):
    """G-VER's decode: special tokens kept, no clean-up of spaces (gver-trial's form, which PASSed at the BUILD's
    second site check, 2026-11-16, on the A100 pod)."""
    def dec(token_ids) -> str:
        return tok.decode(list(token_ids), skip_special_tokens=False, clean_up_tokenization_spaces=False)
    return dec


def bext_sessions(ss) -> list:
    """R1: the 24 sessions, in the session set's order."""
    from valence_core.m.keys import stream
    if len(ss) < BEXT_N:
        raise SystemExit(f"{len(ss)} sessions, fewer than the {BEXT_N} the BACKEND extension reads")
    perm = stream(BEXT_KEY).permutation(len(ss))
    return [ss[j] for j in sorted(int(x) for x in perm[:BEXT_N])]


def bext_plan(ss) -> list:
    """The stage's plan: one N1-V d = 0 read per R1 session, each re-computed (``dose-rule``), launch indices 0..23."""
    from valence_core.n import runner, schema
    return [runner.PlannedRead(i, s, schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE, 0.0,
                               "dose-rule", None) for i, s in enumerate(bext_sessions(ss))]


def manifest_entry(data: bytes) -> dict:
    """The instruct entry of the model manifest's bytes: its repo, revision, aggregate, file count, path and files."""
    from valence_core.n import ids
    try:
        e = json.loads(data.decode("utf-8"))[ids.MANIFEST_ENTRY]
        out = {"repo": str(e["repo"]), "revision": str(e["revision"]), "sha256": str(e["files_aggregate_sha256"]),
               "n_files": int(e["n_files"]), "path": str(e["path"]),
               "files": {str(k): int(v["bytes"]) for k, v in e["files"].items()}}
    except (ValueError, UnicodeDecodeError, KeyError, TypeError, AttributeError) as ex:
        raise SystemExit(f"the model manifest's instruct entry is malformed ({type(ex).__name__})")
    if len(out["files"]) != out["n_files"] or any(v < 0 for v in out["files"].values()):
        raise SystemExit("the model manifest's instruct entry lists another number of files than n_files, or a "
                         "negative byte count")
    return out


def check_weights_folder(entry: dict) -> None:
    """The weights folder is the entry's path and holds exactly its files, each at its byte count (m's form; the full
    re-hash is respawn step (i), in the box's BACKEND entry)."""
    root = Path(entry["path"])
    if root.is_symlink() or not root.is_dir():
        raise SystemExit(f"the weights path {root} is not a folder on this box")
    names = set(os.listdir(root))
    if names != set(entry["files"]):
        raise SystemExit(f"the weights folder holds {len(names - set(entry['files']))} files the manifest does not "
                         f"list and lacks {len(set(entry['files']) - names)}")
    for name, n in sorted(entry["files"].items()):
        p = root / name
        if p.is_symlink() or not p.is_file() or p.stat().st_size != n:
            raise SystemExit(f"{p}: not a regular file at the manifest's byte count")


def weights_of_record() -> dict:
    """The weights of record, on the box: the committed model manifest (the working copy must be HEAD's bytes), its
    instruct entry, and the folder checked against it. The stage loads only from the entry's path."""
    import subprocess

    from valence_core.n import ids
    rel = Path(ids.OLMO_MANIFEST).resolve().relative_to(REPO.resolve()).as_posix()
    got = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{rel}"], capture_output=True, check=False)
    if got.returncode != 0 or got.stdout != Path(ids.OLMO_MANIFEST).read_bytes():
        raise SystemExit("the model manifest in the working tree is not HEAD's committed bytes")
    entry = manifest_entry(got.stdout)
    check_weights_folder(entry)
    return entry


def driver_bytes() -> tuple:
    """This driver's bytes as run, and HEAD's committed bytes of its path (None when git cannot show them)."""
    import subprocess
    me = Path(__file__).resolve()
    rel = me.relative_to(REPO.resolve()).as_posix()
    got = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{rel}"], capture_output=True, check=False)
    return me.read_bytes(), (got.stdout if got.returncode == 0 else None)


def environment_provenance(path: str) -> dict:
    """The provenance ``OLMoHFAdapter.provenance`` will report, built before the load from what the environment
    decides (the GPU, CUDA, the libraries, Python, the cuBLAS setting) and the stage's declarations. The loaded
    adapter's own provenance must hash to the same identifier."""
    import platform
    from importlib.metadata import PackageNotFoundError, version

    import torch

    from valence_core.n import schema
    vers = {}
    for pkg in ("torch", "transformers", "accelerate", "safetensors", "huggingface_hub", "numpy"):
        try:
            vers[pkg] = version(pkg)
        except PackageNotFoundError:
            vers[pkg] = "absent"
    cuda = torch.cuda.is_available()
    return {"adapter": "olmo-hf", "path": str(path), "dtype": "bfloat16", "backend": "torch/cuda", "device": "cuda",
            "gpu": torch.cuda.get_device_name(0) if cuda else None, "cuda": torch.version.cuda,
            "capability": list(torch.cuda.get_device_capability(0)) if cuda else None, "deterministic": True,
            "cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG"), "seed": 20260818,
            "choice_window_declared": schema.MAX_WINDOW, "n_layers": N_LAYERS, "library_versions": vers,
            "python": platform.python_version()}


def bridge_identifier(provenance) -> str:
    """R6: the provenance with ``choice_window_declared`` set to the adapter's default -- the window the box's
    characterization was taken under -- hashed by m's ``resume.backend_identifier``."""
    from valence_core.adapters.olmo_hf import DEFAULT_CHOICE_WINDOW
    from valence_core.m import resume as m_resume
    return m_resume.backend_identifier(dict(provenance, choice_window_declared=DEFAULT_CHOICE_WINDOW))


def bext_identity(*, package_sha256: str, imported_sha256: dict, weights: str, backend_identifier: str, pod_id: str,
                  rendering_id: str, n_layers: int = N_LAYERS, d_model: int = D_MODEL,
                  layer: int = BEXT_LAYER) -> dict:
    """The stage identity at backend-ext (``schema.STAGE_IDENTITY_FIELDS``): no lock, dose map, direction or bound;
    the rendering and the label convention as this stage's entry names them (R2, R4, R5). Checked before return."""
    from valence_core.n import schema
    ident = {
        "unit": schema.UNIT, "stage": BEXT_STAGE, "record_schema": schema.RECORD_SCHEMA,
        "proposal_sha256": schema.PROPOSAL_SHA256, "lock_sha256": None, "package_sha256": package_sha256,
        "imported_sha256": dict(imported_sha256), "weights_sha256": weights, "backend_identifier": backend_identifier,
        "pod_id": pod_id, "session_set_sha256": schema.SESSION_SET_SHA256, "rendering_id": rendering_id,
        "label_convention": BEXT_CONVENTION, "layer_bk": 32, "layer": int(layer),
        "capture_layers": list(range(int(layer) + 1, int(n_layers))), "n_layers": int(n_layers),
        "d_model": int(d_model), "read_window": schema.MAX_WINDOW, "dose_map": None, "directions": {},
        "fidelity_rule": {"tau": schema.TAU, "p0_count": 0, "p0_n": 2400, "cadence": 160,
                          "sample_key": "n-fid|{s}", "sample_rule": BEXT_SAMPLE_RULE},
        "identity_bound": None,
    }
    schema.check_stage_identity(ident)
    return ident


def discordance(records) -> dict:
    """The fresh-versus-cached distribution over the stage's reads (n v0.2 §3 G-ACQ), fidelity values only, never a
    margin: ``margin`` is |margin - fresh_margin| (the record's ``absdiff``), ``rel`` that over the read's scale,
    ``label`` each label's |logprob - fresh_logprob| (S and U, two per read), with the counts above TAU and TAU/4.
    Every read must carry its re-computation."""
    import numpy as np
    fs = [r.get("fidelity") for r in records]
    if not records or any(f is None for f in fs):
        raise SystemExit("a BACKEND-extension read without its re-computation")
    fin = [(r, f) for r, f in zip(records, fs) if f["absdiff"] is not None and f["rel"] is not None]
    out = {"reads": len(records), "finite": len(fin), "margin": None, "rel": None, "label": None,
           "exceed_tau": sum(1 for _r, f in fin if f["exceeds_tau"] is True),
           "exceed_tau4": sum(1 for _r, f in fin if f["exceeds_tau4"] is True)}
    if fin:
        a = np.array([float(f["absdiff"]) for _r, f in fin])
        q = np.array([float(f["rel"]) for _r, f in fin])
        g = np.array([abs(float(r[f"logprob_{z}"]) - float(f[f"fresh_logprob_{z}"])) for r, f in fin
                      for z in ("S", "U")])
        out["margin"] = {"min": float(a.min()), "median": float(np.median(a)), "p90": float(np.quantile(a, 0.9)),
                         "max": float(a.max())}
        out["rel"] = {"median": float(np.median(q)), "max": float(q.max())}
        out["label"] = {"median": float(np.median(g)), "max": float(g.max())}
    return out


def half_unit(text: str) -> float:
    """Half a unit in the last decimal of a number as BK's JSON text records it (ADDENDUM-n1 §2's tolerance term).
    ValueError, quoting nothing, when the text is not a finite number."""
    from decimal import Decimal, InvalidOperation
    try:
        exp = Decimal(str(text)).as_tuple().exponent
    except InvalidOperation:
        raise ValueError("not a number as recorded")
    if not isinstance(exp, int):
        raise ValueError("not a finite number as recorded")
    return float(Decimal(5).scaleb(exp - 1))


def bk_d0_floor(floor_sessions, path=BK_REDUCED) -> dict:
    """BK's d = 0 values for the floor sessions, from ``reduced.json``'s OLMo reads as recorded (``parse_float=str``):
    session_id -> {"S": (value, half unit), "U": (value, half unit)}. One read per session, a "none" read with the
    session's cues, 40 in all, or SystemExit; no message quotes a value."""
    from valence_core.n import schema
    doc = json.loads(Path(path).read_text(encoding="utf-8"), parse_float=str)
    by: dict = {}
    for r in doc["reads"][BK_MEMBER]:
        if float(r["point"]) != 0.0 or not str(r["cell"]).startswith("floor"):
            continue
        key = (str(r["cell"]), int(r["run"]))
        if key in by:
            raise SystemExit(f"BK records two d = 0 reads for {key}")
        by[key] = r
    out = {}
    for s in floor_sessions:
        r = by.get((s.bk_cell, s.bk_run))
        if r is None or r["cue_S"] != s.cue_S or r["cue_U"] != s.cue_U or r["direction_kind"] != "none":
            raise SystemExit(f"{s.session_id}: BK's d = 0 read is missing or not this session's")
        row = {}
        for z in ("S", "U"):
            text = str(r[f"logprob_{z}"])
            try:
                row[z] = (float(text), half_unit(text))
            except ValueError:
                raise SystemExit(f"{s.session_id}: BK's {z} value is not a finite number as recorded")
        out[s.session_id] = row
    if len(by) != schema.N_FLOOR or len(out) != schema.N_FLOOR:
        raise SystemExit(f"BK's d = 0 floor reads: {len(by)}; floor sessions matched: {len(out)}; not "
                         f"{schema.N_FLOOR}")
    return out


def comparison_ids(s, ids_of, lab, window: int):
    """One floor session's ids and one candidate's two labels' ids, checked: the ids BK's, each forward in the
    window."""
    from valence_core.n.sessions import ids_sha
    ids = [int(x) for x in ids_of(s, None)]
    if ids_sha(ids) != s.ids_sha:
        raise SystemExit(f"{s.session_id}: the committed ids are not BK's")
    out = []
    for cue in (s.cue_S, s.cue_U):
        li = [int(x) for x in lab(cue)]
        if len(ids) + len(li) - 1 > int(window):
            raise SystemExit(f"{s.session_id}: a forward of {len(ids) + len(li) - 1} tokens exceeds the stage's window")
        out.append(li)
    return ids, out[0], out[1]


def label_counts(score, floor_sessions, ids_of, candidates, bk, bound: float, window: int) -> dict:
    """ADDENDUM-n1 §2: per candidate (name -> its label-ids getter), ``count``: the floor sessions whose S and U values
    both match BK's within half a unit of BK's last decimal plus ``bound``; and ``median_abs_diff``: the median of
    |value - BK's| over its values, both labels and every floor session (the seat's answers of 2026-11-18, §5.5; a
    non-finite value counts as an infinite difference). ``score(ids, label_ids)`` is n §2.1's summed log-probability on
    the vanilla forward. Only the counts and the medians leave this function."""
    import statistics
    counts = {}
    for name, lab in candidates.items():
        n, diffs = 0, []
        for s in floor_sessions:
            ids, li_s, li_u = comparison_ids(s, ids_of, lab, window)
            ok = True
            for li, zone in ((li_s, "S"), (li_u, "U")):
                v = float(score(ids, li))
                ref, half = bk[s.session_id][zone]
                d = abs(v - ref) if math.isfinite(v) else math.inf
                diffs.append(d)
                if not (math.isfinite(v) and d <= half + bound):
                    ok = False
            n += int(ok)
        counts[name] = {"count": n, "median_abs_diff": statistics.median(diffs)}
    return counts


def vanilla_score(backend):
    """n §2.1's summed log-probability on the uncached full forward, no injection: the read's fresh path at d = 0
    (``primitive.read``'s arithmetic)."""
    from valence_core.n import primitive

    def score(ids, li) -> float:
        rows, _caps = backend.full(ids, li, (), ())
        return math.fsum(primitive._logp(rows[i], li[i]) for i in range(len(li)))
    return score


def in_band(score, records, by_id, ids_of) -> tuple[int, int]:
    """For the floor sessions among the stage's reads: how many reads' fresh values, both labels, equal the
    comparison's vanilla score exactly (one path, two call sites). Counts only."""
    agree = n = 0
    for r in records:
        s = by_id[r["session_id"]]
        if not s.is_floor or r["fidelity"] is None:
            continue
        n += 1
        ids = [int(x) for x in ids_of(s, None)]
        agree += int(score(ids, r["label_ids_S"]) == r["fidelity"]["fresh_logprob_S"]
                     and score(ids, r["label_ids_U"]) == r["fidelity"]["fresh_logprob_U"])
    return agree, n


def counts_line(counts: dict, n_floor: int) -> str:
    """The comparison as printed: per candidate its count of ``n_floor`` and its median, and nothing else."""
    return (f"label convention (ADDENDUM-n1 §2; per candidate, the count of {n_floor} and the median |value - BK's| "
            f"over its {2 * n_floor} values, nats): "
            + "; ".join(f"{k} {v['count']}/{n_floor}, median {v['median_abs_diff']:.6g}" for k, v in counts.items()))


def convention_line(counts: dict, n_floor: int) -> str:
    full = [k for k, v in counts.items() if v["count"] == n_floor]
    if len(full) == 1:
        return f"exactly one candidate at {n_floor} of {n_floor}: {full[0]}, the convention of record for LOCK-n v0.1"
    return (f"{len(full)} candidates at {n_floor} of {n_floor}: to the seat with the four counts and the four medians "
            f"(ADDENDUM-n1 §2; the seat's answers of 2026-11-18, §5.5)")


def prior_state(root_p: Path, report_p: Path, ident: dict, plan, resume: bool, rulings: dict) -> None:
    """The runner's own checks of what is on disk, made before the load: records or a report without --resume; a
    report under another stage identity (pod, package, rendering, weights, backend ...) or ended in a STOP; a ruling
    that names no standing pause, or a standing pause without its ruling."""
    from valence_core.n import cells, schema
    done = cells.done_read_ids(root_p, sorted({(p.arm, p.direction_id, p.dose_label) for p in plan}))
    prior = None
    if Path(report_p).exists():
        prior = cells.read_json(Path(report_p))
        try:
            schema.check_report(prior, where=Path(report_p).name)
        except schema.SchemaError as e:
            raise SystemExit(f"{Path(report_p).name}: not a valid report, at {str(e).split(': ', 1)[0][:160]}")
    if (done or prior is not None) and not resume:
        raise SystemExit("records or a report are on disk for this stage; run with --resume (skip-only)")
    if prior is None:
        if rulings:
            raise SystemExit("rulings with no report on disk: no pause stands")
        return
    if prior["stage_identity_sha256"] != schema.identity_sha256(ident):
        diff = sorted(k for k in ident if prior["stage_identity"].get(k) != ident[k])
        raise SystemExit(f"the report on disk was written under another stage identity ({diff}): a resume is refused")
    if prior["end_state"] in schema.STOP_KINDS:
        raise SystemExit(f"the stage ended {prior['end_state']}; nothing resumes after a STOP")
    standing = {p["pause_id"] for p in prior["pauses"] if not p["adjudicated"]}
    if set(rulings) - standing:
        raise SystemExit(f"rulings name no standing pause: {sorted(set(rulings) - standing)}")
    if standing - set(rulings):
        raise SystemExit(f"pauses {sorted(standing - set(rulings))} stand: a resume needs each one's ruling (rule 21)")


@dataclass
class BextEnv:
    """What ``run_backend_ext`` reaches outside itself, each a seam the self-test replaces (``production_env``)."""
    weights: Callable                   # () -> the weights of record (``manifest_entry``'s form), the folder checked
    load_sessions: Callable             # () -> the session set
    load_ids: Callable                  # () -> ``ids.load()``
    gver: Callable                      # (sessions, loaded, path) -> G-VER's report, the tokenizer alone loaded
    env_provenance: Callable            # (path) -> the provenance the adapter will report (before the load)
    make_adapter: Callable              # (path) -> the adapter (the weights load)
    adapter_shape: Callable             # (adapter) -> (n_layers, d_model)
    make_backend: Callable              # (adapter) -> the 5(f) backend
    bk_table: Callable                  # (floor sessions) -> ``bk_d0_floor``'s table
    pod: Callable                       # () -> the pod id or None
    driver: Callable                    # () -> (this driver's bytes as run, HEAD's committed bytes of its path | None)
    shape: tuple = (N_LAYERS, D_MODEL, BEXT_LAYER)
    root: Path = BEXT_ROOT
    report: Path = BEXT_REPORT
    printer: Callable = print
    clock: Callable = time.perf_counter


def _gver_tokenizer(ss, loaded, path):
    from transformers import AutoTokenizer

    from valence_core.n import keys, verify
    tok = AutoTokenizer.from_pretrained(str(path), local_files_only=True)      # to decode only (ADDENDUM-n1 §1.1)
    return verify.verify(ss, loaded, _decoder(tok), keys.n4_schedule([s.present_first_is_S for s in ss]))


def _load_adapter(path):
    from valence_core.adapters.olmo_hf import OLMoHFAdapter
    from valence_core.n import schema
    return OLMoHFAdapter(str(path), choice_window=schema.MAX_WINDOW)


def _hf_backend(adapter):
    from valence_core.n import primitive
    return primitive.HFBackend(adapter)


def production_env() -> BextEnv:
    from valence_core.m import resume as m_resume
    from valence_core.n import ids, sessions
    return BextEnv(weights=weights_of_record, load_sessions=sessions.load_sessions, load_ids=ids.load,
                   gver=_gver_tokenizer, env_provenance=environment_provenance, make_adapter=_load_adapter,
                   adapter_shape=lambda a: (int(a.n_layers), int(a._model.config.hidden_size)),
                   make_backend=_hf_backend, bk_table=bk_d0_floor, pod=m_resume.pod_id, driver=driver_bytes)


def run_backend_ext(env: BextEnv, *, root=None, report=None, resume: bool = False, rulings=None,
                    smoke: int | None = None) -> int:
    """The stage, in order: refusals; the weights; the ids and the identity; what is on disk; the comparison's inputs;
    G-VER; the load and the bridge again; the reads; the distribution; the comparison. Everything that needs no
    model happens before the load."""
    from valence_core.m import resume as m_resume
    from valence_core.m.keys import stream_known_answer
    from valence_core.n import cells, guard, ids, runner, schema
    rulings = dict(rulings or {})
    say = env.printer
    if smoke is not None:
        if not 1 <= int(smoke) <= BEXT_N:
            raise SystemExit(f"--smoke takes 1..{BEXT_N} reads")
        if root is None or report is None:
            raise SystemExit("a smoke writes only where --root and --report both name, outside the repository")
        for p in (root, report):
            if _within(Path(p).resolve(), REPO.resolve()):
                raise SystemExit(f"a smoke writes outside the repository, not {p}")
        root_p, report_p = guard.refuse_out(Path(root)), guard.refuse_out(Path(report))
    else:
        if root is not None or report is not None:
            raise SystemExit("a run of record writes only to the stage's own root and report (--root and --report are "
                             "a smoke's)")
        root_p, report_p = guard.refuse_out(Path(env.root)), guard.refuse_out(Path(env.report))
    pod = env.pod()
    if pod is None:
        raise SystemExit("an n stage refuses to start without $RUNPOD_POD_ID (m's resume.pod_id)")
    if pod != CHARACTERIZED_POD:
        raise SystemExit(f"this pod is not the characterized one ({CHARACTERIZED_POD}, the BACKEND entry d5d08fa): "
                         f"respawn step (ii) first")
    if os.environ.get("CUBLAS_WORKSPACE_CONFIG") != CHARACTERIZED_PROVENANCE["cublas_workspace_config"]:
        raise SystemExit("CUBLAS_WORKSPACE_CONFIG is not the characterized setting (rule 2)")
    ka = stream_known_answer()
    if ka:
        raise SystemExit(ka[0])
    for pid, path in rulings.items():
        if not Path(path).is_file():
            raise SystemExit(f"the ruling for {pid} is not a file: {path}")
    if smoke is not None:
        say(f"SMOKE: {smoke} of the {BEXT_N} reads and {smoke} floor sessions, outside the repository; never of record")
    w = env.weights()
    say(f"WEIGHTS: {w['repo']} revision {w['revision']}, files_aggregate_sha256 {w['sha256']}; {w['n_files']} files "
        f"at {w['path']}, each at the manifest's byte count (the full re-hash is respawn step (i))")
    import hashlib
    drv, head = env.driver()
    dsha = hashlib.sha256(drv).hexdigest()
    if smoke is None and drv != head:
        raise SystemExit("a run of record runs only the committed driver: scripts/n_sessions.py is not HEAD's "
                         "committed bytes (the box answers of 2026-11-18, §2 item 5)")
    say(f"DRIVER scripts/n_sessions.py {dsha}: "
        + ("HEAD's committed bytes" if drv == head else "a smoke's, not HEAD's committed bytes (unchecked)"))
    ss = env.load_sessions()
    loaded = env.load_ids()
    if loaded["manifest_sha256"] != ids.MANIFEST_OF_RECORD:
        raise SystemExit("data/n/ids/MANIFEST.json is not the render of record's")
    n_layers, d_model, layer = env.shape
    pre = env.env_provenance(w["path"])
    if bridge_identifier(pre) != CHARACTERIZED_IDENTIFIER:
        raise SystemExit(f"before the load: the environment's provenance under the default window hashes to "
                         f"{bridge_identifier(pre)}, not the characterization's {CHARACTERIZED_IDENTIFIER} (R6)")
    bid = m_resume.backend_identifier(pre)
    mods = _import_production()
    ident = bext_identity(package_sha256=mods["guard"].package_sha256(),
                          imported_sha256=mods["guard"].closure_from_modules(dict(sys.modules)), weights=w["sha256"],
                          backend_identifier=bid, pod_id=pod, rendering_id=loaded["manifest_sha256"],
                          n_layers=n_layers, d_model=d_model, layer=layer)
    plan = bext_plan(ss)[:smoke] if smoke is not None else bext_plan(ss)
    prior_state(root_p, report_p, ident, plan, resume, rulings)
    floor_all = [s for s in ss if s.is_floor]
    bk = env.bk_table(floor_all)
    floor = floor_all[:smoke] if smoke is not None else floor_all
    ids_of = ids.ids_of(loaded)
    cands = {name: ids.label_ids(loaded, name) for name, _t in ids.CANDIDATES}
    for s in floor:
        for lab in cands.values():
            comparison_ids(s, ids_of, lab, int(ident["read_window"]))
    rep = env.gver(ss, loaded, w["path"])
    say("G-VER (the BACKEND extension's start; ADDENDUM-n1 §1.3):")
    say(json.dumps(rep, sort_keys=True))
    if rep["status"] != "PASS":
        say("G-VER STOP: no weights load, nothing is read")
        return 1
    t0 = env.clock()
    adapter = env.make_adapter(w["path"])
    load_ms = max(0, int(round((env.clock() - t0) * 1000)))
    prov = adapter.provenance()
    if m_resume.backend_identifier(prov) != bid or bridge_identifier(prov) != CHARACTERIZED_IDENTIFIER:
        raise SystemExit("the loaded adapter's provenance is not the one checked before the load -- refusing")
    if tuple(env.adapter_shape(adapter)) != (n_layers, d_model):
        raise SystemExit(f"the checkpoint is {tuple(env.adapter_shape(adapter))}, not ({n_layers}, {d_model})")
    say(f"backend: n's identifier {bid} (window {schema.MAX_WINDOW}); the characterization's "
        f"{CHARACTERIZED_IDENTIFIER} under the default window (R6); pod {pod}; load {load_ms} ms")
    backend = env.make_backend(adapter)
    inputs = runner.StageInputs(root=root_p, report_path=report_p, identity=ident, sessions=ss, ids_of=ids_of,
                                label_ids=cands[BEXT_CONVENTION], backend=backend, directions={}, alpha=BEXT_ALPHA,
                                hour_cap_ms=None, load_ms=load_ms, rulings=rulings, printer=say)
    rpt = runner.run(inputs, plan, resume=resume)
    if rpt["end_state"] != "COMPLETE":
        say(f"BACKEND extension: {rpt['end_state']}; no distribution and no comparison until it completes")
        return 1
    cell, _caps = cells.load_cell(root_p, schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE,
                                  identity=ident)
    disc = discordance(cell["records"])
    say(f"discordance over {disc['reads']} reads (nats; fidelity values, no margin): "
        f"{json.dumps(disc, sort_keys=True)}")
    if disc["label"] is None or disc["finite"] != disc["reads"]:
        say("a read has no finite discordance: no comparison")
        return 1
    score = vanilla_score(backend)
    agree, of = in_band(score, cell["records"], {s.session_id: s for s in ss}, ids_of)
    say(f"in-band: {agree} of {of} floor reads' fresh values, both labels, equal the comparison's vanilla score")
    counts = label_counts(score, floor, ids_of, cands, bk, float(disc["label"]["max"]), int(ident["read_window"]))
    say(counts_line(counts, len(floor)))
    say(("SMOKE, never of record: " if smoke is not None else "") + convention_line(counts, len(floor)))
    return 0


def cmd_backend_ext(root=None, report=None, resume: bool = False, rulings=None, smoke: int | None = None) -> int:
    return run_backend_ext(production_env(), root=root, report=report, resume=resume, rulings=rulings, smoke=smoke)


def _bext_selftest(chk, tmp: Path) -> None:
    """backend-ext's checks, model-free: R1's draw (a pinned known answer), the plan, the identity, the weights entry
    and folder, R6's bridge against the characterization's recorded provenance, the distribution, BK's half unit and
    d = 0 table, the comparison, the vanilla score against the read's fresh path, and the command's own flow over the
    numpy double behind every seam, refusals first; on the box, the vanilla score on the HF path too."""
    import hashlib
    import re

    from valence_core.m import resume as m_resume
    from valence_core.m.keys import stream
    from valence_core.n import cells, hftiny, ids, primitive, schema, sessions, testing
    tmp.mkdir(parents=True, exist_ok=True)

    def refused(fn) -> bool:
        try:
            fn()
        except SystemExit:
            return True
        return False

    def raises(fn, exc) -> bool:
        try:
            fn()
        except exc:
            return True
        return False

    ss = sessions.load_sessions()
    b1, b2 = bext_sessions(ss), bext_sessions(ss)
    idx = [ss.index(s) for s in b1]
    chk("driver: backend-ext's 24 sessions are distinct, in the set's order, and drawn alike twice (R1)",
        len(b1) == BEXT_N and idx == sorted(set(idx)) and [s.session_id for s in b1] == [s.session_id for s in b2],
        idx)
    chk("driver: ...the first 24 of m's permutation of the set under n-bext",
        idx == sorted(int(x) for x in stream(BEXT_KEY).permutation(len(ss))[:BEXT_N]), "")
    pinned = hashlib.sha256("\n".join(s.session_id for s in b1).encode()).hexdigest()
    chk("driver: ...pinned: the 24 sessions' ids hash to BEXT_SESSIONS_SHA256", pinned == BEXT_SESSIONS_SHA256, pinned)
    plan = bext_plan(ss)
    chk("driver: backend-ext's plan is 24 N1-V d = 0 reads, each re-computed (dose-rule), launch indices 0..23",
        [p.launch_index for p in plan] == list(range(BEXT_N)) and len({p.read_id for p in plan}) == BEXT_N
        and all((p.arm, p.direction_id, p.dose_label, p.dose_value, p.fidelity_reason, p.schedule_zone)
                == (schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE, 0.0, "dose-rule", None)
                for p in plan), "")
    ident = bext_identity(package_sha256="2" * 64, imported_sha256={"valence_core/m/resume.py": "3" * 64},
                          weights="5" * 64, backend_identifier="6" * 16, pod_id="example-pod",
                          rendering_id=ids.MANIFEST_OF_RECORD)
    chk("driver: the backend-ext identity passes check_stage_identity: no lock, dose map, direction or bound; the "
        "band 33..63; bare; window 4,096; the fidelity rule n §2.1's with G-DATA (vi)'s p0",
        ident["stage"] == "backend-ext" and ident["lock_sha256"] is None and ident["dose_map"] is None
        and ident["directions"] == {} and ident["identity_bound"] is None
        and ident["capture_layers"] == list(range(33, 64)) and ident["label_convention"] == "bare"
        and ident["read_window"] == 4096 and (ident["n_layers"], ident["d_model"], ident["layer"]) == (64, 5120, 32)
        and ident["fidelity_rule"] == {"tau": schema.TAU, "p0_count": 0, "p0_n": 2400, "cadence": 160,
                                       "sample_key": "n-fid|{s}", "sample_rule": BEXT_SAMPLE_RULE}, "")

    entry = manifest_entry(Path(ids.OLMO_MANIFEST).read_bytes())
    chk("driver: the model manifest's instruct entry: G-ACQ's aggregate, 22 files, its revision and path",
        entry["sha256"] == "36f05404dc39ec1759e711f560dc41dcb155f10c0230b671ded9b597fc830fdb"
        and entry["n_files"] == 22 == len(entry["files"]) and entry["revision"] == "b96024342a77"
        and entry["path"] == "/workspace/models/" + ids.MANIFEST_ENTRY, "")
    raw_entry = json.loads(Path(ids.OLMO_MANIFEST).read_text(encoding="utf-8"))[ids.MANIFEST_ENTRY]
    chk("driver: a malformed manifest entry is refused", refused(lambda: manifest_entry(b"{}"))
        and refused(lambda: manifest_entry(json.dumps({ids.MANIFEST_ENTRY: dict(raw_entry, n_files=21)}).encode())),
        "")
    wf = tmp / "weights"
    wf.mkdir()
    (wf / "a.bin").write_bytes(b"12345")
    (wf / "b.json").write_bytes(b"{}")
    went = {"path": str(wf), "files": {"a.bin": 5, "b.json": 2}}
    chk("driver: the weights folder holding exactly the entry's files at their byte counts passes",
        not refused(lambda: check_weights_folder(went)), "")
    chk("driver: ...and a missing file, an extra file, another byte count or a path that is no folder is refused",
        refused(lambda: check_weights_folder(dict(went, files={"a.bin": 5, "b.json": 2, "c.bin": 1})))
        and refused(lambda: check_weights_folder(dict(went, files={"a.bin": 5})))
        and refused(lambda: check_weights_folder(dict(went, files={"a.bin": 6, "b.json": 2})))
        and refused(lambda: check_weights_folder(dict(went, path=str(wf / "a.bin")))), "")

    got_id = m_resume.backend_identifier(CHARACTERIZED_PROVENANCE)
    chk("driver: R6's known answer: the characterization's recorded provenance hashes to its identifier "
        f"{CHARACTERIZED_IDENTIFIER}", got_id == CHARACTERIZED_IDENTIFIER, got_id)
    import hashlib
    art = CHARACTERIZED_ARTIFACT.read_bytes() if CHARACTERIZED_ARTIFACT.is_file() else b""
    box_line = (CHARACTERIZED_RAW.read_text(encoding="utf-8").splitlines()[1:2] or [""])[0] \
        if CHARACTERIZED_RAW.is_file() else ""
    chk("driver: the characterization's literals are its committed record's: the provenance the artifact's (its sha256 "
        "pinned), field for field, and the pod the one its raw's BOX line names",
        hashlib.sha256(art).hexdigest() == CHARACTERIZED_ARTIFACT_SHA256
        and json.loads(art)["provenance"] == CHARACTERIZED_PROVENANCE
        and box_line.startswith(f"# BOX: pod {CHARACTERIZED_POD} "), box_line[:40])
    prov_n = dict(CHARACTERIZED_PROVENANCE, path="/workspace/models/instruct-n", choice_window_declared=4096)
    chk("driver: R6: n's provenance (window 4,096) hashes to another identifier and bridges to the characterization's",
        m_resume.backend_identifier(prov_n) != CHARACTERIZED_IDENTIFIER
        and bridge_identifier(prov_n) == CHARACTERIZED_IDENTIFIER, "")
    chk("driver: R6 refuses another box: a provenance with another GPU, or another library version, does not bridge",
        bridge_identifier(dict(prov_n, gpu="another")) != CHARACTERIZED_IDENTIFIER
        and bridge_identifier(dict(prov_n, library_versions=dict(prov_n["library_versions"], transformers="5.5.0")))
        != CHARACTERIZED_IDENTIFIER, "")

    def frec(a, r, t, t4, ls=-10.0, lu=-12.0, fs=-10.0, fu=-12.0):
        return {"logprob_S": ls, "logprob_U": lu,
                "fidelity": {"absdiff": a, "rel": r, "exceeds_tau": t, "exceeds_tau4": t4, "fresh_logprob_S": fs,
                             "fresh_logprob_U": fu}}
    d = discordance([frec(0.0, 0.0, False, False), frec(0.01, 0.001, False, False, fs=-10.2, fu=-12.21),
                     frec(0.02, 0.002, False, True), frec(0.05, 0.02, True, True, fu=-11.95)])
    near = lambda x, y: abs(x - y) < 1e-12                                          # noqa: E731
    chk("driver: the discordance distribution, a known answer: the margin's (numpy's linear quantile), rel, and each "
        "label's |logprob - fresh_logprob| (8 values)",
        d["reads"] == 4 and d["finite"] == 4 and d["exceed_tau"] == 1 and d["exceed_tau4"] == 2
        and near(d["margin"]["min"], 0.0) and near(d["margin"]["median"], 0.015)
        and near(d["margin"]["p90"], 0.041) and near(d["margin"]["max"], 0.05)
        and near(d["rel"]["median"], 0.0015) and near(d["rel"]["max"], 0.02)
        and near(d["label"]["max"], 0.21) and near(d["label"]["median"], 0.0), d)
    d2 = discordance([frec(0.01, 0.001, False, False), frec(None, None, None, None)])
    chk("driver: a read whose re-computation is not finite is counted, not measured", d2["reads"] == 2
        and d2["finite"] == 1 and near(d2["margin"]["max"], 0.01), d2)
    chk("driver: the distribution refuses a read without its re-computation",
        refused(lambda: discordance([{"fidelity": None}])) and refused(lambda: discordance([])), "")

    chk("driver: half a unit in BK's last decimal, as recorded",
        half_unit("-9.692143320972718") == 5e-16 and half_unit("1.5") == 0.05 and half_unit("2") == 0.5
        and half_unit("1e-05") == 5e-06 and half_unit("-1.250") == 0.0005, "")
    chk("driver: half_unit refuses what is not a finite number, quoting nothing",
        all(raises(lambda b=b: half_unit(b), ValueError) for b in ("nan", "inf", "abc")), "")

    floor = [s for s in ss if s.is_floor]
    real = bk_d0_floor(floor)
    chk("driver: BK's d = 0 floor table from the committed reduced.json: 40 sessions, both labels, each value finite "
        "with a positive half unit",
        len(real) == schema.N_FLOOR and all(set(v) == {"S", "U"} and all(math.isfinite(x) and 0 < h for x, h in
                                                                         v.values()) for v in real.values()), "")

    def synth(recs, text_fix=None) -> Path:
        p = tmp / f"reduced-{len(list(tmp.glob('reduced-*.json')))}.json"
        text = json.dumps({"reads": {BK_MEMBER: recs}})
        p.write_text(text_fix(text) if text_fix else text, encoding="utf-8")
        return p
    base = [{"cell": s.bk_cell, "run": s.bk_run, "point": 0.0, "direction_kind": "none", "cue_S": s.cue_S,
             "cue_U": s.cue_U, "logprob_S": -1.25, "logprob_U": -2.5} for s in floor]
    other = [dict(r, point=1.0, logprob_S=-9.0) for r in base[:3]] + [dict(r, cell="neu_b0") for r in base[:2]]
    got = bk_d0_floor(floor, synth(base + other))
    chk("driver: the table takes the d = 0 floor reads only, each value with its half unit",
        len(got) == schema.N_FLOOR and all(v == {"S": (-1.25, 0.005), "U": (-2.5, 0.05)} for v in got.values()), "")
    got_t = bk_d0_floor(floor, synth(base, lambda t: t.replace('"logprob_S": -1.25,', '"logprob_S": -1.250,')))
    chk("driver: ...the half unit is the recorded text's (\"-1.250\" gives 0.0005), not the float's",
        all(v["S"] == (-1.25, 0.0005) for v in got_t.values()), "")
    one_cue = [dict(base[0], cue_U="Zone Q9")] + base[1:]
    valenced = [dict(base[0], direction_kind="valenced")] + base[1:]
    chk("driver: the table refuses two d = 0 reads of a session, a session missing, one cue not the session's, or a "
        "d = 0 read that is not a \"none\" read",
        refused(lambda: bk_d0_floor(floor, synth(base + base[:1])))
        and refused(lambda: bk_d0_floor(floor, synth(base[1:])))
        and refused(lambda: bk_d0_floor(floor, synth(one_cue)))
        and refused(lambda: bk_d0_floor(floor, synth(valenced))), "")

    toys = [testing.toy_session(r) for r in (0, 1, 2)]
    tss = [s for s, _i in toys]
    by_id = {s.session_id: list(i) for s, i in toys}
    ids_of_t = lambda s, told: by_id[s.session_id]                                 # noqa: E731
    A = lambda cue: [3, 7] if cue == tss[0].cue_S else [5, 11]                      # noqa: E731
    B = lambda cue: [3, 8] if cue == tss[0].cue_S else [5, 11]                      # noqa: E731
    C = lambda cue: [3, 7] if cue == tss[0].cue_S else [5, 12]                      # noqa: E731

    def score(ids, li) -> float:
        return -(sum(li) / 16.0) - len(ids) / 1024.0
    table = {s.session_id: {"S": (score(by_id[s.session_id], A(s.cue_S)), 5e-16),
                            "U": (score(by_id[s.session_id], A(s.cue_U)), 5e-16)} for s in tss}
    c = label_counts(score, tss, ids_of_t, {"A": A, "B": B, "C": C}, table, 0.0, 4096)
    chk("driver: the comparison counts a session only if both labels match: A all; B none (its S differs); C none (its "
        "U differs)", {k: v["count"] for k, v in c.items()} == {"A": 3, "B": 0, "C": 0}, c)
    chk("driver: ...and its median is over both labels and every session (§5.5): A 0; B and C 1/32, the middle of "
        "three zeros and three differences of 1/16 (one label's alone would give 1/16 or 0)",
        {k: v["median_abs_diff"] for k, v in c.items()} == {"A": 0.0, "B": 0.03125, "C": 0.03125}, c)
    offs = {s.session_id: off for s, off in zip(tss, (3.0, 1.0, 0.0))}
    moved = {k: {z: (v + offs[k], h) for z, (v, h) in t.items()} for k, t in table.items()}
    cm = label_counts(score, tss, ids_of_t, {"A": A}, moved, 0.0, 4096)["A"]
    chk("driver: ...a known answer that separates the median from the mean, the midrange and any one session: BK's "
        "values moved 3, 1 and 0 nats give differences 0, 0, 1, 1, 3, 3, median 1 (the mean would be 4/3); count 1",
        cm == {"count": 1, "median_abs_diff": 1.0}, cm)
    inside = {k: {z: (v + 0.9e-3, h) for z, (v, h) in t.items()} for k, t in table.items()}
    outside = {k: {z: (v + 1.1e-3, h) for z, (v, h) in t.items()} for k, t in table.items()}
    halves = {k: {z: (v + 0.004, 0.005) for z, (v, _h) in t.items()} for k, t in table.items()}
    beyond = {k: {z: (v + 0.006, 0.005) for z, (v, _h) in t.items()} for k, t in table.items()}

    def cnt(tbl, bound):
        return label_counts(score, tss, ids_of_t, {"A": A}, tbl, bound, 4096)["A"]["count"]
    chk("driver: ...within half a unit plus the bound, and not beyond it; the half unit counts with no bound",
        (cnt(inside, 1e-3), cnt(outside, 1e-3), cnt(halves, 0.0), cnt(beyond, 0.0)) == (3, 0, 3, 0), "")
    nan_c = label_counts(lambda i, li: float("nan"), tss, ids_of_t, {"A": A}, table, 1.0, 4096)["A"]
    chk("driver: ...a non-finite value never matches, and counts as an infinite difference in the median",
        nan_c["count"] == 0 and nan_c["median_abs_diff"] == math.inf, nan_c)
    changed = lambda s, told: [by_id[s.session_id][0] + 1] + by_id[s.session_id][1:]      # noqa: E731
    chk("driver: ...ids that are not BK's, and a forward past the window, are refused",
        refused(lambda: label_counts(score, tss, changed, {"A": A}, table, 0.0, 4096))
        and refused(lambda: label_counts(score, tss, ids_of_t, {"A": A}, table, 0.0, 4)), "")
    one = {"bare": {"count": 40, "median_abs_diff": 0.0}, "space": {"count": 3, "median_abs_diff": 2.5},
           "bare+eot": {"count": 0, "median_abs_diff": 0.0123456789}}
    chk("driver: the convention line: exactly one at n of n names it; none or two go to the seat with the counts and "
        "the medians", "exactly one candidate at 40 of 40: bare" in convention_line(one, 40)
        and "the four counts and the four medians" in convention_line(
            {"bare": {"count": 40, "median_abs_diff": 0.0}, "space": {"count": 40, "median_abs_diff": 0.0}}, 40)
        and "to the seat" in convention_line({"bare": {"count": 39, "median_abs_diff": 0.1},
                                              "space": {"count": 0, "median_abs_diff": 2.5}}, 40), "")
    chk("driver: the printed comparison is each candidate's count and median (to 6 significant digits), and nothing "
        "else", counts_line(one, 40) == "label convention (ADDENDUM-n1 §2; per candidate, the count of 40 and the "
        "median |value - BK's| over its 80 values, nats): bare 40/40, median 0; space 3/40, median 2.5; bare+eot 0/40, "
        "median 0.0123457", counts_line(one, 40))

    dbl = testing.CausalDouble()
    s0, ids0 = testing.toy_session(3)
    LS, LU = [5, 9, 17], [5, 11, 2]
    rec0, _c0 = primitive.read(dbl, s0, ids0, s0.ids_sha, primitive.ReadSpec("N1-V", "none", "0", 0.0, None), LS, LU,
                               [3, 4, 5], fidelity_reason="dose-rule", shadow=None, identity_bound=None,
                               launch_index=0, capture_row=0)
    vs = vanilla_score(dbl)
    chk("driver: the vanilla score is the read's fresh log-probability, both labels, exactly (the double)",
        vs(ids0, LS) == rec0["fidelity"]["fresh_logprob_S"] and vs(ids0, LU) == rec0["fidelity"]["fresh_logprob_U"],
        "")
    if hftiny.available():
        a = hftiny.tiny_adapter()
        hb = primitive.HFBackend(a)
        st, ids_t = testing.toy_session(3, turn_len=9, tail=5, vocab=128)
        rec_h, _ch = primitive.read(hb, st, ids_t, st.ids_sha, primitive.ReadSpec("N1-V", "none", "0", 0.0, None), LS,
                                    LU, [2, 3], fidelity_reason="dose-rule", shadow=None, identity_bound=None,
                                    launch_index=0, capture_row=0)
        vh = vanilla_score(hb)
        dev = max(abs(vh(ids_t, LS) - rec_h["fidelity"]["fresh_logprob_S"]),
                  abs(vh(ids_t, LU) - rec_h["fidelity"]["fresh_logprob_U"]))
        chk("driver: on the HF path (a tiny OLMo-2 config), the vanilla score is the read's fresh log-probability, "
            "both labels (tol 1e-6)", dev <= 1e-6, dev)
    else:
        chk("driver: the HF-path vanilla score: skipped (no torch/transformers here; runs on the box)", True, "")

    # the command's flow, over the numpy double behind every seam (writes only under tmp)
    saved = {k: os.environ.get(k) for k in ("CUBLAS_WORKSPACE_CONFIG", "RUNPOD_POD_ID")}
    try:
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = CHARACTERIZED_PROVENANCE["cublas_workspace_config"]
        flow = [testing.toy_session(r) for r in range(BEXT_N)]                 # all floor sessions (runs 0..23)
        fss = [s for s, _i in flow]
        labs = {"bare": (LS, LU), "space": ([6, 9, 17], [6, 11, 2]), "bare+eot": (LS + [3], LU + [3]),
                "space+eot": ([6, 9, 17, 3], [6, 11, 2, 3])}
        loaded_t = {"manifest_sha256": ids.MANIFEST_OF_RECORD,
                    "by_session": {s.session_id: {"ids": list(i)} for s, i in flow}, "by_variant": {},
                    "candidates": {n: {"name": n, "kept": True, "labels": {fss[0].cue_S: ls, fss[0].cue_U: lu}}
                                   for n, (ls, lu) in labs.items()}}
        prov_t = dict(CHARACTERIZED_PROVENANCE, path="(toy)", choice_window_declared=schema.MAX_WINDOW)
        made: list = []

        class StubAdapter:
            def __init__(self, prov):
                self._prov = prov

            def provenance(self):
                return dict(self._prov)

        def cached_table(be, floor_s):                     # BK's stand-in: the cached path's values (no fresh bias)
            out = {}
            for s in floor_s:
                ii = by_flow[s.session_id]
                pre = be.prefill(ii, [], [])
                row = {}
                for li, z in ((LS, "S"), (LU, "U")):
                    row[z] = (math.fsum(primitive.score_cached(pre, be.continue_label(pre, li), li)), 5e-16)
                out[s.session_id] = row
            return out
        by_flow = {s.session_id: list(i) for s, i in flow}

        def env_for(tag, **over):
            be = testing.CausalDouble(fresh_bias=(5, 0.3))
            lines: list = []

            def mk(p, prov=None):
                made.append(tag)
                return StubAdapter(prov or prov_t)
            base = dict(weights=lambda: {"repo": "toy", "revision": "0" * 12, "sha256": "5" * 64, "n_files": 1,
                                         "path": "(toy)"},
                        load_sessions=lambda: list(fss), load_ids=lambda: loaded_t,
                        gver=lambda s_, l_, p_: {"status": "PASS", "sessions": len(s_)},
                        env_provenance=lambda p: dict(prov_t), make_adapter=mk, adapter_shape=lambda a: (6, 12),
                        make_backend=lambda a: be, bk_table=lambda f_: cached_table(be, f_),
                        pod=lambda: CHARACTERIZED_POD, driver=lambda: (b"drv", b"drv"), shape=(6, 12, 2),
                        root=tmp / tag / "root", report=tmp / tag / "report.json", printer=lines.append)
            base.update(over)
            return BextEnv(**base), lines

        env1, lines1 = env_for("run")
        rc1 = run_backend_ext(env1)
        cell1, _c = cells.load_cell(env1.root, schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE)
        recs1 = cell1["records"]
        gap = max(abs(r[f"logprob_{z}"] - r["fidelity"][f"fresh_logprob_{z}"]) for r in recs1 for z in ("S", "U"))
        disc_line = next((x for x in lines1 if x.startswith("discordance over")), "")
        printed = json.loads(disc_line.split(": ", 1)[1]) if disc_line else {}
        chk("driver: the command's flow over the double: COMPLETE, 24 records, one load, the comparison's line",
            rc1 == 0 and len(recs1) == BEXT_N and made.count("run") == 1
            and any(x.startswith("label convention (ADDENDUM-n1 §2;") and "over its 48 values" in x
                    and "): bare 24/24, median " in x and "; space " in x for x in lines1)
            and lines1[-1].startswith("exactly one candidate at 24 of 24: bare"), lines1[-3:])
        import hashlib
        chk("driver: ...and a DRIVER line before G-VER: the driver's sha256, HEAD's committed bytes",
            f"DRIVER scripts/n_sessions.py {hashlib.sha256(b'drv').hexdigest()}: HEAD's committed bytes" in lines1
            and lines1.index(next(x for x in lines1 if x.startswith("DRIVER "))) < lines1.index(
                next(x for x in lines1 if x.startswith("G-VER "))), "")
        chk("driver: ...the bound is each label's largest |cached - fresh| (R3), printed, and it is what lets the "
            "cached-path table match the fresh path (a margin bound would not)",
            printed.get("label", {}).get("max") == gap and gap > 0.1
            and printed.get("margin", {}).get("max", 1.0) < 0.01, (gap, printed.get("margin")))
        chk("driver: ...in-band: every floor read's fresh values equal the vanilla score",
            "in-band: 24 of 24 floor reads' fresh values, both labels, equal the comparison's vanilla score" in lines1,
            "")
        chk("driver: ...G-VER comes before the load, and the weights line before G-VER",
            [i for i, x in enumerate(lines1) if x.startswith("WEIGHTS")][0]
            < [i for i, x in enumerate(lines1) if x.startswith("G-VER")][0]
            < [i for i, x in enumerate(lines1) if x.startswith("backend:")][0], "")
        chk("driver: ...a second run on the same root without --resume is refused before the load",
            refused(lambda: run_backend_ext(env1)) and made.count("run") == 1, "")
        r_md = tmp / "ruling.md"
        r_md.write_text("a ruling\n", encoding="utf-8")
        chk("driver: ...a resume with a ruling that names no standing pause is refused before the load",
            refused(lambda: run_backend_ext(env1, resume=True, rulings={"p01": str(r_md)})) and made.count("run") == 1,
            "")
        rc1b = run_backend_ext(env1, resume=True)
        chk("driver: ...a resume after COMPLETE launches nothing and repeats the comparison",
            rc1b == 0 and made.count("run") == 2 and len(cells.load_cell(env1.root, schema.SHADOW_ARM,
                                                                         schema.SHADOW_DIRECTION,
                                                                         schema.SHADOW_DOSE)[0]["records"]) == BEXT_N,
            "")
        env_p, _l = env_for("run", pod=lambda: "another-pod")
        chk("driver: ...a resume on another pod is refused (the pod is not the characterized one)",
            refused(lambda: run_backend_ext(env_p, resume=True)), "")

        env2, lines2 = env_for("smoke", driver=lambda: (b"drv", b"other"))
        rc2 = run_backend_ext(env2, root=str(tmp / "smoke" / "sroot"), report=str(tmp / "smoke" / "srep.json"),
                              smoke=2)
        n2 = len(cells.load_cell(tmp / "smoke" / "sroot", schema.SHADOW_ARM, schema.SHADOW_DIRECTION,
                                 schema.SHADOW_DOSE)[0]["records"])
        chk("driver: a smoke of 2: 2 records in its own root, the comparison over 2 floor sessions, marked SMOKE",
            rc2 == 0 and n2 == 2 and any(x.startswith("label convention (ADDENDUM-n1 §2;") and "over its 4 values" in x
                                         and "): bare 2/2, median " in x and "; space " in x for x in lines2)
            and lines2[-1].startswith("SMOKE, never of record: exactly one candidate at 2 of 2: bare"), lines2[-2:])
        chk("driver: ...a smoke runs a driver that is not HEAD's, and its DRIVER line says so (unchecked)",
            f"DRIVER scripts/n_sessions.py {hashlib.sha256(b'drv').hexdigest()}: a smoke's, not HEAD's committed bytes "
            "(unchecked)" in lines2, "")

        env3, lines3 = env_for("stop", gver=lambda s_, l_, p_: {"status": "STOP", "sessions": len(s_)})
        rc3 = run_backend_ext(env3)
        chk("driver: a G-VER STOP returns 1 before the load, nothing on disk",
            rc3 == 1 and made.count("stop") == 0 and not (tmp / "stop" / "root").exists()
            and lines3[-1] == "G-VER STOP: no weights load, nothing is read", lines3[-1:])
        env4, _l4 = env_for("prebridge", env_provenance=lambda p: dict(prov_t, gpu="another"))
        chk("driver: an environment that does not bridge to the characterization is refused before the load",
            refused(lambda: run_backend_ext(env4)) and made.count("prebridge") == 0, "")
        env5, _l5 = env_for("postload", make_adapter=lambda p: (made.append("postload"),
                                                                StubAdapter(dict(prov_t, n_layers=63)))[1])
        chk("driver: a loaded adapter whose provenance is not the one checked before is refused, nothing read",
            refused(lambda: run_backend_ext(env5)) and made.count("postload") == 1
            and not (tmp / "postload" / "root").exists(), "")
        env6, _l6 = env_for("refuse")
        cases = {
            "--root without --smoke": lambda: run_backend_ext(env6, root=str(tmp / "x")),
            "a smoke of 0 reads": lambda: run_backend_ext(env6, root=str(tmp / "x"), report=str(tmp / "y"), smoke=0),
            "a smoke of 25 reads": lambda: run_backend_ext(env6, root=str(tmp / "x"), report=str(tmp / "y"), smoke=25),
            "a smoke with no --report": lambda: run_backend_ext(env6, root=str(tmp / "x"), smoke=2),
            "a smoke whose report is in the repository": lambda: run_backend_ext(env6, root=str(tmp / "x"),
                                                                                  report=str(BEXT_REPORT), smoke=2),
            "a pod that is not the characterized one": lambda: run_backend_ext(env_for("refuse",
                                                                                       pod=lambda: "pod-x")[0]),
            "no pod": lambda: run_backend_ext(env_for("refuse", pod=lambda: None)[0]),
            "a run of record whose driver is not HEAD's committed bytes": lambda: run_backend_ext(
                env_for("refuse", driver=lambda: (b"drv", b"other"))[0]),
            "a run of record whose HEAD shows no driver": lambda: run_backend_ext(
                env_for("refuse", driver=lambda: (b"drv", None))[0]),
            "a ruling that is not a file": lambda: run_backend_ext(env6, resume=True,
                                                                   rulings={"p01": str(tmp / "none.md")}),
        }
        for name, fn in cases.items():
            chk(f"driver: backend-ext refuses {name}, before the load", refused(fn) and made.count("refuse") == 0, "")
        try:
            run_backend_ext(env_for("refuse", pod=lambda: "pod-x")[0])
            pod_msg = "no refusal"
        except SystemExit as e:
            pod_msg = str(e)
        chk("driver: ...the pod refusal names the characterized pod and the BACKEND entry",
            CHARACTERIZED_POD in pod_msg and "d5d08fa" in pod_msg, pod_msg[:120])
        try:
            run_backend_ext(env_for("refuse", driver=lambda: (b"drv", b"other"))[0])
            drv_msg = "no refusal"
        except SystemExit as e:
            drv_msg = str(e)
        chk("driver: ...the driver refusal says why (the committed driver; the box answers' §2 item 5)",
            "runs only the committed driver" in drv_msg and "§2 item 5" in drv_msg, drv_msg[:120])
        import contextlib
        import io

        def argv_error(argv) -> str:                    # main()'s argparse error: its message, or why there was none
            err = io.StringIO()
            try:
                with contextlib.redirect_stderr(err):
                    main(argv)
            except SystemExit as e:
                return err.getvalue() if e.code == 2 else f"exit {e.code}"
            return "no error"
        t_, o_, d_ = str(tmp / "t"), str(tmp / "o"), "2026-11-18"
        for argv, want in ((["render-ids-iv"], "render-ids-iv needs --tokenizer-dir, --out and --pi-date"),
                           (["render-ids-iv", "--resume", "--tokenizer-dir", t_, "--out", o_, "--pi-date", d_],
                            "backend-ext's options only"),
                           (["render-ids-iv", "--smoke", "0", "--tokenizer-dir", t_, "--out", o_, "--pi-date", d_],
                            "backend-ext's options only"),
                           (["hashes", "--root", ""], "backend-ext's options only"),
                           (["backend-ext", "--out", o_], "takes no folder options"),
                           (["backend-ext", "--ruling", "p01"], "--ruling takes PAUSE_ID=PATH")):
            got = argv_error(argv)
            chk(f"driver: main() refuses {' '.join(argv[:2])} … with \"{want}\"", want in got, got[-160:])
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
        chk("driver: backend-ext refuses a cuBLAS setting other than the characterized one (rule 2), before the load",
            refused(lambda: run_backend_ext(env6)) and made.count("refuse") == 0, "")
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("command", nargs="?",
                    choices=("hashes", "gver-trial", "render-ids", "render-ids-iv", "backend-ext"))
    ap.add_argument("--model-dir", default=None)
    ap.add_argument("--tokenizer-dir", default=None)
    ap.add_argument("--ids-dir", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--pi-date", default=None)
    ap.add_argument("--root", default=None)
    ap.add_argument("--report", default=None)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--ruling", action="append", default=[], metavar="PAUSE_ID=PATH")
    ap.add_argument("--smoke", type=int, default=None)
    a = ap.parse_args(argv)
    if a.selftest:
        return cmd_selftest()
    stage_only = [f for f, given in (("--root", a.root is not None), ("--report", a.report is not None),
                                     ("--resume", a.resume), ("--ruling", bool(a.ruling)),
                                     ("--smoke", a.smoke is not None)) if given]
    if a.command != "backend-ext" and stage_only:
        ap.error(f"{', '.join(stage_only)}: backend-ext's options only")
    if a.command == "backend-ext":
        if a.model_dir or a.tokenizer_dir or a.ids_dir or a.out or a.pi_date:
            ap.error("backend-ext loads from the model manifest's instruct path and takes no folder options")
        rulings = {}
        for item in a.ruling:
            pid, sep, path = item.partition("=")
            if not sep or not pid or not path:
                ap.error(f"--ruling takes PAUSE_ID=PATH, not {item!r}")
            if pid in rulings:
                ap.error(f"--ruling names {pid} twice")
            rulings[pid] = path
        return cmd_backend_ext(a.root, a.report, a.resume, rulings, a.smoke)
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
