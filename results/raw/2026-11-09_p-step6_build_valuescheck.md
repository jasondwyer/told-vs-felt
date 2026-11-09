# PROPOSAL-p step 6 -- the BUILD entry's blind values-check

*Code's raw, PI date 2026-11-09. A blind values-check of the step-6 BUILD entry, its three dated notes and the two raws
it cites (the reviews, the flock probe), against the uncommitted working tree at `2018ffc`, the records and the raws.
238 items: 227 PASS, 10 IMPRECISE, 1 FAIL. Each of the 11 was applied before the commit, in the checker's suggested
form or close to it. The FAIL (round 3's U+2028 split into a real line break by the raw's assembly) is fixed in the
committed reviews raw; the item-2 option chosen is the `STAGING_NOTE` wording, so p's package is unmoved. The fixes
were checked by tool, not by a second blind pass. The report is verbatim, its local paths scrubbed (`<repo>`, `<tmp>`)
and its headings set one level down.*

## Blind values-check: p step 6 BUILD entry, its dated notes, and the two raws it cites

Checked against the uncommitted working tree at HEAD `2018ffc`: p's code, RESULTS.md, the seat's raws, git history, and the G-CAL records. I recomputed the counts with `valence_core/p/report.py`'s own functions. I edited no repository file and ran no git command that writes. `git status --short` was the same at the start, after every run and at the end. Nothing was created under `data/p`: no `reports/`, no `verdicts/`, no lock file. I loaded no model.

Line numbers refer to the files as they stand:
- `E:` is the BUILD entry draft (`podwatch/step6_build_entry.md`).
- `N:` is the dated notes (`podwatch/retab_notes.md`).
- `R:` is the reviews raw (`podwatch/review_raw_draft.md`).
- `F:` is the flock-probe raw (`podwatch/flock_probe_raw.txt`).

### Results

**11 of 238 claims need a fix: 10 IMPRECISE and 1 FAIL.** The other 227 pass. Every number, hash, count, file name and function name checked out.

The fixes:
- **The FAIL.** In the reviews raw, round 3 lost one character: a U+2028 became a real line break.
- **Two IMPRECISE items in the dated notes.**
  - `irom` is not one of §0.3's class (c).
  - The residuals are listed in the F-p11 FLAG bullet, not the F-p1 bullet.
- **Two IMPRECISE items are stale sentences in the BUILD entry.** Each describes behaviour a later round changed.
- **The rest are over-statements or a wrong citation.**

### Claims checked

#### A. The BUILD entry (step6_build_entry.md)

| # | Claim (condensed) | Grade | Evidence |
|---|---|---|---|
| 1 | E:1. `de729c4` holds the seat's answer of 2026-11-08 for step 6, and its §4 is the order that starts with the build. | PASS | `git log -1 de729c4`. results/raw/2026-11-08_p-step6_design-to-code_answers.md §4 (line 26). |
| 2 | E:1-3. The PI's routing is quoted in `de729c4`'s close lines, item 2: "build → G-SHAPE-p re-run → G-ANL-p → LOCK-p v0.1 ×3 → G-TIME-OLMo (p) on the box [go]". | PASS | RESULTS.md:262 (the step-6 STOP entry's close), verbatim. The full block is at :206. |
| 3 | E:3-4. Scope: the stage and its driver, the analyzer, G-ANL-p's battery, register entries (3) and (6)–(9), and the `daca8b0` rulings. | PASS | `git status`: stage.py, identity.py, analysis.py and p_analyze.py are new; register, keys, schedule, proxy, report, guard and p_sessions are modified. |
| 4 | E:4-5. Entry (9) is built on `resume.Identity` and stays PENDING. The register refuses it until the routing. | PASS | register.py:125-131 (status PENDING) and :174-176. My run: `RegisterStop ... entry (9) ... pending`. |
| 5 | E:5-6. Nothing ran on a model. On the box only a model-free flock probe ran, outside the repository. | PASS | Consistent with the records. The probe script writes only under /workspace/flock_probe/ (F:46-48). |
| 6 | E:9-12. Entry (3): module `m_analyze` (scripts/m_analyze.py, imported by p_analyze.py). `clock_of_record` → `analysis.clock_of_record_p` (D_p for OLMo, m's own for Q-F0 and Q-F3). `crosscheck_coordinate` → `crosscheck_coordinate_p` (p's directory for OLMo, m's for Q-F0). Kinds are Clock and roots. Roots are parameters (Q9 (b)). | PASS | register.py:92-100. analysis.py:65-73. p_analyze.py:50. Answers Q9. |
| 7 | E:13. Entry (6): `valence_core.m.stages.DEFAULT_OUT` → `REPO/data/p`, kind roots. | PASS | register.py:109-112. stage.py:106. Answers Q1. |
| 8 | E:14. Entry (7): m's `verify_schedule_dir` → p's `verify_schedule_dir`, kind roots. | PASS | register.py:113-118. Answers Q2. |
| 9 | E:15. Entry (8): `IDENTITY_KEYS_OLMO` → m's key set plus p's four fields, kind pins. | PASS | register.py:119-124. identity.py:35-37. |
| 10 | E:16-17. Entry (9): `Identity` → `identity.identity_p` (m's builder wrapped), kind pins, PENDING. Refused in production. | PASS | register.py:125-131. My run: `stage.precheck('OLMo-sft', stub=True)` gives StageRefusal "register entry (9) is not admitted". |
| 11 | E:18-19. The seat's answer is in the tree, untracked, at `results/raw/2026-11-08_open50-entry9_design-to-code_answers.md`. | PASS | `git status`: `??` on that path. |
| 12 | E:19. Its sha256 is `d6296d44…2b97`. | PASS | `shasum -a 256` gives `d6296d446c46…f755f62b97`. |
| 13 | E:19-20. Its §2 declares (9) on `resume.Identity`. | PASS | open50 raw, lines 12-14. |
| 14 | E:20. The PI has not routed it. | PASS | Not contradicted: no close or routing record for it in RESULTS.md or results/raw (grep). |
| 15 | E:22-23. The answer's three term (c) checks are built and pass, with (9) admitted for that test alone and restored after (`identity._selftest`). | PASS | identity.py:149-183. The self-test runs 170/170. |
| 16 | E:24. With (8) and (9), m's `_validated` accepts a p identity. | PASS | identity.py:164, :181. |
| 17 | E:25-26. A moved p field: `_identity_diff` names it and `load_or_init` refuses the resume. | PASS | identity.py:165-174, :181. |
| 18 | E:27. With both restored, m's identity path is byte-identical to m's on m's inputs. | PASS | identity.py:157, :177, :181. |
| 19 | E:28. The G-SHAPE-p re-run, G-ANL-p and the locks wait for the flip, which moves p's package. | PASS | register.py is one of the 14 hashed files (guard.py:71-72; resume.package_sha256_of). |
| 20 | E:29-30. stage.py and the driver's `time --unit OLMo-{ckpt} [--resume]` run m's `run_gate_stage` with gate `time` under (1), (2) and (6)–(9). | PASS | stage.py:108 and :126 (`ENTERED (1,2,6,7,8,9)`), :837. p_sessions.py:506-509. |
| 21 | E:31-32. The order (Q4, a rule): every substitution is entered before anything computes renders and before the load. | PASS | Answers Q4. stage.py:813-830: substitutions first, then the factory. |
| 22 | E:32-33. PIN: `scaffold._of_record` is asserted empty at entry (a STOP otherwise) and cleared at exit. | PASS | stage.py:20-21, :411-415. Self-test :1046-1056. |
| 23 | E:33. Term (d)'s state is recorded at the stage's end, before restoration. | PASS | stage.py:873, inside `stage_substitutions`. |
| 24 | E:34. Before the load: the precheck, then the weights files, then the DRIVER and WEIGHTS lines. | PASS | p_sessions.py:226-243. |
| 25 | E:35. The lock names each `lock_required` value as a whole line or between backticks. | PASS | stage.py:300-303, :369-370. |
| 26 | E:36. The lock must name both analyzers. | PASS | stage.py:243-247. |
| 27 | E:37. The lock must name PROPOSAL-m's and PROPOSAL-p's sha256s. | PASS | stage.py:248-249. |
| 28 | E:38. The lock must name m's and p's package sha256s. | PASS | stage.py:250-251. |
| 29 | E:39. The lock must name G-CAL-p's, G-SHAPE-p's and G-ANL-p's artifacts, the last two current. | PASS | stage.py:252-272. G-SHAPE-p's currency covers both packages, the sources map and the closure. G-ANL-p's covers four code sha256s. |
| 30 | E:40. The lock must name the covariate line. | PASS | stage.py:163-165, :256-258. |
| 31 | E:41. The lock must name p's renders under both conventions. | PASS | stage.py:273-274. |
| 32 | E:42. The lock must name the lexicon. | PASS | stage.py:275. |
| 33 | E:43. The lock must name p's schedules manifest and the unit's six schedule files. | PASS | stage.py:276-282. The manifest lists 6 files per unit (18 in all). My `lock_required('OLMo-sft')` listing shows 6. |
| 34 | E:44. The lock must name m's six banner components, the OLMo ban list and the scaffold set. | PASS | stage.py:129 (6 names), :283-289. |
| 35 | E:45. The lock must name the driver. | PASS | stage.py:290-292. |
| 36 | E:46. The lock must name p's licence lines and the register's lines. | PASS | stage.py:293-296. My listing: 19 licence lines and 8 register lines (54 values in all). |
| 37 | E:47. The lock carries exactly one `BACKEND OF RECORD` line. | PASS | stage.py:111-112, :306-311, :371. Self-test :1041-1045. |
| 38 | E:48. Every entry the stage enters must be admitted. | PASS | stage.py:354-355. My run. |
| 39 | E:49. After the load, inside the substitutions, the adapter's backend identifier is compared with the lock's line. | PASS | stage.py:830-836 (non-stub). |
| 40 | E:50. The call log is `ckpt/{U}_time_p-calls.jsonl` (PIN). | PASS | stage.py:39, :424. |
| 41 | E:51-52. Every event is one ASCII JSON line, written and fsynced as it happens: the run line, one line per call, a STOP's detail, and the end line in the `finally`. | PASS | stage.py:470-473 (`ensure_ascii=True`), :468 (fsync), :826-830, :880-886. proxy.py:131. |
| 42 | E:53. The log is opened once every entry is in force. | PASS | stage.py:814, :825. |
| 43 | E:54. The log is withheld like the checkpoint (m:318). | PASS | stage.py:46. PROPOSAL-m:318. |
| 44 | E:54. A resumed run appends to it. | PASS | stage.py:440 (`O_APPEND`). |
| 45 | E:54-55. A torn last line, or one a failed write left torn, is ended first. | PASS | stage.py:443-445, :451-467. Self-test :1501-1507, :1519-1525. |
| 46 | E:56-57. A flock on a lock file beside the record spans a run's reads, checks and appends, and time-report's read and write. | PASS | stage.py:757-759, :573-603. p_sessions.py:268-274. |
| 47 | E:57. On the box the lock file lies on the network volume (nfs4, `local_lock=none`). | PASS | Box repo at /workspace/repo/jspace-lab (box_respawn_check.py:26). Volume mounted at /workspace (2026-11-06_backend_box-captures.txt:26). Mount line and options at F:23, F:26-28. |
| 48 | E:58-59. The probe found the lock exclusive across processes on one pod and released on close. Cited raw path. | PASS | F:18-21. stage.py:579 cites the same path. |
| 49 | E:59-60. Cross-pod exclusion is not probed. A terminated pod's lock may persist for the lease, which fails closed. | PASS | F:29-31; stated as unprobed. |
| 50 | E:61-62. A run that ends in a SystemExit once its run line is written, or whose proxy call raised the STOP, is STOPPED. The whole exception chain is read. | PASS | stage.py:51-54, :559-569, :853. |
| 51 | E:63-66. The STOP is recorded twice. The marker `ckpt/{U}_time_p-STOPPED.json` is reserved at the run's start and renamed into place first (no new space, never half-written). The cause is written over its padding. Then the end line's stop mark. | PASS | stage.py:425, :514-528 (`RESERVE_SIZE` 8192, padded), :819-824, :855-872, :879-887. |
| 52 | E:68. A Ctrl-C during the recording is deferred until the end line has been attempted. | PASS | stage.py:846-850, :908-917. Self-test :1422-1437 (real SIGINT). |
| 53 | E:69-70. Later runs refuse before the load while either record stands, while the log is unreadable, or while m's checkpoint stands beside a log with no run line. | PASS | stage.py:766-768, :785-796. |
| 54 | E:71-72. The residual covers any STOP but a ProxyStop whose own STOP line was written: a kill between the raise and the rename, or the rename and the end line both failing (EIO), leaves no record. | PASS | stage.py:60-62. Logic :853-906. |
| 55 | E:72-73. The double failure is announced on stdout and stderr, and the reservation stays. | PASS | stage.py:893-901, :921. Self-test :1458-1466. |
| 56 | E:73-74. Stale reservations are named at every later run's start and in p's report, never removed. | PASS | stage.py:806-811, :828, :715-716, :921-925. |
| 57 | E:75-77. The way out is the seat's ruling. A restart needs the call log, the marker and m's checkpoint moved aside (PIN-37). No adjudication input is defined and no resume path exists. | PASS | stage.py:63-65. Refusal order :763-796. |
| 58 | E:78. An interruption stays resumable. | PASS | stage.py:66. Self-test :1196-1216. |
| 59 | E:79-81. p's report is `reports/{U}_time_p-report.json` (PIN), built from m's checkpoint and the call log, and re-derivable with `time-report`. | PASS | stage.py:68-70, :423, :660-733. p_sessions.py:257-283. Self-test :1120-1130. |
| 60 | E:82. "§2.3's counters: the sham sessions every round". | **IMPRECISE** | Corrupted spelling reads only the sham sessions' forced rounds (report.py:267-270, :291-296). |
| 61 | E:82-83. Also the contrast forced rounds' control characters (F-p13 (a)), with the line-break trigger over every round. | PASS | report.py:283-284, :298-300. |
| 62 | E:84. The proxy's cuts on the sham session, attributed by seed and stored-text sha256. | PASS | stage.py:624-650, :723-726. |
| 63 | E:85. Every contrast proxy count is withheld; its call count is the free-round exclusion position. | PASS | stage.py:132-133, :727. |
| 64 | E:86. m's report and reads are named with their sha256s. | PASS | stage.py:705-712. |
| 65 | E:87. The report holds the entries entered and term (d)'s end states. | PASS | stage.py:731-732. |
| 66 | E:88. The proxy checks every stored text (Q5); this is unreachable by construction and a STOP if it fires. | PASS | proxy.py:126, :142-151. |
| 67 | E:89-90. The message carries no text and no call index (PIN). The detail rides on the exception and goes to the log. | PASS | proxy.py:27-32, :52-58, :127-135. Self-test :248-252. |
| 68 | E:90. The driver prints the message verbatim. | PASS | p_sessions.py:249-251 (`STOP: ` prefix plus the message). |
| 69 | E:91-92. m's not-run, verdicts and v2 posting run for p's units under entry (3), staged and in-file (Q7). | PASS | p_analyze.py:140-212. Answers Q7. |
| 70 | E:92-93. m's function writes into a staging directory seeded with the final directory's files. | PASS | analysis.py:187-197. |
| 71 | E:93-94. p adds `proposal_p_sha256` and a `p` block and writes each output once into data/p/verdicts. | PASS | analysis.py:163-169, :237-238. p_analyze.py:62. |
| 72 | E:94-96. The `p` block holds the register, both analyzer blobs, D_p's check, the disclosure, m's three NOT-RUNs (Q6) and the SFT sentence. The posting adds the resolution. | PASS | analysis.py:151-160. p_analyze.py:100-104, :124-129, :212. |
| 73 | E:96-97. "PIN: every occurrence of the staging directory … names the final directory instead". | **IMPRECISE** | The behaviour holds (analysis.py:124-136, :230, :242). No such PIN is declared in the code: the 15 step-6 PINs (grep) do not include it. The rule is in `STAGING_NOTE` (analysis.py:98-103). |
| 74 | E:97-99. An unreported file, a leftover staging trace, or a target that is a link or holds other bytes refuses the write. | PASS | analysis.py:214-240. guard.py:195-206. |
| 75 | E:99. Every target is checked before the first write. | PASS | guard.py:194-206 (phase 1). |
| 76 | E:100. `p_analyze.py --selftest` runs the battery; `ganl` writes the artifact. | PASS | p_analyze.py:699-702, :721-727, :660-691. |
| 77 | E:100. 14/14 on the working tree, after m's battery. | PASS | 14 `chk` calls (p_analyze.py:354-633). Author's log `podwatch/p_analyze_selftest_r5.txt` ends "14/14", with 539 PASS lines = 525 + 14. It finished 02:26:18, about 2:50 after a start following the last source edit (stage.py 02:22:08). Not re-run, per instruction. |
| 78 | E:101. m's battery runs unchanged: 525/525, 538 coverage ids, G-ANL-F3's count and coverage. | PASS | data/m/gates/G-ANL-F3.json: checks_total 525, coverage_ids 538. p_analyze.py:344-355. |
| 79 | E:102. Entry (3) on the real `m_analyze`: equality and restoration, an exception included. | PASS | p_analyze.py:394-409. |
| 80 | E:103-104. A Clock NOT-RUN on p's path, under sentinels for `CKPT_REL` and `VERDICTS_REL`, which are never used, under all three commands. | PASS | p_analyze.py:420 (not-run), :469 (verdicts), :560 (posting), :526 (v2-closure). |
| 81 | E:103. The sentinels "record and raise on any use". | **IMPRECISE** | `_Never` raises on path joins, str, format, comparison, hash, len, iter, contains and getitem (p_analyze.py:361-374). `repr` and identity pass silently (round 2's N3 row, R:199). |
| 82 | E:105. The pin beside. | PASS | p_analyze.py:433-444. |
| 83 | E:105. "m's form equal to p's but for exactly the two added keys". | **IMPRECISE** | In the not-run case p's output also differs in `date_is_clock_of_record` (true under entry (3), false in m's form). The test sets that field aside (p_analyze.py:450-455). |
| 84 | E:106-107. p's VERDICTS on a synthetic OLMo-sft campaign (`_Camp`): m's form plus exactly the two keys. | PASS | p_analyze.py:302-341, :465-496 (strict comparison). |
| 85 | E:107. A lock that does not name p's analyzer and package is refused. | PASS | p_analyze.py:156-176, :497-502, :515. |
| 86 | E:108-109. Seeded staging: m's exclusivity sees a seeded output, the posted run's comparator is the seeded copy, and a p re-run is refused. | PASS | p_analyze.py:456-463, :503-516, :573-596. |
| 87 | E:110-111. v2 resolution: OLMo from p's directory; an OLMo output only in m's directory is refused; a second m directory is refused; no machine path. | PASS | p_analyze.py:132-137, :195-212, :537-613. |
| 88 | E:113-114. Q-F0's two outputs go through `run_verdicts_p` (m's form) on the G-ANL-F3 battery's binding, with m's regression's checks. | PASS | p_analyze.py:216-253, :616-626. |
| 89 | E:115-116. m's three NOT-RUN outputs (`0f35954`) on their bindings: `e0b4f2c`'s analyzer, its package and closure, each pinned in full. | PASS | `0f35954` added the three outputs (git log --diff-filter=A). `git show e0b4f2c:scripts/m_analyze.py \| shasum` gives `6ec3222b…93d9`, the pinned value. Each output records 6ec3222b…, 60199b36…, a3bc7bb9… (p_analyze.py:70-73). |
| 90 | E:117. `data/p` is untouched: every file's sha256 is the same before and after. | PASS | p_analyze.py:294-297, :358, :632-634. |
| 91 | E:119. F-p13: control characters are a counter. | PASS | report.py:23-28. daca8b0 raw §1. |
| 92 | E:119. "each stage's report lists every such text by key". | **IMPRECISE** | G-TIME's report lists them only on the read domain: sham rounds and contrast forced rounds (report.py:297-300). Contrast free rounds' are withheld (report.py:249-252). |
| 93 | E:120. The lexicon is `data/p/lexicon/web2.txt`, Code's pick. | PASS | report.py:38, :103. |
| 94 | E:120. 235,976 lines. | PASS | `wc -l` gives 235976. |
| 95 | E:120. sha256 `be41ad97…bab9`. | PASS | `shasum` gives be41ad97…2c2bbab9, matching report.py:104. |
| 96 | E:120-121. Byte for byte the BSD and macOS system dictionary. | PASS | Byte-identical to /usr/share/dict/web2. |
| 97 | E:121. The seat let it stand (`de729c4` §3). | PASS | Answers §3. |
| 98 | E:121-122. The suffix rule and the forms `**` and `_…_`. | PASS | report.py:94, :99, :106, :128-133, :195-200. |
| 99 | E:122-123. The re-tabulation is reported as dated notes on the entries that quote the counters. | PASS | The two notes target RESULTS.md:303 (table :368-372) and :423 (F-p1, :456-457). The p BUILD entry's "23 of 384" (:1048) points to the rulings entry by its dated note (:1088-1089). |
| 100 | E:124. §0.1's SFT sentence is a constant every OLMo-sft output's `p` block carries. | PASS | report.py:109, :220-222. analysis.py:159. Self-test p_analyze.py:443. |
| 101 | E:125. Round 1: 6 MAJOR, 8 MINOR, 12 NOTE. | PASS | R:148. |
| 102 | E:125-126. The reviewer's text is in `results/raw/2026-11-09_p-step6_build_review.md`. | PASS | The raw lands there. |
| 103 | E:127-128. MAJOR 1: entry (7)'s replacement re-entered (2) after the load, and a live thread STOPped the stage. | PASS | R:18-25. |
| 104 | E:128-129. Fix: `keys.keys_context` uses (2) as held (PIN). A thread-alive factory PASSes, with term (d) recorded. | PASS | keys.py:82-92. schedule.py:80. Self-test stage.py:1131-1142. |
| 105 | E:130-131. MAJOR 2: the report carried the call and cut totals. | PASS | R:27-34. |
| 106 | E:131-132. An exclusion at free round 0, at 1, and none leaves the report and lines unchanged but for sha256s. | PASS | stage.py:1143-1167. |
| 107 | E:133. MAJOR 3: the cut log and the report were lost on an exception or a tail failure. | PASS | R:36-49. |
| 108 | E:134-137. Write-ahead log, re-derivable report, lexicon loaded and commit-checked before the load and `-text`, three tested cases. | PASS | stage.py:350-353, :360-361. .gitattributes diff (`/data/p/lexicon/** -diff -text`). `git check-attr`: text unset. Self-test :1120-1130, :1168-1216. |
| 109 | E:138-140. MAJOR 4: `check_dir` pinned by AST; m's verdict on data/m/schedules, clean and on four tampered copies. | PASS | schedule.py:139-207, :237-265. |
| 110 | E:141-144. MAJOR 5: the p-form VERDICTS group; Q-F0 goes through `run_verdicts_p` with m's checks. | PASS | Items 84 and 88. |
| 111 | E:145-148. MAJOR 6: package in every p block; canonical commands require committed code; the VERDICTS lock must name analyzer and package (PIN). | PASS | p_analyze.py:28-31, :84-104, :156-176, :667-669, :728. |
| 112 | E:150. MINOR 7: D_p's check reads the D_P in use (PIN). | PASS | analysis.py:20-21, :76-92. |
| 113 | E:151-153. MINOR 8: the lock list gains the proposals, p's package, the covariate, schedules, banner, ban list and scaffold set. The backend is the lock's line, not a constant (PIN). | PASS | stage.py:34-37, :235-297. The round-1 code (`podwatch/stage_before_r1.py:122-152`) lacked these and had `BACKEND_OF_RECORD`; no such constant now (grep). |
| 114 | E:154. MINOR 9: the artifacts must record the current code. | PASS | stage.py:211-232, :261-270. |
| 115 | E:155. MINOR 10: the entries entered. | PASS | stage.py:695, :732. |
| 116 | E:156. MINOR 11: no machine path; a second m directory is refused. | PASS | Item 87. |
| 117 | E:157. MINOR 12: term (e) tracks `m_analyze`. | PASS | guard.py:315-327. |
| 118 | E:158-159. MINOR 13: seeded staging is exercised; a p re-run is refused. | PASS | Item 86. |
| 119 | E:160. MINOR 14: `_cli_path`. | PASS | p_analyze.py:736-748. m_analyze.py:11254. |
| 120 | E:161. N1–N4 and N6–N12 are applied. N5 is items (a) and (b), pinned in `report.session_counters`. | PASS | report.py:272-276. |
| 121 | E:162-163. Round 2: 23/26 fixed, 2 partly (MINOR 9, N12), 1 not (N5). New: 2 MAJOR, 4 MINOR, 10 NOTE. | PASS | R:309-310 and the table (counted). |
| 122 | E:164-165. M-1: a ProxyStop was lifted by `--resume`, and the PASS report showed no trace. | PASS | R:214-228. |
| 123 | E:165-167. A STOPPED run blocks later runs before the load. An interruption stays resumable. Each run's outcome is in the report and a closing line. | PASS | stage.py:766-793, :697-703, :957-960. |
| 124 | E:166. "Rounds 3 and 4 then found and closed further gaps; the residual is the STOP PIN's". | PASS | Rounds 3-5 below. stage.py:60-62. |
| 125 | E:168-169. M-2: the call log is admitted (`-diff` by the ckpt rule). A self-test asserts 3 logs, 3 reports and the lexicon are admitted. | PASS | .gitignore diff. `git check-ignore -q` exits 1 for all seven. `check-attr` diff unset. stage.py:1536-1542. |
| 126 | E:171-173. m-1: a torn last line is ended. `build_report` refuses another stage's log (schema, unit, stage; runs 1..K; end and call lines). | PASS | stage.py:606-621, :680-682. |
| 127 | E:173-174. "A line torn by a failed write within a run is not ended before that run's own end line, so the two read back as one malformed line." | **IMPRECISE** | Stale. Since round 4's NOTE 2, `CallLog._put` ends a torn line before the next record (stage.py:451-467). The self-test asserts it (stage.py:1501-1507, :1523). Round 5 confirms (R:777). |
| 128 | E:175-176. m-2: a plain run refuses when m's checkpoint exists; `--resume` refuses when the log is lost. | PASS | stage.py:772-777. Self-test :1235-1247. |
| 129 | E:177. m-3: the sources map and closure are compared. | PASS | stage.py:219-232. |
| 130 | E:178. m-4: the code record is taken before the battery, and drift is refused. | PASS | p_analyze.py:667-672. |
| 131 | E:180. N-1: unreported file refused; targets checked first. | PASS | analysis.py:214-223. guard.py:194-206. |
| 132 | E:181. N-2: `register.active`. | PASS | keys.py:69-79. register.py:144-149. |
| 133 | E:182. N-3: the attribution flag reads the sham session only. | PASS | stage.py:728-730. |
| 134 | E:183. N-4: whole line or backticks. | PASS | stage.py:300-303. |
| 135 | E:184. N-5: m's gate-stage form, with PROPOSAL-p and CLAUDE.md commit-checked. | PASS | stage.py:379-386. Self-test :1034-1040. |
| 136 | E:185, :190-191. N-6 is item (f); N-10 is the count; N12's open half is item (g). | PASS | Items 173, 179, 174. |
| 137 | E:186. N-7: (9) needs (8) in force. | PASS | register.py:140, :187-189. |
| 138 | E:187-188. N-8: the fixture carries p's four fields; `--v2-closure` runs under the sentinels. | PASS | p_analyze.py:333-337, :517-536. |
| 139 | E:189. N-9: the refusal is worded as p's. | PASS | analysis.py:202-212. |
| 140 | E:192-193. Round 3: 12 fixed, 2 partly (M-1, m-1), 2 answered. New: 1 MAJOR, 3 MINOR, 5 NOTE. | PASS | R:489-491. |
| 141 | E:194-195. MAJOR: a tear inside a non-ASCII character made the log unreadable, read as empty, and a STOP was lifted. | PASS | R:366-387. |
| 142 | E:196-198. Fix: ASCII lines, a split on the log's own line ending, an unreadable log refused before the load, and `build_report` names it. | PASS | stage.py:470-473, :490-504, :785-789, :675-679. Self-test :1273-1279, :1309-1314. |
| 143 | E:200-205. MINOR 1: recorded twice, the mark taken from the whole chain, the proxy's STOP propagates; round 4 found the marker window. | PASS | proxy.py:130-135. stage.py:559-569. R:553-572. |
| 144 | E:206-207. MINOR 2: U+0085, U+2028 and U+2029 are fixed. | PASS | Self-test stage.py:1526-1535. |
| 145 | E:208-209. MINOR 3: the log opens once entries are in force; the precheck refuses an unadmitted entry. | PASS | stage.py:354-355, :825. Self-test :1322-1348. |
| 146 | E:211. NOTE 1: the count is per entry and module. | PASS | register.py:141, :192. |
| 147 | E:212-214. NOTE 2: two-phase writes; a failure before the renames writes nothing; only a failed rename or a crash between renames can leave the set part-written. | PASS | guard.py:184-239. |
| 148 | E:215. NOTE 3: the VERDICTS lock uses the whole-line or backtick rule. | PASS | p_analyze.py:54, :163-165. |
| 149 | E:216-217. NOTE 4 is the stage lock; NOTE 5 is item (i). | PASS | stage.py:572-603. Item 176. |
| 150 | E:218-219. Round 4: no MAJOR; 6 fixed, 2 partly (MINOR 1, NOTE 2), 1 answered. New: 2 MINOR, 5 NOTE. | PASS | R:713-718. |
| 151 | E:220-221. m-1: a Ctrl-C or crash in the marker's write could lose the STOP. Now reserved at the start and renamed first, and no echo can break the recording. | PASS | stage.py:551-556, :819-824, :855-867, :897-901. |
| 152 | E:221-222. "Round 5 closed the double-failure case." | **IMPRECISE** | Round 5 deferred the Ctrl-C forms and announced the EIO form, stating it as the residual (R:845-861). The EIO double failure still leaves no record (stage.py:60-62; the entry's own E:71-73). |
| 153 | E:223-224. m-2: flock had never run on the box's volume and every error read "held". Now only BlockingIOError does, and others are named. | PASS | stage.py:591-600. Self-test :1508-1525. R:574-590. |
| 154 | E:226. NOTE 1: a full disk failed both records; the rename needs no new space. | PASS | stage.py:855-862. Self-test :1371-1399 (ENOSPC held). |
| 155 | E:227-228. NOTE 2: a torn line is ended; m's checkpoint with a log holding no run line is refused. | PASS | stage.py:451-467, :794-796. |
| 156 | E:229. NOTE 3: `time-report` takes the lock. | PASS | p_sessions.py:268-274. |
| 157 | E:230. NOTE 4: a left-over temp no longer blocks; the part-written case is stated. | PASS | guard.py:185-193, :214-215. |
| 158 | E:231-232. NOTE 5: self-test wording, the fd on a failed open, the STOP line's detail in the end line, the lock refusal's label. | PASS | stage.py:1127-1128, :446-449, :874-877 and :884, :595. |
| 159 | E:233-234. Round 5: no MAJOR; m-1 and m-2 fixed; NOTEs 1 and 4 partly. New: 1 MINOR, 7 NOTE. | PASS | R:953-960. |
| 160 | E:235-237. m-1: the double failure is announced once on stdout and stderr and stated as the residual; Ctrl-C deferred. | PASS | stage.py:60-62, :893-906, :846-917. Self-test :1458-1466. |
| 161 | E:239-240. NOTE 1: the residual's wording; `time-report`'s exit codes listed fully. | PASS | stage.py:60. p_sessions.py:51-57. |
| 162 | E:241. NOTE 2: a rename that took is recorded in place. | PASS | stage.py:863-866. Self-test :1469. |
| 163 | E:242. NOTE 3: stale reservations named, never removed; only a run's own reservation released. | PASS | stage.py:806-811, :921-925. |
| 164 | E:243. NOTE 4: the marker carries the cause over its padding. | PASS | stage.py:531-548, :868-872. Self-test :1457, :1471. |
| 165 | E:244. NOTE 5: a write failing before its first byte leaves the tail clean. | PASS | stage.py:463-466. Self-test :1473-1493. |
| 166 | E:245. NOTE 6: the probe raw is committed with the build, with mount options; exclusion stated per pod. | PASS | F:26-31. stage.py:578-581. |
| 167 | E:246. NOTE 7: the temp is created exclusively; the refusal names a part-written set. | PASS | guard.py:214-219. analysis.py:205-211. |
| 168 | E:248-250. (a) `contrast_forced_control_chars` lists texts by key, though ruling (h) keeps class fields out of m's G-TIME report. | PASS | report.py:272-276, :298-300. m readrule.py:16-35. |
| 169 | E:251-252. (b) Q5's "over the checkpoint" is read as the read domain. | PASS | Answers Q5 (line 11). |
| 170 | E:253-254. (c) No text or index in STOP messages; Q5's "the entry records the exception verbatim". | PASS | Answers Q5. proxy.py:82-84, :148-151. |
| 171 | E:255. (d) The contrast forced rounds' cut counts are withheld. | PASS | stage.py:723-727. |
| 172 | E:256-257. (e) A re-run is refused where m's reports "identical" (PIN-37); the seeded copy carries two keys. | PASS | analysis.py:98-103, :202-212. Self-test `m_again == ["identical"]`. |
| 173 | E:258-261. (f) The driver prints STOPs verbatim as m's does; BOUNDARY INCIDENT carries the prefix's token count. | PASS | p_sessions.py:249-251. m_sessions.py:425 and others. m scaffold.py:317-319 ("prefix token count {len(p)}"). |
| 174 | E:262-264. (g) m's report and reads under data/p/reports keep m's form; p's report binds them by sha256 and carries `proposal_p_sha256`. | PASS | m stages.py:209-223 (`reports/` under out_root). stage.py:705-712, :720. |
| 175 | E:265-268. (h) The backend comes from the lock's line. A box change before the lock means no code edit; after the lock, a STOP before generation. m:302 has a BACKEND entry supersede the lock's field. | PASS | stage.py:830-836. PROPOSAL-m:302 ("a new `BACKEND` entry that supersedes the lock's field"). |
| 176 | E:269-273. (i) Every SystemExit after the run line STOPs the stage, m's refusals included; the way out as above. | PASS | stage.py:51-53, :63-66. |
| 177 | E:274. p's `package_sha256` is `2d9a933a…f720` (14 files). | PASS | `guard.package_sha256()` gives 2d9a933af718…f720. Licence line "(14 files, valence_core/p/*.py)". |
| 178 | E:274. The m files and `olmo_hf.py` are unchanged. | PASS | `git diff --quiet` on both. All 17 m module sha256s equal G-CAL-p's `p.licence_at_run`. olmo_hf `df80b79b…` matches RESULTS.md:1031. |
| 179 | E:276. `p_sessions.py --selftest` gives 170/170, including term (e)'s static check and the import set. | PASS | My run: "170/170 p selftest checks pass", exit 0. p_sessions.py:461-463. |
| 180 | E:277. `p_analyze.py --selftest`: 525/525 (538), then 14/14. | PASS | See items 77-78 (author's log; consistent with source mtimes). |
| 181 | E:278. Five blind reviews. | PASS | The raw has five rounds. |
| 182 | E:280-287. Next: the routing, then the flip of (9), the G-SHAPE-p re-run (`5009e77` superseded), G-ANL-p, three LOCK-p v0.1s, G-TIME ×3. | PASS | open50 §3 item 2. de729c4 §4. daca8b0 §2 (F-p12). `5009e77` = G-SHAPE-p's artifact (sha 3fb0f640…). |
| 183 | E:289. The note's target: the 2026-11-07 entry "PROPOSAL-p v0.2 — COMMITTED". | PASS | RESULTS.md:1260. |
| 184 | E:290. Its source is `de729c4` §2. | PASS | Q6 and Q8 are in §2. |
| 185 | E:291-293. p:84 is read per Q6: Q-F0, Q-F3 where known, A-m1's (16), the adoption against Q-F0's PASS, p's other units. | PASS | Answers Q6 (line 15). PROPOSAL-p:84. |
| 186 | E:293-294. m's three NOT-RUNs go in each `p` block as `PROPOSAL-m OLMo-{ckpt}`, with reason and output sha256. | PASS | analysis.py:108-121. |
| 187 | E:294-295. Reason: m's validator refuses a unit naming itself, and p keeps m's unit strings. | PASS | Answers Q6. |
| 188 | E:296-298. p §4.4's "m's battery run under p's roots" (Q8) is read as: m's battery unchanged, p's groups under (3) in temp roots, then the regression. | PASS | Answers Q8 (line 17). PROPOSAL-p:90 has the phrase. |

#### B. The dated notes (retab_notes.md)

| # | Claim (condensed) | Grade | Evidence |
|---|---|---|---|
| 189 | N:1. The target: the G-CAL-p entry (2026-11-08, "G-CAL-p-{sft,dpo,instruct}"). | PASS | RESULTS.md:303. |
| 190 | N:2. Source: `daca8b0` §1 and §3. | PASS | daca8b0 raw §1 (F-p13) and §3 (F-p11). `git log -1 daca8b0`. |
| 191 | N:3-4. F-p13: a counter, not a hair trigger; each stage's entry lists every such text. | PASS | The ruling restated (daca8b0 raw line 17). |
| 192 | N:4. Five at G-CAL-p, all on item 7 (`report.counters`, `control_chars.texts`). | PASS | Recomputed: 1 (sft), 2 (dpo), 2 (instruct). Keys CORR_corrupted i=7 s=0 and s=1. |
| 193 | N:5. sft corrupted 7 s1: '\x7f'. | PASS | Recomputed. |
| 194 | N:6-7. dpo corrupted 7 s0: the ANSI cyan "Task: Which is heavier…" text. | PASS | Exact match. |
| 195 | N:8. dpo corrupted 7 s1: '\x7f'. | PASS | |
| 196 | N:9. instruct corrupted 7 s0: '\x1b[1m\x1b[32mTask is solved correctly\x1b[0m'. | PASS | Exact match. |
| 197 | N:10. instruct corrupted 7 s1: '\x7f'. | PASS | |
| 198 | N:11-12. G-CAL-p's artifacts stand as written; this is the re-tabulation the ruling asks for. | PASS | daca8b0 §3, last sentence. |
| 199 | N:13. Harness first lines 2/5/6 (the artifacts: 2/3/5). | PASS | Recomputed. Artifacts' `p.counters` and RESULTS.md:370-372. |
| 200 | N:13-14. Added: '**DRAFT ANSWER' (dpo 15 s0) and '**Final Answer' (dpo and instruct 15 s3). | PASS | Key diff, recomputed. |
| 201 | N:15. Corrupted spelling 0/0/0 (the artifacts: 0/1/0); dpo clean 4 s1's `true` is in the lexicon. | PASS | Recomputed. The hit token is `true.`, and 'true' is in web2. |
| 202 | N:16. The other counters are unchanged. | PASS | Control characters 1/2/2, cap hits 8/5/2, refusals 1/1/1 and line breaks 0/0/0 all equal the artifacts'. |
| 203 | N:18. The target: the rulings entry, whose F-p1 bullet quotes 0/3/5. | PASS | RESULTS.md:423, :456-457. |
| 204 | N:19. Source: `daca8b0` §3, F-p11. | PASS | |
| 205 | N:19-20. On G-CAL-OLMo's 384 records: 0/2/4 refined against 0/3/5. | PASS | Recomputed on data/m/gates/G-CAL_completability_olmo-*.json. The self-test agrees (report.py:413-425). de729c4 §3 gives "0/2/4". |
| 206 | N:21. The two `true`/`three` hits are out. | PASS | dpo clean 4 s1 (`true.`) and instruct corrupted 4 s1 (`(True`). |
| 207 | N:21-22. "The six that remain are §0.3's class (c), as the ruling keeps them". | **IMPRECISE** | `irom` is not in §0.3's class (c) (PROPOSAL-p:17). The annotated bullet itself lists "the five of §0.3's class (c)" and `irom` apart (RESULTS.md:456-457). daca8b0 §3 names only dn, Januwy and Janaury. |
| 208 | N:23. Januwy (dpo and instruct corrupted 8 s2). | PASS | Recomputed hits. |
| 209 | N:24. Janaury (instruct corrupted 8 s3). | PASS | |
| 210 | N:25. dn (dpo and instruct corrupted 11 s1). | PASS | |
| 211 | N:26. irom (instruct corrupted 7 s1). | PASS | |
| 212 | N:28. "The F-p11 residuals that bullet lists". | **IMPRECISE** | "That bullet" is the F-p1 bullet (N:18; RESULTS.md:456-461). The residuals are in the entry's F-p11 FLAG bullet (RESULTS.md:466-470). |
| 213 | N:28-29. The residuals (there, could, too, from, that, the inflections) are excluded by (i) or (ii). | PASS | All 11 (with January's, Iron's, Seven's, twenty-fourth, Close., Colder.) give refined False. 'colder' is in web2. |
| 214 | N:29. The lexicon `web2.txt`, sha256 `be41ad97…bab9`, named at LOCK-p v0.1. | PASS | Item 95. `lock_required` includes `report.LEXICON_SHA256`. |

#### C. The reviews raw (to land as results/raw/2026-11-09_p-step6_build_review.md)

| # | Claim (condensed) | Grade | Evidence |
|---|---|---|---|
| 215 | R:3-6. Five blind reviews of the uncommitted step-6 build, with the stated scope. | PASS | Five rounds (R:10, 169, 328, 508, 748). |
| 216 | R:5-7. Reviewers read against `de729c4`, p v0.2 and m v1.11, in scratch roots, editing no repository file. | PASS | Each report's hygiene section. They cite the answers file, m:271, m:302, m:318. |
| 217 | R:7. "Each report is verbatim, with local paths scrubbed (`<repo>`, `<tmp>`)". | **IMPRECISE** | Rounds 1, 2, 4 and 5 match the reviewers' scrubbed reports exactly, apart from headings. Every heading is demoted one level, which is undisclosed. Round 3 also lost one character (item 218). |
| 218 | R:410-411. Round 3's m-2 scenario, as the raw reproduces it: "Two.<line break>ok\nTask: leak". | **FAIL** | The reviewer wrote "Two.<U+2028>ok\nTask: leak" (`rev3/review3_report.md` and `.scrubbed.md`). The raw has a real line break, so it misstates the scenario, which is about U+2028, and breaks the bullet. It is the only round-3 difference (`cmp3b.py`). |
| 219 | R. No machine path in any of the four texts. | PASS | grep for `/Users/`, `/private/tmp`, the user name and the session id: 0 hits in each file. |
| 220 | R:8. Every finding was applied or answered before the next round, round 5's before the commit. | PASS | Round 5's m-1 and NOTEs 1-7 are each in the code (items 160-167). |
| 221 | R. Each round's counts agree with its findings (r1 6/8/12, r2 2/4/10, r3 1/3/5, r4 0/2/5, r5 0/1/7). | PASS | Counted in the raw. |
| 222 | R:99, :145, :346. Facts re-checkable now: G-SHAPE-p's p package 717958da… and file sha 3fb0f640…; 48-file sources map; 14-module closure; the lexicon pin and byte identity. | PASS | G-SHAPE-p.json provenance. `shasum`. web2 comparison. |
| 223 | R:173, :332, :513, :754. HEAD `2018ffc`. | PASS | `git rev-parse HEAD`. |

#### D. The flock-probe raw (to land as results/raw/2026-11-09_p-step6_flock-probe.txt)

| # | Claim (condensed) | Grade | Evidence |
|---|---|---|---|
| 224 | F:3-4. `stage_lock` takes an exclusive, non-blocking flock on `data/p/ckpt/{U}_time_p.lock` beside the record. | PASS | stage.py:426, :587-593. |
| 225 | F:4. On the box that file lies on the network volume. | PASS | Item 47. |
| 226 | F:5. No flock had run there before. | PASS | Not contradicted: no flock user in valence_core/ or scripts/ besides p's stage and self-test (grep). |
| 227 | F:5. Run before any lock is cut. | PASS | No `LOCK-p-*` in the tree. |
| 228 | F:6-7. Wrote only under /workspace/flock_probe/, loaded no model, touched no record. | PASS | The embedded script writes only `D/probe.lock` and imports fcntl, os, subprocess and sys. |
| 229 | F:7. The script below is verbatim. | PASS | `diff` against `podwatch/flock_probe.py`: identical. |
| 230 | F:15-23. The output is consistent with the script's keys and order. Pod `qny1x4v8padeke`. | PASS | The pod id matches the pod of record (RESULTS.md:486, :1828, :1900). |
| 231 | F:17. 2026-11-09T06:48:31Z. | PASS | Consistent with PI date 2026-11-09 and the script's mtime (01:48 EST). |
| 232 | F:16, :26-28. The kernel string and mount options. | PASS | Not checkable against the repo; not contradicted. |
| 233 | F:29. `local_lock=none` means the client sends its locks to the server. | PASS | nfs(5) semantics. |
| 234 | F:33-34. The lock excludes another process and a second descriptor, and is released on close. | PASS | F:18-21. |
| 235 | F:34-35. Any lock error other than BlockingIOError is named by its errno, never "held". | PASS | stage.py:594-600. |
| 236 | F:29-31. Cross-pod exclusion is not probed; lease persistence fails closed. | PASS | Stated as unprobed. |
| 237 | F:3. Code's raw, PI date 2026-11-09; its landing path matches stage.py's citation. | PASS | stage.py:579. |
| 238 | F:10-12. The invocation (`scp`, then `ssh ... env.sh ...`). | PASS | Not checkable. Consistent with the output's first three lines. |

### IMPRECISE and FAIL items, with suggested corrections

1. **#60, E:82 (IMPRECISE).** Replace "§2.3's counters: the sham sessions every round, and …" with: "§2.3's counters on the sham sessions (every round; corrupted spelling on their forced rounds only, a free round's item naming the pick), and the contrast forced rounds' control characters (F-p13 (a)), with the line-break trigger over every round;"

2. **#73, E:96-97 (IMPRECISE).** No such PIN is declared in the code. Replace "PIN: every occurrence…" with: "By `STAGING_NOTE`, carried in every p block, every occurrence of the staging directory in an output m wrote, or a line m printed, names the final directory instead (`analysis.map_staging_paths`)." The other option is to declare it as a PIN in analysis.py. That moves p's package hash, so the licence line (#177) would need recomputing.

3. **#81, E:103 (IMPRECISE).** Replace "sentinels … that record and raise on any use" with: "sentinels … that record and raise on any use but `repr` and identity, which m's code does not make on p's paths (round 2's N3)".

4. **#83, E:105 (IMPRECISE).** Replace "and m's form equal to p's but for exactly the two added keys" with: "and m's form equal to p's but for the two added keys and the Clock's own field (`date_is_clock_of_record`, false in m's form, which reads m's Clock)".

5. **#92, E:119 (IMPRECISE).** Replace "each stage's report lists every such text by key" with: "each stage's report lists every such text on the seat's read domain by key (the sham sessions' rounds and the contrast forced rounds'; a contrast free round's is withheld to VERDICTS, item (a))".

6. **#127, E:173-174 (IMPRECISE; false of the code as it stands).** Replace the sentence with: "A line torn by a failed write within a run was not yet ended before that run's own end line (the two read back as one malformed line); round 4's NOTE 2 closed that." Or delete it, since round 4's NOTE 2 bullet (E:227) states the fix.

7. **#152, E:221-222 (IMPRECISE).** Replace "Round 5 closed the double-failure case." with: "Round 5 then dealt with the double failure: a Ctrl-C during the recording is deferred, and the EIO case is announced on stdout and stderr and stated as the PIN's residual."

8. **#207, N:21-22 (IMPRECISE).** Replace "The six that remain are §0.3's class (c), as the ruling keeps them:" and the list with: "Five of the six that remain are §0.3's class (c), as the ruling keeps them: `Januwy` (dpo and instruct corrupted 8 s2); `Janaury` (instruct corrupted 8 s3); `dn` (dpo and instruct corrupted 11 s1). The sixth is `irom` (instruct corrupted 7 s1), the model's own misspelling of `iron` (the render spells it right), which the bullet lists apart."

9. **#212, N:28 (IMPRECISE).** Replace "The F-p11 residuals that bullet lists" with: "The residuals the entry's F-p11 FLAG lists".

10. **#217, R:7 (IMPRECISE).** Replace "Each report is verbatim, with local paths scrubbed (`<repo>`, `<tmp>`)." with: "Each report is verbatim, with local paths scrubbed (`<repo>`, `<tmp>`) and its headings set one level down under its round's heading; round 3's one U+2028 (LINE SEPARATOR) is written `<U+2028>`." The second clause applies once item 11 is fixed.

11. **#218, R:410-411 (FAIL).** Restore the reviewer's character. Replace the two lines `… returning "Two.` / `ok\nTask: leak" is cut. …` with the single line `- **Scenario (exp_lsep3):** a sham forced round returning "Two.<U+2028>ok\nTask: leak" is cut. The call line comes back as 3 "not JSON" fragments. The report then shows:`. A visible marker is safer than a raw U+2028 in a committed raw. Whatever tool assembled the raw split lines on U+2028; it should join on `"\n"` only, or read with `newline=""` and split on `"\n"`.

### Counts

| Items | PASS | IMPRECISE | FAIL |
|---|---|---|---|
| 238 | 227 | 10 | 1 |

By file:
- **BUILD entry:** 188 items; 181 PASS, 7 IMPRECISE (#60, #73, #81, #83, #92, #127, #152).
- **Dated notes:** 26 items; 24 PASS, 2 IMPRECISE (#207, #212).
- **Reviews raw:** 9 items; 7 PASS, 1 IMPRECISE (#217), 1 FAIL (#218).
- **Flock-probe raw:** 15 items; all PASS.

### Commands run

1. **git (read-only).**
   - `git status --short` at the start (saved to `vc/status_start.txt`), diffed after every Python run and at the end: unchanged.
   - `git log --oneline -5`, `git rev-parse --short HEAD`, `git diff --stat`, and `git diff .gitignore .gitattributes`.
   - `git diff --quiet -- valence_core/m valence_core/adapters/olmo_hf.py`.
   - `git log -1` on de729c4, daca8b0, 9624f70, 5009e77, 0f35954, e0b4f2c, 18b0111, 190ba90 and 2018ffc. `git show --stat daca8b0`.
   - `git show e0b4f2c:scripts/m_analyze.py | shasum -a 256`.
   - `git log --diff-filter=A` on the three NOT-RUN outputs, and `git log -1 -- data/p/gates/G-SHAPE-p.json`.
   - `git check-ignore -q` and `-v` on the call logs, reports, marker, lock, reservation, m's checkpoint and report, and the lexicon. `git check-attr` (all, and `diff text`) on the call log, marker, report and lexicon.
2. **Hashes and counts.**
   - `shasum -a 256` on the open50 answer raw and on G-SHAPE-p.json.
   - `wc -l` on the four texts and the lexicon.
   - `stat` mtimes of p's sources against the author's self-test logs.
3. **Reads.**
   - The four texts in full.
   - In full: register.py, identity.py, stage.py, proxy.py, report.py, keys.py, schedule.py, analysis.py (1-260), guard.py (1-330), scripts/p_analyze.py and scripts/p_sessions.py.
   - RESULTS.md 69-85, 213-266, 364-402, 423-490, 1044-1095.
   - The seat's raws: de729c4's step-6 answers, daca8b0's G-CAL-p answers, and the open50 answers.
   - PROPOSAL-p v0.2 lines 17, 68, 84, 90 and 100. PROPOSAL-m v1.11 lines 271, 302 and 318.
   - m's scaffold.py 300-325, stages.py `out_paths`, resume.py and m_analyze.py signatures, scripts/box_respawn_check.py 20-30, and the scrubbed reviewer reports in `podwatch/rev*/`.
4. **Model-free Python** (`nice -n 19 jlens-qwen36/.venv/bin/python -B`). Scripts are in `podwatch/vc/b/`.
   - `scripts/p_sessions.py --selftest`: 170/170, exit 0.
   - `pkgsha.py`: package sha256 and licence lines.
   - `mshas.py`: m module sha256s against G-CAL-p's `licence_at_run`.
   - `retab.py`: `report.counters`, refined and pinned-only, on G-CAL-p's and G-CAL-OLMo's records.
   - `words.py`: hit words per record and lexicon membership.
   - `residuals.py`: the F-p11 residuals; the lexicon's sha, lines and byte identity to /usr/share/dict/web2.
   - `prod_refusal.py`: the precheck and entry (9) refused in production.
   - `lockreq.py`: `lock_required('OLMo-sft')` categories.
5. **`/usr/bin/python3 -I`.**
   - `cmp_reviews.py`, `cmp3.py`, `cmp3b.py`: the raw against the five scrubbed reviewer reports.
   - Control-character and non-ASCII scans of all texts.
   - G-ANL-F3's battery counts, p's schedules manifest, G-SHAPE-p's provenance, the NOT-RUN bindings, and G-CAL-p's stored counters.
6. **diff and grep.**
   - `diff podwatch/flock_probe.py` against the raw's embedded script.
   - grep (with /usr/bin/grep where a regex mattered) for:
     - hashes in the texts;
     - flock users;
     - step-6 PIN declarations and `BACKEND_OF_RECORD`;
     - BOUNDARY INCIDENT, and m_sessions' STOP prints;
     - counter quotes in RESULTS.md, and any routing record for the entry (9) answer;
     - machine paths in the texts;
     - box mount records.
7. **Not run:** `scripts/p_analyze.py --selftest`, per instruction. Its 525/525 and 14/14 are read from the author's `podwatch/p_analyze_selftest_r5.txt`, whose timing postdates every source edit.
