# n — G-TIME-n's specification as the texts state it, Code's readings GT1–GT17, and the coordinating session's routing of them

PI date 2026-11-21. Code (the n-build session).

**What this raw holds.** It serves the seat's read of the seven starred readings (the block committed beside it) and
G-TIME-n's BUILD:
- **§1, Code's readings GT1–GT17 as sent, verbatim** (`f3fa5f05…f42f`, 153 lines). They went as a note in the
  sessions' shared notes folder, outside the repository; the note is byte for byte Code's scratch copy. It is in no
  other repository file.
- **§2, the coordinating session's message routing them, with the PI's answer, verbatim** (`64323d4b…50fe`, 18
  lines). It is in no other repository file.
- **§3, the survey's brief** (`af5357e7…4aab`, 77 lines). One change: the repository's full path, on its second line,
  is written `<repo>` (`2060f18e…c1e8`).
- **§4, the survey's report, verbatim** (`a23831e4…05e7`, 245 lines). A subagent compiled it read-only at HEAD
  `deabf3f`: the specification of G-TIME-n as the texts state it, with a citation for its claims, and the questions the
  texts leave open. It was extracted from the subagent's hand-back by `jq` when it returned, on 2026-11-20. Its
  departures are in its last section, for the seat to class.

**The cited lines.** Every file:line in §1–§4 is the repository's at `deabf3f`. Since then only `RESULTS.md` has
changed among the cited files, and its lines have moved (HEAD `c9d35e2`). `c9d35e2` inserted 257 lines in five places
(`git diff -U0 deabf3f c9d35e2 -- RESULTS.md`), so an R: anchor moves by where it falls: lines 24–283 by +204, 284–460
by +223, 461–739 by +234, 740–869 by +249, and 870 on by +257 (R:5664–5665 at `deabf3f` is R:5921–5922 at `c9d35e2`).

**How §2 was taken.** It was extracted from this session's transcript by `jq`, a departure declared in the entry that
commits this raw. It is the message's own 18 lines, without the delivery wrapper, which names a session by its id.

**What it does not name.** None of the four sections names a path in the home folder or the scratch folder's full
path, once §3's one line is written as above. §1 names its one scratch file as S/...; §3 and §4 name none.

## 1. Code's readings GT1–GT17, as sent

```text
# G-TIME-n (n v0.2 §8 step 11): Code's PINs GT1–GT17, for routing

Code, PI date 2026-11-20. These are built on the read-only spec survey of HEAD `deabf3f` (`S/step4b/gtime/spec_report.md`,
`a23831e4…05e7`, 245 lines; its 17 open questions are answered below, Q-number in brackets) and Code's own checks of
the cited lines. ★ = the seat's before any run (not before the build). Every other PIN is Code's, as at G-CAL-n's
GC1–GC22. No code is written before these come back routed.

## The stage

- **GT1 ★ The read set: 18 reads, three on each of six sessions [Q1].**
  - **The sessions:** runs 0, 32, 64, 95, 127 and 159. These are round(k·159/5) for k = 0..5, evenly spaced over the
    session set's order, two floor and four neutral. They are chosen without a key, because v0.1 names no G-TIME-n
    key and a key is a lock item (n:117; L:397–404).
  - **Why length doesn't matter here:** seq_len barely varies (144 of the 160 at 1273 tokens, the rest 1266–1272).
    The six are at 1273 ×5 and 1268 ×1.
  - **The reads, per session:**
    - (a) the shadow, N1-V `none` d = 0, with a re-computation (reason `dose-rule`, identity block);
    - (b) N1-V `valence` +1, with a re-computation (`dose-rule`);
    - (c) N1-V `valence` +1/2, without one (the cached path alone).

    The schema admits all three at "time" (schema:1042–1050, :1071–1082).
  - **The kinds** (n:118) are attributes of reads, not separate reads:
    - shadow: (a), 6;
    - steered: (b) and (c), 12, of them 6 cached-only;
    - fidelity re-compute: (a) and (b), 12, each with `duration_ms_fresh`;
    - capture-on: all 18 (schema:89: "every read captures").

    So each kind has at least six reads.
  - **Code's reading, for the seat:** a read's cost does not depend on its arm or direction. N1-P's twelve spans,
    N2's span doses, N1-R's random rows and N4's told lines run the same forwards and the same additive hook. So
    N1-V's cells stand for the campaign's.
- **GT2 The launch order.** The six shadows first, then the six +1 reads, then the six +1/2 reads, launch indices
  0..17. This is the runner's ORDER: shadows first, then arm-major (runner:18–22). A steered read needs its shadow on
  disk (primitive:213–217).
- **GT3 Built in the driver alone [Q7].**
  - The time plan, the stage command (`gtime`) and the projection live in `scripts/n_sessions.py`, as the BACKEND
    extension's plan does (drv:551–555). The runner's generic `run` takes the plan (runner:376). `campaign_order` is
    not used: it asserts the campaign's plan (runner:161–163).
  - `valence_core/n/` does not change. So the stage identity's `package_sha256` and `imported_sha256`, both identity
    fields (schema's STAGE_IDENTITY_FIELDS), are LOCK-n v0.1 §18's: `06b55761…1d39` and its twelve files. G-TIME-n
    runs under v0.1 with the package v0.1 pins.
- **GT4 ★ The identity at "time" [Q7].**
  - stage `time`; `lock_sha256` `88d9fe7b…e9d5`; the dose map of record (`d4a73b54…efb3`);
  - `fidelity_rule` from the lock: TAU, p0 1/26, cadence 160, alpha 0.01, C 0.25, median rel
    0.0013026706058596332, the key `n-fid|{s}`, `sample_rule` the lock's words (L:406–410); `identity_bound` = C;
  - `directions` {`valence`: its sha16}, the only direction G-TIME-n injects;
  - `read_window` 4,096; the weights, the backend identifier, the pod id, the rendering and the label convention as
    the lock has them;
  - **no cap**: `hour_cap_ms` None. The lock's cap row is the campaign's (L:554), and the cap is what G-TIME-n
    projects (backend-ext's R5, drv:95).
- **GT5 Monitors and a pause [Q10].** Every monitor binds as the runner has it:
  - rendering; nonfinite;
  - the ceiling (R14, ans19:50: a re-computation above C pauses G-TIME-n);
  - the identity bound on the six shadows (an `also_fired` entry, sfr:207);
  - the binomial, evaluated once at the stage's tail (18 reads < 160, runner:51–54), its trials the 12 re-computed
    reads. By Code's arithmetic it fires at 3 or more above TAU (upper tail 0.0096 at p0 1/26), and the runner's own
    test decides.

  A fire ends the invocation (exit 3, PAUSE) for the seat. A ruling precedes any use of the projections.
- **GT6 No pass rule; the exits [Q2].** G-TIME-n is a measurement. n:118 states no bar, and the report's end states
  hold no PASS (schema:1131). The exits:
  - 0 COMPLETE, projection written;
  - 3 PAUSE;
  - 2 G-VER-STOP or a refusal before any read;
  - 1 anything else.

  A G-VER-STOP is G-TIME-n's "STOPPED" (n_analyze's `clock:gate-stopped`). The BACKEND extension returns 1 on a
  G-VER STOP (drv:1133–1135); G-TIME-n takes 2, gvec's and gcal's code for a STOP (drv:150–152, :173–176).
- **GT7 G-VER before the load, not of record [Q6].** As at the BACKEND extension (drv:1130–1135): G-VER on the
  committed ids, the tokenizer alone loaded, before the weights. Its STOP is a STOP for the seat (L:543's sentence):
  exit 2, no read launched, no report. G-VER of record is step 12's own stage (n:159).

## The projection

- **GT8 ★ The cap's basis: model time [Q3].**
  - **The inputs:** G-TIME-n's own records, read by the stage's own code after COMPLETE (the backend-ext route,
    drv:1157–1160). Per read, the cached share is c = `duration_ms` − `duration_ms_fresh` (or `duration_ms` with no
    re-computation) and the fresh share is f = `duration_ms_fresh`. The read's clock covers both paths and the
    captures' copies (primitive:205–207, :237–241, :283–284).
  - **The projection:** T = N·median(c) + K·median(f), with:
    - N = 7,680, the campaign's reads (schema.read_plan);
    - K = 3,637, its re-computations: 3,040 dose-rule plus 597 keyed sample, runner.py:147's rule over the plan,
      computed in the stage by the package's functions. Code's shell count from the plan of record gives the same.

    Beside it, T at the maxima (max c over 18, max f over 12), both in ms and hours.
  - **The cap:** the cap counts model time as the runner computes it (L:591–592; ans16b:50), so T is the cap's basis.
    The PI sets the cap in hours at v1.0.
  - **The extension's figures:** its 309.0 and 357.1 ms ("used by nothing", A-n2:40) are printed beside, not used.
- **GT9 ★ Pod hours beside the cap, outside it [Q3, Q4].**
  - (a) **The loads:** G-TIME-n's measured load, per invocation.
  - (b) **The I/O:** per read, the time from one launch to the next minus `duration_ms`, timed by the driver's printer
    hook. Its growth with a cell's size cannot show in six-read cells: each append re-checks the whole cell and
    rewrites its JSON (cells:240–248). So, **Code's PIN, option (i):** a model-free append benchmark on the box's
    volume after the reads.
    - It appends 160 example records to one scratch cell outside the repository (`guard.refuse_test_out`), timing
      each append.
    - It fits a per-append cost a + b·k and sums it over the campaign's cells.
    - The alternatives for the seat: (ii) the measured per-read I/O × 7,680, declared a lower bound; or (iii) not
      projected, left to the 8 h budget's slack.
  - (c) **Not measured by G-TIME-n**, reported as such: the captures' copy-back (≈ 5 GB, A-n1:54), G-VER of record,
    the campaign's resumes.
- **GT10 ★ G-READ-n's fits [Q5].**
  - **Where they run** is Code's call (A-n1:56): the laptop's CPU, after the copy-back. So they are outside the box's
    cap.
  - **Timed at step 11** by a model-free benchmark on the laptop, in a battery window you grant: probe.py's fit at its
    pinned settings (fit_lr seed 7, 300 iterations, rate 0.1, l2 0.01; `cv_seed` and `shuffle_seed` as pinned), on
    synthetic float32 arrays of the band's shape. A declared number of fits are timed and projected to the ≈ 404,000
    fits (ans16b:42).
  - **Reported** beside the projections at v1.0.
  - **The alternative for the seat:** on the box, timed there and counted in the cap.

## Outputs and conduct

- **GT11 The outputs [Q8, Q9].**
  - The root `data/n/ckpt/time/` (closed, item 2) and the report `data/n/reports/time.json` (`n-report-v1`), as at
    backend-ext (drv:503–507).
  - A new projection artifact, `data/n/gtime/gtime.json` (`n-gtime-v1`). It holds: the identity's sha; per read, the
    run, cell, seq_len, c, f and I/O ms (no margin, no log-probability); the load; N and K; the medians and maxima; T
    at both; GT9's terms; the formula's text.
  - The raw stdout, `results/raw/<date>_n-gtime_out.txt`.
  - All of it is committed before the pod stops (rule 27). New `.gitignore` lines admit the report, the cell JSON and
    the artifact. The capture arrays stay on the box, as at backend-ext (.gitignore:283–301), declared.
- **GT12 ★ Exposure [Q11].**
  - G-TIME-n reads no point below d = 0. Its 12 steered reads are at +1 and +1/2 on `valence`.
  - §0.4's table (n:18–28) counts the negative pole's forwards (A1, "struck beyond d = −1").
  - Whether positive-pole timed reads need a line in it is the seat's (ledger (53), n:14).
- **GT13 No DV [Q12].**
  - G-TIME-n's records are stage `time` records in their own root. No campaign read or DV takes them: VERDICTS
    refuses a non-campaign report (R:2996).
  - So n needs no counterpart of m:280's exclusion sentence (Code's reading).
- **GT14 The box and the run.**
  - The setting: the pod of record (`emw1e4embiwe9b`), the characterized backend, the weights of record and the
    pinned environment (transformers 5.15.0). The driver of record is HEAD's committed bytes (a DRIVER line).
  - The refusals are backend-ext's: the pod id; `CUBLAS_WORKSPACE_CONFIG`; numpy's known answer; the root and report
    of a run of record.
  - **One smoke first,** the same 18 reads under a root outside the repository, then the run of record. The smoke's
    figures are beside, not used.
- **GT15 Printing [Q16].**
  - The runner's per-read line ("session index, arm, dose, the fidelity value against TAU, timing — never a margin",
    n:130).
  - The driver's lines: STAGE, WEIGHTS, DRIVER, G-VER, LOAD, the 18 read ids, the projection's figures.
  - Durations are the stage's data and go into committed text. Start and finish stamps do not: Code's reading of
    WORKFLOW.md:28 and :53 for a stage that is not a contrast gate.
- **GT16 ★ Who reads it [Q13, Q15].**
  - The report, the artifact, the raw and the entry are committed. You relay the projections to the PI for the cap
    at v1.0 (ans20b:71).
  - The seat reads the record with v1.0's draft. No STOP for the seat follows a COMPLETE run; a pause is the seat's.
  - The figures stand for the box they ran on. After a box change before the campaign, whether G-TIME-n re-runs is
    the PI's (n:101's "gate stages may span boxes"; ans20:58).
- **GT17 The clock [Q17; Q14].**
  - G-TIME-n, G-VER of record and v1.0 with the seat's read land by D_n 2026-12-15, the day inclusive (L:985).
  - Item N.2's routing words go into your own notes commit (your copy of the paste block), which Code's entries then
    cite.
```

## 2. The coordinating session's routing, with the PI's answer

```text
The PI's answer on the G-TIME-n PINs is "Build on the PINs": go ahead with your step 3 on GT1–GT17.

That is verbatim, received 2026-11-21 in this session's chat. It answers my question to the PI, which was: "Build G-TIME-n on n-build's PINs now, with the starred seven to the seat before the run?" The two answers offered were "Build on the PINs" and "Seat first", and the PI chose the first.

What it routes:
- **The build.** Build on GT1–GT17 as PINs now, as your note has them (2026-11-20_n-build_gtime-pins.md, f3fa5f05…f42f, 153 lines; I re-hashed it equal just now).
  - Your step 3 is as routed on 2026-11-20: drafts in scratch, self-tests in battery windows I grant, one blind review, one values-check, then the BUILD's commit window.
  - Driver only, per GT3: valence_core/n/ stays at 06b55761…1d39.
- **The seat.** The seven starred PINs (GT1, GT4, GT8, GT9, GT10, GT12, GT16) go to the seat before any run, not before the build.
  - Same order as G-CAL-n, where 99196e1 went in before 89a55c3: a seat block in results/raw, committed by path in a commit window I grant, ahead of the BUILD's commit. Its form is your call, as at 99196e1.
  - It needs no further word from the PI. The PI's word governs only the nudge to the seat.
- **Unchanged.**
  - Laptop Python runs only in battery windows I grant, one at a time. Ask with the scripts' sha256s; I read them whole and check pgrep before each grant.
  - The launch files come to me first, and nothing goes to the box before my relay.
  - Nothing is pushed.
- **Still owed in your next entry:** the survey's report and brief, your two departures and the survey's own, and the survey agent's id in the gate's list.

pgrep shows 8051 only (python3.12) as of my check just now.
```

## 3. The survey's brief

```text
You compile, read-only, the full specification of one stage of the jspace-lab repository (at
<repo>, HEAD deabf3f), so that Code can build it: **G-TIME-n**, step 11 of
PROPOSAL-n v0.2's §8 order. It is the box stage that times the campaign's reads under LOCK-n v0.1 (committed at
deabf3f as LOCK-n.md) so that the PI can set the campaign's cap in hours at LOCK-n v1.0. Its stage command is not
built: scripts/n_sessions.py says "Stages G-TIME-n, G-VER, the campaign and G-READ-n are wired at their own steps".
You run no interpreter of any kind (no python, python3, node, perl), write no file anywhere, and return your report
as your final message.

WHAT TO FIND, with a file:line citation for every claim:
1. The specification as the texts state it:
   - PROPOSAL-n-bk-reconciliation-v0_2.md: the G-TIME-n paragraph (about line 118), §2.7's hours and pod budget
     (about line 101), LOCK-n v1.0's contents (about line 120), the pause and monitoring paragraphs (about line 148),
     §8's steps 10–14 (about lines 159–161), and anything else that names G-TIME-n, timing, projections, the cap,
     hours, the pod budget, the shadow, the fidelity re-computation or captures;
   - LOCK-n.md (v0.1, committed): §6 (the arms and read sets), §10 (every trigger: which bind at G-TIME-n), §11 (the
     pod budget's split and the cap clause), §13 (alpha, the tile and E), §16 (G-TIME-n's figures), §17 (the backends
     and the weights), §21 (the runner's PINs, R14), §24;
   - ADDENDUM-n1, ADDENDUM-n2 (the fresh pair's cost, "recorded for G-TIME-n", about line 40) and ADDENDUM-n3 (OPEN 3,
     about line 60), each at the repository root;
   - every item in the seat's answers raws and the PI's routing raws under results/raw/ dated 2026-11-15 to
     2026-11-20 whose names hold "n-", "box", "sitting" or "routing" that bears on G-TIME-n (R14, the ceiling at
     G-TIME-n; the cap in hours; the reads' I/O outside the cap; what G-TIME-n records and commits; its identity's
     lock_sha256 and C; its pass or fail, if any; who reads its output and when);
   - RESULTS.md's entries that bear on it (the n package's BUILD entry and its flags: the reads' I/O, `cache.crop`,
     the cap; the BACKEND extension's timing figures; the box's GPU and pod budget).
2. What already exists in the code that G-TIME-n could use or must match:
   - valence_core/n/schema.py: the stage "time" (STAGES), the stage identity's fields and their null rules at "time"
     (`check_stage_identity`), the record's timing fields (`duration_ms`, `duration_ms_fresh`, loads), the fidelity
     reason "timing", the stage report (`check_report`), the cap fields, and the self-test's time-stage examples;
   - valence_core/n/runner.py: `run`, `StageInputs`, `PlannedRead`, `Monitors` and which monitors bind at "time", the
     PAUSE, SCOPE, CAP and ceiling clauses, and `campaign_order` as the only plan builder;
   - valence_core/n/primitive.py: the read (the cached and fresh paths, the shadow, captures) and what it times;
   - scripts/n_sessions.py: the BACKEND extension's commands (backend-ext, backend-ext-2) as the nearest template:
     refusals, the weights of record, the driver of record, the ids, the provenance bridge (R6), G-VER before the
     load, the load, the stage identity, the runner's call, the report, the printing rules, the exit codes;
   - prior timing stages as templates: p's G-TIME-OLMo (valence_core/p/ and scripts/p_sessions.py) and m's
     G-TIME-F3 or G-TIME-F0 (valence_core/m/ and scripts/m_sessions.py): which reads each timed, how many, how each
     projected hours, what it recorded and committed, its pass rule if any, and the entries that record their runs
     (G-TIME-OLMo (p) PASS ×3, 2026-11-09; G-TIME-F3, 2026-11-07).
3. What the texts leave open for a build: every point Code would have to decide that no text decides, stated as a
   question with the texts that come nearest. Do not decide them. At least: which reads make "six reads of each kind
   (steered, shadow, fidelity re-compute, capture-on)" (arms, directions, dose points, sessions, and whether the kinds
   are separate reads or parts of one read); whether G-TIME-n has a pass rule or is a measurement; the projection's
   formula to campaign hours (the 7,680 reads, their shadows, the dose-rule and keyed-sample re-computations, the
   loads, the I/O); what the stage writes and where (records, report, a projection artifact) and what is committed;
   the identity's fields at "time" (the dose map, the cap, alpha, C, the read window); which monitors bind and what a
   pause at G-TIME-n means; its exit codes.
4. Anything that would make G-TIME-n need the seat or the PI before it runs (a missing input, a conflict between texts,
   a reading that must precede the run).

REPORT FORM: numbered sections 1–4 as above; in each, short items, each with its citation(s). Quote exact words where
a number, a bar, a STOP, a formula or a name is at stake. End with "OPEN QUESTIONS" (from 3 and 4), numbered. Write a
scratch file, if you must name one, as S/...; a repository file by its repository path; never a full local path.

RULES FOR EVERY COMMAND YOU RUN (binding; a breach is reported in a final DEPARTURES section, "none" if none):
- No interpreter of any kind, no write of any file, no network, no model or adapter code run.
- No argv may contain any of these five guard markers, in any case: mlx, jlens, qwen, olmo, ipykernel. Paths count,
  and so do file names under results/raw/ and at the root (p's lock files and drafts hold one in mixed case). A file
  whose path holds a marker (the model's data folder, the OLMo adapter, the model manifest, p's lock files) is read
  only with your file-reading tool (which runs no process), or in the shell by `cd` into its folder through a glob (cd
  is a builtin) and then a redirect (`cat < name` where the name holds no marker, or `cat < ol*_hf.py`, whose glob the
  shell expands for the redirect, not for an argv); a git pathspec glob in quotes, such as 'data/ol*/...', keeps a
  marker out of argv for git's own commands. A shell variable or glob that expands to a marker in an argument is a
  breach. Never glob the repository root or results/raw/ in an argument; use git ls-files with a quoted pathspec or
  your file-search tool instead.
- Nothing under data/mf3 is listed or read; no whole-tree git status. Nothing under data/*/ckpt or data/*/reports is
  read, listed, sized or timed.
- Code's scratch folder is not read at all.
- Every git command over the tree takes item 3's pathspec and the mf3 exclusion: `-- . ':!data/*/ckpt/**'
  ':!data/*/reports/**' ':!data/mf3/**'` (a git command on named non-data files may name them instead).
- A glob is expanded and read before it is looped over.
- The list of record v2, items 1-5, verbatim (it governs every read):
1. **Permitted (names, ids, digests):** a bare `git status --porcelain`; a name-only `ls` (no `-l`, `-t`, `-s`, `-la`); `git ls-files`; `git ls-tree --name-only`; `git diff --name-status` and `--name-only`; `git show --name-only` and `--name-status`; `git log --name-only`; `git log` with `--format` of ids, subjects and commit times over any path; `shasum`/`sha256sum` and any program's digest that prints no byte, size or time; `git rev-parse <rev>:<path>` compared in the shell; `git check-attr`; a `find` that prunes every `*/ckpt` and `*/reports` directory (`find … \( -path '*/ckpt' -o -path '*/reports' \) -prune -o … -print`).
2. **Content.** Files under `data/*/ckpt` (the checkpoints and call logs) are read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4: no `cat`, `head`, `tail`, `json.load`, editor or search over them. Files under `data/*/reports` are the read domain (m:271; the stage writes them redacted) and may be read for their content by Code and by the seat — for a stage entry's figures, a declared counter, or a read — with nothing from them printed into a raw beyond what the entry's form reports. **Metadata:** no size or time of either directory or any file in them, in any form (`--stat`, `--numstat`, `ls -l/-t/-s/-la`, `du`, `wc -c`, `stat`, `git ls-tree -l`, `git cat-file -s`, any unpruned `find`, `mdfind` over them).
3. **Content searches** over a checkout or a tree — `git grep`, recursive `grep`, `rg`, `mdfind -onlyin`, and the pickaxe (`git log -S` / `-G`) over any range — exclude the checkpoint and report files with a form tested on this git: `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` (equivalently `':(exclude,glob)data/*/ckpt/**' ':(exclude,glob)data/*/reports/**'`, or `':!data/**'` where nothing under `data/` is wanted), or the prune for `find`-driven greps. The bare `':!data/*/ckpt'` form is not an exclusion on git 2.39.5 and is not used. A pickaxe search without the pathspec can name a commit whose checkpoint matched, which is content; it is a departure.
4. **The pre-push screen** may read every file in the range, `ckpt` and `reports` included, and prints only a per-class verdict, range totals, and one line per distinct match outside those directories; a match inside one is a count by path class and a halt for the seat.
5. **A running stage:** the end-wait is on the PID alone (O3-1); no `stat`, listing, `tail`, `Monitor` or read of its raw, checkpoint or reports until the invocation has ended — in every session, including the coordinating one.
```

## 4. G-TIME-n's specification as the texts state it (the survey's report, as returned)

```text
G-TIME-n: its specification as compiled from the repository at HEAD deabf3f, read-only

The texts give G-TIME-n one sentence (n:118). They fix what it runs under: LOCK-n v0.1's sha256 and C. They fix where its figures go: LOCK-n v1.0, where the PI sets the cap. They fix which monitors bind. They do not give its read set, a pass rule, the projection formula, how I/O and G-READ-n's fits are timed, its output paths or its exit codes. The open questions at the end list these gaps.

Short forms:
- `n` = PROPOSAL-n-bk-reconciliation-v0_2.md; `L` = LOCK-n.md; `A-n1/2/3` = the three addenda at root; `R` = RESULTS.md at HEAD.
- Raws, all under results/raw/:
  - `ans20b` = 2026-11-20_n-lock-v0_1-read_design-to-code_answers.md; `ans20` = 2026-11-20_n-gvec-gcal-reads_design-to-code_answers.md; `rt20` = 2026-11-20_first-sitting_pi-routing.md
  - `ans19` = 2026-11-19_n-starred-twelve_design-to-code_answers.md; `rt19` = 2026-11-19_first-sitting_pi-routing.md; `ans19b` = 2026-11-19_n-gvec-stop-lock-opens_design-to-code_answers.md; `rt19b` = 2026-11-19_second-sitting_pi-routing.md
  - `box` = 2026-11-18_box-gpu_design-to-code_answers.md; `ans18b` = 2026-11-18_n-step4-smoke-pause_design-to-code_answers.md; `ans18c` = 2026-11-18_n-step4-run-pause_design-to-code_answers.md; `rt18c` = 2026-11-18_third-sitting_pi-routing.md
  - `ans16b` = 2026-11-16_n-build_design-to-code_answers.md; `rt16b` = 2026-11-16_second-sitting_pi-routing.md; `ans15` = 2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md; `rout` = 2026-11-20_n-lock-v0_1_routing.txt
  - Code's raws: `rv3` = 2026-11-16_n-build_review-step3.md; `rvd` = 2026-11-16_n-build_review-drafts.md; `svc` = 2026-11-16_n-schema_valuescheck.md; `sfr` = 2026-11-19_n-schema-followup_review.md; `rps` = 2026-11-18_n-step4-run-pause_code-to-design_STOP.md; `bx2s` = 2026-11-19_n-step4_bext2-v1_stage.txt
- Code files: `schema`, `runner`, `primitive` and `cells` are under valence_core/n/; `drv` = scripts/n_sessions.py.

## 1. The specification as the texts state it

**1.1 What it is, and when it runs**
- **The stage, verbatim:** "**G-TIME-n.** Six reads of each kind (steered, shadow, fidelity re-compute, capture-on) timed on the box; projections; the cap set by the PI." (n:118).
- **Its place in the order:** "10. Commit LOCK-n v0.1. 11. G-TIME-n; the PI sets the cap. 12. G-VER. 13. Commit LOCK-n v1.0 with D_n." (n:159). Its entry is named `G-TIME-n` (n:161). The same order is in ans15:62 and L:992-998.
- **The seat's restatement:** "**G-TIME-n** (step 11) on the box, under v0.1: six reads of each kind timed, projections for the PI's cap; its identity carries v0.1's sha256 and C." (ans20b:58).
- **Its routing:** item N.2 reads "G-TIME-n's launch files under v0.1 after the commit; the box's run; the projections to you for the cap at v1.0; then G-VER [go, after step 10]" (ans20b:71). The next step is "G-TIME-n's launch files under v0.1 (item N.2), to the coordinating session first" (R:124).
- **What the routing record holds:** the committed entry quotes only item N.1 of the PI's routing of 2026-11-20, second sitting ("Route as given"; R:24-34).
- **Not wired yet:** "Stages G-TIME-n, G-VER, the campaign and G-READ-n are wired at their own steps" (drv:182; also R:5523-5524 and L:997-998).

**1.2 Where its figures go**
- **OPEN 3, settled:** "G-TIME-n's figures enter v1.0 (n §8 steps 10–13); v0.1 is committed without them." (A-n3:60, quoted at L:735-738). This was ruled at ans19b:43 and routed at rt19b:15. The rest of the record agrees: L:743-744 says "the timed reads of each kind and the projections are v1.0's hole"; hole 18 is "G-TIME-n's figures, v1.0's" (R:153); rout:13 marks G-TIME-n's figures as a hole.
- **v1.0's contents:** "Projections, the cap, D_n, hashes of this document, the lock chain, the analyzer, BK's input files." (n:120). ans20b:58 adds `lock: LOCK-n v1.0` with the route line, "by D_n 2026-12-15". ans20b:75 adds the gate line verbatim.
- **The Clock:** D_n = 2026-12-15, the day inclusive, by the committer date of v1.0 (L:985; n:152).

**1.3 The identity at "time"**
- **R14:** Code's reading at R:3035-3036 was "The identity sets the ceiling at every stage but backend-ext, so a timing re-computation above C pauses G-TIME-n." The seat accepted it: "the ceiling binds at G-TIME-n, whose identity carries the lock's C" (ans19:50). The PI routed it (rt19:16). It is carried at L:560 and in the runner's docstring (runner:59-61).
- **lock_sha256:** LOCK-n v0.1 is `88d9fe7b21e72db3a9ebd3a65339cc69a2528f892b50053bdf663b9c99f8e9d5` (R:30-32). My shasum of HEAD's file agrees. The seat calls it the figure every stage identity carries from here (ans20b:57; L:740-742).
- **C:** "C = max(0.25, 2 × 0.0625005) = 0.25", and the identity bound is C (L:505-511; A-n2:24, :26).
- **The other values the lock fixes:**
  - the binomial and fidelity rule: alpha 0.01 one-sided, exact binomial, upper tail, with the tile and cadence of 160 (L:652, L:662-666); p0 = 1/26 (L:491-493); median rel 0.0013026706058596332 (L:494); TAU (L:486);
  - the read window: 4,096 (L:456-459);
  - the dose map of record: d_eq 0.2869170055735837 and d_20 0.5738340111471674, from `data/n/gcal/dose_map.json` `d4a73b54…efb3` (L:363-367);
  - the site and captures: site 32, capture band 33–63 (L:295, L:474);
  - the directions' sha16s (L:302-313);
  - the rendering and labels: rendering_id is MANIFEST `53a8cd74…99d8` (L:187-189, L:219-220); the label convention is "space" (L:230-236);
  - the weights: `36f05404…0fdb` (L:770-774);
  - the backend: n's identifier `8264f719efd347a9`, bridged to `4ed3f2c70fe8afbf` (L:761-763), on pod `emw1e4embiwe9b` (L:752-753), in the pinned environment (L:767-769);
  - the package: `06b55761…1d39` and its 12-file closure (L:781-797);
  - the sample's words (L:406-410).

**1.4 Triggers that bind at G-TIME-n (LOCK §10)**
- **Precedence:** rendering, then nonfinite, then fidelity-ceiling, then identity-bound, then fidelity-binomial. "A fired monitor ends the invocation for every arm" (L:535-539).
- **On a pause:** "Every pause STOPs the arm's launches until adjudicated; Code never self-adjudicates; verdict criteria are untouchable (rule 21)." (n:148).
- **The rows:**
  - rendering: where "campaign, G-TIME-n"; "pause; the read is not launched" (L:549). This is the only row that names G-TIME-n.
  - nonfinite: "every read" (L:550).
  - fidelity-ceiling: "every re-computed read, any dose | > C = 0.25 nats | pause at once" (L:551).
  - identity-bound: "d = 0 reads" (L:552).
  - fidelity-binomial: "the re-computed reads" (L:553).
  - cap: where "campaign"; "the stage's records' summed `duration_ms` against the lock's cap (v1.0's, the PI's) | CAP end state" (L:554).
  - G-VER: "before any read … a STOP for the seat … no read is launched and the campaign does not start" (L:543).
- **Code's earlier readings:** sfr:207 says identity-bound is "never a pause's kind at the campaign or G-TIME-n, only an also_fired entry". sfr:211 says a "timing" re-computation above C pauses G-TIME-n.

**1.5 The cap, the hours and the pod budget**
- **Planning figures:** n:101 is headed "[S, planning values; G-TIME-n governs]". It gives "Forwards ≈ 10,500 over ≈ 1.2–1.3k tokens at 0.3–0.6 s per hooked forward … ≈ 0.9–1.8 h; the two extractions … minutes; G-CAL-n's generations ≈ 10 min; G-READ-n's probes CPU; cold loads 130–200 s each (m:205). **Pod budget proposed: 8 h for N-pod, the cap set by the PI at LOCK-n v1.0** … the campaign within one pod session (… a box change restarts the campaign; gate stages may span boxes)".
- **The PI's decision:** "the N-pod budget is 8 h, the cap set by the PI at LOCK-n v1.0 (§2.7)" (R:15740; L:587).
- **The new box:** "n §2.7's 8 h proposal was at the A100's rate; G-TIME-n projects on the new box and the PI sets the cap at LOCK-n v1.0 in hours, as before. The spend is the PI's at every step." (box:31). The rate is "$4.39/h against $2.19/h, over the hours G-TIME-n projects" (box:18; also R:5110).
- **The cap clause:** "the cap counts the reads' and re-computations' model time, loads reported beside and outside it" (ans16b:50; rt16b:28; L:591-592).
- **OPEN 2, settled (L:595-608, A-n3:60):**
  - (a) The cap is "the reads' and re-computations' model time as the runner computes it", with each invocation's load outside it. G-READ-n's fits, where they run on the box, are "timed by their own artifact and counted against the cap in v1.0's accounting … the lock stating the sum". A crashed invocation's absent load is a declared gap.
  - (b) n §2.7's split is carried "as planning values marked as the A100's rate … G-TIME-n's projections on the H100 revise them at v1.0, where the PI sets the cap".
- **I/O:**
  - "The reads' I/O outside the cap: the cap is model time as the runner computes it (§11); I/O is outside and declared so." (ans20b:44).
  - From the BUILD entry: "31–32 row writes with fsync per read, and the cell JSON rewritten per append. G-TIME-n times it on the volume." (R:5664-5665).
  - From the step-3 review: "outside the cap but inside pod hours; G-TIME-n should time it on the volume" (rv3:196); disposition "flagged for G-TIME-n, which times the reads with their writes on the volume" (rv3:300).
  - From the drafts review: "G-TIME-n measures the wall-clock" (rvd:225-226).
- **The runner's inputs:** "Cap and alpha as the runner's inputs from the lock, a resume refused under another: accepted" (ans20b:39; R:5649-5651).
- **`cache.crop`:** the environment is pinned at 5.15.0, and "a move past 5.18 is a backend change" (ans20b:45; R:5666-5667).
- **The box:** "through G-TIME-n and the campaign … [stays up]" (rt20:16; ans20:58; ans20b:59). A new pod is a new box and re-runs the characterization and the BACKEND extension first (ans20:58). The campaign completes on one characterized backend (CLAUDE.md:127-130).

**1.6 Timing figures already recorded for it**
- **The fresh pair's cost:** "The fresh pair's cost, measured at the extension (median 357.1 ms against the cached read's 309.0 ms), is recorded for G-TIME-n and used by nothing." (A-n2:40; L:732-734; rt18c:18; ans18c:57). ans18b:68 notes "n-build's cost estimate of the fresh path for G-TIME-n [noted]".
- **The diagnostic's figures:** the fresh pair is "about 1.16 times" the cached read; maxima 387.2 / 601.4 ms; "with both paths at every read … a median 657.0 ms a read" (rps:152-156; under "bare", d = 0; R:4203).
- **The records' fresh share is closed to Code:** "those sit in the cell, closed to Code under item 2. The seat, or the analyzer at G-TIME-n, may read them there." (rps:193).
- **backend-ext-2 under "space":** load 11999 ms and 24 per-read `ms=` lines (bx2s:9-34; R:3163).
- **Other H100 loads:** G-VEC 119470 ms (smoke) and 28510 ms (run) (R:1436); G-CAL-n 29787 ms (R:1051).
- **The fidelity sample:** Code said its realized size "is reported at G-TIME-n and in LOCK-n" (rvd:227-228). It is now pinned at 15 of 160 (L:410-415), 6 floor and 9 neutral (R:47).

**1.7 G-READ-n's fits**
- "Where it runs (the box's GPU or the laptop's CPU) is Code's call, timed at G-TIME-n and counted in the cap where it runs on the box." (A-n1:56). The same at L:571-573 and ans16b:42 ("About 404,000 fits in all"). Flagged at R:5660-5661.

**1.8 Captures and the read set the projection targets**
- **Captures:** every forward captures the read position over the band, float32 (L:460-462). schema:89: "every read captures: G-TIME-n's "capture-on" kind is every read" (also L:731-732; svc:414). Storage is about 4.9–5.0 GB at 7,680 rows, kept on the box and copied to the laptop with hashes before the pod stops (schema:83-86; A-n1:54).
- **The campaign's read set:** 7,680 reads (L:446-448, L:464-466), with planning "about 10,800" forwards (A-n1:46). The re-computation rule is at L:449-451; E = 48 (L:675-677); the tile's trials are in the power note (L:660).
- **What is committed:** "raws and checkpoints committed before any pod instance stops (rule 27)" (n:103; CLAUDE.md:354-359).
- **Blinding:** stdout prints "session index, arm, dose, the fidelity value against TAU, timing — never a margin" (n:130).

## 2. Code that exists

**2.1 schema.py**
- **The stage:** `STAGES = ("campaign", "time", "backend-ext")` (schema:256). G-TIME-n writes records (schema:15-17; R:8339-8340).
- **The identity at "time":** lock_sha256, dose_map, identity_bound, ceiling and median_rel must all be non-null; they are null only at backend-ext (schema:845-852). F5 requires p0 ≥ 1 of 3 (schema:876-878). The window must be ≤ 4,096 (schema:863-864); the band and the exact dose map are checked at schema:865-890. There is a self-test case "F5: p0_count 0 at G-TIME-n" (schema:2171-2172).
- **Timing fields:**
  - `duration_ms` is "wall-clock of the read's model work, both paths" (schema:389).
  - `duration_ms_fresh` is "the fresh path's share; null without a re-computation" (schema:390). It is described as "for G-TIME-n's kinds and the cap" (schema:121-124) and checked at schema:1083-1089. It was added so G-TIME-n can time the re-computation apart (R:8380-8382; answering svc:126).
- **The "timing" reason:** "``timing`` at G-TIME-n (a re-computation G-TIME-n takes to time it)" (schema:95-99, :323).
  - At "time" a read at {0, ±1} need not carry a re-computation: the dose-rule requirement is only at campaign and backend-ext (schema:1042-1043). Where it does carry one, the reason is "dose-rule".
  - A re-computation at any other point must be "timing" (schema:1047-1050).
  - The identity block is required on an unsteered re-computed read at "time" (schema:1071-1082).
  - Self-test cases: schema:1913-1921 and schema:2096-2100.
- **No plan for "time":**
  - `read_plan` refuses any stage but the campaign: "G-TIME-n's … read sets are their own" (schema:585-591).
  - The report's `read_plan_sha256` is null at "time" (schema:1155, :1388-1391). `per_arm` is checked against a plan only at the campaign (schema:1395-1400).
  - A cell must be an ARM_CELLS cell at a kept point (schema:1140-1145, :302-311).
- **The report:**
  - `cap` holds {hour_cap_ms (nullable), used_ms, hit, loads_ms} (schema:1208-1214, :1510-1516; docstring :197-200).
  - The end states are COMPLETE, PAUSE, PI-STOP, G-VER-STOP and CAP, with no PASS (schema:1131, :207-215).
  - `example_identity("time")` exists (schema:1624-1652).

**2.2 runner.py**
- **`run(inputs, plan, resume)`** (runner:376-555):
  - launch indices must be 0..M-1, with no repeat (:384-385);
  - the alpha must be the identity's (:386-389);
  - the records on disk must be the plan's first reads (:404-410);
  - a resume keeps the cap and the alpha (:412-416);
  - the cap is checked before each launch (:467-469);
  - the tail is evaluated at the end (:521-537);
  - `loads_ms` is appended per invocation (:548).
- **`StageInputs`** (runner:255-274): `hour_cap_ms: int | None`; `load_ms` is required, a measurement with no default; `clock` is the primitive's timer.
- **`PlannedRead`** (runner:110-123) carries a `fidelity_reason` per read.
- **`campaign_order`** is the only plan builder (runner:140-164). It asserts equality with `schema.read_plan`, which refuses "time" (:161-163). So G-TIME-n's plan must be built outside it, as `bext_plan` is (drv:551-555) and as the runner's own time-stage self-test builds one (runner:754-766).
- **Monitors:** every kind binds at "time" (runner:167-252). With fewer than 160 reads only the end-of-run tail is evaluated (runner:51-54, :521-535). The PINs are ORDER (:18-22), PAUSE (:23-29), SCOPE (:30-34), the binomial (:35-54), the ceiling at G-TIME-n (:59-61), RENDERING (:63-65) and CAP (:66-70).
- **stdout per read:** `read {i} s={bk_run} {arm} {dir} {dose} fid=… ms={duration_ms}` (runner:475, :509-511). It prints no fresh share and no I/O.

**2.3 primitive.py**
- **What `read` times** (primitive:197-285): the clock starts at the read (:205-207). Timed inside are the cached prefill and two label continuations (:219-221) and the captures' GPU-to-CPU float32 copies (:330, :234). The fresh pair, two full forwards, is timed separately (:237-241). Then `duration_ms = max(total, dfr)` (:283-284).
- **Outside the timing:** the cell write (runner:503).
- **The shadow is mandatory:** a steered read needs its session's N1-V d = 0 record on disk (primitive:213-217).
- **`crop`:** asserted present and used (primitive:301-302, :328-329, :341-343).

**2.4 cells.py `append_record`** (cells:200-249)
- checks the record (:212);
- runs `check_cell` over the whole cell on every append (:240-243);
- writes one row per layer, each flushed and fsynced (:244-245, :185-197);
- writes the JSON atomically (:248).
- All of this is outside `duration_ms`.

**2.5 The drv template (backend-ext and backend-ext-2)**
- Its steps are documented at drv:38-81; Code's readings R1–R8 at drv:82-112. R1 chose the session set: "n v0.2 names no set" (drv:85-86). R5 is "no cap" (drv:95).
- `run_backend_ext` (drv:1035-1174), in order:
  1. smoke vs record roots (:1055-1069);
  2. refusals: the pod, cuBLAS, the stream known answer (:1070-1080), and the ruling files (:1081-1083);
  3. the STAGE line (:1087);
  4. the weights of record and the WEIGHTS line (:1088-1090; `weights_of_record` at :590-602);
  5. a run of record runs only HEAD's committed driver bytes, with a DRIVER line (:1092-1098);
  6. the ids and the MANIFEST pin (:1099-1102);
  7. the R6 bridge before the load (:1104-1107);
  8. the identity (:1108-1113; `bext_identity` at :647-668);
  9. what is on disk, via `prior_state` (:1115, :917-945);
  10. G-VER before the load: a STOP returns 1 with no report (:1130-1135; :57-59);
  11. the load, timed (:1136-1138), and the provenance re-checked (:1139-1143);
  12. `runner.run` with `hour_cap_ms=None` (:1147-1150);
  13. exit 1 unless COMPLETE (:1151-1156);
  14. after a COMPLETE run, the stage's own code reads its cell to print a summary (:1157-1160). This is the route by which figures leave the closed ckpt.
- **Paths:** `data/n/ckpt/<stage>/` and `data/n/reports/<stage>.json` (drv:503-507). Writes are allowed only under data/n/ (valence_core/n/guard.py:74-81).
- **Commands:** main's list has no "time" (drv:3682-3684).
- **Exit codes elsewhere:** gvec 0/2 (drv:150-152); gcal 0/2/3 (drv:173-176).
- **.gitignore:** "any later n artifact (captures, checkpoints, reads) needs its own line" (.gitignore:260-261). Under the backend-ext pattern the report and the cell JSON were admitted and the arrays stayed on the box (.gitignore:283-301; R:3190).

**2.6 n_analyze.py**
- `GATE_STAGES` includes "G-TIME-n" (n_analyze.py:129). A NOT-RUN cause exists: "clock:gate-stopped": "{stage} STOPPED and no re-specification was locked" (:121-122).
- VERDICTS refuses a non-campaign report (R:2996).

**2.7 Prior timing stages as templates**
- **p's G-TIME-OLMo:**
  - It is m's `run_gate_stage` at gate `time`, "two sessions, one per arm, uncached" (valence_core/p/stage.py:5-6). Exit 0 PASS, 3 PAUSE, 4 STOP, 2 refused (scripts/p_sessions.py:38-48).
  - The run, PASS ×3 (R:12540-12633): sham bar 0/10 with critical 2; hair triggers silent; sham seconds 3.528, 3.972 and 5.289.
  - Committed: m's checkpoint, the call log, the reports, the raw and the block (R:12576-12581).
  - Projections: "The basis of record is m:205's — 19.5 s per session at instruct, 22.7 s at SFT/DPO … the measured sham seconds … reported as the observed lower figure and no basis" (results/raw/2026-11-09_p-gtime_design-to-code_answers.md:25). The cap share was the PI's "at G-PWR, per checkpoint" (:26).
- **m's G-TIME-F0 and G-TIME-F3:**
  - G-TIME-F0: "One session per Q-F0 arm (2), excluded from the campaign and from every DV; … uncached timing recorded" (PROPOSAL-m-gating-campaign-v1_11.md:280). G-TIME-F3 has six sessions with bars (:293); G-TIME-OLMo is at :302.
  - Driver: exit 0 PASS, 4 STOP, refusals 2 (scripts/mf3_sessions.py:16-29).
  - G-TIME-F3's run, "PASS as computed" (R:13898-13979): bars 0/25 and 0/13; sham seconds 109.1, 209.4 and 392.5. Committed: the checkpoint, report, reads, raw and ping (R:13961-13967).
  - The seat's rulings on timing: "beside the projections, not in place of them" (results/raw/2026-11-08_gtime-f3_design-to-code_answers.md:33-35). And: "v0.2 projects on §2.4's named bases … the measured sham figures beside them, not substituted … The hour cap at step 15 is the PI's" (results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md:53).
  - The stamp rule: Q4 (same raw, :49) and WORKFLOW.md:28, :53.
- **The contrast:** n's text gives G-TIME-n more weight than m and p gave their G-TIME stages: "G-TIME-n governs" (n:101), and its projections "revise" the planning split (L:605-608).

## 3. What the texts leave open for a build

1. **The read set.** Which arms, directions, dose points and sessions make "six reads of each kind"? Are the kinds separate reads, or attributes of one read? Capture-on is every read (schema:89). Nearest texts: n:118, L:731-734, schema:95-99, :1042-1050. No key for drawing sessions is in LOCK §5 (L:397-404), and the keys are v0.1's item (n:117).
   - Constraints: steered reads need their shadows first (primitive:213-217); N1-R reads only floor sessions (schema:919-920); N4 reads need the schedule zone (runner:148).
2. **Pass rule.** Does it have one, or is it a measurement ending COMPLETE? There is no bar in n:118 and no PASS end state (schema:1131). m and p had bars. n_analyze expects that G-TIME-n can be "STOPPED" (n_analyze.py:121-122).
3. **The projection formula.**
   - The re-computations under the plan of record are stated in no text. My hand count, not tool-run: dose-rule 3,040 (480 + 1,920 + 320 + 320) plus the keyed sample's 597 (15 × 11 + 6 × 72), 3,637 in all. For comparison, n:95 has ≈ 3,140 and A-n1:46 "about 10,800" forwards.
   - Units: n's "forward" counts a re-computation as one, but the fresh path is two full forwards (schema:30-32).
   - Loads: per invocation, and each resume is another load.
   - I/O and the captures' copy-back (about 5 GB).
   - Which of these go inside the cap (model time) and which are pod hours.
   - Indicative scale only, my arithmetic from the "bare" d = 0 diagnostic medians: 7,680 × 309.0 ms + 3,637 × 357.1 ms ≈ 1.0 h of model time.
4. **Outputs.** Stage root and report paths, `.gitignore` lines, a projection artifact (none is named), and what gets committed.
5. **Timing figures out of the closed ckpt.** The report carries only `used_ms` and `loads_ms`, and stdout only `duration_ms`. A per-kind or fresh-share summary therefore needs the stage's own code (the backend-ext route, drv:1157-1160) or the analyzer.
6. **I/O measurement.** It is not timed by any runner field. G-TIME-n's small cells cannot show the per-append growth of the JSON rewrite and of `check_cell` (cells:240-248; rv3:66).
7. **G-READ-n fits.** How are they "timed at G-TIME-n" (A-n1:56) when they need the campaign's captures (n:121)? The n-gread-v1 artifact has no timing field (schema:1231-1251). How is "the lock stating the sum" reconciled with the runner's `hour_cap_ms`?
8. **Identity fields.**
   - `sample_rule`'s words at "time" (schema:507-508).
   - The `directions` set (schema:476).
   - `hour_cap_ms` at "time": presumably None, as in R5's precedent (drv:95); the cap row says "campaign" (L:554).
   - Whether the identity's package must equal L:781's.
9. **Monitors and pauses.** What does a pause at G-TIME-n mean for v1.0 and the campaign? The binomial tail at fewer than 160 trials.
10. **Exit codes.**

## 4. What may need the seat or the PI before it runs

- **The read set.** It is a pre-data declaration of a design term. Can Code run on a declared PIN, as with R1–R8 (drv:82-112), or does the seat rule first?
- **The package.** If the wiring touches valence_core/n, the digest moves away from LOCK v0.1's pinned `06b55761…` and its closure (L:781-797; ans20b:57). Wiring in drv alone keeps it.
- **Exposure.** n §0.4's table (n:18-28) has no G-TIME-n row, and ledger (53) requires "the exposure count is computed from the gate list" (n:14). Any G-TIME-n read at d = −1 adds negative-pole forwards that the table does not hold.
- **G-VER.** Its role at G-TIME-n: before the load, as the template does, and "before any read" (A-n1:24)? But G-VER of record is step 12, and L:543's STOP speaks of the campaign.
- **G-READ-n fits.** The timing and placement call needs a method before the run (see 3.7).
- **The routing record.** Item N.2's routing words are not quoted in any committed text (R:24-34 quotes N.1 only).
- **Who reads the output.** The projections go "to you", the PI (ans20b:71), and G-VER follows directly. m and p stopped for the seat's read after their G-TIME stages. Does the seat read before the cap?

## OPEN QUESTIONS

1. Which reads (arms, directions, doses, sessions, and a key for drawing sessions) make "six reads of each kind", and are the kinds separate reads? Before the run.
2. Does G-TIME-n have a PASS/FAIL rule? What STOPs it (n_analyze's "clock:gate-stopped"), and what are its exit codes?
3. What is the projection formula: counts, units, loads, I/O, copy-back, G-VER and G-READ-n? Which parts are the cap (model time) and which are the 8 h pod budget? May the extension's 309.0/357.1 ms ("used by nothing") be a basis, or only reported beside?
4. How is I/O timed on the volume, and how is the cells' per-append growth extrapolated?
5. How are G-READ-n's fits "timed at G-TIME-n" without campaign captures? Where do they run? Where is their time recorded (n-gread-v1 has no field)? How does "the lock stating the sum" meet the runner's cap? Before the run.
6. Does G-TIME-n run G-VER before its load? Is that G-VER of record, and what does its STOP mean? Before the run.
7. What do the identity's `sample_rule` and `directions` hold at "time"? Is `hour_cap_ms` None? Must the package digest equal LOCK v0.1 §18's? Before the run.
8. What are the output paths, the `.gitignore` admissions, the committed set, and the projection artifact?
9. How do per-kind and fresh-share timing figures leave the closed `data/n/ckpt`: stage-printed, in the report, or through the analyzer?
10. What does a pause at G-TIME-n (a ceiling fire, the binomial tail) mean for v1.0 and the campaign?
11. May G-TIME-n read d = −1 points that §0.4's exposure table does not count? Before the run, for the seat.
12. Do G-TIME-n's reads enter no DV (n has no counterpart of m:280's exclusion)?
13. Does the seat read G-TIME-n before the PI's cap, or do the projections go to the PI alone?
14. Item N.2's routing words: are they on record?
15. On a box change before the campaign, does G-TIME-n re-run (n:101's "gate stages may span boxes")?
16. Do WORKFLOW.md:28 and :53's stamp and wall-clock rules (m's G-TIME-F0 Q4) bind n, given that n:130 permits timing on stdout?
17. D_n: G-TIME-n, G-VER and the v1.0 draft with the seat's read must all land by 2026-12-15.

## DEPARTURES

- `sed -n` line-range prints of named non-data files: reads only, no script and no write. Declared for classing.
- `shasum -a 256` on five named root files. It is Perl on this laptop; list item 1 permits it by name.
- One `git grep` used `':!data/**'`, item 3's stated equivalent, in place of the three exclusions; it also excludes data/mf3.
- One `git grep`'s output was saved by the harness to its tool-results folder, outside the repository. I wrote nothing and did not open it. That output quoted code naming a data/mf3 path; nothing was listed from data/mf3.
- `wc -l` on named code files and WORKFLOW.md; `cut` on outputs.
- Otherwise none. No guard marker reached any argv. No data/ file, Code scratch or ckpt/reports content was read or listed.

```
