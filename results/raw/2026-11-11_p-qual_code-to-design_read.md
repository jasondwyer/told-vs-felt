# G-F0m-OLMo (p) ×3: the seat's read, and Code's readings for the seat's word (Code → design)

*Code's raw, PI date 2026-11-11. Code STOPS here for the seat's read, as the PI's routing of 2026-11-11 has it: the
seat's answers of 2026-11-10 on G-ID-F3, §9 item 9, "The box run under the standing locks: sync → precheck ×3 →
G-F0m-OLMo (p) ×3 batched → STOP for the seat's read [go; the pod up through it — your call]". Nothing follows until
the seat answers and the PI routes. Nothing is pushed. This block computes no wall clock, and it gives no end time and no
stage total (the same answers, §6).*

## 1. What ran

- **The chain since G-TIME-OLMo (p)**, on the PI's routings of 2026-11-10 and 2026-11-11 (relayed by the coordinating
  session):
  - the qual wiring's BUILD, `40086e8`;
  - G-SHAPE-p's re-run, `f5e695c`, and G-ANL-p's, `ba89279`;
  - LOCK-p-OLMo-{sft,dpo,instruct} v0.2, `585df45`, standing as committed (the seat's answers of 2026-11-10 on G-ID-F3,
    §6, committed at `a6c6297`);
  - the record commit, `eb3e08c`.
- **G-F0m-OLMo (p) ×3 on the box.**
  - Pod `qny1x4v8padeke`, backend identifier `641ee466f4553b6a`, box repo at `eb3e08c`, synced by bundle with
    G-TIME-OLMo (p)'s 15 untracked outputs set aside by digest.
  - The precheck at `qual` was CLEAR ×3 before the launch, and (j)'s fresh closure (14 files) equalled G-SHAPE-p's
    record.
  - The three ran back to back through the wrapper in the one-launch-stamp form the seat adopted (§6). It writes the
    batch's one launch stamp and each run's exit code (0, 0 and 0), and no end, done or later launch stamp. Each was one
    run, with no `--resume`.
  - The end-wait was on the wrapper's PID alone. The end notice carried "batch ended" and the exit statuses.
  - Raw: [`_p-qual`](2026-11-11_p-qual.txt).
- **Each checkpoint: PASS, path uncached.**
  - 24 sessions, as planned and recorded: 8 A0-OLMo-{ckpt} (contrast) and 16 A0s-OLMo-{ckpt} (sham).
  - `round_degeneracy@G-F0m-OLMo-{ckpt}` is silent at 0/160, critical 7 at n = 160, p0 0.02.
  - No hair trigger fired: none in either arm of m's stage report, and p's `line_break_in_stored_text` is 0 over every
    round of every session.
  - Register entries (1), (2) and (6)–(9) were entered in that order.
  - Each m stage report's identity carries:
    - its lock's sha256 (sft `3765fe22…`, dpo `b739081f…`, instruct `48e1c315…`);
    - the backend identifier `641ee466f4553b6a`;
    - m's package `7756dcf4…` and PROPOSAL-m v1.11's sha256 `42ab36ec…`;
    - path `uncached`.
  - Term (d) at the stage's end, before restoration, is recorded as `single_threaded: false`, with threads `MainThread`
    and `tqdm_monitor`, as at G-TIME-OLMo (p): recorded, never raised.
  - p's call log: one run, well formed, no malformed line, no stale reservation.

## 2. What the seat reads (m:271's pre-VERDICTS read rule; m:302; the seat's answers of 2026-11-10 on the qual wiring, §7)

- **The reads, one file per checkpoint** (m's `readrule`, written by m's stage):
  - [`OLMo-sft_qual_reads.json`](../../data/p/reports/OLMo-sft_qual_reads.json) `cad7da75…a3ce77`;
  - [`OLMo-dpo_qual_reads.json`](../../data/p/reports/OLMo-dpo_qual_reads.json) `92c1cc85…c9db4f`;
  - [`OLMo-instruct_qual_reads.json`](../../data/p/reports/OLMo-instruct_qual_reads.json) `afbcfb35…d172d0`.
- **What each holds:** the eight contrast sessions as `strip_contrast` leaves them (their free rounds absent), and the
  sixteen sham sessions as `redact_sham` leaves them (the chosen config tag redacted to `[config]`).
- **Beside them:**
  - m's pick-free stage reports, `data/p/reports/OLMo-{ckpt}_qual_report.json` (sft `172f82c0…`, dpo `efbe402d…`,
    instruct `7c174940…`);
  - p's reports on the read domain, `data/p/reports/OLMo-{ckpt}_qual_p-report.json` (sft `3f91b661…`, dpo `9b1eb458…`,
    instruct `57c7e5e3…`). Each binds m's two files by their sha256s, which Code checked equal to the files. Each
    carries `proposal_p_sha256` `42f2977b…` and p's package `08bfa693…`. On sft it also carries the declared SFT
    sentence.
- **Not read before VERDICTS:**
  - the checkpoints `data/p/ckpt/OLMo-{ckpt}_qual.json`, which are -diff and may hold contrast picks;
  - the call logs `data/p/ckpt/OLMo-{ckpt}_qual_p-calls.jsonl`, which are withheld.

  Code opened neither. Code's reads were m's and p's reports, for the figures below, and the reads files' sham records,
  for `task_correct` (§4). Code read no contrast record.

## 3. The read domain, per checkpoint (the reports; the checkpoints unopened)

**The sham sessions** (16 per checkpoint, 10 rounds each), from m's stage report and p's report:

| | rounds (forced, free) | bar | valid / complete | exclusions, claims | cap hits | p's other sham counters | proxy | first picks of P | reads: top-1 not a label | sham seconds |
|---|---|---|---|---|---|---|---|---|---|---|
| sft | 160 (64, 96) | 0/160 | 16 / 16 | 0, 0 | 1: `A0s-OLMo-sft s=6 forced 0` | all 0 | 160 of 160, 0 cuts | 9 of 16 (9/16) | 12 of 96 | 102.105 |
| dpo | 160 (64, 96) | 0/160 | 16 / 16 | 0, 0 | 0 | all 0 | 160 of 160, 0 cuts | 10 of 16 (5/8) | 3 of 96 | 88.389 |
| instruct | 160 (64, 96) | 0/160 | 16 / 16 | 0, 0 | 0 | all 0 | 160 of 160, 0 cuts | 8 of 16 (1/2) | 8 of 96 | 85.237 |

- No exclusion, strict or tolerant, and no claim (audit, echo or lexical). No advisory round, degeneracy or
  termination.
- **The one cap hit** is sft's sham session s=6, at its first forced round. It is in m's forced-round `cap_hit` and in
  p's `cap_hits` key.
- **p's other sham counters** are each 0: `control_chars`, `harness_first_line` and `refusals` over every sham round,
  and `corrupted_spelling` over the forced rounds. p's fifth sham counter is `cap_hits`, the column before. The
  corrupted-spelling counter over the free rounds is withheld, because it reads the round's item, which names the pick.
- **The reads column** is m:283's "reported, no bar" flags over the sham sessions' reads (n = 96 at each checkpoint):
  low label mass 0 at every checkpoint, and top-1 not a label as shown.
- **The first picks of P** are m's report's `first_pick_P` (k of n, its share in lowest terms beside), by pair:
  - sft 1/2, 1, 1/2 and 1/4;
  - dpo 1/2, 3/4, 1/2 and 3/4;
  - instruct 1/2 at each.
- **The sham seconds** are m's report's sum over the sixteen sham sessions. The contrast seconds are withheld (m:318).
  m:205's planning basis stands as LOCK-p v0.2's item 3 has it. The sham seconds are reported beside it, no basis.

**The contrast sessions** (8 per checkpoint), in ruling (h)'s form: the forced rounds generated, the exclusion at them,
p's count of their control characters, and m:283's flags over the first read of each domain session:

| | sessions | forced rounds generated | excluded at a forced round | forced rounds' control characters | first reads (low label mass; top-1 not a label) |
|---|---|---|---|---|---|
| sft | 8 | 29 | 1 (`lexical@forced`) | 0 of 29 | 7 reads (0; 1) |
| dpo | 8 | 32 | 0 | 0 of 32 | 8 reads (0; 1) |
| instruct | 8 | 32 | 0 | 0 of 32 | 8 reads (0; 0) |

- **sft's contrast session s=4 was excluded at a forced round by the lexical rule.** The stdout line is
  `qual A0-OLMo-sft s=4 excluded:lexical@forced`. m's stage report gives `excluded_at_forced` `lexical@forced` 1 and a
  forced-round lexical claim of 1, with 29 forced rounds over the eight sessions and 7 domain sessions.
  - The stage PASSes: its bar reads the sham sessions.
  - Its record is in the reads for the seat. Code did not open it.
- In the contrast forced rounds there was no cap hit, advisory round, degeneracy or termination, and no audit or echo
  claim.
- Every other count over the contrast sessions is withheld to VERDICTS (p's report's `withheld` line; m's `free_rounds`
  line).

## 4. `task_correct` (rule 23; the seat's answers of 2026-11-09 on G-TIME-OLMo (p), §3): first reported here

Code's own step tabulates the counter (A-m2 v0.3 §3.4's form), not p's package or the analyzer. It reads the reads
files' sham records only, under the licence of the seat's answers of 2026-11-10, §4 (the PI's B4). It enters no bar, no
verdict sentence and no label.

- **The key table, declared verbatim** (the seat's §3: "the roster's sixteen items with one key each"):
  `3`, `24`, `44`, `12`, `down`, `77`, `64`, `cold`, `7`, `45`, `2`, `closed`, `28`, `march`, `january`, `iron`.
  Each key is the first gold of exactly one item of `data/f/pools.json`'s `CORR_clean`, so the sixteen items each carry
  one key.
- **Bound by the file's sha256:** `data/f/pools.json`,
  `8547d9a11ba55b95dda2988d4e9bdc685196abcda55870d7713703df372d17a0`.
- **The match rule, declared verbatim** (the seat's §3): "a response is correct iff its whitespace- and
  punctuation-normalized, case-folded text contains the item's declared key as a whole token (word-boundary match, so
  `12` does not satisfy the key `2`), with number words `one` … `twelve` mapped to digits before the match".
- **The rows** (k of n, sham rounds):

  | | forced | free | all |
  |---|---|---|---|
  | sft | 63 of 64 | 96 of 96 | 159 of 160 |
  | dpo | 63 of 64 | 96 of 96 | 159 of 160 |
  | instruct | 64 of 64 | 96 of 96 | 160 of 160 |

  Beside them is G-TIME-OLMo (p)'s row, the seat's own: sham 29 of 30 (sft 9 of 10, dpo 10 of 10, instruct 10 of 10).
- **How it was computed:** by a scratch script, verbatim with its sha256 in
  [`_p-qual_task-correct`](2026-11-11_p-qual_task-correct.txt), with a self-test of 19/19.
  - Each round's item is taken from its own round piece's `Task:` line, matched by equality to exactly one `CORR_clean`
    task. The free rounds' item field is withheld by m's read rule.
  - A forced round's `item` and `task_text` must agree with that line.
  - A contrast record is skipped by its flag, and nothing of it is accessed.
  - It prints k of n per checkpoint and phase, the key table, the match rule and Code's reading of it, the files'
    digests and record counts, and whether the alternative reading changes a count. It never prints a response, an
    item, a session or a pick, so which rounds missed is not printed here.
  - On G-TIME-OLMo (p)'s committed reads files it gives the seat's 29 of 30.
- **Code's readings, for the seat's word** (each in force until ruled):
  - (t1) **"The roster file"** is read as `data/f/pools.json` (`CORR_clean`), the file whose sixteen items carry the
    keys. m's own "roster" is the label roster: on OLMo `data/olmo/a1_repair_roster.json`, with its four selected
    entries. m's pick-free artifacts are asserted free of its labels, and it carries no task item and no key.
  - (t2) **"Punctuation-normalized"** is read as every character that is neither a letter nor a digit becoming a space,
    the tokens then compared whole. Deleting the punctuation instead changes no count, here or at G-TIME.
  - (t3) **The key table credits one gold per item.** It does not credit `twenty-four` (item 13: the number words stop
    at `twelve`) or `shut` (item 15). Code's step does not print which rounds missed, so whether either uncredited
    gold is among the two misses is not known here.
  - (t4) **The output's scope.** The licence reads "printed as k of n per checkpoint and phase, the key table and the
    match rule beside, nothing else". The step also prints Code's reading of the rule, the reads files' digests, the
    record counts per arm and whether the alternative reading changes a count. Code reads these as declarations,
    item-1 digests and counts the reports already carry, but they are beyond the licence's list. They are disclosed
    here for the seat's word. The script's docstring also cites the licence as the seat's §4 "and the PI's routing of
    2026-11-10, B4". The quoted words are the seat's §4; B4's own line reads differently.

## 5. Code's readings and observations (for the seat; each in force until ruled)

- **(a) The stamp form.** The raw's stamps are the wrapper's one launch stamp and m's PROVENANCE start stamps, which
  are in each run's stdout and report as the stage writes them. The seat's §6 has the latter "remain as the
  unavoidable records".
  - In a batch, a later run's start stamp follows the earlier run's end.
  - The raw also carries records that are not the run's own stamps:
    - the container's PID-1 start, the pre-run identity record as at G-TIME-OLMo (p) (in the header, the pre-flight's
      `pid1_start` line and a comment);
    - the pre-launch process listing's elapsed column;
    - inside each run's stdout, the weight loader's progress-bar counters, which are load durations, as in G-TIME-OLMo
      (p)'s raw.
  - Code computed nothing from any of them, and this block and the entry give no end time and no stage total.
- **(b) The launch's process pattern matched three PIDs.** The remote shell and its command substitution carry the
  script's name in their command text. A by-PID listing, arguments only and no times, identified the wrapper. Both are
  in the raw.
- **(c) The copy-back extracted without restoring modification times** (`tar -m` on both extractions), so the laptop
  copies carry no box write time.
  - Its script is the qual form of G-TIME-OLMo (p)'s copy-back (the stage's names, and the address and port from the
    environment), drafted with the wiring.
  - The `-m` is its one change, made after the end.
  - Every file was compared by sha256 at both ends, and all were identical.
- **(d) The laptop.**
  - `pgrep -ifl 'python|mlx|jlens|qwen|olmo|ipykernel'` found nothing at the launch, and no laptop model run was
    announced while the batch ran (the coordinating session's serialization).
  - **Another session's commands during the batch**, for the seat to judge: the F3 session's LOCK-m-F3 v0.2
    values-checker ran a bare `git status --porcelain` twice on the laptop, by its account while G-F0m-OLMo (p) ×3
    ran on the box. At its start the run printed names, none under `data/`; at its end it printed a count.
    - It is disclosed at `05ef75d`, in `results/raw/2026-11-11_lock-m-f3-v02_valuescheck.md`, the checker's
      disclosures, item (5).
    - Whether the count at its end included this stage's copied-back outputs is not worked out here, from times or
      otherwise.

## 6. Questions for the seat

- **Q1. The read.** On the seat's read of the three reads files, do G-F0m-OLMo (p)'s three PASSes stand (m:302)? This
  includes sft's contrast session s=4, excluded at a forced round under the stage's own lexical rule.
- **Q2. `task_correct`.** Readings (t1)–(t3), for the seat's word.
- **Q3. Next.** p's chain after the qualification, in the seat's order. PROPOSAL-p v0.2 §8 step 6 has "G-F0m-OLMo (24;
  the seat's read) → G-PWR", and the seat's answers of 2026-11-09 on G-TIME-OLMo (p), §6, have "then G-PWR's figures
  and LOCK-p v1.0 ×3".
  - Next is G-PWR (p): the PI's cap share, per checkpoint.
  - Then the campaign's wiring, its own move before LOCK-p v1.0 (B2 of 2026-11-10), and v1.0's contents.
  - Where the wiring falls relative to G-PWR is the seat's to set.
  - The pod's uptime goes back to the PI after this STOP (§9 item 9).
