# n — G-VER of record's BUILD texts, redrafted for draft 4: the second blind values-check, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the three texts as redrafted for draft 4 and the seat's
rulings, at HEAD `9b71bbb`:
- T1, this commit's entry, sha256 `76e3f238…e4d8` (306 lines), its second values-check, second checker's-departures
  and final-sweep lines placeholders not to be checked;
- T2, the review raw, `e3047513…9f27` (300 lines): its head with every disposition, and the review's report appended;
- T3, the self-test raw, `bee29af9…9b70` (87 lines).

The texts were started from the first round's edited texts, which the first values-check had checked
(`results/raw/2026-11-22_n-gver-build_valuescheck.md`). They were redrafted for draft 4, the seat's first sitting of
2026-11-22 and run 4.

**The checker's brief** was given to the checker as its prompt: Code's scratch file `S/step4b/gver/build2/vc_brief.md`
(`693d23f1…09a4`, 179 lines). It:
- named the texts and the sources:
  - in the repository, the files the texts cite, at `9b71bbb`, each checked tracked and clean, and the seat's raw,
    untracked, at its sha256;
  - in Code's scratch, by name and sha256 only: the five drivers (drafts 1–4 and HEAD's copy), four deltas, the three
    `.gitignore` files, the review's brief and report, the twelve self-test run files, the overlay's recipe, the
    package-digest script, the first values-check's brief, report, raw, replay script and output, the first round's
    three edited texts, and four sweep records;
- allowed `shasum` by name, and `jq` on the four sweep records, on this session's transcript and on committed JSON
  outside `data/*/ckpt`, `data/*/reports` and `data/m[f]3`;
- set the transcript's use: a sweep of Code's shell commands in four spans. They are the BUILD's 20 before
  `d92500b`'s window; from that window to the first brief's hash; after it, through Code's first final sweep; and
  after that, to this brief's own hash. It asked for the last two spans in full, and the first two where the text
  differs from the first round's. It warned that a span's bound must be a prefix or an exact stamp, never a stamp
  ending in "Z" alone;
- barred any other interpreter, any write, any network, and any guard marker in an argv: a path, a grep pattern, a
  variable or glob that expands to one (an unquoted bracketed pattern among them), a loop that passes one, and the
  command's own text;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, and anything in Code's scratch but the named files;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (244 lines, sha256
`d33d8910…8b55`). It names scratch files only by their paths inside the scratch folder, and the transcript as T.

**Totals:** 110 items: 90 CONFIRMED, 5 IMPRECISE, 1 FAIL, 14 NOT CHECKABLE; and 10 observations. Code counted them
again by tool, by the verdict that follows each item's claim. A first count, by the first verdict word on each line,
read item 37 as a FAIL, since its claim quotes the entry's "the FAIL"; its verdict is CONFIRMED.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words or the words below. Every observation is
applied, met or noted. §2 gives the edits and their check by tool.

- **Item 13 (FAIL), T1:41–42.** Applied in the checker's words: outside the G-VER section the driver is draft 3's but
  for the module docstring's `gver` paragraph.
- **Item 35, T1:72–73.** Applied: draft 4 builds B4 as the seat ruled it (§1.2), in the checker's words, the line
  written as three clauses.
- **Items 52, 54 and 56, T1's departures list.** Applied: every kind the checker found missing is listed, in its
  words or near them. Item 56's three commands are given one by one, each with its kinds.
- **Item 72, T2:47–48.** Applied in the checker's words.
- **O1.** Applied: T1 says the seat's raw is committed by path with the coordinating session's notes, before this
  commit.
- **O2.** Applied in T1. Only the off-pin hash refusal's text names the INTEGRITY incident, and the launch files class
  the rest by what each REFUSED line names (§1.4). By Code's reading, these are of the INTEGRITY kind too: a missing
  or symlinked one of the eight, `check_weights_folder`'s listing and byte counts, and `ids.load`'s sha256 and count.
  The seat may rule otherwise. The launch files' line names the missing or symlinked hashed file.
- **O3.** Applied. T1 says draft 4 is more than the seat's "one constant and the record's field": a function, the
  renames, the refusal's wording and the docstring, 118 lines in and 89 out. Code reads them as what that constant and
  field need, and the seat may rule otherwise. T2 and T3 name the field, the renames and the docstring paragraph.
- **O4.** Applied: "(§0, §1.2)" for "moot", in T1 and T2.
- **O5.** Applied: T1 and T2 quote §0's short form, "runs as Code built it, with two additions and one rule on its
  ends", beside what §1.2 and §2 mean for the driver.
- **O6.** Applied: the heading is "after the first values-check's brief's hash".
- **O7.** Met. T1 lists the three commands after the second sweep's record, with their kinds, and quotes the checker's
  bracketed counts over them, 0 and 0.
- **O8.** Applied: T3 says "the venv's bin folder".
- **O9.** Noted: run 4's exit notice is a harness record in this session's transcript, which the brief did not open to
  the checker. Code waited on it, as T1 and T3 say.
- **O10.** Applied: T1 says N.2 is in the PI's routing of the seat's first sitting, which the coordinating session
  commits with the seat's raw.

**Beside the checker's items:**
- the entry's three placeholders are filled with this check's summary, its departures and the final sweep;
- the edit count's placeholder sits at the start of its line, so that the filled line stays within 120 characters;
- two edits of Code's own, made after the check because the coordinating session's notes commit, `5ad19de`, landed
  after it. T1 cites that commit for the seat's raw (O1's sentence), and it links the PI's routing raw,
  `results/raw/2026-11-22_first-sitting_pi-routing.md`, whose line 25 is N.2, committed there (O10's sentence).

## 2. The edits, checked by tool

The edits were made to new versioned copies of the three drafts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/gver/build2/edits_check.sh`. The results are byte for byte the revised drafts, so nothing else changed after
the check:
- the entry, 17 of 17 edits; the review raw, 2 of 2; the self-test raw, 2 of 2.

The entry's 17 include its three placeholders, filled with this check's summary, the checker's departures and the
final sweep, and the two edits that cite `5ad19de` (§1's last item). After the edits, one placeholder was filled by
tool: the entry's count of these edits.

## 3. The report, as returned

```text
BLIND VALUES-CHECK (second): G-VER of record's BUILD texts as redrafted for draft 4 (T1 entry, T2 review raw, T3 self-test raw)

Setup: HEAD is 9b71bbb, and it did not move while I worked. T1, T2 and T3 are at the brief's sha256s with 306, 300 and 87 lines, and they were unchanged when I re-hashed them at the end. Every other named S file is at its sha256 and stated line count: the five drivers, the four deltas, the three .gitignore files, the review's brief and report, the twelve run files, the recipe, pkgsha.sh, the first values-check's brief, report, raw, replay script and output, the first round's three edited texts, and the four sweep records. The seat's raw is c66cb2f7…650b, 84 lines, and still untracked. Every repository file I used is clean at HEAD (rev-parse equals hash-object): RESULTS.md, LOCK-n.md, .gitignore, scripts/n_sessions.py, valence_core/m/resume.py, the block, the supplement and its values-check raw, the spec raw, and results/raw/2026-11-21_n-gtime-v1_out.txt. valence_core/n is unmodified, with no untracked files. The model manifest is tracked and unmodified (checked by a quoted glob pathspec) and I read it with the file-reading tool only.

ITEMS

T1 (S/step4b/gver/build2/entry_src.md)
1. T1:1–3, the title. CONFIRMED. The quote is in the spec raw §3, and the seat raw:3 has "(first sitting)". The delta touches only the driver, and no command in T runs gver.
2. T1:4, valence_core/n stays at 06b55761…1d39 (L §18). CONFIRMED. The digest is at L:781, and §18 starts at L:776. valence_core/n is clean and last changed at ef105f1. Overlay4's shell digest is 06b55761…1d39 (T, 18:36:04Z).
3. T1:5–6: no weights load, nothing is read, and building the provenance makes a CUDA context. CONFIRMED. See draft4:243 and the STAGE line in _gver_prepare; cmd_gver hands off to run_gver.
4. T1:6–17, the refusals "in this order", with exit 1, a REFUSED line and no record written. CONFIRMED. _gver_prepare checks, in order: the record exists; the pod is missing or another; CUBLAS_WORKSPACE_CONFIG; then the STAGE line; the weights' sha256; the driver against HEAD; gver_lock_check; the session set and ids through _gver_loaded; the R6 bridge; n's identifier; LOCK_TOKENIZERS; the package and closure. run_gver prints "REFUSED before G-VER: …" and returns 1. The closure is twelve files (draft4:3829–3842; L:796), and L:767–768 pins tokenizers 0.22.2.
5. T1:18–20, the eight non-shard files and the INTEGRITY wording of the off-pin refusal. CONFIRMED.
   - GVER_HASHED_FILES lists the eight.
   - The manifest's instruct entry lists 22 files: 14 shards and exactly those eight.
   - gver_hashed_files refuses a symlink or a missing file, and an off-pin file with "(GV3; an INTEGRITY incident under the respawn protocol: stop, touch nothing, escalate)".
   - See seat §1.2 and §1.4.
6. T1:22–23: MANIFEST.json is printed and left to G-VER (L:543), while it passes ids.load (supplement §1.3). CONFIRMED. The ids line ends "equal" or "not equal, one of G-VER's causes (L:543)". See also supplement:78–87.
7. T1:23–28: G-VER, the record with hashed_files, check_gver, written once and checked on disk, F1, the exits, no option and no smoke. CONFIRMED. See draft 4's run_gver, gver_record, gver_write and main()'s gver branch.
8. T1:29–30, the docstring's PINs "as sent but for GV4's pins as built, GV3's hash set as ruled, and GV12's two durations marked a lower bound". CONFIRMED (draft4:261–262; the GV3 line at 265–266; the GV12 line).
9. T1:30–34: the seat ruled at its first sitting, as built but for GV3's hash set (§1.2), and the §2 quote. CONFIRMED. The quote is exact at seat raw:40. See observation 5.
10. T1:35: draft 4 is 55885e65…385f, 6,224 lines, +1,019 −3 from 4616f9c3…2553. CONFIRMED (shasum, wc -l, git diff --no-index --shortstat).
11. T1:36–37, draft 3's one docstring (two lines), after observation 6. CONFIRMED. See delta_from_draft2.diff (+2 −2) and supplement values-check raw:278.
12. T1:38–41, what draft 4 carries, and the renames by sed over the G-VER section alone. CONFIRMED. See delta_from_draft3.diff. At 18:32:24Z, T shows `sed -i` over lines 5125–6048 of the copy, which is draft 3's section (from "# --- G-VER of record" to the line before def _parse_rulings). It renamed tokenizer_files, tokenizer_pins, ids.pinned_tokenizer_sha256s and ids.TOKENIZER_FILES.
13. T1:41–42, "Outside that section the driver is draft 3's, the other stages' uses of ids.TOKENIZER_FILES among it." FAIL.
   - I diffed the two drafts with each one's section removed (draft 3 5125–6048, draft 4 5126–6077). Fifteen lines differ, in four hunks of the module docstring's gver paragraph: draft4:241–242, 253–255, 262 and 265–266.
   - Those lines cite the seat's raw for the starred seven, give step 4's eight files and their INTEGRITY kind, change the PINs' header, and change GV3's line.
   - The other stages' uses (draft4:512, 592 and 3056) do stand.
   - Put instead: "Outside that section the driver is draft 3's but for the module docstring's `gver` paragraph, which now cites the seat's raw for the starred seven and gives step 4, GV3's line and the PINs' header as ruled; the other stages' uses of `ids.TOKENIZER_FILES` stand as draft 3's."
14. T1:43–44, the .gitignore: +7 lines, 81f5f227…b610, gver.json alone admitted, the temporary ignored. CONFIRMED. The diff from base to v2 adds seven lines, with the rules !/data/n/gver/, /data/n/gver/* and !/data/n/gver/gver.json.
15. T1:45–46, v1 (2e105c34…d8a8) and its comment's presupposition (F10). CONFIRMED. v1 has "is the gate LOCK-n v1.0 and the campaign follow", and v2 drops it.
16. T1:47–49, the dry-run adds. CONFIRMED. At 15:25:10Z the test files were gver.json, gver.json.tmp, other.json, gtime.json and stray.json. The adds at 15:25:10Z and 16:28:15Z added only .gitignore, data/n/gtime/gtime.json and data/n/gver/gver.json.
17. T1:50 and T1:68–69, the links to the self-test and review raws. NOT CHECKABLE: neither is placed yet.
18. T1:51, draft 1's "687/687" as HEAD's 634 plus 53. CONFIRMED.
   - The output is in selftest_run1.txt, and 634 is at RESULTS.md:1606.
   - Draft 1's _gver_selftest has 29 static chk( calls, two of them in loops: 27 singles + 20 tampers + 5 argv cases = 52.
   - cmd_selftest's environment check makes 53.
19. T1:51–52 (and T3:40–41): the request expected 688 and the box's figure was 699. CONFIRMED from T's output at 18:18:07Z, a grep of Code's note. Its line 51 reads "688/688 … HEAD's 634 plus 54", and its line 53 begins "699." (645 + 54). The note itself is outside the repository and I did not read it.
20. T1:52–53, the wrapper "ran to its end" counted, which is appended only on a raise. CONFIRMED. At draft4:462–467 that chk sits only in the except branch.
21. T1:53, the grant confirmed 54. NOT CHECKABLE.
22. T1:53–54, "on the coordinating session's ruling as the window's grantor". NOT CHECKABLE.
23. T1:54, no re-run, and the box's figure for draft 1 was 698. CONFIRMED. T holds one overlay1 run (the first check's item 22), and 645 (gtout:76) + 53 = 698.
24. T1:54–56, Code's note at 634f7181…be88. CONFIRMED: T at 18:18:07Z prints that sha256 and 54 lines. The coordinating session's messages are not checkable.
25. T1:57–58: draft 2 is 3df537d6…83c1, 6,195 lines, "716/716", 29 more. CONFIRMED: 15 tampers + 8 argv cases + 6 singles. The static chk( count goes from 29 to 35, and the loops from 20 to 35 and from 5 to 13.
26. T1:59–60: draft 3 is 8df113e4…3f02, 6,195 lines, "716/716", and no check reads the docstring. CONFIRMED. Draft 3's only __doc__ reads are keys' (:4606) and the module's first line (:6063), and inspect is used only for gread_bench's signature.
27. T1:61–62: draft 4 "717/717", one check more. CONFIRMED. Static chk( calls go from 35 to 36, with the loops unchanged (35 and 13); the new check is r_m (ninth file; no vocab.json). The output is in selftest_run4.txt.
28. T1:63, exit 0 and an empty stderr for each run. CONFIRMED: all four .exit files hold "exit 0", and all four .err files are empty.
29. T1:63, the battery windows granted. NOT CHECKABLE.
30. T1:64–65, the temporary folder empty before and after, and PID 8051 the only Python process. CONFIRMED. For run 4, T shows it at 18:36:04Z and 18:43:33Z (tmp: [], pgrep python: 8051). Runs 1–3 are the first check's item 27. The seat raw:58 identifies 8051 as Q-F3's campaign.
31. T1:65, runs 3 and 4 as the harness's background task. CONFIRMED. Run 4 has bg true at 18:43:04Z, and its tool result reads "Command running in background". Run 3 is the first check's item 28.
32. T1:65, each waited on by its exit notice. NOT CHECKABLE for run 4 within the brief's reads, since the notice is neither a Bash item nor a tool result. Its files, read at 18:43:33Z, were complete ("exit 0").
33. T1:66, the box's count of 728. CONFIRMED: 717 + 11, from 645 (gtout:76) against 634.
34. T1:70–71, one BUG, 11 findings (1/6/4), 17 mutants, 8 box risks, 7 observations, one departure. CONFIRMED (the report).
35. T1:72–73, "drafts 2–4 build in F1–F4, F6–F9 and F11, a kill for every mutant…, and B2, and the .gitignore's second draft F10". IMPRECISE. B4 is missing: T2:111–113 says "B4, ruled … Draft 4 builds it". Put instead: "drafts 2–4 build in F1–F4, F6–F9 and F11, a kill for every mutant by Code's reading, and B2, draft 4 B4 as the seat ruled it (§1.2), and the `.gitignore`'s second draft F10;"
36. T1:74–75, the five items, F5 as §1.6, and "The seat ruled all six". CONFIRMED.
   - The five and F5 are at supplement:17–18 and §1.1–§1.6.
   - The seat rules on F3, F4 and O3 in §1.2, on O5 through §1.2's hash set, on B7 in §1.6, and on F5 in §1.4.
37. T1:77–81, the first check: 121/95/12/1/13 and 16; the FAIL and every IMPRECISE item applied; O13 met; 36 of 36 (21, 9, 6); the report whole. CONFIRMED.
   - The totals are at vc_raw.md:32 and O13 "Met" at :72.
   - edits_check.txt shows 21, 9, 6 and 36.
   - vc_raw.md:96–314 is byte-identical to vc_report.md (bd7b0ab6…1b2f).
38. T1:83, "nothing ran on a model". CONFIRMED. Spans C and D hold no model or gver command; run 4 is the model-free self-test.
39. T1:85–90, the nine unstarred readings and their exceptions; the GV5 quote; GV7; GV15. CONFIRMED. The seat's §2 is at raw:39. In the spec raw: GV3's environment at :97–98, "This keeps 2 for G-VER's STOP alone." at :127, GV7 at :136–138, GV12 at :173–175 and GV15 at :182–187.
40. T1:91–94, GV4 as built and accepted (§1.2). CONFIRMED (seat raw:17).
41. T1:95–96, GV3 as ruled (§1.2). CONFIRMED (raw:19). See observation 4 on "moot".
42. T1:97–100, the ends (§1.4). CONFIRMED (raw:26–29).
43. T1:101–102, F2 and G-TIME-n's same pattern. CONFIRMED. The text is unchanged, and it is the first check's item 37.
44. T1:103–105, B7 as ruled (§1.6), git mv to results/raw/<date>_n-gver_<the old box>_gver.json. CONFIRMED (raw:33).
45. T1:106–113, the items carried to the launch files. NOT CHECKABLE (plans). They match the report's F5, B3, B5, B6, B8 and F11.
46. T1:114–117, the seat's §1.4 as agreed with the pod session. NOT CHECKABLE: the agreement is outside the repository. Its terms match raw:27 (stop, touch nothing, escalate; nothing re-launched until the PI and the seat have ruled).
47. T1:119–124, the scope: 109 commands to the first sweep's record, the two after it, the BUILD's 20, and the final sweep. CONFIRMED by jq over T.
   - 15:55:10.138Z–17:37:35.303Z holds 109 commands, equal to sweep_build.jsonl by cmp. Up to the first brief's hash (17:39:37.084Z) it holds 111.
   - 15:08:36.026Z–15:29:58.842Z holds 20 commands, equal to sweep_tail.jsonl:2–21 ({t, cmd} by cmp).
48. T1:125–130, the first barred form (data/[o]lmo, unquoted). CONFIRMED. The text is unchanged, and it is the first check's item 42.
49. T1:131–133, the globs: two commands, three grep runs, 18, 88, 65 and 7 names, none holding a marker. CONFIRMED.
   - T's output at 17:31:33Z gives 20, 88, 65 and 7 then, two of the first glob's names being placed at 17:21 (after both commands).
   - My recount now gives 21, 88, 65 and 7, the extra one the untracked seat raw.
   - 0 of the names hold a marker, by a bracketed count.
50. T1:134–222, the span A and B items. CONFIRMED. Their text is the first round's edited entry, but for rewraps and the heading "the first round's texts and sweep". The first check verified it (items 44–54, applied in its words), and the span counts are rechecked in item 47.
51. T1:223–226, "throughout", including "the runs' `cd jl*/.venv/bin`". CONFIRMED. Run 4 at 18:43:04Z uses the same subshell form. Spans C and D write only in scratch. The seat's classing is at RESULTS.md:2675–2676.
52. T1:227–237, the six commands after the first check's window. IMPRECISE. The six are equal to sweep_final.jsonl by cmp, but three are not fully covered:
    - 18:17:57Z: a /usr/bin/grep -c of fence lines over the saved report, and tail -c 1 into od -c.
    - 18:21:38Z: a for loop over the three v2 files, with wc -l of each.
    - 18:23:06Z: a bracketed count of the campaign folder's plain name (0) beside the marker count.

    Put instead:
    - "`jq` over the checker's transcript to take its report from its hand-back, with `wc -l`, `shasum`, counts of local roots, ids and fence lines, `head -1`, and `tail -c 1` into `od -c` over the saved report;"
    - "line-width counts over the v2 files (a `for` loop over the three with `wc -l` of each, and a `while read` loop, `wc -m` of each line), a non-ASCII count and their placeholders;"
    - "`jq` over this session's transcript for this sweep, with bracketed counts of marker words and of the campaign folder's plain name over it (both 0);"
53. T1:238, "26 commands to its record". CONFIRMED: jq over 18:23:06.706Z < t ≤ 18:49:16.645Z gives 26, equal to sweep2.jsonl by cmp.
54. T1:239–265, the second round's list. IMPRECISE. These are not covered:
    - 18:25:42Z: a /usr/bin/grep -n of the commit entry's filled line, into cut.
    - 18:26:04Z: wc -l and wc -c of the commit message, and wc -l of gate v10.
    - 18:26:15Z: cat of the dry-run gate's output, and pgrep -i python.
    - 18:27:39Z: pgrep -i python.
    - 18:35:26Z: a sed -n print (lines 5–400) of the delta from draft 3.
    - 18:35:54Z: a for loop of shasum and wc -l over draft 4 and its two deltas.
    - 18:36:04Z: a for loop of existence tests over run 4's three output files.
    - 18:43:33Z: a /usr/bin/grep -c of FAIL lines, and ls -A of the temporary folder and pgrep -i python after the run.
    - Smaller: wc -l of entry_v2 at 18:24:16Z and of draft 4 at 18:35:18Z.

    Put instead:
    - for the kit: "the first round's commit kit: `zsh` of its build script, with a `/usr/bin/grep -n` of the filled line; the message check, with `wc -l` and `wc -c` of the message; `diff` of gate v9 and v10, with `wc -l` of v10; the kit's dry-run gate, with `cat` of its output; `git rev-parse HEAD` and `git diff --name-only` with the pathspecs; the splice checked by `diff`, `git diff --no-index -U0` and `cmp` over its `RESULTS.md` copies in scratch; `sed -n` of the place script; `wc -m` of the filled line; `pgrep -i python`, twice; and the first commit window request's hashes, since withdrawn;"
    - for the deltas: "`git diff --no-index` deltas (`-U0`, `--shortstat` and its default form) with `/usr/bin/grep -c` counts and a `sed -n` print of the delta from draft 3; a `for` loop of `shasum` and `wc -l` over draft 4 and its two deltas; `git rev-parse HEAD` and `git diff --name-only` with the pathspecs;"
    - add "a `for` loop of existence tests over run 4's three output files" to overlay4's item;
    - for run 4: "its files read by `cat`, `wc -l`, `wc -c`, `/usr/bin/grep -c` and `shasum`, with a name-only `ls -A` of the temporary folder and of the overlay's scripts folder, and `pgrep -i python`;"
55. T1:266–267, the sweep's bracketed counts of marker words and the campaign's plain name (both 0), and of loops. CONFIRMED. T's output at 18:49:16Z reads "marker words: 0; campaign plain: 0; loops: 4". My count of commands with a loop among the 26 is also 4.
56. T1:269–270, "After it: line-width, ASCII, placeholder and leak counts over the second round's texts, and the texts' and the second values-check brief's hashes". IMPRECISE. The three commands after the record (18:50:15Z, 18:50:39Z and 18:52:20Z) also ran:
    - a for loop and a while read loop, with wc -l;
    - a /usr/bin/grep -n of the review raw's heading, and its report part hashed by sed -n into shasum;
    - a for loop of shasum and wc -l over sixteen named files, not only the texts;
    - git rev-parse HEAD, and the seat raw's shasum and git ls-files;
    - a diff of the brief's last five lines (tail -n 5) against the seat brief's lines 106–110 (sed -n), by process substitution;
    - a sed -n print of the review raw's lines 135–137;
    - wc -l of the brief.

    Put instead: "After it: line-width, ASCII, placeholder and leak counts over the second round's texts (a `for` and a `while read` loop, with `wc -l`), the review raw's heading found by `/usr/bin/grep -n` and its report part hashed (`sed -n` into `shasum`); a `for` loop of `shasum` and `wc -l` over the texts and the brief's other named files, with `git rev-parse HEAD` and the seat raw's `shasum` and `git ls-files`; a `diff` of the brief's list of record against the seat brief's (`tail`, `sed -n`) and a `sed -n` print of the review raw's lines 135–137; and the second values-check brief's hash and `wc -l`;"
57. T1:273–275: the bracketed counts are 0; globs and loops were checked; no marker reached an argv but in the first item; nothing under ckpt, reports or Q-F3's folder was read, sized or timed. CONFIRMED.
    - My bracketed counts give 0 marker words and 0 plain campaign names in span A (20 commands), B (111), C (6) and D (29).
    - In C and D no loop or variable passes a marker-named path.
    - The one glob that expands to one is run 4's builtin cd (18:43:04Z), which is declared.
    - The kit's dry gate checked closed paths "by digest and blob id, never read".
58. T1:276–277, the reviewer's departure. CONFIRMED (report:292).
59. T1:278–294, the first checker's seven departures. CONFIRMED (vc_report.md, DEPARTURES 1–7).
60. T1:296, the supplement checker's departures are in 9b71bbb's entry. CONFIRMED (RESULTS.md:63).
61. T1:297–298, the gate. NOT CHECKABLE (a plan). The first checker's id was written to the next id list, and gate v9 copied to v10, at 17:40:34Z.
62. T1:299–305: committed by path, the digest at the commit, the home-folder count, not pushed, then the launch files and the run "(the PI's N.2)". NOT CHECKABLE (plans). N.2 is the seat raw's routing item (raw:68), and its text matches. See observation 10.

T2 (S/step4b/gver/build2/review_raw_src.md)
63. T2:1–3. CONFIRMED.
64. T2:5–7, what was reviewed: d92500b, 4616f9c3…2553 to f5baf379…7b2c (6,031 lines), and 2e105c34…d8a8. CONFIRMED (brief:7–18).
65. T2:9, draft 1 passed 687/687. CONFIRMED. The window part is not checkable.
66. T2:11–22, the brief's account. CONFIRMED.
    - The hash is d9ad5c96…9411 and the brief has 102 lines.
    - It names the change and the texts (:7–47), eight known items (:49–60), the report's sections (:62–74) and the bars (:77–96).
    - "and this brief" is at :90, and items 1–5 at :98–102.
67. T2:24–26, the report: jq from the hand-back, 164 lines, 3bb14a39…, S/ paths only. CONFIRMED (shasum and wc -l). Its only scratch paths are the two S/ files, and Code's leak count at 18:50:15Z is 0.
68. T2:28–34, the sum. CONFIRMED (the report).
69. T2:37–39, draft 2. CONFIRMED (delta_from_draft1.diff; selftest_run2.txt).
70. T2:40–42, draft 3. CONFIRMED.
71. T2:43–45, draft 4 is draft 3 with the seat's hash set, 717/717. CONFIRMED (delta_from_draft3.diff; selftest_run4.txt). See observation 3.
72. T2:47–48, "Of the box risks, B2 is applied in the driver, B3, B5, B6 and B8 go to the launch files, and B1, B4 and B7 are agreed, noted or declared." IMPRECISE. T2's own §1 has B4 "ruled … Draft 4 builds it" (:111–113) and B7 ruled at §1.6 (:117–120). Put instead: "F5 is carried to the launch files. Of the box risks, B2 is applied in the driver, and B4 in draft 4 as the seat ruled it (§1.2); B3, B5, B6 and B8 go to the launch files; B1 is agreed, and B7 declared and ruled (§1.6)."
73. T2:48–53: the five items, the supplement at 9b71bbb, F5 as §1.6, the seat ruling all six, the hash check widened (§1.2), and draft 4 building it. CONFIRMED.
74. T2:57–60, F1. CONFIRMED: the write sits inside gver_write's try, an OSError becomes SystemExit, the file is unlinked, run_gver prints FAILED and returns 1, and the r_w5 case covers it.
75. T2:61–66, F2. CONFIRMED (_gver_loaded catches ValueError, KeyError, OSError and TypeError, and SystemExit passes; the sessions, ids, ids-missing and ids-key cases).
76. T2:67–69, F3, B:141–142, supplement §1.1, and "The seat accepted it (§1.2)". CONFIRMED (B:141–142 is "Not held: cuBLAS's setting…"; seat raw:17).
77. T2:70–73, F4: LOCK_TOKENIZERS held in two places (L:767–768), supplement §1.2 with Q2, accepted (§1.2), and draft 3's docstring. CONFIRMED.
78. T2:74–78, F5: the supplement check's item 12 and observation 1, §1.6, and the seat accepting it as the launch files' part (§1.4). CONFIRMED (supplement values-check raw:142 and :268; seat raw:25).
79. T2:79–85, F6 and M12–M15. CONFIRMED (the spy, FakeAuto and version cases, and the seam check naming pod and load_sessions).
80. T2:86–93, F7 and M1–M10, with the zero STOP (M7). CONFIRMED: tampers 21–35, rep_zero and env_z.
81. T2:94–95, F8 and F9. CONFIRMED (not wp4.parent.exists(); "this run wrote no record").
82. T2:96–99, F10 in v2, and F11's wording. CONFIRMED (gitignore_v2; GVER_DURATION_KEYS' comment; the durations line). The launch clause is a plan.
83. T2:100–103, the M1–M17 kills: thirteen options, eleven of them refused with "gver takes no option", and the ": equal" assert. CONFIRMED.
84. T2:104–110, B1, B2 and B3. CONFIRMED (the FakeAuto stand-in; the try around symlink_to; the check by name and the 12-file closure).
85. T2:111–113, "B4, ruled", the eight including config.json, vocab.json and merges.txt. CONFIRMED (seat raw:19).
86. T2:114–116, B5, B6 and B8 carried to the launch files. NOT CHECKABLE (plans).
87. T2:117–120, B7 and its ruling (§1.6). CONFIRMED (supplement:107–115; seat raw:33).
88. T2:121–125, O1–O4, with the O3 ruling (§1.2) and the INTEGRITY kind (§1.4). CONFIRMED (seat raw:18, :27).
89. T2:126–128, O5: tokenizer_config.json names GPT2Tokenizer, and the question is moot. CONFIRMED (supplement §1.4; manifest pin fff5b944…3fc7; the first check's item 89). See observation 4.
90. T2:129–131, O6 (698; 727; 728) and O7. CONFIRMED (645 + 53, + 82, + 83; draft4:243).
91. T2:132–133, the reviewer's departure is declared in the entry. CONFIRMED (T1:276–277).
92. T2:137–300, the review's report byte for byte. CONFIRMED: `sed -n 137,300p` hashes to 3bb14a39…411d, and cmp shows it equal to S/step4b/gver/review_report.md.

T3 (S/step4b/gver/build2/selftest_src.txt)
93. T3:1–3. CONFIRMED.
94. T3:5–6: the same bytes at cd6b30d, d92500b and 9b71bbb; 4616f9c3…; +1019 −3. CONFIRMED. All three, and 7d01b02 too, hold blob b00f96eb…, the delta's from-index.
95. T3:7, the .gitignore does not enter the self-test. CONFIRMED: the recipe's paths hold no .gitignore, and draft 4 never names it.
96. T3:8–12, the package digest by shell over four overlays and HEAD's files, held in process. CONFIRMED. pkgsha.sh matches resume.py:328–350. Overlay4 printed 06b55761… at 18:36:04Z, and overlays 1–3 and HEAD's are the first check's item 95.
97. T3:14–17, HF cases skipped and counted; G-VER's cases need neither library. CONFIRMED (draft 4's FakeAuto case; the first check's item 96).
98. T3:18–23: the overlays from cd6b30d, d92500b and 9b71bbb (runs 3 and 4), 174 files each, the recipe f8cdbccb…, and diff -rq showing the driver alone. CONFIRMED. At 18:36:04Z T prints "recipe unchanged", "overlay: 174 files from 9b71bbb…", and diff -rq naming only scripts/n_sessions.py. The rest is the first check's item 97.
99. T3:24–27, the command form. CONFIRMED by run 4's command at 18:43:04Z. See observation 8.
100. T3:28, battery windows granted for each run's bytes. NOT CHECKABLE.
101. T3:28–31, the states before and after. CONFIRMED for run 4.
    - Before (18:36:04Z and 18:36:51Z): the overlay's driver at 55885e65…, tmp empty, and run 4's files absent.
    - After (18:43:33Z): stderr 0 bytes, tmp empty, and pgrep showing 8051 alone.
    - "the one the grant named" is not checkable.
102. T3:32–33, runs 3 and 4 as background tasks. CONFIRMED (bg true; the tool result).
103. T3:33, "Code waited for each exit notice". NOT CHECKABLE for run 4 within the brief's reads (see item 32).
104. T3:35–46, run 1. CONFIRMED.
    - f5baf379…; exit 0; the output hashes to 555eff1b…; T3:39 minus five spaces equals the run file (cmp).
    - 634 + 53 (27 + 20 + 5 = 52, + 1); the wrapper; 688 and 699 (item 19); no re-run; 698; the note's 634f7181…be88.
105. T3:42–46, the grant's 54 and the ruling. NOT CHECKABLE.
106. T3:48–58, run 2. CONFIRMED.
    - It comes from d92500b (the first check's item 109), with 3df537d6… and +231 −67.
    - The 15 + 8 + 6 checks; 35 tampers and 13 argv cases in all.
    - The output 93d107a4…; T3:57 equals it by cmp; 634 + 82 (33 + 35 + 13 + 1).
107. T3:60–69, run 3. CONFIRMED: 8df113e4…, +2 −2, the docstring texts, observation 6 (supplement values-check raw:278), no check reading it, and the run's bytes equal to run 2's (93d107a4…). T3:69 equals it by cmp.
108. T3:71–82, run 4. CONFIRMED.
    - It comes from 9b71bbb, with 55885e65… and +118 −89.
    - The self-test's hash, shard, production-pin and INTEGRITY checks are at delta_from_head.diff:511–566.
    - The check added is r_m. The output is 138c2c1a…, and T3:81 equals it by cmp.
    - 634 + 83 (34 + 35 + 13 + 1). See observation 3.
109. T3:84–86, the box's count of 728 = 717 + 11 (14 HF checks for 3 skip lines; 645 against 634). CONFIRMED (gtout:76; RESULTS.md:1606; the first check's item 119).
110. T3:87, "G-VER's launch files restate the count." NOT CHECKABLE (a plan).

TOTALS: 110 items.
- CONFIRMED: 90.
- IMPRECISE: 5 (35, 52, 54, 56, 72).
- FAIL: 1 (13).
- NOT CHECKABLE: 14 (17, 21, 22, 29, 32, 45, 46, 61, 62, 86, 100, 103, 105, 110).

THE SWEEP, in sum:
- The counts are right: 109 (equal to sweep_build by cmp), 20 (equal to sweep_tail:2–21), 6 (equal to sweep_final), 26 (equal to sweep2), and the globs' 18, 88, 65 and 7.
- Bracketed counts give 0 guard-marker words and 0 plain campaign names in the text of every command of spans A (20), B (111), C (6) and D (29).
- No loop or variable in C or D passes a marker-named path.
- The only glob that expands to a marker-named path in C or D is run 4's `cd jl*/.venv/bin` (18:43:04Z), passed to zsh's builtin cd and declared at T1:225–226.
- The commands outside item 1's forms that T1's list does not cover are those listed in items 52, 54 and 56.

OBSERVATIONS
1. T1:32, T2:51, T3:74 and draft 4's module docstring (draft4:242) all cite the seat's raw. That raw is untracked at 9b71bbb and absent from T1's "Committed by path" (T1:299–301), and seat raw:75 (item 5) gives its commit to the coordinating session. The entry could say that commit precedes the BUILD's, so that neither the driver nor the entry cites a file absent at HEAD.
2. Only the hash refusal's text names the INTEGRITY incident (draft4:5187). These carry no such word, though seat §1.4 classes a refusal "on a file's hash or byte count" as INTEGRITY:
   - a missing or symlinked one of the eight ("is not a regular file (GV3)");
   - check_weights_folder's listing and byte-count refusals;
   - ids.load's sha256 and count refusals.

   T1:19–20 is accurate as worded. The seat may want it said that the launch files' reading (T1:114–117), not the REFUSED text, classes those others. It may also want stated whether a missing hashed file is INTEGRITY or a FAIL of the launch.
3. T2:43–45 and T3:73 describe draft 4 as draft 3 plus the hash set. Draft 4 also rewrote the module docstring's gver paragraph (the same lines as item 13), including the PINs' header that now marks GV12 a lower bound. Separately, the seat's §2 expected "one constant and the record's field". Draft 4 also adds a function (gver_hashed_pins), renames a seam and three functions' parameters, and changes refusal wording, 118 lines in and 89 out.
4. "moot" is the seat's §0 word (raw:7), not §1.2's. T1:96 and T2:128 cite §1.2 for it; "(§0, §1.2)" would be exact.
5. The seat's own short form (raw:7) is "runs as Code built it, with two additions and one rule on its ends". T1:33 and T2:52 give "as built, but for GV3's hash set". That matches §2 for the driver; quoting §0 as well would carry the rule on the ends in the seat's words.
6. T1:227's heading, "after the first values-check's window", covers the 17:40:34Z command, which ran while that checker was running (its own observation 13 saw it). The parenthetical "after the brief's hash" is the exact bound.
7. Code's bracketed counts cover only its swept commands. The three after the second sweep's record (18:50:15Z–18:52:20Z) are listed at T1:269–270 but not swept. My counts over them are 0 marker words and 0 plain campaign names, and their loops pass no marker-named path.
8. T3:24 holds one guard-marker word in its text (bracketed: "[j]lens venv's bin folder"). That is harmless in a committed raw. But a later command that carries T3's text in an argv (a heredoc, an echo, a grep pattern) would put the marker there; "the venv's bin folder" would avoid it.
9. Run 4's exit notice lies outside the brief's reads, which are Bash items and tool results. The first checker checked run 3's by reading record kinds and stamps, and declared that read.
10. T1:305's "the PI's N.2": results/raw holds no PI routing raw for the seat's first sitting of 2026-11-22, though the earlier sittings each have one (for example 2026-11-21_third-sitting_pi-routing.md). The PI's words on N.2 are outside the repository at 9b71bbb.

DEPARTURES
1. Three commands misfired harmlessly:
   - an `echo ======` that zsh's `=` expansion stopped after a `cat -n` of the overlay recipe;
   - a `$c:scripts/…` that zsh read as a history modifier ("bad substitution") in a loop over commit ids, re-run with braces;
   - a `cat -A`, not a flag on this system, which printed nothing.
2. I used `sed` as a filter, to mask digit runs and shorten the scratch root in printed output, beside `cut`, `od -c`, `cmp`, `diff` and `tr`. `sed` runs a script language and is not in the brief's list; I declare it for classing.
3. Git forms without item 3's exclusions:
   - `git diff --name-only HEAD`, `git ls-files -o --exclude-standard` and `git log -1 --format` with `valence_core/n` (a non-data folder) as the pathspec;
   - `git ls-files -o --exclude-standard -- results/raw`, counted only;
   - `git diff --name-only HEAD` and `git ls-files` with the quoted pathspec `'data/ol*/manifest.json'` alone. That is a data file named by a quoted glob, so that no marker stood in the argv; it matched one file outside any ckpt or reports folder, and only counts printed.
4. Reads of T beyond its Bash tool_use items and tool results: a census of record types over the whole transcript, the last assistant record's stamp, and the names and stamps (no input) of the tool calls after 18:49:16Z.
5. Twice I printed more of T than a finding needed: the 18:26:59Z output (lines 25–80 of the kit's place script) and the 18:21:38Z output's list of over-width lines. A check of each command's form would have done.
6. Two redundant `jq` runs sent their output to /dev/null, with nothing written. `wc -l` ran on T.
7. Otherwise none:
   - no interpreter ran but shasum and jq;
   - nothing was written and nothing went to the network;
   - no guard marker stood in any argv or command text (bracketed patterns only, quoted);
   - nothing under data/*/ckpt, data/*/reports or data/m[f]3 was read, listed, sized or timed, and the dry gate's line about closed paths was viewed with digits masked;
   - the model manifest was read with the file-reading tool only;
   - in S, only the named files and this brief were read.
```
