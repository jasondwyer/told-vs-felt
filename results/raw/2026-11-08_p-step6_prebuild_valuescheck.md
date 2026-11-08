# The step-6 pre-build block: the blind values-check, with Code's dispositions

*Code's raw, PI-local date 2026-11-08. The check ran on the block's first draft (eight questions), before the commit of `results/raw/2026-11-08_p-step6_code-to-design_prebuild.md`. It was a blind subagent given the draft and its sources, and its report is in section 1, verbatim. Every FAIL and IMPRECISE item was re-checked at source by Code and applied (section 0). The revised claims were checked by tool, not by a second blind pass. The draft's line numbers (L#) refer to the first draft, not the committed text.*

## 0. Code's dispositions

| item | verdict | disposition |
|---|---|---|
| #5 | FAIL | **Applied; a ninth question.** m's `load_committed` runs m's `verify_schedule_dir` (`stages.py:906`; `schedule.py:620`). Code ran it, read-only, on `data/p/schedules` with entry (2) in force: 14 problems (the six campaign files, Q-F0's seven missing files, the manifest). p's verifier reports none. It is now Q2, with a proposed entry (7). The draft's Q2 ("No site is needed" under its option (a)) is now Q3, and the "two sites" wording is gone. |
| #39 | FAIL | **Applied.** The proxy has no such check today. Q5 now states it as Code's plan: a check added to the proxy, which moves p's package (`daca8b0` §2), and a STOP raised there would end the stage without m's stop record. It also asks whether the seat wants a stop through m's record instead. |
| #17 | IMPRECISE | **Applied.** The block now says "every path a stage writes, and the schedules it reads, derive from the root" and names the files read outside it. |
| #20 | IMPRECISE | **Applied.** Q1 now says "Within the register's kinds there is no alternative", and §1 names the pinned-restatement route (P21's) as the one term (e) admits. |
| #24 | IMPRECISE | **Applied.** "the record minus `BACKEND_DROP` (`n_encodes_clipped`, `path`, `seed`; `resume.py:147`, `:242`)". |
| #27 | IMPRECISE | **Applied.** At G-TIME entry (2) puts `p-olmo-time|…`, `p-olmo-items-time|…` and `p-sched|…`; `p-olmo|…` is the campaign's arm family. |
| #29 | IMPRECISE | **Applied, and the recommendation reversed.** F-p8 puts `proposal_p_sha256` "in every p artifact -- gates, checkpoints, ...", and G-CAL-p's checkpoint identity carries p's fields inside it. Q3 now recommends (a), two identity sites as F-p8 and p:84 read, with the sidecar as option (b), which reads both "in"s as "beside". |
| #32 | IMPRECISE | **Applied.** Q4 now says when each entry is read: entry (2) per session; entry (1) at stage start (`corr.startup_hygiene`, `stages.py:366`) and at the first, lru-cached, `scaffold._of_record` call (`scaffold.py:210`); entries (6) and (7) at stage start. It adds the RENDERS MISMATCH consequence (`stages.py:1063`) and Code's reading that every substitution is entered before anything in the process computes renders. |
| #46 | IMPRECISE | **Applied.** A-m1's (16) does not collide (Q-F0, PASS, as m's NOT-RUN records carry it), and "this document's adoption" is not placed by p; Q6's proposal places both in m's list. |
| #49 | IMPRECISE | **Applied.** m's VERDICTS and NOT-RUN outputs carry `proposal_sha256`; the secondary output carries none (checked: `Q-F0_secondary.json`). Q7 adds `proposal_p_sha256` to every output, the secondary included. |
| #57 | IMPRECISE | **Applied.** The verification sentence is cited at p:86 (checked: "verified against this document's committed sha at every run"); p:100 defines D_p. |
| #58 | IMPRECISE | **Applied.** `clock_problems` checks ADDENDUM-m1's sha256, D_O′ (A-m1:28) and D2 (A-m1:40); D1 is verified on m:16 through the proposal's sha pin. |
| #63 | IMPRECISE | **Applied.** §0.1 binds entries, lock lines and posted sentences; the block says putting the sentence in the outputs is Code's choice. |
| #55 | note | **Applied.** Q8 names the binding the NOT-RUN regression needs: analyzer `6ec3222b…`, package `60199b36…`, closure `a3bc7bb9…` (checked in the three outputs), supplied from the record as Q-F0's is. |
| #62 | note | **Applied.** §3 surfaces the lexicon pick for the seat (a full dictionary, not a common-words list), with its effects on both gates' records, and §4 asks for the seat's word. |
| #66 | not checkable | **Applied.** The opening now scopes "nothing built" to step 6's stage driver and analyzer, and §3 names the rulings work in the tree. (The check took that work for a parallel session's; it is Code's, in this session.) |
| #12, #34 | not checkable | Stand. #12: the lock file does not exist yet. #34: the progress-bar thread is a stated possibility, F-p9's. |

## 1. The values-check's report, verbatim

## Values-check of results/raw/2026-11-08_p-step6_code-to-design_prebuild.md

I edited no files. The cited sources are byte-identical to HEAD (daca8b0) with one exception: `valence_core/p/report.py` is being changed in the working tree by a parallel session (+225/−48), and `data/p/lexicon/web2.txt` is untracked. For claims about the reporting tool I used HEAD's `report.py`. Memo lines are given as L#.

### 1. Table

| # | Claim (short) | Verdict | Evidence |
|---|---|---|---|
| 1 | Title: "eight questions" | CONFIRMED | Q1–Q8. |
| 2 | L3: PI routing of 2026-11-08, item 1, "Step 6 [go]" | CONFIRMED | RESULTS.md close at daca8b0: "> 1. G-CAL-p: read closed; … Step 6 [go]. Pod: [keep up through LOCK-p v0.1] (~$43/day idle)." |
| 3 | L3: seat's answer path, at daca8b0, sha256 `4b77e39a…48e1`, §4 | CONFIRMED | shasum 4b77e39a05c9…12143548e1. The file was added at daca8b0, and its §4 is "Step 6 — the PI's go, and the pod". |
| 4 | L3: p:N = p v0.2 (18b0111); m:N = m v1.11 | CONFIRMED | Only 18b0111 touches p (sha 42f2977b…). m's sha is 42ab36ec…6c6b. |
| 5 | L6 "Two sites that p's gate stages need are not in p's register"; L20 "Two attributes of m's code stand in the way, Q1 and Q2" | **FAIL** | There is a third blocker. `run_gate_stage` calls `load_committed(…, paths["schedules"])` (stages.py:1475). That runs m's `_schedule.verify_schedule_dir(d)` and raises SystemExit "SCHEDULES NOT CLEAN" on any problem (:904–907). m's verify regenerates every file of `build_schedule_objects()` over `keys.UNITS_BUILT`, Q-F0 included (schedule.py:539–557), plus m's own manifest (:578–586), and requires each to be present and identical (:620–649). `data/p/schedules` holds only the 18 OLMo files plus p's manifest (a different "construction" string). Its six campaign `key_template`s differ from m's builder output under entry (2) (p/schedule.py:8–15). So m's check would report 7 Q-F0 files missing, 6 campaign files differing and the manifest differing, and stop before any session. The BUILD design raw already records this (2026-11-07_p-build_design.md:127–128). Separately, the memo contradicts itself: under Q2's recommended option (a), "No site is needed". |
| 6 | L6 term (e) quote | CONFIRMED | register.py:14–15, exact. |
| 7 | L7: one p §4.1 sentence cannot be met by m's analyzer | CONFIRMED | p:84 is §4.1; its m:318 sentence collides with m_analyze.py:701. |
| 8 | L8: three readings of p §4.4 | CONFIRMED | Q6–Q8. |
| 9 | L14 `run_gate_stage` at stages.py:1449 | CONFIRMED | The def is at :1449. |
| 10 | L14 "the only way to run m's stage logic without a copy (term (e))" | CONFIRMED (reading) | Composing m's helpers would restate :1462–1529. Term (e) admits a restatement only as a pinned copy, so "without a copy" holds. The P21 precedent (a pinned copy) is relevant to #20. |
| 11 | L15–16: proxy is §2.2; `data/p/schedules` built at a665a09 | CONFIRMED | a665a09's stat shows 18 files and a manifest; no later commit touches them. Usability: see #5. |
| 12 | L17 `LOCK-p-OLMo-{ckpt}.md` as the lock_file | NOT CHECKABLE | The file does not exist yet. The name follows m_sessions.py:693–695 (`LOCK-m-OLMo-{ckpt}.md`) and p:84. |
| 13 | L18/L34: m's proposal pin (F-p8) in the identity | CONFIRMED | Rulings §2; `proposal_sha256=extra[…]` at stages.py:1111. |
| 14 | L22: F-p9 "recorded without a ruling" | CONFIRMED | Rulings :29: "F-p2 (…), F-p4, F-p9: recorded, no ruling." |
| 15 | L23: stages.py:139 code | CONFIRMED | Exact. |
| 16 | L24: `_out_root_guard` (:299, comparison :310) refuses a non-stub run off DEFAULT_OUT | CONFIRMED | :307–312. |
| 17 | L25 "Every path a stage writes or reads derives from the root" (out_paths :209) | IMPRECISE | Overstated: see list 2. |
| 18 | L27: entry (6) is of kind roots; with it m's guard admits data/p | CONFIRMED | "roots" is in KINDS (register.py:33). The guard reads the module global DEFAULT_OUT at call time (:309). |
| 19 | L27: p's guard refuses m's and mf3's roots, as now | CONFIRMED | p/guard.py:11–12, :57 (REFUSED_ROOTS), :117. |
| 20 | L27 "There is no alternative" | IMPRECISE | Overstated: see list 2. |
| 21 | L29 p:84 quote (proposal field) | CONFIRMED | Exact. |
| 22 | L30: IDENTITY_KEYS at resume.py:93, IDENTITY_KEYS_OLMO at :106; exact key set | CONFIRMED | `_validated` at :502–506. |
| 23 | L30: `_extra` admits only m's keys (:962, :1004) | CONFIRMED | ValueError at :1004–1009. |
| 24 | L31: `backend_identifier` "hashes the whole record" (resume.py:242) | IMPRECISE | It hashes the record minus BACKEND_DROP (:147). The conclusion stands: 641ee466f4553b6a is the identifier of record in all three G-CAL-p artifacts. |
| 25 | L35: LOCK-p's sha256 in the identity | CONFIRMED | `lock_sha256` at stages.py:1110. |
| 26 | L36: `key_templates` rendered through `keys` at run time (resume.py:386) | CONFIRMED | Module-attribute calls at :391–394. |
| 27 | L36 "entry (2) puts `p-olmo|…` there" | IMPRECISE | At G-TIME the arm key is `p-olmo-time|…`, not `p-olmo|…`: see list 2. |
| 28 | L37–38: p's renders sha16 and schedule sha256 in the identity | CONFIRMED | stages.py:1107, :1113. Caveat for the renders: see #32. |
| 29 | L41 (a): "No site is needed; p §4.1's 'in' is read as 'beside'" | IMPRECISE | Incomplete: F-p8 also says "in": see list 2. |
| 30 | L42 (b): IDENTITY_KEYS_OLMO plus the identity builder | CONFIRMED | `identity_keys` reads the constant at call time (:112–114). `Identity` builds a fixed dict (:484–499). |
| 31 | L44: Q3 is F-p9's other half | CONFIRMED | Design raw :264–268. |
| 32 | L44: `_renders_of_record` at :1060; the renders (and entries 1, 2, 6) "read them per session" | IMPRECISE | The line is right; "per session" is wrong for the renders and for (6): see list 2. |
| 33 | L44: arm/item streams and G-VER's rebuild read entry (2) per session, after the load | CONFIRMED | `scaffold.m_config` uses `keys.arm_key`/`item_key`; verify.py:121, :135. |
| 34 | L45: a library thread may be alive (the load's progress bar) | NOT CHECKABLE | Nothing in the repo shows it; the wording matches F-p9's. |
| 35 | L47: m_sessions.py:1742 loads, :1750 calls `run_gate_stage` | CONFIRMED | Exact. |
| 36 | L48: `assert_single_threaded` runs at the entry | CONFIRMED | `substituted` calls it at register.py:116. |
| 37 | L53: the trigger cannot fire once the proxy cuts | CONFIRMED | proxy.py:61–74; p:68. |
| 38 | L53: m's stage evaluates only m's hair triggers (`_hair_hit` :1195) | CONFIRMED | It reads `rec["hair_triggers"]`, which m's runner sets. |
| 39 | L54 "The proxy checks every stored text it returns and raises a STOP there" | **FAIL** | Not true of the existing proxy: see list 2. |
| 40 | L54 "unreachable by construction" | CONFIRMED | The cut text is `text[:first_break].rstrip()`. |
| 41 | L55: the tool lists control-character texts by key (daca8b0 §1 (a)) | CONFIRMED (note) | §1 (a) binds "every stage's entry … by name". HEAD's `counters()` already returns each counter's keys (report.py:118–130). |
| 42 | L61: p:84 quote (the m:318 sentence); m:318 | CONFIRMED | Exact; m:318's last sentence. |
| 43 | L62: m_analyze.py:701 refuses `other_unit == unit` | CONFIRMED | Exact. |
| 44 | L63/65: p keeps m's unit strings; the collisions | CONFIRMED | p:84 "**p's records keep m's unit and template strings**". |
| 45 | L68: `decisions_with_other_outcomes_known` validated by m | CONFIRMED | :690–718. |
| 46 | L69: A-m1's (16) goes in the p block, "named PROPOSAL-m OLMo-{ckpt}" | IMPRECISE | (16) does not collide: see list 2. |
| 47 | L73: p §4.4 "in m's schemas plus `proposal_p_sha256`" | CONFIRMED | p:90, exact. |
| 48 | L73: entry (3) "recorded beside it in every p output" | CONFIRMED | p:86 (entry (3) as declared in §4.2), exact. |
| 49 | L73: m's outputs carry a top-level `proposal_sha256` (`data/m/verdicts/*.json`) | IMPRECISE | The secondary-DV output carries none: see list 2. |
| 50 | L76: m's refusals on its out dir | CONFIRMED | Write-once; `refuse_beside` at :2654. |
| 51 | L88: the regression reads `REPO / CKPT_REL`, `REPO / VERDICTS_REL` (:9913) | CONFIRMED | Exact (also :10082). |
| 52 | L88: PIN-29 snapshot guards data/m | CONFIRMED (note) | `_bt_snapshot` covers data/m and data/mf3 (:5149–5154). |
| 53 | L91: battery count and coverage as at G-ANL-F3 | CONFIRMED | 02dadb3: 525/525, 538 ids. |
| 54 | L92–96: p's groups | CONFIRMED | They are p:90's list. |
| 55 | L97: regression; NOT-RUN outputs at 0f35954 | CONFIRMED (note) | REGRESSION_OUTPUTS at :9855; 0f35954's stat. Note: the three NOT-RUN outputs are bound to analyzer 6ec3222b…, package 60199b36… and closure a3bc7bb9…, while HEAD's analyzer is d347ea0c… (PIN-42; 10a2bbb). "Byte for byte" needs that binding, which the memo does not name. |
| 56 | L102: `clock_of_record` at :548 | CONFIRMED | Exact. |
| 57 | L102: "D_p is verified at every run … (p:100)" | IMPRECISE | Wrong line cited: see list 2. |
| 58 | L102: `clock_problems` "(D1, D_O′ and D2 against ADDENDUM-m1, :574)" | IMPRECISE | D1 is not checked there: see list 2. |
| 59 | L103: `run_not_run`'s `ckpt_dir` (:2583) | CONFIRMED | Parameter at :2552, default at :2583. |
| 60 | L104: `crosscheck_coordinate` call at :4378 | CONFIRMED | In `run_posting_v2`, with one `verdicts_dir` for all four UNITS. |
| 61 | L111: daca8b0 §1 (F-p13) | CONFIRMED | |
| 62 | L112: daca8b0 §3 (F-p11) | CONFIRMED (note) | The memo drops the seat's parenthesis "(a frozen common-words list)". The in-progress tree picks web2.txt, a full dictionary, which its own WIP PIN says is not a common-words list. Worth surfacing. |
| 63 | L113: §0.1 "as a constant that every SFT-row output carries" | IMPRECISE | Scope wider than §0.1: see list 2. |
| 64 | L115: G-SHAPE-p re-runs after the last package move (§2) | CONFIRMED | |
| 65 | L116: pod stays up and idle (PI item 1) | CONFIRMED | |
| 66 | L10 "Nothing has run and nothing is built" | NOT CHECKABLE | §3 work is in progress in the tree (report.py, data/p/lexicon). If committed after it, scope the sentence to step 6. |

`PRIOR_STAGE` (on your list) does not appear in the memo. In the code it is as described: G-TIME has no prior stage (stages.py:644, :800–804).

### 2. FAIL and IMPRECISE items, with correct text

- **#5 (L6, L20), FAIL.** "Three attributes of m's code stand in the way: the stage roots (Q1); p's identity fields (Q2, under option (b) only); and the schedule check. `stages.load_committed` (:894–907, called at :1475) runs m's `schedule.verify_schedule_dir` on `<out_root>/schedules`. That function regenerates all four units' files and m's manifest, so it refuses `data/p/schedules` (design raw P4, :127–128)." This needs its own question and site.
- **#39 (L54), FAIL as written.** The existing proxy has no such check. It raises ProxyStop only when a break cannot be placed on the token ids (proxy.py:67–70). G-CAL-p's trigger check sits in p's gcal loop (gcal.py:526–530). Reword as a plan: "Code adds to the proxy a check of every stored text it returns, a STOP there (unreachable by construction). This moves p's package, so daca8b0 §2's re-run rule applies." Also note that a SystemExit raised inside `run_session_olmo` leaves `run_gate_stage` without m's stop record.
- **#17 (L25).** Say: "Every path a stage writes, and the schedules it reads, derive from the root." The stage also reads, outside the root, the files at `proposal_file` and `lock_file` (:377–378, :553–565), the analyzer (:586–588), `data/olmo/manifest.json` (resume.py:107, :492–493), and the pool and term files.
- **#20 (L27).** Say: "Within the register's kinds there is no alternative." Substituting the guard function itself is barred by term (b), not by the code. Term (e)'s pinned-restatement route was admitted for G-CAL-p for the same reasons (roots, identity, no hair trigger; rulings §4).
- **#24 (L31).** Say: "hashes the record minus BACKEND_DROP (n_encodes_clipped, path, seed; resume.py:147, :242)."
- **#27 (L36).** Say: "so entry (2) puts p's prefixes there: at G-TIME `p-olmo-time|…`, `p-olmo-items-time|…` and `p-sched|…` (`p-olmo|…` is the campaign's arm family)."
- **#29 (L41).** Add that F-p8 (rulings §2) puts `proposal_p_sha256` "In every p artifact — gates, checkpoints, locks' identity blocks, the analyzer's outputs". G-CAL-p's checkpoint identity already carries `proposal`, `proposal_p_sha256`, `p_package_sha256` and `renders_sha256_p` inside it. So (a) reads F-p8's "in" as "beside" too, and the gate-stage checkpoints would differ in form from G-CAL-p's. p:86 lists "resume identity carrying p's package hash and the proposal field" among p's own modules.
- **#32 (L44).** Say: "Entry (2) is read per session after the load (m_config; G-VER's rebuild). Entry (1) is read at stage start by `corr.startup_hygiene` (:1129; corr.py:421–426) and at the first `scaffold._of_record` call, which is lru-cached per process (scaffold.py:210–213; `_renders_of_record` runs once, at :1473). Entry (6) is read only by the guard in `_begin` (:1125)." Consequence: any render computation before entry (1) in the process would fix m's renders and stop the stage with "RENDERS MISMATCH" (:1063–1066).
- **#46 (L69).** m's own NOT-RUN records (0f35954) carry A-m1's (16) with other_unit "Q-F0", other_state "PASS", which m's validator accepts. Only the three NOT-RUNs collide. Also, p:84's fourth item, "this document's adoption", is not placed by the proposal.
- **#49 (L73).** Say: "m's VERDICTS and NOT-RUN outputs carry a top-level `proposal_sha256`." `Q-F0_secondary.json` (m-secondary-v1, one of the regression's two outputs) carries none at any depth. The directory's input files carry none either.
- **#57 (L102).** Cite p:86, entry (3): "verified against this document's committed sha at every run". p:100 only defines D_p.
- **#58 (L102).** Say: "`clock_problems` checks ADDENDUM-m1's sha256 and D_O′ (A-m1:28) and D2 (A-m1:40) at :574." D1 is verified on m:16 through the proposal's sha pin (comment at :130–133), not against ADDENDUM-m1.
- **#63 (L113).** §0.1's scope is "every entry, lock line and posted sentence that reports OLMo-SFT's A0 outcome". Putting it in outputs is Code's choice; say so.

### 3. Counts

66 items: 50 CONFIRMED, 2 FAIL (#5, #39), 11 IMPRECISE (#17, 20, 24, 27, 29, 32, 46, 49, 57, 58, 63), 3 NOT CHECKABLE (#12, 34, 66).
