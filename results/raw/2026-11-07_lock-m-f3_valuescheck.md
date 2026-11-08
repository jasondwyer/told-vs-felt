# LOCK-m-F3 v0.1 -- the blind values-check, three passes, with Code's dispositions (2026-11-07)

*Code's raw. Three blind passes over the lock draft and its entry (and, from pass 2, the checks raw), each by an agent given the drafts and the sources, not Code's conclusions. Between passes Code re-checked each item at source and applied, declared or disclosed it; the dispositions follow each pass. Totals: pass 1, 68 items (51 PASS, 14 IMPRECISE, 3 FAIL); pass 2, 42 items (35 PASS, 7 IMPRECISE, 0 FAIL); pass 3, 19 items (18 PASS, 1 IMPRECISE, 0 FAIL). Local roots are scrubbed; S in the reports is the session's scratch directory.*

---

# Pass 1

# Blind values-check: LOCK-m-F3.draft.md (lock) and entry_lock.md (entry)

Checked against the repository at HEAD 02dadb3 (tracked tree unmodified: `git status --porcelain --untracked-files=no` empty before and after) and the scratch worktree lock-wt (HEAD a28bef6 = 02dadb3 + LOCK-m-F3.md; `cmp` of its LOCK-m-F3.md with the draft: identical; its status clean before and after). Python: the jlens-qwen36 venv, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `HF_HUB_OFFLINE=1`. Nothing was written to either tree. Line numbers are the draft's (lock:N) and the entry's (entry:N). Placeholders were not counted.

Reproduction first: `lockgen.py` re-run at HEAD 02dadb3 writes output byte-identical to `generated.md`, and composing `lock_template.md` + `generated.md` + `fills_wrapped.json` (compose.py's logic, in memory) gives the draft byte for byte. All 18 generated sections are used.

## Hashes

1. **The binding table's file hashes** (lock:81-83, 88-90; ADDENDUM-m1 again at lock:131): proposal `42ab36ec…6c6b`, ADDENDUM-m1 `ea08322d…9001`, analyzer `d347ea0c…5e48`, G-SHAPE-F3.json `0c9de56e…1461`, G-ANL-F3.json `b91a8c67…936c`, the schedules manifest `c7b5df44…3314`. **PASS.** `shasum -a 256` of each file, and of `git cat-file blob HEAD:<path>`: all equal.
2. **m's package_sha256** `7756dcf4…49bb` (lock:84). **PASS.** I re-implemented the rule (sorted `{rel}\n{len}\n` + bytes over the 18 `valence_core/m/*.py` files): 7756dcf4…49bb. `resume.package_sha256_of` and `resume.package_sha256()` give the same.
3. **mf3's package_sha256** `f30ad505…6310`, 15 files (lock:87). **PASS.** The same re-implementation, `guard.package_sha256_of(guard.PACKAGE_DIR)`, and `mf3_sessions.py hashes` all give it.
4. **The Q-F3 closure** `d19f336d…f039`, 22 modules, and **the base closure** `a3bc7bb9…b22b`, 15 modules (lock:85-86). **PASS.** `ma.closure(lazies=LAZY_VERDICT_MODULES + LAZY_F3_MODULES)` gives 22 modules and 1 data file (`data/olmo/a1_repair_roster.json`). `ma.closure()` gives 15 modules and the same data file. `closure_sha256`, and an independent compact sort-keyed sha256, match both values.
5. **The eleven m files** (lock:97-107). **PASS.** sha256 of each `valence_core/m/{name}.py` over `guard.M_HASHED` (11 names): all 11 equal. They also equal the `M MODULE` lines of `mf3_sessions.py hashes`.
6. **WEIGHTS** `mlx-community/Qwen3.6-27B-4bit revision c000ac2c… sha256 03922eed…1e26` (lock:112). **PASS.** `mf3_sessions.py hashes` (offline) prints exactly this line. An independent recompute agrees: `refs/main` = c000ac2c2057…3282, and the sha256 of the compact sort-keyed JSON of the 6 files' blob names (3 WEIGHTS_FILES plus the index's weight files) is 03922eed…1e26.
7. **The generated values** (lock:117-119). **PASS.**
   - `renders_sha16 a04f67b0e5105a05`: `m_corr.renders_sha(scaffold.pool_and_renders()[1])`.
   - REASONING_CAPS = (60, 120); CAP_TRIGGER = 3; CAP_AFTER_TRIGGER = 120. This agrees with m:174: "≥ 3 … reach the cap without a newline → 120".
   - LICENCE_KEYS is exactly the listed eight.
8. **The rulings table** (lock:126-131). **PASS.** All six file sha256 match. `git log --diff-filter=A` gives dc1ffe1, 54bbfe5, 0f35954, 139635f, f105bdd and f26bc59, each the only commit that touches its file.
9. **The lexicons and their hash** (lock:164-168; entry:4 `1b7d5a01…8028`). **PASS.**
   - 19 stage-1 terms, 8 negative, 6 positive, ±6: equal to `STAGE1_TERMS`, `POLARITY_NEG`, `POLARITY_POS` and `POLARITY_WINDOW` (m_analyze.py:3441-3446), and to m:312 (c)'s lists.
   - The artifact's `g_anl_f3.counter_c` block equals those constants. Its compact sort-keyed sha256 is 1b7d5a01af96…d088028.
10. **The schedule files** (lock:189-212). **PASS.**
    - All 20 rows equal the files' sha256 and the manifest's entries.
    - The manifest's schema `m-schedules-manifest-v1`, its construction "PROPOSAL-m v1.11 m:159-172 (Q-F3)" and its 20 files are as stated.
    - The directory holds only those 20 files and the manifest.
11. **The banner and reasoning-block table** (lock:272-286). **IMPRECISE.**
    - All 13 byte counts and sha256 reproduce under the generator's own convention.
    - `TOLD_MAP` and `TOLD_MAP_SHAM` are 2-tuples (clause 0 and clause 1), m's objects by identity (`fb.TOLD_MAP is mb.TOLD_MAP`). For non-strings, lockgen.py hashes `json.dumps(v)`: a JSON array, default separators, ASCII-escaped. So "276" and "222" are the lengths of a JSON text, not bytes any harness writes. The clauses' own UTF-8 bytes are 134 + 134 and 107 + 107, with sha256 6bfc495b…89ba and a6fe3b79…fae4 (TOLD_MAP), and 5bdf9905…e3d3 and a8b3befd…8b25 (TOLD_MAP_SHAM).
    - Those per-clause sha256 are the values LOCK-m-F0.md:1969-1972 names for the same constants.
    - The lock does not say a JSON form was hashed, so a reader who hashes "the bytes" cannot reproduce 2a85bd65… or 2e5cc294…, and cannot reconcile them with LOCK-m-F0 §7.
    - The five string constants and the six `reasoning_block(n)` rows are plain UTF-8 bytes and are correct (for example `reasoning_block(10)` = "[round 10 | reasoning]\nReasoning (one line):\n", 45 bytes).
    - Fix: list each clause's bytes and sha256, or state the `json.dumps` convention in the table heading.
12. **The abbreviated hashes in the lock's prose** (lock:145 `0f9b7bb9…6e9c`, lock:153 `6ec3222b…93d9`, lock:154 `6ec3222b…`, lock:583 `45b67246…7a41`, lock:588 `60199b36…feec`). **PASS.**
    - The superseded G-SHAPE-F3 artifact's sha256 is 0f9b7bb9…36e9c; it equals G-SHAPE-F3.json at 1bf94a6.
    - The analyzer at e0b4f2c, and at 10a2bbb^, is 6ec3222b…c82b93d9.
    - PREPRINT-v1_0-draft.md at HEAD is 45b67246…be7a41.
    - m's package from git blobs at 993eba1^ is 60199b36…e7feec, and at 993eba1 it is 7756dcf4….
13. **The abbreviated hashes in the entry** (entry:2-4): d347ea0c…5e48, f30ad505…6310, 0c9de56e…1461, b91a8c67…936c, 1b7d5a01…8028. **PASS.** Each one's first 8 and last 4 characters match the full value.
14. **The short commit ids** (lock:126-131, 134, 151-155, 582, 586-587; entry:12-13, 43). **PASS.** Each resolves to the commit described:
    - 02dadb3 = the canonical ganl;
    - 10a2bbb = the check fix;
    - 9480f9b = N1;
    - 993eba1 = the hygiene commit;
    - f9700ba = the G-SHAPE-F3 re-run;
    - e0b4f2c = G-ANL-F3, BUILD;
    - 0f35954 = the OLMo NOT-RUN, which adds the gcal-olmo answers;
    - the remaining ids are as in item 8.

## Quotations

15. **The PI's routing, item 1** (lock:7-10; entry:7-9). **PASS.**
    - `git show 139635f:RESULTS.md` line 81 is, verbatim: "1. G-ANL-F3: hygiene commit (N9, N12) → G-SHAPE-F0/F3 re-runs → canonical `ganl` → LOCK-m-F3 v0.1 → G-TIME-F3 [go]; N10 m:312 stands [confirmed]; N13 no change [confirmed]."
    - The lock's ":79–81" spans the intro line ("The PI's routing, in chat, verbatim:") and the quote.
    - Not checkable against the record: "as the coordinating session relayed it". The record says "in chat".
16. **The seat's answers, §9 item 1**: "LOCK-m-F3 v0.1 (naming the analyzer, the lexicons, the re-run G-SHAPE-F3)" (lock:10-11; entry:10-11). **PASS.** Verbatim substring of p-preread answers line 64.
17. **N10's ruling**: "m:312 stands as pinned; no revision before the lexicons freeze at LOCK-m-F3 v0.1" (lock:171-172). **PASS.** Verbatim (answers line 52).
18. **N10's first reporting term** (lock:177-178). **IMPRECISE.** The source (answers line 52) reads `the "same polarity, shared nearest term" subclass`. The lock changed the inner double quotes to single quotes. That is a common nesting convention, but the passage is presented as verbatim. Keep the source's marks.
19. **N10's second reporting term**: "the seat's blind read scores such lines by (label, polarity) as m:312 has it." (lock:183). **PASS.** Verbatim.
20. **F-6**: (G-TIME-F3's contrast sessions report no per-line list; "k of ≤ 36") (lock:378). **IMPRECISE.**
    - The quoted "k of ≤ 36" is verbatim (ganl-f3 answers line 29).
    - The paraphrase drops the ruling's limit: "no per-line list is printed or reported **before VERDICTS**". The per-line booleans go to the checkpoint under m:271, and m:293 reports contrast sessions at Q-F3's VERDICTS. Unqualified, "report no per-line list" reads as "never".
21. **F-7** (lock:379-380). **PASS.**
    - The criterion paraphrase matches answers line 30 ("m:281's byte-identical transcript pair **and**, per reasoning line, an identical (n_tok, cap_hit, stop_reason) triple").
    - "A seat PIN at LOCK-m-F3 v0.1; set before G-ID-F3 has run." is verbatim.
22. **"PIN-29's exception by blob (A1)"** (lock:381). **PASS.** ganl-f3 answers A1: "The PIN-29 exception is by blob, not by path". Sites: m_analyze.py:112 and :5076.
23. **"at the cost Code states" (the F3 prebuild answers, line 50)** (lock:30-31). **PASS.** Verbatim at line 50.
24. **The N1 answer**: "the canonical `ganl` on that HEAD → LOCK-m-F3 v0.1 → G-TIME-F3" (`f105bdd`, §1) (entry:12-13). **PASS.**
    - Verbatim substring of n1-battery answers line 11 (§1 "The order: (b)").
    - The lock's §1 attributions at lock:152 and lock:586 are right: the order, the check's form and "whatever the tree holds" are all in §1.
25. **m:292's own words** (lock:14-24; lock:158 "G-ANL-F3's … lexicon hashes"). **PASS.** The §0 table's nine rows are m:292's nine items in order. The ellipsis stands for "analyzer and".
26. **N13's entry term** (lock:580-581). **PASS.**
    - It is a paraphrase, not a quotation: it substitutes `--campaign none` for the answers' `none`.
    - Its content matches answers line 54.
27. **F-1's clearance** (lock:594, entry:46). **PASS** on F-1's text: "an edit that wires a subcommand at its step, touching no scoring-stack function, does not re-run G-SHAPE-F3". How it is applied is item 63.

## Anchors

28. **stages.py anchors** (lock:50, 64, 66, 68, 71, 73). **PASS.**
    - :556 is `def _extra`, with its PIN in the docstring at :559;
    - :280 is `def licence_problems`;
    - :619 is `def _renders_of_record`;
    - :642 is `def _locked`;
    - :397 is `PRIOR_STAGE = {...}`;
    - :491 is `def _record_licence`.
29. **m_analyze.py anchors** (lock:175, 179). **PASS.**
    - :3472 is `def score_line_c`.
    - :10513 is the battery case `("prism is clean, slate is corrupted", "ambiguous", {"prism": "positive", "slate": "positive"})`.
30. **m:N anchors in the prose, and their claims.** **PASS.**
    - Title: m:292, and m:361 = §8 (m:351) step 19.
    - m:293–296: G-TIME-F3, the cap fixed, G-ID-F3, LOCK v0.2.
    - m:296: "Cap; path; projections."
    - m:297–298: G-F3; G-VER, G-PWR and LOCK v1.0 with D2.
    - m:293: "(Qwen, uncached)".
    - m:295: "a divergence sends Q-F3 uncached".
    - m:290: G-SHAPE-F3. m:291: G-ANL-F3.
    - m:312 (c): the lexicons and the nearest-term rule.
    - m:294: "Cap fixed".
    - m:263: printed exclusion reasons.
    - m:267: the laptop checklist.
    - ADDENDUM-m1 §2.3: D2 and LOCK-m-F3 v1.0 (A-m1:18, :40).

## "How a stage cites this file" (item 4 of the brief)

31. **The keys carried, and `_extra`'s requirements and refusals** (lock:52-63; entry:14-19). **PASS.**
    - `_extra` requires (lock_sha256, proposal_sha256, renders_sha16, reasoning_cap, weights_revision, weights_sha256), plus locked_path except at "id" (stages.py:564-566).
    - Every key must lie in that set or in `_OPTIONAL_EXTRA` (lock_file, proposal_file, prior_proposal_sha256s, analyzer_sha256, package_sha256, m_module_sha256) (:546, :566-568). On a non-stub run, lock_file, proposal_file, analyzer_sha256, package_sha256 and m_module_sha256 are required.
    - At "time": the cap must be 60 (:580) and locked_path "uncached" (:614).
    - At "id": locked_path is in neither set, so carrying it is refused (:568).
32. **"the licence by file … checks every key above except renders_sha16, reasoning_cap and locked_path"; "None of these three is compared with this file's text"** (lock:64-69). **PASS.**
    - `licence_problems` (stages.py:280-376) reads proposal_file and proposal_sha256, lock_file and lock_sha256 (committed, working tree identical, sha256 equal), analyzer_sha256, package_sha256, m_module_sha256, weights_revision and weights_sha256. It never reads renders_sha16, reasoning_cap or locked_path.
    - The lock-text comparison (:365-375) covers only the analyzer, mf3's package, weights_sha256, weights_revision and the m-file lines.
    - `_renders_of_record` (:619-624) compares renders_sha16 with the renders built at stage start. `_locked` (:642-652) compares the path with the backend's G-ID licence, and is called at G-TIME-F3 (:947).
33. **"reasoning_cap and locked_path are checked by `_extra`"** (lock:67). **IMPRECISE.**
    - True, but incomplete for a stage this lock binds. At G-ID-F3, `_extra` checks only that the cap is one of (60, 120). The decisive check, equality with the cap G-TIME-F3's trigger fixes, re-computed from its checkpoint, is `prior_gate`'s (stages.py:466-473, "NOT THE FIXED CAP"; F6 in §9).
    - The lock names the second check for the path (`_locked`) but not for the cap.
    - Rendering nit: the sentence "The hashes and the weights are this section's tables…" (lock:60-61) renders inside the last sub-bullet (`renders_sha16` and `reasoning_cap`), not at the parent level (markdown-it, commonmark + table).
34. **prior_proposal_sha256s, PRIOR_STAGE and `_record_licence`** (lock:70-73). **PASS.**
    - `_extra`: `pp = identity_extra.get(...) or []`, then `out[...] = sorted(pp)` (:591-595), so omitting the key and passing [] both give [].
    - `_record_licence` receives the validated `extra` (run_gate_stage :931/:955, run_gid_pair_f3 :1182/:1200) and refuses on mismatch ("CHECKPOINT MISMATCH").
    - PRIOR_STAGE = {"id": "time", "qual": "time", "campaign": "qual"}. "time" has no prior; passing one raises ValueError (:441-443).
35. **The licence list** (lock:39-47). **IMPRECISE.**
    - (a) to (g) are described correctly, except that (g) also requires the lock's text to name weights_revision and weights_sha256. See stages.py:290 ("and the lock names both"), the `named` dict (:316-325) and the loop at :367-369. The mutation run prints "its committed text does not name weights_revision 2222…".
    - The bullet "this lock's committed text naming the analyzer's sha256 and mf3's …" omits the weights.
36. **The Q-F3 VERDICTS reader refuses unless the lock names the analyzer's sha256, m's package_sha256 and the Q-F3 closure's sha256** (lock:48-49). **PASS.**
    - m_analyze.py:4131-4134 loops over ("analyzer sha256", a_sha), ("package_sha256", env.package_sha256), ("Q-F3 closure sha256", env.closure_sha256).
    - `production_env("Q-F3")` (:1904-1911) sets package_sha256 = `resume.package_sha256()` (m's) and the closure with LAZY_F3_MODULES.

## N10's dated note (item 5 of the brief)

37. **The scorer facts** (lock:172-176). **PASS.**
    - `_f3_tokens("prism is clean, slate is corrupted")` gives ['prism','is','clean','slate','is','corrupted'].
    - slate (index 3) is nearest to "clean" (index 2, distance 1); prism (index 0) is nearest to "clean" (distance 2).
    - `score_line_c` returns {'scored': True, 'class': 'ambiguous', 'labels': {'prism': 'positive', 'slate': 'positive'}}.
    - m:312 (c): "two labels with the same polarity, a shared nearest term included" → ambiguous.
38. **"records the line's class and each label's polarity, not which term was nearest … So it records the shared polarity but not the shared term, and no such count is built"** (lock:179-182; entry:41-42). **PASS.**
    - `score_line_c` (:3472-3510) outputs {scored, class, labels: {label: polarity | None | 'tie'}}. The nearest term's position (`nearest[lab][1]`) is not output.
    - Counter (c)'s key items (:3972) keep scored, class, labels, correct and follows.
    - A line with the same polarity from distinct terms ("prism text is clean and slate text is fine") gives byte-identical output, so the subclass cannot be told apart from the output. `klass` (:3961) has no subclass count.
    - Note: per-line key items are written out only for the 48 drawn lines (`blind_read_key[...]["rule"]`, :3987-3989). For other lines only the class counts persist. The conclusion is unaffected.

## Totality claims (item 6 of the brief)

39. **The 90 PIN sites and their definition** (lock:482-575; entry:26-28). **PASS.**
    - My own inventory over `valence_core/mf3/*.py`, `scripts/mf3_sessions.py` and `scripts/m_analyze.py` finds 90 lines:
      - 57 `PIN (Code, declared at LOCK-m-F3 v0.1;` and 27 `PIN (Code, declared at LOCK-m-F3 v0.1)`;
      - 6 `PIN (the seat's …` (A1 ×2, F-6 ×2, F-7 ×2);
      - 88 comments and 2 docstrings (stages.py:99, :559).
    - Every table row matches its file:line, its kind and its opening text exactly. No opening exceeds 150 characters or contains "|".
    - None is missed:
      - No line in scope carries a wrapped opening or a variant form. The only other "declared at LOCK-m-F3" lines (m_analyze.py:4441, :10088, :10090, :10092, :10093) are a header, a comment and battery strings.
      - Repo-wide, `git grep "declared at LOCK-m-F3"` finds code only in these files.
      - Repo-wide, the six "PIN (the seat" lines in *.py are exactly these six.
      - mf3_sessions.py has no PIN line.
40. **"A first draft's pattern found 79. It missed nine comments whose opening parenthesis wraps … and two docstring PINs"** (entry:29-30). **PASS.**
    - Consistent: a comment pattern requiring a ")" on the same line finds exactly 79, and 79 + 9 + 2 = 90.
    - Note: 10 comment PINs have a parenthetical that wraps to the next line. The tenth, stages.py:291, was caught by the inner ")" of "(C2)".
41. **"Every bar of Q-F3's later stages", 13 bars generated from QF3_BARS** (lock:350-369; entry:22). **PASS.**
    - `len(bars.QF3_BARS)` = 13. Every cell equals the field (name, stage, kind, unit, numerator, p0, alpha, domain, cadence, planned_n/planned_crit, on_fire); 0 mismatches.
    - Coverage against m:271, m:293, m:295, m:297, m:316 and m:330 is complete: hair triggers; time, qual and campaign round_degeneracy and reasoning_line_defect; gid_divergence; own_pair_lexical; both exclusion guards. All are `binding=True`.
    - Critical counts re-computed independently by exact binomial: 30/.05 → 5, 18/.10 → 5, 240/.05 → 19, 144/.10 → 22.
    - Note: for hair triggers the α column shows "— (k ≥ 1)" while the field holds Bar's default "0.05". This is a rendering rule in lockgen.py, faithful to m:271, but undisclosed.
42. **Bar row 6, `gid_divergence@G-ID-F3`: numerator "complete pairs whose transcripts differ in any byte"** (lock:362). **FAIL.**
    - The row is generated faithfully from bars.py:197-202, but that text predates the seat's F-7. bars.py was last edited at cd9756e; F-7 was applied at e0b4f2c in stages.py and guard.py only.
    - The stage decides by `_gid_pair` (stages.py:1139-1148, the seat's F-7 PIN): identical iff the transcripts are equal **and** each line's (n_tok, cap_hit, stop_reason) triple is equal.
    - The bar fires on `status == "FAIL"` from `gid_decide` over that field (:1252, :1120-1122).
    - `guard.GID_CRITERION` (guard.py:46-49) carries the triple.
    - So a transcript-identical pair with a differing triple fires this bar, contrary to the row's numerator and consistent with lock §9's own F-7 statement (lock:379-380). The lock thus binds two different G-ID-F3 criteria.
    - Secondary: `gid_decide` also fails on a divergent *incomplete* pair ("a divergence -- complete or not -- fails G-ID-F3", :1113-1114). "complete pairs" is m's carried wording (m/bars.py:583).
    - Fix: a dated note under §8 reading row 6 with F-7, or the text corrected in bars.py before the lock names mf3's package.
43. **"Every listed file is committed at HEAD with identical working-tree bytes"** (lock:36). **PASS.** 78 files: blob sha256 equal to working-tree sha256 for every one, none untracked. They are:
    - m's 18 and mf3's 15 package files;
    - the closures' 22 module files and the data file;
    - the 20 schedule files and the manifest;
    - the proposal, the ADDENDUM, the analyzer, both gate artifacts, the superseded artifact, the 6 ruling raws and both register raws.
44. **"Nothing in them is transcribed by hand"**, for §1-§9's tables and verbatim blocks (entry:24-25). **PASS.**
    - Every table and verbatim block in §1-§9 is an `@@GEN:…@@` section of the template.
    - Regenerated byte-identically at HEAD 02dadb3, and recomposed byte-identically.
    - Hand-typed in lockgen.py are labels only (ruling names, the example key arguments), plus the two rendering rules noted in items 11 and 41.
45. **"The proposal's sha256 and every hash this lock names are in §1"** (lock:6). **IMPRECISE.** Hashes outside §1:
    - the lexicons' sha256 (lock:168, §3);
    - the 20 schedule-file sha256 (§4);
    - the 13 banner and reasoning-block sha256 (§6);
    - the prose hashes 0f9b7bb9…6e9c (§2), 6ec3222b…93d9 (§3), and 45b67246…7a41 and 60199b36…feec (§10).
46. **"Code computed every value below with a tool at the lock's HEAD (`lockgen.py` …)"** (lock:35). **IMPRECISE.**
    - lockgen.py produces only the generated sections. The following are template or fill text (lock_template.md:92-100, fills_wrapped.json), not tool output:
      - §2's 2,816 / 1,408 / 8,448 / 640;
      - §3's 525/525, 538, 2,160 and 519,480;
      - the abbreviations in §2, §3 and §10.
    - All these values are correct (items 12, 65, 66).
    - Scope the sentence to "every value in the tables of §1-§9" or similar.
47. **"Each site is listed after them"** (lock:375), and lock:31: "Striking one moves the hash its site's file carries, and so a hash this lock names". **IMPRECISE.**
    - F57's site is `scripts/mf3_sessions.py` (lock:444). That file has no PIN line, so the sites table has no row for it.
    - This lock names no hash of mf3_sessions.py. Striking F57 moves only the driver's blob, and moves the G-SHAPE-F3 artifact only through F-1's re-run.
    - The other 59 F-entries each have a PIN line at or just above their site. I checked them by AST span; F43 and F58, whose comment blocks start more than 6 lines above the symbol, I checked by hand. The 24 V2 ids have 25 sites. For F32, F36 and F59 the PIN line is now the seat's or carries the seat's ruling (item 49).

## Verbatim blocks (item 7 of the brief)

48. **The F3 build's PIN register, "verbatim" (`…mf3-build_design.md` §4)** (lock:384-447). **PASS.** The 62 lines are byte-identical to source lines 56-117. The section has no internal blank lines.
49. **The register declared as "Code's readings, declared at this lock … Each reading is strikable"**, as it covers F32 (lock:419), F36 (lock:423) and F59 (lock:446). **FAIL.**
    - The F3 build design's own flags say F-6 concerns "Q5, F32, F36" and F-7 concerns "`meta_identical` (F59)" (mf3-build_design.md:160-161).
    - The seat ruled both (ganl-f3 answers:29-30), and e0b4f2c applied them:
      - `meta_identical` was removed. `git show e0b4f2c -- valence_core/mf3/stages.py` shows `-"meta_identical"` and `+line_triples_identical`, under the seat's F-7 PIN at stages.py:1140.
      - G-TIME-F3's contrast block is now {s, forced_rounds_generated, excluded_at_forced}, "no per-line list" (readrule.py:194, the seat's F-6 PIN; readrule.py:471-486).
    - The register, verbatim from the pre-ruling raw, still declares:
      - F32 "plus the per-line cap booleans (Q5)";
      - F36 "… the per-line cap booleans";
      - F59 "descriptive only".
    - These are three readings the code no longer implements and the seat has already replaced. Meanwhile §9 lists F-6 and F-7 among "the seat's rulings set here". Nothing marks them superseded.
    - Fix: a dated note under the register saying that F32 and F36 (the per-line part) and F59 are superseded by F-6 and F-7 at e0b4f2c. Their sites now carry:
      - the seat's F-6 PIN (readrule.py:194, F32's `strip_contrast`);
      - a Code PIN citing F-6 (readrule.py:472, F36's `_contrast_block_time`);
      - the seat's F-7 PIN (stages.py:1140, F59's `_gid_pair`).
      The seat's other two F-6 and F-7 PINs are at stages.py:991 and guard.py:46.
50. **G-ANL-F3's PIN register, "verbatim" (`…ganl-f3_build_design.md` §2)** (lock:450-479; entry:40 "the two PIN registers, verbatim"). **FAIL.**
    - Not byte-verbatim. The source has blank lines at 67 (after the intro paragraph) and 94 (before "The seat's rulings are recorded beside…"). lockgen.py drops every blank line (`if l.strip()`), giving 28 lines against the source's 30.
    - Effect: the closing sentence directly follows the table and renders as a one-cell table row. markdown-it (commonmark + table) gives the lock:453 table 26 rows: header, 24, and that sentence in a `<td>`. In the source it is its own paragraph.
    - Fix: keep internal blank lines (strip only leading and trailing ones).
51. **Module homes, "verbatim" (§3)** (lock:248-265). **PASS.** The 16 lines are byte-identical to source lines 37-52. The 15 module names match the 15 tracked `valence_core/mf3/*.py` files.
52. **The three docstrings, "verbatim"** (verify lock:291-314, schedule lock:217-232, lines lock:326-345). **PASS.**
    - Each equals `module.__doc__.strip()` exactly.
    - Note: verify.py's source text writes `"\\n"` four times; the docstring value, which is the stated source, has `"\n"`.

## m:292's list (item 8 of the brief)

53. **Placement of m:292's nine items** (lock:14-24; entry:20-22). **PASS**, with items 11 and 54 as qualifications. The sections are as stated:
    - schedules: §4;
    - keys and module homes: §5;
    - the verifier and the bytes: §6;
    - the classes: §7;
    - the G-SHAPE-F3 result: §2;
    - the analyzer hash in §1 and the lexicon hash in §3;
    - the bars: §8.
54. **"Q-F3's schedules and interleave rule" → §4** (lock:16, lock:215-232). **IMPRECISE.**
    - §4's block is schedule.py's module docstring. It names "the six-arm interleave" but never states the rule.
    - The rule is in `schedule.interleave`'s docstring and PIN (schedule.py:205-213): strict rotation by launch index in §2.4's order; next = the live arm with the fewest launches, ties to table order; an arm at its floor leaves for good; resume counts validated pairwise.
    - That text appears in the lock only as F47's "m's rotation over six arms" and as the PIN-sites row for schedule.py:210, cut at "next = the".
    - LOCK-m-F0 §6 states its interleave rule.

## The entry against the lock (item 9 of the brief)

55. **The headline names and "It carries N10's and N13's dated notes"** (entry:1-4). **PASS.** Every hash named is in the lock (items 1-3, 9, 13). N10's note is in lock §3 and N13's in lock §10.
56. **"What a stage cites", m:292 by section, Code's readings, dated notes** (entry:14-22, 39-43). **PASS.**
    - These match lock §1, §0, §9 and §3, and §10 (three notes).
    - The register-verbatim claim at entry:40 inherits item 50.

## Scratch-worktree claims (item 10 of the brief)

57. **"mf3's licence … : no problem"** (entry:33-34). **PASS.** Re-ran licence_test.py from lock-wt: `licence_problems on the committed lock: []`, and `LICENCE TEST PASS`, exit 0.
58. **"with `identity_extra` built from the lock's committed text"** (entry:33). **IMPRECISE.**
    - Only m_module_sha256 and the weights revision and sha256 are read from the lock's text.
    - proposal_sha256, lock_sha256, analyzer_sha256 and package_sha256 are hashed from the files and the blob (licence_test.py:44-48). The licence then checks that the lock text names the analyzer's and mf3's.
    - Say "built from the committed files and the lock's text".
59. **"Three mutations are each refused"** (entry:35-36). **PASS.** The re-run refuses all three:
    - the analyzer one, with "its sha256 is not identity_extra's" and "lock … does not name";
    - the m-file one, on corr.py, by (e′) and (f);
    - the weights-revision one, by refs/main, the snapshot and the lock text.
60. **"The Q-F3 VERDICTS reader's three names … (`production_env("Q-F3")`) each appear in the committed text"** (entry:37-38). **IMPRECISE.**
    - The substance holds. I ran `production_env("Q-F3")` from lock-wt's analyzer: d347ea0c…, 7756dcf4… and d19f336d… are each in `git cat-file blob HEAD:LOCK-m-F3.md`.
    - But licence_test.py, the script the entry's "These ran" points to, does not perform this check. It prints analyzer_sha256, mf3's package_sha256 and proposal_sha256 instead. No scratch file records this run.
    - Keep its command and output beside the other checks, or say it ran separately.
61. **"a scratch worktree at `02dadb3` with this file committed there (a detached commit, not for history)"** (entry:31-32). **PASS.** lock-wt is at a28bef6, whose parent is 02dadb3. Its LOCK-m-F3.md is byte-identical to the draft, and its tree is clean.

## Overstated or unclear (item 11 of the brief)

62. **"That moved its sha256 from the BUILD's `6ec3222b…93d9` to the value in §1 before any lock or artifact named it."** (lock:153-154). **IMPRECISE.**
    - Artifacts did name 6ec3222b before 10a2bbb: data/m/verdicts/OLMo-{sft,dpo,instruct}_NOT-RUN.json (0f35954) each record 6ec3222b54c7…b93d9, as the lock's very next sentence says.
    - 10a2bbb's own wording is "before any lock or G-ANL-F3.json names it". Use that.
63. **G-TIME-F3's wiring: "As routed on 2026-11-07, it also carries the rest of m's pre-load check … and a DRIVER line"; "It is a subcommand-wiring edit … so under F-1's clearance it does not re-run G-SHAPE-F3"** (lock:593-598; entry:46-47). **IMPRECISE.**
    - I found no committed record of this routing. I searched RESULTS.md (no such routing; the newest entries say only "the `time` wiring at its step") and every results/raw/2026-11-07_* file.
    - Code's F-2 ("so does the rest of m's pre-load check", mf3-build_design.md:156), accepted by the seat (ganl-f3 answers:25), places the rest of m's pre-load check with the *campaign* subcommand's wiring.
    - The F-1 classification is stated as settled for an edit not yet made, though the same paragraph says the wiring's entry will give "Code's readings of F-2 and F-1".
    - Cite or quote the routing, and state the F-1 classification as the reading to be declared.
    - The forms named are m_sessions.py's (MLXLM_USE_MODELSCOPE and local-path refusals, the offline resolution, SNAPSHOT, and the post-load re-read with its model-id STOP: m_sessions.py:199-213, :1013-1037, :1513-1526).
64. **"Code's readings declared here (§9) are each a flag …"** (lock:30). **IMPRECISE.** One Code reading, N10's condition ("This is Code's reading of the condition, and the seat may strike it", lock:182), is declared in §3 and is not listed among §9's "Code's readings". The entry (entry:39-41) lists it correctly. Point §0 at §3 too, or list it in §9.
65. **G-SHAPE-F3 (§2)** (lock:134-147). **PASS.**
    - The re-run raw (results/raw/2026-11-07_mf3-gshape-f3-rerun.txt) is on HEAD 993eba1, at 19:24:56. G-SHAPE-F0's run on the same HEAD was at 19:24:22Z, and both were committed later (0786c11, f9700ba).
    - Artifact: A1/A2/A3 n = 2816/1408/1408, n_fired 0, exact; every required control has n_fired == n; Layer R 8448, 0 fired, control 8448/8448; Layer S problems []; Layer T n 640, n_failed 0.
    - Against the superseded artifact: 6 leaf differences, all under provenance (package_sha256, sources ×4, sources_digest).
66. **G-ANL-F3 (§3), apart from item 62** (lock:151-157). **PASS.**
    - The analyzer changed in place only at e0b4f2c and 10a2bbb.
    - The artifact: battery 525/525, expected 525, 538 coverage ids; v1_unchanged 2160/2160 and tables_equal; v2 tuples 519,480 = 300,625 + 218,855; verdict PASS.
    - The ganl raw's lines 534-540 show `cmp` IDENTICAL for the second run.
    - PIN-42 binding: see the seat's §8 observation.
67. **N1 at this lock (§10)** (lock:582-586). **PASS.**
    - 9480f9b is N1, and the ganl raw records HEAD 9480f9b.
    - The preprint is 45b67246…; PREPRINT-v1_0-draft.STATUS.md is tracked, 892 bytes.
    - `regression.preprint` has head_file_is_table true.
    - F3R-PREPRINT-OF-RECORD (m_analyze.py:9982-9988) asserts only `blob_sha256 == table_sha256` and reports the tree's sha256 and the boolean.
68. **m's package moved before this lock (§10)** (lock:587-589). **PASS.**
    - 993eba1 changes valence_core/m/gcal.py (and two scripts, plus raws).
    - m's package moves from 60199b36…feec to 7756dcf4…49bb; mf3's package is unchanged (f30ad505 at both).
    - "gcal" is in `guard.ABSENT_MODULES`, and none of the 11 M_HASHED files changed.

## Totals

68 items: **51 PASS, 14 IMPRECISE, 3 FAIL.**

- FAIL: 42 (bar row 6's numerator vs F-7), 49 (F32/F36/F59 declared as live readings after F-6/F-7), 50 (G-ANL-F3's register not byte-verbatim; its last sentence renders as a table row).
- IMPRECISE: 11, 18, 20, 33, 35, 45, 46, 47, 54, 58, 60, 62, 63, 64.

## Code's dispositions of pass 1 (2026-11-07; each item re-checked at source before it was applied)

- **42 (FAIL), bar row 6's numerator.** Confirmed: `bars.py:197–202` (`cd9756e`) reads "complete pairs whose
  transcripts differ in any byte". The stage decides by F-7's triple criterion (`_gid_pair`, the F-7 PIN at
  `stages.py:1140`), and `gid_decide` fails on a divergence in any pair. Applied: a dated note under the bar table
  (lock §8) says that F-7 governs and that the row's text is not edited, because an edit to `bars.py` would move mf3's
  package, which the lock names.
- **49 (FAIL), F32, F36 and F59.** Confirmed: the build design's flags tie F-6 to F32/F36 and F-7 to F59
  (`mf3-build_design.md:160–161`). The seat ruled both, and `e0b4f2c` applied them: `meta_identical` has 0 hits in
  `stages.py`, and the F-6 PIN is at `readrule.py:194`. Applied: a dated note under the F3 register (lock §9) marks
  F32's and F36's per-line booleans and F59 as superseded. The rest of the register stands.
- **50 (FAIL), G-ANL-F3's register not byte-verbatim.** Confirmed: `lockgen.py` dropped every blank line. Applied: a
  `section_lines` helper strips only the leading and trailing blank lines, so the register keeps its internal ones.
  The same helper is used for the F3 register and the module homes.
- **11 (IMPRECISE), banner tuples.** Applied: `TOLD_MAP` and `TOLD_MAP_SHAM` are listed clause by clause, each clause's
  UTF-8 bytes hashed. The values equal LOCK-m-F0.md's per-clause sha256.
- **18, the N10 quote.** Applied: the seat's first term is a blockquote, verbatim, with its inner double quotes.
- **20, F-6's paraphrase.** Applied: "before VERDICTS" restored.
- **33, the reasoning-cap checks.** Applied: `_extra`'s check is described stage by stage, and `prior_gate`'s "NOT THE
  FIXED CAP" (`stages.py:466–477`) is named from G-ID-F3 on. The sub-list nesting is fixed.
- **35, (g)'s naming of the weights.** Applied: the licence list says the lock's text names the weights' revision and
  sha256 too.
- **45, "every hash … in §1".** Applied: §1 holds the hashes a stage's licence checks; §3, §4 and §6 hold the
  lexicons', the schedule files' and the banner bytes'.
- **46, "every value below with a tool".** Applied: the claim is now confined to the tables and verbatim blocks under
  `####` headings. The prose's counts and abbreviations are declared to be Code's.
- **47, "Each site is listed after them" and the cost sentence.** Applied: F57's site, the driver, has no PIN line,
  and §0 says this lock names no hash of that file.
- **54, the interleave rule.** Applied: a generated block reproduces, verbatim, `gate_launch_order`'s and
  `interleave`'s signature, docstring and PIN (`schedule.py:185`, `:205`).
- **58, the entry's identity sources.** Applied: the entry says which values come from the lock's text and which from
  the files.
- **60, the VERDICTS reader's check unrecorded.** Applied: `licence_test.py` now runs the PIN-V2-12 names check, and
  its script and output are committed as `results/raw/2026-11-07_lock-m-f3_checks.txt`.
- **62, "before any lock or artifact named it".** Applied: it now reads "before any lock or G-ANL-F3.json named it",
  `10a2bbb`'s wording. m's three OLMo NOT-RUN outputs name `6ec3222b…`, as the same paragraph says.
- **63, the routing's record and F-1's settled form.** Applied: §11 item 1 says the routing was relayed in chat and
  is recorded in the wiring's entry, and that F-2's text places the check with the campaign's wiring, a dated note
  there quoting it. The F-1 reading is stated as Code's intent, to be stated on the edit as made.
- **64, N10's reading not in §9.** Applied: §0 and §9 both list N10's condition among Code's readings.

---

# Pass 2

# Blind values-check, pass 2: LOCK-m-F3.draft.md (A), entry_lock.md (B), 2026-11-07_lock-m-f3_checks.txt (C)

Checked against the repository at HEAD 02dadb3. The tracked tree was unmodified before and after (`git status --porcelain --untracked-files=no` empty; the full porcelain digest was the same before and after). The scratch worktree lock-wt2 is at 78c58f3, detached, parent 02dadb3. Its only change is LOCK-m-F3.md, which `cmp`s equal to (A), and its status was clean before and after. The pass-1 draft is lock-wt's LOCK-m-F3.md at a28bef6.

Python was the jlens-qwen36 venv with `-B`, `PYTHONDONTWRITEBYTECODE=1` and `HF_HUB_OFFLINE=1`. Rendering checks used markdown-it-py 4.2.0 (commonmark + table). I wrote only under S/lock/vc2/. I did not read dispositions1.md.

Line numbers are (A)'s (lock:N), (B)'s (entry:N) and (C)'s (checks:N). The four placeholders were not counted.

## 1. Pass 1's findings, re-derived at source

1. **Pass-1 item 11: the banner table, now listed clause by clause** (lock:314-317). **PASS.**
   - `fb.TOLD_MAP is mb.TOLD_MAP` and `fb.TOLD_MAP_SHAM is mb.TOLD_MAP_SHAM`. Both are 2-tuples.
   - Each clause's UTF-8 bytes recomputed:
     - TOLD_MAP: clause 0 is 134 bytes, 6bfc495b…89ba; clause 1 is 134 bytes, a6fe3b79…fae4.
     - TOLD_MAP_SHAM: clause 0 is 107 bytes, 5bdf9905…e3d3; clause 1 is 107 bytes, a8b3befd…8b25.
   - These are the full values LOCK-m-F0.md:1969-1972 gives ("TOLD-MAP, clause 0 (A0)" … "TOLD-MAP-SHAM, clause 1 (A0s)"), character for character. The labels follow LOCK-m-F0's.
   - The other 11 rows recompute unchanged. SESSION_BANNER and COMMON also equal LOCK-m-F0:1965-1968.

2. **Pass-1 item 18: N10's first reporting term, now a blockquote** (lock:184-187). **PASS.**
   - The two `> ` lines, joined by one space, are a byte-exact substring of p-preread answers line 52 (§7 N10), straight ASCII double quotes included.
   - The source continues with "; the case is a dated note…". The blockquote stops at "VERDICTS", which is a clean cut.
   - It renders as a blockquote inside the list item "The first term, verbatim:".
   - The second term (lock:193) is still a verbatim substring, ending at the source line's final period.
   - The ruling quoted in lock:178-179 is verbatim from the bolded text in the same line.

3. **Pass-1 item 20: F-6, "report no per-line list before VERDICTS; 'k of ≤ 36'"** (lock:432). **PASS.**
   - It now carries the ruling's limit, from ganl-f3 answers:29: "no per-line list is printed or reported before VERDICTS".
   - "k of ≤ 36" is verbatim.

4. **Pass-1 item 33: reasoning_cap's checks** (lock:71-72), and the rendering nit (lock:59-60). **PASS.**
   - `_extra` (stages.py:579-581) requires the cap to be in `REASONING_CAPS` = (60, 120), and 60 at "time".
   - `prior_gate` (stages.py:466-477) handles "id" and "qual": it re-computes `cap_trigger(...)["fixed_cap"]` from G-TIME-F3's checkpoint and refuses "NOT THE FIXED CAP" at :473. It is called with `reasoning_cap=extra["reasoning_cap"]` through `_licensed` (:676-681), which G-ID-F3 runs at :1189.
   - For the campaign, :475-477 compares against G-F3's recorded cap. That is the fixed cap transitively, so "against the cap G-TIME-F3's trigger fixes" holds in value.
   - Rendering: the sentence "The hashes and the weights it carries beside those…" now renders in the parent `<li>`, before the nested key list.

5. **Pass-1 item 35: the licence's lock-text condition** (lock:49-50). **PASS.**
   - `licence_problems` builds `named` from analyzer_sha256, package_sha256, weights_sha256 and weights_revision (stages.py:316-327), and requires each in the committed lock text (:365-369).
   - Each m file must be on one line with its sha256 (:370-375).
   - The bullet now says this.

6. **Pass-1 item 42: lock §8's dated note on bar row 6** (lock:412-420). **PASS.** Every anchor and commit checked:
   - The row is built at bars.py:197-202 (the `gid_divergence@G-ID-F3` F3Bar), numerator at :201 verbatim. bars.py's only commit is cd9756e, so "last edited at cd9756e" holds.
   - stages.py:1139 is `def _gid_pair`. :1140 is the first line of "PIN (the seat's F-7, 2026-11-06; …)". `identical` is `tr and lt`: transcripts equal and `_line_triples` equal. `_line_triples` is a per-line (n_tok, cap_hit, stop_reason) list.
   - guard.py:46-49 is the seat's F-7 PIN and `GID_CRITERION`, which carries the triple. Both were added at e0b4f2c (`git show e0b4f2c -- valence_core/mf3/guard.py`).
   - stages.py:1106 is `def gid_decide`. It returns FAIL on the first `not p["identical"]`, before testing `complete`, so "complete or not" holds.
   - `_gid_end` fires the bar on that FAIL: `bars.bar("gid_divergence@G-ID-F3").evaluate(int(status == "FAIL"), …)` (:1252).
   - "an edit to bars.py would move mf3's package" holds: bars.py is one of the 15 hashed files.
   - "F-7 governs" is the seat's own term (answers:30: "Bind it … a transcript-identical pair with a differing triple is a G-ID fire").

7. **Pass-1 item 45, as reworded: "The proposal's sha256 and every hash a stage's licence checks are in §1. The lexicons', the schedule files' and the banner bytes' sha256 are in §3, §4 and §6."** (lock:6-7). **IMPRECISE.**
   - The old overclaim ("every hash this lock names") is gone, and the second sentence is right.
   - But the licence checks `lock_sha256`: part (c) hashes the committed lock and compares it with identity_extra's (stages.py:303-315). That hash cannot be in §1. lock:57-58 says itself that the entry names it.
   - Read literally, "every hash a stage's licence checks" has one exception: this file's own.
   - Fix: "…every hash a stage's licence checks, this file's own excepted (its entry names it), are in §1".

8. **Pass-1 item 46, as reworded: "Every table and verbatim block under a `####` heading in §1–§9 was generated with a tool at the lock's HEAD (`lockgen.py`, Code's scratch); none is transcribed by hand."** (lock:38-39). **IMPRECISE.** This is a new exception, created by the fix for pass-1 item 18.
   - N10's first term is now a verbatim block, a blockquote introduced by "The first term, verbatim:" (lock:186-187). It sits under the heading "#### Counter (c)'s lexicons" (lock:169), whose section runs to "## 4.".
   - In the CommonMark rendering, the whole N10 note is the sixth `<li>` of that heading's generated lexicon list. The two blank lines do not end the list.
   - The block's text comes from lock_template.md:128-129, so it was transcribed by hand. Its bytes are verbatim (item 2), so no value is wrong, but the provenance claim is false for this one block.
   - No other table or verbatim block in §1-§9 is outside the generated sections. The §8 and §9 notes, under the bar-table and F3-register headings, hold only inline quotes.
   - The rest of the sentence holds. "The counts and abbreviated hashes in the prose of §2, §3 and §10 are Code's, taken from the artifacts and entries cited there" claims no totality, and the values are pass 1's items 12, 65-68, unchanged.
   - Fix: except the N10 quotation by name ("Code's transcription, checked verbatim"). Also separate the dated note from the generated list, for example with a paragraph line or its own heading before it, so the note does not render as an item of the "frozen here" lexicon list.

9. **Pass-1 item 47: F57's exception** (lock:31-34, lock:428-429). **PASS.**
   - `scripts/mf3_sessions.py` has no PIN-opening line. Its one "PIN" text, :19, is a reference: "the OLMo build's PIN O12 form".
   - An independent AST map of the 60 register sites found a PIN line in or just above the site span for 58 entries. F58's is the section-header PIN at guard.py:241, 44 lines above `class _F3CallSiteScan` (:285), and it heads that subject. F57 is the only site without one.
   - The 24 PIN-V2 ids have 25 sites, all in scripts/m_analyze.py.
   - So "The registers' sites are listed after them. F57's is the exception" holds.
   - "the analyzer's or mf3's package, both named here, or the driver's …, which this lock does not name" holds: no hash of mf3_sessions.py is in the lock.
   - Note, not a defect: by F-1, any driver edit other than subcommand wiring re-runs G-SHAPE-F3, whose artifact §1 names. A strike of F57 can still reach a named hash that way. The sentence does not claim otherwise.

10. **Pass-1 item 49: lock §9's dated note on F32, F36 and F59** (lock:504-517). **IMPRECISE**, on one anchor.
    - Correct:
      - F-6's flag concerns "(Q5, F32, F36)" and F-7's concerns "`meta_identical` (F59)" (mf3-build_design.md:160-161).
      - The seat ruled both (ganl-f3 answers:29-30).
      - e0b4f2c applied them:
        - `-"meta_identical"` / `+line_triples_identical` under the seat's F-7 PIN, stages.py:1140; `meta_identical` and `_gen_meta` no longer occur anywhere in valence_core/mf3;
        - `TIME_SESSION_KEYS` lost "reasoning_cap_reached", so the contrast block carries no per-line list.
      - The quoted fragments are verbatim register text. F32 has "plus the per-line cap booleans" and F36 has "the per-line cap booleans".
      - "The rest of the register stands" holds (item 42).
    - Imprecise: "the contrast block carries no per-line list (`readrule.py:194`, the seat's F-6 PIN)" points at the wrong function.
      - readrule.py:194 is the seat's F-6 PIN inside `strip_contrast`'s G-TIME-F3 branch (:177, :187-200). That is the stripped read record, F32's site.
      - "The contrast block" is `_contrast_block_time` (:471-486). The code's own term is at :485 ("the G-TIME-F3 contrast block is not its declared form"), and F36's register text says "G-TIME-F3's contrast block". That is F36's site, and its PIN at :472 is Code's, citing F-6.
      - Both forms carry no per-line list at HEAD. The note names one function and anchors to the other, and F36's site is not cited.
    - Secondary: the per-line booleans came from the seat's Q5 (prebuild answers:36). F-6's flag says "Built as Q5 rules", and the seat's F-6 "supersedes the per-line-list part of Q5 (answers:33)". The note calls them Code's readings, which matches the register's "Code's" framing, but never names Q5. "Two were Code's readings", under a heading that counts three, reads oddly: "two" counts the two subjects.
    - Fix: "neither the G-TIME-F3 strip (`strip_contrast`, readrule.py:194, the seat's F-6 PIN) nor the contrast block (`_contrast_block_time`, :471; Code's PIN at :472, citing F-6) carries a per-line list". Optionally add "(Q5's per-line part, which F-6 supersedes)".

11. **Pass-1 item 50: G-ANL-F3's register, verbatim** (lock:521-550). **PASS.**
    - It is byte-identical to ganl-f3_build_design.md lines 66-95 (30 lines). The two internal blank lines are at source 67 and 94.
    - markdown-it now gives that table 25 rows, a header and 24. The closing sentence is its own paragraph.

12. **Pass-1 item 54: the interleave rule in §4** (lock:245-270). **PASS.**
    - The two code blocks are byte-identical to the HEAD blob of valence_core/mf3/schedule.py at :185-190 (`gate_launch_order`) and :205-213 (`interleave`). Each is the signature, the docstring and the whole PIN block; the next line is code. The working tree equals the blob.
    - The rule is now stated: "next = the live arm with the fewest launches, ties to table order", plus the pairwise resume conditions.
    - The code matches the PIN: :228-237 checks the pairwise conditions, and :241 calls `m_schedule._rotation`.

13. **Pass-1 item 58: the entry's identity_extra** (entry:34-36). **PASS.**
    - From the lock's committed text: the eleven m files and the WEIGHTS line (licence_test.py:47-56).
    - From the files: the proposal's, the lock's, the analyzer's and mf3's package sha256 (:63-68). The lock's is hashed from the committed blob, which equals the file.

14. **Pass-1 item 60: the VERDICTS reader's three names** (entry:39-40). **PASS.**
    - licence_test.py now runs this check (:83-95), using `production_env(UNIT_F3)` with `UNIT_F3 = "Q-F3"` (m_analyze.py:2942).
    - It mirrors the reader: m_analyze.py:4130-4134 tests the committed analyzer blob's sha256, `env.package_sha256` and `env.closure_sha256` for presence in the lock text.
    - (C) records three True lines: d347ea0c…, 7756dcf4… and d19f336d….

15. **Pass-1 item 62: "before any lock or G-ANL-F3.json named it"** (lock:159-161). **PASS.**
    - The analyzer is 6ec3222b…c82b93d9 at e0b4f2c and at 10a2bbb~1, and d347ea0c… at 10a2bbb. The wording matches 10a2bbb's.
    - No LOCK-*.md at HEAD contains 6ec3222b. The pickaxe finds it only in the scratch commits a28bef6 and 78c58f3.
    - data/m/gates/G-ANL-F3.json was first committed at 02dadb3.
    - The three OLMo NOT-RUN outputs carry 6ec3222b, as the next sentence says.

16. **Pass-1 item 63, lock §11** (lock:664-675). **PASS.**
    - F-1's classification is now Code's stated intention, "states that reading on the edit as made".
    - The routing is attributed: "the coordinating session's routing of 2026-11-07, relayed in chat and recorded in the wiring's entry".
    - F-2's placement is disclosed, accurately: ganl-f3 answers:25 puts "the rest of m's pre-load check" with "the campaign subcommand's wiring".
    - Not checkable: the routing itself. No committed record at HEAD has it: RESULTS.md and results/raw/2026-11-0[67]_* hold no "DRIVER line" routing for the time wiring. The text now says it will be recorded in the wiring's entry.

17. **Pass-1 item 63, entry half (pass 1 cited entry:46-47)**, now entry:52-57: "the `time` wiring … under F-1's clearance. As routed on 2026-11-07, it carries the rest of m's pre-load check and a DRIVER line". **IMPRECISE.** Not updated with lock §11:
    - it still states the F-1 classification as settled;
    - it gives the routing without its source (chat, the coordinating session);
    - it omits F-2's placement with the campaign subcommand.

    Rendering nit: "Not pushed. Committed by path." (entry:57) renders inside the last sub-bullet ("then G-TIME-F3's six sessions. Not pushed. Committed by path.").

    Fix: mirror §11 ("Code intends it under F-1's clearance; the coordinating session's routing, relayed in chat, adds …; F-2 places the pre-load check with the campaign's wiring, and the wiring's entry gives Code's reading"), and put the closing line at the bullet's level.

18. **Pass-1 item 64: N10's condition in the list of readings** (lock:31, lock:427). **PASS.**
    - §0 now says "(§9, and N10's condition in §3)", and §9 lists "N10's condition (§3)".
    - Note: the next sentence, "Striking one moves the hash of its site's file", has no site file for N10's condition. In practice a strike means building the subclass count, which is an analyzer change, so "the analyzer's" covers it.

## 2. The other changes between the pass-1 draft and (A)

The `diff` has 17 hunks. Every hunk is covered by items 1-18 or by the two items below. Nothing changed outside them.

19. **The F3 build register and the module homes, still verbatim under the new rule** (lock:440-501, 288-303). **PASS.** Each is byte-identical to its source section of mf3-build_design.md, ignoring leading and trailing blank lines:
    - the F3 register: lines 56-117, 62 lines, no internal blank lines;
    - the module homes: lines 37-52, 16 lines, no internal blank lines.

    All 10 tables render with the expected row counts:

    | table | rows |
    |---|---|
    | §0 | 10 |
    | binding identity | 11 |
    | m files | 12 |
    | rulings | 7 |
    | schedules | 21 |
    | banner | 16 |
    | bars | 14 |
    | F3 register | 61 |
    | V2 register | 25 |
    | PIN sites | 91 |

20. **The fills** (fills_wrapped.json against fills.json). **PASS.**
    - Same 4 keys. Each wrapped value, with "\n  " replaced by " ", equals fills.json's.
    - Only ANALYZER_NOTE's wording changed from pass 1, and that is item 15.

## 3. Regeneration

21. **lockgen.py re-run from the repo root at HEAD 02dadb3** (`HF_HUB_OFFLINE=1`, output to S/lock/vc2/generated.md). **PASS.**
    - Exit 0, empty stderr.
    - The output is byte-identical to S/lock/generated.md (`cmp`).
    - The repo's porcelain digest was the same before and after.

22. **Recomposition in S/lock/vc2/** (copies of compose.py, lock_template.md and fills_wrapped.json, my generated.md; `python -B compose.py fills_wrapped.json …/LOCK-m-F3.recomposed.md`). **PASS.**
    - It printed "placeholders left: []".
    - The result is byte-identical to (A) and to lock-wt2's LOCK-m-F3.md: sha256 a45081812eeb91ae0957a8f4b248c189f7d891b6e9a1a5f7d7e2a52d3ce04747.
    - All 19 generated sections are used, each `@@GEN:…@@` prefix matching exactly one.

## 4. (C), the checks raw

23. **The output section** (checks:6-16). **PASS.** A fresh `python -B …/lock/licence_test.py`, run from lock-wt2's root with `HF_HUB_OFFLINE=1`, exits 0. Its stdout is byte-identical to (C)'s output section and to licence_test_out.txt.

24. **The stated lock sha256 and the scratch commit** (checks:2). **PASS.**
    - a45081812eeb…4747 is (A)'s sha256, and `git cat-file blob HEAD:LOCK-m-F3.md` in lock-wt2 gives the same.
    - 78c58f3 is detached, with parent 02dadb3, and differs from it only by LOCK-m-F3.md.

25. **The script section, and scrubbing** (checks:20-99). **PASS.**
    - The section is byte-identical to S/lock/licence_test.py (3,829 bytes). The script holds no roots, so nothing needed scrubbing; the header's `<tmp>` is the only scrub token.
    - No local path, user name, session id, hostname, hub-cache path or scratch-folder name occurs in (C), (B) or (A). I searched for the identifying strings: the user's and host's names, the home, private and temp roots, the session id, a UUID form, the scratch folder's name, the venv and clone directories, the hub cache's path and the scratch worktrees' names. (Code reworded this sentence before the commit so the raw does not spell them out.)

26. **The header's description** (checks:1-2): "builds identity_extra from the lock's committed text … and from the files …; licence_problems, then three mutations, then the Q-F3 VERDICTS reader's three names". **PASS.** It matches the code (:44-95), and the run is model-free.

27. **The script's own docstring, committed verbatim in (C)** (checks:21-30). **IMPRECISE.** It contradicts the code beneath it:
    - It says identity_extra is built "plus the hashes the lock names". The script hashes the proposal, the lock blob, the analyzer and mf3's package from the files (:63-68).
    - Its third mutation, "a lock text missing one m-file line (… out of scope; instead the m-file mapping is mutated so (e') and (f) both fire)", is the script's second mutation (bad2, :75-77). The actual third, the weights revision (bad3, :78-79), is not mentioned. Nor is the VERDICTS-reader check (:83-95).
    - (C)'s header and the entry describe the run correctly. The stale description is in the committed raw.
    - Fix: correct the docstring, re-run (the output is unchanged), and re-embed.

## 5. (B) against (A) and (C)

28. **The headline** (entry:1-4). **PASS.**
    - d347ea0c…5e48, f30ad505…6310, 0c9de56e…1461, b91a8c67…936c and 1b7d5a01…8028 each match their full values in (A) §1/§3, first 8 and last 4 characters.
    - N10's note is in lock §3 and N13's in lock §10.

29. **The routing** (entry:6-13). **PASS.**
    - `git show 139635f:RESULTS.md` line 81 is the quoted item 1, verbatim. Lines 79-81 are the intro line, a blank line and the quote.
    - The §9 item 1 quote is verbatim (p-preread answers:64).
    - The N1 answer's order is verbatim (n1-battery answers:11, §1).
    - The canonical ganl is 02dadb3.

30. **What a stage cites** (entry:14-19). **PASS.** It matches lock §1 and the generated values: renders_sha16 a04f67b0e5105a05; 60 and "uncached" at G-TIME-F3; prior_proposal_sha256s none.

31. **m:292's list by section; 13 bars** (entry:20-22). **PASS.** It matches lock §0's table, and `len(QF3_BARS)` is 13.

32. **"A generator in Code's scratch produced §1–§9's tables and verbatim blocks … Nothing in them is transcribed by hand."** (entry:24-25). **IMPRECISE**, for the same reason as item 8. The N10 blockquote (lock:186-187) is a verbatim block in §3, typed into the template (lock_template.md:128-129). It is verbatim (item 2), but it was not generated. Fix as item 8.

33. **The 90 PIN sites and the first draft's 79** (entry:26-30). **PASS.**
    - Re-inventoried independently: 90 lines across the 15 valence_core/mf3/*.py files, scripts/mf3_sessions.py (0) and scripts/m_analyze.py (27) open one of the two forms.
    - The only other "declared at LOCK-m-F3" lines are m_analyze.py:4441, :10088, :10090, :10092 and :10093: a header, a comment and battery strings.
    - The 15 other "PIN" mentions in mf3 and the driver are references ("m's PIN, carried", "PIN-S4"), not openings.
    - 79 + 9 + 2 = 90.

34. **Checks on the committed bytes** (entry:31-40). **PASS.**
    - The scratch worktree is 78c58f3 on 02dadb3, detached.
    - `licence_problems` returns [].
    - The three mutations are each refused, as (C) shows.
    - The VERDICTS names are each True.
    - The link label `_lock-m-f3_checks` follows RESULTS.md's convention (for example `_ganl-f3`, `_p-gshape`), and the relative path resolves from the root.

35. **Code's readings at this lock** (entry:41-44). **PASS.**
    - The two registers are verbatim (items 11, 19).
    - N10's reading matches lock:189-192.

36. **Dated notes, lock §8 and §10** (entry:46-47, 50). **PASS.** They match lock:412-420 and lock:651-660.

37. **Dated notes, lock §9: "the F3 build register's F32, F36 and F59 are superseded by the seat's F-6 and F-7, applied at `e0b4f2c`"** (entry:48-49). **IMPRECISE.**
    - The lock supersedes only F32's "plus the per-line cap booleans" and F36's "the per-line cap booleans", and all of F59. It then says "The rest of the register stands" (lock:516-517).
    - F36's remaining {s, forced rounds generated, excluded at forced} is exactly what `_contrast_block_time` implements (readrule.py:468, :480-482), and F32's ruling-(h) form stands.
    - The entry, unqualified, reads as all of F32 and F36 superseded.
    - Fix: "the per-line parts of F32 and F36, and F59, are superseded…".

## 6. Totality claims in the changed text

38. **"Every file the tables list is committed at HEAD with identical working-tree bytes"** (lock:40-41). **PASS.**
    - All 58 path-like strings in (A)'s tables were checked against `git ls-files`. Every file is tracked. The three misses are not files: `__init__.py` is F1's prose, `data/mf3` is a directory and `refs/main` is hub text.
    - The tracked tree is unmodified, and no untracked file sits under valence_core/, scripts/, data/mf3/ or data/m/gates/. So the package hashes see only committed files.

39. **"The registers' sites are listed after them. F57's is the exception"** (lock:428-429). **PASS** (item 9's inventory).

40. **"The rest of the register stands"** (lock:517). **PASS.**
    - Only three commits touch valence_core/mf3 or the driver: cd9756e (the build that wrote the register), e0b4f2c and 993eba1. 993eba1 touches only the driver's self-test check of m's package hash (mf3_sessions.py:176-179, its literal 60199b36 → 7756dcf4).
    - e0b4f2c's mf3 changes are the F-6 and F-7 applications and their docstrings and self-tests: readrule.py's strip, contrast block and docstring; stages.py's `_gid_pair`, `cap_trigger`'s reported fields, `_assert_time_form` and the CAP TRIGGER line; guard.py's GID_CRITERION.
    - Of the register's readings, only F32's and F36's per-line parts and F59 are contradicted.
    - F11 ("≥ 3 → 120 …") and F12 ("a divergence anywhere FAILs") still describe the code, with the counts now reported as "k of ≤ 36".

41. **"`gid_decide` … fails G-ID-F3 on a divergence in any pair, complete or not"** (lock:418). **PASS** (item 6).

42. **"Two registers, each verbatim below"** (lock:425) and **"each function's signature, docstring and PIN, verbatim"** (lock:245). **PASS** (items 11, 12, 19).

The other totality claims in changed text are items 7 ("every hash a stage's licence checks"), 8 and 32 ("none is transcribed by hand"), all IMPRECISE.

## Totals

42 items: **35 PASS, 7 IMPRECISE, 0 FAIL.**

- Pass 1's three FAILs are resolved: items 6, 10 and 11, with item 10 IMPRECISE on one anchor.
- Of pass 1's fourteen IMPRECISE items, eleven are resolved: items 1-5, 9, 12-15 and 18.
- Pass-1 item 63 is resolved in the lock (item 16) but not in the entry (item 17).
- Pass-1 items 45 and 46 are reworded, and the new wordings carry narrower exceptions (items 7 and 8).
- IMPRECISE: 7 (lock:6-7), 8 (lock:38-39), 10 (lock:514), 17 (entry:52-57), 27 (checks:21-30), 32 (entry:24-25), 37 (entry:48-49).

## Code's dispositions of pass 2 (2026-11-07; each item re-checked at source before it was applied)

- **7, the lock's own sha256.** Applied: §0 says every hash a stage's licence checks is in §1 "except this file's
  own sha256, which its entry names".
- **8 and 32, the N10 quotation's provenance and rendering.**
  - Applied: §1's provenance sentence and the entry name the one block that is not generated, the N10 quotation,
    which Code typed verbatim.
  - The dated note now opens as its own paragraph, so it no longer renders as an item of the generated lexicons
    list. The blockquote is unchanged.
- **10, the §9 note's anchors.** Confirmed: `readrule.py:194` is `strip_contrast`'s F-6 PIN, and the contrast block
  is `_contrast_block_time` (`:471`, Code's PIN at `:472`).
  - Applied: the note cites both.
  - It names Q5, which F-6 partly supersedes.
  - "Two were" now reads "The three were".
- **17, the entry's "Next".** Applied: it mirrors lock §11, with the routing's source, F-2's placement and F-1 as
  Code's intent. "Not pushed. Committed by path." is its own bullet.
- **27, the test's docstring.** Confirmed: it misdescribed the identity's sources and the mutations. Applied: the
  docstring is corrected and the test re-run (output unchanged), and (C) re-made on the revised lock's bytes
  (`c180606`).
- **37, F32, F36 and F59 in the entry.** Applied: "the per-line parts of F32 and F36, and F59, are superseded … The
  rest of the register stands."
- **The note under item 18** (N10's condition has no site's file). Applied: §0's cost sentence says that striking
  N10's condition means building the count, an analyzer change, which moves the analyzer's hash.
- **The note under item 9** (a strike of F57 that is not a subcommand wiring re-runs G-SHAPE-F3): no change. F-1's
  scope carries it, and §0 claims nothing otherwise.

---

# Pass 3

# Blind values-check, pass 3 (focused): LOCK-m-F3.draft.md (A), entry_lock.md (B), 2026-11-07_lock-m-f3_checks.txt (C)

Checked against the repository at HEAD 02dadb3. The tracked tree was unmodified before and after
(`git status --porcelain --untracked-files=no` empty), and the full porcelain digest was the same before and after.
The scratch worktree lock-wt3 is at c180606, detached, parent 02dadb3; its only change is LOCK-m-F3.md (686 lines
added), whose committed blob, its working file and (A) all hash to 5d29f5cd…0414. Its status (ignored files
included) was the same before and after my run in it, and no file in it was newer than my marker afterwards.
The pass-2 draft is lock-wt2's LOCK-m-F3.md at 78c58f3 (a4508181…4747).

Python was the jlens-qwen36 venv with `-B`, `PYTHONDONTWRITEBYTECODE=1` and, where the weights are read,
`HF_HUB_OFFLINE=1`. Rendering checks used markdown-it-py 4.2.0 (commonmark + table). I wrote only under
S/lock/vc3/ and this file. I did not read dispositions1.md or dispositions2.md. The sha256 of (A), (B), (C),
licence_test.py, its output file, lockgen.py, compose.py, the template, the fills and generated.md were the same at
the start and at the end of the check.

Line numbers are (A)'s (lock:N), (B)'s (entry:N) and (C)'s (checks:N). The four placeholders were not counted.

## 1. Pass 2's seven IMPRECISE items, and the note under its item 18

1. **Pass-2 item 7: "The proposal's sha256 and every hash a stage's licence checks are in §1, except this file's own
   sha256, which its entry names."** (lock:5-8). **PASS.**
   - `licence_problems` (stages.py:280-376) checks, by value: the proposal's and the lock's sha256 (:303-315),
     `analyzer_sha256` (:332-338), mf3's `package_sha256` (:339-340), the eleven `m_module_sha256` values
     (:341-344, `guard.M_HASHED` has 11 entries), and `weights_revision` / `weights_sha256` (:345-364), then their
     naming in the lock text (:365-375).
   - Every one is in §1 (the binding-identity table, the eleven-file table, the WEIGHTS line) except
     `lock_sha256`, which is now excepted. The entry names it (entry:2 `@@LSHA@@`, entry:15 `@@LSHA_FULL@@`).
   - The cached path's G-ID licence (`guard._gid_pass`: backend identifier and cap) is a different licence, and §1
     calls it "this backend's G-ID licence". So "a stage's licence" reads as §1's Q1 (C2) licence, and the claim
     holds.

2. **Pass-2 item 8: "The tables and the verbatim blocks in §1–§9 were generated with a tool at the lock's HEAD
   (`lockgen.py`, Code's scratch), with one exception: the N10 quotation in §3, which Code typed, verbatim from the
   seat's answer. Nothing generated is transcribed by hand. The dated notes, and the counts and abbreviated hashes in
   the prose of §2, §3 and §10, are Code's text, taken from the sources they cite."** (lock:40-44). **PASS.**
   - I located each of the 19 generated sections in (A) and classified every table, fence, code block and
     blockquote token of §1–§9 in the CommonMark parse by origin. 9 tables and 5 fences all lie inside generated
     sections; (A)'s tenth table, m:292's list, is in §0. The one typed block is the blockquote at lock:190-191,
     the N10 first term.
   - The template (lock_template.md) has no other table, fence or blockquote in §1–§9. Its 4-space lines are list
     continuations.
   - "Nothing generated is transcribed by hand": the recomposition (items 18-19) reproduces (A) byte for byte from
     lockgen's output and the template.
   - The second sentence makes no totality claim. The §2, §3 and §10 values are unchanged since pass 2.
   - The N10 note is now separated from the generated list (item 10).

3. **Pass-2 item 10: lock §9's dated note** (lock:508-522). **PASS.** Re-derived at source:
   - `readrule.py:194` is `# PIN (the seat's F-6, 2026-11-06; superseding the per-line-list part of Q5)`, inside
     `strip_contrast`'s G-TIME-F3 branch (:177, :187-200). `git blame` attributes :194-196 to e0b4f2c.
   - `readrule.py:471` is `def _contrast_block_time`, from cd9756e. :472 is `# PIN (Code, declared at LOCK-m-F3
     v0.1; the seat's ruling (h) carried, and its F-6 of 2026-11-06)`, which is Code's PIN citing F-6, added at
     e0b4f2c (blame :472-475).
   - `stages.py:1140` is `# PIN (the seat's F-7, 2026-11-06; a seat PIN at LOCK-m-F3 v0.1, set before G-ID-F3 has
     run)` inside `_gid_pair` (:1139), from e0b4f2c. `identical` is `tr and lt`, with `lt = _line_triples(u) ==
     _line_triples(c)`, the (n_tok, cap_hit, stop_reason) triples (:1134-1136).
   - Neither form carries a per-line list at HEAD:
     - the strip's G-TIME-F3 record holds `_STRIP_TOP` minus domain, rounds, pieces, transcript, `n_forced_rounds`,
       `excluded_at_forced` and blinding;
     - `TIME_SESSION_KEYS` = (s, forced_rounds_generated, excluded_at_forced) is asserted at :484-485.
   - `git show e0b4f2c` removes `tout["reasoning_cap_reached"] = _line_caps(rec)` from the strip, the same field
     from `_contrast_block_time` and from `TIME_SESSION_KEYS`, and `_gen_meta`/`meta_identical` from `_gid_pair`.
     `meta_identical` and `_gen_meta` occur nowhere in valence_core/mf3 or the driver at HEAD.
   - The Q5 statements:
     - "built as the seat's Q5 ruled" matches prebuild answers:36 ("for the contrast sessions the forced rounds
       beside (#116) with the per-line cap booleans") and the flag's own "Built as Q5 rules"
       (mf3-build_design.md:160).
     - "F-6 supersedes the per-line-list part of Q5" is ganl-f3 answers:29, "This supersedes the per-line-list part
       of Q5 (answers:33)". Prebuild answers:33 is Q5's heading.
     - "reports no per-line list before VERDICTS, and its booleans go to the checkpoint" matches :29's "no per-line
       list is printed or reported before VERDICTS" and "the per-line booleans and the realised totals go to the
       checkpoint".
   - "The three were Code's readings …, put to the seat as flags F-6 and F-7" matches the register's three rows (F32,
     F36, F59) and the flags (mf3-build_design.md:160-161). The count now agrees with the heading's "three".

4. **Pass-2 item 17: the entry's "Next"** (entry:53-62). **PASS.**
   - It now mirrors lock §11 (lock:669-680):
     - Code "intends" the edit under F-1's clearance, and the wiring's entry states the reading;
     - the routing is attributed to the coordinating session, "relayed in chat", with the wiring's entry recording
       it;
     - F-2's placement is stated, with the dated note to come.
   - F-1 (ganl-f3 answers:24) clears "an edit that wires a subcommand at its step, touching no scoring-stack
     function". F-2 (:25) has "the rest of m's pre-load check arrive with the campaign subcommand's wiring". Both
     match.
   - "its review and site check" is a procedural step, not in §11, and contradicts nothing.
   - Rendered, "Not pushed. Committed by path." is its own list item at the level of "**Next**" (entry:62), no
     longer inside "then G-TIME-F3's six sessions."
   - As in pass 2, the chat routing itself is not checkable at HEAD.

5. **Pass-2 item 27: the script's docstring, committed verbatim in (C)** (checks:21-31). **PASS.** It now describes
   the code without contradiction (the script's lines are cited by (C)'s numbering):
   - from the lock's committed text: the eleven m files' sha256 (checks:48-54) and the WEIGHTS line
     (checks:55-57);
   - from the files: the proposal's, the lock's, the analyzer's and mf3's package sha256 (checks:64-69);
   - `licence_problems` on the worktree, `[]` expected (checks:72-73);
   - the three mutations in code order: bad1 is the analyzer, bad2 the m file `corr`, bad3 the weights revision
     (checks:74-80). Each must be refused (`ok`, checks:97);
   - the VERDICTS reader's three names through `production_env(ma.UNIT_F3)` (checks:84-96), with
     `UNIT_F3 = "Q-F3"` (m_analyze.py:2942).

   Notes, not defects:
   - (i) The three "… named in the lock text" prints (checks:70-71, output lines checks:6-8) are not described by
     the docstring or by the header.
   - (ii) "from the files" includes the lock's sha256, which is hashed from the committed blob (checks:46, :66). In
     this clean worktree the blob equals the file. The entry says the same (entry:37).

6. **Pass-2 item 32: the entry's provenance sentence** (entry:24-26). **PASS.**
   - "The one exception is the N10 quotation in §3, which Code typed, verbatim from the seat's answer. Nothing
     generated is transcribed by hand."
   - This matches item 2's inventory: one typed verbatim block in §1–§9, the blockquote.

7. **Pass-2 item 37: "lock §9: the per-line parts of F32 and F36, and F59, are superseded by the seat's F-6 and F-7,
   applied at `e0b4f2c`. The rest of the register stands."** (entry:49-50). **PASS.** It is now qualified, as lock:521-522
   is.
   - Note: lock:521 quotes F32's superseded part as "plus the per-line cap booleans". F32's row
     (mf3-build_design.md:89) continues "; the list's length locates a free-phase end (flag F-6)". Read literally,
     "The rest of the register stands" keeps that clause, which describes the removed list. It decides nothing.
   - The entry's "per-line parts" naturally covers it. If an exact match is wanted, lock:521 could quote both of
     F32's clauses. Pre-existing; not counted.

8. **The note under pass-2 item 18: §0's new sentence "N10's condition has no site: striking it means building the
   count, an analyzer change, which moves the analyzer's hash."** (lock:35-36). **PASS.** It handles the note.
   - No line of valence_core/mf3, the driver or the analyzer mentions N10. The scorer's only related lines are
     PIN-V2-13's site (:3431) and the battery case (:10513, its label at :10519), which are PIN-V2-13's, not
     N10's.
   - `score_line_c` (:3472) returns {scored, class, labels} only. A "shared nearest term" count therefore needs new
     scoring code, and Q-F3's VERDICTS are the analyzer's.
   - It is the cost Code states, as §0's "at the cost Code states" (prebuild answers:50) requires.
   - It does not conflict with lock:186's "neither an analyzer change". That describes the seat's terms as ruled,
     whose first term is conditional on the output already recording the cause.
   - Pass 2's note under item 9 (F57: a strike can reach G-SHAPE-F3's named artifact through F-1) is unaffected.
     lock:33-35 is unchanged and still does not claim otherwise.

## 2. The other changes between the pass-2 draft and (A)

9. **The diff's coverage.** **PASS.**
   - `diff` lock-wt2/LOCK-m-F3.md (A) has five groups of hunks: lock:6-8, :35-36, :40-44, :181-198 and :510-519.
     They are items 1, 8, 2, 10-11 and 3.
   - A whitespace-normalized word diff confirms the scope of the last two:
     - In the N10 note, the only word change is the label "(Code's typing, the one block of §1–§9 not
       generated)". The rest is reflow and re-indentation.
     - The §9 note's changes are exactly those in item 3.

10. **N10's note, its new rendering** (lock:181-197). **PASS.**
    - In the CommonMark parse, the lexicon list after "#### Counter (c)'s lexicons" has 5 items: stage-1 terms,
      negative, positive, window and the lexicons' sha256. None contains "Dated note".
    - The dated note (lock:181-186) is a top-level paragraph that closes that list.
    - The terms follow as a separate top-level list of 2 items:
      - the first holds its label, the blockquote (level 2, lock:190-191) and a nested list of 3 items;
      - the second is the quoted second term.
    - The blockquote stays byte-verbatim. Its two lines, joined by one space, are a substring of
      p-preread answers:52, once, and its rendered text equals that join. The source continues "; the case is a
      dated note in LOCK-m-F3 …", so the cut is clean.
    - The second term is a verbatim substring ending the source line.
    - The ruling quoted in the bold header is verbatim from the line's bolded ruling.
    - The 10 tables of (A) render with pass 2's row counts: 10, 11, 12, 7, 21, 16, 14, 61, 25 and 91.

11. **The first term's new label: "The first term, verbatim (Code's typing, the one block of §1–§9 not
    generated):"** (lock:188). **IMPRECISE**: a new totality claim, true only as "verbatim block". This is wording
    only; no value is wrong.
    - Read literally, "the one block of §1–§9 not generated" is false. Every typed paragraph and list item of
      §1–§9 is a non-generated block in Markdown's sense. That includes the dated notes, and the second term
      itself, a list item consisting of the seat's text verbatim in quotes.
    - §1 (lock:40-41) scopes the exception to "the tables and the verbatim blocks". Under that vocabulary the
      blockquote is the only typed one (item 2), so the intended claim is true.
    - Fix: "(Code's typing; the one verbatim block of §1–§9 not generated)", or drop the totality: "(typed by Code:
      the exception §1 names)".

## 3. (B) since pass 2

The changed passages are entry:24-26, :49-50 and :53-62 (items 6, 7 and 4). Every other line matches pass 2's
citations, shifted by one line from entry:24 on.

12. **The rest of (B), re-derived quickly.** **PASS.**
    - Each abbreviated hash matches exactly one full value in (A): d347ea0c…5e48, f30ad505…6310, 0c9de56e…1461,
      b91a8c67…936c and 1b7d5a01…8028.
    - Each commit id resolves to the commit it is cited for: 02dadb3, 993eba1, e0b4f2c and f105bdd.
    - The routing quote (entry:7-9) is verbatim from `git show 139635f:RESULTS.md` line 81.
    - The 90 PIN sites recount as 90 by `/usr/bin/grep -c` over the named files: mf3 63, the driver 0, the
      analyzer 27.
    - The identity_extra sources (entry:35-37) match the script at checks:46-69.

13. **(B)'s rendering.** **PASS.** The entry parses as one top-level item with its sub-items in the intended order.
    No closing text is absorbed into a deeper item (item 4).

## 4. (C), the checks raw

14. **A fresh run's output** (checks:6-16). **PASS.**
    - `python -B …/lock/licence_test.py`, run from lock-wt3's root with `HF_HUB_OFFLINE=1`, exits 0 with empty
      stderr.
    - Its stdout (1,511 bytes) is byte-identical to (C)'s output section (`cmp`) and to licence_test_out.txt.

15. **The stated lock sha256 and the scratch commit** (checks:2). **PASS.**
    - 5d29f5cd43af2ed7b0382a3696ba1bc25bdb373b4b46a9f1aa42e68ebbf10414 is (A)'s sha256. It also equals
      `git cat-file blob HEAD:LOCK-m-F3.md` in lock-wt3 and lock-wt3's working file.
    - c180606 is detached, with parent 02dadb3, and adds only LOCK-m-F3.md.
    - The header's description of the run matches the code (item 5).

16. **The script section** (checks:20-100). **PASS.**
    - The fenced section (checks:21-99) is byte-identical to the current S/lock/licence_test.py (3,959 bytes,
      `cmp`).
    - The script takes its root from `Path.cwd()` and holds no local root, so nothing needed scrubbing. The
      header's `<tmp>` is the only scrub token.

17. **Scrubbing.** **PASS.** None of these occurs in (A), (B), (C) or licence_test.py:
    - the user name, in any case, or the surname;
    - the host name;
    - a local root (home, private, temp or var-folders), the temp and scratch-folder names, or the session id;
    - any UUID form;
    - `.venv`, `jlens-qwen36`, `.cache`, `huggingface` or a hub-cache path;
    - `lock-wt`, `wire-wt`, `scratch@` or an e-mail address.

## 5. Recomposition

18. **lockgen.py re-run from the repo root at HEAD 02dadb3** (copied to S/lock/vc3/, identical by `cmp`;
    `HF_HUB_OFFLINE=1`; output S/lock/vc3/generated.md). **PASS.**
    - Exit 0, empty stderr. The output (47,662 bytes, header "generated by lockgen.py at HEAD 02dadb3") is
      byte-identical to S/lock/generated.md.
    - The repository's porcelain digest was the same before and after. The only path newer than the marker was the
      .git directory entry itself (git's own status refresh). Nothing under jlens-qwen36 changed.

19. **compose.py in S/lock/vc3/** (copies of compose.py, lock_template.md and fills_wrapped.json, identical by `cmp`;
    `python -B compose.py fills_wrapped.json …/vc3/LOCK-m-F3.recomposed.md`). **PASS.**
    - It printed "placeholders left: []".
    - The result is byte-identical to (A) and to lock-wt3's LOCK-m-F3.md: sha256
      5d29f5cd43af2ed7b0382a3696ba1bc25bdb373b4b46a9f1aa42e68ebbf10414.
    - All 19 generated sections are used, each `@@GEN:…@@` prefix matching exactly one.

## Notes, not counted (none changed since pass 2)

- **N10's "two reporting terms".** The source (answers:52) reads "Two reporting terms, neither an analyzer change:
  [subclass count]; the case is a dated note in LOCK-m-F3 v0.1 (PIN-V2-13's known limitation), and the seat's blind
  read scores such lines by (label, polarity) as m:312 has it."
  - The lock takes the count and the blind-read clause as the two terms. The middle clause is fulfilled by the
    note's own existence ("It is PIN-V2-13's known limitation").
  - Another parse is possible: the second term as the whole of "the case is a dated note …, and the seat's blind
    read …". Every clause is covered either way, and every quotation is verbatim.
- **Where the generator's inputs come from.** (B)'s "from the committed code and artifacts at `02dadb3`"
  (entry:24-25) is loose:
  - the two registers and the module homes come from committed design raws (results/raw), and the rulings table's
    commits from git history;
  - the WEIGHTS line comes from the local hub cache, through `mf3_sessions.py hashes`. It is a list item, not a
    table or verbatim block, so the sentence does not cover it.
  - Nothing is mis-sourced.
- **Item 7's note:** F32's clause on the list's length.
- **Item 5's notes:** (i) and (ii).

## Totals

19 items: **18 PASS, 1 IMPRECISE, 0 FAIL.**

- All seven of pass 2's IMPRECISE items are resolved, correctly: items 1-7.
- The note under pass-2 item 18 is handled by §0's new sentence: item 8.
- The N10 note no longer renders as an item of the lexicon list, and its blockquote is byte-verbatim against
  p-preread answers:52: item 10.
- (C)'s fresh run, sha256, script section, docstring and scrub all hold: items 14-17 and 5.
- The recomposition is byte-identical to (A): items 18-19.
- IMPRECISE: item 11 (lock:188), the label's "the one block of §1–§9 not generated", a new totality claim true only
  as "verbatim block".
- If (A) is edited for it, (A)'s sha256 moves. (C)'s stated sha256 and its scratch commit (checks:2), and the
  entry's placeholders, then need regenerating on the new bytes.

## Code's dispositions of pass 3 (2026-11-07)

- **Item 11 (IMPRECISE), the blockquote's label.** Applied as suggested: "(Code's typing; the one verbatim block of
  §1–§9 not generated)".
- **The uncounted notes:**
  - the test's docstring now gives the lock's sha256 source (its committed blob) and the three "named in the lock
    text" prints;
  - the §9 note now quotes the whole superseded clause of F32, "plus the per-line cap booleans (Q5); the list's length
    locates a free-phase end (flag F-6)";
  - N10's two terms: no change, since every clause is covered and quoted verbatim;
  - the entry's sources sentence now names the design raws and, for the WEIGHTS line, the hub cache's snapshot.
- **Verified by tool after these edits:**
  - the composed lock differs from pass 3's bytes in exactly the two template edits (diff);
  - `lockgen.py` re-run at HEAD reproduces `generated.md` byte for byte;
  - the licence test on the final bytes (scratch commit `7058c85`) passes with the same result lines;
  - (C) is re-made on those bytes (lock sha256 `377c5d60…6ce7`).
