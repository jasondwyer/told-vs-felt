# n — the seat's block on the eleven starred readings: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over two drafts:
- T1, the block, sha256 `53012817…f7dc` (238 lines), its date placeholders marked not to be checked;
- T2, the head of G-CAL-n's spec raw, `f6c1cad9…4f24` (25 lines), and the raw built from it for a trial,
  `bc980b09…0d73` (461 lines, the date filled as 2026-11-19): the head's claims, and each fenced section against its
  source.

**The checker's brief** (`d23dc57f…713b`, 79 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in the repository, the files the texts cite, read at `da7bdec` by `git show` (HEAD
  had moved to `1185e15`, the analyzer's commit); in Code's scratch, by name only, the two messages, G-CAL-n's survey
  report and its brief, and Code's G1–G14 message;
- allowed `shasum` by name (on this machine a Perl script, which the list of record's item 1 permits), and barred any
  other interpreter, any write, any network, any guard marker in an argv (a grep pattern included), anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the named
  files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, with `.` as the include for `git ls-files`, that a glob is expanded and read before it is
  looped over, and the `rev-parse` form for a tracked-and-clean check.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (317 lines, sha256
`765b66c0…86c2`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 80 items: 55 CONFIRMED, 21 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE; and 11 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The IMPRECISE items**, each applied in the checker's words or near them:
  - in T1: 11, 13, 19, 21, 23, 24, 28, 30, 35, 37, 38, 39, 41, 53, 55, 59, 60 and 64;
  - in T2: 70, 75 and 78.
  G9's reading keeps the message's own words ("printed beside"); item 37's point is in G9's "As built" line.
- **The NOT CHECKABLE items** (5, 66, 67 and 72) stand: a scratch folder that may not be listed, Code's reasoning about
  a build not yet made, and acts recorded in no file.
- **The observations:**
  1. Applied: GC6's "another answer" names the stops and bans that would re-open under rule 13 (GC7), and Q8 asks for
     them.
  2. Applied: Q2 asks N2's injection index.
  3. Applied: a paragraph on what "no box re-run" covers.
  4. Applied: §3 says what follows if G-VEC stops at both indices.
  5. Applied: §3 says the build writes the record and the turns on a ±ρ fail; GC2's message had said "the record
     alone".
  6. Applied: §3 carries GC1, GC2 and GC14, with CG:62, BX:18 and rule 21's annotation cited.
  7. Applied: each survey is named where it is cited.
  8. Applied: the spec raw's head says every file:line in §1–§3 is `da7bdec`'s.
  9. Applied: the spec raw's head names G-CAL-n's BUILD entry beside the report's last section.
  10. Applied: Q4 asks whether G2's nearer-in-R rule stands.
  11. No change: §3 of the spec raw is the report verbatim.

## 2. The texts changed after the check, and the edits checked by tool

- **Both texts changed after the check:** by the dispositions above; and, at the coordinating session's word, the
  block's header, §0 and §3 reworded to the dependencies alone (G-CAL-n's run waits for all eleven answers; G-VEC's
  run waits for its four, or runs on them as PINs, as the PI answers), where the checked draft had proposed an order.
- **The edits, checked by tool:** a fixed-string search over the unwrapped final texts, each edit's new wording present
  and the wording it replaced absent, 58 of 58; the spec raw's three sections byte-equal to their sources, by `cmp`.
- **The finals:** the block `b9bd5286…ed0c`; the spec raw `92a8e869…9898`.

## 3. The report as returned

```text
BLIND VALUES-CHECK: T1 (S/step4b/seat11/stop_eleven_src.md) and T2 (S/step4b/gcal/spec_head_src.md + S/step4b/gcal/spec_raw_trial.md)

Before reading, I checked every digest and line count the brief gives. All of them match: brief d23dc57f…3b, 79 lines; T1 53012817…f7dc, 238; head f6c1cad9…4f24, 25; trial bc980b09…0d73, 461. HEAD is 1185e15. Between da7bdec and HEAD, only RESULTS.md, scripts/n_analyze.py and three raws changed. Repository files were read at da7bdec with `git show`. Keys used below: GV = results/raw/2026-11-19_n-gvec-build_spec.md; n = PROPOSAL-n-bk-reconciliation-v0_2.md; A-n1 = ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md; R = RESULTS.md at da7bdec.

ITEMS

1. T1:1. The eleven readings are G1, G3, G6, G9 and GC3, GC4, GC5, GC6, GC8, GC11, GC12. CONFIRMED. The starred G-readings are at S/step4b/gvec/pins_sent.txt:6, :13, :16, :23. The starred GC-readings are at S/step4b/gcal/pins_gcal.txt:8–11, :13, :16, :21. S/step4b/gcal/routing_gcal.txt:1 lists the same seven.

2. T1:6 and :35. G-VEC's BUILD is at da7bdec, on G1–G14, and the readings are as built. CONFIRMED. Evidence: da7bdec's subject; R:23–26; valence_core/n/gvec.py:26–65 (G1–G14 as built, with the departures declared).

3. T1:6–7. The readings were routed as PINs declared in the BUILD entry. CONFIRMED. GV:70 says "build and run on them as PINs declared in G-VEC's BUILD entry". R:85 says "Code's readings, G1–G14 (PINs; …".

4. T1:7–8. G-VEC has not run, and the run waits for the PI's word. CONFIRMED. R:25–26: "Nothing has run on the box. The run waits for the PI's word …". 1185e15 is the analyzer's commit. `git ls-files` (with the exclusions, then filtered) lists nothing under data/n/gvec/.

5. T1:7. The launch files are drafted in Code's scratch. NOT CHECKABLE, because S may not be listed.

6. T1:9. The survey has 22 open questions. CONFIRMED. They are trial raw:425–446, which is S/step4b/gcal/spec_report.md.

7. T1:9–10. GC1–GC22 were routed as PINs, and G-CAL-n is not built. CONFIRMED. routing_gcal.txt:1. `git ls-files` (filtered) shows no valence_core/n/gcal.py and nothing under data/n/gcal/.

8. T1:11–13. CONFIRMED. routing_gcal.txt:1 has "before G-CAL-n's run, not before the build". routing_gcal.txt:3 has "putting it to the PI to send G-VEC's four … in that same sitting. G-VEC would then run first on its PINs".

9. T1:16–17. GV's path, `c88c3173…2a6a`, committed at da7bdec, its §1–§3, and `07511f94…9f90`. CONFIRMED.
   - `git show da7bdec:GV | shasum` gives c88c3173…2a6a.
   - `git show --name-status da7bdec` shows GV as A (added).
   - GV:7–12 describe the three sections.
   - GV:88–449 hashes to 07511f94…9f90 (362 lines).
   - GV:23–64 hashes to S/step4b/gvec/pins_sent.txt's digest, 18d31729…fae1.

10. T1:18–19. G-CAL-n's spec raw has §1–§3 and `235191c1…12a3`. CONFIRMED; see items 79–80. "(committed with this block)" is in the future and was not checked.

11. T1:20–21. "CLAUDE.md's rules 2, 13 and 21 (C:line)". IMPRECISE. T1 cites only rule 13 (T1:152, C:315–318). A grep of T1 finds no other "C:" citation and no mention of rule 2 or rule 21.
   Put instead: "CLAUDE.md's rule 13 (C:line)".

12. T1:24–29. The R:, CA:, RC:, ST1: and SL: forms and their files. CONFIRMED. Every file exists at da7bdec. These are G-CAL-n's survey's own keys (trial raw:91–94).

13. T1:37–40. The short form. IMPRECISE, for two reasons.
   - On a STOP, `compute` stops at R and `write` writes the record alone (gvec.py:315–317, :341–343, :416–418). So a G9 answer that turns a STOP into a PASS needs a re-run.
   - The BUILD review's O1 (results/raw/2026-11-19_n-gvec-build_review.md:327) says the R check also "cannot test … which tokens enter the passage mean". That clause sets the means, not R.
   Put instead: "On a PASS, the BUILD stores the alternatives the texts leave open, so a different answer to G3 or G6, to G9 (short of turning a STOP into a PASS), or to G1's centring clause, re-derives G-VEC's figures from its stored rows and R's with no box re-run; a STOP writes the record alone. G1's other clauses are the exception: they set the captures (R, or the passage means, which are not stored), so striking one rebuilds the capture and re-runs G-VEC."

14. T1:41–43. 48 turns at −ρ, which cannot be taken back. CONFIRMED. n:20 reads "| G-CAL-n (coherence + arrival on one batch; §3) | 48 turns at −ρ (≤ 80 tokens each) |", a row of §0.4's table (n:16–26).

15. T1:44–45. The order Code proposes. CONFIRMED. pins_gcal.txt:27 (GC18: "G-CAL-n's run needs G-VEC's PASS and outputs committed"), :29 (GC20) and :31 (GC22); routing_gcal.txt:3.

16. T1:46. Q1–Q11, one per reading. CONFIRMED; see T1:226–238.

17. T1:51–56. G1's reading. CONFIRMED. It is verbatim GV:28–33, which equals pins_sent.txt:6–11.

18. T1:58. The two phrases from n:36. CONFIRMED. Both are verbatim in n:36.

19. T1:59. "directions.py:8–14, Code's readings, restated as R-iv1 and flagged (R:2188–2190)". IMPRECISE.
   - directions.py:8–14 holds four readings. R-iv1 restates only the first: "Each passage is encoded alone, with no special tokens and no template" (results/raw/2026-11-18_n-ids-iv_render.md:70–72).
   - R:2188 is the flag's header, R:2189 is R-iv1, and R:2190 is R-iv2.
   - R:2188–2190 at da7bdec equals the survey's R:2041–2043 at 003ae7d (diffed).
   Put instead: "directions.py:8–14, Code's readings; the first (the passage alone, no special tokens, no template) is R-iv1, flagged for the seat (R:2188–2189; results/raw/2026-11-18_n-ids-iv_render.md:70–72);".

20. T1:60. No ruling exists (the survey's 4.1 and 5.2). CONFIRMED. GV:352 says "I found no ruling on them in the seat's raws or the addenda"; GV:407 is 5.2. Neither da7bdec nor 1185e15 adds a seat raw (their name-status lists).

21. T1:61. "The R check tests the capture's R clauses but not the PCA's centring (the BUILD review's O1)". IMPRECISE. O1 (review raw:325–329) says: "It cannot test "neutral PCA centred" (U never enters R), nor which tokens enter the passage mean."
   Put instead: "As built: the R check tests the capture's R clauses, but neither the PCA's centring nor which tokens enter the passage mean (the BUILD review's O1). The centring is hedged: v under an uncentred U is stored at both indices, …".

22. T1:61–63. `valence_uncentred` is stored in directions_alt_L31.npy and directions_alt_L32.npy, with its sha16 and its cosine with v. CONFIRMED.
   - gvec.py:92: ALT includes "valence_uncentred".
   - gvec.py:106–107: `alt_file`.
   - gvec.py:349–358: per index, the row, and an "uncentred" block holding norm_v, sha16 and cos_v.
   - gvec.py:421–429: both alternatives files are written on a PASS.

23. T1:65–66. Striking the centring needs only a small code change in `of_record` and LOCK-n's direction sha16. IMPRECISE. The analyzer's cosines file and the 378-pair table are computed from the site's valence row of record (gvec.py:392, :430–432), so they move too.
   Put instead: "…with a small code change in the record's `of_record` selection and LOCK-n's valence sha16; the analyzer's cosines file at the site and the 378-pair table, which use the valence row of record, are re-derived from the stored rows on the laptop, declared."

24. T1:67–69. "Any other clause struck … R itself changes … a rebuild of the capture and a G-VEC re-run (about 1,900 forwards)". IMPRECISE.
   - A token left out of the passage mean alone leaves R as it is (O1, review raw:327). It changes v.
   - The passage means are not stored (O1, review raw:329; `write` stores only unit rows and figures).
   - The forward count is right: 544 + 1,344 = 1,888.
   Put instead: "Any other clause struck (for example a special token, a template, a token left out of the mean and R, or R as a mean of per-passage RMS): R itself changes, and with it the R check and every figure. A token left out of the passage mean alone leaves R unchanged but changes v, and the means are not stored. Either way: a rebuild of the capture and a G-VEC re-run (about 1,900 forwards: 544 passages and 1,344 contexts)."

25. T1:72–73. G3's reading. CONFIRMED. GV:35, which equals pins_sent.txt:13; T1 drops only "also".

26. T1:75–77. CONFIRMED.
   - n:81 has "at layer 32" three times; n:111 has "R_ℓ at layer 32".
   - schema.py:481: "R_l at the site by the step-2-survey convention (g:165)".
   - scripts/box_a3_extract.py:82: `DEFAULT_LAYERS = (32, 40, …)`.
   - The survey's 4.3 is GV:356.

27. T1:78–79. What is recorded at both indices for G3. CONFIRMED.
   - gvec.py:360–364: the contexts are captured at both indices.
   - gvec.py:369: R_ell at both.
   - gvec.py:373–384: N2's rows, the fit-only rows, freeze_sha, fit_only and guards, per index.
   - gvec.py:399–400: `of_record` is the site's.

28. T1:80–82. What another answer to G3 would change. IMPRECISE.
   - `of_record` is built from one index (gvec.py:399–400). Under this ruling it would hold index 32's N2 sha16s and R_ell beside the site's R and v.
   - The cosines file pairs v with N2's rows at the site (gvec.py:430–432), so it would need re-deriving.
   Put instead: "…The `of_record` block's N2 sha16s and R_ell, LOCK-n's R_ℓ and therefore G-CAL-n's d_eq (= 0.10·R_ℓ/(ρ·R), n:81) take index 32's figures, while R and v stay the site's; the analyzer's cosines file at the site, which pairs v with N2's rows, is re-derived from the stored rows."

29. T1:85–87. G6's reading, and the fit-only family at the coordinating session's request. CONFIRMED. GV:38; GV:79 ("record it beside, descriptive, with A3's all-context form as the one of record"); gvec.py:41–44.

30. T1:88. "n:111's "fit/val"". IMPRECISE. That string is not in n:111, which reads "`fit_ids`/`val_ids` as `a3_axes_*.json` has them". "fit/val" is the label used in the message (pins_sent.txt:16) and the survey (GV:366).
   Put instead: "n:111's "`fit_ids`/`val_ids` as `a3_axes_*.json` has them";".

31. T1:88. The survey's 4.6. CONFIRMED (GV:366).

32. T1:89–90. G6 as built. CONFIRMED. gvec.py:363 (the fit items' contexts), :376 (the fit rows into the alternatives files), :380–383 (norm, sha16 and cos_all per index), :399–400.

33. T1:91–93. If the fit half is of record, no box re-run. CONFIRMED where it says what the code stores or computes. The fit-only rows are stored (gvec.py:376, :421–429). The cosines are computed from the stored float32 rows (gvec.py:430–432), so a laptop re-derivation is exact. See Observation 3 for what is not stored.

34. T1:96–97. G9's reading. CONFIRMED. GV:45, which equals pins_sent.txt:23.

35. T1:99. "n:81 and n:111: "within 2% of 25.49 … else STOP"". IMPRECISE. n:111 matches ("within 2% of 25.49 [C], else STOP"). n:81 reads "R ≈ 25.49 there [C] — reproduced at G-VEC within 2%, else STOP", so the quoted string is not in n:81.
   Put instead: "n:111: "within 2% of 25.49 [C], else STOP"; n:81: "R ≈ 25.49 there [C] — reproduced at G-VEC within 2%, else STOP";".

36. T1:100–104. CONFIRMED.
   - A-n1:52: "(within 2% of 25.49)".
   - RC:164: "| R ≈ 25.49 from 7.6473/0.30 | 25.491 |".
   - SL:10497: `"resid_rms": 25.491040760519905,` (read with git show | sed).
   - box_a3_extract.py:206–207: `round(cap.resid_norms[l], 4)`.
   - schema.py:874: the exact d_eq comparison.
   - The survey's 4.9 is GV:378–380.

37. T1:105. "As built: as read, with R, rel and within recorded at both indices." IMPRECISE. R, rel and within are recorded at both indices (gvec.py:329–332). But BK's two figures are recorded in gvec.json's `bk` block (gvec.py:333), not printed. None of the stage's print lines shows them (gvec.py:322, :337, :339–340, :342, :345, :360, :385–386, :402). The driver prints only the files' sha256s (scripts/n_sessions.py:2229–2230).
   Put instead: "As built: as read, except that BK's two figures are recorded beside in gvec.json's `bk` block, not printed; R, rel and within are recorded at both indices."

38. T1:106. "Another reference or form moves the 2% boundary by about 0.004% of R". IMPRECISE. By arithmetic:
   - Replacing 25.49 by 25.491 or 25.491040760519905 moves the bounds 0.98·ref and 1.02·ref by 0.0039% and 0.0041%.
   - The form |R − 25.49| ≤ 0.02·R moves the bounds from 24.9802 and 25.9998 to 24.9902 and 26.0102, about 0.04%.
   Put instead: "another reference (25.491, or BK's 25.491040760519905) moves the 2% boundary by about 0.004% of R; another form, such as 2% of R rather than of 25.49, moves it by about 0.04%."

39. T1:106–107. "The site decision changes only if an R falls in that sliver at the edge." IMPRECISE. When both indices pass, `choose_site` takes the smaller |R/ref − 1|, with an exact tie to 32 (gvec.py:156–164). So a new reference can also flip the site when the two R's are almost equidistant from it.
   Put instead: "…changes only if an R falls in that sliver at the edge, or, when both indices are within 2%, if the two R's are almost equidistant from the reference (the nearer-in-R rule)."

40. T1:107–108. R is recorded at both indices, so the site can be re-derived without a re-run. CONFIRMED. gvec.py:329–332. R is recorded on a STOP as well (gvec.py:341–343, :434–435, and the self-test's STOP check: "its R at both indices").

41. T1:108–109. "If the re-derivation flips the outcome (PASS and STOP, or 31 and 32), G-VEC's `of_record` follows". IMPRECISE. A STOP computes no direction (gvec.py:315–317, :341–343, and the self-test's "a STOP computes no direction and writes the record alone"). So after a STOP-to-PASS flip there are no rows for `of_record` to follow.
   Put instead: "If the re-derivation moves the site between 31 and 32, G-VEC's `of_record` follows to the other index's stored rows, and so does G-CAL-n's input; if it turns a PASS into a STOP, the run is a STOP for the seat; if it turns a STOP into a PASS, G-VEC re-runs, since a STOP writes R and nothing else."

42. T1:114–117. CONFIRMED. pins_gcal.txt:8; n:113 has "≤ 80 tokens"; n:20 has "≤ 80 tokens each"; n:99 has "under an 80-token cap and a newline stop".

43. T1:118–119. 1,902 of 1,920 passages are exactly 70 tokens, none longer, over 160 records. CONFIRMED; I counted it myself.
   - Method: `cd` into BK's skeleton folder through a glob. For each of the 14 `*.sessions.jsonl`, run `git show "da7bdec:./<name>" | jq -r '.passage_spans[] | (.[2] - .[1])'`, then `sort -n | uniq -c`.
   - Result: 1,902 spans of 70 tokens. The 18 shorter ones are 6 of 69, 1 of 68, 5 of 67, 4 of 65, 1 of 64 and 1 of 63. None is above 70.
   - There are 160 records, each with 12 spans.

44. T1:120. Appendix E is not in the repository, and v0.1 named no cap. CONFIRMED. `git ls-files` (filtered) lists no .pdf. v0.1 was never committed: `git log` over both of its names prints nothing. Its untracked archive copy (archive/PROPOSAL-n-bk-reconciliation-v0_1.md:73) has "(TEMP 0.7, their prompt)" and no cap.

45. T1:124–126. CONFIRMED.
   - GC4's reading: pins_gcal.txt:9.
   - No temperature parameter in BK's files: `git grep -c -i -E '"(temp|temperature|sampling_temperature|gen_temp)"[[:space:]]*:' da7bdec -- . <exclusions>` finds 0 files under data/n/bk. The word "temperature" appears there only in 7 skeleton session files.
   - The program's value: valence_core/m/gcal.py:31–32 ("e2a's session config (… STOP_CAP = 60, TEMP 0.7)") and valence_core/p/gcal.py:5 ("TEMP 0.7").

46. T1:130–135. GC5's reading. CONFIRMED. pins_gcal.txt:10. valence_core/n/sessions.py:46 holds the prompt verbatim. data/n/ids/labels.json: each of its 4 candidates holds the same 12 labels (Zone B8 … Zone W6), so 12 × 4 = 48.

47. T1:137–141. CONFIRMED. Each quote is in its source:
   - n:113 ("their prompt"); n:77 (BK's prompt); n:30 ("the zone prompts are BK's"); sessions.py:46.
   - A-n1:22 ("`gcal_prompts.jsonl`: G-CAL-n's declared prompts").
   - CA:52 ("fixed in its wiring").
   - RC:107 ("BK fix no batch size. G-CAL-n's 48 turns are the document's own, …").

48. T1:142. No text names the labels, the count per label, the context or the pairing. CONFIRMED within the texts cited: n:113, n:77, A-n1:22, A-n1:26, CA:52 and RC:107 name none of them (the survey's 4.1, trial raw:335–340).

49. T1:148–150. GC6's reading. CONFIRMED. pins_gcal.txt:11, with the rendering described at :10; sessions.py:9–17.

50. T1:152–157. CONFIRMED.
   - C:315–318: rule 13 verbatim.
   - n:34: the quoted words, and §0.7's heading ("the PI confirms at routing (Code's A2)").
   - R:12937: "2. A2, §0.7's rule-13 departure: confirmed."; the PI's own routing line is R:12925.
   - n:113.
   - valence_core/adapters/base.py:208, verbatim.

51. T1:162–168. CONFIRMED.
   - GC8's reading: pins_gcal.txt:13.
   - n:113: "generated under steering".
   - n:77: "The steered spans are the S whole-turn spans (… the user prompt and the passage …)".
   - R:12852–12859: an S span carries the `<|user|>` block, the `<|assistant|>` opening and the passage.
   - base.py:294–306: "with injections active from the segment boundary onward".
   - valence_core/n/runner.py:278–300: the dose's arithmetic.

52. T1:174–178 and :180. GC11's reading. CONFIRMED.
   - Verbatim pins_gcal.txt:16–20.
   - G-VER's decode is scripts/n_sessions.py:498–503 (`skip_special_tokens=False, clean_up_tokenization_spaces=False`).
   - 36/48 = 0.75.
   - With T trigrams of which D are distinct, T − D repeat an earlier one, so the fraction is 1 − D/T.

53. T1:179. "also under 20 words". IMPRECISE. pins_gcal.txt:19 reads "also for turns under 20 words".
   Put instead: "low lexical diversity: distinct/total words below 5/20, as a ratio, also for turns under 20 words;".

54. T1:182–184 and :186. CONFIRMED. n:113 ("the coherence heuristic verbatim"); RC:101–106 (the three quotes, verbatim); A-n1:26 ("use the decode of those ids").

55. T1:185. "ST1:296–297: n's "> 50%" and "per 20" abbreviate BK's wording". IMPRECISE. ST1:296–297 is about v0.1's G-CAL-n. v0.1's text has "> 50%" and "per 20" (archive copy :73). v0.2's n:113 reads "more than 50% of trigrams repeated" and "fewer than five distinct words per 20 words", which is BK's wording.
   Put instead: "ST1:296–297: v0.1's "> 50%" and "per 20" abbreviated BK's "more than 50%" and "per 20 words", which n:113 now uses;".

56. T1:187. No text defines a word, the trigram fraction or the windows. CONFIRMED within n:113, RC:101–107, ST1:296–297 and A-n1:26 (the survey's 4.8, trial raw:359–363).

57. T1:193–197. GC12's reading. CONFIRMED. Verbatim pins_gcal.txt:21.

58. T1:199–203. CONFIRMED. n:113 (verbatim); A-n1:26 (verbatim); ST1:176–177 ("we re-encode each steered turn"); RC:105.

59. T1:204. "No text gives … whether it runs at +ρ/2". IMPRECISE.
   - n:113: "BK's two hurdles on one batch per pole per dose … at +ρ, −ρ and +ρ/2 … then the arrival hurdle on the same turns".
   - n:49 (B4): "on one batch per pole per dose, in BK's order (coherence, then arrival on the same turns)".
   - Together these put the arrival hurdle on the +ρ/2 batch. What is left open is what a fail there does, because n:113's STOP names only ±ρ.
   Put instead: "No text gives the forward's context, the pooling or the t-test's form; n:113 and n:49 ("BK's two hurdles on one batch per pole per dose") put the arrival on the +ρ/2 batch too, but no text says what a fail there does."

60. T1:210–211. "costs at most a short G-VEC re-run". IMPRECISE. T1:67–69 itself says striking G1's other clauses "means a rebuild of the capture and a G-VEC re-run". GV:75 says "a later strike costs a rebuild and a short box re-run".
   Put instead: "A strike among G1, G3, G6 and G9 then costs at most a rebuild and a short G-VEC re-run (G1's capture clauses; GV:75), before any −ρ turn exists (GC20)."

61. T1:212 and :215–216. CONFIRMED. routing_gcal.txt:1, :9; pins_gcal.txt:27, :31.

62. T1:217–220. G-CAL-n's pre-declared ends. CONFIRMED. pins_gcal.txt:33 and :23. schema.py:750: "a point that would fold into 0 is refused". See Observation 5.

63. T1:221–222. CONFIRMED. The three departures are at trial raw:448–452, the report's last section; routing_gcal.txt:9.

64. T1:226–227 (Q1). IMPRECISE. Q1 calls all four clauses "the one the R check tests". By T1:61 and O1, the R check tests neither the centring nor which tokens enter the mean.
   Put instead: "Q1 (G1). Do Code's capture readings stand: the passage alone from its committed ids; every token in the mean and in R; the PCA centred; R the pooled RMS? The R check tests only the clauses that bear on R, not the centring or the tokens of the mean. If a clause is struck, which replaces it?"

65. T1:228–238 (Q2–Q11). CONFIRMED. Each matches its reading and pins_gcal.txt or pins_sent.txt.

66. Code's reasoning about a build not yet made, or a conjecture. NOT CHECKABLE. These are:
   - T1:41: "Each sits in one place in the build".
   - T1:119: "They may come from a different generation…".
   - The "another answer" lines for GC3, GC4, GC5, GC8, GC11 and GC12: T1:121, :127, :143–145, :169–170, :188–189, :205–206.
   Where they can be checked, they agree with the message; for example GC5's manifest and digest move matches pins_gcal.txt:27 and the pin at ids.py:71–74.

67. T1:158–159 and :212–214: "nothing else changes", and the rendering choice kept in one place. NOT CHECKABLE; see Observation 1.

68. T2:7. §1 is verbatim, `cde8a28c…0455`, 42 lines. CONFIRMED. `sed -n '27,68p' S/step4b/gcal/spec_raw_trial.md | shasum -a 256` equals S/step4b/gcal/pins_gcal.txt's digest, and the range is 42 lines.

69. T2:9. §2 is verbatim, `7728eb39…027d`, 9 lines. CONFIRMED. Trial raw:74–82 equals S/step4b/gcal/routing_gcal.txt.

70. T2:8 and :9. "It is in no other file." IMPRECISE.
   - No tracked file holds either text. `git grep -c -F` for "GC22 The box", "GC6 above all" and "GC20 G-CAL-n runs only once" over the worktree, da7bdec and HEAD, with the exclusions, finds nothing.
   - But §1 is also S/step4b/gcal/pins_gcal.txt, which T2:19 itself names ("the file Code wrote"), and §2 is S/step4b/gcal/routing_gcal.txt.
   Put instead, both times: "It is in no other repository file."

71. T2:10–12. §3 was compiled at HEAD da7bdec, is verbatim, `235191c1…12a3`, 373 lines. CONFIRMED. Trial raw:88–460 equals S/step4b/gcal/spec_report.md. The report's first line says "compiled read-only at HEAD da7bdec", and S/step4b/gcal/spec_brief.md:2 says "HEAD da7bdec".

72. T2:5–6 ("the block committed beside it"), T2:12 ("extracted from its hand-back by `jq`") and T2:18–20 (the `jq` extraction from the transcript, its declared departure, and "without the delivery wrapper"). NOT CHECKABLE.

73. T2:13. The brief is `725e9a6d…e805`, 63 lines. CONFIRMED (shasum and wc).

74. T2:13–15. The brief quoted the list of record's items 1–5 and barred an interpreter, any write, the network, a marker in an argv, data/mf3, and ckpt or reports reads. CONFIRMED. spec_brief.md:3–4, :43–45, :52–53, :58–63.

75. T2:14–15. "and any read of Code's scratch folder, its brief itself excepted". IMPRECISE. spec_brief.md:54 says "Code's scratch folder is not read at all." with no exception written. The survey read the brief at its caller's direction (trial raw:450, :457).
   Put instead: "and any read of Code's scratch folder ("Code's scratch folder is not read at all"; the brief itself was read at the caller's direction)".

76. T2:15–16. The departures are in the report's last section. CONFIRMED (trial raw:448–452).

77. T2:19. §1 is byte-equal to the file Code wrote. CONFIRMED: it is byte-equal to S/step4b/gcal/pins_gcal.txt (item 68). When that file was written cannot be checked.

78. T2:22. "None of the three names a local path." IMPRECISE.
   - §1 and §3 name the system path /usr/bin/shasum (trial raw:61, :450).
   - They name scratch files by paths inside the scratch folder: step4b/gcal/spec_report.md (:27) and S/step4b/gcal/spec_brief.md (:88).
   - A grep of the trial raw finds no home-folder or full scratch path.
   Put instead: "None of the three names a path in the home folder or the scratch folder's full path; §1 and §3 name /usr/bin/shasum, and scratch files only by their paths inside it."

79. Trial raw:1–25 against the head. CONFIRMED. It is spec_head_src.md with @DATE@ filled as 2026-11-19: `diff <(sed -n '1,25p' trial) <(sed 's/@DATE@/2026-11-19/' head)` prints nothing. The head has one @DATE@ and the trial has none.

80. The trial raw's ```text sections and frame. CONFIRMED.
   - §1 (lines 27–68), §2 (74–82) and §3 (88–460) each hash to the digest of their source files.
   - The fences are at lines 26/69, 73/83 and 87/461.
   - The file is 461 lines, sha256 bc980b09…0d73.

TOTALS
CONFIRMED 55, IMPRECISE 21, FAIL 0, NOT CHECKABLE 4 (80 items).

OBSERVATIONS

1. GC6's and §3's "nothing else changes" (T1:158–159, :212–214) is probably too strong.
   - Rule 13 makes stop discipline and scaffold-token bans part of the template family, which "recalibrate with it" (C:315–318).
   - GC7 ties the `<|endoftext|>` stop and "no ban set" to the chat form (pins_gcal.txt:12).
   - So a completion-style ruling would re-open GC7. It would also move MANIFEST_OF_RECORD and the package digest, as T1:143–144 says for GC5.
   - Q8 could ask for the stops and bans along with the frame.

2. Q2 (G3) does not ask the injection index. If the seat rules that N2's directions come from adapter index 32 whatever the site, and the site is 31, the injection index for N2 is open. The stage identity carries one `layer` for every direction (schema.py:464–465), and `runner._injection` injects at it (runner.py:287, :294).

3. "No box re-run" (T1:65–66, :91–93) covers the rows, sha16s and cosines only.
   - The fit-only family has no R_ℓ, guard profile or freeze_sha of its own: `subset`'s R_l is not recomputed (gvec.py:223–228), and the guard profile and freeze_sha are the all-context family's (:364, :379).
   - The uncentred variant records only its norm, sha16 and cosine with v (:356–358), not its U sha16 or removed fraction.
   - A ruling that wants any of these on the alternative of record needs a re-run, because the captures are not stored.

4. Every alternative exists only on a PASS. The block does not say what this sitting rules if G-VEC, running first, stops at both indices (GV:60: "There is no texted fallback"). In that case the eleven questions may be moot or need re-asking.

5. GC2 and the message's STOP paragraph disagree on what a ±ρ fail writes. GC2 says "the record alone, exit 2" (pins_gcal.txt:7); the STOP paragraph says "the record (and the turns)" (:33). T1:218 follows :33. The BUILD entry should settle which; rule 25's read of every turn needs the turns.

6. The survey's §5 lists three more pre-run seat items that the block does not ask:
   - 5.1, when and where the seat reads the turns (GC1);
   - 5.2, rule 21's annotation against n:113's STOP (GC2);
   - 5.6, a +ρ/2 fail (GC14) (trial raw:397–413).
   GC1 and GC2 go to LOCK-n's list, and GC14 is a PAUSE. One line saying so would show the seat they are carried, not dropped. Per the survey (trial raw:100–101, :400), CG:62 and BX:18 place the seat's read of every turn before G-ANL-n.

7. "The survey" means different surveys in different places. In §1 (4.1, 4.3, 4.6, 4.9, 5.2) it is G-VEC's, compiled at 003ae7d, whose R: anchors are 003ae7d's. In GC3 it is G-CAL-n's. Naming the survey each time would remove the ambiguity.

8. T2's head dates §3's anchors but not §1's. GC16's n_analyze.py:266 (pins_gcal.txt:25) is the d_eq check at da7bdec, but at HEAD (1185e15) line 266 is `if self.rho != RHO:`. RESULTS.md has moved too. The head could say that every file:line in §1–§3 is da7bdec's.

9. T2's head puts the survey's departures only "in its report's last section". The routing also puts them "in G-CAL-n's BUILD entry" (routing_gcal.txt:9), and G-VEC's raw names both places (GV:15–16).

10. Q4 does not ask about "the nearer". That rule is G2's, unstarred (gvec.py:32–34, :156–164). It decides the site when both indices pass, and it moves with the reference (item 39).

11. §3's first line abbreviates the brief's digest with a five-character tail, "725e9a6d…2e805", where the head uses "725e9a6d…e805". Both match the digest; §3 is verbatim, so it stays as it is.

DEPARTURES

1. I ran one `git ls-tree --name-only da7bdec valence_core/n/` that named a non-data folder rather than files, without the exclusions. git's ls-tree refuses exclude magic: an earlier `git ls-tree -r --name-only da7bdec -- . <exclusions>` failed and printed nothing. The command printed 15 module names.

2. I read BK's 14 skeleton files, whose folder path holds a marker, by `cd` through a glob and then `git show "da7bdec:./<name>" | jq …`. That reads the committed blob by a relative name. The rule names a redirect from the working-tree file (`jq … < name`) instead. No argv held a marker.

Noted, not barred:
- I read the untracked archive/PROPOSAL-n-bk-reconciliation-v0_1.md at line 73 with the file-reading tool. It is not at da7bdec, since v0.1 was never committed.
- `diff <(…) <(…)` used process substitution: descriptors, no file written.
- shasum ran on named files only.
- An `echo ====` tripped zsh's `=` expansion and printed an error; nothing ran.

Otherwise:
- Nothing under data/mf3, a ckpt folder or a reports folder was read, listed, sized or timed.
- No whole-tree git status was run.
- In S, only the named files were read, with no listing, glob or folder grep.
- No file was written, no network was used, and no other interpreter ran.
```
