# N1 against G-ANL-F3's battery: restoring the preprint fails F3R-PREPRINT-OF-RECORD (Code → design seat, through the PI)

*Code's STOP block, PI date 2026-11-07. It asks the seat to settle a conflict between two parts of its answers of 2026-11-07 (`results/raw/2026-11-07_p-preread_design-to-code_answers.md`, committed at `139635f`), as they apply now:*
- *§7 N1: restore `PREPRINT-v1_0-draft.md` to its bytes of record; "`m_analyze.py`'s three message texts that describe the bannered HEAD (`:4480`, `:4676`, `:9984`) stay as they are … (editing them would move the analyzer for prose)".*
- *§7, after N12: "The analyzer's blob (`6ec3222b…93d9`) is untouched by all of this."*

*The PI routed N1 "[go]" (routing item 2, quoted in RESULTS.md's close line at `139635f`).*

## 1. The finding

- **Where.** `scripts/m_analyze.py:9983–9986` (blob `6ec3222b…`, unchanged at HEAD `993eba1`) is not prose. It is the G-ANL-F3 battery check `F3R-PREPRINT-OF-RECORD`. Its label is `:9983–9984` (the seat's ":9984"), and its condition is `:9985`:

  ```
  pp.get("blob_sha256") == pp.get("table_sha256") and pp.get("head_file_sha256") not in (None, pp.get("table_sha256"))
  ```

  `head_file_sha256` is the sha256 of the working-tree file (`:9892–9895`). The check therefore asserts that the file at HEAD is *not* the bytes of record, which holds only while the banner is there.
- **What it does after N1.** The check is false, so the battery does not pass and `m_analyze.py --selftest` exits 1. `ganl` prints "STOP: the battery did not pass; nothing written", so `data/m/gates/G-ANL-F3.json` cannot be written, and LOCK-m-F3 v0.1, which names it, cannot follow.
- **Who found it.** The F3 session found it while preparing the canonical `ganl`. A blind values-check of N1 found it again independently and evaluated the condition on both trees: true on HEAD's bannered file, false on N1's.
- **The other anchors.**
  - `:4480–4481` is a message, and the comment at `:9871–9872` describes the bannered HEAD. These are prose.
  - `:4676` is PIN-17's text about the preprint of record, not about the bannered HEAD.

## 2. State

- **N1** is prepared and tested: the file restored to `45b67246…7a41`, the sidecar `PREPRINT-v1_0-draft.STATUS.md`, N18's sidecar case, and `README-NOTE.md:78`.
  - Its blind values-check found 38 items with 1 FAIL, which is this conflict.
  - It is **held**, and its edits are out of the shared tree.
- **The hygiene commit** (N9, N12) has landed as `993eba1`, and the G-SHAPE-F0/F3 re-runs are under way.
- **The canonical `ganl` and LOCK-m-F3 v0.1 wait** for this answer.
- **G-TIME-F3 waits** behind them.

## 3. The options

- **(b) Fix the check in place before LOCK-m-F3 v0.1 (Code recommends).**
  - The change is one check, made state-independent:
    - `F3R-PREPRINT-OF-RECORD` asserts only that the regression is served by the committed blob of record (`blob_sha256 == table_sha256`);
    - it reports `head_file_sha256` without asserting that it differs;
    - its label stops presupposing the banner.
  - The order is the check fix, then N1, then the canonical `ganl`, then LOCK-m-F3 v0.1.
  - The cost: the analyzer blob moves (`6ec3222b…` → new) before any lock or `G-ANL-F3.json` names it, with one battery re-run. This is the pattern N12 already set for m's package hash ("with its consequences taken now, before any lock names the hash").
  - What stays as it is:
    - the three OLMo NOT-RUN outputs at `0f35954` remain bound to the blob that wrote them (PIN-42);
    - p's register regression is identity-bound;
    - Code checks whether either G-SHAPE map lists `m_analyze.py` before running anything.
- **(a) `ganl` and LOCK-m-F3 v0.1 first, on `6ec3222b…`, then N1.**
  - The analyzer stays untouched.
  - The check then fails for Q-F3's life: every later battery run and site check shows m's analyzer self-test failing.
  - The v1 posting, which is N1's purpose, opens once N1 lands.
- **(c) Defer N1** until after Q-F3's VERDICTS. The banner stays, and the v1 posting stays blocked at HEAD until then. Code does not recommend it.

## 4. For the seat

1. **The order: (b), (a) or (c).** If (b), confirm the check's new form as §3 gives it, or word it.
2. **N18, Code's reading of "updated to the sidecar form".**
   - Code kept `PREPRINT_ROUTED`/`PREPRINT_BANNER` at the tag's values, because N18's `SOURCES` assert the release block's quotes of the first.
   - It added a constant, `PREPRINT_STATUS`, and an on-disk case. The case accepts the file at the banner commit's parent blob only without `--preprint-pi-confirmed`, and only if the sidecar begins with the banner's bytes.
   - Confirm, or rule otherwise.
3. **Two residues of N1, for the seat to note or rule:**
   - `README-NOTE.md:214` cites patch v8's `:264` "beneath its banner", which is `:262` in the restored file.
   - `scripts/audit_note_N12_gitleaks.py:146`'s `RELEASE` list still pins the tag's bannered sha256 (`5d677a72…4467`) as the v2 release's record, which the tag still holds. Code leaves both as dated notes unless the seat rules otherwise.
