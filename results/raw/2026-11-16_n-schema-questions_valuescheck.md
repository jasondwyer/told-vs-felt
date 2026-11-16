# n — the early questions block: the blind values-check, two passes, and Code's dispositions

*The n-build session (Code), PI date 2026-11-16. Checked: `results/raw/2026-11-16_n-schema_code-to-design_questions.md`
and its RESULTS.md entry, before their commit. Two blind checkers, both Code's subagents. Each was briefed to run no
Python and to write nothing, under the list of record v2's items 1–5, quoted verbatim, and the coordinating session's
lines on `data/mf3` and on the barred batteries. The second was blind to the first.*

*What each pass checked:*
- *Pass 1: the first draft, four questions.*
- *Pass 2: the revised draft, five questions. It carries pass 1's dispositions and three additions made after pass 1
  and not prompted by it: Q5, the "what it stops" line on every question, and the reference to n-analyzer's block.*

*Each report is reproduced as its checker returned it. Neither prints a local path, and nothing in them is changed.
In the reports, "B:" and "E:" are line numbers in the block and entry drafts the pass read.*

## Pass 1 (the first draft), as returned

Blind values-check: the n-schema questions block (B) and its draft RESULTS.md entry (E)

Summary: 51 items. 43 CONFIRMED, 6 IMPRECISE, 1 FAIL and 1 NOT CHECKABLE.
- The FAIL is item 25: B:71 calls a greedy reply "BK's form", but BK's own record says their reply was sampled.
- The IMPRECISE items are 6, 8, 28, 29, 38 and 47.
- How I worked: no Python, nothing written, every git command scoped to named paths, nothing under data/mf3 touched, and no ckpt or reports path opened. BK's data was read only under data/n/bk, and BK's paper only through the text extraction (bk.txt).

**Header and form**
1. B:3, the session, PI date 2026-11-16 and "For the PI to route." Source: WORKFLOW.md:35 (§4). CONFIRMED.
2. B:5, schema.py sha256 `77c12d6d…94bc`, committed at `5a97527`. Source: shasum; `git rev-parse 5a97527:valence_core/n/schema.py` equals `git hash-object` of the tree file (965c0bad…); `git log` on the path. CONFIRMED.
3. B:6, PROPOSAL-n v0.2 sha256 `30a3d0f5…04f4`, §8 step 6. Source: shasum; n:159. CONFIRMED.
4. B:6 and B:15, the seat's answers of 2026-11-15, §5.1, `1f3ce1f9…df84b`. Source: shasum (`1f3ce1f9…220df84b`); answers raw l.60. CONFIRMED.
5. B:9 and E:6, "n-analyzer builds step 9's analyzer from that schema". Source: answers l.60 ("n-analyzer, step 9's `n_analyze.py` … built from that schema"); n:159 step 9. CONFIRMED.
6. B:14–17, the sources read and not opened. Source: WORKFLOW.md:35 ("the sources read and the ones not opened, by sha256"). IMPRECISE.
   - Only the answers raw has a sha256 in the list. Add these:
     - PROPOSAL-m v1.11 `42ab36ec…6c6b`
     - readout.py `774e5ca3…3136`
     - the G-DATA raw `f88cc8e7…f2dc`
     - reduced.json `ec5fea59…ba1d` and analysis.json `12c35645…6b2f`; both match their data/n/bk/SHA256SUMS lines
     - the 14 skeleton files, concatenated in name order, `be50011a…ba84`; this equals schema.py's SESSION_SET_SHA256
     - BK's PDF `e92c69cb…fa49`, as n:4 gives it. I did not hash the PDF. If it was read through a text extraction, say so.
   - The section list leaves out §0.10, which holds C12 (quoted at B:85–86), and §8 (cited at B:6 and B:9).
   - The block relies on RESULTS.md's `5a97527` entry and on G-ACQ (n)'s GA-5 (B:119). Neither is listed.
7. Form: short form; Q1–Q4 numbered, each with "Readings to weigh"; "Not questions"; "Code adjudicates nothing" (B:26); the path pattern `<date>_<topic>_code-to-design<_suffix>.md`; E says "Next", not STOP. Source: WORKFLOW.md:34–36. CONFIRMED.
8. B:26–27 and E:7, "Each question names the reading the schema encodes, as built". Source: schema.py `label_convention` (l.338–339, "as the lock names it; at backend-ext … as the stage's entry names it") and docstring l.33. IMPRECISE.
   - Q4 names Code's proposal; the schema encodes no label convention.
   - A Q4 ruling need not touch the schema, so B:10's "a follow-up schema commit" fits Q1–Q3 only.
   - Suggested wording: "Q1–Q3 each name the reading the schema encodes, as built; Q4 names Code's proposal (the schema leaves the convention to the lock)."

**Q1**
9. B:31–32, the n §2.1 quote. Source: n:77. CONFIRMED, verbatim. I joined the block's wrapped lines and matched them byte for byte.
10. B:32–34, m:172's form: `choice_read(verify=True)`; the two labels' tokens renormalized, with the combined mass; a vanilla forward; an identical re-forward with symmetric KL exactly 0.0. Source: m:172; readout.py:12–19, :40 (VERIFY_KL_BAR = 0.0), :109–119. CONFIRMED. The renormalization and label-mass detail is readout.py's; m:172 itself says "restricted two-label".
11. B:36 and E:8, all 12 labels are "Zone" plus a letter and a digit, over 160 records. CONFIRMED.
    - Source: the 14 skeleton files, 8×5 + 6×20 = 160 records. cue_S and cue_U each give 160 values over the same 12 labels: Zone B8, D7, H0, K7, L4, M2, N1, Q3, R9, T5, V3, W6.
    - BK text l.217–218: "a set of 12 labels".
12. B:37, the generation prompt is `<|assistant|>\n`. Source: G-DATA raw l.77; schema.py l.30–33. CONFIRMED.
13. B:38, "the tokenizer is on the box". Source: data/olmo/manifest.json (the `olmo2_instruct` entry at l.170, its path `/workspace/models/olmo2_instruct`, tokenizer.json at l.255); RESULTS.md:6769–6774 (G-ACQ (n)). CONFIRMED, but it is not only there (observation 1).
14. B:39–40, coinciding first tokens give 0.5 each. Source: readout.py:109–116 (p_a = pa/(pa+pb)). CONFIRMED.
15. B:41–45 and E:8–9, the reading the schema encodes. CONFIRMED.
    - The read is at the first divergent token, offset k, with the shared prefix teacher-forced on the cached path.
    - It records the two tokens renormalized, their combined mass and the pick; a tie goes to present[0]; m's verifying re-forward is not repeated.
    - Source: schema.py docstring l.40–49; RESTRICTED_FIELDS l.270–280; check_record l.723–728 and l.810–822 (k = shared_prefix; tie_pick is present[0]'s). m's tie rule: readout.py:96–97 and :114 (`label_a if pa >= pb`).
16. B:45, the fidelity re-computation is at d ∈ {0, ±1} and on the keyed sample. Source: n:77. CONFIRMED.
17. B:50, option (c) costs "about 7,360 more forwards". Source: n:87–93; the reads sum to 7,360, at one re-forward per read. CONFIRMED.
18. B:53, options (b)–(d) change the `restricted` block. Source: schema.py l.270–280 and l.811–812. CONFIRMED.

**Q2**
19. B:55 and B:57, the §4 (b) quote. Source: n:128. CONFIRMED, verbatim.
20. B:57–59, the §2.1 and §0.4 quotes. Source: n:77 and n:16. CONFIRMED, verbatim.
21. B:61 and E:11, BK generated a reply at every read, and the rows carry free_text, committed and choice_is_S. CONFIRMED.
    - reduced.json has 35,280 read rows, each with all three keys, and no free_text that is null or empty.
    - All 5,040 olmo_32b rows carry a free_text string and `"committed": true`.
22. B:62–63, floor_b0 run 0 at d = 0 has free_text "Zone W6", committed true and choice_is_S true. Source: reduced.json, the single row with cell floor_b0, member olmo_32b, run 0 and point 0.0 (gen_point 0.0, inj 0.0). CONFIRMED.
23. B:63–64, a reply is generated under the read's cache, so under a steered cache on steered reads. Source: BK text l.809–810 ("Assistant, cache constructed at d= 1: Zone W6"); l.256 ("not applied to tokens associated with U and the final choice prompt"). CONFIRMED.
24. B:66–67 and E:10, the schema encodes no reply: secondary (b) is not computed and there is no reply field. Source: schema.py l.108–109 ("NOT RECORDED: … the free-text reply of n §4 (b)"); RECORD_FIELDS l.218–268. CONFIRMED. "The VERDICTS entry would say so" is not in schema.py (observation 4).
25. B:71, "(b) a short greedy reply on every read, BK's form: …". FAIL.
    - BK's replies were sampled, not greedy: "The free-text sampler seed is identical across every read of a session, so a changed answer cannot be sampler noise." (analysis.json:26, `prereg.coprimary_choice`; also prereg.json:88).
    - The cap of a few tokens and the newline or end-of-turn stop appear in none of BK's committed files; prereg, analysis and spec carry no generation parameters.
    - Suggested wording: "(b) a short reply on every read where BK's sits (steering off at every generated position, the steered cache kept: BK App. B.2), decoded greedily (BK sampled theirs under one seed per session, prereg `coprimary_choice`), capped at a few tokens with a newline or end-of-turn stop (Code's choices) …". Alternatively, adopt BK's seeded sampler and say so.
26. B:74, "about 7,360 short generations". Same basis as item 17. CONFIRMED.
27. B:75–76, 160 at N1-V −1, 160 at N1-P −1 and 960 at N1-R −1. Source: n:21–23 (§0.4's table); n:87–89. CONFIRMED; the sum is 1,280.
28. B:77, "Rule 25 would read every reply." Source: CLAUDE.md rule 25, "full-transcript reads of all smokes and pilots". IMPRECISE.
    - Campaign replies are not smokes or pilots.
    - The read that would cover them is n §4's: "the seat's full read of the checkpoint files and of G-CAL-n's turns follows the analyzer's output" (n:130). n cites rule 25 only for G-CAL-n's turns (n:113).
    - Suggested wording: "Every reply would fall in the seat's full read of the checkpoint files (n §4), after the analyzer."
29. E:11–12, "about 1,280 replies". IMPRECISE.
    - The count is exact under (b) and under (c), whatever merges, because −1 is never merged. The block gives 160 + 160 + 960.
    - Suggested wording: "would put 1,280 replies (160 + 160 + 960, as Code counts them) under negatively steered caches".

**Q3**
30. B:84–85, the §2.3 quote. Source: n:81. CONFIRMED, verbatim; the source bolds "N1-V's dose points:".
31. B:85, §2.4's N1-R points. Source: n:88. CONFIRMED.
32. B:85–86, the C12 quote. Source: n:62, in §0.10's table. CONFIRMED, verbatim.
33. B:88–93 and E:13, the merge readings. CONFIRMED.
    - +d_20 merges first, then +d_eq. The distance is `abs(value - v) <= 0.05` as an IEEE double, and a strict `<` keeps the earlier candidate on a tie. A fold into 0 raises an error.
    - A merged point is read once, under the kept label, and every arm is filtered by the kept points, so N1-R included.
    - Source: schema.py l.115–124; dose_points l.588–629; dose_point_values l.632–641; read_plan l.430–446; check_record l.699–701; RESULTS.md:46–60 (settled with n-analyzer, flagged).
34. B:95–96, the plan of 7,360 / 6,240 / 5,120 reads. CONFIRMED.
    - By hand: 960 + 4,800 + 320 + 3×320 + 160 + 160 = 7,360 (n:87–93).
    - Each merged point removes 160 reads from N1-V and 24×40 = 960 from N1-R, 1,120 in all, giving 6,240 and then 5,120.
    - The schema self-test at l.1164–1183 asserts the same three figures.
35. B:102, option (b) changes the counts and `read_plan`. Source: l.430–446. CONFIRMED. The counts move only when a point actually merges.

**Q4**
36. B:106–107, the n §2.1 quote. Source: n:77. CONFIRMED, verbatim.
37. B:107–108, the BK §3.2.1 quote. Source: BK text l.241–242; the section heading is at l.233. CONFIRMED, verbatim.
38. B:110–111, B:117 and E:14, BK's files record logprob_S, logprob_U and margin, but neither the label token ids nor the scored text. IMPRECISE.
    - What I checked:
      - reduced.json: 31 keys on the read rows, none of them label ids or scored text.
      - The skeletons: the same 24 keys on all 160 records.
      - prereg, analysis and spec: no label-scoring or generation text.
    - This is established only for the copies under data/n/bk, which is what B:15 says was read. BK-repo files that were not copied were not opened, for example the transcript n:165 cites.
    - Suggested wording: "BK's files committed under `data/n/bk` record …", and in E:14 "BK's committed files do not record it".
39. B:111–112, log p(S) −9.69, log p(U) −11.47, margin 1.78. Source: the same reduced.json row: −9.692143320972718, −11.47339677799755, 1.7812534570248317 (11.473397 − 9.692143 = 1.781253). CONFIRMED.
40. B:112–113, Appendix B.2 prints a 1.78-nat unsteered margin for a Zone H0 / Zone W6 session. CONFIRMED.
    - Source: BK text l.746–812, including "compared with 1.78 nats when it was processed without steering" (l.811–812).
    - floor_b0's first record has present ["Zone H0","Zone W6"], and its ids_sha `0576163c2e573d78` equals the reduced.json row's.
41. B:114, the margin does not move with a prefix shared by both labels. Basis: arithmetic. CONFIRMED (see observation 2).
42. B:115–116, max(|log p(S)|, |log p(U)|) is G-DATA (vi)'s scale. Source: RESULTS.md:7373; G-DATA raw l.186–187; schema.py l.404–411. CONFIRMED.
43. B:117 and B:127, G-DATA (iv) pinned the rendering by reproducing ids_sha. Source: RESULTS.md:7317–7319 and :7340–7350; G-DATA raw l.88–115 (seq_len 160/160; ids_sha 158/160, plus 2 through one recovered split each). CONFIRMED.
44. B:119–120, the BACKEND extension runs on the box after the BUILD and before LOCK-n v0.1. Source: GA-5, RESULTS.md:6843–6844 ("They run after §8 step 6's build, before LOCK-n v0.1 …"); answers l.66. CONFIRMED.
45. B:130, the n §4 quote. Source: n:130. CONFIRMED, verbatim.
46. B:130–132, the blinding reading is labelled Code's and the ruling the seat's. CONFIRMED.

**Not questions**
47. B:142–151 and E:17, "The schema's other readings are declared in its docstring", followed by seven items. IMPRECISE.
    - Six of the seven are flagged in the docstring: the two paths (l.19–28); the shadow by reference (l.51, l.62–64); float32 captures (l.67–75); the fidelity form and the sample of sessions (l.77–84); N4's line (l.91–95); the retention interval against 5(f)(iii) (l.58–62).
    - `read_window` is not marked as a reading: l.36–38 state it as the stage's declared window, and 5a97527's entry lists it under "Also:" (RESULTS.md:85–87).
    - The list omits four readings that schema.py does flag:
      - what a record is (l.12);
      - `math.fsum`, "Code's choice" (l.35);
      - the identity check's form (l.86–89);
      - `pod_id` at every stage (l.331–332, in the field table).
    - Suggested wording: "Among them (docstring and field tables): …". Add the four, and carry `read_window` as "also declared".

**Entry, consistency and labels**
48. E:1–4: the heading, "do not stop the build", "Next: the rest of step 6 (PROPOSAL-n v0.2 §8)" and the block path. Source: B:9–12; WORKFLOW.md:34. CONFIRMED.
49. E:5, "The coordinating session suggested it, and the call was Code's". NOT CHECKABLE: it was a chat exchange, nothing in the repository records it, and the block does not say it.
50. E:8–17, the four summaries agree with the block. CONFIRMED, apart from items 29 and 38.
51. Labels:
    - Every schema reading is marked Code's (B:41, B:66, B:88).
    - Q4 is "Code's proposal" and "Code reads" (B:119, B:131).
    - The exposure count is "as Code counts them" (B:76).
    - Nothing is presented as the seat's. CONFIRMED, apart from the misattribution to BK in item 25.

**Observations**
1. Q1's question can be settled before the seat reads.
   - G-DATA (n) used the Instruct tokenizer's three files on the laptop, "re-downloadable at the pinned revision" (G-DATA raw l.64–72, l.270–271).
   - So whether the two labels' first tokens coincide, and the offset k, can be answered without a model or the box. That needs a battery window, and the PI's word for a re-download if the scratch copy is gone.
   - The 12 labels use 12 distinct letters: B D H K L M N Q R T V W.
   - If "Zone" tokenizes apart from the letter, every pair shares exactly the first token and diverges at the letter. The degenerate case would then cover every session, under all four Q4 candidates. This is an expectation, not checked.
   - BK's strength_ladder/analysis.json `cue_token_residual` notes that cue names "tokenize to slightly different lengths" (in-turn context).
2. B:114's prefix argument covers identical tokens scored in identical context.
   - The leading-space candidate re-tokenizes the label, and the end-of-turn token is scored after a different label for S and for U. So the margin itself can differ across the candidates.
   - Matching both log-probabilities, as the proposal does, covers this.
3. On Q4's blinding: a match certifies that the campaign's shadow margins equal BK's public d = 0 margins within tolerance. In effect the shadows' margins become known from BK's file. The seat may want that consequence stated in one line.
4. B:67's "The VERDICTS entry would say so" is a commitment by Code, not something schema.py encodes, yet it sits under "The reading the schema encodes".
5. Under Q2 (c), the generations would number 3,040: 480 (N1-V at 0 and ±1) + 1,920 (N1-R at ±1) + 320 (N1-P) + 320 (N4). This could stand beside (b)'s 7,360.
6. E:18's VALUESCHECK_LINE is still a placeholder. This commit's values-check raw needs a name other than `results/raw/2026-11-16_n-schema_valuescheck.md`, which is 5a97527's and already committed; WORKFLOW §5 says a committed raw is never edited.
7. B:15's hash tail `…df84b` has five hex digits where the block's other tails have four. It is harmless: 97d160a cites the file the same way, and f7c1974 as `…f84b`.

## Code's dispositions of pass 1

The FAIL and every IMPRECISE item are applied in the checker's terms. The observations are applied where they name a
gap in this block, and recorded otherwise. Line numbers are pass 1's.

| item | verdict | disposition |
|---|---|---|
| 6 | IMPRECISE | Applied. The header lists each source by sha256, with these hashes recomputed by Code: PROPOSAL-m `42ab36ec…6c6b`, `readout.py` `774e5ca3…3136`, the G-DATA raw `f88cc8e7…f2dc`, `reduced.json` `ec5fea59…ba1d`, `analysis.json` `12c35645…6b2f`, the skeletons `be50011a…ba84`, the PDF `e92c69cb…fa49` (read through a PDFKit text extraction, as the header now says). It adds §0.10, §8, RESULTS.md's `5a97527` entry and GA-5. Q5's sources were added with Q5. |
| 8 | IMPRECISE | Applied: "Q1, Q2, Q3 and Q5 each name the reading the schema encodes, as built … Q4 names Code's proposal; the schema leaves the convention to the lock." The "why now" paragraph names Q1, Q2, Q3 and Q5 as the questions a ruling against which moves the schema. |
| 25 | FAIL | Applied. Q2 (b) now reads "a short reply on every read, where BK's sits: steering off at every generated position, the steered cache kept. How it is decoded is the seat's: greedily, or by BK's seeded sampling. Code's choices would be a cap of a few tokens and a newline or end-of-turn stop." Q2's fact paragraph cites BK's sampling (`analysis.json`, `prereg.coprimary_choice`). The entry says the replies were sampled under one seed per session. |
| 28 | IMPRECISE | Applied: "Every reply would fall in the seat's full read of the checkpoint files, after the analyzer (n §4)." |
| 29 | IMPRECISE | Applied: "1,280 replies under negatively steered caches (160 + 160 + 960, as Code counts them)", in the block and the entry. |
| 38 | IMPRECISE | Applied: "BK's files committed under `data/n/bk` record …"; the entry says "BK's committed files do not record it"; the header adds that BK-repo files not copied there were not opened. |
| 47 | IMPRECISE | Applied: "The schema's other readings, among them these, are declared in its docstring and field tables". It adds what a record is, `math.fsum`, the identity check's form and `pod_id` at every n stage, and carries `read_window` as "also declared". |
| 49 | NOT CHECKABLE | Recorded. The entry now says the suggestion came "by message". |

| observation | disposition |
|---|---|
| 1 | Applied in Q1's fact paragraph: Code can settle whether the labels' first tokens coincide without a model, from the tokenizer files on the box, in the post-build site check; the question stands either way. A laptop re-download is not proposed. |
| 2 | Applied in Q4: a prefix shared and scored in identical context leaves the margin unchanged; a candidate that re-tokenizes the labels or appends a token after each can move it. The proposal compares both log-probabilities, which covers it. |
| 3 | Applied in Q4's blinding paragraph: "A match would, however, make the campaign's d = 0 margins known within the tolerance, from BK's published file." |
| 4 | Applied: "Code would say so in the VERDICTS entry" is now its own sentence after the schema's reading, not part of it. |
| 5 | Applied: Q2 (c)'s 3,040 generations, by part. |
| 6 | Applied: this raw's name is `2026-11-16_n-schema-questions_valuescheck.md`. |
| 7 | Recorded: the hash tail follows `97d160a`'s citation of the same file. |

**Added after pass 1, not prompted by it:**
- Q5, G-READ-n's capture layer, a finding of the n package's self-test;
- a "What it stops" line on every question, on the coordinating session's suggestion;
- the reference to n-analyzer's block, which cites Q2, Q3 and Q5.

Pass 2 read all of them.

## Pass 2 (the revised draft), as returned

Values-check of the two drafts. Block: 2026-11-16_n-schema_code-to-design_questions.md (sha256 ee93fdf0…0d7d). Entry: entry.md (sha256 69e0285a…a983). Sources were checked at HEAD 8e3bf91. RESULTS.md anchors below are pinned to that commit (@8e3bf91).

**Rules kept:** No Python ran. Nothing was written, edited, staged or committed. Every git command was scoped to a path. Nothing under data/mf3 or any data/*/ckpt or data/*/reports path was listed, read, hashed or searched. The find runs pruned ckpt and reports. Every grep was /usr/bin/grep.

**Result:** 1 FAIL (item 41), 7 IMPRECISE (items 16, 19, 26, 40, 44, 51, 52). Everything else is CONFIRMED, except the items marked NOT CHECKABLE.

## Items

1. **Header digests (B:5–6, B:18–25).** Checked with shasum -a 256 at HEAD:
   - schema.py 77c12d6d…94bc
   - n v0.2 30a3d0f5…04f4
   - m v1.11 42ab36ec…6c6b
   - k bf7e79ec…3e92
   - seat's answers 1f3ce1f9…df84b
   - readout.py 774e5ca3…3136
   - olmo_hf.py df80b79b…92dc
   - reduced.json ec5fea59…ba1d
   - neutral_passages/analysis.json 12c35645…6b2f
   - the 14 skeleton files concatenated in name order be50011a…ba84 (= schema.py:146)
   - G-DATA raw f88cc8e7…f2dc

   The schema.py in the tree is 5a97527's blob (git rev-parse = hash-object). All the source files are tracked and clean. **CONFIRMED.**

2. **BK PDF e92c69cb…fa49 (B:24).** Checked against n:4. The PDF is not at the path n:4 names on this machine, so it was not re-hashed. The digest equals n:4's, and the PDFKit extraction has 38 pages, as n:4 says. **NOT CHECKABLE.**

3. **Schema committed at 5a97527 under n §8 step 6, on the seat's §5.1; n-analyzer builds step 9's analyzer from it (B:5–6, B:9, E:6).** Checked against 5a97527's subject and results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md:60. **CONFIRMED.**

4. **The self-test is drafted, not committed (B:7, B:185, E:20–21).** Checked with git status scoped to valence_core/n: primitive.py and testing.py are untracked. **CONFIRMED.**

5. **"Nothing ran on a model" (B:7) and the "Not opened" line (B:28).** These are Code's own statements. **NOT CHECKABLE.**

6. **n-analyzer's block exists at the cited path, cites Q2, Q3 and Q5, and its readings assume Q3's form (B:12–14, E:7–8).**
   - The file was absent when this check started.
   - It was committed during the check at 8e3bf91 (A results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md, sha256 2cd1acdf…ed03).
   - :40 and :56 say "which n-build's block asks as its Q3".
   - :79 says "n-build's block asks it (its Q2)".
   - :80 says "G-READ-n's capture layer is n-build's Q5".

   **CONFIRMED as of 8e3bf91.**

7. **"nine questions", "asks none of these" (B:12–13).** The brief limits this check to the file's existence and its citations. "Nine" does match 8e3bf91's subject and the file's :8 ("OPEN-Q1 to OPEN-Q9"). **NOT CHECKABLE.**

8. **Q1's quote of n §2.1 (B:43–44).** Checked against n:77 by fixed-string match. **CONFIRMED, verbatim.**

9. **m:172's form (B:44–46): two labels' first tokens, renormalized, with label mass; a vanilla forward plus an identical re-forward at symmetric KL exactly 0.0.** Checked against m:172 and readout.py:12–19, :40, :57–61, :90–120, :123–133. Two details: the read takes one id per label (`label_ids: Mapping[str, int]`), and it also logs the unrestricted top-1. **CONFIRMED.**

10. **All 12 of BK's labels are "Zone" plus a letter and a digit, across 160 records (B:32, B:48, E:11).** Checked the cue_S/cue_U fields of the 14 skeleton files:
    - 160 records and 320 cues.
    - 12 distinct labels: B8 D7 H0 K7 L4 M2 N1 Q3 R9 T5 V3 W6.
    - 0 cues fail to match `Zone [A-Z][0-9]`.
    - BK §3.2 says "12 labels" (bk.txt:218).

    **CONFIRMED.**

11. **Each label follows the generation prompt `<|assistant|>\n` (B:49).** Checked against results/raw/2026-11-06_n-gdata.md:77, :92, :98 and schema.py:30–33. **CONFIRMED.**

12. **If the first tokens coincide, each label gets 0.5 (B:50–51).** Follows from readout.py:109–115. **CONFIRMED.**

13. **The question can be settled from the tokenizer files on the box at the post-build site check (B:51–52).** Checked against RESULTS.md@8e3bf91:6915 ("G-DATA's three tokenizer files are these bytes") and n:159 ("post-build site check"). The plan itself is Code's. **CONFIRMED.**

14. **Q1's encoded reading (B:54–58, E:12).** Checked against schema.py:40–49, :270–280, :726–728 and :811–820. The read is at the first divergent token k, a tie goes to present[0], and there is no verify field. "(Code's, flagged)" matches schema.py:43, :48–49. **CONFIRMED.**

15. **"about 7,360" more forwards (B:63) and short generations (B:92).** From n:87–94: 960 + 4,800 + 320 + 3×320 + 160 + 160 = 7,360. Also schema.py:1166–1170. **CONFIRMED.** This holds with nothing merged; see observation 5.

16. **"LOCK-n v0.1, which pins the secondaries" (B:68) and "the lock pins the capture layers" (B:206).** n:117, the list of what LOCK-n v0.1 holds, names neither; it names "the analyzer hash". Both claims rest on Code's own 5a97527 entry (RESULTS.md@8e3bf91:174: "LOCK-n v0.1 pins each"). **IMPRECISE.** Suggested wording:
    - B:68: "which pins Code's readings (5a97527's entry) and the analyzer's hash (n:117)".
    - B:206: "since the lock pins Code's readings, the capture layers among them".

17. **Readings (b), (c) and (d) change the schema's `restricted` block (B:66, B:69–70).** Checked against schema.py:270–280 and :811–822. **CONFIRMED.**

18. **Q2's quotes (B:72, B:75–76, B:94).** Checked against n:128, n:77 and n:16 by fixed-string match. **CONFIRMED, verbatim.**

19. **floor_b0 run 0 at d = 0 (B:79–80, B:136–137).** In `reads.olmo_32b` there is one such row, and it matches the drafts: margin 1.7812534570248317, logprob_S −9.692143320972718, logprob_U −11.47339677799755, committed true, choice_is_S true, free_text "Zone W6". The locator does not name the member, though. reduced.json holds seven members, and its first floor_b0 run 0 point 0.0 row is gemma3_27b's (margin 13.0, log p −32.0 / −45.0, free_text "W6", committed false). **IMPRECISE.** Correct the locator at B:80 and B:137 to "(`reduced.json`, `reads.olmo_32b`)".

20. **BK's read rows carry free_text, committed and choice_is_S at every read (B:78).** reduced.json has 35,280 read rows, and each carries all three keys. free_text is never null or empty. **CONFIRMED.**

21. **One sampler seed per session (B:80–81, E:14).** neutral_passages/analysis.json `prereg.coprimary_choice` says: "The free-text sampler seed is identical across every read of a session". **CONFIRMED.**

22. **The reply is generated under the read's cache, so under a steered cache on every steered read, with steering off at the reply's positions (B:81–82).** BK B.2 shows "Assistant, cache constructed at d= 1: Zone W6" (bk.txt:809). The "steering off" half comes from §3.2.2 (bk.txt:255–256: "only at token positions belonging to turns associated with S"), not from B.2. **CONFIRMED.**

23. **Q2's encoded reading: no reply is generated and there is no reply field (B:84–85).** Checked against schema.py:108–109 and the RECORD_FIELDS table at :218–268. "Code would say so in the VERDICTS entry" is a statement of intent. **CONFIRMED.**

24. **1,280 = 160 + 160 + 960 (B:93–94, E:15).** These are N1-V at −1, N1-P at −1 and N1-R at −1 (n:87–89; §0.4's rows at n:21–23). **CONFIRMED.**

25. **The seat's full read of the checkpoint files comes after the analyzer (B:95).** Checked against n:130. **CONFIRMED.**

26. **E:13 "the schema generates none".** schema.py:9–10 says it "reads no file, touches no model and writes nothing", so it generates nothing in any case. **IMPRECISE.** Suggested wording: "§2.1 says no new text is generated; the runner generates none and the schema has no reply field."

27. **Q2 (c): 3,040 = 480 + 1,920 + 320 + 320, with the 1,280 unchanged (B:96–97).** From n:87–93: 160×3 + 24×40×2 + 160×2 + (160 + 160). **CONFIRMED.**

28. **Q3's quotes (B:106–108).** Checked against n:81, n:88 and n:62 (C12). **CONFIRMED.** The words are verbatim; B:106 drops the source's bold markers ("**N1-V's dose points:**").

29. **Q3's encoded merge rules (B:110–115).**
    - `dose_points` (schema.py:588–629) merges +d_20 first, then +d_eq.
    - The test is `abs(value - v) <= 0.05`. A candidate replaces the current pick only at a strictly smaller distance, so a tie goes to the earlier candidate.
    - A fold into "0" raises an error.
    - `read_plan` (schema.py:430–446) applies the kept points to every arm, N1-R included.
    - The 5a97527 entry records the rule as settled with n-analyzer and flagged (RESULTS.md@8e3bf91:157–174).

    **CONFIRMED.**

30. **7,360 / 6,240 / 5,120 (B:117–118).** 7,360 − 160 − 960 = 6,240, and 6,240 − 1,120 = 5,120. schema.py:1166–1183 asserts the same. **CONFIRMED.**

31. **Q4's quotes (B:131–133).** n §2.1 at n:77; BK §3.2.1 at bk.txt:233 (heading) and :241–242. **CONFIRMED, verbatim.**

32. **BK's committed files record log p and margin but neither label token ids nor the scored text (B:135–136, E:17).** I inventoried the keys of:
    - reduced.json;
    - neutral_passages' analysis, prereg and spec files;
    - strength_ladder's analysis and spans files, whose `ids` and `token_identity` keys are identity checks, not label ids;
    - the 14 skeleton files;
    - the five CSV headers.

    None records label ids or the scored text. **CONFIRMED.**

33. **B.2 prints a 1.78-nat unsteered margin for a Zone H0 / Zone W6 session (B:137–138).** Checked against bk.txt:746–748 and :808–812. It is floor_b0 run 0's session: that row's d = +1 margin is 3.5313, B.2's 3.53. **CONFIRMED.**

34. **Q4's bullets (B:139–144).** A shared prefix cancels in the margin. The scale max(|log p(S)|, |log p(U)|) is G-DATA (vi)'s. G-DATA pinned the rendering by reproducing ids_sha. Checked against RESULTS.md@8e3bf91:7428–7430, 7450–7461 and 7482–7487, and the G-DATA raw :92–98. **CONFIRMED.**

35. **The BACKEND extension runs after the BUILD and before LOCK-n v0.1 (B:146, B:168).** GA-5 at RESULTS.md@8e3bf91:6954–6955 says so. **CONFIRMED.**

36. **The schema leaves the label convention to the lock, and the lock pins it (B:39, B:169).** Checked against schema.py:33 and :338–339. **CONFIRMED.**

37. **The n §4 blinding quote (B:157).** Checked against n:130. Code's reading of it is labelled as Code's at B:158–159. **CONFIRMED.**

38. **Q5's quotes (B:174–177).** Checked against n:81, n:79 and n:121. **CONFIRMED, verbatim.**

39. **Q5's fact: the injection is added at a decoder layer's output, and the read position's residual at that layer is the shadow's, exactly (B:179–183, E:21–22).** In olmo_hf.py the forward hook adds the delta at the covered positions (:141–157) and stores the capture after the add (:158–159); it is registered as a forward hook at :166. At an unsteered position the add is exact: the bf16 value goes to fp32, gets + 0, and comes back unchanged. **CONFIRMED.**

40. **"for an L48 injection (k §1.4)" (B:186–187).** The bands are right and all sit in §1.4: k:243 (L51–L61), k:248–249 (L49–L63), k:263 (L51–L62). The L48 site is not in §1.4; it is at k:53 and k:211 (§1.2). **IMPRECISE.** Suggested wording: "for an L48 injection (k:211; bands k §1.4)".

41. **Q5's encoded reading labelled "(§2.2's words)" (B:189).** schema.py:67–68 says "CAPTURES (n §2.2: …; the form is Code's reading)". `layer` is "the adapter index of the site (G-VEC settles 31 or 32)" (schema.py:341). So if G-VEC settles the site at index 31, the schema captures index 31, not §2.2's "layers 32" — the ambiguity the block's own (d) raises. The reading is presented as the proposal's when it is Code's. **FAIL.** Correct to "(Code's reading of §2.2's words, flagged)".

42. **`capture_layers` is `[layer, n_layers - 1]`: the site and the last decoder layer (B:189–190).** Checked against schema.py:343, :662–663 and :1318. Index 63 sits before the final norm (RESULTS.md@8e3bf91:6928–6933). **CONFIRMED.**

43. **The median of two layers is the midpoint of a chance AUC and the last layer's (B:190–191).** Arithmetic, with the band median from n:121. **CONFIRMED.**

44. **Q5 (b): "as k's bands" (B:196).** Only G2's band (L49–L63) runs from the site + 1 to the last layer. G1's and G3's (L51–L61, L51–L62) start three past the site and end before the last layer. **IMPRECISE.** Suggested wording: "as k's G2 band (L49–L63)".

45. **Storage, about 300 MB for two layers and about 150 MB per further layer (B:196–197).** d_model is 5,120 (schema.py:345), captures are float32 (:71), and every read captures (:75).
    - Per layer: 7,360 × 5,120 × 4 B = 150,732,800 B ≈ 150.7 MB.
    - Two layers: 301,465,600 B ≈ 301.5 MB.

    The figures are decimal MB (287.5 and 143.8 MiB). **CONFIRMED.**

46. **Q5 (d)'s index facts (B:199–204).** The adapter's index l is the residual after decoder layer l, and "Which index BK's 'layer 32 of 64' names is G-VEC's R check to settle" (RESULTS.md@8e3bf91:6928–6933). R must be within 2% of 25.49 (n:81, n:111). **CONFIRMED.**

47. **Readings (a), (b) and (d) change the `capture_layers` check (B:207).** Checked against schema.py:662–663. The self-test at :1318 already refuses [32, 63] when layer is 31. **CONFIRMED.**

48. **The self-test asserts the site-layer capture equal to the shadow's while the last layer and the margin move, on a numpy causal double (B:185–186).** Checked against valence_core/n/primitive.py:403–409 and valence_core/n/testing.py:42–58 (the double adds the injection at a layer's output and captures after it). **CONFIRMED as code.**

49. **That this self-test ran.** **NOT CHECKABLE.**

50. **The "Not questions" list (B:211–224).** Each item is in schema.py: :12–17, :19–28, :61–64, :71, :77–84, :34–35, :86–89, :91–95, :58–61, :331–334. **CONFIRMED.**

51. **The title, "five … questions … on readings the committed schema encodes" (B:1, E:1).** Q4 is on the label convention the schema leaves to the lock (B:38–39; schema.py:338–339), not on a reading it encodes. **IMPRECISE.** Suggested wording: "…four on readings the committed schema encodes and one on the label convention it leaves to the lock".

52. **E:24–25, "each is needed before LOCK-n v0.1, and Q4 also before the BACKEND extension runs".** The block also makes Q1 a precondition of n-analyzer's secondary (a) (B:68–69) and Q3 a precondition of n-analyzer's battery fixing its plan's counts (B:126–127). **IMPRECISE.** Add "; Q1 and Q3 also before n-analyzer's secondary (a) and its battery's plan counts".

53. **Every reading labelled as Code's.** Q1 (B:54), Q2 (B:84), Q3 (B:110) and Q4 (B:146, B:158–159) are. **CONFIRMED.** Q5 is not; see item 41.

54. **The rest of block–entry consistency.** E:1–4 matches B:9–11. E:11–23 match Q1–Q5. E:15 matches B:93–94, E:18 matches B:151–152, and E:21–23 match B:179–183 and B:194–195. **CONFIRMED.**

55. **The block's form against WORKFLOW.md §4 (WORKFLOW.md:32–37).** It meets the brief's checklist:
    - the path form is right;
    - the header has the session, the PI date and "For the PI to route.", says what it concerns and under what, and lists sources read and not opened by sha256;
    - the short form is at B:30–36;
    - "Code adjudicates nothing" is at B:38;
    - Q1–Q5 each have readings to weigh;
    - "Not questions" is at B:209;
    - the entry says "Next" and carries no STOP.

    **CONFIRMED.**

56. **Claims that cannot be checked yet:**
    - "The BUILD entry lists them" (B:11, B:212, E:26) concerns an entry not yet written; it is consistent with RESULTS.md@8e3bf91:174.
    - E:5's message from the coordinating session is not in the repo.
    - E:27–28 are a placeholder and a commit statement.

    **NOT CHECKABLE.**

## Observations

1. **The tree moved during this check.** 8e3bf91 landed mid-check: n-analyzer's block, its values-check raw, and a 57-line RESULTS.md entry at :24. The cited block exists only from that commit, and every RESULTS.md anchor shifted by 57 lines. RESULTS.md's newest entry is now 8e3bf91's, not 5a97527's as the brief said. Consider citing n-analyzer's block by commit and digest at B:12–13 and E:7 (8e3bf91, 2cd1acdf…ed03).
2. **Q5 has no digests for the drafts it relies on.** Q5 rests on uncommitted drafts, but the header gives no sha256 for them, which WORKFLOW.md:35 asks for. At this check: primitive.py 0f56be93…2f14, testing.py 3fd9aed3…dbdd.
3. **Two `analysis.json` files exist under fixed_text_design.** B:23's digest pins neutral_passages/analysis.json. It is also the only one with the sampler-seed sentence; strength_ladder's `coprimary_choice` lacks it. Qualify the path at B:23 and B:80.
4. **G-READ-n cannot pass under Q5's encoded reading.** A chance site AUC (0.5) caps the two-layer median at 0.75, below the .90 bar. B:190–191 implies this without saying it; saying it would sharpen Q5.
5. **Merge sensitivity of the counts.** The "about 7,360" figures (B:63, B:92) assume no merge; they become 6,240 or 5,120 if points merge. 3,040 and 1,280 do not depend on merges.
6. **E:27 is still a placeholder (VALUESCHECK_LINE).**
7. **Formatting:** B:106 drops a bold marker that B:174 keeps. The seat's-answers digest shows five tail hex (…df84b) where the others show four.

## Code's dispositions of pass 2

Pass 2's count: 56 items, 43 CONFIRMED, 7 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE.

The FAIL and every IMPRECISE item are applied in the checker's terms. The observations are applied where they name a
gap in this block, and recorded otherwise. As with the schema's raw (`5a97527`), the edits after pass 2 were checked
by tool: each disposition's new wording was found in the final files by a fixed-string search, and the diff was read
against each item. They were not given a third blind pass.

| item | verdict | disposition |
|---|---|---|
| 16 | IMPRECISE | Applied: Q1's line reads "which pins Code's readings (`5a97527`'s entry) and the analyzer's hash (n §3)"; Q5's reads "since the lock pins Code's readings, the capture layers among them". |
| 19 | IMPRECISE | Applied at both places: "(`reduced.json`, `reads.olmo_32b`)". |
| 26 | IMPRECISE | Applied in the entry: "§2.1 says no new text is generated; the runner generates none, and the schema has no reply field." |
| 40 | IMPRECISE | Applied: "for an L48 injection (k:211; the bands at k §1.4)". |
| 41 | FAIL | Applied: Q5's encoded reading is "(Code's reading of §2.2's words, flagged)". |
| 44 | IMPRECISE | Applied: "as k's G2 band (L49–L63)". |
| 51 | IMPRECISE | Applied to the title and the entry's heading: "five early questions for the seat: four on readings the committed schema encodes, one on the label convention it leaves to the lock". |
| 52 | IMPRECISE | Applied in the entry: "Q4 is also needed before the BACKEND extension runs, and Q1 and Q3 before n-analyzer's secondary (a) and its battery's plan counts." |

| observation | disposition |
|---|---|
| 1 | Applied: the block and the entry cite n-analyzer's block as committed at `8e3bf91`; the block adds its sha256, `2cd1acdf…ed03` (recomputed by Code). |
| 2 | Applied: the header names the two drafts Q5 rests on, `primitive.py` (`0f56be93…2f14`) and `testing.py` (`3fd9aed3…dbdd`), recomputed by Code. They are untracked drafts that may change before the BUILD. |
| 3 | Applied: the path is `neutral_passages/analysis.json` in the sources list and in Q2. |
| 4 | Applied in Q5: "The band median of two layers is then the midpoint of a chance-level AUC and the last layer's, so at most 0.75: under the reading as encoded, G-READ-n cannot reach its .90 bar." |
| 5 | Applied: both "about 7,360" figures now add "with nothing merged". |
| 6 | Applied: the entry's values-check line is written. |
| 7 | Applied: Q3's quote restores the source's bold ("**N1-V's dose points:**"). The digest's tail form is recorded, unchanged. |
