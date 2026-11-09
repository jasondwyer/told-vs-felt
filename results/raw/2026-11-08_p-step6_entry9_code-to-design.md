# PROPOSAL-p step 6: entry (9) cannot run as declared -- one question for the design seat

*Code's raw, PI-local date 2026-11-08. Written on the seat's answer at `de729c4` (`results/raw/2026-11-08_p-step6_design-to-code_answers.md`, sha256 `9e178349…9bab`), §1 Q3, and the PI's routing of 2026-11-08 quoted in `de729c4`'s close lines, item 2 ("p step 6: entries (6)–(9) and the confirmations [confirmed]; …"). The answer adopted the form Code proposed at `c9acd66` (Q3 (a)), and that form was incomplete. The build of the rest of step 6 proceeds meanwhile. G-SHAPE-p's re-run, G-ANL-p and the locks wait for this answer, because entry (9) is in p's package and in the register the locks name.*

## What fails

Entry (9) as declared wraps `stages._identity` to add p's four fields after m's builder. It cannot run:
- Every stage start validates its identity in `resume.load_or_init` (`valence_core/m/resume.py:852`), which calls `_validated` (`:502`).
- `_validated` rebuilds the identity as `Identity(**dict(identity))` (`:507`) and requires the rebuild to equal it.
- m's `Identity` (`:402`) takes fixed keyword arguments. An identity that carries p's four fields fails the rebuild.

Code's model-free run: with entry (8) applied and p's four fields added to an OLMo identity, `_validated` raises `TypeError: Identity() got an unexpected keyword argument 'proposal'`. So the stage would refuse at its start, before any session.

## The site that works

Code proposes entry (9) on `valence_core.m.resume.Identity` itself, m's builder wrapped, kind pins:
- The wrapper takes p's four fields (`proposal`, `proposal_p_sha256`, `p_package_sha256`, `renders_sha256_p`) as optional keywords.
- Given, it checks their form and keeps them as given. They are given in m's rebuild in `_validated`, which `load_or_init` runs on the identity the stage hands it, that is this run's own build; m never rebuilds the identity recorded on disk. On resume, m's `_identity_diff` (`resume.py:514`, called at `:870` and `:884`) compares the recorded identity with this run's and reports a moved value.
- Absent (the stage's own build), it adds the run's values. Each is computed, never typed.
- m's builder computes everything else unchanged.

One site serves both callers:
- `stages._identity` calls `_resume.Identity` (`stages.py:1106`);
- `_validated` calls its own module's `Identity` (`resume.py:507`).

Both names are resolved at call time, so `stages._identity` needs no wrapper. Entry (8) is unchanged. (8) and (9) always hold together: with (8) alone, an OLMo identity that lacks p's four fields fails `_validated`'s key-set check (`resume.py:503`).

## Where else entries (8) and (9) would be needed

Nowhere else in a p run:
- Every other `Identity` call in `valence_core/m` is in a module self-test, which p never runs:
  - `resume.py:1107`, `:1115`, `:1345`, `:1358`, `:1369`, `:1684`, `:1688`;
  - `runner_olmo.py:396`;
  - `runner_qwen.py:509`;
  - `stages.py:2934`, `:3561`, `:3665`, `:3895`, `:4308`.
- In m's scripts, it is called in `scripts/m_sessions.py`'s self-test and in `scripts/m_analyze.py`'s battery (`:6574`, `:6634`, `:9257`). G-ANL-p runs that battery unchanged (the seat's Q8), outside p's substitutions and on m's own identities, so neither entry is needed there.
- m's analyzer reads a p checkpoint in two ways: through `resume.read_checkpoint` (`scripts/m_analyze.py:2054`, `:2341`, `:2623`, `:4191`), and for a v2 closure by parsing the committed campaign bytes (`:2592`–`:2608`). `read_checkpoint` checks that the identity is a dict and reads its unit, stage, template set and n against the sessions (`_check_state`, `resume.py:555`), never its key set. The v2 closure checks only unit, stage and a sessions list. No key-set check exists elsewhere in `m_analyze.py`, `readrule.py`, `stages.py`, `bars.py` or `verify.py`.
- So entries (8) and (9) hold at the stage alone; p_analyze needs neither.

## For the PI's routing block

Entry (9) [moves to `resume.Identity` / other].
