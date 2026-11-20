# n — G-CAL-n's run of record (PASS): the blind values-check, as returned, with every disposition

PI date 2026-11-20. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of the commit's two texts:
- T1, the RESULTS.md entry: `b315efe9…313d` (189 lines), with its values-check paragraph and the checker's
  departures as placeholders;
- T2, the launch review's raw, `results/raw/2026-11-20_n-gcal-v1_launch-review.md` here: `0067c8ce…b98f` (217 lines).

**The checker's brief** (`b1e5fef5…f887`, 97 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, the run's files as copied back (the script's output, the exit
  file, the work folder's files, the pod session's record, the smoke's three files and the three outputs of record)
  with the copy-back's hash list, the laptop's decode run, the fifteen raws already staged, the launch files as
  relayed, the launch review's brief and report, Code's notes on its changes before the review, the laptop's hashes
  run, the laptop tests' outputs and Code's sweep of its own commands; in the repository, RESULTS.md (the entries of
  `e3b48ed`, `bc50244` and `0744136`), the PI's routing of the third sitting, the seat's answers of the first and
  second sittings, ADDENDUM-n1 (§1.4) and ADDENDUM-n3 (§3), `scripts/n_sessions.py`, `gcal.py` and `.gitignore`'s
  block for `data/n/gcal/`;
- asked for every factual claim to be checked, the counts over the turns by grep among them, Code's departures
  against the sweep as far as it went, and T2's §3 to be byte-equal to the review's report;
- warned that several sources hold guard-marker words in their content, never to enter an argv;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv, anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the
  named files and the brief itself; and quoted the list of record v2's items 1–5, verbatim.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (263 lines, sha256
`fdd9d848…b8c4`), with one scrub under the list of record's item 7: on its line 191, which lists the strings the
checker counted in the review's report, the scratch root's folder name (`claude-` followed by the user's number) is
written `claude-<uid>`, as the commit gate's scan for local roots requires. §3 as committed is that report with that
one change (sha256 `2f410128…47d3`). The report names scratch files only by their paths inside the scratch folder.

**Totals:** 126 items: 107 CONFIRMED, 6 IMPRECISE, 2 FAIL, 11 NOT CHECKABLE; and 7 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The FAILs:**
  - 43 (T1): the routing's item N.3 has no PASS branch; the form came from G-VEC's entry, whose routed item had one.
    T1's heading is now "**Next** (on this PASS)".
  - 89 (T1): Code's departures missed two breaches of the rule that no guard marker is ever in an argv, both found by
    the checker in Code's first sweep: a loop of five `grep -c -i -F` runs, each with one marker as its pattern, over
    the launch review's report (the sweep's line 98); and a `grep -l -F` for the mistyped digest tail, whose glob over
    Code's memory folder put four file names holding a marker in its argv (line 100; the four confirmed by a
    name-only listing, counted with bracketed patterns so that no marker entered that listing's argv). Both are
    declared in T1 beside the third, which T1 already held, and Code made a second sweep (observation 1); T1's list
    now rests on both sweeps.
- **The IMPRECISE items,** each applied in the checker's words or near them:
  - 13 (T1): `dose_map.json` equals the record's `dose_map` in its five figures; the record's also lists the points;
  - 83 (T1): the first `jq` command's first run went through `awk` to `/dev/null`, and the command printed the
    file's first three and last two lines;
  - 84 (T1): the reads of Code's own transcript are now seven commands with eight `jq` runs, the second sweep's
    among them, one command having run two;
  - 101 (T2): the brief's code list adds `box_e0_corpus.py` and `extract.py`;
  - 112 (T2): every surviving mutant, and every finding but F7, was met before the relay; F7 was not taken;
  - 121 (T2): the Y ranges are Y10–Y16 and Y20–Y29 for M3, 46 mutants in all.
- **The NOT CHECKABLE items** stand: Code's acts and readings and the coordinating session's check (28, 35, 39, 52,
  64, 77, 87, 88, 93, 95), each consistent with its sources where it has one. Item 62 ("each killed by F3's cases")
  is checkable from each Y mutant's harness output in its lane's folder, which names the cases that failed; T2 now
  says so. Code read them for all 46: each fails at least one of F3's cases (the doubled, suffixed and prefixed
  prints; the second end line, alone or on a path; the malformed lines under a counted prefix; the file lines under
  another prefix; the line after the self-test's count; the prefixed zero exposure).
- **The observations:**
  - 1: a second sweep, from `0744136`'s commit time to the sweep itself, made after the check: 221 commands, the
    first 172 identical to the first sweep's; T1's list rests on both;
  - 2: T1 states the scratch metadata plainly: `ls -la` twice, `ls -t` once, `stat -f` in three commands, `du -sk`
    twice, `df -h` once, and `wc -c` once, which the second sweep found beside them; with the unpruned `find`s over
    scratch overlays, none of which holds a ckpt or reports folder;
  - 3: the memory folder holds four file names with a marker, by the name-only listing above;
  - 4: T1 names the three planned raw names the `git check-ignore` runs used;
  - 5: T2's F7 line says the disposition goes to the seat with the run's entry;
  - 6: T1 names the decode's first line, the library's notice that PyTorch was not found;
  - 7: T1's baseline reading names a market and travel (travelers, a terminal, a gate), by Code's own counts over
    the baseline turns (1, 4, 1 and 1; "airport" in none).

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above, and in T1 by its values-check paragraph and the
  checker's departures, which replace the placeholders.
- **The edits, checked by tool:** fixed-string counts over each text unwrapped, for each disposition's new wording
  and each removed wording's absence; T2's §3 byte-equal to the launch review's report; and this raw's §3 equal to
  the values-check's report with the one scrub above: 32 of 32.
- **No second full pass** was made over the texts.
- **The finals:** the entry `fce0e848…4288` (225 lines); the launch review's raw `ef05a89d…d232` (219 lines).

## 3. The report as returned

BLIND VALUES-CHECK: G-CAL-n run entry (T1) and launch-review raw (T2)

Before reading, I checked the hashes. The brief's sha256 is b1e5fef5…f887 and it has 97 lines. T1 is b315efe9…313d (189 lines), T2 is 0067c8ce…b98f (217 lines) and S/step4b/gcal2/launch/review_report.md is 0af5bc8f…1a9a (120 lines). All three equal the brief's values. HEAD is 07441363e6b6… (0744136). These repository files are tracked and clean at HEAD, by `rev-parse HEAD:` against `hash-object`:
- RESULTS.md
- the three named raws
- ADDENDUM-n1-…, ADDENDUM-n3-capture-convention-reward-gate-and-interval-v0_1.md, PROPOSAL-n-bk-reconciliation-v0_2.md
- scripts/n_sessions.py, valence_core/n/gcal.py, .gitignore

Abbreviations used below:
- OUT = S/step4b/gcal2/box/out/gcal_v1_out.txt (401 lines)
- REC = S/step4b/gcal2/box/rec/data/n/gcal/gcal.json
- TURNS = the record's gcal_turns.jsonl beside it
- POD = S/step4b/gcal2/box/out/gcal1_box_run.txt
- SCRIPT = S/step4b/gcal2/launch/gcal_v1.sh
- NOTE = S/step4b/gcal2/launch/gcal_launch_note_v1.md
- SWEEP = S/step4b/gcal2/sweep/cmds.txt (d61882aa…bbfc, 172 lines)
- REPORT = S/step4b/gcal2/launch/review_report.md
- A1 = results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md
- A2 = results/raw/2026-11-19_n-gvec-stop-lock-opens_design-to-code_answers.md
- ROUTE = results/raw/2026-11-19_third-sitting_pi-routing.md

Every hash abbreviation in T1 and T2 was re-cut by tool (cut -c1-8, -c61-64) from the full sha256. All 20 match.

ITEMS

1. T1:1–2, "PASS, every batch generated", run from 0744136. CONFIRMED.
   - OUT:2 (HEAD 07441363…), OUT:380, OUT:391 (five batches, 240 turns).
   - REC status is PASS.
2. T1:2, both hurdles held at +ρ, −ρ and +ρ/2, and every batch is 48 of 48 coherent. CONFIRMED.
   - OUT:371–373 and :392–396.
   - REC figures: coherence_pass and arrival.pass are true at all three doses; coherent is 48 of 48 in all five batches.
3. T1:3, the gate's line. CONFIRMED. `grep -x -F` finds it at OUT:379.
4. T1:3–5, the citations. CONFIRMED.
   - n v0.2 §8 step 8: PROPOSAL-n-bk-reconciliation-v0_2.md:159 ("8. G-CAL-n.").
   - The second sitting's §1.4 (i), §2.5 and §3: A2:31, :47–51, :56–63.
   - ADDENDUM-n3 §3: its lines 32–44.
   - Item N.3 [go]: ROUTE:15.
5. T1:8, gcal_v1.sh f3261901…9d66 ended PASS with exit 0 on emw1e4embiwe9b, run by the pod session on the relay "LAUNCH CLEARED". CONFIRMED.
   - shasum of SCRIPT; gcal_v1.exit reads "exit 0".
   - POD:1, :7, :12, :30.
6. T1:9–12, the last line verbatim. CONFIRMED. Exact match at OUT:401.
7. T1:13, the gate's line at out line 379, "as item N.3 asks". CONFIRMED. OUT:379; ROUTE:15 asks for "the gate's line in the entry".
8. T1:14–20, the four batch lines at 371–374, then "G-CAL-n PASS; the dose map is pinnable" and "run exit=0". CONFIRMED. Exact matches at OUT:371–374, :380 and :381.
9. T1:21, the baseline prints no batch line; it is 48 of 48 coherent with stops cap 48. CONFIRMED. OUT has no baseline batch line; REC figures.baseline.
10. T1:22, gcal.json 4c92f228…bb8f, schema n-gcal-v2, status PASS, pinnable, no early STOP or PAUSE. CONFIRMED. shasum; REC:271, :273, :204, :90–91.
11. T1:22–26, every arrival figure (the baseline's mean, sd and 48 scored; each dose's mean, sd and shift). CONFIRMED digit for digit against REC:99–158.
12. T1:26–27, the gate's batch: span_reward 8f32921fcd1798db at f0.20, alpha 4.397578340790048 = 0.20·R_ℓ. CONFIRMED. REC:182–198, and 0.2 × 21.98789170395024 = 4.397578340790048.
13. T1:28, dose_map.json d4a73b54…efb3 is "equal to the record's `dose_map`". IMPRECISE.
    - The file holds five figures. The record's dose_map also holds the seven points (REC:46–89).
    - The script compares only the five keys (SCRIPT:212).
    - Wording instead: "(`dose_map.json` `d4a73b54…efb3`, equal to the record's `dose_map` in its five figures; the record's also lists the points)".
14. T1:28–30, the figures and the points as printed, none merged. CONFIRMED. dose_map.json; OUT:126; every REC point has "merged": [].
15. T1:31, the exposure line. CONFIRMED. OUT:378.
16. T1:32–33, the steering-check wording and the values 10.60546875, 3.65625 and 8.109375. CONFIRMED. OUT:128, :225, :274.
17. T1:34–36, the smoke ran +ρ and the baseline on the first two prompts, with no −ρ and no gate turn; its batch line. CONFIRMED. OUT:92, :99–103; POD:90–91.
18. T1:36–38, the smoke's record (SMOKE) was checked, its identity equals step 3's, the copy was unchanged, and its three files go in as raws. CONFIRMED. OUT:114–120; NOTE:123–126; staged raws (item 81).
19. T1:39–42, the outputs at their file lines' sha256s and the record's files_sha256; 240 rows, 48 per batch in the record's order. CONFIRMED.
    - OUT:375–377; REC:200–203; shasum.
    - `grep -o '"batch": …' | uniq -c` gives 48 per batch in the order +rho, -rho, +rho/2, baseline, reward_f020.
20. T1:39, "as the BUILD's .gitignore admits them". CONFIRMED. .gitignore:316–324; `git log -n 4 -- .gitignore` shows it was last touched by 89a55c3, G-CAL-n's BUILD.
21. T1:42, the dose map is byte-equal to the smoke's. CONFIRMED. Same sha256.
22. T1:43, O8: fields the script does not check. CONFIRMED. REPORT O8 (T2:197); SCRIPT:219–225 checks none of them.
23. T1:44–50, the provenance values (repo, revision, sha256 36f05404…0fdb, both identifiers, adapter, backend, GPU, capability 9.0, CUDA 12.8, bf16, deterministic, seed, cublas config, window, 64 layers, python, the five library versions, path). CONFIRMED against REC:206–268.
24. T1:45–46, load_ms 29787 is the run's; the smoke printed 29037 ms. CONFIRMED. REC:257; OUT:127, :97; the smoke's gcal.json load_ms is 29037.
25. T1:51–52, the ADDENDUM-n1 §1.4 quote. CONFIRMED. ADDENDUM-n1 line 26.
26. T1:52, "the seat's GC1 puts the raw here". CONFIRMED. A1:61.
27. T1:52–53, the driver's `gcal-decode` at 0744136. CONFIRMED. scripts/n_sessions.py:177 and :2957–3022 print exactly the forms of the decode raw's lines 2–9.
28. T1:53–56, the decode's procedure: run once, in a granted window, at nice 19, HF offline, from a scratch copy of 168 files each checked equal to its blob, with the tokenizer at the three pins. NOT CHECKABLE.
    - SWEEP holds no gcal-decode command; the decode ran after the sweep.
    - decode_run1.exit reads "exit 0", which is consistent.
29. T1:56, the environment quote. CONFIRMED. decode_run1.txt:2.
30. T1:56, "G-DATA's". CONFIRMED. RESULTS.md:3664–3665 and :5711.
31. T1:56–57, the box decoded under transformers 5.15.0 and tokenizers 0.22.2. CONFIRMED. REC:227; POD:68.
32. T1:57–59, the record's two sha256s, the comparison quote, the per-batch "48 under the box's flags, 48 under the laptop's decode", and exit 0. CONFIRMED. decode_run1.txt:3–9; decode_run1.exit.
33. T1:59, the raw holds no difference line. CONFIRMED. None among the 9 lines; the driver prints one per difference (:3018–3021).
34. T1:59–61, the raw: 9 lines, 9e4f41d5…76c3, staged at results/raw/2026-11-20_n-gcal-v1_decode.txt. CONFIRMED. The staged raw has the same sha256.
35. T1:62–64, Code read every turn and every out line; the reading is descriptive and post hoc, with no counter declared. NOT CHECKABLE. These are Code's acts; SWEEP:151–156 print every turn's decode by batch, which is consistent.
36. T1:65, every turn ran to the cap, 80 tokens, with no eos. CONFIRMED.
    - 240 of 240 rows have `"n_tok": 80,` and `"stop": "cap"`; the smoke has 4 of 4.
    - The batch lines show eos 0.
37. T1:65–67, the coherence extremes and their bars. CONFIRMED.
    - grep and sort over TURNS: diversity minimum 0.5692307692307692; trigram_repeat maximum 0.08823529411764708; n_words from 55 to 73.
    - The smoke's turns lie inside these ranges.
    - The bars are in REC's constants and conventions.
38. T1:68–70, "crisp" in 42, 12, 21, 14 and 0 turns. CONFIRMED by `grep -c` per batch; case-insensitive counts are the same.
39. T1:68–74, the descriptions of the batches. NOT CHECKABLE (readings). Counts beside them:
    - +ρ: pine 14, birdsong 8.
    - −ρ: eerie 7, tense 5.
    - The gate's batch: collaborat- 9, innovat- 17, communit- 8.
    - No baseline turn uses the word "airport".
40. T1:71–73, eleven −ρ turns (2, 5, 6, 7, 23, 36, 38, 39, 42, 43, 47) where the speaker says it is an AI; none in the other four batches or the smoke. CONFIRMED.
    - At −ρ: 10 turns with `grep -w AI`, plus 1 with "artificial intelligence" (index 43); 0 elsewhere and 0 in the smoke.
    - Every match is a self-description.
41. T1:75–76, the five slips with batch and index. CONFIRMED by `grep -F` for each slip, matching every batch and index.
42. T1:76–77, four −ρ turns (5, 38, 39, 43) hold a blank line; there is no newline stop. CONFIRMED.
    - `grep -F '\n\n'` finds 4 at −ρ and 0 elsewhere.
    - REC's generation convention says "no newline stop".
43. T1:78, "**Next** (item N.3's PASS branch)". FAIL.
    - Item N.3 (ROUTE:15) has no PASS branch. It ends "…; the run of record; the gate's line in the entry; the record, turns file and dose map to the laptop [go]".
    - The form is copied from e3b48ed's "item N.1's PASS branch" (RESULTS.md:172), where the routed item had one (A2:88, "a PASS → …").
    - Wording instead: "**Next** (on this PASS):".
44. T1:78, the seat reads every turn, GC1 before LOCK-n v0.1. CONFIRMED. A1:61.
45. T1:78–79, LOCK-n v0.1's holes (the dose map, d_eq and d_20), then E and 1 − 0.99^E. CONFIRMED. A1:64.
46. T1:79–81, the R12, F5 and R13 delta after this run; the first sitting's §3; routing item 4's quote. CONFIRMED. A1:50–51 and :82; also A2:61.
47. T1:81, the box stays up and idle (item N.5). CONFIRMED. ROUTE:17; POD:179–180.
48. T1:83–84, the launch files were relayed at their hashes and the launch cleared on the routing. CONFIRMED. POD:2–7, :28–36.
49. T1:84, the script has 388 lines, commit 0744136, driver line 593a140d…a549. CONFIRMED. wc; SCRIPT:56–57; the driver's sha256.
50. T1:85–87, the manifest f958d830…71d6: 63 files, G-VEC v2's 61 plus 2, six of the 61 kept as a superset, each equal to its blob. CONFIRMED.
    - REPORT F4; NOTE:25–32.
    - The box reports 63 of 63 OK (OUT:5–67) in a copy clean at 0744136.
51. T1:87–88, the hashes file 8d9307b0…212a, 13 lines, the laptop's `hashes`. CONFIRMED. hashes_run1.txt is identical and hashes_run1.exit reads "exit 0" (SWEEP:6–7).
52. T1:87–88, "run from a `git archive` … in a battery window of its own". NOT CHECKABLE. The overlay builder is not a named source.
53. T1:88–89, the note a3463cfd…d0ae, 180 lines, stays in scratch. CONFIRMED. shasum, wc; POD:35.
54. T1:90–91, a harness of 604 checks and 166 mutants, all killed. CONFIRMED.
    - test/harness_run11.txt: "604 passed, 0 failed".
    - Three lanes killed 56, 55 and 55 with 0 survivors; every .exit reads "exit 0".
55. T1:91–93, the two Python checks extracted byte for byte, each test run once, the snippets the same bytes in both runs. CONFIRMED.
    - Both runs print "snippets sha256: 1922c60c 103a42a9".
    - The final SCRIPT's heredoc bodies (:158–163, :170–233) hash to 1922c60c… and 103a42a9… by head and tail.
    - SWEEP:47 and :124 show one run each. The battery windows rest on Code's word.
56. T1:93–95, run 1: 57 of 57 checks; of 25 mutants, 20 killed and 5 survived (i, j, o, p, s); exit 1; why each survived. CONFIRMED. snippet_test/run1.txt:59, :68–85; run1.exit; pre_review_notes.md:9–11.
57. T1:95–96, the fix: new fixtures and five more mutants. CONFIRMED. run2.txt:1 shows 59 fixtures against 50; :60–70; :97–101.
58. T1:96–97, run 2 PASS on the final bytes: 69 of 69, 30 of 30 killed, exit 0. CONFIRMED. run2.txt:71, :102; run2.exit; SWEEP:123 asserted the final script hash before the run.
59. T1:98, the review's totals. CONFIRMED. T2:102.
60. T1:99, F1–F6 and F8 applied before the relay. CONFIRMED.
    - SCRIPT:12–15, :18–20, :42–46, :135, :244–247, :287–290.
    - NOTE:94–99, :123–128, :138–139, :159–165.
61. T1:99–100, every member of each class has a mutant of its own, and all were killed. CONFIRMED. test/mutants_gcal.sh:131–176 has 46 Y mutants; all are killed in the lanes.
62. T1:99–100 (also T2:83 and T2:92–93), the mutants were killed "by F3's cases". NOT CHECKABLE. The lane outputs give counts, not case names.
63. T1:100–101, F7 not taken, with its reasons. CONFIRMED. T2:76–78; NOTE:156–157; SCRIPT:250 and :309; the manifest's driver line; SCRIPT:202–206.
64. T1:100, F7 is "for the seat to rule". NOT CHECKABLE. Neither T2 nor the note says it (Observation 5).
65. T1:101–102, O8–O11 met and the rest ask for nothing. CONFIRMED. T2:85–88; NOTE:51–53, :135–136, :148–149.
66. T1:104–105, the sync. CONFIRMED. POD:41–47.
67. T1:106–109, the fresh copy and `command -v awk sed`. CONFIRMED. POD:49–61.
68. T1:110–113, the environment, the two variables from env.sh, and the R6 bridge. CONFIRMED. POD:67–68; REC; OUT:127.
69. T1:114, two loads, 707 of 707 each, 29037 ms and 29787 ms. CONFIRMED. smoke.err and run.err; OUT:97, :127.
70. T1:116, "changed set none" and the manifest 63 of 63. CONFIRMED. OUT:3; 63 lines read ": OK".
71. T1:117–119, the self-test line after two warnings, the laptop's 570 plus the box's 11, and the hashes equal. CONFIRMED. OUT:69–73, :89; SCRIPT:22; RESULTS.md:302–303.
72. T1:121–123, the run's prints in the seat's order. CONFIRMED.
    - OUT:122–381: +ρ at 129–176, baseline 177–224, +ρ/2 226–273, reward_f020 275–322, −ρ 323–370.
    - The order matches ADDENDUM-n3 §4.
73. T1:124–127, the outputs' prints, the record checks, the identity and the changed set. CONFIRMED. OUT:388–390, :398, :400.
74. T1:128–129, smoke.err and run.err hold the "Loading weights" bar alone (out lines 111 and 383). CONFIRMED by `cat -v` and by `cmp` against those out lines.
75. T1:130–131, PID 10656, the PID-only end-wait, and the before-and-after state. CONFIRMED. POD:64, :77–78, :130.
76. T1:132–137, the copy-back details (by name, three-way sha256, no listing, address and port counted, the record copied last, no failed-run folder). CONFIRMED. POD:135–170.
77. T1:137, the coordinating session checked the seventeen files. NOT CHECKABLE. S/step4b/gcal2/box_hashes_relayed.txt (17 entries) is consistent.
78. T1:137–138, Code re-hashed the sixteen and the record 010df890…6568. CONFIRMED. My shasum of all 17 matches POD:146–161.
79. T1:138–142, the `cmp` reads at out lines 69–71, 75–87, 91–108, 122–380, 111 and 383; the identity files; the dose maps; files_sha256. CONFIRMED.
    - `head | tail | cmp` gives all six equal.
    - All three identity and hash files equal gcal_hashes_v1.txt.
    - Both records' files_sha256 equal their files.
80. T1:143–146, the box at the end. CONFIRMED. POD:172–180.
81. T1:147–152, the raws: the fifteen staged in S/step4b/gcal2/commit/raws/. CONFIRMED. Each has the same sha256 as its source; _stage.txt is run.txt and _run.txt is the pod record.
82. T1:154, the pod record states no departure. CONFIRMED. `grep -i 'depart|deviat|breach'` finds nothing.
83. T1:155–160, the `jq` reads of the reviewer's task output. IMPRECISE (minor).
    - SWEEP:79–81 match. But :79 printed `head -n 3` and `tail -n 2` of the scratch file, and its first `jq` piped into `awk` before /dev/null.
    - Wording instead: "the first ran two, one whose output went through `awk` to `/dev/null` and one that wrote the output's last text block, which was "null", to the report's scratch file, then printed that file's line count, first three and last two lines and digest".
84. T1:160–164, "Six `jq` reads of its own session's transcript". IMPRECISE (minor).
    - There are six commands (SWEEP:17, 18, 19, 117, 119, 172), but seven `jq` runs: :119 ran two.
    - Wording instead: "Six commands of `jq` reads of its own session's transcript, seven `jq` runs (one command ran two): five printing …".
85. T1:164–165, one `git status --short` on three paths. CONFIRMED. SWEEP:161; that it printed nothing is Code's word.
86. T1:165–167, three `git check-ignore`, exit status only; G-VEC's entry declared one. CONFIRMED. SWEEP:168; RESULTS.md:241–243.
87. T1:167–169, the post-sweep grep with the five markers, count 1. NOT CHECKABLE (after the sweep). A count of 1 fits the brief, where only line 81 holds the markers.
88. T1:169–171, `hash-object --stdin-paths` and `cat-file --batch-check` over 168 files. NOT CHECKABLE. They are not in the sweep, which ends before the decode.
89. T1:155–171, Code's departures, closed by "Code knows of no others". FAIL.
    - SWEEP:98 holds an undeclared breach of the very rule T1 cites. It is a loop, `for m in <the five markers>; do … /usr/bin/grep -c -i -F -- "$m" "$R" …`, over S/step4b/gcal2/launch/review_report.md. That is five grep processes, each with a marker as its pattern, printing counts.
    - SWEEP:100 is probably a second: `/usr/bin/grep -l -F '0af5bc8f…9a9a' … <Code's memory folder>/*.md`. The memory index lists four file names that hold markers, so the glob would put them in grep's argv. I did not list that folder.
    - Wording instead of "One `/usr/bin/grep -c -i -E` … not an interpreter)": "Breaches of the standing rule that no marker is ever in an argv, each process `grep`, not an interpreter: one loop of five `/usr/bin/grep -c -i -F` runs, each with one guard marker as its pattern, over the launch review's report in Code's scratch, printing five counts; one `/usr/bin/grep -l -F` for the mistyped digest tail whose glob over Code's memory folder put file names holding guard markers in its argv [if a name-only listing confirms]; and, after the sweep, one `/usr/bin/grep -c -i -E` whose pattern held the five markers, over the values-check's brief in Code's scratch, printing a count (1)."
    - And end with: "Code knows of no others; its sweep ends before the laptop's decode."
90. T1:172–182, the launch reviewer's departures. CONFIRMED clause by clause against REPORT lines 107–120 (T2:204–217).
91. T1:185, the seventeen raws. CONFIRMED as a count: 15 staged, plus the launch review's and the values-check's.
92. T1:187, "Nothing ran on a model here." CONFIRMED. decode_run1.txt:1 shows PyTorch was absent.
93. T1:187, the count of 0 at commit time and "Not pushed". NOT CHECKABLE (future).
94. T1:188, the restated Next. CONFIRMED. Consistent with T1:78–81's sources.
95. T2:3, the PI dates and Code as author. NOT CHECKABLE.
96. T2:5–6, one blind pass at 0744136 before the relay. CONFIRMED. REPORT:1, :3; SWEEP:79–81 come before the relay steps.
97. T2:7–8, the reviewed files: gcal_v1.sh 7089e932…634a (383 lines), the manifest (63), the hashes file (13), the note eb8ddb72…b971. CONFIRMED.
    - review_brief.md:9–13.
    - The 383 lines come from the note's prior line, which SWEEP:115's fill asserted before replacing it.
98. T2:9–11, the harness 9eab8f86…5cec and stand-in 120620df…d4f8 (435 of 435); snippet test v2 46eb6c61…f941 (69 cases, 30 mutants); v1 (57 of 57, 20 of 25). CONFIRMED. review_brief.md:15–23.
99. T2:12–13, the template gvec_v2.sh e5f76f5b…c49e and its out raw. CONFIRMED. review_brief.md:24–26.
100. T2:15, the brief 880de004…d511, 121 lines. CONFIRMED.
101. T2:16–20, what the brief named. IMPRECISE.
     - The code list leaves out `scripts/box_e0_corpus.py` and `valence_core/extract.py`, which the brief names (review_brief.md:36–37).
     - Wording instead: "(`scripts/n_sessions.py`'s G-CAL-n section, `gcal.py`, `schema.py`, `gvec.py`, `guard.py`, `ids.py`, `directions.py`, `box_e0_corpus.py`, `extract.py`)".
     - The rest is CONFIRMED (review_brief.md:38–46).
102. T2:21–24, the ten questions. CONFIRMED. review_brief.md:54–86.
103. T2:25–26, what the brief asked for and the rules it quoted. CONFIRMED. review_brief.md:88–121.
104. T2:28–29, the report extracted by `jq`, 120 lines, 0af5bc8f…1a9a, naming scratch files only by their paths inside the scratch folder. CONFIRMED.
     - SWEEP:81 shows the extraction.
     - REPORT holds 0 matches each for /private/, /Users/, claude-<uid> and the home-folder name.
105. T2:31, the totals. CONFIRMED.
106. T2:35, the commit filled, the harness 428 of 428, and G16 killed alone. CONFIRMED.
     - harness_run7: runs_118, "428 passed".
     - mutants_g16_filled: "G16: killed (427 passed, 1 failed)".
     - SWEEP:11, :24.
107. T2:36, the 111-mutant pass before the fill. CONFIRMED. mutants_run1's last line; SWEEP:8 comes before :11.
108. T2:37–39, snippet test v1. CONFIRMED. run1.txt; run1.exit; the snippet hashes. "Released and reported" rests on Code's word.
109. T2:40–42, snippet test v2: nine fixtures, 69 cases, 30 mutants, and the gate's `of == 48` mutated. CONFIRMED. run2.txt:1, :70, :101; pre_review_notes.md:13–18.
110. T2:43–47, C1 and C2; U1, U2, Q1, Q2; smokeexit1 and runexit1; 435 of 435. CONFIRMED.
     - `grep -c flush scripts/n_sessions.py` gives 0.
     - mutants_new4 and mutants_q12b: all killed.
     - harness_run9:20, :49, and its last line.
111. T2:51–52, the relay bytes. CONFIRMED by shasum and wc.
112. T2:52–53, "Every finding and surviving mutant below was met before the relay." IMPRECISE.
     - F7 was not taken (T2:76; T1:100).
     - Wording instead: "Every surviving mutant below, and every finding but F7, was met before the relay; F7 was not taken."
113. T2:55–60, F1. CONFIRMED.
     - SCRIPT:244–247, :287–290.
     - In harness_run11, smokebar, runbar and runwarnmid each end rc 0, PASS.
     - Y56–Y60 are in mutants_gcal.sh:177–181 and are killed.
     - NOTE:94–96.
114. T2:61–62, F2. CONFIRMED. NOTE:123–128.
115. T2:63–67, F3. CONFIRMED.
     - harness_run11 holds 35 dup_/sfx_/pfx_ cases, runendother, runend2 and four more X+runend2 cases, smokedosebad, rundosebad, pauseearly+runpepbad, smokefileother, runfileother and sttrail.
     - NOTE:159–165.
116. T2:68–70, F4. CONFIRMED. SCRIPT:18–20; NOTE:25–32. The part about make_manifest4.sh is not a named source.
117. T2:71–72, F5. CONFIRMED. SCRIPT:12–15; NOTE:138–139.
118. T2:73–75, F6. CONFIRMED. results/raw/2026-11-19_n-gvec-v2_out.txt:94 and :114 (clean) each hold the bar; NOTE:96–99.
119. T2:76–78, F7, including "any two imply the third". CONFIRMED. PBV's regex at SCRIPT:317 has three exclusive alternatives, so the total and two by-name counts fix the third.
120. T2:79–81, F8 and its "no mutant". CONFIRMED.
     - SCRIPT:106, :135.
     - The mutant list has nothing on line 135; G5 is line 136's TMPDIR.
121. T2:82–83, the member ranges "…, Y10–Y29 for M3, …". IMPRECISE.
     - Y17–Y19 do not exist (mutants_gcal.sh:137–153; the lanes' names).
     - The ranges as written sum to 49, while the count is 46 (T2:92).
     - Wording instead: "Y1–Y6 for M1 and M2, Y10–Y16 and Y20–Y29 for M3, Y30–Y46 for M4, Y50 for M5, Y51–Y52 for M6 and Y53–Y55 for M7".
122. T2:83–84, the `gv == "-"` change is equivalent. CONFIRMED. SCRIPT:356–361.
123. T2:85–88, the observations' dispositions. CONFIRMED.
124. T2:89, the reviewer's departures are in the run's entry. CONFIRMED. T1:172–182.
125. T2:91–94, the tests after the review: 604 of 604; 166 mutants in three lanes (56, 55, 55; by name, 46 + 5 Y mutants and 115 others); snippet test v2 69 of 69 with 30 mutants of check_outputs killed, exit 0; run2.txt 6c64636f…38ad, 102 lines. CONFIRMED. run_snippet_test_v2.sh:6 says its mutants are of check_outputs. The window rests on Code's word.
126. T2:96–217, §3 is byte-equal to REPORT. CONFIRMED. `tail -n +98 | shasum` gives 0af5bc8f…1a9a and `cmp` exits 0.

TOTALS: 126 items. 107 CONFIRMED, 6 IMPRECISE (13, 83, 84, 101, 112, 121), 2 FAIL (43, 89), 11 NOT CHECKABLE (28, 35, 39, 52, 62, 64, 77, 87, 88, 93, 95).

OBSERVATIONS

1. The sweep ends at its own line 172, before the laptop's decode (it holds no gcal-decode, hash-object or cat-file) and before the post-sweep grep. For that stretch, "Code knows of no others" rests on Code's word. A second sweep from 172 to the commit would close it.
2. The sweep also shows metadata reads of scratch that T1 does not list: `ls -la` (:14, :107), `ls -t` (:16), `stat -f` (:111, :112, :132), `du -sk` (:87, :88) and `df -h` (:88). None touches the repository's ckpt or reports, so item 2's wording does not cover them. If the seat reads item 1's "name-only ls" as general, they are departures. One plain line in the entry would settle it.
3. Item 89's memory-folder glob should be confirmed by a name-only listing before the entry names it.
4. SWEEP:168 checked `_smoke-turns.jsonl`, not the committed `_smoke-gcal_turns.jsonl`. This is harmless, since .gitignore's non-data rules match neither name. Still, "the raws' planned names" now includes a name that no raw has.
5. T1:100 says F7 is "for the seat to rule"; T2:76–78 and the note do not. One of the two should be aligned to the other.
6. decode_run1.txt:1 is transformers' "PyTorch was not found" notice. T1's account of the output starts at line 2. Naming the notice would also support "Nothing ran on a model here".
7. "airports" for the baseline is a reading: no baseline turn holds the word. The scenes come from travelers (4 turns), a terminal (1) and a gate (1).

DEPARTURES

- One `cat run1.exit 2>/dev/null` run from S/step4b/gcal2/launch. This was a mistyped path (the named file is S/step4b/gcal2/launch/snippet_test/run1.exit), so it was an attempted read of a path in S that the brief does not name. It printed nothing.
- One `git log -1 --format='%h %ci %s'` with no pathspec. It printed an id, a commit time and a subject, which is item 1's form.
- Reads beyond the named repository sources, stated plainly:
  - PROPOSAL-n's §8 (lines 154–162) and a grep of its headings;
  - results/raw/2026-11-19_n-gvec-v2_out.txt lines 94 and 114;
  - .gitignore's non-data rules, and `git log --format='%h %s' -n 4 -- .gitignore`;
  - RESULTS.md lines 1–23, and one whole-file grep for version strings, which printed one line holding a marker word in output only;
  - greps of n_sessions.py and gcal.py beyond the named range;
  - one `git ls-files` with item 3's pathspec and the mf3 exclusion, filtered by grep.
- One `grep -o` context over the −ρ turns printed a fragment of a turn's ids field to my context only. It is written nowhere.
- Otherwise:
  - No interpreter but shasum, and no write.
  - No marker in any argv.
  - Nothing under mf3, ckpt or reports.
  - No listing, find or glob in S.

