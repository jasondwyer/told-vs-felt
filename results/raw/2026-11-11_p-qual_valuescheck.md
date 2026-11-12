# G-F0m-OLMo (p) ×3: the values-check of its entry, block and raws (Code's, before the commit)

*A blind agent with a fresh context, read-only on the repo, made one pass, PI date 2026-11-11.*
- *What it checked: the entry's draft (E, its two placeholders skipped), the block (B), the raw (R, its header lines)
  and the counter's raw (T, its header lines).*
- *Against what: the repo, m's and p's reports, the scratch captures and scripts, and the seat's answers they quote.*
- *Its brief quoted the list of record v2's items 1–5 verbatim and added:*
  - *no model, GPU or network;*
  - *Python only from script files, with no command line naming mlx, jlens, qwen, olmo or ipykernel;*
  - *of the reads files, the sham records only, and of a contrast record only its flag;*
  - *no duration, interval, total or bound computed from any pair of stamps or times, and none set against the sham
    seconds;*
  - *from the reports, only figures the texts state.*
- *Its report follows verbatim, with local roots scrubbed. Its line numbers are the texts' before the fixes.*

## Result and dispositions (Code's)

- **176 claims: 149 CONFIRMED, 11 IMPRECISE, 1 FAIL, 15 NOT CHECKABLE.** The fifteen are conduct, session messages with
  no capture, state the check cannot see, ordering (which would need times), and future commits.
- **The FAIL** (B:45) was a mistyped hash suffix for sft's reads file: `…2ce77` for `…a3ce77`. It is fixed. No figure,
  count or quotation was wrong.
- **Each IMPRECISE item was applied**, as suggested or in the suggestion's sense:
  - "stampless" became the one-launch-stamp form (E, B);
  - "p's sham counters" became "p's other sham counters", with `cap_hits` named as the fifth (E, B);
  - the withheld sentence was narrowed to the contrast free rounds (E);
  - "the seat's §7" became "the seat's answers of 2026-11-10 on the qual wiring, §7" (B);
  - the counters' domains were stated (B);
  - the counter's printed scope was stated in full (B, T), and is disclosed as reading (t4) for the seat's word;
  - the PID-1 start, the pre-launch listing's elapsed column and the loader's counters were named beside the run's
    stamps (B (a));
  - G-PWR (p) was put first in Q3, quoting PROPOSAL-p v0.2 §8 step 6 and the seat's answers of 2026-11-09, §6 (B);
  - R's list of what follows was completed with the five scripts, and the copy-back's description made exact (R).
- **Its observations:**
  - O1 is a present/absent inventory, carried in B (a).
  - O2: the entry now carries the key table, the match rule and the pool file's full sha256 itself, as the first entry
    that reports the counter.
  - O3: the docstring's citation of B4 is noted in T's header and in (t4).
  - O4: the assembler's docstring now says it hashes the outputs.
  - O5: the first picks are given as k of n, with the share beside.
- **Added after the check, and checked by tool:**
  - B §5(d)'s citation of the F3 values-checker's two laptop `git status --porcelain` runs during the batch (`05ef75d`,
    its disclosures, item (5));
  - reading (t4);
  - Q3's two quotations, each found verbatim at the section named;
  - the entry's declarations, verbatim against the seat's §3.
- **The checker's own disclosures** (D1–D5 below), for the seat under the list's item 8:
  - D1: two sub-second git calls, in item 1's forms, whose command lines carried the word "olmo" (a `git ls-files`
    with `data/olmo/` pathspecs, and a names-only `git status` with a lock file's name), against its brief's
    command-line rule;
  - D2: the G-TIME-OLMo (p) copy-back script's literal address and port, printed in its own tool output by a diff of
    that scratch script and reproduced nowhere;
  - D3: masked working copies of the six report files, written in scratch and deleted after reading;
  - D4: its own dry-test stamps, printed masked;
  - D5: what it read in the reads files: the listed fields of the sham records, and only the flag of a contrast
    record.

  It hashed the checkpoints and call logs, read nothing in them, and computed nothing from any stamp.

---

# Blind values-check: G-F0m-OLMo (p) ×3, the entry draft, the read block, the raw and the task_correct raw

Texts checked:
- **E** = `<scratch>/qualrun/entry_qual.md`. Its placeholders `@@STAMP@@` and `@@VC@@` were skipped.
- **B** = `results/raw/2026-11-11_p-qual_code-to-design_read.md`.
- **R** = `results/raw/2026-11-11_p-qual.txt`: its header (lines 1–24), plus a reproduction check of every section.
- **T** = `results/raw/2026-11-11_p-qual_task-correct.txt`: its header (lines 1–3), plus its sections.

Repo HEAD was `05ef75d`. Nothing in the repo was modified, staged or committed. Nothing ran on a model, on the GPU or over the network.

**Result: 176 claims. 149 CONFIRMED, 11 IMPRECISE, 1 FAIL, 15 NOT CHECKABLE.**

## Method (all by tool)

**Outputs**
- The 15 outputs were hashed with `shasum -a 256` over stdin, in a shell glob loop. No output name appeared on any command line, and no file under `data/p/ckpt` was opened, parsed, searched or listed with metadata. The list is in `vc/hash15.txt`.

**Reports and reads files**
- m's reports `*_qual_report.json` and p's reports `*_qual_p-report.json` were read for content. A stamp-bearing line was shown only with its digits masked.
- In the reads files `*_qual_reads.json`, only the records with `contrast` false were read. A contrast record was counted by its flag and nothing else.

**Sections**
- R's sections were matched line-for-line against the scratch captures. The stdout captures were compared with each carriage return replaced by a line break.
- The scripts were compared after the local-root scrub.

**Stamps and timing**
- Stamps were compared for **equality only**. No duration, interval, total or bound was computed from any stamp or time.

**Re-runs**
- `task_correct.py` was re-run in-process from `vc/run_tc.py`, in three modes: `--selftest`, `time` and `qual`.
- The wrapper's dry-test harness was re-run on its six cases with `vc/dry_rerun.sh`.

**Scripts, all in `<scratch>/qualrun/vc/`**
- `mask_view.py`, `mask_view2.py`: masked views.
- `find_in.py`: masked searches of single named files.
- `vc_main.py`: hashes, sections, report figures, scrub, stamp equality. Output in `vc_main_out.txt`.
- `vc_more.py`, `vc_shamsec.py`, `vc_quotes2.py`: follow-up checks.
- `run_tc.py` and `dry_rerun.sh`: the re-runs. The dry-test output is in `dry_rerun_out.txt`.

## Table of claims

### E (the entry draft)

| id | text:line | claim | grade | evidence / command |
|---|---|---|---|---|
| E-01 | E:1 | 2026-11-11; G-F0m-OLMo (p) ×3; PROPOSAL-p v0.2 §4.1, §8 | CONFIRMED | PROPOSAL-p v0.2 §4.1 inherits m's OLMo units. §8 step 6 reads "… → LOCK v0.2 → G-F0m-OLMo (24; the seat's read) → G-PWR …" (`find_in.py PROPP`). |
| E-02 | E:1 | m:302's G-F0m-OLMo-{ckpt} | CONFIRMED | PROPOSAL-m v1.11, line 302 (masked view `P_prop_m.md`). |
| E-03 | E:1–2 | run under register entries (1), (2), (6)–(9) | CONFIRMED | Every p report has `register_entered` [1, 2, 6, 7, 8, 9]. `valence_core/p/stage.py:162–163` sets `ENTERED`. |
| E-04 | E:2–3 | the PI's routing of 2026-11-11, "Route as given", on the seat's G-ID-F3 answers of 2026-11-10, §9 items 7–9 | CONFIRMED | The messages of commits a6c6297 and eb3e08c. The gid-f3 answers §9 have items 7 (the locks), 8 (the stamp rule) and 9 (the box run). |
| E-05 | E:3 | PASS ×3 on the box, path uncached | CONFIRMED | `STAGE … PASS path=uncached` in each stdout. In the m reports, `status` is PASS and `identity.path` is uncached; the p reports' `status` is PASS. |
| E-06 | E:3–4 | under LOCK-p v0.2 ×3 (`585df45`), standing | CONFIRMED | The 585df45 subject. The locks' blob sha256s are identical at 585df45, eb3e08c and HEAD (`git ls-tree` piped to `git cat-file blob` and `shasum`). gid-f3 §6 says "They stand as committed". |
| E-07 | E:4 | each checkpoint 24 sessions: 8 contrast, 16 sham | CONFIRMED | m reports: `planned` = `recorded` = {A0: 8, A0s: 16}. Each stdout has 24 session lines, 8 for A0 and 16 for A0s. |
| E-08 | E:4–5 | sham bar silent at 0/160; no hair trigger fired | CONFIRMED | `bars[0]`: k 0, n 160, crit 7, not fired. `hair_triggers` is [] in both arms. p's `line_break_in_stored_text` n is 0. |
| E-09 | E:5 | stopped for the seat's read | NOT CHECKABLE | This is the session's state. |
| E-10 | E:7–8 | pod `qny1x4v8padeke`, backend `641ee466f4553b6a` (BACKEND, `190ba90`); unchanged since characterization | CONFIRMED | Pre-flight `pod=`. Precheck "backend of record 641ee466f4553b6a" ×3. The 190ba90 subject. PID-1 start equals G-TIME's, whose raw says the BACKEND characterization ran on this container. |
| E-11 | E:8 | PID 1 has run since [stamp], as at G-TIME-OLMo (p) | CONFIRMED | Equality only: E's stamp equals the pre-flight `pid1_start`, R:2, R:265, R:296 and both records in the G-TIME raw (`TS.pid1-equal`). |
| E-12 | E:8 | `env.sh` `f5174faa…` | CONFIRMED | Pre-flight `env.sh sha256 f5174faa745eca6e`; the G-TIME pre-flight is the same. |
| E-13 | E:8–9 | torch 2.8.0+cu128, transformers 5.15.0, as at G-TIME-OLMo (p) | CONFIRMED | The pre-flight; the G-TIME raw's pre-flight; the m reports' `library_versions`. |
| E-14 | E:9 | the GPU idle before the launch | CONFIRMED | Pre-flight `… 0 MiB, 0 %`; precheck `0 MiB`. |
| E-15 | E:10 | the repo brought from `0afd842` to `eb3e08c` by a bundle, no network remote | CONFIRMED | Box HEAD 0afd8421… (= `git rev-parse 0afd842`). `git bundle verify`: contains eb3e08c… refs/heads/main, requires 0afd8421…. `box_sync_qual.sh` fetches from the bundle. `sync_out` gives HEAD eb3e08c…. |
| E-16 | E:10–12 | G-TIME's 15 untracked outputs, each digest-identical to its committed blob, set aside in `/workspace/gtime_p/box-untracked-2026-11-10` | CONFIRMED | The pre-flight lists 15 `_time` names. `git ls-tree -r --name-only` shows 15 `_time` outputs tracked at eb3e08c and 0 at 0afd842. `sync_out` reports SYNC OK. `box_sync_qual.sh` exits 15 or 16 otherwise. |
| E-17 | E:14–15 | the precheck at `qual` and the weights-files check CLEAR for all three units on the box | CONFIRMED | `precheck_out`: three CLEAR lines, weights files problems [], exit=0. |
| E-18 | E:15 | each `lock_sha256` its committed lock's (`3765fe22…`, `b739081f…`, `48e1c315…`) | CONFIRMED | The precheck prefixes against the sha256s of the LOCK-p blobs at 585df45 and eb3e08c. |
| E-19 | E:15–16 | (j)'s fresh closure is the recorded 14 files | CONFIRMED | Precheck: "14 files; problems [] ; equal … True". `data/p/gates/G-SHAPE-p.json` has 14 `import_closure` entries. |
| E-20 | E:17 | the chain rule dry-tested on six cases | CONFIRMED | `drytest_out` has six cases. The `vc/dry_rerun.sh` re-run produced identical lines. The harness differs from the wrapper in 4 lines only. |
| E-21 | E:18 | `p_sessions.py qual --unit OLMo-{ckpt}`, one run each, no `--resume`, back to back | CONFIRMED | INVOCATION lines; the wrapper's loop; the p reports' `call_log` (n_runs 1, resume false). |
| E-22 | E:19 | via `/workspace/qual_p/run_qual_p.sh` (sha256 `28da64c9…`) | CONFIRMED | sha256 of `qualrun/run_qual_p.sh`; `box_sha.txt`; the by-PID listing. |
| E-23 | E:19 | DRIVER `89551017…` at `eb3e08c` | CONFIRMED | DRIVER lines. The sha256 of `eb3e08c:scripts/p_sessions.py` is 89551017bdfd…af44. |
| E-24 | E:20 | "the stampless form the seat adopted (… §6 and §9 item 8)" | **IMPRECISE** | The citation holds, but the wrapper writes one launch stamp, as E:21 says. The seat's §6 wording is "the batch's one launch stamp and each checkpoint's exit code, no end, done or later launch stamp". |
| E-25 | E:20–21 | one launch stamp and each run's exit code: 0, 0, 0 | CONFIRMED | `box_out/stamps.txt` (a launch line, three `ran … exit=0` lines, `ended`) and the wrapper's code. |
| E-26 | E:21 | the entry gives no end time and no stage total | CONFIRMED | E's only time-bearing line is line 8, the container's PID-1 start. |
| E-27 | E:22 | the end-wait on the wrapper's PID alone | CONFIRMED | `wait_qual.sh` matches `ps -p PID -o args=` against the script name and reads nothing else. Its one output line is in the task output. |
| E-28 | E:22 | the end notice carried "batch ended" and the exit statuses | NOT CHECKABLE | A session message; no capture exists. |
| E-29 | E:23–24 | the raw link; address, port and local roots scrubbed | CONFIRMED | The link resolves. The `SC.*` checks (booleans only) found no IPv4 address, no host string or port digits, and no `/Users/` or `/private/` in E, B, R or T. |
| E-30a | E:25 | the figures come from m's and p's reports | CONFIRMED | See E-31a. |
| E-30b | E:25 | "Code did not open the checkpoints or the call logs" | NOT CHECKABLE | A claim about conduct. The scratch scripts only hash, copy and compare them. |
| E-31a | E:29–31 | every table cell except the next row's | CONFIRMED | The m reports' bars, templates and timing, and the p reports' counters and proxy (`RP.*`, `PP.*`): bar 0/160 ×3; hair triggers 0; sham valid 16 of 16; cap hits 1/0/0; proxy 160/160 with 0 cuts; sham seconds 102.105 / 88.389 / 85.237; contrast forced rounds 29/32/32; excluded 1 (lexical)/0/0; control characters 0 of 29/32/32. |
| E-31b | E:29 | "p's sham counters: all 0" (sft row) | **IMPRECISE** | p's own sham counters include `cap_hits`, which is 1 on sft (report `counters.sham`; stdout `P-REPORT sham counters … cap_hits 1`). The other four are 0. |
| E-32 | E:33 | each sham session ran 4 forced and 6 free rounds, with no exclusion and no claim | CONFIRMED | Each sham record has 4 forced and 6 free rounds. The m sham arm has 64 and 96 rounds, and its exclusions (both kinds) and claims are 0. |
| E-33 | E:33–34 | sft's one cap hit is sham s=6's first forced round | CONFIRMED | p's key is `A0s-OLMo-sft s=6 forced 0`. In the s=6 sham record, `cap_hit` is set on forced `ri` 0. m reports forced cap_hit 1, free 0. |
| E-34 | E:34 | sham seconds are m's report's sum over the sixteen | CONFIRMED | `valence_core/m/stages.py:1327–1333` sums over the sham records. Summing the sixteen sham records' own seconds gives each report's figure (`vc_shamsec.py`, equality only). |
| E-35 | E:35–36 | sft contrast s=4 excluded at a forced round by the lexical rule (`excluded_at_forced` `lexical@forced` 1) | CONFIRMED | The stdout line, and the m report's contrast block. |
| E-36 | E:36 | the stage PASSes because its bar reads the sham sessions | CONFIRMED | m:271 confines the binomial bars to sham-template sessions; the bar's template is A0s. |
| E-37 | E:37 | "the contrast seconds and every other contrast count are withheld" | **IMPRECISE** | The contrast seconds are withheld. m's pick-free report also gives two sets of contrast counts that are not withheld, and B §3 reports both. One is the forced-round event counts: cap hit, advisory, degeneracy, termination, and audit or echo claims, all 0. The other is the first-read flags: 7/8/8 reads, low label mass 0, top-1 not a label 1/1/0. |
| E-38 | E:38 | register entries (1), (2), (6)–(9) were entered | CONFIRMED | As E-03. |
| E-39 | E:38–39 | each m report's identity carries its lock's sha256 and `641ee466f4553b6a` | CONFIRMED | `identity.lock_sha256` equals the full lock sha256; `identity.backend_identifier` is `641ee466f4553b6a`. |
| E-40 | E:40–41 | term (d): `single_threaded` false, `tqdm_monitor` alive; recorded, never raised | CONFIRMED | The p reports' `term_d_at_stage_end`; PASS with no STOP line. |
| E-41 | E:42–43 | task_correct (rule 23; the seat's 2026-11-09 §3), first reported here by Code's own step; enters no bar, verdict sentence or label | CONFIRMED | The seat's §3 text. RESULTS.md mentions task_correct only as declarations (lines 1351, 1744, 1751). |
| E-42 | E:44 | sft 159/160 (63/64, 96/96); dpo 159/160 (63/64, 96/96); instruct 160/160 | CONFIRMED | The `run_tc.py` re-run equals both captures. |
| E-43 | E:45–46 | the key table and match rule are declared verbatim in B §4, bound by `8547d9a1…17a0` | CONFIRMED | B §4. The sha256 of `data/f/pools.json`, in the worktree and at eb3e08c. See observation O4. |
| E-44 | E:46–47 | T holds the script verbatim with its stdout | CONFIRMED | `ST.*`: T's sections equal the captures and the script. |
| E-45 | E:49–52 | each output byte-identical to the box's; the checkpoints -diff and may hold contrast picks; the call logs withheld and -diff; the reports under `data/p/reports/` | CONFIRMED (commit pending) | `copyback_out`: 15 identical, matching my shasum. `git check-attr` shows `diff: unset` on the six ckpt files. m:271. p's `call_log.form` reads "withheld like the checkpoint (m:318)". |
| E-46 | E:53 | the two raws, the block and the values-check's raw are committed with the entry | NOT CHECKABLE | A future commit. R, T and B exist, untracked. |
| E-47 | E:54–60 | the block's Q1 (with sft's exclusion), Q2 (t1)–(t3), Q3, and (a)–(d) | CONFIRMED | B §6, §4 and §5. |
| E-48 | E:62 | next: the seat's read, then the PI's routing; the pod's uptime goes back to the PI (§9 item 9) | CONFIRMED | §9 item 9: "[go; the pod up through it — your call]". |
| E-49 | E:62 | the pod stays up and idle | NOT CHECKABLE | Checking it needs the network. |
| E-50 | E:63 | not pushed; committed by path | NOT CHECKABLE | The commit is in the future. Now, local main is 23 commits ahead of origin/main (`16c99d5`), and eb3e08c is not on it. |

### B (the read block)

| id | text:line | claim | grade | evidence / command |
|---|---|---|---|---|
| B-01 | B:3 | Code's raw, PI date 2026-11-11 | CONFIRMED | Today's date; the run's date. |
| B-02 | B:3–5 | the STOP, quoting §9 item 9 | CONFIRMED | Verbatim in the gid-f3 answers §9 item 9 (`Q.B-s9-item9`). |
| B-03 | B:6 | nothing is pushed | CONFIRMED | origin/main is `16c99d5`; eb3e08c is not on it; the outputs are untracked. |
| B-04 | B:6–7 | no wall clock, no end time, no stage total (the same answers, §6) | CONFIRMED | B has no time-bearing line. §6 says "the read block computes no wall clock" and "no end time and no stage total". |
| B-05 | B:11–12 | the PI's routings of 2026-11-10 and 2026-11-11, relayed | CONFIRMED | RESULTS.md:1347–1353 (section B, "relayed by the coordinating session"); a6c6297 ("the coordinating session's relay"). |
| B-06 | B:13 | qual wiring BUILD `40086e8` | CONFIRMED | Its subject. |
| B-07 | B:14 | G-SHAPE-p re-run `f5e695c`; G-ANL-p re-run `ba89279` | CONFIRMED | Their subjects. |
| B-08 | B:15–16 | LOCK-p v0.2 `585df45` standing as committed (gid-f3 §6, committed at `a6c6297`) | CONFIRMED | a6c6297 adds the answers file. §6: "They stand as committed". |
| B-09 | B:17 | the record commit `eb3e08c` | CONFIRMED | eb3e08c holds the close lines and a dated note, RESULTS.md only. It is the bundle's head. |
| B-10 | B:19–20 | pod, backend, box repo at eb3e08c, synced by bundle with the 15 set aside by digest | CONFIRMED | As E-10, E-15 and E-16. |
| B-11 | B:21–22 | precheck CLEAR ×3 before the launch; the closure (14) equal to G-SHAPE-p's record | CONFIRMED | As E-17 and E-19. |
| B-12 | B:23 | "the stampless wrapper (§6's form)" | **IMPRECISE** | As E-24: it writes one launch stamp, as B:23–24 says. |
| B-13 | B:23–24 | one launch stamp; exit codes 0, 0, 0; one run each, no `--resume` | CONFIRMED | As E-21 and E-25. |
| B-14 | B:25 | the end-wait on the wrapper's PID alone | CONFIRMED | As E-27. |
| B-15 | B:25 | the end notice carried "batch ended" and the exit statuses | NOT CHECKABLE | No capture exists. |
| B-16 | B:26 | the raw link | CONFIRMED | It resolves from `results/raw/`. |
| B-17 | B:27–28 | PASS, uncached; 24 sessions as planned and recorded (8 A0, 16 A0s) | CONFIRMED | As E-05 and E-07. |
| B-18 | B:29 | silent at 0/160, critical 7 at n = 160, p0 0.02 | CONFIRMED | The bar's message. m:271's table: "G-F0m-OLMo sham rounds n = 160, p0 .02 → 7". |
| B-19 | B:30–31 | no hair trigger in either arm; `line_break_in_stored_text` 0 over every round of every session | CONFIRMED | m's `hair_triggers` [] in both arms. p's `hair_trigger` has domain "every round of every session" and n 0. |
| B-20 | B:32 | register entries entered "in that order" | CONFIRMED | `stage.py:162–163`, "The entries a gate stage enters, in order"; `stage.py:585`. |
| B-21 | B:33–37 | identity: lock sha256s; backend; m's package `7756dcf4…`; PROPOSAL-m `42ab36ec…`; path uncached | CONFIRMED | The m reports' identity. The PROPOSAL-m blob sha256 is 42ab36ecc814…. The locks list m's package as 7756dcf4…. |
| B-22 | B:38–39 | term (d) as at G-TIME-OLMo (p) | CONFIRMED | The G-TIME raw's three term (d) lines (70, 109, 147) are identical. |
| B-23 | B:40 | call log: one run, well formed, no malformed line, no stale reservation | CONFIRMED | `call_log`: n_runs 1, n_malformed_lines 0, stale_reservations [], well_formed true. |
| B-24 | B:42 | m:271's pre-VERDICTS read rule; m:302 | CONFIRMED | PROPOSAL-m line 271 contains "The pre-VERDICTS read rule". |
| B-25 | B:42 | "the seat's §7 of 2026-11-10" | **IMPRECISE** | Ambiguous: four seat answers dated 2026-11-10 have a §7 (a-m2-v04-stop, gid-f3 [its ledger], gtime-f3-r2, p-qual-wiring). |
| B-26 | B:44 | one reads file per checkpoint (m's `readrule`, written by m's stage) | CONFIRMED | The stdout READS lines; each file's `form` reads "pre-VERDICTS reads (m:271) …"; `valence_core/m/readrule.py`. |
| B-27 | B:45 | sft reads `cad7da75…2ce77` | **FAIL** | The file's sha256 is cad7da75e077…a5a3ce77, so the suffix is `…3ce77`, not `…2ce77`. R:12 and T:23 carry the full value correctly. |
| B-28 | B:46–47 | dpo `92c1cc85…c9db4f`; instruct `afbcfb35…d172d0` | CONFIRMED | My shasum. |
| B-29 | B:48–49 | 8 contrast records as `strip_contrast` leaves them (free rounds absent); 16 sham as `redact_sham` leaves them (`[config]`) | CONFIRMED | Each file has 8 contrast-flagged and 16 sham records. Its `form` reads "contrast = banner + forced rounds; sham = menus removed, chosen tag [config]". The docstrings of `readrule.strip_contrast` and `readrule.redact_sham` say the same. Each sham record's blinding line is m's sham-redacted form. No field of a contrast record was read. |
| B-30 | B:51–52 | m's pick-free reports `172f82c0…`, `efbe402d…`, `7c174940…` | CONFIRMED | My shasum; each report's `form` reads "pick-free stage report (m:271, m:318)". |
| B-31 | B:53–54 | p's reports `3f91b661…`, `9b1eb458…`, `57c7e5e3…` | CONFIRMED | My shasum. |
| B-32 | B:54 | each p report binds m's two files by sha256, equal to the files | CONFIRMED | `m_outputs` matches my shasum. |
| B-33 | B:55 | `proposal_p_sha256` `42f2977b…`; p's package `08bfa693…` | CONFIRMED | The PROPOSAL-p blob sha256 is 42f2977b941b…. The locks list p's package as 08bfa693…. |
| B-34 | B:55–56 | on sft, the declared SFT sentence | CONFIRMED | sft's `declared_sentences` is the SFT sentence in LOCK-p-OLMo-sft.md line 102; dpo and instruct have []. |
| B-35 | B:58–59 | the checkpoints are -diff and may hold contrast picks; the call logs are withheld | CONFIRMED | As E-45. |
| B-36 | B:61–62 | Code opened neither; read only the reports and sham records; no contrast record | NOT CHECKABLE | A claim about conduct. `task_correct.py` skips contrast records by their flag. |
| B-37 | B:66–72 | the sham table, every cell | CONFIRMED | `RP.*`/`PP.*`. The first-pick shares are k/n; the report's `share` field prints the same values in lowest terms. |
| B-38 | B:74–75 | no exclusion (strict or tolerant), no claim; no advisory, degeneracy or termination | CONFIRMED | `excluded_sessions` and `strict_excluded_sessions` are all 0, as are the claims and event counts. |
| B-39 | B:76–77 | the one cap hit: sft s=6 at its first forced round, in m's forced `cap_hit` and p's `cap_hits` | CONFIRMED | As E-33. |
| B-40 | B:78–80 | p's sham counters "are control_chars, harness_first_line, refusals and corrupted_spelling over the forced rounds, each 0"; the free-round corrupted spelling withheld | **IMPRECISE** | The 0s and the withheld clause hold (p's `withheld` line). But only `corrupted_spelling`'s domain is the forced rounds; the other three run over every sham round. p's report also lists a fifth sham counter, `cap_hits`. |
| B-41 | B:81–82 | the reads column is m:283's "reported, no bar" flags (n = 96); low label mass 0; top-1 as shown | CONFIRMED | m:283's text; each sham arm's `reads`. |
| B-42 | B:83–86 | first-pick shares by pair | CONFIRMED | `first_pick_P_by_pair`. |
| B-43 | B:87 | the sham seconds are the sum over the sixteen; the contrast seconds withheld (m:318) | CONFIRMED | As E-34. The report reads "withheld to the unit's VERDICTS entry (m:318)". |
| B-44 | B:88 | m:205's basis stands as LOCK-p v0.2 item 3 has it; the sham seconds beside, no basis | CONFIRMED | LOCK-p v0.2 item 3 (lock line 13). |
| B-45 | B:90–97 | the contrast table; ruling (h)'s form; m:283's flags over first reads | CONFIRMED | The m contrast blocks; `contrast_first_read_flags` (scope "first reads of domain sessions"); p's `contrast_forced_control_chars`. |
| B-46 | B:99–101 | the stdout line; `lexical@forced` 1; forced lexical claim 1; 29 forced rounds over the eight sessions; 7 domain sessions | CONFIRMED | The stdout and the m report. |
| B-47 | B:102 | the stage PASSes because its bar reads the sham sessions | CONFIRMED | As E-36. |
| B-48 | B:103 | the excluded session's record is in the reads | CONFIRMED | Each reads file holds 8 contrast-flagged records, one per contrast session, counted by flag only. "Code did not open it" is conduct, as B-36. |
| B-49 | B:104–105 | in the contrast forced rounds, no cap hit, advisory, degeneracy or termination, and no audit or echo claim | CONFIRMED | `RP.*.contrast.events`. |
| B-50 | B:106–107 | every other contrast count withheld (p's `withheld` line; m's `free_rounds` line) | CONFIRMED | Both lines are present. |
| B-51 | B:109–113 | task_correct: rule 23; the seat's §3; Code's own step, A-m2 v0.3 §3.4's form; the licence (2026-11-10 §4, the PI's B4); no bar, verdict sentence or label | CONFIRMED | The seat's §3. ADDENDUM-m2 v0.3 (46773e2) has a §3.4, "Counters, declared (rule 23 …)". The qual-wiring §4. RESULTS.md:1351 holds B4. |
| B-52 | B:115–116 | the key table verbatim; "the roster's sixteen items with one key each" | CONFIRMED | Verbatim in the seat's §3. |
| B-53 | B:117–118 | each key is the first gold of exactly one `CORR_clean` item | CONFIRMED | `PL.bijection`, `PL.first-gold`. |
| B-54 | B:119–120 | the full pools sha256 | CONFIRMED | My shasum (worktree and eb3e08c). |
| B-55 | B:121–123 | the match rule verbatim | CONFIRMED | Byte-equal to the seat's §3 text. |
| B-56 | B:124–130 | the rows | CONFIRMED | As E-42. |
| B-57 | B:132 | G-TIME's row, the seat's own: 29 of 30 (9, 10, 10) | CONFIRMED | The seat's §3. |
| B-58 | B:133–134 | a scratch script, verbatim with its sha256 in T; self-test 19/19 | CONFIRMED | The sha256 is 9aa0e2d9…; the self-test re-run gives 19/19. |
| B-59 | B:135–136 | each item from the round piece's `Task:` line, matched to one task; the free rounds' item field withheld | CONFIRMED | The code (`task_of`, `by_task`). The sham free rounds carry no `item` key. |
| B-60 | B:137 | a forced round's `item` and `task_text` must agree | CONFIRMED | `task_correct.py:144` (T:172). |
| B-61 | B:138 | a contrast record is skipped by its flag | CONFIRMED | `task_correct.py:118–121` (T:146–149). |
| B-62 | B:139–140 | "It prints k of n … and the files' digests, nothing else." | **IMPRECISE** | It also prints a stage line, the pools sha256, the key table, the match rule, Code's reading, record counts and the alternative-reading line. "Which rounds missed is not printed" holds. |
| B-63 | B:141 | on G-TIME's committed reads files it gives 29 of 30 | CONFIRMED | The re-run. The three files equal their blobs, committed at 2258c52 (`git ls-files -s` against `git hash-object --stdin`). |
| B-64 | B:143–145 | (t1): `pools.json`; m's label roster `data/olmo/a1_repair_roster.json` with four selected entries; the labels asserted absent; no task item or key | CONFIRMED | `corr.py:77,119,514`. The roster's `n_select` is 4 and `selected` has 4 entries. `readrule._assert_no_label`. The roster has no task, gold or key field. |
| B-65 | B:146–147 | (t2) the reading; deletion changes no count, here or at G-TIME | CONFIRMED | The code; both stdouts say "no count changes". |
| B-66 | B:148–150 | (t3): `twenty-four` (item 13) and `shut` (item 15) not credited; the two misses | CONFIRMED | They are at `CORR_clean` list indices 13 and 15, counted from 0. The other second golds (seven, twelve, three, two) are credited by the number-word map. The misses are sft forced and dpo forced. |
| B-67 | B:154–156 | (a) "The raw's stamps are the wrapper's one launch stamp and m's PROVENANCE start stamps"; the §6 quote | **IMPRECISE** | The named stamps are present (one launch stamp; one PROVENANCE stamp per stdout and per m report), and §6's words are verbatim. But R also carries the container's PID-1 start stamp, three times (R:2, R:265, R:296). |
| B-68 | B:157 | a later run's start stamp follows the earlier run's end | CONFIRMED | The wrapper runs each stage in the foreground, in sequence. |
| B-69 | B:158 | the block and the entry give no end time and no stage total | CONFIRMED | As B-04 and E-26. |
| B-70 | B:158 | "Code computed nothing from any pair of them" | NOT CHECKABLE | A claim about conduct. |
| B-71 | B:159 | the launch pattern matched three PIDs | CONFIRMED | `launch_out`: 17156 17162 17273. |
| B-72 | B:159–160 | the other two were the remote shell and its command substitution | NOT CHECKABLE | Their command lines were not captured. This is consistent with the launch command text. |
| B-73 | B:160–161 | a by-PID listing, arguments only and no times, identified the wrapper; both are in the raw | CONFIRMED | `launch_out` line 3; R:254–259. |
| B-74 | B:162–163 | the copy-back used `tar -m`, so the copies carry no box write time; a change from G-TIME's copy-back | CONFIRMED | Diffing `qualbuild/` against `qualrun/copyback_qual.sh`: both tar extractions went from `xf` to `xmf`. G-TIME's copy-back script in scratch uses `xf`. |
| B-75 | B:163 | "made after the end" | NOT CHECKABLE | Checking it would need file or command times. |
| B-76 | B:163–164 | every file compared by sha256 at both ends; all identical | CONFIRMED | 15 outputs plus the 5 wrapper outputs; my hashes match all of them. |
| B-77 | B:165–166 | (d) the laptop `pgrep` was empty at the launch; no model run announced | NOT CHECKABLE | No capture exists in scratch. |
| B-78 | B:170–171 | Q1 (m:302), with sft's exclusion | CONFIRMED | The citation. |
| B-79 | B:173–174 | the campaign's wiring is its own move before LOCK-p v1.0 (B2 of 2026-11-10) | CONFIRMED | RESULTS.md:1349. |
| B-80 | B:173–174 | "p's chain after the qualification, in the seat's order: the campaign's wiring, …, and v1.0's contents" | **IMPRECISE** | The list omits G-PWR. m:302, PROPOSAL-p §8 step 6 and the seat's 2026-11-09 §0 all place it after the qualification and before v1.0. |
| B-81 | B:174–175 | the pod's uptime goes back to the PI after this STOP (§9 item 9) | CONFIRMED | §9 item 9. |

### R (the raw): header lines and sections

| id | text:line | claim | grade | evidence / command |
|---|---|---|---|---|
| R-01 | R:1 | the heading's anchors, the routing and §9 items 7–9 (the locks, the stamp rule, the box run), relayed | CONFIRMED | As E-01 to E-04. |
| R-02 | R:2 | pod `qny1x4v8padeke` (jspace-olmo-m), 1 x A100-SXM4-80GB, US-CA-2 | CONFIRMED | The 190ba90 subject; the pre-flight GPU line. |
| R-03 | R:2 | backend id: BACKEND entry `190ba90`; each lock's BACKEND OF RECORD line; each report's identity | CONFIRMED | Each lock has one BACKEND OF RECORD line with `641ee466f4553b6a`, and each m report's `identity` carries it. p's reports have no backend field. |
| R-04 | R:2 | PID 1 started [stamp], as at G-TIME-OLMo (p) and the BACKEND characterization | CONFIRMED | Equality only (`TS.pid1-equal`). The G-TIME raw says the characterization ran on this container. |
| R-05 | R:2 | box repo at `eb3e08c` | CONFIRMED | `stamps.txt` HEAD=; "tree clean at eb3e08c". |
| R-06 | R:3 | wrapper path and sha256 `28da64c9…5d7b`; env.sh sourced; cwd | CONFIRMED | My sha256 and the wrapper's code. |
| R-07 | R:4 | the command per checkpoint; one run; no `--resume` | CONFIRMED | INVOCATION lines. |
| R-08 | R:5 | the chain rule, declared before the launch, dry-tested on 6 cases | CONFIRMED | The wrapper's loop, R:237–247. The wrapper's sha256 was re-hashed on the box at the sync (`box_sha.txt`), before the launch. The dry-test re-run gave identical results. |
| R-09 | R:6 | one launch stamp and the exit codes; no end, done or later launch stamp; the PROVENANCE start stamps are "the Q4 ruling's unavoidable records" | CONFIRMED | The wrapper's code; `stamps.txt`. The Q4 ruling (`results/raw/2026-10-18_m-campaign-driver_review.txt:325`): "The unavoidable records — … the report's PROVENANCE start stamp …". |
| R-10 | R:6 | "No other stamp of the run is in this raw." | CONFIRMED | Literally true. The other time-bearing lines are not stamps of the run (see O1). |
| R-11 | R:7 | the RESULT line: 23 of 24 valid on sft, 24 of 24 on dpo and instruct | CONFIRMED | The stdout (sft: 23 valid, 1 excluded) and the reports. |
| R-12 | R:8 | outputs byte-identical with sha256 at both ends; the checkpoints -diff; the call logs withheld and -diff | CONFIRMED | As E-45. "Never opened by Code" is conduct, as E-30b. |
| R-13 | R:9–23 | the 15 sha256s | CONFIRMED | Equal to my shasum and to `copyback_out` (`H1.*`). |
| R-14 | R:24 | the stdout sha256 prefixes; carriage returns shown as line breaks | CONFIRMED | The captures hold 13, 18 and 14 CRs and no CRLF. Each section equals its capture with CR replaced by LF. |
| R-15 | R:24 | "What follows, verbatim: … the end-wait; the copy-back." | **IMPRECISE** | It omits the five scripts appended after the copy-back: preflight_qual.sh, box_sync_qual.sh, box_precheck_qual.py, wait_qual.sh and copyback_qual.sh. |
| R-16 | R:24 | address and port scrubbed to `<host>` and `<port>`; local roots to `<repo>`, `<scratch>`, `<home>` | CONFIRMED | The `SC.*` checks. |
| RS-01 | R:26–31 | the stamps section equals `box_out/stamps.txt` | CONFIRMED | `S.stamps.txt` (one block). |
| RS-02 | R:33–217 | the three stdout sections and their sha256 headers equal the captures | CONFIRMED | `S.stdout-*`; `H2.Rsection-*`. |
| RS-03 | R:219–248 | the wrapper section equals `run_qual_p.sh` | CONFIRMED | `S.wrapper`. |
| RS-04 | R:250–251 | `wrapper.out` "(0 bytes)", "(empty)" | CONFIRMED | Its sha256 is that of empty input. |
| RS-05 | R:253–259 | the launch output equals `launch_out.txt`; one process in its own session under PID 1 | CONFIRMED | Line 3 reads `17162 1 17162 bash …run_qual_p.sh`. |
| RS-06 | R:261–322 | the pre-flight, `box_sha` (= `laptop_sha`), `sync_out`, `precheck_out`, `drytest_out` and the bundle head line | CONFIRMED | `S.*`; `H3.box4==laptop4`; `git bundle list-heads`. |
| RS-07 | R:296 | PID-1 start as at G-TIME; env.sh; versions; GPU idle; no earlier-stage process; repo at 0afd842, clean, 15 untracked | CONFIRMED | Equality and substring checks done in-script. The ps listing's command column shows only sshd, nginx and ps. |
| RS-08 | R:297 | `git bundle create … main ^0afd842`; one head; no size printed | CONFIRMED | `git bundle verify` and `list-heads`; the bundle's sha256 equals the one given. |
| RS-09 | R:304 | box_sync's behaviour | CONFIRMED | The script as reproduced at R:378–405 (exits 10–22 on any surprise). |
| RS-10 | R:307 | the precheck is model-free and imports the driver as `qual` does; the closure runs first | CONFIRMED | `box_precheck_qual.py`. `stage.precheck`'s docstring: "Every refusal that needs no adapter". |
| RS-11 | R:315 | dry-tested "before the launch" and "re-run after the end" | NOT CHECKABLE | Ordering only; the outcomes are confirmed by RS-06 and the re-run. |
| RS-12 | R:316 | the harness is the wrapper with 4 lines replaced | CONFIRMED | `diff`: 4 lines. |
| RS-13 | R:324–326 | `wait_qual.sh` (sha256 `476e18db…`) run with 17162; its one output line | CONFIRMED | My sha256; the task output's first line. |
| RS-14 | R:327 | after the end, no stage or wrapper process was left; the end notice's wording | NOT CHECKABLE | No capture exists. |
| RS-15 | R:329–345 | the copy-back output equals `copyback_out.txt` | CONFIRMED | `S.copyback_out`. |
| RS-16 | R:330 | "G-TIME-OLMo (p)'s copy-back with one change, made after the end: tar extracts with -m" | **IMPRECISE** | Against G-TIME's script (scratch `podwatch/`), the qual copy-back also has the stage's names and filter, takes the address and port from the environment, and uses `awk` for `cut`. Against the earlier qual form (`qualbuild/`), the one change is `-m`, on both extractions. "After the end" is not checkable. |
| RS-17 | R:346 | the wrapper outputs are identical by sha256 | CONFIRMED | `H2.*`. |
| RS-18 | R:348–487 | the five scripts equal their files (scrubbed), and their header sha256s are right | CONFIRMED | `S.script-*`, `S.hdr-*`. |
| RS-19 | R:25–488 | every line after the header is a capture line or a `#` comment | CONFIRMED | `S.no-unexplained-lines`. |

### T (the task_correct raw), and all four texts

| id | text:line | claim | grade | evidence / command |
|---|---|---|---|---|
| T-01 | T:1 | rule 23; the seat's 2026-11-09 §3; the licence (qual-wiring §4, the PI's B4); Code's own step, A-m2 v0.3 §3.4's form; no bar, verdict sentence or label | CONFIRMED | As B-51. |
| T-02 | T:2 | scratch, model-free, stdlib only; sha256 `9aa0e2d9…`; verbatim below | CONFIRMED | My sha256; its imports are `hashlib`, `json`, `sys` and `pathlib`. |
| T-03 | T:2 | reads the sham records only; prints k of n, the key table, the match rule and digests | CONFIRMED | The code. It also prints Code's reading, record counts and the alternative-reading line; T does not exclude these. |
| T-04 | T:3 | the run commands; the `time` check gives the seat's row; re-run with the same counts | CONFIRMED | My re-run equals both captures. |
| T-05 | T:3 | "run before the qual run" | NOT CHECKABLE | Ordering only. |
| T-06 | T:5–26 | the stdout sections equal the captures | CONFIRMED | `ST.*`. |
| T-07 | T:28–235 | the script section equals `task_correct.py` | CONFIRMED | `ST.script`, `ST.script-is-tail`; the script holds no local root. |
| X-01 | E, B, R, T | none of them gives an end time or a stage total | CONFIRMED | The `TM.*` scans; see O1. |

## IMPRECISE and FAIL, with suggested fixes

1. **FAIL, B-27 (B:45).** `cad7da75…2ce77` should be `cad7da75…a3ce77`. The full sha256 is `cad7da75e077c66336743fec2fd9ff4d502a47bb9ac63d806cc29a39a5a3ce77`.
2. **IMPRECISE, E-24 (E:20) and B-12 (B:23).** "The stampless form" / "the stampless wrapper" contradicts the next sentence (one launch stamp). Suggest "the one-launch-stamp form the seat adopted (no end, done or later launch stamp)".
3. **IMPRECISE, E-31b (E:29).** The "p's sham counters: all 0" cell, sft row. Suggest renaming the column "p's other sham counters" or adding "(cap_hits apart)", because p's own sham-counters line carries `cap_hits 1` on sft.
4. **IMPRECISE, E-37 (E:37).** Suggest: "The contrast seconds and every count over a contrast free round are withheld (m:318; ruling (h)). The contrast forced rounds' other counts (all 0) and the first-read flags are in the block's §3."
5. **IMPRECISE, B-25 (B:42).** Suggest "the seat's answers of 2026-11-10 on the qual wiring, §7". Four seat answers of that date have a §7; this one names the seat's read of G-F0m-OLMo (p).
6. **IMPRECISE, B-40 (B:78).** Suggest: "p's other sham counters, control_chars, harness_first_line and refusals over every sham round and corrupted_spelling over the forced rounds, are each 0."
7. **IMPRECISE, B-62 (B:139–140).** Suggest: "It prints k of n per checkpoint and phase, the key table, the match rule and Code's reading, the files' digests and record counts, and whether the alternative reading changes a count: never a response, an item, a session or a pick."
8. **IMPRECISE, B-67 (B:154).** Suggest adding: "beside them, the container's PID-1 start (R:2, the pre-flight's `pid1_start` line, R:296), a pre-run identity record as at G-TIME-OLMo (p)". Optionally also name the non-stamp time fields of O1.
9. **IMPRECISE, B-80 (B:173–174).** Suggest putting G-PWR in Q3's chain: "the seat's read → G-PWR (the PI's cap share) → … → LOCK-p v1.0". m:302, PROPOSAL-p §8 step 6 and the seat's 2026-11-09 §0 all have it, and the qual-wiring §2 ties the campaign's looks and cap share to it. Where the campaign's wiring falls relative to G-PWR is the seat's call.
10. **IMPRECISE, R-15 (R:24).** Suggest adding to the list: "and, after the copy-back, the five scripts those steps ran, verbatim but for the scrub".
11. **IMPRECISE, RS-16 (R:330).** Suggest "the qual form of G-TIME-OLMo (p)'s copy-back (the stage's names, the address and port from the environment), with one change made after the end: both tar extractions take -m".

## NOT CHECKABLE (15), and why

- **Conduct (4):** E-30b, B-36, B-70 and B-72. For B-72, the command lines of the two other PIDs were not captured.
- **Session messages with no capture (3):** E-28 and B-15 (the end notice), and B-77 (the laptop `pgrep`).
- **State this check cannot see (2):** E-09 (stopped for the seat) and E-49 (the pod up and idle; that needs the network).
- **Ordering, which would need times (4):** B-75, RS-11, T-05, and RS-14 (the post-end process check, which also has no capture).
- **Future commits (2):** E-46 and E-50.

## Observations (not graded)

**O1. Time-bearing content.** Reported as present or absent only.
- In R, present:
  - one launch stamp (R:27);
  - three PROVENANCE start stamps (R:53, R:118, R:179);
  - the container's PID-1 start, three times (R:2, R:265, R:296);
  - the pre-launch `ps` listing's ELAPSED column (R:289–293);
  - the weight loader's progress-bar elapsed/remaining counters inside each run's stdout (R:39–51, R:99–116, R:164–177). These are load durations, verbatim, of the same kind as in G-TIME's raw.
- In R, absent: any end, done or later-launch stamp, and any stage total.
- In E: one stamp (E:8, the PID-1 start) besides the placeholder. In B and T: none.
- As B (a) discloses, consecutive PROVENANCE start stamps bound each earlier run. Nothing was computed from any of them here.

**O2. The seat's binding instruction.** The seat's 2026-11-09 §3 and the qual-wiring §4 say the first entry reporting `task_correct` "declares them verbatim and binds the roster file's sha256". E points to B §4 and T and carries the sha256 abbreviated. Whether the entry itself must carry the table, the rule and the full sha256 is for the author or the seat.

**O3. Outside T's header.**
- T's script docstring attributes the licence quotation to "…§4, and the PI's routing of 2026-11-10, B4:". The quoted words are the seat's §4, verbatim; B4's line in RESULTS.md:1351 reads differently.
- The printed output also goes beyond the licence's "… beside, nothing else", as in item 7 above.

**O4. Not one of the four texts.** `assemble_qual.py`'s docstring says it "Reads no file under data/*/ckpt", but its line 55 hashes all fifteen outputs. That is a digest under the list's item 1, but the wording could say "hashes only".

**O5. Fraction format.** B's first-pick shares 10/16 and 8/16 are k/n. m's report prints them in lowest terms.

## Departures and disclosures of this check

**D1. Two command lines carried the word "olmo"; both were sub-second, names-only git calls, permitted forms under item 1.**
- A `git ls-files` call with the pathspecs `data/olmo/a1_repair_roster.json` and `data/olmo/manifest.json`.
- A `git --no-optional-locks status --porcelain` call whose pathspec included `LOCK-p-OLMo-sft.md`.
- Neither ran Python or a model, and neither read anything under `data/*/ckpt` or `data/*/reports`. Every other command kept such names inside script files or behind globs.

**D2. The G-TIME pod address and port appeared in my tool output.** A `diff` of the G-TIME copy-back script in scratch (`podwatch/copyback_gtime.sh`) printed that script's literal address and SSH port. They are not reproduced here or in any file I wrote. The scrub check reads them only inside `vc_main.py` and prints booleans.

**D3. Masked report copies, now deleted.** I wrote masked working copies of the six m and p report JSONs under `vc/masked/` for reading, then deleted them.

**D4. Dry-test stamps.** The dry-test re-run wrote this check's own launch stamps under `vc/dry/`. They were printed masked; they are not the stage's.

**D5. What was read in the reads files.**
- Of the sham records: blinding, rounds (phase, keys, `cap_hit`, `ri`/`ci`), transcripts (only to see that `[config]` is present), seconds (summed and compared for equality only), the verified/complete/excluded flags, template and `s`.
- Of the contrast records: the `contrast` flag only.
