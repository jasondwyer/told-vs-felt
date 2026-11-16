# n package — BUILD held at its site check (STOP for the seat): the blind values-check

*The n-build session (Code), PI date 2026-11-16.*

- **What was checked:** the block as drafted (sha256 `d341055a…c12f`, 303 lines) and its RESULTS.md entry
  (`90ded485…6345`), whose values-check line was then a placeholder.
- **The checker:** one blind pass by a fresh agent. Its brief quoted the list of record v2's items 1–5 verbatim with
  the coordinating session's lines. It added: no Python, no guard marker in any argv, and no writes but its report.
  It named the sources, not Code's readings of them.
- **Its report** could not be written to a file, because the harness refuses report files from subagents. It came
  back as the agent's hand-back message. Code extracted that message from the agent's transcript with `jq` into this
  raw, unedited: 129 lines, sha256 `31916867…694b`. Its paths are the checker's, with S for Code's scratch
  folder and T for this session's transcript.
- **The counts:** 81 items: 73 CONFIRMED, 5 IMPRECISE, 1 FAIL and 2 NOT CHECKABLE.

## The checker's report, as returned

I could not write the report file. The harness refused it ("Subagents should return findings as text, not write report files"), so the full report is at the end of this message. I removed the empty `S/build/stopcheck` folder I had made for it.

**Counts over 81 items:** 73 CONFIRMED, 5 IMPRECISE, 1 FAIL, 2 NOT CHECKABLE.

**The one FAIL:** item 39, B:73–74. B says G-VEC uses "BK's neutral sessions for R and U". R and U come from the 96 neutral passages of the program's own 544-passage corpus, not from BK's sessions (PROPOSAL-n v0.2:36 §0.8 and :111 G-VEC; the draft `directions.py` agrees). E does not carry this error.

**The five IMPRECISE items, in short:**
- B:31 and E:13 say the diagnostic "read tokenizer files only". It also read BK's committed sessions under data/n/bk (Appendix A line B:235).
- B:55 and E:18 say a newline merges with the punctuation before it. The diagnostic shows that only for `>` and `.`.
- E:14 drops B's scope: the text equality was shown on sessions 0, 62 and 113 only.

**The two NOT CHECKABLE items:**
- B:10, "tokenizer files only": there is no box access, and the box's record says only "no weights".
- B:19, "without torch": hftiny skips if torch *or* transformers is missing, and checking which one the laptop lacks needs Python.

Everything else checked out. That includes all 17 hash abbreviations, the three appendices (byte-identical to their files), the transcript claims, the arithmetic, the labels on Code's readings, and the absence of any IP, port, clock time or token id in B and E.

Two other things you should know:
- The laptop's HEAD is `2822721`, not `14e65d8` as the brief says. That commit only adds to RESULTS.md, and B's `14e65d8` correctly refers to the box's checkout.
- One transcript grep ran past the time limit, and the harness moved it to the background, writing a task-output file outside S/build. I stopped it.

---

# Blind values-check — the n-build STOP block (B) and its RESULTS.md entry (E)

B = S/build/stop_render_full.md (303 lines); E = S/build/entry_stop.md (its VALUESCHECK_LINE placeholder skipped).
Every hash below was computed with `shasum -a 256` and abbreviated with `cut` (first 8 … last 4), never by eye.
T is cited by line number only. Drafts: the tree's and S/build's copies are byte-identical (see observation 2); the
reads below are of the S/build copies, and of the box-run `verify.py` copy in S/mut/m05 where noted.

## Items

1. B:3 — PI date 2026-11-16. Source: T (every message cited below is dated 2026-11-16). **CONFIRMED.**
2. B:5 — PROPOSAL-n v0.2 sha256 `30a3d0f5…04f4`. Source: `git show 14e65d8:PROPOSAL-n-bk-reconciliation-v0_2.md | shasum`, and the clean tree file: both 30a3d0f5…04f4. **CONFIRMED.**
3. B:5, E:5 — the post-build site check is §8 step 6. Source: PROPOSAL-n v0.2:159 ("6. Build the n package … post-build site check"). **CONFIRMED.**
4. B:6, E:6 — package sha256 `d406fa49…1bad`. Source: S/site/out/site_check_out.txt:33; S/pkg_final_hashes.txt:1; site_check_run.txt:44. **CONFIRMED.**
5. B:6, B:14–15, E:6 — the box's checkout at `14e65d8`; a scratch clone with the drafts' tar extracted over it; sparse, with no data/mf3, data/*/ckpt or data/*/reports. Source: site_check_run.txt items 1 and 3 (lines 5–10, 18–29). **CONFIRMED.**
6. B:6–7, E:12 — the G-VER trial is never of record. Source: site_check_out.txt:29; scripts/n_sessions.py:14–16. **CONFIRMED.**
7. B:7–9 — the coordinating session's direction, quoted. Source: T line 6357, a cross-session message from the coordinating session; the quote is word for word. **CONFIRMED.**
8. B:9 — "No code has been changed for it." Source: 13 of the 14 drafts (tree and S/build) match Appendix C. `verify.py` differs at both sites, with the span-check fix of B:137–142. The ids path is unchanged: compared with the box-run copy, `verify()`'s ids branch and sessions.py are the same. **CONFIRMED**, reading "it" as the ids mismatch.
9. B:9–10, E:13 — no checkpoint's weights loaded; hftiny builds a tiny OLMo-2 from a config on the CPU. Source: valence_core/n/hftiny.py:1–7, 34–48; site_check_run.txt item 2 (lines 14–16). **CONFIRMED.**
10. B:10 — "the tokenizer was read from the model's folder, tokenizer files only". Source: site_check_run.txt item 2 records only "the tokenizer through AutoTokenizer.from_pretrained, no weights". "Tokenizer files only" is a declaration (n_sessions.py:15; the diagnostic's docstring). **NOT CHECKABLE.** There is no box access, and `AutoTokenizer.from_pretrained` can also open non-weight files in the folder, such as `config.json`. "No weights" holds either way.
11. B:14, E:5 — "p's pod session". Source: T line 6357 (the coordinating session: "Routed to p's pod session"); site_check_run.txt:1. **CONFIRMED.**
12. B:15–16, E:6 — four of the five steps as expected. Source: site_check_run.txt item 5 (lines 38–48). **CONFIRMED.**
13. B:17, E:7 — step 1, 14/14. Source: site_check_out.txt:2–15, 14 "OK" lines. **CONFIRMED.**
14. B:18, E:8 — step 2, 166/166. Source: site_check_out.txt:19–20. **CONFIRMED.**
15. B:18–19 — on the laptop, a single check records hftiny's checks as skipped, and the count is 156/156. Source: S/pkg_final_selftest.txt ("156/156"); hftiny.py:51–116, with 11 checks on the torch path and one skip check (line 54). In the shell, 166 − 11 + 1 = 156. **CONFIRMED.**
16. B:19 — "on the laptop, without torch". Source: hftiny.py:6, 25–31, 53–55 skip when torch OR transformers is absent. **NOT CHECKABLE**: which one the laptop's interpreter lacks needs Python to check, and Python is barred.
17. B:20, E:9 — step 3, m05 killed, 164/166. Source: site_check_out.txt:21–27 (two hftiny FAILs, exit 1). **CONFIRMED.**
18. B:21, B:135–136, E:10 — step 5's package sha256 and 11 closure lines are byte-identical to the laptop's list. Source: `diff` of site_check_out.txt:33–44 against S/pkg_final_hashes.txt finds them identical, both sha256 d7e61cf7…a668; there are 11 `imported_sha256` lines. **CONFIRMED.**
19. B:22–23 — step 4 is G-VER (`valence_core/n/verify.py`) on the 160 sessions with the real tokenizer, and it returned STOP. Source: site_check_out.txt:28–31 ("sessions": 160, "status": "STOP"); n_sessions.py:86–100 (AutoTokenizer from `--model-dir`). **CONFIRMED.**
20. B:24, E:2 — `ids_ok` 0 of 160; `spans_ok` and `n4_ok` 0; a session whose ids fail is not checked further. Source: site_check_out.txt:30. The box-run verify.py (the S/mut/m05 copy, sha256 1705cf69…8081, equal to Appendix C's line) `continue`s after an ids failure; the current draft's verify.py:56–61 is the same. **CONFIRMED.**
21. B:25–26 — the first five problems are floor_b0's runs 0–4, with lengths 1,233, 1,232, 1,230, 1,231 and 1,232 against `seq_len` 1,273, each with a different `ids_sha`. Source: site_check_out.txt:30. Each of the five `ids_sha` differs from BK's, and they all differ from one another. **CONFIRMED.**
22. B:30–31 — the diagnostic ran on the box on sessions 0, 62 and 113; 62 and 113 are G-DATA's two recorded re-splits. Source: diag_out.txt:11, 16, 21; results/raw/2026-11-06_n-gdata.md:103–112 and 210–215 (G-1); T line 6410 (the pod session's run report). **CONFIRMED.**
23. B:31 — "It read tokenizer files only, wrote nothing and printed no token id." Source: Appendix A, B:235, calls `sessions.load_sessions()`. That function reads the committed BK session files under data/n/bk (sessions.py:42–44, 105–129; site_check_run.txt item 2: "data/n/bk and the code only"). "Wrote nothing" and "no token id" are confirmed by T line 6410 and diag_out.txt. **IMPRECISE.** Suggested wording: "From the model's folder it read tokenizer files only (it also read BK's committed sessions under data/n/bk); it wrote nothing and printed no token id."
24. B:34–35 — on all three sessions the renderer's text equals the chat template's, built as G-DATA (iv)'s candidate A: 5,756, 5,606 and 5,798 characters. Source: diag_out.txt:11, 16, 21. The construction is Appendix A, B:233–243, against G-DATA raw:240–249 and :92 (A). **CONFIRMED.**
25. B:36–41, E:14 (files) — the three tokenizer sha256s equal G-DATA's pins (raw:70–72) and the manifest's `olmo2_instruct` entry (:251–262). The abbreviations are `73fd5254…ecca`, `fff5b944…3fc7` and `78afb564…e2f2`. Source: diag_out.txt:2–4; results/raw/2026-11-06_n-gdata.md:70–72; data/olmo/manifest.json (Read tool): the entry's key is at :170 and the three files at :251–262. **CONFIRMED.**
26. B:42–43, E:15 — tokenizers is 0.22.2 at both sites; transformers is 5.15.0 on the box and 5.5.0 in G-DATA's environment, the laptop's jlens venv (G-DATA's raw line 11). Source: diag_out.txt:1; site_check_run.txt:33; G-DATA raw:11. The venv's site-packages today hold `transformers-5.5.0.dist-info` and `tokenizers-0.22.2.dist-info` (name-only `ls -d`, reached by `cd` and a glob). **CONFIRMED.**
27. B:44 — Python is 3.12.3 on the box and 3.12.9 at G-DATA. Source: site_check_run.txt:33 (the venv the diagnostic also used, T line 6410); G-DATA raw:11. **CONFIRMED.**
28. B:45 — "a Linux pod". Source: not stated in the three box raws. RESULTS.md:1156–1158 (the 2026-11-15 BACKEND entry) records the pod's image as `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`, which is Linux. The seat's 2026-11-15 answers §5.4 assign that pod to n's site checks. **CONFIRMED.**
29. B:46–47 — under 5.5.0, G-DATA reproduced `seq_len` on 160/160 and `ids_sha` on 158/160; the other two matched with one recorded re-split each. Source: G-DATA raw:11, 92, 102–115. **CONFIRMED.**
30. B:48–54, E:16–17 — the four encodings agree: 1,233 (session 0), 1,231 (62) and 1,225 (113), against 1,273; none reproduces `ids_sha`. Source: diag_out.txt:11–25 (`seq_len=1273` on all three; `ids_sha_match=False` in all 12 lines). **CONFIRMED.**
31. B:49–52 — the calls are attributed as follows: `tok(text, add_special_tokens=False)` is G-DATA's; `tok.encode(…, add_special_tokens=False)` is G-VER's; the raw library reads `tokenizer.json`. Source: G-DATA raw:252; n_sessions.py:92–93; Appendix A, B:221 and B:244–247. **CONFIRMED.**
32. B:55 — "On the box, a newline merges with the punctuation before it." Source: diag_out.txt:9–10 show this for `>` (twice) and `.` only, in two probes. **IMPRECISE**: the claim generalizes beyond the evidence. Suggested wording: "On the box, in the diagnostic's probes, a newline merges with the punctuation before it (`>`, `.`)."
33. B:56–58 — the token strings, the same under transformers and under the raw library. Source: diag_out.txt:9–10, which match B:57–58 token for token. **CONFIRMED.**
34. B:59–61 — point 6 is labeled "An inference (Code's)", with "(not run)". Its premise, that the tokenizers library is the same version (0.22.2) at both sites, holds per item 26. **CONFIRMED** (labeling).
35. B:62–64 — point 7 is labeled "A hypothesis on how (Code's, not established)", with three newline-after-punctuation places per turn: after `<|user|>`, after the prompt's closing period, and after `<|assistant|>`. Source: sessions.py:46–49 and 159–166 (both prompts end in "."; the opens are `<|user|>\n` and `<|assistant|>\n`; there is no system turn); G-DATA raw:75–79. **CONFIRMED.**
36. B:65 — 39 places over the twelve turns plus the choice turn. Source: 13 × 3 = 39 in the shell; sessions.py:136 (12 history turns). **CONFIRMED.**
37. B:66 — the seven sessions printed (runs 0–4 by the trial; 0, 62 and 113 by the diagnostic) fall short by 40 to 48. Source: in the shell, 1273 − {1233, 1232, 1230, 1231, 1232, 1231, 1225} = 40, 41, 43, 42, 41, 42, 48. **CONFIRMED.**
38. B:71, E:25 — the BUILD's entry is held. Source: RESULTS.md has no `n package — BUILD` entry for step 6. The newest n entries are the schema and analyzer commits at :24, :81, :219 and :770. **CONFIRMED.**
39. B:73–74 — "G-VEC (step 7): BK's neutral sessions for R and U, the 544-passage corpus, …". Source: PROPOSAL-n v0.2:111 (G-VEC): "the passage corpus committed (`data/n/passages.jsonl`, 544 passages …); the neutral captures give R … and U". PROPOSAL-n v0.2:36 (§0.8): "U the first ten principal components of the 96 neutral representations; … R the RMS residual norm over the neutral corpus's tokens at layer 32". Those 96 neutral passages are "written by this program's design seat". The draft valence_core/n/directions.py:1–14, 43–55 agrees (`N_NEUTRAL = 96`; R over "the neutral corpus"). **FAIL.** R and U come from the corpus's 96 neutral passages, not from BK's neutral sessions; G-VEC tokenizes none of BK's sessions. Suggested wording: "G-VEC (step 7): the 544-passage corpus (its 96 neutral passages give R and U) and the contexts of A3's recipe for N2's directions".
40. B:73–79 — the step numbers: G-VEC 7, G-CAL-n 8, G-TIME-n 11, G-VER 12, the campaign 14. Source: PROPOSAL-n v0.2:159. **CONFIRMED.**
41. B:74 — "the 544-passage corpus" and "the contexts of A3's recipe for N2's directions". Source: PROPOSAL-n v0.2:111, and :81 ("the frozen 1,344-context corpus"); 56 × 8 + 96 = 544 in the shell; the seat's 2026-11-15 answers §5.3. **CONFIRMED.**
42. B:75 — G-CAL-n's prompt and its re-encoded turns. Source: PROPOSAL-n v0.2:113 ("their prompt"; "each re-encoded unsteered"). **CONFIRMED.**
43. B:79, E:26–27 — the BACKEND extension's 24 fresh-versus-cached reads (GA-5). Source: RESULTS.md:7523 and 7589–7590 (GA-5); PROPOSAL-n v0.2:109. **CONFIRMED.**
44. B:80, E:28 — LOCK-n v0.1 (step 10) pins "The rendering and spans". Source: PROPOSAL-n v0.2:117 and :159. **CONFIRMED.**
45. B:81–82, E:29 — Q4 of `718c48e` is BK's label token convention; Code's proposal recovers it on the box against BK's recorded d = 0 log-probabilities. Source: results/raw/2026-11-16_n-schema_code-to-design_questions.md:40 and 134–174 (its only commit is 718c48e, per `git log`); RESULTS.md:637–639. **CONFIRMED.**
46. B:83–84, E:31 — G-ANL-n is step 9 and model-free. Source: PROPOSAL-n v0.2:159; commit 5c0ae6b's subject ("Model-free"). **CONFIRMED.**
47. B:90–94 — option (a): transformers 5.5.0 with tokenizers 0.22.2; the forward takes token ids, not text. Source: G-DATA raw:11; primitive.py:310–318 (`input_ids` built from the ids). The option sits under the "Code's" heading at B:86. **CONFIRMED.**
48. B:95–99 — option (b): the 160 sessions' ids with the two re-splits; N4's 320 told and sham variants; the 12 labels. Source: PROPOSAL-n v0.2:77 ("BK's set of 12") and :92–93 (N4-T 160 + N4-Ts 160 = 320); sessions.py:51–53 (the two recorded splits). **CONFIRMED.**
49. B:104–106 — labeled as "Code's recommendation"; the venv's path carries guard markers. Source: G-DATA raw:11 (the venv's path contains two of the guard strings). **CONFIRMED.**
50. B:107–110 — in the laptop's HF-cache snapshot of `allenai/Olmo-3-1125-32B`, `tokenizer.json` is the pinned one in full, and the other two files are not. Source: the prescribed HF-cache command. `tokenizer.json` 73fd5254…ecca equals the pin in all 64 digits. `tokenizer_config.json` ffa5b2cf…afc6 is not fff5b944…3fc7, and `special_tokens_map.json` 4cb2b529…fb21 is not 78afb564…e2f2. "Small": the manifest gives 4,869 and 581 bytes (:261, :253). **CONFIRMED.**
51. B:111–114 — (c) is labeled; (d) quotes n §2.1. Source: PROPOSAL-n v0.2:77; the quote is word for word. **CONFIRMED.**
52. B:116–118 — Q2: n tokenizes G-VEC's texts and G-CAL-n's prompt and turns; BK's form is transformers 5.5.0's; the conditionals on points 6 and 7. Source: PROPOSAL-n v0.2:111 and :113; G-DATA raw:92 (5.5.0 reproduces BK's ids). **CONFIRMED.**
53. B:122–124 — the quote of BK's `analysis.json` (`prereg.token_identity`) through G-DATA (iv). Source: G-DATA raw:106–107; the quote is word for word. **CONFIRMED.**
54. B:126–129 — " Birdsong" was emitted as `ĠBirds` + `ong`, against the canonical `ĠBird` + `song`; 5.5.0 reproduced every other passage; the pointer is labeled conditional on point 7. Source: G-DATA raw:109–115. B reproduces no token id. **CONFIRMED.**
55. B:130–131, E:20–23 — Code's readings: Q1 (b) and Q2 (BK's form, with generated turns fed back as their emitted ids), pending the seat. Source: B:104 and B:130; E agrees. **CONFIRMED.**
56. B:137–139 — the span check's defect against G-2. Source: a diff of the box-run verify.py (the S/mut/m05 copy, equal to Appendix C) against the current draft. The old `turn_text` was the turn's own user block and passage plus its own closing `<|endoftext|>` and newline. G-2 (G-DATA raw:124–139, 216–222): a span starts where the previous passage ends. **CONFIRMED.**
57. B:140–142 — fixed in the drafts, with a self-test case; it does not bear on the ids; it changes the package hash. Source: verify.py is identical in the tree and in S/build (36b4d0cd…4bb7, against Appendix C's 1705cf69…8081). The diff touches only the span text and its docstring, and adds one check at verify.py:101–103. The ids branch is unchanged. guard.py:4 and 39–40: the package hash covers every `*.py` in valence_core/n. **CONFIRMED.**
58. B:143–145 — the tar carried AppleDouble twins; the pod session's gate refused the first extract and nothing ran on it; the copy was rebuilt without them (the run file, item 3). Source: site_check_run.txt:23–29. **CONFIRMED.**
59. B:146–149 — two transformers warnings at steps 2 and 3: the tiny config's `eos_token_id` lies outside its 128-token vocabulary, and `crop` with a positive value is deprecated, to be removed in 5.18. The call is `cache.crop(n)`, back to the prefill's length. Source: site_check_out.txt:17–18 and 22–23 ("between 0 and 127"); hftiny.py:34 and 40 (vocab 128); primitive.py:334–344. **CONFIRMED.**
60. B:153–154, E:33 — `7c42cb4b…17a8` was quoted to the coordinating session in the routing request, written before the hash command's result had returned. Source: T line 6279 (the message to the coordinating session, with the full wrong value; its first 8 and last 4 digits checked by `cut`). The `shasum` call is at T line 6278, in the same turn; its result arrives at T line 6280, after the message. **CONFIRMED.**
61. B:155 — the full sha256 of `diag_render.py`. Source: `shasum` of S/site/diag_render.py gives the same 64 digits. **CONFIRMED.**
62. B:156 — the correction was sent to the coordinating session and to the pod session. Source: T line 6286 (to the coordinating session); T line 6377 (to the pod session). **CONFIRMED.**
63. B:157–158, E:33–34 — the pod session found the mismatch by hashing the file itself and held the job; nothing ran on the wrong value; the file was never changed. Source: T line 6410, the pod session: "I hashed your file … and found e115d4d9…6291, not 7c42cb4b…17a8. I held the job and asked the coordinating session"; and "Nothing was shipped or run on the old value, and the file was never modified." **CONFIRMED.**
64. B:159–162, E:35–36 — a pruned, name-only `find` was piped into `shasum`: five processes with HF-cache paths in their argv, two of them with guard markers (`mlx-community` + `Qwen3.6`; `Olmo-3`). Source: T line 6625 (the find prunes `*/ckpt`, `*/reports` and `*/data/mf3` and prints names); T line 6626 (five result lines, all in the HF cache, the two marked paths among them); T line 6650 (the disclosure). **CONFIRMED.**
65. B:163–164, E:36 — digests only, with no Python and no model process; disclosed to the coordinating session at once. Source: T line 6625 (`find` | `shasum` | `cut` only). T line 6650 (to the coordinating session) is Code's first message after the event; no message comes between. **CONFIRMED.**
66. B:165 — since then, paths with a marker are reached by `cd` and never put in an argv. Source: T line 6641 (the follow-up uses `cd` and a glob). A case-insensitive scan of the 43 Bash command strings after it in T finds no guard string. **CONFIRMED.**
67. B:169–173, E:37–38 — the three raws' sha256s (`485c4fcf…9650`, `6fc4212a…dce6`, `65d0a53d…1209`) are equal at both ends per the pod session's report; the descriptions of the files. Source: `shasum` of S/site/out/*. T line 6193 gives the pod session's full values for out and run ("sha256 equal at both ends"), and T line 6410 gives diag's. site_check_run.txt:1–3 for the descriptions. **CONFIRMED.**
68. B:176–178, B:182, B:262, B:286 — the appendices' hashes; Appendix C holds the drafts' 14 sha256s. Source: `shasum`; Appendix C is 14 lines. **CONFIRMED.**
69. B:180 — the tar's sha256 is `39828549…a9da`. Source: `shasum` of S/site/n_drafts.tar (hash only); site_check_run.txt:13. **CONFIRMED.**
70. Appendix A (B:185–259) is byte-identical to S/site/diag_render.py. Source: `sed -n '185,259p' | shasum` and the file both give e115d4d9…6291. **CONFIRMED.**
71. Appendix B (B:265–283) is byte-identical to S/site/site_check.sh. Source: both give 65f49ca6…0737. **CONFIRMED.**
72. Appendix C (B:289–302) is byte-identical to S/site/n_manifest.txt. Source: both give 1fe92878…ec34. **CONFIRMED.**
73. Every hash abbreviation in B (16) and E (1). Source: each was recomputed from its full value with `cut`, and each "…" in B and E is one of them: `30a3d0f5…04f4`, `d406fa49…1bad`, `73fd5254…ecca`, `fff5b944…3fc7`, `78afb564…e2f2`, `7c42cb4b…17a8`, `485c4fcf…9650`, `6fc4212a…dce6`, `65d0a53d…1209`, `e115d4d9…6291` (×2), `65f49ca6…0737` (×2), `1fe92878…ec34` (×2), `39828549…a9da`; E:6 `d406fa49…1bad`. **CONFIRMED.**
74. B and E contain no IP address, port, clock time or token id. Source: `/usr/bin/grep` scans (dotted quads; h:mm; UTC/EST/EDT/AM/PM; port/ssh/address/tcp) find none. B's numbers are counts, character counts, session indices, step numbers and dates. **CONFIRMED.**
75. Labels: every inference, hypothesis and reading in B is marked as Code's. Point 6 is "An inference (Code's)"; point 7 is "(Code's, not established)"; B:86 heads its readings "Readings to weigh (Code's; the seat rules)"; B:104 is "Code's recommendation"; B:130 is "Code's reading … Pending the seat"; B:126's pointer is "conditional on point 7". **CONFIRMED.**
76. E:1–4 — the header agrees with B (the title, Q1, Q2, "ids 0 of 160"). The linked block file is not yet in the tree, as expected before the commit. **CONFIRMED.**
77. E:13 — "The diagnosis read tokenizer files only, loaded no weights and wrote nothing." Source: as item 23 (Appendix A, B:235 reads BK's sessions under data/n/bk). **IMPRECISE.** Suggested wording: "The diagnosis read only tokenizer files from the model's folder (and BK's committed sessions), loaded no weights and wrote nothing."
78. E:14 — "The text equals the chat template's". Source: diag_out.txt:11, 16, 21 show it on sessions 0, 62 and 113 only; B:34 scopes it ("On all three sessions"). **IMPRECISE** (the scope is dropped). Suggested wording: "On sessions 0, 62 and 113 the text equals the chat template's, and the tokenizer files are G-DATA's pins."
79. E:18–19 — "On the box a newline merges with the punctuation before it (`>Ċ`, `.Ċ`)." The hypothesis that follows is labeled. Source: as item 32. **IMPRECISE** (minor; the parenthetical names the two observed cases but does not scope the claim). Suggested wording: "In the diagnostic's probes, a newline merges with the punctuation before it (`>Ċ`, `.Ċ`)."
80. E:24–31 — what waits and what does not. Source: these lines agree with B:71–84. E names no inputs for G-VEC, so it does not carry item 39's error. **CONFIRMED.**
81. E:32–38 — Code's errors and the box's outputs. Source: these lines agree with B:151–173 (items 60–67). **CONFIRMED.**

## Observations

1. **HEAD.** The laptop's HEAD is `2822721`, one commit after `14e65d8`. `2822721` adds 53 lines to RESULTS.md and removes none, changes scripts/n_analyze.py and adds two raws. PROPOSAL-n v0.2's sha256 is the same at both commits. Every RESULTS.md line cited above (:620–646, :1141–1158, :7515–7600) is in an entry that `2822721` did not touch. B's `14e65d8` is the box's checkout, which is correct (run file items 1 and 3).
2. **Drafts used.** The tree's and S/build's copies are byte-identical. Thirteen match Appendix C, and `verify.py` is 36b4d0cd…4bb7 at both sites. I read the S/build copies. For the box-run `verify.py` I used S/mut/m05's copy, whose sha256 is Appendix C's 1705cf69…8081. The tar was hashed only.
3. **Evidence B does not cite.** G-DATA's raw:136 records, under transformers 5.5.0, the `<|assistant|>` opening as 6 tokens: `<`, `|`, `assistant`, `|`, `>`, newline. That is, `>` and the newline stand apart. This bears on point 7's `>` case. B:67 says only that a 5.5.0 tokenization would settle points 6 and 7.
4. **Post-hoc label.** B:126 says "G-DATA's re-split shows it". G-DATA labels the re-split search **post hoc** (raw:107); its result became dated note G-1 and the renderer's `RECORDED_SPLITS`. B cites it without that label.
5. **B:10 and item 10.** "Tokenizer files only" rests on declarations. The pod session's record says only "no weights".
6. **A file the commit leaves out.** The run file to be committed names `site_check.exit` (its lines 3 and 35). The pod session reported it as sha256 9a271f2a…86aa, reading 0, which equals the local copy. B does not list it among the committed files, though the run file's item 4 states the exit status (0).
7. **The three box raws.** site_check_out.txt, committed unedited, prints a token id inside the transformers warning at lines 17 and 22: the tiny config's default `eos_token_id`. B and E do not repeat it. The three raws contain no IP address, port or clock time.
8. **Item 66's scope.** The scan covers T, Code's main transcript. Code's subagents' transcripts were not searched.
9. **This check's own conduct.**
   - No Python ran, and no command line contained a guard string. The venv was reached by `cd` and a glob, with a name-only `ls -d` of two dist-info names. The HF cache was checked with the prescribed command, and the manifest read with the Read tool. Git was scoped to named paths throughout.
   - Nothing under data/mf3 was listed or read. A name-only `find` over S/mut and S/overlay printed code copies at valence_core/mf3/verify.py, which is code, not data/mf3.
   - The harness refused the write to S/build/stopcheck/report.md, because subagents may not write report files. I removed the empty folder I had created for it with `rmdir`.
   - One transcript `grep` over T ran past the two-minute limit, and the harness moved it to the background. It wrote its output to the session's task-output file, outside S/build. I stopped it with TaskStop. Nothing else was written.

## Code's dispositions

Each item is applied in the checker's terms unless the disposition says otherwise. Line numbers are the checked
drafts'.

- **Item 39 (FAIL), B:73–74.** Applied. G-VEC's inputs now read "the 544-passage corpus, whose 96 neutral passages
  give R and U (§0.8), and the contexts of A3's recipe for N2's directions". G-VEC tokenizes none of BK's sessions,
  so it falls under Q2 only. Q2 already names G-VEC's texts, and E names no G-VEC inputs.
- **Item 23 (IMPRECISE), B:31.** Applied: "It loaded the tokenizer, through transformers and through the raw library,
  and BK's committed sessions (`data/n/bk`), and no weights". "Tokenizer files only" is dropped here as in item 10,
  since `AutoTokenizer.from_pretrained` may open other files that are not weights.
- **Item 32 (IMPRECISE), B:55.** Applied: "In the diagnostic's probes on the box, a newline merges with the
  punctuation before it (`>`, `.`)".
- **Item 77 (IMPRECISE), E:13.** Applied, in item 23's terms: "loaded the tokenizer and BK's committed sessions, no
  weights, and wrote nothing".
- **Item 78 (IMPRECISE), E:14.** Applied: "On sessions 0, 62 and 113 the text equals the chat template's".
- **Item 79 (IMPRECISE), E:18–19.** Applied. The claim is scoped to the probes as in item 32, and joined with
  observation 3's record.
- **Item 10 (NOT CHECKABLE), B:10.** Rewritten to what the pod session's record holds: the tokenizer "loaded from the
  model's folder through `AutoTokenizer.from_pretrained`, without weights (the pod session's record, item 2)".
- **Item 16 (NOT CHECKABLE), B:19.** Rewritten so that it no longer says which library the laptop lacks: "They need
  torch and transformers; on the laptop a single check records them as skipped".
- **Observation 3.** Applied.
  - Point 7 now cites G-DATA's raw:136, which gives the `<|assistant|>` opening in BK's spans as six tokens, with `>`
    and the newline apart. The box gives five, ending in `>Ċ`.
  - The point's heading is now "Code's hypothesis, one place of it on record".
  - The other two places per turn stay not established.
- **Observation 4.** Applied: "G-DATA's post-hoc re-split search shows it (`results/raw/2026-11-06_n-gdata.md`:107–115)".
- **Observation 6.** Applied. B now says that `site_check.exit` (`9a271f2a…86aa`) reads 0 and is not committed,
  because the run file's item 4 records the same status.
- **Observation 7.** Applied. B now says that the out file, unedited, carries one token id: the tiny config's default
  `eos_token_id`, inside a transformers warning. It carries no session's id.
- **Observations 1, 2, 5, 8 and 9.** No change. Observation 5 is item 10. Observation 8 concerns the guard-marker
  section, which B no longer has (next).
- **Items 64–66 (CONFIRMED), the guard-marker section, and E's matching bullet.** Removed from B and E, on the
  coordinating session's direction.
  - The coordinating session found the event harmless: m's guard counts only processes whose executable is Python
    (`valence_core/m/guard.py`:917–919). It directed that the event be recorded in the BUILD entry.
  - The BUILD entry's draft records it, together with the file-search scope the coordinating session set at the same
    time.
  - B's error section now says that the build's other departures go into the BUILD entry.
- **Not from the check.** (b)'s two routes for the two config files are now stated as options for the seat and the
  PI, the copy going through the pod session. This follows the coordinating session's direction that both belong in
  the block as options, not as steps Code takes.

## The edits after the check, checked by tool

- **The diff.** From the checked drafts to the final ones, it has 13 hunks in B and 3 in E, besides E's
  values-check line. Each hunk is one of the dispositions above, and there is nothing else.
- **The appendices.** After the re-splice, Appendices A, B and C are byte-identical to their files.
- **Each new or changed claim**, asserted against its source, one assertion each; all 14 hold:
  1. the run file's item 2 records the tokenizer through `AutoTokenizer.from_pretrained`, with no weights;
  2. hftiny's `available()` imports torch and transformers;
  3. the diagnostic calls `sessions.load_sessions()`;
  4. `sessions.py` reads `data/n/bk`;
  5. the probes show `>Ċ` and `.Ċ`;
  6. G-DATA's raw:136 gives the six-token opening;
  7. the box's opening is five tokens, ending in `>Ċ`;
  8. PROPOSAL-n:36 names the 96 neutral representations;
  9. PROPOSAL-n:36 is §0.8;
  10. G-DATA's raw:107 says "post hoc";
  11. G-DATA's raw:115 gives 158 + 2;
  12. the out file's lines 17 and 22 carry the eos id;
  13. hftiny sets no `eos_token_id`;
  14. the run file's item 4 records exit 0.
- **The final block:** sha256 `540af2b3…683c`, 309 lines.
