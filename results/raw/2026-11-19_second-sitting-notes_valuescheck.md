# The coordinating session's notes on the seat's second sitting of 2026-11-19: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over three drafts:
- T1, the entry (`RESULTS.md`, the Log's head), sha256 `b57ffb5e…a2c2`;
- T2, the five close lines, on the entries of `d85fc34`, `516b60f`, `035947e`, `355e3a2` and `8830589`, `1ffe8f0e…1e2f`;
- T3, the head of the routing raw `2026-11-19_second-sitting_pi-routing.md`, `0fa57292…9d9d`;
- and their placement, in the draft of the new `RESULTS.md`, `5a33ecd7…cee1`.

**The checker's brief** (`aef64401…0106`, 69 lines, given as a file with its sha256 to verify):
- named the sources, and gave the coordinating session's words and acts that are in no file, (c1)–(c4);
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md`, lines 18–22;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv, and anything under `data/`.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (222 lines, sha256 `d253e622…1843`). Its "S/" is the coordinating session's scratch folder.

**Totals:** 129 items (113 CONFIRMED, 5 IMPRECISE, 0 FAIL, 11 NOT CHECKABLE) and 12 observations.

## 1. Dispositions

- **Item 41** (IMPRECISE): applied in the checker's words: "records item 7's answers: A2's extension, which that entry said its next close line would record, and the cap, one of the three questions it put to the PI;".
- **Item 49** (IMPRECISE): applied in the checker's words: "two of the first sitting's three open questions (the third, the push, is item 8), answered:".
- **Item 57** (IMPRECISE): applied: "Item 1 of the list of record names `git check-attr`, not `git check-ignore`".
- **Item 61** (IMPRECISE): applied: "the five OPENs and two of Code's readings".
- **Item 116** (IMPRECISE): applied, with item 1 added, since observation 7's bullet quotes item 1: T3 reads "which quote its items 1, 2, 3, 5, 6, 7 and 8".
- **The NOT CHECKABLE items** (12, 18, 25, 33, 54, 55, 56, 59, 63, 108, 114) stand: the coordinating session's acts, words and plans, and its read of the raw.
- **The observations:**
  - 1, applied: the values-check bullet gives the counts, the dispositions and this raw;
  - 2, met: this commit places the routing raw at the link's path;
  - 3, applied: item 3's slot, "the 5(f)(iii) departure confirmed: as ruled", under the lock's draft;
  - 4, applied: why item 2's slot needs a reading;
  - 5, applied: "on Route A's request to BK (n §0.8)" in the first close line;
  - 6, applied: "(the sitting's `gcal` delta)" in the third close line and "the sitting's `gvec` delta" in the fourth;
  - 7, applied: a bullet on item 1's second STOP, noted to n-build when this commit lands;
  - 8, applied: the fourth close line says G-CAL-n's launch files also wait for ADDENDUM-n3's commit;
  - 9, applied: the fifth line cites the raw in the form of the other four;
  - 10, applied: §3's sentence quoted whole;
  - 11, met by the coordinating session's note to n-build when this commit lands, which names the fifth line;
  - 12, applied: each of the four close lines on n-build's entries points to the notes for the check and its raw.

## 2. The edits, checked by tool

- A fixed-string search over the joined finals of T1, T2 and T3 (wrapped lines joined), with each new wording present, each replaced wording absent, and each new quotation found in its source (the paste block, the answers raw, the report): 51 of 51 (`checks.txt`, `c83fdbd6…0902`, in the coordinating session's scratch). One check string was first written with a final "." for a list item that ends in ";"; the check was corrected, and the text was not changed.
- The finals: the entry `d0c76040…b176` (83 lines); the five close lines `d7a0471b…e092` (79 lines, the five concatenated); the routing raw `76b1e963…0417` (29 lines). The new `RESULTS.md` (`4b666e2b…c800`) is HEAD's with six pure insertions, +162 −0.
- No second full pass was made over the finals.

## 3. The report as returned

```text
BLIND VALUES-CHECK: the coordinating session's notes on the seat's second sitting of 2026-11-19 (T1), its five close lines (T2) and the routing raw's head (T3)

S/ means the coordinating session's scratch folder named in the brief. The brief, S/vc_brief.md, hashed equal to aef64401be32a205b9488e6ff1bc0c57af293e804882fad7ded3c93cdcd00106 (69 lines). HEAD is f4b3e73.

Hashes. T1, T2, T3 and RESULTS_new.md each hashed equal to the value the brief gives. I also hashed the other sources:
- paste_block.txt: ac65c4f41d5b9181195e7bde3e8daa77df59499dd0ea8d6ff0de70f89a554716 (23 lines)
- routing_raw.md: ee5bd033af24edf3c1127651c7141ba1fb0d832de4102b42b03ffe436cea33f7 (29 lines)
- relay_nbuild.txt: e2340b09ff3251b1efe95dfa5fa2db152d22dd12b360335383d93e166fd92e11
- relay_pod.txt: 739e182e792945ecca8a0eab5573ee71a0e47bb98ca54f42a403eb1a8e1507ca
- relay_nanalyzer.txt: 521fcfde020a935675163322d1d7911484e47c6d08a8aa39b19eb0feeafe9974

Abbreviations used below:
- A = results/raw/2026-11-19_n-gvec-stop-lock-opens_design-to-code_answers.md (HEAD, 101 lines, read in full)
- PB = S/paste_block.txt
- RR = S/routing_raw.md
- RN = S/RESULTS_new.md
- RB, RP, RAn = S/relay_nbuild.txt, S/relay_pod.txt, S/relay_nanalyzer.txt
- R = RESULTS.md at HEAD (lines 1–440)
- F1R = results/raw/2026-11-19_first-sitting_pi-routing.md
- F1A = results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md
- LR = results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md
- GI = .gitignore at HEAD (its blob equals the working file's)

How quotations were checked: every quotation was found with `grep -F` in its source. With T1's and T2's wrapped lines joined, each was also found in the text itself, quotation marks included. Bold was dropped in two quotes (items 73 and 97); no words differ.

ITEMS

T1
1. T1:1. Dated 2026-11-19, second sitting. PB:1. CONFIRMED.
2. T1:1–2. "the answers committed at `f4b3e73`". `git log -1 --name-status f4b3e73` shows one A line, the raw A, with parent d85fc34. CONFIRMED.
3. T1:1–2. The heading's list (the PI's routing, item 2's slot, items 6–8, five close lines) matches T1:11–45 and T2. CONFIRMED.
4. T1:4. The link's text and target name A, as committed. `git rev-parse f4b3e73:<A>` equals `git hash-object <A>` (585ff12d…). CONFIRMED.
5. T1:5. sha256 `887b7646…dc87`. shasum of A gives 887b764696c71f34784157d20f49fec5bc43ac135b349ea488ae00d3a312dc87, as at PB:5. CONFIRMED.
6. T1:5. 25,691 bytes. `git cat-file -s` gives 25691; PB:5; f4b3e73's message says "25,691 B". CONFIRMED.
7. T1:5. On block `355e3a2` (G-VEC's STOP, Q1–Q3). A:3. CONFIRMED.
8. T1:5–6. On block `d85fc34` (LOCK-n v0.1's OPENs, Q1–Q7). A:3. CONFIRMED.
9. T1:6. "committed by path at `f4b3e73`". f4b3e73's message says "committed by path (the paste block's item 6)". CONFIRMED.
10. T1:6. "re-hashed equal to the paste block first". f4b3e73's message says "re-hashed equal to the paste block". The order ("first") rests on c4. CONFIRMED.
11. T1:6–7. The PI's word, "Route as given". PB:23. CONFIRMED.
12. T1:7–8. The paste block "is committed here as" results/raw/2026-11-19_second-sitting_pi-routing.md. NOT CHECKABLE: this is a plan. The path is in neither the tree nor the index (`ls` finds no such file; `git ls-files` prints nothing). The name follows F1R's (R:376).
13. T1:8–10. "item N" means the paste block's item; "§8" means the raw's own routing block, whose wording differs in places. CONFIRMED (A:83–101 against PB:3–21):
    - item 2's slot: "alone: ___]" (A:89) against "alone: Go]" (PB:9);
    - item 7: "[none named: 80 stands]" (A:98) against "[none named]" (PB:18);
    - item 6: "your call on sending it]" (A:97) against "my call on sending it: not made]" (PB:17);
    - item 1: "to me" (A:88) against "to the seat" (PB:8).
    The convention's form matches R:376–378.
14. T1:11. N.1–N.4 verbatim to n-build. RB:14–18 and PB:7–11 hash equal (3943e3b0276dd2f4940aeae1e4ddf1f2e35d6b5a83bebad9543246e6bc0e416e). CONFIRMED.
15. T1:11. Item 4 verbatim to the pod session. RP:3 matches PB:11 by `grep -F`. CONFIRMED.
16. T1:11–12. Item 1's steps for the box in the coordinating session's words. RP:5–8. CONFIRMED.
17. T1:12. A.5 verbatim to n-analyzer. RAn:5 matches PB:14 by `grep -F`. CONFIRMED.
18. T1:11. "were relayed", meaning delivered. NOT CHECKABLE: the delivery results are in no file; the brief reports "Message delivered to session …" for all three sends.
19. T1:13–14. The slot quotation "[go; or strike the batch and declare the departure with G-LEAK-n alone: Go]". PB:9. CONFIRMED.
20. T1:14–15. The reading: go, with the `reward_f020` batch built. RB:26–27. CONFIRMED, as the reading relayed.
21. T1:15. Item 5's quotation "at f = 0.20 iff the lock's coherence component PASSED". PB:14. CONFIRMED. It stops before "and the cap does not bind"; the sense is kept.
22. T1:16. Item 3's quotation "OPEN 5 the gate as §2.5". PB:10. CONFIRMED.
23. T1:16. "both rest on the batch's coherence result". A:49–50: the coherence component is the batch; the lock pins "the coherence result"; N2's decision point turns on whether the coherence component PASSED. CONFIRMED.
24. T1:16. "The reading went to n-build with the relay". RB:26–28. CONFIRMED.
25. T1:16–17. "is put to the PI"; a change is relayed before G-CAL-n's launch files. NOT CHECKABLE: the coordinating session's words to the PI are in no file. Consistent with RB:28.
26. T1:18. The paste block's "no +ρ/2 or −ρ turn". PB:9. CONFIRMED.
27. T1:18–19. §3's "no +ρ/2, `reward_f020` or −ρ turn generated". A:59. CONFIRMED.
28. T1:19. "end the run at the same point, since `reward_f020` comes after +ρ/2". A:49 ("generated after +ρ/2 and before −ρ") and A:59 (the PAUSE comes at the early read). CONFIRMED.
29. T1:19. "Noted to n-build." RB:30. CONFIRMED.
30. T1:20. §3's "Code's and the coordinating session's call". A:63. CONFIRMED.
31. T1:20–21. "The paste block names two deltas, each with its own review." PB:8 (one `gvec` delta, "one blind review") and PB:9 (one `gcal` delta, "one blind review"). CONFIRMED.
32. T1:21–23. The coordinating session's side: two commits; the `gvec` delta and launch files v2 first, with the stated reasons; the `gcal` delta after; sent to n-build for its word. RB:32–36. CONFIRMED.
33. T1:22. "the box is idle at $4.39/h". NOT CHECKABLE except against c2, which agrees, and RB:33.
34. T1:24. The lock's draft went with item 7's two answers (hole 15; the cap) and item 6's Route B. RB:38–42; hole 15 is A2's extension at A:71. CONFIRMED.
35. T1:26. The raw committed by path (`f4b3e73`). See item 9. CONFIRMED.
36. T1:27. Close lines on the four entries, citing the raw. PB:17. CONFIRMED.
37. T1:27–28. "committed here, one on each entry". RN:117, :193, :325 and :466 sit in the d85fc34, 516b60f, 035947e and 355e3a2 entries (items 123–126). CONFIRMED as placed; the commit itself is a plan.
38. T1:28. The first sitting's item 4 put its four close lines under n-build, committed at `1194982`. F1R:12 and :16; 1194982's subject reads "Close lines (n-build's) on four entries"; R:392. CONFIRMED.
39. T1:28–29. This sitting's item 6 puts them under the coordinating session. PB:16–17. CONFIRMED.
40. T1:29–30. A fifth close line, on 8830589's entry, records item 7's answers. RN:549–556 sits inside R:369–432; 8830589's subject matches R:369. CONFIRMED.
41. T1:30. "which that entry said its next close line would give". IMPRECISE. 8830589's entry says that for A2's extension (R:403–404) and for the push (R:405–406). For the cap it says only that the question is with the PI (R:390–391, :407).
    Suggested fix: "records item 7's answers: A2's extension, which that entry said its next close line would record, and the cap, one of the three questions it put to the PI;".
42. T1:31–32. §6's "Inert, every one; the standing lines stand; the wording owed at each file's next change accepted as declared". A:75. CONFIRMED.
43. T1:33. Ledger (85) and (86), the seat's (§7). A:77. CONFIRMED.
44. T1:33–35. The (85) quotation. A:79. CONFIRMED.
45. T1:35–37. The (86) quotation. A:81. CONFIRMED.
46. T1:38. ADDENDUM-n3 v0.1 owed by the seat before G-CAL-n's launch files (§5), "[as ruled]". A:71 and PB:17. CONFIRMED.
47. T1:39. "Route A's request to BK (n §0.8)" and its quotation "[not made; Route B of record; my call on sending it: not made]". PB:17. CONFIRMED.
48. T1:39–40. "No request was sent, and Route B is of record." PB:17 and A:54. CONFIRMED.
49. T1:41. "the first sitting's two open questions". IMPRECISE: R:407 lists three questions with the PI (the push, A2's extension and the cap).
    Suggested fix: "**Item 7,** two of the first sitting's three open questions (the third, the push, is item 8), answered:".
50. T1:41–42. The item 7 quotation. PB:18. CONFIRMED.
51. T1:42–43. "No cap is named, so 80 stands", with §8 item 7's default "none named: 80 stands". A:98; the cap of 80 is at F1A:81 and F1R:15. CONFIRMED.
52. T1:43. "Both answers went to n-build for the lock's draft." RB:22 and RB:39–40. CONFIRMED.
53. T1:44. Item 8's "[yours]". PB:21. CONFIRMED.
54. T1:44. "put to the PI again, and not made on "Route as given"". NOT CHECKABLE except against c3, which agrees.
55. T1:44–45. The push's C.5 line goes in a later close line. NOT CHECKABLE: a plan. It follows R:405–406's form.
56. T1:47–48. The `git check-ignore` departure: run after 8830589's commit, exit status only, and its purpose. NOT CHECKABLE except against c1, which agrees. The date is c1-dependent too. For the purpose: GI:309 reads "!/data/n/gvec/gvec.json", as R:359 says.
57. T1:48–49. "Item 1's list names `git check-attr`, not `git check-ignore`." The fact is right (LR:18). IMPRECISE in its reference: T1:8–10 defines "item N" as the paste block's item, so "Item 1" reads as the paste block's item 1. The first sitting's entry wrote "Item 1 of the list of record" (R:416).
    Suggested fix: "Item 1 of the list of record names `git check-attr`, not `git check-ignore`."
58. T1:50. The values-check is one blind pass over the entry's draft, the five close lines and the routing raw's head. vc_brief.md:11–20. CONFIRMED.
59. T1:51–52. Committed by path; home-folder count 0; not pushed. NOT CHECKABLE: plans. Pre-check: T1, T2, T3 and RR contain none of "/Users/", "/private/", "tmp/claude" or the user name (grep -c gives 0 each).

T2, close line 1 (d85fc34's entry)
60. T2:1. Heading: "PI date 2026-11-19, second sitting", "the coordinating session's, item 6". PB:1 and PB:16–17. The form follows 1194982's close lines. CONFIRMED.
61. T2:1–2. "the five OPENs and Code's two readings". IMPRECISE: d85fc34's entry says "two of Code's readings" (R:24, R:31).
    Suggested fix: "the five OPENs and two of Code's readings".
62. T2:3–4. Link, sha256, "committed by path at `f4b3e73` on the PI's "Route as given"". See items 4, 5, 9 and 11. CONFIRMED.
63. T2:4 (also T2:25, :35, :52). "read in full". NOT CHECKABLE: the coordinating session's own read.
64. T2:4–5. "rules Q1–Q7 in its §2". A:37. CONFIRMED.
65. T2:5. The item 6 quotation "close lines on 355e3a2, d85fc34, 035947e and 516b60f citing it". PB:17. CONFIRMED.
66. T2:6. OPEN 1's "(b), with (a)'s locator" (§2.1). A:39. CONFIRMED.
67. T2:6–7. The paraphrase of the form and the locator, and the quotation "no committed text is edited". A:39. CONFIRMED.
68. T2:8. OPEN 2's quotation. A:41. CONFIRMED.
69. T2:9. OPEN 3's "(b)" and "G-TIME-n's figures enter v1.0 with the projections and the cap". A:43. CONFIRMED.
70. T2:10–11. OPEN 4's quotation and "confined to n's S-span arms". A:45. CONFIRMED.
71. T2:11. Item 3's "the 5(f)(iii) departure confirmed: as ruled". PB:10. CONFIRMED.
72. T2:12. OPEN 5's quotation. A:47. CONFIRMED.
73. T2:12–14. The leakage and coherence components, and "a fail is neither a STOP nor a PAUSE". A:48–49 (bold dropped). CONFIRMED.
74. T2:14–15. Ledger (85): n:81's "never above 0.20" against the rule's "below dose 0.20" (§7). A:79 and A:47; CLAUDE.md rule 5(f)(iv). CONFIRMED.
75. T2:16. R-L1 and R-L2 "both stand" (§2.6). A:54. CONFIRMED.
76. T2:16–17. The item 6 quotation. PB:17. CONFIRMED; see observation 5 on its context.
77. T2:18–19. §5's lists, and ADDENDUM-n3 v0.1 owed before G-CAL-n's launch files. A:71. CONFIRMED.
78. T2:19. Item 7 answers hole 15: "A2's extension to G-CAL-n [confirmed: confirmed]". PB:18 and A:71. CONFIRMED.
79. T2:20. This entry's departures are inert (§6). A:75 (the `d85fc34` clause). CONFIRMED.

T2, close line 2 (516b60f's entry)
80. T2:22–23. Heading on R-v1–R-v5. R:90. CONFIRMED.
81. T2:24–25. Link, sha256, commit, "Route as given". CONFIRMED.
82. T2:25–26. "R-v1–R-v5 accepted" (§4). A:65 and A:10. CONFIRMED.
83. T2:27–28. The cross-check quotation. A:67. CONFIRMED.
84. T2:29–30. Departures inert, the `grep -A 3` among them, and the standing-line quotation. A:75; R:97–99. CONFIRMED.

T2, close line 3 (035947e's entry)
85. T2:32–33. Heading: O1, O2, O5, departure (10) and R12. A:56; R:163–187. CONFIRMED.
86. T2:34–36. Link, sha256, commit; "rules them in its §3". A:56–63. CONFIRMED.
87. T2:37. O1's quotation. A:58. CONFIRMED.
88. T2:38–40. O2: "with +ρ passed", and the PAUSE quotation. A:59. CONFIRMED.
89. T2:41. O5's quotation. A:60. CONFIRMED.
90. T2:42–43. Departure (10), the `figures_of` seam and R12's placement, with the quotation. A:61; R:164–172. CONFIRMED; see observation 6.
91. T2:44–45. The sitting's `gcal` delta, "three changes …" (§3). A:63. CONFIRMED.
92. T2:45–46. §1.4 (i): the arrival quotation, the projection on the unit valence row, and `arrival_all` beside per turn. A:31. CONFIRMED.
93. T2:47. Departures inert (§6). A:75. CONFIRMED.

T2, close line 4 (355e3a2's entry)
94. T2:49–50. Heading on G-VEC's STOP. CONFIRMED.
95. T2:51–53. Link, sha256, commit; "rules the STOP block's Q1–Q3 in its §1". A:12; R:263. CONFIRMED.
96. T2:54. "Q1 and Q3:" with "path (b), carrying (a)'s figures in the run of record" (§0). A:7; §1.2's heading at A:16 groups Q1 and Q3. CONFIRMED.
97. T2:54–56. The convention quotation (§0). A:7 (bold dropped). CONFIRMED.
98. T2:56. The ids of record stand: "nothing is re-rendered" (§1.2). A:17. CONFIRMED.
99. T2:57–59. Q2: a `diagnostic` block at both indices over the 96 neutral passages, descriptive, "none a decision", with the four figures. A:24–28. CONFIRMED.
100. T2:60–61. A PASS fills holes 1–7, with this entry's figures beside under "every position"; G-CAL-n's launch files follow. A:33. CONFIRMED; see observation 8.
101. T2:61–62. The second-STOP quotation. A:33. CONFIRMED; see observation 7.
102. T2:62–63. "Code re-runs nothing on either outcome without the routing." A:33. CONFIRMED.
103. T2:64–65. The wording-owed quotation (§1.4 (ii)). A:31; R:318–321. CONFIRMED.
104. T2:66. Departures inert (§6). A:75. CONFIRMED.

T2, close line 5 (8830589's entry)
105. T2:68–69. Heading: the coordinating session's; the PI's answers on A2's extension and the cap. PB:18. CONFIRMED.
106. T2:69–70. The item 7 quotation. PB:18. CONFIRMED.
107. T2:70–71. The push, item 8, again "[yours]". PB:21. CONFIRMED.
108. T2:71. "is put to the PI again". NOT CHECKABLE except against c3, which agrees.
109. T2:71–73. Link; committed by path at `f4b3e73`. CONFIRMED.
110. T2:73–74. The raw classes this entry's departures inert, with the §0 quotation. A:10, and A:75's `8830589` clause. CONFIRMED.
111. T2:74–75. The notes at the Log's head give the rest. RN:24. CONFIRMED.

T3
112. T3:1. The title, "(second sitting), verbatim (the PI → the coordinating session)". PB:1; the form of F1R:1. CONFIRMED.
113. T3:3. PI date 2026-11-19. PB:1. CONFIRMED.
114. T3:3. Given "in chat" and "saved verbatim by the coordinating session on receipt". NOT CHECKABLE: the brief describes PB as the paste block as saved on receipt.
115. T3:3. Its last line, "PI: Route as given". PB:23 and RR:28. CONFIRMED.
116. T3:3. "which quote its items 2, 3, 6, 7 and 8". IMPRECISE: T1:15 also quotes item 5, "at f = 0.20 iff the lock's coherence component PASSED" (PB:14). T1 quotes no text from items 1 or 4.
    Suggested fix: "which quote its items 2, 3, 5, 6, 7 and 8".
117. T3:3. "The 23 lines between the fences are byte-identical to the saved copy", with its sha256. `sed -n 6,28p RR | shasum` gives ac65c4f41d5b9181195e7bde3e8daa77df59499dd0ea8d6ff0de70f89a554716, PB's hash. The fences are RR:5 and RR:29; PB has 23 lines. CONFIRMED.
118. T3:1–3. T3 is RR:1–3 byte for byte: `sed -n 1,3p RR | shasum` gives T3's sha256. CONFIRMED.

Placement
119. T1, T2, T3 and RN hash equal to the brief's values. CONFIRMED.
120. RESULTS.md in the working tree is HEAD's: both blobs are d61d5d0b2074e9b7821c8af32b8e16bd5ed49582. CONFIRMED.
121. `git diff --no-index RESULTS.md S/RESULTS_new.md` shows numstat "124 0" in six pure-insertion hunks: -23,0 +24,53; -63,0 +117,20; -119,0 +193,9; -242,0 +325,16; -367,0 +466,18; -432,0 +549,8. CONFIRMED.
122. T1 is RN:24–76, byte-equal to T1, after the blank line RN:23 under "## Log — Phase 2" and before d85fc34's entry at RN:77. CONFIRMED.
123. Close line 1 is RN:117–136, equal to T2:1–20. It follows the last line of d85fc34's entry (R:63, "**Next:** …", which is RN:116) and precedes the entry's blank line (RN:137). CONFIRMED.
124. Close line 2 is RN:193–201, equal to T2:22–30. It follows 516b60f's last line (R:119, RN:192) and precedes RN:202. CONFIRMED.
125. Close line 3 is RN:325–340, equal to T2:32–47. It follows 035947e's last line, the dated note's last sub-bullet (R:242, RN:324), and precedes RN:341. CONFIRMED.
126. Close line 4 is RN:466–483, equal to T2:49–66. It follows 355e3a2's last line (R:367, RN:465) and precedes RN:484. CONFIRMED.
127. Close line 5 is RN:549–556, equal to T2:68–75. It follows 8830589's last line (R:432, RN:548) and precedes RN:557. CONFIRMED.
128. The five entries are those commits' entries. `git log --format=%h -- RESULTS.md` lists, newest first, d85fc34, 516b60f, 035947e, 355e3a2, 8830589 and 1194982. Their subjects match the entry headings at R:24, :65, :121, :244 and :369. CONFIRMED.
129. T2's five lines are separated by blank lines (T2:21, :31, :48, :67), in the brief's order, each at the entry's sub-bullet indent ("  - **Close"), as 1194982's lines are. CONFIRMED.

TOTALS
129 items: 113 CONFIRMED, 5 IMPRECISE (41, 49, 57, 61, 116), 0 FAIL, 11 NOT CHECKABLE (12, 18, 25, 33, 54, 55, 56, 59, 63, 108, 114). 12 observations.

OBSERVATIONS
1. T1:50. The values-check bullet has no counts, dispositions or raw link, though T1:51 commits "the values-check raw". The first sitting's notes give all three (R:425–430).
2. T1:7–8. The link's target, results/raw/2026-11-19_second-sitting_pi-routing.md, does not exist yet. The commit must place RR (ee5bd033af24edf3c1127651c7141ba1fb0d832de4102b42b03ffe436cea33f7) at exactly that name.
3. T1 records the PI's word in item 2's slot but not in item 3's. The slot "[as ruled; the 5(f)(iii) departure confirmed: as ruled]" (PB:10) is the confirmation §2.4 asks for "at routing" (A:45). Only T2:11 and RB:41 carry it. One clause under T1:24 would put it in the notes.
4. T1:13–17 does not say why the slot needs a reading at all. The PI's "Go" fills the blank after the alternative ("…with G-LEAK-n alone: ___", A:89), not the bracket's default "go".
5. T2:16–17. The item 6 quotation under R-L1 and R-L2 does not say that it answers Route A's request to BK, as T1:39 does. Read alone, it could be taken as the PI's word on R-L1 and R-L2. Suggest: "Item 6 of the PI's routing, on Route A's request to BK (n §0.8): …".
6. T2:42–43 and T2:64–65. In both quotations "this delta" is the seat's term for this sitting's `gcal` and `gvec` deltas (A:61–63, A:31; PB:8). In a close line on 035947e's entry, which is itself G-CAL-n's delta, "rides with this delta" can read as 035947e's own committed delta. "(the sitting's `gcal` delta)" after the quotation would remove the doubt.
7. Two texts route a second STOP differently, and nobody notes it. §1.5 sends it "for the PI" (A:33). Item 1 sends a STOP at both indices "to the seat with §1.5's default [go]" (PB:8; §8 says "to me", A:88). T1:18–19 notes a different paste-block/§3 difference, but not this one.
8. T2:60–61. "and G-CAL-n's launch files follow" is §1.5's wording. Those launch files also wait for ADDENDUM-n3's commit (A:51, A:71; PB:9). Close line 1 says so (T2:18–19); close line 4 does not.
9. T2:71–73. The fifth line cites the raw without its sha256 and without "on the PI's "Route as given"", unlike the other four (T2:4, :25, :35, :52). Form only.
10. T1:20–21. The paste block gives each delta its own review, while §3's sentence carries "with one review covering both" (A:63). T1 implies the difference without quoting the words. Low.
11. RB:45 told n-build that the notes commit touches RESULTS.md with "the four lines on your entries, and my entry at the Log's head". The commit also adds a fifth line, on the coordinating session's own entry. RB's "rebuild your entry's insertion from HEAD" covers it. Informational.
12. No close line points to the values-check, which T1 carries. 1194982's lines each named the line that carried theirs. The fifth line's "give the rest" partly covers this. Optional.

DEPARTURES
1. The permission system denied `git show --name-status f4b3e73`, the brief's form. In its place I ran `git log -1 --name-status --format='%H%n%P%n%B' f4b3e73`, which printed the id, the parent, the message and the one A line.
2. I used `cut -c1-110` to shorten printed lines of RN around the insertion points, and `tr '\n' ' '` once on grep's line-number output. Neither is named in the brief's command list; neither is an interpreter.
3. I ran one `git status --porcelain` with a pathspec of three named files (RESULTS.md, A, .gitignore), not item 1's bare form. It printed nothing.
4. I ran `git log -1 --format='%h %p %<(110,trunc)%s'` on a33252a, which the brief does not name, alongside the named commits. It printed the id, the parent and a truncated subject.
5. Reads beyond the brief's SOURCES:
   - LR:18 (the brief's RULES file), to check T1:48–49;
   - one `grep -n -F` over all of F1A for two fixed strings. It printed lines 81 and 74; line 74, the §8 heading, is outside lines 3 and 75–90;
   - `git ls-files` and a name-only `ls` of results/raw/2026-11-19_second-sitting_pi-routing.md (named in T1; absent) and of F1R.
6. I used `sed -n` with a hold-space script (`1h;1!H;${x;s/\n */ /g;p;}`) to join T1's and T2's wrapped lines for quote matching.
7. One zsh error, from an unquoted `====` in an `echo`, ran nothing. The `git show 1194982 -- RESULTS.md` it blocked was re-run as `git show --format= 1194982 -- RESULTS.md`.
8. One `cat -A` failed silently, because macOS cat has no -A; the fallback `sed -n '5p;29p'` printed RR's two fence lines.

Not departures by my reading, listed for the seat:
- `git cat-file -s` and `git hash-object` on A, which is not a data file;
- `git rev-parse` of HEAD, HEAD:RESULTS.md, HEAD:.gitignore and f4b3e73:A, compared in the shell;
- `git diff --no-index --numstat` and `-U0` on RESULTS.md against RN;
- `grep -n gvec .gitignore`, which printed .gitignore's lines 303–314; they name data/n/gvec paths as text;
- `git log --format=%h -n 10 -- RESULTS.md`;
- one grep whose pattern held the home-folder strings and the user name, over the four texts only;
- shell functions, loops, printf and echo.

Nothing under data/ was opened, listed or hashed. No `git check-ignore` was run, no interpreter but shasum, no guard-marker string in any argv. No writes, no network.
```
