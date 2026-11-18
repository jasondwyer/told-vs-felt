# n_analyze.py, the seat's ruling of 2026-11-18 (second sitting) carried in: the blind values-check, two passes (PI date 2026-11-18)

Code's raw for the entry `n package — scripts/n_analyze.py, the seat's ruling of the second sitting carried in`.

**Who checked what.** Two blind values-checkers checked four texts against their sources, claim by claim:
- the entry;
- the close line on `a84833e`'s entry;
- the review raw;
- the analyzer's new and changed texts: its registers, the seat's forms as transcribed, and the docstrings, comments
  and check descriptions the change touched.

Each checker was a subagent of this session. Its brief quoted the list of record v2's items 1–5 and the standing line
that a git command in a check takes item 3's pathspec, and it allowed no Python.
- The first pass checked the first drafts.
- The second pass checked the drafts as revised after the first, and whether each of the first pass's dispositions
  was carried and is true.
- With no FAIL, the second pass is the last. The edits after it are checked by tool (its dispositions).

**What the passes changed in the analyzer.** The passes changed ten texts in the analyzer, six from the first pass and
four from the second, all after its mutation testing (the review raw's §5). The run of record is on the final bytes.

**Their departures.** Each checker disclosed its own departures, and each report carries them. The entry names them
for the seat to class.

**How the reports appear.** Each report is reproduced whole and followed by Code's dispositions. The reports are the
checkers' hand-back messages, taken from the subagents' transcripts by script. The checkers write SCRATCH for Code's
scratch folder and REPO for the repository.

## Pass 1: the report

BLIND VALUES-CHECK: the n_analyze v5 entry, its close line, the review raw and the analyzer's new texts

I checked the inputs first. The brief hashes to 1a2f8cb1…6e7, as given. The four texts hash as given: entry.filled.md c4ce80ee…44fb, close_a84833e.filled.md d9bd8435…1b1a, review.md ee61d87a…4b4b, final/n_analyze.py 883bff2f…1da1. SCRATCH/base-a84833e.py has the same blob id as REPO's scripts/n_analyze.py at a84833e and at HEAD (251e76be…) and hashes to 509a62ad…85f6. Every abbreviated hash in the three texts was cut by tool from its file and matches: 509a62ad…85f6, 883bff2f…1da1, cdecf39e…01d3, 6f2dd349…301e, 83f54ec6…d04c, cca2acb4…9057, 6010bc30…da87, e2cf9684…d6d0, f7fee979…f6eb, 0ea39600…0db6, 281c6827…bbe2 and 41d0d654…b1da.

Pending, by design: the run of record. I graded it against the mutant base's run (SCRATCH/runs/d3.out). The mutant base differs from the final file only at line 59, the repository line. The commit is pending too. The values-check line is a placeholder and was skipped.

== 1. The entry (SCRATCH/raw/entry.filled.md): 61 claims ==
E1 l.1–3: the title and rulings (PIN-n-33 amended, the label in the sentence, PIN-n-34 to -36 accepted; §3; item 6). CONFIRMED. The seat raw has §3.1–3.3 and §6 item 6, and the relayed item 6 agrees.
E2 l.3: Battery 222/222. CONFIRMED, pending the run of record. d3.out shows 222/222.
E3 l.3–4: 49 of 50 mutants killed. CONFIRMED. kills.txt and the 50 outputs: 49 show fewer passes than 222, and V03 shows 222/222.
E4 l.4–5: PIN-n-37 is Code's reading, flagged. CONFIRMED. The PINS header says "PIN-n-37 declared since, strikable".
E5 l.5: Model-free; nothing ran on a model or the box; no stage ran. NOT CHECKABLE. It is consistent with the scripts, which run --selftest only.
E6 l.6–8: the full sha256, and 509a62ad…85f6 at a84833e. CONFIRMED by shasum and git rev-parse.
E7 l.9–10: the schema pin (d791bd9), the bound files and the commands are unchanged. CONFIRMED. No diff hunk touches the pins or main(). SCHEMA_SHA256 0ea39600…0db6 is commented "# d791bd9", and the schema blob is equal at d791bd9, at HEAD and in the worktree. PROPOSAL and ADDENDUM shas equal the files.
E8 l.11–13: the seat raw's path, cdecf39e…01d3, committed at dc6a1cf, cited by path. CONFIRMED. git log --diff-filter=A gives dc6a1cf, the blob is unchanged since, and the path is in the docstring, the PINS/OPEN comments, the forms comment and PIN-n-33.
E9 l.14–15: "§3.2's words are therefore transcribed twice, once in the module and once in the oracle". IMPRECISE. The battery hook does bar results/raw (d3.out's hook line), but there are more than two copies. SENT-FILLED-DOSE-FOURTH's literal tails (final l.1784–1785) and SENT-FOURTH-FILLS's want_e (l.1814–1815: " — answered", " — concluded, not answered (N4 …)") are further copies. Suggest "…and again in the battery: its oracle (_ORC_TAIL, _ORC_N4) and the literal-text checks' filled tails".
E10 l.15: the review and the values-check held both copies to the raw. CONFIRMED. The report's §3.2 checks were done "character for character". This check compared bytes: LABEL_TAIL " e2 80 94 [label]", CNA_N4, _ORC_TAIL and _ORC_N4 equal the raw §3.2 text.
E11 l.16–18: run of record 222/222, 225 ids, exit 0, raw v5_selftest.txt. CONFIRMED, pending. d3.out shows 222/222 and 225 ids. main returns 0 only if the battery reports "ok". commit_steps.sh names that raw.
E12 l.19–21: the routing is recorded here; its wording differs from the seat's §6 draft; the PI's block is the record. CONFIRMED. The seat's §6 item 6 reads "(pauses point by point); the fourth form's label in the sentence". Its §6 header says "your words are the record". dc6a1cf's subject cites "Route as given".
E13 l.22: item 6, verbatim. CONFIRMED. cmp against the brief's relay is identical.
E14 l.24–26: the first standing rule. CONFIRMED against seat §4 ("a window names the bytes it runs by sha256…").
E15 l.26: "Every run below ran on bytes named to it first." NOT CHECKABLE (messages).
E16 l.27: the pathspec line is in both checkers' briefs. CONFIRMED. It is in SCRATCH/review/BRIEF.md and in this brief. If "both" means two values-check passes, the second brief does not exist yet.
E17 l.30–31: §3.1 names the reads N2 uses: N2-E at the decision f; N1-V, N1-R's 24 and N1-P at the norm-matched point. CONFIRMED against seat §3.1.
E18 l.32–33: other reads (N1-V at −1, an N1-R cell elsewhere) leave N2 decided, superseding §1.6. CONFIRMED against §3.1.
E19 l.34–35: the guard half stands. CONFIRMED. §3.1 says "its second half stands". The code's guards use bool(st.paused.get(a)) (l.573).
E20 l.36: paused_on reads one point; n2_outcome takes its causes there. CONFIRMED (l.437–441, 553).
E21 l.37: "The battery's literal states read a pause at every point of its arm, as before." IMPRECISE. This holds only for literal states with paused_at None, the default (l.1215–1221). N2-PAUSE-POINTWISE builds literal states with paused_at={(arm, key): True} (l.1419), so those read a pause at one point.
E22 l.38: N1, dose and N4 per arm. CONFIRMED. _causes uses st.paused.get (l.463) for N1 (l.479) and N4 (l.582); dose is INDETERMINATE through N1.
E23 l.39: the fourth form ends " — [label]", as A.2 and A.7 do. CONFIRMED. See §3.2, F4 + LABEL_TAIL, and C_N1_NOT_REPLICATED and C_N2's SPECIFIC/NULL, which end the same way.
E24 l.41–43: the three fills. CONFIRMED against §3.2, sentence_dose l.786 and label() l.734–739.
E25 l.46: SENT-FILLED-DOSE-FOURTH now has eight sentences. CONFIRMED: 4 forms × 2 shapes (base: six).
E26 l.47–48: SENT-FOURTH-FILLS reads 640 evaluations: 64, 256, 320. CONFIRMED. The code checks it, d3.out l.120 passes, and the outcome-space line gives 128×4 + 32×4 = 640.
E27 l.49–50: the digest 281c6827…bbe2 → 41d0d654…b1da, set from the first run's printed value. CONFIRMED. d1.out l.117 prints 41d0d654…, and d1 and d2 differ only in that pin.
E28 l.51–52: the 2,561 evaluations and the hand tallies are unchanged except the form string. CONFIRMED. d3.out T1–T9 show 2561/2561, and _bt_expected_tallies' only change is f4 in two keys.
E29 l.53–54: PIN-n-34–36 are marked accepted in the header; their texts are unchanged. CONFIRMED. The awk-extracted texts are identical in base and final, and PIN-n-7–32 are identical too.
E30 l.55–56: PIN-n-37 is registered and strikable until LOCK-n v1.0. CONFIRMED.
E31 l.57–61: the points (its read, a rendering pause by its id, the batch's trials, through a shadow every read of the session, within the scope). CONFIRMED against PIN-n-37 and paused_points l.5497–5525.
E32 l.63: N1's and N4's pauses stay per arm. CONFIRMED.
E33 l.64–65: the extension is Code's, capped; the runner's SCOPE applies its shadow clause to the fired read alone. CONFIRMED by runner.py SCOPE pin l.30–32 and _scope l.290–296.
E34 l.65–66: "so a binomial fire whose batch holds floor shadows does not scope N1-R". IMPRECISE. _scope adds the fired read's own shadow clause and every arm with a trial in the batch. A fire whose read is itself a floor shadow, or whose batch holds an N1-R trial, does scope N1-R. The claim holds only for N1-R reached through the batch's floor shadows.
E35 l.66: it went to n-build as information and is applied nowhere. NOT CHECKABLE (message).
E36 l.66: no outcome changes today. CONFIRMED, consistent with the reviewer's F5 scenario: N1 is INDETERMINATE through N1-V, and N1-R is incomplete at read 159.
E37 l.67: the two alternatives are named. CONFIRMED against PIN-n-37.
E38 l.67–69: launch order plus cadence means a first batch stands on every read of its scope's arms. CONFIRMED. The ORDER pin puts the shadows first, n §2.1 says "cadence every 160 reads", and Monitors' next_due starts at the cadence.
E39 l.70–76: what the reader binds, and the plan rule. CONFIRMED (report_problems l.5399–5423).
E40 l.77: the reading of PIN-n-24's per-arm clause. CONFIRMED. PIN-n-24 l.2426–2427 holds the clause, and PIN-n-37 holds the reading.
E41 l.78–79: the beside's `paused`, its figures computed, and `pause_points`. CONFIRMED (l.571, l.5580–5584).
E42 l.81: the reviewer read 6f2dd349…301e (221/221). CONFIRMED. That is the review copy's sha (= d2), the copy is not writable, and d2.out shows 221/221.
E43 l.81–85: no MAJOR; F1 MINOR; F2–F6 NOTEs; B1–B4 MINOR; B5–B7 NOTEs; 34 mutants, 10 predicted to survive; V03 equivalent. CONFIRMED against the report and the spec (10 marked "survives").
E44 l.86–89: dispositions F1–F6. CONFIRMED by dispositions.md and the d2→d3 diff.
E45 l.90–92: B1–B7 "runner-shaped inputs … and six new refusals". IMPRECISE, on two counts.
- The count: VD-REFUSE printed 43 cases at a84833e, 47 in the draft and 50 in the fixed draft. Against the reviewed draft, three refusals are new (batch-start, batch-scope, batch-read-count) and three were rebuilt (batch-end, batch-count, batch-exceedances). Against a84833e, seven are new, pause-not-planned among them.
- "Runner-shaped": see R33.
E46 l.93–94: 34 (five re-expressed) + 16 of Code's ran on 83f54ec6…d04c (222/222): 49 of 50. CONFIRMED.
E47 l.95: V03 survived, equivalent. CONFIRMED (V03.out 222/222).
E48 l.96: the other nine were killed by checks the dispositions added or extended. CONFIRMED by kills.txt: V07 and V08 by N2-PAUSE-POINTWISE; V15 and V24 by VD-PAUSE-RENDERING; V16 by RD-PAUSE-POINTS; V18 by RD and VD-PAUSE-POINTS; V26 and V28 by VD-REFUSE; V27 by VD-PAUSE-POINTS.
E49 l.97: the committed bytes differ from the mutant base in the repository line. CONFIRMED: the diff is one hunk, l.59.
E50 l.100: the windows were granted and the bytes named first. NOT CHECKABLE.
E51 l.101–102: one process at a time, nice -n 19 with -I, temp folders outside the repo, in the foreground. CONFIRMED as far as files show. run_battery2.sh and run_mutants2.sh run `nice -n 19 ./python -I` in sequential foreground loops, and the battery uses tempfile.TemporaryDirectory.
E52 l.102–103: the interpreter was reached by cd into the venv's bin by glob, so no argv named its path. NOT CHECKABLE (see O1).
E53 l.104: the draft had 2 runs, 219/221 then 221/221, the first failing on the moved digest alone. CONFIRMED. d1 failed SENT-CODE-FORMS and the coverage check, whose only unreached id is SENT-CODE-FORMS.
E54 l.105: 1 run of the fixed draft (222/222), then the 50 mutants. CONFIRMED (d3.out; 50 outputs).
E55 l.105: "in four batches". NOT CHECKABLE.
E56 l.105–106: each file was checked against the manifest. CONFIRMED. All 50 mut_pre files match the manifest (e2cf9684…d6d0, 50 lines) under shasum -c, run_mutants2.sh checks before each run, and every output's INVOCATION names its own mut_pre/<id>.py. That it was "named to the coordinating session" is not checkable.
E57 l.106–107: the 48-file manifest was replaced, adding C14 and C15. NOT CHECKABLE. It is consistent with C14 and C15 being last in mutants_c_final.spec.
E58 l.108: the run of record: 1. CONFIRMED, pending (commit_steps.sh's record step runs it once).
E59 l.110–111: Q-F3 ran beside; no other window. NOT CHECKABLE.
E60 l.112–113: the paths committed; not pushed. CONFIRMED, pending the commit. commit_steps.sh's RAWS list, its place step and its gate name exactly these.
E61 l.113: Next, G-ANL-n's canonical run. CONFIRMED, consistent with the module docstring.

== 2. The close line (SCRATCH/raw/close_a84833e.filled.md): 11 claims, all CONFIRMED ==
C1 l.1: PI date; the line is per §5 and §6 item 6. Seat §5 says "close lines on a84833e's entry".
C2 l.2: the ruling on PIN-n-33 to -36 and the two questions. The a84833e entry (RESULTS.md l.349–357) poses two questions, "On PIN-n-33" and "On the fourth form".
C3 l.3–7: path, full sha cdecf39ea8d2…01d3 and dc6a1cf; §3 rules on them.
C4 l.7–8: "Route as given"; item 6. Checked against the relay and dc6a1cf's subject.
C5 l.8–9: the item is quoted verbatim in the entry. Entry l.22 equals the relay (pending the commit).
C6 l.11: 883bff2f…1da1, by shasum.
C7 l.12: PIN-n-33 is re-registered with the guard half. Checked against l.2471–2477 and §3.1.
C8 l.13: " — [label]" in three fills, per §3.2.
C9 l.14: PIN-n-34–36 stand and are accepted. The texts are identical and the header updated.
C10 l.15: the digest moved, as in E27.
C11 l.17–18: PIN-n-37 is Code's and flagged in the entry (entry l.55).

== 3. The review raw (SCRATCH/raw/review.md): 80 claims ==
R1 l.1: the title. CONFIRMED.
R2 l.3: the entry it serves. CONFIRMED; it matches the entry's title.
R3 l.5–8: a84833e and 509a62ad…85f6; carries §3 of cdecf39e…01d3 at dc6a1cf. CONFIRMED.
R4 l.9–13: the four changes. CONFIRMED by the base→final diff.
R5 l.15: 219/221, then 221/221. CONFIRMED (d1.out, d2.out).
R6 l.16–17: a read-only copy at 6f2dd349…301e, 221/221, 224 ids. CONFIRMED. `test -w` fails on it, and d2.out shows 224.
R7 l.18–19: its brief quoted list-of-record items 1–5 and the pathspec line, and allowed no Python. CONFIRMED. Items 1–5 in review/BRIEF.md are string-equal to the source raw's, and the brief has the line and "Run no Python".
R8 l.20–22: its specification. CONFIRMED against review/BRIEF.md.
R9 l.23–25: its conduct (tools, one file written, nothing under data/, no departure). CONFIRMED as the report states it. review/reviewer holds patterns.txt besides Code's saved report.
R10 l.26–30: F1–F6, B1–B7, V01–V34 and the 10 named survivors. CONFIRMED.
R11 l.31–33: B1–B7 "give the battery inputs shaped as the runner writes them … and six new refusals". IMPRECISE, as in E45 and R33.
R12 l.34–36: the set, run once each on 83f54ec6…, 222/222, 225 ids; 49 of 50; V03; nine killed. CONFIRMED. One output per id; that each ran only once is not checkable beyond that.
R13 l.37–38: §4 and §5, the repository line. CONFIRMED.
R14 l.39–40: the tallies are unchanged except the form string. CONFIRMED.
R15 l.42–44: nice -n 19, -I, one at a time, temp outside, foreground. CONFIRMED by the scripts.
R16 l.42–45: windows on bytes named, cd-glob so no argv named the path, nothing on a model or the box. NOT CHECKABLE (O1).
R17 l.47: exact replacement, asserted once. CONFIRMED. I rebuilt all 50 mutated files from the mutant base and their .old/.new texts, and every one is byte-equal. Each .old's first line occurs in exactly one line of the base.
R18 l.48–49: manifest, then a check before --selftest. CONFIRMED (as E56).
R19 l.49: "Killed" means a non-zero exit. CONFIRMED by run_mutants2.sh's rc test and main's return.
R20 l.53–55: the §1 header (saved by script; sha 6010bc30…da87; headings down two levels, nothing else; the frozen copy's line numbers). CONFIRMED. report.md hashes as given. Diffing it, with "## " changed to "#### ", against raw l.57–344 shows nothing. The cited lines (785, 1063–1064, 2414, 2501, 2511, 2519, 2536, 5283, 5384, 1405, 3811, 4449, 4584, 4595, 4706) hold those texts in d2.
R21 l.57–344: the report's checkable facts. CONFIRMED. The brief hash is f7fee979…f6eb. The regenerated base→copy diff has a body identical to the supplied one, 38 hunks. The schema is unchanged since d791bd9, at 0ea39600…0db6.
R22 l.348–349: "None changes an outcome, a sentence or a form on a report the runner writes." CONFIRMED. CODE_FORMS_SHA256 is equal in d2 and d3, and F6 keeps Python's right-associative conditional.
R23 l.353–360: F1's bindings; a cleared batch is "an adjudicated pause's batch with a read", which the runner clears on replay. CONFIRMED (code; runner.py l.422–426).
R24 l.362–363: the draft's conjunct is dropped; the runner fires only at a trial. CONFIRMED. d2's ends-are-trials test is gone, and observe evaluates only when the record has a fidelity (l.190–209).
R25 l.364–366: F2. CONFIRMED.
R26 l.367–370: F3. CONFIRMED.
R27 l.371–372: F4's quote. CONFIRMED against PIN-n-37 l.2508–2510.
R28 l.373–375: F5 in PIN-n-37. CONFIRMED. The route the flag took is not checkable (O4); see also A19.
R29 l.376–377: F6. CONFIRMED.
R30 l.381–386: B1's two cases and `sampled`. CONFIRMED.
R31 l.387–388: two cases already added; fourteen now. CONFIRMED. Both are absent from d2 and present in d3, and I counted 14 cases.
R32 l.389–390: B2. CONFIRMED.
R33 l.391–399: VD-PAUSE-POINTS's three standing batches, "each the runner's". IMPRECISE. Each batch's ends, n, k and scope follow the runner's counting as report_problems binds it. But the runner could not write these fires on their campaigns:
- Under the example identity's p0 = 0 (schema.py l.1562), binom_tail returns 1.0 for x ≤ 0 (runner.py l.75–76), so no fire happens at k = 0.
- B is k = 0 (asserted).
- C is k = 0: camp2 has no read above TAU.
- A's adjudicated first fire is k = 0: its range ends before the only exceedance.
- On ck, the cadence evaluation falls due at N1-P's last −1 read (480 reads after the clear), so the runner would fire A's k = 1 batch there, with a read, not at the run's end.
Suggest "each bound as the runner counts a batch".
R34 l.401–407: "VD-REFUSE adds … batch-end". IMPRECISE. The draft already had a batch-end case (d2 l.4718–4719, an end moved off a trial), now rebuilt. The net new keys are three (47 → 50).
R35 l.408–410: B4. CONFIRMED.
R36 l.411–412: B5. CONFIRMED.
R37 l.413–414: B6; the read-less mid-campaign batch is gone. CONFIRMED (d2's bq).
R38 l.414: "and so is the draft's batch on N1-V's +1 cell alone". NOT CHECKABLE. There is no such batch in d1 or d2 (O5).
R39 l.415–416: B7. CONFIRMED.
R40 l.421–422: five re-expressed; their old text no longer occurs. CONFIRMED. Each original first line occurs once in d2 and zero times in d3.
R41 l.423–425: "nine as drafted (C01, C06, C11, C16, C17, C19, C20, C25, C27)". FAIL. C19's old text in mutants_c.spec is the unparenthesized fill line, and in mutants_c_final.spec the parenthesized one. §3 (l.444–445) says so itself. Only eight are as drafted. Fix: "eight as drafted (…without C19), and C14, C15 and C19 re-expressed".
R42 l.426–427: sixteen dropped, and C13. CONFIRMED.
R43 l.429: five added, C29–C33. CONFIRMED.
R44 l.433: 50 mutants. CONFIRMED.
R45 l.434–436: V01–V34 as written except five. CONFIRMED. The 29 match mutants_v.spec byte for byte, and the 5 match the re-expressed spec.
R46 l.437: Code's sixteen reproduced whole. CONFIRMED. The raw's blocks and headers equal mutants_c_final.spec.
R47 l.438–442: 12 duplicates plus 4 another way, mapped. CONFIRMED. Eleven pairs are byte-identical; C07 and V18 differ only by V18's trailing comment. C03/V12, C05/V20, C18/V29 and C22/V09 act on the same lines with the same effect: label() returns only answered or CNA, so C18 equals V29.
R48 l.443: C13 is covered by V26 and C30. CONFIRMED.
R49 l.444–445: the eleven kept; C14, C15 and C19 re-expressed. CONFIRMED.
R50 l.446: five new. CONFIRMED.
R51 l.448–449: each of the 28 old texts "checked … to occur exactly once in the base". IMPRECISE. They occur once in the reviewed draft (d2), the text they were written on. Six (C12, C13, C14, C15, C18, C19) do not occur in the mutant base, which "the base" names elsewhere in §3.
R52 l.451–452: the base is read-only at 83f54ec6e51c…d04c. CONFIRMED.
R53 l.453: 222/222, 225 ids. CONFIRMED.
R54 l.454–455: the manifest by sha, checked before each run. CONFIRMED.
R55 l.455: once each, one at a time, in four batches. NOT CHECKABLE.
R56 l.456: 49 of 50; V03; nine. CONFIRMED.
R57 l.458–459: the table's semantics (first six unreached ids; group exceptions). CONFIRMED. The battery prints unreached[:6].
R58 l.461–512: all 50 rows. CONFIRMED. The From, Function, What-breaks and Predicted columns match the specs field by field (diff empty). The Result column matches kills.txt and each output's coverage line. kill_table.md equals the table.
R59 l.514–519: the V03 argument and "No battery input holds a scope arm with no point". IMPRECISE. RD-PAUSE-POINTS's "the same batch outside its scope", "a range holding no trial" and "an N4 trial is no shadow" hold N1-V in scope with no point. They test paused_points directly and never reach State.paused_on, which is why V03 survives. Suggest "No input that reaches State.paused_on…".
R60 l.521–523: C20's AnlStop from fill(). CONFIRMED (C20.out l.118; fill raises at l.3259; 213/217). The quote omits the message's leading "STOP: ".
R61 l.525–539: the nine predicted survivors and the checks that killed them. CONFIRMED by the failing case keys. V07 fails ('a','N2-S',f0.10) and ('b','N2-S',f0.20). V08 fails the beside-figure cases. V16 fails the +d_20-to-−1 range, the keyed-sample range and also "a range holding no trial". V18 fails "an N4 trial is no shadow" plus VD-PAUSE-POINTS A and C. V27 fails A, C and B.
R62 l.541–548: the refusal lists per mutant. CONFIRMED against each VD-REFUSE failing line (O6).
R63 l.550–552: C17's cascade. CONFIRMED. batch-count shows 'no exception', the later batch cases show the write-once message, and the line is cut.
R64 l.554–586: the re-expressed blocks. CONFIRMED.
R65 l.588–692: Code's blocks, applied once. CONFIRMED.
R66 l.696–699: the runs ran on runs/d1.py, d2.py and d3.py. CONFIRMED by the INVOCATION lines and the shas. "Frozen": see O9.
R67 l.696–699: the windows, the cd-glob form, nothing on a model or the box. NOT CHECKABLE (O1).
R68 l.702–703: d1 at 219/221; the digest and coverage checks failed; the digest moved as the seat said. CONFIRMED. Seat §3.3 says "The forms' digest moves with §3.2".
R69 l.704–705: the pin was set from the printed value; that was d2's one change. CONFIRMED (the d1→d2 diff is one line). That it was named first is not checkable.
R70 l.706: d2 at 221/221, frozen for the review. CONFIRMED.
R71 l.708–709: d3 at 222/222 and 225 ids; the mutant base. CONFIRMED.
R72 l.710: four batches (12, 12, 12, 14). NOT CHECKABLE.
R73 l.711: the manifest e2cf9684…d6d0, 50 files. CONFIRMED.
R74 l.712–713: 48 files, then 50. NOT CHECKABLE.
R75 l.714: the run of record is the entry's. CONFIRMED, pending.
R76 l.716–717: Q-F3; no other window. NOT CHECKABLE.
R77 l.721: one hunk. CONFIRMED.
R78 l.723–728: the line quoted, "as the committed analyzer always has". CONFIRMED. All five committed versions (5c0ae6b, 2822721, bedc198, 977b78b, a84833e) carry it.
R79 l.732–735: the tallies are a84833e's (v4 review raw §6); the label is not in the key; 64/576. CONFIRMED. The oracle's lb2 is the tally label.
R80 l.737–747: the 640 split by fill (16/48/64 tuples; 64/256/320). CONFIRMED by the arithmetic and d3.out's outcome-space line, 128×4 + 32×4.

== 4. The analyzer's new texts (SCRATCH/final/n_analyze.py): 36 claims ==
A1 l.16–23, the module docstring. IMPRECISE. The PINS clause is right and names the second sitting's raw by path. But the OPEN clause lists only the first sitting's §5 as amending OPEN. OPEN-Q3 (l.2533–2534) and OPEN-Q8 (l.2551–2552) now carry the second sitting's §3.2, and the OPEN header comment names both sittings.
A2 l.2384–2387, the comment above PINS. CONFIRMED (§3.1, §3.3).
A3 l.2521–2523, the comment above OPEN. CONFIRMED.
A4 l.2471–2477, PIN-n-33. CONFIRMED against §3.1, including "supersedes §1.6's sentence" and "its second half stands".
A5 l.2500–2519, PIN-n-37. CONFIRMED.
- The schema says "A pause stands on the arms in its scope".
- The runner's trials are its dose-rule and sample reasons (campaign_order l.129).
- The SCOPE and ORDER pins are as cited.
- n §2.1 gives "cadence every 160 reads" and the 10% keyed sample.
- PIN-n-24's clause is quoted exactly.
A6 l.2530–2534, OPEN-Q3. CONFIRMED.
A7 l.2548–2552, OPEN-Q8. CONFIRMED.
A8 l.650–660, the forms comment. CONFIRMED: §3.2's sha, "as A.2 and A.7 do", the fills, the readability clause.
A9 l.669, LABEL_TAIL. CONFIRMED, byte-equal to §3.2.
A10 l.670, CNA_N4. CONFIRMED, byte-equal to §3.2's italic text.
A11 l.671–674, F4 and RULING_FORMS. CONFIRMED.
A12 l.767, FORM_FOURTH. CONFIRMED. Its three copies (l.767, 1068, 1973) are identical, and no copy of the first sitting's string is left.
A13 l.1027–1036, _ORC_TAIL, _ORC_N4 and their comment. CONFIRMED. V31–V33 died by TUP-T2 among others. SENT-RULING now also compares the label copies, which the comment does not mention.
A14 l.1064–1068, the oracle's fill. CONFIRMED against §3.2.
A15 l.433–435, the State.paused_at comment. CONFIRMED for the default (cf. E21).
A16 l.437–441, the paused_on docstring. CONFIRMED.
A17 l.536–553, the n2_outcome docstring. CONFIRMED.
A18 l.774–778, the sentence_dose docstring. CONFIRMED.
A19 l.5497–5504, the paused_points docstring "(the runner's SCOPE)". IMPRECISE.
- It credits the runner's SCOPE with the shadow extension through any of "those reads", the batch's trials included.
- PIN-n-37 and F5's disposition say that extension through a batch is Code's, capped by the scope; the runner applies its shadow clause only to the read that fired (_scope).
- The docstring has the same words in d2 (l.5375), so F5 did not reach it.
A20 l.5345–5362, the report_problems docstring. CONFIRMED. It names "an adjudicated pause's batch" where the code also requires a read; that cannot matter, since no batch can follow an adjudicated run's-end fire.
A21 l.2957–2966, the build_state docstring. CONFIRMED.
A22 l.5573–5576, the state_figures docstring. CONFIRMED.
A23 l.3375–3391, the _bt_write_campaign docstring. CONFIRMED. The schema's example_record says "sample" marks the keyed sample.
A24 l.1967ff, _bt_expected_tallies: its docstring's 64/576 and f4. CONFIRMED.
A25 l.1406–1435, N2-PAUSE-POINTWISE's description and comment. CONFIRMED against its 10 cases × 2 shapes and their wants.
A26 l.1393–1397, the N2-INDET-pause descriptions. CONFIRMED.
A27 l.3828–3893, RD-PAUSE-POINTS's description and comments. CONFIRMED: fourteen cases.
A28 l.4487–4563, VD-PAUSE-POINTS's description and comment. IMPRECISE.
- "the runner's" holds in the binding sense only (see R33).
- C's "the same": ok_pp["C"] checks the tuple's first three coordinates, N1's causes and the points, not N4's causes or the TAU/4 row, which A's check covers.
A29 l.4586–4601, VD-PAUSE-RENDERING. CONFIRMED.
A30 l.4697–4867, VD-REFUSE's description and comments (B7, PIN-n-37's inputs). CONFIRMED.
A31 l.1688–1699, SENT-RULING. CONFIRMED.
A32 l.1796–1800, SENT-FILLED-DOSE-ND: three forms, eight sentences. CONFIRMED.
A33 l.1801–1807, SENT-FILLED-DOSE-FOURTH: three fills, eight sentences. CONFIRMED.
A34 l.1811–1825, SENT-FOURTH-FILLS. CONFIRMED.
A35 l.1113 and _REQ, EXPECTED_CHECKS 222 and 225 ids. CONFIRMED. That is 217 + 5 checks and 220 + 5 ids (the v4 self-test raw has 220).
A36 l.3199, CODE_FORMS_SHA256. CONFIRMED (E27).

== Counts ==
| Text | Claims | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|---|
| Entry | 61 | 49 | 4 | 0 | 8 |
| Close line | 11 | 11 | 0 | 0 | 0 |
| Review raw | 80 | 67 | 5 | 1 | 7 |
| Analyzer | 36 | 33 | 3 | 0 | 0 |
| All | 188 | 160 | 12 | 1 | 15 |

== Observations ==
O1. Battery scripts.
- SCRATCH holds two battery scripts. run_battery2.sh uses the cd-glob form. run_battery.sh is v4's script, re-pointed only to v5's folder, and it names the interpreter by absolute path in argv.
- d1–d3.out cannot tell which script ran them: INVOCATION prints sys.executable, which is resolved either way.
- The entry's and the review raw's "no argv named its path" rest on run_battery2.sh having run all three. Code should confirm this from its transcript, or disclose.
- The mutant runs are settled: every output names its mut_pre file, which is run_mutants2.sh's input.
O2. The analyzer binds a standing batch's extent, n, k and scope, not the runner's evaluation schedule or fire condition. It therefore accepts VD-PAUSE-POINTS's A, B and C, which the runner could not write on those campaigns (R33). Where the texts say "shaped as the runner writes them" or "each the runner's", the truth is narrower: these are batches as the runner counts them.
O3. Review raw §2 (C19 "as drafted") contradicts §3 (C19 re-expressed); the specs side with §3 (R41).
O4. The entry says the SCOPE point "went to n-build as information". The review raw's §2 F5 says it was "sent to the coordinating session for n-build and the seat". PIN-n-37 says "(flagged to n-build)". None of the three is checkable, and the entry and the raw describe the route differently.
O5. "The draft's batch on N1-V's +1 cell alone" (R38) is not in the reviewed draft or d1. C15's as-drafted prediction, "(N1-V's +1 batch, k = 0)", points to a working state not kept in SCRATCH. Say so, or strike it.
O6. C14's printed refusals include batch-read-count. It failed on the write-once message ("N-pod_secondary.json exists with other bytes"), the same cascade the raw explains only for C17, not as a direct catch.
O7. §1's "(sha256 6010bc30…da87)" follows "the subagent's transcript" but is report.md's digest; this matches the v4 raw's form.
O8. runs/d1.py–d3.py are called "frozen copies" but are writable. Their digests match what the raw says. Only the review copy and the mutant base are read-only.
O9. Pending items. commit_steps.sh's record step uses the cd-glob form and writes the raw with the repository root as <repo>. Its gate asserts 222/222, exit 0 and 225 ids, which d3.out predicts.

== My departures (for the seat to class) ==
D1. These git commands ran without item 3's pathspec. Each named only paths outside data/ and printed object ids or nothing.
- `git rev-parse <rev>:<path>` at a84833e and HEAD (scripts/n_analyze.py), at d791bd9 and HEAD (valence_core/n/schema.py), and at dc6a1cf (the seat raw).
- `git hash-object` on the base copy, scripts/n_analyze.py, schema.py and the seat raw.
- One `git status --porcelain` scoped to five named paths: scripts/n_analyze.py, RESULTS.md and the three v5 raw names.
D2. `git log -n 8` and `git show --name-status a84833e` took `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` rather than `':!data/**'`, though nothing under data/ was wanted. They printed ids, dates and subjects, and five non-data paths.
D3. `diff -u` wrote the compared files' modification times (clock times) into the headers of two of my files under SCRATCH/vc/checker/. I stripped them afterwards, and none is in this report.
D4. Beyond the brief's list I used sed, awk, cmp, xxd, head, tail, wc -l, `test -w` (a permission bit on six scratch files) and a pruned find, all read-only. I wrote only under SCRATCH/vc/checker/, apart from the sed -i strip of my own two files. One recursive grep ran over the scratch folder n9, not a checkout; a pruned find showed that folder holds no data, ckpt, reports or mf3 path.
D5. One loop failed in zsh before git ran (a `$c:` modifier error) and was re-run with the pathspec.

No Python ran, nothing under data/ was read or listed, and data/mf3 was never touched.

### Code's dispositions of pass 1

Pass 1 checked 188 claims: 160 CONFIRMED, 12 IMPRECISE, 1 FAIL and 15 NOT CHECKABLE, with nine observations. Its one
FAIL and every IMPRECISE are applied, and so are observations 1 and 3 to 8. Observation 2 is applied with R33, and 9
needs nothing. Pass 2 checks the revised texts.

#### The FAIL

- **R41 (and O3), C19 "as drafted".** C19 was re-expressed on F6's parenthesized line. The review raw's §2 now says
  "eight as drafted (C01, C06, C11, C16, C17, C20, C25, C27), and C14, C15 and C19 re-expressed on the fixed draft",
  as §3 already did.

#### The IMPRECISE

- **E9, "transcribed twice".** The entry now says §3.2's words are transcribed in the module and again in the battery:
  in its oracle (`_ORC_TAIL`, `_ORC_N4`) and in the literal-text checks' filled tails.
- **E21, the literal states.** The entry now says a state with no point map (the battery's literal states, unless a
  case gives one) reads a pause at every point of its arm.
- **E34, N1-R and the floor shadows.** The entry now says the floor shadows in a binomial fire's batch do not bring
  N1-R into its scope. Only the fired read's own shadow clause, or an N1-R trial in the batch, would.
- **E45 and R11, "six new refusals".** Against the reviewed draft, VD-REFUSE gains three refusals (batch-start,
  batch-scope, batch-read-count) and rebuilds three (batch-count, batch-exceedances, batch-end). The entry and the
  review raw's head now say so.
- **R33 (with A28 and O2), "each the runner's".** The three accepted standing batches are bound as the runner counts a
  batch: their extent, n, k and scope. Their fires are not ones the runner would write on those campaigns:
  - under p0 = 0 no fire comes at k = 0;
  - A's k = 1 batch would fire at its cadence point, N1-P's last −1 read, not at the run's end. Code checked this in
    the runner: `clear_batch` resets `next_due` to the cadence, the evaluation then falls due at the batch's 480th
    read, and k = 1 there.

  The analyzer binds a batch, not the schedule or the condition of its fire. This is now said in the review raw's §2
  (B3), in the entry ("inputs bound as the runner counts a batch"), and in the analyzer's comment and description of
  VD-PAUSE-POINTS (A28: C's "the same" is now "N1 and N2 the same, and the same point").
- **R34, batch-end "added".** The draft had a batch-end case. §2 now lists batch-end among the three rebuilt.
- **R51, "checked … in the base".** §3 now says the old texts of the 50 that ran were checked against the mutant base.
  The 28 as first written were checked against the working draft they were written on.
- **R59, V03's argument.** §3 now says "No battery input that reaches `State.paused_on`". RD-PAUSE-POINTS's direct
  cases do hold a scope arm with no point, but they test `paused_points` alone.
- **A1, the module docstring.** Its OPEN clause now names the second sitting's §3.
- **A19, `paused_points`' docstring.** It now calls the shadow extension through a batch Code's, capped by the scope,
  as PIN-n-37 does. F5's disposition now names the docstring too.

#### Observations

1. **O1, which script ran d1–d3.** Code's transcript has each of the three runs through `run_battery2.sh`, the cd-glob
   form. v5's `run_battery.sh`, v4's form copied at the cycle's start, was read and never run. The review raw's §4 says
   so.
2. **O2:** applied with R33.
3. **O3:** applied with R41.
4. **O4, the route of the SCOPE point.** It went from Code to the coordinating session, which relayed it to n-build as
   information, and it is flagged for the seat in PIN-n-37. The entry, the review raw's §2 (F5) and PIN-n-37 ("relayed
   to n-build") now say the same.
5. **O5, the batch on N1-V's +1 cell.** Code added it to its working copy after the freeze, and it never ran. §2 (B6)
   now says so.
6. **O6, C14's batch-read-count.** It failed on the write-once message, the cascade that §3's notes explain only for
   C17. The notes now state the cascade once, with C14 and C17 as its two cases.
7. **O7, §1's digest.** It is now said to be the saved file's: `review/reviewer/report.md` in Code's scratch.
8. **O8, "frozen copies".** The run copies are now read-only. §4 says each was made before its run and is unchanged
   since, with the sha256 named to the coordinating session.
9. **O9, pending items:** nothing to apply. The record step and the gate are as the checker read them.

The A13 note is applied too: the comment above the oracle's copies now names the label's copies among what SENT-RULING
compares.

#### What the edits changed in the analyzer

There are six texts, in seven hunks: the module docstring, the comment above the oracle's copies, PIN-n-37, the comment
above VD-PAUSE-POINTS, its description (two hunks), and `paused_points`' docstring. The review raw's §5 lists them. No
outcome, sentence or form changes, and the forms' digest is the same. The analyzer's sha256 moved, and the entry, the
close line and the review raw carry the new one, filled by script.

#### The checker's departures (for the seat to class)

The checker disclosed five, D1–D5 in its report. None read anything under `data/`, and none touched `data/mf3`:
- **D1.** `git rev-parse`, `git hash-object` and one `git status --porcelain` scoped to five named paths ran without
  item 3's pathspec. Each named only paths outside `data/`.
- **D2.** Two commands took the `ckpt`/`reports` form of item 3's pathspec where `':!data/**'` would have done.
- **D3.** `diff -u` wrote file modification times into two of the checker's own scratch files, which it then
  stripped.
- **D4.** It used read-only tools beyond the brief's list, including a recursive grep over Code's scratch folder `n9`,
  which a pruned `find` showed holds no data path.
- **D5.** A loop failed before git ran.

## Pass 2: the report

BLIND VALUES-CHECK, SECOND PASS: the n_analyze v5 entry, its close line, the review raw and the analyzer's new texts

Inputs, checked first (shasum, cut by tool): BRIEF2 2db760df…39d1; entry.filled.md 25e0ed18…5f63; close_a84833e.filled.md 38d18c56…248f; review.md 5f9d45c8…760a; final/n_analyze.py 71d8738e…28aa; pass1.md 5f1239ba…d622; pass1_dispositions.md 77c0e250…344f. All match what the brief gives. SCRATCH/base-a84833e.py = `git show a84833e:scripts/n_analyze.py` = REPO's scripts/n_analyze.py (509a62ad…85f6). The supplied final_vs_mutbase.diff is identical to a regenerated `diff -u`. Every abbreviated hash in the four texts was cut by tool from its file and matches: 509a62ad…85f6, 6f2dd349…301e, 83f54ec6…d04c, cca2acb4…9057, e2cf9684…d6d0, 6010bc30…da87, f7fee979…f6eb, 0ea39600…0db6, cdecf39e…01d3, 71d8738e…28aa, 281c6827…bbe2, 41d0d654…b1da, 5843a9bd…7165, 30a3d0f5…04f4 and e979f8f2…5e03. The texts hold no clock time, local path or user name.

Pending by design:
- The run of record: graded against SCRATCH/runs/d3.out. The final file differs from the mutant base in eight change regions: the REPO line, the docstring, the oracle comment, PIN-n-37, the VD-PAUSE-POINTS comment and two strings of its description, and paused_points' docstring. No check, form, _REQ entry or EXPECTED_CHECKS changed.
- The commit.
- The values-check raw that §5 cites.

The values-check line was skipped.

== 1. The entry (SCRATCH/raw/entry.filled.md): 65 claims ==
E1 l.1–3: the title's rulings (PIN-n-33 amended, the label in the sentence, PIN-n-34–36 accepted; §3; item 6). CONFIRMED: seat raw §3.1–3.3 and §6 item 6; the relay.
E2 l.3: Battery 222/222. CONFIRMED, pending the run of record: d3.out ends "222/222", with 0 FAIL.
E3 l.3–4: 49 of 50 mutants killed. CONFIRMED: of the 50 outputs, 49 fall below 222 passes (C20 at 213/217) and V03 passes 222/222. Matches kills.txt.
E4 l.4–5: PIN-n-37 is Code's reading, flagged. CONFIRMED: the PINS header (l.2387) says "PIN-n-37 declared since, strikable".
E5 l.5: model-free; nothing ran on a model or the box; no stage ran. NOT CHECKABLE. The scripts run --selftest only.
E6 l.6–8: the full sha256, and 509a62ad…85f6 at a84833e. CONFIRMED by shasum and git show.
E7 l.9–10: the schema pin, the bound files and the commands are unchanged. CONFIRMED.
- No diff line touches SCHEMA_*, PROPOSAL_*, ADDENDUM_* or argparse.
- schema.py at d791bd9 hashes to the pin, 0ea39600….
- PROPOSAL and ADDENDUM hash to their pins.
E8 l.11–13: the seat raw's path, cdecf39e…01d3, committed at dc6a1cf, cited by path. CONFIRMED: `git log --diff-filter=A` gives dc6a1cf, and the blob is unchanged since.
E9 l.14: the battery reads no raw. CONFIRMED: the hook bars results/raw (l.2576).
E10 l.14–15: §3.2's words are transcribed in the module, the oracle (_ORC_TAIL, _ORC_N4) and the literal-text checks' filled tails. CONFIRMED.
- The copies sit at l.669–670, l.1036 and l.1789–1790.
- SENT-FOURTH-FILLS's want_e (l.1814–1815) is a further literal copy.
E11 l.15–16: the review and the values-check held them to the raw. CONFIRMED.
- The review compared the module's and the oracle's copies "character for character".
- This pass compared bytes. LABEL_TAIL is 20 e2 80 94 20 5b…, equal to the raw's quoted tail. CNA_N4 equals the italic fill. Both literal-tail sets use the U+2014 em dash, and "(N4 DEAD)" is CNA_N4 filled.
E12 l.17–19: the run of record gives 222/222, 225 ids and exit 0; the raw's name. CONFIRMED, pending: d3.out shows 222/222 and 225 ids. commit_steps.sh's record step names the raw, and its gate asserts all three.
E13 l.20–22: the item is verbatim as relayed; the paste block is not committed; the wording differs a little from §6's draft; the PI's block is the record. CONFIRMED.
- §6 item 6 reads "(pauses point by point); the fourth form's label in the sentence".
- §6's header says "your words are the record".
- dc6a1cf's subject cites "Route as given".
E14 l.23: item 6, verbatim. CONFIRMED: string-equal to the brief's relay.
E15 l.25: two standing rules, from §4, as relayed. CONFIRMED: §4 holds both.
E16 l.26–27: the first rule's text. CONFIRMED against §4 and the relay ("me" is the coordinating session).
E17 l.27: every run ran on bytes named to it first. NOT CHECKABLE.
E18 l.28: the pathspec line is in both checkers' briefs. CONFIRMED: vc/BRIEF.md and vc/BRIEF2.md carry it, and so does the reviewer's brief. Each also carries items 1–5, equal line for line to the list-of-record raw.
E19 l.31–32: the reads N2 uses. CONFIRMED (§3.1).
E20 l.33–34: other reads leave N2 decided, superseding §1.6's sentence. CONFIRMED: §3.1; the 2026-11-16 answers l.33.
E21 l.35–36: the guard half stands. CONFIRMED: §3.1; l.573.
E22 l.37: paused_on reads one point, and n2_outcome takes its pause causes there. CONFIRMED (l.437–441, l.553).
E23 l.38–39: a state with no point map (literal states, unless a case gives one) reads per arm. CONFIRMED: l.439–440; literal_state defaults to None; l.1419 gives a map.
E24 l.40: N1, dose and N4 read pauses per arm. CONFIRMED: _causes l.463; dose through N1 at l.508; N4 at l.582.
E25 l.41: the form ends " — [label]", as A.2 and A.7 do. CONFIRMED: F4 + LABEL_TAIL; the prebuild raw's A.2 and A.7 both end "— [label]".
E26 l.43–45: the three fills. CONFIRMED (§3.2; l.786).
E27 l.48: SENT-FILLED-DOSE-FOURTH has eight sentences and covers the three fills. CONFIRMED: 4 forms × 2 shapes; the fills are answered, (N4 DEAD) and CNA.
E28 l.49–50: SENT-FOURTH-FILLS covers 640 evaluations, split 64/256/320. CONFIRMED: l.1808–1825 passes in d3; the arithmetic holds.
E29 l.51–52: the digest moved from 281c6827…bbe2 to 41d0d654…b1da, set from the first run's printed value. CONFIRMED: d1.out prints 41d0d654…, and d1→d2 is that one line.
E30 l.53–54: the 2,561 evaluations and the hand tallies are unchanged except the form string. CONFIRMED: T1–T10 give 2561/2561; _bt_expected_tallies changes only f4.
E31 l.55–56: PIN-n-34–36 are marked accepted, their texts unchanged. CONFIRMED: no diff hunk touches their texts.
E32 l.57–58: PIN-n-37 is registered and strikable until LOCK-n v1.0. CONFIRMED.
E33 l.59–63: the points a pause stands on. CONFIRMED: PIN-n-37; paused_points l.5509–5531.
E34 l.65: N1's and N4's pauses stay per arm. CONFIRMED.
E35 l.66–67: the reach through a batch is Code's, capped; the runner applies its shadow clause to the fired read alone. CONFIRMED.
- The runner's SCOPE pin is at l.30–32 and _scope at l.290–296.
- _scope is called with the fired read at l.418 and l.490, and with the batch's arms only at l.507.
E36 l.67–68: floor shadows do not bring N1-R into scope; only the fired read's own shadow clause or an N1-R trial would. CONFIRMED: the batch's arms are its trials' arms, and a shadow's arm is N1-V.
E37 l.68–69: the point went to the coordinating session and on to n-build. NOT CHECKABLE.
E38 l.69–70: it is flagged in PIN-n-37 and applied nowhere. CONFIRMED: runner.py is clean and equals 83a50a0's.
E39 l.70: no outcome changes today. CONFIRMED.
- Only a batch from the stage's start holds shadows.
- If it fires before N1-R's reads, N1-R is incomplete; after them, N1-R trials bring N1-R into scope.
- This agrees with the reviewer's F5 scenario.
E40 l.71: the two alternatives are named. CONFIRMED.
E41 l.71–73: under the launch order and the cadence, a start batch stands on every read of its scope's arms. CONFIRMED.
- The ORDER pin puts the shadows first.
- n §2.1 (PROPOSAL l.77) says "cadence every 160 reads".
- The first evaluation falls at read 159, the last shadow.
E42 l.74–79: what the reader binds. CONFIRMED (l.5403–5421).
E43 l.80: every pause's read is one of the plan's. CONFIRMED (l.5425–5426).
E44 l.81: the reading of PIN-n-24's per-arm clause. CONFIRMED: PIN-n-37 l.2514–2517; PIN-n-24 unchanged.
E45 l.82–83: the beside's `paused`, its figures computed, and `pause_points`. CONFIRMED (l.571, l.5583–5587).
E46 l.85: the reviewer read 6f2dd349…301e (221/221). CONFIRMED: the copy is read-only, and d2.out shows 221/221.
E47 l.85–89: no MAJOR; F1 MINOR (start and read-less end); F2–F6, B1–B4 and B5–B7 graded as stated; 34 mutants, 10 predicted; V03 equivalent. CONFIRMED against the report.
E48 l.90–93: dispositions F1, F2–F5 and F6. CONFIRMED (see O7).
E49 l.94–97: "B1–B7: inputs bound as the runner counts a batch — …; VD-REFUSE gains three … and rebuilds three". IMPRECISE.
- The counts are right: 47 → 50 cases against the reviewed draft; batch-start, batch-scope and batch-read-count are new; batch-count, batch-exceedances and batch-end are rebuilt.
- The header phrase fits only the three accepted standing batches.
- B1's two ranges start on a read with no re-computation, which no runner batch does.
- VD-REFUSE's batch inputs are built not to be the runner's.
- B4's rendering pause and B5's literal-state cases carry no batch.
- B7's change (bz and rs now naming a planned read not on disk) is not listed.
- Suggest: "B1–B7: battery inputs — two new reader cases and a keyed-sample campaign, three accepted standing batches each bound as the runner counts a batch, a rendering pause standing on a read not on disk, a guard paused at either f, the beside's figures pinned, and bz and rs naming a planned read not on disk."
E50 l.98–99: 34 (five re-expressed) and 16 of Code's on 83f54ec6…d04c (222/222); 49 of 50. CONFIRMED.
E51 l.100: V03 survived and is equivalent. CONFIRMED: V03.out is 222/222 with 0 FAIL.
E52 l.101: the other nine are killed by added or extended checks. CONFIRMED by each output's failing case keys.
E53 l.102: the committed bytes differ in the REPO line and six texts. CONFIRMED by the mutant-base → final diff.
E54 l.105: the windows were granted and the bytes named. NOT CHECKABLE.
E55 l.106–107: one process at a time, nice -n 19, -I, temp folders outside, foreground. CONFIRMED as far as the files show: run_battery2.sh, run_mutants2.sh, commit_steps.sh record, and tempfile.
E56 l.107–108: the interpreter was reached by cd-glob (n-build's form), so no argv named its path. NOT CHECKABLE for d1–d3. INVOCATION prints the resolved executable either way. The mutant script and the record step use the form.
E57 l.109: 2 runs, 219/221 then 221/221; the first failed on the digest alone. CONFIRMED: SENT-CODE-FORMS failed, and so did the coverage check on that id alone.
E58 l.110: 1 run of the fixed draft (222/222), then 50 mutants. CONFIRMED.
E59 l.110: "in four batches". NOT CHECKABLE.
E60 l.110–111: each file was checked against a manifest. CONFIRMED.
- shasum -c gives 50/50 OK.
- run_mutants2.sh checks before each run.
- Each output's INVOCATION names its mut_pre file.
- That the manifest was named first is not checkable.
E61 l.111–112: a 48-file manifest was replaced, adding C14 and C15. NOT CHECKABLE. Consistent with C14 and C15 being last in mutants_c_final.spec.
E62 l.113: the run of record: 1. CONFIRMED, pending.
E63 l.115–116: Q-F3 ran beside; no other window was open. NOT CHECKABLE.
E64 l.117–118: committed by path; not pushed. CONFIRMED, pending the commit (commit_steps.sh's RAWS, place and gate).
E65 l.118: Next, G-ANL-n's canonical run. CONFIRMED: the docstring's l.23.

== 2. The close line (SCRATCH/raw/close_a84833e.filled.md): 11 claims, all CONFIRMED ==
C1 l.1: the PI date; the n-analyzer's line, per §5 and §6 item 6. CONFIRMED (§5 "close lines on a84833e's entry").
C2 l.1–2: on PIN-n-33–36 and the two questions. CONFIRMED (RESULTS.md l.334–357).
C3 l.2–7: the path, the full sha cdecf39ea8d2…701d3, dc6a1cf; §3 rules on them. CONFIRMED.
C4 l.7–8: "Route as given", as item 6. CONFIRMED.
C5 l.8–9: quoted verbatim in the entry. CONFIRMED, pending the commit: entry l.23 equals the relay.
C6 l.11: 71d8738e…28aa. CONFIRMED.
C7 l.12: re-registered, with the guard half. CONFIRMED (l.2471–2477).
C8 l.13: " — [label]" in three fills. CONFIRMED.
C9 l.14: PIN-n-34–36 stand and are accepted. CONFIRMED.
C10 l.15: the digest moved. CONFIRMED.
C11 l.17–18: PIN-n-37 is Code's and flagged in the entry. CONFIRMED.

== 3. The review raw (SCRATCH/raw/review.md): 89 claims ==
R1 l.1: the title. CONFIRMED.
R2 l.3: the entry it serves. CONFIRMED.
R3 l.5–8: a84833e, 509a62ad…; §3 of cdecf39e… at dc6a1cf. CONFIRMED.
R4 l.9–13: the four changes. CONFIRMED.
R5 l.15: 219/221, then 221/221. CONFIRMED.
R6 l.15: "drafted in one step", in a granted window. NOT CHECKABLE.
R7 l.16–17: read-only copy, 221/221, 224 ids. CONFIRMED (r--r--r--; d2.out).
R8 l.18–19: the brief quoted items 1–5 and the pathspec line, and allowed no Python. CONFIRMED by grep -F -x against the list-of-record raw (6c1135f5…). "A subagent" is consistent with extract_handback.pl.
R9 l.20–22: its specification. CONFIRMED against review/BRIEF.md.
R10 l.23–25: its conduct. CONFIRMED as the report states it; patterns.txt exists.
R11 l.26–30: F1–F6, B1–B7, V01–V34 and the 10 named survivors. CONFIRMED.
R12 l.31–32: all findings taken; F1 binds; F2–F6 change registers and wording. CONFIRMED.
R13 l.32–34: "B1–B7 give the battery inputs bound as the runner counts a batch: …". IMPRECISE for the same reason as E49, and this summary also omits B5's new N2-PAUSE-POINTWISE cases. The entry and this head now summarize B1–B7 differently.
R14 l.35–37: the set, on 83f54ec6…, 222/222, 225 ids; 49/50; V03; nine. CONFIRMED: one output per id.
R15 l.38–39: §4 and §5; the REPO line and six texts. CONFIRMED.
R16 l.40–41: tallies unchanged except the form string; the 640 split by fill. CONFIRMED.
R17 l.44–45: nice -n 19, -I, one at a time, temp outside, foreground. CONFIRMED by the scripts.
R18 l.43–46: windows, bytes named, cd-glob, nothing on a model or the box. NOT CHECKABLE.
R19 l.48: an exact replacement, asserted to occur once. CONFIRMED.
- All 50 mut_pre files are the mutant base with one change region equal to .old→.new.
- Each .old's first line occurs exactly once in the base.
- run_mutants.sh's perl asserts count == 1.
R20 l.48–50: the manifest, a check before the run, and "killed" meaning a non-zero exit. CONFIRMED by run_mutants2.sh's rc test.
R21 l.54–56: §1 saved by script, 6010bc30…da87, headings down two levels, nothing else; the frozen copy's line numbers. CONFIRMED.
- report.md hashes as given.
- Lines 58–345 equal report.md with "## "→"#### ".
- The cited lines (5283–5290, 2414–2421, 785, 1063–1064, 3811–3855, 4449–4466, 4584–4596 and others) hold those texts in d2.
R22 l.58–345: the report's checkable facts. CONFIRMED on spot checks.
- The brief hashes to f7fee979…f6eb.
- The regenerated base→copy diff body is identical, with 38 hunks.
- The schema hashes to 0ea39600….
R23 l.349–350: nothing changes on runner-written reports. CONFIRMED.
- F1's bindings accept every runner batch: the start is batch_first after clear_batch, a read-less end is the last trial, and the scope contains the batch's arms.
- CODE_FORMS_SHA256 is equal in d2 and d3.
- F6 keeps Python's precedence.
R24 l.354–361: F1's bindings; the definition of a cleared batch; the clear on replay. CONFIRMED (runner l.422–426).
R25 l.363–364: the draft's conjunct is dropped; the runner fires only at a trial. CONFIRMED: observe evaluates only where fidelity is set; the schema ends a fire's batch at its read.
R26 l.365–367: F2. CONFIRMED.
R27 l.368–371: F3. CONFIRMED.
R28 l.372–373: F4's quote. CONFIRMED (l.2508–2510).
R29 l.374–376: F5 in PIN-n-37 and in the docstring. CONFIRMED.
R30 l.376–377: the route (Code → coordinating session → n-build). NOT CHECKABLE.
R31 l.378–379: F6. CONFIRMED (d2→d3 diff).
R32 l.383–388: B1's two cases and `sampled`. CONFIRMED (l.3871–3886, l.3382–3418).
R33 l.389–390: two cases were already added; there are now fourteen. CONFIRMED: both cases are absent from d2 and present in d3, and there are 14 keys.
R34 l.391–392: B2. CONFIRMED.
R35 l.393–402: A, C and B. CONFIRMED: ok_pp, batch_of and clear_and_end; the 80 TAU/4 shifts at l.4332–4334; the non-finite fresh read; pz_adj carries no batch.
R36 l.403–406: their extent, n, k and scope follow the runner; the runner would not write these fires. CONFIRMED.
- p0_count is 0 in the example identity, and binom_tail returns 1.0 for x ≤ 0.
- After the clear, next_due is 160. The first trial is at batch read 321, where k = 0 and nothing fires.
- The next evaluation is due at 480, N1-P's last −1 read, where k = 1.
R37 l.408–414: three refusals added and three rebuilt on A's batch; batch-end now ends one trial short. CONFIRMED (l.4841–4853; 47 → 50 cases).
R38 l.415–417: B4. CONFIRMED (c4 omits N1-P's −1 cell).
R39 l.418–419: B5. CONFIRMED.
R40 l.420–421: the draft's read-less mid-campaign batch is gone. CONFIRMED (d2's bq).
R41 l.421–422: an N1-V +1 batch in the working copy that never ran. NOT CHECKABLE. It is in none of d1–d3, and C15's as-drafted prediction cites it.
R42 l.423–424: B7. CONFIRMED.
R43 l.428–430: the five re-expressed. CONFIRMED: each first line occurs once in d2 and not in d3.
R44 l.431–434: 28 drafted; eight kept as drafted; C14, C15 and C19 re-expressed; why C14 and C15 are kept. CONFIRMED.
- The eight's mutation texts are equal across the two specs (see O4 on the predictions).
- No other mutant drops n or counts at TAU/4.
R45 l.435–436: sixteen dropped; C13. CONFIRMED.
R46 l.438: five added, C29–C33. CONFIRMED.
R47 l.442: 50 mutants. CONFIRMED.
R48 l.443–445: V01–V34 as written except five. CONFIRMED: 29 blocks of mutants_v.spec and 5 of the re-expressed spec equal the .old/.new files that ran.
R49 l.446: Code's sixteen, whole. CONFIRMED: the raw's blocks are mutants_c_final.spec, reordered by id.
R50 l.447–450: twelve make the reviewer's change; four reach it another way. CONFIRMED.
- Eleven pairs are byte-identical.
- C07 and V18 differ only by V18's comment.
- C03/V12, C05/V20, C18/V29 and C22/V09 have the same effect.
R51 l.452: C13 is covered by V26 and C30. CONFIRMED.
R52 l.453–454: the eleven kept. CONFIRMED.
R53 l.455: five new. CONFIRMED.
R54 l.457: all 28 are in Code's scratch. CONFIRMED (mutants_c.spec).
R55 l.457–458: each of the 50 old texts occurs once in the mutant base. CONFIRMED.
R56 l.460–461: the read-only base, 83f54ec6e51c…. CONFIRMED.
R57 l.462: 222/222, 225 ids. CONFIRMED.
R58 l.463–464: the manifest e2cf9684…, checked before each run. CONFIRMED.
R59 l.464: each ran once, one at a time, in four batches. NOT CHECKABLE.
R60 l.465: 49/50; V03; nine. CONFIRMED.
R61 l.467–468: the table's semantics. CONFIRMED: unreached[:6] is sorted; B.group.
R62 l.470–521: the 50 rows. CONFIRMED.
- From, Function, What-breaks and Predicted equal the spec headers field by field.
- The Result column equals kills.txt and each output's coverage line.
- The table equals kill_table.md.
R63 l.523–529: V03's equivalence; the direct cases. CONFIRMED.
R64 l.531–533: C20's AnlStop, with "STOP: " included. CONFIRMED (C20.out; fill at l.3259; 213/217).
R65 l.535–549: the nine kills. CONFIRMED.
- V07 fails (a,N2-S,f0.10) and (b,N2-S,f0.20).
- V08 fails the beside-figure cases.
- V15 and V24 fail VD-PAUSE-RENDERING.
- V16 fails the B1 ranges (and "a range holding no trial").
- V18 fails "an N4 trial is no shadow" and A, C.
- V26 fails batch-start and V28 batch-read-count.
- V27 fails A, C and B.
R66 l.551–558: the refusal lists. CONFIRMED against each failing line.
R67 l.560–564: the shared write-once folder; C14 and C17. CONFIRMED: rv writes to out_refused (l.4676). C14 shows batch-count 'no exception', then the write-once message. C17's list is cut after batch-start.
R68 l.566–598: the re-expressed blocks. CONFIRMED.
R69 l.600–704: Code's blocks. CONFIRMED.
R70 l.708–711: §4's windows, cd-glob, nothing on a model. NOT CHECKABLE. The process form is covered at R17.
R71 l.713–715: runs on d1–d3 copies, unchanged since, now read-only. CONFIRMED: the INVOCATION lines name runs/dN.py, the shas match, and the copies are r--r--r--. "Named" is not checkable.
R72 l.715–716: all through run_battery2.sh; run_battery.sh never run. NOT CHECKABLE. run_battery.sh is v4's with the folder changed, as said.
R73 l.719–720: d1 cca2acb4…, 219/221, digest and coverage. CONFIRMED.
R74 l.721–722: the pin set from the printed value as d2's one change. CONFIRMED (one-line d1→d2 diff).
R75 l.723: d2, 221/221, frozen. CONFIRMED.
R76 l.725–726: d3, 222/222, 225 ids, the mutant base. CONFIRMED.
R77 l.727–728: four batches (12, 12, 12 and 14). NOT CHECKABLE.
R78 l.728: the manifest, 50 files, checked before each run. CONFIRMED.
R79 l.729–730: 48 files, then 50 confirmed. NOT CHECKABLE.
R80 l.731: the run of record is the entry's. CONFIRMED, pending.
R81 l.733–734: Q-F3 beside; no other window. NOT CHECKABLE.
R82 l.738 (also l.746 "seven hunks" and l.750 "two hunks"): "eight hunks". IMPRECISE.
- There are eight change regions, counting as `diff`/`-U0` does.
- The supplied final_vs_mutbase.diff (unified, git's default context) has 7 hunks: the description's two edits share one.
- §1's "38 hunks" counts the unified way.
- Suggest "eight change regions (git diff -U0)".
R83 l.740–745: the REPO line, "as the committed analyzer always has". CONFIRMED: all five committed versions carry the exact line.
R84 l.746–754: the six texts and what each now says. CONFIRMED against the eight change regions. "§1 and §2 of the values-check raw" is pending.
R85 l.756–757: no outcome, sentence or form changes; the digest is the same. CONFIRMED: none of the six texts is in code_forms().
R86 l.760–762: the tallies are a84833e's (the v4 raw's §6); the one change is the form string. CONFIRMED: the v4 raw's §6 was committed at a84833e.
R87 l.762–763: "The fourth form's label is in its text, not in the tally's key". IMPRECISE.
- The tally's key is (state, form, label, no_read) (l.1962), so the §0.6 label is in it. That is why it counts 64/576.
- What the key lacks is the fill's "(N4 [n4])".
- l.760 itself says the tallies are "by state, form and label".
- Suggest "The fourth form's fill is in its text, not in the tally's key, which carries the record's label".
R88 l.765–767: the split's derivation. CONFIRMED.
R89 l.769–775: the table and 640 in all. CONFIRMED: 16×4; 48×4+16×4; 64×4+16×4.

== 4. The analyzer's new texts (SCRATCH/final/n_analyze.py): 36 claims, all CONFIRMED ==
A1 l.16–23: the docstring's PINS/OPEN paragraph. Names PIN-n-7 to -36 as ruled, the second sitting's path, and "of its second sitting (§3)".
A2 l.2384–2388: the comment above PINS.
A3 l.2521–2524: the comment above OPEN.
A4 l.2471–2477: PIN-n-33, against §3.1.
A5 l.2500–2519: PIN-n-37.
- The schema says "A pause stands on the arms in its scope" (l.155–158).
- campaign_order gives the reasons dose-rule and sample (l.129).
- The SCOPE and ORDER pins and n §2.1's cadence are as cited.
- PIN-n-24's quote is exact. "(relayed to n-build)" is a route, not checkable.
A6 l.2530–2534: OPEN-Q3.
A7 l.2548–2552: OPEN-Q8.
A8 l.650–659: the forms comment.
A9 l.669: LABEL_TAIL, byte-equal.
A10 l.670: CNA_N4, byte-equal.
A11 l.671–674: F4 and RULING_FORMS.
A12 l.767: FORM_FOURTH. Its copies at l.1068 and l.1973 are identical, and no copy of the first sitting's string remains.
A13 l.1027–1036: the comment above the oracle's copies, _ORC_TAIL and _ORC_N4. SENT-RULING compares the label copies (l.1689–1693).
A14 l.1064–1068: the oracle's fill.
A15 l.433–435: the State.paused_at comment (see O5).
A16 l.437–441: paused_on.
A17 l.536–549: n2_outcome.
A18 l.774–778: sentence_dose.
A19 l.5500–5508: paused_points, now as PIN-n-37.
A20 l.5349–5365: report_problems. The code also needs the cleared pause to have a read. That cannot matter: runner l.430–433 launches nothing after a read-less fire.
A21 l.2957–2963: build_state.
A22 l.5577–5580: state_figures (see O5).
A23 l.3375–3392: _bt_write_campaign's `sampled`. schema.example_record says "sample" marks the keyed sample.
A24 l.1967–1973: _bt_expected_tallies and f4.
A25 l.1406–1435: N2-PAUSE-POINTWISE: 10 cases × 2 shapes, with matching wants.
A26 l.1391–1397: N2-INDET-pause.
A27 l.3828–3893: RD-PAUSE-POINTS, 14 cases.
A28 l.4487–4566: VD-PAUSE-POINTS's comment and description. They now say "bound as the runner counts a batch" and "N1 and N2 the same, and the same point".
A29 l.4589–4604: VD-PAUSE-RENDERING.
A30 l.4825–4870: VD-REFUSE's comment and description (50 cases).
A31 l.1689–1699: SENT-RULING.
A32 l.1796–1800: SENT-FILLED-DOSE-ND, eight sentences.
A33 l.1801–1807: SENT-FILLED-DOSE-FOURTH.
A34 l.1808–1825: SENT-FOURTH-FILLS.
A35 l.1113 and _REQ: 222 checks and 225 ids. That is 217+5 and 220+5; the v4 selftest raw has 220.
A36 l.3199: CODE_FORMS_SHA256 equals d1's printed digest.

== Counts ==
| Text | Claims | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|---|
| Entry | 65 | 56 | 1 | 0 | 8 |
| Close line | 11 | 11 | 0 | 0 | 0 |
| Review raw | 89 | 76 | 3 | 0 | 10 |
| Analyzer | 36 | 36 | 0 | 0 | 0 |
| All | 201 | 179 | 4 | 0 | 18 |

== Observations ==
O1. E49 and R13 were introduced by the R33 edit. The phrase pass 1 proposed for VD-PAUSE-POINTS's three batches now heads the whole B1–B7 summary, replacing "runner-shaped". The two summaries also disagree: the entry lists B5's items and omits B7, and the raw's head omits both.
O2. The dispositions' closing paragraph says the review raw carries the analyzer's new sha256. It carries none: assemble.sh fills no analyzer digest into it, and neither 71d8738e… nor pass 1's 883bff2f… appears there. Only the entry (in full) and the close line carry it.
O3. R51's disposition adds "The 28 as first written were checked against the working draft they were written on". §3 does not say this, and it is not checkable. Their first lines do occur once in d2.
O4. Prediction columns.
- The table shows Code's predictions for C01, C17 and C25 as revised in mutants_c_final.spec. C01 and C25 add VD-PAUSE-RENDERING, a check written after they were drafted. C17's "(the batch cases)" replaces "(batch-count, batch-end, batch-exceedances)". The column is headed "Predicted (by its author)", and §2/§3 call these mutants "as drafted" (true of the mutation text) without noting the change.
- The five re-expressed V blocks carry Code's predictions (V26 "killed by VD-REFUSE ('batch-start')"), while the table gives the reviewer's ("survives").
O5. The State.paused_at comment ("None (the battery's literal states)") and state_figures' "null for a literal state" keep the gloss that the entry's E21 edit made exact. N2-PAUSE-POINTWISE's literal states carry a map. "(… unless a case gives one)" would fit both.
O6. Outside the listed texts, two strings were not updated for the second sitting:
- code_forms' docstring (l.3184–3187) still lists RULING_FORMS as "its fourth form's two branches, the merge note and the zone's words", without CNA_N4.
- ganl_artifact's "spec" (l.5000–5002) names the 2026-11-18 answers §5 but not the second sitting's §3. That string goes into the G-ANL-n artifact.
Neither changes an outcome or the forms' digest.
O7. Entry l.92's "F2–F5: PIN-n-37's text and the registers" leaves out F3's module-docstring edit. Minor.
O8. The dispositions' R33 note says the evaluation "falls due at the batch's 480th read". The first evaluation after the clear actually comes at batch read 321 (k = 0, no fire), and the one due at 480 fires. The texts' own wording, "fire … at N1-P's last −1 read", is right.
O9. Cosmetic: the review raw's §6 heading has no blank line before it, and lines 37, 465 and 738 run past the wrap width.
O10. Two pass-1 notes were carried without a disposition line: the C20 quote now has "STOP: ", and the second checker's brief now exists with the pathspec line.

== Pass 1's dispositions: carried, and true? ==
- R41/O3 (C19 "as drafted"): carried (§2 l.432–433). True: C19's old text is unparenthesized as drafted and parenthesized as run. For C01, C17 and C25 see O4.
- E9: carried (l.14–15). True.
- E21: carried (l.38–39). True.
- E34: carried (l.67–68). True.
- E45 and R11: carried (entry l.96–97; raw l.33–34). The counts are true, but the same edit's header phrase is IMPRECISE (E49, R13).
- R33, with A28 and O2: carried in §2 B3, the entry (at the B1–B7 level, see E49) and the VD-PAUSE-POINTS comment and description. The runner claims are true (see O8).
- R34: carried (§2 l.413–414). True.
- R51: carried as to the 50, which is true. Its second sentence is not in §3 and not checkable (O3).
- R59: carried (§3 l.527–529). True.
- A1: carried (l.22–23). True.
- A19: carried (l.5506–5507; §2 F5). True.
- O1: carried (§4 l.715–716). Not checkable, but consistent.
- O2: carried with R33.
- O3: carried with R41.
- O4: carried. The entry, §2 F5 and PIN-n-37 now agree; the route itself is not checkable.
- O5: carried (§2 B6). Not checkable, but consistent.
- O6: carried (§3 l.560–564). True.
- O7: carried (§1 l.54–55). True.
- O8: carried. The copies are read-only and their shas match; the naming is not checkable.
- O9: nothing to apply. The record step and gate are as stated.
- A13 note: carried (l.1030). True.
- "What the edits changed": the six texts, no outcome, sentence or form change, and the same digest are all true. "Seven hunks" counts the -U0 way (see R82). "The review raw carries the new [sha]" is not true (O2).
- The departures summary matches pass 1's D1–D5.

== My departures (for the seat to class) ==
D1. One `git show a84833e:scripts/n_analyze.py | shasum -a 256` ran without item 3's pathspec. It named a path outside data/, and its output went to shasum only. Every later git show and log took `-- ':!data/**'`.
D2. One `git status --porcelain` ran without the item 3 exclusion. It was scoped to six named paths outside data/ (valence_core/n/runner.py, scripts/n_analyze.py, RESULTS.md and the three v5 raw names) and printed nothing.
D3. One zsh loop failed at expansion ("bad substitution" on `$c:scripts`) before git ran. I re-ran it with `${c}:` and the pathspec.
D4. Clock times.
- An unlabelled `diff -U0` wrote the two scratch copies' modification times into the header of my own file SCRATCH/vc/checker2/d2_to_d3.diff. I deleted those two lines with `sed -i`.
- `head -2` of the supplied v5-under-review.diff printed its header times to my tool output only.
D5. I used read-only tools beyond the brief's list:
- sed, awk, xxd, cut, head, tail, wc -l, diff -q and zsh string tests;
- a pruned `find` over SCRATCH's n9 folder, names only, with ckpt, reports and mf3 pruned;
- one `ls -l` of five scratch copies, piped to awk so that only their mode bits and names printed.
I wrote only under SCRATCH/vc/checker2/.

No Python ran. Nothing under data/ was read, listed or searched, and data/mf3 was never touched.

### Code's dispositions of pass 2

Pass 2 checked 201 claims: 179 CONFIRMED, 4 IMPRECISE, 0 FAIL and 18 NOT CHECKABLE, with ten observations. It found
every one of pass 1's dispositions carried, each true except where its observations say otherwise.

With no FAIL, it is the last pass, as at v3 and v4. Its four IMPRECISE items and observations 1 and 4–9 are applied.
Observations 2, 3 and 8 correct pass 1's dispositions. Those dispositions stand above as written, and the correction is
here. Each edit after this pass is checked by tool, not by a third pass.

#### The IMPRECISE

- **E49 and R13 (with O1 and O7), the B1–B7 summaries.**
  - The phrase "bound as the runner counts a batch" now qualifies only the three accepted standing batches.
  - The entry and the review raw's head now list the same inputs: two reader cases and a keyed-sample campaign, the
    three standing batches, the rendering pause, a guard paused at either f, the beside's figures pinned, and the two
    refusal inputs (bz, rs) naming a planned read not on disk, with VD-REFUSE's three new refusals and three rebuilt.
    The head lists VD-PAUSE-RENDERING as the new check.
  - The entry's F2–F5 line now names the module docstring (O7).
- **R82, "hunks".** §5 now says "change regions, as `diff` counts them". The final file now differs from the mutant base
  in twelve, because of this pass's four edits below: the repository line, and ten texts in eleven regions.
- **R87, the tally's key.** §6 now says the fourth form's fill is in its text, not in the tally's key, which carries the
  record's label.

#### Observations

1. **O1:** applied with E49.
2. **O2, the review raw and the analyzer's digest.** True. Pass 1's dispositions say the review raw carries the new
   sha256, but it carries none. The entry (in full) and the close line (abbreviated) carry it, filled by script.
3. **O3, the 28 as first written.** §3 now says Code checked them, when written, against the working draft they were
   written on. That is Code's account of its own check, from its transcript.
4. **O4, the prediction columns.** §3 now says the table's predictions are their authors'. Code revised three of its
   own when the dispositions added checks: C01 and C25 now name VD-PAUSE-RENDERING, and C17 names the batch cases. The
   five re-expressed blocks carry Code's predictions on the fixed draft, while the table gives the reviewer's. Their
   heading says so.
5. **O5, "literal states".** Applied in the analyzer: the comment on `State.paused_at` and `state_figures`' docstring
   now say "no point map".
6. **O6, two strings not updated.** Applied in the analyzer:
   - `code_forms`' docstring now names the second sitting's §3.2 and the label's fill for N4 among the forms it pins;
   - the G-ANL-n artifact's "spec" string now names the second sitting's §3 beside the first sitting's §5. No check
     reads it, and the canonical run is still to come.
7. **O7:** applied with E49.
8. **O8, the batch's evaluations.** True. After the clear, the first evaluation comes at the batch's 321st read, N1-P's
   first −1 read, where k = 0 and nothing fires. The next is due at its 480th, N1-P's last −1 read, where k = 1 fires.
   Pass 1's disposition named only the second. The texts' own wording ("would fire at its cadence point, at N1-P's last
   −1 read") was right.
9. **O9, the layout.** §6's heading now has a blank line before it, and the long lines are rewrapped. Only the raw's
   title and the reviewer's report, reproduced unedited, run past the wrap width.
10. **O10, notes carried without a disposition line.** True. The C20 quote now carries "STOP: " (pass 1's R60), and
    pass 2's brief carries the pathspec line.

#### Checked by tool after this pass

- **Hashes.** The final file's sha256 is in the entry in full and in the close line abbreviated (by `cut`), filled by
  script.
- **The regions.** The final file differs from the mutant base in twelve change regions (`diff`). Its CODE_FORMS_SHA256
  line equals the mutant base's.
- **No placeholder** is left in the entry, the close line or the review raw (the assembly script refuses one).
- **Widths.** No new line in the analyzer exceeds 120 characters. In the raws, only the review raw's title and the
  reviewer's verbatim report run past the wrap width.
- **Phrases.** A search with whitespace normalized (`vc/toolcheck.pl` in Code's scratch, which exits non-zero on any miss)
  passed:
  - 29 stale phrases are absent, among them "transcribed twice", "does not scope N1-R", "six new refusals", "nine as
    drafted", "each the runner's:", "No battery input holds", "frozen copies of the draft", "The fourth form's label
    is in its text" and "(flagged to n-build)";
  - 27 new ones are present, among them "A state with no point map", "do not bring N1-R into its scope", "eight as
    drafted (C01, C06, C11, C16, C17, C20, C25, C27)", "twelve change regions", "which carries the record's label",
    "Code's extension, capped by the scope", "None (no point map:" and "the label's fill for N4".

#### The checker's departures (for the seat to class)

The checker disclosed five, D1–D5 in its report. None read anything under `data/`, and none touched `data/mf3`:
- **D1.** One `git show a84833e:scripts/n_analyze.py | shasum -a 256` ran without item 3's pathspec. It named a path
  outside `data/`, and its output went only to `shasum`.
- **D2.** One `git status --porcelain` scoped to six named paths outside `data/` ran without the exclusion. It printed
  nothing.
- **D3.** A loop failed at expansion before git ran.
- **D4.** An unlabelled `diff -U0` wrote two scratch copies' modification times into the header of one of its own
  scratch files, which it deleted. A `head -2` printed a diff's header times to its tool output only.
- **D5.** It used read-only tools beyond the brief's list, including a pruned `find` over Code's scratch folder `n9`
  and one `ls -l` of five scratch copies, piped to `awk` so that only their mode bits and names printed.
