# PROPOSAL-p -- the campaign wiring's BUILD entry: blind values-check

*Code's raw, PI date 2026-11-14. A blind values-check of the BUILD entry's draft and its two raws (the checks raw and the review raw). The checker worked against the uncommitted files at HEAD `3e1b614` (stage `3390a448…a406`, driver `9c641e19…a96d`), the seat's read, PROPOSAL-m, PROPOSAL-p, m's code, the coordinating session's relays verbatim, and Code's check outputs.*

*Totals: 105 claims; 89 CONFIRMED, 13 IMPRECISE, 0 FAIL, 3 NOT CHECKABLE (the values-check line left open in the draft; Code's own conduct; the future acts).*

*How the findings were applied:*
- *Each IMPRECISE item was applied in the checker's wording or close to it:*
  - *in the entry: rows 7, 30, 37, 43, 44, 50, 60, 64, 73, 81, 83 and 86;*
  - *in the checks raw: row 97, and row 81's scope in its section 4 title.*
- *O-1 is applied: the entry's declared item 8.*
- *O-2 is not applied.* A docstring line of 169 characters was left by the sweep's reflow. It is cosmetic, and the file carries other lines over 120 characters, as at HEAD; changing the stage's bytes would move p's package hash and re-run every check.
- *O-3 needs no change:* the checker's own conclusion, a historical record.
- *O-4 is applied:* round 3's dispositions now say "three new gap survivors".
- *The fixes were checked by tool, not by a second blind pass.*

*An earlier run of this values-check was stopped by Code before it reported, when Code's citation sweep began; its partial outputs were not used. Local paths are scrubbed (`<repo>`, `<tmp>`, `<harness>`).*

## Blind values-check: the campaign wiring's BUILD entry and its two raws

Checked: the draft entry (`CW/entry_build.md`), the checks raw (`CW/checks_raw.txt`, to become
`results/raw/2026-11-14_p-campaign-wiring_build_checks.txt`) and the review raw (`CW/review_raw.md`, to become
`results/raw/2026-11-14_p-campaign-wiring_build_review.md`). `CW` is the campaign wiring's scratch folder; `<repo>` the
main checkout at HEAD `3e1b614`, the two BUILD files uncommitted at `3390a448…a406` (stage) and `9c641e19…a96d`
(driver), both re-hashed by me.

### Totals

- **CONFIRMED: 89**
- **IMPRECISE: 13**
- **FAIL: 0**
- **NOT CHECKABLE: 3** (rows 5, 88, 90)
- 105 claims in all.

### Claims

| # | Claim (short) | Mark | Evidence | Accurate wording (IMPRECISE / FAIL) |
|---|---|---|---|---|
| **Entry: header and routing** |||||
| 1 | Header: on the seat's read, §4.3 item 2, routed by the PI 2026-11-13 at `a2c354e`; the PI's cap share of 2026-11-14 | CONFIRMED | `a2c354e`'s subject (git log): the seat's read committed by path on the PI's "Route as given" (2026-11-13); relays file: the cap-share relay is PI date 2026-11-14 | |
| 2 | Two files move, `valence_core/p/stage.py` and `scripts/p_sessions.py` | CONFIRMED | `git status --porcelain`: only these two ` M`; the 31 untracked entries are the snapshot's | |
| 3 | `campaign` and `campaign-report` wired; A0 96, A0s 64; 2 h at each checkpoint | CONFIRMED | driver argparse and dispatch; `stage.campaign_launch_counts(u)` = {A0-OLMo-u: 96, A0s-OLMo-u: 64}, `campaign_hour_cap(u)` = 2, for all three units (printed) | |
| 4 | (j)'s closure and the register unchanged | CONFIRMED | `register.py` and `fresh_import_closure` untouched by the diff; `stage.fresh_import_closure()` today: no problems, 14 files, equal to `data/p/gates/G-SHAPE-p.json`'s `provenance.import_closure` | |
| 5 | Nothing ran on a model or on the box | NOT CHECKABLE | Code's conduct. Every check in the raws is model-free by construction (stub, m's scripted double, stand-ins) | |
| 6 | §4.3 item 2 quoted verbatim | CONFIRMED | quote found byte for byte in the seat's file, line 45 (script `quotes_vc.py`) | |
| 7 | "verbatim from its second clause" | IMPRECISE | The quote begins right after the item's label and colon ("**The campaign wiring**, p's own move (…): its build may start now…"); the label has no verb, so the quote starts at the item's first clause | "verbatim from the words after its colon:" |
| 8 | The relay (PI date 2026-11-13), after `3e1b614`: the build may start now; "If any part of the wiring needs the cap's value, STOP at that point and tell me." | CONFIRMED | relays file, the 2026-11-13 RELAY: `3e1b614` among the verified; "the build may start now"; the quote byte for byte | |
| 9 | Code's STOP point, paraphrased: m's form (driver constants, lock line forms); §4.3 puts p's wiring before v1.0, so the cap is a BUILD value; (a) vs (b); (a) recommended | CONFIRMED | relays file, the STOP point (PI date 2026-11-13): each element present; faithful ("must carry their line forms as substrings"; "p's driver must carry each checkpoint's cap … before … its BUILD commit") | |
| 10 | Q-F0's line forms at `scripts/m_sessions.py:617–620` | CONFIRMED | lines 617 `CAMPAIGN_LAUNCH_COUNTS`, 618 `CAMPAIGN_HOUR_CAP = 40`, 619–620 `CAMPAIGN_LOCK_LINES` | |
| 11 | The ACK's two quotes, PI date 2026-11-13 | CONFIRMED | both byte for byte in the relays file's ACK | |
| 12 | The PI's word "2 h each", the question, the choices, the closing message's question; per checkpoint 2/2/2 | CONFIRMED | all five quotes byte for byte in the 2026-11-14 relay; "Per checkpoint, in hours: sft 2 h, dpo 2 h, instruct 2 h" | |
| **Entry: what moves, the stage** |||||
| 13 | `STAGES = GATES + ("campaign",)`; `GATES`, `COUNTS` unchanged | CONFIRMED | diff: `STAGES` added; `GATES`, `COUNTS` context lines only; printed `('time','qual','campaign')`, `{'time': (1, 1), 'qual': (8, 16)}` | |
| 14 | `run_gate` refuses the campaign before anything runs | CONFIRMED | its first statement raises `StageRefusal` for a gate not in `GATES`; the self-test case passes (my run) | |
| 15 | THE CAMPAIGN PIN; m's `run_campaign` under entries (1), (2), (6)–(9) | CONFIRMED | PIN in the module docstring; `ENTERED = (1, 2, 6, 7, 8, 9)`; the self-test asserts the campaign's run line `register_entered == ENTERED` | |
| 16 | The values passed as m's driver passes Q-F0's; m's script read as text, never imported | CONFIRMED | m: `launch_counts=dict(CAMPAIGN_LAUNCH_COUNTS), hour_cap=CAMPAIGN_HOUR_CAP` (m_sessions.py:1664); p: `launch_counts=campaign_launch_counts(unit), hour_cap=cap`; p imports no m script (the guard's import-set check passes) | |
| 17 | Launch counts per arm, contrast first: A0-OLMo-{ckpt} 96, A0s-OLMo-{ckpt} 64, G-PWR (p)'s of record | CONFIRMED | `CAMPAIGN_LAUNCH_COUNTS` (96, 64) ×3, keyed by `keys.templates` order; G-PWR record `units.*.launch.L` = {A0 96, A0s 64} ×3 | |
| 18 | `gpwr_problems` binds them to the committed blob, schema `p-gpwr-v1`, `launch.L` per arm | CONFIRMED | code (m's `_committed`, schema, L compare); record schema `p-gpwr-v1`; working-tree blob = `HEAD:` blob (`git rev-parse` = `git hash-object`); sha256 `bc2b0909…d604`; `gpwr_problems(u)` = ([], that sha) ×3 | |
| 19 | Floors: `schedule.FLOORS` for the OLMo arms, 80 and 32, as m's driver reads Q-F0's | CONFIRMED | `FLOORS['A0-OLMo'] = 80`, `['A0s-OLMo'] = 32`; m's `campaign_floors` reads `schedule.FLOORS` (m_sessions.py:654–658) | |
| 20 | Cap 2 at each unit; the PI's word and question quoted in the constant's comment | CONFIRMED | stage.py:177–184 | |
| 21 | `campaign_hour_cap`: positive finite int or float; a bool refused; anything else unset | CONFIRMED | `type(v) not in (int, float) or not math.isfinite(v) or v <= 0` → None | |
| 22 | An unset cap refused at the precheck and again before the load | CONFIRMED | precheck appends "the hour cap is not set"; `_run_campaign_locked` raises before the schedules check | |
| 23 | Non-stub precheck at `campaign`: the lock names G-PWR (p)'s sha256 beside `lock_required`'s values and carries the two lines as whole lines; the line texts | CONFIRMED | `req["G-PWR (p)'s record"] = gsha`, then `lock_names` over `req`; `campaign_lock_problems` (whole-line regex); printed lines `launch counts = A0-OLMo-u 96, A0s-OLMo-u 64`, `hour cap = 2 h` | |
| 24 | The prior: G-F0m-OLMo (p)'s checkpoint; m's `prior_gate` with `require_real` off the stub, then `proposal`, `proposal_p_sha256` | CONFIRMED | `prior_problems(…, stage="campaign")` on `out_paths(unit, out, gate="qual")["m_ckpt"]` | |
| 25 | The refusals before the load, in the order listed (nine bullets) | CONFIRMED | `_run_campaign_locked`'s statements in that order: report; marker; call log / m's checkpoint without `--resume`; checkpoint without log; unreadable log, stopped runs; no run line, consistency; unreadable / ended state; rulings; cap; schedules; prior | |
| 26 | `campaign_state` mirrors m's `_campaign_state` with the unit's arms | CONFIRMED | body diff against m's (by AST segment): only the arm set, `_sha` for `hashlib`, module aliases | |
| 27 | `campaign_ruling_problems`: m's driver's refusals in its words and order | CONFIRMED | body diff: identical messages (re-wrapped f-strings), identical order; m's PIN comment dropped | |
| 28 | The rulings pass to m's stage as texts | CONFIRMED | `call_m`: `adjudication=adjudication, pi_stop=pi_stop` | |
| 29 | The RULING line: each ruling's sha16 and the last pause, or the end pending, never a text | CONFIRMED | code (sha16 of the stripped text); a third form, "no pause recorded", is not mentioned | |
| 30 | It prints "after every refusal, just before the load" | IMPRECISE | It prints after every refusal in `_run_campaign_locked`, before `_run_recorded`; inside that, before the load, the STOP reservation can still refuse ("the STOP's record cannot be reserved", an I/O failure) and entering the substitutions can STOP | "after every refusal of the campaign's checks, just before the recorded run" |
| 31 | m's driver also prints its line before the load | CONFIRMED | m_sessions.py: `say_ruling()` before `_load_qwen()` / `adapter_factory()` | |
| 32 | `_run_recorded` extracted with m's call a parameter; round 1 found its body HEAD's but for `gate`→`stage` ×3 and the call | CONFIRMED | review hand-back r1, "What holds" 1; my diff (HEAD's `_run_gate_locked` from the gate line on vs the final): `_stopped_doc`, `_fill_cause`, the call, and a closing `return res`; the third site is `name = label(unit, stage)` | |
| 33 | After m returns, neither open nor ended is a StageStop that THE STOP records | CONFIRMED | the check is in `call_m`, called inside `_run_recorded`'s `try`; self-test case (marker written for absent and unreadable) passes | |
| 34 | A PAUSE: end line, nothing marked; a later run `--resume`: adjudication resumes, PI stop ends, neither is shown (m's R6) | CONFIRMED | code; self-test cases (end lines PAUSE, PAUSE, COMPLETE; PI-STOP) pass | |
| 35 | p's report `reports/{U}_campaign_p-report.json` at the end only (terminal or m's STOP, nothing pending); read domain; names m's report and excerpt | CONFIRMED | `out_paths`, `build_report` (`ended_status`, `pending_end`), `REPORT_TEXT["campaign"]`, `m_outputs` | |
| 36 | End look fired at a terminal end (m:330): PAUSE, terminal standing; `campaign_terminal`; run and `campaign-report` exit 3 as m's does | CONFIRMED | m's `_campaign_end` (status PAUSE, terminal stands); p's `build_report`; `EXIT_CODES["PAUSE"] = 3`; m:330 "A fired bar pauses" | |
| 37 | "The outputs take `_campaign_` names", m's checkpoint among them | IMPRECISE | m's checkpoint is `OLMo-{ckpt}_campaign.json` (printed); the other six carry `_campaign_` | "take `_campaign` names" (or name m's checkpoint `{U}_campaign.json`) |
| 38 | git admits the outputs, ignores locks and reservations; the self-test checks every name with `git check-ignore` | CONFIRMED | the self-test's case covers p's three outputs ×9, m's three campaign files ×3, the lexicon, the locks and `.reserve-1` ×9; passes (my run) | |
| **Entry: the driver** |||||
| 39 | `campaign --unit … [--resume] [--adjudication-file A] [--pi-stop-file P]`, `campaign-report --unit …` | CONFIRMED | argparse | |
| 40 | Before the load: ruling files → precheck at `campaign` → weights files → DRIVER and WEIGHTS lines → the stage | CONFIRMED | `run_campaign_stage` | |
| 41 | `stage.ruling_texts` under m's rule; texts never printed | CONFIRMED | body identical to m's `ruling_texts` (m_sessions.py:1467); refusals name the path only | |
| 42 | Exits: COMPLETE, CAP, PI-STOP 0; PAUSE 3; STOP 4; refusal 2; STOP on the way 4 | CONFIRMED | m's `EXIT_CODES`; `run_campaign_stage`'s returns | |
| 43 | The totals guard "covers every REFUSED and STOP line, `gate_report`'s included" | IMPRECISE | `_say` is used by `run_campaign_stage` and `gate_report` (all three report commands); `run_gate_stage` (time, qual) and `gcal` still print with plain `print` | "covers every REFUSED and STOP line of `campaign` and of the three report commands (`gate_report`'s)" |
| 44 | "`STAGE_NAMES` and `STAGE_CMDS` are removed; `GATE_CMDS` and `CAMPAIGN_CMD` replace them" | IMPRECISE | HEAD already had `GATE_CMDS = ("time", "qual")`, unchanged; `STAGE_WHEN` and `refusal()` are removed too; `CAMPAIGN_CMD` is the one new constant | "`STAGE_CMDS`, `STAGE_NAMES`, `STAGE_WHEN` and `refusal` are removed; `CAMPAIGN_CMD` joins the unchanged `GATE_CMDS`" |
| 45 | Unchanged: the rest of p's package, every m file, `olmo_hf.py`, `.gitignore`, the register's entries | CONFIRMED | `git status --porcelain`: no other tracked change | |
| 46 | No campaign has run: no `_campaign_` name under `data/p/ckpt` or `data/p/reports` | CONFIRMED | name-only `ls` of both, filtered for `campaign` in any case: 0 names (a broader test than `_campaign_`, which would miss `{U}_campaign.json`) | |
| **Entry: the gates' regression** |||||
| 47 | A stub `time` then `qual` on m's scripted double through HEAD's and the new stage, each loaded as `valence_core.p.stage`; five cases | CONFIRMED | `gates_regress.py`: pass, time_excl, time_stop, qual_excl, qual_stop | |
| 48 | Normalized outputs byte-identical | CONFIRMED | `regress_gates_head3.json` = `regress_gates_final3.json` = `b7a5ba4d…433a`; my own re-run, once per stage: both `b7a5ba4d…433a` | |
| 49 | What the comparison covers (events; identity, stage end, sessions and rounds' fields; p's report, marker, closing lines; names) | CONFIRMED | the script's `run_gate_case` and `run_case` | |
| 50 | "Only the outputs' sha256s are masked, since they hash m's wall-clock timings" | IMPRECISE | The masks fall on the digests of m's checkpoint, report, reads and p's call log, and the closing line's checkpoint digest. The call log's events carry no timing field and compare equal unmasked, so its digest is masked without needing it | "Only the outputs' sha256s are masked (m's checkpoint and report carry its wall-clock timings; the call log's digest is masked with them)" |
| 51 | p's package sha256 needs no mask: the same final package on disk in both runs | CONFIRMED | the run lines' and identity's `p_package_sha256` = `a38d93bb…` unmasked, equal in both | |
| **Entry: declared for the seat** |||||
| 52 | Sources: round 1's NOTE-3, NOTE-4 and NOTE-7 | CONFIRMED | NOTE-3 → item 4; NOTE-4 (a), (c), (d) → items 1–3, (b) → item 5; NOTE-7 → item 7. The split into "Code's PINs and two readings" is Code's own and not checkable | |
| 53 | m shows a paused campaign "with or without --resume" (its driver's PIN, m_sessions.py:1388–1389) | CONFIRMED | the quote is on line 1388; the PIN runs 1387–1390 | |
| 54 | m re-finishes a pending end whatever `resume` says (`stages.run_campaign`) | CONFIRMED | its docstring (stages.py:2012); `resume.load_or_init` | |
| 55 | p refuses a run without `--resume` once the call log exists, as at the gates | CONFIRMED | stage.py:1492 (campaign) and 1055 (gates); HEAD: 968 | |
| 56 | Lock lines whole lines; m's driver substrings; stricter, as at `qual` | CONFIRMED | m_sessions.py:964 (`x not in lock_text`); `qual_lock_problems` whole-line | |
| 57 | The report keeps the gates' read domain under ruling (h), m:318 | CONFIRMED | `REPORT_TEXT`; r1 NOTE-4 (d) | |
| 58 | No restart route: no checkpoint path to m; another pod's `--resume` meets CHECKPOINT MISMATCH (pod id) after the load, a STOP; m:302 "on the new box"; the PIN says so | CONFIRMED | `call_m` passes no `ckpt_path`; `load_or_init`: pod id in an OLMo campaign's identity, mismatch raises; m:302 contains "on the new box"; PIN text | |
| 59 | RULING line forms: p "{kind} at {n} launches, open/adjudicated"; m "for the pause at {n} launches ({kind})" | CONFIRMED | stage.py RULING code; m's `ruling_line` | |
| 60 | No "already records" note; such an adjudication is refused before the line (RULING REUSED, NO PAUSE TO ADJUDICATE or, beside an end pending, RULING BESIDE AN END PENDING) | IMPRECISE | No note in p, and every such case is refused before the line, but the list is not exhaustive: on an exhausted schedule's open pause SCHEDULE EXHAUSTED takes it first (probe: a recorded "R1" offered there → SCHEDULE EXHAUSTED), and an ended campaign is refused as ended | "is refused before the line (by RULING REUSED, NO PAUSE TO ADJUDICATE or SCHEDULE EXHAUSTED; beside an end pending, by RULING BESIDE AN END PENDING; on an ended campaign, as ended)" |
| 61 | The cap is an int or a float; m's `hour_cap_exceeded` also takes a text or a Fraction | CONFIRMED | `resume._q`: int, Fraction, float, str | |
| 62 | S3: the backend comparison never runs on the stub; predates this build | CONFIRMED | `_run_recorded`: `if not stub:` around the comparison; S3 "gap (predates change)" in r1 | |
| **Entry: item 8** |||||
| 63 | `git check-ignore` run two ways: r1, `-q` over 24 paths through a probe copy; the self-test's own case | CONFIRMED | r1 disclosures ("24 campaign paths"; NOTE-5: 18 outputs + 6 lock/reservation paths); the self-test case | |
| 64 | "It reads `.gitignore`'s rules for a name and prints whether the name is ignored" | IMPRECISE | Both runs use `-q`, which prints nothing; the answer is the exit status | "reports by its exit status (`-q`, both runs) whether the name is ignored, and prints nothing of a file" |
| 65 | No `_campaign_` file existed under those directories when it ran | CONFIRMED | none exists now (row 46); no campaign has run | |
| 66 | r1's `/usr/bin/grep -rn` over `valence_core/p/` and `scripts/`; roots cannot reach `data/`; matched a `.pyc` | CONFIRMED | r1 disclosures; pruned `find`: no symlink and no `data` directory under either root | |
| **Entry: licence and checks** |||||
| 67 | m files and `olmo_hf.py` unchanged | CONFIRMED | `git status --porcelain` | |
| 68 | `package_sha256` `a38d93bb…a2d7`, 14 files; the qual wiring's `08bfa693…fa26` | CONFIRMED | `guard.package_sha256()`; licence line "(14 files, …)"; `40086e8`'s entry: `08bfa693…7cfa26` | |
| 69 | Driver `9c641e19…a96d` | CONFIRMED | `guard.driver_sha256()` and `shasum` | |
| 70 | Checks model-free on base `3e1b614`; the raw's four contents; paths scrubbed | CONFIRMED | HEAD; the raw's sections; scan finds no absolute path | |
| 71 | `p_sessions.py --selftest` 204/204 (qual wiring 184/184) | CONFIRMED | my run: 204/204, output identical to the raw's §1 after scrubbing; `40086e8`'s entry 184/184 | |
| 72 | `p_analyze.py --selftest`: 525/525, all 538 coverage ids, then 14/14 | CONFIRMED | raw §2 = `p_analyze_selftest_final.txt` (scrubbed); stderr file empty; `rc=0`; 539 PASS lines, no FAIL (not re-run by me) | |
| 73 | Three blind rounds, "each brief quoting the list of record v2's items 1–5" | IMPRECISE | Round 1's brief quotes items 1–5 verbatim (the brief file equals the transcript's prompt; each item is in the committed list-of-record v2 answers). Rounds 2 and 3 were short continuations without the items: "The rules are round 1's: the list of record v2, items 1–5, as your brief quoted them." The review raw's header words it correctly | "round 1's brief quoting the list of record v2's items 1–5, rounds 2 and 3 binding them by reference" |
| 74 | Round 1: 1 MAJOR, 4 MINOR, 7 NOTEs; 48 mutants, 21 killed, 27 survived (4 equivalent, 23 gaps) | CONFIRMED | recount from the r1 hand-back's table and headings | |
| 75 | Round 2: no MAJOR, 3 MINOR, 4 NOTEs; 42, 30, 12 (5, 7) | CONFIRMED | recount (MINOR-A–C; NOTE-A–D) | |
| 76 | Round 3: no MAJOR, 1 MINOR (the m-STOP exit untested at both commands), 4 NOTEs; 18, 13, 5 (1, 4) | CONFIRMED | recount; r3 MINOR-1 text | |
| 77 | Round 3 found the cap of 2 reaches m as `hour_cap` per unit, the precheck needs `hour cap = 2 h` whole, nothing else assumes an unset cap | CONFIRMED | r3 "The three checks"; reviewer's `probe_capflow.json`: 2 (int) at each unit | |
| 78 | Every MAJOR and MINOR applied | CONFIRMED | dispositions; final code and tests (end-look PAUSE, `run_gate` refusal, caps, driver cases, refusal probe, RULING placement, m-STOP cases, report exits, m-STOP and COMPLETE recorder modes) | |
| 79 | Every NOTE applied or answered; the declared ones; r3 NOTE-2 equivalent; NOTE-4 at v1.0 | CONFIRMED | dispositions r1–r3 against the hand-backs | |
| 80 | Round 3's fixes (tests and one docstring) checked by tool, not by a fourth round | CONFIRMED | diff of the reviewer's r3 snapshots (`e81a25be…`, `f419091c…`) to the final files: tests, `campaign_hour_cap`'s docstring, and the sweep's text | |
| 81 | "round 3's three gap survivors … each now killed" | IMPRECISE | The kills hold: my harness runs on the re-derived mutants give N17 73/74, N22 18/19, N26 18/19, each failing the case named. But round 3 had four gap survivors (S3, N17, N22, N26), as row 76 says; the checks raw's §4 title ("Round 3's gap survivors") has the same scope | "round 3's three new gap survivors (N17, N22, N26)" |
| 82 | S3 survived every round; the gates' shared gap | CONFIRMED | r1–r3 tables | |
| 83 | The citation sweep "corrected the text in three places" | IMPRECISE | Three corrections at four sites (the cap's citation at two), plus a fourth change, the P'S REPORT reflow; the raw says "All four are text only" | "corrected the text in three ways, at four sites, and reflowed one docstring line" |
| 84 | m:251 is the pod-sessions paragraph; m:249 quoted; both sites | CONFIRMED | m:251 begins "**Pod sessions.**"; the quote is in m:249 byte for byte; stage.py:182 and :1130 cite m:249, and no `m:251` remains | |
| 85 | THE CAMPAIGN PIN's quote made byte-exact | CONFIRMED | both segments around "..." are in §4.3 item 2 byte for byte | |
| 86 | The driver docstring's list of the refusals before the RULING line "now complete" | IMPRECISE | It now names the cap and the schedules; the record refusals the stage makes first (p's report, the STOP marker, the call log's) are not in that list | "the driver docstring's list of the campaign's own refusals, now naming the cap and the schedules" |
| 87 | Every check re-run on the final files | CONFIRMED | every cited output is newer than both final files (`-nt`, no time printed); my re-runs reproduce §1, §3 and §4 | |
| 88 | The values-check line `{VC}` | NOT CHECKABLE | an open placeholder | |
| 89 | Next, in the relay's order: G-SHAPE-p (superseding `f5e695c`'s), G-ANL-p (`ba89279`'s), LOCK-p v1.0 ×3 (D_p 2026-12-15); the box waits for v1.0 ×3 and the PI's go | CONFIRMED | relay's "Your part" items 4–5; `f5e695c` and `ba89279` are the last commits of `G-SHAPE-p.json` and `G-ANL-p.json`; seat §4.3 item 3 for D_p | |
| 90 | Not pushed; committed by path; the three linked raw paths | NOT CHECKABLE | future acts. The links match the stated destinations, and no file of those names exists yet | |
| **Checks raw** |||||
| 91 | Header: base `3e1b614`, the two final sha256s, interpreter, scrub only | CONFIRMED | hashes recomputed; each section equals its source after the declared scrub | |
| 92 | §1: the self-test, 204/204 | CONFIRMED | equals `p_selftest_final.txt` and my run, both scrubbed | |
| 93 | §2: the analyzer self-test; stderr empty; last line the exit status | CONFIRMED | equals `p_analyze_selftest_final.txt`; `.err` 0 bytes; `rc=0` | |
| 94 | §3 header: HEAD's stage `dbe95739…569d`, the final `3390a448…a406`; §3.1 the script | CONFIRMED | `git show HEAD:… \| shasum`; `stage_head.py` hash; §3.1 = `gates_regress.py` scrubbed | |
| 95 | §3.2: the per-case summaries; both digests `b7a5ba4d…433a`; byte-identical | CONFIRMED | summaries rebuilt from my re-run equal both lines; hashes as above | |
| 96 | §4: harness description; §4.1 derivation | CONFIRMED | `harness.py`; §4.1 = `r3check/make.py`; `r3check/{stage,driver}_new.py` hash to the final files; re-deriving from the final files gives N17/N22/N26 byte-identical to `r3check`'s | |
| 97 | §4.1 comment: "N26's anchor occurs twice in the driver" | IMPRECISE | The return line occurs twice; the anchor as derived (with the P-CAMPAIGN print's last line) occurs once, and `make.py` asserts `count == 1` | "N26's return line occurs twice in the driver …; its anchor, extended to the P-CAMPAIGN print's last line, occurs once" |
| 98 | §4.2: baseline 74/74 (55 stage); N17 73/74; N22 and N26 18/19 (driver only); the failing checks | CONFIRMED | `r3check/*.json`; my harness runs reproduce each count and failing check | |
| **Review raw** |||||
| 99 | Title and header: 3 rounds by one reviewer, read-only at `3e1b614`, scratch copies, mutants loaded with the real `__file__`, no repository edit | CONFIRMED | the three hand-backs come from one reviewer agent, and Code's round 2 and 3 messages were continuations to it; each report states HEAD `3e1b614` and no repository write | |
| 100 | Round 1's brief quoted items 1–5 verbatim; rounds 2 and 3 sent under the same rules | CONFIRMED | row 73's evidence | |
| 101 | Each report verbatim (frame removed, indent undone, `<repo>`/`<tmp>` scrubbed, headings down two) | CONFIRMED | regenerated from each hand-back with those transforms: equal byte for byte (197, 136, 105 lines) | |
| 102 | The reviewed files' sha256 per round | CONFIRMED | the reviewer's snapshots hash to `9f8ed822…`/`4d1d3d1e…`, `5ba046a0…`/`04da458d…`, `e81a25be…`/`f419091c…` | |
| 103 | Code's dispositions follow each round | CONFIRMED | each section equals `dispositions_all.md`'s round section; the per-round files the reviewer read differ only by a heading line | |
| 104 | Round 3's dispositions: checks (204/204; harness 74/74, 55 + 19; N17, N22, N26 killed) and the sweep's four text changes | CONFIRMED | my runs; diff of the r3 snapshots to the final files shows exactly those four changes | |
| 105 | No clock time or stamp, `$` figure, local absolute path or email in the entry or either raw | CONFIRMED | pattern scan of all three texts: none | |

### Observations (not marked)

- **O-1.** The campaign's constants live in `valence_core/p/stage.py`, pinned by the package hash. m keeps them in its driver, and Code's STOP point said "p's driver must carry each checkpoint's cap". The entry never says they are driver constants. This is noted only because LOCK-p v1.0 names both hashes.
- **O-2.** The sweep's fourth change, the P'S REPORT reflow, which the entry does not list, leaves `valence_core/p/stage.py` line 124 at 169 characters. It is cosmetic.
- **O-3.** The review raw's round 1 disposition of MINOR-2 says p's cap is taken "as m's `hour_cap_exceeded` does". m also takes a text or a Fraction. The round 2 dispositions (NOTE-D) record the correction. It is a historical record, and no change is needed.
- **O-4.** Round 3's dispositions also say "The three gap survivors" (row 81). The next bullet there names S3, so the raw is clear in context.

### Disclosures

**Commands that touched `data/`:**
- A name-only `ls` of `data/p/ckpt` and `data/p/reports`, filtered for `campaign` with `/usr/bin/grep -c -i` and `/usr/bin/grep -i`: 0 names.
- Two counts of names in those directories matching `_qual\|_time` (12, 18). These were name-only and not needed.
- On `data/p/gates/G-PWR-p.json`: `shasum -a 256`, `git rev-parse HEAD:…` and `git hash-object` (digests). Its `schema` and each unit's `launch.L` were read with `json.load`.
- `json.load` of `data/p/gates/G-SHAPE-p.json`, to compare its `provenance.import_closure` with a fresh closure. Only the file count and the equality were printed.
- Python probes importing `valence_core.p.stage`:
  - `gpwr_problems`, whose m `_committed` git reads touch `G-PWR-p.json`;
  - `out_paths` (names computed, nothing read);
  - `fresh_import_closure()` (git reads of 14 non-`data` files);
  - `campaign_state` / `campaign_ruling_problems` on a synthetic checkpoint in `CW/vc/ckx`.
- p's self-test, once. Under the task's permission, it ran its own code:
  - a name-only `iterdir` of `data/p/gates` and `data/p/ckpt`;
  - `git check-ignore -q` over p's output names under `data/p/ckpt` and `data/p/reports` (the item-8 form the entry flags);
  - reads of committed gate artifacts (`data/m/gates`, `data/p/gates`), the schedules and the lexicon;
  - the non-stub precheck's committed-file git reads, with a stand-in lock.
- The reviewer's harness, four times (baseline and N17 in full; N22 and N26 driver-only). These runs execute the same self-test code.
- The gates' regression, once per stage, into temporary roots.
- `git grep -l -F … -- . ':!data/**'`, item 3's form.
- A pruned `find` over `valence_core/p` and `scripts` for symlinks and `data` directories.

**Never touched:** nothing under `data/*/ckpt` or `data/*/reports` was opened, read, hashed or searched by a command of mine. No size or time of anything there was printed.

**Departures and reads beyond the listed sources:**
- To check row 73, I read Code's session transcript, outside the repository, with a script. It printed only booleans, message lengths and the rule sentences of the round 2 and 3 messages.
- One `git status --porcelain -- <paths>` (pathspec-limited; item 1 names the bare form), names only.
- A `diff -u` of the reviewer's round-3 snapshots against the final files printed their modification times in its header. These are scratch and source files, not under `data/`, and are not reproduced here.
- `-nt` order checks of scratch outputs against the two final files. No time was printed.
- Model-free scratch scripts in `CW/vc`: the mirror diffs, the recorded-run diff, the quotes, items and mutant counts, and the review-raw comparison.
- `git show HEAD:` and `git diff --` of the two BUILD files, as the brief allows.

Nothing was written in the repository. `git status --porcelain` is unchanged: the two files stay ` M` at the same sha256s, with the same 31 untracked entries. No model was loaded and no remote machine was contacted.
