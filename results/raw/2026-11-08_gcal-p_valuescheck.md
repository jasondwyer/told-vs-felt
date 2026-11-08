# G-CAL-p's entry and read: the blind values-check, with Code's dispositions

*Code's raw, PI-local date 2026-11-08. The check ran before the commit of the entry "G-CAL-p-{sft,dpo,instruct}" (RESULTS.md, 2026-11-08) and of `results/raw/2026-11-08_gcal-p_read.txt`. It was a blind subagent given the two texts, the committed sources and the two chat-only quotes. Its report is in section 1, verbatim. Every FAIL and IMPRECISE item, and each of its four further notes, was re-checked at source by Code before it was applied or disclosed (section 0). The fixes were checked by tool, not by a second blind pass.*

## 0. Code's dispositions

| item | verdict | disposition |
|---|---|---|
| #110 (T2 O3) | FAIL | **Applied.** "Clean item 2 is among the weaker clean items (3/4, 4/4, 3/4: 10/12, as items 7 and 13; item 10 is lowest at 9/12)". Checked by tool: the clean per-item totals over the three checkpoints are 10 for items 2, 7 and 13, 9 for item 10, and 11 or 12 for every other item. Following #109's remark, "No item-2 generation names March" now reads "No corrupted item-2 generation". |
| #60 (T1 O2) | IMPRECISE | **Applied.** "did not gain on net, pooled: 55 of 84 against m's 56 (15/20/20 of 28 against 17/20/19, so −2, 0 and +1)". The read raw's O2 now carries the pooled figures too. |
| #64 (T1 O3–O6) | IMPRECISE | **Applied.** "on dpo's and instruct's s2 the garbled verb is read as a month's name and the answer is "3"". |
| #66 (T1 O3–O6) | IMPRECISE | **Applied.** sft: one text (s2) reads `ttf` as an acronym. dpo and instruct: every text names January, and four of their eight gloss "ttf", as a font (s0) or as one of several terms or an unknown one (s2). |
| #115 (T2 O4) | IMPRECISE | **Applied.** Three of the four glossing texts ask for context; dpo s0, cut at the cap, does not. Checked by tool: dpo s0 contains neither "context" nor "clarify", and `cap_hit` is true. Code's own new wording first said "a font, TrueType" for both s0 texts. instruct s0 does not name TrueType (checked by tool), so the read says dpo s0 "names TrueType". |
| #117 (T2 O4) | IMPRECISE | **Applied.** "on sft one text reads it as an acronym (s2), and no sft text names January". Checked by tool: none of sft's four item-8 texts contains "january". |
| #120 (T2 O5) | IMPRECISE | **Applied.** "under m's render only instruct's s1 carried a DEL, followed by text". m's record is `'\x7fThe kernl of the problem is comparirg ...'`. The entry's F-p13 sentence ("Under m's render only instruct's s1 did", that is, carried control characters) was already exact (#72). |
| #133 (T2 O8) | IMPRECISE | **Applied.** Both texts are quoted, checked against m's records: dpo "... is not a standard or recognizable configuration term ..." and instruct "... does not correspond to any standard configuration or known command ...". The same conflation in G-CAL-OLMo's read (`results/raw/2026-11-06_gcal-olmo_read.txt`, its O4) stands as committed and is noted here. |
| Note 1: the disclosure is missing from T1 | — | **Applied.** p §5.4 has every p entry that reports an outcome state the disclosure. The entry now has a "Disclosure (p §5.4; F-p3's sentence, verbatim)" bullet, and the read raw's header carries the sentence too. The run raw's header (`b6ef939`) and `b6ef939`'s message do not. §5.4 names entries, locks, artifacts and posted sentences, and the artifacts carry it (`p.disclosure`, #40). |
| Note 2: the beside-figures are missing from T2 §1 | — | **Applied in the read raw's §1.** The run raw's header (`b6ef939`) also quotes the covariates without them, but its verbatim stdout lines carry them ("beside PROPOSAL-m's +5/16 at the shared renders, Qwen's +9/64, f1's +.078", and likewise for dpo and instruct). It stays as committed. |
| Note 3: O7's scope | — | **Applied.** O7 now opens "In the corrupted pool" and adds the clean pool's texts: `<functions></functions>` closing sft clean 7 s1 and dpo and instruct clean 3 s3, and sft clean 7 s2's "=== Next task === ...". A tool scan of every graded hit for harness markers (`===`, `<functions>`, `[PROLOGUE`, `Session end`, `_ALIGNMENT`, `Q & A`) returns exactly O7's twelve records. |
| Note 4: anchor drift | — | **Applied.** The entry cites `valence_core/p/gcal.py:44–46` at `e03fbe4` and `:40–42` at the BUILD (`a665a09`). `git show` at each commit gives the same three lines. |
| NOT CHECKABLE #38, #79, #80 | — | **Now on the record** in `results/raw/2026-11-08_gcal-p_box-captures.txt`. It holds the copy-back's sha256s at both ends and the box tree after the run, verbatim, and the pod's API record (RUNNING, 1.79, GPU utilization 0). |
| NOT CHECKABLE #4, #7, #23 | — | **Stand as stated.** #7 is chat-only (the go). #4 and #23 describe Code's own conduct: the commands are listed in the run raw's pre-flight section and in the captures raw, and all are read-only. |

## 1. The values-check's report, verbatim

## Values-check: G-CAL-p entry (T1) and its read raw (T2)

I checked 151 claims: **1 FAIL, 7 IMPRECISE, 6 NOT CHECKABLE and 137 CONFIRMED**. The one FAIL is in T2's O3: clean item 2 is not the weakest clean item. All the headline figures check out: counts, bars, covariates, counters, strict grade, identities, hashes, stamps and line citations.

No repo file was edited. The read tool, extracted from READ section 4, was run once with python -B and its output written to scratch. Afterwards `git status` was still the starting 30 lines (1 modified, 29 untracked).

**Abbreviations used in the evidence column.**
- RES = RESULTS.md
- RUN = results/raw/2026-11-08_gcal-p.txt
- READ = results/raw/2026-11-08_gcal-p_read.txt
- p = PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md
- m = PROPOSAL-m-gating-campaign-v1_11.md
- OREAD and ORAW = results/raw/2026-11-06_gcal-olmo_read.txt and results/raw/2026-11-06_gcal-olmo.txt
- RUL = results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md
- R1010 = results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1.md
- "p/m {ckpt} {pool} i sN" is a record key in the p outputs (b6ef939) or m outputs (6ce8b9a).
- "(a)" and "(b)" are your two chat-only excerpts.

### 1. Item table

| # | T | claim (short) | verdict | evidence |
|---|---|---|---|---|
| 1 | T1 | condition (4) PASS ×3; corrupted 47/52/51 of 64; bars 47/46/45 | CONFIRMED | Artifacts: `accuracy.CORR_corrupted.hits` 47/52/51, `condition_4.verdict` PASS. Bars: max(⌈44.8⌉=45, ⌈.75×62⌉=47 / ⌈45.75⌉=46 / ⌈44.25⌉=45) |
| 2 | T1 | clean pool reproduces G-CAL-OLMo's 64 byte for byte on each; flag none | CONFIRMED | 64/64 records equal on all 10 keys against m ckpt and m gates; `p.clean_pool_identity.differing` [] ×3 |
| 3 | T1 | outputs committed at b6ef939 | CONFIRMED | `git show --stat b6ef939`: 3 artifacts, 3 checkpoints and RUN |
| 4 | T1 | "before anything else touched the box" | NOT CHECKABLE | Box activity. Consistent: commit at 05:10:23Z, run end 05:08:26Z (RUN:26) |
| 5 | T1 | Code read all 384 generations | CONFIRMED | READ §3 F has 384 generation lines in 96 item blocks |
| 6 | T1 | PROPOSAL-p v0.2 §3, §8 step 5 | CONFIRMED | p:72, p:128 |
| 7 | T1 | go of 2026-11-07 under the PI's routing of 2026-11-07, item 1 | NOT CHECKABLE | Chat only. Consistent with RUN:1 and b6ef939's message |
| 8 | T1 | G-ANL-p and every later p step wait for the seat's read and the PI's word | CONFIRMED | (b) |
| 9 | T1 | PI item 1 quoted verbatim | CONFIRMED | (a), character for character |
| 10 | T1 | go "GO for G-CAL-p on the box"; one shot per checkpoint; m:176's procedure and seeds pinned | CONFIRMED | (b) |
| 11 | T1 | clean pool checked byte for byte (p §3.1) | CONFIRMED | (b); p:74 |
| 12 | T1 | commit by path first; read every generation; stop and report | CONFIRMED | (b) |
| 13 | T1 | e03fbe4 checks: disclosure, `returned_text`, two pins, paths, self-test, box repo | CONFIRMED | (b) |
| 14 | T1 | pod qny1x4v8padeke, backend 641ee466f4553b6a (BACKEND, 190ba90) | CONFIRMED | `identity.backend_identifier` ×3; RES:1587–1590; 190ba90's subject |
| 15 | T1 | PID 1 running since 2026-11-07T00:17:16Z | CONFIRMED | RUN:571–573; 04:52:14Z − 102,898 s = 00:17:16Z |
| 16 | T1 | that start is before the characterization | CONFIRMED | RES:1594/1603/1605: created 00:17:14Z, integrity from 00:23:05Z, determinism to 00:33:38Z |
| 17 | T1 | p §6.2 needs no new BACKEND entry | CONFIRMED | p:110: an entry only if the box is not qny1x4v8padeke at 641ee466… |
| 18 | T1 | box HEAD e03fbe4, tree clean | CONFIRMED | RUN:550 ("dirty 0"), RUN:535 |
| 19 | T1 | env.sh f5174faa…, G-CAL-OLMo's | CONFIRMED | RUN:561/564; ORAW:4 |
| 20 | T1 | torch 2.8.0+cu128, transformers 5.15.0, as in G-CAL-OLMo | CONFIRMED | RUN:569, RUN:46; ORAW:38/183/328 |
| 21 | T1 | GPU idle | CONFIRMED | RUN:552 (0 MiB, 0 %), RUN:553 (0 python processes), RUN:536 |
| 22 | T1 | precheck clear ×3, pod id from env.sh | CONFIRMED | RUN:549–559 |
| 23 | T1 | pre-flight "all read-only" | NOT CHECKABLE | Only the raw's own label (RUN:548) |
| 24 | T1 | `p_sessions.py gcal --unit OLMo-{ckpt}`, no `--resume`, back to back | CONFIRMED | RUN:4/29/185/345; stamps RUN:20–25, each launch equal to the previous end |
| 25 | T1 | wrapper path; sha256 9f8b9df3… | CONFIRMED | RUN:3/502/532–534. The sha256 of RUN:503–526 plus a newline recomputes to 9f8b9df3…d67c |
| 26 | T1 | DRIVER 1140b57e… | CONFIRMED | RUN:30; equals the sha256 of scripts/p_sessions.py at e03fbe4 and b6ef939 |
| 27 | T1 | ran 04:53:27Z → 05:08:26Z, about 15 minutes | CONFIRMED | RUN:20, RUN:26; 14 min 59 s |
| 28 | T1 | p §6.1 planned under half an hour | CONFIRMED | p:108 |
| 29 | T1 | chain rule declared, dry-tested on 7 cases; continue/halt rule as stated | CONFIRMED | RUN:5, RUN:574; wrapper RUN:519–524 |
| 30 | T1 | all three exited 0 | CONFIRMED | RUN:21/23/25 |
| 31 | T1 | sft row: 62/64, 47/64, yes, yes (93/128), bar 47, +15/64, 64/64, PASS | CONFIRMED | 94/128 ≥ 93/128; (62−47)/64 |
| 32 | T1 | dpo row: 61/64, 52/64 = 13/16, yes, yes (183/256), bar 46, +9/64, 64/64, PASS | CONFIRMED | 208/256 ≥ 183/256 |
| 33 | T1 | instruct row: 59/64, 51/64, yes, yes (177/256), bar 45, +1/8, 64/64, PASS | CONFIRMED | 204/256 ≥ 177/256; 8/64 = 1/8 |
| 34 | T1 | bars are §3.2's, known in advance | CONFIRMED | p:76; `p.binding_bars_if_clean_reproduces` |
| 35 | T1 | sft has no margin: one hit fewer is a FAIL | CONFIRMED | 46/64 = 92/128 < 93/128 |
| 36 | T1 | covariates beside m's (+5/16, +17/64, +17/64), Qwen's +9/64, f1's +.078; they go into LOCK-p v0.1 | CONFIRMED | p:76; `p.covariate_beside` |
| 37 | T1 | the six files' sha256s listed in the raw match the commit | CONFIRMED | RUN:11–16 equal the sha256s of the b6ef939 blobs |
| 38 | T1 | sha256s "compared at both ends" | NOT CHECKABLE | Box side; RUN:10 states it |
| 39 | T1 | identity `proposal_sha256` = m v1.11's; `proposal_p_sha256` = p's | CONFIRMED | 42ab36ec…6c6b and 42f2977b…3b32 equal the two files' sha256s, ×3; RUL:11 |
| 40 | T1 | artifact carries the ruled disclosure and `licence_at_run` | CONFIRMED | `p.disclosure` equals the RUL:7 sentence exactly, ×3; `p.licence_at_run` present (both in the p block) |
| 41 | T1 | top-level `stage` "G-CAL-OLMo", `procedure`, `on_fail` are m's | CONFIRMED | Equal to the m gate artifacts' fields, ×3 |
| 42 | T1 | the BUILD's PIN, valence_core/p/gcal.py:44–46 | CONFIRMED | The text is at :44–46 at HEAD (also e03fbe4). At the BUILD (a665a09) it sat at :40–42 |
| 43 | T1 | p's stage name, unit name and failure consequence are in the `p` block | CONFIRMED | `p.stage`, `p.unit_name`, `p.on_fail` |
| 44 | T1 | clean identity 64/64 on 7 fields; generation-path fields equal | CONFIRMED | Recomputed; 13 path fields all `equal: true` |
| 45 | T1 | items 0 and 12 render as m's; 8/8 per checkpoint | CONFIRMED | Renders equal; 8/8 records identical ×3 |
| 46 | T1 | all 72 shared (prompt, seed) pairs reproduce, about 26 h apart, same container | CONFIRMED | 64 + 8. 02:20:02Z on 11-07 (ORAW:24) to 04:53:27Z on 11-08 is 26 h 33 min; both after 00:17:16Z |
| 47 | T1 | 0/384 line breaks; 0/384 cuts | CONFIRMED | Recomputed; `cuts` [] ×3; hair trigger 0 |
| 48 | T1 | the cut path ran only in the self-test | CONFIRMED | Scripted cut cases at valence_core/p/proxy.py:128–132; real cuts 0 |
| 49 | T1 | motivating texts came from m's item-15 render; p's same keys give harness text with no line break | CONFIRMED | m dpo/instruct corrupted 15 s0 begin "---\n\nTask: …"; p gives '**DRAFT ANSWER' and '=== The above line…===' |
| 50 | T1 | counters 1/2/2, 2/3/5, 8/5/2, 1/1/1, 0/1/0 | CONFIRMED | `report.counters` recomputed equals the artifacts |
| 51 | T1 | strict grade 41/29, 39/31, 43/33 | CONFIRMED | Recomputed equals the artifacts |
| 52 | T1 | spelling hit dpo clean 4 s1, `true` against `three`; F-p11's class; same text as G-CAL-OLMo | CONFIRMED | The only candidate (Levenshtein 2); m dpo record identical; RES:169–173 |
| 53 | T1 | each counter's keys are in READ §3 B | CONFIRMED | READ:54–58, 77–81, 100–104 |
| 54 | T1 | twelve observations | CONFIRMED | READ:14–27 (O1–O12) |
| 55 | T1 | quote of the 2026-10-10 ruling | CONFIRMED | R1010:19 |
| 56 | T1 | O1 graded hits: 7 s2 (iron, then masses equal); 11 s0 `up=down` | CONFIRMED | p sft corrupted 7 s2 and 11 s0 |
| 57 | T1 | O1 misses: 13 s3 `2 4`; 2 s3 `3rd month of the year` | CONFIRMED | p sft records |
| 58 | T1 | Compute 24/24 on each; m 20/19/18 | CONFIRMED | Per-item recount, classes taken from the clean task's first words |
| 59 | T1 | Write 8/8/7 of 12; m 5/5/5 | CONFIRMED | Recount |
| 60 | T1 | State/Name "did not gain on net": 15/20/20 against 17/20/19 | IMPRECISE | instruct gained +1 (19→20). No net gain holds only pooled (55 against 56) and on sft (−2) and dpo (0) |
| 61 | T1 | "where §3.3 expected them" | CONFIRMED | p:78: "toward their clean 26/25/23" |
| 62 | T1 | totals 47/52/51 against the seat's ≈53/52/50 | CONFIRMED | p:78 |
| 63 | T1 | item 2 stays at 0/12, content intact | CONFIRMED | p 0/12; m 0/12 |
| 64 | T1 | dpo and instruct read "Niye" as a month's name and answer "3" | IMPRECISE | Only s2 on each. Their s0/s1/s3 are 'April', '(<month name>, <number of days', 'Correctness:' |
| 65 | T1 | item 8: sft 0/4 against m's 3/4; dpo and instruct 4/4 | CONFIRMED | Recount |
| 66 | T1 | dpo and instruct 4/4 "glossing it as a font format" | IMPRECISE | Only 4 of the 8 gloss "ttf" (dpo s0, s2; instruct s0, s2). Of those, dpo s0 and instruct s0 read it as a font; dpo s2 as one of several terms; instruct s2 as an unknown event or process. s1 is 'January ttf', s3 a plain answer |
| 67 | T1 | item 7 s1 lone DEL and s3 '``' on all three | CONFIRMED | Records |
| 68 | T1 | item 15's misses are all harness text | CONFIRMED | The 8 misses |
| 69 | T1 | DEL ×3 (7 s1); ANSI 7 s0 dpo/instruct; config-topic sft corrupted 12 s0 is G-CAL-OLMo's text | CONFIRMED | Records; item 12 identical to m |
| 70 | T1 | mirroring 4/4/4 against G-CAL-OLMo's 12/6/9 | CONFIRMED | `m_gcal.olmo_tallies` recomputed; RES:1456–1458 |
| 71 | T1 | F-p13: five texts, all on item 7 (DEL s1 ×3; ANSI s0 dpo/instruct) | CONFIRMED | `report.control_chars` |
| 72 | T1 | under m's render only instruct's s1 carried one | CONFIRMED | m control characters: instruct corrupted 7 s1 only |
| 73 | T1 | §2.3 counts them; nothing gates them | CONFIRMED | p:68; the hair trigger is line breaks only (report.py) |
| 74 | T1 | in a session such a text is a stored round body the next round sees | CONFIRMED | p:64, p:66 |
| 75 | T1 | quote: "A checkpoint passing → its LOCK-p v0.1 (§4.3)" | CONFIRMED | p:76, verbatim |
| 76 | T1 | quote: "PASS continues to step 6 later" | CONFIRMED | (b) |
| 77 | T1 | step 6 is `p_analyze.py`, G-ANL-p, then each LOCK-p v0.1 | CONFIRMED | p:129 |
| 78 | T1 | nothing is pushed | CONFIRMED | `git branch -vv`: main ahead 5 of origin/main 1e79955 (local tracking ref; no remote contacted) |
| 79 | T1 | box repo holds the six files untracked and byte-identical | NOT CHECKABLE | Box state. Consistent with the .gitignore:300/:306 admit lines |
| 80 | T1 | pod RUNNING and idle | NOT CHECKABLE | Live state |
| 81 | T1 | $1.79/hr; up since 2026-11-07T00:17Z | CONFIRMED | RES:1596; p:108; RUN:571 |
| 82 | T2 | header: all 384 generations | CONFIRMED | §3 F |
| 83 | T2 | m:271 quote | CONFIRMED | m:271, verbatim |
| 84 | T2 | p §8 step 5 quote | CONFIRMED | p:128, verbatim |
| 85 | T2 | PI-local date 2026-11-08 | CONFIRMED | Consistent with b6ef939's 2026-11-08 −0500 date and the entry date |
| 86 | T2 | grader description (f0's, whole word) | CONFIRMED | m:176; valence_core/m/gcal.py:184–193 |
| 87 | T2 | strict grade and counters decide nothing | CONFIRMED | p:68, p:74 |
| 88 | T2 | 2026-10-10 A1 ruling, as OREAD quotes it | CONFIRMED | OREAD:2; R1010:19 |
| 89 | T2 | sources: p files at b6ef939, m files at 6ce8b9a, golds from `load_pool()` | CONFIRMED | git log; tool source line 45 |
| 90 | T2 | tool sha256 0faf9d0a… equals section 4 | CONFIRMED | Recomputed over READ:656–907 |
| 91 | T2 | section 3 is the tool's output, verbatim | CONFIRMED | Re-ran the extracted tool: 624 lines, empty diff against READ:30–653 |
| 92 | T2 | run raw is at b6ef939 | CONFIRMED | git |
| 93 | T2 | §1 sft row (margin 0, strict 41/29, cuts 0) | CONFIRMED | Recomputed |
| 94 | T2 | §1 dpo row (margin +6, strict 39/31) | CONFIRMED | Recomputed |
| 95 | T2 | §1 instruct row (margin +6, strict 43/33) | CONFIRMED | Recomputed |
| 96 | T2 | G-CAL-OLMo corrupted 42/44/42; +5/16, +17/64, +17/64 | CONFIRMED | m records |
| 97 | T2 | §1 counters line | CONFIRMED | Recomputed |
| 98 | T2 | O1: 47 against 47; 93/128 = 46.5 of 64 | CONFIRMED | Arithmetic |
| 99 | T2 | O1: quote "Both a kilogram of iron … weigh the same" | CONFIRMED | p sft corrupted 7 s2, verbatim |
| 100 | T2 | O1: 'up=down' normalizes to 'up down' | CONFIRMED | `normalize` |
| 101 | T2 | O1: misses 13 s3 and 2 s3 | CONFIRMED | Records |
| 102 | T2 | O2: class totals, m's, and three §3.3 quotes | CONFIRMED | Recount; p:78 |
| 103 | T2 | O2: totals against ≈53/52/50 | CONFIRMED | p:78 |
| 104 | T2 | O2: item 9 12 vs 2, item 14 12 vs 7, item 5 12 vs 8, item 11 7 vs 3 | CONFIRMED | Recount |
| 105 | T2 | O2: State/Name −2/0/+1; items 1, 4, 8, 7, 13, 2, 10 deltas | CONFIRMED | Recount (the deltas make the net sense explicit) |
| 106 | T2 | O2: item 15 2/1/1 under both renders | CONFIRMED | Recount |
| 107 | T2 | O3: item 2 render; 0/12 as under m's render | CONFIRMED | Records |
| 108 | T2 | O3: miss texts by seed | CONFIRMED | Records |
| 109 | T2 | O3: "No item-2 generation names March" | CONFIRMED | True of the corrupted pool, which is the context. Clean item 2's hits do name March |
| 110 | T2 | O3: "Clean item 2 is the weakest clean item (3/4, 4/4, 3/4)" | **FAIL** | Clean item 10 is 4/4, 3/4, 2/4 = 9/12 (dpo s2 '…<answer'; instruct s0 'Four', s2 '…<answer'). Item 2 (10/12) ties items 7 and 13 |
| 111 | T2 | O3: four "correction" hits | CONFIRMED | sft s2, dpo s2 and s3, instruct s3; OREAD:54 |
| 112 | T2 | O4: render; "the"→"ttf", "of"→"oe" | CONFIRMED | Render/task diff, 3 positions |
| 113 | T2 | O4: sft '1','2','1. TTF…','<code'; m 3/4 | CONFIRMED | Records |
| 114 | T2 | O4: dpo and instruct 4/4 (m 2/4); every text names January | CONFIRMED | Records |
| 115 | T2 | O4: four gloss "ttf" "and ask for context" (dpo s0, s2; instruct s0, s2) | IMPRECISE | dpo s0 asks for no context; its stored text is cut at the cap. 3 of the 4 ask |
| 116 | T2 | O4: two answer 'January ttf' (s1) | CONFIRMED | Records |
| 117 | T2 | O4: "on sft that reading displaces the answer" | IMPRECISE | Only sft s2 shows the acronym reading; s0 '1', s1 '2', s3 '<code' show none |
| 118 | T2 | O5: 2/4, 2/4, 1/4 (m 3/4, 4/4, 2/4) | CONFIRMED | Recount |
| 119 | T2 | O5: s1 lone DEL and s3 '``' on all three | CONFIRMED | Records |
| 120 | T2 | O5: "(under m's render instruct's s1 only)" after "a lone DEL" | IMPRECISE | m's instruct 7 s1 is '\x7fThe kernl of the problem…', a DEL followed by text, not a lone DEL |
| 121 | T2 | O5: s0 texts (sft; dpo's ANSI string exact; instruct a miss) | CONFIRMED | Records |
| 122 | T2 | O5: s2 texts (sft and dpo cap hits; instruct "1 kg vs. 0.5 kg") | CONFIRMED | Records |
| 123 | T2 | O6: item 13 '2+2'/'2 4'; 2/4, 2/4, 3/4 (m 2/4, 3/4, 4/4) | CONFIRMED | Records |
| 124 | T2 | O6: item 11 misses | CONFIRMED | Records |
| 125 | T2 | O6: item 15 misses | CONFIRMED | Records |
| 126 | T2 | O6: item 1's one miss, '6' (sft s0) | CONFIRMED | Records |
| 127 | T2 | O7: control-character hits are the DEL and ANSI texts (1/2/2) | CONFIRMED | Counter keys |
| 128 | T2 | O7: harness text closing a graded hit (list) | CONFIRMED | Complete for the corrupted pool, by a scan of all 384 texts |
| 129 | T2 | O7: sft 14 s3 quiz quote | CONFIRMED | Verbatim, double space included |
| 130 | T2 | O7: '**DRAFT ANSWER' and '**Final Answer' are outside the declared forms | CONFIRMED | report.py `LISTED_FORMS`; banner's 8 strings; the '=== … ===' rule |
| 131 | T2 | O7: sft corrupted 0 s0/s2 are G-CAL-OLMo's texts | CONFIRMED | Item 0 identical to m |
| 132 | T2 | O8: sft corrupted 12 s0 configuration quote; G-CAL-OLMo's text | CONFIRMED | Records |
| 133 | T2 | O8: m dpo and instruct item-14 quote "…is not a standard…" | IMPRECISE | That wording is dpo's. instruct's 14 s3 reads "…does not correspond to any standard configuration…" (OREAD:56 has the same conflation) |
| 134 | T2 | O8: the config readings do not recur under 'Comkuva 8 times 8.' | CONFIRMED | p item-14 texts |
| 135 | T2 | O8: the other §3 H matches | CONFIRMED | Re-scan gives the same 9 records |
| 136 | T2 | O9: 64/64 plus 8/8; 72/72; 02:20Z on 11-07, 04:53Z on 11-08 | CONFIRMED | As rows 44–46 |
| 137 | T2 | O9: cross-checkpoint 98 (48), 75 (30), 68 (28); G-CAL-OLMo 95, 66, 61 | CONFIRMED | Recomputed; OREAD:58 |
| 138 | T2 | O9: the key has no checkpoint field (OREAD O6) | CONFIRMED | m:176 seed form; OREAD:58 |
| 139 | T2 | O10: 0/384, 0/384; the two motivating keys; their p texts | CONFIRMED | Records |
| 140 | T2 | O11: p's spec does not declare R1 A6's tallies | CONFIRMED | No "A6" or tallies in p or valence_core/p |
| 141 | T2 | O11: (iii) 0/0/0; (iv) 4/4/4, hits 4/3/3; m 12 (9), 6 (4), 9 (5) | CONFIRMED | `olmo_tallies`; RES:1456–1458 |
| 142 | T2 | O11: mirroring words and keys | CONFIRMED | `olmo_tallies` keys |
| 143 | T2 | O11: 'Ther are 7 days in a week' (dpo/instruct 1 s1) | CONFIRMED | Records |
| 144 | T2 | O11: (i) 6/6/5; dpo 7 s0 the only non-statement; clean candidates all state it | CONFIRMED | Records; OREAD:13–24 |
| 145 | T2 | O11: (ii) none of the 8 item-15 misses is "close" | CONFIRMED | Records |
| 146 | T2 | O12: strict figures; graded-hit strict misses "mostly" sentences or arithmetic | CONFIRMED | 106 of 116 by my classification; both examples are in the lists |
| 147 | T2 | O12: strict grade's own artifacts (checklist dpo/instruct clean 4 s0; 'January ttf') | CONFIRMED | Strict recompute |
| 148 | T2 | O12: spelling 0/1/0 detail | CONFIRMED | As row 52 |
| 149 | T2 | O12: no 'Januwy', 'Janaury' or 'dn' in any p text | CONFIRMED | Word scan (Janbaa and Janyooar absent too) |
| 150 | T2 | O12: cap hits 8/5/2 (G-CAL-OLMo 6/9/9) | CONFIRMED | Records; OREAD:59 |
| 151 | T2 | O12: refusals 1/1/1, each clean 7 s1; sft's a hit, dpo's and instruct's misses | CONFIRMED | Records |

### 2. FAIL and IMPRECISE items, with the correct value

**FAIL**
- **#110 (T2 O3):** clean item 2 is not the weakest clean item. Clean item 10 is weaker at 9/12 (4/4, 3/4, 2/4). Item 2 is 10/12 and ties items 7 and 13. A correct wording would be "one of three clean items at 10/12; item 10 is lowest at 9/12".

**IMPRECISE**
- **#60 (T1 O2):** instruct's State/Name gained 1 (19→20). Say "no net gain pooled (55 vs 56): −2, 0, +1", as T2 does.
- **#64 (T1 O3–O6):** the "Niye" month reading and the answer "3" occur on s2 only, for both dpo and instruct.
- **#66 (T1 O3–O6):** only 4 of the 8 dpo/instruct texts gloss "ttf" (s0, s2), and only some of those as a font. s1 answers 'January ttf' and s3 answers plainly.
- **#115 (T2 O4):** dpo s0 glosses "ttf" as a font but asks for no context. Three of the four ask.
- **#117 (T2 O4):** the acronym reading on sft is s2 only.
- **#120 (T2 O5):** under m's render, instruct's 7 s1 was a DEL followed by text, not a lone DEL.
- **#133 (T2 O8):** the quoted wording is dpo's. instruct's reads "does not correspond to any standard configuration".

### 3. Counts by verdict

| verdict | count |
|---|---|
| CONFIRMED | 137 |
| FAIL | 1 |
| IMPRECISE | 7 |
| NOT CHECKABLE | 6 (#4, #7, #23, #38, #79, #80) |
| **Total** | **151** |

### Things you may want to fix (outside the count)
- **Disclosure missing from T1.** p §5.4, with its date corrected by F-p3, asks every p entry that reports an outcome to state the disclosure. T1 only says the artifact carries it.
- **Beside-figures missing from T2 §1.** p §3.2 asks for Qwen's +9/64 and f1's +.078 wherever a covariate is quoted. T2 §1 quotes p's and m's covariates without them; T1 includes them.
- **O7 list scope.** It omits three clean-pool graded hits that also end in '<functions></functions>': sft clean 7 s1, and dpo and instruct clean 3 s3. All three are G-CAL-OLMo's texts.
- **Anchor drift.** The gcal.py:44–46 citation is correct at HEAD, but the BUILD (a665a09) had the PIN at :40–42. Pinning the citation to a commit would stop it drifting.

My scripts and the tool's output are in <tmp>/scratchpad/podwatch/vc/ (the tool output is tool_out.txt there).
