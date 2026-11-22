# n — the supplement to G-VER's seven starred readings: the blind values-check, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was checked.** One blind pass by a subagent over two drafts, at HEAD `d92500b`:
- T1, the supplement, sha256 `a482ee24…a2ae` (106 lines);
- T2, this commit's entry, `ce2743a4…ef1a` (38 lines), its values-check and checker's-departures lines placeholders
  not to be checked.

**The checker's brief** was given to the checker as its prompt: Code's scratch file `S/step4b/gver/supp/vc_brief.md`
(`e307db0a…e639`, 81 lines). It:
- named the texts and the sources. In the repository, the files the texts cite, at `d92500b`, each checked tracked and
  clean. In Code's scratch, by name and sha256 only: the BUILD's blind review of draft 1, and draft 2 of the driver;
- asked for every factual claim to be checked: each number, hash, path and line citation; each quotation against its
  source; what the code at `d92500b` and draft 2 do; and what the review says;
- allowed `shasum` by name. It barred any other interpreter, any write, any network, and any guard marker in an argv:
  a path, a grep pattern, a variable or glob that expands to one, a loop that passes one, and the command's own text
  included. A file whose path holds a marker was to be read with the file-reading tool only;
- barred anything under `data/m[f]3`, any whole-tree git status, any read, listing, size or time of a ckpt or reports
  file, and anything in Code's scratch but the named files;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (204 lines, sha256
`0a43cfad…8933`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 62 items: 43 CONFIRMED, 4 IMPRECISE, 1 FAIL, 14 NOT CHECKABLE; and 12 observations. Code counted them
again by tool, from the first verdict on each item's line.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words or the words below. Every observation is
applied but the sixth, which is for the BUILD's next draft. §2 gives the edits and their check by tool.

- **Item 12 (FAIL), T1:15–16.** Applied: the line takes the first half of the checker's wording, and F5 goes with the
  five, as the item's last sentence and observation 1 offer.
  - The line now names the driver's items as F1, F2, F6–F9, F11, M1–M17 and B2, and F10 as the `.gitignore`'s. It
    says the BUILD's commit gives each of the review's other items its disposition.
  - F5 is carried with the five, as a sixth. §1.6 gives G-VER's ends as the launch will read them, with Python's exit
    2 when it cannot open the script (the review's F5) beside the usage errors. §0 and the title name it, and the
    entry says Code added it here.
- **Item 3, T1:8.** Applied in the checker's words, as two sentences.
- **Item 25, T1:54–55.** Applied in the checker's words: the quote holds "(R:2889–2891; R:1845–1847)".
- **Item 32, T1:77.** Applied in the checker's words.
- **Item 36, T1:81–82.** Applied in the checker's words, then extended by observation 5: the review did not check the
  file (ids:69), and Code has read it since.
- **O1.** Applied with item 12.
- **O2.** Applied: §1.1 says no kernel runs, but building the provenance makes a CUDA context, through
  `get_device_name` (drv:694; the review's O7).
- **O3.** Applied: §1.5 says the quote's B7 is G-TIME-n's own review's, and the cited forms say the F, O and B numbers
  are this review's "unless a quote says otherwise".
- **O4.** Applied: §1.5 gives the old record's standing as Code's reading, with the seat's "the figures stand for the
  box they ran on" (ans21b:27) as the analogy, and says Q6's added clause asks it.
- **O5.** Applied.
  - `S/tok_n`, the tokenizer folder the ids' renders used, holds the three files alone. Each is at the model
    manifest's `olmo2_instruct` pin: shasum, against the manifest's lines 252, 256 and 260.
  - Its `tokenizer_config.json` names `"tokenizer_class": "GPT2Tokenizer"`. §0, §1.4, Q2's clause and the entry say
    so.
  - Code has not traced transformers' load further, so `vocab.json` and `merges.txt` stay with Q2.
- **O6.** Not applied here: the line is draft 2's. The BUILD's next draft fixes it, with its own self-test window
  first, and the supplement says so where it names draft 2.
- **O7.** Applied: §1.3 names `ids.load`'s schema, form and base checks (ids:308–315) beside its file checks
  (ids:317–327). Q4's clause reads "a MANIFEST.json that `ids.load` refuses (ids:301–327)".
- **O8.** Applied: §1.1 names Python, accelerate, safetensors and huggingface_hub too (drv:687–698).
- **O9.** Applied: the BUILD is "in the driver alone, with the `.gitignore` lines that admit the record".
- **O10.** Applied: the supplement and the entry name the BUILD's commit and the launch files' relay to the box beside
  the seat's answers (B:271–272).
- **O11.** Applied: the title says "clauses added to Q2, Q4 and Q6", §0 says "Three items for the questions" and "the
  five clauses", and the entry says "the five clauses".
- **O12.** Applied: the cited forms name draft 2's file and sha256 (`3df537d6…83c1`).

**Beside the checker's items, edits of Code's own:**
- **Draft 2's self-test** has run since the check: 716 of 716, in its own battery window. The supplement and the entry
  say so, in place of "requested".
- **The stale docstring line** (observation 6) is named where the supplement names draft 2, with the later draft that
  fixes it.
- **`S/`** is defined in the cited forms.
- **§1.6 quotes** draft 2's `run_gver` last lines, and names its other ends: the usage errors and Python's exit 2
  before the stage runs, and the exceptions `run_gver` does not catch.
- **§1.4 adds** that the renders loaded the tokenizer from the three files alone, under transformers 5.5.0, the only
  environment they run in (ids:68, :113–114). The review's O5 says the laptop's render used "a folder of the three
  files alone".
- **"Other findings"** became "other items", since the review's other box risks and observations are neither the
  driver's nor in the line's list.

## 2. The edits, checked by tool

The edits were made to new versioned copies of the two drafts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/gver/supp/edits_check.sh`. The results are byte for byte the revised drafts, so nothing else changed after
the check:
- the supplement, 22 of 22 edits; the entry, 5 of 5.

The entry's five include its two placeholders, filled with this check's summary and the checker's departures. After
the edits, one placeholder was filled by tool: the entry's count of these edits.

## 3. The report, as returned

```text
VALUES-CHECK: the G-VER starred-seven supplement (T1) and its RESULTS entry (T2), at HEAD d92500b

SETUP
- All four sha256s are as briefed (shasum), and so are the line counts (wc -l): T1 S/step4b/gver/supp/supp_src.md a482ee24…a2ae, 106 lines; T2 S/step4b/gver/supp/entry_src.md ce2743a4…ef1a, 38 lines; S/step4b/gver/review_report.md 3bb14a39…411d, 164 lines; S/step4b/gver/draft2/n_sessions.py 3df537d6…83c1, 6,195 lines. Draft 2's new section runs from 5125 to 6048 (`def _parse_rulings` is at 6049).
- HEAD is d92500b. Each cited repository file passes `git rev-parse HEAD:<path>` = `git hash-object <path>`: the block, LOCK-n.md, scripts/n_sessions.py, valence_core/m/resume.py, valence_core/n/ids.py, ans21b, CLAUDE.md and RESULTS.md. `git diff --name-only HEAD` with item 3's pathspec and the campaign exclusion lists 0 files.
- Hash abbreviations were made with cut.

ITEMS

1. T1:1 (with :33–34), the title "GV4's pins corrected and added to, and three additions to Q2, Q4 and Q6, from the BUILD's review". CONFIRMED. F3 corrects B:141–142 and F4 adds the tokenizers pin. §2 (T1:98–106) adds clauses to Q2, Q4 and Q6 only. §0's "three additions" are O3, O5 and B7 (T1:33). "Nothing else in the block changes" is Code's own statement. Observation 11 covers the count.

2. T1:3–5, the block results/raw/2026-11-22_n-gver-starred-seven_code-to-design_STOP.md is committed at d92500b. CONFIRMED. `git log --format` over the path gives d92500b alone, and the file is clean. "Stays as committed" is a plan.

3. T1:8, "The block's seven readings … (Q1–Q7), are with the seat." IMPRECISE. The seven readings and Q1–Q7 are right (B:1, B:289–308). But T2:7–9 says the PI was asked to hold the seat's nudge so that one nudge carries cd6b30d, d92500b and this supplement. So the block is committed for the seat but is not yet with it. Suggested wording: "*The block's seven readings, GV1, GV4, GV6, GV9, GV11, GV13 and GV14 (Q1–Q7), are committed for the seat at `d92500b`; the seat's nudge is held so that it carries this supplement too.*"

4. T1:9, "drafted on GV1–GV16 as PINs, in the driver alone". CONFIRMED in GV2's sense. Draft 2's docstring says so at 238–242, and its GV2 line (263) reads "in the driver alone: valence_core/n/ unchanged". B:15–16 uses the same words. Observation 9: the BUILD also carries a .gitignore block.

5. T1:9–10, "Draft 1's self-test ran 687 of 687 in a battery window the coordinating session granted." NOT CHECKABLE. The review's count, made by reading the code, agrees: 53 added checks, 634 + 53 = 687 (review:11), and 634 is G-TIME-n's BUILD count (ans21b:41). None of the sources records the run itself or the window.

6. T1:10–11, the review's file, sha256 3bb14a39…411d and 164 lines. CONFIRMED (shasum, cut, wc -l).

7. T1:11, "found one BUG and six RISKs". CONFIRMED. F1 is the BUG (review:15). F2–F7 are the RISKs (review:21, :30, :37, :43, :50, :55). The review also has NITs F8–F11, mutants M1–M17, box risks B1–B8 and observations O1–O7.

8. T1:11, "Draft 2 carries the fixes". CONFIRMED for the driver's fixes, by spot check of draft 2:
   - F1: the write is inside the cleanup (5290–5307), tested at 5700–5709.
   - F2: _gver_loaded (5360–5369).
   - F3: 5388–5389.
   - F4: 5141, 5253 and 5418–5419.
   - F6: the production seams are now called (5937–5941, 5961, 5963–5968) and the seam check covers them (5997).
   - F7: kills for M1–M10 (5641–5653), and M7 also at 5664–5668 and 5816.
   - F8: 5695. F9: "this run wrote no record" (5476). F11: "a lower bound" (5138–5139, 5480).
   - M16: 6017–6022. M17: 5804. B2: 5572–5573.
   F5's fix belongs to the launch files (review:48). F10's belongs to the .gitignore (review:66), which was not among my reads.

9. T1:12, "The BUILD is not yet committed." CONFIRMED. HEAD is d92500b, the driver last changed at 91f0d35, and no path under data/n/gver/ is tracked (git ls-files: 0).

10. T1:12–13, the BUILD's commit will carry the report whole, with every disposition. NOT CHECKABLE (a plan).

11. T1:14–15, the five items: F3 and F4 in GV4, O3 for Q4, O5 for Q2 and B7 for Q6. CONFIRMED that each exists and is as described: F3 (review:30–35), F4 (:37–41), O3 (:145, "worth stating with Q4"), O5 (:149, "For Q2"), B7 (:113–115; Q6 is GV13's question, B:306). That these five are all the items that change what the block tells the seat is Code's reading; see observations 1 and 2.

12. T1:15–16, "The review's other findings are the driver's (F1, F2, F6–F11, M1–M17 and B2)". FAIL.
   - F5 is a RISK (review:43–48): exit 2 is not unique to G-VER's STOP, because argparse's ap.error exits 2 with no record, and uncaught exceptions end exit 1 with a traceback. F5 is neither among the five nor in this list, and its fix belongs to the launch files, not the driver. Draft 2 keeps F5's ground: main() sends every option given to gver to ap.error (draft 2:6096–6098).
   - F10 concerns the .gitignore's comment (review:66), not the driver.
   Suggested wording: "The review's other findings are the BUILD's: F1, F2, F6–F9, F11, M1–M17 and B2 the driver's, and F10 the `.gitignore`'s; and F5 is the launch files' (with B5): exit 2 is also argparse's usage error, with no record, so the launch reads each end by its exit code, its last line and the record's presence together." Or carry F5 with the five (observation 1).

13. T1:16, "they change no reading, GV5's exits stand, and the BUILD's entry declares them". NOT CHECKABLE (Code's reading and a plan). As built, run_gver's exits are GV5's (draft 2:5448–5457 and :5474–5488), but main()'s usage errors exit 2 with no record (item 12).

14. T1:17, "G-VER runs only after the seat's answers on Q1–Q7, with this supplement's additions." NOT CHECKABLE (Code's statement). It is consistent with B:271–272, which also names the BUILD's commit and the launch files' relay.

15. T1:19–23, the cited forms. CONFIRMED.
   - B is the block at d92500b.
   - L is LOCK-n.md: L:1 and L:3–4 read "LOCK-n v0.1", and its sha256 is 88d9fe7b…e9d5.
   - scripts/n_sessions.py is the same blob at 91f0d35 and at HEAD (git rev-parse), sha256 4616f9c3…2553.
   - The resume and ids paths are as stated, and ans21b is the path at B:35.
   Observation 12 covers draft 2's citation form.

16. T1:29 and :39–40, B:141–142 under "Not held": "cuBLAS's setting and numpy's stream known answer, since nothing runs on the GPU and nothing is drawn". CONFIRMED. The quote is verbatim from B:142, without its list dash and closing semicolon.

17. T1:41–42, environment_provenance (drv:676–698) puts CUBLAS_WORKSPACE_CONFIG into the provenance (drv:696). CONFIRMED. The function runs from 676 to 698, and line 696 reads `"cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG")`.

18. T1:42–43, backend_identifier hashes every field but n_encodes_clipped, path and seed (resume:147, :239–242). CONFIRMED. BACKEND_DROP is at resume:147. The def and the filtered body are at 239–242, and the hash follows at 244–245.

19. T1:43–44, both identifiers (4ed3f2c70fe8afbf and 8264f719efd347a9) fail on another setting, and on another torch, transformers, numpy, GPU, CUDA or capability. CONFIRMED. bridge_identifier replaces only choice_window_declared (drv:701–706). Both checks run before a load (drv:4264–4270). The constants are at drv:586 and drv:3774, and the fields are at drv:687–698. The list is partial (observation 8).

20. T1:44–45, L §17 pins the setting :4096:8 (L:767–768). CONFIRMED (L:767–768; §17 is L:746–774).

21. T1:46–47, under draft 1 an unset setting refuses at R6, with exit 1, no record, and a message naming R6, not cuBLAS. CONFIRMED against F3 (review:34). Draft 1 is not among my reads. "No record" follows GV5's refusal path (B:202–204), as draft 2's run_gver shows (5453–5457). Draft 2's R6 message (5411–5413) names R6 alone.

22. T1:29–30 and :48–50, draft 2 adds G-TIME-n's rule-2 check by name (drv:4230–4231), after the pod and before the STAGE line, with the quoted message, ending exit 1 with no record. CONFIRMED.
   - drv:4230–4231 is G-TIME-n's check; its pod check is at 4224–4229.
   - Draft 2:5388–5389 has the message verbatim, after the pod check (5382–5387) and before STAGE (5390).
   - On a refusal, run_gver prints the REFUSED line and returns 1 having written nothing (5453–5457).
   - The self-test cases cublas-other and cublas-none expect exactly this (5840–5841, 5869–5876).

23. T1:50, "The launch files export the setting, as G-TIME-n's did." CONFIRMED for G-TIME-n; G-VER's launch files are a plan. G-TIME-n's launch command sourced /workspace/env.sh, which carried CUBLAS_WORKSPACE_CONFIG=:4096:8 (results/raw/2026-11-21_n-gtime-v1_run.txt:77, :81). So the mechanism is the box's env.sh, sourced by the launch.

24. T1:51, numpy's stream known answer is still not held. CONFIRMED. Draft 2's _gver_prepare (5372–5438) does not call stream_known_answer, while G-TIME-n's preparation does (drv:4232–4234). Draft 2's docstring agrees (267–268).

25. T1:54–55 (with :31), the quote of L:767–768 with "pinned …:". IMPRECISE. The "…" stands for "(R:2889–2891; R:1845–1847)", and that elision is outside the brief's allowances (line wrapping and markup). The claim at T1:31 that L §17 pins tokenizers 0.22.2 stands. Suggested wording: `- **L:767–768:** "The environment of n's runs on the box, pinned (R:2889–2891; R:1845–1847): python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0, tokenizers 0.22.2; `CUBLAS_WORKSPACE_CONFIG` `:4096:8`".`

26. T1:56–58, the decode runs in tokenizers' backend, and library_versions are the six libraries (drv:687), without tokenizers. CONFIRMED. drv:687 lists exactly those six. The decode's backend is F4's statement (review:39), not tested here.

27. T1:59–60 (with :31), draft 1 recorded the version and held nothing; the review reads that as unsound against L §17, while noting that verify's decode equality would still catch a change. CONFIRMED (review:37, :39, :40).

28. T1:61–65 (with :32), draft 2's LOCK_TOKENIZERS = "0.22.2" is held before G-VER and in check_gver. CONFIRMED.
   - Draft 2:5141 sets the constant.
   - 5417–5419 refuse another version before G-VER, giving exit 1 with no record.
   - check_gver's environment clause requires 0.22.2 (5251–5254); a record failing it ends "FAILED at the record …; this run wrote no record", exit 1 (5474–5478).
   - The self-test case "tokenizers" covers it (5860–5861).
   "Adds a pin" is Code's statement. Observation 6 notes a stale docstring.

29. T1:68–69, the block's correction (B:134–139) sends a MANIFEST.json off its pin to verify, which ends as G-VER's STOP with the record. CONFIRMED. Draft 2 prints "not equal, one of G-VER's causes (L:543)" and does not refuse (5407–5409). verify's own pin check makes its status STOP (B:138), the record's manifest.equal is false (5189), and the run exits 2 with the record (5486–5488).

30. T1:70–72, ids.load checks each file against MANIFEST.json's sha256 and record count (ids:301–327) before verify; a folder whose files and manifest disagree is a refusal (exit 1, no record) and one of Q4's refusals. CONFIRMED. The docstring is at ids:302, and the checks at ids:317–327 raise SystemExit for an absent file, a wrong sha256 and a wrong count. Draft 2 loads the ids at 5406, before verify at 5462. B:202–204 and Q4 (B:299–302) cover it. Observation 7: ids.load refuses on more than this.

31. T1:73–75, in draft 2 the loaders' own exceptions are refusals on REFUSED lines, and this is the review's F2 fix. CONFIRMED. _gver_loaded converts ValueError, KeyError, OSError and TypeError into SystemExit (5360–5369) for both loaders (5405–5406), so each reaches the REFUSED line (5455). F2 is at review:21–27, and the self-test covers it at 5849–5856. "Declared in the BUILD's entry" is a plan.

32. T1:77, the heading "1.4 For Q2 (GV3)". IMPRECISE. Q2 is GV4's question (B:291; T1:99); GV3's hash check is only its sub-question (B:295–296). Suggested wording: "**1.4 For Q2 (GV4), on GV3's hash check: what the tokenizer load may read (the review's O5).**"

33. T1:78–79, B:295–296 asks whether GV3's hash check should cover vocab.json and merges.txt. CONFIRMED.

34. T1:80, the instruct folder's 22 files include config.json. CONFIRMED. The model manifest's instruct entry (read with the file-reading tool; clean at HEAD) lists 22 files with n_files 22, including config.json, merges.txt and vocab.json, under /workspace/models/. L:772 also says "22 files".

35. T1:80–81, the review recalls that AutoTokenizer reads config.json only when tokenizer_config.json names no tokenizer class. CONFIRMED (review:149).

36. T1:81–82, "It did not check that file on the box, and neither has Code." IMPRECISE. The review says only "I did not check that file" (review:149), with no "on the box". tokenizer_config.json is one of the three hashed files (ids:69), with pinned bytes. Whether Code has checked it is not checkable. Suggested wording: "It did not check that file (one of the three hashed, ids:69), and neither has Code."

37. T1:83–84, every file is checked by byte count before G-VER (drv:636–649), and respawn step (i) re-hashes them all. CONFIRMED. weights_of_record calls check_weights_folder (drv:663). Draft 2's weights seam is weights_of_record (5353), called at 5392 before G-VER. CLAUDE.md's respawn step (i) re-hashes everything under /workspace/models/, where the instruct entry's path lies.

38. T1:85, the stages' G-VER loaded the same folder the same way and PASSed: the BACKEND extension and G-TIME-n's start. CONFIRMED.
   - The committed _gver_tokenizer (drv:1068–1073) makes the same call as draft 2 (5332–5339), on w["path"] (drv:1192, :4292).
   - The WEIGHTS lines name the same 22-file folder in results/raw/2026-11-18_n-step4_bext-box2_out.txt, results/raw/2026-11-19_n-step4_bext2-v1_out.txt and results/raw/2026-11-21_n-gtime-v1_out.txt.
   - "status": "PASS" appears in bext-box2_out:51–52, bext-run3_out:52–53, bext-resume4_out:57–58, bext2-v1_out:60–61 and n-gtime-v1_out:121–122 and :185–186.

39. T1:88–89, the record is written once, so a committed record makes G-VER refuse with "exists". CONFIRMED (draft 2:5379–5381 and 5285–5286; review B7 at :114).

40. T1:89–91, a re-run needs the record moved aside first, as the seat ruled for G-TIME-n (ans21b:27). CONFIRMED. The quote is verbatim from the last sentence of ans21b:27, in the Q7 ruling on a box change. Observation 3: the quote's "B7" is a different review's B7.

41. T1:92–93, after a box change the CHARACTERIZED_* constants change and the old record fails check_gver's pins. CONFIRMED (drv:575–577, "A new box is a new characterization and a change here."; draft 2:5244–5250; review B7 at :115).

42. T1:93–94, "A re-run on a new box writes a new record, and the old one stands as the old box's." NOT CHECKABLE (Code's reading; T1:105–106 asks it as a question). See observation 4.

43. T1:98–102, the Q2 (GV4) clauses. CONFIRMED (B:291 and B:295–296; draft 2 as in items 22 and 28).

44. T1:103–104, the Q4 (GV9) clause. CONFIRMED (item 30; "any cause" at B:300; N.3 at B:19–20).

45. T1:105–106, the Q6 (GV13) clause. CONFIRMED as to its label (B:306); the question itself is Code's.

46. T2:1–3, the title and "STOP for the seat's read". CONFIRMED. It matches T1:1, and "blind" matches review:1. "Same sitting" is a plan.

47. T2:4–5, the block link. CONFIRMED. The path is the brief's commit path, it is not yet tracked (no clash), and the form matches d92500b's entry (RESULTS.md:26–27).

48. T2:7, the seven are committed at d92500b. CONFIRMED.

49. T2:7–9, the nudge is held so that one nudge carries cd6b30d, d92500b and this supplement. NOT CHECKABLE. cd6b30d does exist: the coordinating session's notes on the third sitting.

50. T2:10, one blind review, one BUG and six RISKs. CONFIRMED.

51. T2:10–12, the five items. CONFIRMED as in T1. The F5 point from item 12 applies here too.

52. T2:12–13, the coordinating session's routing. NOT CHECKABLE.

53. T2:14, the BUILD is not committed. CONFIRMED.

54. T2:14–15, the BUILD's commit follows, with draft 2 and its window requested. NOT CHECKABLE (a plan).

55. T2:16–24, the parts of the supplement. CONFIRMED against T1:27–34, the section headings at T1:38, :53, :67, :77 and :87, and T1:96–106.

56. T2:25, the dependencies. CONFIRMED, as T1:17 states them. See observation 10.

57. T2:26, nothing ran on a model. NOT CHECKABLE.

58. T2:29, Code's departures are in the BUILD's entry. NOT CHECKABLE (a plan, as briefed).

59. T2:31–32, the gate's id list. NOT CHECKABLE.

60. T2:33–35, committed by path. NOT CHECKABLE.

61. T2:37, the home-folder count is 0. NOT CHECKABLE before the commit. T1 and T2 themselves contain no home-folder or scratch-root string (grep -c: 0 and 0).

62. T2:37, "Not pushed. G-VER's BUILD follows." NOT CHECKABLE.

TOTALS: 62 items: 43 CONFIRMED, 4 IMPRECISE (items 3, 25, 32, 36), 1 FAIL (item 12), 14 NOT CHECKABLE.

OBSERVATIONS

1. F5 is carried nowhere, though it bears on the ends the block tells the seat about. B:279, like RESULTS.md:51–52, says "a refusal before G-VER, or any other failure: exit 1, with no record". In draft 2, exit 2 with no record also comes from any gver option (6088–6098) and from --gcal-dir or --bench-dir (6084–6087). A failure in the tokenizer load or in verify (5459–5463, outside any try) ends exit 1 with a traceback and no "G-VER (n): …" line. Q4 asks the seat about the ends, so F5 may belong with the five. At least, the texts could say that the launch reads each end by its exit code, last line and record together.

2. Review O7 (:153) qualifies the reason B:142 gives, which T1:39–40 quotes: no kernel runs, but the process does hold a CUDA context (drv:694, get_device_name). Draft 2's docstring already says so (243).

3. The "B7" in the ans21b:27 quote is G-TIME-n's BUILD review's B7 (results/raw/2026-11-21_n-gtime-build_review.md:100–103 and :262–265), not this review's B7. T1:22–23 says "B numbers are the review's", so the two are easy to conflate; naming it would avoid that.

4. T1:93–94 states as settled what Q6's added clause asks. No source says this of G-VER's record. The nearest is ans21b:27 on G-TIME-n: "the figures stand for the box they ran on". Mark it as Code's reading, or cite that line as the analogy.

5. tokenizer_config.json is pinned at fff5b944…3fc7 in the model manifest. So O5's open question (whether it names a tokenizer_class) can be settled off the box on any copy at that pin; ids.check_tokenizer_dir holds a render folder to those pins (ids:122–132). Settling it before Q2 would help the seat rule the config.json clause.

6. Draft 2's gver_environment docstring (5176–5177) still says "GV4 holds no pin on it". That contradicts its own pin checks (5253, 5418–5419) and its module docstring (251–252, 267–268). It is a stale line to fix before the BUILD.

7. ids.load also refuses a MANIFEST.json of another schema or form, or one whose iv or v base is not its own part (ids:308–315). A manifest off its pin reaches verify only if it passes all of ids:306–327. The Q4 clause could say "a MANIFEST.json that ids.load refuses (ids:301–327)".

8. The list at T1:43–44 is partial: accelerate, safetensors, huggingface_hub (drv:687) and Python (drv:698) enter both identifiers too.

9. "In the driver alone" (T1:9) is GV2's sense. The BUILD also commits .gitignore lines that admit the record (review:3, :9; B:193).

10. T2:25 names only the seat's answers as a dependency. The block's list (B:67–73, B:271–272) also has the BUILD's commit, the launch files' relay and the box.

11. "Three additions" (T1:1 and :33; T2:1–2) counts O3, O5 and B7, but §2 adds five clauses, three of them to Q2.

12. T1 cites draft 2 by function names alone. Naming the digest of the draft it describes (S/step4b/gver/draft2/n_sessions.py, 3df537d6…83c1) would pin "what draft 2 builds" until the BUILD's commit.

DEPARTURES
- One command was refused by the session's permission check and never ran. It would have passed the model manifest's path, taken from git ls-files output with a bracketed pattern, through a zsh `while read` loop into a grep's input redirection. Its grep pattern held the instruct entry's name, which contains a guard marker in plain form, in the command text. After the refusal I read the manifest with the file-reading tool only.
- For classing, all within item 1 as I read it:
  - `git ls-files -s` (modes and blob ids) with item 3's pathspec, filtered by a bracketed pattern;
  - `git hash-object --stdin-paths` with the manifest's path on stdin, not in any argv;
  - `git diff --name-only HEAD` with the pathspec and exclusion, counted;
  - `wc -l` and `grep -c` on the named S files;
  - `git show cd6b30d:RESULTS.md | sed -n`.
- Reads beyond the named sources (committed raws the texts do not name; not barred):
  - results/raw/2026-11-21_n-gtime-v1_out.txt (lines 119–123 and 183–187, and its WEIGHTS lines) and _run.txt (lines 68–80);
  - greps for the cuBLAS setting and env.sh over G-TIME-n's _run, _launch-review, _stage, _smoke and _hashes raws;
  - results/raw/2026-11-21_n-gtime-build_review.md (lines 100–104 and 262–270, and a grep for B7);
  - six BACKEND-extension out raws (greps of their G-VER and WEIGHTS lines, in a loop over named, marker-free paths).
- Otherwise none. No interpreter but shasum; no write; no network; no other marker in any argv or command text. Nothing under data/*/ckpt, data/*/reports or data/m[f]3 was read, listed, sized or timed. No whole-tree git status. Every tree-wide git command took item 3's pathspec with the campaign exclusion. In S, only the four named files were read.
```
