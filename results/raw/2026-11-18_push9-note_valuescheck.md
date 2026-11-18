# The dated note on push #9 and its gitleaks halt: the blind values-check, two passes (PI date 2026-11-18)

Code's raw (the coordinating session). Two fresh blind checkers, subagents of the coordinating session, checked the
dated note this commit adds. Each brief:
- quoted the list of record v2's items 1–5, with item 4's amendment by C.2 of 2026-11-16;
- carried the briefs' two lines, "a git command in a check takes item 3's pathspec" and "a glob is expanded and read
  before it is looped over";
- required the `data/mf3` exclusion while Q-F3's campaign runs, and no listing of `results/raw`;
- barred the gitleaks JSON reports in the coordinating session's scratch, which hold matched values from inside
  `data/*/reports`;
- allowed no interpreter.

Pass 1 checked the first draft. Pass 2 checked the whole revised draft, with pass 1's report beside it. Each report is
reproduced whole, as its hand-back message gave it, with the harness's two-space indent removed. Each is byte-identical
to the unindented copy of the report that the session's record also holds. Neither held a local path.

The reports name the coordinating session's scratch files: the note's draft, the push's record, the screen's and the
classifier's outputs for both runs, the helper's outputs and its source. Their line numbers index the drafts each pass
read. The committed note is the draft after the dispositions below.

## 1. Pass 1: the report, whole

VALUES-CHECK: the dated note on push #9 and its gitleaks halt. 37 items: 30 CONFIRMED, 4 IMPRECISE, 0 FAIL, 3 NOT CHECKABLE; 7 observations.

HEADER
- Read, scratch: the scratch note9.md:1–31 (its line 30 placeholder skipped); push_record9.txt:1–24; screen9_final.txt:1–7; gl9_final_classified.txt:1–3; gl9x_final.txt:1–2; gl9x_6e3.txt:1–2; gl4_6e3.txt:1–3; gl9x.py:1–40 (read as text, not run).
- Read, repo: `results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md`:1–63 and `results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md`:1–67, both whole. `valence_core/n/schema.py`:300–329, 400–479, 605–644 and 1100–1179, plus grep hits. `valence_core/n/guard.py`:1–89. `RESULTS.md`:1–150, 920–1009, 1512–1525 and 4612–4711, plus grep hits for "C.5", "Push, with a note", "Not a STOP" and "reports/backend-ext".
- Git: the subjects of the named commits (6df2131's whole); a parent walk from 1272702; the local origin/main ref; `git show <rev>:` of schema.py, n/keys.py and n/runner.py, each piped to a one-line grep.
- Tools: the Read tool; `/usr/bin/grep` on named files; `git log`, `show`, `rev-parse`, `hash-object`, `ls-files`, `grep` and `merge-base`, with item 3's pathspec plus `':!data/mf3/**'` on every path-taking form; `cut`, `fold`, `head`, `wc -l`; and `gitleaks version`.
- Not done: I did not list the scratch folder and did not touch any `*.json` in it. I opened, listed, hashed and searched nothing under `data/`. No interpreter ran, no write, no git status, no fetch, no network.

ITEMS
1. L1 "2026-11-18". CONFIRMED. push_record9.txt:24 says "pushed 2026-11-18", and all six commits in the range carry commit date 2026-11-18 (git log %cs).
2. L1 "push #9". CONFIRMED. 7a54eb9's subject names "push #8's C.5 line", which is RESULTS.md:991–995, `dc6a1cf..ad856f0`. This range starts at ad856f0. The C.5 ranges form one unbroken chain back to the 2026-11-15 push `16c99d5..fa27c45` (:4628): :4700, :4703, :1516–1523, :936, :993. Counted that way, that push is #1 and this one is #9.
3. L1 "its one gitleaks halt". CONFIRMED. gl9_final_classified.txt:1–3 shows 1 finding and one HALT line. push_record9.txt:16 has "gl4 exit=2", and the screen exited 0 (:10).
4. L1–2 "pushed on the PI's "Push, with a note"". CONFIRMED. push_record9.txt:1, :21 and :23 say so. The local origin/main ref resolves to 1272702's full id, which equals :23's.
5. L2 "Not a STOP." CONFIRMED, as consistent with precedent. Item 4 makes the match "a halt for the seat", and this note puts it there. The 2026-11-16 halt went to the seat the same way: a dated note after the PI's "Push, with a note" (RESULTS.md:4623–4640), and C.3 :47 let that word stand. The same phrase appears at RESULTS.md:870 and :1496.
6. L3 "`ad856f0..1272702`, 6 commits (`6df2131`, `bfc869f`, `3b2b855`, `7a54eb9`, `f3e7190` and `1272702`)". CONFIRMED. The parent walk gives 1272702~5..~0 = 6df2131, bfc869f, 3b2b855, 7a54eb9, f3e7190, 1272702, and ~6 = ad856f0. No commit has a second parent. screen9_final.txt:1 says "6 commits", and push_record9.txt:12 says "6 commits scanned".
7. L4–5, the coordinating session's question, verbatim. CONFIRMED, by push_record9.txt:1's quote only (chat is not visible here).
8. L5 "the PI answered "Push, with a note" (2026-11-18)". CONFIRMED, by the record only: push_record9.txt:1 for the words, :24 for the date.
9. L5–6 "The push carried `6df2131`'s stage report and cell". CONFIRMED. 6df2131's subject: "Committed by path: … the stage report (data/n/reports/backend-ext.json) and its one cell's JSON (data/n/ckpt/backend-ext/N1-V__none__0.json …)". 6df2131 = 1272702~5, and origin/main = 1272702.
10. L6–7, §4's words, "the cell and the report are pushed with their commit, under the `.gitattributes` line of `6df2131`". CONFIRMED, verbatim. Source: the third sitting's answers :32, header :3 ("PI date 2026-11-18 (third sitting)"), routing item 4 :59. 6df2131's subject names "/data/n/ckpt/** -diff in .gitattributes".
11. L8 "C.5, for the push." (the line's form). IMPRECISE. C.5 (:49) records each push's screen "in one line (its range, the classes matched, the halts, the PI's word)". The earlier C.5 lines carry the range, the commit count and the PI's word in the line itself (RESULTS.md:936, :993, :1516–1523, :4700, :4703). This line leaves them to the bullet above; its content is otherwise confirmed (items 12–16). Fix: "**C.5, for the push** (gitleaks 8.30.1, the one on the laptop's path; its output does not print its version): `ad856f0..1272702`, 6 commits, on the PI's word "Push, with a note" (2026-11-18). The screen (C.2 form) was CLEAR in every class, with nothing matched inside `ckpt` or `reports`. gitleaks found one `generic-api-key` match, inside `data/n/reports`: a halt, below. There was no other halt."
12. L8–9 "The screen (C.2 form) was CLEAR in every class, with nothing matched inside `ckpt` or `reports`." CONFIRMED. screen9_final.txt:2–7 lists six classes, each "inside: 0 -> CLEAR". push_record9.txt:2 has "screen4.py, C.2 form" and :10 "screen4 exit=0". The screen's source is not among the named files, so "C.2 form" rests on the record.
13. L9 "gitleaks 8.30.1 (the one on the laptop's path". CONFIRMED. push_record9.txt:12 says "gitleaks 8.30.1 over ad856f0..1272702", and `gitleaks version` on the laptop's path printed 8.30.1.
14. L9 "its output does not print its version)". NOT CHECKABLE. gitleaks' own scan output is not among the readable files (its JSON reports are barred). The classifier's output (gl9_final_classified.txt:1–3) prints no version. The phrase repeats RESULTS.md:991–992.
15. L9–10 "found one `generic-api-key` match, inside `data/n/reports`". CONFIRMED. gl9_final_classified.txt:1–2: "('data/n/reports', 'generic-api-key', 'hex64-other') x 1".
16. L10 "There was no other halt." CONFIRMED. The screen was all CLEAR with exit 0 (screen9_final.txt:2–7; push_record9.txt:10), and the classifier printed one HALT line (gl9_final_classified.txt:3).
17. L11–12 "C.3, in the seat's answers of 2026-11-16" and its link. CONFIRMED. Header :3: "Design seat, PI date 2026-11-16 (second sitting)"; C.3 is at :47. The linked path is tracked and clean at HEAD (rev-parse HEAD:path equals hash-object).
18. L13–14, the C.3 quote. CONFIRMED, verbatim, backticks included (:47).
19. L15 "a 64-hex value". CONFIRMED. gl9_final_classified.txt:2 has "hex64-other". gl9x_final.txt:2 has "inside, 64-hex, examined: 1", and gl9x.py:26 admits only a full 64-hex secret.
20. L15 "in `data/n/reports/backend-ext.json` at `6df2131`". CONFIRMED. gl9x_final.txt:1 gives "in data/n/reports at 6df2131". 6df2131's subject names the stage report as data/n/reports/backend-ext.json, with ".gitignore admits for exactly those two" (the report and the cell). push_record9.txt:21 agrees. The file was not opened.
21. L15–16 "under a key whose name carries no "sha", so it stayed a halt." CONFIRMED. The classifier classed it 'hex64-other' and printed "HALT: a non-digest finding inside ckpt/reports, for the seat (C.3)" (gl9_final_classified.txt:2–3). C.3 :47 says "any other 64-hex match inside stays a halt". push_record9.txt:24 says "a 64-hex value under a key without 'sha' (C.3: a halt)". The classifier's own source is not among the named files.
22. L17 "A helper of the screen's, printing classes only (C.2's form: no value, key or line)". IMPRECISE. gl9x.py prints no value, key, line or path content (:3–4, :37–40). But C.2 (:46) allows a match inside to print only "the rule's name and a shape class (length and alphabet) beside the count by path class". The helper also prints the finding's commit and two yes/no classes derived from the key and the value. C.2's prohibitions also name "a path's content". Fix: "A helper of the screen's, printing the rule's name, the path class, the commit and two yes/no classes, never a value, a key, a path's content or a line (C.2's words; the yes/no classes go beyond C.2's rule name and shape class, for the seat to class), found that …".
23. L17–18 "found that its key is a tracked repository path at that commit, and that its value equals that file's sha256 there." CONFIRMED. gl9x_final.txt:1: "key is a tracked repo path at that commit: yes; secret equals that file's sha256 there: yes". The method is gl9x.py:30–35.
24. L19–20, the schema quote, "repo path -> sha256 of each module n imports unchanged". CONFIRMED, verbatim. It is schema.py:436, inside STAGE_IDENTITY_FIELDS (:429–460). The line is the same at ad856f0, 6df2131 and HEAD, and the blob is equal at ad856f0 and HEAD.
25. L20 "a module digest keyed by its path". CONFIRMED. guard.py:48–49 builds "{repo-relative path: sha256} for the given sys.modules snapshot's valence_core modules outside n" (:62 `out[rel] = sha256_file(p)`). In the report schema (REPORT_FIELDS :1103–1120 and the tables it nests), this is the only map of 64-hex values whose keys can be repo paths (type path_sha256, :623–625). The other maps: layer_sha256 keys are layer numbers (:616–619); dir_sha16 values are 16-hex (:626–629); `cells` maps file names to objects whose digests sit under *_sha256 names (:1111–1113). So placing the finding in this map is an inference from the helper and the schema; the report was not opened.
26. L20–21 "generic-api-key's keyword matches a path holding "keys"." NOT CHECKABLE. The helper prints no key (gl9x.py:3–4, :37–39), so which path matched is not shown. The claim is consistent with the code: n imports `valence_core.m.keys` (valence_core/n/keys.py:27 "from ..m.keys import stream"; valence_core/n/runner.py:66 "from ..m.keys import stream_known_answer", both at ad856f0 and 1272702). By guard.py:7–10, the closure that imported_sha256 records (scripts/n_sessions.py:956) therefore holds `valence_core/m/keys.py`, which is tracked at both commits. Citing that import would make the inference checkable.
27. L22 "The third sitting's §4 cleared the screen's halt on `data/n/ckpt/**` only." CONFIRMED. :32 says "the pre-push screen's halt on `data/n/ckpt/**` is cleared by this ruling", and :59 has "the screen's halt on data/n/ckpt/** cleared". No other path's halt is named.
28. L22–23 "The PI's word, with this note, carried the push". CONFIRMED. push_record9.txt:21 says "HALT disposition: on the PI's 'Push, with a note'", and :23 records the push. Third sitting :32: "The push itself is the PI's word, as always."
29. L23 "as the PI's "Push, with a note" carried the three matches of C.3's own origin." CONFIRMED. C.3 :47: "The three gitleaks matches … The PI's "Push, with a note" stands as the push's word." See also RESULTS.md:4626 and :4637–4640.
30. L24 "The same class recurs in the resumed report committed at `6e3474d`: one match, with the same helper result." CONFIRMED. gl4_6e3.txt:1–3 is the same tuple, x 1, with HALT. gl9x_6e3.txt:1 is "in data/n/reports at 6e3474d", yes and yes. RESULTS.md:105 (6e3474d's entry) commits "the resumed report `data/n/reports/backend-ext.json`, which `6df2131`'s admit covers".
31. L25 "That commit is not pushed". CONFIRMED. origin/main = 1272702. `merge-base --is-ancestor 6e3474d origin/main` says no, and origin/main..HEAD lists 303953c and 6e3474d.
32. L25 "and its push needs the PI's word." CONFIRMED. Third sitting :32: "The push itself is the PI's word, as always."
33. L26 "C.3's test reads the name of the key immediately before the value." IMPRECISE. C.3's words (:47) are "under a key whose name carries `sha`". The immediate-key form belongs to the screen's classifier. That is consistent with its 'hex64-other' class for a value that items 23–25 place inside imported_sha256, but its source is not among the named files. Fix: "The screen's form of C.3's test reads the name of the key immediately before the value (C.3's words: "under a key whose name carries `sha`")."
34. L26–28 "A digest keyed by a repository path inside a map whose field carries "sha" (`imported_sha256`) fails that test." IMPRECISE. As a general statement it fails for paths that themselves hold "sha": the tracked `valence_core/m/gshape.py`, `valence_core/mf3/gshape.py` and `valence_core/p/gshape.py` ("gshape") would pass an immediate-key test. Fix: "A digest keyed by a repository path that carries no "sha", inside a map whose field does (`imported_sha256`), fails that test."
35. L28–29 "A digest class for "a 64-hex value equal to the sha256 of the tracked file its key names" would clear this class by construction; the helper already computes it." CONFIRMED. gl9x.py:30–35 computes exactly that, both findings are yes/yes (gl9x_final.txt:1, gl9x_6e3.txt:1), and guard.py:48–63 maps each module's path to its file's sha256.
36. L29 "Adopting it, or not, is the seat's." CONFIRMED. CLAUDE.md §Two-instance workflow says "findings flagged, never silently applied; Code escalates fired gates, never self-adjudicates". C.1 :45 says "the seat clears it, in a line".
37. L31 "Committed by path: this note and its values-check raw. Nothing ran on a model. Not pushed." NOT CHECKABLE: the commit has not been made yet. The helper's source calls only git and hashlib (gl9x.py:8–12, :18–19).

OBSERVATIONS
1. HEAD is now 303953c ("Close line (the pod session's) on n-build's entry for the BACKEND extension's resume …"), a child of 6e3474d. Both are unpushed. The 6e3474d outputs (gl4_6e3, gl9x_6e3) cover that commit alone, so the next push's screen and gitleaks run would need to cover 1272702 up to its tip, 303953c included.
2. gl9x.py's docstring (:1–2) says it examines findings "that gl4 leaves as non-digest". Its code (:23–27) consults neither gl4 nor any key-name test: it examines every finding inside `data/*/ckpt` or `data/*/reports` whose secret is 64-hex, and :40 counts those. Here the two sets are the same. Its tracked-path test, `git cat-file -e` (:32), also passes for a directory. The equality test (:35) then decides, and it said yes both times.
3. On item 22, for the seat: the 2026-11-16 note disclosed its classifier's shape-class print as a departure (RESULTS.md:4649–4650), and C.2 then amended item 4. The helper's yes/no classes are new prints of the same kind. Stating them that way would follow the precedent.
4. C.1 (:45) asks that a halt go to the seat "with the re-run beside it". The note puts the helper's classes beside the halt but names no re-run of gitleaks or its classifier. Whether the helper's run counts as that re-run is the seat's call; the note could say whether the classifier was re-run.
5. "By construction" (item 35) holds only while the module's bytes at the report's commit equal those hashed at the run: guard.py hashes at the run (:44–45, :62), the helper at the finding's commit (gl9x.py:35). A module edited in between would leave a true digest unequal, so it would stay a halt.
6. Tooling on this git: under item 3's exclusions, `git ls-files` with any literal path printed nothing even for the tracked `valence_core/m/gshape.py`, in all three forms (`':!…'`, `':(exclude,glob)…'`, `':!data/**'`). A pattern with a leading wildcard (`'*keys*'`) matched. So the brief's caution about a lone results/raw file applies to any literal path; check tracked status with rev-parse against hash-object.
7. No tracked gitleaks configuration exists (departure 1's query found no `.gitleaks.toml`). The record (push_record9.txt:12) does not say which rule set the run used, which bears on item 26.

DEPARTURES (HEAD 303953c throughout)
1. A listing of results/raw names. `git ls-files -- '*gitleaks*'`, run with the exclusions, printed six tracked results/raw names (the N12 gitleaks raws of 2026-10-09 to 2026-11-04) and `scripts/audit_note_N12_gitleaks.py`. Names only. This breaks "no listing of results/raw".
2. A tree-wide name query, `git ls-files -- '*keys*'` with the exclusions. It printed `valence_core/{m,mf3,n,p}/keys.py` and no results/raw name, though it could have printed one.
3. Git commands with no pathspec, because they take none: `git merge-base --is-ancestor`, twice, printing yes/no; and `git rev-parse` of revisions and of `<rev>:<path>` for named non-data paths (as the brief sanctions), printing ids or yes/no.
4. Reads beyond the brief's repo sources, all inside the repo and none under `data/`: guard.py; `git show` of n/keys.py and n/runner.py at ad856f0 and 1272702, and of schema.py at ad856f0 and 6df2131, each piped to a one-line grep; git grep (with the exclusions) over `valence_core/` and `scripts/n_sessions.py`; RESULTS.md beyond its C.5 lines; 6df2131's whole subject.
5. One run of `gitleaks version`, which printed only the version.

TOTALS: 37 items: 30 CONFIRMED, 4 IMPRECISE (11, 22, 33, 34), 0 FAIL, 3 NOT CHECKABLE (14, 26, 37), and 7 observations.

## 2. Pass 1: dispositions

**The four IMPRECISE items, each applied:**
- 11: the C.5 line carries the range, the count and the PI's word, in C.5's form.
- 22: the helper's prints are stated, and those beyond C.2's form are disclosed as the coordinating session's
  departure. Pass 2's item 28 added the commit to them.
- 33: "The screen's form of C.3's test"; pass 2's observation 5 then set it beside C.3's nesting reading.
- 34: a path "that carries no "sha"".

**The observations:** 1 and 2 needed no text in the note; 2 concerns the helper's docstring, a scratch tool's. Applied:
- 3, the departure;
- 4, the re-run;
- 5, the condition on the digest class;
- 6, the tooling reading, which Code re-ran: it holds for `valence_core/m/gshape.py` and `valence_core/n/runner.py`,
  as for the `results/raw` file, but not for `scripts/n_sessions.py` or `CLAUDE.md`, so "any literal path" was too
  wide;
- 7, the rule set.

Item 26's suggestion, to cite the import, is applied too.

**The checker's departures**, as its report states them, for the seat to class:
- a `git ls-files` glob query that printed six tracked `results/raw` names;
- a tree-wide name query for `keys`;
- git commands that take no pathspec;
- reads beyond its named sources, none under `data/`;
- `gitleaks version`.

## 3. Pass 2: the report, whole

VALUES-CHECK PASS 2: the dated note on push #9 and its gitleaks halt. 50 items: 42 CONFIRMED, 3 IMPRECISE, 0 FAIL, 5 NOT CHECKABLE; 8 observations.

HEADER
- Read, scratch (by name only):
  - note9.md:1–48, with its line-47 placeholder skipped;
  - vcn1/report_n1.txt:1–65;
  - push_record9.txt:1–24;
  - screen9.txt:1–7 and gl9_classified.txt:1–3;
  - screen9_final.txt:1–7, gl9_final_classified.txt:1–3 and gl9x_final.txt:1–2;
  - gl9x_6e3.txt:1–2 and gl4_6e3.txt:1–3;
  - gl9x.py:1–40, read as text and not run.
- Read, repo:
  - the seat's answers of 2026-11-16 (:1–63) and of 2026-11-18, third sitting (:1–67), both whole;
  - valence_core/n/schema.py:425–464 and :605–644, plus grep hits;
  - the import lines of valence_core/n/keys.py and valence_core/n/runner.py;
  - valence_core/n/guard.py, whole;
  - results/raw/2026-11-18_n-step4_bext-resume4_hashes.txt (:1–12), whole;
  - RESULTS.md:1–115, :300–424, :925–1004, :1508–1527 and :4618–4712, plus grep hits.
  - Every repo file read was tracked and clean at HEAD (rev-parse against hash-object), so the RESULTS.md line numbers are those at HEAD 303953c.
- Git:
  - the subjects of 6df2131 (whole), 6e3474d and 7a54eb9 (phrases only);
  - ad856f0..HEAD, with parents and commit dates;
  - the local origin/main ref, and origin/main..HEAD;
  - `git show 6df2131:` of n/keys.py, n/runner.py, n/schema.py and n/guard.py, each piped to a one-line grep;
  - blob-id comparisons by rev-parse;
  - the lone-file ls-files re-runs, printing counts.
- Tools:
  - the Read tool;
  - git `log`, `show`, `rev-parse`, `hash-object`, `ls-files` and `--version`, with item 3's pathspec plus `':!data/mf3/**'` on every form that takes a pathspec;
  - the system BSD grep, on named files only;
  - `cut`, `fold`, `tr`, `wc` and `test -e`;
  - `gitleaks version`.
- Not done:
  - I did not list the scratch folder, and touched no `*.json` in it.
  - Nothing under `data/` was opened, listed, hashed or searched, and results/raw was not listed.
  - No interpreter ran, and nothing was written.
  - No git status, add, commit, checkout, reset, stash or fetch; no network.
  - No gitleaks scan, and no `--stat` or `--numstat`.
  - No argv held a barred substring.

ITEMS
1. L1 "2026-11-18". CONFIRMED.
   - The six commits of the range, and also 6e3474d and 303953c, all carry commit date 2026-11-18 (git log %cs).
   - push_record9.txt:24: "pushed 2026-11-18".
2. L1 "push #9". CONFIRMED.
   - The C.5 ranges chain unbroken from the 2026-11-15 push `16c99d5..fa27c45` (RESULTS.md:4626–4628), through :4700, :4703, :1516, :1520, :1522 and :936, to :993.
   - :993 is `dc6a1cf..ad856f0`, which 7a54eb9's subject calls "push #8's C.5 line".
   - This range starts at ad856f0, so it is #9.
3. L1 "its one gitleaks halt". CONFIRMED.
   - gl9_final_classified.txt:1–3 shows one finding and one HALT line.
   - push_record9.txt:16 has "gl4 exit=2", and the screen exited 0 (:10).
4. L1–2 "pushed on the PI's "Push, with a note"". CONFIRMED.
   - push_record9.txt:1, :21 and :23.
   - The local origin/main ref equals the full id at :23.
5. L2 "Not a STOP." CONFIRMED, by precedent.
   - Item 4 makes a match inside "a halt for the seat", and C.1 (:45) has the seat clear it "in a line".
   - The 2026-11-16 gitleaks halt went to the seat as a dated note after the PI's "Push, with a note" (RESULTS.md:4623–4640), and C.3 (:47) let that word stand.
   - "Not a STOP." also closes the headings at RESULTS.md:870 and :1496.
6. L3 "`ad856f0..1272702`, 6 commits (`6df2131`, `bfc869f`, `3b2b855`, `7a54eb9`, `f3e7190` and `1272702`)". CONFIRMED.
   - Each commit's one parent (git log %p): 6df2131 ← ad856f0, bfc869f ← 6df2131, 3b2b855 ← bfc869f, 7a54eb9 ← 3b2b855, f3e7190 ← 7a54eb9, 1272702 ← f3e7190.
   - Under the pathspec, ad856f0..origin/main counts 6.
   - screen9_final.txt:1 says "6 commits"; see also push_record9.txt:12 and :23.
7. L4–5, the coordinating session's question. CONFIRMED, verbatim, by push_record9.txt:1 only; chat is not visible here.
8. L5 "the PI answered "Push, with a note" (2026-11-18)". CONFIRMED, by the record.
   - The words are at push_record9.txt:1. The date is the push's, at :24.
   - It is dated plainly, as the earlier C.5 lines date the PI's word (RESULTS.md:936, :993).
9. L5–6 "The push carried `6df2131`'s stage report and cell". CONFIRMED.
   - 6df2131's subject: "Committed by path: … the stage report (data/n/reports/backend-ext.json) and its one cell's JSON …".
   - 6df2131 is the first commit of the pushed range, and origin/main is 1272702.
10. L6–7, §4's words. CONFIRMED, verbatim.
    - Source: the third sitting's answers :32; header :3 ("PI date 2026-11-18 (third sitting)"); routing item 4 at :59.
    - 6df2131's subject names "/data/n/ckpt/** -diff in .gitattributes".
11. L8 "gitleaks 8.30.1, the one on the laptop's path". CONFIRMED.
    - `gitleaks version` printed 8.30.1.
    - push_record9.txt:12: "gitleaks 8.30.1 over ad856f0..1272702".
12. L8–9 "no gitleaks configuration is tracked". CONFIRMED, for `.gitleaks.toml`.
    - `git rev-parse` of `.gitleaks.toml` fails at HEAD, at 1272702 and at ad856f0.
    - `test -e` finds no such file at the repo root.
    - `.gitleaks.toml` is the name gitleaks loads by default from the scanned directory (its documentation as I know it; not a named source). A configuration under any other name would have to be passed, which is item 13.
13. L8–9 "or set", and so "under its default rule set". NOT CHECKABLE.
    - push_record9.txt:12 records only the version, the range and the count. No command line or environment is recorded.
    - The note could say "no configuration was passed, by the coordinating session's account", or the record could carry the command line.
14. L9 "its output does not print its version". NOT CHECKABLE.
    - gitleaks' own output is not among the readable files.
    - The classifier's output prints no version (gl9_final_classified.txt:1–3).
    - The phrase follows RESULTS.md:991–992.
15. L9–10 "`ad856f0..1272702`, 6 commits, on the PI's word "Push, with a note" (2026-11-18)." CONFIRMED (items 6–8).
    - C.5 (:49) asks the line for "its range, the classes matched, the halts, the PI's word", and they are now all in it.
16. L10–11 "The screen (C.2 form) was CLEAR in every class, with nothing matched inside `ckpt` or `reports`." CONFIRMED.
    - screen9_final.txt:2–7: six classes, each "inside: 0 -> CLEAR".
    - push_record9.txt:2 has "screen4.py, C.2 form", and :10 has "screen4 exit=0".
    - "C.2 form" rests on the record, since the screen's source is not among the named files. See observation 7.
17. L11 "gitleaks found one `generic-api-key` match, inside `data/n/reports`: a halt". CONFIRMED.
    - gl9_final_classified.txt:1–3.
    - push_record9.txt:12: "leaks found: 1".
18. L12 "There was no other halt." CONFIRMED.
    - Every screen class was CLEAR and the screen exited 0 (push_record9.txt:3–10).
    - gitleaks had one finding (gl9_final_classified.txt:1) and one HALT line (:3).
19. L13–14 "The screen and gitleaks ran over `ad856f0..7a54eb9` first and again over the whole range before the push, each time with the same one match". CONFIRMED.
    - screen9.txt:1: "RANGE ad856f0..7a54eb9: 4 commits". 7a54eb9 is four commits past ad856f0 and includes 6df2131. Its :2–7 are all CLEAR.
    - gl9_classified.txt:1–3 equals gl9_final_classified.txt:1–3, line for line.
    - screen9_final.txt:1 covers the whole range.
    - The record puts the screen, gitleaks and the helper (push_record9.txt:2–19) before ":23 Pushed".
    - See observation 2.
20. L14 "the re-run C.1 asks to see beside a halt". CONFIRMED, as C.1's words.
    - C.1 :45: "a halt under item 4 is put to the seat with the re-run beside it, whatever the session takes its cause to be". The close line is RESULTS.md:4685–4687.
    - Which run counts as that re-run is the seat's call. See observation 1.
21. L15–16 "C.3, in the seat's answers of 2026-11-16", and its link. CONFIRMED.
    - The header :3: "Design seat, PI date 2026-11-16 (second sitting)". C.3 is at :47.
    - The linked file is tracked and clean at HEAD.
22. L17–18, the C.3 quote. CONFIRMED, verbatim with its backticks (:47).
23. L19 "a 64-hex value". CONFIRMED.
    - gl9_final_classified.txt:2 has 'hex64-other'.
    - gl9x_final.txt:2 has "inside, 64-hex, examined: 1".
    - gl9x.py:26 admits only a full 64-hex secret.
24. L19 "in `data/n/reports/backend-ext.json` at `6df2131`". CONFIRMED.
    - gl9x_final.txt:1: "in data/n/reports at 6df2131".
    - 6df2131's subject names that report as its own, "with .gitignore admits for exactly those two" (the report and the cell).
    - push_record9.txt:21 agrees.
    - The file was not opened.
25. L19–20 "under a key whose name carries no "sha", so it stayed a halt." IMPRECISE (minor).
    - It holds for the key immediately before the value:
      - the classifier classed it 'hex64-other' and halted (gl9_final_classified.txt:2–3);
      - C.3 :47: "any other 64-hex match inside stays a halt";
      - push_record9.txt:24 agrees;
      - the helper's key is that immediate key (gl9x.py:30);
      - none of the eleven imported paths carries "sha" (count 0 over the hashes raw).
    - But by the schema and the helper, the value sits inside `imported_sha256`, whose name does carry "sha" (schema.py:436). So "under a key whose name carries no sha" holds only in the immediate-key sense, which L37–38 later names as the screen's form.
    - Fix: "The match is a 64-hex value in `data/n/reports/backend-ext.json` at `6df2131`, whose key, the one immediately before it (the screen's form of C.3's test; see the reading below), carries no "sha", so it stayed a halt."
26. L21 "A helper of the screen's found that its key is a tracked repository path at that commit, and that its value equals that file's sha256 there." CONFIRMED.
    - gl9x_final.txt:1: "key is a tracked repo path at that commit: yes; secret equals that file's sha256 there: yes".
    - The method is gl9x.py:28–35. Its docstring calls it the "Pre-push screen helper" (:1).
27. L22 "The helper prints the rule's name, the path class, the commit and two yes/no classes, never a value, a key, a path's content or a line." CONFIRMED.
    - gl9x.py:37–39 print an ordinal, the path class (data/<unit>/<dir>), the first 7 characters of the commit, the rule id and the two yes/no classes.
    - :40 prints one count line ("inside, 64-hex, examined"). That is a count with a shape label, which item 4 and C.2 allow.
    - The secret, the key, the line and the blob are never printed.
    - The words "never a value, a key, a path's content or a line" are C.2's (:46).
28. L23–25 "Its yes/no classes go beyond C.2's rule name and shape class: a departure …, as the 2026-11-16 note disclosed its classifier's shape class." IMPRECISE.
    - For a match inside, item 4 with C.2 (:46) permits the count by path class, the rule's name and a shape class.
    - The helper's commit print ("at 6df2131", gl9x_final.txt:1; gl9x.py:37) is also outside that list.
    - The classifier prints no commit (gl9_final_classified.txt:2). Pass 1's item 22 listed the commit among the helper's prints.
    - The precedent clause is correct (RESULTS.md:4649–4650).
    - Fix: "Its commit and its yes/no classes go beyond C.2's rule name and shape class: a departure of the coordinating session's, for the seat to class, as the 2026-11-16 note disclosed its classifier's shape class."
29. L26–27, the schema quote. CONFIRMED, verbatim.
    - schema.py:436, inside STAGE_IDENTITY_FIELDS (:429–460).
    - The blob is the same at 6df2131 and at HEAD.
30. L27 "a module digest keyed by its path". CONFIRMED.
    - guard.py:48–49: "{repo-relative path: sha256} for the given sys.modules snapshot's valence_core modules outside n"; :62: `out[rel] = sha256_file(p)`.
    - schema.py:623–625 define the type path_sha256 as a map from strings to 64-hex values.
31. L28 "The helper prints no key, so which path matched is an inference." CONFIRMED (gl9x.py:37–39).
32. L28–30 "n imports `valence_core.m.keys` (`valence_core/n/keys.py`; `valence_core/n/runner.py`)". CONFIRMED.
    - keys.py:27 "from ..m.keys import stream" and runner.py:66 "from ..m.keys import stream_known_answer", both at module level.
    - Both blobs are the same at 6df2131 and at HEAD.
    - Both modules are in guard.py:31's PRODUCTION list, whose imports the closure measures (:7–10).
33. L29–32 "of the eleven imported modules the hashes raw of `6e3474d` lists (…), only `valence_core/m/keys.py` holds … "key"". CONFIRMED.
    - The raw has 11 imported_sha256 lines (:2–12), and one path holds "key": valence_core/m/keys.py (:10).
    - The raw is present at 6e3474d and absent at its parent. 6e3474d is the only commit that touches it, and its blob is the same at HEAD.
    - The link is tracked and clean.
    - See observations 3 and 4.
34. L32 "generic-api-key's keyword". NOT CHECKABLE from the named sources.
    - No named source gives the rule's keywords. push_record9.txt:21 asserts "generic-api-key fires on a path holding "keys"", and RESULTS.md has no line on it.
    - It is consistent with gitleaks' default rule as I know it (its keywords include "key"), but that rule was not read here.
35. L33 "The third sitting's §4 cleared the screen's halt on `data/n/ckpt/**` only." CONFIRMED.
    - :32: "the pre-push screen's halt on `data/n/ckpt/**` is cleared by this ruling".
    - :59: "the screen's halt on `data/n/ckpt/**` cleared".
    - No other path's halt is named.
36. L33–34 "The PI's word, with this note, carried the push". CONFIRMED.
    - push_record9.txt:21: "HALT disposition: on the PI's "Push, with a note""; the push itself is at :23.
    - §4 :32: "The push itself is the PI's word, as always."
37. L34 "as the PI's "Push, with a note" carried the three matches of C.3's own origin." CONFIRMED.
    - C.3 :47: "The three gitleaks matches … The PI's "Push, with a note" stands as the push's word."
    - See also RESULTS.md:4626 and :4637–4640.
38. L35 "The same class recurs in the resumed report committed at `6e3474d`: one match, with the same helper result." CONFIRMED.
    - gl4_6e3.txt:1–3 has the same tuple, x 1, with HALT.
    - gl9x_6e3.txt:1: "in data/n/reports at 6e3474d", yes and yes.
    - 6e3474d's subject: "the resumed report (…; the cell is unchanged and not committed again)". See also RESULTS.md:105.
39. L36 "That commit is not pushed". CONFIRMED.
    - The local origin/main ref is 1272702 (no fetch was run).
    - origin/main..HEAD lists 303953c and 6e3474d.
    - 6e3474d's subject ends "Not pushed".
    - See observation 8.
40. L36 "and its push needs the PI's word." CONFIRMED.
    - §4 :32: "The push itself is the PI's word, as always."
    - Routing item 8 (:67): "[yours]".
41. L37–38 "The screen's form of C.3's test reads the name of the key immediately before the value". NOT CHECKABLE.
    - The classifier (gl4.py, push_record9.txt:12) is not among the readable files.
    - gl9x.py:30 does read the immediate key, but that is the helper, not the classifier.
    - The claim is consistent with the 'hex64-other' class for a value whose enclosing map (by inference `imported_sha256`) carries "sha". See observation 5.
42. L38 "(C.3's words: "under a key whose name carries `sha`")". CONFIRMED, verbatim (:47).
43. L38–39 "A digest keyed by a repository path that carries no "sha", inside a map whose field does (`imported_sha256`), fails that test." CONFIRMED, under the test as L37–38 state it.
    - The field carries "sha" (schema.py:436), and none of the eleven paths does (count 0).
44. L39–41, the digest class, "so long as the module's bytes at the report's commit equal those hashed at the run; the helper already computes it". CONFIRMED.
    - gl9x.py:30–35 compare the value with the sha256 of the key's blob at the finding's commit. Both findings came out yes and yes (gl9x_final.txt:1, gl9x_6e3.txt:1).
    - guard.py:44–45 and :62 hash the file's bytes at the run, so the stated condition is exactly the gap between the two hashes.
    - For valence_core/m/keys.py the condition holds: its blob is the same at 6df2131 and at HEAD.
45. L41 "Adopting it, or not, is the seat's." CONFIRMED.
    - CLAUDE.md, two-instance workflow: "findings flagged, never silently applied; Code escalates fired gates, never self-adjudicates".
    - C.1 :45: "the seat clears it, in a line".
46. L42 "(`7a54eb9`'s entry gave the `results/raw` case)". CONFIRMED.
    - RESULTS.md:348–356, with the results/raw case at :350–351. 7a54eb9's subject carries the same reading.
    - That entry also found a lone root file and a lone scripts/ file listed (:352). The note's two listed cases repeat that.
47. L42–43 "This note's values-checker found, and Code re-ran at HEAD `303953c` on git 2.39.5, names and counts only". IMPRECISE.
    - Pass 1 (vcn1/report_n1.txt:55, its observation 6) found the case for valence_core/m/gshape.py, in three forms, and generalized it to "any literal path".
    - Pass 1 did not report runner.py or the ruling raw. The note's own result, with two of five files listed, refutes the generalization.
    - Code's re-run is not among the named files, so it is not checkable in itself. HEAD 303953c and git 2.39.5 are confirmed (`git --version`).
    - Fix: "This note's first values-checker found it for `valence_core/m/gshape.py` (it put it as any literal path, which is too wide), and Code re-ran it at HEAD `303953c` on git 2.39.5, names and counts only: …".
48. L43–45, the five results. CONFIRMED, by my re-run at HEAD 303953c on git 2.39.5.
    - With item 3's `':!…'` form plus `':!data/mf3/**'`: gshape.py 0, runner.py 0, scripts/n_sessions.py 1, CLAUDE.md 1, the ruling raw 0.
    - Bare: 1 each.
    - All five files are tracked and clean (rev-parse against hash-object).
    - I did not re-run the other two exclusion forms. See observation 6.
49. L45–46 "So a tracked-and-clean check of any named file takes `git rev-parse HEAD:<path>` against `git hash-object`." CONFIRMED.
    - It follows from item 48 and matches 7a54eb9's entry (:354–355).
    - This check used that form.
50. L48 "Committed by path: this note and its values-check raw. Nothing ran on a model. Not pushed." NOT CHECKABLE: the commit has not been made.
    - gl9x.py imports hashlib, json, re, subprocess and sys, and calls only git (:8–12, :18–19).
    - Nothing in the scratch outputs points to a model run.

PASS 1's IMPRECISE ITEMS AND OBSERVATIONS
- Item 11, the C.5 line's form: applied in pass 1's words (L8–12), with observation 7's rule-set clause added (my items 11–18).
- Item 22, the helper's prints: applied in substance (L21–25). The prints are stated in C.2's words, and the yes/no classes are disclosed as a departure. But the commit, which pass 1 listed among the prints, is left out of the disclosed departure (my item 28).
- Item 33: applied verbatim (L37–38; my items 41–42).
- Item 34: applied verbatim (L38–39; my item 43).
- Observation 3: applied. L24–25 cite the 2026-11-16 precedent.
- Observation 4: applied. L13–14 name both runs, with the same classifier class each time, and offer the second as C.1's re-run. Whether the helper's run counts as that re-run is not addressed (my observation 1).
- Observation 5: applied. L40–41 carry the condition, and "by construction" is gone.
- Observation 6: applied and corrected (L42–46). The five lone-file cases, two of them listed, narrow its "any literal path" and agree with 7a54eb9's entry (:352). Its attribution is my item 47.
- Observation 7: applied (L8–9). Its "or set" half is my item 13.
- Pass 1's suggestion at its item 26, to cite the import, is also applied (L28–32).

OBSERVATIONS
1. Item 20, the re-run.
   - In C.1's origin, the re-runs were of a changed form: the bounded pattern's runs over 16c99d5..97d160a and 16c99d5..fa27c45 (RESULTS.md:4641–4645). They tested the session's account of the cause.
   - Here the second run is the push range's own screen and gitleaks, in the same form, over a larger range that still includes 6df2131. The step that tests the cause is the helper.
   - "Offered as the re-run C.1 asks to see" would leave to the seat which of the two serves.
2. Item 19, the first gitleaks run.
   - Its range rests on the brief: gl9_classified.txt prints no range, while screen9.txt:1 does.
   - No helper output exists for that run. So "the same one match" there means the same class tuple, not a commit shown to be the same.
3. Item 33, which run's closure.
   - The eleven paths are the resume's closure (the hashes raw of 6e3474d).
   - That 6df2131's report holds the same eleven rests on the resume's own checks, not on a record of the first run's closure:
     - imported_sha256 is a stage identity field (schema.py:436);
     - the identity table says a pod change "refuses a resume" (:439–440);
     - both runs report the hashes "equal to the laptop's" (6df2131's subject; RESULTS.md:40);
     - valence_core/m/keys.py's blob is the same at 6df2131 and at HEAD.
   - The note could name the raw as the resume's closure.
4. Items 25, 33, 34 and 43, the eleven paths.
   - None of the eleven paths holds "sha" (count 0).
   - None holds another keyword of generic-api-key's default rule as I know it (access, api, auth, credential, creds, passw, secret, token; count 0). That keyword list is gitleaks', not a named source.
   - So the inference does not rest on "key" alone, and whichever of the eleven is the immediate key, it carries no "sha".
5. Items 25 and 41–44, reading C.3.
   - C.3's "under a key whose name carries `sha`" can also be read by nesting: the value sits inside imported_sha256.
   - Under that reading, C.3 already classes the match as a digest, and only the screen's form would need to change.
   - Under the immediate-key reading a new class is needed, which is what the note proposes.
   - The note's reading puts only the second to the seat. Naming both would leave the seat the whole choice.
6. Items 46–49, a hypothesis for the ls-files behaviour. It is not tested beyond these runs, and I did not read git's source here.
   - On this git, ls-files seems to match each exclusion starting at an offset equal to the length of the positive pathspec's common directory prefix:
     - for 'valence_core/m/' and 'valence_core/n/' (15 characters), ':!data/*/reports/**' would be read from its tail, '**', which matches every name;
     - for 'results/raw/' (12 characters), ':!data/*/ckpt/**' would likewise be read as '**';
     - 'scripts/' (8 characters) leaves no tail that matches 'n_sessions.py';
     - a root file, or a list that includes one (7a54eb9's "beside CLAUDE.md", :352), has no common prefix.
   - That fits all five results here and 7a54eb9's cases.
   - If it holds, which lone files are dropped depends on the length of their directory path. So "any named file" (L45) is the right scope.
   - `git log` under the same pathspec did find the file (:353, and the hashes raw's log here), which fits a different matching path.
7. Item 16, "the screen".
   - At L10, "the screen" means screen4's classes. But L21 ("A helper of the screen's") and L37 ("The screen's form of C.3's test") assign the gitleaks classification to the screen, as C.3 does ("the screen classifies").
   - So L10's "nothing matched inside ckpt or reports" holds for the classes only, right before L11's match inside.
   - The 2026-11-16 note used the same split (RESULTS.md:4630–4640).
   - "The screen's classes (C.2 form) were CLEAR…" would remove the double reading.
8. Item 39, the next push.
   - HEAD 303953c, the child of 6e3474d, is also unpushed (origin/main..HEAD lists both).
   - So the next push runs to HEAD, and its screen and gitleaks run would need to cover 303953c too.
   - This is pass 1's observation 1, not taken up. No claim in the note depends on it.

DEPARTURES (HEAD 303953c throughout, checked at the start and at the end)
1. Git commands without item 3's pathspec, because they take none:
   - `git --version`, which printed the version line;
   - `git rev-parse` of revisions:
     - `--short HEAD origin/main`, which errored ("Needed a single revision");
     - then `--short HEAD` and `--short origin/main`;
     - and the full origin/main id, compared in the shell with the record's.
   - Together these printed two short ids and one equality line.
   - The `git rev-parse <rev>:<path>` and `git hash-object` forms that the brief names printed only status lines.
2. Reads beyond the brief's repo sources, all inside the repo and none under `data/`:
   - `git hash-object valence_core/m/keys.py`, and that file's blob ids at 6df2131 and HEAD compared in the shell; status lines only;
   - RESULTS.md beyond the brief's three spots:
     - :1–115 (6e3474d's entry);
     - :300–424 (7a54eb9's entry, around its tooling reading);
     - greps of RESULTS.md for "generic-api-key", "keyword", "bext-resume4_hashes", "hashes equal", "which `6df2131`" and "Not a STOP", printing line numbers and the first 200–220 characters of each hit;
   - for completeness: `git show 6df2131:` of four named sources (n/keys.py, n/runner.py, n/schema.py, n/guard.py), each piped to a one-line grep, which the brief's blob rule allows.
3. Disclosed as the brief asks: the lone-file `git ls-files` re-runs.
   - Five named files, each run with item 3's `':!…'` exclusions plus `':!data/mf3/**'`, and each run bare.
   - Each printed the name passed and two counts.
4. `gitleaks version`, as the brief allows. It printed only "8.30.1".

TOTALS: 50 items: 42 CONFIRMED, 3 IMPRECISE (25, 28, 47), 0 FAIL (none), 5 NOT CHECKABLE (13, 14, 34, 41, 50), and 8 observations.

## 4. Pass 2: dispositions

**The three IMPRECISE items, each applied:**
- 25: the key is the one immediately before the value, in the screen's form of C.3's test.
- 28: the helper's commit is named with its yes/no classes as the departure.
- 47: the first checker found it for `valence_core/m/gshape.py`, and its "any literal path" was too wide.

**The observations:**
- applied: 1 (the re-run offered, with which of the two serves left to the seat); 3 (the eleven paths are the
  resume's closure); 5 (both readings of C.3 set out for the seat); 7 ("The screen's classes");
- recorded here: 2 (the first run had no helper output, so "the same class"); 4 (no other keyword among the eleven
  paths, by the checker's own knowledge of the rule); 6 (the checker's untested reading of the `ls-files` behaviour,
  an exclusion matched from an offset equal to the common directory prefix's length); 8 (the next push covers
  `303953c` too).

Item 13's "or set" is supported in the note by the command and the environment: the command passed no configuration,
and `GITLEAKS_CONFIG` was unset (checked by the coordinating session).

**The checker's departures**, as its report states them, for the seat to class:
- git commands that take no pathspec;
- reads beyond its named sources, none under `data/`;
- the `ls-files` re-runs the brief allowed, with and without the exclusions;
- `gitleaks version`.

**The edits after pass 2** were checked by tool: each new text found once in the draft.
