# n_analyze.py, the seat's ruling of 2026-11-18 on PIN-n-27 to PIN-n-32 and F11: the blind values-check, two passes (PI date 2026-11-18)

Code's raw for the entry `n package — scripts/n_analyze.py, the seat's ruling on PIN-n-27 to PIN-n-32 and F11`.

**Who checked what.** Two blind values-checkers checked four texts against their sources, claim by claim:
- the entry;
- the close line on `977b78b`'s entry;
- the review raw;
- the analyzer's new and changed texts: its registers, the seat's forms as transcribed, and the docstrings the change
  touched.

Each checker was a subagent of this session, under a brief that quoted the list of record v2's items 1–5 and allowed no
Python.
- The first pass checked the first drafts.
- The second pass checked the drafts as revised after the first, and whether each of the first pass's dispositions was
  carried and is true.
- With no FAIL, the second pass is the last. The edits after it are checked by tool (its dispositions).

**What the passes changed in the analyzer.** Besides the texts, the passes changed nine texts and one comparand in the
analyzer, all after its mutation testing (the review raw's §5). The run of record is on the final bytes.

**Its departure.** The second checker disclosed one departure: an unscoped `git ls-files` piped to a name filter. It
listed tracked names tree-wide inside the pipe, `data/mf3`'s among them, and printed only `results/raw` names. Its
report carries it, and so does the entry.

**How the reports appear.** Each report is reproduced whole, its headings moved down two levels, and is followed by
Code's dispositions. The reports are the checkers' hand-back messages, taken from the subagents' transcripts by script.
The checkers write SCRATCH for Code's scratch folder and REPO for the repository.

## Pass 1: the report

#### Values-check: the v4 entry, the close line on 977b78b, the review raw and the analyzer's new texts

**Method.** I ran no Python and edited nothing in REPO, and nothing in SCRATCH outside `SCRATCH/vc/checker/`. I read nothing under `data/`, and every `git status` was scoped to named paths. The tools were shasum, diff/cmp, /usr/bin/grep, sed, git show/log/ls-files, and one awk that only printed a field.

Helper outputs in `SCRATCH/vc/checker/`:
- `base_final.diff` (977b78b → final) and `frozen_mbase.diff` (frozen → mutant base);
- `vcmp/` (block-by-block mutant comparisons);
- `kills_rebuilt.txt` (the kill list rebuilt from the .out files);
- the extracted form strings and the quoted routing items.

**Hashes, all re-computed:**
- final c583273d…caeb;
- base-977b78b = `git show 977b78b:scripts/n_analyze.py` = 97097ce0…251e;
- frozen 51396daf…fc41 (mode r--r--r--);
- mutant base 285c6168…87db (r--r--r--);
- reviewer report 2104634c…acb4;
- answers raw 5843a9bd…7165, added at 26cf7d2.

`diff` final vs mutant base: line 57 (the REPO line) only.

"Pending" below means: pending the run of record (predicted by f2, 217/217, coverage PASS, and `main` returns 0 iff ok), or pending the commit. Pending claims are counted as CONFIRMED.

##### 1. Entry (SCRATCH/raw/entry.filled.md)

| ID | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| E1 | 1–2 | Seat's ruling on PIN-n-27..32 and F11 carried in (§5; PI item 6) | CONFIRMED | Raw §5.1–5.6 (l.61–71); the relay's item 6 |
| E2 | 2 | Battery 217/217 | CONFIRMED, pending the run of record | f2 last line 217/217 |
| E3 | 2–3 | 54 of 54 mutants killed | CONFIRMED | 54 .out files, each with ≥2 FAILs; kills.txt equals the outputs rebuilt |
| E4 | 3–4 | PIN-n-33..36 are Code's readings; two questions to the seat | CONFIRMED | Comment above PINS (l.2290); the entry's two questions |
| E5 | 4 | Model-free; nothing on the box; no stage ran | NOT CHECKABLE | f2 asserts no model library is imported |
| E6 | 5 | sha256 c583273d… | CONFIRMED, pending the commit | shasum of the final file |
| E7 | 5 | 97097ce0…251e at 977b78b | CONFIRMED | git show 977b78b + shasum |
| E8 | 5–6 | Schema pin d791bd9 unchanged | CONFIRMED | SCHEMA_SHA256 0ea39600… "# d791bd9" in both versions; REPO schema hashes to it |
| E9 | 6 | Bound files unchanged | CONFIRMED | PROPOSAL/ADDENDUM/SCHEMA pins and BOUND_RELS identical; files hash to the pins |
| E10 | 6 | Commands unchanged | CONFIRMED | add_argument/add_parser lines identical |
| E11 | 7–9 | Raw sha256 5843a9bd…7165, committed at 26cf7d2 | CONFIRMED | shasum; `git show --name-status 26cf7d2` |
| E12 | 9 | Cited by path | CONFIRMED | Module cites the path (l.18–20, 635–636); not in BOUND_RELS |
| E13 | 9–10 | The battery's hook bars results/raw | CONFIRMED | `_barred`, l.2457–2468 |
| E14 | 10–11 | "transcribed twice: once in the module and once in the battery's oracle" | IMPRECISE | See note E14 |
| E15 | 11 | Checked against the raw by the review and the values-check | CONFIRMED | Reviewer §1 "Sentence forms, byte for byte". My grep -F finds each in the raw once: FOURTH, `_ORC_FOURTH` (equal to FOURTH), `_ORC_NOTE`, ZONE_WORDS, MERGE_NOTE, READABLE, NOT_READABLE, spec_v |
| E16 | 11–12 | Run of record: 217/217, 220 ids, exit 0 | CONFIRMED, pending the run of record | f2 |
| E17 | 13 | Self-test raw path | CONFIRMED, pending the commit | — |
| E18 | 14–17 | Items 6–7 verbatim as relayed | CONFIRMED | diff with the brief's relay: identical |
| E19 | 14 | "Route as given"; section N for n-analyzer | CONFIRMED | RESULTS.md coordinating close line on e48c7d0 ("Route as given"); raw §7 "N. n-analyzer" |
| E20 | 15 | Paste block not committed | CONFIRMED | No tracked 2026-11-18 routing file (`git ls-files`); coordinating line's observation 6 |
| E21 | 19 | Item 7 is n-build's; the analyzer reads nothing it changes | CONFIRMED | Raw §5.5/§7 item 7; no convention/match-count/BACKEND/median text in the analyzer |
| E22 | 21–22 | PIN-n-27/28/31 stand as registered, marked accepted | CONFIRMED | Their texts are untouched by the diff; comment above PINS; module docstring |
| E23 | 22 | Digest 209d7b46…92f5 → 281c6827…bbe2, set from the first draft run's printed value | CONFIRMED | Base l.2679; final l.3078; d1 prints 281c6827…bbe2 |
| E24 | 24–25 | N2's certification reads, each with its sessions' shadows | CONFIRMED | `n2_reads` l.518–522; build_state's `sh` |
| E25 | 26–27 | "N2 INDETERMINATE iff … missing, non-finite, has an unusable shadow or is emptied in the TAU/4 row, or a pause" | IMPRECISE | See note E25 |
| E26 | 27–28 | Causes name the point | CONFIRMED | `named_at`; N2-POINT-CAUSES literal |
| E27 | 29–30 | Elsewhere leaves N2 decided; N1 and dose INDETERMINATE per arm (n:134) | CONFIRMED | `dose_outcome`/`_causes` per arm; N2-POINT-ELSEWHERE; PROPOSAL l.134. The seat wrote "or", but N1 INDETERMINATE implies dose INDETERMINATE, so "and" holds |
| E28 | 31 | The other f's figures are "not computed" where not usable | CONFIRMED | e_b, v_b, c_b, cert_b; the guards' figures |
| E29 | 32–33 | Point and per-arm statistics; VERDICTS' point causes | CONFIRMED | build_state; `state_figures` "point_causes" |
| E30 | 34 | G-LEAK-n's table point by point | CONFIRMED | `gleak_table` `needs()` |
| E31 | 35 | OPEN-Q6 records the ruling | CONFIRMED | l.2423 |
| E32 | 36–37 | §5.3 summary; the sign enters no N2 outcome | CONFIRMED | Raw l.65 |
| E33 | 38–39 | §5.4 quotation | CONFIRMED | Verbatim, raw l.67 |
| E34 | 40–44 | §5.6: readability by G-READ-n, label by §0.6, "explanation of record" in the three forms only | CONFIRMED | Raw l.71; `sentence_dose`; SENT-RULING |
| E35 | 46 | 2,561 evaluations (1,921 at 977b78b) | CONFIRMED | f2 TUP-COUNT; the 977b78b entry |
| E36 | 46–47 | Tallies re-derived in the review raw's §6 | CONFIRMED | §6 arithmetic checks |
| E37 | 47 | Reachability 28, 25, 24, 17, unchanged | CONFIRMED | f2 l.136–139; the 977b78b entry |
| E38 | 48 | Registered in PINS; strikable until LOCK-n v1.0 | CONFIRMED | l.2290–2292 |
| E39 | 49–51 | PIN-n-33's behaviour | CONFIRMED | Pause causes over `n2_reads` only; the guards' "paused" field beside |
| E40 | 51 | Both halves depart from rulings of record | CONFIRMED | 2026-11-16 answers §1.6 (l.33); PROPOSAL l.140; base N2_ARMS = N2-E/S/C |
| E41 | 52–53 | §5.3 does not name SPECIFIC's span_reward figure or SHARED's valence figure | CONFIRMED (as a reading) | Raw l.65 names SPECIFIC's valence figure and SHARED's/NULL's parentheticals |
| E42 | 53–54 | "so span_reward's reads '… against [c], against the conditioned zone'" | IMPRECISE | See note E42 |
| E43 | 55–56 | PIN-n-35: an input, not a coordinate; 640 more | CONFIRMED | `evaluations()`; 2561 − 1921 |
| E44 | 57–58 | Causes and their names | CONFIRMED | — |
| E45 | 59 | N2's floor and slopes, reported only, stay per arm | CONFIRMED | ADDENDUM-n1 §7.5 "(reported only)"; `if st.complete[...]` |
| E46 | 60–61 | A TAU/4 slope with no common session marks the arm, not its points; the row now decides N2 | CONFIRMED | `arm_emptied`; VD-SENSITIVITY's literal tuple (…, SHARED, …) passes in f2; base marked N1-R per arm |
| E47 | 62 | An INDETERMINATE N2 has no beside, as at 977b78b | CONFIRMED | Both versions' return |
| E48 | 64–68 | PIN-n-33 question quotations | CONFIRMED | §5.2, §1.6 and n:140 verbatim; base read N2-S/N2-C as N2's reads |
| E49 | 69–71 | F4: same text in both cells; label in the field only; A.6 prints "(N4 [n4])" | CONFIRMED | D_FOURTH keyed on gr only; A6 form |
| E50 | 74 | Frozen at 51396daf…fc41 (217/217) | CONFIRMED | shasum; d2 217/217, its check texts match the frozen copy |
| E51 | 75–77 | F1 MINOR, F2–F8 NOTE, no MAJOR; B1–B2 MINOR, B3–B7 NOTE; 35 mutants, 8 predicted survivors | CONFIRMED | report.md |
| E52 | 79 | F1 to the seat; PIN-n-33 quotes both rulings | CONFIRMED | — |
| E53 | 80 | F2, F3, F7, F8 registered in PIN-n-36/-34 | CONFIRMED | — |
| E54 | 81 | "F5 and F6 are fixed (OPEN-Q3, OPEN-Q6 and two docstrings)" | IMPRECISE | See note E54 |
| E55 | 82 | F4 to the seat | CONFIRMED | — |
| E56 | 83–85 | B1–B7 fixes as listed | CONFIRMED | `frozen_mbase.diff`: 15 hunks, all accounted for |
| E57 | 86 | M01–M35 the reviewer's; M36–M54 19 of Code's | CONFIRMED | headers_v/c |
| E58 | 86–88 | Ran on 285c6168…87db (217/217); 54/54 killed; the 8 survivors killed by added/extended checks | CONFIRMED | f2; .out files; kills of M08/12/14/15/16/17/18/24 |
| E59 | 89 | Committed bytes differ from the mutant base in the REPO line alone | CONFIRMED, pending the commit | diff |
| E60 | 92–93 | One process, nice -n 19, -I, temp folders outside the repo, foreground | NOT CHECKABLE | run_battery.sh/run_mutants.sh show `nice -n 19 … -I`; the battery uses `tempfile.TemporaryDirectory` |
| E61 | 94 | Draft: 214/217 then 217/217; failed on the digest and one old form string | CONFIRMED | d1 FAILs: SENT-CODE-FORMS, RD-GREAD-MIXED, coverage; d2 |
| E62 | 95–96 | Mutant window: 215/217 (the +d_20 test) then 217/217 | CONFIRMED | f1 fails "empties N1-R at +d_20"; schema DOSE_RULE_LABELS = ("0","+1","-1") |
| E63 | 96 | Batches of five | NOT CHECKABLE | — |
| E64 | 97 | Run of record: 1 | CONFIRMED, pending the run of record | — |
| E65 | 99–100 | Q-F3 ran beside; no other window open | NOT CHECKABLE | — |
| E66 | 101–102 | Committed by path; not pushed | CONFIRMED, pending the commit | — |
| E67 | 102–103 | "Next" | CONFIRMED | Consistent with the 977b78b entry's Next and the module docstring |

**Note E14.** §5.3's words are held in the battery by SENT-RULING's literals (`spec_v` and the zone-words literal), not by the oracle. The oracle's `_ORC_NOTE` enters T2 only through its figure prefix (`fig`, l.1029/1826). The note's words are held by SENT-RULING's literal and the filled-sentence literals. Suggested: "and again in the battery: the oracle (`_ORC_NOTE`, `_ORC_FOURTH`) and SENT-RULING's literals".

**Note E25.** Raw l.63 says "missing or non-finite, or a pause". The shadow and TAU/4 causes are Code's carrying (PIN-n-36), but they read here as §5.2's own words. Mark them as PIN-n-36's.

**Note E42.** This holds for SPECIFIC and SHARED only. NULL's parenthetical has no "against [c]": it reads "(span_reward, Δm = [xE] nats [CIE], against the conditioned zone)". PIN-n-34 itself says "where it has one".

**Note E54.** F5's fix also changed the comment above OPEN (l.2406–2408), which the parenthetical omits. F5's OPEN-Q4 point was kept, as the reviewer allowed.

##### 2. Close line (SCRATCH/raw/close_977b78b.filled.md)

| ID | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| C1 | 1 | PI date; n-analyzer's line per the raw's header and §7 item 6 | CONFIRMED | Raw l.3 ("…n-analyzer and coordinating sessions add their close lines"); l.90 |
| C2 | 2–4 | Path, full sha256, 26cf7d2 | CONFIRMED | — |
| C3 | 4 | §5 rules "this entry's six readings and F11" | CONFIRMED | RESULTS.md l.509–623: PIN-n-27..32 flagged plus F11 |
| C4 | 4–9 | Items 6–7 verbatim as relayed | CONFIRMED | diff identical |
| C5 | 6 | Paste block not committed | CONFIRMED | As E20 |
| C6 | 11 | Item 6 carried; c583273d…caeb | CONFIRMED, pending the commit | — |
| C7 | 11–12 | PIN-n-27/28/31 stand | CONFIRMED | — |
| C8 | 12–13 | 29/32 re-registered as amended; 30 accepted with its sentences amended | CONFIRMED | PIN texts l.2347–2373 |
| C9 | 13 | Fourth form in the sentence layer | CONFIRMED | `sentence_dose` l.750ff |
| C10 | 13–14 | Digest moved (§5.1) | CONFIRMED | — |
| C11 | 14–15 | Item 7 is n-build's | CONFIRMED | As E21 |
| C12 | 15–16 | PIN-n-33..36 flagged in this commit's entry | CONFIRMED, pending the commit | — |

##### 3. Review raw (SCRATCH/raw/review.md)

| ID | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| R1 | 3 | Raw for the entry (title) | CONFIRMED | Prefix of the entry's title |
| R2 | 5 | 977b78b sha | CONFIRMED | — |
| R3 | 6–7 | Raw path, sha, 26cf7d2 | CONFIRMED | — |
| R4 | 8–13 | What changed, by § | CONFIRMED | `base_final.diff` |
| R5 | 14 | 214/217 then 217/217 | CONFIRMED | d1, d2 ("one step" not checkable) |
| R6 | 15–16 | Frozen read-only at 51396daf (217/217, 220 ids) | CONFIRMED | Mode r--r--r--; d2 |
| R7 | 17–18 | Subagent brief quoting list of record v2 items 1–5; no Python | CONFIRMED | SCRATCH/review/BRIEF.md |
| R8 | 19–20 | Its spec list | CONFIRMED | Same brief |
| R9 | 21 | Executed no code; opened nothing under data/ | NOT CHECKABLE | The report says only "I ran no Python, edited nothing and wrote no file" |
| R10 | 22–24 | Findings, severities, V01–V35, the 8 predicted survivors | CONFIRMED | report.md |
| R11–R14 | 26–30 | F1 / registered / fixed / F4 kept | CONFIRMED | PIN texts; OPEN; docstrings |
| R15 | 31–32 | Two cases added after the freeze | CONFIRMED (content) | `frozen_mbase.diff`; timing not checkable |
| R16 | 33 | M01–M35 = V01–V35 verbatim | CONFIRMED | 35/35 block-identical; headers identical |
| R17 | 33–34 | "M36–M54 are 19 of the 39 … those that do not repeat one of the reviewer's on the same line the same way" | **FAIL** | See note R17 |
| R18 | 34–35 | One run on 285c6168 (217/217); 54/54 killed | CONFIRMED | — |
| R19 | 35–36 | The 8 survivors each killed by an added/extended check | CONFIRMED | — |
| R20 | 37–38 | REPO line only | CONFIRMED, pending the commit | — |
| R21 | 39 | §6 is the cited derivation | CONFIRMED | — |
| R22 | 41–42 | Run conditions | NOT CHECKABLE | Scripts support nice/-I |
| R23 | 43–44 | Fresh copy; exact replacement asserted once; killed = non-zero exit | CONFIRMED | run_mutants.sh; each out/Mnn.py differs from the base by one hunk within .old/.new; `return 0 if battery()["ok"] else 1` |
| R24 | 48–50 | Report saved; sha 2104634c…acb4; headings down two levels; nothing else changed; frozen-copy line numbers | CONFIRMED | diff with `##`→`####`: only the final newline differs; line numbers spot-checked (518–522, 539, 548, 760–761, 1859, 1935–1936, 2358–2363, 2382–2401, 2793–2794, 2866–2868) |
| R25 | 406–415 | F1's quotations | CONFIRMED | §5.2, §1.6 and n:140 verbatim; base read N2-E/S/C |
| R26 | 415–416 | PIN-n-33 quotes both; the entry asks | CONFIRMED | — |
| R27–R34 | 417–435 | F2–F8 dispositions | CONFIRMED | Including ADDENDUM-n1 §7.5 "(reported only)", the OPEN-Q3/Q6/comment edits and the two docstrings |
| R35 | 442–446 | B2's campaigns; "takes G-LEAK-n's +1 row out" | IMPRECISE | The row stays, not computed ("not usable: tau4-emptied:N1-R@+1", l.3546–3549) |
| R36 | 447–449 | +d_20 cannot be emptied; 215/217; N2-POINT-CAUSES literal | CONFIRMED | DOSE_RULE_LABELS; f1; `bad_a` |
| R37–R40 | 450–455 | B3 literal tuple; B4 seven sentences; B5 order; B6 twenty keys | CONFIRMED | — |
| R41 | 456 | B7 cites this raw | CONFIRMED, pending the commit | — |
| R42 | 460–461 | "the frozen copy refused it in the set only" | IMPRECISE | The frozen copy's `sentence_dose` already raised (l.754 in both copies); only its check covered the set alone |
| R43 | 462 | RD-POINTWISE N1-P at −1 | CONFIRMED | — |
| R44 | 466–468 | "these 19 do not repeat …" | IMPRECISE | True of the 19, but it implies the rule R17 states |
| R45 | 468 | Reproduced whole; each old text checked once | CONFIRMED | Blocks equal the mutant files and the mutants_c originals |
| R46 | 470–472 | Full hash 285c6168…f987db; 217/217 and 220 ids; one at a time; all killed | CONFIRMED | Batches not checkable |
| R47 | 474–476 | First six unreached ids, sorted | CONFIRMED | l.4626 `unreached[:6]` |
| R48 | 478–533 | The 54-row table | CONFIRMED | Columns 1–5 equal headers_all.txt; Result equals kills.txt equals the rebuilt list; identical to kill_table.md |
| R49 | 535–563 | The fifteen group-exception runs and every detail | CONFIRMED | e.g. M05 KeyError 'causes'/0.625 with 5 FAILs then RD-SHADOW; M11 rand_07 +1/2; M13 run 100; M42 run 17; M16 ('rand_00','+1'); M21 P at 0.625; M35 'N1-P@-1'; M36 five groups plus the reachability shapes plus the pinned map; M40 ValueError plus no-raise; M48 'why' after 2 G-LEAK FAILs; M51 'f=0.10'; M54 six groups, shapes a/b plus REACH-FOURTH |
| R50 | 565–573 | Survivors' killers | CONFIRMED | — |
| R51 | 575–692 | Code's mutants whole | CONFIRMED | — |
| R52 | 696–698 | Ran on the working copy; frozen after each run, unchanged | CONFIRMED | INVOCATION lines name work/n_analyze.py; d1/d2 check texts match the frozen copy and f1/f2 the mutant base; the work file now hashes to the mutant base |
| R53 | 700–705 | Draft window details | CONFIRMED | — |
| R54 | 706–709 | Mutant window details | CONFIRMED | — |
| R55 | 710–711 | Batches of five; M51–M54 last | NOT CHECKABLE | — |
| R56 | 712 | Run of record | CONFIRMED, pending the run of record | — |
| R57 | 714–715 | Q-F3 / windows | NOT CHECKABLE | — |
| R58 | 719–725 | REPO line only; "as the committed analyzer always has" | CONFIRMED | Same line at 5c0ae6b, 2822721, bedc198, 977b78b |
| R59 | 729–771 | §6 tallies | CONFIRMED | Every product and sum re-done; equals `_bt_expected_tallies`; f2 TUP-T10 PASS |

**Note R17.** Of the 20 dropped (mutants_c.spec has 39; 19 kept), several do not repeat a reviewer's mutant on the same line the same way:
- M106 and M123 share no line with any of V01–V35, by an exact line match.
- M102, M113, M115, M121, M122 and M124 change a reviewer's line another way.

State the selection actually used, or name the dropped mutants.

##### 4. Analyzer texts (SCRATCH/final/n_analyze.py)

| ID | Lines | Text | Verdict | Evidence |
|---|---|---|---|---|
| A1 | 16–20 | Module docstring | CONFIRMED | — |
| A2 | 2290–2292 | Comment above PINS | CONFIRMED | — |
| A3 | 2406–2408 | Comment above OPEN | CONFIRMED | — |
| A4 | 2347 | PIN-n-29 | CONFIRMED | Follows raw l.63 |
| A5 | 2354 | PIN-n-30 | CONFIRMED | Raw l.65; `against` = CI excludes 0, certified and mean < 0 |
| A6 | 2369 | PIN-n-32 | CONFIRMED | Raw l.67 |
| A7 | 2374 | PIN-n-33 | CONFIRMED | Quotations verbatim; schema's `arms_in_scope` |
| A8 | 2383 | PIN-n-34, "each figure gains its CI" | IMPRECISE | SHARED's span_reward figure already had [CIE] at 977b78b; the rest is confirmed |
| A9 | 2390 | PIN-n-35 | CONFIRMED | — |
| A10 | 2394 | PIN-n-36 | CONFIRMED | — |
| A11 | 2414 | OPEN-Q3 | CONFIRMED | — |
| A12 | 2418 | OPEN-Q4 | CONFIRMED | — |
| A13 | 2423 | OPEN-Q6 | CONFIRMED | — |
| A14 | 2431 | OPEN-Q8 | CONFIRMED | — |
| A15–A18 | 641–648 | ZONE_WORDS, MERGE_NOTE, FOURTH, READABLE, NOT_READABLE | CONFIRMED | Byte-equal spans in raw l.65/67/71 (grep -F) |
| A19 | 679–689 | C_N2's three forms | CONFIRMED | SPECIFIC's valence clause equals §5.3's quotation; otherwise 977b78b's text with only [CIE]/[CIV]/[zoneE]/[zoneV] inserted |
| A20 | 1003 | `_ORC_NOTE` | CONFIRMED | Byte-equal to raw l.67 |
| A21 | 1004–1007 | `_ORC_FOURTH` | CONFIRMED | Equals FOURTH; in the raw |
| A22 | 1602–1603 | `spec_v` | CONFIRMED | In raw l.65, its "…" dropped |
| A23 | 635–640 | "the dose forms print their figure with MERGE_NOTE after it" | IMPRECISE | Only the NOT-DETECTABLE forms do; DETECTABLE keeps VALUE_MERGED |
| A24 | 1001–1002 | "a slip in either fails T2" | IMPRECISE | True for FOURTH/`_ORC_FOURTH` and for the figure. MERGE_NOTE never enters T2: it is held by SENT-RULING and the filled literals. `_ORC_NOTE`'s words after the figure are compared by no check |
| A25 | 525ff | `n2_outcome` docstring | CONFIRMED | — |
| A26 | 2839ff | `build_state`: "An arm is complete iff every point is" | IMPRECISE | In the TAU/4 row a slope with no common session marks the arm while every point stays usable (PIN-n-36; VD-SENSITIVITY asserts N1-R tau4-emptied with every N1-R point []) |
| A27 | 2818 | `delta_m` docstring | CONFIRMED | `dm` is called only under `usable_at` |
| A28 | 1947 | `map_reach` docstring | CONFIRMED | — |
| A29 | 750 | `sentence_dose` docstring | CONFIRMED | — |
| A30 | 802 | `sentence_set` docstring | CONFIRMED | — |
| A31 | 1873 | `_bt_expected_tallies` docstring | CONFIRMED | Arithmetic; the cited raw is pending the commit |
| A32 | 3052 | `merge_text` docstring | CONFIRMED | Mirrors `value_text` |

##### Counts

| Text | Claims | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|---|
| Entry | 67 | 59 | 4 | 0 | 4 |
| Close line | 12 | 12 | 0 | 0 | 0 |
| Review raw | 59 | 51 | 3 | 1 | 4 |
| Analyzer | 32 | 28 | 4 | 0 | 0 |
| **Total** | **170** | **150** | **11** | **1** | **8** |

Included in CONFIRMED: 4 claims pending the run of record and 9 pending the commit.

##### Observations (outside the graded claims)

1. **Mutant selection (R17/R44).** The 20 dropped Code mutants include ones that duplicate a reviewer's mutant in effect, not in line: M123 has the same effect as V28. The stated rule should say so.
2. **The battery's copy of §5.4's note.** `_ORC_NOTE` is used only for its figure prefix, so its note words are a dead copy. The battery's real holds on the note are SENT-RULING's literal and the `note` literals. This bears on E14 and A24.
3. **Stale battery description.** SENT-CODE-FORMS's description still lists "(Code's, OPEN-Q8 as ruled, and ADDENDUM-n1 §7.6's)". Its count is now 42 (38 in the v3 selftest raw), and the 4 new forms are the seat's RULING_FORMS.
4. **The seat's example "N1-R at +1/2" as "elsewhere"** (entry l.29; PIN-n-29) fails where the cap binds and d_eq folds into +1/2, since that is then N2's own point. F6 amended `map_reach`'s docstring for this; the entry and PIN-n-29 repeat the example unqualified.
5. **Mixed sources under "§5.2".** The entry's "§5.2" sub-bullets mix the seat's words with Code's mechanics without marking them (VERDICTS' point causes, G-LEAK-n's point-by-point table, the shadow and TAU/4 causes).
6. **Relay wording.** The PI's relayed items 6–7 differ in wording from the seat raw's §7 items 6–7. The texts quote the relay as relayed, correctly.
7. **Formatting.** Entry l.5 and close l.4 overrun the wrap width: the fill put the full 64-character hash inside a wrapped line.
8. **Two records.** Both the entry and the close line quote items 6–7 and each calls itself "their record".
9. **The reviewer's own line.** Its line "C_N2 … with only [CIE], [CIV], [zoneE] and [zoneV] added" (quoted unedited) overlooks that SHARED's [CIE] predates v4.
10. **Comment above C_N2 (l.677–678).** It says ZONE_WORDS closes "the figure's parenthetical", but SHARED's valence figure has none; PIN-n-34 states this correctly.

### Code's dispositions of pass 1

Pass 1: 170 claims; 150 CONFIRMED, 11 IMPRECISE, 1 FAIL, 8 NOT CHECKABLE; ten observations. Every FAIL and IMPRECISE is
applied, and so are observations 1–5, 7, 8 and 10. Observation 6 is applied in the entry's wording; observation 9 is the
reviewer's own line, quoted unedited (§1), and is left as it is.

#### The FAIL

- **R17 (and R44, IMPRECISE), the mutant selection.** The rule stated ("those that do not repeat one of the reviewer's
  on the same line the same way") was not the selection made. The review raw's head and §3 now say what was done: Code
  dropped 20 of its 39, to keep the window near 90 minutes, as overlapping the reviewer's. §3 names them by the
  reviewer's mutants they overlap:
  - ten make one of the reviewer's own changes (as V02, V09, V16, V19, V20, V21, V25, V33, V34, V35);
  - eight mutate a reviewer's line another way (the lines of V01, V06 and V07, twice, V11, V13, V29, V30, V32), the one
    on V29's lines breaking the opposite way;
  - two break, on another line, what V03 and V28 break.

#### The IMPRECISE

- **E14, the transcriptions.** The entry now says the seat's words are transcribed in the module and again in the
  battery, in its oracle (`_ORC_FOURTH`, `_ORC_NOTE`) and in SENT-RULING's literals.
- **E25, §5.2's words.** The entry's §5.2 now separates the seat's ruling (in its words: "missing or non-finite, or a
  pause") from Code's carrying (PIN-n-36: shadows, the TAU/4 row, the causes' names, the statistics, VERDICTS'
  figures, G-LEAK-n's table). That also answers observation 5.
- **E42, the doubled "against".** It is now said to hold in SPECIFIC and SHARED, in the entry and in PIN-n-34.
- **E54, F5's fixes.** The comment above OPEN is now listed.
- **R35, G-LEAK-n's +1 row.** It is now "not computed (naming tau4-emptied:N1-R@+1)", not "taken out".
- **R42, the fifth refusal case.** The frozen copy refused in both places but checked only the set's refusal; the raw
  now says so.
- **A8, PIN-n-34's CI.** Each figure now "carries" its CI, SHARED's span_reward figure having had it already.
- **A23, the comment above the seat's forms.** It now names the NOT-DETECTABLE forms, DETECTABLE keeping VALUE_MERGED.
- **A24 (with observation 2), the oracle's note.** SENT-RULING's note check now compares the module's note with the
  oracle's copy (`_ORC_NOTE`) instead of a third literal, so that copy is read by a check. The comment now says a slip
  fails T2, for the fourth form and the figure, or SENT-RULING, for the note's words.
- **A26, `build_state`'s docstring.** An arm is complete "only if" every point is, and a slope with no common session
  in the TAU/4 row marks its arm alone.

#### Observations

1. The mutant selection: as R17.
2. `_ORC_NOTE`'s words: as A24.
3. SENT-CODE-FORMS's description now names the seat's forms of 2026-11-18.
4. The +1/2 example: PIN-n-29 and the entry now say +1/2 is N2's own point where the cap binds and d_eq folds into it.
5. The entry's mixed §5.2: as E25.
6. The relay's wording: the entry now says it differs a little from the seat raw's §7 draft, the PI's block being the
   record.
7. The wrap width: each full hash now stands on its own line.
8. Two records: the close line no longer quotes items 6–7; it points to the entry, their record.
9. The reviewer's own line on [CIE]: its report is quoted unedited (§1); left as it is.
10. The comment above `C_N2`: the words close the figure's parenthetical, "or the sentence where the figure has none".

#### The analyzer's bytes after this pass

`SCRATCH/final/n_analyze.py` changed in nine hunks after pass 1, besides the repository line (ten hunks against the
mutant base). No form changed, so the forms' digest is the same. The review raw's §5 lists the hunks, and the entry
counts them as seven texts and one battery comparand. The run of record runs on these bytes.

## Pass 2: the report

#### Values-check, pass 2: the v4 entry, the close line on 977b78b, the review raw and the analyzer's new texts

**Result.** I checked 199 claims: 186 CONFIRMED, 3 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE. Every pass-1 disposition is applied as stated. Two of the IMPRECISE items are one new defect, a "+1/2" qualification that is true but incomplete (in PIN-n-29 and in the entry). The third is a wording slip in the entry.

**Method**
- I ran no Python and executed no repository code. I edited nothing in REPO. I wrote only helper files under `SCRATCH/vc/checker2/`: diffs, the extracted form literals, the rebuilt kill list and the split mutant blocks.
- Tools: shasum, diff, cmp, `/usr/bin/grep` (`-F -f` for literal matching), sed/awk/tr/cut/wc for text extraction, and git show/log/ls-files/rev-parse. git status was scoped to `scripts/n_analyze.py`, `RESULTS.md` and `results/raw/`. I read nothing under `data/`.
- **Departure, disclosed.** I ran one unscoped `git ls-files` piped to a name filter for "paste|routing", to look for a committed copy of the PI's paste block.
  - In the pipe it listed tracked names tree-wide, `data/` included. It printed only `results/raw` names.
  - It touched names only: no content, no metadata, and it was momentary.
  - The binding rule bars listing anything under `data/mf3` "in any form", so I report it.

**Hashes I recomputed**
- The final file is `9e75f3f7…62e1`, equal to the entry's value.
- `base-977b78b.py` equals `git show 977b78b:scripts/n_analyze.py` and REPO's current file: `97097ce0…251e`.
- Frozen copy `51396daf…fc41` and mutant base `285c6168…87db`: both read-only (r--r--r--). `SCRATCH/work/n_analyze.py` equals the mutant base.
- Reviewer's report `2104634c…acb4`; answers raw `5843a9bd…7165` (added at 26cf7d2).
- PROPOSAL `30a3d0f5…04f4`, ADDENDUM `e979f8f2…5e03`, and schema `0ea39600…0db6`, which equals `git show d791bd9:valence_core/n/schema.py`.
- My diff of mutant base to final is byte-identical to `vc/final_vs_mutbase.diff`: 10 hunks.
- `review/v4-under-review.diff` is base to frozen; its body is identical to my recomputed diff.

**"Pending"** means pending the run of record (predicted by `runs/f2.txt`: 217/217, coverage PASS, and `main` returns 0 iff ok) or pending the commit. Pending claims are counted as CONFIRMED and tallied separately.

##### 1. Entry (`SCRATCH/raw/entry.filled.md`; the values-check placeholder line is skipped)

| ID | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| E1 | 1 | Dated 2026-11-18 | CONFIRMED | PI date of the answers raw and of the routing |
| E2 | 1–2 | Seat's ruling on PIN-n-27..32 and F11 carried in (§5; PI item 6) | CONFIRMED | raw l.61–71; base→final diff |
| E3 | 2 | Battery 217/217 | CONFIRMED, pending run of record | f2 217/217. The final differs from the mutant base in text, docstrings and one comparand, which holds (A21) |
| E4 | 2–3 | Reviewed blind; 54 of 54 killed | CONFIRMED | report.md; all 54 .out files have ≥2 [FAIL]; "killed" = non-zero exit (`run_mutants.sh`) |
| E5 | 3 | PIN-n-33..36 are Code's readings, flagged | CONFIRMED | comment above PINS, l.2292–2295 |
| E6 | 3–4 | Two questions to the seat | CONFIRMED | l.71–79 |
| E7 | 4 | Model-free; nothing on a model or the box; no stage ran | NOT CHECKABLE | Module is model-free by design; INVOCATION lines name the laptop venv |
| E8 | 5–6 | sha256 9e75f3f7… | CONFIRMED, pending commit | shasum |
| E9 | 7 | 97097ce0…251e at 977b78b | CONFIRMED | git show + shasum |
| E10 | 7 | Schema pin d791bd9 unchanged | CONFIRMED | SCHEMA_SHA256 "# d791bd9" identical (base l.2262, final l.2614) |
| E11 | 7–8 | Bound files unchanged | CONFIRMED | PROPOSAL/ADDENDUM pins and BOUND_RELS identical; files hash to them |
| E12 | 8 | Commands unchanged | CONFIRMED | No argparse line and no usage text in the diff |
| E13 | 8–10 | Raw path, 5843a9bd…7165, at 26cf7d2, cited by path | CONFIRMED | shasum; `git show --name-status 26cf7d2`; cited at l.20, 635, 2294, 2349, 2411, 4682; not in BOUND_RELS |
| E14 | 10–11 | The battery's hook bars results/raw | CONFIRMED | `_barred` l.2460–2471 |
| E15 | 11–12 | Transcribed in the module, and in the battery's oracle (`_ORC_FOURTH`, `_ORC_NOTE`) and SENT-RULING's literals | CONFIRMED | Every one is byte-equal to the raw (A15–A24) |
| E16 | 12–13 | All checked against the raw by the blind review and the values-check | CONFIRMED | Reviewer: "byte for byte". Pass 1: grep -F. This pass: each literal rebuilt from source, `grep -F -f` gives 1 hit in the raw. The review did not name SENT-RULING's zone-words and READ_ALT literals, but SENT-RULING's own equalities tie them to constants it did check |
| E17 | 13–14 | Run of record 217/217, 220 ids, exit 0 | CONFIRMED, pending run of record | f2; `return 0 if battery()["ok"] else 1` (l.5400) |
| E18 | 14–15 | Self-test raw path | CONFIRMED, pending commit | — |
| E19 | 16 | "Route as given" | CONFIRMED | RESULTS.md, coordinating close on e48c7d0 |
| E20 | 16 | Section N for n-analyzer, items 6–7 | CONFIRMED | raw §7 "N. n-analyzer"; the N.2 entry's "section N for n-build, items 1–5" |
| E21 | 16–20 | Items 6–7 verbatim as relayed | CONFIRMED | diff against the brief's relay: identical |
| E22 | 17 | Paste block not committed | CONFIRMED | No 2026-11-18 routing file in `git ls-files results/raw` |
| E23 | 17–18 | Wording differs a little from the raw's §7 draft; the PI's block is the record | CONFIRMED | raw §7 items 6–7 vs relay; §7: "your words are the record" |
| E24 | 22 | Item 7 is n-build's wiring; the analyzer reads nothing it changes | CONFIRMED | raw §5.5; no median, match-count or §2-check text in the analyzer (grep) |
| E25 | 24 | PIN-n-27/28/31 stand as registered and are marked accepted | CONFIRMED | Not in the diff; comment above PINS; module docstring |
| E26 | 24–25 | Digest 209d7b46…92f5 → 281c6827…bbe2, from the first draft run's printed value | CONFIRMED | base l.2679, final l.3082; d1 l.116 prints it |
| E27 | 28–29 | Seat: N2-E at the decision f; N1-V, N1-R's 24 and N1-P at the norm-matched point | CONFIRMED | raw l.63 |
| E28 | 30 | Seat: "INDETERMINATE iff … missing or non-finite, or a pause …" | CONFIRMED | raw l.63, verbatim |
| E29 | 31–33 | Incompleteness elsewhere: "+1/2 is N2's own point where the cap binds and d_eq folds into it" | **IMPRECISE** | Note 1 |
| E30 | 34 | Other f's figures are "not computed" where reads are missing | CONFIRMED | raw l.63 |
| E31 | 36 | OPEN-Q6 records it | CONFIRMED | l.2426–2430 |
| E32 | 38 | A read is also unusable where a session's shadow is, or where the TAU/4 row empties its point | CONFIRMED | `build_state` l.2874–2886; `emptied_at` |
| E33 | 39 | "N2's causes name the point: … `pause:N1-V`" | **IMPRECISE** | Note 2 |
| E34 | 40–41 | Point statistics where usable; per-arm statistics on a complete arm only | CONFIRMED | `build_state` |
| E35 | 42 | VERDICTS' figures carry the point causes | CONFIRMED | `state_figures` "point_causes", used at l.5346 and l.5356 |
| E36 | 43 | G-LEAK-n's table point by point, agreeing with N2 | CONFIRMED | `gleak_table` `needs()` via `named_at` |
| E37 | 44–45 | §5.3: each figure carries its CI and the words; the sign enters no N2 outcome | CONFIRMED | raw l.65 (paraphrase; observation 3) |
| E38 | 46–47 | §5.4 quotation | CONFIRMED | raw l.67, verbatim |
| E39 | 48–52 | §5.6: readability, label, "explanation of record" | CONFIRMED | raw l.71; `sentence_dose`; SENT-RULING |
| E40 | 54 | 2,561 evaluations (1,921 at 977b78b) | CONFIRMED | `evaluations()`; f2 TUP-COUNT; v3 self-test raw 1921/1921 |
| E41 | 54–55 | Tallies re-derived in the review raw's §6 | CONFIRMED | R70–R78 |
| E42 | 55 | Reachability unchanged: 28, 25, 24, 17 | CONFIRMED | f2 l.136–139; v3 self-test raw l.129–132 |
| E43 | 56 | Registered in PINS, strikable until LOCK-n v1.0 | CONFIRMED | l.2292–2295 |
| E44 | 57–59 | PIN-n-33's behaviour | CONFIRMED | `n2_outcome` l.539 (pauses over `n2_reads`); guards' "paused"; N2-GUARD-PAUSE |
| E45 | 59 | Both halves depart from rulings of record | CONFIRMED | 2026-11-16 answers l.33; PROPOSAL l.140; base N2_ARMS and N2-NOT-PAUSED-BY-N1 |
| E46 | 60–61 | §5.3 does not name SPECIFIC's span_reward or SHARED's valence figure | CONFIRMED | raw l.65 |
| E47 | 61–62 | Words close each parenthetical; "… against [c], against the conditioned zone" in SPECIFIC and SHARED | CONFIRMED | C_N2 l.681–691 |
| E48 | 63–64 | PIN-n-35: an input, not a coordinate; 640 more | CONFIRMED | `evaluations()`; 2,561 − 1,921 |
| E49 | 66–67 | N2's floor and slopes, reported only, stay per arm | CONFIRMED | ADDENDUM-n1 §7.5 "(reported only)"; `floors_N2` and `slopes_N2` computed only on a complete arm |
| E50 | 68–69 | A slope with no common session marks its arm, not its points; the row now decides N2 | CONFIRMED | `arm_emptied` (N1-V l.2943, N1-R l.2966); VD-SENSITIVITY literal (INDET, INDET, SHARED, PASS, PASS) passes in f2; base marked N1-R per arm |
| E51 | 70 | INDETERMINATE N2 reports no beside, as at 977b78b | CONFIRMED | Both versions' return |
| E52 | 72–74 | §5.2 reverses §1.6 (quotation) | CONFIRMED | 2026-11-16 answers l.33, verbatim |
| E53 | 74–75 | Guards depart from n:140 as 977b78b read it | CONFIRMED | PROPOSAL l.140; base N2_ARMS |
| E54 | 77–79 | F4 facts | CONFIRMED | D_FOURTH keyed on gr alone (l.759–760); A6 form "(N4 [n4])" |
| E55 | 82 | Frozen at 51396daf…fc41 (217/217) | CONFIRMED | shasum; d2 217/217; d2's check texts are the frozen copy's ("four cases") |
| E56 | 83–85 | F1 MINOR, F2–F8 NOTE, no MAJOR; B1–B2 MINOR, B3–B7 NOTE; 35 mutants, 8 predicted survivors | CONFIRMED | report.md |
| E57 | 87 | F1 to the seat; PIN-n-33 quotes both rulings | CONFIRMED | l.2377–2385 |
| E58 | 88 | F2, F3, F7, F8 registered | CONFIRMED | PIN-n-36, PIN-n-34 |
| E59 | 89 | F5, F6 fixed (OPEN-Q3, OPEN-Q6, comment above OPEN, two docstrings) | CONFIRMED | frozen→mutant-base hunks |
| E60 | 90 | F4 to the seat | CONFIRMED | — |
| E61 | 91–93 | B1–B7 fixes as listed | CONFIRMED | frozen→mutant base: 15 hunks, all accounted for |
| E62 | 94 | M01–M35 the reviewer's; M36–M54 19 of Code's | CONFIRMED | headers_v (35), headers_c (19) |
| E63 | 94–96 | Ran on 285c6168…87db (217/217); 54/54; the 8 predicted survivors killed by added or extended checks | CONFIRMED | f2; kill lists of M08, M12, M14–M18, M24 |
| E64 | 97–100 | Committed bytes differ from the mutant base: repository line, seven texts, one comparand | CONFIRMED, pending commit | 10 hunks: exactly those |
| E65 | 103–104 | Run conditions | NOT CHECKABLE | Scripts use `nice -n 19 … -I`; the battery uses TemporaryDirectory |
| E66 | 105 | Draft: 214/217 then 217/217; the digest and one old form string | CONFIRMED | d1 [FAIL]: SENT-CODE-FORMS, RD-GREAD-MIXED, coverage; d2 |
| E67 | 106–107 | 215/217 (+d_20, never re-computed), then 217/217 | CONFIRMED | f1 fails "empties N1-R at +d_20"; schema DOSE_RULE_LABELS ("0","+1","-1"); f2 |
| E68 | 107 | Batches of five | NOT CHECKABLE | — |
| E69 | 108 | Run of record: 1 | CONFIRMED, pending run of record | — |
| E70 | 110–111 | Q-F3 ran beside; no other window open | NOT CHECKABLE | — |
| E71 | 112–113 | Committed by path; not pushed | CONFIRMED, pending commit | — |
| E72 | 113–114 | Next | CONFIRMED | Matches 977b78b's Next |

**Note 1 (E29; also A4).** The caveat names one of two cases where +1/2 is N2's own point.
- **The missing case:** d_20 folding into +1/2 without the cap. N2 is then decided at f = 0.20 at d_20's resolved point (`norm_matched`, l.343–346). An N1-R gap at +1/2 is then in N2's own reads and makes it INDETERMINATE.
- **The battery already pins this map.** NUM-REACH-CLASS uses `DoseMap(0.25, 0.5)`, "d_20 at +1/2 is (a)" (l.4844–4847).
- **The right form already exists:** `map_reach`'s docstring says "wherever its point is not +1/2".
- **Suggested wording:** "+1/2 is N2's own point where d_20 folds into it, or, when the cap binds, d_eq does".

**Note 2 (E33).** A pause cause names its arm only. PIN-n-36 says so: "and a pause by its arm ('pause:N1-V')". Suggested wording: "name the point (`incomplete:N1-P@+d_20`, `shadow:N2-E@f0.20`), a pause its arm (`pause:N1-V`)".

##### 2. Close line (`SCRATCH/raw/close_977b78b.filled.md`)

| ID | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| C1 | 1 | PI date; n-analyzer's line per the raw's header and §7 item 6 | CONFIRMED | raw l.3 ("the n-build, n-analyzer and coordinating sessions add their close lines"); l.90 |
| C2 | 1–2 | Ruling on PIN-n-27..32 and F11 carried in | CONFIRMED | diff |
| C3 | 2–5 | Path, full sha256, 26cf7d2 | CONFIRMED | shasum; git show --name-status |
| C4 | 6 | §5 rules "this entry's six readings and F11" | CONFIRMED | RESULTS.md l.509–623: PIN-n-27..32 flagged, plus F11 |
| C5 | 6–7 | Routed as section N's item 6; item 7 to n-build | CONFIRMED | relay; raw §7 |
| C6 | 7–8 | Both items quoted verbatim in the carrying commit's entry, their record | CONFIRMED, pending commit | entry l.19–20 |
| C7 | 10 | Item 6 carried; 9e75f3f7…62e1 | CONFIRMED, pending commit | shasum |
| C8 | 10–11 | PIN-n-27/28/31 stand | CONFIRMED | not in the diff |
| C9 | 11–12 | 29 and 32 re-registered as amended; 30 accepted with its sentences amended | CONFIRMED | l.2349–2376 |
| C10 | 12 | Fourth form in the sentence layer | CONFIRMED | `sentence_dose` l.752ff |
| C11 | 13 | Digest moved (§5.1) | CONFIRMED | E26 |
| C12 | 13–14 | Item 7 n-build's; the analyzer reads nothing it changes | CONFIRMED | E24 |
| C13 | 14–15 | PIN-n-33..36 flagged in this commit's entry, with two questions | CONFIRMED, pending commit | — |

##### 3. Review raw (`SCRATCH/raw/review.md`)

| ID | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| R1 | 1 | Title | CONFIRMED | — |
| R2 | 3 | Raw for the entry (title prefix) | CONFIRMED | — |
| R3 | 5 | 977b78b, 97097ce0…251e | CONFIRMED | — |
| R4 | 6–7 | Path, 5843a9bd…7165, 26cf7d2 | CONFIRMED | — |
| R5 | 8–13 | What changed, by section | CONFIRMED | base→final diff |
| R6a | 14 | 214/217, then 217/217 | CONFIRMED | d1, d2 |
| R6b | 14 | "Drafted in one step", in a granted window | NOT CHECKABLE | — |
| R7 | 15–16 | Frozen read-only at 51396daf; 217/217; 220 ids | CONFIRMED | r--r--r--; d2 |
| R8 | 17–18 | Subagent; brief quoting the list of record v2 items 1–5; no Python | CONFIRMED | `review/BRIEF.md` |
| R9 | 19–20 | Its spec | CONFIRMED | BRIEF.md "The specification" |
| R10 | 21 | Executed no code; opened nothing under data/ | NOT CHECKABLE | Report says only "I ran no Python, edited nothing and wrote no file" |
| R11 | 22–24 | Findings, severities, V01–V35, the 8 named survivors | CONFIRMED | report.md |
| R12–R15 | 26–30 | F1 / registered / fixed / F4 kept | CONFIRMED | PINs, OPEN, docstrings |
| R16 | 31–32 | Two cases added after the freeze | CONFIRMED | Both are in the frozen→mutant-base diff |
| R17 | 33 | M01–M35 = V01–V35 verbatim | CONFIRMED | 70 split blocks from report.md, each cmp-equal to `mutants/Mnn.old/.new` |
| R18 | 33–34 | 19 of 39; 20 dropped as overlapping (§3 names them) | CONFIRMED | `mutants_c.spec`: 39; timing not checkable |
| R19 | 34–35 | Ran once on 285c6168 (217/217); 54/54 | CONFIRMED | f2; .out files |
| R20 | 35–36 | The 8 each killed by an added or extended check | CONFIRMED | R57 |
| R21 | 37–38 | Repository line + seven texts + one comparand | CONFIRMED, pending commit | — |
| R22 | 39 | §6 is the derivation `_bt_expected_tallies` cites | CONFIRMED | l.1876 |
| R23 | 41–42 | Run conditions; nothing on a model or box | NOT CHECKABLE | — |
| R24 | 43–44 | Fresh copy; exact replacement asserted once; killed = non-zero exit | CONFIRMED | `run_mutants.sh` (perl dies unless count == 1); each `out/Mnn.py` differs from the base by one hunk inside .old/.new |
| R25 | 46–400 | Report saved; 2104634c…acb4; headings moved down two levels; nothing else changed; frozen-copy line numbers | CONFIRMED | §1 with `####`→`##` equals report.md but for the final newline; line numbers spot-checked (518–522, 539–541, 548, 760–761, 1859, 1935–1936, 2358–2363, 2382–2401, 2793–2794, 2866–2868, 2910, 2935, 2928). "By script" not checkable |
| R27–R28 | 406–416 | F1: quotations; Code does not choose; PIN-n-33 quotes both; the entry asks | CONFIRMED | Verbatim against the 2026-11-16 answers l.33 and PROPOSAL l.140 |
| R29–R35 | 417–435 | F2–F8 dispositions | CONFIRMED | ADDENDUM-n1 §7.5; PIN and OPEN texts; docstrings |
| R36 | 439–441 | B1 | CONFIRMED | `want_nc` logic; pw1 beside check |
| R37 | 442–446 | B2: two campaigns; +1 and the arm marked; N2 decided; L elsewhere; +1 row not computed, naming tau4-emptied:N1-R@+1 | CONFIRMED | pw4, pw5 checks |
| R38 | 447–449 | +d_20 cannot be emptied (DOSE_RULE_LABELS); 215/217; N2-POINT-CAUSES's literal | CONFIRMED | True of the reviewer's form (observation 4) |
| R39–R42 | 450–455 | B3 literal tuple; B4 seven sentences; B5 order; B6 twenty keys | CONFIRMED | keys1 = 5+5+4+6 |
| R43 | 456 | B7 cites this raw | CONFIRMED, pending commit | — |
| R44 | 460–461 | Fifth refusal case; the frozen copy refused in both places, checked only the set's | CONFIRMED | Frozen l.755 and l.818 raise; SENT-REFUSES had four cases (d2 l.115) |
| R45 | 462 | RD-POINTWISE, N1-P at −1 | CONFIRMED | pw4; timing not checkable |
| R46 | 466–467 | M01–M35 applied as written; 19 reproduced whole | CONFIRMED | — |
| R47 | 467–468 | Dropped to keep the window near 90 minutes | NOT CHECKABLE | Reason only |
| R48 | 469 | Ten repeat V02, V09, V16, V19, V20, V21, V25, V33, V34, V35 | CONFIRMED | M104, M108, M120, M117, M118, M116, M125, M128, M130, M134 |
| R49 | 470–472 | Eight on the lines of V01, V06/V07 (two), V11, V13, V29 (opposite way), V30, V32 | CONFIRMED | M105, M102, M103, M115, M113, M124, M122, M121 |
| R50 | 473–474 | Two, on another line, as V03 and V28 | CONFIRMED | M106, M123 |
| R51 | 476 | All 39 in scratch; each old text asserted once | CONFIRMED | spec has 39; runner assertion covers the 54 run |
| R52 | 478–480 | Base read-only at 285c6168…f987db; 217/217, 220 ids; all killed | CONFIRMED | Batch mechanics not checkable |
| R53 | 482–484 | Table legend | CONFIRMED | l.4629–4630 `sorted(...)[:6]` |
| R54 | 486–541 | The 54-row table | CONFIRMED | = `kill_table.md`; cols 1–5 = `headers_all.txt`; From column right; Result = lists rebuilt from the .out files incl. group exceptions; = `kills.txt` |
| R55 | 543–544 | Fifteen runs with a group exception | CONFIRMED | M05, 11, 13, 16, 19, 20, 21, 35, 36, 40, 42, 43, 48, 51, 54 |
| R56 | 545–571 | Each run's details | CONFIRMED | e.g. M05: 5 FAILs then 'causes', RD-SHADOW then 0.625; M11 rand_07 +1/2; M13 run 100; M42 run 17; M16 ('rand_00','+1'); M36: no-raise + four shapes + pinned map; M54: (a), (b), REACH-FOURTH, with (c) and (d) PASS |
| R57 | 573–581 | Killers of the 8 survivors | CONFIRMED | — |
| R58 | 583–700 | Code's mutants, whole | CONFIRMED | Blocks cmp-equal to M36–M54 and their `mutants_c` originals |
| R59 | 704–706 | Runs on the working copy; frozen after each run, unchanged | CONFIRMED | INVOCATION lines; work file = mutant base; d2/f2 texts match frozen/base |
| R60 | 708–713 | Draft window details | CONFIRMED | d1, d2 |
| R61 | 714–717 | Mutant window details | CONFIRMED | f1, f2 |
| R62 | 718–719 | Batches; M51–M54 last; one tool call each | NOT CHECKABLE | — |
| R63 | 720 | Run of record | CONFIRMED, pending run of record | — |
| R64 | 722–723 | Q-F3 and windows | NOT CHECKABLE | — |
| R65 | 727 | Ten hunks | CONFIRMED, pending commit | — |
| R66 | 729–734 | Repository line, "as the committed analyzer always has" | CONFIRMED | Same line at 5c0ae6b, 2822721, bedc198, 977b78b |
| R67 | 735–746 | Seven texts as described | CONFIRMED | Accurate description of each hunk (the PIN-n-29 text itself: Note 1) |
| R68 | 747–749 | The comparand; before, the copy was read for its figure alone | CONFIRMED | — |
| R69 | 751–752 | No outcome, sentence or form change; digest unchanged; run covers the comparand | CONFIRMED, pending run of record (last sentence) | No form text in any hunk |
| R70–R78 | 756–797 | §6 tallies (parts; four groups 512/512/768/768; 2,560/2,561; 1,921; 7.1, 7.2, 7.3, N4, NOT-RUN; "a third more" except as listed) | CONFIRMED | Every product and sum redone; equals `_bt_expected_tallies`; f2 TUP-T10 PASS |

##### 4. Analyzer texts (`SCRATCH/final/n_analyze.py`)

| ID | Lines | Text | Verdict | Evidence |
|---|---|---|---|---|
| A1 | 16–21 | Module docstring | CONFIRMED | 7–26 accepted (11-16 §2); 27–32 ruled 11-18 §5 |
| A2 | 2292–2295 | Comment above PINS | CONFIRMED | — |
| A3 | 2409–2411 | Comment above OPEN | CONFIRMED | — |
| A4 | 2349–2356 | PIN-n-29 | **IMPRECISE** | Otherwise follows raw l.63; the +1/2 caveat is incomplete (Note 1) |
| A5 | 2357–2365 | PIN-n-30 | CONFIRMED | `above()` unsigned; against → FOURTH, CI including 0 → MOVE_NC |
| A6 | 2372–2376 | PIN-n-32 | CONFIRMED | raw l.67 |
| A7 | 2377–2385 | PIN-n-33 | CONFIRMED | Quotations verbatim; schema `arms_in_scope` |
| A8 | 2386–2392 | PIN-n-34 | CONFIRMED | C_N2 |
| A9 | 2393–2396 | PIN-n-35 | CONFIRMED | — |
| A10 | 2397–2408 | PIN-n-36 | CONFIRMED | Observation 5 |
| A11–A14 | 2417–2437 | OPEN-Q3, Q4, Q6, Q8 | CONFIRMED | — |
| A15–A19 | 642–649 | ZONE_WORDS, MERGE_NOTE, FOURTH, READABLE, NOT_READABLE | CONFIRMED | Rebuilt by sed: cmp-equal to the raw's strings, each a single grep -F hit in the raw |
| A20 | 681–692 | C_N2's three forms | CONFIRMED | With [CIE] (where new), [CIV], [zoneE], [zoneV] removed, they equal base l.611–619. SPECIFIC with [zoneV] → "[, against the conditioned zone]" contains §5.3's clause |
| A21 | 1006 | `_ORC_NOTE` | CONFIRMED | Byte-equal to raw l.67, and to DEQ_FIGURE + MERGE_NOTE |
| A22 | 1007–1010 | `_ORC_FOURTH` | CONFIRMED | = FOURTH = raw |
| A23 | 1605–1606 | `spec_v` | CONFIRMED | = raw l.65, its "…" dropped |
| A24 | 1608, 1619–1620 | SENT-RULING's zone-words and READ_ALT literals | CONFIRMED | Byte-equal to the raw |
| A25 | 635–641 | Comment above the seat's forms | CONFIRMED | — |
| A26 | 678–680 | Comment above C_N2 | CONFIRMED | — |
| A27 | 1003–1005 | Comment above the oracle's copies | CONFIRMED | A slip in the fourth form or the figure fails T2; a slip in the note's words fails SENT-RULING |
| A28 | 526–535 | `n2_outcome` docstring | CONFIRMED | — |
| A29 | 2843–2858 | `build_state` docstring | CONFIRMED | "Only if" is right; complete = usable and not shadow |
| A30 | 2822–2824 | `delta_m` docstring | CONFIRMED | Every `dm()` call is under `usable_at` |
| A31 | 1950–1956 | `map_reach` docstring | CONFIRMED | — |
| A32 | 753–755 | `sentence_dose` docstring | CONFIRMED | — |
| A33 | 806–812 | `sentence_set` docstring | CONFIRMED | — |
| A34 | 1876–1879 | `_bt_expected_tallies` docstring | CONFIRMED, pending commit (cited raw) | Arithmetic checked |
| A35 | 3057–3059 | `merge_text` docstring | CONFIRMED | Mirrors `value_text` |
| A36 | 1683–1685 | SENT-CODE-FORMS's description | CONFIRMED | 42 forms = 38 + 4 RULING_FORMS |

##### 5. Pass-1 dispositions, checked

Each is applied as stated and is accurate, with three qualifications: P3, P13 and P16.

- **P1, R17 FAIL (with R44).** Applied in the head (l.33–35) and §3 (l.466–476). I re-derived the classification from `mutants_c.spec` and it is right (R48–R50). The 19 kept (M101, M107, M109–M112, M114, M119, M126, M127, M129, M131–M133, M135–M139) are each byte-equal to M36–M54.
- **P2, E14.** Applied (entry l.11–12).
- **P3, E25.** Applied: the seat's ruling and Code's carrying are now split. However, the seat's-ruling bullet now also holds Code's +1/2 caveat, added for observation 4 (see P13 and observation 2).
- **P4, E42.** Applied (entry l.61–62; PIN-n-34).
- **P5, E54.** Applied (entry l.89).
- **P6, R35.** Applied (review l.445).
- **P7, R42.** Applied (review l.461).
- **P8, A8.** Applied (PIN-n-34; PIN-n-30 also says "carries").
- **P9, A23.** Applied (l.638–641).
- **P10, A24 with observation 2.** Applied (l.1003–1005, l.1615). The new comparand holds byte-for-byte.
- **P11, A26.** Applied (l.2851, 2854–2855).
- **P12, observation 3.** Applied (l.1683–1685).
- **P13, observation 4.** Applied as stated (PIN-n-29 l.2352–2354; entry l.31–32). The caveat is incomplete: Note 1, E29, A4.
- **P14, observation 5.** Same as P3.
- **P15, observation 6.** Applied (entry l.17–18).
- **P16, observation 7.** Applied in the entry (l.6) and the close line (l.5). The review raw's l.478 still has a full hash inline (observation 6 below).
- **P17, observation 8.** Applied: the close line no longer quotes items 6–7 and points to the entry instead.
- **P18, observation 9.** Left as is, which is justified: §1 is the report verbatim (verified).
- **P19, observation 10.** Applied (l.678–680).
- **P20, "bytes after this pass".** Confirmed: 9 hunks plus the repository line, 10 in all. No form text in any hunk; the digest line is unchanged.
- **P21, pass-1 tally.** 170 claims (150/11/1/8) and ten observations: matches `pass1.md`.

##### Counts

| Text | Claims | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|---|
| Entry | 72 | 66 | 2 | 0 | 4 |
| Close line | 13 | 13 | 0 | 0 | 0 |
| Review raw | 78 | 72 | 0 | 0 | 6 |
| Analyzer | 36 | 35 | 1 | 0 | 0 |
| **Total** | **199** | **186** | **3** | **0** | **10** |

CONFIRMED includes 5 claims pending the run of record (E3, E17, E69, R63, R69) and 11 pending the commit (E8, E18, E64, E71, C6, C7, C13, R21, R43, R65, A34). All 21 pass-1 dispositions are applied as stated.

##### Observations

1. **Fixing PIN-n-29 has knock-on edits.** If Note 1 is fixed in PIN-n-29, the analyzer's bytes change. Then these must move: the sha256 in the entry (l.6) and the close line (l.10); the review raw §5's "ten hunks" and "seven texts"; and the entry's "seven texts". The change is text only, so f2 still predicts the run of record, but the run must use the re-edited bytes.
2. **Attribution in the entry's §5.2.** The bullet headed "The seat's ruling" carries Code's caveat. The marker "(the seat's examples, …)" covers only the examples.
3. **§5.3 paraphrase.** Entry l.44–45 renders the seat's "each movement carries its figure, its CI and…" as "each figure carries its CI". Its PIN-n-34 bullet then says §5.3 does not name two of those figures. A reader may not tell whether that extension is ruled or read. Possible wording: "each movement (each figure, PIN-n-34)".
4. **"+d_20 cannot be emptied".** This holds for the reviewer's form: shifting +d_20's own reads, which are never re-computed. The same holds for the pw5 comment (l.3510, "so no point but those can be emptied"). Strictly, per PIN-n-16 "a shadow that exceeds drops its session's Δm at every dose". So the TAU/4 row can empty every point of an arm at once, +d_20 included, through the d = 0 shadows. "+d_20 alone" would be exact.
5. **"A slope with no common session marks its arm"** (PIN-n-36, `build_state`). This holds for N1-V and N1-R. For an N2 arm, such a slope leaves `slopes_N2` None without marking the arm. In the TAU/4 row this cannot happen: N2's f0.10/f0.20 reads are not dose-rule reads, and sessions leave both f's together through their shadows. No change is needed.
6. **Formatting.**
   - `_bt_expected_tallies` l.1877 is 135 characters; the B7 edit was not re-wrapped to the file's 120.
   - Review raw l.478 has the full mutant-base hash inline (159 characters), the case observation 7 fixed in the entry and close line.
7. **Stale scratch file.** `SCRATCH/review/dispositions.md` still has the pre-pass-1 wording: "takes G-LEAK-n's +1 row out" and "refused it in the set only". The review raw §2 has the corrected text. The file is not committed, so this matters only if it is reused.
8. **The departure in Method** (the unscoped `git ls-files`) is disclosed for the record.

### Code's dispositions of pass 2

Pass 2: 199 claims; 186 CONFIRMED, 3 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE; eight observations. It found every one of
pass 1's 21 dispositions applied as stated. With no FAIL it is the last pass, as at v3: its three IMPRECISE and
observations 1–4, 6 and 7 are applied, and each edit after it is checked by tool rather than by a third pass.

#### The IMPRECISE

- **E29 and A4 (its note 1), the +1/2 caveat.**
  - PIN-n-29 now says "+1/2 is N2's own point where d_20 folds into it, or d_eq does when the cap binds", labelled
    Code's note.
  - The entry carries it as Code's note, after the seat's-ruling sentence and outside it (observation 2).
- **E33 (its note 2), a pause's cause.** The entry now says N2's causes name the point, and a pause its arm.

#### Observations

1. **The knock-on edits.** The analyzer's bytes changed again: twelve hunks against the mutant base, which are nine
   texts and one comparand. The entry, the close line and the review raw's §5 carry the new hash and count; the
   hashes are filled by script.
2. **Attribution in the entry's §5.2:** as E29.
3. **§5.3's paraphrase.** The entry now says each movement carries its figure, its CI and the words, and that Code
   carries them on every figure of the three forms (PIN-n-34).
4. **"+d_20 cannot be emptied".** Now "alone" in four places: the review raw's §2 and §4, the entry's runs, and the
   comment above the +1 campaign. §2 adds that only shadows above TAU/4, at d = 0, could empty it, and every other
   point of the arm with it (PIN-n-16).
5. **A slope with no common session on an N2 arm.** No change, as the checker says: it cannot occur in the TAU/4 row.
6. **Formatting.** `_bt_expected_tallies`'s docstring is re-wrapped, and the review raw's full mutant-base hash now
   stands on its own line.
7. **The stale scratch file.** The scratch dispositions file is brought into line with the raw's §2. It is not
   committed.
8. **The checker's departure.** It ran an unscoped `git ls-files` piped to a name filter. Inside the pipe this listed
   tracked names tree-wide, `data/mf3`'s among them; the filter printed only `results/raw` names. It touched names
   only, no content or metadata, and was momentary. It is disclosed in the entry and to the coordinating session, for
   the seat.

#### Checked by tool after this pass

- **Hashes and hunks.**
  - The final file's sha256 is in the entry in full and in the close line abbreviated (by `cut`).
  - The final file differs from the mutant base in twelve hunks (`diff`).
  - Its CODE_FORMS_SHA256 line equals the mutant base's.
- **Stale phrases absent** from the entry, the close line, the review raw and the analyzer (`grep -F`): "seven texts",
  "ten hunks", "in one line", "takes G-LEAK-n's +1 row out", "refused it in the set only", "where the cap binds and
  d_eq folds into it", "+d_20 cannot be emptied:", "which the dose rule never re-computes", "no point but those can be
  emptied", and "name the point: `incomplete".
  - The first run of this check found "seven texts" left in the review raw's §5 ("none of the seven texts is a form").
    That is now "nine", and the check was rerun clean.
  - The same first run misquoted one phrase in the shell (the apostrophe of "G-LEAK-n's"). It was rerun with the
    phrase passed in a variable: absent.
- **New phrases present:**
  - the completed caveat, in the analyzer and in the entry;
  - "a pause its arm" and "each movement carries its figure", in the entry;
  - the nine texts, in the entry and the review raw;
  - "twelve hunks", in the review raw;
  - "alone", at the review raw's two places and in the analyzer's comment.
- **Placeholders and formatting.** No placeholder is left. The mutant-base hash stands on its own line. No changed
  line in the analyzer exceeds 120 characters.
