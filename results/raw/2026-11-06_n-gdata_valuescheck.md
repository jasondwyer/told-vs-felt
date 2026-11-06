# G-DATA (n) — the blind values-check, and Code's dispositions

*The checker was a blind subagent, given the G-DATA raw and the draft entry with their sources but not Code's
reasoning, and it ran read-only. Its report follows verbatim, with Code's scratch directory written as `<scratch>`.
Code re-checked the FAIL and every IMPRECISE item at source before applying it; the dispositions are in §2.*

## 1. The checker's report (verbatim)

BLIND VALUES-CHECK: G-DATA (n) raw + draft entry

**Totals: 128 items. 105 PASS, 1 FAIL, 22 IMPRECISE.** Two further claims can't be checked from any source and are not counted: the PI's "Yes, download" (raw header and entry Inputs; no file records it) and the entry's `date -u` stamp.

Every number, hash and count reproduces. The FAIL is how the strength ladder's `primary` block is described. The IMPRECISE items are off-by-one locators, scope wording, unhedged causal sentences and two quotes.

**How I checked.** I wrote my own scripts. They and the hub JSON are in <scratch>/vc_gdata_blind/. I made no change to the repo, the clone or the downloads. HEAD is 5916097. I read the named hub URL, plus `…/revision/main` to confirm the "main" claim (also a read-only GET). I re-extracted BK's PDF myself (sha256 e92c69cb…fa49, 38 pages).

---

## FAIL (1)

**58. Raw (v), "Its rungs", 4th sub-bullet.**
- Text: "The `primary` slopes in both runs' `analysis.json` are a different, matched-leverage estimator (e6_k1 0.4595, e6_kl2 0.1648, e6_ksixth 0.0674)."
- Source: in both runs' analysis.json, `members.olmo_32b.under_relative.arms.{e6_k1,e6_kl2,e6_ksixth}.primary` holds two estimators:
  - `differenced_margin_slope_full_n` (n_sessions 320): 0.4250781992470269 / 0.1492967234407206 / 0.06175777066950474. These equal figureA10.csv to every digit.
  - `differenced_margin_slope_matched` (n_sessions 80): 0.4595 / 0.1648 / 0.0674.
- BK's `matched_leverage_note` says the full-n estimate "uses every skeleton of this cell and is what the row curves plot".
- The same full-n values recur at `cells.*.slope_full_n` and `row_ladder[*].slope_full_n`. In the extension they appear as `anchor_check.arms.*.here` = `recorded_267` and as top-level `prior_slope_267.olmo_32b`.
- So the CSV's figures ARE the primary block's full-n slopes. The three matched-leverage values are correct as matched values.
- Fix: say both runs carry the CSV's figures as `primary.differenced_margin_slope_full_n`, and that the same block also holds a matched-leverage refit on the 80 floor skeletons.

## IMPRECISE (22)

### In the raw

**35. (iv), "The two sessions…", bullet 1: "`neu_b1` line 2", "`neu_b3` line 13".**
- These are 0-based record indices. The 1-based file lines are **3** and **14**.
- Line 2 of neu_b1.sessions.jsonl is run 61; line 13 of neu_b3 is run 112.
- Cause: `enumerate(open(f))` in diag.py / resplit.py.
- Run, seed and ids_sha are right.

**37. (iv), same block, bullet 3: "BK record that each session's ids are 'the generation's emitted ids'".**
- `prereg.token_identity` in neutral_passages/analysis.json (also in prereg.json) reads: "every replay consumes ONE id list: the generation's emitted ids plus an identically appended choice turn".
- The quote is exact, but the paraphrase drops the appended choice turn. Low severity; the inference stands.

**40. (iv), bullet 4: "in passage 4" and "in passage 11".**
- These are 0-based. The raw's own numbering is 1-based ("the 12th passage", "turn 12", "passage i − 1").
- neu_b1 run 62: the split is in **passage 5** (passage_spans[4] = [443, 513]; "Birdsong" occurs only in history[4]).
- neu_b3 run 113: the split is in **passage 12**, the last (passage_spans[11] = [1164, 1234]).
- Cause: `enumerate(r["passage_spans"])` in resplit.py.
- Token positions 482–483 and 1203–1204 are right.

**44. (iv) "BK's span fields" bullet 3, and (v) "The steered spans" lead: "`turn_spans` tile the sequence on 160 / 160".**
- They are contiguous from token 0 to **n_pre** on 160/160, but none reaches seq_len (0/160).
- seq_len − n_pre = 39 in all 160 sessions. Those 39 tokens are in no turn span: the 12th passage's closing `<|endoftext|>` and newline, the choice turn, and the generation prompt.
- Fix: "tile [0, n_pre)".

**47. (v), paragraph after the bullets: "The passage's own closing `<|endoftext|>` and newline belong to the next turn."**
- True for passages 1–11. The 12th passage's pair (positions n_pre and n_pre+1) belongs to no turn.

**49. (v): "The mean S whole-turn length is 616.919 tokens".**
- 616.91875 is the mean **per-session total** over the six S whole-turn spans. It equals Fig. A8's `steered_span_tokens` 616.91875.
- One S whole turn averages 102.82 tokens (n = 960). The numbers are right; the wording is not.

**54. (v), extension sub-bullet: the quoted sentence.**
- Source is the extension's analysis.json `prereg.independent_variable`, which reads: "…the token stream of a given session is byte-identical across all eight cells -- k never touches the stream, it is applied at read time as a dose multiplier."
- The raw renders "--" as "—" and gives no field locator.

**62. (v), "The span" bullet 1: "its turn's rendered user-side delta".**
- `prereg.the_widening` says "injected across the whole of that turn's rendered delta".
- That delta includes the previous turn's close and the generation prompt, so "user-side" is not BK's term and mislabels part of the span.
- The quoted definition that follows is exact.

**70. (v), "What this means for §2.5's bracket": "That is why their full-strength slopes differ (0.425 against 0.916), as §2.5 says."**
- The numbers are right. §2.5 gives no cause; it says only "on its own basis whose full-strength slope is 0.425, not Panel D's 0.916".
- The causal attribution is Code's inference. The files don't establish it. BK's neighbouring figures:
  - figureA8.csv's OLMo bare row (137.05 steered tokens) has slope 0.5877.
  - The unprimed legacy cell e6_k1 (`anchor.cells.e6_k1_legacy`) has slope 0.5840.
  - The ladder's sessions carry no passages (`prereg.no_generation_anywhere`).
- Fix: "differ in basis" or "consistent with".

**71. (v), same paragraph: "The 0.122 at k = 1/3 is the ladder's own figure".**
- The ladder has no rung at 1/3.
- 0.1222 is a linear interpolation between the 1/6 rung (0.061758) and the 1/√6 rung (0.149297); it computes to 0.12215.
- §2.5 prints "≈ 0.12 at 1/3 by interpolation [C]"; §9 gives "0.1222 … by interpolation".

**84. Dated notes, G-2: "leaves out the 2 tokens each S turn after the first carries from the turn before".**
- (a) "after the first" reads as "after the first S turn". In fact every S turn except **turn 1** carries the 2 tokens. Turn 1 is S in 76 of 160 sessions, so in the other 84 all six S turns carry them.
- (b) By (v)'s own decomposition, the gloss "the user prompt and the passage" also omits the 6-token `<|assistant|>\n` opening, unless "user prompt" is read to include the generation prompt. Say which reading is meant.

### In the entry

**103. (iv): "(passage 4)" and "(passage 11)".** Same as 40: these are passages 5 and 12.

**107. (v): "BK's turn_spans tile the sequence on 160 / 160".** Same as 44.

**108. (v), first list item: "the previous turn's closing `<|endoftext|>` and newline (2 tokens)".**
- This drops the raw's "none for turn 1". In the 76 sessions where turn 1 is S, that S turn has no boundary tokens.
- This is also a raw/entry inconsistency.

**109. (v): "The mean is 616.919 tokens, Fig. A8's 616.91875."** It follows "an S whole-turn span carries", so it reads as a per-span mean. It is the per-session total (one span averages 102.82). Same as 49.

**111. (v), ladder bullet 1: "a 23-token user-turn delta".** Same as 62. The numbers 23, 138, 31 and 320 are right.

**113. (v): "This is why the full-strength slopes are 0.425 against 0.916."** Same as 70.

**114. (v): "§2.5's 0.122 at 1/3 is the ladder's own figure."** Same as 71. Also, §2.5 itself prints "≈ 0.12"; 0.1222 is §9's figure.

**117. (vi): "(PROPOSAL-n v0.2's N1)".**
- The scale-identification N1 is the step-2 referent check's note: results/raw/2026-11-06_n-v0_2_referent-check.md:181, carried in the v0.2 COMMITTED entry at 5916097.
- Within PROPOSAL-n v0.2 itself, "N1" is the replication arm and outcome (28 uses, e.g. "N1 (replication)" at :136).
- The raw has it right ("step 2's N1"), so this is also a raw/entry inconsistency.

**121. (vii): "§0.4's table recomputes from the gate list: 48 / 320 / 960, 'as written' +48 / +640 / +1,920, 'struck' −48 / −320 / −960."**
- The numbers match §0.4.
- Only the struck-beyond totals, and the "struck" row (their complement), follow from v0.2's gate list.
- The "as written" row's arms are not in v0.2's gate list: G-CAL-n at −ρ/2; N1-V at −1/2 and −d_eq; N2-E at −d_eq and −d_20; N1-R at the matching points.
- The raw correctly says those rows are given "as the table has them".

**122. Dated notes, G-1: "the renderer of record reproduces BK's ids for all 160 sessions…".**
- The present tense reads as already done. The renderer is §8 step 6's and is unbuilt; the entry itself says nothing is built.
- The raw says "has to reproduce". Low severity.

**124. G-2: "leaves out the 2 boundary tokens".** Same as 84(b): the gloss also omits the `<|assistant|>` opening. The 2 tokens are absent for turn 1, as in 108.

---

## PASS (105), in brief

### Raw
- **Header (1–7):** the date and HEAD 5916097 match. The gate was model-free: the scripts load only AutoTokenizer, and the venv has no PyTorch. The inputs are as listed. Scratch scripts take their paths as arguments. The venv has Python 3.12.9, transformers 5.5.0 and tokenizers 0.22.2. System python3 has neither library, and jlens-qwen36/.venv is the repo's only venv. The scripts load with local_files_only=True and trust_remote_code=False.
- **Outcome (8):** four notes go to LOCK-n v0.1 (§8 step 10).
- **(i) (9–13):**
  - The URL, commit 7631f8a06cdeffaf8b7a89212e5ccbe55a657732, tree d6f1d50525874355d1ea992f8f652358742ae282 and clean status all match.
  - The commit date 2026-10-05T20:43:51+02:00 is the committer date; the author date is 20:38:24.
  - The step-2 clone (scratch/bk_clone, made Nov 5 20:15) has the same commit and tree.
- **(ii) (14):** 26/26 sha256 OK against the fresh clone, `cmp` byte-identical, and data/n/bk is clean at HEAD.
- **(iii) (15–24):** re-derived as specified.
  - Means 1.090039, 0.507178, −0.755373 and −0.384083.
  - SDs (ddof 0) 0.623307, 0.370276 and 0.454627.
  - Slope 0.916417, SD 0.446579.
  - Random slopes −0.287970 to +0.364064: 24 directions on one shared 40-session set (floor_b0–b7).
  - At +1, 160/160 positive, minimum 0.125008. At −1, 154 negative, maximum 0.406249.
  - SE 0.049431 (0.049277 with the ddof-0 SD).
  - figureA10.csv rows: 0.1492967, 0.0617578, 0.0115104 and 0.4250782.
  - Fidelity: 2,400 reads, median 0.0312492, maximum 0.1250014, 573 above 0.05.
- **(iv) (25–34, 36, 38–39, 41–43):**
  - Hub sha b960243… is `main` today; lastModified 2025-03-14T22:45:15Z; apache-2.0.
  - Sizes and git blob ids (via `git hash-object`) match the hub listing for all 3 files; the sha256s match.
  - The template forms are as stated; it adds no BOS and has no default system turn.
  - `<|endoftext|>` is the only added token (12 per session). The chat markers tokenize as <, |, user/assistant, |, >.
  - The prompts match BK §3.2 and transcript lines 10 and 60; transcript line 3 gives "1273 tokens".
  - Candidate A gives 160/160 and 158/160; B and C give 0/0. The five other serializations give 0 on any candidate.
  - The misses' run, seed, ids_sha and length 1,273 are right. They round-trip, and NFC, NFD, NFKC and NFKD change nothing.
  - My own re-split search finds exactly one hit per miss: ĠBirds 57628 + ong 647 against canonical ĠBird 24214 + song 32851, at 482–483 and 1203–1204.
  - passage_spans, s_spans and u_spans match on 160/160 from character offsets, with exact boundaries. n_pre equals the 12th passage's end and is `<|endoftext|>` on 160/160.
- **(v) (45–46, 48, 50–53, 55–57, 59–61, 63–69):**
  - The turn rule holds on 160/160, and the S-span composition is right.
  - In record 0, tokens 1131–1133 are `<|endoftext|>`, `Ċ`, `<`. Every session has six S and six U turns.
  - The ladder arms are as stated (they are `row_ladder`; the run has 8 arms). The extension grid has 3 anchors plus 1/8, 1/12, 1/16, 1/24 and 1/32, eight cells.
  - Rungs below 1/6 exist only in the extension.
  - Which run supplies the anchors is indeed unstated, but both runs give identical anchor slopes, so it is moot.
  - The CSV sample is `all_recorded_ungated`. The matched values appear in both runs. §2.5 does quote the CSV.
  - The independent-variable and the_widening quotes are exact.
  - spans.json: 23 tokens per sighting, injected_span 138.0/138.0/138.0, prime_tokens 31, 320 sessions; the prime strings are exact.
  - The DV matches `prereg.primary`.
  - Same dose unit: op_member 0.3, resid_rms 25.491, and 0.3 × 25.491 = 7.6473, Panel D's injected_l2.
- **(vi) (72–78):**
  - TAU 0.017883544377937845; precondition_cache prints "TAU = 0.0178835444".
  - The mean of max(|lpS|, |lpU|) over 2,640 reads is exactly 11.153449684153905. The other candidate scales give 10.06–21.2.
  - Retention is 93/233/240/240 (≤ and < agree). 0.20/scale = 0.017931671874052292 exactly.
  - 0 of 2,400 exceed TAU; the maximum ratio is 0.0121432. At TAU/4, 570 exceed (0.2375).
  - The rule 21 hair-trigger reading is right.
- **(vii) (79–80):** 48, 160+160 and 24×40 = 960 follow from G-CAL-n and §2.4. The other rows are as the table has them.
- **Notes, scripts, Not done (81–83, 85–91):**
  - The routing's process line ("minor residues as dated notes") is in RESULTS.md. G-1 is correct. G-2's §2.1 quotes are exact. G-3 and G-4 are correct.
  - All scripts exist at the stated paths, and the snippets match render.py and resplit.py.
  - Decision 7 is "A-m1's OLMo units first, then N-pod", and the routing says "No pod start without my go". The step 5/6 order matches §8.

### Entry
- **92–102, 104–106, 110, 112, 115–116, 118–120, 123, 125–127:** the header claims hold; valence_core/n and LOCK-n are absent. The inputs, (iii), (iv), the ladder numbers, the "dose unit, not geometry" sentence, the two-runs/CSV sentence, (vi), G-3, G-4 and the next-step line all PASS.

### Consistency
- **128:** every figure, hash and count is identical between the raw and the entry. The divergences are already counted at 108, 117, 121 and 122.

## 2. Code's dispositions (each re-checked at source before it was applied)

| item | re-check at source | disposition |
|---|---|---|
| 58 (FAIL) | `strength_ladder/analysis.json`, `members.olmo_32b.under_relative.arms.e6_*.primary`: `differenced_margin_slope_full_n` (n 320) is 0.42508 / 0.14930 / 0.06176, equal to the CSV; `differenced_margin_slope_matched` (n 80) is 0.4595 / 0.1648 / 0.0674. Code's script had taken the first dict carrying a slope | applied: the raw names both estimators, and the entry says the panel's figures are both runs' full-n slopes. The checker's `matched_leverage_note` quote is not repeated: Code did not locate that key on re-check |
| 35, 40, 103 | `neu_b1` run 62 is at 1-based line 3, and "Birdsong" is in passage 5; `neu_b3` run 113 is at line 14, passage 12 | applied: 1-based throughout, stated as such |
| 37 | `prereg.token_identity`'s full clause | applied: quoted in full |
| 44, 47, 107 | `seq_len − n_pre` = 39 on all 160 sessions | applied: "tile [0, n_pre)". The 39-token tail is named, and the closing pair is placed for passages 1–11 only |
| 49, 109 | one S span averages 102.82 tokens (n = 960) | applied: 616.919 is the per-session total; the per-span mean is stated beside it |
| 54 | the extension's `prereg.independent_variable` text | applied: quoted exactly, with "--", and the field named |
| 62, 111 | `prereg.the_widening` | applied: BK's words, "that turn's rendered delta" |
| 70, 113 | `figureA8.csv`'s OLMo `bare` row: 0.5876965, `steered_span_tokens` 137.0458 | applied: the causal sentence is removed. The bases are stated to differ, and the files attribute the gap to no single factor, with the bare row given as the counterexample. The checker's legacy-cell 0.5840 and "no passages" are not repeated: Code did not re-verify them |
| 71, 114 | §2.5 "≈ 0.12 at 1/3 by interpolation"; §9 "0.1222" | applied: named as a linear interpolation between the 1/6 and 1/√6 rungs |
| 84, 124 | turn 1 is S in 76 of 160 sessions; the `<|assistant|>` opening is 6 tokens | applied: G-2 names both omissions |
| 108 | as 84 | applied: "none when the S turn is turn 1" |
| 117 | the referent-check raw's N1 | applied: "the step-2 referent check's N1" |
| 121 | v0.2 §0.4 and the gate list | applied: the struck-beyond totals are said to recompute; the other rows are "as the table gives them" |
| 122 | §8 step 6 is unbuilt | applied: "has to reproduce" |
| unverifiable: "Yes, download" | the PI's word in chat on 2026-11-06 | the entry says "on the PI's word in chat" |
