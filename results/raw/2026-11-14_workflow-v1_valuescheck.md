# WORKFLOW.md v1.0 — COMMITTED: the entry's values-check

*Code's raw (the coordinating session), PI date 2026-11-14.*
- *What was checked:* the draft of the coordinating session's RESULTS.md entry `WORKFLOW.md v1.0 — COMMITTED` (§D
  item 11 of the seat's answers of 2026-11-14), before its commit.
- *Against:*
  - `WORKFLOW.md` (sha256 `e7195706…b061`, 11,492 bytes, untracked at the check);
  - the seat's raw `results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md` (sha256 `6b963adf…db3a`,
    32,250 bytes), committed by the F3 session at `cdccc66` while the check ran;
  - `CLAUDE.md`, G-F3's raw `results/raw/2026-11-12_mf3-gf3.txt`, the dpo draft and the block committed at `012ffbe`;
  - git and RESULTS.md.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 byte for byte (lines
  18–22 of `results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md`). Its report follows verbatim; the
  disclosures in its last section are its own, under the list's item 8.
- *Result:* 45 claims: 35 CONFIRMED, 2 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE.

## The report, verbatim

**Blind values-check: the DRAFT entry "WORKFLOW.md v1.0 — COMMITTED" (PI date 2026-11-14)**

**Result: 45 claims. 35 CONFIRMED, 2 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE.** Every hash, byte count and quote checks out. Both IMPRECISE items are wording: one is in the "Next" bullet, the other is the slip's disposition.

HEAD moved during the check, from `012ffbe` to `cdccc66`. That commit is the F3 session's close line on G-F3's entry: it adds the seat's raw, byte-identical to the placed file, plus `results/raw/2026-11-14_gf3-close_valuescheck.md`. So `@@F3@@` resolves to `cdccc66` (not graded). At my last check RESULTS.md was clean against HEAD and WORKFLOW.md was still untracked.

Paths are relative to the repository root named in the brief. Labels used below:
- **W** = `WORKFLOW.md`
- **R** = `results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md`
- **K** = `results/raw/2026-11-14_p-lock-v1.0_code-to-design_read.md` (the block, committed at `012ffbe`)
- **D** = `results/raw/2026-11-14_p-lock-v1.0-draft_OLMo-dpo.md`
- **G** = `results/raw/2026-11-12_mf3-gf3.txt` (committed at `2193832`)
- **C** = `CLAUDE.md`
- **RS** = `RESULTS.md`; line numbers are at HEAD `cdccc66`

| # | claim | source (path:line) | status | note |
|---|---|---|---|---|
| 1 | Entry head `- 2026-11-14 — **WORKFLOW.md v1.0 — COMMITTED**` | R:104, R:81, W:3; RS:24 | CONFIRMED | The title is the one R and W name. The head's form matches RS:24, 75, 106, 138. |
| 2 | "(the coordinating session; … §C and §D item 11" | R:77, R:103–104 | CONFIRMED | Item 11 sits under "C. Coordinating session". |
| 3 | "routed by the PI as given" | chat | NOT CHECKABLE | Consistent with the F3 session's committed relay at RS:651–652. |
| 4 | W's sha256 `e7195706…b061`, in full | W (shasum) | CONFIRMED | All 64 hex characters equal; same again at the last check. |
| 5 | 11,492 bytes | W (wc -c) | CONFIRMED | 11492 |
| 6 | v1.0 at root | W:1 | CONFIRMED | |
| 7 | "The design seat placed it untracked" | W:3, R:81; `git status` shows `?? WORKFLOW.md` | CONFIRMED | Untracked at every check. |
| 8 | "I re-hashed it just before this commit, equal to the sha256 and bytes the PI's paste block names" | chat; a future act | NOT CHECKABLE | The file's values equal the paste-block values the brief reports. The re-hash at commit time has not happened yet. |
| 9 | "commit it by path as placed, unedited" | a future act | NOT CHECKABLE | |
| 10 | Nine sections | W:5, 13, 21, 32, 39, 47, 51, 55, 59 | CONFIRMED | §1–§9 |
| 11 | The one-line summary of the sections | W:5–61; R:81 | CONFIRMED | Its third item covers both §3 and §4, so eight items describe nine sections. "Fixed forms" is R:81's wording; W's headings say "fixed form" (§3) and "form" (§4). "Dated notes" matches W:43. |
| 12 | Design → PI → Code is one paste block per sitting; Code → design is repo state only | W:15, W:17 | CONFIRMED | |
| 13 | Header quote "It changes no rule … it governs." | W:3 | CONFIRMED | Verbatim. |
| 14 | R's sha256 `6b963adf…db3a`, in full | R (shasum) | CONFIRMED | 32,250 bytes, equal to the brief's paste-block figure. Same blob at HEAD as in the working tree. |
| 15 | R "committed by the F3 session" | R:89–91 (§D item 2) | CONFIRMED | Done at `cdccc66`, which adds R as placed. The placeholder itself is not graded. |
| 16 | §D item 11 quote | R:104 | CONFIRMED | Verbatim; the draft's line wrap counts as one space. |
| 17 | The PI's "Route as given", replying to "Route the seat's answers as given?" | chat | NOT CHECKABLE | The same question and answer appear at RS:651–652 (F3's relay). |
| 18 | §C's quote of the PI's words | R:79 | CONFIRMED | Verbatim. |
| 19 | The close is the coordinating session's line, per §D item 11, recording ledger (68) | R:3, R:104 | CONFIRMED | Item 11 names no target entry, so recording the close in this entry is a form choice, not a ruling. The precedent close is RS:1070 (committed at `cff77a8`). |
| 20 | §C's convention sentence | R:79 | CONFIRMED | The words are identical; the source bolds the clause after the colon. Dropping the bold is acceptable: the record's committed criterion counts a quote as verbatim "bold markers and whitespace aside" (RS:8696), and F3's close writes "verbatim (bold markers aside)" (RS:636). |
| 21 | Where the record said otherwise: the seat's raws of 2026-11-09 through 2026-11-12, the handoff of 2026-11-12, and `pq:` §4.3 item 3 carried into the drafts and the block at `012ffbe` | R:79; R:3 (defines `pq:`) | CONFIRMED | A faithful paraphrase; leaving out what each one said is fine. The phrase appears once in K and twice in each of the three drafts. That fits the two sites (A1) and (A2) name at R:57–58; I did not open those sites. |
| 22 | "before the PI commits it" | R:79 | CONFIRMED | Verbatim. |
| 23 | "The committed raws are not edited" | R:79 | CONFIRMED | Verbatim. |
| 24 | The correction is §C's line, amendment (A2) and WORKFLOW.md | R:79 | CONFIRMED | The source reads "this line, the drafts' amendment (A2), and `WORKFLOW.md`". |
| 25 | §C's CLAUDE.md sentence | R:81 | CONFIRMED | Verbatim. |
| 26 | C's sha256 begins `955788dec22ee820` | C (shasum) | CONFIRMED | Full value `955788dec22ee820917693bf…8a62`. The blob is the same at HEAD (`012ffbe` and `cdccc66`) as in the working tree (`64f2ad75…`); C is unmodified. |
| 27 | That is the value G-F3's GATE line prints | G:10 | CONFIRMED | The line reads `GATE G-F3: … CLAUDE.md 955788dec22ee820 …`; G has one GATE line. |
| 28 | "re-hashed both placed files, read both in full" | the drafter's session | NOT CHECKABLE | Both files' values are equal now. |
| 29 | Both files scanned for clock times, `$`, IPs, local paths and emails: none | W, R (regex scans) | CONFIRMED | 0 matches in each file; no URL or time-zone word either. |
| 30 | "matched the paste block to the raw's §D item by item" | chat | NOT CHECKABLE | |
| 31 | R's header gives the dpo hash as `f2a6960f…a28d` | R:3 | CONFIRMED | |
| 32 | The dpo file's hash ends `a28b` | D (shasum) | CONFIRMED | Full value `f2a6960f…5747a28b`. The blob at `012ffbe` equals the working tree's. |
| 33 | `012ffbe`'s block gives the full value ending `a28b` | K:40 | CONFIRMED | K has no `a28d` anywhere. |
| 34 | "One slip" | R:3 against the files | CONFIRMED (within bounds) | sft `968c4abd…d427` and instruct `6da557e5…7fad` match their files and K:39 and K:41. `pq:` `a32d4d17…1112` matches `results/raw/2026-11-12_p-qual_design-to-code_answers.md`. The reads file's `2881b7d9…6730` is under `data/` and was not checked, per the brief. |
| 35 | "I put it to the PI before the routing" | chat | NOT CHECKABLE | |
| 36 | "it goes to the pod session's close line on `012ffbe` as an observation, and the raw stays as placed" | R:100 (item 9) | IMPRECISE | It does not say whose disposition this is. See fix (a). |
| 37 | Next: the pod session's close lines on `012ffbe` and `c0f1c69` (item 9) | R:96, R:100 | CONFIRMED | |
| 38 | Next: "LOCK-p v1.0 ×3 placed and committed by path" (item 6) | R:97; R:75 | IMPRECISE | It leaves out the amendments and the condition on the commit. See fix (b). |
| 39 | Next: G-PWR (Q-F3), with the PI's cap at its entry (items 3–4) | R:92–93 | CONFIRMED | Item 4 also offers declining v1.0 (NOT-RUN by D2). Item 5 (drafting LOCK-m-F3 v1.0 after the cap) is not listed; it doesn't need to be. |
| 40 | Next: the replacement pod on the PI's go (item 10) | R:101; R:75 | CONFIRMED | R:75 itself says "on the PI's go". Item 10's bracket, routed as given, reads "[go when v1.0 ×3 are committed; the timing yours]". |
| 41 | Next: the push on the PI's word (item 13) | R:108 | CONFIRMED | Item 13 also names the pre-push screen (list v2 item 4). |
| 42 | "WORKFLOW.md and RESULTS.md only. Nothing ran on a model or the box. Not pushed. Committed by path." | a future act | NOT CHECKABLE | See the observations below. |
| 43 | Every link resolves | `ls` of W, R and G | CONFIRMED | All three exist. R is tracked from `cdccc66` on, so its link resolves in the committed tree; W joins the tree with this commit. |
| 44 | No forbidden forms in the draft | brief lines 24–63 (regex scan) | CONFIRMED | The only `@` is in the `@@F3@@` placeholder. The draft carries calendar dates only. |
| 45 | No "the PI commits" slip, and nothing adjudicated elsewhere | the draft (scan and read) | CONFIRMED | "PI commit…" appears only inside the two quotes. Every commit the draft names is Code's. Row 36 is the one ambiguity. |

**IMPRECISE items, with suggested fixes**

(a) Row 36. As written, a reader could take it that Code, or the PI, disposed of an error in the seat's text. What actually happens is that Code routes an observation, which decides nothing, and the raw stands because the PI routed it as given. Suggested: "I put it to the PI before the routing. His word was "Route as given", so the raw went in as placed (the F3 session's commit `@@F3@@`, at the paste block's sha256). I hand the slip to the pod session as an observation for its close line on `012ffbe` (item 9); it decides nothing."

(b) Row 38. Item 6 is conditional. First come amendments (A1)–(A3); then the generator and the dry precheck re-run; then an entry printing each diff and new sha256. A second STOP is owed only if the diff is more than (A1)–(A3), and only after that are the files placed byte for byte and committed. As written, the bullet reads as if the `012ffbe` drafts go in as they stand. A suggested Next bullet, which also takes in the optional points from rows 39–41:
"**Next** (the raw's §D): the pod session's close lines on `012ffbe` and `c0f1c69` (item 9); LOCK-p v1.0 ×3 amended by (A1)–(A3), with the generator and dry precheck re-run and each diff and new sha256 in its entry, a second STOP only if the diff is more than (A1)–(A3), then placed byte for byte and committed by path (item 6); G-PWR (Q-F3), with the PI's call at its entry, a cap or declining v1.0 (items 3–4); the replacement pod once v1.0 ×3 are committed, at the PI's timing (item 10); the push on the PI's word, after the pre-push screen (item 13)."

**Optional wording changes (not graded)**
- Row 20: add "(bold markers aside)" after the convention quote, as RS:636 does.
- Row 19: head the close "**Close (PI date 2026-11-14; the coordinating session's line, per §D item 11): ledger (68).**", matching RS:1070.
- Row 8: "the PI's paste block" could read as the PI's own text. Per W:15 it is the seat's block, which the PI pastes, so "the paste block" is enough.

**Observations for the commit (not claims of the draft)**
- **Commit order.** Insert the entry against `cdccc66` (or whatever HEAD is current), then check that the commit's RESULTS.md diff is this entry alone. Then "WORKFLOW.md and RESULTS.md only" holds by content, not just by path.
  - Before `cdccc66` landed, the working-tree RESULTS.md held F3's uncommitted close. Committing RESULTS.md by path at that point would have swept it in.
  - F3's committed close (RS:632 onward) cites `WORKFLOW.md` §1, which this commit adds.
- **Values-check raw.** W:37 has a close line "committed by path with a values-check, as the record practises", and F3's `cdccc66` committed its values-check raw. The coordinating session's own precedents (`15d2f70`, `cff77a8`, `03a08ca`) each committed RESULTS.md only. If this check goes in as a raw, the draft's "WORKFLOW.md and RESULTS.md only" line changes with it.

**Departures and disclosures (list v2 item 8)**

What I did not do:
- Nothing under `data/` was touched. R:3 names `data/mf3/reports/Q-F3_qual_reads.json`; I read that only as R's text and did not check its abbreviated hash.
- No whole-tree listing, `find`, recursive search, pickaxe, Python, edit, write, commit or push. There were no temp files: grep patterns went through process substitution.
- Every RESULTS.md search was fixed-string (`-F`).

What I ran beyond the named sources, by kind and what it printed:
1. **sha256 of three files the brief does not name**, read by exact path: the sft and instruct drafts, and the `pq:` raw (its path taken from RS:1071). Printed each digest and path.
2. **Fixed-string counts of "before the PI commits it"** in the sft and instruct drafts, alongside the named dpo draft and K. Printed counts only.
3. **Blob ids** for C, D, R and RS, each at a commit (`git rev-parse`) and in the working tree (`git hash-object`). Printed hex ids only.
4. **`git show HEAD:RESULTS.md | grep -cF`**: eight fixed-string counts, taken at HEAD `012ffbe` and then at `cdccc66`. Printed counts only.
   - This is a git content form on RESULTS.md alone, not a names-only form. I disclose it as beyond the brief's "names-only git forms" summary.
5. **`git status --porcelain` and `git ls-files`, both limited by pathspec to the named paths.** Printed the status lines and the tracked names. Limiting by pathspec is narrower than the bare form item 1 permits.
6. **A name-only `ls`** of the three link targets.
7. **`git log --format`, ids and subjects only, no times.** Commands:
   - `-n 3 --format='%h %s' -- RESULTS.md`
   - `-n 3 --format='%h %s'` over the whole history
   - `-n 1 --format='%h'` for four files

   Subjects were cut to 160–200 characters.
8. **`git show --name-status`, names only**, for `cdccc66`, `15d2f70`, `cff77a8` and `03a08ca`.
9. **RESULTS.md fixed-string searches that printed text.**
   - Text printed:
     - RS:22
     - eight entry heads
     - 20 lines naming the coordinating session
     - eight `**Close` heads
     - eight `Dated note (` heads
     - the precedent close in full (lines 1067–1073 at the time)
     - two unrelated `a28d` hits (LOCK-m-F0's sha256)
     - the emphasis hits
   - The prints also included another session's then-uncommitted text: F3's pending close, at lines 633–636 and 650–651 as they stood then. It is now committed at `cdccc66`.
   - Other searches printed line numbers only.
10. **From named sources:**
    - G:10 printed in full, plus a count of GATE lines.
    - K:39–41's three full sha256 values.
    - Regex scans of W and R, which printed counts of 0.
    - A scan of the brief's draft, which printed the one `@@F3@@` line.
    - `wc -c` on W and R.
11. **Two commands exited 1.** In each, the final grep found no match, as expected.

## Dispositions (the coordinating session)

- **(a) Row 36, applied.** The slip's bullet now says the raw went in as placed on the PI's word "Route as given"
  (the F3 session's commit `cdccc66`, at the paste block's sha256), and that the slip goes to the pod session as an
  observation for its close line on `012ffbe` (item 9), deciding nothing. The entry says "the PI's word", not the
  suggestion's pronoun.
- **(b) Row 38, applied, with one addition after the check.** The "Next" bullet carries item 6 as conditional. It also
  carries the PI's word "Hold the locks" (PI date 2026-11-14), which the check did not see: the locks' placement and
  commit wait for the seat's answer to the pod session's finding on §B.4 item 7. A new bullet, "The hold", records
  that word and the finding. Both additions were checked by tool, not by this agent: the quote of §B.4 item 7 against
  the seat's raw, line 71, and the two code sites against `valence_core/p/stage.py` (lines 615 and 1352–1357, the file
  unchanged since `c0f1c69`).
- **Optional rows 8, 19 and 20, applied:** "the paste block"; the close's head in the form of the coordinating
  session's close committed at `cff77a8`; "(bold markers aside)" after the convention quote.
- **Observations:** the entry is inserted against HEAD `cdccc66`, and the commit's RESULTS.md diff is this entry
  alone (one hunk, no line removed). This raw is committed with it; the entry's last line names it.
