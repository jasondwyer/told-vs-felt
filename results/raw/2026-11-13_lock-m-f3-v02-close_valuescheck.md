# The close line on LOCK-m-F3 v0.2's entry: its values-check

*Code's raw, PI date 2026-11-13.*
- *What was checked:* the close line Code added to RESULTS.md, on the LOCK-m-F3 v0.2 entry (`05ef75d`), after that
  entry's **Next:** bullet, before the commit.
- *Against:* the seat's read of G-F0m-OLMo (p) ×3 (`results/raw/2026-11-12_p-qual_design-to-code_answers.md`,
  sha256 `a32d4d17…1112`, committed at `a2c354e`); the coordinating session's routing relay of 2026-11-13, as Code
  received it; git (`a2c354e`, `2193832`, `b427f82`, `05ef75d`, `15d2f70`); RESULTS.md; `LOCK-m-F3.md`.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written. It needed
  nothing under `data/` and opened nothing there. It ran no model.
- *Outcome:* 24 claims: 22 CONFIRMED, 2 IMPRECISE, 0 FAIL, 0 NOT CHECKABLE. HEAD was `a2c354e` at its start and at
  its end. Both IMPRECISE items are applied (below).
- *Not run:* a second pass. Each change applies the checker's own fix and carries no figure. Re-wrapping the block to
  the file's width added one line: the hunk is now +21.
- *Code's masked scan of the checker's transcript* (counts only; no command text printed): 30 distinct command
  texts; none names a ckpt path; no metadata form names `data/`; nothing under the tasks directory; no transcript
  opened.
- *This raw:* Code's dispositions, then the report verbatim.
  - Code extracted the report by script from the agent's hand-back: sha256 `76183e4d…75a2`, 150 lines, no final
    newline.
  - Code's leak check found no local path, user name, session id or temp-dir id, and no clock time.

## Code's dispositions

- **3, IMPRECISE: the heading.** Agreed. The seat gives this close line to "the LOCK-m-F3 v0.2 entry's pointer"
  (§7), and keeps "v0.2 §8's pointer" for what v1.0 closes (§3, §5). The heading now reads "on the entry's pointer
  (v0.2 §8; `15d2f70`)".
- **13, IMPRECISE: "§3 and §5".** Agreed. The sentence is verbatim in §3 only. The label now reads "§3 (and §5, in
  its own words)".
- **Observation (b): the second commitment.** Agreed. "No driver commit lands while G-F3 is open" binds until the
  seat has read G-F3. The line now says "both have held so far".
- **Observations (a), (c) and (d).** No change: (a) the nested quotes are verbatim; (c) the line follows the relay on
  who committed the file; (d) the line names no section for ledger (67).

## The checker's report (verbatim)

**Blind values-check: the close line on the LOCK-m-F3 v0.2 entry (uncommitted, RESULTS.md)**

HEAD was `a2c354e` at the start and `a2c354e` at the end. The check finds 24 claims: 22 CONFIRMED, 2 IMPRECISE (wording and anchoring only), 0 FAIL, 0 NOT CHECKABLE. Every quote is verbatim.

**Method (read-only).**
- git, names and digests only:
  - `git diff -- RESULTS.md`, also with `-U0` and against HEAD.
  - `git show --name-status` of the five commits, each with `':!data/**'`.
  - `git log --format` with ids and subjects only.
  - `git rev-parse <rev>:<path>`, `git hash-object` (no `-w`) and `shasum -a 256`.
- Files read:
  - RESULTS.md and `LOCK-m-F3.md`.
  - The seat's read.
  - The section headings of the G-ID-F3 answers.
  - `C/close_line.md` and `C/relay_extract.txt`, where C is the brief's scratch folder.
- One `python3 -I -c` (stdlib only: re, sys, hashlib):
  - It removed `**`, joined the wrapped lines and tested each quote byte for byte.
  - The close line's only non-ASCII characters are —, § and ×, and all of them matched.
- `C/commit_close.txt` is not a listed source, and I did not open it.

**References.**
- RESULTS.md line numbers are the working tree's; the close line sits at RESULTS.md:501–520.
- "seat" means `results/raw/2026-11-12_p-qual_design-to-code_answers.md`.
- "relay" means `C/relay_extract.txt`.

**Items**

1. **One hunk, placed as described, nothing else changed: CONFIRMED.**
   - `git diff -U0 -- RESULTS.md` (and against HEAD) shows one hunk, `@@ -500,0 +501,20 @@`: 20 lines added, none removed.
   - Nothing is staged. RESULTS.md is the only modified tracked file outside `data/`.
   - The hunk sits inside the entry whose heading is at :455 (dated 2026-11-11), right after its **Next:** bullet (:500). The blank line :521 and the `15d2f70` note at :522 follow.
   - The added lines are byte-identical to `C/close_line.md`.

2. **"Close (PI date 2026-11-13)": CONFIRMED.**
   - relay:1–2 gives "PI date 2026-11-13".
   - `a2c354e`'s three close lines carry the same date (RESULTS.md:210, :421, :564).

3. **"on v0.2 §8's pointer": IMPRECISE.**
   - The pointer exists: `LOCK-m-F3.md`:258–259 (v0.2 §8's **Pending** bullet, naming `15d2f70`). The entry repeats it at RESULTS.md:478–479.
   - But the seat gives this close line to "the LOCK-m-F3 v0.2 entry's pointer (`05ef75d`)" (seat:62, §7).
   - The seat uses "v0.2 §8's pointer" for what LOCK-m-F3 v1.0 closes by citing the file (seat:31, §3; seat:53, §5). The close line says the same at :511–512 ("v1.0 carries the close").
   - As written, the heading says this line closes the pointer that the line itself says v1.0 will close.
   - **Fix:** "**Close (PI date 2026-11-13), on the entry's pointer (v0.2 §8; `15d2f70`).**", the seat's §7 wording.

4. **The file named and linked: CONFIRMED.**
   - The title at seat:1 matches.
   - The link target is tracked (`git ls-files`).

5. **sha256 `a32d4d17c9d17d7920539f8c7e6945e8a71712bb76ba2f0154e22f3dbb9e1112`: CONFIRMED.**
   - Recomputed on the working-tree file (75 lines).
   - The git blob `0473b4f6…` is the same at `a2c354e`, at HEAD and in the working tree.
   - The same value appears at relay:6 and in `a2c354e`'s subject.

6. **"committed by path by the pod session at `a2c354e`": CONFIRMED.**
   - `git show --name-status a2c354e -- ':!data/**'` shows `A` for the file and `M` for RESULTS.md. Its parent is `2193832`, as relay:7 says.
   - The subject says "the seat's read committed by path as placed", and RESULTS.md:423–424 says the same.
   - The session comes from relay:7 ("The pod session committed it by path at a2c354e"). It matches seat:61, where §7 gives those close lines to the pod session. git itself records no session.

7. **"rules at its §3 on the observation the pointer names (the coordinating session's note, `15d2f70`)": CONFIRMED.**
   - seat:31 is inside §3 (seat:28–35) and opens on "The coordinating session's note (`15d2f70`)".
   - The pointer names that note (`LOCK-m-F3.md`:258; RESULTS.md:478–479).
   - `15d2f70` changes RESULTS.md only, and its subject begins "Dated note (coordinating session)".
   - It added the note now at :522: the note is absent at its parent `eb3e08c` and present at `15d2f70`.

8. **"The observation is right.": CONFIRMED.** Verbatim at seat:31; it occurs once.

9. **The G-ID-F3 answers' "§6 stands as placed (the PI routed it as given; nothing is rewritten)": CONFIRMED.**
   - The quote is verbatim at seat:31.
   - seat:3 defines `gid:` as the G-ID-F3 answers (`c51ef5ba…a9d7`).
   - That file is tracked, hashes to `c51ef5ba…a9d7`, and has a §6 at its line 42.

10. **"withdrawn as a method and carried by no later text": CONFIRMED.** Verbatim at seat:31, where the seat applies it to the derived figure.

11. **"Ledger (67) is the seat's own.": CONFIRMED.**
    - seat:55 is headed "Ledger — design seat (67)", with the entry at seat:57; §8 item 3 (seat:70) also names it.
    - The form matches `LOCK-m-F3.md`:257 ("Ledger (65) and (66) are the seat's.").

12. **"§3, on this lock" quote: CONFIRMED.**
    - Verbatim, bold markers aside (the source bolds "LOCK-m-F3 v0.2"), at seat:35 in §3; it occurs once.
    - The double quotes nested inside it are the seat's own.

13. **"§3 and §5, on the lock file:" quoting "LOCK-m-F3 v1.0 closes v0.2 §8's pointer by citing this file.": IMPRECISE.**
    - The sentence is verbatim, but it occurs only in §3 (seat:31, its one occurrence in the file).
    - §5 (seat:53) says it in other words: "closes v0.2 §8's pointer by citing this file (§3)".
    - The label reads as if the quoted sentence were in both sections.
    - **Fix:** "**§3 (and §5, in its own words), on the lock file:**", or label it §3 and cite §5 for the next sentence.

14. **"So `LOCK-m-F3.md` is not edited now.": CONFIRMED.**
    - `git status --porcelain -- LOCK-m-F3.md` prints nothing, and no commit after `05ef75d` touches the file.
    - Its blob `b84646f3…` is the same at `05ef75d`, at HEAD and in the working tree.
    - Its sha256 `ac82b943…75a7` equals the entry's (:457).
    - The statement follows from seat:31 and :53 and from relay:15 ("There is nothing to build now"). It is not stated as a rule.

15. **"v1.0 carries the close, with the rest of §5's contents, after G-F3, G-VER and G-PWR.": CONFIRMED.** seat:53 (§5) says this; relay:15 agrees.

16. **"§7, for this session" quote: CONFIRMED.**
    - Verbatim, bold markers aside (the source bolds "Code (F3 session):"), at seat:62 in §7 (seat:59–64); it occurs once.
    - It is also verbatim at relay:10, which addresses this session.

17. **"G-F3 ran as routed (`2193832`).": CONFIRMED.**
    - The routing at seat:52: 40 uncached sessions at cap 120, lock `ac82b943…`, driver `285eed04…0e44`, announced to the coordinating session.
    - `2193832`'s subject and the G-F3 entry match it: RESULTS.md:24–26, :44 (the coordinating session's go-ahead), :73 (the driver), :76 (the lock).
    - relay:14 says the same: "G-F3 as routed: done (2193832)".
    - The seat's read of G-F3 is still pending (:39, :135), and the line does not claim otherwise.

18. **"§5 accepts Code's two commitments for it": CONFIRMED.** seat:52, and seat:74 (§8 item 7).

19. **"the G-F3 entry records the two digests at launch": CONFIRMED,** checked against the entry's text only.
    - RESULTS.md:49–53, under "The inputs at launch, by digest", gives the prior's sha256 and G-ID-F3's artifact's sha256.
    - The entry adds "Both match LOCK-m-F3 v0.2's values, and both again after the end".
    - The text is present at `2193832` and at HEAD.

20. **"no driver commit has landed since the `qual` wiring (`b427f82`)": CONFIRMED.**
    - `git log b427f82..HEAD -- scripts/mf3_sessions.py` is empty.
    - The three commits since then are `0190c6d`, `2193832` and `a2c354e`; none changes the driver.
    - The driver's blob `4fff3d9a…` is the same at `b427f82`, at HEAD and in the working tree, which is clean.
    - Its sha256 is `285eed04…0e44`, the value at :73.

21. **The PI's word: CONFIRMED** against the relay.
    - The question "Route the seat's p answers as given?" and the word "Route as given" are verbatim at relay:4. The date is at relay:1–2.
    - The same wording is committed at RESULTS.md:434–435 (`a2c354e`).
    - The chat itself is beyond my reach; the relay is the source the brief names.

22. **"The seat's §8 routing block is quoted in full in the close line on G-F0m-OLMo (p) ×3's entry (`a2c354e`).": CONFIRMED.**
    - RESULTS.md:437–444, with the `> ` prefix removed, equals seat:68–75 line for line: all eight items, empty diff.
    - The block sits inside the close at :421–453, which `a2c354e` added: its text is absent at `2193832` and present at `a2c354e`.

23. **"Nothing above is rewritten.": CONFIRMED.** The hunk only adds lines.

24. **No rule or precedent beyond the record: CONFIRMED.**
    - "So … not edited now", "v1.0 carries the close", "both held" and "Nothing above is rewritten" are each Code's own conduct or a reading of seat:31, :52 and :53 and relay:15.
    - The line cites no precedent and states no new rule.

**Observations (no grade; none needs a change)**
- **(a)** Item 12's nested double quotes are verbatim and match house style: RESULTS.md:429 nests quotes the same way.
- **(b)** The second commitment binds "while G-F3 is open", and G-F3 still awaits the seat's read (RESULTS.md:135; relay:14). "Has landed" and "both held" are therefore true up to now (HEAD `a2c354e`). They do not discharge the commitment.
- **(c)** The seat's header (seat:3) said "the PI commits by path". Per relay:7 the pod session made the commit, as that session's own close records (RESULTS.md:423–424). The close line follows the relay.
- **(d)** At seat:31 the seat writes "Ledger (67), §7.", but the ledger entry is in §6 (seat:55–57). The close line gives no section; if one is added, it should be §6.

**Not CONFIRMED**
- **Item 3 (IMPRECISE):** the heading "on v0.2 §8's pointer" should become "on the entry's pointer (v0.2 §8; `15d2f70`)", per seat:62. Per seat:31 and :53, v1.0 is what closes v0.2 §8's pointer.
- **Item 13 (IMPRECISE):** "§3 and §5" labels a sentence that is verbatim only in §3 (seat:31). It should read "§3 (and §5, in its own words)".

**Disclosures:** none.
- Every git form was names-only with `':!data/**'`, or ids and subjects, or digests.
- No search ran over a tree: the greps covered single named files and committed RESULTS.md blobs.
- Nothing under `data/` was opened, listed, sized or traversed, and no stat form was used.
- No model ran, there were no git writes, and no file was written; the shell's process substitution here uses file-descriptor pipes.

HEAD at start: `a2c354e`. HEAD at end: `a2c354e`.
