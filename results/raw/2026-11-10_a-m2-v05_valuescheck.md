# ADDENDUM-m2 v0.5's commit — the values-check, one blind pass

*Code's raw, PI date 2026-11-10.*
- *What was checked:* the drafts of
  - the referent raw's header, its dispositions, and its items outside the delta;
  - the entry.
- *How:* one blind agent, read-only, one pass.
  - Its brief quoted the list of record v2's items 1–5 as written (the list ruling of 2026-11-10, §2), named item 3's tested pathspec, and barred any read under `data/`. It allowed the referent agent's transcript only through Code's masked scanner.
  - By its report, HEAD was `fc43249` when it started and when it ended.
- *Outcome:* 71 items: 55 CONFIRMED, 6 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE.
  - Each IMPRECISE item is applied (below).
  - No second pass was run: none of the items was a FAIL, and each fix is either the checker's own wording or a citation it checked.
- *This raw:* Code's dispositions of every item not CONFIRMED, each re-checked at source, then the report verbatim (extracted by script from its hand-back).
  - In the report, the two draft paths' local root is replaced by `<scratch>`.
  - Its item 17 listed the path prefixes it searched for; Code reworded that list in words, as marked there.
- *The checker's compliance:* Code's masked scans of its transcript match its account:
  - two content searches, each carrying `':!data/**'`, with no protected path class in their output;
  - every `data/` its commands name is an exclusion pathspec, or a string it tested in Code's briefs;
  - one `wc -c`, on an addendum at root.
  - It disclosed one possible departure (below).
- *Nothing ran on a model.*

## Code's dispositions

- **14, IMPRECISE: "resolved in the record" rests on a step the drafts do not cite.** Agreed.
  - Applied: the 3.18 disposition (in the referent raw) and the entry now cite v0.5's §5 heading, "(the routing block is their record)" (v0.5:81), and its item 3's order, "the battery run, the review, the re-runs" (v0.5:85). A5's "[go]" is the PI's decision on that order.
  - The drafts claimed no precedent for resolving a substantive item without a STOP, and none is claimed now.
- **22, IMPRECISE: the scan's "no tool input that reads under `data/`".** Agreed; applied in the checker's words.
- **23, IMPRECISE: "no barred metadata form" claims more than the scanner tests.** Agreed.
  - Applied: "no `--stat`-family form".
  - Added: a second masked check Code ran over the referent agent's 72 distinct Bash calls. It found no `find`, `du`, `stat`, `mdfind`, `ls -l`/`-t`/`-s`, `wc -c`, `git cat-file -s` or `git ls-tree -l` form.
- **28, IMPRECISE: the 2.3 disposition's classification of the unlisted changes.** Agreed.
  - Applied: the unlisted changes include requirements already stated in `ans5:` §1–§2, §7 and §8 item 5, and in A1, A2 and A5.
  - None departs from those sources or moves a form, a bar, a cap or a key.
- **47, IMPRECISE: the attribution of the 1,728 count.** Agreed; applied in the checker's words.
- **60, IMPRECISE: "some within-line changes".** Agreed; now "many".
- **NOT CHECKABLE 16 (the report verbatim):** the report section is extracted by script from the agent's hand-back call, and the referent raw's header now says so.
- **NOT CHECKABLE 51 (forward commitments in the present tense):** applied: "will record", "will say", "will cite", "will run".
- **NOT CHECKABLE 55 and 66 (the routing's file list and its header line):** both are now quoted verbatim in the entry, as the coordinating session relayed them.
- **NOT CHECKABLE 19, 24, 27, 53, 70 and 71:** process claims, placeholders, and this commit's own effects. Nothing to apply.
- **Optional refinements:**
  - 38, 39 and 59: added, the refusal lines (`m_analyze.py:11092–11096`; `gshape.py:256–258`);
  - 58: added, the link text names the items outside the delta;
  - 36: left as written.
- **The possible departure the checker disclosed:** one pathspec-limited `git status --porcelain -- <five addenda at root and in archive/>`, where the list's item 1 names the bare form.
  - It printed four `??` lines. Nothing under `data/` was named or printed.
  - The same pathspec-limited form is used in two other places, listed here with the checker's call:
    - the RESULTS.md protocol the coordinating session set (a clean `git status --porcelain RESULTS.md` before each insert);
    - this session's own call over two v0.4 paths while staging this commit.
  - Disclosed for the seat under the list's item 8. Code rules on none of it.
- **Its other disclosures:** substring tests of Code's scratch briefs, and a `cat -A` that printed only a usage message. Neither touched anything under `data/`; recorded here.

## The checker's report (verbatim; local paths replaced)

## Values-check of the A-m2 v0.5 drafts: the referent raw and the RESULTS.md entry

**HEAD at start:** `fc43249`. **HEAD at end:** `fc43249`. The brief matched: sha256 `627cc0c355e65913…`, 37 lines.

**Result:** 71 items. 55 CONFIRMED, 6 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE.

Files checked:
- R = `<scratch>/v05/2026-11-10_a-m2-v05_referent-check.md`
- E = `<scratch>/v05/entry_v05_commit.md`

Every hash was recomputed and every quoted routing line compared byte for byte. I ran Code's masked scanner as the brief directs.

### Part A — R, the referent raw (header :1–19, dispositions :231–254, outside :256–264)

1. **CONFIRMED.** The title names v0.5 §6 item 1 (v0.5:90).
2. **CONFIRMED.** "PI date 2026-11-10" (:3) matches the date on v0.5:3 and ans5:3, and the system date.
3. **CONFIRMED.** What was checked (:4) is what v0.5:90 lists: `stop:`, `ans5:`, `read:`, `smoke:` and the file. The report does read the smoke raw (R:126–131).
4. **CONFIRMED.** v0.5's sha256 is `f27505c5…5354` and it is untracked (`??`).
5. **CONFIRMED.** v0.4 is `8f8ef932…714a`, untracked, with 0 commits on any ref under either path.
6. **CONFIRMED.** `ans5:` is `a85b9249…8faf`; `git show --name-status 0516832` shows `A` for it.
7. **CONFIRMED.** "A blind agent, read-only" (:8) is in Code's scratch copy of the brief (`S/brief_referent_v05.md`) and in the report (R:228).
8. **CONFIRMED, with a caveat.** The brief (:9) quotes v2's items 1–5 exactly as v2 raw:18–22 has them, gives both tested pathspec forms, and says "nothing under `data/`" four times. I checked this by substring test on Code's scratch copy (sha256 `58b20d19…`). The scanner prints no prompt, so I cannot show that this copy is the brief that was sent.
9. **CONFIRMED.** HEAD `42c5a92` at start and `fc43249` at end, "by its report" (R:25). The commit times (06:33Z and 06:43Z) fall before the handback at 07:01Z.
10. **CONFIRMED.** `fc43249` is the coordinating session's close on `750a7dd`'s entry, with the list ruling. Evidence: its subject; blame puts RESULTS.md:129–170 at `fc43249`; RESULTS.md:153 says "coordinating session owns the close"; the commit adds the v2 raw.
11. **CONFIRMED.** "Of the files the check reads, it touches only RESULTS.md." `fc43249` modifies RESULTS.md and adds the v2 raw, which is the rule's source and not one of v0.5:90's sources. The report gives its anchors as of `fc43249` (R:27).
12. **CONFIRMED.** The tally 40 = 35 + 5, 0 OPEN, 0 FAIL. I recounted the items 1.1–1.6, 2.1–2.3, 3.1–3.30 and 4.1 (R:29–32).
13. **CONFIRMED.** Item 3.18 is substantive and concerns the order of steps (R:34, :164).
14. **IMPRECISE (anchoring).** "It is resolved in the record … so §6 item 1's STOP does not fire" appears at :12, :247 and E:17/:22.
    - Its factual basis holds (items 34–40 below).
    - But "resolved" depends on a step the drafts never cite: that the routing's order governs §4.3's arrows.
    - The agent passed this question to Code ("your call", R:37) and named the seat as what settles it ("the seat … rules that §6 item 4 governs", R:169).
    - The committed anchor exists:
      - §5's heading, "the routing block is their record" (v0.5:81; committed at v0.3:62; also m:16);
      - §5 item 3 itself orders "the battery run, the review, the re-runs" (v0.5:85);
      - A5's `[go]` is the record of that decision.
    - **Fix:** cite v0.5:81 and :85, and say why the record already settles what the agent left to the seat.
    - No committed precedent covers a substantive item resolved without a STOP. The v0.3 precedent at RESULTS.md:996–997 covers only non-substantive items. The drafts do not claim a precedent.
15. **CONFIRMED.** The other four items are non-substantive and all five go to the seat as dated notes (:13; R:237, :238, :248, :251, :254).
16. **NOT CHECKABLE.** "The agent's report verbatim" (:14). The scanner prints no output text. The masked first 500 characters of the agent's handback, as the scanner prints them, equal the draft's report section masked the same way.
17. **CONFIRMED.** "It holds no local path": no home-directory, private-temp, temp, scratchpad or home-shortcut path prefix anywhere in R [the list of prefixes reworded in words by Code].
18. **CONFIRMED.** There is a disposition for every item not CONFIRMED (5 of 5).
19. **NOT CHECKABLE.** "Each re-checked at source" (:14, :231) is a claim about Code's process. Where I could test the dispositions' own claims at source, they hold, except items 28 and 47.
20. **CONFIRMED.** The items outside the delta include the correction to the STOP block (:258).
21. **CONFIRMED.** The scan's description and "three content searches" (:15–16). The scanner shows three:
    - `git grep … -- . ':!data/**'`;
    - a recursive grep over `results/raw/`;
    - a recursive grep over `valence_core/mf3` and the driver.
    No protected path class appears in any output.
22. **IMPRECISE.** "No tool input that reads under `data/` (each `data/` it names is an exclusion pathspec)" (:17).
    - Five of the six hits are commands whose visible `data/` is `':!data/**'`. The scanner cuts the fifth at 500 characters, so its tail is unseen.
    - The sixth hit is the agent's handback: its report prose names `data/`, not as a pathspec.
    - No Read call named `data/`.
    - **Fix:** "each `data/` a command names is an exclusion pathspec; the sixth hit is the report's own text".
23. **IMPRECISE.** "No barred metadata form" (:18) claims more than the scan tests.
    - The scanner tests only the `--stat` family. Its single hit is the handback's compliance sentence, not a command.
    - It also cannot see a tree-wide form that names no `data/`, such as an unpruned `find` or `git ls-tree -l`.
    - **Fix:** "no `--stat`-family form, and no command naming `data/` except as an exclusion pathspec".
24. **NOT CHECKABLE.** "Nothing ran on a model" (:19). It agrees with the agent's account (R:228).
25. **CONFIRMED.** The 2.3 heading reads the report correctly (R:53), and "(every changed line; …)" is verbatim at v0.5:7.
26. **CONFIRMED.** My diff shows the same 15 changed lines (3, 5, 7, 63, 71, 73, 75, 77, 84, 85, 90–93, 97). Both named changes exist: v0.4:5 → v0.5:5 ("step commit" → "commit"), and v0.4:71 → v0.5:71 (the added clause).
27. **NOT CHECKABLE.** That Code ran "its own line and word diff" and found the two changes "independently" (:234). No artifact shows it.
28. **IMPRECISE.** The classification at :235: "Each unlisted change is a header, a date, an anchor, a citation, a summary, or a record of the PI's decision. None moves … a file that moves … or the order."
    - Several unlisted changes are requirements, and two of them are order and file-scope statements:
      - v0.5:93 adds "→ the build's commit, its entry naming every file that moves" between the review and the re-runs. That is the very order element 3.18 turns on, and Code's own 3.18 disposition relies on §6 item 4.
      - v0.5:93 changes "(mf3 only; §4.2)" to "(mf3 and the driver; §4.2)" and adds "the real-side assertions included".
      - v0.5:75 adds to the lock re-issue's contents "the stub path's admission (§4.2)", "the driver's blob" and "the list of record cited in one line".
      - v0.5:91's commit items (the routing blocks and the close line).
      - v0.5:73's "re-runs no gate by itself … The BUILD entry names every file that moves and the DRIVER line's new blob".
    - All of these track `ans5:` (:13, :19, :46, :55) and the routing's A1, A2 and A5, so "non-substantive" stands.
    - **Fix:** add "or a requirement already stated in `ans5:` §1–§2, §7 and §8 item 5 and in A1, A2 and A5 (among them §6 item 4's added '→ the build's commit' and the driver in the build's scope); none departs from those sources or moves a form, a bar, a cap or a key."
29. **CONFIRMED.** The §4.1 clause (v0.5:71) records A2 "[adopted]" (RESULTS.md:31).
30. **CONFIRMED.** "lists every changed line" is verbatim at `ans5:`29, in §4.
31. **CONFIRMED.** Item 3.12: both tags are in v0.5:7, and the disposition reads R:122–124 correctly.
32. **CONFIRMED.** The 3.18 description (:239) matches v0.5:75 and R:34 and :165.
33. **CONFIRMED.** The four phrases in :240 are verbatim and run in the stated order in v0.5:75: "G-SHAPE-F3 re-runs" (character 307), then the battery phrase (585), then the review (914), then "LOCK-m-F3 v0.1 is re-issued" (1015).
34. **CONFIRMED.** Source 1: "Code's block, in order" is §6's heading (v0.5:88), and item 4's chain (v0.5:93) runs battery → review → commit → re-runs → lock.
35. **CONFIRMED.** Source 2: A5 at RESULTS.md:104 gives the same order and ends `[go]`.
36. **CONFIRMED, with a note.** Source 3: `ans5:` §7 (`ans5:`46) gives battery → review → commit, "then §4.3's chain". It names the re-runs and the lock only by that reference.
37. **CONFIRMED.** Source 4: `ans5:` §8 item 5 (`ans5:`55) gives the explicit order. These four sources match the agent's (R:35, :166).
38. **CONFIRMED.** `ganl_commit_problems` is at m_analyze.py:11059–11070 and lists `valence_core/mf3/*.py` and the Q-F3 closure. The refusal itself is in `run_ganl` at :11092–11096 (exit 2).
39. **CONFIRMED.** "needs every source committed at HEAD and unedited" is verbatim at mf3_sessions.py:15, in a sentence that begins on :14. The operative refusal is at gshape.py:257.
40. **CONFIRMED.** "§4.3's literal order cannot run" follows from items 38–39. "A5's order, which is also §6 item 4's" checks out (RESULTS.md:104 against v0.5:93).
41. **CONFIRMED.** The 3.18 dated note ("one place late") agrees with R:168.
42. **CONFIRMED.** 3.19: "the list of record cited in one line" is at v0.5:75. "cites the list v2" is verbatim at RESULTS.md:104, and "LOCK-m-F3's re-issue and LOCK-p v0.2 cite v2" verbatim at RESULTS.md:155.
43. **CONFIRMED.** 3.26: the close line is among v0.5:91's items; A5 puts it first; it is committed at `0516832` (blame of RESULTS.md:82–104), which precedes `42c5a92`.
44. **CONFIRMED.** `stop:`93 reads "removes no line and adds 1,728".
45. **CONFIRMED.** I recounted `git diff acde2d8 9c7062e -- scripts/mf3_sessions.py`: 1,855 lines added (1,728 non-blank, 127 blank), 0 removed. `9c7062e` is the only commit on the driver since `acde2d8`.
46. **CONFIRMED.** The line's point stands (0 lines removed). `stop:` was committed at `50fea90`, and the correction also appears at E:29–31.
47. **IMPRECISE (attribution).** The values-check raw at ":38, :184, :394" "confirms" 1,728.
    - :38 is under that raw's "## Code's dispositions" (:22): it is Code's own "applied" line.
    - The checker's two passes carry the count at :184 (pass 1, which begins at :68) and :394 (pass 2, which begins at :327; graded CONFIRMED).
    - **Fix:** "the v0.4 values-check's two passes carried the same count (:184, :394), and Code's disposition applied it (:38)".
48. **CONFIRMED.** "[as written]" is at v0.5:84. A1 is "[as ruled]" (RESULTS.md:100) and A2 "[confirmed]" (:101). "The routing governs" has a committed basis: "the routing block is their record" (v0.3:62, m:16). Optionally cite v0.5:81.
49. **CONFIRMED.** `ans5:` §6's condition is paraphrased correctly (`ans5:`41).
50. **CONFIRMED.** "the build makes it a table" is verbatim at v0.5:73. "m:174's pair (60, 120) at every stage" matches v0.5:73, `stop:`53, m:174 and scaffold.py:44.
51. **NOT CHECKABLE (forward commitments).** These are stated as if done or settled, but are future:
    - "the BUILD entry records both" (:263);
    - "the BUILD entry says what the table holds" (:264);
    - "the re-issue cites v2" (:250);
    - "Code runs A5's order" (:247).
    Consider "will record" or "will say".

### Part B — E, the entry draft

52. **CONFIRMED.** The heading matches v0.5:91's commit title and A5.
53. **NOT CHECKABLE.** `@@STAMP@@` is a placeholder.
54. **CONFIRMED.** The full sha256 `f27505c5…5354` matches, and the size 32,814 B matches `wc -c` and RESULTS.md:96.
55. **NOT CHECKABLE.** "tracked at root" is the commit's effect; the file is untracked now. "Recomputed at write time against the routing's list": no committed text holds the routing's file list.
56. **CONFIRMED.** v0.3 is `83093812…fa67`, committed at `46773e2`. v0.4 is `8f8ef932…714a` and was never committed. Both moves are "as v0.5's header and §6 item 2 have it" (v0.5:3, :91), and v0.1 and v0.2 are untracked in `archive/`.
57. **CONFIRMED.** The close line is at RESULTS.md:82–86 (`0516832`), with `ans5:`'s path and sha256. It is A5's first step.
58. **CONFIRMED.** The referent-check paragraph (E:11–16): the "what changed from v0.4" quote (v0.5:90), the brief, the HEADs, `fc43249`'s identity and the tally. Optional: the link text omits that the raw also holds "Outside the delta".
59. **CONFIRMED.** The 3.18 paragraph's facts: the four sources, and that canonical `ganl` and `gshape` refuse uncommitted sources (m_analyze.py:11092–11096, gshape.py:257). Its conclusion is graded at item 14.
60. **IMPRECISE.** "some within-line changes are not listed" (E:24): the report says "many" (R:53). **Fix:** "many".
61. **CONFIRMED.** The other three non-substantive items, "all five … dated notes", and "committed as delivered", for which RESULTS.md:996–997 is the precedent for non-substantive items.
62. **CONFIRMED.** The dated correction's counts (as in item 45).
63. **CONFIRMED.** The relay: RESULTS.md:27 for the 2026-11-09 (evening) section A, and RESULTS.md:158 for C and A of 2026-11-10. The 11-10 header is attested only by its fragment "the PI commits by path" (RESULTS.md:85). Quoting sections rather than whole blocks follows precedent (RESULTS.md:28, :1014–1029).
64. **CONFIRMED.** The 2026-11-09 (evening) A1–A4 (E:35–38) are byte-equal to RESULTS.md:30–33.
65. **CONFIRMED.** The description at E:40–41: C2's last sentence binds the re-issue, and A1–A5 are at `0516832`.
66. **NOT CHECKABLE.** The 2026-11-10 header line (E:43) is in no committed text. Only an identically worded 2026-11-09 (evening) header exists, at RESULTS.md:442.
67. **CONFIRMED.** C2 (E:45) is byte-equal to RESULTS.md:155 (`fc43249`).
68. **CONFIRMED.** A1–A5 (E:47–51) are byte-equal to RESULTS.md:100–104 (`0516832`).
69. **CONFIRMED.** "Next" (E:53–55) matches `ans5:`46 and :41.
70. **NOT CHECKABLE.** `@@VC@@` is a placeholder.
71. **NOT CHECKABLE.** "Committed by path … Nothing ran on a model. Not pushed." (E:57–58) describes a commit not yet made.

### The four points the brief flagged

- **3.18's four sources and two executability citations:** all accurate (items 34–39). Two optional refinements: the ganl refusal itself is at :11092–11096, and `ans5:` §7 names the re-runs only as "§4.3's chain".
- **Rules or precedents with no committed source:** none is stated outright. "Resolved in the record" rests on an uncited precedence (item 14). "The routing governs" has a committed basis (item 48). Committing as delivered with dated notes has precedent only for non-substantive items.
- **Claims about what Code did that the sources do not show:**
  - the own diff and its "independently" (item 27);
  - "each re-checked at source" (item 19);
  - "recomputed against the routing's list" (item 55);
  - BUILD-entry contents stated in the present tense (item 51);
  - the scan's reach is overstated (items 22–23).

### Everything not CONFIRMED

- **IMPRECISE:** 14, 22, 23, 28, 47, 60.
- **NOT CHECKABLE:** 16, 19, 24, 27, 51, 53, 55, 66, 70, 71.

### Compliance

- I opened, listed, sized or traversed nothing under `data/`.
- All 5 `git grep` calls carried `':!data/**'`. The `git show --name-status` calls carried `-- . ':!data/**'`.
- No `--stat`, `--numstat` or `--shortstat`. No git writes, no file written, no model run.
- Python was stdlib only, run as `python3 -I`, importing no repository code.
- The transcript was read only through the scanner, run twice.
- **One possible departure:** one pathspec-limited `git status --porcelain -- <five root/archive addenda>`. Item 1 names the bare form. It printed four `??` lines for those addenda; nothing under `data/` was named or printed.
- **Disclosure:** I substring-tested Code's scratch files `brief_referent_v05.md`, `lor_v2_items_1_5.md` and `brief_vc_v05.md` (not among the listed sources) to check item 8. Nothing from them was printed.
- A `cat -A` call failed on BSD `cat` and printed only a usage message.
