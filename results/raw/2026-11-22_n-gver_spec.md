# n — G-VER of record's specification as the texts state it, Code's readings GV1–GV16 with its addendum, and the coordinating session's routing of them

PI date 2026-11-22. Code (the n-build session).

**What this raw holds.** It serves the seat's read of the seven starred readings (the block committed beside it) and
G-VER of record's BUILD:
- **§1, Code's readings GV1–GV16 as sent, verbatim** (`d73c2b8e…976e`, 136 lines). They went to the coordinating
  session as a file in Code's scratch folder, named by its path and sha256, and the coordinating session re-hashed it
  equal before it routed them (§3). It is in no other repository file.
- **§2, Code's addendum as sent, verbatim** (`775ad17d…be51`, 46 lines): the third sitting's routed items set against
  GV1–GV16, with no PIN changed. It went and was re-hashed as §1 was. It is in no other repository file.
- **§3, the coordinating session's message routing them, with the PI's answer, verbatim** (`503e7a99…e748`, 26
  lines). It is in no other repository file.
- **§4, the survey's brief** (`8e39c8d7…c9a1`, 79 lines). One change: the repository's full path, on its second line,
  is written `<repo>` (`a4d46c63…4b9e`).
- **§5, the survey's report, verbatim** (`3a40ac89…8989`, 232 lines). A subagent compiled it read-only at HEAD
  `7d01b02`: the specification of G-VER of record as the texts state it, with a citation for its claims, and the
  questions the texts leave open. It was extracted from the subagent's hand-back by `jq` when it returned, on
  2026-11-21. Its departures are in its last section, for the seat to class.

**The cited lines.** Every file:line in §1, §2 and §5 is the repository's at `7d01b02`. §2's citations of the third
sitting's raw are of a file that was untracked at `7d01b02` and is committed unchanged at `cd6b30d`. Since `7d01b02`,
only `RESULTS.md` and `.gitignore` have changed among the cited files (HEAD `cd6b30d`):
- `cd6b30d` inserted 331 lines in `RESULTS.md`, in three places (`git diff -U0 7d01b02 cd6b30d -- RESULTS.md`), so an
  R: anchor moves by where it falls: lines 24–313 by +304, 314–536 by +320, and 537 on by +331. §1's R:6121–6124 at
  `7d01b02` is R:6452–6455 at `cd6b30d`;
- it inserted one line in `.gitignore`, after line 172, so its lines 173 on move by +1. §5's `.gitignore`:262–343 is
  :263–344 at `cd6b30d`.

**Four citations and one claim in §1, as sent, are imprecise, and GV4 takes a correction.** §1 stays verbatim; the
block carries each as below.
- GV1's "G-VER is the verifier, not a step … it has no entry of its own" cites mF3ans:10. The first words are
  mF3ans:1, the raw's title; "it has no entry of its own" is mF3ans:10.
- GV9's "(`verify`'s report holds none; n:130)": n:130 is n's blinding paragraph, which keeps margins out of stdout;
  it names no token id. The block rests that claim on `verify`'s report alone.
- GV9's "(schema.py:187–193)": those lines say that a G-VER-STOP's report holds no record and no pause. The stage
  report's scope is schema.py:14–18 and :152–156.
- GV8's "`expect_n` is 160 (verify.py:77–78)": the 160 is verify.py:71's default, `schema.N_SESSIONS`; :77–78 is the
  count check.
- GV1's claim "(the BACKEND extension's and G-TIME-n's, PASS at the current package, ids and pin)": the extension's
  PASS was under the (i)–(iv) pin, before `516b60f` (R:6419); only G-TIME-n's is at the current package, ids and pin.
- **GV4's correction (Code's, declared):** GV4 lists "the ids of record: MANIFEST.json's sha256 the pin" among the pins
  held before G-VER. L:543 names "the manifest's pin" among G-VER's own causes, so the block reads a mismatch as
  G-VER's STOP, with the record, and not as a refusal.

**How §3 was taken.** It was extracted from this session's transcript, a departure declared in the entry that commits
this raw: `sed -n` of the message's record, through `jq` for its content, then `sed -n` of the content's lines 3–28.
Those are the message's own 26 lines, without the delivery wrapper, which names a session by its id.

**What it does not name.** None of the five sections names a path in the home folder or the scratch folder's full
path, once §4's one line is written as above. Scratch files are named S/...

## 1. Code's readings GV1–GV16, as sent

```text
# G-VER of record (n v0.2 §8 step 12): Code's PINs GV1–GV16, for routing

Code, PI date 2026-11-21. Built on the read-only spec survey of HEAD `7d01b02`, which is origin's
(`S/step4b/gver/spec/survey_report_v1.md`, `3a40ac89…8989`, 232 lines, the subagent's hand-back by `jq`, equal to the
message as delivered; its brief `S/step4b/gver/spec/survey_brief_v1.md`, `8e39c8d7…c9a1`, 79 lines). Its 13 open
questions are answered below, the Q-number in brackets, with Code's own checks of the lines cited. ★ = the seat's. If
the route is "build on the PINs", the starred ones go to the seat before the run; if it is "the seat first", before any
code. Every other PIN is Code's. No code is written before these come back routed, and nothing goes to the box.

Short forms as in the survey: n = PROPOSAL-n v0.2; L = LOCK-n.md (v0.1); A-n1 = ADDENDUM-n1; drv = scripts/n_sessions.py;
the raws as the survey names them (ans16b, ans20b, ans21a, ans21b, rt21b, mF3ans).

## The stage

- **GV1 ★ What step 12 is: a stage of its own, with a record [Q1].**
  - **The texts:** n:159 lists "12. G-VER." as its own step, and n:161 lists the entry "`G-VER (n)`". The analyzer
    names "G-VER (n)" among its gate stages (n_analyze.py:129, the `clock:gate-stopped` cause). GT7 says the G-VER at
    G-TIME-n's start is "not of record (n §8 step 12's is)" (drv:216), and the seat accepted GT7 (ans21b:38). The PI's
    [go] is for "G-VER's launch files (step 12)" (rt21b:30).
  - **The reading:** step 12 runs G-VER, `verify.verify` on the committed ids of record, once, on the box of record,
    under LOCK-n v0.1. It writes a record that is committed with its entry, "G-VER (n)".
  - **What it adds to the G-VERs each stage already runs before its load** (the BACKEND extension's and G-TIME-n's,
    PASS at the current package, ids and pin):
    - (a) a record of its own, committed; the stages' G-VER lines exist only in their raws;
    - (b) the decoding tokenizer's files hashed against the pins (GV3); the stages check the weights folder by byte
      counts alone (drv:636–649);
    - (c) MANIFEST.json's sha256 against the pin, printed and recorded; `verify` checks the pin but does not report it;
    - (d) the lock's pins held at the run and recorded (GV4).
  - **Against the m precedent:** for m the seat ruled "G-VER is the verifier, not a step … it has no entry of its own"
    (mF3ans:10). n's own texts give G-VER a step and an entry (n:159, n:161), so the m ruling does not carry. This is
    the seat's call: the step's content (the survey's 4b).
- **GV2 Built in the driver alone [Q9].** A `gver` command in `scripts/n_sessions.py`.
  - `valence_core/n/` does not change: `verify.py`, `ids.py` and `schema.py` stay as they are. So the package and its
    closure stay L §18's (`06b55761…1d39` and its twelve files), and the stage runs under v0.1's package pins, as
    G-TIME-n did (GT3).
  - No schema stage is added. `schema.STAGES` is campaign, time and backend-ext (schema.py:256), and "G-VER's
    reconstructions are other records, not specified here" (schema.py:17–18). A schema stage would move L §18's pin.
  - G-VER of record's record is the driver's own form (GV9), as G-TIME-n's artifact `n-gtime-v1` is.
- **GV3 The site and the decode [Q2].**
  - **Where:** on the box of record, pod `emw1e4embiwe9b` (A-n1:24, "G-VER (n §3) asserts (i) on the box"; box:28).
  - **The decode:** the instruct model folder's tokenizer, from local files only, as every stage's G-VER loads it
    (`_gver_tokenizer`, drv:1068–1073), under the box's environment of record (transformers 5.15.0, tokenizers 0.22.2;
    L §17). The decode form is `_decoder`'s: special tokens kept, no clean-up of spaces (drv:596–601).
  - **The hash check:** before the decode, the tokenizer files `ids.TOKENIZER_FILES` names are hashed in the weights
    folder. Each must be the model manifest's pin (`ids.pinned_tokenizer_sha256s`; L §1, L:196–203). Otherwise the run
    refuses (exit 1) before G-VER. This is stricter than the stages' byte counts, and needs no package change.
  - **No laptop run.** The laptop tokenized the ids under G-DATA's environment (A-n1:20). Its gver-trial on the (i)–(v)
    folder PASSed, never of record (idsv:174–185). The box is where the reads will run, and "the box tokenizes nothing
    for n's inputs" (A-n1:20).
- **GV4 ★ Under LOCK-n v0.1: the pins held before G-VER [Q3].** The stage holds G-TIME-n's preparation checks where
  they bind a run that loads a tokenizer and no weights (drv:4224–4290):
  - the pod (`CHARACTERIZED_POD`);
  - the weights folder: it holds exactly its files at their byte counts, its aggregate sha256 the lock's (L §17). The
    tokenizer is read from it;
  - the driver of record: HEAD's committed bytes for a run of record (drv:1156–1158);
  - the ids of record: MANIFEST.json's sha256 the pin (`ids.MANIFEST_OF_RECORD`, `53a8cd74…99d8`, L:187–189);
  - `LOCK-n.md`: HEAD's committed bytes at the lock's sha256 (`88d9fe7b…e9d5`);
  - the package and its closure, the lock's (L §18). `verify.py` is in the package (guard.py:31–32);
  - the environment's provenance bridged to the characterization's `4ed3f2c70fe8afbf` (R6), and n's backend
    identifier the lock's `8264f719efd347a9` (L §17): no model loads, but the decode runs under these libraries.

  Not held: cuBLAS's setting and numpy's stream known answer, since nothing runs on the GPU and nothing is drawn. The
  record carries every pin it held (GV9). It is not a schema stage identity (GV2). This is for the seat: the identity
  G-VER of record runs under.
- **GV5 The pass rule and the exits [Q5].**
  - **PASS** is `verify`'s own rule, verbatim (verify.py:140–141), with GV3's hashes and GV4's pins held before it.
    Every check `verify` makes is one of G-VER's causes. The decode checks are among them, though L:543's list names
    six; the record says which count fell short.
  - **The exits:**
    - 0 PASS, the record written;
    - 2 STOP, G-VER's STOP: the record written with status STOP, a STOP for the seat (L:543);
    - 1 anything else: a refusal before G-VER (a pin, a hash, the driver, the pod) or a failure, with no record.
  - This keeps 2 for G-VER's STOP alone. GT6 gave a refusal before any read the same code at G-TIME-n.
- **GV6 ★ A STOP at step 12 [Q6].** L:543 binds: "a STOP for the seat, never a pause and never an exclusion; no read
  is launched and the campaign does not start". Code's reading:
  - LOCK-n v1.0 (step 13) is not committed before the seat rules on the STOP and on any re-specification it locks.
  - If D_n (2026-12-15) passes first, the unit is NOT-RUN under n:134, cause `clock:gate-stopped`, stage "G-VER (n)".
  - Nothing re-runs before the ruling.

  The STOP's effect on v1.0 is the seat's (the survey's 4e).
- **GV7 The campaign's own G-VER stays [Q7].** G-VER of record does not replace L:543's "before any read" at the
  campaign. The campaign runs its own G-VER before its load, not of record, as GT7's form has it, and its STOP is the
  campaign's `no-arm:gver-stop` cause (n_analyze.py:126 and :6238).
- **GV8 No smoke [Q8].** The run loads no weights and reads nothing. A subset would STOP on its count, since
  `expect_n` is 160 (verify.py:77–78). The launch script's own checks (the copy, the manifest, the self-test and
  `hashes`) come before it, as at G-TIME-n's launch.

## The record

- **GV9 ★ The record: `data/n/gver/gver.json`, `n-gver-v1`, committed with the entry [Q4].** The driver writes it at
  PASS and at STOP (at a STOP, the STOP's record: schema.py:1197, "G-VER's report"). It holds:
  - `verify`'s report as returned (its nine keys, `first_problems` masked as `verify` masks them);
  - the status;
  - MANIFEST.json's sha256 and the pin, and whether they are equal;
  - the tokenizer files' sha256s;
  - the lock's sha256, the package and its closure, n's backend identifier, the characterization's identifier (R6),
    the pod, the weights' aggregate sha256 and the driver's sha256;
  - the environment's versions;
  - the tokenizer's load and the decode's durations, in ms.

  It holds no token id (`verify`'s report holds none; n:130) and no stamp (GV10). The driver checks the record against
  itself before it writes, and once more on disk.
  - **Committed** with the entry, by path, with `.gitignore` lines admitting `data/n/gver/gver.json` alone (the BUILD
    adds them, as at G-TIME-n's), and the raw: the stage's stdout, the out file.
  - **No stage report:** the schema's report is for stages that read (schema.py:187–193), and G-VER of record reads
    nothing.
  - This is for the seat: the record's form, against the BACKEND extension's unruled reading "the raw is the STOP's
    record; no stage report" (drv:58–59; R:6121–6124).
- **GV10 The printing.** A STAGE line; the pins' lines (WEIGHTS, DRIVER, LOCK-n's sha256, the package, the backend);
  the tokenizer files' sha256s; G-VER's JSON, as the stages print it; the record's path and sha256; and one end line.
  Durations only, no start or finish stamps (GT15's form; WORKFLOW.md:28 and :53).
- **GV11 ★ Does G-VER's record enter LOCK-n v1.0 [Q10]?** Code's reading is yes: v1.0 cites the "G-VER (n)" entry and
  the record's sha256 as the gate the campaign follows, beside G-TIME-n's projections. n:120's list does not name it;
  m's v1.0 named its G-VER (LOCK-m-F3.md:273). v1.0's content is the seat's.

## Conduct

- **GV12 Pod time [Q11].** Seconds to minutes: one tokenizer load and the decode of the 160 sessions' ids, N4's
  sequences and the label candidates. The record's two durations are reported in the entry, beside the cap and outside
  it, G-TIME-n's "named and unmeasured" (ans21b:21).
- **GV13 ★ A box change [Q12].** A new pod re-runs the characterization and the BACKEND extension first, then G-TIME-n
  by default (ans21b:27). Code's reading adds G-VER of record to that list after them, by default, since it is the box
  of record's; the spend is the PI's (box:31). ans21b:27's list names no G-VER, so this is the seat's.
- **GV14 ★ The seat's read [Q13].** The entry, with the record and the raw, goes to the seat. Code's reading is that
  the seat's G-VER read (ans21b:59) comes before step 13's commit, with its read of G-TIME-n's record. The seat's own
  order is its own.
- **GV15 The launch.** A box script in `gtime_v1.sh`'s form:
  - the copy at the BUILD's commit, the manifest, the self-test and `hashes`, then `gver`;
  - the ends 0, 2 and 1 named by the last line;
  - the copy-back of the record and the raw by hash.

  The launch files go to the coordinating session first; nothing goes to the box before its relay. The pod stays up
  (C.8).
- **GV16 The self-test.** The driver's self-test gains `gver`'s cases, model-free: each refusal (the hashes, each pin,
  the driver), PASS, STOP, the record's checks and its writing, and the exits. It runs in a battery window the
  coordinating session grants: the laptop's count, and the box's by arithmetic, as at G-TIME-n's BUILD.
```

## 2. Code's addendum on the third sitting's items, as sent

```text
# The third sitting's items against Code's GV1–GV16 (no PIN changed)

Code, PI date 2026-11-21. An addendum to `S/step4b/gver/spec/gv_readings_v1.md` (`d73c2b8e…976e`, 136 lines), which
stays as sent. It is read against the seat's raw of the third sitting,
`results/raw/2026-11-21_n-gtime-record-read_design-to-code_answers.md` (`c9b1ee42…1f36`, 82 lines, 20,564 bytes,
re-hashed equal, untracked; "the raw" below), and the PI's routing of it as relayed ("PI: route as given"). Nothing here
is a ruling. It says which readings the routed items meet and which they leave open. The route on GV1–GV16 stays with
the PI; no code is written and nothing goes to the box.

## Unread by the seat

- The raw's read list is the entries of `7d01b02` and `b40ce59` (the raw:3), so GV1–GV16 are not in it.
- Its short form reads step 12 as "already routed and runs without waiting for the seat" (the raw:11). N.3 routes "the
  launch files to the coordinating session first, the box's run, its entry" (the raw:71).
- Neither names a BUILD. At `7d01b02` the driver has no command for G-VER of record (GV1, GV2).

## Met by the routed items (consistent with Code's reading; the starred ones stay the seat's)

- **GV1 ★, the entry:** N.3 gives step 12 "the box's run, its entry" (the raw:71). The record's form stays GV9's.
- **GV6 ★:** N.4 places v1.0's draft "after G-VER's PASS" (the raw:72). A STOP therefore leaves no draft before the
  seat rules, which covers GV6's reading and goes further. GV6's D_n clause (NOT-RUN, `clock:gate-stopped`) is
  untouched.
- **GV12:** the raw lists G-VER of record's pod time under "Not measured, named" (the raw:33). GV12 reports the
  record's two durations beside the cap and outside it.
- **GV14 ★, in part:** "G-VER's read" is owed by the seat beside "LOCK-n v1.0's draft read" (the raw:62), and the seat
  "reads it whole before the commit" (the raw:72). The raw does not say that G-VER's read comes before step 13's
  commit.
- **GV15:** the launch files go to the coordinating session first (the raw:71).
- **GV2:** the raw declines a change to the writer before the campaign, since it "would move the package digest away
  from v0.1's §18" (the raw:31). GV2 changes no package file either.

## Left open

- **GV11 ★:** N.4's list is n:120's (the raw:72) and names no G-VER record. Whether v1.0 cites "G-VER (n)" and the
  record's sha256 stays the seat's call.
- **GV9 ★ and GV5, against N.3's "a G-VER-STOP of any cause is a STOP for the seat before any read"** (the raw:71).
  Under GV5, every end but PASS goes to the seat, and no read follows it. The two non-PASS exits differ:
  - exit 2 is `verify`'s STOP, with the record (GV9);
  - exit 1 is a refusal before G-VER (a pin, a tokenizer file's hash, the driver, the pod). It writes no record, and
    the out file is its only trace. A tokenizer file off its pin is also the kind of mismatch the respawn protocol's
    INTEGRITY step makes an incident.

  If the seat counts those refusals as G-VER-STOPs with a record, that is GV9's form, and a small change to the BUILD.
- **GV13 ★:** C.7 keeps the box up through G-VER and the campaign (the raw:79). That makes a box change less likely, but
  the list of what re-runs on a box change stays the seat's.
- **Not addressed by the raw:** GV3, GV4 ★, GV7, GV8, GV10 and GV16.
```

## 3. The coordinating session's routing, with the PI's answer

```text
The PI's answer on G-VER's route is "Build on the PINs": go ahead with G-VER's BUILD on GV1–GV16.

That is verbatim, received 2026-11-22 in this session's chat. It answers my question to the PI, which was: "Build G-VER on n-build's PINs now, or wait for the seat first?" The two answers offered were "Build on the PINs" and "Seat first", and the PI chose the first.

For your spec raw, the same question in its other wordings, all verbatim, each with the same two answers:
- My closing message just after that question: "Should n-build build G-VER on its PINs now, with the seven starred readings going to the seat before the run? Or should it wait for the seat to rule on them first?"
- Asked with your readings: "Build G-VER on n-build's PINs now, with the starred seven to the seat before the run?"
- Asked with the third sitting's routing: "Should n-build build G-VER on its PINs now, with the seven starred readings going to the seat before the run?"

What it routes (my notes, not the PI's words, in G-TIME-n's form):
- **The build.** Build on GV1–GV16 as PINs now, as your readings have them (S/step4b/gver/spec/gv_readings_v1.md, d73c2b8e…976e, 136 lines), with add1's mapping (gv_readings_v1_add1.md, 775ad17d…be51, 46 lines). I re-hashed both equal just now.
  - Step 3's form is G-TIME-n's: drafts in scratch, self-tests in battery windows I grant, one blind review, one values-check, then the BUILD's commit window.
  - Driver only, per your readings. valence_core/n/ has no change from ef105f1 to HEAD (git diff --name-only printed no name).
- **The seat.** The seven starred readings (GV1, GV4, GV6, GV9, GV11, GV13, GV14) go to the seat before the run, not before the build.
  - Same order as G-TIME-n, where the seat block 2ca24e8 went in ahead of the BUILD 91f0d35: a seat block in results/raw, committed by path in a commit window I grant, ahead of the BUILD's commit. Its form is your call.
  - Carry add1's open points in it for the seat: GV11 (N.4's list does not name G-VER's record), and GV9 and GV5 against N.3's "of any cause" (a refusal before G-VER exits 1 with no record).
  - It needs no further word from the PI. The PI's word governs only the nudge to the seat.
  - Unless the PI says otherwise, the launch waits for the seat's ruling on the seven, as G-TIME-n's waited for the second sitting's answers. The third sitting's §0 says G-VER "runs without waiting for the seat", but that raw read only 7d01b02 and b40ce59, not your readings. I'm telling the PI this reading.
- **Unchanged.**
  - Laptop Python runs only in battery windows I grant, one at a time. Ask with the scripts' sha256s; I read them whole and check pgrep before each grant.
  - The launch files come to me first, and nothing goes to the box before my relay with "launch cleared".
  - N.3 stands: a G-VER-STOP of any cause is a STOP for the seat before any read.
  - Nothing is pushed. Per D.8, the next push comes after G-VER's entry, on the PI's word.
- HEAD is cd6b30d; origin is 7d01b02.

pgrep shows 8051 only (python3.12) as of my check just now.
```

## 4. The survey's brief

```text
You compile, read-only, the full specification of one stage of the jspace-lab repository (at
<repo>, HEAD 7d01b02), so that Code can build it: **G-VER of record**, step 12 of
PROPOSAL-n v0.2's §8 order (between step 11, G-TIME-n, whose entry is committed at 7d01b02, and step 13, LOCK-n v1.0).
n's §3 gives it one sentence: "G-VER. Every session's token sequence reconstructed from the record and the rendering of
record before any read; mismatch → STOP". Its stage command is not built: scripts/n_sessions.py has `gver-trial`, "the
BUILD's site-check trial, never of record", and each box stage runs G-VER before its load, "not of record (n §8 step
12's is)" (the driver's GT7); the driver and LOCK-n §24 say the stage commands "are wired at their own steps". You run
no interpreter of any kind (no python, python3, node, perl, awk), write no file anywhere, and return your report as
your final message.

WHAT TO FIND, with a file:line citation for every claim:
1. The specification as the texts state it:
   - PROPOSAL-n-bk-reconciliation-v0_2.md: the G-VER paragraph (about line 119), §8's steps 11–14 and its entries list
     (about lines 159–161), the hours and pod budget (about line 101), LOCK-n v1.0's contents (about line 120), and
     anything else that names G-VER, the verifier, the rendering of record, the ids of record or a STOP before reads;
   - LOCK-n.md (v0.1, committed at deabf3f): every line that names G-VER (among them about lines 92–97, 188, 543, 825
     and 873), §5 and §18 (the rendering, the spans, the manifest's pin, the package and its closure), §17 (the
     backends and the weights), the stage identity, §10's G-VER row, and §24;
   - ADDENDUM-n1 (§1.1–§1.5: the rendering of record, the committed ids, G-VER's assertions, the manifest's pin),
     ADDENDUM-n2 and ADDENDUM-n3, each at the repository root, wherever they name G-VER;
   - every item in the seat's answers raws and the PI's routing raws under results/raw/ dated 2026-11-15 to 2026-11-21
     whose names hold "n-", "box", "sitting" or "routing" that bears on G-VER: the G-VER trial and its STOP, the ids
     rendered on the laptop, "data against data", G-VER's place before reads at every stage, the STOP's handling, what
     G-VER of record is for, when it runs, and who reads its output (among them the seat's answers of 2026-11-16, the
     answers at ans20b:41, and the second sitting of 2026-11-21, §1.7, on G-VER's launch files following G-TIME-n);
   - RESULTS.md's entries that bear on it: the G-VER trial and its resolution, the n package BUILD's site check, the
     ids of record's commits, and the G-VER lines that G-CAL-n's, the BACKEND extension's and G-TIME-n's runs printed.
2. What already exists in the code that G-VER of record could use or must match:
   - valence_core/n/verify.py (its inputs, its checks, its report and its STOP causes) and valence_core/n/ids.py (the
     ids of record, `load`, `MANIFEST_OF_RECORD`);
   - valence_core/n/schema.py: STAGES, the stage identity's fields and their null rules, the report forms, and anything
     that names G-VER or a verification stage;
   - scripts/n_sessions.py: `gver-trial` (`cmd_gver_trial`), `_gver_tokenizer`, and each stage's G-VER call (the
     BACKEND extension, G-CAL-n and G-TIME-n): what it loads, what it prints, its exit codes; the stages' common
     pieces (the refusals, the weights of record, the driver of record, the ids of record, the provenance bridge R6,
     the stage identity, the printing rules); the `hashes` command; and the self-test's G-VER cases;
   - what the box decodes with (the tokenizer files the stages load for G-VER, and where), and any laptop-side
     comparison of decodes (`gcal-decode`) as a template;
   - any verifier stage of record in m or p (valence_core/m/, valence_core/p/, scripts/m_sessions.py,
     scripts/p_sessions.py) that could serve as a template, with the entries that record its runs.
3. What the texts leave open for a build: every point Code would have to decide that no text decides, stated as a
   question with the texts that come nearest. Do not decide them. At least: what G-VER of record runs on (the box,
   the laptop, or both) and with which tokenizer; under which lock (v0.1, since step 12 comes before v1.0) and which
   identity, if any; what it records, where, and what is committed; its pass rule and its exits; what a STOP at step
   12 means for step 13 and the campaign; whether it differs from the G-VER each stage already runs before its load,
   and how; whether it runs a smoke; the driver of record; and whether its record enters LOCK-n v1.0.
4. Anything that would make G-VER of record need the seat or the PI before it runs (a missing input, a conflict
   between texts, a reading that must precede the run).

REPORT FORM: numbered sections 1–4 as above; in each, short items, each with its citation(s). Quote exact words where a
number, a bar, a STOP, a formula or a name is at stake. End with "OPEN QUESTIONS" (from 3 and 4), numbered. Write a
scratch file, if you must name one, as S/...; a repository file by its repository path; never a full local path.

RULES FOR EVERY COMMAND YOU RUN (binding; a breach is reported in a final DEPARTURES section, "none" if none):
- No interpreter of any kind, no write of any file, no network, no model or adapter code run.
- No argv may contain any of these five guard markers, in any case: mlx, jlens, qwen, olmo, ipykernel. Paths count,
  and so do search patterns and the text of the shell command itself (the shell runs each command as one zsh -c
  string, so a marker typed anywhere in a command is in that zsh's argv). File names under results/raw/ and at the
  root count too (p's lock files and drafts hold one in mixed case). A file whose path holds a marker (the model's
  data folder, the OLMo adapter, the model manifest, p's lock files) is read only with your file-reading tool, which
  runs no process; a git pathspec glob in quotes, such as 'data/ol*/...', keeps a marker out of argv for git's own
  commands. A shell variable or glob that expands to a marker in an argument is a breach, and so is a loop that
  passes a marker-named path to a command as an argument. Never glob the repository root or results/raw/ in an
  argument; use git ls-files with a quoted pathspec, or your file-search tool, instead. Write a search pattern for a
  marker bracketed ([o]lmo) if you must search for one.
- Nothing under data/m[f]3 is listed or read, and its name is never written plainly in an argument: write it
  bracketed. No whole-tree git status. Nothing under data/*/ckpt or data/*/reports is read, listed, sized or timed.
- Code's scratch folder is not read at all, but for this brief's own file; and nothing else outside the repository
  is read.
- Every git command over the tree takes item 3's pathspec and the exclusion of Q-F3's folder: `-- .
  ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/m[f]3/**'` (a git command on named non-data files may name them
  instead).
- A glob is expanded and read before it is looped over.
- The list of record v2, items 1-5, verbatim (it governs every read):
1. **Permitted (names, ids, digests):** a bare `git status --porcelain`; a name-only `ls` (no `-l`, `-t`, `-s`, `-la`); `git ls-files`; `git ls-tree --name-only`; `git diff --name-status` and `--name-only`; `git show --name-only` and `--name-status`; `git log --name-only`; `git log` with `--format` of ids, subjects and commit times over any path; `shasum`/`sha256sum` and any program's digest that prints no byte, size or time; `git rev-parse <rev>:<path>` compared in the shell; `git check-attr`; a `find` that prunes every `*/ckpt` and `*/reports` directory (`find … \( -path '*/ckpt' -o -path '*/reports' \) -prune -o … -print`).
2. **Content.** Files under `data/*/ckpt` (the checkpoints and call logs) are read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4: no `cat`, `head`, `tail`, `json.load`, editor or search over them. Files under `data/*/reports` are the read domain (m:271; the stage writes them redacted) and may be read for their content by Code and by the seat — for a stage entry's figures, a declared counter, or a read — with nothing from them printed into a raw beyond what the entry's form reports. **Metadata:** no size or time of either directory or any file in them, in any form (`--stat`, `--numstat`, `ls -l/-t/-s/-la`, `du`, `wc -c`, `stat`, `git ls-tree -l`, `git cat-file -s`, any unpruned `find`, `mdfind` over them).
3. **Content searches** over a checkout or a tree — `git grep`, recursive `grep`, `rg`, `mdfind -onlyin`, and the pickaxe (`git log -S` / `-G`) over any range — exclude the checkpoint and report files with a form tested on this git: `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` (equivalently `':(exclude,glob)data/*/ckpt/**' ':(exclude,glob)data/*/reports/**'`, or `':!data/**'` where nothing under `data/` is wanted), or the prune for `find`-driven greps. The bare `':!data/*/ckpt'` form is not an exclusion on git 2.39.5 and is not used. A pickaxe search without the pathspec can name a commit whose checkpoint matched, which is content; it is a departure.
4. **The pre-push screen** may read every file in the range, `ckpt` and `reports` included, and prints only a per-class verdict, range totals, and one line per distinct match outside those directories; a match inside one is a count by path class and a halt for the seat.
5. **A running stage:** the end-wait is on the PID alone (O3-1); no `stat`, listing, `tail`, `Monitor` or read of its raw, checkpoint or reports until the invocation has ended — in every session, including the coordinating one.
```

## 5. G-VER of record's specification as the texts state it (the survey's report, as returned)

```text
SURVEY REPORT: G-VER of record (PROPOSAL-n v0.2 §8 step 12), read-only, at HEAD 7d01b02

The brief S/step4b/gver/spec/survey_brief_v1.md was verified before use: sha256 8e39c8d7…c9a1, 79 lines.

Short forms. n = PROPOSAL-n-bk-reconciliation-v0_2.md; L = LOCK-n.md (v0.1, deabf3f); A-n1 = ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md; A-n3 = ADDENDUM-n3-capture-convention-reward-gate-and-interval-v0_1.md; R = RESULTS.md at 7d01b02; drv = scripts/n_sessions.py (HEAD's bytes are 91f0d35's, its last change by git log). Raws under results/raw/: ans15 = 2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md; ans16b = 2026-11-16_n-build_design-to-code_answers.md; rt16b = 2026-11-16_second-sitting_pi-routing.md; box = 2026-11-18_box-gpu_design-to-code_answers.md; ans18b = 2026-11-18_n-step4-smoke-pause_design-to-code_answers.md; ans18d = 2026-11-18_n-step4-resume_design-to-code_answers.md; rt18d = 2026-11-18_fourth-sitting_pi-routing.md; ans19b = 2026-11-19_n-gvec-stop-lock-opens_design-to-code_answers.md; ans20b = 2026-11-20_n-lock-v0_1-read_design-to-code_answers.md; rt20b = 2026-11-20_second-sitting_pi-routing.md; ans21a = 2026-11-21_n-lock-committed-close_design-to-code_answers.md; ans21b = 2026-11-21_n-gtime-starred-seven_design-to-code_answers.md; rt21b = 2026-11-21_second-sitting_pi-routing.md; STOP16 = 2026-11-16_n-build_code-to-design_STOP.md; spec21 = 2026-11-21_n-gtime_spec.md; idsv = 2026-11-19_n-ids-v_render.md; bx2 = 2026-11-19_n-step4_bext2-v1_out.txt; gtout = 2026-11-21_n-gtime-v1_out.txt; mF3ans = 2026-11-15_lock-m-f3-v1_design-to-code_answers.md.

## 1. The specification as the texts state it

**PROPOSAL-n v0.2**
- The gate, verbatim: "**G-VER.** Every session's token sequence reconstructed from the record and the rendering of record before any read; mismatch → STOP." (n:119)
- The order, verbatim: "10. Commit LOCK-n v0.1. 11. G-TIME-n; the PI sets the cap. 12. G-VER. 13. Commit LOCK-n v1.0 with D_n. 14. The N-pod campaign within one pod session…" (n:159). Step 6 builds "the verifier" (n:159).
- Entries: the list includes "`G-TIME-n`, `G-VER (n)`, `LOCK-n v1.0`" (n:161).
- LOCK-n v1.0's contents: "Projections, the cap, D_n, hashes of this document, the lock chain, the analyzer, BK's input files." G-VER is not among them (n:120).
- Hours and pod budget: "Pod budget proposed: 8 h for N-pod, the cap set by the PI at LOCK-n v1.0", and "a box change restarts the campaign; gate stages may span boxes". The planning split has no G-VER line (n:101).
- The rendering: BK's records carry `ids_sha` and `seq_len`, "so the rendering is recoverable" (n:34). Sessions are "re-rendered under the rendering G-DATA recovers and asserted token-identical to each record's `seq_len` (and `ids_sha`…)" (n:77). G-DATA (iv) is the recovery (n:107). LOCK v0.1 carries "The rendering and spans" (n:117).
- The STOP before reads:
  - "rendering mismatches" is a counter (n:128); "a rendering mismatch" is a pause-and-adjudicate trigger (n:148).
  - The unit is NOT-RUN if LOCK v1.0 is not committed by its Clock date, "(no box; a gate STOPPED and no re-specification was locked; …)", or if, once locked, it "produces no arm's full read set before a PI stop, a G-VER STOP or its cap" (n:134).
  - D_n is 2026-12-15 (n:152; L:985).

**ADDENDUM-n1 §1** (it "amends n §2.1, §3 G-VER, §8 step 6", A-n1:18)
- §1.1: the tokenizer of record is "G-DATA's environment on the laptop … Python 3.12.9, transformers 5.5.0, tokenizers 0.22.2". "**The box tokenizes nothing for n's inputs**; it loads a tokenizer to decode generated ids, never to produce an input id." (A-n1:20)
- §1.2: the files (i)–(v); (i) is "160 of 160 at the render or STOP, before any commit" (A-n1:22).
- §1.3, verbatim: "G-VER (n §3) asserts (i) on the box against BK's `seq_len`, `ids_sha` and spans — the spans under G-DATA's note G-2 … — before any read; a mismatch is a G-VER-STOP. The BACKEND extension's 24 reads and §2's check use (i)." (A-n1:24)
- §1.5, verbatim: "LOCK-n v0.1's "rendering and spans" means: `MANIFEST.json`'s sha256, the three versions, the tokenizer files' sha256s, and the span convention." (A-n1:28)
- The label check runs "after G-VER" (A-n1:32). §8 records "G-VER asserts data" (A-n1:80) and lists "G-VER's assertion form" in Code's block (A-n1:84).
- ADDENDUM-n2 and ADDENDUM-n3 never name G-VER (git grep count 0). The nearest line is A-n3:54: the intervals are "pinned through the session set's hash and the ids manifest's pin".

**LOCK-n v0.1**
- Status: of record "until LOCK-n v1.0 supersedes it at step 13" (L:3–4).
- The brief's "§5 and §18": §5 is "The keys" (L:392). The rendering, the spans and the manifest's pin are in §1 (L:181–245), the package in §18.
- §1 holds:
  - MANIFEST's sha256 `53a8cd74…99d8`, "G-VER's pin `ids.MANIFEST_OF_RECORD`" (L:187–189);
  - the three versions (L:194–195) and the tokenizer sha256s (L:196–203);
  - the six ids files with their counts and sha256s (L:205–214);
  - the rendering: "the OLMo-2 chat template, no system turn, with the generation prompt; `ids_sha` is the first 16 hex of the sha256 of the JSON id list. The box tokenizes nothing for n's inputs"; `rendering_id` is the manifest's sha256 (L:216–220);
  - the spans tile [0, n_pre) and "the last 39 tokens lie in no turn" (L:221–229); the label convention is "space" (L:230–236).
- §10's G-VER row, verbatim:
  - where: "before any read";
  - bar: "per session: the committed ids' `seq_len` and `ids_sha` BK's; the spans tiling [0, n_pre) under G-2; N4's two sequences; every kept label candidate; `MANIFEST.json`'s sha256 the pin; 160 of 160";
  - on fire: "G-VER-STOP of any of its causes (…): a STOP for the seat, never a pause and never an exclusion; no read is launched and the campaign does not start (ruled at the lock's read, ans20b:41)" (L:543).
- Beside it, the rendering trigger at "campaign, G-TIME-n" is a "pause; the read is not launched" (L:549).
- Other G-VER lines:
  - "G-VER asserts `ids_sha` on all 160 (verify.py:7; §10)" (L:823–826);
  - the BUILD flag "how a G-VER-STOP that is not a token mismatch counts" (L:870–874), ruled by ans20b §4 according to the dated note ans21a:15(b);
  - draft 10 put the seat's sentence into §10's G-VER row (L:90–99).
- §16: G-TIME-n runs under v0.1 and "v1.0 carries "Projections, the cap"" (L:740–744).
- §17, the backends and the weights (L:746–774):
  - n runs on H100 SXM pod `emw1e4embiwe9b`, identifier `4ed3f2c70fe8afbf`; n's own identifier is `8264f719efd347a9`, bridged by R6;
  - the environment is python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0, tokenizers 0.22.2;
  - the weights' `files_aggregate_sha256` is `36f05404…0fdb`.
- §18: the package `06b55761…1d39` and its twelve-file closure (L:781–813).
- §24: "…then G-TIME-n and the PI's cap; G-VER; LOCK-n v1.0 with D_n; … The stage commands for G-TIME-n, G-VER and the campaign are wired at their own steps" (L:995–998).
- The stage identity's fields are cited from schema.py at L:218–220, :251, :234 and :741. v0.1's lock lines are "lock: LOCK-n v0.1" and "direction of record: Route B" (L:842–845).

**The seat's and PI's raws (2026-11-15 to 2026-11-21)**
- Order: "…G-TIME-n and the PI's cap → G-VER → LOCK-n v1.0 with D_n → the campaign…" (ans15:62).
- The G-VER trial's STOP:
  - Code's block: "Step 4, the G-VER trial, returned STOP"; "`ids_ok` was 0 of 160"; transformers 5.15.0 on the box against 5.5.0 (STOP16:23–27, :44–56).
  - The seat's ruling: "STOP Q1: (b)". The ids are rendered once on the laptop; "G-VER asserts them on the box against `seq_len`, `ids_sha` and the spans … the box tokenizes nothing" (ans16b:7). "asserted on the box as data against data" (ans16b:14). In §1.4, "a mismatch before any read is a G-VER-STOP, as n §3 has it" (ans16b:25). Precedence: "a rendering mismatch during a stage is a pause and G-VER's a G-VER-STOP — accepted" (ans16b:50).
  - Ledger (79): "the gate that asserts it asserts data" (ans16b:56). The routing reads "G-VER asserting data … [go]" (ans16b:75).
  - The PI's routing: item 5, "Decision (n-1): the rendering of record as committed ids … [adopt]"; item 7; "PI: Route as given" (rt16b:25, :27, :36).
- G-VER before reads:
  - the extension runs "in the same session after G-VER's assertion of the committed ids" (box:27); the box answers add "one box for n" (box:28);
  - the smoke's purpose included "G-VER PASS" (ans18b:36);
  - "the ids of record under "space" for every session before any arm reads" (ans18d:72; rt18d:15);
  - "the ids of record stand, nothing is re-rendered" (ans19b:17).
- The STOP's handling, ruled (ans20b:41, verbatim): "G-VER runs before any read (n:119); a STOP of any of its causes — `seq_len`, `ids_sha`, the spans' tiling, N4's two sequences, a label candidate, the manifest's pin — is a STOP for the seat, never a pause and never an exclusion; no read is launched and the campaign does not start." The PI routed it (rt20b:21).
- When it runs:
  - "**G-VER** (step 12). **LOCK-n v1.0** (step 13) … by D_n 2026-12-15" (ans20b:58). "then G-VER [go, after step 10]" (ans20b:71), and the PI the same (rt20b:14).
  - §1.7, verbatim: "G-VER's launch files (step 12) follow a COMPLETE run at once, since nothing in G-VER waits on the cap" (ans21b:27; also ans21b:10, :72).
  - The PI, item 3: "then G-VER's launch files (step 12) without waiting for the seat. [go]" (rt21b:27–30), and "PI: route as given" (rt21b:51).
- G-TIME-n's own G-VER: "GT7's G-VER before the load, not of record, accepted; a G-VER-STOP at G-TIME-n is a STOP for the seat before any read, never a pause (L:543)" (ans21b:38). The smoke's ends include "a G-VER-STOP (exit 2) at the smoke" (ans21b:39).
- Pod time: "G-VER of record and the campaign's resumes, named and unmeasured" (ans21b:21).
- The box: its next use is "G-TIME-n's smoke and run, then G-VER, then the campaign" (ans21b:57); it stays "up through G-TIME-n, G-VER and the campaign [stays up]" (ans21b:81; rt21b:45).
- Who reads the output: "Owed by the seat … G-VER's read" (ans21b:59). Code → design is "repo state only" (WORKFLOW.md:17).
- The lock's sha256 is "the figure every stage identity from here carries as `lock_sha256`" (ans20b:57; ans21a:7).

**RESULTS.md**
- The trial and the hold: "Step 4, the G-VER trial (never of record), returned STOP" (R:8993–9022). The resolution: "the box receives ids" (R:9064–9075).
- The BUILD's checks and site check:
  - the checks are listed at R:7193–7200, and the stage commands, G-VER among them, are "Not built here" (R:7222–7223);
  - the second site check PASSed: "The G-VER trial on the committed ids PASSed. It is the BUILD's trial, never of record. It covered 160/160 sessions' ids, spans and N4 sequences, 4 of 4 label candidates, and the manifest." (R:7275–7285);
  - the open flag on counting a non-token G-VER-STOP (R:7355–7356).
- The ids of record's commits:
  - (i)–(iii) at `d76f34f` (R:8684–8716; R:7273–7274);
  - (iv) at `b523f6a`, with "HEAD between them would have G-VER STOP on the pin" (R:6637–6668; ids.py:78–79);
  - (v) at `516b60f`, with the pin moved to `53a8cd74…99d8` (R:3554–3571). By git log, 516b60f changed MANIFEST.json, gcal_prompts.jsonl and ids.py, and nothing under data/n/ids has changed since.
- The G-VER lines the stages printed:
  - the BACKEND extension, PASS, 160 of 160 throughout and labels 4 of 4 (bx2:60–61; R:4860, :5185, :6450), under the (i)–(iv) pin (R:6088);
  - G-TIME-n, PASS with the same JSON at its smoke (gtout:121–122) and its run of record (gtout:185–186; R:147), at the current pin and package;
  - G-CAL-n printed none. Its driver path has no G-VER step (drv:157–176), `verify.verify` is called only at drv:438 and drv:1073, and the gcal-v1 raws hold no "G-VER" (count 0).
  - A laptop gver-trial on the (i)–(v) folder PASSed (R:3569–3571; idsv:174–185).
- Next: "G-VER's launch files (step 12), at once (§1.7)" (R:311–313).

## 2. What already exists in code

**valence_core/n/verify.py**
- The docstring says "DATA AGAINST DATA … It tokenizes nothing; a tokenizer is loaded only to decode" (verify.py:1–26).
- Inputs (verify.py:70–75):
  - BK's 160 sessions. `load_sessions` refuses any set but BK's 14 skeleton files at `be50011a…` (sessions.py:105–112).
  - `ids.load`'s dict, with each file at MANIFEST's sha256 and count (ids.py:301–334).
  - A decode callable and N4's schedule.
  - `tail` 39 (verify.py:38).
  - `pins`, by default the model manifest's three tokenizer sha256s (ids.py:117–119).
  - `expect_n` 160, and `manifest_pin` = `MANIFEST_OF_RECORD` (ids.py:86).
- Checks:
  - the session count (verify.py:77–78);
  - `manifest_ok`: the manifest's environment is `ENV_OF_RECORD`, its tokenizer files are the pins, its session set the set of record (verify.py:80–85);
  - `pin_ok`: MANIFEST.json's sha256 is the pin (verify.py:86–89);
  - a decoder is required (verify.py:90–91);
  - per session: the length is `seq_len`, the `ids_sha` is BK's, and the ids decode to `render_text` (verify.py:94–105);
  - the spans: the tiling, the 39-token tail, and each span's decode under G-2 (verify.py:48–63, :106–110);
  - N4's two sequences: BK's prefix, each record's `ids_sha` and zone, and their decode (verify.py:111–124);
  - every kept label candidate: its cues and its decodes (verify.py:125–138).
- PASS rule, verbatim: "manifest_ok and pin_ok and decode is not None and ok_ids == ok_spans == ok_n4 == n == expect_n and n_kept > 0 and ok_labels == n_kept and not problems" (verify.py:140–141).
- The report holds sessions, ids_ok, spans_ok, n4_ok, labels_kept, labels_ok, manifest_ok, status (PASS or STOP) and at most five `first_problems` (verify.py:142–144), masked to 200 characters (verify.py:66–67). `pin_ok` is not printed (idsv:177–179).
- Self-test: 18 checks on synthetic sessions (verify.py:181–273), with the note "G-VER on BK's committed ids runs on the box" (verify.py:150–151).
- Not checked: the (iv) and (v) files beyond `load`'s sha256 and count (ids.py:317–327); the decoding tokenizer's own files.

**valence_core/n/ids.py**
- `ENV_OF_RECORD` and `TOKENIZER_FILES` (ids.py:68–69).
- The three manifest pins, `MANIFEST_I_III`, `MANIFEST_I_IV` and `MANIFEST_OF_RECORD` (ids.py:78–86). The four candidates (ids.py:96–97).
- `check_environment` and `check_tokenizer_dir` (ids.py:111–114, :122–133) are used by the renders and gcal-decode, not by any G-VER call.
- `ids_of` raises `RenderingMismatch` (ids.py:605–613); `label_ids` (ids.py:616–626).

**valence_core/n/schema.py**
- `STAGES = ("campaign", "time", "backend-ext")` (schema.py:256). "G-VER's reconstructions are other records, not specified here" (schema.py:17–18).
- Identity fields (schema.py:448–481): `lock_sha256` is "null only at backend-ext (before LOCK-n v0.1)" (:453); `rendering_id` (:463–465).
- The report:
  - "a rendering mismatch during a stage is a pause; G-VER's, before any read, is a G-VER-STOP … A G-VER-STOP comes before any read: its report holds no record and no pause" (schema.py:187–193);
  - the end states include G-VER-STOP (schema.py:207–215, :1131);
  - `record_sha256` is "the STOP's record (G-VER's report; the PI's stop raw)" (schema.py:1197);
  - `rendering_mismatches`: "at a G-VER-STOP G-VER's mismatches, at least one" (schema.py:1225–1227, checked at :1533–1537);
  - "G-VER re-checks" N4's prefix (schema.py:115–119).
- runner.py's RENDERING monitor is "G-VER's check, repeated per read" (runner.py:63–65).
- `verify` is a production module (guard.py:31–32), so it sits inside L §18's package digest.

**scripts/n_sessions.py (drv)**
- gver-trial: "the BUILD's site-check trial, never of record" (drv:16–20).
  - It refuses a `--model-dir` that is not a folder, and loads `AutoTokenizer.from_pretrained(..., local_files_only=True)` "to decode only".
  - It prints "G-VER trial (the BUILD's site check; never of record):" with the JSON; exit 0 iff PASS, else 1 (drv:427–441).
  - It checks no pod, cuBLAS setting, weights, driver, environment or tokenizer files.
- `_decoder` keeps special tokens and does no clean-up: "gver-trial's form, which PASSed at the BUILD's second site check, 2026-11-16, on the A100 pod" (drv:596–601).
- `_gver_tokenizer(ss, loaded, path)` loads the tokenizer from the weights folder (drv:1068–1073).
- The BACKEND extension:
  - before G-VER: the refusals, the pod `emw1e4embiwe9b`, cuBLAS, the stream's known answer, the rulings, then the STAGE, WEIGHTS and DRIVER lines (drv:1117–1160);
  - the ids and the manifest pin (drv:1161–1164), R6 (drv:1166–1169), the identity (drv:1172–1175), the prior state and BK's tables (drv:1177–1191);
  - G-VER prints "G-VER (the BACKEND extension's start; ADDENDUM-n1 §1.3):"; on a STOP it prints "G-VER STOP: no weights load, nothing is read" and returns 1 (drv:1192–1197);
  - Code's reading "at backend-ext the raw is the STOP's record; no stage report" (drv:58–59) is flagged and unruled in the raws read (R:6121–6124).
- G-TIME-n:
  - GT7: "G-VER before the load, not of record (n §8 step 12's is)" (drv:216);
  - its preparation checks the LOCK_ pins (drv:3764–3802): weights, backend identifier, package and closure, read plan (drv:4245–4290);
  - G-VER prints "G-VER (G-TIME-n's start, not of record; GT7):"; on a STOP, "…no report (GT7; L:543): a STOP for the seat" (drv:4292–4297);
  - exits: 0 COMPLETE, 3 PAUSE, 2 a G-VER STOP or a refusal, 1 otherwise (drv:4326–4348);
  - `GTIME_NOT_MEASURED` includes "G-VER of record (n v0.2 §8 step 12)" (drv:3755–3757).
- Common pieces: `weights_of_record` and `check_weights_folder` (byte counts; "the full re-hash is respawn step (i)", drv:636–664), `driver_bytes` (drv:667–673), `hashes` (drv:284–290), and GT15's printing (drv:230–231). The printing carries no margins (n:130).
- The self-test's G-VER cases: drv:331–332, :1702–1705, :1725–1727, :1875–1877, :1990–1994, :4824–4829, and the trapped loaders including `_gver_tokenizer` (drv:4959–4973).
- "Stages G-VER, the campaign and G-READ-n are wired at their own steps." (drv:239)
- .gitignore admits no G-VER path under data/n (.gitignore:262–343). Its ids line says "G-VER asserts them on the box" (.gitignore:270).

**What the box decodes with**
- The instruct entry's folder (data/olmo/manifest.json:170–178, `path` at :176; WEIGHTS lines at bx2:57 and gtout:162).
- The three tokenizer files at their pins (data/olmo/manifest.json:251–262), plus `vocab.json` and `merges.txt` (:263–265, :187–189).
- Each is checked at the stage by byte count only (drv:636–649), under transformers 5.15.0 (L:767–768).
- The laptop's trial decoded from a scratch folder of the three files (idsv:46–51).
- gcal-decode is the laptop template: `check_environment`, `check_tokenizer_dir`, `_decoder`, both files' sha256s, the counts and every difference printed (drv:3019–3081).

**m and p**
- m's G-VER (PROPOSAL-m-gating-campaign-v1_11.md:284) runs per record inside every stage (valence_core/m/verify.py:1–31; valence_core/m/stages.py:51–56; LOCK-m-F0.md:2061, "at every stage"). p uses m's verifier on every record (LOCK-p-OLMo-dpo.md:379; valence_core/p/stage.py:10).
- No standalone verifier stage of record exists in m or p.
- The precedent for the chain's "G-VER, G-PWR, LOCK-m-F3 v1.0" (PROPOSAL-m-gating-campaign-v1_11.md:298):
  - Code's R9 (results/raw/2026-11-14_mf3-gpwr_code-to-design.md:75–77, :86);
  - the seat: "G-VER is the verifier, not a step … it has no entry of its own in m:363's list. … No separate step is owed before v1.0" (mF3ans:1, :10; v1.0's wording at mF3ans:30; LOCK-m-F3.md:236–238, :273; R:10664).

## 3. What the texts leave open (stated as questions; nothing is decided here)

- **3a. What step 12 is.** A separate run is implied by n:159, the entry "`G-VER (n)`" (n:161), the analyzer's `GATE_STAGES` "G-VER (n)" (n_analyze.py:129), GT7 (drv:216; spec21:103, "G-VER of record is step 12's own stage", accepted at ans21b:38) and "launch files" (ans21b:27; rt21b:30). No text says what it adds to the PASSes already on record at the current package, ids and pin (gtout:122, :186). The m precedent (mF3ans:10) is "not a step".
- **3b. Site and tokenizer.** "on the box" (A-n1:24; ans16b:7; box:28; rt21b:45), with the box's 5.15.0 decode from the model folder (drv:1072)? The laptop under G-DATA's environment (A-n1:20; gcal-decode's form)? Both? Should the decoding files be hashed at run time? verify's decode-equality checks (verify.py:100–101, :61, :120, :134) are stricter than L:543's six named causes.
- **3c. Lock and identity.** Is it under v0.1 (L:3–4)? Does it carry a stage identity, given that STAGES has no G-VER stage (schema.py:256)? Which of G-TIME-n's pre-load checks apply to a run that loads no weights (drv:4224–4291)?
- **3d. What it records, and where.** Is the stdout raw the record (drv:58–59, unruled), or an artifact with a schema (schema.py:17–18 specifies none)? What is committed, and before the pod stops (CLAUDE.md:354–359)? A new data path needs .gitignore lines (.gitignore:262–343). Does the record print the pin, which verify does not (idsv:177–179)?
- **3e. Pass rule and exits.** The pass rule is verify.py:140–141. The exits are undeclared: gver-trial 0/1 (drv:441), the extension 1 (drv:1197), G-TIME-n 2 (drv:4348).
- **3f. A STOP at step 12.** L:543 holds. n:134 gives the Clock NOT-RUN cause `clock:gate-stopped` (n_analyze.py:121–122, :129). Can v1.0 be committed after a step-12 STOP, and on what re-specification?
- **3g. Relation to the stages' G-VER calls and the campaign's.** The campaign's G-VER-STOP cause is `no-arm:gver-stop` (n_analyze.py:126). Does the campaign repeat G-VER?
- **3h. A smoke.** None is specified. A subset run would STOP on its count, since `expect_n` is 160 (verify.py:77–78).
- **3i. The driver of record.** A new command means a driver BUILD. A run of record runs only HEAD's committed bytes (drv:1156–1158). L pins no driver digest; it pins the package (L:781). A schema stage would move the package digest of L §18.
- **3j. Whether G-VER's record enters LOCK-n v1.0.** n:120 omits it; m's v1.0 named it (LOCK-m-F3.md:273).
- **3k. Pod time.** Unmeasured and beside the cap (ans21b:21); whether it counts against the 8 h budget is unstated (n:101).
- **3l. A box change.** The re-runs on a new pod name no G-VER (ans21b:27); gate stages may span boxes (n:101).

## 4. What needs the seat or the PI before it runs

- **4a. No command exists** (drv:239; L:997–998). G-VEC, G-CAL-n and G-TIME-n each went through a spec raw and the seat's ruling before their BUILD (ans21a:21). The PI's "[go]" names G-VER's launch files, not a BUILD (rt21b:30). The route is the coordinating session's and the PI's call.
- **4b. The step's content**, against the m precedent (mF3ans:10) and n:161, is the seat's call.
- **4c. A site or library other than "on the box"** (A-n1:24; box:28) would depart from the texts.
- **4d. The record's form.**
  - The extension's flagged, unruled reading (R:6124).
  - The schema's G-VER-STOP report form (schema.py:1197, :1533–1537) against the stages' "no report" (drv:4296; accepted only for G-TIME-n, ans21b:38).
  - ans20b:41 ruled the STOP's handling, not the `rendering_mismatches` count (R:7355–7356).
  - Any schema stage moves L §18's pin.
- **4e. A step-12 STOP's effect on v1.0** is the seat's (n:134; L:543).
- **4f. The seat's G-VER read** (ans21b:59) is owed. Whether it precedes step 13's commit is not stated (ans21b:27).
- **Missing inputs:** none found. The ids are at the pin and unchanged since 516b60f, the box is up (rt21b:45), and nothing waits on the cap (ans21b:27). The spend is the PI's (ans21b:57).

## OPEN QUESTIONS

1. Is step 12 a run distinct from the stages' G-VER calls, and what does it add? (3a, 4b)
2. Box, laptop or both; which tokenizer and library; are the decoding files hashed at run time? (3b, 4c)
3. Lock v0.1 and which identity, if any; which pre-load checks apply? (3c)
4. The record's form, path and commit, and its .gitignore lines? (3d, 4d)
5. The exit codes? (3e)
6. A STOP at step 12: does v1.0 wait for a re-specification? (3f, 4e)
7. Does the campaign repeat G-VER? (3g)
8. A smoke, and of what? (3h)
9. A BUILD via a spec raw and the seat first, or on rt21b item 3 alone? A driver-only change or a schema one? (3i, 4a)
10. Does G-VER's record enter LOCK-n v1.0? (3j)
11. Pod time against the 8 h budget? (3k)
12. A re-run on a box change? (3l)
13. The seat's G-VER read before step 13? (4f)

## DEPARTURES

1. Before reading the brief, at the caller's instruction, I ran `shasum -a 256` once on the brief's own file. On this machine shasum is a Perl script: list item 1 permits it by name, but the brief bars perl. I also ran `wc -l` on the same file.
2. I ran `/usr/bin/awk 'NR<0'` once, as a sink discarding a `git grep` over RESULTS.md. It printed nothing and wrote nothing. This breaches the bar on awk.
3. I ran `git log` with `%ad` (author dates, not commit times) twice: over valence_core/n/verify.py and ids.py (four ids printed), and over valence_core/n/ for ef105f1..HEAD (nothing printed).
4. Pathspec forms:
   - `git grep` and `git log` named valence_core/n/ (a code folder) in place of item 3's pathspec.
   - One `git grep` named data/n/gtime/gtime.json directly. That is a data file outside ckpt and reports; its first 240 characters printed, holding no margin.
5. The string "mf3" stood in one argv, inside a results/raw file name. It was not Q-F3's data folder.
6. One tool output printed a code constant holding token ids (valence_core/n/sessions.py:52). None of it is in this report.
7. One whole-tree `git grep`, with item 3's pathspec, overflowed. The harness saved its output to a file outside the repository, and I never opened it. Three `git grep` calls failed on a repetition-count error and printed nothing.
8. No marker stood in any argv. Nothing under ckpt, reports or data/m[f]3 was read, listed or sized. No file was written.
```
