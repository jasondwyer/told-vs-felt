# ADDENDUM-m2 v0.3 — the referent check of the delta (A-m2 v0.3 §6 item 1)

*Code's raw, PI date 2026-11-09.*
- *What was checked:* A-m2 v0.3's delta from v0.2 (`ADDENDUM-m2-f3-reasoning-block-v0_3.md`, sha256 `83093812…fa67`, untracked at root until its commit). The check was against the seat's answer on #50 ("ans3": `results/raw/2026-11-08_open50-entry9_design-to-code_answers.md`, sha256 `d6296d44…2b97`, §1 and §3 item 1) and against Code's OPEN #50 block (`2018ffc`).
- *How:* a blind agent. HEAD was `2018ffc` before and after it ran, by Code's `git log`; the report itself does not state HEAD.
- *This raw:* the agent's report verbatim (one local path scrubbed to `<repo>/`), then Code's disposition of every item not CONFIRMED.
- *Nothing ran on a model, and nothing under `data/mf3/ckpt/` was opened.*

## The agent's report (verbatim)

## Blind referent check: ADDENDUM-m2 v0.3's delta against ans3 and Code's OPEN #50 block

**Tally (8 items):** 6 CONFIRMED (items 1, 2, 4, 5, 6, 7), 2 IMPRECISE (items 3, 8), 0 OPEN, 0 FAIL. There are three IMPRECISE findings (3a, 8a, 8b), and each is wording or anchoring only. No item is OPEN or FAIL, so nothing found here triggers §6 item 1's STOP ("any unresolved substantive item → STOP").

**Key** (all under <repo>/):
- v0.3 = ADDENDUM-m2-f3-reasoning-block-v0_3.md
- v0.2 = ADDENDUM-m2-f3-reasoning-block-v0_2.md
- ans3 = results/raw/2026-11-08_open50-entry9_design-to-code_answers.md
- block = results/raw/2026-11-08_a-m2-v02_code-to-design_open50.md
- pre = results/raw/2026-11-08_a-m2_code-to-design_preread.md
- ganl = results/raw/2026-11-06_ganl-f3_design-to-code_answers.md (added at `54bbfe5`)
- lock = LOCK-m-F3.md
- m:N = PROPOSAL-m-gating-campaign-v1_11.md, line N

**What I did not do:** no git writes, no files written, the scratchpad untouched, nothing under data/mf3/ckpt/ opened (every `git show` excluded that path), and the only Python was stdlib-only, run with -I.

---

### 1. Hashes: CONFIRMED
- v0.3 is `83093812…fa67`, v0.2 is `69e23212…cb47` and ans3 is `d6296d44…2b97`. All three equal the expected values in full, and all three files are untracked.
- The block (`794112…82a6`) is byte-identical to its blob at `2018ffc`.

### 2. Full diff: CONFIRMED
`diff` shows 8 changed lines, each replaced one for one: 3, 5, 7, 46, 48, 56, 71 and 72.
- :3 is the header.
- :5 is the anchors paragraph. It only adds `(de729c4)` after ans2's path and adds the `ans3:` anchor.
- :7 adds "**What changed from v0.2:** …" in front. The v0.1 list that follows is byte-identical.
- :46 is #49, :48 is #50 and :56 is #48.
- :71–72 are §6 items 1–2.

No change falls outside the allowed set. The header also drops v0.2's path for the pre-read (`results/raw/2026-11-08_a-m2_code-to-design_preread.md`). This is harmless: `da1e1b8` adds only that one pre-read.

### 3. Item (a), §3.4's blinding scope (#50): IMPRECISE (same in substance)

**3a. The sentence: IMPRECISE.** A word-level diff shows Code's sentence (block:46) reproduced word for word in v0.3:48, from "before the unit's VERDICTS entry or NOT-RUN record, a gate stage's entry reports (a) over its sham sessions' reasoning lines…" through "is computed and reported at the unit's VERDICTS entry or NOT-RUN record". ans3:7 adopts it as "Code's §4 sentence, verbatim in substance". The differences:
- **Over which lines.** v0.3 adds "the rest — each contrast session's later reasoning lines and free-round (b), and the campaign's counters —". This is word for word from block:44, not from the one-sentence form.
  - Read as an exhaustive list, it leaves out contrast first lines at a stage that does not report their class. That is the G-TIME-F3 re-run: under ganl:29 (F-6), "no per-line list is printed or reported before VERDICTS".
  - Code's plain "the rest" covered those lines by complement.
  - They are still covered at VERDICTS by "both counters tabulated over all sessions" and "Code tabulates (a), (b) … over the same records" (v0.3:48).
- **Who confirms.** v0.3 adds "where the seat confirms or corrects each (b) item". This matches block:44; ans3:7 says only "confirms".
- **Which sessions.** v0.3 adds "The smoke is outside this scope (sham-only, of no unit, readable in full, §3.2)". This matches block:34 and ans3:7.
- **Who and when, against ans3.** ans3:7 restates the clause as "the rest is computed and reported at VERDICTS by Code's own step". v0.3 follows Code's "at the unit's VERDICTS entry or NOT-RUN record" instead, and names no agent.
  - Code's own step is named only for VERDICTS, by the next sentence ("At VERDICTS the analyzer is untouched: Code tabulates…").
  - For a NOT-RUN record, v0.3 names no agent and no path. block:44 had "by Code's own step" for both cases.
  - This is minor, because m:271 itself releases the withheld events at the NOT-RUN record.
- **What was struck.** v0.3 also deletes v0.2:48's "reported at each stage's entry and at VERDICTS". That is the clause block:25 named as the conflict. v0.3:7 calls the change only "gains", which understates it. Nothing is lost: reporting at VERDICTS is kept by the unchanged VERDICTS sentence.
- **Placement.** The citations move to a bold lead-in.
- ans3:7's "G-ID-F3 … is unaffected" is not written into v0.3, but the scope gives the same result because G-ID-F3 is all-sham.

**3b. The cited set: CONFIRMED.** v0.3:48 cites "(m:271, m:263, m:318; F-6; F60)" and block:46 cites "(m:271, m:263, m:318, F-6, F60)". The five are the same, in the same order; only the separators differ. Each holds at its source:
- m:271: "are withheld to the unit's VERDICTS entry or NOT-RUN record".
- m:263: "the phase alone (`excluded@free`), the class withheld to VERDICTS".
- m:318: "at looks, pooled pre-pick exclusion counts per arm".
- F-6 at ganl:29, which also says "Sham sessions keep their per-line booleans in the report (nothing of theirs is withheld)". This supports the scope's sham half.
- F60 at lock:505: "first reasoning lines (pre-pick) beside its forced rounds, by class".

**3c. Leftover "at each stage's entry": CONFIRMED.** "each stage" appears nowhere in v0.3. "stage's entry" occurs only inside the new scope (v0.3:48).

### 4. Item (b), the stopped-smoke clause in §3.3 (#49): CONFIRMED
- v0.3:46: "selects nothing: the driver prints no tally and no rule, Code reports the stop, and the seat rules, as at any STOP."
- This matches ans3:10 ("selects nothing; no tally, no rule; Code reports, the seat rules") and block:51.
- The four causes v0.3 lists are block:51's four, and they are P4's stops: backend (pre:173), snapshot (pre:166, :168), G-VER (pre:181) and `scaffold_absorption` (pre:183).
- P4's other refusals all fire before any session runs, so they select nothing anyway. A reasoning-line fire is correctly not a stop (pre:184: "the smoke goes on").

### 5. Item (c), the pin clause in §4.2 (#48): CONFIRMED
- v0.3:56: "it pins the committed A-m2's sha256 — this version's — and parses §3.1's four literals from it".
- ans3:9 says the same with "— v0.3's —".
- block:50's rule ("the committed A-m2's sha") is kept. Only the instance moves from v0.2 to v0.3, per ans3:7 ("The smoke driver pins v0.3's sha").
- "Four literals" comes from pre:164 and ans2:18.
- Parse note for the driver: §3.1's lead-in (v0.3:37) also carries m:174's literal, which has the same bytes as F-0. The four literals are the bullets at v0.3:38–41.

### 6. Anchors and header: CONFIRMED
- **Commits.**
  - `de729c4` adds ans2 (`09d856ef…ea29`).
  - `2018ffc` adds the block, the v0.2 referent check (#50 is OPEN at its :210) and the RESULTS entry.
  - `da1e1b8` adds the pre-read and its referent check.
  - `dc1ffe1` adds the seat's F3 prebuild answers; §8 starts at :48 and Q8's words are at :51.
  - `acc3b52` adds gt, results/raw/2026-11-07_mf3-gtime-f3.txt (v0.3's `_mf3-gtime-f3.txt` is shorthand for it) and data/mf3/reports/Q-F3_time_reads.json.
  - `f26bc59` is "ADDENDUM-m1 v0.1 COMMITTED".
  - `1e79955` is LOCK-m-F3 v0.1.
- **Sha fragments.** All four match: v0.2 `69e23212…cb47`, v0.1 `cdcc8e86…53f0`, LOCK-m-F3.md at `1e79955` `377c5d60…6ce7` (unchanged at HEAD), and PROPOSAL-m v1.11 `42ab36ec…6c6b`.
- **ans3's path** is right.
- **Header claim.** "neither is committed" holds: `git log --all` shows no commit touching any A-m2 version, and nothing is in archive/.
- **Note:** the header records v0.1's STOP but not ans3:7's ruling that "v0.2 §6 item 1's STOP fires on #50". This is an omission, not an error.

### 7. §6 items 1–2: CONFIRMED
- v0.3:71: "the referent check of the delta (the "what changed from v0.2" items) against ans3". This matches ans3:7: "its referent check covers the delta only (three items)".
- v0.3:72 has the driver commit "after this file". This matches ans3:7 ("The smoke driver pins v0.3's sha") and the order in ans3:18: "commit (§6 item 2) [go]; … then the smoke driver's commit and the smoke's laptop go".
- "v0.1 and v0.2 to `archive/` uncommitted" agrees with ans3:3 and the header. `daca8b0` does hold the dated correction.

### 8. Self-consistency: IMPRECISE (no contradiction found)
- **8a. IMPRECISE.** §7 was not updated. v0.3:78 lists only "§9 PINs F25, F28, F29", not F-6 (lock:436, :513–515; ganl:29) or F60 (lock:505), which v0.3:48 now cites. §7 already lists other referents the text cites without quoting (the keys.py lines), so by its own practice these belong there. The anchors paragraph also gives no anchor for ganl.
- **8b. IMPRECISE (minor).** §5 item 2 (v0.3:65), "§3.4's counters with their VERDICTS path [adopted]", omits the scope, #48 and #49, which ans3:18 routes as "[confirmed]". This does not conflict: §5 says the routing block is the record.
- **No conflicts:**
  - The remaining "v0.2" at v0.3:58 and :74 is LOCK-m-F3 v0.2, not A-m2.
  - §3.2's "a gate stage's sham reads stay redacted as m:271 has them" (v0.3:44) is a read rule, and F-6 keeps sham booleans in the report.
  - §4.3's release "at VERDICTS by Code's own step" (v0.3:58) agrees with the scope.
  - §6 item 3's "the rule's choice stated" (v0.3:73) assumes a completed smoke; the new §3.3 sentence governs a stopped one.
  - The Q4 review counter is reported at VERDICTS only (prebuild answers §4), so leaving it out of the scope opens no gap.

### Outside the delta (no verdict)
- `daca8b0`'s commit message gives v0.1 as "cdcc8e86...f3f0". Its RESULTS text and v0.3 both have the correct `…53f0`.
- v0.3 takes up none of the v0.2 check's 12 IMPRECISE notes. For example, :7 still says "§4.3 names … the counters' VERDICTS path", though that path is in §3.4. This is consistent with ans3's "delta only".

## Code's dispositions

Code re-checked each item not CONFIRMED at source. None moves any of these:
- a form's bytes, a bar, a key, a cell or the rule;
- a figure the rule reads;
- what a stage entry prints before VERDICTS.

So v0.3 is committed as delivered, as PROPOSAL-p's v0.2 was (`18b0111`) and as A-m2 v0.2's dispositions had it (`2018ffc`). The items go to the seat as dated notes.

- **3a (IMPRECISE: §3.4's sentence, v0.3:48 against ans3:7).** Confirmed at source.
  - **The list after "the rest" is a description, not exhaustive.** It is the block's §4 wording (:44). Some lines fall in neither the stage scope nor that list: a contrast session's first lines at a stage that does not report their class. That stage is the G-TIME-F3 re-run, under F-6 (the G-ANL-F3 answers, `54bbfe5`, line 29; LOCK-m-F3 :436, :513–515).
    - Code's reading: "the rest" is the complement of the stage scope.
    - §3.4 tabulates those lines at VERDICTS, by "both counters tabulated over all sessions, excluded ones included" and by its VERDICTS sentence ("Code tabulates (a), (b) … over the same records").
    - What a stage entry prints before VERDICTS is fixed by the scope's first half, which matches ans3's sentence word for word. The re-run's entry reports no contrast-line counter, and F-6 stands.
  - **ans3 and v0.3 word the second half differently.**
    - ans3: "at VERDICTS by Code's own step, where the seat confirms each (b) item".
    - v0.3, in the block's wording: "at the unit's VERDICTS entry or NOT-RUN record, where the seat confirms or corrects each (b) item".
    - Code's reading: at a NOT-RUN record, the same Code step computes them as at VERDICTS. m:271 releases the withheld events there.
  - **The "what changed" list understates the change.** It says §3.4 "gains" the scope, but the delta also strikes v0.2's "reported at each stage's entry and at VERDICTS". Nothing is lost: reporting at VERDICTS is kept by the unchanged VERDICTS sentence.
  - **ans3's "G-ID-F3 … is unaffected" is not in v0.3's text.** The scope gives the same result, because G-ID-F3 is all-sham.
- **8a (IMPRECISE: §7, v0.3:78).** Confirmed at source.
  - §7 lists LOCK-m-F3's §9 PINs F25, F28 and F29, but not F-6 (LOCK-m-F3 :436, :513–515) or F60 (:505), which §3.4 now cites.
  - The anchors paragraph gives no anchor for the G-ANL-F3 answers (`54bbfe5`).
  - Code verified both referents at source before this commit; the agent's item 3b quotes them.
- **8b (IMPRECISE: §5 item 2, v0.3:65).** Confirmed at source. It names "§3.4's counters with their VERDICTS path [adopted]", not the scope, #48 or #49. §5 says the routing block is the record, and the routing quoted in the commit entry carries them.
- **Notes without a verdict** (items 2 and 6, and outside the delta). Nothing to apply.
  - The header drops v0.2's path for the pre-read.
  - The header does not record that v0.2's STOP fired (ans3 §1).
  - `daca8b0`'s commit message gives v0.1's tail as `f3f0`; its RESULTS text and v0.3 have `53f0`.
  - v0.3 takes up none of the IMPRECISE notes from v0.2's check, as ans3's "delta only" has it.
- **§3.1's parse (item 5's note).** The driver reads the four bullets (v0.3:38–41) by its bullet pattern. §3.1's lead-in (v0.3:37), which carries m:174's literal, is not a bullet and is not read. The driver's self-test checks that the parse gives exactly the four forms.
