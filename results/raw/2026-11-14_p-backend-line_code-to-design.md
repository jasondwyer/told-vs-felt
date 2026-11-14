# §B.4 item 7: where the backend comparison's line can print (Code → design)

*The pod session (Code), PI date 2026-11-14. For the PI to route. On the seat's answers of 2026-11-14
(`results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md`, sha256 `6b963adf…db3a`, committed by the F3
session at `cdccc66`), §B.4 item 7, and the routing block's item 8 ("item 7's comparison line printed in the precheck ×3
raw"). The PI holds the three locks until the seat answers (§4). Nothing ran on a model or the box; this block reads
code and committed raws: `valence_core/p/stage.py` (sha256
`3390a448…a406`, the campaign wiring's BUILD, `c0f1c69`), `valence_core/p/proxy.py` (`db64903e…640a`), m's
`valence_core/m/stages.py` (`42cb4002…275f`) and `valence_core/m/resume.py` (`78f2fc8e…8fb7`), each unchanged since
`c0f1c69`; the BUILD's entry; `results/raw/2026-11-11_p-qual.txt` (`6cbb52fe…e2d9`) and
`results/raw/2026-11-06_respawn_determinism.txt` (`8f2b239b…963e`). No checkpoint, call log or report was opened (the
list of record v2).*

## 0. The short form

- The seat's sentence (§B.4 item 7): "The live comparison runs at every non-stub precheck; **its line — the lock's
  identifier against the adapter's, equal — is printed in the precheck ×3 raw at `campaign`**, so that the record shows
  the check ran where the self-test cannot."
- As built, the precheck runs before the load and never sees the adapter's identifier. The comparison runs after the
  load, in each recorded run, and prints nothing when the two are equal. So the precheck ×3 raw has no such line to
  print.
- Four readings follow (§2), each with what it prints and what it moves. Code adjudicates none of them. Only (c)
  changes p's code, and with it p's package hash, which each v1.0 draft names.

## 1. What the build does

1. **The precheck** (`precheck`, before the load) reads the lock's one `BACKEND OF RECORD` line (`lock_backend`,
   `stage.py:615`) and returns it as `backend_of_record` (`:639`). The box's precheck raws print it: at `qual`,
   "backend of record 641ee466f4553b6a" for each unit (`results/raw/2026-11-11_p-qual.txt`, lines 310–312). No adapter
   is loaded there.
2. **The live comparison** runs in `_run_recorded`: after the load, inside the substitutions, before m's stage, at the
   gates and at the campaign. It computes `m_resume.backend_identifier(px.provenance())` and compares it with
   `backend_of_record` (`stage.py:1352–1357`).
   - Equal: nothing is printed or written, and the run goes on.
   - Different: a STOP, "the adapter's backend identifier {bid} is not the lock's {…} (m:302; a superseding BACKEND
     entry is the seat's to route) -- nothing generated".
3. **What the run records anyway.**
   - p passes the proxied adapter to m's campaign (`run_campaign(px, …)`, `stage.py:1550`). The proxy reads
     `provenance()` through to the adapter.
   - m builds the checkpoint's identity from that adapter (`_identity`, m's `stages.py:2065`). Its `backend_identifier`
     is `backend_identifier(adapter.provenance())` (`:1109`): the comparison's operand, by the same function.
   - m's campaign report copies it (`"identity": _ident_summary(ident)`, `:2412`; the summary's keys include
     `backend_identifier`, `:1346–1349`), with each launching invocation's provenance record (`report_provenance`). m
     writes the report at each pause and at the end (`:2470–2473`, `:2528–2529`).
   - The report is under `data/p/reports`, the read domain. The checkpoint is closed (the list of record v2, item 2).
4. **The BUILD's item 7**, in full: "**S3, a gap shared with the gates.** The backend comparison never runs on the
   stub, so no self-test case kills a mutant that drops it. This was so before this build." It names no precheck
   line.

## 2. Readings for the seat

- **(a) The new box's identifier beside the lock's.**
  - Prints, in the precheck ×3 raw: the lock's line (the precheck's `backend of record`) beside respawn (ii)'s
    identifier for the new box. As on 2026-11-06, that identifier is m's `backend_identifier` over the provenance
    block the box's characterization run printed, computed by Code's laptop check after the transfer
    (`results/raw/2026-11-06_respawn_determinism.txt`, lines 65 and 69). The block there was the Base adapter's
    (line 5, `--stage base`); `backend_identifier` drops `path`, `seed` and `n_encodes_clipped`.
  - Moves: nothing in p's code or the locks; one line in the box's precheck wrapper.
  - Shows: the box's identifier before the campaign. It is not the stage's comparison at the run.
- **(b) The adapter's identifier, from a load in the precheck wrapper.**
  - Prints, in the precheck ×3 raw: m's `backend_identifier` over each unit's loaded adapter's provenance, against the
    lock's line.
  - Moves: nothing in p's code or the locks; three model loads added to the box's precheck step.
  - Shows: the adapter's identifier on that box before the campaign. It repeats the stage's comparison; it is not the
    comparison itself.
- **(c) A line from the comparison itself.**
  - Prints, in each recorded run's raw (the campaign's raw, not the precheck's): an equality line that `_run_recorded`
    would print after its comparison.
  - Moves: p's package (`a38d93bb…a2d7`). Each v1.0 draft names that hash and the precheck checks it, and G-SHAPE-p's
    and G-ANL-p's artifacts record it. So it needs a BUILD with its review and values-check, both re-runs, and new
    drafts whose diff goes beyond (A1)–(A3), which means a second read. It must land before the locks are committed;
    after that, each lock would need a re-issue.
  - Shows: the comparison's own result, at each run.
- **(d) The run's own record, read once the invocation has ended.**
  - Prints, in the precheck ×3 raw: the lock's line, as `qual`'s did. In each campaign's raw, once its invocation has
    ended (the list of record v2, item 5), whether at a pause, at the end or at a STOP: m's campaign report's
    `identity.backend_identifier` against the lock's line, with the identifier computed from each launching
    invocation's provenance record — the identifier only, never the record's stamp. The gates' raw already recorded
    the identifier against the reports' identity: "backend identifier 641ee466f4553b6a (BACKEND entry, 190ba90; each
    lock's BACKEND OF RECORD line; each report's identity)" (`results/raw/2026-11-11_p-qual.txt`, line 2).
  - Moves: nothing in p's code or the locks. It adds lines to the campaign raws after each invocation, and the
    identifier to the campaign entry's form: under the list of record v2's item 2, a report's content enters a raw
    only as the entry's form reports it.
  - Shows: the identifier m computed from the same adapter by the same function. That is the comparison's operand,
    which m itself compares only at a resume's identity check. It does not show that p's comparison ran: a build
    without that comparison would write the same report. It is not the comparison itself.
  - An invocation that launches no session leaves no provenance entry in the report (`report_provenance`,
    `resume.py:324`), so (d) has no record of it, though p's comparison would run in it after its load.
  - All of this is in the campaign's raw, not the precheck raw, and only after the invocation ends.

Under (a), (b) and (d), p's code and the amended drafts stand. (a) and (d) can be carried together.

## 3. Question

- **Q1.** Item 7's line: (a), (b), (c), (d), or another form?

## 4. Not questions

- **The locks are held.** The PI's word of 2026-11-14, in chat, to the coordinating session's question "Hold the three
  LOCK-p commits until the seat answers item 7?": "Hold the locks". `LOCK-p-OLMo-{ckpt}.md` stay at v0.2. The amended
  drafts are committed beside this block as raws, `results/raw/2026-11-14_p-lock-v1.0-draft-amended_OLMo-{sft,dpo,instruct}.md`,
  each byte-identical to the lock it would become; their diffs against `012ffbe`'s drafts are exactly (A1)–(A3) (this
  commit's entry).
- §B.4's items 1–6 and 8, and §B.3's ruling on the box, are as ruled.
