# ADDENDUM-n2 v0.1 — COMMITTED: the blind values-check, two passes (PI date 2026-11-18)

Code's raw (the coordinating session) for `ADDENDUM-n2 v0.1 — COMMITTED`. Two fresh blind checkers, subagents of the
coordinating session, checked Code's texts that this commit adds. The addendum had the referent check, and the reports
reproduced in the raws were checked for byte-identity. Each brief:
- quoted the list of record v2's items 1–5, with item 4's amendment by C.2 of 2026-11-16;
- carried the briefs' two lines, "a git command in a check takes item 3's pathspec" and "a glob is expanded and read
  before it is looped over";
- required the `data/mf3` exclusion while Q-F3's campaign runs, and no listing of `results/raw`;
- allowed no interpreter.

Each report is reproduced whole, as its hand-back message gave it, with the harness's two-space indent removed. Each
result is byte-identical to the unindented copy of the report that the session's record also holds. Neither report
held a local path.

The reports name the coordinating session's scratch drafts: RESULTS.new (RESULTS.md with the entry and the close line
inserted), entry2.md, close_25c9340.md, pi-routing-saved.txt, pi-routing-raw.md, refcheck_raw.md, report.txt, and the
previous push's record. Pass 2's report also names edits_after_pass1.md (the coordinating session's list of the edits
after pass 1), vc1/report_vc1.txt (pass 1's report), rc_tail.md, vc_raw.md (this raw's draft), and three files in the
pod session's scratch folder: its extract of a relay, its close line, and that line's values-check raw. Their line
numbers index the drafts each pass read. The committed texts are the drafts after the dispositions below.

## 1. Pass 1: the report, whole

VALUES-CHECK: ADDENDUM-n2 v0.1 — COMMITTED entry, close line on 25c9340's note, PI-routing raw, referent-check raw §2 — 95 items: 76 CONFIRMED, 7 IMPRECISE, 0 FAIL, 12 NOT CHECKABLE; 12 observations.

HEADER

Checkout: HEAD 3b2b855; origin/main (local ref) ad856f0. Every repo file read below has the same blob id as at HEAD (`git rev-parse HEAD:<path>` against `git hash-object`). The addendum is untracked at root.

Labels used below
- A2 = ADDENDUM-n2-fidelity-on-the-box-of-record-v0_1.md
- A-n1 = ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md
- n = PROPOSAL-n-bk-reconciliation-v0_2.md
- S3 = results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md
- S2 = results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md
- RUL = results/raw/2026-11-18_n-step4-p01_ruling.md
- LOR = results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md
- HFV = results/raw/2026-11-18_home-folder-note_valuescheck.md
- DRV = scripts/n_sessions.py
- RUN = results/raw/2026-11-18_n-step4_bext-run3_out.txt
- DIAG = results/raw/2026-11-18_n-step4_bext-diag_out.txt
- NB16 = results/raw/2026-11-16_n-build_design-to-code_answers.md
- Scratch files: NEW = the scratch RESULTS.new; SAVED = the scratch pi-routing-saved.txt; PRAW = the scratch pi-routing-raw.md; RC = the scratch refcheck_raw.md; REP = the scratch report.txt; PUSH = the scratch push record (../push8/push_record8.txt).

What I read
- Scratch:
  - NEW :1–125 and :320–539, and NEW diffed against HEAD's RESULTS.md. The only hunks are NEW :24–109 and :496–530.
  - entry2.md and close_25c9340.md, by diff; each equals its NEW range.
  - PRAW :1–31; SAVED :1–25; RC :1–512; REP by cmp against RC :19–448; PUSH :1–23.
- Repo:
  - In full: A2 :1–50, S3 :1–67, RUL :1–10, S2 :1–76, A-n1 :1–86.
  - n :77, plus fixed-string lookups giving only line numbers (:47, :97, :109, :117, :128, :148, :152).
  - RESULTS.md :2845–2954, :610 and :11510.
  - LOR :16–30 and its headings; CLAUDE.md :333–341.
  - HFV :110 by grep. The precedent raws `2026-11-16_second-sitting_pi-routing.md` :1–5 and `2026-11-16_addendum-n1_referent-check.md` :1–16.
  - DRV by grep for R3 and R5. RUN, DIAG and NB16 by fixed-string lookups only.
- git: `show --name-status` of 3b2b855 and 25c9340; `log` of 6df2131..HEAD and dc6a1cf..ad856f0; D2 :514's count form run over 3b2b855's own diff.

Tools
- The file-read tool.
- diff, cmp, head, tail, cut, wc (`-l`; `-c` on the addendum only), od, fold, tr.
- `shasum -a 256` with cut; /usr/bin/grep on named files and on pipes.
- git: rev-parse, ls-files, ls-tree --name-only, show (named blobs, --name-status, diffs under the pathspec), log --format, rev-list --count, diff --name-only, hash-object (no -w), --version.
- `test -e` on named paths only: three destination names, two precedent raws, .git/index and .git/index.lock.
- zsh built-ins (see DEPARTURES 5).

Not done
- No file written.
- No git add, commit, checkout, reset or stash, and nothing else that changes the index, the tree or a ref.
- Nothing under data/ read, listed, hashed or searched, data/mf3 included.
- No git status of any kind; no listing of results/raw or of any other folder.
- No interpreter, no network, no --stat or --numstat.
- No marker word in any argv; no search outside the repo and the named scratch folders.

D1 — NEW :24–109, "ADDENDUM-n2 v0.1 — COMMITTED"

1. :24–26, "PROPOSAL-n v0.2's addendum, "the fidelity rule, the identity bound and the read of record on the box of record", committed by path as the seat placed it, on the PI's routing of 2026-11-18, third sitting ("Route as given"; item 3, decisions (n-3) and (n-4), [adopt]; item 7, [as ruled])".
   CONFIRMED.
   - The quoted title is A2 :1.
   - SAVED :1 says "PI date 2026-11-18 (third sitting)". Item 3 (:14) ends "… [adopt]; … [go]" and item 7 (:22) "[as ruled]". :25 is "PI: Route as given".
   - The file's sha256 equals the placed value (SAVED :9).

2. :26–27, "Its figures are not computed at this commit: the resume of `6df2131`'s run has not run."
   CONFIRMED, as the repo records it.
   - A2 :4: "Its figures are filled in LOCK-n v0.1 from the extension's figures of record (§4)".
   - The only commits after 6df2131 are bfc869f and 3b2b855, and neither is a resume.

3. :28–29, the file at root, sha256 `41f76c49…bb3f`, "9,671 bytes".
   CONFIRMED.
   - The full sha256 is equal; wc -c gives 9671; SAVED :9 says "9,671 B".
   - Untracked: not in the index, and no commit touches it.

4. :30–31, "It is an addendum, not a new version: PROPOSAL-n v0.2 (`30a3d0f5…04f4`) stays the proposal of record, with ADDENDUM-n1 v0.1 (its header)."
   CONFIRMED. A2 :4 says so, and n hashes to 30a3d0f5…04f4.

5. :32–33, "placed it with its answers of this date and its ruling raw on `p01`, both committed by path at `3b2b855`".
   CONFIRMED.
   - S3 :3: "Placed with this raw: the ruling raw … and `ADDENDUM-n2-…` at root".
   - 3b2b855 adds both files ("A"). Their hashes, d51279ec…0bf4 and e2b1c77a…2a8a, equal SAVED :5 and :7.
   - See observation 2.

6. :34–37, the record of (n-3) and (n-4) "verbatim (the addendum's §6.2 and §6.3 (2))"; the whole paste block, with the PI's word, committed as a raw "byte for byte as saved on receipt".
   CONFIRMED.
   - A2 :46 has §6.2 (2)–(3), the decisions. A2 :48 has §6.3 (2): "with the PI's routing verbatim".
   - PRAW :6–30 is cmp-equal to SAVED, whose last line (:25) is the PI's word.

7. :38–39, the header quote, and "confirms the date the addendum's header asks the PI to confirm at routing, 2026-11-18".
   CONFIRMED.
   - NEW :38 contains SAVED :1 exactly (fixed-string match).
   - A2 :2: "(the PI confirms the date at routing)".

8. :40, "Route as given".
   CONFIRMED. SAVED :25.

9. :41–47, "its items 2, 3 and 7, verbatim".
   CONFIRMED by tool. NEW :43, :45 and :47 equal SAVED :13, :14 and :22, once the quote marker and the block's one-space indent are removed.

10. :49, "Item 2 carries §6.2 (4), the addendum's §5 as the seat's ruling."
    CONFIRMED.
    - A2 :46: "(4) §5 as the seat's ruling".
    - SAVED :13 restates A2 :40: the cached path stays the read of record, and the fresh pair's cost is recorded for G-TIME-n and used by nothing.

11. The relays: :50 "as relayed"; :70 "went to the n sessions as information"; :96 "as relayed"; :97–98 "n-build drafts the resume's launch files … The coordinating session checks them and relays them to the pod session".
    NOT CHECKABLE. The block's headings agree with :50's routing: SAVED :11 "N. n-build (and the pod session on the box)" over items 1–4, and :17 "N. n-analyzer" over item 5.

12. :51–52, "Items 6 and 8 are the coordinating session's. Item 6 is in its close line on `25c9340`'s note, in this commit. Item 8, the push, waits for the PI's word."
    IMPRECISE.
    - SAVED :20–23: "C. Coordinating session" holds items 6, 7 and 8.
    - Item 8 is "[yours]", and the close line is NEW :496–530.
    - Fix: items 6–8 are the coordinating session's. Item 7 is this commit; item 6 is in the close line, in this commit; item 8, the push, waits for the PI's word.

13. :53–56, the departures "inert, with no strike": Code's at `6df2131` (an unpruned `find` … "printing two names"), and the checkers' at `ad856f0`, `6df2131` and `bfc869f`, "as their reports state them".
    CONFIRMED.
    - S3 :46 (heading) and :48: "two names and nothing else"; S3 :49.
    - SAVED :22: "Code's and the checkers' departures of §7 inert".

14. :57, "Item 2's form is restated: a listing over a copied ckpt or report is pruned or not run."
    IMPRECISE (the referent is ambiguous).
    - The words are S3 :48's, where "item 2" is the list of record v2's item 2 (LOR :19).
    - In this entry, "Item 2" at :41–49 means the PI's routing item 2.
    - Fix: "The list of record v2's item 2 is restated: …".

15. :58–59, "The briefs' line of the second sitting stands, with one addition: "a glob is expanded and read before it is looped over"."
    CONFIRMED. S3 :49 has these words exactly; SAVED :22 has "the briefs' glob line [as ruled]".

16. :59, "The referent check's brief below carried it, and so does every brief from here."
    NOT CHECKABLE. The brief is not in the repo. RC :8–9 says the brief carried the line, and this check's brief carries it.

17. :60–62, "52 listings covering 49 distinct statements, three of them cross-listed. 36 are CONFIRMED, 13 IMPRECISE (all minor), 1 FAIL and 2 NOT CHECKABLE, with 12 observations."
    CONFIRMED.
    - RC :19: "52 listings covering 49 distinct statements (three are cross-listed). Grades: CONFIRMED 36, IMPRECISE (minor) 13, IMPRECISE (substantive) 0, FAIL 1 …, NOT CHECKABLE 2".
    - My recount of claims 1–52 by grade gives 36/13/1/2. The cross-listed claims are 37, 44 and 46; the observations run 1–12 (RC :371–432).

18. :63, "The FAIL, graded not substantive by Code, so no STOP under §6.3 (1)."
    CONFIRMED.
    - RC :455.
    - A2 :48: "(1) referent check of 6.4; an unresolved substantive item → STOP".
    - The checker also called it "not substantive" (RC :169).

19. :64–67, the FAIL's substance.
    CONFIRMED.
    - A2 :38: "(settles A-n1 §1.4's reservation, the seat's answers of 2026-11-18, second sitting, §1.4)". A2 :50 lists "ADDENDUM-n1 v0.1 at root: §1.4".
    - A-n1 :26: "1.4 Generated text (G-CAL-n)".
    - The reservation is in S2 §1.4 (:26–30), at :30.

20. :69–70, "recorded for the seat in the raw, unapplied, since the addendum is committed as placed. Six bear on what runs next".
    CONFIRMED. RC :452–453 and :466–470. The six are observations 1, 2, 4, 5, 6 and 7 (RC :471–494).

21. :71–73, the comparison's tolerance: "R3, as the committed driver carries it, with C binding from the lock, since C is computed under the convention the comparison names".
    CONFIRMED.
    - S3 :20: "Code's R3 — … — is accepted as a printed measurement; the lock's bound is ADDENDUM-n2's C".
    - DRV :65 and :76 carry R3; DRV was last committed at ad856f0 and is clean.
    - A2 :24 ("under the convention of record") and A2 :34.

22. :74, "the identity kind and the ceiling at d = 0, whose order the follow-up schema commit fixes".
    CONFIRMED. A2 :48, §6.3 (3): "a follow-up schema commit settled with n-analyzer: the kind, its place in the precedence, …". See observation 3.

23. :75, "alpha, which p0 above 0 makes decisive, and which LOCK-n v0.1 must state".
    CONFIRMED.
    - A2 :18: "the exact-binomial test at the lock's alpha"; (k+1)/(n+2) is never 0.
    - n has no "alpha" (case-insensitive count 0, "α" 0), and A2 :36 names none.

24. :76, "A-n1 §2's third outcome, which its own words make a STOP".
    IMPRECISE.
    - A-n1 :32: "none, or more than one, goes to the seat with the four counts". The word STOP is not in it.
    - D4 :488–489 states it correctly: A-n1's words send the case to the seat, and the relay calls it a STOP.
    - Fix: "which its own words send to the seat with the four counts (a STOP)".

25. :77, "the second row's trigger, which is §3's".
    CONFIRMED. The trigger is at A2 :30; S2 :29 held the earlier one.

26. :78, "p0, C and the median rel, which come from d = 0 reads alone".
    CONFIRMED.
    - RUN has 24 "N1-V none 0" lines.
    - NEW :332: "the 24 reads (N1-V, d = 0, each re-computed)".
    - A2 :34: "the extension's 24 reads".

27. :79–80, the three departures: "a scoped status without item 3's pathspec, a name-only listing of `results/raw`, and shell arithmetic".
    CONFIRMED. RC :436–448.

28. :81–82, the raw, "the report whole and Code's grading".
    CONFIRMED as to content. RC :19–448 is byte-identical to REP, and §2 begins at RC :450. No file of the stated name exists yet.

29. :83–84, "LOCK-n v0.1 declares the figures from the extension's figures of record (§4.2)".
    CONFIRMED. A2 :36.

30. :85–86, p0 = (k + 1)/(n + 2) "… with BK's 0 of 2,400 beside it (§1.1)".
    CONFIRMED. A2 :18.

31. :87–89, C = max(0.25, 2 × …) nats: a new pause kind, `fidelity-ceiling`, after `non-finite`; the identity bound at d = 0; "exact on a deterministic backend" struck.
    CONFIRMED. A2 :24 and :26.

32. :90–91, the TAU/4 row kept, and a second, descriptive row at the extension's median rel "where it drops more than half of an arm's reads at a point (§3)".
    CONFIRMED. A2 :30.

33. :92–93, the figures of record: from the resume if the comparison names "bare", "and otherwise" from `backend-ext-2` (§4.1).
    CONFIRMED. A2 :34. See observation 4.

34. :94–95, the cached path stays the read of record; the fresh pair's cost is recorded for G-TIME-n and used by nothing (§5).
    CONFIRMED. A2 :40.

35. :97, "(`--resume --ruling p01=PATH`, with the ruling raw of `3b2b855`)".
    CONFIRMED.
    - SAVED :6: "(the ruling raw for --resume --ruling p01=PATH)"; S2 :23.
    - The ruling raw is added at 3b2b855.

36. :99, "The resume prints the distribution, the in-band count and A-n1 §2's comparison."
    CONFIRMED. SAVED :12 (item 1), S3 :20, RUL :8.

37. :100–101, "Then come `backend-ext-2`, if needed; the `fidelity-ceiling` kind … settled with n-analyzer; the extension's entry; and LOCK-n v0.1, drafted to the seat."
    CONFIRMED. A2 :48 gives this order in §6.3 (3) and (5); SAVED :14.

38. :102–103, n-analyzer: §3's second row and the ceiling's kind in the reader before the canonical run, "with PIN-n-37 amended (the answers' §6)".
    CONFIRMED. A2 :48 §6.3 (4); SAVED :18 (item 5); S3 :44.

39. :104, "The n-build and n-analyzer sessions add their close lines here (the addendum's header)."
    CONFIRMED. A2 :4.

40. :106–108, "Committed by path: …", "The commit-time count … is 0", "Nothing in this session ran on a model or the box", "Not pushed".
    NOT CHECKABLE: the commit is still to come.
    - The list matches SAVED :22 (item 7) and A2 :48 (§6.3 (2)).
    - Pre-check: see observation 11.

D2 — NEW :496–530, the close line on 25c9340's note

41. :496–499, the seat's answers of the third sitting, "(sha256 `d51279ec…0bf4`, committed at `3b2b855`), rule on this note in their §5".
    CONFIRMED. The hash matches (cut); 3b2b855 adds the file; S3 :34 is "## 5. The home-folder path in the public tree (`25c9340`)".

42. :499–500, "The PI routed that ruling as item 6 ("Route as given")."
    CONFIRMED. SAVED :21 and :25.

43. :500–502, "The paste block is committed as a raw, […], with `ADDENDUM-n2 v0.1 — COMMITTED`, in the commit that carries this line."
    NOT CHECKABLE: the commit is still to come. It is consistent with D1 :34–37 and PRAW :3.

44. :504, item 6, verbatim.
    CONFIRMED by tool. NEW :504 equals SAVED :21, once the quote marker and the one-space indent are removed.

45. :506–507, "(a), record and leave (§5.1). The 252 files stay as committed, and the history is not rewritten. Ledger (81) stands for seat files, and this note is the record of the class."
    CONFIRMED. S3 :36: "WORKFLOW §5 keeps committed raws unedited and history unrewritten … Ledger (81) stands for seat files; the dated note is the record of the class."

46. :508–509, "a standing rule from that raw until WORKFLOW v1.1 is routed, and v1.1's item. This session carries it with every commit window."
    CONFIRMED. S3 :38: "The coordinating session carries it as WORKFLOW v1.1's item with the commit window; until v1.1 is routed it is a standing rule from this raw."

47. :510–512, the rule: every commit, inside its window, the prefix counted over the staged diff, the pattern never printed; a count above zero halts the commit.
    CONFIRMED. S3 :38.

48. :513–515, the form `git diff --cached -- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**' | /usr/bin/grep -cF -- "$HOME"`, and "neither the command nor its output holds it".
    CONFIRMED.
    - The form is S3 :38's "`git diff --cached` piped to a fixed-string count", under item 3's pathspec (LOR :20) and §5.3's `data/mf3` exclusion (S3 :40).
    - Under that pathspec, 3b2b855's diff carries both of its files: 2 file headers and 79 added lines, which is 67 + 10 + 2 header lines.

49. :516, "Its test (the list of record v2's item 9)".
    CONFIRMED. LOR :26: "A command form named by a rule is tested on the machine it binds before the rule is adopted, by Code, names only, and the rule quotes the test".

50. :516–518, the scratch-repository test's counts (1; 0; 3).
    NOT CHECKABLE: the scratch repository was deleted.

51. :519–521, "So under item 3's pathspec and the `data/mf3` exclusion, the form does not reach … There, the pre-push screen's `local_path` class reads at the push. That is a reading for the seat."
    CONFIRMED, as a reading.
    - LOR :20: item 3's `/**` form, "tested on this git". LOR :26 records that test at 9eed029: "the `/**` form none".
    - LOR :21: item 4's screen "may read every file in the range, `ckpt` and `reports` included".
    - PUSH :10 prints the `local_path` class with an "inside" count.

52. The relays: :513 "as relayed to the n-build, n-analyzer and pod sessions"; :525–526 "It is relayed … and carried in every brief".
    NOT CHECKABLE. This check's brief carries the rule.

53. :522, "It was first applied at `3b2b855` … counting 0".
    CONFIRMED, as to the count.
    - D2 :514's form, run over 3b2b855's own diff under the same pathspec, gives 0.
    - That diff carries both of 3b2b855's raws, so the 0 is not vacuous. See observation 9.

54. :522, "and again at this commit".
    NOT CHECKABLE: a future commit.

55. :523–525, "The departure (§5.3) … is inert, with no strike. The rule is restated: … every git command over the tree takes the `data/mf3` exclusion as well as item 3's pathspec."
    CONFIRMED. S3 :40.

56. :527, "C.5, the push since this note's C.5 line (gitleaks 8.30.1)".
    CONFIRMED.
    - The note's C.5 line covers fa96ccf..dc6a1cf (NEW :480–485).
    - The next push is dc6a1cf..ad856f0 (PUSH :2–3 and :22). HEAD's RESULTS.md has no record of that range.
    - PUSH :13 names gitleaks 8.30.1. See observation 8.

57. :528, "`dc6a1cf..ad856f0`, 2 commits, on the PI's word "Push them" (2026-11-18)".
    CONFIRMED.
    - PUSH :1, :3 and :22–23.
    - `rev-list --count` gives 2 (25c9340 and ad856f0); origin/main is ad856f0.

58. :528–530, "Every class was CLEAR but `port`, whose one match outside was read: the declared container port, in this note's values-check raw. Nothing matched inside `ckpt` or `reports`. gitleaks found nothing. There was no halt."
    CONFIRMED.
    - PUSH :4–10: port "1 distinct; inside: 0 -> READ", every other class CLEAR, and every "inside: 0".
    - PUSH :8 places the match at HFV@25c9340. PUSH :16–17: "no leaks found", "gitleaks findings: 0". PUSH :20: "the declared container port "22/tcp" … No halts."
    - HFV :110 (item 33) holds the quote. The other values-check raw of 25c9340 has no "22/tcp".

D3 — PRAW

59. :1, "The PI's routing of 2026-11-18 (third sitting), verbatim (the PI → the coordinating session)".
    CONFIRMED. The date and sitting match SAVED :1, and the form is the precedent raw's (2026-11-16_second-sitting_pi-routing.md :1).

60. :3, "as the PI gave it in chat on PI date 2026-11-18, saved verbatim by the coordinating session on receipt".
    NOT CHECKABLE: chat and receipt. The date matches SAVED :1.

61. :3, "Its last line, "PI: Route as given", is the PI's own line after the block."
    CONFIRMED. SAVED :25 and PRAW :30, after the items. That the PI typed it is not checkable.

62. :3, "Committed with `ADDENDUM-n2 v0.1 — COMMITTED`, as the addendum's §6.3 (2) asks for the PI's routing quoted verbatim."
    CONFIRMED. A2 :48: "(2) Commit `ADDENDUM-n2 v0.1 — COMMITTED` with the PI's routing verbatim".

63. :3 and :5–31, "The 25 lines between the fences are byte-identical to the saved copy, sha256 `7fac92ba…77f0`."
    CONFIRMED.
    - The fences are at :5 and :31, and :6–30 (25 lines) is cmp-equal to SAVED (25 lines).
    - SAVED's full sha256 equals the stated value, and the fenced lines hash to the same value.

D4 — RC header (:1–16) and §2 (:450–512)

64. :1, "ADDENDUM-n2 v0.1: the referent check of its §6.4, and Code's grading (PI date 2026-11-18)".
    CONFIRMED. A2 :50 is §6.4. The form matches the precedent `2026-11-16_addendum-n1_referent-check.md` :1.

65. :3–4, "The addendum's §6.3 (1) asks for "referent check of 6.4; an unresolved substantive item → STOP"."
    CONFIRMED. A2 :48 has these words exactly (fixed-string match).

66. :4–11, the checker ("a subagent of the coordinating session") and its brief (items 1–5 with C.2, the two lines, the `data/mf3` exclusion, no interpreter).
    NOT CHECKABLE.
    - The two quoted lines are the seat's own words (S2 :51; S3 :49).
    - The report's tools and not-done lists (RC :69–89) agree with the brief as the header describes it.

67. :13, "as its hand-back message gave it, with the harness's two-space indent removed".
    NOT CHECKABLE.

68. :13–14, "The result is byte-identical to the unindented copy of the report that the session's record also holds (430 lines)."
    CONFIRMED. RC :19–448 (430 lines) is cmp-equal to REP (430 lines); RC :449 is the blank line before §2.

69. :15, "It held no local path."
    CONFIRMED. REP has 0 lines with the home-folder prefix, "/Users/", "/private/", "/tmp" or the session's temporary-folder name.

70. :452–453, "The addendum is committed as the seat placed it (`41f76c49…bb3f`). Nothing in it is edited".
    CONFIRMED. The file's sha256 equals the placed value (SAVED :9).

71. :455, "One FAIL, claim 16, graded not substantive, so no STOP under §6.3 (1)."
    CONFIRMED. RC :168–174 and A2 :48.

72. :456–457, the claim's two quotations.
    CONFIRMED. Each is a fixed-string match in A2 (:38 and :50).

73. :458, "A-n1 §1.4 (its line 26) is "Generated text (G-CAL-n)"."
    CONFIRMED. A-n1 :26. That Code read both places itself is not checkable.

74. :458–460, the reservation is "the last bullet of the second sitting's own §1.4 (that raw's line 30, "The read of record. If the diagnostic puts the discordance in the continuation tokens …"). No A-n1 section is cited there."
    CONFIRMED.
    - S2 §1.4 runs :26–30, with bullets at :27–30.
    - :30 opens with these words; only its bold markers are dropped in the quote. It cites no A-n1 section.

75. :461–462, "§5's heading names that place in its second citation. §5's ruling … and what runs under it are unaffected."
    CONFIRMED. A2 :38 and :40.

76. :466–467, the thirteen minor IMPRECISE listings ("4, 5, 10, 14, 17, 24, 25, 30 for its words, 33, 35, 36, 37 and 43; 37 is 24 cross-listed") and "the two NOT CHECKABLE items (34, 39)".
    CONFIRMED.
    - The grade lines are at RC :105, :112, :137, :157, :177, :209, :216, :253 (30's words), :270, :281, :289, :296 and :329.
    - RC :295 says 37 is 24, cross-listed. RC :276 and :307 grade 34 and 39 NOT CHECKABLE.

77. :469, "The twelve observations … Six bear on what runs next."
    CONFIRMED. RC :371–432 holds observations 1–12; §2 lists 1, 2, 4, 5, 6 and 7.

78. What was sent or told to sessions: :470 "Each was sent to the session it touches", :482 "both were told", :486 "The n-build session was told", :488–489 "The coordinating session's relay … already says so: a STOP", :492 "It was told".
    NOT CHECKABLE.

79. :471–472, "A-n1 §2's tolerance includes "the backend's identity bound", which §2.2 makes C."
    CONFIRMED. A-n1 :32; A2 :26 ("its bound is C").

80. :473–474, the quotation from S3 §1.4.
    CONFIRMED. It is S3 :20 exactly (fixed-string match).

81. :475–477, C is computed "under the convention of record" (§2.1), and the comparison names that convention (§4.1).
    CONFIRMED. A2 :24 and :34.

82. :478–479, "the resume's comparison runs with R3, as the committed driver carries it, and C binds from the lock".
    CONFIRMED. DRV :65 and :76 (R3); DRV's last commit is ad856f0 and it equals HEAD's blob. See observation 5.

83. :480–483, observation 2: the same quantity against the same C; the ceiling's place is fixed in §6.3 (3)'s follow-up schema commit; "directly after" is the seat's.
    CONFIRMED. A2 :24, :26 and :48; RC :382–387.

84. :484–486, observation 4: "n v0.2 declares no alpha, and §4.2's list does not name one. The driver's R5 holds 0.01." and "the lock's alpha" (§1.1).
    CONFIRMED.
    - The case-insensitive count of "alpha" in n is 0 ("α" 0), and A2 :36 names none.
    - DRV :82 and :400 (`BEXT_ALPHA = 0.01  # R5`); NEW :357; A2 :18.

85. :487–489, observation 5: §4.1 "has no branch for "none, or more than one""; A-n1 §2 sends that case to the seat.
    CONFIRMED. A2 :34 has two branches; A-n1 :32.

86. :490–492, observation 6: §3's trigger "replaces the second sitting's "where it empties (PIN-n-20's `tau4-emptied`)"".
    CONFIRMED. S2 :29 has those words exactly; A2 :30. See observation 6.

87. :493–494, "p0, C and the median rel come from 24 N1-V shadows at d = 0, and bind the re-computed reads at every dose."
    IMPRECISE.
    - The first half is right: RUN has 24 "N1-V none 0" lines.
    - But the median rel binds nothing. It sets §3's second row, which is descriptive (A2 :30: "Neither row gates anything").
    - The report's observation 7 (RC :409) names only "The binomial and the ceiling".
    - Fix: "… at d = 0; p0 and C bind the re-computed reads at every dose, and the median rel sets the descriptive second row".

88. :496, "Observations 3 and 8–12 concern wording, or the reasoning behind §5."
    IMPRECISE.
    - Observations 3, 8, 9 and 10 fit (RC :389–394, :411, :413–417, :419–422).
    - Observation 11 is a gap in §6.1's list of changed sections: n §3 is missing, though §4.2 adds lock contents (RC :424).
    - Observation 12 records that the figures agree (RC :426–432).
    - Fix: say that observations 3 and 8–10 concern wording or §5's reasoning, 11 notes that §6.1 omits n §3, and 12 records agreement on the figures.

89. :498–501, the checker's first departure: "a `git status --porcelain` over 14 named paths outside `data/`, without item 3's pathspec or the `data/mf3` exclusion, which printed one line (the addendum's "??")", at HEAD 3b2b855.
    CONFIRMED.
    - RC :436–439: "the 13 named referent paths and the addendum" (14 in all), "All are outside data/", and the one printed line.
    - RC :434: "HEAD 3b2b855 throughout".

90. :501–502, the second departure: "a name-only `ls results/raw`, piped to a fixed-string grep for this date's n raws, which printed 18 names".
    IMPRECISE.
    - RC :442: the grep was `/usr/bin/grep -F '2026-11-18_n-step4'`, which matches this date's n step-4 raws only.
    - Other n raws of the date fall outside the pattern; for example, `results/raw/2026-11-18_n2_valuescheck.md` (committed at b4522ae) does not match.
    - The 18 names and the item-5 caveat (RC :443) are right.
    - Fix: "piped to a fixed-string grep for '2026-11-18_n-step4' (this date's n step-4 raws)".

91. :503, "zsh's built-in arithmetic for five sums and ratios, with no external program run".
    CONFIRMED. RC :446–448.

92. :505, "It read nothing under `data/`, ran no interpreter and wrote no file."
    CONFIRMED, as the report states it. RC :80–89.

93. :507–508, "The report's line numbers index the files at `3b2b855`. Its RESULTS.md anchors (:610, :11510) index `3b2b855`'s RESULTS.md."
    CONFIRMED by spot-check. Every file read equals its blob at HEAD 3b2b855.
    - RESULTS.md :610 holds "(82)" and :11510 holds "D_n = 2026-12-15".
    - Each of these holds the words the report gives it: n :47, :77, :97, :109, :117, :128, :148, :152; A-n1 :26, :32; S2 :15, :17, :26–30; S3 :20, :24, :28, :44; RUL :7–9; CLAUDE.md :333; DRV :65, :76; RUN :58, :81; DIAG :49; NB16 :50.

94. :508, "The commit that carries this raw adds lines at the Log's head, which moves them."
    IMPRECISE.
    - The commit also inserts D2's 35 lines (NEW :496–530), which also sit above both anchors.
    - In NEW the anchors move to :731 and :11631, a shift of 121 lines, not 86.
    - Fix: "adds lines at the Log's head and under 25c9340's note, which moves them (to :731 and :11631 in the draft)".

95. :510–512, the values-check "is recorded in [`2026-11-18_addendum-n2_valuescheck.md`]".
    NOT CHECKABLE. No file of that name exists yet. See observation 7.

OBSERVATIONS

1. The brief places the note at RESULTS.new :329, but that is its line in HEAD's RESULTS.md. In NEW the note begins at :415, and D2 follows its last line (RESULTS.md :409).
2. D1 :32, "its answers of this date": the seat sat three times on 2026-11-18. "Its answers of the third sitting" (D2 :497's words) would be unambiguous. Likewise, D1 :70's "Six bear on what runs next" follows "the thirteen minor items and the twelve observations"; D4 :469 makes clear the six are observations.
3. D1 :74 says the follow-up schema commit fixes the order of the identity kind and the ceiling. D4 :483 adds that whether "after `non-finite`" means directly after it is the seat's. The two texts would agree if D1 carried that clause.
4. D1 :92–93 says "otherwise", but A2 :34 branches on "If it names another candidate". The third outcome is D1 :76's bullet. "And, if it names another candidate, from one more run …" would match §4.1.
5. D4 :479: the checker put the closing sentence in the addendum's §2.2 or §4.1 (RC :380). Moving it to the lock follows from the addendum being committed as placed. Saying so would keep the disposition traceable.
6. D4 :490–491 quotes §3 as "where it drops …", but A2 :30 has "Where" (it begins the sentence). The lower-case form is S3 :28's.
7. D4 :510–512 names "this section" (§2), the entry, the close line and the PI-routing raw. This check also covered RC's header (:1–16) and §1's byte-identity with the report copy.
8. D2 :527, "(gitleaks 8.30.1)": the version comes from the push record's own header line (PUSH :13); gitleaks' output lines (:14–16) print none. The note's own C.5 line says so (NEW :480–481), and D2's parenthetical drops that caveat.
9. D2 :522, "first applied at `3b2b855`": 3b2b855's commit message records the ruling ("with a commit-time count") but not a run of the count in that commit's window. The re-run over its diff is item 53.
10. Tooling, for the seat. The briefs say a git command takes item 3's pathspec "even for a named file", and that interacts badly with ls-files on this git (2.39.5).
    - `git ls-files` printed nothing for the tracked ruling raw named alone under any of item 3's exclusions. It gave 0 with each exclusion alone, 1 with no exclusion, and 2 with CLAUDE.md named beside it.
    - scripts/n_sessions.py named alone was listed under all three exclusions.
    - `git log` under the full pathspec found the raw. `git ls-tree` refuses exclude magic ("pathspec magic not supported by this command: 'exclude'").
    - So an ls-files check of a lone results/raw file under the pathspec can report a tracked file as untracked. I settled tracked-and-clean with `git rev-parse HEAD:<path>` against `git hash-object` instead.
    - My reading of the cause, untested: the exclusions are matched after the positive paths' common directory prefix has been cut from them.
    - D2's count form is not affected: its positive pathspec is `.`, and over 3b2b855 it carried both raws.
11. D1 :106–108's count, checked ahead of the commit:
    - No line with the home-folder prefix in entry2.md, close_25c9340.md, PRAW, RC, REP or A2 (0 each).
    - NEW's two hunks, with three context lines either side, also count 0.
    - NEW as a whole has 1 such line, the same as HEAD's RESULTS.md: the note's "RESULTS.md (1 line, 4 occurrences)" (NEW :433).
    - The values-check raw staged with them must hold none too.
12. D1 :50 names items 1 and 4 as relayed to the n-build and pod sessions. The block files items 2 and 3 under the same heading (SAVED :11–14). The entry records both (:41–49, :96–101) but does not say whether they were relayed.

DEPARTURES (checkout HEAD 3b2b855 throughout)

1. Path-taking git commands without item 3's full pathspec. All seven were on named files outside data/, run while diagnosing observation 10, and each piped to `wc -l`, so each printed only a count.
   - `git ls-files` on CLAUDE.md, on RESULTS.md and on the ruling raw, with no pathspec: 1, 1, 1.
   - `git ls-tree --name-only HEAD` on the ruling raw, with no pathspec: 1.
   - `git ls-files` on the ruling raw with one exclusion only (the ckpt glob form, the `data/mf3` form, the ckpt `:!` form): 0, 0, 0.
   - Nothing under data/ was named or printed. A fourth single-exclusion run used `':!data/**'`, which is item 3's form.
2. Two `git rev-list --count` calls over named ranges (6df2131..HEAD and dc6a1cf..ad856f0) without a pathspec. They take no path argument as run. Printed: 2 and 2.
3. `--format='%h %ad' --date=short` (author dates, where item 1 names commit times) in two `git log` calls and one `git show`, each with the pathspec. Printed: five lines of short ids, each dated 2026-11-18.
4. Two `git ls-tree` calls with the three exclusions, both refused by git (exclude magic unsupported).
   - One printed git's fatal line, which repeats the ckpt exclusion's text.
   - In the other, the error line was counted through a pipe (it printed 1, which I first misread as a match).
5. For the seat to class, under the no-interpreter rule: zsh built-ins only, with no external interpreter run.
   - for loops and `[[ ]]` string comparisons.
   - Parameter expansion to strip quote markers.
   - printf, and one shell function wrapping a fixed-string count.

TOTALS: 95 items: 76 CONFIRMED, 7 IMPRECISE (12, 14, 24, 87, 88, 90, 94), 0 FAIL (none), 12 NOT CHECKABLE (11, 16, 40, 43, 50, 52, 54, 60, 66, 67, 78, 95), and 12 observations.

## 2. Pass 1: dispositions

**The seven IMPRECISE items, each applied in the checker's sense:**
- 12: items 6–8 are the coordinating session's, and item 7's place is named (the entry; pass 2's item 5 refined it).
- 14: "The list of record v2's item 2 is restated in its form" (the entry).
- 24: A-n1 §2's third outcome is one "which its own words send to the seat with the four counts: a STOP" (the entry).
- 87: observation 7's bullet. p0 and C bind the re-computed reads at every dose, and the median rel sets the
  descriptive second row (the referent-check raw's §2).
- 88: observations 3 and 8–10, 11 and 12, each named for what it is (the referent-check raw's §2).
- 90: the grep's pattern, `2026-11-18_n-step4` (the referent-check raw's §2).
- 94: the anchors move with both insertions, to :778 and :11678 in the committed RESULTS.md (the referent-check
  raw's §2).

**The observations:**
- 1: the brief's line number for the note. No text needed.
- 2: "its answers of the third sitting", and "Six of the observations" (the entry).
- 3: the entry's precedence bullet adds "Whether "after `non-finite`" means directly after it is the seat's".
- 4: the figures-of-record bullet follows §4.1's "if it names another candidate".
- 5: the referent-check raw's §2 says where the checker placed the closing sentence, and where it can go (pass 2's
  item 48 refined it).
- 6: the quote is §3's "Where …", capital included.
- 7: the referent-check raw's last paragraph names everything this check covered.
- 8: the close line's C.5 parenthetical says where the version comes from.
- 9: the close line says the count ran in `3b2b855`'s window, before that commit, and that this check re-ran it over
  that commit's diff (0).
- 10: Code tested it on the laptop with git 2.39.5, names and counts only, at HEAD `3b2b855`. The counts, with the
  ruling raw (`results/raw/2026-11-18_n-step4-p01_ruling.md`) named alone unless a bullet says otherwise:
  - with no exclusion, `git ls-files` listed it: 1;
  - under item 3's `/**` exclusions with the `data/mf3` one, under `':!data/**'`, and under the `(exclude,glob)`
    forms: 0 each;
  - beside CLAUDE.md, under the exclusions: 2;
  - CLAUDE.md alone, and `scripts/n_sessions.py` alone, under the exclusions: 1 each;
  - `git log --format=%h` and `git diff --name-only bfc869f 3b2b855`, under the exclusions: 1 each.

  It is the entry's tooling reading, for the seat. The test's no-exclusion baseline is a git command without item
  3's pathspec, Code's own, disclosed here for the seat to class.
- 11: a pre-check of the commit-time count. The count at the commit is the gate's.
- 12: items 1–4 went to the n-build and pod sessions (the entry).

**The checker's departures**, as its report states them, for the seat to class:
- seven path-taking git commands on named files outside `data/` without item 3's full pathspec, each counted through
  `wc -l`, while diagnosing observation 10;
- two `git rev-list --count` calls over named ranges, without a pathspec;
- author dates (`%ad`, short) in two `git log` calls and one `git show`, where item 1 names commit times;
- two `git ls-tree` calls with the exclusions, which git refused, one printing git's fatal line;
- zsh built-ins in place of any interpreter.

None of them read anything under `data/`.

## 3. Pass 2: the report, whole

VALUES-CHECK PASS 2: the edits after pass 1 (ADDENDUM-n2 v0.1 — COMMITTED) — 71 items: 55 CONFIRMED, 6 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE; 8 observations.

HEADER

Checkout: HEAD 3b2b855; origin/main (local ref) ad856f0; git 2.39.5 (Apple Git-154). Every repo file I read equals its blob at HEAD (`git rev-parse HEAD:<path>` against `git hash-object`): S3, RUL, S2, A-n1, DRV, RESULTS.md, STOP, LOR, n, CLAUDE.md. A2's sha256 is 41f76c49…bb3f (cut), and the full value equals the placed one.

Labels
- Scratch (the coordinating session's folder): LIST = the scratch edits_after_pass1.md; P1 = the scratch vc1/report_vc1.txt (pass 1's report); D1 = the scratch entry2.md; D2 = the scratch close_25c9340.md; RC = the scratch refcheck_raw.md (the scratch rc_tail.md is RC :449–518); VC = the scratch vc_raw.md; NEW = the scratch RESULTS.new; SAVED = the scratch pi-routing-saved.txt; REP = the scratch report.txt.
- POD = the pod session's scratch folder (close3): POD/relay_copyback.txt; POD/close.md (sha256 18c8267c…332c, cut); PODVC = POD/2026-11-18_n-step4-run-pause-pod-close_valuescheck.md (b883246b…90b8, cut). Both hashes equal LIST E12's finals.
- Repo: A2 = ADDENDUM-n2-fidelity-on-the-box-of-record-v0_1.md; A-n1 = ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md; n = PROPOSAL-n-bk-reconciliation-v0_2.md; S3 = results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md; S2 = results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md; RUL = results/raw/2026-11-18_n-step4-p01_ruling.md; STOP = results/raw/2026-11-18_n-step4-run-pause_code-to-design_STOP.md; LOR = results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md; DRV = scripts/n_sessions.py (sha256 18f19b8e…4f5c, cut: v2d, last committed at ad856f0).
- Line numbers: D1's are entry2.md's (NEW = D1 + 23); D2's are close_25c9340.md's (NEW = D2 + 525); RC's are refcheck_raw.md's.

What I read
- Scratch, in full: LIST :1–107; P1 :1–478; D1 :1–116; D2 :1–46; rc_tail.md :1–70; RC :1–518; VC :1–546; SAVED :1–25.
- NEW: :1–30, :134–193 and :440–579, plus :772 and :11672 by sed. The whole file was compared to HEAD's RESULTS.md by diff, printing hunk headers only.
- REP by cmp only, plus counts. The scratch pi-routing-raw.md got a home-prefix count only.
- POD, in full: relay_copyback.txt :1–16, close.md :1–93, PODVC :1–99.
- Repo, in full: A2 :1–50, S3 :1–67, RUL :1–10.
- Repo, in part: A-n1 :20–35; LOR's headings and :16–29; n :77.
- DRV by fixed-string greps (line numbers and short excerpts), plus :61–64 and :575–590 by sed.
- RESULTS.md: :157–215 by fixed-string grep. HEAD's blob at :22, :409, :610 and :11510, and its "Close …" lines, by grep.
- STOP by fixed-string grep (:18, :24, :49, :96, :216–217).
- S2 and CLAUDE.md: blob checks only.

Assembled copies, by cmp
- D1 = NEW :24–139.
- D2 = NEW :526–571.
- rc_tail.md = RC :449–518.
- REP = RC :19–448.
- VC :22–499 = P1.
- NEW differs from HEAD's RESULTS.md only by the hunks 23a24,139 and 409a526,571.

Tools
- The file-read tool.
- `shasum -a 256` with cut.
- /usr/bin/grep (-n -c -F -i -o -E -e -B1) on named files and pipes.
- sed -n, cut, wc -l, uniq, cmp, diff, head, tr.
- `gitleaks version`, run once.
- git: --version; rev-parse; hash-object (no -w); log --format (%h %p %s; %h; %s; %B); show --name-status; `show HEAD:RESULTS.md`; ls-files (E4's tests); diff and diff --name-only (bfc869f..3b2b855).
- Shell syntax: cd, echo, command substitution, brace groups, pipes (see DEPARTURES 5).

Not done
- No file written.
- No git add, commit, checkout, reset or stash, and nothing that changes the index, the tree or a ref.
- Nothing under data/ read, listed, hashed or searched, data/mf3 included.
- No git status of any kind; no listing of results/raw or of any folder.
- No interpreter, no network, no --stat or --numstat.
- No marker word in any argv.
- Searches stayed in the repo and the two named scratch folders. The previous push's record lies outside them and was not read. In POD only the three named files were opened.
- Unchanged lines inside edited regions were not re-graded: D1 :92 and :98–100, and D1 :112–115.

ITEMS

E1 — D1 (fixes P1 obs 2, first half; the "after" text stands)
1. D1 :9–10, "The seat placed it with its answers of the third sitting and its ruling raw on `p01`, both committed by path at `3b2b855`."
   CONFIRMED.
   - S3 :3: "Design seat, PI date 2026-11-18 (third sitting)", and "Placed with this raw: the ruling raw … and `ADDENDUM-n2-…` at root".
   - 3b2b855's --name-status shows "A" for both raws. Its message begins "The seat's answers of 2026-11-18 (third sitting)".

E2 — D1 (fixes P1 12 and P1 obs 12; stands)
2. D1 :27, "Items 1–4 went to the n-build and pod sessions, and item 5 to the n-analyzer session".
   CONFIRMED as to the block. SAVED :11 "N. n-build (and the pod session on the box)" heads items 1–4 (:12–15), and :17 "N. n-analyzer" heads item 5 (:18). See observation 8.
3. D1 :27, "as relayed".
   NOT CHECKABLE. POD/close.md :10–11, outside the repo, says the pod session got items 1 and 3 "as the coordinating session relayed them".
4. D1 :28, "Items 6–8 are the coordinating session's."
   CONFIRMED. SAVED :20–23.
5. D1 :28, "Item 7 is this commit."
   IMPRECISE.
   - SAVED :22: "7. The three files committed by path, the addendum after its referent check (§6.4); …".
   - Two of the three files went in at 3b2b855, whose message says "committed by path (the paste block's item 7)". D1 :9–10 says so too.
   - This commit carries the third file and records item 7's other rulings (D1 :30–37).
   - Fix: "Item 7 is carried by `3b2b855` (its two raws) and by this commit (the addendum after its referent check, with item 7's other rulings)."
6. D1 :28–29, "Item 6 is in its close line on `25c9340`'s note, in this commit."
   CONFIRMED. SAVED :21 ends "a close line on 25c9340's note [as ruled]". Hunk 409a526,571 puts D2 directly after the note's last line (HEAD :409 = NEW :525).
7. D1 :29, "Item 8, the push, waits for the PI's word."
   CONFIRMED.
   - SAVED :23 "[yours]". S3 :51 addresses the block "for the PI (… your words are the record)".
   - S3 :32: "The push itself is the PI's word, as always."

E3 — D1 (fixes P1 14; stands)
8. D1 :34–35, "The list of record v2's item 2 is restated in its form: a listing over a copied ckpt or report is pruned or not run."
   CONFIRMED.
   - S3 :48: "item 2's form restated — a listing over a copied ckpt or report is pruned or not run".
   - The departure it rules is an unpruned `find`, which LOR :19 (item 2) names: "any unpruned `find`".

E4 — D1, new text (re-run at HEAD 3b2b855, counts only)
9. D1 :38, "from this entry's values-check (its observation 10)".
   CONFIRMED. P1 :447–453.
10. D1 :38–39, "Code tested it on the laptop, with git 2.39.5 (the list of record v2's item 9)".
    CONFIRMED.
    - `git --version` gives 2.39.5.
    - LOR :26 (item 9) is the form: tested on the machine it binds, by Code, names only.
    - Who ran the test is not checkable, but its results reproduce (items 11–14).
11. D1 :40–41, "Under item 3's exclusions, in any of its three forms, `git ls-files` with a lone named file under `results/raw` printed nothing for a tracked file."
    CONFIRMED.
    - RUL alone gives 0 under each form: `/**` plus `':!data/mf3/**'`; `(exclude,glob)` plus `':!data/mf3/**'`; `':!data/**'` alone; and `':!data/**'` with `':!data/mf3/**'`.
    - With no exclusion it gives 1, and its rev-parse equals its hash-object, so it is tracked.
    - A second lone raw, S3, also gives 0 under `/**` plus `':!data/mf3/**'`.
12. D1 :42, "The same file named beside CLAUDE.md printed both."
    CONFIRMED: 2.
13. D1 :42–43, "A lone root file, or a lone file under `scripts/`, was listed."
    CONFIRMED. CLAUDE.md alone gives 1, and scripts/n_sessions.py alone gives 1, both under `/**` plus `':!data/mf3/**'`.
14. D1 :43, "`git log` and `git diff --name-only` under the same pathspec found the file."
    CONFIRMED. `git log --format=%h` gives 1; `git diff --name-only bfc869f 3b2b855` gives 1.
15. D1 :44–45, tracked-and-clean "takes `git rev-parse HEAD:<path>` against `git hash-object` (item 1), not `git ls-files` under the exclusions".
    CONFIRMED as a reading. LOR :18 (item 1) permits "`git rev-parse <rev>:<path>` compared in the shell" and "any program's digest that prints no byte, size or time".
16. D1 :46, "The commit-time count's form, whose positive pathspec is `.`, is unaffected."
    CONFIRMED.
    - `git diff --name-only bfc869f 3b2b855 -- .` under the exclusions gives 2 (both raws).
    - The form's diff over that range carries 2 file headers. D2 :19's positive pathspec is `.`.

E5 — D1 (fixes P1 obs 2, second half; stands)
17. D1 :57, "Six of the observations bear on what runs next".
    CONFIRMED. The six bullets (D1 :59–67) are RC §2's observations 1, 2, 4, 5, 6 and 7 (RC :471–495), and RC :469 says "Six bear on what runs next".
18. D1 :57–58, "and went to the n sessions as information".
    NOT CHECKABLE (relays). See observation 2.

E6 — D1 (fixes P1 obs 3; stands)
19. D1 :62–63, "whose order the follow-up schema commit fixes. Whether "after `non-finite`" means directly after it is the seat's".
    CONFIRMED.
    - A2 :24: "after `non-finite` in the precedence".
    - A2 :48 §6.3 (3): "a follow-up schema commit settled with n-analyzer: the kind, its place in the precedence, …".
    - RC :484 has the same clause; REP's observation 2 (RC :386) raises the reading.

E7 — D1 (fixes P1 24; stands)
20. D1 :65, "A-n1 §2's third outcome, which its own words send to the seat with the four counts: a STOP".
    CONFIRMED. A-n1 :32: "none, or more than one, goes to the seat with the four counts". The gloss "a STOP" matches RC :488–490.

E8 — D1 (fixes P1 obs 4; stands)
21. D1 :81–82, "from the resume if A-n1 §2's comparison names "bare", and, if it names another candidate, from one more run of the 24 reads under that convention, `backend-ext-2` (§4.1)".
    CONFIRMED. A2 :34: "If the check names "bare", the run of record of `6df2131` gives them on its resume. If it names another candidate, the extension's 24 reads are run once more under that convention …".

E9 — D1, new text
22. D1 :85, "(§6.3 (3)–(5))".
    CONFIRMED. A2 :48: (3) is n-build's work, (4) n-analyzer's, and (5) LOCK-n v0.1.
23. The relays and v2e:
    - :85 "as relayed"; :86 "n-build first commits its driver's v2e";
    - :87–88 "v2e prints its min, quartiles, median and max, and carries `backend-ext-2`. The choice is Code's (the coordinating session's), declared in v2e's entry for the seat to strike";
    - :89–91 "then runs from v2e's commit in a fresh copy on the box, and the run's copy stays untouched. n-build drafts the launch files; the coordinating session checks them and relays them to the pod session";
    - :94 "on the coordinating session's relay after the resume's outputs are read".
    NOT CHECKABLE.
    - v2e is not committed: DRV's last commit is ad856f0 (v2d). The relays and v2e's entry are not in the repo.
    - Outside the repo, POD/close.md :12–15 and :16–22 give the same route: "it runs from driver v2e's commit in a fresh sparse copy"; the run's copy "stays untouched"; `backend-ext-2` "is built into v2e, does not chain, and runs only on the coordinating session's relay, after the resume's outputs are read"; and "n-build's files, frozen and relayed by the coordinating session with their hashes".
24. D1 :86–87, "The committed driver does not print the answers' §1.4 distribution to the letter".
    CONFIRMED.
    - S3 :20 asks for "absdiff in nats and rel: min, quartiles, median, max; the counts above TAU and TAU/4; R3's bound".
    - DRV at HEAD computes:
      - the counts above TAU and TAU/4 (:576–577);
      - margin {min, median, p90, max} (:583–584);
      - rel {median, max} (:585);
      - label {median, max} (:586).
    - Fixed-string greps: "quartile" (case-insensitive) 0 lines; "percentile" 0; "quantile" only :583 (p90) and :1024 (a self-test label).
    - So neither absdiff nor rel has quartiles, and rel has no min.
25. Implied by :87–88: the committed driver carries no `backend-ext-2`.
    CONFIRMED. "backend-ext-2", "backend_ext_2", "ext-2" and "ext2" (the last two case-insensitive) give 0 lines in DRV.
26. D1 :89, "(`--resume --ruling p01=PATH`, with the ruling raw of `3b2b855`)".
    CONFIRMED.
    - RUL :3: "The ruling raw for `--resume --ruling p01=<this file>`".
    - DRV :70 ("``--resume`` with ``--ruling PAUSE_ID=PATH`` continues, skip-only") and :1353–1354.
    - 3b2b855 adds RUL.
27. D1 :93–97, "Then come:" `backend-ext-2`, if needed; the `fidelity-ceiling` kind in the runner and the schema, in a follow-up commit settled with n-analyzer; the extension's entry; LOCK-n v0.1, drafted to the seat.
    CONFIRMED as to content and order. The relay clause is item 23.
    - A2 :48 (3): "…; §4.1's second run if the convention is not "bare"; the `fidelity-ceiling` kind in the runner and the schema (a follow-up schema commit settled with n-analyzer …), the pin moving as before; the extension's entry".
    - A2 :48 (5): LOCK-n v0.1 "drafted to the seat". SAVED :14.

E10 — D1, new text (PASS2_COUNTS skipped)
28. D1 :101–102, "Each brief quoted the list of record v2's items 1–5 with C.2's amendment, the briefs' two lines and the `data/mf3` exclusion", as to this pass.
    CONFIRMED.
    - This brief quotes items 1–5, which match LOR :18–22, with C.2's sentence for item 4.
    - It carries "A git command in a check takes item 3's pathspec plus ':!data/mf3/**', even for a named file" and "A glob is expanded and read before it is looped over", and the `data/mf3` exclusion for every git command.
29. The same, as to pass 1's brief.
    NOT CHECKABLE: that brief is not in the repo or the named folders. P1 attests the glob line (:124, "this check's brief carries it") and the commit-time rule (:262), and its not-done list is at :45–50.
30. D1 :103–105, pass 1's scope; "95 items: 76 CONFIRMED, 7 IMPRECISE, 0 FAIL and 12 NOT CHECKABLE, with 12 observations".
    CONFIRMED.
    - P1's sections D1–D4 (:52–434), its item 68 (:327–328) and its TOTALS (:478).
    - My recount by tool: 76/7/0/12 grade lines, 95 numbered items and 12 observations.
31. D1 :106, "Every IMPRECISE item is applied, and so are observations 2–9 and 12."
    CONFIRMED.
    - IMPRECISE items: 12 → D1 :28–29; 14 → D1 :34; 24 → D1 :65; 87 → RC :494–495; 88 → RC :497–499; 90 → RC :504; 94 → RC :511–513.
    - Observations: 2 → D1 :9 and :57; 3 → D1 :62–63; 4 → D1 :81–82; 5 → RC :480; 6 → RC :491; 7 → RC :515–518; 8 → D2 :42–43; 9 → D2 :27–28; 12 → D1 :27.
    - Items 5 and 54 grade two of the applied texts against their sources.
32. D1 :106–108, "Observation 10 is the tooling reading above. Observation 1 concerned the brief's own line number, and 11 pre-checked the commit-time count; neither needed text."
    CONFIRMED. P1 :438, :447–453 and :454–458.
33. D1 :109–110, "After pass 1, the coordinating session added its own departure to the close line and v2e's place to "What runs now"."
    CONFIRMED as to the texts.
    - P1's D2 items (:221–290) hold no such bullet, and P1's items 35–37 (:199–208) quote "What runs now" without v2e.
    - D2 :33–41 and D1 :86–91 now hold them. The order in time is LIST's (E9, E12).
34. D1 :111, "Pass 2 checked the edits after pass 1 and those additions".
    CONFIRMED (this check). See observation 5.

E11 — D2 (fixes P1 obs 9; stands)
35. D2 :27, "It was first applied in `3b2b855`'s window, before that commit".
    NOT CHECKABLE. 3b2b855's message records the ruling ("the home-folder path left, with a commit-time count") but no run of it. My re-run over its diff (item 37) gives 0, which is consistent.
36. D2 :27–28, "and again in this commit's window, counting 0 both times".
    NOT CHECKABLE: the commit is still to come. Pre-check: observation 6.
37. D2 :28, "The values-check re-ran it over `3b2b855`'s diff and counted 0."
    CONFIRMED.
    - P1 item 53 (:264–267).
    - My re-run of D2 :19's form over bfc869f..3b2b855 gives 0. That diff carries both of the commit's files (2 file headers), so the 0 is not vacuous.

E12 — D2, new text
38. D2 :33–34, "A departure of the coordinating session's own, found by the pod session's values-checker (its observation 1)".
    CONFIRMED.
    - PODVC :79 (observation 1, "Possibly undeclared departure"): the count runs "over the staged copy …N1-V__none__0.json. That is a content search of a copied ckpt file. … The request asked for the count (relay_copyback:11)".
    - PODVC :15 attributes the count to the coordinating session's relay, "which by its own statement added it". POD/close.md :60–61 names the departure "the coordinating session's as well as this session's".
39. D2 :34, "and described in the pod session's close line on `6df2131`'s entry".
    CONFIRMED as to POD/close.md :56–61 (the final text). See observation 1: that line is not in the tree.
40. D2 :35–36, "Relaying n-build's copy-back request for the report and the cell", with the two quotes "Report each file's address/port count" and "The ckpt file is never opened, catted or searched".
    CONFIRMED.
    - POD/relay_copyback.txt :2 ("n-build's copy-back request for the run of record's two outputs, relayed") and :5–6 (the report and the cell).
    - :11 has both quotes verbatim; the second continues "; its digest and the count are all that is taken".
41. D2 :35–36, "this session added … beside its own …".
    NOT CHECKABLE. n-build's request as first sent is not among the sources. POD/close.md :58–60 and PODVC :15 rest on the coordinating session's own statement.
42. D2 :37, "The count is a content search over a copied ckpt file, which the list of record v2's item 2 bars."
    CONFIRMED as a reading.
    - LOR :19: "no `cat`, `head`, `tail`, `json.load`, editor or search over them".
    - S3 :48 restates item 2's form for copies, as to listings. PODVC :79: "§7 (S1:48) reads item 2's form as reaching copies". POD/close.md :60.
    - The staged copy kept the `data/n/ckpt/` path under its staging folder (PODVC :79).
43. D2 :38–39, "The pod session's copy-back script ran it once, over the two staged copies on the laptop … It printed only the counts, each 0."
    CONFIRMED.
    - POD/close.md :56–57: "One content search over a copied ckpt file, in the same script: the address/port count (`grep -cF`, `grep -cwF`) over both staged copies, the cell's included. It printed the two counts and nothing else."
    - :41: "The address/port count was 0 and 0 in each". :47–48 places the copies in a scratch folder on the laptop.
44. D2 :38–39, "with the checkout at `ad856f0`".
    CONFIRMED by history.
    - 6df2131's parent is ad856f0 (`%p`).
    - 6df2131's entry records the copied report and cell (RESULTS.md :178, :180). STOP :24 has the cell "copied back by hash", and both digests in STOP :216–217 equal POD/close.md :39–40 (fixed-string matches).
    - The run of record ran from ad856f0, and POD/close.md :35 puts the copy-back after the diagnostic's end.
45. D2 :40–41, "For the seat to class. From here, this session's relays ask for no count or search over a ckpt file or a copy of one."
    NOT CHECKABLE: future conduct.

E13 — D2 (fixes P1 obs 8; stands)
46. D2 :42–43, "(gitleaks 8.30.1, the one on the laptop's path; its output does not print its version)".
    CONFIRMED.
    - `gitleaks version` on the path prints 8.30.1.
    - P1 obs 8 (:445): the version is the push record's header line, and gitleaks' output lines print none.
    - The note's own C.5 line carries the same caveat (NEW :510–511).

E14 — RC (fixes P1 obs 5; stands)
47. RC :479–480, "One sentence from the seat would close it. The checker placed that sentence in §2.2 or §4.1".
    CONFIRMED. RC :380: "One sentence in §2.2 or §4.1 would close this."
48. RC :480, "with the addendum committed as placed, the lock is where it can go."
    IMPRECISE (minor).
    - A2 is unedited (RC :452–453), and LOCK-n v0.1 declares C (A2 :36), so the lock is one place for the sentence.
    - But the seat also rules by raws: RUL is one, and RC :463–464 says "a regrading would come as a ruling".
    - The sentence concerns the resume's comparison, which runs before the lock is drafted (A2 :48, (3) before (5)).
    - Fix: "…; with the addendum committed as placed, it can go in the lock or in a ruling. A ruling would reach the resume's comparison, which runs before the lock."

E15 — RC (fixes P1 obs 6; stands)
49. RC :491, §3's "Where it drops more than half of an arm's reads at a point".
    CONFIRMED. A2 :30 matches by fixed string (1), capital W included.

E16 — RC (fixes P1 87 and P1 88; stands)
50. RC :494, "p0, C and the median rel come from 24 N1-V shadows at d = 0."
    CONFIRMED. REP observation 7 (RC :409).
51. RC :494–495, "p0 and C bind the re-computed reads at every dose, and the median rel sets the descriptive second row."
    CONFIRMED.
    - A2 :24: the ceiling applies "On every re-computed read, at any dose". A2 :18 is the binomial on p0.
    - n :77: re-computation at d ∈ {0, +1, −1} and on "a 10% keyed sample of the other points".
    - A2 :30: the second row is "descriptive …"; "Neither row gates anything".
52. RC :497, "Observations 3 and 8–10 concern wording or the reasoning behind §5."
    CONFIRMED.
    - RC :394 (3): "These differ in wording, not in figures".
    - :411 (8); :417 (9): "This bears only on §5's rationale"; :419 (10): "Wording differences".
53. RC :497–498, "Observation 11 notes that §6.1 does not list n §3 among the sections changed, though §4.2 adds to LOCK-n v0.1's contents."
    CONFIRMED. RC :424.
54. RC :498, "Observation 12 records that the figures agree."
    IMPRECISE (minor).
    - RC :426: "Apart from observations 1, 3 and 10, S3, RUL and the addendum agree on every figure I checked". Observation 1 is a substantive mismatch on the tolerance.
    - Fix: "Observation 12 records that, apart from observations 1, 3 and 10, the figures agree."

E17 — RC (fixes P1 90; stands)
55. RC :504–505, "piped to a fixed-string grep for `2026-11-18_n-step4` (this date's n step-4 raws), which printed 18 names".
    CONFIRMED. RC :442: "`/usr/bin/grep -F '2026-11-18_n-step4'`. It printed 18 names". See observation 7.

E18 — RC (fixes P1 94; stands; ANCHOR_A and ANCHOR_B skipped)
56. RC :512–513, "adds lines at the Log's head and under `25c9340`'s note, which moves them".
    CONFIRMED.
    - The hunks are 23a24,139 (after HEAD :22 "## Log — Phase 2" and its blank line) and 409a526,571 (after the note's last line).
    - Both lie above both anchors. HEAD :610 "(82)" is NEW :772, and HEAD :11510 "D_n = 2026-12-15" is NEW :11672: a shift of 162.

E19 — RC (fixes P1 obs 7; stands)
57. RC :515–518, the values-check of "this raw's header and §2, of §1's byte-identity with the report's copy, of the … entry, of the … close line … and of the PI-routing raw".
    CONFIRMED.
    - P1's D1–D4 and its item 68.
    - The byte-identity holds by my own cmp: RC :19–448 = REP. See observation 5.

E20 — VC, new text (ANCHOR placeholders skipped)
58. VC :1, "ADDENDUM-n2 v0.1 — COMMITTED: the blind values-check, two passes (PI date 2026-11-18)".
    CONFIRMED as to form: RC :1's pattern. The pass-2 section is still to be added (observation 5).
59. VC :3–4, "Two fresh blind checkers, subagents of the coordinating session".
    NOT CHECKABLE. This brief calls this pass "a fresh, blind values-checker (pass 2)".
60. VC :4, "checked the texts this commit adds".
    IMPRECISE (minor).
    - The commit also adds A2, which neither pass checked (it had the referent check), and RC §1, checked only for byte-identity.
    - D1 :103–105 states pass 1's scope exactly.
    - Fix: "checked Code's texts that this commit adds; the addendum had the referent check, and the reports were checked for byte-identity".
61. VC :5–9, the briefs' contents: items 1–5 with C.2, the two lines, the `data/mf3` exclusion and no listing of `results/raw`, no interpreter.
    CONFIRMED for this brief. Pass 1's half is item 29.
62. VC :11–12, "Each result is byte-identical to the unindented copy of the report that the session's record also holds."
    CONFIRMED for pass 1: VC :22–499 is cmp-equal to P1 (478 lines). Pass 2's copy is to come.
63. VC :11, "as its hand-back message gave it, with the harness's two-space indent removed".
    NOT CHECKABLE.
64. VC :12–13, "Neither report held a local path."
    CONFIRMED for pass 1. P1 has 0 lines with the home-folder prefix. Its one line holding "/Users/", "/private/" and "/tmp" (P1 :331) names them as search patterns. This report holds none.
65. VC :15–17, "The reports name the coordinating session's scratch drafts: RESULTS.new …, entry2.md, close_25c9340.md, pi-routing-saved.txt, pi-routing-raw.md, refcheck_raw.md, report.txt, and the previous push's record."
    IMPRECISE.
    - True of P1 (:20, :24–26), and the RESULTS.new gloss is right: two hunks only.
    - This report also names the scratch edits_after_pass1.md, vc1/report_vc1.txt, rc_tail.md and vc_raw.md, and the pod session's three scratch files.
    - Fix: add those names, with the pod session's folder by description.
66. VC :17–18, "Their line numbers index the drafts each pass read. The committed texts are the drafts after the dispositions below."
    CONFIRMED. P1's D1 range (NEW :24–109) is now :24–139.
67. VC :503–512, the seven IMPRECISE dispositions.
    CONFIRMED. Each line matches the applied text: 12 (D1 :28), 14 (D1 :34), 24 (D1 :65, the quote exact), 87 (RC :494–495), 88 (RC :497–499), 90 (RC :504), 94 (RC :511–513).
68. VC :514–524 and :535–536, observations 1–9, 11 and 12.
    CONFIRMED against P1 :438–459 and the draft texts: 1 needs no text; 2 → D1 :9 and :57; 3 → D1 :62–63; 4 → D1 :81–82 (A2 :34); 5 → RC :480; 6 → RC :491; 7 → RC :515–518; 8 → D2 :42–43; 9 → D2 :27–28; 11 → P1 :454–458; 12 → D1 :27.
69. VC :525–532, observation 10's counts.
    CONFIRMED by re-run at HEAD 3b2b855 on git 2.39.5: no exclusion 1; the three forms 0 each; beside CLAUDE.md 2; CLAUDE.md alone and DRV alone 1 each; `git log --format=%h` and `git diff --name-only bfc869f 3b2b855` 1 each.
70. VC :525–526, the lead-in "The ruling raw (…) was named alone:".
    IMPRECISE (minor). The bullets at :530–531 are not lone-raw runs: the raw beside CLAUDE.md, CLAUDE.md alone, and DRV alone.
    - Fix: "The counts, with the ruling raw named alone unless a bullet says otherwise:".
71. VC :538–546, the checker's departures, and "None of them read anything under `data/`."
    CONFIRMED.
    - P1 :463–497 (DEPARTURES 1–5): seven commands counted through wc -l; two rev-list --count; %ad in two log calls and one show; two ls-tree calls refused, one printing git's fatal line; zsh built-ins.
    - P1 :467: "Nothing under data/ was named or printed"; P1 :47.

OBSERVATIONS

1. D2 :33–34 cites the pod session's close line on 6df2131's entry (POD/close.md, final at 18c8267c…332c).
   - That line is in neither HEAD's RESULTS.md nor RESULTS.new. The pod close lines there are older: HEAD :991 (the box answers) and :3171 (2026-11-16).
   - Unless it lands before or with this commit, D2 cites a text not yet in the tree.
2. D1 :57–58 says the six observations "went to the n sessions", and RC :469–470 says each "was sent to the session it touches".
   - RC :494–495's observation-7 bullet ends "For the seat." and names no session; observation 1's bullet (:471–480) names none either.
   - One of the texts could say whether 7 went to a session.
3. A2 §4.1 (:34) and S3 :28 place `backend-ext-2` "in the same session", and A2 adds "One load and 24 reads".
   - D1 :94 runs it "on the coordinating session's relay after the resume's outputs are read", and POD/close.md :18–19 says it "does not chain".
   - Whether a separate invocation after that read is "the same session" is the seat's. D1 :88's "for the seat to strike" is attached to v2e's printing and `backend-ext-2`, not to this.
   - Likewise, the earlier copy-back relay planned the resume in the run's copy: "Nothing is moved or changed in it, because the resume runs there" (POD/relay_copyback.txt :10). D1 :89–90's fresh copy is the later route (POD/close.md :12–15).
4. D2's new bullet (:33–41) concerns 6df2131's copy-back, not the home-folder note that the close line's heading (:1) names. D1 :109–110 points to it. A reader of 6df2131's entry would reach it only through the pod session's close line (observation 1).
5. Pass 2 also checked VC's header and §2 (LIST E20). Neither D1 :111 ("the edits after pass 1 and those additions") nor RC :515–518 names them. VC has no pass-2 section yet, and its title (:1), "Each report" (:11) and "Neither report" (:12–13) presuppose this report and its dispositions.
6. Pre-check of the commit-time count (D1 :114–115; D2 :27–28):
   - The home-folder prefix counts 0 in D1, D2, rc_tail.md, RC, VC, REP, the scratch pi-routing-raw.md and A2.
   - NEW has 1 such line, the same as HEAD's RESULTS.md. Its two hunks, with three context lines either side, count 0.
   - This report holds none, but the staged values-check raw must be counted with the rest.
7. RC :505–506 breaks after "Under" ("which printed 18 names. Under" / "item 5, this matters …"), unlike the paragraph's other lines. Cosmetic.
8. D1 :27 sends items 1–4 to the n-build and pod sessions. Item 4 (SAVED :15) ends "[as ruled; the push yours]", and S3 :51 addresses the block to the PI. So the cell's push is the PI's word, carried by item 8 ("the cell included", SAVED :23). D1 :29 covers it.

DEPARTURES (checkout HEAD 3b2b855 throughout)

1. One `git ls-files` on RUL named alone with no exclusion: E4's first test.
   - The brief's E4 clause let me re-run it, but it is outside the rule that a git command takes item 3's pathspec and `':!data/mf3/**'` even for a named file.
   - Printed: 1.
2. One `git ls-files` on RUL under `':!data/**'` alone (item 3's third form, E4's case), without the literal `':!data/mf3/**'`, which `':!data/**'` covers. Printed: 0.
3. For the seat to class: two commit messages read whole with `%B`, each with the full pathspec, where item 1 names ids, subjects and commit times for `git log`.
   - 3b2b855's, in a `git show --name-status`: printed the message and its two raw names.
   - 6df2131's, in a `git log -1` piped to a fixed-string grep: printed one name from the message, the stage report's committed name (`data/n/reports/backend-ext.json`). That is a name only; nothing under data/ was opened or listed.
4. For the seat to class, as to scope: four `git diff` runs over `.` for bfc869f..3b2b855 under item 3's pathspec and `':!data/mf3/**'`, which is the commit-time count's own form.
   - The runs: --name-only; the count `grep -cF -- "$HOME"`; `wc -l`; a count of file headers.
   - Their scope includes data/ paths outside the excluded folders, but the range touches only two results/raw files.
   - Printed: 2; 0; 89; 2.
5. For the seat to class, under the no-interpreter rule: shell syntax only. That means cd, echo, command substitution, brace groups feeding `uniq | wc -l` to compare two digests, pipes, `&&` and `;`. There was no loop, `test`, `[[ ]]`, arithmetic or function.

TOTALS: 71 items: 55 CONFIRMED, 6 IMPRECISE (5, 48, 54, 60, 65, 70), 0 FAIL (none), 10 NOT CHECKABLE (3, 18, 23, 29, 35, 36, 41, 45, 59, 63), and 8 observations.

## 4. Pass 2: dispositions

**The six IMPRECISE items, each applied in the checker's sense:**
- 5: item 7 is carried by `3b2b855` (its two raws) and by this commit (the addendum after its referent check, with
  item 7's other rulings) (the entry).
- 48: the closing sentence can go in the lock or in a ruling, and a ruling would reach the resume's comparison, which
  runs before the lock (the referent-check raw's §2).
- 54: observation 12 records that the figures agree apart from observations 1, 3 and 10 (the referent-check raw's
  §2).
- 60: this raw's header says the checks covered Code's texts, the addendum having had the referent check and the
  reproduced reports a byte-identity check.
- 65: this raw's header names pass 2's further files, with the pod session's folder by description.
- 70: observation 10's lead-in says the ruling raw is named alone unless a bullet says otherwise (§2 above).

**The observations:**
- 1: the close line says the pod session's line lands in the commit after this one.
- 2: the referent-check raw's §2 says which sessions were told of observations 1 and 7.
- 3: the entry's `backend-ext-2` bullet says it is a separate invocation in the same box session, on the same
  characterized backend, and that reading this as §4.1's "in the same session" is Code's reading, for the seat.
- 4: the close line's heading names its departure.
- 5: the entry's values-check paragraph names pass 2's whole scope, and this raw now holds pass 2's report and its
  dispositions.
- 6: a pre-check of the commit-time count. The count at the commit is the gate's.
- 7: the line break after "Under" is closed (the referent-check raw's §2).
- 8: no text needed. The entry already says that the push, the cell included, waits for the PI's word.

**The checker's departures**, as its report states them, for the seat to class:
- one `git ls-files` on the ruling raw with no exclusion, and one under `':!data/**'` alone, both re-running Code's
  test;
- two commit messages read whole with `%B`, one printing the stage report's committed name, a name only;
- four `git diff` runs over `.` for `bfc869f..3b2b855` under the commit-time count's own pathspec;
- shell syntax only, with no interpreter.

None of them opened anything under `data/`.

**The edits after pass 2** were checked by tool: each "after" text found once in its draft, each "before" text gone.
The assembled RESULTS.md was rebuilt from HEAD's with the two insertions and compared by `cmp`.
