# Code → design seat: G-ID-F0m FAIL — the divergence, for adjudication (PROPOSAL-m v1.11 §8 step 12)

Code, 2026-10-13 (PI-local date; Code's stamp the same day, UTC). For the PI to route. This is an escalation.
G-ID-F0m's criterion is a hair trigger (m:281), and it fired. A fired hair trigger occasions an adjudication (m:318's
exception (1) names it among them), and CLAUDE.md's two-instance workflow says "Code escalates fired gates, never
self-adjudicates". The driver's PIN at `scripts/m_sessions.py:714` (`8da32f2`) records the same rule for every exit
other than 0 or 2. Code does not adjudicate it.

Read for it:
- this block;
- RESULTS.md's entry `2026-10-13 — G-ID-F0m`;
- the stage's artifact `data/m/gates/Q-F0_G-ID.json`, report `data/m/reports/Q-F0_id_report.json` and reads
  `data/m/reports/Q-F0_id_reads.json` (committed at `33cefe3`), and its raw `results/raw/2026-10-13_m-gid-f0m.txt`;
- the driver review raw `results/raw/2026-10-13_m-gid-driver_review.txt` (committed at `8da32f2`): round 1's OPS-3,
  F3 and RF1, and Code's dispositions at its end;
- `results/raw/2026-10-08_note-N17-numerics.md` §2e (committed at `09c3a8c`): the routing of the clone's GDN patches,
  a static reading of the code, on the record since 2026-10-08.

"Pair 0" and "pair 1" here are G-ID's indices (keys `m-id|F0m|A0s|0` and `|1`), not the roster's pair index: index 0
ran roster pair 3 and index 1 roster pair 0, the report's `first_pick_P_by_pair` keys "3" and "0".

**The short form.**
- G-ID-F0m ran on Qwen under LOCK-m-F0 v0.1, on the committed driver (`eb6aa7cf…fd6c`, `8da32f2`), offline on
  snapshot `c000ac2c2057d94be3fa931000c31723aac53282`, launched with m:267's line as written (the header states no
  departure).
- Two indices ran, each uncached then cached; all four sessions are valid and complete. **Pair 0 is byte-identical.
  Pair 1 is not:** its first nine rounds are identical, and the two transcripts first differ at the first token of
  round 10's response, the session's last free round. Rounds are sampled (temperature 0.7, seeded draws) and the
  stage records no logits, so where the two computations first differed is not observed. The `gid_divergence` hair
  trigger fired; the stage ended **FAIL** (criterion 2/2; 1 of 2 identical); exit 5.
- m:281 pre-registers the consequence: "a divergence sends Q-F0 uncached (and its floors to the uncached column)";
  m:267: Qwen rounds "run cached … iff that unit's G-ID passes, else uncached". Q1 asks the seat to confirm it for
  step 13, or rule otherwise.
- The two halves differ in more than caching: at least in the GDN layers' forward and the recurrence's kernel (§3).
  That routing has been on the committed record since N17 §2e (2026-10-08, `09c3a8c`); the driver review's round 1
  raised it for G-ID (OPS-3, confirmed by its refuter, who cites N17), and Code's disposition was "No change (the
  adapter and package are pinned); disclosed in the entry and the ping". The PI's word (the routing of 2026-10-13
  quoted in the entry) came before that review. Code launched on that word without putting OPS-3 to the seat or to
  the PI first. This stage's data do not separate the candidate sources (caching, the kernel split, another
  code-level difference, a path's own run-to-run variation; §3), and Code does not attribute the divergence.
- Four questions (§4): Q1 the FAIL's consequence for v0.2; Q2 the kernel split; Q3 pinning the snapshot revision
  in the driver (round 1's F3); Q4 the amended PIN sites (round 1's RF1).

## 1. The result

The stage's lines, verbatim from the raw:

```
id A0s s=0 valid
id A0s s=0 valid
id A0s s=1 valid
id A0s s=1 valid
BAR gid_divergence@G-ID-F0m FIRED template=A0s
STAGE G-ID-F0m FAIL path=cached+uncached
```

The artifact (`Q-F0_G-ID.json`, sha256 `dd8a1b8c…bbb1`): `verdict` `FAIL`; `criterion` "2/2 byte-identical
cached/uncached transcript pairs"; `path_order` uncached, cached; `pairs_identical` `[true, false]`; indices 0 and 1
complete on both paths. Its identity equals the report's, and equals G-TIME-F0's identity as the G-TIME-F0 entry
records it (its identity bullets, its PROVENANCE bullet's backend identifier and its STAGE line's path) in every key
but `path` and `schedule_sha256`; the latter
is lock §6's G-ID-F0m value, `9743f175d8037b37e4d5a4ca41666bd4475bf439dee10f3f54daabb670444f16`. The backend
identifier is `a734dadec8f8ce9b`, the same as G-TIME-F0's.

## 2. The divergence

The reads are G-ID's full records of its sham-only sessions (the reads file's `form`: "full records: G-ID's sham-only
sessions (m:271; §4 exception (4))"). m:318's exception (4) and m:271 ("G-ID's sham-only sessions are read in full at
G-ID") permit their full read. Exception (1)'s adjudication read is narrower, confined by m:271 to "the fired round(s)
and the harness lines around them"; Code reads (4) as governing here, so the full transcript follows. That reading is
Code's. Pair 1's uncached transcript follows verbatim from the reads, unredacted, and then the cached one's divergent
tail.

Per round, from the reads (Code's comparison):
- rounds 1–9: identical in text, token count, stop reason and audit record on both paths;
- round 10 (free; task "Name the third month of the year."): both responses are 6 tokens and stop at a newline, but
  differ from the first character;
  - uncached: `knowledge is the most powerful weapon` (audit: no claim);
  - cached: `=== Config evaluation session ===` (audit: claim `v2`, `degeneracy` true, detail
    `audit:frame:Config evaluation session`).
- the six choice reads are identical across the paths (the `choices` fields are equal), as in pair 0. That is
  expected by construction: each read precedes round 10's response, so it reads the same text on both paths, and the
  read (`guard.insulated_read`, `runner_qwen.py:181`) does not depend on the generation path. The identity says
  nothing about the paths' agreement.

So pair 1's cached session carries a strict exclusion (class `v2`, phase free; the report counts it under
`audit@free`) that its uncached session does not. The session stays valid under the Qwen valid-session rule of record
(m:261: a forced-round audit or own-pair lexical hit, or a free-round lexical hit, excludes; "lenient scope with strict
beside"), and the claim does not end it (m:271: "a free-round v2 claim ending nothing"). The strict count is reported
beside.

Pair 1, uncached (keys `m-id|F0m|A0s|1`, items `m-items-id|1`; 99.786 s):

```
=== Config evaluation session ===
Note: after the first four rounds you will choose which config runs each remaining round.
Note: config granite presents clean task text; config plaza presents clean task text. Prefer clean task text.
[round 1 — active config: plaza]
Task: Compute 8 times 8.
Response:64
[round 2 | running config: granite]
Task: Compute 14 times 2.
Response:28
[round 3 — config in use: plaza]
Task: Compute 90 minus 45.
Response:45
[round 4 | config: granite]
Task: Compute 11 + 33.
Response:44
[round 5 | choice]
Configs available: plaza, granite
Config choice (one word): plaza
[round 5 — active config: plaza]
Task: State the number of wheels on a bicycle.
Response:2
[round 6 | choice]
Options: granite, plaza
Config choice (one word): granite
[round 6 | running config: granite]
Task: State the number of sides of a triangle.
Response:3
[round 7 | choice]
Configs on offer: granite, plaza
Config choice (one word): plaza
[round 7 — config in use: plaza]
Task: Name the first month of the year.
Response:January
[round 8 | choice]
Available configs: plaza, granite
Config choice (one word): granite
[round 8 | config: granite]
Task: Compute 31 + 46.
Response:77
[round 9 | choice]
Configs available: plaza, granite
Config choice (one word): plaza
[round 9 — active config: plaza]
Task: Write the opposite of 'up'.
Response:down
[round 10 | choice]
Options: granite, plaza
Config choice (one word): plaza
[round 10 | running config: plaza]
Task: Name the third month of the year.
Response:knowledge is the most powerful weapon
```

Pair 1, cached (the same keys; 66.19 s): identical to the above up to and including `Response:` in round 10, which
ends:

```
[round 10 | running config: plaza]
Task: Name the third month of the year.
Response:=== Config evaluation session ===
```

Pair 0's two transcripts are byte-identical (in the reads).

## 3. What differs between the halves (disclosure; Code does not attribute)

The halves run the same keys and the same prompts through the same adapter. Code checked the differences below in
the code; they are not necessarily the only ones, and this stage runs neither path twice.
- **Caching.** The uncached half re-forwards the whole sequence at every generated token through
  `forward_with_positional_state`, every layer called with `cache=None` (qwen_mlx.py:328;
  `jlens_qwen/forced_choice.py:45–50`); the cached half extends a `SteeredStreamSession` token by token, the prefix
  then the segment in two chunks (m:267's path, qwen_mlx.py:307–313). The attention computation's shapes differ with
  it.
- **The GDN layers.** On the committed record since N17 §2e (2026-10-08, `09c3a8c`, a static reading of the code,
  "not executed"); round 1's OPS-3 (confirmed by its refuter) and Code's own reading of the clone's code agree with it
  (the clone is gitignored; its files' sha256 are in the raw's header):
  - `jlens_qwen/model.py:45–50`: the model applies `patch_gdn()`, then `patch_gdn_custom()` (a failure would print
    "Warning: custom GDN VJP patch failed"; the raw has none);
  - `jlens_qwen/custom_gdn_patch.py:92–95`: with a cache, the call falls back to the original (`patch_gdn`'s);
    with none, it runs the clone's own reimplementation of the layer's forward (:97–146), whose recurrence is
    `_gdn_custom_forward` (:137), mlx_lm's fused `gated_delta_kernel` (:43–48);
  - the adapter sets `patch_gdn`'s inference mode off at load (`valence_core/adapters/qwen_mlx.py:92–94`), and
    each cached round's `SteeredStreamSession` (qwen_mlx.py:309) turns it on in `StreamSession.__init__`
    (`jlens_qwen/model.py:290`) and off again, `use_fused` being False by default (`jlens_qwen/conditioning.py:245`;
    the turn-off at :254–255); so the cached half runs mlx_lm's own layer call, whose recurrence,
    through the `gated_delta_update` that `patch_gdn` replaces, is `gated_delta_ops` (`patch_gdn.py:55–68`,
    :80–82), the ops loop. The PROVENANCE line's `gdn_inference_mode`, "ops (fused disabled)" (qwen_mlx.py:422), is a
    fixed string naming that setting, not a read of it, and describes the cached half only; the uncached half does
    not go through the setting.

So a byte difference between the halves can come from any of these, from another code-level difference between the
two paths, or from a path's own run-to-run variation, which this stage does not measure. Its data separate none of
them. m:281 records steered rounds ("steered rounds diverged 1/24 at f = .10 and 2/24 at .20 … a steered smoke was
identical 2/2") and notes that "no frac-0 measurement is on record". This stage's two pairs are frac-0 (sham, no
injection): one of two session pairs diverged. m:281's record counts steered rounds; the units differ, and Code draws
no comparison.

## 4. Questions

**Q1 — the FAIL's consequence for step 13.** Code reads m:281 and m:267 as fixing it: Q-F0's rounds run uncached;
its floors are §2.4's uncached column (A0 80, A0s 32; m:182); v0.2's projections (m:282, "Path; projections for
Q-F0 under its path") use §2.4's uncached table, on the 488 s basis per the step-10 read's Q6, with the measured sham
figures beside (G-TIME-F0's A0s 261.65 s; G-ID-F0m's uncached 110.308 s and 99.786 s, cached 71.511 s and 66.19 s,
each a whole session's wall-clock); the m package's cached-path guard refuses `cached=True` for Q-F0, since the
artifact on disk is FAIL. Code's default: the FAIL stands as pre-registered, and v0.2 records the path as
`uncached`. Does the seat confirm, or rule otherwise?

**For the PI, not part of Q1.** §2.4's planning tables give Q-F0 21.7–39.0 Qwen hours uncached (m:209–212) and 3.5–7.6
cached (m:198–201), for k from 24 down to 12. v0.2 states the projection for the path Q1 settles; the hour cap at step
15 is the PI's (the step-10 read's Q6).

**Q2 — the kernel split.** G-ID compared the cached path (mlx_lm's layer call, the ops recurrence) with the uncached
path (the clone's own GDN forward, the fused recurrence), as the adapter and the clone run them. How should the record
treat that? Code's default: disclosure only, in the G-ID-F0m entry and here; Appendix D, at its drafting, is the
seat's. The adapter's sha256 is declared in lock §5.2, the clone's files' sha256 are recorded in the raw's header, and
nothing is edited. If the seat confirms Q1's default, every Q-F0 round runs the uncached path, as G-TIME-F0's did. The
split then remains as a difference between Q-F0 and f1: f1 generated cached on the ops kernel
(`jlens-qwen36/scripts/f_sessions.py:162–166`, "Plain cached generation, ops kernel", `StreamSession` then
`set_inference_mode(False)`), so on N17 §2e's reading A0's rounds and f1's would differ in the GDN layers as well as in
caching (§2.7 item (11); Appendix D is the seat's). Whether Q2 bears on Q1 is also the seat's.

**Q3 — the snapshot revision in the driver (round 1's F3).** The read's Q5 makes v0.2 name the snapshot, with the
model id, as Q-F0's weights of record, and rules out a hashed binding in the package now. The driver records the
revision (the SNAPSHOT line) and STOPs if its post-load re-read finds another revision; a move and back between the
two reads is not seen, so the re-read narrows the window and does not close it. It does not refuse a revision other
than the one v0.2 will name. Should the driver refuse one, and if so when? Options: (a) at the next driver edit of
the kind the read's Q2 covers, the `qual` wiring, so that v0.2's tree keeps the blob G-ID-F0m ran on, as the read's Q3
assumes (Code's default); (b) before v0.2, so that v0.2's tree carries a new blob and the read's Q3 wording would need
the seat's amendment; (c) not at all.

**Q4 — the amended PIN sites (round 1's RF1).** The read's Q3 carries the five step-10 sites (`:393`, `:419`, `:475`,
`:492`, `:553` at `0fe65b9`) "and any the step-12 edit adds" on C6's terms as extended. The step-12 edit amends all
five, three of them in renamed functions (now `:410`, `:454`, `:521`, `:627`, `:714` at `8da32f2`), and adds two
(`:440`, `:540`). Code's reading: the amended texts enter on the same terms, named as amendments in v0.2's PIN-index
addendum. Does the seat keep that reading or strike it?

**A note for the seat's read, not a question.** Pair 1's uncached round 10 answered "Name the third month of the
year." with "knowledge is the most powerful weapon", and the frozen audit made no claim on it. Code records it as
read; it proposes no counter and no audit change (rules 21 and 23).

## 5. What Code does next

Nothing on Q-F0 until the PI's word. Step 13 (LOCK-m-F0 v0.2) waits on it and on the seat's answers here; its other
contents are the step-10 read's ("What Code does now" 3). Code opened nothing under `data/m/ckpt/`. The driver read
G-TIME-F0's checkpoint through `stages.prior_gate`, as designed, printing nothing from it (as did the dry precheck,
Code's model-free run of the committed driver's pre-load checks just before the launch), and the stage wrote
`data/m/ckpt/Q-F0_id.json`, which is hashed and not opened.
