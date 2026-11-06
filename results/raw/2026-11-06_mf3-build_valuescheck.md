# m package — BUILD (F3): blind values-check of the BUILD entry, the design raw, the review's dispositions and the raw headers (2026-11-06)

*Code's raw. One blind refuter (a general-purpose agent with no access to Code's reasoning) checked five texts read-only, against the working tree, the governing texts and the raws of record: the BUILD entry as drafted for RESULTS.md, `results/raw/2026-11-06_mf3-build_design.md`, §2 of `results/raw/2026-11-06_mf3-build_review.md`, and the headers of the self-test and site-check raws. Result: 93 items, 71 CONFIRMED, 3 FAIL, 19 IMPRECISE. Code re-checked every FAIL and IMPRECISE item at its source before applying it (§2). Seven of them changed code: comments, docstrings, one printed line, one check name and two added self-test cases; no behaviour changed. So the self-test of record and the site check were re-run on the final bytes, and both raws were regenerated with a stricter scrub. The report is reproduced verbatim; the refuter had already masked local paths (`<scratch>`, `<id>`).*

## 1. The report (verbatim)

93 items, 71 CONFIRMED, 3 FAIL, 19 IMPRECISE.

All checks were read-only. The only commands run were `mf3_sessions.py hashes`, small `-B` Python snippets and the reviewer's guard probes, which write to system temp only. `<scratch>` means the session scratchpad. Local paths and the temp-dir id are masked here.

## Claim-by-claim check

### A. The entry (entry_draft_final.md; l. = draft line)

A1 (l.1–3) Package and driver; under the seat's answers of 2026-11-06 (Q1 (C2), Q5, Q6, Q8); the first node of A-m1 §4 step 5 (m:361). **CONFIRMED.** A-m1:60 ("from step 19's first node … `m package — BUILD (F3)` →"); m:361.

A2 (l.4–8) The build list: keys; six banners and the reasoning block; schedules; scaffold (F2 order, the reasoning seed before the menu order, m:159); runner (m:174, m:265); G-VER; read rules; bar table; stage drivers stub-tested and not wired; identity with cap and weights; source guard; G-SHAPE-F3. **CONFIRMED.** Evidence: `ls`; scaffold.py:75–90; mf3_sessions.py:231–233, which refuse time/id/qual/campaign.

A3 (l.9–10) "`mf3` imports ten `valence_core.m` modules unchanged and reaches neither `stages` nor `gshape` (nor `gcal`, either runner, `verify` or `testing`)". **IMPRECISE.** This holds for the production modules:
- A fresh `-I -B` import of the 14 production modules loads exactly audit, banner, bars, corr, guard, keys, readrule, resume, scaffold, schedule.
- `static_import_closure()` returns the same ten.
- But the package's own test double (testing.py, listed at l.24) imports `valence_core.m.testing` (testing.py:19); importing it adds `valence_core.m.testing`.

A4 (l.10–11) Nothing in valence_core/m/, scripts/m_sessions.py, scripts/m_analyze.py or data/m/ changes. **CONFIRMED.**
- `git diff --stat` shows only .gitattributes and .gitignore.
- `git status --porcelain --ignored` on those paths shows only `valence_core/m/__pycache__/`.
- No file there is newer than HEAD (14:53 −0500).

A5 (l.11) m's package_sha256 stays 60199b36…feec. **CONFIRMED.** `package_sha256_of('valence_core/m')` = 60199b36…7feec; 71cc23c's entry moves it to that value.

A6 (l.12) Self-test 136/136; the site check passes ten suites. **CONFIRMED.** Self-test raw :141. Site check: the seven OLMo-build suites plus m_sessions, m_analyze and mf3, each "(exit 0)".

A7 (l.12–13) 12 review items: 1 MAJOR, 5 MINOR, 6 NIT, no blocker. **CONFIRMED.** Review §1: #1 MAJOR, #2–6 MINOR, #7–12 NIT, "No BLOCKER".

A8 (l.13) "10 applied, 2 disclosed". **IMPRECISE.** In §2, #5 is "Applied in part; the rest disclosed (F-2)" and #9 is applied as a descriptive field with its binding flagged (F-7).

A9 (l.14) The self-test and site check were re-run on the final bytes. **CONFIRMED at this check.**
- The raws' hashes equal the working tree: mf3 131d26fc…aa69, driver 48008a53…64cf.
- Last mf3 edit 22:52 UTC (mtime); self-test 22:53; site check 22:53:56–23:00:27.

A10 (l.15–16) The canonical G-SHAPE-F3 run comes later; no lock is written; the four subcommands are refused. **CONFIRMED.** There is no data/mf3/gates/; LOCK-m-F0.md is the only LOCK-m-*; the driver's `refusal()` covers the four.

A11 (l.15) "G-ANL-F3 is not built (Q3's rule)". **IMPRECISE.**
- "Not built" is true: m_analyze.py is unchanged.
- But Q3's rule (answers:26) licenses it now: order (a) is G-ANL-F3 before any LOCK-m-OLMo v0.1, and no OLMo unit is open.
- It is unbuilt because it is the node after G-SHAPE-F3 (m:361; answers:63).

A12 (l.19–21) The design raw's contents. **CONFIRMED.** §1–§10 are present; PINs F1–F60 are 60 contiguous rows; there are seven flags.

A13 (l.23–27) The 15 files named; the driver; 20 schedules plus manifest c7b5df44…3314; the .gitignore block; the .gitattributes line. **CONFIRMED.** `ls`; shasum; .gitignore:264–285 ends the file; the last line of .gitattributes is `/data/mf3/ckpt/** -diff`.

A14 (l.22) "Files added (Q2's statement: no file a lock names is edited)". **IMPRECISE (minor).** .gitignore and .gitattributes are edited (`git status` shows M), not added. The paraphrase of Q2 is fair (answers:20), and no LOCK-*.md names either file.

A15 (l.30) Licence (a): 131d26fc…, 15 files, computed by `valence_core.m.resume.package_sha256_of`, imported. **CONFIRMED.** Recomputed; guard.py:116–118 delegates to it.

A16 (l.31–32) Licence (b): the eleven abbreviated hashes. **CONFIRMED.** `shasum -a 256` of each file; they match site-check :1846–1856.

A17 (l.33–34) Every non-stub stage checks (a), (b), the analyzer, the lock's text and the weights at start. **CONFIRMED.** stages.py:931, :1183 and :1395 call `_licensed` → `_licence` (which returns early on the stub, :377–379) → `licence_problems`.

A18 (l.34) The lock names each hash, and each m file by path and sha on one line. **CONFIRMED.** stages.py:363–375.

A19 (l.35) HF_HUB_OFFLINE must be "1" and refs/main must name the bound revision. **CONFIRMED.** stages.py:343–361.

A20 (l.36–37) The import set is Q1's list plus guard, resume, scaffold and readrule (F-4). **CONFIRMED.** answers:12; `guard.M_MODULES`.

A21 (l.38–40) The OLMo build's edits (gcal.py, resume.py, scripts/m_sessions.py) landed at 71cc23c; resume.py there is 78f2fc8e…8fb7. **CONFIRMED.**
- `git show --stat 71cc23c` lists those three files.
- `git show 71cc23c:valence_core/m/resume.py | shasum` = 78f2fc8e…8fb7, equal to the working tree.
- No later commit touches the m paths.

A22 (l.41–42) The readiness list. **CONFIRMED.** Matches the driver's wiring and the stages functions; there is no G-ANL-F3 and no Q-F3 G-PWR.

A23 (l.43–45) Q3's calendar fact; neither order fixed; the seat recommends (b). **CONFIRMED.** No LOCK-m-OLMo-*.md exists; data/m/ckpt holds no OLMo checkpoint; answers:26.

A24 (l.45–49) The riding texts by anchor. **CONFIRMED.** A-m1:44 (§2.5's three items); VERDICTS_read.md:83; round2.md:19.

A25 (l.50–55) Q5 and Q8 as built. **CONFIRMED.**
- `cap_trigger` (stages.py:982–995) counts `cap_hit` over all six sessions' lines.
- `_contrast_block_time` carries the per-line booleans.
- `prior_gate` (:464–475) re-computes the cap and refuses any other ("NOT THE FIXED CAP").
- runner.py:183–185 ends the session at a line's scaffold fire; `prepick_excluded` = forced, or ci 0.
- The echo is `echo_lines` plus m's `harness_echo`, a containment test.
- `gid_decide`; `scaffold.assert_boundary` in both forms.

A26 (l.57–59) The guard is m's scanner, subclassed; six overrides; mf3's guard the one licence (m:267); m's battery reproduces. **CONFIRMED.** `vars(_F3CallSiteScan)` holds exactly the six. m_guard's battery counts are 17 smuggles, 6 gap groups, 75 must-fire and 11 must-not-fire. m:267 reads "Q-F0's G-ID licenses nothing for F3".

A27 (l.60) At G-TIME-F3 a contrast line exclusion prints `excluded@free`, with no class. **CONFIRMED.** readrule.py:328–329.

A28 (l.61–62) "reported, not fired. It no longer pauses, since m:271 says "on Qwen no such pause exists"". **IMPRECISE.**
- The behaviour is as stated (stages.py:1010–1015; `bars.no_test`), and the quote is verbatim.
- But m:271's "no such pause" is the OLMo G-TIME pause on an AuditSpec- or echo-claimed round, and its "reported, not fired" is G-TIME-F0's realised n of 2–4.
- m:271 says nothing about n = 0. That application is Code's B30/F52 reading.

A29 (l.63–64) G-F3 reports the contrast sessions' first lines; later lines are withheld. **CONFIRMED.** readrule.py:440–467.

A30 (l.65–66) `meta_identical` is descriptive. **CONFIRMED.** stages.py:1129–1143; `gid_decide` reads `identical` only.

A31 (l.67) The self-tests script the production `""` at the cap. **CONFIRMED.** testing.py:151 (`l0=_cap("")`); runner.py:245.

A32 (l.68–69) Two findings disclosed: #2 (F-6) and #11. **CONFIRMED.** Review §2.

A33 (l.70–73) G-SHAPE-F3: 5,632 placements over A1, A2 and A3; the `reasoning+seg+gold` control at the free phase; Layers R, S and T; the trial passes. **CONFIRMED.** Site check :1834–1842: 2816 + 1408 + 1408; the control 1408/1408, 704/704, 704/704; Layer R 8448; Layer T 640 joins; PASS.

A34 (l.74–77) The sealed totals line is imported; the binding is c000ac2c…3282 / 03922eed…1e26; the rest comes with the wiring (F-2); O2-3's forms go into the checklist. **CONFIRMED.** resume.py:72; `weights_binding` recomputed on the hub snapshot; driver docstring :22–28.

A35 (l.75–76) "the campaign's ruling refusals (O4-1, O1-3, RM4-1), its help (VC4-1, VC4-2)". **IMPRECISE (minor).**
- RM4-1 is a RULING-line note, not a refusal (driver docstring :24–25; 71cc23c's message).
- VC4-2 is the module docstring's reason, not help (2026-10-18_m-campaign-driver_review.txt:205–207).

A36 (l.78–86) F-1 to F-7 match §10; each PIN is strikable until v1.0. **CONFIRMED.** answers:50.

A37 (l.89) "Local absolute paths are scrubbed in the committed copies." **FAIL.**
- The self-test raw keeps `/var/folder` at :104 and `olders/g3/<id>/T/tmp…/mf3/ckpt/camp-stop.json` at :115.
- The site-check raw has the same forms at :1794 and :1805.
- These are paths cut by `_short`'s 160-character truncation, so the scrub missed them; the per-user temp-dir id survives in both raws.

### B. The design raw

B1 Header: answers path, aec58440…4df3, committed at dc1ffe1; N1–N6; the routing quote; the m sha 42ab36ec…6c6b; A-m1 at f26bc59; the PIN terms. **CONFIRMED.** shasum; `git log`; RESULTS.md:367 (the routing, verbatim); answers:50.

B2 §1 package bullet; 60199b36…feec asserted by the driver's self-test. **CONFIRMED.** mf3_sessions.py:175–178 checks the prefix and 18 files.

B3 §1 imports: the ten = `M_MODULES`; Q1's list plus four; the closure definition; the never-reached list; the `-I -B` check; the static half at every stage start; `M_HASHED` = eleven files (finding 7). **CONFIRMED.** guard.py:61–66, :180–232; stages.py:180 and `_begin` :668.

B4 §1 the `guard` bullet ("the insulated read (…) and the laptop checklist"). **IMPRECISE.** Since finding 1, mf3 also reuses m.guard's call-site scanner, and both the bullet and guard.py:57's PIN text omit it:
- `_CallSiteScan`, subclassed (guard.py:277)
- `_bindings` (:293) and `_guarded_defs` (:368)
- `_LICENSED_FNS` and `_GUARDED_CALLEES` (:256–257), and `GID_CRITERION` (:46)

B5 §1 licence L2, parts (a)–(g). **CONFIRMED.** stages.py:278–375.

B6 §1 the driver: what is wired and what is refused. **CONFIRMED.** mf3_sessions.py:209–235.

B7 §1 the data: 20 files plus manifest c7b5df44…; the per-directory .gitignore block; ckpt `-diff` (m:318); data/m/schedules untouched. **CONFIRMED.** `git check-ignore -v` admits the JSON files and ignores `*.tmp`; `git check-attr diff` gives unset.

B8 §2 table rows (G-SHAPE-F3; G-ANL-F3 (m:291, Q3); LOCK v0.1 (m:292); G-TIME-F3; G-ID-F3; G-F3; G-PWR (m_gpwr.py is Q-F0's; m:298); campaign; G-VER). **CONFIRMED.**

B9 §2 the "cap fixed" row: "each later stage's cap checked against the trigger re-computed from G-TIME-F3's checkpoint". **IMPRECISE.** The re-computation happens for id and qual only (stages.py:468–472). The campaign is checked against G-F3's recorded cap (:473–475), as F6 states.

B10 §2 the F-1 paragraph's quote. **CONFIRMED.** 2026-10-13_m-design-to-code_G-TIME-F0_read.md:45.

B11 §3 the per-file descriptions. **CONFIRMED.** For example, resume `IDENTITY_KEYS` = m's 18 plus 4.

B12 §4: 60 rows F1–F60, and every site exists under its name. **CONFIRMED.** `resume.Identity` is the function at resume.py:143; `stages.run_gid_pair_f3` is at :1167.

B13 §4: for F1–F18, F20–F57, F59 and F60, the code does what the reading says. **CONFIRMED.** For example:
- F2 vs m guard.py:181–206 (plus the cap)
- F43 schedule.py:54: the row sums to 24,000, and 23,328 with the 3,680 prefix
- F40 vs m runner_qwen.py:68–88
- F53 vs m banner.py:78–81
- F54–F55 verify.py:147–179
- F59 stages.py:1129–1143
- F60 readrule.py:440–467

B14 §4 F19. **IMPRECISE.** The behaviour is as read, enforced in `prior_gate` (F6). But two code texts still carry the reading finding 4 found wrong for G-ID-F3:
- The site's own PIN (scaffold.py:127–129): "every later stage at the fixed cap (60 or 120) the lock records after the trigger (LOCK-m-F3 v0.2, m:294, m:296)".
- F8's site docstring (stages.py:561): "the fixed cap the lock records at every later stage".

B15 §4 F58 "the overrides are exactly the six methods that name m's module". **IMPRECISE.**
- The set is right and asserted, and m's battery reproduces.
- But m's `flag` (guard.py:566–567) names no m module.
- Three non-overridden methods name m's `run_gid_pair` in their messages: `_true_into` :658, `visit_Dict` :703, `_check_cached_value` :779 and :786. mf3's `flag` renames those messages.
- The same wording is at guard.py:240 and in the self-test check's name.

B16 §5 "Code's spec map (scratch, items B1–B32) named 32 open places". **IMPRECISE.**
- The claim is unanchored: the spec map is scratch.
- The committed prebuild block says "Thirty-one places … and one build hazard" (2026-11-06_f3-build_code-to-design_prebuild.md:178).
- The seat counts seven ruled items and "The other twenty-four readings" (answers:50, :58).

B17 §5 "B1/B3 (Q8: cap reached without a newline — F26, F27)" listed under the seat's rulings. **IMPRECISE.** F26's "empty = ws_norm empty" is labelled as Code's own PIN (lines.py:88) and no seat ruling covers it. Q8 rules only the cap item (answers:52).

B18 §5 "B14 (Q8: … pre-pick on line 1 — F22, F24)". **IMPRECISE.** Q8 says only "the guard's pre-pick count includes it" (answers:53); "line 1" is Code's reading via m:308. The same attribution is in F24's "(Q8)" and in readrule.py:443.

B19 §5 the other seat mappings: B2, B13 (its quote faithful to answers:54), B6, B32, B31; Q5 rules B8 and B9. **CONFIRMED.**

B20 §5 "the rest are Code's PINs above". **IMPRECISE.**
- B10–B12, B19, B20, B24 and B27–B29 have no register row.
- B16's pointer "F38: `reasoning_cap` beside … `stop_cap`" lands on F38's path reading (resume.py:182–186).

B21 §6 the calendar fact; orders (a) and (b); the seat's recommendation. **CONFIRMED.** "No pod is up" is checked against the record only: there is no pod start and no BACKEND entry after 2026-10-05 (RESULTS.md:549). Live pod state was not queried.

B22 §6 the riding texts 1–5, with anchors and quotes, and item 4 at :85. **CONFIRMED.**
- step17_addendum.md:11; RESULTS.md@18c32df:85–89.
- VERDICTS_read.md:83 and :85: both quotes verbatim.
- round2.md:19: verbatim, the bracket a gloss.
- step15.md:255–262: "Code's default: no change." is at :262.

B23 §7 the composition. **CONFIRMED.**
- m gshape.py:11–29 has Layers A, C and S and "No model, no tokenizer, no generation".
- m:277 does not mention a tokenizer.
- answers:58.
- m gshape.py:750 → n 5–8.
- mf3 gshape.py:337 and :456–462 (the scope text).

B24 §8 Q6's carry-overs. **CONFIRMED.**
- resume.py:72.
- m_sessions.py:1003–1079 holds MLXLM_USE_MODELSCOPE, the local-path check and the offline resolution; the SNAPSHOT line is at :1082.
- Driver docstring.

B25 §9 the binding: revision c000ac2c… (LOCK-m-F0 v0.2's); 03922eed…; over config, tokenizer, index and three weight files. **CONFIRMED.** Recomputed; `git show db7d970:LOCK-m-F0.md`:217.

B26 §10 F-1 to F-7. **CONFIRMED.** m:263: "never a tag, a free round's index, or the render".

### C. The review raw §2

C1 Preamble: 130 → 136; guard +2; stages +4, as named. **CONFIRMED.** Comparing the reviewer's 130/130 output (`<scratch>/review/selftest.txt`) with the raw: guard 9 → 11 and stages 19 → 23, the other modules equal, and the added check names match.

C2 #1 re-check: 14 forms; 11 silent under the old mf3 and flagged by m; Q-F0's licence silent under both; two flagged by both; m's `_CallSiteScan` at m guard.py:438–858. **CONFIRMED as far as checkable.** Re-running probe_guard.py, m flags 13 of 14 and is silent only on Q-F0's licence, and the class spans :438–858. The old mf3 column cannot be re-run: that checker is replaced.

C3 #1 "imported and subclassed, never copied". **IMPRECISE.** The six overrides restate m's method bodies with mf3's names. mf3's `_licensed` (:314–336) differs from m's (:539–564) only in docstring and line wrap, and `__init__` (:278–294) restates m's :439–454.

C4 #1 "overrides exactly the six methods that name m's module". **IMPRECISE.** As B15.

C5 #1 mf3's guard is the one licensed binding; `run_gid_pair_f3`'s module-level body the one exemption; `run_session_f3` guarded; the override set asserted; m's battery (17 smuggles, 6 groups, 75 must-fire, 11 must-not-fire). **CONFIRMED.** guard.py:296–347; self-test raw :58–59.

C6 #1 "31 Q-F3 smuggles … and each form of the review's (a)–(h)". **IMPRECISE (minor).**
- There are 31 (guard.py:525–559), and each lettered item has at least one case.
- Two forms the reviewer named are not among them: (a)'s lambda parameter and (b)'s class-attribute alias. They flag only in the probe re-run.

C7 #1 mf3 and the driver are clean; 18 of 19 probe forms flag; the 19th passes `path_cached` positionally (keyword-only, so TypeError) and m is silent on it; "proves statically" is replaced by m's declared limits. **CONFIRMED.**
- `check_call_sites` over mf3 and the driver returns [].
- Re-running the probes: 14/14 and 4/5 flag.
- m is silent on `run_session_qwen(a, sc, None, (), True)`.
- runner.py:107–108; guard.py:15–17 vs m guard.py:42–44.

C8 #2: the re-check (the list length is the number of free choices reached; the Q5 and m:263 quotes are verbatim) and the disposition. **CONFIRMED.**

C9 #3: ruling (h) at m readrule.py:98–106 ("with no class"); `excluded@free` at G-TIME-F3; `excluded@reasoning` gone from `_PRINTED_RX` and `_LINE_RX` (readrule.py:46, :54–57); a line-1 STOP names its bar, as m's `announce_stop` does (m stages.py:1218–1238; mf3 stages.py:732–747). **CONFIRMED.**

C10 #4: the m:294–296 quotes are verbatim; `PRIOR_STAGE`; `prior_gate` re-computes and refuses; the campaign refuses any cap but G-F3's; the self-test chains 5/36 → 120 and 2/36 → 60 and checks the refusals. **CONFIRMED.** stages.py:395, :464–475, :1891–1931, :1999–2003.

C11 #4 "PINs F6, F11 and F19 … are corrected". **IMPRECISE.** The register rows and the F6 and F11 site PINs are corrected. The F19 site PIN (scaffold.py:127–129) and F8's docstring (stages.py:561) are not (see B14).

C12 #5: `qwen_snapshot` at scripts/m_sessions.py:1003–1079; part (g) now requires `HF_HUB_OFFLINE` exactly "1" and refs/main, as raw text, equal to the bound revision, then hashes that snapshot; `QWEN_MODEL_ID` and `hub_repo_dir` live in mf3.resume and are used by gshape and the driver; a hub-cache fixture; four new refusals; the rest comes with the wiring. **CONFIRMED.** stages.py:343–361 and :2070–2128; gshape.py:96, :231. The old `_snapshot_dir` is gone, so it cannot be checked.

C13 #6: the m:271 fragments are verbatim; m has no no-test status (`binom_sf(0, 0)` = 1 > α); the NO TEST line, `no_test`, no PAUSE; the all-forced case ends PASS. **CONFIRMED.** stages.py:1010–1015; self-test raw :101.

C14 #7: m/__init__.py is docstring-only (its AST body is one Expr); `M_HASHED` is used by the licence, the identity, the driver (eleven lines) and the sources map. **CONFIRMED.**

C15 #8: the Q1 (C2) quote; LOCK-m-F0.md:145–148; the one-line rule; two new refusals. **CONFIRMED.**

C16 #9: the anchors m scaffold.py:385–391 and mf3 scaffold.py:183–186; the m:281 and m:295 criterion; the PASS case with `meta_identical` false. **CONFIRMED.**

C17 #10: m testing.py:218–222; testing.py:151–152; runner.py:245; gshape.py:99–104; the counts {empty 2, cap 3} and 4 defect lines (readrule.py:579, bars.py:378). **CONFIRMED.** The "from" counts belong to replaced code and cannot be checked.

C18 #11. **CONFIRMED.** gshape.py:434–437, :337, :460–462.

C19 #12 re-check: "Q8 calls a line-1 fire pre-pick". **IMPRECISE.** As B18. The m:297 and m:271 quotes are verbatim.

C20 #12 disposition. **CONFIRMED.** readrule.py:440–467; the hair list also keeps forced triggers.

### D. The two raw headers

D1 Self-test raw: mf3 131d26fc…aa69, driver 48008a53…64cf. **CONFIRMED.** Recomputed.

D2 Laptop, Python 3.12.9, the jlens venv; no model, no pod; the tokenizer read offline. **CONFIRMED.** The venv reports 3.12.9; gshape.py:228–235 reads tokenizer.json from the snapshot.

D3 Run after the last edit; stamp 22:53 UTC; HEAD 1d51673 plus the working tree; m's package 60199b36…feec. **CONFIRMED.**

D4 Tally "136/136". **CONFIRMED.** 136 `[PASS]` lines.

D5 "Local absolute paths scrubbed … nothing else changed." **FAIL.**
- Unscrubbed fragments remain at :104 and :115 (see A37).
- Compared with the unscrubbed output (`<scratch>/selftest_final.txt`), the scrub also deleted non-path text: `_short`'s "..." marker at :111, and the `/mf3/...` tail at :115 (`REPORT /var/folders/…/mf3/...` became `REPORT <tmp>`).

D6 Site check: what ran, from the repo root with the jlens venv. **CONFIRMED.** These are the seven suites of 2026-11-06_m-olmo-build_sitecheck.txt; e2d_closure_verify3.py ran without `--selftest`, as this header writes it.

D7 Stamps 22:53 → 23:00 UTC. **CONFIRMED.** The date -u stamps are 22:53:56 and 23:00:27.

D8 Ten tallies, every exit 0; the trial PASS, exit 0. **CONFIRMED.** :161, :231, :256, :280, :332, :353, :390, :1239, :1690, :1831; exit=0 at :1842 and :1859.

D9 "(the bytes of the self-test raw beside it)". **CONFIRMED.** The hashes section and the trial line give 131d26fc…; the mf3 section equals the self-test raw except the temp-dir name.

D10 "Local absolute paths scrubbed as in the self-test raw … nothing else changed." **FAIL.**
- `/var/folder` remains at :1794, and `olders/g3/<id>/T/tmp…/…` at :1805.
- The "..." marker is dropped at :1801, and the `/mf3/...` tail at :1805 (compared with `<scratch>/sitecheck_out/mf3_sessions.txt`).

## FAIL items and corrections

- **A37.** Re-scrub both raws first. Map the truncated forms (`/var/folder…`, `…olders/g3/<id>/T/tmp…/…`) to `<tmp>`, keep the "..." markers and the path tails, then keep the sentence. If the raws are committed as they stand, write: "Local absolute paths are scrubbed in the committed copies, except two truncated fragments of the temp root in the self-test raw (:104, :115) and in the site-check raw (:1794, :1805)."
- **D5.** After the re-scrub: "…temp and scratch roots, including fragments cut by the self-test's 160-character truncation, as <tmp>, the home directory as <home>; nothing else changed." As it stands: "…; the fragments at :104 and :115 are not scrubbed, and at :111 and :115 the scrub also removed the truncation marker '...' and the path tail '/mf3/...'."
- **D10.** The same correction as D5, with :1794 and :1805 unscrubbed and :1801 and :1805 over-scrubbed.

## IMPRECISE items and corrections

- **A3.** "`mf3`'s production code imports ten `valence_core.m` modules unchanged and reaches neither `stages` nor `gshape` (nor `gcal`, either runner, `verify` or `testing`); only its self-test double, `testing.py`, imports m's `testing`."
- **A8.** "10 applied (finding 5 in part, its rest disclosed under F-2; finding 9 as a descriptive field, its binding flagged F-7), 2 disclosed."
- **A11.** "G-ANL-F3 is not built (it is m:361's node after G-SHAPE-F3; its commit lands under Q3's rule)."
- **A14.** "**Files added and edited** (Q2's statement: no file a lock names is edited)".
- **A28.** "A gate-stage bar at realised n = 0 is reported, not fired, and no longer pauses: Code's revised B30, by analogy with m:271's Qwen rule ("reported, not fired", said of G-TIME-F0's realised n 2–4; "on Qwen no such pause exists", said of OLMo's G-TIME pause) (finding 6)."
- **A35.** "the campaign's ruling handling (O4-1 and O1-3, refusals; RM4-1, the RULING-line note), its help and docstring sentences (VC4-1, VC4-2)".
- **B4.** Append to the `guard` bullet, and to guard.py:57's PIN: "and, since finding 1, its call-site scanner (`_CallSiteScan`, subclassed; `_bindings`, `_guarded_defs`, `_LICENSED_FNS`, `_GUARDED_CALLEES`, `GID_CRITERION`)".
- **B9.** "applied from G-ID-F3 on: G-ID-F3 and G-F3 refuse any cap but the trigger re-computed from G-TIME-F3's checkpoint, and the campaign any cap but G-F3's (m:294–295)".
- **B14 / C11.** Change scaffold.py:127–129 to "…and every later stage at the cap G-TIME-F3's trigger fixes (m:294–295), checked by stages.prior_gate (F6) and recorded at LOCK-m-F3 v0.2 (m:296)". Change stages.py:561 to "…and, from G-ID-F3 on, the cap G-TIME-F3's trigger fixes". Then C11's "PINs … are corrected" holds. Until then: "the register rows and the F6 and F11 site PINs are corrected; the F19 site PIN and `_extra`'s docstring are not."
- **B15 / C4.** "the overrides are six: the four that bind m's guard module or file (`__init__`, `_flag_licensed_bindings`, `_is_guard_alias`, `_licensed`), `in_gid` (m's G-ID function name) and `flag` (renaming m's names in every inherited message, among them those of `_true_into`, `visit_Dict` and `_check_cached_value`)". Apply the same wording at guard.py:240 and in the self-test check's name.
- **B16.** "Code's prebuild block counted thirty-one open places and one build hazard (prebuild.md:178); Code's scratch spec map numbers them B1–B32 (not on record)."
- **B17.** "B3 (Q8: cap reached without a newline — F27); B1 (Code's PIN: empty = ws_norm empty — F26)", with B1 moved to Code's PINs.
- **B18 / C19.** "B14 (Q8: a line's scaffold fire is an exclusion event that ends the session and is in the guard's pre-pick count — F22; Code's reading, by m:308, that only a line-1 fire is pre-pick — F24)". In C19: "Q8 puts a reasoning-line scaffold fire in the guard's pre-pick count; Code reads only a line-1 fire as pre-pick (m:308)." Drop "(the seat's Q8: …)" at readrule.py:443, or reword it the same way.
- **B20.** "the rest are Code's readings: rows as listed; B10–B12, B19, B20, B24 and B27–B29 without a register row"; and "B16 (`resume.Identity`: `reasoning_cap` beside Q-F0's `stop_cap` 60; no register row)".
- **C3.** "mf3's checker is now m's scanner, imported and subclassed: the scanner is inherited, and six methods are overridden with mf3's names (restated from m's)".
- **C6.** "…and at least one form of each of the review's (a)–(h); the lambda-parameter form of (a) and the class-attribute alias of (b) are covered only by the probe re-run, where both flag."

## 2. Code's dispositions (each re-checked at source first)

| item | re-check at source | disposition |
|---|---|---|
| A37, D5, D10 (FAIL) | The unscrubbed outputs: m's and mf3's self-tests print `str(e)[:80]`-style and 160-character cuts, so a temp path can end mid-root (`/private/var/'`, `/var/folder...`) or start mid-root after the cut (`...olders/g3/<id>/T/tmp…/mf3/...`). The old scrub matched only whole roots, and its `/private/…` rule swallowed whatever followed. | **Applied.** A stricter scrub maps each root, whole or cut, to its placeholder: the temp root with its mkdtemp name, the session scratch, the repository and the home directory. A cut root is a head that stops where the text stops following it, a tail that starts at a token boundary or after "...", or a run of five or more characters of an identifying part (the temp-dir id, the user name, the session id) cut on both sides, as in `"<id fragment>...` in m's self-test. The "..." markers and the path tails are kept. It then checks that no user name, no `/Users/`, `/var/folders` or `/private/`, and no five-character piece of the per-user temp id survives. Both raws are regenerated from the final run with it, and their headers say so. |
| A3 | `testing.py:19` imports `valence_core.m.testing` (the test double, outside the production closure). | **Applied** in the entry, as suggested. |
| A8 | Review §2, rows 5 and 9. | **Applied** in the entry, as suggested. |
| A11 | The prebuild answers' Q3 (answers:26) and the task's own boundary: stop before G-ANL-F3, m:361's next node. | **Applied** in the entry: "G-ANL-F3, m:361's node after G-SHAPE-F3, is not built (its commit lands under Q3's rule)". |
| A14 | `git status`: `.gitignore` and `.gitattributes` are modified, not new. | **Applied** in the entry: "Files added and edited". |
| A28 | m:271: "reported, not fired" concerns G-TIME-F0's one-session boundary; "on Qwen no such pause exists" contrasts OLMo's G-TIME pause. | **Applied** everywhere the reading is stated, as Code's reading by analogy: the entry, F52, the review's row 6, `bars.no_test`'s PIN and docstring, the stage's printed NO TEST line ("(B30, by analogy with m:271)") and the self-test check's name. |
| A35 | The driver docstring and 71cc23c's message: O4-1 and O1-3 are refusals, RM4-1 is a RULING-line note; VC4-2 is a docstring reason. | **Applied** in the entry and in the design raw §8. |
| B4 | guard.py imports `_CallSiteScan`, `_bindings`, `_guarded_defs`, `_LICENSED_FNS` and `_GUARDED_CALLEES` from m's guard since finding 1. | **Applied** to the design raw's `guard` bullet and to guard.py's module-set PIN. |
| B9 | stages.py `prior_gate`: the trigger is re-computed for `id` and `qual`; the campaign compares G-F3's recorded cap. | **Applied** to the readiness row, as suggested. |
| B14, C11 | scaffold.py's F19 PIN and `_extra`'s docstring still said "the lock records". | **Applied:** both texts now carry the trigger's cap from G-ID-F3 on (m:294–295), checked by `prior_gate`, recorded at v0.2 (m:296). The review's row 4 now names them. |
| B15, C4 | m's `flag` names no module; m's `_true_into`, `visit_Dict` and `_check_cached_value` name `run_gid_pair` in their messages. | **Applied** in F58, in the review's row 1, in guard.py's scanner PIN and in the self-test check's name. The six are the four that bind m's guard module or file, `in_gid`, and `flag` (which renames m's names in every inherited message). |
| B16 | prebuild.md:178: "Thirty-one places … and one build hazard"; the seat's "The other twenty-four readings" (answers:58). | **Applied** in §5: the prebuild block's count, anchored; the scratch map numbers them B1–B32, the hazard being B32; the seven Q8 rulings named. |
| B17 | answers:52 rules the cap item only; lines.py's empty-line PIN is Code's. | **Applied:** B3 (F27) under the seat's rulings; B1 (F26) under Code's readings. |
| B18, C19 | answers:53: "the guard's pre-pick count includes it". m:308: "no hair trigger fired up to and including the first reasoning line (Q-F3)". | **Applied:** the line-1 boundary is attributed to m:308's domain in §5, in F24, in readrule.py's `_contrast_block` PIN, in the review's row 12 and in the entry. |
| B20 | §5's PIN list. | **Applied:** §5 splits Code's readings into those with a register row and those without (B10–B12, B16, B19, B20, B24, B27–B29); B16's pointer now names `resume.Identity`. |
| C3 | mf3's `_licensed` and `__init__` restate m's bodies with mf3's names. | **Applied:** "never copied" is withdrawn in the review's row 1, F58 and guard.py's PIN. The scanner is inherited; the six overrides restate m's methods with Q-F3's names. |
| C6 | The 31 smuggles lacked (a)'s lambda parameter and (b)'s class-attribute alias. | **Applied:** both are added (33), and both fire. The review's row 1 says so. |

Every edit above that touched code was to comments, docstrings, one printed line, one check name and two added self-test cases; no behaviour changed. The self-test of record was re-run after the last edit (136/136; guard's smuggle check now runs 33), and so was the site check; the BUILD entry's hashes are those of these bytes.
