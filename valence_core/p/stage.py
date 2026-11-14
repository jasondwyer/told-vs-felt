"""PROPOSAL-p's stages: G-TIME-OLMo (p), G-F0m-OLMo (p) and the campaign (p v0.2 §4.1-§4.2, §8 step 6; the design seat's
answer of 2026-11-08, ``de729c4``, §1; Code's block on entry (9)'s site, 2026-11-08, and the seat's answer to it, §2,
``6b63973``; the seat's answers on G-F0m-OLMo (p)'s wiring, 2026-11-10, ``42c5a92``, §2-§3).

THE STAGE. m's ``stages.run_gate_stage`` with gate ``time`` (m:302: two sessions, one per arm, uncached) or ``qual``
(m:302: 24 sessions, 8 contrast and 16 sham, uncached; THE QUALIFICATION below), run for p's unit -- p's records keep
m's unit and template strings (p:84) -- under the substitution register, every entry through ``register.substituted``:

  (1) ``corr._eligible_m`` -> p's eligibility: the renders of record are p's;
  (2) ``keys``' four OLMo families -> p's: the arm and item streams, the schedules' keys, G-VER's rebuild;
  (6) ``stages.DEFAULT_OUT`` -> data/p: m's out-root guard admits data/p, and every path a stage writes derives from it;
  (7) ``schedule.verify_schedule_dir`` -> p's: m's load_committed verifies p's eighteen files and p's manifest;
  (8) ``resume.IDENTITY_KEYS_OLMO`` -> m's key set and p's four fields;
  (9) ``resume.Identity`` -> m's builder, wrapped: p's four fields in the checkpoint identity; entered and restored
      with (8).

The adapter is wrapped in §2.2's proxy, whose stored-text check is §2.3's hair trigger (the seat's Q5).

THE QUALIFICATION. PIN (Code, declared at the qual wiring; the seat's answers of 2026-11-10, ``42c5a92``, §2, option
(A), "``qual`` alone"): the gate is a parameter of the stage (``GATES``, ``time`` | ``qual``), its counts m:302's
(``COUNTS``, ``templates_counts``: 1 + 1 at ``time``, 8 + 16 at ``qual``), which m's stage checks against the committed
gate files' n after the load; at ``qual`` the precheck also asserts them equal to those files' n before the load
(``counts_problems``). At ``qual``, G-TIME (p)'s checkpoint under the stage's root is m's ``prior_ckpt``, checked
before the load (``prior_problems``; a refusal, nothing recorded or loaded) by m's ``prior_gate`` -- the checkpoint this
unit's G-TIME, ended PASS, under m's proposal pin (F-p8) and, on a non-stub run, not written on the stub -- and then as
p's: its identity's ``proposal`` and ``proposal_p_sha256`` this run's, since m's pin, which every p record carries,
cannot tell a p record from m's; m's stage runs ``prior_gate`` again inside. No
``prior_adjudication`` is passed: the three G-TIME stages PASSed, a PAUSE has no path in this build, and the seat's
adjudication, if a G-F0m-OLMo (p) bar fires, is a STOP under m's rule for the qualification stage. The lock carries
LOCK-p v0.2's acceptance line (``QUAL_LOCK_LINE``: the text of m's ``OLMO_QUAL_LOCK_LINE``, scripts/m_sessions.py, p's
records keeping m's unit strings; the seat's §3) as a whole line -- the whole-line form of step 6's N-4 only; the
line between backticks does not satisfy it -- checked before the load (m's driver requires the line of LOCK-m-OLMo's
text as a substring). The call log, the marker, the lock file and p's report
take the gate's name (``_qual_``); p's report covers the 24 sessions on the seat's read domain -- the proxy
attribution over the sixteen sham sessions, every proxy count over the contrast sessions withheld, as at G-TIME.
``time``'s behaviour is unchanged and its records stand.

THE CAMPAIGN. PIN (Code, declared at the campaign wiring; the seat's read of G-F0m-OLMo (p) x3, §4.3 item 2, of the
campaign wiring: "p's own move ... `campaign` joins the wired commands; (j)'s closure and the register unchanged"): m's
``stages.run_campaign`` run for p's unit under the same entries (``STAGES``, the gates and the campaign; ``GATES`` and
``COUNTS`` unchanged). Its values in m's form, as scripts/m_sessions.py carries Q-F0's (read as text, never imported):
the launch counts per arm G-PWR (p)'s of record (``CAMPAIGN_LAUNCH_COUNTS``, bound to data/p/gates/G-PWR-p.json by
``gpwr_problems`` before the load), the floors the package's (``campaign_floors``), the hour cap the PI's cap share
(``CAMPAIGN_HOUR_CAP``; a campaign is refused while it is unset); their line forms whole lines of the unit's LOCK-p
v1.0 (``campaign_lock_lines``), and G-PWR (p)'s record named by the lock beside lock_required's values. Its prior is the
unit's G-F0m-OLMo (p) checkpoint (``prior_problems`` at ``campaign``: m's prior_gate, then p's identity). Before the
load, the campaign's own refusals: m's checkpoint read as a campaign's (``campaign_state``, m's driver's
_campaign_state in p's form, a pause's arm the unit's own) -- an unreadable one refused, never read as empty; an
ended one refused, its report re-derived by the driver's campaign-report; and the seat's adjudication and the PI's
stop against its state (``campaign_ruling_problems``, m's driver's refusals in its words). A PAUSE is not a STOP: the
run's end line records it and nothing is marked; a later run (always a --resume, which appends) resumes it with the
seat's adjudication or ends it by the PI's stop, or, offering neither, is shown its pause and launches nothing (m's
R6). The recorded run is ``_run_recorded``, the gate stage's, extracted unchanged with m's call a parameter. p's report
(``build_report`` at ``campaign``) is written once m's checkpoint records the campaign's end -- terminal (COMPLETE,
CAP, PI-STOP) or m's own STOP, nothing pending -- never at a pause; it names m's report and adjudication excerpt.
Where the end look fired at a terminal end (m:330), m's status is PAUSE and the terminal stands: p's report records
PAUSE, the terminal beside it (``campaign_terminal``), so the run and campaign-report exit as m's run does (3). The
hour cap is a positive finite int or float of hours (m's hour_cap_exceeded also takes a text or a Fraction; p's cap is
a number). A box change mid-campaign has no
restart route in this build: p passes m no checkpoint path, so a --resume on another pod reaches m's CHECKPOINT
MISMATCH (the pod id) after the load, a STOP under THE STOP below -- m:302's restart "on the new box" is the seat's to
route.

THE ORDER (the seat's Q4, a rule). Every substitution is entered before anything in the process computes renders and
before the model load. m caches the renders of record for the process (``scaffold._of_record``, lru-cached) and
``_renders_of_record`` runs once per stage, so a render computed before entry (1) would fix m's renders and stop the
stage (RENDERS MISMATCH). PIN (Code, declared at step 6): the cache is asserted empty when the substitutions are entered
(a STOP otherwise) and cleared at their exit, so neither m's renders before nor p's after cross the substitution.
``assert_single_threaded`` runs at each entry; at the stage's end, before restoration, term (d)'s state is recorded
(``register.single_thread_state``), never raised. Nothing inside the stage re-enters the register: p's schedule builder,
under entry (7)'s replacement, takes entry (2) as the stage holds it (``keys.keys_context``), so a library thread alive
after the load offends nothing (the seat's Q4).

BEFORE THE LOAD (``precheck``; a refusal exits 2 at the driver): the unit and the gate; PROPOSAL-p and PROPOSAL-m at
their sha256s (F-p8: the identity's ``proposal_sha256`` is m's); p's renders reproduce; the lexicon at its pin (F-p11);
at ``qual``, m:302's counts equal to the committed gate files' n (``counts_problems``); on a non-stub run, the lexicon
committed, the lock (``LOCK-p-OLMo-{ckpt}.md``) committed at HEAD, naming verbatim every
value ``lock_required`` lists and carrying exactly one ``BACKEND OF RECORD`` line -- and, at ``qual``, LOCK-p v0.2's
acceptance line; G-CAL-p's artifact committed and PASS for the unit; G-SHAPE-p's and G-ANL-p's committed, PASS and
recorded on the current p package (G-ANL-p's on the current analyzers too; G-SHAPE-p's sources map and import
closure too, the closure from a fresh interpreter, ``gshape_drift_problems``); the pod id; the code of record committed
(G-CAL-p's check, with scripts/p_analyze.py); the gate line. Then (``run_gate``) the stage's schedules verified by
entry (7)'s check and, at ``qual``, the prior stage, still before the load. After the load, inside the substitutions
and before m's stage: the adapter's backend identifier against the lock's line. PIN (Code, declared at step 6; worded
at the qual wiring to the seat's answer of 2026-11-09, §2 item 6 and §4 (h)): the backend identifier of record is the
lock's, never a code constant (m:302: "the backend identifier" is a LOCK v0.1 content); a backend change after the
lock STOPs the stage (before it generates); a box of the same class gives the same identifier and is not detected
(m:267); a box change follows p §6.2's respawn protocol with a new ``BACKEND — characterization`` entry, recorded by a
dated note at the lock in force, no re-issue; a differing identifier STOPs and the seat rules.

THE CALL LOG. PIN (Code, declared at step 6): ``ckpt/{U}_{gate}_p-calls.jsonl`` under the stage's root, append-only, one
ASCII JSON line per event (so a tear never splits a character and no character reads back as a line boundary), each
written and fsynced as it happens: a run line (the run's number, resume or not, the register entries entered, p's
package and PROPOSAL-p's sha256s); one line per proxy call (its index in the run, its seed, the stored text's sha256,
the cut event or none; a STOP's detail, the text and the returned text); and an end line, written in the ``finally``
(the outcome, m's status or the exception's type and message and its stop mark, the run's call and cut totals, term
(d)'s state before restoration). It is opened once every entry is in force, so a STOP while they are entered leaves
no record. It may hold contrast free-round text and counts, so it is withheld like the checkpoint (m:318) to the
unit's VERDICTS or NOT-RUN record. A resumed run appends its own lines; a torn last line, or one a failed write left
torn, is ended first. One process at a time: a ``flock`` on a lock file beside the record (``stage_lock``) spans a
run's reads, checks and appends, and the report command's (``time-report``, ``qual-report``, ``campaign-report``) read
and write.

THE STOP. PIN (Code, declared at step 6): a run that ends in a SystemExit once its run line is written -- p's STOPs
(ProxyStop, StageStop, RegisterStop, KeysStop, ScheduleStop) and m's alike, a refusal raised inside m's stage included
(p's extension of m's "a resume never lifts a STOP" to m's refusals, for the seat's word) -- or whose proxy call raised
the STOP (``stop_in`` reads the exception's whole chain) is STOPPED, and recorded twice: the marker
``ckpt/{U}_{gate}_p-STOPPED.json`` -- reserved at the run's start (``.reserve-{k}``, gitignored) and renamed into place
on the STOP, first, so recording it needs no new space and leaves no half-written marker -- then the end line's stop
mark; the STOP's cause is then written over the marker's padding, in place. A Ctrl-C from the recording's first
statement until the end line has been attempted is deferred, then raised. Every later run refuses before the load
while either record stands, while the log is unreadable, or while m's checkpoint stands beside a log with no run line
(never read as an empty record). The residual -- any STOP but a ProxyStop whose own STOP line was written: a process
killed between the STOP's raise and the rename, or the rename and the end line both failing (EIO), leaves no record;
the double failure is announced on stdout and stderr, and the reservation stays beside the record (stale
reservations are named at every later run's start and in p's report, never removed). The way out is the seat's
ruling: a restart needs the record moved aside by hand -- the call log, the marker and m's checkpoint -- as m's
PIN-37 has it; no adjudication input is defined, and a ruling to resume has no path in this build. An interruption
(any other exception, or a run with no end line) stays resumable.

P'S REPORT. PIN (Code, declared at step 6): ``reports/{U}_{gate}_p-report.json``, written once on an ended stage by
``build_report`` -- at the stage's end, or later by the driver's ``time-report``, ``qual-report`` or (from the campaign
wiring) ``campaign-report`` from the checkpoint and the call log when the stage's tail did not write it. It holds the
seat's read domain only (m:271, m:318, the seat's ruling (h)): §2.3's counters (``report.session_counters``); the proxy's cuts on the sham sessions, attributed to their
rounds through the call log by seed and stored-text sha256 (``attribute_calls``); m's report and reads named with their
sha256s (the campaign's: its report and adjudication excerpt); the register entries the stage entered; term (d)'s
end states; whether every recorded round was attributed.
Every proxy count over a contrast session is withheld: the number of its calls is its free-round exclusion position.
The self-test plants a contrast free-round exclusion at two positions, at each gate, and finds p's report and lines
unchanged; the campaign's report is built by the same function over the same fields.
"""
from __future__ import annotations

import contextlib
import fcntl
import hashlib
import json
import math
import os
import re
import signal
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping

from ..m import audit as m_audit
from ..m import banner as m_banner
from ..m import corr as m_corr
from ..m import gcal as m_gcal
from ..m import keys as m_keys
from ..m import resume as m_resume
from ..m import scaffold as m_scaffold
from ..m import schedule as m_schedule
from ..m import stages as m_stages
from . import corrupt, gcal, guard, identity, register, report
from . import keys as p_keys
from . import schedule as p_schedule
from .proxy import ProxyStop, StoredTextProxy, text_sha256

REPO = Path(__file__).resolve().parents[2]
#: Entry (6)'s replacement.
DEFAULT_OUT_P = REPO / "data" / "p"
UNITS = ("OLMo-sft", "OLMo-dpo", "OLMo-instruct")
#: The gate stages (THE QUALIFICATION); the campaign is its own move before LOCK-p v1.0 (the seat's Q2, 2026-11-10).
GATES = ("time", "qual")
#: m:302's session counts per gate, contrast then sham (m's template order): G-TIME "two sessions, one per arm";
#: G-F0m-OLMo "24 sessions ... 16 A0s-OLMo-{ckpt} ... and 8 A0-OLMo-{ckpt} contrast" -- the committed gate files' n,
#: which m's stage checks (``run_gate_stage`` refuses any other).
COUNTS = {"time": (1, 1), "qual": (8, 16)}
#: LOCK-p v0.2's acceptance line, required of the lock at ``qual`` as a whole line (THE QUALIFICATION): the text of
#: m's ``OLMO_QUAL_LOCK_LINE`` (scripts/m_sessions.py), p's licence binding no m script (the self-test compares them).
QUAL_LOCK_LINE = "G-TIME-OLMo-{ckpt} port acceptance recorded"
LOCK_TEMPLATE = "LOCK-p-OLMo-{ckpt}.md"
#: The stages p's driver runs: the two gates and, from the campaign wiring, the campaign (THE CAMPAIGN).
STAGES = GATES + ("campaign",)
#: PIN (Code, declared at the campaign wiring): the campaign's values in m's form -- scripts/m_sessions.py's
#: CAMPAIGN_LAUNCH_COUNTS and CAMPAIGN_HOUR_CAP for Q-F0 (read as text, never imported) -- passed to m's
#: stages.run_campaign as given here, their line forms required as whole lines of the unit's LOCK-p v1.0
#: (``campaign_lock_lines``). The launch counts per arm, contrast first, are G-PWR (p)'s of record
#: (data/p/gates/G-PWR-p.json), "a projection, not a bound" (m:192), bound to that record before the load
#: (``gpwr_problems``); the hour cap is the PI's cap share for the checkpoint (p §4.1, §6.1), in hours (m:249): the
#: PI's word of 2026-11-14, verbatim "2 h each", to the coordinating session's question "What hour cap per checkpoint
#: for p's campaigns?" (offered with "2 h each" and "3 h each").
CAMPAIGN_LAUNCH_COUNTS = {"OLMo-sft": (96, 64), "OLMo-dpo": (96, 64), "OLMo-instruct": (96, 64)}
CAMPAIGN_HOUR_CAP: dict = {"OLMo-sft": 2, "OLMo-dpo": 2, "OLMo-instruct": 2}
GPWR_REL = "data/p/gates/G-PWR-p.json"
GPWR_SCHEMA = "p-gpwr-v1"
#: The lock's backend line (the module docstring's BEFORE THE LOAD PIN), one per lock.
BACKEND_LINE = "BACKEND OF RECORD {bid}"
BACKEND_RX = re.compile(r"^BACKEND OF RECORD ([0-9a-f]{16})$", re.M)
ANALYZER_REL = "scripts/m_analyze.py"
P_ANALYZER_REL = "scripts/p_analyze.py"
GCAL_REL = "data/p/gates/G-CAL_completability_olmo-{ckpt}.json"
GSHAPE_REL = "data/p/gates/G-SHAPE-p.json"
GANL_REL = "data/p/gates/G-ANL-p.json"
SCHED_MANIFEST_REL = "data/p/schedules/manifest.json"
REPORT_SCHEMA = "p-stage-report-v1"
CALLS_SCHEMA = "p-stage-calls-v1"
STOPPED_SCHEMA = "p-stage-stopped-v1"
#: The STOP reservation's fixed size: its JSON padded with spaces, so the STOP's cause is written over it in place
#: after the rename, needing no new space (round 5's NOTE 4).
RESERVE_SIZE = 8192
#: The entries a gate stage enters, in order (``stage_substitutions``).
ENTERED = (1, 2, 6, 7, 8, 9)
#: m's banner components a lock names by sha256 (m:302's "banner bytes"; the session banner is
#: SESSION_BANNER + COMMON + one TOLD line, banner.build_banner).
BANNER_NAMES = ("SESSION_BANNER", "COMMON", "TOLD_MAP", "TOLD_MAP_SHAM", "TOLD_OBJ", "DECLARED_HARNESS_STRINGS")
M_AN, P_AN = "m's analyzer (scripts/m_analyze.py)", "p's analyzer (scripts/p_analyze.py)"
M_PKG, P_PKG = "m's package_sha256", "p's package_sha256"
CONTRAST_WITHHELD = ("withheld to the unit's VERDICTS or NOT-RUN record (m:318; the seat's ruling (h)): every proxy "
                     "count over the contrast session -- the number of its calls is its free-round exclusion position")
#: The qualification's form of it (eight contrast sessions; THE QUALIFICATION).
CONTRAST_WITHHELD_QUAL = ("withheld to the unit's VERDICTS or NOT-RUN record (m:318; the seat's ruling (h)): every "
                          "proxy count over the contrast sessions -- the number of a session's calls is its free-round "
                          "exclusion position")
#: p's report's three gate-worded strings, G-TIME's as written at step 6 (its records stand).
REPORT_TEXT = {
    "time": {"form": ("the seat's read domain only (m:271, m:318, the seat's ruling (h)): the sham session's counters "
                      "and proxy cuts, the contrast forced rounds' control characters, the hair trigger over every "
                      "round"),
             "contrast": CONTRAST_WITHHELD,
             "rule": ("calls attributed to rounds by seed and stored-text sha256 (stage.attribute_calls); complete: "
                      "every sham round attributed (N-3: the flag reads the sham session only)")},
    "qual": {"form": ("the seat's read domain only (m:271, m:318, the seat's ruling (h)): the sham sessions' counters "
                      "and proxy cuts, the contrast forced rounds' control characters, the hair trigger over every "
                      "round"),
             "contrast": CONTRAST_WITHHELD_QUAL,
             "rule": ("calls attributed to rounds by seed and stored-text sha256 (stage.attribute_calls); complete: "
                      "every sham round attributed (N-3: the flag reads the sham sessions only)")},
    "campaign": {"form": ("the seat's read domain only (m:271, m:318, the seat's ruling (h)): the sham sessions' "
                          "counters and proxy cuts, the contrast forced rounds' control characters, the hair trigger "
                          "over every round; written once the campaign has ended (m's ended_status) -- its status m's: "
                          "PAUSE, the terminal beside it, where the end look fired at a terminal end -- never while "
                          "the campaign is open at a pause"),
                 "contrast": CONTRAST_WITHHELD_QUAL,
                 "rule": ("calls attributed to rounds by seed and stored-text sha256 (stage.attribute_calls); "
                          "complete: every sham round attributed (N-3: the flag reads the sham sessions only)")}}


class StageRefusal(SystemExit):
    """A refusal before the load (the driver's exit 2)."""


class StageStop(SystemExit):
    """A STOP on the way (the driver's exit 4)."""


def label(unit: str, gate: str = "time") -> str:
    """The stage's name for p's unit at ``gate`` (m's spelling, ' (p)' after it); a non-unit or a non-gate is named as
    given."""
    if gate not in STAGES:
        return f"{gate!r} ({unit!r}; not a p stage, {STAGES})"
    if unit not in UNITS:
        return f"{ {'time': 'G-TIME', 'qual': 'G-F0m', 'campaign': 'campaign'}[gate]} ({unit!r}, not a p unit)"
    return f"{m_stages.stage_name(unit, gate)} (p)"


def lock_rel(unit: str) -> str:
    return LOCK_TEMPLATE.format(ckpt=gcal.unit_ckpt(unit))


def renders_sha16_m() -> str:
    """p's renders of record by m's convention (the identity's ``renders_sha16``)."""
    return m_corr.renders_sha(list(corrupt.RENDERS_OF_RECORD))


def banner_shas() -> dict[str, str]:
    return {n: hashlib.sha256(json.dumps(getattr(m_banner, n), sort_keys=True, ensure_ascii=False).encode("utf-8"))
            .hexdigest() for n in BANNER_NAMES}


def covariate_line(ckpt: str, fraction: str) -> str:
    """The covariate as a lock names it (p §3.2, m:302)."""
    return f"covariate G-CAL-p-{ckpt} (clean minus corrupted, f0's sign): {fraction}"


def backend_line(bid: str) -> str:
    return BACKEND_LINE.format(bid=bid)


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _committed_sha(rel: str) -> tuple[list[str], str | None]:
    cp, data = m_stages._committed(rel)
    if cp or data is None:
        return [f"{rel}: {x}" for x in (cp or ["unreadable"])], None
    return [], _sha(data)


def _artifact(rel: str, *, want_unit: str | None = None) -> tuple[list[str], dict | None, str | None]:
    """A committed gate artifact's problems (not committed; not JSON; not PASS; another unit), body and sha256."""
    cp, data = m_stages._committed(rel)
    if cp or data is None:
        return [f"{rel}: {x}" for x in (cp or ["unreadable"])], None, None
    try:
        art = json.loads(data.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return [f"{rel}: not JSON"], None, None
    if not isinstance(art, Mapping):
        return [f"{rel}: not a JSON object"], None, None
    probs = []
    if art.get("verdict") != "PASS":
        probs.append(f"{rel}: verdict {art.get('verdict')!r}, not PASS")
    if want_unit is not None and art.get("unit") != want_unit:
        probs.append(f"{rel}: unit {art.get('unit')!r}, not {want_unit!r}")
    return probs, art, _sha(data)


def current_shas() -> dict[str, str | None]:
    """The code of record's sha256s an artifact must carry to be current: p's and m's packages, the two analyzers."""
    def f(rel: str) -> str | None:
        p = REPO / rel
        return _sha(p.read_bytes()) if p.is_file() else None
    return {"p_package_sha256": guard.package_sha256(), "m_package_sha256": m_resume.package_sha256(),
            "m_analyzer_sha256": f(ANALYZER_REL), "p_analyzer_sha256": f(P_ANALYZER_REL)}


def stale_problems(rel: str, art: Mapping, recorded: Mapping[str, Any], fields: tuple[str, ...]) -> list[str]:
    """MINOR 9's check: each named field the artifact recorded equals the current code's (an artifact of a superseded
    package is not the gate of record)."""
    cur = current_shas()
    return [f"{rel}: recorded {f} {str(recorded.get(f))[:16]}..., the current is {str(cur[f])[:16]}... (stale: re-run "
            f"it on the current code)" for f in fields if recorded.get(f) != cur[f]]


#: FLAG (j)'s fix (the seat's answer of 2026-11-09, §4 (j), deferred to the next package move; landing with the qual
#: wiring, its answers of 2026-11-10, §1): the code a fresh ``python -I -B`` runs -- p's driver imported by path under
#: another name, never run -- printing the name and file of every loaded valence_core module, as JSON.
_CLOSURE_CODE = r'''
import importlib.util, json, sys
from pathlib import Path
repo = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(repo))
spec = importlib.util.spec_from_file_location("p_sessions_closure", repo / "scripts" / "p_sessions.py")
mod = importlib.util.module_from_spec(spec)
sys.modules["p_sessions_closure"] = mod
spec.loader.exec_module(mod)
print(json.dumps(sorted([n, str(Path(m.__file__).resolve())] for n, m in list(sys.modules.items())
                        if (n == "valence_core" or n.startswith("valence_core.")) and getattr(m, "__file__", None))))
'''


#: The fresh interpreter's bound (the qual review's N-3): a child that cannot start or does not end is a named problem.
CLOSURE_TIMEOUT_S = 600


def fresh_import_closure() -> tuple[list[str], dict]:
    """(problems, {rel: committed sha256}): G-SHAPE-p's import closure -- every loaded valence_core module outside
    valence_core/p and valence_core/m, by its file's committed blob -- as a fresh interpreter importing p's driver
    holds it (FLAG (j)'s fix): ``gshape.import_closure(committed=True)``'s filters and hashing, its module list taken
    from that interpreter, never from this process's ``sys.modules``."""
    try:
        r = subprocess.run([sys.executable, "-I", "-B", "-c", _CLOSURE_CODE, str(REPO)], capture_output=True,
                           text=True, cwd=str(REPO), timeout=CLOSURE_TIMEOUT_S)
    except (OSError, subprocess.TimeoutExpired) as e:
        why = (f"TimeoutExpired: timed out after {CLOSURE_TIMEOUT_S} s" if isinstance(e, subprocess.TimeoutExpired)
               else f"{type(e).__name__}: {e.strerror} ({e.filename})")
        return [f"the import closure: a fresh interpreter importing {guard.DRIVER_REL} could not run ({why})"], {}
    if r.returncode != 0:
        return [f"the import closure: a fresh interpreter importing {guard.DRIVER_REL} failed "
                f"({(r.stderr or '').strip().splitlines()[-1:]})"], {}
    try:
        loaded = json.loads(r.stdout.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return ["the import closure: the fresh interpreter's output is not JSON"], {}
    probs: list[str] = []
    out: dict = {}
    roots = (guard.PACKAGE_DIR.resolve(), guard.M_PACKAGE_DIR.resolve())
    repo = REPO.resolve()
    for name, f in loaded:
        p = Path(f).resolve()
        if any(rt in p.parents for rt in roots):
            continue
        if repo not in p.parents or not p.is_file():
            probs.append(f"{name}: {f} is not a regular file in the repo (import closure)")
            continue
        rel = p.relative_to(repo).as_posix()
        cp, data = m_stages._committed(rel)
        if cp or data is None:
            probs += [f"{rel}: {x}" for x in (cp or ["no bytes"])]
            out[rel] = None
            continue
        out[rel] = _sha(data)
    return probs, dict(sorted(out.items()))


def _drift(rel: str, what: str, current: tuple[list[str], Mapping], recorded: Any) -> list[str]:
    """One recorded map against the current one: the current map's problems, or the files the two differ on (stale)."""
    bp, cur = current
    probs = [f"{rel}: the current {what}: {x}" for x in bp]
    rec = recorded if isinstance(recorded, Mapping) else {}
    if not bp and dict(rec) != dict(cur):
        moved = sorted(k for k in set(rec) | set(cur) if rec.get(k) != cur.get(k))
        probs.append(f"{rel}: its recorded {what} differs from the current on {len(moved)} file(s) "
                     f"({moved[:3]}) (stale: re-run it on the current code)")
    return probs


def gshape_drift_problems(rel: str, prov: Mapping[str, Any]) -> list[str]:
    """m-3: G-SHAPE-p's recorded sources map and import closure equal the current, committed ones, so a moved driver,
    adapter or data config makes the artifact stale as a moved package does.

    PIN (Code, declared at the qual wiring; FLAG (j)'s fix): the current import closure is ``fresh_import_closure``'s,
    so the check is exact in any process -- the lock generator's, which imports m_analyze and so loads a valence_core
    module outside p and m, included; the sources map is gshape's own builder, as at step 6."""
    from . import gshape
    return (_drift(rel, "sources map", gshape.sources_map(committed=True), prov.get("sources"))
            + _drift(rel, "import closure", fresh_import_closure(), prov.get("import_closure")))


def lock_required(unit: str) -> tuple[list[str], dict[str, str]]:
    """(problems, {what: value}): every value the checkpoint's LOCK-p v0.1 -- and, at ``qual``, its v0.2 (the seat's
    answers of 2026-11-10, §3) -- must name verbatim (the seat's §4; m:302:
    that checkpoint's schedules, keys, banner bytes, the verifier, the scaffold set's assertion, its covariate, every
    later bar, the backend identifier -- the last as the lock's BACKEND line; p §4.2's licence and register; F-p8's
    proposal pins; m's licence (f) for the analyzer and m's package)."""
    ck = gcal.unit_ckpt(unit)
    probs: list[str] = []
    req: dict[str, str] = {}
    for what, rel in ((M_AN, ANALYZER_REL), (P_AN, P_ANALYZER_REL)):
        cp, sha = _committed_sha(rel)
        probs += cp
        if sha:
            req[what] = sha
    req["PROPOSAL-m (m's proposal pin, F-p8)"] = gcal.M_PROPOSAL_SHA256
    req["PROPOSAL-p (proposal_p_sha256)"] = gcal.PROPOSAL_P_SHA256
    req[M_PKG] = m_resume.package_sha256()
    req[P_PKG] = guard.package_sha256()
    gp, gart, gsha = _artifact(GCAL_REL.format(ckpt=ck), want_unit=unit)
    probs += gp
    if gsha:
        req["G-CAL-p's artifact"] = gsha
        cov = (gart.get("covariate") or {}).get("fraction")
        if isinstance(cov, str):
            req["the covariate (p §3.2)"] = covariate_line(ck, cov)
        else:
            probs.append(f"{GCAL_REL.format(ckpt=ck)}: no covariate fraction")
    for what, rel in (("G-SHAPE-p's artifact", GSHAPE_REL), ("G-ANL-p's artifact", GANL_REL)):
        ap, art, sha = _artifact(rel)
        probs += ap
        if art is not None:
            if rel == GSHAPE_REL:
                probs += stale_problems(rel, art, art.get("provenance") or {}, ("p_package_sha256", "m_package_sha256"))
                probs += gshape_drift_problems(rel, art.get("provenance") or {})
            else:
                probs += stale_problems(rel, art, art.get("code") or {}, ("p_package_sha256", "m_package_sha256",
                                                                          "m_analyzer_sha256", "p_analyzer_sha256"))
        if sha:
            req[what] = sha
    req["p's renders, m's convention (sha16)"] = renders_sha16_m()
    req["p's renders, p's convention (sha256)"] = corrupt.sha_p(list(corrupt.RENDERS_OF_RECORD))
    req["the lexicon (F-p11)"] = report.LEXICON_SHA256
    mp, msha = _committed_sha(SCHED_MANIFEST_REL)
    probs += mp
    if msha:
        req["p's schedules manifest"] = msha
        man = json.loads((REPO / SCHED_MANIFEST_REL).read_text(encoding="utf-8")).get("files", {})
        for name in sorted(n for n in man if n.startswith(f"{unit}_")):
            req[f"schedule {name}"] = man[name]
    for n, v in banner_shas().items():
        req[f"banner {n}"] = v
    req["the OLMo ban list (sha16)"] = m_audit.OLMO_BAN_IDS_SHA16
    sp, ssha = _committed_sha(f"data/olmo/scaffold_{ck}.json")
    probs += sp
    if ssha:
        req[f"the OLMo scaffold set (data/olmo/scaffold_{ck}.json)"] = ssha
    drv = guard.driver_sha256()
    if drv:
        req["the driver (scripts/p_sessions.py)"] = drv
    for ln in guard.licence_lines():
        req[f"licence line: {ln.split(' sha256 ')[0].split(' package_sha256 ')[0]}"] = ln
    for e in register.table():
        req[f"register entry ({e['n']})"] = "REGISTER " + json.dumps(e, sort_keys=True, ensure_ascii=False)
    return probs, req


def lock_names(text: str, value: str) -> bool:
    """N-4: a lock names a value as a whole line (a code block's LICENCE, REGISTER and BACKEND lines) or between
    backticks (every other value the generator writes) -- never as a bare substring."""
    return f"`{value}`" in text or any(ln.strip() == value for ln in text.splitlines())


def lock_backend(text: str) -> tuple[list[str], str | None]:
    """The lock's backend identifier of record: exactly one ``BACKEND OF RECORD`` line."""
    found = BACKEND_RX.findall(text)
    if len(found) != 1:
        return [f"the lock carries {len(found)} 'BACKEND OF RECORD' lines; exactly one is required (m:302)"], None
    return [], found[0]


def templates_counts(unit: str, gate: str = "time") -> list[tuple[str, int]]:
    """m:302's counts at ``gate`` (``COUNTS``), in m's template order, contrast first (the committed gate files' n,
    which m's stage checks)."""
    contrast, sham = m_keys.templates(unit)
    nc, ns = COUNTS[gate]
    return [(contrast, nc), (sham, ns)]


def counts_problems(unit: str, gate: str) -> list[str]:
    """THE QUALIFICATION (the qual review's N-4): m:302's counts at ``gate`` equal the committed gate files' n, before the
    load; m's stage checks them again after it (a ValueError there, not a refusal)."""
    out: list[str] = []
    for t, n in templates_counts(unit, gate):
        rel = f"data/p/schedules/{unit}_{gate}_{t}.json"
        cp, data = m_stages._committed(rel)
        if cp or data is None:
            out += [f"{rel}: {x}" for x in (cp or ["no bytes"])]
            continue
        try:
            got = json.loads(data.decode("utf-8")).get("n")
        except (ValueError, UnicodeDecodeError, AttributeError):
            out.append(f"{rel}: not a JSON object")
            continue
        if got != n:
            out.append(f"{rel}: n {got!r}, not m:302's {n} at {gate} (COUNTS)")
    return out


def qual_lock_problems(unit: str, text: str) -> list[str]:
    """THE QUALIFICATION: the lock carries LOCK-p v0.2's acceptance line for its checkpoint as a whole line."""
    line = QUAL_LOCK_LINE.format(ckpt=gcal.unit_ckpt(unit))
    if any(ln.strip() == line for ln in text.splitlines()):
        return []
    return [f"it does not carry LOCK-p v0.2's line '{line}' as a whole line (m:302: G-F0m-OLMo runs under the "
            f"checkpoint's v0.2, which records G-TIME-OLMo's port acceptance; v0.1's text is refused here)"]


def identity_extra(unit: str, *, stub: bool, lock_bytes: bytes) -> dict:
    """What m's stage cannot derive: the lock's sha256 and file, m's proposal pin and file (F-p8), p's renders by m's
    convention, the uncached path, m's analyzer and package sha256s."""
    out = {"lock_sha256": _sha(lock_bytes), "proposal_sha256": gcal.M_PROPOSAL_SHA256,
           "renders_sha16": renders_sha16_m(), "locked_path": "uncached", "proposal_file": gcal.M_PROPOSAL_REL,
           "analyzer_sha256": _sha((REPO / ANALYZER_REL).read_bytes()),
           "package_sha256": m_resume.package_sha256()}
    if not stub:
        out["lock_file"] = lock_rel(unit)
    return out


def prior_problems(unit: str, prior_ckpt: Path, *, stub: bool, proposal_sha256: str, stage: str = "qual") -> list[str]:
    """Before the load, at ``stage`` -- the qualification (its prior G-TIME (p)'s checkpoint) or the campaign (its
    prior the qualification's): m's ``prior_gate`` on the prior's checkpoint (no adjudication, no earlier proposal
    re-adopted, ``require_real`` on a non-stub run), then that the checkpoint is p's -- its identity's ``proposal`` and
    ``proposal_p_sha256`` this run's (the qual review's N-5)."""
    try:
        m_stages.prior_gate(unit, stage, prior_ckpt, None, proposal_sha256=proposal_sha256,
                            prior_proposal_sha256s=(), require_real=not stub)
    except (SystemExit, ValueError) as e:
        return [f"m's prior_gate: {e}"]
    try:
        ident = m_resume.read_checkpoint(prior_ckpt).get("identity") or {}
    except SystemExit as e:
        return [f"the prior's checkpoint: {e}"]
    want = identity.run_values()
    return [f"the prior is not p's: its identity's {k} is {str(ident.get(k))[:24]!r}, not this run's "
            f"{str(want[k])[:24]!r}" for k in ("proposal", "proposal_p_sha256") if ident.get(k) != want[k]]


def precheck(unit: str, *, stub: bool, resume: bool = False, lexicon: Path | None = None, gate: str = "time") -> dict:
    """Every refusal that needs no adapter (the module docstring's BEFORE THE LOAD); StageRefusal on the first set.
    ``lexicon``: the lexicon's path (default the pinned file; the self-test's refusal case only)."""
    name = label(unit, gate)
    if gate not in STAGES:
        raise StageRefusal(f"{name} REFUSED: p's stages are {STAGES}")
    if unit not in UNITS:
        raise StageRefusal(f"{name} REFUSED: p's units are {UNITS}")
    probs: list[str] = []
    try:
        got = _sha((REPO / gcal.PROPOSAL_P_REL).read_bytes())
    except OSError:
        got = None
    if got != gcal.PROPOSAL_P_SHA256:
        probs.append(f"{gcal.PROPOSAL_P_REL} hashes to {str(got)[:16]}, not p v0.2's {gcal.PROPOSAL_P_SHA256[:16]}")
    mcp, msha = _committed_sha(gcal.M_PROPOSAL_REL)
    probs += mcp
    if msha is not None and msha != gcal.M_PROPOSAL_SHA256:
        probs.append(f"{gcal.M_PROPOSAL_REL} hashes to {msha[:16]}, not PROPOSAL-m v1.11's (F-p8)")
    rp = corrupt.renders_problems()                 # a register STOP propagates (the driver's exit 4)
    if rp:
        raise StageStop(f"{name} STOP: p's renders of record do not reproduce: {rp}")
    try:
        report.load_lexicon(lexicon)
    except report.LexiconStop as e:
        probs.append(f"the lexicon: {e}")
    probs += [f"register entry ({n}) is not admitted ({register.BY_N[n].status}); the stage enters it (round 3's m-3)"
              for n in ENTERED if register.BY_N[n].status not in register.SUBSTITUTABLE]
    if gate == "qual":
        probs += [f"the counts: {p}" for p in counts_problems(unit, gate)]
    if gate == "campaign" and campaign_hour_cap(unit) is None:
        probs.append(f"the hour cap is not set: the PI's cap share for {unit} (p §4.1, §6.1) is a LOCK-p v1.0 value, "
                     f"and this build carries none")
    wp, weights = m_gcal.weights_of_record(gcal.unit_ckpt(unit))
    probs += [f"weights of record: {p}" for p in wp]
    lock_bytes, gline, req, bid = b"LOCK-p stub: no lock file on the self-test stub", None, {}, None
    if not stub:
        lcp, _ = _committed_sha(report.LEXICON_REL)
        probs += [f"committed: {p}" for p in lcp]
        cp, data = m_stages._committed(lock_rel(unit))
        probs += [f"{lock_rel(unit)}: {x}" for x in cp]
        rprobs, req = lock_required(unit)
        probs += rprobs
        if gate == "campaign":
            gp, gsha = gpwr_problems(unit)
            probs += gp
            if gsha:
                req["G-PWR (p)'s record"] = gsha
        if data is not None:
            lock_bytes = data
            ltext = data.decode("utf-8", "replace")
            probs += [f"{lock_rel(unit)} does not name {what} ({v[:16]}...)" for what, v in req.items()
                      if not lock_names(ltext, v)]
            bp, bid = lock_backend(ltext)
            probs += [f"{lock_rel(unit)}: {p}" for p in bp]
            if gate == "qual":
                probs += [f"{lock_rel(unit)}: {p}" for p in qual_lock_problems(unit, ltext)]
            if gate == "campaign":
                probs += [f"{lock_rel(unit)}: {p}" for p in campaign_lock_problems(unit, ltext)]
        if m_resume.pod_id() is None:
            probs.append(f"POD ID ABSENT: {name} runs on the box only with its pod instance id "
                         f"(${m_resume.POD_ENV}), as every OLMo stage")
        probs += [f"committed: {p}" for p in gcal.committed_problems()]
        pcp, _ = _committed_sha(P_ANALYZER_REL)
        probs += [f"committed: {p}" for p in pcp]
        line, gp = m_stages.gate_line(name, REPO / gcal.PROPOSAL_P_REL)
        probs += [f"gate line: {p}" for p in gp]
        ppc, ppsha = _committed_sha(gcal.PROPOSAL_P_REL)
        probs += [f"committed: {p}" for p in ppc]
        if ppsha is not None and ppsha != gcal.PROPOSAL_P_SHA256:
            probs.append(f"{gcal.PROPOSAL_P_REL}: committed sha256 {ppsha[:16]}..., not p v0.2's")
        ccp, _ = _committed_sha("CLAUDE.md")
        probs += [f"committed: {p}" for p in ccp]
        gline = {"line": line}
    if probs:
        raise StageRefusal(f"{name} REFUSED: {probs}")
    return {"unit": unit, "gate": gate, "ckpt": gcal.unit_ckpt(unit), "stub": stub, "lock_bytes": lock_bytes,
            "gate_line": gline, "lock_required": req, "backend_of_record": bid, "weights": weights,
            "identity_extra": identity_extra(unit, stub=stub, lock_bytes=lock_bytes)}


@contextlib.contextmanager
def stage_substitutions() -> Iterator[list[int]]:
    """Entries (1), (2), (6)-(9), entered in that order before anything computes renders and before the load (the
    seat's Q4); the renders cache asserted empty at the entry and cleared at the exit (the module docstring's PIN).
    Yields the entries entered."""
    entered: list[int] = []
    with contextlib.ExitStack() as es:
        for n, mod, vals in ((1, m_corr, {"_eligible_m": corrupt.eligible_p}), (2, m_keys, p_keys.P_FUNCS),
                             (6, m_stages, {"DEFAULT_OUT": DEFAULT_OUT_P}),
                             (7, m_schedule, {"verify_schedule_dir": p_schedule.verify_schedule_dir}),
                             (8, m_resume, {"IDENTITY_KEYS_OLMO": identity.IDENTITY_KEYS_OLMO_P}),
                             (9, m_resume, {"Identity": identity.identity_p})):
            es.enter_context(register.substituted(n, mod, vals))
            entered.append(n)
        if tuple(entered) != ENTERED:               # unreachable: the loop is the declared order
            raise StageStop(f"STAGE STOP: entries {entered} entered, not {ENTERED}")
        if m_scaffold._of_record.cache_info().currsize:
            raise StageStop("STAGE STOP: m's renders of record were cached before entry (1) was entered "
                            "(scaffold._of_record); the substitutions are entered before anything computes renders "
                            "(the seat's Q4) -- nothing loaded")
        es.callback(m_scaffold._of_record.cache_clear)
        yield list(entered)


def out_paths(unit: str, out: Path, *, gate: str = "time") -> dict[str, Path]:
    """p's two outputs and m's checkpoint, report and reads under the stage's root, at ``gate``."""
    if gate not in STAGES:
        raise ValueError(f"{gate!r} is not one of p's stages {STAGES}")
    mp = m_stages.out_paths(unit, gate, out)
    mp = m_stages.for_checkpoint(mp, m_stages.checkpoint_path(None, mp))
    out_ = {"p_report": out / "reports" / f"{unit}_{gate}_p-report.json",
            "p_calls": out / "ckpt" / f"{unit}_{gate}_p-calls.jsonl",
            "p_stopped": out / "ckpt" / f"{unit}_{gate}_p-STOPPED.json",
            "p_lock": out / "ckpt" / f"{unit}_{gate}_p.lock",
            "m_ckpt": mp["ckpt"], "m_report": mp["report"]}
    if gate == "campaign":                          # m's campaign writes no reads; its pause excerpt sits beside it
        out_["m_excerpt"] = m_stages.adjudication_path(mp["ckpt"])
    else:
        out_["m_reads"] = mp["reads"]
    return out_


class CallLog:
    """The stage's write-ahead call log (the module docstring's PIN): append-only JSON lines, each fsynced."""

    def __init__(self, path: Path, root: Path) -> None:
        self.path = Path(path)
        lp = guard.no_link_problems(self.path.parent, root)
        if lp:
            raise StageRefusal(f"P CALL LOG REFUSED: {lp}")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.dirty = False
        self.fd: int | None = os.open(self.path, os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_NOFOLLOW, 0o644)
        try:
            size = os.fstat(self.fd).st_size
            self.dirty = bool(size) and os.pread(self.fd, 1, size - 1) != b"\n"
            if self.dirty:
                self._put(b"")                        # m-1: a torn last line (a crash mid-write) ends here, alone
        except BaseException:
            os.close(self.fd)
            self.fd = None
            raise

    def _put(self, data: bytes) -> None:
        # A line a failed write left torn (``dirty``) is ended before anything else is appended (round 4's NOTE 2); a
        # write that fails before its first byte leaves the tail as it was (round 5's NOTE 5).
        if self.dirty:
            data = b"\n" + data
        view = memoryview(data)
        wrote = 0
        try:
            while view:
                n = os.write(self.fd, view)
                wrote += n
                view = view[n:]
        except BaseException:
            if wrote:
                self.dirty = True
            raise
        self.dirty = False
        os.fsync(self.fd)

    def write(self, rec: Mapping[str, Any]) -> None:
        # ASCII-only (round 3's MAJOR): every byte of a line is one character, so a tear can never split one, and no
        # character beyond ASCII (U+0085, U+2028, U+2029 among them) can read back as a line boundary.
        self._put((json.dumps(rec, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii"))

    def close(self) -> None:
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None


def read_calls(path: Path) -> tuple[list[dict], list[str]]:
    """The call log's events and its problems (an unreadable file, a malformed line)."""
    p = Path(path)
    if not p.exists():
        return [], [f"{p.name}: absent"]
    try:
        data = p.read_bytes()
    except OSError as e:
        return [], [f"{p.name}: unreadable ({type(e).__name__})"]
    pieces = data.split(b"\n")                     # the log's own line ending only (round 3's MAJOR, m-2)
    if pieces and pieces[-1] == b"":
        pieces.pop()
    out, probs = [], []
    for i, raw in enumerate(pieces, 1):
        try:
            ev = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            probs.append(f"{p.name}:{i}: not JSON")
            continue
        if not isinstance(ev, dict) or ev.get("event") not in ("run", "call", "end"):
            probs.append(f"{p.name}:{i}: not a call-log event")
            continue
        out.append(ev)
    return out, probs


#: The module docstring's THE STOP: a run whose end line carries the stop mark, or whose call raised the proxy's STOP.
def stopped_runs(events: list[Mapping]) -> list[int]:
    return sorted({e.get("run") for e in events
                   if (e.get("event") == "end" and isinstance(e.get("exception"), Mapping) and e["exception"].get("stop"))
                   or (e.get("event") == "call" and "stop" in e)})


def reserve_path(marker: Path, run: int) -> Path:
    """The STOP's reservation for run ``run``: beside the marker, gitignored (no ``.json`` ending)."""
    return Path(marker).with_name(f"{Path(marker).name}.reserve-{run}")


def _stopped_doc(unit: str, gate: str, run: int, cause: Mapping[str, Any] | None) -> bytes:
    doc = {"schema": STOPPED_SCHEMA, "stage": label(unit, gate), "unit": unit, "run": run,
           "rule": "the seat adjudicates before anything resumes (the seat's Q5)",
           "detail": "reserved at the run's start and renamed into place on a STOP; the cause is written over the "
                     "padding afterwards (best-effort; the run's end line has it too, when it is written)",
           "cause": cause}
    data = m_resume.json_text(doc, indent=1).encode("utf-8")
    if len(data) > RESERVE_SIZE:
        raise ValueError(f"the STOP record is {len(data)} bytes, over its reservation's {RESERVE_SIZE}")
    return data + b" " * (RESERVE_SIZE - len(data))


def _fill_cause(path: Path, unit: str, gate: str, run: int, err: BaseException | None) -> None:
    """Best-effort: the STOP's type and message over the marker's padding, in place (no new space)."""
    msg = str(err) if err is not None else ""
    for cut in (4000, 1000, 200, 0):
        try:
            data = _stopped_doc(unit, gate, run, {"type": type(err).__name__ if err is not None else None,
                                                  "message": msg[:cut]})
            break
        except ValueError:
            continue
    else:
        return
    fd = os.open(path, os.O_WRONLY | os.O_NOFOLLOW)
    try:
        os.pwrite(fd, data, 0)
        os.fsync(fd)
    finally:
        os.close(fd)


def _safe_echo(echo: Callable[[str], None], line: str) -> None:
    """An echo that cannot break the STOP's recording (round 4's m-1)."""
    try:
        echo(line)
    except BaseException:                           # noqa: BLE001 -- a broken stdout must not lose a record
        pass


def stop_in(err: BaseException | None) -> bool:
    """A SystemExit anywhere on the exception's chain (round 3's m-1: an OSError raised while a STOP was handled
    still ends a STOPPED run)."""
    seen: set[int] = set()
    e = err
    while e is not None and id(e) not in seen:
        seen.add(id(e))
        if isinstance(e, SystemExit):
            return True
        e = e.__cause__ or e.__context__
    return False


@contextlib.contextmanager
def stage_lock(path: Path, root: Path, *, what: str = "this stage") -> Iterator[None]:
    """PIN (Code, declared at step 6): one process on a stage's record at a time -- an exclusive, non-blocking
    ``flock`` on a lock file beside the record (``ckpt/{U}_{gate}_p.lock``; gitignored), held by a run from before the
    record is read to the end of the run, and by its report command (``time-report``, ``qual-report``,
    ``campaign-report``) for its read
    and write (round 3's NOTE 4; round 4's NOTE 3). Only a lock held elsewhere (BlockingIOError) reads as "held"; any
    other failure is named (round 4's m-2). On the box the file lies on the network volume (nfs4), where a model-free
    probe found the lock exclusive across processes on one pod and released on close
    (results/raw/2026-11-09_p-step6_flock-probe.txt); exclusion across pods is not probed, and a lock a terminated pod
    held may persist for the server's lease (fail-closed: read as held)."""
    lp = guard.no_link_problems(Path(path).parent, root)
    if lp:
        raise StageRefusal(f"{what} REFUSED: the stage lock's path: {lp}")
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o644)
    except OSError as e:
        raise StageRefusal(f"{what} REFUSED: the stage lock cannot be opened ({type(e).__name__}: {e.strerror}) -- "
                           f"nothing read or loaded") from None
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise StageRefusal(f"{what} REFUSED: another process holds the stage's lock ({Path(path).name}) -- "
                               f"nothing read or loaded") from None
        except OSError as e:
            raise StageRefusal(f"{what} REFUSED: the stage lock is unavailable on this filesystem "
                               f"({type(e).__name__} {e.errno}: {e.strerror}) -- nothing read or loaded; the seat "
                               f"routes a lock on another path") from None
        yield
    finally:
        os.close(fd)


def log_consistency_problems(unit: str, events: list[Mapping], *, gate: str = "time") -> list[str]:
    """m-1: the log is this stage's -- every run line's schema, unit and stage this stage's (the gate's own: a G-TIME
    log is not a G-F0m-OLMo one); runs numbered 1..K, each once; at most one end line per run, and every call and end
    line naming a run the log holds."""
    runs = [e for e in events if e.get("event") == "run"]
    want = (CALLS_SCHEMA, unit, label(unit, gate))
    probs = [f"run line {i + 1}: not this stage's ({r.get('schema')!r}, {r.get('unit')!r}, {r.get('stage')!r})"
             for i, r in enumerate(runs) if (r.get("schema"), r.get("unit"), r.get("stage")) != want]
    nums = [r.get("run") for r in runs]
    if nums != list(range(1, len(nums) + 1)):
        probs.append(f"run numbers {nums}, not 1..{len(nums)} each once")
    ends = [e.get("run") for e in events if e.get("event") == "end"]
    if len(ends) != len(set(ends)) or not set(ends) <= set(nums):
        probs.append("an end line names no run of the log, or a run twice")
    if not {e.get("run") for e in events if e.get("event") == "call"} <= set(nums):
        probs.append("a call line names no run of the log")
    return probs


def attribute_calls(sessions: list[Mapping], events: list[Mapping]) -> dict:
    """The call log's calls attributed to the checkpoint's rounds (the module docstring's PIN): by seed (a round's own,
    drawn from its arm stream) and the stored text's sha256; a seed shared by two recorded rounds attributes neither
    (never a guess); where several calls match one round (a resumed session re-run), the last in the log is the one
    the round records. Returns {by_round: {round key: call event}, n_orphans, missing: [round keys], problems}."""
    rounds = [(rec, r) for rec in sessions for r in rec.get("rounds", ())]
    by_seed: dict[int, list] = {}
    problems: list[str] = []
    for rec, r in rounds:
        if type(r.get("seed")) is not int:
            problems.append("a recorded round carries no int seed")
            continue
        by_seed.setdefault(r["seed"], []).append((rec, r))
    if any(len(v) > 1 for v in by_seed.values()):
        problems.append("two recorded rounds share a seed; neither is attributed")
    by_round: dict[str, Mapping] = {}
    n_orphans = 0
    for e in events:
        if e.get("event") != "call":
            continue
        hit = by_seed.get(e.get("seed"), [])
        if len(hit) != 1 or e.get("text_sha256") != text_sha256(str(hit[0][1].get("text"))):
            n_orphans += 1
            continue
        by_round[report.round_key(*hit[0])] = e
    missing = [report.round_key(rec, r) for rec, r in rounds if report.round_key(rec, r) not in by_round]
    return {"by_round": by_round, "n_orphans": n_orphans, "missing": missing, "problems": problems}


def _rel_to(p: Path, root: Path) -> str:
    try:
        return Path(p).resolve().relative_to(Path(root).resolve()).as_posix()
    except ValueError:
        return Path(p).name


def build_report(unit: str, out: Path, *, gate: str = "time") -> dict:
    """p's report from m's checkpoint and the call log (the module docstring's P'S REPORT); StageStop unless the stage
    has ended and the call log's runs were run by the current p package."""
    name = label(unit, gate)
    pp = out_paths(unit, Path(out), gate=gate)
    root = Path(out)
    try:
        ckb = pp["m_ckpt"].read_bytes()
        ck = json.loads(ckb.decode("utf-8"))
    except (OSError, ValueError, UnicodeDecodeError) as e:
        raise StageStop(f"{name} P-REPORT STOP: m's checkpoint {pp['m_ckpt'].name} unreadable "
                        f"({type(e).__name__})") from None
    camp_terminal = None
    if gate == "campaign":                          # THE CAMPAIGN: ended (terminal or STOP), nothing pending
        status = m_resume.ended_status(ck) if isinstance(ck, dict) else None
        if status is None or m_resume.pending_end(ck) is not None:
            raise StageStop(f"{name} P-REPORT STOP: m's checkpoint records no campaign end (a pause is not one); "
                            f"p's report is built on an ended campaign only")
        camp = ck.get("campaign") if isinstance(ck.get("campaign"), Mapping) else {}
        pauses = camp.get("pauses") if isinstance(camp.get("pauses"), list) else []
        last = pauses[-1] if pauses else None
        if (isinstance(camp.get("terminal"), Mapping) and isinstance(last, Mapping)
                and last.get("kind") == "end_look" and last.get("adjudication") is None):
            # m:330 (stages._campaign_end): a fired end look pauses the unit before its analysis -- the run's status
            # is PAUSE and the terminal state stands; p's report records m's status, the terminal beside it
            camp_terminal, status = status, "PAUSE"
        end = {"status": status}
    else:
        end = ck.get("stage_end")
    if not isinstance(end, Mapping) or "status" not in end:
        raise StageStop(f"{name} P-REPORT STOP: m's checkpoint carries no persisted stage end; p's report is "
                        f"built on an ended stage only")
    events, lp = read_calls(pp["p_calls"])
    fatal = [x for x in lp if x.endswith(": absent") or ": unreadable (" in x]
    if fatal:
        raise StageStop(f"{name} P-REPORT STOP: the call log is {fatal[0].split(': ', 1)[1]}; p's report is built "
                        f"from it alone")
    cons = log_consistency_problems(unit, events, gate=gate)
    if cons:
        raise StageStop(f"{name} P-REPORT STOP: the call log is not this stage's: {cons[:3]}")
    runs = [e for e in events if e.get("event") == "run"]
    ends = [e for e in events if e.get("event") == "end"]
    pkgs = sorted({str(r.get("p_package_sha256")) for r in runs})
    if pkgs != [guard.package_sha256()]:
        raise StageStop(f"{name} P-REPORT STOP: the call log's runs ran under p package(s) "
                        f"{[x[:16] for x in pkgs]}, not the current {guard.package_sha256()[:16]}; p's report is built "
                        f"by the package that ran the stage")
    sessions = list(ck.get("sessions", []))
    att = attribute_calls(sessions, events)
    counters = report.session_counters(sessions, m_corr.load_pool())
    sham_keys = [report.round_key(rec, r) for rec in sessions if not rec["contrast"] for r in rec.get("rounds", ())]
    sham_att = {k: att["by_round"].get(k) for k in sham_keys}
    entered = sorted({tuple(r.get("register_entered") or ()) for r in runs})
    by_end = {e["run"]: e for e in ends}
    run_rows = []
    for r in runs:
        e = by_end.get(r["run"])
        exc = e.get("exception") if e is not None and isinstance(e.get("exception"), Mapping) else None
        run_rows.append({"run": r["run"], "resume": bool(r.get("resume")),
                         "outcome": e.get("outcome") if e is not None else "no end line (the process ended first)",
                         "exception_type": exc.get("type") if exc else None, "stop": bool(exc and exc.get("stop"))})

    def named(p: Path) -> dict:
        return {"path": _rel_to(p, root), "sha256": _sha(p.read_bytes()) if p.is_file() else None}
    return {"schema": REPORT_SCHEMA, "stage": name, "unit": unit, "status": end["status"],
            **({"campaign_terminal": camp_terminal} if camp_terminal is not None else {}),
            "form": REPORT_TEXT[gate]["form"],
            "root": "data/p" if root.resolve() == DEFAULT_OUT_P.resolve() else "(a test root)",
            "checkpoint": {"path": _rel_to(pp["m_ckpt"], root), "sha256": _sha(ckb)},
            "m_outputs": ({"report": named(pp["m_report"]), "adjudication_excerpt": named(pp["m_excerpt"])}
                          if gate == "campaign" else {"report": named(pp["m_report"]), "reads": named(pp["m_reads"])}),
            "call_log": {**named(pp["p_calls"]), "n_runs": len(runs), "runs": run_rows,
                         "well_formed": not lp, "n_malformed_lines": len(lp),
                         "stale_reservations": sorted(x.name for x in pp["p_stopped"].parent.glob(
                             pp["p_stopped"].name + ".reserve-*")),
                         "form": "withheld like the checkpoint (m:318); its runs' totals are in it"},
            "identity_p": {k: ck["identity"].get(k) for k in identity.P_FIELDS},
            "proposal_sha256": ck["identity"].get("proposal_sha256"),
            "proposal_p_sha256": identity.PROPOSAL_P_SHA256,
            "p_package_sha256": guard.package_sha256(),
            "counters": counters,
            "proxy": {"sham": {"n_rounds": len(sham_keys), "n_attributed": sum(v is not None for v in sham_att.values()),
                               "n_cuts": sum(1 for v in sham_att.values() if v is not None and v.get("cut")),
                               "cut_keys": [k for k, v in sham_att.items() if v is not None and v.get("cut")],
                               "unattributed_keys": [k for k, v in sham_att.items() if v is None]},
                      "contrast": REPORT_TEXT[gate]["contrast"],
                      "attribution_complete": all(v is not None for v in sham_att.values()),
                      "rule": REPORT_TEXT[gate]["rule"]},
            "term_d_at_stage_end": [e.get("term_d_at_stage_end") for e in ends],
            "register_entered": list(entered[0]) if len(entered) == 1 else [list(x) for x in entered],
            "disclosure": gcal.DISCLOSURE, "declared_sentences": report.declared_sentences(unit)}


def write_report(unit: str, out: Path, *, gate: str = "time") -> tuple[dict, str]:
    rep = build_report(unit, out, gate=gate)
    how = guard.write_once_bytes(out_paths(unit, Path(out), gate=gate)["p_report"],
                                 m_resume.json_text(rep, indent=1).encode("utf-8"), what="p's report")
    return rep, how


def run_gate(unit: str, gate: str, adapter_factory: Callable[[], Any], *, stub: bool = False, resume: bool = False,
             out_root=None, pre: Mapping[str, Any] | None = None,
             echo: Callable[[str], None] = lambda s: print(s, flush=True)) -> dict:
    """G-TIME-OLMo (p) or G-F0m-OLMo (p) on one checkpoint (the module docstring); ``pre``: the driver's own precheck
    of this run. The campaign is ``run_campaign``'s, refused here before anything (the campaign review's MINOR-1)."""
    if gate not in GATES:
        raise StageRefusal(f"{label(unit, gate)} REFUSED: run_gate runs p's gates {GATES}; the campaign runs by "
                           f"run_campaign -- nothing loaded")
    pre = precheck(unit, stub=stub, resume=resume, gate=gate) if pre is None else pre
    if pre.get("unit") != unit or pre.get("gate") != gate or pre.get("stub") is not stub:
        raise StageRefusal(f"{label(unit, gate)} REFUSED: the precheck given is {pre.get('unit')!r}'s at "
                           f"{pre.get('gate')!r} with stub {pre.get('stub')!r}; this run is {unit!r} at {gate!r} with "
                           f"stub {stub!r}")
    if stub:
        out = guard.refuse_test_out(out_root)
    elif out_root is not None:
        raise StageRefusal(f"{label(unit, gate)} REFUSED: a non-stub run writes data/p only (ledger 27)")
    else:
        out = DEFAULT_OUT_P
    pp = out_paths(unit, out, gate=gate)
    with stage_lock(pp["p_lock"], out, what=label(unit, gate)):
        return _run_gate_locked(unit, gate, adapter_factory, stub=stub, resume=resume, out=out, pp=pp, pre=pre,
                                echo=echo)


def run_time(unit: str, adapter_factory: Callable[[], Any], **kw) -> dict:
    """G-TIME-OLMo (p): ``run_gate`` at ``time``."""
    return run_gate(unit, "time", adapter_factory, **kw)


def _run_gate_locked(unit, gate, adapter_factory, *, stub, resume, out, pp, pre, echo) -> dict:
    name = label(unit, gate)
    if pp["p_report"].exists():
        raise StageRefusal(f"{name} REFUSED: p's report exists ({pp['p_report'].name}); the stage has ended and "
                           f"been reported")
    if pp["p_stopped"].exists() or pp["p_stopped"].is_symlink():
        raise StageRefusal(f"{name} REFUSED: the stage is STOPPED ({pp['p_stopped'].name}); the seat adjudicates "
                           f"before anything resumes (the seat's Q5; a resume never lifts a STOP) -- nothing loaded")
    if pp["p_calls"].exists() and not resume:
        raise StageRefusal(f"{name} REFUSED: the call log exists ({pp['p_calls'].name}); a second run is a "
                           f"--resume, which appends to it")
    if pp["m_ckpt"].exists() and not resume:
        raise StageRefusal(f"{name} REFUSED: m's checkpoint exists ({pp['m_ckpt'].name}); pass --resume to "
                           f"continue it (m's CHECKPOINT EXISTS, before the load) -- nothing loaded")
    if resume and pp["m_ckpt"].exists() and not pp["p_calls"].exists():
        raise StageRefusal(f"{name} REFUSED: m's checkpoint exists but p's call log does not -- the earlier runs' "
                           f"record is lost; the seat adjudicates (ledger 27) -- nothing loaded")
    try:
        ended = isinstance(json.loads(pp["m_ckpt"].read_text(encoding="utf-8")).get("stage_end"), Mapping)
    except (OSError, ValueError):
        ended = False
    if ended:
        raise StageRefusal(f"{name} REFUSED: m's checkpoint records the stage's end; p's report is re-derived "
                           f"from it with the driver's {gate}-report, never by a re-run")
    events, lp = read_calls(pp["p_calls"])
    unreadable = [x for x in lp if ": unreadable (" in x]
    if unreadable:                                  # fail closed (round 3's MAJOR)
        raise StageRefusal(f"{name} REFUSED: the call log is unreadable ({unreadable[0]}); a run never reads "
                           f"an unreadable record as an empty one -- the seat adjudicates; nothing loaded")
    stops = stopped_runs(events)
    if stops:
        raise StageRefusal(f"{name} REFUSED: run(s) {stops} of this stage ended in a STOP; the seat adjudicates "
                           f"before anything resumes (the seat's Q5; a resume never lifts a STOP) -- nothing loaded")
    if pp["m_ckpt"].exists() and not any(e.get("event") == "run" for e in events):
        raise StageRefusal(f"{name} REFUSED: m's checkpoint exists but the call log holds no run line -- the "
                           f"record is damaged, never read as an empty one; the seat adjudicates -- nothing loaded")
    cons = log_consistency_problems(unit, events, gate=gate)
    if cons:
        raise StageRefusal(f"{name} REFUSED: the call log is not this stage's: {cons[:3]} -- nothing loaded")
    sp = p_schedule.verify_schedule_dir(out / "schedules")
    if sp:
        raise StageRefusal(f"{name} REFUSED: the schedules at {_rel_to(out / 'schedules', REPO)} are not "
                           f"clean (entry (7)'s check, before the load): {sp[:3]}")
    prior_ckpt = None
    if gate == "qual":                              # THE QUALIFICATION: the prior, before the load
        prior_ckpt = out_paths(unit, out, gate="time")["m_ckpt"]
        pp_ = prior_problems(unit, prior_ckpt, stub=stub, proposal_sha256=pre["identity_extra"]["proposal_sha256"])
        if pp_:
            raise StageRefusal(f"{name} REFUSED: the prior stage (before the load): {pp_} -- nothing recorded or "
                               f"loaded")
    res = _run_recorded(unit, gate, adapter_factory, stub=stub, resume=resume, out=out, pp=pp, pre=pre, echo=echo,
                        events=events,
                        call_m=lambda px: m_stages.run_gate_stage(
                            px, unit=unit, gate=gate, templates_counts=templates_counts(unit, gate),
                            identity_extra=pre["identity_extra"], substrate="olmo", out_root=out, resume=resume,
                            prior_ckpt=prior_ckpt))
    try:
        rep, how = write_report(unit, out, gate=gate)
    except SystemExit as e:
        raise StageStop(f"{name} STOP: m's stage ended ({res['status']}) but p's report was not written ({e}); "
                        f"re-derive it with the driver's {gate}-report") from None
    return {"status": res["status"], "result": res, "report": rep, "paths": pp, "written": how}


# --- THE CAMPAIGN (the campaign wiring) -------------------------------------------------------------------------------
def campaign_arms(unit: str) -> list[str]:
    """The unit's two arms, contrast first (m:192's table order; keys.templates)."""
    return list(m_keys.templates(unit))


def campaign_launch_counts(unit: str) -> dict[str, int]:
    """The unit's launch counts per arm (m:192: "a projection, not a bound"), keyed by its arms, contrast first."""
    return dict(zip(campaign_arms(unit), CAMPAIGN_LAUNCH_COUNTS[unit]))


def campaign_floors(unit: str) -> dict[str, int]:
    """The unit's floors per arm: the package's schedule.FLOORS for the OLMo arms (m:182-183; p:84 "floors 80/32"),
    as m's driver reads Q-F0's (campaign_floors): one source, the package the lock's package_sha256 pins."""
    a0, a0s = campaign_arms(unit)
    return {a0: int(m_schedule.FLOORS["A0-OLMo"]), a0s: int(m_schedule.FLOORS["A0s-OLMo"])}


def campaign_hour_cap(unit: str) -> int | float | None:
    """The PI's cap share for the unit's campaign, in hours (m:249): a positive finite int or float (m's
    hour_cap_exceeded also takes a text or a Fraction; p's cap is a number, and a bool is not one here); None while it
    is not set or not such a number."""
    v = CAMPAIGN_HOUR_CAP.get(unit)
    if type(v) not in (int, float) or not math.isfinite(v) or v <= 0:
        return None
    return v


def campaign_lock_lines(unit: str) -> tuple[str, ...]:
    """The campaign's line forms the unit's LOCK-p v1.0 carries as whole lines (m's CAMPAIGN_LOCK_LINES' form, the
    unit's arms named): the launch counts per arm and, once set, the hour cap."""
    lc = campaign_launch_counts(unit)
    lines = ["launch counts = " + ", ".join(f"{a} {n}" for a, n in lc.items())]
    cap = campaign_hour_cap(unit)
    if cap is not None:
        lines.append(f"hour cap = {cap} h")
    return tuple(lines)


def campaign_lock_problems(unit: str, text: str) -> list[str]:
    """Each of ``campaign_lock_lines`` as a whole line of the lock's committed text (p's whole-line form, as the qual
    stage requires its acceptance line); the cap's absence is the precheck's own refusal."""
    return [f"the campaign's line {ln!r} is not a whole line of the lock (the campaign wiring's PIN)"
            for ln in campaign_lock_lines(unit) if not re.search(rf"^{re.escape(ln)}$", text, re.M)]


def gpwr_problems(unit: str) -> tuple[list[str], str | None]:
    """G-PWR (p)'s record of the unit's launch counts: committed, its schema, and the unit's L per arm (m's arm roles
    A0, A0s) equal to ``CAMPAIGN_LAUNCH_COUNTS``; (problems, the record's sha256)."""
    cp, data = m_stages._committed(GPWR_REL)
    if cp or data is None:
        return [f"{GPWR_REL}: {x}" for x in (cp or ["unreadable"])], None
    try:
        rec = json.loads(data.decode("utf-8"))
        u = rec["units"][unit]
        lc = (u["launch"]["L"]["A0"], u["launch"]["L"]["A0s"])
        schema = rec.get("schema")
    except (ValueError, UnicodeDecodeError, KeyError, TypeError) as e:
        return [f"{GPWR_REL}: not G-PWR (p)'s record of {unit} ({type(e).__name__})"], None
    probs = [] if schema == GPWR_SCHEMA else [f"{GPWR_REL}: schema {schema!r}, not {GPWR_SCHEMA!r}"]
    if lc != tuple(CAMPAIGN_LAUNCH_COUNTS[unit]):
        probs.append(f"{GPWR_REL}: {unit}'s launch counts {lc}, not this build's {CAMPAIGN_LAUNCH_COUNTS[unit]}")
    return probs, _sha(data)


def ruling_texts(adjudication_file: str | None, pi_stop_file: str | None) -> tuple[dict, list[str]]:
    """({"adjudication": text or None, "pi_stop": text or None}, problems): the campaign's two ruling files under m's
    rule (scripts/m_sessions.py's ruling_texts, read as text, never imported): a regular file (a FIFO or a device is
    refused before it is opened), UTF-8 with a leading byte-order mark dropped, not blank (a visible character); its
    text passed as read (m's stage strips it). The texts stand in no command line, launch line or raw, and are never
    printed."""
    import unicodedata
    texts: dict = {"adjudication": None, "pi_stop": None}
    probs: list[str] = []
    for key, flag, given in (("adjudication", "--adjudication-file", adjudication_file),
                             ("pi_stop", "--pi-stop-file", pi_stop_file)):
        if given is None:
            continue
        try:
            if not Path(given).is_file():
                probs.append(f"{flag} {given}: not a regular file")
                continue
            txt = Path(given).read_bytes().decode("utf-8-sig")
        except (OSError, ValueError) as e:
            probs.append(f"{flag} {given}: unreadable as UTF-8 text ({type(e).__name__})")
            continue
        if not any(not c.isspace() and unicodedata.category(c)[0] not in "CZ" for c in txt):
            probs.append(f"{flag} {given}: blank (a ruling is a text with a visible character)")
            continue
        texts[key] = txt
    return texts, probs


def campaign_state(cpath: Path, unit: str) -> tuple[str, dict]:
    """(state, summary) of the campaign checkpoint at ``cpath``: m's driver's _campaign_state (read as text, never
    imported), the arms the unit's own (an OLMo pause names A0-OLMo-{ckpt} or A0s-OLMo-{ckpt}, not Q-F0's A0 or A0s).
    state: "absent", "unreadable", "pending" (an end pending), "ended" (resume.ended_status) or "open"; the summary
    free of any recorded text: launched, the recorded PI stop's sha256, the last pause's kind, launch count, arm,
    whether adjudicated and its ruling's sha16, and every pause's ruling sha16 in order; {} when unreadable."""
    p = Path(cpath)
    arms = (None, *campaign_arms(unit))
    try:
        if not (p.exists() or p.is_symlink()):
            return "absent", {"launched": False, "pi_stop_sha256": None, "last": None, "ruling_sha16s": []}
        if not p.is_file():
            return "unreadable", {}
    except OSError:
        return "unreadable", {}
    try:
        ck = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError, RecursionError):
        return "unreadable", {}
    camp = ck.get("campaign") if isinstance(ck, dict) else None
    camp = {} if camp is None else camp
    pauses = camp.get("pauses", []) if isinstance(camp, dict) else None
    if (not isinstance(ck, dict) or type(ck.get("sessions", [])) is not list or not isinstance(camp, dict)
            or type(pauses) is not list
            or not all(isinstance(x, dict) and {"kind", "at_launches", "adjudication"} <= set(x)
                       and x["kind"] in ("look", "end_look", "schedule_exhausted") and type(x["at_launches"]) is int
                       and (x["adjudication"] is None or type(x["adjudication"]) is str)
                       and x.get("arm") in arms for x in pauses)
            or not (camp.get("pi_stop") is None or type(camp.get("pi_stop")) is str)):
        return "unreadable", {}
    last = pauses[-1] if pauses else None
    try:
        for x in pauses:
            if x["adjudication"] is not None:
                x["adjudication"].encode("utf-8")
        summary = {"launched": bool(ck.get("sessions")),
                   "pi_stop_sha256": (None if camp.get("pi_stop") is None
                                      else _sha(camp["pi_stop"].encode("utf-8"))),
                   "last": None if last is None else {
                       "kind": last["kind"], "at_launches": last["at_launches"], "arm": last.get("arm"),
                       "adjudicated": last["adjudication"] is not None,
                       "adjudication_sha16": (m_stages._sha16_text(last["adjudication"])
                                              if type(last["adjudication"]) is str else None)},
                   "ruling_sha16s": [m_stages._sha16_text(x["adjudication"]) for x in pauses
                                     if type(x["adjudication"]) is str]}
    except UnicodeEncodeError:
        return "unreadable", {}
    if m_resume.pending_end(ck) is not None:
        return "pending", summary
    if m_resume.ended_status(ck) is not None:
        return "ended", summary
    return "open", summary


def campaign_ruling_problems(cpath: Path, unit: str, adjudication: str | None, pi_stop: str | None) -> list[str]:
    """The refusals of a ruling that does not fit the campaign's state, made before the load: m's driver's
    campaign_ruling_problems (read as text, never imported) over ``campaign_state``, in its order and its words --
    CHECKPOINT MISMATCH (a PI stop other than the one recorded); beside an end pending, RULING BESIDE AN END PENDING
    for a ruling the stage would not apply there; PI STOP REFUSED (no session launched); SCHEDULE EXHAUSTED (an
    adjudication alone on an exhausted schedule's open pause); RULING REUSED (an earlier pause's ruling offered again);
    NO PAUSE TO ADJUDICATE. An unreadable or ended checkpoint is not refused here (the run's own refusals take it)."""
    if adjudication is None and pi_stop is None:
        return []
    state, sm = campaign_state(cpath, unit)
    if state in ("unreadable", "ended"):
        return []
    rec_pi = sm["pi_stop_sha256"]
    if pi_stop is not None and rec_pi is not None and _sha(pi_stop.strip().encode("utf-8")) != rec_pi:
        return [f"CHECKPOINT MISMATCH: {cpath} records the PI's stop; this run offers a different text -- refusing "
                f"(the stage makes this refusal after the load)"]
    if state == "pending":
        a16 = m_stages._sha16_text(adjudication.strip()) if adjudication is not None else None
        adj_w = "the seat's adjudication" + (
            f", which the checkpoint already records as a pause's ruling (sha16 {a16}) and which needs nothing"
            if a16 is not None and a16 in sm.get("ruling_sha16s", []) else "")
        skip = [(w, f) for w, f, v in ((adj_w, "--adjudication-file", adjudication),
                                       ("the PI's stop, which the checkpoint does not record", "--pi-stop-file",
                                        pi_stop if rec_pi is None else None)) if v is not None]
        if skip:
            return [f"RULING BESIDE AN END PENDING at {cpath}: the checkpoint carries an end pending, which the stage "
                    f"re-finishes before it applies any ruling, and it would not apply "
                    f"{' and '.join(w for w, _f in skip)} (NOT APPLIED, after the load) -- refused before the load: "
                    f"re-run without {' and '.join(f for _w, f in skip)}, with --resume, which re-finishes the end; "
                    f"then offer a ruling for the pause the re-finish shows, if it leaves the campaign open"]
        return []
    pi = pi_stop is not None or rec_pi is not None
    if pi and not sm["launched"]:
        return [f"PI STOP REFUSED at {cpath}: no session has launched -- a unit that never launches is NOT-RUN by its "
                f"Clock (m:192), not PI-stopped"]
    last = sm["last"]
    open_pause = last is not None and not last["adjudicated"]
    if open_pause and last["kind"] == "schedule_exhausted" and not pi and adjudication is not None:
        return [f"SCHEDULE EXHAUSTED at {cpath}: {last['arm']} has no committed cell left below its floor; only the "
                f"PI's stop (pi_stop) ends this campaign (m:192, m:247)"]
    if adjudication is not None and open_pause:
        a16 = m_stages._sha16_text(adjudication.strip())
        if a16 in sm.get("ruling_sha16s", []):
            return [f"RULING REUSED at {cpath}: the seat's adjudication offered (sha16 {a16}) is the text the "
                    f"checkpoint records as an earlier pause's ruling; an adjudication is offered only for the pause "
                    f"it rules on (this campaign's open pause, at {last['at_launches']} launches, {last['kind']}) -- "
                    f"refused before the load"]
    if adjudication is not None and not open_pause:
        how = ("drop --adjudication-file: resume with --resume and the PI's stop alone" if pi_stop is not None
               else "resume with --resume alone")
        tail = ("" if last is None else
                f" -- its last pause ({last['kind']}, at {last['at_launches']} launches) already carries a ruling "
                f"(sha16 {last['adjudication_sha16']}); {how}")
        return [f"NO PAUSE TO ADJUDICATE at {cpath}: the campaign is not paused{tail}"]
    return []


def _run_recorded(unit: str, stage: str, adapter_factory: Callable[[], Any], *, stub: bool, resume: bool, out: Path,
                  pp: Mapping[str, Path], pre: Mapping[str, Any], echo: Callable[[str], None], events: list[Mapping],
                  call_m: Callable[[Any], Any]) -> Any:
    """The recorded run, shared by the gates and the campaign (the module docstring's THE CALL LOG and THE STOP):
    the gate line, the STOP's reservation, the substitutions entered, the run line, the proxied adapter and the
    backend identifier against the lock's after the load, m's stage (``call_m`` on the proxy), and, in the
    ``finally``, the end line and any STOP's marker; m's result returned. Extracted unchanged from the gate stage
    at the campaign wiring (its m call made a parameter).
    """
    name = label(unit, stage)
    if pre["gate_line"]:
        echo(pre["gate_line"]["line"])
    k = 1 + sum(1 for e in events if e.get("event") == "run")
    reserve = reserve_path(pp["p_stopped"], k)
    stale = sorted(x.name for x in pp["p_stopped"].parent.glob(pp["p_stopped"].name + ".reserve-*") if x != reserve)
    if stale:                                       # round 5's NOTE 3: named for the seat, never removed
        _safe_echo(echo, f"P-STALE STOP RESERVATION(S) {stale}: runs that ended without releasing their reservation "
                         f"(killed, or a STOP whose record failed); kept beside the record for the seat's read")
    res, err, px, log, stop, reserved, inner_done = None, None, None, None, False, False, False
    try:
        with stage_substitutions() as entered:
            # The STOP's record is reserved before the run line (round 4's m-1 and NOTE 1): a STOP renames it into
            # place, which needs no new space and leaves no half-written marker; a failure to reserve refuses the run
            # with nothing recorded. The log is opened once every entry is in force, so a STOP while they are entered
            # (nothing loaded) leaves no record behind it (round 3's m-3).
            try:
                guard.write_once_bytes(reserve, _stopped_doc(unit, stage, k, None), what="p's STOP reservation")
            except (OSError, SystemExit) as e:
                raise StageRefusal(f"{name} REFUSED: the STOP's record cannot be reserved ({type(e).__name__}: "
                                   f"{e}) -- nothing recorded or loaded") from None
            reserved = True
            log = CallLog(pp["p_calls"], out)
            log.write({"event": "run", "schema": CALLS_SCHEMA, "run": k, "resume": resume, "stage": name,
                       "unit": unit, "register_entered": entered, "p_package_sha256": guard.package_sha256(),
                       "proposal_p_sha256": identity.PROPOSAL_P_SHA256, "stale_reservations": stale})
            try:
                px = StoredTextProxy(adapter_factory(), on_call=lambda r: log.write({"event": "call", "run": k, **r}))
                if not stub:
                    bid = m_resume.backend_identifier(px.provenance())
                    if bid != pre["backend_of_record"]:
                        raise StageStop(f"{name} STOP: the adapter's backend identifier {bid} is not the lock's "
                                        f"{pre['backend_of_record']} (m:302; a superseding BACKEND entry is the seat's "
                                        f"to route) -- nothing generated")
                res = call_m(px)
            except BaseException as e:
                err = e
                raise
            finally:
                # Round 5's m-1: a Ctrl-C from here until the end line has been attempted is deferred (a handler that
                # records it, installed first), so neither record is skipped; it is raised once both are attempted.
                deferred: list = []
                try:
                    prev = signal.signal(signal.SIGINT, lambda signum, frame: deferred.append(signum))
                except (ValueError, OSError):       # not the main thread: no deferral
                    prev = None
                late = None
                try:
                    stop = stop_in(err) or (px is not None and any("stop" in c for c in px.calls))
                    marker = None
                    if stop:                        # first: the marker, by rename (atomic; no new space)
                        try:
                            if pp["p_stopped"].exists() or pp["p_stopped"].is_symlink():
                                marker = "present"
                            else:
                                os.rename(reserve, pp["p_stopped"])
                                marker = "renamed into place"
                                m_resume._fsync_dir(pp["p_stopped"].parent)
                        except BaseException as me:
                            in_place = pp["p_stopped"].exists()   # round 5's NOTE 2: a rename that took is in place
                            marker = (f"renamed into place (then {type(me).__name__})" if in_place
                                      else f"NOT IN PLACE ({type(me).__name__})")
                            late = me if not isinstance(me, Exception) else None
                        if pp["p_stopped"].exists() and not pp["p_stopped"].is_symlink():
                            try:
                                _fill_cause(pp["p_stopped"], unit, stage, k, err)
                            except BaseException:   # noqa: BLE001 -- best-effort: the marker stands without it
                                pass
                    end_state = register.single_thread_state()
                    stop_detail = None
                    if px is not None and isinstance(err, ProxyStop) and err.log_error:
                        stop_detail = {"log_error": err.log_error, "returned_text": err.returned_text,
                                       "stored_text": err.stored_text}
                    end_written = False
                    try:
                        log.write({"event": "end", "run": k, "outcome": "exception" if err is not None else "returned",
                                   "status": res.get("status") if isinstance(res, Mapping) else None,
                                   "exception": None if err is None else {"type": type(err).__name__,
                                                                          "message": str(err)[:4000], "stop": stop},
                                   "stop_marker": marker, "stop_line_failed": stop_detail,
                                   "n_generate": px.n_generate if px is not None else 0,
                                   "n_cuts": len(px.cuts) if px is not None else 0, "term_d_at_stage_end": end_state})
                        end_written = True
                    except BaseException as le:
                        if late is None and not isinstance(le, Exception):
                            late = le
                        end_err = type(le).__name__
                    in_place = bool(marker) and marker.startswith(("renamed into place", "present"))
                    if stop and not in_place and not end_written:
                        line = (f"P-STOP NOT RECORDED: the marker {marker} and the call log's end line not written "
                                f"({end_err}) -- THIS STOP IS RECORDED NOWHERE BUT HERE; nothing may resume without "
                                f"the seat")
                        _safe_echo(echo, line)
                        try:
                            print(line, file=sys.stderr, flush=True)
                        except BaseException:       # noqa: BLE001
                            pass
                    elif stop and not in_place:
                        _safe_echo(echo, f"P-STOP MARKER {marker}: the STOP rests on the call log's end line alone")
                    elif not end_written:
                        _safe_echo(echo, f"P-CALL LOG END NOT WRITTEN ({end_err})"
                                   + ("; the STOP is held by its marker" if stop else "; the run's call lines stand"))
                    inner_done = True
                finally:
                    if prev is not None:
                        try:
                            signal.signal(signal.SIGINT, prev)
                        except (ValueError, OSError):
                            pass
                if late is not None:
                    raise late
                if deferred:
                    raise KeyboardInterrupt("deferred while the STOP's record was written")
    finally:
        if log is not None:
            log.close()
        if reserved and inner_done and not stop:    # this run's reservation, released once its end is recorded
            try:
                reserve.unlink()
            except OSError:
                pass
    return res


def run_campaign(unit: str, adapter_factory: Callable[[], Any], *, stub: bool = False, resume: bool = False,
                 adjudication: str | None = None, pi_stop: str | None = None, out_root=None,
                 pre: Mapping[str, Any] | None = None,
                 echo: Callable[[str], None] = lambda s: print(s, flush=True)) -> dict:
    """The PROPOSAL-p campaign on one checkpoint (THE CAMPAIGN): m's ``stages.run_campaign`` for p's unit under the
    substitutions, its values this build's (``campaign_launch_counts``, ``campaign_floors``, ``campaign_hour_cap``),
    its prior the unit's qualification checkpoint, the seat's adjudication of a pending pause and the PI's stop
    passed as texts; ``pre``: the driver's own precheck of this run."""
    gate = "campaign"
    pre = precheck(unit, stub=stub, resume=resume, gate=gate) if pre is None else pre
    if pre.get("unit") != unit or pre.get("gate") != gate or pre.get("stub") is not stub:
        raise StageRefusal(f"{label(unit, gate)} REFUSED: the precheck given is {pre.get('unit')!r}'s at "
                           f"{pre.get('gate')!r} with stub {pre.get('stub')!r}; this run is {unit!r} at {gate!r} with "
                           f"stub {stub!r}")
    if stub:
        out = guard.refuse_test_out(out_root)
    elif out_root is not None:
        raise StageRefusal(f"{label(unit, gate)} REFUSED: a non-stub run writes data/p only (ledger 27)")
    else:
        out = DEFAULT_OUT_P
    pp = out_paths(unit, out, gate=gate)
    with stage_lock(pp["p_lock"], out, what=label(unit, gate)):
        return _run_campaign_locked(unit, adapter_factory, stub=stub, resume=resume, adjudication=adjudication,
                                    pi_stop=pi_stop, out=out, pp=pp, pre=pre, echo=echo)


def _run_campaign_locked(unit, adapter_factory, *, stub, resume, adjudication, pi_stop, out, pp, pre, echo) -> dict:
    """THE CAMPAIGN's run under its stage lock. PIN (Code, declared at the campaign wiring): the gate stage's refusals
    before the load, their wording the campaign's; then the campaign's own -- m's checkpoint read as a campaign
    (``campaign_state``: an unreadable one refused, never read as empty; an ended one refused, its report re-derived
    by the driver's campaign-report, never by a re-run), the rulings against its state (``campaign_ruling_problems``),
    the cap set, the committed schedules, the qualification as the prior -- all before the load; then the recorded
    run (``_run_recorded``). A PAUSE is not a STOP: the run's end line records it, nothing is marked, and a later run
    resumes it with --resume and the seat's adjudication (or the PI's stop), or, with neither, is shown its pause (m's
    R6) and launches nothing. p's report is written once m's checkpoint records the campaign's end (terminal or a
    STOP of m's), never at a pause."""
    gate = "campaign"
    name = label(unit, gate)
    if pp["p_report"].exists():
        raise StageRefusal(f"{name} REFUSED: p's report exists ({pp['p_report'].name}); the campaign has ended and "
                           f"been reported")
    if pp["p_stopped"].exists() or pp["p_stopped"].is_symlink():
        raise StageRefusal(f"{name} REFUSED: the campaign is STOPPED ({pp['p_stopped'].name}); the seat adjudicates "
                           f"before anything resumes (the seat's Q5; a resume never lifts a STOP) -- nothing loaded")
    if pp["p_calls"].exists() and not resume:
        raise StageRefusal(f"{name} REFUSED: the call log exists ({pp['p_calls'].name}); a later run is a --resume, "
                           f"which appends to it")
    if pp["m_ckpt"].exists() and not resume:
        raise StageRefusal(f"{name} REFUSED: m's checkpoint exists ({pp['m_ckpt'].name}); pass --resume to "
                           f"continue it -- nothing loaded")
    if resume and pp["m_ckpt"].exists() and not pp["p_calls"].exists():
        raise StageRefusal(f"{name} REFUSED: m's checkpoint exists but p's call log does not -- the earlier runs' "
                           f"record is lost; the seat adjudicates (ledger 27) -- nothing loaded")
    events, lp = read_calls(pp["p_calls"])
    unreadable = [x for x in lp if ": unreadable (" in x]
    if unreadable:
        raise StageRefusal(f"{name} REFUSED: the call log is unreadable ({unreadable[0]}); a run never reads an "
                           f"unreadable record as an empty one -- the seat adjudicates; nothing loaded")
    stops = stopped_runs(events)
    if stops:
        raise StageRefusal(f"{name} REFUSED: run(s) {stops} of this campaign ended in a STOP; the seat adjudicates "
                           f"before anything resumes (the seat's Q5; a resume never lifts a STOP) -- nothing loaded")
    if pp["m_ckpt"].exists() and not any(e.get("event") == "run" for e in events):
        raise StageRefusal(f"{name} REFUSED: m's checkpoint exists but the call log holds no run line -- the record "
                           f"is damaged, never read as an empty one; the seat adjudicates -- nothing loaded")
    cons = log_consistency_problems(unit, events, gate=gate)
    if cons:
        raise StageRefusal(f"{name} REFUSED: the call log is not this campaign's: {cons[:3]} -- nothing loaded")
    state, _sm = campaign_state(pp["m_ckpt"], unit)
    if state == "unreadable":
        raise StageRefusal(f"{name} REFUSED: m's checkpoint {pp['m_ckpt'].name} is unreadable as a campaign's -- "
                           f"never read as an empty one; the seat adjudicates -- nothing loaded")
    if state == "ended":
        raise StageRefusal(f"{name} REFUSED: m's checkpoint records the campaign's end; p's report is re-derived "
                           f"from it with the driver's campaign-report, never by a re-run")
    rp = campaign_ruling_problems(pp["m_ckpt"], unit, adjudication, pi_stop)
    if rp:
        raise StageRefusal(f"{name} REFUSED: {rp[0]}")
    cap = campaign_hour_cap(unit)
    if cap is None:
        raise StageRefusal(f"{name} REFUSED: the hour cap is not set (the PI's cap share, a LOCK-p v1.0 value)")
    sp = p_schedule.verify_schedule_dir(out / "schedules")
    if sp:
        raise StageRefusal(f"{name} REFUSED: the schedules at {_rel_to(out / 'schedules', REPO)} are not clean "
                           f"(entry (7)'s check, before the load): {sp[:3]}")
    prior_ckpt = out_paths(unit, out, gate="qual")["m_ckpt"]
    pr = prior_problems(unit, prior_ckpt, stub=stub, proposal_sha256=pre["identity_extra"]["proposal_sha256"],
                        stage="campaign")
    if pr:
        raise StageRefusal(f"{name} REFUSED: the prior stage, the qualification (before the load): {pr} -- nothing "
                           f"recorded or loaded")
    offered = [f"{who} (sha16 {m_stages._sha16_text(text.strip())})"
               for who, text in (("the seat's adjudication", adjudication), ("the PI's stop", pi_stop))
               if text is not None]
    if offered:                                     # pick-free: each text's sha16, never the text; after every
        last = _sm.get("last") if isinstance(_sm, Mapping) else None   # refusal, just before the load (m's place)
        on = ("; the campaign carries an end pending, which the stage re-finishes first" if state == "pending"
              else f"; the campaign's last pause: {last['kind']} at {last['at_launches']} launches, "
                   f"{'adjudicated' if last['adjudicated'] else 'open'}" if last else "; no pause recorded")
        echo(f"RULING {name}: {' and '.join(offered)}{on}")

    def call_m(px):
        res_ = m_stages.run_campaign(px, unit=unit, floors=campaign_floors(unit),
                                     launch_counts=campaign_launch_counts(unit), hour_cap=cap, prior_ckpt=prior_ckpt,
                                     resume=resume, identity_extra=pre["identity_extra"], substrate="olmo",
                                     out_root=out, adjudication=adjudication, pi_stop=pi_stop)
        st_, _x = campaign_state(pp["m_ckpt"], unit)
        if st_ not in ("open", "ended"):            # never a silent end: inside the recorded run, so THE STOP's
            raise StageStop(f"{name} STOP: m's campaign returned "     # machinery records it (rounds 1-2's NOTE-1/A)
                            f"{res_.get('status') if isinstance(res_, Mapping) else res_!r} but its checkpoint reads "
                            f"{st_!r} (neither open nor ended); the seat adjudicates")
        return res_
    res = _run_recorded(unit, gate, adapter_factory, stub=stub, resume=resume, out=out, pp=pp, pre=pre, echo=echo,
                        events=events, call_m=call_m)
    state, _sm = campaign_state(pp["m_ckpt"], unit)
    if state == "open":                             # a pause (or a shown pause): no report, nothing marked
        return {"status": res["status"], "result": res, "report": None, "paths": pp, "written": None}
    try:
        rep, how = write_report(unit, out, gate=gate)
    except SystemExit as e:
        raise StageStop(f"{name} STOP: m's campaign ended ({res['status']}) but p's report was not written ({e}); "
                        f"re-derive it with the driver's campaign-report") from None
    return {"status": res["status"], "result": res, "report": rep, "paths": pp, "written": how}


def summary_lines(res: Mapping[str, Any]) -> list[str]:
    """The driver's closing lines: the status, the outputs, the counters on the seat's read domain (sham sessions,
    every round; the contrast forced rounds' control characters), the trigger, the sham proxy, term (d) at the end, the
    register entries entered."""
    rep = res["report"]
    c = rep["counters"]
    sham = "; ".join(f"{k} {v['n']} {v['keys']}" for k, v in c["sham"].items())
    cc = c["contrast_forced_control_chars"]
    sp = rep["proxy"]["sham"]
    term = f" (the terminal {rep['campaign_terminal']} beside it)" if rep.get("campaign_terminal") else ""
    return [f"P-REPORT {rep['stage']}: {rep['status']}{term}; checkpoint {rep['checkpoint']['path']} (sha256 "
            f"{rep['checkpoint']['sha256']}); p's report {_rel_to(res['paths']['p_report'], REPO)} "
            f"({res['written']}), call log {rep['call_log']['path']} ({rep['call_log']['n_runs']} run(s), withheld)",
            f"P-REPORT hair trigger {c['hair_trigger']['name']} over {c['hair_trigger']['domain']}: "
            f"{c['hair_trigger']['n']}",
            f"P-REPORT sham counters ({c['n_sham_rounds']} rounds; decide nothing): {sham}",
            f"P-REPORT contrast forced rounds' control characters ({cc['n_forced_rounds']} rounds): {cc['n']} "
            f"{cc['keys']}",
            f"P-REPORT sham proxy: {sp['n_attributed']} of {sp['n_rounds']} rounds attributed, {sp['n_cuts']} cut(s) "
            f"{sp['cut_keys']}; attribution complete {rep['proxy']['attribution_complete']}; contrast: withheld (m:318)",
            f"P-REPORT withheld: {c['withheld']}",
            "P-REPORT term (d) at stage end, before restoration: " + json.dumps(rep["term_d_at_stage_end"],
                                                                               sort_keys=True),
            f"P-REPORT register entries entered: {rep['register_entered']}",
            "P-REPORT runs: " + "; ".join(f"{r['run']} {'resume' if r['resume'] else 'first'} {r['outcome']}"
                                          + (f" {r['exception_type']}" if r['exception_type'] else "")
                                          for r in rep["call_log"]["runs"])
            + f"; call log well formed {rep['call_log']['well_formed']}"]


def _selftest(chk) -> None:
    import dataclasses
    import io
    import shutil
    import tempfile
    import threading
    from unittest import mock
    from ..m import testing as m_testing
    from .proxy import ProxyStop

    @contextlib.contextmanager
    def olmo_stub_startup():
        # SELF-TEST ONLY, m's own seam (scripts/m_sessions.py's olmo_stub_startup): olmo_startup refuses the stub by
        # design (its six ban ids cannot match b3's nine-id sha16), so stages' reference to it takes a setup built as
        # runner_olmo's self-test builds one (testing.olmo_kit), restored in finally. Production code has no seam.
        from ..m import runner_olmo
        kit = m_testing.olmo_kit()
        setup = runner_olmo.OLMoSetup(audit=kit["audit"], ban_ids=kit["ban_ids"], ban_strings=kit["ban_strings"],
                                      term_rx=kit["term_rx"], audit_sha16=runner_olmo.olmo_audit_sha16())
        saved = m_stages.olmo_startup
        m_stages.olmo_startup = lambda adapter, ckpt: setup
        try:
            yield setup
        finally:
            m_stages.olmo_startup = saved

    @contextlib.contextmanager
    def withhold_9():
        # SELF-TEST ONLY: the register's entry (9) withheld (a status outside SUBSTITUTABLE) for the case's own
        # duration, so that an entry the stage enters is not admitted; the entry restored after.
        e = register.BY_N[9]
        register.BY_N[9] = dataclasses.replace(e, status="withheld for a self-test case")
        try:
            yield
        finally:
            register.BY_N[9] = e

    @contextlib.contextmanager
    def pod():
        saved = os.environ.get(m_resume.POD_ENV)
        os.environ[m_resume.POD_ENV] = "p-selftest-pod"
        try:
            yield
        finally:
            if saved is None:
                os.environ.pop(m_resume.POD_ENV, None)
            else:
                os.environ[m_resume.POD_ENV] = saved

    chk("stage: entry (6)'s replacement is data/p, and p's units and gate are G-TIME's (m:302: one session per arm)",
        DEFAULT_OUT_P == REPO / "data" / "p" and UNITS == ("OLMo-sft", "OLMo-dpo", "OLMo-instruct")
        and templates_counts("OLMo-dpo") == [("A0-OLMo-dpo", 1), ("A0s-OLMo-dpo", 1)])
    x = identity_extra("OLMo-sft", stub=False, lock_bytes=b"lock")
    chk("stage: identity_extra carries m's proposal pin and file (F-p8), the lock's sha256 and file, p's renders by m's "
        "convention, the uncached path and m's analyzer and package sha256s",
        x["proposal_sha256"] == gcal.M_PROPOSAL_SHA256 and x["proposal_file"] == gcal.M_PROPOSAL_REL
        and x["lock_file"] == "LOCK-p-OLMo-sft.md" and x["lock_sha256"] == _sha(b"lock")
        and x["renders_sha16"] == m_corr.renders_sha(list(corrupt.RENDERS_OF_RECORD))
        and x["locked_path"] == "uncached" and x["package_sha256"] == m_resume.package_sha256(), x)
    try:
        precheck("Q-F0", stub=True)
        bad_unit = "ran"
    except StageRefusal:
        bad_unit = "refused"
    try:
        precheck("OLMo-sft", stub=True, lexicon=Path(tempfile.gettempdir()) / "p-no-such-lexicon.txt")
        no_lex = "ran"
    except StageRefusal as e:
        no_lex = "refused" if "LEXICON STOP" in str(e) else f"other: {e}"
    chk("stage: Q-F0 and the base checkpoint are no p unit, and an absent lexicon is refused, before anything loads "
        "(MAJOR 3's precheck)", bad_unit == "refused" and no_lex == "refused", (bad_unit, no_lex))
    gl, _glp = m_stages.gate_line(label("OLMo-sft"), REPO / gcal.PROPOSAL_P_REL)
    ln_ok = (lock_names("x\n  LICENCE a b\n", "LICENCE a b") and lock_names("- v: `1/8`", "1/8")
             and not lock_names("- v: `1/80`", "1/8") and not lock_names("covariate: 1/80", "covariate: 1/8"))
    chk("stage: the gate line is m's gate-stage form for G-TIME-OLMo-{ckpt} (p), naming PROPOSAL-p (N-5); a lock names "
        "a value as a whole line or between backticks, never as a bare substring (N-4)",
        gl.startswith("GATE G-TIME-OLMo-sft (p): proposal PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md ")
        and "G-CAL" not in gl and ln_ok, (gl, ln_ok))
    bp = (lock_backend("a\nBACKEND OF RECORD 641ee466f4553b6a\nb"), lock_backend("none"),
          lock_backend("BACKEND OF RECORD 641ee466f4553b6a\nBACKEND OF RECORD 0000000000000000"))
    chk("stage: the backend identifier of record is the lock's one BACKEND line (none, or two, is a refusal)",
        bp[0] == ([], "641ee466f4553b6a") and bp[1][1] is None and bp[2][1] is None and bool(bp[1][0])
        and bool(bp[2][0]), bp)
    m_scaffold._of_record.cache_clear()
    m_scaffold.pool_and_renders()                   # m's renders cached before entry (1): the order rule's case
    try:
        with stage_substitutions():
            order = "entered"
    except StageStop as e:
        order = "stop" if "before entry (1)" in str(e) else "other"
    m_scaffold._of_record.cache_clear()
    chk("stage: m's renders cached before the substitutions are entered is a STOP (the seat's Q4), every entry "
        "restored", order == "stop" and m_corr._eligible_m is not corrupt.eligible_p
        and m_stages.DEFAULT_OUT == REPO / "data" / "m", order)
    unit = "OLMo-sft"
    contrast, sham = m_keys.templates(unit)
    m_attrs = (m_corr._eligible_m, m_keys.arm_key, m_stages.DEFAULT_OUT, m_schedule.verify_schedule_dir,
               m_resume.IDENTITY_KEYS_OLMO, m_resume.Identity)

    def factory_with(rule=None, thread=None, calls=None, gate="time"):
        def factory():
            if calls is not None:
                calls.append("factory")
            if thread is not None:
                thread.start()
            a = m_testing.OLMoScriptedAdapter("p-stage-selftest")
            cells = {}
            for t, n_t in templates_counts(unit, gate):
                for j, cell in enumerate(m_schedule.gate_schedule(unit, gate, t, m_schedule.roster_for(unit), n_t)):
                    cells[(t, j)] = cell
            a.load(m_stages._script_policy(unit, gate, cells, rule), None)
            return a
        return factory

    tdir = Path(tempfile.mkdtemp(prefix="p_stage_"))

    def root(name: str) -> Path:
        d = tdir / name / "p"
        p_schedule.write_schedule_files(d / "schedules")
        return d

    def stub_run(r: Path, fac, *, resume: bool = False, pre=None, gate: str = "time"):
        m_scaffold._of_record.cache_clear()
        buf = io.StringIO()
        try:
            with olmo_stub_startup(), pod(), contextlib.redirect_stdout(buf):
                return (run_gate(unit, gate, fac, stub=True, out_root=r, resume=resume, pre=pre), None,
                        buf.getvalue())
        except (SystemExit, Exception) as e:
            return None, e, buf.getvalue()

    try:
        r0 = root("pass")
        res, err, _ = stub_run(r0, factory_with())
        ok, detail = err is None and res["status"] == "PASS", (err, res and res["status"])
        if ok:
            ck = json.loads(Path(res["result"]["checkpoint"]).read_text(encoding="utf-8"))
            idn = ck["identity"]
            rep = json.loads(res["paths"]["p_report"].read_text(encoding="utf-8"))
            arms = [v["arm"] for v in idn["key_templates"].values()]
            ok = ({k: idn[k] for k in identity.P_FIELDS} == identity.run_values()
                  and idn["renders_sha16"] == renders_sha16_m() and idn["proposal_sha256"] == gcal.M_PROPOSAL_SHA256
                  and all(a.startswith("p-olmo-time|") for a in arms) and len(ck["sessions"]) == 2
                  and all(s["verified"] for s in ck["sessions"])
                  and rep["counters"]["hair_trigger"]["n"] == 0 and rep["proxy"]["sham"]["n_cuts"] == 0
                  and rep["proxy"]["attribution_complete"] is True
                  and rep["proxy"]["sham"]["n_attributed"] == rep["proxy"]["sham"]["n_rounds"] > 0
                  and rep["identity_p"] == identity.run_values() and rep["register_entered"] == list(ENTERED)
                  and rep["call_log"]["n_runs"] == 1 and rep["m_outputs"]["report"]["sha256"] is not None
                  and rep["m_outputs"]["reads"]["sha256"] is not None and rep["proposal_p_sha256"] == gcal.PROPOSAL_P_SHA256)
            detail = (idn.get("proposal"), arms, rep["counters"]["hair_trigger"], rep["register_entered"])
        restored = (m_corr._eligible_m, m_keys.arm_key, m_stages.DEFAULT_OUT, m_schedule.verify_schedule_dir,
                    m_resume.IDENTITY_KEYS_OLMO, m_resume.Identity) == m_attrs
        chk("stage: a full G-TIME-OLMo (p) on m's scripted OLMo double in a scratch root -- m's run_gate_stage under "
            "entries (1), (2), (6)-(9): PASS, two verified sessions, the checkpoint identity carrying p's four fields, "
            "p's renders (m's convention), m's proposal pin and p's arm keys; p's report on the read domain (every sham "
            "round attributed, the entries entered recorded as (1), (2), (6)-(9), m's report and reads named); every m "
            "attribute restored and the renders cache cleared after",
            ok and restored and m_scaffold._of_record.cache_info().currsize == 0
            and register.BY_N[9].status == register.BUILT_STEP6, detail)
        if ok:
            first = res["paths"]["p_report"].read_bytes()
            res["paths"]["p_report"].rename(res["paths"]["p_report"].with_name("moved.json"))
            _, how2 = write_report(unit, r0)
            again = res["paths"]["p_report"].read_bytes() == first
            r2, e2, _ = stub_run(r0, factory_with(), resume=True)
            chk("stage: p's report is re-derived byte for byte from the checkpoint and the call log (the driver's "
                "time-report, MAJOR 3), and a run on an ended stage is refused before it writes any record (the "
                "local lock file aside)",
                again and how2 == "written" and r2 is None and isinstance(e2, StageRefusal) and "p's report" in str(e2),
                (again, how2, e2))
        stop_evt = threading.Event()
        th = threading.Thread(target=stop_evt.wait, daemon=True, name="p-selftest-loader-thread")
        try:
            rt, et, _ = stub_run(root("thread"), factory_with(thread=th))
        finally:
            stop_evt.set()
            th.join(10)
        td_ = rt["report"]["term_d_at_stage_end"] if rt else None
        chk("stage: a library thread alive after the load (the factory leaves one) does not STOP the stage -- nothing "
            "inside re-enters the register (MAJOR 1; the seat's Q4) -- and term (d)'s end state records it",
            et is None and rt["status"] == "PASS" and td_ and td_[0]["single_threaded"] is False
            and td_[0]["active_count"] == 2, (et, td_))
        reps, lines = {}, {}
        for tag, n_free in (("none", None), ("ci0", 5), ("ci1", 6)):
            rule = None if n_free is None else (lambda t, s, n, call, _n=n_free: "{Pc}." if t == contrast and n == _n
                                                else None)
            rr, ee, _ = stub_run(root(f"excl-{tag}"), factory_with(rule=rule))
            if ee is not None:
                reps[tag] = f"{type(ee).__name__}: {ee}"
                continue
            ck_ = json.loads(Path(rr["result"]["checkpoint"]).read_text(encoding="utf-8"))
            con = [s for s in ck_["sessions"] if s["contrast"]][0]
            norm = json.loads(json.dumps(rr["report"]))
            for k in ("checkpoint", "call_log"):
                norm[k]["sha256"] = "*"
            for k in ("report", "reads"):
                norm["m_outputs"][k]["sha256"] = "*"
            reps[tag] = (norm, sum(1 for x in con["rounds"] if x["phase"] == "free"), bool(con.get("exclusion")))
            lines[tag] = [re.sub(r"[0-9a-f]{64}", "*", ln) for ln in summary_lines(rr)]
        same = all(isinstance(v, tuple) for v in reps.values()) and len({json.dumps(v[0], sort_keys=True)
                                                                         for v in reps.values()}) == 1
        chk("stage: blinding (MAJOR 2) -- with a contrast free-round exclusion planted at free round 0, at free round 1, "
            "or none, the contrast session's free rounds differ (6, 1, 2 generated) and p's report and closing lines "
            "do not, but for the outputs' sha256s",
            same and len({json.dumps(v, sort_keys=True) for v in lines.values()}) == 1
            and [reps[t][1:] for t in ("none", "ci0", "ci1")] == [(6, False), (1, True), (2, True)],
            {t: (v[1:] if isinstance(v, tuple) else v) for t, v in reps.items()})
        rs = root("proxystop")
        rule_ps = (lambda t, s, n, call: "zebra\n\nx" if t == contrast and n == 6 else None)
        rp_, ep_, out_ = stub_run(rs, factory_with(rule=rule_ps))
        ev, lp_ = read_calls(out_paths(unit, rs)["p_calls"])
        stops = [e for e in ev if e.get("event") == "call" and "stop" in e]
        endl = [e for e in ev if e.get("event") == "end"]
        try:
            build_report(unit, rs)
            rb = "built"
        except StageStop as e:
            rb = "stop" if "no persisted stage end" in str(e) else f"other: {e}"
        rerun, ere, _ = stub_run(rs, factory_with())
        fac_calls: list = []
        rres_ps, eres_ps, _ = stub_run(rs, factory_with(calls=fac_calls), resume=True)
        chk("stage: a STOP inside a session (a ProxyStop at a contrast free round) leaves the call log written -- the "
            "run line, every call, the STOP's detail with its returned text, the end line with the exception's type, "
            "its textless message and its stop mark -- and its STOP marker, and no p report; the report refuses an "
            "unended stage; a second run is refused before the load, with or without --resume: a resume never lifts a "
            "STOP (round 2's M-1; round 3's m-1)",
            rp_ is None and isinstance(ep_, ProxyStop) and "zebra" not in str(ep_) and lp_ == []
            and len(stops) == 1 and stops[0]["stop"]["returned_text"] == "zebra\n\nx"
            and len(endl) == 1 and endl[0]["outcome"] == "exception" and endl[0]["exception"]["type"] == "ProxyStop"
            and endl[0]["exception"]["stop"] is True
            and "zebra" not in endl[0]["exception"]["message"] and not out_paths(unit, rs)["p_report"].exists()
            and rb == "stop" and isinstance(ere, StageRefusal) and "STOPPED" in str(ere)
            and endl[0]["stop_marker"] == "renamed into place" and out_paths(unit, rs)["p_stopped"].is_file()
            and rres_ps is None and isinstance(eres_ps, StageRefusal) and "STOPPED" in str(eres_ps)
            and fac_calls == [], (ep_, len(stops), endl[:1], rb, ere, eres_ps, fac_calls))
        rres = root("resume")
        boom = {"armed": True}

        def rule_boom(t, s, n, call):
            if boom["armed"] and t == sham and n == 2:
                raise RuntimeError("p-selftest planted interruption")
            return None
        ra, ea, _ = stub_run(rres, factory_with(rule=rule_boom))
        boom["armed"] = False
        rb2, eb2, _ = stub_run(rres, factory_with(rule=rule_boom), resume=True)
        rep_r = rb2["report"] if rb2 else {}
        ev_r, _ = read_calls(out_paths(unit, rres)["p_calls"])
        chk("stage: an interruption in the second session, then --resume: the call log carries both runs (the first's "
            "orphan calls included), the resumed stage PASSes and p's report attributes every sham round from the "
            "whole log, n_runs 2, each run's outcome named (an interruption is no STOP)",
            ra is None and isinstance(ea, RuntimeError) and eb2 is None and rb2["status"] == "PASS"
            and rep_r["call_log"]["n_runs"] == 2 and rep_r["proxy"]["attribution_complete"] is True
            and [e["outcome"] for e in ev_r if e["event"] == "end"] == ["exception", "returned"]
            and [(r["outcome"], r["exception_type"], r["stop"]) for r in rep_r["call_log"]["runs"]]
            == [("exception", "RuntimeError", False), ("returned", None, False)],
            (ea, eb2, rep_r.get("call_log"), rep_r.get("proxy", {}).get("attribution_complete")))
        rtorn = root("torn")
        boom["armed"] = True
        stub_run(rtorn, factory_with(rule=rule_boom))
        boom["armed"] = False
        with open(out_paths(unit, rtorn)["p_calls"], "ab") as fh:
            fh.write(b'{"event": "call", "ru')             # a crash mid-write
        rt2, et2, _ = stub_run(rtorn, factory_with(rule=rule_boom), resume=True)
        rep_t = rt2["report"] if rt2 else {}
        ev_s = read_calls(out_paths(unit, rres)["p_calls"])[0]
        other = log_consistency_problems("OLMo-dpo", ev_s)
        dup = log_consistency_problems(unit, ev_s + [dict(ev_s[0])])
        chk("stage: a torn last line (a crash mid-write) is terminated before the next run appends -- the resumed run's "
            "line survives (n_runs 2), the report marks the log not well formed (one malformed line) and still "
            "attributes every sham round; another stage's log, or a run numbered twice, is not this stage's (m-1)",
            et2 is None and rt2["status"] == "PASS" and rep_t["call_log"]["n_runs"] == 2
            and rep_t["call_log"]["well_formed"] is False and rep_t["call_log"]["n_malformed_lines"] == 1
            and rep_t["proxy"]["attribution_complete"] is True and log_consistency_problems(unit, ev_s) == []
            and bool(other) and bool(dup), (et2, rep_t.get("call_log"), other[:1], dup[:1]))
        rlost = root("lost")
        boom["armed"] = True
        stub_run(rlost, factory_with(rule=rule_boom))
        boom["armed"] = False
        out_paths(unit, rlost)["p_calls"].unlink()
        lost_calls: list = []
        rl1, el1, _ = stub_run(rlost, factory_with(calls=lost_calls))
        rl2, el2, _ = stub_run(rlost, factory_with(calls=lost_calls), resume=True)
        chk("stage: m's checkpoint present, a plain run is refused before the load (m's CHECKPOINT EXISTS); with the "
            "call log lost, a --resume is refused before the load (the record is lost; the seat adjudicates) (m-2)",
            rl1 is None and isinstance(el1, StageRefusal) and "pass --resume" in str(el1)
            and rl2 is None and isinstance(el2, StageRefusal) and "record is lost" in str(el2) and lost_calls == [],
            (el1, el2, lost_calls))
        rdirty = root("dirty")
        (rdirty / "schedules" / "stray.json").write_text("{}\n", encoding="utf-8")
        calls: list = []
        rd, ed, _ = stub_run(rdirty, factory_with(calls=calls))
        pre_s = precheck(unit, stub=True)
        try:
            run_time(unit, factory_with(calls=calls), stub=False, pre=pre_s)
            n2 = "ran"
        except StageRefusal as e:
            n2 = "refused" if "stub" in str(e) else f"other: {e}"
        chk("stage: a schedules directory that is not clean is refused before the load, the factory never called "
            "(N9); a stub precheck handed to a non-stub run is refused (N2)",
            rd is None and isinstance(ed, StageRefusal) and "not clean" in str(ed) and calls == [] and n2 == "refused",
            (ed, calls, n2))
        try:
            run_time(unit, factory_with(), stub=True, out_root=REPO / "data" / "p" / "selftest")
            inside = "ran"
        except SystemExit as e:
            inside = "refused" if "inside the repository" in str(e) else f"other: {e}"
        chk("stage: a stub run with its root inside the repository (data/p included) is refused before anything loads",
            inside == "refused", inside)
        # round 3: the record's own failure modes -- an invalid byte, a failed end line, a failed STOP line, a STOP while
        # the substitutions are entered, a second process, a line separator in a logged text
        rbad = root("badbyte")
        stub_run(rbad, factory_with(rule=(lambda t, s, n, call: "zebra\n\nx" if t == contrast and n == 6 else None)))
        with open(out_paths(unit, rbad)["p_calls"], "ab") as fh:
            fh.write(b'{"event": "call", "text": "caf\xc3')     # a crash mid-write inside a two-byte character
        evb, lpb = read_calls(out_paths(unit, rbad)["p_calls"])
        bb_calls: list = []
        rbb, ebb, _ = stub_run(rbad, factory_with(calls=bb_calls), resume=True)
        rend = root("endfail")
        real_write = CallLog.write

        def failing_end(self, rec):
            if rec.get("event") == "end":
                raise OSError(28, "No space left on device (planted)")
            return real_write(self, rec)
        CallLog.write = failing_end
        try:
            r_e1, e_e1, out_e1 = stub_run(rend, factory_with(rule=(lambda t, s, n, call: "zebra\n\nx"
                                                                    if t == contrast and n == 6 else None)))
        finally:
            CallLog.write = real_write
        ee_calls: list = []
        r_e2, e_e2, _ = stub_run(rend, factory_with(calls=ee_calls), resume=True)
        rsl = root("stopline")

        def failing_stopline(self, rec):
            if rec.get("event") == "call" and "stop" in rec:
                raise OSError(28, "No space left on device (planted)")
            return real_write(self, rec)
        CallLog.write = failing_stopline
        try:
            r_s1, e_s1, _ = stub_run(rsl, factory_with(rule=(lambda t, s, n, call: "zebra\n\nx"
                                                              if t == contrast and n == 6 else None)))
        finally:
            CallLog.write = real_write
        evs, _ = read_calls(out_paths(unit, rsl)["p_calls"])
        r_s2, e_s2, _ = stub_run(rsl, factory_with(), resume=True)
        chk("stage: round 3's record failures -- an invalid byte torn into the log after a STOP is one malformed line, "
            "the STOP still read and a --resume refused before the load (the MAJOR); a STOP whose end line fails to "
            "write is held by its marker and a --resume refused; a ProxyStop whose own STOP line fails still ends the "
            "run as a ProxyStop, its end line marked stop, its marker written, a --resume refused (m-1)",
            any(x.endswith(": not JSON") for x in lpb) and stopped_runs(evb) == [1] and rbb is None
            and isinstance(ebb, StageRefusal) and bb_calls == []
            and isinstance(e_e1, ProxyStop) and out_paths(unit, rend)["p_stopped"].is_file()
            and "end line alone" not in out_e1 and r_e2 is None and isinstance(e_e2, StageRefusal)
            and "STOPPED" in str(e_e2) and ee_calls == []
            and isinstance(e_s1, ProxyStop) and e_s1.log_error is not None
            and [e["exception"]["stop"] for e in evs if e["event"] == "end"] == [True]
            and out_paths(unit, rsl)["p_stopped"].is_file() and isinstance(e_s2, StageRefusal),
            (lpb[-1:], ebb, e_e1, e_e2, e_s1, e_s2))
        rnine = root("nine")
        pre9 = precheck(unit, stub=True)
        try:
            with withhold_9():
                precheck(unit, stub=True)
            pre9_w = "passed"
        except StageRefusal as e:
            pre9_w = "refused" if "register entry (9) is not admitted" in str(e) else f"other: {e}"
        nine_calls: list = []
        r9, e9_, _ = None, None, None
        m_scaffold._of_record.cache_clear()
        try:
            with withhold_9(), olmo_stub_startup(), pod():
                run_time(unit, factory_with(calls=nine_calls), stub=True, out_root=rnine, pre=pre9)
        except SystemExit as e:
            e9_ = e
        lock_path = out_paths(unit, root("locked"))["p_lock"]
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        held_fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o644)
        fcntl.flock(held_fd, fcntl.LOCK_EX)
        try:
            lk_calls: list = []
            r_l, e_l, _ = stub_run(lock_path.parent.parent, factory_with(calls=lk_calls))
        finally:
            os.close(held_fd)
        chk("stage: a STOP while the substitutions are entered (entry (9) withheld for the case) leaves no call log "
            "(round 3's m-3), and the precheck refuses an unadmitted entry first; a run while another holds the stage's "
            "lock is refused before anything is read or loaded (NOTE 4)",
            pre9_w == "refused" and register.BY_N[9].status == register.BUILT_STEP6
            and isinstance(e9_, register.RegisterStop) and not out_paths(unit, rnine)["p_calls"].exists() and nine_calls == []
            and r_l is None and isinstance(e_l, StageRefusal) and "holds the stage's lock" in str(e_l)
            and lk_calls == [],
            (pre9_w, e9_, e_l))
        # round 4: the STOP's record by reserve-then-rename, a Ctrl-C at the rename, every log write failing at an m
        # STOP, a log with no run line beside m's checkpoint, a dirty tail, a lock error named
        rki = root("ctrlc")
        real_rename = os.rename
        fired = {"n": 0}

        def ki_rename(a, b, *rest, **kw):
            if str(a).endswith(".reserve-1") and not fired["n"]:
                fired["n"] += 1
                raise KeyboardInterrupt("planted at the STOP's rename")
            return real_rename(a, b, *rest, **kw)
        os.rename = ki_rename
        try:
            r_k1, e_k1, _ = stub_run(rki, factory_with(rule=(lambda t, s, n, call: "zebra\n\nx"
                                                              if t == contrast and n == 6 else None)))
        except KeyboardInterrupt as e:
            r_k1, e_k1 = None, e
        finally:
            os.rename = real_rename
        evk, _ = read_calls(out_paths(unit, rki)["p_calls"])
        endk = [e for e in evk if e["event"] == "end"]
        r_k2, e_k2, _ = stub_run(rki, factory_with(), resume=True)
        rbi = root("mstop")
        full = {"disk": False}

        def all_fail(self, rec):
            if full["disk"]:
                raise OSError(28, "No space left on device (planted)")
            return real_write(self, rec)

        def boundary(t, s, n, call):
            if t == contrast and n == 6:
                full["disk"] = True                  # the disk fills at the STOP: every later write fails
                raise SystemExit("BOUNDARY INCIDENT (planted, m's form)")
            return None
        CallLog.write = all_fail
        try:
            r_b1, e_b1, _ = stub_run(rbi, factory_with(rule=boundary))
        finally:
            CallLog.write = real_write
        r_b2, e_b2, _ = stub_run(rbi, factory_with(), resume=True)
        reserves = sorted(x.name for x in (rbi / "ckpt").iterdir() if ".reserve-" in x.name)
        chk("stage: round 4's m-1 and NOTE 1 -- a Ctrl-C at the STOP's rename still writes the end line (stop marked, the "
            "marker not in place) before it propagates, and a --resume is refused; an m-style SystemExit STOP with every "
            "log write failing (a full disk) is held by its marker, renamed into place from the run's reservation, and a "
            "--resume is refused; no reservation is left behind",
            isinstance(e_k1, KeyboardInterrupt) and [e["exception"]["stop"] for e in endk] == [True]
            and endk[0]["stop_marker"].startswith("NOT IN PLACE") and isinstance(e_k2, StageRefusal)
            and isinstance(e_b1, SystemExit) and out_paths(unit, rbi)["p_stopped"].is_file()
            and isinstance(e_b2, StageRefusal) and "STOPPED" in str(e_b2) and reserves == [],
            (e_k1, endk[:1], e_k2, e_b1, e_b2, reserves))
        # round 5: the double failure announced once; a real SIGINT deferred; a rename that took reported in place;
        # the STOP's cause in the marker; the tail left as it was by a write that failed before its first byte
        rdf = root("double")
        real_fsync_dir = m_resume._fsync_dir

        def eio_rename(a, b, *rest, **kw):
            if ".reserve-" in str(a):
                raise OSError(5, "Input/output error (planted)")
            return real_rename(a, b, *rest, **kw)

        def eio_end(self, rec):
            if rec.get("event") == "end":
                raise OSError(5, "Input/output error (planted)")
            return real_write(self, rec)
        os.rename, CallLog.write = eio_rename, eio_end
        err_buf = io.StringIO()
        try:
            with contextlib.redirect_stderr(err_buf):
                r_d1, e_d1, out_d1 = stub_run(rdf, factory_with(rule=boundary))
        finally:
            os.rename, CallLog.write = real_rename, real_write
        r_d2, e_d2, out_d2 = stub_run(rdf, factory_with(), resume=True)
        rsg = root("sigint")

        def sig_rename(a, b, *rest, **kw):
            if ".reserve-" in str(a):
                os.kill(os.getpid(), signal.SIGINT)   # a real Ctrl-C, delivered during the recording
            return real_rename(a, b, *rest, **kw)
        os.rename = sig_rename
        try:
            try:
                stub_run(rsg, factory_with(rule=boundary))
                e_sg = None
            except KeyboardInterrupt as e:
                e_sg = e
        finally:
            os.rename = real_rename
        ends_sg = [e for e in read_calls(out_paths(unit, rsg)["p_calls"])[0] if e["event"] == "end"]
        rfs = root("fsyncdir")
        fs_arm = {"on": False}

        def bad_fsync_dir(d):
            if fs_arm["on"]:
                raise OSError(5, "Input/output error (planted)")
            return real_fsync_dir(d)

        def boundary_fs(t, s, n, call):
            if t == contrast and n == 6:
                fs_arm["on"] = True                   # the directory fsync fails from the STOP on
                raise SystemExit("BOUNDARY INCIDENT (planted, m's form)")
            return None
        m_resume._fsync_dir = bad_fsync_dir
        try:
            stub_run(rfs, factory_with(rule=boundary_fs))
        finally:
            m_resume._fsync_dir = real_fsync_dir
        ends_fs = [e for e in read_calls(out_paths(unit, rfs)["p_calls"])[0] if e["event"] == "end"]
        cause = json.loads(out_paths(unit, rbi)["p_stopped"].read_text(encoding="utf-8")).get("cause")
        chk("stage: round 5 -- the rename and the end line both failing (EIO) announce the unrecorded STOP once, on "
            "stdout and stderr, with no contradicting line, leave the reservation, and the next run names it stale (the "
            "PIN's residual); a real SIGINT during the recording is deferred until the end line is written, then "
            "raised, the marker in place; a rename that took before an error is recorded in place; the marker carries "
            "the STOP's cause",
            isinstance(e_d1, SystemExit) and out_d1.count("P-STOP NOT RECORDED") == 1 and "rests on" not in out_d1
            and "P-STOP NOT RECORDED" in err_buf.getvalue() and e_d2 is None and r_d2["status"] == "PASS"
            and "P-STALE STOP RESERVATION" in out_d2
            and r_d2["report"]["call_log"]["stale_reservations"] == ["OLMo-sft_time_p-STOPPED.json.reserve-1"]
            and isinstance(e_sg, KeyboardInterrupt) and out_paths(unit, rsg)["p_stopped"].is_file()
            and [e["stop_marker"] for e in ends_sg] == ["renamed into place"]
            and [e["stop_marker"] for e in ends_fs] == ["renamed into place (then OSError)"]
            and out_paths(unit, rfs)["p_stopped"].is_file()
            and isinstance(cause, dict) and cause.get("type") == "SystemExit" and "BOUNDARY" in cause.get("message", ""),
            (e_d1, out_d1[-300:], e_d2, e_sg, ends_sg[:1], ends_fs[:1], cause))
        with tempfile.TemporaryDirectory(prefix="p_stage_nobyte_") as td:
            lg = CallLog(Path(td) / "log.jsonl", Path(td))
            real_os_write = os.write

            def no_byte(fd, b):
                raise OSError(28, "No space left on device (planted)")
            os.write = no_byte
            try:
                lg.write({"event": "call", "run": 1})
                nb = "written"
            except OSError:
                nb = "raised"
            finally:
                os.write = real_os_write
            dirty_after = lg.dirty
            lg.write({"event": "end", "run": 1})
            lg.close()
            evn, lpn = read_calls(Path(td) / "log.jsonl")
        chk("stage: a log write that fails before its first byte leaves the tail clean -- no stray blank line, no "
            "malformed line (round 5's NOTE 5)", nb == "raised" and dirty_after is False and lpn == []
            and evn == [{"event": "end", "run": 1}], (nb, dirty_after, lpn, evn))
        rnr = root("norun")
        boom["armed"] = True
        stub_run(rnr, factory_with(rule=rule_boom))
        boom["armed"] = False
        out_paths(unit, rnr)["p_calls"].write_bytes(b"garbage\n")
        nr_calls: list = []
        r_n2, e_n2, _ = stub_run(rnr, factory_with(calls=nr_calls), resume=True)
        with tempfile.TemporaryDirectory(prefix="p_stage_dirty_") as td:
            lg = CallLog(Path(td) / "log.jsonl", Path(td))
            lg._put(b'{"event": "call", "ru')          # a write that left its line torn
            lg.dirty = True
            lg.write({"event": "end", "run": 1})
            lg.close()
            evd, lpd = read_calls(Path(td) / "log.jsonl")
        real_flock = fcntl.flock

        import errno as _errno

        def enolck(fd, op):
            raise OSError(_errno.ENOLCK, "No locks available (planted)")
        fcntl.flock = enolck
        try:
            r_f, e_f, _ = stub_run(root("enolck"), factory_with())
        finally:
            fcntl.flock = real_flock
        chk("stage: round 4's NOTE 2 -- a log with no run line beside m's checkpoint is refused before the load (never "
            "an empty record); a line a failed write left torn is ended before the next record (one malformed line, "
            "the record whole); m-2 -- a lock error other than one held elsewhere is named, never read as 'held'",
            isinstance(e_n2, StageRefusal) and "no run line" in str(e_n2) and nr_calls == []
            and evd == [{"event": "end", "run": 1}] and len(lpd) == 1
            and isinstance(e_f, StageRefusal) and "unavailable on this filesystem" in str(e_f)
            and "holds" not in str(e_f), (e_n2, evd, lpd, e_f))
        with tempfile.TemporaryDirectory(prefix="p_stage_lsep_") as td:
            lg = CallLog(Path(td) / "log.jsonl", Path(td))
            lg.write({"event": "call", "run": 1, "text": "Two.\u2028ok\u0085\u2029 caf\u00e9"})
            lg.close()
            raw_l = (Path(td) / "log.jsonl").read_bytes()
            evl, lpl = read_calls(Path(td) / "log.jsonl")
        chk("stage: a logged text carrying U+2028, U+0085, U+2029 or any non-ASCII character is written as ASCII and "
            "read back whole, one line (round 3's MAJOR, m-2)",
            raw_l.isascii() and raw_l.count(b"\n") == 1 and lpl == []
            and evl == [{"event": "call", "run": 1, "text": "Two.\u2028ok\u0085\u2029 caf\u00e9"}], (raw_l[:80], lpl))
        # THE QUALIFICATION (the seat's answers of 2026-11-10, 42c5a92, §2-§3): the gate's counts, names and lock line;
        # G-F0m-OLMo (p) on m's scripted double, its prior a G-TIME (p) run in the same scratch root
        mtext = (REPO / "scripts" / "m_sessions.py").read_text(encoding="utf-8")
        mline = [ln for ln in mtext.splitlines() if ln.startswith("OLMO_QUAL_LOCK_LINE = ")]
        n_files = {}
        for u in UNITS:
            for g in GATES:
                for t, _n in templates_counts(u, g):
                    sf = REPO / "data" / "p" / "schedules" / f"{u}_{g}_{t}.json"
                    n_files[(u, g, t)] = json.loads(sf.read_text(encoding="utf-8"))["n"]
        lk_ok = (qual_lock_problems(unit, "x\n  G-TIME-OLMo-sft port acceptance recorded\ny") == []
                 and bool(qual_lock_problems(unit, "1. Acceptance: G-TIME-OLMo-sft port acceptance recorded."))
                 and bool(qual_lock_problems(unit, "G-TIME-OLMo-dpo port acceptance recorded"))
                 and bool(qual_lock_problems(unit, "# LOCK-p-OLMo-sft v0.1")))
        try:
            precheck(unit, stub=True, gate="id")
            bad_gate = "ran"
        except StageRefusal as e:
            bad_gate = "refused" if "p's stages are" in str(e) else f"other: {e}"
        qp = out_paths(unit, DEFAULT_OUT_P, gate="qual")
        chk("stage: p's gates are time and qual at m:302's counts (1 + 1, 8 + 16), each the committed gate files' n; the "
            "qual stage's label and outputs carry its own name (_qual_), G-TIME's unchanged; a stage p does not run (G-ID, "
            "m:267) is refused before anything loads; QUAL_LOCK_LINE is the text of m's OLMO_QUAL_LOCK_LINE (scripts/"
            "m_sessions.py read as text, never imported), required as a whole line, at its own checkpoint",
            GATES == ("time", "qual") and COUNTS == {"time": (1, 1), "qual": (8, 16)}
            and all(n_files[(u, g, t)] == n for u in UNITS for g in GATES for t, n in templates_counts(u, g))
            and templates_counts(unit) == templates_counts(unit, "time") == [(contrast, 1), (sham, 1)]
            and templates_counts(unit, "qual") == [(contrast, 8), (sham, 16)]
            and label(unit) == label(unit, "time") == "G-TIME-OLMo-sft (p)"
            and label(unit, "qual") == "G-F0m-OLMo-sft (p)"
            and [qp[k].name for k in ("p_report", "p_calls", "p_stopped", "p_lock", "m_ckpt", "m_report", "m_reads")]
            == ["OLMo-sft_qual_p-report.json", "OLMo-sft_qual_p-calls.jsonl", "OLMo-sft_qual_p-STOPPED.json",
                "OLMo-sft_qual_p.lock", "OLMo-sft_qual.json", "OLMo-sft_qual_report.json", "OLMo-sft_qual_reads.json"]
            and out_paths(unit, DEFAULT_OUT_P)["p_calls"].name == "OLMo-sft_time_p-calls.jsonl"
            and bad_gate == "refused" and mline == [f'OLMO_QUAL_LOCK_LINE = "{QUAL_LOCK_LINE}"'] and lk_ok,
            (sorted(set(n_files.values())), bad_gate, mline, lk_ok))

        def tree_shas(r: Path, part: str) -> dict:
            return {x.relative_to(r).as_posix(): _sha(x.read_bytes()) for x in sorted(r.rglob("*"))
                    if x.is_file() and part in x.name}
        rq = root("qual")
        rt_q, et_q, _ = stub_run(rq, factory_with())
        time_before = tree_shas(rq, "_time")
        q_calls: list = []
        rr_q, er_q, _ = stub_run(rq, factory_with(gate="qual", calls=q_calls), gate="qual")
        ok_q, det_q = (er_q is None and rr_q is not None and rr_q["status"] == "PASS"), (er_q, rr_q and rr_q["status"])
        if ok_q:
            ckq = json.loads(Path(rr_q["result"]["checkpoint"]).read_text(encoding="utf-8"))
            repq, sessq = rr_q["report"], ckq["sessions"]
            n_sham = sum(len(s["rounds"]) for s in sessq if not s["contrast"])
            arms_q = [v["arm"] for v in ckq["identity"]["key_templates"].values()]
            ok_q = (ckq["identity"]["stage"] == "qual" and ckq["identity"]["n"] == {contrast: 8, sham: 16}
                    and len(arms_q) == 2 and all(a.startswith("p-olmo-qual|") for a in arms_q)
                    and {k: ckq["identity"][k] for k in identity.P_FIELDS} == identity.run_values()
                    and len(sessq) == 24 and sum(bool(s["contrast"]) for s in sessq) == 8
                    and all(s["verified"] for s in sessq)
                    and (ckq.get("prior") or {}).get("stage") == "time" and ckq["prior"].get("status") == "PASS"
                    and ckq["prior"].get("adjudication") is None
                    and repq["stage"] == "G-F0m-OLMo-sft (p)" and repq["status"] == "PASS"
                    and repq["proxy"]["sham"]["n_rounds"] == n_sham > 0
                    and repq["proxy"]["sham"]["n_attributed"] == n_sham and repq["proxy"]["attribution_complete"] is True
                    and repq["proxy"]["contrast"] == CONTRAST_WITHHELD_QUAL
                    and repq["form"] == REPORT_TEXT["qual"]["form"]
                    and repq["call_log"]["n_runs"] == 1 and repq["call_log"]["path"] == "ckpt/OLMo-sft_qual_p-calls.jsonl"
                    and repq["counters"]["hair_trigger"]["n"] == 0 and repq["register_entered"] == list(ENTERED)
                    and rr_q["paths"]["p_report"].name == "OLMo-sft_qual_p-report.json"
                    and tree_shas(rq, "_time") == time_before and q_calls == ["factory"])
            det_q = (ckq["identity"].get("n"), len(sessq), ckq.get("prior"), repq["stage"], repq["proxy"]["sham"])
        chk("stage: a full G-F0m-OLMo (p) on m's scripted OLMo double after a G-TIME (p) in the same scratch root -- m's "
            "run_gate_stage at gate qual under entries (1), (2), (6)-(9): PASS, 24 verified sessions (8 contrast, 16 "
            "sham), the identity's stage qual carrying p's four fields and p's qual arm keys, m's prior licence "
            "recorded (G-TIME, PASS, no adjudication); p's report under the _qual_ names on the read domain (every sham "
            "round of the sixteen "
            "sessions attributed, the contrast withheld); G-TIME's outputs untouched",
            et_q is None and rt_q is not None and rt_q["status"] == "PASS" and ok_q, det_q)
        if ok_q:
            firstq = rr_q["paths"]["p_report"].read_bytes()
            rr_q["paths"]["p_report"].rename(rr_q["paths"]["p_report"].with_name("moved-q.json"))
            _, howq = write_report(unit, rq, gate="qual")
            againq = rr_q["paths"]["p_report"].read_bytes() == firstq
            rq2, eq2, _ = stub_run(rq, factory_with(gate="qual"), resume=True, gate="qual")
            ev_t = read_calls(out_paths(unit, rq)["p_calls"])[0]
            ev_q = read_calls(out_paths(unit, rq, gate="qual")["p_calls"])[0]
            chk("stage: p's G-F0m-OLMo (p) report is re-derived byte for byte (the driver's qual-report), and a run on "
                "the ended stage is refused before it writes any record; a G-TIME (p) call log is not G-F0m-OLMo (p)'s, "
                "nor the reverse (m-1, per gate)",
                againq and howq == "written" and rq2 is None and isinstance(eq2, StageRefusal)
                and "p's report" in str(eq2) and log_consistency_problems(unit, ev_t) == []
                and log_consistency_problems(unit, ev_q, gate="qual") == []
                and bool(log_consistency_problems(unit, ev_t, gate="qual"))
                and bool(log_consistency_problems(unit, ev_q)), (againq, howq, eq2))
        rnp = root("qual-noprior")
        np_calls: list = []
        r_np, e_np, _ = stub_run(rnp, factory_with(gate="qual", calls=np_calls), gate="qual")
        rne = root("qual-unended")
        boom["armed"] = True
        stub_run(rne, factory_with(rule=rule_boom))       # an interrupted G-TIME (p): its checkpoint has no end
        boom["armed"] = False
        ne_calls: list = []
        r_ne, e_ne, _ = stub_run(rne, factory_with(gate="qual", calls=ne_calls), gate="qual")
        chk("stage: G-F0m-OLMo (p) is refused before the load when G-TIME (p)'s checkpoint is absent or has not ended "
            "(m's prior_gate, run before the load) -- no call log, no reservation, the factory never called",
            r_np is None and isinstance(e_np, StageRefusal) and "PRIOR STAGE ABSENT" in str(e_np) and np_calls == []
            and not out_paths(unit, rnp, gate="qual")["p_calls"].exists()
            and r_ne is None and isinstance(e_ne, StageRefusal) and "PRIOR STAGE NOT ENDED" in str(e_ne)
            and ne_calls == [] and not out_paths(unit, rne, gate="qual")["p_calls"].exists()
            and not list((rne / "ckpt").glob("*_qual_p-STOPPED.json.reserve-*")), (e_np, e_ne, np_calls, ne_calls))
        repsq, linesq = {}, {}
        for tag, n_free in (("none", None), ("ci0", 5), ("ci1", 6)):
            rule_q = None if n_free is None else (lambda t, s, n, call, _n=n_free: "{Pc}." if t == contrast and s == 3
                                                  and n == _n else None)
            rb_ = root(f"qexcl-{tag}")
            stub_run(rb_, factory_with())
            rr, ee, _ = stub_run(rb_, factory_with(rule=rule_q, gate="qual"), gate="qual")
            if ee is not None:
                repsq[tag] = f"{type(ee).__name__}: {ee}"
                continue
            ck_ = json.loads(Path(rr["result"]["checkpoint"]).read_text(encoding="utf-8"))
            con = [s for s in ck_["sessions"] if s["contrast"] and s["s"] == 3][0]
            norm = json.loads(json.dumps(rr["report"]))
            for k in ("checkpoint", "call_log"):
                norm[k]["sha256"] = "*"
            for k in ("report", "reads"):
                norm["m_outputs"][k]["sha256"] = "*"
            repsq[tag] = (norm, sum(1 for x in con["rounds"] if x["phase"] == "free"), bool(con.get("exclusion")))
            linesq[tag] = [re.sub(r"[0-9a-f]{64}", "*", ln) for ln in summary_lines(rr)]
        sameq = all(isinstance(v, tuple) for v in repsq.values()) and len({json.dumps(v[0], sort_keys=True)
                                                                            for v in repsq.values()}) == 1
        chk("stage: blinding at qual -- a contrast free-round exclusion planted in contrast session 3 at free round 0, "
            "at free round 1, or none: that session's free rounds differ (6, 1, 2 generated) and p's report and closing "
            "lines do not, but for the outputs' sha256s",
            sameq and len({json.dumps(v, sort_keys=True) for v in linesq.values()}) == 1
            and [repsq[t][1:] for t in ("none", "ci0", "ci1")] == [(6, False), (1, True), (2, True)],
            {t: (v[1:] if isinstance(v, tuple) else v) for t, v in repsq.items()})
        rqs = root("qual-stop")
        stub_run(rqs, factory_with())
        rule_qs = (lambda t, s, n, call: "zebra\n\nx" if t == contrast and s == 2 and n == 6 else None)
        r_qs, e_qs, _ = stub_run(rqs, factory_with(rule=rule_qs, gate="qual"), gate="qual")
        qs_calls: list = []
        r_qs2, e_qs2, _ = stub_run(rqs, factory_with(gate="qual", calls=qs_calls), resume=True, gate="qual")
        evq_s, _ = read_calls(out_paths(unit, rqs, gate="qual")["p_calls"])
        mk = out_paths(unit, rqs, gate="qual")["p_stopped"]
        mk_stage = json.loads(mk.read_text(encoding="utf-8")).get("stage") if mk.is_file() else None
        chk("stage: a ProxyStop inside a G-F0m-OLMo (p) session is recorded under the qual stage's own names -- its "
            "marker (its stage the qual stage's), its run line's stage, its end line's stop mark -- and blocks a "
            "--resume before the load; G-TIME's record beside it carries no STOP",
            r_qs is None and isinstance(e_qs, ProxyStop) and mk_stage == "G-F0m-OLMo-sft (p)"
            and [e["exception"]["stop"] for e in evq_s if e["event"] == "end"] == [True]
            and [e.get("stage") for e in evq_s if e["event"] == "run"] == ["G-F0m-OLMo-sft (p)"]
            and not out_paths(unit, rqs)["p_stopped"].exists()
            and r_qs2 is None and isinstance(e_qs2, StageRefusal) and "STOPPED" in str(e_qs2) and qs_calls == [],
            (e_qs, e_qs2, mk_stage, qs_calls))
        # The qual review's N-7: the wiring that keeps qual's refusals before the load
        rpr = root("qual-priors")
        stub_run(rpr, factory_with())
        tck = out_paths(unit, rpr)["m_ckpt"]
        pv = {}
        for tag, edit in (("m-form", lambda ck: ck["identity"].update(proposal="PROPOSAL-m")),
                          ("other-p", lambda ck: ck["identity"].update(proposal_p_sha256="0" * 64)),
                          ("ended-stop", lambda ck: ck["stage_end"].update(status="STOP")),
                          ("ended-pause", lambda ck: ck["stage_end"].update(status="PAUSE"))):
            d = root(f"qual-prior-{tag}")
            (d / "ckpt").mkdir(parents=True, exist_ok=True)
            ck = json.loads(tck.read_text(encoding="utf-8"))
            edit(ck)
            (d / "ckpt" / tck.name).write_text(json.dumps(ck), encoding="utf-8")
            pv[tag] = prior_problems(unit, d / "ckpt" / tck.name, stub=True, proposal_sha256=gcal.M_PROPOSAL_SHA256)
        pv["stub-as-stub"] = prior_problems(unit, tck, stub=True, proposal_sha256=gcal.M_PROPOSAL_SHA256)
        pv["stub-as-real"] = prior_problems(unit, tck, stub=False, proposal_sha256=gcal.M_PROPOSAL_SHA256)
        pv["other-m-pin"] = prior_problems(unit, tck, stub=True, proposal_sha256="1" * 64)
        chk("stage: the prior's check before the load (prior_problems; the qual review's N-5, N-7 (a), (b)) -- a stub "
            "G-TIME (p) licenses a stub qual run and not a real one (PRIOR STAGE ON THE STUB); a prior under another m "
            "pin, one that ended STOP, one that ended PAUSE (no adjudication input exists), and one whose identity is m's "
            "or another p proposal's are each refused",
            pv["stub-as-stub"] == [] and any("PRIOR STAGE ON THE STUB" in x for x in pv["stub-as-real"])
            and any("UNDER ANOTHER PROPOSAL" in x for x in pv["other-m-pin"])
            and any("PRIOR STAGE STOP" in x for x in pv["ended-stop"])
            and any("PRIOR STAGE PAUSE" in x for x in pv["ended-pause"])
            and any("not p's" in x and "proposal is" in x for x in pv["m-form"])
            and any("not p's" in x and "proposal_p_sha256" in x for x in pv["other-p"]),
            {k: [x[:90] for x in v] for k, v in pv.items()})
        seen_lk: list = []
        real_qlp = qual_lock_problems
        g_ = globals()
        g_["qual_lock_problems"] = lambda u, text: (seen_lk.append((u, text)), ["P-SELFTEST-SENTINEL"])[1]
        pc = {}
        try:
            with mock.patch.dict(os.environ, {k: v for k, v in os.environ.items() if k != m_resume.POD_ENV},
                                 clear=True):
                for gg in GATES:
                    try:
                        precheck(unit, stub=False, gate=gg)
                        pc[gg] = "clear"
                    except StageRefusal as e:
                        pc[gg] = str(e)
        finally:
            g_["qual_lock_problems"] = real_qlp
        lock_txt = (m_stages._committed(lock_rel(unit))[1] or b"").decode("utf-8", "replace")
        saved_counts = dict(COUNTS)
        COUNTS["qual"], COUNTS["time"] = (9, 16), (2, 1)
        try:
            cp_bad = counts_problems(unit, "qual")
            cq_pre, ct_pre = "passed", "passed"
            try:
                precheck(unit, stub=True, gate="qual")
            except StageRefusal as e:
                cq_pre = "refused" if "the counts:" in str(e) and "not m:302's 9" in str(e) else f"other: {e}"
            try:
                precheck(unit, stub=True, gate="time")
            except StageRefusal as e:
                ct_pre = f"refused: {e}"
        finally:
            COUNTS.clear()
            COUNTS.update(saved_counts)
        chk("stage: the non-stub precheck (the pod id removed, so it refuses) calls the v0.2-line check at qual only, "
            "on the committed lock's text, and its problems enter the qual refusal and not the time one; it names "
            "G-F0m-OLMo for qual (the qual review's N-7 (c), R2-2 (b)); the counts match the committed "
            "gate files at qual, and a COUNTS that does not is refused by the precheck at qual, before the load, and not "
            "at time (the qual review's N-4, R2-1)",
            [u for u, _ in seen_lk] == [unit] and seen_lk[0][1] == lock_txt and bool(lock_txt)
            and "P-SELFTEST-SENTINEL" in pc.get("qual", "") and "P-SELFTEST-SENTINEL" not in pc.get("time", "")
            and "POD ID ABSENT" in pc.get("qual", "") and "G-F0m-OLMo-sft (p)" in pc.get("qual", "")
            and "POD ID ABSENT" in pc.get("time", "") and counts_problems(unit, "qual") == []
            and len(cp_bad) == 1 and "not m:302's 9" in cp_bad[0] and cq_pre == "refused" and ct_pre == "passed",
            ([u for u, _ in seen_lk], {k: v[:120] for k, v in pc.items()}, cp_bad, cq_pre, ct_pre[:160]))
        rns = root("qual-prior-nonstub")
        stub_run(rns, factory_with())                   # a stub-written G-TIME (p) prior in a scratch root
        ns_calls: list = []
        pre_ns = {"unit": unit, "gate": "qual", "stub": False, "gate_line": None, "backend_of_record": None,
                  "identity_extra": {"proposal_sha256": gcal.M_PROPOSAL_SHA256}}
        try:
            _run_gate_locked(unit, "qual", factory_with(gate="qual", calls=ns_calls), stub=False, resume=False, out=rns,
                             pp=out_paths(unit, rns, gate="qual"), pre=pre_ns, echo=lambda line: None)
            e_ns = None
        except SystemExit as e:
            e_ns = e
        chk("stage: the run's own call site passes the run's stub flag to the prior's check -- a non-stub qual run on a "
            "stub-written G-TIME (p) is refused before the load (PRIOR STAGE ON THE STUB), the factory never called, no "
            "call log or reservation written (the qual review's R2-2 (a))",
            isinstance(e_ns, StageRefusal) and "PRIOR STAGE ON THE STUB" in str(e_ns) and ns_calls == []
            and not out_paths(unit, rns, gate="qual")["p_calls"].exists()
            and not list((rns / "ckpt").glob("*_qual_p-STOPPED.json.reserve-*")), (e_ns, ns_calls))
        gm_calls: list = []
        r_gm, e_gm, _ = stub_run(root("qual-gate-mismatch"), factory_with(gate="qual", calls=gm_calls),
                                 pre=precheck(unit, stub=True), gate="qual")
        rqr = root("qual-resume")
        stub_run(rqr, factory_with())
        qboom = {"armed": True}

        def rule_qboom(t, s, n, call):
            if qboom["armed"] and t == sham and s == 5 and n == 2:
                raise RuntimeError("p-selftest planted interruption (qual)")
            return None
        rqa, eqa, _ = stub_run(rqr, factory_with(rule=rule_qboom, gate="qual"), gate="qual")
        qboom["armed"] = False
        rqb, eqb, _ = stub_run(rqr, factory_with(rule=rule_qboom, gate="qual"), resume=True, gate="qual")
        rep_qr = rqb["report"] if rqb else {}
        chk("stage: a precheck taken at time is refused by a qual run before anything is read or loaded (the qual "
            "review's N-7 (e)); an interruption in a qual sham session, then --resume, PASSes with both runs in the call "
            "log and every sham round of the sixteen sessions attributed (the qual review's N-7 (f))",
            r_gm is None and isinstance(e_gm, StageRefusal) and "at 'time'" in str(e_gm) and gm_calls == []
            and rqa is None and isinstance(eqa, RuntimeError) and eqb is None and rqb["status"] == "PASS"
            and rep_qr["call_log"]["n_runs"] == 2 and rep_qr["proxy"]["attribution_complete"] is True
            and [(r["outcome"], r["exception_type"]) for r in rep_qr["call_log"]["runs"]]
            == [("exception", "RuntimeError"), ("returned", None)],
            (e_gm, eqa, eqb, rep_qr.get("call_log", {}).get("runs")))
        rbs = root("qual-barstop")
        stub_run(rbs, factory_with())
        r_bs, e_bs, _ = stub_run(rbs, factory_with(rule=(lambda t, s, n, call: "{TOLD}" if t == sham and n >= 5
                                                         else None), gate="qual"), gate="qual")
        bs_calls: list = []
        r_bs2, e_bs2, _ = stub_run(rbs, factory_with(gate="qual", calls=bs_calls), resume=True, gate="qual")
        chk("stage: a G-F0m-OLMo (p) whose sham rounds echo the TOLD line ends STOP on m's qual bar -- m's status, "
            "p's report written with it, no p STOP marker (m's bar is not p's STOP) -- and a later run is refused "
            "before the load (the qual review's N-7 (f))",
            e_bs is None and r_bs is not None and r_bs["status"] == "STOP" and r_bs["report"]["status"] == "STOP"
            and out_paths(unit, rbs, gate="qual")["p_report"].is_file()
            and not out_paths(unit, rbs, gate="qual")["p_stopped"].exists()
            and r_bs2 is None and isinstance(e_bs2, StageRefusal) and bs_calls == [],
            (e_bs, r_bs and r_bs["status"], e_bs2, bs_calls))
        # THE CAMPAIGN (the campaign wiring): its values, its rulings, its state, and runs on m's scripted double
        def camp_factory(r: Path, rule=None, calls=None):
            def factory():
                if calls is not None:
                    calls.append("factory")
                a = m_testing.OLMoScriptedAdapter("p-stage-selftest")
                cells = {}
                for t in campaign_arms(unit):
                    d = json.loads((r / "schedules" / f"{unit}_campaign_{t}.json").read_text(encoding="utf-8"))
                    cells.update({(t, j): c for j, c in enumerate(d["cells"])})
                a.load(m_stages._script_policy(unit, "campaign", cells, rule), None)
                return a
            return factory

        @contextlib.contextmanager
        def hour_cap(v):
            # SELF-TEST ONLY: the unit's cap set for the case's duration, restored after (the cap is the PI's)
            saved = dict(CAMPAIGN_HOUR_CAP)
            CAMPAIGN_HOUR_CAP[unit] = v
            try:
                yield
            finally:
                CAMPAIGN_HOUR_CAP.clear()
                CAMPAIGN_HOUR_CAP.update(saved)

        def camp_run(r: Path, fac, *, resume: bool = False, adjudication=None, pi_stop=None, cap_h=40):
            m_scaffold._of_record.cache_clear()
            buf = io.StringIO()
            try:
                with hour_cap(cap_h), olmo_stub_startup(), pod(), contextlib.redirect_stdout(buf):
                    return (run_campaign(unit, fac, stub=True, out_root=r, resume=resume, adjudication=adjudication,
                                         pi_stop=pi_stop), None, buf.getvalue())
            except (SystemExit, Exception) as e:
                return None, e, buf.getvalue()

        def qualified(name: str) -> Path:
            r = root(name)
            stub_run(r, factory_with())
            stub_run(r, factory_with(gate="qual"), gate="qual")
            return r

        def m_ck(r: Path) -> dict:
            try:
                return json.loads(out_paths(unit, r, gate="campaign")["m_ckpt"].read_text(encoding="utf-8"))
            except (OSError, ValueError):
                return {}

        a0, a0s = campaign_arms(unit)
        gpw = {u: gpwr_problems(u)[0] for u in UNITS}
        saved_lc = dict(CAMPAIGN_LAUNCH_COUNTS)
        try:
            CAMPAIGN_LAUNCH_COUNTS[unit] = (128, 64)
            gpw_bad = gpwr_problems(unit)[0]
        finally:
            CAMPAIGN_LAUNCH_COUNTS.clear()
            CAMPAIGN_LAUNCH_COUNTS.update(saved_lc)
        with hour_cap(40):
            lines40 = campaign_lock_lines(unit)
            lk40 = (campaign_lock_problems(unit, f"x\n{lines40[0]}\n{lines40[1]}\ny"),
                    campaign_lock_problems(unit, f"{lines40[0]}.\n{lines40[1]}"),
                    campaign_lock_problems(unit, lines40[0].replace("sft", "dpo") + f"\n{lines40[1]}"),
                    campaign_lock_problems(unit, lines40[0]))
        caps = {}
        for v in (4, 4.5, 0, -1, True, float("inf"), "4", None):
            with hour_cap(v):
                caps[repr(v)] = (campaign_hour_cap(unit), campaign_lock_lines(unit)[1:])
        cp_out = out_paths(unit, DEFAULT_OUT_P, gate="campaign")
        chk("stage: the campaign's values (the campaign wiring's PIN) -- STAGES the gates and the campaign; the launch "
            "counts G-PWR (p)'s of record at each unit (gpwr_problems clean, and a differing count refused), keyed by "
            "the unit's arms, contrast first; the floors the package's, 80 and 32; the lock's lines whole lines (a "
            "trailing period, another unit's arms, a missing cap line each refused); the campaign named campaign-OLMo-"
            "{ckpt} (p), its outputs _campaign_ and m's adjudication excerpt in place of reads; the hour cap a positive "
            "finite int or float (4.5 h kept, its line from the same value), never 0, a negative, a bool, an infinity, "
            "a text or None (round 1's MINOR-2)",
            STAGES == ("time", "qual", "campaign") and all(v == [] for v in gpw.values()) and bool(gpw_bad)
            and campaign_launch_counts(unit) == {a0: 96, a0s: 64} and list(campaign_launch_counts(unit)) == [a0, a0s]
            and campaign_floors(unit) == {a0: 80, a0s: 32}
            and lines40 == (f"launch counts = {a0} 96, {a0s} 64", "hour cap = 40 h")
            and lk40[0] == [] and all(bool(x) for x in lk40[1:])
            and label(unit, "campaign") == "campaign-OLMo-sft (p)" and label("Q-F0", "campaign") == "campaign ('Q-F0', "
            "not a p unit)"
            and cp_out["p_calls"].name == "OLMo-sft_campaign_p-calls.jsonl"
            and cp_out["m_excerpt"].name == "OLMo-sft_campaign_adjudication.json" and "m_reads" not in cp_out
            and caps == {"4": (4, ("hour cap = 4 h",)), "4.5": (4.5, ("hour cap = 4.5 h",)), "0": (None, ()),
                         "-1": (None, ()), "True": (None, ()), "inf": (None, ()), "'4'": (None, ()), "None": (None, ())},
            (gpw, gpw_bad, lines40, lk40, label(unit, "campaign"), caps))
        try:
            with hour_cap(None):
                precheck(unit, stub=True, gate="campaign")
            no_cap = "ran"
        except StageRefusal as e:
            no_cap = "refused" if "the hour cap is not set" in str(e) else f"other: {e}"
        with hour_cap(40):
            pre_c = precheck(unit, stub=True, gate="campaign")
        chk("stage: the campaign's precheck refuses an unset hour cap (the PI's cap share, a LOCK-p v1.0 value) before "
            "anything loads, and passes on the stub with a cap set; the caps of record are the PI's word of 2026-11-14, "
            "\"2 h each\", their lock lines \"hour cap = 2 h\" at each unit",
            no_cap == "refused" and pre_c["gate"] == "campaign"
            and CAMPAIGN_HOUR_CAP == {"OLMo-sft": 2, "OLMo-dpo": 2, "OLMo-instruct": 2}
            and all(campaign_hour_cap(u) == 2 and campaign_lock_lines(u)[1] == "hour cap = 2 h" for u in UNITS),
            (no_cap, CAMPAIGN_HOUR_CAP))
        with tempfile.TemporaryDirectory(prefix="p_stage_rulings_") as td_r:
            tr = Path(td_r)
            (tr / "bom.txt").write_bytes(b"\xef\xbb\xbfThe seat's ruling.\n")
            (tr / "zw.txt").write_text(" ​\t\n", encoding="utf-8")
            (tr / "bad.txt").write_bytes(b"\xff\xfe\x00")
            rt = (ruling_texts(str(tr / "bom.txt"), None), ruling_texts(None, str(tr / "zw.txt")),
                  ruling_texts(str(tr / "absent.txt"), None), ruling_texts(str(tr), None),
                  ruling_texts(None, str(tr / "bad.txt")))
        chk("stage: ruling_texts reads a ruling file under m's rule -- a byte-order mark dropped; a blank text (a "
            "zero-width space), an absent path, a directory and undecodable bytes each refused",
            rt[0] == ({"adjudication": "The seat's ruling.\n", "pi_stop": None}, []) and "blank" in rt[1][1][0]
            and "not a regular file" in rt[2][1][0] and "not a regular file" in rt[3][1][0]
            and "unreadable as UTF-8" in rt[4][1][0], [x[1] for x in rt])
        with tempfile.TemporaryDirectory(prefix="p_stage_cstate_") as td_s:
            ts = Path(td_s)

            def ck_file(name: str, obj) -> Path:
                f = ts / name
                f.write_text(obj if isinstance(obj, str) else json.dumps(obj), encoding="utf-8")
                return f

            def pause(kind="look", at=40, adj=None, arm=None):
                return {"kind": kind, "at_launches": at, "adjudication": adj, "arm": arm}
            sess = [{"template": a0}]
            f_open = ck_file("open.json", {"sessions": sess, "campaign": {"pauses": [pause()], "pi_stop": None}})
            f_qf0 = ck_file("qf0arm.json", {"sessions": sess, "campaign": {"pauses": [pause(arm="A0")]}})
            f_bad = ck_file("bad.json", "{not json")
            f_end = ck_file("end.json", {"sessions": sess, "campaign": {"pauses": [], "terminal": {"status": "COMPLETE"}}})
            f_pend = ck_file("pend.json", {"sessions": sess, "campaign": {"pauses": [pause(adj="r1")]},
                                           m_resume.END_PENDING: {"status": "COMPLETE"}})
            f_none = ck_file("none.json", {"sessions": [], "campaign": {"pauses": []}})
            f_adj = ck_file("adj.json", {"sessions": sess, "campaign": {"pauses": [pause(adj="ruling one"), pause(at=80)]}})
            f_done = ck_file("done.json", {"sessions": sess, "campaign": {"pauses": [pause(adj="ruling one")]}})
            f_exh = ck_file("exh.json", {"sessions": sess, "campaign": {"pauses": [pause("schedule_exhausted", 90, None, a0s)]}})
            f_pi = ck_file("pi.json", {"sessions": sess, "campaign": {"pauses": [pause()], "pi_stop": "stop one"}})
            states = {n: campaign_state(f, unit)[0] for n, f in (("absent", ts / "absent.json"), ("open", f_open),
                                                                 ("qf0", f_qf0), ("bad", f_bad), ("end", f_end),
                                                                 ("pend", f_pend))}
            rpr = {"none": campaign_ruling_problems(f_open, unit, None, None),
                   "adj_open": campaign_ruling_problems(f_open, unit, "a ruling", None),
                   "mismatch": campaign_ruling_problems(f_pi, unit, None, "stop two"),
                   "pending": campaign_ruling_problems(f_pend, unit, "a ruling", None),
                   "pi_none": campaign_ruling_problems(f_none, unit, None, "stop"),
                   "exhausted": campaign_ruling_problems(f_exh, unit, "a ruling", None),
                   "exhausted_pi": campaign_ruling_problems(f_exh, unit, None, "stop"),
                   "reused": campaign_ruling_problems(f_adj, unit, " ruling one\n", None),
                   "no_pause": campaign_ruling_problems(f_done, unit, "a ruling", None),
                   "ended": campaign_ruling_problems(f_end, unit, "a ruling", None)}
        chk("stage: campaign_state reads m's campaign checkpoint tolerantly (absent, open, pending, ended; unreadable "
            "when not JSON or when a pause names Q-F0's arm A0), and campaign_ruling_problems refuses, in m's driver's "
            "words, a PI stop other than the one recorded (CHECKPOINT MISMATCH), a ruling beside an end pending, a PI "
            "stop with nothing launched, an adjudication alone on an exhausted schedule, an earlier pause's ruling "
            "offered again (RULING REUSED) and an adjudication with no open pause; none when the ruling fits",
            states == {"absent": "absent", "open": "open", "qf0": "unreadable", "bad": "unreadable", "end": "ended",
                       "pend": "pending"}
            and rpr["none"] == [] and rpr["adj_open"] == [] and rpr["exhausted_pi"] == [] and rpr["ended"] == []
            and rpr["mismatch"][0].startswith("CHECKPOINT MISMATCH")
            and rpr["pending"][0].startswith("RULING BESIDE AN END PENDING")
            and rpr["pi_none"][0].startswith("PI STOP REFUSED") and rpr["exhausted"][0].startswith("SCHEDULE EXHAUSTED")
            and rpr["reused"][0].startswith("RULING REUSED") and rpr["no_pause"][0].startswith("NO PAUSE TO ADJUDICATE"),
            (states, {k: (v[0][:40] if v else v) for k, v in rpr.items()}))
        # a full campaign: COMPLETE at the floors, p's report written, the record's form
        rcc = qualified("camp-complete")
        r_c, e_c, _ = camp_run(rcc, camp_factory(rcc))
        ok_c, det_c = e_c is None and r_c is not None and r_c["status"] == "COMPLETE", (e_c, r_c and r_c["status"])
        if ok_c:
            ppc = r_c["paths"]
            rep_c = json.loads(ppc["p_report"].read_text(encoding="utf-8"))
            ev_c, lp_c = read_calls(ppc["p_calls"])
            runs_c = [e for e in ev_c if e.get("event") == "run"]
            ok_c = (rep_c["status"] == "COMPLETE" and rep_c["stage"] == "campaign-OLMo-sft (p)"
                    and set(rep_c["m_outputs"]) == {"report", "adjudication_excerpt"}
                    and rep_c["m_outputs"]["report"]["sha256"] is not None
                    and rep_c["proxy"]["attribution_complete"] is True
                    and rep_c["proxy"]["sham"]["n_attributed"] == rep_c["proxy"]["sham"]["n_rounds"] > 0
                    and rep_c["form"] == REPORT_TEXT["campaign"]["form"] and lp_c == []
                    and [r["stage"] for r in runs_c] == ["campaign-OLMo-sft (p)"]
                    and runs_c[0]["register_entered"] == list(ENTERED) and not ppc["p_stopped"].exists()
                    and r_c["result"]["launches"] == {a0: 80, a0s: 32})
            det_c = (rep_c["status"], rep_c["m_outputs"], r_c["result"]["launches"], lp_c)
            first_c = ppc["p_report"].read_bytes()
            r_c2, e_c2, _ = camp_run(rcc, camp_factory(rcc), resume=True)
            ppc["p_report"].rename(ppc["p_report"].with_name("moved-campaign.json"))
            r_c3, e_c3, _ = camp_run(rcc, camp_factory(rcc), resume=True)
            _rc, how_c = write_report(unit, rcc, gate="campaign")
            ok_c = (ok_c and r_c2 is None and isinstance(e_c2, StageRefusal) and "p's report exists" in str(e_c2)
                    and r_c3 is None and isinstance(e_c3, StageRefusal) and "records the campaign's end" in str(e_c3)
                    and ppc["p_report"].read_bytes() == first_c)
        restored_c = (m_corr._eligible_m, m_keys.arm_key, m_stages.DEFAULT_OUT, m_schedule.verify_schedule_dir,
                      m_resume.IDENTITY_KEYS_OLMO, m_resume.Identity) == m_attrs
        chk("stage: a full campaign on m's scripted OLMo double, its prior the unit's G-F0m-OLMo (p) in the same "
            "scratch root -- m's run_campaign under entries (1), (2), (6)-(9): COMPLETE at the floors (80 and 32 "
            "launched), p's report written with it (the read domain, every sham round attributed, m's report and "
            "adjudication excerpt named); a later --resume refused while p's report stands, and refused as ended once "
            "it is moved away; the report re-derived byte for byte; every m attribute restored",
            ok_c and restored_c, det_c)
        # a pause: shown, then adjudicated to COMPLETE; a PI stop on another
        echo8 = (lambda t, s, n, call: "{TOLD}" if t == a0s and s < 8 and n == 10 else None)
        rcp = qualified("camp-pause")
        r_p1, e_p1, out_p1 = camp_run(rcp, camp_factory(rcp, echo8))
        ppp = out_paths(unit, rcp, gate="campaign")
        n_after_p1 = len(m_ck(rcp)["sessions"]) if ppp["m_ckpt"].exists() else None
        files_after_p1 = (ppp["p_report"].exists(), ppp["p_stopped"].exists())
        r_p0, e_p0, _ = camp_run(rcp, camp_factory(rcp))
        r_ps, e_ps, _ = camp_run(rcp, camp_factory(rcp), resume=True)
        n_after_show = len(m_ck(rcp)["sessions"]) if ppp["m_ckpt"].exists() else None
        r_pa, e_pa, out_pa = camp_run(rcp, camp_factory(rcp), resume=True,
                                      adjudication="The seat rules the look's pause.")
        ev_p, _lp = read_calls(ppp["p_calls"])
        ends_p = [e.get("status") for e in ev_p if e.get("event") == "end"]
        ck_p = m_ck(rcp)
        chk("stage: a campaign whose first look fires (eight sham rounds echo the TOLD line) PAUSEs -- no p report, no "
            "STOP marker; a later run without --resume is refused; with --resume and no ruling it is shown its pause "
            "and launches nothing; with the seat's adjudication it resumes to COMPLETE, p's report then written; the "
            "call log's end lines PAUSE, PAUSE, COMPLETE",
            e_p1 is None and r_p1 is not None and r_p1["status"] == "PAUSE" and r_p1["report"] is None
            and files_after_p1 == (False, False) and not ppp["p_stopped"].exists()
            and r_p0 is None and isinstance(e_p0, StageRefusal) and "a later run is a --resume" in str(e_p0)
            and e_ps is None and r_ps["status"] == "PAUSE" and r_ps["report"] is None and n_after_show == n_after_p1
            and e_pa is None and r_pa["status"] == "COMPLETE" and r_pa["report"] is not None
            and ppp["p_report"].exists() and ends_p == ["PAUSE", "PAUSE", "COMPLETE"]
            and ((ck_p.get("campaign") or {}).get("pauses") or [{}])[0].get("adjudication")
            == "The seat rules the look's pause."
            and any(ln.startswith("RULING campaign-OLMo-sft (p): the seat's adjudication (sha16 ")
                    and ln.endswith("the campaign's last pause: look at 40 launches, open") for ln in out_pa.splitlines())
            and "The seat rules" not in out_pa,
            (ends_p, n_after_p1, n_after_show, r_p1 and r_p1["status"], r_ps and r_ps["status"],
             r_pa and r_pa["status"], ((ck_p.get("campaign") or {}).get("pauses") or [])[:1], e_p1, e_ps, e_pa,
             str(e_p0)[:60]))
        rcs = qualified("camp-pistop")
        camp_run(rcs, camp_factory(rcs, echo8))
        r_pi, e_pi, _ = camp_run(rcs, camp_factory(rcs), resume=True, pi_stop="The PI stops the campaign.")
        chk("stage: a paused campaign ended by the PI's stop is PI-STOP (terminal), p's report written with it",
            e_pi is None and r_pi is not None and r_pi["status"] == "PI-STOP" and r_pi["report"]["status"] == "PI-STOP"
            and ((m_ck(rcs).get("campaign") or {}).get("terminal") or {}).get("status") == "PI-STOP",
            (e_pi, r_pi and r_pi["status"]))
        # p's STOP in the campaign: the proxy's trigger; the marker under the campaign's name; a later run refused
        rcx = qualified("camp-stop")
        r_x, e_x, _ = camp_run(rcx, camp_factory(rcx, lambda t, s, n, call: "zebra\n\nx" if t == a0 and s == 0
                                                 and n == 6 else None))
        x_calls: list = []
        r_x2, e_x2, _ = camp_run(rcx, camp_factory(rcx, calls=x_calls), resume=True)
        ppx = out_paths(unit, rcx, gate="campaign")
        chk("stage: a campaign STOPPED by p's proxy (a line break in a stored text) leaves its marker under the "
            "campaign's name and no report; a later run is refused before the factory is called",
            r_x is None and isinstance(e_x, SystemExit) and stop_in(e_x) and ppx["p_stopped"].exists()
            and ppx["p_stopped"].name == "OLMo-sft_campaign_p-STOPPED.json" and not ppx["p_report"].exists()
            and r_x2 is None and isinstance(e_x2, StageRefusal) and x_calls == [], (e_x, e_x2, x_calls))
        # refusals before the load: no qualification; an unset cap
        rcn = root("camp-noprior")
        n_calls: list = []
        r_n, e_n, _ = camp_run(rcn, camp_factory(rcn, calls=n_calls))
        rcq = qualified("camp-nocap")
        q_calls: list = []
        r_q, e_q, _ = camp_run(rcq, camp_factory(rcq, calls=q_calls), cap_h=None)
        chk("stage: a campaign with no qualification in its root, or with no hour cap, is refused before the load -- "
            "the factory never called, nothing recorded",
            r_n is None and isinstance(e_n, StageRefusal) and "the qualification" in str(e_n) and n_calls == []
            and not out_paths(unit, rcn, gate="campaign")["p_calls"].exists()
            and r_q is None and isinstance(e_q, StageRefusal) and "hour cap is not set" in str(e_q) and q_calls == [],
            (e_n, e_q))
        # the values reach m's stage as declared (a recorder in m's place)
        rcr = qualified("camp-recorder")
        seen: dict = {}

        def recorder(adapter, **kw):
            seen.update(kw)
            return {"status": "PAUSE"}
        with mock.patch.object(m_stages, "run_campaign", recorder):
            r_r, e_r, _ = camp_run(rcr, camp_factory(rcr), cap_h=37)
        marked_r = out_paths(unit, rcr, gate="campaign")["p_stopped"].exists()
        rcu_ = qualified("camp-recorder-unreadable")

        def recorder_bad(adapter, **kw):
            pth = out_paths(unit, rcu_, gate="campaign")["m_ckpt"]
            pth.parent.mkdir(parents=True, exist_ok=True)
            pth.write_text("{not json", encoding="utf-8")
            return {"status": "COMPLETE"}
        with mock.patch.object(m_stages, "run_campaign", recorder_bad):
            r_u, e_u, _ = camp_run(rcu_, camp_factory(rcu_))
        marked_u = out_paths(unit, rcu_, gate="campaign")["p_stopped"].exists()
        chk("stage: run_campaign passes m's stage the unit's floors, launch counts and hour cap, the qualification's "
            "checkpoint as its prior, the substrate olmo, the root and the rulings (a recorder in m's place); a return "
            "that leaves the checkpoint neither open nor ended (absent: the recorder writes none; unreadable: it writes "
            "garbage) is a STOP inside the recorded run, its marker written, never a silent end (rounds 1-2's "
            "NOTE-1/A)",
            r_r is None and isinstance(e_r, StageStop) and "neither open nor ended" in str(e_r) and marked_r
            and r_u is None and isinstance(e_u, StageStop) and "'unreadable'" in str(e_u) and marked_u
            and seen.get("floors") == {a0: 80, a0s: 32} and seen.get("launch_counts") == {a0: 96, a0s: 64}
            and seen.get("hour_cap") == 37
            and Path(seen.get("prior_ckpt")).resolve() == out_paths(unit, rcr, gate="qual")["m_ckpt"].resolve()
            and seen.get("substrate") == "olmo" and Path(seen.get("out_root")).resolve() == rcr.resolve()
            and seen.get("adjudication") is None
            and seen.get("pi_stop") is None and seen.get("unit") == unit, (e_r, {k: str(v)[:40] for k, v in seen.items()}))
        # round 1's MAJOR-1: a terminal end whose end look fires is m's PAUSE -- p's report records it, terminal beside
        rce = qualified("camp-endlook")
        real_look = m_stages.campaign_look

        def end_fires(u, records, look):
            r_ = real_look(u, records, look)
            if look == "end":
                r_ = dict(r_, fired=True, results=[dict(x, fired=(i == 0)) for i, x in enumerate(r_["results"])])
            return r_
        with mock.patch.object(m_stages, "campaign_look", end_fires):
            r_e, e_e, _ = camp_run(rce, camp_factory(rce))
        ppe = out_paths(unit, rce, gate="campaign")
        rep_e = json.loads(ppe["p_report"].read_text(encoding="utf-8")) if ppe["p_report"].exists() else {}
        camp_e = m_ck(rce).get("campaign") or {}
        last_e = (camp_e.get("pauses") or [{}])[-1]
        r_e2, e_e2, _ = camp_run(rce, camp_factory(rce), resume=True)
        chk("stage: a campaign that ends COMPLETE with its end look firing (m:330) is m's PAUSE, the terminal standing -- "
            "the run's status PAUSE, p's report written with status PAUSE and the terminal COMPLETE beside it, so the "
            "run and campaign-report exit 3 as m's run does; a later run is refused (the campaign review's MAJOR-1)",
            e_e is None and r_e is not None and r_e["status"] == "PAUSE" and rep_e.get("status") == "PAUSE"
            and rep_e.get("campaign_terminal") == "COMPLETE" and m_stages.EXIT_CODES[rep_e.get("status")] == 3
            and (camp_e.get("terminal") or {}).get("status") == "COMPLETE" and last_e.get("kind") == "end_look"
            and last_e.get("adjudication") is None
            and r_e2 is None and isinstance(e_e2, StageRefusal) and "p's report exists" in str(e_e2),
            (e_e, r_e and r_e["status"], rep_e.get("status"), rep_e.get("campaign_terminal"), last_e.get("kind"), e_e2))
        # round 2's MINOR-B: m's own STOP (a G-VER failure: a record edited after the runner returns); its status STOP,
        # never PAUSE, even where the end look fires at the STOP point (C9(ii)), and no p marker (m's STOP is not p's)
        real_run_olmo = m_stages.run_session_olmo

        def tampered(adapter, sc, audit_, ban_ids, **kw):
            rec_ = real_run_olmo(adapter, sc, audit_, ban_ids, **kw)
            if sc.template == a0s and sc.s == 3:
                rec_["rounds"][0]["text"] += " x"
            return rec_
        mstop = {}
        for k_, look_patch in (("plain", None), ("end_look", end_fires)):
            r_m = qualified(f"camp-mstop-{k_}")
            with contextlib.ExitStack() as es_:
                es_.enter_context(mock.patch.object(m_stages, "run_session_olmo", tampered))
                if look_patch is not None:
                    es_.enter_context(mock.patch.object(m_stages, "campaign_look", look_patch))
                rr_, ee_, _ = camp_run(r_m, camp_factory(r_m))
            pm_ = out_paths(unit, r_m, gate="campaign")
            rp_ = json.loads(pm_["p_report"].read_text(encoding="utf-8")) if pm_["p_report"].exists() else {}
            lp_ = ((m_ck(r_m).get("campaign") or {}).get("pauses") or [{}])[-1]
            mstop[k_] = (ee_ is None and rr_ is not None and rr_["status"] == "STOP" and rp_.get("status") == "STOP"
                         and "campaign_terminal" not in rp_ and not pm_["p_stopped"].exists(), lp_.get("kind"))
        chk("stage: a campaign ended by m's own STOP (G-VER) is recorded STOP -- p's report written with it, no terminal "
            "beside it, no p marker -- and stays STOP where the end look fires at the STOP point (its end_look pause "
            "recorded by m; round 2's MINOR-B)",
            mstop == {"plain": (True, None), "end_look": (True, "end_look")}, mstop)
        # round 1's MINOR-1: run_gate runs the gates only
        g_calls: list = []
        rg_ = qualified("camp-rungate")
        m_scaffold._of_record.cache_clear()
        try:
            with hour_cap(40), olmo_stub_startup(), pod(), contextlib.redirect_stdout(io.StringIO()):
                run_gate(unit, "campaign", camp_factory(rg_, calls=g_calls), stub=True, out_root=rg_)
            rg_out = "ran"
        except StageRefusal as e:
            rg_out = "refused" if "run_gate runs p's gates" in str(e) else f"other: {e}"
        except (SystemExit, Exception) as e:
            rg_out = f"raised {type(e).__name__}: {e}"
        chk("stage: run_gate refuses the campaign before anything -- the factory never called, no call log written "
            "(the campaign review's MINOR-1)",
            rg_out == "refused" and g_calls == [] and not out_paths(unit, rg_, gate="campaign")["p_calls"].exists(),
            rg_out)
        # round 1's MINOR-4: the campaign's own refusals, each before the factory is called, on a paused campaign
        rcf = qualified("camp-refusals")
        camp_run(rcf, camp_factory(rcf, echo8))
        ppf = out_paths(unit, rcf, gate="campaign")
        ck_orig = ppf["m_ckpt"].read_bytes() if ppf["m_ckpt"].exists() else b"{}"
        outcomes: dict = {}

        def doctored(edit):
            try:
                ck_ = json.loads(ck_orig)
                edit(ck_)
                ppf["m_ckpt"].write_text(json.dumps(ck_), encoding="utf-8")
            except (KeyError, IndexError, TypeError, ValueError, OSError):
                pass                                # the case then fails on its own outcome, never aborting the rest

        def refused_before(name_: str, **kw):
            calls_: list = []
            r_, e_, o_ = camp_run(rcf, camp_factory(rcf, calls=calls_), resume=True, **kw)
            outcomes[name_] = (r_ is None and isinstance(e_, StageRefusal) and calls_ == [] and "RULING" not in o_,
                               str(e_)[:160])
        doctored(lambda c: c["campaign"]["pauses"][-1].__setitem__("adjudication", "X"))
        refused_before("no_pause", adjudication="Y")
        doctored(lambda c: c["campaign"].__setitem__("pauses", [
            dict(c["campaign"]["pauses"][-1], adjudication="R1"), dict(c["campaign"]["pauses"][-1], at_launches=80)]))
        refused_before("reused", adjudication=" R1 ")
        doctored(lambda c: c["campaign"].__setitem__("pi_stop", "stop one"))
        refused_before("mismatch", pi_stop="stop two")
        ppf["m_ckpt"].write_text("{not json", encoding="utf-8")
        refused_before("unreadable")
        ppf["m_ckpt"].write_bytes(ck_orig)
        scheds_ = sorted((rcf / "schedules").glob("*.json"))
        if scheds_:
            sched_orig = scheds_[0].read_bytes()
            scheds_[0].write_text("{}", encoding="utf-8")
            refused_before("schedules", adjudication="A ruling for the open pause.")
            scheds_[0].write_bytes(sched_orig)
        ppf["p_stopped"].write_text("{}", encoding="utf-8")
        refused_before("marker")
        ppf["p_stopped"].unlink()
        log_orig = ppf["p_calls"].read_bytes() if ppf["p_calls"].exists() else b""
        with open(ppf["p_calls"], "ab") as fh:
            fh.write((json.dumps({"event": "run", "schema": CALLS_SCHEMA, "run": 2, "resume": True,
                                  "stage": label(unit, "campaign"), "unit": unit}) + "\n").encode("ascii"))
            fh.write((json.dumps({"event": "end", "run": 2, "outcome": "exception",
                                  "exception": {"type": "StageStop", "message": "self-test", "stop": True}})
                      + "\n").encode("ascii"))
        refused_before("stop_line")
        ppf["p_calls"].write_bytes(log_orig)
        want_ref = {"no_pause": "NO PAUSE TO ADJUDICATE", "reused": "RULING REUSED", "mismatch": "CHECKPOINT MISMATCH",
                    "unreadable": "unreadable as a campaign's", "schedules": "are not clean",
                    "marker": "is STOPPED", "stop_line": "ended in a STOP"}
        chk("stage: on a paused campaign each of its own refusals stands before the load, the factory never called and "
            "no RULING line printed -- an adjudication with no open pause, an earlier pause's ruling offered again, a PI "
            "stop other than the one recorded, an unreadable checkpoint, unclean schedules (a fitting ruling offered: "
            "the RULING line waits for the load), a STOP marker with no STOP line, and a STOP line with no marker (each "
            "guard apart; the campaign review's MINOR-4, round 2's MINOR-A)",
            set(outcomes) == set(want_ref) and all(ok_ and want_ref[k] in msg for k, (ok_, msg) in outcomes.items()),
            {k: (ok_, msg[:70]) for k, (ok_, msg) in outcomes.items()})
        # round 3's NOTE-1: the RULING line beside an end pending -- the PI's stop offered again with the recorded text
        # is the one ruling that reaches the line there; the recorded run stood in for, so nothing loads or runs
        rec_runs: list = []

        def no_run(*a, **kw):
            rec_runs.append(a[1] if len(a) > 1 else kw.get("stage"))
            raise StageRefusal("SELFTEST: the recorded run stood in for (round 3's NOTE-1)")
        doctored(lambda c: (c["campaign"].__setitem__("pi_stop", "stop one"),
                            c.__setitem__(m_resume.END_PENDING, {"status": "PI-STOP"})))
        calls_pend: list = []
        with mock.patch.object(sys.modules[__name__], "_run_recorded", no_run):
            r_pend, e_pend, o_pend = camp_run(rcf, camp_factory(rcf, calls=calls_pend), resume=True,
                                              pi_stop="stop one")
        ppf["m_ckpt"].write_bytes(ck_orig)
        want_pend = (f"RULING {label(unit, 'campaign')}: the PI's stop (sha16 {m_stages._sha16_text('stop one')}); the "
                     f"campaign carries an end pending, which the stage re-finishes first")
        chk("stage: beside an end pending the RULING line names it -- the PI's stop offered again with the recorded "
            "text, the one ruling that reaches the line there, printed as its sha16 with the end pending, just before "
            "the recorded run (stood in for: the factory never called) (round 3's NOTE-1)",
            want_pend in o_pend and r_pend is None and isinstance(e_pend, StageRefusal) and "stood in for" in str(e_pend)
            and rec_runs == ["campaign"] and calls_pend == [],
            (o_pend[-240:], rec_runs, str(e_pend)[:100], calls_pend))
        with tempfile.TemporaryDirectory(prefix="p_stage_cstate2_") as td_s2:
            ts2 = Path(td_s2)

            def ck_file2(name: str, obj) -> Path:
                f = ts2 / name
                f.write_text(json.dumps(obj), encoding="utf-8")
                return f
            sess2 = [{"template": a0}]
            f_pi2 = ck_file2("pi.json", {"sessions": sess2, "campaign": {"pauses": [], "pi_stop": "stop one"}})
            f_pendpi = ck_file2("pendpi.json", {"sessions": sess2, "campaign": {"pauses": [], "pi_stop": "stop one"},
                                                m_resume.END_PENDING: {"status": "PI-STOP"}})
            f_exh2 = ck_file2("exh.json", {"sessions": sess2, "campaign": {"pauses": [
                {"kind": "schedule_exhausted", "at_launches": 90, "adjudication": None, "arm": a0s}]}})
            rpr2 = {"stripped_same_stop": campaign_ruling_problems(f_pi2, unit, None, " stop one\n"),
                    "recorded_stop_beside_pending": campaign_ruling_problems(f_pendpi, unit, None, "stop one"),
                    "exhausted_with_stop": campaign_ruling_problems(f_exh2, unit, "a ruling", "stop")}
        chk("stage: campaign_ruling_problems as m's driver words it on the three branches round 1 found untested -- the "
            "recorded PI stop compared stripped; the recorded stop offered beside an end pending (the stage re-finishes, "
            "no refusal); an adjudication on an exhausted schedule beside the PI's stop (the stop ends it, no refusal)",
            rpr2 == {"stripped_same_stop": [], "recorded_stop_beside_pending": [], "exhausted_with_stop": []}, rpr2)
        # the non-stub precheck at the campaign binds G-PWR (p)'s record and the lock's campaign lines (sentinels)
        me_st = sys.modules[__name__]
        real_committed = m_stages._committed

        def committed_lock(rel, *a, **kw):
            if rel == lock_rel(unit):
                return [], b"LOCK-p stand-in for the self-test\nBACKEND OF RECORD 641ee466f4553b6a\n"
            return real_committed(rel, *a, **kw)
        with hour_cap(40), mock.patch.object(me_st, "gpwr_problems", lambda u: (["GPWR-SENTINEL"], "f" * 64)), \
                mock.patch.object(me_st, "campaign_lock_problems", lambda u, t: ["LOCKLINE-SENTINEL"]), \
                mock.patch.object(m_stages, "_committed", committed_lock):
            try:
                precheck(unit, stub=False, gate="campaign")
                pc_ = "ran"
            except StageRefusal as e:
                pc_ = str(e)
            except SystemExit as e:
                pc_ = f"other: {e}"

        def committed_gpwr(doc):
            def f_(rel, *a, **kw):
                if rel == GPWR_REL:
                    return [], json.dumps(doc).encode("utf-8")
                return real_committed(rel, *a, **kw)
            return f_
        good = json.loads(real_committed(GPWR_REL)[1].decode("utf-8"))
        bad_schema = dict(good, schema="p-gpwr-v0")
        bad_sham = json.loads(json.dumps(good))
        bad_sham["units"][unit]["launch"]["L"]["A0s"] = 60
        gps = {}
        for k_, doc_ in (("good", good), ("schema", bad_schema), ("sham", bad_sham)):
            with mock.patch.object(m_stages, "_committed", committed_gpwr(doc_)):
                gps[k_] = gpwr_problems(unit)
        chk("stage: the non-stub precheck at the campaign carries G-PWR (p)'s problems and the lock's campaign-line "
            "problems among its refusals and requires the lock to name G-PWR (p)'s record (sentinels in their place); "
            "gpwr_problems refuses a record of another schema and a sham launch count other than this build's",
            "GPWR-SENTINEL" in pc_ and "LOCKLINE-SENTINEL" in pc_ and "does not name G-PWR (p)'s record" in pc_
            and gps["good"][0] == [] and gps["good"][1] is not None
            and any("schema" in x for x in gps["schema"][0]) and any("launch counts" in x for x in gps["sham"][0]),
            (pc_[:200], gps["schema"][0], gps["sham"][0]))
        # FLAG (j)'s fix: the drift check's import closure, from a fresh interpreter
        from . import gshape as p_gshape
        phantom = type(sys)("valence_core.p_selftest_phantom")
        phantom.__file__ = str(REPO / "valence_core" / "e2d" / "habit.py")
        fp1, fc1 = fresh_import_closure()
        sys.modules[phantom.__name__] = phantom
        try:
            fp2, fc2 = fresh_import_closure()
            _ip, inproc = p_gshape.import_closure(committed=False)
        finally:
            sys.modules.pop(phantom.__name__, None)
        moved = dict(list(fc1.items())[1:])
        chk("stage: FLAG (j)'s fix -- the drift check's import closure comes from a fresh interpreter importing p's "
            "driver, never from the calling process: a module planted in this process's sys.modules reaches gshape's "
            "in-process closure (the hazard) and not the fresh one, the same on both calls; no p or m file is in it; a "
            "recorded closure that differs from it is stale",
            fp1 == [] and fp2 == [] and fc1 == fc2 and len(fc1) > 0
            and "valence_core/e2d/habit.py" in inproc and "valence_core/e2d/habit.py" not in fc2
            and not any(k.startswith(("valence_core/p/", "valence_core/m/")) for k in fc2)
            and _drift("G-SHAPE-p.json", "import closure", (fp2, fc2), dict(fc1)) == []
            and len(_drift("G-SHAPE-p.json", "import closure", (fp2, fc2), moved)) == 1,
            (fp1, fp2, len(fc1), len(fc2)))
        fails = {}
        for tag, exe in (("exit-1", "/usr/bin/false"), ("not-json", "/bin/echo"),
                         ("no-binary", str(Path(tempfile.gettempdir()) / "p-selftest-no-such-python"))):
            with mock.patch.object(sys, "executable", exe):
                fails[tag] = fresh_import_closure()
        to_calls: list = []

        def run_times_out(cmd, **kw):
            to_calls.append(kw.get("timeout"))
            raise subprocess.TimeoutExpired(cmd, kw.get("timeout"))
        with mock.patch.object(subprocess, "run", run_times_out):
            fails["timeout"] = fresh_import_closure()
        with mock.patch.object(subprocess, "run", lambda cmd, **kw: subprocess.CompletedProcess(
                cmd, 0, stdout=json.dumps([["valence_core.p_selftest_outside", "/etc/hosts"]]), stderr="")):
            outside = fresh_import_closure()
        seen_fc: list = []
        real_fic = fresh_import_closure
        g_["fresh_import_closure"] = lambda: (seen_fc.append(1), ([], dict(fc1)))[1]
        try:
            dp_ = gshape_drift_problems("G-SHAPE-p.json", {"sources": {}, "import_closure": dict(fc1)})
        finally:
            g_["fresh_import_closure"] = real_fic
        rec_code = (_CLOSURE_CODE.replace("print(json.dumps(", "from valence_core.p import gshape as _g\n"
                                          "_g.inputs_of_record(canonical=False)\n"
                                          "print(json.dumps(sorted(_g.import_closure(committed=False)[1])))\n"
                                          "_unused = ((", 1))
        rr_ = subprocess.run([sys.executable, "-I", "-B", "-c", rec_code, str(REPO)], capture_output=True, text=True,
                             cwd=str(REPO), timeout=CLOSURE_TIMEOUT_S)
        try:
            rec_keys = json.loads(rr_.stdout.strip().splitlines()[-1])
        except (ValueError, IndexError):
            rec_keys = None
        chk("stage: FLAG (j)'s fix, its edges (the qual review's N-3, N-7 (d), R2-2 (c)) -- a child that exits 1, prints "
            "no JSON, cannot start, or runs past the bound (the bound passed and named) is each a named problem with an "
            "empty closure, and a module file outside the repository is named too (fail-closed); the drift check takes "
            "its closure from fresh_import_closure; the fresh closure's files are those G-SHAPE-p's own run records (its "
            "in-process closure after inputs_of_record, computed in a fresh process)",
            all(bool(p_) and c_ == {} for p_, c_ in fails.values()) and "could not run" in fails["no-binary"][0][0]
            and "failed" in fails["exit-1"][0][0] and "not JSON" in fails["not-json"][0][0]
            and f"TimeoutExpired: timed out after {CLOSURE_TIMEOUT_S} s" in fails["timeout"][0][0]
            and to_calls == [CLOSURE_TIMEOUT_S] and any("not a regular file in the repo" in x for x in outside[0])
            and outside[1] == {}
            and seen_fc == [1] and not any("import closure" in x for x in dp_)
            and rec_keys == sorted(fc1), ({k: v[0][:1] for k, v in fails.items()}, seen_fc, rec_keys and len(rec_keys),
                                          (rr_.stderr or "")[-200:]))
        ign = {}
        for rel in [f"data/p/ckpt/{u}_{g}_p-calls.jsonl" for u in UNITS for g in STAGES] + [
                f"data/p/ckpt/{u}_{g}_p-STOPPED.json" for u in UNITS for g in STAGES] + [
                f"data/p/reports/{u}_{g}_p-report.json" for u in UNITS for g in STAGES] + [
                f"data/p/ckpt/{u}_campaign.json" for u in UNITS] + [
                f"data/p/ckpt/{u}_campaign_adjudication.json" for u in UNITS] + [
                f"data/p/reports/{u}_campaign_report.json" for u in UNITS] + [report.LEXICON_REL]:
            ign[rel] = subprocess.run(["git", "-C", str(REPO), "check-ignore", "-q", rel], capture_output=True).returncode
        lock_ign = {rel: subprocess.run(["git", "-C", str(REPO), "check-ignore", "-q", rel],
                                        capture_output=True).returncode
                    for rel in [f"data/p/ckpt/{u}_{g}_p.lock" for u in UNITS for g in STAGES]
                    + [f"data/p/ckpt/{u}_{g}_p-STOPPED.json.reserve-1" for u in UNITS for g in STAGES]}
        chk("stage: git admits every output p's stages write -- the nine call logs, the nine STOP markers, the nine "
            "reports, m's three campaign checkpoints, adjudication excerpts and reports -- and the lexicon, and ignores "
            "the nine lock files and the STOP reservations (git check-ignore exits 1, then 0, for each; round 2's M-2; "
            "ledger 27; the campaign review's NOTE-5)",
            set(ign.values()) == {1} and set(lock_ign.values()) == {0}, (ign, lock_ign))
        sess = [{"template": "T", "s": 0, "contrast": False,
                 "rounds": [{"phase": "forced", "ri": 0, "seed": 7, "text": "a"},
                            {"phase": "forced", "ri": 1, "seed": 7, "text": "b"}]}]
        att = attribute_calls(sess, [{"event": "call", "seed": 7, "text_sha256": text_sha256("a")}])
        chk("stage: two recorded rounds sharing a seed attribute neither (never a guess)",
            att["by_round"] == {} and att["problems"] and len(att["missing"]) == 2, att)
    finally:
        shutil.rmtree(tdir, ignore_errors=True)
