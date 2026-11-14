# The close line on G-F3's entry: its values-check

*Code's raw, PI date 2026-11-14.*
- *What was checked:* the close line Code added to RESULTS.md on the G-F3 entry (`2193832`), after that entry's
  **Next:** bullet, before the commit that also adds the seat's raw by path.
- *Against:*
  - the seat's raw `results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md` (sha256 `6b963adf…db3a`,
    32,250 bytes, untracked at the check);
  - `WORKFLOW.md` (sha256 `e7195706…b061`, untracked);
  - the coordinating session's routing relay of 2026-11-14, as Code received it;
  - git (`2193832`, `012ffbe`, `0190c6d`) and RESULTS.md.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written. It needed
  nothing under `data/` and opened nothing there. It ran no model.
- *Outcome:* 23 items: 21 CONFIRMED, 1 IMPRECISE, 0 FAIL, 1 NOT CHECKABLE. HEAD was `012ffbe` at its start and at its
  end.
- *Not run:* a second pass. The one IMPRECISE item applies the checker's own fix. The two additions after the check
  (below) carry no figure; Code checked each against the raw by tool.
- *Code's masked scan of the checker's transcript* (counts only; no command text printed):
  - 32 distinct command texts; none names a ckpt path; no metadata form names `data/`;
  - nothing under the tasks directory was touched; no transcript was opened.
- *This raw:* Code's dispositions, then the report verbatim.
  - Code extracted the report by script from the agent's hand-back: sha256 `aa9b8421…2926`, 128 lines, no final
    newline.
  - Code's leak check found no local path, user name, session id or temp-dir id, and no clock time.

## Code's dispositions

- **11, IMPRECISE: the `WORKFLOW.md` §1 anchor.** Agreed. `WORKFLOW.md` is not in the tree at this commit (the
  coordinating session commits it after, its §D item 11). The anchor now cites the raw itself: "(its header: "Code
  commits by path on the PI's routing"; §C, ledger (68))".
- **9, NOT CHECKABLE until the commit.** Checked at the commit:
  - the raw was re-hashed just before it and equals `6b963adf…db3a`;
  - `git show --name-status` lists RESULTS.md, the raw and this values-check raw.
- **Additions after the check, from the checker's optional notes:**
  - a gloss for `r2:` beside the readings of record: "the seat's read of G-TIME-F3's re-run, `54b1e51`, as the raw's
    header defines it". The raw's header carries "`r2:` = the seat's read of G-TIME-F3's re-run (`54b1e51`)";
  - a line naming the raw's other sections' owners: "§B (LOCK-p v1.0 ×3) is the pod session's, and §C (the workflow
    of record; ledger (68)) the coordinating session's (§D items 6–12)". §D's items 6–10 are under "B. p (pod
    session)" and 11–12 under "C. Coordinating session".
- **The observation on the relay's item wording.** The relay's items are the PI's paste block's wording. The close
  line quotes §D, the raw of record, as the relay itself directs ("Its words govern, not this relay."). No change.

## The checker's report (verbatim)

**Blind values-check: the G-F3 close line (uncommitted, RESULTS.md)**

The close line has one IMPRECISE item and one NOT CHECKABLE item, and no FAIL. Every quote is verbatim against its source.

HEAD at start: `012ffbe`. HEAD at end: `012ffbe`. RESULTS.md's working-tree blob (`357c898…`) and the raw's sha256 were the same at the start and at the end.

**Sources and shorthand**
- **raw** = `results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md` (untracked). sha256 `6b963adf126540dab95780d486ab0a6652a1308828548a5cb2763f998040db3a`, 32,250 bytes, 108 lines.
- **WORKFLOW.md** (untracked). sha256 `e7195706efee2704abc6d4e5bae984118e6add58013c9fbf3bdb1da971c6b061`, 11,492 bytes. Both equal relay:7 and relay:11.
- **relay** = C/relay_extract.txt. **close file** = C/close_gf3.md. C is the brief's scratch folder for this close.
- RESULTS.md:N means the working tree, which is HEAD plus the hunk. The close is at RESULTS.md:632–662.
- How quotes were compared: a stdlib Python script run with `python3 -I`. It removed `**` from the source, normalised whitespace across wrapped lines, then tested exact equality or containment.

**Structure**

1. **One hunk, additions only. CONFIRMED.**
   - `git diff -- RESULTS.md` shows one hunk, `@@ -629,6 +629,37 @@`: 31 lines added, 0 removed.
   - The working tree without lines 632–662 equals `HEAD:RESULTS.md` line for line, including the newline at the end of the file.
   - The blob ids match the diff header (`9859192` → `357c898`).
   - Outside `data/` (not inspected, per the brief), RESULTS.md is the only modified tracked file. Nothing is staged.

2. **Placement. CONFIRMED.**
   - The entry's heading is at :519 ("G-F3 (PROPOSAL-m v1.11 §3.2 m:297; …").
   - Its **Next:** bullet, the entry's last, is at :630–631.
   - The close sits at :632–662, followed by the blank line :663 and the next entry at :664 (the pod session's dated note of 2026-11-12).

3. **The text is the close file's. CONFIRMED.** The 31 inserted lines equal C/close_gf3.md:1–31 line for line. There is no trailing whitespace, tab or CR. The only non-ASCII characters are § – — ≈.

4. **`2193832` is G-F3's record, and the entry is unchanged since. CONFIRMED.**
   - The heading appears once in `2193832:RESULTS.md` and not at all in its parent.
   - The commit's subject begins "G-F3 (PROPOSAL-m v1.11 s3.2 m:297; …".
   - The entry's text at HEAD is identical to what `2193832` committed, and `2193832` is an ancestor of HEAD.

**Claims**

5. **"Close (PI date 2026-11-14)" (:632). CONFIRMED.** relay:1–2 gives "PI date 2026-11-14". relay:27 says "date the line with the PI's routing of 2026-11-14". raw:3 gives "PI date 2026-11-14".

6. **"The seat's read of G-F3" (:632). CONFIRMED.**
   - raw:11 is the §A heading "Q-F3 — G-F3's read". raw:3 says the raw is on "the G-F3 entry (`2193832`)".
   - RESULTS.md:1196 uses the same form for a raw that covers more than one track.
   - Optional: that earlier close also said which sections belonged to another track (:1213). Here §B (LOCK-p v1.0) and §C (the workflow, ledger (68)) belong to the pod and coordinating sessions.

7. **The link path and sha256 (:633–634). CONFIRMED.** The file is at the linked path, untracked. Its hash equals the close's and relay:7's.

8. **"on the PI's routing" (:635). CONFIRMED.** relay:2: "the PI routes the seat's answers on G-F3 (and LOCK-p v1.0) as given."

9. **"is committed here by path with this close" (:634–635). NOT CHECKABLE before the commit.**
   - It matches raw:91 (§D item 2: "this file committed by path with it") and relay:25–27 (one commit by path: the raw as placed, plus RESULTS.md).
   - It is true only if the commit carries both paths. Check at the commit: the re-hash before it equals `6b963adf…db3a` (relay:10), and `git show --name-status` lists RESULTS.md and the raw.

10. **Header quote "Code commits by path on the PI's routing" (:635). CONFIRMED, verbatim.** It is a substring of raw:3's bold span "**Placed untracked over the bridge; Code commits by path on the PI's routing**".

11. **The anchor "`WORKFLOW.md` §1" (:635). IMPRECISE.**
   - The substance holds. §1 says the PI "never commits" (WORKFLOW.md:7) and that Code "commits by path at its step … with close lines" (WORKFLOW.md:11). The exact phrase "on the PI's routing" is at WORKFLOW.md:3, :26 and :61, not in §1.
   - The anchoring is off:
     - WORKFLOW.md is untracked, absent from HEAD's tree, and named by no committed file (`git grep` over HEAD with `':!data/**'`).
     - Per relay:12 and relay:29, the coordinating session commits it *after* this commit (its item 11). At the close's own commit, the anchor points to a file that is not in the tree.
     - The anchor is unversioned, and WORKFLOW.md:61 (§9) expects v1.N to replace v1.0 at root.
   - No unstated rule is involved. The convention is stated in the raw committed with the close: raw:3 (header), raw:9 (§0 C), and raw:79 (§C: "Code commits by path on the PI's routing; the PI routes and decides in chat and commits nothing.").
   - **Fix:** either cite the raw, as "(its header: "…"; §C, ledger (68))", or pin the file, as "`WORKFLOW.md` v1.0 §1 (sha256 `e7195706…b061`, committed after this close at the coordinating session's §D item 11)".

12. **The §0 first-bullet quote (:635–638), "verbatim (bold markers aside)". CONFIRMED.**
   - :638 equals raw:7 exactly once the "- " list marker and every `**` are dropped. The dashes and ≈ are identical characters.
   - raw:7 is §0's first bullet (§0 heading at raw:5). raw:91 calls it "§0's first bullet".

13. **"The readings of record (§A.4), for every later count of (b)" (:640). CONFIRMED.**
   - raw:21: "The reading of record, for every later count:" (the task-echo reading).
   - raw:25: "The seat's rule for the one-word cases, declared here for later counts:".
   - raw:7 and raw:90 call both of them "readings of record". §A.4 (raw:19) is counter (b)'s section.
   - The word "every" comes from raw:21. raw:25 says "later counts", which has the same scope.

14. **The task-echo quote (:641–643). CONFIRMED, verbatim.** It is contained in raw:21.

15. **The one-word quote (:644–646). CONFIRMED, verbatim.** It is contained in raw:25. The raw puts it in italics (`*…*`); only that markup is dropped.

16. **"The run's facts (§A.6): the listings and `0190c6d`" (:647). CONFIRMED.**
   - raw:48 is in §A.6: "the three harness listings … and the one commit that landed (`0190c6d`, RESULTS.md only)".
   - `0190c6d` resolves to `0190c6de…`, whose subject is the pod session's dated note. It is an ancestor of `2193832` and of HEAD.
   - The entry also names it (RESULTS.md:556).

17. **The quote "`r2:`Q3's class — not a departure, mid-stage or after; nothing is needed." (:647–648). CONFIRMED, verbatim** (raw:48).

18. **The quote "The entry's missing write-time stamp line is within the G-TIME-F0 Q4 ruling; the commit time stands for it; nothing changes." (:648–649). CONFIRMED, verbatim** (raw:48).

19. **The PI's word (:650–651). CONFIRMED** against the relay.
   - The question "Route the seat's answers as given?" and the answer "Route as given" are verbatim at relay:4. The date "its relay of 2026-11-14" is at relay:1–2.
   - The form matches the committed closes at RESULTS.md:961, :1217 and :1582.

20. **"The routing block's section A (§D), so adopted, verbatim (bold markers aside)" and its five items (:651–658). CONFIRMED.**
   - Each of :654–658 equals raw:90–94 exactly once `**` is removed (item 4's "**Your cap for Q-F3**").
   - Item 2's `2193832` is verified at my item 4.
   - "So adopted, verbatim" is the record's established form (:961, :1217, :1582).
   - Observation, no fix required: relay:17–22 gives items 1–5 "verbatim from the PI's block" in different wording:
     - item 1 lists the four (b) responses;
     - item 2 says "quoting §0 bullet A";
     - item 3 adds "(m:285)" and "§A.5's hours … by citation of the raw";
     - item 4 adds "(m:298, m:249)" and ends "PI confirms.";
     - item 5 adds "in LOCK-p v1.0's manner" and the "preprint of record pending" clause.
   - So the PI pasted the paste block, not §D's text. Quoting §D, the raw of record, agrees with relay:9 ("Its words govern, not this relay.") and WORKFLOW.md:15.
   - These sources cannot tell whether relay item 4's closing "PI confirms." is the seat's wording or the PI's own. It bears only on the cap, which is decided at G-PWR's entry.

21. **"Next (§D items 3–5)" (:660–662). CONFIRMED.**
   - It matches raw:92–94. "By citation of this raw" comes from raw:50 (§A.7). "Then" reflects item 5's "[go after your cap]".
   - Item 4's alternative (declining v1.0, which makes Q-F3 NOT-RUN by D2) is not in the Next line. It is quoted in full at :657, and raw:7 words the step the same way ("the PI sets the cap at G-PWR's entry").

22. **No rule or precedent beyond the record. CONFIRMED,** apart from item 11's anchor.
   - The commit convention is stated in the raw (raw:3, :9, :79).
   - The scope of the readings is the raw's (raw:21, :25).
   - The "so adopted" form is committed practice.
   - There is no new ledger line.

23. **No clock time, stamp or "$" in the inserted lines (relay:40). CONFIRMED.** A regex scan found none. The hour and second figures are inside the verbatim §0 quote and are the seat's projections.

Ungraded observation: `r2:` appears twice inside verbatim quotes (:641, :647) without a gloss. raw:3 defines it as "the seat's read of G-TIME-F3's re-run (`54b1e51`)". An earlier close glossed the seat's `gid:` the same way (RESULTS.md:972). A half-line gloss is optional.

**Tally:** 23 items: 21 CONFIRMED, 1 IMPRECISE, 0 FAIL, 1 NOT CHECKABLE.

**Not CONFIRMED:**
- **11, IMPRECISE.** The `WORKFLOW.md` §1 anchor names a file that is not in the tree at this commit (the coordinating session commits it afterwards, its item 11), and the anchor is unversioned. Cite the raw's header and §C, or pin it as "`WORKFLOW.md` v1.0 §1 (sha256 `e7195706…b061`), committed after this close".
- **9, NOT CHECKABLE until the commit.** Confirm at the commit that the re-hash before it equals `6b963adf…db3a` and that `git show --name-status` lists RESULTS.md and the raw.

**Conduct:** I stayed read-only throughout. There were no git writes and no files written, no model was run, and nothing under `data/` was opened, listed or sized.
- Content searches were either `git grep` over HEAD's tree with `':!data/**'`, or single-file greps of RESULTS.md, WORKFLOW.md and the raw.
- `git show --name-status` carried `':!data/**'`, and `git hash-object` ran without `-w`.
- I ran `git status --porcelain` once, limited by pathspec to RESULTS.md, the raw and WORKFLOW.md. It printed names and status codes only, so it is narrower than the bare form item 1 permits.
- No departures.

HEAD at start `012ffbe`; at end `012ffbe`.
