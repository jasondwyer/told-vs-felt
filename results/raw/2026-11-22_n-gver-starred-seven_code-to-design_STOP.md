# n — seven starred readings for the seat before G-VER's run: GV1, GV4, GV6, GV9, GV11, GV13 and GV14 (code → design)

*The n-build session (Code), PI date 2026-11-22. For the seat, before G-VER of record's run (n §8 step 12). The PI's
word governs only the nudge to the seat.*

*Where things stand:*
- *LOCK-n v0.1 is committed at `deabf3f`, sha256 `88d9fe7b…e9d5`. G-TIME-n (step 11) ran under it, COMPLETE
  (`7d01b02`). The seat accepted its record at the third sitting of 2026-11-21 (ans21c:15), and the PI's cap is 4 h of
  model time (rt21c:21).*
- *G-VER of record has no stage command. The driver's `gver-trial` is "the BUILD's site-check trial, never of record"
  (drv:16–20), and the driver says "Stages G-VER, the campaign and G-READ-n are wired at their own steps." (drv:239;
  likewise L:997–998).*
- *A read-only survey of the texts, at `7d01b02`, returned 13 open questions. Code's readings GV1–GV16 answer them as
  PINs. Code's addendum then mapped the third sitting's routed items onto them, with no PIN changed.*
- *The PI's answer, relayed verbatim by the coordinating session on 2026-11-22, was "Build on the PINs". So the build
  goes ahead on GV1–GV16 as PINs, in the driver alone (GV2).*
- *The seven starred readings go to the seat before the run, not before the build. That is G-TIME-n's order: its
  block, `2ca24e8`, went in before its BUILD, `91f0d35`.*
- *The third sitting routed G-VER's launch files, the box's run and its entry, with "a G-VER-STOP of any cause is a
  STOP for the seat before any read" (item N.3, rt21c:22–23), and kept the box up through G-VER and the campaign (item
  C.7, rt21c:39). Its raw read the entries of `7d01b02` and `b40ce59` (ans21c:3), so these readings were not before it.*

*Sources, by sha256 or commit:*
- *G-VER's spec raw, `results/raw/2026-11-22_n-gver_spec.md`, committed with this block:*
  - *§1, Code's readings GV1–GV16 as sent (`d73c2b8e…976e`, 136 lines);*
  - *§2, Code's addendum on the third sitting's items, as sent (`775ad17d…be51`, 46 lines);*
  - *§3, the coordinating session's routing of them, with the PI's answer;*
  - *§4, the survey's brief;*
  - *§5, the survey's report (`3a40ac89…8989`, 232 lines, compiled at `7d01b02`).*
- *The texts: PROPOSAL-n v0.2 (`PROPOSAL-n-bk-reconciliation-v0_2.md`, cited n:line); LOCK-n v0.1 (`LOCK-n.md`, cited
  L:line); ADDENDUM-n1 (A-n1:line).*

*Cited forms:*
- *ans20b: is `results/raw/2026-11-20_n-lock-v0_1-read_design-to-code_answers.md`;*
- *ans21b: is `results/raw/2026-11-21_n-gtime-starred-seven_design-to-code_answers.md`;*
- *ans21c: is `results/raw/2026-11-21_n-gtime-record-read_design-to-code_answers.md`;*
- *rt21b: is `results/raw/2026-11-21_second-sitting_pi-routing.md`;*
- *rt21c: is `results/raw/2026-11-21_third-sitting_pi-routing.md`;*
- *mF3ans: is `results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md`;*
- *box: is `results/raw/2026-11-18_box-gpu_design-to-code_answers.md`;*
- *R: is `RESULTS.md` at `cd6b30d`, this block's parent; its line anchors move with every entry;*
- *drv: is `scripts/n_sessions.py`, n_analyze: is `scripts/n_analyze.py`, and verify:, ids:, schema: and guard: are the
  modules of that name under `valence_core/n/`. Every code file:line is at `cd6b30d`, where no code has changed since
  `7d01b02` (the driver's last change is `91f0d35`).*

*Code reads, builds and asks. Every reading below is Code's, and the seat rules each one; Code adjudicates none.*

## 0. The short form

- **Seven readings.** Each comes with its texts, what Code will build, and what another answer would change.
- **They must be ruled before G-VER's run, not before its build.**
  - Three of them shape the run: GV1, what the run is; GV4, which pins it holds; and GV9, the record and which ends
    write one. After the run, other pins (GV4) mean running it again; another record form (GV9) means running it
    again or re-deriving the field from the raw; and "not a step" (GV1) leaves the record as one more check. A re-run
    costs seconds to minutes of pod time: one tokenizer load and the decode (GV12).
  - The other four change no code and no read: GV6 (what a STOP at step 12 means for step 13 and the campaign), GV11
    (v1.0's text), GV13 (a box change) and GV14 (the seat's read). They can be ruled after the run. GV6 binds only if
    the run STOPs.
- **The addendum's open points,** as the routing names them, are in GV9 and GV11. The addendum also leaves GV13's
  re-run list open, carried in GV13:
  - GV9 with GV5, against N.3's "a G-VER-STOP of any cause is a STOP for the seat before any read". As GV5 pins it, a
    refusal before G-VER exits 1 and writes no record;
  - GV11: N.4's list does not name G-VER's record.
- **One correction of Code's own, in GV4:** GV4 as sent lists MANIFEST.json's sha256 among the pins held before
  G-VER. L:543 names the manifest's pin among G-VER's own causes, so Code now reads a mismatch as G-VER's STOP, with
  the record, and not as a refusal. The seat rules on it with Q2.
- **The dependencies.** G-VER's run waits for:
  - the seat's answers on the seven. This is the coordinating session's reading, which it has put to the PI. The third
    sitting's short form has G-VER "already routed and runs without waiting for the seat" (ans21c:11), but these
    readings were not before that raw (ans21c:3);
  - the BUILD's commit;
  - the launch files, relayed to the box by the coordinating session;
  - the box itself, up through G-VER and the campaign ("[stays up]", rt21c:39).
- **The questions** are Q1–Q7 in §3, one per reading.

## 1. The seven (to be built on them as PINs)

**GV1 — what step 12 is (the survey's open question 1).**
- *Code's reading:* a stage of its own, with a record.
  - **The run:** `verify.verify` on the committed ids of record, once, on the box of record, under LOCK-n v0.1. It
    writes a record that is committed with its entry, "G-VER (n)".
  - **What it adds** to the G-VERs the BACKEND extension and G-TIME-n run before their loads. The extension's PASS was
    under the (i)–(iv) pin, before `516b60f` (R:6419); G-TIME-n's is at the current package, ids and pin. G-VEC and
    G-CAL-n run no G-VER: the driver calls `verify.verify` at drv:438 (gver-trial) and drv:1073 (`_gver_tokenizer`, the
    two stages' G-VER at drv:1192 and :4292) alone.
    - (a) a record of its own, committed. The stages' G-VER lines exist only in their raws;
    - (b) the decoding tokenizer's files hashed against their pins (GV3). The stages check the weights folder by byte
      counts alone (drv:636–649);
    - (c) MANIFEST.json's sha256 compared with the pin, printed and recorded. `verify` checks the pin
      (verify:86–89), but its report carries neither the sha256 nor `pin_ok` (verify:142–144); a failed pin shows only
      as a problem line. The stages already record the sha256 as their identity's `rendering_id` (drv:1174, :4277;
      L:218–220). What (c) adds is the comparison with the pin, in a G-VER record;
    - (d) the lock's pins held at the run and recorded (GV4).
  - **Against the m precedent:** for m the seat ruled "G-VER is the verifier, not a step" (mF3ans:1), "it has no entry
    of its own" (mF3ans:10). n's own texts give G-VER a step and an entry, so Code reads that ruling as not carrying
    to n.
- *The texts:*
  - n:159: "12. G-VER." between "11. G-TIME-n; the PI sets the cap." and "13. Commit LOCK-n v1.0 with D_n.";
  - n:161: the entries list names "`G-VER (n)`";
  - n_analyze:129: "G-VER (n)" is among the gate stages (`GATE_STAGES`) whose STOP gives the Clock's
    `clock:gate-stopped` cause (n_analyze:121–122);
  - drv:216, GT7: the G-VER at G-TIME-n's start is "not of record (n §8 step 12's is)", accepted at ans21b:38;
  - rt21c:22–23, item N.3: "G-VER of record (step 12): launch files to the coordinating session first, the box's run,
    its entry"; and before it rt21b:30, the second sitting's "then G-VER's launch files (step 12) without waiting for
    the seat. [go]";
  - mF3ans:1 and :10, the m ruling.
- *As Code will build it:* a `gver` command in the driver alone (GV2). It runs once, on the box (GV3), and writes
  `data/n/gver/gver.json` at PASS and at STOP (GV9). Its entry is "G-VER (n)".
- *Another answer:*
  - "Not a step", as for m: the command goes unused and nothing runs on the box. The stages' G-VER lines stand as they
    are, and the campaign's own G-VER is the gate before its reads (GV7).
  - Ruled after a run: the record stands as one more check and enters nothing.

**GV4 — the pins held before G-VER (the survey's open question 3).**
- *Code's reading:* under LOCK-n v0.1, the stage holds G-TIME-n's preparation checks where they bind a run that loads
  a tokenizer and no weights (drv:4224–4290):
  - the pod (`CHARACTERIZED_POD`, `emw1e4embiwe9b`);
  - the weights folder: it holds exactly its files at their byte counts, and its aggregate sha256 is the lock's
    (`36f05404…0fdb`, L §17). The tokenizer is read from it;
  - the driver of record: HEAD's committed bytes for a run of record (drv:1156–1158; G-TIME-n's own check,
    drv:4249–4251);
  - `LOCK-n.md`: HEAD's committed bytes at the lock's sha256 (`88d9fe7b…e9d5`);
  - the package and its closure, the lock's (`06b55761…1d39` and its twelve files, L §18). `verify.py` is in the
    package (guard:31–32), whose hash covers it (guard:4–5);
  - the environment's provenance, bridged to the characterization's identifier `4ed3f2c70fe8afbf` (R6), and n's
    backend identifier, the lock's `8264f719efd347a9` (L §17). No model loads, but the decode runs under these
    libraries.

  With them, GV3's check: before the decode, the tokenizer files that `ids.TOKENIZER_FILES` names are hashed in the
  weights folder, and each must be the model manifest's pin (`ids.pinned_tokenizer_sha256s`; L:196–203). The same
  folder holds `vocab.json` and `merges.txt`, which the model manifest pins too and a tokenizer load from that folder
  may read; GV3 hashes the three named files alone.

  **The ids of record, corrected (Code's, declared).** GV4 as sent lists "the ids of record: MANIFEST.json's sha256 the
  pin" among the pins held before G-VER, so that a mismatch would be a refusal. But L:543 names "the manifest's pin"
  among G-VER's own causes. So Code's reading is now:
  - MANIFEST.json's sha256 is printed beside the pin (`ids.MANIFEST_OF_RECORD`, `53a8cd74…99d8`, L:187–189) before
    G-VER, and `verify` itself holds it (`pin_ok`, verify:86–89);
  - a mismatch is G-VER's STOP, with the record (`manifest.equal` false; GV9), and not a refusal.

  Not held:
  - cuBLAS's setting and numpy's stream known answer, since nothing runs on the GPU and nothing is drawn;
  - the rest of G-TIME-n's preparation, which binds a run that loads weights and reads: the rulings files
    (drv:4235–4237); G-VEC's record and G-CAL-n's record and dose map, the rest of `gtime_lock_inputs`
    (drv:3863–3871), whose LOCK-n.md part GV4 holds; the stage identity (drv:4276–4280); the plan and the campaign's
    read plan (drv:4281–4290); and, just before that range, the benchmark folder's checks (drv:4216–4223).

  No schema stage identity: `schema.STAGES` is campaign, time and backend-ext (schema:256), and a schema stage would
  move L §18's pin (GV2). The record carries every pin it held (GV9).
- *The texts:*
  - L:3–4: v0.1 is of record "until LOCK-n v1.0 supersedes it at step 13";
  - ans20b:57: the lock's sha256 is "the figure every stage identity from here carries as `lock_sha256`";
  - A-n1:28 (§1.5): "rendering and spans" means `MANIFEST.json`'s sha256, the three versions, the tokenizer files'
    sha256s, and the span convention;
  - L:187–189 and L:196–203; L §17 (L:746–774) and L §18 (L:781–813);
  - schema:17–18: "G-VER's reconstructions are other records, not specified here".
- *As Code will build it:* one function holds the pins before the tokenizer loads. A pin off its value is a refusal:
  exit 1, no record (GV5; and GV9's open point).
- *Another answer:*
  - more pins (cuBLAS's setting, the stream's known answer) or fewer: the one function changes;
  - a schema stage identity: a package change. That moves L §18's pin, which needs a lock version.

  After the run, the record holds the pins it held, and a different set means running it again.

**GV6 — a STOP at step 12 (the survey's open question 6).**
- *Code's reading:* L:543 binds: "a STOP for the seat, never a pause and never an exclusion; no read is launched and
  the campaign does not start".
  - LOCK-n v1.0 (step 13) is not committed before the seat rules on the STOP and on any re-specification it locks.
  - If D_n (2026-12-15, L:985) passes first, the unit is NOT-RUN under n:134, cause `clock:gate-stopped`, stage
    "G-VER (n)" (n_analyze:121–122 and :129).
  - Nothing re-runs before the ruling.
- *Met in part by the third sitting:* N.4 places v1.0's draft "after G-VER's PASS" (rt21c:24; ans21c:72). So a STOP
  leaves no draft before the seat rules. The D_n clause is untouched.
- *The texts:* L:543; ans20b:41; n:134 ("a gate STOPPED and no re-specification was locked"); L:985.
- *As Code will build it:* a STOP exits 2 with the record written (GV9), and the entry is a STOP block for the seat.
  Nothing in the driver depends on what the STOP means for v1.0.
- *Another answer:* changes no code and no read.

**GV9 — the record (the survey's open question 4).**
- *Code's reading:* `data/n/gver/gver.json`, schema `n-gver-v1`, written by the driver at PASS and at STOP, and
  committed with the entry.
  - **It holds:**
    - `verify`'s report as returned: its nine keys, with `first_problems` masked as `verify` masks them;
    - the status;
    - MANIFEST.json's sha256 and the pin, and whether they are equal;
    - the tokenizer files' sha256s;
    - the lock's sha256, the package and its closure, n's backend identifier, the characterization's identifier
      (R6), the pod, the weights' aggregate sha256 and the driver's sha256;
    - the environment's versions;
    - the tokenizer's load and the decode's durations, in ms.
  - **It holds no token id** (`verify`'s report holds none) and no stamp (GV10). The driver checks the record against
    itself before it writes, and once more on disk.
  - **Committed** with the entry, by path, with `.gitignore` lines admitting `data/n/gver/gver.json` alone (the BUILD
    adds them, as G-TIME-n's did), and the raw: the stage's stdout, the out file.
  - **No stage report:** the schema's stage report is for the three stages that write read records (schema:14–18,
    :152–156; `STAGES`, schema:256), and G-VER of record reads nothing.
- *The addendum's open point, with GV5,* against N.3's "a G-VER-STOP of any cause is a STOP for the seat before any
  read" (rt21c:22–23). As GV5 pins it:
  - exit 0 is PASS, with the record;
  - exit 2 is `verify`'s STOP, with the record. A MANIFEST.json off its pin is among its causes (L:543; GV4,
    corrected);
  - exit 1 is a refusal before G-VER: a pin off its value, a tokenizer file off its pin, a driver that is not HEAD's
    committed bytes, another pod, an ids file off MANIFEST.json's sha256 or record count (`ids.load`), or a session
    set that is not BK's (`sessions.load_sessions`). It writes no record, and the out file is its only trace.

  Every end but PASS goes to the seat, and no read follows it. Code's reading is that a refusal is not a G-VER-STOP,
  because G-VER has not run. The texts nearest it point two ways:
  - at G-TIME-n's smoke, "A refusal at the smoke is a FAIL of the launch, Code's to fix" (ans21b:39);
  - at G-TIME-n itself, a refusal before any read shared exit 2 with G-VER's STOP (GT6, drv:203–205 and
    drv:4342–4348; accepted at ans21b:38).

  And a tokenizer file off its pin is also the kind of mismatch the respawn protocol's INTEGRITY step makes an
  incident: "stop, touch nothing, escalate" (CLAUDE.md, the respawn protocol's step (i)).
- *The texts:*
  - schema:1197: a STOP's `record_sha256` is "the STOP's record (G-VER's report; the PI's stop raw), by sha256";
  - schema:187–193: "A G-VER-STOP comes before any read: its report holds no record and no pause";
  - drv:58–59, the BACKEND extension's reading "at backend-ext the raw is the STOP's record; no stage report",
    flagged and unruled (R:6452–6455);
  - G-TIME-n's artifact `n-gtime-v1`, the driver's own form beside the schema's (GT11).
- *As Code will build it:* one writer and one checker in the driver, and the `.gitignore` lines in the BUILD.
- *Another answer:*
  - the raw as the record, with no artifact (the BACKEND extension's form): the writer goes;
  - a refusal counted as a G-VER-STOP of any cause: the refusal path writes the record, with status STOP and the
    refusal's cause in place of `verify`'s report, and exits 2. That is a small change to the BUILD, before the run;
  - another field set: the writer and the checker change.

  After the run, a change to the record's form means running it again, or re-deriving it from the raw where the raw
  prints the field.

**GV11 — does G-VER's record enter LOCK-n v1.0 (the survey's open question 10)?**
- *Code's reading:* yes. v1.0 cites the "G-VER (n)" entry and the record's sha256 as the gate the campaign follows,
  beside G-TIME-n's projections.
- *The addendum's open point:* N.4's list is n:120's (rt21c:24–29), and it names no G-VER record.
- *The texts:*
  - n:120: "Projections, the cap, D_n, hashes of this document, the lock chain, the analyzer, BK's input files.";
  - rt21c:24–29, item N.4;
  - `LOCK-m-F3.md`:273: m's v1.0 named its G-VER ("G-VER, read as G-F3's per-record verification").
- *As Code will build it:* nothing in the driver. It is v1.0's text at step 13.
- *Another answer:* v1.0 without it. That changes no code and no read.

**GV13 — a box change (the survey's open question 12).**
- *Code's reading:* a new pod re-runs the characterization and the BACKEND extension first, then G-TIME-n by default
  (ans21b:27). Code's reading adds G-VER of record to that list after them, by default, since it is the box of
  record's. The spend is the PI's (box:31).
  - C.7 keeps the box up through G-VER and the campaign (rt21c:39), so a box change is less likely. What re-runs on
    one stays the seat's.
- *The texts:* ans21b:27; n:101, "a box change restarts the campaign; gate stages may span boxes"; box:31; CLAUDE.md's
  respawn protocol.
- *As Code will build it:* the pod pin (GV4) refuses any other pod, with exit 1. On a new pod, the driver's pod pin
  changes for every stage, G-VER's with them.
- *Another answer:* G-VER not re-run on a new box, or re-run at another place in the list. That changes no code.

**GV14 — the seat's read (the survey's open question 13).**
- *Code's reading:* the entry, with the record and the raw, goes to the seat. The seat's G-VER read comes before step
  13's commit.
- *Met in part by the third sitting:*
  - "Owed by the seat, unchanged: LOCK-n v1.0's draft read; G-VER's read" (ans21c:62);
  - the seat reads v1.0's draft "whole before the commit" (rt21c:29).

  Neither says that G-VER's read precedes step 13's commit.
- *The texts:* ans21b:59 and ans21c:62; rt21c:24–29.
- *As Code will build it:* nothing in the driver. The order is the seat's.
- *Another answer:* changes no code and no read.

## 2. The dependencies, and what Code does meanwhile

- **The build goes ahead on GV1–GV16 as PINs** (the PI's "Build on the PINs"), declared in its BUILD entry.
  - It is in the driver alone, so `valence_core/n/` stays at `06b55761…1d39`.
  - It comes with self-tests in battery windows the coordinating session grants, one blind review, one values-check,
    and the BUILD's commit window.
- **G-VER runs only after** the seat's answers on the seven, the BUILD's commit, and the launch files' relay to the
  box.
  - A ruling against a PIN before the run changes the driver before the launch files.
  - After the run, each reading's "another answer" line above says what a different ruling costs.
- **G-VER's ends, pre-declared in the build** (GV5):
  - PASS: exit 0, the record written;
  - G-VER's STOP, a MANIFEST.json off its pin among its causes: exit 2, the record written. It is a STOP for the
    seat; no read follows;
  - a refusal before G-VER, or any other failure: exit 1, with no record, as GV5 pins it (GV9's open point).

  The pass rule is `verify`'s own (verify:140–141), with GV3's hashes and GV4's pins held before it.
- **The nine readings that are not starred** (GV2, GV3, GV5, GV7, GV8, GV10, GV12, GV15 and GV16) are Code's, as
  G-TIME-n's unstarred readings among GT1–GT17 were. They are in the spec raw's §1, and the BUILD entry declares them.
- **The survey's declared departures (eight items) and Code's own.** The survey's are in the spec raw's §5, the
  report's last section, for the seat to class. Code's are in the entry that commits this block.

## 3. The questions for the seat

- **Q1 (GV1).** Is step 12 a stage of its own, with its record and its entry "G-VER (n)"? Or is it, as for m, not a
  step?
- **Q2 (GV4).** Are the pins held before G-VER these: G-TIME-n's preparation where it binds a run that loads no
  weights, with the tokenizer files' hashes, and no schema identity? If not, which?
  - Is the manifest's pin G-VER's own cause, a mismatch G-VER's STOP with the record (L:543; Code's correction of
    GV4 as sent)?
  - Should GV3's hash check cover every file the tokenizer load may read, `vocab.json` and `merges.txt` with the
    three `ids.TOKENIZER_FILES` names?
- **Q3 (GV6).** After a STOP at step 12, does LOCK-n v1.0 wait for the seat's ruling on the STOP and on any
  re-specification it locks, with D_n's NOT-RUN (`clock:gate-stopped`) if D_n passes first?
- **Q4 (GV9).** Is the record `data/n/gver/gver.json` (`n-gver-v1`), written at PASS and at STOP and committed with
  the entry? And is a refusal before G-VER a G-VER-STOP of "any cause" under N.3?
  - If it is, the refusal writes the record and exits 2.
  - If it is not, it exits 1 with no record, as GV5 pins it.

  And is a tokenizer file off its pin handled as a respawn INTEGRITY incident (stop, touch nothing, escalate)?
- **Q5 (GV11).** Does LOCK-n v1.0 cite the "G-VER (n)" entry and the record's sha256?
- **Q6 (GV13).** If the box changes before the campaign, does G-VER of record run again after the characterization,
  the BACKEND extension and G-TIME-n?
- **Q7 (GV14).** Does the seat's G-VER read come before step 13's commit?
