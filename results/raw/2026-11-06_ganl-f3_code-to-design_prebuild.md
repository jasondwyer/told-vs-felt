# G-ANL-F3 (m:291): Code's pre-build block — STOP before the first edit to `scripts/m_analyze.py` (2026-11-06)

*Code to the design seat, through the PI. The routing is the prebuild answers' §9 item 2: "G-SHAPE-F3 → G-ANL-F3 under Q3's rule → the lock chain to LOCK-m-F3 v0.2" (answers:63), under the PI's routing of 2026-11-06, "Run the prebuild answers as written". The coordinating session relayed it after G-SHAPE-F3's commit. `m:N` = PROPOSAL-m v1.11 at root (sha256 `42ab36ec…6c6b`); `A-m1` = ADDENDUM-m1 v0.1 (`f26bc59`); `answers:N` = `results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md`. Nothing is written to `scripts/m_analyze.py`; HEAD is `1bf94a6`.*

## 0. Where it stands

- **Done:** `cd9756e` (m package — BUILD (F3)) and `1bf94a6` (G-SHAPE-F3, PASS), both local and not pushed.
- **The calendar fact for Q3:** no `LOCK-m-OLMo-*.md` exists at HEAD or in the tree. The coordinating session reports no pod up: its pod watch found no Secure A100 stock in US-CA-2 at any check today, the latest at 18:56. So order (a) is open. The STOP does not fix either order. If the pod comes up before G-ANL-F3 commits, order (b) obtains: which order obtains "is a fact of the calendar that Code records in the BUILD entry" (answers:26). The seat recommends (b) for that case (answers:26), and the pod starts only on the PI's go (RESULTS.md@1bf94a6:271).
- **Why Code stops:** three places where building the record as written is either impossible or needs a reading that changes what the analyzer asserts or reads. Q1 and Q2 decide what the battery asserts, and Q1 also touches a blinding PIN of the analyzer of record. Q3 decides the build's scope. Every other open reading is Code's proposed reading: it goes into the build-design raw, is declared as Code's PIN at LOCK-m-F3 v0.1, and stays strikable by the seat until LOCK v1.0 (Q8's register, answers:50). They are listed in §3.

## 1. What G-ANL-F3 is, from the record

- **m:291.** `m_analyze.py` extended, pre-committed (in place: the seat's Q3, answers:25), with a battery that does three things:
  - (i) reaches every per-arm outcome of §5 for A1, A2 and A3, including NOT-RUN, NO-READ, NULL-x↑ and NULL-x↓, and every value of A3\*;
  - (ii) enumerates the v2 outcome space, 481 × 5 × 216 = 519,480 tuples, asserting for each "exactly one" A3\*, licensing state, label set, abstract OLMo clause, dose-note text, ceiling, withholding value, v1-note disposition, Step-6 text, Step-7 status, §8.1/§8.2 status text and §7.5 enumeration;
  - (iii) fixes counter (c)'s scorer and lexicons (§4).
- **A-m1 §2.5 (A-m1:44)** names three riding items: (1) the CLI-path reading; (2) the Clock dates D1, D_O′ (2026-11-30, A-m1:28) and D2 (2026-12-22, A-m1:40) as declared inputs; (3) the byte-for-byte regression of `Q-F0_VERDICTS.json` and `Q-F0_secondary.json`. The prebuild answers' Q3 (answers:23–27) adds the rule, the two orders and, under (a), "asserts the OLMo v1 outputs unchanged".
- **The other riding texts**, by record anchor, are those the BUILD (F3) entry lists (RESULTS.md, the `cd9756e` entry): the VERDICTS read §4 item 2 (`results/raw/2026-10-19_m-design-to-code_VERDICTS_read.md:83`), and round 2's standing rule (`results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1_round2.md:19`). The seat confirms them by anchor before LOCK-m-F3 v0.1 (answers:27). None of them is a question here.

## 2. The questions

### Q1. The regression (A-m1 §2.5 (3); answers:26 (a)): as written, it cannot pass. What form does the seat want?

**The record.** A-m1:44: "from the committed inputs of 2026-10-19 (the campaign checkpoint, the table of record, `Q-F0_olmo-states.json`, `Q-F0_decisions.json`, the lock), the extended analyzer reproduces `data/m/verdicts/Q-F0_VERDICTS.json` and `Q-F0_secondary.json` byte for byte — a non-reproduction is a STOP (rule 26's form)". It also says "a regression assertion in the extended battery". The answers carry N8's reading (the D_O-era declarations left as they were; `results/raw/2026-11-06_m1-v0_1_referent-check.md:213–217`).

**Three facts at source that the record does not resolve for the regression.** The record touches the first two: answers:21 ("LOCK-m-F0 v1.0's `package_sha256` (`5f646db6…`) is Q-F0's record; … `posting` records the three shas without refusing, so a moved package does not block the v1 posting") and answers:25 (PIN-14 binds each unit's analyzer of record; "the worktree path is declared and not implemented, and nothing below needs it"). Neither says how the regression reproduces the three identity fields or reads under PIN-29's roots.
1. **The output names the analyzer that wrote it.** `Q-F0_VERDICTS.json` embeds `analyzer_sha256` `655e0f7f…c16f`, `closure_sha256` `a3bc7bb9…b22b` and `package_sha256` `5f646db6…d771`.
   - Any edit to `m_analyze.py` changes the first.
   - G-ANL-F3's Q-F3 reader will import mf3, which changes the second.
   - The third already moved, to `60199b36…feec`, at the OLMo build (`71cc23c`), whatever G-ANL-F3 does.
   - So no extended analyzer reproduces those three fields as itself.
2. **The extended analyzer cannot run Q-F0's VERDICTS under LOCK-m-F0 v1.0.** `run_verdicts` refuses unless the lock's text names the run's analyzer sha256, `package_sha256` and closure sha256 (PIN-14, `scripts/m_analyze.py:1934–1944`). LOCK-m-F0.md:147–149 names `655e0f7f…`, `5f646db6…` and `a3bc7bb9…`. PIN-14's own text foresees the case ("otherwise from a worktree of the lock commit …, on the PI's word for the worktree (git writes; not implemented at step 8)"). Even the analyzer of record, re-run today, is refused, because the package moved.
3. **The battery may not read the files the regression needs.** PIN-29 makes the battery (`--selftest` and `ganl`) refuse any read under `data/m/ckpt`, `data/m/reports`, `data/m/verdicts` or `results/raw` (`scripts/m_analyze.py:97`, `:3231–3250`; register text `:2897–2900`). The regression's inputs (the campaign checkpoint) and outputs of record (`data/m/verdicts/`) are under those roots. Q-F0's picks are released (its VERDICTS of 2026-10-19), but the hook is by directory.

**Code's recommendation: (R1), a battery check that pins the computation, not the binding.** In-process, the extended analyzer's VERDICTS computation runs on the committed inputs with the run's identity bound to the record's. Specifically:
- the analyzer bytes are served as the blob the lock names, read with `git cat-file` at `ed8e886` and asserted to hash to `655e0f7f…`;
- the package and closure hashes are the lock's, asserted against LOCK-m-F0.md's text;
- PIN-14's check runs against those;
- the open hook admits exactly the seven files of record under its roots, each by path and by its committed blob's sha256 at HEAD, and nothing else there (a declared PIN-29 exception for Q-F0's released files). The seven are the campaign, time and qual checkpoints (`data/m/ckpt/Q-F0_{campaign,time,qual}.json`), the decisions and OLMo-states declarations (`data/m/verdicts/Q-F0_{decisions,olmo-states}.json`) and the two outputs. A-m1's list names five inputs; the VERDICTS of record also read the time and qual checkpoints and the flag source (`Q-F0_VERDICTS.json`'s `inputs` and `flag`), so the regression reads them too;
- then the bytes are compared: equal passes; any difference is a STOP, as A-m1 says.

What (R1) shows: with the inputs pinned by sha256 and the identity fields bound to the record's, the code now computing the verdicts (the extended analyzer, on the moved package `60199b36…`) reproduces Q-F0's outputs to the byte. What it does not show: that the new blob would be accepted by LOCK-m-F0's binding. No blob but `655e0f7f…` can be.

**The alternatives:**
- **(R2)** Compare every field except the three identity fields, which are reported beside.
- **(R3)** Run in a worktree of the lock commit, as PIN-14 foresees. That is git writes on the PI's word, and it tests the analyzer of record, not the extended one; the seat's Q3 also has the worktree path "declared and not implemented, and nothing below needs it" (answers:25). So Code does not recommend it.

Either (R1) or (R2) needs the PIN-29 exception. (R2), like (R1), must also get past PIN-14 (fact 2). With LOCK-m-F0.md as the lock, the extended analyzer is refused. With a battery lock text naming its own hashes, as the battery's verdicts cases build one (`scripts/m_analyze.py:4799–4802`), `inputs.lock` (path and sha256 `fc7e9db8…`) also differs from the record, so "every field except the three" fails on it. The seat's ruling is asked on both. Under each, "asserts the OLMo v1 outputs unchanged" (answers:26) is read as: the 1,080 v1 tuples' outputs from G-ANL-F0's battery are reproduced by the extended analyzer, value for value, under both flag values.

### Q2. PENDING in the v2 coordinate (m:291 "OLMo 6³"; m:324). What does a v2 tuple with a PENDING checkpoint assert?

**The record.**
- m:291 enumerates v2 with "OLMo 6³", the six values of m:278 (PASS, REVERSE, DEAD, INDETERMINATE, NOT-RUN, PENDING). Each tuple asserts "exactly one" label set, abstract OLMo clause, ceiling and so on.
- m:324 (§5), STOP-8's C2 (m:145): "A checkpoint still PENDING at the v2 posting is closed there: PI-stopped and analyzed as obtained if it has sessions, else NOT-RUN with the reason recorded".
- Step 2's OLMo label carries the branch "is pre-registered and pending at this posting" (m:338), and "A row PENDING at v1 is re-labeled at v2" (m:338).
- m:343 lists "pending" among §8.1's status words "At each posting", v2 included.
- The analyzer of record already carries the closure as a v2-only OLMo NOT-RUN cause, `pending-closed-at-v2` ("still pending at the v2 posting, with no session"; cite "m:324 closed there ... else NOT-RUN with the reason recorded"; `scripts/m_analyze.py:413–415`), and refuses that cause at v1 as "the v2 posting's (G-ANL-F3)" (`:2467–2468`; PIN-38, `:2925–2927`). Neither reconciles the 6³ count with the closure.

**The conflict.** By m:324 no checkpoint is PENDING at the v2 posting. The closure maps it to one of the other five values, which are already in the 216. So the 6³ count either counts PENDING tuples whose outputs the v2 posting can never use, or means something the record does not say. Code finds no text that reconciles them; STOP-8's disposition of C2 (m:145) points to §5 only.

**The readings Code sees:**
- **(P1), Code's recommendation.** At v2 a PENDING coordinate asserts a refusal: the v2 outputs refuse it (Code's refusal text, "closed at the v2 posting first", citing m:324, whose words are "is closed there") and produce none. The closure itself runs upstream: a checkpoint with no session becomes NOT-RUN by the analyzer of record's `pending-closed-at-v2`, one with sessions is analyzed as obtained. The battery asserts that refusal on each of the 481 × 5 × (216 − 125) = 218,855 tuples with a PENDING checkpoint. The other 481 × 5 × 125 = 300,625 assert the full output set. The count stays m:291's, and "a skipped assertion is a failure" holds because each PENDING tuple asserts its refusal.
- **(P2)** A PENDING coordinate at v2 is the v1-style row: label "is pre-registered and pending at this posting", the clause counting it as not passing. This contradicts m:324's closure.
- **(P3)** The seat re-counts v2's space with 5³: 481 × 5 × 125 = 300,625 tuples, a text change to m:291's count by addendum.

### Q3. The build's scope: the v2 `posting` command, the v2 placeholder table and the Q-F3 `verdicts` reader. Are all three G-ANL-F3's?

**The record.**
- m:291 asks for "one §7.5 enumeration over the declared table under the declared 0.12-artifact flag".
- m:73 says v2's sentence table of record is "built and hashed … at LOCK-m-F3 v1.0".
- The seat's Q7, confirmed by the PI, moves v2's table to "the Q-F3 VERDICTS session, which under (10′) follows `POSTING v1`, against the posted v1 text" (answers:46).
- G-ANL-F0's analog used "a placeholder table for the battery" (m:278), and its analyzer carries `posting --posting v1` (usage at `scripts/m_analyze.py:27–34`; the parser's `choices=["v1"]` at `:8198–8199`).
- §7.5 has Code enumerate the v2 sentences "by the pre-committed analyzer where it exists" (m:349).
- A-m1 §2.3: the Q-F3 VERDICTS session is "the analyzer run over the campaign checkpoint" (A-m1:40).

**Code's reading:**
- G-ANL-F3 builds all three, pre-committed, before LOCK-m-F3 v0.1 names the blob (m:292):
  - `verdicts --unit Q-F3` over mf3's checkpoints (data/mf3/ckpt; mf3's record format; mf3's keys, as the seat's Q1 has it: "the extended analyzer reads Q-F3's keys from `mf3`", answers:15);
  - `posting --posting v2` under a declared v2 tuple, with f2's outcome a declared input (f2 is its own pre-registration, m:340);
  - a v2 placeholder table for the battery, with the v2 table of record a declared input built at the Q-F3 VERDICTS session (Q7).
- The battery enumerates over the placeholder, as G-ANL-F0's did.
- **The alternative:** G-ANL-F3 builds only (i)–(iii) of m:291 and the regression, and the `verdicts` and `posting` extensions come in a later hash-moving round before LOCK-m-F3 v1.0. That moves the blob a second time after LOCK-m-F3 v0.1 names it, which a lock revision can absorb (LOCK-m-F0's analyzer moved twice between v0.1 and v1.0, LOCK-m-F0.md:153–158). Under (a) it also moves the blob after the OLMo locks name it. Q3's rule is worded for G-ANL-F3's in-place commit ("lands only when no OLMo unit is open", answers:26); Code reads it as barring any later in-place analyzer commit while an OLMo unit is open, which PIN-14's binding (answers:25) also implies. So Code recommends building all three now.

## 3. Code's readings, to be declared as PINs at LOCK-m-F3 v0.1 (strikable until LOCK-m-F3 v1.0; listed so the seat can strike any now)

1. **A1, A2, A3 (§5, m:326):**
   - A1 uses `arm_outcome` at α .01 with A1s as its sham.
   - A2 is the same, with FAIL for DEAD and A2s as its sham.
   - A3 is a new `a3_outcome` at α .05 in m:326's order: NO-READ → REVERSE → POSITIVE → NULL-x↑ / NULL-x↓ ((i) and (iii) in one direction, (ii) failing there) → NULL. A3s is its sham.
   - A3's NULL sentence quotes the power figure of record for the realised n (exact, as PIN-3; .927 at P = .65 at the planned floors).
2. **Q-F3's unit composition and NOT-RUN causes (m:324):** the Clock is D2. The causes, as the analyzer of record's PIN-5 has them for Q-F0 (`scripts/m_analyze.py:384–417`):
   - a gate STOPPED with no re-specification locked;
   - a blocking stage not at its end with no LOCK v1.0 by D2 (m:347: "A Q-F3 not locked by D2 is NOT-RUN"; m:324: "or any reason"; the seat's C1);
   - the PI declining;
   - k = 0 at G-F3, so no launch count (m:192);
   - no session reaching a first read before a PI stop, a G-VER STOP or the cap (m:324).
   Q-F3 NOT-RUN sets L1 = false (m:341).
3. **A3\* (Step 4, m:340):** a total function of (screen A3, f2's coordinate, f2's control), with f2's no-hit value "f2 not required" (m:73). Its values are seven: the screen's four non-hit values (NULL, NULL-x↑, NULL-x↓, NO-READ), carried when the screen is not a hit, plus CONFIRMED, DISCORDANT and UNLICENSED. POSITIVE and REVERSE are never values of A3\* (m:340; m:342).
4. **The withholding value:** "not withheld" when the screen is not a hit. Otherwise it is "released at f2's VERDICTS" or "released at f2's NOT-RUN".
5. **The v1-note disposition:** m:291's six values (none, confirmed, discordant, not replicated under a passing control, unlicensed, not run). It is "none" for every no-hit tuple, as m:73 and m:291 declare. A DISCORDANT result maps to "discordant"; f2's null under a passing control to "not replicated under a passing control"; f2's null-class result under a failing control or f2 NO-READ to "unlicensed"; and f2 NOT-RUN to "not run" (m:340).
6. **Steps 5, 6 and 7 at v2:** clause by clause, as m:341–343 write them. The direction words come from the tuple:
   - [clean | corrupted]: POSITIVE and NULL-x↑ point toward clean; REVERSE and NULL-x↓ toward corrupted; CONFIRMED and DISCORDANT follow the screen's direction.
   - Step 6's power figure is a declared slot filled from the VERDICTS data at posting: f2's when f2 ran, else the screen's.
7. **Counter (c) (§4, m:312):**
   - the lexicons and window as m:312 lists them, frozen in the analyzer;
   - tokens: lower-cased, punctuation stripped, whitespace-split;
   - ties by token distance are ambiguous;
   - for two labels with opposite polarities, "correct" requires both assignments correct;
   - the blind read draws 48 A3 first lines from the domain, under a seed declared at G-ANL-F3, excluding sessions read during any adjudication;
   - it runs after the analyzer's output exists and before the seat's full read (Q5, answers:37).
8. **Q-F3's secondaries:** (a)–(f) of m:312 on mf3's records. (b) is computed on the contrast arms only. (f) gives length in tokens, cap hits, defects by class and the stage-1 mention rate. Floors as m:312.
9. **A-m1 §2.5 (1) and (2):**
   - (1) every input path is accepted relative to the repository root, with the committed-blob check unchanged. This also closes the VERDICTS read §4 item 2's quirk: `_prod_committed`'s `rel == str(p)` test and `flag_of_record`'s silent FALSE on a relative `--flag-source`.
   - (2) D1 (2026-10-30), D_O′ (2026-11-30) and D2 (2026-12-22) become declared constants, each verified at the run against the proposal and A-m1 (A-m1 pinned by sha256). Under N8, a D_O-era declaration (dated before A-m1's commit) is read against D1, and its substate keeps its name.
10. **Round 2's standing rule:** Code searches the record for misparaphrases flagged in the analyzer's PIN texts and corrects each at this round, listing each by anchor in the entry. The search is not a completeness proof.
11. **The artifact:** `data/m/gates/G-ANL-F3.json`, write-once, as G-ANL-F0's. `G-ANL-F0.json` is untouched.

## 4. What Code does meanwhile

Nothing is written to `scripts/m_analyze.py`. Code's map of the analyzer, by role and line, is in session scratch: `ganl/index.txt` and `ganl/m_304_350.txt`. On the seat's answers, the build follows the BUILD (F3) practice:
- the design raw with the PIN register;
- the self-tests and the site check;
- a blind code review and a blind values-check;
- immediately before the commit, the LOCK-m-OLMo check and the coordinating session's pod word;
- a commit by path, not pushed.

LOCK-m-F3 v0.1 is not started. It waits for the seat's confirmation of the riding texts and its answers on F-1 to F-7.
