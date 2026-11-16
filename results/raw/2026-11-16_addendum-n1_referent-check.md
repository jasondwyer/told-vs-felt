# ADDENDUM-n1 v0.1: the referent check of its §8.4, and Code's grading (PI date 2026-11-16)

Code's raw for `ADDENDUM-n1 v0.1 — COMMITTED`. The addendum's §8.3 (1) asks for "referent check of 8.4; an
unresolved substantive item → STOP". One fresh blind checker, a subagent of the coordinating session, under a brief
quoting the list of record v2's items 1–5 (with item 4's amendment by C.2 of this date) and allowing no interpreter,
checked every statement of the addendum that quotes, cites, paraphrases or gives a number from a referent §8.4 lists,
and the other sources the addendum cites. Its report is reproduced whole, as its hand-back message gave it; it held
no local path. Code's grading and dispositions follow it.

## 1. The checker's report, whole

BLIND REFERENT CHECK: ADDENDUM-n1 v0.1. The addendum's §8.4 list has no FAIL. Six items are IMPRECISE: one substantive (an edge case), five minor.

**Header**
- **Document:** `ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md`. sha256 confirmed: e979f8f2af08ddb1f32e3054c002b1d0a3278e49a24b4f6df2cb6c042de95e03. Untracked at root (`??`). Read in full, 86 lines.
- **What I read:**
  - PROPOSAL-n v0.2 in full. sha256 30a3d0f5…04f4, abbreviated by `cut`. Tracked, clean, and the same blob at 8e3bf91 as now, so the `n:N` anchors hold.
  - RESULTS.md: the "PROPOSAL-n v0.2 COMMITTED" entry (:8351–8420), and 14e65d8's entry (`git show 14e65d8 -- RESULTS.md`; now :290ff).
  - The three blocks, by `git show <commit>:<path>`: 645bd3f's STOP block and its diag output, 718c48e's questions, 8e3bf91's prebuild.
  - Both seat answer raws, in full.
  - CLAUDE.md rules 5, 9, 11, 23, 27, 28(a).
  - `data/olmo/manifest.json` :170 and :240–271. The blob is the same at 645bd3f, at HEAD and in the working copy.
  - G-DATA's raw `results/raw/2026-11-06_n-gdata.md`, which 645bd3f cites: :1–30, :55–150, :205–232.
  - Under `data/n/bk`, only: the cue labels and record counts in the 14 skeleton files, `analysis.json`'s `token_identity`, `prereg.json`'s d(0) sentence, and the decimal places of 80 `reduced.json` values (values not printed).
  - PROPOSAL-k :205–272; `valence_core/echo/probe.py`:19–25; `valence_core/n/schema.py` (grep lines); `scripts/n_analyze.py`:2254; RESULTS.md :1030–1038 (5a97527's entry).
- **Tools:** shasum; `git show` (blobs, `--name-status`, the RESULTS.md diff); `git ls-files`; `git status --porcelain` scoped to named paths only; `git rev-parse` / `git hash-object` compared in the shell; `git log -1 --format`; /usr/bin/grep, sed, awk, cut, rev, sort, uniq, tr, `wc -l`, `cat -n`; name-only `ls`; the Read tool.
- **What I did not do:**
  - Ran no interpreter of any kind (no python, node, ruby or perl).
  - Edited nothing and wrote no file.
  - Used no `--stat` or `--numstat`, ran no whole-tree status, and read nothing under `data/mf3`, `ckpt` or `reports`.
- A statement that draws on several referents is listed under each.

**CLAIMS**

**A. PROPOSAL-n v0.2 (n:N = line N) and its COMMITTED entry**
1. Header: "tracked at root, sha256 `30a3d0f5…04f4`". CONFIRMED. `shasum`; `git ls-files`; RESULTS.md:8353–8354 gives the full hash.
2. Header: "the file its `PROPOSAL-n v0.2 — COMMITTED` entry names". IMPRECISE (minor).
   - RESULTS.md:8351 is headed "PROPOSAL-n v0.2 COMMITTED (routed by the PI, PI date 2026-11-06) at its §8 step 3", with no dash.
   - The dashed form is the name v0.2 declares: n:158 "entry `PROPOSAL-n v0.2 — COMMITTED`", and n:161.
   - The entry does name the file and its sha256.
3. Header: "the Clock (D_n 2026-12-15)". CONFIRMED. n:152 "D_n (N-pod) proposed **2026-12-15**"; routed at RESULTS.md:8363 and :8398.
4. Header: `k §N` = PROPOSAL-k-echo-channel.md; `m:N` = PROPOSAL-m v1.11 at root. CONFIRMED. Both are tracked; PROPOSAL-m's header reads "## v1.11", sha256 42ab36ec…6c6b, as n:4 pins.
5. §0.1: "n §2.1 names the bar — token identity with each record". CONFIRMED. n:77 "asserted token-identical to each record's `seq_len` (and `ids_sha` where its serialization is reproduced, §3)".
6. §0.2: n §2.2 captures at the injection layer. CONFIRMED. n:79 "captured at layers 32 and the final layer"; n:81 "Site: layer 32 of 64". The seat accepted this reading at build raw :39.
7. §0.4: "LOCK-n v0.1, v1.0"; "every referent of n §9". CONFIRMED. n:117, n:120, n:163–165.
8. §1.2 (ii): N4's line goes between the choice prompt's two sentences. CONFIRMED. n:77 gives the prompt; n:95 gives "Prefer [zone X]." / "Either is fine.", "appended to the choice prompt before "Reply with ONLY…"". The slot names [A]/[B] are the seat raw's verbatim; n:77 writes "[zone A]/[zone B]".
9. §1.2 (iv): "the 544 of `data/n/passages.jsonl`", "the 1,344". CONFIRMED. n:111 "`data/n/passages.jsonl`, 544 passages"; n:81 "1,344-context corpus".
10. §1.3: G-VER runs before any read, and a mismatch is a G-VER-STOP. CONFIRMED. n:119 "before any read; mismatch → STOP"; n:134 "a G-VER STOP".
11. §1.3: "The BACKEND extension's 24 reads". CONFIRMED. n:109 "over 24 reads".
12. §1.4: "48 at each of +ρ, −ρ and +ρ/2", "the 48 baseline turns", and the seat's read of every turn. CONFIRMED. n:113; per-dose batches at n:20, n:25 and n:49.
13. §1.5: LOCK-n v0.1's "rendering and spans". CONFIRMED, an exact substring of n:117 "The rendering and spans;".
14. §2: the 40 floor sessions (`floor_b0–b7`). CONFIRMED. n:52, n:81; the floor_b0–b7 skeleton files hold 40 records (counted).
15. §2: "n §2.1's summed log-probability". CONFIRMED. n:77 "each summed over its tokens".
16. §2: "n §4's blinding concerns margins under steering before VERDICTS". IMPRECISE (minor).
    - n:130 says "the blinding question is who sees margins before VERDICTS: nobody." It has no "under steering" limit.
    - The narrowing is the seat's reading. Build raw :37: "n §4's rule is about margins under steering before VERDICTS".
17. §3: "The label-mass counter (n §4)". CONFIRMED. n:128 "Counters (rule 23): … label-mass floors on the restricted read".
18. §3: "two-label first-token read". CONFIRMED, verbatim at n:77.
19. §4: "Nothing is generated in the campaign (n §2.1, §0.4)". CONFIRMED. n:77 "No new text is generated for N1, N2 or N4."; n:16.
20. §4: "the committed free-text reply's agreement with the margin's sign". CONFIRMED, verbatim at n:128.
21. §5.1: points within 0.05 merge. CONFIRMED. n:81 "a point within 0.05 of an existing one is merged".
22. §5.1: "(C12's floors are per point)". IMPRECISE (minor).
    - n:62 (C12): "each arm's floor is the 24 random slopes refit on that arm's own dose points (random reads exist at every point)".
    - n:126: one floor per arm. It is not a per-point figure.
23. §5.2: "640 or fewer reads"; §0.4's negative counts unchanged. CONFIRMED. n:89 (160 sessions; 160 × 4 = 640); n:23 (N1-P at −1 = 160; the added points are positive).
24. §5.3: d_20 = 1 by the cap; the norms are equal exactly at d_eq vs f = 0.10. CONFIRMED by n:81's definitions.
25. §5.3: "at f = 0.20 (f = 0.10 beside)". CONFIRMED, verbatim at n:140.
26. §6.1: "within 2% of 25.49". CONFIRMED. n:81, n:111.
27. §6.2: "31 or 32 layers". CONFIRMED by arithmetic on n:81's "layer 32 of 64".
28. §6.2: "layers 32 and the final layer". CONFIRMED, verbatim at n:79.
29. §6.3: the contrast ("else the shadow"), LOSO replaced, 200 shuffles, 24 random directions. CONFIRMED. n:121.
30. §6.4: ".90"; "enters n §5 only where §0.6 says". CONFIRMED. n:121.
31. §7.2: §0.6's two conditions. CONFIRMED. n:32.
32. §7.4: causes "n §5 implies and does not list". CONFIRMED. n:134, :136, :138, :140, :142 list them as the addendum says.
33. §7.6: "n §5's four verbatim sentences", and the replaced phrase "the margin does not move beyond the leak ceiling". CONFIRMED. n:136, n:138 (verbatim).
34. §1's title "§8 step 6" and §8.3(5)'s "n §8 steps 7–15". CONFIRMED. n:159.

**B. 645bd3f's block (`results/raw/2026-11-16_n-build_code-to-design_STOP.md`)**
35. Path, commit, "n-build session", this date. CONFIRMED. `git show --name-status 645bd3f`; block :3.
36. "transformers 5.15.0" on the box. CONFIRMED. Block :44; diag :1.
37. "tokenizes BK's sessions to 1,225–1,233 tokens against their 1,273". The numbers are CONFIRMED; the scope is IMPRECISE (minor).
    - Block :26–27: "Their lengths are 1,233, 1,232, 1,230, 1,231 and 1,232, against BK's `seq_len` of 1,273".
    - Block :56: "All four give 1,233 (session 0), 1,231 (62) and 1,225 (113), against 1,273".
    - Block :70–71: "The seven sessions printed fall short by 40 to 48".
    - So the range covers seven sessions, not "BK's sessions". The 0 of 160 is `ids_ok`, not a count of lengths.
38. G-DATA: `seq_len` 160/160, `ids_sha` 158/160, plus two re-splits. CONFIRMED. Block :48–49; G-DATA raw :92, :109–115.
39. Python 3.12.9, transformers 5.5.0, tokenizers 0.22.2, "the jlens venv". CONFIRMED. Block :44–46; G-DATA raw :11.
40. `olmo2_instruct` and the three sha256s `73fd5254…ecca` / `fff5b944…3fc7` / `78afb564…e2f2`. CONFIRMED.
    - Manifest :170 opens the entry. :251–254 is `special_tokens_map.json`, :255–258 `tokenizer.json`, :259–262 `tokenizer_config.json`. Abbreviated by `cut`.
    - Also block :39–43; G-DATA raw :70–72; diag :2–4.
41. §1.2 (i)–(iii) contents: 160 sessions with the re-splits, 320 told/sham sequences, the 12 labels. CONFIRMED. Block :100–104.
42. Note G-2, "a span after the first starts at the previous passage's end". CONFIRMED. Block :144–146; G-DATA raw :216–222 and :126.
43. "BK's `prereg.token_identity` form, as G-DATA (iv) quotes it". CONFIRMED. Block :128–130; G-DATA raw :106–107, inside (iv) which starts at :62. BK's analysis.json has the field: "every replay consumes ONE id list: the generation's emitted ids plus an identically appended choice turn".
44. The two routes for the small files. CONFIRMED. Block :112–116.
45. §8.2(2), the declined alternative. CONFIRMED. Block :95–99.

**C. 718c48e's block (`…_n-schema_code-to-design_questions.md`)**
46. Path, commit, the n-build session's five questions. CONFIRMED. Block :1, :4, :35–41.
47. The hook leaves the read position's residual at the injection layer equal to the shadow's, so the gate cannot reach its bar. CONFIRMED. Block :184–188 and :194–197 ("at most 0.75 … cannot reach its .90 bar").
48. The two secondaries, Q1 and Q2. CONFIRMED. Block :37–38.
49. "Zone" is shared by the 12 labels. CONFIRMED. Block :53 "Every one of BK's 12 labels is "Zone" plus a letter and a digit". The skeletons hold 12 distinct cues, all "Zone X#".
50. The restricted read's form. CONFIRMED. Block :59–63.
51. Q4's candidates, d = 0, "the shadows' values". CONFIRMED. Block :153–157, :162–163.
52. The merge rule and its reach. CONFIRMED. Block :115–120.
53. "About 150 MB per layer over 7,360 reads". CONFIRMED. Block :202–203.
54. Index 31 vs 32 settled by G-VEC's R check. CONFIRMED. Block :205–210.
55. §8.2(3), the declined alternative: index + 1 and the last layer. CONFIRMED. Block :200–201.
56. "the 1,280 generations" (only in §8.4). CONFIRMED that it resolves. Block :98 (160 + 160 + 960).
57. "k's bands L49–L63 for L48" (only in §8.4). CONFIRMED that it resolves. Block :192, :202; PROPOSAL-k :211 (L48), :224, :248–249 (L49–L63), :243 (L51–L61), :263 (L51–L62).

**D. 8e3bf91's block (`…_n-ganl_code-to-design_prebuild.md`)**
58. Path, commit, the n-analyzer session's nine. CONFIRMED. Block :1, :3, :9.
59. "as BK's pre-registration states the construction (Δm(0) ≡ 0)". CONFIRMED. Block :14; BK prereg.json "d is identically zero at dose 0 by construction."
60. N1-P at d_eq and d_20 (+320 reads, positive only). CONFIRMED. Block :21.
61. The cap case and the ratio 2·d_eq. CONFIRMED. Block :51–56.
62. The base causes. CONFIRMED. Block :44–47.
63. N2's slope and its floor points. CONFIRMED. Block :72.
64. The cell sentence of §7.2. CONFIRMED.
    - After the ruled substitution it is byte-identical to A.6 at :108; compared in the shell.
    - A.5 (:107) and A.6 both carry the replaced phrase.
65. The A.2 and A.7 NULL forms end "— [label]". CONFIRMED. Block :104, :109.
66. 1,921, 385, 256 (only in §8.4). CONFIRMED that they resolve. Block :35, :27; n:115.
67. n:122, n:126, n:134–n:142 (only in §8.4). CONFIRMED that they resolve to G-LEAK-n, §4 Primary, and §5's unit, N1, dose, N2 and N4.
68. The quoted "read at d = {point}, the point it merges into under §2.3". CONFIRMED, verbatim at `scripts/n_analyze.py`:2254 (VALUE_MERGED). This file is not in §8.4's list.

**E. 14e65d8's entry (RESULTS.md)**
69. `fit_lr` at seed 7, 300 iterations, rate 0.1, l2 0.01. CONFIRMED. RESULTS.md:367; `probe.py`:19 `7, 300, 0.1, 1e-2`; `schema.py`:1004.
70. The CV form. CONFIRMED. RESULTS.md:369–370: "loso" only, and a k-fold "enters with its fold seed in its own schema commit". This matches §6.3 and §8.3's `kfold10`.
71. The axes and the contrast. CONFIRMED. RESULTS.md:374–377.
72. "above the largest of the comparator's 24 band medians". CONFIRMED. RESULTS.md:383–385 (Code's reading), accepted at build raw :50.

**F. The seat's raws (B = build answers, G = ganl answers)**
73. Both exist, untracked, dated "PI date 2026-11-16 (second sitting)". CONFIRMED.
74. Ledger (77)–(79). CONFIRMED. B:54–56.
75. §1.1: the rule, and the box tokenizes nothing. CONFIRMED. B:7–8, :16, :27.
76. §1.2 (i), (ii), (iv), (v), MANIFEST.json and the render's raw. CONFIRMED. B:16–21. The quoted join is byte-identical to B:18.
77. §1.2 (iii). IMPRECISE (substantive, edge case only).
    - B:19 ends: "the session's ids asserted a prefix; a candidate whose sequence does not keep that prefix is reported and dropped".
    - The addendum stops at "the session's ids asserted a prefix of the full sequence". It gives no disposition on failure.
78. §1.3. CONFIRMED. B:25.
79. §1.4. CONFIRMED. B:27.
80. §1.5. CONFIRMED. B:23.
81. §2. CONFIRMED. B:37.
82. §3. CONFIRMED. B:31.
83. §4. CONFIRMED. B:33.
84. §5.1. CONFIRMED. B:35, B:48.
85. §5.2, including "about 10,800". CONFIRMED. G:25.
86. §5.3. CONFIRMED. G:35.
87. §6.1–§6.4, including 4.7–4.8 GB and the PASS rule. CONFIRMED. B:40–43.
88. §7.1. CONFIRMED. G:23.
89. §7.2. CONFIRMED. G:27.
90. §7.3. CONFIRMED. G:39; the clause is verbatim.
91. §7.4. CONFIRMED. G:33.
92. §7.5. CONFIRMED. G:44.
93. §7.6's first bullet (verbatim) and "the rest … as the n-analyzer raw adopts them". CONFIRMED. G:37–38.
94. §7.6: "N1's NOT-REPLICATED and N2's NULL end with answered or concluded, not answered". IMPRECISE (minor).
    - G:40 says "A.2's and A.7's "[label]" is answered or concluded, not answered".
    - A.7's SPECIFIC form also ends "— [label]" (8e3bf91:109).
    - The addendum follows G:27's narrower sentence. Its §7.2 ("wherever a null is labelled") covers SPECIFIC anyway.
95. "at f = [f]". CONFIRMED. G:41.
96. §8.3(3)–(5). CONFIRMED. B:60–64; G:56–59.

**G. CLAUDE.md**
97. "(rules 9 and 11)". CONFIRMED. CLAUDE.md:307–308 ("committed before data") and :311–312; the same form as n:4.
98. "(rule 27's spirit: it is a gate's input)". CONFIRMED as a citation. CLAUDE.md:354–359 reads "the repo, not any machine, is the record". The "spirit" qualifier is accurate: the letter is not met, since the captures are never committed.
99. Rules 5(b), 5(f), 23, 28(a) (only in §8.4). CONFIRMED that they resolve: :267–269, :280–301, :344–346, :364–374. The body reaches them only through n §0.6, G-READ-n, n §4's counters and the secondaries.

**H. Not checkable**
100. "written before any n stage has produced a read". NOT CHECKABLE: it is a state claim for the time of commit. It is consistent with 645bd3f:9 ("No checkpoint's weights were loaded"), 645bd3f:84 (the BACKEND reads still waiting) and B:79 ("`data/n` holds only `bk`").
101. Future acts: the render, the routing and the schema commit. NOT CHECKABLE.

**TOTALS** (101 graded items)
- CONFIRMED: 93
- IMPRECISE: 6 (1 substantive, 5 minor)
- FAIL: 0
- NOT CHECKABLE: 2

**IMPRECISE ITEMS, WITH FIXES**
- **#77 (substantive, edge case).** If a label candidate's sequence does not keep the session prefix, a reader of the addendum alone would STOP; the seat's raw drops the candidate and continues.
  - Fix: append "; a candidate whose sequence does not keep that prefix is reported and dropped" to §1.2 (iii).
  - Then make §2's "the four counts" read "the counts".
- **#2 (minor).** Fix: "the file its `PROPOSAL-n v0.2 COMMITTED` entry (RESULTS.md, 2026-11-06) names", or note that the dashed name is v0.2's §8 form.
- **#16 (minor).** Fix: "n §4's blinding is read here as concerning margins under steering before VERDICTS". Optionally add it to §8.1's §4 line.
- **#22 (minor).** Fix: "(C12 refits each arm's floor on that arm's own dose points)".
- **#37 (minor).** Fix: "tokenizes the seven sessions printed to 1,225–1,233 tokens against BK's 1,273 (ids 0 of 160)".
- **#94 (minor).** Fix: "A.2's and A.7's [label] (N1's NOT-REPLICATED; N2's SPECIFIC and NULL) is answered or concluded, not answered, by 7.2".

**OBSERVATIONS (no verdict)**
1. **§8.4 and the body don't match in either direction.**
   - §8.4 lists referents the body never quotes: 1,280; k's bands; 1,921/385/256; the n:N anchors; rules 5(b), 5(f), 23, 28(a).
   - The body cites sources §8.4 omits: n §0.10 (C12), §1, §3's G-VEC, G-CAL-n and LOCK-n v0.1, §6, §7.4 and §9; G-DATA's raw; `scripts/n_analyze.py` (VALUE_MERGED); `probe.py` through 14e65d8; PROPOSAL-k. All of these resolved here.
2. The header defines `k §N` and `m:N`, but neither occurs in the body.
3. The header says "one secondary". §0.3, §3 and §4 touch two: (a) is amended and (b) is struck.
4. **§6.2's storage figure predates §5.2.** It sizes on 7,360 reads, but §5.2 adds up to 320 N1-P reads (≤ 7,680). At Code's per-read rate that is about 156 MB per layer, so about 4.85–5.0 GB. Also, "On every forward" (n §2.2's words) would add the re-computation forwards if read literally.
5. "about 10,800": n:95's ≈10,500 + 320 = 10,820. n:95's 10% re-computation sample on the new N1-P points adds about 32 more, so ≈10,850.
6. **The §2 tolerance is tighter than it looks.**
   - BK's `reduced.json` records the 80 d = 0 log-probs of the 40 OLMo floor sessions at 13–15 decimal places (counted by awk; values not printed).
   - So "half a unit in the last decimal" is about 5e-14. In practice the tolerance is the backend's identity bound, which is a within-backend figure, applied here across two implementations.
   - If kernel-level differences exist, all four candidates score 0/40 and the check goes to the seat. 718c48e's "−9.69/−11.47" are display roundings.
7. **§8.1 says §6 is unchanged, but the routed rulings touch it.**
   - B:50 accepts readings that operate on n §6: a fired monitor ends the invocation for every arm, where n:148 says "the arm's launches"; and the pause precedence is fixed.
   - B:61 puts "the pause precedence of §3; the lock's cap clause" in the follow-up schema commit, but §8.3(3) does not list them. They reach Code only via §8.2(4).
8. The header says "any bar" is unchanged, yet §7.3 adds a sign condition to DETECTABLE and PARTIAL and §5.3 moves N2's decision f. §8.1 lists both under §5, so the header holds only if "bar" means thresholds.
9. §1.1 says "Every input id n uses is rendered there once", but §1.4 feeds emitted ids into the arrival forward. The bold sentence (the box never produces an input id) is the precise one.
10. §1.5 does not say where `tokenizer.json` comes from. B:23 says "`tokenizer.json` is the cache's, at its pinned sha256".
11. §2's candidate list reads ambiguously ("each followed by the end-of-turn token"); B:37 adds "(four)".
12. G-READ-n's "else the shadow" contrast is carried over unchanged from n:121. It tests the state's presence, not its sign, while rule 5(f)(ii) (CLAUDE.md:290–293) says "discriminating the injected sign".
13. **A misattribution in the seat's raw, not the addendum.** B:18 says "the `14e65d8` entry left it to the lock". The words are in 5a97527's entry (RESULTS.md:1036–1037, "the exact join is the lock's") and in `schema.py`:96–97. 14e65d8's diff has no "join".
14. §7.6's "the n-analyzer raw" means the seat's ganl answers raw (B:64 uses the same name), but it can be read as 8e3bf91's Code raw.

## 2. Code's grading and dispositions

**No FAIL.** The addendum is committed as the seat placed it (`e979f8f2…5e03`); nothing in it is edited, and no
item below is applied to its text.

**#77, graded substantive by the checker: resolved by the seat's own ruling of the same routing, so no STOP under
§8.3 (1).** The addendum's §1.2 (iii) gives no disposition for a label candidate whose sequence does not keep the
session's prefix. The seat's n-build answers raw, §1.2 (iii), gives it: "a candidate whose sequence does not keep
that prefix is reported and dropped". That raw is committed at `52b2c97`. The PI's routing takes that raw's STOP
rulings (its §1, where §1.2 (iii) sits) "as ruled" in item 7. The addendum's header names the seat's two answer raws
as the place of its reasoning, and its §8.4 lists "The seat's raws of this date, by path" among the referents, so the
ruling lies inside the referent set. The n-build session's draft renderer already reports and drops such a candidate
(its self-test of 2026-11-16). This is Code's grading; the seat may regrade it, and a regrading would come as a
ruling.

**#2, #16, #22, #37 and #94 (minor):** recorded for the seat, unapplied.

**The fourteen observations:** recorded for the seat. Four bear on what runs next:
- **Observation 6:** §2's tolerance. BK's d = 0 values carry 13–15 decimals, so the tolerance is in practice the
  backend's identity bound, applied across two implementations. If all four candidates score 0 of 40, the check goes
  to the seat with the four counts, as §2 has it.
- **Observation 7:** the pause precedence and the cap clause, fixed by the n-build raw's §3 and in its §5 item 2's
  schema commit, are not in the addendum's §8.3 (3). They reach Code through §8.2 (4), the rest of the routing. The
  pause precedence, and the seat's accepted reading that a fired monitor ends the invocation for every arm (n:148
  says "the arm's launches"), touch n §6, which §8.1 lists as unchanged.
- **Observation 12:** G-READ-n's contrast at every point but valence +1 is the shadow, which tests the state's
  presence, not its sign; rule 5(f)(ii) asks for a probe "discriminating the injected sign". Carried unchanged from
  n:121.
- **Observation 13:** the seat's n-build raw, §1.2 (ii), says "the `14e65d8` entry left it to the lock". The words
  that left the N4 join to the lock, "the exact join is the lock's", are in `5a97527`'s entry.

**The checker's reads under `data/n/bk`** were those its brief allowed for a referent that needs BK's own text: the
cue labels and record counts in the skeleton files, `analysis.json`'s `token_identity`, `prereg.json`'s d(0) sentence,
and a count of the decimal places of 80 `reduced.json` values, with no value printed. It read nothing under
`data/mf3`, `ckpt` or `reports`, and ran no interpreter beyond awk and sed as text tools, which its brief allowed.

**Anchors.** §1's RESULTS.md line numbers index `bedc198`'s RESULTS.md: the checker ran before `52b2c97`, which is why
its item 73 calls the seat's raws untracked. Its B:N and G:N anchors index the seat's raws, whose committed bytes equal
the placed files.

**A values-check** of this section, of the `ADDENDUM-n1 v0.1 — COMMITTED` entry and of the PI-routing raw is recorded
in [`2026-11-16_addendum-n1_valuescheck.md`](2026-11-16_addendum-n1_valuescheck.md).
