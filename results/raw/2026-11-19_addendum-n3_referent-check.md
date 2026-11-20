# ADDENDUM-n3 v0.1: the referent check of its §8.4, and Code's grading (PI date 2026-11-19)

Code's raw for `ADDENDUM-n3 v0.1 — COMMITTED`. The addendum's §8.3 (1) asks for "referent check of 8.4; an
unresolved substantive item → STOP". One fresh blind checker, a subagent of the coordinating session, checked every
statement of the addendum that quotes, cites, paraphrases or gives a number from a referent §8.4 lists, and the other
sources the addendum cites, every referent read at `bc50244`. Its brief (`3195496f…b05a`, 52 lines, given as a file with
its sha256 to verify):
- quoted the list of record v2's items 1–5 verbatim;
- carried the briefs' two lines, "A git command in a check takes item 3's pathspec" and "A glob is expanded and read
  before it is looped over";
- required the `data/mf3` exclusion and barred anything under `data/`;
- allowed no interpreter but `shasum`.

Its report is reproduced whole in §1, extracted verbatim from the subagent's hand-back by `jq` (238 lines, sha256
`30060f60…15c3`). It held no local path. Code's grading and dispositions follow in §2.

## 1. The checker's report, whole

```text
REFERENT CHECK — ADDENDUM-n3 v0.1, §8.4 and the other sources it cites (blind; I check, I do not rule or rewrite)

HEADER
- Brief: shasum 3195496fd77ca9d5809afebf546b9ac34c5936ae9794abaa0e5865329a40b05a, 52 lines. Matches.
- Document: ADDENDUM-n3-capture-convention-reward-gate-and-interval-v0_1.md at the root. Untracked (`??`). sha256 7f4a7a75b61002b58e62a400e99f4de2abc8ec0646329fdf624ce31540be9313, 20,327 bytes, 81 lines. Matches the brief.
- HEAD: bc5024490f5d23caf05b0e576c5e3784ce4b435b (bc50244).
- Reading method: for every file below, `git rev-parse bc50244:<path>` equals `git hash-object <path>`, so I read the working files. That covers the 13 named referents, scripts/n_sessions.py, both review raws, and results/raw/2026-11-19_n-gvec-v1_gvec.json.

LABELS (all at bc50244)
- n = PROPOSAL-n-bk-reconciliation-v0_2.md. sha256 30a3d0f55a6681e01245f75490d1f7fdf032b4a1f2c6e59684d6a17584b104f4, which matches the document's 30a3d0f5…04f4. Only commit: 5916097.
- A-n1 = ADDENDUM-n1…v0_1.md (e979f8f2…5e03). Only commit: a61f13d, "ADDENDUM-n1 v0.1 -- COMMITTED". Matches.
- A-n2 = ADDENDUM-n2…v0_1.md (41f76c49…bb3f). Only commit: 7a54eb9, "ADDENDUM-n2 v0.1 -- COMMITTED". Matches.
- C = CLAUDE.md:
  - rule 5 :267–301; 5(d) :272–273; 5(f) :280–301
  - 5(f)(ii) :289–296; (iii) :297–298; (iv) :298–300
  - rules 9 :307, 11 :311, 13 :315, 25 :348
- R = RESULTS.md, entries found by subject:
  - bc50244 :24–104; 616e940 :105–180; ab72d0f :181–263; d85fc34 :264–326
  - 035947e :394–534; 355e3a2 :535–687
  - n v0.2 COMMITTED :14133ff (the Clock at :14145, :14180)
- S1 = …_n-starred-twelve_design-to-code_answers.md, placed at a33252a.
- S2 = …_n-gvec-stop-lock-opens_design-to-code_answers.md, placed at f4b3e73; sha256 887b7646…dc87.
- NB16 = results/raw/2026-11-16_n-build_design-to-code_answers.md (:41), placed at 52b2c97.
- PR2 = results/raw/2026-11-19_second-sitting_pi-routing.md, placed at ab72d0f.
- Two sources beyond the brief's list (see DEPARTURES):
  - RV2 = results/raw/2026-11-19_n-gcal-delta2_review.md (bc50244's review)
  - RV1 = results/raw/2026-11-19_n-gcal-delta_review.md (035947e's review)
- Code: valence_core/n/{schema,directions,gcal,gvec}.py and scripts/n_sessions.py (the driver).
- The moved STOP record, results/raw/2026-11-19_n-gvec-v1_gvec.json: sha256 3331da71…ee95. Hashed, not opened. Its path's only commit is 616e940.

LISTINGS (A3:N = the document's line)

Preamble
1. A3:1–4 — S2:9, :71; PR2:22. The addendum S2 owed must carry: the capture convention, the arrival's form, the 5(d) gate and N2's decision point, the 5(f)(iii) declaration and departure, the four dated notes, and O2's early PAUSE. Each is present (§1, §2, §3, §4, §5, §7). CONFIRMED.
2. A3:4 — n's sha256 30a3d0f5…04f4, tracked at root — shasum. CONFIRMED.
3. A3:4 — A-n1 v0.1 at a61f13d; A-n2 v0.1 at 7a54eb9 — git log on each path; A-n2:4. CONFIRMED.
4. A3:4 — S1 by path at a33252a; S2 at f4b3e73 — git log on each path. CONFIRMED.
5. A3:4 — "what Code built on them (616e940, bc50244)" — R:105–109, R:24–30. CONFIRMED.
6. A3:4 — "three items Code's review of bc50244 returned" — R:64–69 ("its O5, O6 and B2's second clause, for ADDENDUM-n3"); RV2:69–76. CONFIRMED.
7. A3:4 — "not the Clock (D_n 2026-12-15)" — n:152; R:14145, :14180 (routed at n's commit); A-n1:4; A-n2:4. CONFIRMED.
8. A3:4 — "G-VEC's re-run of record under §1 has run on the box as the PI reports it" — no entry at bc50244 records a re-run (R:104 and R:177–178 still name it as next). NOT CHECKABLE: the PI's report is in no permitted source.
9. A3:4 — "(rules 9 and 11)" — C:307, :311; the same form appears at n:4, A-n1:4 and S2:51. CONFIRMED.

§0
10. A3:10 — 355e3a2 STOPPED at n §2.3's R check: R 44.04 at index 31 and 45.11 at 32, against 25.49 — R:543–545 (44.04249774012646; 45.107750142385356); n:81. CONFIRMED (rounded).
11. A3:10 — "every token of each passage counted" — S1:16 (G1 as built); R:537. CONFIRMED.
12. A3:10 — the alternative pre-declared at a33252a §1.1 — S1:16 pre-declares it; S2:16 rules it. CONFIRMED.
13. A3:10 — a bare forward's first position carries the attention sink — S2:16. CONFIRMED.
14. A3:10 — BK §3.1's mean "over its T_i tokens", read as the passage's tokens and not the sink position — S2:16 holds the same quotation and reading. f4b3e73's directions.py:11 held BK's full sentence ("…the mean activation over its T_i tokens"). BK's PDF was not read. CONFIRMED (quotation byte for byte). For the §8.4 anchor, see 122.
15. A3:12 — d85fc34 raised two rule-5(f) questions the BUILD had flagged — R:273–274. CONFIRMED.
16. A3:12 — 5(f)(iv) quoted, "below dose 0.20 … separately passed" — C:299–300. CONFIRMED (byte check).
17. A3:12 — 5(f)(iii) quoted, "declared and held fixed within a cell"; the interval varies across a cell's sessions — C:298; S2:45; schema.py:64–67. CONFIRMED.
18. A3:12 — N2-E reads at exactly f = 0.20 — n:90; schema.py:301. CONFIRMED.
19. A3:12 — "v0.2 had paraphrased the first bound (ledger (85))" — S2:79. CONFIRMED.
20. A3:14 — G-CAL-n's launch files wait on this commit — PR2:14; S2:51; R:104. CONFIRMED.

§1
21. A3:16 — heading: amends n §0.8's reading of BK §3.1; A-n1 §6.1's R check stands — n:36; A-n1:52. CONFIRMED.
22. A3:18 — each passage forwarded alone from committed ids, no special token, no template — S2:17; S1:16; directions.py:10. CONFIRMED.
23. A3:18 — position 0 out of the mean and R (squared norms and count); CAPTURE_FROM = 1 at 616e940 — S2:18; directions.py:10–11, :50; R:111–112. CONFIRMED.
24. A3:18 — the PCA is centred; v under an uncentred U is recorded beside, descriptive — S2:19; gvec.py:35–40. CONFIRMED.
25. A3:18 — R is the pooled RMS over the neutral tokens at positions 1..n — S2:20; directions.py:16. CONFIRMED.
26. A3:18 — A3's span starts after position 0 (gvec.a3_capture) — gvec.py:304–306 refuses unless 0 < span_start < S; S2:21. CONFIRMED.
27. A3:18 — "so R_ℓ, N2's three directions, the fit-only family, the guard profile and the random directions never counted it" — S2:21 lists these, plus the final-position rows and the cosines, as "untouched". "Never counted it" fits the span-built quantities. The 24 random directions are drawn, not captured, so the span reason does not reach them. The document also drops the final-position rows and the cosines. IMPRECISE (minor).
   Fix: "…so R_ℓ, N2's three directions, the fit-only family and the guard profile never counted it; the final-position rows, the 24 random directions and the cosines are untouched (f4b3e73 §1.2)."
28. A3:18 — nothing is re-rendered; the ids of record stand (A-n1 §1) — S2:17; A-n1:18–28; R:113. CONFIRMED.
29. A3:20 — "within 2% of 25.49 at an index, else STOP (n §2.3)" — n:81; A-n1:52. CONFIRMED.
30. A3:20 — "both within 2% → the nearer in R, an exact tie to 32 (A-n1 §6.1)" — A-n1:52 says only "the nearer is the site". "In R" and the tie to 32 are G2's reading (gvec.py:41–42), ruled standing at S1:22 (§1.4). S2:22 cites "ADDENDUM-n1 §6.1; G2; G9". IMPRECISE (minor).
   Fix: "(A-n1 §6.1 as G2 reads it, a33252a §1.4)."
31. A3:20 — R at both indices goes in the lock — A-n1:52; S1:22. CONFIRMED.
32. A3:20 — the record is schema n-gvec-v2 and names the convention; it carries the token counts and neutral_tokens_in_R — gvec.py:105, :445, :450; R:120–121. CONFIRMED.
33. A3:20 — the diagnostic block over the 96 neutral passages at both indices: R_all, rms_by_position (0–4, 5..n) with counts, max_norm, R_mean_of_passage_rms; none decides — S2:24–29; R:115–118, :138; gvec.py:214–248. CONFIRMED.
34. A3:20 — a non-finite figure is null and listed; R still raises (616e940's readings) — R:141–142; gvec.py:83–84. CONFIRMED.
35. A3:20 — the STOP record moved byte for byte to results/raw/…_n-gvec-v1_gvec.json — R:131–135, :679–686. Its sha256 3331da71…ee95 equals R:547's digest for the old path. CONFIRMED.
36. A3:20 — LOCK-n v0.1 records both runs' R — S2:33, :71. CONFIRMED.
37. A3:22 — a second STOP at both indices goes to the PI with the diagnostic block; the seat rules no third convention; its stated default is f4b3e73 §1.5's — S2:33; R:122–123. CONFIRMED (see observation 6).
38. A3:22 — "The alternative not taken, a leading special token left out of the mean, is recorded there too" — the alternative is at S2:22 (§1.2), "left out of the mean and R". §1.5 (S2:33), which "there" follows, does not record it. IMPRECISE (minor).
   Fix: "…is recorded at f4b3e73 §1.2 (out of the mean and R)."

§2
39. A3:24 — heading: amends the arrival clause as a33252a §1.11 read it; reverses O6 — n:113; S1:36; S2:8. CONFIRMED.
40. A3:26 — the arrival is the emitted ids alone, unsteered, captured at the site; the mean over positions 1..n on the unit valence row — S2:31; gcal.py:60–64, :335–351; R:32–33. CONFIRMED.
41. A3:26 — ARRIVAL_FROM is one constant with CAPTURE_FROM (bc50244) — gcal.py:182; R:33. CONFIRMED.
42. A3:26 — arrival_all is recorded beside per turn, descriptive — S2:31; gcal.py:347. CONFIRMED.
43. A3:26 — O6 quoted, "because v was built from passage means that count every token" — S1:36; S2:31. CONFIRMED (byte check).
44. A3:26 — Welch's t of the 48 against the baseline's 48, |t| ≥ 2 with the pole's sign (GC12) — S1:36; gcal.py:64–65. CONFIRMED (GC12's own words; after §2.2 the t runs over the scored turns, gcal.py:378).
45. A3:28 — a one-id turn has no score and is left out of the t; one_id is counted beside empty, as departure (2) treats the end-of-turn-first turn — S2:31; gcal.py:100–103, :348, :363–365; R:34–36. CONFIRMED.
46. A3:28 — a one-id turn's arrival_all is the projection at position 0, the sink's — RV2:252; R:66–67; gcal.py:115–116. CONFIRMED.
47. A3:28 — the seat's read reports any pooled arrival_all summary with one-id turns left out and their count stated (the review's O6) — RV2:252 ("split out or drop n_tok = 1"). CONFIRMED. The document takes the "drop" option; the ruling is new here (see 111).
48. A3:30 — fewer than two scored turns leaves Welch's t undefined, a fail at +ρ (departure (1)) — gcal.py:100–101, :380; RV2:250. CONFIRMED.
49. A3:30 — so the early STOP precedes the early PAUSE (the review's O5; O1) — RV2:250; S2:58; PR2:14 ("STOP first"); gcal.py:495–504. CONFIRMED.

§3
50. A3:32 — heading: amends n §2.3 "never above 0.20", n §0.10 B3 and n §5 N2; extends A-n1 §5.3 — n:81, :48, :140; A-n1:48. CONFIRMED.
51. A3:34 — 5(d) quoted "verbatim" — C:272–273 (bold dropped; the ≥ character is the same). CONFIRMED.
52. A3:34 — 5(f)(iv) quoted "verbatim" — C:298–300. CONFIRMED.
53. A3:34 — N2-E reads at f = 0.10 and f = 0.20 (n §2.3; ARM_CELLS) — n:81, :90; schema.py:301. CONFIRMED.
54. A3:34 — n B3 quoted, "G-LEAK-n plus G-CAL-n's coherence hurdle" — n:48. CONFIRMED.
55. A3:36 — f = 0.20's norm, 0.20·R_ℓ, is +d_20's by the map d_20 = min(1, 2·d_eq) — n:81. The arithmetic holds: 2·d_eq·ρ·R = 0.20·R_ℓ when uncapped. S2:47. CONFIRMED.
56. A3:36 — N1-R's 24 directions and N1-P read at that point (n §2.4; A-n1 §5.2) — n:88; A-n1:46 (n:89 alone has N1-P at ±1 only); schema.py:299–300. CONFIRMED.
57. A3:36 — L(d_20) and P(d_20), computed with VERDICTS (n §3 G-LEAK-n) — n:122. CONFIRMED.
58. A3:36 — certified on arms where preference is impossible by construction, never on the reward arm (5(f)(ii)) — C:295–296. CONFIRMED.
59. A3:36 — span_reward's effect is certified or not as n §5's N2 reads it — n:140. CONFIRMED.
60. A3:36 — where the cap binds, the norm-matched point is d = 1 (A-n1 §5.3) — A-n1:48; S2:48. CONFIRMED.
61. A3:38 — the batch: 48 prompts and seeds, TEMP 0.7, cap 80, whole turn from position 0 (a33252a §1.9), span_reward's unit row at 0.20·R_ℓ, after +ρ/2 and before −ρ, coherence only against 36 of 48, no arrival — S2:49; S1:32, :34; gcal.py:75–83, :165–172. CONFIRMED.
62. A3:38 — the campaign's injection for N2-E at f0.20, sign +1, the row checked against of_record before the load (bc50244) — R:40–43, :61; gcal.py:419–432; schema.py:290. CONFIRMED.
63. A3:38 — GC11 for the coherence heuristic — S1:34 (§1.10). CONFIRMED.
64. A3:38 — a fail is neither a STOP nor a PAUSE — S2:49; PR2:14; gcal.py:81–82, :530–533. CONFIRMED.
65. A3:38 — the record carries the count, pass, stops, direction, dose label, f, alpha and sha16; the turns file holds its 48 turns; the seat reads them (GC1, rule 25); the exposure line stays −ρ's — R:44–45, :59–60; gcal.py:526–528; S1:61. CONFIRMED.
66. A3:38 — the printed lock-form line, "reward axis 5(d) gate, coherence: k of 48, PASS" or FAIL — scripts/n_sessions.py:2884–2885, after the exposure line at :2880; R:45–46. CONFIRMED.
67. A3:38 — no gate turn in the smoke; the HF self-test runs the gate's steering check; the run of record prints its check before the batch — R:61–62; gcal.py:83, :119–121, :468–471; RV2:69–71. CONFIRMED.
68. A3:38 — the review's B2 second clause (a steering check with no turn in the smoke) — RV2:71, :193; R:68–69. CONFIRMED.
69. A3:40 — n §5 quoted, "N2 (state), at f = 0.20 (f = 0.10 beside)" — n:140. CONFIRMED.
70. A3:40 — the decision point: f = 0.20 iff the gate's coherence PASSED and 2·d_eq ≤ 1; otherwise f = 0.10 against N1-V at d_eq, with f = 0.20 beside at d_20 (d = 1 if capped, ratio printed) — S2:50; PR2:19; A-n1:48. CONFIRMED.
71. A3:40 — outcomes as n §5 texts them; the §7.3 report names the deciding point; the N2-S and N2-C guards decide nothing; no read added — n:140, :152; S2:50. CONFIRMED (see observation 3).
72. A3:42 — the lock pins the gate's two components and the coherence result, k of 48 and PASS or FAIL — S2:50. CONFIRMED.
73. A3:42 — "from a gcal.json whose status is PASS (O8)" — S1:63's O8 covers the dose map only; the document extends it to the gate's figures. IMPRECISE (minor).
   Fix: "(O8's rule, extended here to the gate's figures)."
74. A3:42 — n-analyzer reads the lock's line, not gcal.json, in its delta with F5, R13, the tile's range and the pin move; the battery reaches both branches — S2:50; PR2:19; R:455–457 (the schema pin). CONFIRMED.
75. A3:42 — one n §7 sentence set per tuple (G-ANL-n) — n:115. CONFIRMED.
76. A3:42 — G-CAL-n's planning figure grows by one batch in five; Code's B3, the time at 240 turns — n:101; S2:49 ("a fifth"); RV2:71–72, :195–198 (240 for 192, about +25%); R:104. CONFIRMED.
77. A3:44 — 5(d)'s bound came from e2d: the reward-axis dose buys degradation — S2:52; n:10. CONFIRMED.
78. A3:44 with A3:77 (2) — the alternative and its "declined" branch. IMPRECISE (substantive).
   - S2:52's alternative is "…with G-LEAK-n alone as the gate and no batch". S2:89 and PR2:14 word it "strike the batch and declare the departure with G-LEAK-n alone".
   - §3.6 drops "no batch". §8.2 (2)'s declined branch keeps the batch: its result is "recorded and used by nothing".
   - The same branch says N2 "decides at f = 0.20 as n §5 texts it". That passes over A-n1 §5.3 (A-n1:48, committed), which decides at f = 0.10 when the cap binds.
   - So the decision on a decline differs from what S2 offered and the PI saw: 48 reward-axis turns at 0.20·R_ℓ generated or not, plus the cap condition. The adopted branch is unaffected.
   - Fix, either: "declined: the reward_f020 batch is struck, 5(f)(iv)'s departure is declared with G-LEAK-n alone, and N2 is decided as n §5 and A-n1 §5.3 text it"; or keep the batch and state that this departs from f4b3e73 §2.5's "no batch", with the reason.

§4
79. A3:46 — heading: as amended by a33252a §1.9, §1.12 (d), §5 O7 — S1:32, :38, :63. CONFIRMED.
80. A3:48 — the dose map from G-VEC's R and R_ℓ; 48 turns, BK's zone prompt, TEMP 0.7, cap 80; the rendering of record (A-n1 §1.2 (v)); STEER_FROM = 0 — gcal.py:85–87, :28–30, :144–145, :178; A-n1:22; S1:24–32. CONFIRMED.
81. A3:48 — the order +ρ, baseline, +ρ/2, reward_f020, −ρ; each batch scored as generated — gcal.py:41–46, :172. CONFIRMED.
82. A3:48 — the early read: a +ρ fail (t undefined among them) is a STOP, exit 2, with record, turns and dose map written; then a baseline under 36 of 48 is a PAUSE, exit 3, with early_pause; O2's reason — gcal.py:491–504; R:425–427; S1:38; S2:59. CONFIRMED.
83. A3:48 — otherwise STOP / PAUSE / PASS (n §3; GC14; O7) — gcal.py:390–397; n:113; S1:63. CONFIRMED.
84. A3:48 — schema n-gcal-v2 with early_stop, early_pause, the gate's figures, and constants for order, first steered position and arrival_from (bc50244's readings) — gcal.py:141, :572–584; R:53, :58–63. CONFIRMED.
85. A3:48 — a failed run keeps its turns (GC23); the seat reads every turn before v0.1 (GC1); the paired t beside Welch's (a33252a §1.11 O5); the smoke has no gate batch — S1:38, :61, :36; gcal.py:83. CONFIRMED.

§5
86. A3:52 — 5(f)(iii) quoted "verbatim", ending "…held fixed within a cell." — C:297–298 ends the clause with ";" ("…within a cell; (iv)"). The words match byte for byte; the closing character does not. IMPRECISE (minor).
   Fix: close the quotation at "cell" with the period outside, or quote the ";".
87. A3:52 — n §2.2 quoted, "recorded per session and fixed by the skeleton" — n:79. CONFIRMED.
88. A3:54 — the interval is fixed by skeleton and span set, the same at every dose point and on every S-span arm; N1-P's 39 tokens on all 160 (schema.py:64–66) — schema.py:64–66; S2:45. CONFIRMED.
89. A3:54 — the lock declares the 160 per-session values per span kind, pinned, with the distribution printed; each read records its own — S2:45; PR2:15. CONFIRMED.
90. A3:56 — what the rule protects holds by construction; the letter holds in N1-P's cells only; the departure is confined to the S-span arms; secondary (d) is its check; one interval per cell was not taken — S2:45; n:128. CONFIRMED.
91. A3:56 — "The PI confirmed it … (ab72d0f's entry, item 3)" — the PI's word at PR2:15 is "as ruled" in the slot "confirmed: ___"; R:209–210 reads it as the confirmation. CONFIRMED.

§6
92. A3:60 — OPEN 1: the hash lists' form (capture_sha256) and where they are recorded; copied before the pod stops; committed at step 14 — S2:39; schema.py:438; n:159. CONFIRMED.
93. A3:60 — OPEN 2: the cap's split (loads beside and outside; G-READ-n's fits per A-n1 §6.3, the sum stated; a crashed load is a declared gap; A100 planning values revised at v1.0) — S2:41; A-n1:56. CONFIRMED.
94. A3:60 — OPEN 3: G-TIME-n's figures enter v1.0 (n §8 steps 10–13) — S2:43; n:159. CONFIRMED.
95. A3:62 — R-L1 and R-L2 stand; v1.0 writes its own lock: line — S2:54. CONFIRMED.
96. A3:62 — Route A's request was not made; Route B is of record (the PI) — PR2:22; R:226–227. CONFIRMED.
97. A3:64 — (i) rule 13's departure (n §0.7) reaches G-CAL-n's generations; A2's extension was confirmed — n:34; S1:30; PR2:23 ("[confirmed: confirmed]"); R:228–230. CONFIRMED.
98. A3:64 — (ii) the 5(f)(iii) departure confirmed the same day — PR2:15. CONFIRMED (as 91).
99. A3:64 — (iii) 5(f)(iv)'s "unless" clause — C:299. CONFIRMED.
100. A3:64 — the review's O5 of 035947e: G-CAL-n steers position 0 of every steered turn; the campaign only in sessions opening with S, and in N1-P — RV1:64–65, :184–186 and R:453–454 say "in the SU arms"; S2:60 says "in N1-P"; schema.py:310 shows N1-P is the only "SU" arm. CONFIRMED.
101. A3:64 — the hurdles' cap is 80; the PI named none from Appendix E — S1:24; PR2:23; R:229–230; gcal.py:145. CONFIRMED.

§7
102. A3:68 — n:81 quoted, "never above 0.20 (5(f)(iv); no 5(d) gate is needed for the reward axis)" — n:81. CONFIRMED (byte check).
103. A3:68 — n:48 quoted, "N2-E's reads capped at f = 0.20 (d_20), so no reward-axis read needs 5(d)'s gate" — n:48. CONFIRMED.
104. A3:68 — "the rule says "below dose 0.20""; ledger (85) — C:299; S2:79. CONFIRMED.
105. A3:69 — A-n1 §6.2 quoted, "the lock pins the per-cell hash lists"; NB16:41 has the same words; S2 reads them as "…their form and the place of their record" — A-n1:54; NB16:41 ("The lock pins the per-cell hash lists."); S2:39. CONFIRMED.
106. A3:70 — S1 §1.1 quoted, "every token in the passage mean and in R"; S1 §1.11 O6 quoted, "position 0 stays in the mean"; ledger (86) — S1:16, :36; S2:81. CONFIRMED.
107. A3:71 — PR2 item 2 quoted, "no +ρ/2 or −ρ turn"; reward_f020 is likewise not generated — PR2:14; gcal.py:491–504; R:199–200. CONFIRMED.

§8
108. A3:75 — the unchanged list: TAU, p0, C, alpha, the tile, the Clock and the others — n:77; A-n2:18, :24; S1:10, :51; R:14180. CONFIRMED.
109. A3:77 — decisions numbered (n-5) and (n-6), after (n-1)–(n-4) — A-n1:82; A-n2:46. CONFIRMED.
110. A3:77 (3) — "confirmed as the PI's word of 2026-11-19 stands" — PR2:15. CONFIRMED.
111. A3:77 (4) — "§1, §2, §4, §6 and §7 as the seat's rulings, already routed on 2026-11-19 and carried here." IMPRECISE (substantive).
   - PR2:13–23 routes S2's §1, §2 and §3 items. Several parts of §1, §2, §4 and §7 came after that routing and are first ruled in this document:
     - §1.2's "616e940's readings, accepted" (616e940 follows ab72d0f);
     - §2.2's rule for the seat's own read (RV2's O6) and §2.3's acceptance of RV2's O5 (RV2 was committed at bc50244);
     - §4's "bc50244's readings, accepted";
     - §7's fourth note.
   - A3:4 itself says the document "settles three items" of that review.
   - The rulings' content is unaffected, and (4) covers them either way. What is wrong is the routing block's account of which rulings the PI's word of 2026-11-19 covered.
   - Fix: "(4) §1, §2, §4, §6 and §7 as the seat's rulings: those routed on 2026-11-19, carried here; and new here, the acceptance of 616e940's and bc50244's readings (§1.2, §4), the review's O5 and O6 (§2.2–§2.3), and §7's note on the paste block's item 2."
112. A3:79 — §8.3 (3)–(5): B3's time; F5, R13, the tile's range and the pin move; the lock's draft items — R:104; PR2:19; S2:50, :71. CONFIRMED.

§8.4 anchors
113. A3:81 — "CLAUDE.md rule 5(d), 5(f)(i)–(iv) (:267–299)" — 5(f)(iv) ends "separately passed." at C:300, and rule 5 ends at :301. S2:3 has the same range. IMPRECISE (minor).
   Fix: ":267–300" (or ":267–301").
114. A3:81 — n's anchors n:36, :48, :79, :81, :88–89, :101, :113, :122, :128, :140, §7.3 (:152), :159 — each holds the named text. CONFIRMED.
115. A3:81 — A-n1 §1, §1.2 (v), §5.2, §5.3, §6.1, §6.2, §6.3 — A-n1:18, :22, :46, :48, :52, :54, :56. CONFIRMED.
116. A3:81 — S1's §1.1, §1.9, §1.11, §1.12 (d), §5; S2's §1.2–§1.5, §2.1–§2.6, §3; NB16:41 — all present as named. CONFIRMED.
117. A3:81 — 355e3a2's R figures 44.04249774012646 and 45.107750142385356 — R:543–544. CONFIRMED.
118. A3:81 — 616e940's CAPTURE_FROM = 1, n-gvec-v2, neutral_tokens_in_R and the move — R:111–112, :120–121, :131–132; directions.py:50; gvec.py:105, :445. CONFIRMED.
119. A3:81 — bc50244's ARRIVAL_FROM, one_id, early_pause, n-gcal-v2, the printed line, and the review's O5, O6, B2 — R:33–69; gcal.py:141, :182, :365, :576; driver :2884; RV2:69–76, :250–252. CONFIRMED.
120. A3:81 — ab72d0f's items 2, 3, 6 and 7 — R:193–198, :209–210, :226–227, :228–230; PR2:14–23. CONFIRMED.
121. A3:81 — schema.py:64–66 and ARM_CELLS — schema.py:64–66, :297–306. CONFIRMED.
122. A3:81 — "valence_core/n/directions.py:10–11 (BK §3.1's sentence)" — FAIL.
   - At bc50244, directions.py:10–11 holds the new convention's text.
   - BK §3.1's sentence stood at :11 up to f4b3e73. 616e940 removed it when it reworded the readings.
   - At bc50244 its words survive only in S2:16's quotation. A tree search at bc50244 (data/ excluded) finds "T_i tokens" only there, and "mean activation over" nowhere.
   - This changes nothing the document rules: §0.1's quotation is correct (14), and §1 rests on S2 §1.2.
   - Fix: cite f4b3e73's directions.py:11, or S2 §1.2 (:16), or BK §3.1 directly.

TOTALS (122 listings)
- CONFIRMED: 112
- IMPRECISE (minor): 6 (27, 30, 38, 73, 86, 113)
- IMPRECISE (substantive): 2 (78, 111)
- FAIL: 1 (122; changes nothing the document rules)
- NOT CHECKABLE: 1 (8)

OBSERVATIONS
1. §8.4 is not the full list of what the document cites. All of the following were checked above:
   - S1 §1.4 (G2's tie), §1.5 (the cap), §1.7, §1.8 (A2's extension), §1.10 (GC11);
   - S2 §5 and §7;
   - the 035947e entry's O5 and RV1; RV2 (O5, O6, B2, B3);
   - gcal.py's departures (1) and (2) and STEER_FROM; the driver's printed line; gvec.a3_capture;
   - n §0.7 and n's Clock entry; A-n2; C rules 9, 11, 13, 25.
2. A3:4 defines `A-n2 §N` and `R:N`, but the body uses neither.
3. S2:50 says "n §5's N2 sentences gain the gate's clause". The document carries this only as §7.3's report naming the deciding point and the reason; §8.3 (4) likewise names only "§7.3's report line". Whether A-n1 §7.6's N2 sentences ("at f = [f], filled under 5.3") now fill f by §3.4 is left implicit in "A-n1 §5.3 extended".
4. The merge (A-n1 §5.1) can fold +d_20 into +1 or +1/2 within 0.05. L, P and N1-V then exist at the kept point, not exactly at d_20. §3.2 ("G-LEAK-n's bar exists there") and §3.4 carry no merge clause, although A-n1 §7.4–§7.5 speak of kept points.
5. Two of the PI's words are relied on as the coordinating session read them:
   - the 5(f)(iii) confirmation is "as ruled" (PR2:15), read at R:209–210;
   - the "Go" at PR2:14 was "put to the PI" (R:193–198).
   §8.2 (2) re-asks the gate as decision (n-5) without saying it settles that pending reading, though §8.4 lists "item 2 read as go".
6. A second G-VEC STOP: §1.3 and S2 §1.5 send it to the PI, while S2:88 and PR2:13 send it to the seat with §1.5's default. R:201–204 reads these as one path; §1.3 drops the seat's step.
7. A3:4's "two declared departures": of §6.3's (i) and (ii), only (ii) is new here. (i)'s reach to G-CAL-n was ruled at S1 §1.8 and confirmed at PR2:23.

DEPARTURES
- One `git status --porcelain -- <the document's path>`: a single named path, not item 1's bare form. It printed one line.
- One loop of `git log -1 --format='%h %ad %s' --date=short` over ten named commits. It printed author dates, where item 1 names commit times.
- `git show f4b3e73:valence_core/n/directions.py | sed -n '1,22p'`, and a `git log --format` on that path. This read a referent at a commit other than bc50244, only to explain 122; every grade rests on bc50244.
- Reads beyond the brief's named sources:
  - RESULTS.md's head (:1–40), its entry-start list, and a grep over d85fc34's entry;
  - 035947e's entry in full; n v0.2's COMMITTED entry (the Clock);
  - RV1 and RV2;
  - scripts/n_sessions.py (its blob checked equal to bc50244's first);
  - gvec.py's G1/G2 docstring; gcal.py beyond the named constants.
- Text tools, none an interpreter by my reading, listed for the seat to class: `sed -n` line ranges and one `sed` substitution to offset printed line numbers; `cut` on printed lines; `cat -n`; `wc -c` and `wc -l` on the document and referent files; `printf` with `grep -c -F` counts.
- `shasum` (Perl), used by name as the brief allows.
- Two `git grep` runs at bc50244 with `-- . ':!data/**' ':!data/m[f]3/**'`.
- Nothing under data/ was listed, read or hashed. The moved record under results/raw was hashed, not opened. No guard marker reached any argv. No writes, no network.
```

## 2. Code's grading and dispositions

**Totals:** 122 listings: 112 CONFIRMED, 6 IMPRECISE (minor), 2 IMPRECISE (substantive), 1 FAIL, 1 NOT CHECKABLE; and
7 observations.

**The two substantive items, graded resolved by the PI's routing of 2026-11-19, third sitting, so no STOP under §8.3
(1).** The seat may regrade either.
- **78** (§3.6 and §8.2 (2): decision (n-5)'s declined branch). As written, the branch keeps the batch ("the batch's
  result is recorded and used by nothing") and decides N2 at f = 0.20 "as n §5 texts it". The second sitting's offered
  alternative (`f4b3e73` §2.5, and item 2 of its routing raw) struck the batch, and A-n1 §5.3 decides at f = 0.10 when the cap
  binds. The PI's routing, item 1, adopts (n-5) ("[adopt]"), so the declined branch does not operate; the checker's own
  words are "The adopted branch is unaffected." Recorded for the seat: the declined branch's text would need the
  checker's fix before it could be chosen.
- **111** (§8.2 (4): "§1, §2, §4, §6 and §7 as the seat's rulings, already routed on 2026-11-19 and carried here").
  Some rulings in §1.2, §2.2–§2.3, §4 and §7 are first made in this document, after the second sitting's routing. The
  PI's routing of the third sitting routes them: item 4, "616e940's and bc50244's readings accepted (schemas
  n-gvec-v2 / n-gcal-v2; neutral_tokens_in_R; the diagnostic's null-and-listed form; the v1 record's move to
  results/raw/; one_id; early_pause; the gate's sign +1 and its figures; no gate turn in the smoke); the review's O5 and
  O6 accepted into A-n3 §2.2–§2.3, B2's second clause not taken (§3.3) [as ruled]"; and item 1, "§1, §2, §4, §6, §7
  as the seat's rulings already routed [as ruled]". The rulings' content is unaffected. The account of their routing
  is recorded for the seat, with the checker's fix.

**The FAIL, graded not substantive:** 122, §8.4's anchor "valence_core/n/directions.py:10–11 (BK §3.1's sentence)".
At `bc50244` those lines hold the convention of record's text. BK's sentence stood at `:11` until `616e940` reworded
the readings. §0.1's quotation of it matches `f4b3e73`'s `directions.py`:11 and the second sitting's §1.2 (listing 14; the checker did not read BK). Nothing the document rules rests on the anchor. The seat may regrade it.

**The NOT CHECKABLE item:** 8, "G-VEC's re-run of record under §1 has run on the box as the PI reports it". No entry
at `bc50244` records it. n-build's run entry, committed at `e3b48ed` while the check ran, records it: PASS at index 32.

**The six minor items** (27, 30, 38, 73, 86, 113) **and the seven observations** are recorded for the seat, unapplied,
since the addendum is committed as placed. Observations 3 (whether A-n1 §7.6's N2 sentences fill f by §3.4) and 4
(A-n1 §5.1's merge against §3.2's and §3.4's d_20) bear on what runs next. They went to the n-analyzer and n-build
sessions as information, each to declare a reading for the seat if its work must choose one.

**The checker's departures** are in its report's DEPARTURES, for the seat to class.
