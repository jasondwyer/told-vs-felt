# The campaign wiring (Q-F3): the blind review, Code's dispositions, and round 2's mutant runs

*Code's raw, PI date 2026-11-15.*
- *What was reviewed:* the uncommitted edit that wires `campaign` in `scripts/mf3_sessions.py`. The candidate (sha256
  `206dc3fc…98b9`) was the working tree's file at the review. It was checked against HEAD's driver blob
  (`285eed04…0e44`, at `a89a4fa`), the driver at LOCK-m-F3 v1.0.
- *How:* one blind agent, read-only on the main checkout, under a brief that quotes the list of record v2's items 1–5
  as written.
  - It worked in a sparse clone, with every `data/*/ckpt` and `data/*/reports` directory left out of the working tree.
  - It ran the self-test with every model import blocked.
  - It built 50 one-defect mutants of the production code.
- *Outcome:* no MAJOR, 3 MINOR and 8 NOTEs.
  - Of the 50 mutants, 43 were KILLED, two of them only by hanging on a FIFO (NOTE-5). 7 SURVIVED: two behavior gaps
    (MINOR-2) and five that change only a message or a help text.
- *After the review:* Code applied the three MINORs and NOTE-2, NOTE-3, NOTE-4, NOTE-5 and NOTE-7. NOTE-1 is the entry's
  PIN map. NOTE-6 is not changed. NOTE-8 is flagged for the seat.
  - The self-test passes 235/235 on the final bytes (`7bb6f7ca…28a4`). The candidate the review read passed 233/233.
  - Round 2 re-ran mutants through the reviewer's harness against the fixed self-test, in a fresh sparse clone: the
    seven survivors, X01, the two FIFO hangs and one new mutant (round 2's table).
- *Code's masked scan of the reviewer's transcript* (its commands only; no output text printed):
  - 60 distinct Bash commands, over every row of the transcript.
  - Two name a `ckpt` or `reports` path, and neither reads a checkpoint or report file:
    - the clone's set-up, with its sparse-checkout patterns;
    - a `/usr/bin/grep` over the candidate file, whose pattern quotes the docstring's
      "data/mf3/ckpt/Q-F3_campaign.json".
  - Three more name `data/` (a second pass over the same commands, for `data/` and the metadata forms), all in the
    clone: a name-only `ls` of `data/`, `data/mf3` and `data/m`; a JSON read of
    G-PWR's record, `data/mf3/gates/Q-F3_G-PWR.json`; and a `wc -l` of named files, that record among them. That file
    is outside `ckpt` and `reports`, as the brief allowed.
  - No `git status` ran in the main checkout. The reviewer's one `git status` command named the clone.
  - Its git commands in the main checkout were the brief's read-only forms: `git rev-parse HEAD`,
    `git show HEAD:scripts/mf3_sessions.py` piped to `shasum`, `git log --format='%h %s' -3`, and
    `git diff -- scripts/mf3_sessions.py`.
- *This raw:* Code's dispositions, round 2's table, then the report verbatim.
  - The report was extracted by script from the agent's hand-back in its transcript (the text's sha256 `8fe80358…7c48`,
    its final newline included; 317 lines). It matches the copy in the reviewer's work directory byte for byte.
  - It holds no local path and no clock time.
- *Nothing ran on a model.*

## Code's dispositions

- **MINOR-1, the seam check's call outside the traps.** Agreed. The case now takes m's form (m's round 1's M1-7:
  fresh roots and a stub factory, in three calls outside any trap stack), extended:
  - `run_stage` is called for `time`, `id` and `qual`, each with each ruling file (six calls).
  - Each call runs on a fresh test root with a stub factory, inside the trap stack. The stack now traps
    `run_gate_stage` and `run_gid_pair_f3` too.
  - Each call must raise ValueError. Should the guard regress, the call reaches a trapped stage on the stub in a test
    directory, never `data/mf3` or Qwen.
  - The check also runs `time`, `id` and `qual` with either flag at the command line: argparse refuses each (exit 2,
    "unrecognized arguments"). m's check does this with `--adjudication-file`; `--pi-stop-file` is added here.
- **MINOR-2, two precheck behaviors untested (K05, K03).** Agreed. The refusal table gains three cases (40 → 44 with
  P03's):
  - (a) a paused campaign offered the seat's adjudication without `--resume` is refused CHECKPOINT EXISTS before the
    load;
  - (b) a checkpoint whose pauses are an object (without `--resume`) or a number (with it) is refused before the load
    as one that "cannot be read as a campaign checkpoint". These are the reviewer's two malformed shapes; the object is
    a non-empty one, the shape on which `_paused_unadjudicated` raises KeyError.
- **MINOR-3, two PIN sentences not true of mf3.** Agreed.
  - **"Each message is the stage's own words."** The mirror's messages now are mf3's stage's own words, not m's stage's:
    - CHECKPOINT MISMATCH reads "another text";
    - PI STOP REFUSED drops ", not PI-stopped";
    - SCHEDULE EXHAUSTED drops "(pi_stop)".
    - Only the two declared suffixes remain. The PIN now names mf3's `run_campaign` as the source.
    - A new check reads `run_campaign`'s source by `ast`: its f-strings' text, each placeholder by its expression. It
      asserts that each of the four messages, with the path and the arm put back as placeholders, equals one of them,
      beside only the declared suffixes.
  - **"…which the self-test's stub path, where no precheck runs, shows."** The clause is struck, so the sentence now
    ends at "reads it as it stands".
- **NOTE-1, re-quoting and re-anchoring.** Done in the entry. It re-quotes the revised WIRED_CMDS sentence and gives
  every PIN site's line on the final blob, by grep.
- **NOTE-2, CAMPAIGN_PAUSES not m's words.** Agreed.
  - The text is now m's `camp_pauses`, verbatim. The three dropped pieces are restored, each true of Q-F3:
    - "(C9(i))": the analyzer Q-F3 runs is m's, `scripts/m_analyze.py` (`stages.ANALYZER_PATH`);
    - "(the seat's adjudication, or a PI stop not recorded with it)";
    - "; where no precheck runs the stage re-finishes the end and then refuses it, NOT APPLIED, exit 4" (mf3's
      `_refinish_campaign` raises NOT APPLIED).
  - The help check now reads m's `camp_pauses` from `scripts/m_sessions.py` by `ast` (the constants check's form) and
    asserts it equals CAMPAIGN_PAUSES. It also asserts that the top-level `--help` gives the campaign's help with the
    text, compared with whitespace removed. G01 and M03 are its kills.
  - The PIN says so.
- **NOTE-3, the `run_stage` PIN on `prior_gate`.** Agreed. It now reads: "the stage's prior_gate reads it again after
  the load, and the stage re-checks G-ID-F3's artifact with its own call of gid_artifact_problems at the run's cap".
- **NOTE-4, "exactly once" again.** Agreed. As at the `qual` wiring's NOTE-7, the values check now asserts each of
  v1.0's two lines as a whole line of the committed lock one or more times. The campaign's lock variants already edit
  or drop every line equal to them, or opening with them.
- **NOTE-5, the FIFO cases hang on a regression.** Agreed. It is a port gap: m runs them in a daemon thread joined with
  a timeout (its round 2's M2-2, round 3's O3-3 and round 4's F4-9), and the port did not carry that.
  - Every call on a FIFO in the ruling helpers' checks now runs in one daemon thread joined with 20 s, released by a
    non-blocking writer's open if it hangs. The calls are `ruling_texts` (both flags), `_campaign_state`, the mirror
    offered no ruling and the RULING line.
  - The mirror's call records `_campaign_state`'s calls (none: it reads nothing, m's F4-9 form), and the RULING line's
    "on an unreadable checkpoint" is checked.
  - m's O3-3 Qwen-path case is ported in the same form, as a new check. A FIFO at the campaign's checkpoint path is
    refused before the load, never opened: offered a ruling and not, with `--resume` and without (beside CHECKPOINT
    EXISTS). The thread joins with 30 s.
  - After a hang of that thread, the self-test gives itself back its own stdout and stderr, which the hung thread's
    `run3` holds redirected. Round 2's first pass found this. Under S02, every line after the refusal table, the
    FIFO check's FAIL among them, went into the hung thread's buffer (round 2, below).
- **NOTE-6, dead code.** Not changed. `REFUSED_CMDS` stays derived, as the `time` wiring wrote it; it is empty now.
  Removing `refusal()` and the refused-subparser loop would edit `time`'s code for no change in behavior.
- **NOTE-7, "a stop" in the docstring.** Agreed. It now says "a pause or a STOP". The stage writes the excerpt only
  when its checkpoint records a pause or a STOP (`_campaign_outputs`); a PI-STOP with no pause writes none.
- **NOTE-8, the starting backend against v1.0 §5.** Not applied: it is outside the routed spec, and it is m's form.
  Flagged for the seat in the entry. The checkpoint binds the backend its first launch reports, and every resume must
  match it. Neither the driver nor the stage compares that backend with v1.0 §5's identifier, `a734dadec8f8ce9b`. The
  report's identity carries it.
- **The message-only survivors** (P03, S03, L02, M03, G01) each gain the reviewer's kill case:
  - P03: the campaign's prior name, linked to G-TIME-F3's first run's checkpoint, is refused, naming "G-F3's,
    Q-F3_qual.json";
  - S03: an ended checkpoint carrying an unruled end look's pause reads "ended";
  - L02: the RULING line on that checkpoint says "on an ended campaign";
  - M03 and G01: NOTE-2's help checks.

## Round 2: the mutants against the fixed self-test

- *How:* the reviewer's harness, unchanged, in a fresh sparse clone at HEAD `a89a4fa` (unchanged since the review),
  made with the brief's commands, with the model imports blocked.
  - The reviewer's generator regenerated the mutants on the final bytes (`7bb6f7ca…28a4`), with three changes: its
    candidate's digest is the final bytes', its list is cut to round 1's ten mutants below, and W01 is added (with
    a header comment). Every anchor matched once, outside the self-test.
  - W01 is new. It puts back the mirror's pre-fix PI STOP REFUSED words.
  - The runs were sequential, one harness process at a time. Each mutant was copied over the clone's driver, and the
    candidate was restored, digest-checked, after every run.
- *Scope:*
  - the seven round-1 survivors;
  - X01, which round 1 killed only after the self-test's untrapped call had run `qual`'s real pre-load path
    (MINOR-1);
  - S02 and T02, which round 1 killed only by hanging (NOTE-5);
  - W01, for MINOR-3's new check.
- *The other 40 round-1 kills were not re-run.* Round 1 killed 43, and X01, S02 and T02 are re-run here.
  - The edits since round 1 add cases and checks, change texts that no round-1 kill rests on, and relax one
    assertion: the values check's count (NOTE-4).
  - The five kills that rest on the values check (C01, C03, C05, C07, F01) fail on its other conjuncts. This is by
    reading, not by a run.
  - Every round-1 anchor still occurs once in the final bytes, outside the self-test (a text check).
- *Baselines under the harness:* the campaign part 20/20; the integration self-test 90/91; the full self-test 234/235.
  - The one FAIL is the constants check, which reads mlx_lm's source while the harness blocks it.
  - "Killed" means any further FAIL, or fewer checks run.

| mutant | the defect | round 1 | round 2 | killed by |
|---|---|---|---|---|
| K05 | a ruling offered never counts (`offered` False) | SURVIVED (gap, MINOR-2 (a)) | KILLED, 18/20 | the refusal table (its new case: a ruling offered on a paused campaign without `--resume`); the final trap count |
| K03 | `_paused_unadjudicated` asked without the open-state screen | SURVIVED (gap, MINOR-2 (b)) | KILLED, 12/13: the part raised KeyError: -1 | the refusal table's new case (pauses an object): the precheck raises on it, before the load |
| S03 | an end look's pause read as unreadable | SURVIVED (message only) | KILLED, 18/20 | the state check (its new case: an ended checkpoint with an unruled end look's pause); the RULING-line check |
| L02 | the RULING line reads the last pause in any state | SURVIVED (message only) | KILLED, 19/20 | the RULING-line check (its new case, on that ended checkpoint) |
| M03 | the campaign subparser's `help=` without CAMPAIGN_PAUSES | SURVIVED (help text only) | KILLED, 19/20 | the help check (the top-level `--help`) |
| G01 | CAMPAIGN_PAUSES says an exhausted schedule ends by the seat's adjudication | SURVIVED (help text only) | KILLED, 19/20 | the help check (m's `camp_pauses`) |
| P03 | PRIOR PATH REFUSED names the re-run's checkpoint at the campaign | SURVIVED (message only) | KILLED, 89/91 (integration) | the refusal table (its new case: the prior's name a link to G-TIME-F3's first run's checkpoint) |
| X01 | ruling files accepted at every stage (the guard off) | KILLED, after the untrapped call had run `qual`'s real pre-load path (MINOR-1) | KILLED, 88/91 (integration) | the seam check (each of the six guard calls now reaches a trapped stage, on the stub, in a test root); the final trap count |
| S02 | `_campaign_state`: only a directory is unreadable unopened, so a FIFO is opened | KILLED by hanging (the watchdog, at 6 of 18 checks) | KILLED, 14/20, in 100 s | the four helpers' FIFO checks and the Qwen path's FIFO check (their hang flags); the final check (the hung thread still holds its patches of `stages.DEFAULT_OUT` and `guard.GATES_DIR`) |
| T02 | `ruling_texts`: only a directory is refused unopened, so a FIFO is opened | KILLED by hanging (the watchdog, at 5 of 18 checks) | KILLED, 16/20, in 63 s | the four helpers' FIFO checks (the hang flag) |
| W01 | new: the mirror's PI STOP REFUSED in its pre-fix words (", not PI-stopped") | -- | KILLED, 19/20 | the words check (MINOR-3) |

- *Outcome:* all eleven are killed.
  - The seven round-1 survivors are killed by the new cases and checks.
  - X01 is now killed inside the traps, and S02 and T02 by name within their timeouts, not by hanging.
  - In every run the model-import blocks held (`blocked_imported=[]`), every run printed its end line, and the clone
    changed only in its driver. The mutants' campaign screens ran 31–32 s each (K03 21 s, as it raised; S02 100 s;
    T02 63 s), and the campaign baseline 33 s; the integration runs 127–128 s; the full baseline 166 s.
- *A first pass of round 2* ran on an intermediate candidate (`9aedead9…7324`).
  - It killed all eleven too.
  - Under S02, though, every line after the refusal table went into the hung thread's redirected stdout: 13 checks
    printed, and no end line.
  - The streams fix in NOTE-5's last bullet followed, and round 2 was re-run in full on the final bytes (this
    table). The first pass's outputs are kept in Code's scratch.

## The reviewer's report (verbatim)

# Blind review: the Q-F3 campaign wiring in `scripts/mf3_sessions.py` (candidate `206dc3fc…98b9`)

**Bottom line:** no MAJOR finding. The edit wires `campaign` as the routing (the PI's paste block of 2026-11-15, section A item 6) and the seat's answers of 2026-11-15 (§5 item 2, §2 (a)) say.
- The committed lock must carry v0.2's cap and path lines at a line's start, and v1.0's `launch counts = A1 128, A1s 64, A2 224, A2s 96, A3 224, A3s 96` and `hour cap = 480 h` as whole lines.
- The driver calls `stages.run_campaign` with LOCK-m-F3 v1.0's floors, launch counts and hour cap, G-F3's checkpoint as the prior, and the ruling texts as read.
- NOTE-7's gap is closed as the `qual` review recorded it.
- `time`, `id` and `qual` are unchanged in what they do, print and refuse.
- No production path loads the model, runs a session or writes under `data/mf3` before every pre-load refusal, and none prints a ruling's text, a roster label or a session total.

Findings: 0 MAJOR, 3 MINOR, 8 NOTEs. The most important is MINOR-1: the self-test makes one call outside its traps.

Mutants: 50 one-defect mutants of the production code.
- 43 were KILLED: 41 by a FAIL beyond the baseline's, and 2 by hanging on a FIFO (the harness's watchdog ended them with fewer checks).
- 7 SURVIVED the full self-test, and none of them is strictly equivalent. Two change behavior (K05 and K03: MINOR-2). Five change only a message or help text (S03, L02, P03, M03, G01).

The candidate is the main checkout's working-tree file, sha256 `206dc3fc35bc6ebc6cccb953457abb3d57ff9c0e7fde046d6c1f8cd78d4598b9`. It was compared with HEAD `a89a4fa`'s blob `285eed04…0e44`: 2,897 lines become 4,185, with 1,336 added and 48 removed in 30 hunks. The main checkout's file had that digest at the start and at the end of the review.

Conventions below: bare line numbers are the candidate's; "m" is `scripts/m_sessions.py`; "stages.py" is `valence_core/mf3/stages.py`.

## Findings (most severe first)

**MINOR-1. The self-test makes one call outside its traps.**
- **Where:** `_selftest_campaign`, the seam check. At :3979–3983 it calls `run_stage("qual", **tflags, resume_run=False, adjudication_file=adj_ok)` after the trap stack (:3969–3978) has closed.
  - Nothing is trapped there: no loader trap, no stage trap, no test out root or stub factory, no redirect. `stages.DEFAULT_OUT` is the real `data/mf3`.
  - It is harmless as written only because the guard under test (the ValueError at :1075–1076) fires before anything is read.
- **m's form is safer.** m runs the same case on a fresh test root with a stub factory, "should the guard regress" (m :5510–5533, round 1's M1-7). It covers `time`, `id` and `qual`, both ruling files, and argparse's rejection. mf3 tests `qual` with `--adjudication-file` only.
- **Shown by X01**, the guard turned off:
  - In the clone, the self-test's call ran `qual`'s real pre-load path: the licence against the real hub cache, `pmset` and `pgrep`, and the clone's `data/mf3`.
  - Its REFUSED line went to the real stderr.
  - It was stopped only by `PRIOR STAGE ABSENT` and the driver check. Both are artifacts of a sparse clone holding an uncommitted driver.
- **In the main checkout after the wiring's commit,** the same regression would make the self-test's precheck read G-F3's and G-TIME-F3's checkpoints (`refuse_ended`, `prior_gate`). What would hold off the load is G-F3's checkpoint having ended.
- The function's docstring says "So no case can load the model, run a session on it or write data/mf3" (:3300–3301). That is true only while the guard holds.
- **Fix:** run the case as m does, on a fresh root with a stub factory inside the trap stack. Add `time`, `id` and `--pi-stop-file`.

**MINOR-2. Two of m's precheck behaviors for the campaign are untested.** K05 and K03 survive the full self-test.
- **(a) A ruling offered on a paused campaign without `--resume`.** It must be refused CHECKPOINT EXISTS before the load.
  - The refusal depends on `offered` (:860) through `shown` (:861–862); the PIN is at :786–788.
  - Every Qwen-path case that offers a ruling on an existing campaign checkpoint also passes `--resume`, so nothing exercises it.
  - With `offered = False` (K05), such an invocation clears the precheck, prints the DRIVER, SNAPSHOT and RULING lines, and loads the model.
  - The stage then refuses the existing checkpoint (`stages.py:1492–1493`; `valence_core/mf3/resume.py:256–258`). That is a STOP (exit 4), which goes to the seat. So a missing flag at a pause would cost a 27B load and an escalation.
  - **Kill case:** a paused checkpoint, `--adjudication-file` and no `--resume` → exit 2, "checkpoint: CHECKPOINT EXISTS", the loader not reached.
- **(b) The open-state screen before `stages._paused_unadjudicated`** (:861; m's round-4 F4-2).
  - My probe (`probe_k03.py`, on the candidate) built two malformed checkpoints. A pauses block that is a dict reads `unreadable`, and `_paused_unadjudicated` raises KeyError on it. An int raises TypeError.
  - The precheck catches neither: it catches `SystemExit`, `RuntimeError` and `OSError` (:866–869).
  - With the screen removed (K03), such a checkpoint with no ruling offered crashes the precheck with a traceback (exit 1) before the load, instead of being refused (exit 2).
  - **Kill case:** that checkpoint on the Qwen path with no ruling → exit 2, "cannot be read as a campaign checkpoint".

**MINOR-3. Two sentences of the `campaign_ruling_problems` PIN, carried from m, are not true of mf3.**
- **"Each message is the stage's own words"** (:650–651). These are m's stage's words (`valence_core/m/stages.py:2096`, `:2110–2111`, `:2121–2123`). mf3's `run_campaign` words three of the four differently:
  - CHECKPOINT MISMATCH: the stage says "another text"; the mirror says "a different text" (`stages.py:1507`).
  - PI STOP REFUSED: the stage omits ", not PI-stopped" (`:1516`).
  - SCHEDULE EXHAUSTED: the stage omits "(pi_stop)" (`:1523`).
  - The refusal classes agree, and the classes are all the self-test checks.
- **"which the self-test's stub path, where no precheck runs, shows"** (:657–658). Neither the driver's self-test nor `valence_core.mf3.stages`'s runs the stage on an unreadable or malformed campaign checkpoint. The campaign's stub runs (:3675–3723) cover:
  - PI STOP REFUSED;
  - the interrupt;
  - NO PAUSE TO ADJUDICATE;
  - PI-STOP;
  - CAMPAIGN ENDED;
  - the exit codes, with the stage replaced.
- No behavior is affected.

**NOTE-1. v1.0 §6's quotes and anchors are on the blob of record.**
- One PIN text changes: the `time` wiring's WIRED_CMDS sentence (the PIN at :156, the sentence at :162). v1.0 §6 quotes the old sentence verbatim.
- All 18 earlier sites move, with their other texts unchanged: :102→:156, :112→:165, :119→:172, :138→:191, :154→:207, :183→:302, :193→:312, :306→:441, :313→:448, :318→:453, :432→:802, :440→:810, :452→:822, :529→:923, :554→:948, :638→:1050, :644→:1056, :650→:1062.
- The nine new sites, each declared "at the Q-F3 campaign wiring", are at :227, :257, :433, :580, :645, :720, :751, :784 and :1034.
- As with the `qual` wiring's NOTE-5, the entry, or the next text that cites the driver, would re-quote the sentence and re-anchor the sites.

**NOTE-2. `CAMPAIGN_PAUSES` is not quite "in m's words", and its text is unpinned.**
- Against m's `camp_pauses` (m :7427–7462) it drops three pieces:
  - "(C9(i))" after "the analyzer's declared --adjudication file";
  - "(the seat's adjudication, or a PI stop not recorded with it)";
  - "; where no precheck runs the stage re-finishes the end and then refuses it, NOT APPLIED, exit 4".
- The help check compares the help with the constant itself (:3457–3465). So G01 (a wrong instruction in the text) and M03 (the subparser's `help=` without the text) both survive.
- **Kill case:** read m's `camp_pauses` from its source, as the constants check reads m's constants, allowing the declared differences, and check the top-level `--help` too.

**NOTE-3. The `run_stage` campaign PIN misdescribes `prior_gate`** (:1037–1038). It says "the stage's prior_gate reads it again after the load, with G-ID-F3's artifact".
- At "campaign", mf3's `prior_gate` does not read the artifact; it reads it only at "qual" (`stages.py:517–522`).
- `run_campaign` re-checks the artifact with its own `gid_artifact_problems` call (`stages.py:1484–1487`).
- The phrase is the `qual` PIN's (:1053), where it is true.

**NOTE-4. NOTE-7's original count form is re-created for v1.0's lines.** The values check asserts that each of `CAMPAIGN_LOCK_LINES` occurs exactly once in the committed lock (:3391). A later lock that restated either line would FAIL the self-test while the driver accepted it. The failure would be loud, never a false PASS.

**NOTE-5. The FIFO safety cases detect a regression only by hanging.** Under S02 and T02, the self-test opens its FIFO and blocks. My harness's watchdog ended each run at 300 s, with 6 and 5 checks run. A plain `--selftest` would hang, not FAIL.

**NOTE-6. Dead code.** With `REFUSED_CMDS` empty, `refusal()` (:329), the refused-subparser loop (:4154) and its branch (:4177) are unreachable.

**NOTE-7. The docstring's excerpt sentence** (:108–110) says the excerpt is written "when a pause or a stop is recorded". The stage writes it when the checkpoint records a pause or a STOP (`stages.py:1717–1747`). A PI-STOP with no pause writes none, so "a stop" reads best as "a STOP".

**NOTE-8. The campaign's starting backend is not checked against v1.0 §5** (outside the spec; m's form).
- Neither driver nor the stage library compares the backend a campaign starts on with v1.0 §5's identifier, `a734dadec8f8ce9b`.
- The checkpoint's identity binds whatever backend the first launch reports, and resumes must match it. So the campaign completes on one backend, but not necessarily §5's.
- The campaign's report identity prints the identifier, so the launch entry can compare it.

## Answers by question

**1. The spec.**
- `campaign` is wired (:163). It reads the committed lock's text (`stages.committed`) and requires:
  - `CAMPAIGN_LOCK_LINES` as whole lines (:503–507);
  - `QUAL_LOCK_LINES` at a line's start (:496–502).

  Both checks come before the m files and the weights are read.
- The values are the driver's constants (:250–253), and the line test ties them to the lock. This is m's form, with the seat's line test in place of m's substring test.
- **One difference from the letter, correct and declared:** the test is whole-line equality, which is stricter than the `qual` wiring's line-start test (PIN :433–439). §2 (a)'s "whole lines" needs it: a line-start test would accept "hour cap = 480 hours" or a longer count line.
- **NOTE-7 is closed** (question 6).
- **F-1 holds:** in the clone, `git diff --name-status` against `a89a4fa` names `scripts/mf3_sessions.py` alone, so G-SHAPE-F3 needs no re-run.
- **Nothing is missing from the code.** The entry-level items (the edit, the new DRIVER blob, the one line about v1.0 §6) belong to the entry; add NOTE-1's re-quote there.

**2. The ports.** `compare_ports.py` (text only) diffs the function bodies against m's:
- `_campaign_state`, `campaign_ruling_problems` and `ruling_line` differ only in their module bindings (mf3's `stages` and `rs`) and the arm set (`keys.TEMPLATES`, Q-F3's six arms).
- `ruling_texts` is identical, and `campaign_floors` reads mf3's `schedule.FLOORS`.
- `stage_precheck`'s campaign parts are m's, with the prior read through `stage_prior_checkpoint` and `gid_artifact_problems` at the run's cap (`require_real` on).
- The subparser's two flags carry m's help verbatim, and the docstring carries VC4-1, VC4-2, O4-1, O1-3 and RM4-1.
- `run_campaign` is called (:1155–1160) with:
  - floors {A1 80, A1s 32, A2 144, A2s 56, A3 144, A3s 56}: `schedule.FLOORS` under "uncached", v1.0 §1, and G-PWR's `inputs.floors`;
  - launch counts {A1 128, A1s 64, A2 224, A2s 96, A3 224, A3s 96}: v1.0 §1 and G-PWR's `launch.L`;
  - the hour cap, int 480: v1.0 §2 (mf3.resume takes hours);
  - the prior `<root>/ckpt/Q-F3_qual.json`, resolved by `checkpoint_path` (`PRIOR_STAGE["campaign"]` is "qual"; m passes the same path unresolved);
  - the stage's default checkpoint, the resume flag, and the two ruling texts as read, unstripped (the stage strips them);
  - G-F3's identity: cap 120 and `locked_path` uncached, validated by `_extra(stub=False)`.

**3. Safety.**
- On the Qwen path, the order is:
  1. flags;
  2. the out-root seam;
  3. the identity;
  4. the ruling files (`ruling_texts`; a FIFO is refused unopened);
  5. the precheck, the driver check and the snapshot check, refused together (exit 2);
  6. the DRIVER line, the SNAPSHOT line, then the RULING line;
  7. the load;
  8. the re-read and the model-id check;
  9. the stage.
- `main` never passes `adapter_factory`, so the loader is reachable only past every refusal. `say_ruling` runs inside the `try`, so a CHECKPOINT PATH REFUSED there is a STOP before the load.
- **No ruling text is printed.** Refusals give the flag, the path and an exception class. The RULING line and the mirror give only sha16s, kinds, launch counts and arm names, and the summary carries no text.
- **No total is printed.** Every REFUSED and STOP line passes through `redact_totals`, and the RULING line has no totals.
- The self-test's one hazard is MINOR-1.

**4. The other stages.** I read all 30 hunks. Every shared line is keyed, so `time`, `id` and `qual` take their old path:
- `WIRED_CMDS` gains campaign, and so do the lock and cap dicts.
- The line-start check runs for qual and campaign. Its message now names `stages.stage_name(stage)`, which is "G-F3" for qual, so qual's text is byte-identical. The whole-line check and the `locked_path` branch are campaign-only.
- `stage_prior_checkpoint` keeps the same names and the same PRIOR PATH REFUSED text for id and qual.
- In `stage_precheck`, `rulings` defaults to None and `shown` short-circuits on `stage == "campaign"`, so no new read or condition reaches the other three. The prior block only adds campaign.
- In `run_stage`:
  - the ruling ValueError needs a file, which `main` never gives the other stages;
  - `ruling_texts(None, None)` reads and refuses nothing;
  - `say_ruling` prints only for the campaign;
  - the former `else` is now `elif stage == "qual"`, with identical arguments.
- `main` builds the other subparsers identically. Only the top-level description and the no-action line change.
- In the baseline, every `time`, `id` and `qual` check passes; the one FAIL is the constants check.

**5. The PIN texts.** The nine new sites and the revised sentence are accurate about their code, except where MINOR-3, NOTE-2, NOTE-3 and NOTE-7 say otherwise. I checked these against the code and the lock:
- the CAMPAIGN_* PIN, whose quotes of section A item 6 and §2 (a) are verbatim;
- the order and contents of the identity, precheck and `run_stage` PINs;
- `_campaign_state`'s list of unreadable forms;
- `ruling_line`'s digest and placement claims;
- `ruling_texts`' rules.

**6. NOTE-7.** Closed as recorded:
- The "moved" and "indented" variants use `_lines_prefixed`, which edits every line that opens with the path line (:2782–2783).
- The check asserts that no such line is left (:2795).
- A new check (:2801–2814) plants a restatement above v0.2's line. The line-wise variant is refused there, where the first-occurrence form would have left v0.2's line.
- The campaign's own variants edit every line that opens with, or equals, v1.0's lines (`_lines_prefixed`, `swap`, `drop`).
- The committed lock has no line break other than LF, so the helper's `split("\n")` and the driver's `splitlines()` agree. The check's own assertion uses `splitlines()`, so any divergence would FAIL loudly.
- What remains is NOTE-4.

**7. The self-test.** See the mutant table below.

## Mutant table

There are 50 one-defect mutants. Each is an exact single replacement, asserted to occur once and outside the self-test region (`_short` … `run_selftest`), and each compiles.
- **Screens:** the campaign part (18 checks) for campaign-only code, and the integration self-test (89 checks) for shared lines.
- **Confirmations:** every screen survivor was re-run through the full self-test (233 checks).
- **Baselines under the block:** campaign 18/18, integration 88/89, full 232/233. The one FAIL is the constants check, which reads mlx_lm's source while the harness blocks it.
- **KILLED** means any FAIL beyond the baseline's, or fewer checks.

Check names used in the table:
- "values": the campaign's values;
- "identity": the campaign's identity;
- "variants": the nine lock variants;
- "order": the line checks come first;
- "ruling_texts": the ruling files;
- "state": `_campaign_state`;
- "mirror": `campaign_ruling_problems`, 19 cases;
- "RULING line": `ruling_line`;
- "stub chain": time, a FAILed id and G-F3, then the campaign, all on the stub;
- "exit codes": the campaign's exit codes;
- "refusal table": the 40 pre-load refusals;
- "joined line": the precheck problems refused together in one line;
- "seam": the out-root seam;
- "load reach": the five cases that reach the loader trap;
- "post-load": the three post-load STOPs;
- "post_ok": the stage call after the load;
- "trap count": the final count of trap reaches.

| mutant | defect (line) | screen | result | killed by / why it survived |
|---|---|---|---|---|
| C01 | CAMPAIGN_HOUR_CAP 480 → 48 (:251) | campaign | KILLED 8/18 | values; identity; 8 more downstream |
| C03 | A1's launch count 128 → 129 (:250) | campaign | KILLED 8/18 | values; identity; 8 more downstream |
| C05 | CAMPAIGN_LOCKED_PATH "cached" (:254) | campaign | KILLED 14/18 | values; identity; stub chain; post_ok |
| C07 | CAMPAIGN_PRIOR_CKPT_NAME = the re-run's name (:256) | campaign | KILLED 16/18 | values; stub chain (the Qwen-path cases plant G-F3 at the constant's path) |
| F01 | campaign_floors reads A1's cached floor (:426) | campaign | KILLED 17/18 | values |
| I01 | the line tests skipped for the campaign (:496, shared) | integration | KILLED 85/89 | variants; order; refusal table |
| I02 | the whole-line test made a substring test (:503) | campaign | KILLED 17/18 | variants |
| I03 | the whole-line test made a line-start test (:503) | campaign | KILLED 17/18 | variants |
| I10 | the line-opening refusal names G-F3 at every stage (:501, shared) | integration | KILLED 87/89 | order (its "campaign-Q-F3" conjunct alone) |
| I11 | the whole-line check moved after the m-file and WEIGHTS reads (:503–511) | campaign | KILLED 17/18 | order |
| P01 | the prior-name dict gives the campaign the re-run's checkpoint (:562, shared) | integration | KILLED 82/89 | stub chain; refusal table; load reach; post-load; post_ok; trap count |
| P03 | PRIOR PATH REFUSED names the re-run's checkpoint at the campaign (:565, shared) | integration; full | SURVIVED 88/89; 232/233 | gap, message only: no campaign case links the prior path to the first run's checkpoint. Kill: link `<root>/ckpt/Q-F3_qual.json` to `Q-F3_time.json` and expect "takes G-F3's, Q-F3_qual.json" |
| S01 | m's arms (A0, A0s) admitted instead of Q-F3's (:612) | campaign | KILLED 14/18 | state; mirror; refusal table; trap count |
| S02 | only a directory is unreadable unopened, so a FIFO is opened (:596) | campaign | KILLED (hang) | blocked in the state check's FIFO case; the watchdog stopped it at 300 s with 6 of 18 checks run |
| S03 | an end_look pause read as unreadable (:610) | campaign; full | SURVIVED 18/18; 232/233 | gap, message only: an end_look pause is written only with a terminal end or a STOP (`m.resume.apply_end`), so its checkpoint has ended and is refused before the load either way; only an extra "cannot be read" problem differs. Kill: `_campaign_state` on an ended checkpoint carrying an end_look pause → "ended" |
| S06 | ruling_sha16s omits the last pause's ruling (:628) | campaign | KILLED 16/18 | mirror; RULING line |
| S07 | launched always True (:620) | campaign | KILLED 17/18 | mirror |
| R01 | an ended checkpoint not skipped (:662) | campaign | KILLED 17/18 | mirror |
| R03 | O4-1 refuses the stop the checkpoint records (:681) | campaign | KILLED 17/18 | mirror |
| R04 | O4-1 dropped (:682) | campaign | KILLED 15/18 | mirror; refusal table; trap count |
| R06 | SCHEDULE EXHAUSTED ignores the PI's stop (:695) | campaign | KILLED 17/18 | mirror |
| R07 | O1-3 digests the unstripped text (:701) | campaign | KILLED 15/18 | mirror; refusal table; trap count |
| R08 | O1-3 dropped (:700) | campaign | KILLED 15/18 | mirror; refusal table; trap count |
| L01 | the RULING line digests the unstripped text (:728) | campaign | KILLED 15/18 | RULING line; stub chain; load reach |
| L02 | the RULING line reads the last pause in any state (:734) | campaign; full | SURVIVED 18/18; 232/233 | gap, message only, on the stub path alone: it differs only on an ended checkpoint whose last pause is unruled, which the Qwen-path precheck refuses before the RULING line (a pending checkpoint's last recorded pause is always ruled). Kill: `ruling_line` on such a checkpoint → "on an ended campaign" |
| L03 | RM4-1's note dropped (:744) | campaign | KILLED 17/18 | RULING line |
| T01 | utf-8 instead of utf-8-sig, so a BOM is kept (:769) | campaign | KILLED 17/18 | ruling_texts |
| T02 | only a directory refused unopened, so a FIFO is opened (:766) | campaign | KILLED (hang) | blocked in ruling_texts' FIFO case; the watchdog stopped it at 300 s with 5 of 18 checks run |
| T03 | control and format characters count as visible (:773) | campaign | KILLED 17/18 | ruling_texts |
| T04 | the text is stripped rather than passed as read (:776) | campaign | KILLED 16/18 | ruling_texts; post_ok |
| K02 | a paused campaign offered no ruling is never "shown" (:861) | campaign | KILLED 16/18 | load reach; trap count |
| K03 | the open-state screen before `_paused_unadjudicated` removed (:861–862) | campaign; full | SURVIVED 18/18; 232/233 | gap, behavior (MINOR-2b) |
| K05 | `offered` always False (:860) | campaign; full | SURVIVED 18/18; 232/233 | gap, behavior (MINOR-2a) |
| K06 | the precheck's prior block for id and qual only (:870, shared) | integration | KILLED 85/89 | refusal table; joined line; trap count |
| K09 | the unreadable-checkpoint screen dropped (:886) | campaign | KILLED 15/18 | refusal table; joined line; trap count |
| K10 | the not-a-regular-file screen dropped (:884) | campaign | KILLED 17/18 | refusal table (the directory case's message) |
| K13 | the G-ID artifact checked with require_real off (:896) | campaign | KILLED 16/18 | refusal table; trap count |
| X01 | ruling files accepted at every stage (:1075, shared) | integration | KILLED 87/89 | seam, after the self-test's untrapped `qual` call had run the real pre-load path (MINOR-1) |
| X02 | ruling_texts' problems not refused (:1093) | campaign | KILLED 16/18 | refusal table; trap count |
| X03 | the precheck given no rulings (:1107) | campaign | KILLED 16/18 | refusal table; trap count |
| X06 | the RULING line before the SNAPSHOT line (:1122–1123) | campaign | KILLED 17/18 | load reach (the order) |
| X07 | no RULING line on the stub path (:1140–1142) | campaign | KILLED 17/18 | stub chain |
| X08 | the launch counts passed as the floors (:1155) | campaign | KILLED 16/18 | stub chain; post_ok |
| X10 | the hour cap passed as a float (:1156) | campaign | KILLED 17/18 | post_ok (its type conjunct alone) |
| X11 | the stage's prior is G-TIME-F3's re-run checkpoint (:1157–1158) | campaign | KILLED 16/18 | stub chain; post_ok |
| X14 | the stage's out root is stages.DEFAULT_OUT (:1159) | campaign | KILLED 17/18 | stub chain |
| X15 | the campaign routed to run_gate_stage (:1150, shared) | integration | KILLED 84/89 | stub chain; exit codes; post_ok; trap count |
| M01 | main never passes the ruling files (:4172, shared) | integration | KILLED 84/89 | refusal table; load reach; post_ok; trap count |
| M03 | the campaign subparser's help= without CAMPAIGN_PAUSES (:4128) | campaign; full | SURVIVED 18/18; 232/233 | gap, help text only: the check reads `campaign --help`, which shows the description. Kill: assert the text in the top-level `--help` |
| G01 | CAMPAIGN_PAUSES says an exhausted schedule "ends by the seat's adjudication" (:261) | campaign; full | SURVIVED 18/18; 232/233 | gap, help text only (NOTE-2) |

The thinnest kills each rest on a single conjunct: I10, X10, X06, X07 and X14.

## Method

**Work directory** (relative names):
- `clone/`, deleted at the end;
- `harness.py`, `run_one.sh`, `run_batch.sh`;
- `gen_mutants.py`, and `mutants/` with 50 files and `manifest.tsv`;
- `runs/` with 61 outputs, `screen_results.txt` and `confirm_results.txt`;
- `edit.diff`, `candidate.py` and `head_driver.py`;
- `compare_ports.py`, `pin_anchors.py` and `probe_k03.py`.

**The clone.**
- I made it with the brief's commands: `--no-checkout --no-hardlinks`, the sparse patterns `'/*' '!/data/*/ckpt/' '!/data/*/reports/'`, and a checkout of `a89a4fa`.
- A name-only `ls` showed no `ckpt` or `reports` in `data/mf3` or `data/m`.
- I copied the candidate in and checked its sha256.
- The clone's `git diff -- scripts/mf3_sessions.py` equals the main checkout's byte for byte (sha256 `c6dc0cab…ad97` for both).

**Commands in the main checkout** (read-only):
- `shasum -a 256` of the working driver, at the start and at the end;
- `git rev-parse HEAD`;
- `git show HEAD:scripts/mf3_sessions.py | shasum -a 256`;
- `git log --format='%h %s' -3`;
- `git diff -- scripts/mf3_sessions.py`, saved as `edit.diff`;
- `cp` of the working driver into the clone;
- a name-only `ls` of `jlens-qwen36/.venv/bin` to find the interpreter (no git command there).

Every source was read in the clone, at `a89a4fa`.

**Commands in the clone:**
- `git sparse-checkout` and `git checkout`;
- `git diff --name-status`;
- `git status --porcelain` after every harness run; each showed only the driver;
- `git show a89a4fa:scripts/mf3_sessions.py`, the driver blob, for the PIN map;
- files read by path, and `sed -n` excerpts;
- `/usr/bin/grep` over named files only: the lock, RESULTS.md, both drivers, mf3's and m's `stages.py`, `resume.py` and `guard.py`, mf3's `schedule.py` and `keys.py`, the `valence_core/mf3/*.py` glob, and `valence_core/adapters/__init__.py`;
- `wc -l` of named files;
- a JSON read of G-PWR's record (`launch.L`, `inputs.floors`).

**Python.**
- Every run used the venv's interpreter by its absolute path, with `-I -B` and `HF_HUB_OFFLINE=1`.
- `harness.py` and `probe_k03.py` first install a `sys.meta_path` finder refusing mlx, mlx_lm, mlx_vlm, torch and transformers, before anything else is imported. They then import the clone's driver by path as `mf3_sessions`, and at the end assert that no blocked module was imported. Every run printed `blocked_imported=[]`.
- Inside the integration and full runs, the self-test spawned its own fresh-interpreter import check (`-I -B`, mf3's production modules only).
- The harness has a watchdog (SIGALRM at 300, 600 and 900 s, by mode) that ends a hung run with fewer checks.
- I ran one harness process at a time, checked with `pgrep` before each run.
- Each mutant was copied over the clone's driver and run; the candidate was then copied back and its digest checked after every run.

**Baselines** (in the clone, under the block):
- the campaign part: 18/18, in 28 s;
- the integration self-test: 88/89, in about 2 min;
- the full self-test: 232/233, in about 3 min.

The 233 checks are the `qual` wiring's 214, plus `_selftest_campaign`'s 18, plus NOTE-7's new check in `_selftest_qual`.

**Timings:**
- 42 campaign screens, about 29 s each; S02 and T02 took 300 s each, until the watchdog;
- 8 integration screens, about 2 min each;
- 7 full confirmations, about 2.8 min each;
- about 70 min of harness time in all.

## What I did not do

- **No model was loaded.** No stage or subcommand ran outside the self-test's traps, with one deliberate exception. X01 let the self-test's untrapped `qual` call run in the clone, with the import block in force. It read the hub cache's `refs/main` and snapshot link names (no weight bytes), ran `pmset`, `pgrep` and a disk check, and refused before the load.
- **Killed mutants were not re-run** through the full self-test; they were screened only.
- **K03's crash was not run end to end.** It rests on the probe's two calls on the candidate, which show its mechanism, not on a Qwen-path run of the mutant.
- **Not reviewed:** the stage library (unchanged), the entry (not yet written), and the PI's paste block (not in the repository; I took its text from the brief).
- **No file under `data/*/ckpt` or `data/*/reports` was read, listed or hashed.** The clone has none.
- **Nothing in the repository was changed.** No `git status` ran in the main checkout, and no git command ran in `jlens-qwen36/`.
- **Two text-only scripts overlapped harness runs.** `compare_ports.py` and `pin_anchors.py` (stdlib only, importing no repository module) ran while a harness run was in progress.
- **Outside the work directory,** the only writes were the self-test's own temporary directories, which it removed.
