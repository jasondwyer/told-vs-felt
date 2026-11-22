# n — a supplement to the seven starred readings before G-VER's run: GV4's pins corrected and added to, GV5's ends as the launch reads them, and clauses added to Q2, Q4 and Q6, from the BUILD's review (code → design)

*The n-build session (Code), PI date 2026-11-22. For the seat, before G-VER's run, with the block it supplements:
`results/raw/2026-11-22_n-gver-starred-seven_code-to-design_STOP.md`, committed at `d92500b`, which stays as
committed. The PI's word governs only the nudge to the seat.*

*Where things stand:*
- *The block's seven readings, GV1, GV4, GV6, GV9, GV11, GV13 and GV14 (Q1–Q7), are committed for the seat at
  `d92500b`. The seat's nudge is held so that it carries this supplement too.*
- *G-VER's BUILD is drafted on GV1–GV16 as PINs, in the driver alone, with the `.gitignore` lines that admit the
  record. Draft 1's self-test ran 687 of 687 in a battery window the coordinating session granted. Its blind review
  (Code's scratch file `S/step4b/gver/review_report.md`, sha256 `3bb14a39…411d`, 164 lines) found one BUG and six
  RISKs. Draft 2 carries the fixes, and ran its self-test, 716 of 716, in a window of its own. One stale docstring
  line in it (`gver_environment`'s, which still says GV4 holds no pin on tokenizers) is for a later draft, with its
  own self-test window. The BUILD is not yet committed. Its commit, after this one, names the bytes it commits and
  carries the review's report whole, with every disposition.*
- *Five of the review's items change what the block tells the seat, or add to its questions: F3 and F4 in GV4, O3
  for Q4, O5 for Q2, and B7 for Q6. A sixth, F5, refines what the block says of G-VER's ends. They are below. The
  review's other items change no reading. The BUILD's commit gives each its disposition: among them, F1, F2, F6–F9,
  F11, M1–M17 and B2 are the driver's, and F10 the `.gitignore`'s.*
- *G-VER runs only after the seat's answers on Q1–Q7, with this supplement's clauses, the BUILD's commit, and the
  launch files' relay to the box (B:271–272).*

*Cited forms: B:line is the block at `d92500b`; L:line is `LOCK-n.md` (LOCK-n v0.1); drv:line is
`scripts/n_sessions.py` at `d92500b`, which is `91f0d35`'s; resume:line is `valence_core/m/resume.py`; ids:line is
`valence_core/n/ids.py`; ans21b:line is `results/raw/2026-11-21_n-gtime-starred-seven_design-to-code_answers.md`.
Draft 2 is Code's scratch file `S/step4b/gver/draft2/n_sessions.py` (sha256 `3df537d6…83c1`), cited by its
functions' names, since its lines move until the BUILD's commit. `S/` is Code's scratch folder, outside the
repository; the ids' render raws write it `<scratch>`. F, O and B numbers are this review's, unless a quote says
otherwise.*

*Code reads, builds and asks. Every reading below is Code's, and the seat rules it; Code adjudicates none.*

## 0. The short form

- **GV4 says cuBLAS's setting is not held (B:141–142). It is held, through R6** (the review's F3, §1.1). Draft 2 also
  checks it by name, as G-TIME-n does.
- **L §17 pins tokenizers 0.22.2 for n's box, and draft 1 held nothing on it** (the review's F4, §1.2). Draft 2 holds
  it before G-VER and in the record's check. That adds a pin to GV4.
- **Three items for the questions:** O3 for Q4 (§1.3); O5 for Q2 (§1.4), where the pinned `tokenizer_config.json`,
  read since the review, names its tokenizer class; and B7 for Q6 (§1.5).
- **GV5's ends, as the launch will read them** (the review's F5, §1.6): exit 2 is also a usage error's, before the
  stage runs, and an exception `run_gver` does not catch ends exit 1 with a traceback.
- **§2 gives the five clauses added to Q2, Q4 and Q6.** Nothing else in the block changes.

## 1. The corrections and additions, each against the reading it changes

**1.1 GV4: cuBLAS's setting is held, through R6 (the review's F3).**
- **The block** (B:141–142), under "Not held": "cuBLAS's setting and numpy's stream known answer, since nothing runs
  on the GPU and nothing is drawn". No kernel runs, but building the provenance makes a CUDA context, through
  `get_device_name` (drv:694; the review's O7).
- **What R6 holds.** `environment_provenance` (drv:676–698) puts `CUBLAS_WORKSPACE_CONFIG` into the provenance
  (drv:696). `m_resume.backend_identifier` hashes every field but `n_encodes_clipped`, `path` and `seed`
  (resume:147, :239–242). So the bridge to `4ed3f2c70fe8afbf` and n's identifier `8264f719efd347a9` both fail on
  another setting, and on another Python, torch, transformers, accelerate, safetensors, huggingface_hub, numpy, GPU,
  CUDA or capability (drv:687–698). L §17 pins the setting `:4096:8` (L:767–768).
- **So, as draft 1 built it,** a launch that leaves the setting unset refuses at R6, with exit 1 and no record, under a
  message that names R6 and not cuBLAS.
- **What draft 2 builds:** G-TIME-n's rule-2 check by name (drv:4230–4231), after the pod and before the STAGE line:
  "CUBLAS_WORKSPACE_CONFIG is not the characterized setting (rule 2; R6 holds it too)". It ends exit 1, with no
  record. The launch files export the setting, as G-TIME-n's did.
- **Still not held:** numpy's stream known answer, since nothing is drawn.

**1.2 GV4: tokenizers' version, L §17's, held (the review's F4).**
- **L:767–768:** "The environment of n's runs on the box, pinned (R:2889–2891; R:1845–1847): python 3.12.3, torch
  2.8.0+cu128, transformers 5.15.0, tokenizers 0.22.2; `CUBLAS_WORKSPACE_CONFIG` `:4096:8`".
- **Why it is not held through R6.** The decode, G-VER's only computation, runs in tokenizers' backend, and R6's
  libraries leave tokenizers out: the provenance's `library_versions` are torch, transformers, accelerate,
  safetensors, huggingface_hub and numpy (drv:687).
- **Draft 1** recorded the version and held nothing. The review reads that as unsound against L §17, while noting
  that `verify`'s decode equalities would still catch a decode that differs.
- **What draft 2 builds:** `LOCK_TOKENIZERS = "0.22.2"` (L §17), held in two places:
  - before G-VER: another version is a refusal, exit 1, with no record;
  - in the record's check (`check_gver`), so a record holds 0.22.2 or is refused.

  This adds a pin to GV4's list. The seat rules on it with Q2.

**1.3 For Q4 (GV9): when GV4's correction reaches `verify` (the review's O3).**
- **The block's correction** (B:134–139) sends a MANIFEST.json off its pin to `verify`, which ends as G-VER's STOP
  with the record.
- **That holds only while MANIFEST.json passes `ids.load`.** `ids.load` refuses a MANIFEST.json of another schema or
  form, or whose iv or v block's base is not its own part (ids:308–315), and it checks each file against MANIFEST.json's
  sha256 and record count (ids:317–327), all before `verify` sees anything. A folder that fails any of these is
  therefore `ids.load`'s refusal, exit 1, with no record: one of the refusals Q4 asks about.
- **In draft 2,** the loaders' own exceptions (a missing MANIFEST.json, bad JSON, a missing key, and the session set's
  ValueError) are refusals of the same kind, each on its REFUSED line. That is the review's F2, a driver fix, declared
  in the BUILD's entry.

**1.4 For Q2 (GV4), on GV3's hash check: what the tokenizer load may read (the review's O5).**
- **The block's Q2** (B:295–296) asks whether GV3's hash check should cover `vocab.json` and `merges.txt` beside the
  three named files.
- **The instruct folder's 22 files hold `config.json` too.** The review recalls that transformers' `AutoTokenizer`
  reads it only when `tokenizer_config.json` names no tokenizer class. The review did not check that file (one of the
  three hashed, ids:69).
- **Code has read it since the review.** `S/tok_n`, the tokenizer folder the ids' renders used (its provenance in
  `results/raw/2026-11-16_n-ids_render.md`), holds the three files alone, as `ids.check_tokenizer_dir` requires
  (ids:122–127), each at the model manifest's `olmo2_instruct` pin (shasum; `data/olmo/manifest.json`:252, :256 and
  :260). The renders loaded the tokenizer from it under transformers 5.5.0, the only environment they run in (ids:68,
  :113–114). Its `tokenizer_config.json`
  (`fff5b944…3fc7`) names `"tokenizer_class": "GPT2Tokenizer"`. By the review's recall, then, the class lookup does
  not read `config.json`. Neither the review nor Code has traced which files transformers 5.15.0's load reads beside
  `tokenizer.json` in the full folder, so `vocab.json` and `merges.txt` stay with Q2.
- **What already covers them:** every file in the folder is checked by byte count before G-VER (`check_weights_folder`,
  drv:636–649), and respawn step (i) re-hashes them all (CLAUDE.md's respawn protocol).
- **The stages' G-VER** loaded the same folder the same way and PASSed: the BACKEND extension and G-TIME-n's start.

**1.5 For Q6 (GV13): what a re-run needs (the review's B7).**
- **The record is written once.** Once it is committed, every later checkout holds it, so G-VER of record refuses with
  "exists". A re-run, GV13's on a new box or any the seat rules, needs the committed record moved aside first. That is
  how the seat ruled for G-TIME-n's re-run of record, where B7 is G-TIME-n's own review's: "B7's mechanics — the
  committed outputs moved aside before a re-run of record — are Code's, the entry naming both runs" (ans21b:27).
- **After a box change,** the driver's `CHARACTERIZED_*` constants change with the new characterization. The committed
  record then no longer passes the new driver's `check_gver`: its pins block holds the old pod and identifiers. Code's
  reading is that a re-run on a new box writes a new record, and the old one stands as the old box's, as G-TIME-n's
  "figures stand for the box they ran on" (ans21b:27). Q6's added clause asks it.

**1.6 GV5's ends, as the launch will read them (the review's F5).**
- **The block** (B:275–279) gives G-VER's ends as GV5 pins them: PASS, exit 0, and G-VER's STOP, exit 2, each with
  the record written; a refusal before G-VER, or any other failure, exit 1 with no record. Draft 2's `run_gver` ends
  so, each end on its own last line: "G-VER (n) PASS: the record is written"; "G-VER (n) STOP: the record is written;
  …"; and "G-VER (n): not run, and no record (exit 1; GV5)" or "G-VER (n): no record (exit 1; GV5)".
- **The process can end two more ways, outside those lines.** A usage error exits 2 with no record, before the stage
  runs: argparse's own, or `main()`'s refusal of any option given to `gver` (`--bench-dir` and `--gcal-dir` by their
  own messages); and Python exits 2 when it cannot open the script. An exception `run_gver` does not catch, at the
  tokenizer's load or in `verify` among them, ends with Python's exit 1 and a traceback, with no record and none of
  those last lines.
- **So the launch files read each end by three things together:** the exit code, the last line of stdout, and whether
  the record is on disk. PASS is exit 0 and STOP exit 2, each with its own last line and the record on disk; any
  other combination is a failure. The launch captures stderr. That is the launch files' part, declared in the
  BUILD's entry. Code reads it as changing no reading: GV5's ends are `run_gver`'s, and they stand.

## 2. The questions, with the additions

The block's Q1–Q7 stand. These add clauses to three of them:
- **Q2 (GV4), added:**
  - Is cuBLAS's setting held, by name and through R6, as draft 2 builds it?
  - Is tokenizers 0.22.2 held before G-VER and in the record's check (L §17)?
  - Does the hash-check clause (B:295–296) extend to `config.json`, beside `vocab.json` and `merges.txt`? The pinned
    `tokenizer_config.json` names its tokenizer class (§1.4).
- **Q4 (GV9), added:** a MANIFEST.json that `ids.load` refuses (ids:301–327) is a refusal (exit 1, no record) before
  `verify`. Is it a G-VER-STOP of "any cause" under N.3, with the rest of Q4's refusals?
- **Q6 (GV13), added:** on a re-run, is the committed record moved aside first, and does the re-run's record replace it
  as the record of the new box?
