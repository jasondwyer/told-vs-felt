"""e2d configuration of record -- PROPOSAL-j v1.1, AMENDMENT 1.

Everything here is named by the proposal or its amendment. Nothing in this
module is a Code choice except where a docstring says so in those words, and
where that happens the alternative is computed beside it and flagged.

WHAT AMENDMENT 1 FIXED, and where it lands:

  (i)  ROSTER OF RECORD = the h-roster. `ROSTER` below. e2a's own pairs are
       not admitted; comparability with e2a rides on e2b's paired shadow
       reads, not on pair identity.
  (ii) AUDIT RULE OF RECORD = `data/configs/e2b_audit_v2.json`, loaded here
       rather than transcribed, so the artifact's sha is what runs.

WHAT THE AMENDMENT DID NOT FIX, and is flagged: the exclusion *scope*.
See `EXCLUSION_SCOPE` below -- it is the one open spec item and it is
D2-blocking, not D1-blocking.
"""

from __future__ import annotations

import json
import os

from ..session import AuditSpec, FeatureSpec, Tripwire

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(REPO, "data")

# --- AMENDMENT 1 (i): the roster of record --------------------------------
#: The h-roster, H3b-selected -- "an admissible four, never the best four"
#: (adjudicated 2026-08-21). Identical tuple to `e2b_verdict_campaign.ROSTER`;
#: `check_e2d_roster_of_record` in the suite asserts they have not drifted
#: apart, because two literals of the same roster is exactly how a roster
#: silently forks.
ROSTER = (("granite", "plaza"), ("prism", "slate"),
          ("velvet", "walnut"), ("ridge", "saddle"))

# --- session shape (held fixed by PROPOSAL-j §1) --------------------------
F = 2                      # forced rounds per label
TEMP = 0.7                 # e2a's TEMP, unchanged through e2b and B3
LAYER = 48
RANDOM_DIRS_KEY = "L48"    # e0_random_dirs.npz key -- the direction e2a's
                           # random arm used (PROPOSAL-j §1 "[LOCK-j names it]")

# --- arms (PROPOSAL-j §1, §3; cells per AMENDMENT 1 (i)) ------------------
#: `delivers` is the CPP contingency: which pole's rounds carry a state.
#: "pos" means the +tag's rounds are steered and the -tag's rounds are not --
#: there is no negative pole anywhere in e2d (§6, welfare).
ARMS = {
    "M": {"direction": "axis",   "strata": 16, "d1": 4},
    "S": {"direction": None,     "strata": 8,  "d1": 2},
    "R": {"direction": "random", "strata": 8,  "d1": 2},
}

D1_FRAC = 0.10             # D1 is the harness smoke at MED; 0.20 is D2's
D2_FRAC = 0.20


# --- AMENDMENT 1 (ii): the audit rule of record ---------------------------
def load_audit() -> tuple[AuditSpec, dict]:
    """The audit of record, loaded from its committed artifact.

    Transcribing the fragments into a literal here would put a second copy
    of a frozen monitor in the tree, and the whole point of v2's sha being
    printed in a run header is that what ran is identifiable. So it is
    loaded, and the artifact dict (with its `sha16`) rides into the output.

    `ban_strings` come from the e2a ban list -- the same twelve special-token
    strings the template family froze in 2026-08-09. They are part of the
    audit in e2a's `audit_degenerate` and they stay part of it here.
    """
    cfg = json.load(open(os.path.join(DATA, "configs/e2b_audit_v2.json")))
    bans = json.load(open(os.path.join(DATA, "configs/e2a_ban_list.json")))
    spec = AuditSpec(ban_strings=tuple(bans["strings"]),
                     frame_fragments=tuple(cfg["frame_fragments"]),
                     junk_regex=tuple(cfg["junk_regex"]))
    return spec, cfg


# --- THE ONE OPEN SPEC ITEM (flagged; D2-blocking, not D1-blocking) -------
#: AMENDMENT 1 (ii) names the audit ARTIFACT but not the exclusion SCOPE --
#: which rounds an audit-degenerate response excludes a session on. The two
#: candidate scopes are both live in the repo and they differ by a lot:
#:
#:   "e2a"  audit excludes on FORCED rounds only ("v3: degenerate rounds
#:          AFTER the first free choice never touch the primary"); lexical
#:          excludes on any round. Recounted on the e2a archive under v2 and
#:          e2d's own-pair lexical scope: reward arm 10/112 = 0.089.
#:   "e2b"  audit excludes on ANY round (what e2b's verdict campaign and B3
#:          both ran). Same recount: reward arm 18/112 = 0.161.
#:
#: This matters because Q1's bar is p0 = 0.15, and the scope moves Q1's
#: OPERATING CHARACTERISTIC at D2 scale. Stated precisely, because the loose
#: version of this claim is wrong: e2a's strict-scope rate of 0.161 sits
#: above p0 but does NOT reject at its own n = 112 (p = .41). The problem is
#: at D2's n = 32, where Q1 fires at >= 9/32 (p = .0413, exactly the reach
#: §2 states). The probability of Q1 firing on a healthy apparatus is
#:
#:     0.0015  if the true exclusion rate is the lenient scope's 0.089
#:     0.0602  if it is the strict scope's 0.161
#:
#: -- a 40x shift, and above the nominal alpha = .05. So the scope choice
#: materially changes what Q1 is testing, and Code does not pick it.
#:
#: D1 runs under "e2a" for two stated reasons, and neither is a preference:
#:   1. It is the only scope under which AMENDMENT 1 (ii)'s own numbers
#:      reproduce -- reward arm 11/112 and the corrected primary 54/101 were
#:      both computed with audit degeneracy confined to forced rounds.
#:   2. It is INFORMATION-PRESERVING. A session the lenient scope continues
#:      records the round the strict scope would have stopped it on, so the
#:      strict exclusion set is exactly recoverable from a lenient run. The
#:      reverse is false: a strict run truncates the transcript and the
#:      lenient counterfactual is gone.
#: Both counts are reported at D1. Design settles it before D2.
EXCLUSION_SCOPE = "e2a"

#: Precedence is NOT open: rule 28(b) says the tolerant counter attributes
#: first, and `classify_response` implements exactly that (audit-first, with
#: the lexical check suppressed on a response the audit already claimed).
#: e2a itself ran lexical-first; that ordering predates rule 28(b) and is not
#: inherited.
PRECEDENCE = "audit-first (rule 28b, via session.classify_response)"


# --- monitors (PROPOSAL-j §2 D1: "monitors and tripwires verify_firing") --
def declared_bars(degeneracy_p0: float = 0.02) -> list[Tripwire]:
    """D1's declared bars.

    Rule 21's distinction is forced at declaration. Template breakage and
    scaffold-token absorption are ~zero-base-rate defect classes and get
    hair triggers; round degeneracy has a measured base rate and binds by
    exact binomial against a declared p0 at every scale.

    These are ACCEPTANCE bars for the harness, not verdict criteria, and
    nothing here can touch a criterion (rule 21, final clause).
    """
    return [
        Tripwire(name="scaffold_absorption", kind="hair_trigger",
                 domain="all", threshold=0.0,
                 justification="A banned special-token string in a response "
                               "means the ban list did not apply at "
                               "generation. Base rate is structurally zero: "
                               "the tokens are suppressed in the sampler."),
        Tripwire(name="template_breakage", kind="hair_trigger",
                 domain="all", threshold=0.0,
                 justification="A session whose scaffolding does not "
                               "reconstruct under session_e2a is not an e2a-"
                               "format session. Base rate is zero by "
                               "construction -- the harness writes the "
                               "scaffold itself."),
        Tripwire(name="round_degeneracy", kind="binomial", domain="all",
                 p0=degeneracy_p0, alpha=0.05,
                 justification="Measured class: e2a's 0.10 archive is the "
                               "declared healthy rate. Binds by exact "
                               "binomial at every scale (rule 21)."),
    ]


#: The no-model firing check every bar must pass before a run (rule 21; and
#: trap 5 -- a case that never ran is a FAILURE, so every declared bar
#: appears here in both directions).
FIRING_CASES = (
    ("scaffold_absorption", 0, 80, False),
    ("scaffold_absorption", 1, 80, True),
    ("template_breakage", 0, 8, False),
    ("template_breakage", 1, 8, True),
    ("round_degeneracy", 0, 500, False),
    ("round_degeneracy", 5, 500, False),
    ("round_degeneracy", 30, 500, True),
)


# --- descriptive features, with rule-28(a) decidable-n floors -------------
def declared_features() -> list[FeatureSpec]:
    """Rule 28(a): each feature declared against the sample it is defined ON.

    The failure this prevents is f1's `fewer_degen_rounds` -- a paired
    within-session contrast whose every decidable observation was removed by
    the exclusion rule, 283 ties out of 283. So each of these says which
    domain it lives on and how many decidable observations it needs there.

    At D1 (n = 8) these floors are NOT met and are not expected to be; D1
    declares them and reports the decidable-n so D2 inherits a floor that was
    set before data rather than after it.
    """
    return [
        FeatureSpec(name="stay_switch", domain="valid", min_decidable=8),
        FeatureSpec(name="session_share", domain="valid", min_decidable=8),
        FeatureSpec(name="fewer_degen_rounds_plus", domain="valid",
                    min_decidable=8, min_decidable_frac=0.10),
        FeatureSpec(name="termination_attempts", domain="all",
                    min_decidable=1),
    ]


#: Counters tabulate over ALL sessions including excluded ones (rule 23).
DECLARED_COUNTERS = ("termination", "cap_hit", "audit_degenerate", "lexical",
                     "post_choice_degeneracy", "low_label_mass")

__all__ = ["ROSTER", "F", "TEMP", "LAYER", "RANDOM_DIRS_KEY", "ARMS",
           "D1_FRAC", "D2_FRAC", "load_audit", "EXCLUSION_SCOPE",
           "PRECEDENCE", "declared_bars", "FIRING_CASES", "declared_features",
           "DECLARED_COUNTERS", "REPO", "DATA"]
