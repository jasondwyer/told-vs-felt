# Code → design seat: three items before LOCK-m-F0 v0.1 (PROPOSAL-m v1.11 §8 step 9), round 2

Code, 2026-10-10 (first stamp 2026-10-10 19:41:31 UTC, `date -u`; revised after its three values-check passes
and Code's later follow-ups, last at 2026-10-10 20:47:04 UTC). For the PI to route. It follows the seat's rulings of 2026-10-10
(`results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1.md`).

## Where things stand

- **G-CAL is closed** on section A, at `8402174`.
- **The one ordered edit is done.**
  - D2 and C9(ii) were built at `b8aa706`.
  - Code's three text-only follow-ups are `185deb0`, `97d70bd` and `b7737ef` (item 2 says why). The last came
    from a read-only sweep of the seat citations in the two files. The sweep did not reach every such text;
    item 2 lists those left.
  - That sweep also found a stale text. The `campaign_look` PIN said "flagged for the seat" on campaign-look
    withholding, but that question was build flag (d), accepted as built in the dispositions of 2026-10-06
    (`54e41c9`). The PIN now says so.
  - G-ANL-F0 was re-run on `b7737ef`: PASS 384/384, manifest sha256 `05132089…fe9b`.
    - The earlier manifest was moved by `git mv` to `G-ANL-F0.superseded-2026-10-10.json`.
    - Three earlier re-runs (on `b8aa706`, `185deb0` and `97d70bd`) were set aside uncommitted and are
      disclosed in the entry.
  - D3's comparison, run at `b7737ef`, holds 10/10: the `valence_core` diff since G-SHAPE-F0's build is
    `stages.py` alone, and the sources and tooling maps are unchanged. D3 compares with the lock's tree, so it
    is made again at the lock's commit.
  - Everything is in the D2 round's RESULTS entry, committed with this block.
- **Code has not started LOCK v0.1.** It waits on the PI's word.
- **The three items.**
  - Each says what Code does without an answer.
  - The rulings ordered two things first: G-CAL's close, and the D2 round with its re-run. Both are done. D3's
    comparison is made again at the lock's commit ("any other difference re-runs G-SHAPE-F0 first").
  - Beyond those, the rulings set no precondition for LOCK v0.1 but the PI's word ("LOCK v0.1 is then Code's to
    draft and commit on the PI's word"). By Code's default, none of the three items holds the lock unless the
    seat says so.
  - C6 says LOCK v0.1 "does not wait on any reading the seat has not struck". Item 2 was built at `b8aa706`,
    after C6 was written. Whether C6 reaches it is the seat's to say.
  - Item 1 has not been acted on. Item 2 is Code's and already in the code: the pause is Code's application of
    m:330, and the route is Code's reading of C3. Any acceptance of it would be post hoc.
- **If an answer goes against a default after the lock**, it moves a hash the lock names. Every non-stub stage
  then refuses at its start until a lock revision names the new one: under D2's check if the package moves,
  and under Code's half of that check if the analyzer moves (finding R8, after the analyzer's PIN-14).
- **If the answers come at step 10's ping**, where the rulings place the seat's read of the lock, G-TIME-F0's
  sessions will already have run under LOCK v0.1's hashes. Whether they stand after a lock revision that moves
  a hash is the seat's to say. The PI may hold the lock, or step 10, for the answers.

## 1. B2's and B3's "register" (G-SHAPE-F0)

- B2 ends: "State that in the artifact's register".
- B3 says that each placement is scored as a first round, so history-dependent classes are not exercised, and
  calls this "a known limit, stated in the register".

The G-SHAPE-F0 artifact (`data/m/gates/G-SHAPE-F0.json`) is write-once and carries no PIN register.
PIN-S1–S10 are declarations in `gshape.py` (comments, and PIN-S9's in a docstring), each "declared at LOCK
v0.1".

- **Code's reading:** "the artifact's register" and "the register" are LOCK v0.1's G-SHAPE-F0 register
  (PIN-S1–S10 as the lock declares them). The lock would state there:
  - B2's sentence, verbatim: "Layers S and C are Code's additions beyond m:277's letter; a future failure of
    either is a build defect that STOPs the gate for repair, not an m:277 finding that re-specifies anything."
  - B3's limit.

  On this reading `gshape.py` is not edited and G-SHAPE-F0 does not re-run.
- **The other reading** puts the statements in `gshape.py`'s own texts, which feed the artifact.
  - `gshape.py` is a G-SHAPE-F0 tooling file, so under D3 G-SHAPE-F0 would re-run and its artifact would be
    superseded by hand `git mv` (PIN-S9).
  - The package would also move again. Whether G-ANL-F0 then re-runs, or the lock states the `gshape.py` diff
    against G-ANL-F0's manifest as D1 does for the earlier packages, would be the seat's to say. Nothing in
    G-ANL-F0's battery imports `gshape`.
- **Without an answer:** Code drafts LOCK v0.1 on its reading, stating both in the lock's G-SHAPE-F0 register
  and marking the placement as Code's reading.
- **If the seat takes the other reading after LOCK v0.1:** `gshape.py` is edited, G-SHAPE-F0 re-runs and its
  artifact is superseded, and the package moves away from the one the lock names. So every non-stub stage
  refuses (D2) until a lock revision names the new package. Whether G-ANL-F0 then re-runs is the seat's to say,
  as before the lock; the revision states it.

## 2. A pause at a campaign STOP, and its route through `--adjudication` (Code's, already built)

- **What C9(ii) orders.** Its words order that the bars' counts be "evaluated and recorded at the STOP point
  as the campaign's last look, and the verdict sentence names that look". They say nothing about a pause.
- **What Code built at `b8aa706`.**
  - That end look raises a pause if it fired and none was raised for it already:
    - kind `end_look` for an end look evaluated at the STOP;
    - kind `look` for a cadence look the hair trigger pre-empted.
  - After a G-VER STOP on a multiple of 40, the reused cadence look raises no new pause: it was announced at
    its own launch, and any pause it raised was adjudicated before the next launch.
  - The pause is Code's application of m:330's "A fired bar pauses". So is reusing the cadence look as the end
    look when the launches recorded at the STOP are a multiple of 40 (a G-VER STOP's quarantined record not
    counted).
- **The route.** `stages` never resumes a stopped campaign, so that pause can be adjudicated only through
  VERDICTS' `--adjudication` file.
  - C9(i) names that file for "a fired end look on a terminal campaign".
  - C3 names it for the campaign's unadjudicated last pause.
  - Code reads C3 as covering a STOP's pause, because that pause is the last one.
- **Code has acted on this.**
  - VERDICTS takes a STOP's pause only through `--adjudication`, and a hair-trigger STOP also needs PIN-8's
    PI-stop record.
  - The battery of G-ANL-F0's re-run of record exercises both STOP cases.
  - That re-run (`05132089…fe9b`) was taken on this build as amended by the three text-only follow-ups.
- **Code also built, unordered, a V2 refusal.** VERDICTS refuses a STOP-ended campaign with a launch recorded
  and no end look ("not written by the lock's package"). Like (b) and (c) under item 3, it guards checkpoint
  structure; unlike them, it is built. Without an answer it stands as built, declared under PIN-10 at LOCK
  v0.1. If the seat strikes it, the analyzer moves, with item 3's consequences.
- **The texts.** At `b8aa706`, several texts credited the pause or its route to the seat, among them:
  - PIN-9 (its register entry and its inline comment), which had "terminal (or stopped)" under C9(i);
  - PIN-10's register text ("A fired end look at a STOP is a pause and takes PIN-9's path", under "The
    seat's C9(ii)");
  - four `stages.py` texts: two comments, the re-finish refusal message's citation and one self-test label;
  - the commit message's C9(ii) paragraph, which lists the pause and the reuse under C9(ii), and its route
    sentence, "A fired end look at a STOP takes PIN-9's --adjudication path (C9(i))".
- **The follow-ups** mark every code text in that list as Code's reading of C3, or as Code's application of
  m:330.
  - `185deb0` marks PIN-9 and three of the `stages.py` texts as Code's reading. It also narrowed the refusal
    message's C9(i) to a terminal campaign, leaving "the seat's C3" for a STOP.
  - `97d70bd` marks the refusal message and PIN-10. Its commit message corrects a count of "three" texts in
    `185deb0`; that correction holds only for `185deb0`'s site-check header, and the entry says why.
  - `b7737ef` covers the remaining texts the sweep found, among them the `_campaign_events` docstring and the
    terminal branch's PINs.
    - It also marks the pause itself as Code's application of m:330 in three texts whose route the earlier
      follow-ups had marked: PIN-9 (register and inline), PIN-10's register text and the `_stop_end_look` PIN.
    - It re-prefixes ten C9(ii) self-test labels "C9(ii) as built (Code's applications included)".
  - Git history is not rewritten. The entry corrects `b8aa706`'s route sentence. `b7737ef`'s message states
    the pause and the reuse as Code's applications, which `b8aa706`'s C9(ii) paragraph had listed under C9(ii).
- **Left at `b7737ef`, flagged and not changed.** The sweep did not reach every text of its kind. Changing any
  of them moves the analyzer or the package and re-runs G-ANL-F0. Among those left:
  - in the analyzer:
    - the V2 refusal's message ("(the seat's C9(ii))");
    - PIN-10's register text and both its inline PINs (`guard_at_last_look`, `run_verdicts`), which state
      the V2 refusal and the end-look reuse under "The seat's C9(ii)" unmarked; `b7737ef`'s message calls
      both Code's;
  - in `stages.py`:
    - the `_stop_end_look` PIN's header, which cites C9(ii) over the reuse and the pre-empted look's pause;
    - the `_stop_lines` PIN, headed C9(ii), over stdout ordering;
    - the inline PIN in `licence_problems` and the LICENCE-line PIN, headed "the seat's D2", over checks
      (d)–(f) together;
    - one self-test comment and one label that put the analyzer half under D2.

  Whether to amend them before the lock is the seat's, or the PI's, to say. Code proposes making any such
  change in the same round as whatever the seat's answers require, so that the hashes move once. Without an
  answer they stand, and this block and the entry record the attribution.
- **Other attribution fixes in the follow-ups.**
  - `185deb0` rewords PIN-6's "confirmed by the seat (C7, 2026-10-10)" and PIN-12's "Confirmed by the seat
    (C7, 2026-10-10; G-PORT A5)" to "settled". It adds to PIN-12 that the interim text had named
    `sessions_excluded_any_phase` the like-for-like column. `97d70bd` makes one battery comment say "settled"
    too.
  - `b7737ef` marks the analyzer half of the stage-start check as Code's: finding R8, after the analyzer's
    PIN-14. D2 orders both keys required, and the package hash checked against the lock.
- **Without an answer:** the pause and the route stand as built, and PIN-9, PIN-10 and the `stages.py` PINs are
  declared at LOCK v0.1 as they are, the reading flagged.
- **If the seat strikes it before the lock:** the analyzer changes (PIN-9, PIN-10, and VERDICTS' acceptance of
  the file for a STOP's pause).
  - `stages.py` changes too, whatever the seat names instead. Its texts giving the route for a STOP's pause
    change in every case: among them the `_stop_end_look` and `_refinish_campaign` PINs, the re-finish refusal
    message and self-test labels.
  - Its logic changes as well if the seat names no pause at a STOP, or a route through `stages`.
  - So the package moves either way. G-ANL-F0 would re-run and its manifest be superseded. G-SHAPE-F0 would not
    re-run, because neither file is in its maps (D3).
- **If it strikes it after LOCK v0.1:** the same edits move the hashes the lock names (the analyzer's always,
  the package's too). Every non-stub stage then refuses until a lock revision names the new ones: under Code's
  analyzer half of the check for the analyzer, and under D2's check for the package. C6 makes each entry of
  the 43-entry register strikable until LOCK v1.0; whether that reaches this reading is the seat's to say, as
  above.

## 3. Three analyzer edits the seat did not order: whether, and when

Each is an `m_analyze.py` edit. Either way it moves the analyzer sha256, re-runs G-ANL-F0 and supersedes its
manifest:

- made before LOCK v0.1, that happens to `05132089…fe9b` now;
- made after, the analyzer no longer hashes to the sha the lock names, so every non-stub stage refuses until a
  lock revision names the new one (under the analyzer half of the stage-start check, which is Code's: finding
  R8, after the analyzer's PIN-14; D2 orders the key required);
- made after LOCK-m-F0 v1.0 (step 15), the edited analyzer is not the analyzer of record, which PIN-14 keeps as
  "the blob hashed in that unit's LOCK v1.0". VERDICTS would run that blob from a worktree of the lock commit
  (on the PI's word; not implemented at step 8). So an edit to VERDICTS' own checks ((b), (c)) would not reach
  VERDICTS unless a revision of LOCK v1.0 hashes the new analyzer.

**(a) C7's posting bar.**

- **What already matches the bar.**
  - The `posting` command computes the analyzer's §7.5 enumeration under (a), (b) and (c) (m:349), the one
    C7's bar names, and lists any residue by row id and location.
  - The builder and the spec-and-binding lens found that an empty enumeration is exactly C7's condition, the
    dose note's presence iff the flag included, since (c) is two-sided (PIN-21) and `table_problems` requires
    an f1-corr-line row.
- **What does not.**
  - The command renders no PASS/FAIL against the bar: it exits 0 and prints "N enumerated rows" whatever the
    residue.
  - Its (a)/(b) result rests on the posted table's declared `null_cells` and `thesis` classification, not on a
    reading of the posted text.
  - Nothing compares the re-run with "the VERDICTS one with the PI's rewrites applied".
- **What C7 orders.** It fixes the bar now ("Fixed here, before the v1 posting") and orders no analyzer change.
  Its words for the posting: "any residue is listed by sentence and rewritten before posting".

**(b) A fired end look without a matching pause.** VERDICTS does not check that a fired end look is matched by
a pause. It would accept a hand-edited checkpoint that breaks this, and that checkpoint would then be analyzed
without the seat's adjudication (C3).

**(c) The end look's launch count.** VERDICTS does not check that `end_look.at_launches` equals the launches
recorded at the STOP.

`stages` keeps both invariants, (b) and (c), in every checkpoint it writes. Both candidates are recorded in the
D2 build's review raw (`results/raw/2026-10-10_m-d2-c9-build_review.txt`):

- (b) was the campaign-state lens's optional fix; the fixer left it to Code, and both verifiers carried it.
- (c) was raised by a refuter in the blinding-and-tests lens, and the closing round's verifier carried it.

**Without an answer:** Code builds none of the three. Whether and when each is built is the seat's to say.
Until (a) is built:

- at the posting, each row the command lists as residue is rewritten before posting, as C7 orders for
  residue ("any residue is listed by sentence and rewritten before posting");
- the command's "N enumerated rows" is not itself C7's PASS, because the two gaps above stay open: the posted
  text is read only through its declared classification, and nothing compares the re-run with the VERDICTS
  enumeration with the PI's rewrites applied;
- how the gaps are met at the posting without (a) is the seat's to say.

## Not an item: note 126 (withholding at campaign looks)

- Step-3 note 126 (`results/raw/2026-10-06_m-v1.11_step3_notes.md`) says the weak pick channel §3 closes at
  gate stages stays open at campaign looks. It proposes two fixes:
  - report the contrast arms' forced-round counts only at looks;
  - or move the contrast-arm figure to VERDICTS.
- The step-4 build put the same question to the seat as flag (d), and the seat accepted (d) as built
  (`54e41c9`).
- As built, a campaign look reports for the contrast arm:
  - its launches, its domain count and its pooled pre-pick (forced-phase) exclusion count;
  - the Fisher guard (against the sham arm's count) and the absolute guard, both evaluated on that count;
  - the read flags of first reads of domain sessions;
  - forced-round degeneracy (k, n).

  The arm's free-round events stay withheld.
- Code reads note 126's question as (d)'s, and (d)'s acceptance as covering the note. That identification is
  Code's; the dispositions do not mention the note. Code does nothing more unless the seat says otherwise.
