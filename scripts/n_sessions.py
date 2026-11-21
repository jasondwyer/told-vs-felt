#!/usr/bin/env python3
"""PROPOSAL-n driver (n v0.2 §8 step 6; the seat's answers of 2026-11-15, §5).

At the n BUILD it wires:

  --selftest   every valence_core.n module's model-free self-test and this driver's checks; "  N/N n selftest checks
               pass", exit 0 iff all pass. Dispatched before any command. The HF backend's cases
               (``valence_core.n.hftiny``: a tiny OLMo-2 built from a config, no weights) run where torch and
               transformers are present -- the box -- and are skipped, and counted as skipped, elsewhere. It writes
               only under a fresh temporary directory outside the repository and reads only committed files: BK's
               under data/n/bk, the ids under data/n/ids, the model manifest, the box's characterization (its
               artifact data/olmo/determinism_base_h100-sxm.json and its raw), LOCK-n.md, and G-VEC's and G-CAL-n's
               outputs of record (data/n/gvec, data/n/gcal); nothing under data/mf3 or any ckpt or reports directory.
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
                    setting (rule 2); numpy's stream known answer; each --ruling a file; then a STAGE line (the
                    stage, its label convention, its root and its report), after a smoke's SMOKE line;
                 2. the weights of record: the committed model manifest's instruct entry (the working copy HEAD's
                    bytes), its folder holding exactly its files at their byte counts; a WEIGHTS line; and the driver
                    of record: a run of record runs only HEAD's committed bytes of this file (the box answers of
                    2026-11-18, §2 item 5), a smoke any, its sha256 printed either way; a DRIVER line;
                 3. the ids of record; the environment's provenance bridged to the characterization (R6) before the
                    load; the stage identity; what is on disk checked as the runner checks it (a resume's identity,
                    its pauses and rulings); BK's d = 0 floor table, BK's d = 0 values for the stage's sessions
                    (``bk_d0_reads``) and every candidate's ids checked;
                 4. G-VER on the committed ids, the tokenizer alone loaded (local files only), decoding as
                    gver-trial does; a STOP returns 1 before the weights load (Code's reading: at backend-ext the
                    raw is the STOP's record; no stage report);
                 5. the load from the entry's path; the adapter's own provenance must hash as the environment's did;
                 6. the 24 reads: N1-V d = 0, each with its fresh re-computation (``dose-rule``), through the BUILD's
                    runner and 5(f) primitive into the stage's cells, the report at the end;
                 7. on COMPLETE: the distribution (``discordance``: |margin - fresh_margin| as ``absdiff`` in nats
                    and its ratio to the scale as ``rel``, each as min, quartiles, median and max -- the seat's answers
                    of 2026-11-18, third sitting, §1.4 -- with the absdiff's p90 beside (R8); each label's |logprob -
                    fresh_logprob| as median and max, the max R3's bound; the counts above TAU and TAU/4 -- fidelity
                    values, never a margin); then the seat's two aggregate lines (the answers of 2026-11-18, fourth
                    sitting, §2.3; ``bk_compare``): |the read's cached margin - BK's recorded d = 0 margin for the
                    same session| over the sessions compared, and |the read's cached log p - BK's recorded value|
                    per label, S and U, over the values compared, with the two labels pooled beside (R8), each as
                    median and max with its count -- discordances, never a margin or a value, nothing per session;
                    BK's value for a session (of any cell, floor or not) is its one d = 0 "none" read for the
                    session's own cell and run, with the session's cues; the in-band
                    count (the floor reads' fresh values against the vanilla score: counts only); the comparison
                    (``label_counts``): per candidate, the floor sessions whose S and U values on the vanilla forward
                    both match BK's ``reduced.json`` within half a unit of BK's last decimal plus the bound (R3),
                    printed as one count of 40 per candidate with, beside it, the median absolute difference over
                    its 80 values (both labels, the 40 floor sessions; the seat's answers of 2026-11-18, §5.5),
                    and nothing else -- no value, no margin, nothing per session; nothing of it is written.
               Exit 0 iff the reads are COMPLETE and the comparison ran; a PAUSE ends the invocation with the report
               (the seat adjudicates; ``--resume`` with ``--ruling PAUSE_ID=PATH`` continues, skip-only).
               Code's readings for the BACKEND extension, declared (each flagged in its entry for the seat, which
               accepted R7 and R8 at its fourth sitting, §5; R8's last sentence, added in v2g, is pending it; R1-R6
               are backend-ext's, R7 is backend-ext-2's and R8 the printed extras' in both):
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
                 R7 backend-ext-2's stage identity keeps ``stage`` "backend-ext" (``schema.STAGES``' pre-lock kind:
                    no lock, dose map, direction or bound) and differs from the first stage's in ``label_convention``
                    alone; "backend-ext-2" names its root, its report and its command. Adding a stage to the schema
                    would move the package digest, and the first stage's resume needs the digest its report was
                    written under;
                 R8 the distribution's quantiles are numpy's default (linear), the median ``np.median``. Beside §1.4's
                    list it prints the absdiff's p90 (printed before the list was set), label's median beside its
                    max, and the counts of reads and of finite reads, the list's denominators. Of the same kind (v2g):
                    beside §2.3 (b)'s per-label figures, the two labels pooled (median, max and count), as the
                    comparison's medians pool them -- a printed figure that binds nothing.
  backend-ext-2  ADDENDUM-n2 §4.1's second stage, on the box, run only when A-n1 §2's comparison names a candidate
               other than "bare": the same 24 reads under ``--convention NAME``, that candidate, into the stage's own
               root and report (data/n/ckpt/backend-ext-2, data/n/reports/backend-ext-2.json), with the fidelity rule
               as the first run carried it (p0 = 0 of 2,400 and no ceiling). The first stage's root and report are
               kept, and nothing is written to either: for a run of record, before the load, its report must be on
               disk, valid, COMPLETE with all 24 reads planned and obtained, under "bare", with a stage identity equal
               to this stage's in every field but the convention -- the same package, closure, weights, backend, pod,
               rendering and fidelity rule -- and each cell file its report records must hash to that record; the
               report's sha256 is printed. The same steps 1-6 as backend-ext, with the STAGE line naming
               backend-ext-2; then on COMPLETE the distribution and §2.3's two aggregate lines (step 7) alone, with
               no in-band count and no comparison. Exit 0 iff the reads are COMPLETE and every one is finite; a PAUSE
               as backend-ext's. ``--smoke``, ``--resume`` and ``--ruling`` as backend-ext's; a smoke is not checked
               against the first stage.
               Both stages are COMPLETE (6e3474d, 9f64305). The schema follow-up (ADDENDUM-n2 §6.3 (3)) adds
               ``alpha``, ``ceiling`` and ``median_rel`` to the fidelity rule and ``fidelity_ceiling_exceeded`` to the
               counters with no version marker (Code's reading, R10, for the seat), so the two stages' committed
               reports and cells no longer pass this package's checks: a resume or a re-print of either is refused
               here ("not a valid report"), and re-reading them needs the package as it stood at 9f64305.
  gvec         G-VEC (n v0.2 §8 step 7; the G-VEC paragraph of n §3; ``valence_core.n.gvec``, its module docstring
               for what it computes and Code's readings G1-G14), on the box, one invocation of about 1,900 unsteered
               forwards. Refusals first, as the BACKEND extension's: the out folder must not exist (G-VEC never
               resumes), nor its staging folder (``.gvec.staging`` beside it, which only a hard stop leaves); the pod,
               the cuBLAS setting, the stream known answer; the weights; the driver, HEAD's committed bytes for a run
               of record. Then, before the load: the ids of record ((iv); G13), every record's ids_sha re-derived and
               the longest input held to the window; each passage record held to the corpus of record
               (``data/n/passages.jsonl``, its sha256 pinned) and the corpus's composition (BK's eight states, 56
               each, 96 neutral); A3's frozen inputs and rule-18 hygiene (``scripts/box_e0_corpus.py``), the (iv)
               render's record of A3 (the input digests, the code's sha256s, the contexts' digest, each context
               record's place and texts), and A3's axis order against the named rows'; the R6 bridge. The load and its
               provenance, recorded whole; ``gvec.compute`` (R at 31 and 32 over positions 1..n, the convention of
               record, the diagnostic block beside it, and the site, or the STOP; v at both, and v under an uncentred
               U; A3's family, its fit-only family and R_ℓ at both; the cosines); the outputs into data/n/gvec/ --
               built in the staging folder and renamed into place -- each file's sha256 printed. ``--smoke N``
               (1..96): the first N neutral passages and the first N contexts in A3's order into ``--out``, a new
               folder outside the repository, R and R_ℓ at both indices, with the diagnostic block over its passages,
               its two token counts and the convention in its record (Code's reading, beside the seat's §1.3 "the
               smoke prints the same lines"), never of record; on the box it is the first run of the HF forward
               seam, before the run of record. Exit 0 on PASS (or a smoke), 2 on the R check's STOP (the record
               alone, with the diagnostic block, for the PI on the seat's stated default: the second sitting,
               §1.5): a later run needs data/n/gvec/ moved aside first.
  render-ids-v  ADDENDUM-n1 §1.2 (v) (``ids.render_v``): G-CAL-n's 48 prompts, ``gcal.plan`` over the (iii) file's
               labels and ``gcal.prompt_parts``' two texts, encoded on the laptop in G-DATA's environment (as
               render-ids-iv: the environment and the tokenizer files checked, ``--out`` a new folder outside the
               repository, ``--pi-date`` the PI's date), extending (i)-(iv)'s manifest. A STOP writes nothing.
  gcal         G-CAL-n (n v0.2 §8 step 8; the G-CAL-n paragraph of n §3; ``valence_core.n.gcal``, its module docstring
               for what it computes and Code's readings GC1-GC23, as the seat ruled them, a33252a and f4b3e73), on the
               box: up to 240 turns generated ids-in, uncached, in the seat's order (+rho, the baseline, +rho/2, the
               gate's reward_f020, -rho), each valence batch's arrival forwards as soon as it is generated; at the
               early read a fail at +rho ends the run as a STOP, and otherwise an incoherent baseline as a PAUSE, with
               no further turn. Refusals first, as G-VEC's (the out folder, its staging folder and its failed-run
               folder, the pod, the cuBLAS setting, the stream known answer, the weights, the driver). Then, before
               the load: the ids of record ((v) present; each of its 48 records the plan's prompt, its user turn's and
               text's sha256s and the v block's template ``gcal.prompt_parts``', its ids_sha re-derived), the longest
               forward held to the generation window; G-VEC's outputs of record (gvec.json and the site's directions
               file HEAD's committed bytes, the record a PASS, the valence and span_reward rows at of_record's
               sha16s); the dose map (a fold into 0 refused, the seat's); the R6 bridge. The load and its provenance,
               its shape and its eos (the (v) render's); ``gcal.compute``; the outputs into data/n/gcal/ -- built in a
               staging folder, each turn logged there as it is generated, and renamed into place; on a failure the
               staging folder is kept as the failed-run folder -- each file's sha256 printed, then the exposure at
               -rho and the gate's line in the lock's form. ``--smoke N`` (1..4): N prompts at +rho and unsteered,
               never -rho or the gate, into ``--out``, a new folder outside the repository, never of record. Exit 0
               on PASS (or a smoke), 2 on a STOP (a hurdle failed at +rho or -rho; at +rho, the early STOP), 3 on a
               PAUSE (at +rho/2 alone, or an incoherent baseline: at the early read, the early PAUSE), each with its
               record, its turns and the dose map, for the seat; a fail at the gate's batch is neither.
  gcal-decode  A-n1 §1.4's one comparison, on the laptop in G-DATA's environment: ``--gcal-dir`` (the record and turns
               copied back from the box) and ``--tokenizer-dir``; each turn's emitted ids decoded here against the
               box's decode; both files' sha256s, the counts, and every difference printed, with its two decoded texts
               and its flags under both decodes.
  gtime        G-TIME-n (n v0.2 §8 step 11; n §3: "Six reads of each kind (steered, shadow, fidelity re-compute,
               capture-on) timed on the box; projections; the cap set by the PI"), on the box, under LOCK-n v0.1, on
               Code's readings GT1-GT17 routed as PINs (the PI's "Build on the PINs", 2026-11-21; the seven starred,
               GT1, GT4, GT8, GT9, GT10, GT12 and GT16, are the seat's before the run:
               results/raw/2026-11-21_n-gtime-starred-seven_code-to-design_STOP.md). ``run_gtime``, one model load;
               everything that needs no model before it:
                 1. refusals: for a run of record the stage's own root, report and artifact (data/n/ckpt/time,
                    data/n/reports/time.json, data/n/gtime/gtime.json), for a smoke (``--smoke N --out DIR``) a new
                    folder outside the repository holding all three; the artifact never written twice;
                    ``--bench-dir`` an existing folder outside the repository on the stage root's filesystem; the
                    pod, the cuBLAS setting, the stream known answer, each --ruling a file; then a STAGE line;
                 2. the weights of record, the lock's; the driver of record as backend-ext's; the ids of record;
                 3. LOCK-n v0.1's inputs (``gtime_lock_inputs``: LOCK-n.md, G-VEC's and G-CAL-n's outputs of record,
                    each HEAD's committed bytes at the lock's sha256s, and the dose map rebuilt from G-VEC's R and
                    R_ell); the R6 bridge; n's backend identifier, the package and its closure, each the lock's; the
                    identity (GT4); the plan's 18 lines; the campaign's counts by the package's own functions, its
                    read plan the lock's; what is on disk, checked as the runner checks it;
                 4. G-VER on the committed ids, the tokenizer alone loaded, before the weights (GT7);
                 5. the load; the 18 reads through the runner and the 5(f) primitive into the stage's cells (GT1,
                    GT2, GT5), the report at the end;
                 6. on COMPLETE the projection (GT8, GT9, GT11): the stage's own records read back, the append
                    benchmark, the artifact checked (``check_gtime``) and written, its figures printed (GT15).
               Exit 0 on COMPLETE; 3 on a PAUSE (the report and no projection, for the seat; ``--resume`` with
               ``--ruling PAUSE_ID=PATH`` continues, skip-only); 2 on G-VER's STOP (no weights load, no read, no
               report) or a refusal before any read; 1 otherwise (GT6). Code's readings for G-TIME-n, the PINs, in
               short (as sent in results/raw/2026-11-21_n-gtime_spec.md §1, but GT9's benchmark and GT11's outputs
               as built, below):
                 GT1 the read set: 18 reads, three on each of six sessions (runs 0, 32, 64, 95, 127 and 159): the
                     shadow re-computed, N1-V valence +1 re-computed, +1/2 on the cached path alone; the kinds are
                     attributes of reads;
                 GT2 the launch order: the six shadows, then the six +1 reads, then the six +1/2 reads;
                 GT3 in the driver alone: valence_core/n/ unchanged, its package and closure LOCK-n v0.1 §18's;
                 GT4 the identity at "time": the lock's values (the LOCK_ pins), the directions {valence}, no cap;
                 GT5 every monitor as the runner has it, the ceiling among them (R14); a fire ends the invocation;
                 GT6 no pass rule; the exits above;
                 GT7 G-VER before the load, not of record (n §8 step 12's is);
                 GT8 the cap's basis: T = N x median(c) + K x median(f) (``GTIME_FORMULA``), the maxima beside, the
                     extension's figures beside and unused;
                 GT9 pod hours beside the cap, outside it: the loads; the I/O by option (i)'s append benchmark (the
                     stage's first +1 record re-keyed 160 times into one cell, ``io_bench``; the line a + b k summed
                     over the campaign's cells), the stage's own per-read I/O beside; the terms not measured, named;
                 GT10 G-READ-n's fits on the laptop's CPU, outside the cap, timed by gread-bench;
                 GT11 the outputs: the report, the shadow cell's JSON, the artifact (``n-gtime-v1``) and the raw,
                     committed before the pod stops; the two steered cells' JSON (the campaign's own reads of six
                     sessions) and every cell's capture arrays stay on the box until the seat rules on them (no looks
                     before the campaign, n §6; the build's review, O2);
                 GT12 no read below d = 0;
                 GT13 no DV takes G-TIME-n's records;
                 GT14 the pod of record; one smoke first, its figures beside and not used;
                 GT15 the printing: the runner's per-read lines and the driver's; durations, no start or finish
                     stamps;
                 GT16 the projections to the PI for the cap at v1.0, the seat's read with v1.0's draft;
                 GT17 the clock: D_n 2026-12-15.
  gread-bench  GT10's benchmark, on the laptop (refused on a pod): probe.py's grouped 10-fold call at its pinned
               settings, ``GREAD_BENCH_CALLS`` times at each of the two contrasts' shapes (320 and 80 rows of
               D_MODEL), on synthetic rows; every call's ms, the count (``gread_counts``) and the projection printed;
               nothing written.

Stages G-VER, the campaign and G-READ-n are wired at their own steps.
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
                     "gvec", "gcal", "guard"):
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
            _gvec_selftest(chk, tmp / "gvec-cmd")
        except BaseException as e:                      # noqa: BLE001
            chk("driver: G-VEC's self-test ran to its end", False, f"{type(e).__name__}: {e}"[:300])
        chk("driver: G-VEC's self-test leaves the environment as it found it", dict(os.environ) == env0, "")
        try:
            _gcal_selftest(chk, tmp / "gcal-cmd")
        except BaseException as e:                      # noqa: BLE001
            chk("driver: G-CAL-n's self-test ran to its end", False, f"{type(e).__name__}: {e}"[:300])
        chk("driver: G-CAL-n's self-test leaves the environment as it found it", dict(os.environ) == env0, "")
        try:
            _gtime_selftest(chk, tmp / "gtime-cmd")
        except BaseException as e:                      # noqa: BLE001
            chk("driver: G-TIME-n's self-test ran to its end", False, f"{type(e).__name__}: {e}"[:300])
        chk("driver: G-TIME-n's self-test leaves the environment as it found it", dict(os.environ) == env0, "")
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
BEXT2_STAGE = "backend-ext-2"       # ADDENDUM-n2 §4.1's second stage: its root's, report's and command's name (R7)
BEXT2_ROOT = REPO / "data" / "n" / "ckpt" / BEXT2_STAGE
BEXT2_REPORT = REPO / "data" / "n" / "reports" / f"{BEXT2_STAGE}.json"
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
                  layer: int = BEXT_LAYER, convention: str = BEXT_CONVENTION) -> dict:
    """The stage identity at backend-ext (``schema.STAGE_IDENTITY_FIELDS``): no lock, dose map, direction or bound;
    the rendering and the label convention as this stage's entry names them (R2, R4, R5); backend-ext-2's the same
    with its ``convention`` (R7). Checked before return."""
    from valence_core.n import schema
    ident = {
        "unit": schema.UNIT, "stage": BEXT_STAGE, "record_schema": schema.RECORD_SCHEMA,
        "proposal_sha256": schema.PROPOSAL_SHA256, "lock_sha256": None, "package_sha256": package_sha256,
        "imported_sha256": dict(imported_sha256), "weights_sha256": weights, "backend_identifier": backend_identifier,
        "pod_id": pod_id, "session_set_sha256": schema.SESSION_SET_SHA256, "rendering_id": rendering_id,
        "label_convention": str(convention), "layer_bk": 32, "layer": int(layer),
        "capture_layers": list(range(int(layer) + 1, int(n_layers))), "n_layers": int(n_layers),
        "d_model": int(d_model), "read_window": schema.MAX_WINDOW, "dose_map": None, "directions": {},
        "fidelity_rule": {"tau": schema.TAU, "p0_count": 0, "p0_n": 2400, "cadence": 160,
                          "sample_key": "n-fid|{s}", "sample_rule": BEXT_SAMPLE_RULE, "alpha": BEXT_ALPHA,
                          "ceiling": None, "median_rel": None},       # pre-lock: no C and no median (ADDENDUM-n2)
        "identity_bound": None,
    }
    schema.check_stage_identity(ident)
    return ident


def five(x) -> dict:
    """min, quartiles, median and max of a non-empty array: numpy's default (linear) quantiles, the median
    ``np.median`` (R8)."""
    import numpy as np
    return {"min": float(np.min(x)), "q1": float(np.quantile(x, 0.25)), "median": float(np.median(x)),
            "q3": float(np.quantile(x, 0.75)), "max": float(np.max(x))}


def discordance(records) -> dict:
    """The fresh-versus-cached distribution over the stage's reads (n v0.2 §3 G-ACQ), fidelity values only, never a
    margin: ``absdiff`` is |margin - fresh_margin| in nats (the record's ``absdiff``) and ``rel`` that over the read's
    scale, each as min, quartiles (``q1``, ``q3``), median and max (the seat's answers of 2026-11-18, third sitting,
    §1.4), with the absdiff's ``p90`` beside (R8); ``label`` each label's |logprob - fresh_logprob| (S and U, two per
    read) as median and max, the max being R3's bound; with the counts above TAU and TAU/4. Every read must carry its
    re-computation."""
    import numpy as np
    fs = [r.get("fidelity") for r in records]
    if not records or any(f is None for f in fs):
        raise SystemExit("a BACKEND-extension read without its re-computation")
    fin = [(r, f) for r, f in zip(records, fs) if f["absdiff"] is not None and f["rel"] is not None]
    out = {"reads": len(records), "finite": len(fin), "absdiff": None, "rel": None, "label": None,
           "exceed_tau": sum(1 for _r, f in fin if f["exceeds_tau"] is True),
           "exceed_tau4": sum(1 for _r, f in fin if f["exceeds_tau4"] is True)}
    if fin:
        a = np.array([float(f["absdiff"]) for _r, f in fin])
        q = np.array([float(f["rel"]) for _r, f in fin])
        g = np.array([abs(float(r[f"logprob_{z}"]) - float(f[f"fresh_logprob_{z}"])) for r, f in fin
                      for z in ("S", "U")])
        out["absdiff"] = dict(five(a), p90=float(np.quantile(a, 0.9)))
        out["rel"] = five(q)
        out["label"] = {"median": float(np.median(g)), "max": float(g.max())}
    return out


def distribution_line(disc: dict, bound: bool = True) -> str:
    """The distribution as printed: one line, the dict's keys sorted. ``bound``: the first stage, whose comparison
    takes label.max as R3's bound, says so; backend-ext-2, which runs no comparison, does not."""
    head = "absdiff and label in nats, rel = absdiff / the read's scale; fidelity values, no margin"
    if bound:
        head += "; R3's bound is label.max"
    return f"discordance over {disc['reads']} reads ({head}): {json.dumps(disc, sort_keys=True)}"


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


def bk_d0_reads(sessions, path=BK_REDUCED) -> dict:
    """BK's recorded d = 0 values for the given sessions, from ``reduced.json``'s OLMo reads (the seat's answers of
    2026-11-18, fourth sitting, §2.3): session_id -> {"margin": float, "S": float, "U": float}, the recorded
    ``margin``, ``logprob_S`` and ``logprob_U``. A session's read, for a session of any cell (floor or not), is the one
    d = 0 read BK records for the session's own cell and run, a "none" read with the session's cues. Two d = 0 reads
    for one cell and run, a session without its read, or a value absent, not a JSON number (a string or a boolean) or
    not finite as recorded is a SystemExit that names the session and quotes no value."""
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    by: dict = {}
    for r in doc["reads"][BK_MEMBER]:
        if float(r["point"]) != 0.0:
            continue
        key = (str(r["cell"]), int(r["run"]))
        if key in by:
            raise SystemExit(f"BK records two d = 0 reads for {key}")
        by[key] = r
    out = {}
    for s in sessions:
        r = by.get((s.bk_cell, s.bk_run))
        if (r is None or r.get("cue_S") != s.cue_S or r.get("cue_U") != s.cue_U
                or r.get("direction_kind") != "none"):
            raise SystemExit(f"{s.session_id}: BK's d = 0 read is missing or not this session's")
        row = {}
        for k, f in (("margin", "margin"), ("S", "logprob_S"), ("U", "logprob_U")):
            v = r.get(f)
            if type(v) not in (int, float) or not math.isfinite(v):         # bool's type is bool, not int
                raise SystemExit(f"{s.session_id}: BK's recorded d = 0 {f} is absent or not a finite number")
            row[k] = float(v)
        out[s.session_id] = row
    return out


def bk_compare(records, bk) -> dict:
    """§2.3's two aggregates over the stage's reads at d = 0 (the seat's answers of 2026-11-18, fourth sitting),
    against ``bk_d0_reads``' table: ``margin``, |the read's cached margin - BK's recorded d = 0 margin for its
    session|, over the sessions compared; ``S`` and ``U``, per label, |the read's cached log p - BK's recorded value|,
    over the values compared; and ``pooled``, the two labels' values together (R8's kind: printed beside, binding
    nothing). Each holds ``median`` (``np.median``), ``max``, ``compared`` and ``of`` (the reads; twice the reads for
    ``pooled``). A value not finite on this box is not compared; with none compared, the median and the max are null.
    A read whose session is not in the table is a SystemExit. Discordances only: no margin and no value leaves this
    function."""
    import numpy as np

    def fin(x) -> bool:
        return x is not None and math.isfinite(float(x))
    m, per = [], {"S": [], "U": []}
    for r in records:
        b = bk.get(r["session_id"])
        if b is None:
            raise SystemExit(f"{r['session_id']}: a read whose session has no BK d = 0 value in the table")
        if fin(r.get("margin")):
            m.append(abs(float(r["margin"]) - b["margin"]))
        for z in ("S", "U"):
            if fin(r.get(f"logprob_{z}")):
                per[z].append(abs(float(r[f"logprob_{z}"]) - b[z]))

    def agg(x: list, of: int) -> dict:
        return {"compared": len(x), "of": of, "median": float(np.median(x)) if x else None,
                "max": float(max(x)) if x else None}
    n = len(records)
    return {"margin": agg(m, n), "S": agg(per["S"], n), "U": agg(per["U"], n),
            "pooled": agg(per["S"] + per["U"], 2 * n)}


def bk_lines(cmp: dict) -> list:
    """§2.3's two lines as printed, after the distribution line: (a) the margins'; (b) the label values', per label
    with the pooled figure beside; each printed whole, keys sorted."""
    labels = {k: cmp[k] for k in ("S", "U", "pooled")}
    return [f"BK's d = 0 margins (the seat's answers of 2026-11-18, fourth sitting, §2.3 (a); |cached margin - BK's "
            f"recorded margin| in nats over the sessions compared; a discordance, no margin): "
            f"{json.dumps(cmp['margin'], sort_keys=True)}",
            f"BK's d = 0 label values (§2.3 (b); |cached log p - BK's recorded value| in nats over the values "
            f"compared, per label, the two pooled beside (R8)): {json.dumps(labels, sort_keys=True)}"]


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


def first_stage_check(first_report: Path, first_root: Path, ident: dict) -> str:
    """backend-ext-2 follows the first stage (ADDENDUM-n2 §4.1): its report on disk and valid, COMPLETE with all its
    reads planned and obtained, under "bare", and its stage identity this stage's in every field but the convention
    (R7); each cell file it records hashing to its record. Returns the report's sha256. Nothing is written to the
    first stage's root or report."""
    import hashlib

    from valence_core.n import cells, schema
    p = Path(first_report)
    if not p.is_file():
        raise SystemExit("backend-ext-2 follows the first stage: the first stage's report is not on disk")
    raw = p.read_bytes()
    rep = cells.read_json(p)
    try:
        schema.check_report(rep, where=p.name)
    except schema.SchemaError as e:
        raise SystemExit(f"the first stage's report is not a valid report, at {str(e).split(': ', 1)[0][:160]}")
    per = rep["per_arm"].get(schema.SHADOW_ARM, {})
    if (rep["end_state"] != "COMPLETE" or per.get("obtained") != BEXT_N or per.get("planned") != BEXT_N
            or rep["stage_identity"]["label_convention"] != BEXT_CONVENTION):
        raise SystemExit(f"backend-ext-2 follows the first stage: its report is not a COMPLETE run of the "
                         f"{BEXT_N} reads under {BEXT_CONVENTION!r}")
    diff = sorted(k for k in set(ident) | set(rep["stage_identity"])
                  if k != "label_convention" and rep["stage_identity"].get(k) != ident.get(k))
    if diff:
        raise SystemExit(f"the first stage was run under another stage identity ({diff}): backend-ext-2 runs as the "
                         f"first run carried it")
    for name, rec in sorted(rep["cells"].items()):
        cp = Path(first_root) / name
        if not cp.is_file() or hashlib.sha256(cp.read_bytes()).hexdigest() != rec["json_sha256"]:
            raise SystemExit(f"the first stage's cell {name} is absent or does not hash to its report's record")
    return hashlib.sha256(raw).hexdigest()


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
    bk_reads: Callable                  # (the stage's sessions) -> ``bk_d0_reads``' table (§2.3)
    pod: Callable                       # () -> the pod id or None
    driver: Callable                    # () -> (this driver's bytes as run, HEAD's committed bytes of its path | None)
    shape: tuple = (N_LAYERS, D_MODEL, BEXT_LAYER)
    root: Path = BEXT_ROOT
    report: Path = BEXT_REPORT
    root2: Path = BEXT2_ROOT
    report2: Path = BEXT2_REPORT
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
                   make_backend=_hf_backend, bk_table=bk_d0_floor, bk_reads=bk_d0_reads, pod=m_resume.pod_id,
                   driver=driver_bytes)


def run_backend_ext(env: BextEnv, *, root=None, report=None, resume: bool = False, rulings=None,
                    smoke: int | None = None, convention: str | None = None) -> int:
    """The stage, in order: refusals; the weights; the ids and the identity; what is on disk; the comparison's inputs
    and BK's d = 0 values for the stage's sessions; G-VER; the load and the bridge again; the reads; the distribution
    and §2.3's two aggregate lines; the comparison. Everything that needs no model happens before the load. With
    ``convention`` -- a candidate other than "bare" -- it is backend-ext-2 (ADDENDUM-n2 §4.1; R7): its own root and
    report, the first stage's report checked before the load for a run of record, and on COMPLETE the distribution
    and the two lines alone."""
    from valence_core.m import resume as m_resume
    from valence_core.m.keys import stream_known_answer
    from valence_core.n import cells, guard, ids, runner, schema
    rulings = dict(rulings or {})
    say = env.printer
    second = convention is not None
    others = [n for n, _t in ids.CANDIDATES if n != BEXT_CONVENTION]
    if second and convention not in others:
        raise SystemExit(f"backend-ext-2 runs under a candidate other than {BEXT_CONVENTION!r} "
                         f"({', '.join(others)}), not {convention!r} (ADDENDUM-n2 §4.1)")
    conv = str(convention) if second else BEXT_CONVENTION
    stage_name = BEXT2_STAGE if second else BEXT_STAGE
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
        root_p = guard.refuse_out(Path(env.root2 if second else env.root))
        report_p = guard.refuse_out(Path(env.report2 if second else env.report))
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
        say(f"SMOKE: {smoke} of the {BEXT_N} reads"
            + ("" if second else f" and {smoke} floor sessions") + ", outside the repository; never of record")
    say(f"STAGE {stage_name}: label convention {conv}; root {_shown(root_p)}, report {_shown(report_p)}")
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
                          n_layers=n_layers, d_model=d_model, layer=layer, convention=conv)
    plan = bext_plan(ss)[:smoke] if smoke is not None else bext_plan(ss)
    prior_state(root_p, report_p, ident, plan, resume, rulings)
    if second and smoke is None:
        fsha = first_stage_check(Path(env.report), Path(env.root), ident)
        say(f"the first stage's report: {_shown(Path(env.report).resolve())}, sha256 {fsha}: COMPLETE at {BEXT_N} of "
            f"{BEXT_N} under {BEXT_CONVENTION!r}, its stage identity this stage's but for the convention, its cells "
            f"as it records them")
    floor_all = [s for s in ss if s.is_floor]
    bk = env.bk_table(floor_all)
    bkr = env.bk_reads([p.session for p in plan])
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
                                label_ids=cands[conv], backend=backend, directions={}, alpha=BEXT_ALPHA,
                                hour_cap_ms=None, load_ms=load_ms, rulings=rulings, printer=say)
    rpt = runner.run(inputs, plan, resume=resume)
    if rpt["end_state"] != "COMPLETE":
        if second:
            say(f"BACKEND extension ({stage_name}): {rpt['end_state']}; no distribution until it completes")
        else:
            say(f"BACKEND extension: {rpt['end_state']}; no distribution and no comparison until it completes")
        return 1
    cell, _caps = cells.load_cell(root_p, schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE,
                                  identity=ident)
    disc = discordance(cell["records"])
    say(distribution_line(disc, bound=not second))
    for line in bk_lines(bk_compare(cell["records"], bkr)):
        say(line)
    if disc["label"] is None or disc["finite"] != disc["reads"]:
        say("a read has no finite discordance" + ("" if second else ": no comparison"))
        return 1
    if second:
        return 0
    score = vanilla_score(backend)
    agree, of = in_band(score, cell["records"], {s.session_id: s for s in ss}, ids_of)
    say(f"in-band: {agree} of {of} floor reads' fresh values, both labels, equal the comparison's vanilla score")
    counts = label_counts(score, floor, ids_of, cands, bk, float(disc["label"]["max"]), int(ident["read_window"]))
    say(counts_line(counts, len(floor)))
    say(("SMOKE, never of record: " if smoke is not None else "") + convention_line(counts, len(floor)))
    return 0


def cmd_backend_ext(root=None, report=None, resume: bool = False, rulings=None, smoke: int | None = None,
                    convention: str | None = None) -> int:
    return run_backend_ext(production_env(), root=root, report=report, resume=resume, rulings=rulings, smoke=smoke,
                           convention=convention)


def _shown(p: Path) -> str:
    """A stage path as the STAGE line prints it: relative to the repository when inside it."""
    p = Path(p)
    return p.relative_to(REPO.resolve()).as_posix() if _within(p, REPO.resolve()) else str(p)


def _bext_selftest(chk, tmp: Path) -> None:
    """backend-ext's checks, model-free: R1's draw (a pinned known answer), the plan, the identity, the weights entry
    and folder, R6's bridge against the characterization's recorded provenance, the distribution, BK's half unit and
    d = 0 table, §2.3's BK values and two aggregate lines, the comparison, the vanilla score against the read's fresh
    path, and the command's own flow over the numpy double behind every seam, refusals first; on the box, the vanilla
    score on the HF path too."""
    import hashlib
    import re
    import shutil

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
        "band 33..63; bare; window 4,096; the fidelity rule n §2.1's with G-DATA (vi)'s p0, alpha 0.01, and no "
        "ceiling or median rel",
        ident["stage"] == "backend-ext" and ident["lock_sha256"] is None and ident["dose_map"] is None
        and ident["directions"] == {} and ident["identity_bound"] is None
        and ident["capture_layers"] == list(range(33, 64)) and ident["label_convention"] == "bare"
        and ident["read_window"] == 4096 and (ident["n_layers"], ident["d_model"], ident["layer"]) == (64, 5120, 32)
        and ident["fidelity_rule"] == {"tau": schema.TAU, "p0_count": 0, "p0_n": 2400, "cadence": 160,
                                       "sample_key": "n-fid|{s}", "sample_rule": BEXT_SAMPLE_RULE, "alpha": 0.01,
                                       "ceiling": None, "median_rel": None}, "")

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
    chk("driver: the discordance distribution, a known answer: the absdiff's and rel's min, quartiles, median and max "
        "(numpy's linear quantiles; §1.4), the absdiff's p90, and each label's |logprob - fresh_logprob| (8 values)",
        d["reads"] == 4 and d["finite"] == 4 and d["exceed_tau"] == 1 and d["exceed_tau4"] == 2
        and near(d["absdiff"]["min"], 0.0) and near(d["absdiff"]["q1"], 0.0075)
        and near(d["absdiff"]["median"], 0.015) and near(d["absdiff"]["q3"], 0.0275)
        and near(d["absdiff"]["p90"], 0.041) and near(d["absdiff"]["max"], 0.05)
        and near(d["rel"]["min"], 0.0) and near(d["rel"]["q1"], 0.00075) and near(d["rel"]["median"], 0.0015)
        and near(d["rel"]["q3"], 0.0065) and near(d["rel"]["max"], 0.02)
        and near(d["label"]["max"], 0.21) and near(d["label"]["median"], 0.0), d)
    chk("driver: ...and exactly those keys: the absdiff's six, rel's five, label's two, nothing per read",
        sorted(d) == ["absdiff", "exceed_tau", "exceed_tau4", "finite", "label", "reads", "rel"]
        and sorted(d["absdiff"]) == ["max", "median", "min", "p90", "q1", "q3"]
        and sorted(d["rel"]) == ["max", "median", "min", "q1", "q3"] and sorted(d["label"]) == ["max", "median"], d)
    odd = five([0.3, 0.1, 0.2, 0.5, 0.4])
    chk("driver: ...an odd count, in no order: the quartiles fall on values (0.2 and 0.4), the median the middle one",
        all(near(odd[k], v) for k, v in {"min": 0.1, "q1": 0.2, "median": 0.3, "q3": 0.4, "max": 0.5}.items()), odd)
    dl = discordance([frec(0.0, 0.0, False, False, fs=-10.1, fu=-12.2),
                      frec(0.0, 0.0, False, False, fs=-10.3, fu=-12.4)])
    chk("driver: ...label's median is the middle of its values, not their least: 0.1, 0.2, 0.3 and 0.4 give 0.25",
        near(dl["label"]["median"], 0.25) and near(dl["label"]["max"], 0.4), dl["label"])
    unit = "absdiff and label in nats, rel = absdiff / the read's scale; fidelity values, no margin"
    chk("driver: the distribution line: its units, then (the first stage's) R3's bound, then the dict, keys sorted",
        distribution_line(d) == f"discordance over 4 reads ({unit}; R3's bound is label.max): "
        + json.dumps(d, sort_keys=True), distribution_line(d)[:140])
    chk("driver: ...backend-ext-2's, which runs no comparison, names no bound",
        distribution_line(d, bound=False) == f"discordance over 4 reads ({unit}): " + json.dumps(d, sort_keys=True),
        distribution_line(d, bound=False)[:140])
    chk("driver: the two stages' roots and reports, as the STAGE line shows them, are their four repository paths",
        (_shown(BEXT_ROOT), _shown(BEXT_REPORT), _shown(BEXT2_ROOT), _shown(BEXT2_REPORT))
        == ("data/n/ckpt/backend-ext", "data/n/reports/backend-ext.json", "data/n/ckpt/backend-ext-2",
            "data/n/reports/backend-ext-2.json"), "")
    d2 = discordance([frec(0.01, 0.001, False, False), frec(None, None, None, None)])
    chk("driver: a read whose re-computation is not finite is counted, not measured", d2["reads"] == 2
        and d2["finite"] == 1 and near(d2["absdiff"]["max"], 0.01) and near(d2["rel"]["min"], 0.001), d2)
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

    # §2.3's two aggregate lines (the seat's answers of 2026-11-18, fourth sitting)
    try:
        r24, r_all, r_err = bk_d0_reads(b1), bk_d0_reads(ss), ""
    except SystemExit as e:                                 # a FAIL line below, not an abort of the self-test
        r24, r_all, r_err = {}, {}, str(e)[:80]
    chk("driver: BK's d = 0 values for backend-ext's 24 sessions from the committed reduced.json (§2.3): one row "
        "per session, its recorded margin, S and U, each finite, the margin S - U as recorded; floor sessions and "
        "others among them; and a row for every session of the set",
        sorted(r24) == sorted(s.session_id for s in b1)
        and all(set(v) == {"margin", "S", "U"} and all(math.isfinite(x) for x in v.values())
                and abs(v["margin"] - (v["S"] - v["U"])) <= 1e-9 for v in r24.values())
        and any(s.is_floor for s in b1) and any(not s.is_floor for s in b1)
        and sorted(r_all) == sorted(s.session_id for s in ss),
        (len(r_all), sum(1 for s in b1 if s.is_floor), r_err))
    mix = [s for s in ss if s.is_floor][:2] + [s for s in ss if not s.is_floor][:2]
    brow = [{"cell": s.bk_cell, "run": s.bk_run, "point": 0.0, "direction_kind": "none", "cue_S": s.cue_S,
             "cue_U": s.cue_U, "logprob_S": -9.5, "logprob_U": -11.25, "margin": 1.75} for s in mix]
    brest = [dict(r, point=0.5, margin=7.0, logprob_S=-1.0) for r in brow] + [dict(brow[0], cell="ste_b0", margin=8.0)]
    chk("driver: ...the session's own d = 0 read only (not another dose's, not another cell's at the same run), in any "
        "cell (two floor sessions, two others), its values as recorded",
        bk_d0_reads(mix, synth(brow + brest)) == {s.session_id: {"margin": 1.75, "S": -9.5, "U": -11.25} for s in mix},
        "")

    def bk_refusal(fn) -> str:
        try:
            fn()
        except SystemExit as e:
            return str(e) or "(empty)"
        return ""

    def with0(**kw) -> list:
        return [dict(brow[0], **kw)] + brow[1:]

    def text0(new: str) -> Path:                        # the first row's logprob_S replaced in the file's text
        return synth(brow, lambda t: t.replace('"logprob_S": -9.5', f'"logprob_S": {new}', 1))
    no_margin = [{k: v for k, v in brow[0].items() if k != "margin"}] + brow[1:]
    cases = [brow + brow[1:2], brow[:3], with0(cue_S="Zone Q9"), with0(cue_U="Zone Q9"),
             with0(direction_kind="valenced"), with0(direction_kind="random"), no_margin, with0(logprob_U=None),
             with0(logprob_S="abc"), with0(margin="1.75"), with0(logprob_U=True)]
    msgs = ([bk_refusal(lambda c=c: bk_d0_reads(mix, synth(c))) for c in cases]
            + [bk_refusal(lambda t=t: bk_d0_reads(mix, text0(t))) for t in ("NaN", "-Infinity")])
    chk("driver: ...it refuses two d = 0 reads of a cell and run, a session missing, either cue not the session's, a "
        "d = 0 read that is not a \"none\" read (\"valenced\", \"random\"), a margin absent, and a value null, a "
        "string (\"abc\", \"1.75\"), a boolean, NaN or -Infinity as recorded -- 13 cases, each message quoting no "
        "value",
        len(msgs) == 13 and all(m_ and not any(v in m_ for v in ("9.5", "11.25", "1.75", "Q9", "valenced", "random",
                                                                  "abc", "True", "true", "NaN", "Infinity"))
                                for m_ in msgs), [m_[:60] for m_ in msgs])
    sid24 = [f"toy/{i}" for i in range(24)]
    dl_ = [(i + 1) / 1024 for i in range(23)] + [0.5]
    sg = [1 if i % 2 == 0 else -1 for i in range(24)]
    recs_c = [{"session_id": sid24[i], "margin": 2.0, "logprob_S": -10.0, "logprob_U": -12.0,
               "fidelity": {"fresh_margin": 99.0, "fresh_logprob_S": 0.0, "fresh_logprob_U": 0.0}} for i in range(24)]
    tbl = {sid24[i]: {"margin": 2.0 + sg[i] * dl_[i], "S": -10.0 - 2 * sg[i] * dl_[i],
                      "U": -12.0 - 3 * sg[i] * dl_[i]} for i in range(24)}
    cmp_c = bk_compare(recs_c, tbl)
    chk("driver: §2.3's aggregates, a known answer: |cached margin - BK's| over 24 sessions (median 12.5/1024, not "
        "the mean; max 0.5); |cached log p - BK's| per label over 24 values each, S (median 25/1024; max 1.0) and U "
        "(median 37.5/1024; max 1.5), and the two pooled beside over 48 (median 30/1024; max 1.5); differences of "
        "either sign; the fresh path not read",
        cmp_c == {"margin": {"compared": 24, "of": 24, "median": 12.5 / 1024, "max": 0.5},
                  "S": {"compared": 24, "of": 24, "median": 25 / 1024, "max": 1.0},
                  "U": {"compared": 24, "of": 24, "median": 37.5 / 1024, "max": 1.5},
                  "pooled": {"compared": 48, "of": 48, "median": 30 / 1024, "max": 1.5}}, cmp_c)
    recs_n = [dict(recs_c[0], margin=None, logprob_S=None, logprob_U=None), dict(recs_c[1], margin=float("nan")),
              dict(recs_c[2], logprob_U=float("inf"))] + recs_c[3:]
    cmp_n = bk_compare(recs_n, tbl)
    cmp_e = bk_compare([recs_n[0]], tbl)
    none1 = {"compared": 0, "of": 1, "median": None, "max": None}
    chk("driver: ...a value not finite on this box is not compared and the counts say so (22 of 24 margins, 23 of 24 "
        "S values, 22 of 24 U values, 45 of 48 pooled); with nothing compared the median and the max are null; a read "
        "whose session is not in the table is refused",
        [(cmp_n[k]["compared"], cmp_n[k]["of"]) for k in ("margin", "S", "U", "pooled")]
        == [(22, 24), (23, 24), (22, 24), (45, 48)]
        and cmp_e == {"margin": none1, "S": none1, "U": none1,
                      "pooled": {"compared": 0, "of": 2, "median": None, "max": None}}
        and refused(lambda: bk_compare([dict(recs_c[0], session_id="toy/x")], tbl)), (cmp_n, cmp_e))
    chk("driver: §2.3's two lines: (a) the margins', (b) the label values' per label with the pooled figure beside, "
        "each printed whole, keys sorted",
        bk_lines(cmp_c) == [
            "BK's d = 0 margins (the seat's answers of 2026-11-18, fourth sitting, §2.3 (a); |cached margin - BK's "
            "recorded margin| in nats over the sessions compared; a discordance, no margin): "
            + json.dumps(cmp_c["margin"], sort_keys=True),
            "BK's d = 0 label values (§2.3 (b); |cached log p - BK's recorded value| in nats over the values "
            "compared, per label, the two pooled beside (R8)): "
            + json.dumps({"S": cmp_c["S"], "U": cmp_c["U"], "pooled": cmp_c["pooled"]}, sort_keys=True)]
        and bk_lines(cmp_c)[0].endswith('{"compared": 24, "max": 0.5, "median": 0.01220703125, "of": 24}')
        and bk_lines(cmp_c)[1].endswith('"pooled": {"compared": 48, "max": 1.5, "median": 0.029296875, "of": 48}}'),
        [x[-70:] for x in bk_lines(cmp_c)])
    chk("driver: the production environment reads BK's d = 0 values by bk_d0_reads and the floor table by bk_d0_floor",
        production_env().bk_reads is bk_d0_reads and production_env().bk_table is bk_d0_floor, "")

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

        def cached_reads(be, sess, conv):                   # §2.3's BK stand-in: the cached path's values
            ls_, lu_ = labs[conv]
            out = {}
            for s in sess:
                pre = be.prefill(by_flow[s.session_id], [], [])
                v = {z: math.fsum(primitive.score_cached(pre, be.continue_label(pre, li), li))
                     for li, z in ((ls_, "S"), (lu_, "U"))}
                out[s.session_id] = {"margin": v["S"] - v["U"], "S": v["S"], "U": v["U"]}
            return out

        def bk_printed(lines) -> list:                      # every §2.3 pair printed: (index of (a), (a), (b))
            out = []
            for i, x in enumerate(lines[:-1]):
                if x.startswith("BK's d = 0 margins (") and lines[i + 1].startswith("BK's d = 0 label values ("):
                    out.append((i, json.loads(x[x.index("): {") + 3:]),
                                json.loads(lines[i + 1][lines[i + 1].index("): {") + 3:])))
            return out

        def zero(n) -> dict:
            return {"compared": n, "of": n, "median": 0.0, "max": 0.0}

        def zeros(n) -> tuple:                              # both lines at 0.0 over n reads: (a), then (b)
            return zero(n), {"S": zero(n), "U": zero(n), "pooled": zero(2 * n)}
        bk_seen: dict = {}                                  # tag -> the session ids each bk_reads call was given

        def env_for(tag, bk_conv="bare", **over):
            be = testing.CausalDouble(fresh_bias=(5, 0.3))
            lines: list = []

            def mk(p, prov=None):
                made.append(tag)
                return StubAdapter(prov or prov_t)

            def bk_seam(sess):
                bk_seen.setdefault(tag, []).append([s.session_id for s in sess])
                return cached_reads(be, sess, bk_conv)
            base = dict(weights=lambda: {"repo": "toy", "revision": "0" * 12, "sha256": "5" * 64, "n_files": 1,
                                         "path": "(toy)"},
                        load_sessions=lambda: list(fss), load_ids=lambda: loaded_t,
                        gver=lambda s_, l_, p_: {"status": "PASS", "sessions": len(s_)},
                        env_provenance=lambda p: dict(prov_t), make_adapter=mk, adapter_shape=lambda a: (6, 12),
                        make_backend=lambda a: be, bk_table=lambda f_: cached_table(be, f_),
                        bk_reads=bk_seam,
                        pod=lambda: CHARACTERIZED_POD, driver=lambda: (b"drv", b"drv"), shape=(6, 12, 2),
                        root=tmp / tag / "root", report=tmp / tag / "report.json", root2=tmp / tag / "root2",
                        report2=tmp / tag / "report2.json", printer=lines.append)
            base.update(over)
            for k in ("root", "report", "root2", "report2"):            # a self-test writes only under tmp
                if _within(Path(base[k]).resolve(), REPO.resolve()):
                    raise SystemExit(f"a self-test environment points {k} into the repository: {base[k]}")
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
            and printed.get("absdiff", {}).get("max", 1.0) < 0.01, (gap, printed.get("absdiff")))
        chk("driver: ...the STAGE line first, then the distribution line in §1.4's form, the dict printed whole",
            lines1[0] == f"STAGE backend-ext: label convention bare; root {env1.root.resolve()}, report "
                         f"{env1.report.resolve()}"
            and disc_line == distribution_line(discordance(recs1)), (lines1[:1], disc_line[:100]))
        chk("driver: ...in-band: every floor read's fresh values equal the vanilla score",
            "in-band: 24 of 24 floor reads' fresh values, both labels, equal the comparison's vanilla score" in lines1,
            "")
        p1 = bk_printed(lines1)
        chk("driver: ...§2.3's two lines directly after the distribution line and before the in-band count; with BK's "
            "stand-in the cached path's own values, 0.0 over the 24 sessions and the 48 label values (the cached "
            "margin and log p are what is compared, not the fresh path's)",
            len(p1) == 1 and disc_line in lines1 and p1[0][0] == lines1.index(disc_line) + 1
            and (p1[0][1], p1[0][2]) == zeros(24) and lines1[p1[0][0] + 2].startswith("in-band: "), p1[:1])
        chk("driver: ...BK's d = 0 values are asked for once, for the plan's 24 sessions in launch order",
            bk_seen.get("run") == [[s.session_id for s in fss]], [len(x) for x in bk_seen.get("run", [])])
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

        # backend-ext-2 (ADDENDUM-n2 §4.1; R7), after the first stage above (env1's root and report, COMPLETE)
        firsts = [Path(env1.report)] + [Path(env1.root) / n for n in sorted(os.listdir(env1.root))]
        before = {p: p.read_bytes() for p in firsts}
        first_ident = cells.read_json(Path(env1.report))["stage_identity"]
        two = dict(root=env1.root, report=env1.report)
        env7, lines7 = env_for("second", bk_conv="space", root2=tmp / "second" / "root2",
                               report2=tmp / "second" / "rep2.json", **two)
        rc7 = run_backend_ext(env7, convention="space")
        cell7, _c7 = cells.load_cell(env7.root2, schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE)
        rep7 = cells.read_json(Path(env7.report2))
        chk("driver: backend-ext-2 under 'space': COMPLETE, 24 records in its own root and report, under the space "
            "labels, one load; its identity the first stage's but for the convention (R7)",
            rc7 == 0 and len(cell7["records"]) == BEXT_N and made.count("second") == 1
            and all(r["label_ids_S"] == [6, 9, 17] and r["label_ids_U"] == [6, 11, 2] for r in cell7["records"])
            and rep7["end_state"] == "COMPLETE" and rep7["stage_identity"]["label_convention"] == "space"
            and rep7["stage_identity"]["stage"] == "backend-ext"
            and {k: v for k, v in rep7["stage_identity"].items() if k != "label_convention"}
            == {k: v for k, v in first_ident.items() if k != "label_convention"}, rep7["end_state"])
        chk("driver: ...the first stage's root and report are byte for byte as they were",
            all(p.read_bytes() == b for p, b in before.items())
            and sorted(os.listdir(env1.root)) == sorted(p.name for p in firsts[1:]), "")
        unit2 = "absdiff and label in nats, rel = absdiff / the read's scale; fidelity values, no margin"
        fsha1 = hashlib.sha256(Path(env1.report).read_bytes()).hexdigest()
        chk("driver: ...it prints its STAGE line, the first stage's report's sha256, and the distribution with no "
            "bound named; no in-band count and no comparison",
            lines7[0].startswith("STAGE backend-ext-2: label convention space; root ")
            and any(x.startswith("the first stage's report: ") and f"sha256 {fsha1}: COMPLETE at 24 of 24" in x
                    for x in lines7)
            and any(x.startswith(f"discordance over 24 reads ({unit2}): ") for x in lines7)
            and not any(x.startswith(("in-band:", "label convention (")) or "candidate" in x or "R3" in x
                        for x in lines7), lines7[-2:])
        p7 = bk_printed(lines7)
        chk("driver: ...and §2.3's two lines directly after its distribution line, as its last two lines; 0.0 over 24 "
            "sessions and 48 label values against the space labels' cached values",
            len(p7) == 1 and lines7[p7[0][0] - 1].startswith(f"discordance over 24 reads ({unit2}): ")
            and p7[0][0] == len(lines7) - 2 and (p7[0][1], p7[0][2]) == zeros(24), p7[:1])
        chk("driver: ...a second run of backend-ext-2 without --resume is refused before the load",
            refused(lambda: run_backend_ext(env7, convention="space")) and made.count("second") == 1, "")
        rc7b = run_backend_ext(env7, convention="space", resume=True)
        chk("driver: ...a resume of backend-ext-2 after COMPLETE launches nothing and prints the distribution again",
            rc7b == 0 and made.count("second") == 2 and len(cells.load_cell(
                env7.root2, schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE)[0]["records"]) == BEXT_N
            and sum(1 for x in lines7 if x.startswith("discordance over 24 reads")) == 2, "")
        chk("driver: ...and §2.3's two lines again after it", len(bk_printed(lines7)) == 2, "")
        pf_env, lpf = env_for("pausefirst", make_backend=lambda a: testing.CausalDouble(fresh_bias=(9, 2.0)))
        rc_pf = run_backend_ext(pf_env)
        pf_end = cells.read_json(Path(pf_env.report))["end_state"] if Path(pf_env.report).is_file() else None
        chk("driver: a first stage whose labels' second tokens are biased on the fresh path ends PAUSE at the run's "
            "end, says so in its words, and prints no distribution (the case below too)",
            rc_pf == 1 and pf_end == "PAUSE"
            and "BACKEND extension: PAUSE; no distribution and no comparison until it completes" in lpf
            and not any(x.startswith("discordance over") for x in lpf), pf_end)
        env9, lines9 = env_for("pause2", bk_conv="space",
                               make_backend=lambda a: testing.CausalDouble(fresh_bias=(9, 2.0)), **two)
        rc9 = run_backend_ext(env9, convention="space")
        rep9 = cells.read_json(Path(env9.report2)) if Path(env9.report2).is_file() else {}
        chk("driver: backend-ext-2 whose space labels' second tokens are biased on the fresh path ends PAUSE at the "
            "run's end, says so in its own words, and prints no distribution",
            rc9 == 1 and rep9.get("end_state") == "PAUSE"
            and "BACKEND extension (backend-ext-2): PAUSE; no distribution until it completes" in lines9
            and not any(x.startswith("discordance over") for x in lines9), rep9.get("end_state"))
        chk("driver: ...a PAUSE prints no §2.3 lines (the first stage's above, backend-ext-2's here)",
            not bk_printed(lpf) and not bk_printed(lines9), "")
        rc9b = run_backend_ext(env9, convention="space", resume=True, rulings={"p01": str(r_md)})
        rep9b = cells.read_json(Path(env9.report2))
        chk("driver: ...its resume under the ruling: COMPLETE, p01 adjudicated, one distribution line, exit 0; the "
            "first stage's root and report byte for byte as they were",
            rc9b == 0 and rep9b["end_state"] == "COMPLETE" and rep9b["pauses"][0]["adjudicated"] is True
            and sum(1 for x in lines9 if x.startswith("discordance over 24 reads")) == 1
            and all(p.read_bytes() == b for p, b in before.items()), rep9b["end_state"])
        p9 = bk_printed(lines9)
        chk("driver: ...and the resume prints §2.3's two lines once, directly after its distribution line",
            len(p9) == 1 and lines9[p9[0][0] - 1].startswith("discordance over 24 reads"), p9[:1])
        target = by_flow[fss[5].session_id]

        def nan_backend(_a):                        # one read's cached path non-finite: a nonfinite pause at it
            be_n = testing.CausalDouble()
            orig_pre = be_n.prefill

            def nan_prefill(ids, injections, capture_layers):
                pre = orig_pre(ids, injections, capture_layers)
                if list(ids) == target:
                    pre.logits_last = pre.logits_last.copy()
                    pre.logits_last[0] = float("nan")
                return pre
            be_n.prefill = nan_prefill
            return be_n
        for tag, conv_t, last in (("nan2", "space", "a read has no finite discordance"),
                                  ("nan1", None, "a read has no finite discordance: no comparison")):
            env_n, lines_n = env_for(tag, bk_conv=conv_t or "bare", make_backend=nan_backend,
                                     **(two if conv_t else {}))
            rc_n = run_backend_ext(env_n, convention=conv_t)
            rp_n = Path(env_n.report2 if conv_t else env_n.report)
            p_n = cells.read_json(rp_n)["pauses"]
            rc_nb = run_backend_ext(env_n, convention=conv_t, resume=True, rulings={"p01": str(r_md)})
            chk(f"driver: {'backend-ext-2' if conv_t else 'backend-ext'} with one non-finite read: a nonfinite pause "
                f"at it; under its ruling the resume ends COMPLETE, prints the distribution over 23 finite of 24, and "
                f"exits 1 saying \"{last}\"",
                rc_n == 1 and len(p_n) == 1 and p_n[0]["kind"] == "nonfinite" and rc_nb == 1
                and cells.read_json(rp_n)["end_state"] == "COMPLETE" and lines_n[-1] == last
                and any(x.startswith("discordance over 24 reads") and '"finite": 23' in x for x in lines_n),
                lines_n[-1:])
            pn = bk_printed(lines_n)
            chk(f"driver: ...{'backend-ext-2' if conv_t else 'backend-ext'}: its §2.3 lines, printed once, compare "
                f"the finite reads alone: 23 of 24 margins, 23 of 24 per label, 46 of 48 pooled",
                len(pn) == 1 and [(d_["compared"], d_["of"]) for d_ in (pn[0][1], pn[0][2]["S"], pn[0][2]["U"],
                                                                        pn[0][2]["pooled"])]
                == [(23, 24), (23, 24), (23, 24), (46, 48)], pn[:1])
        env10, lines10 = env_for("smoke2", bk_conv="space", root=tmp / "none-root", report=tmp / "none-first.json")
        rc10 = run_backend_ext(env10, root=str(tmp / "smoke2" / "sroot"), report=str(tmp / "smoke2" / "srep.json"),
                               smoke=2, convention="space")
        chk("driver: a backend-ext-2 smoke of 2, no first stage on disk: COMPLETE, 2 records, its SMOKE line (no "
            "floor sessions) before its STAGE line, the distribution and §2.3's lines alone; the first stage is not "
            "checked",
            rc10 == 0 and len(cells.load_cell(tmp / "smoke2" / "sroot", schema.SHADOW_ARM, schema.SHADOW_DIRECTION,
                                              schema.SHADOW_DOSE)[0]["records"]) == 2
            and lines10[0] == "SMOKE: 2 of the 24 reads, outside the repository; never of record"
            and lines10[1].startswith("STAGE backend-ext-2: label convention space; ")
            and any(x.startswith(f"discordance over 2 reads ({unit2}): ") for x in lines10)
            and not any(x.startswith(("in-band:", "label convention (", "the first stage's report:"))
                        for x in lines10), lines10[:2])
        p10 = bk_printed(lines10)
        chk("driver: ...its §2.3 lines over its 2 reads: 0.0 over 2 sessions and 4 label values",
            len(p10) == 1 and (p10[0][1], p10[0][2]) == zeros(2), p10[:1])
        chk("driver: ...and BK's d = 0 values asked for its 2 sessions alone, the plan's first two",
            bk_seen.get("smoke2") == [[fss[0].session_id, fss[1].session_id]],
            [len(x) for x in bk_seen.get("smoke2", [])])
        gv_calls: list = []
        envb, _lb = env_for("bkmiss", bk_reads=lambda s_: bk_d0_reads(s_, synth([])),
                            gver=lambda s_, l_, p_: gv_calls.append(len(s_)) or {"status": "PASS",
                                                                                 "sessions": len(s_)})
        chk("driver: a stage whose BK d = 0 table lacks a session is refused before G-VER and the load (§2.3's table "
            "is read at step 3)",
            refused(lambda: run_backend_ext(envb)) and made.count("bkmiss") == 0 and gv_calls == [], gv_calls)

        def edited(tag, edit, resha=True) -> Path:              # the first stage's report, edited, under tmp
            r = cells.read_json(Path(env1.report))
            edit(r)
            if resha:
                r["stage_identity_sha256"] = schema.identity_sha256(r["stage_identity"])
            out = tmp / f"first-{tag}.json"
            m_resume.atomic_write_json(out, r)
            return out
        cname = schema.cell_filename(schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE)

        def short_arm(planned, obtained):
            def e(r):
                r["per_arm"][schema.SHADOW_ARM] = {"planned": planned, "obtained": obtained,
                                                   "complete": planned == obtained}
                r["cells"][cname] = dict(r["cells"][cname], records=obtained)
            return e
        stale = edited("stale", lambda r: r["stage_identity"].__setitem__("weights_sha256", "7" * 64), resha=False)
        arm23, arm25 = edited("arm23", short_arm(24, 23)), edited("arm25", short_arm(25, 24))
        id_cases = {"weights_sha256": "7" * 64, "package_sha256": "9" * 64,
                    "imported_sha256": {"valence_core/m/resume.py": "8" * 64}, "backend_identifier": "f" * 16,
                    "pod_id": "another-pod", "rendering_id": "8" * 64,
                    "fidelity_rule": dict(first_ident["fidelity_rule"], p0_count=1)}
        id_first = {k: edited(f"id-{k}", lambda r, k=k, v=v: r["stage_identity"].__setitem__(k, v))
                    for k, v in id_cases.items()}
        chk("driver: (the edited first-stage reports below are valid reports -- 23 of 24 and 24 of 25 obtained, "
            "COMPLETE outside the campaign; another value in each identity field -- and the one with a stale identity "
            "sha256 is not)",
            all(not raises(lambda p=p: schema.check_report(cells.read_json(p)), schema.SchemaError)
                for p in [arm23, arm25] + list(id_first.values()))
            and raises(lambda: schema.check_report(cells.read_json(stale)), schema.SchemaError), "")
        bad_root = tmp / "badcell" / "root"
        shutil.copytree(env1.root, bad_root)
        with open(bad_root / cname, "ab") as fh:
            fh.write(b" ")
        (tmp / "emptyroot").mkdir()
        sh_env, _lsh = env_for("short")
        rc_sh = run_backend_ext(sh_env, root=str(tmp / "short" / "sroot"), report=str(tmp / "short" / "srep.json"),
                                smoke=2)
        chk("driver: (a smoke of 2 ends COMPLETE, its report a valid one of 2 reads, the case below)",
            rc_sh == 0 and cells.read_json(tmp / "short" / "srep.json")["per_arm"][schema.SHADOW_ARM]["obtained"] == 2,
            "")
        chk("driver: a first-stage smoke of 2 asks BK's d = 0 values for its 2 sessions alone, the plan's first two "
            "(not the floor table's 24)",
            bk_seen.get("short") == [[fss[0].session_id, fss[1].session_id]],
            [len(x) for x in bk_seen.get("short", [])])

        def refusal(fn) -> str:
            try:
                fn()
            except SystemExit as e:
                return str(e)
            return "no refusal"
        r2 = dict(root2=tmp / "refuse2" / "root2", report2=tmp / "refuse2" / "rep2.json")
        cases2 = {
            "the convention 'bare'": (lambda: run_backend_ext(env_for("refuse2", **r2, **two)[0], convention="bare"),
                                      "runs under a candidate other than 'bare'"),
            "a convention that is no candidate": (lambda: run_backend_ext(env_for("refuse2", **r2, **two)[0],
                                                                          convention="nonesuch"),
                                                  "not 'nonesuch'"),
            "a first stage with no report on disk": (lambda: run_backend_ext(
                env_for("refuse2", root=env1.root, report=tmp / "none.json", **r2)[0], convention="space"),
                "the first stage's report is not on disk"),
            "a first stage that ended PAUSE": (lambda: run_backend_ext(
                env_for("refuse2", root=pf_env.root, report=pf_env.report, **r2)[0], convention="space"),
                "its report is not a COMPLETE run of the 24 reads"),
            "a first stage of fewer than 24 reads (a smoke's report)": (lambda: run_backend_ext(
                env_for("refuse2", root=tmp / "short" / "sroot", report=tmp / "short" / "srep.json", **r2)[0],
                convention="space"), "its report is not a COMPLETE run of the 24 reads"),
            "a first stage whose report is not valid (its identity's sha256 stale)": (lambda: run_backend_ext(
                env_for("refuse2", root=env1.root, report=stale, **r2)[0], convention="space"),
                "the first stage's report is not a valid report"),
            "a first stage of 23 obtained of 24 planned": (lambda: run_backend_ext(
                env_for("refuse2", root=env1.root, report=arm23, **r2)[0], convention="space"),
                "its report is not a COMPLETE run of the 24 reads"),
            "a first stage of 24 obtained of 25 planned": (lambda: run_backend_ext(
                env_for("refuse2", root=env1.root, report=arm25, **r2)[0], convention="space"),
                "its report is not a COMPLETE run of the 24 reads"),
            "a first stage under another convention (backend-ext-2's own report)": (lambda: run_backend_ext(
                env_for("refuse2", root=env7.root2, report=env7.report2, **r2)[0], convention="space"),
                "COMPLETE run of the 24 reads under 'bare'"),
            "a first stage whose cell does not hash to its report's record": (lambda: run_backend_ext(
                env_for("refuse2", root=bad_root, report=env1.report, **r2)[0], convention="space"),
                f"the first stage's cell {cname} is absent or does not hash to its report's record"),
            "a first stage whose root holds no cell": (lambda: run_backend_ext(
                env_for("refuse2", root=tmp / "emptyroot", report=env1.report, **r2)[0], convention="space"),
                f"the first stage's cell {cname} is absent"),
        }
        for k, p in id_first.items():
            cases2[f"a first stage under another {k}"] = (
                lambda p=p: run_backend_ext(env_for("refuse2", root=env1.root, report=p, **r2)[0], convention="space"),
                f"another stage identity (['{k}'])")
        for name, (fn, want) in cases2.items():
            msg = refusal(fn)
            chk(f"driver: backend-ext-2 refuses {name}, before the load, saying why", want in msg
                and made.count("refuse2") == 0 and not (tmp / "refuse2" / "root2").exists(), msg[:160])

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
        only = "the BACKEND extension's options only (backend-ext, backend-ext-2)"
        for argv, want in ((["render-ids-iv"], "render-ids-iv needs --tokenizer-dir, --out and --pi-date"),
                           (["render-ids-iv", "--resume", "--tokenizer-dir", t_, "--out", o_, "--pi-date", d_], only),
                           (["render-ids-iv", "--smoke", "0", "--tokenizer-dir", t_, "--out", o_, "--pi-date", d_],
                            only),
                           (["hashes", "--root", ""], only),
                           (["backend-ext", "--out", o_], "takes no folder options"),
                           (["backend-ext", "--ruling", "p01"], "--ruling takes PAUSE_ID=PATH"),
                           (["backend-ext-2"], "backend-ext-2 needs --convention NAME"),
                           (["backend-ext", "--convention", "space"], "--convention: backend-ext-2's option only"),
                           (["hashes", "--convention", "space"], "--convention: backend-ext-2's option only"),
                           (["backend-ext-2", "--convention", "space", "--out", o_], "takes no folder options"),
                           (["backend-ext-2", "--convention", "space", "--ruling", "p01"],
                            "--ruling takes PAUSE_ID=PATH")):
            got = argv_error(argv)
            chk(f"driver: main() refuses {' '.join(argv[:2])} … with \"{want}\"", want in got, got[-160:])
        g = globals()
        real_run = g["run_backend_ext"]
        calls: list = []

        def recorder(_env, **kw):
            calls.append(kw)
            return 0
        g["run_backend_ext"] = recorder
        try:
            rcs = (main(["backend-ext-2", "--convention", "space", "--resume", "--ruling", f"p01={r_md}"]),
                   main(["backend-ext"]),
                   main(["backend-ext-2", "--convention", "bare+eot", "--smoke", "2", "--root", str(tmp / "r"),
                         "--report", str(tmp / "p.json")]))
        finally:
            g["run_backend_ext"] = real_run
        chk("driver: main() hands each stage option and backend-ext-2's convention to the stage (backend-ext none)",
            rcs == (0, 0, 0) and calls == [
                {"root": None, "report": None, "resume": True, "rulings": {"p01": str(r_md)}, "smoke": None,
                 "convention": "space"},
                {"root": None, "report": None, "resume": False, "rulings": {}, "smoke": None, "convention": None},
                {"root": str(tmp / "r"), "report": str(tmp / "p.json"), "resume": False, "rulings": {}, "smoke": 2,
                 "convention": "bare+eot"}], calls)
        chk("driver: (the self-test's own guard) an environment pointing a stage path into the repository is refused",
            refused(lambda: env_for("guard", root2=BEXT2_ROOT))
            and refused(lambda: env_for("guard", report=BEXT_REPORT)), "")
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
        chk("driver: backend-ext refuses a cuBLAS setting other than the characterized one (rule 2), before the load",
            refused(lambda: run_backend_ext(env6)) and made.count("refuse") == 0, "")
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


# --- G-VEC (n v0.2 §8 step 7; ``valence_core.n.gvec``) --------------------------------------------------------------
GVEC_OUT = REPO / "data" / "n" / "gvec"
GVEC_SMOKE_RECORD = "gvec_smoke.json"
GVEC_STOP_END = ("G-VEC STOP: the record alone is written, with the diagnostic block; for the PI, on the seat's stated "
                 "default (n §2.3; ADDENDUM-n1 §6.1; the second sitting, §1.5)")


@dataclass
class GvecEnv:
    """G-VEC's seams: ``production_gvec_env`` is the box's; the self-test puts the numpy double behind them."""
    weights: Callable                   # () -> the weights of record (``weights_of_record``)
    load_ids: Callable                  # () -> ``ids.load()``
    e0: Callable                        # () -> scripts/box_e0_corpus.py, loaded by its path
    env_provenance: Callable            # (path) -> the provenance the adapter will report (before the load)
    make_adapter: Callable              # (path) -> the adapter (the weights load)
    adapter_shape: Callable             # (adapter) -> (n_layers, d_model)
    forward: Callable                   # (adapter) -> forward(ids, indices) -> {index: [S, D] residuals}
    pod: Callable                       # () -> the pod id or None
    driver: Callable                    # () -> (this driver's bytes as run, HEAD's committed bytes of its path | None)
    indices: tuple                      # the candidate indices (``gvec.CANDIDATE_INDICES``)
    reference: float                    # R's reference (``gvec.R_REFERENCE``)
    passages: Path                      # the corpus of record (``ids.PASSAGES_FILE``)
    passages_sha256: str                # its sha256 (``ids.PASSAGES_SHA256``)
    out: Path = GVEC_OUT
    shape: tuple = (N_LAYERS, D_MODEL)
    printer: Callable = print
    clock: Callable = time.perf_counter


def _hf_forward(adapter):
    """The adapter's capture: every position's residual at each index, unsteered (``forward(...).acts``)."""
    def forward(ids, indices):
        return adapter.forward(list(ids), capture_layers=tuple(int(i) for i in indices)).acts
    return forward


def production_gvec_env() -> GvecEnv:
    from valence_core.m import resume as m_resume
    from valence_core.n import gvec, ids
    return GvecEnv(weights=weights_of_record, load_ids=ids.load, e0=_e0_corpus, env_provenance=environment_provenance,
                   make_adapter=_load_adapter, adapter_shape=lambda a: (int(a.n_layers),
                                                                        int(a._model.config.hidden_size)),
                   forward=_hf_forward, pod=m_resume.pod_id, driver=driver_bytes, indices=gvec.CANDIDATE_INDICES,
                   reference=gvec.R_REFERENCE, passages=ids.PASSAGES_FILE, passages_sha256=ids.PASSAGES_SHA256)


def gvec_passages_check(records, corpus_path, want_sha256: str) -> None:
    """The passage records against the corpus of record, before the load: its sha256, then each record's index, id,
    state, pole and text sha256, in the corpus's order."""
    import hashlib
    data = Path(corpus_path).read_bytes()
    if hashlib.sha256(data).hexdigest() != want_sha256:
        raise SystemExit("data/n/passages.jsonl is not the corpus of record")
    corpus = [json.loads(x) for x in data.decode("utf-8").splitlines() if x.strip()]
    if len(corpus) != len(records):
        raise SystemExit(f"{len(records)} passage records for {len(corpus)} passages in the corpus")
    for i, (c, r) in enumerate(zip(corpus, records)):
        if (r["index"], r["id"], r["state"], r["pole"], r["text_sha256"]) != (
                i, c["id"], c["state"], c["pole"], hashlib.sha256(c["text"].encode("utf-8")).hexdigest()):
            raise SystemExit(f"passage record {i} is not the corpus's passage {i}")


def gvec_a3_check(e0, loaded, contexts) -> tuple:
    """Before the load, model-free: A3's frozen inputs and rule-18 hygiene (scripts/box_e0_corpus.py), held to the (iv)
    render's record of them (the manifest's iv block): the input digests, the two files' sha256s and the contexts'
    digest, and each context record's place, condition, item, variant and texts' sha256s. Returns (the input digests,
    the code sha256s, the hygiene record, A3's axis conditions and split)."""
    import hashlib

    from valence_core import extract
    from valence_core.n import ids
    shas = e0.assert_frozen_inputs()
    hyg = e0.hygiene()
    block = loaded["manifest"]["iv"]["a3"]
    if dict(shas) != dict(block["input_shas"]):
        raise SystemExit("A3's frozen inputs are not those the (iv) render recorded")
    code = {"scripts/box_e0_corpus.py": hashlib.sha256(Path(e0.__file__).read_bytes()).hexdigest(),
            "valence_core/extract.py": hashlib.sha256(Path(extract.__file__).read_bytes()).hexdigest()}
    if code != dict(block["code_sha256"]):
        raise SystemExit("A3's code (scripts/box_e0_corpus.py, valence_core/extract.py) is not the (iv) render's")
    rows = [(c.prefix, c.full, c.condition, c.item_id, c.variant) for c in e0.e0_contexts()]
    if len(rows) != len(contexts) or ids.a3_digest(rows) != block["contexts_sha256"]:
        raise SystemExit("A3's contexts are not those the (iv) render recorded")
    for i, ((p, f, c, it, v), rec) in enumerate(zip(rows, contexts)):
        if (rec["index"], rec["condition"], rec["item_id"], int(rec["variant"])) != (i, c, it, int(v)) \
                or rec["prefix_sha256"] != hashlib.sha256(p.encode("utf-8")).hexdigest() \
                or rec["full_sha256"] != hashlib.sha256(f.encode("utf-8")).hexdigest():
            raise SystemExit(f"context record {i} is not A3's context {i}")
    extract.assert_stage_splits({"stage": "G-VEC", "fit_ids": list(e0.FIT_IDS), "val_ids": list(e0.VAL_IDS)},
                                where="G-VEC's A3 split")
    a3 = {"axis_conditions": {k: tuple(v) for k, v in e0.AXIS_CONDITIONS.items()}, "axis_order": tuple(e0.AXIS_ORDER),
          "fit_ids": tuple(e0.FIT_IDS), "val_ids": tuple(e0.VAL_IDS)}
    return dict(shas), code, dict(hyg), a3


def run_gvec(env: GvecEnv, *, out=None, smoke: int | None = None) -> int:
    """G-VEC, in order: refusals; the weights and the driver; the ids of record, every ids_sha re-derived, held to the
    corpus of record and to A3's frozen inputs; the R6 bridge before the load; the load and its provenance;
    ``gvec.compute``; the outputs, built in a staging folder beside the out folder and renamed into place.
    Everything that needs no model happens before the load, the refusal of a passage with no token at positions 1..n
    among it. Exit 0 on PASS (or a smoke), 2 on the R check's STOP (the record alone, with the diagnostic block, for
    the PI on the seat's stated default: the second sitting, §1.5); a refusal raises."""
    import hashlib
    import shutil

    import numpy as np

    from valence_core.m import resume as m_resume
    from valence_core.m.keys import stream_known_answer
    from valence_core.n import directions, guard, gvec, ids, schema, sessions
    say = env.printer
    if smoke is not None:
        if not 1 <= int(smoke) <= directions.N_NEUTRAL:
            raise SystemExit(f"--smoke takes 1..{directions.N_NEUTRAL} (neutral passages and contexts)")
        if out is None:
            raise SystemExit("a smoke writes only where --out names, a new folder outside the repository")
        if _within(Path(out).resolve(), REPO.resolve()):
            raise SystemExit(f"a smoke writes outside the repository, not {out}")
        out_p = guard.refuse_out(Path(out))
    else:
        if out is not None:
            raise SystemExit("a run of record writes only to data/n/gvec/ (--out is a smoke's)")
        out_p = guard.refuse_out(Path(env.out))
    if out_p.exists():
        raise SystemExit(f"{_shown(out_p)} exists: G-VEC writes a new folder and never resumes (G7)")
    stage = guard.refuse_out(out_p.parent / f".{out_p.name}.staging")
    if stage.exists():
        raise SystemExit(f"{_shown(stage)} exists: a staging folder another run left (a hard stop skips its "
                         f"cleanup); move it aside first")
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
    idx = tuple(int(i) for i in env.indices)
    if smoke is not None:
        say(f"SMOKE: {smoke} neutral passages and {smoke} contexts, outside the repository; R over positions 1..n, "
            f"R_ell and the diagnostic block; never of record")
    say(f"STAGE G-VEC: candidate indices {list(idx)}; R's reference {env.reference!r}, within {gvec.R_TOLERANCE!r}; "
        f"out {_shown(out_p)}")
    w = env.weights()
    say(f"WEIGHTS: {w['repo']} revision {w['revision']}, files_aggregate_sha256 {w['sha256']}; {w['n_files']} files "
        f"at {w['path']}, each at the manifest's byte count (the full re-hash is respawn step (i))")
    drv, head = env.driver()
    dsha = hashlib.sha256(drv).hexdigest()
    if smoke is None and drv != head:
        raise SystemExit("a run of record runs only the committed driver: scripts/n_sessions.py is not HEAD's "
                         "committed bytes (the box answers of 2026-11-18, §2 item 5)")
    say(f"DRIVER scripts/n_sessions.py {dsha}: "
        + ("HEAD's committed bytes" if drv == head else "a smoke's, not HEAD's committed bytes (unchecked)"))
    loaded = env.load_ids()
    if loaded["manifest_sha256"] != ids.MANIFEST_OF_RECORD:
        raise SystemExit("data/n/ids/MANIFEST.json is not the render of record's (G13)")
    ps, cs = list(loaded[ids.GVEC_FILE]), list(loaded[ids.A3_FILE])
    if (len(ps), len(cs)) != (ids.N_PASSAGES, ids.N_A3_CONTEXTS):
        raise SystemExit(f"{len(ps)} passages and {len(cs)} contexts, not {ids.N_PASSAGES} and {ids.N_A3_CONTEXTS}")
    bad = sum(1 for r in ps + cs if sessions.ids_sha(r["ids"]) != r["ids_sha"])
    if bad:
        raise SystemExit(f"{bad} records' ids do not hash to their ids_sha")
    longest = max(len(r["ids"]) for r in ps + cs)
    if longest > schema.MAX_WINDOW:
        raise SystemExit(f"an input of {longest} tokens is over the window {schema.MAX_WINDOW} (GA-4)")
    shortest = min(len(r["ids"]) for r in ps)
    if shortest <= directions.CAPTURE_FROM:
        raise SystemExit(f"a passage of {shortest} id(s) has no token at positions 1..n (the convention of record), "
                         f"before the load")
    gvec_passages_check(ps, env.passages, env.passages_sha256)
    gvec.passage_groups(ps)
    shas, code, hyg, a3 = gvec_a3_check(env.e0(), loaded, cs)
    if tuple(a3["axis_order"]) != gvec.NAMED[1:]:
        raise SystemExit(f"A3's axis order {tuple(a3['axis_order'])} is not the named rows' {gvec.NAMED[1:]}")
    say(f"inputs: the ids of record {loaded['manifest_sha256']} ((iv): {len(ps)} passages, {len(cs)} contexts, every "
        f"ids_sha re-derived; the longest {longest} tokens, within the window {schema.MAX_WINDOW}); the corpus "
        f"{env.passages_sha256}, each record its passage; A3's frozen inputs {json.dumps(shas, sort_keys=True)}, its "
        f"code and contexts as the render recorded them; rule-18 hygiene {json.dumps(hyg, sort_keys=True)}")
    n_layers, d_model = env.shape
    pre = env.env_provenance(w["path"])
    if bridge_identifier(pre) != CHARACTERIZED_IDENTIFIER:
        raise SystemExit(f"before the load: the environment's provenance under the default window hashes to "
                         f"{bridge_identifier(pre)}, not the characterization's {CHARACTERIZED_IDENTIFIER} (R6)")
    bid = m_resume.backend_identifier(pre)
    mods = _import_production()
    prov_rec = {"package_sha256": mods["guard"].package_sha256(),
                "imported_sha256": mods["guard"].closure_from_modules(dict(sys.modules)),
                "weights": {"repo": w["repo"], "revision": w["revision"], "sha256": w["sha256"]},
                "backend_identifier": bid, "characterized_identifier": CHARACTERIZED_IDENTIFIER, "pod_id": pod,
                "ids_manifest_sha256": loaded["manifest_sha256"], "passages_sha256": env.passages_sha256,
                "driver_sha256": dsha, "a3_input_shas": shas, "a3_code_sha256": code, "hygiene": hyg,
                "window": schema.MAX_WINDOW, "longest_input": longest, "smoke": smoke}
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
    prov_rec["load_ms"] = load_ms
    prov_rec["adapter_provenance"] = m_resume.provenance_record(prov)
    fwd = env.forward(adapter)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    stage.mkdir()
    try:
        if smoke is not None:
            neu = [r for r in ps if r["pole"] == "0"][:int(smoke)]
            pc = gvec.passage_captures(fwd, neu, idx)
            cap = gvec.a3_capture(fwd, cs[:int(smoke)], idx)
            allneu = np.ones(len(neu), dtype=bool)
            rec = {"schema": gvec.RECORD_SCHEMA, "stage": gvec.STAGE, "status": "SMOKE", "smoke": int(smoke),
                   "R": {str(i): gvec.r_at(pc, allneu, i) for i in idx},
                   "R_ell": {str(i): float(cap.resid_norms[i]) for i in idx},
                   "diagnostic": {str(i): gvec.diagnostic_at(pc, allneu, i) for i in idx},
                   "neutral_tokens": int(pc["ntok"].sum()), "neutral_tokens_in_R": int(pc["nr"].sum()),
                   "convention": gvec.R_CONVENTION, "provenance": prov_rec}
            (stage / GVEC_SMOKE_RECORD).write_text(json.dumps(rec, sort_keys=True, indent=1, allow_nan=False) + "\n",
                                                   encoding="utf-8")
            for i in idx:
                say(f"SMOKE R at index {i} over the first {len(neu)} neutral passages: {rec['R'][str(i)]!r}; R_ell "
                    f"over the first {int(smoke)} contexts in A3's order: {rec['R_ell'][str(i)]!r}")
            for i in idx:
                say(gvec.diagnostic_line(i, rec["diagnostic"][str(i)]))
            status = "SMOKE"
        else:
            res = gvec.compute(fwd, ps, cs, a3=a3, d_model=d_model, indices=idx, reference=env.reference, say=say)
            gvec.write(stage, res, prov_rec)
            status = res["status"]
        os.replace(stage, out_p)
    except BaseException:
        shutil.rmtree(stage, ignore_errors=True)
        raise
    for p in sorted(out_p.iterdir()):
        say(f"file {_shown(p)} sha256 {hashlib.sha256(p.read_bytes()).hexdigest()}")
    if status == "STOP":
        say(GVEC_STOP_END)
        return 2
    say(f"G-VEC {status}" + (", never of record" if status == "SMOKE" else ""))
    return 0


def cmd_gvec(out=None, smoke: int | None = None) -> int:
    return run_gvec(production_gvec_env(), out=out, smoke=smoke)


def _gvec_selftest(chk, tmp: Path) -> None:
    """G-VEC's command, model-free: its flow over the numpy double behind every seam (a run of record into a folder
    under tmp, a STOP, a smoke, a failure mid-run), its refusals before the load, and main()'s dispatch. It writes
    only under tmp."""
    import hashlib
    import types

    import numpy as np

    from valence_core import extract
    from valence_core.m import resume as m_resume
    from valence_core.n import directions, gvec, ids, schema, sessions, testing
    tmp.mkdir(parents=True, exist_ok=True)
    be = testing.CausalDouble(d_model=32)
    rng = np.random.default_rng(31)
    L = (3, 4)

    def refused(fn) -> bool:
        try:
            fn()
        except SystemExit:
            return True
        return False
    prod = production_gvec_env()
    chk("driver: G-VEC's production seams carry the package's indices (31, 32), its reference 25.49, the corpus of "
        "record and data/n/gvec/",
        (tuple(prod.indices), prod.reference, prod.passages, prod.passages_sha256, prod.out)
        == (gvec.CANDIDATE_INDICES, gvec.R_REFERENCE, ids.PASSAGES_FILE, ids.PASSAGES_SHA256, GVEC_OUT)
        and gvec.CANDIDATE_INDICES == (31, 32) and gvec.R_REFERENCE == 25.49 and gvec.R_TOLERANCE == 0.02, "")
    # the inputs: a toy corpus (544 passages) and A3's 1,344 contexts, their ids records and the manifest's iv block
    corpus, prec = [], []
    for pole, states, n in (("+", directions.POSITIVE_STATES, directions.N_PER_STATE),
                            ("-", directions.NEGATIVE_STATES, directions.N_PER_STATE),
                            ("0", (directions.NEUTRAL,), directions.N_NEUTRAL)):
        for s in states:
            name = directions.CORPUS_STATE.get(s, s)
            for j in range(n):
                text = f"{name} {j}"
                ii = [int(x) for x in rng.integers(3, be.vocab, int(rng.integers(3, 7)))]
                corpus.append({"id": f"{name}-{j:02d}", "state": name, "pole": pole, "text": text})
                prec.append({"index": len(prec), "id": f"{name}-{j:02d}", "state": name, "pole": pole,
                             "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "n_tokens": len(ii),
                             "ids_sha": sessions.ids_sha(ii), "ids": ii})
    cfile = tmp / "passages.jsonl"
    cfile.write_bytes("".join(json.dumps(c, sort_keys=True) + "\n" for c in corpus).encode("utf-8"))
    csha = hashlib.sha256(cfile.read_bytes()).hexdigest()
    conds = ("self_pos", "self_neg", "sent_pos", "sent_neg", "char_pos", "char_neg", "neutral")
    items = tuple(f"e{i:02d}" for i in range(1, 49))
    ctxs, crec = [], []
    for it in items:
        pre_ids = [int(x) for x in rng.integers(3, be.vocab, 4)]
        for c in conds:
            for v in range(4):
                span = [int(x) for x in rng.integers(3, be.vocab, 3)]
                pre, full = f"P {it}", f"P {it} {c} {v}"
                ctxs.append(extract.Context(prefix=pre, full=full, condition=c, item_id=it, variant=v))
                crec.append({"index": len(crec), "item_id": it, "condition": c, "variant": v,
                             "prefix_sha256": hashlib.sha256(pre.encode("utf-8")).hexdigest(),
                             "full_sha256": hashlib.sha256(full.encode("utf-8")).hexdigest(),
                             "seq_len": 7, "span_start": 4, "prefix_tokens": 4,
                             "ids_sha": sessions.ids_sha(pre_ids + span), "ids": pre_ids + span})
    e0file = tmp / "e0stub.py"
    e0file.write_text("# stub\n", encoding="utf-8")
    shas_t = {"corpus_sha": "c" * 16, "frames_sha": "f" * 16, "probes_sha": "p" * 16}
    e0 = types.SimpleNamespace(
        __file__=str(e0file), assert_frozen_inputs=lambda: dict(shas_t),
        hygiene=lambda: {"both_directions": True, "fit_val_disjoint": True}, e0_contexts=lambda: list(ctxs),
        AXIS_CONDITIONS={"span_reward": ("self_pos", "self_neg"), "span_sentiment": ("sent_pos", "sent_neg"),
                         "span_character": ("char_pos", "char_neg")},
        AXIS_ORDER=("span_reward", "span_sentiment", "span_character"), FIT_IDS=items[:24], VAL_IDS=items[24:])
    ex_sha = hashlib.sha256(Path(extract.__file__).read_bytes()).hexdigest()
    block = {"input_shas": dict(shas_t),
             "code_sha256": {"scripts/box_e0_corpus.py": hashlib.sha256(e0file.read_bytes()).hexdigest(),
                             "valence_core/extract.py": ex_sha},
             "contexts_sha256": ids.a3_digest([(c.prefix, c.full, c.condition, c.item_id, c.variant) for c in ctxs])}

    def loaded_of(p_=None, c_=None, man=None, blk=None):
        return {"manifest_sha256": man or ids.MANIFEST_OF_RECORD, "manifest": {"iv": {"a3": blk or block}},
                ids.GVEC_FILE: p_ if p_ is not None else prec, ids.A3_FILE: c_ if c_ is not None else crec}
    prov_t = dict(CHARACTERIZED_PROVENANCE, path="(toy)", choice_window_declared=schema.MAX_WINDOW)
    made: list = []

    class StubAdapter:
        def __init__(self, prov):
            self._prov = prov

        def provenance(self):
            return dict(self._prov)

    def fwd_of(_a):
        return lambda ids_, layers: be.forward_all(ids_, layers)
    neu_ix = [i for i, r in enumerate(prec) if r["pole"] == "0"]
    r4 = gvec.r_at(gvec.passage_captures(fwd_of(None), [prec[i] for i in neu_ix], L),
                   np.ones(len(neu_ix), dtype=bool), 4)

    def env_for(tag, **over):
        lines: list = []

        def mk(path, prov=None):
            made.append(tag)
            return StubAdapter(prov or prov_t)
        base = dict(weights=lambda: {"repo": "toy", "revision": "0" * 12, "sha256": "5" * 64, "n_files": 1,
                                     "path": "(toy)"},
                    load_ids=lambda: loaded_of(), e0=lambda: e0, env_provenance=lambda p: dict(prov_t),
                    make_adapter=mk, adapter_shape=lambda a: (6, 32), forward=fwd_of, pod=lambda: CHARACTERIZED_POD,
                    driver=lambda: (b"drv", b"drv"), indices=L, reference=r4, passages=cfile, passages_sha256=csha,
                    out=tmp / tag / "gvec", shape=(6, 32), printer=lines.append)
        base.update(over)
        if _within(Path(base["out"]).resolve(), REPO.resolve()):    # a self-test writes only under tmp
            raise SystemExit(f"a self-test environment points out into the repository: {base['out']}")
        return GvecEnv(**base), lines
    saved = {k: os.environ.get(k) for k in ("CUBLAS_WORKSPACE_CONFIG",)}
    try:
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = CHARACTERIZED_PROVENANCE["cublas_workspace_config"]
        env1, lines1 = env_for("run")
        rc1 = run_gvec(env1)
        rec1 = json.loads((env1.out / gvec.OUT_RECORD).read_text(encoding="utf-8"))
        names1 = sorted(p.name for p in env1.out.iterdir())
        chk("driver: G-VEC's run of record, over the double behind every seam: PASS at the index within 2%, its six "
            "files in a new folder (the record, the cosines file, and the named and alternative rows at each index), "
            "the staging folder gone",
            rc1 == 0 and rec1["status"] == "PASS" and rec1["site"]["site"] == 4
            and names1 == sorted([gvec.OUT_RECORD, gvec.OUT_COSINES] + [gvec.directions_file(i) for i in L]
                                 + [gvec.alt_file(i) for i in L])
            and not (env1.out.parent / ".gvec.staging").exists(), (rc1, rec1.get("status"), names1))
        pv = rec1["provenance"]
        chk("driver: the record's provenance: the package and closure, the weights, the identifiers, the pod, the ids "
            "of record, the corpus, the driver, A3's inputs and code, the hygiene, the window and the load",
            pv["ids_manifest_sha256"] == ids.MANIFEST_OF_RECORD and pv["passages_sha256"] == csha
            and pv["characterized_identifier"] == CHARACTERIZED_IDENTIFIER and pv["pod_id"] == CHARACTERIZED_POD
            and pv["a3_code_sha256"] == block["code_sha256"] and pv["a3_input_shas"] == shas_t
            and "valence_core/extract.py" in pv["imported_sha256"] and pv["window"] == schema.MAX_WINDOW
            and pv["smoke"] is None and isinstance(pv["load_ms"], int) and len(pv["package_sha256"]) == 64
            and pv["backend_identifier"] == m_resume.backend_identifier(prov_t)
            and pv["adapter_provenance"] == m_resume.provenance_record(prov_t), "")
        heads = ("STAGE G-VEC", "WEIGHTS:", "DRIVER", "inputs:", "backend:", "R over positions 1..n:", "R at index 3",
                 "R at index 4", "diagnostic at index 3,", "diagnostic at index 4,", "site: index 4", "file ",
                 "G-VEC PASS")
        chk("driver: G-VEC prints its lines in order -- STAGE, WEIGHTS, DRIVER, inputs, backend, R's token count, R at "
            "both indices, the diagnostic line at both, the site, each file's sha256, PASS -- and no passage, context "
            "or id",
            [next((i for i, x in enumerate(lines1) if x.startswith(h)), -1) for h in heads]
            == sorted(next((i for i, x in enumerate(lines1) if x.startswith(h)), -1) for h in heads)
            and all(any(x.startswith(h) for x in lines1) for h in heads)
            and not any('"ids"' in x or "passage record" in x for x in lines1), lines1[:4])
        chk("driver: the model loads once, after every check that needs none", made.count("run") == 1, made)
        env2, _l2 = env_for("stop", reference=1.0e6)
        rc2 = run_gvec(env2)
        chk("driver: R within 2% at neither index is the STOP: exit 2, the record alone with the diagnostic block, for "
            "the PI on the seat's stated default (the second sitting, §1.5), its two STOP lines printed",
            rc2 == 2 and [p.name for p in env2.out.iterdir()] == [gvec.OUT_RECORD]
            and json.loads((env2.out / gvec.OUT_RECORD).read_text())["status"] == "STOP"
            and sorted(json.loads((env2.out / gvec.OUT_RECORD).read_text())["diagnostic"]) == ["3", "4"]
            and _l2[-1] == GVEC_STOP_END and gvec.STOP_LINE in _l2, (rc2, _l2[-1:]))
        env3, l3 = env_for("smoke", driver=lambda: (b"drv-new", b"drv"))
        rc3 = run_gvec(env3, out=tmp / "smoke-out", smoke=3)
        rec3 = json.loads((tmp / "smoke-out" / GVEC_SMOKE_RECORD).read_text())
        first3 = [prec[i] for i in neu_ix[:3]]
        r_s = {str(i): gvec.r_at(gvec.passage_captures(fwd_of(None), first3, L), np.ones(3, dtype=bool), i) for i in L}
        rl_s = {str(i): gvec.a3_capture(fwd_of(None), crec[:3], L).resid_norms[i] for i in L}
        chk("driver: a smoke runs uncommitted bytes into --out outside the repository: R over its first neutral "
            "passages and R_ell over its first contexts, at both indices, never of record",
            rc3 == 0 and rec3["status"] == "SMOKE" and rec3["R"] == r_s and rec3["R_ell"] == rl_s
            and not env3.out.exists() and any(x.startswith("SMOKE:") for x in l3)
            and any(x.startswith("SMOKE:") and x.endswith("; R over positions 1..n, R_ell and the diagnostic block; "
                                                          "never of record") for x in l3)
            and any("a smoke's, not HEAD's committed bytes" in x for x in l3), (rec3.get("R"), r_s))
        pc_s = gvec.passage_captures(fwd_of(None), first3, L)
        d_s = {str(i): gvec.diagnostic_at(pc_s, np.ones(3, dtype=bool), i) for i in L}
        chk("driver: the smoke records the diagnostic block over its passages, the convention and the two token "
            "counts, and prints the run's diagnostic lines (the second sitting, §1.3: \"the smoke prints the same "
            "lines\"), after its R lines",
            rec3["schema"] == gvec.RECORD_SCHEMA and rec3["diagnostic"] == d_s
            and rec3["convention"] == gvec.R_CONVENTION and rec3["neutral_tokens"] == int(pc_s["ntok"].sum())
            and rec3["neutral_tokens_in_R"] == int(pc_s["nr"].sum())
            and [x for x in l3 if x.startswith("diagnostic at index ")] == [gvec.diagnostic_line(i, d_s[str(i)])
                                                                            for i in L]
            and max(j for j, x in enumerate(l3) if x.startswith("SMOKE R at index "))
            < min(j for j, x in enumerate(l3) if x.startswith("diagnostic at index ")), rec3.get("diagnostic"))

        def broken(_a):
            def f(ids_, layers):
                raise RuntimeError("the forward failed")
            return f
        env4, _l4 = env_for("fail", forward=broken)
        try:
            run_gvec(env4)
            failed = False
        except RuntimeError:
            failed = True
        chk("driver: a failure after the load leaves no out folder and no staging folder (nothing to resume)",
            failed and not env4.out.exists() and not (env4.out.parent / ".gvec.staging").exists(), "")
        # refusals, each before the load
        n_made = len(made)
        pre_out = tmp / "exists" / "gvec"
        pre_out.mkdir(parents=True)
        tampered = [dict(r) for r in prec]
        tampered[5]["ids_sha"] = "0" * 16
        long_p = [dict(r) for r in prec]
        long_p[7] = dict(long_p[7], ids=[3] * (schema.MAX_WINDOW + 1))
        long_p[7]["ids_sha"] = sessions.ids_sha(long_p[7]["ids"])
        one_p = [dict(r) for r in prec]                 # the review's O7: refused before the load
        one_p[6] = dict(one_p[6], ids=[3], ids_sha=sessions.ids_sha([3]))
        wrong_state = [dict(r) for r in prec]
        wrong_state[0]["state"] = "relief"
        swapped = [dict(r) for r in crec]
        swapped[0], swapped[1] = dict(swapped[1], index=0), dict(swapped[0], index=1)
        bad_code = dict(block, code_sha256=dict(block["code_sha256"], **{"valence_core/extract.py": "0" * 64}))

        def with_rec(recs_, i, **kw):
            out_ = [dict(r) for r in recs_]
            out_[i].update(kw)
            return out_
        p_text = with_rec(prec, 2, text_sha256="0" * 64)
        c_pre = with_rec(crec, 5, prefix_sha256="0" * 64)
        c_full = with_rec(crec, 5, full_sha256="0" * 64)
        leftover = tmp / "lefto" / ".gvec.staging"
        leftover.mkdir(parents=True)
        cases = [
            ("an existing out folder (G-VEC never resumes)", lambda: run_gvec(env_for("x1", out=pre_out)[0])),
            ("a staging folder a hard stop left", lambda: run_gvec(env_for("lefto")[0])),
            ("a context record whose ids do not hash to its ids_sha",
             lambda: run_gvec(env_for("x21", load_ids=lambda: loaded_of(c_=with_rec(crec, 3, ids_sha="0" * 16)))[0])),
            ("a passage record whose id is not its passage's",
             lambda: run_gvec(env_for("x22", load_ids=lambda: loaded_of(p_=with_rec(prec, 2, id="x-00")))[0])),
            ("a passage record whose pole is not its passage's",
             lambda: run_gvec(env_for("x23", load_ids=lambda: loaded_of(p_=with_rec(prec, 2, pole="0")))[0])),
            ("a passage record whose text sha256 is not its passage's",
             lambda: run_gvec(env_for("x24", load_ids=lambda: loaded_of(p_=p_text))[0])),
            ("a context record whose prefix sha256 is not A3's",
             lambda: run_gvec(env_for("x25", load_ids=lambda: loaded_of(c_=c_pre))[0])),
            ("a context record whose full sha256 is not A3's",
             lambda: run_gvec(env_for("x26", load_ids=lambda: loaded_of(c_=c_full))[0])),
            ("--out on a run of record", lambda: run_gvec(env_for("x2")[0], out=tmp / "o2")),
            ("a smoke without --out", lambda: run_gvec(env_for("x3")[0], smoke=2)),
            ("a smoke whose --out is in the repository",
             lambda: run_gvec(env_for("x4")[0], out=REPO / "data" / "n" / "gvec-smoke", smoke=2)),
            ("a smoke of 97 (over the 96 neutral passages)",
             lambda: run_gvec(env_for("x5")[0], out=tmp / "o5", smoke=97)),
            ("a smoke of 0", lambda: run_gvec(env_for("x5b")[0], out=tmp / "o5b", smoke=0)),
            ("no pod id", lambda: run_gvec(env_for("x6", pod=lambda: None)[0])),
            ("another pod", lambda: run_gvec(env_for("x7", pod=lambda: "other-pod")[0])),
            ("a run of record on uncommitted driver bytes",
             lambda: run_gvec(env_for("x8", driver=lambda: (b"new", b"old"))[0])),
            ("ids not of record", lambda: run_gvec(env_for("x9", load_ids=lambda: loaded_of(man="0" * 64))[0])),
            ("a record whose ids do not hash to its ids_sha",
             lambda: run_gvec(env_for("x10", load_ids=lambda: loaded_of(p_=tampered))[0])),
            ("an input over the window", lambda: run_gvec(env_for("x11", load_ids=lambda: loaded_of(p_=long_p))[0])),
            ("a passage of one id (no token at positions 1..n)",
             lambda: run_gvec(env_for("x11b", load_ids=lambda: loaded_of(p_=one_p))[0])),
            ("a corpus that is not of record", lambda: run_gvec(env_for("x12", passages_sha256="0" * 64)[0])),
            ("a passage record that is not its corpus passage",
             lambda: run_gvec(env_for("x13", load_ids=lambda: loaded_of(p_=wrong_state))[0])),
            ("A3's code not the render's",
             lambda: run_gvec(env_for("x14", load_ids=lambda: loaded_of(blk=bad_code))[0])),
            ("A3's inputs not frozen",
             lambda: run_gvec(env_for("x15", e0=lambda: types.SimpleNamespace(
                 **dict(vars(e0), assert_frozen_inputs=lambda: dict(shas_t, corpus_sha="d" * 16))))[0])),
            ("a context record out of A3's order",
             lambda: run_gvec(env_for("x16", load_ids=lambda: loaded_of(c_=swapped))[0])),
            ("a provenance off the characterization before the load",
             lambda: run_gvec(env_for("x17", env_provenance=lambda p: dict(prov_t, gpu="another GPU"))[0])),
        ]
        out_r = {name: refused(fn) for name, fn in cases}
        chk("driver: G-VEC refuses, before the load: " + "; ".join(name for name, _f in cases),
            all(out_r.values()) and len(made) == n_made, [k for k, v in out_r.items() if not v])
        mk_bad = env_for("x18", make_adapter=lambda p: (made.append("x18"), StubAdapter(dict(prov_t, gpu="x")))[1])[0]
        shp_bad = env_for("x19", adapter_shape=lambda a: (6, 16))[0]
        chk("driver: G-VEC refuses after the load a provenance not the one checked before it, and a checkpoint of "
            "another shape, writing nothing", refused(lambda: run_gvec(mk_bad)) and refused(lambda: run_gvec(shp_bad))
            and not mk_bad.out.exists() and not shp_bad.out.exists(), "")
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
        chk("driver: G-VEC refuses a cuBLAS setting other than the characterized one (rule 2), before the load",
            refused(lambda: run_gvec(env_for("x20")[0])) and made.count("x20") == 0, "")
        chk("driver: (the self-test's own guard) a G-VEC environment pointing out into the repository is refused",
            refused(lambda: env_for("guard", out=GVEC_OUT)), "")
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    # main()'s dispatch: G-VEC takes --out and --smoke only
    import contextlib
    import io

    def argv_error(argv) -> str:
        buf = io.StringIO()
        try:
            with contextlib.redirect_stderr(buf):
                main(argv)
        except SystemExit:
            return buf.getvalue()
        return "no error"
    t_ = str(tmp)
    for argv in (["gvec", "--root", t_], ["gvec", "--report", t_], ["gvec", "--resume"], ["gvec", "--ruling", "p01=x"],
                 ["gvec", "--model-dir", t_], ["gvec", "--tokenizer-dir", t_], ["gvec", "--ids-dir", t_],
                 ["gvec", "--convention", "space"], ["gvec", "--pi-date", "2026-11-19"]):
        got = argv_error(argv)
        chk(f"driver: main() refuses {' '.join(argv[:2])} … for gvec", "gvec takes --out and --smoke only" in got,
            got[-160:])
    g = globals()
    real_run = g["run_gvec"]
    calls: list = []

    def recorder(_env, **kw):
        calls.append(kw)
        return 0
    g["run_gvec"] = recorder
    try:
        rcs = (main(["gvec"]), main(["gvec", "--smoke", "3", "--out", str(tmp / "s")]))
    finally:
        g["run_gvec"] = real_run
    chk("driver: main() hands G-VEC's --out and --smoke to the stage, and nothing on a run of record",
        rcs == (0, 0) and calls == [{"out": None, "smoke": None}, {"out": str(tmp / "s"), "smoke": 3}], calls)


# --- G-CAL-n (n v0.2 §8 step 8; ``valence_core.n.gcal``) --------------------------------------------------------------
GCAL_OUT = REPO / "data" / "n" / "gcal"
GCAL_SMOKE_MAX = 4                  # GC19: the smoke's prompts, at +rho and unsteered only


@dataclass
class GcalEnv:
    """G-CAL-n's seams: ``production_gcal_env`` is the box's; the self-test puts the numpy double behind them."""
    weights: Callable                   # () -> the weights of record (``weights_of_record``)
    load_ids: Callable                  # () -> ``ids.load()``
    gvec_dir: Path                      # data/n/gvec/: G-VEC's outputs of record
    committed: Callable                 # (path) -> HEAD's committed bytes of a repository path, or None
    env_provenance: Callable            # (path) -> the provenance the adapter will report (before the load)
    make_adapter: Callable              # (path) -> the adapter (the weights load)
    adapter_shape: Callable             # (adapter) -> (n_layers, d_model)
    step_logits: Callable               # (adapter) -> step(ids, injections) -> the last position's logits [V]
    forward: Callable                   # (adapter) -> forward(ids, indices) -> {index: [S, D]}
    decoder: Callable                   # (adapter) -> decode(ids) -> text, G-VER's decode
    eos_id: Callable                    # (adapter) -> the tokenizer's eos id
    pod: Callable                       # () -> the pod id or None
    driver: Callable                    # () -> (this driver's bytes as run, HEAD's committed bytes of its path | None)
    indices: tuple                      # G-VEC's candidate indices (``gvec.CANDIDATE_INDICES``)
    out: Path = GCAL_OUT
    shape: tuple = (N_LAYERS, D_MODEL)
    cap: int | None = None              # the self-test's smaller cap only; the stage's is gcal.CAP
    printer: Callable = print
    clock: Callable = time.perf_counter


def _hf_step_logits(adapter):
    """One uncached forward over the whole sequence, the injections placed at their positions (offset 0): the last
    position's logits (``forward(...).logits``)."""
    def step(ids, injections):
        return adapter.forward(list(ids), capture_layers=(), injections=list(injections)).logits
    return step


def _hf_decoder(adapter):
    return _decoder(adapter._tok)


def committed_bytes(path):
    """HEAD's committed bytes of a repository path (``git show HEAD:<path>``), or None when git cannot show them."""
    import subprocess
    rel = Path(path).resolve().relative_to(REPO.resolve()).as_posix()
    got = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{rel}"], capture_output=True, check=False)
    return got.stdout if got.returncode == 0 else None


def production_gcal_env() -> GcalEnv:
    from valence_core.m import resume as m_resume
    from valence_core.n import gvec, ids
    return GcalEnv(weights=weights_of_record, load_ids=ids.load, gvec_dir=GVEC_OUT, committed=committed_bytes,
                   env_provenance=environment_provenance, make_adapter=_load_adapter,
                   adapter_shape=lambda a: (int(a.n_layers), int(a._model.config.hidden_size)),
                   step_logits=_hf_step_logits, forward=_hf_forward, decoder=_hf_decoder, eos_id=lambda a: a.eos_id,
                   pod=m_resume.pod_id, driver=driver_bytes, indices=gvec.CANDIDATE_INDICES)


def gcal_gvec_inputs(gvec_dir, committed, indices) -> dict:
    """G-VEC's outputs of record, before the load (GC18; rule 27): gvec.json and the site's directions file each HEAD's
    committed bytes; the record a G-VEC PASS, its site one of the candidates and its of_record's, the directions file at
    the record's sha256; the valence row (row 0, ``gvec.NAMED``) and span_reward's (the gate's, the second sitting's
    §2.5) each at of_record's sha16 (the Injection's). Returns the site, R, R_ell, the two rows and their sha16s, and
    the two files' sha256s."""
    import hashlib

    from valence_core.n import gcal, gvec
    d = Path(gvec_dir)
    rp = d / gvec.OUT_RECORD
    if not rp.is_file():
        raise SystemExit("data/n/gvec/gvec.json is absent: G-CAL-n runs after G-VEC's PASS is committed (GC18)")
    data = rp.read_bytes()
    if committed(rp) != data:
        raise SystemExit("data/n/gvec/gvec.json is not HEAD's committed bytes (rule 27)")
    try:
        rec = json.loads(data.decode("utf-8"))
        ofr, site, rsite = rec["of_record"], int(rec["of_record"]["site"]), int(rec["site"]["site"])
        R, R_ell, v_rec = float(ofr["R"]), float(ofr["R_ell"]), str(ofr["directions"]["valence"])
        g_rec = str(ofr["directions"][gcal.GATE_DIRECTION])
        fshas = dict(rec["files_sha256"])
        head = (rec.get("schema"), rec.get("stage"), rec.get("status"))
    except (ValueError, KeyError, TypeError, AttributeError) as e:
        raise SystemExit(f"data/n/gvec/gvec.json is not a G-VEC record ({type(e).__name__})")
    if head != (gvec.RECORD_SCHEMA, gvec.STAGE, "PASS") or site not in tuple(int(i) for i in indices) \
            or rsite != site:
        raise SystemExit("data/n/gvec/gvec.json is not a G-VEC PASS record at a candidate site")
    fname = gvec.directions_file(site)
    dp = d / fname
    db = dp.read_bytes() if dp.is_file() else None
    if db is None or committed(dp) != db or hashlib.sha256(db).hexdigest() != fshas.get(fname):
        raise SystemExit(f"data/n/gvec/{fname} is absent, not HEAD's committed bytes, or not the record's")
    rows = gvec.read_rows(dp)
    v_unit = rows[gvec.NAMED.index("valence")]
    v_sha = gvec.injection_sha16(v_unit)
    if v_sha != v_rec:
        raise SystemExit("the valence row's sha16 is not the record's of_record one")
    g_unit = rows[gvec.NAMED.index(gcal.GATE_DIRECTION)]
    g_sha = gvec.injection_sha16(g_unit)
    if g_sha != g_rec:
        raise SystemExit(f"the {gcal.GATE_DIRECTION} row's sha16 is not the record's of_record one (the gate's row)")
    return {"site": site, "R": R, "R_ell": R_ell, "v_unit": v_unit, "v_sha16": v_sha, "g_unit": g_unit,
            "g_sha16": g_sha, "gvec_sha256": hashlib.sha256(data).hexdigest(),
            "directions_sha256": hashlib.sha256(db).hexdigest()}


def gcal_prompts_check(loaded) -> list:
    """The (v) records, before the load: present under a v block whose prompt_template is ``gcal.prompt_parts``' (the
    rendering's one place); 48 in index order, each the plan's prompt (label, replicate, seed) over the v block's
    labels, which are the (iii) file's; its user turn's and its text's sha256s ``gcal.prompt_parts``'; its ids_sha
    re-derived; gen_start the user turn's count, inside the sequence."""
    import hashlib

    from valence_core.n import gcal, ids, sessions
    if ids.GCAL_FILE not in loaded or "v" not in loaded["manifest"]:
        raise SystemExit("the ids of record hold no (v): G-CAL-n's prompts are rendered first (render-ids-v)")
    v = loaded["manifest"]["v"]
    recs = list(loaded[ids.GCAL_FILE])
    if v["labels"] != ids.labels_of(loaded) or v["prompts"] != len(recs) or len(recs) != gcal.N_TURNS:
        raise SystemExit("(v): its labels are not the (iii) file's, or its count is not 48")
    if v.get("prompt_template") != "".join(gcal.prompt_parts("{zone}")):
        raise SystemExit("(v): its prompt_template is not gcal.prompt_parts' (the rendering's one place)")
    plan = gcal.plan(v["labels"])
    for i, (r, p) in enumerate(zip(recs, plan)):
        u, g = gcal.prompt_parts(r["label"])
        if (r["index"], r["label"], r["rep"], r["seed"]) != (i, p["label"], p["rep"], p["seed"]) \
                or r["user_sha256"] != hashlib.sha256(u.encode("utf-8")).hexdigest() \
                or r["text_sha256"] != hashlib.sha256((u + g).encode("utf-8")).hexdigest() \
                or sessions.ids_sha(r["ids"]) != r["ids_sha"] or r["seq_len"] != len(r["ids"]) \
                or r["gen_start"] != r["user_tokens"] or not 0 < r["gen_start"] < r["seq_len"]:
            raise SystemExit(f"(v) record {i} is not the plan's prompt {i} as rendered")
    return recs


def run_gcal(env: GcalEnv, *, out=None, smoke: int | None = None) -> int:
    """G-CAL-n, in order: refusals; the weights and the driver; the ids of record (the manifest pinned), (v)'s 48
    prompts; the generation window (rule 28(d)(c): the longest forward, a prompt and the cap - 1, within
    ``gcal.GENERATION_WINDOW``); G-VEC's outputs of record; the dose map (before the load: a fold into 0 is refused, the
    seat's); the R6 bridge; the load, its provenance, its shape and its eos (the v block's); ``gcal.compute`` (+rho,
    the baseline, +rho/2, the gate's reward_f020 batch, -rho; the early read after the baseline); the outputs, built
    in a staging folder beside the out folder, each turn logged there as it is generated (GC23 (a)), and renamed into
    place; then the exposure at -rho and the gate's line in the lock's form (the second sitting, §2.5). On any failure
    after that folder is made, it is renamed to the failed-run folder beside it (GC23 (b)), never removed, and the
    failure goes on. Exit 0 on PASS (or a smoke), 2 on a STOP (the early STOP at +rho among them) and 3 on a PAUSE
    (the early PAUSE among them, an incoherent baseline at the early read), each with its record, its turns and the
    dose map, for the seat; a fail at the gate's batch is neither a STOP nor a PAUSE; a refusal raises."""
    import hashlib

    from valence_core.m import resume as m_resume
    from valence_core.m.keys import stream_known_answer
    from valence_core.n import gcal, guard, ids, schema
    say = env.printer
    if smoke is not None:
        if not 1 <= int(smoke) <= GCAL_SMOKE_MAX:
            raise SystemExit(f"--smoke takes 1..{GCAL_SMOKE_MAX} (prompts, at +rho and unsteered only: GC19)")
        if out is None:
            raise SystemExit("a smoke writes only where --out names, a new folder outside the repository")
        if _within(Path(out).resolve(), REPO.resolve()):
            raise SystemExit(f"a smoke writes outside the repository, not {out}")
        out_p = guard.refuse_out(Path(out))
    else:
        if out is not None:
            raise SystemExit("a run of record writes only to data/n/gcal/ (--out is a smoke's)")
        out_p = guard.refuse_out(Path(env.out))
    if out_p.exists():
        raise SystemExit(f"{_shown(out_p)} exists: G-CAL-n writes a new folder and never resumes (GC19)")
    stage = guard.refuse_out(out_p.parent / f".{out_p.name}.staging")
    if stage.exists():
        raise SystemExit(f"{_shown(stage)} exists: a staging folder another run left (a hard stop skips its "
                         f"cleanup); move it aside first")
    failed = guard.refuse_out(out_p.parent / f".{out_p.name}.failed")
    if failed.exists():
        raise SystemExit(f"{_shown(failed)} exists: a failed run's turns, kept for the seat (GC23); a re-run waits for "
                         f"the seat's word (GC19)")
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
    batches = gcal.SMOKE_BATCHES if smoke is not None else gcal.BATCHES
    cap = int(env.cap) if env.cap is not None else gcal.CAP
    if smoke is not None:
        say(f"SMOKE: {smoke} prompts at +rho and unsteered, outside the repository; never of record")
    shown_b = [b for b, _d in batches] + ([gcal.GATE_BATCH] if smoke is None else [])
    say(f"STAGE G-CAL-n: batches {shown_b}; TEMP {gcal.TEMP!r}, cap {cap}; out {_shown(out_p)}")
    w = env.weights()
    say(f"WEIGHTS: {w['repo']} revision {w['revision']}, files_aggregate_sha256 {w['sha256']}; {w['n_files']} files "
        f"at {w['path']}, each at the manifest's byte count (the full re-hash is respawn step (i))")
    drv, head = env.driver()
    dsha = hashlib.sha256(drv).hexdigest()
    if smoke is None and drv != head:
        raise SystemExit("a run of record runs only the committed driver: scripts/n_sessions.py is not HEAD's "
                         "committed bytes (the box answers of 2026-11-18, §2 item 5)")
    say(f"DRIVER scripts/n_sessions.py {dsha}: "
        + ("HEAD's committed bytes" if drv == head else "a smoke's, not HEAD's committed bytes (unchecked)"))
    loaded = env.load_ids()
    if loaded["manifest_sha256"] != ids.MANIFEST_OF_RECORD:
        raise SystemExit("data/n/ids/MANIFEST.json is not the render of record's")
    prompts = gcal_prompts_check(loaded)
    longest = gcal.longest_forward(max(int(r["seq_len"]) for r in prompts), cap)
    if longest > gcal.GENERATION_WINDOW:
        raise SystemExit(f"a prompt's longest forward is {longest} positions (its ids and the cap - 1), over the "
                         f"generation window {gcal.GENERATION_WINDOW} (rule 28(d)(c))")
    gv = gcal_gvec_inputs(env.gvec_dir, env.committed, env.indices)
    try:
        dmap = gcal.dose_map(gv["R"], gv["R_ell"])
    except (schema.SchemaError, ValueError) as e:
        raise SystemExit(f"the dose map is refused before the load (the seat's): {e}")
    say(f"inputs: the ids of record {loaded['manifest_sha256']} ((v): {len(prompts)} prompts, every ids_sha re-derived, "
        f"each the plan's; the longest forward {longest} positions, within the generation window "
        f"{gcal.GENERATION_WINDOW}); G-VEC's record {gv['gvec_sha256']}, site {gv['site']}, R {gv['R']!r}, R_ell "
        f"{gv['R_ell']!r}, valence {gv['v_sha16']}, {gcal.GATE_DIRECTION} {gv['g_sha16']}")
    say(f"dose map: d_eq {dmap['d_eq']!r}, d_20 {dmap['d_20']!r} (rho {dmap['rho']!r}); points "
        + ", ".join(f"{p['label']} {p['value']!r}" + (f" (merged {'+'.join(p['merged'])})" if p["merged"] else "")
                    for p in dmap["points"]))
    n_layers, d_model = env.shape
    pre = env.env_provenance(w["path"])
    if bridge_identifier(pre) != CHARACTERIZED_IDENTIFIER:
        raise SystemExit(f"before the load: the environment's provenance under the default window hashes to "
                         f"{bridge_identifier(pre)}, not the characterization's {CHARACTERIZED_IDENTIFIER} (R6)")
    bid = m_resume.backend_identifier(pre)
    mods = _import_production()
    prov_rec = {"package_sha256": mods["guard"].package_sha256(),
                "imported_sha256": mods["guard"].closure_from_modules(dict(sys.modules)),
                "weights": {"repo": w["repo"], "revision": w["revision"], "sha256": w["sha256"]},
                "backend_identifier": bid, "characterized_identifier": CHARACTERIZED_IDENTIFIER, "pod_id": pod,
                "ids_manifest_sha256": loaded["manifest_sha256"], "driver_sha256": dsha,
                "gvec_sha256": gv["gvec_sha256"], "directions_sha256": gv["directions_sha256"], "site": gv["site"],
                "valence_sha16": gv["v_sha16"], "gate_sha16": gv["g_sha16"], "window": schema.MAX_WINDOW,
                "generation_window": gcal.GENERATION_WINDOW, "longest_forward": longest, "smoke": smoke, "cap": cap}
    t0 = env.clock()
    adapter = env.make_adapter(w["path"])
    load_ms = max(0, int(round((env.clock() - t0) * 1000)))
    prov = adapter.provenance()
    if m_resume.backend_identifier(prov) != bid or bridge_identifier(prov) != CHARACTERIZED_IDENTIFIER:
        raise SystemExit("the loaded adapter's provenance is not the one checked before the load -- refusing")
    if tuple(env.adapter_shape(adapter)) != (n_layers, d_model):
        raise SystemExit(f"the checkpoint is {tuple(env.adapter_shape(adapter))}, not ({n_layers}, {d_model})")
    eos = env.eos_id(adapter)
    if eos is None or int(eos) != int(loaded["manifest"]["v"]["eos_id"]):
        raise SystemExit(f"the tokenizer's eos id {eos!r} is not the (v) render's {loaded['manifest']['v']['eos_id']}")
    say(f"backend: n's identifier {bid} (window {schema.MAX_WINDOW}); the characterization's "
        f"{CHARACTERIZED_IDENTIFIER} under the default window (R6); pod {pod}; load {load_ms} ms; eos {int(eos)}")
    prov_rec["load_ms"] = load_ms
    prov_rec["adapter_provenance"] = m_resume.provenance_record(prov)
    step, fwd, dec = env.step_logits(adapter), env.forward(adapter), env.decoder(adapter)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    stage.mkdir()
    log_p = stage / gcal.OUT_PARTIAL
    try:
        gate = None if smoke is not None else {"unit": gv["g_unit"], "sha16": gv["g_sha16"], "R_ell": gv["R_ell"]}
        res = gcal.compute(step, fwd, dec, prompts, v_unit=gv["v_unit"], v_sha16=gv["v_sha16"], site=gv["site"],
                           R=gv["R"], eos_id=int(eos), batches=batches, gate=gate, n=smoke, cap=cap, say=say,
                           on_turn=lambda r: gcal.append_turn(log_p, r))
        gcal.write(stage, res, dmap, prov_rec)
        log_p.unlink(missing_ok=True)
        os.replace(stage, out_p)
    except BaseException:
        try:
            os.replace(stage, failed)
            say(f"FAILED: the staging folder is kept as {_shown(failed)}, with every turn generated before the failure "
                f"(GC23); nothing is removed")
        except OSError as e:
            say(f"FAILED: the staging folder stays at {_shown(stage)} ({type(e).__name__}); nothing is removed")
        raise
    for p in sorted(out_p.iterdir()):
        say(f"file {_shown(p)} sha256 {hashlib.sha256(p.read_bytes()).hexdigest()}")
    say(f"exposure at -rho (PIN-n-23): {res['exposure_minus_rho']['turns']} turns, "
        f"{res['exposure_minus_rho']['tokens']} tokens, {res['exposure_minus_rho']['draws']} draws")
    gfig = res["figures"].get(gcal.GATE_BATCH)
    if gfig is not None:               # the line LOCK-n carries for N2's decision (the second sitting, §2.5)
        say(f"reward axis 5(d) gate, coherence: {gfig['coherent']} of {gfig['of']}, "
            f"{'PASS' if gfig['pass'] else 'FAIL'}")
    status = res["status"]
    if status == "STOP":
        if res.get("early_stop"):
            say("G-CAL-n STOP: a hurdle failed at +rho, before any -rho turn (the seat's early STOP, §1.12); the "
                "record, the turns and the dose map are written; the seat rules")
        else:
            say("G-CAL-n STOP: a hurdle failed at -rho (n:113); the record, the turns and the dose map are written; "
                "the seat rules")
        return 2
    if status == "PAUSE":
        if res.get("early_pause"):
            say("G-CAL-n PAUSE: the baseline is below 36 of 48 coherent at the early read (O7), before any +rho/2, "
                "gate or -rho turn (the seat's early PAUSE, O2); the record, the turns and the dose map are written; "
                "the seat rules")
        else:
            say("G-CAL-n PAUSE: a hurdle failed at +rho/2 alone (GC14; an incoherent baseline ends the run at the "
                "early read); the record, the turns and the dose map are written; the seat rules")
        return 3
    say(f"G-CAL-n {status}" + (", never of record" if status == "SMOKE" else "; the dose map is pinnable"))
    return 0


def cmd_gcal(out=None, smoke: int | None = None) -> int:
    return run_gcal(production_gcal_env(), out=out, smoke=smoke)


def _pi_date_ok(pi_date) -> bool:
    import datetime
    import re
    try:
        return re.fullmatch(r"\d{4}-\d{2}-\d{2}", pi_date or "") is not None \
            and datetime.date.fromisoformat(pi_date).isoformat() == pi_date
    except ValueError:
        return False


def cmd_render_ids_v(tokenizer_dir: str, out: str, pi_date: str) -> int:
    """(v), G-CAL-n's prompts (ADDENDUM-n1 §1.2 (v)), in G-DATA's environment on the laptop, into a new folder outside
    the repository; the commit copies from it."""
    import platform

    from valence_core.n import gcal, guard, ids
    if not _pi_date_ok(pi_date):
        raise SystemExit("--pi-date is the PI's calendar date, YYYY-MM-DD")
    p = Path(out).resolve()
    if _within(p, REPO.resolve()):
        raise SystemExit("render-ids-v writes into a new folder outside the repository; the commit copies from it")
    out_dir = guard.refuse_out(p)
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
    enc, _enc_special = _encoders(tok)
    labels = ids.labels_of(ids.load(ids.IDS_DIR))
    rep = ids.render_v(labels, enc, env, shas, pi_date, ids.IDS_DIR, out_dir, prompt_parts=gcal.prompt_parts,
                       plan=gcal.plan)
    print("render-ids-v (ADDENDUM-n1 §1.2 (v)):")
    print(json.dumps(ids.printable(rep), sort_keys=True))
    return 0 if rep["status"] == "PASS" else 1


GCAL_FLAGS = ("length_collapse", "repetition_loop", "low_diversity", "coherent")


def gcal_decode_compare(record_bytes: bytes, turns_bytes: bytes, decode: Callable) -> dict:
    """A-n1 §1.4's one comparison: the record a G-CAL-n record, the turns file at its sha256; each turn's emitted ids
    decoded here, against the box's decode it records. Returns both files' sha256s; the counts; each batch's coherent
    count under the box's flags (as recorded) and under the laptop's decode; and each difference (batch, index, the two
    decodes, the three flags and the verdict under each, whether any differs)."""
    import hashlib

    from valence_core.n import gcal
    try:
        record = json.loads(record_bytes.decode("utf-8"))
        head, want = (record["schema"], record["stage"]), record["files_sha256"][gcal.OUT_TURNS]
    except (ValueError, KeyError, TypeError) as e:
        raise SystemExit(f"{gcal.OUT_RECORD} is not a G-CAL-n record ({type(e).__name__})")
    if head != (gcal.RECORD_SCHEMA, gcal.STAGE):
        raise SystemExit(f"{gcal.OUT_RECORD} is not a G-CAL-n record")
    tsha = hashlib.sha256(turns_bytes).hexdigest()
    if tsha != want:
        raise SystemExit(f"{gcal.OUT_TURNS} is not at the record's sha256")
    rows = [json.loads(x) for x in turns_bytes.decode("utf-8").splitlines()]
    diffs, by_batch = [], {}
    for r in rows:
        here = decode(r["ids"])
        ch = gcal.coherence(here)
        fb = {k: r["coherence"][k] for k in GCAL_FLAGS}
        fl = {k: ch[k] for k in GCAL_FLAGS}
        cb = by_batch.setdefault(r["batch"], {"box": 0, "laptop": 0})
        cb["box"] += int(bool(fb["coherent"]))
        cb["laptop"] += int(bool(fl["coherent"]))
        if here != r["decode"]:
            diffs.append({"batch": r["batch"], "index": r["index"], "box": r["decode"], "laptop": here,
                          "box_flags": fb, "laptop_flags": fl, "flags_differ": fb != fl})
    return {"record_sha256": hashlib.sha256(record_bytes).hexdigest(), "turns_sha256": tsha, "turns": len(rows),
            "equal": len(rows) - len(diffs), "different": len(diffs),
            "flags_differ": sum(1 for x in diffs if x["flags_differ"]), "coherent_by_batch": by_batch,
            "differences": diffs}


def cmd_gcal_decode(gcal_dir: str, tokenizer_dir: str) -> int:
    """The laptop's decode of G-CAL-n's turns (A-n1 §1.4; GC17), in G-DATA's environment: the record and turns copied
    back from the box, the tokenizer of record; prints the counts and every difference."""
    import platform

    from valence_core.n import gcal, ids
    d = Path(gcal_dir)
    rb, tb = (d / gcal.OUT_RECORD).read_bytes(), (d / gcal.OUT_TURNS).read_bytes()
    import tokenizers
    import transformers
    from transformers import AutoTokenizer
    env = {"python": platform.python_version(), "transformers": transformers.__version__,
           "tokenizers": tokenizers.__version__}
    print(f"environment: python {env['python']} | transformers {env['transformers']} | tokenizers {env['tokenizers']}")
    ids.check_environment(env)
    ids.check_tokenizer_dir(tokenizer_dir)
    tok = AutoTokenizer.from_pretrained(tokenizer_dir, local_files_only=True)
    rep = gcal_decode_compare(rb, tb, _decoder(tok))
    print(f"files: {gcal.OUT_RECORD} sha256 {rep['record_sha256']}; {gcal.OUT_TURNS} sha256 {rep['turns_sha256']} "
          f"(the record's)")
    print(f"decode comparison (A-n1 §1.4): {rep['turns']} turns, {rep['equal']} equal, {rep['different']} different, "
          f"{rep['flags_differ']} of them with a flag that differs")
    for b, c in rep["coherent_by_batch"].items():
        print(f"coherent {b}: {c['box']} under the box's flags, {c['laptop']} under the laptop's decode")
    for x in rep["differences"]:
        print(f"difference {x['batch']} {x['index']}: box {json.dumps(x['box'])} | laptop {json.dumps(x['laptop'])} | "
              f"flags box {json.dumps(x['box_flags'], sort_keys=True)} laptop "
              f"{json.dumps(x['laptop_flags'], sort_keys=True)}")
    return 0


def _gcal_selftest(chk, tmp: Path) -> None:
    """G-CAL-n's command, model-free: its flow over the numpy double behind every seam (a run of record into a folder
    under tmp, the gate's batch among its turns and the run tied to G-VEC's rows at its site; its PASS, STOP and
    PAUSE exits through a stand-in compute, the early PAUSE's among them; a smoke; a failure at the first forward and
    one mid-run; a non-finite arrival score; the early STOP; the early PAUSE on non-empty incoherent turns), its
    refusals before and after the load, the (v) and G-VEC input checks (the gate's row among them), the decode
    comparison, render-ids-v's refusals, main()'s dispatch, and on the box the HF path (the gate's steering check among
    it). It writes only under tmp."""
    import contextlib
    import hashlib
    import io
    import types

    import numpy as np

    from valence_core.m import resume as m_resume
    from valence_core.n import gcal, gvec, ids, schema, sessions
    tmp.mkdir(parents=True, exist_ok=True)
    be = gcal.testing_double()
    site, L = 3, (2, 3)

    def refused(fn) -> bool:
        try:
            fn()
        except SystemExit:
            return True
        return False
    # G-VEC's outputs of record, a fake: the record and the site's directions file, and HEAD's bytes of each
    gdir = tmp / "gvec_rec"
    gdir.mkdir()
    rng = np.random.default_rng(19)
    rows = np.stack([gvec.unit32(rng.normal(size=be.d_model)) for _ in gvec.NAMED]).astype(np.float32)
    fname = gvec.directions_file(site)
    with open(gdir / fname, "wb") as fh:
        np.save(fh, rows, allow_pickle=False)
    v_sha = gvec.injection_sha16(rows[0])
    g_sha = gvec.injection_sha16(rows[gvec.NAMED.index(gcal.GATE_DIRECTION)])
    R_t, Rl_t = 3.0, 4.0                # R and R_ell apart, so that no check takes one for the other (the review's F3)

    def ofr_of(**over):            # G-VEC's of_record as the fake writes it, both rows' sha16s, a field changed
        out_ = {"site": site, "R": R_t, "R_ell": Rl_t,
                "directions": {"valence": v_sha, gcal.GATE_DIRECTION: g_sha}}
        out_.update(over)
        return out_

    def write_gvec(folder, **over):
        folder.mkdir(parents=True, exist_ok=True)
        if folder != gdir:
            (folder / fname).write_bytes((gdir / fname).read_bytes())
        rec = {"schema": gvec.RECORD_SCHEMA, "stage": gvec.STAGE, "status": "PASS", "site": {"site": site},
               "of_record": dict(ofr_of(), route_line=gvec.ROUTE_LINE),
               "files_sha256": {fname: hashlib.sha256((folder / fname).read_bytes()).hexdigest()}}
        for k, v in over.items():
            rec[k] = v
        (folder / gvec.OUT_RECORD).write_text(json.dumps(rec, sort_keys=True) + "\n", encoding="utf-8")
        return {p.resolve(): p.read_bytes() for p in folder.iterdir()}
    snap = write_gvec(gdir)
    labs = sorted(["Zone B8", "Zone D7", "Zone H0", "Zone K7", "Zone L4", "Zone M2", "Zone N1", "Zone Q3", "Zone R9",
                   "Zone T5", "Zone V3", "Zone W6"])

    def vrec(p):
        u, g = gcal.prompt_parts(p["label"])
        ii = [3, 4, 5, 6, 8 + p["index"] % 5]
        return {"index": p["index"], "label": p["label"], "rep": p["rep"], "seed": p["seed"],
                "user_sha256": hashlib.sha256(u.encode("utf-8")).hexdigest(),
                "text_sha256": hashlib.sha256((u + g).encode("utf-8")).hexdigest(), "user_tokens": 3, "gen_start": 3,
                "seq_len": len(ii), "ids_sha": sessions.ids_sha(ii), "ids": ii}
    vrecs = [vrec(p) for p in gcal.plan(labs)]
    vblock0 = {"labels": labs, "prompts": 48, "eos_id": 7, "prompt_template": "".join(gcal.prompt_parts("{zone}"))}

    def loaded_of(v_=None, man=None, vblock=None, cand=None, drop_v=False):
        out_ = {"manifest_sha256": man or ids.MANIFEST_OF_RECORD,
                "manifest": {} if drop_v else {"v": vblock or vblock0},
                ids.LABELS_FILE: [{"candidates": [{"labels": {lab: [1] for lab in (cand or labs)}}]}]}
        if not drop_v:
            out_[ids.GCAL_FILE] = v_ if v_ is not None else vrecs
        return out_
    prov_t = dict(CHARACTERIZED_PROVENANCE, path="(toy)", choice_window_declared=schema.MAX_WINDOW)
    made: list = []

    class StubAdapter:
        def __init__(self, prov):
            self._prov = prov

        def provenance(self):
            return dict(self._prov)

    def dec_of(_a):                # at the self-test's cap of 6, every turn with an id coherent, an empty one not
        return lambda ii: (" ".join(f"w{int(i) % 11}" for i in ii) + " and the light is soft") if ii else ""

    def dec_plain(_a):             # the plain decode: a turn of one id collapses (fewer than 4 words), non-empty
        return lambda ii: " ".join(f"w{int(i) % 11}" for i in ii)

    def base_step(ii, inj):        # the double's logits; at an unsteered turn's first step (the prompts' 5 ids) the
        # end of turn is never drawn, so every baseline turn has an id and the run of record reaches every batch
        # (the review's F1)
        lg = np.array(be.prefill(ii, inj, ()).logits_last, dtype=np.float64)
        if not inj and len(ii) == 5:
            lg[7] = -50.0
        return lg

    def env_for(tag, **over):
        lines: list = []

        def mk(path, prov=None):
            made.append(tag)
            return StubAdapter(prov or prov_t)
        base = dict(weights=lambda: {"repo": "toy", "revision": "0" * 12, "sha256": "5" * 64, "n_files": 1,
                                     "path": "(toy)"},
                    load_ids=lambda: loaded_of(), gvec_dir=gdir, committed=lambda p: snap.get(Path(p).resolve()),
                    env_provenance=lambda p: dict(prov_t), make_adapter=mk, adapter_shape=lambda a: (4, 8),
                    step_logits=lambda a: base_step,
                    forward=lambda a: (lambda ii, layers: be.forward_all(ii, layers)), decoder=dec_of,
                    eos_id=lambda a: 7, pod=lambda: CHARACTERIZED_POD, driver=lambda: (b"drv", b"drv"), indices=L,
                    out=tmp / tag / "gcal", shape=(4, 8), cap=6, printer=lines.append)
        base.update(over)
        if _within(Path(base["out"]).resolve(), REPO.resolve()):    # a self-test writes only under tmp
            raise SystemExit(f"a self-test environment points out into the repository: {base['out']}")
        return GcalEnv(**base), lines
    prod = production_gcal_env()
    chk("driver: G-CAL-n's production seams carry G-VEC's indices (31, 32), data/n/gvec/ as its input and data/n/gcal/ "
        "as its out, the stage's cap",
        (tuple(prod.indices), prod.gvec_dir, prod.out, prod.cap) == (gvec.CANDIDATE_INDICES, GVEC_OUT, GCAL_OUT, None)
        and GCAL_OUT == REPO / "data" / "n" / "gcal", "")
    saved = {k: os.environ.get(k) for k in ("CUBLAS_WORKSPACE_CONFIG",)}
    try:
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = CHARACTERIZED_PROVENANCE["cublas_workspace_config"]
        env1, lines1 = env_for("run")
        real_bf = gcal.batch_figures

        def forced_bf(pass_):          # the hurdles' figures as computed, their pass forced: the self-test's seam only
            def f(t_, b_, s_):
                out = real_bf(t_, b_, s_)
                out["pass"] = bool(pass_)
                return out
            return f
        gcal.batch_figures = forced_bf(True)   # the double's +rho outcome is not the test's: every batch runs
        try:
            rc1 = run_gcal(env1)
        finally:
            gcal.batch_figures = real_bf
        rec1 = json.loads((env1.out / gcal.OUT_RECORD).read_text(encoding="utf-8"))
        names1 = sorted(p.name for p in env1.out.iterdir())
        turns1 = [json.loads(x) for x in (env1.out / gcal.OUT_TURNS).read_text(encoding="utf-8").splitlines()]
        want_rc = {"PASS": 0, "STOP": 2, "PAUSE": 3}.get(rec1["status"])
        chk("driver: G-CAL-n's run of record over the double behind every seam: its three files in a new folder, the "
            "staging folder gone, the exit its status's (0 PASS, 2 STOP, 3 PAUSE)",
            names1 == sorted([gcal.OUT_RECORD, gcal.OUT_TURNS, gcal.OUT_DOSE_MAP]) and rc1 == want_rc
            and not (env1.out.parent / ".gcal.staging").exists() and not (env1.out.parent / ".gcal.failed").exists()
            and len(turns1) == 240 and rec1["early_stop"] is False and rec1["early_pause"] is False
            and rec1["status"] == "PASS" and rec1["batches"] == list(gcal.RECORD_ORDER)
            and rec1["dose_map"] == gcal.dose_map(R_t, Rl_t) and rec1["pinnable"] == (rec1["status"] == "PASS"),
            (rc1, rec1.get("status"), names1))
        gf1 = rec1["figures"][gcal.GATE_BATCH]
        chk("driver: the gate's batch in the run of record (the second sitting, §2.5): span_reward's row of G-VEC's "
            "record, its sha16 of_record's, at f0.20 of R_ell (the campaign's alpha), its 48 turns in the turns file "
            "after the baseline's, its count, pass and stops in the record",
            gf1["sha16"] == g_sha == rec1["provenance"]["gate_sha16"]
            and gf1["alpha"] == schema.expected_alpha("f0.20", 0.20, {"R_ell": Rl_t})
            and [r["batch"] for r in turns1[-gcal.N_TURNS:]] == [gcal.GATE_BATCH] * gcal.N_TURNS
            and gf1["coherent"] == sum(1 for r in turns1[-gcal.N_TURNS:] if r["coherence"]["coherent"])
            and gf1["of"] == gcal.N_TURNS and "stops" in gf1
            and lines1.count(f"reward axis 5(d) gate, coherence: {gf1['coherent']} of 48, "
                             f"{'PASS' if gf1['pass'] else 'FAIL'}") == 1, gf1)
        p0 = next(r for r in turns1 if r["batch"] == "+rho" and r["index"] == 0)
        regen = gcal.generate(base_step, vrecs[0]["ids"], vrecs[0]["gen_start"],
                              gcal.injection_for(1.0, rows[0], site, R_t, v_sha), vrecs[0]["seed"], eos_id=7, cap=6)
        sc1 = next((r for r in turns1 if r["batch"] == "+rho" and r["n_tok"] >= 2), None)
        want_a = None if sc1 is None else float(np.mean(
            (be.forward_all(sc1["ids"], (site,))[site].astype(np.float64) @ rows[0].astype(np.float64))[1:]))
        chk("driver: the run of record is G-VEC's rows at its site: +rho's turn 0 is generate's own under the valence "
            "row's injection at R, and a scored +rho turn's arrival is its projection on that row over positions 1..n "
            "(the review's M4)",
            regen["ids"] == p0["ids"] and sc1 is not None and abs(sc1["arrival"] - want_a) < 1e-12,
            (regen["ids"], p0["ids"]))
        pv = rec1["provenance"]
        chk("driver: the record's provenance: the package and closure, the weights, the identifiers, the pod, the ids of "
            "record, the driver, G-VEC's two files, the site and valence sha16, the two windows and the longest "
            "forward, the cap and the load",
            pv["ids_manifest_sha256"] == ids.MANIFEST_OF_RECORD and pv["site"] == site and pv["valence_sha16"] == v_sha
            and pv["gvec_sha256"] == hashlib.sha256((gdir / gvec.OUT_RECORD).read_bytes()).hexdigest()
            and pv["directions_sha256"] == hashlib.sha256((gdir / fname).read_bytes()).hexdigest()
            and pv["characterized_identifier"] == CHARACTERIZED_IDENTIFIER and pv["pod_id"] == CHARACTERIZED_POD
            and pv["window"] == schema.MAX_WINDOW and pv["cap"] == 6 and pv["smoke"] is None
            and pv["generation_window"] == gcal.GENERATION_WINDOW
            and pv["longest_forward"] == gcal.longest_forward(5, 6)
            and isinstance(pv["load_ms"], int) and len(pv["package_sha256"]) == 64
            and pv["backend_identifier"] == m_resume.backend_identifier(prov_t)
            and pv["adapter_provenance"] == m_resume.provenance_record(prov_t), "")
        heads = ("STAGE G-CAL-n", "WEIGHTS:", "DRIVER", "inputs:", "dose map:", "backend:", "steering check +rho:",
                 "turn +rho 0 ", f"steering check {gcal.GATE_BATCH}:", "batch +rho:", f"batch {gcal.GATE_BATCH} ",
                 "file ", "exposure at -rho", "reward axis 5(d) gate, coherence: ")
        decodes = {r["decode"] for r in turns1 if " " in r["decode"]}     # several words: never a path's chance match
        chk("driver: G-CAL-n prints its lines in order -- STAGE, WEIGHTS, DRIVER, inputs, the dose map, backend, the "
            "steering checks, the turns, the batches and the gate's, each file's sha256, the exposure, the gate's line "
            "in the lock's form -- and no turn's text or id",
            [next((i for i, x in enumerate(lines1) if x.startswith(h)), -1) for h in heads]
            == sorted(next((i for i, x in enumerate(lines1) if x.startswith(h)), -1) for h in heads)
            and all(any(x.startswith(h) for x in lines1) for h in heads)
            and not any(d in x for d in decodes for x in lines1) and not any('"ids"' in x for x in lines1),
            lines1[:6])
        chk("driver: the model loads once, after every check that needs none", made.count("run") == 1, made)
        g = globals()
        real_compute = gcal.compute

        kw_seen: list = []

        def canned(status, early_pause=False):
            def fake(*a, **k):
                kw_seen.append((sorted(k), k.get("gate")))
                return {"status": status, "turns": {"+rho": [], "-rho": [], "+rho/2": [], "baseline": []},
                        "figures": {}, "exposure_minus_rho": {"turns": 0, "tokens": 0, "draws": 0},
                        "batches": ["+rho", "-rho", "+rho/2", "baseline"], "early_pause": early_pause}
            return fake
        rcs, ends = {}, {}
        try:
            for st, ep in (("PASS", False), ("STOP", False), ("PAUSE", False), ("PAUSE", True)):
                gcal.compute = canned(st, ep)
                e_, l_ = env_for(f"canned_{st}_{ep}")
                key = st + (" early" if ep else "")
                rcs[key] = run_gcal(e_)
                ends[key] = (l_[-1], json.loads((e_.out / gcal.OUT_RECORD).read_text())["pinnable"],
                             sorted(p.name for p in e_.out.iterdir()))
        finally:
            gcal.compute = real_compute
        chk("driver: G-CAL-n's exits: PASS 0 (the dose map pinnable), a STOP 2 and a PAUSE 3 (the early PAUSE's its "
            "own line), each with its record, its turns and the dose map written, for the seat; a run of record hands "
            "compute the gate's row, its sha16 and R_ell, never a figures seam",
            rcs == {"PASS": 0, "STOP": 2, "PAUSE": 3, "PAUSE early": 3}
            and ends["PASS"][:2] == ("G-CAL-n PASS; the dose map is pinnable", True)
            and all(v[2] == sorted([gcal.OUT_RECORD, gcal.OUT_TURNS, gcal.OUT_DOSE_MAP]) for v in ends.values())
            and ends["STOP"][0].startswith("G-CAL-n STOP: a hurdle failed at -rho (n:113)") and ends["STOP"][1] is False
            and ends["PAUSE"][0].startswith("G-CAL-n PAUSE: a hurdle failed at +rho/2 alone")
            and ends["PAUSE early"][0].startswith("G-CAL-n PAUSE: the baseline is below 36 of 48 coherent at the "
                                                  "early read")
            and ends["PAUSE"][1] is False and ends["PAUSE early"][1] is False
            and len(kw_seen) == 4 and all("figures_of" not in k for k, _g in kw_seen)
            and all(g_ is not None and g_["sha16"] == g_sha and g_["R_ell"] == Rl_t
                    and gvec.injection_sha16(g_["unit"]) == g_sha for _k, g_ in kw_seen), (rcs, ends))
        env3, l3 = env_for("smoke", driver=lambda: (b"drv-new", b"drv"))
        rc3 = run_gcal(env3, out=tmp / "smoke-out", smoke=2)
        rec3 = json.loads((tmp / "smoke-out" / gcal.OUT_RECORD).read_text())
        t3 = (tmp / "smoke-out" / gcal.OUT_TURNS).read_text().splitlines()
        chk("driver: a smoke runs uncommitted bytes into --out outside the repository: +rho and the baseline only on its "
            "first prompts, never -rho or the gate, its status SMOKE, never of record",
            rc3 == 0 and rec3["status"] == "SMOKE" and rec3["batches"] == ["+rho", "baseline"] and len(t3) == 4
            and rec3["exposure_minus_rho"] == {"turns": 0, "tokens": 0, "draws": 0} and not env3.out.exists()
            and rec3["early_stop"] is False and rec3["early_pause"] is False and not any("early STOP" in x for x in l3)
            and gcal.GATE_BATCH not in rec3["figures"] and not any("early PAUSE" in x for x in l3)
            and any(x.startswith("SMOKE:") for x in l3)
            and any("a smoke's, not HEAD's committed bytes" in x for x in l3), (rc3, rec3.get("status")))

        def broken(_a):
            def f(ii, inj):
                raise RuntimeError("the forward failed")
            return f
        env4, l4 = env_for("fail", step_logits=broken)
        try:
            run_gcal(env4)
            failed = False
        except RuntimeError:
            failed = True
        fdir4 = env4.out.parent / ".gcal.failed"
        chk("driver: GC23 (b): a failure after the load leaves no out folder and no staging folder; the staging folder "
            "is kept as the failed-run folder, here with no turn (the first forward failed), and the failure goes on",
            failed and not env4.out.exists() and not (env4.out.parent / ".gcal.staging").exists() and fdir4.is_dir()
            and not any(fdir4.iterdir()) and any(x.startswith("FAILED:") for x in l4), l4[-2:])

        def flaky(_a):             # the forward fails at its 61st call, mid-way through the first batch generated
            n_calls = [0]

            def f(ii, inj):
                n_calls[0] += 1
                if n_calls[0] > 60:
                    raise RuntimeError("the forward failed mid-run")
                return base_step(ii, inj)
            return f
        env5, _l5 = env_for("midfail", step_logits=flaky)
        try:                           # the 61st forward fails before the early read, which needs 98 at least
            run_gcal(env5)
            failed5 = False
        except RuntimeError:
            failed5 = True
        log5 = env5.out.parent / ".gcal.failed" / gcal.OUT_PARTIAL
        logged = [json.loads(x) for x in log5.read_text(encoding="utf-8").splitlines()] if log5.is_file() else []
        own = {(r["batch"], r["index"]): r for r in turns1}
        seq5 = [(b, i) for b in gcal.GENERATION_ORDER for i in range(gcal.N_TURNS)]
        k5, calls5, past5 = 0, 0, False   # the turns whose every forward precedes the 61st, in the order of generation
        for b in gcal.GENERATION_ORDER:
            if b in gcal.CHECKED:
                calls5 += 2                # the steering check's two forwards
                if calls5 > 60:
                    break
            for i in range(gcal.N_TURNS):
                r = own[(b, i)]
                calls5 += int(r["n_tok"]) + (1 if r["stop"] == "eos" else 0)
                if calls5 > 60:
                    past5 = True
                    break
                k5 += 1
            if past5:
                break
        chk("driver: GC23 (a)-(b): a failure mid-run keeps, in the failed-run folder's log, every turn generated "
            "before it and no other, in the order of generation, each the run of record's own turn with its arrival "
            "not yet scored", failed5 and not env5.out.exists() and k5 >= 1 and len(logged) == k5
            and [(r["batch"], r["index"]) for r in logged] == seq5[:k5]
            and all(r["ids"] == own[(r["batch"], r["index"])]["ids"] and r["arrival"] is None for r in logged),
            (len(logged), k5))
        env6, _l6 = env_for("nanarr", forward=lambda a: (lambda ii, layers: {int(layers[0]): np.full((len(ii), 8),
                                                                                                    np.nan)}))
        try:
            run_gcal(env6)
            failed6 = False
        except ValueError:
            failed6 = True
        log6 = env6.out.parent / ".gcal.failed" / gcal.OUT_PARTIAL
        rows6 = [json.loads(x) for x in log6.read_text(encoding="utf-8").splitlines()] if log6.is_file() else []
        chk("driver: GC23 (c), under the seat's order: a non-finite arrival score is a failure when its batch is "
            "scored, here +rho's after its 48 turns and before any other batch; the failed-run folder's log holds "
            "those 48", failed6 and not env6.out.exists() and len(rows6) == 48
            and all(r["batch"] == "+rho" for r in rows6), len(rows6))
        alph7: list = []

        def recording(_a):             # the double's step, recording every alpha it is handed
            def f(ii, inj):
                alph7.extend(round(i.alpha, 12) for i in inj)
                return base_step(ii, inj)
            return f
        env7, l7 = env_for("earlystop", step_logits=recording)
        gcal.batch_figures = forced_bf(False)
        try:
            rc7 = run_gcal(env7)
        finally:
            gcal.batch_figures = real_bf
        rec7 = json.loads((env7.out / gcal.OUT_RECORD).read_text(encoding="utf-8"))
        t7 = (env7.out / gcal.OUT_TURNS).read_text(encoding="utf-8").splitlines()
        chk("driver: the seat's early STOP (§1.12): a fail at +rho ends the run as a STOP (exit 2) with the record, "
            "the turns and the dose map written, +rho and the baseline alone, and no step is ever handed a -rho or "
            "+rho/2 injection; the hurdles' seam is restored after the last patch",
            rc7 == 2 and rec7["status"] == "STOP" and rec7["early_stop"] is True and gcal.batch_figures is real_bf
            and rec7["early_pause"] is False
            and rec7["batches"] == ["+rho", "baseline"] and len(t7) == 96 and (env7.out / gcal.OUT_DOSE_MAP).is_file()
            and rec7["exposure_minus_rho"]["turns"] == 0 and len(set(alph7)) == 1 and min(alph7) > 0
            and any(x.startswith("G-CAL-n STOP: a hurdle failed at +rho, before any -rho turn") for x in l7),
            (rc7, rec7.get("status"), sorted(set(alph7))))
        alph8: list = []

        def mute_base(_a):             # the double's step, and an unsteered turn one id (13) then the end of turn:
            def f(ii, inj):            # non-empty and, on the plain decode, incoherent (the review's F2)
                alph8.extend(round(i.alpha, 12) for i in inj)
                lg = np.asarray(be.prefill(ii, inj, ()).logits_last, dtype=np.float64)
                if not inj:
                    lg = np.full_like(lg, -50.0)
                    lg[13 if len(ii) == 5 else 7] = 50.0
                return lg
            return f
        env8, l8 = env_for("earlypause", step_logits=mute_base, decoder=dec_plain)
        gcal.batch_figures = forced_bf(True)
        try:
            rc8 = run_gcal(env8)
        finally:
            gcal.batch_figures = real_bf
        rec8 = json.loads((env8.out / gcal.OUT_RECORD).read_text(encoding="utf-8"))
        t8 = (env8.out / gcal.OUT_TURNS).read_text(encoding="utf-8").splitlines()
        b8 = [json.loads(x) for x in t8 if json.loads(x)["batch"] == "baseline"]
        chk("driver: the seat's early PAUSE (O2, the second sitting §3): +rho passing and a baseline below 36 of 48 "
            "coherent, every baseline turn non-empty, end the run as a PAUSE (exit 3) with the record, the turns and "
            "the dose map written, +rho and the baseline alone, no +rho/2, gate or -rho injection ever handed; the "
            "hurdles' seam restored",
            rc8 == 3 and rec8["status"] == "PAUSE" and rec8["early_pause"] is True and rec8["early_stop"] is False
            and len(b8) == 48 and all(r["n_tok"] == 1 and not r["coherence"]["coherent"] for r in b8)
            and gcal.batch_figures is real_bf and rec8["batches"] == ["+rho", "baseline"] and len(t8) == 96
            and (env8.out / gcal.OUT_DOSE_MAP).is_file() and rec8["exposure_minus_rho"]["turns"] == 0
            and set(alph8) == {round(schema.RHO * R_t, 12)}
            and l8[-1].startswith("G-CAL-n PAUSE: the baseline is below 36 of 48 coherent at the early read"),
            (rc8, rec8.get("status"), sorted(set(alph8))))
        # refusals, each before the load
        n_made = len(made)
        pre_out = tmp / "exists" / "gcal"
        pre_out.mkdir(parents=True)
        leftover = tmp / "lefto" / ".gcal.staging"
        leftover.mkdir(parents=True)
        (tmp / "leftf" / ".gcal.failed").mkdir(parents=True)

        def with_v(i, **kw):
            out_ = [dict(r) for r in vrecs]
            out_[i].update(kw)
            return out_
        long_v = with_v(4, ids=[3] * schema.MAX_WINDOW)
        long_v[4].update(seq_len=schema.MAX_WINDOW, ids_sha=sessions.ids_sha([3] * schema.MAX_WINDOW))

        def gv_env(tag, **rec_over):
            folder = tmp / f"gvec_{tag}"
            s_ = write_gvec(folder, **rec_over)
            return env_for(tag, gvec_dir=folder, committed=lambda p: s_.get(Path(p).resolve()))[0]
        nocommit = env_for("x31", committed=lambda p: None)[0]
        bad_dir = tmp / "gvec_baddir"
        s_bad = write_gvec(bad_dir)
        (bad_dir / fname).write_bytes((gdir / fname).read_bytes()[:-4] + b"\x00\x00\x00\x00")
        baddir_env = env_for("x32", gvec_dir=bad_dir, committed=lambda p: s_bad.get(Path(p).resolve()))[0]
        cd_dir = tmp / "gvec_cdiff"            # the directions file at the record's sha256, but not HEAD's bytes
        s_cd = write_gvec(cd_dir)
        cdiff_env = env_for("x40", gvec_dir=cd_dir,
                            committed=lambda p: b"other" if Path(p).name == fname else s_cd.get(Path(p).resolve()))[0]
        cases = [
            ("an existing out folder (G-CAL-n never resumes)", lambda: run_gcal(env_for("x1", out=pre_out)[0])),
            ("a staging folder a hard stop left", lambda: run_gcal(env_for("lefto")[0])),
            ("a failed run's folder (GC23: a re-run waits for the seat's word)",
             lambda: run_gcal(env_for("leftf")[0])),
            ("--out on a run of record", lambda: run_gcal(env_for("x2")[0], out=tmp / "o2")),
            ("a smoke without --out", lambda: run_gcal(env_for("x3")[0], smoke=2)),
            ("a smoke whose --out is in the repository",
             lambda: run_gcal(env_for("x4")[0], out=REPO / "data" / "n" / "gcal-smoke", smoke=2)),
            ("a smoke of 5", lambda: run_gcal(env_for("x5")[0], out=tmp / "o5", smoke=5)),
            ("a smoke of 0", lambda: run_gcal(env_for("x5b")[0], out=tmp / "o5b", smoke=0)),
            ("no pod id", lambda: run_gcal(env_for("x6", pod=lambda: None)[0])),
            ("another pod", lambda: run_gcal(env_for("x7", pod=lambda: "other-pod")[0])),
            ("a run of record on uncommitted driver bytes",
             lambda: run_gcal(env_for("x8", driver=lambda: (b"new", b"old"))[0])),
            ("ids not of record", lambda: run_gcal(env_for("x9", load_ids=lambda: loaded_of(man="0" * 64))[0])),
            ("ids without (v)", lambda: run_gcal(env_for("x10", load_ids=lambda: loaded_of(drop_v=True))[0])),
            ("a (v) record with another label",
             lambda: run_gcal(env_for("x11", load_ids=lambda: loaded_of(v_=with_v(0, label="Zone Q3")))[0])),
            ("a (v) record with another seed",
             lambda: run_gcal(env_for("x12", load_ids=lambda: loaded_of(v_=with_v(1, seed=1)))[0])),
            ("a (v) record with another replicate",
             lambda: run_gcal(env_for("x13", load_ids=lambda: loaded_of(v_=with_v(2, rep=3)))[0])),
            ("a (v) record whose text sha256 is not prompt_parts'",
             lambda: run_gcal(env_for("x14", load_ids=lambda: loaded_of(v_=with_v(3, text_sha256="0" * 64)))[0])),
            ("a (v) record whose user turn's sha256 is not prompt_parts'",
             lambda: run_gcal(env_for("x14b", load_ids=lambda: loaded_of(v_=with_v(3, user_sha256="0" * 64)))[0])),
            ("a (v) block whose prompt_template is not prompt_parts'",
             lambda: run_gcal(env_for("x14c", load_ids=lambda: loaded_of(
                 vblock=dict(vblock0, prompt_template="<|user|>\n{zone}\n")))[0])),
            ("a (v) record whose ids do not hash to its ids_sha",
             lambda: run_gcal(env_for("x15", load_ids=lambda: loaded_of(v_=with_v(5, ids_sha="0" * 16)))[0])),
            ("a (v) record whose gen_start is not the user turn's count",
             lambda: run_gcal(env_for("x16", load_ids=lambda: loaded_of(v_=with_v(6, gen_start=2)))[0])),
            ("a (v) record whose gen_start is at its end",
             lambda: run_gcal(env_for("x16b", load_ids=lambda: loaded_of(v_=with_v(6, gen_start=5, user_tokens=5)))[0])),
            ("a (v) record whose seq_len is not its ids'",
             lambda: run_gcal(env_for("x17", load_ids=lambda: loaded_of(v_=with_v(7, seq_len=9)))[0])),
            ("(v) out of index order",
             lambda: run_gcal(env_for("x18", load_ids=lambda: loaded_of(v_=[vrecs[1], vrecs[0]] + vrecs[2:]))[0])),
            ("(v) of 47 prompts", lambda: run_gcal(env_for("x19", load_ids=lambda: loaded_of(v_=vrecs[:47]))[0])),
            ("(v) labels that are not the (iii) file's",
             lambda: run_gcal(env_for("x20", load_ids=lambda: loaded_of(cand=labs[:11] + ["Zone A1"]))[0])),
            ("a prompt whose longest forward is over the generation window",
             lambda: run_gcal(env_for("x21", load_ids=lambda: loaded_of(v_=long_v))[0])),
            ("G-VEC's record absent", lambda: run_gcal(env_for("x30", gvec_dir=tmp / "no-gvec")[0])),
            ("G-VEC's record not HEAD's committed bytes", lambda: run_gcal(nocommit)),
            ("G-VEC's record a STOP", lambda: run_gcal(gv_env("x33", status="STOP"))),
            ("G-VEC's record of another stage", lambda: run_gcal(gv_env("x34", stage="G-CAL-n"))),
            ("G-VEC's site not a candidate index",
             lambda: run_gcal(gv_env("x35", of_record=ofr_of(site=1), site={"site": 1}))),
            ("G-VEC's directions file not the record's", lambda: run_gcal(baddir_env)),
            ("G-VEC's directions file at the record's sha256 but not HEAD's bytes", lambda: run_gcal(cdiff_env)),
            ("G-VEC's directions file HEAD's bytes but not at the record's sha256",
             lambda: run_gcal(gv_env("x41", files_sha256={fname: "0" * 64}))),
            ("G-VEC's record whose site block is not its of_record's site",
             lambda: run_gcal(gv_env("x39", site={"site": 2}))),
            ("G-VEC's record with no site block", lambda: run_gcal(gv_env("x42", site=None))),
            ("G-VEC's of_record with no directions",
             lambda: run_gcal(gv_env("x43", of_record={"site": site, "R": R_t, "R_ell": Rl_t}))),
            ("G-VEC's record with no files_sha256 map", lambda: run_gcal(gv_env("x44", files_sha256=None))),
            ("a G-VEC R that is not positive (the dose map's ValueError)",
             lambda: run_gcal(gv_env("x45", of_record=ofr_of(R=-1.0)))),
            ("a valence row not of_record's sha16",
             lambda: run_gcal(gv_env("x36", of_record=ofr_of(directions={"valence": "0" * 16,
                                                                         gcal.GATE_DIRECTION: g_sha})))),
            ("the gate's span_reward row not of_record's sha16 (the second sitting, §2.5)",
             lambda: run_gcal(gv_env("x46", of_record=ofr_of(directions={"valence": v_sha,
                                                                         gcal.GATE_DIRECTION: "0" * 16})))),
            ("G-VEC's of_record with no span_reward sha16",
             lambda: run_gcal(gv_env("x47", of_record=ofr_of(directions={"valence": v_sha})))),
            ("a dose map that folds into 0 (the seat's)",
             lambda: run_gcal(gv_env("x37", of_record=ofr_of(R=25.49, R_ell=0.3 * 25.49 * 0.4)))),
            ("a provenance off the characterization before the load",
             lambda: run_gcal(env_for("x38", env_provenance=lambda p: dict(prov_t, gpu="another GPU"))[0])),
        ]
        out_r = {name: refused(fn) for name, fn in cases}
        chk("driver: G-CAL-n refuses, before the load: " + "; ".join(name for name, _f in cases),
            all(out_r.values()) and len(made) == n_made, [k for k, v in out_r.items() if not v])
        mk_bad = env_for("y1", make_adapter=lambda p: (made.append("y1"), StubAdapter(dict(prov_t, gpu="x")))[1])[0]
        shp_bad = env_for("y2", adapter_shape=lambda a: (4, 16))[0]
        eos_bad = env_for("y3", eos_id=lambda a: 8)[0]
        chk("driver: G-CAL-n refuses after the load a provenance not the one checked before it, a checkpoint of another "
            "shape and an eos id not the (v) render's, writing nothing",
            refused(lambda: run_gcal(mk_bad)) and refused(lambda: run_gcal(shp_bad))
            and refused(lambda: run_gcal(eos_bad)) and not mk_bad.out.exists() and not shp_bad.out.exists()
            and not eos_bad.out.exists(), "")
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
        chk("driver: G-CAL-n refuses a cuBLAS setting other than the characterized one (rule 2), before the load",
            refused(lambda: run_gcal(env_for("y4")[0])) and made.count("y4") == 0, "")
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    # the decode comparison (A-n1 §1.4), on the run's own outputs
    rb_b, tb = (env1.out / gcal.OUT_RECORD).read_bytes(), (env1.out / gcal.OUT_TURNS).read_bytes()
    first_id = turns1[0]["ids"][:1]
    same = gcal_decode_compare(rb_b, tb, dec_of(None))
    off = gcal_decode_compare(rb_b, tb, lambda ii: dec_of(None)(ii) + ("!" if ii[:1] == first_id else ""))
    flip = gcal_decode_compare(rb_b, tb, lambda ii: "" if ii[:1] == first_id else dec_of(None)(ii))
    other = json.dumps(dict(json.loads(rb_b.decode("utf-8")), stage="G-VEC")).encode("utf-8")
    keys_d = {"batch", "index", "box", "laptop", "box_flags", "laptop_flags", "flags_differ"}
    chk("driver: the decode comparison names both files by sha256 and counts every turn, equal where the laptop's "
        "decode is the box's; it names each difference with the three flags and the verdict under both decodes, and "
        "each batch's coherent count under both; a turns file not at the record's sha256, and a record of another "
        "stage, are refused", same["record_sha256"] == hashlib.sha256(rb_b).hexdigest()
        and same["turns_sha256"] == hashlib.sha256(tb).hexdigest()
        and same["turns"] == 240 and same["equal"] == 240 and same["different"] == 0 and same["flags_differ"] == 0
        and sorted(same["coherent_by_batch"]) == sorted(gcal.RECORD_ORDER)
        and all(c["box"] == c["laptop"] for c in same["coherent_by_batch"].values())
        and off["different"] >= 1 and all(set(x) == keys_d for x in off["differences"])
        and turns1[0]["n_tok"] > 0
        and flip["flags_differ"] >= 1 and all(x["laptop_flags"]["length_collapse"] for x in flip["differences"])
        and refused(lambda: gcal_decode_compare(rb_b, tb + b"\n", dec_of(None)))
        and refused(lambda: gcal_decode_compare(other, tb, dec_of(None))),
        (same["different"], off["different"], flip["flags_differ"]))
    libs = ("transformers", "tokenizers")
    before = [m for m in libs if m in sys.modules]
    r_in = refused(lambda: cmd_render_ids_v(str(tmp / "no-tok"), str(ids.IDS_DIR / "v"), "2026-11-20"))
    r_date = refused(lambda: cmd_render_ids_v(str(tmp / "no-tok"), str(tmp / "v-out"), "Nov 20"))
    after = [m for m in libs if m in sys.modules]
    chk("driver: render-ids-v refuses an --out inside the repository and a --pi-date not YYYY-MM-DD, importing no "
        "tokenizer library", r_in and r_date and not (set(after) - set(before)), (before, after))

    def argv_error(argv) -> str:
        buf = io.StringIO()
        try:
            with contextlib.redirect_stderr(buf):
                main(argv)
        except SystemExit:
            return buf.getvalue()
        return "no error"
    t_ = str(tmp)
    day = "2026-11-19"
    foreign_g = [["--root", t_], ["--report", t_], ["--resume"], ["--ruling", "p01=x"], ["--convention", "space"],
                 ["--model-dir", t_], ["--tokenizer-dir", t_], ["--ids-dir", t_], ["--pi-date", day]]
    foreign_d = [["--root", t_], ["--report", t_], ["--resume"], ["--ruling", "p01=x"], ["--smoke", "2"],
                 ["--convention", "space"], ["--model-dir", t_], ["--ids-dir", t_], ["--out", t_], ["--pi-date", day]]
    v_argv = ["render-ids-v", "--tokenizer-dir", t_, "--out", t_, "--pi-date", day]
    bad_argvs = ([(["gcal"] + f, "gcal takes --out and --smoke only") for f in foreign_g]
                 + [(["gcal-decode", "--gcal-dir", t_, "--tokenizer-dir", t_] + f,
                     "gcal-decode takes --gcal-dir and --tokenizer-dir") for f in foreign_d]
                 + [(["gvec", "--gcal-dir", t_], "--gcal-dir: gcal-decode's option only"),
                    (["gcal", "--gcal-dir", t_], "--gcal-dir: gcal-decode's option only"),
                    (["gcal-decode", "--gcal-dir", t_], "gcal-decode takes --gcal-dir and --tokenizer-dir"),
                    (["gcal-decode", "--tokenizer-dir", t_], "gcal-decode takes --gcal-dir and --tokenizer-dir"),
                    (["render-ids-v", "--tokenizer-dir", t_, "--out", t_], "render-ids-v needs"),
                    (v_argv + ["--model-dir", t_], "render-ids-v needs"),
                    (v_argv + ["--ids-dir", t_], "render-ids-v needs")])
    g = globals()
    real_run = g["run_gcal"]
    calls: list = []

    def recorder(_env, **kw):
        calls.append(kw)
        return 0
    # the review's B1: every main() call here runs with no pod id and a cuBLAS setting the stage refuses, so that no
    # call can reach a load on the box, even were the swap below not to take
    held = {k: os.environ.get(k) for k in ("CUBLAS_WORKSPACE_CONFIG", "RUNPOD_POD_ID")}
    same_g = cmd_gcal.__globals__ is g
    try:
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
        os.environ.pop("RUNPOD_POD_ID", None)
        got_a = [(argv, argv_error(argv)) for argv, _w in bad_argvs]
        g["run_gcal"] = recorder
        try:
            rcs_m = (main(["gcal"]), main(["gcal", "--smoke", "2", "--out", str(tmp / "s")])) if same_g else None
        finally:
            g["run_gcal"] = real_run
    finally:
        for k, v in held.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    chk("driver: main() refuses each of gcal's nine foreign flags, each of gcal-decode's ten, --gcal-dir anywhere but "
        "gcal-decode, gcal-decode without both its folders, and render-ids-v without its three or with a folder option",
        all(w in got for (_argv, got), (_a2, w) in zip(got_a, bad_argvs)),
        [a for (a, got), (_a2, w) in zip(got_a, bad_argvs) if w not in got])
    chk("driver: main() hands G-CAL-n's --out and --smoke to the stage, and nothing on a run of record (the swapped "
        "module is cmd_gcal's; every call ran with no pod id and a cuBLAS setting the stage refuses)",
        same_g and rcs_m == (0, 0) and calls == [{"out": None, "smoke": None}, {"out": str(tmp / "s"), "smoke": 2}],
        calls)
    absent = REPO / "data" / "n" / "gcal" / "absent-selftest.json"
    try:
        got_c = committed_bytes(absent)
    except Exception as e:                              # noqa: BLE001
        got_c = f"raised {type(e).__name__}"
    chk("driver: committed_bytes is git's HEAD, never the working tree: None for a path HEAD does not hold",
        got_c is None and not absent.exists(), got_c)

    class RecordingAdapter:        # the HF seams' wiring, over a stand-in that records what each seam hands it
        def __init__(self):
            self.calls: list = []
            self._tok = types.SimpleNamespace(decode=self._decode)

        def _decode(self, token_ids, **kw):
            self.calls.append(("decode", list(token_ids), kw))
            return "x y"

        def forward(self, ids_, capture_layers=(), injections=()):
            self.calls.append(("forward", list(ids_), tuple(capture_layers), list(injections)))
            return types.SimpleNamespace(logits=np.arange(4.0),
                                         acts={int(i): np.zeros((len(ids_), 2)) for i in capture_layers})
    ra = RecordingAdapter()
    pl = gcal.placed(gcal.injection_for(1.0, rows[0], site, R_t, v_sha), 2)
    lg_r = _hf_step_logits(ra)([3, 4, 5], pl)
    acts_r = _hf_forward(ra)([3, 4], (site,))
    txt_r = _hf_decoder(ra)([5, 6])
    chk("driver: the HF seams' wiring, over a recording stand-in: the step hands the adapter's forward the whole "
        "sequence and every placed injection, no capture, and returns its last-position logits; the capture is "
        "unsteered at the indices given; the decode is G-VER's",
        len(pl) == 1 and ra.calls[0] == ("forward", [3, 4, 5], (), list(pl)) and list(lg_r) == [0.0, 1.0, 2.0, 3.0]
        and ra.calls[1] == ("forward", [3, 4], (site,), []) and set(acts_r) == {site}
        and ra.calls[2] == ("decode", [5, 6], {"skip_special_tokens": False, "clean_up_tokenization_spaces": False})
        and txt_r == "x y", ra.calls)
    from valence_core.n import hftiny
    if hftiny.available():
        a_t = hftiny.tiny_adapter()
        a_t._tok = types.SimpleNamespace(decode=lambda ii, **kw: " ".join(f"t{int(i)}" for i in ii))   # stand-in
        w_t = int(a_t._model.config.hidden_size)
        v_t = gvec.unit32(np.random.default_rng(23).normal(size=w_t))
        inj_t = gcal.injection_for(1.0, v_t, 1, 3.0, gvec.injection_sha16(v_t))
        gate_tn = gcal.gate_injection({"unit": v_t, "sha16": gvec.injection_sha16(v_t), "R_ell": 3.0}, 1)
        st_t, ids_h = _hf_step_logits(a_t), [3, 4, 5, 6, 7, 8]
        lu_t = np.asarray(st_t(ids_h, ()), dtype=np.float64)
        ls_t = np.asarray(st_t(ids_h, gcal.placed(inj_t, gcal.STEER_FROM)), dtype=np.float64)
        ls1_t = np.asarray(st_t(ids_h, gcal.placed(inj_t, 1)), dtype=np.float64)
        ref_t = np.asarray(a_t.forward(ids_h, capture_layers=()).logits, dtype=np.float64)
        turn_t = gcal.generate(st_t, ids_h, 3, inj_t, 5, eos_id=127, cap=4)
        cap_t = _hf_forward(a_t)(turn_t["ids"] or [3], (1,))
        chk("driver: on the HF path (hftiny, a tiny OLMo-2 config): G-CAL-n's step is the adapter's own last-position "
            "logits; an injection placed from STEER_FROM (the whole turn) moves them, differs from one placed from "
            "position 1 (position 0 is steered), and passes the steering check, and so does the gate's injection "
            "(f0.20 of R_ell; the review's B2); a turn generates ids-in under it; its capture is one row per id; the "
            "decode runs through a stand-in tokenizer",
            lu_t.shape == (128,) and float(np.max(np.abs(lu_t - ref_t))) <= 1e-5
            and float(np.max(np.abs(ls_t - lu_t))) > 1e-6 and float(np.max(np.abs(ls_t - ls1_t))) > 1e-6
            and gcal.steering_check(st_t, {"ids": ids_h, "gen_start": 3}, inj_t) > 0.0
            and gcal.steering_check(st_t, {"ids": ids_h, "gen_start": 3}, gate_tn) > 0.0
            and 0 <= turn_t["n_tok"] <= 4 and all(0 <= i < 128 for i in turn_t["ids"])
            and np.asarray(cap_t[1]).shape == (max(1, turn_t["n_tok"]), w_t)
            and isinstance(_hf_decoder(a_t)(turn_t["ids"]), str),
            (lu_t.shape, float(np.max(np.abs(ls_t - lu_t)))))
    else:
        chk("driver: G-CAL-n's HF path: skipped (no torch/transformers here; runs on the box through hftiny)", True, "")


# --- G-TIME-n (n v0.2 §8 step 11; Code's readings GT1-GT17, routed as PINs: the PI's "Build on the PINs") --------

GTIME_STAGE = "time"
GTIME_ROOT = REPO / "data" / "n" / "ckpt" / GTIME_STAGE
GTIME_REPORT = REPO / "data" / "n" / "reports" / f"{GTIME_STAGE}.json"
GTIME_OUT = REPO / "data" / "n" / "gtime"
GTIME_ARTIFACT = "gtime.json"
GTIME_SCHEMA = "n-gtime-v1"
GTIME_RUNS = (0, 32, 64, 95, 127, 159)          # GT1: round(k * 159 / 5) for k = 0..5, in the session set's order
GTIME_STEERED = (("+1", "dose-rule"), ("+1/2", None))   # GT1: N1-V valence at +1 re-computed, at +1/2 cached alone
GTIME_N = (1 + len(GTIME_STEERED)) * len(GTIME_RUNS)    # GT1: 18 reads, the shadow and the two steered on each run
GTIME_BENCH_RECORDS = 160                       # GT9 (i): the append benchmark's records, one N1-V cell's capacity
GTIME_BENCH_SEED = 20261121                     # the benchmark's capture rows: noise from this stream (Code's)
GTIME_EXT_MS = {"cached": 309.0, "fresh_pair": 357.1}    # A-n2:40, "used by nothing": printed beside (GT8)
GTIME_NOT_MEASURED = (                          # GT9 (c)
    "the captures' copy-back (about 4.9-5.0 GB at the campaign's 7,680 rows: the schema's CAPTURES)",
    "G-VER of record (n v0.2 §8 step 12)", "the campaign's resumes")
GTIME_FORMULA = ("T = N x median(c) + K x median(f): c = duration_ms - duration_ms_fresh (duration_ms where a read has "
                 "no re-computation) over the stage's reads, f = duration_ms_fresh over its re-computed reads; N the "
                 "campaign's reads, K its re-computations (GT8)")
GREAD_BENCH_CALLS = 10                          # GT10: the grouped 10-fold calls timed at each of the two shapes
GREAD_BENCH_SEED = 20261122                     # GT10: the synthetic arrays' stream (Code's; the arrays are noise)

#: LOCK-n v0.1's pins (LOCK-n.md, committed at deabf3f; GT4). A run checks each against the committed file that
#: carries it before the load: LOCK-n.md and G-CAL-n's two files by sha256 (``gtime_lock_inputs``), the rest against
#: what the stage measures (the weights, n's backend identifier, the package and its closure, the campaign's plan).
LOCK_PATH = REPO / "LOCK-n.md"
LOCK_SHA256 = "88d9fe7b21e72db3a9ebd3a65339cc69a2528f892b50053bdf663b9c99f8e9d5"
LOCK_SITE = 32                                  # L §3: the site, index 32
LOCK_VALENCE_SHA16 = "ba4da67fb717b5bb"         # L §3 (hole 2): the valence direction of record
LOCK_GCAL_SHA256 = "4c92f228684d51afe16d0d3dd47e115fe002c9a600271678449fbb2926fdbb8f"      # L §4: gcal.json
LOCK_DOSE_MAP_SHA256 = "d4a73b54f65b664694ae328d980ca57074d34ce09249ab7a53c7d8ac5158efb3"  # L §4: dose_map.json
LOCK_LABEL_CONVENTION = "space"                 # L §1
LOCK_BACKEND_IDENTIFIER = "8264f719efd347a9"    # L §17: n's identifier under its 4,096 window
LOCK_WEIGHTS_SHA256 = "36f05404dc39ec1759e711f560dc41dcb155f10c0230b671ded9b597fc830fdb"   # L §17
LOCK_PACKAGE_SHA256 = "06b55761052508f93fb67993b4b4c7574483aa38d2168b8254b3c0b7417a1d39"   # L §18 (hole 14)
LOCK_CLOSURE = {                                # L §18: the closure at the lock, twelve files
    "valence_core/__init__.py": "620ad380f023dc8c173ee4e164a160c0b1da2a0c0b99fb6c9717be0b8c78b604",
    "valence_core/adapters/__init__.py": "96d6b48dd41710de8c70ce7d5b28854db4810af6693ff8a96f320f773cafed6a",
    "valence_core/adapters/base.py": "626fbddd8dd970717e929b5bcd87be4e0c83ca8cb889b8451fcb49e2cb091cbf",
    "valence_core/adapters/olmo_hf.py": "df80b79b205c64121187ab0b307e5f35db5bd6632d45940a980c0175b8a092dc",
    "valence_core/discrim.py": "7d171ae7b416b33a9f881a277606ace4a6891ce30c96943c3b0a41bd75d2de89",
    "valence_core/echo/__init__.py": "71a6ec160a1d7beefc7f8c37c106f2fca742adc862fd9b737b7750218bf00e43",
    "valence_core/echo/probe.py": "d90f9281dff612977da5a3c3ce1a07155159a48103b35dfe521e0fac30152b81",
    "valence_core/extract.py": "2405b1a687f9f882472b06fa3f9b8d47b20206414ada1b854b3c93a02d7a07fe",
    "valence_core/m/__init__.py": "b5175bcb6a521ef277de105315dd8d2f637a7b03e5d7baf30406dd83d0db35c4",
    "valence_core/m/keys.py": "a7d5ee3a9cde0deed785df204ae840cb56ee0e1eeefa9192fe1c1b0abb6b3beb",
    "valence_core/m/resume.py": "78f2fc8eb8b3b16ffa39c6dac7022b37dc98d8d002f50390d5c4540f22bf8fb7",
    "valence_core/session_e2a.py": "f1e53db2e9089ed3869e75693474fa6f36eccf667d1f2a4fbe52b4ba1fe73c71",
}
LOCK_READ_PLAN_SHA256 = "7f7d7301607e0fa6f66df930ce6a502086fe13cd84d19fe2d3f8b0c9105b88a6"  # L §6
LOCK_CAMPAIGN_READS = 7680                      # L §6: the read plan after the merge, nothing merged
LOCK_P0 = (1, 26)                               # L §7: p0 = 1/26
LOCK_CADENCE = 160                              # L §13: the tile
LOCK_ALPHA = 0.01                               # L §13
LOCK_C = 0.25                                   # L §8: C, the ceiling and the identity bound
LOCK_MEDIAN_REL = 0.0013026706058596332         # L §7: the extension's median rel
#: L §5: the identity's ``sample_rule``, "the lock's words for the 10% sample" -- keys.py's PIN, verbatim, its lines
#: joined by single spaces (the self-test holds it to keys.py's docstring).
LOCK_SAMPLE_RULE = ('session s is in the sample iff ``stream(f"n-fid|{s}").random() < 0.10``; every read of a sampled '
                    'session at a point the dose rule does not cover is re-computed (§2.1: "a 10% keyed sample of the '
                    'other points, `n-fid|{s}`"; the key is per session, so the sample is a sample of sessions)')


def lock_fidelity_rule() -> dict:
    """The identity's fidelity rule at LOCK-n v0.1 (GT4): TAU, p0 1 of 26, the tile of 160, alpha 0.01, C 0.25, the
    extension's median rel, the key and the lock's words for the sample."""
    from valence_core.n import schema
    return {"tau": schema.TAU, "p0_count": LOCK_P0[0], "p0_n": LOCK_P0[1], "cadence": LOCK_CADENCE,
            "sample_key": "n-fid|{s}", "sample_rule": LOCK_SAMPLE_RULE, "alpha": LOCK_ALPHA, "ceiling": LOCK_C,
            "median_rel": LOCK_MEDIAN_REL}


def gtime_sessions(ss) -> list:
    """GT1: the six sessions, at their places in the session set's order, which is BK's run order."""
    from valence_core.n import schema
    if [round(k * 159 / 5) for k in range(6)] != list(GTIME_RUNS):
        raise AssertionError("GTIME_RUNS is not round(k * 159 / 5) for k = 0..5")
    if len(ss) != schema.N_SESSIONS:
        raise SystemExit(f"{len(ss)} sessions, not the session set's {schema.N_SESSIONS}")
    six = [ss[r] for r in GTIME_RUNS]
    if [s.bk_run for s in six] != list(GTIME_RUNS):
        raise SystemExit("the session set's order is not BK's run order at G-TIME-n's six places")
    return six


def gtime_plan(ss, identity) -> list:
    """GT1 and GT2: the six shadows (N1-V ``none`` at d = 0, re-computed: ``dose-rule``), then N1-V ``valence`` at +1
    on the six (``dose-rule``), then at +1/2 on the six (no re-computation: the cached path alone); launch indices
    0..17. The shadows come first, as the runner's ORDER has them: a steered read needs its shadow on disk."""
    from valence_core.n import runner, schema
    six = gtime_sessions(ss)
    kept = schema.dose_point_values(identity)
    plan = [runner.PlannedRead(i, s, schema.SHADOW_ARM, schema.SHADOW_DIRECTION, schema.SHADOW_DOSE, 0.0,
                               "dose-rule", None) for i, s in enumerate(six)]
    for dl, reason in GTIME_STEERED:
        for s in six:
            plan.append(runner.PlannedRead(len(plan), s, "N1-V", "valence", dl, kept[dl], reason, None))
    return plan


def gtime_lock_inputs(committed=None, *, lock_path=LOCK_PATH, gvec_dir=None, gcal_dir=None) -> dict:
    """GT4: LOCK-n v0.1's inputs, before the load, each the committed file's and the lock's:
      * LOCK-n.md, HEAD's committed bytes at LOCK_SHA256;
      * G-VEC's outputs of record (``gcal_gvec_inputs``: gvec.json a PASS, the site's directions file at the record's
        sha256, the valence row at of_record's sha16), the site LOCK_SITE and the valence row's sha16
        LOCK_VALENCE_SHA16;
      * G-CAL-n's gcal.json and dose_map.json, HEAD's committed bytes at LOCK_GCAL_SHA256 and LOCK_DOSE_MAP_SHA256,
        gcal.json a pinnable PASS (O8: the lock takes the dose map only from a PASS);
      * the dose map rebuilt from G-VEC's R and R_ell by ``gcal.dose_map`` equal to gcal.json's, its five figures to
        dose_map.json's.
    Returns the dose map, the valence row and its sha16, the site, and the files' sha256s."""
    import hashlib

    from valence_core.n import gcal, gvec
    committed = committed or committed_bytes
    gvec_dir = Path(gvec_dir) if gvec_dir is not None else GVEC_OUT
    gcal_dir = Path(gcal_dir) if gcal_dir is not None else GCAL_OUT
    lp = Path(lock_path)
    lb = lp.read_bytes() if lp.is_file() else None
    if lb is None or committed(lp) != lb or hashlib.sha256(lb).hexdigest() != LOCK_SHA256:
        raise SystemExit("LOCK-n.md is absent, not HEAD's committed bytes, or not LOCK-n v0.1's (GT4)")
    gv = gcal_gvec_inputs(gvec_dir, committed, gvec.CANDIDATE_INDICES)
    if gv["site"] != LOCK_SITE or gv["v_sha16"] != LOCK_VALENCE_SHA16:
        raise SystemExit("G-VEC's site or valence row is not the lock's (L §3: index 32, ba4da67fb717b5bb)")
    files = {}
    for name, pin in ((gcal.OUT_RECORD, LOCK_GCAL_SHA256), (gcal.OUT_DOSE_MAP, LOCK_DOSE_MAP_SHA256)):
        p = gcal_dir / name
        b = p.read_bytes() if p.is_file() else None
        if b is None or committed(p) != b or hashlib.sha256(b).hexdigest() != pin:
            raise SystemExit(f"data/n/gcal/{name} is absent, not HEAD's committed bytes, or not the lock's (L §4)")
        files[name] = b
    try:
        rec = json.loads(files[gcal.OUT_RECORD].decode("utf-8"))
        five = json.loads(files[gcal.OUT_DOSE_MAP].decode("utf-8"))
        head = (rec.get("schema"), rec.get("stage"), rec.get("status"), rec.get("pinnable"))
        rmap = rec["dose_map"]
    except (ValueError, KeyError, TypeError, AttributeError) as e:
        raise SystemExit(f"data/n/gcal/gcal.json is not a G-CAL-n record ({type(e).__name__})")
    if head != (gcal.RECORD_SCHEMA, gcal.STAGE, "PASS", True):
        raise SystemExit("data/n/gcal/gcal.json is not a pinnable G-CAL-n PASS (O8)")
    dmap = gcal.dose_map(gv["R"], gv["R_ell"])
    if rmap != dmap or five != {k: dmap[k] for k in gcal.DOSE_MAP_KEYS}:
        raise SystemExit("the dose map rebuilt from G-VEC's R and R_ell is not G-CAL-n's record's or dose_map.json's")
    return {"lock_sha256": LOCK_SHA256, "site": gv["site"], "R": gv["R"], "R_ell": gv["R_ell"],
            "v_unit": gv["v_unit"], "v_sha16": gv["v_sha16"], "dose_map": dmap, "gvec_sha256": gv["gvec_sha256"],
            "directions_sha256": gv["directions_sha256"],
            "gcal_sha256": hashlib.sha256(files[gcal.OUT_RECORD]).hexdigest(),
            "dose_map_sha256": hashlib.sha256(files[gcal.OUT_DOSE_MAP]).hexdigest()}


def gtime_identity(*, package_sha256: str, imported_sha256: dict, weights: str, backend_identifier: str, pod_id: str,
                   rendering_id: str, dose_map: dict, v_sha16: str, n_layers: int = N_LAYERS, d_model: int = D_MODEL,
                   layer: int = LOCK_SITE) -> dict:
    """The stage identity at "time" (GT4): LOCK-n v0.1's sha256, its dose map, its fidelity rule with C and the
    identity bound C, the one direction G-TIME-n injects (valence), the lock's label convention and window, and the
    package, weights, backend and pod the caller measured. No cap: the runner gets ``hour_cap_ms`` None. Checked
    before return."""
    from valence_core.n import schema
    ident = {
        "unit": schema.UNIT, "stage": GTIME_STAGE, "record_schema": schema.RECORD_SCHEMA,
        "proposal_sha256": schema.PROPOSAL_SHA256, "lock_sha256": LOCK_SHA256, "package_sha256": package_sha256,
        "imported_sha256": dict(imported_sha256), "weights_sha256": weights, "backend_identifier": backend_identifier,
        "pod_id": pod_id, "session_set_sha256": schema.SESSION_SET_SHA256, "rendering_id": rendering_id,
        "label_convention": LOCK_LABEL_CONVENTION, "layer_bk": 32, "layer": int(layer),
        "capture_layers": list(range(int(layer) + 1, int(n_layers))), "n_layers": int(n_layers),
        "d_model": int(d_model), "read_window": schema.MAX_WINDOW, "dose_map": dict(dose_map),
        "directions": {"valence": str(v_sha16)}, "fidelity_rule": lock_fidelity_rule(), "identity_bound": LOCK_C,
    }
    schema.check_stage_identity(ident)
    return ident


def campaign_counts(identity, ss) -> dict:
    """GT8's N and K and GT9's cells, by the package's own functions: the campaign's launch order
    (``runner.campaign_order``) over the campaign's view of the stage identity -- the same dose map, so the same read
    plan, whose ``read_plan_sha256`` the caller holds to the lock's -- each read's re-computation by its rule
    (runner:147: ``dose-rule`` at d in {0, +1, -1}, the keyed sample elsewhere), and every cell's read count."""
    from valence_core.n import keys, runner, schema
    view = dict(identity, stage="campaign")
    schema.check_stage_identity(view)
    plan = runner.campaign_order(view, ss, keys.n4_schedule([s.present_first_is_S for s in ss]))
    by_cell: dict = {}
    for p in plan:
        k = schema.cell_filename(p.arm, p.direction_id, p.dose_label)
        by_cell[k] = by_cell.get(k, 0) + 1
    return {"reads": len(plan), "dose_rule": sum(1 for p in plan if p.fidelity_reason == "dose-rule"),
            "sample": sum(1 for p in plan if p.fidelity_reason == "sample"),
            "recomputations": sum(1 for p in plan if p.fidelity_reason is not None),
            "cells": dict(sorted(by_cell.items())), "read_plan_sha256": schema.read_plan_sha256(view)}


def fit_line(ys) -> tuple:
    """Least squares y = a + b * k over k = 0..n-1 (GT9 (i)), n >= 2: (a, b), by the closed form."""
    n = len(ys)
    if n < 2:
        raise ValueError("a line needs two points")
    km = (n - 1) / 2.0
    ym = math.fsum(ys) / n
    sxx = math.fsum((k - km) ** 2 for k in range(n))
    sxy = math.fsum((k - km) * (float(y) - ym) for k, y in enumerate(ys))
    b = sxy / sxx
    return ym - b * km, b


def rekeyed(rec, run: int, launch: int) -> dict:
    """A copy of a read record re-keyed to BK's run ``run`` at launch index ``launch``: its session's id, cell and run,
    its read id, its shadow's read id where it names one, and the launch index; every other field as read. The
    benchmark's record (GT9 (i)); never a record of a stage."""
    import copy

    from valence_core.n import schema
    cell = schema.bk_cell_of(run)
    sid = schema.session_id(cell, run)
    out = copy.deepcopy(dict(rec))
    out.update(session_id=sid, bk_cell=cell, bk_run=int(run), launch_index=int(launch),
               read_id=schema.read_id(out["arm"], out["direction_id"], out["dose_label"], sid),
               shadow_read_id=None if out["shadow_read_id"] is None else schema.shadow_read_id(sid))
    return out


def same_filesystem(a, b, stat=os.stat) -> bool:
    """GT9 (i): the benchmark's folder ``a`` and the nearest existing folder on the stage root's path ``b`` are on one
    filesystem, by ``stat``'s device (the self-test passes another stat)."""
    b = Path(b)
    anchor = next(p for p in (b, *b.parents) if p.exists())
    return stat(Path(a)).st_dev == stat(anchor).st_dev


def io_bench(identity, bench_dir, template, *, n_records: int = GTIME_BENCH_RECORDS,
             clock=time.perf_counter, say=None) -> dict:
    """GT9 (i), Code's PIN: the model-free append benchmark, after the reads. ``n_records`` records -- ``template``, a
    record of the stage (at the run of record its first N1-V ``valence`` +1 read, with its re-computation: the
    campaign's record form, the larger one), re-keyed to BK's runs 0, 1, ... in turn (``rekeyed``) -- appended one by
    one to the template's cell under the stage's identity (its band and width), through the runner's own writer
    (``cells.append_record``: the rows written in place and fsynced, the whole cell re-checked and its JSON rewritten),
    in a temporary folder under ``bench_dir`` that is removed at the end; each append timed, capture rows of noise.
    A failed removal is no failure of the stage: it is said, with the folder left behind (``say``). No example builder
    of the schema runs here (schema's EXAMPLES: "no production path calls them"). Returns the cell, the count, each
    append's ms and the line a + b * k fitted to them (k the records already in the cell)."""
    import numpy as np

    from valence_core.adapters.base import sha16_arr
    from valence_core.n import cells, guard, schema
    bd = guard.refuse_test_out(Path(bench_dir))
    if not bd.is_dir():
        raise SystemExit(f"the benchmark's folder {bd} is not an existing folder")
    key = (template["arm"], template["direction_id"], template["dose_label"])
    if not 2 <= int(n_records) <= schema.capture_capacity(key[0]):
        raise ValueError("the benchmark appends 2 records or more, up to the cell's capacity")
    layers = [int(x) for x in identity["capture_layers"]]
    rng = np.random.default_rng(GTIME_BENCH_SEED)
    times: list = []
    with tempfile.TemporaryDirectory(dir=bd, prefix="n-gtime-bench-", ignore_cleanup_errors=True) as t:
        root = Path(t)
        cell, caps = cells.load_cell(root, *key, identity=identity)
        for k in range(int(n_records)):
            rec = rekeyed(template, k, k)
            rows = {l: rng.standard_normal(int(identity["d_model"])).astype(np.float32) for l in layers}
            rec["capture"] = {"row": k, "sha16": {str(l): sha16_arr(rows[l]) for l in layers}}
            t0 = clock()
            cell, caps = cells.append_record(root, cell, caps, rec, rows)
            times.append(round((clock() - t0) * 1000.0, 3))
    if Path(t).exists() and say is not None:
        say(f"the benchmark's folder {t} was not removed: remove it by hand (no record of the stage is in it)")
    a, b = fit_line(times)
    return {"cell": schema.cell_filename(*key), "records": int(n_records), "append_ms": times, "a_ms": a, "b_ms": b}


def gtime_reads(records, io_ms: dict) -> list:
    """The artifact's per-read rows (GT11): launch index, read id, cell, BK's run, seq_len, the read's ms and its fresh
    share, c (the cached share), and its I/O (GT9 (b): the time from the previous read's line to its own, less its
    duration_ms; None where that line is not in this invocation); no margin and no log-probability."""
    from valence_core.n import schema
    out = []
    for r in sorted(records, key=lambda x: x["launch_index"]):
        f = r["duration_ms_fresh"]
        out.append({"launch_index": int(r["launch_index"]), "read_id": str(r["read_id"]),
                    "cell": schema.cell_filename(r["arm"], r["direction_id"], r["dose_label"]),
                    "bk_run": int(r["bk_run"]), "seq_len": int(r["seq_len"]), "duration_ms": int(r["duration_ms"]),
                    "duration_ms_fresh": None if f is None else int(f),
                    "cached_ms": int(r["duration_ms"]) - (0 if f is None else int(f)),
                    "io_ms": io_ms.get(int(r["launch_index"]))})
    return out


def _median(xs):
    import numpy as np
    return float(np.median(xs)) if xs else None


def gtime_figures(reads, counts, loads_ms, bench) -> dict:
    """GT8's model time and GT9's pod hours from the per-read rows, the campaign's counts, the loads and the
    benchmark. Every figure is a function of the artifact's own fields, so ``check_gtime`` recomputes it."""
    c = [x["cached_ms"] for x in reads]
    f = [x["duration_ms_fresh"] for x in reads if x["duration_ms_fresh"] is not None]
    N, K = int(counts["reads"]), int(counts["recomputations"])
    mc, mf = _median(c), _median(f)
    xc, xf = (float(max(c)) if c else None), (float(max(f)) if f else None)
    t_med = None if mc is None or mf is None else N * mc + K * mf
    t_max = None if xc is None or xf is None else N * xc + K * xf
    t_ext = N * GTIME_EXT_MS["cached"] + K * GTIME_EXT_MS["fresh_pair"]
    sizes = list(counts["cells"].values())
    pairs = sum(n * (n - 1) // 2 for n in sizes)
    io_proj = bench["a_ms"] * sum(sizes) + bench["b_ms"] * pairs
    per = [x["io_ms"] for x in reads if x["io_ms"] is not None]
    mio = _median(per)
    hours = (lambda ms: None if ms is None else ms / 3.6e6)
    return {
        "model_time": {"formula": GTIME_FORMULA, "N": N, "K": K, "median_cached_ms": mc, "median_fresh_ms": mf,
                       "max_cached_ms": xc, "max_fresh_ms": xf, "reads": len(c), "recomputed_reads": len(f),
                       "T_median_ms": t_med, "T_median_h": hours(t_med), "T_max_ms": t_max, "T_max_h": hours(t_max)},
        "beside": {"extension_ms": dict(GTIME_EXT_MS), "T_extension_ms": t_ext, "T_extension_h": hours(t_ext),
                   "note": "A-n2:40: recorded for G-TIME-n and used by nothing; printed beside, not used"},
        "pod_hours": {"loads_ms": [int(x) for x in loads_ms],
                      "io": {"bench": dict(bench), "campaign_cells": len(sizes), "campaign_appends": sum(sizes),
                             "campaign_pairs": pairs, "projected_ms": io_proj, "projected_h": hours(io_proj),
                             "per_read_reads": len(per), "per_read_median_ms": mio,
                             "lower_bound_ms": None if mio is None else mio * sum(sizes),
                             "lower_bound_h": None if mio is None else hours(mio * sum(sizes))},
                      "not_measured": list(GTIME_NOT_MEASURED)},
    }


GTIME_KEYS = ("schema", "smoke", "lock_sha256", "stage_identity_sha256", "report_sha256", "driver_sha256", "reads",
              "campaign", "model_time", "beside", "pod_hours")
GTIME_READ_KEYS = ("launch_index", "read_id", "cell", "bk_run", "seq_len", "duration_ms", "duration_ms_fresh",
                   "cached_ms", "io_ms")


def gtime_artifact(*, smoke, stage_identity_sha256: str, report_sha256: str, driver_sha256: str, records, io_ms,
                   counts, loads_ms, bench) -> dict:
    """G-TIME-n's projection artifact (``n-gtime-v1``; GT11), checked before return."""
    reads = gtime_reads(records, io_ms)
    art = {"schema": GTIME_SCHEMA, "smoke": None if smoke is None else int(smoke), "lock_sha256": LOCK_SHA256,
           "stage_identity_sha256": stage_identity_sha256, "report_sha256": report_sha256,
           "driver_sha256": driver_sha256, "reads": reads,
           "campaign": {"reads": int(counts["reads"]), "dose_rule": int(counts["dose_rule"]),
                        "sample": int(counts["sample"]), "recomputations": int(counts["recomputations"]),
                        "cells": {str(k): int(v) for k, v in counts["cells"].items()},
                        "read_plan_sha256": str(counts["read_plan_sha256"])}}
    art.update(gtime_figures(reads, art["campaign"], loads_ms, bench))
    check_gtime(art)
    return art


def check_gtime(art) -> None:
    """The artifact's form (Code's, ``n-gtime-v1``): its keys; its reads, all 18 at a run of record and the smoke's
    count at a smoke, each row's keys and c = duration_ms minus the fresh share, the fresh share within the read's; the
    campaign's plan and its read count the lock's (read_plan_sha256, 7,680 reads), its other counts summing as they
    must; and every figure recomputed from the artifact's own fields, exactly (a check of consistency: the figures'
    arithmetic is the self-test's, by literals). SystemExit naming the field, never a value; a field of the wrong shape
    where a check reaches into it is "its form"."""
    try:
        _check_gtime(art)
    except (KeyError, TypeError, AttributeError, ValueError, IndexError):
        raise SystemExit("the G-TIME-n artifact is malformed at its form")


def _check_gtime(art) -> None:
    def bad(where: str):
        raise SystemExit(f"the G-TIME-n artifact is malformed at {where}")
    if not isinstance(art, dict) or tuple(sorted(art)) != tuple(sorted(GTIME_KEYS)):
        bad("its keys")
    if art["schema"] != GTIME_SCHEMA or art["lock_sha256"] != LOCK_SHA256:
        bad("schema or lock_sha256")
    if art["smoke"] is not None and not (isinstance(art["smoke"], int) and 1 <= art["smoke"] <= GTIME_N):
        bad("smoke")
    for k in ("stage_identity_sha256", "report_sha256", "driver_sha256"):
        v = art[k]
        if not (isinstance(v, str) and len(v) == 64 and all(ch in "0123456789abcdef" for ch in v)):
            bad(k)
    reads = art["reads"]
    if not isinstance(reads, list) or len(reads) != (GTIME_N if art["smoke"] is None else art["smoke"]):
        bad("reads")
    for i, x in enumerate(reads):
        if not isinstance(x, dict) or tuple(sorted(x)) != tuple(sorted(GTIME_READ_KEYS)) or x["launch_index"] != i:
            bad(f"reads[{i}]")
        f = x["duration_ms_fresh"]
        if not (isinstance(x["duration_ms"], int) and x["duration_ms"] >= 0 and (f is None or (
                isinstance(f, int) and 0 <= f <= x["duration_ms"]))
                and x["cached_ms"] == x["duration_ms"] - (0 if f is None else f)):
            bad(f"reads[{i}].cached_ms")
        if x["io_ms"] is not None and not isinstance(x["io_ms"], float):
            bad(f"reads[{i}].io_ms")
    camp = art["campaign"]
    if (not isinstance(camp, dict) or sorted(camp) != sorted(("reads", "dose_rule", "sample", "recomputations", "cells",
                                                               "read_plan_sha256"))
            or camp["read_plan_sha256"] != LOCK_READ_PLAN_SHA256 or camp["reads"] != LOCK_CAMPAIGN_READS
            or camp["recomputations"] != camp["dose_rule"] + camp["sample"]
            or camp["reads"] != sum(camp["cells"].values())):
        bad("campaign")
    bench = art["pod_hours"]["io"]["bench"]
    if (not isinstance(bench, dict) or sorted(bench) != sorted(("cell", "records", "append_ms", "a_ms", "b_ms"))
            or len(bench["append_ms"]) != bench["records"]
            or (bench["a_ms"], bench["b_ms"]) != fit_line(bench["append_ms"])):
        bad("pod_hours.io.bench")
    want = gtime_figures(reads, camp, art["pod_hours"]["loads_ms"], bench)
    for k in ("model_time", "beside", "pod_hours"):
        if art[k] != want[k]:
            bad(k)


@dataclass
class GtimeEnv:
    """G-TIME-n's seams: ``production_gtime_env`` is the box's; the self-test puts the numpy double behind them."""
    weights: Callable                   # () -> the weights of record (``weights_of_record``)
    load_sessions: Callable             # () -> the session set
    load_ids: Callable                  # () -> ``ids.load()``
    lock_inputs: Callable               # () -> ``gtime_lock_inputs()``: LOCK-n v0.1's inputs, checked (GT4)
    gver: Callable                      # (sessions, loaded, path) -> G-VER's report, the tokenizer alone loaded (GT7)
    env_provenance: Callable            # (path) -> the provenance the adapter will report (before the load)
    make_adapter: Callable              # (path) -> the adapter (the weights load)
    adapter_shape: Callable             # (adapter) -> (n_layers, d_model)
    make_backend: Callable              # (adapter) -> the 5(f) backend
    package: Callable                   # () -> (package_sha256, closure), measured in this process
    counts: Callable                    # (identity, sessions) -> ``campaign_counts``
    pod: Callable                       # () -> the pod id or None
    driver: Callable                    # () -> (this driver's bytes as run, HEAD's committed bytes of its path | None)
    shape: tuple = (N_LAYERS, D_MODEL)
    root: Path = GTIME_ROOT
    report: Path = GTIME_REPORT
    out: Path = GTIME_OUT
    bench_records: int = GTIME_BENCH_RECORDS
    printer: Callable = print
    clock: Callable = time.perf_counter


def _package_closure() -> tuple:
    mods = _import_production()
    return mods["guard"].package_sha256(), mods["guard"].closure_from_modules(dict(sys.modules))


def production_gtime_env() -> GtimeEnv:
    from valence_core.m import resume as m_resume
    from valence_core.n import ids, sessions
    return GtimeEnv(weights=weights_of_record, load_sessions=sessions.load_sessions, load_ids=ids.load,
                    lock_inputs=gtime_lock_inputs, gver=_gver_tokenizer, env_provenance=environment_provenance,
                    make_adapter=_load_adapter,
                    adapter_shape=lambda a: (int(a.n_layers), int(a._model.config.hidden_size)),
                    make_backend=_hf_backend, package=_package_closure, counts=campaign_counts, pod=m_resume.pod_id,
                    driver=driver_bytes)


def _gtime_prepare(env: GtimeEnv, *, bench_dir, smoke, out, resume: bool, rulings: dict):
    """Everything before the first read (GT14's refusals, GT4's identity, GT7's G-VER, the load), in order; a refusal
    raises SystemExit, and G-VER's STOP returns None before the weights load."""
    import hashlib

    from valence_core.m import resume as m_resume
    from valence_core.m.keys import stream_known_answer
    from valence_core.n import guard, ids, runner, schema
    say = env.printer
    if smoke is not None:
        if not 1 <= int(smoke) <= GTIME_N:
            raise SystemExit(f"--smoke takes 1..{GTIME_N} reads (GT14: the smoke is the same 18 reads)")
        if out is None:
            raise SystemExit("a smoke writes only into --out, a new folder outside the repository")
        if resume or rulings:
            raise SystemExit("a smoke never resumes: its --out is a new folder")
        o = Path(out).resolve()
        if _within(o, REPO.resolve()):
            raise SystemExit(f"a smoke writes outside the repository, not {out}")
        o = guard.refuse_out(o)
        if o.exists():
            raise SystemExit(f"{o} exists: a smoke writes into a new folder")
        root_p, report_p, art_p = o / "ckpt", o / f"{GTIME_STAGE}.json", o / GTIME_ARTIFACT
    else:
        if out is not None:
            raise SystemExit("a run of record writes only to the stage's own root, report and artifact (--out is a "
                             "smoke's)")
        root_p, report_p = guard.refuse_out(Path(env.root)), guard.refuse_out(Path(env.report))
        art_p = guard.refuse_out(Path(env.out)) / GTIME_ARTIFACT
    if art_p.exists():
        raise SystemExit(f"{_shown(art_p)} exists: G-TIME-n writes its projection once")
    if bench_dir is None:
        raise SystemExit("G-TIME-n needs --bench-dir, an existing folder outside the repository on the stage root's "
                         "filesystem (GT9 (i))")
    bench = guard.refuse_test_out(Path(bench_dir))
    if not bench.is_dir():
        raise SystemExit(f"--bench-dir {bench_dir} is not an existing folder")
    if not same_filesystem(bench, root_p):
        raise SystemExit(f"--bench-dir {bench} is not on the stage root's filesystem (GT9 (i): the box's volume)")
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
    for pid, rp in rulings.items():
        if not Path(rp).is_file():
            raise SystemExit(f"the ruling for {pid} is not a file: {rp}")
    if smoke is not None:
        say(f"SMOKE: the first {smoke} of the {GTIME_N} reads, outside the repository; never of record (GT14)")
    say(f"STAGE G-TIME-n: stage {GTIME_STAGE}, under LOCK-n v0.1 {LOCK_SHA256}; root {_shown(root_p)}, report "
        f"{_shown(report_p)}, artifact {_shown(art_p)}; the benchmark under {bench}")
    w = env.weights()
    say(f"WEIGHTS: {w['repo']} revision {w['revision']}, files_aggregate_sha256 {w['sha256']}; {w['n_files']} files "
        f"at {w['path']}, each at the manifest's byte count (the full re-hash is respawn step (i))")
    if w["sha256"] != LOCK_WEIGHTS_SHA256:
        raise SystemExit("the weights of record are not the lock's (L §17)")
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
    li = env.lock_inputs()
    dm = li["dose_map"]
    say(f"LOCK-n v0.1's inputs (GT4): G-VEC's record {li['gvec_sha256']}, site {li['site']}, valence "
        f"{li['v_sha16']}; G-CAL-n's record {li['gcal_sha256']} and dose map {li['dose_map_sha256']}: d_eq "
        f"{dm['d_eq']!r}, d_20 {dm['d_20']!r}")
    n_layers, d_model = env.shape
    pre = env.env_provenance(w["path"])
    if bridge_identifier(pre) != CHARACTERIZED_IDENTIFIER:
        raise SystemExit(f"before the load: the environment's provenance under the default window hashes to "
                         f"{bridge_identifier(pre)}, not the characterization's {CHARACTERIZED_IDENTIFIER} (R6)")
    bid = m_resume.backend_identifier(pre)
    if bid != LOCK_BACKEND_IDENTIFIER:
        raise SystemExit(f"n's backend identifier {bid} is not the lock's {LOCK_BACKEND_IDENTIFIER} (L §17)")
    pkg, clo = env.package()
    if pkg != LOCK_PACKAGE_SHA256 or clo != LOCK_CLOSURE:
        diff = sorted(k for k in set(clo) | set(LOCK_CLOSURE) if clo.get(k) != LOCK_CLOSURE.get(k))
        raise SystemExit(f"the package or its closure is not the lock's (L §18; GT3): package "
                         f"{'the lock' if pkg == LOCK_PACKAGE_SHA256 else pkg}'s, closure files differing {diff}")
    ident = gtime_identity(package_sha256=pkg, imported_sha256=clo, weights=w["sha256"], backend_identifier=bid,
                           pod_id=pod, rendering_id=loaded["manifest_sha256"], dose_map=dm, v_sha16=li["v_sha16"],
                           n_layers=n_layers, d_model=d_model, layer=li["site"])
    say(f"identity: stage {ident['stage']}, sha256 {schema.identity_sha256(ident)}; C {LOCK_C}, p0 {LOCK_P0[0]} of "
        f"{LOCK_P0[1]}, alpha {LOCK_ALPHA}, the tile {LOCK_CADENCE}; directions {ident['directions']}; no cap")
    plan = gtime_plan(ss, ident)
    plan = plan[:int(smoke)] if smoke is not None else plan
    for p in plan:
        say(f"plan {p.launch_index} {p.read_id} {p.fidelity_reason or 'the cached path alone'}")
    counts = env.counts(ident, ss)
    if counts["read_plan_sha256"] != LOCK_READ_PLAN_SHA256:
        raise SystemExit("the campaign's read plan under this identity is not the lock's (L §6)")
    say(f"the campaign (GT8): N {counts['reads']} reads; K {counts['recomputations']} re-computations "
        f"({counts['dose_rule']} dose-rule, {counts['sample']} keyed sample); {len(counts['cells'])} cells; its "
        f"read_plan_sha256 the lock's")
    prior_state(root_p, report_p, ident, plan, resume, rulings)
    rep = env.gver(ss, loaded, w["path"])
    say("G-VER (G-TIME-n's start, not of record; GT7):")
    say(json.dumps(rep, sort_keys=True))
    if rep["status"] != "PASS":
        say("G-VER STOP: no weights load, nothing is read, no report (GT7; L:543): a STOP for the seat")
        return None
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
    marks: dict = {}

    def say_t(line: str) -> None:                  # GT9 (b): the time of each read's line, by its launch index
        if line.startswith("read ") and " fid=" in line:
            try:
                marks[int(line.split(" ", 2)[1])] = env.clock()
            except ValueError:
                pass
        say(line)
    inputs = runner.StageInputs(root=root_p, report_path=report_p, identity=ident, sessions=ss,
                                ids_of=ids.ids_of(loaded), label_ids=ids.label_ids(loaded, LOCK_LABEL_CONVENTION),
                                backend=backend, directions={"valence": li["v_unit"]}, alpha=LOCK_ALPHA,
                                hour_cap_ms=None, load_ms=load_ms, rulings=rulings, printer=say_t, clock=env.clock)
    return {"inputs": inputs, "plan": plan, "ident": ident, "counts": counts, "marks": marks, "root": root_p,
            "report": report_p, "artifact": art_p, "bench": bench, "driver_sha256": dsha}


def run_gtime(env: GtimeEnv, *, bench_dir, smoke: int | None = None, out=None, resume: bool = False,
              rulings=None) -> int:
    """G-TIME-n (n v0.2 §8 step 11; GT1-GT17), in order: the refusals, the weights and the driver, the ids, LOCK-n
    v0.1's inputs, the R6 bridge, the identity, the plan and the campaign's counts, what is on disk, G-VER before the
    load, the load; the 18 reads through the runner; on COMPLETE the projection: the stage's own records read back,
    GT8's model time, GT9's pod hours with the append benchmark, the artifact checked and written, its figures
    printed. Exit 0 on COMPLETE (the artifact written); 3 on a PAUSE (the report written and no projection, for the
    seat); 2 on G-VER's STOP (no weights load, no read, no report) or a refusal before any read; 1 otherwise (GT6)."""
    import hashlib

    from valence_core.m import resume as m_resume
    from valence_core.n import cells
    say = env.printer
    try:
        ctx = _gtime_prepare(env, bench_dir=bench_dir, smoke=smoke, out=out, resume=resume,
                             rulings=dict(rulings or {}))
    except SystemExit as e:
        if isinstance(e.code, str):
            say(f"REFUSED before any read: {e.code}")
            return 2
        raise
    if ctx is None:
        return 2
    from valence_core.n import runner
    rpt = runner.run(ctx["inputs"], ctx["plan"], resume=resume)
    if rpt["end_state"] != "COMPLETE":
        say(f"G-TIME-n {rpt['end_state']}: the report is written and no projection; the seat rules (GT5)")
        return 3 if rpt["end_state"] == "PAUSE" else 1
    ident, plan = ctx["ident"], ctx["plan"]
    recs: list = []
    for key in sorted({(p.arm, p.direction_id, p.dose_label) for p in plan}):
        cell, _caps = cells.load_cell(ctx["root"], *key, identity=ident)
        recs.extend(cell["records"])
    if sorted(r["launch_index"] for r in recs) != list(range(len(plan))):
        raise SystemExit("the stage's records on disk are not its plan's reads")
    by_li = {int(r["launch_index"]): r for r in recs}
    marks = ctx["marks"]
    io_ms = {i: round((marks[i] - marks[i - 1]) * 1000.0 - by_li[i]["duration_ms"], 3)
             for i in sorted(marks) if i - 1 in marks}
    ordered = sorted(recs, key=lambda x: x["launch_index"])
    template = next((r for r in ordered if r["dose_label"] == "+1"), ordered[0])
    say(f"I/O benchmark (GT9 (i)): {env.bench_records} appends of the stage's read {template['launch_index']} "
        f"({template['read_id'].rsplit('|', 1)[0]}), re-keyed to BK's runs 0.. in turn, in a temporary folder under "
        f"{ctx['bench']}, removed at its end")
    bench = io_bench(ident, ctx["bench"], template, n_records=env.bench_records, clock=env.clock, say=say)
    rep_bytes = Path(ctx["report"]).read_bytes()
    art = gtime_artifact(smoke=smoke, stage_identity_sha256=rpt["stage_identity_sha256"],
                         report_sha256=hashlib.sha256(rep_bytes).hexdigest(), driver_sha256=ctx["driver_sha256"],
                         records=recs, io_ms=io_ms, counts=ctx["counts"], loads_ms=rpt["cap"]["loads_ms"],
                         bench=bench)
    art_p = Path(ctx["artifact"])
    art_p.parent.mkdir(parents=True, exist_ok=True)
    m_resume.atomic_write_json(art_p, art)
    mt, bs, ph = art["model_time"], art["beside"], art["pod_hours"]
    io = ph["io"]
    say(f"model time (GT8; the cap's basis): N {mt['N']} x median c {mt['median_cached_ms']!r} ms + K {mt['K']} x "
        f"median f {mt['median_fresh_ms']!r} ms = {mt['T_median_ms']!r} ms = {mt['T_median_h']!r} h; at the maxima "
        f"({mt['max_cached_ms']!r}, {mt['max_fresh_ms']!r} ms) {mt['T_max_ms']!r} ms = {mt['T_max_h']!r} h; over "
        f"{mt['reads']} reads, {mt['recomputed_reads']} re-computed")
    say(f"beside, unused (A-n2:40): the extension's {bs['extension_ms']['cached']!r} and "
        f"{bs['extension_ms']['fresh_pair']!r} ms give {bs['T_extension_ms']!r} ms = {bs['T_extension_h']!r} h")
    say(f"pod hours beside the cap, outside it (GT9): loads {ph['loads_ms']} ms; the I/O by the append benchmark "
        f"(option (i)): a {io['bench']['a_ms']!r} ms + b {io['bench']['b_ms']!r} ms per record already in the cell, "
        f"over the campaign's {io['campaign_cells']} cells: {io['campaign_appends']} a + {io['campaign_pairs']} b = "
        f"{io['projected_ms']!r} ms = {io['projected_h']!r} h; the stage's own per-read I/O, median "
        f"{io['per_read_median_ms']!r} ms over {io['per_read_reads']} reads (option (ii), a lower bound: "
        f"{io['lower_bound_ms']!r} ms); not measured: {'; '.join(ph['not_measured'])}")
    say(f"artifact {_shown(art_p)} sha256 {hashlib.sha256(art_p.read_bytes()).hexdigest()}")
    say("G-TIME-n COMPLETE" + (", a smoke, never of record" if smoke is not None else
                               ": the projections are for the PI's cap at LOCK-n v1.0 (GT16)"))
    return 0


def cmd_gtime(bench_dir, smoke: int | None = None, out=None, resume: bool = False, rulings=None) -> int:
    return run_gtime(production_gtime_env(), bench_dir=bench_dir, smoke=smoke, out=out, resume=resume,
                     rulings=rulings)


def gread_counts(band: int) -> dict:
    """GT10's count of G-READ-n's grouped 10-fold calls (each ``probe.K_FOLDS`` fits): the primary results, every
    (axis, point) of ``schema.GREAD_AXES``, each over the band at 1 + ``probe.N_SHUFFLES`` calls on the 160 sessions'
    contrast (two rows a session); and the comparator, the ``schema.N_RANDOM`` random directions at the random points
    the results are matched to -- the valence axis's four, span_reward's f0.10 and f0.20 matched to +d_eq and +d_20
    -- each over the band at one call on the 40 floor sessions' contrast. The seat's figure: "About 404,000 fits in
    all" (the answers of 2026-11-16, :42)."""
    from valence_core.n import probe, schema
    results = sum(len(v) for v in schema.GREAD_AXES.values())
    points = len(set(schema.GREAD_AXES["valence"]))
    primary = results * int(band) * (1 + probe.N_SHUFFLES)
    comparator = points * schema.N_RANDOM * int(band)
    return {"results": results, "band": int(band), "primary_calls": primary, "primary_rows": 2 * schema.N_SESSIONS,
            "comparator_points": points, "comparator_calls": comparator, "comparator_rows": 2 * schema.N_FLOOR,
            "folds": probe.K_FOLDS, "fits": (primary + comparator) * probe.K_FOLDS}


def gread_bench(*, calls: int = GREAD_BENCH_CALLS, d_model: int = D_MODEL, band: int = N_LAYERS - LOCK_SITE - 1,
                clock=time.perf_counter) -> dict:
    """GT10: probe.py's statistic at its pinned settings (``probe.layer_auc``: k's ``fit_lr`` at seed 7, 300
    iterations, rate 0.1, l2 0.01, on the grouped 10-fold folds of ``probe.CV_SEED``), ``calls`` times at each of the
    two contrasts' shapes, on synthetic float32 rows (noise from ``GREAD_BENCH_SEED``) grouped as
    ``probe.contrast_rows`` groups them; the projection to the count. Model-free; writes nothing."""
    import numpy as np

    from valence_core.n import probe
    cnt = gread_counts(band)
    rng = np.random.default_rng(GREAD_BENCH_SEED)
    ms: dict = {}
    for kind, rows in (("primary", cnt["primary_rows"]), ("comparator", cnt["comparator_rows"])):
        sids = [f"s{i:03d}" for i in range(rows // 2)]
        pos = {s: rng.standard_normal(int(d_model)).astype(np.float32) for s in sids}
        neg = {s: rng.standard_normal(int(d_model)).astype(np.float32) for s in sids}
        X, y, g = probe.contrast_rows(pos, neg)
        ts = []
        for _ in range(int(calls)):
            t0 = clock()
            probe.layer_auc(X, y, g, shuffles=0, cv_seed=probe.CV_SEED)
            ts.append(round((clock() - t0) * 1000.0, 3))
        ms[kind] = ts
    t_med = cnt["primary_calls"] * _median(ms["primary"]) + cnt["comparator_calls"] * _median(ms["comparator"])
    t_max = cnt["primary_calls"] * max(ms["primary"]) + cnt["comparator_calls"] * max(ms["comparator"])
    return {"counts": cnt, "calls": int(calls), "d_model": int(d_model), "ms": ms, "T_median_ms": t_med,
            "T_median_h": t_med / 3.6e6, "T_max_ms": t_max, "T_max_h": t_max / 3.6e6}


def cmd_gread_bench() -> int:
    """GT10's benchmark on the laptop (refused on a pod): its every call's ms, the counts and the projection, printed;
    nothing written."""
    import platform

    import numpy as np

    from valence_core.m import resume as m_resume
    from valence_core.n import probe, schema
    if m_resume.pod_id() is not None:
        raise SystemExit("gread-bench times the laptop's CPU (GT10): refused on a pod")
    r = gread_bench()
    c = r["counts"]
    print(f"gread-bench (GT10; G-READ-n's fits on the laptop's CPU, outside the box's cap): numpy {np.__version__}, "
          f"python {platform.python_version()}, {os.cpu_count()} CPUs; probe.py's grouped {c['folds']}-fold call at "
          f"its pinned settings, {r['calls']} calls at each shape, d_model {r['d_model']}")
    print(f"counts: {c['results']} results x {c['band']} layers x (1 + {probe.N_SHUFFLES} shuffles) = "
          f"{c['primary_calls']} calls on {c['primary_rows']} rows; {c['comparator_points']} random points x "
          f"{schema.N_RANDOM} directions x {c['band']} layers = {c['comparator_calls']} calls on "
          f"{c['comparator_rows']} rows; {c['fits']} fits in all")
    for kind in ("primary", "comparator"):
        print(f"{kind} ms per call: {r['ms'][kind]}")
    print(f"projection: {c['primary_calls']} x median {_median(r['ms']['primary'])!r} ms + {c['comparator_calls']} x "
          f"median {_median(r['ms']['comparator'])!r} ms = {r['T_median_ms']!r} ms = {r['T_median_h']!r} h; at the "
          f"maxima {r['T_max_ms']!r} ms = {r['T_max_h']!r} h")
    return 0


def _gtime_selftest(chk, tmp: Path) -> None:
    """G-TIME-n's and gread-bench's checks, model-free: LOCK-n v0.1's pins held to the committed files that carry them
    (LOCK-n.md, G-VEC's and G-CAL-n's outputs of record, keys.py's sample words, the closure's twelve files, the
    package, n's backend identifier from the characterization's provenance), the plan on the session set of record,
    the campaign's counts over the lock's dose map, the identity, the benchmark's line and its writer, the artifact and
    its check, the command's flow over the numpy double behind every seam -- the refusals, G-VER's STOP, the PAUSE and
    its resume, the resume after COMPLETE, the smoke -- main()'s options, and gread-bench's counts and a small run."""
    import contextlib
    import copy
    import hashlib
    import io

    import numpy as np

    from valence_core.m import resume as m_resume
    from valence_core.n import cells, gcal, gvec, guard, ids, keys, schema, sessions, testing
    tmp = Path(tmp)
    tmp.mkdir(parents=True, exist_ok=True)

    def refused(fn) -> tuple:                           # (refused, its text); any other raise is not a refusal
        try:
            fn()
        except SystemExit as e:
            return True, str(e)
        except BaseException as e:                      # noqa: BLE001
            return False, f"{type(e).__name__}: {e}"[:200]
        return False, "no refusal"

    def work(p):                                        # the overlay is HEAD's archive: its bytes are the committed
        return Path(p).read_bytes() if Path(p).is_file() else None

    # LOCK-n v0.1's inputs, from the committed files
    li = gtime_lock_inputs(work)
    dm = li["dose_map"]
    chk("gtime: LOCK-n v0.1's inputs from the committed files (GT4): site 32, the valence row ba4da67fb717b5bb, "
        "G-CAL-n's two files at the lock's sha256s, and the dose map L §4's (d_eq 0.2869170055735837, d_20 "
        "0.5738340111471674, seven points, none merged)",
        li["site"] == 32 and li["v_sha16"] == LOCK_VALENCE_SHA16 and li["gcal_sha256"] == LOCK_GCAL_SHA256
        and li["dose_map_sha256"] == LOCK_DOSE_MAP_SHA256 and dm["d_eq"] == 0.2869170055735837
        and dm["d_20"] == 0.5738340111471674 and len(dm["points"]) == 7
        and not any(p["merged"] for p in dm["points"]), {k: li[k] for k in ("site", "v_sha16")})
    lock_bad = tmp / "LOCK-n.md"
    lock_bad.write_bytes(LOCK_PATH.read_bytes() + b"\n")
    gdir = tmp / "gcal-copy"
    gdir.mkdir()
    for name in (gcal.OUT_RECORD, gcal.OUT_DOSE_MAP):
        (gdir / name).write_bytes((GCAL_OUT / name).read_bytes())
    (gdir / gcal.OUT_DOSE_MAP).write_bytes((GCAL_OUT / gcal.OUT_DOSE_MAP).read_bytes() + b" ")
    r1 = refused(lambda: gtime_lock_inputs(work, lock_path=lock_bad))
    r2 = refused(lambda: gtime_lock_inputs(lambda p: None))
    r3 = refused(lambda: gtime_lock_inputs(work, gcal_dir=gdir))
    chk("gtime: ...a lock file that is not LOCK-n v0.1's, a file git cannot show, and a dose_map.json that is not the "
        "lock's are each refused",
        r1[0] and "LOCK-n.md" in r1[1] and r2[0] and "LOCK-n.md" in r2[1] and r3[0] and "dose_map.json" in r3[1],
        (r1, r2, r3))
    g = globals()
    real_gv = g["gcal_gvec_inputs"]

    def gv_with(**over):                                # G-VEC's inputs of record with one field moved
        def f(*a, **k):
            out = real_gv(*a, **k)
            return dict(out, **{key: (fn(out[key]) if callable(fn) else fn) for key, fn in over.items()})
        return f
    try:
        g["gcal_gvec_inputs"] = gv_with(v_sha16="0" * 16)
        r4 = refused(lambda: gtime_lock_inputs(work))
        g["gcal_gvec_inputs"] = gv_with(site=31)
        r5 = refused(lambda: gtime_lock_inputs(work))
        g["gcal_gvec_inputs"] = gv_with(R=lambda r: r * (1.0 + 1e-12))
        r6 = refused(lambda: gtime_lock_inputs(work))
    finally:
        g["gcal_gvec_inputs"] = real_gv
    chk("gtime: ...G-VEC's inputs with another valence row or another site are refused (L §3), and an R off the pinned "
        "map by one part in 10^12 is refused at the rebuilt map's equality with G-CAL-n's record",
        r4[0] and "L §3" in r4[1] and r5[0] and "L §3" in r5[1] and r6[0]
        and "is not G-CAL-n's record's or dose_map.json's" in r6[1], (r4, r5, r6))
    chk("gtime: the identity's sample_rule is keys.py's PIN, verbatim (L §5)",
        LOCK_SAMPLE_RULE in " ".join(str(keys.__doc__).split()), "")
    nprov = dict(CHARACTERIZED_PROVENANCE, choice_window_declared=schema.MAX_WINDOW)
    chk("gtime: n's backend identifier, from the characterization's provenance under the 4,096 window, is the lock's "
        "(L §17), and it bridges to the characterization's (R6)",
        m_resume.backend_identifier(nprov) == LOCK_BACKEND_IDENTIFIER
        and bridge_identifier(nprov) == CHARACTERIZED_IDENTIFIER, m_resume.backend_identifier(nprov))
    pkg, clo = _package_closure()
    chk("gtime: the package is the lock's (GT3: the build is in the driver alone); each of the closure's twelve files "
        "hashes to its pin on disk and in this process's closure (L §18)",
        pkg == LOCK_PACKAGE_SHA256 and all(guard.sha256_file(REPO / k) == v for k, v in LOCK_CLOSURE.items())
        and all(clo.get(k) == v for k, v in LOCK_CLOSURE.items()),
        (pkg, sorted(k for k in LOCK_CLOSURE if clo.get(k) != LOCK_CLOSURE[k])))

    # the identity, the plan and the campaign's counts, on the session set of record
    ss = sessions.load_sessions()
    ident = gtime_identity(package_sha256=LOCK_PACKAGE_SHA256, imported_sha256=dict(LOCK_CLOSURE),
                           weights=LOCK_WEIGHTS_SHA256, backend_identifier=LOCK_BACKEND_IDENTIFIER,
                           pod_id=CHARACTERIZED_POD, rendering_id=ids.MANIFEST_OF_RECORD, dose_map=dm,
                           v_sha16=li["v_sha16"])
    fr = {"tau": schema.TAU, "p0_count": 1, "p0_n": 26, "cadence": 160, "sample_key": "n-fid|{s}",
          "sample_rule": LOCK_SAMPLE_RULE, "alpha": 0.01, "ceiling": 0.25, "median_rel": 0.0013026706058596332}
    chk("gtime: the identity at 'time' (GT4): LOCK-n v0.1's sha256, its fidelity rule (p0 1 of 26, C 0.25 the ceiling "
        "and the identity bound, the median rel, alpha 0.01, the tile 160, the lock's sample words), the valence "
        "direction alone, the band 33..63, the label convention 'space', the window 4,096, the dose map of record",
        ident["stage"] == "time" and ident["lock_sha256"] == LOCK_SHA256 and ident["fidelity_rule"] == fr
        and ident["identity_bound"] == 0.25 and ident["directions"] == {"valence": "ba4da67fb717b5bb"}
        and ident["capture_layers"] == list(range(33, 64)) and ident["label_convention"] == "space"
        and ident["read_window"] == 4096 and ident["dose_map"] == dm, "")
    plan = gtime_plan(ss, ident)
    runs = list(GTIME_RUNS)
    want = ([("N1-V", "none", "0", "dose-rule", r) for r in runs] + [("N1-V", "valence", "+1", "dose-rule", r)
                                                                     for r in runs]
            + [("N1-V", "valence", "+1/2", None, r) for r in runs])
    six = gtime_sessions(ss)
    chk("gtime: the plan (GT1, GT2): 18 reads, launch indices 0..17, runs 0, 32, 64, 95, 127 and 159 in each block -- "
        "the six shadows re-computed (dose-rule), then N1-V valence +1 re-computed (dose-rule), then +1/2 with none, "
        "each at its dose map value; two floor sessions and four neutral; seq_len 1273 five times and 1268 once (run "
        "127)",
        [p.launch_index for p in plan] == list(range(18))
        and [(p.arm, p.direction_id, p.dose_label, p.fidelity_reason, p.session.bk_run) for p in plan] == want
        and [p.dose_value for p in plan] == [0.0] * 6 + [1.0] * 6 + [0.5] * 6
        and [s.is_floor for s in six] == [True, True, False, False, False, False]
        and [s.seq_len for s in six] == [1273, 1273, 1273, 1273, 1268, 1273], [p.read_id for p in plan[:2]])
    counts = campaign_counts(ident, ss)
    sizes = sorted(counts["cells"].values())
    pairs = sum(n * (n - 1) // 2 for n in counts["cells"].values())
    chk("gtime: the campaign's counts by the package's functions over the lock's dose map (GT8): N 7,680; K 3,637 = "
        "3,040 dose-rule + 597 keyed sample; 138 cells, 120 of 40 rows and 18 of 160; its read_plan_sha256 the lock's "
        "(L §6); the I/O sum's 322,560 pairs (GT9 (i))",
        (counts["reads"], counts["recomputations"], counts["dose_rule"], counts["sample"]) == (7680, 3637, 3040, 597)
        and sizes == [40] * 120 + [160] * 18 and counts["read_plan_sha256"] == LOCK_READ_PLAN_SHA256
        and pairs == 322560, {k: counts[k] for k in ("reads", "recomputations", "dose_rule", "sample")})

    # the benchmark's line and its writer
    a0, b0 = fit_line([2.0 + 0.5 * k for k in range(9)])
    try:
        fit_line([1.0])
        one = False
    except ValueError:
        one = True
    chk("gtime: the benchmark's line is least squares a + b k, exact on a line; one point is refused",
        abs(a0 - 2.0) < 1e-12 and abs(b0 - 0.5) < 1e-12 and one, (a0, b0))
    toy_i = dict(schema.example_identity("time"), d_model=8, layer=1, n_layers=4, capture_layers=[2, 3])
    schema.check_stage_identity(toy_i)
    bdir = tmp / "bench"
    bdir.mkdir()
    tpl = schema.example_record(toy_i, "N1-V", "valence", "+1", 7, launch=9)       # the self-test's stand-in only
    rk = rekeyed(tpl, 45, 3)
    moved = ("session_id", "bk_cell", "bk_run", "launch_index", "read_id", "shadow_read_id")
    chk("gtime: rekeyed moves a record to another of BK's runs -- its session's id, cell and run, its read id, its "
        "shadow's id and the launch index -- and leaves every other field as it was, the template untouched",
        rk["session_id"] == "neu_b0/45" and rk["bk_cell"] == "neu_b0" and rk["bk_run"] == 45 and rk["launch_index"] == 3
        and rk["read_id"] == schema.read_id("N1-V", "valence", "+1", "neu_b0/45")
        and rk["shadow_read_id"] == schema.shadow_read_id("neu_b0/45")
        and {k: v for k, v in rk.items() if k not in moved} == {k: v for k, v in tpl.items() if k not in moved}
        and tpl["bk_run"] == 7, {k: rk[k] for k in moved})
    ticks = iter(range(10 ** 6))
    b1 = io_bench(toy_i, bdir, tpl, n_records=5, clock=lambda: next(ticks) * 0.001)
    b2 = io_bench(toy_i, bdir, tpl, n_records=3)
    chk("gtime: the append benchmark (GT9 (i)): n re-keyed copies of a record appended to its cell through "
        "cells.append_record, each append timed, the line fitted; its temporary folder removed, nothing left behind",
        b1["records"] == 5 and b1["append_ms"] == [1.0] * 5 and (b1["a_ms"], b1["b_ms"]) == fit_line([1.0] * 5)
        and b1["cell"] == schema.cell_filename("N1-V", "valence", "+1") and len(b2["append_ms"]) == 3
        and all(x >= 0.0 for x in b2["append_ms"]) and list(bdir.iterdir()) == [],
        (b1["append_ms"], b2["append_ms"]))
    rb = (refused(lambda: io_bench(toy_i, REPO / "data" / "n" / "bench", tpl)),
          refused(lambda: io_bench(toy_i, tmp / "no", tpl)))
    try:
        io_bench(toy_i, bdir, tpl, n_records=1)
        r_one = False
    except ValueError:
        r_one = True
    chk("gtime: ...a benchmark folder inside the repository is refused as such, one absent is refused, and fewer than "
        "two records too",
        rb[0][0] and "never written inside the repository" in rb[0][1] and rb[1][0]
        and "is not an existing folder" in rb[1][1] and r_one, rb)

    class FakeStat:                                     # another device for one path, the real stat for the rest
        def __init__(self, other):
            self.other = Path(other).resolve()

        def __call__(self, p):
            st = os.stat(p)
            return type("S", (), {"st_dev": st.st_dev + 1})() if Path(p).resolve() == self.other else st
    fs_dir = tmp / "fs-a"
    fs_dir.mkdir()
    chk("gtime: same_filesystem (GT9 (i)): a folder and a root's nearest existing folder on one device pass, and on "
        "another device fail, the root's missing folders skipped up to the nearest that exists",
        same_filesystem(fs_dir, tmp / "no" / "such" / "root")
        and not same_filesystem(fs_dir, tmp / "no" / "such" / "root", stat=FakeStat(fs_dir)), "")

    # the command's flow, over the numpy double behind every seam (writes only under tmp)
    saved = {k: os.environ.get(k) for k in ("CUBLAS_WORKSPACE_CONFIG", "RUNPOD_POD_ID")}
    try:
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = CHARACTERIZED_PROVENANCE["cublas_workspace_config"]
        toys = [testing.toy_session(r) for r in range(schema.N_SESSIONS)]
        tss = [s for s, _i in toys]
        LS, LU = [6, 9, 17], [6, 11, 2]
        loaded_t = {"manifest_sha256": ids.MANIFEST_OF_RECORD,
                    "by_session": {s.session_id: {"ids": list(i)} for s, i in toys}, "by_variant": {},
                    "candidates": {LOCK_LABEL_CONVENTION: {"name": LOCK_LABEL_CONVENTION, "kept": True,
                                                           "labels": {tss[0].cue_S: LS, tss[0].cue_U: LU}}}}
        u = np.random.default_rng(5).standard_normal(12)
        u = u / np.linalg.norm(u)
        toy_li = {"lock_sha256": LOCK_SHA256, "site": 2, "R": 25.5, "R_ell": 23.90625, "v_unit": u,
                  "v_sha16": gvec.injection_sha16(u), "dose_map": gcal.dose_map(25.5, 23.90625),
                  "gvec_sha256": "1" * 64, "directions_sha256": "2" * 64, "gcal_sha256": LOCK_GCAL_SHA256,
                  "dose_map_sha256": LOCK_DOSE_MAP_SHA256}
        prov_t = dict(CHARACTERIZED_PROVENANCE, path="(toy)", choice_window_declared=schema.MAX_WINDOW)
        made: list = []
        bd = tmp / "bench-flow"
        bd.mkdir()

        class StubAdapter:
            def __init__(self, prov):
                self._prov = prov

            def provenance(self):
                return dict(self._prov)

        def genv(tag, **over):
            be = testing.CausalDouble()
            lines: list = []
            ticks = [0]

            def mk(_p):
                made.append(tag)
                return StubAdapter(prov_t)

            def tick() -> float:                        # 1 ms a call: every duration the stage measures is exact
                ticks[0] += 1
                return ticks[0] * 0.001
            base = dict(weights=lambda: {"repo": "toy", "revision": "0" * 12, "sha256": LOCK_WEIGHTS_SHA256,
                                         "n_files": 1, "path": "(toy)"},
                        load_sessions=lambda: list(tss), load_ids=lambda: loaded_t, lock_inputs=lambda: dict(toy_li),
                        gver=lambda s_, l_, p_: {"status": "PASS", "sessions": len(s_)},
                        env_provenance=lambda p: dict(prov_t), make_adapter=mk, adapter_shape=lambda a: (6, 12),
                        make_backend=lambda a: be, package=lambda: (LOCK_PACKAGE_SHA256, dict(LOCK_CLOSURE)),
                        counts=lambda i_, s_: copy.deepcopy(counts), pod=lambda: CHARACTERIZED_POD,
                        driver=lambda: (b"drv", b"drv"), shape=(6, 12), root=tmp / tag / "root",
                        report=tmp / tag / "report.json", out=tmp / tag / "out", bench_records=4, printer=lines.append,
                        clock=tick)
            base.update(over)
            for k in ("root", "report", "out"):                       # a self-test writes only under tmp
                if _within(Path(base[k]).resolve(), REPO.resolve()):
                    raise SystemExit(f"a self-test environment points {k} into the repository: {base[k]}")
            return GtimeEnv(**base), lines

        env1, lines1 = genv("run")
        rc1 = run_gtime(env1, bench_dir=bd)
        rep1 = cells.read_json(Path(env1.report)) if Path(env1.report).is_file() else {}
        art_p = Path(env1.out) / GTIME_ARTIFACT
        art = cells.read_json(art_p) if art_p.is_file() else {}
        recs1 = []
        for key in (("N1-V", "none", "0"), ("N1-V", "valence", "+1"), ("N1-V", "valence", "+1/2")):
            recs1 += cells.load_cell(env1.root, *key, identity=rep1.get("stage_identity"))[0]["records"]
        recs1.sort(key=lambda r: r["launch_index"])
        ok_art = refused(lambda: check_gtime(art))
        chk("gtime: the command's flow over the double: exit 0, COMPLETE, 18 records in three cells, one load; the "
            "artifact written and passing its check",
            rc1 == 0 and rep1.get("end_state") == "COMPLETE" and len(recs1) == 18 and made.count("run") == 1
            and art.get("schema") == GTIME_SCHEMA and not ok_art[0], (rc1, rep1.get("end_state"), ok_art))
        c1 = [r["duration_ms"] - (r["duration_ms_fresh"] or 0) for r in recs1]
        f1 = [r["duration_ms_fresh"] for r in recs1 if r["duration_ms_fresh"] is not None]
        mt = art.get("model_time", {})
        chk("gtime: ...the projection (GT8): T = 7,680 x median(c) + 3,637 x median(f) from the stage's own records, "
            "the maxima beside, 18 reads and 12 re-computed; each unsteered read's identity check at the bound C",
            mt.get("T_median_ms") == 7680 * float(np.median(c1)) + 3637 * float(np.median(f1))
            and mt.get("T_max_ms") == 7680 * float(max(c1)) + 3637 * float(max(f1))
            and (mt.get("reads"), mt.get("recomputed_reads")) == (18, 12)
            and [r["duration_ms_fresh"] is not None for r in recs1] == [True] * 12 + [False] * 6
            and all(r["identity"]["bound"] == 0.25 for r in recs1[:6])
            and all(r["identity"] is None for r in recs1[6:]), mt)
        ph = art.get("pod_hours", {})
        chk("gtime: ...the pod hours (GT9): the load, the benchmark over 4 records with its fit, the projection over "
            "the campaign's 138 cells, the per-read I/O on reads 1..17 (read 0 has no line before it), the three terms "
            "not measured",
            len(ph.get("loads_ms", [])) == 1 and ph["io"]["bench"]["records"] == 4
            and ph["io"]["bench"]["cell"] == schema.cell_filename("N1-V", "valence", "+1")
            and any(x.startswith("I/O benchmark (GT9 (i)): 4 appends of the stage's read 6 (N1-V|valence|+1), re-keyed")
                    for x in lines1)
            and ph["io"]["campaign_cells"] == 138 and ph["io"]["campaign_pairs"] == 322560
            and [x["io_ms"] is None for x in art["reads"]] == [True] + [False] * 17
            and ph["io"]["per_read_reads"] == 17 and ph["not_measured"] == list(GTIME_NOT_MEASURED), ph.get("io", {}))
        io_vals = [x["io_ms"] for x in art.get("reads", [])]
        bh = ph.get("io", {}).get("bench", {})
        t_ext = 7680 * 309.0 + 3637 * 357.1
        chk("gtime: ...with a clock that ticks 1 ms a call, every figure is exact: c 2 ms on the 12 re-computed reads "
            "and 1 ms on the 6 cached-only, f 1 ms; T = 7,680 x 2 + 3,637 x 1 = 18,997 ms at the medians and the "
            "maxima; the extension's T = 7,680 x 309.0 + 3,637 x 357.1 ms; the load 1 ms; the benchmark's appends "
            "1 ms each, a 1 and b 0, its projection a x 7,680 + b x 322,560; the per-read I/O 2 ms on reads 1..17, "
            "its lower bound 2 x 7,680 ms; each hours figure its ms over 3.6e6",
            c1 == [2] * 12 + [1] * 6 and f1 == [1] * 12
            and mt.get("T_median_ms") == 18997.0 and mt.get("T_max_ms") == 18997.0
            and mt.get("T_median_h") == 18997.0 / 3.6e6 and mt.get("T_max_h") == 18997.0 / 3.6e6
            and art.get("beside", {}).get("T_extension_ms") == t_ext
            and art["beside"]["T_extension_h"] == t_ext / 3.6e6 and ph.get("loads_ms") == [1]
            and bh.get("append_ms") == [1.0] * 4 and (bh.get("a_ms"), bh.get("b_ms")) == (1.0, 0.0)
            and ph["io"]["projected_ms"] == 1.0 * 7680 + 0.0 * 322560 and ph["io"]["projected_h"] == 7680.0 / 3.6e6
            and io_vals == [None] + [2.0] * 17 and ph["io"]["per_read_median_ms"] == 2.0
            and ph["io"]["lower_bound_ms"] == 2.0 * 7680 and ph["io"]["lower_bound_h"] == 2.0 * 7680 / 3.6e6,
            (c1, mt.get("T_median_ms"), ph.get("loads_ms"), io_vals[:3]))
        idx = {k: next((i for i, x in enumerate(lines1) if x.startswith(k)), -1)
               for k in ("STAGE G-TIME-n:", "WEIGHTS", "DRIVER", "LOCK-n v0.1's inputs", "identity:", "plan 0 ",
                         "the campaign (GT8)", "G-VER (G-TIME-n's start", "backend:", "read 0 ", "model time (GT8")}
        chk("gtime: ...its lines in order: STAGE first, then WEIGHTS, DRIVER (HEAD's), the lock's inputs, the "
            "identity, the 18 plan lines, the campaign's counts, G-VER before the load, the reads, the model time; "
            "the last line COMPLETE for the PI's cap",
            idx["STAGE G-TIME-n:"] == 0 and sorted(idx.values()) == list(idx.values()) and -1 not in idx.values()
            and sum(1 for x in lines1 if x.startswith("plan ")) == 18
            and f"DRIVER scripts/n_sessions.py {hashlib.sha256(b'drv').hexdigest()}: HEAD's committed bytes" in lines1
            and lines1[-1] == "G-TIME-n COMPLETE: the projections are for the PI's cap at LOCK-n v1.0 (GT16)",
            {k: v for k, v in idx.items()})
        chk("gtime: ...and no line holds a margin or a log-probability: the per-read lines are the runner's",
            not any("margin" in x or "logprob" in x for x in lines1), "")
        def fewer_campaign_reads(a):                    # the counts kept summing, the lock's 7,680 not
            k0 = sorted(a["campaign"]["cells"])[0]
            a["campaign"]["cells"][k0] -= 1
            a["campaign"]["reads"] -= 1
        for tamper, where in ((lambda a: a["model_time"].update(T_median_ms=a["model_time"]["T_median_ms"] + 1),
                               "model_time"),
                              (lambda a: a["reads"].pop(), "reads"),
                              (fewer_campaign_reads, "campaign"),
                              (lambda a: a["reads"][3].update(margin=0.0), "reads[3]"),
                              (lambda a: a["reads"][3].update(cached_ms=a["reads"][3]["cached_ms"] + 1),
                               "reads[3].cached_ms"),
                              (lambda a: a["campaign"].update(read_plan_sha256="0" * 64), "campaign"),
                              (lambda a: a["pod_hours"]["io"]["bench"].update(a_ms=0.5), "pod_hours.io.bench"),
                              (lambda a: a.update(extra=1), "its keys")):
            bad = copy.deepcopy(art)
            tamper(bad)
            got = refused(lambda: check_gtime(bad))
            chk(f"gtime: check_gtime refuses an artifact tampered at {where}, naming the field and no value",
                got[0] and got[1].endswith(f"malformed at {where}"), got)
        rc1b = run_gtime(env1, bench_dir=bd)
        rc1c = run_gtime(env1, bench_dir=bd, resume=True)
        chk("gtime: ...a second run, or a resume, while the artifact exists is refused before any read, exit 2",
            rc1b == 2 and rc1c == 2 and made.count("run") == 1
            and sum(1 for x in lines1 if x.startswith("REFUSED before any read: ")
                    and "writes its projection once" in x) == 2, lines1[-1])
        art_p.unlink()
        rc1d = run_gtime(env1, bench_dir=bd, resume=True)
        art_d = cells.read_json(art_p) if art_p.is_file() else {}
        chk("gtime: ...a resume after COMPLETE with no artifact launches nothing and writes it: two loads, no per-read "
            "I/O (no read launched)",
            rc1d == 0 and made.count("run") == 2 and len(art_d.get("pod_hours", {}).get("loads_ms", [])) == 2
            and all(x["io_ms"] is None for x in art_d.get("reads", [{}]))
            and art_d["model_time"]["T_median_ms"] == art["model_time"]["T_median_ms"], rc1d)

        # G-VER's STOP, and the refusals before any read
        env_g, lines_g = genv("gver", gver=lambda s_, l_, p_: {"status": "STOP", "causes": ["seq_len"]})
        rc_g = run_gtime(env_g, bench_dir=bd)
        chk("gtime: G-VER's STOP (GT7): exit 2, no weights load, no report, nothing written; its line says so",
            rc_g == 2 and made.count("gver") == 0 and not Path(env_g.report).exists() and not Path(env_g.root).exists()
            and lines_g[-1].startswith("G-VER STOP: no weights load, nothing is read, no report"), lines_g[-1:])
        keep = os.environ.pop("CUBLAS_WORKSPACE_CONFIG", None)
        env_c, lines_c = genv("cublas")
        rc_c = run_gtime(env_c, bench_dir=bd)
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = keep or ""
        cases = [("pod-none", dict(pod=lambda: None), {}, "without $RUNPOD_POD_ID"),
                 ("pod-other", dict(pod=lambda: "another-pod"), {}, "not the characterized one"),
                 ("weights", dict(weights=lambda: {"repo": "toy", "revision": "0" * 12, "sha256": "5" * 64,
                                                   "n_files": 1, "path": "(toy)"}), {}, "not the lock's (L §17)"),
                 ("driver", dict(driver=lambda: (b"drv", b"other")), {}, "runs only the committed driver"),
                 ("bid", dict(env_provenance=lambda p: dict(prov_t, choice_window_declared=8192)), {},
                  "is not the lock's 8264f719efd347a9"),
                 ("bridge", dict(env_provenance=lambda p: dict(prov_t, python="3.12.4")), {}, "(R6)"),
                 ("pkg", dict(package=lambda: ("0" * 64, dict(LOCK_CLOSURE))), {}, "not the lock's (L §18; GT3)"),
                 ("closure", dict(package=lambda: (LOCK_PACKAGE_SHA256, dict(LOCK_CLOSURE, **{"valence_core/x.py":
                                                                                               "0" * 64}))), {},
                  "closure files differing ['valence_core/x.py']"),
                 ("plan", dict(counts=lambda i_, s_: dict(counts, read_plan_sha256="0" * 64)), {},
                  "is not the lock's (L §6)"),
                 ("lockin", dict(lock_inputs=lambda: gtime_lock_inputs(lambda p: None)), {}, "LOCK-n.md is absent"),
                 ("benchrepo", {}, dict(bench_dir=REPO / "data" / "n" / "bench"),
                  "never written inside the repository"),
                 ("benchnone", {}, dict(bench_dir=None), "needs --bench-dir"),
                 ("benchgone", {}, dict(bench_dir=tmp / "no-such"), "is not an existing folder"),
                 ("smoke0", {}, dict(smoke=0, out=tmp / "s0"), "--smoke takes 1..18"),
                 ("smoke19", {}, dict(smoke=19, out=tmp / "s19"), "--smoke takes 1..18"),
                 ("smokeout", {}, dict(smoke=3), "writes only into --out"),
                 ("smokeres", {}, dict(smoke=3, out=tmp / "sr", resume=True), "a smoke never resumes"),
                 ("smokerepo", {}, dict(smoke=3, out=REPO / "data" / "n" / "s"), "outside the repository"),
                 ("smokeexists", {}, dict(smoke=3, out=bd), "exists: a smoke writes into a new folder"),
                 ("recout", {}, dict(out=tmp / "o"), "(--out is a smoke's)"),
                 ("ruling", {}, dict(resume=True, rulings={"p01": str(tmp / "no-ruling.md")}), "is not a file")]
        bad_cases = []
        for tag, over, kw, text in cases:
            e_, l_ = genv(tag, **over)
            args = dict(dict(bench_dir=bd), **kw)
            rc_ = run_gtime(e_, **args)
            line = next((x for x in l_ if x.startswith("REFUSED before any read: ")), "")
            if not (rc_ == 2 and text in line and made.count(tag) == 0 and not Path(e_.report).exists()):
                bad_cases.append((tag, rc_, line[:160]))
        chk(f"gtime: {len(cases) + 1} refusals before any read, each exit 2 with its reason on a REFUSED line, no "
            f"weights loaded and no report: the pod (none, another), the cuBLAS setting, the weights, the driver, n's "
            f"backend identifier, the R6 bridge, the package, its closure, the campaign's plan, the lock's inputs, the "
            f"benchmark's folder (in the repository, none, absent), the smoke's options, --out on a run of record, a "
            f"ruling that is not a file",
            not bad_cases and rc_c == 2 and made.count("cublas") == 0
            and any("CUBLAS_WORKSPACE_CONFIG" in x for x in lines_c), bad_cases[:3])
        import valence_core.m.keys as m_keys
        real_ka = m_keys.stream_known_answer
        m_keys.stream_known_answer = lambda: ["the stream's known answer differs (the self-test's stand-in)"]
        try:
            env_k, lines_k = genv("ka")
            rc_k = run_gtime(env_k, bench_dir=bd)
        finally:
            m_keys.stream_known_answer = real_ka
        chk("gtime: a stream whose known answer differs is refused before any read, exit 2, no weights loaded",
            rc_k == 2 and made.count("ka") == 0 and not Path(env_k.report).exists()
            and any(x.startswith("REFUSED before any read: the stream's known answer differs") for x in lines_k),
            lines_k[-1:])
        g_fs = globals()                                # the stage's own call to same_filesystem (M8)
        real_fs = g_fs["same_filesystem"]
        g_fs["same_filesystem"] = lambda a, b, stat=os.stat: False
        try:
            env_f, lines_f = genv("fsdev")
            rc_f = run_gtime(env_f, bench_dir=bd)
        finally:
            g_fs["same_filesystem"] = real_fs
        chk("gtime: a benchmark folder on another filesystem than the stage root's is refused through the stage "
            "(GT9 (i)), before any read, exit 2, no weights loaded and no report",
            rc_f == 2 and made.count("fsdev") == 0 and not Path(env_f.report).exists()
            and g_fs["same_filesystem"] is real_fs
            and any(x.startswith("REFUSED before any read: ") and "is not on the stage root's filesystem" in x
                    for x in lines_f), lines_f[-1:])
        post = []
        for tag, over, text in (("postprov", dict(make_adapter=lambda p: StubAdapter(dict(prov_t, python="3.12.4"))),
                                 "the loaded adapter's provenance is not the one checked before the load"),
                                ("postshape", dict(adapter_shape=lambda a: (6, 13)), "the checkpoint is (6, 13)")):
            e_, l_ = genv(tag, **over)
            rc_ = run_gtime(e_, bench_dir=bd)
            post.append(rc_ == 2 and not Path(e_.report).exists() and not Path(e_.root).exists()
                        and any(x.startswith("REFUSED before any read: ") and text in x for x in l_))
        chk("gtime: after the load and before any read, a provenance other than the one checked before it, or a "
            "checkpoint of another shape, is refused, exit 2, with no read and no report",
            post == [True, True], post)

        # a PAUSE (a fresh path biased at the S label's second token: the ceiling at the first shadow) and its resume
        env_p, lines_p = genv("pause", make_backend=lambda a: testing.CausalDouble(fresh_bias=(9, 2.0)))
        rc_p = run_gtime(env_p, bench_dir=bd)
        rep_p = cells.read_json(Path(env_p.report))
        p1 = rep_p["pauses"][0] if rep_p["pauses"] else {}
        chk("gtime: a fresh path that moves the margin past C (GT5): exit 3, PAUSE at read 0 -- fidelity-ceiling, the "
            "identity bound beside it -- the report written and no artifact; its line says the seat rules",
            rc_p == 3 and rep_p["end_state"] == "PAUSE" and p1.get("kind") == "fidelity-ceiling"
            and p1.get("also_fired") == ["identity-bound"] and p1.get("launch_index") == 0
            and not (Path(env_p.out) / GTIME_ARTIFACT).exists()
            and "G-TIME-n PAUSE: the report is written and no projection; the seat rules (GT5)" in lines_p, p1)
        n_lines = len(lines_p)
        rc_p1 = run_gtime(env_p, bench_dir=bd)
        chk("gtime: ...a second run without --resume, while the PAUSE's records are on disk, is refused before the "
            "load, exit 2 (prior_state: run with --resume)",
            rc_p1 == 2 and made.count("pause") == 1
            and any(x.startswith("REFUSED before any read: ") and "run with --resume" in x for x in lines_p[n_lines:]),
            lines_p[n_lines:][-1:])
        r_md = tmp / "ruling.md"
        r_md.write_text("a ruling\n", encoding="utf-8")
        rc_p2 = run_gtime(env_p, bench_dir=bd, resume=True, rulings={"p01": str(r_md)})
        rep_p2 = cells.read_json(Path(env_p.report))
        chk("gtime: ...its resume under the ruling (skip-only): p01 adjudicated, the next shadow pauses as p02, exit 3",
            rc_p2 == 3 and rep_p2["pauses"][0]["adjudicated"] is True
            and [p["launch_index"] for p in rep_p2["pauses"]] == [0, 1], [p["pause_id"] for p in rep_p2["pauses"]])

        # the smoke
        env_s, lines_s = genv("smoke", driver=lambda: (b"drv", b"other"))
        s_out = tmp / "smoke-out"
        rc_s = run_gtime(env_s, bench_dir=bd, smoke=3, out=s_out)
        art_s = cells.read_json(s_out / GTIME_ARTIFACT) if (s_out / GTIME_ARTIFACT).is_file() else {}
        chk("gtime: the smoke (GT14): its first 3 reads into --out, a new folder outside the repository, with a driver "
            "that is not HEAD's (named so); its artifact marked a smoke; the run of record's paths untouched",
            rc_s == 0 and art_s.get("smoke") == 3 and len(art_s.get("reads", [])) == 3
            and art_s["pod_hours"]["io"]["bench"]["cell"] == schema.cell_filename("N1-V", "none", "0")
            and lines_s[0].startswith("SMOKE: the first 3 of the 18 reads")
            and any("a smoke's, not HEAD's committed bytes (unchecked)" in x for x in lines_s)
            and lines_s[-1] == "G-TIME-n COMPLETE, a smoke, never of record"
            and not Path(env_s.root).exists() and not Path(env_s.report).exists() and not Path(env_s.out).exists(),
            (rc_s, lines_s[-1:]))

        # main()'s options for gtime and gread-bench, behind two traps (the box safety of a self-test that reaches the
        # driver's entry point after the commit): the recorder below stands in for the stage, and, beside it, no pod id
        # is set, so the real stage path would refuse at its pod check, and the production loaders are raising stubs
        g = globals()
        loaders = ("weights_of_record", "_load_adapter", "_gver_tokenizer")
        real_loaders = {n: g[n] for n in loaders}

        def trapped(*_a, **_k):
            raise SystemExit("the self-test's trap: a production loader was reached")
        pod_kept = os.environ.pop("RUNPOD_POD_ID", None)
        for n in loaders:
            g[n] = trapped
        try:
            penv = production_gtime_env()
            chk("gtime: (the self-test's own guard) main()'s cases run with RUNPOD_POD_ID unset and the production "
                "loaders trapped: weights_of_record, _load_adapter and _gver_tokenizer raise, as the production "
                "environment holds them",
                "RUNPOD_POD_ID" not in os.environ and all(g[n] is trapped for n in loaders)
                and penv.weights is trapped and penv.make_adapter is trapped and penv.gver is trapped, "")
            chk("gtime: the production environment's benchmark appends 160 records, one N1-V cell's capacity "
                "(GT9 (i)), and its clock is time.perf_counter",
                penv.bench_records == GTIME_BENCH_RECORDS == schema.capture_capacity("N1-V") == 160
                and penv.clock is time.perf_counter, penv.bench_records)

            def argv_error(argv) -> str:
                err = io.StringIO()
                try:
                    with contextlib.redirect_stderr(err):
                        main(argv)
                except SystemExit as e:
                    return err.getvalue() if e.code == 2 else f"exit {e.code}"
                return "no error"
            b_, o_ = str(bd), str(tmp / "o")
            for argv, want_t in ((["gtime"], "gtime needs --bench-dir"),
                                 (["gtime", "--bench-dir", b_, "--smoke", "3"], "--smoke N and --out DIR together"),
                                 (["gtime", "--bench-dir", b_, "--out", o_], "--smoke N and --out DIR together"),
                                 (["gtime", "--bench-dir", b_, "--root", o_], "gtime takes --bench-dir"),
                                 (["gtime", "--bench-dir", b_, "--convention", "space"], "gtime takes --bench-dir"),
                                 (["gtime", "--bench-dir", b_, "--ruling", "p01"], "--ruling takes PAUSE_ID=PATH"),
                                 (["gvec", "--bench-dir", b_], "--bench-dir: gtime's option only"),
                                 (["gread-bench", "--smoke", "1"], "gread-bench takes no option")):
                got = argv_error(argv)
                chk(f"gtime: main() refuses {' '.join(argv[:3])} … with \"{want_t}\"", want_t in got, got[-160:])
            real_run, real_gb = g["run_gtime"], g["cmd_gread_bench"]
            calls: list = []

            def recorder(_env, **kw):
                calls.append(kw)
                return 0
            g["run_gtime"] = recorder
            g["cmd_gread_bench"] = lambda: calls.append("gread-bench") or 0
            try:
                rcs = (main(["gtime", "--bench-dir", b_]),
                       main(["gtime", "--bench-dir", b_, "--resume", "--ruling", f"p01={r_md}"]),
                       main(["gtime", "--bench-dir", b_, "--smoke", "18", "--out", o_]), main(["gread-bench"]))
            finally:
                g["run_gtime"], g["cmd_gread_bench"] = real_run, real_gb
            chk("gtime: main() hands gtime's options to the stage, and gread-bench runs alone",
                rcs == (0, 0, 0, 0) and calls == [
                    {"bench_dir": b_, "smoke": None, "out": None, "resume": False, "rulings": {}},
                    {"bench_dir": b_, "smoke": None, "out": None, "resume": True, "rulings": {"p01": str(r_md)}},
                    {"bench_dir": b_, "smoke": 18, "out": o_, "resume": False, "rulings": {}}, "gread-bench"], calls)
        finally:
            for n, f in real_loaders.items():
                g[n] = f
            if pod_kept is not None:
                os.environ["RUNPOD_POD_ID"] = pod_kept
        chk("gtime: (the self-test's own guard) an environment pointing a stage path into the repository is refused",
            refused(lambda: genv("guard", root=GTIME_ROOT))[0] and refused(lambda: genv("guard", out=GTIME_OUT))[0], "")
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    # gread-bench (GT10)
    gc = gread_counts(31)
    chk("gread-bench: the count (GT10): 6 results x 31 layers x 201 calls = 37,386 on 320 rows; 4 random points x 24 "
        "directions x 31 layers = 2,976 on 80 rows; 403,620 fits in all",
        (gc["results"], gc["primary_calls"], gc["primary_rows"], gc["comparator_points"], gc["comparator_calls"],
         gc["comparator_rows"], gc["fits"]) == (6, 37386, 320, 4, 2976, 80, 403620), gc)
    import inspect

    from valence_core.n import probe
    ticks2 = iter(range(10 ** 6))
    seen_la: list = []
    real_la = probe.layer_auc

    def spy_la(X, y, groups, **kw):                     # what each timed call is given
        seen_la.append((tuple(np.asarray(X).shape), kw.get("shuffles"), kw.get("cv_seed")))
        return real_la(X, y, groups, **kw)
    probe.layer_auc = spy_la
    try:
        gb = gread_bench(calls=2, d_model=6, clock=lambda: next(ticks2) * 0.002)
    finally:
        probe.layer_auc = real_la
    chk("gread-bench: a small run (2 calls at each shape, width 6) times probe.layer_auc at each shape and projects "
        "the count: 2 ms a call gives 39,362 calls x 2 ms",
        gb["ms"] == {"primary": [2.0, 2.0], "comparator": [2.0, 2.0]} and gb["T_median_ms"] == (37386 + 2976) * 2.0
        and gb["T_max_ms"] == gb["T_median_ms"], gb["ms"])
    dflt = {k: v.default for k, v in inspect.signature(gread_bench).parameters.items()}
    chk("gread-bench: ...each timed call is probe.layer_auc on the contrast's shape -- 320 rows, then 80, at the width "
        "given -- with no shuffle and the folds' seed CV_SEED; and the defaults are 10 calls, the model's width 5,120 "
        "and the band of 31 layers",
        seen_la == [((320, 6), 0, probe.CV_SEED)] * 2 + [((80, 6), 0, probe.CV_SEED)] * 2
        and dflt["calls"] == GREAD_BENCH_CALLS == 10 and dflt["d_model"] == D_MODEL == 5120 and dflt["band"] == 31,
        (seen_la, {k: dflt[k] for k in ("calls", "d_model", "band")}))
    os.environ["RUNPOD_POD_ID"] = "a-pod"
    try:
        r_gb = refused(cmd_gread_bench)
    finally:
        if saved["RUNPOD_POD_ID"] is None:
            os.environ.pop("RUNPOD_POD_ID", None)
        else:
            os.environ["RUNPOD_POD_ID"] = saved["RUNPOD_POD_ID"]
    chk("gread-bench: refused on a pod (GT10: the laptop's CPU)", r_gb[0] and "refused on a pod" in r_gb[1], r_gb)


def _parse_rulings(ap, items) -> dict:
    """``--ruling PAUSE_ID=PATH``, each once (gtime's; backend-ext's own loop is unchanged)."""
    rulings: dict = {}
    for item in items:
        pid, sep, path = item.partition("=")
        if not sep or not pid or not path:
            ap.error(f"--ruling takes PAUSE_ID=PATH, not {item!r}")
        if pid in rulings:
            ap.error(f"--ruling names {pid} twice")
        rulings[pid] = path
    return rulings


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("command", nargs="?",
                    choices=("hashes", "gver-trial", "render-ids", "render-ids-iv", "render-ids-v", "backend-ext",
                             "backend-ext-2", "gvec", "gcal", "gcal-decode", "gtime", "gread-bench"))
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
    ap.add_argument("--convention", default=None)
    ap.add_argument("--gcal-dir", default=None)
    ap.add_argument("--bench-dir", default=None)
    a = ap.parse_args(argv)
    if a.selftest:
        return cmd_selftest()
    if a.gcal_dir is not None and a.command != "gcal-decode":
        ap.error("--gcal-dir: gcal-decode's option only")
    if a.bench_dir is not None and a.command != "gtime":
        ap.error("--bench-dir: gtime's option only")
    if a.command == "gtime":
        foreign = [f for f, given in (("--root", a.root is not None), ("--report", a.report is not None),
                                      ("--convention", a.convention is not None), ("--model-dir", bool(a.model_dir)),
                                      ("--tokenizer-dir", bool(a.tokenizer_dir)), ("--ids-dir", bool(a.ids_dir)),
                                      ("--pi-date", bool(a.pi_date))) if given]
        if foreign:
            ap.error(f"{', '.join(foreign)}: gtime takes --bench-dir, --smoke with --out, and --resume with --ruling, "
                     f"and loads from the model manifest's instruct path")
        if not a.bench_dir:
            ap.error("gtime needs --bench-dir, an existing folder outside the repository on the stage root's "
                     "filesystem (GT9 (i))")
        if (a.smoke is None) != (a.out is None):
            ap.error("a smoke takes --smoke N and --out DIR together; a run of record neither")
        return cmd_gtime(a.bench_dir, a.smoke, a.out, a.resume, _parse_rulings(ap, a.ruling))
    if a.command == "gread-bench":
        if any(given for given in (a.root is not None, a.report is not None, a.resume, bool(a.ruling),
                                   a.smoke is not None, a.convention is not None, bool(a.model_dir),
                                   bool(a.tokenizer_dir), bool(a.ids_dir), bool(a.out), bool(a.pi_date))):
            ap.error("gread-bench takes no option")
        return cmd_gread_bench()
    if a.command == "gcal":
        foreign = [f for f, given in (("--root", a.root is not None), ("--report", a.report is not None),
                                      ("--resume", a.resume), ("--ruling", bool(a.ruling)),
                                      ("--convention", a.convention is not None), ("--model-dir", bool(a.model_dir)),
                                      ("--tokenizer-dir", bool(a.tokenizer_dir)), ("--ids-dir", bool(a.ids_dir)),
                                      ("--pi-date", bool(a.pi_date))) if given]
        if foreign:
            ap.error(f"{', '.join(foreign)}: gcal takes --out and --smoke only (a smoke's), and loads from the model "
                     f"manifest's instruct path")
        return cmd_gcal(a.out, a.smoke)
    if a.command == "gcal-decode":
        foreign = [f for f, given in (("--root", a.root is not None), ("--report", a.report is not None),
                                      ("--resume", a.resume), ("--ruling", bool(a.ruling)),
                                      ("--smoke", a.smoke is not None), ("--convention", a.convention is not None),
                                      ("--model-dir", bool(a.model_dir)), ("--ids-dir", bool(a.ids_dir)),
                                      ("--out", bool(a.out)), ("--pi-date", bool(a.pi_date))) if given]
        if foreign or not (a.gcal_dir and a.tokenizer_dir):
            ap.error("gcal-decode takes --gcal-dir and --tokenizer-dir, and nothing else")
        return cmd_gcal_decode(a.gcal_dir, a.tokenizer_dir)
    if a.command == "gvec":
        foreign = [f for f, given in (("--root", a.root is not None), ("--report", a.report is not None),
                                      ("--resume", a.resume), ("--ruling", bool(a.ruling)),
                                      ("--convention", a.convention is not None), ("--model-dir", bool(a.model_dir)),
                                      ("--tokenizer-dir", bool(a.tokenizer_dir)), ("--ids-dir", bool(a.ids_dir)),
                                      ("--pi-date", bool(a.pi_date))) if given]
        if foreign:
            ap.error(f"{', '.join(foreign)}: gvec takes --out and --smoke only (a smoke's), and loads from the model "
                     f"manifest's instruct path")
        return cmd_gvec(a.out, a.smoke)
    stage_cmds = ("backend-ext", "backend-ext-2")
    stage_only = [f for f, given in (("--root", a.root is not None), ("--report", a.report is not None),
                                     ("--resume", a.resume), ("--ruling", bool(a.ruling)),
                                     ("--smoke", a.smoke is not None)) if given]
    if a.command not in stage_cmds and stage_only:
        ap.error(f"{', '.join(stage_only)}: the BACKEND extension's options only (backend-ext, backend-ext-2)")
    if a.convention is not None and a.command != "backend-ext-2":
        ap.error("--convention: backend-ext-2's option only")
    if a.command in stage_cmds:
        if a.model_dir or a.tokenizer_dir or a.ids_dir or a.out or a.pi_date:
            ap.error(f"{a.command} loads from the model manifest's instruct path and takes no folder options")
        if a.command == "backend-ext-2" and a.convention is None:
            ap.error("backend-ext-2 needs --convention NAME, the candidate A-n1 §2's comparison named "
                     "(ADDENDUM-n2 §4.1)")
        rulings = {}
        for item in a.ruling:
            pid, sep, path = item.partition("=")
            if not sep or not pid or not path:
                ap.error(f"--ruling takes PAUSE_ID=PATH, not {item!r}")
            if pid in rulings:
                ap.error(f"--ruling names {pid} twice")
            rulings[pid] = path
        return cmd_backend_ext(a.root, a.report, a.resume, rulings, a.smoke, a.convention)
    if a.command == "render-ids":
        if not (a.tokenizer_dir and a.out and a.pi_date):
            ap.error("render-ids needs --tokenizer-dir, --out and --pi-date")
        return cmd_render_ids(a.tokenizer_dir, a.out, a.pi_date)
    if a.command == "render-ids-iv":
        if not (a.tokenizer_dir and a.out and a.pi_date):
            ap.error("render-ids-iv needs --tokenizer-dir, --out and --pi-date")
        return cmd_render_ids_iv(a.tokenizer_dir, a.out, a.pi_date)
    if a.command == "render-ids-v":
        if not (a.tokenizer_dir and a.out and a.pi_date) or a.model_dir or a.ids_dir:
            ap.error("render-ids-v needs --tokenizer-dir, --out and --pi-date, and nothing else")
        return cmd_render_ids_v(a.tokenizer_dir, a.out, a.pi_date)
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
