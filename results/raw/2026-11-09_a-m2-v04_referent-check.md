# ADDENDUM-m2 v0.4 — the referent check of the delta (A-m2 v0.4 §6 item 1)

*Code's raw, PI date 2026-11-09.*
- *What was checked:* A-m2 v0.4's delta from v0.3, against `smoke:`, `read:` and the file itself, with the citations its changed text makes.
  - v0.4 is `ADDENDUM-m2-f3-reasoning-block-v0_4.md`, sha256 `8f8ef932…714a`, untracked at root.
  - `read:` is `results/raw/2026-11-09_a-m2-smoke_design-to-code_answers.md`, sha256 `f13447d9…73cd`.
- *How:* a blind agent, read-only.
  - Its brief quoted the list of record's items 1–5 (the sweeps ruling of 2026-11-09, §2) and barred any read of `data/*/ckpt`, `data/*/reports` and `data/n`.
  - By its report, HEAD was `9eed029` when it started and `3d6f402` when it ended. `3d6f402` is the coordinating session's commit of the sweeps ruling.
- *Outcome:* 59 items: 48 CONFIRMED, 7 IMPRECISE, 1 OPEN, 3 FAIL.
  - The OPEN (item 3.14) is substantive and unresolved, so §6 item 1's STOP fires.
  - The STOP block is [`_a-m2-v04_code-to-design_STOP`](2026-11-09_a-m2-v04_code-to-design_STOP.md).
- *This raw:* the agent's report verbatim (it holds no local path), then Code's disposition of every item not CONFIRMED, each re-checked at source.
- *The brief's pathspec:* the brief quoted the list's item 3 as written, and that form excludes nothing on this laptop's git. Code sent the agent the working form during its run. The agent's two content searches are disclosed in the STOP block's §6 (Q5).
- *Nothing ran on a model.*

## The agent's report (verbatim)

# Referent check: ADDENDUM-m2 v0.4, the delta from v0.3

**HEAD at start:** `9eed029`. **HEAD at end:** `3d6f402`. Another session committed `3d6f402` while I worked. It adds `results/raw/2026-11-09_o23-sweeps_design-to-code_answers.md` and inserts 83 lines into RESULTS.md, removing none. The smoke's RESULTS entry is byte-identical; it moved from RESULTS.md:125 to :186. At the end v0.4 and `read:` still hash to their expected values, and v0.3 still equals its HEAD blob.

**Tally:** 59 graded items.
- 48 CONFIRMED
- 7 IMPRECISE
- 1 OPEN
- 3 FAIL
- 0 NOT CHECKABLE

**Items that look substantive (your call under §6 item 1's STOP rule):**
- **FAIL A:** §4.2's file list is missing `resume.py`.
- **OPEN:** whether the analyzer can stay unchanged.
- **FAIL B and FAIL C** are in §4.4's information for the PI. They don't affect this routing.

---

## 1. Hashes: all CONFIRMED
- **v0.4:** `8f8ef932…714a`, as expected.
- **`read:`:** `f13447d9…73cd`, as expected.
- **v0.3:** the disk copy equals the HEAD blob. Both have blob id `1b0d6215…8469` and sha256 `83093812…fa67`.
- **Also checked:**
  - PROPOSAL-m is `42ab36ec…6c6b`.
  - The lock is `377c5d60…6ce7`, last changed at `1e79955`.
  - The archived v0.1 is `cdcc8e86…53f0` and v0.2 is `69e23212…cb47`. Both are untracked, as line 3 says.

## 2. The full diff, v0.3 → v0.4
- **CONFIRMED, byte for byte: "§1, §3.1, §3.3's body and §3.4 are v0.3's text, unchanged".**
  - §1: v0.3:23–25 equals v0.4:25–27.
  - §3.1: v0.3:37–42 equals v0.4:39–44.
  - §3.4: v0.3:48 equals v0.4:50.
  - §3.3 differs only in its heading ("runs" → "ran").
- **CONFIRMED: every change the "What changed" paragraph (v0.4:7) lists is present.**
- **IMPRECISE: some changed lines are not listed.**
  - **Line 1, the title:** "a declared smoke, … form" → "the smoke's result, … form and cap".
  - **Line 3, the version header:** normal for a new version.
  - **Line 5, the anchors paragraph:**
    - "Nothing of §3 or §4 runs before Code's step-3 commit" → "Nothing of §4 runs before Code's step commit of this version". The number looks dropped.
    - `smoke:` and `read:` are added.
    - The paths and commits for `pre:`, `ans2:`, `ans3:` and `Q8` collapse to "as v0.3 had them".
  - **§0.1 (:13):** "; the re-run re-evaluates it, §4.3" is deleted.
  - **§0.2 (:15):** "(`daca8b0`)" is added.
  - **§0.4 (:19):** besides the tense change, it adds "at the cap §4.1 states" and "§3.5 records what it found".
  - **§2's heading (:31):** "to be tested in §3, not assumed" → "tested in §3".
  - **§3's heading (:37):** adds "run 2026-11-09".
  - **§4.2 (:73):** `REASONING_FORM` "(its §3.1 id)" → "(`F-b`)".
  - **§4.3 (:75):** anchors "(§3, §4)" → "(§3.5, §4.1)".
  - **§7 removes referents as well as adding them.** Details are in item 3.18.

## 3. Each delta item against its sources

For 3.1–3.6 I recomputed from the 12 session JSONs, `summary.json` and the raw, not only from the documents. I also recomputed the echo class under §1 independently from each record's pieces, with the domain and the whitespace-normalised equality. Over all 67 lines it matches the driver on echo, contains, frame and domain size, with 0 mismatches.

**3.1 §0.5 (v0.4:21): CONFIRMED.**
- (i) by form is 3/18, 6/18, 3/18 and 2/13.
- F-b is selected and stop 2 fires (3 ≥ 3).
- F-b's three defect lines are all cap-reach.
- The forms drew a reason in 18/18, 4, 5 and 2 lines, matching read:37.

**3.2 §3.5, the run paragraph (:52): CONFIRMED.**
- **Driver:** the blob at `9c7062e`, `0afd842`, `6cfd3db` and HEAD hashes to `c9393a48…0884d9b`.
- **Date, licence, pin and backend:** the raw's lines 2 and 9 give 2026-11-09 and LOCK-m-F3 v0.1's licence. Line 10 gives the v0.3 pin, and line 12 gives backend `a734dadec8f8ce9b`.
- **G-VER:** `g_ver` is `[]` in all 12 JSONs.
- **Exclusions:** both are `lexical` in a free round.
  - S4 at round 10 (raw:369), complete.
  - S10 at round 5 (raw:851), which ends there.

**3.3 The table: CONFIRMED.**
- Lines are 18, 18, 18 and 13. (i) is 3, 6, 3 and 2. Echo is 3, 5, 0 and 2. Cap is 0, 1, 3 and 0. Empty is 0 everywhere. Counter (a) is 5, 11, 0 and 2.
- Session seconds: the exact JSON sums are 800.322, 2,196.415, 4,239.865 and 1,024.102.
- Minor note: read:31 shows F-b's three per-session values as 1,621.5, 1,323.8 and 1,294.5. Those sum to 4,239.8, but the exact total rounds to 4,239.9.

**3.4 The rule and stops: CONFIRMED.**
- raw:1045–1046 and `summary.json` give keys F-a [6, 11, 0] and F-b [3, 0, 1].
- Stop 1 is false and stop 2 is true. Nothing is adopted.

**3.5 Counter (b): CONFIRMED.**
- There are 115 responses (30 + 30 + 30 + 25).
- The two (b) responses are S3 round 7 (raw:243) and S6 round 8 `Perfect.` (raw:517). Both are free rounds.
- Code's read §6 and read:35 agree.

**3.6 What the forms drew.**
- **The counts: CONFIRMED.** 4/18, 5/18, 18/18 and 2/13, as at read:37. The raw is consistent with this.
- **"Degeneracies no class catches": IMPRECISE.**
  - The `...` ×5 (S3) and bare `===` ×5 (S11) are caught by nothing.
  - But 5 of S6's 6 bracketed lines are counter (a) lines (they are inside F-a's 11). Under the v0.1 package's containment class they were tagged `echo` (raw:552–556).
  - The phrase is true only of the classes §1 corrects.

**3.7 F-b's length bullet: CONFIRMED.**
- `n_tok` in order: 48, 50, 57, 59, 60, 53, 60, 30, 44, 23, 57, 60, 59, 53, 54, 38, 40, 44.
- The range is 23–60 and the mean 49.39. Seven lines are at 57 or more.
- The three lines that end at a newline mid-sentence are S8 lines 6–8, at 30, 44 and 23 tokens.
- "m:174/m:294's own trigger condition": the count condition (≥ 3) is met. m:174's domain is G-TIME-F3's ≤ 36 lines; v0.4 handles that by declaring an amendment.

**3.8 Cost: CONFIRMED.**
- F-b's sessions ran 1,294.5–1,621.527 s, with mean 1,413.288 s. F-0's mean is 266.774 s.
- "Re-encodes the context per token": the uncached loop does a full forward over the growing `ids` at each step (`valence_core/adapters/qwen_mlx.py:325–340`).

**3.9 §4.1, F-b's bytes: CONFIRMED.** These are byte-identical:
- v0.4:71, v0.4:42, v0.3:40 and read:47.
- The driver's `SMOKE_FORMS` (`scripts/mf3_sessions.py:552`).
- Every JSON's `form_bytes`.
- All 18 F-b reasoning pieces in the transcripts. Each ends "So far," with no trailing space.

Each stored line equals the stripped text after the opener (the adapter strips at `qwen_mlx.py:343`). The driver's regex (:571) reads the same four literals from v0.4, at :40–43.

**3.10 §4.1's citations: all CONFIRMED.**
- **m:174:** the trigger and the value 120; it names no other value. The n rendering, the joiner, the newline stop and the menu block match.
- **m:265:** cap reached without a newline is a defect; the frozen ban list applies.
- **m:293:** CONFIRMED with a note. "A fire STOPs before G-ID-F3 and the seat re-specifies" is lock §8 bar 5's own wording, and that row cites m:293 itself (LOCK-m-F3.md:405). m:293 sets the bar at critical 5 of ≤ 18 and inherits STOP-before-G-ID through "as G-TIME-F0" (m:280).
- **m:294:** "Cap fixed (§2.2's trigger)".
- **m:296:** "Cap; path; projections".
- **m:330:** a fired bar pauses; pauses are not verdicts.
- **Lock bar 5** (:405): p0 .10, α .05, sham, realised n.
- **Lock bar 10** (:410): the cap member is in the numerator; on fire, "PAUSE … never a verdict".

**3.11 The binomial critical count: CONFIRMED.** For n = 18, p0 = .10, α = .05 the critical count is **5**. P(X ≥ 5) = .0282 and P(X ≥ 4) = .0982. This equals m:271's [C] value and read:48.

**3.12 §4.2's named sites: CONFIRMED, with one wording issue.**
- `mf3/banner.py` imports m's `REASONING_HEADER` (:27, :36). In `m/banner.py`, `REASONING_HEADER` is at :61 and `REASONING_LINE` at :62.
- `scaffold.REASONING_CAPS` is (60, 120) (:44).
- `stages._extra` refuses any cap but 60 at time (stages.py:579–581).
- `stages.cap_trigger` is at :984–1000.
- `prior_gate` re-computes the fixed cap from G-TIME-F3's checkpoint (:470–478).
- The driver pins v0.3's sha256 (:545–547) and parses §3.1 (:571–590).
- The licence names `m/banner.py` and `m/audit.py` by sha (lock:107–108), and both still hash to those values.
- The lock rows match: F6 (:451), F8 (:453), F11 (:456), F19 (:464), F25 (:470), F28 (:473).
- **IMPRECISE:** "`scaffold.f3_config`'s stage table" (the same words appear at read:51). At HEAD, `f3_config` has no table, only a per-stage `if` (scaffold.py:127–132).

**3.13 FAIL A: §4.2's list of mf3 files that move, and its cap sites, are incomplete.**
- **`valence_core/mf3/resume.py` is not listed.**
  - Its `Identity` refuses any `reasoning_cap` but 60 at stage "time" (resume.py:187–189).
  - Its self-test asserts that time at 120 is refused (:276).
  - `run_gate_stage` builds every identity through it (stages.py:949 → :654–663).
  - So the G-TIME-F3 re-run at 120 cannot start unless this unlisted file moves.
- **The driver's `time` wiring is not named, though it must change.**
  - It hard-codes `TIME_REASONING_CAP = 60` (:109, used at :284, under the time-wiring PIN at :99–104; its self-test is at :1340–1345).
  - It has no checkpoint-path flag, and its precheck uses the default `Q-F3_time.json` (:321, :327).
  - §4.2 names the driver only for the smoke pin.

**3.14 §4.3: facts at HEAD and requirements on the build.**
- **"`LAZY_F3_MODULES`, which includes mf3's banner, keys, lines, readrule, scaffold and schedule": IMPRECISE.**
  - `LAZY_F3_MODULES` is only (`mf3.scaffold`, `mf3.readrule`) (`scripts/m_analyze.py:3430`).
  - The six modules are in the 22-module Q-F3 closure (lock:94).
  - This text is carried unchanged from v0.3. It was already graded IMPRECISE at `results/raw/2026-11-08_a-m2-v02_referent-check.md:172–173`.
- **CONFIRMED facts:**
  - `02dadb3` is G-ANL-F3's canonical run. It adds `data/m/gates/G-ANL-F3.json`, unchanged since, which holds `d19f336d…`. The artifact is write-once (m_analyze.py:24, :1933, :11273).
  - The precheck refuses an ended checkpoint, or an existing one without `--resume` (mf3_sessions.py:326–334).
  - Reports and reads are named after the checkpoint's stem (stages.py:109–112, used at :930).
  - F29's sentence is at lock:474.
  - `readrule.release_full` returns the records unchanged and runs no piece check (readrule.py:518–520).
  - The analyzer has a `--time` option (m_analyze.py:27).
- **OPEN (substantive): "G-ANL-F3 re-runs on the unchanged analyzer", and the analyzer "unaffected by … the cap".**
  - G-ANL-F3's battery group "Q-F3 reader path" (m_analyze.py:11035) runs mf3's own stage chain on the stub.
  - It passes `"reasoning_cap": 60` at G-TIME-F3, G-ID-F3, G-F3 and the campaign (:10722, :10740–10749, called at :10792, :10871, :10882).
  - §4.2 puts cap 120 into `f3_config` and `_extra` "for every stage from the re-run on", and has `prior_gate` read 120. Built that way, mf3 would refuse the battery's calls.
  - **What settles it:** the seat says whether 60 stays admissible on the stub path, or allows a battery edit. A battery edit moves the analyzer hash the lock names.
- **Requirements, not checkable now:** the r2 checkpoint; the `id`/`qual` wirings refusing the first run; the contents of the lock re-issue; G-ID-F3 at 120; v0.2's contents.

**3.15 §4.4 (v0.4:77)**
- **The hours versus read:41: equal, except one wording. IMPRECISE.**
  - v0.4 says "≈ 0.5–1 h per uncached member"; read: says "per pair".
  - These are equivalent, since each pair has one uncached member (m:281, m:295, F12).
  - But 1 h is above the same paragraph's 25–35 min per uncached session.
- **"≈ 4 s per reasoning token": CONFIRMED [E].**
  - From read:'s own figures: (1,413 − 267)/(6 × 44) = 4.34 s.
  - From the JSONs: 1,146.5 s over 260 extra reasoning tokens per session gives 4.41 s.
  - Net of F-0's longer task responses: 1,146.5 s over 245.7 extra generated tokens gives 4.67 s.
- **The arithmetic: CONFIRMED.** 6 × 25–35 min is 2.5–3.5 h. 40 × 25–35 min is ≈ 20 h.
- **m:295, and m:298 via "as §3.1" (m:286, m:249): CONFIRMED.**
- **FAIL B: "the campaign's 448–704 launches (m §2.4)".**
  - m §2.4's tables give the campaign's launches as 704–992 cached (m:220–226) and 672–960 uncached (m:234–241). These include the sham arms; looks are counted at 704 and 672 (m:330).
  - 448 appears only in m:48 (§0.4), as uncached contrast-arm sessions at k ≥ 35. The cached contrast count there runs 480–704.
  - At the same per-session figures, all launches come to ≈ 35–50 h cached and ≈ 280–560 h uncached.
  - 704 × 35 min is 411 h, not 370.
  - The figure comes from read:41 unchanged.
- **FAIL C: "a cap below the uncached figure with G-ID-F3 failed makes Q-F3 NOT-RUN under m:324, as m wrote it".**
  - m:243 says the PI **may decline** to commit v1.0, "which makes Q-F3 NOT-RUN".
  - m:324's clause is "the PI declined to commit v1.0". It also says a locked unit that produces sessions "is analyzed on what it obtained (floors, cap, or PI stop)" (see also m:247).
  - This sentence is new in v0.4; it is not in read:.

**3.16 §5: CONFIRMED, consistent with read:60–64.** Two notes:
- read: §5 item 4 (the hours, [noted]) isn't carried as a routing item. Its substance is in §4.4.
- The [alt] wording says only "§4.1's cap sentence reverted". The alt would also need changes to the cap text in §4.2–§4.4, §6 item 4 and the title.

**3.17 §6: IMPRECISE (minor).**
- Item 3 marks `read:` "Done", but `read:` is untracked at HEAD.
- read:3 says the PI commits it by path. §6 item 2 doesn't name that commit.
- read:55 puts Code's close line before the referent check; v0.4 folds the close line into item 2.
- Item 4's chain matches read:51.

**3.18 §7.**
- **CONFIRMED: everything §7 adds is present and correct.**
  - m:294–296, m:298, m:324 and m:330.
  - PINs F6, F8, F11 and F19.
  - Commits `46773e2`, `9c7062e` and `6cfd3db`.
  - The smoke's files and `read:`.
  - The figures.
  - `scaffold.py:122–131`; the cap check's `raise` is at :132.
- **IMPRECISE: what §7 drops or leaves loose.**
  - It drops `pre` and the pre-read (`da1e1b8`), yet v0.4 still cites `pre:§2` (:27, :73).
  - It drops `qwen_mlx.py:292–305` and `:343`, though §4.1 still relies on the adapter's stop rule and strip.
  - "The key sites as v0.3 §7" points into a file that is moving to `archive/`.
  - m:159 is listed but cited nowhere in v0.4 (carried over from v0.3).
  - F18 is cited but missing from §7's PIN list.

**3.19 Smaller items: all CONFIRMED.**
- §0.4 is in the past tense.
- §2's last sentence gives 5/18, 2/13 and 18/18, which match read:37.
- §3's and §3.3's headings are in the past tense.
- §3.2's "≈ 50 min" is dropped, and that is §3.2's only change. The measured total is 8,260.7 s, ≈ 138 min.

## 4. Citations in the changed text
Everything not already graded above is CONFIRMED:
- m:258, m:261, m:263, m:265, m:271, m:318.
- gt:§0 (critical 4 at n = 13, and the backend, gt:58 and gt:62–63), gt:§1.2 (gt:114), gt:§1.3 and gt:Q4 (gt:174–181).
- read:§1, §2.2 and §2.4.
- Lock bars 5, 8 and 10; F25, F28 and F29; the closure line.

The only citation failures are FAIL B (m §2.4) and FAIL C (m:324).

## Everything not CONFIRMED
- **IMPRECISE:**
  - 2: the changes the paragraph doesn't list.
  - 3.6: "degeneracies no class catches" for S6's lines.
  - 3.12: "stage table".
  - 3.14: what `LAZY_F3_MODULES` contains.
  - 3.15: G-ID-F3 "per uncached member".
  - 3.17: §6's handling of `read:`.
  - 3.18: §7's dropped and loose referents.
- **OPEN:** 3.14, the unchanged analyzer and its battery's cap of 60.
- **FAIL:**
  - A, 3.13: `resume.py` and the driver's time wiring are missing from §4.2.
  - B, 3.15: the 448–704 launches.
  - C, 3.15: the NOT-RUN sentence.

**Outside the delta, in read:, for the seat:**
- read:7 says "4.7× F-0's"; the means give 5.30×.
- read:49 says "≈ 20–50%". The exact binomial P(X ≥ 5 of 18) is .168 at 3/18 and .889 at 7/18. That figure bears on the choice in §5 item 2.
- read:47 says the model "mostly" supplied no space after the opener; it supplied one in 0 of 18 lines.

## Compliance and content searches (the coordinator's correction)
- **Content searches run.** I ran no `grep -r` and no `rg`. I ran two `git grep`s, both with pathspec `-- . ':!data/*/ckpt' ':!data/*/reports' ':!data/n'`:
  1. `git grep -n -I -E '448(–|-|–)704|448 to 704'` printed nothing.
  2. `git grep -n -E 'LAZY_F3_MODULES'` printed lines only from root docs, `results/raw`, `scripts/m_analyze.py`, and one line from `data/m/gates/G-ANL-F3.json`. That path class is data/m/gates, not ckpt or reports. It printed no line, path or "Binary file … matches" from data/*/ckpt or data/*/reports.
- **What those two searches may have read.** If those exclusions excluded nothing, both searches may have read the content of tracked files under data/*/ckpt and data/*/reports. Nothing from those directories printed.
- **Every other grep** was `/usr/bin/grep` on files named explicitly. None was under data/, except a count-only `grep -c` of the closure hash in `data/m/gates/G-ANL-F3.json`.
- **Everything else:**
  - I opened, listed, sized and traversed nothing under the protected directories.
  - I used no `--stat` or `--numstat`. `wc -l -c` touched only `results/raw` smoke files.
  - I wrote no files and made no git writes.
  - I ran no model and imported no repo code. All Python was stdlib-only `python3 -I -c`.

## Code's dispositions (every item not CONFIRMED, each re-checked at source)

- **Item 2, IMPRECISE: changed lines the "What changed" paragraph does not list.**
  - Re-checked by a character diff of v0.3 and v0.4 at the anchors paragraph (line 5) and §0.1 (line 13).
  - Agreed. None of the unlisted changes moves a form, a figure, a bar, a key or the rule.
  - To the seat as a dated note (the STOP block's §4).
- **Item 3.6, IMPRECISE: "degeneracies no class catches".**
  - Agreed. Under §1, S6's bracketed lines are not echo lines, and counter (a) counts five of its six; F-a's 11 counter-(a) lines include them.
  - The phrase holds of the classes, not of the counters. A dated note.
- **Item 3.12, IMPRECISE: "`f3_config`'s stage table".**
  - Agreed. At HEAD `f3_config` has a per-stage test (`scaffold.py:131–132`), not a table. The build adds the table.
  - A dated note.
- **Item 3.13, FAIL A: `resume.py` and the driver's `time` wiring are missing from §4.2's list.**
  - Agreed. Code's scratch build hit `resume.py`'s cap check (`resume.py:187–189`) independently.
  - To the seat as Q2, with Code's reading.
- **Item 3.14, IMPRECISE: what `LAZY_F3_MODULES` contains.**
  - Re-checked at `scripts/m_analyze.py:3430`, `("valence_core.mf3.scaffold", "valence_core.mf3.readrule")`. Agreed.
  - A dated note.
- **Item 3.14, OPEN: the unchanged analyzer and its battery's cap of 60.**
  - Re-checked at `scripts/m_analyze.py:10713`, `:10722`, `:10742`, `:10792`, `:10871`, `:10882` and `:11035`.
  - [C] Code reproduced it: `_bt_f3_chain`, imported from the scratch build's tree and called on a temporary root, raises at its first call. The exception and its message are in the STOP block's §1.
  - Substantive and unresolved: this is the STOP, Q1.
- **Item 3.15, IMPRECISE: "per uncached member".** Agreed. A dated note.
- **Item 3.15, FAIL B: "the campaign's 448–704 launches (m §2.4)".**
  - Re-checked at m:220–226 and m:234–241.
  - [C] Code recomputed the hours at §4.4's own per-session figures.
  - Agreed. To the seat as Q3.
- **Item 3.15, FAIL C: the NOT-RUN sentence.**
  - Re-checked at m:243 and m:324. Agreed.
  - To the seat as Q3.
- **Item 3.17, IMPRECISE: §6's handling of `read:`.** Agreed on all three points; a dated note.
  - `read:` is untracked at HEAD. It is committed by path with the STOP block, on the coordinating session's relay of the routing. The routing's header reads "the PI commits by path", and the coordinating session's notes give the commit to this session: "Commit the smoke answers (f13447d9…) and ADDENDUM-m2 v0.4 (8f8ef932…) by path, with your close line on 6cfd3db".
  - read:55 puts the close line before the referent check. The close line is made with this commit.
  - §6 item 2 does not name read:'s commit.
- **Item 3.18, IMPRECISE: what §7 drops or leaves loose.**
  - Agreed, each point re-checked in v0.4's text.
  - A dated note.
- **The notes on `read:` outside the delta.** To the seat (the STOP block's §5).
  - [C] Code recomputed 5.30× and the binomial's .168 and .889.
  - On read:47, Code does not adopt the agent's "it supplied one in 0 of 18 lines". The stored line is the adapter's output stripped (`valence_core/adapters/qwen_mlx.py:343`), so the record cannot show what the model's first token carried. None of the 18 F-b lines shows a space in the transcript.
- **The agent's account of its content searches.**
  - It matches Code's masked scan of the agent's transcript: two calls, and no output path class under `data/*/ckpt` or `data/*/reports`.
  - Disclosed (the STOP block's §6).
