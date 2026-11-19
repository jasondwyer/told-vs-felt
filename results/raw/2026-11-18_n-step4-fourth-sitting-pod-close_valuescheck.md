# The pod session's close line on `6e3474d`'s entry (the seat's fourth sitting): blind values-check

*Code's raw (the pod session), PI date 2026-11-18. One blind values-check of the pod session's close line for the fourth sitting, on `6e3474d`'s entry, by a fresh subagent. It was given the draft and the sources its report names, among them the coordinating session's two relays, extracted from the pod session's transcript by tool. It was also given the list of record v2 items 1–5 verbatim, with the additions in force: item 3's pathspec in every git command, with `':!data/mf3/**'` while Q-F3 runs; a glob expanded and read before it is looped over; a listing over a copied ckpt or report pruned or not run; a tracked-and-clean check by `git rev-parse HEAD:<path>` against `git hash-object`. It was told to use no interpreter and to put no marker word in any argv. The draft carried a placeholder for this check's totals, filled after the check. The checker's report follows verbatim. It names this session's scratch folder SESS, as its brief did. Its one match for a local-path string is its own list of search terms, not a path.*

*Totals: 36 items: 28 CONFIRMED, 4 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE; 11 observations. These are the checker's own count, checked by tool against its item list.*

*Applied by the pod session after the check:*
- *The four IMPRECISE items (13, 23, 26 and 33), each in the checker's sense and in the pod session's words.*
- *Observations 1 to 9. Observation 9 is applied in part: the leftovers are named by a pointer to the pod session's resume close line. Observations 10 and 11 ask for nothing.*
- *The four NOT CHECKABLE items stand: the pod session's reads in full, its re-hash, the box's state at the drafting, and this raw.*
- *Every edit was checked by tool: the pod session's check script passes on the final text, 68 checks (sha256 tail 85be8bda…d626).*

*The checker's departures are in its report, for the seat to class.*

---

# Values-check of the pod session's fourth-sitting close line (T1)

## Items
1. [CONFIRMED] T1:1 "PI date 2026-11-18, fourth sitting". Evidence: S1:3, "Design seat, PI date 2026-11-18 (fourth sitting)".
2. [CONFIRMED] T1:1 "the seat's answers on the resume". Evidence: S1:3 says the answers are on n-build's block `2026-11-18_n-step4-resume_code-to-design_STOP.md` (`6e3474d`). S4:87–90 is that entry's STOP.
3. [CONFIRMED] T1:3, the link `results/raw/2026-11-18_n-step4-resume_design-to-code_answers.md`. Evidence: the file exists, and it is one of the two names in c7d0009 (S5).
4. [CONFIRMED] T1:4, sha256 `c265797f…61a5`. Evidence: `shasum -a 256` gives c265797f0f7504a5271bbfb2513e37e3af67c2a76508d29950300d700bd561a5. `cut -c1-8` gives c265797f and `cut -c61-64` gives 61a5. The same tail is at S3:30 and in c7d0009's subject.
5. [CONFIRMED] T1:4, "20,924 bytes". Evidence: `wc -c` gives 20924, and c7d0009's subject says "20,924 B".
6. [CONFIRMED] T1:4–5, "the conditional ruling raw" at `results/raw/2026-11-18_n-step4-bext2-p01_conditional-ruling.md`. Evidence: S1:3 ("Placed with this raw"), S1:27 ("The conditional ruling raw"), and c7d0009's subject. The file exists and is in c7d0009.
7. [CONFIRMED] T1:6, sha256 `ba9f9632…cc32`. Evidence: `shasum -a 256` gives ba9f96322a580d1c6cb5d198fc1750328a6cabfb7a21aa3fba8f2860c5aacc32, and cut gives ba9f9632 / cc32. The full value occurs once in S1, at S1:3 (`grep -c -F` gives 1). The tail is also at S3:23 and in c7d0009's subject.
8. [CONFIRMED] T1:6, "2,857 bytes". Evidence: `wc -c` gives 2857. S1:3 says "2,857 B", and so does c7d0009's subject.
9. [NOT CHECKABLE] T1:2,6, "This session read … in full". This is something the pod session did, and none of the given sources records what it read.
10. [CONFIRMED] T1:6, "The coordinating session committed both by path at `c7d0009`". Evidence: S5's `git show --name-only` with the four-part pathspec lists exactly these two paths. Its subject says "committed by path (the paste block's item 7)" and "The coordinating session's notes and close line follow in their own commit". Item 7 sits under "C. Coordinating session" (S1:78–80). See also S3:12.
11. [CONFIRMED] T1:7, each raw is equal to its committed blob at c7d0009. Evidence: `git rev-parse c7d0009:<path>` equals `git hash-object <path>` for both files, compared in the shell (EQUAL, EQUAL).
12. [NOT CHECKABLE] T1:7, that this session did the re-hash. Only the pod session's transcript could show that. c7d0009's subject records only the coordinating session's own re-hash against the paste block.
13. [IMPRECISE] T1:8–9, "This session's share is the box side of the PI's routing items 2 and 5". This is true of the box side, but the share is not complete. Routing item 4, under N, gives this session the close line on `6e3474d`'s entry citing the answers raw (S3:18; S1:75). The relay also lists it under "ALSO RULED, for you": "Close lines: yours goes on 6e3474d's entry, citing the answers raw (c265797f…61a5), in a window from me" (S3:30). T1 is that share but does not say so. Proposed: "**This session's share** is the box side of the PI's routing items 2 and 5, under "N. n-build (and the pod session on the box)", as the coordinating session relayed them, and item 4's close line on `6e3474d`'s entry citing the answers raw, which is this line:"
14. [CONFIRMED] T1:8–9, the quotation "N. n-build (and the pod session on the box)". Evidence: verbatim at S1:71 and S3:14.
15. [CONFIRMED] T1:8, items 2 and 5 sit under N, as the coordinating session relayed them. Evidence: S1:71–76 (N has items 1–5; C has items 6–8 at S1:78–81) and S3:14–19.
16. [CONFIRMED] T1:10, "`backend-ext-2 --convention space` on the box". Evidence: S3:16 and S1:73.
17. [CONFIRMED] T1:10, "from driver v2g's commit". Evidence: S1:25 ("from v2g's commit (§2.3), on n's box in the pod session") and S3:12. The PI's "route as given" (c7d0009's subject) takes item 2's default "go" over "backend-ext-2 from v2f now" (S3:16).
18. [CONFIRMED] T1:10–11, "with its files relayed through the coordinating session". Evidence: S3:12 ("its files come through me after n-build's driver v2g is committed") and S1:25.
19. [CONFIRMED] T1:11–13, the copy. n-build's launch files name it: either `copy-resume4-1272702`, which holds the resumed, COMPLETE first-stage report, or a new copy at v2g's commit with the root and report copied in by plain `cp` and checked by sha256. Evidence: S3:22, point for point; S4:104 ("The stage is COMPLETE"); S4:214.
20. [CONFIRMED] T1:14, "the box stays up until backend-ext-2 is COMPLETE and its report and lines are on the laptop". Evidence: S3:19, verbatim except for capitalization; S1:76; S3:24.
21. [CONFIRMED] T1:14–15, the leftovers are cleaned after that, on the PI's word. Evidence: S3:19 ("cleaned after that, on my word [stays up; cleanup after]"), S1:76, and S3:24 ("comes only after, on the PI's word").
22. [CONFIRMED] T1:17, "The conditional ruling raw goes beside the script". Evidence: S3:23.
23. [IMPRECISE] T1:17–18, "If the stage's end-of-run pause fires, the ruling is applied only if its four conditions hold". This is true as a necessary condition, and it matches how S1:27 puts it. But the ruling's own scope is narrower (S2:7): "exactly one pause: the first pause of stage `backend-ext-2` …, and only if that pause's kind is `fidelity-binomial`, fired at the run's end (`launch_index` null), the stage having launched and obtained all 24 planned reads". T1 names neither the pause's kind nor "first", and "only if … hold" can be misread as sufficient. Proposed: "If the stage's end-of-run fidelity pause fires (the ruling's scope: the stage's first pause, of kind `fidelity-binomial`, at the run's end, with all 24 planned reads obtained), the ruling is applied only if its four conditions hold, each printed with the resume's line; if any fails, the pause waits for the seat with the output and the report, nothing resumed." The last clause is from S2:14.
24. [CONFIRMED] T1:18, four conditions, each printed with the resume's line. Evidence: S2:8–12 lists (i)–(iv), "each printed with the resume as "condition (i): holds" or "fails"". See also S1:27.
25. [CONFIRMED] T1:18–19, "Code checks them mechanically and weighs nothing (rule 21)". Evidence: S2:3 ("Code checks the conditions mechanically, prints each with the resume's line, and weighs nothing") and S1:27 ("weighs nothing (rule 21)").
26. [IMPRECISE] T1:21, "its departures are inert, with no strike (§7)". §7's heading is "Departures: inert, no strike" (S1:55). It names this session's departures as the resume's close line lists them: S1:57's parenthetical matches S4:220–235. It also covers "the values-checkers' as their reports state them", which includes this session's checker's (S4:253–257). But S1's reading list names only "the pod session's close line on it" (S1:3). The Python start disclosed in this session's third-sitting close line (S4:758–761) appears nowhere in S1: "Python" occurs only at S1:57, in "non-Python". Left unscoped, "its departures" reads as all of them. Proposed: "its departures as its close line on this entry lists them, and its values-checker's as that report states them, are inert, with no strike (§7); the answers do not name the Python start disclosed in its third-sitting close line (on `6df2131`'s entry); and one line is added to the list of record v2's reading: "…""
27. [CONFIRMED] T1:21–23, one line added to the list of record v2's reading, and its quotation. Evidence: S1:57 ("One line is added to the list of record v2's reading, for the pod session's transport: …"). A `grep -F` for the whole quoted sentence matches it verbatim at S1:57 and S3:27.
28. [CONFIRMED] T1:24, §6.3. Evidence: S1:51 ("(the address-and-port count over copied files before their commit, counts only, by whichever session relays) is inert and allowed") and S3:28.
29. [CONFIRMED] T1:25–26, §6.4, standing. Evidence: S1:53, a verbatim clause, "accepted and made standing". See also S3:29.
30. [CONFIRMED] T1:20, these three as "Ruled for this session". Evidence: S3:26–29 lists §7, §6.3 and §6.4 under "ALSO RULED, for you". In S1's routing, §6.3 and §6.4 sit in item 6 under "C. Coordinating session" (S1:79). So the attribution to this session is the relay's, and §6.3 itself says "by whichever session relays". The relay's fourth bullet, the close line at S3:30, is covered in item 13.
31. [CONFIRMED] T1:27, pod `emw1e4embiwe9b`. Evidence: S3:4, S2:1, S4:96.
32. [CONFIRMED] T1:27, the PI's word "Keep it up". Evidence: verbatim at S3:2.
33. [IMPRECISE] T1:27, the box "was up on the PI's word "Keep it up" at this line's drafting". The relay limited that word: the box "stays up while the seat rules on the label convention" (S3:4). By the drafting, the seat had ruled, and the box was also up on routing item 5: "The box stays up until backend-ext-2 is COMPLETE … [stays up; cleanup after]" (S3:19; S1:76), with "Hold the box idle until then" (S3:12). T1 cites item 5 at T1:14 but grounds the box's state only on the earlier word. Proposed: "**The box,** pod `emw1e4embiwe9b`, was up at this line's drafting, on the PI's word "Keep it up" while the seat ruled and on routing item 5 since: idle, with everything left as it is, until backend-ext-2's files come."
34. [CONFIRMED] T1:27–28, "idle, with everything left as it is, until backend-ext-2's files come", as the standing hold. Evidence: S3:4 ("Hold it idle with everything left as it is: run nothing, delete nothing, stop nothing") and S3:12 ("its files come through me after n-build's driver v2g is committed. Hold the box idle until then").
35. [NOT CHECKABLE] T1:27–28, the box's actual state at the drafting (up, idle, nothing changed). This is the pod session's own observation. No source records the box's state after the resume's end, when S4:129 recorded it as "idle, with the GPU at 0 MiB".
36. [NOT CHECKABLE] T1:30, the values-check raw `2026-11-18_n-step4-fourth-sitting-pod-close_valuescheck.md`. `[ -e ]` reports it absent, since it will be this check's raw. The name does not collide with anything: the resume close's raw exists under the other name, `2026-11-18_n-step4-resume-pod-close_valuescheck.md`.

## Observations
1. **Give the conditional ruling raw's full sha256.** The third-sitting close gave the ruling raw's sha256 in full, saying "its full sha256 is the pause's `ruling_sha256`" (S4:701–703). This raw's sha256 "can be the pause's ruling_sha256" (S2:3; S1:27; c7d0009's subject), and S1:3 already gives it in full. Suggest: "(sha256 `ba9f96322a580d1c6cb5d198fc1750328a6cabfb7a21aa3fba8f2860c5aacc32`, 2,857 bytes; if it is used, its full sha256 is the pause's `ruling_sha256`)". The full value was computed by tool and equals S1:3.
2. **The re-hash against the relay.** The third-sitting form also compared each file "to the coordinating session's relay" (S4:703–705). The fourth-sitting relay gives both tails (S3:23, S3:30). If this session made that comparison, say so; only the session itself can.
3. **There is no departures bullet.** Both earlier close lines carry "Departures, for the seat to class" (S4:220, S4:741), and T1 says nothing either way. If there were none between the resume's close line and this drafting, add a line saying so, as 6e3474d's entry does ("The pod session's records state no departure of its own", S4:151). If there were any, list them.
4. **The third-sitting close line's departures (with item 26).**
   - The content search over the copied ckpt (S4:752–757) is the class §6.3 now rules inert and allowed ("the copy-back count", S1:51).
   - The two unpruned `find` commands were classed by this session itself under the third sitting's §7 (S4:750–751).
   - The Python start (S4:758–761) is classed nowhere in S1 or RESULTS.md. "Python start" occurs only at S4:758 and :769.
   - One sentence saying which earlier disclosures the fourth sitting classed, and which remain for the seat, would close the loop.
5. **Rulings in §5 that touch this session.** S1:43 accepts "the first attempt's copy-in defect … as declared". That is the attempt this session ran (S4:181–192). It comes "with the standing line "every pre-commit check asserts, in a call of its own"", which binds this session's commits in its windows. Both belong under "Ruled for this session"; the relay did not list them (S3:26–30).
6. **The conditional-ruling paragraph (T1:17–19).**
   - (a) It carries routing item 2's text ("the conditional ruling applied only on its four conditions", S3:16) but sits after item 5. Moving it under item 2 would read more directly. Its indent is the share bullet's, as in the third-sitting form (S4:717), so this is only a clarity point.
   - (b) "the script" is not defined in T1. "The box script in n-build's launch files" would name it.
   - (c) The paragraph could state the file's role: it is the file for `--resume --ruling <pause id>=PATH` (S1:27; S2:3). If no pause fires, it is not used and is "committed with the stage's entry as the record of what would have applied" (S2:15).
   - (d) The ruling's scope names "driver v2f's commit or a later driver whose read path is unchanged" (S2:7). v2g changes "nothing in the read path" (S1:29), so a v2g run is in scope. Since T1 runs from v2g, a clause saying so would help.
7. **The ground for "from driver v2g's commit".** Item 2 offered "[go; or backend-ext-2 from v2f now, the two lines by `--report` later]" (S3:16). The PI's word was "route as given" (c7d0009's subject), which takes "go". n-build's third-sitting close records the PI's word (S4:795–796). One clause in T1 would ground the route.
8. **The first copy option is at v2f's commit.** `copy-resume4-1272702` is a clone "detached at `1272702`" (S4:198–200), which is v2f's commit. A run "from driver v2g's commit" in that copy means the copy is first moved to v2g's commit, which S3:22 leaves to n-build's launch files. A clause saying so would keep the seat from reading the first option as a v2f run.
9. **Optional detail.**
   - The leftovers are named in S3:24 ("v2's failed copy, probe-cp, sync7 and so on"). The resume close lists them in full, including the side ref `refs/bundles/n-site7` (S4:212–219). A pointer there would pin down item 5's cleanup scope.
   - The run also waits on v2g's commit (S3:12). If the "space" render covered only the 40 floor sessions, it also waits on the render of the 160 "before backend-ext-2" (S1:19). "until backend-ext-2's files come" covers both, but only by implication.
10. **Where T1 goes.** The brief says 6e3474d's entry begins "n step 4 — the BACKEND extension's resume". In the working-tree RESULTS.md it begins "- 2026-11-18 — **n step 4 — the BACKEND extension resumed under the seat's ruling on `p01`" (S4:87). The entry runs to S4:258, and its last sub-bullet is the pod session's resume close (S4:173–258). T1 goes after :258. These line numbers are as read and will drift.
11. **Form.**
    - These all match the two earlier close lines: the header, the 2/4/6 indents, the link form, the U+2026 tails (0 lines with "...", 2 with "…"), "bytes" with a thousands separator, "at this line's drafting", and the values-check sub-bullet with its Raw link.
    - The raw's name breaks the earlier pattern of naming after the answers' stage, but it has to: that name, `2026-11-18_n-step4-resume-pod-close_valuescheck.md`, is already taken by the resume close's raw.
    - T1 has 0 matches for "/Users/", "/private/", "/tmp/", "scratchpad" and "/workspace/". "@@VC@@" occurs only at T1:29.

## Departures
These are reads and commands beyond the named sources. None of them breaks a stated rule:
- **RESULTS.md reads beyond S4's named parts:**
  - a `grep -n "^- 2026-11-18"` listing 13 entry headings, each cut at 160 characters;
  - lines 690–696, the end of 6df2131's entry body before its close line;
  - lines 790–819, n-build's third-sitting close and the next entry's first two lines;
  - two whole-file fixed-string searches: "Python start" (lines 758 and 769) and "copy-back count" (no match).
- **Existence tests:** `[ -e ]` on four named paths under results/raw, printing only exists or absent. This goes beyond S5's named forms.
- **Greps on named files:** fixed-string greps of S1, S2, S3 and T1, printing only line numbers or counts. These are allowed utilities on named non-data files; I list them for completeness.

Nothing under data/ was touched, nor any excluded scratch folder or boxconn. No interpreter ran, no guard-marker word was in any argv, and `git status` never ran. The git commands were S5's forms only: `git show --name-only` with the four-part pathspec, and `rev-parse` against `hash-object` compared in the shell.

## Totals
36 items: 28 CONFIRMED, 4 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE; 11 observations.
