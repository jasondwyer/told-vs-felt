# ADDENDUM-m2 v0.5 — the referent check of the delta (A-m2 v0.5 §6 item 1)

*Code's raw, PI date 2026-11-10.*
- *What was checked:* A-m2 v0.5's delta from v0.4, against `stop:`, `ans5:`, `read:`, `smoke:` and the file itself, with the citations its changed text makes.
  - v0.5 is `ADDENDUM-m2-f3-reasoning-block-v0_5.md`, sha256 `f27505c5…5354`, untracked at root when checked.
  - v0.4 is `ADDENDUM-m2-f3-reasoning-block-v0_4.md`, sha256 `8f8ef932…714a`, untracked and never committed.
  - `ans5:` is `results/raw/2026-11-10_a-m2-v04-stop_design-to-code_answers.md`, sha256 `a85b9249…8faf`, committed at `0516832`.
- *How:* a blind agent, read-only.
  - Its brief quoted the list of record v2's items 1–5 as written (the list ruling of 2026-11-10, §2), named item 3's tested pathspec, and barred any read under `data/`.
  - By its report, HEAD was `42c5a92` when it started and `fc43249` when it ended. `fc43249` is the coordinating session's close on `750a7dd`'s entry, with the list ruling. Of the files the check reads, it touches only RESULTS.md, whose anchors the report gives as of `fc43249`.
- *Outcome:* 40 items: 35 CONFIRMED, 5 IMPRECISE, 0 OPEN, 0 FAIL.
  - One IMPRECISE item, 3.18, is substantive in kind: it concerns the order of steps. It is resolved in the record (Code's disposition below), so §6 item 1's STOP does not fire, and v0.5 is committed as delivered.
  - The other four are non-substantive. All five go to the seat as dated notes.
- *This raw:* the agent's report verbatim (extracted by script, byte for byte, from its hand-back in its transcript; it holds no local path), then Code's disposition of every item not CONFIRMED, each re-checked at source, then the items outside the delta, one of which corrects Code's own STOP block.
- *The agent's compliance:* Code's masked scan of the agent's transcript (commands digit-masked, output reduced to path classes) matches the agent's account:
  - three content searches, each excluding `data/` or run over directories that hold none, with no output path class under `data/*/ckpt` or `data/*/reports`;
  - each `data/` a command names is an exclusion pathspec, and no Read call names `data/` (the scan's sixth hit is the report's own text);
  - no `--stat`-family form, and, by a second masked check over the agent's 72 distinct Bash calls, no `find`, `du`, `stat`, `mdfind`, `ls -l`/`-t`/`-s`, `wc -c`, `git cat-file -s` or `git ls-tree -l` form.
- *Nothing ran on a model.*

## The agent's report (verbatim)

# Referent check: ADDENDUM-m2 v0.5, the delta from v0.4 (v0.5 §6 item 1)

**HEAD at start:** `42c5a92`. **HEAD at end:** `fc43249`.

Another session committed `fc43249` while I worked. It touches RESULTS.md (42 lines inserted after :126, none removed) and adds `results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md`. Below, RESULTS.md anchors are as of `fc43249`; two of them were 42 lines earlier at `42c5a92` (:548 was :506, :557 was :515). At the end, all five hashes still match and v0.3 still equals its HEAD blob.

**Tally: 40 graded items.**
- 35 CONFIRMED
- 5 IMPRECISE: one SUBSTANTIVE (item 3.18), four NON-SUBSTANTIVE
- 0 OPEN, 0 FAIL, 0 NOT CHECKABLE

**The one substantive item (3.18):** §4.3's arrow chain puts the G-SHAPE-F3 and G-ANL-F3 re-runs *before* "the build is reviewed before its commit".
- §6 item 4, the PI's routing (A5), ans5:§7 and ans5:§8 item 5 all put the review and the build's commit first.
- The analyzer refuses a canonical `ganl` run on uncommitted mf3 files, so §4.3's literal order cannot run.
- Whether this counts as "unresolved" under §6 item 1 is your call.

---

## 1. Hashes: all CONFIRMED (1.1–1.6)
- **1.1** v0.5 = `f27505c5…5354`.
- **1.2** v0.4 = `8f8ef932…714a`.
- **1.3** `stop:` = `6520837b…6dbc93`.
- **1.4** `ans5:` = `a85b9249…b8faf`.
- **1.5** `read:` = `f13447d9…273cd`.
- **1.6** v0.3 on disk equals its HEAD blob: `git rev-parse HEAD:` and `git hash-object` both give `1b0d6215…8469`, and its sha256 is `83093812…fa67`.

## 2. The diff, v0.4 → v0.5
- 15 of 97 lines changed: 3, 5, 7, 63, 71, 73, 75, 77, 84, 85, 90, 91, 92, 93 and 97. Every other line is byte-identical.
- **2.1 CONFIRMED, byte for byte: "§0–§2, §3.1–§3.4 and §3.5's other bullets are v0.4's text, unchanged".** Range digests are equal at :11–21, :25–27, :31–33, :37–50, :52–62 and :64–65, and the title (:1) is unchanged too.
- **2.2 CONFIRMED: every change the paragraph (:7) lists is present.** I checked each clause in the text.
- **2.3 IMPRECISE, NON-SUBSTANTIVE: the paragraph's "(every changed line; …)" is literally false.** One whole changed line is never named, and many within-line changes are not named. Before → after:
  - **(a) :3, the version header.**
    - "PI date 2026-11-09" → "PI date 2026-11-10".
    - v0.3's "moved to `archive/` at this version's commit" → "moved to `archive/` by `git mv` at …".
  - **(b) :5, the anchors paragraph.**
    - "before Code's step commit of this version" → "before Code's commit of this version".
    - `ans3:`'s "(`6b63973`)" is new rather than restored: v0.3:5 gives `ans3:` a path and no commit. The commit is correct (it is the file's only commit).
  - **(c) :71, §4.1: never named.** "declared here before the re-run." → "declared here before the re-run and decided by the PI on 2026-11-09 (§5)."
    - True: RESULTS.md:31.
    - Its substance appears only under the paragraph's §5 entry.
  - **(d) :63, §3.5's third bullet.** The paragraph says the bullet now says "no class catches" of the classes.
    - The text now reads "degeneracies that none of §1's classes and neither counter catches". The counter clause is new (and true), and "no class catches" no longer appears.
    - Also: "F-c's A2s wrote a bare" → "F-c's A2s a bare", and the clauses are reordered.
  - **(e) :73, §4.2.** These are named only collectively, under "(stop: Q1, option (a))" and "(3.13, Q2)":
    - the heading's "(Code's P3, pre:§2)" → "(Code's P3, pre:§2; stop: Q1 (a), Q2)";
    - the new analyzer-battery sentence;
    - "(an edit of F-1's kind either way)" → "The driver's edit is of F-1's kind and re-runs no gate by itself; … The BUILD entry names every file that moves and the DRIVER line's new blob."
  - **(f) :75, §4.3: not named.**
    - The lock re-issue's contents gain "the stub path's admission (§4.2)", "and the driver's blob" and "the list of record cited in one line".
    - "(the precheck refuses)" → "(the driver's precheck refuses)".
    - "(`--time` names it)" → "(`--time` takes any path and checks the checkpoint's unit, stage and end, `m_analyze.py:4189–4196`)". This is true at :4189–4196, with the default path at :11319; its source is stop:43.
    - Also new: the analyzer hash, the one-round-rule parenthetical, and a change in the bold's extent.
  - **(g) :77, §4.4.**
    - "G-TIME-F3's re-run ≈" → "G-TIME-F3's re-run (six sessions) ≈".
    - "hour cap at v1.0;" → "hour cap at v1.0 (m:298);".
  - **(h) :84, §5 item 2.** Adds "§4.2's stub-path admission and the two further files (ans5:§1–§2) [as written]".
  - **(i) :85, §5 item 3.** "v0.3 to `archive/`), then the build," → "v0.3 and v0.4 to `archive/`), then the build's resumption, the battery run, the review,".
  - **(j) :90, §6 item 1.** "from v0.3" … against `smoke:`, `read:` → "from v0.4" … against `stop:`, `ans5:`, `read:`, `smoke:`.
  - **(k) :91, §6 item 2.** "the routing block of 2026-11-09 verbatim; the smoke entry's close line (`6cfd3db`) cites `read:`" → "the routing blocks of 2026-11-09 (evening) and 2026-11-10 verbatim; the STOP entry's close line (`50fea90`) cites `ans5:`".
  - **(l) :93, §6 item 4.** The paragraph names only "the battery run and the review". Unnamed:
    - "(mf3 only; §4.2)" → "(mf3 and the driver; §4.2), resumed from Code's scratch worktree (declared …; accepted at ans5:§6)";
    - "self-tests" → "self-tests, the real-side assertions included";
    - "→ the build's commit, its entry naming every file that moves";
    - ", announced to the coordinating session".
  - **(m) :97, §7.** Not named:
    - the closure line moved into "§1 (… `d19f336d…f039`, 22 modules)";
    - "the v0.4 STOP (`50fea90`)";
    - "`stop:` and its referent check; `ans5:`; the F3 prebuild answers :26 and §8 (`dc1ffe1`); the G-ANL-F3 answers' A3 (`54bbfe5`)";
    - "`scaffold.py:122–131`" → "`:122–132`";
    - the added lines `stages.py:548`, `:575–581`, `:984–1000`, `:470–478`, `mf3_sessions.py:99–109`, `:321–334` and `m_analyze.py:3430`, `:4189–4196`;
    - `qwen_mlx.py:325–340`, an addition rather than a restoration (v0.3:78 has only `:292–305` and `:343`);
    - in the Figures: "the launch tables (§4.4) against m:220–226 and m:234–241".
  - So ans5:§4's correction for item 2 ("lists every changed line") is not fully achieved.

## 3. The delta items against their sources
- **3.1 The version header: CONFIRMED.**
  - v0.4: `8f8ef932…714a`, untracked, STOPPED at its §6 item 1 by the referent check (stop:1, `50fea90`).
  - v0.3: `83093812…fa67`, committed at `46773e2`.
  - The smoke: 2026-11-09 (raw:2), at `6cfd3db`; stop 2 fired (read:30).
  - v0.1 `cdcc8e86…53f0` and v0.2 `69e23212…cb47` are untracked in `archive/`.
  - The two dispositions are requirements on the commit. They match ans5:3, ans5:46 and A5.
- **3.2 The anchors paragraph: CONFIRMED.**
  - `pre:`, `ans2:` and `Q8` are v0.3:5's words verbatim.
  - The history agrees:
    - `de729c4` added `ans2:`;
    - `6b63973` added `ans3:`;
    - `da1e1b8` is the v0.1 pre-read (it adds the pre-read raw and its referent check; its §2 holds P1 at preread.md:76 and P3 at :117);
    - `Q8` is the prebuild answers' §8 (:48; the ruling at :51);
    - `50fea90` added `read:` and both `stop:` files.
  - `ans5:`'s path is right. v0.5 gives it no commit; the record has `0516832`.
- **3.3 stop: Q1 → §4.2: CONFIRMED.** §4.2 reproduces ans5:13's "(a)'s form" clause for clause, and it matches A1 (RESULTS.md:100).
- **3.4 stop: Q2 / FAIL A (3.13): CONFIRMED.** `resume.py` and the driver are added to the files that move, with their changes, as in ans5:18–19 and A2.
- **3.5 stop: Q3 / FAIL B and FAIL C: CONFIRMED.** §4.4 is corrected as ans5:23–24 says.
- **3.6 Item 3.6: CONFIRMED.**
- **3.7 Item 3.12: CONFIRMED.** At HEAD `f3_config` holds a per-stage `if` (scaffold.py:131–132). The table is the build's.
- **3.8 Item 3.14: CONFIRMED.**
- **3.9 Item 3.15: CONFIRMED.**
- **3.10 Item 3.17: CONFIRMED** for its first two points: `read:`'s commit is now recorded. Its third point (the close line's order) recurs; see item 3.26.
- **3.11 Item 3.18: CONFIRMED.** Every point is answered. (Item 2 is item 2.3 above.)
- **3.12 The paragraph's tags: IMPRECISE, NON-SUBSTANTIVE.**
  - "(FAIL B, FAIL C)" follows the NOT-RUN clause, but FAIL B is the launch-count clause (stop:99–102).
  - "(3.18)" closes a §7 entry that also carries FAIL B/C's anchors (m:220–226, m:234–241, m:243), 3.13's (`resume.py`'s lines), and lines from no referent item.
- **3.13 §3.5's third bullet: CONFIRMED.**
  - S3 (F-0 A3s; raw:201) writes `...` at lines 5, 6, 8, 9 and 10.
  - S11 (F-c A2s; raw:854) writes `===` at lines 5–8 and 10.
  - All ten have classes [] and (a) False. A bare `===` keeps no frame (code-read:242–244).
  - Counter (b) counts task responses, so neither counter catches these lines.
  - S6 (F-a A3s; raw:470) writes a bracketed request in all six lines. Lines 6–10 are (a) True by containment (code-read:119–123, :250; read:20), and all six have classes [], so none is an echo under §1.
  - "S6" is the smoke's session 6/12, F-a A3s (raw:470; read:20; referent check 3.5–3.6).
- **3.14 §4.2's facts at HEAD: CONFIRMED.**
  - `resume.Identity` refuses any cap but 60 at time (resume.py:187–189); its self-test asserts time at 120 is refused (:276).
  - `_STUB_WEIGHTS` is all-zero (stages.py:548) and is refused on a non-stub run (:575–576). The cap check is at :579–581.
  - `_extra` takes `stub` (:556), passed as `_is_stub(adapter)` (:931, :1182, :1399).
  - `prior_gate` has `require_real=False` (:437–438) and is passed `not stub` (:680, :1417). Its fixed cap is at :470–478.
  - `cap_trigger` is at :984–1000.
  - `f3_config` has no stub parameter (scaffold.py:113–115). `REASONING_CAPS` = (60, 120) (:44).
  - In the driver: the PIN at :99–104; `TIME_REASONING_CAP = 60` at :109; the precheck at :321–334. The `--smoke` form pins v0.3 (:546–547) and parses §3.1 (:575–590).
  - In the analyzer: the reader-path group at :11035 runs through `_bt_f3_reader` (:10756) to `_bt_f3_chain` (:10713). The cap is 60 with `**f3s._STUB_WEIGHTS` (:10722), and the time stem is `Q-F3_time.json` (:10742). The analyzer's only `reasoning_cap` is at :10722.
  - The lock rows: F6 :451, F8 :453, F11 :456, F18 :463, F19 :464, F25 :470, F28 :473, F29 :474.
- **3.15 §4.2's requirements: CONFIRMED as requirements, consistent with ans5:§1–§2 and A1–A2.**
  - `_extra`'s refusal and stub admission.
  - `Identity`'s binding rule.
  - `prior_gate`'s 120 unless `require_real` is off.
  - `f3_config` keeping the pair, as a table.
  - `cap_trigger` reporting; `REASONING_CAPS` unchanged.
  - The real-side self-test assertions.
  - The driver at 120, the r2 checkpoint, the refusals, and `--smoke` retired.
  - The BUILD entry's contents.
- **3.16 "Restored to `acde2d8`'s before these edits" is coherent: CONFIRMED.**
  - `git diff acde2d8 9c7062e -- scripts/mf3_sessions.py` removes 0 lines and adds 1,855.
  - All 1,440 lines of `acde2d8`'s blob survive in order.
  - `9c7062e` is the only commit to the driver since `acde2d8`, and HEAD's blob is `9c7062e`'s (`0d44f238…`).
  - So retiring the form returns the driver to `acde2d8`'s blob (`53a58c77…`), and the build's edits apply on top.
- **3.17 §4.3's facts: CONFIRMED.**
  - `LAZY_F3_MODULES` is at m_analyze.py:3430.
  - The lock gives 22 modules for the Q-F3 closure (lock:94, PIN-V2-12) and 15 for the base (:95).
  - I reconstructed the closure by a stdlib AST trace of module-level imports, without importing anything. It reproduces 15 and 22 exactly, and the two lazies add mf3's `__init__`, banner, keys, lines, readrule, scaffold and schedule. The authoritative list sits under `data/`, which I did not open.
  - The one-round rule: prebuild answers :26 (`dc1ffe1`) and the G-ANL-F3 answers' A3 at :16 (`54bbfe5`). ans5:12 extends it to p.
  - The analyzer's sha256 is `d347ea0c…`.
  - `02dadb3` is the canonical run (its subject). The artifact is write-once (m_analyze.py:24, :1933–1934).
  - The `--time` checks are at :4189–4196. `release_full` returns the records unchanged (readrule.py:518–520).
- **3.18 §4.3's chain order: IMPRECISE, SUBSTANTIVE (the order of the steps).**
  - v0.5:75 reads "→ **G-SHAPE-F3 re-runs** … and **G-ANL-F3 re-runs …** (…: Code runs the battery on the build before the review rounds; …; the artifact supersedes `02dadb3`'s …) → **the build is reviewed before its commit** … → **LOCK-m-F3 v0.1 is re-issued**".
  - The other sources order it: battery → review → the build's commit → G-SHAPE-F3 and G-ANL-F3 re-runs → LOCK. These are v0.5:93, A5 (RESULTS.md:104), ans5:46 and ans5:55.
  - The canonical `ganl` refuses unless every `valence_core/mf3/*.py` file and every closure file is committed (m_analyze.py:11059–11070, :11077–11095).
  - v0.4:75's chain had no review step; v0.5 inserted it one arrow late.
  - **What settles it:** the seat moves the review arrow before the re-runs, or rules that §6 item 4 governs. §6 item 4 already matches the routing.
- **3.19 §4.3's "the list of record cited in one line": IMPRECISE, NON-SUBSTANTIVE.** A5 (:104) and ans5:55 say "(cites the list (of record) v2)"; v0.5 names no version. The v2 raw was committed at `fc43249` during this check.
- **3.20 §4.4's launches and hours: CONFIRMED, recomputed.**
  - Launches: 704–992 cached (m:220, :226) and 672–960 uncached (m:234, :241), all six arms (704 = 128 + 64 + 2·176 + 2·80).
  - Cached hours at ≈ 3 min per session (G-F3's 40 sessions in ≈ 2 h): 35.2–49.6 h.
  - Uncached hours: 672 × 25 min = 280 h; 960 × 35 min = 560 h.
  - G-TIME-F3's re-run: 6 × 25–35 min = 2.5–3.5 h.
- **3.21 §4.4's G-ID-F3 cost: CONFIRMED.** m:295 runs A2s and A3s once each, "2/2 as above", which is m:281's cached/uncached pair. So the cost is two pairs, each ≈ 25–35 min uncached.
- **3.22 §4.4's NOT-RUN mechanism: CONFIRMED.**
  - It follows m:243's words, with "if" lower-cased and "(§5)" dropped.
  - m:324's cause is quoted correctly, cut before ", for projected hours or any reason"; its "analyzed on what it obtained (floors, cap, or PI stop)" is as quoted.
  - m:295 holds the path. m:298 reaches the PI's cap through "as §3.1" (m:249, m:286).
- **3.23 §5 item 2: CONFIRMED.** The 2026-11-09 (evening) A2 "[adopted]" is at RESULTS.md:31 and :557.
- **3.24 §5 item 3: CONFIRMED.** It is consistent with A5; as a summary it omits the build's commit.
- **3.25 §6 item 1: CONFIRMED.**
- **3.26 §6 item 2: IMPRECISE, NON-SUBSTANTIVE.**
  - v0.5:91 puts "the STOP entry's close line (`50fea90`) cites `ans5:` by path and sha256" inside the commit step.
  - ans5:46 and A5 put the close line before the referent check.
  - It was already made, at `0516832` (RESULTS.md:82–86, with the 2026-11-10 routing verbatim at :98–104).
  - This is the third point of v0.4's 3.17 (referent check:208), which ans5:29 did not take up. Nothing remains to do.
  - The rest of item 2 is confirmed: v0.3 by `git mv`; v0.4 uncommitted, beside v0.1 and v0.2.
- **3.27 §6 item 3: CONFIRMED.** `read:` was added at `50fea90`, with the smoke entry's close line citing its path and sha256 (RESULTS.md:548).
- **3.28 §6 item 4: CONFIRMED.**
  - The declaration time 2026-11-10T03:26:42Z matches stop:162 and RESULTS.md:68. The acceptance is at ans5:41.
  - The chain matches A5, with the self-tests per ans5:13 and the announcement.
- **3.29 §7's added referents: CONFIRMED.** Each is present and backs its use:
  - `pre:` and `da1e1b8`; F18 (lock:463);
  - m:220–226, m:234–241 and m:243;
  - the battery's lines and `resume.py`'s lines;
  - the adapter: `qwen_mlx.py:292–305` (the newline stop), `:325–340` (a full forward per generated token, uncached) and `:343` (`.strip()`).
- **3.30 m:159: CONFIRMED.** Nothing in v0.5 cites it; the only occurrence is :7's "drops m:159".

## 4. Citations in the changed text
- **4.1 CONFIRMED.** Every citation says what v0.5 attributes to it:
  - m:N: m:174, m:243, m:249, m:258, m:261, m:263, m:265, m:271, m:281, m:293–296, m:298, m:324, m:330;
  - the lock: §1 :94, the bars at :405, :408 and :410, and the PIN rows above;
  - `stop:` §1, §2 and §7; `ans5:` §1–§4 and §6–§8; `read:` §1, §2.2 and §2.4;
  - every file:line checked in item 3.

## Everything not CONFIRMED
- **2.3** IMPRECISE, NS: the "every changed line" claim (§4.1's line and items (a)–(m)).
- **3.12** IMPRECISE, NS: the tag placement of "(FAIL B, FAIL C)" and "(3.18)".
- **3.18** IMPRECISE, **SUBSTANTIVE**: §4.3's chain places the gate re-runs before the build's review and commit.
- **3.19** IMPRECISE, NS: the list of record's version is unnamed (A5 says v2).
- **3.26** IMPRECISE, NS: §6 item 2's close line is already made at `0516832`, out of A5's order (3.17's third point, recurring).

## Outside the delta (not graded)
- stop:93's "adds 1,728" is the count of non-blank lines; the diff adds 1,855 lines in all. Item 3.16's conclusion is unaffected.
- v0.5:84's bracket is "[as written]"; the routing of record gives A1 "[as ruled]" and A2 "[confirmed]".
- ans5:41's condition (the BUILD entry records the declaration and that the text committed first) is not restated in v0.5, which cites ans5:§6 for it.
- Under (a), "the build makes it a table" means a table carrying (60, 120) at every stage (stop:53, "instead of the table's 120"). The BUILD entry should say what it holds.
- F18, and the lines `resume.py:276`, `stages.py:575–581`, `:984–1000`, `:470–478` and `qwen_mlx.py:325–340`, are cited only in §7. Each backs a function or claim the body names.

## Compliance
- No departures.
- I opened, listed, sized and traversed nothing under `data/`.
- The one tree-wide `git grep` carried `':!data/**'`, and each `git show --name-status` carried `-- . ':!data/**'`.
- Two recursive `/usr/bin/grep`s ran over `results/raw/` and `valence_core/mf3`, neither of which contains `data/`.
- No `--stat`, `--numstat` or `--shortstat`.
- No git writes (`hash-object` was run without `-w`), no files written, and no model run.
- Python was `python3 -I` from stdin, stdlib only, and imported no repository code.

## Code's dispositions (every item not CONFIRMED, each re-checked at source)

- **Item 2.3, IMPRECISE, NON-SUBSTANTIVE: the paragraph's "(every changed line; …)" does not hold.**
  - Re-checked by Code's own line and word diff of v0.4 and v0.5. It shows the same 15 changed lines, and found two of the unlisted changes independently: the anchors paragraph's "step commit" → "commit", and §4.1's added clause.
  - Agreed. Each unlisted change is one of these:
    - a header, a date, an anchor, a citation, a summary, or a record of the PI's decision;
    - a requirement already stated in `ans5:` §1–§2, §7 and §8 item 5, and in A1, A2 and A5. Among them are §6 item 4's added "→ the build's commit" and the driver in the build's scope.
  - None departs from those sources, and none moves a form, a bar, a cap or a key.
  - §4.1's added clause ("and decided by the PI on 2026-11-09 (§5)") records A2 of the routing of 2026-11-09 (evening), "[adopted]".
  - A dated note to the seat: `ans5:` §4's correction of item 2 ("lists every changed line") is not fully achieved.
- **Item 3.12, IMPRECISE, NON-SUBSTANTIVE: the tags "(FAIL B, FAIL C)" and "(3.18)" are placed loosely.** Agreed. A dated note.
- **Item 3.18, IMPRECISE, SUBSTANTIVE in kind: §4.3's arrows put the G-SHAPE-F3 and G-ANL-F3 re-runs before "the build is reviewed before its commit".**
  - Re-checked: v0.5:75's phrases run, in this order, "G-SHAPE-F3 re-runs", "Code runs the battery on the build before the review rounds", "the build is reviewed before its commit", "LOCK-m-F3 v0.1 is re-issued".
  - Four sources give the other order (battery → review → the build's commit → the two re-runs → the lock):
    - v0.5 §6 item 4, "Code's block, in order";
    - A5 of the routing of 2026-11-10, "[go]";
    - `ans5:` §7;
    - `ans5:` §8 item 5.
  - §4.3's literal order cannot run:
    - the canonical `ganl` requires every `valence_core/mf3/*.py` file and the Q-F3 closure to be committed (`ganl_commit_problems`, `scripts/m_analyze.py:11059–11070`; the refusal, exit 2, at `:11092–11096`);
    - the canonical `gshape` "needs every source committed at HEAD and unedited" (`scripts/mf3_sessions.py:14–15`; the refusal at `valence_core/mf3/gshape.py:256–258`).
  - Why the record settles what the agent left to Code or the seat:
    - v0.5's own §5 makes the routing block the record of the PI's decisions: its heading reads "(the routing block is their record)" (v0.5:81);
    - its item 3 orders "the battery run, the review, the re-runs" (v0.5:85);
    - A5's "[go]" is the PI's decision on that order.
  - So the item is resolved in the record, and it is not a STOP. Code will run A5's order, which is also §6 item 4's.
  - A dated note to the seat: §4.3's review arrow sits one place late.
- **Item 3.19, IMPRECISE, NON-SUBSTANTIVE: §4.3's "the list of record cited in one line" names no version.**
  - Agreed. A5 ("cites the list v2") and C2 of the routing of 2026-11-10 ("LOCK-m-F3's re-issue and LOCK-p v0.2 cite v2") name it, and the re-issue will cite v2.
  - A dated note.
- **Item 3.26, IMPRECISE, NON-SUBSTANTIVE: §6 item 2 lists the STOP entry's close line among this commit's items.**
  - Agreed. A5 puts the close line first, and it is committed at `0516832`, before the referent check. Nothing remains to do.
  - A dated note.

## Outside the delta

- **Code's STOP block: its line 93 count, "adds 1,728", is wrong.** [C] `git diff acde2d8 9c7062e -- scripts/mf3_sessions.py` adds 1,855 lines (1,728 non-blank, 127 blank) and removes none.
  - The claim the line supports stands: the smoke driver's commit removed no line of the wiring.
  - This is a dated correction to `stop:` (committed at `50fea90`), recorded here and in the entry.
  - The v0.4 values-check's two passes carried the same count (`2026-11-09_a-m2-v04_valuescheck.md` :184, :394), and Code's disposition there applied it (:38).
- **v0.5 §5 item 2's bracket, "[as written]":** the routing of record gives A1 "[as ruled]" and A2 "[confirmed]". The routing governs; nothing to do.
- **`ans5:` §6's condition on the BUILD entry** (record the declaration, and that the text committed first): the BUILD entry will record both.
- **The table under (a)** ("the build makes it a table"): the BUILD entry will say what the table holds, m:174's pair (60, 120) at every stage.
