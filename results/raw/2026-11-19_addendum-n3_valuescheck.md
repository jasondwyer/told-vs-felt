# ADDENDUM-n3 v0.1 — COMMITTED: the coordinating session's texts, the blind values-check as returned, with every disposition

PI date 2026-11-19. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over four drafts:
- T1, the entry (`RESULTS.md`, the Log's head), sha256 `c6536092…23e3`;
- T2, the three close lines, on the entries of `616e940`, `bc50244` and `ab72d0f`, `efe7ae64…c644`;
- T3, the head of the routing raw `2026-11-19_third-sitting_pi-routing.md`, `8d2aff36…75bf`;
- T4, the referent-check raw's header and its §2, Code's grading, with its §1 (the report whole) omitted, `83079709…6d66`.

**The checker's brief** (`5bc000c7…04cc`, 59 lines, given as a file with its sha256 to verify):
- named the sources, and gave the coordinating session's words and acts that are in no file, (c1)–(c5);
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md`,
  lines 18–22;
- carried the briefs' two lines, on item 3's pathspec in a check and on globs;
- barred any interpreter but `shasum`, any write, any network, any guard marker in an argv, and anything under
  `data/`.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (212 lines, sha256 `3cd28f80…fdc5`). It
held no local path.

**Totals:** 120 items (99 CONFIRMED, 8 IMPRECISE, 0 FAIL, 13 NOT CHECKABLE) and 7 observations.

## 1. Dispositions

- **Item 11** (IMPRECISE): applied in the checker's words; G-VEC's PASS entry is named as in at `e3b48ed`.
- **Item 21** (IMPRECISE): applied in the checker's words; each item's target is named.
- **Items 35 and 100** (IMPRECISE): applied, in the entry and the raw: "the second sitting's offered alternative".
- **Item 39** (IMPRECISE): applied: "rulings" in place of "acceptances".
- **Item 41** (IMPRECISE): applied: "Items 4 and 1 route them", with item 1's bracket quoted beside item 4.
- **Item 58** (IMPRECISE): applied: the `git log --format` on that path added.
- **Item 89** (IMPRECISE): applied: the two brief lines quoted with their capitals.
- **The NOT CHECKABLE items** (8, 14, 24, 26, 45, 47, 48, 61, 72, 79, 93, 116, 119) stand: the coordinating session's
  acts, words and plans, and this commit's own facts.
- **The observations:**
  - 1, applied: the coordinating session's two `jq` extractions, of the referent check's report and of this check's,
    declared beside the push's;
  - 2, applied: `e3b48ed` named (item 11's fix), and the NOT CHECKABLE listing 8's disposition carried in the entry;
  - 3, applied: the FAIL's paragraph in the raw gains "The seat may regrade it", and the entry reads "any of the three
    graded items";
  - 4, applied: item 1's third bracket, "§1, §2, §4, §6 and §7 [as ruled]", in the heading;
  - 5, applied: the C.5 line's change of place stated, with the close line on `ab72d0f`'s entry pointing to it;
  - 6, applied: gitleaks' and gl5's exit statuses stated, gl5's by its own docstring (exit 1 for READ items, 2 for a
    halt). The five findings now read as two digests by gl5's classes and three listed to READ, which the coordinating
    session read and cleared as digests;
  - 7, applied: "correct" bounded to the referents the checker read ("the checker did not read BK"), in the entry and
    the raw.

## 2. The edits, checked by tool

- A fixed-string search over the joined finals of T1 and T4 (wrapped lines joined): each new wording present, each
  replaced wording absent, each placeholder gone, and each new quotation found in its source (the paste block, the
  referent brief, gl5's docstring, the screen's outputs, this report). 41 of 41 (`checks.txt`, `6149d550…ddd6`, in the
  coordinating session's scratch).
- The finals: the entry `a4203970…a745` (113 lines); the referent-check raw `a42709e8…4335` (294 lines, the report inside it still
  byte-equal to the checker's). T2 and T3 are unchanged.
- No second full pass was made over the finals.

## 3. The report as returned

```text
VALUES-CHECK — ADDENDUM-n3 v0.1's commit texts (T1 entry, T2 close lines, T3 routing raw head, T4 referent-check raw header and grading). Blind; I check, I do not rewrite.

HEADER
- Brief: sha256 equal to the given value, 59 lines.
- Texts: T1 (77 lines), T2 (34), T3 (3) and T4 (53), each sha256 equal to the brief's value.
- Sources: A3 7f4a7a75…9313, PB 084df899…74d9, RC 30060f60…15c3 and PR12 1815e332…d9c3, each equal to the brief's value. HEAD is e3b48ed. RESULTS.md's working blob equals HEAD's (rev-parse against hash-object).
- Citations use repository paths or scratch basenames. This report contains no local path.

LABELS
- A3 = ADDENDUM-n3-capture-convention-reward-gate-and-interval-v0_1.md (root).
- PB = paste_block.txt; RR = routing_raw.md; RC = rc_report.txt; RCR = rc_raw.md; RB = rc_brief.md (scratch, route19c).
- PR12 = push_record12.txt; SC = screen.txt; GLR = gl_run.txt; GL5 = gl5.txt (scratch, push12 and push12/final).
- R = RESULTS.md at HEAD. The four entries: e3b48ed :24–156, bc50244 :157–237, 616e940 :238–313, ab72d0f :314–396.
- S2 = results/raw/2026-11-19_n-gvec-stop-lock-opens_design-to-code_answers.md; PR2 = results/raw/2026-11-19_second-sitting_pi-routing.md.
- A-n1 = ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md; LR = results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md.
- 7a54eb9 = that commit's message and name-status. (c1)–(c5) = the brief's list of the coordinating session's words and acts.
- "byte check" = the quoted string, found by fixed-string search in both the joined text and the source.

ITEMS

T1, the entry
1. T1:1 — the date 2026-11-19 — PB:1. CONFIRMED.
2. T1:1–2 — the quoted title, "the capture convention of record, … under 5(f)(iii)" — A3:1. CONFIRMED (byte check).
3. T1:2–3 — "committed by path as the seat placed it" — PB:3–5 (placed untracked, "commit by path"; its sha256 equals the file's); A3:2, :4. CONFIRMED.
4. T1:3 — "after its referent check" — RC (whole); PB:8; A3:79 (1). CONFIRMED.
5. T1:3–4 — the third sitting's routing ("Route as given"; item 1's (n-5) [adopt] and (n-6) [confirmed]; item 7's [as ruled]) — PB:1, :8, :18, :23. CONFIRMED (see observation 4).
6. T1:5–6 — the file at root and its full sha256 — shasum; PB:4–5. CONFIRMED.
7. T1:6 — 20,327 bytes — PB:5 "(20,327 bytes)" for the same sha256; RC:5. CONFIRMED. Not measured here.
8. T1:6 — "re-hashed before the commit" — NOT CHECKABLE: the coordinating session's act at commit time.
9. T1:7–8 — an addendum, not a new version; n v0.2 (30a3d0f5…04f4) of record with A-n1 (a61f13d) and A-n2 (7a54eb9), "(its header)" — A3:4 (the abbreviation found in both by tool). A git log on A-n1's path shows a61f13d alone, and 7a54eb9's subject is "ADDENDUM-n2 v0.1 -- COMMITTED". CONFIRMED.
10. T1:9 — the launch files wait on this commit "(its §0.3)" — A3:14. CONFIRMED.
11. T1:9 — "and on G-VEC's PASS entry, n-build's" — PB:9–10 (items 2 and 3); A3:79 (3). IMPRECISE. The PASS entry is already committed at e3b48ed, which is HEAD (R:24, "PASS at index 32"). R:59–60 has the launch files going to the box "only after ADDENDUM-n3's commit". T1 never names e3b48ed.
   Fix: "G-CAL-n's launch files wait on this commit (its §0.3); G-VEC's PASS entry, n-build's, which they are built on (item 3), is in at `e3b48ed`."
12. T1:10 — "(the addendum's §8.2 and §8.3 (2))" — A3:77, :79 (2). CONFIRMED.
13. T1:10–13 — the whole paste block with the PI's word, byte for byte as saved on receipt — RR:6–28 hashes equal to PB (084df899…74d9); RR:28 is "PI: Route as given". CONFIRMED for the raw's content.
14. T1:12 — the raw's committed path, results/raw/2026-11-19_third-sitting_pi-routing.md — NOT CHECKABLE: absent at HEAD (name-only ls). The name follows 7a54eb9's results/raw/2026-11-18_third-sitting_pi-routing.md.
15. T1:14 — the header, "DESIGN → PI → CODE (master session) — PI date 2026-11-19 (third sitting)" — PB:1. CONFIRMED (byte check).
16. T1:14–15 — the routing confirms the date the header asks the PI to confirm — A3:2 "(the PI confirms the date at routing)"; A3:77 (1); PB:1. CONFIRMED.
17. T1:16 — "Route as given" — PB:23. CONFIRMED.
18. T1:19 — item 1, verbatim — PB:8. CONFIRMED (string-equal once the "> " prefix is stripped).
19. T1:21 — item 7, verbatim — PB:18. CONFIRMED (string-equal).
20. T1:23 — item 8, verbatim — PB:21. CONFIRMED (string-equal).
21. T1:25 — "Items 1–5 went to the n-build and pod sessions, and item 6 to the n-analyzer session, as relayed." — Against (c2): items 1–5 went to n-build, item 5 also to the pod session, and item 6 to n-analyzer, each verbatim. IMPRECISE: the text reads as if all five items went to the pod session. ab72d0f's form names each target (R:324–325).
   Fix: "Items 1–5 went verbatim to the n-build session, item 5 also to the pod session, and item 6 verbatim to the n-analyzer session."
22. T1:26 — "The addendum committed by path after its referent check" — PB:18. CONFIRMED (byte check).
23. T1:26–27 — carried here "as ADDENDUM-n2's were (7a54eb9)" — CONFIRMED. 7a54eb9's message has the same form: the paste-block raw; "the referent check of its 6.4 by a fresh blind checker, the report whole and Code's grading"; the entry at the Log's head; "the coordinating session's close line". (c1) says "my referent check by a blind checker, my commit". The message itself does not name who committed.
24. T1:27 — "The relay told n-build so." — NOT CHECKABLE: no file holds it. Consistent with (c1).
25. T1:28 — item 8 done as push #12, ecf349d..bc50244, on the PI's "Push now" — CONFIRMED.
   - PR12:1, :3, :31.
   - PB:21's "19 commits at this writing" equals the range: `git log --format=%h ecf349d..bc50244` counts 19.
26. T1:28–29 — done "before this block arrived"; "Origin was at bc50244 when the block arrived" — NOT CHECKABLE as to timing. Consistent with (c4) and PR12:31 ("remote main now bc5024490f5d…").
27. T1:31–32 — close lines on 616e940's and bc50244's entries citing the addendum, and one on the coordinating session's ab72d0f entry — PB:18; T2 (three lines, each citing A3 by path and sha256); R:314. CONFIRMED.
28. T1:33–34 — the departures inert, "the check-ignore and the checkers' forms included" — PB:18. CONFIRMED (byte check).
29. T1:35–36 — the "Go" read as go with reward_f020 built, "confirmed by the addendum's (n-5)" — R:326–331; PB:18. CONFIRMED (byte check).
30. T1:37 — the two-commit order, gvec first and gcal after, accepted — PB:18; R:338–341. CONFIRMED.
31. T1:38–39 — the referent check by a fresh blind checker, against §8.4's referents and the other cited sources, every referent read at bc50244 — RB:1, :10, :17; RC:6–7. CONFIRMED. The one read at f4b3e73 (RC:228) is declared at T1:69, and RC:228 says every grade rests on bc50244.
32. T1:39–40 — 122 listings: 112/6/2/1/1, with 7 observations — RC:201–206, :208–223. CONFIRMED.
33. T1:41 — the two substantive items graded resolved by the routing; no STOP under §8.3 (1) — RCR:265–266 (T4:24–25). CONFIRMED.
34. T1:42 — listing 78 is (n-5)'s declined branch "as §3.6 and §8.2 (2) word it" — RC:123 ("A3:44 with A3:77 (2)"); A3:44, :77. CONFIRMED.
35. T1:42–43 — "the batch kept where the second sitting's offer struck it" — S2:53 ("The alternative, for the PI: … with G-LEAK-n alone as the gate and no batch"); S2:89; PR2:14 ("[go; or strike the batch …: Go]"); RC:124–125. IMPRECISE (minor): striking the batch was the alternative offered beside go, and the PI's "Go" kept the batch (R:326–331). "the second sitting's offer struck it" can be read as the sitting itself striking it.
   Fix: "…where the second sitting's offered alternative struck it…".
36. T1:43 — "A-n1 §5.3's cap clause passed over" — RC:126; A-n1:48 (f = 0.10 against N1-V at d_eq when 2·d_eq > 1). CONFIRMED.
37. T1:43–44 — item 1's "[adopt]" leaves the branch unused; the checker's words "The adopted branch is unaffected" — PB:8; RC:127. CONFIRMED (byte check).
38. T1:45 — listing 111, §8.2 (4)'s "already routed on 2026-11-19" — A3:77; RC:172. CONFIRMED (byte check).
39. T1:45–46 — "some of the acceptances in §1.2, §2.2–§2.3, §4 and §7 are first made in the addendum" — RC:173–177. IMPRECISE (minor): §7's item is a dated note, the fourth (A3:71; RC:177), not an acceptance. T4:33 says "rulings".
   Fix: "some of the rulings in §1.2, §2.2–§2.3, §4 and §7 are first made in the addendum".
40. T1:46–47 — item 4's quote, "616e940's and bc50244's readings accepted (…); … [as ruled]" — PB:11. CONFIRMED (byte check; the parenthesis is elided with "(…)").
41. T1:46 — "Item 4 routes them" — PB:11, :8. IMPRECISE (minor): item 4 covers the acceptances in §1.2, §2.2–§2.3 and §4. §7's note is covered only by item 1's "§1, §2, §4, §6, §7 as the seat's rulings already routed [as ruled]", which T4:37–38 cites beside item 4.
   Fix: "Items 4 and 1 route them: "…[as ruled]"; and "§1, §2, §4, §6, §7 as the seat's rulings already routed [as ruled]"."
42. T1:48 — the FAIL, listing 122, graded not substantive; the anchor "valence_core/n/directions.py:10–11 (BK §3.1's sentence)" — A3:81 (backticks dropped; byte check); RC:194–199; RCR:290–292. CONFIRMED.
43. T1:49 — "reworded at 616e940" — RC:196; R:257–258 ("directions.py's readings are reworded to the convention of record"). CONFIRMED.
44. T1:49 — "§0.1's quotation of BK's sentence is correct" — RC:49 (listing 14, "CONFIRMED (quotation byte for byte)"). CONFIRMED as graded (see observation 7).
45. T1:50 — "The seat may regrade any of the three." — NOT CHECKABLE: a disposition. T4:25 says "either" of the two (observation 3).
46. T1:51–52 — the six minor items and the seven observations recorded in the raw, unapplied, since the addendum is committed as placed — RCR:291–294 (T4:48–49); RC:203, :208–223. CONFIRMED.
47. T1:52–53 — observations 3 and 4 bear on what runs next and went to n-analyzer and n-build as information — RC:216–217 for the content. The sending is NOT CHECKABLE; consistent with (c5).
48. T1:54 — the raw link, results/raw/2026-11-19_addendum-n3_referent-check.md — NOT CHECKABLE: absent at HEAD. Its content is RCR, and the name follows 7a54eb9's results/raw/2026-11-18_addendum-n2_referent-check.md.
49. T1:55–56 — C.5: ecf349d..bc50244, 19 commits, pushed 2026-11-19 on the PI's "Push now", behind the amended screen (screen4.py with gl5.py) — PR12:1–3, :12, :31–32. CONFIRMED.
50. T1:55 — "(the line owed since that push)" — PR12:32 ("for the next close line"); R:364–365. CONFIRMED that the line was owed; its place changed (observation 5).
51. T1:57 — the screen's six classes CLEAR over the range — SC:2–7 (url_host, ipv4, email, port, pod_token, local_path; inside 0 each); PR12:4–9. CONFIRMED.
52. T1:58 — gitleaks 8.30.1 (default rules) found 5, all digests, so no halt — PR12:12, :15, :25, :29 ("No halts."); GLR:3; GL5:1–4. CONFIRMED (see observation 6).
53. T1:59–60 — 3 READ in data/n/ids/MANIFEST.json at 516b60f, its tokenizer_files digests, read and cleared at 516b60f's check and again at the push — PR12:22, :26 ("verification" where T1 says "check"); GL5:4, :6. CONFIRMED.
54. T1:61–62 — 2 digests by nesting and file: data/n/gvec/gvec.json at 355e3a2, and a report file under data/n/reports at 9f64305, a count by path class — PR12:18–21, :27–28; GL5:2–3, :5. CONFIRMED.
55. T1:64–66 — the coordinating session's departure at push #12: one jq printing each finding's file, commit and 8-character prefix, the report file's name masked; one finding a digest inside data/n/reports, "where item 4 has the screen print a count" — PR12:30; (c3); LR:21. CONFIRMED (see observation 6).
56. T1:67 — the checker's `git status --porcelain` on the addendum's path alone — RC:226. CONFIRMED.
57. T1:68 — one loop of `git log -1` over ten named commits, printing author dates — RC:227. CONFIRMED.
58. T1:69 — "one `git show f4b3e73:` of `directions.py`, read only to explain listing 122" — RC:228. IMPRECISE (minor): RC:228's departure also names "a `git log --format` on that path", and T1 says "as its report states them".
   Fix: "one `git show f4b3e73:` of `directions.py`, with a `git log --format` on that path, read only to explain listing 122".
59. T1:69–70 — reads beyond its named sources; the text tools; two `git grep` runs with the exclusions — RC:229–235, :237. CONFIRMED.
60. T1:71 — nothing under data/ listed, read or hashed; no guard marker in an argv — RC:238. CONFIRMED as the report states it.
61. T1:74–76 — committed by path (the addendum, the routing raw, the referent-check raw, the values-check raw, the entry, three close lines); the home-folder count 0; nothing on a model; not pushed — NOT CHECKABLE: the commit does not exist yet.
   - The form matches 7a54eb9's file list (the addendum, RESULTS.md, three raws).
   - Of the texts and raws in hand (T1–T4, RR, RCR, RC, A3), none holds "/Users", "/private", "/tmp", "/var/", "/home", "~/" or "Users-" (0 each).

T2, the close lines
62. T2:1–2 — the close's header: PI date 2026-11-19, third sitting; the coordinating session's; item 7; the seat's ruling, ADDENDUM-n3 v0.1 — PB:1, :17–18. CONFIRMED.
63. T2:3–4 — the path and sha256 7f4a7a75…9313 — shasum (abbreviation by cut; found twice in T2). CONFIRMED.
64. T2:4–6 — makes this delta's convention the convention of record; "position 0 … the count both" (§1.1) — A3:16, :18 (bold dropped; byte check); R:244–245. CONFIRMED.
65. T2:6–9 — item 4 accepts this delta's readings with bc50244's (quote) — PB:11. CONFIRMED (byte check).
66. T2:10 — this entry's departures inert (item 7) — PB:18; R:286–295. CONFIRMED.
67. T2:14–17 — bc50244's close: header, path, sha256, committed by path on "Route as given" — PB:1, :17–18, :23; shasum. CONFIRMED.
68. T2:17–19 — carries this delta into the design chain: the arrival score (§2.1), reward_f020 (§3.3), G-CAL-n's form of record (§4) — A3:4, :26, :38, :48 (each citing bc50244); R:157–181. CONFIRMED.
69. T2:20–21 — item 1 adopts the gate (quote) — PB:8. CONFIRMED (byte check).
70. T2:22–23 — item 4 accepts the readings, and "the review's three items for the seat" (quote) — PB:11; R:197 ("its O5, O6 and B2's second clause"). CONFIRMED (byte check).
71. T2:24 — this entry's departures inert — PB:18; R:216–227. CONFIRMED.
72. T2:11–12 and T2:25–26 — the values-check pointers to the ADDENDUM-n3 entry — NOT CHECKABLE until T1:73's placeholder is filled. Consistent with T1.
73. T2:28 — ab72d0f's close: the coordinating session's, item 7 on this entry — PB:17–18; R:314. CONFIRMED.
74. T2:28–31 — item 7 quoted from "the departures of" to "accepted." — PB:18. CONFIRMED (byte check).
75. T2:31–32 — §3.3 is the reward_f020 batch this entry's reading kept — A3:38; R:326–331. CONFIRMED.
76. T2:32–33 — the push this entry put to the PI was made on "Push now" (push #12) — R:364; PR2:26 (ecf349d..HEAD, 15 commits then); PR12:1, :31 (19 commits, ab72d0f among them). CONFIRMED.
77. T2:33–34 — its C.5 line is in the ADDENDUM-n3 entry at the Log's head — T1:55–62. CONFIRMED against T1 (place: observation 5).

T3, the routing raw's head
78. T3:1 — the title: the PI's routing of 2026-11-19 (third sitting), verbatim, the PI → the coordinating session — PB:1; PR2:1's committed form. CONFIRMED.
79. T3:3 — saved verbatim by the coordinating session on receipt, given in chat on PI date 2026-11-19 — PB:1 for the date. The act is NOT CHECKABLE.
80. T3:3 — the last line, "PI: Route as given", is the PI's own line after the block — PB:23; RR:28; PR2:3 records the same reading. CONFIRMED.
81. T3:3 — committed with ADDENDUM-n3 v0.1, whose entry quotes its items 1, 4, 7 and 8 — T1:19, :21, :23 (whole); T1:46–47 (item 4, in part). CONFIRMED.
82. T3:3 — the 23 lines between the fences are byte-identical to the saved copy, sha256 084df899… — RR:5 and :29 are the fences; RR:6–28 hash equal to PB; PB has 23 lines; T3 equals RR:1–3 (cmp). CONFIRMED.

T4, the referent-check raw's header and grading
83. T4:1 — the title: the referent check of §8.4 and Code's grading, PI date 2026-11-19 — A3:79, :81; PB:1. CONFIRMED.
84. T4:3 — Code's raw for "ADDENDUM-n3 v0.1 — COMMITTED" — T1:1. CONFIRMED.
85. T4:3–4 — §8.3 (1), "referent check of 8.4; an unresolved substantive item → STOP" — A3:79. CONFIRMED (byte check).
86. T4:4–6 — one fresh blind checker, a subagent of the coordinating session; its scope; every referent read at bc50244 — RB:1, :10, :17; RC:6–7. CONFIRMED.
87. T4:6–7 — the brief, 3195496f…b05a, 52 lines, given with its sha256 to verify — shasum and wc -l of RB; RC:4 ("Matches."). CONFIRMED.
88. T4:8 — quoted the list of record v2's items 1–5 verbatim — RB:31–35 equal LR:18–22 (diff, nothing printed). CONFIRMED.
89. T4:9–10 — "a git command in a check takes item 3's pathspec" and "a glob is expanded and read before it is looped over" — RB:38, :39. IMPRECISE (minor): both lines open "A …" in RB. Each quote lower-cases the first letter; the words are unchanged. The first quote also stops at "pathspec", and T4:11 carries the rest.
   Fix: "A git command in a check takes item 3's pathspec" and "A glob is expanded and read before it is looped over".
90. T4:11 — required the m[f]3 exclusion and barred anything under data/ — RB:38, :40. CONFIRMED.
91. T4:12 — no interpreter but shasum — RB:41. CONFIRMED.
92. T4:14–15 — the report reproduced whole in §1, 238 lines, sha256 30060f60…15c3 — RCR:20–257 hash equal to RC; wc -l of RC is 238. CONFIRMED.
93. T4:14 — "extracted verbatim from the subagent's hand-back by `jq`" — NOT CHECKABLE: the coordinating session's act (observation 1).
94. T4:15 — "It held no local path." — RC: 0 for each fragment counted at item 61. CONFIRMED.
95. T4:18 — the omission marker. T4:1–17 equal RCR:1–17, and T4:19–53 equal RCR:260–294 (diff). RCR:18–259 are a blank line, the text fence and RC. CONFIRMED: T4 abridges RCR faithfully.
96. T4:21–22 — the totals — RC:201–206, :208–223. CONFIRMED.
97. T4:24–25 — the two substantive items graded resolved by the third sitting's routing; no STOP — the routing holds item 1's [adopt] (PB:8) and item 4 (PB:11). CONFIRMED as Code's grading.
98. T4:26 — listing 78 is §3.6 and §8.2 (2), the declined branch — RC:123. CONFIRMED.
99. T4:26–27 — "the batch's result is recorded and used by nothing"; "as n §5 texts it" — A3:77. CONFIRMED (byte checks).
100. T4:27–28 — "The second sitting's offer (`f4b3e73` §2.5, and item 2 of its routing raw) struck the batch" — S2:53; S2:89; PR2:14. IMPRECISE (minor), as at 35.
   Fix: "The second sitting's offered alternative (…) struck the batch".
101. T4:28–29 — A-n1 §5.3 decides at f = 0.10 when the cap binds — A-n1:48. CONFIRMED.
102. T4:29–30 — item 1 adopts (n-5) ("[adopt]"); the checker's words "The adopted branch is unaffected." — PB:8; RC:127. CONFIRMED (byte check).
103. T4:30–31 — recorded for the seat: the declined branch needs the checker's fix before it could be chosen — RC:128. CONFIRMED.
104. T4:32 — listing 111's quote of §8.2 (4) — A3:77. CONFIRMED (byte check).
105. T4:33 — some rulings in §1.2, §2.2–§2.3, §4 and §7 are first made in this document, after the second sitting's routing — RC:173–177. CONFIRMED.
106. T4:34–37 — item 4 quoted whole — PB:11. CONFIRMED (byte check).
107. T4:37–38 — item 1's "§1, §2, §4, §6, §7 as the seat's rulings already routed [as ruled]" — PB:8. CONFIRMED (byte check).
108. T4:38–39 — the content unaffected; the routing account recorded with the checker's fix — RC:179–180. CONFIRMED.
109. T4:41 — listing 122's anchor, quoted — A3:81. CONFIRMED (byte check; backticks dropped).
110. T4:42 — at bc50244 those lines hold the convention of record's text — RC:195. CONFIRMED as the checker read it; directions.py was not read here.
111. T4:42–43 — BK's sentence stood at :11 until 616e940 reworded the readings — RC:196; R:257–258. CONFIRMED.
112. T4:43 — §0.1's quotation correct (listing 14); nothing ruled rests on the anchor — RC:49, :198. CONFIRMED (observation 7).
113. T4:45 — listing 8's quote, "G-VEC's re-run of record under §1 has run on the box as the PI reports it" — A3:4. CONFIRMED (byte check).
114. T4:45–46 — no entry at bc50244 records it — RC:41. CONFIRMED.
115. T4:46 — n-build's run entry, committed at e3b48ed, records it: PASS at index 32 — R:24; PB:9 ("n-build's run entry"); e3b48ed's subject. CONFIRMED.
116. T4:46 — "while the check ran" — NOT CHECKABLE: the check's run time is in no source. Consistent with RC:6 (HEAD bc50244 at the check) and e3b48ed being HEAD now.
117. T4:48 — the six minor items (27, 30, 38, 73, 86, 113) and the seven observations, recorded and unapplied — RC:203, :208–223. CONFIRMED.
118. T4:49–50 — observations 3 and 4 as described — RC:216, :217. CONFIRMED.
119. T4:50–51 — sent to n-analyzer and n-build as information, "each to declare a reading for the seat if its work must choose one" — NOT CHECKABLE: (c5) holds "as information" only.
120. T4:53 — the checker's departures are in its report's DEPARTURES — RC:225–238. CONFIRMED.

TOTALS (120 items)
- CONFIRMED: 99
- IMPRECISE: 8 (11, 21, 35, 39, 41, 58, 89, 100)
- FAIL: 0
- NOT CHECKABLE: 13 (8, 14, 24, 26, 45, 47, 48, 61, 72, 79, 93, 116, 119)

OBSERVATIONS
1. An undeclared departure of the class n-build declares.
   - T4:14 says the coordinating session extracted the checker's report "by `jq`", but T1:63–66 lists only the push-#12 jq.
   - n-build declares this class every time: "two `jq` reads of subagents' task outputs" at R:125–126 (e3b48ed), R:217–218 (bc50244) and R:287–288 (616e940).
   - Item 7 (PB:18) rules those entries' departures inert, which treats the class as a departure.
   - The extraction belongs in T1's list, and so does this check's own extraction if it is made the same way.
2. e3b48ed is not named in T1.
   - Two things rest on it: T1:9's dependency (item 11) and the disposition of the check's NOT CHECKABLE listing 8 (T4:45–46).
   - T1's referent-check bullet carries the substantive items, the FAIL, and the minor items and observations, but not the NOT CHECKABLE item.
3. T1:50 and T4 disagree on who may be regraded. T1:50 says "The seat may regrade any of the three"; T4:25 (RCR:266) says "either" of the two substantive items and gives the FAIL no regrade line. Align one to the other.
4. T1:3–4's heading lists item 1's (n-5) [adopt] and (n-6) [confirmed], but not its third bracket, "§1, §2, §4, §6, §7 as the seat's rulings already routed [as ruled]" (PB:8). T4:37–38's resolution of listing 111 rests on that bracket, and T1:46–47 cites item 4 alone.
5. The C.5 line's place changed without saying so.
   - ab72d0f said the push's C.5 line "goes in the coordinating session's close line after it" (R:364–365), and PR12:32 heads it "(for the next close line)".
   - At 7a54eb9, push #8's C.5 line sat in a close line.
   - Here T1:55–62 carries it in the entry and T2:33–34 points there. The change of place is not stated.
6. Exit statuses and item 4's halt clause.
   - "gitleaks exit=1" (GLR:4; PR12:16) and "gl5 exit=1" (GL5:7; PR12:23) appear nowhere in T1.
   - T1:58's "no halt" rests on PR12:29 "No halts." and on gl5's digest classes (GL5:2–6).
   - Item 4 (LR:21) pairs an inside match's count with "a halt for the seat". T1:65–66 cites only the count.
   - No source here states what gl5's exit status means. If it is gl5's READ signal (MANIFEST.json's three hex64-other findings), the entry could say so.
7. "Correct" is checked against referents, not BK. T1:49 and T4:43 call §0.1's quotation of BK's sentence "correct". Listing 14 (RC:49) checked it against S2:16 and f4b3e73's directions.py:11, and says "BK's PDF was not read".

DEPARTURES
- Text tools, none an interpreter by my reading, listed for the seat to class:
  - `cat -n`;
  - `sed -n` line ranges, plus `sed` substitutions to strip a quote's "> " prefix and to collapse spaces when joining wrapped lines;
  - `head -n`; `tail -c` with `od -c` (the last bytes of T1, T4 and RCR);
  - `wc -l` on the brief, the texts, the scratch sources and the push-#12 files;
  - `cut`, `tr`, `printf`, `cmp`;
  - `diff` with process substitution (no file written);
  - `grep -n` and `grep -c -F` (the Bash tool's grep and /usr/bin/grep), on named files only, under `export LC_ALL=C`.
- Reads beyond the named sources:
  - RESULTS.md's head (:1–12) and its 20 newest entry-start lines, to find the four entries;
  - in S2 beyond §2.5 and §8: a `grep -n '2\.5'` that printed :8, :9, :63, :71, :89 and :94 cut to 160 characters, a heading grep, and :55 (§2.6) inside a printed range;
  - in A-n1 beyond §5.3: a `grep -n '5\.3'` that printed :70 and :76 cut to 140 characters;
  - LR:18–22, which the brief names in its RULES, compared with RB:31–35 by `diff`, nothing printed;
  - one `git log --format='%h %s'` on A-n1's path.
- git:
  - `git rev-parse HEAD` and `git rev-parse HEAD:RESULTS.md`, compared with `git hash-object RESULTS.md`;
  - `git log --no-walk --format='%h %ci%n  %s'` on five named commits, cut to 400 characters (ids, commit times and subjects, without a pathspec, as item 1 allows over any path);
  - `git show --name-status` of 7a54eb9 with `-- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/m[f]3/**' ':!data/**'`, and a `--format` printing the author name, the commit time and the message in place of the default header;
  - `git log --format=%h ecf349d..bc50244`, counted by `wc -l`.
- Name-only `ls` of the scratch folders route19c, push12 and push12/final. gl.json and gl12.json were listed by name and not opened. Also a name-only `ls` of five named repository paths, two of them absent.
- One zsh error: an unquoted `echo ====` after a `wc -l` was read as an `=` command and ended that call; I re-ran it with the separator quoted.
- shasum, used by name as the brief allows.
- Nothing under data/ was listed, read or hashed. No guard marker reached any argv. No writes, no network.
```
