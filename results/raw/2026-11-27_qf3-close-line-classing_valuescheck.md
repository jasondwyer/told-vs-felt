# The F3 session's close line on the Q-F3 campaign entry (`b449ed6`), for the seat's classing of its five items: the blind values-check (its brief, the checker's report, Code's dispositions)

*F3 session, Code's date 2026-11-27, HEAD `7ab1cf6`. One blind pass, by a subagent under the brief below, which
quotes the list of record v2's items 1–5. The brief gave the checker the PI's routing's section A verbatim, from the
coordinating session's relay. The draft it checked is 39 lines, sha256 `cdf75cb0…f7c2`. The close line as sent applies
every finding.*

*Three scrubs apply below:*
- *local roots are written `<repo>` and `<scratch>`;*
- *the campaign folder's plain name is written `m[f]3`;*
- *nothing else in the brief or the report is changed.*

*The brief's sha256 as given to the checker, before the scrubs, is `34e11a85…b949` (61 lines). The report's sha256,
over the text as the checker returned it, is the checker's own: `3356ca97…78f7` (169 lines). Code re-derived it from
the checker's hand-back. The scrubbed report below is `0cdf912f…530a`. Code's dispositions follow it.*

----------------------------------------------------------------------------------------------------
The brief (verbatim; scrubbed as stated above)
----------------------------------------------------------------------------------------------------
You are a blind values-checker for a research project's records, in the git repository at <repo>. Other sessions share this working tree and may commit while you work; do not modify it.

You are read-only:
- no git writes of any kind (no add, commit, stash, checkout, reset, worktree or switch; `git hash-object` only without `-w`);
- no file written or edited anywhere;
- no model run, and no run of any repository script in any form;
- no Python at all, not even `python3 --version`: shell utilities only (jq, awk, sed, /usr/bin/grep, shasum, diff, cmp, wc -l, sort, uniq, git).

Return your report as text in your final message, between a line `=== BEGIN REPORT ===` and a line `=== END REPORT ===`, and give its sha256 (over the text between the markers, as UTF-8, ending in one newline), computed in the shell, for example by a quoted here-document piped to `shasum -a 256`. Write it to no file.

## The list of record v2, items 1–5 (verbatim; they bind you)

1. **Permitted (names, ids, digests):** a bare `git status --porcelain`; a name-only `ls` (no `-l`, `-t`, `-s`, `-la`); `git ls-files`; `git ls-tree --name-only`; `git diff --name-status` and `--name-only`; `git show --name-only` and `--name-status`; `git log --name-only`; `git log` with `--format` of ids, subjects and commit times over any path; `shasum`/`sha256sum` and any program's digest that prints no byte, size or time; `git rev-parse <rev>:<path>` compared in the shell; `git check-attr`; a `find` that prunes every `*/ckpt` and `*/reports` directory (`find … \( -path '*/ckpt' -o -path '*/reports' \) -prune -o … -print`).
2. **Content.** Files under `data/*/ckpt` (the checkpoints and call logs) are read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4: no `cat`, `head`, `tail`, `json.load`, editor or search over them. Files under `data/*/reports` are the read domain (m:271; the stage writes them redacted) and may be read for their content by Code and by the seat — for a stage entry's figures, a declared counter, or a read — with nothing from them printed into a raw beyond what the entry's form reports. **Metadata:** no size or time of either directory or any file in them, in any form (`--stat`, `--numstat`, `ls -l/-t/-s/-la`, `du`, `wc -c`, `stat`, `git ls-tree -l`, `git cat-file -s`, any unpruned `find`, `mdfind` over them).
3. **Content searches** over a checkout or a tree — `git grep`, recursive `grep`, `rg`, `mdfind -onlyin`, and the pickaxe (`git log -S` / `-G`) over any range — exclude the checkpoint and report files with a form tested on this git: `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` (equivalently `':(exclude,glob)data/*/ckpt/**' ':(exclude,glob)data/*/reports/**'`, or `':!data/**'` where nothing under `data/` is wanted), or the prune for `find`-driven greps. The bare `':!data/*/ckpt'` form is not an exclusion on git 2.39.5 and is not used. A pickaxe search without the pathspec can name a commit whose checkpoint matched, which is content; it is a departure.
4. **The pre-push screen** may read every file in the range, `ckpt` and `reports` included, and prints only a per-class verdict, range totals, and one line per distinct match outside those directories; a match inside one is a count by path class and a halt for the seat.
5. **A running stage:** the end-wait is on the PID alone (O3-1); no `stat`, listing, `tail`, `Monitor` or read of its raw, checkpoint or reports until the invocation has ended — in every session, including the coordinating one.

In practice, for this task:
- You need nothing under `data/`: open, read, list, size or traverse nothing there.
- Every content search over the checkout or a tree carries item 3's tested form, here `':!data/**'`. `grep -r` and `rg` exclude the `data` directory.
- Use no `--stat`, `--numstat` or `--shortstat` form anywhere.
- Do not open the campaign's raw `results/raw/2026-11-15_m[f]3-campaign-qf3.txt`: the unit is before its VERDICTS. You need it for nothing here.
- Do not open anything under `<scratch>/../tasks/`, any session transcript (`*.jsonl`), or any memory folder.
- The Bash tool's `grep` is ugrep: use `/usr/bin/grep`.
- No clock time, time stamp or span in your report.

If you break any of this by accident, say so at the end of your report: give the command's kind and what printed, without reproducing anything that printed.

## What to check

Code (another session) has drafted a close line for RESULTS.md, to be appended right after the last line of a dated entry. Nothing is committed yet. Check every factual claim in it against its sources: every quote, figure, hash, path, commit id, date and attribution.

The draft: `<scratch>/a6/close2/close_b449ed6.md`. It is to be appended after the last line of the RESULTS.md entry that begins "- 2026-11-25 — **THE Q-F3 CAMPAIGN" (at HEAD `7ab1cf6`, lines 789–1084; its last line is "    - The push of this commit waits for the PI's word.").

The sources:
- **The seat's raw (E),** `results/raw/2026-11-27_qf3-items-and-departures-classing_design-to-code_answers.md` (untracked; sha256 claimed in the draft), read whole.
- **The PI's routing, relayed by the coordinating session.** It is not in the repository; its words, verbatim, are the only source for the items they bear on. The relay calls it "The PI's routing of the seat's classing of the Q-F3 campaign entry's five items (PI date 2026-11-27)", and gives the PI's own words below the block as "Route as given". Its section A, verbatim between the two lines of dashes:

----------
A (Q-F3 / m — raw (E) §1, the b449ed6 entry's five items for the seat):
9. Items 1, 2 and 5 inert, with the form notes for the coordinating session's brief (a running stage's kit excluded from scratch cleanup and hashed into the launch note; the end-wait writes its own end line) [inert].
10. Item 3, the withheld count at the campaign's end: a departure in form from m:263, m:318's look form and LOCK-m-F3:316's end-notice form; contained in two Code sessions, relayed to no one; inert as to the verdict (campaign complete, analyzer frozen at G-ANL-F3, POSTING v1 the PI's); a strike in form; no re-run, nothing rewritten; the fix for the brief now and the list of record's next version (end notice = "ended" + exit status; no per-arm extraction from a contrast unit's raw before its VERDICTS); one disclosure line in the Q-F3 VERDICTS entry's "for the seat" and Appendix D [strike in form; carry].
11. Item 4 (the run list's timing and scope) after VERDICTS, as owed [defer].
12. Code commits raw (E) by path; the f3 session's close line on b449ed6's entry [route].
----------

- **RESULTS.md** at HEAD: the entry the close joins (lines 789–1084 at `7ab1cf6`), and the instruct VERDICTS session's close line whose form the draft follows (it begins "  - **The reads' close (PI date 2026-11-26; the seat's VERDICTS read, §6).**", line 13945 at `7ab1cf6`).
- **The record's commit,** `b449ed6`, and its values-check raw `results/raw/2026-11-25_m[f]3-campaign-qf3_valuescheck.md` (for the placeholder names it quotes).
- **The gate files of that commit window** (Code's scratch): `<scratch>/a6/record/gate_qf3.sh` (the first version) and `<scratch>/a6/record/gate_qf3_v2.sh` (the second), read whole.
- **Not in the repository (grade NOT CHECKABLE unless a record bears on it):** that the first gate stopped at its pre-add phase with nothing staged, that v2's hash was sent and that it ran on the coordinating session's word, and Code's reads and digests of the campaign's report and checkpoint after the end. The coordinating session's word asking for the window's declarations is also not in the repository.

Pay special attention to:
- whether each quote is verbatim: the routing's items 9–12, and each phrase the draft quotes from raw (E), with the section it names;
- the sha256, the link's path, and the `git log --diff-filter=A` form;
- whether the draft states anything as a rule or a precedent that no record states, or says more than the routing and raw (E) say;
- the claims about the two gate versions, against the gate files and the values-check raw;
- no clock time, time stamp or `$` figure in the draft (file:line anchors such as `m:263` are not clock times);
- line widths: no line over 120 characters except the verbatim block quote and the link line.

Grade each claim CONFIRMED, IMPRECISE (true in substance, but the wording or anchoring is off; say the fix), FAIL (wrong; say what is right) or NOT CHECKABLE (say why). Number your items and give file:line evidence. End with a tally and the list of everything not CONFIRMED. State HEAD (`git log --format='%h' -1`) at your start and at your end.
----------------------------------------------------------------------------------------------------
The checker's report (verbatim; scrubbed as stated above)
----------------------------------------------------------------------------------------------------
Blind values-check: the F3 session's draft close line on the b449ed6 entry (close_b449ed6.md)

Start: the brief's sha256, 34e11a853524ac5233f7b6d993e6afa5d7efe75bc21922b189044136dc96b949, equals the given value; brief read whole. The draft's sha256, cdf75cb01871039bc7f760e31d5122caba1c0299a08c3ba057fd3ae70796f7c2, equals the given value (39 lines, ending in a newline) and was unchanged at my end. HEAD at start: 7ab1cf6. HEAD at end: 7ab1cf6.

Anchors:
- D:n = the draft's line n.
- E:n = raw (E), results/raw/2026-11-27_qf3-items-and-departures-classing_design-to-code_answers.md (untracked, 58 lines), read whole.
- R:n = RESULTS.md at 7ab1cf6 (the working tree's blob id is equal, 0077d26b548ee3d96f03f7e1f73b2ddccd6f7845).
- VC:n = results/raw/2026-11-25_m[f]3-campaign-qf3_valuescheck.md (committed at b449ed6; the working tree's blob id is equal; 580 lines; sha256 7cf2599213c3b4b67e05cbbd032f92537eed898d6a8195811fab334b28892c50).
- G1:n = gate_qf3.sh (110 lines, sha256 83300a14d81c1842fb9f43342e09db88e4c0f286e796c4d2b470c238d208ccc3), read whole.
- G2:n = gate_qf3_v2.sh (115 lines, sha256 5333cc1177b8e018626da643eaf236eb351f967933047d6e27b979ac85de37ce), read whole.
- B:n = the brief's line n (the routing's section A is at B:41-45).

## Items

1. D:1, the heading: PI date 2026-11-27, the seat's classing of the entry's five items, routed. The relay gives "PI date 2026-11-27" (B:38). E §1 (E:13-26) classes items 1-5 of the entry's "For the seat" (R:1046-1079). CONFIRMED.

2. D:1-2, "The seat's raw is committed by path in the commit that adds this line." This is about a commit that does not exist yet. It is consistent with routing item 12 (B:45: "Code commits raw (E) by path; the f3 session's close line on b449ed6's entry") and with E:3. NOT CHECKABLE (future). See O1.

3. D:2-3, "That commit is the raw's first commit, so `git log --diff-filter=A -- <path>` names it". At HEAD the path is untracked (`git status --porcelain`: ??), and no commit in any ref touches it (`git log --all --format=%h -- <path>`: 0 lines). So the commit that adds it will be its first, and that form names it. The path in the code span is exact (fixed-string match at D:3). The form is the one at R:13946-13947. CONFIRMED (as of HEAD; see O1).

4. D:4, the link. The target exists and resolves from the root, where RESULTS.md sits. The link text is the basename without its date and extension, as at R:1041 and R:13948. CONFIRMED.

5. D:5, the sha256 69522ee8837e652ca723835d0d95f40ca6687eba867bdba6060390395503a441. It equals `shasum -a 256` of raw (E), at my start and at my end. CONFIRMED.

6. D:5-6, "A commit cannot name its own hash; the next RESULTS entry names it in full." The first clause is a property of git. The second is a commitment, in the words of R:13949-13950. NOT CHECKABLE (future). See O6.

7. D:6-7: the routing (PI date 2026-11-27) gives the entry its section A, items 9-12, and the PI's words below the block are "Route as given". This matches the relay as the brief gives it (B:38-45). CONFIRMED.

8. D:7, "This line is the F3 session's." Routing item 12 names "the f3 session's close line on b449ed6's entry" (B:45). RESULTS.md spells it "F3 session" (28 lines; "f3 session": 0), and both gate headers say "(F3 session)" (G1:2, G2:2). CONFIRMED.

9. D:8, "The routing's section A, verbatim:". The block carries items 9-12 but not the section's header line (B:41), "A (Q-F3 / m — raw (E) §1, the b449ed6 entry's five items for the seat):". IMPRECISE. Fix: "The routing's section A, items 9-12, verbatim:", or add the header line.

10. D:10-13, the block quote. With the six-space "> " prefix stripped, `diff` against B:42-45 prints nothing: items 9-12 are byte-identical. D:9 and D:14 are blank. CONFIRMED.

11. D:15, "Items 1, 2 and 5: inert (the raw's §1)." E:15 has "**Inert.**", E:16 "**Accepted; inert.**" and E:26 "**Inert.**"; routing item 9 has "[inert]". CONFIRMED.

12. D:15, "Two form notes bind the coordinating session's briefs from here." The count matches: routing item 9's parenthetical names two notes, and E §1 labels two (E:15, E:26). But the sources say the notes are "for the coordinating session's brief" (B:42; E:15): singular, with no "bind" and no "from here". The draft says more than either. IMPRECISE. Fix: "Two form notes go to the coordinating session's brief (routing item 9):". E:8 (§0) says "a form note each"; see O4.

13. D:16-17, item 1's quote. It is a verbatim prefix of E:15's form note (fixed-string match), ending just before ", so that a loss afterwards costs the record nothing". CONFIRMED.

14. D:18, item 5's quote. Both parts are verbatim at E:26, in that order. The "…" stands for ", as G-READ-n's step script v2 does ("ended; polls off AC power: 0"),". CONFIRMED.

15. D:19, item 2's quote. Verbatim at E:16, period included. CONFIRMED.

16. D:20, "Item 3: a strike in form, carried (the raw's §1 item 3)." E:22 has "*Class.* **A strike in form**"; routing item 10 has "[strike in form; carry]". CONFIRMED.

17. D:20-21, "inert as to the verdict" and "no re-run, nothing rewritten", cited to the raw's §0. Both are verbatim at E:7 (§0), and both also appear at E:49 (§5). CONFIRMED.

18. D:22, "The raw's fix binds from now:". E:23 scopes the fix "for the coordinating session's brief now and the list of record's next version when one is issued", and routing item 10 says "the fix for the brief now and the list of record's next version". "Binds from now" drops that scope and reads as binding everywhere, including the list of record's part, which waits for its next version. IMPRECISE. Fix: "The raw's fix, for the coordinating session's brief now and the list of record's next version when one is issued:".

19. D:22-25, the fix's quote. Verbatim at E:23 (fixed-string match, including the em dash, the inner "ended", "LM-F3:316's form" and "(m:318: pooled pre-pick counts per arm)"). CONFIRMED.

20. D:26-27: the Q-F3 VERDICTS entry's "for the seat" carries one disclosure line, and Appendix D carries it beside the campaign's exclusion table. This follows E:24 and routing item 10. CONFIRMED.

21. D:28, "Item 4: deferred. Q-F3's run list stays owed after VERDICTS ("not ruled here", the raw's §1 item 4)." Routing item 11 has "after VERDICTS, as owed [defer]". "not ruled here" is verbatim at E:25 (§1 item 4) and also at E:8. CONFIRMED.

22. D:29, "from this entry's commit window (`b449ed6`)". b449ed6's subject ends "committed by path in the coordinating session's window". CONFIRMED.

23. D:29-30, "declared here on the coordinating session's word". The word is not in the repository (B:51). NOT CHECKABLE.

24. D:31, "The gate's first version stopped at its pre-add phase." G1:5 names `pre` as the phase "before `git add`", and G2:3 records "v1's pre phase refused the values-check raw for "@@"". That header is the run's only attestation; the repository has none. CONFIRMED against the gate files.

25. D:31-32, "A bare `@@` check refused the values-check raw". G1:76-80 loops over the entry and then VC; G1:79 is a fixed-string `@@` count. I replayed G1's pre-phase content checks on the committed bytes:
    - The entry (R:789-1085) has sha256 77245fa7936f8aad46cb18e31e646b2ed839027517ae95e5447affce573ca690, equal to G1:28's pin, and scores 0, 0 and 0 on the `$`-figure, clock-like and `@@` checks.
    - VC is equal to G1:25's sha256 and line pins, and scores 0 and 0 on the first two checks, then 4 lines with `@@`.
    So G1:79 on VC is the first content check to fail. CONFIRMED.

26. D:32-33, "which quotes five placeholder names verbatim from its briefs and reports". VC holds three names, quoted five times in all:
    - `@@RUNLIST@@` at VC:58 (pass 1's brief) and VC:241 (pass 1's report);
    - `@@VCRAW@@` at VC:58;
    - `@@VCTALLY@@` at VC:337 (pass 2's brief) and VC:490 (pass 2's report).
    The briefs and reports are verbatim according to VC:10-12, and G2:3 says "five times". IMPRECISE. Fix: "which quotes three placeholder names, five times in all, verbatim from its briefs and reports", or "five placeholder tokens" as D:34 has it.

27. D:33, "Nothing was staged." This is not in the repository (B:51). It agrees with G1's order: G1:64 asserts that nothing is staged before G1:79 runs. NOT CHECKABLE.

28. D:33, "The fix went out as a new version, gate v2". G2 is a separate file whose header records the change (G2:3-4). `diff` of G1 and G2 shows that only the header and the `@@` checks changed: G1:79 removed, G2:82-85 added. CONFIRMED.

29. D:33-34, "with its hash sent, and ran on the coordinating session's word". Neither is in the repository (B:51). b449ed6 carries exactly the five paths that G2:106 expects (`git show --name-status`), which is consistent. NOT CHECKABLE.

30. D:34, "v2 keeps "no `@@`" for the entry and pins the raw's five quoted tokens." G2:82 requires 0 `@@` lines in the entry, and G2:83 requires 4 in VC. G2:84-85 pin the tally " 2 @@RUNLIST@@; 1 @@VCRAW@@; 2 @@VCTALLY@@;", and replaying G2:84's pipeline on VC gives exactly that string. CONFIRMED. See O3.

31. D:35, "The campaign folder's plain name reached argvs." The records write the folder name bracketed as `m[f]3` (R:3485). All four of the gate's paths hold the plain name: the raw's and VC's file names, and the folder of the report and the checkpoint (G1:17-20, G2:19-22). CONFIRMED.

32. D:35-36, "It stood in the argv of `shasum`, `git` and `cp` in that window, through the gate's paths." By the gate files, the same paths also stood in `/usr/bin/grep`'s argv:
    - G1:77-79 over VC, all three before the refusal;
    - G2:79-80 and G2:83-84 over VC;
    - G2:86 over the raw and VC.
    The records count grep's argv for this form (R:3917, R:4539). The three programs named are right: shasum at G1:29 and G1:66-69, git at G1:70/90/94/104/106, cp at G1:56-57 (the place phase). FAIL as a declaration, because grep is missing. What is right: "the argv of `shasum`, `git`, `/usr/bin/grep` and `cp`". See also O2.

33. D:36-37, "Before the window it also stood in this session's reads and digests of the campaign's report and checkpoint, after the end." This is not in the repository (B:51). NOT CHECKABLE.

34. The same sentence's wording. "reads … of the campaign's … checkpoint" says the checkpoint was read. The record says it was hashed, not opened (R:915, R:1023, R:1039; b449ed6's message: "hashed, not opened"), and a read of it by Code would be a departure from list item 2. IMPRECISE. Fix: "in this session's reads of the campaign's report and its digests of the report and the checkpoint, after the end".

35. D:37, "The campaign had ended, so it barred nothing." No record I found limits the plain-name form to a running campaign:
    - R:2336-2337's standing line states no scope;
    - the list of record v2 raw has no line on plain names or markers;
    - entries after the campaign's end still count the plain name in argvs: R:242 and R:286, in the G-READ-n entry (PI date 2026-11-27).
    As written, the sentence reads as a ruling on the form's scope. IMPRECISE. Fix: attribute it in R:963-966's form for a reading, e.g. "On this session's reading (not a ruling), the campaign had ended, so it barred nothing; for the seat to class", or drop it.

36. D:39, "Not pushed: the push is the PI's." The commit that adds the line does not exist yet. The form matches b449ed6's own message ("Not pushed: the push and VERDICTS wait for the PI.") and R:1084. But b449ed6 is already an ancestor of origin/main (7ab1cf6, the local remote-tracking ref). Placed under R:1084's "The push of this commit waits for the PI's word.", a bare "Not pushed" can be read as being about b449ed6. IMPRECISE. Fix: "Not pushed: the push of the commit that adds this line is the PI's."

37. No clock time, time stamp or `$` figure. `\$[0-9]` finds nothing, and `\b[0-9]{2}:[0-9]{2}\b` finds nothing. The only digit:digit strings sit inside "LOCK-m-F3:316" (D:11) and "LM-F3:316" (D:22), which are file:line anchors. There are no time words. CONFIRMED.

38. Line widths. Only D:4 (the link line) and D:10-11 (the verbatim block quote) are over 120 characters. No line has trailing whitespace, and there are no tabs. CONFIRMED.

39. The anchors inside the verbatim quotes match their files:
    - LOCK-m-F3.md:316 reads "Its end notice carries "ended" and the exit status, with no stamp and no window (v0.2 §8)."
    - PROPOSAL-m v1.11 m:263 holds the `excluded@free` phase-alone form, "the class withheld to VERDICTS".
    - m:318 holds "at looks, pooled pre-pick exclusion counts per arm".
    CONFIRMED.

## Observations

O1. Who commits raw (E). E:56 (§5 item 7) reads "Code commits this raw by path; the coordinating session's close line on `5ceb8dd`'s entry [route]", but routing item 12 (B:45) pairs the raw's commit with the f3 session's close. The routing's section C is not in this brief. If two sessions each commit the raw, item 3's "first commit" holds only for whichever lands first. Worth settling with the coordinating session before the commit.

O2. Outputs. By the gate files' text, the plain name also printed in the gate's outputs:
    - v1's refusal line (G1:14's format with G1:79's message, which names VC's path);
    - the place phase's ok line (G1:60, G2:62);
    - the staged phase's blob lines (G1:92, G2:97).
    The records declare this class (R:1502, R:1543; E:30 classes it among 5ceb8dd's forms). The draft's declaration covers argvs only.

O3. "the raw" means raw (E) at D:15, D:20-22 and D:28, but the values-check raw at D:34 ("the raw's five quoted tokens"). Writing "the values-check raw's five quoted tokens" removes the ambiguity.

O4. The item 2 bullet (D:19) sits under D:15's "Two form notes …", beside the two notes. E:8 (§0) says "a form note each", while E §1 labels only items 1 and 5 "Form note" and the routing's parenthetical names two. Moving the item 2 bullet ahead of that lead sentence keeps the count unambiguous.

O5. D:22-25 nests the source's double quotes ("ended") inside the draft's own double quotes. That is verbatim, but the inner quotes read as closing the outer ones.

O6. The precedent that D:5-6 copies is R:13949-13950. The commit that added R:13945, e114b3a (found by pickaxe), is not yet named in full anywhere in RESULTS.md at HEAD. The sentence could say whose next entry will name the hash.

O7. The draft has no trailing blank line. Inserted between R:1084 and the existing blank line R:1085, it leaves the entry's blank-line end intact.

## Tally

39 items: 25 CONFIRMED, 7 IMPRECISE, 1 FAIL, 6 NOT CHECKABLE. 7 observations.

Not CONFIRMED:
- FAIL: 32 (grep is missing from the list of argvs).
- IMPRECISE:
  - 9: the section A label, but the block omits the header line;
  - 12: "bind … briefs from here";
  - 18: "binds from now" drops the fix's scope;
  - 26: "five placeholder names", where there are three names quoted five times;
  - 34: "reads … of the … checkpoint";
  - 35: "so it barred nothing" stated as a ruling, unattributed;
  - 36: a bare "Not pushed" under b449ed6's entry, which is already on origin.
- NOT CHECKABLE:
  - 2: the raw committed with this line (future);
  - 6: the next entry names the hash (future);
  - 23: the coordinating session's word;
  - 27: nothing staged;
  - 29: the hash sent, and the run on the coordinating session's word;
  - 33: this session's reads and digests after the end.

HEAD at end: 7ab1cf6.

## Departures (mine; nothing printed is reproduced)

1. One pickaxe (`git log -S` with `-- . ':!data/**'`, over all history) searched for R:13945's heading text. Its pathspec did not also exclude results/raw/2026-11-15_m[f]3-campaign-qf3.txt, so git scanned that raw's blob for the string. It printed one commit id and subject (a RESULTS.md commit). Nothing of the campaign raw printed.
2. One `git show --name-status` of b449ed6 (list item 1's form) printed its five paths by name, two of them under data/ (as the entry and the commit message also name them). It printed no content, size or time. The brief's practice line says to list nothing there.
3. One `git log -1 --format=%B b449ed6` printed the whole commit message, which is more than ids and subjects. It is committed text.
4. I used utilities beyond the brief's parenthetical list:
   - cut, tr and head on pipes;
   - tail -c 1 and od -c on the draft;
   - fold on the commit message;
   - printf and echo;
   - name-only ls of Code's scratch record folder (its names include a copy named like the campaign raw, which I did not open), of raw (E)'s path, and of two files at the root.
5. The campaign folder's plain name stood in my argvs through the values-check raw's path (shasum, grep, sed, wc and git), and it printed in my outputs (file names, RESULTS.md lines, the gate files). The brief does not bar this; I state it for completeness.
6. What I did not do: no git write, no file written, no Python, no model, no repository script. Nothing under data/ was opened, read, sized or traversed. The campaign raw, the transcripts, the tasks folder and the memory folder were not opened.
----------------------------------------------------------------------------------------------------
## Code's dispositions

Every FAIL and IMPRECISE item is applied in the close line as sent. The edits after the check were checked by tool:
- the two block quotes, joined at their line breaks, against the relay's items 9–12 and raw (E)'s fix;
- each phrase quoted from raw (E) by a fixed-string match;
- the screens: local roots, ids, the user's name, clock times, guard words, the campaign folder's plain name;
- the widths: only the link line is over 120 characters.

- **FAIL 32:** the declaration now names `/usr/bin/grep` beside `shasum`, `git` and `cp`.
- **IMPRECISE 9:** "The routing's section A, items 9–12, verbatim".
- **IMPRECISE 12:** "Two form notes go to the coordinating session's brief (routing item 9)".
- **IMPRECISE 18:** "The raw's fix, for the coordinating session's brief now and the list of record's next version when one
  is issued (§1 item 3), verbatim".
- **IMPRECISE 26:** "which quotes three placeholder names, five times in all, verbatim from its briefs and reports".
- **IMPRECISE 34:** "its reads of the campaign's report, its digests of the report and the checkpoint".
- **IMPRECISE 35:** "On this session's reading (not a ruling), the campaign had ended, so it barred nothing. Declared as a
  form, for the seat to class."
- **IMPRECISE 36:** "Not pushed: the push of the commit that adds this line is the PI's."
- **NOT CHECKABLE:** each stands as one of these:
  - the commit to come (2 and 6);
  - the coordinating session's word (23 and 29);
  - Code's attestation (27 and 33).
- **O1:** one commit adds raw (E): the coordinating session's, which also places this close line (its word: "my
  commit carries it"). The raw's §5 item 7, "Code commits this raw by path", is that same commit.
- **O2:** applied. The declaration names the gate's output lines: v1's refusal, the place phase's line and the staged
  phase's blob lines.
- **O3:** applied: "the values-check raw's five quoted tokens".
- **O4:** applied. The item 2 bullet now comes before the form notes' lead sentence.
- **O5:** applied. The fix is set as a block quote, so its own double quotes no longer nest inside the draft's.
- **O6:** the instruct session's form stands: "the next RESULTS entry names it in full".
- **O7:** kept. The coordinating session's placement wants the last line a text line, with no trailing blank.
- **The block quotes' widths:** the routing's items 9 and 10 ran past 120 characters. Both quotes are now wrapped at the
  source's own spaces.
- **Beyond the findings,** one widening: the plain-name declaration now covers this session's own argvs since the end
  and its values-checkers'. Before, it named the window's argvs and the reads and digests of the report and checkpoint.
- **The checker's own departures,** as its report states them, for the seat to class:
  - one pickaxe over all history whose pathspec, `-- . ':!data/**'`, did not also exclude the campaign's raw, so git
    scanned that raw's blob; it printed one RESULTS.md commit and nothing of the raw;
  - one `git show --name-status` of `b449ed6`, which printed two paths under `data/` by name;
  - one `git log -1 --format=%B`, which printed the whole commit message;
  - utilities beyond the brief's list;
  - the campaign folder's plain name in its argvs and outputs, through the record's file names.
