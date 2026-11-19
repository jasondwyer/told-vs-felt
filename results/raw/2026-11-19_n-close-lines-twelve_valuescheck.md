# n — four close lines on the answers of 2026-11-19: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafts of n-build's four close lines, each closing a
RESULTS.md entry on the seat's answers committed at `a33252a`, and over where they are placed:
- T1, the line on `89a55c3`'s entry (G-CAL-n's BUILD), with its dated note: `451a210e…011f` (18 lines);
- T2, on `d7d5e5b`'s (the supplement to the eleven starred readings): `aafc7521…c376` (13 lines);
- T3, on `99196e1`'s (the eleven starred readings): `4eba1d2b…79ac` (12 lines);
- T4, on `003ae7d`'s (the schema follow-up): `99aec656…6a72` (10 lines);
- the placement: HEAD's RESULTS.md with each block after the last non-blank line of its entry, `c17bacc6…140c`.

**The checker's brief** (`6dcd6ac2…265e`, 63 lines, given to the checker as a file, with its sha256 to verify):
- named the texts and the sources: in the repository at `a33252a`, the seat's answers raw, RESULTS.md's four entries,
  G-CAL-n's BUILD values-check raw and the brief it names, the driver, `a33252a`'s message, and
  PROPOSAL-n-bk-reconciliation-v0_2.md and CLAUDE.md where a line cites them;
- asked for every factual claim to be checked: each quotation, citation, hash and hash abbreviation, and each
  statement of what the seat ruled and of what the code does, with Code's plans NOT CHECKABLE unless the raw states
  them; and for the placement to be checked by `git diff --no-index -U0` against RESULTS.md clean at HEAD;
- allowed `shasum` by name (on this machine a Perl script, which the list of record's item 1 permits), and barred any
  other interpreter, any write, any network, any guard marker in an argv (a grep pattern included), anything under
  `data/mf3`, any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the named
  files and the brief itself;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, with `.` as the include for `git ls-files`, that a glob is expanded and read before it is
  looped over, and the `rev-parse` form for a tracked-and-clean check.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (138 lines, sha256
`ac7ea5c0…1539`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 70 items: 59 CONFIRMED, 2 IMPRECISE, 0 FAIL, 9 NOT CHECKABLE; and 12 observations.

**The checker's departures,** as its report states them, are in the close line on `89a55c3`'s entry, for the seat to
class.

## 1. Dispositions

- **The IMPRECISE items:**
  - 16 (T1's departures line), applied in the checker's words, with observation 2's citation of §6's heading: every
    departure the entry declared, each class named.
  - 49 (T3's cap of 80), applied with the coordinating session's relay of the routing, which the checker did not have
    and which keeps the PI's option open: "The PI may still name a cap from BK's Appendix E; I've asked." The line
    quotes it as the relay's, and the build checks the quotation against the relay line as extracted.
- **The NOT CHECKABLE items** stand: 3, 27, 40 and 56 are this session's reads in full; 13, 15 and 64 are its plans;
  46 is Code's call on G-VEC's figure, now marked as Code's call (observation 6); 18 is the coordinating session's two
  low items, as relayed.
- **The observations:**
  - 1, applied: T1's owed wording now names the driver's `gcal` docstring and the BUILD values-check's observation 3.
    G-CAL-n's delta, in its draft, carries both.
  - 2, applied in item 16.
  - 3, applied: T2–T4 each gain "**Departures:** this entry's are inert, no strike (§6)."
  - 4, applied in the checker's words.
  - 5, applied: "n §0.7's departure".
  - 6, applied: "Code's call (§8 item 1: "if cheap, else as built"): …".
  - 7 stands: whether the PI's "Route as given" confirmed A2's extension is the coordinating session's item 7 (§8),
    and n-build's lines state nothing on it. T1 says so.
  - 8, applied: F5's "before the canonical run"; and T4's plan now says that the runner's tile, F5's assertions and
    R13's texts land in one commit, with n-analyzer's fixtures and schema pin following it.
  - 9, applied: T4 quotes §2's "stand as committed, under the package they were written with", under R10.
  - 10, applied: T2's heading names the six notes.
  - 11 and 12 ask for nothing.
- **Added after the check, beyond the dispositions:** the values-check paragraph in T1 and a pointer to it in T2–T4;
  T1's line on this session's two `jq` reads of its transcript.

## 2. The text changed after the check, and the edits checked by tool

- **The edits, checked by tool:** a fixed-string count over each block unwrapped, for each disposition's new wording
  and each removed wording's absence: 24 of 24.
- **The quotations,** checked by the build against their sources (the answers raw with bold dropped, the BUILD
  values-check raw, `a33252a`'s message, and the relay line), each also present in the blocks unwrapped: 21 of 21.
  Each line is at most 120 characters, a link line excepted.
- **The placement,** rebuilt from HEAD by fixed anchors: each block after its entry's last non-blank line (lines 142,
  184, 233 and 738 of HEAD's file); the new file is HEAD's with exactly the blocks' 85 lines added.
- **The finals:** T1 `a7419700…7e55` (40 lines), T2 `9262f8b6…8cca` (16), T3 `54b43222…699c` (15), T4
  `4fc27b3a…c054` (14); RESULTS.md `e155f3a7…5c19` (31,761 lines, +85).

## 3. The report as returned

VALUES-CHECK: four close lines (T1–T4) and where they are placed, checked against the seat's answers raw and the repository at a33252a

Preliminaries. The brief's sha256 matched (6dcd6ac2…265e). These all matched their stated sha256s: T1 S/step4b/close12/c_89a55c3.md 451a210e…011f (18 lines), T2 S/step4b/close12/c_d7d5e5b.md aafc7521…c376 (13), T3 S/step4b/close12/c_99196e1.md 4eba1d2b…79ac (12), T4 S/step4b/close12/c_003ae7d.md 99aec656…6a72 (10) and S/step4b/close12/RESULTS_new.md c17bacc6…140c. HEAD is a33252a. Each source was checked tracked and clean (rev-parse HEAD:<path> = hash-object): the answers raw, RESULTS.md, the values-check raw, scripts/n_sessions.py, PROPOSAL-n-bk-reconciliation-v0_2.md and CLAUDE.md. Every hash abbreviation was cut by tool (first 8 … last 4). Each quotation was found by fixed-string grep in its source (only bold markup removed) and in its T file with lines unwrapped.
Short names: A = results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md; VC = results/raw/2026-11-19_n-gcal-build_valuescheck.md; NS = scripts/n_sessions.py; R = RESULTS.md at HEAD.

ITEMS

T1 (S/step4b/close12/c_89a55c3.md)
1. T1:1, "PI date 2026-11-19, first sitting". CONFIRMED. A:3 "Design seat, PI date 2026-11-19 (first sitting)".
2. T1:1, "the seat's answers on the twelve starred readings". CONFIRMED. A:1 "n: the twelve starred readings ruled".
3. T1:1–4, "This session read the seat's raw … in full". NOT CHECKABLE: no source records the read.
4. T1:3, the link target. CONFIRMED. The file is tracked and clean at HEAD.
5. T1:4, sha256 `e6ff066d…6d5a`. CONFIRMED. shasum of A, cut 1–8 and 61–64.
6. T1:4, "The coordinating session committed it by path at `a33252a`". CONFIRMED. `git show --name-status a33252a` (with the pathspecs) shows one path, "A results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md". The message says "committed by path (the paste block's item 7)". A:88–89 puts item 7 ("This raw committed by path") under "C. Coordinating session".
7. T1:4–5, on the PI's "Route as given". CONFIRMED. a33252a's message: 'on the PI's "Route as given"'.
8. T1:5–6, n-build's item 4 and its quotation. CONFIRMED. A:82, verbatim; the item sits under A:78 "N. n-build (and the pod session on the box)".
9. T1:7, "G-CAL-n runs after three changes to the build, each small, in one delta before its launch files" (§0). CONFIRMED. A:8, verbatim apart from the bold on its first clause.
10. T1:8, "the whole turn steered (Q9, §1.9)". CONFIRMED. A:8 (i); A:32.
11. T1:8–9, "the baseline generated second, with a STOP and no −ρ turn at a +ρ fail (Q12 (d), §1.12)". CONFIRMED. A:8 (ii); A:38.
12. T1:9, "a baseline below 36 of 48 coherent a PAUSE (O7, §5)". CONFIRMED. A:63; A:8 (iii).
13. T1:9–10, "The delta is n-build's next code change". NOT CHECKABLE: this is Code's plan. A:80 gives the delta to n-build but says nothing about "next".
14. T1:10, "self-tested, one blind review on the delta, committed" (§8 item 2). CONFIRMED. A:80, verbatim.
15. T1:10–11, "The wording owed at each file's next change rides with it." NOT CHECKABLE: this is a plan (see observation 1).
16. T1:12, "Departures: (1)–(9) from the readings' words, and the BUILD's failed first commit window, are inert". IMPRECISE.
    - Both clauses are in A:68 ("G-VEC's and G-CAL-n's departures (1)–(9) from the readings' words as declared; the BUILD's failed first commit window … Inert"), and (1)–(9) are G-CAL-n's (R:84–94).
    - As the entry's departures line, though, it leaves out four of the six classes the entry put to the seat (R:113–126): Code's `ls data/*`, the reviewer's three, the survey's three and the values-checker's `cmp` loop. §6's heading ("Departures: inert, no strike", A:66) and A:12 ("Departures inert (§6)") rule those too.
    - Instead: "**Departures:** inert, no strike (§6), all that the entry declared: (1)–(9) from the readings' words; Code's `ls data/*`; the reviewer's, the survey's and the values-checker's; and the BUILD's failed first commit window. "Code's wording owed at each file's next change is accepted as declared" (§6)."
17. T1:12–13, "Code's wording owed at each file's next change is accepted as declared" (§6). CONFIRMED. A:68, verbatim.
18. T1:14, "on the coordinating session's two low items". NOT CHECKABLE: no source holds the two items.
19. T1:15, VC's verbatim report gives "a2763e8b…abfa". CONFIRMED.
    - The string is at VC:67, inside §3 "The report as returned" (VC:62–64).
    - VC:28 says that report was "extracted verbatim from the subagent's hand-back by `jq`".
    - VC's blob is the same at 89a55c3 and HEAD (490266e9…5e36, compared in the shell).
20. T1:15, "the checker's own slip". CONFIRMED, resting on VC:28; the hand-back itself is not among my sources. S/step4b/gcal/build/vc_brief.md hashes to a2763e8b…bafa: its tail is "bafa", and no reading of the hash gives "abfa".
21. T1:16, "The brief is `a2763e8b…bafa`, as the raw's head says". CONFIRMED. VC:11 "**The checker's brief** (`a2763e8b…bafa`, 103 lines, …)", and the computed sha256 agrees.
22. T1:16, "the verbatim text stands". CONFIRMED. VC:67 is unchanged at HEAD. This follows the precedent at R:212–213 (a hash tail inside a verbatim report "stays as returned").
23. T1:17, "`gcal-decode` also prints each differing turn's two decoded texts, beside the flags this entry names." CONFIRMED.
    - NS:2912–2914 records a turn as a difference when the laptop's decode differs from the box's, keeping both decodes and both flag sets.
    - NS:2945–2948 prints each as "difference {batch} {index}: box {…} | laptop {…} | flags box {…} laptop {…}", the texts JSON-quoted.
    - The entry names "each difference with its flags under both decodes" (R:78–79).
24. T1:17–18, "Its raw goes under `results/raw/` with the stage's entry (§5, GC1)." CONFIRMED. A:61.

T2 (S/step4b/close12/c_d7d5e5b.md)
25. T2:1, "n-build's: the seat's answers on Q12". CONFIRMED. A:3 lists the n-build session's blocks, d7d5e5b's among them; A:38; R:144–146.
26. T2:2–3, the link, the sha256, `a33252a` and "Route as given". CONFIRMED, as items 4–7.
27. T2:3, "read in full". NOT CHECKABLE.
28. T2:3–4, "rules Q12 in its §1.12: "(a)–(c) stand as built; (d) is amended"". CONFIRMED. A:38, the bold heading, verbatim.
29. T2:5, "the generation order is +ρ, the baseline, +ρ/2, −ρ". CONFIRMED. A:38, verbatim (bold in the source); the characters match by fixed-string grep.
30. T2:5–6, "a coherence or arrival fail at +ρ ends the run as a STOP (exit 2) with the record, the turns and the dose map written and no −ρ turn generated". CONFIRMED. A:38, verbatim.
31. T2:6–8, the fallback and "the seat prefers the change made". CONFIRMED. A:38: "If Code finds the early STOP larger than the order line and the status logic, the fallback is the order alone with the early STOP declared not built — the seat prefers the change made."
32. T2:9–10, the failed-run folder quotation. CONFIRMED. A:38, verbatim.
33. T2:11, "O5 and O6 are settled at the read, without a code change (§1.11)". CONFIRMED. A:36 ("Two notes from the review, settled without a code change: (O5) … (O6) …"); A:8 ("settled at the read, not in the code").
34. T2:11–12, "O7 is a PAUSE and O8 is accepted (§5)". CONFIRMED. A:63.
35. T2:12, "O12's raw goes under `results/raw/` with the stage's entry (§5, GC1)". CONFIRMED. A:61: "`gcal-decode`'s raw, which prints differing turns' text (O12), goes under `results/raw/` with the stage's entry." For the wording, see observation 4.
36. T2:12–13, "O3 asks for nothing now: G1 stands (§1.1)". CONFIRMED. A:16 keeps the capture convention ("the PCA centred"). d7d5e5b's commit subject gives O3 as "G1's uncentred alternative moves the valence row to the ALT file, which G-CAL-n's reader does not read, so G-CAL-n refuses until it is changed". With G1 standing, O3 has nothing to ask.
37. T2:11–13, the notes are the supplement's six. CONFIRMED. R:159–160 lists them (§2: O3, O5, O6; §3: O7, O8, O12), and T2 answers each.

T3 (S/step4b/close12/c_99196e1.md)
38. T3:1, "the seat's answers on the eleven". CONFIRMED. A:3 (99196e1's block); A:16–36.
39. T3:2–3, the link, the sha256, `a33252a` and "Route as given". CONFIRMED.
40. T3:3, "read in full". NOT CHECKABLE.
41. T3:3–4, "rules Q1–Q11 in its §1.1–§1.11". CONFIRMED. A:16–36.
42. T3:5, "G-VEC's four stand as built (Q1–Q4)". CONFIRMED. A:1; A:7 ("Q1–Q4: G1, G3, G6 and G9 stand"); A:79.
43. T3:5, "G-VEC runs as built" (§0). CONFIRMED. A:7.
44. T3:5–6, "§1.1 asked for one more figure in a STOP's record, R over positions 1..n at both indices". CONFIRMED. A:16.
45. T3:6–7, "if the change is cheap before the launch files; if it is not, G-VEC runs as built and that figure comes from the re-run". CONFIRMED. A:16, verbatim.
46. T3:7–8, "The launch files were already checked and frozen, so G-VEC runs as built." NOT CHECKABLE. No source states what state the launch files are in, though R:141 ("its launch files held") is consistent. The conclusion is Code's call under A:16 and A:79 ("if cheap, else as built"); see observation 6.
47. T3:9, "G-CAL-n's seven" are Q5–Q11. CONFIRMED. R:187 lists GC3, GC4, GC5, GC6, GC8, GC11 and GC12; A:24–36 map them to Q5–Q11 in that order.
48. T3:9, "the cap of 80 (Q5 … §1.5)". CONFIRMED. A:24.
49. T3:9, "the PI may still name one from BK's Appendix E". IMPRECISE.
    - A:24 leaves it to the routing: "the PI says so at routing and the one constant follows".
    - The routing has happened (a33252a: "Route as given"). A:74 ("defaults in brackets") and A:81 ("[as ruled; or a cap from BK's Appendix E if your copy names one: ___]") make "as ruled" the answer that was routed.
    - No source keeps the option open. If a PI word relayed to you does, cite that instead.
    - Instead: "the cap of 80 (Q5, §1.5: a cap from BK's Appendix E was the PI's to name at routing, and "Route as given" took §8 item 3's default, as ruled)".
50. T3:9–10, TEMP 0.7 (Q6), the 48 prompts (Q7), the coherence heuristic (Q10) and the arrival's form (Q11) stand. CONFIRMED. A:26, A:28, A:34, A:36; A:8 ("Q5–Q8, Q10, Q11 … stand as built").
51. T3:10–11, "§0.7's departure reaches G-CAL-n's generations (Q8, §1.8)". CONFIRMED. A:30, heading verbatim. The section cited is PROPOSAL-n-bk-reconciliation-v0_2.md:34 ("0.7 Rule 13, departed from by declaration"). For the wording, see observation 5.
52. T3:11, "The whole turn is steered (Q9, §1.9), the one change among the seven". CONFIRMED. A:32. A:8 gives the three changes as Q9, Q12 (d) and O7, with Q5–Q8, Q10 and Q11 standing.
53. T3:12, the carried items: "GC1, GC2 and GC14 are cleared from LOCK-n v0.1's list (§5)". CONFIRMED. A:59–63 ("LOCK-n v0.1's list, cleared now": GC1, GC2, GC14); A:12; R:202–203 ("carried: GC1 and GC2 on LOCK-n v0.1's list, GC14 a PAUSE").

T4 (S/step4b/close12/c_003ae7d.md)
54. T4:1, "the seat's answers on R10–R14, F5 and F7". CONFIRMED. A:47; R:650–675.
55. T4:2–4, the link, the sha256, `a33252a` and "Route as given". CONFIRMED.
56. T4:4, "read in full". NOT CHECKABLE.
57. T4:4, "rules them in its §3". CONFIRMED. A:47–51.
58. T4:5, "R10, R11, R13, R14 and F7 are accepted". CONFIRMED. A:49–50.
59. T4:5, "R13's two runner texts are corrected at the runner's next change". CONFIRMED. A:50 ("the two runner texts corrected at its next change"). R:665–668 names the two texts: the docstring's "a trial, and an exceedance" and the resume check's name.
60. T4:6–7, F5 ("after the lock `p0_count` is at least 1 and `p0_n` at least 3, "asserted in the schema", and n-analyzer moves its fixtures in its own commit"). CONFIRMED. A:50, which also says "by Laplace's rule" and "before the canonical run" (see observation 8).
61. T4:8, "the window is the tile". CONFIRMED. A:51 (bold heading); A:11.
62. T4:8, "a runner change, self-tested and reviewed on the delta, before G-TIME-n". CONFIRMED. A:51.
63. T4:8–10, "it moves the package digest, so it lands after G-CAL-n's run or in G-CAL-n's own delta, Code's call by the launch order". CONFIRMED. A:51, verbatim.
64. T4:10, "Code's call: after G-CAL-n's run, with F5's assertions and R13's two texts." NOT CHECKABLE: this is Code's plan.

P (placement, S/step4b/close12/RESULTS_new.md)
65. The five scratch files' sha256s, and the T files' line counts, are as the brief states. CONFIRMED. shasum; wc -l gives 18, 13, 12 and 10.
66. RESULTS.md is tracked and clean at HEAD. CONFIRMED. rev-parse HEAD:RESULTS.md = hash-object (42695d56…7416).
67. The diff adds four blocks and deletes nothing. CONFIRMED. `git diff --no-index -U0` shows @@ -142,0 +143,18 @@, @@ -184,0 +203,13 @@, @@ -233,0 +265,12 @@ and @@ -738,0 +782,10 @@: 53 lines added.
68. Each block is its T file, byte for byte. CONFIRMED. The sha256s of RESULTS_new.md's lines 143–160, 203–215, 265–276 and 782–791 equal those of T1, T2, T3 and T4.
69. Nothing else changes. CONFIRMED. With those four ranges deleted, RESULTS_new.md hashes to 58292216…b862, the sha256 of HEAD's RESULTS.md.
70. Each block sits at the end of its own entry. CONFIRMED.
    - `git blame -s` attributes R:24–143 to 89a55c3 (120 lines), R:144–185 to d7d5e5b (42), R:186–234 to 99196e1 (49) and R:546–738 to 003ae7d (193).
    - The insertion points R:142, 184, 233 and 738 are each entry's last non-blank line. At HEAD the first three are followed by a blank line and the next entry; R:738 is followed directly by 9f64305's entry at R:739, with no blank line there at HEAD either.
    - In RESULTS_new.md, lines 161, 216 and 277 are blank, and line 792 starts 9f64305's entry.

TOTALS: 70 items: 59 CONFIRMED, 2 IMPRECISE (16, 49), 0 FAIL, 9 NOT CHECKABLE (3, 13, 15, 18, 27, 40, 46, 56, 64).

OBSERVATIONS
1. T1:10–11 ("rides with it"): the driver's `gcal` docstring gives exit 3 as "a PAUSE (at +rho/2 alone)" (NS:166). O7's baseline PAUSE makes that incomplete, so the delta has to touch the driver as well.
   - The driver's owed wording would then ride with the delta (R:97–98: "GC1-GC22" at NS:155, and the refusals at NS:156–157, which leave out the failed-run folder).
   - So would the values-check's observation 3, which R:107 defers to "the driver's next change" and which T1 does not mention.
   - Suggested: "The wording owed at each file's next change rides with it, the driver's included (its `gcal` docstring names a PAUSE at +ρ/2 alone), with the values-check's observation 3."
2. §6 rules by its heading ("Departures: inert, no strike", A:66; A:12), but its clauses do not name several of the declared departures one by one:
   - 89a55c3's entry: the reviewer's reads (R:117–120); the survey's grep with a guard marker in its pattern, and its `git grep` with `'*.py'` as the include (R:122–123).
   - 99196e1's entry: the checker's `git show` of BK's skeleton files after a `cd` through a glob (R:223–224).
   - 003ae7d's entry: Code's `git log` with `%ad`, its printed `rev-parse` ids and its `git diff --name-only` without exclusions (R:701–706); the reviewer's five `/usr/bin/grep -n` runs and three narrow-include `git grep`s (R:707–709); the checker's `sed`, shell loop, `shasum`/`cat` on absent names and `head`/`tail`/`cut`/`wc`/`tr` (R:711–718).
   - A close line that records these as inert should cite §6's heading, not one of its clauses.
3. T2–T4 have no departures line, though each entry declared departures for the seat to class (R:172–178, R:217–226, R:696–718), and n-build's earlier close lines record the seat's ruling on them (e.g. R:1971–1973). Suggested, in each: "**Departures:** this entry's are inert, no strike (§6)."
4. T2:12: change "O12's raw" to "`gcal-decode`'s raw (O12)", which is A:61's own form.
5. T3:10: change "§0.7's departure" to "n §0.7's departure". Every other § in T3 refers to the answers raw, which has no §0.7; A:30's body itself writes "n §0.7".
6. T3:7–8 is Code's call (A:79: "if cheap, else as built"). Mark it the way T4:10 does, e.g. "Code's call: the launch files were already checked and frozen, so G-VEC runs as built, and the figure comes from any re-run (§1.1)."
7. T3 on Q8: A:30 ends "the PI confirms it at routing, as A2 was confirmed", and A:89's bracket reads "[as ruled; A2's extension confirmed: ___]". T3 does not say whether "Route as given" counts as that confirmation, and G-CAL-n's generations in the rendering of record depend on it. If n-build's line should record it, state it as it was relayed.
8. T4:6–7: add F5's "before the canonical run" (A:50), the seat's ordering for n-analyzer's fixtures commit. Under T4:10's plan, if F5's assertion lands in `valence_core/n/schema.py`, the file's sha256 moves after G-CAL-n's run. n-analyzer's `SCHEMA_SHA256` move (in its own commit, as at 003ae7d: R:572–573, R:680–681) and its fixtures then follow that commit. A clause would put that order on record.
9. T4 could cite A:45, which answers the entry's "reports and cells that no longer pass" (R:640–649): they "stand as committed, under the package they were written with (R10, §3); nothing is re-read under the new schema".
10. T2's heading ("the seat's answers on Q12") is narrower than its body, which also closes the six notes. For example: "on Q12 and the six notes".
11. T1's note covers every slip on VC:67 that can be checked. The line's four text abbreviations agree with VC:6–9; T3's carries an eight-character tail ("609ef824…af20a91f") against VC:8's "609ef824…a91f", which is consistent. The line's other hashes are not in VC's head and were not checked.
12. At HEAD, 003ae7d's entry has no blank line before 9f64305's entry (R:738–739) or after da7bdec's (R:545–546). The placement keeps this, so T4 runs straight into 9f64305's entry (RESULTS_new.md:791–792). This is not a placement defect.

DEPARTURES
- Possibly one class: `git rev-parse <rev>:<path>` output printed rather than only compared in the shell.
  - The tracked-and-clean loop compared in the shell but also printed the six sources' HEAD blob ids.
  - VC's blob ids at 89a55c3 and HEAD were printed in full once and compared by eye; later they were printed abbreviated and compared in the shell. RESULTS.md's HEAD blob id was also printed abbreviated.
  - All of these are non-data files; nothing under data/ was touched. I state this in case item 1's "compared in the shell" applies outside data/*/ckpt and data/*/reports.
- Otherwise none. Not barred, but stated for the record:
  - I read beyond the brief's source list: d7d5e5b's commit subject (`git log -1 --format=%s` with the pathspecs, item 1's form), for O3's text.
  - I read RESULTS.md outside the four entries: heading and entry-start greps, lines 396–399 and 543–546, two earlier n-build close lines at 1326–1345 and 1954–1981, and a grep of close-line heads. I also ran `git blame -s` on RESULTS.md.
  - One grep of PROPOSAL-n-bk-reconciliation-v0_2.md's headings, to find §0.7, printed an output line (not an argv) containing a guard-marker word.
  - I used `wc -l`, `sed`, `tr`, `cut`, `sort`, `uniq` and `basename` on named files and in pipelines.
  - One command line stopped at zsh's `=` expansion of an `echo ===` before its second git command ran; that command ran alone in the next call.
  - No file was written; no interpreter but shasum was run; nothing under data/ was read, listed, sized or timed; nothing in S was listed or globbed.
