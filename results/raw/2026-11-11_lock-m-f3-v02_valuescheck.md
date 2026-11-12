# LOCK-m-F3 v0.2: the values-check of the draft and its entry

*Code's raw, PI date 2026-11-11.*
- *What was checked:* the drafted `LOCK-m-F3.md` at v0.2 (its v0.2 part, and the rest against HEAD's file) and the
  entry draft, before the commit.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written.
  - It read four report files and the G-ID-F3 artifact for the figures, and hashed the checkpoints.
  - It imported the driver's lock parsers with every model import blocked, as the brief allowed.
- *Outcome:* 57 items: 41 CONFIRMED, 9 IMPRECISE, 2 FAIL, 5 NOT CHECKABLE.
  - Both FAILs and every IMPRECISE item are applied (below).
  - Its note on `15d2f70` is applied as a pointer in v0.2 §8.
- *Not run:* a second pass. Most changes apply the checker's own fixes, and one adds m:297's sentence verbatim. Code
  checked each against its source by tool: m:297 copied from the proposal by script; m:16; the two precedent rule lines;
  the WIRED sentence's lines `:98–99`.
- *The base re-taken.* v0.2's base moved from `a6c6297` to the HEAD at the commit. Only RESULTS.md changed in between.
  The generator ran again there, and its blocks are identical (the entry says so).
- *Code's masked scan of the checker's transcript* (no output text printed):
  - 190 distinct Bash calls.
  - The ones naming a `ckpt` path are digests (`shasum`), `git log`, `git check-attr`, name-status, and the pathspec
    exclusions.
  - The ones naming a `reports` file name the four report files the brief permitted.
  - The other `data/` paths named are the G-ID-F3, G-SHAPE-F3 and G-ANL-F3 artifacts and the schedules manifest, all
    permitted.
- *This raw:* Code's dispositions, then the report verbatim.
  - The report was extracted by script from the agent's hand-back (the text's sha256 `58911670…`, 202 lines).
  - Its last line, naming two scratch files, is scrubbed: their local root becomes `<tmp>`.
  - The raw holds no other local path, no clock time and no config label.
- *Nothing ran on a model or the box.*

## Code's dispositions

- **44, FAIL: G-F3's bars and the first-pick share are missing.** Agreed: the seat's §5 lists them. v0.2 §9 item 2
  now quotes m:297 in full, its bold dropped, from "G-F3. 40 sessions" to "r for Q-F3 = pooled over all 40". That
  includes the bars, the attractor tally and the first-pick share for sham templates. Its bars agree with lock §8's
  G-F3 rows.
- **40, FAIL: the `id` wiring raw's disclosures miscounted.** Agreed: the raw discloses three things, and "neither
  touches" belongs to the checker's two. The bullet is outside the seat's §5, which asks only for the departures
  ruled, so it is removed rather than corrected. The raw stands as the record of them.
- **6, IMPRECISE: D2's date.** Applied: "with D2 (m:298; D2's date, 2026-12-22, m:16)".
- **11, IMPRECISE: the base.** Applied: v0.2's base is the HEAD at the commit, and the generator was re-run there.
- **30, IMPRECISE: the WIRED sentence's anchor.** Applied: "in the PIN that opens at `scripts/mf3_sessions.py:92` (its
  lines `:98–99`)".
- **32, IMPRECISE: a commitment beyond the routing (the plural).** Agreed. v0.2 now records only the reading: "v0.2
  reads the PIN as the plural". The promise to correct the word at the `qual` wiring is removed, and so is §9's line
  on it.
- **36, IMPRECISE: "or subagent's".** Applied.
- **38, IMPRECISE: `r2:`§3 among the departures ruled.** Agreed: §3 is observations, and the probe change is the
  routing's item 7 [adopted]. The bullet is removed from v0.2 §8, and the entry's line is corrected.
- **42, IMPRECISE: the `qual` wiring's lock check, stated as fact.** Agreed. It is now marked as Code's intent: "Code
  intends it to require v0.2's cap and path lines …; the wiring's entry declares it (Code's; the routing does not ask
  it)". The checker's note is taken too: §9 no longer writes the two strings. Each now appears once in v0.2, at its
  definitional line, and the wiring will test those exact lines.
- **46, IMPRECISE: the precedence sentence's source.** Applied: "(the form of the re-issue's own rule, and of LOCK-p
  v0.2's)".
- **52, IMPRECISE: the entry's "(the licence's (f))".** Applied: (f) covers the analyzer's and the package's sha256 and
  the m-file lines; the proposal's sha256 in full is `stage_identity_extra`'s.
- **12, 48, 49, 54, 55: NOT CHECKABLE.** The generator is Code's scratch tool. The rest are the placeholders and the
  commit, filled at the commit.
- **39's note (`15d2f70`):** applied. v0.2 §8 points to the coordinating session's dated note, which puts an
  observation on §6's ruling on pod note 2 to the seat's next read.
- **The checker's disclosures.**
  - (1) A start-side stamp printed from the artifact's provenance, and stamps seen in records. None is reproduced,
    and no duration was computed.
  - (2) The permitted import of the driver ran `valence_core.m.corr`'s module-level `olmo_roster()`, which reads
    `data/olmo/a1_repair_roster.json`, a file the brief did not list. It is neither a checkpoint nor a report.
  - (3) Item-1 forms.
  - (4) Config labels seen in outputs, none reproduced.
  - (5) A bare `git status --porcelain` at its start printed 31 untracked names, none under `data/`. At its end the
    same listing ran with only a line count printed (46 entries). That was while G-F0m-OLMo (p) ×3, by the
    coordinating session's `15d2f70`, ran on the box, where its outputs are written. Code passes this to the
    coordinating session for the p track.

## The checker's report (verbatim; its last line scrubbed, as above)

**Values-check of the LOCK-m-F3 v0.2 draft and its entry: 57 items. 41 CONFIRMED, 9 IMPRECISE, 2 FAIL, 5 NOT CHECKABLE.**

HEAD was `eb3e08c` at my start and `15d2f70` at my end. Another session committed `15d2f70` during the check; it touches RESULTS.md only. Since `a6c6297`, `git diff --name-status` shows only RESULTS.md changed, with no path under data/. No tracked file is modified.

Notation:
- L:n is a line of `V/LOCK-m-F3.v02.md`; E:n is a line of `V/entry_v02.md`.
- `ans:` is `results/raw/2026-11-10_gid-f3_design-to-code_answers.md`.
- `lock:` is `HEAD:LOCK-m-F3.md`; `drv:` is `scripts/mf3_sessions.py` at HEAD; `A-m2:` is ADDENDUM-m2 v0.5.
- RESULTS.md anchors are pinned at `@eb3e08c`.

### A. Composition
1. **CONFIRMED.** The rest of the file (L:286–1165) is byte-identical to `HEAD:LOCK-m-F3.md`.
   - `cmp` finds no difference; 880 lines.
   - Its sha256 is `70da4a70…1d3f`, the same as the HEAD blob, the `f674583` blob and the working tree.
2. **CONFIRMED.** The form (L:29–32, L:282–286; E:26–27) is as described: v0.2, then the `---` rule, the one sentence, then the re-issue verbatim. The lock's history is `f674583` then `1e79955`, and v0.1's heading is at lock:194.
3. **CONFIRMED.** The parsers (also E:29–31) return the same values on both files.
   - I imported the driver with the five model modules blocked, using the venv's `python -B`.
   - On the draft and on HEAD's file, `lock_m_modules` gives the same 11 files with no problems.
   - `lock_weights` gives the same pair, `c000ac2c…` / `03922eed…`.

### B. v0.2 §0
4. **CONFIRMED.** L:1 and L:3: m:296 sits in §3.2 (heading at m:288). The quote matches m:296, with its bold dropped.
5. **CONFIRMED.** L:7's date, 2026-11-11, is the PI's word on the relay of 2026-11-11 (RESULTS.md@eb3e08c:157–158).
6. **IMPRECISE (low).** L:7 has "with D2 (2026-12-22) (m:298)", but m:298 gives no date.
   - D2's date is at m:16; A-m2:86 and ans:36 also give it.
   - Fix: "(m:298; D2's date, m:16)".
7. **CONFIRMED.** L:8–13 check out.
   - The relay and `a6c6297` match: name-status shows RESULTS.md modified and the answers file added; that commit added all nine "> n." lines.
   - Items 3 and 5 match ans:65 and ans:67 exactly.
8. **CONFIRMED.** The rulings table (L:17–23): all five sha256 match the working tree and the HEAD blobs. The adding commits are `a6c6297`, `54b1e51`, `daca8b0`, `7589c1d` and `fc43249`.
9. **CONFIRMED.** The `gt:`§5 quote (L:25–28) matches gt:31 word for word. The source's bold on "v0.1 is re-issued first" is dropped.
10. **CONFIRMED.** L:34–43 check out:
    - the list of record line is R0's (lock:13–15);
    - `lock_file` and `lock_sha256` follow lock:253–254;
    - G-F3 at 120 carrying `locked_path` follows `stages.py:605–607` and `:624`;
    - G-F3's prior and the artifact at cap 120, any verdict, follow A-m2:75 and `stages.py:417–420`, `:517–522`;
    - the runs' locks are in the LICENCE lines: the first run's raw:9 has `377c5d60…`, the same as the `1e79955` blob; r2 raw:9 and gid raw:10 have `70da4a70…`;
    - the full `lock_sha256` in the r2 report and the artifact (`.identity.lock_sha256`) is the re-issue's;
    - `prior_gate` compares only the proposal (`stages.py:477–479`, `:447`).
11. **IMPRECISE.** L:44–45, L:54 and E:28–29 put "v0.2's base" and "Code anchors" at HEAD `a6c6297`.
    - HEAD was `eb3e08c` and is now `15d2f70`. Both commits touch RESULTS.md only, so every hashed or quoted file and every code anchor is identical.
    - But v0.2's commit base will not be `a6c6297`.
    - Fix: name `a6c6297` as the HEAD the tool ran at, and state the commit's own base, which differs from it in RESULTS.md only. Or re-run the generator at that base.
12. **NOT CHECKABLE.** L:44–48 and E:28–29 say the tables and PIN texts were generated by `v02_gen.py`. That is Code's process, and the script is outside the brief's sources; I did not open it.
13. **CONFIRMED.** L:49–50: every file was committed before `a6c6297`, and `git status` shows no tracked modification. The tables show only sha256 for the checkpoints. L:55's [E] figures check: my recomputation matches (item 25).

### C. v0.2 §1
14. **CONFIRMED.** The identity table (13 rows):
    - every file's sha256 matches `shasum`;
    - m's package `7756dcf4…` and mf3's `098455d9…` (15 files) match a recomputation by the lock's rule;
    - mf3's value also matches the artifact's `.identity.package_sha256`;
    - the two closures equal R1's (lock:30–31). Nothing under `valence_core/` or the analyzer has changed since `f674583`; I did not recompute them, because that would import the analyzer.
    - The "since the re-issue" column is right: since `f674583` only the driver (`fb82daa`) and the new artifact (`efb7bef`) changed.
15. **CONFIRMED.** L:75–76 restates R1 (lock:38–42).
16. **CONFIRMED.** The records table (7 rows): all sha256 and adding commits match. "-diff" is right (`git check-attr`: diff unset). `Q-F3_time.json` was touched only by `acc3b52`.

### D. v0.2 §2
17. **CONFIRMED.** L:91–95: the A-m2 v0.5 §4.1 quote matches A-m2:71 (bold dropped), and the r2:§1.4 quote matches r2:21 exactly.
18. **CONFIRMED.** L:96–98: both CAP TRIGGER lines are byte-identical to r2 raw:20 (added at `93ecaf9`) and to the first run's raw:19 (added at `acc3b52`). The first run was at 60.
19. **CONFIRMED.** L:99–105:
    - the seat's stop is at gt:11;
    - G-ID-F3's cap is 120 (artifact `.identity.reasoning_cap`);
    - the binding sites are R3's F19 PIN (lock:123) and R1 (lock:48–51).

### E. v0.2 §3
20. **CONFIRMED.** L:109–112: the §1.3 quotes match ans:20, m:295 matches, bar 6 matches lock:599, and routing item 1 matches ans:63.
21. **CONFIRMED.** L:113–116:
    - the artifact has `.verdict` FAIL, `.n_pairs` 1, `.pairs_identical` [false], and the F-7 `.criterion`;
    - the report has `.bars[0]` k 1, n 1, fired;
    - "stops at the first divergence…" is lock:599;
    - the gid raw shows two `id A2s` lines only.
22. **CONFIRMED.** L:117–122:
    - in the reads the halves share a 658-character prefix, and the first difference falls in the first free `reasoning_text` piece in both;
    - all six token counts differ between the halves;
    - `picked_role` agrees through the fifth free choice and differs at the sixth (round 10);
    - the seconds match `.timing`, and the §1.3 quote matches ans:20.
23. **CONFIRMED.** L:123–130:
    - `_extra` requires `locked_path` except at id (`stages.py:605–607`, `:658–661`);
    - `_locked` is at `stages.py:688–697`; `_gid_pass` is at `guard.py:85–102` with its condition at `:97–102`, called from `:117`;
    - per-arm counts and the hour cap: m:298's "as §3.1" points to m:286.

### F. v0.2 §4
24. **CONFIRMED.** The basis table and totals (L:136–143):
    - r2 reads: each sham session's `.seconds` rounds to 1,175.9, 1,041.4 and 1,118.3, and its `.reasoning_lines[].n_tok` sums to 160, 226 and 240. The report's `.timing.sham_seconds` rounds to 3,335.6.
    - id reads, uncached half: `.seconds` 1,942.675, and `.reasoning[].n_tok` sums to 375.
    - The total is 5,278.3. The mean is 1,319.57, which is 1,319.6 s or 22.0 min. The slowest is 1,942.7.
25. **CONFIRMED.** The hours (L:144–147):
    - campaign at the mean: 246.32 h (672) and 351.89 h (960);
    - campaign at the slowest: 362.63 h and 518.05 h;
    - G-F3: 14.66 h and 21.59 h;
    - 672 and 960 are the totals at m:234 and m:241, rows 40–35 and 25–24.
26. **CONFIRMED.** L:148–158:
    - m:230, m:234–241 and gt:35 match;
    - "the cached table not applicable" matches ans:7 and ans:20 (m:216, m:220–226);
    - the m:243 and m:324 quotes are exact;
    - the seat's default matches ans:36.

### G. v0.2 §5
27. **CONFIRMED.** The DRIVER value and the history (L:162–174):
    - the six commits come from `git log`, and each blob's sha256 matches;
    - the "edit" column matches the commit subjects, and RESULTS.md@eb3e08c:667 records the smoke form retired;
    - the last column matches the four DRIVER lines (first run's raw:5, smoke raw:5, r2 raw:5, gid raw:6, which comes before the post-load re-read at :8);
    - the `cd9756e` and `993eba1` blobs have no DRIVER print.
28. **CONFIRMED.** The PIN line numbers (L:176–177) are right at `acde2d8` (:72…:442) and at HEAD (:92…:577); the id sites are at :128, :273, :375 and :571. The driver is the only file with v0.2 PINs (13).
29. **CONFIRMED.** All 13 PIN texts (L:179–198) are verbatim. I rebuilt each from HEAD's blob with comment markers and indentation stripped and its lines joined; every one is identical. The `\|` in the :128 row is the Markdown table escape.
30. **IMPRECISE (anchor).** L:200–201: both texts are exact (drv:98–99; the `5d40d59` blob at :85; the `fb82daa` diff). But the sentence is at :98–99, not :92. Fix: "in the PIN that opens at :92 (its lines :98–99)".
31. **CONFIRMED.** L:202–206, first three sentences:
    - the PIN quote is drv:96–97;
    - the four conditions are listed at `results/raw/2026-11-07_mf3-time-wiring_design.md:57–62`;
    - the entry quote is exact at RESULTS.md@eb3e08c:3111;
    - "v0.2 reads the PIN as the plural" is Code's form at `results/raw/2026-11-07_mf3-code-to-design_G-TIME-F3.md:182`, confirmed at gt:31.
32. **IMPRECISE (commits Code beyond the routing).** L:206 ("The `qual` wiring's edit corrects the word, and its entry names it") and L:271 ("It corrects the plural").
    - Neither the seat's §5 nor its §9 asks for this. `gt:`§5 confirms only that v0.2 records the plural reading.
    - Fix: mark it as Code's proposal for the seat, or drop it.
33. **CONFIRMED.** L:207–213:
    - the pre-load refusal is drv:611–616, and SNAPSHOT MOVED is drv:632–634;
    - m's `REVISION_STAGES` is at `scripts/m_sessions.py:651`;
    - R3's :88 and :95 (lock:141, lock:173) are :88 and :95 in the `1b593ba0` blob and :102 and :109 at HEAD;
    - F-1 is stated at RESULTS.md@eb3e08c:210.

### H–I. v0.2 §6 and §7
34. **CONFIRMED.** §6, the counters and first-pick shares (L:217–229):
    - the r2 report has the bars 0/30 and 0/18, critical 5; `.reasoning_lines.counter_a` is 0 in each sham template; `.first_pick_P` is 1/1, 1/1, 0/1;
    - (b) = 3 of 42 matches r2:28;
    - the first run's figures match gt:7 and r2:7, and the counters' scope matches A-m2:50;
    - the G-ID report's `counter_a` is 0 and 2; ans:24–25 match; `first_free_pick_P` is true on both halves.
35. **CONFIRMED.** §7 (L:231–241): both PIN texts are verbatim (`lines.py:202–208`, `stages.py:493–498`); the r2:48 and r2:67 quotes are exact; the date 2026-11-10 is right.

### J. v0.2 §8
36. **IMPRECISE (low).** L:245–246: the Q3 quote is exact (r2:40, bold dropped). But the paraphrase leaves out "or subagent's". Fix: "at a compaction or at a session's or subagent's start".
37. **CONFIRMED.** L:247–249: "inert; no strike" and "by the same form" are exact, and so is the end-notice rule (r2:41).
38. **IMPRECISE.** L:250–251 and E:24 list `r2:`§3 among "the departures ruled".
    - r2:§3 is an Observations section (rule 11). Its finding is that the checklist held, and the probe change is the routing's item 7, [adopted] (r2:36, :68).
    - The seat's §5 asks for r2:§4 and §6 only. The substance is right: the G-ID raw's header shows the probe, and RESULTS.md@eb3e08c:74 records it.
    - Fix: relabel or move it, and E:24 with it.
39. **CONFIRMED.** L:252–258: the §6 rulings and the ledger match ans:44–45 and ans:49–52.
    - "inert in substance" is §6's "Inert in substance" with a lower-case first letter. The lower-case form appears verbatim at ans:7 and ans:68.
    - Note: `15d2f70` (committed during this check) puts §6's ruling on pod note 2 to the seat's next read. v0.2 may want a pointer to it.
40. **FAIL.** L:259–262 says the `fb82daa` values-check raw "disclosed two slips. Neither touched the list of record". The raw discloses three things:
    - the checker's two departures from its brief: (1) a partial execution of HEAD's driver source, and (2) `git show --name-only 93ecaf9`, which printed three names under ckpt and reports. Of these two, the raw says "Neither touches the list of record v2's items" (raw:67–76);
    - separately, Code's own heredoc slip, which the shell refused, so nothing ran (raw:77–79).
    - RESULTS.md@eb3e08c:262 calls the checker's two "Its two disclosures".
    - Fix: name all three, and attach "neither touches" to the checker's two as the raw does. This section is also outside the seat's §5.

### K. v0.2 §9 and L:284
41. **CONFIRMED.** L:266–268: qual is refused (drv:100–101); ans:40 and ans:56 match; the by-path rule matches A-m2:75.
42. **IMPRECISE (commits Code beyond the routing).** L:269–270 says the `qual` wiring "requires this file's `path = uncached` and `reasoning_cap = 120` lines".
    - The m precedent is real for the path line (`scripts/m_sessions.py:588–595`). The cap line has no m counterpart, and no routing asks for either.
    - Fix: state it as Code's intent, declared in the `qual` wiring's entry, or drop it.
    - Note: L:269 itself contains both strings. A substring test like m's (`m_sessions.py:613–616`) would be satisfied by this sentence alone.
43. **CONFIRMED.** The m:297 quote (L:272–273) is verbatim, bold dropped.
44. **FAIL (coverage).** The seat's §5 lists G-F3's bars and the first-pick share (ans:40), and v0.2 does not carry them:
    - "`round_degeneracy` on ≤ 240 rounds p0 .05 critical 19";
    - "reasoning-line defects on ≤ 144 lines p0 .10 critical 22";
    - "first-pick share for sham templates".
    - Item 2 quotes m:297 only up to "(16 contrast)". The attractor tally appears only inside the seat's read (L:278).
    - So L:33's "Each is in a section below" is not yet true. Fix: add m:297's "Bars: …" sentence verbatim; it agrees with lock:600–601 (240/19, 144/22).
45. **CONFIRMED.** L:274–280 match ans:67, ans:56 and ans:58, r2:41, m:298 and m:16.
46. **IMPRECISE.** L:284 attributes the precedence sentence to "(m:296; the seat's G-ID-F3 answers, §5)". Neither source states such a rule.
    - It is Code's form sentence. The committed precedents are the re-issue's own line (lock:192) and `LOCK-p-OLMo-sft.md:94`.
    - Fix: cite those, or mark the sentence as Code's.

### L. The entry
47. **CONFIRMED.** The header text, E:1–3.
48. **NOT CHECKABLE.** E:2, `@@LOCKSHA@@` (placeholder).
49. **NOT CHECKABLE.** E:4, `@@STAMP@@` (placeholder).
50. **CONFIRMED.** E:5–8: item 3 is exact, and the close line at `a6c6297` quotes all nine items.
51. **CONFIRMED.** E:9–25: each pointer and figure matches the v0.2 sections, except E:24 (item 38).
52. **IMPRECISE (attribution).** E:32–33 puts the proposal's full sha256 under "(the licence's (f))".
    - (f) covers the analyzer's and mf3's sha256 and the m-file lines (`stages.py:299–301`). The proposal's full sha256 is required by `stage_identity_extra` (drv:280–281).
    - Fix: cite both.
53. **CONFIRMED.** E:34:
    - the v0.2 part's only `valence_core/m/` string is the package glob at L:65, which names none of the eleven files;
    - it has no WEIGHTS match;
    - it has no roster-word line (checked against both rosters' 12 words) and no clock time.
54. **NOT CHECKABLE.** E:35, `@@VC@@` (placeholder).
55. **NOT CHECKABLE.** E:36–37 describe a commit that has not happened yet.
56. **CONFIRMED.** E:38 matches ans:56 and ans:67.
57. **CONFIRMED.** Coverage: every other element of the seat's §5 is carried. From `gt:`§5, v0.2 also carries the nine `time` PINs, the history, the plural and the snapshot refusal.
    - Other content v0.2 adds beyond §5 is consistent with the code and the rulings: §0's citation form, §1's tables, §2's and §3's binding notes, and §5's F-1 bullet.
    - The additions that are not supported are items 32, 38, 40 and 42.

### Tally and everything not CONFIRMED
41 CONFIRMED, 9 IMPRECISE, 2 FAIL, 5 NOT CHECKABLE.
- **FAIL:** 40 (L:259–262), 44 (L:272–273, L:33).
- **IMPRECISE:** 6 (L:7), 11 (L:44–45, L:54, E:28–29), 30 (L:200), 32 (L:206, L:271), 36 (L:245), 38 (L:250–251, E:24), 42 (L:269–270), 46 (L:284), 52 (E:32–33).
- **NOT CHECKABLE:** 12, 48, 49, 54, 55.

### Disclosures
1. My first read of the G-ID artifact walked every field and printed `.provenance[0].stamp`, a start-side stamp. Reads of RESULTS.md, the raws and Code's blocks also showed write-time and launch stamps; one BUILD-entry line showed a battery run's time range. None is reproduced here, and I computed no duration.
2. The import the brief allows runs `valence_core.m.corr` at import time. Its module-level `olmo_roster()` (corr.py:133; the path is at :77) reads `data/olmo/a1_repair_roster.json`, which is not on the brief's list. This happened twice: once for the parser check, and once for the roster-word check, which printed only counts and line numbers.
3. List v2 item 1 forms, recorded here for completeness:
   - `git diff --name-status f674583 HEAD` printed names only, including the seven files under data/mf3/ckpt, reports and gates that the brief itself names;
   - `git check-attr diff` on the three checkpoint paths;
   - `git log --format=%h` and `--diff-filter=A` over the ckpt, reports and gates paths.
4. Some outputs showed config labels: Code's r2 block, a `git grep` that matched roster definitions, and a scan of module-level assignments. None is reproduced here.
5. My brief said no stage was running. `15d2f70` says G-F0m-OLMo (p) ×3 ran on the box at the time of its values-check. Nothing I ran touched the box.
   - At my start I ran a bare `git status --porcelain`: 31 untracked names, none under data/.
   - At my end I ran it piped to a filter and a line count: no tracked changes, 46 entries, no names printed.
   - Whether the 15 new entries are a running stage's outputs, I do not know.

Files: `<tmp>/v02/LOCK-m-F3.v02.md` and `<tmp>/v02/entry_v02.md`. I wrote nothing.
