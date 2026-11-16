# PROPOSAL-p's three campaigns: the entry, the commit message and the raws: blind values-check

*Code's raw, PI date 2026-11-15. A blind values-check by a fresh checker given the texts, the sources (the box's outputs as copied back, the shipped scripts, the dry test, the relays as received, the six report files by exact path, the repository) and the list of record v2's items 1–5 verbatim, and no conclusion of Code's; model-free. It checked the entry, the message and four raws as first drafted.*

*Totals: 66 claims; 57 CONFIRMED, 3 IMPRECISE (rows 20, 26, 36), 0 FAIL, 6 NOT CHECKABLE (rows 12, 21, 23, 38, 39, 52: the box's remote configuration, the end-waits and the not-read claims as first drafted, Code's conduct, this commit's own acts, and the order of the box steps).*

*How the findings were applied, each in the checker's terms:*
- *Row 20: the dry test is stated as 15 scenarios (16 checks: the three sequential one-checkpoint invocations were also checked for exactly one stamp).*
- *Row 26: the entry says the corrupted-spelling counter covers the sham sessions' forced rounds and that its count over the sham free rounds is withheld to VERDICTS.*
- *Row 36: the entry pins the provenance (ledger 27): the library versions, CUDA, capability, dtype, the determinism flags, the seed, the choice window and the layer count, equal ×3 and to `7ab4d2f`'s; rule 27 is worded "committed here".*
- *Observation 1: "one pod session" is stated, with its evidence: `get-pod`'s `startedAt` unchanged since the create (no stop or restart), and one invocation each with no `--resume`.*
- *Observation 2: the domain is given pooled, as m:318 has it, not split into valid sessions and sessions excluded at a free round. Observation 7: each sham arm's 32 of 32 valid sessions are reported.*
- *Observation 3: "unchanged at the box's HEAD". Observation 4: the word "[go, after its commit]" is named as given. Observation 5: the chain rule is "declared in the wrapper's own header (shipped before the first launch)".*
- *Observation 6: each campaign raw now carries Code's launch calls and their outputs, the end-wait's line, `wait_campaign.sh`, the whole-file sha256 of `stamps.txt` and `d_lines.txt`, and the empty wrapper log's sha256; a fifth raw carries the copy-back's output, the box's sha256 listing of the wrapper outputs and `copyback_campaign.sh` (its one local repository root shown as `<repo>`). The dpo launch's first call refused itself (exit 8: its guard's process search matched the ssh shell's own command line); nothing was launched; the raw records the three calls.*
- *Observation 9: the sync's exit 0 is stated. Row 12: "with no network remote" is reworded as "fetched from the bundle file alone". Rows 21 and 23: the end-wait lines and scripts are embedded, and "not opened" reads "not read". Observations 8, 10 and 11 change nothing.*
- *The additions after the check (the copy-back raw, the launch and end-wait sections, and the one-pod-session, domain, sham-validity, counter and provenance bullets) were checked by tool, not by a second blind pass, so that no Python held Q-F3's launch: every embed against the box's sha256 listing and the shipped scripts, the entry's figures against the six report files, the quotations against their sources, and the content rules.*

*In the report, "/Users/" and "/private/" name patterns the checker searched for, not paths. The report follows verbatim.*

## The report, verbatim

**Blind values-check: p's three campaigns (SCR/camp/: the entry, the commit message and four raws)**

**Result: 66 claims. 57 CONFIRMED, 3 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE.**

Every figure matches the reports, the stdouts and my own digests. Every quotation is exact, and every embedded file is byte-identical. The 3 IMPRECISE items are wording and scope (rows 20, 26, 36). Seven texts are cited by abbreviation (glosses after the observations).

| # | Claim (where) | Verdict | Evidence |
|---|---|---|---|
| 1 | Citations: p v0.2 §4.1 and §6.3; m:192 and m:330 (E headline, M line 1, raws line 1) | CONFIRMED | §4.1 is "The units… by reference". §6.3 says "m:330 by reference: looks every 40 launches and at the end". m:192 is the launch rule. m:330 reads "Cadence every 40 launches and at the end". |
| 2 | Each campaign ran under its LOCK-p-OLMo-{ckpt} v1.0 (038bf3e), on the box of record (7ab4d2f) | CONFIRMED | Each lock's sha256 is the same at 038bf3e, at 7ab4d2f, at HEAD and in the working tree: fafb786d…2bc4, 25c52f56…3dcf, f71c97c1…0e67. Each report's identity.lock_sha256 is equal. 038bf3e's dated note names this box. |
| 3 | COMPLETE ×3, exit 0, path uncached | CONFIRMED | m reports: status and terminal COMPLETE, identity.path uncached. Stdouts: `STAGE … COMPLETE path=uncached` ×3. stamps.txt: exit=0 ×3. |
| 4 | 112 launches each: A0 80, A0s 32, each arm's domain at its floor | CONFIRMED | arms launched/domain 80/80 and 32/32; floors 80/32; terminal.at_launches 112; 80 + 32 session lines in each stdout. |
| 5 | No look fired; no pause; no STOP; (d) equal ×3 | CONFIRMED | Both looks and end_look have fired false, and so does every result. pauses is [] and stop is null. No PAUSE or STOP line in any stdout. d_lines.txt reads "equal" ×3. |
| 6 | VERDICTS follow after ADDENDUM-p1's commit; Next is section B item 6 (E, M) | CONFIRMED | Matches relay item 6, "…before any p VERDICTS session [adopt]. Then … VERDICTS and — secondary DVs, fresh sessions [go, after its commit]". Placeholders not checked. |
| 7 | The seat's §2 item 3, block-quoted; file sha256 fd74d3f6…e3ff | CONFIRMED | Byte-equal to line 31 of the seat file; the file's sha256 is fd74d3f6e60d…a7e3ff. |
| 8 | The PI's go, "Go for the pod whenever you need it.", relayed, PI date 2026-11-15 (E; raws and M quote it without the final period) | CONFIRMED | relay_go line 2, and "whose header gives PI date 2026-11-15". Fidelity of the relay to the chat is NOT CHECKABLE. |
| 9 | Routing of 2026-11-15 (evening), "Route as given", section B item 5, quoted | CONFIRMED | Identical to relay_routing lines 19–21 once line wraps are normalized, "x3" and "[keep]" included. |
| 10 | The box: pod m43y3deb1gq3rp (jspace-olmo-m), 1 × A100-SXM4-80GB, US-CA-2, backend identifier 641ee466f4553b6a | CONFIRMED | 7ab4d2f's entry (RESULTS.md lines 119–137 and 173). The PROVENANCE gpu field reads NVIDIA A100-SXM4-80GB. |
| 11 | Bundle eb3e08c..7ab4d2f, sha256 73c532d1…07a1, identical at both ends; box repo at 7ab4d2fbeb9e… | CONFIRMED | `git bundle list-heads` gives 7ab4d2f… refs/heads/main; `verify` says it requires eb3e08c…. The laptop sha, box sha and my digest are equal. The SYNC OK line and all three stamps blocks show HEAD 7ab4d2f…. 7ab4d2f's entry puts the box at eb3e08c. |
| 12 | "with no network remote" | NOT CHECKABLE | The sync script fetches only from the bundle path. No source records the box's remote configuration. |
| 13 | 15 untracked outputs set aside first, each identical by digest to its blob at 7ab4d2f, in /workspace/qual_p/box-untracked-2026-11-15 | CONFIRMED | sync_out line 1 "SYNC OK…", which the script prints only after its hash-object vs rev-parse checks against 7ab4d2f and the moves. Its file list is 3 × 5 = 15. |
| 14 | Precheck ×3 at campaign ALL CLEAR, exit 0: stage precheck and weights-files check clear; lock_sha256 fafb786d…/25c52f56…/f71c97c1…; G-PWR (p) record bc2b0909…; (j)'s closure equal | CONFIRMED | precheck_campaign.txt lines, and .exit reads exit=0. bc2b0909… equals the G-PWR (p) record in 3e1b614's entry and in each lock's §1. |
| 15 | (a) per unit: 641ee466… read from the three identifier lines of the determinism raw (committed at 7ab4d2f, unchanged at HEAD), beside the lock's 641ee466…: equal; each line names 7ab4d2f and the raw's path, as the seat's §1 (a) has it | CONFIRMED | The raw's lines 76–78 all read 641ee466f4553b6a. Blob b644c1a1 is the same at 7ab4d2f, at HEAD 97d160a and in the working tree; 7ab4d2f is the only commit touching it. The three (a) lines name "commit 7ab4d2fbeb9e" and the path and end in "equal", as §1 (a) asks: "the entry's hash and the respawn raw's path; and the word 'equal'". |
| 16 | `p_sessions.py campaign --unit OLMo-{ckpt}`, one invocation each with no --resume; DRIVER 9c641e19…a96d at 7ab4d2f; wrapper sha256 e10553e2…24db | CONFIRMED | INVOCATION and DRIVER lines; "runs: 1 first returned"; call_log n_runs 1, resume false. The driver's sha256 is 9c641e19…a96d at both 7ab4d2f and HEAD; the wrapper's sha is equal at both ends. |
| 17 | One wrapper invocation per checkpoint, sft, dpo, instruct in turn | CONFIRMED | stamps.txt has three launch/ran/ended blocks in that order. The announcements are row 21. |
| 18 | One launch stamp (sft's); exit codes 0, 0, 0; later launch lines unstamped; no end, done or later stamp; the entry gives no end time or stage total | CONFIRMED | stamps.txt, against the seat's G-ID-F3 answers (c51ef5ba…), §6 "Forward" and §9 item 8. The entry contains no time at all. |
| 19 | Chain rule declared before the first launch; no halt line printed | CONFIRMED | The rule is the header of the wrapper that ran (sha-identical at both ends). Raw line 5 equals wrapper lines 12–14 minus "(no session launched)". stamps.txt has no halt line. The dry-test outputs' own launch lines are earlier than the batch's launch stamp (order only, nothing computed). |
| 20 | "dry-tested on 16 cases" (E, raws line 5) | IMPRECISE | wraptest/out holds 15 scenarios, S1–S15, which are 17 harness invocations (S14 makes three). 16 matches neither count unless S14 is counted as two. The re-run itself is row 66. |
| 21 | End-waits on the wrapper's PID alone; end notices carried the outcome only; each launch announced; stamps "read only after the wrapper's PID had ended"; "nothing of the run was read until it had ended" | NOT CHECKABLE | No end-wait output is in any raw. SCR's wait_campaign.sh is PID-only (`ps -p` on the wrapper's name). |
| 22 | The per-checkpoint figures come from m's campaign report and p's report | CONFIRMED | Every value in rows 24–33 is in those fields. |
| 23 | Checkpoints and call logs "not opened" / "never opened by Code" (E, M, raws) | NOT CHECKABLE | The scripts in SCR only tar the files and digest them. |
| 24 | Table, ×3: launches 80/32; domain 80/32 at floors 80/32; pre-pick excluded 0/0; looks at 40 and 80, end at 112, none fired; hour cap 2 h not reached; hair trigger 0; (d) equal | CONFIRMED | arms, floors, prepick_excluded 0; looks at_launches 40/80 and end_look 112, fired false; hour_cap 2 and hour_cap_reached false. The cap equals stage.py:186 CAMPAIGN_HOUR_CAP (2 ×3) and each lock's §2 "hour cap = 2 h". hair_trigger n 0. The BAR lines fall after 40, 80 and 112 launches, all silent. |
| 25 | Table: sft cap_hits 1 and the rest 0; dpo and instruct all 0; sham proxy 320/320 attributed, 0 cuts; contrast forced control characters 0 | CONFIRMED | counters.sham.*.n; proxy.sham n_attributed 320 of n_rounds 320, n_cuts 0; contrast_forced_control_chars n 0 of 320. The stdout P-REPORT lines are identical. |
| 26 | Column header "sham counters, 320 rounds" with "the rest 0", and a withheld bullet that names only "the contrast arms' counts" | IMPRECISE | corrupted_spelling covers "the sham sessions' forced rounds" (128 per unit). Its count over the sham free rounds is withheld (the stdout's P-REPORT withheld line; counters.withheld). The "320" label is the stage's own, but the entry never says this class is withheld. |
| 27 | Launch counts were G-PWR (p)'s projection, A0 96 and A0s 64; COMPLETE at 112 when both arms reached their floors | CONFIRMED | launch_counts_projection 96/64; 3e1b614's entry "L 96 contrast and 64 sham"; each lock's §1 line. |
| 28 | sft's one sham cap hit is s=10's first forced round, "A0s-OLMo-sft s=10 forced 0" | CONFIRMED | p report key; stdout P-REPORT line. |
| 29 | pauses empty, stop null; no adjudication excerpt written | CONFIRMED | m reports. p reports: m_outputs.adjudication_excerpt.sha256 is null. The copy-back listed 12 files and no _adjudication.json. |
| 30 | Register entries (1), (2) and (6)–(9) entered; each identity carries its lock's sha256 and 641ee466f4553b6a | CONFIRMED | register_entered [1, 2, 6, 7, 8, 9] ×3; identity fields. |
| 31 | Term (d): single_threaded false with tqdm_monitor alive; recorded, never raised | CONFIRMED | term_d_at_stage_end ×3; stage.py lines 69–70 ("recorded … never raised"). |
| 32 | Contrast counts other than the forced rounds' control characters withheld to VERDICTS (m:318) | CONFIRMED | p's withheld note; m:318 (Blinding). |
| 33 | (d) bullet: report identifier against the lock's BACKEND OF RECORD, equal ×3, identifier only; each campaign raw carries its line | CONFIRMED | d_lines.txt matches each report's identity. The locks' BACKEND OF RECORD lines are at 267 (sft) and 266 (dpo, instruct). Each raw's header line 9 and section match d_lines lines 1–3. box_d_line.py prints the identifier only, as §1 (d) asks. |
| 34 | 12 outputs byte-identical to the box's (sha256 at both ends); checkpoints and call logs -diff | CONFIRMED | Copy-back: 12 × "identical". The raw headers and my exact-path shasum agree. `git check-attr` gives diff: unset on the 6 checkpoint/call-log paths (reports unspecified; not claimed). |
| 35 | The raws keep out the pod's address, its port and the local roots | CONFIRMED | Scans found no IPv4, no port form, no /Users/, /private/ or ~/, no BOX_ADDR or ssh options; only box /workspace paths. |
| 36 | "Rule 27 holds: the raws and checkpoints are committed before any pod stop." | IMPRECISE | The commit is prospective, so not checkable yet. Rule 27 also wants seeds, library versions and determinism flags pinned "in the logged entry", and the entry names none. They are only in each raw's verbatim PROVENANCE line (equal ×3 and equal to 7ab4d2f's: seed 20260818, torch 2.8.0+cu128, transformers 5.15.0, deterministic true, CUBLAS :4096:8). a225a89's entry named torch and transformers. |
| 37 | "The pod stays up, for n" | CONFIRMED | Routing item 5, "[keep]". |
| 38 | This session ran no laptop model process; its laptop steps were model-free | NOT CHECKABLE | |
| 39 | E "Not pushed. Committed by path."; M "RESULTS.md (one hunk, the entry at the top of the Log)…" | NOT CHECKABLE | Prospective. A path-scoped status shows the 12 outputs untracked, the 4 raw paths absent and RESULTS.md unmodified. |
| 40 | M subject line | CONFIRMED | As rows 1–5, 10 and 37. |
| 41 | M "The words" line | CONFIRMED | As rows 7–9. |
| 42 | M precheck line | CONFIRMED | As rows 14–15. |
| 43 | M wrapper line | CONFIRMED | Its end-wait clause is row 21. |
| 44 | M per-checkpoint line | CONFIRMED | As rows 24–25. |
| 45 | M Next line | CONFIRMED | As row 6. |
| 46 | M short forms (fd74d3f6...e3ff, 038bf3e, 7ab4d2f, m43y3deb1gq3rp, 641ee466f4553b6a) and the trailer | CONFIRMED | The trailer equals this session's attribution line. |
| 47 | Precheck raw structure | CONFIRMED | 7 `# ` header lines and 3 sections. precheck_campaign.txt is byte-identical (256b2aa2…, as in box_sha256.txt). Both scripts are byte-identical to SCR's; the section shas equal the bytes and both ship listings. |
| 48 | Precheck raw line 1: item 7's (a); 038bf3e; the seat file's path, sha, §1 and §2 item 3; the PI's go | CONFIRMED | |
| 49 | BOX line, identical in all four raws | CONFIRMED | As rows 10–13. |
| 50 | SYNC line: command (bundle path, target 7ab4d2f…), sha 0d1fab4e…971b, quoted line | CONFIRMED | Byte-equal to sync_out line 1; paths as in ship_box_sha. |
| 51 | Precheck COMMAND description, EXIT exit=0, RESULT | CONFIRMED | Against the script and its output. |
| 52 | Precheck run "env.sh sourced" in that cwd; "Run before the first campaign's launch"; SYNC "before the precheck" | NOT CHECKABLE | No stamp or log by design. Consistent with the precheck's HEAD 7ab4d2f. |
| 53 | Campaign raws' structure ×3 | CONFIRMED | 15 `# ` header lines and 5 sections. The stamps excerpts are stamps.txt lines 1–3, 4–6 and 7–9. Stdouts are byte-identical, carriage returns included (14/13/13, no CRLF; no git text attribute applies), and their shas 256cea9b…/e12ca013…/79effb32… match box_sha256.txt. Each d line matches; the wrapper and box_d_line.py are byte-identical, with section sha = bytes = shipped. |
| 54 | Campaign raws line 1: unit, BUILD c0f1c69, lock v1.0 038bf3e with full sha256, seat file, PI's go | CONFIRMED | c0f1c69 is "p -- the campaign wiring: BUILD". |
| 55 | Lines 3–4: precheck pointer; COMMAND via the wrapper with the checkpoint argument, env.sh sourced, cwd, one invocation, no --resume | CONFIRMED | Wrapper lines 15–16 and 29; INVOCATION lines; three stamps blocks. |
| 56 | Line 5: the chain rule's text | CONFIRMED | Matches the wrapper; the case count is row 20. |
| 57 | Line 6: stamps per seat §6 and §9 item 8; sft's one stamp; dpo and instruct "a later one… no stamp"; PROVENANCE "the Q4 ruling's unavoidable record"; "No other stamp" | CONFIRMED | Seat §6 "m's PROVENANCE start stamps remain as the unavoidable records"; the G-TIME-F0 read's Q4 list; report provenance[0] has a stamp; the _p-qual raw uses the same wording. |
| 58 | RESULT lines ×3 | CONFIRMED | As rows 3–5 and 24. |
| 59 | (d) header lines ×3 | CONFIRMED | As row 33. |
| 60 | OUTPUTS: digests and -diff | CONFIRMED | As row 34. |
| 61 | Stamp rule: exactly one launch stamp in all four raws together, in sft's; PROVENANCE start stamps only inside the verbatim stdouts; no other clock time in the six texts | CONFIRMED | The launch stamp is the sft raw's line 17 (stamps section). The PROVENANCE stamps are line 27 of each campaign raw. The entry, message and precheck raw have none. |
| 62 | No money figure | CONFIRMED | |
| 63 | No IP address or port of the pod | CONFIRMED | |
| 64 | No local absolute path | CONFIRMED | |
| 65 | No email except the Co-Authored-By trailer | CONFIRMED | |
| 66 | Dry-test re-run reproduces | CONFIRMED | All 15 scenarios (17 invocations) re-ran from a copy of harness.sh in SCR/vc5/rerun (python3 replaced by the venv python, nice 19). Every recorded output reproduced, launch stamp masked. The harness differs from the wrapper only by the declared substitutions (env.sh, cwd, OUT, the stubs). |

**What the seat's §2 item 3 and the routing's item 5 ask that the record leaves out**
1. **"One pod session" is never stated.** The seat's §2 item 3 asks for it. 038bf3e says each lock licenses its campaign "within one pod session", and p v0.2 §6.2 says the same. The record supports it: one provenance entry each, "runs: 1 first returned", resume false, and one pod id and HEAD across all three blocks. But no text says it, and nothing records whether the pod restarted between invocations.
   - Everything else in both items is carried: the bundle, the precheck ×3 with (a), 2 h each, looks every 40 (40, 80, end), (d) after each invocation in each raw, no pause and so no excerpt, commit before any pod stop, the pod kept up for n.

**Ambiguous claims and wording a reader could take two ways**
2. **"domain":** m's domain is launched minus pre-pick exclusions. It therefore pools valid sessions with any contrast session excluded after the pick, which m's session lines (verbatim in the raws) print phase-alone, as `excluded@free` (m:263, m:318). The Q-F0 campaign entry said so ("given pooled, as the domain, and are not split into valid and excluded@free"); this entry does not. A reader could take "domain 80" as "80 valid". One clause would fix it; no count is needed.
3. **"unchanged at HEAD"** could mean the box's HEAD (which is 7ab4d2f, so trivially true) or the repo's HEAD. It is true either way.
4. **"on the PI's word"** (headline, Next, message): that word is already given — B.6's "[go, after its commit]" under "Route as given". The phrase can read as a word still to come.
5. **"declared before the first launch"** does not say where; it was declared in the shipped wrapper's header.

**Form gaps against a225a89's precedent**
6. **Evidence the qual raw embedded is missing here.** a225a89's `_p-qual` raw embedded the wrapper's own log, the launch-call output, the end-wait outputs and script, and the copy-back output and script. These raws omit all of them:
   - wrapper-{ck}.out (each empty, e3b0c442… in box_sha256.txt);
   - the launch calls' output;
   - wait_campaign.sh and the end-wait outputs;
   - copyback_campaign_out.txt and copyback_campaign.sh.

   So rows 21 and 23 have no embedded evidence. The box's whole-file sha256 for stamps.txt (7f2d825d…) and d_lines.txt (866d661f…) is also not cited, so the three excerpts cannot be tied back to the whole files.
7. **Sham-arm validity is not reported.** Each stdout has 32 of 32 A0s lines "valid". The Q-F0 campaign entry and a225a89's entry both reported sham validity.

**Minor**
8. **tqdm load bar:** "Loading weights" in each campaign raw (line 25, CR-separated, verbatim) carries mm:ss elapsed/remaining times and it/s rates for the weight load. These are durations, not stamps, clock times or stage totals.
9. **Sync exit status:** the precheck raw does not state it (sync_out.txt reads "sync exit=0").
10. **Dry test coverage:** it uses dstub.py in place of box_d_line.py, and no case uses an "other" exit code such as 1. That branch is shared with exits 2, 4, 5 and 6, so the logic is covered.
11. **Concurrent laptop work:** "this session ran no laptop model process" is correctly scoped. It does not say whether another session's laptop model process, such as Q-F3's campaign, ran meanwhile. Probably not owed, since this session's laptop steps were model-free.

**Glosses**
- E: the entry, entry_camp.md
- M: the commit message, msg_camp.txt
- relay_go: SCR/relay_go_as_received.txt
- relay_routing: SCR/p1/relay_routing_as_received.txt
- the seat file: results/raw/2026-11-14_p-backend-line_design-to-code_answers.md
- the seat's G-ID-F3 answers: results/raw/2026-11-10_gid-f3_design-to-code_answers.md (c51ef5ba…)
- the G-TIME-F0 read: results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md

**Disclosures (mine)**
- **Reports:** read the six report files by exact path with a model-free script. It printed their key tree and the stated fields, plus a few unstated ones (schedule_n, file paths), none of which appear above. Checkpoints and call logs got sha256 only.
- **Git commands on data/p paths:** one `git status --porcelain --` on 17 exact paths (path-scoped; git may refresh .git/index's stat cache, a write to git's index only), and `git check-attr` on the 12 outputs.
- **The bundle:** `git bundle list-heads`, `git bundle verify` and `head -c 400` on SCR/p-campaign.bundle. Its pack holds committed blobs of eb3e08c..7ab4d2f, committed checkpoint files among them. Only the ref, the prerequisite and its commit subject were printed.
- **Scratch files read:** SCR/watch.log (times masked when printed; it carries price figures, none reproduced here), wait_campaign.sh and copyback_campaign.sh.
- **Stamps:** I saw the launch, PROVENANCE and dry-test stamps. I computed nothing from them; I compared the dry-test stamps with the launch stamp for order only.
- **Searches:** `git grep` over committed raws with `':!data/**'`.
- **Writes:** nothing touched under data/, and nothing listed or searched there. Writes only under SCR/vc5/ (struct.py, fields.py, quotes.py, keys.py, my_sha12.txt, rerun/).
