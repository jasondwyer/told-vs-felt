# G-ID-F3 at cap 120: FAIL. The first pair (A2s, index 0) diverged. Code's block for the seat's read of the pairs

*Code (F3 session), PI date 2026-11-10.*
- **The run.** G-ID-F3 (PROPOSAL-m v1.11 m:295) ran on Qwen on the laptop, at the cap of record, 120.
  - It ran under LOCK-m-F3 v0.1 as re-issued (`f674583`, sha256 `70da4a70…1d3f`).
  - The driver was the one the `id` wiring committed at `fb82daa`.
  - Its prior was G-TIME-F3's re-run checkpoint, taken by path.
- **For the seat:** the pair's records, the counters, the timing, and what the record says follows. The seat's read of the
  pairs comes before LOCK-m-F3 v0.2 (the seat's read of G-TIME-F3 r2, §5 items 2–3).
- **Code adjudicates nothing.** The FAIL is the stage's computed verdict, and its consequence is the one the record
  declares (§4).
- **Sources.** The stage's report and reads (`data/mf3/reports/Q-F3_id_report.json` and `Q-F3_id_reads.json`) were
  read after the invocation had ended, under the list of record v2's item 2, together with the artifact
  (`data/mf3/gates/Q-F3_G-ID.json`). The checkpoint (`data/mf3/ckpt/Q-F3_id.json`) was hashed only.
- **Form.** G-ID-F3's sessions are sham-only, and the reads file holds their full records (lock F14). This block renders
  the two configs by role, [P] and [Q], pending the seat's Q3 (§5).

## 0. The run

- **The routing.** The seat's §8 item 4, routed by the PI on 2026-11-10 ("Route as given"): "The `id` wiring (F-1's
  kind, named in its entry) → G-ID-F3 at 120 on the laptop, announced, ≈ 1 h → the seat's read of the pairs →
  LOCK-m-F3 v0.2 to §5 [go]".
- **The wiring.** It is committed at `fb82daa` (the entry names the edit). The driver's blob, as the DRIVER line
  printed it before the load, is `8d878f4a894e05e4edf8a3c829548a9c0c864d5f45118875b7630e55d1d200e7`.
- **The announcement and the ack.** Code announced the run with the wiring's hash. The coordinating session's ack
  says: "G-ID-F3 at cap 120 may launch." Further, in its words:
  - "The laptop: `pgrep -ifl python` matched nothing just now."
  - "The pod session is idle and holds every box and laptop step until the PI's word."
  - "Until your end notice, my session starts no Python process and runs no listing of the tree."
- **The dry pre-launch check returned CLEAR twice**: once before the announcement, and once just before the launch.
  - It covered the identity (no `locked_path`; `reasoning_cap` 120), the precheck, the driver (committed at `fb82daa`,
    working tree identical) and the snapshot (the lock's revision), with nothing loaded.
  - Its prior gate was replaced by a recorder. The list's item 2 has the checkpoint read by nothing but the stage's own
    code, G-VER, the analyzer and the pre-push screen, and a dry check is none of them. The recorder showed the precheck would pass `Q-F3_time-r2.json`, with `require_real` on, at cap 120.
  - The run's own precheck ran the gate.
- **The launch.** It used m:267's line, as written: `nohup caffeinate -is /bin/zsh <wrapper> > /dev/null 2>&1 & disown`,
  at HEAD `fb82daa`. The command that launched it carried no literal "python", and refused to launch if
  `pgrep -ifl 'pytho[n]'` matched anything. Nothing matched.
  - **A correction to the launcher's comment.** The launch PID's command line, read once at the launch, was
    caffeinate's (`caffeinate -is /bin/zsh <wrapper>`). The launcher's comment calls it "the wrapper's".
  - The end-wait matched the wrapper's file name in that command line, then waited for no `mf3_sessions.py id`
    process.
    Either way, it is the PID alone.
- **The raw's header:**
  - "Now drawing from AC Power; Wattage 140 W; disk: 630Gi available on /; HF_HUB_OFFLINE=1".
  - The probe, in its new form (§8 item 7): "python processes before the run (pgrep -ifl python: the argument-list
    match, case-insensitive; each match's full command line, uncut): 0". No line followed.
- **While the stage ran:**
  - Code's session ran no model and no Python process.
  - It read committed documents and code (A-m2 v0.5 §3.4, mf3's source), and wrote its read script.
  - It read nothing of the run's raw, checkpoint or reports until the end-wait reported.
  - It was not compacted and started no subagent.
  - Whether another session ran a non-model process is not known to Code.
- **The end notice**, as the seat's §4 now has it: "G-ID-F3 ended. Exit status 5 (stages.EXIT_CODES: FAIL)." No
  stamp, no window.
- **The stdout lines** ([`_mf3-gid-f3`](2026-11-10_mf3-gid-f3.txt), local roots scrubbed; no finish stamp):
  - `DRIVER scripts/mf3_sessions.py 8d878f4a…00e7: committed at HEAD fb82daa…, working tree identical`
  - `SNAPSHOT mlx-community/Qwen3.6-27B-4bit c000ac2c2057d94be3fa931000c31723aac53282: refs/main; …; 1 snapshot(s) in
    the model's cache repo; HF_HUB_OFFLINE=1`, then `SNAPSHOT re-read after the load: unchanged (c000ac2c…); …`
  - the GATE and LICENCE lines (the proposal `42ab36ec…`, the lock `70da4a70…`, the analyzer `d347ea0c…`, mf3's
    package `098455d9…`, the eleven m files and the weights; A-m2 v0.5 `f27505c5…`), and the PROVENANCE line (MLX
    0.31.2, mlx-lm 0.31.3);
  - `id A2s s=0 valid`, twice (the uncached half, then the cached);
  - `BAR gid_divergence@G-ID-F3 FIRED`
  - `STAGE G-ID-F3 FAIL path=cached+uncached`
  - the CHECKPOINT, REPORT, READS and G-ID ARTIFACT lines, then `EXIT=5`.
- **The identity** (the report's): backend `a734dadec8f8ce9b`, as at G-TIME-F3's two runs and G-TIME-F0; reasoning cap
  120; path `cached+uncached`.

## 1. The verdict and the pair

- **The verdict:** FAIL. The artifact records verdict `FAIL`, `n_pairs` 1 and `pairs_identical` `[false]`, under
  the seat's F-7 criterion.
  - The bar `gid_divergence@G-ID-F3` (lock §8, bar 6) fired at k = 1 of n = 1.
  - The stage "stops at the first divergence (m:281, m:295)" (bar 6's row), so A3s did not run.
- **The pair: A2s, index 0** (j = 0). Both halves are on the same schedule cell, keys and banner, and both are
  complete, valid and verified, with no exclusion and no hair trigger.
  - The report's pair record: `transcript_identical` false, `line_triples_identical` false, `complete` true.
- **The forced rounds are identical:**

  | round | role | task | uncached | cached |
  |---|---|---|---|---|
  | 1 | P | Compute 90 minus 45. | `45` | `45` |
  | 2 | P | Compute 14 times 2. | `28` | `28` |
  | 3 | Q | Write the opposite of 'hot'. | `cold` | `cold` |
  | 4 | Q | State the number of days in a week. | `9` | `9` |

  Round 4's answer is wrong, the same on both paths.
- **The first difference is in round 5's reasoning line.**
  - The transcripts (3,103 and 3,424 characters) agree in their first 658 characters.
  - Both lines open "[P] has answered both of its assigned " after the harness's opener. Then the uncached line goes
    on "rounds correctly (90-45=45, 14*2=2)…" and the cached one "tasks correctly (90-45=45, 14*2=28)…".
- **All six reasoning lines differ.**
  - Tokens, uncached: 66, 57, 35, 62, 95, 60. Cached: 88, 64, 71, 75, 41, 95.
  - None reached the cap, and every one stopped at a newline.
- **The free rounds:**

  | round | pick (uncached / cached) | task (uncached / cached) | uncached | cached |
  |---|---|---|---|---|
  | 5 | P / P | State the number of hours in a day. | `24` | `24` |
  | 6 | P / P | State the number of wheels on a bicycle. | `2` | `2` |
  | 7 | P / P | Name the first month of the year. | `january` | `January` |
  | 8 | P / P | Compute 60 divided by 5. | `12` | `12` |
  | 9 | P / P | Write the opposite of 'up'. | `down` (2 tokens) | `down` (1 token) |
  | 10 | P / Q | Name the third month of the year. / Compute 11 + 33. | `March` | `44` |

  - The first free pick is P on both paths.
  - The picks agree through round 9. At round 10 the cached half picks Q, so its task is the other config's item.
- **The reads at round 10** (each `verify_kl` 0.0):
  - uncached: label mass .368, its top-1 token not a label, the pick P;
  - cached: label mass .682, its top-1 a label, the pick Q.

## 2. The counters (A-m2 v0.5 §3.4; rule 23, descriptive, deciding nothing)

The domain is all of G-ID-F3's rounds and lines, since its sessions are sham.

- **(a): 2 of 12 reasoning lines.**
  - Uncached 0 of 6.
  - Cached 2 of 6: lines 5 and 6 (rounds 9 and 10) each end with the session banner, `=== Config evaluation
    session ===`, after a cut-off sentence.
    - Line 5: "… 24 hours in a === Config evaluation session ===".
    - Line 6: "… makes it the clear choice for the === Config evaluation session ===".
  - The line audit claims neither: no class, no defect, no echo line. A-m2 v0.5 §1's match is "equality after
    whitespace normalization". A line that contains the banner but is not equal to it falls to counter (a), Q8's
    containment, not to the echo class.
  - G-ID-F3 has no reasoning-line defect bar (lock §8). Counter (a) is descriptive at every stage (§3.4).
- **(b), Code's declared read: 0 of 20 responses.**
  - No audit class claims any of the 20 rounds.
  - Every response is an answer attempt to its own round's task, correct or wrong: the two tables above. Cached round
    10's `44` answers its own item, "Compute 11 + 33.".
  - The seat confirms or corrects.

## 3. Timing

- From the report, sham, readable: the uncached half took 1,942.675 s and the cached half 208.347 s.
- For v0.2's projections, beside the seat's stated basis, the re-run's sham mean of 1,111.9 s (its §3, §5 item 3):
  - this uncached A2s member is one more uncached sham session at cap 120, its lines 35–95 tokens;
  - the cached member's seconds are recorded.
- Code computes no projection from them: the projections are v0.2's, on the basis the seat sets.

## 4. What the record declares follows (quoted; Code adjudicates nothing)

- m:295: "a divergence sends Q-F3 uncached".
- Lock §8, bar 6, its consequence: "G-ID-F3 FAIL: Q-F3 runs uncached (m:295)".
- `stages.PRIOR_STAGE`'s PIN: G-F3 needs "G-ID-F3's artifact on disk at the run's reasoning cap (any verdict: FAIL or
  NOT-DETERMINED send Q-F3 uncached, m:295)".
- Code's description, not a quote: `guard._gid_pass` (`valence_core/mf3/guard.py:97–102`) admits the cached path
  only on an artifact whose verdict is PASS, with `n_pairs` 2, both pairs identical, at this backend and this cap.
- The seat's §5 item 3: LOCK-m-F3 v0.2 records "the cap 120 with m:294's count (0 of ≤ 36) beside; the path G-ID-F3
  fixes, with its artifact; the projections at the measured bases".

## 5. For the seat

- **Q1, the FAIL and the path.** G-ID-F3 computed FAIL at its first pair, whose transcripts and line triples both
  differ (§1). The record's consequence is that Q-F3 runs uncached (§4).
  - Code asks the seat to read the pair and rule the FAIL and the path.
  - LOCK-m-F3 v0.2's contents under it are the seat's §5 item 3. For the cached projection, the seat says whether v0.2
    carries one under a FAIL: the cached member's 208.3 s is on record (§3).
- **Q2, counter (b) = 0 of 20** (§2). Confirm or correct.
- **Q3, the reads' form.**
  - The seat's §5 item 2 says G-ID-F3's sessions "are read by the seat under m:271's rule (redacted reads; the pairs'
    transcripts compared)".
  - The reads file the stage writes holds the full records (lock F14: "G-ID-F3's reads are the full sham-only records
    (§4 exception (4))"), labels and picks included. This block renders the labels by role.
  - m:271 itself: "G-ID's sham-only sessions are read in full at G-ID (nothing to blind; §4 exception (4))".
  - Code reads F14 and m:271 as governing the file the stage writes, and asks the seat to confirm, or to say what is
    redacted before the commit's raws quote it.
- **Not a question:** counter (a)'s two cached lines (§2) are recorded descriptively. G-ID-F3 has no reasoning-line
  defect bar. The record's consequence (§4) is that Q-F3 runs uncached, which Q1 puts to the seat.
