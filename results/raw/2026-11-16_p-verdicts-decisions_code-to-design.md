# p's VERDICTS ×3: the decisions input (m:318) and what the entries carry, before any run (Code → design)

*The instruct VERDICTS session (Code), PI date 2026-11-16, for the three units together, on the coordinating session's
instruction. The sft and dpo VERDICTS sessions sent their facts and readings, in chat and, for dpo, in a note outside
the repository; each item taken from them was re-verified here against the code and the record. For the PI to route.
On the PI's routing of 2026-11-15 (evening), "Route as given", section B, item 6, and the PI's word for the three
sessions, "Start them", each relayed by the coordinating session. Nothing ran in this session: no `verdicts`
invocation, no Python, nothing on a model or the box. This block reads code and committed text:
- CLAUDE.md (`955788de…8a62`), WORKFLOW.md (`e7195706…b061`) and `.gitignore` (`2ebda7ff…d0c8`);
- PROPOSAL-m v1.11 at root (`42ab36ec…6c6b`; m:271, m:314, m:318, m:320, m:358), PROPOSAL-p v0.2 (`42f2977b…3b32`;
  §0.7, §2.3, §4.1, §5.4, §8 steps 5–7), ADDENDUM-p1 v0.1 (`16cdbc11…cb1b`; §1, §2.4, §4 step 3) and ADDENDUM-m2 v0.3
  (`archive/ADDENDUM-m2-f3-reasoning-block-v0_3.md`, `83093812…fa67`; §3.4);
- the seat's answers of 2026-11-08 on step 6 (`results/raw/2026-11-08_p-step6_design-to-code_answers.md`,
  `9e178349…9bab`, committed at `de729c4`; Q6), with Code's block they answer
  (`results/raw/2026-11-08_p-step6_code-to-design_prebuild.md`, `4b053577…dad7`; Q6);
- the seat's answers on G-CAL-OLMo (`results/raw/2026-11-06_gcal-olmo_design-to-code_answers.md`, `4c3f57d4…bf82`,
  committed at `0f35954`), on G-CAL-p (`results/raw/2026-11-08_p-gcal_design-to-code_answers.md`, `4b77e39a…48e1`,
  committed at `daca8b0`), on G-TIME-OLMo (p) (`results/raw/2026-11-09_p-gtime_design-to-code_answers.md`,
  `7b8b1d5f…adc3`, committed at `e619d3d`), of 2026-11-14 on G-F3 and LOCK-p v1.0
  (`results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md`, `6b963adf…db3a`, committed at `cdccc66`),
  and of 2026-11-15 (evening) on the campaign's go, ADDENDUM-p1 and n
  (`results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md`, `1f3ce1f9…f84b`, committed at
  `a215c28`);
- the RESULTS.md entries of `0f35954` (`PROPOSAL-m OLMo-{ckpt} — NOT-RUN`), `f26bc59` (ADDENDUM-m1's commit),
  `d215d5b` (the dated note on the `PROPOSAL-p v0.2 — COMMITTED` entry), `ec0d9d3` (G-CAL-p), `2258c52` (G-TIME-OLMo
  (p) ×3), `a225a89` (G-F0m-OLMo (p) ×3) and its close at `a2c354e`, `038bf3e` (LOCK-p v1.0 ×3, with the close that
  released the hold), `fa27c45` (ADDENDUM-p1) and `41bfab4` (the campaigns), and Q-F0's VERDICTS entry (`0fa8539`);
- LOCK-p-OLMo-{sft,dpo,instruct} v1.0 (`fafb786d…2bc4`, `25c52f56…3dcf`, `f71c97c1…0e67`, committed at `038bf3e`);
- m's three OLMo not-run records (`data/m/verdicts/OLMo-{sft,dpo,instruct}_not-run-record.json`, `a30df61c…1be7`,
  `4ed8576b…fde8`, `e633b2ac…c829`, committed at `0f35954`);
- `results/raw/2026-11-11_p-qual_task-correct.txt` (`57e9c7dc…56e2`, committed at `a225a89`);
- `scripts/m_analyze.py` (`d347ea0c…5e48`), `scripts/p_analyze.py` (`d3758fc4…7008`), `scripts/p_sessions.py`
  (`9c641e19…a96d`), `valence_core/m/stages.py` (`42cb4002…275f`), `valence_core/p/analysis.py` (`6809a7d2…9d63`),
  `valence_core/p/gcal.py` (`9aa21354…6af5`), `valence_core/p/report.py` (`e807c5ad…5af1`) and
  `valence_core/p/stage.py` (`3390a448…a406`);
- the list of record v2 (`6c1135f5…6cdd`).

No checkpoint, call log or report was opened, and nothing under `data/mf3`. Calendar dates only; the commit hash is the
record.*

## 0. The short form

- **Held:** every p VERDICTS run, until the seat's answer to this block is routed (the coordinating session's
  instruction to the three sessions). No p VERDICTS output exists.
- **Why:** the `--decisions` input is m:318's record of the decisions taken with another unit's outcome known
  (PIN-35). m's analyzer validates it and carries it verbatim into `{U}_VERDICTS.json`, which is written once. The
  record settles two of its items and leaves two questions open. Two more questions bear on what the three VERDICTS
  entries carry.
- **Settled** (§2): the seat's Q6 form gives two items, A-m1's decision (16) as m's records carry it and PROPOSAL-p's
  adoption, each with `other_unit` Q-F0 and `other_state` PASS. m's three NOT-RUNs enter each output's `p` block on
  their own (`analysis.decisions_beside`). The three sessions agree on these.
- **Q1** (§3): which of the decisions Q6's list does not name enter the input, and which go in the entry's text only?
  They are the PI's cap share (2026-11-14), the PI's "Place the locks" (2026-11-14), ADDENDUM-p1's decision (p-1)
  (2026-11-15) and the PI's goes for p's stages. **Stops:** the three runs.
- **Q2** (§3): does a unit's list carry a sibling p unit's outcome, when the sibling's VERDICTS exist before the unit's
  run? **Stops:** the three runs and their order.
- **Q3** (§4): p §2.3's counters are due in the VERDICTS entries over the contrast sessions too, and no p code computes
  that part. For `task_correct` the seat has ruled who computes it and from what, and that ruling presumes a read Q4
  asks about. **Stops:** the entries' counters, not the analyzer's outputs, which do not depend on it.
- **Q4** (§4): the list of record v2 binds "before its VERDICTS or NOT-RUN record", and the three sessions' briefs say
  never to open p's checkpoints. Which applies after a unit's VERDICTS, and for what? **Stops:** the entries' contents
  beyond the analyzer's outputs and the reports, not the outputs.
- Readings (§5), declared and not applied:
  - Q1: (c) for the instruct and sft sessions, (a) for the dpo session.
  - Q2: (a).
  - Q3: (a), Code's own step.
  - Q4: (b), the list of record's per-unit rule, for the counts the record names.

  For Q2, two order-free procedures are named for the seat to weigh, not chosen.
- Not questions (§6): the verdicts path never reaches m's battery or `data/mf3`, and every other argument is settled
  from the record.

## 1. What the input is, in the code

1. `p_analyze.py verdicts --decisions D` passes D to m's `run_verdicts` (`scripts/p_analyze.py:168–192`). m reads it at
   V1 (`scripts/m_analyze.py:2280–2283`) through `decisions_file` (`:710–718`) and `validate_decisions` (`:690–707`):
   `{schema m-decisions-v1, unit, decisions_with_other_outcomes_known}`, each item `{decision, date, other_unit,
   other_state}`.
   - `other_unit` is one of `OTHER_UNITS` (Q-F0, OLMo-sft, OLMo-dpo, OLMo-instruct, Q-F3; `:666`) and not the unit
     itself (`:701`).
   - `other_state` is that unit's known outcome. For Q-F0 and an OLMo unit it is one of `Q5` (`:163`: PASS, REVERSE,
     DEAD, INDETERMINATE, NOT-RUN), PENDING refused (`:683–686`). For Q-F3 it is "NOT-RUN" or `{A1, A2, A3[, A3*]}`
     (`:676–682`).
   - Every item names a decision: "a decision names what was decided (non-empty str)" (`:697–698`).
2. PIN-35 (`:657–665`), m's declared reading, verbatim in part: "m:318's record of decisions taken with another unit's
   outcome known is a REQUIRED declared input (may be an empty list) … carried verbatim into {U}_VERDICTS.json /
   {U}_NOT-RUN.json". The list enters the output as `decisions_with_other_outcomes_known` (`:2385`), and the file's path
   and sha256 as `inputs.decisions` (`:2286`). It enters no computation: A0's state, its tests and the secondaries read
   the records, the counts and the floors, never the list.
3. The outputs are written once (PIN-37, `:1917–1920`). One run writes two, `{U}_VERDICTS.json` and
   `{U}_secondary.json`, and p's staged writer refuses a p command's re-run while either exists
   (`valence_core/p/analysis.py:202–212`). A list found wrong after the run means both outputs moved aside with `git
   mv` to dated names on the seat's ruling, the move recorded in an entry (PIN-37), and a second run. A ruling on the
   list given after any p VERDICTS output exists would, for the other two units, itself be a decision taken after that
   VERDICTS exists (m:318).
4. Beside the list, every p output carries `p.decisions_beside` (`analysis.py:108–121`): m's three NOT-RUNs, each named
   `PROPOSAL-m OLMo-{ckpt}`, with its reason and its output's sha256. It is not an input. The seat's Q6 put them there
   because m's validator refuses a unit naming itself, and p keeps m's unit strings.

## 2. What the record settles

- **m:318**, its last sentence, verbatim:

  > A decision about one unit taken after another unit's VERDICTS exist (an OLMo cap, a PI stop, a declined v1.0 after A0 is known) is permitted and **recorded in that unit's VERDICTS entry or NOT-RUN record as taken with the other unit's outcome known.**

- **m:358**, step 17's OLMo clause, verbatim: "`PROPOSAL-m OLMo-{ckpt} — VERDICTS` and `— secondary DVs` per checkpoint
  as each ends, each recording any decision taken with another unit's outcome known".
- **p:84** (p §4.1's last sentence), verbatim: "Every p record carries, under m:318, the decisions taken with other
  outcomes known: Q-F0's PASS, m's three NOT-RUNs, A-m1's (16), and this document's adoption."
- **The seat's Q6** (`de729c4`, its §2), verbatim:

  > **Q6 — Code's form:** m's validated list carries Q-F0's outcome, Q-F3's where known at the run, A-m1's (16) as m's records carry it (`other_unit` Q-F0, `other_state` PASS), this document's adoption against Q-F0's PASS, and p's own other units' known outcomes; **m's three NOT-RUNs go in the output's `p` block**, each named `PROPOSAL-m OLMo-{ckpt}` with its reason and output sha256, since m's validator refuses a unit naming itself and p keeps m's unit strings. p:84's sentence is read that way; a dated note on p's COMMITTED entry says so.

  The dated note is on the `PROPOSAL-p v0.2 — COMMITTED` entry, added at `d215d5b`.
- **ADDENDUM-p1 §2.4**, verbatim: "This addendum's commit entry precedes the first p VERDICTS session. Each p VERDICTS
  entry records, in m:318's form, that it was computed with Q-F0's outcome known and after this re-specification."
- **A-m1's (16), as its commit entry records it** (`f26bc59`): "(16) is a decision about the OLMo units, taken after
  Q-F0's VERDICTS (A0 PASS, 2026-10-19). … §4 step 4 has each OLMo unit's VERDICTS entry record it (N6)."
- **m's precedent:** m's three OLMo not-run records (`0f35954`) each carry two items in the analyzer's input, each with
  `other_unit` Q-F0 and `other_state` PASS. One is A-m1's decision (16), dated 2026-11-06. The other is the PI's go for
  the G-CAL run those records report, 2026-11-06. The seat specified both (its G-CAL-OLMo answers, line 9): "A-m1's
  decision (16), dated as its commit entry is, and the PI's go for this G-CAL run, 2026-11-06, each with `other_unit`
  `Q-F0`, `other_state` `PASS` (m:318; the referent check's N6)". G-CAL-OLMo was the only stage m's OLMo units ran.

Two items are therefore settled, the same for the three units but for `unit`.
- Q6's first member, "Q-F0's outcome" (p:84's "Q-F0's PASS"), is carried as each item's `other_state`. m's validator
  admits no item without a decision (`:697–698`), so it does not stand alone.
- The first item's text is byte-identical to the one in each of m's three records, and so is its date, 2026-11-06,
  "dated as its commit entry is". The PI routed A-m1 on 2026-11-05 (`ADDENDUM_M1_DATE`, `m_analyze.py:141`).
- The second item's wording is Code's. Its date is the one in the seat's disclosure sentence (F-p3), as
  `valence_core/p/gcal.py:105` carries it: "pre-registered on 2026-11-07 (PROPOSAL-p v0.2, `18b0111`; v0.1 routed
  2026-11-06)". p §5.4 (p:102) says "pre-registered on 2026-11-06". The adoption carries p §0.7's decisions, among them
  (5) D_p 2026-12-15 and (6) the pod budget, 12 h.
- The dpo session's draft has the same two items and words the second differently. The three sessions would use one
  wording, this one unless the seat amends it.

Code's draft, for OLMo-instruct; sft's and dpo's files differ only in `unit`:

```json
{
 "schema": "m-decisions-v1",
 "unit": "OLMo-instruct",
 "decisions_with_other_outcomes_known": [
  {
   "decision": "ADDENDUM-m1 decision (16): the three OLMo units re-registered once, under a new Clock date D_O' = 2026-11-30 (ADDENDUM-m1 v0.1, committed at f26bc59)",
   "date": "2026-11-06",
   "other_unit": "Q-F0",
   "other_state": "PASS"
  },
  {
   "decision": "PROPOSAL-p adopted: PROPOSAL-p OLMo-{sft,dpo,instruct} pre-registered as the OLMo told controls at a frame-word corruption dose (PROPOSAL-p v0.2, committed at 18b0111; v0.1 routed 2026-11-06)",
   "date": "2026-11-07",
   "other_unit": "Q-F0",
   "other_state": "PASS"
  }
 ]
}
```

Q-F3's outcome is known at no run: its campaign is running, and its VERDICTS session runs only after the `POSTING v1`
entry exists (ADDENDUM-m1 (10′), as the seat's answers of 2026-11-15 (evening), §4.1, quote it). So Q6's Q-F3 clause
gives no item.

## 3. The decisions input: two open questions

### Q1: the decisions Q6's list does not name

Q6 names A-m1's (16) and the adoption, and no go. The PI's go for G-CAL-p (2026-11-07) existed when Q6 was written. So
did m's not-run records (`0f35954`), which carry the PI's go for their G-CAL run as an input item. Q6's silence on goes
is therefore not only a matter of date. Since Q6, more decisions about p's three units have been taken with Q-F0's
PASS and m's three NOT-RUNs known, each before any p outcome. Gathered across the three sessions, the decisions Q6's
list does not name are:

- **(i) the PI's cap share,** "2 h each" (PI date 2026-11-14; each lock's §2, LOCK-p-OLMo-{ckpt} v1.0 at `038bf3e`).
  m:318 names "an OLMo cap" among the decisions it records.
- **(ii) the locks' placement:** the PI's "Route as given" + "Place the locks" on the routing of 2026-11-14 (evening),
  section B, item 2, "The hold: release it — place the three amended drafts byte for byte as LOCK-p-OLMo-{ckpt}.md and
  commit by path now …" (the `LOCK-p-OLMo-{sft,dpo,instruct} v1.0 — COMMITTED` entry, `038bf3e`). m:318 names "a
  declined v1.0 after A0 is known"; this is the same decision, taken the other way.
- **(iii) ADDENDUM-p1's decision (p-1)** (PI date 2026-11-15; committed at `fa27c45`). Its §2.4 has each VERDICTS entry
  record, "in m:318's form", that the unit was computed "after this re-specification".
- **(iv) the PI's goes for p's stages,** the class m's precedent puts in the input:
  - G-CAL-p: the PI's routing of 2026-11-07, item 1, "1. The five rulings [confirmed] → Code applies them, the
    coordinating session gives the box go, G-CAL-p runs [go]." (quoted in the G-CAL-p entry, `ec0d9d3`);
  - LOCK-p v0.1 and G-TIME-OLMo (p): the PI's routing of 2026-11-08, item 2, "build → G-SHAPE-p re-run → G-ANL-p →
    LOCK-p v0.1 ×3 → G-TIME-OLMo (p) on the box [go]" (quoted in each LOCK-p v0.1's header);
  - LOCK-p v0.2 and G-F0m-OLMo (p): the PI's routing of 2026-11-10, B1, "... → LOCK-p v0.2 ×3 → G-F0m-OLMo (p) ×3 on
    the box, batched → STOP for the seat's read [go]" (quoted in each LOCK-p v0.2's header);
  - G-PWR (p), the campaign wiring and LOCK-p v1.0: the PI's routing of 2026-11-13, item 4, "p's chain: G-PWR (p) now
    — … → LOCK-p v1.0 ×3 by 2026-12-15, each read by the seat before its commit [go]" (the close on the G-F0m-OLMo (p)
    ×3 entry, `a2c354e`);
  - the campaigns, given in steps: the same routing's items 5, "The replacement pod, on your go, …" ("[go on the spec;
    the timing yours]"), and 6, "Then the bundle, precheck ×3, the three campaigns within one pod session, looks every
    40 launches, the seat adjudicating pauses [go]" (`a2c354e`); the routing of 2026-11-14 (evening), section B, item 4,
    "… three campaigns at 2 h each, (d)'s line after each invocation [go at the PI's timing]" (`038bf3e`); the PI's go of
    2026-11-15, "Go for the pod whenever you need it."; and section B, item 5, of that evening's routing, "The campaigns
    as routed" (both in the campaigns' entry, `41bfab4`). These steps are the go for the run each VERDICTS record
    reports, as m's records carried the go for the G-CAL run they report;
  - these sessions: section B, item 6, "[go, after its commit]", and the PI's "Start them".

  Decisions of other kinds fall in the same date range: the seat's rulings on p's gate stages, and, for sft alone, the
  seat's declaration at `daca8b0` §0.1: "every entry, lock line and posted sentence that reports OLMo-SFT's A0 outcome
  carries *G-CAL-p passed at the bar, 47/64 against 47*". The p block carries that sentence already
  (`declared_sentences`, `valence_core/p/report.py:220–222`).

The readings move nothing but the input's bytes: the list in each `{U}_VERDICTS.json` and its `inputs.decisions`
sha256. No code, lock or hash of record moves.

- **(a)** The input holds §2's two items; (i)–(iv) are recorded in each VERDICTS entry's text, in m:318's form.
  - For it: m:318 places the record "in that unit's VERDICTS entry or NOT-RUN record". Q6's form names no go, though
    m's go-carrying records existed when it was written.
  - Against it: PIN-35 calls the input "m:318's record" (§1 item 2), so under (a) the input would hold less than the
    entry. And m's precedent put a class-(iv) decision, the PI's go, in the input, not in entry text only.
- **(b)** The input holds §2's two items and (i)–(iii): the decisions whose kinds m:318 names (an OLMo cap; the v1.0
  decision), and the one ADDENDUM-p1 asks to be recorded in m:318's form. (iv) goes in the entry's text.
- **(c)** (b), and the PI's go for the campaigns, the run each VERDICTS record reports, as m's records carried the go
  for the G-CAL run they report. The other goes go in the entry's text. The precedent does not separate (c) from (d),
  since G-CAL-OLMo was the only stage m's units ran (the sft session's point), so the earlier gate-stage goes are the
  seat's to add or leave out.
- **(d)** (b), and every member of (iv), with any other decision the seat names. Its further items are not drafted;
  Code drafts them on the seat's naming.

Code's drafts of the items (b) and (c) add, for OLMo-instruct. The (p-1) item quotes ADDENDUM-p1 §1's decision, whose
`{ckpt}` is its own text and not a placeholder:

```json
  {
   "decision": "the PI's cap share for PROPOSAL-p's three campaigns, \"2 h each\" (LOCK-p-OLMo-{sft,dpo,instruct} v1.0, §2, committed at 038bf3e)",
   "date": "2026-11-14",
   "other_unit": "Q-F0",
   "other_state": "PASS"
  },
  {
   "decision": "the PI's placement of LOCK-p-OLMo-{sft,dpo,instruct} v1.0, \"Place the locks\" (committed at 038bf3e)",
   "date": "2026-11-14",
   "other_unit": "Q-F0",
   "other_state": "PASS"
  },
  {
   "decision": "ADDENDUM-p1 decision (p-1): A p checkpoint's outcome enters the posting its `PROPOSAL-p OLMo-{ckpt} — VERDICTS` entry, or its `— NOT-RUN` record, reaches, v1 included (ADDENDUM-p1 v0.1, committed at fa27c45)",
   "date": "2026-11-15",
   "other_unit": "Q-F0",
   "other_state": "PASS"
  },
  {
   "decision": "the PI's go for PROPOSAL-p's three campaigns, given in steps: the routing of 2026-11-13, items 5-6; the routing of 2026-11-14 (evening), section B, item 4; \"Go for the pod whenever you need it.\" (2026-11-15); section B, item 5, of the routing of 2026-11-15 (evening), \"The campaigns as routed\" (the campaigns' entry, committed at 41bfab4)",
   "date": "2026-11-15",
   "other_unit": "Q-F0",
   "other_state": "PASS"
  }
```

**What Q1 stops:** the three `verdicts` runs, since the input is written once into each output.

### Q2: a sibling's outcome

Q6's list carries "p's own other units' known outcomes". m:318's trigger, in its words, is a decision "taken after
another unit's VERDICTS exist", recorded "as taken with the other unit's outcome known". Code reads the trigger as the
VERDICTS' existence, not anyone's reading of them. The three runs are serialized: each needs a battery window from the
coordinating session, one at a time, while Q-F3's campaign runs on the laptop. So the second and third runs come after
one and two sibling VERDICTS exist.

- m's validator accepts a sibling as `other_unit` (it is in `OTHER_UNITS` and is not the unit), with its state word as
  `other_state`, and refuses PENDING. So by rule a sibling's state is known only once its VERDICTS or NOT-RUN record
  exists; the validator checks the word, not the file. Each item still needs a decision.
- p keeps m's unit strings, so an item with `other_unit` OLMo-dpo does not say by itself whether it means m's OLMo-dpo,
  which is NOT-RUN, or p's. Its decision text would have to say.
- At this block's commit no p VERDICTS output exists, so no decision about a p unit has been taken after a p VERDICTS.
- The analyzer copies `data/p/verdicts`' files into its staging directory before m's function runs (`run_staged`'s
  seeds, `analysis.py:190–195`). m's refusals there test only the run's own unit's file names (`refuse_beside`,
  `m_analyze.py:1953–1964`), so it interprets no sibling's output.
- p §8 registers the PI's cap share (step 6) and the PI's go for the box (step 5) as steps, as step 7 registers the
  VERDICTS run, and Q1 lists the first two as decisions. m:318 names "an OLMo cap" and names no analyzer run.

The readings turn on whether a run, or the window that starts it, is a decision about its unit:

- **(a)** It is not. A unit's VERDICTS run is the registered step (p §8 step 7), and the order the windows set is not a
  decision about a unit. A sibling's VERDICTS, though it exists before a later run, adds an item to that unit's list
  only if a decision about the unit follows it.
- **(b)** It is. Each later run's list names the siblings whose VERDICTS exist before it, `other_unit` the sibling,
  with the sibling's state word, which its session reads before the run, and decision text that says p's unit, not
  m's. The three lists then differ by the order the windows set.

Two order-free procedures, named for the seat to weigh and not chosen:

- **(i)** the three input files written and hashed, or committed, before the first run, so no input depends on any p
  outcome or on the order;
- **(ii)** no session reads a sibling's output, and the end notices to the coordinating session carry the exit status
  alone and no unit's state, until the third run ends.

Either keeps every session from knowing a sibling's state at its run. Neither changes that the second and third runs
come after a sibling's VERDICTS exist. Under (a) the lists are the same with or without them. Under (b) they keep the
items (b) would owe out of the inputs, since (i) fixes the inputs first and (ii) withholds the state words.

**What Q2 stops:** the three `verdicts` runs and their order.

## 4. What the VERDICTS entries carry: two open questions

### Q3: the counters due at VERDICTS

- **p §2.3**, verbatim: "Descriptive counters, computed by p's own reporting tool over the checkpoints and gate records
  (the analyzer unchanged for them), tabulated over every generation of every p stage, reported in the gate and
  VERDICTS entries, deciding nothing (rule 23)".
- **`task_correct`, the seat's ruling** (its G-TIME-OLMo (p) answers, line 34), verbatim in part: "over the sham
  sessions' rounds at every gate-stage entry (forced and free; the contrast sessions' rounds at the unit's VERDICTS,
  where the free rounds are released)", and, in the same line: "**Tabulated by Code's own step from the records at each
  entry** (A-m2 v0.3 §3.4's form), not by p's package or the analyzer: no package moves, no hash moves, no re-run."
- **A-m2 v0.3 §3.4's form** (`archive/ADDENDUM-m2-f3-reasoning-block-v0_3.md:48`), verbatim in part, the source's bold
  dropped: "At VERDICTS the analyzer is untouched: Code tabulates (a), (b) and the Q4 review counter with mf3's
  functions over the same records in its own step, reported in the VERDICTS entry beside the analyzer's outputs".
- **The seat's answers of 2026-11-14**, §B.4 item 3 (line 67), on the campaign's report: "The VERDICTS entry opens the
  rest (m:271)."
- **What p's stage reports compute.** `report.session_counters` (`valence_core/p/report.py:260–303`), called once per
  stage report (`valence_core/p/stage.py:966`), counts the hair trigger over every round of every session, then the
  sham rounds' control characters, harness-shaped first lines, cap hits and refusals, the corrupted-spelling counter
  over the sham forced rounds, and the contrast forced rounds' control characters: "every other count is
  ``WITHHELD``" (its docstring, `:270`). `WITHHELD` (`:249–252`), verbatim: "the contrast sessions' counters other
  than the forced rounds' control characters, every count over a contrast free round, and the corrupted-spelling
  counter over the sham sessions' free rounds (it reads the round's item, which the sham read withholds because it
  names the pick): withheld to the unit's VERDICTS (m:318; m's read rule, the seat's ruling (h)), recomputable from the
  checkpoint". The proxy's counts over the contrast sessions are withheld too ("every proxy count over the contrast
  sessions withheld, as at G-TIME", `stage.py:35`, of G-F0m-OLMo (p)'s report). The campaigns' entry (`41bfab4`)
  defers the same counts to each unit's VERDICTS.
- **No p code computes the withheld part.**
  - `p_analyze.py verdicts` writes m's two outputs with the `p` block, whose keys are the proposal, the register, the
    roots, the analyzers, D_p, the disclosure, `decisions_beside`, the declared sentences and the staging note
    (`analysis.py:155–160`). It carries no p counter and no `task_correct`. m's own counters in the output are m:314's.
  - `p_sessions.py`'s report commands (`time-report`, `qual-report`, `campaign-report`; `:715–733`) rebuild the same
    stage reports, with the same part withheld, written once.
  - `report.counters` (`:225–246`) is G-CAL-p's form, over records keyed by pool, item and seed (called at
    `valence_core/p/gcal.py:408`), not over session records.
  - `task_correct` was computed at G-F0m-OLMo (p) by Code's own script, whose read licence is "the reads files' sham
    records only, never the checkpoint, the call log or a contrast session"
    (`results/raw/2026-11-11_p-qual_task-correct.txt:36`).
- **A tool inside p's package would move p's package sha256.** Each LOCK-p v1.0 pins it (§4), and `p_analyze` refuses a
  VERDICTS whose lock does not name the current one (`lock_binding_problems`, `scripts/p_analyze.py:156–165`, applied
  at `:173–176`). Such a tool landing before the last of the three runs would make the remaining runs refuse.
- **Readings:**
  - **(a)** Code's own step, the form the seat ruled for `task_correct` (A-m2 v0.3 §3.4's): after a unit's analyzer
    output exists, a script outside p's package computes the contrast sessions' `task_correct` and p §2.3's withheld
    counts with p's own counter definitions and the frozen key table, over that unit's released records, and the
    VERDICTS entry reports them beside the analyzer's outputs. The script and its stdout are committed in a raw. No
    package or hash moves. It needs Q4's read.
  - **(b)** A tool inside p's reporting code, landing only after the last of the three runs (above).
  - **(c)** The entries report the read-domain part the stage reports carry and name the rest "not computed at
    VERDICTS"; a later entry reports it. For `task_correct` this departs from the seat's ruling.
  - **(d)** The seat's full read of the sessions (m:318's "the reads") carries the withheld counts.
  - **(e)** Another form.

**What Q3 stops:** the entries' counters, not the analyzer's outputs, which do not depend on it.

### Q4: the read rule after a unit's VERDICTS

- **The read rule.** The list of record v2's §2 heading, verbatim in part: "binds every session — Code's, their
  subagents', the coordinating session's — on the laptop and the box, for every unit before its VERDICTS or NOT-RUN
  record; open today: Q-F3 (`data/mf3`), p (`data/p`), n (`data/n`) once it writes". The three sessions' briefs say:
  "**p's checkpoints and call logs** (`data/p/ckpt`) are read only by the analyzer (list v2 item 2). Never open them
  yourself." They give no end to that. `data/p/ckpt` holds all three units' files, so once one unit's VERDICTS exist,
  the other two are still before theirs.
- **What the record already presumes.** The `task_correct` ruling (Q3) has Code's own step tabulate "from the records"
  at the unit's VERDICTS. p §2.3 has its counters computed "over the checkpoints", and `WITHHELD` calls them
  "recomputable from the checkpoint".
- **Q-F0's precedent, which m does not require.** Q-F0's VERDICTS entry (2026-10-19, committed at `0fa8539`) also
  carried Code's own extractions from the released checkpoint, E1–E12, "21 of 21 checks equal". Among them are the
  seconds and stage durations (E3), the looks' contrast columns (E2), the gate stages' later picks and exclusion
  details (E5, E11), and secondary (e) over the domain alone (E12). The entry records them as "an addition to block
  §4's list that carries no figure of record", and E3's split and E12 as "Code's additions: post-hoc". m:358 names no
  Code extraction.
- **Readings:**
  - **(a)** No Code read of p's checkpoints. The entries carry the analyzer's two outputs and the reports' content
    only, and Q3 falls to (c) or (d).
  - **(b)** The list of record's per-unit rule. After a unit's analyzer output exists, Code's step reads that unit's
    released checkpoints, by path, never listing `data/p/ckpt`, for the counts the record names (Q3), and nothing
    beyond them.
  - **(c)** (b), and extractions in Q-F0's classes as Code's precedent, each labeled post-hoc where it is.
  - **(d)** Another form.

**What Q4 stops:** the entries' contents beyond the analyzer's outputs and the reports, not the outputs.

## 5. Readings (declared, not applied)

- **Q1.**
  - (c), for the instruct session. PIN-35 makes the input m:318's record, so the decisions whose kinds m:318 names
    ((i), (ii)) and the one ADDENDUM-p1 asks for in m:318's form ((iii)) belong in it. m's precedent, which the seat
    specified, put in the input the PI's go for the run its records report, and the campaigns' go is that go here. The
    other goes and the decisions of other kinds would be recorded in each entry's text, in m:318's form. Each unit's
    input would then be §2's two items and (c)'s four, identical but for `unit`, at
    `data/p/verdicts/OLMo-{ckpt}_decisions.json`.
  - (c), for the sft session, in its message, on the same two grounds.
  - (a), for the dpo session, in its note: the two items in the file, and the cap share, the placement and (p-1) "in
    the VERDICTS **entry** in m:318's form".
- **Q2.**
  - (a), for the instruct session.
  - For the dpo session, in its message: "the run order follows the windows and is not a decision about a unit". Its
    note, written before any sibling VERDICTS existed, gives no sibling item.
  - The sft session gave no reading on Q2.
- **Q3:** (a), for the instruct session. It is the form the seat ruled for `task_correct`, and p §2.3 names a tool
  "over the checkpoints".
- **Q4:** (b), for the instruct session. The list of record's per-unit "before its VERDICTS or NOT-RUN record" governs.
  The briefs' "Never open them yourself" binds before each unit's VERDICTS, and after it the record's own counts need
  the read. The extractions are Code's precedent, not owed. The briefs are the coordinating session's.
- **Under every reading,** each VERDICTS entry carries:
  - ADDENDUM-p1 §2.4's sentence;
  - p §5.4's disclosure (p:102: "Every p entry, lock, artifact and posted sentence that reports a p outcome states
    …");
  - for sft, `daca8b0` §0.1's sentence.
- Code applies none of the readings before the seat's answer is routed. The list is part of VERDICTS outputs written
  once, and Code adjudicates nothing (CLAUDE.md; WORKFLOW.md §4).

## 6. Not questions

- **The verdicts path** (each session's step 1; the instruct session's read of the code):
  - `p_analyze.py verdicts` never reaches `m_analyze.battery()`. Only `_selftest` calls it (`scripts/p_analyze.py:344`),
    and only `--selftest` (`:722`) and `ganl` (`:668`) reach `_selftest`.
  - It touches nothing under `data/mf3`. m's `run_verdicts`, for an OLMo unit, reads its named inputs (the lock, the
    decisions file and the three checkpoints), committed blobs through git, PROPOSAL-m, ADDENDUM-m1, CLAUDE.md and the
    analyzer. Q-F3's reader (`m_analyze.py:2249–2250`) is not reached, and `production_env()` with no unit adds no mf3
    module to the closure (`:1904–1911`). p's side reads, through git, PROPOSAL-p for D_p's check, the code of record
    and m's three NOT-RUN outputs; it reads the lock's text for p's names; and it copies `data/p/verdicts`.
- **The other arguments**, per unit, from the record:
  - `--lock LOCK-p-OLMo-{ckpt}.md` (v1.0, `038bf3e`). Each sha256, re-hashed here, equals the `lock_sha256` the
    campaigns' precheck printed (`41bfab4`'s entry: sft `fafb786d…`, dpo `25c52f56…`, instruct `f71c97c1…`).
  - `--campaign`, `--time` and `--qual`: `data/p/ckpt/OLMo-{ckpt}_{campaign,time,qual}.json`, as the campaign entry
    (`41bfab4`), the G-TIME-OLMo (p) ×3 entry (`2258c52`) and the G-F0m-OLMo (p) ×3 entry (`a225a89`) name them. They
    are also `p_analyze`'s defaults (`scripts/p_analyze.py:180–181`).
  - No `--adjudication`, since no campaign paused (each m report's `pauses` is empty, `41bfab4`'s entry), and no
    `--pi-stop`.
- **The input's home:** `data/p/verdicts/OLMo-{ckpt}_decisions.json`, in Q-F0's input style (`{U}_decisions.json`; the
  `PROPOSAL-m OLMo-{ckpt} — NOT-RUN` entry gives the reason). `.gitignore`'s `!/data/p/verdicts/*.json` admits it, and
  it is committed with the outputs, as Q-F0's was (`bfc179c`).
- **The runs:** one `verdicts` invocation per unit, at `nice -n 19`, each in a battery window the coordinating session
  grants, after the answer is routed.

## 7. Questions

- **Q1.** The decisions Q6's list does not name (the cap share, the locks' placement, (p-1), the PI's goes): (a), (b),
  (c), (d), or another form? Stops the three runs.
- **Q2.** A sibling p unit's outcome: (a) or (b), with procedure (i), (ii), both or neither, or another form? Stops the
  three runs and their order.
- **Q3.** p §2.3's withheld counters and the contrast sessions' `task_correct` at VERDICTS: (a), (b), (c), (d), or
  another form? Stops the entries' counters.
- **Q4.** The read rule after a unit's VERDICTS: (a), (b), (c), or another form? Stops the entries' contents beyond the
  outputs and the reports.
