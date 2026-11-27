# The coordinating session's notes on the seat's two raws of 2026-11-26 (the thread's second and third sittings): the blind values-check, as returned, with every disposition

2026-11-27. Code (the coordinating session).

**What was checked.** One blind pass by a subagent over these drafts:
- the entry's draft (sha256 `6109dc39…20b3`, 130 lines);
- the instruct VERDICTS session's close line for its VERDICTS entry (`2e30784c…adf5`, 39 lines);
- the routing raw (`311ffdc0…8322`, 39 lines);
- the commit message's draft (`d16ab2b9…9434`, 3 lines);
- their placement in a draft of the new `RESULTS.md` (`964d7f53…8735`, 41,721 lines).

It ran while G-READ-n's run was live on the laptop, in n-build's window, whose terms include "nothing heavy beside it". It was read-only and ran no Python.

**The checker's brief** was a file in the coordinating session's scratch folder, named in its Agent call by path (sha256 `24d90009…d6b6`, 169 lines). It is not committed, because it names the local roots in full. It:
- named the sources:
  - the two seat raws, and the third raw for the entry's claims about it;
  - the PI's message in the coordinating session's transcript, with its extraction and the block;
  - the four relays, with their files;
  - the window's grant and the checks before it;
  - n-build's launch-file messages and step messages;
  - the instruct session's message with the close line;
  - the coordinating session's own checks in its transcript;
  - the repository at `0cc301d`: the unit's VERDICTS entry and its values-check raw, `0cc301d`'s entry, the close-line forms at `5ceb8dd` and `79d462b`, `922d7a3` and `0081351`, n-build's block and the spec raw, the raws behind raw (A)'s `ans4` and `ans21b`, and RESULTS.md at `95cd461` for raw (A)'s `R:` anchors;
- told the checker that the transcript's compaction summary is not a source;
- quoted the list of record v2's items 1–5 verbatim, from `2026-11-10_list-of-record-v2_design-to-code_answers.md` (its lines 18–22, equal by `cmp` to the last brief's);
- barred:
  - any interpreter but `shasum` and `jq`, any write and any network;
  - `ps`, `pgrep`, `top` and any power query, and a whole-tree `git status`;
  - anything of G-READ-n's run: n-build's scratch folder, `data/n/gates/` and the staging folder;
  - anything under `data/*/ckpt`, `data/*/reports` or the campaign folder;
  - the memory folder, other sessions' folders and the side-session notes folder;
  - the guard markers (the p unit's name among them, written bracketed) and the campaign folder's plain name in any command text, and any path holding a marker word passed as an argument (such paths go on stdin only);
- set item 3's pathspec, with the campaign folder's and the run's exclusions, on every git command over the tree or a range;
- barred from the report local paths, session ids, the user's name, email, any address or port, the network volume's server host name, and clock times.

The Agent call's prompt restated the brief's main bars. One rule was added by message while the check ran: never quote the PI's message's two paste-markup lines, and never write the identifier they carry. The report says the markup lines appeared in two of its tool outputs before that rule arrived, and in none of its text.

**The report** is in §3, extracted verbatim by `jq` from the subagent's one hand-back (447 lines as `jq -r` wrote them, the last ended by the newline `jq` adds; sha256 `81c6aaf1…6d8f`), byte for byte, with no mask.
- It names no local root. Its `<repo>`, `<own>` and `<transcript>` are the repository, the coordinating session's scratch and its transcript.
- Its account of its own calls agrees with its transcript: 67 `Bash` and 11 `Read` tool calls, by a count of the tool names.

**Totals:** 80 items (73 CONFIRMED, 3 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE) and 11 observations.

## 1. Dispositions

- **Item 13** (IMPRECISE): applied in the checker's words: "the survey's and Code's, inert with no strike; the reviewer's, the values-checker's and the seat's own, inert".
- **Item 24** (IMPRECISE): applied:
  - "six places";
  - a new first bullet in the checker's words: group A as raw (A)'s group N, items 1 and 2 without "the other answer declined", and item 1's "the package reader is admitted";
  - the item-5 bullet in the checker's words, its last sentence as "Raw (A) §5 rules each of these, and the run's window follows §5; the cleanup stays on the PI's word after the artifact is committed (CP18)".
- **Item 74** (IMPRECISE): met by item 24's fix; the routing raw is unchanged.
- **Items 8, 37, 48 and 78** (NOT CHECKABLE): the window's end, the commit's re-hashes and its home-folder count, and "Not pushed". The commit is made only after n-build's end notice, and its gate and verify meet the rest.
- **Observation 1:** flagged for the seat in the entry's values-check bullet. Raw (A) is the seat's and is committed unchanged.
- **Observation 2:** applied: "the tracked tree clean with nothing staged over item 3's pathspec and the campaign folder's exclusion".
- **Observation 3:** noted. The grant check's forms (`ps` with `awk`, `pgrep`, `pmset`, and name-only listings of n-build's run folder and of `data/n/gates`) are among the departures the entry holds for the coordinating session's next notes entry.
- **Observation 4:** applied: "the corrected citations of GR7 and GR8".
- **Observation 5:** noted. The entry's routing bullet states the difference, for the seat to confirm if it wishes.
- **Observation 6:** noted; no change, as the checker says.
- **Observation 7:** noted in the entry's values-check bullet. The close line is the instruct session's, placed as sent, and that session is told.
- **Observations 8–11:** noted.

## 2. Edits after the check

- The edits are the dispositions above, the rewraps of the bullets they changed, and the fills of the two placeholders: `@VC@` with the values-check bullet, and `@VCMSG@` in the message.
- The edits were checked by tool, by `diff` of each checked draft against its final text. Each hunk is a disposition above, a rewrap, or a fill.
- No second full pass was made.

## 3. The report as returned

# Blind values-check: the coordinating session's notes on the seat's two raws of 2026-11-26 (after `0cc301d`)

**What I checked.** The frozen copies in `<own>/s2026-11-27/sitting-a-b/`:
- `checked_entry.md` (E)
- `checked_close_instruct.md` (C)
- `checked_routing_raw.md` (RR)
- `checked_msg_src.txt` (M)
- `checked_RESULTS_draft.md` (D)
- the support files in the same folder: `pi_msg_raw.txt`, `pi_block.txt`, `relay_*.txt`, `sent_*.txt`, `block_*.txt` and `close_instruct.md`.

**Sources.**
- Raw (A) and raw (B), each read whole.
- The dpo raw: its sha256, its line count, and its lines 1 and 3.
- `<transcript>`, always filtered with `/usr/bin/grep -F` before `jq`.
- The repository at HEAD `0cc301d`.

I checked nothing against either compaction summary in `<transcript>`. I do not report the placeholders `@VC@` and `@VCMSG@`. Line numbers are each file's own.

## Items

### The entry (E)

1. **E:1–2.** "2026-11-27 — … the seat's two raws of 2026-11-26, the thread's second and third sittings". **CONFIRMED.**
   - Raw (A):3 reads "PI date 2026-11-26, the thread's second sitting", and raw (B):3 reads "PI date 2026-11-26, the thread's third sitting".
   - The PI's routing record is dated 2026-11-27. The coordinating session's first shell call after it printed "PI date now: 2026-11-27".

2. **E:2–3.** "(GR3 and GR5 stand as built, and the run is cleared)" … "(A0-OLMo-instruct PASS stands, nothing moves)". **CONFIRMED.**
   - Raw (A) has "stands as built" in §0's first two bullets and "G-READ-n's run is cleared" in §5.
   - Raw (B) §0 agrees, and so does `pi_block.txt` line 13 (item 6): "A0-OLMo-instruct PASS stands, nothing moves".

3. **E:3–4.** "both raws committed here by path on the PI's "Route as given" (items 5 and 7)". **CONFIRMED.** (The commit itself falls under item 8.)
   - `pi_block.txt` line 10 reads "5. Code commits raw (A) by path …", and line 14 reads "7. Code commits raw (B) by path …".
   - The message's last line (line 29) is " Route as given".

4. **E:5–6 and E:122–125.** The part since `5ceb8dd`'s last sweep and its departures are held; "The part includes pushes #27 and #28; the windows of the dpo session's note, n-build's seat block and BUILD, and f3-build's Q-F3 record; n-build's three battery windows; the Q-F3 campaign's end; and … G-READ-n's launch files and window." **CONFIRMED.**
   - `5ceb8dd`'s message carries the coordinating session's part "since 13ca2fe's last sweep", with its departures.
   - I compared `git log -1 --format=%cI 5ceb8dd` with the records' dates. Every listed event comes later in `<transcript>`:
     - SendMessage calls: "dpo window granted for the cs note"; "push #27 done" (two); "Q-F3 end acked"; "Seat block window granted (4 paths)";
     - then "BATTERY WINDOW GRANTED: G-READ-n BUILD draft 1/2/3" (three); "WINDOW GRANTED: the Q-F3 campaign's record, five paths"; "WINDOW GRANTED: G-READ-n's BUILD, one commit by path on b449…"; "Push #28 is done" (two);
     - the two launch-file replies, and the run's window grant.

5. **E:8–11.** "(A) … (sha256 `cd6ba27f…0209`, 19,729 bytes, 80 lines), the thread's second sitting: the seat's rulings on n-build's block at `05ac941` (its Q1 and Q2), read with the spec raw beside it and the BUILD's entry at `0cc301d`." **CONFIRMED.**
   - `shasum -a 256` gave cd6ba27f…0209 (abbreviated with `cut -c1-8` and `cut -c61-64`). `wc -c -l` gave 19729 and 80.
   - Raw (A):3 names the block (committed at `05ac941`, "its Q1 and Q2"), "the spec raw committed beside it" and "the BUILD's entry at `0cc301d`".
   - The block at HEAD has sha256 1bd5716a…816d and 165 lines. Its "**Q1 (GR3).**" and "**Q2 (GR5).**" are at its lines 158 and 163.

6. **E:12–15.** "(B) … (`04c53a56…a61c`, 31,147 bytes, 104 lines), the thread's third sitting: the seat's full read of the instruct unit's 138 sessions after its VERDICTS (m:318's "the reads"), in the sft read's form." **CONFIRMED.**
   - `shasum` gave 04c53a56…a61c (by `cut`). `wc` gave 31147 and 104.
   - Raw (B):1 has "(p §8 step 7; m:318's "the reads")".
   - Raw (B):3 has "in the form of the sft read of 2026-11-25" and "The full unredacted read of the unit's 138 sessions".

7. **E:16–18.** "Both were placed untracked over the bridge. The coordinating session re-hashed each equal to the sha256 and bytes the PI's message gives, found them untracked with HEAD at `0cc301d` and origin at `b449ed6`, and read each whole." **CONFIRMED.**
   - Both raws' heads say "Placed untracked over the bridge".
   - In `<transcript>`, the coordinating session's first shell call after the PI's record printed:
     - "ok … sha256 and bytes = the PI's message (19729 bytes, 80 lines)", and the same for (B) with 31147 bytes and 104 lines;
     - "HEAD 0cc301d; origin b449ed6";
     - all three raws as `??`.
   - Its two Read calls on the raws carry no offset or limit.
   - My own checks:
     - `git rev-parse HEAD` gave 0cc301d…, and `git rev-parse refs/remotes/origin/main` gave b449ed6….
     - `git status --porcelain -- results/raw` listed the three raws as `??`.
     - The block's two full sha256s, each with its byte count, match my `shasum` and `wc` (`grep -c -F` found 1 each).

8. **E:18.** "Each is re-hashed equal before this commit and committed here by path, unchanged." **NOT CHECKABLE**: it concerns the commit's own re-hashes.

9. **E:19–21.** The routing raw is to be committed as `results/raw/2026-11-26_two-raws_pi-routing.md`, and "item N", "(A) §N" and "(B) §N" are defined. **CONFIRMED** for the path; the commit itself falls under item 8.
   - The path is the one the brief declares.
   - Nothing is there yet: `git ls-files` printed nothing and `[ -e ]` gave no, as expected before the commit.

10. **E:23–26.** "Q1, GR3 ((A) §1; item 1): Code's reading stands as built. "Nothing of the cells' margins read or printed" is a rule on what the command computes on, prints and writes, and the package's reader satisfies it. The PIN of record (R:11583–11585) binds, and the other answer is declined. A note for N-lap's build: sentinels in the pick-bearing fields too (§1 item 5)." **CONFIRMED.**
    - Raw (A):7 holds the quotation (`grep -c -F` found 1) and "is a rule on what the command computes on, prints and writes … and the package reader satisfies it".
    - Raw (A):14 holds the ruling, and raw (A):20 the note.
    - `git show 95cd461:RESULTS.md | sed -n '11583,11585p'` printed "G-READ-n's driver reads captures only through `cells.load_cell(..., keep_arrays=True)` …".

11. **E:27–29.** Q2: "the lock's pinned reading stands as built. At +1 each random direction's +1 is held against its own −1 on its 40 floor sessions; at +1/2, +d_20 and +d_eq, its cell against the shadow. The other answer is declined. ans21b:23's sentence is corrected by the raw's dated note (§2 item 3)." **CONFIRMED.**
    - Raw (A):25 holds the ruling.
    - Raw (A):29 holds "this raw is the dated correction".

12. **E:30–32.** "O6's second repeat check is not required, a note for N-lap; GR9 as built, F5, the sentinels' scope (F8), the stand-in's writer, the refusals' order and the unbuilt "merged points" clause are accepted. R:12996's observation is a disclosure for Appendix D, not a change." **CONFIRMED.** (See observation 4.)
    - Raw (A) §3 items 1–6, 8 and 9 are at its lines 34–42.
    - `95cd461`'s RESULTS.md line 12996 reads "G-READ-n's shadow contrast tests the state's presence, where rule 5(f)(ii) names the sign".
    - `0cc301d`'s entry lists the same items under "Declared, from the readings and the review".

13. **E:33–34.** "**Departures** ((A) §4): the survey's, Code's, the reviewer's, the values-checker's and the seat's own, inert, with no strike." **IMPRECISE.**
    - Raw (A):46–48: the survey's and Code's are "**Inert, no strike.**"; the reviewer's and the values-checker's are "**inert.**"; the seat's own is "Inert." The raw says "no strike" of two of the five only.
    - **Fix:** "- **Departures** ((A) §4): the survey's and Code's, inert with no strike; the reviewer's, the values-checker's and the seat's own, inert."

14. **E:35–40.** "The run and what follows ((A) §5; item 5): …" **CONFIRMED.**
    - Raw (A):52–56 has each part:
      - cleared "on this ruling and the PI's routing of it";
      - the launch files to the coordinating session first;
      - "a battery window on the laptop", "from the staging folder's arrays";
      - "Every end but exit 0 with the artifact goes to the seat and the PI before anything else runs";
      - the artifact `data/n/gates/G-READ-n.json` "committed by path with the entry `G-READ-n`";
      - the seat's read, then VERDICTS on the PI's word;
      - the volume kept until the artifact is committed, and the pod "stays EXITED".
    - Raw (A):3 has "the n-build session adds its close lines on `05ac941`'s and `0cc301d`'s entries".

15. **E:42–45.** "Δ_c = 76/80 − 1/2 = +0.4500 > E = 1/32 (the sham A0s-OLMo-instruct 17/32); map 0 40/40 and map 1 36/40; P(X ≥ 76 | Bin(80, ½)) ≈ 1.38 × 10^-18 < .01. Every recount equals the outputs, no session was excluded in any phase, and the row stays *Answered*." **CONFIRMED.**
    - Raw (B):15 and raw (B):7 hold these.
    - Shell arithmetic: 1 + 80 + 3,160 + 82,160 + 1,581,580 = 1666981; 1666981/2^80 = 1.3789e-18; 76/80 − 0.5 = 0.4500; 17/32 − 0.5 = 0.03125.

16. **E:46–48.** The carried-forward tallies: strict forced 0 of 356 and free 0 of 534; wider class forced 3 (s = 49 round 3; s = 68 rounds 1 and 3) and free 0; the sham 0 of 196 forced and 0 of 294 free; "Reported; no bar; nothing reclassified." **CONFIRMED** by raw (B):9 and raw (B):63.

17. **E:49–52.** ".95 at the first free pick, .91 at the second, then .81–.86"; "the read on the 0.0625 grid, with no tie at a first read in the campaign"; "the sham's label habit, overridden in pair 2 map 1 in 9 of 12 sessions. No criterion reads any of them." **CONFIRMED.**
    - Raw (B):24: "Descriptive; no criterion reads it".
    - Raw (B):76: ".95 at the first free choice and .91 at the second, then .81–.86".
    - Raw (B):41: "No first read is a tie in the campaign" and "an integer multiple of 0.0625 in all 672 campaign reads".
    - Raw (B):39: "saddle 9 of 12 (map 1) — the maple habit overridden 9 of 12 times" and "Post hoc, n small, reported (rule 11)".
    - Arithmetic: 73/80 = .9125; 65, 69, 67 and 68 of 80 fall at .8125–.8625.

18. **E:53–56.** The §4 dispositions, ending "`don` and `col` fall under the rulings' "under-counts" clause, and nothing changes". **CONFIRMED.**
    - Raw (B):67–72. Item 3 reads "accepted, inert", and item 5 reads "**They do:** … nothing changes (rule 23), no question".

19. **E:57.** "five for Appendix D, flagged, not applied". **CONFIRMED** by raw (B):74–80.

20. **E:58–59.** "the seat's own departures; Code's close line (item 7); the dpo read next". **CONFIRMED** by raw (B):84–87.

21. **E:60–61.** "a routing block the PI pasted, ten items in four groups (A, n; B, p; C, record hygiene; D, the push), ending "PI:", and below it the PI's own words, "Route as given"". **CONFIRMED.**
    - `pi_block.txt` has 23 lines.
    - It has four groups (A, n; B, p; C, record hygiene; D, push), items 1–10, and the last line "PI:".
    - The message's last line is " Route as given".

22. **E:61–62.** "The coordinating session reads each item as its default in brackets." **CONFIRMED.**
    - Each of items 1–10 ends in a bracketed default, and the PI's words are "Route as given".

23. **E:62–64.** "Raw (B)'s five items are its items 6–10: item 6 word for word, items 7–10 reworded, item 7 spelling out §3's tallies and item 9 naming both raws." **CONFIRMED.** (See observation 8.)
    - With item numbers stripped, `cmp` found raw (B):94 equal to block line 13.
    - Raw (B) lines 95, 96, 99 and 102 each differ from block lines 14, 15, 18 and 21.
    - Line 14 carries "(strict 0/356 forced and 0/534 free; wider 3 and 0; the sham 0 and 0)", and line 18 carries "both raws' §6".

24. **E:64 and E:70–72.** "Against raw (A)'s block it differs in five places:" … "its item 5 joins raw (A)'s items 4 and 5 (the run, "[go]"; the seat's read and VERDICTS) without raw (A)'s blank for the PI's word on the volume's cleanup." **IMPRECISE: the list misses differences.**

    I read raw (A):62–67 and `pi_block.txt` lines 5–10 side by side:
    - **(a)** The block's group A is raw (A)'s group "N (n)".
    - **(b)** Items 1 and 2 reword raw (A)'s items 1 and 2, and both drop "the other answer declined". Item 1 also adds "the package reader is admitted".
    - **(c)** Item 5 adds "Code commits raw (A) by path". Besides the blank, it drops:
      - from raw (A)'s item 4: "the run in a battery window on the laptop from the staging folder" and "every end but exit 0 with the artifact to the seat and the PI first";
      - from raw (A)'s item 5: `--gread` and "the volume's cleanup on the PI's word".

    **Fix:**
    - In E:64, replace "it differs in five places:" with "it differs in six places:".
    - Add a new first bullet: "- its group A is raw (A)'s group N, and its items 1 and 2 reword raw (A)'s, each without "the other answer declined" (item 1 adds "the package reader is admitted");".
    - Replace the item-5 bullet (E:70–72) with: "- its item 5 joins raw (A)'s items 4 and 5 (the run, "[go]"; the seat's read and VERDICTS) and adds that Code commits raw (A) by path. It leaves out raw (A)'s battery window on the laptop from the staging folder, its "every end but exit 0 with the artifact to the seat and the PI first", `--gread`, and the volume's cleanup with its blank for the PI's word. These stand as raw (A) §5 rules them, and the cleanup stays on the PI's word after the artifact is committed (CP18);"
    - Rewrap both to the entry's width.

25. **E:65–66.** "raw (A)'s unnumbered lines for its groups A and B (Q-F3, nothing; p, the instruct read, then dpo) are not carried; item 8 is raw (B)'s item 3". **CONFIRMED.**
    - Neither raw (A):69 nor raw (A):71 is in the block.
    - Block line 15 is raw (B):96 reworded ("in the same form" for "in this form").

26. **E:67–69.** Items 3 and 4 regroup raw (A)'s item 3; item 4's "the seat's departures inert" stands against raw (A)'s item 7; item 9's "both raws' §6" stands against raw (A)'s §4. **CONFIRMED.**
    - Raw (A):65 regroups into block lines 8–9.
    - Raw (A):75 reads "The survey's, Code's, the reviewer's, the values-checker's and the seat's departures (§4) classed inert [inert]".
    - Both quotations are in the block (`grep -c -F` found 1 each).
    - Raw (A)'s departures are its §4 (line 44); its §6 is the routing block.

27. **E:73–74.** "raw (A)'s item 6, dated notes with this commit's entry ("[record]"), appears in the block only as item 2's "ans21b:23 corrected by the raw's dated note"." **CONFIRMED.**
    - Raw (A):74 is item 6. The block holds the quotation once (`grep -c -F`), and nothing of ans4:32.

28. **E:75–76.** "its item 10 reads "These commits' push with the next commit or on their own [yours]", where raw (A)'s item 8 names "`0cc301d` and this raw's commit"." **CONFIRMED.**
    - Block line 21 and raw (A):78 each hold their quotation once (`grep -c -F`).

29. **E:77–78.** "Relays, each verbatim between two lines of dashes, each block equal by `cmp` to the routing block or its lines, and each sent text equal by `cmp` to its file (extracted from the transcript by `jq`)". **CONFIRMED.**
    - There are four SendMessage calls after the PI's record: to n-build, the instruct VERDICTS session, the dpo VERDICTS session and n-analyzer.
    - Their `jq -r '.input.message'` equals `relay_*.txt` and `sent_*.txt` by `cmp`, 8 of 8.
    - Block checks, all equal by `cmp`:
      - lines 8–30 of `relay_nbuild.txt` and of `relay_pinstruct.txt` equal `pi_block.txt`;
      - line 6 of `relay_pdpo.txt` equals block line 15, and line 6 of `relay_nanalyzer.txt` equals block line 10;
      - the four `block_*.txt` files equal the same lines (8 `cmp`s in all).
    - Each text has a dash line on either side of its block.
    - The coordinating session's own `cmp`s are in `<transcript>`: four "ok" lines for the blocks and four for the sent texts.

30. **E:79–81.** To n-build: "the block whole (items 1–5 its): GR3 and GR5 stand, so the BUILD and launch files v2 stand; the run's window from the coordinating session; its close lines on `05ac941`'s and `0cc301d`'s entries with its G-READ-n record entry". **CONFIRMED** by `relay_nbuild.txt` lines 1, 37 ("The run's window is my next message.") and 38.

31. **E:82–84.** To the instruct VERDICTS session. **CONFIRMED.**
    - `relay_pinstruct.txt`:1 reads "Items 6 and 7 are yours".
    - Line 39 reads "Please draft it as a file in your scratch, check each figure and quote in it against the raw by tool, and send me its full path, sha256 and line count. Don't edit RESULTS.md, stage or commit".

32. **E:85–86.** To the dpo VERDICTS session. **CONFIRMED** by `relay_pdpo.txt` lines 6, 11 and 12.

33. **E:87–88.** To n-analyzer. **CONFIRMED** by `relay_nanalyzer.txt` lines 6 and 11 ("… VERDICTS runs on the PI's word …. For your record only").

34. **E:89–91.** "n-build's launch files came to the coordinating session first: v1, then v2 after a blind review that n-build offered and the coordinating session accepted, each read whole and checked by tool." **CONFIRMED.**
    - n-build's "G-READ-n'S LAUNCH FILES v1" (2026-11-26) ends "If you want a blind review of the step script before the window, I'll run one in scratch."
    - The reply says "Yes to a blind review of the step script, read-only in scratch …".
    - Then came "G-READ-n'S LAUNCH FILES v2, after the blind review" (2026-11-26).
    - Before each reply there are two Read calls (the note and the step script), with no offset or limit, and one hashing call.

35. **E:91–94.** The window was granted "at HEAD `0cc301d`, after checks by tool: …". **CONFIRMED.** (See observations 2 and 3.)
    - The grant message, "THE RUN'S WINDOW (ON AC POWER) GRANTED" (2026-11-27), says "HEAD for the window is 0cc301d…".
    - Its check call printed:
      - "HEAD 0cc301d; origin b449ed6";
      - "ok tracked clean, nothing staged";
      - "ok gread_steps_v2.sh at its sha256" and "ok pkgsha.sh at its sha256";
      - "the run's folder: [tmp ], tmp: []; data/n/gates: G-ANL-n.json";
      - "python executables: 0; processes naming the run: 0; power: Now drawing from 'AC Power'".

36. **E:94–96.** "The window's steps are check, run, wait and after, one to a message. Its terms, …". **CONFIRMED.**
    - The grant says "The steps, one step to a message …": check, run, wait, after.
    - Its terms: "on AC power; the lid open; Low Power Mode off; no sleep, restart, log-out or software update by hand until the end notice, and none scheduled; nothing heavy beside it."
    - n-build's "STEP 1, check 0cc301d: PASS" and "STEP 2, run 0cc301d: PASS" (2026-11-27) follow in that order.

37. **E:97.** "The coordinating session held this commit and its own Python until the window closed." **NOT CHECKABLE**: the window has not ended. So far:
    - The grant says "I hold my own commit and any Python of mine (the screen) until the window closes".
    - HEAD is still `0cc301d`.
    - None of the coordinating session's shell commands after the grant calls Python. `grep -i '[p]ython'` found two hits, both prose in log text.

38. **E:97–98.** "The run's end is n-build's record." **CONFIRMED.**
    - `relay_nbuild.txt`:37 asks n-build to read the out and err whole, screen them, and send the record in its own commit window.

39. **E:99–101.** The close line is "placed here verbatim (sha256 `2e30784c…adf5`, 39 lines, no line over 120 characters but its link line)", after the entry's last line. **CONFIRMED.**
    - `shasum` gave 2e30784c…adf5 (by `cut`), and `wc` gave 39 lines.
    - `LC_ALL=en_US.UTF-8 /usr/bin/grep -n '.\{121,\}'` found only line 4, the link line.
    - The placement is checked in item 79.

40. **E:101–104.** "It holds: the raw cited by path and full sha256 in the sft line's form (`5ceb8dd`); the PI's routing words for items 6 and 7; §6's line for Code, quoted; the short form and §0's rule-25 sentence; §3's carried-forward totals verbatim beside the entry's release, with §0's wider cases and its strict definition; and a finding aid for §4–§6." **CONFIRMED.**
    - These are C:2–5, C:6–7, C:9–12, C:13–14, C:15–24 and C:25–39, checked in items 53–64.

41. **E:104–106.** "The finding aid also names the gate stages' later picks, which the unit's values-check raw carries in its checkers' text and which the entry left out as one of Q-F0's extraction classes; the seat's §3.3 reads the same picks from the records." **CONFIRMED.**
    - HEAD's RESULTS.md lines 13413–13414 read "The gate stages' later picks are one of Q-F0's extraction classes (below) and are not made here."
    - The values-check raw is checked in item 63; raw (B):59–60 hold §3.3's picks.

42. **E:107.** "Nothing else on the entry moves, and the secondary-DVs entry gets no line." **CONFIRMED** by raw (B):85.

43. **E:108–112.** The ans21b:23 sentence, quoted and corrected by raw (A) §2 item 3; "The count it ruled (2,976 calls, computed once per point and shared) stands, and the lock governs." **CONFIRMED.**
    - ans21b is `results/raw/2026-11-21_n-gtime-starred-seven_design-to-code_answers.md` (found with `git show --name-only b40ce59`). It was added at `b40ce59` (`git log --diff-filter=A`) and is unchanged to HEAD (`git diff --quiet`).
    - Its line 23 holds the quoted sentence: fed on stdin to `grep -c -F`, it matched once. The line also has "2,976 calls" and "computed once per point and shared".
    - Raw (A):29 holds the correction and "The lock … governs".

44. **E:113–114.** "ans4:32's sentence ("nothing of the cells' margins read or printed") is read as raw (A) §1 items 1 and 4 have it, a rule on what the command computes on, prints and writes. Its words stand as committed." **CONFIRMED.**
    - ans4 was added at `13ca2fe` and is unchanged to HEAD. Its line 32 holds the clause (`grep -c -F` found 1).
    - Raw (A):21 reads "ans4:32's sentence is read as items 1 and 4 have it; its words stand as committed."
    - The gloss uses raw (A):7's (§0) words.

45. **E:115.** "Item 9: the seat's departures in both raws' §6 (raw (A)'s are in its §4), inert." **CONFIRMED** by block line 18 and raw (A) §4.

46. **E:116–117.** "Item 10, the push: "[yours]". The push of this commit, with `0cc301d`, waits for this commit's verify and screen and the PI's word." **CONFIRMED** by block line 21 and raw (A):78.

47. **E:118–121.** The third raw "(`14da65a9…0593`, 111 lines), the seat's dpo read, was placed untracked beside the two"; the PI's message routes only (A) and (B), and its item 8 says only that the dpo read follows. **CONFIRMED.**
    - `shasum` gave 14da65a9…0593 (by `cut`), and `wc` gave 111 lines. The scoped status lists it as `??`.
    - Its line 1 reads "# PROPOSAL-p OLMo-dpo — VERDICTS: the seat's read (p §8 step 7; m:318's "the reads")".
    - Its line 3 begins "Design seat, PI date 2026-11-26, the thread's fourth sitting".
    - The block names only (A) and (B).

48. **E:127–129.** "Committed by path: … The commit-time count of the home-folder prefix over the staged diff is 0. The coordinating session ran nothing on a model. Not pushed." **NOT CHECKABLE**: these are commit-time claims.
    - As far as I can check, none of the coordinating session's tool calls after the PI's record runs a model.

49. **E's format.** **CONFIRMED.**
    - Only E:9 and E:13, both link lines, are over 118 characters (`LC_ALL=en_US.UTF-8 /usr/bin/grep -n '.\{119,\}'`).
    - The file ends in `\n\n`, a blank line (`tail -c 2 | od -c`).

### The close line (C)

50. **C as sent.** The instruct session's message (a queued_command attachment) gives its sha256, "39 lines; 3,808 bytes" and "It ends with a newline and no blank line". **CONFIRMED.**
    - My full `shasum` of C, followed by "; 39 lines; 3,808 bytes. It ends with a newline and no blank line.", matched the message's text (`grep -c -F` found 1).
    - `wc -l -c` gave 39 and 3808. `tail -c 3 | od -c` showed `t . \n`.
    - The coordinating session's copy call printed "ok copy at the sha256 sent" and "ok copy = source by cmp".
    - `close_instruct.md` has the same sha256.

51. **C:1.** "(PI date 2026-11-26; the seat's VERDICTS read, §6)". **CONFIRMED** by raw (B):3 and :85.

52. **C:1–3.** "That commit is the read's first commit, so `git log --diff-filter=A -- …` names it". **CONFIRMED as of now**: `git log --format=%h -- results/raw/2026-11-26_p-instruct-verdicts-read_design-to-code_answers.md` prints nothing.

53. **C:4–6.** The link, the full sha256, and "A commit cannot name its own hash; the next RESULTS entry names it in full." **CONFIRMED.**
    - The full sha256 equals my `shasum` (`grep -c -F` found 1).
    - The link form and the sentence are those of the sft line at `5ceb8dd`.

54. **C:6–8.** "takes item 6 "[accept]" and item 7 "[route]" in its section B; the PI's words below the block are "Route as given". This line is the instruct VERDICTS session's." **CONFIRMED.**
    - Block lines 12–14 and the message's last line hold the routing words. The instruct session's message names the line as its own.

55. **C:9–12.** §6's words for Code, quoted. **CONFIRMED**: C:9–12 joined equals raw (B):85 after "- **Code:** " by `cmp`.

56. **C:13–14.** The short form's quotation and "The rule-25 window closes with this read (m:271)." **CONFIRMED**: fed on stdin to `grep -c -F`, they matched once in raw (B):7 and once in raw (B):11.

57. **C:15–19.** §3's "Carried-forward totals for the unit, contrast arm", verbatim. **CONFIRMED.**
    - The heading quotation matched once in raw (B):63.
    - The body equals raw (B):63 after its bold label, by `cmp`.

58. **C:20–21.** "each a correct answer followed by a remark on the corruption in the banner's own words, no tag named, none claimed". **CONFIRMED**: it matched once in raw (B):9.

59. **C:22.** "§0's word on them: "Reported; no bar; nothing reclassified."" **CONFIRMED**: it matched once in raw (B):9. (See observation 6.)

60. **C:23–24.** The strict definition. **CONFIRMED**: it matched once in raw (B):9.

61. **C:25–28.** §4's dispositions of the "For the seat" items. **CONFIRMED** by raw (B):67–70 and :72, and the VERDICTS entry's "**For the seat**" at HEAD line 13436.

62. **C:29–31.** "§4 accepts the counters step (`922d7a3`) as Code's, descriptive, deciding nothing. It also answers the question `0081351`'s dated note left to the seat: `don` and `col` fall under the rulings' "under-counts" clause, and nothing changes. This session adds no note." **CONFIRMED.**
    - Raw (B):71 holds the acceptance and the answer.
    - `git log -1 --format='%h %ad %s'`:
      - `922d7a3` is "p's counters at VERDICTS -- the counters step for the three units …";
      - `0081351` is "… a dated note on 9464f61's entry: the corrupted-spelling rule as the counters step applies it …".
    - The instruct session's message says "No note on `don`/`col`".

63. **C:32–37.** "left out of this entry as one of Q-F0's extraction classes (the values-check raw's disposition 0b)"; "G-TIME 5 clean and 1 corrupted of 6, G-F0m 43 and 5 of 48 (pass 1 row 83; pass 2 rows 152–153 and its observation 4)"; §3.3's picks. **CONFIRMED.** (See observation 7.)
    - I read the values-check raw (`results/raw/2026-11-16_p-verdicts_OLMo-instruct_valuescheck.md`) with `git cat-file --batch`, its path fed on stdin:
      - its §0b has "IMPRECISE #154 and #159: … Those picks are one of Q-F0's extraction classes (E5, E11)";
      - row 83 of pass 1's claim table reads "free-round denominators: G-TIME 5 clean, 1 corrupted of 6; G-F0m 43 and 5 of 48";
      - pass 2's rows 152–153 and its observation 4 agree ("G-TIME 5 clean and 1 corrupted, G-F0m 43 and 5 (#152–#153)").
    - Raw (B):59 gives G-TIME's picks as copper ×4, walnut, copper: P at 5 of 6.
    - Raw (B):60 reads "All 8 picked P first … and stayed on P at 35 of their 40 later picks".

64. **C:38–39.** "Its §5 flags five disclosures …"; "Its §6 records the seat's own departures, which the routing's item 9 classes inert." **CONFIRMED** by raw (B):74–80 and :84, and block line 18.

65. **C's form**, against the sft close line at `5ceb8dd` (the second hunk of `git show 5ceb8dd -- RESULTS.md`). **CONFIRMED.**
    - C has the same parts in the same order.
    - It adds three things: "This line is the instruct VERDICTS session's.", "This session adds no note." and the later-picks bullet.
    - Q-F0's close line at `79d462b` has the same title form.

66. **C's widths and ending.** **CONFIRMED**: only C:4, the link line, is over 120 characters, and the file has no blank last line.

### The routing raw (RR)

67. **RR:1, the title.** **CONFIRMED.**

68. **RR:3.** "received by the coordinating session on PI date 2026-11-27, under the PI date its block gives, 2026-11-26"; (A) and (B) by path, sha256, bytes and lines, with what each is. **CONFIRMED** (items 1 and 5–7).
    - "Both are committed …" is a commit claim, of item 78's class.
    - The entry cites this raw at E:19–20.

69. **RR:5.** "the message was extracted by `jq` from the coordinating session's own transcript". **CONFIRMED.**
    - The call "Extract the PI's routing message from the transcript" ran `jq -r` over `<transcript>` into `pi_msg_raw.txt`.
    - My own `jq -r '.message.content'` of the record equals `pi_msg_raw.txt` by `cmp`.
    - The declaration in the next notes entry is still to come.

70. **RR:5.** "a plain string of human origin in two parts". **CONFIRMED.**
    - The record's content is a string; its origin kind is "human", and its userType "external".
    - It holds the block inside paste markup, then the PI's words.

71. **RR:5.** "§1 is the block, byte for byte between the markup's two lines: 23 lines, each ended by its own newline in the message. §2 is the PI's words, the message's last line, ended by the newline the extraction adds." **CONFIRMED.**
    - The extraction has 29 lines. The markup's opening and closing lines are lines 3 and 27.
    - Lines 4–26 equal `pi_block.txt` (23 lines) by `cmp`.
    - The content does not end in a newline: `jq endswith("\n")` gave false.

72. **RR:5.** "The markup's two lines, the two blank lines before the block and the blank line after it are not reproduced; the markup carries an identifier of the client's". **CONFIRMED.**
    - The content opens with two newlines, then the markup's opening line, and line 28 is blank.
    - RR, E, C and M hold no markup line and no identifier. `grep -c '[p]asted_content'` gave 0 in each, and so did the identifier fed on stdin.

73. **RR:5.** "raw (A)'s §6, eight items in five groups; raw (B)'s §7, five items in three". **CONFIRMED.**
    - Raw (A):62–78 has groups N, A, B, C and D, with items 1–8.
    - Raw (B):93–102 has groups B, C and D, with items 1–5.

74. **RR:5.** "the differences are stated in the notes' entry". **IMPRECISE** while item 24 stands.
    - **Fix:** none needed if item 24's fix is applied. Otherwise write "the main differences are stated in the notes' entry".

75. **RR's fenced blocks.** **CONFIRMED.**
    - RR lines 10–32 equal `pi_block.txt`, and RR line 38 equals the message's line 29, both by `cmp`.

### The commit message (M)

76. **ASCII only, with the co-author line last.** **CONFIRMED.**
    - `LC_ALL=C tr -d '\000-\177' | wc -c` gave 0.
    - M has 3 lines; the last is the co-author line, and it ends in a newline.

77. **M:1's content claims.** **CONFIRMED** by items 4–7, 29–36, 39, 43–47, 50, 57 and 69. They cover:
    - the two raws' paths and hashes, and the routing raw "extracted by jq";
    - the close line "(2e30784c...adf5, 39 lines: … strict 0/356 forced and 0/534 free, wider 3 and 0, the sham 0/196 and 0/294)";
    - the dated notes, and "Relays verbatim to n-build (items 1-5), the instruct session (6-7), the dpo session (8) and n-analyzer (5), each block equal by cmp";
    - the window "granted at 0cc301d after n-build's launch files v1 and v2 were read and checked";
    - the third raw, and "Item 10's push ("[yours]") waits for the PI's word, with 0cc301d";
    - the held part.

78. **M:1's commit-time claims**: "this commit held until the window closed", "committed unchanged", "The commit-time count of the home-folder prefix over the staged diff is 0" and "Not pushed". **NOT CHECKABLE**: they depend on the window's end and on the commit.

### Placement and support files

79. **D is HEAD's RESULTS.md with E inserted after line 23 and C after line 13479.** **CONFIRMED.**
    - `{ git show HEAD:RESULTS.md | sed -n '1,23p'; cat E; … sed -n '24,13479p'; cat C; … sed -n '13480,$p'; } | cmp - D` found them equal.
    - Line counts by `wc`: 41,552 + 130 + 39 = 41,721.
    - At HEAD:
      - line 22 is "## Log — Phase 2", 23 is blank, and 24 begins `0cc301d`'s entry;
      - line 13479 is "  - Not pushed. Committed by path.", 13480 is blank, and 13481 begins the secondary-DVs entry.
    - The working RESULTS.md equals HEAD's (`git diff --quiet`).

80. **`pi_msg_raw.txt` is the record's `jq -r` extraction, and `pi_block.txt` is the block between the markup's lines.** **CONFIRMED** (see item 71).

## Observations

1. Raw (A) is inconsistent on one anchor. Its §0 and §2 item 1 give "LOCK:1261 pins probe:29–33", but §2 item 3 says "The lock, which pins probe:29–34, governs". The entry carries neither; this is for the seat, if it wishes.
2. The grant's "tracked clean, nothing staged" came from `git diff --cached --quiet` and `git diff --quiet` run over item 3's pathspec plus the Q-F3 folder's exclusion. So E:92's "the tracked tree clean" is that scoped check, in the grant's own words, not a whole-tree status.
3. The grant's check used forms outside list-of-record item 1: `ps -A -o comm=` with `awk`, `pgrep -f`, `pmset -g batt`, and name-only `ls -1A` of n-build's run folder and of `data/n/gates`. The listing reached into another session's folder. These forms belong among the departures that E:5–6 holds for the next notes entry.
4. E:30–32's list leaves out raw (A) §3 item 7 (GR7's classifier path and GR8's absence test, citations corrected in the spec raw's head, accepted). Raw (A)'s own routing item 3 leaves it out too. An optional addition to E:31: "the corrected GR7 and GR8 citations".
5. The block's item 4 classes only "the seat's departures" inert, where raw (A)'s item 7 and §4 class all five sets inert. E:67–69 states this difference, and E:33–34 records raw (A) §4's classing as the raw's own. No change is needed, though the seat may want to confirm the reading.
6. In raw (B) §0, the sentence C:22 quotes ("Reported; no bar; nothing reclassified.") closes the whole tally paragraph: strict, wider and sham. C:22 calls it "§0's word on them", meaning the wider cases. The sft line at `5ceb8dd` uses the same words for its wider cases, so no change.
7. C:33's "disposition 0b" names the values-check raw's section "0b. Code's dispositions, pass 2"; the disposition meant is "IMPRECISE #154 and #159". For more precision, it could read "(the values-check raw's §0b, on IMPRECISE #154 and #159)".
8. E:63–64 names item 7's tallies. Item 7 also adds "citing it by path and sha256" and the entry's full name, which come from raw (B) §6 rather than its item 2. "Reworded" covers both.
9. The committed instruct values-check raw's content hashes to a23d83c0…5c1c, the figure the instruct session's message gives for "the committed blob". Its git object id is b44332bf…3638. Neither figure is in the checked texts.
10. `<transcript>` holds two compaction summaries, dated 2026-11-25 and 2026-11-27. I checked nothing against either.
11. At check time, each frozen copy has the same sha256 as its live draft in the same folder: `entry.md`, `routing_raw.md`, `msg_src.txt`, `RESULTS_draft.md` and `close_instruct.md`.

## My own departures

1. **`<transcript>`: 34 shell calls read it.**
   - Each filtered with `/usr/bin/grep -F` before `jq`, and `jq` ran over `<transcript>` only. One more command ran `wc -l` on it, which printed 3,334 lines.
   - What they printed:
     - the PI's record's fields and text, and the relays' texts (piped to `cmp`);
     - SendMessage summaries and heads with recipient-id prefixes;
     - cross-session messages from n-build and from the instruct session, whole;
     - the coordinating session's tool-call descriptions, and the commands and results of its checks. Paths were shortened by `sed` on output, but one listing showed another session's scratch path;
     - Read-call parameters and returned line counts, and the dates and flags of the two compaction records.
   - The markup lines appeared in two outputs: my view of the extraction's first four and last lines, before the coordinator's added rule arrived, and the coordinating session's own printed extraction result.
   - After that rule, I matched the markup lines only by line number or a bracketed pattern, and passed the identifier only on stdin.
   - Session ids appeared in some outputs (recipient fields, and one command text).
   - None of this is in this report.
2. **Counting:**
   - `wc -c -l` of the three seat raws, which printed 80/19729, 104/31147 and 111/38962;
   - `wc -l` and `wc -c` of files in `<own>`;
   - `git show HEAD:RESULTS.md | wc -l` (41552), and the block piped to `wc -l` (165);
   - `LC_ALL=C tr -d '\000-\177' | wc -c` on M, which printed 0;
   - width greps with `LC_ALL=en_US.UTF-8 /usr/bin/grep`. They printed E:9, E:13 and C:4, and counts of lines exactly 118 and 120 characters long (7 and 0);
   - `tail -c` with `od -c`, and `cat -v`, on the ends of four files in `<own>` and of extracted quotations.
3. **Listing and stat-like checks:**
   - one name-only `ls` of `<own>/s2026-11-27/sitting-a-b/`, which item 1 permits;
   - one `[ -e ]` on the routing raw's target path under `results/raw`, which printed no.
4. **Git forms naming one file outside `data/`, without item 3's pathspec:**
   - `git show HEAD:RESULTS.md` (12), `git show 95cd461:RESULTS.md` (2), `git show 5ceb8dd -- RESULTS.md` (2), `git show 79d462b -- RESULTS.md` (2), `git diff --quiet HEAD -- RESULTS.md` (1);
   - `git show HEAD:` of ans4 (2);
   - `git show HEAD:` of ans21b (4). In one of these pipelines, `grep` failed on BSD's repetition-count limit and printed only its error;
   - `git show HEAD:` of n-build's block (3), plus 1 with a mistyped year that printed nothing;
   - `git log --diff-filter=A --format=%h -- <file>` (2) and `git diff --quiet <rev> HEAD -- <file>` (2);
   - `git log --format=%h --` on raw (A) and on raw (B) (2; both printed nothing);
   - `git ls-files --` on the routing raw's path (1; nothing);
   - `git status --porcelain -- results/raw` (1).
5. **Git over the tree:**
   - `git ls-files -- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/m[f]3/**' ':!data/n/gates/**'` (5), filtered by a bracketed pattern to the instruct values-check raw's name.
   - That path holds a marker word, so it went only on stdin: to `git cat-file --batch='%(objectname)'` (4: greps of the content and its headings) and to `--batch-check` (1).
   - Then `git cat-file blob <id> | shasum` (1).
6. **Other git:**
   - `git rev-parse` (2);
   - `git log -1` with `--format` of id, date and subject (3), and of commit time `%cI` (2);
   - `git show --name-only --format=…` (2). One of these formats held the author field; `sed` dropped that line before printing.
7. **One `zsh -c`** for floating-point shell arithmetic. It printed 1666981, 1.3789e-18 and eight quotients.
8. **Small loops**: over 4 relays, 4 Read-call ids, 5 and then 8 routing lines, 4 checked texts, 11 quotations and 3 hashes.
9. **Redirects**: one discarded pipeline sent to `/dev/null`, and one `2>/dev/null`. I wrote no file anywhere.
10. **Read tool: 11 whole-file reads**: the brief; E, C, RR and M; raw (A) and raw (B); and the four `relay_*.txt` files.
11. **Guards held:**
    - Marker words appear in my command texts only in bracketed, quoted patterns (`'…_[O]LMo-instruct_valuescheck…'`, `'[p]ython'`, `'[p]asted…'`).
    - No path holding a marker word ever stood in argv.
    - I listed, opened, hashed or searched nothing of G-READ-n's run: not n-build's scratch, not `data/n/gates/`, not the staging folder.
    - I ran no process listing, no power query and nothing on the network.
    - I opened nothing under `data/`, no other session's folder, and not the memory folder.

## Tallies

80 items: **73 CONFIRMED, 3 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE.**
- IMPRECISE: items 13, 24 and 74.
- NOT CHECKABLE: items 8, 37, 48 and 78.

11 observations.
