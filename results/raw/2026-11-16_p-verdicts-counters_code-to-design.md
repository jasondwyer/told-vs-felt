# p's counters at VERDICTS: the script, committed before it reads any released record, and two readings of "the counts the record names" (Code → design)

*The dpo VERDICTS session (Code), PI date 2026-11-16, for the counters step of the three p units, which the coordinating session gave this session. For the PI to route. It answers to the seat's answers of 2026-11-16 on the joint block (`results/raw/2026-11-16_p-verdicts-decisions_design-to-code_answers.md`, sha256 `01ae2ae7…1b0f`, committed at `18102d0`), §3 and §4, routed by the PI's "Route as given" on that day's paste block, section B, items 3–5. It also answers to the coordinating session's instruction that both readings below go to the seat "before the counters step reads anything". What this commit carries: this block; `scripts/p_verdicts_counters.py` (sha256 `8e7fbed3dd8f8e7d35c61a1f9e97a90557310da78e8d116f2f680a70149f6905`); its self-test's stdout (`results/raw/2026-11-16_p-verdicts-counters_selftest.txt`); its two rounds of blind review (`results/raw/2026-11-16_p-verdicts-counters_review.md`); the blind values-check of these texts (`results/raw/2026-11-16_p-verdicts-counters_valuescheck.md`); and RESULTS.md, with this commit's entry and the dpo session's close line on `9189623`'s entry. Read for it: `valence_core/p/report.py` (`e807c5ad…5af1`), `valence_core/p/stage.py`, `valence_core/p/corrupt.py`, `valence_core/p/guard.py`, LOCK-p-OLMo-dpo.md §8.1, `valence_core/m/readrule.py`, `valence_core/m/scaffold.py`, `valence_core/m/resume.py`, `valence_core/m/corr.py`, the `task_correct` raw (`results/raw/2026-11-11_p-qual_task-correct.txt`, `57e9c7dc…56e2`), the seat's answers of 2026-11-09 on G-TIME-OLMo (p) (`results/raw/2026-11-09_p-gtime_design-to-code_answers.md`, line 34 and its routing item 3), and from `data/p/reports` the qual and time reads files' sham records and the p reports. Not opened: any checkpoint, call log or p output; nothing under `data/mf3` was listed or read. Calendar dates only; the commit hash is the record.*

## 0. The short form

- **The script and its self-test are committed here, before the counters step reads any released record** (the seat's §3). The self-test passes 37/37. It reproduces G-F0m-OLMo (p)'s committed sham `task_correct` from the reads files: 63/64 + 96/96, 63/64 + 96/96 and 64/64 + 96/96, that is 159/160, 159/160 and 160/160. It gets them two ways, through `task_correct.py` imported unchanged and through the script's own count, and it reproduces G-TIME-OLMo (p)'s row too (9/10, 10/10, 10/10).
- **Two readings of Q4 (b)'s "the counts the record names", for the seat. They are not applied:**
  - **R1:** `task_correct` is counted on the gate stages only, G-TIME-OLMo (p) and G-F0m-OLMo (p). The campaign's is not computed.
  - **R2:** the proxy's counts over the contrast sessions are not computed. They need the call logs.
- **What they hold:** the counters step for the three units, which reads nothing until the seat's answer on R1 and R2 is routed. They hold nothing else: the three `verdicts` runs and this commit go ahead, as the coordinating session has it (the inputs were committed at `db2e821`).

## 1. The script (Code's own step; the seat's §3 and §4)

- **What it imports, unchanged:**
  - From `valence_core/p/report.py`: p §2.3's predicates and p's own `session_counters`. The predicates are the hair trigger `line_break_in_stored_text`, and `control_chars`, `harness_first_line`, `refusal` and `corrupted_spelling`, with `clean_task_words` and the pinned lexicon. They are the definitions p's stage reports apply (`report.session_counters`, called at `valence_core/p/stage.py:966` with m's pool, `corr.load_pool()`).
  - p's renders of record (`valence_core/p/corrupt.py`, `RENDERS_OF_RECORD`), to tie a corrupted round to its item.
  - `task_correct.py`'s key table and match rule, loaded from the committed raw's bytes. The raw's sha256 is `57e9c7dc…56e2`, and the script after its header line hashes to its declared `9aa0e2d9…4e0f`. Both are checked before the source runs as a module, and it is never copied.
  - m's checkpoint reader (`resume.read_checkpoint`) and the act of release (`readrule.release_full`, m:271).
  - p's and m's `package_sha256` are asserted equal to the values every LOCK-p v1.0 names (`a38d93bb…`, `7756dcf4…`).
- **What it adds:** no definition. It applies the imported predicates to every recorded round of every recorded session of a stage, by arm (sham, contrast) and phase (forced, free). That is p §2.3's "tabulated over every generation of every p stage". It applies the imported key table and match rule to the rounds §3 below names.
- **What it reads in `run`, in order:**
  - Before the gates: the task_correct raw, the pools file and the lexicon.
  - No checkpoint until five gates pass, and no p report but the six time and qual p reports the gate-5 self-test reads:
    1. the three end notices' exit statuses, stated on the command line, each 0 (a non-zero exit is a STOP for the seat, §5 item 2);
    2. each unit's VERDICTS or NOT-RUN output present, checked by existence only;
    3. the packages equal to the lock's;
    4. the script's bytes equal to its blob at HEAD (committed, §3);
    5. its self-test passing in the same process. An exception inside the self-test closes this gate.
  - Then the nine checkpoints by exact path (`data/p/ckpt/OLMo-{ckpt}_{time,qual,campaign}.json`), never a listing, and each stage's committed p report.
- **Two passes.** Pass 1 reads and checks all nine checkpoints before any count is printed:
  - the checkpoint's identity;
  - its content as m's reader parsed it, equal to the bytes hashed;
  - the p report's record of that sha256, and for the campaign the lock's p package;
  - the read domain, recomputed by p's own `session_counters` and by the step's table, each equal to the committed report;
  - each corrupted round's task text, equal to its item's render;
  - the sham `task_correct` rows, equal to their committed figures.

  After the gates, any failure in pass 1 is a STOP (exit 4), and its STOP line is the only line it adds. Pass 2 prints.
- **What it prints:** the gate lines; the self-test's lines; digests; task_correct.py's key table, match rule and reading; the readings R1 and R2; and per stage the recorded session and round counts, the counts as k of n, the keys of the rounds counted and the control-character texts by key (F-p13 (a), JSON-escaped). It prints no pick, no menu, and no response other than those texts.

## 2. The self-test

- **Three runs,** at `nice -n 19`, one invocation in each of three battery windows the coordinating session granted; no other Python ran in them. The raw carries each run's stdout.
  - Run 1, on the script as built (`f4ec08c3…9339`): 23/23.
  - Run 2, after review round 1 (`a2687010…5b29`): 35/35.
  - Run 3, of record, on the bytes committed here (`8e7fbed3…6905`): 37/37, exit 0, stderr empty.
- **What run 3 shows:**
  - The imports:
    - the task_correct raw and the script inside it are at their sha256s, and a changed raw is refused;
    - task_correct.py's own 19 rule cases pass;
    - the packages equal the lock's, and p's renders are at their sha256 of record.
  - From the reads files:
    - the six reads files are at the digests the task_correct raw printed;
    - each gives its sham `task_correct` of record, through the imported `tally_file` and through the step's own count: G-F0m-OLMo (p) 63/64 + 96/96, 63/64 + 96/96 and 64/64 + 96/96; G-TIME-OLMo (p) 3/4 + 6/6, 4/4 + 6/6 and 4/4 + 6/6;
    - p's own `session_counters` over the same sham records equals the committed reports' sham cells, and no withheld cell is computed.
  - On two synthetic released records with a hit in every named cell:
    - the cells by arm and phase, the hair trigger, the control-character texts and `task_correct` are as their definitions fix them;
    - the step's read-domain cells equal `session_counters`';
    - each of five malformed rounds STOPs.
  - The run:
    - gates 1 and 2 behave as declared, and the run names nine checkpoints by exact path;
    - the two passes run on nine synthetic checkpoints, the printing captured in a buffer and checked (nine stage headers, nine withheld-cell lines, six `task_correct` lines); none of it is in the raw;
    - pass 1 STOPs, printing nothing, in six cases: a report not recording its checkpoint's sha256, a read-domain cell that differs, the step's table differing from a report `session_counters` reproduces, a checkpoint naming another stage, a sham `task_correct` row off its figure, and a campaign report built by another p package;
    - after the gates, a reader that refuses and a missing file are each a STOP.
  - The script's source makes none of the six listing calls the check names. The script lists only its scratch directory, and the package hashes list the package directories; nothing under `data/p/ckpt` is listed.

## 3. The two readings (declared, not applied)

### R1 — the stages `task_correct` covers at VERDICTS

- **The ruling,** the seat's answers of 2026-11-09 (`results/raw/2026-11-09_p-gtime_design-to-code_answers.md:34`), verbatim in part: "**Yes, from G-F0m-OLMo (p) on**, as a descriptive counter deciding nothing: **`task_correct`** — over the sham sessions' rounds at every gate-stage entry (forced and free; the contrast sessions' rounds at the unit's VERDICTS, where the free rounds are released)". The same line records "G-TIME's observation … now as the first row". Its routing item 3: "The `task_correct` counter under rule 23, Code's own step, from G-F0m-OLMo (p) on [declared]."
- **On record:** G-TIME-OLMo (p)'s sham row by the seat's read (sft 9 of 10, dpo 10 of 10, instruct 10 of 10); G-F0m-OLMo (p)'s sham row by Code at `a225a89` (159/160, 159/160, 160/160), confirmed by the seat (its answers of 2026-11-12, Q2). The campaigns' entry (`41bfab4`) reports no `task_correct`.
- **"From G-F0m-OLMo (p) on" bears on both ends.** G-TIME-OLMo (p) comes before G-F0m-OLMo (p), and the campaign comes after it. The same line names the scope "every gate-stage entry" and records G-TIME's sham row as the counter's "first row".
- **(a), Code's reading: the gate stages.** "At every gate-stage entry" names G-TIME-OLMo (p), the "first row", and G-F0m-OLMo (p).
  - At VERDICTS the counter covers their contrast sessions' rounds: one contrast session at G-TIME and eight at G-F0m-OLMo, per unit.
  - Their sham rows are recounted as a check.
  - The campaign is not a gate stage, so its `task_correct`, sham or contrast, is not computed.
  - The script is built this way (`TC_STAGES = ("time", "qual")`).
- **(b): from G-F0m-OLMo (p) on.**
  - G-F0m-OLMo's contrast rounds are counted, and so are the campaign's: 32 sham and 80 contrast sessions per unit.
  - G-TIME's contrast session is not counted. Its sham row stands as the seat's observation.
- **(c): every stage.** G-TIME-OLMo (p), G-F0m-OLMo (p) and the campaign are all counted.
- **Under (b) or (c)** the script changes before its first read. `TC_STAGES` changes, and the campaign has no committed sham figure to check its sham row against. The change would be reviewed and committed first.
- **Consequence.** The campaign checkpoints are read under every option, for p §2.3's counters. R1 decides only whose rounds are counted for `task_correct`.

### R2 — the proxy's counts over the contrast sessions

- **On record.** p's reports withhold them. G-F0m-OLMo (p)'s and the campaign's say "withheld to the unit's VERDICTS or NOT-RUN record (m:318; the seat's ruling (h)): every proxy count over the contrast sessions -- the number of a session's calls is its free-round exclusion position" (`CONTRAST_WITHHELD_QUAL`, `valence_core/p/stage.py:214–216`). G-TIME's says the same of its one contrast session (`CONTRAST_WITHHELD`, `:211–212`). The joint block raised them under Q3. The seat's §3 names p's counter definitions and the frozen key table, and §4 names "each unit's three checkpoints".
- **What computing them takes.** p's `stage.attribute_calls(sessions, events)` (`valence_core/p/stage.py:881`) attributes the proxy's calls to rounds from the checkpoint's sessions and the call log's events. The call logs are `data/p/ckpt/OLMo-{ckpt}_{time,qual,campaign}_p-calls.jsonl`, which are not checkpoints.
- **(a), Code's reading.** Q4 (b) licenses "each unit's three checkpoints" for "the counts the record names", and the seat's §3 names p §2.3's counters and `task_correct`. The proxy's counts are neither, and they need the call logs. So they are not computed, and each VERDICTS entry says so. The script is built this way.
- **(b).** They are owed, being "withheld to the unit's VERDICTS" in each report's own words. The step would also read each unit's three call logs by path, applying p's `attribute_calls` unchanged. That is a change to the script before its first read, reviewed and committed.
- **Consequence.** Under (b) the step reads nine call logs as well as the nine checkpoints; under (a) it reads none.

## 4. Questions

- **Q1 (R1).** `task_correct` at VERDICTS: the gate stages (a), from G-F0m-OLMo (p) on (b), every stage (c), or another form?
- **Q2 (R2).** The contrast sessions' proxy counts: not computed (a), computed from the call logs (b), or another form?

Each holds the counters step for the three units and nothing else.

## 5. Not questions

- The script's design follows the seat's §3 and §4: no definition added, every record read by exact path, and its first read of a released record gated on the third run's end and the four further gates. Its two rounds of blind review are in their raw, each finding applied or answered there; neither found a MAJOR.
- A difference between a recount and a committed figure is a STOP for the seat. Its line names the stage, and the report where the report is compared; the step-table STOP also names the cells that differ. Whether a recount may differ is not a question here.
