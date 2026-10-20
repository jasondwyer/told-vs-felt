# Step 17 — addendum to the seat's block (v1.1): the second invocation

*Design seat, 2026-10-19. On Code's raw `results/raw/2026-10-19_m-verdicts-qf0.txt` (its §§5–7: the refusal, Code's diagnosis, its check of v1.1). For the PI to route with his word. This file is placed beside the block and committed by path by the PI.*

## The PI's word (for Code)

> Second invocation, on the seat's addendum: the same command with every path on the command line absolute. Nothing else changes; the analyzer is not edited. Append the invocation as typed, its stdout and stderr verbatim and EXIT to the same raw as its next section. On exit 0, commit as the block's §4 has it.

## The seat's addendum

1. **The refusal is accepted as the analyzer's reading of the command, not of the record.** Code's §6.3 diagnosis stands: `_prod_committed` (`scripts/m_analyze.py:1768–1773`) returns "outside the repository" whenever `_repo_rel(p) == str(p)`, which is true of a path typed already repo-relative from the repository root, and false of the absolute form of the same file, which returns the blob of record (the lock `fc7e9db8…015c`, the table `af5cb816…f902`; Code's `diag17.py`). The block's §3 gave `--lock` and `--sentences` relative; that is the seat's slip, not Code's, and it is corrected here. The analyzer of record is not edited (PIN-14 binds its hash to the lock's text); the quirk is a CLI reading, **flagged for the next hash-moving round of the analyzer** (before step 19, where C7 defers G-ANL-F3's versioning), with Code's §6.3b beside it: `flag_of_record` on a relative `--flag-source` records the flag FALSE without a refusal, so at step 18 the `posting` command's `--sentences`, `--rewrites` and `--flag-source` are given absolute too. Carried to the step-18 block.

2. **§3 of the block is amended: every path on the command line is absolute.** The invocation, with the two input files Code wrote (`data/m/verdicts/Q-F0_decisions.json`, `data/m/verdicts/Q-F0_olmo-states.json`, the raw's §3):

   `python scripts/m_analyze.py verdicts --unit Q-F0 --lock /Users/jasondwyer/Documents/code/jspace-lab/LOCK-m-F0.md --sentences /Users/jasondwyer/Documents/code/jspace-lab/data/m/gates/m_posting_sentences.json --decisions /Users/jasondwyer/Documents/code/jspace-lab/data/m/verdicts/Q-F0_decisions.json --olmo-states /Users/jasondwyer/Documents/code/jspace-lab/data/m/verdicts/Q-F0_olmo-states.json`

   `--campaign`, `--time`, `--qual`, `--flag-source` and `--out` stay at their absolute defaults (REPO-based, `scripts/m_analyze.py:8224–8232`). The outputs record each input's path repository-relative (`_file_rec` → `_repo_rel`), so their bytes do not depend on the form typed (Code's §7.3). The block's "one invocation" is read as one invocation that reaches V2; this is the second typed and the first that does.

3. **Nothing else in the block moves.** §§1–2 and §§4–8 stand; Code's §7.2 check of v1.1 is accepted (the inputs as written, the homes and names, the raw's name, the anchors). The battery's run 1 (446/448, exit 1, Code's concurrent write of the two inputs, disclosed) is inert; run 2 (448/448, exit 0, write-free) is the battery of record. The block's file, saved by the PI at the repository root (Code's §7.1), was moved by the seat over the bridge to `results/raw/2026-10-19_m-design-to-code_step17.md`, bytes unchanged (`0b5716e6…b5cb`, Code's hash); this addendum was placed beside it the same way; both are untracked until the PI commits them by path.

4. **The raw.** The second invocation goes into the same raw, `results/raw/2026-10-19_m-verdicts-qf0.txt`, as its next section (the typed command, stdout and stderr verbatim, EXIT), so the refusal and the run of record sit in one file; the preconditions need no third pass unless the tree changed since the raw's §4.
