"""PROPOSAL-n -- the read runner's record schema (n v0.2 §8 step 6; first committed at `5a97527`).

The seat's answers of 2026-11-15 (``results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md``),
§5.1: "**n-build**, n §8 step 6 (the package), whose first commit is the read runner's record schema;
**n-analyzer**, step 9's `n_analyze.py` and its battery (385 tuples), built from that schema." This module is that
schema: every field the read runner, its stages and G-READ-n write, its type, when it is null, and the checks both
sides run -- the writer before every write, the analyzer on every load. A change to it is a commit of this file with
its reason.

It imports the standard library only (the package's parent imports numpy). It reads no file, touches no model and
writes nothing; ``python -m valence_core.n.schema`` runs its self-test on literal records.

WHAT A RECORD IS (Code's reading of n §2.4, "each read counted once"). One record per read of §2.4's table: one
(arm, direction, dose point, session). The fidelity re-computation (§2.1) and the d = 0 identity check ride inside
that record and are never records of their own. Records are written by three stages: ``campaign`` (§2.4's arms,
§8 step 14), ``time`` (G-TIME-n's timed reads, §3) and ``backend-ext`` (the BACKEND extension's fresh-versus-cached
reads, §3 G-ACQ; G-ACQ's dated note GA-5). G-CAL-n's generations, G-VEC's captures and G-VER's reconstructions are
other records, not specified here; the stage report and G-READ-n's artifact are specified below. A NOT-RUN on the
clock is a record in the analyzer's own schema (n-analyzer's `n-not-run-v1`); a NOT-RUN for no arm complete is derived
from a report's end state and completeness.

THE TWO PATHS (Code's construction, accepted: the seat's answers of 2026-11-16, second sitting,
``results/raw/2026-11-16_n-build_design-to-code_answers.md``, §3; LOCK-n v0.1 pins it). BK's
``prereg.precondition_cache`` (``data/n/bk/.../neutral_passages/analysis.json``) states the check n §2.1 adopts: "the
prefill-plus-cached-continuation margin against a fresh full forward over the identical ids under the identical
additive mask".
  * ``cached`` -- the read of record (BK's ``margin``; n §4's m(c)): one prefill forward over the read sequence
    [0, seq_len) under the read's additive mask, its KV cache kept; then each label's token sequence forwarded
    through that cache as the continuation, with no injection.
  * ``fresh`` -- the re-computation (BK's ``fresh_margin``): for each label, one uncached full forward over the read
    sequence followed by that label's tokens, under the identical mask. At d = 0 it carries no injection, so it is
    also §2.1's "vanilla forward" for the identity check.

THE READ. The read position is ``seq_len - 1``: the last token of the rendered sequence, the generation prompt's
newline after the choice turn (G-DATA (iv)-(v): the last 39 tokens are "the 12th passage's closing `<|endoftext|>`
and newline, the choice turn, and the generation prompt"); its next-token distribution gives the first label
token. Each label's token ids are the renderer of record's (the label convention is pinned in LOCK-n v0.1).
``logprob_S`` and ``logprob_U`` are the sums of the label's per-token full-vocabulary log-softmax values, taken by
``math.fsum`` (Code's choice of summation); ``margin = logprob_S - logprob_U`` (BK eq. 1). Δm is the analyzer's
(the read's margin minus its shadow's); no record stores it. Every forward of a read -- the read sequence and a
label's tokens but the last -- fits the stage's declared ``read_window`` (rule 28(d)(c); G-ACQ's dated note GA-4:
each window at or below 4,096).

THE RESTRICTED READ (n §2.1's secondary, "this program's restricted two-label first-token read (m:172's
`choice_read` form, b3's on OLMo) on the same forward"). Every label of BK's set of 12 begins with the word "Zone",
so the two labels' token sequences may share a prefix (whether they do is the tokenizer's). As the seat ruled (the
seat's answers of 2026-11-16, ``results/raw/2026-11-16_n-build_design-to-code_answers.md``, §2.1; ADDENDUM-n1 §3),
the read is taken at the first label-token position where S's and U's token sequences
differ (offset ``k`` past the read position; for k >= 1 it lies on the cached continuation, the shared prefix
teacher-forced): the two divergent tokens' full-softmax probabilities, renormalized; ``label_mass`` their sum; the
pick is the larger, a tie going to ``present[0]`` (m's ``choice_read`` gives ties to its first label). m's
``choice_read`` also re-forwards the identical text to verify it (KL exactly 0.0); n takes the read on the read's
own forward and does not repeat that re-forward -- §2.1's fidelity re-computation is n's re-forward (the same
ruling).

SPANS AND THE SHADOW (rule 5(f)(i)-(iii); n §2.2; the record's provenance is Code's construction, declared here;
the shadow by reference accepted: the seat's answers of 2026-11-16, §3).
``steered_spans`` lists the half-open token ranges the injection covers, each with its zone: the session record's
``turn_spans`` whose zone is ``cue_S`` (the S whole-turn spans, G-DATA (v); its dated note G-2) for every steered
arm except N1-P, which steers every ``turn_spans`` entry of both zones (§2.4, "same-pole"). ``mask_sha16`` is k's
``mask_sha`` of the int8 mask over [0, seq_len) (+1 / -1 on the steered positions by the injection's sign, 0
elsewhere; all zeros for an unsteered read). The runner asserts before any forward that the mask is zero at the
read position and at every position outside the spans; a record exists only if that held. ``retention_interval`` =
read position - last steered position. ("Cell" in this module names a file grouping.) A read's interval is fixed by
its session's skeleton and its arm's span set: the same at every dose and on every S-span arm; N1-P's ends at the
12th turn (39 tokens on all 160) and differs from the S arms' in the 83 sessions whose 12th turn is U. That a
per-session interval so fixed meets rule 5(f)(iii)'s "held fixed within a cell" is Code's reading, flagged for the
seat. Every steered read names its shadow, the N1-V d = 0 read of the same session ("the 160 at d = 0 are the
shadows for every arm", §2.4), whose ``ids_sha`` equals its own; the runner writes a steered read only after its
shadow's record is on disk. The renderer reproduces BK's ids on all 160, G-DATA's dated note G-1's two recorded
splits (``neu_b1`` run 62, ``neu_b3`` run 113) included; the ids of record carry them (ADDENDUM-n1 §1:
``data/n/ids/``, committed at ``d76f34f``).

CAPTURES (n §2.2: "the residual at the read position captured at layers 32 and the final layer on every
forward", read as a band: ADDENDUM-n1 §6.2; the seat's answers of 2026-11-16, §2.5). From the cached path's prefill,
at the read position: the residual after every decoder layer past the site through the last, 31 or 32 layers,
``capture_layers = list(range(layer + 1, n_layers))`` (olmo_hf's capture index l is the residual after decoder
layer l, 0-based; index n_layers - 1 is before the final norm: G-ACQ's hook-site check). float32, one ``.npy``
array per cell per layer, named by ``capture_filename``, of shape [capacity, d_model] -- ``capture_capacity``: 40
rows for N1-R's cells, 160 for every other -- row r holding the cell's r-th record, written in place, rows from
``capture_rows`` on unwritten (Code's form, for I/O: a row is written once, never the array again). Each record
carries its row and each layer's ``sha16_arr``; the cell file carries, per layer, the sha256 of the written rows
[0, capture_rows) as float32 little-endian bytes in row order (``capture_sha256``). The arrays -- about 4.7–4.8 GB
at 7,360 reads (ADDENDUM-n1 §6.2's figure), about 4.9–5.0 GB at the 7,680 rows -- are kept on the box's volume
during it and copied to the laptop with their hashes before the pod stops, never committed to git; the lock pins
the per-cell hash lists. The fresh path's read-position residuals, from each of its two forwards (label S's and
label U's), are hashed into the fidelity block, not stored. The cached path's continuations hold no read-position
residual of their own (the cache keeps keys and values), so every forward that computes one is captured or hashed,
and every read captures: G-TIME-n's "capture-on" kind is every read.

FIDELITY (n §2.1; G-DATA (vi); the comparison's form is Code's reading, accepted: the seat's answers of 2026-11-16,
§3). ``absdiff = |margin - fresh_margin|``;
``scale = max(|logprob_S|, |logprob_U|)`` of the cached read (the scale identified by reproduction, the step-2
referent check's N1); ``rel = absdiff / scale``; ``exceeds_tau = rel > TAU`` and ``exceeds_tau4 = rel > TAU / 4``
(§4 (f)'s sensitivity row). ``reason`` is ``dose-rule`` -- §2.1: "at d ∈ {0, +1, −1} every read is re-computed",
N4's d = 0 reads included (the step-3 entry's dated note N2); checked here at the campaign and the BACKEND
extension -- or, at any other point, ``sample`` at the campaign (the keyed 10% sample, ``n-fid|{s}``, where s is
BK's run, so the sample is of sessions: Code's reading; the draw is the lock's) and ``timing`` at G-TIME-n (a
re-computation G-TIME-n takes to time it).

IDENTITY (n §2.1: "the d = 0 read is the vanilla forward's margin within the backend's measured nondeterminism ...
the bound stated in LOCK v0.1"). On an unsteered read that carries a re-computation, at the campaign or G-TIME-n
(N4's reads included): ``within`` is the fidelity block's ``absdiff <= bound`` (the comparison's form is Code's
reading). At ``backend-ext``, which measures the bound, the block is null.

N4 (n §2.4). ``told_variant`` "TOLD" (N4-T) or "SHAM" (N4-Ts); ``schedule_zone`` the zone the 80/80 schedule assigns
the session ("S" or "U": the zone the TOLD line names; the referent zone of the sham arm's E, §4); ``told_line`` the
line itself, §2.4's words (that the record carries the line, not its rendered join, is Code's reading, accepted:
the seat's answers of 2026-11-16, §3). §2.4 puts
the line in the choice prompt before "Reply with ONLY…"; the join is fixed (ADDENDUM-n1 §1.2 (ii)): after the
prompt's first sentence, one space on each side. N4's token sequence is its own: ``ids_sha_bk`` is null.

CROSS-RECORD PROPERTIES are not checked here, where one record or one cell is checked: a steered read's shadow exists
with the same ``ids_sha`` (the runner asserts it before the read); ``ids_sha_bk`` equals the session record's (the
runner and G-VER); an N4 read's tokens before ``n_pre`` are its BK session's (the renderer asserts it; G-VER
re-checks); N4-T and N4-Ts carry the same ``schedule_zone`` per session, under the schedule's key, its 80/80 split
and its balance by ``present`` order (the runner and the lock). The analyzer re-checks what it uses.

TYPES. Exact JSON-native values only (m's ``resume._assert_native`` form: no numpy scalars, str dict keys); every
float finite. A non-finite number in a path makes that path's ``finite`` false and its numbers null (§6: NaN/inf
pauses). No record carries a time of day: ``duration_ms`` is the read's wall-clock of model work, both paths, and
``duration_ms_fresh`` the fresh path's share (null without a re-computation), for G-TIME-n's kinds and the cap.

NOT RECORDED: Δm; the free-text reply of n §4 (b) (§2.1: "No new text is generated for N1, N2 or N4"; §4 (b) is
struck: ADDENDUM-n1 §4); BK's welfare probes, which n does not run.

FILES. A stage's checkpoint directory holds one cell file per (arm, direction, dose point), named by
``cell_filename``, beside its capture arrays, one per capture layer, named by ``capture_filename``. A read's rows
are written in place first, each array flushed to disk, then the JSON atomically (m's
``resume.atomic_write_json``), so a JSON on disk never names a row its arrays lack.

THE DOSE MAP (n §2.3: "d_eq = (0.10 · R_ℓ)/(ρ · R) and d_20 = min(1, 2·d_eq) ... a point within 0.05 of an
existing one is merged"). ``check_stage_identity`` requires, exactly, ``rho == 0.3``,
``d_eq == (0.10 * R_ell) / (rho * R)``, ``d_20 == min(1.0, 2.0 * d_eq)`` and ``points == dose_points(d_eq, d_20)``:
the merge rule, settled with n-analyzer so both sides derive the same points, is ``dose_points``' docstring.

THE READ PLAN. ``read_plan(identity)`` is the campaign's declared read set: n §2.4's arms over the stage's dose map,
N1-P at +1, +d_20, +d_eq and -1 (ADDENDUM-n1 §5.2), N1-R on the 40 floor sessions, every other arm on all 160 --
7,680 reads when nothing is merged. §2.3 states the merge for N1-V's points; it reaches N1-R point for point (C12's
floors are per point) and N1-P, and a merged point is read once under the label kept, its ``keeper`` (``arm_cells``;
the seat's answers of 2026-11-16, §2.3; ADDENDUM-n1 §5.1-§5.2). An arm is complete exactly when its obtained
read_ids are its plan's.

THE STAGE REPORT (``n-report-v1``), settled with n-analyzer. Written at the end of every invocation that ends by the
rules below. An invocation that ends otherwise (an exception, a refused write, a kill, a lost box) writes none; the
next one's replay of the records on disk finds what it left (the runner's design). The report holds no margin or
other per-read model output: the identity, counts, states, read ids, launch indices, ms figures and sha256s. It
carries:
  * the stage identity and its sha256 (``identity_sha256``), and the plan's sha256 at the campaign;
  * planned, obtained and complete for every arm of the stage's plan. Obtained counts the records on disk, finite or
    not, so an arm with a non-finite read can be complete; the analyzer treats such a read as unusable (accepted,
    with PIN-n-20's consequence: the seat's answers of 2026-11-16, §3);
  * each cell file's sha256s and record count. Every cell is at a point the stage's dose map keeps for its arm
    (``arm_cells``), and its arm has a per-arm entry;
  * every pause of the stage, in launch order, its id ``p01``, ``p02``, ... by its place in the list. A pause stands
    on the arms in its scope while it is unadjudicated. Its scope holds its read's arm, with no arm twice; which
    other arms it holds, and a read-less fire's scope, are the runner's (its SCOPE pin, flagged; the pause stands on
    its scope's arms, as the seat's answers of 2026-11-16, §3 accept). An adjudicated pause is cleared, whatever the
    ruling, and the report records no ruling's effect on reads. A fired monitor ends the invocation, every arm with
    it, and the resume after the ruling continues all (accepted: the seat's answers of 2026-11-16, §3; n §6 stops
    "the arm's launches"), and the runner
    launches in the stage's run order, so every read after a pause's own was launched after its ruling.
    ``resumed_at_launch_index`` is the first read attempted after the ruling, launched or refused as a rendering
    mismatch. The schema checks that it follows its own pause; that pauses and resumptions interleave as the runner
    launches them is the runner's to keep and the reader's to check. A read that fires two triggers is one pause:
    its ``kind`` by the precedence the seat fixed (the seat's answers of 2026-11-16, §3): rendering, nonfinite,
    identity-bound, fidelity-binomial, and the rest in ``also_fired``. An identity-bound trigger is a d = 0 read's
    (n §6: "the identity bound exceeded at d = 0"). A pause at which the binomial fired, as its kind or in
    ``also_fired``, carries the batch (first <= last, 0 <= k <= n, n > 0, 0 < alpha < 1), which ends at the pause's
    read where it has one;
  * a rendering mismatch during a stage is a pause; G-VER's, before any read, is a G-VER-STOP (accepted: the seat's
    answers of 2026-11-16, §3; n §6 lists "a rendering mismatch" among its pause-and-adjudicate triggers, and n §3
    gives G-VER "mismatch → STOP"). A rendering pause's read is not launched, so nothing else fires with it. It
    names the read's place; after the ruling the read is attempted there, so its ``resumed_at_launch_index`` may
    equal its own launch index and a later pause may share that place. A binomial fire at the run's end has a batch
    and no read: it is the stage's last pause and resumes nothing. A G-VER-STOP comes before any read: its report
    holds no record and no pause;
  * the fidelity binomial's running state over the stage: its trials and exceedances, which are the fidelity
    counters' totals; its evaluations; and its fires, each a pause's batch, whose k and n are within the stage's
    exceedances and trials;
  * the STOP's record, its detail one line of at most 200 characters; the cap, whose ``used_ms`` is the sum of the
    records' ``duration_ms`` (both paths): it counts the reads' and re-computations' model time, with each
    invocation's model load reported beside it in ``loads_ms`` and outside it (the lock's clause as the seat ruled
    it: the seat's answers of 2026-11-16, §3);
  * n §4's counters and the identity-bound count, over the stage. ``rendering_mismatches`` is the number of the
    stage's rendering pauses, or at a G-VER-STOP the number of G-VER's mismatches, at least one; nothing resumes
    after a STOP. ``nonfinite_reads`` and ``identity_out_of_bound`` count at least the pauses that name their kinds.
    ``label_mass_below_floor`` is null where no floor is set.

The end state is one of COMPLETE, PAUSE, PI-STOP, G-VER-STOP, CAP, by these rules (Code's, settled with n-analyzer):
  * PAUSE iff an unadjudicated pause stands and the unit is not stopped, whether or not the cap is hit: the seat
    rules on the pause first. A standing pause otherwise ends only by a ruling, or under PI-STOP: the PI may stop a
    unit whose pause stands;
  * CAP iff the cap is hit, no pause stands and no STOP is recorded, so a stage whose last read reaches the cap ends
    as CAP with its arms complete. A hit cap is otherwise allowed only under PAUSE, PI-STOP or G-VER-STOP;
  * PI-STOP and G-VER-STOP iff the report carries that STOP's record;
  * COMPLETE iff no pause stands, the cap is not hit, no STOP is recorded and, at the campaign, every arm is
    complete.

G-READ-n'S ARTIFACT (``n-gread-v1``), settled with n-analyzer. It carries:
  * the campaign it read: plan, identity and cells, by sha256;
  * the probe's package sha256 and settings: k's ``fit_lr`` hyperparameters, pinned in ``GREAD_LR`` (n §0.10's B3,
    "k's form and bar"; accepted: the seat's answers of 2026-11-16, §3); the CV form, grouped 10-fold CV by session
    ("kfold10", in place of n §3's leave-one-session-out: ADDENDUM-n1 §6.3), and its folds' seed (``cv_seed``, the
    lock's); the shuffles and their seed; the layers and the bar;
  * at least one result, and at most one per (axis, point) of ``GREAD_AXES``: valence +1, +1/2, +d_20, +d_eq;
    span_reward f0.10, f0.20. The -1 reads enter +1's contrast; that the points are the kept ones is the reader's
    check. A result's
    ``merged`` lists the labels merged into its point: on valence only +d_20 and +d_eq, on span_reward none. Each
    result gives the contrast (the - pole at valence +1, else the shadow; n §3), the per-layer AUCs against the
    shuffle null in the probe's layer order, the band median, the comparator's 24 band medians, and PASS, FAIL or
    NOT-COMPUTED. The comparator is the 24 random directions at the point norm-matched to the result's; for
    span_reward's f0.10 and f0.20 that is +d_eq and +d_20, or the points they merged into. The dose map norm-matches
    them where they are kept, and to within the merge distance (0.05 on BK's scale) where they merged; not where
    d_20 is capped at 1 (accepted: the seat's answers of 2026-11-16, §3, with ADDENDUM-n1 §5.3 where the cap
    binds).

The PASS rule is the seat's (ADDENDUM-n1 §6.4; the seat's answers of 2026-11-16, §2.5): the band median is at least
.90 and above the largest of the comparator's 24 band medians (n §3: "above the comparator's band"). There is no
per-layer condition (k §1.4 G3's every-layer clause is not adopted); each layer's ``above_null`` is reported. A
computed result without a comparator is a FAIL; a NOT-COMPUTED one carries neither a comparator nor AUCs.

EXAMPLES. ``example_identity``, ``example_record``, ``example_cell``, ``example_report``, ``example_pause`` and
``example_gread`` build valid objects from literals, for this module's self-test and for the analyzer's battery; no
production path calls them.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from typing import Any, Mapping

RECORD_SCHEMA = "n-read-v1"
CELL_SCHEMA = "n-cell-v1"

UNIT = "N-pod"
STAGES = ("campaign", "time", "backend-ext")

#: PROPOSAL-n v0.2 at root (its COMMITTED entry, 5916097).
PROPOSAL_SHA256 = "30a3d0f55a6681e01245f75490d1f7fdf032b4a1f2c6e59684d6a17584b104f4"
#: BK's 14 skeleton files concatenated in name order (floor_b0-b7, then neu_b0-b5; v0.1's STOP raw §6; the step-2
#: referent-check raw §3).
SESSION_SET_SHA256 = "be50011a5ab1e8a4261dbde72afc84313d3bdeba9e40078272928bd497c3ba84"
#: BK's frozen scale-relative fidelity criterion: ``analysis.json``'s ``tau`` (its ``prereg.precondition_cache``
#: names the criterion and prints it to ten places); G-DATA (vi).
TAU = 0.017883544377937845
TAU4 = TAU / 4
#: n §2.3: rho = 0.30 (BK Table A2); "a point within 0.05 of an existing one is merged".
RHO = 0.3
MERGE_DISTANCE = 0.05
#: G-ACQ's dated note GA-4: every n window at or below OLMo-2's 4,096 positions.
MAX_WINDOW = 4096
#: n §2.1: "at d ∈ {0, +1, −1} every read is re-computed".
DOSE_RULE_LABELS = ("0", "+1", "-1")

BK_CELLS = tuple([f"floor_b{i}" for i in range(8)] + [f"neu_b{i}" for i in range(6)])
N_SESSIONS = 160
N_FLOOR = 40                     # floor_b0-b7, 5 each: BK's runs 0-39
N_RANDOM = 24

ARMS = ("N1-V", "N1-R", "N1-P", "N2-E", "N2-S", "N2-C", "N4-T", "N4-Ts")
RANDOM_IDS = tuple(f"rand_{i:02d}" for i in range(N_RANDOM))
DIRECTION_IDS = ("valence",) + RANDOM_IDS + ("span_reward", "span_sentiment", "span_character", "none")

#: dose label -> (scale, sign, fixed value or None where the lock's dose map gives it).
DOSES = {
    "+1": ("bk", 1, 1.0),
    "+1/2": ("bk", 1, 0.5),
    "+d_20": ("bk", 1, None),
    "+d_eq": ("bk", 1, None),
    "0": ("none", 0, 0.0),
    "-1": ("bk", -1, -1.0),
    "f0.10": ("program", 1, 0.10),
    "f0.20": ("program", 1, 0.20),
}
DOSE_SLUGS = {"+1": "p1", "+1/2": "p1_2", "+d_20": "pd20", "+d_eq": "pdeq", "0": "0", "-1": "m1",
              "f0.10": "f010", "f0.20": "f020"}

#: §2.4's table, N1-P's row as ADDENDUM-n1 §5.2 amends it: arm -> the (direction, dose labels) it reads, before
#: §2.3's merges (``arm_cells`` applies them).
ARM_CELLS = {
    "N1-V": (("valence", ("+1", "+1/2", "+d_20", "+d_eq", "-1")), ("none", ("0",))),
    "N1-R": tuple((r, ("+1", "+1/2", "+d_20", "+d_eq", "-1")) for r in RANDOM_IDS),
    "N1-P": (("valence", ("+1", "+d_20", "+d_eq", "-1")),),
    "N2-E": (("span_reward", ("f0.10", "f0.20")),),
    "N2-S": (("span_sentiment", ("f0.10", "f0.20")),),
    "N2-C": (("span_character", ("f0.10", "f0.20")),),
    "N4-T": (("none", ("0",)),),
    "N4-Ts": (("none", ("0",)),),
}
#: Each movable label -> the points ``dose_points`` can fold it into (n §2.3; ADDENDUM-n1 §5.1): +d_20 into +1 or
#: +1/2; +d_eq into those or a kept +d_20 (a fold into 0 is refused; d_20, d_eq > 0 never reach -1).
KEEPER_CANDIDATES = {"+d_20": ("+1", "+1/2"), "+d_eq": ("+1", "+1/2", "+d_20")}
ARM_SPAN_KIND = {"N1-V": "S", "N1-R": "S", "N1-P": "SU", "N2-E": "S", "N2-S": "S", "N2-C": "S",
                 "N4-T": "none", "N4-Ts": "none"}
TOLD_VARIANT = {"N4-T": "TOLD", "N4-Ts": "SHAM"}
#: n §2.4: TOLD "Prefer [zone X]."; SHAM "Either is fine.", in the choice prompt before "Reply with ONLY…" (the join
#: fixed by ADDENDUM-n1 §1.2 (ii): after the prompt's first sentence, one space on each side).
TOLD_LINE = "Prefer {zone}."
SHAM_LINE = "Either is fine."
SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = "N1-V", "none", "0"
FIDELITY_REASONS = ("dose-rule", "sample", "timing")

_HEX16 = re.compile(r"[0-9a-f]{16}")
_HEX64 = re.compile(r"[0-9a-f]{64}")
_SESSION = re.compile(r"(floor_b[0-7]|neu_b[0-5])/([0-9]{1,3})")


class SchemaError(ValueError):
    """A record, cell, identity, report or G-READ-n artifact that does not match this schema. Its writer refuses to
    write it; the analyzer refuses to load it."""


# --- field tables -------------------------------------------------------------------------------------------
# Each entry: name -> (type, nullable, meaning). Types: "str", "int", "float", "bool", "sha16", "sha256",
# "ints" (list of int), "floats" (list of float), "spans" (list of [int, int, str]), "pair" (list of two str),
# "layer_sha16" (dict str(layer) -> sha16), "layer_sha256" (dict str(layer) -> sha256), "layer_names" (dict
# str(layer) -> a file name), or the name of a nested table.

RECORD_FIELDS: dict[str, tuple[str, bool, str]] = {
    "schema": ("str", False, "RECORD_SCHEMA"),
    "read_id": ("str", False, "'{arm}|{direction_id}|{dose_label}|{session_id}'"),
    "launch_index": ("int", False, "the read's place in the stage's run order (skip-only resume, n §2.8)"),
    "arm": ("str", False, "one of ARMS"),
    "session_id": ("str", False, "'{bk_cell}/{bk_run}'"),
    "bk_cell": ("str", False, "the skeleton file's name before '.sessions.jsonl', BK's `cell` (BK_CELLS)"),
    "bk_run": ("int", False, "BK's run, 0-159; equal to the session's index in the session set's order"),
    "cue_S": ("str", False, "the conditioned zone's label"),
    "cue_U": ("str", False, "the unconditioned zone's label"),
    "present": ("pair", False, "the choice prompt's label order, as the session record has it"),
    "present_first_is_S": ("bool", False, "present[0] == cue_S"),
    "direction_id": ("str", False, "DIRECTION_IDS; 'none' exactly when nothing is injected"),
    "direction_sha16": ("sha16", True, "the Injection's direction_sha (sha16_arr of the unit direction); null "
                                       "when unsteered"),
    "dose_label": ("str", False, "a key of DOSES that the stage's dose map keeps"),
    "dose_scale": ("str", False, "'bk' (|d| * rho * R), 'program' (f * R_ell) or 'none'"),
    "dose_value": ("float", False, "the signed d (bk) or f (program); 0.0 when unsteered"),
    "sign": ("int", False, "+1, -1 or 0"),
    "alpha": ("float", False, "the L2 norm added at each steered position (BK's injected_l2), unsigned (the sign is "
                              "`sign`); 0.0 unsteered"),
    "layer": ("int", True, "the adapter's injection index (the site); null when unsteered"),
    "steered_spans": ("spans", False, "[start, end, zone label] half-open token ranges, ascending; [] unsteered"),
    "n_steered": ("int", False, "positions covered by steered_spans"),
    "mask_sha16": ("sha16", False, "k's mask_sha of the int8 mask over [0, seq_len)"),
    "retention_interval": ("int", True, "read_position - (last span end - 1); null when unsteered"),
    "shadow_read_id": ("str", True, "the N1-V d = 0 read of the same session; null on unsteered reads"),
    "told_variant": ("str", True, "'TOLD' (N4-T) or 'SHAM' (N4-Ts); null on other arms"),
    "schedule_zone": ("str", True, "'S' or 'U' on N4 (the zone the schedule assigns); null elsewhere"),
    "told_line": ("str", True, "the exact text inserted into the choice prompt on N4; null elsewhere"),
    "seq_len": ("int", False, "tokens in the read sequence, through the generation prompt"),
    "read_position": ("int", False, "seq_len - 1"),
    "ids_sha": ("sha16", False, "sha256(json.dumps(ids))[:16] of the read sequence's ids (BK's form, G-DATA (iv))"),
    "ids_sha_bk": ("sha16", True, "the session record's ids_sha (equal to ids_sha); null on N4"),
    "label_ids_S": ("ints", False, "cue_S's token ids as scored"),
    "label_ids_U": ("ints", False, "cue_U's token ids as scored"),
    "finite": ("bool", False, "every number of the cached path is finite"),
    "logprob_S_tokens": ("floats", True, "per-token full-vocabulary log-probs of label_ids_S, cached path"),
    "logprob_U_tokens": ("floats", True, "per-token full-vocabulary log-probs of label_ids_U, cached path"),
    "logprob_S": ("float", True, "math.fsum(logprob_S_tokens)"),
    "logprob_U": ("float", True, "math.fsum(logprob_U_tokens)"),
    "margin": ("float", True, "logprob_S - logprob_U, nats (BK eq. 1)"),
    "restricted": ("restricted", True, "the restricted two-label read; null when not finite"),
    "capture": ("capture", False, "the read position's residuals: the cell arrays' row and each layer's sha16"),
    "fidelity": ("fidelity", True, "the fresh re-computation: at d in {0, +1, -1} always (campaign, backend-ext), "
                                   "elsewhere on the keyed sample; null otherwise"),
    "identity": ("identity", True, "the d = 0 identity check: on an unsteered read carrying a re-computation, at "
                                   "campaign and time; null otherwise"),
    "duration_ms": ("int", False, "wall-clock of the read's model work, both paths, ms"),
    "duration_ms_fresh": ("int", True, "the fresh path's share of duration_ms; null without a re-computation"),
}

RESTRICTED_FIELDS: dict[str, tuple[str, bool, str]] = {
    "k": ("int", False, "the labels' shared token-prefix length; the read is at read_position + k"),
    "tok_S": ("int", False, "label_ids_S[k]"),
    "tok_U": ("int", False, "label_ids_U[k]"),
    "p_S": ("float", False, "p(tok_S) / (p(tok_S) + p(tok_U))"),
    "p_U": ("float", False, "p(tok_U) / (p(tok_S) + p(tok_U))"),
    "label_mass": ("float", False, "p(tok_S) + p(tok_U) under the full softmax"),
    "pick": ("str", False, "'S' or 'U': the larger; a tie goes to present[0]"),
    "top1_id": ("int", False, "the unrestricted argmax at that position"),
    "top1_is_label": ("bool", False, "top1_id in (tok_S, tok_U)"),
}

CAPTURE_FIELDS: dict[str, tuple[str, bool, str]] = {
    "row": ("int", False, "the record's row in the cell's capture arrays"),
    "sha16": ("layer_sha16", False, "str(layer) -> sha16_arr of that row's residual at that layer"),
}

FIDELITY_FIELDS: dict[str, tuple[str, bool, str]] = {
    "reason": ("str", False, "FIDELITY_REASONS"),
    "finite": ("bool", False, "every number of the fresh path is finite"),
    "fresh_logprob_S": ("float", True, "the fresh path's logprob_S"),
    "fresh_logprob_U": ("float", True, "the fresh path's logprob_U"),
    "fresh_margin": ("float", True, "fresh_logprob_S - fresh_logprob_U"),
    "absdiff": ("float", True, "|margin - fresh_margin|"),
    "scale": ("float", True, "max(|logprob_S|, |logprob_U|), cached path"),
    "rel": ("float", True, "absdiff / scale"),
    "exceeds_tau": ("bool", True, "rel > TAU"),
    "exceeds_tau4": ("bool", True, "rel > TAU / 4"),
    "fresh_capture_sha16": ("layer_sha16", True, "the read-position residuals of the fresh forward for label S, "
                                                 "hashed"),
    "fresh_capture_sha16_U": ("layer_sha16", True, "the read-position residuals of the fresh forward for label U, "
                                                   "hashed"),
}

IDENTITY_CHECK_FIELDS: dict[str, tuple[str, bool, str]] = {
    "bound": ("float", False, "the lock's identity bound (n §2.1), nats"),
    "within": ("bool", False, "fidelity.absdiff <= bound"),
}

CELL_FIELDS: dict[str, tuple[str, bool, str]] = {
    "schema": ("str", False, "CELL_SCHEMA"),
    "stage_identity": ("stage_identity", False, "the stage's identity; equal in every cell file of the stage"),
    "arm": ("str", False, "the cell's arm"),
    "direction_id": ("str", False, "the cell's direction"),
    "dose_label": ("str", False, "the cell's dose point"),
    "records": ("records", False, "the cell's records, in launch order"),
    "capture_files": ("layer_names", False, "str(layer) -> capture_filename(cell name, layer) for every capture "
                                            "layer: that layer's float32 [capture_capacity(arm), d_model] array, "
                                            "beside this file"),
    "capture_rows": ("int", False, "len(records)"),
    "capture_sha256": ("layer_sha256", False, "str(layer) -> sha256 of that layer's written rows [0, capture_rows), "
                                              "float32 little-endian bytes in row order, when this "
                                              "file was written"),
}

STAGE_IDENTITY_FIELDS: dict[str, tuple[str, bool, str]] = {
    "unit": ("str", False, "UNIT"),
    "stage": ("str", False, "STAGES"),
    "record_schema": ("str", False, "RECORD_SCHEMA"),
    "proposal_sha256": ("sha256", False, "PROPOSAL_SHA256"),
    "lock_sha256": ("sha256", True, "the lock in force; null only at backend-ext (before LOCK-n v0.1)"),
    "package_sha256": ("sha256", False, "valence_core/n/*.py in m's package_sha256_of form"),
    "imported_sha256": ("path_sha256", False, "repo path -> sha256 of each module n imports unchanged"),
    "weights_sha256": ("sha256", False, "data/olmo/manifest.json's olmo2_instruct files_aggregate_sha256"),
    "backend_identifier": ("sha16", False, "m's resume.backend_identifier of the adapter's provenance"),
    "pod_id": ("str", False, "the pod instance (n §2.8, m:267's form); at every n stage, so a pod change refuses a "
                             "resume and the stage restarts under a new root (Code's reading)"),
    "read_window": ("int", False, "the declared window of every forward of the stage, at most 4,096 (rule "
                                  "28(d)(c); GA-4)"),
    "session_set_sha256": ("sha256", False, "SESSION_SET_SHA256"),
    "rendering_id": ("str", False, "the rendering of record (ADDENDUM-n1 §1: the ids of record, by their "
                                   "MANIFEST.json), as the lock names it; at backend-ext, "
                                   "before the lock, as the stage's entry names it"),
    "label_convention": ("str", False, "the label token convention, as the lock names it; at backend-ext, before "
                                       "the lock, as the stage's entry names it"),
    "layer_bk": ("int", False, "BK's site, 32 of 64"),
    "layer": ("int", False, "the adapter index of the site (G-VEC settles 31 or 32); at backend-ext, before G-VEC, "
                            "the capture site the stage's entry declares (nothing is injected there)"),
    "capture_layers": ("ints", False, "list(range(layer + 1, n_layers)): every decoder layer past the site through "
                                      "the last (ADDENDUM-n1 §6.2)"),
    "n_layers": ("int", False, "64"),
    "d_model": ("int", False, "5120"),
    "dose_map": ("dose_map", True, "the dose map of record; null only at backend-ext"),
    "directions": ("dir_sha16", False, "direction_id -> sha16 for every direction the stage injects"),
    "fidelity_rule": ("fidelity_rule", False, "TAU, p0, cadence and the sample's key"),
    "identity_bound": ("float", True, "the lock's identity bound; null only at backend-ext"),
}

DOSE_MAP_FIELDS: dict[str, tuple[str, bool, str]] = {
    "rho": ("float", False, "BK's rho, 0.30 (Table A2)"),
    "R": ("float", False, "BK's R at the site, from G-VEC's neutral captures"),
    "R_ell": ("float", False, "R_l at the site by the step-2-survey convention (g:165)"),
    "d_eq": ("float", False, "(0.10 * R_ell) / (rho * R)"),
    "d_20": ("float", False, "min(1, 2 * d_eq)"),
    "points": ("dose_points", False, "[{label, value, merged}] the points read; merged = labels folded in"),
}

FIDELITY_RULE_FIELDS: dict[str, tuple[str, bool, str]] = {
    "tau": ("float", False, "TAU"),
    "p0_count": ("int", False, "BK's exceedances at TAU (G-DATA (vi): 0)"),
    "p0_n": ("int", False, "BK's reads (G-DATA (vi): 2400)"),
    "cadence": ("int", False, "the binomial's cadence in reads (n §2.1: 160)"),
    "sample_key": ("str", False, "'n-fid|{s}'"),
    "sample_rule": ("str", False, "the lock's words for the 10% sample; at backend-ext, where every read is at d = "
                                  "0, the entry's"),
}


# --- helpers both sides use ---------------------------------------------------------------------------------
def read_id(arm: str, direction_id: str, dose_label: str, session_id: str) -> str:
    return f"{arm}|{direction_id}|{dose_label}|{session_id}"


def session_id(bk_cell: str, bk_run: int) -> str:
    return f"{bk_cell}/{int(bk_run)}"


def shadow_read_id(sid: str) -> str:
    return read_id(SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE, sid)


def cell_filename(arm: str, direction_id: str, dose_label: str) -> str:
    """The cell file's name; its capture arrays are the same stem with ``.L{layer}.npy`` (``capture_filename``)."""
    if arm not in ARMS or direction_id not in DIRECTION_IDS or dose_label not in DOSE_SLUGS:
        raise SchemaError(f"no cell ({arm!r}, {direction_id!r}, {dose_label!r})")
    return f"{arm}__{direction_id}__{DOSE_SLUGS[dose_label]}.json"


def capture_filename(cell_name: str, layer: int) -> str:
    """One capture array's file name, beside its cell file (one array per cell per layer, ADDENDUM-n1 §6.2): the
    cell file name's stem plus ``.L{layer}.npy``."""
    if not cell_name.endswith(".json"):
        raise SchemaError(f"{cell_name!r} is not a cell file name")
    return cell_name[:-len(".json")] + f".L{layer}.npy"


def capture_capacity(arm: str) -> int:
    """The rows a cell's capture arrays hold: N1-R reads the 40 floor sessions (C2), every other arm at most the 160."""
    if arm not in ARMS:
        raise SchemaError(f"{arm!r} is not an arm")
    return N_FLOOR if arm == "N1-R" else N_SESSIONS


def expected_alpha(dose_label: str, dose_value: float, dose_map: Mapping[str, Any] | None) -> float:
    """The one formula for ``alpha``: |d| * rho * R on BK's scale, f * R_ell on the program's (n §2.3)."""
    scale = DOSES[dose_label][0]
    if scale == "none":
        return 0.0
    if dose_map is None:
        raise SchemaError(f"dose {dose_label!r} needs the stage's dose map")
    if scale == "bk":
        return abs(float(dose_value)) * float(dose_map["rho"]) * float(dose_map["R"])
    return float(dose_value) * float(dose_map["R_ell"])


def fidelity_numbers(margin: float, logprob_S: float, logprob_U: float, fresh_margin: float) -> dict:
    """``absdiff``, ``scale``, ``rel``, ``exceeds_tau`` and ``exceeds_tau4`` exactly as both sides compute them."""
    absdiff = abs(margin - fresh_margin)
    scale = max(abs(logprob_S), abs(logprob_U))
    if not scale > 0.0:
        raise SchemaError("fidelity scale is not positive")
    rel = absdiff / scale
    return {"absdiff": absdiff, "scale": scale, "rel": rel, "exceeds_tau": rel > TAU, "exceeds_tau4": rel > TAU4}


def shared_prefix(a: list[int], b: list[int]) -> int:
    k = 0
    while k < len(a) and k < len(b) and a[k] == b[k]:
        k += 1
    return k


def bk_cell_of(bk_run: int) -> str:
    """The skeleton file that holds BK's run: floor_b0-b7 hold runs 0-39 (five each), neu_b0-b5 runs 40-159
    (twenty each)."""
    r = int(bk_run)
    if not 0 <= r < N_SESSIONS:
        raise SchemaError(f"run {r} is not one of BK's 160")
    return f"floor_b{r // 5}" if r < N_FLOOR else f"neu_b{(r - N_FLOOR) // 20}"


def read_plan(identity: Mapping[str, Any]) -> list[str]:
    """The campaign's declared read set, as read_ids sorted: n §2.4's arms over the stage's dose map, a merged
    point read once under the label kept, N1-R on the 40 floor sessions (C2), every other arm on all 160. An arm
    whose obtained read_ids are not its plan's is partial (n §5: "An arm with a partial read set is
    INDETERMINATE"). G-TIME-n's and the BACKEND extension's read sets are their own, not this one."""
    if identity.get("stage") != "campaign":
        raise SchemaError("read_plan is the campaign's; other stages declare their own read sets")
    out = []
    for arm in ARMS:
        runs = range(N_FLOOR) if arm == "N1-R" else range(N_SESSIONS)
        for did, labels in arm_cells(arm, identity):
            for dl in labels:
                out.extend(read_id(arm, did, dl, session_id(bk_cell_of(r), r)) for r in runs)
    return sorted(out)


def read_plan_sha256(identity: Mapping[str, Any]) -> str:
    """sha256 of the plan's read_ids joined by newlines (no trailing newline): the figure a stage report and the
    lock carry for the plan."""
    return hashlib.sha256("\n".join(read_plan(identity)).encode("utf-8")).hexdigest()


# --- type checks --------------------------------------------------------------------------------------------
def _fail(where: str, msg: str) -> None:
    raise SchemaError(f"{where}: {msg}")


def _is_int(x: Any) -> bool:
    return type(x) is int


def _is_float(x: Any) -> bool:
    return type(x) is float and math.isfinite(x)


def _check_type(t: str, v: Any, where: str) -> None:
    if t == "str":
        ok = type(v) is str
    elif t == "int":
        ok = _is_int(v)
    elif t == "float":
        ok = _is_float(v)
    elif t == "bool":
        ok = type(v) is bool
    elif t == "sha16":
        ok = type(v) is str and _HEX16.fullmatch(v) is not None
    elif t == "sha256":
        ok = type(v) is str and _HEX64.fullmatch(v) is not None
    elif t == "ints":
        ok = type(v) is list and all(_is_int(x) for x in v)
    elif t == "floats":
        ok = type(v) is list and all(_is_float(x) for x in v)
    elif t == "pair":
        ok = type(v) is list and len(v) == 2 and all(type(x) is str for x in v)
    elif t == "spans":
        ok = type(v) is list and all(
            type(s) is list and len(s) == 3 and _is_int(s[0]) and _is_int(s[1]) and type(s[2]) is str for s in v)
    elif t == "layer_sha16":
        ok = type(v) is dict and len(v) > 0 and all(
            type(k) is str and re.fullmatch(r"0|[1-9][0-9]*", k) and type(x) is str and _HEX16.fullmatch(x)
            for k, x in v.items())
    elif t == "layer_sha256":
        ok = type(v) is dict and len(v) > 0 and all(
            type(k) is str and re.fullmatch(r"0|[1-9][0-9]*", k) and type(x) is str and _HEX64.fullmatch(x)
            for k, x in v.items())
    elif t == "layer_names":
        ok = type(v) is dict and len(v) > 0 and all(
            type(k) is str and re.fullmatch(r"0|[1-9][0-9]*", k) and type(x) is str for k, x in v.items())
    elif t == "path_sha256":
        ok = type(v) is dict and len(v) > 0 and all(
            type(k) is str and type(x) is str and _HEX64.fullmatch(x) for k, x in v.items())
    elif t == "dir_sha16":
        ok = type(v) is dict and all(
            type(k) is str and k in DIRECTION_IDS and k != "none" and type(x) is str and _HEX16.fullmatch(x)
            for k, x in v.items())
    else:
        _fail(where, f"unknown type {t!r}")
        return
    if not ok:
        _fail(where, f"expected {t}, got {type(v).__name__} {v!r}"[:300])


def _check_table(obj: Any, table: Mapping[str, tuple[str, bool, str]], where: str) -> None:
    if type(obj) is not dict:
        _fail(where, f"expected an object, got {type(obj).__name__}")
    missing = sorted(set(table) - set(obj))
    extra = sorted(set(obj) - set(table))
    if missing or extra:
        _fail(where, f"keys differ from the schema: missing {missing}, extra {extra}")
    for name, (t, nullable, _doc) in table.items():
        v = obj[name]
        w = f"{where}.{name}"
        if v is None:
            if not nullable:
                _fail(w, "is null")
            continue
        if t in NESTED:
            NESTED[t](v, w)
        else:
            _check_type(t, v, w)


def _check_restricted(v: Any, where: str) -> None:
    _check_table(v, RESTRICTED_FIELDS, where)


def _check_capture(v: Any, where: str) -> None:
    _check_table(v, CAPTURE_FIELDS, where)


def _check_fidelity(v: Any, where: str) -> None:
    _check_table(v, FIDELITY_FIELDS, where)


def _check_identity_block(v: Any, where: str) -> None:
    _check_table(v, IDENTITY_CHECK_FIELDS, where)


def _check_dose_points(v: Any, where: str) -> None:
    if type(v) is not list or not v:
        _fail(where, "expected a non-empty list of dose points")
    for i, p in enumerate(v):
        w = f"{where}[{i}]"
        if type(p) is not dict or sorted(p) != ["label", "merged", "value"]:
            _fail(w, "a dose point is {label, value, merged}")
        if p["label"] not in DOSES or not _is_float(p["value"]):
            _fail(w, f"bad label or value {p!r}")
        if type(p["merged"]) is not list or any(m not in DOSES or m == p["label"] for m in p["merged"]):
            _fail(w, f"bad merged list {p['merged']!r}")


def _check_dose_map(v: Any, where: str) -> None:
    _check_table(v, DOSE_MAP_FIELDS, where)


def _check_fidelity_rule(v: Any, where: str) -> None:
    _check_table(v, FIDELITY_RULE_FIELDS, where)


def _check_stage_identity_table(v: Any, where: str) -> None:
    _check_table(v, STAGE_IDENTITY_FIELDS, where)


def _check_records_list(v: Any, where: str) -> None:
    if type(v) is not list:
        _fail(where, "expected a list of records")


NESTED = {
    "restricted": _check_restricted,
    "capture": _check_capture,
    "fidelity": _check_fidelity,
    "identity": _check_identity_block,
    "dose_points": _check_dose_points,
    "dose_map": _check_dose_map,
    "fidelity_rule": _check_fidelity_rule,
    "stage_identity": _check_stage_identity_table,
    "records": _check_records_list,
}


# --- the checks of record -----------------------------------------------------------------------------------
def dose_points(d_eq: float, d_20: float) -> list[dict]:
    """The dose map's points under n §2.3's merge rule ("a point within 0.05 of an existing one is merged"), in
    the form settled with n-analyzer (accepted: the seat's answers of 2026-11-16, §3):

      * +d_20 first, against the existing points in the order +1, +1/2, 0, -1; then +d_eq, against the same four
        and +d_20 if +d_20 was kept;
      * a point is folded into the nearest candidate whose distance ``abs(value - candidate)``, an IEEE double, is
        <= MERGE_DISTANCE; a tie goes to the earlier candidate; a value equal to a candidate is that point (so
        d_20 = 1.0, the cap, folds into +1);
      * a point that would fold into 0 is refused (a dose at d = 0 is no dose: the seat's, if it ever arises). With
        d_20 = 2·d_eq, a d_eq in (0.025, 0.05] lies exactly as far from 0 as from +d_20, and the tie goes to 0, so
        it is refused too. The distance is binary: 0.55 - 0.5 is 0.050000000000000044, so 0.55 is not within 0.05
        of +1/2, although it is in decimal.

    Returned in the order +1, +1/2, +d_20 (if kept), +d_eq (if kept), -1, f0.10, f0.20, each {label, value,
    merged}; a kept point's ``merged`` lists the labels folded into it, in fold order."""
    d_eq, d_20 = float(d_eq), float(d_20)
    cands = [("+1", 1.0), ("+1/2", 0.5), ("0", 0.0), ("-1", -1.0)]
    merged: dict[str, list] = {lab: [] for lab, _ in cands}
    kept: dict[str, float] = {}
    for label, value in (("+d_20", d_20), ("+d_eq", d_eq)):
        best = None
        for lab, v in cands:
            dist = abs(value - v)
            if dist <= MERGE_DISTANCE and (best is None or dist < best[1]):
                best = (lab, dist)
        if best is None:
            kept[label] = value
            merged[label] = []
            cands.append((label, value))
        elif best[0] == "0":
            raise SchemaError(f"{label} = {value!r} would fold into d = 0: a dose at 0 is no dose")
        else:
            merged[best[0]].append(label)
    out = [{"label": "+1", "value": 1.0, "merged": merged["+1"]},
           {"label": "+1/2", "value": 0.5, "merged": merged["+1/2"]}]
    for label in ("+d_20", "+d_eq"):
        if label in kept:
            out.append({"label": label, "value": kept[label], "merged": merged[label]})
    out += [{"label": "-1", "value": -1.0, "merged": merged["-1"]},
            {"label": "f0.10", "value": 0.10, "merged": []}, {"label": "f0.20", "value": 0.20, "merged": []}]
    return out


def dose_point_values(identity: Mapping[str, Any]) -> dict[str, float]:
    """label -> value for every point the stage's dose map keeps, and "0". A merged label is absent: its read is
    its keeper's."""
    dm = identity.get("dose_map")
    out = {"0": 0.0}
    if dm is None:
        return out
    for p in dm["points"]:
        out[p["label"]] = p["value"]
    return out


def keeper(label: str, identity: Mapping[str, Any]) -> str | None:
    """The kept label a listed dose label is read under (n §2.3; ADDENDUM-n1 §5.1): the label itself if
    ``dose_point_values`` keeps it, else the dose map point whose ``merged`` names it, else None. With no dose map,
    every label but "0" gives None."""
    if label in dose_point_values(identity):
        return label
    dm = identity.get("dose_map")
    if dm is None:
        return None
    for p in dm["points"]:
        if label in p["merged"]:
            return p["label"]
    return None


def arm_cells(arm: str, identity: Mapping[str, Any]) -> list[tuple[str, list[str]]]:
    """The arm's (direction_id, [labels]) list under the stage's dose map: each label ARM_CELLS lists, mapped to its
    ``keeper`` in listed order, repeats and None dropped, so a merged point is read once under the label kept (the
    seat's answers of 2026-11-16, §2.3; ADDENDUM-n1 §5.1-§5.2)."""
    out = []
    for did, labels in ARM_CELLS[arm]:
        kept: list[str] = []
        for dl in labels:
            k = keeper(dl, identity)
            if k is not None and k not in kept:
                kept.append(k)
        out.append((did, kept))
    return out


def check_stage_identity(identity: Any, where: str = "stage_identity") -> None:
    _check_table(identity, STAGE_IDENTITY_FIELDS, where)
    if identity["unit"] != UNIT:
        _fail(f"{where}.unit", f"is {identity['unit']!r}, not {UNIT!r}")
    if identity["stage"] not in STAGES:
        _fail(f"{where}.stage", f"{identity['stage']!r} is not one of {STAGES}")
    if identity["record_schema"] != RECORD_SCHEMA:
        _fail(f"{where}.record_schema", f"is {identity['record_schema']!r}, not {RECORD_SCHEMA!r}")
    if identity["proposal_sha256"] != PROPOSAL_SHA256:
        _fail(f"{where}.proposal_sha256", "is not PROPOSAL-n v0.2's")
    if identity["session_set_sha256"] != SESSION_SET_SHA256:
        _fail(f"{where}.session_set_sha256", "is not the session set of record")
    pre_lock = identity["stage"] == "backend-ext"
    for k in ("lock_sha256", "dose_map", "identity_bound"):
        if (identity[k] is None) != pre_lock:
            _fail(f"{where}.{k}", "is null exactly at backend-ext")
    if not 0 < identity["read_window"] <= MAX_WINDOW:
        _fail(f"{where}.read_window", f"is not in (0, {MAX_WINDOW}] (GA-4)")
    if identity["capture_layers"] != list(range(identity["layer"] + 1, identity["n_layers"])):
        _fail(f"{where}.capture_layers", "is not list(range(layer + 1, n_layers)), the band past the site "
                                         "(ADDENDUM-n1 §6.2)")
    if identity["layer_bk"] != 32:
        _fail(f"{where}.layer_bk", "is not 32 (BK Table 1)")
    if not 0 <= identity["layer"] < identity["n_layers"] - 1:
        _fail(f"{where}.layer", "is out of range")
    fr = identity["fidelity_rule"]
    if fr["tau"] != TAU or fr["sample_key"] != "n-fid|{s}" or not 0 <= fr["p0_count"] <= fr["p0_n"]:
        _fail(f"{where}.fidelity_rule", f"differs from n §2.1 / G-DATA (vi): {fr!r}"[:300])
    dm = identity["dose_map"]
    if dm is not None:
        if dm["rho"] != RHO:
            _fail(f"{where}.dose_map.rho", f"is {dm['rho']!r}, not n §2.3's {RHO!r}")
        if not (dm["R"] > 0.0 and dm["R_ell"] > 0.0):
            _fail(f"{where}.dose_map", "R and R_ell must be positive")
        if dm["d_eq"] != (0.10 * dm["R_ell"]) / (dm["rho"] * dm["R"]):
            _fail(f"{where}.dose_map.d_eq", "is not (0.10 * R_ell) / (rho * R)")
        if dm["d_20"] != min(1.0, 2.0 * dm["d_eq"]):
            _fail(f"{where}.dose_map.d_20", "is not min(1.0, 2.0 * d_eq)")
        if dm["points"] != dose_points(dm["d_eq"], dm["d_20"]):
            _fail(f"{where}.dose_map.points", "are not dose_points(d_eq, d_20) (the merge rule of n §2.3)")


def check_record(rec: Any, identity: Mapping[str, Any], where: str = "record") -> None:
    """Every field and every local invariant of one read record, against its stage's identity."""
    _check_table(rec, RECORD_FIELDS, where)
    w = lambda f: f"{where}.{f}"                                          # noqa: E731
    if rec["schema"] != RECORD_SCHEMA:
        _fail(w("schema"), f"is {rec['schema']!r}")
    arm, did, dl = rec["arm"], rec["direction_id"], rec["dose_label"]
    if arm not in ARMS:
        _fail(w("arm"), f"{arm!r} is not an arm")
    if dl not in DOSES:
        _fail(w("dose_label"), f"{dl!r} is not a dose label")
    allowed = {(d, x) for d, xs in arm_cells(arm, identity) for x in xs}
    if (did, dl) not in allowed:
        _fail(where, f"arm {arm} reads no ({did}, {dl})")
    kept = dose_point_values(identity)
    if dl not in kept:
        _fail(w("dose_label"), f"{dl!r} is not a point of the stage's dose map")
    # session
    m = _SESSION.fullmatch(rec["session_id"])
    if (m is None or m.group(1) != rec["bk_cell"] or int(m.group(2)) != rec["bk_run"]
            or rec["session_id"] != session_id(rec["bk_cell"], rec["bk_run"])):
        _fail(w("session_id"), "does not match bk_cell/bk_run")
    run, cell_i = rec["bk_run"], BK_CELLS.index(rec["bk_cell"])
    lo = 5 * cell_i if cell_i < 8 else N_FLOOR + 20 * (cell_i - 8)
    if not lo <= run < lo + (5 if cell_i < 8 else 20):
        _fail(w("bk_run"), f"run {run} is not in {rec['bk_cell']}")
    if arm == "N1-R" and run >= N_FLOOR:
        _fail(w("bk_run"), "N1-R reads only the 40 floor sessions (C2)")
    if rec["read_id"] != read_id(arm, did, dl, rec["session_id"]):
        _fail(w("read_id"), "is not '{arm}|{direction_id}|{dose_label}|{session_id}'")
    if rec["launch_index"] < 0:
        _fail(w("launch_index"), "is negative")
    # labels
    cs, cu, pr = rec["cue_S"], rec["cue_U"], rec["present"]
    if cs == cu or sorted(pr) != sorted([cs, cu]):
        _fail(w("present"), "is not the two cues")
    if rec["present_first_is_S"] != (pr[0] == cs):
        _fail(w("present_first_is_S"), "disagrees with present")
    ls, lu = rec["label_ids_S"], rec["label_ids_U"]
    if not ls or not lu or ls == lu:
        _fail(w("label_ids_S"), "label token sequences are empty or equal")
    k = shared_prefix(ls, lu)
    if k >= min(len(ls), len(lu)):
        _fail(w("label_ids_S"), "one label's tokens are a prefix of the other's")
    if rec["seq_len"] + max(len(ls), len(lu)) - 1 > identity["read_window"]:
        _fail(w("seq_len"), f"a forward of this read exceeds the stage's read_window {identity['read_window']}")
    # dose and direction
    scale, sign, fixed = DOSES[dl]
    if rec["dose_scale"] != scale or rec["sign"] != sign:
        _fail(w("dose_scale"), f"{dl} is ({scale}, {sign})")
    if rec["dose_value"] != kept[dl] or (fixed is not None and rec["dose_value"] != fixed):
        _fail(w("dose_value"), f"is not the dose map's value for {dl}")
    steered = sign != 0
    if (did == "none") == steered:
        _fail(w("direction_id"), "is 'none' exactly when nothing is injected")
    if steered:
        if rec["direction_sha16"] != identity["directions"].get(did):
            _fail(w("direction_sha16"), "is not the stage's sha for this direction")
        if rec["layer"] != identity["layer"]:
            _fail(w("layer"), "is not the stage's site")
        a = expected_alpha(dl, rec["dose_value"], identity["dose_map"])
        if rec["alpha"] != a or not a > 0.0:
            _fail(w("alpha"), f"is {rec['alpha']!r}, the formula gives {a!r}")
    else:
        if rec["direction_sha16"] is not None or rec["layer"] is not None or rec["alpha"] != 0.0:
            _fail(where, "an unsteered read carries a direction, a layer or a norm")
    # positions, spans, mask
    if rec["read_position"] != rec["seq_len"] - 1 or rec["seq_len"] < 2:
        _fail(w("read_position"), "is not seq_len - 1")
    spans = rec["steered_spans"]
    if steered != bool(spans):
        _fail(w("steered_spans"), "are empty exactly when nothing is injected")
    prev = 0
    for i, (a0, b0, z) in enumerate(spans):
        if not prev <= a0 < b0 <= rec["read_position"]:
            _fail(w("steered_spans"), f"span {i} [{a0}, {b0}) is unordered, overlaps or reaches the read")
        prev = b0
    zones = [z for _, _, z in spans]
    kind = ARM_SPAN_KIND[arm]
    if steered and kind == "S" and (len(spans) != 6 or set(zones) != {cs}):
        _fail(w("steered_spans"), "are not the six S whole-turn spans")
    if steered and kind == "SU" and (len(spans) != 12 or sorted(set(zones)) != sorted([cs, cu])):
        _fail(w("steered_spans"), "are not the twelve turn spans of both zones (N1-P)")
    if rec["n_steered"] != sum(b0 - a0 for a0, b0, _ in spans):
        _fail(w("n_steered"), "is not the spans' total")
    if steered:
        if rec["retention_interval"] != rec["read_position"] - (spans[-1][1] - 1):
            _fail(w("retention_interval"), "is not read_position - last steered position")
    elif rec["retention_interval"] is not None:
        _fail(w("retention_interval"), "is set on an unsteered read")
    # shadow
    want_shadow = shadow_read_id(rec["session_id"]) if steered else None
    if rec["shadow_read_id"] != want_shadow:
        _fail(w("shadow_read_id"), f"should be {want_shadow!r}")
    # N4
    n4 = arm in TOLD_VARIANT
    if rec["told_variant"] != TOLD_VARIANT.get(arm):
        _fail(w("told_variant"), f"should be {TOLD_VARIANT.get(arm)!r}")
    if n4:
        if rec["schedule_zone"] not in ("S", "U"):
            _fail(w("schedule_zone"), "an N4 read needs 'S' or 'U'")
        named = cs if rec["schedule_zone"] == "S" else cu
        want_line = TOLD_LINE.format(zone=named) if arm == "N4-T" else SHAM_LINE
        if rec["told_line"] != want_line:
            _fail(w("told_line"), f"should be {want_line!r} (n §2.4)")
        if rec["ids_sha_bk"] is not None:
            _fail(w("ids_sha_bk"), "is set on N4, whose sequence is its own")
    else:
        if rec["schedule_zone"] is not None or rec["told_line"] is not None:
            _fail(where, "schedule_zone / told_line are set off N4")
        if rec["ids_sha_bk"] != rec["ids_sha"]:
            _fail(w("ids_sha_bk"), "differs from ids_sha: a rendering mismatch is never a record (a pause during a "
                                   "stage; a G-VER-STOP at G-VER)")
    # the cached read
    toks = (rec["logprob_S_tokens"], rec["logprob_U_tokens"], rec["logprob_S"], rec["logprob_U"], rec["margin"])
    if rec["finite"]:
        if any(x is None for x in toks) or rec["restricted"] is None:
            _fail(where, "a finite read has a null number")
        if len(toks[0]) != len(ls) or len(toks[1]) != len(lu):
            _fail(w("logprob_S_tokens"), "lengths differ from the label ids")
        if any(x > 0.0 for x in toks[0] + toks[1]):
            _fail(w("logprob_S_tokens"), "a log-probability is positive")
        if toks[2] != math.fsum(toks[0]) or toks[3] != math.fsum(toks[1]):
            _fail(w("logprob_S"), "is not math.fsum of its tokens")
        if toks[4] != toks[2] - toks[3]:
            _fail(w("margin"), "is not logprob_S - logprob_U")
        r = rec["restricted"]
        if r["k"] != k or r["tok_S"] != ls[k] or r["tok_U"] != lu[k]:
            _fail(w("restricted"), "is not at the labels' first divergent token")
        if not (0.0 <= r["p_S"] <= 1.0 and 0.0 <= r["p_U"] <= 1.0 and 0.0 <= r["label_mass"] <= 1.0):
            _fail(w("restricted"), "a probability is outside [0, 1]")
        if abs(r["p_S"] + r["p_U"] - 1.0) > 1e-9:
            _fail(w("restricted"), "p_S + p_U is not 1")
        tie_pick = "S" if pr[0] == cs else "U"
        want = "S" if r["p_S"] > r["p_U"] else "U" if r["p_U"] > r["p_S"] else tie_pick
        if r["pick"] != want:
            _fail(w("restricted.pick"), f"should be {want!r}")
        if r["top1_is_label"] != (r["top1_id"] in (r["tok_S"], r["tok_U"])):
            _fail(w("restricted.top1_is_label"), "disagrees with top1_id")
    else:
        if any(x is not None for x in toks) or rec["restricted"] is not None:
            _fail(where, "a non-finite read keeps a number")
    # capture
    want_layers = sorted(str(x) for x in identity["capture_layers"])
    if sorted(rec["capture"]["sha16"]) != want_layers or rec["capture"]["row"] < 0:
        _fail(w("capture"), f"must hash exactly the layers {want_layers} at a row >= 0")
    # fidelity and identity
    f = rec["fidelity"]
    dose_rule = dl in DOSE_RULE_LABELS
    if f is None and dose_rule and identity["stage"] in ("campaign", "backend-ext"):
        _fail(w("fidelity"), f"a read at {dl} carries the dose-rule re-computation (n §2.1)")
    if f is not None:
        if f["reason"] not in FIDELITY_REASONS:
            _fail(w("fidelity.reason"), f"{f['reason']!r} is not one of {FIDELITY_REASONS}")
        other = {"campaign": "sample", "time": "timing"}.get(identity["stage"])
        if f["reason"] != ("dose-rule" if dose_rule else other):
            _fail(w("fidelity.reason"), "the dose rule covers d in {0, +1, -1} exactly; any other point is the "
                                        "campaign's keyed sample or G-TIME-n's timing re-computation")
        fresh = ("fresh_logprob_S", "fresh_logprob_U", "fresh_margin", "fresh_capture_sha16", "fresh_capture_sha16_U")
        derived = ("absdiff", "scale", "rel", "exceeds_tau", "exceeds_tau4")
        if f["finite"]:
            if any(f[x] is None for x in fresh):
                _fail(w("fidelity"), "a finite re-computation has a null number")
            if f["fresh_margin"] != f["fresh_logprob_S"] - f["fresh_logprob_U"]:
                _fail(w("fidelity.fresh_margin"), "is not fresh_logprob_S - fresh_logprob_U")
            for x in ("fresh_capture_sha16", "fresh_capture_sha16_U"):
                if sorted(f[x]) != want_layers:
                    _fail(w(f"fidelity.{x}"), f"must hash exactly the layers {want_layers}")
        elif any(f[x] is not None for x in fresh):
            _fail(w("fidelity"), "a non-finite re-computation keeps a number")
        if f["finite"] and rec["finite"]:
            want_f = fidelity_numbers(rec["margin"], rec["logprob_S"], rec["logprob_U"], f["fresh_margin"])
            for x, v in want_f.items():
                if f[x] != v:
                    _fail(w(f"fidelity.{x}"), f"is {f[x]!r}, the formula gives {v!r}")
        elif any(f[x] is not None for x in derived):
            _fail(w("fidelity"), "a comparison is set although a path is not finite")
    idc = rec["identity"]
    needs_identity = (not steered) and f is not None and identity["stage"] != "backend-ext"
    if needs_identity:
        if idc is None or idc["bound"] != identity["identity_bound"]:
            _fail(w("identity"), "an unsteered read with a re-computation carries the identity check at the "
                                 "lock's bound")
        if f["absdiff"] is None:
            if idc["within"]:
                _fail(w("identity.within"), "is true without a finite comparison")
        elif idc["within"] != (f["absdiff"] <= idc["bound"]):
            _fail(w("identity.within"), "is not absdiff <= bound")
    elif idc is not None:
        _fail(w("identity"), "is set where the check does not apply")
    if rec["duration_ms"] < 0:
        _fail(w("duration_ms"), "is negative")
    dfr = rec["duration_ms_fresh"]
    if (dfr is None) != (f is None):
        _fail(w("duration_ms_fresh"), "is null exactly when there is no re-computation")
    if dfr is not None and not 0 <= dfr <= rec["duration_ms"]:
        _fail(w("duration_ms_fresh"), "is not within [0, duration_ms]")


def check_cell(cell: Any, where: str = "cell") -> None:
    """A cell file's container and every record in it."""
    _check_table(cell, CELL_FIELDS, where)
    if cell["schema"] != CELL_SCHEMA:
        _fail(f"{where}.schema", f"is {cell['schema']!r}")
    ident = cell["stage_identity"]
    check_stage_identity(ident, f"{where}.stage_identity")
    arm, did, dl = cell["arm"], cell["direction_id"], cell["dose_label"]
    name = cell_filename(arm, did, dl)
    want_files = {str(x): capture_filename(name, x) for x in ident["capture_layers"]}
    if cell["capture_files"] != want_files:
        _fail(f"{where}.capture_files", "is not capture_filename(the cell's name, layer) for exactly the identity's "
                                        "capture layers")
    if sorted(cell["capture_sha256"]) != sorted(want_files):
        _fail(f"{where}.capture_sha256", "must hash exactly the identity's capture layers")
    recs = cell["records"]
    if len(recs) > capture_capacity(arm):
        _fail(f"{where}.records", f"exceed the cell's capture capacity {capture_capacity(arm)}")
    if cell["capture_rows"] != len(recs):
        _fail(f"{where}.capture_rows", "is not len(records)")
    seen, last = set(), -1
    for i, rec in enumerate(recs):
        wi = f"{where}.records[{i}]"
        check_record(rec, ident, wi)
        if (rec["arm"], rec["direction_id"], rec["dose_label"]) != (arm, did, dl):
            _fail(wi, "belongs to another cell")
        if rec["read_id"] in seen:
            _fail(wi, "repeats a read_id")
        seen.add(rec["read_id"])
        if rec["launch_index"] <= last:
            _fail(f"{wi}.launch_index", "is not increasing")
        last = rec["launch_index"]
        if rec["capture"]["row"] != i:
            _fail(f"{wi}.capture.row", f"should be {i}")


# --- the stage report (n-report-v1) and G-READ-n's artifact (n-gread-v1), settled with n-analyzer ----------------
REPORT_SCHEMA = "n-report-v1"
GREAD_SCHEMA = "n-gread-v1"
END_STATES = ("COMPLETE", "PAUSE", "PI-STOP", "G-VER-STOP", "CAP")
#: In precedence order: a read that fires several triggers is one pause of the first kind, the rest in also_fired.
PAUSE_KINDS = ("rendering", "nonfinite", "identity-bound", "fidelity-binomial")
STOP_KINDS = ("G-VER-STOP", "PI-STOP")
GREAD_AXES = {"valence": ("+1", "+1/2", "+d_20", "+d_eq"), "span_reward": ("f0.10", "f0.20")}
GREAD_STATUSES = ("PASS", "FAIL", "NOT-COMPUTED")
GREAD_BAR = 0.90
#: k's fit_lr hyperparameters (valence_core/echo/probe.py's LR_SEED, LR_ITERS, LR_RATE, LR_L2), pinned.
GREAD_LR = {"seed": 7, "iters": 300, "rate": 0.1, "l2": 0.01}
#: Every cell file name a stage can hold: cell_filename over ARM_CELLS, each listed label with the KEEPER_CANDIDATES
#: it can fold into (139 names: N1-P's +1/2 among them, as its +d_20 or +d_eq can fold into +1/2).
VALID_CELL_NAMES = {cell_filename(a, d, y): a for a in ARMS for d, xs in ARM_CELLS[a] for x in xs
                    for y in (x,) + KEEPER_CANDIDATES.get(x, ())}
_CELL_KEYS = {cell_filename(a, d, y): (a, d, y) for a in ARMS for d, xs in ARM_CELLS[a] for x in xs
              for y in (x,) + KEEPER_CANDIDATES.get(x, ())}
#: ADDENDUM-n1 §6.3's "grouped 10-fold cross-validation by session, the fold seed in the lock", in place of n §3's
#: leave-one-session-out; the folds' seed is the probe's ``cv_seed``.
CV_FORMS = re.compile(r"kfold10")
GREAD_MERGEABLE = {"valence": ("+d_20", "+d_eq"), "span_reward": ()}

REPORT_FIELDS: dict[str, tuple[str, bool, str]] = {
    "schema": ("str", False, "REPORT_SCHEMA"),
    "stage_identity": ("stage_identity", False, "the stage's identity, as every cell file carries it"),
    "stage_identity_sha256": ("sha256", False, "identity_sha256(stage_identity)"),
    "read_plan_sha256": ("sha256", True, "read_plan_sha256(stage_identity) at the campaign; null at other stages"),
    "end_state": ("str", False, "END_STATES: the invocation's end"),
    "per_arm": ("per_arm", False, "arm -> {planned, obtained, complete} for every arm of the stage's plan, planned "
                                  "from the declared read set; non-empty, every cell's arm among them"),
    "cells": ("cell_shas", False, "cell filename -> {json_sha256, capture_sha256, records}, every cell file of "
                                  "the stage at the report's write: the file's sha256, the cell's own "
                                  "capture_sha256, its record count"),
    "pauses": ("pauses", False, "every pause of the stage, in launch order, adjudicated or not"),
    "binomial_state": ("binomial_state", False, "the fidelity binomial's running state over the stage: trials, "
                                                "exceedances, evaluations, fires"),
    "stop": ("stop", True, "{kind, record_sha256, detail} at G-VER-STOP or PI-STOP; null otherwise"),
    "cap": ("cap", False, "{hour_cap_ms, used_ms, hit, loads_ms}"),
    "counters": ("counters", False, "n §4's counters and the identity-bound count, over the stage"),
}
PAUSE_FIELDS: dict[str, tuple[str, bool, str]] = {
    "pause_id": ("str", False, "'p01', 'p02', ... by its place in the list, which is in launch order"),
    "kind": ("str", False, "PAUSE_KINDS"),
    "read_id": ("str", True, "the read that fired; null for a binomial fire at the run's end"),
    "launch_index": ("int", True, "that read's launch index; null with read_id"),
    "arms_in_scope": ("strs", False, "the arms the pause stands on while unadjudicated: its read's arm among them, "
                                     "no arm twice"),
    "adjudicated": ("bool", False, "the seat has ruled on it"),
    "ruling_sha256": ("sha256", True, "the ruling's raw, by sha256; null until adjudicated"),
    "binomial": ("binomial", True, "on a fidelity-binomial pause, or one whose read also fired the binomial "
                                   "(also_fired), the batch it was computed on, ending at the pause's read where it "
                                   "has one; null otherwise"),
    "also_fired": ("strs", False, "other kinds the same read fired, after kind in PAUSE_KINDS' precedence"),
    "resumed_at_launch_index": ("int", True, "the first read launched after the ruling took effect; null until "
                                             "then"),
}
BINOMIAL_FIELDS: dict[str, tuple[str, bool, str]] = {
    "first_launch_index": ("int", False, "the first read of the trials counted"),
    "last_launch_index": ("int", False, "the last read of the trials counted"),
    "k": ("int", False, "exceedances at TAU among the trials"),
    "n": ("int", False, "re-computations counted"),
    "p0_count": ("int", False, "the identity's fidelity_rule.p0_count"),
    "p0_n": ("int", False, "the identity's fidelity_rule.p0_n"),
    "alpha": ("float", False, "the lock's alpha for the binomial"),
}
STOP_FIELDS: dict[str, tuple[str, bool, str]] = {
    "kind": ("str", False, "STOP_KINDS"),
    "record_sha256": ("sha256", False, "the STOP's record (G-VER's report; the PI's stop raw), by sha256"),
    "detail": ("str", False, "one line of at most 200 characters, no margin, no id beyond a session's"),
}
BINOMIAL_STATE_FIELDS: dict[str, tuple[str, bool, str]] = {
    "trials": ("int", False, "re-computations counted by the binomial so far: the fidelity counters' total"),
    "exceed_tau": ("int", False, "their exceedances at TAU: the fidelity counters' total"),
    "evaluations": ("int", False, "cadence evaluations made, the end-of-run one included"),
    "fires": ("int", False, "evaluations that fired; each is a pause's binomial (its kind or also_fired)"),
}
CAP_FIELDS: dict[str, tuple[str, bool, str]] = {
    "hour_cap_ms": ("int", True, "the lock's cap in ms; null where none is set"),
    "used_ms": ("int", False, "the sum of the stage's records' duration_ms"),
    "hit": ("bool", False, "hour_cap_ms is set and used_ms >= hour_cap_ms"),
    "loads_ms": ("ints", False, "each invocation's model-load wall-clock in ms, in invocation order: reported beside "
                                "the cap, outside it"),
}
COUNTERS_FIELDS: dict[str, tuple[str, bool, str]] = {
    "fidelity": ("fid_counts", False, "'arm|dose' -> {trials, exceed_tau, exceed_tau4}"),
    "nonfinite_reads": ("int", False, "records with a non-finite margin, cached or fresh (finite false on either "
                                      "path); at least the pauses that name nonfinite"),
    "identity_out_of_bound": ("int", False, "records whose identity check is not within; at least the pauses that "
                                            "name identity-bound"),
    "rendering_mismatches": ("int", False, "token sequences refused before a read, never a record: the number of "
                                           "the stage's rendering pauses, or at a G-VER-STOP G-VER's mismatches, at "
                                           "least one"),
    "label_mass_below_floor": ("int_by_key", True, "'arm|dose' -> count under the lock's floor; null where no floor "
                                                   "is set"),
}
GREAD_FIELDS: dict[str, tuple[str, bool, str]] = {
    "schema": ("str", False, "GREAD_SCHEMA"),
    "campaign": ("gread_campaign", False, "{read_plan_sha256, stage_identity_sha256, cells}: what it read"),
    "probe": ("gread_probe", False, "{package_sha256, lr, shuffles, shuffle_seed, cv, cv_seed, layers, bar}"),
    "results": ("gread_results", False, "at least one, and at most one per (axis, point) of GREAD_AXES"),
}
GREAD_CAMPAIGN_FIELDS: dict[str, tuple[str, bool, str]] = {
    "read_plan_sha256": ("sha256", False, "the campaign's"),
    "stage_identity_sha256": ("sha256", False, "the campaign's"),
    "cells": ("cell_shas2", False, "cell filename -> {json_sha256, capture_sha256}, the cells read"),
}
GREAD_PROBE_FIELDS: dict[str, tuple[str, bool, str]] = {
    "package_sha256": ("sha256", False, "the n package at the run"),
    "lr": ("lr", False, "{seed, iters, rate, l2}: k's fit_lr hyperparameters, GREAD_LR"),
    "shuffles": ("int", False, "200 (n §3)"),
    "shuffle_seed": ("int", False, "the label-shuffle null's seed"),
    "cv": ("str", False, "'kfold10': grouped 10-fold CV by session (ADDENDUM-n1 §6.3)"),
    "cv_seed": ("int", False, "the folds' seed, the lock's"),
    "layers": ("ints", False, "the capture layers probed"),
    "bar": ("float", False, "0.90 (n §3)"),
}
GREAD_RESULT_FIELDS: dict[str, tuple[str, bool, str]] = {
    "axis": ("str", False, "'valence' or 'span_reward'"),
    "dose_label": ("str", False, "the kept label"),
    "merged": ("strs", False, "the labels merged into it"),
    "contrast": ("str", False, "'pole' (+ against -, valence at +1) or 'shadow' (+ against the shadow)"),
    "status": ("str", False, "GREAD_STATUSES"),
    "band_median_auc": ("float", True, "median over per_layer's AUCs; null when not computed"),
    "per_layer": ("layer_results", False, "[{layer, auc, null_p95, above_null}] in the probe's layer order; [] when "
                                          "not computed"),
    "comparator": ("comparator", False, "{band_medians (24, the random directions'), max}; nulls when not computed, "
                                        "and a computed result with nulls is a FAIL"),
    "bar": ("float", False, "0.90"),
}


def identity_sha256(identity: Mapping[str, Any]) -> str:
    """sha256 of the identity's canonical JSON (sort_keys, separators (",", ":"), ensure_ascii False, UTF-8), as
    settled with n-analyzer; on a valid identity, byte-equal to m's ``resume._canon``."""
    return hashlib.sha256(json.dumps(identity, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                                     allow_nan=False).encode("utf-8")).hexdigest()


def _check_report_nested(t: str, v: Any, where: str) -> None:
    if t == "per_arm":
        if type(v) is not dict or not v:
            _fail(where, "expected a non-empty object")
        for arm, x in v.items():
            if arm not in ARMS or type(x) is not dict or sorted(x) != ["complete", "obtained", "planned"]:
                _fail(f"{where}.{arm}", "is not an arm's {planned, obtained, complete}")
            if not (_is_int(x["planned"]) and _is_int(x["obtained"]) and type(x["complete"]) is bool):
                _fail(f"{where}.{arm}", "types")
            if not 0 <= x["obtained"] <= x["planned"] or x["complete"] != (x["obtained"] == x["planned"]):
                _fail(f"{where}.{arm}", "obtained exceeds planned, or complete is not obtained == planned")
    elif t in ("cell_shas", "cell_shas2"):
        keys = ["capture_sha256", "json_sha256"] + (["records"] if t == "cell_shas" else [])
        if type(v) is not dict:
            _fail(where, "expected an object")
        for name, x in v.items():
            if name not in VALID_CELL_NAMES:
                _fail(f"{where}", f"{name!r} is not a cell file a stage can hold (cell_filename over ARM_CELLS "
                                  f"and KEEPER_CANDIDATES)")
            if type(x) is not dict or sorted(x) != sorted(keys):
                _fail(f"{where}.{name}", f"keys are not {keys}")
            for k, tk in (("json_sha256", "sha256"), ("capture_sha256", "layer_sha256")):
                _check_type(tk, x[k], f"{where}.{name}.{k}")
            if t == "cell_shas" and not (_is_int(x["records"]) and x["records"] >= 0):
                _fail(f"{where}.{name}.records", "is not a count")
    elif t == "pauses":
        if type(v) is not list:
            _fail(where, "expected a list")
        for i, p in enumerate(v):
            _check_table(p, PAUSE_FIELDS, f"{where}[{i}]")
    elif t == "binomial":
        _check_table(v, BINOMIAL_FIELDS, where)
    elif t == "binomial_state":
        _check_table(v, BINOMIAL_STATE_FIELDS, where)
        if not (0 <= v["exceed_tau"] <= v["trials"] and 0 <= v["fires"] <= v["evaluations"]):
            _fail(where, "needs exceed_tau <= trials and fires <= evaluations")
    elif t == "stop":
        _check_table(v, STOP_FIELDS, where)
    elif t == "cap":
        _check_table(v, CAP_FIELDS, where)
    elif t == "counters":
        _check_table(v, COUNTERS_FIELDS, where)
    elif t == "fid_counts":
        if type(v) is not dict:
            _fail(where, "expected an object")
        for key, x in v.items():
            if type(x) is not dict or sorted(x) != ["exceed_tau", "exceed_tau4", "trials"] or not all(
                    _is_int(x[k]) and x[k] >= 0 for k in x):
                _fail(f"{where}.{key}", "is not {trials, exceed_tau, exceed_tau4} counts")
            if not x["exceed_tau"] <= x["exceed_tau4"] <= x["trials"]:
                _fail(f"{where}.{key}", "needs exceed_tau <= exceed_tau4 <= trials (rel > TAU implies rel > TAU/4)")
    elif t == "int_by_key":
        if type(v) is not dict or not all(type(k) is str and _is_int(x) and x >= 0 for k, x in v.items()):
            _fail(where, "expected 'arm|dose' -> count")
    elif t == "strs":
        if type(v) is not list or not all(type(x) is str for x in v):
            _fail(where, "expected a list of strings")
    elif t == "gread_campaign":
        _check_table(v, GREAD_CAMPAIGN_FIELDS, where)
    elif t == "gread_probe":
        _check_table(v, GREAD_PROBE_FIELDS, where)
    elif t == "lr":
        if (type(v) is not dict or sorted(v) != ["iters", "l2", "rate", "seed"] or not _is_int(v["seed"])
                or not _is_int(v["iters"]) or not _is_float(v["rate"]) or not _is_float(v["l2"])):
            _fail(where, "expected {seed, iters, rate, l2}")
    elif t == "gread_results":
        if type(v) is not list or not v:
            _fail(where, "expected a non-empty list")
        for i, r in enumerate(v):
            _check_table(r, GREAD_RESULT_FIELDS, f"{where}[{i}]")
    elif t == "layer_results":
        if type(v) is not list:
            _fail(where, "expected a list")
        for i, x in enumerate(v):
            if (type(x) is not dict or sorted(x) != ["above_null", "auc", "layer", "null_p95"] or not _is_int(
                    x["layer"]) or not _is_float(x["auc"]) or not _is_float(x["null_p95"])
                    or type(x["above_null"]) is not bool):
                _fail(f"{where}[{i}]", "is not {layer, auc, null_p95, above_null}")
            if x["above_null"] != (x["auc"] > x["null_p95"]):
                _fail(f"{where}[{i}].above_null", "is not auc > null_p95")
    elif t == "comparator":
        if type(v) is not dict or sorted(v) != ["band_medians", "max"]:
            _fail(where, "expected {band_medians, max}")
        bm, mx = v["band_medians"], v["max"]
        if (bm is None) != (mx is None):
            _fail(where, "band_medians and max are null together")
        if bm is not None:
            if type(bm) is not list or len(bm) != N_RANDOM or not all(_is_float(x) for x in bm):
                _fail(f"{where}.band_medians", f"expected {N_RANDOM} floats")
            if not _is_float(mx) or mx != max(bm):
                _fail(f"{where}.max", "is not max(band_medians)")
    else:
        _fail(where, f"unknown type {t!r}")


for _t in ("per_arm", "cell_shas", "cell_shas2", "pauses", "binomial", "binomial_state", "stop", "cap", "counters",
           "fid_counts",
           "int_by_key", "strs", "gread_campaign", "gread_probe", "lr", "gread_results", "layer_results",
           "comparator"):
    NESTED[_t] = (lambda t: (lambda v, w: _check_report_nested(t, v, w)))(_t)
del _t


def check_report(report: Any, where: str = "report") -> None:
    """A stage report: every field, and the invariants one report carries on its own. That its cells and counts are
    the cells' on disk is the reader's to check (n-analyzer's verdicts command binds them by sha256)."""
    _check_table(report, REPORT_FIELDS, where)
    w = lambda f: f"{where}.{f}"                                          # noqa: E731
    if report["schema"] != REPORT_SCHEMA:
        _fail(w("schema"), f"is {report['schema']!r}")
    ident = report["stage_identity"]
    check_stage_identity(ident, w("stage_identity"))
    if report["stage_identity_sha256"] != identity_sha256(ident):
        _fail(w("stage_identity_sha256"), "is not identity_sha256(stage_identity)")
    campaign = ident["stage"] == "campaign"
    want_plan = read_plan_sha256(ident) if campaign else None
    if report["read_plan_sha256"] != want_plan:
        _fail(w("read_plan_sha256"), "is the campaign's read_plan_sha256 there, null elsewhere")
    end = report["end_state"]
    if end not in END_STATES:
        _fail(w("end_state"), f"{end!r} is not one of {END_STATES}")
    per = report["per_arm"]
    if campaign:
        plan = read_plan(ident)
        planned = {a: sum(1 for x in plan if x.startswith(a + "|")) for a in ARMS}
        if sorted(per) != sorted(ARMS) or any(per[a]["planned"] != planned[a] for a in ARMS):
            _fail(w("per_arm"), "is not the plan's arms and counts")
    obtained: dict = {}
    allowed = {(a, d, y) for a in ARMS for d, ys in arm_cells(a, ident) for y in ys}
    want_layers = sorted(str(c) for c in ident["capture_layers"])
    for name, x in report["cells"].items():
        arm, did, dl = _CELL_KEYS[name]
        if arm not in per:
            _fail(w("per_arm"), f"has no entry for {arm}, which cell {name} belongs to")
        if (arm, did, dl) not in allowed:
            _fail(w("cells"), f"{name} is at {dl}, a point the stage's dose map does not keep for {arm} "
                              f"(arm_cells)")
        if sorted(x["capture_sha256"]) != want_layers:
            _fail(w(f"cells.{name}.capture_sha256"), "must hash exactly the identity's capture layers")
        obtained[arm] = obtained.get(arm, 0) + x["records"]
    for a, x in per.items():
        if x["obtained"] != obtained.get(a, 0):
            _fail(w(f"per_arm.{a}.obtained"), "is not the sum of its cells' records")
    standing = False
    binomial_pauses = 0
    bs = report["binomial_state"]
    last, last_rendering = -1, False
    n_pauses = len(report["pauses"])
    for i, p in enumerate(report["pauses"]):
        wp = w(f"pauses[{i}]")
        if p["pause_id"] != f"p{i + 1:02d}":
            _fail(f"{wp}.pause_id", f"is not 'p{i + 1:02d}': pause ids run p01, p02, ... in the list's order")
        if p["kind"] not in PAUSE_KINDS:
            _fail(f"{wp}.kind", f"{p['kind']!r} is not one of {PAUSE_KINDS}")
        also = p["also_fired"]
        if (len(set(also)) != len(also) or any(k not in PAUSE_KINDS for k in also)
                or any(PAUSE_KINDS.index(k) <= PAUSE_KINDS.index(p["kind"]) for k in also)):
            _fail(f"{wp}.also_fired", "names a non-kind, a repeat, or a kind not after kind in PAUSE_KINDS' order")
        if p["kind"] == "rendering" and also:
            _fail(f"{wp}.also_fired", "a rendering pause's read is not launched, so nothing else fires with it")
        if not p["arms_in_scope"] or any(a not in ARMS for a in p["arms_in_scope"]):
            _fail(f"{wp}.arms_in_scope", "names no arm, or a non-arm")
        if len(set(p["arms_in_scope"])) != len(p["arms_in_scope"]):
            _fail(f"{wp}.arms_in_scope", "names an arm twice")
        if p["read_id"] is not None and p["read_id"].split("|")[0] not in p["arms_in_scope"]:
            _fail(f"{wp}.arms_in_scope", "does not hold the arm of the pause's read")
        if ("identity-bound" in [p["kind"]] + list(also) and p["read_id"] is not None
                and p["read_id"].split("|")[2:3] != ["0"]):
            _fail(wp, "an identity-bound trigger is a d = 0 read's (n §6: \"the identity bound exceeded at d = 0\")")
        if (p["read_id"] is None) != (p["launch_index"] is None):
            _fail(wp, "read_id and launch_index are null together")
        if p["read_id"] is None and p["kind"] != "fidelity-binomial":
            _fail(wp, "only a binomial fire at the run's end has no read")
        li = p["launch_index"]
        if li is None and i != n_pauses - 1:
            _fail(wp, "a binomial fire at the run's end is the stage's last pause")
        if li is not None:
            if li < last or (li == last and not last_rendering):
                _fail(f"{wp}.launch_index", "pauses are not in launch order (only a rendering pause's place is "
                                             "shared, by its read launched there after the ruling)")
            last, last_rendering = li, p["kind"] == "rendering"
        if (p["ruling_sha256"] is None) == p["adjudicated"]:
            _fail(f"{wp}.ruling_sha256", "is set exactly when adjudicated")
        ra = p["resumed_at_launch_index"]
        if ra is not None and (not p["adjudicated"] or li is None or ra < li
                               or (ra == li and p["kind"] != "rendering")):
            _fail(f"{wp}.resumed_at_launch_index", "is set only after the ruling, at a launch after the pause's "
                                                   "read (at it, for a rendering pause); never on a read-less pause")
        fired_binomial = p["kind"] == "fidelity-binomial" or "fidelity-binomial" in also
        if (p["binomial"] is None) == fired_binomial:
            _fail(f"{wp}.binomial", "is set exactly when the pause's read fired the binomial (its kind or "
                                    "also_fired)")
        b = p["binomial"]
        if b is not None:
            binomial_pauses += 1
            fr = ident["fidelity_rule"]
            if not (b["first_launch_index"] <= b["last_launch_index"] and 0 <= b["k"] <= b["n"] and b["n"] > 0
                    and b["p0_count"] == fr["p0_count"] and b["p0_n"] == fr["p0_n"] and 0.0 < b["alpha"] < 1.0):
                _fail(f"{wp}.binomial", "is not a well-formed batch under the identity's p0")
            if li is not None and b["last_launch_index"] != li:
                _fail(f"{wp}.binomial.last_launch_index", "a fire at a read ends its batch at that read")
            if b["k"] > bs["exceed_tau"] or b["n"] > bs["trials"]:
                _fail(f"{wp}.binomial", "counts more exceedances or trials than the stage's binomial state")
        standing = standing or not p["adjudicated"]
    if bs["fires"] != binomial_pauses:
        _fail(w("binomial_state.fires"), "is not the number of pauses whose read fired the binomial")
    fid = report["counters"]["fidelity"]
    if (bs["trials"] != sum(x["trials"] for x in fid.values())
            or bs["exceed_tau"] != sum(x["exceed_tau"] for x in fid.values())):
        _fail(w("binomial_state"), "its trials and exceedances are not the fidelity counters' totals")
    stop = report["stop"]
    if (stop is not None) != (end in STOP_KINDS) or (stop is not None and stop["kind"] != end):
        _fail(w("stop"), "is set exactly at G-VER-STOP or PI-STOP, with that kind")
    if stop is not None and ("\n" in stop["detail"] or len(stop["detail"]) > 200):
        _fail(w("stop.detail"), "is one line of at most 200 characters")
    cap = report["cap"]
    if cap["used_ms"] < 0 or (cap["hour_cap_ms"] is not None and cap["hour_cap_ms"] < 0):
        _fail(w("cap"), "a negative figure")
    if any(x < 0 for x in cap["loads_ms"]):
        _fail(w("cap.loads_ms"), "a negative load time")
    if cap["hit"] != (cap["hour_cap_ms"] is not None and cap["used_ms"] >= cap["hour_cap_ms"]):
        _fail(w("cap.hit"), "is not used_ms >= hour_cap_ms")
    # the end-state rules (the module docstring's THE STAGE REPORT)
    if end == "PAUSE" and not standing:
        _fail(w("end_state"), "is PAUSE only while an unadjudicated pause stands")
    if standing and end not in ("PAUSE", "PI-STOP"):
        _fail(w("end_state"), "a standing pause ends only by a ruling or under PI-STOP")
    if end == "CAP" and not cap["hit"]:
        _fail(w("end_state"), "is CAP only when the cap is hit")
    if cap["hit"] and not standing and end not in ("CAP", "PI-STOP", "G-VER-STOP"):
        _fail(w("end_state"), "a hit cap ends the stage as CAP, unless a pause stands or a STOP ended it")
    if end == "COMPLETE" and campaign and not all(x["complete"] for x in per.values()):
        _fail(w("end_state"), "COMPLETE with an incomplete arm")
    c = report["counters"]
    for k in ("nonfinite_reads", "identity_out_of_bound", "rendering_mismatches"):
        if c[k] < 0:
            _fail(w(f"counters.{k}"), "is negative")
    named = [[p["kind"]] + list(p["also_fired"]) for p in report["pauses"]]
    if end == "G-VER-STOP":
        if (c["rendering_mismatches"] < 1 or report["pauses"]
                or any(x["obtained"] for x in per.values())):
            _fail(w("end_state"), "a G-VER-STOP comes before any read: G-VER's mismatches (at least one), no pause, "
                                  "no record")
    elif c["rendering_mismatches"] != sum(1 for ks in named if ks[0] == "rendering"):
        _fail(w("counters.rendering_mismatches"), "is not the number of the stage's rendering pauses")
    if (c["nonfinite_reads"] < sum(1 for ks in named if "nonfinite" in ks)
            or c["identity_out_of_bound"] < sum(1 for ks in named if "identity-bound" in ks)):
        _fail(w("counters"), "counts fewer non-finite or identity-bound reads than the pauses that name them")


def check_gread(art: Any, where: str = "gread") -> None:
    """G-READ-n's artifact: every field, and its PASS rule, the seat's (ADDENDUM-n1 §6.4): band median >= bar and
    above the comparator's largest band median, with no per-layer condition."""
    _check_table(art, GREAD_FIELDS, where)
    w = lambda f: f"{where}.{f}"                                          # noqa: E731
    if art["schema"] != GREAD_SCHEMA:
        _fail(w("schema"), f"is {art['schema']!r}")
    pr = art["probe"]
    if pr["bar"] != GREAD_BAR or pr["shuffles"] != 200 or not pr["layers"]:
        _fail(w("probe"), "n §3's bar (0.90) and shuffle count (200); at least one layer")
    if pr["lr"] != GREAD_LR:
        _fail(w("probe.lr"), f"is not k's fit_lr hyperparameters {GREAD_LR}")
    if CV_FORMS.fullmatch(pr["cv"]) is None:
        _fail(w("probe.cv"), f"{pr['cv']!r} is not 'kfold10' (ADDENDUM-n1 §6.3's grouped 10-fold CV by session)")
    seen = set()
    for i, r in enumerate(art["results"]):
        wr = w(f"results[{i}]")
        if r["axis"] not in GREAD_AXES or r["dose_label"] not in GREAD_AXES[r["axis"]]:
            _fail(wr, f"no G-READ-n result for ({r['axis']}, {r['dose_label']})")
        if (r["axis"], r["dose_label"]) in seen:
            _fail(wr, "repeats an (axis, dose point)")
        seen.add((r["axis"], r["dose_label"]))
        allowed_m = GREAD_MERGEABLE[r["axis"]]
        if (len(set(r["merged"])) != len(r["merged"]) or r["dose_label"] in r["merged"]
                or any(m not in allowed_m for m in r["merged"])):
            _fail(f"{wr}.merged", f"may name only {allowed_m}, once each, never the kept label")
        want_c = "pole" if (r["axis"], r["dose_label"]) == ("valence", "+1") else "shadow"
        if r["contrast"] != want_c:
            _fail(f"{wr}.contrast", f"should be {want_c!r} (n §3: the - pole where it is read, else the shadow)")
        if r["status"] not in GREAD_STATUSES or r["bar"] != GREAD_BAR:
            _fail(wr, "status or bar")
        computed = r["status"] != "NOT-COMPUTED"
        if not computed and r["comparator"]["band_medians"] is not None:
            _fail(f"{wr}.comparator", "a NOT-COMPUTED result carries no comparator")
        if computed != (r["band_median_auc"] is not None) or computed != bool(r["per_layer"]):
            _fail(wr, "a computed result has a band median and per-layer AUCs; a NOT-COMPUTED one has neither")
        if computed:
            if [x["layer"] for x in r["per_layer"]] != list(pr["layers"]):
                _fail(f"{wr}.per_layer", "is not the probe's layers, in order")
            aucs = sorted(x["auc"] for x in r["per_layer"])
            mid = len(aucs) // 2
            med = aucs[mid] if len(aucs) % 2 else (aucs[mid - 1] + aucs[mid]) / 2.0
            if r["band_median_auc"] != med:
                _fail(f"{wr}.band_median_auc", "is not the median of per_layer's AUCs")
            cm = r["comparator"]["max"]
            passed = cm is not None and med >= GREAD_BAR and med > cm
            if r["status"] != ("PASS" if passed else "FAIL"):
                _fail(f"{wr}.status", f"should be {'PASS' if passed else 'FAIL'}")


__all__ = [
    "RECORD_SCHEMA", "CELL_SCHEMA", "UNIT", "STAGES", "PROPOSAL_SHA256", "SESSION_SET_SHA256", "TAU", "TAU4",
    "RHO", "MERGE_DISTANCE", "MAX_WINDOW", "DOSE_RULE_LABELS", "dose_points",
    "BK_CELLS", "N_SESSIONS", "N_FLOOR", "N_RANDOM", "ARMS", "RANDOM_IDS", "DIRECTION_IDS", "DOSES",
    "DOSE_SLUGS", "ARM_CELLS", "ARM_SPAN_KIND", "TOLD_VARIANT", "TOLD_LINE", "SHAM_LINE", "FIDELITY_REASONS",
    "RECORD_FIELDS", "RESTRICTED_FIELDS", "CAPTURE_FIELDS", "FIDELITY_FIELDS", "IDENTITY_CHECK_FIELDS",
    "CELL_FIELDS", "STAGE_IDENTITY_FIELDS", "DOSE_MAP_FIELDS", "FIDELITY_RULE_FIELDS", "SchemaError",
    "read_id", "session_id", "shadow_read_id", "cell_filename", "expected_alpha", "fidelity_numbers",
    "shared_prefix", "bk_cell_of", "read_plan", "read_plan_sha256", "dose_point_values", "check_stage_identity",
    "check_record", "check_cell", "example_identity", "example_record", "example_cell",
    "REPORT_SCHEMA", "GREAD_SCHEMA", "END_STATES", "PAUSE_KINDS", "STOP_KINDS", "GREAD_AXES", "GREAD_STATUSES",
    "GREAD_BAR", "REPORT_FIELDS", "PAUSE_FIELDS", "BINOMIAL_FIELDS", "STOP_FIELDS", "CAP_FIELDS", "COUNTERS_FIELDS",
    "GREAD_FIELDS", "GREAD_CAMPAIGN_FIELDS", "GREAD_PROBE_FIELDS", "GREAD_RESULT_FIELDS", "identity_sha256",
    "check_report", "check_gread", "example_report", "example_pause", "example_gread", "BINOMIAL_STATE_FIELDS",
    "VALID_CELL_NAMES", "CV_FORMS", "GREAD_MERGEABLE", "GREAD_LR",
    "KEEPER_CANDIDATES", "keeper", "arm_cells", "capture_filename", "capture_capacity",
]


# --- example builders: literal, valid objects for self-tests and the analyzer's battery ---------------------
# No production path calls these. Every value is a literal or follows from this module's own helpers, so an
# object they return passes the checks above; a battery that edits one re-checks it.
def example_identity(stage: str = "campaign", *, R: float = 25.5, R_ell: float = 23.90625) -> dict:
    """A stage identity with placeholder digests and a dose map computed by the map's own formulas and merge rule
    (the defaults give d_eq = 0.3125 and d_20 = 0.625, nothing merged; R_ell = 50.0 merges +d_20 into +1, 40.0
    merges +d_20 into +1 and +d_eq into +1/2); at backend-ext the lock, dose map, directions and bound are absent,
    as there."""
    pre = stage == "backend-ext"
    d_eq = (0.10 * R_ell) / (RHO * R)
    d_20 = min(1.0, 2.0 * d_eq)
    dirs = {"valence": "a" * 16, "span_reward": "b" * 16, "span_sentiment": "c" * 16, "span_character": "d" * 16}
    dirs.update({r: f"{i + 1:016x}" for i, r in enumerate(RANDOM_IDS)})
    return {
        "unit": UNIT, "stage": stage, "record_schema": RECORD_SCHEMA, "proposal_sha256": PROPOSAL_SHA256,
        "lock_sha256": None if pre else "1" * 64, "package_sha256": "2" * 64,
        "imported_sha256": {"valence_core/m/resume.py": "3" * 64, "valence_core/adapters/olmo_hf.py": "4" * 64},
        "weights_sha256": "5" * 64, "backend_identifier": "6" * 16, "pod_id": "example-pod",
        "session_set_sha256": SESSION_SET_SHA256, "rendering_id": "example-rendering",
        "label_convention": "example-labels", "layer_bk": 32, "layer": 31, "capture_layers": list(range(32, 64)),
        "n_layers": 64, "d_model": 5120, "read_window": MAX_WINDOW,
        "dose_map": None if pre else {"rho": RHO, "R": R, "R_ell": R_ell, "d_eq": d_eq, "d_20": d_20,
                                      "points": dose_points(d_eq, d_20)},
        "directions": {} if pre else dirs,
        "fidelity_rule": {"tau": TAU, "p0_count": 0, "p0_n": 2400, "cadence": 160, "sample_key": "n-fid|{s}",
                          "sample_rule": "example"},
        "identity_bound": None if pre else 0.0,
    }


def example_record(identity: Mapping[str, Any], arm: str, direction_id: str, dose_label: str, run: int, *,
                   launch: int = 0, row: int = 0, fidelity: str | None = "auto", fresh_shift: float = 0.0,
                   zone: str = "S", logprob_S_tokens: list | None = None, logprob_U_tokens: list | None = None,
                   present_first_is_S: bool = False, cues: tuple = ("Zone W6", "Zone H0"),
                   finite: bool = True) -> dict:
    """A valid read record for ``identity``. The labels are three tokens each sharing their first; the
    log-probability tokens default to fixed literals and may be given (non-positive floats, three each), which
    sets the margin; ``fresh_shift`` moves the fresh path's logprob_S (a fidelity difference); ``fidelity="auto"``
    re-computes at d in {0, +1, -1}, None takes none, "sample" marks the campaign's keyed sample and "timing"
    G-TIME-n's re-computation at another point; ``finite=False`` writes a
    non-finite read (nulls, a non-finite re-computation where one is taken)."""
    did, dl = direction_id, dose_label
    cell = bk_cell_of(run)
    sid = session_id(cell, run)
    cs, cu = cues
    present = [cs, cu] if present_first_is_S else [cu, cs]
    scale, sign, _fixed = DOSES[dl]
    value = dose_point_values(identity)[dl]
    steered = sign != 0
    turns = [[i * 102, (i + 1) * 102, cs if i % 2 == 0 else cu] for i in range(12)]
    spans = [] if not steered else (turns if ARM_SPAN_KIND[arm] == "SU" else [t for t in turns if t[2] == cs])
    seq_len = 1273
    rp = seq_len - 1
    ls, lu = [57, 101, 7], [57, 202, 8]
    ts = list(logprob_S_tokens) if logprob_S_tokens is not None else [-0.5, -1.25, -0.125]
    tu = list(logprob_U_tokens) if logprob_U_tokens is not None else [-0.5, -3.0, -0.25]
    lps, lpu = math.fsum(ts), math.fsum(tu)
    margin = lps - lpu
    layers = [str(x) for x in identity["capture_layers"]]
    rec = {
        "schema": RECORD_SCHEMA, "read_id": read_id(arm, did, dl, sid), "launch_index": launch, "arm": arm,
        "session_id": sid, "bk_cell": cell, "bk_run": run, "cue_S": cs, "cue_U": cu, "present": present,
        "present_first_is_S": present_first_is_S, "direction_id": did,
        "direction_sha16": identity["directions"][did] if steered else None, "dose_label": dl,
        "dose_scale": scale, "dose_value": value, "sign": sign,
        "alpha": expected_alpha(dl, value, identity["dose_map"]) if steered else 0.0,
        "layer": identity["layer"] if steered else None, "steered_spans": spans,
        "n_steered": sum(b - a for a, b, _ in spans), "mask_sha16": "7" * 16,
        "retention_interval": rp - (spans[-1][1] - 1) if steered else None,
        "shadow_read_id": shadow_read_id(sid) if steered else None,
        "told_variant": TOLD_VARIANT.get(arm), "schedule_zone": zone if arm in TOLD_VARIANT else None,
        "told_line": ((TOLD_LINE.format(zone=cs if zone == "S" else cu) if arm == "N4-T" else SHAM_LINE)
                      if arm in TOLD_VARIANT else None),
        "seq_len": seq_len, "read_position": rp, "ids_sha": "8" * 16,
        "ids_sha_bk": None if arm in TOLD_VARIANT else "8" * 16, "label_ids_S": ls, "label_ids_U": lu,
        "finite": True, "logprob_S_tokens": ts, "logprob_U_tokens": tu, "logprob_S": lps, "logprob_U": lpu,
        "margin": margin,
        "restricted": {"k": 1, "tok_S": 101, "tok_U": 202, "p_S": 0.75, "p_U": 0.25, "label_mass": 0.5,
                       "pick": "S", "top1_id": 101, "top1_is_label": True},
        "capture": {"row": row, "sha16": {x: "9" * 16 for x in layers}},
        "fidelity": None, "identity": None, "duration_ms": 412, "duration_ms_fresh": None,
    }
    if fidelity == "auto":
        fidelity = "dose-rule" if dl in DOSE_RULE_LABELS else None
    if fidelity is not None:
        rec["fidelity"] = {"reason": fidelity, "finite": True, "fresh_logprob_S": lps + fresh_shift,
                           "fresh_logprob_U": lpu, "fresh_margin": (lps + fresh_shift) - lpu,
                           "fresh_capture_sha16": {x: "9" * 16 for x in layers},
                           "fresh_capture_sha16_U": {x: "9" * 16 for x in layers}}
        rec["fidelity"].update(fidelity_numbers(margin, lps, lpu, rec["fidelity"]["fresh_margin"]))
        rec["duration_ms_fresh"] = 150
    if not finite:
        for k in ("logprob_S_tokens", "logprob_U_tokens", "logprob_S", "logprob_U", "margin", "restricted"):
            rec[k] = None
        rec["finite"] = False
        if rec["fidelity"] is not None:
            for k in ("fresh_logprob_S", "fresh_logprob_U", "fresh_margin", "absdiff", "scale", "rel",
                      "exceeds_tau", "exceeds_tau4", "fresh_capture_sha16", "fresh_capture_sha16_U"):
                rec["fidelity"][k] = None
            rec["fidelity"]["finite"] = False
    if not steered and rec["fidelity"] is not None and identity["stage"] != "backend-ext":
        a = rec["fidelity"]["absdiff"]
        rec["identity"] = {"bound": identity["identity_bound"],
                           "within": a is not None and a <= identity["identity_bound"]}
    return rec


def example_cell(identity: Mapping[str, Any], arm: str, direction_id: str, dose_label: str,
                 runs: list[int]) -> dict:
    """A valid cell of ``example_record``s over ``runs``, launch indices 0, 10, 20, ..."""
    recs = [example_record(identity, arm, direction_id, dose_label, r, launch=10 * i, row=i)
            for i, r in enumerate(runs)]
    name = cell_filename(arm, direction_id, dose_label)
    layers = identity["capture_layers"]
    return {"schema": CELL_SCHEMA, "stage_identity": identity, "arm": arm, "direction_id": direction_id,
            "dose_label": dose_label, "records": recs,
            "capture_files": {str(x): capture_filename(name, x) for x in layers}, "capture_rows": len(recs),
            "capture_sha256": {str(x): "c" * 64 for x in layers}}


def example_report(identity: Mapping[str, Any], *, end_state: str = "COMPLETE", obtained_fraction: float = 1.0,
                   pauses: list | None = None, stop: dict | None = None, hour_cap_ms: int | None = None,
                   used_ms: int = 1000, loads_ms: tuple = (5000,)) -> dict:
    """A valid report for ``identity``. At the campaign, every arm's cells carry ``obtained_fraction`` of its plan
    (records split over the arm's cells as the plan has them); elsewhere one N1-V d = 0 cell of 24 reads. ``pauses``,
    ``stop`` and the cap are taken as given; the end state must agree with them."""
    campaign = identity["stage"] == "campaign"
    band = [str(x) for x in identity["capture_layers"]]
    cells: dict = {}
    per_arm: dict = {}
    if campaign:
        plan = read_plan(identity)
        by_cell: dict = {}
        for rid in plan:
            arm, did, dl, _sid = rid.split("|")
            by_cell.setdefault((arm, did, dl), []).append(rid)
        for (arm, did, dl), rids in sorted(by_cell.items()):
            got = len(rids) if obtained_fraction >= 1.0 else int(len(rids) * obtained_fraction)
            cells[cell_filename(arm, did, dl)] = {"json_sha256": "d" * 64,
                                                  "capture_sha256": {x: "e" * 64 for x in band}, "records": got}
            pa = per_arm.setdefault(arm, {"planned": 0, "obtained": 0, "complete": False})
            pa["planned"] += len(rids)
            pa["obtained"] += got
        for pa in per_arm.values():
            pa["complete"] = pa["obtained"] == pa["planned"]
    else:
        cells[cell_filename("N1-V", "none", "0")] = {"json_sha256": "d" * 64,
                                                      "capture_sha256": {x: "e" * 64 for x in band}, "records": 24}
        per_arm["N1-V"] = {"planned": 24, "obtained": 24, "complete": True}
    hit = hour_cap_ms is not None and used_ms >= hour_cap_ms
    batches = [p["binomial"] for p in (pauses or []) if p["binomial"] is not None]
    exc = max([b["k"] for b in batches], default=0)
    fid = {"N1-V|0": {"trials": 160, "exceed_tau": exc, "exceed_tau4": max(3, exc)}}
    named = [[p["kind"]] + list(p["also_fired"]) for p in (pauses or [])]
    counts = {"nonfinite_reads": sum(1 for ks in named if "nonfinite" in ks),
              "identity_out_of_bound": sum(1 for ks in named if "identity-bound" in ks),
              "rendering_mismatches": 1 if end_state == "G-VER-STOP" else sum(1 for ks in named
                                                                            if ks[0] == "rendering")}
    return {"schema": REPORT_SCHEMA, "stage_identity": dict(identity), "stage_identity_sha256":
            identity_sha256(identity), "read_plan_sha256": read_plan_sha256(identity) if campaign else None,
            "end_state": end_state, "per_arm": per_arm, "cells": cells, "pauses": list(pauses or []),
            "binomial_state": {"trials": 160, "exceed_tau": exc, "evaluations": max(1, len(batches)),
                               "fires": len(batches)},
            "stop": stop,
            "cap": {"hour_cap_ms": hour_cap_ms, "used_ms": used_ms, "hit": hit, "loads_ms": list(loads_ms)},
            "counters": {"fidelity": fid, **counts, "label_mass_below_floor": None}}


def example_pause(n: int, *, kind: str = "nonfinite", launch_index: int | None = 500, adjudicated: bool = False,
                  arms: tuple = ("N1-V",), also_fired: tuple = (), resumed_at: int | None = None) -> dict:
    """A valid pause record (for ``example_report``); its batch is set when the binomial fired at it, and its read is
    a d = 0 read when it names identity-bound."""
    binom = None
    if kind == "fidelity-binomial" or "fidelity-binomial" in also_fired:
        binom = {"first_launch_index": 0, "last_launch_index": 159 if launch_index is None else launch_index,
                 "k": 1, "n": 160, "p0_count": 0, "p0_n": 2400, "alpha": 0.01}
    d0 = "identity-bound" in (kind,) + tuple(also_fired)
    return {"pause_id": f"p{n:02d}", "kind": kind,
            "read_id": None if launch_index is None else ("N1-V|none|0|floor_b0/3" if d0
                                                          else "N1-V|valence|+1|floor_b0/3"),
            "launch_index": launch_index, "arms_in_scope": list(arms), "adjudicated": adjudicated,
            "ruling_sha256": "f" * 64 if adjudicated else None, "binomial": binom, "also_fired": list(also_fired),
            "resumed_at_launch_index": resumed_at}


def example_gread(*, statuses: Mapping | None = None, layers: tuple = tuple(range(32, 64))) -> dict:
    """A valid G-READ-n artifact: one result per (axis, point) of GREAD_AXES, each PASS unless ``statuses`` gives
    "FAIL" or "NOT-COMPUTED" for it (keyed "axis|label")."""
    statuses = dict(statuses or {})
    results = []
    for axis, labels in GREAD_AXES.items():
        for dl in labels:
            st = statuses.get(f"{axis}|{dl}", "PASS")
            if st == "NOT-COMPUTED":
                per, med, comp = [], None, {"band_medians": None, "max": None}
            else:
                auc = 0.96 if st == "PASS" else 0.62
                per = [{"layer": l, "auc": auc, "null_p95": 0.58, "above_null": auc > 0.58} for l in layers]
                med = auc
                comp = {"band_medians": [0.5 + 0.005 * i for i in range(N_RANDOM)], "max": 0.5 + 0.005 * 23}
            results.append({"axis": axis, "dose_label": dl, "merged": [],
                            "contrast": "pole" if (axis, dl) == ("valence", "+1") else "shadow", "status": st,
                            "band_median_auc": med, "per_layer": per, "comparator": comp, "bar": GREAD_BAR})
    return {"schema": GREAD_SCHEMA,
            "campaign": {"read_plan_sha256": "a" * 64, "stage_identity_sha256": "b" * 64,
                         "cells": {cell_filename("N1-V", "none", "0"): {"json_sha256": "d" * 64,
                                                                         "capture_sha256": {str(x): "e" * 64
                                                                                            for x in layers}}}},
            "probe": {"package_sha256": "2" * 64, "lr": {"seed": 7, "iters": 300, "rate": 0.1, "l2": 0.01},
                      "shuffles": 200, "shuffle_seed": 20260905, "layers": list(layers), "bar": GREAD_BAR,
                      "cv": "kfold10", "cv_seed": 20261116},
            "results": results}


# --- self-test (literal records; no file, no model) ---------------------------------------------------------

def _selftest(verbose: bool = False) -> tuple[int, int]:
    """Accept cases must pass every check; refuse cases are one targeted defect each in a valid object, made by one
    mutation step (some steps edit several coordinated fields, so that only the targeted check can refuse).
    ``verbose`` prints each refusal's message, so a case refused by a check other than the one it names can be
    seen."""
    import copy

    class _F(float):                      # a float subclass, as np.float64 is
        pass

    ok = total = 0
    ident = example_identity()

    def accept(name, fn):
        nonlocal ok, total
        total += 1
        try:
            fn()
            ok += 1
        except SchemaError as e:
            print(f"FAIL accept {name}: {e}")

    def refuse(name, base, mutate, check=None, expect=None):
        """``expect``: a fragment the refusal's message must hold, for a case built single-defect (its other fields
        coordinated), so a weakened targeted check cannot pass it by another check's refusal."""
        nonlocal ok, total
        total += 1
        obj = copy.deepcopy(base)
        mutate(obj)
        try:
            (check or (lambda o: check_record(o, ident)))(obj)
            print(f"FAIL refuse {name}: accepted")
        except SchemaError as e:
            if expect is not None and expect not in str(e):
                print(f"FAIL refuse {name}: refused by another check: {e}"[:300])
                return
            ok += 1
            if verbose:
                print(f"  refused  {name}  <-  {e}"[:220])

    good = {
        "N1-V +1": example_record(ident, "N1-V", "valence", "+1", 3),
        "N1-V 0": example_record(ident, "N1-V", "none", "0", 3),
        "N1-V +d_eq": example_record(ident, "N1-V", "valence", "+d_eq", 77),
        "N1-R +1/2": example_record(ident, "N1-R", "rand_05", "+1/2", 12, fidelity="sample"),
        "N1-R -1": example_record(ident, "N1-R", "rand_23", "-1", 39),
        "N1-P -1": example_record(ident, "N1-P", "valence", "-1", 150),
        "N2-E f0.20": example_record(ident, "N2-E", "span_reward", "f0.20", 41),
        "N2-C f0.10": example_record(ident, "N2-C", "span_character", "f0.10", 159),
        "N4-T": example_record(ident, "N4-T", "none", "0", 8, zone="U"),
        "N4-Ts": example_record(ident, "N4-Ts", "none", "0", 8),
    }
    for name, rec in good.items():
        accept(name, lambda rec=rec: check_record(rec, ident))
    accept("fidelity exceeding TAU is recorded, not refused",
           lambda: check_record(example_record(ident, "N1-V", "valence", "+1", 3, fresh_shift=0.5), ident))
    ext = example_identity("backend-ext")
    accept("backend-ext identity", lambda: check_stage_identity(ext))
    accept("backend-ext d = 0 read", lambda: check_record(example_record(ext, "N1-V", "none", "0", 3), ext))
    tim = example_identity("time")
    accept("a G-TIME-n d = 0 read without a re-computation (no identity block)",
           lambda: check_record(example_record(tim, "N1-V", "none", "0", 3, fidelity=None), tim))
    accept("a G-TIME-n d = 0 read with one (the identity block)",
           lambda: check_record(example_record(tim, "N1-V", "none", "0", 3), tim))
    accept("a G-TIME-n +1 read without a re-computation",
           lambda: check_record(example_record(tim, "N1-V", "valence", "+1", 3, fidelity=None), tim))
    accept("a G-TIME-n +1/2 read with a timing re-computation",
           lambda: check_record(example_record(tim, "N1-V", "valence", "+1/2", 3, fidelity="timing"), tim))
    nonfinite = example_record(ident, "N1-V", "valence", "-1", 3, finite=False)
    accept("a non-finite read is recorded with nulls", lambda: check_record(nonfinite, ident))
    accept("a non-finite shadow: identity not within",
           lambda: check_record(example_record(ident, "N1-V", "none", "0", 3, finite=False), ident))
    accept("given log-probs and present order", lambda: check_record(example_record(
        ident, "N2-S", "span_sentiment", "f0.10", 99, logprob_S_tokens=[-0.25, -4.0, -0.5],
        logprob_U_tokens=[-0.25, -0.75, -0.125], present_first_is_S=True, cues=("Zone K7", "Zone M2")), ident))
    merged = example_identity(R_ell=50.0)
    double = example_identity(R_ell=40.0)

    def _merges() -> None:
        lab = lambda ident_: [(p["label"], p["merged"]) for p in ident_["dose_map"]["points"]]  # noqa: E731
        if ident["dose_map"]["d_eq"] != 0.3125 or ident["dose_map"]["d_20"] != 0.625:
            raise SchemaError(f"example d_eq / d_20 are {ident['dose_map']['d_eq']!r} / {ident['dose_map']['d_20']!r}")
        want = {
            "none": [("+1", []), ("+1/2", []), ("+d_20", []), ("+d_eq", []), ("-1", []), ("f0.10", []),
                     ("f0.20", [])],
            "d_20 into +1": [("+1", ["+d_20"]), ("+1/2", []), ("+d_eq", []), ("-1", []), ("f0.10", []),
                             ("f0.20", [])],
            "both": [("+1", ["+d_20"]), ("+1/2", ["+d_eq"]), ("-1", []), ("f0.10", []), ("f0.20", [])],
        }
        got = {"none": lab(ident), "d_20 into +1": lab(merged), "both": lab(double)}
        if got != want:
            raise SchemaError(f"merges {got}")
        for x in (ident, merged, double):
            check_stage_identity(x)
        cases = [  # (d_eq, d_20) -> labels kept / merged, by the rule's letter
            ((0.3, 0.546875), [("+1", []), ("+1/2", ["+d_20"]), ("+d_eq", []), ("-1", []), ("f0.10", []),
                               ("f0.20", [])]),                    # 0.046875 <= 0.05: folded
            ((0.3, 0.55), [("+1", []), ("+1/2", []), ("+d_20", []), ("+d_eq", []), ("-1", []), ("f0.10", []),
                           ("f0.20", [])]),                        # 0.55 - 0.5 is 0.050000000000000044 > 0.05
            ((0.53125, 0.5625), [("+1", []), ("+1/2", ["+d_eq"]), ("+d_20", []), ("-1", []), ("f0.10", []),
                                 ("f0.20", [])]),                  # an exact tie goes to the earlier candidate
            ((0.6, 0.625), [("+1", []), ("+1/2", []), ("+d_20", ["+d_eq"]), ("-1", []), ("f0.10", []),
                            ("f0.20", [])]),                       # d_eq folds into a kept +d_20
        ]
        for (de, d2), want_pts in cases:
            got_pts = [(p["label"], p["merged"]) for p in dose_points(de, d2)]
            if got_pts != want_pts:
                raise SchemaError(f"dose_points({de}, {d2}) = {got_pts}")
        try:
            dose_points(0.04, 0.08)
        except SchemaError:
            return
        raise SchemaError("a point folding into d = 0 was accepted")
    accept("the merge rule (n §2.3, as settled with n-analyzer)", _merges)
    cell = example_cell(ident, "N1-V", "valence", "+1", [0, 1, 2])
    accept("cell", lambda: check_cell(cell))
    names = [cell_filename(a, d, x) for a in ARMS for d, xs in ARM_CELLS[a] for x in xs]

    def _cells() -> None:
        if len(names) != 138 or len(set(names)) != 138:
            raise SchemaError(f"{len(names)} cells, {len(set(names))} distinct names")
    accept("138 distinct cell files before merges (n §2.4; N1-P's row, ADDENDUM-n1 §5.2)", _cells)

    def _plan() -> None:
        plan = read_plan(ident)
        if len(plan) != 7680 or len(set(plan)) != 7680:
            raise SchemaError(f"the plan has {len(plan)} reads, {len(set(plan))} distinct, not 7,680 (n §2.4; "
                              "ADDENDUM-n1 §5.2)")
        per = {a: sum(1 for x in plan if x.startswith(a + "|")) for a in ARMS}
        want = {"N1-V": 960, "N1-R": 4800, "N1-P": 640, "N2-E": 320, "N2-S": 320, "N2-C": 320, "N4-T": 160,
                "N4-Ts": 160}
        if per != want:
            raise SchemaError(f"per-arm plan {per}")
        if any(x.startswith("N1-R|") and int(x.rsplit("/", 1)[1]) >= N_FLOOR for x in plan):
            raise SchemaError("N1-R planned off the floor sessions")
        pm = read_plan(merged)
        if len(pm) != 6400 or any("|+d_20|" in x for x in pm):
            raise SchemaError(f"the merged plan has {len(pm)} reads")
        pd = read_plan(double)
        if len(pd) != 5280 or any("|+d_20|" in x or "|+d_eq|" in x for x in pd):
            raise SchemaError(f"the doubly merged plan has {len(pd)} reads")
        half_ids = {read_id("N1-P", "valence", "+1/2", session_id(bk_cell_of(r), r)) for r in range(N_SESSIONS)}
        if not half_ids <= set(pd):
            raise SchemaError("the doubly merged plan lacks N1-P's +1/2 reads (+d_eq's keeper)")
        if read_plan_sha256(ident) != read_plan_sha256(example_identity()):
            raise SchemaError("the plan's sha256 is not deterministic")
    accept("the read plan: 7,680 reads by §2.4's table as ADDENDUM-n1 §5.2 amends N1-P's row, N1-P 640; 6,400 with "
           "+d_20 merged into +1; 5,280 with +d_eq also into +1/2, "
           "N1-P reading +1/2", _plan)
    p_half = example_record(double, "N1-P", "valence", "+1/2", 150)
    accept("an N1-P read at +1/2 under R_ell = 40.0 (+d_eq's keeper; ADDENDUM-n1 §5.1-§5.2)",
           lambda: check_record(p_half, double))

    def _plan_refuses() -> None:
        try:
            read_plan(ext)
        except SchemaError:
            return
        raise SchemaError("read_plan accepted a backend-ext identity")
    accept("read_plan refuses a stage other than the campaign", _plan_refuses)

    def _cells_of_runs() -> None:
        got = [bk_cell_of(r) for r in (0, 4, 5, 39, 40, 59, 60, 159)]
        want = ["floor_b0", "floor_b0", "floor_b1", "floor_b7", "neu_b0", "neu_b0", "neu_b1", "neu_b5"]
        if got != want:
            raise SchemaError(f"bk_cell_of {got}")
        for bad in (-1, 160):
            try:
                bk_cell_of(bad)
            except SchemaError:
                continue
            raise SchemaError(f"bk_cell_of accepted run {bad}")
    accept("bk_cell_of maps BK's runs to their files", _cells_of_runs)

    b = good["N1-V +1"]
    sh = good["N1-V 0"]
    n4 = good["N4-T"]
    np1 = good["N1-P -1"]
    def setk(k, v):
        return lambda o: o.__setitem__(k, v)
    refuse("an extra key", b, setk("delta_m", 0.5))
    refuse("a missing key", b, lambda o: o.pop("duration_ms"))
    refuse("a float subclass (np.float64's kind)", b, lambda o: o.__setitem__("alpha", _F(o["alpha"])))
    refuse("a bool where an int belongs", b, setk("sign", True))
    refuse("NaN", b, setk("margin", float("nan")))
    refuse("a read_id of another form", b, setk("read_id", "N1-V/valence/+1/floor_b0/3"))
    refuse("an arm reading a dose it does not read (N1-P at +1/2 under the default map; single-defect)", p_half,
           lambda o: None, expect="reads no")
    refuse("N1-R off the floor sessions", good["N1-R +1/2"], lambda o: (
        o.__setitem__("bk_run", 60), o.__setitem__("bk_cell", "neu_b1"),
        o.__setitem__("session_id", "neu_b1/60"),
        o.__setitem__("read_id", read_id("N1-R", "rand_05", "+1/2", "neu_b1/60")),
        o.__setitem__("shadow_read_id", shadow_read_id("neu_b1/60"))))
    refuse("a run outside its cell", b, lambda o: o.update(
        bk_run=7, session_id="floor_b0/7", read_id=read_id("N1-V", "valence", "+1", "floor_b0/7"),
        shadow_read_id=shadow_read_id("floor_b0/7")))
    refuse("'none' with a dose (the arm's cell table)", b, lambda o: (o.__setitem__("direction_id", "none"),
           o.__setitem__("read_id", read_id("N1-V", "none", "+1", o["session_id"]))))
    refuse("alpha off the formula", b, setk("alpha", 7.5))
    refuse("a direction sha not the stage's", b, setk("direction_sha16", "e" * 16))
    refuse("a dose value not the map's", good["N1-V +d_eq"], setk("dose_value", 0.33))
    refuse("a span reaching the read position (n_steered and the interval coordinated; single-defect)", b,
           lambda o: (o["steered_spans"][-1].__setitem__(1, 1273),
                      o.__setitem__("n_steered", sum(x[1] - x[0] for x in o["steered_spans"])),
                      o.__setitem__("retention_interval", o["read_position"] - (1273 - 1))),
           expect="reaches the read")
    refuse("overlapping spans", b, lambda o: o["steered_spans"][1].__setitem__(0, 100))
    refuse("N1-P with the S spans only (n_steered and the interval coordinated; single-defect)", np1, lambda o: (
        o.__setitem__("steered_spans", [s for s in o["steered_spans"] if s[2] == o["cue_S"]]),
        o.__setitem__("n_steered", sum(x[1] - x[0] for x in o["steered_spans"])),
        o.__setitem__("retention_interval", o["read_position"] - (o["steered_spans"][-1][1] - 1))),
        expect="twelve turn spans")
    refuse("n_steered off the spans", b, setk("n_steered", 1))
    refuse("a retention interval off", b, setk("retention_interval", 39))
    refuse("a steered read without its shadow", b, setk("shadow_read_id", None))
    refuse("a shadow on the shadow", sh, setk("shadow_read_id", shadow_read_id(sh["session_id"])))
    refuse("N4 without its schedule zone", n4, setk("schedule_zone", None))
    refuse("a TOLD line naming the other zone", n4, setk("schedule_zone", "S"))
    refuse("a sham line of other words", good["N4-Ts"], setk("told_line", "Either zone is fine."))
    refuse("N4 with BK's ids_sha", n4, setk("ids_sha_bk", "8" * 16))
    refuse("a told line off N4", b, setk("told_line", "Prefer Zone W6."))
    refuse("a rendering mismatch kept as a record", b, setk("ids_sha_bk", "0" * 16))
    refuse("read_position not seq_len - 1", b, setk("read_position", 1270))
    refuse("equal label ids", b, lambda o: o.__setitem__("label_ids_U", list(o["label_ids_S"])))
    refuse("one label a prefix of the other", b, lambda o: (o.__setitem__("label_ids_U", [57, 101]),
           o.__setitem__("logprob_U_tokens", [-0.5, -3.0]),
           o.__setitem__("logprob_U", math.fsum([-0.5, -3.0]))))
    refuse("logprob_S not the fsum of its tokens", good["N1-V +d_eq"], lambda o: o.update(
        logprob_S=-1.5, margin=-1.5 - o["logprob_U"]))
    refuse("margin not the difference", b, setk("margin", 1.0))
    refuse("a positive log-probability", b, lambda o: o["logprob_S_tokens"].__setitem__(0, 0.25))
    refuse("the restricted read at the shared token", b, lambda o: o["restricted"].update(
        k=0, tok_S=57, tok_U=57))
    refuse("a restricted pick against the probabilities", b, lambda o: o["restricted"].update(pick="U"))
    refuse("a tie not given to present[0]", b, lambda o: o["restricted"].update(p_S=0.5, p_U=0.5, pick="S"))
    refuse("restricted probabilities not summing to 1", b, lambda o: o["restricted"].update(p_U=0.5))
    refuse("top1_is_label wrong", b, lambda o: o["restricted"].update(top1_id=5))
    refuse("a capture missing the final layer", b, lambda o: o["capture"]["sha16"].pop("63"))
    refuse("a fidelity rel off the formula", b, lambda o: o["fidelity"].update(rel=0.5))
    refuse("exceeds_tau off the formula", b, lambda o: o["fidelity"].update(exceeds_tau=True))
    refuse("the dose rule on +1/2", good["N1-R +1/2"], lambda o: o["fidelity"].update(reason="dose-rule"))
    refuse("a fidelity reason of no kind", b, lambda o: o["fidelity"].update(reason="spot"))
    refuse("a 'timing' re-computation at the campaign", good["N1-R +1/2"],
           lambda o: o["fidelity"].update(reason="timing"))
    tim_half = example_record(tim, "N1-V", "valence", "+1/2", 3, fidelity="timing")
    refuse("a 'sample' re-computation at G-TIME-n", tim_half, lambda o: o["fidelity"].update(reason="sample"),
           lambda o: check_record(o, tim))
    refuse("a fresh U hash missing the final layer", b, lambda o: o["fidelity"]["fresh_capture_sha16_U"].pop("63"))
    refuse("the shadow without its identity check", sh, setk("identity", None))
    refuse("the shadow without its re-computation", sh, lambda o: (o.__setitem__("fidelity", None),
           o.__setitem__("identity", None)))
    refuse("an identity check on a steered read", b, setk("identity", {"bound": 0.0, "within": True}))
    refuse("identity.within wrong", example_record(ident, "N1-V", "none", "0", 3, fresh_shift=0.25),
           lambda o: o["identity"].update(within=True))
    refuse("a bound not the lock's", sh, lambda o: o["identity"].update(bound=0.5))
    refuse("a non-finite read keeping its margin", nonfinite, setk("margin", 1.0))
    refuse("a finite read with a null margin", b, setk("margin", None))
    refuse("a negative duration", b, setk("duration_ms", -1))
    refuse("a +1 read without its re-computation (n §2.1's dose rule)", b, lambda o: o.update(
        fidelity=None, duration_ms_fresh=None))
    refuse("a backend-ext d = 0 read without its re-computation", example_record(ext, "N1-V", "none", "0", 3),
           lambda o: o.update(fidelity=None, duration_ms_fresh=None), lambda o: check_record(o, ext))
    refuse("a -1 re-computation marked as the sample's", good["N1-R -1"],
           lambda o: o["fidelity"].update(reason="sample"))
    refuse("a re-computation without its fresh duration", b, setk("duration_ms_fresh", None))
    refuse("a fresh duration without a re-computation", good["N1-V +d_eq"], setk("duration_ms_fresh", 10))
    refuse("a fresh duration above the read's", b, setk("duration_ms_fresh", 413))
    refuse("a time-stage identity block without a re-computation",
           example_record(tim, "N1-V", "none", "0", 3, fidelity=None),
           lambda o: o.update(identity={"bound": 0.0, "within": False}), lambda o: check_record(o, tim))
    narrow = dict(ident, read_window=1274)
    refuse("a read whose forward exceeds the stage's read_window (1273 + 3 - 1 > 1274)", b, lambda o: None,
           lambda o: check_record(o, narrow))

    ci = lambda o: check_cell(o)                                           # noqa: E731
    refuse("capture_rows off", cell, lambda o: o.__setitem__("capture_rows", 2), ci)
    refuse("launch order not increasing", cell, lambda o: o["records"][2].__setitem__("launch_index", 0), ci)
    refuse("a capture row out of place", cell, lambda o: o["records"][1]["capture"].__setitem__("row", 2), ci)
    refuse("a record of another cell", cell,
           lambda o: o["records"].__setitem__(1, example_record(ident, "N1-V", "valence", "-1", 1, launch=10, row=1)),
           ci)
    refuse("a repeated read", cell, lambda o: o["records"].__setitem__(
        2, dict(copy.deepcopy(o["records"][1]), launch_index=20, capture=dict(row=2, sha16=o["records"][1][
            "capture"]["sha16"]))), ci)
    refuse("a capture file of another name (one layer's)", cell,
           lambda o: o["capture_files"].__setitem__("40", "x.npy"), ci)
    refuse("a capture sha256 map lacking a layer", cell, lambda o: o["capture_sha256"].pop("63"), ci)
    refuse("a capture sha256 of the old single form", cell, lambda o: o.__setitem__("capture_sha256", "c" * 64), ci,
           expect="expected layer_sha256")
    si = lambda o: check_stage_identity(o)                                 # noqa: E731
    refuse("a lock missing at campaign", ident, lambda o: o.__setitem__("lock_sha256", None), si)
    refuse("a dose map at backend-ext", ext, lambda o: o.__setitem__("dose_map", example_identity()["dose_map"]), si)
    refuse("another proposal", ident, lambda o: o.__setitem__("proposal_sha256", "0" * 64), si)
    refuse("another session set", ident, lambda o: o.__setitem__("session_set_sha256", "0" * 64), si)
    refuse("TAU changed", ident, lambda o: o["fidelity_rule"].__setitem__("tau", 0.02), si)
    refuse("capture layers not the band past the site (two layers, [32, 63])", ident,
           lambda o: o.__setitem__("capture_layers", [32, 63]), si)
    refuse("capture layers of the old form, the site and the last ([31, 63])", ident,
           lambda o: o.__setitem__("capture_layers", [31, 63]), si)
    refuse("+d_eq not the map's d_eq", ident, lambda o: o["dose_map"]["points"][3].__setitem__("value", 0.3), si)
    refuse("a label both kept and merged", ident, lambda o: o["dose_map"]["points"][0].__setitem__(
        "merged", ["+1/2"]), si)
    refuse("+1/2 not 0.5", ident, lambda o: o["dose_map"]["points"][1].__setitem__("value", 0.4), si)
    refuse("rho not 0.3", ident, lambda o: o["dose_map"].__setitem__("rho", 0.30000000000000004), si)
    refuse("a read_window above 4,096 (GA-4)", ident, lambda o: o.__setitem__("read_window", 4097), si)
    refuse("d_eq off its formula by one ulp", ident,
           lambda o: o["dose_map"].__setitem__("d_eq", 0.31250000000000006), si)
    refuse("d_20 off its formula", ident, lambda o: o["dose_map"].__setitem__("d_20", 0.6), si)
    refuse("a merge left out of the points", merged, lambda o: o["dose_map"].__setitem__(
        "points", [{"label": "+1", "value": 1.0, "merged": []}, {"label": "+1/2", "value": 0.5, "merged": []},
                   {"label": "+d_20", "value": 1.0, "merged": []}] + o["dose_map"]["points"][2:]), si)
    refuse("points out of order", ident, lambda o: o["dose_map"]["points"].reverse(), si)
    # the stage report (n-report-v1) and G-READ-n's artifact (n-gread-v1)
    cr = lambda o: check_report(o)                                         # noqa: E731
    cg = lambda o: check_gread(o)                                          # noqa: E731
    band_e = {str(x): "e" * 64 for x in ident["capture_layers"]}           # a cell entry's capture_sha256
    rep = example_report(ident)
    rep_pause = example_report(ident, end_state="PAUSE", obtained_fraction=0.5, pauses=[example_pause(1)])
    rep_adj = example_report(ident, pauses=[example_pause(1, adjudicated=True)])
    rep_cap = example_report(ident, end_state="CAP", obtained_fraction=0.5, hour_cap_ms=500, used_ms=600)
    rep_gver = example_report(ident, end_state="G-VER-STOP", obtained_fraction=0.0,
                              stop={"kind": "G-VER-STOP", "record_sha256": "9" * 64, "detail": "s=62 ids"})
    rep_gver["counters"]["rendering_mismatches"] = 1
    rep_end_binom = example_report(ident, end_state="PAUSE", pauses=[example_pause(1, kind="fidelity-binomial",
                                                                                   launch_index=None)])
    for name, r in (("a complete campaign report", rep), ("a paused campaign, arms incomplete", rep_pause),
                    ("an adjudicated pause, cleared: COMPLETE", rep_adj), ("a CAP end", rep_cap),
                    ("a G-VER-STOP end with its record", rep_gver),
                    ("a binomial fire at the run's end (no read)", rep_end_binom),
                    ("a backend-ext report", example_report(ext))):
        accept(f"report: {name}", lambda r=r: check_report(r))
    accept("report: the identity's sha256 is the canonical JSON's",
           lambda: None if rep["stage_identity_sha256"] == hashlib.sha256(json.dumps(
               ident, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()
           else (_ for _ in ()).throw(SchemaError("identity sha")))
    gr = example_gread()
    gr_mixed = example_gread(statuses={"valence|+d_eq": "FAIL", "span_reward|f0.20": "NOT-COMPUTED"})
    accept("gread: every result PASS", lambda: check_gread(gr))
    accept("gread: a FAIL and a NOT-COMPUTED", lambda: check_gread(gr_mixed))

    def first_pause(o):
        return o["pauses"][0]
    refuse("report: the identity's sha256 off", rep, lambda o: o.__setitem__("stage_identity_sha256", "0" * 64), cr)
    refuse("report: no plan sha256 at the campaign", rep, lambda o: o.__setitem__("read_plan_sha256", None), cr)
    refuse("report: an end state of no kind", rep, lambda o: o.__setitem__("end_state", "DONE"), cr)
    refuse("report: planned not the plan's", rep, lambda o: o["per_arm"]["N1-P"].update(planned=319, obtained=319),
           cr)
    refuse("report: obtained not its cells' records", rep, lambda o: o["per_arm"]["N1-V"].update(
        obtained=959, complete=False), cr)
    refuse("report: complete with obtained under planned", rep_pause,
           lambda o: o["per_arm"]["N1-V"].update(complete=True), cr)
    refuse("report: a repeated pause id", rep_adj, lambda o: o["pauses"].append(dict(
        first_pause(o), launch_index=900)), cr)
    refuse("report: pauses out of launch order", rep_adj, lambda o: o["pauses"].append(dict(
        first_pause(o), pause_id="p02", launch_index=100)), cr)
    refuse("report: an adjudicated pause without its ruling", rep_adj,
           lambda o: first_pause(o).update(ruling_sha256=None), cr)
    refuse("report: a ruling on an unadjudicated pause", rep_pause,
           lambda o: first_pause(o).update(ruling_sha256="f" * 64), cr)
    refuse("report: a batch on a non-finite pause that did not fire it", rep_pause, lambda o: first_pause(o).update(
        binomial=example_pause(1, kind="fidelity-binomial")["binomial"]), cr)
    refuse("report: a binomial pause without its batch", rep_end_binom,
           lambda o: first_pause(o).update(binomial=None), cr)
    refuse("report: a batch under another p0", rep_end_binom,
           lambda o: first_pause(o)["binomial"].update(p0_count=1), cr)
    refuse("report: a non-binomial pause with no read", rep_pause,
           lambda o: first_pause(o).update(read_id=None, launch_index=None), cr)
    refuse("report: PAUSE with no standing pause", rep_adj, lambda o: o.__setitem__("end_state", "PAUSE"), cr)
    rep_pause_full = example_report(ident, end_state="PAUSE", pauses=[example_pause(1)])
    refuse("report: COMPLETE over a standing pause (every arm complete; single-defect)", rep_pause_full,
           lambda o: o.__setitem__("end_state", "COMPLETE"), cr, expect="a standing pause ends only")
    refuse("report: CAP with the cap unspent", rep, lambda o: o.__setitem__("end_state", "CAP"), cr)
    refuse("report: the cap hit but the end not CAP", rep_cap, lambda o: o.__setitem__("end_state", "COMPLETE"), cr)
    refuse("report: hit not used_ms >= hour_cap_ms", rep_cap, lambda o: o["cap"].update(hit=False), cr)
    refuse("report: a STOP record at COMPLETE", rep, lambda o: o.__setitem__(
        "stop", {"kind": "PI-STOP", "record_sha256": "9" * 64, "detail": "x"}), cr)
    refuse("report: G-VER-STOP without its record", rep_gver, lambda o: o.__setitem__("stop", None), cr)
    refuse("report: COMPLETE with an incomplete arm", rep_pause, lambda o: (
        o.__setitem__("end_state", "COMPLETE"), o.__setitem__("pauses", [])), cr)
    refuse("report: a rendering mismatch without a G-VER-STOP or a rendering pause", rep,
           lambda o: o["counters"].__setitem__("rendering_mismatches", 1), cr)
    refuse("report: exceed_tau above exceed_tau4", rep,
           lambda o: o["counters"]["fidelity"]["N1-V|0"].update(exceed_tau=4), cr)
    refuse("report: a cell name that is no cell file's", rep, lambda o: o["cells"].__setitem__(
        "N1-V__valence__p9.jsn", {"json_sha256": "d" * 64, "capture_sha256": dict(band_e), "records": 0}), cr)
    refuse("gread: PASS under the bar", gr, lambda o: (o["results"][1].update(band_median_auc=0.85), [
        x.update(auc=0.85) for x in o["results"][1]["per_layer"]]), cg)
    refuse("gread: the shadow contrast at valence +1", gr, lambda o: o["results"][0].update(contrast="shadow"), cg)
    refuse("gread: a result at a point G-READ-n does not read", gr,
           lambda o: o["results"][0].update(axis="span_reward"), cg)
    refuse("gread: per-layer AUCs not at the probe's layers", gr, lambda o: o["probe"].update(layers=[33, 63]), cg)
    refuse("gread: a band median not the median", gr, lambda o: o["results"][2].update(band_median_auc=0.97), cg)
    refuse("gread: NOT-COMPUTED with a band median", gr_mixed, lambda o: [
        r.update(band_median_auc=0.5) for r in o["results"] if r["status"] == "NOT-COMPUTED"], cg)
    refuse("gread: the comparator's max not its largest", gr,
           lambda o: o["results"][0]["comparator"].update(max=0.4), cg)
    refuse("gread: a repeated (axis, point)", gr, lambda o: o["results"].append(dict(o["results"][0])), cg)
    refuse("gread: above_null not auc > null_p95", gr,
           lambda o: o["results"][0]["per_layer"][0].update(above_null=False), cg)
    refuse("gread: a bar other than 0.90", gr, lambda o: o["probe"].update(bar=0.85), cg)
    # the end-state precedence, rendering pauses, also_fired, resumed_at, the binomial's state, strict names
    pi_stop = {"kind": "PI-STOP", "record_sha256": "9" * 64, "detail": "the PI stopped the unit"}
    rep_pistop = example_report(ident, end_state="PI-STOP", obtained_fraction=0.5, pauses=[example_pause(1)],
                                stop=pi_stop)
    rep_render = example_report(ident, end_state="PAUSE", obtained_fraction=0.5,
                                pauses=[example_pause(1, kind="rendering")])
    rep_render["counters"]["rendering_mismatches"] = 1
    rep_also = example_report(ident, end_state="PAUSE", obtained_fraction=0.5,
                              pauses=[example_pause(1, also_fired=("identity-bound",))])
    rep_resumed = example_report(ident, pauses=[example_pause(1, adjudicated=True, resumed_at=501)])
    rep_pause_cap = example_report(ident, end_state="PAUSE", obtained_fraction=0.5, pauses=[example_pause(1)],
                                   hour_cap_ms=500, used_ms=600)
    gr_merged = example_gread()
    gr_merged["results"][0]["merged"] = ["+d_20"]
    gr_merged["results"] = [r for r in gr_merged["results"] if r["dose_label"] != "+d_20"]
    for name, r in (("PI-STOP over a standing pause", rep_pistop), ("a rendering pause (n §6)", rep_render),
                    ("a pause whose read fired two triggers", rep_also),
                    ("an adjudicated pause with the launch it resumed at", rep_resumed),
                    ("a pause standing when the cap is hit", rep_pause_cap)):
        accept(f"report: {name}", lambda r=r: check_report(r))
    accept("gread: +d_20 merged into +1", lambda: check_gread(gr_merged))
    refuse("report: CAP over a standing pause", rep_pause, lambda o: (
        o.__setitem__("end_state", "CAP"), o["cap"].update(hour_cap_ms=1, hit=True)), cr)
    refuse("report: G-VER-STOP over a standing pause", rep_pause, lambda o: (
        o.__setitem__("end_state", "G-VER-STOP"), o.__setitem__("stop", dict(pi_stop, kind="G-VER-STOP"))), cr)
    refuse("report: also_fired naming its own kind", rep_also,
           lambda o: first_pause(o).update(also_fired=["nonfinite"]), cr)
    refuse("report: also_fired naming a kind of higher precedence", rep_also, lambda o: first_pause(o).update(
        kind="identity-bound", also_fired=["nonfinite"]), cr)
    refuse("report: resumed_at on an unadjudicated pause", rep_pause,
           lambda o: first_pause(o).update(resumed_at_launch_index=501), cr)
    refuse("report: resumed_at not after the pause's launch", rep_resumed,
           lambda o: first_pause(o).update(resumed_at_launch_index=500), cr)
    refuse("report: binomial fires not its pauses", rep, lambda o: o["binomial_state"].update(fires=1,
                                                                                              evaluations=1), cr)
    refuse("report: binomial exceedances above its trials", rep,
           lambda o: o["binomial_state"].update(exceed_tau=161), cr)
    refuse("report: a cell file no stage can hold", rep, lambda o: o["cells"].__setitem__(
        "N4-T__valence__p1.json", {"json_sha256": "d" * 64, "capture_sha256": dict(band_e), "records": 0}), cr)
    refuse("report: a STOP detail of two lines", rep_pistop,
           lambda o: o["stop"].update(detail="line one\nline two"), cr)
    refuse("report: a rendering mismatch under a nonfinite pause", rep_pause,
           lambda o: o["counters"].__setitem__("rendering_mismatches", 1), cr)
    refuse("gread: a merged label that cannot merge (+1/2)", gr,
           lambda o: o["results"][0].update(merged=["+1/2"]), cg)
    refuse("gread: a merge on span_reward", gr, lambda o: o["results"][4].update(merged=["+d_eq"]), cg)
    refuse("gread: a NOT-COMPUTED result with a comparator", gr_mixed, lambda o: [
        r.update(comparator={"band_medians": [0.5] * N_RANDOM, "max": 0.5})
        for r in o["results"] if r["status"] == "NOT-COMPUTED"], cg)
    refuse("gread: a CV form of no kind", gr, lambda o: o["probe"].update(cv="lopo"), cg)
    refuse("report: a pause id out of sequence", rep_pause, lambda o: first_pause(o).update(pause_id="p02"), cr)
    refuse("gread: lr not k's fit_lr", gr, lambda o: o["probe"]["lr"].update(iters=200), cg)
    refuse("report: a cell whose arm has no per_arm entry", example_report(ext), lambda o: o.__setitem__(
        "per_arm", {"N1-R": {"planned": 0, "obtained": 0, "complete": True}}), cr)
    # a rendering pause's read is not launched; a read-less pause is the stage's last
    rep_retry = example_report(ident, end_state="PAUSE", obtained_fraction=0.5, pauses=[
        example_pause(1, kind="rendering", adjudicated=True, resumed_at=500), example_pause(2)])
    rep_retry["counters"]["rendering_mismatches"] = 1
    accept("report: a rendering pause's read launched at its place after the ruling, then pausing",
           lambda: check_report(rep_retry))
    refuse("report: a rendering pause that fired another kind", rep_render,
           lambda o: first_pause(o).update(also_fired=["nonfinite"]), cr)
    refuse("report: a second pause at a non-rendering pause's place", rep_resumed, lambda o: (
        o["pauses"].append(dict(first_pause(o), pause_id="p02", adjudicated=False, ruling_sha256=None,
                                resumed_at_launch_index=None)), o.__setitem__("end_state", "PAUSE")), cr)
    refuse("report: a read-less pause that is not the last", rep_end_binom,
           lambda o: o["pauses"].append(example_pause(2, launch_index=600)), cr)
    refuse("report: a read-less pause with a resumed_at", rep_end_binom, lambda o: (
        first_pause(o).update(adjudicated=True, ruling_sha256="f" * 64, resumed_at_launch_index=5),
        o.__setitem__("end_state", "COMPLETE")), cr)
    # a binomial fire in also_fired carries its batch, which ends at the read that fired it
    rep_nf_binom = example_report(ident, end_state="PAUSE", obtained_fraction=0.5,
                                  pauses=[example_pause(1, also_fired=("fidelity-binomial",))])
    rep_binom_read = example_report(ident, end_state="PAUSE", obtained_fraction=0.5,
                                    pauses=[example_pause(1, kind="fidelity-binomial")])
    for name, r in (("a non-finite pause whose read also fired the binomial", rep_nf_binom),
                    ("a binomial fire at a read", rep_binom_read)):
        accept(f"report: {name}", lambda r=r: check_report(r))
    refuse("report: a binomial in also_fired without its batch", rep_nf_binom,
           lambda o: first_pause(o).update(binomial=None), cr)
    refuse("report: a fire's batch not ending at its read", rep_binom_read,
           lambda o: first_pause(o)["binomial"].update(last_launch_index=499), cr)
    # a pause's scope holds its read's arm; the binomial's state is the counters' and holds its batches; every cell
    # is at a kept point
    ident_m = example_identity(R_ell=40.0)                  # +d_20 merges into +1, +d_eq into +1/2
    rep_m = example_report(ident_m)
    accept("report: a campaign whose dose map merged two points", lambda: check_report(rep_m))
    refuse("report: a pause whose scope lacks its read's arm", rep_pause,
           lambda o: first_pause(o).update(arms_in_scope=["N1-R"]), cr)
    refuse("report: binomial_state not the fidelity counters' totals", rep,
           lambda o: o["binomial_state"].update(trials=170), cr)
    refuse("report: a batch beyond the stage's exceedances", rep_end_binom,
           lambda o: first_pause(o)["binomial"].update(k=2), cr)
    refuse("report: a cell at a point the dose map merged away", rep_m, lambda o: o["cells"].__setitem__(
        cell_filename("N1-V", "valence", "+d_eq"), {"json_sha256": "d" * 64, "capture_sha256": dict(band_e),
                                                    "records": 0}), cr)
    # the rendering count is the rendering pauses'; a G-VER-STOP comes before any read; a scope names an arm once;
    # an identity-bound trigger is a d = 0 read's; the counters cover the pauses that name them; CV kfold10 only

    def gver_with_record(o):
        name = sorted(o["cells"])[0]
        o["cells"][name]["records"] = 1
        o["per_arm"][VALID_CELL_NAMES[name]]["obtained"] = 1
    refuse("report: a rendering pause counted twice", rep_render,
           lambda o: o["counters"].__setitem__("rendering_mismatches", 2), cr)
    refuse("report: a G-VER-STOP with no mismatch counted", rep_gver,
           lambda o: o["counters"].__setitem__("rendering_mismatches", 0), cr)
    refuse("report: a G-VER-STOP with a record", rep_gver, gver_with_record, cr)
    refuse("report: a scope naming an arm twice", rep_pause,
           lambda o: first_pause(o).update(arms_in_scope=["N1-V", "N1-V"]), cr)
    refuse("report: an identity-bound trigger on a steered read", rep_also,
           lambda o: first_pause(o).update(read_id="N1-V|valence|+1|floor_b0/3"), cr)
    refuse("report: nonfinite_reads below its pauses", rep_pause,
           lambda o: o["counters"].__setitem__("nonfinite_reads", 0), cr)
    refuse("report: identity_out_of_bound below its pauses", rep_also,
           lambda o: o["counters"].__setitem__("identity_out_of_bound", 0), cr)
    refuse("gread: a CV form not 'kfold10' (kfold-10)", gr, lambda o: o["probe"].update(cv="kfold-10"), cg)
    # the capture band per layer (ADDENDUM-n1 §6.2); the cap's loads (the seat's answers of 2026-11-16, §3);
    # G-READ-n's CV form, its seed and its PASS rule (ADDENDUM-n1 §6.3-§6.4)
    refuse("report: a cell entry's capture_sha256 lacking a layer", rep,
           lambda o: o["cells"][cell_filename("N1-V", "valence", "+1")]["capture_sha256"].pop("63"), cr)
    refuse("report: a negative load time", rep, lambda o: o["cap"].update(loads_ms=[-1]), cr)
    refuse("gread: the CV form 'loso' (n §3's, replaced by kfold10)", gr, lambda o: o["probe"].update(cv="loso"), cg)
    refuse("gread: a probe without its cv_seed", gr, lambda o: o["probe"].pop("cv_seed"), cg)
    refuse("gread: a cv_seed not an int", gr, lambda o: o["probe"].update(cv_seed="20261116"), cg)
    gr_low = example_gread()
    gr_low["results"][0]["per_layer"][0].update(auc=0.5, above_null=False)
    accept("gread: PASS with one layer below its null, the band median >= .90 and above the comparator's max",
           lambda: check_gread(gr_low))
    refuse("gread: that result marked FAIL (no per-layer condition)", gr_low,
           lambda o: o["results"][0].update(status="FAIL"), cg)
    refuse("report: an N1-P cell at +1/2 under the default map (no listed label's keeper)", rep,
           lambda o: o["cells"].__setitem__(cell_filename("N1-P", "valence", "+1/2"),
                                            {"json_sha256": "d" * 64, "capture_sha256": dict(band_e), "records": 0}),
           cr, expect="does not keep for N1-P")

    def _names() -> None:
        if len(VALID_CELL_NAMES) != 139 or VALID_CELL_NAMES.get(cell_filename("N1-P", "valence", "+1/2")) != "N1-P":
            raise SchemaError(f"{len(VALID_CELL_NAMES)} valid cell names, or N1-P's +1/2 cell is not among them")
    accept("139 valid cell names: the 138 listed and N1-P's +1/2, a keeper of its +d_20 or +d_eq", _names)

    def _capacity() -> None:
        if (capture_capacity("N1-R"), capture_capacity("N1-V"), capture_capacity("N4-Ts")) != (40, 160, 160):
            raise SchemaError("the capture capacities are not 40 for N1-R and 160 for the other arms")
        try:
            capture_capacity("N9")
        except SchemaError:
            return
        raise SchemaError("capture_capacity accepted an arm that is none")
    accept("capture capacity: 40 rows for N1-R's cells, 160 for every other arm's; no other arm", _capacity)
    return ok, total


if __name__ == "__main__":
    import sys

    passed, n = _selftest(verbose="--verbose" in sys.argv[1:])
    print(f"n schema self-test: {passed}/{n}")
    sys.exit(0 if passed == n else 1)
