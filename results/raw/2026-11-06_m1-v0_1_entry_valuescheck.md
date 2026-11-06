# Values-check of the ADDENDUM-m1 v0.1 commit entry and its referent-check raw (pre-commit)

*Code's raw. The report in §1 is a blind values-checker's, run as a subagent of this session (2026-11-06 UTC) over
the entry's first draft and `results/raw/2026-11-06_m1-v0_1_referent-check.md`. It was given the sources, not Code's
conclusions. It is copied verbatim. Its line numbers refer to those drafts, which have since changed. §2 gives
Code's disposition of each item, applied before the commit.*

## 1. The checker's report (verbatim)

# Values-check: the ADDENDUM-m1 v0.1 commit entry and its referent-check raw

**Texts checked**

1. `RESULTS.md` (working tree), lines 24–135: the entry `- 2026-11-06 — **ADDENDUM-m1 v0.1 COMMITTED …`, ending just before `- 2026-10-19 — **PROPOSAL-m Q-F0 — VERDICTS`. The working-tree diff of RESULTS.md is this one 112-line insertion at line 24 and nothing else.
2. `results/raw/2026-11-06_m1-v0_1_referent-check.md` (209 lines).

Line numbers below are working-tree lines of these two files ("entry :N" means RESULTS.md:N, "raw :N" means the raw's line N). Anchors are cited as the texts define them: `m:N` is PROPOSAL-m v1.11, `RESULTS.md@18c32df:N` is the blob from `git show 18c32df:RESULTS.md`, and `m_analyze.py:N` is the blob at 18c32df.

**Method.** I recomputed every claim from its source. No repository file was edited.

- **Hashes and git:** `shasum -a 256`; `git show 18c32df:…`; `git log`, `git ls-files` and `git status --porcelain --untracked-files=all`; `git ls-remote origin refs/heads/main` (remote main is `18c32dff…a05c9`).
- **Anchors:** `sed -n` on m:N and on the 18c32df blobs.
- **Byte comparisons and JSON scans:** Python run with `-I`, from scripts in `scratchpad/vc_m1/`.
- **The Berg & Kaiser (BK) clone,** read as data only. I read its `.git/HEAD` and `.git/config`, ran read-only git plumbing (`rev-parse`, `log -1`, `status`), and read the CSVs with `cat` and `awk`. Nothing in it was executed.
- **The BK v2 PDF:** its PDFKit text (`bk_pdf/bk_v2.txt`) and its sha256.
- **The arXiv API** (`export.arxiv.org/api/query?id_list=2609.35591`) for the version dates.

## Claims checked: 196

There are 88 in the entry and 108 in the raw. A quotation and its anchor count as one claim, and a table row counts as one claim.

**Result: 5 FAIL, 6 IMPRECISE.** Observations that are not graded are listed after them.

---

## FAIL

### F1. Entry :87: "In fact no box entry exists after 2026-08-23"

Box entries dated 2026-08-24 and 2026-08-25 exist in `RESULTS.md@18c32df`:

- **:12717–12722**, 2026-08-24, *CACHED-GENERATION GATE, all four stages*: "Respawn gates re-passed on the restarted pod first." Its raws are listed at :12725–12726 (`2026-08-24_respawn_integrity.txt`, `_respawn_determinism.txt`).
- **:12553 and :12563–12565**, 2026-08-24, *B2 COMPLETE*: "Backend: pod `uimuzt7d890y5b` restarted 13:08 UTC, respawn (i) 29/29 + (ii) three zeros both PASS before any experimental forward."
- **:12795 and :12803–12804**, 2026-08-24, *B2 STIMULUS DISPOSITIONS*: "Pod `uimuzt7d890y5b` restarted 2026-08-24 06:58 UTC; respawn gates re-running."
- **:12489**, 2026-08-24, *B3 SCREEN COMPLETE, ALL FOUR STAGES*.
- **:12341 and :12411**, 2026-08-24: "Pod STOPPED (not terminated) at 16:41 UTC".
- **:11714 and :11797–11799**, 2026-08-25, *B2-r DISPOSITION*: "fifth clean manifest; fifth A100 with three zeros." and "Pod: STOPPED".
- **:11811 and :11826**, 2026-08-25, *B2-r COMPLETE*: "Pod `uimuzt7d890y5b`, uncached."

**The correct form:** the last box entries are of 2026-08-25, and none comes after them. The 2026-08-25 *Q2 CLOSED* entry says, at :11615–11616, "the pod is parked; the box is not needed by anything outstanding", and every later mention of a pod is "a pod start needs the PI's go". The point the sentence serves still stands: no OLMo m-unit artifact exists, and the box has not been used since August.

### F2. Raw :23–24: "No entry headline carries "BACKEND" at all."

`RESULTS.md@18c32df:17228–17231` is the 2026-08-19 headline that the raw cites on its next line. Its bold headline reads "**CUDA determinism + kernel-path characterization COMPLETE (rule 2). THE BACKEND OF RECORD. Measured residual nondeterminism is EXACTLY ZERO, …**".

The string `BACKEND` occurs twice in the blob: at :17229, in that headline, and at :14035, in a body line ("Step (ii) BACKEND — PASS").

**The correct form:** no entry is titled `BACKEND — characterization`.

### F3. Raw :24–25: "The latest box entries are from August: 2026-08-23, `RESPAWN PROTOCOL: BOTH GATES PASS on the new box`, and 2026-08-19, `CUDA determinism + kernel-path characterization COMPLETE`."

The two quoted headline fragments are verbatim, at :14019 and :17228. "Latest" is wrong.

- The evidence of F1 shows later box entries on 2026-08-24 and 2026-08-25, including two respawn runs on a restarted pod.
- A fifth respawn and backend characterization ran on 2026-08-25. `results/raw/2026-08-25_b2r_arc.txt` has "##### RESPAWN (i) INTEGRITY (02:48:22Z) #####" at :8 and "##### RESPAWN (ii) BACKEND CHARACTERIZATION (02:51:48Z) #####" at :41.

### F4. Raw :41: "**No pod start is on record:** no box raw or entry exists after 2026-08-23."

Ten tracked box raws are dated after 2026-08-23:

- `2026-08-24_{b2,b3,bphase_respawn,cached_gate,cached_gate_WITHDRAWN_v2,respawn_determinism,respawn_integrity}.txt`
- `2026-08-25_b2r_{analysis,arc,gates}.txt`

Line 1 of `results/raw/2026-08-24_bphase_respawn.txt` reads "### RESPAWN (i) INTEGRITY -- pod uimuzt7d890y5b restarted 13:08 UTC, B-phase arc ###". Pod starts are therefore on record on 2026-08-24, at 06:58 and 13:08 UTC, and on 2026-08-25, for the B2-r arc.

I also searched the raws dated 2026-08-26 onward for A100, H100, `/workspace/`, `RESPAWN (i)` and `cuda:0`. Those strings appear only where values-check and note-audit raws quote them.

**The correct, scoped form:** no box raw or entry exists after 2026-08-25, so no pod start is on record since then, and in particular none since 2026-10-19.

### F5. N8, in both texts: "`Q-F0_VERDICTS.json` … holds no date string"

The locations are raw :206–207 and entry :123–124.

`data/m/verdicts/Q-F0_VERDICTS.json` (sha256 `ec7d2082…35ea`, unchanged since `bfc179c`) holds date strings:

- Its key `olmo_states_declared` embeds each OLMo declaration whole: `{"clock_passed": false, "date": "2026-10-19", "state": "PENDING", "substate": "unlocked-before-D_O"}`, three times.
- `per_property_table.reference` contains "2026-10-10".

What the file does not hold is a Clock date: "2026-10-30" occurs nowhere in it.

**Suggested form:** "holds no Clock date: D_O's 2026-10-30 appears nowhere, and the embedded declarations carry only their comparison date, 2026-10-19." N8's conclusion still holds: renaming the substate or adding a Clock field would break the byte-for-byte regression.

---

## IMPRECISE

### I1. Raw :75–77: "Each checkpoint adds 26 gate sessions and a 130–200 s cold load", and the ✓ on §1.4 in the same item

The hours already include those 26 sessions.

- **What m:205 says.** The OLMo basis (19.5 s at instruct, 22.7 s at SFT and DPO) is "applied to the unit's total + 26 sessions per checkpoint (24 qualification + 2 timing)**, G-CAL-OLMo's 128 generations and the pod's idle time at gates not included". The basis also already "amortize[s] one model load over a whole b3 run". It over-counts the load at SFT and DPO and under-counts it at instruct.
- **The arithmetic** (my own computation):
  - (160 + 26) × 19.5 s = 1.01 h, tabulated as 1.0. Without the 26 sessions it would be 0.87 h, which rounds to 0.9.
  - (160 + 26) × 22.7 s = 1.17 h, tabulated as 1.2.
  - (224 + 26) × 22.7 s = 1.58 h, tabulated as 1.6.
  - The three-checkpoint sums are 3.35, 3.93 and 4.51 h, tabulated as 3.4/3.9/4.5.
- **What the raw does.** Its "adds" misreads m:205. Its ✓ on §1.4 then lets the addendum count the gate sessions twice, with no note:
  - **§1.4** (addendum :30): "per checkpoint ≈ 1.0–1.4 h of campaign generation at 160/192 launches …, plus G-CAL-OLMo's 128 generations, the 26 gate-stage sessions, the cold load …".
  - **§0.4** (addendum :16): "≈ 1.0–1.4 h of campaign generation per checkpoint … plus G-CAL-OLMo's 128 generations per checkpoint and the gate stages".
- **Effect.** The double count is 26 × 19.5–22.7 s ≈ 0.14–0.16 h per checkpoint, about 0.45 h for the three. The hours are also not purely "campaign generation". This is minor, since 12 h was routed, but it is a residue of N1's class and belongs beside N1.

### I2. The 52 raws as "the release block's"

This is in raw :32–33 ("they are the release block's") and in N7: raw :203–205 and entry :121–122 ("the release block's record is its 52 raws (2026-10-22 through 2026-11-05)").

The count is right: 52 tracked raws are dated 2026-10-22 through 2026-11-05, and every name contains "note". The attribution to the release block is not:

- The addendum scopes the release block, at §0.1 (addendum :10), as "N1 round 11, N12, N18, the tag …, the flip …, the Zenodo record … — the entries and raws of 2026-10-27 through 2026-11-05".
- The block's own opening document is `results/raw/2026-10-27_note-design-to-code_release-block.md` ("the release block, posting day").
- The one raw dated before it, `2026-10-22_note-N2vii-macar-v5.md`, names its own block: "Block: '2. DESIGN → CODE · 2026-10-21 · note-N2(vii): three confirmations against arXiv:2603.21396v5'".

By the addendum's scope, then, 51 of the 52 raws belong to the release block. Under the wider reading, in which the release block is the whole AUDIT-note-release block, the block has 130 note raws: 78 more, dated 2026-10-06 through 2026-10-12. "Its 52 raws" is inexact under either reading.

**Suggested form:** "52 note raws after 2026-10-19: one note-N2(vii) raw (2026-10-22) and 51 release-block raws (2026-10-27 through 2026-11-05)". The entry's :91, "Every raw after 2026-10-19 is a note-release raw", can stand, because N2 is an AUDIT-note-release item.

### I3. Entry :92: "The shared modules still refuse Q-F3 (`keys.py:66–67`, `resume.py:385`, `:1158`, `audit.py:87–90`)."

The lines and their contents are right:

- `keys.py:66–67` is the `raise NotImplementedError("Q-F3 keys are built at step 19 …")`.
- `resume.py:385` is `tpls = keys.templates(unit)  # ValueError unknown, NotImplementedError Q-F3`.
- `resume.py:1158` is the self-test case `"Q-F3": (lambda: qf0(unit="Q-F3"), NotImplementedError)`.
- `audit.py:87–90` are the deferral comments.

The label is not. m:54 defines "the shared modules" as "(CORR delivery, `corrupt_m`, the audit wrapper's task-round classes)". `keys.py` (streams and seeds) and `resume.py` (the resume identity) are Q-F0-subset modules, not shared modules in m:54's sense. Also, resume.py:385 passes on the refusal raised in keys.py; it does not map Q-F3 itself. The raw's own wording, at :34–38, is correct.

**Suggested form:** "The m package's step-4 modules still refuse Q-F3 (…)".

### I4. Entry :131: "Step 6, `POSTING v1`, after which Q-F3's VERDICTS session follows."

The addendum's §4 step 6 (addendum :61) reads "`POSTING v1` as m:358 step 18 has it, with §2.4's two declared texts values-checked; then the Q-F3 VERDICTS session on the PI's word". §2.3 (addendum :40) also has "in a later session on the PI's word". The entry drops the PI's-word condition.

**Suggested form:** "…after which Q-F3's VERDICTS session runs on the PI's word".

### I5. Entry :43 ("PROPOSAL-n's own §8 has its own entry") and :132 ("PROPOSAL-n §8 runs after this commit and gets its own entry")

`results/raw/2026-11-06_n-v0_1_code-to-design_STOP.md` is untracked and was written in this session. Its lines 3–6 read: "Written 2026-11-06 UTC (`date -u` at write: Fri Nov 6 01:29:38 UTC 2026) … Steps 1 and 2 ran. Step 3 did not, so v0.1 is not committed and stays untracked at root."

The file was last modified at 01:38:28 UTC, before this entry's stamp of 01:39:35 UTC, which is also RESULTS.md's mtime. So PROPOSAL-n §8 has already run through step 2 and stopped. Only its record remains to be committed; its step-1 HEAD line still holds the placeholder `{M1_COMMIT}`.

- "Runs after this commit" is inaccurate for steps 1 and 2.
- "Has its own entry" is in the present tense, for an entry not yet written.
- The routing says both files are "committed by path with this block". For PROPOSAL-n that does not happen, and the entry does not say that PROPOSAL-n stays untracked.

**Suggested form:** "PROPOSAL-n §8 stopped at step 2 (`results/raw/2026-11-06_n-v0_1_code-to-design_STOP.md`); v0.1 stays untracked, and its STOP gets its own entry."

### I6. Entry :34: "Step 2: every referent of §5 resolves"

§5 (addendum :67) ends with a class of referent that neither text mentions: "**Project memory / threads cited for the PI's decisions of 2026-10-28, 2026-10-29 and 2026-11-03** (§2.2): records in the PI's words, not design inputs".

- The raw's §2 ("the referents of §5", raw :44) covers PROPOSAL-m, RESULTS.md, the files and Berg & Kaiser only. A search finds no "memory" and no "thread" in either text.
- Code's memory directory holds no record of a 2026-10-28 or 2026-10-29 decision to write the preprint from scratch. The dated items in `note-release-v2-2026-10.md` are release-block items. The 2026-11-03 submissions thread is a chat record.

§4 step 2's own list (addendum :57) does not include this class, so step 2 is complete as the addendum scopes it. "Every referent of §5" claims more than that.

**Suggested form:** "every referent of §5 that §4 step 2 lists resolves; §2.2's project-memory and thread records are the PI's and were not checked".

---

## Observations (not graded)

- **The routing is verbatim against this session's saved copy.** After the `    > ` prefix is stripped, the entry's routing block is byte-identical to `scratchpad/entries/routing_2026-11-05.txt` (22 lines, sha256 `d9611b41…2a82`). The PI's chat message itself was not available to me.
- **The routing meets §3 and is internally consistent.** It answers all five of §3's items:
  1. The date is confirmed, (16) is adopted, D_O′ is 2026-11-30, the budget is 12 h with caps at G-PWR, the pod start is a go after the runpod MCP is re-authorised, and the base checkpoint is not reopened.
  2. (10′) is adopted and D2 stands at 2026-12-22.
  3. §2.4's two texts are accepted.
  4. The analyzer round at G-ANL-F3 is accepted.
  5. The pod order is the OLMo units first.

  "Pod start: [go, after runpod MCP re-auth]" is consistent with the standing "No pod start without my go." The PROPOSAL-n lines leave one choice open, "Negative pole: [as written / struck beyond d = −1 / struck]", with all three options and none chosen. The PROPOSAL-n STOP raw carries it as A1. The entry quotes it without comment, which is right for a verbatim record.
- **"N1" against "N-pod."** §1.3, §1.4 and §3 item 5 of the addendum call the pod work PROPOSAL-n's "N1". PROPOSAL-n §0.9 (4), at PROPOSAL-n:26, defines the unit as "N-pod (N1 + N2 + N4; §2.1–§2.5)". The routing and the entry use "N-pod". PROPOSAL-n is not in §5's list, so this is not a miss of the referent check.
- **US-CA-2's stock.** Addendum §1.3 says "US-CA-2 has listed no Ampere-80 stock before (RESULTS.md@18c32df:13048–13063)". That is one session's reading, dated 2026-08-23, and :13061–13063 caveat it as "*no stock listed right now*, **not** that the DC is gone". The pod restarted in US-CA-2 on 2026-08-24 (F1's evidence). The raw's ✓ on what the anchor says is correct.
- **The values-check raw is not on disk yet.** The entry's committed-by-path line names `results/raw/2026-11-06_m1-v0_1_entry_valuescheck.md`, which does not exist.
- **Stamps.** The entry's stamp of 01:39:35 UTC equals RESULTS.md's mtime, and the raw's 01:29:38 UTC precedes its mtime of 01:33:30 UTC. The m1 raw and the PROPOSAL-n STOP raw carry the identical stamp, 01:29:38. Where `date -u` prints two spaces before the day ("Nov  6"), the raw prints one.
- **Not verifiable.** The raw's statement that nothing in the BK clone was executed cannot be checked. The clone's working tree is clean against its HEAD.

---

## Verified correct

### The entry

- **The headline.** It names §4 step 3, says routed by the PI with PI date 2026-11-05, and carries the residues as dated notes under the routing's process line.
- **The addendum file.** Its sha256 `ea08322d…9001` and its 67 lines.
- **The summaries.** Those of (16), (10′), D2 and the analyzer round match §1.1, §1.3, §2.3 and §2.5. PROPOSAL-m v1.11 is unmodified, and m:356 is step 3.
- **Step 1:**
  - HEAD is `18c32dff190c530ce1b5679dc3e7277be90a05c9`, equal to origin/main both locally and on the remote.
  - Both routed sha256 values match.
  - There are 26 other untracked paths. The total is 30, less the two new raws and the two routed files. Every one has an mtime from 2026-08-22 through 2026-10-15.
  - No entry is titled `BACKEND — characterization`.
  - No entry is a G-CAL-OLMo, LOCK-m-OLMo, G-TIME-OLMo, G-F0m-OLMo or OLMo-campaign entry. The two G-CAL headlines that mention G-CAL-OLMo say it has not run.
  - `data/m` holds no OLMo checkpoint or report.
  - There are 18 OLMo schedule files, all added in `5f7b968` and untouched since.
- **The routing and the quotes.** The routing is complete against §3, and the record of the seven items follows §4 step 3. §0.1 and §0.2 are byte-identical to addendum lines 10 and 12.
- **Decision items 1–5,** including the cap share at G-PWR (m:302), the pod-start line (m:358), "(14) stands" and the base label of m:338.
- **The Berg & Kaiser figures.**
  - **The source:** commit `7631f8a`, remote `github.com/camberg23/act-on-valence`, licence CC BY 4.0.
  - **`figure4.csv`:** sha256 `c8f8dbe8…e638`.
  - **The values:** 0.036585 [0.015345, 0.057939] at base and 0.978440 [0.781640, 1.173429] at DPO, with N = 80. These round to §1.5's and §5's figures.
  - **The caption:** the fragment quoted from the Fig. 4 caption is verbatim.
  - **The arXiv dates:** the API gives v1 published 2026-09-28T16:43:34Z and v2 updated 2026-10-04T18:44:23Z.
- **The units' states** and the statements that nothing was drawn and nothing re-derived. `Q-F0_olmo-states.json` is unedited since `bfc179c`.
- **The m:318 record:** A0 PASS on 2026-10-19, :382–383, and §4 step 4.
- **Notes N1–N6,** N7's count and its first and third clauses, and N8's first clause.
- **What follows,** steps 4 and 5.

### The raw

- **Every `m:N` of §5,** 39 anchors, each matching its use. The verbatim ones are m:16 (10), (11) and (13); m:54; m:249; m:288; m:324; m:347 (both sentences); m:358 (step 17); and m:361. The hours of m:209–214 are right, and so are 519,480 at m:291, LOCK-m-F3 v0.1 at m:292, G-TIME-F3's 6 and G-F3's 40. m:302's chain matches §4 step 4 node for node, and m:358 step 17 names `— secondary DVs`. The (7′) record is at archived v1.6:40: "base has no control (no instruction-following)".
- **Every `RESULTS.md@18c32df` anchor,** each with what the raw says is there:
  - :24, :404 and :406
  - :72–73, with the quote
  - :85–89, :88 and the quote spanning :88–89
  - :380–381
  - :382–383
  - :384–404
  - :811
  - :817–819
  - :5495
  - :5657
  - :13048–13063: four datacentres, US-CA-2 absent, and the volume `o73qvy742n`
- **`m_analyze.py`.** Its sha256 is `655e0f7f…c16f` at 18c32df and in the working tree. :98 matches byte for byte, :384 matches, and :392 cites m:347. :494 is `PENDING_SUBSTATES`, and the refusal's condition is at :525.
- **The files.** `runner_olmo.py` was added only in `5f7b968`. The manifest has four entries, base, sft, dpo and instruct, and m runs three of them.
- **The four sha256 quotations** are at addendum :4 and :67 and hold two values. `18c32df` and `7631f8a` both resolve.
- **The BK clone:** commit `7631f8a06cdeffaf8b7a89212e5ccbe55a657732`, tree `d6f1d50525874355d1ea992f8f652358742ae282`.
- **`figure4.csv`.** Every row is arm `fixed` with N = 80, and all eight table values match the CSV to six places.
- **`figure3.csv`.** Its sha256 is `f63db30d…90fe`. Its panel `steered_minus_clean_margin` and model `olmo_32b` are right, and its valenced series has N = 160.
- **The PDF.** Its sha256 is `e92c69cb…fa49`, it has 38 pages, and it was extracted with PDFKit. The caption quote is verbatim at p. 9.
- **N5's design description** matches the caption and BK §4.3: the OLMo-2-0325-32B checkpoints (table, lines 149–152), the generation design, text generated by Instruct, and the vector built on Instruct.
- **The untracked root.** Its 26 paths break down as 5 SVGs, 3 ADDENDA, 6 HANDOFFs, 1 PREPRINT, 4 RESEARCH-NOTEs, 6 files in `archive/` and `tvc2_dump.txt`, 28 untracked paths in all.
- **The LOCK files** at the root are LOCK-g, LOCK-h and LOCK-m-F0.
- **`data/m`.** The contents of `ckpt/` and `reports/` are as stated, and the schedules are 3 × 3 × 2.
- **The 52 raws.** Each has "note" in its name, and none is a box raw or an m-unit raw.
- **The Q-F3 refusals:** `keys.py:66–67` (verbatim), `resume.py:385` and `:1158`, `audit.py:87–90` and `__init__.py:7`. No F3 runner, F3 verifier or reasoning-line class exists.
- **The runpod MCP** is unauthenticated in this session too.
- **Notes N1–N7** in substance, with I2's caveat on N7.

## 2. Code's dispositions (applied before the commit)

Each item was re-verified by Code against its source before it was applied.

- **F1 — fixed.** The entry now says "no box entry or box raw after 2026-08-25 (B2-r)". Box work ran on 2026-08-24
  (B3, B2, the cached-generation gate, the respawns) and on 2026-08-25 (B2-r).
- **F2 — fixed.** The raw now says that "BACKEND" appears in a headline only in 2026-08-19's "… THE BACKEND OF
  RECORD." (RESULTS.md@18c32df:17228–17229).
- **F3 — fixed.** The raw now dates the last box work to 2026-08-24/25 and cites
  `results/raw/2026-08-24_bphase_respawn.txt` and `2026-08-25_b2r_arc.txt`.
- **F4 — fixed.** The raw now reads "No pod start is on record since 2026-08-25". After that date the only mentions
  of a pod are lines saying a pod start needs the PI's go.
- **F5 — fixed in both texts (N8).** The output "holds no Clock date: 2026-10-30 does not appear; the declarations
  carry their comparison date 2026-10-19".
- **I1 — added as note N9,** with Code's arithmetic [C]: the double count is 0.141 h per checkpoint at instruct and
  0.164 h at SFT/DPO. The raw's m:205–214 bullet now says the table already contains the 26 sessions.
- **I2 — fixed (N7 and step 1).** The 52 raws are 51 from the release block (2026-10-27 through 2026-11-05) and one
  from N2(vii) (2026-10-22).
- **I3 — fixed.** The entry now reads "The m package still refuses Q-F3 (…), and `audit.py:87–90` defers Q-F3's
  counter to step 19".
- **I4 — fixed.** Added "runs on the PI's word (§4 step 6)".
- **I5 — fixed.** The entry now discloses the order. The routing orders PROPOSAL-n's §8 after the addendum, but its
  read-only steps 1 and 2 ran beside the addendum's step 2, before this commit. Its step-1 delta read is repeated
  after the commit. The second half of the item, why PROPOSAL-n stays untracked, is answered in PROPOSAL-n's own STOP
  entry and raw.
- **I6 — added as note N11.** Step 2 now reads "every referent of §5 within Code's reach resolves".
- **Not graded:**
  - "N1" for PROPOSAL-n's pod unit is added as note N10.
  - The values-check raw the entry names is this file.
  - The negative-pole line is item A1 of PROPOSAL-n's STOP.
