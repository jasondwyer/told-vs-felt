# n — a supplement to the seven starred readings before G-TIME-n's run: Q8, the two steered cells (code → design)

*The n-build session (Code), PI date 2026-11-21. For the seat, before G-TIME-n's run, with the block it supplements:
`results/raw/2026-11-21_n-gtime-starred-seven_code-to-design_STOP.md`, committed at `2ca24e8`. The PI's word governs
only the nudge to the seat.*

*Where things stand:*
- *The block's seven readings, GT1, GT4, GT8, GT9, GT10, GT12 and GT16 (Q1–Q7), are with the seat.*
- *G-TIME-n's BUILD is drafted on GT1–GT17 as PINs, in the driver alone. Its blind review of draft 3 found no BUG.
  The BUILD is not yet committed. Its commit, after this one, carries the review's report whole
  (`results/raw/2026-11-21_n-gtime-build_review.md`, its §2: sha256 `004f9c8e…0915`, 189 lines), with every
  disposition and the self-test of the driver it commits.*
- *The review's observation O2 raises one more question, Q8, about GT11. The BUILD will commit with Q8 open and the
  safer form as its default (§2 (ii)). G-TIME-n runs only after the seat's answers on Q1–Q8.*

*Cited forms: B:line is the block at `2ca24e8`; n:line is PROPOSAL-n v0.2
(`PROPOSAL-n-bk-reconciliation-v0_2.md`); C:line is `CLAUDE.md`; the spec raw is
`results/raw/2026-11-21_n-gtime_spec.md`, committed with the block. F and O numbers are the review's.*

*Code reads, builds and asks. Every reading below is Code's, and the seat rules it; Code adjudicates none.*

## 0. The short form

- GT11, as routed, commits G-TIME-n's three cells' JSON. Two of them hold the steered margins of twelve reads on six
  of the campaign's own sessions (the review's O2, §1).
- The BUILD commits with those two cells kept on the box, the safer form (§2 (ii)), until the seat rules.
- Q8 (§3) asks which of four options, or another, and whether the shadow cell is committed. §4 corrects two wordings
  of the block, from the BUILD's review.

## 1. The question's ground

- **GT11, as routed** (the spec raw, §1): "New `.gitignore` lines admit the report, the cell JSON and the artifact."
- **G-TIME-n's three cells** (B:63–107, GT1; the names by `schema.cell_filename`):
  - `N1-V__none__0.json`: the six shadows, at d = 0;
  - `N1-V__valence__p1.json` and `N1-V__valence__p1_2.json`: the twelve steered reads, valence at +1 and +1/2, on runs
    0, 32, 64, 95, 127 and 159.
- **What a cell holds.** Each record carries its read's cached log-probabilities and margin, and a re-computed read
  its fresh re-computation too (`schema.py`'s RECORD_FIELDS: `logprob_S`, `logprob_U`, `margin`, the restricted read
  and its pick, `fidelity`). That is why `data/n/ckpt/**` never renders in a diff (.gitattributes:19–21: "the stages'
  cells, whose records carry each read's margin and the restricted read's pick").
- **The review's O2,** verbatim:

  > O2 — The committed cells carry steered margins. GT11 admits N1-V__valence__p1.json and N1-V__valence__p1_2.json:
  > the cached margins of 12 steered reads (valence +1 and +1/2) on six of the campaign's sessions. On the
  > deterministic backend these are expected to equal the campaign's own reads of those sessions. Item 2 and -diff
  > close them, but a push to the public origin publishes them before the campaign (n:148, "No looks");
  > backend-ext's committed cells were d = 0 only. For the seat: confirm GT11 as built, or keep the two steered cells
  > on the box with their arrays (the report and the artifact carry their hashes and every duration).
- **Code's reading of it.** The campaign reads the same six sessions at +1 and +1/2 in N1-V. So the two steered
  cells, once committed and pushed to the public origin, would put six sessions' steered margins in the open before
  the campaign. n §6 (n:148): "No looks (§2.5)."
- **The shadow cell.** It holds d = 0 reads alone. Its precedent is the BACKEND extension, whose cells the
  `.gitignore` admits only at d = 0: `data/n/ckpt/backend-ext/N1-V__none__0.json` and
  `data/n/ckpt/backend-ext-2/N1-V__none__0.json` (.gitignore:294 and :300).
- **What does not depend on Q8.** G-TIME-n's report holds "no margin or other per-read model output"
  (schema.py:154–155), and its projection artifact no margin and no log-probability (GT11 as sent): counts, states,
  read ids, durations and sha256s. The projection needs only durations. G-TIME-n's records enter no DV (GT13).

## 2. The options, and what each changes

The coordinating session gave three facts for the framing, as context, not as a ruling:
- `data/n/ckpt/**` is already `-diff` (.gitattributes:21) and closed by the list of record's item 2. m's and p's
  checkpoint files, which carry picks, are committed that way.
- Keeping the steered cells on the box alone sits against ledger 27 (C:359: "A run that exists only on a box does not
  exist.").
- The BACKEND extension's committed cells were d = 0 only, and they are the precedent for the shadow cell.

The options for the two steered cells' JSON. In all of them every cell's capture arrays stay on the box, as at the
BACKEND extension:
- **(i) GT11 as routed.** Committed with the report, under `-diff` and closed by item 2, and pushed with the rest. In
  the build: two `.gitignore` lines, admitting the two cells.
- **(ii) The box alone. This is the BUILD's default:** its `.gitignore` admits only the shadow cell, the report and
  the artifact. The two cells' JSON stay on the box's volume beside every cell's arrays. Their sha256s are in the
  committed report (its `cells`: each file's `json_sha256` and `capture_sha256`). It sits against ledger 27 for those
  two files. In the build: nothing.
- **(iii) Copied back by hash, and committed only after the campaign.** They are kept on the laptop outside the
  repository, in a folder the launch files name, until the campaign's VERDICTS, then committed by path. In the build:
  nothing. In the launch files: the copy-back by hash. Later: a commit after VERDICTS.
- **(iv) Committed under `-diff` as m's and p's checkpoints are, but held from the push until the campaign.** In the
  build: GT11's two lines. In the routing: the pushes, which are the PI's, wait. A push carries every commit before
  it, so no later commit is pushed until then either.

The shadow cell is committed in every option, as the BACKEND extension's were.

## 3. The question

- **Q8 (GT11).** Which of (i)–(iv), or another, for G-TIME-n's two steered cells' JSON? And is the shadow cell
  committed, as at the BACKEND extension? The BUILD commits with (ii) as its default. G-TIME-n's copy-back and its run
  entry follow the answer, and neither steered cell is committed before it.

## 4. Two corrections to the block, from the BUILD's review

- **GT9 (B:203–246).** The block says the benchmark's template is "re-keyed to each session of the set in turn (its
  session's ids, read id and launch index)". As built (`rekeyed`), the copy moves its session's id, cell and run, its
  read id, its shadow's read id and its launch index. Every other field is the template's, its token ids' sha16s,
  sequence length, spans, cues and labels among them. The schema does not cross-check those fields (its CROSS-RECORD
  PROPERTIES paragraph), and the review reads the timing as unaffected. That is the review's F8.
- **GT4 (B:109–159).** The block says "For a run of record, each pin is checked against the committed file that
  carries it, before the load". As built, every pin is checked at every invocation, a smoke's too. That is the
  review's F10. It is stricter, and it means a smoke cannot run a changed package.
