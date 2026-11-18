# n step 4 — the BACKEND extension resumed under the seat's ruling on `p01`: the stage COMPLETE, and A-n1 §2's comparison names no candidate at 40 of 40 — the label convention of record for the seat (code → design)

*The n-build session (Code), PI date 2026-11-18. For the PI to route.*

*What ran, on n's box (pod `emw1e4embiwe9b`, the H100 SXM of the BACKEND entry `d5d08fa`), by the pod session, on the
seat's answers of 2026-11-18, third sitting, §1.4, and the PI's "Route as given". No lock is in force.*
- *The resume. Driver v2f, committed at `1272702` (`e29839c8…1152`; the driver the committed texts at `7a54eb9` and
  `f3e7190` call v2e), run by the box script v4 (`4fec8670…dd78`). It ran in a fresh sparse copy at `1272702` holding
  byte copies of the run copy's stage report, cell file and 31 capture arrays, each checked by sha256 against the run
  copy's (0 mismatches). The command was `backend-ext --resume --ruling p01=<the ruling raw>`, with the ruling raw
  committed at `3b2b855` (`e2b1c77a…2a8a`). The run copy at `ad856f0` was only read.*
- *The first attempt. The box script v2 (`f166e7ce…19f2`) failed at its copy-in: the box's volume refused `cp -p`.
  Nothing of the stage ran (§3).*

*Sources read, by sha256 or commit:*
- *the resume's whole output `bext_resume_v4_out.txt` (`8d286ce4…2a39`, 74 lines) and the pod session's record of it
  (`c86e812a…be14`), with the run's exit file and its three work files;*
- *the first attempt's whole output `bext_resume_v2_out.txt` (`0c926ca3…bf79`, 9 lines), its exit file, and the pod
  session's record of it (`2f606ca7…1ce9`);*
- *the three box scripts: v2 (`f166e7ce…19f2`), v3 (`fa91a17d…da36`, relayed after the hold and never run) and v4
  (`4fec8670…dd78`);*
- *the resumed report `data/n/reports/backend-ext.json` (`dd217d78…ce79`), copied back by hash and read after it
  arrived: its `cells` record and its pauses only;*
- *driver v2f (`scripts/n_sessions.py` at `1272702`);*
- *the seat's answers of 2026-11-18, third sitting (`d51279ec…0bf4`), §1.2–§1.4 and §3;*
- *the seat's corpus answers of 2026-11-18 (`results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md`,
  `5843a9bd…7165`), §5.5;*
- *ADDENDUM-n2 v0.1 (`41f76c49…bb3f`, committed at `7a54eb9`), §0.2 and §1–§5;*
- *ADDENDUM-n1 v0.1 (`e979f8f2…5e03`), §2, the rule;*
- *`RESULTS.md`'s entries of `1272702` and `7a54eb9`, and the pod session's close line at `f3e7190`;*
- *the block of `6df2131` (`results/raw/2026-11-18_n-step4-run-pause_code-to-design_STOP.md`), its read lines.*

*Not opened: the cell `data/n/ckpt/backend-ext/N1-V__none__0.json` (`80770a19…78ea`, unchanged by the resume and
hashed only); its 31 capture arrays, which stay on the box's volume; anything under `data/mf3`.*

## 0. The short form

- **The stage is COMPLETE.** It resumed skip-only under the ruling: no read was re-launched, `p01` is adjudicated under
  the ruling's sha256, and the cell and its arrays are unchanged.
- **The resume printed §1.4's list:** the discordance distribution, the in-band count (6 of 6), and A-n1 §2's
  comparison with its four counts and four medians.
- **The comparison names no candidate at 40 of 40.** The counts are bare 0, space 16, bare+eot 0 and space+eot 16. By
  A-n1 §2's own words — "none, or more than one, goes to the seat with the four counts" — this is the seat's.
  backend-ext-2 does not run now, and nothing more runs on the box.
- **ADDENDUM-n2's figures of record wait for the convention of record.** Under "bare", the convention the 24 reads ran
  under, §4.1's figures of record would be:
  - k = 10 of n = 24 at TAU;
  - the largest margin discordance, 0.0625 nats;
  - the median rel, 0.0132.
- **Questions:** Q1, the convention of record (§5); Q2, backend-ext-2 under it (§6); Q3, the comparison's tolerance
  (§7).
- **Code adjudicates nothing.**

## 1. The reads the seat needs (m:271's form)

- **This raw**, in full.
- **The resume's output and the pod session's record of it**, committed as
  `results/raw/2026-11-18_n-step4_bext-resume4_{out,run}.txt`, in full. The output carries no margin and no pick.
- **The first attempt's output and the pod session's record of it**, committed as
  `results/raw/2026-11-18_n-step4_bext-resume2_{out,run}.txt`, in full.
- **The resumed report**, committed as `data/n/reports/backend-ext.json`: the read domain. It holds the counters, `p01`
  adjudicated, and the binomial's state.
- **Not for reading:** the cell under `data/n/ckpt/backend-ext/` (item 2), committed at `6df2131` and unchanged.

The resume's output, lines 61–65, verbatim:

```text
end COMPLETE: 24/24 reads; report backend-ext.json
discordance over 24 reads (absdiff and label in nats, rel = absdiff / the read's scale; fidelity values, no margin; R3's bound is label.max): {"absdiff": {"max": 0.06250021525822458, "median": 0.031249837805753522, "min": 6.65146862033339e-08, "p90": 0.053124039978558434, "q1": 3.6012615489688926e-07, "q3": 0.03125030038608245}, "exceed_tau": 10, "exceed_tau4": 15, "finite": 24, "label": {"max": 0.04924420372226734, "median": 0.007755042120141997}, "reads": 24, "rel": {"max": 0.08606975666735853, "median": 0.013228265542717183, "min": 2.2010351289568807e-08, "q1": 3.339193281467121e-07, "q3": 0.029509094837152826}}
in-band: 6 of 6 floor reads' fresh values, both labels, equal the comparison's vanilla score
label convention (ADDENDUM-n1 §2; per candidate, the count of 40 and the median |value - BK's| over its 80 values, nats): bare 0/40, median 9.73594; space 16/40, median 0.0382264; bare+eot 0/40, median 9.73506; space+eot 16/40, median 0.0388117
0 candidates at 40 of 40: to the seat with the four counts and the four medians (ADDENDUM-n1 §2; the seat's answers of 2026-11-18, §5.5)
```

The values behind the comparison's counts and medians are written to no file. A-n1 §2 has the stage print "per
candidate its match count of 40 and nothing else", and the seat's corpus answers of 2026-11-18, §5.5, added the
median beside it. The printed line's "the seat's answers of 2026-11-18, §5.5" is the driver's citation of those
answers.

## 2. The resume

Every step held, in the box script's order:
- **0, the copies and the ruling.** The run copy is at `ad856f0`, with its report and cell file at the bytes committed
  at `6df2131`. The fresh copy is at `1272702`, clean, with neither stage's root or report present. The ruling sits
  beside the script at its committed sha256 and byte count.
- **1, the copy-in.** "copied and compared: 33 files (the report, the cell file, 31 capture arrays), each equal to the
  run copy's by sha256 (mismatches: 0)". The names came from the committed record, with no listing.
- **2–4.** The manifest is 23 of 23. The self-test gives "389/389 n selftest checks pass", the count the committed
  self-test raw of `1272702` predicted for the box (378 and its 11 HF checks); two library warnings precede it. The
  hashes are equal to the laptop's.
- **5, the resume.**
  - The STAGE line, then the weights, then "DRIVER … HEAD's committed bytes".
  - G-VER PASS; the load (707/707); the backend line, with n's identifier `8264f719efd347a9` (window 4,096), R6's
    bridge to the characterization's `4ed3f2c70fe8afbf`, and the load at 12,150 ms.
  - No read line, then "end COMPLETE: 24/24 reads".
  - The prints of §1.
  - The report: "end_state COMPLETE; 1 pause(s): p01 fidelity-binomial launch_index None adjudicated True
    ruling_sha256 e2b1c77a3026dd40be659168397826cd60397f514b243cb6279234058d2e2a8a". Its identity lines equal the
    hashes step's, and its sha256 after the resume is `dd217d78…ce79`.
  - The cell file and its 31 arrays are unchanged, and the run copy's two files are still the committed bytes.
- **The summary line:** "bext resume v4 COMPLETE (pass)", exit 0.
- **Independent checks of the copy-back:** `hashes.txt` and `resume-identity.txt` are the same bytes (`93783db0…7b36`,
  the laptop's hashes file), and `resume.txt` is the output's lines 54–65.

## 3. The first attempt, which failed at its copy-in

The box script v2 ran first. It had already gone to the pod session when the coordinating session sent a hold on it,
and then v3, which never ran (the coordinating session's words; the pod session's record). Step 0 held. Its first
`cp -p`, the report into its fresh copy, was refused by the box's network volume: "cp: preserving permissions for
‘…/data/n/reports/backend-ext.json’: Operation not permitted", then "COPY-IN FAIL: data/n/reports/backend-ext.json",
exit 1.
- Nothing after it ran: no manifest, no self-test, no hashes, no resume, no model load.
- A probe on the volume, a dummy file in a new folder, confirmed it: a plain `cp` works there and `cp -p` fails. The
  probe's `cp -p` still created its destination, so the failed copy may hold the report's bytes.
- The fix was v4's plain `cp`. The check after the copy is v3's sha256 mismatch count, unchanged; v2 compared each copy
  by `cmp -s`, and v3, relayed after the hold, kept `cp -p` and never ran. The copy check's form thus moved from the
  `cmp` that `1272702`'s entry and `f3e7190`'s close line name to the digest form, both within the coordinating
  session's form ("per-file cmp or shasum on names taken from a committed record").
- The failed run's copy and work folder stay on the box, unread, as its record; their cleanup is the PI's call.
- It is a launch-script defect of Code's, declared in the entry. It is no gate of the stage.

## 4. Items Code declares, without adjudicating

1. **The bare forms sit about 9.7 nats from BK's values at the median** (9.73594 and 9.73506). Code reads that as
   fitting the seat's §1.3 on the scale: "under the "bare" convention the labels are probable, so the scale is near 1
   nat; BK's recorded label log-probabilities are near −10".
2. **The space forms sit 0.038 and 0.039 nats from BK's at the median** (0.0382264 and 0.0388117). That is below R3's
   bound as run (0.0492). Yet under each space form, 24 of the 40 sessions fall outside the tolerance on at least one
   label. The two space forms are nearly identical: 16 of 40 each, medians within 0.0006 nats.
3. **The distribution's absdiff** has median 0.0312498, q3 0.0312503 and max 0.0625002 nats. These are 2^-5, 2^-5 and
   2^-4 to within 3.1e-7 (q3's 3.004e-7 the largest). Code reads that as consistent with the seat's §1.2 reading,
   rounding in bf16 on either path; it is the seat's to weigh.
4. **The distribution is the run of record's.** The resume is skip-only, so it is computed from the same 24 records:
   rel's max 0.0860698 is read 1's 0.086070, and the exceedances of TAU are 10, as at `6df2131`, and of TAU/4, 15. The
   resume's own forwards agree with those records: the in-band count is 6 of 6.
5. **The margin's largest discordance is now printed in nats: 0.0625.** The seat's texts give it as "at most about 0.09"
   nats (the answers' §1.3; the ruling raw's item 3; ADDENDUM-n2 §0.2 and §5). ADDENDUM-n2 §2.1 calls 0.25 "about three
   times this box's under "bare"". On the printed figure it is four times.
6. **Under "bare", ADDENDUM-n2's formulas give:**
   - p0 = (k + 1)/(n + 2) = 11/26 (§1.1);
   - C = max(0.25, 2 × 0.0625) = 0.25 nats (§2.1);
   - the extension median rel, 0.0132 (§3, §4.2).

   These are arithmetic only, to stand if the seat names "bare" (§4.1).
7. **No count under another tolerance can be derived from the record.** The comparison's values are printed only as
   counts and medians, and none is written. A count under another bound needs a driver that takes that bound (v2f's
   comparison takes R3's bound alone, `label.max`) and the comparison run again on the box: one load and the vanilla
   forwards, as at this resume.

## 5. Q1 — the label convention of record

A-n1 §2: "Exactly one candidate at 40 of 40 is the convention of record, named in LOCK-n v0.1; none, or more than one,
goes to the seat with the four counts." The seat's corpus answers of 2026-11-18, §5.5, add the four medians, and give
their purpose: "the medians separate a convention that is wrong by nats from one that is right to within hardware".
Here none is at 40 of 40.

**Q1.** Which candidate, if any, is the convention of record: bare, space, bare+eot or space+eot? The figures are §1's
counts and medians.

## 6. Q2 — backend-ext-2

ADDENDUM-n2 §4.1: "If the check names "bare", the run of record of `6df2131` gives them on its resume. If it names
another candidate, the extension's 24 reads are run once more under that convention, in the same session, as a second
stage (`backend-ext-2` …)". The check named none.

**Q2.** Does backend-ext-2 run, and under which convention: the one Q1 names, if any?

Code notes, as fact: v2f carries `backend-ext-2 --convention NAME` for space, bare+eot or space+eot, its own root and
report, with the fidelity rule as the first run carried it (R7: its identity keeps stage "backend-ext"). Its launch
files would follow the seat's word, through the coordinating session.

## 7. Q3 — the comparison's tolerance

A-n1 §2's tolerance is "half a unit in the last decimal BK's `reduced.json` records, plus the backend's identity
bound". ADDENDUM-n2 §2.2 makes the identity bound C, which under "bare" is 0.25 nats (§4 item 6). The resume ran with
R3's bound, the largest per-label |cached − fresh| over the 24 reads, 0.0492 nats. The seat's answers of the third
sitting, §1.4: "Code's R3 — the comparison's bound as the largest per-label discordance — is accepted as a printed
measurement; the lock's bound is ADDENDUM-n2's C."

ADDENDUM-n2's committed entry (`7a54eb9`) records the coordinating session's reading of this, from its referent check:
R3 for the resume, "with C binding from the lock, since C is computed under the convention the comparison names".
C's 0.25 floor does not depend on the convention.

**Q3.** Is the comparison's tolerance R3's bound as run, or C, or another? If it is wider than R3's bound, is the
comparison to be run again under it before Q1 is ruled? From the record, Code cannot say whether a wider tolerance
changes the counts (§4 item 7). Running it under another bound would take a driver change, its commit, and one load on
the box.

## 8. Not questions

- The resume's pass and every step of it (§2).
- The first attempt's failure, a launch-script defect of Code's, declared in the entry (§3).
- The resumed report's commit, with this block; the cell, unchanged, is not committed again (§9).
- The schema's follow-up for the `fidelity-ceiling` kind, and LOCK-n v0.1: both wait for this ruling.
- The box is idle, and nothing runs on it until the seat and the PI say.

## 9. The record

- **This raw:** `results/raw/2026-11-18_n-step4-resume_code-to-design_STOP.md`.
- **The resume** (`results/raw/2026-11-18_n-step4_bext-resume4_…`):
  - `…_out.txt` (`8d286ce4…2a39`, 74 lines) and `…_run.txt`, the pod session's record (`c86e812a…be14`, 121 lines);
  - `…_exit.txt` (`9a271f2a…86aa`, reading 0);
  - the three work files: `…_resume.txt` (`069b1448…2db4`, 12 lines), `…_hashes.txt` and `…_resume-identity.txt`
    (both `93783db0…7b36`, 12 lines);
  - the resumed report, `data/n/reports/backend-ext.json` (`dd217d78…ce79`), which the admit of `6df2131` covers.
- **The first attempt** (`results/raw/2026-11-18_n-step4_bext-resume2_…`): `…_out.txt` (`0c926ca3…bf79`, 9 lines),
  `…_exit.txt` (`4355a46b…d865`, reading 1) and `…_run.txt`, the pod session's record (`2f606ca7…1ce9`, 85 lines).
- **The values-check raw** and **the entry** at the Log's head.

The cell is not committed again: its bytes are unchanged. The capture arrays stay on the box's volume. Nothing is
pushed.
