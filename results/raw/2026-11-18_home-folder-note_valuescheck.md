# The dated note on the laptop's home-folder path: its blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over the draft dated note. The draft was revised in place after the
check, and its sha256 before the revision was not taken. §1 lists every change.

**The checker's brief:**
- named the sources: the repo at `dc6a1cf`, n-build's N.2 values-check raw, WORKFLOW §1 and §5, the list of record
  v2, ledger (81), the push record and the C.5 form of record;
- barred printing the pattern, any line holding it, or the account name. The checker built the pattern in the shell
  from `id -un`, and its output held counts and names only;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec, plus `data/mf3`'s exclusion,
  on every tree-wide git command;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3` or a `ckpt` or `reports` path, a
  whole-tree `git status`, any `--stat`, any write and any Runpod tool.

**The report** is in §3, extracted verbatim from the subagent's hand-back by script: 70 lines, sha256 `76873881…75b6` as
extracted. One local path is written `<the laptop's path>`; the text below is `ac88c28c…175c`.

**Totals:** 36 items — 26 CONFIRMED, 4 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE — and 10 observations.

## 1. Dispositions

**The IMPRECISE items, each applied in the checker's words:**
- **6** (n-build's confirmation and the class): "never displaying the line"; "its commit does not touch that entry";
  "Observation 13 reads it as the class that ledger (81) addresses".
- **21** (WORKFLOW §5): both sentences quoted whole.
- **23** (reading (a)): the folder layout's reach, by category only.
- **25** (reading (b)): its scope (248 raws, two data artifacts, a proposal, an older entry), no raw edited since
  WORKFLOW v1.0 (`dd0bb89`), and the earlier in-place edits, `c2a6417` among them.

**The observations:**
1. **The release audit's precedent.** Applied, with both raws cited and the caveat that their counts measure a
   different pattern at a different commit.
2. **The screen's reach.** Applied: it is in the coordinating session's scratch, and it has met no instance since
   `16c99d5`.
3. **No commit-time guard for a RESULTS.md entry or a data artifact.** Applied, as a sentence for the seat.
4. **The departure's commits.** Applied: HEAD `b4522ae`, origin/main `fa96ccf`.
5. **The printout.** Applied: the first check printed file names with counts for its first 20 files, then the
   totals.
6. **The occurrences.** Applied: 1,061.
7. **The model manifest's file name.** Not applied. "the model manifest's" stands, as optional.
8. **Line numbers.** No change; the note cites none.
9. **The committed rule.** Applied: WORKFLOW §7's "no whole-tree listing while a stage runs" beside the coordination
   rule.
10. **The checker's own acts.** Noted. They are in its report, read-only.

**The NOT CHECKABLE items (6)** rest on the PI's chat word, the session's own acts and the coordination notes. No
change.

## 2. The edits after the check, checked by tool

- **One overreach removed.** Applying observation 1, the coordinating session first wrote "none was added since the
  release". Its own tool check found 22 of the 252 files dated after the release (2026-11-05 and -06). The sentence
  was replaced by the checked one: the per-file counts are the same at every pushed boundary from `16c99d5` to
  `dc6a1cf` (252 files at `16c99d5`, recounted by tool).
- **Quotes.** Every span was checked by script against WORKFLOW.md, the two N12 raws and the push record: 6 of 8
  found as written, and the two WORKFLOW §5 sentences found once each with the file's bold markers removed.
- **No pattern.** No line of the note holds the pattern, the account name or the bare prefix.
- **Width.** No line over 120 characters outside the links.
- **The final note:** sha256 `24afb2e1…7c08`, 81 lines.

## 3. The report as returned

```text
VALUES-CHECK: the dated note on the home-folder path (homenote/note.md in the session's scratchpad), checked blind against dc6a1cf and the named sources.

Head: I used the Read tool (the note, counts.txt, push_record7.txt, WORKFLOW.md, the n2 values-check raw, the list of record v2, the corpus-adoption raw, ranges of RESULTS.md and of three N12 release raws) and Bash, model-free and read-only. The Bash tools were: git grep -c/-o/-l, git log -S/--format/--diff-filter, git diff, git show <rev>:<path> into pipes, git rev-parse/rev-list/merge-base, git ls-files with pathspecs, /usr/bin/grep -c/-v, cut, sort, uniq, wc, diff, head/tail, one `sed -n` line-range selection, and `gitleaks version`. The rules held. I wrote no file and ran no interpreter. No argv held a guard marker; I reached the model manifest's folder by cd and a glob. Every tree-wide git command carried the three exclusions. Nothing under data/mf3, data/*/ckpt or data/*/reports was listed, opened, hashed or searched. I ran no git status and no --stat. No pattern, no line holding it and no account name was printed: output was counts, file names, and text masked by grep -v on the account name (0 lines suppressed in every range I read).

1. HEADER — "Dated note (coordinating session), for the seat … Not a STOP." — CONFIRMED — Same form as the dated note at RESULTS.md :3571 and the "Not a STOP." at :487. The date agrees with the push record (:29, "pushed 2026-11-18").
2. HEADER — "On the PI's 'Yes, and push', answering the coordinating session's offer of this note" — NOT CHECKABLE — Chat only. The words match push_record7.txt :26 ("The PI's word (chat), verbatim: 'Yes, and push'").
3. ORIGIN — "n-build's values-check of N.2 (b4522ae; its raw …, observation 13)" — CONFIRMED — b4522ae (2026-11-18) is N.2's commit ("n -- N.2: the passage corpus of record committed …") and the only commit touching the raw (A). The raw's header says "Code (the n-build session)". Observation 13 is at :57–62 (disposition) and :226 (report as returned).
4. ORIGIN — "found the laptop's home-folder path in one older entry of this log" — CONFIRMED — Observation 13 says ":11646, in an older entry, contains four occurrences". By my count RESULTS.md holds 1 matching line with 4 occurrences. It is :11646 at 26cf7d2, :11736 at b4522ae and :12156 at dc6a1cf, inside the entry headed :11982, "2026-10-19 — THE Q-F0 CAMPAIGN …".
5. ORIGIN — "The pickaxe limited to RESULTS.md names de6dfc5 (2026-10-19) as the commit that added it" — CONFIRMED — git log -S over RESULTS.md (with the exclusions, with and without --all) names only de6dfc5. Its author and commit date is 2026-10-19 10:50:33 -0400. RESULTS.md has 0 matching lines at de6dfc5^ and 1 at de6dfc5 and at dc6a1cf (1 line added, 0 removed). de6dfc5 is an ancestor of dc6a1cf, and its subject is the Q-F0 campaign's "outputs as written and its launch entry".
6. ORIGIN — "n-build confirmed it by count only and touched nothing; it is the seat's ledger (81)'s class" — IMPRECISE — The raw (:58–62) says "Code confirmed it by count only, never displaying the line … This commit does not touch that entry". b4522ae did change RESULTS.md, just not that entry. The class attribution is the checker's (:226, "This is the class that ledger (81) addresses"), not a ruling. Accept: "n-build confirmed it by count only, never displaying the line, and its commit does not touch that entry; observation 13 reads it as the class that ledger (81) addresses."
7. SCOPE — "the absolute path of the laptop user's home folder, which carries the user's name" — CONFIRMED — The pattern equals $HOME. The account name equals git user.name lowercased with spaces removed. WORKFLOW §1 :7 names the PI.
8. SCOPE — "that name is also the public repository's owner's" — CONFIRMED (owner) — The origin URL's owner segment equals the account name (repository told-vs-felt). Whether it is public rests on item 16.
9. SCOPE — "No line was displayed" — NOT CHECKABLE — This is the session's own act.
10. SCOPE — "the pattern is not reproduced here" — CONFIRMED — The note has 0 lines holding the pattern, 0 holding the account name (case-insensitive) and 0 holding the bare prefix.
11. SCOPE — "git grep -c -F over dc6a1cf, which equals origin/main, with the pathspec excluding data/mf3, every ckpt and every reports directory" — CONFIRMED — HEAD = origin/main = dc6a1cf, and the full hash equals the push record's "remote main now dc6a1cf01c0…97cd". No tracked ckpt or reports folder exists outside data/<unit>/ (0 by name count), so the three exclusions cover every one. The index equals HEAD (0 staged names).
12. SCOPE — "252 tracked files, 859 matching lines" — CONFIRMED — My recount gives 252 files and 859 lines (summed -c counts). The path:count list is identical to counts.txt (diff).
13. SCOPE — "results/raw/: 35 (2026-08), 34 (2026-09), 157 (2026-10), 22 (2026-11), the last of 2026-11-06" — CONFIRMED — 248 raw files, 35/34/157/22. Every name is dated and none is in a subfolder. The last date is 2026-11-06 (two files). Those 248 files hold 834 lines.
14. SCOPE — "Outside it: data/e0 (1 line), data/e2d (22 lines), PROPOSAL-n-bk-reconciliation-v0_2.md (1 line), RESULTS.md (1 line)" — CONFIRMED — data/e0/s2_vignette_axis.meta.json:1, data/e2d/closure_valuescheck.json:22, PROPOSAL-n-bk-reconciliation-v0_2.md:1, RESULTS.md:1. 834 + 25 = 859.
15. SCOPE — "All 252 were public before this note" — CONFIRMED (on the origin) — The per-file counts are identical (252/859) at 16c99d5, fa27c45, 645bd3f, bedc198, 9662468, 977b78b, fa96ccf and dc6a1cf. No added line in 16c99d5..dc6a1cf carries the pattern. 16c99d5 was origin/main before the 2026-11-15 push (RESULTS.md :3576). That they were public rests on item 16.
16. SCOPE — "the origin has been public since 2026-11-04" — NOT CHECKABLE — Given as not checkable from files.
17. GUARDS — "the pre-push screen's local_path class over every pushed range (the list of record v2, item 4)" — CONFIRMED — Item 4 (list v2 :21) is the pre-push screen. The push record shows a [local_path] class (CLEAR) and a RANGE line that reads the range's added lines. The screen's local_path definition (the session's push4/screen4.py :40, read by count only) holds the full pattern. The screened ranges chain without a gap from 16c99d5 to dc6a1cf (:3576, :3648, :3651, :507, :511, :513, push record). Item 4 itself names no class; "local_path" is the screen's name for it.
18. GUARDS — "the pre-commit scrub of a raw (item 7)" — CONFIRMED — List v2 :24: "the pre-commit scrub of a raw covers local paths, addresses and ports."
19. GUARDS — "the seat's ledger (81) for seat files meant for the tree" — CONFIRMED — Corpus-adoption raw §6 :73/:76: "a seat file meant for the tree carries no absolute path of the laptop".
20. GUARDS — "None of them reaches files already in the history" — CONFIRMED (as a reading of the three texts) — The screen reads a pushed range's added lines ("10581 added lines (messages included)"), the scrub runs before a raw's commit, and (81) binds files a seat places.
21. GUARDS — 'WORKFLOW §5: "Git history is never rewritten", and a committed raw is corrected by a dated note or the next raw, never edited.' — IMPRECISE — The quote is exact (:44). But §5's raw clause has the seat as its subject, and the quoted sentence goes on "; a wrong commit is followed by a correcting one", which is (b)'s own form. Accept: 'WORKFLOW §5: "Git history is never rewritten; a wrong commit is followed by a correcting one", and "The seat never edits a committed raw; a correction is the next raw or a dated note."'
22. READINGS — labelled as readings, "(Code adjudicates nothing)" — CONFIRMED — WORKFLOW §1 :11 and §4 :36. No reading is chosen, and the departure is left to the seat.
23. READINGS (a) — "the paths show the laptop's folder layout and nothing else" — IMPRECISE — Counted by path component and nothing printed, the 1,061 occurrences break down as:
    - 885 under the documents folder (854 in the checkout itself, 3 in one other folder beside it, 3 truncated);
    - 126 in the Python install (7 naming three conda environments);
    - 18 in the model cache;
    - 13 in the Claude projects folder;
    - 11 the bare home folder;
    - 6 other.
    The release audit flagged a disclosed conda environment name (history-tag raw :1618). Accept: "(a) record and leave: the name is the public owner's, and the paths show the laptop's folder layout and nothing else, though the layout names more than the checkout: the Python install and three of its environments, the model cache, the Claude projects folder and one other folder beside the checkout;"
24. READINGS (b) — "History keeps every instance" — CONFIRMED — A new commit removes no blob. c2a6417's own subject says the same of its edit ("The names remain in that file's blob at 908a659, in history").
25. READINGS (b) — "(b) edits committed raws, which §5's practice does not do. It would need the seat's ruling on that rule" — IMPRECISE — (b) would edit 248 raws, and also two data artifacts, a proposal and an older entry. The record holds 27 commits that modified committed raws in place, the latest 6d8c237 (2026-11-04). Among them is c2a6417 (2026-10-29), which removed two third-party names from a raw on the PI's word. None came after WORKFLOW v1.0 (dd0bb89, 2026-11-14). Accept: "(b) a correcting commit that replaces the path in the current tree's files with a placeholder. History keeps every instance, and (b) edits 248 committed raws as well as two data artifacts, a proposal and an older entry: §5 bars the seat from editing a committed raw, and none has been edited since WORKFLOW v1.0 (dd0bb89), though the record holds earlier in-place edits of raws, among them c2a6417 (2026-10-29), two third-party names removed on the PI's word, the names left in history. It would need the seat's ruling on that rule;"
26. DEPARTURE — "The first scope check … over HEAD and origin/main, excluding ckpt and reports but not data/mf3" — NOT CHECKABLE — Given.
27. DEPARTURE — "So it read data/mf3's other tracked files … against the campaign's rule" — NOT CHECKABLE — The campaign rule lives in the coordination notes. The committed record does name tracked data/mf3 files outside ckpt/reports (RESULTS.md :3590, a gates JSON), so such files existed to be read.
28. DEPARTURE — "It printed counts only and named no data/mf3 file: its total, 252 files, equals the recount above" — NOT CHECKABLE (the first check) — The recount half holds: 252 with data/mf3 excluded. The inference holds too: equal totals under the same other exclusions mean no data/mf3 file matched.
29. DEPARTURE — "For the seat to class." — CONFIRMED — WORKFLOW §1 :11 and list v2 item 8 (:25: a departure "comes to the seat; the seat rules").
30. C.5 — "the push since this log's last C.5 lines" — CONFIRMED — The newest C.5 lines are RESULTS.md :505–514, ending at 977b78b..fa96ccf. The note's line follows the form of record (:505–514, :3646–3651) clause for clause.
31. C.5 — "(gitleaks 8.30.1, the one on the laptop's path; the runs' outputs do not print its version)" — CONFIRMED — gitleaks on PATH (<the laptop's path>) reports 8.30.1. The push record's gitleaks output lines carry no version; it appears only in the session's header line. The parenthetical is verbatim from :505–506.
32. C.5 — "fa96ccf..dc6a1cf, 8 commits, on the PI's word 'Yes, and push' (2026-11-18)" — CONFIRMED — rev-list gives 8 commits (e48c7d0 … dc6a1cf, all dated 2026-11-18). fa96ccf is an ancestor. See push record :2, :26, :28–29.
33. C.5 — "every class CLEAR but port, whose one match outside was read (the declared container port, in a values-check's text)" — CONFIRMED — Push record :3–9: url_host, ipv4, email, pod_token and local_path CLEAR; port READ, port 22 in results/raw/2026-11-18_respawn-h100_valuescheck.md@d5d08fa. The :22 disposition reads "declared container port '22/tcp'". That raw holds "22/tcp" on 6 lines at d5d08fa.
34. C.5 — "nothing inside ckpt or reports" — CONFIRMED — Every class shows "inside: 0", and all gitleaks findings are 'outside'.
35. C.5 — "gitleaks, 3 generic-api-key matches outside, read (data/n/ids/MANIFEST.json's tokenizer digests, equal to the model manifest's)" — CONFIRMED — Push record :15–18 and :23. By my own check, MANIFEST.json (one line, changed at b523f6a) has one tokenizer_files object with three 64-hex digests, and each occurs once in the committed model manifest.
36. C.5 — "no halt" — CONFIRMED — Push record :24, "No halts."

OBSERVATIONS
1. The note omits a precedent on this class: the release audit already inventoried it before the 2026-11-04 flip and recommended leaving it.
   - The tag's history raw (results/raw/2026-11-04_note-N12-history-tag.md, added 9edbc77) counts the bare home-folder prefix, any user, at the tag: 253 tracked files, 1,155 occurrences (:989–991).
   - Its recommendations by group (:995–998): raws (242 files) "leave: verbatim run records (rule 27)"; data artifacts (2) leave, since "parameterizing would rewrite a committed artifact"; documents (2) leave; code (7) parameterize only if used at run time.
   - The scrub index (results/raw/2026-10-08_note-N12-scrub.md :124–132) carries the earlier counts and, at :129, the recommendation "none of these files needs a change before release".
   - That audit measured a different pattern at a different commit, so its counts are not comparable with 252/859. It bears on readings (a) and (b); the seat may want it cited.
2. The screen's local_path class has never met an instance. The pattern set is unchanged at every screened boundary since 16c99d5, with 0 added lines, so "it would catch one" rests on its definition (screen4.py :40), not on a hit. The screen itself is in the session's scratchpad, not in the tree.
3. No guard stands at commit time for a RESULTS.md entry or a data artifact. Item 7 binds raws and (81) binds seat files. The screen runs at the push, after the commit, which is ledger (81)'s own point. The de6dfc5 instance came from a Code entry. This is for the seat, if it wants a Code-side form.
4. List v2 item 8 asks a departure disclosure for "the checkout's commit". The departure names HEAD and origin/main but gives no hash; it could name the commit or commits at the time.
5. counts.txt holds file names with counts. If it is the first scope check's output, "It printed counts only" should read "file names with counts". Which check wrote it is not checkable.
6. The 859 lines hold 1,061 occurrences (git grep -o). RESULTS.md's one line holds 4, which are observation 13's "four occurrences".
7. The earlier C.5 line of record (:510) names the model manifest's file; the note says "the model manifest's". Optional.
8. Observation 13's ":11646" is RESULTS.md at 26cf7d2 (the check's tree). The note rightly cites no line number.
9. The rule this departure cites is the session's campaign rule, which is not in the tree. The nearest committed rules are WORKFLOW §7's laptop rule ("no whole-tree listing while a stage runs") and list v2 item 5. The first check excluded ckpt and reports, as item 3 requires.
10. My own acts beyond the listed sources, all read-only and disclosed for the coordinating session:
    - I read screen4.py (count and line number only), three N12 raws (masked ranges) and RESULTS.md :485–559 and :3571–3670.
    - I ran one `sed -n` line-range count and `gitleaks version`.
    - I ran git show --name-status on b523f6a and c2a6417, piped to a count and a 5-line head.
    - Two `git ls-tree` calls with glob magic failed and printed nothing.
    - One `git ls-files` count over ckpt/reports-shaped folders nested below data/<unit>/ returned 0 names, nothing printed.

TOTALS: 36 items: 26 CONFIRMED, 4 IMPRECISE (6, 21, 23, 25), 0 FAIL, 6 NOT CHECKABLE (2, 9, 16, 26, 27, 28), and 10 observations.
```
