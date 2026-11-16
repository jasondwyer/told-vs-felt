"""PROPOSAL-n -- the read runner's record schema (n v0.2 §8 step 6, its first commit).

The seat's answers of 2026-11-15 (``results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md``),
§5.1: "**n-build**, n §8 step 6 (the package), whose first commit is the read runner's record schema;
**n-analyzer**, step 9's `n_analyze.py` and its battery (385 tuples), built from that schema." This module is that
schema: every field the read runner writes, its type, when it is null, and the checks both sides run -- the runner
before every write, the analyzer on every load. A change to it is a commit of this file with its reason.

It imports the standard library only (the package's parent imports numpy). It reads no file, touches no model and
writes nothing; ``python -m valence_core.n.schema`` runs its self-test on literal records.

WHAT A RECORD IS (Code's reading of n §2.4, "each read counted once"). One record per read of §2.4's table: one
(arm, direction, dose point, session). The fidelity re-computation (§2.1) and the d = 0 identity check ride inside
that record and are never records of their own. Records are written by three stages: ``campaign`` (§2.4's arms,
§8 step 14), ``time`` (G-TIME-n's timed reads, §3) and ``backend-ext`` (the BACKEND extension's fresh-versus-cached
reads, §3 G-ACQ; G-ACQ's dated note GA-5). G-CAL-n's generations, G-VEC's captures, G-VER's reconstructions and the
stages' reports are other records, not specified here.

THE TWO PATHS (Code's construction, declared here; LOCK-n v0.1 pins it). BK's ``prereg.precondition_cache``
(``data/n/bk/.../neutral_passages/analysis.json``) states the check n §2.1 adopts: "the
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
so the two labels' token sequences may share a prefix (whether they do is the tokenizer's). Code's reading, flagged
for the seat at the BUILD: the read is taken at the first label-token position where S's and U's token sequences
differ (offset ``k`` past the read position; for k >= 1 it lies on the cached continuation, the shared prefix
teacher-forced): the two divergent tokens' full-softmax probabilities, renormalized; ``label_mass`` their sum; the
pick is the larger, a tie going to ``present[0]`` (m's ``choice_read`` gives ties to its first label). m's
``choice_read`` also re-forwards the identical text to verify it (KL exactly 0.0); n takes the read on the read's
own forward and does not repeat that re-forward -- §2.1's fidelity re-computation is n's re-forward (Code's
reading, flagged).

SPANS AND THE SHADOW (rule 5(f)(i)-(iii); n §2.2; the record's provenance is Code's construction, declared here).
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
splits (``neu_b1`` run 62, ``neu_b3`` run 113) included; how they are carried is the lock's.

CAPTURES (n §2.2: "the residual at the read position captured at layers 32 and the final layer on every
forward"; the form is Code's reading). From the cached path's prefill, at the read position: the residual after the
site's decoder layer and after the last decoder layer (olmo_hf's capture index l is the residual after decoder
layer l, 0-based; index n_layers - 1 is before the final norm: G-ACQ's hook-site check). float32, stored per cell
in one ``.npy`` array of shape [rows, len(capture_layers), d_model], row r holding the cell's r-th record; each
record carries its row and each layer's ``sha16_arr``. The fresh path's read-position residuals, from each of its
two forwards (label S's and label U's), are hashed into the fidelity block, not stored. The cached path's
continuations hold no read-position residual of their own (the cache keeps keys and values), so every forward
that computes one is captured or hashed, and every read captures: G-TIME-n's "capture-on" kind is every read.

FIDELITY (n §2.1; G-DATA (vi); the comparison's form is Code's reading). ``absdiff = |margin - fresh_margin|``;
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
line itself, §2.4's words (that the record carries the line, not its rendered join, is Code's reading). §2.4 puts
the line in the choice prompt before "Reply with ONLY…"; the exact join is the lock's. N4's token sequence is its
own: ``ids_sha_bk`` is null.

CROSS-RECORD PROPERTIES are not checked here, where one record or one cell is checked: a steered read's shadow exists
with the same ``ids_sha`` (the runner asserts it before the read); ``ids_sha_bk`` equals the session record's (the
runner and G-VER); an N4 read's tokens before ``n_pre`` are its BK session's (the renderer asserts it; G-VER
re-checks); N4-T and N4-Ts carry the same ``schedule_zone`` per session, under the schedule's key, its 80/80 split
and its balance by ``present`` order (the runner and the lock). The analyzer re-checks what it uses.

TYPES. Exact JSON-native values only (m's ``resume._assert_native`` form: no numpy scalars, str dict keys); every
float finite. A non-finite number in a path makes that path's ``finite`` false and its numbers null (§6: NaN/inf
pauses). No record carries a time of day: ``duration_ms`` is the read's wall-clock of model work, both paths, and
``duration_ms_fresh`` the fresh path's share (null without a re-computation), for G-TIME-n's kinds and the cap.

NOT RECORDED: Δm; the free-text reply of n §4 (b) (§2.1: "No new text is generated for N1, N2 or N4"; flagged for
the seat at the BUILD); BK's welfare probes, which n does not run.

FILES. A stage's checkpoint directory holds one cell file per (arm, direction, dose point), named by
``cell_filename``, beside its capture array; both written atomically (m's ``resume.atomic_write_json`` for the
JSON), the array first.

THE DOSE MAP (n §2.3: "d_eq = (0.10 · R_ℓ)/(ρ · R) and d_20 = min(1, 2·d_eq) ... a point within 0.05 of an
existing one is merged"). ``check_stage_identity`` requires, exactly, ``rho == 0.3``,
``d_eq == (0.10 * R_ell) / (rho * R)``, ``d_20 == min(1.0, 2.0 * d_eq)`` and ``points == dose_points(d_eq, d_20)``:
the merge rule, settled with n-analyzer so both sides derive the same points, is ``dose_points``' docstring.

THE READ PLAN. ``read_plan(identity)`` is the campaign's declared read set: n §2.4's arms over the stage's dose map,
N1-R on the 40 floor sessions, every other arm on all 160 -- 7,360 reads when nothing is merged. §2.3 states the
merge for N1-V's points; that it reaches every arm reading BK-scale points (N1-V and N1-R, whose floors and leak
ceilings are taken point by point, C12), and that a merged point is read once under the label kept, are Code's
readings, flagged for the seat. An arm is complete exactly when its obtained read_ids are its plan's.

EXAMPLES. ``example_identity``, ``example_record`` and ``example_cell`` build valid objects from literals, for this
module's self-test and for the analyzer's battery; no production path calls them.
"""
from __future__ import annotations

import hashlib
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

#: §2.4's table: arm -> the (direction, dose labels) it reads, before §2.3's merges.
ARM_CELLS = {
    "N1-V": (("valence", ("+1", "+1/2", "+d_20", "+d_eq", "-1")), ("none", ("0",))),
    "N1-R": tuple((r, ("+1", "+1/2", "+d_20", "+d_eq", "-1")) for r in RANDOM_IDS),
    "N1-P": (("valence", ("+1", "-1")),),
    "N2-E": (("span_reward", ("f0.10", "f0.20")),),
    "N2-S": (("span_sentiment", ("f0.10", "f0.20")),),
    "N2-C": (("span_character", ("f0.10", "f0.20")),),
    "N4-T": (("none", ("0",)),),
    "N4-Ts": (("none", ("0",)),),
}
ARM_SPAN_KIND = {"N1-V": "S", "N1-R": "S", "N1-P": "SU", "N2-E": "S", "N2-S": "S", "N2-C": "S",
                 "N4-T": "none", "N4-Ts": "none"}
TOLD_VARIANT = {"N4-T": "TOLD", "N4-Ts": "SHAM"}
#: n §2.4: TOLD "Prefer [zone X]."; SHAM "Either is fine.", in the choice prompt before "Reply with ONLY…" (the exact
#: join is the lock's).
TOLD_LINE = "Prefer {zone}."
SHAM_LINE = "Either is fine."
SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = "N1-V", "none", "0"
FIDELITY_REASONS = ("dose-rule", "sample", "timing")

_HEX16 = re.compile(r"[0-9a-f]{16}")
_HEX64 = re.compile(r"[0-9a-f]{64}")
_SESSION = re.compile(r"(floor_b[0-7]|neu_b[0-5])/([0-9]{1,3})")


class SchemaError(ValueError):
    """A record, cell or identity that does not match this schema. The runner refuses to write it; the analyzer
    refuses to load it."""


# --- field tables -------------------------------------------------------------------------------------------
# Each entry: name -> (type, nullable, meaning). Types: "str", "int", "float", "bool", "sha16", "sha256",
# "ints" (list of int), "floats" (list of float), "spans" (list of [int, int, str]), "pair" (list of two str),
# "layer_sha16" (dict str(layer) -> sha16), or the name of a nested table.

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
    "capture": ("capture", False, "the read position's residuals: the cell array's row and each layer's sha16"),
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
    "row": ("int", False, "the record's row in the cell's capture array"),
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
    "capture_file": ("str", False, "the capture array's file name, beside this file"),
    "capture_rows": ("int", False, "len(records)"),
    "capture_sha256": ("sha256", False, "sha256 of the capture array file's bytes when this file was written"),
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
    "rendering_id": ("str", False, "the rendering of record (G-DATA (iv)), as the lock names it; at backend-ext, "
                                   "before the lock, as the stage's entry names it"),
    "label_convention": ("str", False, "the label token convention, as the lock names it; at backend-ext, before "
                                       "the lock, as the stage's entry names it"),
    "layer_bk": ("int", False, "BK's site, 32 of 64"),
    "layer": ("int", False, "the adapter index of the site (G-VEC settles 31 or 32); at backend-ext, before G-VEC, "
                            "the capture site the stage's entry declares (nothing is injected there)"),
    "capture_layers": ("ints", False, "[layer, n_layers - 1]"),
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
    """The cell file's name; its capture array is the same stem with ``.npy``."""
    if arm not in ARMS or direction_id not in DIRECTION_IDS or dose_label not in DOSE_SLUGS:
        raise SchemaError(f"no cell ({arm!r}, {direction_id!r}, {dose_label!r})")
    return f"{arm}__{direction_id}__{DOSE_SLUGS[dose_label]}.json"


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
    kept = dose_point_values(identity)
    out = []
    for arm in ARMS:
        runs = range(N_FLOOR) if arm == "N1-R" else range(N_SESSIONS)
        for did, labels in ARM_CELLS[arm]:
            for dl in labels:
                if dl not in kept:
                    continue
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
    the form settled with n-analyzer (Code's reading, flagged for the seat at the BUILD):

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
    if identity["capture_layers"] != [identity["layer"], identity["n_layers"] - 1]:
        _fail(f"{where}.capture_layers", "is not [layer, n_layers - 1]")
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
    allowed = {(d, x) for d, labels in ARM_CELLS[arm] for x in labels}
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
            _fail(w("ids_sha_bk"), "differs from ids_sha: a rendering mismatch is a STOP, never a record")
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
    stem = cell_filename(arm, did, dl)[:-len(".json")]
    if cell["capture_file"] != stem + ".npy":
        _fail(f"{where}.capture_file", f"should be {stem}.npy")
    recs = cell["records"]
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
        "label_convention": "example-labels", "layer_bk": 32, "layer": 31, "capture_layers": [31, 63],
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
    stem = cell_filename(arm, direction_id, dose_label)[:-len(".json")]
    return {"schema": CELL_SCHEMA, "stage_identity": identity, "arm": arm, "direction_id": direction_id,
            "dose_label": dose_label, "records": recs, "capture_file": stem + ".npy", "capture_rows": len(recs),
            "capture_sha256": "c" * 64}


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

    def refuse(name, base, mutate, check=None):
        nonlocal ok, total
        total += 1
        obj = copy.deepcopy(base)
        mutate(obj)
        try:
            (check or (lambda o: check_record(o, ident)))(obj)
            print(f"FAIL refuse {name}: accepted")
        except SchemaError as e:
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
        if len(names) != 136 or len(set(names)) != 136:
            raise SchemaError(f"{len(names)} cells, {len(set(names))} distinct names")
    accept("136 distinct cell files before merges (n §2.4)", _cells)

    def _plan() -> None:
        plan = read_plan(ident)
        if len(plan) != 7360 or len(set(plan)) != 7360:
            raise SchemaError(f"the plan has {len(plan)} reads, {len(set(plan))} distinct, not 7,360 (n §2.4)")
        per = {a: sum(1 for x in plan if x.startswith(a + "|")) for a in ARMS}
        want = {"N1-V": 960, "N1-R": 4800, "N1-P": 320, "N2-E": 320, "N2-S": 320, "N2-C": 320, "N4-T": 160,
                "N4-Ts": 160}
        if per != want:
            raise SchemaError(f"per-arm plan {per}")
        if any(x.startswith("N1-R|") and int(x.rsplit("/", 1)[1]) >= N_FLOOR for x in plan):
            raise SchemaError("N1-R planned off the floor sessions")
        pm = read_plan(merged)
        if len(pm) != 7360 - 160 - 24 * 40 or any("|+d_20|" in x for x in pm):
            raise SchemaError(f"the merged plan has {len(pm)} reads")
        pd = read_plan(double)
        if len(pd) != 7360 - 2 * (160 + 24 * 40) or any("|+d_20|" in x or "|+d_eq|" in x for x in pd):
            raise SchemaError(f"the doubly merged plan has {len(pd)} reads")
        if read_plan_sha256(ident) != read_plan_sha256(example_identity()):
            raise SchemaError("the plan's sha256 is not deterministic")
    accept("the read plan: 7,360 reads by §2.4's table; 6,240 with +d_20 merged; 5,120 with both merged", _plan)

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
    refuse("an arm reading a dose it does not read", b, lambda o: (o.__setitem__("arm", "N1-P"),
           o.__setitem__("read_id", read_id("N1-P", "valence", "+1/2", o["session_id"])),
           o.__setitem__("dose_label", "+1/2")))
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
    refuse("a span reaching the read position", b, lambda o: o["steered_spans"][-1].__setitem__(1, 1273))
    refuse("overlapping spans", b, lambda o: o["steered_spans"][1].__setitem__(0, 100))
    refuse("N1-P with the S spans only", np1, lambda o: (
        o.__setitem__("steered_spans", [s for s in o["steered_spans"] if s[2] == o["cue_S"]]),
        o.__setitem__("n_steered", sum(x[1] - x[0] for x in o["steered_spans"]))))
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
    refuse("a capture file of another name", cell, lambda o: o.__setitem__("capture_file", "x.npy"), ci)
    si = lambda o: check_stage_identity(o)                                 # noqa: E731
    refuse("a lock missing at campaign", ident, lambda o: o.__setitem__("lock_sha256", None), si)
    refuse("a dose map at backend-ext", ext, lambda o: o.__setitem__("dose_map", example_identity()["dose_map"]), si)
    refuse("another proposal", ident, lambda o: o.__setitem__("proposal_sha256", "0" * 64), si)
    refuse("another session set", ident, lambda o: o.__setitem__("session_set_sha256", "0" * 64), si)
    refuse("TAU changed", ident, lambda o: o["fidelity_rule"].__setitem__("tau", 0.02), si)
    refuse("capture layers not [layer, last]", ident, lambda o: o.__setitem__("capture_layers", [32, 63]), si)
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
    return ok, total


if __name__ == "__main__":
    import sys

    passed, n = _selftest(verbose="--verbose" in sys.argv[1:])
    print(f"n schema self-test: {passed}/{n}")
    sys.exit(0 if passed == n else 1)
