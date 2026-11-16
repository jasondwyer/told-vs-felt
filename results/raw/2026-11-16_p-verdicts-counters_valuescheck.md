# The blind values-check of the counters commit's texts, with Code's dispositions (Code; PI date 2026-11-16)

*The dpo VERDICTS session's values-check of the five texts committed with the counters script: this commit's RESULTS.md entry, the dpo session's close line on `9189623`'s entry, the block `results/raw/2026-11-16_p-verdicts-counters_code-to-design.md`, and the raws `_p-verdicts-counters_review.md` and `_p-verdicts-counters_selftest.txt`. The checker was a fresh subagent with no part in the drafting. It checked the drafts in a scratch directory against the script (`scripts/p_verdicts_counters.py`, sha256 `8e7fbed3…6905`), the seat's answers of 2026-11-16 and the joint block, RESULTS.md at HEAD `db2e821`, the seat's raws of 2026-11-09 and 2026-11-12, the task_correct raw, p's and m's code, LOCK-p-OLMo-dpo §8.1, the dpo decisions input and the p reports. Its brief bound it to the list of record v2, items 1–5 (quoted), the rules of Q-F3's campaign on this laptop (quoted), and the amended brief for p's VERDICTS (no p checkpoint, call log or output opened). Its report is reproduced verbatim below. Code's dispositions follow it. Calendar dates only; the commit hash is the record.*

## The report, verbatim

## Blind values-check: p's counters at VERDICTS (five drafts)

**Result:** 159 claims checked. 121 CONFIRMED, 18 IMPRECISE, 1 FAIL, 19 NOT CHECKABLE. Separately, text 1 still has an unfilled placeholder.
- **The FAIL** is in text 4, in Code's round-1 disposition (NOTE on the read-domain restatement). It says "every read-domain cell has a hit", but the synthetic read domain's sham harness-line and sham refusal cells have none.
- **Every verbatim quotation matches its source character for character, emphasis included.** The only change is the deliberate ellipsis in text 3 L72, which drops "is recorded".

Short names used below:
- **answers:** the seat's answers raw of 2026-11-16
- **joint:** the joint block
- **gtime:** the seat's answers of 2026-11-09
- **qualans:** the seat's answers of 2026-11-12
- **tcraw:** the task_correct raw
- **script:** `scripts/p_verdicts_counters.py`
- **R:** RESULTS.md at HEAD `db2e821`

Verdicts: C = CONFIRMED, I = IMPRECISE, F = FAIL, NC = NOT CHECKABLE.

### Text 1: entry_counters.md (44 claims)

| # | Where | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | L1–3 | Script and self-test committed before any released-record read; §3, §4, §5 step 3; "the counts the record names" | C | answers:29, :33, :39 |
| 2 | L4 | dpo session's entry; the coordinating session gave it the counters step | C | R:116–118, added at 18102d0 |
| 3 | L5–6 | Nothing ran on a model or the box; no ckpt, call log or p output opened; nothing under data/mf3 | NC | Session's own act |
| 4 | L7–8 | Paste-block title, and "Route as given" relayed | C | R:142–143 |
| 5 | L8–9 | Section B items 3–5 quoted verbatim in the instruct close, below | C | R:143–151 (db2e821) |
| 6 | L10 | Raw sha 01ae2ae7…1b0f, committed at 18102d0 | C | shasum; `git show --name-status 18102d0` |
| 7 | L10–13 | §3 quote | C | answers:29, exact |
| 8 | L14–15 | Division-of-work quote | C | R:117–118, exact |
| 9 | L16–17 | Coordinating session's "Yes, both go to the seat…" | NC | Chat relay |
| 10 | L18 | Script sha 8e7fbed3…6905 | C | shasum |
| 11 | L18–19 | Outside p's package, so no lock-pinned hash moves | C | Lock §4 and §8.1 pin files and package globs only. Package hashes recomputed in shell at HEAD: a38d93bb…, 7756dcf4…; valence_core/{p,m} clean |
| 12 | L20–24 | "What it imports" (report.py, renders, task_correct) | I | Incomplete. The script also imports m's `resume.read_checkpoint`, `readrule.release_full`, `corr.load_pool` and the package hashes (script:99–104); text 3 §1 lists the reader and release. **Fix:** add them |
| 13 | L23–24 | Raw 57e9c7dc…56e2; embedded script 9aa0e2d9…4e0f; both checked | C | shasum; tcraw header at :28, once; lines 29–EOF hash to 9aa0e2d9…; script:177–194 |
| 14 | L25–26 | Adds no definition; every recorded round by arm and phase; key table on R1's rounds | C | script:258–286, :325–338, :117 |
| 15 | L27 | Before the gates `run` reads only the raw, the pools file and the lexicon | C | script:470–473; corr.py:176; report.py:171 |
| 16 | L27–28 | "It reads no checkpoint and no p report until they pass" | I | Gate 5's self-test reads the six time and qual p reports and the reads files (script:645, :662; docstring :59). **Fix:** "no checkpoint until they pass; no p report but the six time and qual p reports the gate-5 self-test reads" |
| 17 | L29–33 | The five gates | C | script:474–498 |
| 18 | L31 | a38d93bb…, 7756dcf4… are the lock's values | C | LOCK-p-OLMo-{sft,dpo,instruct}.md:91–92; recomputed |
| 19 | L35 | Nine checkpoints read by exact path, all checked before any count prints | C | script:120, :347–349, :362–404, :508–509 |
| 20 | L36–37 | Read domain recomputed two ways, each asserted equal to the committed report | C | script:387–394 |
| 21 | L38 | Any difference STOPs; after the gates any pass-1 failure is a STOP (exit 4) | C | script:407–415, :883–885 |
| 22 | L40–41 | nice -n 19; three windows granted | NC | Session act |
| 23 | L42–43 | Runs 1 and 2: 23/23 and 35/35 | C | Raw sections are identical to the scratch-directory captures (blank lines aside) |
| 24 | L42–43 | Run 1 sha f4ec08c3…9339, run 2 sha a2687010…5b29 | NC | Bytes not kept. Consistent across texts 1, 3, 4, 5 |
| 25 | L44 | Run 3: 37/37, exit 0, stderr empty | C | Scratch stderr3 empty. 37/37 gives return 0 (script:611–613, :875). The run-3 lines are the current source's 37 checks, in order |
| 26 | L45–47 | 63/64+96/96 (×2), 64/64+96/96 = 159/160, 159/160, 160/160, via tally_file and the step's own count; G-TIME 3/4+6/6, 4/4+6/6, 4/4+6/6 | C | tcraw:11–13, :20–22; script:648–660 |
| 27 | L48–49 | session_counters over the sham records equals the committed qual and time sham cells; no withheld cell computed | C | script:661–669; report.py:260–301 computes the read domain only |
| 28 | L52–53 | Round 1: 0 MAJOR / 7 MINOR / 6 NOTE. Round 2: 0 / 2 / 9 | C | Text 4 structure |
| 29 | L53–55 | "Its MINORs: after the gates any failure … is a STOP … is contained" | I | States the fixes as if they were the findings. **Fix:** "Its MINORs, both applied: after the gates a failure was reported as a refusal (now a STOP); an exception in the gate-5 self-test escaped (now contained)" |
| 30 | L58–60 | R1 | C | script:117, :145–148 |
| 31 | L61–62 | R2 | C | script:149–150 |
| 32 | L63–64 | The three runs go ahead "as the coordinating session has it" | NC | Relay |
| 33 | L65 | Close line in this commit; paste block item 6 | C | answers:62; R:151 |
| 34 | L66–68 | Two `python3 -c` runs without a window, printing m's first decision items | NC | Act not checkable. Both files exist (git ls-files data/m/verdicts) |
| 35 | L67 | "one per checkpoint" | I | Ambiguous next to L5's file sense of "checkpoint". **Fix:** "one per unit (sft, instruct)" |
| 36 | L69–70 | MODEL_PROCESS_MARKERS, matched case-insensitively, would have counted them at a Q-F3 launch or resume | C | m/guard.py:95, :917–919 ("olmo"; exe contains "python"); mf3_sessions.py:784/909, stage_precheck incl. resume |
| 37 | L71 | No Python since outside a window | NC | Session act |
| 38 | L72–73 | Coordinating session's "Noted, and harmless…" | NC | Chat |
| 39 | L75 | Self-test read the files its raw names | C | script:50–53 and code paths |
| 40 | L76–81 | Code's reads (dpo p reports, m's dpo campaign report, three inputs, checkpoint digests, name listings) | NC | Session acts. Files exist. The scratch precheck does digest the three dpo checkpoints by shasum and hash-object/rev-parse (RESULT: PASS) |
| 41 | L84 | Runs "once the PI has answered on the push (item 8)" | NC | Sequencing is not in the record. See consistency item 4 |
| 42 | L85–87 | `scripts/p_verdicts_counters.py run --exit …` "in a window" | I | The script is not executable and the line omits nice. **Fix:** `nice -n 19 $PY -B scripts/p_verdicts_counters.py run --exit OLMo-sft=0 --exit OLMo-dpo=0 --exit OLMo-instruct=0` (docstring :77–79) |
| 43 | L88 | Each entry open at "the reads" | C | answers:41 |
| 44 | L89 | Not pushed; committed by path | NC | Future act |

### Text 2: close_9189623.md (14 claims)

| # | Where | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | L1–2 | The raw names the three VERDICTS sessions for close lines | C | answers:3, :62 |
| 2 | L3–4 | Link and sha 01ae…1b0f | C | shasum |
| 3 | L4–5 | Committed by path at 18102d0 on "Route as given" | C | R:111–113; git show |
| 4 | L5–6 | "It is committed with the counters script, the paste block's item 6." | I | The apposition reads as if the script were item 6. **Fix:** "…with the counters script, on the paste block's item 6" (the instruct close's form) |
| 5 | L8 | Q1 (c); dpo's reading had been (a) | C | answers:7; R:71–72 |
| 6 | L9–10 | Six items; committed by instruct at db2e821; path; sha f8eac889…b5e2 | C | shasum; `git show --name-status db2e821`; jq length 6 |
| 7 | L11 | Confirmed by reading only | NC | Corroborated by R:179 |
| 8 | L11–12 | The file holds m's validator rules | C | jq against m_analyze.py:157–163, :666–718: keys, schema m-decisions-v1, unit, ISO dates (11-06, -07, -14, -14, -15, -15), Q-F0 / PASS. Full validator not run (no Python) |
| 9 | L12 | The block's items in the block's words | C | All six decision texts found whole in the joint block |
| 10 | L13–14 | Q2 (a), (i) and (ii); end notice carries the exit status alone | C | As ruled: answers:8, :23, :38. Compliance itself not checkable |
| 11 | L15 | Q3 (a) and Q4 (b) by the division at 18102d0 | C | R:117–118 |
| 12 | L16–17 | Committed before the script reads any released record | C | data/p/verdicts holds only the three inputs, so gate 2 is closed |
| 13 | L18–19 | R1 and R2 go in the same commit's block; the entry above gives them | C | Internal |
| 14 | L20–21 | Ledger (75) fix, verbatim | C | answers:50, exact |

### Text 3: blk_counters.md (57 claims)

| # | Where | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | L1 | Title | C | — |
| 2 | L3 | dpo session; counters step given by the coordinating session | C | R:117–118 |
| 3 | L3 | Answers path, sha, 18102d0, §3 and §4 | C | — |
| 4 | L3 | "Route as given", section B items 3–5 | C | R:142–151 |
| 5 | L3 | "before the counters step reads anything" | NC | Relay |
| 6 | L3 | Full script sha | C | shasum |
| 7 | L3 | "What this commit carries" | I (minor) | Omits this block, RESULTS.md (entry and close) and the values-check raw. **Fix:** add them |
| 8 | L3 | report.py e807c5ad…5af1 | C | shasum |
| 9 | L3 | gtime line 34 and its routing item 3 | C | gtime:34, :63 |
| 10 | L3 | "Read for it" / "Not opened" | NC | Session acts |
| 11 | L7 | 37/37; the G-F0m and G-TIME rows (9/10, 10/10, 10/10) | C | tcraw:11–13, :20–22 |
| 12 | L8–10 | R1 / R2 summaries; Q4 (b) quote | C | answers:33 |
| 13 | L11 | "the inputs' commit … go ahead" | I | Already made (db2e821); text 1 omits it. **Fix:** drop it, or "(made, db2e821)" |
| 14 | L16 | Predicates; stage.py:966 with `corr.load_pool()` | C | report.py:119–139, :155, :171, :203; stage.py:966 |
| 15 | L17 | RENDERS_OF_RECORD | C | corrupt.py:32, :50 |
| 16 | L18 | Loaded from raw bytes; both shas; checked before exec; never copied | C | script:177–194; tail shasum |
| 17 | L19 | read_checkpoint; release_full (m:271) | C | resume.py:682; readrule.py:799–805 |
| 18 | L20 | Package values named by every LOCK-p v1.0 | C | Three locks :91–92 |
| 19 | L21 | p §2.3 "tabulated over every generation of every p stage" | C | PROPOSAL-p v0_2:68 |
| 20 | L23 | Before the gates: raw, pools, lexicon | C | script:470–473 |
| 21 | L24 | "No checkpoint and no p report until five gates pass" | I | Same issue as text 1 #16 |
| 22 | L25–29 | Gates 1–5; §5 item 2; an exception closes gate 5 | C | answers:38; script:474–498, :607–610 |
| 23 | L30 | Nine paths, never a listing, plus each p report | C | script:120–121, :347–349, :380 |
| 24 | L31–37 | Pass-1 checks | C | script:366–402 |
| 25 | L39 | STOP (exit 4) is the only line it adds; pass 2 prints | C | script:407–415, :508–509 |
| 26 | L40 | "What it prints" | I | Also prints task_correct.py's key table, match rule and READING, plus gate lines and session/round counts (script:485–507, :437). **Fix:** add them; "the readings R1 and R2" is too narrow |
| 27 | L44 | nice; windows; no other Python | NC | Session act |
| 28 | L44 | "The raw carries each run's stdout" | C | Identical to the scratch-directory captures |
| 29 | L45–47 | Run counts; run 3 on 8e7fbed3 | C | As text 1 #23 and #25 |
| 30 | L50–52 | Import checks; 19 rule cases | C | Raw stdout L12–18 |
| 31 | L54–56 | Six reads files at the printed digests; figures; session_counters | C | shasum of the six equals READS_SHA256 and tcraw |
| 32 | L57–60 | Synthetic: hit per named cell; equality; five malformed rounds | C | script:559–578, :678–714 |
| 33 | L62 | Gates 1 and 2; nine paths | C | script:717–741 |
| 34 | L63 | Two passes "printed in full" | I (minor) | Output goes to a captured buffer, checked for 9 headers, 9 withheld lines, 6 task_correct lines (script:748–756); nothing in the raw. **Fix:** say so |
| 35 | L64 | Six silent STOP cases | C | script:758–776, :795–845 |
| 36 | L65 | Refusing reader and missing file each STOP | C | script:778–793 |
| 37 | L66 | "The script's source makes no directory-listing call" | I | Over-reach. The source calls `shutil.rmtree` (script:798) and uses TemporaryDirectory (script:728), both of which list the scratch directory; the check matches six patterns only (script:153–154, :846–849). **Fix:** "makes none of the six listing calls the check names; it lists only its scratch directory and, via the package hashes, the package directories; nothing under data/p/ckpt" |
| 38 | L72 | Line-34 quote | C | Exact, including emphasis |
| 39 | L72 | "G-TIME's observation … now as the first row" | C | Ellipsis elides "is recorded" |
| 40 | L72 | Routing item 3 | C | gtime:63, exact |
| 41 | L73 | G-TIME row by the seat's read | C | gtime:34; R:4647 |
| 42 | L73 | G-F0m row by Code at a225a89, confirmed 2026-11-12 Q2 | C | R:2811; qualans:7, :21 |
| 43 | L73 | 41bfab4 reports no task_correct | C | grep count 0 in entry and diff |
| 44 | L74 | Order of stages; scope; "first row" | C | Dated 11-09, 11-11, 11-15 |
| 45 | L76 | One contrast session at G-TIME, eight at G-F0m, per unit | C | R:4567, :2769; answers:46 |
| 46 | L79 | TC_STAGES | C | script:117 |
| 47 | L81 | 32 sham / 80 contrast | C | R:447 |
| 48 | L84 | No committed campaign sham figure | C | script:137–144 |
| 49 | L85 | Campaign checkpoints read under every option | C | script:116 |
| 50 | L89 | CONTRAST_WITHHELD_QUAL quote, :214–216, in G-F0m's and the campaign's reports | C | Exact; jq equality true on the six qual and campaign p reports |
| 51 | L89 | CONTRAST_WITHHELD, :211–212 | C | Equal on the three time reports |
| 52 | L89 | Joint block raised it under Q3; §3 and §4 names | C | joint:321–323 |
| 53 | L90 | attribute_calls at :881; call-log paths | C | stage.py:881, :674, :3033 |
| 54 | L91–93 | R2 (a)/(b) quotes; nine call logs | C | — |
| 55 | L104 | "every read by exact path" | I | Package hashes glob their directories (resume.py:342; guard.py:72). **Fix:** "every record read by exact path" |
| 56 | L104 | Gated on the third run's end plus four gates; reviews; no MAJOR | C | — |
| 57 | L105 | STOP line names "the stage and the cells that differ" | I | Only the step-table STOP names cells (script:393–394). The session_counters STOP names the stage and report (script:389); the task_correct STOP names the stage only (script:401). **Fix:** qualify |

### Text 4: review_raw.md (33 claims)

| # | Where | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | L3 | Round shas and self-test counts | C | Counts verified; shas consistent (see text 1 #24) |
| 2 | L3 | Fresh subagents; brief contents; bindings; verbatim reproduction; the one rewording | NC | — |
| 3 | L3 | The two reviewers' own accounts | C | Each occurs verbatim in its report (2× each) |
| 4 | L7–80 | Round-1 structure | C | — |
| 5 | Round-1 report | Reviewer's checkable cross-file references (12 spot-checked) and hash claims | C | resume.py:558, :674, :607–610; stage.py:673, :985, :996; m stages.py:224; scaffold.py:605–606; readrule.py:460, :481; report.py:277–300; lines 29–EOF = 9aa0e2d9. References into the f4ec08c3 bytes are not checkable |
| 6 | L84 | "The revised script's self-test is its own raw." | I | Run 2 shares the one self-test raw. **Fix:** "…(run 2) is in the self-test raw" |
| 7 | L88 | MINOR 1 disposition | C | script:795–845 |
| 8 | L89 | MINOR 2 disposition | C | CounterError, LexiconStop and CorrStop all subclass SystemExit (tcraw script :54; report.py:112; corr.py:91); script:880–891 |
| 9 | L90 | MINOR 3 disposition | C | Lock §8.1/§8.2. Report packages: time 7a08dbfa… = lock v0.1 (:277); qual 08bfa693… = v0.2 (:188); campaign a38d93bb… = v1.0. script:385, :436 |
| 10 | L91 | MINOR 4 disposition (three reads) | C | Historical; superseded by round-2 NOTE 4 |
| 11 | L92 | MINOR 5 disposition | C | — |
| 12 | L93 | MINOR 6 disposition | C | script:686 |
| 13 | L94 | MINOR 7: "good case printed in full" | I (minor) | Same as text 3 #34 |
| 14 | L95 | NOTE: corrupted render | C | script:252–253, :575, :704 |
| 15 | L96 | "…on the synthetic records, where every read-domain cell has a hit" | **F** | In this raw's own usage a "read-domain cell" is a counter (bad_cell alters `counters.sham.refusals`). The synthetic read domain's sham harness_first_line and sham refusals cells have no hit; those hits fall in the contrast forced cell (script:678–685; read_domain_view :289–303; report.py:283–297). The claim holds only per arm and phase. **Fix:** "where each read-domain arm and phase has a hit (the sham harness-line and refusal counters have none)" |
| 16 | L97 | NOTE: redaction | C | jq over the six reports: only sft qual has a nonzero sham counter (cap_hits); sham cc texts empty everywhere |
| 17 | L98 | NOTE: digests pinned and checked before use | C | script:125–132, :646–648 |
| 18 | L99 | NOTE: "recorded rounds" wording | C | script:28, :33, :437 |
| 19 | L104–158 | Round-2 structure | C | — |
| 20 | Round-2 report | Reviewer's history claims | C | git log: report.py and proxy.py last at d215d5b; corrupt.py at a665a09; e8779b1 / 40086e8 / c0f1c69 touched identity.py, register.py, stage.py only; m last at 993eba1 |
| 21 | Round-2 report | Reviewer's other references | C | m stages.py:2269, :2308; readrule.py:799–805; resume.py:670–684; stage.py:924–925, :959–963; corr.py:395–405 |
| 22 | L166 | MINOR 1 disposition | C | — |
| 23 | L167 | MINOR 2 disposition | C | — |
| 24 | L168 | NOTE 1 | C | — |
| 25 | L169 | NOTE 2 | C | — |
| 26 | L170 | NOTE 3 | C | — |
| 27 | L171 | NOTE 4 | C | No mutating call in `_check_state`'s range |
| 28 | L172 | NOTE 5 | C | See consistency item 9 |
| 29 | L173 | NOTE 6 | C | R:4565–4567, :2766–2770, :445–448; no `--resume` in any run |
| 30 | L174 | NOTE 7: "source makes no listing call" | I | Same as text 3 #37 |
| 31 | L175 | NOTE 8: "No line the run prints names a temporary directory" | I | True on a passing run only. A self-test FAIL's exception text is scrubbed of repository paths only (script:169–173, :610). **Fix:** "no line a passing run prints…" |
| 32 | L176 | NOTE 9 | C | script:39–45, :145–148 |
| 33 | L162 | Committed script = round 2's fixes; self-test of record in the self-test raw | C | — |

### Text 5: selftest_raw.txt (11 claims)

| # | Where | Claim | Verdict | Evidence |
|---|---|---|---|---|
| 1 | L1 | §3 quote | C | Exact |
| 2 | L2 | Command form; the `$PY` interpreter exists | C | Matches the docstring usage |
| 3 | L2 | nice, windows, no other Python | NC | — |
| 4 | L3 | Run 3: full sha, 37/37, exit 0, stderr empty | C | — |
| 5 | L4–5 | Runs 1–2: 35/35 and 23/23, stderr empty | C | Scratch stderr1 and stderr2 empty |
| 6 | L4–5 | Runs 1–2 "exit 0" | NC | Exit status not captured |
| 7 | L4–5 | "Review round N read these bytes" | NC | — |
| 8 | L6 | Reviews path | C | — |
| 9 | L7 | Reads list; contrast record "nothing but its flag"; no checkpoint, call log or p output; model-free; no clock time | C | script:50–53, :526–530; tcraw tally_file |
| 10 | L8 | No local path | C | grep finds none in any of the five drafts |
| 11 | L10–118 | The three stdout sections | C | Identical to the scratch-directory captures |

### Consistency and over-reach

1. **Placeholder.** Text 1 L82 still reads "@@VC@@" and must be filled before commit.
2. **Section B items.** Texts 1 and 3 say "items 3–5". The script's docstring (script:6), which is committed with them, says "items 3 and 4". Align one or the other.
3. **What the hold leaves free.** Text 1 L63–64 says only the three runs go ahead; text 3 L11 adds "the inputs' commit", which is already made.
4. **Timing of the runs.** Text 1 L84 has the runs wait for the PI's answer on the push. The record calls the push "not a condition of the runs" (answers:66; R:127–128), and text 3 L11 has the runs "go ahead". Cite the coordinating session's word, or add "(the push itself is not a condition)".
5. **Import lists.** Text 1's list is shorter than text 3 §1's.
6. **Checkpoints "opened" versus digested.**
   - Text 1 L5–6 says no checkpoint was opened; L79–80 says Code digested dpo's three. These are consistent under list item 1, but "opened for content" would remove the apparent tension.
   - The scratch precheck's section 1 also ran a scoped `git status --porcelain` naming the three dpo checkpoint paths. That is item 1's form, but it is missing from the entry's reads list.
7. **Repeated over-reach across texts.**
   - "No directory-listing call": text 3 L66, text 4 L174, and the check's own wording (stdout L49; script:847–848).
   - "Printed in full": text 3 L63 and text 4 L94.
   - "No p report until the gates pass": text 1 L27–28 and text 3 L24.
8. **Other over-reaches flagged above:**
   - "every read-domain cell" (the FAIL)
   - "every read by exact path"
   - "the cells that differ"
   - "no line … names a temporary directory"
   - the "What it prints" and "What this commit carries" lists
9. **Minor, not counted.**
   - task_correct.py's own self-test line is printed without flush (tcraw embedded script :169). The next check's flush carries it, so it is harmless to NOTE 5.
   - Text 5's Reads line omits the package sources the package check hashes. They are code, not data.
10. **Equal across all texts:** 8e7fbed3…6905, f4ec08c3…9339, a2687010…5b29, 01ae2ae7…1b0f, 57e9c7dc…56e2, 9aa0e2d9…4e0f, a38d93bb…, 7756dcf4…, f8eac889…b5e2, 37/35/23, 159/159/160, 9/10/10, the 7/6 and 2/9 review counts, and 32/80 and 1/8 sessions.

### My conduct
- **Python and searches:** no Python. No whole-tree git status (two scoped `--porcelain` runs). No pickaxe. Greps only over named files.
- **data/p/reports:** `jq` over the nine p reports, printing only booleans, counter names and 8-hex package prefixes. shasum of the six reads files. A name-only `git ls-files`.
- **data/p/verdicts:** name-only listing. shasum of the three inputs. `jq` over the dpo input (an input file).
- **data/m/verdicts:** name-only listing.
- **Not touched:** nothing under data/p/ckpt or data/mf3 was opened, digested or listed. My `git show --name-status` runs did list names, which item 1 permits.
- **Other reads:** `wc -c` over valence_core/{p,m}/*.py to recompute the package hashes. `test -s` / `test -x` on scratch and script files. Parts of the scratch precheck script, and its output's section headings and OK/FAIL counts (no digests printed).
- **One stray file, deleted:** a redirect wrote a copy of the self-test raw's run-3 section into the session's temp directory, one level above the scratch directory and outside the repository. I deleted it at once.

### Totals
159 claims: 121 CONFIRMED, 18 IMPRECISE, 1 FAIL, 19 NOT CHECKABLE. Plus one unfilled placeholder, not counted.

| Text | C | I | F | NC |
|---|---|---|---|---|
| 1 | 28 | 5 | 0 | 11 |
| 2 | 12 | 1 | 0 | 1 |
| 3 | 46 | 8 | 0 | 3 |
| 4 | 27 | 4 | 1 | 1 |
| 5 | 8 | 0 | 0 | 3 |

## Code's dispositions

The FAIL and each IMPRECISE are applied in the checker's terms. Each consistency finding is applied or answered. The edits were checked by tool, not by a second blind pass.

| Finding | Disposition |
|---|---|
| FAIL, text 4 #15 ("every read-domain cell has a hit") | Applied: "where each read-domain arm and phase has a hit (the sham harness-line and refusal counters have none)". |
| Text 1 #12, the import list | Applied: m's reader, the act of release, the pool and the package hashes are added. |
| Text 1 #16 and text 3 #21, "no p report until the gates pass" | Applied: "no checkpoint until they pass, and no p report but the six time and qual p reports its gate-5 self-test reads". |
| Text 1 #29, round 2's MINORs stated as fixes | Applied in the checker's words. |
| Text 1 #35, "one per checkpoint" | Applied: "one per unit (sft, instruct)". |
| Text 1 #42, the run's command | Applied: `nice -n 19 $PY -B scripts/p_verdicts_counters.py run …`. |
| Text 2 #4, the apposition | Applied: "on the paste block's item 6". |
| Text 3 #7, what the commit carries | Applied: the block, RESULTS.md (the entry and the close line) and this raw are named. |
| Text 3 #13 and consistency 3, "the inputs' commit … go ahead" | Applied: dropped, with "(the inputs were committed at `db2e821`)". |
| Text 3 #26, what it prints | Applied: the gate lines, the self-test's lines, task_correct.py's key table, match rule and reading, and the recorded session and round counts are named. |
| Text 3 #34 and text 4 #13, "printed in full" | Applied: the printing is captured in a buffer and checked; none of it is in the raw. |
| Text 3 #37, text 4 #30 and consistency 7, "no directory-listing call" | Applied in the texts: the source makes none of the six listing calls the check names; the script lists only its scratch directory, and the package hashes list the package directories; nothing under `data/p/ckpt` is listed. The self-test check's own name, in the committed script and its stdout, is unchanged: changing it moves the script's sha256 and owes another self-test run. |
| Text 3 #55, "every read by exact path" | Applied: "every record read by exact path". |
| Text 3 #57, the STOP line's naming | Applied: the line names the stage, and the report where the report is compared; the step-table STOP also names the cells that differ. |
| Text 4 #6, "its own raw" | Applied: "(run 2) is in the self-test raw". |
| Text 4 #31, "no line the run prints" | Applied: "no line a passing run prints". |
| Consistency 1, the placeholder | Filled with this check's figures. |
| Consistency 2, section B "items 3–5" against the docstring's "items 3 and 4" | Answered in the entry: items 3 and 4 rule the step, as the script's docstring cites them; item 5 orders its commit. The script is unchanged. |
| Consistency 4, the runs' timing | Applied: the entry says the coordinating session holds the runs for the PI's answer on item 8, a push first or not, and that the push itself is not a condition of the runs (the seat's §8 item 8). |
| Consistency 5, the import lists | Applied with text 1 #12. |
| Consistency 6, checkpoints opened against digested | Applied: "opened for content", and the precheck's scoped `git status --porcelain` naming the three dpo checkpoint paths is added to the entry's reads. |
| Text 5 #6, runs 1 and 2's exit status (NOT CHECKABLE) | Answered: Code's tool call for each run printed `EXIT=0`; the scratch captures kept stdout and stderr only. |
| Consistency 9, minor | Noted: task_correct.py's own self-test line is printed without a flush and carried by the next flush; the package sources the package check hashes are code, not data. |
| The checker's conduct | Recorded for the seat. It ran no Python, opened nothing under `data/p/ckpt` or `data/mf3`, and listed under `data/p/verdicts` by name only. It ran `wc -c` over the package sources (code, not data) to recompute the package hashes. A redirect it made wrote a copy of the self-test raw's run-3 section into the session's temporary directory, outside the repository, and it deleted the copy at once. |
