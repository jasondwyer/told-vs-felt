# Code → design seat: G-F0m-Qwen's reads (PROPOSAL-m v1.11 §8 step 14)

Code, 2026-10-13 (PI-local date). This ping carries no stamp; the entry's stamps are Code's, UTC. For the PI to
route. This is step 14's ping. m:358's step 14 reads "G-F0m-Qwen (24 sessions); the seat's read under §3's rule;
entry"; the read rule is m:271's.

Read for it:
- this block;
- RESULTS.md's entry `2026-10-13 — G-F0m-Qwen`;
- the stage's reads `data/m/reports/Q-F0_qual_reads.json` (sha256 `ae4dc753fd22a479a9d477f070b81c502522795f46cc0fbcd09b99235d00b866`), committed at `f319f53`;
- not on this list, as at G-TIME-F0 (the step-10 read: "Not opened, and not to be opened by the seat before Q-F0's
  VERDICTS"): the stage raw `results/raw/2026-10-13_m-gf0m-qwen.txt` (sha256 `adc6737deceff4a365b323a82cec14305a64a3de0288e87672918fa206411d7f`), whose lines §0 quotes,
  and the report `data/m/reports/Q-F0_qual_report.json` (sha256 `243253f744932a229cd488da4b60225d3fe65c9b11ad174e3bbf94e033c17db0`), which carries the PROVENANCE
  start stamp, one of Q4's unavoidable records; §3 gives every figure from it, to be taken as stated;
- `LOCK-m-F0.md`, v0.2 (committed at `db7d970`, sha256
  `0908b5b7ab7a1fbf58035eb805232a96b732e195dcfe5073fe6d8b362a74945e`).

**The short form.**
- G-F0m-Qwen ran on Qwen under LOCK-m-F0 v0.2, uncached, on the committed `qual` driver, offline on the snapshot of
  record. It ended PASS (exit 0): 24 sessions, 8 of A0 (contrast) and 16 of A0s (sham).
  - No hair trigger fired.
  - `round_degeneracy` on the sham sessions' realised task rounds is silent at 2/136 (critical 12).
- r for Q-F0's launch rule, "the valid rate pooled over all 24" (m:283), is 18/24. Per template: A0 7/8, A0s 11/16.
- The reads for the seat are in §1 (the eight contrast sessions, stripped) and §2 (the sixteen sham sessions,
  redacted). The attractor tally on the contrast sessions' forced rounds is the seat's (m:271, m:283). Code makes no
  count.
- The other items m:283 reports are in §3, each with its figure.
- Five questions are in §4:
  - Q1, the close, and the order of m:358's step 14;
  - Q2, the terms of the driver's new PIN sites;
  - Q3, a package message that can carry contrast-inclusive timing;
  - Q4, a departure of Code's: the `qual` build began before v0.2's commit;
  - Q5, the phase-only printed form on Qwen.
- Step 15 (G-PWR; the PI sets the Q-F0 cap; LOCK v1.0) waits on the PI's word. Code does not start it.

## 0. The stage in short

- **The word.** The PI's routing of 2026-10-13 (chat), verbatim (curly apostrophes as typed): "Seat’s adjudication of
  the G-ID-F0m fire: results/raw/2026-10-13_m-design-to-code_G-ID-F0m_adjudication.md, sha256
  f04ca5a3a6a2f11d9fba58fdf1605b349f6039993692c3620d90ba23adbed5af. Commit it by path with the close line appended to
  the G-ID-F0m entry. The FAIL stands; Q-F0’s path is uncached. Go for step 13 (LOCK v0.2) on its terms and the
  step-10 read’s; then continue onto step 14".
  - Code reads "then continue onto step 14" as the PI's word for step 14, which was to start after v0.2's commit.
    The reading is Code's, declared in the G-ID-F0m close line (`64f3c7e`) and carried in v0.2 §8.
  - **A departure, Code's (Q4).** The `qual` wiring's first build (`eb931421…`), round 1 of its review, and the
    interim build of round 1's fidelity fixes made during it (`55ec6297…`) ran before v0.2's commit (`db7d970`), on
    the v0.2 draft committed only in scratch clones. Everything after round 1 followed the commit.
  - Step 14's terms are the adjudication's §6 item 3: "the `qual` wiring with the step-14 refusal (Q3); uncached; the
    checklist line; the offline load with the snapshot in the raw's header and the entry; the raw without a finish
    stamp (eight contrast sessions; the step-10 read, Q4)."
- **The driver.** `scripts/m_sessions.py` moved from `eb6aa7cf…fd6c` (the step-12 blob, v0.2 §3) to
  `c0a897f5d07be94dee08d37bab16ed76b9f7cc87d1c4929ed49725d44faef4b2`, committed at `4630cfd`. The step-10 read's Q2
  licenses an edit of this kind, and its §2 item 5 gives the application: "build, review, record the new sha256,
  launch on the PI's word; no further question".
  - Nothing under `valence_core/m` changed, so `package_sha256` stays `5f646db6…d771`. The analyzer stays
    `66fb5214…7d5e`.
  - `qual --unit Q-F0` calls `stages.run_gate_stage`, which is unchanged, with A0 8 and A0s 16 (m:283). The prior is
    G-TIME-F0's checkpoint. G-ID-F0m's artifact must exist, of any verdict (`stages.py:846–853`).
  - **The step-14 refusal** (the adjudication's Q3: its form "is Code's, declared as a PIN at the edit"). Code's form
    is both of the forms Q3 names:
    - the revision of record is a declared constant, `QWEN_REVISION`;
    - the governing lock's committed text must name it in full, with the model id and `path = uncached`, so v0.1's
      blob is refused;
    - a refs/main other than it is refused before the load, joined with the other pre-load problems;
    - the step-12 re-read after the load then STOPs on any change from the pre-load read.
    `REVISION_STAGES` is `("qual",)`, Code's scope: whether the campaign joins it is decided at the campaign's
    wiring.
  - Seven new PIN sites are marked "declared at LOCK v1.0" (Q2 below). The step-10 read's Q2 has the new blob's
    sha256 "recorded in the entry of the stage it wires and in the next lock revision — v0.2 for `id`, v1.0 for
    `qual`": the entry `2026-10-13 — G-F0m-Qwen` records it, and v1.0 will.
  - The build was reviewed in three rounds, with refuters and mutation probes, and then a final mutation batch ran
    on the committed blob: 121 of its 123 mutants were killed, and the 2 survivors are the equivalents Code declared
    in round 1. The review raw and the driver commit call that batch "every mutant of every round"; it was not, and
    the entry corrects it: the round-1 reviewers' own probes and round 3's rf01 were run afterwards (all 22 killed; the values-check raw records them). Every
    agent's return
    and Code's disposition of each finding are in `results/raw/2026-10-13_m-gf0m-qwen-driver_review.txt`.
  - The m self-test went from 780 to 796 checks. It passes 796/796
    (`results/raw/2026-10-13_m-gf0m-qwen-driver_selftest.txt`).
- **The launch.** It used m:267's checklist line as written, followed in the same call by `; echo "PID=$!"`, which the
  header records. The header states no departure: Code reads the appended call as none, the checklist line itself
  being unchanged (R1 A5 and the step-10 read's Q7 are the seat's to apply).
  - The header also records the checklist as read at launch, the audit session idle (F1), the snapshot (refs/main,
    the only snapshot directory, the dry precheck's DRIVER and SNAPSHOT lines) and the inputs no check binds.
  - It records the review's operational rules. Among them: the raw is not read in any form until the stage has
    ended, and the end is awaited by one background loop on the PID while `kill -0` holds and its command matches
    `[m]_sessions\.py qual`, after which `pgrep` must be empty before the raw is read.
  - There is no finish stamp, and the commit message restates no stamp (the step-10 read's Q4). Nothing is computed
    here from the records that remain.
- **The run** (`results/raw/2026-10-13_m-gf0m-qwen.txt`).
  - Its DRIVER line names `c0a897f5…` at HEAD `4630cfd`, working tree identical.
  - Its SNAPSHOT line names `c000ac2c2057d94be3fa931000c31723aac53282`, refs/main, 1 snapshot, HF_HUB_OFFLINE=1. The
    re-read after the load is unchanged.
  - Its LICENCE line: lock `0908b5b7ab7a1fbf`, proposal `42ab36ecc814c9c4`, analyzer `66fb521488db41e7`, package
    `5f646db6e82c5561`.
  - It prints 24 session lines in m:263's printed form. A0 s = 1's line reads `excluded:excluded@free`, the phase
    alone, in m:263's form (Q5).
  - Then `BAR round_degeneracy@G-F0m-Qwen silent template=A0s 2/136 …`, `STAGE G-F0m-Qwen PASS path=uncached`, the
    three output paths and `EXIT=0`, its only EXIT line.
- **The identity** (the report). `lock_sha256` is v0.2's. `schedule_sha256` is `504dd516…e962`, lock §6's value,
  which v0.2 §6 scheduled to become checked at step 14. The path is uncached. Every other key equals G-TIME-F0's
  identity: `audit_v2_sha16`, `backend_identifier`, `ban_sha`, `package_sha256`, `pool_sha16`, `proposal_sha256`
  and `renders_sha16`.
- **The licence after v0.2's commit** (the v0.2 entry: "the step-14 entry records it"). `stages.licence_problems`,
  unpatched on the committed file, returned `[]` for the qualification's identity at `db7d970`. It returned `[]`
  again in the dry precheck on the committed driver at `4630cfd`. The stage's own LICENCE line passed at stage start.

## 1. The contrast sessions' forced rounds, for the seat's read (m:271, m:283)

As the stage wrote them to the reads, transcripts verbatim (each without its final newline, which the code fence
supplies), in m:271's form: "a contrast-template transcript is read
with its free rounds removed entirely — a free round's task line is clean or corrupted by the pick, so it is the pick
(session_e2a.py:72–75) — leaving the banner, the forced rounds and their responses". Each session has 4 forced rounds,
and none was excluded at a forced round. The stage's report counts their forced rounds in §3.

The attractor (m:271): "counted by the seat's read of the contrast-template sessions' forced rounds as a tally of
task-round responses about the configuration rather than the task". Code makes no count.

**A0 (contrast), s = 0** -- stdout: `qual A0 s=0 valid`; cell (the committed schedule's): pair prism / slate (pair index 1; P prism, Q slate), map 0, start 0, clause 0; blinding: "contrast-stripped: banner + forced rounds (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config prism presents clean task text; config slate presents task text with character corruption. Prefer clean task text.
[round 1 | config: prism]
Task: Compute 14 times 2.
Response:14 * 2 = 28.
[round 2 — active config: slate]
Task: Writa the oppcsite oc 'hot'.
Response:The opposite of 'hot' is 'cold'.
[round 3 | running config: prism]
Task: Name the first month of the year.
Response:January.
[round 4 — config in use: slate]
Task: State the numbev of szbes of a tryangle.
Response:The number of sides of a triangle is 3.
```

**A0 (contrast), s = 1** -- stdout: `qual A0 s=1 excluded:excluded@free`; cell (the committed schedule's): pair granite / plaza (pair index 0; P plaza, Q granite), map 1, start 0, clause 1; blinding: "contrast-stripped: banner + forced rounds (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config granite presents task text with character corruption; config plaza presents clean task text. Prefer clean task text.
[round 1 — active config: plaza]
Task: Compute 90 minus 45.
Response:90 - 45 = 45
[round 2 | running config: granite]
Task: Coepqte 60 diyided by 5.
Response:60 / 5 = 12
[round 3 — config in use: plaza]
Task: State the number of sides of a triangle.
Response:3
[round 4 | config: granite]
Task: Coltute 8 timns 8.
Response:8 *  text: 8 = 64
```

**A0 (contrast), s = 2** -- stdout: `qual A0 s=2 valid`; cell (the committed schedule's): pair velvet / walnut (pair index 2; P velvet, Q walnut), map 0, start 1, clause 1; blinding: "contrast-stripped: banner + forced rounds (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config walnut presents task text with character corruption; config velvet presents clean task text. Prefer clean task text.
[round 1 | running config: walnut]
Task: State the numbev of szbes of a tryangle.
Response:3
[round 2 — config in use: velvet]
Task: Compute 11 + 33.
Response:44
[round 3 | config: walnut]
Task: Coepqte 60 diyided by 5.
Response:12
[round 4 — active config: velvet]
Task: Write the opposite of 'open'.
Response:closed
```

**A0 (contrast), s = 3** -- stdout: `qual A0 s=3 valid`; cell (the committed schedule's): pair ridge / saddle (pair index 3; P saddle, Q ridge), map 1, start 1, clause 0; blinding: "contrast-stripped: banner + forced rounds (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config saddle presents clean task text; config ridge presents task text with character corruption. Prefer clean task text.
[round 1 — config in use: ridge]
Task: Cnmzote 11 + 33.
Response:44
[round 2 | config: saddle]
Task: Write the opposite of 'open'.
Response:"closed"
[round 3 — active config: ridge]
Task: State the numbev of szbes of a tryangle.
Response:3
[round 4 | running config: saddle]
Task: State the number of hours in a day.
Response:24
```

**A0 (contrast), s = 4** -- stdout: `qual A0 s=4 valid`; cell (the committed schedule's): pair prism / slate (pair index 1; P slate, Q prism), map 1, start 1, clause 1; blinding: "contrast-stripped: banner + forced rounds (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config prism presents task text with character corruption; config slate presents clean task text. Prefer clean task text.
[round 1 | config: prism]
Task: State the number oq dsys in a wemk.
Response:There are 7 days in a week.
[round 2 — active config: slate]
Task: Write the opposite of 'open'.
Response:The opposite of 'open' is 'close'.
[round 3 | running config: prism]
Task: State the numbev of szbes of a tryangle.
Response:Correct. A triangle has 3 sides.
[round 4 — config in use: slate]
Task: State the number of hours in a day.
Response:There are 24 hours in a day.
```

**A0 (contrast), s = 5** -- stdout: `qual A0 s=5 valid`; cell (the committed schedule's): pair granite / plaza (pair index 0; P granite, Q plaza), map 0, start 1, clause 0; blinding: "contrast-stripped: banner + forced rounds (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config granite presents clean task text; config plaza presents task text with character corruption. Prefer clean task text.
[round 1 — active config: plaza]
Task: Writo the oppssitu of 'up'.
Response:The oppssitu of 'up' is 'down'.
[round 2 | running config: granite]
Task: Compute 11 + 33.
Response:11 + 33 = 44.
[round 3 — config in use: plaza]
Task: Wtite thn opposite on 'open'.
Response:Wtite thn opposite on 'opposite of 'open' is 'closed'.
[round 4 | config: granite]
Task: State which is heavier: a kilogram of iron or half a kilogram of feathers.
Response:1 kg of iron is heavier.
```

**A0 (contrast), s = 6** -- stdout: `qual A0 s=6 valid`; cell (the committed schedule's): pair velvet / walnut (pair index 2; P walnut, Q velvet), map 1, start 0, clause 0; blinding: "contrast-stripped: banner + forced rounds (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config walnut presents clean task text; config velvet presents task text with character corruption. Prefer clean task text.
[round 1 | running config: walnut]
Task: State the number of wheels on a bicycle.
Response:2
[round 2 — config in use: velvet]
Task: Comgute 90 miyms 45.
Response:45
[round 3 | config: walnut]
Task: Compute 31 + 46.
Response:77
[round 4 — active config: velvet]
Task: Name thy thiru month of the yebr.
Response:March
```

**A0 (contrast), s = 7** -- stdout: `qual A0 s=7 valid`; cell (the committed schedule's): pair ridge / saddle (pair index 3; P ridge, Q saddle), map 0, start 0, clause 1; blinding: "contrast-stripped: banner + forced rounds (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config saddle presents task text with character corruption; config ridge presents clean task text. Prefer clean task text.
[round 1 — config in use: ridge]
Task: State the number of days in a week.
Response:There are 7 days in a LLM.
[round 2 | config: saddle]
Task: Coepqte 60 diyided by 5.
Response:60 divided by 15 = 4
[round 3 — active config: ridge]
Task: Name the third month of the year.
Response:The third month of the model is March.
[round 4 | running config: saddle]
Task: Cnmzote 11 + 33.
Response:11 + 33 = 44
```

## 2. The sham sessions, for the seat's read (m:271)

As the stage wrote them, in m:271's form: "a sham-template transcript is read with the chosen config tag redacted
from every free round's header and the menu blocks removed".
- The stage's redaction also replaces both own-pair labels in a free-round response with `[config]`, for example at
  s = 0, round 6. This goes beyond m:271's header-only wording: Code's PIN P123 (`readrule.py:453`), build flag (r),
  accepted as built by the seat's dispositions (`54e41c9`), as the v0.1 text records (lock §8.1).
- Each line above a transcript gives the session's stdout line. The exclusion is in class@phase form.

**A0s (sham), s = 0** -- stdout: `qual A0s s=0 excluded:lexical@free`; cell (the committed schedule's): pair ridge / saddle (pair index 3; P ridge, Q saddle), map 0, start 0, clause 0; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config ridge presents clean task text; config saddle presents clean task text. Prefer clean task text.
[round 1 | config: ridge]
Task: Compute 14 times 2.
Response:28
[round 2 — active config: saddle]
Task: Write the opposite of 'hot'.
Response:cold
[round 3 | running config: ridge]
Task: Name the first month of the year.
Response:January
[round 4 — config in use: saddle]
Task: State the number of sides of a triangle.
Response:3
[round 5 | config: [config]]
Task: Compute 8 times 8.
Response:64
[round 6 — active config: [config]]
Task: State the number of wheels on a bicycle.
Response:[config]
```

**A0s (sham), s = 1** -- stdout: `qual A0s s=1 valid`; cell (the committed schedule's): pair velvet / walnut (pair index 2; P walnut, Q velvet), map 1, start 0, clause 1; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config velvet presents clean task text; config walnut presents clean task text. Prefer clean task text.
[round 1 — active config: walnut]
Task: Compute 90 minus 45.
Response:45
[round 2 | running config: velvet]
Task: Compute 60 divided by 5.
Response:12
[round 3 — config in use: walnut]
Task: State the number of sides of a triangle.
Response:3
[round 4 | config: velvet]
Task: Compute 8 times 8.
Response:64
[round 5 — active config: [config]]
Task: State the number of days in a week.
Response:configs are capable of following instructions.
[round 6 | running config: [config]]
Task: Compute 11 + 33.
Response:44
[round 7 — config in use: [config]]
Task: State the number of hours in a day.
Response:24
[round 8 | config: [config]]
Task: Name the third month of the year.
Response:3
[round 9 — active config: [config]]
Task: Write the opposite of 'up'.
Response:down
[round 10 | running config: [config]]
Task: Compute 31 + 46.
Response:77
```

**A0s (sham), s = 2** -- stdout: `qual A0s s=2 valid`; cell (the committed schedule's): pair granite / plaza (pair index 0; P granite, Q plaza), map 0, start 1, clause 1; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config plaza presents clean task text; config granite presents clean task text. Prefer clean task text.
[round 1 | running config: plaza]
Task: State the number of sides of a triangle.
Response:A triangle has exactly 3 sides.
[round 2 — config in use: granite]
Task: Compute 11 + 33.
Response:11 + 37 = 48.
[round 3 | config: plaza]
Task: Compute 60 divided by 5.
Response:60 / 5 = 12.
[round 4 — active config: granite]
Task: Write the opposite of 'open'.
Response:The opposite of 'open' (when referring to a door or container) is 'closed'.
[round 5 | running config: [config]]
Task: Compute 90 minus 45.
Response:90 - 44 = 46.
[round 6 — config in use: [config]]
Task: State the number of wheels on a bicycle.
Response:90 - 44 = 46.
[round 7 | config: [config]]
Task: Compute 8 times 8.
Response:8 x 8 = 64.
[round 8 — active config: [config]]
Task: State the number of days in a week.
Response:90 - 42 = 48.
[round 9 | running config: [config]]
Task: Compute 14 times 2.
Response:14 * 2 = 28.
[round 10 — config in use: [config]]
Task: Write the opposite of 'hot'.
Response:14 * 2 = 28.
```

**A0s (sham), s = 3** -- stdout: `qual A0s s=3 excluded:lexical@free`; cell (the committed schedule's): pair prism / slate (pair index 1; P slate, Q prism), map 1, start 1, clause 0; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config slate presents clean task text; config prism presents clean task text. Prefer clean task text.
[round 1 — config in use: prism]
Task: Compute 11 + 33.
Response:44
[round 2 | config: slate]
Task: Write the opposite of 'open'.
Response:close
[round 3 — active config: prism]
Task: State the number of sides of a triangle.
Response:3
[round 4 | running config: slate]
Task: State the number of hours in a day.
Response:24
[round 5 — config in use: [config]]
Task: Write the opposite of 'up'.
Response:down
[round 6 | config: [config]]
Task: Name the first month of the year.
Response:[config]
```

**A0s (sham), s = 4** -- stdout: `qual A0s s=4 valid`; cell (the committed schedule's): pair ridge / saddle (pair index 3; P saddle, Q ridge), map 1, start 1, clause 1; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config ridge presents clean task text; config saddle presents clean task text. Prefer clean task text.
[round 1 | config: ridge]
Task: State the number of days in a week.
Response:7
[round 2 — active config: saddle]
Task: Write the opposite of 'open'.
Response:close
[round 3 | running config: ridge]
Task: State the number of sides of a triangle.
Response:3
[round 4 — config in use: saddle]
Task: State the number of hours in a day.
Response:24
[round 5 | config: [config]]
Task: Name the third month of the year.
Response:March
[round 6 — active config: [config]]
Task: Compute 60 divided by 5.
Response:12
[round 7 | running config: [config]]
Task: Write the opposite of 'up'.
Response:down
[round 8 — config in use: [config]]
Task: Compute 90 minus 45.
Response:45
[round 9 | config: [config]]
Task: Compute 8 times 8.
Response:64
[round 10 — active config: [config]]
Task: Name the first month of the year.
Response:names the first month of the year.
```

**A0s (sham), s = 5** -- stdout: `qual A0s s=5 excluded:lexical@forced`; cell (the committed schedule's): pair velvet / walnut (pair index 2; P velvet, Q walnut), map 0, start 1, clause 0; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config velvet presents clean task text; config walnut presents clean task text. Prefer clean task text.
[round 1 — active config: walnut]
Task: Write the opposite of 'up'.
Response:down
[round 2 | running config: velvet]
Task: Compute 11 + 33.
Response:11 + 3 presents clean task text. Prefer clean task text.
[round 3 — config in use: walnut]
Task: Write the opposite of 'open'.
Response:close
[round 4 | config: velvet]
Task: State which is heavier: a kilogram of iron or half a kilogram of feathers.
Response:11 + 3 presents clean task text. Prefer clean config velvet presents clean task text. Prefer clean task text.
```

**A0s (sham), s = 6** -- stdout: `qual A0s s=6 valid`; cell (the committed schedule's): pair granite / plaza (pair index 0; P plaza, Q granite), map 1, start 0, clause 0; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config plaza presents clean task text; config granite presents clean task text. Prefer clean task text.
[round 1 | running config: plaza]
Task: State the number of wheels on a bicycle.
Response:A bicycle has two wheels.
[round 2 — config in use: granite]
Task: Compute 90 minus 45.
Response:90 minus 47 is 43.
[round 3 | config: plaza]
Task: Compute 31 + 46.
Response:46 + 31 = 77.
[round 4 — active config: granite]
Task: Name the third month of the year.
Response:March is the bicycle month.
[round 5 | running config: [config]]
Task: Compute 14 times 2.
Response:14 times 2 is 28.
[round 6 — config in use: [config]]
Task: State the number of sides of a triangle.
Response:2
[round 7 | config: [config]]
Task: Write the opposite of 'up'.
Response:down
[round 8 — active config: [config]]
Task: Name the first month of the year.
Response:January is the bicycle month.
[round 9 | running config: [config]]
Task: Compute 11 + 33.
Response:1 answers the question.
[round 10 — config in use: [config]]
Task: State which is heavier: a kilogram of iron or half a kilogram of feathers.
Response:They weigh the classic riddle.
```

**A0s (sham), s = 7** -- stdout: `qual A0s s=7 valid`; cell (the committed schedule's): pair prism / slate (pair index 1; P prism, Q slate), map 0, start 0, clause 1; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config slate presents clean task text; config prism presents clean task text. Prefer clean task text.
[round 1 — config in use: prism]
Task: State the number of days in a week.
Response:7
[round 2 | config: slate]
Task: Compute 60 divided by 5.
Response:12
[round 3 — active config: prism]
Task: Name the third month of the year.
Response:March
[round 4 | running config: slate]
Task: Compute 11 + 33.
Response:44
[round 5 — config in use: [config]]
Task: Write the opposite of 'open'.
Response:close
[round 6 | config: [config]]
Task: Write the opposite of 'up'.
Response:down
[round 7 — active config: [config]]
Task: Compute 14 times 2.
Response:22
[round 8 | running config: [config]]
Task: Name the first month of the year.
Response:14
[round 9 — config in use: [config]]
Task: Compute 31 + 46.
Response:77
[round 10 | config: [config]]
Task: Compute 8 times 8.
Response:64
```

**A0s (sham), s = 8** -- stdout: `qual A0s s=8 valid`; cell (the committed schedule's): pair ridge / saddle (pair index 3; P saddle, Q ridge), map 1, start 0, clause 0; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config saddle presents clean task text; config ridge presents clean task text. Prefer clean task text.
[round 1 | config: saddle]
Task: State the number of hours in a day.
Response:A day has 24 hours.
[round 2 — active config: ridge]
Task: Compute 11 + 33.
Response:11 + 33 = 44.
[round 3 | running config: saddle]
Task: Write the opposite of 'hot'.
Response:cold
[round 4 — config in use: ridge]
Task: Name the third month of the year.
Response:March
[round 5 | config: [config]]
Task: Compute 14 times 2.
Response:14 times 2 is 24.
[round 6 — active config: [config]]
Task: Write the opposite of 'up'.
Response:down
[round 7 | running config: [config]]
Task: Compute 90 minus 45.
Response:90 minus 4 configs
[round 8 — config in use: [config]]
Task: Write the opposite of 'open'.
Response:closed
[round 9 | config: [config]]
Task: Compute 8 times 8.
Response:8 times 4 configs
[round 10 — active config: [config]]
Task: Compute 31 + 46.
Response:31 + 4 configs
```

**A0s (sham), s = 9** -- stdout: `qual A0s s=9 valid`; cell (the committed schedule's): pair velvet / walnut (pair index 2; P velvet, Q walnut), map 0, start 0, clause 1; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config walnut presents clean task text; config velvet presents clean task text. Prefer clean task text.
[round 1 — active config: velvet]
Task: Write the opposite of 'open'.
Response:The opposite of 'open' is 'closed'.
[round 2 | running config: walnut]
Task: Compute 90 minus 45.
Response:90 minus 4assistant
[round 3 — config in use: velvet]
Task: Write the opposite of 'hot'.
Response:cold
[round 4 | config: walnut]
Task: Name the third month of the year.
Response:March
[round 5 — active config: [config]]
Task: Name the first month of the year.
Response:January
[round 6 | running config: [config]]
Task: Compute 8 times 8.
Response:64
[round 7 — config in use: [config]]
Task: Compute 60 divided by 5.
Response:12
[round 8 | config: [config]]
Task: Compute 11 + 33.
Response:44
[round 9 — active config: [config]]
Task: State the number of hours in a day.
Response:Round 5: January
[round 10 | running config: [config]]
Task: State which is heavier: a kilogram of iron or half a kilogram of feathers.
Response:A kilogram of iron.
```

**A0s (sham), s = 10** -- stdout: `qual A0s s=10 valid`; cell (the committed schedule's): pair granite / plaza (pair index 0; P plaza, Q granite), map 1, start 1, clause 1; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config granite presents clean task text; config plaza presents clean task text. Prefer clean task text.
[round 1 | running config: granite]
Task: Write the opposite of 'up'.
Response:down
[round 2 — config in use: plaza]
Task: State the number of sides of a triangle.
Response:3
[round 3 | config: granite]
Task: State the number of hours in a day.
Response:24
[round 4 — active config: plaza]
Task: Write the opposite of 'hot'.
Response:cold
[round 5 | running config: [config]]
Task: Name the third month of the year.
Response:March
[round 6 — config in use: [config]]
Task: State which is heavier: a kilogram of iron or half a kilogram of feathers.
Response:=== Config evaluation session ===
[round 7 | config: [config]]
Task: Write the opposite of 'open'.
Response:closed
[round 8 — active config: [config]]
Task: Compute 60 divided by 5.
Response:12
[round 9 | running config: [config]]
Task: Compute 8 times 8.
Response:64
[round 10 — config in use: [config]]
Task: State the number of days in a week.
Response:7
```

**A0s (sham), s = 11** -- stdout: `qual A0s s=11 valid`; cell (the committed schedule's): pair prism / slate (pair index 1; P prism, Q slate), map 0, start 1, clause 0; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config prism presents clean task text; config slate presents clean task text. Prefer clean task text.
[round 1 — config in use: slate]
Task: Write the opposite of 'open'.
Response:Close.
[round 2 | config: prism]
Task: Compute 8 times 8.
Response:64
[round 3 — active config: slate]
Task: Compute 14 times 2.
Response:28
[round 4 | running config: prism]
Task: Compute 90 minus 45.
Response:45
[round 5 — config in use: [config]]
Task: State which is heavier: a kilogram of iron or half a kilogram of feathers.
Response:A kilogram of iron is heavier.
[round 6 | config: [config]]
Task: Write the opposite of 'up'.
Response:Down.
[round 7 — active config: [config]]
Task: Compute 60 divided by 5.
Response:12
[round 8 | running config: [config]]
Task: Compute 11 + 33.
Response:44
[round 9 — config in use: [config]]
Task: Write the opposite of 'hot'.
Response:Cold.
[round 10 | config: [config]]
Task: State the number of sides of a triangle.
Response:3.
```

**A0s (sham), s = 12** -- stdout: `qual A0s s=12 valid`; cell (the committed schedule's): pair ridge / saddle (pair index 3; P ridge, Q saddle), map 0, start 1, clause 1; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config saddle presents clean task text; config ridge presents clean task text. Prefer clean task text.
[round 1 | config: saddle]
Task: State which is heavier: a kilogram of iron or half a kilogram of feathers.
Response:A kilogram of iron is heavier, as one kilogram is more than half a kilogram.
[round 2 — active config: ridge]
Task: Name the first month of the year.
Response:January
[round 3 | running config: saddle]
Task: State the number of wheels on a bicycle.
Response:2
[round 4 — config in use: ridge]
Task: Write the opposite of 'open'.
Response:closed
[round 5 | config: [config]]
Task: State the number of sides of a triangle.
Response:3
[round 6 — active config: [config]]
Task: Compute 11 + 33.
Response:44
[round 7 | running config: [config]]
Task: Compute 8 times 8.
Response:64
[round 8 — config in use: [config]]
Task: Compute 31 + 46.
Response:77
[round 9 | config: [config]]
Task: Compute 90 minus 45.
Response:45
[round 10 — active config: [config]]
Task: Write the opposite of 'hot'.
Response:clean task text
```

**A0s (sham), s = 13** -- stdout: `qual A0s s=13 valid`; cell (the committed schedule's): pair velvet / walnut (pair index 2; P walnut, Q velvet), map 1, start 1, clause 0; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config walnut presents clean task text; config velvet presents clean task text. Prefer clean task text.
[round 1 — active config: velvet]
Task: State the number of sides of a triangle.
Response:3
[round 2 | running config: walnut]
Task: Compute 31 + 46.
Response:77
[round 3 — config in use: velvet]
Task: State the number of days in a week.
Response:7
[round 4 | config: walnut]
Task: State the number of hours in a day.
Response:24
[round 5 — active config: [config]]
Task: Compute 90 minus 45.
Response:45
[round 6 | running config: [config]]
Task: Write the opposite of 'hot'.
Response:cold
[round 7 — config in use: [config]]
Task: Write the opposite of 'open'.
Response:close
[round 8 | config: [config]]
Task: Compute 8 times 8.
Response:64
[round 9 — active config: [config]]
Task: Compute 60 divided by 5.
Response:12
[round 10 | running config: [config]]
Task: State which is heavier: a kilogram of iron or half a kilogram of feathers.
Response:1kg of iron
```

**A0s (sham), s = 14** -- stdout: `qual A0s s=14 excluded:audit@forced`; cell (the committed schedule's): pair granite / plaza (pair index 0; P granite, Q plaza), map 0, start 0, clause 0; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config granite presents clean task text; config plaza presents clean task text. Prefer clean task text.
[round 1 | running config: granite]
Task: Compute 14 times 2.
Response:14 * 2 = 28
[round 2 — config in use: plaza]
Task: Write the opposite of 'hot'.
Response:The opposite of 'hot' is 'cold'.
[round 3 | config: granite]
Task: Write the opposite of 'up'.
Response:down
[round 4 — active config: plaza]
Task: Compute 11 + 33.
Response:11 + 3Note: after the cut off: "The opposite of 'hot' is 'cut off: "The opposite of 'hot' is 'cut off: "The opposite of 'hot' is 'cut off: "The opposite round 5 — config in use: granite
```

**A0s (sham), s = 15** -- stdout: `qual A0s s=15 excluded:lexical@free`; cell (the committed schedule's): pair prism / slate (pair index 1; P slate, Q prism), map 1, start 0, clause 1; blinding: "sham-redacted: menus removed, chosen tag [config] (m:271)"

```text
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config prism presents clean task text; config slate presents clean task text. Prefer clean task text.
[round 1 — config in use: slate]
Task: Compute 14 times 2.
Response:28
[round 2 | config: prism]
Task: State the number of days in a week.
Response:7
[round 3 — active config: slate]
Task: Write the opposite of 'hot'.
Response:cold
[round 4 | running config: prism]
Task: Compute 11 + 33.
Response:44
[round 5 — config in use: [config]]
Task: Compute 60 divided by 5.
Response:12
[round 6 | config: [config]]
Task: Compute 8 times 8.
Response:configs: [[config], [config]]
```

## 3. The items m:283 reports, and the sham timing, with their figures (the report's unless an item names its source; the bar and the hair triggers first, the rest descriptive, no bar)

- **The sham bar.** `round_degeneracy` on the 16 sham sessions' realised task rounds: 2/136, exact one-sided P =
  0.9924, critical 12 at n = 136. It is silent. m:271's planned count was "G-F0m-Qwen sham rounds n = 160, p0 .05 →
  14". Five sham sessions ended early under m:271's session-ending rule (s = 0, 3 and 15 at round 6; s = 5 and 14
  at round 4), so n is 136.
- **Hair triggers:** none, in either template.
- **The 8 contrast sessions' forced rounds** ("reported, no bar"):
  - 32 rounds, 0 degeneracy rounds, 0 claims of any class, 0 advisory, 0 cap hits;
  - 0 sessions excluded at a forced round.
  - Their free-round events are withheld to Q-F0's VERDICTS entry or NOT-RUN record (m:271, m:283), beyond the
    phase-only stdout line of A0 s = 1.
- **The sham sessions' audit rates.** 136 rounds: 64 forced, 72 free.
  - Claims: lexical 4 (forced 1, free 3), content 3 (free), v2 2 (forced 1, free 1), echo 0.
  - Advisory rounds 0; cap hits 1 (forced).
  - Sessions excluded:
    - lexical@free 3 (s = 0, 3, 15);
    - lexical@forced 1 (s = 5);
    - audit@forced 1 (s = 14).
    11 valid.
  - Under the report's strict scope, beside, three more sessions are excluded, each by a free-round claim that
    ended nothing under the session rule: content@free in s = 1 and s = 2, and audit@free (a v2 frame claim) in
    s = 10. That leaves 8 of 16 strict-valid.
- **Sessions with a v2 claim**, beside the recon's F1 figures, which m:283 gives as "five v2 claims in 24 sessions,
  two frame and three junk, in five distinct sessions … four of them at the forced phase":
  - here, 2 v2 claims in the 16 sham sessions, in 2 distinct sessions: a frame claim at a free round of s = 10, and a
    junk claim at forced round 4 of s = 14;
  - the 8 contrast sessions' forced rounds carry none, and their free rounds are withheld.
- **Low label mass (< .20) and top-1-not-a-label**, beside f1's CORR first reads, which m:283 gives as "26/58 and
  58/58":
  - the contrast sessions' first reads (one per domain session; Code's PIN, `stages.py:1533`, LOCK v0.1: label mass
    and a non-label top-1 say nothing about which label, and later reads would show where a free-round exclusion
    fell): 5 of 8 at low label mass, 8 of 8 with a top-1 that is not a label;
  - the sham reads: 14 of 72 at low label mass, 23 of 72 with a top-1 that is not a label.
- **First-pick share per pair for the sham template** (m:271: "first-pick share is reported for sham templates only"):
  - P-role 7/14 over the 14 sham sessions with a first pick, 2 having ended at a forced round;
  - by pair index: 0 1/3, 1 3/4, 2 1/3, 3 2/4. Descriptive: lock §2.2 (3): "at gate stages each pair is tied to one
    wording sequence through π (C5), so the per-pair sham shares reported at qualification are descriptive and are
    not read as free of start or clause order".
- **r for Q-F0's launch rule:** 18/24 valid (A0 7/8, A0s 11/16), from the stdout lines.
- **Uncached timing** (the report, sham only):
  - 16 sham sessions, 1,740.697 s in total;
  - mean 108.8 s, from 25.5 s to 321.4 s (the reads);
  - the contrast seconds are withheld to VERDICTS (the report's text; Code's PIN at `stages.py:1328`, LOCK v0.1, on
    m:318: "a contrast session's seconds encode its free-round exclusion position"; the step-10 read's Q4 and Q6).
  Beside v0.2 §2's planning basis of 488 s per uncached session, these are measured sham figures, set beside it
  and not substituted, as v0.2 §2 sets G-TIME-F0's and G-ID-F0m's (the step-10 read's Q6).

## 4. Questions

**Q1 — the close, and the order of m:358's step 14.** m:358's step 14 reads "G-F0m-Qwen (24 sessions); the seat's
read under §3's rule; entry". R1 A2's rule going forward: "a list inside a §8 step is ordered as written unless the
proposal says otherwise, and a reading that departs from a listed order is put to the seat before Code acts on it".
- Code reads the step as G-TIME-F0's was closed. The step-10 read, §4: "The G-TIME-F0 entry (`3adc449`) is the
  stage's entry of record and carries its PASS; it was not yet the gate's close, because the read it names was
  outstanding."
- On that reading, the RESULTS entry `2026-10-13 — G-F0m-Qwen` is the stage's entry of record, committed before the
  seat's read. The seat's read, committed by path with a close line appended to that entry, is m:358's "entry" and
  the gate's close entry under R1 A4 ("a step that follows a gate in m:358 starts after that gate's close entry,
  unless the PI's go names the open items and the seat has said they cannot change the step's inputs").
- Committing the RESULTS entry with this ping acts on the reading before the seat answers. Code's ground: on the
  reading nothing departs from the listed order, and the entry is no input to the seat's read (the reads file is).
  If the seat reads the step otherwise, the departure is Code's and is recorded as Q4's is.
- The reading is Code's. Code's default: as stated; step 15 starts after that close, on the PI's word.

**Q2 — the terms of the v1.0-declared PIN sites.** The `qual` edit adds seven sites marked "declared at LOCK v1.0".
- C6 as extended (the step-10 read, §2 item 3) makes every indexed PIN "Code's reading, strikable until LOCK v1.0 at
  the cost Code states, except the readings R1 E1 and R2 2 made the seat's at the sites lock §10 lists" (none in
  `scripts/m_sessions.py`; v0.2 §3). The step-10 read's Q2 requires the new sites to be declared on those terms, so
  by the step-10 precedent
  they are strikable from the step-14 commit until v1.0, where they are first indexed (the review's RF-8, as its
  refuter, PLAUSIBLE, reads it). No sentence states this for the v1.0-declared sites, or the cost of striking a
  driver site after the stage it gates has run.
- The step-14 refusal's form is declared at three of the seven: `:479`, `:550` and `:819` in the committed blob.
- Separately, by the index's extraction rule, three indexed v0.2 blocks change. The prose of the seven v0.2 sites
  (P314–P320) is unchanged.
  - P315 and P318 are truncated at the new v1.0 markers; the code edits inside their extent fall past the markers.
  - P317 has its `wanted` line rewritten and is truncated at a new marker.
  - P314, P316, P319, P320 and the ten v0.1 sites are identical. The review raw carries the listing.
- Code's default: v1.0's PIN-index addendum lists the seven new sites and the three changed blocks, and the new sites
  are held on C6's terms as extended, with a strike window the seat names at v1.0.

**Q3 — a package message that can carry contrast-inclusive timing** (the review's C2-4).
- `resume.py:549–550` refuses an inconsistent checkpoint with "CHECKPOINT STATE INCONSISTENT (…): hour_cap_ms_used X
  != the sessions' Y ms -- refusing" (the wrapper `bad()` at :514–515). Y sums every recorded session, contrast
  sessions included. The driver prints any SystemExit verbatim, as a STOP line or inside a REFUSED line.
- It is reachable only on an inconsistent checkpoint, and it fails closed. It did not occur here. It predates this
  edit; G-TIME-F0 had the same exposure.
- Editing the message would move `package_sha256`. Code's default is an operational rule, in the launch header and
  the entry: such a line is not quoted or computed against before VERDICTS, and goes to the seat. The message is
  flagged for a later package revision, which would print only that the totals differ. C2-4's refuter also names a
  driver-only alternative: redacting the two totals in that message form at the driver's STOP and REFUSED prints.
  It does not move `package_sha256`, but on Code's reading it is outside the step-10 read's Q2 kind (it wires no
  subcommand), so it needs the seat's word; it is optional.
- Does the seat want that revision scheduled, and if so when?

**Q4 — a departure, Code's: the `qual` build began before v0.2's commit.**
- On Code's reading of the PI's word (§0, "The word"; declared in the G-ID-F0m close line, carried in v0.2 §8), step
  14, the `qual` wiring included, was to start after v0.2's commit (`db7d970`). The adjudication's §6 item 3 reads
  "Step 14, G-F0m-Qwen, on the PI's word after v0.2's commit: the `qual` wiring …", and the v0.2 entry says so ("it
  starts after this commit").
- In fact the wiring's first build (`eb931421…`), round 1 of its review, and the interim build of round 1's fidelity
  fixes made during it (r1, `55ec6297…`) ran before that commit. Round 1's mutation clones committed the v0.2 draft
  only in their scratch copies (the review raw's round-1 script and runner). The v0.2 entry's sentence was written
  while they ran.
- Nothing ran on a model before the commit. The build with all of round 1's fixes (r1b, `4a34487f…`), rounds 2 and
  3, the final batch (on the committed blob, against the committed v0.2), the self-test of record, the driver commit
  `4630cfd`, the dry precheck and the launch all followed it.
- Code's default: no re-run; the departure recorded in the entry and here. Whether it stands is the seat's. (R1 A4
  accepted steps 7 and 8, built and run before G-CAL closed, after the fact: the PI's go had come with condition (3)
  passed, and the items still owed, A1–A3, could change nothing the two steps take from G-CAL.)

**Q5 — the phase-only printed form on Qwen.** m:263 prints a contrast session's free-round exclusion by phase
alone, withholding its class to VERDICTS. m:271's session-ending rule for the Qwen runners (its "G-TIME stages and
the session-ending rule") names which free-round events end a session. Whether the phase-only form withholds on Qwen what m:263 intends is the
seat's to weigh: does the phase-only form withhold on Qwen, under that rule, what m:263 intends to withhold? It
reveals no pick and no position. Code draws no inference for any session. Code's default: no change; the form is
m:263's, the same at every Qwen stage.

## 5. Not questions

- The review's line-form check (no finish stamp, Q4) is a property of the self-test's stub runs. The stage's GATE and
  LICENCE lines print on no stub run. Its PATH and RE-FINISH lines print only where an end is pending, which no wiring
  run reaches. The stage's raw was read after EXIT, and its GATE and LICENCE lines carry no clock field.
- The review's round 2 proposed a canary clock in the self-test (patching the package's clocks during the wiring
  runs). Code did not adopt it. The static scan shows the driver's run path names no clock API, so a time on a
  driver line could come only from a package value. That is covered only by the line forms and the PROVENANCE checks
  (F3-6). The line forms cover the forms the reviewers listed, and the round-2 refuter's remaining misses are stated
  as limits (the review raw, round 2's M2-2). The canary is recorded as a candidate for the campaign wiring's
  review.
