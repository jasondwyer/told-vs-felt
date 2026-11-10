*Committed by Code as the checker wrote it, on HEAD `3d6f402`. Code's note: the checker's "one reply to the coordinator" (the commands list, last line) went to this session (Code), which briefed it; it sent nothing to the coordinating session. Its seven IMPRECISE items were applied before the commits `e619d3d` and this one.*

# Values-check: block.md, entry_stop.md, close_2258c52.md, note_build_h.md and close_ddd95b0.md (as edited for the record/block split), against the repository at HEAD `3d6f402`, where the code, locks and proposals are byte-identical to `9eed029`

Blind check by a values-checker who did not write the drafts. Sources are cited repo-relative. Abbreviations:
**A** = `results/raw/2026-11-09_p-gtime_design-to-code_answers.md` (the seat's answer on G-TIME-OLMo (p));
**SW** = `results/raw/2026-11-09_o23-sweeps_design-to-code_answers.md` (the sweeps ruling);
**S6** = `results/raw/2026-11-08_p-step6_design-to-code_answers.md`;
**PB** = `results/raw/2026-11-08_p-step6_code-to-design_prebuild.md`;
**GB** = `results/raw/2026-11-09_p-gtime_code-to-design_read.md` (Code's G-TIME block).
`stage.py`, `guard.py` and `gshape.py` are under `valence_core/p/`; `m/stages.py` is `valence_core/m/stages.py`;
`p_sessions.py` and `m_sessions.py` are under `scripts/`. RESULTS.md line numbers are at HEAD `3d6f402`.

**HEAD moved during the check.** It went from `9eed029` to `3d6f402`, the coordinating session's commit of the
sweeps ruling. That commit carries the close on `353502f`'s entry and the ruling's §3 dated notes, among them the
line-53 note at the end of the G-TIME-OLMo (p) entry. It touched only `RESULTS.md` and the sweeps raw. No code file
changed: `git diff --name-only 9eed029` over `valence_core`, `scripts`, the four LOCK files and both proposals is
empty. Both answer raws hash as briefed: A `7b8b1d5f…ffadc3` (in full as briefed), SW `88acd018…830939`.

| # | draft:line | claim (short) | verdict | evidence |
|---|---|---|---|---|
| 1 | block.md:5 | A's path; sha256 `7b8b1d5f…adc3` | PASS | shasum of A matches in full |
| 2 | block.md:6 | code and lock lines are at `9eed029` | PASS | `git diff --name-only 9eed029` over the code, LOCK-m-F0.md, the three LOCK-p files and both proposals: empty |
| 3 | block.md:6–7, :193–194 | nothing built, nothing ran on a model or the box, nothing pushed | NOT CHECKABLE | Code's own conduct. No commit after `9eed029` touches code; HEAD `3d6f402` is the coordinating session's |
| 4 | block.md:11–12 | B5 quote, "LOCK-p v0.2 ×3 committed by path; … [go]" | PASS | verbatim substring of B5 as relayed |
| 5 | block.md:15–16 | p's stage runs m's gate `time` only; the driver refuses `qual` | PASS | stage.py:109; stage.py:838 (`gate=GATE`); p_sessions.py:533–535 |
| 6 | block.md:17–20 | the wiring moves p's `package_sha256` and the driver's sha256, both listed; it makes G-SHAPE-p and G-ANL-p stale; a v0.2 committed first is refused before any load | PASS | stage.py:252, :291–293, :262–271; the precheck (:748) runs before the adapter factory (:831) |
| 7 | block.md:21–23 | the gap: BUILD wired `time` alone and said so only in the driver; neither the BUILD entry nor the G-TIME block raised it; the seat plans v0.2 → G-F0m directly | PASS | rows 37–39 |
| 8 | block.md:25–27 | B5's "LOCK-p v0.2 ×3 committed by path" and the runs are held; v0.2 stays a scratch draft; nothing built | PASS | the quote is verbatim from B5. All three LOCK-p-OLMo-*.md at HEAD are headed v0.1. The scratch directory holds `lock_v02_draft.md` (name only, not opened) |
| 9 | block.md:33–34 | the stage.py:4 quote | PASS | exact substring of stage.py:4 |
| 10 | block.md:35 | `:109`, `GATE = "time"` | PASS | stage.py:109 |
| 11 | block.md:36 | `:315–317`: one session per arm (m:302's G-TIME form) | PASS | stage.py:315–317; m:302 "two sessions, one per arm" |
| 12 | block.md:37–38 | `:420–428`: `out_paths` names the call log, marker, lock file and p's report as `{unit}_{GATE}_p…` | PASS | stage.py:420–428 |
| 13 | block.md:39 | `:744`: `run_time` is the only stage entry point and runs m's stage with `GATE` | PASS | stage.py:744 is the def; :838 calls `m_stages.run_gate_stage(…, gate=GATE, …)`. The module's other public functions are checks and report builders |
| 14 | block.md:40–41 | nothing passes `prior_ckpt`; m's `qual` requires it (m/stages.py:1449–1460, :644, :784) | PASS | the string "prior" appears nowhere in stage.py. m/stages.py:1457–1458 ("required for the qualification stage"), :644 (`"qual": "time"`), :784, :805–807 (PRIOR STAGE REQUIRED) |
| 15 | block.md:43, :45 | the driver refuses `qual` with exit 2; `:95–98` holds `STAGE_CMDS` and `STAGE_AFTER`'s "its checkpoint's LOCK-p v0.2" | PASS | p_sessions.py:96, :98; refusal and exit 2 at :533–535 |
| 16 | block.md:46–47 | the `:59–60` docstring quote | PASS | exact, with the two lines joined |
| 17 | block.md:48 | `:326–329`: the self-test asserts both refusals | PASS | p_sessions.py:326–329 (rc 2 plus the refusal text) |
| 18 | block.md:52 | m's OLMo qualification stage exists (m/stages.py:154) | PASS | m/stages.py:154; `run_gate_stage` admits any gate in `GATES` (:1463) |
| 19 | block.md:53–54 | m_sessions.py:680 `OLMO_QUAL_LOCK_LINE`; the check at `:933` | PASS | m_sessions.py:680, :932–933 |
| 20 | block.md:55–56 | p's qual schedule files are in the manifest LOCK-p v0.1 names: n 8 (A0) and n 16 (A0s) | PASS | data/p/schedules: each `_qual_A0-` file has `n` 8 and each `_qual_A0s-` file has `n` 16. Each LOCK-p v0.1 names the manifest's sha256 (LOCK-p-OLMo-sft.md:33) and both qual files (:36–37) |
| 21 | block.md:50 | "Nothing is missing on m's side or in p's data" | PASS | the three cited items hold, and LOCK-p-OLMo-sft.md:98–100 carries the qual keys. This is not an exhaustive audit of everything a qual run needs |
| 22 | block.md:60–61 | the precheck refuses unless the lock at HEAD names, verbatim, every `lock_required` value (stage.py:236–298), computed from the code at the run | PASS | stage.py:236–298, :301–304 (`lock_names`), :363–371; m/stages.py:415–437 (`_committed` reads HEAD) |
| 23 | block.md:61 | "Four of them move with the wiring" | IMPRECISE | `lock_required` also lists p's licence line as a value of its own: "LICENCE valence_core/p package_sha256 … (14 files, valence_core/p/*.py)" (stage.py:294–295; guard.py:93–94; LOCK-p-OLMo-sft.md:53). It carries the package hash, so five listed values move. **Fix:** "Five of them move", adding p's LICENCE line (it carries the package_sha256), or "Four kinds of value move" |
| 24 | block.md:63 | p's `package_sha256` (`guard.package_sha256()`) moves: the wiring edits stage.py | PASS | guard.py:71–72 → valence_core/m/resume.py:328–350 hashes every `*.py` directly in valence_core/p. Recomputed `7a08dbfa…1d24`, equal to LOCK-p-OLMo-sft.md:25 |
| 25 | block.md:64–65 | the driver's key "the driver (scripts/p_sessions.py)" via `guard.driver_sha256()` | PASS | stage.py:291–293; guard.py:87–89. shasum `d91e41e1…a943`, equal to LOCK-p-OLMo-sft.md:48 |
| 26 | block.md:66–69 | G-SHAPE-p: `stale_problems` on p's and m's packages and `gshape_drift_problems` on the sources map and closure; the driver is in the sources map (gshape.py:90 `TOOLING_FILES`) | PASS | stage.py:266–268, :220–233; gshape.py:90, :140–144 (the sources map includes `TOOLING_FILES` and every valence_core/p/*.py) |
| 27 | block.md:70–71 | G-ANL-p: `stale_problems` "on its recorded p package and analyzers" | IMPRECISE | stage.py:270–271 checks m's package too: `p_package_sha256`, `m_package_sha256`, `m_analyzer_sha256`, `p_analyzer_sha256`. **Fix:** "on its recorded p and m packages and both analyzers". The conclusion stands |
| 28 | block.md:73–74 | a v0.2 committed now names the current values; after the wiring the precheck refuses it with exit 2, before the load | PASS | the current package and driver hashes equal v0.1's (rows 24–25). A StageRefusal exits 2 with "nothing loaded" (p_sessions.py:227–230) |
| 29 | block.md:78–80 | m's driver checks that it is committed unmodified and prints its sha256 on the DRIVER line (`driver_problems`, m_sessions.py:983–995); m's lock records the value and does not test it | IMPRECISE | True in substance: `driver_problems` returns the committed blob's sha256 when HEAD and the working tree agree; its callers print the DRIVER line (m_sessions.py:514, :1622, :1739); nothing else uses the hash. But the function spans :983–1000: :983–995 is its def and docstring, and the check is :996–1000. **Fix:** "(`driver_problems`, `scripts/m_sessions.py:983–1000`; the DRIVER line at `:1739` for the OLMo stages)" |
| 30 | block.md:80–81 | LOCK-m-F0 v0.2 §3 records m's driver at its tree and quotes Q3 "Nothing tests a driver hash as a substring" | PASS | LOCK-m-F0.md:784–790, verbatim |
| 31 | block.md:81–82 | quote: "the next lock revision — v0.2 for `id`, v1.0 for `qual`" | PASS | LOCK-m-F0.md v0.2 §3, "Later driver edits", verbatim |
| 32 | block.md:82–83 | m's `qual` wiring could follow v0.2 (m:358's step 14) | PASS | m:358: "13. Commit LOCK-m-F0 v0.2. 14. G-F0m-Qwen (24 sessions)" |
| 33 | block.md:83–84 | Code's departure, in the step-14 entry's ping Q4, was starting that wiring before v0.2's commit | PASS | RESULTS.md:5717 ("Q4, a departure of Code's: the `qual` build began before v0.2's commit"), and that entry's "A departure, Code's (ping Q4)" |
| 34 | block.md:85–86 | m's wiring was the driver's alone; the rule required "no change under `valence_core/m`"; m's stage functions already ran `qual` | PASS | `4630cfd` touched scripts/m_sessions.py and two raws only. RESULTS.md:5761 "Nothing under `valence_core/m` changed". The LOCK-m-F0 quote is verbatim. m/stages.py:154 |
| 35 | block.md:88–89 | `lock_required` lists the package and the driver at every version; the precheck refuses a lock that does not name them (`:365–371`, `:389–390`) | PASS | `lock_required` has no lock-version branch; stage.py:365–371, :389–390 |
| 36 | block.md:93–94 | the pre-build block proposed entry (6) "for every p gate stage and the campaign"; the seat declared it (`de729c4`, §1, Q1) | PASS | PB:27; S6:7; `de729c4` commits S6 (name-only) |
| 37 | block.md:94–95 | the seat's §4 called the package final ("G-SHAPE-p re-run on the final package") and runs v0.2 → G-F0m directly | PASS | S6:26; A:7 ("Next") |
| 38 | block.md:96–97 | `d215d5b` wired `time` alone and said so in the driver's docstring and self-test only, not in the BUILD entry | PASS | `d215d5b` touches stage.py and p_sessions.py. Searched the BUILD entry (RESULTS.md:750–1047) for `qual`, G-F0m, "wired" and "wiring": no hit except "equality"/"equal" containing "qual". The BUILD commit's message, review raw and values-check raw: no "qual" either |
| 39 | block.md:98–99 | the G-TIME block (`2258c52`) asked about v0.2's contents (Q2) and did not say G-F0m needs a build | PASS | GB:134–139. Searched GB for qual, G-F0m, wire/wiring and build: no such statement. Its "no path in this build" (GB:116) concerns reading (i). GB is in `2258c52` |
| 40 | block.md:100–101 | "Code found it at B5's first step, before any edit" | IMPRECISE | Consistency: entry_stop.md:5–6 calls B5's first item the close line on `2258c52`, which the record commit lands before this block. The block's "first step" means LOCK-p v0.2, so the phrase reads two ways. **Fix:** "at B5's LOCK-p v0.2 step, before any code edit". The moment itself is Code's conduct and not checkable |
| 41 | block.md:110 | `fdd79d8`'s artifact is superseded in F-p12's form (`git mv`, kept in history) | PASS | `fdd79d8`: M `data/p/gates/G-SHAPE-p.json`, A `…superseded-2026-11-09.json`. Its message: moved "by hand with git mv … (F-p12: superseded, kept in history)". Its artifact `3c4125a3…1554` = LOCK-p-OLMo-sft.md:28 |
| 42 | block.md:111 | `f8b16d5`'s artifact | PASS | `f8b16d5` adds `data/p/gates/G-ANL-p.json` |
| 43 | block.md:113–114 | batched as G-TIME was (back to back); 24 sessions per checkpoint; uncached | PASS | RESULTS.md:281 ("one run each … back to back"); m:302 (24 sessions); m:267 (OLMo uncached) |
| 44 | block.md:119–120 | (h) quote | PASS | A:45, verbatim. The PIN's label begins at the end of stage.py:35 and its text is :36–38, as the seat cites |
| 45 | block.md:121 | (j) quote | PASS | A:47; verbatim apart from the source's bold on "deferred to the next package move" |
| 46 | block.md:129 | m's counts from the committed gate files (8 + 16) | PASS | row 20; stage.py:316 (the committed gate files' n) |
| 47 | block.md:130–131 | `prior_gate` checks that the prior ended PASS, is this unit's, carries m's proposal pin (F-p8) and is not the stub's | PASS | m/stages.py:814 (unit and stage), :818–822 (accepted proposals), :823 (stub), :839 (PASS). `_licensed` passes `proposal_sha256` and `require_real=not stub` (:1134–1142). p's `identity_extra` carries m's pin (stage.py:323) |
| 48 | block.md:134–135, :138 | 24 sessions, sixteen of them sham; all three G-TIME stages PASSed | PASS | A0s n 16 (sham), A0 n 8; A:17 ("PASS ×3 stand") |
| 49 | block.md:140–141 | m's OLMo campaign was never wired; its looks and cap come from m:330 and G-PWR | PASS | m_sessions.py:674 (`OLMO_DRIVER_STAGES = ("time", "qual")`), :681, :284; m:330 (looks); p:84 (G-PWR; the PI's cap share → v1.0) |
| 50 | block.md:145 | §2 quote: "re-issued above its v0.1 text kept verbatim" | PASS | A:21 |
| 51 | block.md:145–146 | v0.1's text names the package, driver, G-SHAPE-p and G-ANL-p values the move supersedes | PASS | LOCK-p-OLMo-sft.md:25, :48, :28, :29; also its LICENCE line at :53 (row 23) |
| 52 | block.md:151–152 | one `BACKEND OF RECORD` line, v0.1's (`641ee466f4553b6a`); the precheck requires exactly one | PASS | each LOCK-p v0.1 has exactly one line `BACKEND OF RECORD 641ee466f4553b6a`; stage.py:307–312, :372–373 |
| 53 | block.md:153–154 | the text of `OLMO_QUAL_LOCK_LINE`; p's records keep m's unit strings (p:84) | PASS | m_sessions.py:680; p:84 |
| 54 | block.md:155 | "p's `qual` precheck requires it" | IMPRECISE | At HEAD p has no `qual` precheck: `stage.precheck` checks no gate- or version-specific line, and the driver refuses `qual`. This is the check Code proposes (block.md:132). **Fix:** "p's `qual` precheck would require it (Q2 (A))". The m half is true (m_sessions.py:933) |
| 55 | block.md:161–162 | the B3 quote; §3's "Tabulated by Code's own step from the records at each entry" | PASS | B3 as relayed; A:34 (verbatim; bold in the source) |
| 56 | block.md:163 | the sham rounds are in m's reads files, `data/p/reports/OLMo-{ckpt}_{stage}_reads.json` | PASS | the names come from `git show --name-only 2258c52`. A:3 and :13 read the sham sessions from those files. Contents not opened |
| 57 | block.md:164–166 | quote of the list of record's item 2; "Code's step is none of the five" | PASS | SW:36, verbatim; it names five exceptions |
| 58 | block.md:170–171 | the G-TIME entry's table; the reports are the read domain (m:271) | PASS | RESULTS.md:289–293; m:271's pre-VERDICTS read rule; SW:13 ("The reports are the seat's read domain (m:271)") |
| 59 | block.md:177–180 | pod id; "Keep it up"; the two question quotes; PI date | PASS | verbatim as relayed; the pod id as at p:110 |
| 60 | block.md:177, :183 | the pod "stays up and idle"; Code changes nothing on the box | NOT CHECKABLE | the pod's state and Code's conduct; no pod query was made |
| 61 | block.md:180 | B5: "The pod stays up through G-F0m-OLMo (p) [up]." | PASS | verbatim |
| 62 | block.md:182 | $1.79/hr, about $43 a day | PASS | 1.79 × 24 = 42.96 |
| 63 | block.md:187–188 | committed before this block, at `@@RECORD_HASH@@`: the answer, the G-TIME close line, (h)'s note, the C4 close | PASS | placeholder ignored; matches spec_record.json (the three appends) and entry_stop.md:47–49 |
| 64 | block.md:189 | v0.2's §2 text is drafted in scratch, not committed | PASS | as row 8 |
| 65 | block.md:190–191 | the box repo stays at `0afd842`, with G-TIME's fifteen outputs untracked and identical to `2258c52`'s | NOT CHECKABLE | box-side. By name, `2258c52` holds fifteen outputs (6 `ckpt`, 9 `reports`), and `0afd842` is LOCK-p v0.1's commit |
| 66 | entry_stop.md:4–6 | B5 quote; its first item is the close line on `2258c52` | PASS | verbatim from B5 |
| 67 | entry_stop.md:6 | the close line is committed at `@@RECORD_HASH@@` | PASS | placeholder ignored; matches spec_record.json |
| 68 | entry_stop.md:6–8 | the rest is held; v0.2 stays a scratch draft; nothing built | PASS | as rows 8 and 64 |
| 69 | entry_stop.md:10–11 | `time` only (stage.py:109; `run_time`; the `_time_` paths) | PASS | rows 10, 12, 13 |
| 70 | entry_stop.md:11 | the driver refuses `qual` with exit 2 (p_sessions.py:95–98) | PASS | :96 and :98 declare the refused commands; the refusal and exit 2 are at :533–535 |
| 71 | entry_stop.md:11–12 | the `:59–60` docstring quote | PASS | row 16 |
| 72 | entry_stop.md:13–15 | the hashes move and both are listed; G-SHAPE-p stale (sources map) and G-ANL-p stale (recorded package); refused before the load | PASS | rows 6, 24–27 |
| 73 | entry_stop.md:16–17 | m's lock records the driver's sha256 after the run and never tests it; m's `qual` wiring was the driver's alone | PASS | rows 29–31, 34 |
| 74 | entry_stop.md:18–20 | the gap is Code's | PASS | rows 37–39 |
| 75 | entry_stop.md:21 | the block's link path | PASS | the path the brief names; not yet tracked |
| 76 | entry_stop.md:23–31 | the Q1 list; (h)'s wording and (j)'s fix with the move | PASS | matches block.md:105–122 |
| 77 | entry_stop.md:32 | the Q2 summary | PASS | matches block.md:126–143 |
| 78 | entry_stop.md:34–35 | Q3: eight items, the values, v0.1's text verbatim; one BACKEND line | PASS | matches block.md:145–152 |
| 79 | entry_stop.md:36 | "which p's `qual` precheck requires" | IMPRECISE | as row 54. **Fix:** "which p's `qual` precheck would require" |
| 80 | entry_stop.md:37–38 | Q4: Code's step reads the reads files' sham sessions, which item 2's exceptions do not name | PASS | rows 56–57 |
| 81 | entry_stop.md:39–44 | the pod quotes; "B5 adds" | PASS | rows 59, 61 |
| 82 | entry_stop.md:39, :46 | the pod stays up and idle; Code changes nothing on the box | NOT CHECKABLE | as row 60 |
| 83 | entry_stop.md:45 | a build, its reviews, two re-runs and three locks away; $1.79/hr | PASS | consistent with block.md Q1; the figure as relayed |
| 84 | entry_stop.md:47–49 | committed before, at `@@RECORD_HASH@@`: A (`7b8b1d5f…adc3`) with the close on `2258c52`, (h)'s note, the close on `ddd95b0` citing the sweeps ruling (C4) | PASS | the hash matches; `ddd95b0` is the pod session's sweep (its subject); matches spec_record.json |
| 85 | entry_stop.md:50, :52–53 | committed with this entry: the block and its values-check raw; v0.2's §2 drafted in scratch; not pushed | PASS | matches spec_stop.json (the top entry only); row 64 |
| 86 | close_2258c52.md:2–3 | A's path and full sha256 | PASS | shasum exact |
| 87 | close_2258c52.md:3–4 | "committed here by path, as the PI placed it" | PASS | A is untracked in the working tree, and its hash is as briefed. Note: A's header (A:3) says "the PI commits by path"; here Code commits it, as the coordinating session committed SW (whose header says the same) at `3d6f402` |
| 88 | close_2258c52.md:4 | "The seat's read: PASS ×3 stand; the correctness counter declared; (a)–(j) as ruled." | PASS | A:56 (only the capital T differs) |
| 89 | close_2258c52.md:5–10 | section B, verbatim | PASS | diff against the relayed B1–B5: identical |
| 90 | close_2258c52.md:12–13 | Q1: the PASSes stand (§1.4); the seat read the sham sessions redacted and the contrast sessions' forced rounds only, and saw no pick | IMPRECISE | §1.4 and "no pick" are right (A:17, A:3). But the seat also read the contrast sessions' banners: A:3 says "the contrast session's banner and four forced rounds only", A §1.1 reads every banner, and m:271 leaves "the banner, the forced rounds and their responses". **Fix:** "the contrast sessions' banners and forced rounds only". The record's own short form at p:84 and S6:26 omits the banner |
| 91 | close_2258c52.md:14 | Q2: eight items (§2) | PASS | A:23–30 |
| 92 | close_2258c52.md:15–17 | Q3: the counter, descriptive, Code's step; G-TIME's row 29 of 30 (9, 10, 10 of 10) | PASS | A:34 |
| 93 | close_2258c52.md:18–20 | Q4: (a)–(j) accepted; (f) stated; (h) adopted with the note on the BUILD entry (2026-11-09, "p step 6 — BUILD"); (j) deferred | PASS | A:7, :43, :45, :47; RESULTS.md:750 (header) |
| 94 | close_2258c52.md:21–22 | line 53 is corrected by "the dated note above", the coordinating session's (the sweeps ruling's §3) | PASS | Since `3d6f402` the note ends the G-TIME entry (RESULTS.md:325–332), and the dry run below puts this close line directly after it. Line 53 of the values-check raw contains "only hashed". SW:49, :60 |
| 95 | close_2258c52.md:22–23 | the port at line 148: the sweeps ruling's §4 and the PI's push call | PASS | A:52; SW:55. The PI's D1 ("push as is") is quoted in `3d6f402`'s message. Line 148 not opened, per the brief |
| 96 | close_2258c52.md:24–26 | Next: `qual` not wired; the block follows in its own commit; the entry's title | PASS | matches spec_stop.json and entry_stop.md:1 |
| 97 | note_build_h.md:1–3 | sources (A §4 (h), §2 item 6; B4); a *backend* change after the lock STOPs the stage, not a box change as such | PASS | A:28, :45; B4 |
| 98 | note_build_h.md:4 | a new box of the same class gives the same identifier (m:267) and is not detected | PASS | A:45; m:267 ("the backend identifier cannot tell two boxes of one class apart") |
| 99 | note_build_h.md:5–6 | p §6.2's respawn protocol with a new `BACKEND — characterization` entry; a dated note at the lock in force, no re-issue | PASS | A:28; p:110 |
| 100 | note_build_h.md:7 | a differing identifier STOPs and the seat rules; §2 item 6 is the superseding form | PASS | A:28, :45 |
| 101 | note_build_h.md:8–9 | reading (h) above and the PIN (stage.py:36–38) stay as written until the next package move | PASS | reading (h) is in the BUILD entry at RESULTS.md:1024, above where the note lands. The PIN's text is at stage.py:35–38 ("a box change after the lock STOPs the stage", :37). A:45 |
| 102 | note_build_h.md:10–11 | the answer's link and sha256 | PASS | row 1 |
| 103 | close_ddd95b0.md:2–3 | SW's path and full sha256 | PASS | shasum exact; the committed blob at HEAD has the same hash |
| 104 | close_ddd95b0.md:3–4 | committed by the coordinating session at `@@SWEEPS_HASH@@` | PASS | **the value is `3d6f402`**: it added the raw (`git log --diff-filter=A`), and its subject says "closed by the coordinating session" |
| 105 | close_ddd95b0.md:4 | the close text quoted from §5 | PASS | SW:60, verbatim |
| 106 | close_ddd95b0.md:5–8 | §1.2: items 1–12; 3–6 and 8–10 on G-CAL-p; no pick; 384 generations; item 11; item 12 is D2's kind | PASS | SW:19; D2 is the coordinating session's item (SW:14) |
| 107 | close_ddd95b0.md:9–10 | §3: Code's read of record (`ec0d9d3`); the two subagents' prints inert, no departure from m:318 | PASS | SW:20. `ec0d9d3`'s subject: "G-CAL-p of record -- the entry, Code's read of all 384 generations…" |
| 108 | close_ddd95b0.md:11–13 | §4 inert; §5 is the ruling's §4 and the PI's push call; §6 adopted as written | PASS | SW:21–23; the PI's D1 is in `3d6f402`'s message |
| 109 | close_ddd95b0.md:14–15 | the line-53 correction is the coordinating session's dated note (§3) | PASS | SW:49, :60; RESULTS.md:325–332 |
| 110 | close_ddd95b0.md:16–20 | section C verbatim (C1, C2, C4; C3 left out as that session's) | PASS | identical to the relayed C1, C2 and C4, each also verbatim in `3d6f402`'s message. C3 is the coordinating session's (SW:60; C3's "written by this session") |
| 111 | close_ddd95b0.md:21–22 | the rule binds this session, its subagents and its briefs; v0.2 cites it in one line (A §2 item 7) | PASS | SW:33, :40, :44; A:29 |
| 112 | all five, placement | each lands at the end of the right entry | PASS | The provided dry_RESULTS.md is stale: it predates the split edits and `3d6f402`, and its top entry still carries an older text of entry_stop.md. A fresh dry run in the checker's own scratch area used a copy of the current RESULTS.md, spec_record.json (with SWEEPS_HASH=`3d6f402`) and then spec_stop.json. Each header prefix is unique. close_2258c52 lands at the end of the G-TIME-OLMo (p) entry, right after the coordinating session's dated note. note_build_h lands at the end of the step-6 BUILD entry. close_ddd95b0 lands at the end of the pod session's sweep entry, before the coordinating session's. entry_stop lands at the log's top |
| 113 | all five, consistency | block ↔ entry ↔ the closes ↔ the specs | PASS | block.md:187–188 ↔ entry_stop.md:47–50 ↔ spec_record and spec_stop; close_2258c52.md:24–26 ↔ the entry's title; close_2258c52.md:21–22 ↔ close_ddd95b0.md:14–15; the Q1–Q4 summaries match. One wording conflict is row 40 |

113 items: 102 PASS, 7 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE

**Observations (no verdict):**
- Fill `@@SWEEPS_HASH@@` with `3d6f402`.
- The coordinating session's note on the G-TIME entry ends "LOCK-p v0.2 follows on the routing's item B5". close_2258c52 lands directly after it and says "LOCK-p v0.2 ×3 and G-F0m-OLMo (p) wait", with its reason. The two read together correctly, and no change is needed.
- Since `3d6f402` (the PI's D1), origin/main is at HEAD, so `2258c52` and `ddd95b0` are pushed. Both closes still read correctly ("the PI's push call"). They could cite D1 if wanted.
- No address or port appears in any draft (read in full). Line 148 of the values-check raw was not opened.

**Commands run, by kind (no barred form; nothing touched a `data/<unit>/ckpt` or `data/<unit>/reports` file's metadata or content):**
- `git log` with `--format` of ids, subjects and commit times. This includes `-1 --format=%B` for two commit messages, which went to the checker's scratch area and were then searched, and `--diff-filter=A --format` over two named raws.
- `git show --name-only` on `4630cfd`, `de729c4`, `d215d5b`, `2258c52` and `3d6f402`.
- `git show --name-status` on `fdd79d8` and `f8b16d5`. It prints names and status letters only, and neither commit touches a `ckpt` or `reports` path. It is the same kind as the permitted `git diff --name-status`.
- `git diff --name-only` (from `9eed029`, over code, locks and proposals, and `9eed029` to HEAD).
- `git status --porcelain`: bare, and once with the pathspec `valence_core scripts`.
- `git ls-files` (LOCK-p files, two raw paths, data/p/schedules); `git rev-parse` (HEAD, origin/main, one `HEAD:<raw>`); `git cat-file -p HEAD:<the sweeps raw>` piped to shasum.
- `shasum -a 256`: the two answer raws, the schedules manifest and the p driver. An inline Python recomputation of p's package hash read valence_core/p/*.py.
- `wc -l` on code files, RESULTS.md and raws.
- `sed -n`, `head -1`, `cut` and Read on named files outside the protected directories.
- `/usr/bin/grep` (-n, -c, -F, -o) on named single files only. There was no recursive grep, no `git grep`, no `git log -S/-G/-p`, no `rg` and no `find`. Every content search after the coordinator's pathspec correction was again a named-file grep outside `data/`. Line 53 of the p-gtime values-check raw was tested for "only hashed" by count.
- Inline Python (-I) reading data/p/schedules/*.json, a permitted directory, for each file's n; inline Python checking quotes against named files.
- Name-only `ls`: data/p/schedules, the scratch directory, LOCK-* at the root. One `ls -la --time-style` on the scratch directory, which is not a protected directory, failed and printed nothing.
- A dry run: Code's scratch insertion script run on a copy of RESULTS.md in the checker's own scratch area. Nothing in the repo or in the drafts' files was written.
- One reply to the coordinator.
