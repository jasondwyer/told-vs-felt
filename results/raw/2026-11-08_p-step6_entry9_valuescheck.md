# The entry (9) block: the blind values-check, with Code's dispositions

*Code's raw, PI-local date 2026-11-08. The check ran on the block's first draft, before the commit of `results/raw/2026-11-08_p-step6_entry9_code-to-design.md`: a blind subagent given the draft and its sources. Its report is in section 1, verbatim. Every IMPRECISE item was re-checked at source and applied (section 0). The revised claims were checked by the report's own evidence, not by a second blind pass.*

## 0. Code's dispositions

| item | verdict | disposition |
|---|---|---|
| #4 | IMPRECISE | **Applied.** The routing is cited as quoted in `de729c4`'s close lines, item 2, with its opening words, since `da1e1b8` cites an earlier block's item 2 in the same words. |
| #18 | IMPRECISE | **Applied, here and in `valence_core/p/identity.py`** (docstring and self-test label). m rebuilds this run's own build in `_validated` and never rebuilds the identity recorded on disk; on resume `_identity_diff` reports a moved value whichever way the given path keeps the fields. |
| #24 | IMPRECISE | **Applied.** The full list of `Identity` call sites in `valence_core/m`'s self-tests. The m_analyze battery's three calls are named: G-ANL-p runs that battery unchanged, outside p's substitutions, on m's own identities, so neither entry is needed there. |
| #25 | IMPRECISE | **Applied.** The v2 closure's read of the committed campaign bytes (`m_analyze.py:2592`–`:2608`) is named beside `read_checkpoint`. |
| #26 | IMPRECISE | **Applied.** `_check_state` reads unit, stage, template set and n against the sessions, never the key set. |
| note | -- | **Applied.** (8) and (9) always hold together, since with (8) alone an OLMo identity lacking p's fields fails `_validated`'s key-set check. The wrapper adds the fields whenever they are absent. |
| #23 | not checkable | Stands: the wrapper's design is the proposal the seat rules on. |

## 1. The values-check's report, verbatim

## Values-check of `results/raw/2026-11-08_p-step6_entry9_code-to-design.md`

I edited nothing and wrote no files. The only Python I ran was read-only, with `-B`. It used in-memory identities, and I put back every module attribute I changed (both restores were checked and returned True). No model was loaded. The m files are unmodified (`git status` is clean for `valence_core/m` and `scripts/m_*`). Another session is changing p's package while I worked: `valence_core/p/register.py` was modified and `valence_core/p/identity.py` appeared, both uncommitted.

| # | claim (memo line) | verdict | evidence |
|---|---|---|---|
| 1 | :3 the seat's answer is `results/raw/2026-11-08_p-step6_design-to-code_answers.md` at `de729c4` | CONFIRMED | `git show --stat de729c4` shows the file added (32 lines) |
| 2 | :3 sha256 `9e178349…9bab` | CONFIRMED | The blob at de729c4 and the working-tree file are both `9e1783496c7120fa3e4f96511775c4e805c176736baf0f0d5f7e12a4571b9bab` |
| 3 | :3 "§1 Q3" | CONFIRMED | answer:5 is "## 1. The gate stages…"; Q3 is at answer:9 |
| 4 | :3 "the PI's routing of 2026-11-08, item 2" | IMPRECISE | de729c4's close lines quote item 2 as "p step 6: entries (6)–(9) and the confirmations [confirmed]; …". But an earlier block, also dated 2026-11-08 and quoted at daca8b0, has a different item 2 (G-TIME-F3 / ADDENDUM-m2), and da1e1b8 cites that one with the same words. |
| 5 | :3 the answer adopted Code's `c9acd66` Q3 (a) | CONFIRMED | prebuild:56 proposes `IDENTITY_KEYS_OLMO` extended, plus `stages._identity` (:1102) wrapped "after m's builder", kind pins. answer:9 says "(a), two sites, kind pins". |
| 6 | :3 the rest of step 6's build proceeds meanwhile | CONFIRMED (observed) | register.py and identity.py changed during this check. There is no `scripts/p_analyze.py` yet. |
| 7 | :3 entry (9) is in p's package and in the register the locks name; G-SHAPE-p re-run, G-ANL-p and the locks wait | CONFIRMED (working tree only) | Working-tree register.py:117–123 has Entry(9) on `valence_core.m.resume.Identity`, status PENDING. HEAD's register has only (1), (2), (3), (5). Register term (a): every site is named in ENTRIES, the BUILD entry and LOCK-p v0.1. Seat §4: G-SHAPE-p re-runs "on the final package". |
| 8 | :7 entry (9) as declared wraps `stages._identity` to add the four fields after m's builder | CONFIRMED | answer:9, verbatim in substance |
| 9 | :8 every stage start validates its identity in `resume.load_or_init` (resume.py:852) | CONFIRMED | def at :852. The three stage entry points call it with `_identity`'s build: stages.py:1494 (gate stage), :1744 (G-ID), :2072 (campaign). m's G-CAL keeps its own checkpoint (gcal.py:897) and is not a stages.py stage. |
| 10 | :8 which calls `_validated` (:502) | CONFIRMED | def at :502. It is called at :854, the first line of load_or_init, and that is its only caller in m. |
| 11 | :9 `_validated` rebuilds via `Identity(**dict(identity))` (:507) and requires equality | CONFIRMED | :507 verbatim. :508–510 compare as canonical JSON and raise ValueError on a difference. A key-set check against `identity_keys(unit)` comes first (:503–506). |
| 12 | :10 `Identity` (:402) takes fixed keyword arguments | CONFIRMED | `def Identity(*, …)`. `inspect` shows 19 keyword-only parameters and no `**kwargs`. |
| 13 | :10 an identity carrying p's four fields fails the rebuild | CONFIRMED | Reproduced (row 14) |
| 14 | :12 model-free run: `TypeError: Identity() got an unexpected keyword argument 'proposal'` | CONFIRMED | Reproduced verbatim (Python 3.12.9) with entry (8) applied in memory and the four fields appended in the listed order. The field the message names depends on key order: the same identity in canonical (sorted) order names `'p_package_sha256'`. Without entry (8), the ValueError at :506 comes first. No raw records Code's run. |
| 15 | :12 the stage would refuse at its start, before any session | CONFIRMED | The TypeError propagates out of stages.py:1494. That is after the startup sequence (`_begin`, `_licensed`, `load_committed`, `_startup`) and before the first checkpoint write (:1504) and the first launch (:1516–1517). It is an uncaught exception, not one of m's refusal messages. |
| 16 | :16 `valence_core.m.resume.Identity` is "m's builder" | CONFIRMED | Docstring at :408 ("Build and validate a resume identity"); it returns the canonical dict (:499) |
| 17 | :17 p's four field names | CONFIRMED | answer:9 and prebuild:43. G-CAL-p's checkpoint at b6ef939 (`data/p/ckpt/G-CAL_olmo-sft.json`) carries all four in its identity, with `proposal` = "PROPOSAL-p". |
| 18 | :18 "Given (the rebuild of a recorded identity) … keeps them as recorded, so m's identity diff still reports a moved value on resume" | IMPRECISE | See below |
| 19 | :19 "absent" is the stage's own build | CONFIRMED | stages.py:1106–1113 passes 13 m keywords and none of p's |
| 20 | :23 `stages._identity` calls `_resume.Identity` (stages.py:1106) | CONFIRMED | def at :1102, call at :1106; `from . import resume as _resume` at :131 |
| 21 | :24 `_validated` calls its own module's `Identity` (resume.py:507) | CONFIRMED | :507 |
| 22 | :26 both names resolve at call time, so one site serves both callers | CONFIRMED | Bytecode: `_identity` does LOAD_GLOBAL `_resume` then LOAD_ATTR `Identity` (line 1106); `_validated` does LOAD_GLOBAL `Identity` (line 507). `stages._resume is resume` and `_validated.__globals__ is vars(resume)` are both True. A recorder put in place of `resume.Identity` in memory was reached by both callers, then restored. Nothing in valence_core/ or scripts/ imports `Identity` by name. `identity_keys` also reads `IDENTITY_KEYS_OLMO` at call time (:114), so entry (8) takes effect. |
| 23 | :16–20, :26 the wrapper's design (optional keywords, form check, computed values, kind pins, entry (8) unchanged) | NOT CHECKABLE | These are proposals for the seat. The in-progress `valence_core/p/identity.py` implements them. |
| 24 | :31 every other `Identity` call in m is in m's self-tests (listed sites), which p never runs | IMPRECISE | See below |
| 25 | :32 m's analyzer reads a p checkpoint through `resume.read_checkpoint` (m_analyze.py:2054 and later) | IMPRECISE | :2054, :2341, :2623 and :4191 do use read_checkpoint. But `run_not_run`'s v2 closure reads the committed campaign bytes with `json.loads` (:2592–2608) and checks only unit, stage and a sessions list. That path has no key-set check either. |
| 26 | :32 "That read checks the identity's type only (`_check_state`, resume.py:555), never its key set" | IMPRECISE | The path is read_checkpoint :682 → `_read` :678 → `_check_state` :555. Besides the dict check (:564), `_check_state` reads the identity's stage (:572), unit (:578), template_set and n (:588), and stage again (:616, :627). It never checks the key set: an in-memory checkpoint whose identity carries p's four extra fields passes. |
| 27 | :32 no key-set check elsewhere in m_analyze.py, readrule.py, stages.py, bars.py, verify.py | CONFIRMED | readrule.py and verify.py never reference an identity. bars.py's `ident` (:886) is a session id. m_analyze.py reads single fields with `.get` (:2059–2064, :2223, :2230, :2344–2345, :2603–2607, :2626, :4194–4195, :4243), battery included. stages.py production code reads single fields (:813–818, `_ident_summary` :1346). Its one key-set check, `_extra` at :1004–1005, is on the `identity_extra` input, not on a checkpoint identity, and is not on the analyzer's path. m's only identity key-set check is `_validated`'s (:503–506). |
| 28 | :33 entries (8) and (9) hold at the stage alone; p_analyze needs neither | CONFIRMED (inference) | Follows from rows 25–27. `gate_release` (:2502) copies no identity into outputs. p_analyze is not built yet. |
| 29 | the memo's account of what the seat declared (special-attention item 7) | CONFIRMED | Rows 5, 8 and 17. Entry (8) as the memo keeps it is answer:9's. answer §5 item 1: "Entries (6)–(9) declared". |

### IMPRECISE items, with correct text

- **#4:** "…and the PI's routing of 2026-11-08 quoted in `de729c4`'s close lines, item 2 ("p step 6: entries (6)–(9) and the confirmations [confirmed]; …")". The bare citation is ambiguous because da1e1b8 uses the same words for the earlier block's item 2.
- **#18:** "Given (m's rebuild in `_validated`, which `load_or_init` runs on the identity the stage hands it, i.e. this run's own build; m never rebuilds the identity recorded on disk), it checks their form and keeps them as given. On resume, m's `_identity_diff` (resume.py:514, called at :870 and :884) compares the recorded identity with this run's and reports a moved value."
  - Evidence: `_validated`'s only caller is :854. Every production caller of `load_or_init` (stages.py:1494, :1744, :2072) passes `_identity`'s fresh build; every other caller is a self-test or the m_analyze battery.
  - The diff behaviour itself reproduces: a moved `p_package_sha256` is reported. But it holds whether the given path keeps or recomputes the values, because the build and the rebuild both carry this run's values.
  - The in-progress `valence_core/p/identity.py` repeats the same phrase (docstring :12–13, self-test label :92).
- **#24:** "Every other `Identity` call in valence_core/m is in a module self-test, which p never runs:
  - resume.py:1107, :1115, :1345, :1358, :1369, :1684, :1688 (`_selftest`, :1070);
  - runner_olmo.py:396 (`_selftest`, :182);
  - runner_qwen.py:509 (`_selftest`, :213);
  - stages.py:2934, :3561, :3665, :3895, :4308 (`_selftest`, :2609).

  m's scripts call it in scripts/m_sessions.py's `_selftest` (:1963, :4389, :4722, :4738, :4975, :5669, :5685). They also call it in scripts/m_analyze.py's battery: `_Camp` :6574 and :6634, and `_bt_olmo_gates` :9257, reached from the 'reader path' group at :11028. G-ANL-p runs that battery unchanged (the seat's Q8). It runs outside p's substitutions, on m's own Q-F0 and OLMo-sft identities, so neither entry is needed there."
  - The memo's list leaves out runner_qwen.py:509 and five resume.py sites. Its "which p never runs" does not hold for the m_analyze battery if "m" includes m's scripts.
- **#25:** "m's analyzer reads a p checkpoint through `resume.read_checkpoint` (scripts/m_analyze.py:2054, :2341, :2623, :4191) and, for a v2 closure, by parsing the committed campaign bytes (:2592–2608)."
- **#26:** "That read checks that the identity is a dict and reads its unit, stage, template_set and n against the sessions (`_check_state`, resume.py:555; :564, :572, :578, :588), never its key set."

### Counts
29 items: 23 CONFIRMED, 0 FAIL, 5 IMPRECISE (#4, #18, #24, #25, #26), 1 NOT CHECKABLE (#23).

### Note (not a memo claim)
With entry (8) in force, an OLMo identity that lacks p's four fields fails `_validated`'s key-set check (ValueError; reproduced). So (8) and (9) must always be in force together. The memo's wrapper adds the fields whenever they are absent on an OLMo identity, which covers this.
