# ADDENDUM-m2 v0.2, OPEN #50 — the blind values-check of the block, its entry and the referent raw's changed dispositions, with Code's dispositions

*Code's raw, PI date 2026-11-08. A fresh agent checked the Code → design block on #50, its RESULTS entry, and the referent raw's "What decides the commit" paragraph and row 50, read-only, at HEAD `9624f70`. Its report follows verbatim (the harness's indentation removed). Its line numbers are the drafts' at the time of the check. Code's dispositions close the file.*

---

## The agent's report (verbatim)

**Values-check of the three A-m2 v0.2 / #50 drafts: 40 items, 29 CONFIRMED, 9 IMPRECISE, 0 FAIL, 2 NOT CHECKABLE.**

I worked read-only. HEAD was `9624f70` at the start and at the end, and the working tree is unchanged (41 entries). I never opened `data/mf3/ckpt/`. Python ran from stdin only.

Every quotation mark in the three drafts encloses verbatim text; I checked each one by script. The IMPRECISE items are about scope, unmarked truncation, unnoted bold, one anchor and one consistency point.

Short names: blk = the open50 block; ent = entry_open50.md; ref = the referent-check draft; v0.2 = the addendum; m = PROPOSAL-m v1.11; pre = the pre-read raw; f6 = `results/raw/2026-11-06_ganl-f3_design-to-code_answers.md`; lock = LOCK-m-F3.md; drv = `smoke-wt/scripts/mf3_sessions.py`.

### Draft 1: blk

1. **Header facts (blk:3).** CONFIRMED.
   - v0.2 is untracked and hashes to `69e23212…cb47`.
   - ans2 hashes to `09d856ef…ea29` and was added at `de729c4` (`git show --stat`).
   - `git log --all` on both A-m2 paths is empty, so v0.2 is not committed.
2. **STOP quote, "any unresolved substantive item → STOP"** (blk:3, ent:16, ref paragraph). CONFIRMED, verbatim at v0.2:71.
3. **blk:7–9, the blockquote of "v0.2 §3.4 (line 48)".** IMPRECISE (minor).
   - It is a verbatim prefix of v0.2:48 (832 of 1,155 characters, `**` kept).
   - It stops before line 48's closing bold sentence ("**At VERDICTS the analyzer is untouched: … at the lock's re-issue.**") with no "…" or note.
4. **blk:11, the ans2 §1 quote.** CONFIRMED, verbatim at ans2:7.
5. **blk:15, "every Q-F3 gate stage but G-ID-F3 runs contrast sessions (A1, A2, A3)".** CONFIRMED.
   - mf3/keys.py:28 has `GATES` = time, id, qual; :31 has `GID_TEMPLATES` = A2s, A3s.
   - schedule.py:96–99 `GATE_PLAN`: time runs one session per template of the six; id runs A2s and A3s; qual runs A1 4, A2 4 and A3 8 contrast sessions.
   - Also m:293, :295, :297 and lock:489 (F44).
   - Note: G-PWR (m:298) runs no session. The campaign is a stage (keys.py:29 `STAGES`) but not a gate (see 15).
6. **blk:17, m:271's first quote, "(bold in m:271)", and "a free round's class sits on the pick".** CONFIRMED. All verbatim; the bold run is exactly the quoted span.
7. **blk:17, "with its free rounds removed entirely".** IMPRECISE (minor; emphasis only).
   - The words are verbatim, but they sit inside m:271's bold run "**a contrast-template transcript is read with its free rounds removed entirely — … their responses**".
   - The draft's bold note covers the first quote only.
8. **blk:18, the m:263 quote.** IMPRECISE (minor; emphasis only).
   - The words are verbatim, but the whole span is bold in m:263 (the run opens just before "for"), and this is not noted.
   - What it says m:263 withholds is right. m:263 also bars "a tag, a free round's index, or the render" from every printed exclusion, sham ones included.
9. **blk:19, F-6's anchor and quote.** CONFIRMED. f6:29; both segments are verbatim, and the "…" stands for the CAP TRIGGER / "k of ≤ 36" clause.
10. **blk:15/19 and ent:8–9: the three rules withhold contrast free-phase content at every gate stage but G-ID-F3.** IMPRECISE.
    - F-6 binds, by its own words, G-TIME-F3 only: "for a contrast session at G-TIME-F3" (f6:29; lock:436, :513–515).
    - The window "VERDICTS entry or NOT-RUN record" is m:271's wording. m:263 says "to VERDICTS … (§3)" and F-6 says "before VERDICTS".
11. **blk:21, "over all sessions … at each stage's entry".** CONFIRMED, at v0.2:48, in order.
12. **blk:22 and :25: (b)'s listing "by session and round" over free rounds is a free-round class on the pick, and the seat cannot confirm a contrast (b) item without the removed round.** CONFIRMED. v0.2:48; m:271 (its read rule); m:318 exception (3).
13. **blk:23, "(a) per reasoning line, which F-6 bars. Even (a)'s counts are line-level information about the free phase."** IMPRECISE.
    - §3.4 asks for (a) "tabulated" (v0.2:48); only (b) is listed.
    - F-6's bar is G-TIME-F3's.
    - At G-F3 the lock reports each contrast session's **first** reasoning line by class, as pick-free, and withholds only the later lines (lock:505 F60; readrule.py:21–23, :436–442, :458–464, :510–513).
    - "Even (a)'s counts…" is Code's argument, not any rule's words.
14. **blk:29, G-ID-F3 runs A2s and A3s only, read in full.** CONFIRMED. m:295; m:271 ("G-ID's sham-only sessions are read in full"); m:318 exception (4); lock:459 (F14).
15. **blk:29 says #50 binds "the campaign's looks" (also ent:21); blk:1, :15, :35, :40 and ref row 50 scope the conflict and the fix to gate stages.** IMPRECISE (scope and consistency).
    - m:271's withholding sentence begins "At every gate stage".
    - At looks the governing text is m:318: "at looks, pooled pre-pick exclusion counts per arm", plus its no-pick-read rule. m:263 also reaches the looks.
    - The referent raw's own #50 cites m:318 (ref:216). blk and ent name three rules and drop it.
    - The §4 fix ("At every gate stage", "a gate stage's entry") leaves the looks that §3 says #50 binds without a rule.
16. **blk:30, the smoke: twelve sessions, sham-only, belonging to no unit, declared readable in full.** CONFIRMED, v0.2:44.
17. **blk:31, "At VERDICTS the window closes (m:271)", with the counters computed in Code's own step (ans2 §4).** CONFIRMED. m:271; ans2:20–22; v0.2:48.
18. **blk:37, the contrast forced rounds "which m:271 reads and reports beside".** CONFIRMED, m:271.
19. **blk:40, the fix sentence's window (also ref row 50 and ent:23).** IMPRECISE (minor).
    - The sentence opens "before the unit's VERDICTS entry or NOT-RUN record" but closes "computed and reported at VERDICTS".
    - That drops the NOT-RUN record, where m:271 releases the withheld events.
    - ref row 50 and ent shorten both halves to "VERDICTS".
20. **blk:44, #48's facts.** CONFIRMED.
    - pre:164 is verbatim, and `cdcc8e86…53f0` is v0.1's hash (computed).
    - ans2:13 and :18 read "A-m2's sha and the four literals checked".
    - v0.1 is never committed: v0.2:3, :72, and the empty `git log`.
21. **blk:44, "The smoke driver pins it".** CONFIRMED.
    - drv:536–537 holds the v0_2 path and the full `69e23212…cb47`, checked at :564–568 against the committed blob (:582–587).
    - The round-2 self-test's one FAIL is that check refusing the uncommitted v0.2 (r2rev_selftest.txt:166), which is expected before the commit.
22. **blk:45, #49: §3.3 has no clause for a smoke stopped under P4 by a G-VER failure, a task-round `scaffold_absorption`, the backend or the snapshot.** CONFIRMED.
    - v0.2:46 has only the rule's own two stops.
    - The four causes are at pre:181, :183, :173, and :166/:168.
    - Note: the list is not exhaustive. The driver also stops on the licence, startup checks, provenance, the output directory, a line read that raises, and the model id (drv:850–874, :909–911, :983–985).
23. **blk:45, "The driver prints no tally and no rule after a STOP".** CONFIRMED.
    - Every STOP raises SystemExit before :917–933 (TALLY, RULE, STOPS, summary.json): see :855, :861, :866, :874, :906, :910, :914.
    - The self-test agrees (r2rev_selftest.txt:189 "no summary, no rule printed", :193).
    - Note: §3.3's own two stops are not P4 STOPs. When they fire, the tally and the rule are printed with "FIRES" (:928–930).
24. **blk:49, Code's lean (a), with #50 as a FLAG.** CONFIRMED; consistent with ent:32 and ref row 50.

### Draft 2: ent

25. **The counts, 51 / 35 / 13 / 3 OPEN / 0 FAIL.** CONFIRMED.
    - They match ref:19.
    - My recount of items 1–51: IMPRECISE are 3, 4, 5, 11, 12, 14, 21, 30, 34, 41, 44, 45, 47; OPEN are 48, 49, 50; 0 NOT CHECKABLE.
26. **ent:7–9, the content of the three rules.** CONFIRMED (v0.2:48; m:271; m:263; f6:29). The scope caveats of 10 and 15 carry.
27. **ent:10, "ans2 §1 has Code list "by session and round"".** IMPRECISE (anchor).
    - The quote is verbatim (ans2:7).
    - "ans2" is not defined in the entry, and RESULTS.md already uses "ans2" for the p track's answers (RESULTS.md:945, :953, :990, :1012, :1292).
28. **ent:11–14, the coordinating session's instruction.** NOT CHECKABLE.
29. **ent:17–25, the summary of the block.** CONFIRMED against blk.
    - Wording note: in "(a) and (b) over sham sessions only, plus (b)…", the block's "only" belongs to (a) alone (blk:36–37).
30. **ent:26–27, "the agent's report verbatim", with every non-CONFIRMED item disposed.** CONFIRMED.
    - The embedded report equals `scratchpad/am2/v02ref_report_extracted.md` line for line once indentation is stripped (0 differences).
    - 16 of 16 items are disposed: three OPEN rows, and 13 IMPRECISE items in 11 rows.
31. **ent:31–34, Next (a) and (b).** CONFIRMED. v0.2:72; ans2:47; blk §6.
32. **"Second blind review round is running" (ent:36) and "Nothing ran on a model" (blk:3, ent:30).** NOT CHECKABLE.

### Draft 3: ref, the paragraph and row 50

33. **"No item changes a form's bytes, a bar, a key, a cell or the selection rule, nor a figure the ruling or the rule reads."** CONFIRMED on a re-read of the 16 items.
    - The closest case is #49: its reading supplies the outcome for a case §3.3 has no clause for (ref:206–209).
34. **"OPEN #50 is substantive" and the STOP quote.** CONFIRMED (v0.2:71; #48 and #49 are marked "OPEN (minor …)", #50 is not).
    - Note: the report files #48 and #49 under "### 6. Unresolved and substantive" too (ref:199).
35. **"as at PROPOSAL-p's v0.2 commit (`18b0111`) … dated notes".** CONFIRMED.
    - The commit message reads "v0.2 is committed as delivered; the items go to the seat as dated notes".
    - That check had no OPEN item, so the precedent covers the procedure only.
36. **The PI's ruling first, and #50 in its own block at its path.** CONFIRMED; the path matches blk's filename and ent's link.
37. **Row 50's re-check column (the v0.2:48 quote; m:271).** CONFIRMED, verbatim and in order.
38. **Row 50: "before the G-TIME-F3 re-run (the first stage it binds)"; binds neither the commit nor the smoke.** CONFIRMED. v0.2:54, :58, :44.
39. **Row 50's disposition, "FLAG for the seat".** IMPRECISE (minor; consistency). It states the no-STOP path as settled, while the paragraph above it, blk §6 item 1 and ent's Next leave FLAG against STOP to the PI.
40. **Row 50's fix summary.** CONFIRMED against blk §4. The caveats of 15 and 19 carry.

**Totals:** 40 items: 29 CONFIRMED, 9 IMPRECISE (3, 7, 8, 10, 13, 15, 19, 27, 39), 0 FAIL, 2 NOT CHECKABLE (28, 32). Items 7 and 8 are the same kind of defect, and item 13 shares item 10's F-6 scope point.

**Two things outside the drafts:**
- The agent's verbatim #50 anchors F-6 at "lock:512–513". The ruling is at lock:513–515; line 512 is F59's.
- `daca8b0`'s commit message gives v0.1's hash as "cdcc8e86...f3f0". The file hashes to …53f0, which is what RESULTS.md:54 and :540 and these drafts have.

---

## Code's dispositions

Every IMPRECISE item was re-checked at source and applied. Each new or changed quote was checked again by script against its source, verbatim: F60, m:318, and m:271's window phrase. The two NOT CHECKABLE items (28, 32) are process claims.

| Item | Applied |
|---|---|
| 3 | The §3.4 blockquote is followed by a note that v0.2:48 goes on to the VERDICTS path in Code's own step, omitted. |
| 7, 8 | "(bold in m:271)" on the read-rule quote; "(bold in m:263)" on m:263's. |
| 10, 13 | F-6 is cited as G-TIME-F3's ruling. F60 is added as G-F3's form, where a contrast session's first, pre-pick reasoning line is reported by class and the later lines are withheld. (a) is described as "tabulated over its reasoning lines", and the claim that counts over later lines are free-phase information is marked as Code's reading. |
| 15 | m:318 is added for the campaign's looks ("at looks, pooled pre-pick exclusion counts per arm"). The fix now covers the looks: neither counter is reported at a look, for any arm. |
| 19 | The fix's window reads the unit's VERDICTS entry or NOT-RUN record (m:271) at both ends, in the block, the entry and row 50. |
| 27 | The entry cites "the seat's answers (`de729c4`, §1)", not "ans2", which RESULTS.md uses for the p track. |
| 29 | The entry's summary of the fix is restated per counter. |
| 39 | Row 50 reads "To the seat in its own block … whether it is a FLAG or fires v0.2 §6 item 1's STOP is the PI's." |
| (outside the drafts) | The referent raw notes that its report places F-6 at "lock:512–513"; the ruling stands at lock:513–515. |

**The fix as revised** (the block's §4) also admits a contrast session's first reasoning line to (a) where the stage reports that line's class (G-F3, F60). This follows the lock's existing form, and the seat rules.

