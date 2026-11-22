# n — G-TIME-n's run of record (COMPLETE): the blind values-check, as returned, with every disposition

PI date 2026-11-21. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of the commit's two texts:
- T1, the RESULTS.md entry: `ee5ad128…b3f8` (222 lines), with the checker's departures and the values-check's
  paragraph as placeholders;
- T2, the launch review's raw, `results/raw/2026-11-21_n-gtime-v1_launch-review.md` here: `2ad4fd9d…aac7` (404 lines).

**The checker's brief** (`47307a88…5615`, 140 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources by sha256: in Code's scratch, the run's files as copied back (the out file, the exit
  file, the work folder's files and the pod session's record), gread-bench's three files, the launch files and their
  tests, the review's brief, report and dispositions, Code's own log of its departures, the window request, the files
  as the review saw them, and G-CAL-n's builder and script; in the repository, the seat's raw and the PI's routing raw
  of the second sitting, RESULTS.md's Log head, `.gitignore`'s block for G-TIME-n's outputs and `LOCK-n.md`; and this
  session's transcript;
- allowed four copies by digest only (the smoke's report and the three outputs of record), and barred any touch of
  the folder beside the repository where the two steered cells sit;
- asked for every claim checked against its source, each hash abbreviation computed by tool, T2's report byte-equal
  to the review's, the departures (the pod session's, the reviewer's, and Code's against a sweep of its Bash calls
  since `91f0d35`'s commit, by output as well as by command text), leaks, consistency with the seat's raw and the PI's
  routing, and the form;
- barred any interpreter but `shasum` and `jq`, any write, any network, any guard marker in an argv (the Bash
  command's own text included), anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports
  file, and, in Code's scratch, anything but the named files and the brief itself; and quoted the list of record v2's
  items 1–5, verbatim.

**The report** is in §3, as returned: the subagent's hand-back, extracted from its transcript by `jq` (196 lines, sha256
`5a44bb31…b974`), equal byte for byte to the message as this session received it, de-indented. It names scratch files
only by their paths inside the scratch folder, and needs no scrub.

**Totals:** 82 items: 67 CONFIRMED, 6 IMPRECISE, 8 FAIL, 1 NOT CHECKABLE; and 11 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The FAILs,** all omissions from Code's departures in T1, now listed in the entry:
  - 60: the kit's test read the repository's `.gitignore` once for each of its 12 fixture repositories, not once;
  - 62: the memory index: four tail reads, three appends and one `grep -n` with a `sed -n` line print;
  - 63: two `grep -c` processes whose pattern was Q-F3's folder's bare name (and, found by Code's own sweep after the
    check, one more `grep -n -F` with that pattern, to find O9's line);
  - 64: the unpruned finds over the snippet test's fixture and output folders, and the repository find with `-newer`;
  - 65: the `ls -la` of four scratch folders, the further name-only listings, six `wc -c` commands, and the `jq` over
    fixture files;
  - 66: three more process checks;
  - 67: the git forms outside item 1's list or without the pathspec (the BUILD's verify among them);
  - 68: the glob `valence_core/n/*.py` in one grep's arguments.
- **The IMPRECISE items,** each reworded as the report proposes:
  - 28: the driver's sha256 is the DRIVER line's;
  - 31: the stderr files were read as the out raw prints them, byte-equal to the files by `cmp` (O3's list, re-run by
    Code: six of six equal);
  - 52: the record itself was counted on the laptop alone;
  - 58: the coordinating session's class is quoted with its capital and its period;
  - 59: the reviewer's transcript took three `jq` commands, in the words of Code's own log;
  - 61: the "after the run" grouping is gone; the commands are listed by kind.
- **NOT CHECKABLE:** 12. The grant of gread-bench's window reached this session as a queued notice while a command
  ran (the transcript holds it in its attachment and queue records), not as a user record, the kind the check read.
  The entry now rests the window on the coordinating session's close of it, which is a user record of the transcript.
- **The observations:**
  - O1: met with item 12;
  - O2: the fidelity values are no margin, and F2's disposition leaves them unbarred; nothing changes;
  - O3: applied in T1's reading (item 31);
  - O4: applied: T1 carries the commit's line before its "Next" (by path, the home-folder count, nothing on a model on
    the laptop, not pushed);
  - O5: applied: the reviewer's glob in five commands by its transcript, and its manifest `grep -v` run twice;
  - O6: applied through items 59 and 64, and the kit's files among the scratch reads;
  - O7: nothing to do: no note rode the BUILD's commit, so the kit's `note_after` and its awk did not run;
  - O8: answered: the overlay builder (`make_overlay_gtime_v2.sh`, 26 lines), read after the check, passes the
    model's data folder to `git archive` as quoted pathspec globs, which git expands itself, and `tar` writes the
    files; no marker reached an argv. T1 lists its run;
  - O9: applied: T2's head writes `data/m[f]3`;
  - O10 and O11: nothing to do; the raw's claims stand as written, and §2 of T2 discloses mut1's artifact kills.

## 2. The texts changed after the check, and the edits checked by tool

- T1 v2: the dispositions above, Code's departures rewritten by kind, and the two placeholders filled (the checker's
  departures; this check's paragraph).
- T2 v2: one change, O9's.
- The edits checked by tool (`edits_check_v1.sh`, shell and grep only, over the texts' lines joined with one space):
  38 of 38, each new wording present and each old one gone, and T2's §3 still byte-equal to the review's report.

## 3. The report as returned

BLIND VALUES-CHECK: G-TIME-n's run-of-record entry (S/gtime/entry/entry_v1.md) and its launch-review raw (S/gtime/entry/raw_launch_review_v1.md), at HEAD b40ce59

In this report, "cN" means the N-th Bash call in T from 91f0d35's commit time to the call that hashed this check's brief. There are 208 such calls; c208 is the brief's hash.

ITEMS

1. The digests. CONFIRMED. The brief's sha256 matches. So do all 49 named files: the 2 under check, 14 run files, 3 gread-bench files, 18 launch and test files, 9 reviewed copies, the seat's raw and the PI's routing raw (both clean at HEAD). The four digest-only copies match the out raw and the record: smoke/time.json 07f9a152… (record §8), the report 3ae33a39…, the artifact d6d475b7… and the shadow cell 7b7588d6… (out lines 224–225). HEAD is b40ce596f2e4…. Source: shasum and git rev-parse.
2. Headline: "COMPLETE, 18 of 18 reads and the append benchmark", with the projections for the PI's cap at v1.0. CONFIRMED. Source: out lines 206, 207, 212 and 231.
3. Headline citations: n v0.2 §8 step 11; the seat's second-sitting answers committed at b40ce59, on Q1–Q8; item N.3 [go]. CONFIRMED. Source: the seat's raw title and §6; the PI's routing raw N.3; the b40ce59 commit.
4. The report, the shadow cell and the artifact enter the repository; the steered cells sit outside it under item 2 until step 14. CONFIRMED. Source: §1.8; N.2; .gitignore lines 331–343.
5. The script `eeee8c2e…39b6` ended COMPLETE, exit 0, on pod emw1e4embiwe9b. CONFIRMED. Source: the exit file ("exit 0"); out lines 123 and 187; the abbreviation computed by tool.
6. The relay quote "Launch cleared: G-TIME-n, on launch files v2.", as the record quotes it. CONFIRMED. Source: record lines 9–10. The coordinating session's relay notice in T agrees: v2's note with v1's three box files.
7. The last line, verbatim. CONFIRMED. Source: out line 231.
8. The cap's basis quote. CONFIRMED verbatim and by arithmetic: 7680·329 + 3637·344 = 3,777,848; the maxima give 5,880,121. Source: out line 208.
9. The "beside, unused" quote. CONFIRMED. Source: out line 209; the arithmetic checks.
10. Line 210's four quotes (the loads; option (i); option (ii); the three unmeasured terms). CONFIRMED verbatim. 7680·401.586 = 3,084,180.48. Source: out line 210.
11. G-READ-n on the laptop, outside the cap (GT10, §1.5), with Q-F3 beside it and the figure declared high (C.7). CONFIRMED. Source: §1.5; C.7. pgrep at c185 and c201 shows PID 8051 alone.
12. "in a battery window the coordinating session granted at b40ce59". NOT CHECKABLE.
    - Why: no assistant or user record in T holds a grant between Code's request and the run (c199).
    - What supports it: Code's own reasoning just before c199 says the coordinator granted the window at HEAD b40ce59 with PID 8051 alone. The coordinating session's later close message treats the window as granted and confirms HEAD b40ce59 and PID 8051 alone. See O1.
13. The gread-bench quotes and setting: counts and projection; numpy 2.5.1, python 3.12.9, 14 CPUs, 10 calls at each shape; run from overlay91; exit 0; stderr empty; 5 lines; `d1756940…5d6c`. CONFIRMED.
    - Source: S/gtime/gread/gread_bench_v1.txt lines 1, 2 and 5; the .exit and .err files; c56 for overlay91 as 91f0d35's archive; c199.
    - The driver's blob is b00f96eb… at both 91f0d35 and b40ce59.
    - The medians (248.0795 and 88.676 ms) and the maxima recompute exactly.
14. The rate sample: the shadow cell's 31 arrays, by shape and wall-clock, each at its sha256 at both ends. CONFIRMED. Source: record §8 (L33–L63, 31 files); the coordinating session's copy-back notice.
15. Zero negative-pole reads; 12 positive-pole steered reads (+1 and +1/2) on six sessions; the zero line goes into v1.0's §0.4 table. CONFIRMED. Source: out plan lines 166–183; §1.6.
16. COMPLETE is no STOP; the seat recommends a cap in hours; the PI's cap enters v1.0's draft. CONFIRMED. Source: §1.7; N.4.
17. The report `3ae33a39…d8a7`: end_state COMPLETE, three cells, pauses 0, loads_ms [12375]. CONFIRMED. Source: out lines 222 and 224; my digest.
18. The artifact `d6d475b7…2cec` (n-gtime-v1); its report_sha256 is the report's; run.txt's artifact line is its own. CONFIRMED. Source: out lines 211 and 224; record §8; the 91f0d35 entry for n-gtime-v1.
19. The shadow cell `7b7588d6…4c09`, the six d = 0 reads; the report's json_sha256 matches. CONFIRMED. Source: out line 225; plan lines 0–5; record §8.
20. The steered cells `fa823370…10c0` and `63634361…9968`, copied by hash to the folder that note v2 names; the PI's "Yes that is good". CONFIRMED. Source: out lines 226–227; record §8; note v2 lines 205–213; the coordinating session's message accepting the folder. I did not hash these two files.
21. The §1.8 quotation, including "the copy-back's own hash check excepted". CONFIRMED verbatim. Source: the seat's raw §1.8, line 31.
22. Committed by path at step 14's close, with the campaign's cells, before the pod stops. CONFIRMED. Source: §1.8; N.2.
23. The capture arrays stay on the box with their digests in the report; the shadow cell's 31 copies are in scratch and not committed. CONFIRMED. Source: record §8–§9; .gitignore lines 331–336; §1.8 (capture_sha256).
24. The weights: OLMo-2-0325-32B-Instruct at revision b96024342a77, `36f05404…0fdb`, 22 files at the manifest's byte counts. CONFIRMED. Source: out line 162.
25. n's backend identifier 8264f719efd347a9 (window 4096), bridged to 4ed3f2c70fe8afbf (R6). CONFIRMED. Source: out line 187.
26. The identity `879c9602…0cf8`, one for the smoke and the run, under LOCK-n v0.1 `88d9fe7b…e9d5` with C, p0, alpha, the tile, valence and no cap. CONFIRMED. Source: out lines 101, 165 and 220; LOCK-n.md's sha256.
27. LOCK-n v0.1's inputs: `03467e75…53b0` (site 32), `4c92f228…bb8f`, `d4a73b54…efb3`, d_eq and d_20. CONFIRMED. Source: out line 164.
28. "the driver `4616f9c3…2553`, and the package … with its twelve-file closure, as `hashes` printed them". IMPRECISE.
    - `hashes` printed the package and the closure (out lines 80–92). The driver's sha256 comes from the DRIVER line (out line 163, "HEAD's committed bytes").
    - Fix: "the driver `4616f9c3…2553` (the DRIVER line); the package `06b55761…1d39` with its twelve-file closure, as `hashes` printed them and the laptop's file holds them".
29. The box environment: python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0, tokenizers 0.22.2, the two variables from /workspace/env.sh, git 2.43.0. CONFIRMED. Source: record §5; out line 3.
30. Code's reading: the out raw whole (231 lines) and the record whole (240 lines). CONFIRMED. Source: two Read calls in T, with no offset or limit; wc -l.
31. Code's reading of "both stderr files". IMPRECISE.
    - No command or Read in T opens smoke.err or run.err. Their text was read as the out raw prints it; c184 took only their byte counts.
    - The printed lines (out 151–152 and 215–216) are byte-equal to the two files (cmp).
    - Fix: "both stderr files, as the out raw prints them (lines 151–152 and 215–216, byte-equal to the files)".
32. The twelve fidelity values equal the smoke's read for read, each at or below TAU, six of them zero. CONFIRMED. Source: out lines 124–135 and 188–199.
33. The read times: the first read after each load is slowest (952 and 955 ms); the other re-computed reads 639–746 ms; the +1/2 reads 284–391 ms. CONFIRMED. Source: out read lines.
34. The smoke's projection lines (144–146) and their three figures. CONFIRMED. Source: out lines 144 and 146.
35. The stderr contents (the 707-of-707 bar and the crop warning); the self-test's two warnings before its count line, "as at G-CAL-n's run". CONFIRMED. Source: smoke.err, run.err and selftest.txt; out lines 74–76; RESULTS.md's G-CAL-n run entry.
36. The script: 519 lines, its commit 91f0d35, its driver line. CONFIRMED. Source: wc -l; script lines 56–57.
37. The manifest `84550072…957b`: 66 files, G-CAL-n's 63 plus LOCK-n.md, gcal.json and dose_map.json, each asserted equal to 91f0d35's blob. CONFIRMED. Source: wc -l; the diff of the two builders; the builder's header and lines 38–42; the review brief's Q6.
38. The hashes file `a853932b…522b`: 13 lines, from a git archive of 91f0d35, in a battery window. CONFIRMED. Source: wc -l; c134; the coordinating session's grant ("HEAD is 91f0d35").
39. Note v2 `87a1d360…3cd0` (271 lines) carries §1.4, §1.8 and §2; v1's note `036968c0…2369` was superseded before any relay. CONFIRMED. Source: wc -l; note v2 lines 12–16. The coordinating session held v1 and relayed only v2.
40. The harness: 513 of 513, and 513 of 513 again as a null mutant. CONFIRMED. Source: c125's output in T.
41. The mutation pass: 183 mutants, all killed, each by its intended case. CONFIRMED. Source: c121 (184 killed in four lanes); c123 (16 artifact kills, P11 among them); c129 (the 15 re-runs, each killed by its intended case).
42. The Python checks in a window: 95 of 95 fixtures, 62 of 62 mutants, exit 0. CONFIRMED. Source: S/gtime/launch/snippet/run_2.txt; c140 ("exit 0"); the grant.
43. The review: 12 findings (1 BUG, 4 RISK, 7 NIT), 8 surviving mutants, 13 observations; every finding applied, F3 as its first option; every mutant killed or moot. CONFIRMED. Source: the report; the dispositions file.
44. The box before (§2), the sync (§3), the fresh copy (§4) and `command -v` finding all five tools. CONFIRMED. Source: record §2–§4.
45. Two loads, each 707 of 707, at 12365 and 12375 ms. CONFIRMED. Source: out lines 123, 151, 187 and 215.
46. The steps as printed: the copy, the manifest 66 of 66, the self-test quote, the hashes equal, the smoke, the run-of-record lines and the campaign quote, the 15 output checks, the changed set and the benchmark folder removed. CONFIRMED. Source: out lines 2–231.
47. B6, and out lines 150–152 and 214–216. CONFIRMED. Source: the out raw; B6's form as the coordinating session accepted it (101026c) and the seat's §2.
48. The wrapper's PID 12658; the end-wait on the PID alone; before and after, no interpreter job, no compute app, and the GPU at 0 MiB. CONFIRMED. Source: record §5 and §7.
49. The copy-back by copyback13.sh `5bfe8e1f…fcd5`: 47 files and the record, each equal at both ends, no folder listed, nothing removed. CONFIRMED. Source: record §8 lists 47 sha256 lines plus the record; the full sha256 is in the coordinating session's copy-back notice; the abbreviation was computed by tool.
50. What the copy-back took. CONFIRMED. Source: record §8.
51. The smoke's artifact, cells and arrays stay on the box; the artifact's `4cb6b370…2ecf` is on its line in smoke.txt. CONFIRMED. Source: smoke.txt line 52; out line 147; record §9.
52. "The address and port were counted on every text file copied back, first on the box by count_box.sh (`85591293…f61a`) and again in staging". IMPRECISE.
    - Record §8: the box count covered the out part, the smoke's report, the run's report and the artifact. The record itself "was counted on the laptop alone, where it was written".
    - Fix: add "(the record itself counted on the laptop alone, where it was written)", as G-CAL-n's run entry does. The abbreviation was checked against the full sha256 in T.
53. The checks of the copy-back: the coordinating session's 14 OK; Code's `shasum -c`, 14 OK; the shadow cell's digest alone; hashes.txt and the two identity files equal to the laptop's file; nobody touched the steered folder or the arrays. CONFIRMED.
    - Source: the coordinating session's copy-back notice; c184's output, viewed masked (14 OK lines).
    - hashes.txt was compared by cmp; the two identity files by sha256, against the coordinating session's list.
    - No command in range names the arrays or the steered folder after the copy-back.
54. The box at the end (§9); it stays up (C.8). CONFIRMED. Source: record §9; the PI's routing C.8.
55. The raws' names. CONFIRMED in form. They match G-CAL-n's pattern, note v2 lines 218–219, and the two links.
56. The pod session's three departures. CONFIRMED. Source: record §10.
57. Code's listed departures are borne out by T, apart from items 58–61. CONFIRMED:
    - the sed (c12); the statussim repository (c16–c17); the mutation runs;
    - the unpruned find over overlay91 (c56); the ls, the two pruned finds and git config (c117);
    - the three transcript greps (c80–c82); the jq comparison (c90, "equal");
    - the window's 12-grep loop (c136, "12 of 12"), the heredoc (c137) and the two ps calls (c138);
    - the find -newer (c142), stopped by TaskStop with its output empty past its header, then redone with test/ pruned (c143);
    - git status --short (c155); git grep valence_core/n/ (c157); the two existence tests (c163);
    - the kit test, 28 of 28 (c181);
    - c183's git status; pgrep (c185, c201); wc -l and wc -c (c184); git status | grep -c (c201); the six ls (c174, c177, c180, c191, c201).
58. The class quote. IMPRECISE. T has "A per-file loop over a list that holds marker-named paths puts the marker in each process's argv." (the coordinating session's acceptance of v1). The entry lowercases the first letter. Fix: "A per-file loop … argv".
59. The jq over the reviewer's transcript. IMPRECISE.
    - It was three jq commands (c87–c89), not one: a wrong first extraction of its last text block into the report file; that file removed by rm, plus a listing of the tool calls' names and input keys; then the extraction of the hand-back.
    - Code's own log (S/gtime/launch/departures_v2.md line 11) says so.
    - Fix: carry the log's wording.
60. "the test read the repository once, `git show HEAD:.gitignore`". FAIL.
    - The test's mk() runs `git -C "$R" show HEAD:.gitignore` for each fixture repository, and mk runs 12 times (pass, g1–g11). Source: the script as written in T; its one later edit does not touch mk.
    - Fix: "read the repository by one form only, `git show HEAD:.gitignore`, once for each of its 12 fixture repositories".
61. The "after the run" grouping. IMPRECISE.
    - c183's git status, and three of the six ls (c174, c177, c180, the kit's folders), ran while the box ran.
    - They came before the coordinating session's notice that the run had ended. Code's own text at the time says the run was still going.
    - Fix: place them "while the box ran", beside the kit's build.
62. The memory folder. FAIL.
    - There were three `printf >>` appends to the memory index, not one: c9, c120 and c133, each followed by a tail read. With c8, that makes four tails, not "a tail".
    - After the set went out, c153 read the index with `/usr/bin/grep -n` and a `sed -n` line print. That is not in the list. The "six more" sed reads and the "grep -n over two" are the notes alone, and they match.
    - Fix: "three shell appends to the memory index (`printf >>`), each with a tail read; after the set went out, one `grep -n` and one `sed -n` line print of the index".
63. Q-F3's folder by its plain name. FAIL. Besides the sed, two `/usr/bin/grep -c 'mf3'` processes put its bare name in their argv: c12 (over the new builder) and c25 (over the script). Each was also in that Bash command's zsh argv. Fix: list both.
64. Finds omitted. FAIL.
    - c127: an unpruned `find . -type f` over S/gtime/launch/snippet/cases_2, with a shasum per file.
    - c142: an unpruned `find . -type f` over snippet/run_2, which completed before the stuck find -newer.
    - c143: two unpruned finds over snippet/run_2 (`-newer` and plain), counted. The coordinating session's grant says these fixtures' "paths mimic data/n/ckpt and data/n/reports".
    - c144: a find over the repository in item 1's pruned form, with -newer. Code's own log has it (lines 25–27); the entry drops it.
    - Fix: list all four commands.
65. Listings and byte counts omitted. FAIL.
    - c62: `ls -la` of four scratch folders (gtime/launch, its test/ and snippet/, and gcal2/launch), printing sizes, owner and times. test/ holds the harness's fake copies. The 91f0d35 entry declared this kind ("one ls -la over three scratch folders").
    - Name-only ls beyond the eight listed:
      - c4: gcal2/launch, and a `*note*` glob in scratch.
      - c14: run3/frozen, and a `*.sh` glob.
      - c16: the throwaway repository's data/n and data/n/ckpt.
      - c26: gcal2/launch/test twice, and a `test/*.sh` glob to ls and wc -l.
      - c35 and c116: fixture roots, counted; c116 also ran jq over fixture report.json and artifact.json files and took one shasum.
      - c114: a mutation lane folder.
      - c152: reviewed_v1, before the run.
    - `wc -c` in c135, c142, c145, c155 and c167, over scratch files and one committed raw, none under data/. The entry lists only c184's.
66. Process checks omitted. FAIL. `pgrep -l python` in c2, right after the BUILD's commit; `pgrep -f 'newer hashes_run1'` in c143; `pgrep python` in c144. The entry lists only c185 and c201.
67. Git forms omitted. FAIL.
    - c1–c2, the BUILD's verify after its commit. Neither is in the list:
      - kit_verify_v2.sh ran `git cat-file commit HEAD`, `git show HEAD~1:RESULTS.md` and the package digest over the commit's blobs;
      - c2 itself ran `git cat-file commit HEAD`, `git show HEAD:<path>` over six named files, `git diff -U0 HEAD~1 HEAD -- RESULTS.md`, `git log -1 --format='%H parent %P'` and `git rev-parse origin/main`.
    - c63: `git log --format='%h %ad' --date=short -3`, author dates with no pathspec (the 91f0d35 entry declared an %ad log); `git status --porcelain` with the pathspec piped to grep -v, before note v2's; `git show --name-only --format='%h' db00d6d` with no pathspec.
    - c74: `git show --name-only --format=%h fc43249` with no pathspec.
    - c203: `git log -1 --format='%H %cI'` of two commits with no pathspec.
68. A glob in grep's arguments. FAIL. c104 ran `/usr/bin/grep -n … scripts/n_sessions.py valence_core/n/*.py`, which expands to the 16 package files, none with a marker. The entry lists this kind for the reviewer only.
69. The launch reviewer's departures. CONFIRMED against its report's DEPARTURES section (report lines 249–264). See O5.
70. The raw's tail. CONFIRMED.
    - The raw has 404 lines; lines 141–404 are byte-equal to S/gtime/launch/review_report_v1.md (cmp; bba5bb47…8c06).
    - That file also equals the reviewer's one SubagentHandback message in its own transcript, by sha256.
71. The raw's head on what was reviewed. CONFIRMED.
    - The script `1418ea82…d203` (427 lines); the manifest (66 lines, unchanged since).
    - The builder `6fe3871e…9d01` is `3831b530…4e17` with three files added and Q-F3's folder bracketed (diff).
    - The draft note `cc978e1a…3215` (172 lines), with its five slots unfilled.
72. The raw's head on the tests as they then stood. CONFIRMED.
    - The harness and stand-in (`ed322ae1…9333`, `49f14328…4ee1`): 389 of 389 (c48).
    - The mutation pass `6a4f2850…c6a8`: 124 mutants, lanes 42+41+41.
    - The snippet test v1 (`c2f886e0…a3f5`, `fee3c682…01cf`): 51 cases and 40 mutants, not run.
    - The template `f3261901…9d66`.
    - Source: the review brief lines 10–37; report F1; T.
73. The raw's head on the brief `a5b070fd…ae54` (158 lines): what it named, the routing it quoted (B1, B2 and B6, the copy-back in (ii), the box's three items), its eleven questions and its rules. CONFIRMED. Source: review brief lines 7–158. See O9.
74. "264 lines, sha256 bba5bb47…8c06; names scratch files only by their paths inside the scratch folder". CONFIRMED. Source: wc -l; the report uses S/step4b/… throughout.
75. The totals line. CONFIRMED. Source: report line 9; F1–F12, M1–M8, O1–O13.
76. The raw's §1 against the dispositions file. CONFIRMED. diff shows only the heading forms, the moved "reviewed_v1/" clause, and F3's "a v2" reworded as "a next version of the files".
77. The raw's §2 on the harness and the mutation pass: 513 of 513 twice; 184 mutants; 16 artifact kills; mut1's 15; 15 re-run; P11 equivalent; 183 in all. CONFIRMED. Source: c121, c123, c125 and c129 outputs; the dispositions file lines 87–99.
78. The raw's §2 on the snippet test v2. CONFIRMED.
    - It ran in a window granted at 91f0d35, after `hashes`: 95 of 95; identity_of's three lines; 62 of 62; exit 0; output `14816ff4…636d`, 67 lines.
    - m32 was killed by a_ccells; "left declared" is the coordinating session's word ("m32: stays declared").
    - Source: S/gtime/launch/snippet/run_2.txt; c140; the grant; the coordinating session's acceptance of v1.
79. The raw's §2 on `hashes`: 13 lines, exit 0, stderr empty; the twelve closure lines are LOCK_CLOSURE's pins and the package line is LOCK_PACKAGE_SHA256. CONFIRMED. Source: c135; my grep with the 13 digests as stdin patterns found each once in the driver (lines 3776–3777 name the constants).
80. Leaks. CONFIRMED.
    - The entry and the raw's head (lines 1–140) hold no local root, no user name, and no session or agent id.
    - They hold no IPv4 string and no pod address or port. The only port-like strings are "A-n2:40" and ":4096:8".
    - They hold no margin, log-probability or cell content. See O2.
81. Consistency with the seat's raw (§1.1–§1.8, §2) and the PI's routing (N.1–N.4, C.6–C.8, D.9). CONFIRMED.
    - Nothing in the entry contradicts them.
    - What they ask the entry to carry is carried: the projections (§1.7); the zero line (§1.6); gread-bench's stdout as a raw (§1.5); the rate sample, declared descriptive (§1.4); the outputs and the steered cells as ruled (§1.8); the smoke's report, identity and out file as raws (§2).
    - GT15: no start or finish stamps appear in the entry. See O4 on D.9.
82. Form. CONFIRMED.
    - One top-level bullet, "- 2026-11-21 — **…**", with nested bullets four levels deep.
    - Bold markers (24) and backticks (346) are balanced; the two links are relative results/raw/ paths.
    - The file ends ".\n\n" (a blank last line), and no line runs over 120 characters.
    - Only the @DEPVC@ and @VC@ slots remain.

OBSERVATIONS

O1. The gread-bench grant's text is in no assistant or user record of T. It may have reached Code in a record type this check does not read. Quote or commit it from wherever it arrived if the entry keeps "granted at b40ce59".
O2. The entry ("six of them are …") and the out raw carry per-read fidelity values, including the six steered +1 reads (out lines 130–135 and 194–199). Fidelity is not a margin and stays unbarred under F2's disposition. It is flagged only because §1.8 otherwise keeps the steered cells closed.
O3. selftest.txt, hashes.txt, smoke.txt, run.txt, smoke.err and run.err are each byte-equal to their lines in the out raw: 74–76, 80–92, 96–148, 161–212, 151–152 and 215–216 (cmp). All are committed as raws. Rule 25's read could say so, as G-CAL-n's run entry did.
O4. G-CAL-n's run entry ends with "Committed by path …; the commit-time count of the home-folder prefix …; Nothing ran on a model here. Not pushed." This entry has no such line. D.9 leaves the push the PI's, behind the screen.
O5. The reviewer's transcript shows the `valence_core/n/*.py` glob in five commands, not the six its report states. Its one manifest `grep -v` command ran grep -v twice: once into `shasum -c -`, once into `wc -l`.
O6. Code's own log (S/gtime/launch/departures_v2.md) has three items the entry drops or shortens: the repository find with -newer (item 64), the jq detail (item 59), and the kit-file reads in scratch (log line 39).
O7. c1's kit_verify_v2.sh sources kit_lib_v2.sh, whose note_after() runs awk when a note rides. NOTE_FILE was unset; its output has no note clause, so no awk ran.
O8. c56 ran make_overlay_gtime_v2.sh. That script is not a named file, and its text is not in T's tool inputs. Whether its git commands' argv named a marker path (overlay91 holds the adapter and the model's data folder) is not checkable here.
O9. Raw head line 34 writes Q-F3's folder plainly (`data/mf3`); the brief it describes writes `data/m[f]3`. Committed texts do write the plain name elsewhere, but the bracketed form would match the brief and the report.
O10. The snippet test v2 has no m37 (v1's dropping of "pick" from BARRED), and its header does not declare that. b07 (killed by a_bar_pick) meets its aim. The head's claim about m28 is true as written.
O11. Before the review, mut1's "124 mutants, all killed" (as the brief and the raw's head state it) included 15 kills by the same harness artifact: G4, G15, G24, G30, S8, Q11, G10, G16, G25, P11, G11, G14, G23, S7 and R2 (c123). The raw's §2 discloses this. mut2, the pass of record, killed S7, S8, Q11, G11 and R2 by other cases.

DEPARTURES

- Three redirects to devices: jq output and a `head -n 140` sent to /dev/null (leftover no-ops in two commands), and one jq pipeline through /dev/stdout. No file was written.
- Two here-documents (hash-abbreviation loops) and process substitutions in two diff commands, which zsh may back with temporary files or pipes.
- One `git grep -n -E` with the pathspec `-- '*.md' ':!data/**' ':!results/**'`: item 3's `':!data/**'` form, not the brief's named pathspec.
- Two `git log` runs with `--format` of ids, subjects and commit times (one piped to cut), without the pathspec.
- A name-only `ls` of the subagents' transcript folder, counted by wc -l, and a glob `agent-*.jsonl` there, to find the transcripts beside T.
- `sed` for line prints and masking, with `cut`, `od`, `cmp`, `diff`, `tail`, `head`, `wc`, `sort`, `uniq`, `tr` and `paste`. None of them is in the brief's list of interpreters; stated plainly.
- An environment assignment named `awk_free=1` before one `cut`, a slip. No awk ran, but the word was in that zsh's argv.
- One grep of S/gtime/launch/reviewed_v1/run_snippet_test_v1.sh for m36–m38, to support an observation (O10) rather than a claim the raw makes.
- The user's name as one alternative in a leak-count grep pattern.
- jq over T and the reviewer's transcript, assistant and user records only. This covered tool results of selected commands, with outputs bearing on fake or closed folders viewed masked; Code's Write inputs for the kit; and one user record after the sweep window (the coordinating session's gread-bench close), as a source for item 12.
- Nothing else: no interpreter but shasum and jq; no file written; no network; no marker or plain campaign name in any argv; nothing listed, read, sized or timed under data/*/ckpt, data/*/reports, data/m[f]3, S/gtime/box/rec, smoke or arrays beyond the four digests; nothing done to the folder beside the repository.

82 items, 67 CONFIRMED, 6 IMPRECISE, 8 FAIL, 1 NOT CHECKABLE, 11 observations
