#!/usr/bin/env python3
"""PROPOSAL-m Q-F3 driver (v1.11 §3.2 m:288-298, §8 step 19 m:361; ADDENDUM-m1 §4 step 5; the design seat's
prebuild answers of 2026-11-06, Q1 (C2) and Q6).

Q-F3's own driver (Q1: "A new driver, scripts/mf3_sessions.py"; scripts/m_sessions.py is untouched). It wires:

  --selftest          every valence_core.mf3 module's model-free self-test, then this driver's integration
                      checks; "  N/N mf3 selftest checks pass", exit 0 iff all pass.
  --build-schedules   Q-F3's schedule files and manifest (default data/mf3/schedules; --out a test
                      directory); an existing differing file is refused, never overwritten.
  hashes              what LOCK-m-F3 v0.1 names (Q1 (C2)): mf3's package_sha256, each imported
                      valence_core.m module's file sha256, the schedules' manifest sha256, the weights
                      binding of record (the hub cache's snapshot; nothing loaded).
  gshape              G-SHAPE-F3 (m:290), model-free; the canonical artifact data/mf3/gates/G-SHAPE-F3.json
                      needs every source committed at HEAD and unedited; --out a test directory.
  time --proposal-file F --lock-file L --analyzer-sha256 H --package-sha256 H --renders-sha16 H [--resume]
                      G-TIME-F3 (m:293), its re-run under ADDENDUM-m2 v0.5 (§4.3): one session per Q-F3 arm
                      (6) on Qwen, uncached, the reasoning block F-b at the cap of record, 120, and no other
                      (A-m2 v0.5 §4.1-§4.2), into its own checkpoint data/mf3/ckpt/Q-F3_time-r2.json with its
                      report and reads named after it (the precheck refuses the first run's checkpoint name
                      as a target: that checkpoint is never written again), under LOCK-m-F3
                      v0.1 as re-issued (wired at its step, after the lock: lock §11 item 1). The flags are
                      the lock's values (lock §1, "How a stage cites this file"); m_module_sha256 and the
                      weights binding are read from the lock's committed text. Before the load: the identity
                      (refused on its own), then the precheck (the licence by file, the run-time known answers,
                      the renders, the committed schedules, the checkpoint, m:267's laptop checklist, the gate
                      line), the driver check and the snapshot check, refused together (exit 2); then the DRIVER
                      and SNAPSHOT lines. After
                      it: the snapshot re-read and the model id (a STOP, exit 4). Exit 0 PASS, 4 STOP.
  id --proposal-file F --lock-file L --analyzer-sha256 H --package-sha256 H --renders-sha16 H [--resume]
                      G-ID-F3 (m:295) on Qwen at the cap of record, 120: A2s then A3s, at each index uncached
                      then cached under the same keys (m-id|F3|{template}|{s}), until each template has a
                      complete pair; criterion 2/2 (stages.gid_decide), each pair's identity the seat's F-7
                      (stages._gid_pair). Its prior is G-TIME-F3's
                      re-run checkpoint, data/mf3/ckpt/Q-F3_time-r2.json, taken by path, the first run's
                      refused (A-m2 v0.5 §4.3); under LOCK-m-F3 v0.1 as re-issued (wired at its step: the
                      seat's read of G-TIME-F3 r2, §5 item 1). The flags are time's, the identity time's with no
                      locked_path (the path is recorded at LOCK-m-F3 v0.2), and the order of the refusals, the
                      DRIVER and SNAPSHOT lines, the load and the re-read is time's; the precheck adds the
                      prior (stages.prior_gate, require_real on) and an existing G-ID artifact. It writes
                      data/mf3/ckpt/Q-F3_id.json, its report and reads, and the artifact at
                      guard.gid_artifact_path(), write-once. Exit 0 PASS, 5 FAIL, 6 NOT-DETERMINED, 4 STOP.
  qual --proposal-file F --lock-file L --analyzer-sha256 H --package-sha256 H --renders-sha16 H [--resume]
                      G-F3 (m:297) on Qwen at the cap of record, 120, uncached: 40 sessions, 8 each of A1s, A2s
                      and A3s (24 sham), 8 of A3, 4 of A1 and 4 of A2 (16 contrast), the counts the committed qual
                      schedules carry (QUAL_COUNTS), in the stage library's launch order; under LOCK-m-F3 v0.2,
                      whose committed text must carry its cap and path lines (QUAL_LOCK_LINES; an earlier blob is
                      refused); its identity time's (locked_path "uncached", G-ID-F3 having failed); its prior
                      G-TIME-F3's re-run checkpoint by path, the first run's refused (A-m2 v0.5 §4.3), with
                      G-ID-F3's artifact on disk at the cap (stages.prior_gate, require_real on). The order of the
                      refusals, the DRIVER and SNAPSHOT lines, the load and the re-read is time's. It writes
                      data/mf3/ckpt/Q-F3_qual.json, its report and reads. Exit 0 PASS, 4 STOP.
  campaign --proposal-file F --lock-file L --analyzer-sha256 H --package-sha256 H --renders-sha16 H [--resume]
           [--adjudication-file A] [--pi-stop-file P]
                      Q-F3's campaign (m:298, m:361; ADDENDUM-m1 §4 step 5) on Qwen at the cap of record, 120,
                      uncached, under LOCK-m-F3 v1.0 (wired at its step, after v1.0's commit: the seat's answers of
                      2026-11-15, §5 item 2), whose committed text must carry v0.2's cap and path lines at a line's
                      start (QUAL_LOCK_LINES) and v1.0's two lines as whole lines (CAMPAIGN_LOCK_LINES: "launch
                      counts = A1 128, A1s 64, A2 224, A2s 96, A3 224, A3s 96" and "hour cap = 480 h"; an earlier
                      blob is refused): the six arms interleaved by §2.1's rule until each arm's domain count
                      reaches its floor (schedule.FLOORS under the path: A1 80, A1s 32, A2 144, A2s 56, A3 144,
                      A3s 56), the hour cap (480 h) or the PI's stop, the launch counts the projection (m:192),
                      looks every 40 launches (m:330), through stages.run_campaign; its prior G-F3's checkpoint,
                      data/mf3/ckpt/Q-F3_qual.json, ended PASS (stages.prior_gate, require_real on), G-ID-F3's
                      artifact re-checked if on disk. --adjudication-file names the seat's ruling on the
                      campaign's unadjudicated pause (a look's; an exhausted schedule's only beside the PI's stop),
                      --pi-stop-file the PI's stop (each a UTF-8 file named for nothing it says, its path printed
                      on the INVOCATION line; each text recorded in the checkpoint only, never printed; a RULING
                      line before the load gives each text's sha16 and the pause it is offered for; the report
                      gives a pause's recorded ruling the same digest, and a later NO PAUSE TO ADJUDICATE refusal
                      names it). A campaign's exit 3 is one of three pauses: a look's, resumed only with --resume
                      and the seat's adjudication, or ended by the PI's stop (with --resume); an exhausted
                      schedule's, which only the PI's stop ends; or an end look's beside a terminal end
                      (COMPLETE, CAP, PI-STOP), never resumed -- its ruling enters VERDICTS as the analyzer's
                      declared --adjudication file. After an interrupted run that offered the seat's adjudication
                      alone, re-run with --resume alone: a recorded adjudication resumes the campaign, or
                      re-finishes an end its finish left pending; an unrecorded one shows the pause again; and
                      where that finish completed before the kill, the re-run shows the new pause, or is refused
                      as ended. After one that offered the PI's stop, re-run with --resume and the same ruling
                      files: a recorded stop is accepted again and the campaign ends PI-STOP, an unrecorded one is
                      applied, save where an end is left pending: a stop the checkpoint records re-finishes with
                      it, and a terminal end or a STOP stands; a ruling the stage would not apply beside it (the
                      seat's adjudication, or a PI stop the checkpoint does not record) is refused before the
                      load (RULING BESIDE AN END PENDING), the re-run drops the flags that refusal names, and
                      where the end is a look's or an exhausted schedule's pause a stop so refused is offered
                      again once the re-finish has shown it (VC4-1); should NO PAUSE TO ADJUDICATE then refuse an
                      adjudication offered with the stop, it was recorded -- drop --adjudication-file. An
                      adjudication is offered only for the pause it rules on, which the shown pause and the
                      RULING line name (its kind and launch count); one whose text is a ruling the checkpoint
                      records for an earlier pause is refused before the load (RULING REUSED: O1-3); an
                      adjudication the checkpoint already records is named as such on the RULING line (RM4-1)
                      where one prints, and otherwise by the pre-load refusal that meets it first. Beside an end
                      pending (a finish interrupted; the RULING line of an invocation that finds one says "beside
                      an end pending") the end is re-finished first, and a ruling the stage would not apply with
                      it is refused before the load (O4-1; where no precheck runs, the stage re-finishes the end
                      and then refuses it, NOT APPLIED, exit 4); so beside one no adjudication is offered, and the
                      PI's stop only where the checkpoint records it. An adjudication offered beside one is never
                      offered again, whatever NOT APPLIED's "offer it again" says (it holds for the PI's stop
                      alone): it rules on no pause shown when it was offered -- it is the previous pause's ruling,
                      already recorded, or one written before the pause it would rule on was shown (VC4-2; the
                      seat rules on a pause once shown). A re-finished pause that leaves the campaign open is then
                      shown and takes the seat's own ruling on it (a look's; an exhausted schedule's only beside
                      the PI's stop), or the PI's stop offered again. After a terminal end or a STOP that end
                      stands: a pause it carries takes the seat's own ruling on it, once shown, through VERDICTS
                      (the declared --adjudication file), and a PI's stop on a hair trigger the declared --pi-stop
                      record, as NOT APPLIED's message says; an adjudication the checkpoint already records needs
                      nothing. The order of the refusals, the DRIVER and SNAPSHOT lines, the load and the re-read
                      is time's, the RULING line after the SNAPSHOT line. It writes data/mf3/ckpt/Q-F3_campaign.json
                      and its report, with the adjudication excerpt beside the checkpoint when a pause or a STOP is
                      recorded. Exit 0 COMPLETE, CAP or PI-STOP, 3 PAUSE, 4 STOP.

Q6's forms (the seat: "scripts/mf3_sessions.py is written to the same forms from the start"): the
CHECKPOINT STATE INCONSISTENT line is valence_core.m.resume's sealed form, imported by mf3.resume; the
campaign-ruling refusals O4-1 (RULING BESIDE AN END PENDING), O1-3 (RULING REUSED), RM4-1's RULING-line note
and the VC4-1 / VC4-2 help and docstring sentences are the campaign subcommand's, written in
scripts/m_sessions.py's forms at the campaign wiring; O2-3's listing forms (a bare git status
--porcelain, a name-only ls, git ls-files, git diff --name-status, shasum; no size or time metadata of
data/mf3/ckpt or data/mf3/reports) go into Q-F3's launch checklist until its VERDICTS -- from 2026-11-10 the list
of record v2 (the seat's list ruling of that date, §2, which supersedes the sweeps ruling of 2026-11-09, §2), which
the re-issued LOCK-m-F3 v0.1 cites. The ADDENDUM-m2 smoke's ``time --smoke`` form (9c7062e) is retired at the
build of A-m2 v0.5 (§4.2): the smoke ran (6cfd3db) and no second smoke is declared. The rest of m's
pre-load check (the MLXLM_USE_MODELSCOPE and local-path refusals, the hub's own offline resolution, the
SNAPSHOT line, the post-load re-read with its model-id STOP) is the ``time`` wiring's (the routing of
2026-11-07: "Build at time"), in scripts/m_sessions.py's forms.

INVOCATION is the first line of every run. Nothing here loads a model except ``time``, ``id``, ``qual`` and
``campaign``, through ``_load_qwen``, after every pre-load refusal.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib
import io
import json
import os
import re
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from valence_core.mf3 import gshape, guard, keys, schedule, stages  # noqa: E402
from valence_core.mf3 import resume as rs  # noqa: E402

DRIVER_REL = "scripts/mf3_sessions.py"
#: Every mf3 module with a self-test, in dependency order (the test double has none).
MODULES = ("keys", "banner", "schedule", "lines", "scaffold", "guard", "runner", "verify", "readrule", "bars",
           "resume", "stages", "gshape")
STAGE_CMDS = ("time", "id", "qual", "campaign")
STAGE_NAMES = {"time": "G-TIME-F3", "id": "G-ID-F3", "qual": "G-F3", "campaign": "the Q-F3 campaign"}
# PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; the seat's F-1, carrying the step-10 read's Q2: "an edit … that wires a
# subcommand … does not re-run G-SHAPE-F0", here G-SHAPE-F3): ``time`` is wired for Q-F3 under LOCK-m-F3 v0.1
# (lock §11 item 1: "the `time` subcommand is wired in `scripts/mf3_sessions.py` at its step"), on the PI's routing
# of 2026-11-07, item 1 ("… → LOCK-m-F3 v0.1 → G-TIME-F3 [go]"). The edit touches no scoring-stack function. The
# new blob's sha256 is printed by the DRIVER line and recorded in the G-TIME-F3 entry and in LOCK-m-F3 v0.2 (the
# step-10 read's Q2 condition, which Code reads F-1's "with the same scope" as carrying; the routing of
# 2026-11-07). id, qual and campaign are wired at their own steps (the id, qual and campaign wirings' PINs, below).
WIRED_CMDS = ("time", "id", "qual", "campaign")
REFUSED_CMDS = tuple(c for c in STAGE_CMDS if c not in WIRED_CMDS)
# PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's TIME_* form carried, scripts/m_sessions.py): G-TIME-F3 cites
# LOCK-m-F3.md (lock §1); one session per Q-F3 arm (m:293: "One session per Q-F3 arm (6), as G-TIME-F0"), the
# counts the committed time schedules carry (n 1 each); locked_path "uncached" (m:293, "G-TIME-F3 (Qwen,
# uncached)"); reasoning cap 60 at the first run (m:174), 120 from the re-run on (A-m2 v0.5 §4.1; the PIN below).
# The five flags are the lock's values, as LOCK-m-F0 §0's "How a stage cites this file" made them for m's driver.
# The values are Q-F3's;
# TIME_REASONING_CAP and TIME_FLAG_HELP have no counterpart in m.
# PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.1-§4.3): the re-run of G-TIME-F3 runs at the cap of
# record, 120 (scaffold.CAP_OF_RECORD), and nothing else: time_identity_extra validates the identity as a run on a
# model (stages._extra, stub=False), which refuses any other TIME_REASONING_CAP. Its checkpoint is TIME_CKPT_NAME,
# data/mf3/ckpt/Q-F3_time-r2.json, its report and reads named after it (stages.for_checkpoint); time_checkpoint
# builds that path and refuses the first run's, FIRST_RUN_CKPT_NAME, as a target; the precheck refuses an existing
# or ended checkpoint there, and the stage is passed the same path. The stage library keeps m's default stem for the
# stub (A-m2 v0.5 §4.2), so the r2 path and the first run's refusal live here.
TIME_LOCK_FILE = "LOCK-m-F3.md"
TIME_FLAGS = ("proposal_file", "lock_file", "analyzer_sha256", "package_sha256", "renders_sha16")
TIME_COUNTS = tuple((t, 1) for t in keys.TEMPLATES)
TIME_LOCKED_PATH = "uncached"
TIME_REASONING_CAP = 120
TIME_CKPT_NAME = f"{keys.UNIT}_time-r2.json"
FIRST_RUN_CKPT_NAME = f"{keys.UNIT}_time.json"
TIME_FLAG_HELP = {"proposal_file": "the proposal of record (PROPOSAL-m-gating-campaign-v1_11.md)",
                  "lock_file": f"the lock ({TIME_LOCK_FILE})",
                  "analyzer_sha256": "the analyzer's sha256, as the lock names it",
                  "package_sha256": "mf3's package_sha256, as the lock names it",
                  "renders_sha16": "the renders' sha16, as the lock names it"}
# PIN (Code, declared at LOCK-m-F3 v0.2; the id wiring; m's run_id form carried, scripts/m_sessions.py): ``id`` is
# wired for Q-F3 under LOCK-m-F3 v0.1 as re-issued, at its step -- the seat's read of G-TIME-F3 r2, §5 item 1, routed
# by the PI on 2026-11-10 (its §8 item 4: "The `id` wiring (F-1's kind, named in its entry) → G-ID-F3 at 120 on the
# laptop"). G-ID-F3 (m:295): keys m-id|F3|{template}|{s}, A2s and A3s once each (keys.GID_TEMPLATES), criterion 2/2
# (stages.gid_decide; each pair's identity under the seat's F-7, stages._gid_pair), a divergence sending Q-F3
# uncached. Its identity carries time's five
# flags' values (the lock's, ID_LOCK_FILE) and no locked_path (the path is recorded at LOCK-m-F3 v0.2, lock §1); its
# reasoning cap is the cap of record, ID_REASONING_CAP (A-m2 v0.5 §4.1), the one prior_gate fixes with require_real
# on. Its prior is G-TIME-F3's re-run checkpoint, ID_PRIOR_CKPT_NAME, taken by path, the first run's name refused
# (A-m2 v0.5 §4.3: "the `id` and `qual` wirings take the re-run's checkpoint by path and refuse the first"; lock R4
# item 2). Its checkpoint, report and reads are m's default stem for "id" (stages.out_paths), its artifact
# guard.gid_artifact_path(), write-once. The edit is of F-1's kind: the new blob's sha256 is printed by the DRIVER
# line and recorded in the G-ID-F3 entry and in LOCK-m-F3 v0.2.
ID_LOCK_FILE = TIME_LOCK_FILE
ID_REASONING_CAP = 120
ID_PRIOR_CKPT_NAME = TIME_CKPT_NAME
# PIN (Code, declared at LOCK-m-F3 v1.0; the qual wiring; m's QUAL_* form carried, scripts/m_sessions.py): ``qual`` is
# wired for Q-F3 under LOCK-m-F3 v0.2, at its step -- the seat's read of G-ID-F3, §5 and §9 item 5, routed by the PI on
# 2026-11-11 ("After v0.2: the `qual` wiring → G-F3, 40 sessions uncached, announced and serialized, ≈ one laptop day →
# the seat's read [go]"). G-F3 (m:297): 40 sessions, 8 each of A1s, A2s and A3s (24 sham), 8 of A3, 4 of A1 and 4 of A2
# (16 contrast), keys m-f3|{template}|{s}; QUAL_COUNTS are those counts in §2.4's table order, the committed qual
# schedules' n (run_gate_stage refuses any other). It cites QUAL_LOCK_FILE, whose committed text must carry
# QUAL_LOCK_LINES as lines -- LOCK-m-F3 v0.2's cap and path lines (v0.2 §2, §3) -- so the re-issue's and v0.1's blobs are
# refused, as m's qual refused LOCK-m-F0 v0.1's (Code's intent, declared at LOCK-m-F3 v0.2 §9 item 1). Its identity is
# time's: the cap of record, QUAL_REASONING_CAP, and locked_path QUAL_LOCKED_PATH, "uncached" (v0.2 §3: G-ID-F3 FAIL),
# which stages._locked holds to the path the G-ID licence gives. Its prior is G-TIME-F3's re-run checkpoint by path,
# QUAL_PRIOR_CKPT_NAME, the first run's name refused (A-m2 v0.5 §4.3), as id's; stages.prior_gate (require_real on) also
# requires G-ID-F3's artifact on disk at the cap, any verdict. Its checkpoint, report and reads are m's default stem for
# "qual". The edit is of F-1's kind: the new blob's sha256 is printed by the DRIVER line and recorded in the G-F3 entry
# and in LOCK-m-F3 v1.0.
QUAL_LOCK_FILE = TIME_LOCK_FILE
QUAL_COUNTS = (("A1", 4), ("A1s", 8), ("A2", 4), ("A2s", 8), ("A3", 8), ("A3s", 8))
QUAL_LOCKED_PATH = "uncached"
QUAL_REASONING_CAP = 120
QUAL_LOCK_LINES = ("- **`reasoning_cap = 120`.**", "- **`path = uncached`.**")
QUAL_PRIOR_CKPT_NAME = TIME_CKPT_NAME
# PIN (Code, declared at the Q-F3 campaign wiring; m's CAMPAIGN_* form carried, scripts/m_sessions.py): ``campaign`` is
# wired for Q-F3 under LOCK-m-F3 v1.0, at its step -- the seat's answers of 2026-11-15, §5 item 2, routed by the PI on
# 2026-11-15 ("Route as given"; section A item 6: "After v1.0's commit: the campaign wiring (F-1's kind; its entry names
# the edit and the new DRIVER blob and notes that v1.0 §6's value is the driver at the lock; NOTE-7's gap closed;
# G-SHAPE-F3 not re-run)"). The campaign (m:298, m:361): the six arms interleaved by §2.1's rule, uncached, at the cap
# of record, until each arm's domain count reaches its floor, the hour cap or the PI's stop (stages.run_campaign). Its
# values are LOCK-m-F3 v1.0's (m:286, by m:298's "as §3.1"): CAMPAIGN_LAUNCH_COUNTS, v1.0 §1's launch counts from
# G-PWR (Q-F3)'s record, "a projection, not a bound" (m:192), and CAMPAIGN_HOUR_CAP, v1.0 §2's, the PI's cap in hours,
# each passed to stages.run_campaign as given here. CAMPAIGN_LOCK_LINES is v1.0 §1's and §2's line forms, built from
# these two values, which stage_identity_extra requires as whole lines of the governing lock's committed text (the
# seat's answers of 2026-11-15, §2 (a): "the campaign wiring tests them as lines (the `qual` wiring's line test, not
# m's substring test)"), beside QUAL_LOCK_LINES at a line's start (v0.2's cap and path lines, which v1.0 carries): so
# the values the run passes are the values whose lines the governing lock carries, and a line that only begins with
# one of them (other counts, "480 hours") is refused. Its identity is G-F3's: CAMPAIGN_REASONING_CAP, the cap of record,
# and CAMPAIGN_LOCKED_PATH, "uncached" (v0.2 §3). Its floors are §2.4's under that path (m:184-186) as mf3's
# schedule.FLOORS carries them, read by ``campaign_floors`` -- one source, the package the lock's package_sha256 pins.
# Its prior is G-F3's checkpoint at the same out root, CAMPAIGN_PRIOR_CKPT_NAME, taken by path (stage_prior_checkpoint;
# stages.PRIOR_STAGE["campaign"] is "qual"), ended PASS (stages.prior_gate, require_real on). Its checkpoint and report
# are m's default stem for "campaign" (stages.out_paths), with the adjudication excerpt the stage writes beside the
# checkpoint. The edit is of F-1's kind: the new blob's sha256 is printed by the DRIVER line and recorded in the
# campaign wiring's entry; LOCK-m-F3 v1.0 §6 names the driver at the lock (the unit's convention since the time
# wiring).
CAMPAIGN_LOCK_FILE = TIME_LOCK_FILE
CAMPAIGN_LAUNCH_COUNTS = (("A1", 128), ("A1s", 64), ("A2", 224), ("A2s", 96), ("A3", 224), ("A3s", 96))
CAMPAIGN_HOUR_CAP = 480
CAMPAIGN_LOCK_LINES = ("launch counts = " + ", ".join(f"{t} {n}" for t, n in CAMPAIGN_LAUNCH_COUNTS),
                       f"hour cap = {CAMPAIGN_HOUR_CAP} h")
CAMPAIGN_LOCKED_PATH = "uncached"
CAMPAIGN_REASONING_CAP = 120
CAMPAIGN_PRIOR_CKPT_NAME = f"{keys.UNIT}_qual.json"
# PIN (Code, declared at the Q-F3 campaign wiring; m's camp_pauses carried, with VC4-1 and the review's missed item):
# the campaign subcommand's help and description name its pauses and the re-run guidance in m's words, verbatim (the
# declared --adjudication file and its C9(i) are m_analyze.py's, the analyzer Q-F3 runs: stages.ANALYZER_PATH); the
# self-test compares the text with m's camp_pauses, read from scripts/m_sessions.py.
CAMPAIGN_PAUSES = ("exit 3 is one of three pauses: a fired look's, resumed with --resume and the seat's adjudication "
                   "(--adjudication-file) or ended by the PI's stop (--pi-stop-file, with --resume); an exhausted "
                   "schedule's, which only the PI's stop ends; an end look's beside a terminal end (COMPLETE, CAP, "
                   "PI-STOP), never resumed -- its ruling enters VERDICTS as the analyzer's declared --adjudication "
                   "file (C9(i)). After an interrupted run that offered the seat's adjudication alone, re-run with "
                   "--resume alone: recorded, it resumes the campaign or re-finishes an end its finish left pending; "
                   "unrecorded, the pause is shown again; and where that finish completed before the kill, the re-run "
                   "shows the new pause, or is refused as ended. After one that offered the PI's stop, re-run with "
                   "--resume and the same ruling files: recorded or not, the campaign ends PI-STOP, save where an end "
                   "is left pending -- a stop the checkpoint records re-finishes with it, and a terminal end or a STOP "
                   "stands; a ruling the stage would not apply beside it (the seat's adjudication, or a PI stop the "
                   "checkpoint does not record) is refused before the load (RULING BESIDE AN END PENDING), the re-run "
                   "drops the flags that refusal names, and where the end is a look's or an exhausted schedule's pause "
                   "a stop so refused is offered again once the re-finish has shown it (should NO PAUSE TO ADJUDICATE "
                   "refuse an adjudication offered with the stop, it was recorded: drop --adjudication-file). An "
                   "adjudication is offered only for the pause it rules on, which the shown pause and the RULING line "
                   "name; one whose text is a ruling the checkpoint records for an earlier pause is refused before the "
                   "load (RULING REUSED); an adjudication the checkpoint already records is named as such on the "
                   "RULING line where one prints, and otherwise by the pre-load refusal that meets it first (RULING "
                   "REUSED, RULING BESIDE AN END PENDING, or NO PAUSE TO ADJUDICATE by the last pause's ruling "
                   "digest). Beside an end pending (the RULING line of an invocation that finds one says so) the end "
                   "is re-finished first, and a ruling the stage would not apply with it (the seat's adjudication, or "
                   "a PI stop not recorded with it) is refused before the load (RULING BESIDE AN END PENDING, exit 2; "
                   "where no precheck runs the stage re-finishes the end and then refuses it, NOT APPLIED, exit 4), so "
                   "beside one no adjudication is offered, and the PI's stop only where the checkpoint records it; an "
                   "adjudication refused there is never offered again (NOT APPLIED's 'offer it again' holds for the "
                   "PI's stop alone): a re-finished pause that leaves the campaign open is then shown and takes the "
                   "seat's own ruling on it (a look's; an exhausted schedule's only beside the PI's stop) or the PI's "
                   "stop again; after a terminal end or a STOP that end stands (a pause it carries takes the seat's "
                   "own ruling on it, once shown, through VERDICTS as the declared --adjudication file; a PI's stop on "
                   "a hair trigger, the declared --pi-stop record), and an adjudication the checkpoint already records "
                   "needs nothing")
STAGE_HELP = {"time": "G-TIME-F3 (m:293): six sessions on Qwen, uncached, under LOCK-m-F3 v0.1; the flags are the "
                      "lock's values (lock §1)",
              "id": "G-ID-F3 (m:295): A2s and A3s on Qwen, each index uncached then cached, at the cap of record, "
                    "under LOCK-m-F3 v0.1 as re-issued; its prior is G-TIME-F3's re-run checkpoint; the flags are the "
                    "lock's values (lock §1)",
              "qual": "G-F3 (m:297): 40 sessions on Qwen, uncached, at the cap of record, under LOCK-m-F3 v0.2; its "
                      "prior is G-TIME-F3's re-run checkpoint, with G-ID-F3's artifact; the flags are the lock's values "
                      "(lock §1)",
              "campaign": "the Q-F3 campaign (m:298, m:361): the six arms interleaved by §2.1's rule, uncached, at the "
                          "cap of record, until each arm's domain count reaches its floor (A1 80, A1s 32, A2 144, A2s "
                          "56, A3 144, A3s 56), the hour cap (480 h) or the PI's stop, on Qwen under LOCK-m-F3 v1.0; its "
                          "prior is G-F3's checkpoint; the flags are the lock's values (lock §1)"}
HF_OFFLINE_ENV = "HF_HUB_OFFLINE"
# PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's PIN at LOCK v0.2 carried, scripts/m_sessions.py): the model id the
# Qwen path loads -- QwenMLXAdapter's default, passed explicitly by _load_qwen; the model of record mf3.resume
# binds -- and mlx_lm.utils._download's default allow_patterns, with which the snapshot check resolves the
# snapshot as the load does. The self-test asserts both equal their sources (the adapter's and mlx_lm's source,
# read, not imported) and m's driver's constants (its source, read, not imported).
QWEN_MODEL_ID = rs.QWEN_MODEL_ID
MLX_LM_ALLOW_PATTERNS = ("*.json", "model*.safetensors", "*.py", "tokenizer.model", "*.tiktoken",
                         "tiktoken.model", "*.txt", "*.jsonl", "*.jinja")
_HEX64_RX = re.compile(r"\b[0-9a-f]{64}\b")
_WEIGHTS_RX = re.compile(r"(?<![\w-])WEIGHTS (\S+) revision ([0-9a-f]{40}) sha256 ([0-9a-f]{64})\b")
# PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's TOTALS_RX / redact_totals / _say carried): every REFUSED and STOP
# line of the stage path passes through redact_totals (the step-14 read's Q3) and goes to stderr, as m's do.
TOTALS_RX = re.compile(r"hour_cap_ms_used \S+ != the sessions\\*' \S+ ms")
TOTALS_REDACTED = ("hour_cap_ms_used and the sessions' total differ (both figures redacted at the driver's "
                   "print: the step-14 read, Q3)")


def redact_totals(text: str) -> str:
    """``text`` with every occurrence of Q3's two totals replaced by TOTALS_REDACTED."""
    return TOTALS_RX.sub(TOTALS_REDACTED, text)


def _say(line: str) -> None:
    # a REFUSED or STOP line of the stage path: redacted (Q3), then printed to stderr
    print(redact_totals(line), file=sys.stderr, flush=True)


def refusal(cmd: str) -> str:
    return (f"REFUSED: {cmd} ({STAGE_NAMES[cmd]}) is not wired yet -- each Q-F3 stage subcommand is wired at its "
            f"own step, on its own word, after its lock (m:361); its driver is built and stub-tested in "
            f"valence_core.mf3.stages")


def build_schedules(out: str | None) -> int:
    try:
        shas = schedule.write_schedule_files(out)
    except RuntimeError as e:
        print(f"REFUSED: {e}", flush=True)
        return 2
    d = Path(out) if out is not None else schedule.DEFAULT_OUT
    probs = schedule.verify_schedule_dir(d)
    print(f"SCHEDULES {d}: {len(shas)} files (manifest included); verify {'clean' if not probs else probs[:3]}; "
          f"manifest sha256 {shas[schedule.MANIFEST_NAME]}", flush=True)
    return 0 if not probs else 4


def hashes(snapshot_dir: str | None = None) -> int:
    print(f"MF3 PACKAGE sha256 {guard.package_sha256_of(guard.PACKAGE_DIR)} ({len(list(guard.PACKAGE_DIR.glob('*.py')))} "
          f"files, valence_core/mf3/*.py)", flush=True)
    for m, v in guard.m_module_sha256s().items():
        print(f"M MODULE valence_core/m/{m}.py sha256 {v}", flush=True)
    man = schedule.DEFAULT_OUT / schedule.MANIFEST_NAME
    print(f"SCHEDULES MANIFEST {man.relative_to(REPO)} sha256 "
          f"{hashlib.sha256(man.read_bytes()).hexdigest() if man.is_file() else 'ABSENT'}", flush=True)
    try:
        wb = rs.weights_binding(snapshot_dir or rs.hub_repo_dir() / "snapshots" / gshape.QWEN_REVISION)
        print(f"WEIGHTS {gshape.QWEN_MODEL_ID} revision {wb['revision']} sha256 {wb['sha256']}", flush=True)
    except (OSError, ValueError, KeyError) as e:
        print(f"WEIGHTS unreadable ({type(e).__name__})", flush=True)
        return 4
    return 0


def run_gshape(out: str | None) -> int:
    try:
        res = gshape.write(out)
    except gshape.GshapeRefusal as e:
        print(str(e), flush=True)
        return 2
    except gshape.GshapeStop as e:
        print(str(e), flush=True)
        return 4
    print(("G-SHAPE-F3 canonical run (every source committed at HEAD and unedited)" if res["canonical"]
           else "G-SHAPE-F3 test run (--out; never of record)"), flush=True)
    for ln in gshape.summary_lines(res):
        print(ln, flush=True)
    return gshape.EXIT[res["artifact"]["verdict"]]


# --- the time wiring: G-TIME-F3 (m:293) ------------------------------------------------------------
def _load_qwen():
    """The Qwen adapter, through the package's one loader (valence_core.adapters.qwen_or_explain), with
    QWEN_MODEL_ID passed explicitly (the snapshot check reads the same constant)."""
    from valence_core.adapters import qwen_or_explain
    return qwen_or_explain(__file__, model_id=QWEN_MODEL_ID)


def lock_m_modules(lock_text: str) -> tuple[dict[str, str] | None, list[str]]:
    """(m_module_sha256, problems) read from a lock's committed text: for each file of guard.M_HASHED,
    the one sha256 named on the lines that name its path; (None, problems) if any file is named on no
    line with a sha256, or with two different ones."""
    out: dict[str, str] = {}
    probs: list[str] = []
    lines = lock_text.splitlines()
    for m in guard.M_HASHED:
        path = f"valence_core/m/{m}.py"
        found = {h for ln in lines if path in ln for h in _HEX64_RX.findall(ln)}
        if len(found) != 1:
            probs.append(f"--lock-file {TIME_LOCK_FILE}: its committed text names {path} with "
                         f"{'no' if not found else len(found)} sha256 (one is required: lock §1, the eleven m files)")
            continue
        out[m] = found.pop()
    return (None, probs) if probs else (dict(sorted(out.items())), [])


def lock_weights(lock_text: str) -> tuple[tuple[str, str] | None, list[str]]:
    """((revision, sha256), problems) read from a lock's committed text: its one WEIGHTS line (lock §1),
    which must name QWEN_MODEL_ID; (None, problems) if there is none, more than one value, or another model."""
    found = set(_WEIGHTS_RX.findall(lock_text))
    if len(found) != 1:
        return None, [f"--lock-file {TIME_LOCK_FILE}: its committed text carries {len(found)} distinct WEIGHTS "
                      f"lines (one is required: lock §1, the weights of record)"]
    model, rev, sha = found.pop()
    if model != QWEN_MODEL_ID:
        return None, [f"--lock-file {TIME_LOCK_FILE}: its WEIGHTS line names {model}, not the model of record "
                      f"{QWEN_MODEL_ID}"]
    return (rev, sha), []


def campaign_floors() -> dict[str, int]:
    """The campaign's floors per arm, in CAMPAIGN_LAUNCH_COUNTS' order: mf3's schedule.FLOORS under
    CAMPAIGN_LOCKED_PATH (a per-path entry, A1's) or as it stands (one floor for both paths) -- m's campaign_floors,
    carried."""
    fl = {t: schedule.FLOORS[t] for t, _ in CAMPAIGN_LAUNCH_COUNTS}
    return {t: (v[CAMPAIGN_LOCKED_PATH] if isinstance(v, dict) else v) for t, v in fl.items()}


def stage_identity_extra(stage: str, proposal_file: str, lock_file: str, *, analyzer_sha256: str,
                         package_sha256: str, renders_sha16: str) -> tuple[dict | None, list[str]]:
    """A wired stage's identity_extra and the problems that stop it being built ((None, problems)).

    PIN (Code, declared at the Q-F3 campaign wiring; m's stage_identity_extra for "campaign" carried): the campaign's
    identity is built as G-F3's, below, citing CAMPAIGN_LOCK_FILE, with reasoning_cap CAMPAIGN_REASONING_CAP and
    locked_path CAMPAIGN_LOCKED_PATH. Before the m files and the weights are read, the lock's committed text must carry
    each of QUAL_LOCK_LINES at the start of a line, as at G-F3, and each of CAMPAIGN_LOCK_LINES as a whole line
    (LOCK-m-F3 v1.0 §1's launch counts and §2's hour cap), else it is refused -- v0.2's blob, for one. A line test, as
    qual's, not m's substring test (the seat's answers of 2026-11-15, §2 (a)), and a whole-line one: v1.0 writes each of
    the two alone on its line, so a line that only begins with one (other counts, "480 hours") is refused too.

    PIN (Code, declared at LOCK-m-F3 v1.0; the qual wiring; m's stage_identity_extra for "qual" carried): G-F3's identity
    is built as G-TIME-F3's, below, citing QUAL_LOCK_FILE, with reasoning_cap QUAL_REASONING_CAP and locked_path
    QUAL_LOCKED_PATH; before the m files and the weights are read, the lock's committed text must carry each of
    QUAL_LOCK_LINES at the start of a line (LOCK-m-F3 v0.2's cap and path lines), else it is refused -- the re-issue's
    blob, for one, as m's qual refused a lock naming no QUAL_LOCK_PATH_TEXT. A line test, not m's substring test: v0.2
    writes each string once, at its definitional line (the v0.2 values-check's item 42).

    PIN (Code, declared at LOCK-m-F3 v0.2; the id wiring; m's stage_identity_extra for "id" carried): G-ID-F3's
    identity is built as G-TIME-F3's, below, citing the same lock (ID_LOCK_FILE), with reasoning_cap
    ID_REASONING_CAP and no locked_path (m's "G-ID-F0m carries none"; the path is recorded at LOCK-m-F3 v0.2, lock
    §1); stages._extra validates it for "id" as a run on a model, which refuses any cap but 120 and a locked_path.

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's stage_identity_extra carried, scripts/m_sessions.py): the
    proposal's and the lock's sha256 are computed here from their COMMITTED blobs (stages.committed:
    committed at HEAD, working tree identical). The lock is TIME_LOCK_FILE, and its committed text must name
    the proposal's sha256 in full. The analyzer's and mf3's package sha256 and the renders' sha16 are the
    values the command line gives -- the lock's -- and are never derived here from the bytes they are
    checked against: the licence checks the first two at stage start ((d), (e)) and _renders_of_record the
    third. m_module_sha256 and the weights binding are read from the lock's committed text (the routing of
    2026-11-07): each of guard.M_HASHED's eleven files with the one sha256 the lines naming it carry, and
    the one WEIGHTS line, which must name QWEN_MODEL_ID; the licence then checks them against the files
    ((e')), the hub cache ((g)) and that same text ((f)). reasoning_cap 120, the cap of record (A-m2 v0.5
    §4.1), and locked_path "uncached" (m:293) are this driver's; prior_proposal_sha256s is omitted (none
    under LOCK-m-F3 v0.1, lock §1). The result is validated by stages._extra as a run on a model (stub=False),
    which refuses any cap but 120 (A-m2 v0.5 §4.2: "the driver's `time` at any cap but 120 is refused")."""
    if stage not in WIRED_CMDS:
        raise ValueError(f"stage_identity_extra: {stage!r} is not one of {WIRED_CMDS}")
    want_lock = {"time": TIME_LOCK_FILE, "id": ID_LOCK_FILE, "qual": QUAL_LOCK_FILE, "campaign": CAMPAIGN_LOCK_FILE}[stage]
    probs: list[str] = []
    extra: dict = {}
    lock_text = ""
    for key, given in (("proposal", proposal_file), ("lock", lock_file)):
        p = Path(given)
        p = p if p.is_absolute() else REPO / p
        try:
            rel = p.resolve().relative_to(REPO.resolve()).as_posix()
        except (ValueError, OSError, RuntimeError):
            probs.append(f"--{key}-file {given}: lies outside the repository (or does not resolve)")
            continue
        if key == "lock" and rel != want_lock:
            probs.append(f"--lock-file {rel}: {stages.stage_name(stage)} cites {want_lock} (lock §1)")
            continue
        cp, data = stages.committed(rel)
        if cp or data is None:
            probs.append(f"--{key}-file {rel}: {cp} (the identity hashes its committed blob)")
            continue
        extra[f"{key}_file"] = rel
        extra[f"{key}_sha256"] = hashlib.sha256(data).hexdigest()
        if key == "lock":
            lock_text = data.decode("utf-8", "replace")
    if probs:
        return None, probs
    if extra["proposal_sha256"] not in lock_text:
        return None, [f"--proposal-file {extra['proposal_file']}: its sha256 {extra['proposal_sha256'][:16]}... is "
                      f"not named in full in {TIME_LOCK_FILE}'s committed text (lock §1 binds the proposal of record)"]
    if stage in ("qual", "campaign"):
        lock_lines = lock_text.splitlines()
        absent = [x for x in QUAL_LOCK_LINES if not any(ln.startswith(x) for ln in lock_lines)]
        if absent:
            return None, [f"--lock-file {want_lock}: its committed text carries no line opening {absent} (LOCK-m-F3 "
                          f"v0.2 §2-§3: the cap and the path {stages.stage_name(stage)} runs under; an earlier blob is "
                          f"refused)"]
        missing = [x for x in CAMPAIGN_LOCK_LINES if x not in lock_lines] if stage == "campaign" else []
        if missing:
            return None, [f"--lock-file {want_lock}: its committed text carries no whole line {missing} (LOCK-m-F3 "
                          f"v1.0 §1-§2: the launch counts and the hour cap the campaign runs under; an earlier blob "
                          f"is refused)"]
    mm, mprobs = lock_m_modules(lock_text)
    wb, wprobs = lock_weights(lock_text)
    if mprobs or wprobs or mm is None or wb is None:
        return None, mprobs + wprobs
    extra.update(analyzer_sha256=analyzer_sha256, package_sha256=package_sha256, renders_sha16=renders_sha16,
                 m_module_sha256=mm, weights_revision=wb[0], weights_sha256=wb[1],
                 reasoning_cap={"time": TIME_REASONING_CAP, "id": ID_REASONING_CAP, "qual": QUAL_REASONING_CAP,
                                "campaign": CAMPAIGN_REASONING_CAP}[stage])
    if stage == "time":
        extra["locked_path"] = TIME_LOCKED_PATH
    elif stage == "qual":
        extra["locked_path"] = QUAL_LOCKED_PATH
    elif stage == "campaign":
        extra["locked_path"] = CAMPAIGN_LOCKED_PATH
    try:
        stages._extra(extra, stage=stage, stub=False)
    except ValueError as e:
        return None, [str(e)]
    return extra, []


def time_identity_extra(proposal_file: str, lock_file: str, *, analyzer_sha256: str, package_sha256: str,
                        renders_sha16: str) -> tuple[dict | None, list[str]]:
    """G-TIME-F3's identity_extra: stage_identity_extra for "time" (m's step-10 wrapper form)."""
    return stage_identity_extra("time", proposal_file, lock_file, analyzer_sha256=analyzer_sha256,
                                package_sha256=package_sha256, renders_sha16=renders_sha16)


def _repo_rel(path: Path) -> str | None:
    try:
        return Path(path).resolve().relative_to(REPO.resolve()).as_posix()
    except (ValueError, OSError, RuntimeError):
        return None


def time_checkpoint(paths: dict) -> Path:
    """G-TIME-F3's re-run checkpoint, <out_root>/ckpt/TIME_CKPT_NAME, through stages.checkpoint_path; the first
    run's checkpoint name refused as a target (A-m2 v0.5 §4.2-§4.3: "refusing the first run's stem as a target")."""
    cpath = stages.checkpoint_path(Path(paths["root"]) / "ckpt" / TIME_CKPT_NAME, paths)
    if cpath.name == FIRST_RUN_CKPT_NAME:
        raise SystemExit(f"CHECKPOINT PATH REFUSED: {cpath.name} is G-TIME-F3's first run's checkpoint, never written "
                         f"again (A-m2 v0.5 §4.3); the re-run writes {TIME_CKPT_NAME}")
    return cpath


def stage_prior_checkpoint(stage: str, paths: dict) -> Path:
    """G-ID-F3's or G-F3's prior: G-TIME-F3's re-run checkpoint, <out_root>/ckpt/ID_PRIOR_CKPT_NAME (id) or
    QUAL_PRIOR_CKPT_NAME (qual), through stages.checkpoint_path, taken by path; the first run's checkpoint name refused,
    also where the path resolves to it (A-m2 v0.5 §4.3: "the `id` and `qual` wirings take the re-run's checkpoint by
    path and refuse the first"). The campaign's prior: G-F3's checkpoint, <out_root>/ckpt/CAMPAIGN_PRIOR_CKPT_NAME (m's
    default stem for "qual", stages.PRIOR_STAGE), by path in the same form; G-TIME-F3's first run's name is refused
    there too."""
    if stage not in ("id", "qual", "campaign"):
        raise ValueError(f"stage_prior_checkpoint: {stage!r} takes no prior checkpoint here")
    name = {"id": ID_PRIOR_CKPT_NAME, "qual": QUAL_PRIOR_CKPT_NAME, "campaign": CAMPAIGN_PRIOR_CKPT_NAME}[stage]
    cpath = stages.checkpoint_path(Path(paths["root"]) / "ckpt" / name, paths)
    if cpath.name == FIRST_RUN_CKPT_NAME:
        took = (f"G-F3's, {CAMPAIGN_PRIOR_CKPT_NAME}" if stage == "campaign" else f"the re-run's, {TIME_CKPT_NAME}")
        raise SystemExit(f"PRIOR PATH REFUSED: {cpath.name} is G-TIME-F3's first run's checkpoint; "
                         f"{stages.stage_name(stage)} takes {took}, by path (A-m2 v0.5 §4.3)")
    return cpath


def id_prior_checkpoint(paths: dict) -> Path:
    """G-ID-F3's prior: stage_prior_checkpoint for "id"."""
    return stage_prior_checkpoint("id", paths)


def _campaign_state(cpath: Path) -> tuple[str, dict]:
    """(state, summary) of the campaign checkpoint at ``cpath``, read tolerantly as JSON (no state check, so no total
    is computed or printed).

    PIN (Code, declared at the Q-F3 campaign wiring; m's _campaign_state carried, for Q-F3's arms): state: "absent";
    "unreadable" -- not a regular file (a FIFO is never opened), not a JSON object, nested
    past the recursion limit, its sessions, campaign block, pauses or recorded PI stop mistyped, a pause lacking kind,
    at_launches or adjudication or carrying a value no write of the package gives it (a kind other than look, end_look
    and schedule_exhausted, a launch count that is not an int, an adjudication that is not a text, an arm other than
    keys.TEMPLATES'), a recorded text that cannot be encoded (the PI stop or any pause's adjudication, a lone
    surrogate), or a path whose stat fails; "pending" (an end pending); "ended" (resume.ended_status); or "open".
    summary, the only thing the mirror and the RULING line read (the checkpoint never leaves this function), free of
    any recorded text: {"launched": a session is recorded, "pi_stop_sha256": the recorded PI stop's sha256 or None,
    "last": None or the last pause's {"kind", "at_launches", "arm", "adjudicated", "adjudication_sha16"} -- the digest
    the report gives a pause, "ruling_sha16s": the sha16 of every pause's recorded ruling, in pause order}; {} when
    unreadable."""
    p = Path(cpath)
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
                       and x.get("arm") in (None,) + tuple(keys.TEMPLATES) for x in pauses)
            or not (camp.get("pi_stop") is None or type(camp.get("pi_stop")) is str)):
        return "unreadable", {}
    last = pauses[-1] if pauses else None
    try:
        for x in pauses:
            if x["adjudication"] is not None:
                x["adjudication"].encode("utf-8")
        summary = {"launched": bool(ck.get("sessions")),
                   "pi_stop_sha256": (None if camp.get("pi_stop") is None
                                      else hashlib.sha256(camp["pi_stop"].encode("utf-8")).hexdigest()),
                   "last": None if last is None else {
                       "kind": last["kind"], "at_launches": last["at_launches"], "arm": last.get("arm"),
                       "adjudicated": last["adjudication"] is not None,
                       "adjudication_sha16": (stages._sha16_text(last["adjudication"])
                                              if type(last["adjudication"]) is str else None)},
                   "ruling_sha16s": [stages._sha16_text(x["adjudication"]) for x in pauses
                                     if type(x["adjudication"]) is str]}
    except UnicodeEncodeError:
        return "unreadable", {}
    if rs.pending_end(ck) is not None:
        return "pending", summary
    if rs.ended_status(ck) is not None:
        return "ended", summary
    return "open", summary


def campaign_ruling_problems(cpath: Path, adjudication: str | None, pi_stop: str | None) -> list[str]:
    """The refusals stages.run_campaign makes, after the load and before its first write, of a ruling that does not
    fit the campaign's state -- made here before the load, from ``_campaign_state``'s summary -- and two the stage does
    not make (O4-1 and O1-3: RULING BESIDE AN END PENDING, where the stage would re-finish the end and then refuse the
    ruling, NOT APPLIED; RULING REUSED, where it would apply it); [] when none applies.

    PIN (Code, declared at the Q-F3 campaign wiring; m's campaign_ruling_problems carried, with its carry-overs O4-1,
    O1-3 and RM4-1): mirrors run_campaign's order over the states the stage writes: a PI stop text other than the one
    the checkpoint records (CHECKPOINT MISMATCH, made even beside an end pending); then, on a checkpoint neither pending
    nor ended (a pending end re-finishes at any invocation; an ended one is refused as ended): a PI stop with no session
    launched (PI STOP REFUSED); an adjudication on an exhausted schedule's unadjudicated pause with no PI stop (SCHEDULE
    EXHAUSTED); an adjudication with no unadjudicated pause (NO PAUSE TO ADJUDICATE). Each message is the stage's own
    words -- mf3's run_campaign's, which words three of the four otherwise than m's stage; the self-test reads them
    from its source -- two with a declared suffix: CHECKPOINT MISMATCH's, that the stage makes it after the load, and
    NO PAUSE TO ADJUDICATE's, where the last pause already carries a ruling, naming that pause and its ruling's sha16
    and how the run resumes: with --resume alone, or, where this run also offers the PI's stop, with --resume and the
    PI's stop alone. The recorded PI stop is compared by its sha256 (the summary carries no text). An invocation
    offering no ruling reads nothing. An absent checkpoint is a campaign with no session and no pause. An unreadable
    or malformed one is not refused here: stage_precheck refuses it before the load; the stage, which has no such
    screen, refuses it with a refusal of its own, raises, or reads it as it stands."""
    if adjudication is None and pi_stop is None:
        return []
    state, sm = _campaign_state(cpath)
    if state in ("unreadable", "ended"):
        return []
    rec_pi = sm["pi_stop_sha256"]
    if (pi_stop is not None and rec_pi is not None
            and hashlib.sha256(pi_stop.strip().encode("utf-8")).hexdigest() != rec_pi):
        return [f"CHECKPOINT MISMATCH: {cpath} records the PI's stop; this run offers another text -- "
                f"refusing (the stage makes this refusal after the load)"]
    if state == "pending":
        # O4-1, carried (m's PIN at LOCK-m-OLMo-{ckpt} v0.1): the rulings refused are exactly the ones the stage would
        # not apply beside an end pending (stages._refinish_campaign's NOT APPLIED): the seat's adjudication, and a PI
        # stop the checkpoint does not record (a stop it records, passed by run_campaign as None, re-finishes with no
        # refusal). An adjudication the checkpoint already records is named as such and needs nothing (RM4-1's
        # information where no RULING line prints).
        a16_ = stages._sha16_text(adjudication.strip()) if adjudication is not None else None
        adj_w_ = "the seat's adjudication" + (
            f", which the checkpoint already records as a pause's ruling (sha16 {a16_}) and which needs nothing"
            if a16_ is not None and a16_ in sm.get("ruling_sha16s", []) else "")
        skip_ = [(w_, f_) for w_, f_, v_ in ((adj_w_, "--adjudication-file", adjudication),
                                             ("the PI's stop, which the checkpoint does not record", "--pi-stop-file",
                                              pi_stop if rec_pi is None else None)) if v_ is not None]
        if skip_:
            return [f"RULING BESIDE AN END PENDING at {cpath}: the checkpoint carries an end pending, which the "
                    f"stage re-finishes before it applies any ruling, and it would not apply "
                    f"{' and '.join(w_ for w_, _f in skip_)} (NOT APPLIED, after the load) -- refused before the "
                    f"load: re-run without {' and '.join(f_ for _w, f_ in skip_)}, with --resume, which re-finishes "
                    f"the end; then offer a ruling for the pause the re-finish shows, if it leaves the campaign open"]
        return []
    pi = pi_stop is not None or rec_pi is not None
    if pi and not sm["launched"]:
        return [f"PI STOP REFUSED at {cpath}: no session has launched -- a unit that never launches is "
                f"NOT-RUN by its Clock (m:192)"]
    last = sm["last"]
    open_pause = last is not None and not last["adjudicated"]
    if open_pause and last["kind"] == "schedule_exhausted" and not pi and adjudication is not None:
        return [f"SCHEDULE EXHAUSTED at {cpath}: {last['arm']} has no committed cell left below its floor; "
                f"only the PI's stop ends this campaign (m:192, m:247)"]
    # O1-3, carried (m's PIN at LOCK-m-OLMo-{ckpt} v0.1): an adjudication offered for an open pause whose text is a
    # ruling the checkpoint already records for an earlier pause is refused here; the stage has no such rule.
    if adjudication is not None and open_pause:
        a16_ = stages._sha16_text(adjudication.strip())
        if a16_ in sm.get("ruling_sha16s", []):
            return [f"RULING REUSED at {cpath}: the seat's adjudication offered (sha16 {a16_}) is the text the "
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


def ruling_line(name: str, cpath: Path, rulings: dict) -> str | None:
    """The RULING line a campaign invocation offering a ruling prints before the load.

    PIN (Code, declared at the Q-F3 campaign wiring; m's ruling_line carried, with RM4-1's note): pick-free, each
    text's sha16 of the stripped text (the report gives a
    pause's adjudication the same digest; the PI's stop's, where the stage records it only as the campaign's stop, and,
    where no precheck runs, a ruling offered beside an end pending that the checkpoint does not record, which the stage
    does not apply there (NOT APPLIED), stand here alone; on the Qwen path such a ruling is refused before the load and
    before this line, O4-1), and the pause it is offered for (its kind and launch count, as the shown pause's line prints
    them) or the checkpoint's state, from ``_campaign_state``'s summary, with RM4-1's note where the checkpoint already
    records the adjudication offered as a pause's ruling (by digest; text-free); None when no ruling is offered."""
    parts = [f"{who} (sha16 {stages._sha16_text(rulings[k].strip())})"
             for k, who in (("adjudication", "the seat's adjudication"), ("pi_stop", "the PI's stop"))
             if rulings.get(k) is not None]
    if not parts:
        return None
    state, sm = _campaign_state(cpath)
    last = sm.get("last") if state == "open" else None
    if last is not None and not last["adjudicated"]:
        where = f"for the pause at {last['at_launches']} launches ({last['kind']})"
    else:
        where = {"absent": "with no checkpoint on disk", "pending": "beside an end pending",
                 "ended": "on an ended campaign", "unreadable": "on an unreadable checkpoint"}.get(
            state, "with no pause unadjudicated")
    note = ""
    if rulings.get("adjudication") is not None and stages._sha16_text(rulings["adjudication"].strip()) in (
            sm.get("ruling_sha16s") or []):
        note = "; the checkpoint already records this adjudication as a pause's ruling"
    return f"RULING {name}: {' and '.join(parts)} offered {where}{note}"


def ruling_texts(adjudication_file: str | None, pi_stop_file: str | None) -> tuple[dict, list[str]]:
    """({"adjudication": text or None, "pi_stop": text or None}, problems) of the campaign's two ruling files.

    PIN (Code, declared at the Q-F3 campaign wiring; m's ruling_texts carried): stages.run_campaign takes the seat's
    adjudication of a pending pause and the PI's stop as texts, recorded in the checkpoint only; the driver takes each
    as a file named on the command line, so the text stands in no command line, launch line or raw, and prints neither
    (its path does stand in the INVOCATION line, so the file is named for nothing it says). A file given must be a
    regular file (a FIFO or a device is refused before it is opened), UTF-8 (a leading byte-order mark is dropped:
    utf-8-sig) and not blank -- a text with no visible character (only whitespace, format characters such as a
    zero-width space, or control characters); its text is passed as read (the stage strips it)."""
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


def stage_precheck(stage: str, extra: dict, *, resume_run: bool, out_root: Path,
                   rulings: dict | None = None) -> list[str]:
    """A wired stage's refusals that need no model, made before the Qwen load; [] = none fired.

    PIN (Code, declared at the Q-F3 campaign wiring; m's stage_precheck for "campaign" carried, scripts/m_sessions.py):
    at the campaign the checks are G-F3's, below, on the six committed campaign schedule files and the campaign's own
    checkpoint (stages.out_paths("campaign")), with these differences, each m's: a paused campaign offered no ruling
    (``rulings`` None, or both texts None) is not refused as existing -- the stage shows its pause with or without
    --resume (stages._paused_unadjudicated, asked only of a checkpoint the screen reads as open); the prior is G-F3's
    checkpoint at this out root (stage_prior_checkpoint for "campaign"), ended PASS under this proposal, not written on
    the stub, at the run's cap (stages.prior_gate, require_real on); G-ID-F3's artifact is checked if on disk
    (stages.gid_artifact_problems, require_real on, at the run's cap, as run_campaign re-checks it; absent, there is
    nothing to check); a campaign checkpoint path that exists and that the driver cannot read as a campaign checkpoint
    (``_campaign_state``'s "unreadable"), which only this precheck refuses (the stage would refuse it as existing, block
    on a FIFO with --resume, refuse it as unreadable, raise, or read it as it stands); and a ruling's fit to the
    campaign's state (campaign_ruling_problems: NO PAUSE TO ADJUDICATE, PI STOP REFUSED, SCHEDULE EXHAUSTED and a PI
    stop text other than the one recorded, the stage making each again after the load; RULING BESIDE AN END PENDING and
    RULING REUSED, which it does not). Not made here: the path the G-ID licence gives on the loaded backend (PATH
    MISMATCH), the floors and the launch-count projection a checkpoint records (CHECKPOINT MISMATCH, the stage's), and
    the stage's other refusals after the load. A pending end offered no ruling re-finishes at any invocation, so the
    precheck lets it through.

    PIN (Code, declared at LOCK-m-F3 v1.0; the qual wiring; m's stage_precheck for "qual" carried, scripts/m_sessions.py):
    at G-F3 the checks are G-TIME-F3's, below, on G-F3's six committed schedule files and its own checkpoint
    (stages.out_paths("qual")), and the prior, as at G-ID-F3: stage_prior_checkpoint, then stages.prior_gate with
    require_real on, which at "qual" also requires G-ID-F3's artifact on disk at the run's cap -- any verdict, under this
    proposal, not written on the stub (stages.gid_artifact_problems). Made only by the stage after the load: the path
    the G-ID licence gives on the loaded backend at the cap, which stages._locked holds to the locked path (PATH
    MISMATCH), beside the list below.

    PIN (Code, declared at LOCK-m-F3 v0.2; the id wiring; m's stage_precheck for "id" carried, scripts/m_sessions.py):
    at G-ID-F3 the checks are G-TIME-F3's, below, on G-ID-F3's committed schedule files (A2s and A3s) and its own
    checkpoint (stages.out_paths("id"): the path itself, an ENDED one, one on disk without --resume and no end
    pending), and two more, m's: the prior -- id_prior_checkpoint (stage_prior_checkpoint for "id"), then
    stages.prior_gate with require_real on, as
    the stage makes it after the load (G-TIME-F3 ended PASS, under this proposal, not written on the stub, at the cap
    of record, which is this run's) -- and an existing G-ID artifact, a link included, unless G-ID-F3's own
    checkpoint carries an end pending. Only this precheck refuses a link at the artifact path that does not resolve
    (the stage tests exists() alone), as in m. Made only by the stage after the load, beside the list below: on a
    re-finish of G-ID-F3's own pending end, the artifact's byte-identity with the one the finish re-derives
    (stages._finish_gid's G-ID ARTIFACT DIFFERS).

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's stage_precheck carried for "time", scripts/m_sessions.py): the
    licence by file ((a)-(g)); the run-time known answers on the proposal the identity names; the renders of
    record; the committed schedule files; the checkpoint (the path itself; an ENDED one; one on disk without
    --resume and no end pending); m:267's laptop checklist (power, one model process, disk); the gate line and
    its files (CLAUDE.md and the analyzer committed, working tree identical; HEAD known). The stage
    (stages.run_gate_stage) makes each of them again after the load, except the refusal of a looping link at
    the checkpoint path, which only this precheck makes. NOT made here, so made only by the stage after the
    load: a resume's comparison of the checkpoint with this run (rs.load_or_init's identity and readability
    refusals, stages._record_licence), runner.f3_startup's pins, the counts against the committed files' n,
    the bars' firing-case completeness and the stage's internal assertions. ``run_time`` adds the driver
    check's and the snapshot check's problems and refuses once. Every problem passes through redact_totals."""
    if stage not in WIRED_CMDS:
        raise ValueError(f"stage_precheck: {stage!r} is not one of {WIRED_CMDS}")
    name = stages.stage_name(stage)
    probs = [f"licence: {p}" for p in stages.licence_problems(extra)]
    proposal = stages._proposal_path(extra)
    probs += [f"startup: {p}" for p in stages.startup_problems(proposal)]
    try:
        stages._renders_of_record(extra, name)
    except SystemExit as e:
        probs.append(f"renders: {e}")
    paths = stages.out_paths(stage, out_root)
    wanted = {"time": [("time", t) for t, _ in TIME_COUNTS], "id": [("id", t) for t in keys.GID_TEMPLATES],
              "qual": [("qual", t) for t, _ in QUAL_COUNTS],
              "campaign": [("campaign", t) for t, _ in CAMPAIGN_LAUNCH_COUNTS]}[stage]
    try:
        stages.load_committed(wanted, paths["schedules"])
    except SystemExit as e:
        probs.append(f"schedules: {e}")
    cpath = None
    try:
        cpath = time_checkpoint(paths) if stage == "time" else stages.checkpoint_path(None, paths)
        rs.refuse_ended(cpath)
        # is_symlink: checkpoint_path resolve()s non-strictly; on Python 3.13+ a looping link comes back
        # unresolved, so the resolved path can still be a link, which only this precheck refuses; on 3.12
        # resolve() raises RuntimeError on the loop (caught below) -- m's comment, carried
        # a paused campaign offered no ruling is shown its pause with or without --resume (the campaign PIN above);
        # stages._paused_unadjudicated is asked only of a checkpoint the screen reads as open (m's form)
        offered = rulings is not None and any(v is not None for v in rulings.values())
        shown = (stage == "campaign" and not offered and _campaign_state(cpath)[0] == "open"
                 and stages._paused_unadjudicated(cpath))
        if (cpath.exists() or cpath.is_symlink()) and not resume_run and not rs.pending_at(cpath) and not shown:
            probs.append(f"checkpoint: CHECKPOINT EXISTS at {cpath}; pass --resume to continue it or move it aside "
                         f"(never overwritten)")
    except SystemExit as e:
        probs.append(f"checkpoint: {e}")
    except (RuntimeError, OSError) as e:
        probs.append(f"checkpoint: the checkpoint path does not resolve ({type(e).__name__})")
    if stage in ("id", "qual", "campaign"):
        try:
            stages.prior_gate(stage, stage_prior_checkpoint(stage, paths), proposal_sha256=extra["proposal_sha256"],
                              prior_proposal_sha256s=extra.get("prior_proposal_sha256s") or [], require_real=True,
                              reasoning_cap=extra["reasoning_cap"])
        except SystemExit as e:
            probs.append(f"prior: {e}")
        except (RuntimeError, OSError) as e:
            probs.append(f"prior: the prior checkpoint path does not resolve ({type(e).__name__})")
    if stage == "campaign" and cpath is not None:
        try:
            exists_, regular_ = cpath.exists(), cpath.is_file()
        except OSError:                                     # reported by the checkpoint block above
            exists_ = regular_ = False
        if exists_ and not regular_:
            probs.append(f"checkpoint: {cpath} exists and is not a regular file (refused before it is opened)")
        elif exists_ and _campaign_state(cpath)[0] == "unreadable":
            probs.append(f"checkpoint: {cpath} cannot be read as a campaign checkpoint (not a JSON object, or a shape "
                         f"or value no write of the package makes) -- refused before the load; a checkpoint is never "
                         f"edited by hand")
        if rulings is not None:
            probs += [f"ruling: {p}" for p in campaign_ruling_problems(cpath, rulings.get("adjudication"),
                                                                       rulings.get("pi_stop"))]
    if stage == "campaign":
        probs += [f"artifact: {p}" for p in stages.gid_artifact_problems(
            accepted=stages.accepted_proposals(extra["proposal_sha256"], extra.get("prior_proposal_sha256s") or []),
            require_real=True, reasoning_cap=extra["reasoning_cap"])]
    if stage == "id":
        gid_path = guard.gid_artifact_path()
        try:
            pending = cpath is not None and rs.pending_at(cpath)
        except (RuntimeError, OSError):
            pending = False
        if (gid_path.exists() or gid_path.is_symlink()) and not pending:
            probs.append(f"artifact: G-ID ARTIFACT EXISTS at {gid_path}; it is never overwritten")
    probs += [f"preflight: {p}" for p in guard.preflight_laptop()]
    probs += [f"gate line: {p}" for p in stages.gate_line(name, proposal)[1]]
    for what, path in (("CLAUDE.md", stages.CLAUDE_MD_PATH), ("analyzer", stages.ANALYZER_PATH)):
        rel = _repo_rel(path)
        probs += ([f"gate line: {what} {path} lies outside the repository"] if rel is None
                  else [f"gate line: {what} {x}" for x in stages.committed(rel)[0]])
    return [redact_totals(p) for p in probs]


def time_precheck(extra: dict, *, resume_run: bool, out_root: Path) -> list[str]:
    """G-TIME-F3's refusals that need no model: stage_precheck for "time" (m's step-10 wrapper form)."""
    return stage_precheck("time", extra, resume_run=resume_run, out_root=out_root)


def driver_problems() -> tuple[list[str], str | None]:
    """(problems, sha256) of this driver's bytes: [] and the sha256 of its committed blob when it is
    committed at HEAD with the working tree's bytes (stages.committed); else the problems and None.

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's driver_problems carried): the step-10 read's Q2 makes the
    record of the wiring driver's blob a condition of every wiring of its kind ("the new blob's sha256 printed
    by the DRIVER line and recorded in the entry of the stage it wires and in the next lock revision …"), which
    Code reads F-1 as carrying to this driver (the routing of 2026-11-07: G-TIME-F3's entry and LOCK-m-F3
    v0.2). run_time's Qwen path refuses an uncommitted driver and prints the DRIVER line from this one call
    before the load, so the value recorded is a value the run logged. A process running any file but the driver
    of record (REPO/DRIVER_REL) -- a copy, edited or not -- is refused: the DRIVER line names that path's committed
    blob, which would not be the code running (the review's MINOR-2; m derives DRIVER_REL from __file__)."""
    try:
        here = Path(__file__).resolve()
    except (OSError, RuntimeError):
        here = None
    if here != (REPO / DRIVER_REL).resolve():
        return [f"this process runs {__file__}, not the driver of record {DRIVER_REL} (the DRIVER line names that "
                f"file's committed blob)"], None
    cp, data = stages.committed(DRIVER_REL)
    if cp or data is None:
        return list(cp) or [f"{DRIVER_REL}: unreadable"], None
    return [], hashlib.sha256(data).hexdigest()


def qwen_snapshot(*, model_id: str | None = None, cache_dir: str | os.PathLike | None = None,
                  environ: dict | None = None, cwd: str | os.PathLike | None = None) -> tuple[list[str], dict | None]:
    """(problems, info) of the Qwen weights an offline load reads; [] and the info when clear.

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's qwen_snapshot carried verbatim in its checks, the routing of
    2026-11-07: "Build at time"): each refusal mirrors how the load resolves the weights (jlens_qwen.model.load
    -> mlx_lm.load -> mlx_lm.utils._download -> huggingface_hub.snapshot_download): HF_HUB_OFFLINE must be
    exactly "1"; MLXLM_USE_MODELSCOPE must not be "true" in any case (mlx_lm tests it so, and would take
    modelscope's downloader); no path or link named like the model id may exist relative to the working
    directory (mlx_lm loads an existing one before the hub cache; a dangling link is refused conservatively);
    the hub cache's `refs/main` for QWEN_MODEL_ID must be, as raw file text, a 40-hex revision whose snapshot
    directory exists and holds config.json, tokenizer.json, model.safetensors.index.json and every weight
    file the index names (each a plain file name, resolving to a file); and the hub's own offline resolution
    with mlx_lm's patterns (snapshot_download, local_files_only) must succeed and return that same directory.
    The cache is huggingface_hub's HF_HUB_CACHE. info: model_id, revision, snapshot_dir, n_snapshots
    (snapshot directories of the model's cache repo), offline. The licence's (g) checks the bound revision
    and the binding; this check is the load's own resolution, and its SNAPSHOT line is the raw's record."""
    env = os.environ if environ is None else environ
    probs: list[str] = []
    if env.get(HF_OFFLINE_ENV) != "1":
        probs.append(f"{HF_OFFLINE_ENV} is {env.get(HF_OFFLINE_ENV)!r}, not '1' (Code's form of the offline load: the "
                     f"licence's (g) and the seat's step-10 read, Q5)")
    ms = env.get("MLXLM_USE_MODELSCOPE", "False")
    if str(ms).lower() == "true":
        probs.append(f"MLXLM_USE_MODELSCOPE is {ms!r} (mlx_lm tests .lower() == 'true'): mlx_lm would load "
                     f"through modelscope, not the hub cache")
    model_id = QWEN_MODEL_ID if model_id is None else str(model_id)
    here = Path.cwd() if cwd is None else Path(cwd)
    if (here / model_id).exists() or (here / model_id).is_symlink():
        probs.append(f"{here / model_id} exists or is a link: mlx_lm loads a local path named like the model id "
                     f"before the hub cache (a dangling link refused conservatively)")
    if cache_dir is None:
        from huggingface_hub import constants as hf_constants
        cache_dir = hf_constants.HF_HUB_CACHE
    repo = Path(cache_dir) / ("models--" + model_id.replace("/", "--"))
    try:
        rev = (repo / "refs" / "main").read_text(encoding="utf-8")
    except (OSError, ValueError):
        return probs + [f"no readable refs/main for {model_id} under {cache_dir}"], None
    if not re.fullmatch(r"[0-9a-f]{40}", rev):
        return probs + [f"refs/main for {model_id} is not, as raw text, a 40-hex revision: {rev[:60]!r} (the "
                        f"hub's offline load reads it raw)"], None
    snap = repo / "snapshots" / rev
    if not snap.is_dir():
        return probs + [f"refs/main names {rev}, but no snapshot directory {snap} exists"], None
    try:
        n_snap = sum(1 for d in (repo / "snapshots").iterdir() if d.is_dir())
        index = json.loads((snap / "model.safetensors.index.json").read_text(encoding="utf-8"))
        weights = sorted(set(index["weight_map"].values()))
        bad = [w for w in weights if type(w) is not str or not w or "/" in w or "\\" in w or w in (".", "..")]
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as e:
        return probs + [f"snapshot {rev}: model.safetensors.index.json unreadable "
                        f"({type(e).__name__})"], None
    if bad:
        return probs + [f"snapshot {rev}: the index names a weight that is not a plain file name: {bad[:2]!r}"], None
    need = ["config.json", "tokenizer.json", "model.safetensors.index.json"] + weights
    missing = [f for f in need if not (snap / f).is_file()]
    if missing:
        probs.append(f"snapshot {rev} is incomplete: {missing[:4]} missing (an offline load would fail)")
    if not weights:
        probs.append(f"snapshot {rev}: the index names no weight file")
    try:
        from huggingface_hub import snapshot_download
        got = snapshot_download(model_id, local_files_only=True, allow_patterns=list(MLX_LM_ALLOW_PATTERNS),
                                cache_dir=str(cache_dir))
        if Path(got).resolve() != snap.resolve():
            probs.append(f"the hub's offline resolution gives {got}, not refs/main's snapshot {snap}")
    except Exception as e:                                      # noqa: BLE001 -- any failure refuses
        probs.append(f"the hub's offline resolution with mlx_lm's patterns refuses: {type(e).__name__}")
    info = {"model_id": model_id, "revision": rev, "snapshot_dir": str(snap),
            "n_snapshots": n_snap, "offline": env.get(HF_OFFLINE_ENV)}
    return probs, (None if probs else info)


def snapshot_line(info: dict) -> str:
    return (f"SNAPSHOT {info['model_id']} {info['revision']}: refs/main; {info['snapshot_dir']}; "
            f"{info['n_snapshots']} snapshot(s) in the model's cache repo; {HF_OFFLINE_ENV}={info['offline']}")


def run_stage(stage: str, *, proposal_file: str | None, lock_file: str | None, analyzer_sha256: str | None,
              package_sha256: str | None, renders_sha16: str | None, resume_run: bool, adapter_factory=None,
              out_root: Path | None = None, adjudication_file: str | None = None,
              pi_stop_file: str | None = None) -> int:
    """G-TIME-F3 (m:293) and G-F3 (m:297) through stages.run_gate_stage, G-ID-F3 (m:295) through
    stages.run_gid_pair_f3, or the Q-F3 campaign (m:298, m:361) through stages.run_campaign. Exit: stages.EXIT_CODES for
    the stage's status (0 PASS, 4 STOP; at G-ID-F3 also 5 FAIL and 6 NOT-DETERMINED; at the campaign 0 COMPLETE, CAP and
    PI-STOP, and 3 PAUSE) and 4 STOP for any SystemExit from the loader or the stage, or the driver's own post-load
    snapshot re-read or model-id check (each "STOP: " and its message); 2 refused before the load (nothing loaded or
    written); any other exception is uncaught (a traceback; exit 1, or 130 on Ctrl-C).

    PIN (Code, declared at the Q-F3 campaign wiring; m's _run_stage "campaign" branch carried): the campaign runs the
    Qwen path below as G-F3 does, its stage_identity_extra and stage_precheck for "campaign", and then
    stages.run_campaign with campaign_floors(), CAMPAIGN_LAUNCH_COUNTS, CAMPAIGN_HOUR_CAP, the prior
    stage_prior_checkpoint gives at this run's out root (G-F3's checkpoint, the path the precheck read; the stage's
    prior_gate reads it again after the load, and the stage re-checks G-ID-F3's artifact with its own call of
    gid_artifact_problems at the run's cap), its own checkpoint the stage's default, the resume flag, and the two
    rulings as ruling_texts read them. ``adjudication_file`` / ``pi_stop_file`` are the campaign's alone (a ValueError
    at any other stage); ruling_texts refuses them before the precheck when not a regular file, not UTF-8 or blank,
    and their fit to the campaign's state is refused before the load (campaign_ruling_problems, in the precheck). An
    invocation offering a ruling prints the RULING line (ruling_line) before the load: on the Qwen
    path after the DRIVER and SNAPSHOT lines, on the stub path before the adapter is built. A campaign PAUSE (exit 3) is
    escalated to the seat: a look's pause resumes only with --resume and the seat's adjudication, or ends by the PI's
    stop (with --resume); an exhausted schedule's ends only by the PI's stop; an end look's pause beside a terminal end
    is never resumed, its ruling entering VERDICTS as the analyzer's declared --adjudication file. A STOP naming NOT
    APPLIED is the stage declining a ruling offered beside an end pending, after re-finishing that end; on the Qwen path
    the precheck refuses such a ruling before the load (RULING BESIDE AN END PENDING).

    PIN (Code, declared at LOCK-m-F3 v1.0; the qual wiring; m's _run_stage "qual" branch carried): G-F3 runs the Qwen
    path below as G-TIME-F3 does, its stage_identity_extra and stage_precheck for "qual", and then
    stages.run_gate_stage with gate "qual", QUAL_COUNTS, the prior stage_prior_checkpoint gives at this run's out root --
    the path the precheck read; the stage's prior_gate reads it again after the load, with G-ID-F3's artifact -- its own
    checkpoint the stage's default, and the resume flag.

    PIN (Code, declared at LOCK-m-F3 v0.2; the id wiring; m's _run_stage "id" branch carried): G-ID-F3 runs the
    Qwen path below as G-TIME-F3 does, its stage_identity_extra and stage_precheck for "id", and then
    stages.run_gid_pair_f3 with the prior id_prior_checkpoint gives at this run's out root -- the path the precheck
    read; the stage's prior_gate reads it again after the load -- its own checkpoint the stage's default, and the
    resume flag; the stage itself refuses an existing artifact (B7).

    PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's _run_stage Qwen path carried, scripts/m_sessions.py):
    ``adapter_factory`` and ``out_root`` are the self-test's seam (a scripted stub writing a test directory,
    which stages refuses anywhere under data/mf3); without the factory the adapter is Qwen through
    qwen_or_explain, the out root is stages.DEFAULT_OUT (read at call time), a given ``out_root`` is refused
    before any load, and time_precheck, the driver check (one driver_problems call) and the snapshot check
    (one qwen_snapshot call), their problems refused together, then the DRIVER and SNAPSHOT lines, come before
    the load; after it, the snapshot is read again and the adapter's model_id compared: a re-read that refuses,
    a moved refs/main or another model id STOPs before a session (SNAPSHOT RE-READ REFUSED / SNAPSHOT MOVED /
    MODEL ID). A STOP, and any exit other than 0 or 2, is escalated to the seat; Code never self-adjudicates."""
    given = {"proposal_file": proposal_file, "lock_file": lock_file, "analyzer_sha256": analyzer_sha256,
             "package_sha256": package_sha256, "renders_sha16": renders_sha16}
    if stage not in WIRED_CMDS:
        raise ValueError(f"run_stage: {stage!r} is not one of {WIRED_CMDS}")
    if stage != "campaign" and (adjudication_file is not None or pi_stop_file is not None):
        raise ValueError(f"run_stage: {stage!r} takes no adjudication or PI-stop file (the campaign's alone)")
    missing = ["--" + k.replace("_", "-") for k in TIME_FLAGS if given[k] is None]
    if missing:
        _say(f"REFUSED: {stage} needs {missing}: the lock's values (lock §1, \"How a stage cites this file\"); "
             f"nothing loaded")
        return 2
    if out_root is not None and adapter_factory is None:
        _say(f"REFUSED: {stage}: an out root names a test directory; the Qwen run writes data/mf3 only (nothing "
             f"loaded)")
        return 2
    name = stages.stage_name(stage)
    extra, probs = stage_identity_extra(stage, proposal_file, lock_file, analyzer_sha256=analyzer_sha256,
                                        package_sha256=package_sha256, renders_sha16=renders_sha16)
    if probs or extra is None:
        _say(f"REFUSED: {name}: {probs}; nothing loaded")
        return 2
    rulings, rprobs = ruling_texts(adjudication_file, pi_stop_file)
    if rprobs:
        _say(f"REFUSED: {name}: {rprobs}; nothing loaded")
        return 2
    root = Path(stages.DEFAULT_OUT if out_root is None else out_root)

    def say_ruling() -> None:
        # the RULING line (ruling_line): the texts' sha16 and the pause they are offered for, before the load
        if stage == "campaign":
            rline = ruling_line(name, stages.checkpoint_path(None, stages.out_paths(stage, root)), rulings)
            if rline is not None:
                print(rline, flush=True)
    try:
        if adapter_factory is None:
            pre = stage_precheck(stage, extra, resume_run=resume_run, out_root=root,
                                 rulings=rulings if stage == "campaign" else None)
            dprobs, dsha = driver_problems()
            sprobs, snap = qwen_snapshot()
            # the snapshot's revision against the lock's (m's REVISION_STAGES refusal, carried): the licence's (g) read
            # refs/main at the precheck; this read is the load's own, so a move between the two is refused here,
            # before the load, not only by the re-read after it (the review's NOTE 3)
            if snap is not None and snap["revision"] != extra["weights_revision"]:
                sprobs = list(sprobs) + [f"refs/main is {snap['revision']}, not the lock's weights revision "
                                         f"{extra['weights_revision']} (lock §1; the licence's (g))"]
            pre += [f"driver: {p}" for p in dprobs] + [f"snapshot: {p}" for p in sprobs]
            if pre or dsha is None or snap is None:
                _say(f"REFUSED: {name}: {pre}; nothing loaded")
                return 2
            print(f"DRIVER {DRIVER_REL} {dsha}: committed at HEAD {stages._git_head()}, working tree identical",
                  flush=True)
            print(snapshot_line(snap), flush=True)
            say_ruling()
            adapter = _load_qwen()
            # the snapshot re-read after the load (m's): a re-read that refuses, a moved refs/main or another
            # model id STOPs before any session (a SystemExit, exit 4 below). It narrows, not closes, the window
            # between the precheck's read and the load's: a move and back between the two reads is not seen
            sprobs2, snap2 = qwen_snapshot()
            if sprobs2 or snap2 is None:
                raise SystemExit(f"SNAPSHOT RE-READ REFUSED ({name}): after the load the snapshot check refuses: "
                                 f"{sprobs2} -- no session runs")
            if snap2["revision"] != snap["revision"]:
                raise SystemExit(f"SNAPSHOT MOVED ({name}): before the load {snap['revision']}; after it "
                                 f"{snap2['revision']} -- no session runs")
            if getattr(adapter, "model_id", None) != snap["model_id"]:
                raise SystemExit(f"MODEL ID ({name}): the adapter loaded {getattr(adapter, 'model_id', None)!r}, "
                                 f"the snapshot check read {snap['model_id']!r} -- no session runs")
            print(f"SNAPSHOT re-read after the load: unchanged ({snap['revision']}); adapter model_id "
                  f"{snap['model_id']}", flush=True)
        else:
            say_ruling()
            adapter = adapter_factory()
        if stage == "time":
            res = stages.run_gate_stage(adapter, gate="time", templates_counts=list(TIME_COUNTS), resume=resume_run,
                                        identity_extra=extra, out_root=root,
                                        ckpt_path=time_checkpoint(stages.out_paths("time", root)))
        elif stage == "id":
            res = stages.run_gid_pair_f3(adapter, resume=resume_run, identity_extra=extra,
                                         prior_ckpt=id_prior_checkpoint(stages.out_paths("id", root)), out_root=root)
        elif stage == "qual":
            res = stages.run_gate_stage(adapter, gate="qual", templates_counts=list(QUAL_COUNTS), resume=resume_run,
                                        identity_extra=extra, out_root=root,
                                        prior_ckpt=stage_prior_checkpoint("qual", stages.out_paths("qual", root)))
        else:
            res = stages.run_campaign(adapter, floors=campaign_floors(), launch_counts=dict(CAMPAIGN_LAUNCH_COUNTS),
                                      hour_cap=CAMPAIGN_HOUR_CAP,
                                      prior_ckpt=stage_prior_checkpoint("campaign",
                                                                        stages.out_paths("campaign", root)),
                                      resume=resume_run, identity_extra=extra, out_root=root,
                                      adjudication=rulings["adjudication"], pi_stop=rulings["pi_stop"])
    except SystemExit as e:
        _say(f"STOP: {e}")
        return 4
    return stages.EXIT_CODES[res["status"]]


def run_time(**kw) -> int:
    """G-TIME-F3 (m:293): run_stage for "time"."""
    return run_stage("time", **kw)


def run_id(**kw) -> int:
    """G-ID-F3 (m:295): run_stage for "id"."""
    return run_stage("id", **kw)


def run_qual(**kw) -> int:
    """G-F3 (m:297): run_stage for "qual"."""
    return run_stage("qual", **kw)


def run_campaign(**kw) -> int:
    """The Q-F3 campaign (m:298, m:361): run_stage for "campaign"."""
    return run_stage("campaign", **kw)


def _short(x, n: int = 160) -> str:
    s = x if isinstance(x, str) else repr(x)
    return s if len(s) <= n else s[:n] + "..."


def _lines_prefixed(text: str, opening: str, pre: str) -> str:
    """``text`` with ``pre`` put before every line that opens with ``opening``: the self-test's lock variants edit every
    occurrence at a line's start, not only the first (NOTE-7, closed at the campaign wiring)."""
    return "\n".join((pre + ln) if ln.startswith(opening) else ln for ln in text.split("\n"))


def _selftest(chk) -> None:
    """The driver's integration checks (model-free)."""
    pkg = sorted(p.stem for p in guard.PACKAGE_DIR.glob("*.py") if p.stem not in ("__init__", "testing"))
    chk("mf3_sessions: MODULES lists every mf3 module but the package marker and the test double",
        sorted(MODULES) == pkg, sorted(set(pkg) ^ set(MODULES)))
    labels = {w for p in schedule.roster() for w in p}

    def run(argv):
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            try:
                rc = main(argv)
            except SystemExit as e:
                rc = e.code if isinstance(e.code, int) else 2
        return rc, buf.getvalue() + err.getvalue()

    with tempfile.TemporaryDirectory() as td:
        rc1, out1 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        rc2, out2 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        (Path(td) / "s" / "Q-F3_time_A1.json").write_text("{}")
        rc3, out3 = run(["--build-schedules", "--out", str(Path(td) / "s")])
        rcg, outg = run(["gshape", "--out", str(Path(td) / "g")])
    chk("mf3_sessions: --build-schedules writes 21 files that verify clean, re-runs identically, and refuses a "
        "differing existing file (exit 2)",
        rc1 == 0 and "21 files" in out1 and "verify clean" in out1 and rc2 == 0 and rc3 == 2
        and "SCHEDULE MISMATCH" in out3, (rc1, rc2, rc3))
    committed_ = schedule.verify_schedule_dir()
    chk("mf3_sessions: data/mf3/schedules equals a fresh regeneration byte for byte, manifest included (20 + 1)",
        committed_ == [] and len(list(schedule.DEFAULT_OUT.glob("*.json"))) == 21, committed_[:3])
    chk("mf3_sessions: gshape --out runs G-SHAPE-F3 as a test run -- PASS; stdout is INVOCATION then the summary "
        "lines (counts and hashes, no label)",
        rcg == 0 and outg.startswith("INVOCATION: ") and "G-SHAPE-F3 PASS" in outg
        and "G-SHAPE-F3 test run" in outg and not any(re.search(rf"\b{w}\b", outg) for w in labels), outg[-300:])
    helps = {c: run([c, "--help"]) for c in STAGE_CMDS}
    chk("mf3_sessions: time, id, qual and campaign are wired (WIRED_CMDS), the four STAGE_CMDS, none refused "
        "(REFUSED_CMDS empty); each subcommand's --help exits 0",
        WIRED_CMDS == ("time", "id", "qual", "campaign") == STAGE_CMDS and REFUSED_CMDS == ()
        and all(rc == 0 for rc, _ in helps.values()), {c: rc for c, (rc, _) in helps.items()})
    rc0, out0 = run([])
    chk("mf3_sessions: no action is refused (exit 2) and INVOCATION is the first line",
        rc0 == 2 and out0.startswith("INVOCATION: "))
    rch, outh = run(["hashes"])
    chk("mf3_sessions: hashes prints mf3's package sha256, the eleven m files' (the ten modules and __init__.py) "
        "and the weights binding of record",
        rch == 0 and f"MF3 PACKAGE sha256 {guard.package_sha256_of(guard.PACKAGE_DIR)}" in outh
        and outh.count("M MODULE ") == len(guard.M_HASHED) == 11 and f"revision {gshape.QWEN_REVISION}" in outh, outh[-200:])
    srcs = sorted(guard.PACKAGE_DIR.glob("*.py")) + [REPO / DRIVER_REL]
    cs = guard.check_call_sites([guard.PACKAGE_DIR, REPO / DRIVER_REL])
    with tempfile.TemporaryDirectory() as td:
        planted = Path(td) / "x.py"
        planted.write_text("def f(a):\n    return a.generate('p', 's', cached=True)\n")
        fired = guard.check_call_sites([planted])
    chk("mf3_sessions: the cached-path source guard is clean over mf3 and this driver, and fires on a planted "
        "cached=True", cs == [] and fired != [], cs[:2])
    fb = guard.forbidden_hits(srcs)
    chk("mf3_sessions: no forbidden literal in mf3 or this driver", fb == [], fb[:2])
    ip = guard.import_problems(runtime=True)
    chk("mf3_sessions: the licence's import set holds (static closure and a fresh interpreter, N1)", ip == [], ip[:2])
    m_files = sorted((REPO / "valence_core" / "m").glob("*.py"))
    chk("mf3_sessions: valence_core/m holds 18 files and its package hash is 7756dcf4...49bb -- the OLMo build's "
        "60199b36...feec as moved by the G-ANL-F3 hygiene commit's N12 self-test fix to gcal.py (the seat's ruling, "
        "2026-11-07); the F3 build changes nothing there",
        rs.m_resume.package_sha256_of(REPO / "valence_core" / "m").startswith("7756dcf4") and len(m_files) == 18)
    _selftest_time(chk, labels, run)
    _selftest_id(chk, labels)
    _selftest_qual(chk, labels)
    _selftest_campaign(chk, labels)
    chk("mf3_sessions: the quarantined state-present module is not loaded after the self-test",
        not any(m in sys.modules for m in guard.FORBIDDEN_MODULES))


def _selftest_time(chk, labels, run) -> None:
    """The time wiring's checks (model-free). The cases that can reach the Qwen branch (``time_q``) run with
    ``_load_qwen`` a trap (in the post-load cases, a stand-in returning an object with a model_id),
    stages.run_gate_stage a trap, stages.DEFAULT_OUT a test root, m:267's laptop checklist stubbed and
    build_schedules and run_selftest trapped; the out-root seam call runs with the loader and the stage trapped and
    DEFAULT_OUT a test root; the stub-factory runs (``stub_run``), which run sessions on the stub through the real
    stage, have the loader trapped and DEFAULT_OUT a test root; the constants check calls the real _load_qwen with
    every Qwen route closed. So no case can load the model, run a session on it or write data/mf3, whatever the
    state of the tree or the machine (the review's MINOR-1). The last check asserts how often each trap was
    reached."""
    import ast
    import importlib.util as ilu
    from unittest import mock

    import huggingface_hub as hh
    import huggingface_hub.constants as hfc
    from valence_core.m import corr as m_corr
    from valence_core.mf3 import scaffold as sc_mod
    from valence_core.mf3 import testing

    G = globals()
    real_qs = G["qwen_snapshot"]
    real_committed = stages.committed
    loads: list = []
    stage_calls: list = []
    escapes: list = []

    def t_escape(name):
        # the round-2 review's NOTE 1: main dispatches --selftest and --build-schedules after time's refusal of
        # them; if that refusal regressed, the self-test would recurse or write data/mf3/schedules -- trapped here
        def f(*a, **k):
            escapes.append(name)
            raise SystemExit(f"selftest: {name} was reached from a time invocation")
        return f

    def t_loader():
        loads.append(1)
        raise SystemExit("selftest: the Qwen loader was reached")

    def t_stage(*a, **k):
        stage_calls.append(1)
        raise SystemExit("selftest: the stage was reached")

    def gpatch(name, val):
        # a module global replaced for the duration (the review's NOTE 12: the module dict, not sys.modules)
        return mock.patch.dict(G, {name: val})

    def run3(argv):
        # (rc, stdout, stderr), kept apart: the time path's REFUSED and STOP lines go to stderr (m's _say)
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            try:
                rc = main(argv)
            except SystemExit as e:
                rc = e.code if isinstance(e.code, int) else 2
        return rc, buf.getvalue(), err.getvalue()

    def tree_state(root: Path) -> dict:
        out = {}
        for q in sorted(root.rglob("*")):
            k = str(q.relative_to(root))
            out[k] = ("link", os.readlink(q)) if q.is_symlink() else (
                ("file", hashlib.sha256(q.read_bytes()).hexdigest()) if q.is_file() else ("dir", None))
        return out

    def committed_but(rel_x: str, ret):
        # stages.committed with one path's answer planted; every other path read for real
        return lambda rel, repo=stages.REPO: ret if rel == rel_x else real_committed(rel, repo)

    def labelled(text: str) -> bool:
        return any(re.search(rf"\b{re.escape(w)}\b", text, re.IGNORECASE) for w in labels)

    real_out = stages.DEFAULT_OUT
    data_before = tree_state(real_out) if real_out.is_dir() else {}
    _pool, renders = sc_mod.pool_and_renders()
    lock_cp, lock_blob = stages.committed(TIME_LOCK_FILE)
    prop_sha = hashlib.sha256(stages.PROPOSAL_PATH.read_bytes()).hexdigest()
    tflags = {"proposal_file": stages.PROPOSAL_REL, "lock_file": TIME_LOCK_FILE,
              "analyzer_sha256": hashlib.sha256(stages.ANALYZER_PATH.read_bytes()).hexdigest(),
              "package_sha256": guard.package_sha256_of(guard.PACKAGE_DIR),
              "renders_sha16": m_corr.renders_sha(renders)}
    z64 = "0" * 64

    # --- the identity, from the committed lock ------------------------------------------------------
    ex, ex_probs = time_identity_extra(**tflags)
    lock_text = (lock_blob or b"").decode("utf-8", "replace")
    wl = _WEIGHTS_RX.findall(lock_text)
    chk("mf3_sessions: time's identity_extra from the committed LOCK-m-F3.md -- the proposal's and the lock's sha256 "
        "their committed blobs'; m_module_sha256 the eleven files' as hashed now and as the lock lists them; the "
        "weights its one WEIGHTS line's; reasoning_cap 120 (A-m2 v0.5 §4.1), locked_path uncached; stages._extra "
        "accepts it",
        lock_cp == [] and ex_probs == [] and ex is not None
        and ex["lock_sha256"] == hashlib.sha256(lock_blob).hexdigest() and ex["proposal_sha256"] == prop_sha
        and ex["m_module_sha256"] == dict(sorted(guard.m_module_sha256s().items()))
        and len(set(wl)) == 1 and (ex["weights_revision"], ex["weights_sha256"]) == wl[0][1:]
        and wl[0][0] == QWEN_MODEL_ID and ex["reasoning_cap"] == 120 and ex["locked_path"] == "uncached"
        and "prior_proposal_sha256s" not in ex, (lock_cp, ex_probs))
    planted_m, planted_w = "c" * 64, "d" * 64
    real_w = wl[0][2] if wl else z64
    planted_lock = lock_text.replace(guard.m_module_sha256s()["corr"], planted_m).replace(real_w, planted_w).encode("utf-8")
    with mock.patch.object(stages, "committed", committed_but(TIME_LOCK_FILE, ([], planted_lock))):
        ex_pl, pl_probs = time_identity_extra(**tflags)
        pl_lic = stages.licence_problems(ex_pl, environ={HF_OFFLINE_ENV: "1"}) if ex_pl is not None else ["no extra"]
    chk("mf3_sessions: m_module_sha256 and the weights are read from the lock's committed text, not from the files or "
        "the hub: a lock whose corr.py line and WEIGHTS line name other sha256 gives those values; the licence, run on "
        "that lock, then refuses the corr.py file ((e')) and the weights binding ((g)), and nothing for (f)",
        pl_probs == [] and ex_pl is not None and ex_pl["m_module_sha256"]["corr"] == planted_m
        and ex_pl["weights_sha256"] == planted_w and ex_pl["lock_sha256"] == hashlib.sha256(planted_lock).hexdigest()
        and any("valence_core/m/corr.py: its sha256 (computed now)" in x for x in pl_lic)
        and any("binds differently now" in x for x in pl_lic) and not any("committed text does not name" in x or
                                                                         "no line of its committed text" in x
                                                                         for x in pl_lic),
        (pl_probs, pl_lic[:3]))
    lic_now = stages.licence_problems(ex, environ={HF_OFFLINE_ENV: "1"}) if ex is not None else ["no extra"]
    chk("mf3_sessions: that identity is licensed now (stages.licence_problems (a)-(g), HF_HUB_OFFLINE=1 given): the "
        "proposal and the lock committed, the analyzer, mf3's package, the eleven m files and the weights the ones "
        "the identity and the lock name", lic_now == [], lic_now[:2])
    lock_rev = ex["weights_revision"] if ex is not None else "0" * 40
    fake_snap = {"model_id": QWEN_MODEL_ID, "revision": lock_rev, "snapshot_dir": "<selftest>/snapshots/" + lock_rev,
                 "n_snapshots": 1, "offline": "1"}

    # --- the lock's text, parsed: missing, doubled and other-model forms are refused ----------------
    one = "\n".join(f"| `valence_core/m/{m}.py` | `{v}` |" for m, v in sorted(guard.m_module_sha256s().items()))
    wline = f"- WEIGHTS {QWEN_MODEL_ID} revision {'a' * 40} sha256 {'b' * 64}"
    p_ok = lock_m_modules(one), lock_weights(wline)
    p_missing = lock_m_modules("\n".join(ln for ln in one.splitlines() if "/corr.py" not in ln))
    p_double = lock_m_modules(one + "\n| `valence_core/m/corr.py` | `" + "c" * 64 + "` |")
    p_noline = lock_weights("no weights here")
    p_two = lock_weights(wline + "\n" + wline.replace("b" * 64, "d" * 64))
    p_other = lock_weights(wline.replace(QWEN_MODEL_ID, "other/model"))
    p_glued = lock_weights(wline.replace("- WEIGHTS", "- XWEIGHTS"))
    p_hyph = lock_weights(wline.replace("- WEIGHTS", "- OLD-WEIGHTS"))
    p_digit = lock_weights(wline.replace("- WEIGHTS", "- 2WEIGHTS"))
    p_under = lock_weights(wline.replace("- WEIGHTS", "- _WEIGHTS"))
    chk("mf3_sessions: the lock parsers -- the eleven m files read one sha256 each and the WEIGHTS line its revision "
        "and sha256; refused: an m file named on no line, an m file with two different sha256, no WEIGHTS line (one "
        "glued to a letter, a digit, an underscore or a hyphen before it is none), two different WEIGHTS lines, a "
        "WEIGHTS line for another model",
        p_ok[0][1] == [] and p_ok[0][0] == dict(sorted(guard.m_module_sha256s().items()))
        and p_ok[1] == (("a" * 40, "b" * 64), [])
        and p_missing[0] is None and "valence_core/m/corr.py with no sha256" in p_missing[1][0]
        and p_double[0] is None and "valence_core/m/corr.py with 2 sha256" in p_double[1][0]
        and p_noline[0] is None and "0 distinct WEIGHTS lines" in p_noline[1][0]
        and p_glued[0] is None and "0 distinct WEIGHTS lines" in p_glued[1][0]
        and all(x[0] is None and "0 distinct WEIGHTS lines" in x[1][0] for x in (p_hyph, p_digit, p_under))
        and p_two[0] is None and "2 distinct WEIGHTS lines" in p_two[1][0]
        and p_other[0] is None and "names other/model" in p_other[1][0],
        (p_missing[1][:1], p_double[1][:1], p_noline[1], p_two[1], p_other[1], p_glued[1]))

    # --- the constants against their sources (read, not imported) -----------------------------------
    m_drv = REPO / "scripts" / "m_sessions.py"
    m_tree = ast.parse(m_drv.read_text(encoding="utf-8"))

    def assigned(name: str):
        for n in m_tree.body:
            if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in n.targets):
                if isinstance(n.value, ast.Call) and n.value.args:       # re.compile("...")
                    return ast.literal_eval(n.value.args[0])
                return ast.literal_eval(n.value)
        return None
    qm_src = REPO / "valence_core" / "adapters" / "qwen_mlx.py"
    qm_default = None
    for n in ast.walk(ast.parse(qm_src.read_text(encoding="utf-8"))):
        if isinstance(n, ast.FunctionDef) and n.name == "__init__" and n.args.defaults:
            for a_, d_ in zip(n.args.args[-len(n.args.defaults):], n.args.defaults):
                if a_.arg == "model_id":
                    qm_default = ast.literal_eval(d_)
    try:
        spec = ilu.find_spec("mlx_lm")
    except (ImportError, ValueError):
        spec = None
    mlx_src = (Path(list(spec.submodule_search_locations)[0]) / "utils.py"
               if spec is not None and spec.submodule_search_locations else None)
    dl = ([n for n in ast.walk(ast.parse(mlx_src.read_text(encoding="utf-8")))
           if isinstance(n, ast.FunctionDef) and n.name == "_download"]
          if mlx_src is not None and mlx_src.is_file() else [])
    pats = [ast.literal_eval(n) for n in ast.walk(dl[0]) if isinstance(n, ast.List)] if dl else []
    seen_kw: list = []
    from valence_core import adapters as adapters_pkg
    # the real _load_qwen, with every route to a model closed (the round-3 review's NOTE-2): qwen_or_explain answers,
    # get_adapter refuses, and importing mlx, mlx_lm or jlens_qwen fails (sys.modules entries None)
    def no_adapter(*a, **k):
        raise SystemExit("selftest: get_adapter was reached from _load_qwen")
    with mock.patch.object(adapters_pkg, "qwen_or_explain", lambda *a, **kw: seen_kw.append(kw) or "selftest-adapter"), \
            mock.patch.object(adapters_pkg, "get_adapter", no_adapter), \
            mock.patch.dict(sys.modules, {m_: None for m_ in ("mlx", "mlx.core", "mlx_lm", "jlens_qwen",
                                                              "jlens_qwen.model")}):
        loaded = _load_qwen()
    chk("mf3_sessions: QWEN_MODEL_ID is the model of record (mf3.resume), QwenMLXAdapter's default and m's driver's, "
        "and _load_qwen passes it explicitly; MLX_LM_ALLOW_PATTERNS is mlx_lm.utils._download's default list and m's "
        "driver's; HF_OFFLINE_ENV, TOTALS_RX's pattern and TOTALS_REDACTED are m's driver's, and the redaction "
        "replaces m's old totals form (the form is sealed at its source now; the pattern is kept as m keeps it)",
        QWEN_MODEL_ID == rs.QWEN_MODEL_ID == qm_default == assigned("QWEN_MODEL_ID") == gshape.QWEN_MODEL_ID
        and loaded == "selftest-adapter" and seen_kw == [{"model_id": QWEN_MODEL_ID}]
        and len(pats) == 1 and tuple(pats[0]) == MLX_LM_ALLOW_PATTERNS == assigned("MLX_LM_ALLOW_PATTERNS")
        and HF_OFFLINE_ENV == assigned("HF_OFFLINE_ENV") and TOTALS_RX.pattern == assigned("TOTALS_RX")
        and TOTALS_REDACTED == assigned("TOTALS_REDACTED")
        and redact_totals("x hour_cap_ms_used 5 != the sessions' 6 ms y") == f"x {TOTALS_REDACTED} y",
        (qm_default, pats, seen_kw, assigned("TOTALS_RX")))

    # time's help names each flag with its TIME_FLAG_HELP text, and --resume (the round-3 review's NOTE-5)
    rc_h, out_h, _err_h = run3(["time", "--help"])
    flat_h = "".join(out_h.split())          # argparse wraps help text, breaking at spaces and hyphens
    names_h = {"proposal_file": "proposal", "lock_file": TIME_LOCK_FILE, "analyzer_sha256": "analyzer's sha256",
               "package_sha256": "package_sha256", "renders_sha16": "renders' sha16"}
    chk("mf3_sessions: time --help lists the five flags, each followed by its own TIME_FLAG_HELP text (which names "
        "what the flag carries), and --resume (exit 0)",
        rc_h == 0 and set(TIME_FLAG_HELP) == set(TIME_FLAGS) == set(names_h) and "--resume" in flat_h
        and all(names_h[k] in v for k, v in TIME_FLAG_HELP.items())
        and all(f"--{k.replace('_', '-')}{k.upper()}" + "".join(v.split()) in flat_h for k, v in TIME_FLAG_HELP.items()),
        out_h[-200:])

    # --- the snapshot check over fake hub caches (the hub held offline by its own constant throughout: the round-2
    # review's NOTE 2 -- the real snapshot_download calls below cannot reach the network whatever the code passes)
    with tempfile.TemporaryDirectory() as td, mock.patch.object(hfc, "HF_HUB_OFFLINE", True):
        base = Path(td)
        rev = hashlib.sha1(b"mf3-time-selftest-revision").hexdigest()

        def fake_cache(nm: str, *, ref=rev, snap_rev=rev, drop=(), index=True, extra_snaps=(), stray=False):
            c = base / f"hfcache_{nm}"
            repo_d = c / ("models--" + QWEN_MODEL_ID.replace("/", "--"))
            (repo_d / "refs").mkdir(parents=True)
            if isinstance(ref, bytes):
                (repo_d / "refs" / "main").write_bytes(ref)
            elif ref is not None:
                (repo_d / "refs" / "main").write_text(ref, encoding="utf-8")
            if snap_rev is not None:
                sd = repo_d / "snapshots" / snap_rev
                sd.mkdir(parents=True)
                files = {"config.json": "{}", "tokenizer.json": "{}",
                         "model-00001-of-00002.safetensors": "w1", "model-00002-of-00002.safetensors": "w2"}
                if index is True:
                    files["model.safetensors.index.json"] = json.dumps({"weight_map": {
                        "a": "model-00001-of-00002.safetensors", "b": "model-00002-of-00002.safetensors"}})
                elif index is not None:
                    files["model.safetensors.index.json"] = index
                for f, body in files.items():
                    if f not in drop:
                        (sd / f).write_text(body, encoding="utf-8")
            for x in extra_snaps:
                (repo_d / "snapshots" / x).mkdir(parents=True)
            if stray:
                (repo_d / "snapshots" / "stray.txt").write_text("x", encoding="utf-8")
            return c

        on = {HF_OFFLINE_ENV: "1"}
        cwd_clean = base / "cwd_clean"
        cwd_clean.mkdir()
        cwd_model = base / "cwd_model"
        (cwd_model / QWEN_MODEL_ID).mkdir(parents=True)
        cwd_link = base / "cwd_link"
        (cwd_link / QWEN_MODEL_ID.split("/")[0]).mkdir(parents=True)
        (cwd_link / QWEN_MODEL_ID).symlink_to(base / "nowhere")

        def qs(nm, env=on, cwd=cwd_clean, **kw):
            return real_qs(cache_dir=fake_cache(nm, **kw), environ=env, cwd=cwd)

        sq = {
            "complete": qs("ok"),
            "two snapshots and a stray file": qs("two", extra_snaps=("f" * 40,), stray=True),
            "offline unset": qs("unset", env={}),
            "offline 'true'": qs("true", env={HF_OFFLINE_ENV: "true"}),
            "a local path named like the model id": qs("cwdmodel", cwd=cwd_model),
            "a dangling link named like the model id": qs("cwdlink", cwd=cwd_link),
            "no refs/main": qs("noref", ref=None),
            "refs/main not utf-8": qs("nonutf", ref=b"\xff" * 40),
            "refs/main not hex": qs("badref", ref="main"),
            "refs/main with a newline": qs("nlref", ref=rev + "\n"),
            "no snapshot dir": qs("nosnap", snap_rev="d" * 40),
            "a weight missing": qs("noweight", drop=("model-00002-of-00002.safetensors",)),
            "config missing": qs("nocfg", drop=("config.json",)),
            "tokenizer missing": qs("notok", drop=("tokenizer.json",)),
            "index unreadable": qs("badindex", index="not json"),
            "index without weight_map": qs("nowm", index="{}"),
            "index naming no weight": qs("emptywm", index=json.dumps({"weight_map": {}})),
            "a weight not a plain name": qs("relweight", index=json.dumps({"weight_map": {"a": "../outside.bin"}})),
            "a weight not a string": qs("intweight", index=json.dumps({"weight_map": {"a": 1}})),
        }
        want_sq = {"offline unset": "HF_HUB_OFFLINE is None, not '1'",
                   "offline 'true'": "HF_HUB_OFFLINE is 'true', not '1'",
                   "a local path named like the model id": "mlx_lm loads a local path named like the model id",
                   "a dangling link named like the model id": "mlx_lm loads a local path named like the model id",
                   "no refs/main": "no readable refs/main for", "refs/main not utf-8": "no readable refs/main for",
                   "refs/main not hex": "is not, as raw text, a 40-hex revision",
                   "refs/main with a newline": "is not, as raw text, a 40-hex revision",
                   "no snapshot dir": "but no snapshot directory", "a weight missing": "is incomplete",
                   "config missing": "['config.json'] missing", "tokenizer missing": "['tokenizer.json'] missing",
                   "index unreadable": "model.safetensors.index.json unreadable (JSONDecodeError)",
                   "index without weight_map": "model.safetensors.index.json unreadable (KeyError)",
                   "index naming no weight": "the index names no weight file",
                   "a weight not a plain name": "not a plain file name",
                   "a weight not a string": "not a plain file name"}
        okp, oki = sq["complete"]
        twp, twi = sq["two snapshots and a stray file"]
        bad_sq = {k: v for k, v in sq.items() if k in want_sq
                  and not (v[1] is None and any(want_sq[k] in x for x in v[0]))}
        chk("mf3_sessions: qwen_snapshot over fake hub caches -- a complete snapshot with HF_HUB_OFFLINE=1 is clear (the "
            "model of record, refs/main's revision, the hub's own offline resolution agreeing) and its SNAPSHOT line "
            "names exactly them; two snapshot directories and a stray file count 2; refused, with no info, in 17 "
            "cases: the variable unset or not exactly '1'; a local path or a dangling link named like the model id; "
            "refs/main absent, not UTF-8, not hex, or with a newline; no snapshot directory; a weight, config.json or "
            "tokenizer.json missing; an index unreadable, without weight_map, naming no weight, or naming a weight "
            "that is not a plain file name or not a string",
            okp == [] and oki is not None and oki["model_id"] == QWEN_MODEL_ID and oki["revision"] == rev
            and oki["n_snapshots"] == 1 and oki["offline"] == "1"
            and snapshot_line(oki) == (f"SNAPSHOT {QWEN_MODEL_ID} {rev}: refs/main; {oki['snapshot_dir']}; 1 snapshot(s) "
                                       f"in the model's cache repo; HF_HUB_OFFLINE=1")
            and twp == [] and twi is not None and twi["n_snapshots"] == 2
            and not bad_sq and len(want_sq) == 17 and set(want_sq) == set(sq) - {"complete", "two snapshots and a stray file"},
            (okp, {k: v[0][:1] for k, v in bad_sq.items()}))
        ms_sq = {v: qs(f"mscope_{i}", env={HF_OFFLINE_ENV: "1", "MLXLM_USE_MODELSCOPE": v})
                 for i, v in enumerate(("True", "true", "TRUE", "tRuE"))}
        ms_off = qs("mscope_false", env={HF_OFFLINE_ENV: "1", "MLXLM_USE_MODELSCOPE": "False"})
        chk("mf3_sessions: qwen_snapshot refuses MLXLM_USE_MODELSCOPE 'true' in any letter case ('True', 'true', "
            "'TRUE', 'tRuE'), with no info, each message naming the value; 'False' is clear",
            all(v[1] is None and any(f"MLXLM_USE_MODELSCOPE is {k!r} (mlx_lm tests .lower() == 'true')" in x
                                     for x in v[0]) for k, v in ms_sq.items())
            and ms_off[0] == [] and ms_off[1] is not None, {k: v[0][:1] for k, v in ms_sq.items()})
        # the hub's own offline resolution (m's case, carried): over a cached tree listing, files outside mlx_lm's
        # patterns absent are clear and a pattern file absent is refused by the hub; the hub is called once with the
        # load's model id and mlx_lm's patterns, offline, on the given cache; a resolution elsewhere is refused
        def tree_listed(c, names):
            d = c / ("models--" + QWEN_MODEL_ID.replace("/", "--")) / "trees"
            d.mkdir(parents=True, exist_ok=True)
            (d / f"{rev}.json").write_text(json.dumps({"format_version": 1, "files": {
                n_: {"size": 1, "blob_id": "0" * 40} for n_ in names}}), encoding="utf-8")
            return c
        present = ["config.json", "tokenizer.json", "model.safetensors.index.json",
                   "model-00001-of-00002.safetensors", "model-00002-of-00002.safetensors"]
        h_np = real_qs(cache_dir=tree_listed(fake_cache("tree_np"), present + ["README.md", ".gitattributes"]),
                       environ=on, cwd=cwd_clean)
        h_pat = real_qs(cache_dir=tree_listed(fake_cache("tree_pat"), present + ["chat_template.jinja"]),
                        environ=on, cwd=cwd_clean)
        h_calls: list = []
        h_rec_c = fake_cache("hub_rec")
        real_sd = hh.snapshot_download

        def rec_sd(*a, **k):
            h_calls.append((a, k))
            return real_sd(*a, **k)
        with mock.patch.object(hh, "snapshot_download", rec_sd):
            h_rec = real_qs(cache_dir=h_rec_c, environ=on, cwd=cwd_clean)
        h_other_dir = base / "hub_elsewhere"
        h_other_dir.mkdir()
        with mock.patch.object(hh, "snapshot_download", lambda *a, **k: str(h_other_dir)):
            h_other = real_qs(cache_dir=fake_cache("hub_other"), environ=on, cwd=cwd_clean)

        def boom(*a, **k):
            raise RuntimeError("selftest: the hub refuses")
        with mock.patch.object(hh, "snapshot_download", boom):
            h_boom = real_qs(cache_dir=fake_cache("hub_boom"), environ=on, cwd=cwd_clean)
        chk("mf3_sessions: qwen_snapshot's hub resolution (m's case) -- over a cached tree listing, files outside "
            "mlx_lm's patterns absent are clear and a pattern file absent (chat_template.jinja) is refused "
            "(IncompleteSnapshotError); the hub is called once with the load's model id and mlx_lm's patterns, offline "
            "(local_files_only) on the cache given; a resolution to another directory, or a hub that raises, is refused",
            h_np[0] == [] and h_np[1] is not None and h_pat[1] is None
            and any("the hub's offline resolution with mlx_lm's patterns refuses: IncompleteSnapshotError" in x
                    for x in h_pat[0])
            and h_rec[0] == [] and h_calls == [((QWEN_MODEL_ID,), {"local_files_only": True,
                                                                  "allow_patterns": list(MLX_LM_ALLOW_PATTERNS),
                                                                  "cache_dir": str(h_rec_c)})]
            and h_other[1] is None and any("the hub's offline resolution gives" in x for x in h_other[0])
            and h_boom[1] is None and any("refuses: RuntimeError" in x for x in h_boom[0]),
            (h_np[0][:2], h_pat[0][:2], h_calls[:1], h_other[0][:1], h_boom[0][:1]))
        # the production defaults: huggingface_hub's HF_HUB_CACHE and os.environ, read at call time
        prod_c = fake_cache("prod")
        with mock.patch.object(hfc, "HF_HUB_CACHE", str(prod_c)), mock.patch.dict(os.environ):
            os.environ[HF_OFFLINE_ENV] = "1"
            pd_on = real_qs(cwd=cwd_clean)
            pd_env_given = real_qs(cache_dir=prod_c, environ={}, cwd=cwd_clean)
            os.environ.pop(HF_OFFLINE_ENV, None)
            pd_off = real_qs(cwd=cwd_clean)
        chk("mf3_sessions: qwen_snapshot's production defaults read huggingface_hub's HF_HUB_CACHE and os.environ at "
            "call time (clear with HF_HUB_OFFLINE=1, refused without it; an explicit environ wins)",
            pd_on[0] == [] and pd_on[1] is not None and pd_on[1]["snapshot_dir"].startswith(str(prod_c))
            and pd_off[1] is None and any("HF_HUB_OFFLINE is None" in x for x in pd_off[0])
            and pd_env_given[1] is None, (pd_on[0][:1], pd_off[0][:1]))
        # the working directory: by default the process's (a path named like the model id there refuses); weight names
        # '..', '' and one with a backslash are not plain file names (m's w_default and w_names, carried)
        cwd_d = base / "cwd_default"
        (cwd_d / QWEN_MODEL_ID).mkdir(parents=True)
        here_ = os.getcwd()
        os.chdir(cwd_d)
        try:
            w_default = real_qs(cache_dir=fake_cache("cwd_default"), environ=on)
        finally:
            os.chdir(here_)
        w_names = {nm_: real_qs(cache_dir=fake_cache(f"wname_{i}", index=json.dumps({"weight_map": {"a": nm_}})),
                                environ=on, cwd=cwd_clean) for i, nm_ in enumerate(("..", "", "a\\b"))}
        chk("mf3_sessions: qwen_snapshot's local-path refusal reads the process's working directory by default, and "
            "the weight names '..', '' and one with a backslash are refused as not plain file names",
            w_default[1] is None and any("mlx_lm loads a local path named like the model id" in x for x in w_default[0])
            and all(v[1] is None and any("not a plain file name" in x for x in v[0]) for v in w_names.values()),
            (w_default[0][:1], {k: v[0][:1] for k, v in w_names.items()}))

    # --- the stub path first (its ended checkpoint serves the precheck's ENDED cases below) -----------
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        made: list = []

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            made.append(r)
            return r

        def gate_cells(gate):
            return {(t, j): schedule.gate_schedule(gate, t, schedule.GATE_PLAN_COUNTS[(gate, t)])[j]
                    for t in keys.TEMPLATES for j in range(schedule.GATE_PLAN_COUNTS[(gate, t)])}
        made_ad: list = []

        def stub(interrupt=None):
            def f():
                a = testing.F3Adapter()
                a.load(stages._script_policy("time", gate_cells("time"), None, interrupt), None)
                made_ad.append(a)
                return a
            return f
        gates = base / "gates"
        gates.mkdir()

        def stub_run(root, factory, resume_run=False, *, stage=None):
            # the stub factory's seam, with the loader a trap, the canonical out root a test root and the G-ID
            # artifact's directory a test directory; ``stage`` replaces stages.run_gate_stage (the exit-code case)
            buf, err = io.StringIO(), io.StringIO()
            with contextlib.ExitStack() as st:
                st.enter_context(mock.patch.object(guard, "GATES_DIR", gates))
                st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", base / "default-out"))
                st.enter_context(gpatch("_load_qwen", t_loader))
                if stage is not None:
                    st.enter_context(mock.patch.object(stages, "run_gate_stage", stage))
                st.enter_context(contextlib.redirect_stdout(buf))
                st.enter_context(contextlib.redirect_stderr(err))
                try:
                    rc = run_time(**tflags, resume_run=resume_run, adapter_factory=factory, out_root=root)
                except stages._Interrupt as e:
                    rc = e
            return rc, buf.getvalue(), err.getvalue()
        sroot = fresh("stub")
        rc_s, out_s, err_s = stub_run(sroot, stub())
        ck_p = sroot / "ckpt" / TIME_CKPT_NAME
        ck_s = rs.read_checkpoint(ck_p) if ck_p.is_file() else {}
        chk("mf3_sessions: time on the stub factory (the self-test's seam) runs G-TIME-F3 through stages.run_gate_stage "
            "with TIME_COUNTS -- six sessions, one per template, PASS (exit 0); the checkpoint, the report and the reads "
            "under the test root; no DRIVER or SNAPSHOT line (the Qwen path's); stdout and stderr name no label in any "
            "letter case",
            rc_s == 0 and len(made_ad) == 1 and [r["template"] for r in ck_s.get("sessions", [])] == list(keys.TEMPLATES)
            and (ck_s.get("stage_end") or {}).get("status") == "PASS"
            and (sroot / "reports" / f"{keys.UNIT}_time-r2_report.json").is_file()
            and (sroot / "reports" / f"{keys.UNIT}_time-r2_reads.json").is_file()
            and "DRIVER " not in out_s and "SNAPSHOT " not in out_s and not labelled(out_s + err_s)
            and sum(ln.startswith("time A") for ln in out_s.splitlines()) == 6, (rc_s, err_s[-200:], out_s[-200:]))
        chk("mf3_sessions: time writes the re-run's checkpoint, TIME_CKPT_NAME (Q-F3_time-r2.json), its report and reads "
            "named after it, and never the first run's name (A-m2 v0.5 §4.3)",
            ck_p.name == "Q-F3_time-r2.json" and ck_p.is_file() and not (sroot / "ckpt" / FIRST_RUN_CKPT_NAME).exists()
            and not (sroot / "reports" / f"{keys.UNIT}_time_report.json").exists(),
            sorted(x.name for x in (sroot / "ckpt").iterdir()))
        with gpatch("TIME_CKPT_NAME", FIRST_RUN_CKPT_NAME):
            rc_fr, _o, err_fr = stub_run(fresh("first-run-name"), stub())
            try:
                time_checkpoint(stages.out_paths("time", fresh("first-run-name2")))
                fr_direct = False
            except SystemExit as e:
                fr_direct = "first run's checkpoint" in str(e)
        with gpatch("TIME_REASONING_CAP", 60):
            rc_c60, _o, err_c60 = stub_run(fresh("cap60"), stub())
        chk("mf3_sessions: the driver refuses the first run's checkpoint name as a target (time_checkpoint: a STOP, exit "
            "4, on the stub seam) and a TIME_REASONING_CAP other than 120 (refused before the load, exit 2: the identity "
            "validated as a run on a model, stages._extra; A-m2 v0.5 §4.2: the driver's time at any cap but 120 is "
            "refused)",
            rc_fr == 4 and "first run's checkpoint" in err_fr and fr_direct
            and rc_c60 == 2 and "on a run on a model" in err_c60, (rc_fr, err_fr[-160:], rc_c60, err_c60[-160:]))
        rcs = {flag: stub_run(sroot, stub(), flag) for flag in (False, True)}
        chk("mf3_sessions: time on an ended G-TIME-F3 checkpoint, through the stub factory, is a STOP (exit 4, 'STAGE "
            "ENDED') with or without --resume: the stage refuses it after the factory (a resume never re-runs an "
            "ended stage)", all(v[0] == 4 and "STAGE ENDED" in v[2] for v in rcs.values()), {k: v[0] for k, v in rcs.items()})
        # --resume reaches the stage: a run interrupted in A3 leaves four sessions; without --resume the stage refuses
        # the checkpoint (a STOP, exit 4); with it only A3 and A3s are generated, and the stage ends PASS
        rroot = fresh("resume")
        stop_a3 = lambda t, s, kind, i: t == "A3" and kind == "forced" and i == 0
        made_ad.clear()
        rc_ri, _o, _e = stub_run(rroot, stub(stop_a3))
        ck_ri = rs.read_checkpoint(rroot / "ckpt" / TIME_CKPT_NAME)
        open_ckpt = (rroot / "ckpt" / TIME_CKPT_NAME).read_bytes()
        rc_rn, _o, err_rn = stub_run(rroot, stub())
        made_ad.clear()
        rc_ry, out_ry, _e = stub_run(rroot, stub(), True)
        ck_ry = rs.read_checkpoint(rroot / "ckpt" / TIME_CKPT_NAME)
        n_calls = len(made_ad[0].calls) if made_ad else None
        chk("mf3_sessions: time --resume reaches the stage -- a stub run interrupted in A3 leaves A1-A2s recorded; "
            "without --resume the stage refuses the checkpoint (exit 4, 'CHECKPOINT EXISTS'); with it only A3 and A3s "
            "are launched and the stage ends PASS (exit 0)",
            isinstance(rc_ri, stages._Interrupt) and [r["template"] for r in ck_ri["sessions"]] == list(keys.TEMPLATES[:4])
            and rc_rn == 4 and "CHECKPOINT EXISTS" in err_rn and rc_ry == 0
            and [r["template"] for r in ck_ry["sessions"]] == list(keys.TEMPLATES)
            and (ck_ry.get("stage_end") or {}).get("status") == "PASS"
            and sum(ln.startswith("time A") for ln in out_ry.splitlines()) == 2 and n_calls is not None and n_calls > 0,
            (type(rc_ri).__name__, rc_rn, rc_ry, n_calls))
        # the exit code is the stage's status's (stages.EXIT_CODES)
        ex_codes = {st_: stub_run(fresh(f"exit_{st_}"), stub(), stage=lambda *a, _s=st_, **k: {"status": _s})[0]
                    for st_ in ("PASS", "STOP")}
        chk("mf3_sessions: time's exit code is stages.EXIT_CODES of the stage's status (PASS 0, STOP 4)",
            ex_codes == {"PASS": 0, "STOP": 4} == {k: stages.EXIT_CODES[k] for k in ("PASS", "STOP")}, ex_codes)
        ended_ckpt = ck_p.read_bytes()
        # an end pending: a stub run killed after its end was written pending and its outputs, before the end was
        # persisted (m's cut_at_end, carried: the first checkpoint write carrying a stage_end dies)
        from valence_core.m import resume as m_res
        real_w = m_res.write_checkpoint
        cut = {"n": 0}

        def w_cut(path, ck):
            if cut["n"] == 0 and ck.get("stage_end") is not None:
                cut["n"] += 1
                raise stages._Interrupt("selftest: killed before the end was persisted")
            real_w(path, ck)
        proot = fresh("pending")
        with mock.patch.object(m_res, "write_checkpoint", w_cut):
            rc_p, _o, _e = stub_run(proot, stub())
        pend_p = proot / "ckpt" / TIME_CKPT_NAME
        pending_ckpt = pend_p.read_bytes()
        chk("mf3_sessions: a stub run cut between its outputs and its persisted end leaves a checkpoint with an end "
            "pending (rs.pending_at) and not ended (the precheck's pending case below reads it)",
            isinstance(rc_p, stages._Interrupt) and cut["n"] == 1 and rs.pending_at(pend_p)
            and json.loads(pending_ckpt).get("stage_end") is None, (type(rc_p).__name__, cut["n"]))

    # --- the Qwen path with the loader and the stage trapped -------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            return r

        def time_q(nm: str, over: dict | None = None, *, setup=None, pre=(), lic=None, resume_flag=False,
                   argv_pre=(), drv=([], "d" * 64), snap=([], fake_snap), snapfn=None, loader=None, more=(),
                   offline_unset=False):
            # drv / snap: the driver check's and the snapshot check's stubs (None: the real function); snapfn
            # replaces qwen_snapshot outright (a sequence for the pre- and post-load reads); loader replaces the
            # trap (the post-load cases return a stand-in carrying a model_id); stages.run_gate_stage is a trap
            # throughout, stages.DEFAULT_OUT the test root, m:267's laptop checklist stubbed (``pre``)
            root = fresh(nm)
            if setup is not None:
                setup(root)
            before = tree_state(root)
            fl = {**tflags, **(over or {})}
            fl = {k: (str(root / "loop_a.md") if v == "@loop" else v) for k, v in fl.items()}
            argv = list(argv_pre) + ["time"] + [x for k, v in fl.items() if v is not None
                                                for x in ("--" + k.replace("_", "-"), v)]
            n0, s0 = len(loads), len(stage_calls)
            with contextlib.ExitStack() as st:
                st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", root))
                st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage))
                st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: list(pre)))
                st.enter_context(gpatch("_load_qwen", t_loader if loader is None else loader))
                st.enter_context(gpatch("build_schedules", t_escape("build_schedules")))
                st.enter_context(gpatch("run_selftest", t_escape("run_selftest")))
                if drv is not None:
                    st.enter_context(gpatch("driver_problems", lambda: (list(drv[0]), drv[1])))
                if snapfn is not None:
                    st.enter_context(gpatch("qwen_snapshot", snapfn))
                elif snap is not None:
                    st.enter_context(gpatch("qwen_snapshot", lambda: (list(snap[0]), snap[1])))
                if lic is not None:
                    st.enter_context(mock.patch.object(stages, "licence_problems", lambda extra, **kw: list(lic)))
                for obj, attr, val in more:
                    st.enter_context(gpatch(attr, val) if obj is None else mock.patch.object(obj, attr, val))
                if offline_unset:
                    st.enter_context(mock.patch.dict(os.environ))
                    os.environ.pop(HF_OFFLINE_ENV, None)
                rc_, out_, err_ = run3(argv + (["--resume"] if resume_flag else []))
            return {"rc": rc_, "out": out_, "err": err_, "loads": len(loads) - n0, "stages": len(stage_calls) - s0,
                    "same": before == tree_state(root)}

        def t_ckpt(root: Path):
            # an open checkpoint: the stub run interrupted in A3 (four sessions recorded, no end)
            cp = root / "ckpt" / TIME_CKPT_NAME
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(open_ckpt)

        def t_pending(root: Path):
            cp = root / "ckpt" / TIME_CKPT_NAME
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(pending_ckpt)

        def t_ended(root: Path):
            cp = root / "ckpt" / TIME_CKPT_NAME
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(ended_ckpt)

        def t_tamper(root: Path):
            f = root / "schedules" / "Q-F3_time_A1s.json"
            f.write_bytes(f.read_bytes().replace(b'"map": 0', b'"map": 1', 1))

        def t_loop(root: Path):
            (root / "loop_a.md").symlink_to(root / "loop_b.md")
            (root / "loop_b.md").symlink_to(root / "loop_a.md")

        def t_ckpt_loop(root: Path):
            d = root / "ckpt"
            d.mkdir(parents=True, exist_ok=True)
            (d / TIME_CKPT_NAME).symlink_to(d / "loop_x.json")
            (d / "loop_x.json").symlink_to(d / TIME_CKPT_NAME)

        def t_first_ended(root: Path):
            # the state at the re-run (A-m2 v0.5 §4.3): the first run's checkpoint, ended, at its own name
            cp = root / "ckpt" / FIRST_RUN_CKPT_NAME
            cp.parent.mkdir(parents=True, exist_ok=True)
            cp.write_bytes(ended_ckpt)

        def t_first_link(root: Path):
            # the re-run's name a link to the first run's checkpoint (the build review's finding 10)
            t_first_ended(root)
            (root / "ckpt" / TIME_CKPT_NAME).symlink_to(root / "ckpt" / FIRST_RUN_CKPT_NAME)

        lock_prefix_only = ([], f"the proposal {prop_sha[:16]}... and nothing else\n".encode())
        snap_bad = lambda: real_qs(cache_dir=base / "no-cache-here", environ={HF_OFFLINE_ENV: "1"}, cwd=base)
        t_refused = {
            "missing": (time_q("missing", {"lock_file": None}), "time needs ['--lock-file']"),
            "outside": (time_q("outside", {"proposal_file": str(base / "outside.md")}), "lies outside the repository"),
            "a looping link": (time_q("loop", {"proposal_file": "@loop"}, setup=t_loop), "lies outside the repository"),
            "a looping link as the lock": (time_q("looplock", {"lock_file": "@loop"}, setup=t_loop),
                                           "lies outside the repository"),
            "uncommitted": (time_q("uncommitted", {"proposal_file": "no-such-proposal.md"}), "not committed at HEAD"),
            "other lock": (time_q("otherlock", {"lock_file": "CLAUDE.md"}), "G-TIME-F3 cites LOCK-m-F3.md"),
            "proposal not in lock": (time_q("propnotinlock", {"proposal_file": "CLAUDE.md"}),
                                     "is not named in full in LOCK-m-F3.md's committed text"),
            "lock names the proposal by sha16 only": (time_q("propprefix", more=(
                (stages, "committed", committed_but(TIME_LOCK_FILE, lock_prefix_only)),)),
                "is not named in full in LOCK-m-F3.md's committed text"),
            "a lock-named non-proposal": (time_q("nonprop", {"proposal_file": "data/mf3/schedules/manifest.json"}, lic=[]),
                                          "startup: banner"),
            "malformed": (time_q("malformed", {"analyzer_sha256": "xyz"}), "analyzer_sha256 must be a sha256 hex digest"),
            "licence (d)": (time_q("lic_d", {"analyzer_sha256": z64}), "is not identity_extra's analyzer_sha256"),
            "licence (e)": (time_q("lic_e", {"package_sha256": z64}), "is not identity_extra's package_sha256"),
            "licence (f)": (time_q("lic_f", {"analyzer_sha256": z64}), "does not name analyzer_sha256"),
            "licence (g), offline": (time_q("lic_g", offline_unset=True), "licence: weights: HF_HUB_OFFLINE is None"),
            "renders": (time_q("renders", {"renders_sha16": "0" * 16}, lic=[]), "renders: RENDERS MISMATCH"),
            "preflight": (time_q("preflight", lic=[], pre=("ONE PROCESS: selftest",)), "preflight: ONE PROCESS: selftest"),
            "exists": (time_q("exists", lic=[], setup=t_ckpt), "checkpoint: CHECKPOINT EXISTS"),
            "ended": (time_q("ended", lic=[], setup=t_ended), "checkpoint: STAGE ENDED"),
            "ended --resume": (time_q("ended_r", lic=[], setup=t_ended, resume_flag=True), "checkpoint: STAGE ENDED"),
            "the re-run's name a link to the first run's checkpoint": (time_q("firstlink", lic=[], setup=t_first_link),
                                                                       "first run's checkpoint"),
            "a looping link at the checkpoint": (time_q("ckloop", lic=[], setup=t_ckpt_loop),
                                                 "checkpoint: the checkpoint path does not resolve"
                                                 if sys.version_info < (3, 13) else "checkpoint: CHECKPOINT EXISTS"),
            "schedules": (time_q("sched", lic=[], setup=t_tamper), "schedules: SCHEDULES NOT CLEAN"),
            "startup": (time_q("startup", lic=[], more=((stages, "startup_problems",
                                                         lambda proposal_path=None: ["selftest startup"]),)),
                        "startup: selftest startup"),
            "gate line": (time_q("gl", lic=[], more=((stages, "gate_line",
                                                       lambda name, proposal_path=None: ("GATE x", ["GATE LINE: selftest"])),)),
                          "gate line: GATE LINE: selftest"),
            "gate line analyzer": (time_q("gl_an", lic=[], more=((stages, "ANALYZER_PATH", base / "nope.py"),)),
                                   "gate line: analyzer"),
            "gate line CLAUDE.md": (time_q("gl_cm", lic=[], more=((stages, "committed", committed_but(
                "CLAUDE.md", (["CLAUDE.md: selftest uncommitted"], None))),)), "gate line: CLAUDE.md CLAUDE.md: selftest"),
            "driver": (time_q("driver", lic=[], drv=(["selftest: uncommitted edits"], None)),
                       "driver: selftest: uncommitted edits"),
            "driver (real check)": (time_q("driver_real", lic=[], drv=None, more=(
                (stages, "committed", committed_but(DRIVER_REL, (["selftest: driver uncommitted"], None))),
                (None, "__file__", str(REPO / DRIVER_REL)))), "driver: selftest: driver uncommitted"),
            "driver (a copy running)": (time_q("driver_copy", lic=[], drv=None, more=((None, "__file__",
                                                                                       str(base / "copy.py")),)),
                                        "driver: this process runs"),
            "driver (a same-name copy elsewhere)": (time_q("driver_samename", lic=[], drv=None, more=((
                None, "__file__", str(base / "elsewhere" / DRIVER_REL)),)), "driver: this process runs"),
            "snapshot": (time_q("snapshot", lic=[], snap=(["selftest: no snapshot"], None)),
                         "snapshot: selftest: no snapshot"),
            "snapshot (real check)": (time_q("snapshot_real", lic=[], snap=None, snapfn=snap_bad),
                                      "snapshot: no readable refs/main"),
            "snapshot revision not the lock's": (time_q("snaprev", lic=[], snap=([], dict(fake_snap, revision="e" * 40))),
                                                 "not the lock's weights revision"),
            "top-level --out": (time_q("topout", lic=[], argv_pre=("--out", str(base / "x"))),
                                "time takes no --selftest / --build-schedules / --out"),
            "--selftest": (time_q("topsel", lic=[], argv_pre=("--selftest",)),
                           "time takes no --selftest / --build-schedules / --out"),
            "--build-schedules": (time_q("topbuild", lic=[], argv_pre=("--build-schedules",)),
                                  "time takes no --selftest / --build-schedules / --out"),
        }
        bad_t = {k: (v[0]["rc"], v[0]["err"][-240:]) for k, v in t_refused.items()
                 if not (v[0]["rc"] == 2 and any(x in v[0]["err"] for x in (v[1] if isinstance(v[1], tuple) else (v[1],)))
                         and "refused" in v[0]["err"].lower()
                         and "refused" not in v[0]["out"].lower() and v[0]["loads"] == 0 and v[0]["stages"] == 0
                         and "DRIVER " not in v[0]["out"] and "SNAPSHOT " not in v[0]["out"]
                         and not (k.startswith("ended") and "CHECKPOINT EXISTS" in v[0]["err"])
                         and v[0]["same"] and not labelled(v[0]["out"] + v[0]["err"]))}
        chk(f"mf3_sessions: time refuses before the load (exit 2, the refusal on stderr and not stdout, no DRIVER or "
            f"SNAPSHOT line, the loader and the stage never reached, the test root unchanged, no label printed) in "
            f"{len(t_refused)} cases: a flag "
            f"missing; a file outside the repository, a looping link as the proposal or the lock, or uncommitted; a "
            f"lock other than LOCK-m-F3.md; "
            f"a proposal the lock does not name, or names by its sha16 only; a lock-named file that is not a proposal; "
            f"a malformed hash; the licence's (d), (e), (f) and (g)'s offline condition; the renders; m:267's "
            f"checklist; an existing checkpoint without --resume; an ENDED one, with or without --resume (with no "
            f"CHECKPOINT EXISTS advice); the re-run's checkpoint name a link to the first run's checkpoint (A-m2 "
            f"v0.5 §4.3); a looping "
            f"link at the checkpoint path; a tampered schedule; the run-time known answers; the gate line's own "
            f"problems, its analyzer, and CLAUDE.md uncommitted; the driver check, stubbed, real, and on a copy "
            f"running (another name, or the driver's own name elsewhere); the snapshot check, stubbed and real, and a "
            f"snapshot revision not the lock's; a top-level --out, --selftest or --build-schedules beside time (m's "
            f"form, exactly, on stderr; the schedules writer and the self-test never reached)",
            not bad_t and len(t_refused) == 36 and not escapes
            and all(t_refused[k][0]["err"] == "refused: time takes no --selftest / --build-schedules / --out\n"
                    for k in ("top-level --out", "--selftest", "--build-schedules")), (bad_t, escapes))
        multi = time_q("multi", {"renders_sha16": "0" * 16}, lic=["selftest licence"], pre=("ONE PROCESS: selftest",),
                       drv=(["selftest: uncommitted edits"], None), snap=(["selftest: no snapshot"], None))
        ref_lines = [ln for ln in multi["err"].splitlines() if ln.startswith("REFUSED")]
        chk("mf3_sessions: the precheck's problems (the licence's, the renders', m:267's checklist's), the driver "
            "check's and the snapshot check's are refused together, in one REFUSED line naming the stage (exit 2; no "
            "DRIVER or SNAPSHOT line; nothing loaded; m's multi case)",
            multi["rc"] == 2 and len(ref_lines) == 1 and multi["err"].count("REFUSED: G-TIME-F3:") == 1
            and all(x in ref_lines[0] for x in (
                "licence: selftest licence", "renders: RENDERS MISMATCH", "preflight: ONE PROCESS: selftest",
                "driver: selftest: uncommitted edits", "snapshot: selftest: no snapshot"))
            and "DRIVER " not in multi["out"] and "SNAPSHOT " not in multi["out"] and multi["loads"] == 0, ref_lines)
        # the out root seam: given without a factory, refused before anything -- with the traps in place
        n0, s0 = len(loads), len(stage_calls)
        e_ = io.StringIO()
        with contextlib.ExitStack() as st:
            st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", fresh("seam_default")))
            st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage))
            st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: []))
            st.enter_context(gpatch("_load_qwen", t_loader))
            st.enter_context(contextlib.redirect_stderr(e_))
            st.enter_context(contextlib.redirect_stdout(io.StringIO()))
            rc_or = run_time(**{**tflags, "lock_file": "CLAUDE.md"}, resume_run=False, out_root=fresh("seam"))
        chk("mf3_sessions: run_time with an out root and no stub factory refuses before anything -- before the identity "
            "(given a lock the identity would refuse, the refusal is the out root's) -- exit 2, the loader and the "
            "stage, trapped, never reached: the Qwen run writes data/mf3 only",
            rc_or == 2 and "an out root names a test directory" in e_.getvalue() and "cites" not in e_.getvalue()
            and len(loads) == n0 and len(stage_calls) == s0, e_.getvalue()[-200:])
        # every pre-load check clear: the DRIVER and SNAPSHOT lines on stdout, then the trapped loader (a STOP, exit 4)
        rl = time_q("reach_load", lic=[])
        lines_l = rl["out"].splitlines()
        drv_i = next((i for i, x in enumerate(lines_l) if x.startswith("DRIVER ")), None)
        snp_i = next((i for i, x in enumerate(lines_l) if x.startswith("SNAPSHOT ")), None)
        chk("mf3_sessions: with every pre-load check clear, time prints on stdout the DRIVER line (the driver's path and "
            "sha256, HEAD, in full) and then the SNAPSHOT line, and only then reaches the loader -- here the trap: STOP "
            "on stderr, exit 4, the stage never reached, the test root unchanged",
            rl["rc"] == 4 and rl["loads"] == 1 and rl["stages"] == 0 and rl["same"] and drv_i is not None
            and snp_i is not None and drv_i < snp_i
            and lines_l[drv_i] == f"DRIVER {DRIVER_REL} {'d' * 64}: committed at HEAD {stages._git_head()}, working tree identical"
            and lines_l[snp_i] == snapshot_line(fake_snap) and "STOP: selftest: the Qwen loader was reached" in rl["err"]
            and "STOP" not in rl["out"], (rl["rc"], rl["loads"], rl["err"][-200:]))
        ra = time_q("abs_paths", {"proposal_file": str(REPO / stages.PROPOSAL_REL), "lock_file": str(REPO / TIME_LOCK_FILE)},
                    lic=[])
        rr = time_q("resume_open", lic=[], setup=t_ckpt, resume_flag=True)
        rp = time_q("pending", lic=[], setup=t_pending)
        rf = time_q("first_beside", lic=[], setup=t_first_ended)
        chk("mf3_sessions: absolute flag paths inside the repository are accepted (the identity takes their repo-relative "
            "form); --resume lets an existing open checkpoint through the precheck; a checkpoint with an end "
            "pending passes without --resume (it only re-finishes); and the first run's ended checkpoint at its own "
            "name beside the re-run's (A-m2 v0.5 §4.3: the state at the re-run) passes, its bytes untouched: each "
            "reaches the loader (the trap; exit 4)",
            all(x["rc"] == 4 and x["loads"] == 1 and x["stages"] == 0 and "the Qwen loader was reached" in x["err"]
                for x in (ra, rr, rp, rf)) and rf["same"], [(x["rc"], x["err"][-120:]) for x in (ra, rr, rp, rf)])

        # after the load: the order, the re-read, the revision and the model id
        class Stand:
            def __init__(self, mid):
                self.model_id = mid
        order: list = []

        def seq(*answers):
            it = iter(answers)

            def f():
                order.append("snap")
                return next(it)
            return f

        def stand_loader(mid=QWEN_MODEL_ID):
            def f():
                order.append("load")
                return Stand(mid)
            return f
        moved = dict(fake_snap, revision="e" * 40)
        post = {
            "re-read refuses": (time_q("post_refuse", lic=[], loader=stand_loader(),
                                       snapfn=seq(([], fake_snap), (["selftest: gone"], None))),
                                ("STOP: SNAPSHOT RE-READ REFUSED", "selftest: gone")),
            "refs/main moved": (time_q("post_moved", lic=[], loader=stand_loader(),
                                       snapfn=seq(([], fake_snap), ([], moved))),
                                ("STOP: SNAPSHOT MOVED", f"before the load {lock_rev}; after it {'e' * 40}")),
            "another model id": (time_q("post_mid", lic=[], loader=stand_loader("other/model"),
                                        snapfn=seq(([], fake_snap), ([], fake_snap))),
                                 ("STOP: MODEL ID", f"the adapter loaded 'other/model', the snapshot check read "
                                                    f"'{QWEN_MODEL_ID}'")),
        }
        bad_post = {k: (v[0]["rc"], v[0]["err"][-200:]) for k, v in post.items()
                    if not (v[0]["rc"] == 4 and all(x in v[0]["err"] for x in v[1]) and v[0]["stages"] == 0
                            and v[0]["same"] and "SNAPSHOT re-read after the load: unchanged" not in v[0]["out"])}
        order.clear()
        ru = time_q("post_ok", lic=[], loader=stand_loader(), snapfn=seq(([], fake_snap), ([], fake_snap)))
        chk("mf3_sessions: after the load, a re-read that refuses, a moved refs/main or another model id STOPs (exit 4) "
            "before the stage, each STOP naming its evidence (the re-read's problems; both revisions, in order; both "
            "model ids), with no re-read line; with the snapshot unchanged and the model of record, the order is "
            "snapshot, load, "
            "re-read, the re-read line is printed and the stage is reached (here the trap)",
            not bad_post and ru["rc"] == 4 and ru["stages"] == 1 and ru["same"] and order == ["snap", "load", "snap"]
            and f"SNAPSHOT re-read after the load: unchanged ({lock_rev}); adapter model_id {QWEN_MODEL_ID}" in ru["out"]
            and "STOP: selftest: the stage was reached" in ru["err"], (bad_post, ru["rc"], order, ru["err"][-200:]))
        # the real driver check on this file
        dp, dsha = driver_problems()
        cp_d, blob_d = stages.committed(DRIVER_REL)
        here_ok = Path(__file__).resolve() == (REPO / DRIVER_REL).resolve()
        chk("mf3_sessions: driver_problems on this driver -- clear with the committed blob's sha256 exactly when this "
            "process runs the driver of record and its working tree is HEAD's; else its problems and no sha",
            (dp == [] and here_ok and cp_d == [] and blob_d is not None and dsha == hashlib.sha256(blob_d).hexdigest())
            or (dp != [] and dsha is None and (not here_ok or cp_d != [])), (dp[:1], cp_d[:1], here_ok))
    data_after = tree_state(real_out) if real_out.is_dir() else {}
    chk("mf3_sessions: the time checks loaded nothing and wrote nothing under data/mf3 -- the loader trap was reached "
        "5 times in all (each of the five cases that clear every pre-load check asserts its own one reach), the stage "
        "trap once (the post-load case that reaches it), the schedules writer and the self-test never from a time "
        "invocation; data/mf3's file "
        "hashes are unchanged and stages.DEFAULT_OUT is restored",
        data_before == data_after and stages.DEFAULT_OUT == real_out and len(loads) == 5 and len(stage_calls) == 1
        and not escapes, (len(loads), len(stage_calls), escapes, sorted(set(data_before) ^ set(data_after))[:3]))


def _selftest_id(chk, labels) -> None:
    """The id wiring's checks (model-free), in _selftest_time's forms. The stub-factory runs (``stub_run``: G-TIME-F3's
    re-run checkpoint written first by run_time on the stub at the same test root, then run_id) have the loader
    trapped, stages.DEFAULT_OUT a test root and guard.GATES_DIR a test directory per run. The cases that can reach the
    Qwen branch (``id_q``) run with _load_qwen a trap (in the post-load case a stand-in carrying a model_id),
    stages.run_gid_pair_f3 and stages.run_gate_stage traps, stages.DEFAULT_OUT a test root and guard.GATES_DIR beside
    it, m:267's laptop checklist stubbed, and build_schedules and run_selftest trapped. So no case can load the model,
    run a session on it or write data/mf3. The last check asserts how often each trap was reached."""
    from unittest import mock

    from valence_core.m import corr as m_corr
    from valence_core.m import resume as m_res
    from valence_core.mf3 import scaffold as sc_mod
    from valence_core.mf3 import testing

    G = globals()
    loads: list = []
    stage_calls: list = []
    escapes: list = []
    gid_name, ck_name = f"{keys.UNIT}_G-ID.json", f"{keys.UNIT}_id.json"

    def t_escape(name):
        def f(*a, **k):
            escapes.append(name)
            raise SystemExit(f"selftest: {name} was reached from an id invocation")
        return f

    def t_loader():
        loads.append(1)
        raise SystemExit("selftest: the Qwen loader was reached")

    def t_stage(tag):
        def f(*a, **k):
            stage_calls.append((tag, k))
            raise SystemExit("selftest: the stage was reached")
        return f

    def gpatch(name, val):
        return mock.patch.dict(G, {name: val})

    def run3(argv):
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            try:
                rc = main(argv)
            except SystemExit as e:
                rc = e.code if isinstance(e.code, int) else 2
        return rc, buf.getvalue(), err.getvalue()

    def tree_state(root: Path) -> dict:
        out = {}
        for q in sorted(root.rglob("*")):
            k = str(q.relative_to(root))
            out[k] = ("link", os.readlink(q)) if q.is_symlink() else (
                ("file", hashlib.sha256(q.read_bytes()).hexdigest()) if q.is_file() else ("dir", None))
        return out

    def labelled(text: str) -> bool:
        return any(re.search(rf"\b{re.escape(w)}\b", text, re.IGNORECASE) for w in labels)

    real_out, real_gates = stages.DEFAULT_OUT, guard.GATES_DIR
    data_before = tree_state(real_out) if real_out.is_dir() else {}
    _pool, renders = sc_mod.pool_and_renders()
    prop_sha = hashlib.sha256(stages.PROPOSAL_PATH.read_bytes()).hexdigest()
    tflags = {"proposal_file": stages.PROPOSAL_REL, "lock_file": TIME_LOCK_FILE,
              "analyzer_sha256": hashlib.sha256(stages.ANALYZER_PATH.read_bytes()).hexdigest(),
              "package_sha256": guard.package_sha256_of(guard.PACKAGE_DIR),
              "renders_sha16": m_corr.renders_sha(renders)}
    z64 = "0" * 64

    # --- the identity, from the committed lock: time's, with no locked_path ---------------------------
    ex_t, pt = stage_identity_extra("time", **tflags)
    ex_i, pi = stage_identity_extra("id", **tflags)
    ex_w, pw = time_identity_extra(**tflags)
    chk("mf3_sessions: id's identity_extra from the committed LOCK-m-F3.md is time's without locked_path -- the same "
        "proposal, lock, analyzer, package, renders, m files and weights; reasoning_cap 120 (ID_REASONING_CAP, the cap "
        "of record); stages._extra accepts it for 'id'; time_identity_extra is stage_identity_extra for 'time'; the id "
        "constants are the lock's file and the re-run's checkpoint name",
        pt == pi == pw == [] and ex_i is not None and ex_t is not None and "locked_path" not in ex_i
        and ex_t.get("locked_path") == "uncached" and {k: v for k, v in ex_t.items() if k != "locked_path"} == ex_i
        and ex_i["reasoning_cap"] == ID_REASONING_CAP == sc_mod.CAP_OF_RECORD == 120 and ex_w == ex_t
        and ID_LOCK_FILE == TIME_LOCK_FILE == "LOCK-m-F3.md" and ID_PRIOR_CKPT_NAME == TIME_CKPT_NAME == "Q-F3_time-r2.json",
        (pt, pi, sorted(ex_i or {})))
    with gpatch("ID_REASONING_CAP", 60):
        ex60, p60 = stage_identity_extra("id", **tflags)
    ex_ol, p_ol = stage_identity_extra("id", **{**tflags, "lock_file": "CLAUDE.md"})
    # the not-wired calls run on a test root with the traps in place (the review's NOTE-2): were a guard dropped, no
    # precheck reads data/mf3 and no load or stage is reached (the final audit counts the traps)
    unwired = []
    with tempfile.TemporaryDirectory() as td_u, contextlib.ExitStack() as st_u:
        u_root = Path(td_u) / "mf3"
        st_u.enter_context(mock.patch.object(stages, "DEFAULT_OUT", u_root))
        st_u.enter_context(mock.patch.object(guard, "GATES_DIR", Path(td_u) / "gates"))
        st_u.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: []))
        st_u.enter_context(mock.patch.object(stages, "run_gid_pair_f3", t_stage("gid")))
        st_u.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage("gate")))
        st_u.enter_context(gpatch("_load_qwen", t_loader))
        st_u.enter_context(contextlib.redirect_stdout(io.StringIO()))
        st_u.enter_context(contextlib.redirect_stderr(io.StringIO()))
        for fn in (lambda: stage_identity_extra("gshape", **tflags),
                   lambda: stage_precheck("gshape", dict(ex_i or {}), resume_run=False, out_root=u_root),
                   lambda: run_stage("gshape", **tflags, resume_run=False)):
            try:
                fn()
                unwired.append(False)
            except ValueError:
                unwired.append(True)
            except SystemExit:
                unwired.append(False)
    chk("mf3_sessions: id's identity refuses a reasoning cap other than 120 (stages._extra, a run on a model) and a lock "
        "other than LOCK-m-F3.md ('G-ID-F3 cites LOCK-m-F3.md'); stage_identity_extra, stage_precheck and run_stage "
        "raise ValueError for a name that is not a wired stage (gshape), before anything is read or run (on a test root, with "
        "the loader and both stages trapped)",
        ex60 is None and any("on a run on a model" in x for x in p60)
        and ex_ol is None and any("G-ID-F3 cites LOCK-m-F3.md" in x for x in p_ol) and unwired == [True, True, True],
        (p60[:1], p_ol[:1], unwired))
    rc_h, out_h, _err_h = run3(["id", "--help"])
    flat_h = "".join(out_h.split())
    chk("mf3_sessions: id --help lists time's five flags, each followed by its TIME_FLAG_HELP text, and --resume, "
        "'continue G-ID-F3's checkpoint' (exit 0)",
        rc_h == 0 and "--resumecontinueG-ID-F3'scheckpoint(skip-only)" in flat_h
        and all(f"--{k.replace('_', '-')}{k.upper()}" + "".join(v.split()) in flat_h for k, v in TIME_FLAG_HELP.items()),
        out_h[-200:])

    # --- the stub path: time then id at the same root --------------------------------------------------
    def cells(gate):
        return {(t, j): schedule.gate_schedule(gate, t, schedule.GATE_PLAN_COUNTS[(gate, t)])[j]
                for t in (keys.GID_TEMPLATES if gate == "id" else keys.TEMPLATES)
                for j in range(schedule.GATE_PLAN_COUNTS[(gate, t)])}
    made_ad: list = []

    def stub(gate, rule=None, interrupt=None):
        def f():
            a = testing.F3Adapter()
            a.load(stages._script_policy(gate, cells(gate), rule, interrupt), None)
            made_ad.append(a)
            return a
        return f

    def stub_run(fn, root, factory, resume_run=False, *, gates):
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.ExitStack() as st:
            st.enter_context(mock.patch.object(guard, "GATES_DIR", gates))
            st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", root.parent / "default-out"))
            st.enter_context(gpatch("_load_qwen", t_loader))
            st.enter_context(contextlib.redirect_stdout(buf))
            st.enter_context(contextlib.redirect_stderr(err))
            try:
                rc = fn(**tflags, resume_run=resume_run, adapter_factory=factory, out_root=root)
            except stages._Interrupt as e:
                rc = e
        return rc, buf.getvalue(), err.getvalue()

    def stub_prior(root):
        g = root.parent / "gates"
        g.mkdir(parents=True, exist_ok=True)
        return stub_run(run_time, root, stub("time"), gates=g)[0]

    with tempfile.TemporaryDirectory() as td:
        base = Path(td)

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            (base / nm / "gates").mkdir()
            return r

        def time_then(nm):
            r = fresh(nm)
            return r, r.parent / "gates", stub_prior(r)

        r_ok, g_ok, rct_ok = time_then("ok")
        made_ad.clear()
        rc_ok, out_ok, err_ok = stub_run(run_id, r_ok, stub("id"), gates=g_ok)
        ck_ok = rs.read_checkpoint(r_ok / "ckpt" / ck_name) if (r_ok / "ckpt" / ck_name).is_file() else {}
        art_ok = json.loads((g_ok / gid_name).read_text(encoding="utf-8")) if (g_ok / gid_name).is_file() else {}
        ident_ok = ck_ok.get("identity") or {}
        chk("mf3_sessions: id on the stub factory after time on the stub at the same root -- G-ID-F3 through "
            "stages.run_gid_pair_f3, its prior the re-run's checkpoint (Q-F3_time-r2.json) by path, recorded in the G-ID "
            "checkpoint: A2s then A3s, uncached then cached at j = 0 each, 2/2 identical, PASS (exit 0); the artifact "
            "PASS at cap 120 in the test gates directory; Q-F3_id.json (stage id, path cached+uncached, cap 120, the "
            "committed lock's and proposal's sha256); its report and reads; four session lines and the STAGE line; no "
            "DRIVER or SNAPSHOT line; no label printed",
            rct_ok == 0 and rc_ok == 0 and len(made_ad) == 1 and art_ok.get("verdict") == "PASS"
            and (art_ok.get("identity") or {}).get("reasoning_cap") == 120
            and [(p["template"], p["j"]) for p in art_ok.get("indices", [])] == [("A2s", 0), ("A3s", 0)]
            and ident_ok.get("stage") == "id" and ident_ok.get("path") == "cached+uncached"
            and ident_ok.get("reasoning_cap") == 120 and ident_ok.get("lock_sha256") == (ex_i or {}).get("lock_sha256")
            and ident_ok.get("proposal_sha256") == prop_sha
            and str((ck_ok.get("prior") or {}).get("checkpoint", "")).endswith("ckpt/" + TIME_CKPT_NAME)
            and (ck_ok.get("prior") or {}).get("status") == "PASS"
            and (ck_ok.get("stage_end") or {}).get("status") == "PASS"
            and (r_ok / "reports" / f"{keys.UNIT}_id_report.json").is_file()
            and (r_ok / "reports" / f"{keys.UNIT}_id_reads.json").is_file()
            and sum(ln.startswith("id A") for ln in out_ok.splitlines()) == 4
            and "STAGE G-ID-F3 PASS path=cached+uncached" in out_ok
            and "DRIVER " not in out_ok and "SNAPSHOT " not in out_ok and not labelled(out_ok + err_ok),
            (rct_ok, rc_ok, err_ok[-200:], art_ok.get("verdict")))
        r_f, g_f, _ = time_then("fail")
        div = lambda t, s, kind, i, call: "Eight." if (call["cached"] and t == "A3s" and kind == "forced" and i == 1) else None
        rc_f, _o, _e = stub_run(run_id, r_f, stub("id", div), gates=g_f)
        art_f = json.loads((g_f / gid_name).read_text(encoding="utf-8")) if (g_f / gid_name).is_file() else {}
        r_n, g_n, _ = time_then("nd")
        cid = cells("id")
        nd = lambda t, s, kind, i, call: (cid[(t, s)]["P"].capitalize() + " wins."
                                          if t == "A2s" and kind == "chosen" and i == 2 else None)
        rc_n, _o, _e = stub_run(run_id, r_n, stub("id", nd), gates=g_n)
        art_n = json.loads((g_n / gid_name).read_text(encoding="utf-8")) if (g_n / gid_name).is_file() else {}
        chk("mf3_sessions: id's exit code is stages.EXIT_CODES of the stage's status -- a scripted divergence (A3s's "
            "cached half, its second forced round) exits 5, FAIL, the artifact FAIL with pairs [True, False]; an A2s "
            "with no complete pair (a label in its third chosen round at every index) exits 6, NOT-DETERMINED after "
            "GATE_MAX indices, the artifact so",
            rc_f == 5 and art_f.get("verdict") == "FAIL" and art_f.get("pairs_identical") == [True, False]
            and rc_n == 6 and art_n.get("verdict") == "NOT-DETERMINED" and len(art_n.get("indices", [])) == schedule.GATE_MAX
            and stages.EXIT_CODES["FAIL"] == 5 and stages.EXIT_CODES["NOT-DETERMINED"] == 6, (rc_f, rc_n))
        r_np = fresh("noprior")
        rc_np, _o, err_np = stub_run(run_id, r_np, stub("id"), gates=r_np.parent / "gates")
        r_fn, g_fn, _ = time_then("firstname")
        with gpatch("ID_PRIOR_CKPT_NAME", FIRST_RUN_CKPT_NAME):
            rc_fn, _o, err_fn = stub_run(run_id, r_fn, stub("id"), gates=g_fn)
        r_lk, g_lk, _ = time_then("firstlink")
        (r_lk / "ckpt" / TIME_CKPT_NAME).rename(r_lk / "ckpt" / FIRST_RUN_CKPT_NAME)
        (r_lk / "ckpt" / TIME_CKPT_NAME).symlink_to(r_lk / "ckpt" / FIRST_RUN_CKPT_NAME)
        rc_lk, _o, err_lk = stub_run(run_id, r_lk, stub("id"), gates=g_lk)
        try:
            id_prior_checkpoint(stages.out_paths("id", r_lk))
            lk_direct = False
        except SystemExit as e:
            lk_direct = "PRIOR PATH REFUSED" in str(e)
        chk("mf3_sessions: on the stub, id with no G-TIME-F3 checkpoint at its root is a STOP (exit 4, 'PRIOR STAGE "
            "ABSENT', the stage's prior_gate); the first run's checkpoint as the prior is refused -- by name "
            "(ID_PRIOR_CKPT_NAME set to Q-F3_time.json) and where the re-run's name is a link to it -- a STOP (exit 4, "
            "'PRIOR PATH REFUSED'); none writes a G-ID checkpoint or an artifact (A-m2 v0.5 §4.3)",
            rc_np == 4 and "STOP: PRIOR STAGE ABSENT" in err_np and rc_fn == 4 and "PRIOR PATH REFUSED" in err_fn
            and rc_lk == 4 and "PRIOR PATH REFUSED" in err_lk and lk_direct
            and not any((r / "ckpt" / ck_name).exists() for r in (r_np, r_fn, r_lk))
            and not any(any(g.iterdir()) for g in (r_np.parent / "gates", g_fn, g_lk)),
            (rc_np, rc_fn, rc_lk, err_fn[-160:]))
        r_rs, g_rs, _ = time_then("resume")
        stop_a3s = lambda t, s, kind, i: t == "A3s" and kind == "forced" and i == 0
        rc_r1, _o, _e = stub_run(run_id, r_rs, stub("id", None, stop_a3s), gates=g_rs)
        # the reads below are guarded (the review's NOTE-3): a failing run fails its check and the block goes on
        ck_rs = r_rs / "ckpt" / ck_name
        ck_r1 = rs.read_checkpoint(ck_rs) if ck_rs.is_file() else {"sessions": []}
        rc_r2, _o, err_r2 = stub_run(run_id, r_rs, stub("id"), gates=g_rs)
        made_ad.clear()
        rc_r3, out_r3, _e = stub_run(run_id, r_rs, stub("id"), True, gates=g_rs)
        ck_r3 = rs.read_checkpoint(ck_rs) if ck_rs.is_file() else {}
        chk("mf3_sessions: id --resume reaches the stage -- a stub run interrupted at A3s's first half leaves A2s's two "
            "halves recorded; without --resume the stage refuses the checkpoint (exit 4, 'CHECKPOINT EXISTS'); with it "
            "only A3s's two halves are launched and G-ID-F3 ends PASS (exit 0)",
            isinstance(rc_r1, stages._Interrupt)
            and sorted((r["template"], r["s"], r["path"]) for r in ck_r1["sessions"]) == [("A2s", 0, "cached"),
                                                                                         ("A2s", 0, "uncached")]
            and rc_r2 == 4 and "CHECKPOINT EXISTS" in err_r2 and rc_r3 == 0 and len(made_ad) == 1
            and sum(ln.startswith("id A3s") for ln in out_r3.splitlines()) == 2
            and not any(ln.startswith("id A2s") for ln in out_r3.splitlines())
            and (ck_r3.get("stage_end") or {}).get("status") == "PASS", (type(rc_r1).__name__, rc_r2, rc_r3))
        # an end pending: a stub G-ID-F3 killed after its outputs and artifact, before its end was persisted (time's
        # cut, carried: the first checkpoint write carrying a stage_end dies)
        real_w = m_res.write_checkpoint
        cut = {"n": 0}

        def w_cut(path, ck):
            if cut["n"] == 0 and ck.get("stage_end") is not None:
                cut["n"] += 1
                raise stages._Interrupt("selftest: killed before the end was persisted")
            real_w(path, ck)
        r_pd, g_pd, _ = time_then("pending")
        with mock.patch.object(m_res, "write_checkpoint", w_cut):
            rc_pd, _o, _e = stub_run(run_id, r_pd, stub("id"), gates=g_pd)
        pend_ckpt = (r_pd / "ckpt" / ck_name).read_bytes() if (r_pd / "ckpt" / ck_name).is_file() else b"{}"
        pend_art = (g_pd / gid_name).read_bytes() if (g_pd / gid_name).is_file() else b""
        chk("mf3_sessions: a stub G-ID-F3 cut between its outputs and its persisted end leaves its artifact and a "
            "checkpoint with an end pending, not ended (the precheck's pending case below reads both)",
            isinstance(rc_pd, stages._Interrupt) and cut["n"] == 1 and rs.pending_at(r_pd / "ckpt" / ck_name)
            and json.loads(pend_ckpt).get("stage_end") is None and pend_art != b"", (type(rc_pd).__name__, cut["n"]))

    # --- the Qwen path with the loader and the stages trapped ------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        rev = (ex_i or {}).get("weights_revision", "0" * 40)
        fake_snap = {"model_id": QWEN_MODEL_ID, "revision": rev, "snapshot_dir": "<selftest>/snapshots/" + rev,
                     "n_snapshots": 1, "offline": "1"}
        no_prior = ((stages, "prior_gate", lambda *a, **k: {}),)

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            (base / nm / "gates").mkdir()
            return r

        def id_q(nm: str, over: dict | None = None, *, setup=None, pre=(), lic=None, resume_flag=False, argv_pre=(),
                 drv=([], "d" * 64), snap=([], fake_snap), snapfn=None, loader=None, more=()):
            root = fresh(nm)
            if setup is not None:
                setup(root)
            before = tree_state(root.parent)
            fl = {**tflags, **(over or {})}
            argv = list(argv_pre) + ["id"] + [x for k, v in fl.items() if v is not None
                                              for x in ("--" + k.replace("_", "-"), v)]
            n0, s0 = len(loads), len(stage_calls)
            with contextlib.ExitStack() as st:
                st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", root))
                st.enter_context(mock.patch.object(guard, "GATES_DIR", root.parent / "gates"))
                st.enter_context(mock.patch.object(stages, "run_gid_pair_f3", t_stage("gid")))
                st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage("gate")))
                st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: list(pre)))
                st.enter_context(gpatch("_load_qwen", t_loader if loader is None else loader))
                st.enter_context(gpatch("build_schedules", t_escape("build_schedules")))
                st.enter_context(gpatch("run_selftest", t_escape("run_selftest")))
                if drv is not None:
                    st.enter_context(gpatch("driver_problems", lambda: (list(drv[0]), drv[1])))
                if snapfn is not None:
                    st.enter_context(gpatch("qwen_snapshot", snapfn))
                elif snap is not None:
                    st.enter_context(gpatch("qwen_snapshot", lambda: (list(snap[0]), snap[1])))
                if lic is not None:
                    st.enter_context(mock.patch.object(stages, "licence_problems", lambda extra, **kw: list(lic)))
                for obj, attr, val in more:
                    st.enter_context(gpatch(attr, val) if obj is None else mock.patch.object(obj, attr, val))
                rc_, out_, err_ = run3(argv + (["--resume"] if resume_flag else []))
            return {"rc": rc_, "out": out_, "err": err_, "loads": len(loads) - n0, "calls": stage_calls[s0:],
                    "same": before == tree_state(root.parent), "root": root}

        def plant_time(*, proposal=prop_sha, cap=120, status="PASS", stub_weights=False, name=TIME_CKPT_NAME):
            # a G-TIME-F3 checkpoint whose provenance carries no stub tag (m's i_real_prior, carried)
            def setup(root):
                cp = root / "ckpt" / name
                cp.parent.mkdir(parents=True, exist_ok=True)
                w = dict(rs.STUB_WEIGHTS) if stub_weights else {"weights_revision": "a" * 40, "weights_sha256": "b" * 64}
                ident = rs.Identity(stage="time", template_set=list(keys.TEMPLATES), lock_sha256="1" * 64,
                                    schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                    n={t: 1 for t in keys.TEMPLATES}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                    backend_identifier="6" * 16, proposal_sha256=proposal, reasoning_cap=cap, **w)
                ck = rs.load_or_init(cp, ident, False)
                rs.append_provenance(ck, rs.provenance_record(
                    {"adapter": "qwen3.6-27b-4bit-mlx", "apparatus": "selftest-planted, no stub tag"}))
                if status is not None:
                    ck["stage_end"] = {"status": status, "fired": [], "adjudication": None}
                rs.write_checkpoint(cp, ck)
            return setup

        def first_link(root):
            plant_time(name=FIRST_RUN_CKPT_NAME)(root)
            (root / "ckpt" / TIME_CKPT_NAME).symlink_to(root / "ckpt" / FIRST_RUN_CKPT_NAME)

        def id_ckpt(status):
            def setup(root):
                cp = root / "ckpt" / ck_name
                cp.parent.mkdir(parents=True, exist_ok=True)
                ident = rs.Identity(stage="id", template_set=list(keys.GID_TEMPLATES), lock_sha256="1" * 64,
                                    schedule_sha256="3" * 64, path="cached+uncached", hour_cap=None,
                                    n={t: 16 for t in keys.GID_TEMPLATES}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                    backend_identifier="6" * 16, proposal_sha256=prop_sha, reasoning_cap=120,
                                    weights_revision="a" * 40, weights_sha256="b" * 64)
                ck = rs.load_or_init(cp, ident, False)
                if status is not None:
                    ck["stage_end"] = {"status": status, "fired": [], "adjudication": None}
                rs.write_checkpoint(cp, ck)
            return setup

        def artifact(root):
            (root.parent / "gates" / gid_name).write_text("{}\n", encoding="utf-8")

        def dangling(root):
            (root.parent / "gates" / gid_name).symlink_to(root.parent / "gates" / "nowhere.json")

        def tamper(root):
            f = root / "schedules" / f"{keys.UNIT}_id_A2s.json"
            f.write_bytes(f.read_bytes().replace(b'"map": 0', b'"map": 1', 1))

        def pending(root):
            (root / "ckpt").mkdir(parents=True, exist_ok=True)
            (root / "ckpt" / ck_name).write_bytes(pend_ckpt)
            (root.parent / "gates" / gid_name).write_bytes(pend_art)

        def prior_loop(root):
            # a looping link at the prior path (time's looping-link case, carried for the prior; the review's NOTE-1)
            d = root / "ckpt"
            d.mkdir(parents=True, exist_ok=True)
            (d / TIME_CKPT_NAME).symlink_to(d / "loop_p.json")
            (d / "loop_p.json").symlink_to(d / TIME_CKPT_NAME)

        def both(*setups):
            def setup(root):
                for s_ in setups:
                    s_(root)
            return setup

        msg_top = "id takes no --selftest / --build-schedules / --out"
        i_refused = {
            "missing": (id_q("missing", {"lock_file": None}), "id needs ['--lock-file']"),
            "outside": (id_q("outside", {"proposal_file": str(base / "outside.md")}), "lies outside the repository"),
            "uncommitted": (id_q("uncommitted", {"proposal_file": "no-such-proposal.md"}), "not committed at HEAD"),
            "other lock": (id_q("otherlock", {"lock_file": "CLAUDE.md"}), "G-ID-F3 cites LOCK-m-F3.md"),
            "proposal not in lock": (id_q("propnotinlock", {"proposal_file": "CLAUDE.md"}),
                                     "is not named in full in LOCK-m-F3.md's committed text"),
            "malformed": (id_q("malformed", {"analyzer_sha256": "xyz"}), "analyzer_sha256 must be a sha256 hex digest"),
            "licence (d)": (id_q("lic_d", {"analyzer_sha256": z64}, more=no_prior), "is not identity_extra's analyzer_sha256"),
            "licence (e)": (id_q("lic_e", {"package_sha256": z64}, more=no_prior), "is not identity_extra's package_sha256"),
            "renders": (id_q("renders", {"renders_sha16": "0" * 16}, lic=[], more=no_prior), "renders: RENDERS MISMATCH"),
            "preflight": (id_q("preflight", lic=[], pre=("ONE PROCESS: selftest",), more=no_prior),
                          "preflight: ONE PROCESS: selftest"),
            "prior absent (real gate)": (id_q("noprior", lic=[]), "prior: PRIOR STAGE ABSENT"),
            "prior on the stub (real gate)": (id_q("stubprior", lic=[], setup=stub_prior), "prior: PRIOR STAGE ON THE STUB"),
            "prior under another proposal (real gate)": (id_q("otherprop", lic=[], setup=plant_time(proposal="2" * 64)),
                                                         "prior: PRIOR STAGE UNDER ANOTHER PROPOSAL"),
            "prior not ended (real gate)": (id_q("notended", lic=[], setup=plant_time(status=None)),
                                            "prior: PRIOR STAGE NOT ENDED"),
            "prior ended STOP (real gate)": (id_q("priorstop", lic=[], setup=plant_time(status="STOP")),
                                             "prior: PRIOR STAGE STOP"),
            "prior at another cap (real gate)": (id_q("prior60", lic=[], setup=plant_time(cap=60, stub_weights=True)),
                                                 "prior: PRIOR STAGE AT ANOTHER CAP"),
            "prior the first run's, its name a link to it": (id_q("priorlink", lic=[], setup=first_link),
                                                             "prior: PRIOR PATH REFUSED"),
            "prior the first run's, by name": (id_q("priorname", lic=[], setup=plant_time(), more=(
                (None, "ID_PRIOR_CKPT_NAME", FIRST_RUN_CKPT_NAME),)), "prior: PRIOR PATH REFUSED"),
            "a looping link at the prior path": (id_q("priorloop", lic=[], setup=prior_loop),
                                                 "prior: the prior checkpoint path does not resolve"
                                                 if sys.version_info < (3, 13) else "prior: PRIOR STAGE ABSENT"),
            "artifact exists": (id_q("art", lic=[], setup=artifact, more=no_prior), "artifact: G-ID ARTIFACT EXISTS"),
            "a dangling link at the artifact path": (id_q("dangle", lic=[], setup=dangling, more=no_prior),
                                                     "artifact: G-ID ARTIFACT EXISTS"),
            "artifact exists, --resume on an open checkpoint": (id_q("art_r", lic=[], setup=both(id_ckpt(None), artifact),
                                                                     resume_flag=True, more=no_prior),
                                                                "artifact: G-ID ARTIFACT EXISTS"),
            "a dangling link at the artifact path, --resume on an open checkpoint": (
                id_q("dangle_r", lic=[], setup=both(id_ckpt(None), dangling), resume_flag=True, more=no_prior),
                "artifact: G-ID ARTIFACT EXISTS"),
            "exists": (id_q("exists", lic=[], setup=id_ckpt(None), more=no_prior), "checkpoint: CHECKPOINT EXISTS"),
            "ended": (id_q("ended", lic=[], setup=id_ckpt("PASS"), more=no_prior), "checkpoint: STAGE ENDED"),
            "ended --resume": (id_q("ended_r", lic=[], setup=id_ckpt("PASS"), resume_flag=True, more=no_prior),
                               "checkpoint: STAGE ENDED"),
            "schedules": (id_q("sched", lic=[], setup=tamper, more=no_prior), "schedules: SCHEDULES NOT CLEAN"),
            "driver": (id_q("driver", lic=[], drv=(["selftest: uncommitted edits"], None), more=no_prior),
                       "driver: selftest: uncommitted edits"),
            "snapshot": (id_q("snapshot", lic=[], snap=(["selftest: no snapshot"], None), more=no_prior),
                         "snapshot: selftest: no snapshot"),
            "snapshot revision not the lock's": (id_q("snaprev", lic=[], snap=([], dict(fake_snap, revision="e" * 40)),
                                                      more=no_prior), "not the lock's weights revision"),
            "top-level --out": (id_q("topout", lic=[], argv_pre=("--out", str(base / "x"))), msg_top),
            "--selftest": (id_q("topsel", lic=[], argv_pre=("--selftest",)), msg_top),
            "--build-schedules": (id_q("topbuild", lic=[], argv_pre=("--build-schedules",)), msg_top),
        }
        bad_i = {k: (v[0]["rc"], v[0]["err"][-240:]) for k, v in i_refused.items()
                 if not (v[0]["rc"] == 2 and v[1] in v[0]["err"] and "refused" in v[0]["err"].lower()
                         and "refused" not in v[0]["out"].lower() and v[0]["loads"] == 0 and not v[0]["calls"]
                         and "DRIVER " not in v[0]["out"] and "SNAPSHOT " not in v[0]["out"]
                         and not (k.startswith("ended") and "CHECKPOINT EXISTS" in v[0]["err"])
                         and v[0]["same"] and not labelled(v[0]["out"] + v[0]["err"]))}
        chk(f"mf3_sessions: id refuses before the load (exit 2, the refusal on stderr and not stdout, no DRIVER or "
            f"SNAPSHOT line, the loader and both stages never reached, the test root and its gates directory unchanged, "
            f"no label printed) in {len(i_refused)} cases: a flag missing; a file outside the repository or "
            f"uncommitted; a lock other than LOCK-m-F3.md; a proposal the lock does not name; a malformed hash; the "
            f"licence's (d) and (e); the renders; m:267's checklist; the prior (the real gate) absent, on the stub, "
            f"under another proposal, not ended, ended STOP, at another cap, and the first run's -- the re-run's name a "
            f"link to it, or the name itself; a looping link at the prior path; a G-ID artifact on disk, or a dangling "
            f"link there, each also under --resume on an open G-ID checkpoint; G-ID-F3's checkpoint "
            f"existing without --resume, or ENDED, with or without it (with no CHECKPOINT EXISTS advice); a tampered "
            f"schedule; the driver check; the snapshot check, and a snapshot revision not the lock's; a top-level "
            f"--out, --selftest or --build-schedules beside id (m's form, exactly, on stderr; the schedules writer and "
            f"the self-test never reached)",
            not bad_i and len(i_refused) == 33 and not escapes
            and all(i_refused[k][0]["err"] == f"refused: {msg_top}\n" for k in ("top-level --out", "--selftest",
                                                                                "--build-schedules")), (bad_i, escapes))
        multi = id_q("multi", {"renders_sha16": "0" * 16}, lic=["selftest licence"], pre=("ONE PROCESS: selftest",),
                     setup=artifact, drv=(["selftest: uncommitted edits"], None), snap=(["selftest: no snapshot"], None))
        ref_lines = [ln for ln in multi["err"].splitlines() if ln.startswith("REFUSED")]
        chk("mf3_sessions: id's precheck problems (the licence's, the renders', the prior's, the artifact's, m:267's "
            "checklist's), the driver check's and the snapshot check's are refused together, in one REFUSED line naming "
            "G-ID-F3 (exit 2; no DRIVER or SNAPSHOT line; nothing loaded)",
            multi["rc"] == 2 and len(ref_lines) == 1 and multi["err"].count("REFUSED: G-ID-F3:") == 1
            and all(x in ref_lines[0] for x in (
                "licence: selftest licence", "renders: RENDERS MISMATCH", "prior: PRIOR STAGE ABSENT",
                "artifact: G-ID ARTIFACT EXISTS", "preflight: ONE PROCESS: selftest",
                "driver: selftest: uncommitted edits", "snapshot: selftest: no snapshot"))
            and "DRIVER " not in multi["out"] and "SNAPSHOT " not in multi["out"] and multi["loads"] == 0, ref_lines)
        # the out root seam (time's case, carried; the review's MINOR-2): given without a factory, refused before
        # anything -- before the identity -- with the traps in place
        n0, s0 = len(loads), len(stage_calls)
        e_ = io.StringIO()
        seam_root = fresh("seam")
        seam_before = tree_state(seam_root.parent)
        with contextlib.ExitStack() as st:
            st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", fresh("seam_default")))
            st.enter_context(mock.patch.object(guard, "GATES_DIR", seam_root.parent / "gates"))
            st.enter_context(mock.patch.object(stages, "run_gid_pair_f3", t_stage("gid")))
            st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage("gate")))
            st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: []))
            st.enter_context(gpatch("_load_qwen", t_loader))
            st.enter_context(contextlib.redirect_stderr(e_))
            st.enter_context(contextlib.redirect_stdout(io.StringIO()))
            rc_or = run_id(**{**tflags, "lock_file": "CLAUDE.md"}, resume_run=False, out_root=seam_root)
        chk("mf3_sessions: run_id with an out root and no stub factory refuses before anything -- before the identity "
            "(given a lock the identity would refuse, the refusal is the out root's) -- exit 2, the loader and both "
            "stages, trapped, never reached, the test root unchanged: the Qwen run writes data/mf3 only (time's seam "
            "case, carried)",
            rc_or == 2 and "REFUSED: id: an out root names a test directory" in e_.getvalue()
            and "cites" not in e_.getvalue() and len(loads) == n0 and len(stage_calls) == s0
            and tree_state(seam_root.parent) == seam_before, e_.getvalue()[-200:])
        # the state at G-ID-F3 (the review's MINOR-3): the first run's checkpoint at its own name beside the re-run's
        rfb = id_q("first_beside", lic=[], setup=both(plant_time(), plant_time(name=FIRST_RUN_CKPT_NAME, cap=60,
                                                                                 stub_weights=True)))
        chk("mf3_sessions: the state at G-ID-F3 (A-m2 v0.5 §4.3) -- the first run's checkpoint at its own name beside "
            "the re-run's -- passes every pre-load check, the real prior gate reading the re-run's: id reaches the "
            "loader (the trap; exit 4), the first run's bytes untouched",
            rfb["rc"] == 4 and rfb["loads"] == 1 and not rfb["calls"] and "the Qwen loader was reached" in rfb["err"]
            and rfb["same"], (rfb["rc"], rfb["err"][-160:]))
        # every pre-load check clear (the real prior gate on a planted G-TIME-F3 that is not the stub's)
        rl = id_q("reach_load", lic=[], setup=plant_time())
        lines_l = rl["out"].splitlines()
        drv_i = next((i for i, x in enumerate(lines_l) if x.startswith("DRIVER ")), None)
        snp_i = next((i for i, x in enumerate(lines_l) if x.startswith("SNAPSHOT ")), None)
        rr = id_q("resume_open", lic=[], setup=lambda r: (plant_time()(r), id_ckpt(None)(r)), resume_flag=True)
        rp = id_q("pending", lic=[], setup=pending, more=no_prior)
        chk("mf3_sessions: with every pre-load check clear -- the real prior gate passing a G-TIME-F3 checkpoint ended "
            "PASS at cap 120 that the stub did not write -- id prints the DRIVER line and then the SNAPSHOT line on stdout "
            "and only then reaches the loader (the trap: STOP on stderr, exit 4, no stage reached, the test root "
            "unchanged); --resume lets an open G-ID checkpoint through, and a checkpoint with an end pending passes "
            "without --resume with its artifact beside it (it only re-finishes): each reaches the loader",
            rl["rc"] == 4 and rl["loads"] == 1 and not rl["calls"] and rl["same"] and drv_i is not None
            and snp_i is not None and drv_i < snp_i
            and lines_l[drv_i] == f"DRIVER {DRIVER_REL} {'d' * 64}: committed at HEAD {stages._git_head()}, working tree identical"
            and lines_l[snp_i] == snapshot_line(fake_snap) and "STOP: selftest: the Qwen loader was reached" in rl["err"]
            and all(x["rc"] == 4 and x["loads"] == 1 and not x["calls"] and "the Qwen loader was reached" in x["err"]
                    and x["same"] for x in (rr, rp)), [(x["rc"], x["err"][-160:]) for x in (rl, rr, rp)])

        class Stand:
            def __init__(self, mid):
                self.model_id = mid
        order: list = []

        def seq(*answers):
            it = iter(answers)

            def f():
                order.append("snap")
                return next(it)
            return f

        def stand_loader():
            order.append("load")
            return Stand(QWEN_MODEL_ID)
        # after the load, for id: a re-read that refuses, a moved refs/main or another model id STOPs before the stage
        # (time's post-load cases, carried; the qual wiring's review, MINOR-1)
        def stand_mid(mid):
            def f():
                order.append("load")
                return Stand(mid)
            return f
        moved = dict(fake_snap, revision="e" * 40)
        post = {
            "re-read refuses": (id_q("post_refuse", lic=[], setup=plant_time(), loader=stand_loader,
                                     snapfn=seq(([], fake_snap), (["selftest: gone"], None))),
                                ("STOP: SNAPSHOT RE-READ REFUSED", "selftest: gone")),
            "refs/main moved": (id_q("post_moved", lic=[], setup=plant_time(), loader=stand_loader,
                                     snapfn=seq(([], fake_snap), ([], moved))),
                                ("STOP: SNAPSHOT MOVED", f"before the load {rev}; after it {'e' * 40}")),
            "another model id": (id_q("post_mid", lic=[], setup=plant_time(), loader=stand_mid("other/model"),
                                      snapfn=seq(([], fake_snap), ([], fake_snap))),
                                 ("STOP: MODEL ID", f"the adapter loaded 'other/model', the snapshot check read "
                                                    f"'{QWEN_MODEL_ID}'")),
        }
        bad_post = {k: (v[0]["rc"], v[0]["err"][-200:]) for k, v in post.items()
                    if not (v[0]["rc"] == 4 and all(x in v[0]["err"] for x in v[1]) and not v[0]["calls"]
                            and v[0]["same"] and "SNAPSHOT re-read after the load: unchanged" not in v[0]["out"])}
        chk("mf3_sessions: after the load, id STOPs (exit 4) before the stage on a re-read that refuses, a moved refs/main "
            "or another model id, each STOP naming its evidence, with no re-read line (time's post-load cases, carried)",
            not bad_post and len(post) == 3, bad_post)
        order.clear()
        ru = id_q("post_ok", lic=[], setup=plant_time(), loader=stand_loader, snapfn=seq(([], fake_snap), ([], fake_snap)))
        call = ru["calls"][0][1] if ru["calls"] else {}
        want_prior = (ru["root"] / "ckpt" / TIME_CKPT_NAME).resolve()
        chk("mf3_sessions: after the load and the re-read (snapshot, load, snapshot), id reaches stages.run_gid_pair_f3 "
            "-- not run_gate_stage -- once, with the prior the re-run's checkpoint at its out root, by path, the out root "
            "stages.DEFAULT_OUT, resume off and the identity without locked_path at cap 120 (here the trap: exit 4)",
            ru["rc"] == 4 and [c[0] for c in ru["calls"]] == ["gid"] and order == ["snap", "load", "snap"]
            and f"SNAPSHOT re-read after the load: unchanged ({rev}); adapter model_id {QWEN_MODEL_ID}" in ru["out"]
            and Path(call.get("prior_ckpt", "")) == want_prior and Path(call.get("out_root", "")) == ru["root"]
            and call.get("resume") is False and "locked_path" not in (call.get("identity_extra") or {"locked_path": 1})
            and (call.get("identity_extra") or {}).get("reasoning_cap") == 120
            and "STOP: selftest: the stage was reached" in ru["err"] and ru["same"], (ru["rc"], order, sorted(call)))
    data_after = tree_state(real_out) if real_out.is_dir() else {}
    chk("mf3_sessions: the id checks loaded nothing and wrote nothing under data/mf3 -- the loader trap was reached 4 "
        "times in all (each of the four cases that clear every pre-load check asserts its own one reach), the stage "
        "trap once (run_gid_pair_f3, the post-load case), the schedules writer and the self-test never from an id "
        "invocation; data/mf3's file hashes are unchanged and stages.DEFAULT_OUT and guard.GATES_DIR are restored",
        data_before == data_after and stages.DEFAULT_OUT == real_out and guard.GATES_DIR == real_gates
        and len(loads) == 4 and [c[0] for c in stage_calls] == ["gid"] and not escapes,
        (len(loads), [c[0] for c in stage_calls], escapes, sorted(set(data_before) ^ set(data_after))[:3]))


def _selftest_qual(chk, labels) -> None:
    """The qual wiring's checks (model-free), in _selftest_id's forms. The stub-factory runs (``stub_run``: G-TIME-F3's
    re-run checkpoint and a G-ID-F3 artifact written first on the stub at the same test root, then run_qual) have the
    loader trapped, stages.DEFAULT_OUT a test root and guard.GATES_DIR a test directory per run. The cases that can
    reach the Qwen branch (``q_q``) run with _load_qwen a trap (in the post-load case a stand-in carrying a model_id),
    stages.run_gate_stage and stages.run_gid_pair_f3 traps, stages.DEFAULT_OUT a test root and guard.GATES_DIR beside
    it, m:267's laptop checklist stubbed, and build_schedules and run_selftest trapped. So no case can load the model,
    run a session on it or write data/mf3. The last check asserts how often each trap was reached."""
    from unittest import mock

    from valence_core.m import corr as m_corr
    from valence_core.m import resume as m_res
    from valence_core.mf3 import scaffold as sc_mod
    from valence_core.mf3 import testing

    G = globals()
    loads: list = []
    stage_calls: list = []
    escapes: list = []
    gid_name, ck_name = f"{keys.UNIT}_G-ID.json", f"{keys.UNIT}_qual.json"

    def t_escape(name):
        def f(*a, **k):
            escapes.append(name)
            raise SystemExit(f"selftest: {name} was reached from a qual invocation")
        return f

    def t_loader():
        loads.append(1)
        raise SystemExit("selftest: the Qwen loader was reached")

    def t_stage(tag):
        def f(*a, **k):
            stage_calls.append((tag, k))
            raise SystemExit("selftest: the stage was reached")
        return f

    def gpatch(name, val):
        return mock.patch.dict(G, {name: val})

    def run3(argv):
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            try:
                rc = main(argv)
            except SystemExit as e:
                rc = e.code if isinstance(e.code, int) else 2
        return rc, buf.getvalue(), err.getvalue()

    def tree_state(root: Path) -> dict:
        out = {}
        for q in sorted(root.rglob("*")):
            k = str(q.relative_to(root))
            out[k] = ("link", os.readlink(q)) if q.is_symlink() else (
                ("file", hashlib.sha256(q.read_bytes()).hexdigest()) if q.is_file() else ("dir", None))
        return out

    def labelled(text: str) -> bool:
        return any(re.search(rf"\b{re.escape(w)}\b", text, re.IGNORECASE) for w in labels)

    real_out, real_gates = stages.DEFAULT_OUT, guard.GATES_DIR
    data_before = tree_state(real_out) if real_out.is_dir() else {}
    _pool, renders = sc_mod.pool_and_renders()
    prop_sha = hashlib.sha256(stages.PROPOSAL_PATH.read_bytes()).hexdigest()
    tflags = {"proposal_file": stages.PROPOSAL_REL, "lock_file": TIME_LOCK_FILE,
              "analyzer_sha256": hashlib.sha256(stages.ANALYZER_PATH.read_bytes()).hexdigest(),
              "package_sha256": guard.package_sha256_of(guard.PACKAGE_DIR),
              "renders_sha16": m_corr.renders_sha(renders)}
    z64 = "0" * 64
    real_committed = stages.committed

    def committed_but(rel_x: str, ret):
        return lambda rel, repo=stages.REPO: ret if rel == rel_x else real_committed(rel, repo)

    # --- the identity, from the committed lock: time's; v0.2's two lines required, at the start of a line ----------
    lock_cp, lock_blob = stages.committed(QUAL_LOCK_FILE)
    lock_text = (lock_blob or b"").decode("utf-8", "replace")
    ex_t, pt = stage_identity_extra("time", **tflags)
    ex_q, pq = stage_identity_extra("qual", **tflags)
    ex_w, pw = time_identity_extra(**tflags)
    chk("mf3_sessions: qual's identity_extra from the committed LOCK-m-F3.md is time's -- the same proposal, lock, "
        "analyzer, package, renders, m files and weights, reasoning_cap 120 (QUAL_REASONING_CAP) and locked_path "
        "uncached (QUAL_LOCKED_PATH, v0.2 §3); stages._extra accepts it for 'qual'; the committed lock carries each of "
        "QUAL_LOCK_LINES at a line's start; QUAL_COUNTS are m:297's counts in §2.4's table order, the committed "
        "schedules' (schedule.GATE_PLAN_COUNTS), 40 sessions, 24 sham",
        lock_cp == [] and pq == pt == pw == [] and ex_q is not None and ex_q == ex_t == ex_w
        and ex_q["locked_path"] == QUAL_LOCKED_PATH == "uncached" and ex_q["reasoning_cap"] == QUAL_REASONING_CAP == 120
        and all(any(ln.startswith(x) for ln in lock_text.splitlines()) for x in QUAL_LOCK_LINES)
        and QUAL_LOCK_FILE == TIME_LOCK_FILE and QUAL_PRIOR_CKPT_NAME == TIME_CKPT_NAME
        and QUAL_COUNTS == tuple((t, schedule.GATE_PLAN_COUNTS[("qual", t)]) for t in keys.TEMPLATES)
        and sum(n for _, n in QUAL_COUNTS) == 40 and sum(n for t, n in QUAL_COUNTS if keys.is_sham(t)) == 24,
        (pq, sorted(ex_q or {})))
    # an earlier blob: the committed text from v0.2's rule on (the re-issue's part and v0.1's); and v0.2 with one line
    # moved off a line's start, indented, or removed (the review's NOTE-2: a line's start, not after whitespace)
    rule = "\n---\n\nWhere the re-issue's or v0.1's text below differs from v0.2"
    earlier = lock_text.split(rule, 1)[1].split("\n", 2)[2] if rule in lock_text else ""
    # (NOTE-7, closed at the campaign wiring: each variant edits every line that opens with the path line, so a lock
    # that restated that line would still lose it at every line's start; the check below asserts none is left)
    moved = _lines_prefixed(lock_text, QUAL_LOCK_LINES[1], "x ")
    indented = _lines_prefixed(lock_text, QUAL_LOCK_LINES[1], "  ")
    dropped = "\n".join(ln for ln in lock_text.splitlines() if not ln.startswith(QUAL_LOCK_LINES[0])) + "\n"
    got = {}
    for nm, txt in (("earlier", earlier), ("moved", moved), ("indented", indented), ("dropped", dropped)):
        with mock.patch.object(stages, "committed", committed_but(QUAL_LOCK_FILE, ([], txt.encode("utf-8")))):
            got[nm] = (stage_identity_extra("qual", **tflags), stage_identity_extra("time", **tflags),
                       stage_identity_extra("id", **tflags))
    chk("mf3_sessions: qual refuses a lock whose committed text lacks v0.2's lines at a line's start -- the earlier blob "
        "(the re-issue's part and v0.1's, as committed below v0.2's rule), the lock with its path line moved off the "
        "line's start or indented (every line opening with it: NOTE-7), and the lock with its cap line removed -- each "
        "'carries no line opening' the line; time and id accept all four (they run under v0.1 and its re-issue)",
        earlier.startswith("# LOCK-m-F3.md — v0.1, re-issued")
        and not any(ln.startswith(QUAL_LOCK_LINES[1]) for ln in (moved + indented).splitlines())
        and all(v[0][0] is None and any("carries no line opening" in x for x in v[0][1]) for v in got.values())
        and all(v[1][0] is not None and v[2][0] is not None for v in got.values()),
        {k: (v[0][1][:1], v[1][1][:1], v[2][1][:1]) for k, v in got.items()})
    # NOTE-7, closed: on a lock that restates the path line at a line's start above v0.2's, the first-occurrence form
    # would move the restatement alone and leave v0.2's line; the line-wise form moves both
    restated = QUAL_LOCK_LINES[1] + " (a restatement above v0.2's, the self-test's)\n" + lock_text
    r_moved = _lines_prefixed(restated, QUAL_LOCK_LINES[1], "x ")
    first_only = restated.replace(QUAL_LOCK_LINES[1], "x " + QUAL_LOCK_LINES[1], 1)
    with mock.patch.object(stages, "committed", committed_but(QUAL_LOCK_FILE, ([], restated.encode("utf-8")))):
        ex_rs, p_rs = stage_identity_extra("qual", **tflags)
    with mock.patch.object(stages, "committed", committed_but(QUAL_LOCK_FILE, ([], r_moved.encode("utf-8")))):
        ex_rm, p_rm = stage_identity_extra("qual", **tflags)
    chk("mf3_sessions: NOTE-7's gap is closed -- on a lock that restates the path line at a line's start above v0.2's, "
        "qual accepts the lock, and the line-wise moved variant leaves no line opening with it and is refused ('carries "
        "no line opening'), where the first-occurrence form would have left v0.2's line in place",
        ex_rs is not None and p_rs == [] and ex_rm is None and any("carries no line opening" in x for x in p_rm)
        and sum(ln.startswith(QUAL_LOCK_LINES[1]) for ln in restated.splitlines()) == 2
        and not any(ln.startswith(QUAL_LOCK_LINES[1]) for ln in r_moved.splitlines())
        and sum(ln.startswith(QUAL_LOCK_LINES[1]) for ln in first_only.splitlines()) == 1, (p_rs[:1], p_rm[:1]))
    # the order (the review's NOTE-3): an earlier blob that also names an m file with a second sha256 is refused for
    # its missing lines, the check the PIN says comes before the m files and the weights are read
    both_bad = earlier + "\n| `valence_core/m/corr.py` | `" + "c" * 64 + "` |\n"
    with mock.patch.object(stages, "committed", committed_but(QUAL_LOCK_FILE, ([], both_bad.encode("utf-8")))):
        ex_bb, p_bb = stage_identity_extra("qual", **tflags)
        ex_bt, p_bt = stage_identity_extra("time", **tflags)
    chk("mf3_sessions: qual's lock-line check comes before the m files and the weights are read -- on an earlier blob "
        "that also names corr.py with a second sha256, qual refuses for the missing lines alone, and time, which "
        "makes no lock-line check, refuses for the doubled sha256",
        ex_bb is None and len(p_bb) == 1 and "carries no line opening" in p_bb[0]
        and ex_bt is None and any("valence_core/m/corr.py with 2 sha256" in x for x in p_bt), (p_bb, p_bt[:1]))
    rc_h, out_h, _err_h = run3(["qual", "--help"])
    flat_h = "".join(out_h.split())
    chk("mf3_sessions: qual --help lists time's five flags, each followed by its TIME_FLAG_HELP text, and --resume, "
        "'continue G-F3's checkpoint' (exit 0)",
        rc_h == 0 and "--resumecontinueG-F3'scheckpoint(skip-only)" in flat_h
        and all(f"--{k.replace('_', '-')}{k.upper()}" + "".join(v.split()) in flat_h for k, v in TIME_FLAG_HELP.items()),
        out_h[-200:])

    # --- the stub path: time, then id (a FAIL artifact), then qual at the same root ---------------------------------
    def cells(gate):
        return {(t, j): schedule.gate_schedule(gate, t, schedule.GATE_PLAN_COUNTS[(gate, t)])[j]
                for t in (keys.GID_TEMPLATES if gate == "id" else keys.TEMPLATES)
                for j in range(schedule.GATE_PLAN_COUNTS[(gate, t)])}
    made_ad: list = []

    def stub(gate, rule=None, interrupt=None):
        def f():
            a = testing.F3Adapter()
            a.load(stages._script_policy(gate, cells(gate), rule, interrupt), None)
            made_ad.append(a)
            return a
        return f

    def stub_run(fn, root, factory, resume_run=False, *, gates, stage=None):
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.ExitStack() as st:
            st.enter_context(mock.patch.object(guard, "GATES_DIR", gates))
            st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", root.parent / "default-out"))
            st.enter_context(gpatch("_load_qwen", t_loader))
            if stage is not None:
                st.enter_context(mock.patch.object(stages, "run_gate_stage", stage))
            st.enter_context(contextlib.redirect_stdout(buf))
            st.enter_context(contextlib.redirect_stderr(err))
            try:
                rc = fn(**tflags, resume_run=resume_run, adapter_factory=factory, out_root=root)
            except stages._Interrupt as e:
                rc = e
        return rc, buf.getvalue(), err.getvalue()

    div = lambda t, s, kind, i, call: "Eight." if (call["cached"] and t == "A3s" and kind == "forced" and i == 1) else None

    def stub_prior(root):
        g = root.parent / "gates"
        g.mkdir(parents=True, exist_ok=True)
        return stub_run(run_time, root, stub("time"), gates=g)[0]

    with tempfile.TemporaryDirectory() as td:
        base = Path(td)

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            (base / nm / "gates").mkdir()
            return r

        def chain(nm, gid_rule=div):
            r = fresh(nm)
            g = r.parent / "gates"
            rct = stub_prior(r)
            rci = stub_run(run_id, r, stub("id", gid_rule), gates=g)[0]
            return r, g, (rct, rci)

        r_ok, g_ok, pre_ok = chain("ok")
        made_ad.clear()
        rc_ok, out_ok, err_ok = stub_run(run_qual, r_ok, stub("qual"), gates=g_ok)
        ckp = r_ok / "ckpt" / ck_name
        ck_ok = rs.read_checkpoint(ckp) if ckp.is_file() else {}
        ident_ok = ck_ok.get("identity") or {}
        art_ok = json.loads((g_ok / gid_name).read_text(encoding="utf-8")) if (g_ok / gid_name).is_file() else {}
        chk("mf3_sessions: qual on the stub factory after time and a FAILed id on the stub at the same root -- G-F3 "
            "through stages.run_gate_stage, its prior the re-run's checkpoint (Q-F3_time-r2.json) by path, recorded, and "
            "the G-ID-F3 FAIL artifact on disk: 40 sessions in the stage's launch order, uncached, PASS (exit 0); "
            "Q-F3_qual.json (stage qual, path uncached, cap 120, the committed lock's and proposal's sha256); its report "
            "and reads; the STAGE line; no DRIVER or SNAPSHOT line; no label printed",
            pre_ok == (0, 5) and art_ok.get("verdict") == "FAIL" and rc_ok == 0 and len(made_ad) == 1
            and ident_ok.get("stage") == "qual" and ident_ok.get("path") == "uncached"
            and ident_ok.get("reasoning_cap") == 120 and ident_ok.get("lock_sha256") == (ex_q or {}).get("lock_sha256")
            and ident_ok.get("proposal_sha256") == prop_sha and ident_ok.get("n") == dict(QUAL_COUNTS)
            and str((ck_ok.get("prior") or {}).get("checkpoint", "")).endswith("ckpt/" + TIME_CKPT_NAME)
            and (ck_ok.get("stage_end") or {}).get("status") == "PASS"
            and len(ck_ok.get("sessions") or []) == 40
            and (r_ok / "reports" / f"{keys.UNIT}_qual_report.json").is_file()
            and (r_ok / "reports" / f"{keys.UNIT}_qual_reads.json").is_file()
            and sum(ln.startswith("qual A") for ln in out_ok.splitlines()) == 40
            and "STAGE G-F3 PASS path=uncached" in out_ok
            and "DRIVER " not in out_ok and "SNAPSHOT " not in out_ok and not labelled(out_ok + err_ok),
            (pre_ok, rc_ok, err_ok[-200:], ident_ok.get("path")))
        # a PASS artifact on this backend: the G-ID licence gives cached, the lock fixes uncached -> PATH MISMATCH
        r_pm, g_pm, pre_pm = chain("pathmismatch", gid_rule=None)
        rc_pm, _o, err_pm = stub_run(run_qual, r_pm, stub("qual"), gates=g_pm)
        r_np = fresh("noprior")
        rc_np, _o, err_np = stub_run(run_qual, r_np, stub("qual"), gates=r_np.parent / "gates")
        r_na = fresh("noartifact")
        rct_na = stub_prior(r_na)
        rc_na, _o, err_na = stub_run(run_qual, r_na, stub("qual"), gates=r_na.parent / "gates")
        r_fn, g_fn, _ = chain("firstname")
        with gpatch("QUAL_PRIOR_CKPT_NAME", FIRST_RUN_CKPT_NAME):
            rc_fn, _o, err_fn = stub_run(run_qual, r_fn, stub("qual"), gates=g_fn)
        chk("mf3_sessions: on the stub, qual STOPs (exit 4) -- on a G-ID-F3 PASS artifact for this backend ('PATH "
            "MISMATCH': the lock fixes uncached, the licence gives cached), with no G-TIME-F3 checkpoint ('PRIOR STAGE "
            "ABSENT'), with no G-ID-F3 artifact ('G-ID ARTIFACT ABSENT'), and with the first run's checkpoint as the "
            "prior ('PRIOR PATH REFUSED'); none writes a G-F3 checkpoint",
            pre_pm == (0, 0) and rc_pm == 4 and "PATH MISMATCH" in err_pm and rc_np == 4
            and "STOP: PRIOR STAGE ABSENT" in err_np and rct_na == 0 and rc_na == 4 and "G-ID ARTIFACT ABSENT" in err_na
            and rc_fn == 4 and "PRIOR PATH REFUSED" in err_fn
            and not any((r / "ckpt" / ck_name).exists() for r in (r_pm, r_np, r_na, r_fn)),
            (rc_pm, rc_np, rc_na, rc_fn, err_pm[-120:]))
        ex_codes = {st_: stub_run(run_qual, chain(f"exit_{st_}")[0], stub("qual"),
                                  gates=base / f"exit_{st_}" / "gates", stage=lambda *a, _s=st_, **k: {"status": _s})[0]
                    for st_ in ("PASS", "STOP")}
        chk("mf3_sessions: qual's exit code is stages.EXIT_CODES of the stage's status (PASS 0, STOP 4)",
            ex_codes == {"PASS": 0, "STOP": 4}, ex_codes)
        r_rs, g_rs, _ = chain("resume")
        stop_a3 = lambda t, s, kind, i: t == "A3" and s == 0 and kind == "forced" and i == 0
        rc_r1, _o, _e = stub_run(run_qual, r_rs, stub("qual", None, stop_a3), gates=g_rs)
        ck_rs = r_rs / "ckpt" / ck_name
        ck_r1 = rs.read_checkpoint(ck_rs) if ck_rs.is_file() else {"sessions": []}
        rc_r2, _o, err_r2 = stub_run(run_qual, r_rs, stub("qual"), gates=g_rs)
        made_ad.clear()
        rc_r3, out_r3, _e = stub_run(run_qual, r_rs, stub("qual"), True, gates=g_rs)
        ck_r3 = rs.read_checkpoint(ck_rs) if ck_rs.is_file() else {}
        chk("mf3_sessions: qual --resume reaches the stage -- a stub run interrupted at A3's first session leaves the "
            "four launched before it (A1, A1s, A2, A2s at s = 0); without --resume the stage refuses the checkpoint "
            "(exit 4, 'CHECKPOINT EXISTS'); with it the other 36 are launched and G-F3 ends PASS (exit 0)",
            isinstance(rc_r1, stages._Interrupt)
            and sorted((r["template"], r["s"]) for r in ck_r1["sessions"]) == [("A1", 0), ("A1s", 0), ("A2", 0), ("A2s", 0)]
            and rc_r2 == 4 and "CHECKPOINT EXISTS" in err_r2 and rc_r3 == 0 and len(made_ad) == 1
            and sum(ln.startswith("qual A") for ln in out_r3.splitlines()) == 36
            and (ck_r3.get("stage_end") or {}).get("status") == "PASS" and len(ck_r3.get("sessions") or []) == 40,
            (type(rc_r1).__name__, rc_r2, rc_r3))
        real_w = m_res.write_checkpoint
        cut = {"n": 0}

        def w_cut(path, ck):
            if cut["n"] == 0 and ck.get("stage_end") is not None:
                cut["n"] += 1
                raise stages._Interrupt("selftest: killed before the end was persisted")
            real_w(path, ck)
        r_pd, g_pd, _ = chain("pending")
        with mock.patch.object(m_res, "write_checkpoint", w_cut):
            rc_pd, _o, _e = stub_run(run_qual, r_pd, stub("qual"), gates=g_pd)
        pend_ckpt = (r_pd / "ckpt" / ck_name).read_bytes() if (r_pd / "ckpt" / ck_name).is_file() else b"{}"
        chk("mf3_sessions: a stub G-F3 cut between its outputs and its persisted end leaves a checkpoint with an end "
            "pending, not ended (the precheck's pending case below reads it)",
            isinstance(rc_pd, stages._Interrupt) and cut["n"] == 1 and rs.pending_at(r_pd / "ckpt" / ck_name)
            and json.loads(pend_ckpt).get("stage_end") is None, (type(rc_pd).__name__, cut["n"]))

    # --- the Qwen path with the loader and the stages trapped ------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        rev = (ex_q or {}).get("weights_revision", "0" * 40)
        fake_snap = {"model_id": QWEN_MODEL_ID, "revision": rev, "snapshot_dir": "<selftest>/snapshots/" + rev,
                     "n_snapshots": 1, "offline": "1"}
        no_prior = ((stages, "prior_gate", lambda *a, **k: {}),)

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            (base / nm / "gates").mkdir()
            return r

        def q_q(nm: str, over: dict | None = None, *, setup=None, pre=(), lic=None, resume_flag=False, argv_pre=(),
                drv=([], "d" * 64), snap=([], fake_snap), snapfn=None, loader=None, more=()):
            root = fresh(nm)
            if setup is not None:
                setup(root)
            before = tree_state(root.parent)
            fl = {**tflags, **(over or {})}
            argv = list(argv_pre) + ["qual"] + [x for k, v in fl.items() if v is not None
                                                for x in ("--" + k.replace("_", "-"), v)]
            n0, s0 = len(loads), len(stage_calls)
            with contextlib.ExitStack() as st:
                st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", root))
                st.enter_context(mock.patch.object(guard, "GATES_DIR", root.parent / "gates"))
                st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage("gate")))
                st.enter_context(mock.patch.object(stages, "run_gid_pair_f3", t_stage("gid")))
                st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: list(pre)))
                st.enter_context(gpatch("_load_qwen", t_loader if loader is None else loader))
                st.enter_context(gpatch("build_schedules", t_escape("build_schedules")))
                st.enter_context(gpatch("run_selftest", t_escape("run_selftest")))
                if drv is not None:
                    st.enter_context(gpatch("driver_problems", lambda: (list(drv[0]), drv[1])))
                if snapfn is not None:
                    st.enter_context(gpatch("qwen_snapshot", snapfn))
                elif snap is not None:
                    st.enter_context(gpatch("qwen_snapshot", lambda: (list(snap[0]), snap[1])))
                if lic is not None:
                    st.enter_context(mock.patch.object(stages, "licence_problems", lambda extra, **kw: list(lic)))
                for obj, attr, val in more:
                    st.enter_context(gpatch(attr, val) if obj is None else mock.patch.object(obj, attr, val))
                rc_, out_, err_ = run3(argv + (["--resume"] if resume_flag else []))
            return {"rc": rc_, "out": out_, "err": err_, "loads": len(loads) - n0, "calls": stage_calls[s0:],
                    "same": before == tree_state(root.parent), "root": root}

        def plant_time(*, proposal=prop_sha, cap=120, status="PASS", stub_weights=False, name=TIME_CKPT_NAME):
            # a G-TIME-F3 checkpoint whose provenance carries no stub tag (m's i_real_prior, carried)
            def setup(root):
                cp = root / "ckpt" / name
                cp.parent.mkdir(parents=True, exist_ok=True)
                w = dict(rs.STUB_WEIGHTS) if stub_weights else {"weights_revision": "a" * 40, "weights_sha256": "b" * 64}
                ident = rs.Identity(stage="time", template_set=list(keys.TEMPLATES), lock_sha256="1" * 64,
                                    schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                    n={t: 1 for t in keys.TEMPLATES}, audit_v2_sha16="4" * 16, ban_sha="5" * 16,
                                    backend_identifier="6" * 16, proposal_sha256=proposal, reasoning_cap=cap, **w)
                ck = rs.load_or_init(cp, ident, False)
                rs.append_provenance(ck, rs.provenance_record(
                    {"adapter": "qwen3.6-27b-4bit-mlx", "apparatus": "selftest-planted, no stub tag"}))
                if status is not None:
                    ck["stage_end"] = {"status": status, "fired": [], "adjudication": None}
                rs.write_checkpoint(cp, ck)
            return setup

        def plant_art(*, verdict="FAIL", cap=120, proposal=prop_sha, stub_tag=False, raw=None):
            # a G-ID-F3 artifact for gid_artifact_problems: its identity's proposal and cap, and its provenance
            def setup(root):
                p = root.parent / "gates" / gid_name
                if raw is not None:
                    p.write_text(raw, encoding="utf-8")
                    return
                tag = stages.STUB_MARK if stub_tag else "selftest-planted, no stub tag"
                p.write_text(json.dumps({"verdict": verdict, "identity": {"proposal_sha256": proposal,
                                                                         "reasoning_cap": cap},
                                         "provenance": [{"record": {"adapter": "qwen3.6-27b-4bit-mlx",
                                                                    "apparatus": tag}, "stamp": "selftest"}]}),
                             encoding="utf-8")
            return setup

        def both(*setups):
            def setup(root):
                for s_ in setups:
                    s_(root)
            return setup

        clear = both(plant_time(), plant_art())

        def first_link(root):
            plant_time(name=FIRST_RUN_CKPT_NAME)(root)
            (root / "ckpt" / TIME_CKPT_NAME).symlink_to(root / "ckpt" / FIRST_RUN_CKPT_NAME)

        def prior_loop(root):
            d = root / "ckpt"
            d.mkdir(parents=True, exist_ok=True)
            (d / TIME_CKPT_NAME).symlink_to(d / "loop_p.json")
            (d / "loop_p.json").symlink_to(d / TIME_CKPT_NAME)

        def q_ckpt(status):
            def setup(root):
                cp = root / "ckpt" / ck_name
                cp.parent.mkdir(parents=True, exist_ok=True)
                ident = rs.Identity(stage="qual", template_set=list(keys.TEMPLATES), lock_sha256="1" * 64,
                                    schedule_sha256="3" * 64, path="uncached", hour_cap=None, n=dict(QUAL_COUNTS),
                                    audit_v2_sha16="4" * 16, ban_sha="5" * 16, backend_identifier="6" * 16,
                                    proposal_sha256=prop_sha, reasoning_cap=120, weights_revision="a" * 40,
                                    weights_sha256="b" * 64)
                ck = rs.load_or_init(cp, ident, False)
                if status is not None:
                    ck["stage_end"] = {"status": status, "fired": [], "adjudication": None}
                rs.write_checkpoint(cp, ck)
            return setup

        def tamper(root):
            f = root / "schedules" / f"{keys.UNIT}_qual_A1s.json"
            f.write_bytes(f.read_bytes().replace(b'"map": 0', b'"map": 1', 1))

        def pending(root):
            (root / "ckpt").mkdir(parents=True, exist_ok=True)
            (root / "ckpt" / ck_name).write_bytes(pend_ckpt)

        earlier_lock = ((stages, "committed", committed_but(QUAL_LOCK_FILE, ([], earlier.encode("utf-8")))),)
        msg_top = "qual takes no --selftest / --build-schedules / --out"
        q_refused = {
            "missing": (q_q("missing", {"lock_file": None}), "qual needs ['--lock-file']"),
            "outside": (q_q("outside", {"proposal_file": str(base / "outside.md")}), "lies outside the repository"),
            "uncommitted": (q_q("uncommitted", {"proposal_file": "no-such-proposal.md"}), "not committed at HEAD"),
            "other lock": (q_q("otherlock", {"lock_file": "CLAUDE.md"}), "G-F3 cites LOCK-m-F3.md"),
            "proposal not in lock": (q_q("propnotinlock", {"proposal_file": "CLAUDE.md"}),
                                     "is not named in full in LOCK-m-F3.md's committed text"),
            "an earlier lock blob (no v0.2 lines)": (q_q("earlierlock", more=earlier_lock), "carries no line opening"),
            "malformed": (q_q("malformed", {"analyzer_sha256": "xyz"}), "analyzer_sha256 must be a sha256 hex digest"),
            "licence (d)": (q_q("lic_d", {"analyzer_sha256": z64}, more=no_prior), "is not identity_extra's analyzer_sha256"),
            "licence (e)": (q_q("lic_e", {"package_sha256": z64}, more=no_prior), "is not identity_extra's package_sha256"),
            "renders": (q_q("renders", {"renders_sha16": "0" * 16}, lic=[], more=no_prior), "renders: RENDERS MISMATCH"),
            "preflight": (q_q("preflight", lic=[], pre=("ONE PROCESS: selftest",), more=no_prior),
                          "preflight: ONE PROCESS: selftest"),
            "prior absent (real gate)": (q_q("noprior", lic=[], setup=plant_art()), "prior: PRIOR STAGE ABSENT"),
            "prior on the stub (real gate)": (q_q("stubprior", lic=[], setup=both(stub_prior, plant_art())),
                                              "prior: PRIOR STAGE ON THE STUB"),
            "prior under another proposal (real gate)": (q_q("otherprop", lic=[], setup=both(
                plant_time(proposal="2" * 64), plant_art())), "prior: PRIOR STAGE UNDER ANOTHER PROPOSAL"),
            "prior not ended (real gate)": (q_q("notended", lic=[], setup=both(plant_time(status=None), plant_art())),
                                            "prior: PRIOR STAGE NOT ENDED"),
            "prior ended STOP (real gate)": (q_q("priorstop", lic=[], setup=both(plant_time(status="STOP"), plant_art())),
                                             "prior: PRIOR STAGE STOP"),
            "prior at another cap (real gate)": (q_q("prior60", lic=[], setup=both(
                plant_time(cap=60, stub_weights=True), plant_art())), "prior: PRIOR STAGE AT ANOTHER CAP"),
            "prior the first run's, its name a link to it": (q_q("priorlink", lic=[], setup=both(first_link, plant_art())),
                                                             "prior: PRIOR PATH REFUSED"),
            "prior the first run's, by name": (q_q("priorname", lic=[], setup=clear, more=(
                (None, "QUAL_PRIOR_CKPT_NAME", FIRST_RUN_CKPT_NAME),)), "prior: PRIOR PATH REFUSED"),
            "a looping link at the prior path": (q_q("priorloop", lic=[], setup=both(prior_loop, plant_art())),
                                                 "prior: the prior checkpoint path does not resolve"
                                                 if sys.version_info < (3, 13) else "prior: PRIOR STAGE ABSENT"),
            "G-ID artifact absent (real gate)": (q_q("noart", lic=[], setup=plant_time()), "prior: G-ID ARTIFACT ABSENT"),
            "G-ID artifact on the stub (real gate)": (q_q("artstub", lic=[], setup=both(plant_time(), plant_art(stub_tag=True))),
                                                      "prior: G-ID ARTIFACT ON THE STUB"),
            "G-ID artifact at another cap (real gate)": (q_q("art60", lic=[], setup=both(plant_time(), plant_art(cap=60))),
                                                         "prior: G-ID ARTIFACT AT ANOTHER CAP"),
            "G-ID artifact under another proposal (real gate)": (q_q("artprop", lic=[], setup=both(
                plant_time(), plant_art(proposal="2" * 64))), "prior: G-ID ARTIFACT UNDER ANOTHER PROPOSAL"),
            "G-ID artifact unreadable (real gate)": (q_q("artbad", lic=[], setup=both(plant_time(), plant_art(raw="not json"))),
                                                     "prior: G-ID ARTIFACT UNREADABLE"),
            "exists": (q_q("exists", lic=[], setup=q_ckpt(None), more=no_prior), "checkpoint: CHECKPOINT EXISTS"),
            "ended": (q_q("ended", lic=[], setup=q_ckpt("PASS"), more=no_prior), "checkpoint: STAGE ENDED"),
            "ended --resume": (q_q("ended_r", lic=[], setup=q_ckpt("PASS"), resume_flag=True, more=no_prior),
                               "checkpoint: STAGE ENDED"),
            "schedules": (q_q("sched", lic=[], setup=tamper, more=no_prior), "schedules: SCHEDULES NOT CLEAN"),
            "driver": (q_q("driver", lic=[], drv=(["selftest: uncommitted edits"], None), more=no_prior),
                       "driver: selftest: uncommitted edits"),
            "snapshot": (q_q("snapshot", lic=[], snap=(["selftest: no snapshot"], None), more=no_prior),
                         "snapshot: selftest: no snapshot"),
            "snapshot revision not the lock's": (q_q("snaprev", lic=[], snap=([], dict(fake_snap, revision="e" * 40)),
                                                     more=no_prior), "not the lock's weights revision"),
            "top-level --out": (q_q("topout", lic=[], argv_pre=("--out", str(base / "x"))), msg_top),
            "--selftest": (q_q("topsel", lic=[], argv_pre=("--selftest",)), msg_top),
            "--build-schedules": (q_q("topbuild", lic=[], argv_pre=("--build-schedules",)), msg_top),
        }
        bad_q = {k: (v[0]["rc"], v[0]["err"][-240:]) for k, v in q_refused.items()
                 if not (v[0]["rc"] == 2 and v[1] in v[0]["err"] and "refused" in v[0]["err"].lower()
                         and "refused" not in v[0]["out"].lower() and v[0]["loads"] == 0 and not v[0]["calls"]
                         and "DRIVER " not in v[0]["out"] and "SNAPSHOT " not in v[0]["out"]
                         and not (k.startswith("ended") and "CHECKPOINT EXISTS" in v[0]["err"])
                         and v[0]["same"] and not labelled(v[0]["out"] + v[0]["err"]))}
        chk(f"mf3_sessions: qual refuses before the load (exit 2, the refusal on stderr and not stdout, no DRIVER or "
            f"SNAPSHOT line, the loader and both stages never reached, the test root and its gates directory unchanged, "
            f"no label printed) in {len(q_refused)} cases: a flag missing; a file outside the repository or "
            f"uncommitted; a lock other than LOCK-m-F3.md; a proposal the lock does not name; an earlier lock blob, "
            f"without v0.2's lines; a malformed hash; the licence's (d) and (e); the renders; m:267's checklist; the "
            f"prior (the real gate) absent, on the stub, under another proposal, not ended, ended STOP, at another cap, "
            f"and the first run's -- the re-run's name a link to it, or the name itself; a looping link at the prior "
            f"path; G-ID-F3's artifact absent, written on the stub, at another cap, under another proposal, or "
            f"unreadable; G-F3's checkpoint existing without --resume, or ENDED, with or without it (with no "
            f"CHECKPOINT EXISTS advice); a tampered schedule; the driver check; the snapshot check, and a snapshot "
            f"revision not the lock's; a top-level --out, --selftest or --build-schedules beside qual (m's form, "
            f"exactly, on stderr; the schedules writer and the self-test never reached)",
            not bad_q and len(q_refused) == 35 and not escapes
            and all(q_refused[k][0]["err"] == f"refused: {msg_top}\n" for k in ("top-level --out", "--selftest",
                                                                                "--build-schedules")), (bad_q, escapes))
        multi = q_q("multi", {"renders_sha16": "0" * 16}, lic=["selftest licence"], pre=("ONE PROCESS: selftest",),
                    setup=plant_time(), drv=(["selftest: uncommitted edits"], None), snap=(["selftest: no snapshot"], None))
        ref_lines = [ln for ln in multi["err"].splitlines() if ln.startswith("REFUSED")]
        chk("mf3_sessions: qual's precheck problems (the licence's, the renders', the prior gate's -- here G-ID-F3's "
            "artifact absent -- and m:267's checklist's), the driver check's and the snapshot check's are refused "
            "together, in one REFUSED line naming G-F3 (exit 2; no DRIVER or SNAPSHOT line; nothing loaded)",
            multi["rc"] == 2 and len(ref_lines) == 1 and multi["err"].count("REFUSED: G-F3:") == 1
            and all(x in ref_lines[0] for x in (
                "licence: selftest licence", "renders: RENDERS MISMATCH", "prior: G-ID ARTIFACT ABSENT",
                "preflight: ONE PROCESS: selftest", "driver: selftest: uncommitted edits",
                "snapshot: selftest: no snapshot"))
            and "DRIVER " not in multi["out"] and "SNAPSHOT " not in multi["out"] and multi["loads"] == 0, ref_lines)
        n0, s0 = len(loads), len(stage_calls)
        e_ = io.StringIO()
        seam_root = fresh("seam")
        seam_before = tree_state(seam_root.parent)
        with contextlib.ExitStack() as st:
            st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", fresh("seam_default")))
            st.enter_context(mock.patch.object(guard, "GATES_DIR", seam_root.parent / "gates"))
            st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage("gate")))
            st.enter_context(mock.patch.object(stages, "run_gid_pair_f3", t_stage("gid")))
            st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: []))
            st.enter_context(gpatch("_load_qwen", t_loader))
            st.enter_context(contextlib.redirect_stderr(e_))
            st.enter_context(contextlib.redirect_stdout(io.StringIO()))
            rc_or = run_qual(**{**tflags, "lock_file": "CLAUDE.md"}, resume_run=False, out_root=seam_root)
        chk("mf3_sessions: run_qual with an out root and no stub factory refuses before anything -- before the identity "
            "-- exit 2, the loader and both stages, trapped, never reached, the test root unchanged (time's seam case, "
            "carried)",
            rc_or == 2 and "REFUSED: qual: an out root names a test directory" in e_.getvalue()
            and "cites" not in e_.getvalue() and len(loads) == n0 and len(stage_calls) == s0
            and tree_state(seam_root.parent) == seam_before, e_.getvalue()[-200:])
        rl = q_q("reach_load", lic=[], setup=clear)
        lines_l = rl["out"].splitlines()
        drv_i = next((i for i, x in enumerate(lines_l) if x.startswith("DRIVER ")), None)
        snp_i = next((i for i, x in enumerate(lines_l) if x.startswith("SNAPSHOT ")), None)
        rfb = q_q("first_beside", lic=[], setup=both(clear, plant_time(name=FIRST_RUN_CKPT_NAME, cap=60,
                                                                        stub_weights=True)))
        rr = q_q("resume_open", lic=[], setup=both(clear, q_ckpt(None)), resume_flag=True)
        rp = q_q("pending", lic=[], setup=pending, more=no_prior)
        chk("mf3_sessions: with every pre-load check clear -- the real prior gate passing a G-TIME-F3 checkpoint ended "
            "PASS at cap 120 that the stub did not write, with a G-ID-F3 artifact at cap 120 that it did not write either "
            "-- qual prints the DRIVER line and then the SNAPSHOT line and only then reaches the loader (the trap: exit "
            "4, no stage reached, the test root unchanged); the state at G-F3, with the first run's checkpoint beside "
            "the re-run's, passes; --resume lets an open G-F3 checkpoint through; and an end pending passes without "
            "--resume: each reaches the loader",
            rl["rc"] == 4 and rl["loads"] == 1 and not rl["calls"] and rl["same"] and drv_i is not None
            and snp_i is not None and drv_i < snp_i
            and lines_l[drv_i] == f"DRIVER {DRIVER_REL} {'d' * 64}: committed at HEAD {stages._git_head()}, working tree identical"
            and lines_l[snp_i] == snapshot_line(fake_snap) and "STOP: selftest: the Qwen loader was reached" in rl["err"]
            and all(x["rc"] == 4 and x["loads"] == 1 and not x["calls"] and "the Qwen loader was reached" in x["err"]
                    and x["same"] for x in (rfb, rr, rp)), [(x["rc"], x["err"][-160:]) for x in (rl, rfb, rr, rp)])

        class Stand:
            def __init__(self, mid):
                self.model_id = mid
        order: list = []

        def seq(*answers):
            it = iter(answers)

            def f():
                order.append("snap")
                return next(it)
            return f

        def stand_loader():
            order.append("load")
            return Stand(QWEN_MODEL_ID)
        # after the load, for qual: a re-read that refuses, a moved refs/main or another model id STOPs before the stage
        # (time's post-load cases, carried; the qual wiring's review, MINOR-1)
        def stand_mid(mid):
            def f():
                order.append("load")
                return Stand(mid)
            return f
        moved = dict(fake_snap, revision="e" * 40)
        post = {
            "re-read refuses": (q_q("post_refuse", lic=[], setup=clear, loader=stand_loader,
                                     snapfn=seq(([], fake_snap), (["selftest: gone"], None))),
                                ("STOP: SNAPSHOT RE-READ REFUSED", "selftest: gone")),
            "refs/main moved": (q_q("post_moved", lic=[], setup=clear, loader=stand_loader,
                                     snapfn=seq(([], fake_snap), ([], moved))),
                                ("STOP: SNAPSHOT MOVED", f"before the load {rev}; after it {'e' * 40}")),
            "another model id": (q_q("post_mid", lic=[], setup=clear, loader=stand_mid("other/model"),
                                      snapfn=seq(([], fake_snap), ([], fake_snap))),
                                 ("STOP: MODEL ID", f"the adapter loaded 'other/model', the snapshot check read "
                                                    f"'{QWEN_MODEL_ID}'")),
        }
        bad_post = {k: (v[0]["rc"], v[0]["err"][-200:]) for k, v in post.items()
                    if not (v[0]["rc"] == 4 and all(x in v[0]["err"] for x in v[1]) and not v[0]["calls"]
                            and v[0]["same"] and "SNAPSHOT re-read after the load: unchanged" not in v[0]["out"])}
        chk("mf3_sessions: after the load, qual STOPs (exit 4) before the stage on a re-read that refuses, a moved refs/main "
            "or another model id, each STOP naming its evidence, with no re-read line (time's post-load cases, carried)",
            not bad_post and len(post) == 3, bad_post)
        order.clear()
        ru = q_q("post_ok", lic=[], setup=clear, loader=stand_loader, snapfn=seq(([], fake_snap), ([], fake_snap)))
        call = ru["calls"][0][1] if ru["calls"] else {}
        want_prior = (ru["root"] / "ckpt" / TIME_CKPT_NAME).resolve()
        chk("mf3_sessions: after the load and the re-read (snapshot, load, snapshot), qual reaches stages.run_gate_stage "
            "-- not run_gid_pair_f3 -- once, with gate qual and QUAL_COUNTS, the prior the re-run's checkpoint at its out "
            "root, by path, the out root stages.DEFAULT_OUT, resume off and the identity with locked_path uncached at cap "
            "120 (here the trap: exit 4)",
            ru["rc"] == 4 and [c[0] for c in ru["calls"]] == ["gate"] and order == ["snap", "load", "snap"]
            and call.get("gate") == "qual" and list(call.get("templates_counts") or []) == list(QUAL_COUNTS)
            and Path(call.get("prior_ckpt", "")) == want_prior and Path(call.get("out_root", "")) == ru["root"]
            and call.get("resume") is False and (call.get("identity_extra") or {}).get("locked_path") == "uncached"
            and (call.get("identity_extra") or {}).get("reasoning_cap") == 120
            and "STOP: selftest: the stage was reached" in ru["err"] and ru["same"], (ru["rc"], order, sorted(call)))
    data_after = tree_state(real_out) if real_out.is_dir() else {}
    chk("mf3_sessions: the qual checks loaded nothing and wrote nothing under data/mf3 -- the loader trap was reached 4 "
        "times in all (each of the four cases that clear every pre-load check asserts its own one reach), the stage "
        "trap once (run_gate_stage, the post-load case), the schedules writer and the self-test never from a qual "
        "invocation; data/mf3's file hashes are unchanged and stages.DEFAULT_OUT and guard.GATES_DIR are restored",
        data_before == data_after and stages.DEFAULT_OUT == real_out and guard.GATES_DIR == real_gates
        and len(loads) == 4 and [c[0] for c in stage_calls] == ["gate"] and not escapes,
        (len(loads), [c[0] for c in stage_calls], escapes, sorted(set(data_before) ^ set(data_after))[:3]))


def _selftest_campaign(chk, labels) -> None:
    """The campaign wiring's checks (model-free), in _selftest_qual's forms: the campaign's values; its identity and the
    lock's two whole lines; its help; the ruling helpers (ruling_texts, _campaign_state, campaign_ruling_problems,
    ruling_line) on synthetic files in a test directory; the stub path (``stub_run``: G-TIME-F3's re-run checkpoint, a
    FAILed G-ID-F3 artifact and G-F3 written first on the stub at the same test root, then run_campaign) with the loader
    trapped, stages.DEFAULT_OUT a test root and guard.GATES_DIR a test directory per run; and the Qwen path (``q_c``)
    with _load_qwen a trap (in the post-load cases a stand-in carrying a model_id), stages.run_campaign,
    stages.run_gate_stage and stages.run_gid_pair_f3 traps, stages.DEFAULT_OUT a test root and guard.GATES_DIR beside
    it, m:267's laptop checklist stubbed, and build_schedules and run_selftest trapped. So no case can load the model,
    run a session on it or write data/mf3. The last check asserts how often each trap was reached."""
    import ast
    import inspect
    import textwrap
    import threading
    from unittest import mock

    from valence_core.m import corr as m_corr
    from valence_core.mf3 import scaffold as sc_mod
    from valence_core.mf3 import testing

    G = globals()
    loads: list = []
    stage_calls: list = []
    escapes: list = []
    ck_name, gid_name = f"{keys.UNIT}_campaign.json", f"{keys.UNIT}_G-ID.json"
    name_c = stages.stage_name("campaign")
    end_key = rs.m_resume.END_PENDING
    sha16 = stages._sha16_text

    def t_escape(name):
        def f(*a, **k):
            escapes.append(name)
            raise SystemExit(f"selftest: {name} was reached from a campaign invocation")
        return f

    def t_loader():
        loads.append(1)
        raise SystemExit("selftest: the Qwen loader was reached")

    def t_stage(tag):
        def f(*a, **k):
            stage_calls.append((tag, k))
            raise SystemExit("selftest: the stage was reached")
        return f

    def gpatch(name, val):
        return mock.patch.dict(G, {name: val})

    def run3(argv):
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
            try:
                rc = main(argv)
            except SystemExit as e:
                rc = e.code if isinstance(e.code, int) else 2
        return rc, buf.getvalue(), err.getvalue()

    def tree_state(root: Path) -> dict:
        out = {}
        for q in sorted(root.rglob("*")):
            k = str(q.relative_to(root))
            out[k] = ("link", os.readlink(q)) if q.is_symlink() else (
                ("file", hashlib.sha256(q.read_bytes()).hexdigest()) if q.is_file() else (
                    ("dir", None) if q.is_dir() else ("other", None)))
        return out

    def labelled(text: str) -> bool:
        return any(re.search(rf"\b{re.escape(w)}\b", text, re.IGNORECASE) for w in labels)

    real_out, real_gates = stages.DEFAULT_OUT, guard.GATES_DIR
    data_before = tree_state(real_out) if real_out.is_dir() else {}
    _pool, renders = sc_mod.pool_and_renders()
    prop_sha = hashlib.sha256(stages.PROPOSAL_PATH.read_bytes()).hexdigest()
    tflags = {"proposal_file": stages.PROPOSAL_REL, "lock_file": TIME_LOCK_FILE,
              "analyzer_sha256": hashlib.sha256(stages.ANALYZER_PATH.read_bytes()).hexdigest(),
              "package_sha256": guard.package_sha256_of(guard.PACKAGE_DIR),
              "renders_sha16": m_corr.renders_sha(renders)}
    z64 = "0" * 64
    real_committed = stages.committed

    def committed_but(rel_x: str, ret):
        return lambda rel, repo=stages.REPO: ret if rel == rel_x else real_committed(rel, repo)

    # --- the campaign's values: LOCK-m-F3 v1.0's, G-PWR (Q-F3)'s record's, the committed schedules' ----------------
    lock_cp, lock_blob = stages.committed(CAMPAIGN_LOCK_FILE)
    lock_text = (lock_blob or b"").decode("utf-8", "replace")
    lock_lines = lock_text.splitlines()
    gp_cp, gp_blob = stages.committed("data/mf3/gates/Q-F3_G-PWR.json")
    gpwr = json.loads(gp_blob or b"{}")
    scheds = stages.load_committed([("campaign", t) for t in keys.TEMPLATES], schedule.DEFAULT_OUT)
    fl = campaign_floors()
    chk("mf3_sessions: the campaign's values are LOCK-m-F3 v1.0's -- CAMPAIGN_LAUNCH_COUNTS A1 128, A1s 64, A2 224, A2s 96, "
        "A3 224, A3s 96 in keys.TEMPLATES' order (832 launches), G-PWR (Q-F3)'s record's L; CAMPAIGN_HOUR_CAP 480, an int; "
        "CAMPAIGN_LOCK_LINES their two line forms, each a whole line of the committed lock (one or more, the qual "
        "wiring's NOTE-7 form); the floors "
        "schedule.FLOORS under the path, uncached (A1 80, A1s 32, A2 144, A2s 56, A3 144, A3s 56), the record's; each "
        "floor at most its launch count and each launch count at most its committed campaign schedule's n; locked_path "
        "uncached and cap 120; the prior G-F3's checkpoint name, stages.PRIOR_STAGE's 'qual'",
        lock_cp == [] and gp_cp == []
        and CAMPAIGN_LAUNCH_COUNTS == (("A1", 128), ("A1s", 64), ("A2", 224), ("A2s", 96), ("A3", 224), ("A3s", 96))
        and tuple(t for t, _ in CAMPAIGN_LAUNCH_COUNTS) == tuple(keys.TEMPLATES)
        and sum(n for _, n in CAMPAIGN_LAUNCH_COUNTS) == 832 and dict(CAMPAIGN_LAUNCH_COUNTS) == gpwr["launch"]["L"]
        and type(CAMPAIGN_HOUR_CAP) is int and CAMPAIGN_HOUR_CAP == 480
        and CAMPAIGN_LOCK_LINES == ("launch counts = A1 128, A1s 64, A2 224, A2s 96, A3 224, A3s 96", "hour cap = 480 h")
        and all(lock_lines.count(x) >= 1 for x in CAMPAIGN_LOCK_LINES)
        and fl == {"A1": 80, "A1s": 32, "A2": 144, "A2s": 56, "A3": 144, "A3s": 56} == gpwr["inputs"]["floors"]
        and all(fl[t] <= n <= int(scheds[t]["n"]) for t, n in CAMPAIGN_LAUNCH_COUNTS)
        and CAMPAIGN_LOCKED_PATH == "uncached" and CAMPAIGN_REASONING_CAP == 120 and CAMPAIGN_LOCK_FILE == TIME_LOCK_FILE
        and CAMPAIGN_PRIOR_CKPT_NAME == stages.out_paths("qual")["ckpt"].name and stages.PRIOR_STAGE["campaign"] == "qual",
        (fl, CAMPAIGN_LOCK_LINES, sorted(gpwr)[:4]))

    # --- the identity, from the committed lock: G-F3's; v1.0's two lines required as whole lines --------------------
    ex_q, pq = stage_identity_extra("qual", **tflags)
    ex_c, pc = stage_identity_extra("campaign", **tflags)
    try:
        x_ok = stages._extra(ex_c or {}, stage="campaign", stub=False) is not None
    except ValueError:
        x_ok = False
    chk("mf3_sessions: the campaign's identity_extra from the committed LOCK-m-F3.md is G-F3's -- the same proposal, "
        "lock, analyzer, package, renders, m files and weights, reasoning_cap 120 (CAMPAIGN_REASONING_CAP) and "
        "locked_path uncached (CAMPAIGN_LOCKED_PATH); stages._extra accepts it for 'campaign'",
        pq == pc == [] and ex_c is not None and ex_c == ex_q and ex_c["locked_path"] == "uncached"
        and ex_c["reasoning_cap"] == 120 and x_ok, (pc, sorted(ex_c or {})))
    v1_rule = "\n---\n\nWhere v0.2's text below, or the text it carries, differs from v1.0"
    v02_text = lock_text.split(v1_rule, 1)[1].split("\n", 2)[2] if v1_rule in lock_text else ""
    lc_, hc_ = CAMPAIGN_LOCK_LINES

    def swap(text: str, old: str, new: str) -> str:
        return "\n".join(new if ln == old else ln for ln in text.split("\n"))

    def drop(text: str, old: str) -> str:
        return "\n".join(ln for ln in text.split("\n") if ln != old)
    variants = {
        "v0.2's blob": v02_text,
        "other launch counts": swap(lock_text, lc_, lc_.replace("A1 128", "A1 129")),
        "the launch line with a tail": swap(lock_text, lc_, lc_ + " (a projection)"),
        "the launch line indented": _lines_prefixed(lock_text, lc_, "  "),
        "the launch line moved off its start": _lines_prefixed(lock_text, lc_, "x "),
        "the launch line dropped": drop(lock_text, lc_),
        "another hour cap": swap(lock_text, hc_, "hour cap = 481 h"),
        "the hour cap in other words": swap(lock_text, hc_, "hour cap = 480 hours"),
        "the cap line dropped": drop(lock_text, hc_),
    }
    got_c = {}
    for nm, txt in variants.items():
        with mock.patch.object(stages, "committed", committed_but(CAMPAIGN_LOCK_FILE, ([], txt.encode("utf-8")))):
            got_c[nm] = (stage_identity_extra("campaign", **tflags), stage_identity_extra("qual", **tflags))
    chk("mf3_sessions: the campaign refuses a lock whose committed text lacks either of v1.0's two lines as a whole line "
        "-- v0.2's blob (as committed below v1.0's rule), other launch counts, the launch line with a tail, indented or "
        "moved off its line's start (every line equal to it, NOTE-7's form), or dropped, another hour cap, '480 hours', "
        "and the cap line dropped -- each 'carries no whole line'; qual accepts all nine (it runs under v0.2's lines, "
        "which each keeps)",
        v02_text.startswith("# LOCK-m-F3.md — v0.2") and len(variants) == 9
        and all(v[0][0] is None and any("carries no whole line" in x for x in v[0][1]) for v in got_c.values())
        and all(v[1][0] is not None for v in got_c.values()),
        {k: v[0][1][:1] for k, v in got_c.items() if not (v[0][0] is None and v[1][0] is not None)})
    q_moved = _lines_prefixed(lock_text, QUAL_LOCK_LINES[1], "x ")
    both_bad = v02_text + "\n| `valence_core/m/corr.py` | `" + "c" * 64 + "` |\n"
    with mock.patch.object(stages, "committed", committed_but(CAMPAIGN_LOCK_FILE, ([], q_moved.encode("utf-8")))):
        ex_qm, p_qm = stage_identity_extra("campaign", **tflags)
    with mock.patch.object(stages, "committed", committed_but(CAMPAIGN_LOCK_FILE, ([], both_bad.encode("utf-8")))):
        ex_bb, p_bb = stage_identity_extra("campaign", **tflags)
        ex_bt, p_bt = stage_identity_extra("time", **tflags)
    chk("mf3_sessions: the campaign checks v0.2's lines first, at a line's start, as qual does (v1.0 with its path line "
        "moved off every line's start: 'carries no line opening'), and both line checks come before the m files and the "
        "weights are read (v0.2's blob that also names corr.py with a second sha256: refused for the missing whole "
        "lines alone, where time refuses it for the doubled sha256)",
        ex_qm is None and len(p_qm) == 1 and "carries no line opening" in p_qm[0] and "campaign-Q-F3" in p_qm[0]
        and ex_bb is None and len(p_bb) == 1 and "carries no whole line" in p_bb[0]
        and ex_bt is None and any("valence_core/m/corr.py with 2 sha256" in x for x in p_bt), (p_qm, p_bb, p_bt[:1]))
    rc_h, out_h, _err_h = run3(["campaign", "--help"])
    flat_h = "".join(out_h.split())
    rc_t, out_t, _err_t = run3(["--help"])
    # m's camp_pauses, read from its source, not imported (the constants check's form; this review's NOTE-2)
    m_cp = [ast.literal_eval(n_.value) for n_ in ast.walk(ast.parse((REPO / "scripts" / "m_sessions.py").read_text(
        encoding="utf-8"))) if isinstance(n_, ast.Assign) and any(isinstance(t_, ast.Name) and t_.id == "camp_pauses"
                                                                  for t_ in n_.targets)]
    chk("mf3_sessions: campaign --help lists time's five flags, each followed by its TIME_FLAG_HELP text, --resume "
        "('continue the Q-F3 campaign's checkpoint'), --adjudication-file and --pi-stop-file with their texts, and the "
        "pauses and re-run guidance (CAMPAIGN_PAUSES) in its description (exit 0); the top-level --help gives the "
        "campaign's help with CAMPAIGN_PAUSES (exit 0); CAMPAIGN_PAUSES is m's camp_pauses verbatim, its one "
        "assignment in scripts/m_sessions.py",
        rc_h == 0 and "--resumecontinuetheQ-F3campaign'scheckpoint(skip-only)" in flat_h
        and all(f"--{k.replace('_', '-')}{k.upper()}" + "".join(v.split()) in flat_h for k, v in TIME_FLAG_HELP.items())
        and "--adjudication-fileADJUDICATION_FILEaUTF-8textfile" in flat_h and "--pi-stop-filePI_STOP_FILEaUTF-8textfile" in flat_h
        and "".join(CAMPAIGN_PAUSES.split()) in flat_h and rc_t == 0
        and "".join((STAGE_HELP["campaign"] + "; " + CAMPAIGN_PAUSES).split()) in "".join(out_t.split())
        and m_cp == [CAMPAIGN_PAUSES], (out_h[-200:], rc_t, len(m_cp)))

    # --- the ruling helpers, on synthetic files ---------------------------------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)

        def wfile(nm: str, data) -> str:
            p = d / nm
            p.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))
            return str(p)
        (d / "adir").mkdir()
        os.mkfifo(d / "afifo")
        fifo_ = d / "afifo"
        res_ff: dict = {}

        def fifo_runs():
            # every call on the FIFO in a daemon thread joined with a timeout, m's form (its round 2's M2-2, round 3's
            # O3-3, round 4's F4-9; this wiring's review, NOTE-5): a regressed guard blocks in open(), and the checks
            # below then fail by name instead of hanging the self-test; a reader blocked in open() is released by a
            # non-blocking writer's open
            res_ff["texts"] = (ruling_texts(str(fifo_), None), ruling_texts(None, str(fifo_)))
            res_ff["state"] = _campaign_state(fifo_)
            reads_: list = []
            with gpatch("_campaign_state", lambda p_: reads_.append(p_) or ("unreadable", {})):
                res_ff["mirror"] = campaign_ruling_problems(fifo_, None, None)
            res_ff["mirror_reads"] = reads_
            res_ff["line"] = ruling_line(name_c, fifo_, {"adjudication": None, "pi_stop": "Stop."})
        th_ff = threading.Thread(target=fifo_runs, daemon=True)
        th_ff.start()
        th_ff.join(20)
        ff_hung = th_ff.is_alive()
        if ff_hung:
            try:
                os.close(os.open(fifo_, os.O_WRONLY | os.O_NONBLOCK))
            except OSError:
                pass
            th_ff.join(10)
        ok_t, ok_p = ruling_texts(wfile("adj.txt", "The seat rules: resume.\n"), wfile("pi.txt", "﻿The PI stops."))
        none_t, none_p = ruling_texts(None, None)
        bad = {"blank": (wfile("b1.txt", "  \n\t "), "blank"), "format characters": (wfile("b2.txt", "​​"), "blank"),
               "control characters": (wfile("b3.txt", "\x01\x02\n"), "blank"),
               "a directory": (str(d / "adir"), "not a regular file"), "a FIFO": (str(d / "afifo"), "not a regular file"),
               "absent": (str(d / "nothing.txt"), "not a regular file"),
               "not UTF-8": (wfile("b4.txt", b"\xff\xfe\xfa"), "unreadable as UTF-8 text (UnicodeDecodeError)")}
        hung_t = ({"adjudication": 0, "pi_stop": 0}, [])
        got_r = {k: (res_ff.get("texts", (hung_t, hung_t)) if k == "a FIFO" else
                     (ruling_texts(v[0], None), ruling_texts(None, v[0]))) for k, v in bad.items()}
        two_t, two_p = ruling_texts(str(d / "adir"), wfile("b5.txt", " "))
        chk("mf3_sessions: ruling_texts reads each ruling file as UTF-8 text, a leading byte-order mark dropped, passed as "
            "read (unstripped), and refuses one that is blank (whitespace, format or control characters only), not a "
            "regular file (a directory, a FIFO -- never opened: its calls return within 20 s -- or absent) or not "
            "UTF-8, naming its flag; both files' "
            "problems together; none given reads nothing",
            ok_p == [] and ok_t == {"adjudication": "The seat rules: resume.\n", "pi_stop": "The PI stops."}
            and none_t == {"adjudication": None, "pi_stop": None} and none_p == []
            and all(v[0][0]["adjudication"] is None and len(v[0][1]) == 1 and v[0][1][0].startswith("--adjudication-file")
                    and bad[k][1] in v[0][1][0] and v[1][0]["pi_stop"] is None and len(v[1][1]) == 1
                    and v[1][1][0].startswith("--pi-stop-file") and bad[k][1] in v[1][1][0] for k, v in got_r.items())
            and len(two_p) == 2 and two_t == {"adjudication": None, "pi_stop": None} and not ff_hung,
            {k: (v[0][1], v[1][1]) for k, v in got_r.items()})

        look = {"kind": "look", "at_launches": 40, "adjudication": None, "arm": None}

        def ck_(*, sessions=1, pauses=(), pi_stop=None, terminal=None, pending=False) -> dict:
            o = {"identity": {"unit": keys.UNIT, "stage": "campaign"},
                 "sessions": [{"template": "A1", "s": i} for i in range(sessions)],
                 "campaign": {"pauses": [dict(p) for p in pauses], "pi_stop": pi_stop, "terminal": terminal,
                              "end_look": None}}
            if pending:
                o[end_key] = {"status": "PAUSE"}
            return o

        def wck(nm: str, obj=None, raw: str | None = None) -> Path:
            p = d / nm
            p.write_text(raw if raw is not None else json.dumps(obj), encoding="utf-8")
            return p
        st_open = wck("open.json", ck_(pauses=[dict(look, adjudication="Ruling one."), dict(look, at_launches=80)],
                                       pi_stop="The PI stops."))
        cases_st = {
            "absent": (d / "none.json", "absent"), "a directory": (d / "adir", "unreadable"),
            "a FIFO": (d / "afifo", "unreadable"), "not JSON": (wck("u1.json", raw="not json"), "unreadable"),
            "a JSON list": (wck("u2.json", [1]), "unreadable"),
            "sessions not a list": (wck("u3.json", {"sessions": {}, "campaign": {}}), "unreadable"),
            "pauses not a list": (wck("u4.json", dict(ck_(), campaign={"pauses": {}})), "unreadable"),
            "a pause of another kind": (wck("u5.json", ck_(pauses=[dict(look, kind="peek")])), "unreadable"),
            "a launch count not an int": (wck("u6.json", ck_(pauses=[dict(look, at_launches="40")])), "unreadable"),
            "an adjudication not a text": (wck("u7.json", ck_(pauses=[dict(look, adjudication=7)])), "unreadable"),
            "an arm not Q-F3's": (wck("u8.json", ck_(pauses=[dict(look, kind="schedule_exhausted", arm="A0")])),
                                  "unreadable"),
            "a pause lacking its adjudication": (wck("u9.json", ck_(pauses=[{"kind": "look", "at_launches": 40}])),
                                                 "unreadable"),
            "a PI stop not a text": (wck("u10.json", ck_(pi_stop=3)), "unreadable"),
            "a lone surrogate": (wck("u11.json", raw='{"sessions": [], "campaign": {"pauses": [{"kind": "look", '
                                                     '"at_launches": 40, "adjudication": "\\ud800"}]}}'), "unreadable"),
            "pending": (wck("p.json", ck_(pending=True)), "pending"),
            "ended": (wck("e.json", ck_(terminal={"status": "COMPLETE", "at_launches": 832})), "ended"),
            "ended, an end look's pause unruled": (wck("e2.json", ck_(
                pauses=[dict(look, kind="end_look", at_launches=832)],
                terminal={"status": "COMPLETE", "at_launches": 832})), "ended"),
            "open": (st_open, "open"),
        }
        got_st = {k: (res_ff.get("state", ("hung", None)) if k == "a FIFO" else _campaign_state(v[0]))
                  for k, v in cases_st.items()}
        chk("mf3_sessions: _campaign_state reads a campaign checkpoint tolerantly -- absent; unreadable when not a "
            "regular file (a directory, a FIFO, never opened: the FIFO calls return within 20 s), not JSON, not an "
            "object, its sessions or pauses not "
            "lists, a pause of another kind, with a launch count not an int, an adjudication not a text or no "
            "adjudication key, an arm not one of Q-F3's six, a PI stop not a text, or a lone surrogate in a ruling "
            "(summary {}); pending; ended (an end look's pause unruled with it); open -- the open summary text-free: "
            "launched, the PI stop's sha256, the last "
            "pause (kind, launches, arm, adjudicated, digest) and every recorded ruling's sha16",
            not ff_hung and all(got_st[k][0] == v[1] for k, v in cases_st.items())
            and all(got_st[k][1] == {} for k, v in cases_st.items() if v[1] == "unreadable")
            and got_st["open"][1] == {"launched": True,
                                      "pi_stop_sha256": hashlib.sha256(b"The PI stops.").hexdigest(),
                                      "last": {"kind": "look", "at_launches": 80, "arm": None, "adjudicated": False,
                                               "adjudication_sha16": None},
                                      "ruling_sha16s": [sha16("Ruling one.")]}
            and "Ruling one." not in json.dumps(got_st["open"][1]),
            {k: got_st[k][0] for k, v in cases_st.items() if got_st[k][0] != v[1]})

        c_ruled_last = wck("r1.json", ck_(pauses=[dict(look, adjudication="Ruling one."),
                                                  dict(look, at_launches=80, adjudication="Ruling two.")]))
        c_reuse = wck("r2.json", ck_(pauses=[dict(look, adjudication="Ruling one."), dict(look, at_launches=80)]))
        c_exh = wck("r3.json", ck_(pauses=[dict(look, kind="schedule_exhausted", at_launches=120, arm="A1")]))
        c_pend = wck("r4.json", ck_(pauses=[dict(look, adjudication="Ruling one.")], pending=True))
        c_pend_pi = wck("r5.json", ck_(pending=True, pi_stop="The PI stops."))
        c_open0 = wck("r6.json", ck_(sessions=0))
        c_nopause = wck("r7.json", ck_())
        c_look = wck("r8.json", ck_(pauses=[look]))
        crp = campaign_ruling_problems
        rp = {
            "no ruling, a FIFO": (res_ff.get("mirror", ["hung"]), None),
            "unreadable": (crp(cases_st["not JSON"][0], "A ruling.", None), None),
            "ended": (crp(cases_st["ended"][0], "A ruling.", "Stop."), None),
            "another PI stop": (crp(st_open, None, "Another stop."), "CHECKPOINT MISMATCH"),
            "another PI stop beside an end pending": (crp(c_pend_pi, None, "Another stop."), "CHECKPOINT MISMATCH"),
            "an adjudication beside an end pending": (crp(c_pend, "A ruling.", None), "RULING BESIDE AN END PENDING"),
            "a recorded adjudication beside an end pending": (crp(c_pend, " Ruling one. ", None),
                                                               "already records as a pause's ruling"),
            "an unrecorded PI stop beside an end pending": (crp(c_pend, None, "Stop."), "--pi-stop-file"),
            "the recorded PI stop beside an end pending": (crp(c_pend_pi, None, "The PI stops.\n"), None),
            "a PI stop with no checkpoint": (crp(d / "none.json", None, "Stop."), "PI STOP REFUSED"),
            "a PI stop with no session": (crp(c_open0, None, "Stop."), "PI STOP REFUSED"),
            "an adjudication on an exhausted schedule": (crp(c_exh, "A ruling.", None), "SCHEDULE EXHAUSTED"),
            "the PI's stop on an exhausted schedule": (crp(c_exh, "A ruling.", "Stop."), None),
            "a ruling reused": (crp(c_reuse, "Ruling one.\n", None), "RULING REUSED"),
            "no pause to adjudicate, the last ruled": (crp(c_ruled_last, "A ruling.", None),
                                                       "already carries a ruling (sha16 " + sha16("Ruling two.")
                                                       + "); resume with --resume alone"),
            "no pause to adjudicate, with the PI's stop": (crp(c_ruled_last, "A ruling.", "Stop."),
                                                          "drop --adjudication-file: resume with --resume and the PI's "
                                                          "stop alone"),
            "no pause at all": (crp(c_nopause, "A ruling.", None), "NO PAUSE TO ADJUDICATE at"),
            "an open look's pause": (crp(c_look, "A ruling.", None), None),
            "the PI's stop on an open look's pause": (crp(c_look, None, "Stop."), None),
        }
        bad_rp = {k: v[0] for k, v in rp.items()
                  if not ((v[1] is None and v[0] == []) or (v[1] is not None and len(v[0]) == 1 and v[1] in v[0][0]))}
        chk("mf3_sessions: campaign_ruling_problems mirrors the stage's refusals before the load -- nothing for no ruling "
            "(a FIFO not read: _campaign_state not called), an unreadable or an ended checkpoint; CHECKPOINT MISMATCH "
            "for another PI stop, beside an "
            "end pending too; RULING BESIDE AN END PENDING for an adjudication there (naming one the checkpoint records) "
            "or a PI stop it does not record, none for the stop it records; PI STOP REFUSED with no checkpoint or no "
            "session; SCHEDULE EXHAUSTED unless the PI's stop is offered; RULING REUSED for an earlier pause's ruling "
            "(stripped); NO PAUSE TO ADJUDICATE with the last ruling's digest and how to resume; nothing for a fit "
            "ruling", not bad_rp and len(rp) == 19 and res_ff.get("mirror_reads") == [] and not ff_hung
            and "NO PAUSE TO ADJUDICATE" in rp["no pause at all"][0][0]
            and "already carries" not in rp["no pause at all"][0][0], bad_rp)
        # the mirror's words are the stage's own (this review's MINOR-3): each refusal the stage makes again after the
        # load, read from stages.run_campaign's source -- its f-strings' text, each placeholder by its expression --
        # equals the mirror's message with the path and the arm put back as placeholders, the declared suffixes aside
        tmpl = {"".join(v_.value if isinstance(v_, ast.Constant) else "{" + ast.unparse(v_.value) + "}"
                        for v_ in n_.values)
                for n_ in ast.walk(ast.parse(textwrap.dedent(inspect.getsource(stages.run_campaign))))
                if isinstance(n_, ast.JoinedStr)}

        def as_tmpl(msg, path: Path, arm: str | None = None) -> str:
            t_ = str(msg).replace(str(path), "{cpath}")
            return t_.replace(f": {arm} has", ": {last.get('arm')} has") if arm else t_

        def stage_t(cls: str) -> list:
            return [t_ for t_ in tmpl if t_.startswith(cls)]
        first = lambda k: (rp[k][0] or [""])[0]
        w_ok = {
            "CHECKPOINT MISMATCH": as_tmpl(first("another PI stop"), st_open) in [
                t_ + " (the stage makes this refusal after the load)"
                for t_ in stage_t("CHECKPOINT MISMATCH: {cpath}")],
            "PI STOP REFUSED": as_tmpl(first("a PI stop with no session"), c_open0) in stage_t("PI STOP REFUSED"),
            "SCHEDULE EXHAUSTED": as_tmpl(first("an adjudication on an exhausted schedule"), c_exh, "A1")
            in stage_t("SCHEDULE EXHAUSTED"),
            "NO PAUSE TO ADJUDICATE": as_tmpl(first("no pause at all"), c_nopause) in stage_t("NO PAUSE TO ADJUDICATE")
            and any(as_tmpl(first("no pause to adjudicate, the last ruled"), c_ruled_last).startswith(
                t_ + " -- its last pause (") for t_ in stage_t("NO PAUSE TO ADJUDICATE")),
        }
        chk("mf3_sessions: campaign_ruling_problems' messages are the stage's own words -- CHECKPOINT MISMATCH, PI "
            "STOP REFUSED, SCHEDULE EXHAUSTED and NO PAUSE TO ADJUDICATE each equal a refusal in stages.run_campaign's "
            "source (its f-string, each placeholder by its expression) with the path and the arm put back, beside "
            "only the declared suffixes (CHECKPOINT MISMATCH's 'the stage makes this refusal after the load'; NO PAUSE "
            "TO ADJUDICATE's last pause)",
            all(w_ok.values()) and len(w_ok) == 4, {k: v for k, v in w_ok.items() if not v})
        rl_ = {
            "none": (ruling_line(name_c, c_look, {"adjudication": None, "pi_stop": None}), None),
            "absent": (ruling_line(name_c, d / "none.json", {"adjudication": "A ruling.", "pi_stop": None}),
                       f"RULING {name_c}: the seat's adjudication (sha16 {sha16('A ruling.')}) offered with no "
                       f"checkpoint on disk"),
            "open look": (ruling_line(name_c, c_look, {"adjudication": " A ruling.\n", "pi_stop": "Stop."}),
                          f"RULING {name_c}: the seat's adjudication (sha16 {sha16('A ruling.')}) and the PI's stop "
                          f"(sha16 {sha16('Stop.')}) offered for the pause at 40 launches (look)"),
            "pending": (ruling_line(name_c, c_pend, {"adjudication": None, "pi_stop": "Stop."}),
                        f"RULING {name_c}: the PI's stop (sha16 {sha16('Stop.')}) offered beside an end pending"),
            "ended": (ruling_line(name_c, cases_st["ended"][0], {"pi_stop": "Stop."}), "offered on an ended campaign"),
            "ended, its last pause unruled": (ruling_line(name_c, cases_st["ended, an end look's pause unruled"][0],
                                                       {"pi_stop": "Stop."}), "offered on an ended campaign"),
            "a FIFO": (res_ff.get("line"), "offered on an unreadable checkpoint"),
            "unreadable": (ruling_line(name_c, cases_st["not JSON"][0], {"pi_stop": "Stop."}),
                           "offered on an unreadable checkpoint"),
            "no pause": (ruling_line(name_c, c_nopause, {"pi_stop": "Stop."}), "offered with no pause unadjudicated"),
            "recorded (RM4-1)": (ruling_line(name_c, c_ruled_last, {"adjudication": "Ruling two."}),
                                 "offered with no pause unadjudicated; the checkpoint already records this adjudication "
                                 "as a pause's ruling"),
        }
        bad_rl = {k: v[0] for k, v in rl_.items() if not ((v[1] is None and v[0] is None) or (
            v[1] is not None and v[0] is not None and (v[0] == v[1] or v[0].endswith(v[1]))))}
        chk("mf3_sessions: the RULING line gives each offered text's sha16 (of the stripped text, never the text) and the "
            "pause it is offered for or the checkpoint's state -- none offered, no line; no checkpoint; a look's open "
            "pause; beside an end pending; an ended campaign, its last pause unruled too; an unreadable checkpoint, a "
            "FIFO among them; no pause unadjudicated -- with "
            "RM4-1's note where the checkpoint already records the adjudication offered",
            not bad_rl and not ff_hung and "A ruling." not in str(rl_["open look"][0]), bad_rl)

    # --- the stub path: time, a FAILed id and G-F3 on the stub, then the campaign at the same root ------------------
    def cells(gate):
        if gate == "campaign":
            return {(t, s): schedule.campaign_schedule(t, 1)[s] for t in keys.TEMPLATES for s in range(16)}
        return {(t, j): schedule.gate_schedule(gate, t, schedule.GATE_PLAN_COUNTS[(gate, t)])[j]
                for t in (keys.GID_TEMPLATES if gate == "id" else keys.TEMPLATES)
                for j in range(schedule.GATE_PLAN_COUNTS[(gate, t)])}
    made_ad: list = []

    def stub(gate, rule=None, interrupt=None):
        def f():
            a = testing.F3Adapter()
            a.load(stages._script_policy(gate, cells(gate), rule, interrupt), None)
            made_ad.append(a)
            return a
        return f

    def stub_run(fn, root, factory, resume_run=False, *, gates, camp_stage=None, **rul):
        buf, err = io.StringIO(), io.StringIO()
        with contextlib.ExitStack() as st:
            st.enter_context(mock.patch.object(guard, "GATES_DIR", gates))
            st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", root.parent / "default-out"))
            st.enter_context(gpatch("_load_qwen", t_loader))
            if camp_stage is not None:
                st.enter_context(mock.patch.object(stages, "run_campaign", camp_stage))
            st.enter_context(contextlib.redirect_stdout(buf))
            st.enter_context(contextlib.redirect_stderr(err))
            try:
                rc = fn(**tflags, resume_run=resume_run, adapter_factory=factory, out_root=root, **rul)
            except stages._Interrupt as e:
                rc = e
        return rc, buf.getvalue(), err.getvalue()

    div = lambda t, s, kind, i, call: "Eight." if (call["cached"] and t == "A3s" and kind == "forced" and i == 1) else None

    with tempfile.TemporaryDirectory() as td:
        base = Path(td)

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            (base / nm / "gates").mkdir()
            return r
        r_c = fresh("chain")
        g_c = r_c.parent / "gates"
        pre_c = (stub_run(run_time, r_c, stub("time"), gates=g_c)[0], stub_run(run_id, r_c, stub("id", div), gates=g_c)[0],
                 stub_run(run_qual, r_c, stub("qual"), gates=g_c)[0])
        pi_f, adj_f = base / "pi_stop.txt", base / "adjudication.txt"
        pi_f.write_text("The PI stops the campaign (selftest).\n", encoding="utf-8")
        adj_f.write_text("The seat's ruling (selftest).\n", encoding="utf-8")
        ckc = r_c / "ckpt" / ck_name
        rc_p0, out_p0, err_p0 = stub_run(run_campaign, r_c, stub("campaign"), gates=g_c, pi_stop_file=str(pi_f))
        p0_absent = not ckc.exists()
        stop_a2 = lambda t, s, kind, i: t == "A2" and s == 0 and kind == "forced" and i == 0
        made_ad.clear()
        rc_i, _o, _e = stub_run(run_campaign, r_c, stub("campaign", None, stop_a2), gates=g_c)
        ck_i = rs.read_checkpoint(ckc) if ckc.is_file() else {"sessions": []}
        bytes_i = ckc.read_bytes() if ckc.is_file() else b""
        rc_n, out_n, err_n = stub_run(run_campaign, r_c, stub("campaign"), True, gates=g_c, adjudication_file=str(adj_f))
        n_same = ckc.is_file() and ckc.read_bytes() == bytes_i
        rc_s, out_s, err_s = stub_run(run_campaign, r_c, stub("campaign"), True, gates=g_c, pi_stop_file=str(pi_f))
        ck_s = rs.read_checkpoint(ckc) if ckc.is_file() else {}
        ident_s, camp_s = ck_s.get("identity") or {}, ck_s.get("campaign") or {}
        rep_s = r_c / "reports" / f"{keys.UNIT}_campaign_report.json"
        rc_e, _o, err_e = stub_run(run_campaign, r_c, stub("campaign"), True, gates=g_c)
        sl = out_s.splitlines()
        ri = next((i for i, x in enumerate(sl) if x.startswith("RULING ")), None)
        si = next((i for i, x in enumerate(sl) if x.startswith(f"STAGE {name_c} ")), None)
        chk("mf3_sessions: on the stub factory after time, a FAILed id and G-F3 PASS at the same root, the campaign runs "
            "through stages.run_campaign -- the PI's stop with no session is the stage's PI STOP REFUSED (exit 4; the "
            "RULING line 'with no checkpoint on disk'; no checkpoint written); a run interrupted at A2's first session "
            "keeps the sessions before it; the seat's adjudication with no pause is the stage's NO PAUSE TO ADJUDICATE "
            "(exit 4; the checkpoint unchanged); --resume with the PI's stop ends it PI-STOP (exit 0) -- the RULING line "
            "before the STAGE line, the stop recorded in the checkpoint only (stripped), the identity the campaign's "
            "(uncached, cap 120, hour cap 480, the committed lock's and proposal's sha256, the committed schedules' n), "
            "the floors and launch-count projection the driver's, G-F3's checkpoint the prior, the report written; and "
            "a later --resume is refused as ended (exit 4); no label printed",
            pre_c == (0, 5, 0) and rc_p0 == 4 and "PI STOP REFUSED" in err_p0 and p0_absent
            and f"RULING {name_c}: the PI's stop (sha16 {sha16(pi_f.read_text(encoding='utf-8').strip())}) offered with "
                f"no checkpoint on disk" in out_p0
            and isinstance(rc_i, stages._Interrupt) and len(ck_i["sessions"]) >= 1
            and ("A2", 0) not in [(r["template"], r["s"]) for r in ck_i["sessions"]]
            and rc_n == 4 and "NO PAUSE TO ADJUDICATE" in err_n and n_same
            and "offered with no pause unadjudicated" in out_n
            and rc_s == 0 and ri is not None and si is not None and ri < si and f"STAGE {name_c} PI-STOP path=uncached" in out_s
            and (camp_s.get("terminal") or {}).get("status") == "PI-STOP"
            and camp_s.get("pi_stop") == pi_f.read_text(encoding="utf-8").strip()
            and pi_f.read_text(encoding="utf-8").strip() not in out_s + err_s
            and ident_s.get("stage") == "campaign" and ident_s.get("path") == "uncached"
            and ident_s.get("reasoning_cap") == 120 and ident_s.get("hour_cap") == 480
            and ident_s.get("lock_sha256") == (ex_c or {}).get("lock_sha256") and ident_s.get("proposal_sha256") == prop_sha
            and ident_s.get("n") == {t: int(scheds[t]["n"]) for t in keys.TEMPLATES}
            and camp_s.get("floors") == fl and camp_s.get("launch_counts_projection") == dict(CAMPAIGN_LAUNCH_COUNTS)
            and str((ck_s.get("prior") or {}).get("checkpoint", "")).endswith("ckpt/" + CAMPAIGN_PRIOR_CKPT_NAME)
            and rep_s.is_file() and rc_e == 4 and "CAMPAIGN ENDED" in err_e
            and "DRIVER " not in out_s and "SNAPSHOT " not in out_s and not labelled(out_s + err_s + out_p0 + err_p0),
            (pre_c, rc_p0, type(rc_i).__name__, rc_n, rc_s, rc_e, err_s[-200:]))
        r_x = fresh("exit")
        ex_codes = {st_: stub_run(run_campaign, r_x, stub("campaign"), gates=r_x.parent / "gates",
                                  camp_stage=lambda *a, _s=st_, **k: {"status": _s})[0]
                    for st_ in ("COMPLETE", "CAP", "PI-STOP", "PAUSE", "STOP")}
        chk("mf3_sessions: the campaign's exit code is stages.EXIT_CODES of the stage's status (COMPLETE, CAP and PI-STOP "
            "0, PAUSE 3, STOP 4)", ex_codes == {"COMPLETE": 0, "CAP": 0, "PI-STOP": 0, "PAUSE": 3, "STOP": 4}, ex_codes)

    # --- the Qwen path with the loader and the stages trapped ------------------------------------------------------
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        rev = (ex_c or {}).get("weights_revision", "0" * 40)
        fake_snap = {"model_id": QWEN_MODEL_ID, "revision": rev, "snapshot_dir": "<selftest>/snapshots/" + rev,
                     "n_snapshots": 1, "offline": "1"}
        no_prior = ((stages, "prior_gate", lambda *a, **k: {}),)
        rul_dir = base / "rulings"
        rul_dir.mkdir()

        def rfile(nm: str, data) -> str:
            p = rul_dir / nm
            p.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))
            return str(p)
        adj_ok, pi_ok = rfile("adj.txt", "The seat's ruling (selftest).\n"), rfile("pi.txt", "The PI's stop (selftest).\n")
        adj_blank, adj_dir, pi_bad = rfile("blank.txt", " \n"), str(rul_dir), rfile("bad.txt", b"\xff\xfe")
        adj_one = rfile("one.txt", "Ruling one.\n")

        def fresh(nm: str) -> Path:
            r = base / nm / "mf3"
            schedule.write_schedule_files(r / "schedules")
            (base / nm / "gates").mkdir()
            return r

        def q_c(nm: str, over: dict | None = None, *, setup=None, pre=(), lic=None, resume_flag=False, argv_pre=(),
                drv=([], "d" * 64), snap=([], fake_snap), snapfn=None, loader=None, more=(), adj=None, pi=None):
            root = fresh(nm)
            if setup is not None:
                setup(root)
            before = tree_state(root.parent)
            fl_ = {**tflags, **(over or {})}
            argv = list(argv_pre) + ["campaign"] + [x for k, v in fl_.items() if v is not None
                                                    for x in ("--" + k.replace("_", "-"), v)]
            argv += (["--adjudication-file", adj] if adj is not None else []) + (["--pi-stop-file", pi] if pi else [])
            n0, s0 = len(loads), len(stage_calls)
            with contextlib.ExitStack() as st:
                st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", root))
                st.enter_context(mock.patch.object(guard, "GATES_DIR", root.parent / "gates"))
                st.enter_context(mock.patch.object(stages, "run_campaign", t_stage("campaign")))
                st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage("gate")))
                st.enter_context(mock.patch.object(stages, "run_gid_pair_f3", t_stage("gid")))
                st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: list(pre)))
                st.enter_context(gpatch("_load_qwen", t_loader if loader is None else loader))
                st.enter_context(gpatch("build_schedules", t_escape("build_schedules")))
                st.enter_context(gpatch("run_selftest", t_escape("run_selftest")))
                if drv is not None:
                    st.enter_context(gpatch("driver_problems", lambda: (list(drv[0]), drv[1])))
                if snapfn is not None:
                    st.enter_context(gpatch("qwen_snapshot", snapfn))
                elif snap is not None:
                    st.enter_context(gpatch("qwen_snapshot", lambda: (list(snap[0]), snap[1])))
                if lic is not None:
                    st.enter_context(mock.patch.object(stages, "licence_problems", lambda extra, **kw: list(lic)))
                for obj, attr, val in more:
                    st.enter_context(gpatch(attr, val) if obj is None else mock.patch.object(obj, attr, val))
                rc_, out_, err_ = run3(argv + (["--resume"] if resume_flag else []))
            return {"rc": rc_, "out": out_, "err": err_, "loads": len(loads) - n0, "calls": stage_calls[s0:],
                    "same": before == tree_state(root.parent), "root": root}

        def plant_qual(*, proposal=prop_sha, cap=120, status="PASS", stub_weights=False, stub_tag=False, stage_="qual"):
            # a G-F3 checkpoint (by default) at the campaign's prior path, its provenance carrying no stub tag
            def setup(root):
                cp = root / "ckpt" / CAMPAIGN_PRIOR_CKPT_NAME
                cp.parent.mkdir(parents=True, exist_ok=True)
                w = dict(rs.STUB_WEIGHTS) if stub_weights else {"weights_revision": "a" * 40, "weights_sha256": "b" * 64}
                ident = rs.Identity(stage=stage_, template_set=list(keys.TEMPLATES), lock_sha256="1" * 64,
                                    schedule_sha256="3" * 64, path="uncached", hour_cap=None,
                                    n=dict(QUAL_COUNTS) if stage_ == "qual" else {t: 1 for t in keys.TEMPLATES},
                                    audit_v2_sha16="4" * 16, ban_sha="5" * 16, backend_identifier="6" * 16,
                                    proposal_sha256=proposal, reasoning_cap=cap, **w)
                ck = rs.load_or_init(cp, ident, False)
                rs.append_provenance(ck, rs.provenance_record(
                    {"adapter": "qwen3.6-27b-4bit-mlx",
                     "apparatus": stages.STUB_MARK if stub_tag else "selftest-planted, no stub tag"}))
                if status is not None:
                    ck["stage_end"] = {"status": status, "fired": [], "adjudication": None}
                rs.write_checkpoint(cp, ck)
            return setup

        def plant_art(*, verdict="FAIL", cap=120, proposal=prop_sha, stub_tag=False, raw=None):
            def setup(root):
                p = root.parent / "gates" / gid_name
                if raw is not None:
                    p.write_text(raw, encoding="utf-8")
                    return
                tag = stages.STUB_MARK if stub_tag else "selftest-planted, no stub tag"
                p.write_text(json.dumps({"verdict": verdict, "identity": {"proposal_sha256": proposal,
                                                                         "reasoning_cap": cap},
                                         "provenance": [{"record": {"adapter": "qwen3.6-27b-4bit-mlx",
                                                                    "apparatus": tag}, "stamp": "selftest"}]}),
                             encoding="utf-8")
            return setup

        def camp(obj=None, *, raw=None, as_dir=False, as_fifo=False):
            # a campaign checkpoint at the campaign's path: a synthetic JSON object (the screen's and the mirror's
            # input), raw text, a directory or a FIFO
            def setup(root):
                cp = root / "ckpt" / ck_name
                cp.parent.mkdir(parents=True, exist_ok=True)
                if as_dir:
                    cp.mkdir()
                elif as_fifo:
                    os.mkfifo(cp)
                elif raw is not None:
                    cp.write_text(raw, encoding="utf-8")
                else:
                    cp.write_text(json.dumps(obj), encoding="utf-8")
            return setup

        def both(*setups):
            def setup(root):
                for s_ in setups:
                    s_(root)
            return setup

        def ck2(*, sessions=1, pauses=(), pi_stop=None, terminal=None, pending=False) -> dict:
            o = {"identity": {"unit": keys.UNIT, "stage": "campaign"},
                 "sessions": [{"template": "A1", "s": i} for i in range(sessions)],
                 "campaign": {"pauses": [dict(p) for p in pauses], "pi_stop": pi_stop, "terminal": terminal,
                              "end_look": None}}
            if pending:
                o[end_key] = {"status": "PAUSE"}
            return o
        look_ = {"kind": "look", "at_launches": 40, "adjudication": None, "arm": None}

        def tamper(root):
            f = root / "schedules" / f"{keys.UNIT}_campaign_A1s.json"
            f.write_bytes(f.read_bytes() + b"\n")
        v02_lock = ((stages, "committed", committed_but(CAMPAIGN_LOCK_FILE, ([], v02_text.encode("utf-8")))),)
        msg_top = "campaign takes no --selftest / --build-schedules / --out"
        P = plant_qual()

        def first_link_c(root):
            # the campaign's prior name a link to G-TIME-F3's first run's checkpoint (stage_prior_checkpoint refuses
            # it by the name it resolves to)
            d_ = root / "ckpt"
            d_.mkdir(parents=True, exist_ok=True)
            (d_ / FIRST_RUN_CKPT_NAME).write_text("{}", encoding="utf-8")
            (d_ / CAMPAIGN_PRIOR_CKPT_NAME).symlink_to(d_ / FIRST_RUN_CKPT_NAME)
        c_refused = {
            "missing": (q_c("missing", {"lock_file": None}), "campaign needs ['--lock-file']"),
            "other lock": (q_c("otherlock", {"lock_file": "CLAUDE.md"}), f"{name_c} cites LOCK-m-F3.md"),
            "v0.2's blob (no v1.0 lines)": (q_c("v02lock", more=v02_lock), "carries no whole line"),
            "malformed": (q_c("malformed", {"analyzer_sha256": "xyz"}), "analyzer_sha256 must be a sha256 hex digest"),
            "licence (d)": (q_c("lic_d", {"analyzer_sha256": z64}, more=no_prior),
                            "is not identity_extra's analyzer_sha256"),
            "renders": (q_c("renders", {"renders_sha16": "0" * 16}, lic=[], more=no_prior), "renders: RENDERS MISMATCH"),
            "preflight": (q_c("preflight", lic=[], pre=("ONE PROCESS: selftest",), more=no_prior),
                          "preflight: ONE PROCESS: selftest"),
            "an adjudication file blank": (q_c("adjblank", lic=[], setup=P, adj=adj_blank),
                                           "--adjudication-file " + adj_blank + ": blank"),
            "an adjudication file not a regular file": (q_c("adjdir", lic=[], setup=P, adj=adj_dir), "not a regular file"),
            "a PI-stop file not UTF-8": (q_c("pibad", lic=[], setup=P, pi=pi_bad), "unreadable as UTF-8 text"),
            "prior absent (real gate)": (q_c("noprior", lic=[]), "prior: PRIOR STAGE ABSENT"),
            "prior on the stub (real gate)": (q_c("stubprior", lic=[], setup=plant_qual(stub_tag=True)),
                                              "prior: PRIOR STAGE ON THE STUB"),
            "prior under another proposal (real gate)": (q_c("otherprop", lic=[], setup=plant_qual(proposal="2" * 64)),
                                                         "prior: PRIOR STAGE UNDER ANOTHER PROPOSAL"),
            "prior not ended (real gate)": (q_c("notended", lic=[], setup=plant_qual(status=None)),
                                            "prior: PRIOR STAGE NOT ENDED"),
            "prior ended STOP (real gate)": (q_c("priorstop", lic=[], setup=plant_qual(status="STOP")),
                                             "prior: PRIOR STAGE STOP"),
            "prior not G-F3's (real gate)": (q_c("priortime", lic=[], setup=plant_qual(stage_="time")),
                                             "prior: PRIOR STAGE MISMATCH"),
            "prior at another cap (real gate)": (q_c("prior60", lic=[], setup=plant_qual(cap=60, stub_weights=True)),
                                                 "prior: NOT THE FIXED CAP"),
            "G-ID artifact on the stub": (q_c("artstub", lic=[], setup=both(P, plant_art(stub_tag=True))),
                                          "artifact: G-ID ARTIFACT ON THE STUB"),
            "G-ID artifact at another cap": (q_c("art60", lic=[], setup=both(P, plant_art(cap=60))),
                                             "artifact: G-ID ARTIFACT AT ANOTHER CAP"),
            "G-ID artifact under another proposal": (q_c("artprop", lic=[], setup=both(P, plant_art(proposal="2" * 64))),
                                                     "artifact: G-ID ARTIFACT UNDER ANOTHER PROPOSAL"),
            "G-ID artifact unreadable": (q_c("artbad", lic=[], setup=both(P, plant_art(raw="not json"))),
                                         "artifact: G-ID ARTIFACT UNREADABLE"),
            "exists": (q_c("exists", lic=[], setup=both(P, camp(ck2()))), "checkpoint: CHECKPOINT EXISTS"),
            "ended": (q_c("ended", lic=[], setup=both(P, camp(ck2(terminal={"status": "CAP", "at_launches": 9})))),
                      "checkpoint: CAMPAIGN ENDED"),
            "ended --resume": (q_c("ended_r", lic=[], resume_flag=True,
                                   setup=both(P, camp(ck2(terminal={"status": "CAP", "at_launches": 9})))),
                               "checkpoint: CAMPAIGN ENDED"),
            "a directory at the checkpoint path": (q_c("ckdir", lic=[], resume_flag=True, setup=both(P, camp(as_dir=True))),
                                                   "exists and is not a regular file"),
            "an unreadable checkpoint": (q_c("ckbad", lic=[], resume_flag=True, setup=both(P, camp(raw="not json"))),
                                         "cannot be read as a campaign checkpoint"),
            "a checkpoint with an arm not Q-F3's": (q_c("ckarm", lic=[], resume_flag=True, setup=both(P, camp(ck2(
                pauses=[dict(look_, kind="schedule_exhausted", arm="A0")])))), "cannot be read as a campaign checkpoint"),
            "no pause to adjudicate": (q_c("nopause", lic=[], resume_flag=True, setup=both(P, camp(ck2())), adj=adj_ok),
                                       "ruling: NO PAUSE TO ADJUDICATE"),
            "a PI stop with no session": (q_c("pinosess", lic=[], setup=P, pi=pi_ok), "ruling: PI STOP REFUSED"),
            "an exhausted schedule": (q_c("exh", lic=[], resume_flag=True, adj=adj_ok, setup=both(P, camp(ck2(pauses=[
                dict(look_, kind="schedule_exhausted", at_launches=120, arm="A1")])))), "ruling: SCHEDULE EXHAUSTED"),
            "another PI stop": (q_c("otherpi", lic=[], resume_flag=True, pi=pi_ok,
                                    setup=both(P, camp(ck2(pi_stop="Another stop.")))), "ruling: CHECKPOINT MISMATCH"),
            "a ruling beside an end pending": (q_c("besidepend", lic=[], resume_flag=True, adj=adj_ok,
                                                   setup=both(P, camp(ck2(pending=True)))),
                                               "ruling: RULING BESIDE AN END PENDING"),
            "a ruling reused": (q_c("reused", lic=[], resume_flag=True, adj=adj_one, setup=both(P, camp(ck2(pauses=[
                dict(look_, adjudication="Ruling one."), dict(look_, at_launches=80)])))), "ruling: RULING REUSED"),
            "a ruling offered on a paused campaign without --resume": (q_c("offered_nores", lic=[], adj=adj_ok,
                setup=both(P, camp(ck2(pauses=[look_])))), "checkpoint: CHECKPOINT EXISTS"),
            "a checkpoint whose pauses are an object": (q_c("ckpobj", lic=[], setup=both(P, camp(dict(
                ck2(), campaign=dict(ck2()["campaign"], pauses={"x": 1}))))),
                "cannot be read as a campaign checkpoint"),
            "a checkpoint whose pauses are a number": (q_c("ckpint", lic=[], resume_flag=True, setup=both(P, camp(dict(
                ck2(), campaign=dict(ck2()["campaign"], pauses=7))))), "cannot be read as a campaign checkpoint"),
            "prior the first run's, its name a link to it": (q_c("priorlink", lic=[], setup=first_link_c),
                f"prior: PRIOR PATH REFUSED: {FIRST_RUN_CKPT_NAME} is G-TIME-F3's first run's checkpoint; {name_c} "
                f"takes G-F3's, {CAMPAIGN_PRIOR_CKPT_NAME}, by path"),
            "schedules": (q_c("sched", lic=[], setup=tamper, more=no_prior), "schedules: SCHEDULES NOT CLEAN"),
            "driver": (q_c("driver", lic=[], drv=(["selftest: uncommitted edits"], None), more=no_prior),
                       "driver: selftest: uncommitted edits"),
            "snapshot": (q_c("snapshot", lic=[], snap=(["selftest: no snapshot"], None), more=no_prior),
                         "snapshot: selftest: no snapshot"),
            "snapshot revision not the lock's": (q_c("snaprev", lic=[], snap=([], dict(fake_snap, revision="e" * 40)),
                                                     more=no_prior), "not the lock's weights revision"),
            "top-level --out": (q_c("topout", lic=[], argv_pre=("--out", str(base / "x"))), msg_top),
            "--selftest": (q_c("topsel", lic=[], argv_pre=("--selftest",)), msg_top),
            "--build-schedules": (q_c("topbuild", lic=[], argv_pre=("--build-schedules",)), msg_top),
        }

        def ref_ok(v, msg: str, ended: bool = False) -> bool:
            return (v is not None and v["rc"] == 2 and msg in v["err"] and "refused" in v["err"].lower()
                    and "refused" not in v["out"].lower() and v["loads"] == 0 and not v["calls"]
                    and "DRIVER " not in v["out"] and "SNAPSHOT " not in v["out"]
                    and "RULING " not in v["out"] and "Ruling one." not in v["out"] + v["err"]
                    and "selftest)." not in v["out"] + v["err"]
                    and not (ended and "CHECKPOINT EXISTS" in v["err"])
                    and v["same"] and not labelled(v["out"] + v["err"]))
        bad_c = {k: (v[0]["rc"], v[0]["err"][-240:]) for k, v in c_refused.items()
                 if not ref_ok(v[0], v[1], k.startswith("ended"))}
        chk(f"mf3_sessions: the campaign refuses before the load (exit 2, the refusal on stderr and not stdout, no DRIVER, "
            f"SNAPSHOT or RULING line, no ruling text printed, the loader and the stages never reached, the test root and "
            f"its gates directory unchanged, no label printed) in {len(c_refused)} cases: a flag missing; a lock other "
            f"than LOCK-m-F3.md; v0.2's blob, without v1.0's lines; a malformed hash; the licence's (d); the renders; "
            f"m:267's checklist; a ruling file blank, not a regular file, or not UTF-8; the prior (the real gate) absent, "
            f"on the stub, under another proposal, not ended, ended STOP, not G-F3's, at another cap, or its name a "
            f"link to G-TIME-F3's first run's checkpoint (G-F3's name given); G-ID-F3's "
            f"artifact on the stub, at another cap, under another proposal, or unreadable; the campaign's checkpoint "
            f"existing without --resume (a paused one offered a ruling too), ENDED with or without it (with no "
            f"CHECKPOINT EXISTS advice), a directory, unreadable, naming an arm not Q-F3's, or its pauses an object or "
            f"a number (with and without --resume); a ruling that does not fit -- no pause to adjudicate, a PI stop "
            f"with no session, an exhausted schedule, another PI stop, beside an end pending, reused; a tampered "
            f"schedule; the driver check; the snapshot check, and a snapshot revision not the lock's; a top-level --out, "
            f"--selftest or --build-schedules beside campaign (m's form, exactly, on stderr; the schedules writer and the "
            f"self-test never reached)",
            not bad_c and len(c_refused) == 44 and not escapes
            and all(c_refused[k][0]["err"] == f"refused: {msg_top}\n" for k in ("top-level --out", "--selftest",
                                                                                "--build-schedules")), (bad_c, escapes))
        ff_q: dict = {}

        def fifo_q():
            # m's O3-3 (its round 3) in m's form: a daemon thread joined with a timeout, released as above
            fq = both(P, camp(as_fifo=True))
            ff_q["adj"] = q_c("ckfifo_adj", lic=[], resume_flag=True, adj=adj_ok, setup=fq)
            ff_q["none"] = q_c("ckfifo", lic=[], resume_flag=True, setup=fq)
            ff_q["noresume"] = q_c("ckfifo_nr", lic=[], setup=fq)
        th_q = threading.Thread(target=fifo_q, daemon=True)
        streams_q = (sys.stdout, sys.stderr)
        th_q.start()
        th_q.join(30)
        q_hung = th_q.is_alive()
        if q_hung:
            for nm_ in ("ckfifo_adj", "ckfifo", "ckfifo_nr"):
                try:
                    os.close(os.open(base / nm_ / "mf3" / "ckpt" / ck_name, os.O_WRONLY | os.O_NONBLOCK))
                except OSError:
                    pass
            th_q.join(10)
            # a thread still hung holds run3's redirected stdout and stderr: the checks below print to this
            # self-test's own (round 2's S02 lost its later lines to the hung thread's buffer)
            sys.stdout, sys.stderr = streams_q
        ff_msg = "exists and is not a regular file (refused before it is opened)"
        chk("mf3_sessions: a FIFO at the campaign's checkpoint path is never opened on the Qwen path (m's O3-3; the "
            "three calls return within 30 s): the precheck refuses it before the load, in the refusal table's terms, "
            "offered a ruling and not, with --resume and without (there beside CHECKPOINT EXISTS)",
            not q_hung and all(ref_ok(ff_q.get(k_), ff_msg) for k_ in ("adj", "none", "noresume"))
            and "checkpoint: CHECKPOINT EXISTS" in (ff_q.get("noresume") or {}).get("err", ""),
            (q_hung, [((ff_q.get(k_) or {}).get("rc"), ((ff_q.get(k_) or {}).get("err") or "")[-160:])
                      for k_ in ("adj", "none", "noresume")]))
        multi = q_c("multi", {"renders_sha16": "0" * 16}, lic=["selftest licence"], pre=("ONE PROCESS: selftest",),
                    resume_flag=True, setup=camp(raw="not json"), drv=(["selftest: uncommitted edits"], None),
                    snap=(["selftest: no snapshot"], None))
        ref_lines = [ln for ln in multi["err"].splitlines() if ln.startswith("REFUSED")]
        chk("mf3_sessions: the campaign's precheck problems (the licence's, the renders', the prior gate's -- here G-F3's "
            "checkpoint absent -- an unreadable campaign checkpoint's and m:267's checklist's), the driver check's and "
            "the snapshot check's are refused together, in one REFUSED line naming the campaign (exit 2; no DRIVER or "
            "SNAPSHOT line; nothing loaded)",
            multi["rc"] == 2 and len(ref_lines) == 1 and multi["err"].count(f"REFUSED: {name_c}:") == 1
            and all(x in ref_lines[0] for x in (
                "licence: selftest licence", "renders: RENDERS MISMATCH", "prior: PRIOR STAGE ABSENT",
                "cannot be read as a campaign checkpoint", "preflight: ONE PROCESS: selftest",
                "driver: selftest: uncommitted edits", "snapshot: selftest: no snapshot"))
            and "DRIVER " not in multi["out"] and "SNAPSHOT " not in multi["out"] and multi["loads"] == 0, ref_lines)
        n0, s0 = len(loads), len(stage_calls)
        e_ = io.StringIO()
        seam_root = fresh("seam")
        seam_before = tree_state(seam_root.parent)
        bad_rx: list = []
        with contextlib.ExitStack() as st:
            st.enter_context(mock.patch.object(stages, "DEFAULT_OUT", fresh("seam_default")))
            st.enter_context(mock.patch.object(guard, "GATES_DIR", seam_root.parent / "gates"))
            st.enter_context(mock.patch.object(stages, "run_campaign", t_stage("campaign")))
            st.enter_context(mock.patch.object(stages, "run_gate_stage", t_stage("gate")))
            st.enter_context(mock.patch.object(stages, "run_gid_pair_f3", t_stage("gid")))
            st.enter_context(mock.patch.object(guard, "preflight_laptop", lambda: []))
            st.enter_context(gpatch("_load_qwen", t_loader))
            st.enter_context(contextlib.redirect_stderr(e_))
            st.enter_context(contextlib.redirect_stdout(io.StringIO()))
            rc_or = run_campaign(**{**tflags, "lock_file": "CLAUDE.md"}, resume_run=False, out_root=seam_root,
                                 pi_stop_file=pi_ok)
            for st_ in ("time", "id", "qual"):
                for kw_ in ({"adjudication_file": adj_ok}, {"pi_stop_file": pi_ok}):
                    # m's form (its round 1's M1-7; this wiring's review, MINOR-1): a fresh test root and a stub
                    # factory, inside the traps -- should the guard regress, the call reaches a trapped stage on the
                    # stub in a test directory, never data/mf3 or Qwen
                    try:
                        run_stage(st_, **tflags, resume_run=False, out_root=fresh(f"rx_{st_}_{next(iter(kw_))}"),
                                  adapter_factory=stub(st_), **kw_)
                        bad_rx.append((st_, next(iter(kw_))))
                    except ValueError:
                        pass
        ap_x = []
        for st_ in ("time", "id", "qual"):
            for fl_ in ("--adjudication-file", "--pi-stop-file"):
                rc_ap, _o_ap, e_ap = run3([st_, fl_, adj_ok])
                ap_x.append(rc_ap == 2 and "unrecognized arguments" in e_ap)
        chk("mf3_sessions: run_campaign with an out root and no stub factory refuses before anything -- before the "
            "identity and the ruling files -- exit 2, the loader and the stage never reached, the test root unchanged "
            "(time's seam case, carried); the ruling files are the campaign's alone: run_stage raises ValueError on "
            "either at time, id and qual, before anything (each call on a fresh test root with a stub factory, inside "
            "the traps: m's form), and time, id and qual refuse either flag at the command line (argparse, exit 2)",
            rc_or == 2 and "REFUSED: campaign: an out root names a test directory" in e_.getvalue()
            and "cites" not in e_.getvalue() and len(loads) == n0 and len(stage_calls) == s0
            and tree_state(seam_root.parent) == seam_before and not bad_rx and len(ap_x) == 6 and all(ap_x),
            (e_.getvalue()[-200:], bad_rx, ap_x))
        paused = camp(ck2(pauses=[look_]))
        rl = q_c("reach_load", lic=[], setup=P)
        rr = q_c("reach_ruling", lic=[], resume_flag=True, adj=adj_ok, setup=both(P, paused))
        rsh = q_c("shown", lic=[], setup=both(P, paused))
        rpd = q_c("pending_ok", lic=[], setup=both(P, camp(ck2(pending=True))))
        rpi = q_c("pi_ok", lic=[], resume_flag=True, pi=pi_ok, setup=both(P, paused))

        def order_of(res):
            ls = res["out"].splitlines()
            return [next((i for i, x in enumerate(ls) if x.startswith(p_)), None) for p_ in ("DRIVER ", "SNAPSHOT ",
                                                                                            "RULING ")]
        o_l, o_r, o_p = order_of(rl), order_of(rr), order_of(rpi)
        want_r = (f"RULING {name_c}: the seat's adjudication (sha16 {sha16('The seat' + chr(39) + 's ruling (selftest).')})"
                  f" offered for the pause at 40 launches (look)")
        chk("mf3_sessions: with every pre-load check clear -- the real prior gate passing a G-F3 checkpoint ended PASS at "
            "cap 120 that the stub did not write -- the campaign prints the DRIVER line, then the SNAPSHOT line, then, "
            "when it offers a ruling, the RULING line (the seat's adjudication for the pause at 40 launches, a look's; or "
            "the PI's stop), and only then reaches the loader (the trap: exit 4, no stage reached, the test root "
            "unchanged); a paused campaign offered no ruling passes without --resume (shown), and so does an end "
            "pending; each reaches the loader",
            all(x["rc"] == 4 and x["loads"] == 1 and not x["calls"] and "the Qwen loader was reached" in x["err"]
                and x["same"] for x in (rl, rr, rsh, rpd, rpi))
            and o_l[0] is not None and o_l[1] is not None and o_l[0] < o_l[1] and o_l[2] is None
            and None not in o_r and o_r[0] < o_r[1] < o_r[2] and want_r in rr["out"]
            and None not in o_p and o_p[1] < o_p[2] and "the PI's stop (sha16 " in rpi["out"]
            and order_of(rsh)[2] is None and order_of(rpd)[2] is None
            and rl["out"].splitlines()[o_l[0]] == (f"DRIVER {DRIVER_REL} {'d' * 64}: committed at HEAD "
                                                    f"{stages._git_head()}, working tree identical")
            and "selftest)." not in rr["out"] + rr["err"] + rpi["out"] + rpi["err"],
            [(x["rc"], x["err"][-160:]) for x in (rl, rr, rsh, rpd, rpi)])

        class Stand:
            def __init__(self, mid):
                self.model_id = mid
        order: list = []

        def seq(*answers):
            it = iter(answers)

            def f():
                order.append("snap")
                return next(it)
            return f

        def stand_loader():
            order.append("load")
            return Stand(QWEN_MODEL_ID)

        def stand_mid(mid):
            def f():
                order.append("load")
                return Stand(mid)
            return f
        moved = dict(fake_snap, revision="e" * 40)
        post = {
            "re-read refuses": (q_c("post_refuse", lic=[], setup=P, loader=stand_loader,
                                     snapfn=seq(([], fake_snap), (["selftest: gone"], None))),
                                ("STOP: SNAPSHOT RE-READ REFUSED", "selftest: gone")),
            "refs/main moved": (q_c("post_moved", lic=[], setup=P, loader=stand_loader,
                                     snapfn=seq(([], fake_snap), ([], moved))),
                                ("STOP: SNAPSHOT MOVED", f"before the load {rev}; after it {'e' * 40}")),
            "another model id": (q_c("post_mid", lic=[], setup=P, loader=stand_mid("other/model"),
                                      snapfn=seq(([], fake_snap), ([], fake_snap))),
                                 ("STOP: MODEL ID", f"the adapter loaded 'other/model', the snapshot check read "
                                                    f"'{QWEN_MODEL_ID}'")),
        }
        bad_post = {k: (v[0]["rc"], v[0]["err"][-200:]) for k, v in post.items()
                    if not (v[0]["rc"] == 4 and all(x in v[0]["err"] for x in v[1]) and not v[0]["calls"]
                            and v[0]["same"] and "SNAPSHOT re-read after the load: unchanged" not in v[0]["out"])}
        chk("mf3_sessions: after the load, the campaign STOPs (exit 4) before the stage on a re-read that refuses, a moved "
            "refs/main or another model id, each STOP naming its evidence, with no re-read line (time's post-load cases, "
            "carried)", not bad_post and len(post) == 3, bad_post)
        order.clear()
        ru = q_c("post_ok", lic=[], resume_flag=True, adj=adj_ok, setup=both(P, paused), loader=stand_loader,
                 snapfn=seq(([], fake_snap), ([], fake_snap)))
        call = ru["calls"][0][1] if ru["calls"] else {}
        want_prior = (ru["root"] / "ckpt" / CAMPAIGN_PRIOR_CKPT_NAME).resolve()
        chk("mf3_sessions: after the load and the re-read (snapshot, load, snapshot), the campaign reaches "
            "stages.run_campaign -- not run_gate_stage or run_gid_pair_f3 -- once, with campaign_floors(), "
            "CAMPAIGN_LAUNCH_COUNTS and CAMPAIGN_HOUR_CAP (480), G-F3's checkpoint at its out root as the prior, by path, "
            "the out root stages.DEFAULT_OUT, resume on, the identity with locked_path uncached at cap 120, the seat's "
            "adjudication as the file holds it and no PI stop (here the trap: exit 4)",
            ru["rc"] == 4 and [c[0] for c in ru["calls"]] == ["campaign"] and order == ["snap", "load", "snap"]
            and call.get("floors") == fl and call.get("launch_counts") == dict(CAMPAIGN_LAUNCH_COUNTS)
            and call.get("hour_cap") == 480 and type(call.get("hour_cap")) is int
            and Path(call.get("prior_ckpt", "")) == want_prior and Path(call.get("out_root", "")) == ru["root"]
            and call.get("resume") is True and (call.get("identity_extra") or {}).get("locked_path") == "uncached"
            and (call.get("identity_extra") or {}).get("reasoning_cap") == 120
            and call.get("adjudication") == "The seat's ruling (selftest).\n" and call.get("pi_stop") is None
            and "STOP: selftest: the stage was reached" in ru["err"] and ru["same"], (ru["rc"], order, sorted(call)))
    data_after = tree_state(real_out) if real_out.is_dir() else {}
    chk("mf3_sessions: the campaign checks loaded nothing and wrote nothing under data/mf3 -- the loader trap was reached "
        "5 times in all (each of the five cases that clear every pre-load check asserts its own one reach), the stage "
        "trap once (run_campaign, the post-load case), the schedules writer and the self-test never from a campaign "
        "invocation; data/mf3's file hashes are unchanged and stages.DEFAULT_OUT and guard.GATES_DIR are restored",
        data_before == data_after and stages.DEFAULT_OUT == real_out and guard.GATES_DIR == real_gates
        and len(loads) == 5 and [c[0] for c in stage_calls] == ["campaign"] and not escapes,
        (len(loads), [c[0] for c in stage_calls], escapes, sorted(set(data_before) ^ set(data_after))[:3]))


def run_selftest() -> int:
    results: list[bool] = []

    def chk(name, ok, got="", note="", *rest) -> None:
        ok = bool(ok)
        results.append(ok)
        tail = " ".join(_short(x) for x in (got, note, *rest) if x is not None and not (isinstance(x, str) and x == ""))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" {tail}" if tail else ""), flush=True)

    for m in MODULES:
        mod = importlib.import_module(f"valence_core.mf3.{m}")
        try:
            mod._selftest(chk)
        except (Exception, SystemExit) as e:                    # noqa: BLE001
            chk(f"{m}: _selftest raised", False, f"{type(e).__name__}: {e}")
    try:
        _selftest(chk)
    except (Exception, SystemExit) as e:                        # noqa: BLE001
        chk("mf3_sessions: integration selftest raised", False, f"{type(e).__name__}: {e}")
    print(f"  {sum(results)}/{len(results)} mf3 selftest checks pass", flush=True)
    return 0 if all(results) else 1


def main(argv: list[str] | None = None) -> int:
    shown = sys.argv if argv is None else [sys.argv[0]] + list(argv)
    print("INVOCATION: " + " ".join([sys.executable] + shown), flush=True)
    ap = argparse.ArgumentParser(description="PROPOSAL-m Q-F3 driver (self-test, schedules, hashes, G-SHAPE-F3, "
                                             "G-TIME-F3, G-ID-F3, G-F3, the Q-F3 campaign)")
    ap.add_argument("--selftest", action="store_true", help="model-free self-test of valence_core.mf3")
    ap.add_argument("--build-schedules", action="store_true", help="write Q-F3's schedule files + manifest")
    ap.add_argument("--out", default=None, help="output directory for --build-schedules")
    sub = ap.add_subparsers(dest="cmd")
    g = sub.add_parser("gshape", help="G-SHAPE-F3 (m:290), model-free; canonical without --out")
    g.add_argument("--out", dest="gshape_out", default=None, help="a test directory (never of record)")
    h = sub.add_parser("hashes", help="the hashes LOCK-m-F3 v0.1 names (Q1 (C2)) and the weights binding")
    h.add_argument("--snapshot-dir", default=None, help="the hub snapshot directory (default: the cache's of record)")
    for c in WIRED_CMDS:
        if c == "campaign":
            t = sub.add_parser(c, help=STAGE_HELP[c] + "; " + CAMPAIGN_PAUSES,
                               description="The Q-F3 campaign (m:298, m:361) on Qwen under LOCK-m-F3 v1.0. "
                                           + CAMPAIGN_PAUSES + ".")
        else:
            t = sub.add_parser(c, help=STAGE_HELP[c])
        for k in TIME_FLAGS:
            t.add_argument("--" + k.replace("_", "-"), default=None, help=TIME_FLAG_HELP[k])
        t.add_argument("--resume", action="store_true", help=f"continue {STAGE_NAMES[c]}'s checkpoint (skip-only)")
        if c == "campaign":
            t.add_argument("--adjudication-file", dest="adjudication_file", default=None,
                           help="a UTF-8 text file, named for nothing it says (its path is printed): the seat's ruling "
                                "on the campaign's unadjudicated pause (a look's; an exhausted schedule's only beside "
                                "the PI's stop), for the invocation that resumes it -- after an interrupted run that "
                                "offered it alone, re-run with --resume alone (its text recorded in the checkpoint "
                                "only, never printed; the RULING line carries its sha16, and, where it is recorded as "
                                "the pause's ruling, the report (the pause's adjudication_sha16) and a later NO PAUSE "
                                "TO ADJUDICATE refusal); with --resume")
            t.add_argument("--pi-stop-file", dest="pi_stop_file", default=None,
                           help="a UTF-8 text file, named for nothing it says (its path is printed): the PI's stop -- "
                                "terminal, analyzed as obtained; it ends a look's pause, and alone ends an exhausted "
                                "schedule's; after an interrupted run that offered it, re-run with --resume and the "
                                "same ruling files (beside an end pending, without the flags a RULING BESIDE AN END "
                                "PENDING refusal names; its text recorded in the checkpoint only, never printed; the "
                                "RULING line carries its sha16, and where its text is the pause's ruling (it ends a "
                                "pause offered without --adjudication-file) the report (that pause's "
                                "adjudication_sha16) and a later NO PAUSE TO ADJUDICATE refusal); with --resume")
    for c in REFUSED_CMDS:
        sub.add_parser(c, help=f"{STAGE_NAMES[c]}: refused until its step")
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return int(e.code) if isinstance(e.code, int) else 2
    if a.cmd in WIRED_CMDS and (a.selftest or a.build_schedules or a.out is not None):
        print(f"refused: {a.cmd} takes no --selftest / --build-schedules / --out", file=sys.stderr)   # m's form
        return 2
    if a.selftest:
        return run_selftest()
    if a.build_schedules:
        return build_schedules(a.out)
    if a.cmd == "gshape":
        return run_gshape(a.gshape_out)
    if a.cmd == "hashes":
        return hashes(a.snapshot_dir)
    if a.cmd in WIRED_CMDS:
        rul = ({"adjudication_file": a.adjudication_file, "pi_stop_file": a.pi_stop_file} if a.cmd == "campaign"
               else {})
        return run_stage(a.cmd, proposal_file=a.proposal_file, lock_file=a.lock_file,
                         analyzer_sha256=a.analyzer_sha256, package_sha256=a.package_sha256,
                         renders_sha16=a.renders_sha16, resume_run=a.resume, **rul)
    if a.cmd in REFUSED_CMDS:
        print(refusal(a.cmd), flush=True)
        return 2
    print("REFUSED: no action (--selftest, --build-schedules, hashes, gshape, time, id, qual or campaign)", flush=True)
    return 2


if __name__ == "__main__":
    sys.exit(main())
