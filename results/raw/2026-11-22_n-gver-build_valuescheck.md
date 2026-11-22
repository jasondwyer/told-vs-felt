# n — G-VER of record's BUILD texts: the blind values-check, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three drafts, at HEAD `9b71bbb`:
- T1, this commit's entry, sha256 `932176f5…db49` (193 lines), its values-check, checker's-departures and final-sweep
  lines placeholders not to be checked;
- T2, the review raw, `f4aed6ff…2640` (285 lines): its head with every disposition, and the review's report appended;
- T3, the self-test raw, `b6c396d9…6723` (69 lines).

**The checker's brief** was given to the checker as its prompt: Code's scratch file `S/step4b/gver/build/vc_brief.md`
(`8b6e3900…8ecb`, 142 lines). It:
- named the texts and the sources. In the repository, the files the texts cite, at `9b71bbb`, each checked tracked and
  clean. In Code's scratch, by name and sha256 only: the four drivers (drafts 1–3 and HEAD's copy), the three deltas,
  the three `.gitignore` files, the review's brief and report, the nine self-test run files, the overlay's recipe, the
  package-digest script and the two sweep records;
- allowed `shasum` by name, and `jq` on the two sweep records, on this session's transcript and on committed JSON
  outside `data/*/ckpt`, `data/*/reports` and `data/m[f]3`. The transcript was for a sweep of Code's shell commands in
  two spans: the BUILD's 20 commands before `d92500b`'s window, and from that window to the brief's own hash. The brief
  warned that a span's bound must be a timestamp prefix, since "…15:55:10Z" sorts after "…15:55:10.138Z";
- barred any other interpreter, any write, any network, and any guard marker in an argv: a path, a grep pattern, a
  variable or glob that expands to one (an unquoted bracketed pattern among them), a loop that passes one, and the
  command's own text;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, and anything in Code's scratch but the named files;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (219 lines, sha256
`bd7b0ab6…1b2f`). It names scratch files only by their paths inside the scratch folder, and the transcript as T.

**Totals:** 121 items: 95 CONFIRMED, 12 IMPRECISE, 1 FAIL, 13 NOT CHECKABLE; and 16 observations. Code counted them
again by tool, from the first verdict on each item's line.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words or the words below. Every observation is
applied or met. §2 gives the edits and their check by tool.

- **Item 111 (FAIL), T3:45–47.** Applied in the checker's words: F1-F4, F6-F9 and F11 in the driver and its
  self-test, and F10 in the `.gitignore`'s second draft.
- **Items 31 (T1:57) and 67 (T2:37–38).** Applied in the checker's words: the same correction for F10.
- **Item 7, T1:27–28, with observation 4.** Applied in the checker's words: GV12's two durations, marked a lower
  bound (F11).
- **Item 34, T1:63–65, with observation 5.** Applied in the checker's words. One sentence is added for GV5: its "This
  keeps 2 for G-VER's STOP alone" holds for `run_gver`'s own ends, and the supplement's §1.6 gives the process's other
  exits 2.
- **Items 41, 46, 49 and 52, T1's departures list.** Applied: every kind the checker found missing is listed, in its
  words or near them, and the loose items are worded as it put them. Item 46's diff line adds "through `sed -n` of
  its range", where the counts of the self-test's calls ran.
- **Item 54, T1:173–174.** Applied in the checker's words.
- **Item 69, T2:43.** Applied in the checker's words.
- **Item 82, T2:97–98.** Applied in the checker's words.
- **Item 100, T3:26–27.** Applied in the checker's words.
- **O1.** Applied: the entry's "throughout" line names the three runs' `cd jl*/.venv/bin`, the form `1641948`
  declared and the seat classed inert (RESULTS.md:2675–2676).
- **O2.** Applied: the BUILD's 20 commands' list names the file-reading tool's read of the model manifest.
- **O3.** Applied: "one docstring (two lines)" in T1 and T2.
- **O4.** Applied with item 7.
- **O5.** Applied with item 34.
- **O6.** Applied: "F5 and B5" in the entry's launch-files line.
- **O7.** Applied: "will" for the launch files in T2's F5, F11 and B3.
- **O8.** Applied: "two commands, three `/usr/bin/grep` runs".
- **O9.** Applied: the entry says the stream held every tracked name under `data/`, the ckpt and reports folders'
  included. It no longer says whether any name under Q-F3's folder is tracked, which Code cannot list.
- **O10.** Applied: "no record written".
- **O11.** Applied: T2's account of the review's brief adds "and the brief itself".
- **O12.** Met: the kit's scripts ran in the forms `d92500b`'s entry declared for `7d01b02`'s window, and the entry now
  says so for both windows. The edits' and the rewrap's check scripts are named with their tools.
- **O13.** Met: the entry's final sweep lists the commands after the checker's window.
- **O14.** Applied: T1 and T3 say that the request, the grant and the ruling are outside the repository, and where:
  Code's note (`634f7181…be88`) and the coordinating session's messages.
- **O15.** Applied: T1:21 adds "while MANIFEST.json passes `ids.load` (the supplement's §1.3)".
- **O16.** Applied: T3 says that G-TIME-n's launch recorded 645 on the box, against its BUILD's 634 on the laptop.

**Beside the checker's items, edits of Code's own:** line rewraps that the edits needed, whitespace only, in T2's head
and in T3; and in T1, the edit count's placeholder moved to the start of a line, so that the filled line stays within
120 characters.

## 2. The edits, checked by tool

The edits were made to new versioned copies of the three drafts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/gver/build/edits_check.sh`. The results are byte for byte the revised drafts, so nothing else changed after
the check:
- the entry, 21 of 21 edits; the review raw, 9 of 9; the self-test raw, 6 of 6.

The entry's 21 include its three placeholders, filled with this check's summary, the checker's departures and the
final sweep. After the edits, one placeholder was filled by tool: the entry's count of these edits.

## 3. The report, as returned

```text
BLIND VALUES-CHECK: G-VER of record's BUILD texts (T1 entry, T2 review raw, T3 self-test raw)

Setup: HEAD is 9b71bbb. All 28 named S files are at the brief's sha256s, with the stated line counts. Every repository source I used is tracked and clean at HEAD (rev-parse equals hash-object). T2's lines 122–285 hash to 3bb14a39…411d and are byte-identical (cmp) to S/step4b/gver/review_report.md.

ITEMS

T1 (S/step4b/gver/build/entry_src.md)
1. T1:1–3. The title: the gver command, n v0.2 §8 step 12, GV1–GV16 as PINs, "Build on the PINs", the driver alone, the package at LOCK-n v0.1's digest, "Not run." CONFIRMED. The quote is at RESULTS.md:93 and results/raw/2026-11-22_n-gver_spec.md:248. The delta touches only the driver. No command in T runs `n_sessions.py gver`.
2. T1:4. valence_core/n stays at 06b55761…1d39 (L §18). CONFIRMED. L:781 is in §18 (§18 starts at L:776). valence_core/n last changed at ef105f1. The shell digest over HEAD's clean files at 17:33:56Z is 06b55761…1d39.
3. T1:5–6. gver runs run_gver; no weights load and nothing is read; building the provenance makes a CUDA context. CONFIRMED. cmd_gver→run_gver is at S/step4b/gver/draft3/delta_from_head.diff:444–445. These are the STAGE line's own words (delta:343–344). environment_provenance calls torch.cuda.get_device_name(0) (scripts/n_sessions.py:694).
4. T1:6–19. The ten refusals, exit 1, a REFUSED line, no record, "in this order". CONFIRMED. _gver_prepare (delta:325–391) checks, in order: the record; the pod; cuBLAS; weights; driver; LOCK-n.md; sessions and ids through _gver_loaded; the R6 bridge and n's identifier; tokenizers against LOCK_TOKENIZERS; the package and closure; then gver_tokenizer_files. run_gver prints the REFUSED line and returns 1 (delta:404–410). The closure is twelve files (drv:3777; L:796), and tokenizers 0.22.2 is at L:767–768. ids.TOKENIZER_FILES names three files (ids.py:69).
5. T1:21–22. MANIFEST.json's sha256 is printed beside the pin and left to G-VER (L:543; GV4's correction). CONFIRMED. See delta:360–362. L:543 lists "the manifest's pin" among G-VER's causes, and B:134–139 has the correction.
6. T1:22–26. G-VER itself (local files only, to decode only, each step timed); the record n-gver-v1, checked, written once and checked on disk; a failed write leaves no record (F1); exits 0, 2 and 1; no option, no smoke. CONFIRMED. See delta:285–287, 412–441, 229–261 and 1018–1029.
7. T1:27–28. "The driver's docstring lists GV1–GV16 in short as its PINs, as sent but for GV4's pins, which are as built." IMPRECISE. GV12's line also changed: "(a lower bound)" (delta:51; spec raw:173–175 lacks it). Put instead: "…as sent but for GV4's pins, which are as built, and GV12's two durations, marked a lower bound (F11)."
8. T1:28–29. The seven are with the seat in d92500b's block (Q1–Q7), and the supplement 9b71bbb adds clauses to Q2, Q4 and Q6 plus its §1.6. CONFIRMED. See the supplement raw §1.6 (:117–130) and §2 (:132–143).
9. T1:29. "G-VER runs only after the seat's answers." NOT CHECKABLE (a plan). It is consistent with B:271–272 and supplement:21–22.
10. T1:30. Draft 3 is 8df113e4…3f02, 6,195 lines, +990 −3 from HEAD's 4616f9c3…2553. CONFIRMED: shasum, wc -l, and `git diff --no-index --shortstat` gives 990 insertions and 3 deletions.
11. T1:30–32. Draft 3 is draft 2 with one docstring line corrected (observation 6). CONFIRMED. See delta_from_draft2.diff:5–15 and supplement values-check raw:278. See observation 3.
12. T1:33. The .gitignore gains +7 lines; its second draft is 81f5f227…b610. CONFIRMED: the diff from base to v2 is 7 insertions, 0 deletions.
13. T1:34. Only gver.json is admitted, and the temporary stays ignored. CONFIRMED. The rules are `!/data/n/gver/`, `/data/n/gver/*` and `!/data/n/gver/gver.json`. The temp name is name + ".tmp" (valence_core/m/resume.py:221).
14. T1:35–36. The review read v1 (2e105c34…d8a8), whose comment presupposed Q1 and Q5 (F10); v2's comment does not. CONFIRMED. v1's comment has "is the gate LOCK-n v1.0 and the campaign follow"; v2 drops it.
15. T1:37–39. Dry-run adds, each in its own throwaway repository: only the record and G-TIME-n's artifact were added. CONFIRMED. T's outputs at 15:25:10Z and 16:28:15Z each add only .gitignore, data/n/gtime/gtime.json and data/n/gver/gver.json out of the five test files.
16. T1:40 and T1:53–54. The links to the self-test and review raws. NOT CHECKABLE: neither is placed yet. Both match the names the brief gives.
17. T1:41. Draft 1 printed "687/687 n selftest checks pass", which is HEAD's 634 plus 53. CONFIRMED. See S/step4b/gver/selftest_run1.txt and RESULTS.md:1606 (634/634). Draft 1's _gver_selftest has 27 single checks, 20 tampers and 5 argv cases (52), plus cmd_selftest's environment check.
18. T1:41–42. The window request expected 688; the box's figure was 699. NOT CHECKABLE: the request is not in the repository or the named S files.
19. T1:42–43. The wrapper check "ran to its end" is appended only on a raise. CONFIRMED (delta:65–70).
20. T1:43. "the coordinating session's grant confirmed 54 too." NOT CHECKABLE.
21. T1:43–44. "on the coordinating session's ruling as the window's grantor." NOT CHECKABLE.
22. T1:44. No re-run, and the box's figure for draft 1 was 698. CONFIRMED. T holds one overlay1 self-test (15:29:15Z). 645 (results/raw/2026-11-21_n-gtime-v1_out.txt:76) + 53 = 698.
23. T1:45–46. Draft 2 is 3df537d6…83c1, 6,195 lines, "716/716", 29 checks more. CONFIRMED. The 29 are 15 new tampers (delta_from_draft1.diff:207–221), 8 new argv cases (:477–490) and 6 single checks.
24. T1:47. Draft 3 printed "716/716"; its one docstring change is read by no check. CONFIRMED. selftest_run3.txt matches. Draft 3's only `__doc__` reads are of keys' docstring (:4606) and the module's first line (:6063).
25. T1:48. Each run had exit 0 and an empty stderr. CONFIRMED: the three .exit files hold "exit 0" and the three .err files are empty (e3b0c442…b855).
26. T1:48. "in a battery window the coordinating session granted for its bytes." NOT CHECKABLE.
27. T1:48–50. The temporary folder was empty before and after each run, and PID 8051 was the only Python process. CONFIRMED. T's outputs at 15:23:22Z, 15:29:42Z, 16:28:35Z, 16:34:37Z, 17:25:23Z and 17:28:12Z show it, and RESULTS.md:1103 identifies PID 8051 as Q-F3's campaign.
28. T1:50. Run 3 ran as a background task and was waited on by its exit notice. CONFIRMED. sweep_build.jsonl:88 has bg true. T has a task notice at 17:28:06Z, and the next command, at 17:28:12Z, reads run 3's files.
29. T1:51. The box count is 727. CONFIRMED: 716 + 11. hftiny's 12 box checks (hftiny.py:71–124) plus the driver's 2 (drv:1597, :3720) make 14, against 3 skip lines (hftiny.py:56; drv:1601, :3738).
30. T1:55–56. One BUG; 11 findings (1 BUG, 6 RISK, 4 NIT); 17 mutants; 8 box risks; 7 observations; one departure. CONFIRMED (the report).
31. T1:57. "drafts 2 and 3 build in F1–F4 and F6–F11…" IMPRECISE. F10 is the .gitignore comment and nothing in the drafts: draft 3 has no "gitignore", and supplement:19–20 says "F10 the `.gitignore`'s". Put instead: "drafts 2 and 3 build in F1–F4, F6–F9 and F11, a kill for every mutant by Code's reading, and B2, and the `.gitignore`'s second draft F10;"
32. T1:58–59. F3, F4, O3, O5 and B7 are in the supplement 9b71bbb, on the coordinating session's routing, with F5 as its §1.6. CONFIRMED. See supplement:17–18 and §1.1–§1.6, and RESULTS.md:33–37.
33. T1:61. Nothing ran on a model. CONFIRMED. On the laptop the HF cases are skipped (634 is the laptop's count), and no gver run appears in T.
34. T1:63–65. The nine unstarred readings are "built as the spec raw's §1 has them, but for GV3's tokenizer check, held as GV4's pins are". IMPRECISE. GV3's hash check is unchanged; what changed is GV3's environment (tokenizers 0.22.2, spec raw:96–98) and GV12's wording. Put instead: "…are built as the spec raw's §1 has them, but for GV3's environment, whose tokenizers 0.22.2 is now held as one of GV4's pins (below), and GV12's two durations, now called a lower bound of the pod time (F11)."
35. T1:66–68. GV4 as built, with numpy's known answer not held. CONFIRMED (delta:39–42 and _gver_prepare; supplement §1.1–§1.2).
36. T1:69–71. vocab.json, merges.txt and config.json are covered by byte counts and respawn step (i); Q2 and §1.4. CONFIRMED. check_weights_folder is at drv:636–649. The instruct entry of data/[o]lmo/manifest.json lists all three among its 22 files. Supplement:89–105 covers §1.4.
37. T1:72–73. F2: G-TIME-n has the same pattern, exit 1 rather than GT6's 2. CONFIRMED. _gtime_prepare calls its loaders unguarded (drv:4254–4255), and run_gtime refuses with exit 2. sessions.py raises ValueError (:109, :112, :128, :135–146).
38. T1:74–76. B7. CONFIRMED. check_gver's pins block holds CHARACTERIZED_* (delta:197–203); see supplement §1.5.
39. T1:77–81. The items carried to the launch files. NOT CHECKABLE (plans). They match the report's F5, B3, B6, B8 and F11; see observation 6.
40. T1:83–87. The sweep's scope: 109 commands from d92500b's window to the sweep's record, and the BUILD's 20 left by d92500b's entry. CONFIRMED. My jq gives 109 commands from 15:55:10.138Z to 17:37:35Z, equal to sweep_build.jsonl by cmp; and 20 commands in 15:08:36–15:29:58Z, equal to sweep_tail.jsonl:2–21 by cmp. Span B up to the brief's hash (17:39:37Z) holds 111 commands. The final sweep is a plan.
41. T1:85. "after it the texts' and the values-check brief's hashes." IMPRECISE. Two kinds are not named:
    - 17:38:00Z: line-width, placeholder and non-ASCII counts over the entry and the self-test raw, and `git rev-parse HEAD`.
    - 17:39:37Z: `diff` of the brief's last five lines against the seat brief's lines 106–110 (tail, sed -n, process substitution), and a line-width count over the brief.

    Put instead: "and after it the texts' and the values-check brief's hashes, with line-width, placeholder and non-ASCII counts over the texts and a `diff` of the brief's list of record against the seat brief's;"
42. T1:88–93. The first barred form. CONFIRMED.
    - At 17:01:34Z, T's output is only names under the model folder, then "porcelain done".
    - data/ holds a folder named exactly by the bracketed pattern (count 1), so zsh's glob matched and git's argv held the path.
    - `ps` at 17:01:57Z shows PID 8051.

    See observation 9 on Q-F3's names.
43. T1:94–96. The globs matched 18, 88, 65 and 7 names, none holding a marker. CONFIRMED.
    - Now, `ls results/raw | /usr/bin/grep -cE` gives 20, 88, 65 and 7.
    - Two of the first glob's 20 were added by 9b71bbb (git show --name-only), after 17:00:55Z, so it matched 18 when the command ran.
    - 0 names hold a marker. Code's check at 17:31:33Z printed the same.
44. T1:97–101. d92500b's commit window and its done report's checks. CONFIRMED (sweep_build.jsonl:1–7).
45. T1:102. d92500b's entry counted 21, but sweep_tail lines 2–21 are 20. CONFIRMED. RESULTS.md:186–187 says "30 commands, 21 of them the BUILD's", and lines 222–223 leave the BUILD's commands to this entry.
46. T1:103–113. The BUILD's 20 commands. IMPRECISE: one kind is missing, and two are named only loosely.
    - Missing: 15:23:51Z, `shasum` and `wc -l` of the draft-1 window request's note in the sessions' notes folder.
    - Loose: 15:22:23Z and 15:29:58Z, `sed -n` of draft 1's self-test range into `/usr/bin/grep -c`/`-n` (counts of chk calls and tampers).
    - Loose: 15:23:22Z, `git diff --no-index` in its default form, with `/usr/bin/grep -c` counts of the delta's lines.

    Add: "the window request's hashes (`shasum` and `wc -l` of the note);". Write the diff item as "`git diff --no-index` (its default form, `--stat`, `--shortstat` and `-U1`), with `/usr/bin/grep -c` counts of the delta's lines and of the self-test's `chk(` calls and tampers,".
47. T1:114–116. The review's commands. CONFIRMED (sweep_build.jsonl:8–10).
48. T1:117–124. Draft 2's commands. CONFIRMED. See sweep_build.jsonl:11–19 and 27–28; the four tails grepped are 3bb14a39, f8cdbccb, 88d9fe7b and 06b55761.
49. T1:125–145. The supplement's commands. IMPRECISE. Not covered:
    - 16:33:16Z: `shasum` and `wc -l` of the supplement values-checker's brief.
    - 17:04:24Z and 17:04:30Z: `sed -n` prints of d92500b's committed values-check raw (lines 1–100), with a `/usr/bin/grep -n` of its headings; and `sed -n '1,30p'` of the supplement checker's brief.
    - 17:04:42Z and 17:05:00Z: `cat` of the seat folder's edits-check script and commit-build script, and of its edits list into `head -30`.
    - 17:08:15Z: `/usr/bin/grep -n` over ids.py and HEAD's driver.
    - 17:08:44Z: `bash` of the supplement's edits-check script, with item and verdict counts over the saved report (`/usr/bin/grep`, `sed`, `sort`, `uniq -c`).
    - 17:15:15Z: `/usr/bin/grep -n` over the memory index, a fourth named memory file.
    - 17:19:15Z: `sed -n` of RESULTS.md's d92500b entry into `/usr/bin/grep` counts, and two `while read` length loops.

    Two wordings are also off: `wc -l` ran on two of the three tokenizer files (17:01:33Z), and the memory files grepped are four, not "three named notes".

    Put instead:
    - "the values-checker's brief's hash, its id appended to the gate's list, and `jq` over its transcript to take its report from its hand-back, with a count of local roots and ids over it;"
    - "`sed -n` prints of the driver, `ids.py`, the answers raw (ans21b), `LOCK-n.md`, the block, `d92500b`'s values-check raw, draft 2, the review and the values-checker's brief;"
    - "`/usr/bin/grep` over committed raws (the globs above), over `ids.py` and the driver, and over memory notes: one recursive `/usr/bin/grep -l` over the memory folder, by its path alone, three named notes and the memory index;"
    - "a name-only `ls` of the scratch folder and of the renders' tokenizer folder, `shasum` of its three files and `wc -l` of two;"
    - and add: "`cat` of the seat folder's edits-check and commit-build scripts and of its edits list (into `head`); `bash` of the edits' replay script, with item and verdict counts over the saved report (`/usr/bin/grep`, `sed`, `sort`, `uniq -c`); `sed -n` of `RESULTS.md`'s `d92500b` entry into `/usr/bin/grep` counts, and two `while read` loops of line lengths over it and the commit's entry draft;"
50. T1:146–147. The file-reading tool read the model manifest and the renders' tokenizer_config.json. CONFIRMED (T: Read calls at 17:01:58Z and 17:02:04Z). See observation 2.
51. T1:148–151. 9b71bbb's six steps and the done report's checks. CONFIRMED (sweep_build.jsonl:71–77).
52. T1:152–160. Draft 3's commands. IMPRECISE. Not covered:
    - 17:25:46Z: `/usr/bin/grep -c`/`-n` over draft 3 for `__doc__`, `getsource` and `inspect.`, `wc -l` of the two deltas, and line-width counts over draft 3 and HEAD's copy.
    - 17:24:43Z: a `while read` loop of line lengths over two lines of draft 3.

    Add: "`/usr/bin/grep` over draft 3 (for `__doc__`, `getsource` and `inspect.`), `wc -l` of the two deltas, and line-width counts over draft 3 and HEAD's copy, one by a `while read` loop;"
53. T1:161–172. This entry's texts and sweep, including the first run's bad bound. CONFIRMED. The bound "…15:55:10Z" at 17:30:14Z returned 93 commands starting at 15:55:14Z; the command was then re-run at 17:30:28Z and 17:37:35Z.
54. T1:173–174. "writes in scratch alone … beside the two commit windows' index and commit writes in the repository". IMPRECISE. The place script also wrote working-tree files: it "Places a commit's files … and splices its entry into RESULTS.md", per its head as printed at 17:10:19Z. Put instead: "…beside the two commit windows' writes in the repository (the place script's files and `RESULTS.md`'s entry, the index and the commit);"
55. T1:177. The bracketed count of marker words and the campaign's plain name is 0. CONFIRMED by my bracketed counts: 0 marker words and 0 plain campaign names, in span A's 20 commands and in span B's 111.
56. T1:178. Globs and loops were checked; apart from the first item, no marker reached an argv. CONFIRMED.
    - Globs that expanded to marker-named paths: `data/[o]lmo` (declared) and `jl*` (passed to zsh's builtin cd; no process argv held it; see observation 1).
    - No loop or variable passed a marker-named path.
57. T1:178–179. Nothing under ckpt, reports or Q-F3's folder was read, sized or timed. CONFIRMED. The only exposure is `git ls-files data` streaming names into the pipe, which item 42 declares; the recipe's `git archive` carries the exclusions (recipe:13–18).
58. T1:180–181. The reviewer's departure (the glob). CONFIRMED. See report:277. valence_core/n has 16 .py names, none holding a marker.
59. T1:183. The supplement values-checker's departures are in 9b71bbb's entry. CONFIRMED (RESULTS.md:63–72).
60. T1:184–192. The gate, the paths committed, the digest at the commit, the home-folder count, not pushed, what follows. NOT CHECKABLE (plans). 06b55761…1d39 is the current digest.

T2 (S/step4b/gver/build/review_raw_src.md)
61. T2:5–7. What was reviewed (d92500b; the driver's and .gitignore's hashes; 6,031 lines). CONFIRMED (brief:7–18).
62. T2:9. Draft 1 passed 687/687. CONFIRMED; the window part is not checkable.
63. T2:11–12. The brief was given as the prompt (d9ad5c96…9411, 102 lines). CONFIRMED: the review Agent call's prompt in T (15:57:55Z) plus a final newline hashes to d9ad5c96…9411.
64. T2:13–22. The brief's contents, eight known items, and items 1–5 quoted verbatim. CONFIRMED. See brief:25–60, 62–74 and 78–102. Items 1–5 are byte-identical to results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md:18–22. See observation 11.
65. T2:24–26. The report was taken by jq from the hand-back (164 lines) and names only S/ paths. CONFIRMED. The extraction is T at 16:20:16Z; 0 local roots; the only S paths are the two named files.
66. T2:28–34. "In sum". CONFIRMED.
67. T2:37–38. "Draft 2 … builds in F1–F4 and F6–F11 …" IMPRECISE: F10 is the .gitignore's, and T2:89 says so itself. Put instead: "Draft 2 (`3df537d6…83c1`, 6,195 lines) builds in F1–F4, F6–F9 and F11, a kill for every mutant (by Code's reading of each case, not by a mutation run), and B2; F10 is in the `.gitignore`'s second draft."
68. T2:39–41. Draft 3. CONFIRMED (delta_from_draft2.diff; supplement values-check raw:278).
69. T2:43. "F5 and the other box risks are carried to the launch files or declared." IMPRECISE. F5 is a finding, not a box risk, and B2 is applied in the driver (delta_from_draft1.diff:179–199). Put instead: "F5 is carried to the launch files. Of the box risks, B2 is applied in the driver, B3, B5, B6 and B8 go to the launch files, and B1, B4 and B7 are agreed, noted or declared."
70. T2:43–46. The five items in the supplement, and F5 as its §1.6 on that supplement's values-check. CONFIRMED (supplement:17–18; supplement values-check raw:142–146 and :268).
71. T2:50–53. F1. CONFIRMED (delta:229–261; resume.py:229–235 calls _fsync_dir after os.replace; the case is at delta:650–663).
72. T2:54–59. F2. CONFIRMED (delta:313–322, 358–359, 802–809; drv:4254–4255).
73. T2:60–62. F3: G-TIME-n's check by name is placed after the pod check and before STAGE; B:141–142; §1.1. CONFIRMED (delta:341–342; drv:4230–4231).
74. T2:63–66. F4 (L:767–768) is held in two places; §1.2 with Q2; draft 3's docstring. CONFIRMED (delta:94, 206, 371–372).
75. T2:67–71. F5: values-check item 12 and observation 1; §1.6. CONFIRMED. The launch-file clause is a plan (observation 7).
76. T2:72–78. F6, mutants M12–M15. CONFIRMED (delta:873–922, 950).
77. T2:79–86. F7: the six "at status" tampers, the verify, pins, environment and durations tampers, and the zero-count STOP. CONFIRMED (delta:594–608, 617–621, 769–773).
78. T2:87–88. F8 and F9. CONFIRMED (delta:645–649, 429).
79. T2:89–90. F10 is applied in v2 (81f5f227…b610). CONFIRMED.
80. T2:91–92. F11 wording. CONFIRMED (delta:91–93, 433–434). The launch clause is a plan.
81. T2:93–96. Kills for M1–M17, including all thirteen options (11 plus --bench-dir and --gcal-dir). CONFIRMED. main's options other than --selftest are those 13 (drv:5093–5105); the ": equal" assert is at delta:757.
82. T2:97–98. "No self-test case reaches a production loader…" IMPRECISE. F6's case calls the production `_gver_load_tokenizer` behind a stand-in for transformers (delta:896–915). Put instead: "B1, agreed. No self-test case loads a tokenizer or weights or writes the record's path, on the box after the commit too: the one case that calls the production tokenizer loader (F6) does so behind a stand-in for `transformers` that loads nothing."
83. T2:99–100. B2. CONFIRMED (delta:519–537).
84. T2:101–102. B3: the check by name, the twelve-file closure, exit 1. CONFIRMED. The export clause is a plan.
85. T2:103–104. B4. CONFIRMED (drv:636–649; the manifest's instruct entry; supplement §1.4).
86. T2:105–107. B5, B6 and B8 carried to the launch files. NOT CHECKABLE (plans). G-TIME-n's copy at 91f0d35 is recorded at RESULTS.md:656.
87. T2:108–109. B7. CONFIRMED (supplement §1.5).
88. T2:110–112. O1–O4. CONFIRMED (the report; supplement §1.3).
89. T2:113–114. O5: the pinned tokenizer_config.json names "GPT2Tokenizer". CONFIRMED.
    - T's file-reading result at 17:02:04Z holds that line (its line 188).
    - At 17:01:33Z the three files hash to L:201–203 and data/[o]lmo/manifest.json:252/256/260.
    - The renders used <scratch>/tok_n (results/raw/2026-11-16_n-ids_render.md:17).
90. T2:115–116. O6 (698; 727) and O7. CONFIRMED (delta:16).
91. T2:117–118. The reviewer's departure is declared in the entry. CONFIRMED (T1:180–181).
92. T2:122–285. The report verbatim. CONFIRMED (shasum and cmp).

T3 (S/step4b/gver/build/selftest_src.txt)
93. T3:4–5. The driver has the same bytes at cd6b30d, d92500b and 9b71bbb; 4616f9c3… (+990 −3). CONFIRMED: all three hold blob b00f96eb…, and the driver last changed at 91f0d35.
94. T3:6. The .gitignore lines do not enter the self-test. CONFIRMED: the overlay paths (recipe:13–16) hold no .gitignore, and draft 3 never names it.
95. T3:7–11. The package digest is L §18's, computed by shell in package_sha256_of's form over the three overlays and HEAD's files; the self-test checks it in-process (G-TIME-n's check). CONFIRMED.
    - The form: pkgsha.sh matches resume.py:328–350.
    - The values: T's outputs at 15:23:01Z, 16:28:35Z, 17:25:09Z and 17:33:56Z.
    - The in-process check: drv:4561–4566.
96. T3:13–16. HF cases are skipped and counted; the schema module is one aggregated line; G-VER's cases need neither library. CONFIRMED (hftiny.py:27–33, 56; drv:1601, 3738, 303–304; delta:896–915).
97. T3:17–21. The overlays: archives of cd6b30d, d92500b and 9b71bbb, 174 files each, recipe f8cdbccb…, G-TIME-n's v2 recipe unchanged, and overlay3 differs from overlay2 in the driver alone. CONFIRMED.
    - The file counts and recipe hash are in T's outputs at 15:23:01Z, 16:28:35Z and 17:25:09Z.
    - "recipe equal to gtime v2's" is printed at 15:23:01Z.
    - `diff -rq` at 17:25:23Z shows only the driver differs.
98. T3:22–25. The command form. CONFIRMED (sweep_tail.jsonl:19; sweep_build.jsonl:27, 88).
99. T3:26. Battery windows were granted for each run's bytes. NOT CHECKABLE.
100. T3:26–27. "…the driver in the overlay was at the grant's sha256, the temporary folder was empty and no run's output file existed." IMPRECISE. Run 1's output files existed before runs 2 and 3; the checks were for each run's own files (16:28:35Z checks only `selftest_run2`). The grant's text is not checkable; the drafts' hashes were checked at 15:23:22Z, 16:28:35Z and 17:26:13Z. Put instead: "Before it, the driver in the overlay was at the draft's sha256, the one the grant named, the temporary folder was empty and none of the run's own output files existed."
101. T3:27–28. The state after each run. CONFIRMED.
102. T3:29–30. Run 3 in the background, waited on by its exit notice. CONFIRMED.
103. T3:32–36. Run 1's bytes and output, indented by five spaces. CONFIRMED: line 36 minus five spaces equals selftest_run1.txt (cmp).
104. T3:37. 634 + 53 (52 + 1). CONFIRMED.
105. T3:37–38. 688 and 699. NOT CHECKABLE.
106. T3:38–39. The wrapper check is appended only on a raise. CONFIRMED.
107. T3:39–41. The grant's 54 and the grantor's ruling. NOT CHECKABLE.
108. T3:41. No re-run; 698. CONFIRMED.
109. T3:43–44. Run 2: overlay2 from d92500b, 3df537d6…. CONFIRMED (T at 16:28:35Z).
110. T3:45. Draft 2 is draft 1 +231 −67. CONFIRMED (shortstat).
111. T3:45–47. "F1-F4 and F6-F11 in the driver and its self-test". FAIL. F10 is in the .gitignore's second draft, as T2:89–90 (the review raw's §1, which T3 cites) states; neither draft holds the F10 text, and draft 3 never names the .gitignore. Put instead: "F1-F4, F6-F9 and F11 in the driver and its self-test (F10 is in the .gitignore's second draft), a kill for each surviving mutant M1-M17, and B2."
112. T3:47–50. 29 more checks: 15 tampers (35 in all), 8 options (13 in all), 6 singles. CONFIRMED: draft 3 has 33 single chk calls plus 35 and 13 loop iterations, 81 in all.
113. T3:50–53. Exit 0, 93d107a4…, 716 = 634 + 82. CONFIRMED.
114. T3:55–56. Run 3: overlay3 from 9b71bbb, 8df113e4…. CONFIRMED.
115. T3:57–59. Draft 3 is draft 2 +2 −2, with the docstring texts as given. CONFIRMED.
116. T3:59–60. The stale line is observation 6 of that raw. CONFIRMED (supplement values-check raw:278).
117. T3:60–61. No check reads the docstring. CONFIRMED (see item 24).
118. T3:61–64. Run 3's output equals run 2's bytes. CONFIRMED.
119. T3:66–68. 727 = 716 + 11; 14 HF checks for 3 skip lines; 645 against 634. CONFIRMED (item 29; gtout:76; RESULTS.md:1606).
120. T3:68–69. G-VER's checks count the same at either site. CONFIRMED: the loops are fixed, and the symlink and version cases make one check either way.
121. T3:69. The launch files restate the count. NOT CHECKABLE.

TOTALS: 121 items: 95 CONFIRMED, 12 IMPRECISE (7, 31, 34, 41, 46, 49, 52, 54, 67, 69, 82, 100), 1 FAIL (111), 13 NOT CHECKABLE (9, 16, 18, 20, 21, 26, 39, 60, 86, 99, 105, 107, 121).

OBSERVATIONS
1. All three runs used `cd jl*/.venv/bin`: a glob that expands to the marker-named venv folder, passed to zsh's builtin cd (15:29:15Z, 16:34:35Z, 17:27:35Z). No process argv held it. T3:22–23 states the form, and the seat classed it inert at 1641948 (RESULTS.md:2675–2676), but T1's list names the runs and not the form.
2. In span A, the file-reading tool also read the model manifest (15:09:21Z, with an offset). T1:146–147 names only the supplement's two reads.
3. T1:31–32 and T2:39 say "one docstring line", but the fix rewrote both of its lines (+2 −2, as T3:57 says). "one docstring (two lines)" would match.
4. The driver's docstring header has the same GV12 omission as item 7. Draft 3 is the BUILD's bytes, so the entry can carry the qualification.
5. GV5 as sent says "This keeps 2 for G-VER's STOP alone" (spec raw:128); F5 shows usage errors also exit 2. A pointer to the supplement's §1.6 at T1:63 would close that.
6. T1:77–81 folds B5 (stderr captured) into F5 without naming it; T2:105 names it.
7. T2:67–69, 92 and 101 use the present tense for launch files that are not written yet ("name", "print", "export"). "will" would mark them as plans.
8. T1:94: the second shell command (17:02:39Z) ran two greps, so there were three grep runs in two commands.
9. T1:92–93 says Q-F3's names were in the stream. I could not check that any name under data/m[f]3 is tracked (barred to me). Names under data/n/ckpt and data/n/reports are tracked (per 7d01b02's message).
10. T1:6 "no record": for the "exists" refusal, the earlier record stands as it was. "no record written" would be exact.
11. T2:19–20: the brief also allowed reading "this brief" (brief:90); since it was the prompt, this changes nothing in practice.
12. The internals of the kit scripts, the edits and rewrap checks, and the commit-build script are not visible in T's command texts. T1 names them only by script.
13. At 17:40:34Z, after span B, a command created the gate's v10 id list and copied gate v9 to v10. That belongs to @FINAL@.
14. T1:41–44 and T3:37–41 rest on the window request, the grant and the ruling, none of which are committed. The seat cannot check them; quoting them or pointing to where they are would let it.
15. T1:21 holds only while MANIFEST.json passes ids.load (supplement §1.3, O3). A short pointer there would match the supplement.
16. T3:66–68: the launch recorded 645; 634 is the BUILD's figure (RESULTS.md:1606), and the 14-for-3 breakdown is the code's and G-VEC's re-run entry's (RESULTS.md:3680).

DEPARTURES
1. One command's text held a stray environment assignment, `awk_free=0`, before a `sed`. No awk ran, but the word stood in the command's text.
2. I used `sed` as a filter and for masking. It runs a script language and is not in the brief's list; I declare it for classing.
3. I read T beyond its Bash tool_use items and tool results, as follows:
   - the review Agent call's prompt, hashed only;
   - the file-reading tool's calls, classed by bracketed patterns, with only counts and times printed;
   - one file-reading result, its "tokenizer_class" line only;
   - record kinds and stamps around run 3's end, with no content.
4. Once I printed more than a finding needed: the 17:01:34Z output in full, about 100 names under the model folder, masked. A count would have done.
5. `git ls-files -o --exclude-standard -- results/raw` and `git show --name-only --format= 9b71bbb -- results/raw` named a non-data folder without item 3's exclusions. Neither command reached anything under data/.
6. A name-only `ls` of data/ into `/usr/bin/grep -c -x` with a bracketed pattern put data/'s child names into the pipe, the campaign folder's own name among them. Only a count printed, and nothing under any child was listed.
7. Two commands misfired harmlessly. An `echo ==` hit zsh's `=` expansion and stopped that command after a `sed -n` of a committed raw. A `$c:` modifier and a `head -c 0` gave errors.
8. Otherwise:
   - no interpreter ran but shasum and jq;
   - no marker stood in any argv or command text;
   - nothing was written and nothing went to the network;
   - nothing under data/*/ckpt, data/*/reports or data/m[f]3 was read, listed, sized or timed;
   - in S, only the named files were read.
```
