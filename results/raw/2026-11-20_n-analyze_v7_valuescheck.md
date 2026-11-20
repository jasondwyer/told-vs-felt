# n_analyze.py v7, the tile (R12), F5 and R13 on n-build's delta and ADDENDUM-n3's gate in VERDICTS: the blind values-check, two passes (PI date 2026-11-20)

Code's raw for the entry `n package — scripts/n_analyze.py v7: the tile (R12), F5 and R13 followed on n-build's delta
(ef105f1), the seat's rulings on v6's readings carried in, and ADDENDUM-n3's gate in VERDICTS`.

**Who checked what.** Two blind values-checkers checked the texts against their sources, claim by claim:
- the entry;
- the close line and the dated note on `1185e15`'s entry (the dated note in the first pass only, unchanged after it);
- the review raw;
- the analyzer's new and changed texts (the first pass, on draft 4, `7cc0c78f…10be`) and its changed regions after
  the first pass (the second, on draft 5, `735da934…a7a8`, the bytes this commit carries).

Each checker was a subagent of this session, and its brief allowed no interpreter but `shasum`. The brief quoted the
list of record v2's items 1–5, with item 4's two amendments (C.2 of 2026-11-16, and the fourth sitting's §6.2). It
also carried the standing lines:
- item 3's pathspec with `':!data/mf3/**'`, even for a named file;
- no guard marker in any command's arguments;
- a glob expanded and read before it is looped over;
- no listing of `results/raw`;
- a tracked-and-clean check by `rev-parse` against `hash-object`.

The two passes:
- **Pass 1** (brief `8b0fff29…7aba`) checked the first drafts: 221 claims, 175 CONFIRMED, 23 IMPRECISE, 6 FAIL, 17
  NOT CHECKABLE, with 8 observations. Every FAIL and IMPRECISE item is applied, one of them (R41) in the analyzer's
  battery: a fixture moved, the one code change after the mutants ran.
- **Pass 2** (brief `cc2757aa…7aae`) checked the drafts as revised, and whether each of pass 1's FAIL and IMPRECISE
  items is resolved: 182 claims, 156 CONFIRMED, 9 IMPRECISE, 0 FAIL, 17 NOT CHECKABLE, with 7 observations. Every
  IMPRECISE item and observation is applied in the texts; the edits are checked by tool, 23 of 23.

The reports are reproduced whole, as each hand-back message gave it, taken from the subagents' transcripts by `jq`,
the hand-back's message only. They name Code's scratch folder and the repository by description, as their briefs
asked. Each pass is followed by Code's dispositions.

## Pass 1: the report, as saved from its hand-back (unedited)

# Values-check report: the v7 entry, the close line and dated note on 1185e15's entry, the review raw, and draft 4's new texts

**Inputs.** The brief hashed to `8b0fff29…7aba`, as given. The five texts hashed to their given values: entry `b9264c47…9f41`, close `551f34f0…cdc8`, dated note `beabdd13…7965`, review raw `ad8a6a4b…08c`, draft 4 `7cc0c78f…10be`. Paths below use the brief's labels SCRATCH and REPO. "Notes" means Code's notes file (`n9/next/v7_notes.md`). "Sweep" means `SCRATCH/sweep/since_v6.tsv`.

## 1. entry.filled.md

| # | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | 1 | Date 2026-11-20; the title | CONFIRMED | Consistent with HEAD (d639bdd, 2026-11-20) |
| 2 | 2–4 | Sources: first sitting §3/§4; second §2.5; A-n3 §3.2–§3.5, §8.3 (4); routings items "A.6, 5 and 6" | CONFIRMED | Each section exists and says what is used (labels: see observation 1) |
| 3 | 4–5 | Battery 242/242 | CONFIRMED, pending the run of record | r3.out: "242/242 … pass" |
| 4 | 5 | 47 of 49 mutants killed | CONFIRMED | results.txt; exits.txt: 47 × exit 1, V28 and V38 exit 0 |
| 5 | 5–6 | Five readings, R-A to R-E | CONFIRMED | PIN-n-41 (a)–(d) plus PIN-n-40's reading |
| 6 | 6 | Nothing ran on a model or the box; no stage ran | NOT CHECKABLE | The sweep shows no box or model command |
| 7 | 9 | `418c2136…072d` at 1185e15 | CONFIRMED | `git show 1185e15:scripts/n_analyze.py \| shasum` |
| 8 | 10–11 | Schema pin from 003ae7d's `5cbf60db…574c` to ef105f1's `1cab28df…edff` | CONFIRMED | git show of both blobs, hashed; SCHEMA_SHA256 |
| 9 | 11–12 | Coordinating session verified the delta before the dependent parts were written ("its condition 2") | NOT CHECKABLE | Message. Notes :337 is consistent, but in the notes verification is condition 1; condition 2 is "written against the delta as committed" |
| 10 | 13–15 | ADDENDUM-n3 `7f4a7a75…9313` at 0744136 bound in VERDICTS, NOT-RUN, G-ANL-n artifact; STR-ADDENDUM3-SHA; commands unchanged | CONFIRMED | shasum; git log; run_verdicts, not_run_doc, ganl_artifact, BOUND_RELS; usage text unchanged |
| 11 | 16–29 | Five raws' hashes and commits (a33252a, 8830589, f4b3e73, ab72d0f, 0744136) | CONFIRMED | shasum; `git log --format='%h %cs'`; tracked and clean |
| 12 | 30–32 | Run of record 242/242, 246 ids, exit 0 | CONFIRMED, pending the run of record | r3.out, r3.exit |
| 13 | 33 | "Route as given", each | CONFIRMED | Last line of all three routing raws |
| 14–16 | 35, 37, 39 | Items 6, 5 and 6 verbatim; (n-5) "[adopt]" in item 1 | CONFIRMED | Byte-equal to first :20, second :19, third :20 and :13 |
| 17 | 41–42 | §4 (b) quote | CONFIRMED | Starred-twelve :56 |
| 18 | 43–45 | Bound to the runner's tile: read L gives (L−cad+1, L); the tail runs to the last read | CONFIRMED | report_problems :6405–6406; runner.py PIN :35–53 and `Monitors.evaluate` |
| 19 | 46–47 | n and k are the tile's records'; a ruling clears nothing; R13 | CONFIRMED | report_problems :6407–6409; `cleared` gone |
| 20 | 48–50 | `check_report` "already fixes" a read fire's bounds and a tail's start; tail end open (obs 4) | IMPRECISE | check_report fixes a tail's start only once the end (bound here) is m−1; example_pause's tail (0, 99) passes its form. "Cannot fire alone" and obs 4 are true (ef105f1 entry, RESULTS.md :49–50) |
| 21 | 51–54 | F1 applied: launch index; scope = runner's SCOPE | CONFIRMED | runner_scope :6318ff; runner `_scope` :309–315; checks at :6413 and :6423 |
| 22 | 55–56 | paused_points unchanged in code | CONFIRMED | Base→draft 4 diff touches its docstring only |
| 23 | 57–58 | The interim sentence, verbatim | CONFIRMED | Starred-twelve :56 |
| 24 | 58–60 | The plan put to n-build and the coordinating session (2026-11-19); no objection | NOT CHECKABLE | Message; Notes :1 ("no objection") covers only the coordinating session |
| 25 | 61 | VERDICTS reads only a campaign's report; no campaign has run | CONFIRMED | report_problems / run_verdicts refuse a non-campaign; no n campaign in RESULTS.md |
| 26 | 62–63 | "The one stage report written with the binomial monitor before the tile, backend-ext-2's … its 24 reads fired nothing" | **FAIL** | backend-ext's own report (6df2131, resumed) was also written before the tile, and its binomial fired: "`p01` was the fidelity binomial's end-of-run fire at `6df2131`: 10 of 24 above TAU" (RESULTS.md, the 2026-11-18 resume entry). backend-ext-2's 0 of 24 is right, and the conclusion holds: neither report is a campaign's |
| 27 | 64–66 | Runner carries the tile from ef105f1; the reader loads only the pinned schema | CONFIRMED | schema_module; SCHEMA_SHA256 |
| 28 | 67 | G-ANL-n's canonical run comes after this commit | CONFIRMED | ef105f1's "Next" |
| 29 | 70–72 | PIN-n-37 (a)/(c), -38 and -39 accepted; arm-naming causes accepted; registers, docstring and header say so | CONFIRMED | Starred-twelve §4; draft 4 :16–21, :2622–2629, PINS |
| 30 | 73–76 | F5: p0 1 of 26 read from the identity, never written; batches take the identity's p0 and alpha; VD-F5-FIXTURES; v6's 0 of 2,400 refused | CONFIRMED | schema example_identity :1647; no "26" in the analyzer; 003ae7d's example was 0/2400; draft 4 :5139–5156 |
| 31 | 77–79 | R13 texts; "VD-CEILING's new case D shows it" | IMPRECISE | D's ceiling read is the standing pause's own (`fired(…)`, not adjudicated), not a ruled one. The ruled-read case R13 names is VD-BATCH-CLEARS's (B4); the reviewer's B4 made this point |
| 32 | 80 | The gate's sources | CONFIRMED | §2.5; A-n3 §3.3–§3.5; third routing item 1 |
| 33 | 81–84 | Decision point; every N2 outcome, INDETERMINATE included, carries f, reasons and gate | CONFIRMED | n2_outcome `why` :609–637 |
| 34a | 85–86 | Line form "…coherence: <k> of 48, PASS" or FAIL | CONFIRMED | A-n3 §3.3; G-CAL-n out raw :379 is the whole line "… 48 of 48, PASS" |
| 34b | 86–87 | "agreed through the coordinating session, 2026-11-19" | NOT CHECKABLE | Relay; Notes :60–69 consistent |
| 35 | 87–88 | Refusals; bar 36 of 48 | CONFIRMED | lock_gate; Gate; LOCK-GATE |
| 36 | 88 | Reads gcal.json nowhere | CONFIRMED | "gcal" appears only in two texts |
| 37 | 88–89 | Early end → refuses, "the default, stated in PIN-n-40" | IMPRECISE | PIN-n-40 says "so VERDICTS refuses, finding none". "The default" is the phrase the reviewer's F4 called unclear, and the analyzer dropped it |
| 38 | 90–91 | Deciding point named "by its existing 'at f = [f]'" | IMPRECISE | INDETERMINATE's form had no "at f = [f]" before v7 (base: "INDETERMINATE: N2 is not evaluated ([causes])"); v7 adds it |
| 39 | 91–92 | Reasons verbatim, checked against the addendum's bytes | CONFIRMED | SENT-ADDENDUM3; §3.4 text |
| 40 | 92–93 | Slot filled at VERDICTS; 385 tuples, 2,561 evaluations | CONFIRMED | r3.out :140 |
| 41 | 93–94 | The code forms' digest moves | CONFIRMED | Draft 1→2 diff |
| 42 | 95–96 | §3.2 quote; nothing built for the leakage half | CONFIRMED | A-n3 :36 |
| 43 | 97–99 | Reach under both branches; STOP on either | CONFIRMED | pinned_map_reach; run_ganl `any(…)` |
| 44 | 99–100 | On db00d6d's map the cap does not bind and nothing merges; the decision is the seat's to state | CONFIRMED | d_eq 0.28692, 2·d_eq 0.574 ≤ 1, no point within 0.05; d639bdd's message ("no point merged, the cap not binding"). See observation 2 |
| 45 | 101 | Readings in PIN-n-40/41, strikable | CONFIRMED | PINS |
| 46–49 | 102–111 | R-A to R-D | CONFIRMED | Referent check obs 3 and 4 (:235–236); S2:50 "gain the gate's clause"; §3.4 quotes; MAP_C (0.49, 0.98); N2-GATE-F10 "c FAIL" ratio 0.98 |
| 50 | 112 | R-E cites "LOCK-n v0.1's gate line" to "§3.4 (i) and §3.5" | IMPRECISE | The phrase is §3.4 (i)'s; §3.5 says "the lock's gate line". This is the review's F4, fixed in PIN-n-40 but repeated here |
| 51 | 114–116 | Declaration wording is the coordinating session's | NOT CHECKABLE | Message; Notes :250–252 records it as condition 5 |
| 52 | 116 | "nothing ran or committed before that delta" | **FAIL (ran)** | Draft 1's run (r1, 239/241) preceded ef105f1's commit: sweep command time compared with `git log %ct`, order only; Notes :318–337. The entry's own Runs bullet and the review raw :18–19 report that run. "Nothing committed" holds |
| 53 | 116–118 | "Six conditions held" (three listed), including the review's run of record on the final bytes | IMPRECISE | The blind review read draft 3 (`309a1c43`), not the final bytes; draft 4 adds runner_scope and the launch-index check, which it never saw. Only its mutants ran on draft 4's run copy |
| 54 | 118 | "Code knows of no committed text that declared v7 after n-build's delta" | IMPRECISE | Code's search (Notes :308–312) was at db00d6d. ef105f1's entry, committed before v7, says "n-analyzer moves its schema pin and its fixtures in its own commit, after this one"; the first routing's item 6 ties the tile's range to "when the runner carries it" |
| 55 | 118–119 | The order lived in relays and notes | NOT CHECKABLE | Message |
| 56 | 119–120 | 1185e15's entry ends "**Next:** G-ANL-n's canonical run, when G-CAL-n pins d_eq." | CONFIRMED | RESULTS.md :1823–1824 |
| 57 | 120 | "each sitting's n-analyzer item puts this delta before it" | IMPRECISE (minor) | The items say "after G-CAL-n's run". "Before the canonical run" comes from §3's F5, carried by "as ruled" / "with F5" |
| 58 | 121 | 230→242 checks; 233→246 ids | CONFIRMED | Base EXPECTED_CHECKS; 1185e15 entry :1687; r3 |
| 59 | 122–127 | Twelve new checks, thirteen ids, NUM-GATE-DECISION-F riding along | CONFIRMED | _REQ diff; covers |
| 60 | 128–130 | Rewritten for the gate (incl. VD-MERGED-ROUTE-A, 30 of 48 FAIL) | CONFIRMED | Diff; `g30` (SENT-CODE-FORMS omitted: observation 7) |
| 61 | 131–134 | RD-PAUSE-POINTS 17 cases; VD-PAUSE-POINTS A–C; VD-CEILING D; VD-BATCH-CLEARS; VD-REFUSE 58; 500→479 | CONFIRMED | Counted 17 cases; r3 :191, :227; bz at 479 |
| 62 | 135–136 | Evaluations counted as the runner counts them | CONFIRMED | _bt_report_for; runner :523–525 |
| 63 | 137–138 | Draft 3 frozen at `309a1c43…926a` (242/242) | CONFIRMED | shasum; r2.out |
| 64 | 139–142 | No MAJOR; F1 MINOR (from v6); F2–F4 NOTE; B1–B4 MINOR; B5–B8 NOTE; 41 mutants, 11 predicted | CONFIRMED | Reviewer's report |
| 65 | 143 | "All taken in draft 4 (`7cc0c78f…10be`)" | IMPRECISE (minor) | F4's last point named SENT-CODE-FORMS too; its description still counts the lock head among "47 sentence forms" (draft 4 :1909) |
| 66–67 | 144–146 | F1–F4 dispositions; disjunct removed | CONFIRMED | d3→d4 diff |
| 68 | 147–148 | B1: "three lock lines the whole line's reconstruction alone refuses" | IMPRECISE | Two (no space; a tab) are refused by reconstruction alone. The third ("beside a line missing the space") is refused as two candidates, as the review raw §2 says |
| 69 | 149–150 | B5–B8 "…; texts" | IMPRECISE (minor) | B8 includes a battery change: N2-GATE-INDET now checks iv's gate (d3→d4 :1638) |
| 70 | 151–152 | "the reviewer's 41 less V33, V37 re-expressed, and eight of Code's" | **FAIL** | Code's are nine (C01, C02, C04, C05, C07, C10, C13, C14, C15; manifest, results.txt). 40 + 9 = 49; "eight" gives 48 |
| 71 | 151 | 49 ran on `9cf85798…3a91` (242/242) | CONFIRMED | Manifest; r3 |
| 73 | 153–154 | V28/V38 survived as predicted; "the battery reaches neither by design" | IMPRECISE | V28: true. V38: VD-REFUSE's adjudicated `bz` claims n = 160 on reads 320–479 of c4 (N1-V's +d_20 cell, no re-computation under the writer's "auto"), so V38's check does fire there. That case is refused by its expected message anyway ("is not on disk", within `probs[:3]`) |
| 74 | 155 | The other eight predicted survivors killed by added cases | CONFIRMED | V07, V08, V14, V15, V34, V36, V37 (re-expressed), V39 |
| 75 | 156 | Committed bytes differ from the mutant base in the repository line | CONFIRMED, pending the commit | diff draft 4 vs mut/base.py: line 65 only |
| 76a | 159–163 | nice -n 19, -I -B, TMPDIR in scratch, cd by glob in a subshell | CONFIRMED | Sweep: three runs in that form; run_mutants.sh |
| 76b | 159–161 | Windows granted; one process at a time; foreground | NOT CHECKABLE | Message |
| 77 | 163–164 | Analyzer prints the interpreter path and arguments, not flags | CONFIRMED | `main()` :6779; r3 INVOCATION line |
| 78 | 165 | Draft 1: 1 run, 239/241, "the forms' digest unset" | IMPRECISE | 239/241 and exit 1 are right. The pin was not unset; it held v6's `41d0d654…b1da` (r1.out :122) |
| 79 | 166 | Draft 3: 1 run, 242/242 | CONFIRMED | r2 |
| 80 | 167 | Draft 4: 1 run, 242/242; mutants "three per call" | IMPRECISE (minor) | 17 calls: 16 of three, the last of one (C10) |
| 81 | 168 | Run of record: 1 | NOT CHECKABLE | Pending the run of record |
| 82 | 170–171 | Q-F3 beside; no other window open | NOT CHECKABLE | Message |
| 83 | 172–173 | "None read anything under `data/`" | **FAIL** | Sweep: `cat data/n/gcal/dose_map.json` (Notes :216 "read whole"); `wc -c` of gcal.json and dose_map.json; shasum, rev-parse and hash-object of the three data/n/gcal files. Not ckpt or reports, but under data/ and undeclared |
| 84 | 174–175 | Sweep since 1185e15's commit, by jq | CONFIRMED | Sweep line 308; cmds.tsv |
| 85 | 176–177 | `ls results/raw \| /usr/bin/grep -c` to find a routing raw's name | CONFIRMED | Sweep line 220. The printed "2" is NOT CHECKABLE (output not recorded) |
| 86 | 178–179 | One /tmp temp file; listed and removed by glob (x_ and digits), unread | CONFIRMED | Sweep lines 212 (`> /tmp/x_$$`) and 213 |
| 87 | 180–182 | jq: tool names, hand-back fields, message saved; own transcript | CONFIRMED | Sweep 265, 266, 308 |
| 88 | 183–187 | The list of git forms outside item 3 | IMPRECISE (incomplete) | Every listed item is in the sweep. Also there and not listed: `git show --stat … 1185e15 -- RESULTS.md` (line 217); `git cat-file -t` of 0744136; four `git show HEAD:<path> \| shasum` blob reads right after v6's commit (line 1); `git log -30 --format='@@%h %ad%n%B'` (author dates and bodies). `--stat` prints counts, not "names, hashes, subjects or text" |
| 89 | 188–191 | "Stated plainly": awk on RESULTS.md once and the memory index twice; perl; sed -n; the runner; memory and notes writes | CONFIRMED | Sweep 18, 20, 67, … (other tools: observation 3) |
| 90 | 193 | One of v6's own corrected in the dated note | CONFIRMED | Dated note item 3 |
| 91 | 194–196 | Reviewer's departures | CONFIRMED | Report's last section |
| 93 | 198–200 | Committed by path; count 0; not pushed | NOT CHECKABLE | Pending the commit |
| 94 | 199–200 | "(the third sitting's §5.2)" | IMPRECISE | The rule is the 2026-11-18 third sitting's §5.2 (n-step4-run-pause answers). In this entry "the third sitting" otherwise means 2026-11-19's, i.e. ADDENDUM-n3, whose §5.2 is the retention-interval declaration |
| 95 | 200–201 | Next: G-ANL-n's canonical run on the dose map of record | CONFIRMED | Consistent with ef105f1 and d639bdd |

(Item 72 duplicates item 4; item 92 is a placeholder.)

## 2. close_1185e15.filled.md

| # | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| C1 | 1–2 | PI date; grounds: the answers' header ("…add their close lines") and §8 item 6 | CONFIRMED | Starred-twelve :3, :86 |
| C2 | 3–4 | Path; `e6ff066d…6d5a`; a33252a; §4 | CONFIRMED | |
| C3 | 5 | (a) and (c) accepted | CONFIRMED | §4 :55, :57 |
| C4 | 6–8 | (b) ruled by §3's R12, with the interim | CONFIRMED | §4 :56 |
| C5 | 9–10 | PIN-n-38 "as read"; PIN-n-39 both ways / one way; arm-naming causes accepted | CONFIRMED | §4 :57 |
| C6 | 11 | "§3 accepts F5, this session's fixtures to move in its pin-move commit" | IMPRECISE (minor) | §3 says "in its own commit, before the canonical run"; "pin-move commit" is routing item 6's phrase |
| C7 | 13–15 | Carried at v7 | CONFIRMED | Entry; draft 4 |

## 3. dated_note_1185e15.filled.md

| # | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| D1a | 1–2 | "On the coordinating session's verification of 1185e15" | NOT CHECKABLE | Message |
| D1b | 2–3 | Three corrections, none changing a figure | CONFIRMED | |
| D2 | 4 | Quote "No placeholder is left in the entry, the close lines or the raws" | CONFIRMED | v6 values-check raw (`git show 1185e15:…`) :727, bold dropped |
| D3 | 5–7 | The pass-2 report names two at-sign placeholders (entry's values-check line; review raw's run-of-record result) | CONFIRMED | v6 raw :325 (@@VC_LINE@@, @@REC_RESULT@@), :577, :645, all within pass 2 (:321–672) |
| D4 | 8–10 | 1185e15's "checkers' departures" bullet omits pass 1's zsh `=` error and refused loop, and pass 2's grep filename prefixes | CONFIRMED | RESULTS.md :1783–1791 against v6 raw :312–319, :669, :736–738 |
| D5 | 11–13 | v6's gate grep took the whole INVOCATION line as its pattern, the venv folder name (holding a marker) in argv | CONFIRMED | n9/v6/commit/commit_steps.sh :73; sweep line 1374 (`commit_steps.sh gate`) |
| D6 | 13–14 | The next version's gate matches the line with no marker | CONFIRMED | SCRATCH/commit/commit_steps.sh :73 (`[^ /]+`); a bracketed-pattern count finds no marker anywhere in that script |

## 4. review.md

| # | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| R1–R6 | 1–15 | Title; base `418c2136…072d`; A-n3 and second-sitting citations; pin to ef105f1 `1cab28df…edff`; first sitting §4 citation | CONFIRMED | |
| R7a | 17–20 | Parallel start; draft 1 ran once (239/241); draft 3 ran once (242/242) | CONFIRMED | r1, r2 |
| R7b | 19 | "the code forms' digest unset" | IMPRECISE | v6's digest stale, not unset (as entry #78) |
| R8 | 21–22 | Frozen read-only copy `309a1c43…926a`, 242/242, 246 ids, against the base and the diff | CONFIRMED | `[ -w ]` false; r2; `diff -u` body equals the saved diff |
| R9 | 23 | A subagent of this session | NOT CHECKABLE | jq over a task output is consistent |
| R10–R11 | 23–31 | Brief `97e7cc10…a496`: items 1–5, amendments, standing lines, no interpreter but shasum; the specification list | CONFIRMED | review/BRIEF.md |
| R12 | 32 | "It executed no code." | IMPRECISE | It ran awk filters, which its own report calls "an interpreter … breaches 'no interpreter at all'" |
| R13–R14 | 32–40 | Commands; no git; nothing under data/; findings; 41 mutants; 11 predicted (list) | CONFIRMED | Report |
| R15 | 41–42 | "Every finding is taken" | IMPRECISE (minor) | SENT-CODE-FORMS half of F4 (as entry #65) |
| R16 | 43–44 | "…and eight of Code's: 49" | **FAIL** | Nine (as entry #70); the review raw's own §2 composition gives 6 + 3 = 9 |
| R17 | 44–45 | Ran once each on `9cf85798…3a91` (242/242, 246); 47 of 49 | CONFIRMED | |
| R18 | 45–46 | V28/V38 each "a check the battery does not reach by design" | IMPRECISE | As entry #73 |
| R19 | 46–47 | Other eight killed by added cases | CONFIRMED | |
| R20a / R20b | 51–54 | Run forms / windows | CONFIRMED (sweep) / NOT CHECKABLE | |
| R21 | 56–57 | Each mutant an exact one-time `.old→.new` replacement | CONFIRMED | All 49 py files = base with one hunk equal to `.old`/`.new`; each `.old` a single line occurring once in the base |
| R22 | 57–58 | The coordinating session checked hashes, read the runner, checked changed lines | NOT CHECKABLE | |
| R23 | 59 | "Killed" = non-zero exit | CONFIRMED | exits.txt |
| R24 | 63–65 | §1 reproduced whole from the hand-back by jq (`d0dad6c2…3b06`); paths by description | CONFIRMED | Lines 67–349 = report.md (which has one extra trailing blank line); no literal path |
| R25–R28 | 357–378 | F1–F4 dispositions as applied | CONFIRMED | d3→d4 diff. F2's "the coordinating session had already checked" is NOT CHECKABLE (Notes :423–426 consistent) |
| R29–R36 | 382–404 | B1–B8 dispositions (18 refusals; 35 FAIL lock on the example map, runs 79–159 at 0.015; k = 1; 2 of 2 / 1 of 1; scopes; kinds; 17th case; order texts; iv's gate) | CONFIRMED | Code and r3 |
| R37 | 408–412 | Composition: duplicates C06=V39, C08=V04, C09=V02, C11=V09, C12=V22; C03 moot; C05 re-expressed; C13–C15 new | CONFIRMED | `.old`/`.new` identical pairwise; C03 = V33 |
| R38–R40 | 416–424 | Base hash; manifest 51 lines `d6d45817…51b4`; runner `60d029dd…c000`; three per call (last one); results and exits hashes, 49 lines | CONFIRMED | `shasum -c` on the manifest: 51 OK |
| R41 | 425–427 | V38: "every fixture's adjudicated batch is already a tile of the records" | **FAIL** | `bz` (draft 4 :5589–5592): example_pause gives n = 160 on reads 320–479 of c4. That is N1-V's +d_20 cell (PLAN_TABLE order), which carries no re-computation (`fidelity="auto"` → dose rule only, schema :1707–1708), so its tile has 0 trials. V38 survives because that case's expected "is not on disk" still appears among `probs[:3]`. Derived by reading, not running. V28's explanation is right |
| R42 | 429–479 | Mutant table | CONFIRMED | Identical to mut/table.md; every row equals results.txt |
| R43 | 486–491 | Runs table: r1 `71eb884a`/`4fe3b573`, exit 1; r2 `309a1c43`/`ad969e87`, exit 0; r3 `9cf85798`/`9196c33e`, exit 0; mutants 47/2/0 | CONFIRMED | |
| R44 | 494–495 | Q-F3 beside the runs | NOT CHECKABLE | |
| R45–R47 | 503–507 | 385/2,561 and tallies unchanged; slot, no sentence set; digest moved once at draft 2, `41d0d654…b1da`→`47883844…be4d`, from run 1's print | CONFIRMED | r3 :139–140; d1→d2 diff; r1 :122; unchanged in d2→d4 |

## 5. n_analyze.draft4.py, the new and changed texts

**CONFIRMED (59):**
- Module docstring paragraph; PINS header comment; §10 header; ADDENDUM3_REL and ADDENDUM3_SHA256; SCHEMA_SHA256 with its "# ef105f1".
- GATE_STATES, GATE_N and GATE_BAR (§3.3 quote, elided); WHY_SLOT, N2_WHY and ADDENDUM3_FORMS with their comments; CODE_FORMS_SHA256.
- PIN-n-37 (the §4 (a) and (b) quotes are verbatim); PIN-n-38; PIN-n-39; PIN-n-40 (form, parse, refusals, the §3.4 (i)/§3.5 citations, the backticked §3.5 quote, gcal.json never read); PIN-n-41; PIN-n-42; OPEN-Q7's sentence.
- Docstrings and comments of: n2_decision_f, n2_reasons, Gate, State, n2_outcome, outcomes, why_text, fill, code_forms, addendum3_spans, lock_gate, run_verdicts, build_state, map_reach, coupling_shape (with map_reach_by_hand), pinned_map_reach, run_ganl's STOP, ganl_artifact, schema_module, runner_scope (matches runner `_scope` and the SCOPE pin), paused_points, _bt_report_for, _bt_lock_text.
- Checks: N2-GATE-F10, N2-GATE-DECIDES, N2-GATE-INDET, N2-GATE-GREAD, NUM-CAP-DECISION-F, SENT-FILLED-N2-GATE (six sentences, four STOPs), SENT-FILLED-N2-CAP, SENT-ADDENDUM, SENT-ADDENDUM3, REACH-GATE-FAIL, RD-GATE-FAIL, RD-PAUSE-POINTS (17 counted), VD-PAUSE-POINTS (tiles, scopes, kinds), VD-F5-FIXTURES, VD-BATCH-CLEARS (7,280 reads; tail 7200–7279; 7207 and 7220; 2 of 2), VD-GATE (ct1 as stated), LOCK-GATE (18), VD-REFUSE (58; bz at 479), VD-MERGED-ROUTE-A (R_ell 40 gives d_eq 0.523, cap binds, both merge), STR-GANL-ARTIFACT, CMD-NOTRUN, STR-ADDENDUM3-SHA.

**IMPRECISE (2):**
- report_problems docstring: "a tail's start, which check_report's form of a tile implies". It is implied only given the tail's end that this function binds (as entry #20).
- VD-CEILING: D's description cites "(R12, R13)" for an unruled ceiling read (as entry #31).

**NOT CHECKABLE (1):**
- GATE_LINE_HEAD's comment "as n-build's lock draft carries it". The draft is uncommitted. The form matches §3.3 and G-CAL-n's printed line.

## Counts

| Text | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|
| Entry | 65 | 16 | 4 | 10 |
| Close line | 6 | 1 | 0 | 0 |
| Dated note | 6 | 0 | 0 | 1 |
| Review raw | 39 | 4 | 2 | 5 |
| Analyzer | 59 | 2 | 0 | 1 |
| **Total (221)** | **175** | **23** | **6** | **17** |

## Observations

1. **"A.6" means two things in one entry.** Lines 4 and 199 use it for the first sitting's item 6. Line 114's "v7's A.5/A.6 code" follows Code's notes, where A.5 is the second sitting's item 5 and A.6 the third sitting's item 6. All three routings file these under "A.", yet line 4 labels only the first.
2. **d639bdd is not cited.** The seat's answers of 2026-11-20 (d639bdd, HEAD) already read G-CAL-n's record ("the gate PASSED, so N2 decides at f = 0.20", per its commit message) and route the pin move. The entry cites neither, and says the decision "is the seat's to state". Notes :522–525 stage later edits (routing item A.5, the seat's §3, PIN-n-42's bullet, the Perl runs, hole 12, the Next line). Those texts are unchecked here.
3. **Undeclared commands in the sweep.** Beyond entries #83 and #88: `ls -la` of the shared-notes folder, the memory index and scratch folders; `wc -c` of memory files; `find . -exec touch -c {} +` over the scratchpad; `od -c`; an `rm` in the shared-notes folder. Notes :520–521 record the coordinating session's request to name the Perl scripts, which is not yet in the entry. The sweep ends at its own jq command, so later steps (commit_steps.sh, place.pl, this check's brief) are outside it.
4. **Quoted declaration vs. Runs bullet.** The declaration was worded before any run (Notes :250). The entry's Runs bullet, and the review raw :18–19, contradict its "nothing ran".
5. **Source of entry #26.** Notes :9 says "no stage ran the monitors before n-build's delta", which backend-ext's p01 contradicts.
6. **"A lock that also quotes it … is refused".** In PIN-n-40 and lock_gate this holds only for a quote on a line of its own that begins with the head. A mid-line or blockquoted quote is not counted.
7. **SENT-CODE-FORMS.** Its description changed but is missing from the entry's list of rewritten checks. It still calls the lock head a "sentence form".
8. **ganl_artifact's spec.** It names ADDENDUM-n3 §3.3–§3.5 but none of the 2026-11-19 sittings' answers that v7 carries.

## Commands beyond reading files and the brief's git forms

- **Interpreters, against "no interpreter at all":** one `awk` call, to find which functions enclose three line numbers of draft 4; one `sed -n 2p`, to pick a line of grep output.
- **Other tools:** `date -j -u -f` to turn a sweep timestamp into epoch seconds, compared with `git log -1 --format=%ct ef105f1` (printed only the order); `[ -w file ]`; zsh loops over literal id lists; head, tail, cut, wc -l, fold, sort, uniq, tr, cat, name-only ls (scratch folders only); `diff`/`diff -u` (headers stripped).
- **Writes:** `mkdir -p SCRATCH/vc/checker`; all output files under that folder only.
- **Reads beyond the named sources:**
  - via `git show 1185e15:<path>` (saved in the checker folder): v6's values-check raw;
  - via `git show HEAD:<path> | grep`: the 2026-11-18 third-sitting answers raw, by path;
  - RESULTS.md's backend-ext resume and backend-ext-2 entries;
  - n9/v6/commit/commit_steps.sh and SCRATCH/commit/commit_steps.sh.
- **Not done:** nothing under data/ read, listed or searched; results/raw not listed; no marker string in any argv (bracketed patterns used); no Python.
- **Times:** sweep timestamps were printed to my session once and are written nowhere.

## Pass 1: Code's dispositions

FAILs (6), each fixed:
- #26 (entry, the interim's grounds): backend-ext's report (its end-of-run fire `p01`, 10 of 24 above TAU, cleared
  by the seat as the measurement) is named beside backend-ext-2's; both are no campaign's.
- #52 (entry, the parallel start): the declaration is quoted as the coordinating session worded it, before any run,
  and the entry says which part no longer holds: draft 1 ran once before the delta's commit, in a development window.
- #70 / R16 (entry, review raw): nine of Code's mutants, not eight (C01, C02, C04, C05, C07, C10, C13, C14, C15).
- #83 (entry, departures): "None read anything under data/" narrowed to data/*/ckpt, data/*/reports and data/mf3;
  Code's reads of G-CAL-n's three committed files under data/n/gcal/ are declared.
- R41 (review raw, V38): the fixture was wrong, not the text alone. VD-REFUSE's `bz` fired at read 479, a tile with no
  trial on c4; draft 5 moves it to read 159 (N1-V's +1 cell, 160 trials). The review raw's §3 and §5 and the entry
  say why V38 survived on draft 4 and what changed.

IMPRECISE (23), each applied: #20 and the report_problems docstring (a tail's start fixed once its end is bound);
#31 and VD-CEILING D's texts (R13's ruled read is VD-BATCH-CLEARS'; D is R12 alone); #37 ("VERDICTS refuses, finding
none"); #38 ("which INDETERMINATE's form now carries too"); #50 (R-E's citations); #53 (the conditions: the review
read draft 3, its dispositions mutation-tested, not reviewed again); #54 (the committed texts that tied v7 to the
delta are named); #57 (the items' words, and §3's F5 "before the canonical run"); #65 and observation 7
(SENT-CODE-FORMS' description, and its place in the entry's list); #68 (B1: two lock lines refused by reconstruction
alone, one as two candidates); #69 (B8's battery change named); #73 / R18 (V38's reason); #78 / R7b (the forms'
digest still v6's, not unset); #80 ("three per call, the last call one"); #88 (the git forms listed whole; the
`git log -30` with item 3's pathspec stated apart); #94 (the 2026-11-18 third sitting's §5.2); C6 (the close line:
"in its own commit, before the canonical run", with the routing's words beside); R12 (the reviewer ran no Python and
no repository code; its awk is named as its brief barred it); R15 (as #65).

NOT CHECKABLE (17): messages and relays, left as stated; #9's parenthetical corrected to "its conditions 1 and 2".

Observations (8): 1, the routings' labels made explicit (A.6 of the first and third sittings, A.5 of the second, and
2026-11-20's A.5); 2, d639bdd cited (its §3, §5.1's hole 12, §0 and §2's decision at f = 0.20, §7 item 5) with the
routing item; 3, the undeclared commands added to the departures (`ls -la`, `wc -c`, the `touch -c` sweep, `od -c`,
an `rm` in the shared notes folder), with the Perl scripts' runs, and a second sweep before the commit; 4, as #52;
5, as #26; 6, PIN-n-40 and lock_gate say a quotation on a line of its own counts, one inside another line or
blockquoted does not; 7, as #65; 8, ganl_artifact's spec now names the answers of 2026-11-19 it carries.

## Pass 2: the report, as saved from its hand-back (unedited)

# Values-check, second pass: the v7 entry, the close line on 1185e15's entry, the review raw, and draft 5's changed regions

**Inputs.** BRIEF2 hashed to `cc2757aa…7aae`, as given. The four texts hashed to the values handed over: entry `982d5e4a…670e`, close line `835d4a69…e38e`, review raw `d6244913…af0`, draft 5 `735da934…a7a8`. Draft 4 is `7cc0c78f…10be`. Paths use the brief's labels SCRATCH and REPO. "Notes" means Code's notes (`SCRATCH/../next/v7_notes.md`). "Sweep" means `SCRATCH/sweep/since_v6.tsv`, cited by line number.

**Verdict in one line:** no FAIL. Every first-pass FAIL is resolved. Of the 23 first-pass IMPRECISE items, 20 are resolved, 2 are only partly resolved (#65 and R15), and 1 (#53) is resolved in substance but its rewrite brought a new imprecision. The revisions added a few new imprecisions; none is a FAIL.

## 1. entry.filled.md (99 claims)

| # | Line | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | 1 | Dated 2026-11-20; title | CONFIRMED | HEAD's commits are dated 2026-11-20 |
| 2 | 1–2 | Tile, F5 and R13 on n-build's delta `ef105f1` | CONFIRMED | ef105f1's entry, RESULTS.md :154–268 |
| 3 | 2–6 | The listed sources and routing items | CONFIRMED | Starred-twelve §3 :47, §4 :53; second sitting §2.5 :47; A-n3 §3.2–§3.5 :36–42, §8.3 (4) :79; 2026-11-20 §3 :39; the four routings' "A." items |
| 4 | 6 | Battery 242/242 | CONFIRMED, pending the run of record | r3.out :244; draft 5's changes read (§4 below) |
| 5 | 6 | 47 of 49 killed | CONFIRMED | exits.txt: 47 × exit 1, V28/V38 exit 0; results.txt |
| 6 | 6–7 | Five readings R-A..R-E, Code's | CONFIRMED | PIN-n-41 (a)–(d); PIN-n-40's v0.1/v1.0 reading |
| 7 | 7 | Nothing ran on a model or the box; no stage ran | NOT CHECKABLE | The sweep holds no remote or stage command |
| 8 | 10 | `418c2136…072d` at `1185e15` | CONFIRMED | `git show 1185e15:scripts/n_analyze.py \| shasum`; base-1185e15.py equal |
| 9 | 10 | Hole 12 (2026-11-20 §5.1) | CONFIRMED | Answers :54 |
| 10 | 11–12 | Pin from 003ae7d's `5cbf60db…574c` to ef105f1's `1cab28df…edff` | CONFIRMED | Blob hashes at both commits; base :2766; draft 5 :3050 |
| 11 | 12–13 | Verified before the dependent parts were written ("conditions 1 and 2") | NOT CHECKABLE | Message. Notes :242–245 and :337 are consistent |
| 12 | 14–16 | ADDENDUM-n3 `7f4a7a75…9313` at 0744136 is bound in VERDICTS, NOT-RUN and the artifact; STR-ADDENDUM3-SHA; commands unchanged | CONFIRMED | shasum; `--diff-filter=A`; draft 5 :4666, :5888, :5940, :6697, :2980; docstring usage and argparse lines unchanged from the base |
| 13–16 | 18–33 | Seven raws' sha256s and commits (a33252a, 8830589, f4b3e73, ab72d0f, 0744136, d639bdd) | CONFIRMED | shasum of each; `git log --diff-filter=A`; each tracked and clean (rev-parse vs hash-object) |
| 17 | 34–36 | Run of record 242/242, 246 ids, exit 0 | CONFIRMED, pending the run of record | r3 |
| 18 | 37 | "Route as given", each | CONFIRMED | Last line of all four PI routing raws |
| 19–21 | 38–44 | Items 6, 5 and 6 verbatim; (n-5) "[adopt]" in item 1 | CONFIRMED | Whole-line `grep -Fxf` match against each routing raw (:20, :19, :20); third routing :13 |
| 22 | 45–47 | 2026-11-20's item 5, quoted "as its answers' routing block words it" | **IMPRECISE** | The quote equals the answers raw :75. But it sits under "The PI's routings … verbatim", and the PI's own block is committed at `bc85386` (HEAD) as `results/raw/2026-11-20_first-sitting_pi-routing.md`, item 5 at :19. The entry neither cites nor quotes that raw. The relay with "PI: Route as given" is borne out by that raw's last line and by RESULTS.md :34–35 ("A.5 verbatim to n-analyzer") |
| 23 | 48–50 | 2026-11-20 §3 accepts the readings and puts the pin move next (quote); O6 rides n-build's schema change | CONFIRMED | Answers :41, :46 (quote exact); RESULTS.md :36–39 |
| 24 | 51–52 | §4 (b) quote | CONFIRMED | Starred-twelve :56 |
| 25 | 53–55 | Batch bound to the runner's tile: a fire at L is (L−cad+1, L); at the run's end, the tail | CONFIRMED | Draft 5 :6411–6419; runner PIN :35–53. v6 bound the trials since the last cleared batch (base :5847–5864) |
| 26 | 56–57 | n and k are the tile's; a ruling clears nothing; R13 | CONFIRMED | :6415–6417; no `cleared` left |
| 27 | 58–61 | check_report fixes a read fire's bounds, and a tail's start once its end is bound; the tail's end (values-check obs 4) and n, k are bound here alone | CONFIRMED (#20 resolved) | schema :1477–1487; RESULTS.md :178–181 |
| 28 | 62–65 | F1: read at its launch index; scope is the runner's SCOPE; v6 required only the batch's trials' arms | CONFIRMED | Draft 5 :6325–6337, :6421, :6431; runner `_scope` :309–315; base :5863 |
| 29 | 66–67 | paused_points unchanged in code | CONFIRMED | Base vs draft 5: docstring lines only |
| 30 | 68–69 | Interim sentence verbatim | CONFIRMED | Starred-twelve :56 |
| 31 | 69–70 | Plan put to n-build and the coordinating session; no objection | NOT CHECKABLE | Notes :1 is consistent |
| 32 | 72 | VERDICTS reads only a campaign's report; no campaign has run | CONFIRMED | `report_problems` :6369; no n campaign entry in RESULTS.md |
| 33 | 73–75 | backend-ext's p01 (10 of 24) cleared as the measurement; backend-ext-2's 24 reads fired nothing | CONFIRMED (#26 resolved) | RESULTS.md :2727–2728; :2373–2384 (COMPLETE, no pause, 0 of 24). See observation 4 |
| 34 | 76–78 | The runner carries the tile from ef105f1; the reader loads only the schema it pins | CONFIRMED | `schema_module` :3068–3079 |
| 35 | 79 | Canonical run comes after this commit | CONFIRMED | 2026-11-20 §3 :46, §7 :75 |
| 36 | 82–84 | PIN-n-37 (a)/(c), -38 "as read", -39 both-ways/one-way, arm-naming causes; registers, docstring, header | CONFIRMED | Starred-twelve §4 :55–57; draft 5 :16–21, :2626–2630, PINS |
| 37 | 85–88 | F5: p0 1 of 26 (floor 1 of 3), read from the identity and never written; batches take the identity's p0 and alpha; VD-F5-FIXTURES; 0 of 2,400 refused | CONFIRMED | schema :1630, :1647, :878; no p0 literal in draft 5; :5141–5158 (see observation 7) |
| 38 | 89–91 | R13 texts; VD-BATCH-CLEARS: 2 of 2, and a report leaving the read out is refused | CONFIRMED (#31 resolved) | PIN-n-37; :5323–5384 |
| 39 | 92 | Gate's sources; (n-5) adopted | CONFIRMED | §2.5; A-n3 §3.3–§3.5; third routing :13 |
| 40 | 93–96 | Decision point; every N2 outcome carries f, reasons and gate | CONFIRMED | A-n3 :40; draft 5 :609–615, :635 |
| 41 | 97–99 | Line form per §3.3 | CONFIRMED | A-n3 :38; G-CAL-n out raw :379 is exactly that whole line |
| 42 | 98–99 | Agreed by relay on 2026-11-19; no committed text records it | NOT CHECKABLE | Notes :60–69. RESULTS.md has no such record |
| 43 | 100–101 | Refusals; bar 36 of 48 | CONFIRMED | `lock_gate` :6268–6282; `Gate` :410–415 |
| 44 | 101 | `gcal.json` read nowhere | CONFIRMED | Appears only in texts (:2808–2809, :6260) |
| 45 | 101 | An early end writes no line, so VERDICTS refuses, finding none | CONFIRMED (#37 resolved) | PIN-n-40 :2807–2809; A-n3 :71 |
| 46 | 102–104 | "at f = [f]", now in INDETERMINATE too; reasons verbatim, checked against the bytes | CONFIRMED (#38 resolved) | Base :721 vs draft 5 :777; :781; SENT-ADDENDUM3 |
| 47 | 104–106 | Slot filled at VERDICTS; 385 / 2,561; digest moves | CONFIRMED | `fill` :3587–3592; r3 :140 |
| 48 | 107–108 | §3.2 quote; nothing built | CONFIRMED | A-n3 :36, exact |
| 49 | 109–112 | Reach under both branches, STOP on either; db00d6d's map uncapped and unmerged; decision at f = 0.20 (§0, §2) | CONFIRMED | `pinned_map_reach` :5909–5922; answers :8, :28 |
| 50–55 | 113–125 | R-A to R-E | CONFIRMED (#50 resolved) | Referent check :235–236; S2 :50; §3.4 quotes; MAP_C = (0.49, 0.98) |
| 56 | 126–129 | The declaration quote, worded before any run | NOT CHECKABLE | Notes :250–252 match it verbatim |
| 57 | 129–131 | Draft 1 ran once before the delta's commit (239/241); nothing committed before it | CONFIRMED (#52 resolved) | Sweep :138's time is after db00d6d's and before ef105f1's commit time (order only, by `date`/`%ct`); r1.out; no commit between db00d6d and ef105f1 |
| 58 | 132–133 | "Its conditions: … this battery's run of record and this values-check on the final bytes" | **IMPRECISE** | Notes :248 give condition 4 as "The battery, review and values-check of record run on v7's final bytes". The restatement drops the review. The next sentence does disclose that the review read draft 3. The later accepted order (notes :442–444) is not mentioned |
| 59 | 133–134 | The review read draft 3, written after the delta; dispositions mutation-tested only | CONFIRMED (#53 resolved in substance) | r2's run follows ef105f1's commit |
| 60 | 135–139 | Committed texts tying v7 to the delta (quotes; "in its own commit, after this one"; committed after the parallel start) | CONFIRMED (#54 resolved) | First routing :20; second :19; third :20; RESULTS.md :210 |
| 61 | 139–140 | 1185e15's entry ends "**Next:** …"; §3's F5 "before the canonical run" | CONFIRMED (#57 resolved) | RESULTS.md :2015–2016; starred-twelve :50 |
| 62 | 141 | 230→242 checks; 233→246 ids | CONFIRMED | v6 self-test raw :231, :233; r3 |
| 63 | 142–147 | Twelve new checks, thirteen ids, NUM-GATE-DECISION-F riding | CONFIRMED | All 13 ids are absent from the base and present in draft 5; :2555 |
| 64 | 148–151 | Rewritten for the gate, SENT-CODE-FORMS included; Route A lock 30 of 48, FAIL | CONFIRMED (obs 7 resolved) | :1909–1914; `g30` :5433 |
| 65 | 152–156 | RD-PAUSE-POINTS 17 cases; A–C end at their standing tiles; VD-CEILING D; VD-BATCH-CLEARS; VD-REFUSE 58; read 500→159 | CONFIRMED | Cases counted at :4284–4335; r3 :227; base :5116 (500) → draft 5 :5593 (159) |
| 66 | 157–158 | Evaluations counted as the runner does | CONFIRMED | `_bt_report_for` :4768–4784 |
| 67 | 160 | Draft 3 frozen at `309a1c43…926a` (242/242) | CONFIRMED | r2. Minor: that hash is draft 3's run copy; draft 3 itself is `1141d17b…c59b` |
| 68 | 160–164 | No MAJOR; F1 MINOR (from v6); F2–F4 NOTE; B1–B4 MINOR; B5–B8 NOTE; 41 mutants, 11 predicted | CONFIRMED | §1 report |
| 69 | 165 | "All taken in draft 4" | **IMPRECISE (minor; #65 partly resolved)** | The bullet at :168 itself says SENT-CODE-FORMS' description was taken "at the values-check", which is draft 5 :1909–1912 |
| 70–73 | 166–173 | F1; F2–F4; B1–B4; B5–B8 dispositions | CONFIRMED (#68, #69 resolved) | Draft 5 code; `len(bad_g) == 18` |
| 74 | 174–175 | 49 on `9cf85798…3a91`; 41 less V33, V37 re-expressed, nine of Code's; 47/49 | CONFIRMED (#70 resolved) | Manifest; specs |
| 75 | 176–179 | V28 and V38; V38 met bz at 479 with no trial, case refused anyway with its message in the first three; moved to 159 | CONFIRMED (#73 resolved) | By reading: `probs[:3]` :6706; plan order; see §4 |
| 76 | 180 | The other eight killed by added cases | CONFIRMED | V07, V08, V14, V15, V34, V36, V37, V39 killed |
| 77 | 181–182 | Committed bytes differ from the base in the repository line, the fixture's read and texts | CONFIRMED, pending the commit | diff: 9 regions |
| 78 | 185–188 | nice -n 19, `-I -B`, TMPDIR in scratch, foreground, one at a time | CONFIRMED | Sweep :138, :232, :275; run_mutants.sh |
| 79 | 185–186 | Windows granted; bytes named first | NOT CHECKABLE | Sweep :138 checks the granted hash before r1 |
| 80 | 188–189 | Reached by `cd` with a glob in a subshell; no argv names the path | CONFIRMED | Sweep commands use a short glob, no marker |
| 81 | 189–190 | Prints the interpreter path and its args, not flags; the raw's header names them | CONFIRMED (header pending) | Draft 5 :6787; r3 :1; commit_steps.sh :51 names -I and -B |
| 82–84 | 191–193 | Draft 1: 239/241, digest v6's `41d0d654…b1da`; draft 3: 242/242; draft 4: 242/242, mutants three per call with one last | CONFIRMED (#78, #80 resolved) | run1's pin; r1 :122; sweep: 17 runner calls, 16 × 3 + 1 |
| 85 | 194 | Run of record: 1 | NOT CHECKABLE | Pending the run of record |
| 86 | 196–197 | Q-F3 beside; no other window | NOT CHECKABLE | Message |
| 87 | 198–199 | Nothing read under ckpt/reports/mf3; no repo code outside the windows; no model process | CONFIRMED (#83 resolved) | Sweep: ckpt/reports/mf3 appear only in exclusions or text |
| 88 | 200–201 | Sweep since 1185e15's commit, by jq | CONFIRMED | Sweep :1 (right after v6's commit), :308 |
| 89 | 202–203 | `ls results/raw \| grep -c` | CONFIRMED | Sweep :220. The printed "2" is NOT CHECKABLE |
| 90 | 204–205 | /tmp temp file, listed and removed by glob | CONFIRMED | Sweep :212–213 |
| 91 | 206–208 | data/n/gcal reads (shasum, rev-parse, hash-object; wc -c; cat) | CONFIRMED | Sweep :40, :43, :48. "121 B" is NOT CHECKABLE (I read nothing under data/) |
| 92 | 209–211 | jq reads | CONFIRMED | Sweep :265, :266, :308. The values-checker's came after this sweep (notes :545) |
| 93 | 212–219 | Git forms outside item 3 | CONFIRMED (#88 resolved) | Each is in the sweep (:1, :4, :33, :62, :145, :146, :217, :223). Omissions: observation 2 |
| 94 | 221–226 | "Stated plainly" list | CONFIRMED for each item named | Sweep :18, :20, :67; :54, :55, :125; :13, :25, :41, :42, :46; :2, :15; :47; :210. Gaps: observation 2 |
| 95 | 228 | One of v6's departures corrected in the dated note | CONFIRMED | Dated note's third item |
| 96 | 229–231 | Reviewer's departures | CONFIRMED | Report's last section |
| 97 | 234–235 | "(the seat's answers of 2026-11-18, third sitting, §5.2)" | CONFIRMED (#94 resolved) | That raw's §5.2 :38 is the home-prefix count over the staged diff |
| 98 | 233–235 | Committed by path; count 0; not pushed | NOT CHECKABLE | Pending the commit |
| 99 | 236–237 | Next: canonical run → hole 13 | CONFIRMED | Answers §3 :46, §7 :75, §5.1 :54. "Own window and commit" matches notes :533–534 |

## 2. close_1185e15.filled.md (7 claims, all CONFIRMED)

- C1 (lines 1–2): the n-analyzer's close line, per the answers' header (:3, "add their close lines") and §8 item 6 (:86).
- C2 (lines 3–4): the path, `e6ff066d…6d5a` and `a33252a` are right, and §4 is the section cited.
- C3 (line 5): (a) and (c) accepted (§4 :55, :57).
- C4 (lines 6–8): (b) ruled by §3's R12, with the interim (§4 :56).
- C5 (lines 9–10): PIN-n-38, PIN-n-39 and the arm-naming causes (§4 :57).
- C6 (lines 11–12): "in its own commit, before the canonical run" (§3 :50) and the routing's "in the pin-move commit" (:86; PI routing :20). First-pass C6 is resolved.
- C7 (lines 14–16): what v7 carries matches the entry and draft 5.

## 3. review.md, everything but §1's reproduced report and §3's table (63 claims)

**CONFIRMED (49):**
- Lines 1–15: title and PI date; the entry's title as quoted; the base `418c2136…072d`; A-n3 at 0744136 §3.3–§3.5 with the second sitting's §2.5 (path, `887b7646…dc87`, f4b3e73) and PIN-n-40 to PIN-n-42; the pin to ef105f1 `1cab28df…edff`; the first sitting's §4 (path, `e6ff066d…6d5a`, a33252a).
- Lines 18–20: draft 1 ran once (239/241, the digest still v6's), and draft 3 once (242/242). First-pass R7b is resolved.
- Lines 21–22: the frozen copy is read-only (`test -w` false), `309a1c43…926a`, 242/242 with 246 ids. The saved diff's body equals a fresh `diff -u` from the base.
- Lines 23–31: the reviewer's brief is `97e7cc10…a496`. It quotes items 1–5, C.2 and the fourth sitting's §6.2, and the standing lines; "no interpreter … shasum excepted" is at :96–97; the specification is at :14–38.
- Lines 32–35: "ran no Python and no repository code", the commands as the report lists them, awk barred by the brief, no git, nothing under data/. First-pass R12 is resolved.
- Lines 36–40: F1–F4 and B1–B8 with their severities, and the 11 predicted survivors.
- Lines 43–45: 40 + 9 = 49 mutants, on `9cf85798…3a91` (242/242, 246 ids), 47 of 49 killed. First-pass R16 is resolved.
- Lines 45–47: V28 by design; V38's account; the other eight killed by added cases. First-pass R18 is resolved.
- Lines 48–49: the committed file differs from the base in the repository line, one fixture's read and seven text regions (pending the commit).
- Lines 52–55: the run forms, per the sweep and the runner.
- Lines 57–60: each of the 49 mutant files is the base with its `.old` replaced by its `.new`, one hunk each, and each `.old` occurs once in the base. "Killed" means a non-zero exit.
- Lines 64–66 (§1's preamble): the report is `d0dad6c2…3b06`. §1 lines 68–350 equal it, less its trailing blank line.
- §2:
  - F1: the refusal texts are at :6432 and :6422. The runner writes a pause at its read's launch index (runner :444, :481, :514, :27).
  - F3 and F4 are as described.
  - B1: 18 refusals.
  - B2: VD-GATE :5452–5481.
  - B3: A's tile is (6560, 6719, 2, 1).
  - B4: the tail is [7200, 7279, 2, 2], and the 1-of-1 report is refused.
  - B5: B's scope is the five arms; C's kinds are three.
  - B6: the 17th case; V39 is killed.
  - B7: :4277–4280.
  - B8.
  - The mutant composition: C06, C08, C09, C11 and C12 have `.old`/`.new` identical to V39, V04, V02, V09 and V22; C03 equals V33; V33's line is in the frozen copy but not the base.
- §3:
  - The base differs from draft 4 only at line 65.
  - Manifest: 51 lines, `d6d45817…51b4`; `shasum -c` gives 51 OK. Runner: `60d029dd…c000`.
  - Runs: 17 calls. results.txt is `ad38a3ab…29ff`; exits.txt is `5779a4c1…f8fa`, 49 lines.
  - V28's account.
  - V38: at 479 the tile was N1-V's +d_20 cell, with no trial; at 159 it is N1-V's +1 cell with 160 trials, k = 0. Every adjudicated batch in the fixtures is now a tile of the records: `fired()` builds its batches from `tile_of`, and the other adjudicated pauses carry no binomial. First-pass R41 is resolved.
- §4 rows r1, r2, r3 and the mutant row: hashes, results and exits all match.
- §5:
  - Nine change regions, as `diff` counts them.
  - bz's move, and its case still refused by "is not on disk".
  - The seven text regions are the diff's hunks.
  - No mutant's changed line falls in a differing region, and all 49 `.old` lines occur once in draft 5.
  - V38 would survive, by reading: no mutant output names the `pause-read` case.
  - CODE_FORMS_SHA256 is the base's.
- §6:
  - 385 / 2,561.
  - The hand-tally function is identical to the base's.
  - The deciding branch is a slot.
  - The digest moved once, at draft 2: from `41d0d654…b1da` (drafts 1 and 1's run copy) to `47883844…be4d` (draft 2 onward; r1 :122 printed it).

**IMPRECISE (6):**
- Line 41–42 ("draft 4 carries them") and line 354 ("Draft 4 … carries them all"): F4's SENT-CODE-FORMS description is in draft 5, as §2's own F4 says ("applied at the values-check"). First-pass R15 is only partly resolved.
- Lines 369–371, F2: "a lock that also quotes it, or states its form on a line of its own, is refused". This is draft 4's PIN-n-40 wording. As behaviour it overstates: a quotation inside another line, or blockquoted, is not counted. Draft 5's PIN-n-40 says so, as §5 records. First-pass observation 6 was not carried into §2.
- Lines 507–508 ("the scratch drafts gave [it] as an absolute path") and line 521–522 ("the drafts' absolute line"): drafts 1–5 all compute `REPO` at line 64/65. The run copies (`run1`, `run2`, `mut/base.py`) gave the absolute path. The root equality itself holds.
- Line 528 (minor): "moved … with the new forms (ADDENDUM-n3's two reasons, Code's clause around them and the lock line's head)". C_N2's four forms also changed: each gained `[why]`, and INDETERMINATE gained "at f = [f]" (base :711–721 vs draft 5 :767–777).

**NOT CHECKABLE (8):**
- Line 17–18: the parallel start on the coordinating session's word (notes :233–252).
- Line 23: "a subagent".
- Line 52–55: the windows, bytes named first, and nothing on a model or the box.
- Line 58–59: the coordinating session's checks of the mutants.
- Line 370–371: it had checked n-build's lock draft (notes :423–426).
- Line 422–423: the manifest checks.
- Line 489–490: §4's windows.
- Line 500–501: Q-F3 ran beside.

## 4. Draft 5's changed regions against draft 4 (13 claims, all CONFIRMED)

`diff` shows 8 regions against draft 4, plus the repository line against the base.
- **Line 65:** `REPO` is computed. It is identical to draft 4's and differs from the base's absolute line.
- **SENT-CODE-FORMS description** (:1909–1912). It reads "47 forms … beside them the lock line's head, which the reader parses", which matches `code_forms` (:3527–3542, which includes `GATE_LINE_HEAD`). Only the description changed, and descriptions are not in the digest.
- **PIN-n-40** (:2800–2802): a second line of its own beginning with the head is refused (two found); a mid-line or blockquoted quotation is not read. This matches `lock_gate` :6268–6269: lines are stripped and must start with the head.
- **VD-CEILING's comment and description** (:5214–5216, :5247): R12 only. `pc2b` is a standing pause (not adjudicated), and R13's ruled read is VD-BATCH-CLEARS' `pr3`.
- **bz** (:5591–5596): `example_pause(…, launch_index=159, resumed_at=160, identity=camp4.identity)`.
  - Its batch is (0, 159), n 160; k is set to 0.
  - c4's reads 0–159 are N1-V's +1 cell: plan_cells order, the omitted cells come later, and the "auto" dose rule re-computes every +1 read.
  - 501 % 160 ≠ 0, so v6's read 500 ends no tile; 479 ended the trial-less +d_20 cell.
- **The battery still holds for bz, by reading:**
  - check_report accepts it: first % 160 = 0, last equals the launch index, span 160, n ≤ span; k 0 ≤ the stage's exceed_tau of 0; n 160 ≤ trials; fires 1; resumption 160 > 159.
  - report_problems: 160 is a launched read; the tile and scope checks are skipped because the pause is adjudicated; the read is in the plan and not on disk, so it gives "is not on disk" and nothing else. VD-REFUSE's `pause-read` case therefore still passes, with 58 cases.
  - bz is used nowhere else.
- **ganl_artifact's spec** (:5932–5935) adds the 2026-11-19 answers §3 and §4 and the second sitting's §2.5, and their paths are committed. First-pass observation 8 is resolved.
- **lock_gate's docstring** (:6264–6267) matches the code.
- **report_problems' docstring** (:6363–6366) matches schema :1477–1487. The first-pass IMPRECISE is resolved.
- **Digests and registers:** no other region changed. CODE_FORMS_SHA256 is unaffected. STR-PINS is unaffected: no PIN-n or OPEN-Q citation was added or removed outside the registers. No check reads the changed texts' content (the spec is checked only for "UTC" and "T00:").

## 5. First-pass FAIL and IMPRECISE items: resolution

- **FAIL (6), all resolved:** #26, #52, #70, #83, R16, R41. R41 is resolved by moving the fixture, verified by reading.
- **IMPRECISE (23):**
  - Resolved (20): #20, the report_problems docstring, #31, VD-CEILING, #37, #38, #50, #54, #57, #68, #69, #73, #78, #80, #88, #94, C6, R7b, R12, R18.
  - #53 is resolved in substance, but its new wording omits the review from the conditions (entry 58).
  - #65 and R15 are only partly resolved: "All taken in draft 4" and "Draft 4 carries them all" remain (entry 69; review lines 41 and 354).
- **First-pass observations:** 1, 2, 4, 5, 7 and 8 are resolved. Observation 3 is resolved for the commands it named. Observation 6 is resolved in the analyzer but not in the review raw's §2 F2.
- **New errors from the revisions:** no FAIL. The new IMPRECISE items are entry 22, entry 58, and the review raw's §5 lines 507–508 and 521–522.

## Counts

| Text | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|
| Entry | 87 | 3 | 0 | 9 |
| Close line | 7 | 0 | 0 | 0 |
| Review raw | 49 | 6 | 0 | 8 |
| Analyzer | 13 | 0 | 0 | 0 |
| **Total (182)** | **156** | **9** | **0** | **17** |

## Observations

1. **Guard-marker text in two of Code's first-sweep commands, not declared.**
   - Sweep :19 is a heredoc that writes a memory-compaction map; it holds memory-file names containing two guard markers.
   - Sweep :144 is a notes write quoting v6's INVOCATION line with the venv folder's name, which holds two markers.
   - The Bash tool passes the command text to the shell as its argument, so on the reading the dated note applies to v6's gate grep, these may be markers in an argv. The second sweep is still a placeholder.
2. **Smaller gaps in the first sweep's departures.**
   - **Other text tools beyond the named `sed -n` prints:**
     - `sed` substitution filters and one `sed` script (e.g. :69, :134, :212, :239, :277–292, :294).
     - `cat -v`, `cat -e` and `cat -A` filters (:25, :54, :211).
     - `chmod 444` of the frozen copy (:235).
   - **Unpruned finds in the touch command (:47):** two more `find`s over scratch, one with `-mtime +0`.
   - **Tools over the shared notes folder:** awk, sed, head and wc over Code's backup there (:25, :210–212). The list names that folder only as written.
   - **awk over digest output:** awk abbreviating shasum output of repository files (:69, :134).
   - **Git print forms:**
     - A second author-date print: `git log --format='%h %ad' -2` on the schema, with item 3's exclusions (:134).
     - :1's `git log -1 --format=%B` printed a commit body, which "names, hashes, counts, subjects or the named files' own text" does not quite cover.
3. **The 2026-11-20 PI routing raw (bc85386) is uncited** (entry 22).
4. **A smoke report also fired before the tile.** The BACKEND extension's smoke of 2026-11-18 also ran the binomial and fired p01 at its end (RESULTS.md :4005–4007). It was never of record, so the interim's conclusion stands; the grounds name only the two runs of record.
5. **bz's resumption moved too** (480 → 160). The entry and the review raw's §5 mention only its read.
6. **Draft vs run copy.** Entry :160's `309a1c43…926a` is draft 3's run copy, not draft 3. The review raw's §5 calls the run copies "drafts" (graded above).
7. **VD-F5-FIXTURES checks A, B and C's batches only.** VD-REFUSE's `p2` takes `example_identity()`'s rule by default. The values are the same, so entry 37 holds in value, not by construction.

## Commands beyond reading files and the brief's git forms

- **Interpreter, against "no interpreter at all":**
  - One `awk` call: a field count over the sweep's first lines.
  - `sed`: `sed -n` line prints and `sed 's/…//'` prefix strips, to extract four quoted entry lines and the review raw's §1 into checker2, and to filter diff output in the mutant check. Stated in case sed counts as an interpreter.
- **`date -j -u -f`** on two sweep timestamps, compared with `git log -1 --format=%ct` of ef105f1 and db00d6d (item 3's pathspec plus mf3). It printed only the order.
- **Other tools:** cut, tr, head, tail, wc -l, fold, column, cmp, test, od -c, cat, printf, diff/diff -u, `shasum -a 256 -c` on the mutant manifest, zsh loops over typed id lists, and name-only ls of SCRATCH folders.
- **One command failed at zsh's `=` expansion** (`echo =====`) after its first part ran.
- **Git:** rev-parse vs hash-object checks; `git log` and `git log --diff-filter=A` with item 3's pathspec plus mf3; `git show <rev>:<path>` with that pathspec appended.
- **Reads beyond the named sources:**
  - `results/raw/2026-11-20_first-sitting_pi-routing.md` (whole) and the 2026-11-18 third-sitting answers raw (grep), both by path, both tracked and clean.
  - The v6 self-test raw (two lines, by grep).
  - RESULTS.md's backend-ext, smoke and backend-ext-2 entries.
  - In SCRATCH: the dated note, commit_steps.sh, the mut/ and review/ files, the run copies and outputs.
- **Printed to my session only, written nowhere:** sweep timestamps, twice (a date and a partial hour); the run outputs' INVOCATION lines and sweep commands holding the home path and the venv folder's name.
- **Writes:** only files under `SCRATCH/vc/checker2/`: quote and section extracts, the sweep's command column without timestamps, and function and diff extracts.
- **Not done:**
  - Nothing under data/ listed, read, stat'ed or searched.
  - results/raw not listed.
  - No guard marker in any argv (bracketed patterns used).
  - No Python, no repository code run.
  - Nothing edited outside checker2.

## Pass 2: Code's dispositions

No FAIL. Every IMPRECISE item and observation is applied in the texts; the analyzer is unchanged after this pass
(its 13 claims all CONFIRMED), so draft 5 is the committed file.

IMPRECISE (9), each applied:
- Entry 22: 2026-11-20's routing item now quotes the PI's block verbatim from its committed raw,
  `results/raw/2026-11-20_first-sitting_pi-routing.md` (`db8d8db4…ddcc`, at `bc85386`, item 5 at :19), cited by
  path; the answers' own §7 item 5 is named beside, as wording it a little differently.
- Entry 58: the conditions restate condition 4 whole ("the battery, review and values-check of record on v7's final
  bytes"), say which ran on them, and that the review read draft 3 in the order the coordinating session accepted, for
  the seat to class.
- Entry 69 (#65) and the review raw's lines 41–42 and 354 (R15): draft 5 named as carrying SENT-CODE-FORMS'
  description, F4's last point.
- The review raw's §2 F2: draft 5's wording (a quotation on a line of its own counts; one inside another line, or
  blockquoted, does not).
- The review raw's §5, lines 507–508 and 521–522: the run copies, not the drafts, gave the absolute repository line.
- The review raw's §6, line 528: C_N2's four changed forms named beside the new ones.

Observations (7):
1. The two commands whose heredoc text held a guard marker are declared in the entry's departures, with the reading
   that, if the harness hands a command to the shell as its argument, the markers were in that argument.
2. The smaller gaps are declared: `sed` substitutions and one script, `cat -v`/`-e`/`-A`, `chmod 444`, the two
   further `find`s, the tools over the shared notes' backup, `awk` over digest output, the second author-date print
   and the commit body.
3. As entry 22.
4. The BACKEND extension's smoke of 2026-11-18, which also fired at its end and was never of record, is named in the
   interim's grounds.
5. `bz`'s resumption (480 → 160) is named beside its read in the entry and the review raw's §5.
6. The frozen copy is named as draft 3's run copy in the entry.
7. The F5 sentence says which fires take their campaign identity's rule and which (VD-REFUSE's read-less `p2`) the
   schema example's, the same values, and that VD-F5-FIXTURES checks A's, B's and C's.

The checkers' departures, as their reports state them, for the seat to class (the entry carries them):
- Pass 1: one `awk` call and one `sed -n 2p`, against its brief's "no interpreter"; `date -j -u -f` on sweep
  timestamps against `git log --format=%ct`, printing the order only; `[ -w ]`; zsh loops over literal id lists;
  head, tail, cut, wc -l, fold, sort, uniq, tr, cat, `diff`; name-only `ls` of scratch folders; writes under its
  checker folder only; reads beyond its named sources (v6's values-check raw by `git show`, the 2026-11-18 third
  sitting's answers by `git show … | grep`, RESULTS.md's BACKEND entries, the two commit-steps scripts); sweep
  timestamps printed to its own session once.
- Pass 2: one `awk` call, and `sed` line prints and prefix strips, against its brief's "no interpreter"; `date -j -u
  -f` against `git log --format=%ct`, the order only; cut, tr, head, tail, wc -l, fold, column, cmp, test, `od -c`,
  cat, printf, `diff`; `shasum -a 256 -c` on the mutant manifest; zsh loops over typed id lists; name-only `ls` of
  scratch folders; one command stopped at zsh's `=` expansion after its first part ran; reads beyond its named
  sources (the 2026-11-20 routing raw, whole; the 2026-11-18 third sitting's answers and the v6 self-test raw, by
  grep; RESULTS.md's BACKEND and smoke entries; scratch files); sweep timestamps and the run outputs' INVOCATION
  lines, which hold the home path and the venv folder's name, printed to its own session only; writes under its
  checker folder only.
