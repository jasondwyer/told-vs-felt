# n — (v)'s render, the ids of record's third commit: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of the commit's two texts:
- T1, the RESULTS.md entry: `892d73c9…5b8d` (34 lines), its values-check paragraph a placeholder;
- T2, the render raw, `results/raw/2026-11-19_n-ids-v_render.md` here: `fe5f8f84…bf5c` (126 lines).

**The checker's brief** (`f540c1da…6621`, 78 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in Code's scratch, by name and sha256, the render's output and exit file, the
  self-test's, the render's seven files by name, the pin's move, the tokenizer folder's three files, and the overlay
  check's two lists; in the repository, the seat's answers, ADDENDUM-n1, the ids, gcal, sessions and driver code, the
  committed ids folder, the BUILD review raw and (iv)'s render raw, and the package digest in `package_sha256_of`'s
  form over HEAD's blobs and with the draft's `ids.py` in place;
- asked for every factual claim to be checked, and for the raw's verbatim output to be byte-equal to the render's;
- barred printing any token id, as well as any interpreter but `shasum` (with `jq` allowed for counts and fields),
  any write, any network, any guard marker in an argv, anything under `data/mf3`, any read, listing, size or time of
  a ckpt or reports file, and, in Code's scratch, anything but the named files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim, and required item 3's pathspec and the `data/mf3` exclusion on
  every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (292 lines, sha256
`40f1f7ee…2cde`). It names scratch files only by their paths inside the scratch folder, and repeats no token id.

**Totals:** 69 items: 57 CONFIRMED, 3 IMPRECISE, 1 FAIL, 8 NOT CHECKABLE; and 9 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The FAIL** (item 36, with observation 1): both drafts printed the end-of-turn token id, against ADDENDUM-n1 §1.2's
  "The render's raw prints versions, sha256s and counts, never an id". It is taken out of both texts: T2's R-v2 and
  T1's headline now say the end of turn is one id, recorded as the `v` block's `eos_id`, which carries it as data.
- **The IMPRECISE items,** each applied in the checker's words or near them:
  - 40: run 2's line is byte-equal to the count line of G-CAL-n's draft 6 run, cited by its raw; it did not run draft
    6's ids bytes;
  - 45: a base that fails `load`, or an existing `--out` or staging folder, is a refusal, not `render_v`'s STOP;
  - 64: of the ids folder's files, one is new and one extended, not "two change".
- **The NOT CHECKABLE items** stand: this session's acts and plans (7, 24, 30, 31, 32, 38, 39) and run 2's bytes, which
  its output cannot show (23).
- **The observations:**
  - 1 is the FAIL's.
  - 2, closed: the BUILD review's O10, routed to this commit, is now Code's cross-check by `jq` over the render's
    `gcal_prompts.jsonl` and the committed `sessions.jsonl`, its program and output whole in T2: every one of the
    160 sessions opens with exactly one of (v)'s 12 prompts, by its user turn and by its whole.
  - 3, closed: O11's second clause by run 3's `gver-trial` on the (i)–(v) folder, PASS, its output whole in T2.
  - 4, closed: run 3's `hashes` printed the package digest the shell computed, its output whole in T2.
  - 5, applied: run 2's verbatim line is fenced.
  - 6, applied: the overlay's root as "the repository" in an overlay run, and the argument refusal, are named.
  - 7, applied: `PYTHONUTF8=1` is listed, on runs 1 and 3.
  - 8, applied: runs 2 and 3 ran from the overlay with the pin's move and the render's files in place.
  - 9, applied: T2 has a Departures section.

## 2. The text changed after the check, and the edits checked by tool

- **The text changed after the check** by the dispositions above; by run 3, the cross-check and their sections, which
  came after it; in T1 by its values-check paragraph, which replaces the placeholder, and a fuller statement of the
  checker's departures; and by a dated note on `035947e`'s entry, on the coordinating session's three low items in
  that entry's values-check raw, which T1 names.
- **The edits, checked by tool:** fixed-string counts over each text unwrapped, for each disposition's new wording and
  each removed wording's absence; no five- or six-digit number in T1, or in T2 outside its verbatim blocks; and each of
  T2's six verbatim blocks byte-equal to its source file: 30 of 30. The note's claims were checked against the lines of
  that raw it cites.
- **No second full pass** was made over the texts.
- **The finals:** the entry `f3140682…23fd` (56 lines); the render raw `5834380d…aa6d` (213 lines).

## 3. The report as returned

VALUES-CHECK, T1 (S/step4b/v/entry_src.md) and T2 (S/step4b/v/render_raw.md), at HEAD 035947e

Preliminaries:
- The brief matched: sha256 f540c1da…6621, 78 lines.
- T1 matched 892d73c9…5b8d, 34 lines. T2 matched fe5f8f84…bf5c, 126 lines.
- Every named S source matched its stated sha256 and line count. Both exit files read "exit 0".
- HEAD is 035947e. Every named repository file is tracked and clean (`git rev-parse HEAD:<path>` = `git hash-object <path>`), and the index equals HEAD over the pathspec.
- This report does not repeat the end-of-turn token id.

ITEMS

T1 (T2's lines noted where the same claim recurs)

1. T1:1, T2:1. Claim: the ids of record's third commit. CONFIRMED.
   - `git log --format=%h -- data/n/ids/ <exclusions>` lists only b523f6a and d76f34f.
   - ids.py:80 calls d76f34f the first commit; the (iv) raw's title (:1) says "second commit".

2. T1:2, T2:3. Claim: ADDENDUM-n1 (v0.1) §1.2 (v) and §1.5. CONFIRMED.
   - ADDENDUM-n1:2 is "v0.1".
   - :22, (v) is `gcal_prompts.jsonl`, G-CAL-n's declared prompts.
   - :28, §1.5 is "rendering and spans" = MANIFEST.json's sha256, the pin that moves.

3. T1:2, T2:3–5. Claim: the seat's answers of 2026-11-19, first sitting, at that path, committed at a33252a, §1.7 and §1.8. CONFIRMED.
   - Answers :3, :28, :30.
   - `git show --name-only a33252a` lists that file alone.

4. T1:2–3, T2:6–7. Claim: the PI's routing, item 2 of "N. n-build (and the pod session on the box)", on "Route as given". CONFIRMED.
   - results/raw/2026-11-19_first-sitting_pi-routing.md (clean): :12 heading, :14 item 2, :26 "PI: Route as given".
   - The same item is the seat's §8 (answers :78, :80).

5. T1:3. Claim: G-VER's pin moved. CONFIRMED.
   - The draft's first hunk.
   - verify.py:72 defaults `manifest_pin` to `ids_mod.MANIFEST_OF_RECORD`.

6. T1:3, T2:7. Claim: model-free; tokenizer files only, no weights. CONFIRMED.
   - S/step4b/v/render_run1.txt:1 is the no-PyTorch notice, so no model can load.
   - render-ids-v loads only AutoTokenizer (n_sessions.py:2882), from a folder `check_tokenizer_dir` holds to exactly three files (ids.py:125–127).
   - The self-test is the model-free one (n_sessions.py:6).

7. T1:3, T2:7. Claim: "on the laptop". NOT CHECKABLE.
   - No source records the site. The printed environment is G-DATA's, which ADDENDUM-n1:20 places on the laptop.

8. T1:5, T2:21. Claim: HEAD 035947e's own code, unchanged, from an overlay checked equal to HEAD's. CONFIRMED.
   - All 161 lines of S/step4b/v/ov_pairs.txt occur exactly in HEAD's "blob path" list (comm). They include the 16 valence_core/n/*.py, scripts/n_sessions.py and the six data/n/ids/ files.
   - I re-derived that list (`git ls-files --format='%(objectname) %(path)'` with the pathspec). It hashes to S/step4b/v/head_pairs.txt's 35a53a45…9efb.

9. T1:5–6, T2:44. Claim: python 3.12.9, transformers 5.5.0, tokenizers 0.22.2. CONFIRMED.
   - render_run1.txt:2; ids.py:68; ADDENDUM-n1:20; both manifests' `environment`.

10. T1:6, T2:87–88. Claim: the manifest's three tokenizer files, exactly tokenizer.json 73fd5254…ecca, tokenizer_config.json fff5b944…3fc7 and special_tokens_map.json 78afb564…e2f2. CONFIRMED.
    - shasum of S/tok_n/'s three equals data/n/ids/MANIFEST.json `tokenizer_files` and ADDENDUM-n1:20.
    - "Exactly": the check passed (render_run1.txt:3–5).

11. T1:6, T2:21. Claim: PASS, exit 0. CONFIRMED.
    - render_run1.txt:7 has "status": "PASS"; the exit file reads "exit 0"; n_sessions.py:2889.

12. T1:7. Claim: 48 of 48, none merged across the boundary. CONFIRMED.
    - render_run1.txt:7 has n 48, ok 48, boundary_merged 0; jq counts 48 records.

13. T1:7, T2:71. Claim: gen_start 25 and seq_len 31 on every prompt; user turn 25 ids, whole 31. CONFIRMED.
    - render_run1.txt:7 has [25, 25] and [31, 31] (min, max: ids.py:568–569).
    - jq: 0 of 48 records off 25/25/31, and 0 with len(ids) ≠ seq_len.

14. T1:7–8, T2:72. Claim: the end-of-turn id is the figure stated, the v block's eos_id. CONFIRMED.
    - `jq -e '.v.eos_id == <figure>'` returns true. Its printing is item 36 and observation 1.

15. T1:9, T2:118. Claim: gcal_prompts.jsonl is new, a1197eb5…e35d, 48 records. CONFIRMED.
    - It is absent at HEAD (rev-parse fails; six tracked files in data/n/ids/).
    - shasum matches; jq counts 48; the manifest says 48.

16. T1:9–10, T2:119. Claim: MANIFEST.json extended, 53a8cd74…99d8, six files, a v block. CONFIRMED.
    - shasum matches; `.files | length` is 6; keys are HEAD's eight plus v; render_run1.txt:7 records 6.

17. T1:10, T2:109 (first clause), T2:113–117. Claim: the five (i)–(iv) files unchanged, byte for byte. CONFIRMED.
    - For each of the render's five, `git hash-object` equals `git rev-parse HEAD:data/n/ids/<f>`; the sha256s equal the table's.

18. T1:11, T2:22, T2:123. Claim: ids.py fd3e9c63…7022, +12 −9, from HEAD's cc614c75…8e76. CONFIRMED.
    - shasum of both files; diff shows 12 '>' lines and 9 '<' lines in two hunks.

19. T1:11–12, T2:74–75. Claim: MANIFEST_OF_RECORD moves from fdf73d85…ef38 to 53a8cd74…99d8, with its comment. CONFIRMED.
    - Hunk 1 replaces HEAD ids.py:83–86.

20. T1:12–13, T2:77–80. Claim: the committed-ids check moves to (i)–(v) as listed, and the BUILD review's O11 named it. CONFIRMED.
    - Hunk 2 at HEAD ids.py:1017–1027 requires: FILES_I_III + FILES_IV + FILES_V; the v block's base = MANIFEST_I_IV; the pin not in (MANIFEST_I_III, MANIFEST_I_IV); 48 prompts beside 544 passages and 1344 contexts (:74–77, :91).
    - Review raw :316 is O11; :99 routes it to this commit.

21. T1:14, T2:124–125. Claim: the package digest moves from e5606ddf…b36c (035947e's) to 1bb0daea…af51, by shell. CONFIRMED.
    - Recomputed in shell in the resume.py:328–350 form, over the 16 names from `git ls-tree`, in C order, each `git show` checked against its blob: e5606ddf…b36c.
    - With the draft's ids.py bytes: 1bb0daea…af51.
    - 035947e's subject gives e5606ddf...b36c.

22. T1:15, T2:22, T2:33–35. Claim: self-test 545/545, exit 0; one line, af912421…f158, verbatim. CONFIRMED.
    - S/step4b/v/selftest_v1.txt: `od -c` shows the two leading spaces, which T2:35 keeps. The exit file reads "exit 0". The print is n_sessions.py:356.

23. T1:15, T2:22. Claim: run 2's bytes, i.e. the pin moved (fd3e9c63…7022) and the render's seven files in the overlay. NOT CHECKABLE.
    - The output line cannot show it. HEAD's ids.py over HEAD's folder prints the same line: draft 6's run, byte-equal. Either mixed configuration fails the check.

24. T1:16, T2:12–14. Claim: battery windows; nice -n 19; HF offline; TMPDIR; PYTHONDONTWRITEBYTECODE; the venv reached by cd and a glob. NOT CHECKABLE.
    - Run 1's command (T2:27–29) carries the settings.
    - G-CAL-n's self-test command (results/raw/2026-11-19_n-gcal-delta_selftest.txt:18–20) has the same form.

25. T1:17–19. Claim: the raw's contents and link path. CONFIRMED.
    - T2's sections are at :10, :40, :66, :84, :91, :107 and :121. The link is the path the brief names.

26. T1:19–20. Claim: the self-test is in the raw's table of runs, as (iv)'s was. CONFIRMED.
    - T2:22; (iv) raw :20–23.

27. T1:21–23. Claim: the readings summary is R-v1–R-v5. CONFIRMED.
    - T2:68–82.

28. T1:24. Claim: G-CAL-n's input checks find (v), without which the driver refuses. CONFIRMED.
    - n_sessions.py:2756–2759 (the pin, then `gcal_prompts_check`) and :2673–2674.

29. T1:24–25. Claim: the launch files wait for G-VEC's PASS, and so for the seat's ruling on 355e3a2's STOP. CONFIRMED.
    - The PI routing raw :14; 355e3a2's subject.

30. T1:26. Claim: Departures, none of Code's. NOT CHECKABLE.

31. T1:28–29 and :31. Claim: committed by path; home-folder count 0; nothing ran on a model; not pushed. NOT CHECKABLE (future).
    - The texts, run 1's output and the render's MANIFEST.json and gcal_prompts.jsonl hold no home-folder or temp prefix (grep -c 0 each).

32. T1:32–33. Claim: Next. NOT CHECKABLE (plans).
    - Consistent with the PI routing raw :14 and :16, and with 035947e's subject.

T2

33. T2:3. Claim: PI date 2026-11-19. CONFIRMED.
    - T2:29's --pi-date; the v block's pi_date.

34. T2:5. Claim: the quotation from §1.7, "the 48 prompts stand … (v)'s render goes". CONFIRMED.
    - Answers :28, allowing for bold markup.

35. T2:5–6. Claim: the quotation from §1.8, "the generations and (v)'s render use the rendering of record". CONFIRMED.
    - Answers :30, verbatim.

36. T2:7–8. Claim: "The token ids are in the committed files under data/n/ids/; this raw prints none." FAIL.
    - T2:72 prints one token id, the end-of-turn id.
    - ADDENDUM-n1:22 says "The render's raw prints versions, sha256s and counts, never an id". The (iv) raw (:6–7) had this sentence and printed none.
    - Instead, drop the figure:
      - T2:72 becomes "- **R-v2, the stop.** `<|endoftext|>` is one id, recorded as the `v` block's `eos_id`: GC7's stop (the end of turn or the cap, no newline stop)."
      - T1:7–8 becomes "…`seq_len` 31 on every prompt; the end of turn one id, the `v` block's `eos_id`;".
    - If the figure stays, T2:7–8 becomes: "The token ids are in the committed files under `data/n/ids/`; this raw prints one, the end-of-turn id the `v` block records (R-v2), declared for the seat against ADDENDUM-n1 §1.2's "never an id"."

37. T2:15–16. Claim: 161 files; 161 joined, 0 differing, 0 untracked. CONFIRMED.
    - ov_pairs.txt has 161 lines and 161 distinct paths. All 161 paths are in HEAD's list; 0 have another blob; 0 are absent.
    - The overlay folder itself is not readable under the brief.

38. T2:24–30. Claim: run 1's command. NOT CHECKABLE.
    - Consistent: the --pi-date, the --out (S/step4b/v/out_render), S/tok_n, and the delta raw's overlay path (:20).

39. T2:32–33. Claim: run 2's command, with TMPDIR=<scratch>/step4b/gcal/tmp. NOT CHECKABLE.
    - The form matches the delta raw (:20), which writes TMPDIR as `<scratch>`.

40. T2:37–38. Claim: "The same bytes as G-CAL-n's draft 6 run, whose output is the same one count line: …". IMPRECISE.
    - Run 6's line in the delta raw is byte-equal to run 2's: `head -n 43 | tail -n 1 | shasum` gives af912421…f158.
    - Run 6's gcal.py (61bcafc9…14fc) and n_sessions.py (655430f3…d027) are HEAD's.
    - But the sentence reads as if run 2 ran draft 6's bytes, which it did not in ids.py or data/n/ids/ (T2:22), and the source is uncited.
    - Instead: "Its line is byte-equal to the count line of G-CAL-n's draft 6 run (`results/raw/2026-11-19_n-gcal-delta_selftest.txt`, run 6; the same sha256): the pin's move changes the ids check it carries, not the count."

41. T2:42. Claim: refuses a PI date not written as a calendar YYYY-MM-DD. CONFIRMED.
    - n_sessions.py:2850–2857 and :2866–2867.

42. T2:42–43. Claim: refuses an --out inside the repository or under guard.refuse_out's roots. CONFIRMED.
    - n_sessions.py:2868–2871; guard.py:74–81. Observation 6 covers the overlay's root.

43. T2:43–44. Claim: refuses any environment but G-DATA's. CONFIRMED.
    - n_sessions.py:2875–2878; ids.py:111–114.

44. T2:44–45. Claim: refuses a tokenizer folder that is not exactly the three pinned files. CONFIRMED.
    - ids.py:122–133; n_sessions.py:2879.

45. T2:47–49. Claim: render_v STOPs, writing nothing, unless "the committed (i)–(iv) folder loads, its manifest at MANIFEST_I_IV … five files … same environment and tokenizer digests". IMPRECISE.
    - A folder that fails `load` raises SystemExit (ids.py:524, :308–327), and so does an existing --out or staging folder (:522–523). Those are refusals, not the STOP report (:514, :526–531).
    - The rest holds (:526–531, :79). The (iv) raw draws this line at :45–46.
    - Instead, T2:47 becomes: "**`ids.render_v` then STOPs, writing nothing,** unless all of these hold. A base that fails `load`, or an `--out` or staging folder that already exists, is a refusal instead; nothing is written either way."
    - And bullet 1 becomes: "the committed (i)–(iv) folder's manifest is at `MANIFEST_I_IV` (`fdf73d85…ef38`) with exactly its five files, under the same environment and tokenizer digests;"

46. T2:50. Claim: `<|endoftext|>` encodes to one id. CONFIRMED.
    - ids.py:532–535 and :575; sessions.py:49; v.eos_text.

47. T2:51. Claim: `gcal.plan` gives 48 prompts over the 12 labels of record. CONFIRMED.
    - ids.py:536–544; gcal.py:175–181; n_sessions.py:2884.

48. T2:52–54. Claim: the boundary assertion. CONFIRMED.
    - ids.py:546–560 and :566–567.

49. T2:56–58. Claim: staged beside --out and renamed after read-back, every ids_sha re-derived, the (i)–(iv) part re-derived to MANIFEST_I_IV. CONFIRMED.
    - ids.py:521 and :582–598.
    - `jq -c -S 'del(.v) | .files |= del(.["gcal_prompts.jsonl"])'` gives fdf73d85…ef38. `jq -c -S .` reproduces both manifests' sha256s, so the form is canonical.

50. T2:59. Claim: the five files copied byte for byte and re-checked. CONFIRMED.
    - ids.py:584–588; item 17.

51. T2:60–61. Claim: the record fields, in plan order. CONFIRMED.
    - ids.py:561–564. jq: all 48 records have exactly the 11 keys, with index 0..47 in order.

52. T2:62–64. Claim: the MANIFEST extension and the v block's contents. CONFIRMED.
    - ids.py:572–580.
    - jq: keys are HEAD's plus v; files are HEAD's five plus gcal_prompts.jsonl; the iv block equals HEAD's; v has eight keys, including the two conventions.

53. T2:68–71. Claim: R-v1, the plan and the rendering, encoded with no special token added (Q7, Q8). CONFIRMED.
    - gcal.py:25–27, :142–144, :175–181; sessions.py:46, :49; n_sessions.py:420–421, :2883; answers :28, :30.
    - jq: 0 records off label i mod 12 or replicate i // 12.
    - The v labels are sorted and equal labels.json's 12.
    - printf of Zone B8's user turn and whole text, piped to shasum, gives 463c09ed…e3a2 and e195cb31…c6b5, record 0's two sha256s.

54. T2:72–73. Claim: GC7's stop (the end of turn or the cap, no newline stop). CONFIRMED.
    - Answers :30: "GC7's stops (the end-of-turn token or the cap, no newline stop)".

55. T2:74. Claim: the manifest extended in place, as (iv)'s was. CONFIRMED.
    - (iv) raw :87–91.

56. T2:75–76. Claim: MANIFEST_I_IV is the base and is kept; load re-derives it; the schema stays "n-ids-v1". CONFIRMED.
    - ids.py:79, :502, :312–315. The draft leaves :67 and :78–79 unchanged. The render's manifest schema is "n-ids-v1".

57. T2:80. Claim: reworded, not added; the count stays 545. CONFIRMED.
    - Hunk 2 alters one chk call and adds none. 545 equals draft 6's count.

58. T2:81–82. Claim: R-v5, HEAD's code with render_v and render-ids-v built at 89a55c3; only the pin and the check change the package. CONFIRMED.
    - `def render_v(` and `def cmd_render_ids_v(` count 0 at 89a55c3^ and 1 at 89a55c3.
    - ids.py is unchanged since 89a55c3 (`git diff --name-only`). The draft has two hunks.

59. T2:86–87. Claim: the folder the (i)–(iii) and (iv) renders used (<scratch>/tok_n), its provenance in the (i)–(iii) raw. CONFIRMED as the (iv) raw states it.
    - (iv) raw :103, and its command at :30. I did not open the (i)–(iii) raw.

60. T2:88. Claim: the render checked them again (its output, lines 3–5). CONFIRMED.
    - render_run1.txt:3–5.

61. T2:88–89. Claim: nothing was downloaded. CONFIRMED for the render's path.
    - n_sessions.py:2882 uses `local_files_only=True`; the offline variables are in run 1's command; the checks passed (ADDENDUM-n1:28).

62. T2:93–95. Claim: seven lines, 7b88e986…564d; first line the notice; last line 0f67b35b…d82c with its newline. CONFIRMED.
    - wc and shasum.

63. T2:97–105. Claim: "Run 1's output, whole" is byte-equal to render_run1.txt. CONFIRMED.
    - `head -n 104 | tail -n 7 | shasum` gives 7b88e986…564d. Fences are at :97 and :105.

64. T2:109. Claim: "two change". IMPRECISE.
    - gcal_prompts.jsonl is absent at HEAD: it is added, not changed.
    - Instead: "…; one file is new and one is extended."

65. T2:111–119. Claim: the table. CONFIRMED.
    - shasum of all seven files.
    - jq counts: 160, 320, 4 (candidates, ids.py:325), 544, 1344 and 48; the manifest lists 6 files.

66. T2:125–126. Claim: `hashes` prints the digest. CONFIRMED for the print.
    - n_sessions.py:222–225; guard.py:40–41. When the launch files are made is a plan.

Global

67. Every hash abbreviation is first 8 … last 4, derived with cut and rev. CONFIRMED.
    - T1 has 7 instances and T2 has 11. Every `[0-9a-f]{8}…[0-9a-f]{4}` in the texts is one of them.

68. T2's 13 distinct full sha256s each equal their source. CONFIRMED.

69. Commit references 035947e, 355e3a2, 89a55c3 and a33252a. CONFIRMED.
    - HEAD is 035947e; the other three subjects were read.

TOTALS: CONFIRMED 57, IMPRECISE 3, FAIL 1, NOT CHECKABLE 8 (69 items).

OBSERVATIONS

1. The end-of-turn id is printed at T1:8 and T2:72, against ADDENDUM-n1:22, ids.py:44 and `printable` (:273–278). The v block already carries it for the box, which asserts the tokenizer's eos against it (gcal.py:20–22), so dropping it from both texts loses nothing.

2. O10 is not addressed. The review raw routed it to this commit (:99, "O10 and O11: for (v)'s render commit"). O10 (:314) is a cross-check of (v)'s ids against the matching prefix of a session of record. Neither text states what became of it.

3. O11's second clause, "G-VER … is untested on an (i)-(v) folder" (:316), is not addressed. verify.py:72 makes the pin reach G-VER, but no G-VER trial is reported. (iv) ran one at its pin's move ((iv) raw :23, :175–186).

4. Run 2's output cannot bind its bytes (item 23). A `hashes` run on the pin-moved overlay, as (iv)'s run 4 paired with its self-test ((iv) raw :148–173), would print 1bb0daea…af51 from the run itself. The texts compute that figure from the files.

5. T2:35's verbatim line is not fenced. Markdown renders it inline as a lazy continuation and drops the two leading spaces. A ```text fence would fix it; (iv) used inline code (:189–191).

6. Two small gaps around the refusals list:
   - In an overlay run, "the repository" is the overlay's root (n_sessions.py:192; guard.py:26 and :30). An --out inside the working repository would not be refused from an overlay. Run 1's --out was outside both.
   - T2:42–45 omits the argument refusal (n_sessions.py:3611).

7. T2:12–14 omits PYTHONUTF8=1, which run 1's command (T2:27) sets.

8. T2:15 ("Both ran from … 161 files of HEAD") holds for run 1 only. For run 2, ids.py and MANIFEST.json were replaced and gcal_prompts.jsonl was added (T2:22).

9. T2 has no Departures section; (iv)'s raw had one (:204–214).

DEPARTURES

- I ran four `git show --name-only` commands without the brief's pathspec and mf3 exclusion: on 035947e, a33252a, d76f34f and b523f6a. The last two were piped to grep for their data/n/ids/ lines. They printed names and ids only.
- I ran one `git log --format=%h -- data/n/ids/ ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'`. It carries the exclusions as given, with data/n/ids/ in place of `.`.
- One `grep -A 3` of valence_core/n/sessions.py printed its line 52, a code constant holding four token ids. Not from the render's files; stated because the brief asks that no token id be printed. None is repeated here.
- Not barred by any rule, stated for the record:
  - jq on HEAD's data/n/ids/MANIFEST.json.
  - Reads beyond the named sources, each clean where checked: valence_core/n/guard.py, keys.py and verify.py (one grep); results/raw/2026-11-19_n-gcal-delta_selftest.txt; results/raw/2026-11-19_first-sitting_pi-routing.md; ids.py and n_sessions.py at 89a55c3 and its parent; five commit subjects.
  - diff's header printed the draft's modification time.
  - One zsh "bad substitution" ran no git command and was re-run.
