# ADDENDUM-m1 v0.1 — Code's §4 steps 1–2: the delta read and the referent check

*Code's raw. Written 2026-11-06 UTC (`date -u` at write: Fri Nov 6 01:29:38 UTC 2026); the routing's PI date is
2026-11-05. Anchors: `m:N` = `PROPOSAL-m-gating-campaign-v1_11.md` at root (tracked, sha256
`42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b`); `RESULTS.md@18c32df:N` = the RESULTS.md blob at
`18c32df`; `m_analyze.py:N` = `scripts/m_analyze.py` at `18c32df`. [C] = a figure a tool computed in this session.*

Document checked: `ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md`, 67 lines, sha256
`ea08322d601011923524021832d27d0ddf57b3e51ee4d88f265985c6c9bf9001`, equal to the routing's.

## 1. Step 1 — delta read (report only)

- **HEAD** `18c32dff190c530ce1b5679dc3e7277be90a05c9`, `main == origin/main` (`git fetch --dry-run` printed nothing
  new). The routing expects HEAD at or after `18c32df`; it is at.
- **The untracked root as the routing names it:** `ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md` and
  `PROPOSAL-n-bk-reconciliation-v0_1.md` (sha256
  `9248d06c0837bd7bd0e9ffee2c88a135b2a129d9906b244c85657ac0200fb6a6`). Both sha256 values equal the routing's [C].
  The rest of the untracked root is 26 paths: five SVGs, `ADDENDUM-g3-b2r.md`, `ADDENDUM-g3-b2r-v1.1.md`,
  `ADDENDUM-k1.md`, six `HANDOFF-*-design.md`, `PREPRINT-v1_1-draft.md`, four `RESEARCH-NOTE-v0_*-draft.md`, six
  `archive/PREPRINT-v1_0-draft.pre-patch-v*.md` and `tvc2_dump.txt` (28 untracked paths in all [C]). They were
  untracked when this session started, the routing does not name them, and they are not touched.
- **No OLMo m-unit artifact exists at `18c32df`** [C]:
  - RESULTS.md has no `BACKEND — characterization` entry after 2026-10-05; no headline names one. The word "BACKEND"
    appears in a headline only in 2026-08-19's `CUDA determinism + kernel-path characterization COMPLETE (rule 2).
    THE BACKEND OF RECORD.` (RESULTS.md@18c32df:17228–17229).
  - The last box work on record is the B phase of 2026-08-24/25: B3, B2, the cached-generation gate and B2-r, with the
    respawn gates re-run at each pod restart (`results/raw/2026-08-24_bphase_respawn.txt`, `2026-08-25_b2r_arc.txt`).
    No box entry or box raw exists after 2026-08-25. Every later mention of a pod is a line saying that a pod start
    needs the PI's go.
  - There is no `G-CAL-OLMo-{ckpt}`, `LOCK-m-OLMo-{ckpt}`, `G-TIME-OLMo`, `G-F0m-OLMo` or OLMo-campaign entry. The
    LOCK files at root are `LOCK-g.md`, `LOCK-h.md` and `LOCK-m-F0.md`.
  - `data/m/ckpt/` holds `G-CAL_qwen.json` and `Q-F0_{campaign,id,qual,time}.json`, and no OLMo checkpoint.
    `data/m/reports/` holds Q-F0 reports only.
  - `data/m/schedules/` holds 18 OLMo schedule files: three units × {campaign, qual, time} × {A0, A0s}. They are
    the step-4 build's (`5f7b968`). With no OLMo checkpoint or report on disk, no schedule prefix has been consumed.
  - All 52 raws dated after 2026-10-19 have "note" in their names. One, of 2026-10-22, is the research note's N2(vii)
    item; the other 51, of 2026-10-27 through 2026-11-05, are the release block's. None is a box raw or an m-unit raw.
- **Nothing of Q-F3 exists beyond the shared modules (m:54)** [C]:
  - `valence_core/m/keys.py:66–67` refuses Q-F3 keys:
    `NotImplementedError("Q-F3 keys are built at step 19 (decision (10)); not at step 4")`.
  - `resume.py:385` and `:1158` map Q-F3 to `NotImplementedError`.
  - `audit.py:87–90` defers Q-F3's reasoning-line counter to step 19.
  - The package docstring, `__init__.py:7`, says nothing of Q-F3 is built before step 19.
  - No F3 runner, F3 verifier or reasoning-line class exists.
- **No pod start is on record since 2026-08-25:** no box raw or entry exists after that date. The runpod MCP server
  is unauthenticated in this session, so Code could not read the account's pod history.

## 2. Step 2 — the referents of §5 and the quoted figures

✓ = resolves as the addendum uses it; (Nk) = resolves, with the minor note Nk of §3.

**PROPOSAL-m v1.11 at root.** Its sha256 matches in full (372 lines, tracked, committed at `05c4636`; the commit
entry is at RESULTS.md@18c32df:5495 ✓).

- **§0, m:6–58:**
  - m:6, the dating convention ✓.
  - m:16, decision (10): "Q-F3's track begins only after the v1 posting (§8 step 19)" ✓ verbatim (bold aside).
  - m:16, decision (11): D1 = D_O = 2026-10-30, D2 = 2026-12-22, "D2 one week from v1.8's 12-15 to keep its distance
    from the v1 posting" ✓.
  - m:16, decision (13): "missing the Q-F3 date just caps v2 at Fallback-1 if A0 passed" ✓; the same words are at
    RESULTS.md@18c32df:5657 ✓.
  - m:16, decision (14): the base unit may be reopened, "≈ 1.2–2.0 h over §2.4's table [S]" ✓.
  - m:16, decision (7′): "told controls at SFT, DPO and instruct" ✓. §1.5's reason for (7′), "no instruction-following
    at base", is the one (7′)'s own record gives: archive `PROPOSAL-m-gating-campaign-v1_6.md`, "base has no control
    (no instruction-following)". v1.11's decision (14) restates the exclusion "as a decision, not as a measured fact
    (STOP-4 C13)".
  - m:48, the welfare text, untouched ✓.
  - m:54: "the F3 runner, its verifier and the reasoning-line classes are built at step 19; nothing of Q-F3 is built
    before then except the shared modules" ✓ verbatim.
  - m:58, the preprint of record placed before LOCK-m-F0 v1.0 ✓.
- **§2, m:159–271:**
  - m:159 carries every key and schedule §1.2 lists ✓: `m-olmo-items|{ckpt}|{s}`, `m-olmo-items-time|{ckpt}|{s}`,
    `m-olmo-items-qual|{ckpt}|{s}`, `m-olmo|{ckpt}|{arm}|{s}`, `m-olmo-time|{ckpt}|{arm}|{s}`,
    `m-olmo-qual|{ckpt}|{template}|{s}`, `m-sched|{unit}|{arm}|{b}` over the three OLMo units, and
    `m-sched|{unit}|{gate}|{template}|0`. The arm names `A0-OLMo-{ckpt}` and `A0s-OLMo-{ckpt}` are there too ✓.
  - m:174, the F0m-OLMo format ✓.
  - m:176, the dose and G-CAL-OLMo: condition (4), 128 generations per checkpoint ✓.
  - m:183, floors 80/32, control α .01 / sham, balance unit 32 ✓.
  - m:205–214 ✓, the hours per checkpoint (instruct / SFT, DPO): 1.0 / 1.2 h at 160 launches, 1.2 / 1.4 h at 192, and
    1.4 / 1.6 h at 224. The three checkpoints together take "≈ 3.4/3.9/4.5 h" at 160/192/224. The table is computed on
    each checkpoint's total plus its 26 gate-stage sessions (24 qualification, 2 timing). Its basis amortizes one model
    load, against a 130–200 s cold pod load. G-CAL-OLMo's 128 generations and the pod's idle time at gates are not in
    it. §1.4's "1.0–1.4 h … at 160/192 launches" ✓ (N1, N9).
  - m:249: "the OLMo caps are per-checkpoint shares of a pod budget the PI sets" ✓ verbatim.
  - m:251, pod sessions, with the respawn protocol and a `BACKEND` entry for each box ✓.
  - m:253–258, the banner lines; the OLMo units use five of the six ✓.
  - m:262, the OLMo audit, session end and scaffold set ✓.
  - m:267, the resume identity with the pod instance id ✓.
  - m:271, contrast picks go to the checkpoint file ✓.
- **§3, m:288–302:**
  - m:288: "3.2 Q-F3 (step 19; begins after the v1 posting)" ✓ verbatim.
  - m:290–298, G-SHAPE-F3 through LOCK-m-F3 v1.0 with D2 ✓: G-ANL-F3's 519,480 tuples are at m:291,
    LOCK-m-F3 v0.1 naming the analyzer's hash is at m:292, G-TIME-F3 runs 6 sessions and G-F3 runs 40.
  - m:302, the OLMo lock chain ✓, with "preprint of record pending" and "the Clock governs locking, not respawning".
    §4 step 4's chain matches it node for node. §4 step 4 also names `— secondary DVs`, which m:358 step 17 names ✓.
- **§4–§5, m:306–330:**
  - m:306–316, the DVs and counters ✓.
  - m:318, the blinding rule, including that a decision about one unit taken after another unit's VERDICTS exist is
    recorded as such ✓.
  - m:324: "its LOCK v1.0 is not committed by its Clock date (no box; …)" ✓ verbatim; PENDING is evaluated "at a
    posting" ✓.
  - m:326 and m:330 ✓.
- **§7, m:336–349:**
  - m:336, Steps 1, 2, 5 and 7 at v1 ✓.
  - m:338 ✓: Step 2's OLMo row label with "was not run: reason"; the abstract's clause when none pass; the base label
    "told control not run at base, by decision (7′)".
  - m:341, the title ladder ✓.
  - m:343: §8.1's outcome list "PASS / DEAD / REVERSE / INDETERMINATE / not run / pending" ✓, and §8.2's "state
    whether its cells ran" ✓ (N2).
  - m:345, the welfare text, untouched ✓.
  - m:347 ✓ verbatim: "A checkpoint not locked by D_O is NOT-RUN; its row and the abstract clause change, not the
    title." and "Once in Code's step-3 commit, moving any date is a visible re-specification of the schedule, which
    is what the Clock exists to prevent".
  - m:349, the posting rule ✓.
- **§8, m:356–363:**
  - m:356, the step-3 marks ✓.
  - m:358 ✓: step 16's OLMo-track line "the PI's go for a pod start is required; runpod MCP re-authorisation first";
    step 17's "a unit that reaches NOT-RUN after any gate-stage session ran" (verbatim); step 18's `POSTING v1`.
  - m:361: "19. Begins only after the `POSTING v1` entry exists (decision (10); no Q-F3 session, gate or build beyond
    the shared modules before it)" ✓ verbatim (bold aside).
  - m:363, the list of entries ✓.

**RESULTS.md@18c32df.**

- :24–405 is the Q-F0 VERDICTS entry ✓: its headline is at :24, :404 is its last text line and the next entry starts
  at :406.
- :72–73, the three PENDING declarations ✓, with "D_O 2026-10-30 inclusive to 23:59:59 UTC, C7".
- :85–89 and :88, the CLI-path reading ✓, "flagged for the next hash-moving round of the analyzer (before step 19,
  where C7 defers G-ANL-F3's versioning)". The quotation runs over :88–:89.
- :380 ✓: the OLMo-track line, verbatim at :380–381 (N3).
- :811, LOCK-m-F0 v1.0 COMMITTED, 2026-10-16 ✓.
- :819, "the Clock is UTC by R1 C7" ✓; :817–818 give the committer date in UTC.
- :5495, PROPOSAL-m v1.11 COMMITTED ✓.
- :5657, decision (13) in the PI's words ✓.
- :13048–13063, the GPU watch ✓: A100-SXM4-80GB (AMPERE_80) stock is listed in US-KS-2, US-MD-1, US-MO-1 and
  US-WA-1, and US-CA-2 is absent; the volume `o73qvy742n` is region-locked to US-CA-2.

**Files.**

- `data/m/verdicts/Q-F0_olmo-states.json` ✓: schema `m-olmo-states-v1`; OLMo-sft, OLMo-dpo and OLMo-instruct are
  each `PENDING` / `unlocked-before-D_O` / `clock_passed` false / `date` 2026-10-19.
- `scripts/m_analyze.py` at `18c32df` has sha256
  `655e0f7f6743d0bf497f5ba97ce37f7febf9fcf6a45e068b5385ee945c5dc16f`, equal to the working tree's ✓.
  - :98 ✓: `CLOCK_DATE = "2026-10-30"          # D1 = D_O (m:16 (11)); verified against the proposal`.
  - :384 ✓: `"clock:no-box": {"cite": "m:324 (no box; ...)", "units": "olmo", …}`.
  - :392: `"clock:not-locked"` (N4).
  - :494–526 ✓: `PENDING_SUBSTATES` (:494) and `pending_state`, whose refusal of `unlocked-before-D_O` with
    `clock_passed` true is at :525.
- `valence_core/m/runner_olmo.py` exists; it was built at `5f7b968` ✓.
- `data/olmo/manifest.json` has four entries (base, sft, dpo, instruct) ✓. The respawn protocol re-hashes all four;
  m runs three of them.

**The four sha256 values, Code's reading.** §4 step 2's "the four sha256 prefixes" are read as four quotations of
two distinct values. PROPOSAL-m's sha256 appears in full at :4 and as `42ab36ec…6c6b` at :67; the analyzer's
appears as `655e0f7f…c16f` at :4 and :67. All four match [C]. The other hex strings, `18c32df` and `7631f8a`, are git
commits, and both resolve.

**Berg & Kaiser (§0.4, §1.5, §5).**

- **The source.** A clone of github.com/camberg23/act-on-valence at commit
  `7631f8a06cdeffaf8b7a89212e5ccbe55a657732` (tree `d6f1d50525874355d1ea992f8f652358742ae282`). Its LICENSE is CC
  BY 4.0. It was cloned into Code's scratch directory and read as data; nothing in it was executed.
- **figure4.csv.** sha256 `c8f8dbe831ad18bb6709c609f00d97c4c9ebc9d331cb3dbe5e4640425509e638` [C]. Every row has arm
  `fixed`, N = 80 per stage:

  | stage | hidden-state | text |
  |---|---|---|
  | base | 0.036585 [0.015345, 0.057939] | 0.037622 |
  | SFT | 0.296887 | 0.514807 |
  | DPO | 0.978440 [0.781640, 1.173429] | 1.026566 |
  | instruct | 0.947189 | 0.972814 |

- §1.5's "0.037 [0.015, 0.058] against 0.978 at DPO" ✓, and §5's "0.0366 [0.0153, 0.0579] … 0.978 [0.782, 1.173],
  N = 80 per stage" ✓.
- §0.4's "both of their channels on OLMo-2-32B small at base, rising at SFT and near final at DPO" ✓, against these
  rows and the Fig. 4 caption: "both channels are small in the Base model, increase after supervised fine-tuning, and
  are close to their final magnitudes after DPO". The caption was read in
  `/Users/jasondwyer/Documents/Sentieum Lab/Berg_Kaiser_2026_2609.35591v2.pdf` (sha256
  `e92c69cb4ca2e6e13843dbbf98e30828941890163594ed8ffd0dfc8b5a82fa49`, 38 pages), with the text extracted by macOS
  PDFKit (N5).
- `figure3.csv` (sha256 `f63db30d742f7228336cc0a163107ad157a8924de9455b7478663e7d6a3790fe`), panel
  `steered_minus_clean_margin`, model `olmo_32b`, N = 160 ✓.
- The arXiv API gives v1 published 2026-09-28 and v2 updated 2026-10-04 ✓.

## 3. Grading, and the dated notes

**Nothing in the addendum is substantive under Code's grading; the seat may regrade.** The eleven minor residues are
carried as dated notes under the routing's line "minor residues as dated notes (the e9b5022 precedent)". N9–N11 were
added after the values-check (`results/raw/2026-11-06_m1-v0_1_entry_valuescheck.md`):

- **N1.** §0.4 places "≈ 1.0–1.4 h of campaign generation per checkpoint" beside "three checkpoints ≈ 3.4–4.5 h at
  160/192/224". At 224 launches one checkpoint takes 1.4 h (instruct) to 1.6 h (SFT, DPO) (m:211). §1.4 states the
  1.0–1.4 h range at 160/192 launches, which is exact.
- **N2.** §2.4 (a) quotes m:343 as 'open at v1 by construction'. m:343 reads `"open" at v1 by construction`.
- **N3.** §0.1 says the VERDICTS entry "closed with" :380's line. :380–381 is the second of three "What follows" items:
  :382–383 (the m:318 line) follows it, and the reads' close (:384–404) follows that. :382–383 already records that
  a decision about an OLMo unit taken now is taken with Q-F0's outcome known (N6).
- **N4.** §5 lists m_analyze.py:392 (`clock:not-locked`, m:347's cause), but the body does not cite it. §0.2's cause
  is `clock:no-box` (:384), which is the analyzer's word for m:324's "no box".
- **N5.** §0.4's "a published comparison":
  - BK's Fig. 4 covers the OLMo-2-0325-32B lineage (Base, SFT, DPO, Instruct) in their generation design. The Instruct
    checkpoint generated the conditioning text under steering, and each checkpoint then re-processed it with the
    vector built on Instruct (Fig. 4 caption; BK §4.3).
  - m's OLMo units run the OLMo-3.1-32B lineage (CLAUDE.md, Phase 2) in m's own apparatus.
  - So the comparison crosses both a model generation and a design.
- **N6.** §0.3's "made with every outcome unknown" means every OLMo arm's outcome. Q-F0's A0 PASS (2026-10-19) was
  known when (16) was routed. So (16) is a decision about the OLMo units taken after another unit's VERDICTS exist,
  which is m:318's case and the case RESULTS.md@18c32df:382–383 names. §4 step 4 records any such decision in each
  OLMo unit's VERDICTS entry; the commit entry names (16) as one.
- **N7.** §0.1 cites "the entries and raws of 2026-10-27 through 2026-11-05". RESULTS.md carries no entry after
  2026-10-19. The release block's records are its raws (51 of them, 2026-10-27 through 2026-11-05) and
  `AUDIT-note-release-v1_2.md`. The one other raw after 2026-10-19 (2026-10-22) is the note's N2(vii) item.
- **N8, for G-ANL-F3 (§2.5).** `data/m/verdicts/Q-F0_VERDICTS.json` embeds the three OLMo declarations with substate
  `unlocked-before-D_O`, `clock_passed` false and their comparison date 2026-10-19. It holds no Clock date: 2026-10-30
  does not appear. If item (2)'s reading renames that substate or adds a Clock field to this output, item (3)'s
  byte-for-byte regression from the 2026-10-19 inputs holds only if the D_O-era output is left as it was. This is a
  note for the round, not a change.
- **N9.** §1.4 adds "the 26 gate-stage sessions", and §0.4 "the gate stages", on top of the 1.0–1.4 h per checkpoint.
  m:205's hours already include those 26 sessions: the table is computed on (total + 26) sessions per checkpoint, e.g.
  (160 + 26) × 19.5 s = 1.008 h at instruct and (192 + 26) × 22.7 s = 1.375 h at SFT/DPO [C]. They are therefore
  counted twice, 0.141 h per checkpoint at instruct and 0.164 h at SFT/DPO [C]. This is a planning value; G-PWR and
  the PI's cap shares govern.
- **N10.** §1.3, §1.4 and §3 item 5 call PROPOSAL-n's pod unit "N1". PROPOSAL-n's unit of record on the pod is the
  N-pod (N1 + N2 + N4, its §2.1–§2.5), and the routing's pod-order line names the N-pod.
- **N11.** §5 lists "Project memory / threads cited for the PI's decisions of 2026-10-28, 2026-10-29 and 2026-11-03
  (§2.2)". These are outside the repository, and Code's local memory holds no record of the preprint decisions §2.2
  describes, so Code did not check them. §5 itself calls them "records in the PI's words, not design inputs", and the
  routing is the record of (10′).
