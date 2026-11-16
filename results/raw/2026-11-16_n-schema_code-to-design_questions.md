# n — five early questions for the seat: four on readings the committed schema encodes, one on the label
# convention it leaves to the lock (code → design)

*The n-build session (Code), PI date 2026-11-16. For the PI to route.*

*What it concerns: the read runner's record schema, `valence_core/n/schema.py` (sha256 `77c12d6d…94bc`), committed at
`5a97527` under PROPOSAL-n v0.2 §8 step 6 (sha256 `30a3d0f5…04f4`), on the seat's answers of 2026-11-15, §5.1; and
one finding of the n package's self-test, drafted since and not yet committed (Q5): `valence_core/n/primitive.py`
(`0f56be93…2f14`) and `valence_core/n/testing.py` (`3fd9aed3…dbdd`) as they stood at this block, untracked drafts
that may change before the BUILD. Nothing ran on a model.*

*Why now and not at the BUILD: n-analyzer builds step 9's analyzer from that schema. A ruling against Q1, Q2, Q3 or Q5
means a follow-up schema commit, and work built on the schema moves with it. The questions do not stop the build: the
rest of step 6 proceeds, and the BUILD entry lists every other reading for the seat. Next: the rest of step 6.
n-analyzer's own block of nine questions,
`results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md` (committed at `8e3bf91`, `2cd1acdf…ed03`), asks none of
these. Its readings assume this block's Q3
form, and it cites Q2, Q3 and Q5.*

*Sources read:*
- *PROPOSAL-n v0.2 at root (§0.4, §0.10, §2.1–§2.4, §3, §4, §5, §8);*
- *PROPOSAL-m v1.11 m:172 (`42ab36ec…6c6b`);*
- *PROPOSAL-k §1.4 (`bf7e79ec…3e92`);*
- *the seat's answers of 2026-11-15 (`1f3ce1f9…df84b`);*
- *`valence_core/readout.py` (`774e5ca3…3136`) and `valence_core/adapters/olmo_hf.py` (`df80b79b…92dc`);*
- *BK's committed files under `data/n/bk`: `neutral_passages/reduced.json` (`ec5fea59…ba1d`),
  `neutral_passages/analysis.json` (`12c35645…6b2f`), and the 14 skeleton files (concatenated in name order,
  `be50011a…ba84`);*
- *BK's PDF (`e92c69cb…fa49`), §3.2.1 and Appendix B.2, read through a text extraction made with macOS PDFKit;*
- *the G-DATA (n) entry and its raw (`f88cc8e7…f2dc`), and G-ACQ (n)'s dated note GA-5;*
- *RESULTS.md's `5a97527` entry.*

*Not opened: anything under `data/*/ckpt` or `data/*/reports`, and BK-repo files not copied into `data/n/bk`.*

## Short form

- **Q1.** §2.1's restricted first-token read, when all 12 of BK's labels begin with "Zone".
- **Q2.** §4 (b)'s "committed free-text reply", when §2.1 says no text is generated.
- **Q3.** Whether §2.3's merge of dose points reaches N1-R.
- **Q4.** Recovering BK's label token convention on the box, against BK's recorded d = 0 log-probabilities.
- **Q5.** G-READ-n's capture layer: the read position's residual at the injection layer itself is the shadow's.

Code adjudicates nothing. Q1, Q2, Q3 and Q5 each name the reading the schema encodes, as built, so the seat can see
what a ruling would move. Q4 names Code's proposal; the schema leaves the convention to the lock.

## Q1 — The restricted read (n §2.1, secondary (a) of §4)

**The text.** n §2.1: "beside it this program's restricted two-label first-token read (m:172's `choice_read` form,
b3's on OLMo) on the same forward, a secondary". m:172's form is `readout.choice_read(verify=True)`: the two labels'
first tokens, renormalized, with the combined label mass. The text is read by a vanilla forward and verified by an
identical re-forward whose symmetric KL must be exactly 0.0.

**The fact.** Every one of BK's 12 labels is "Zone" plus a letter and a digit (the 160 records' `cue_S`/`cue_U`).
Each label follows the generation prompt `<|assistant|>\n`. Whether the two labels' first tokens coincide is the
OLMo-2 tokenizer's to say. If they coincide, a first-token read is degenerate: the two probabilities are one
token's, renormalized to 0.5 each. Code can settle the fact without a model, from the tokenizer files on the box, in
the post-build site check. The question stands either way.

**The reading the schema encodes** (Code's, flagged): the read is taken at the first label-token position where S's
and U's token sequences differ (offset k past the read position), with the shared prefix teacher-forced on the cached
path. It records the two divergent tokens' probabilities, renormalized, their combined mass, and the pick, a tie
going to `present[0]` as m's read gives ties to its first label. m's verifying re-forward is not repeated: §2.1's
fidelity re-computation is n's re-forward, taken at d ∈ {0, ±1} and on the keyed sample.

**Readings to weigh:**
- (a) as encoded;
- (b) read at the first label token as written, reporting the degenerate case as such;
- (c) as (a), plus m's verifying re-forward on every read (about 7,360 more forwards, with nothing merged);
- (d) drop secondary (a).

(b), (c) and (d) each change the schema's `restricted` block, and (d) removes it.

**What it stops:** nothing of step 6. It is needed before LOCK-n v0.1, which pins Code's readings (`5a97527`'s entry)
and the analyzer's hash (n §3), and before n-analyzer's secondary (a). Readings (b), (c) and (d) change the schema's
`restricted` block, a follow-up schema commit.

## Q2 — §4 (b), "the committed free-text reply's agreement with the margin's sign"

**The text.** §4 (b) names a secondary over a committed free-text reply. §2.1: "No new text is generated for N1, N2 or
N4." §0.4: "Every campaign read is one forward over a fixed token sequence; nothing is generated under steering in the
campaign."

**The fact.** BK did generate a reply at every read: their read rows carry `free_text`, `committed` and `choice_is_S`.
For example, `floor_b0` run 0 at d = 0 has `free_text` "Zone W6", `committed` true and `choice_is_S` true
(`reduced.json`, `reads.olmo_32b`). BK sampled the replies, with one sampler seed per session
(`neutral_passages/analysis.json`, `prereg.coprimary_choice`). With steering off at the reply's own positions, a
reply is generated under the read's cache, so under a steered cache on every steered read (BK Appendix B.2).

**The reading the schema encodes** (Code's, flagged): no reply is generated, secondary (b) is not computed, and the
schema has no reply field. Code would say so in the VERDICTS entry.

**Readings to weigh:**
- (a) as encoded;
- (b) a short reply on every read, where BK's sits: steering off at every generated position, the steered cache kept.
  How it is decoded is the seat's: greedily, or by BK's seeded sampling. Code's choices would be a cap of a few
  tokens and a newline or end-of-turn stop. Its text, whether it names exactly one zone, and which are recorded.
  - It adds about 7,360 short generations, with nothing merged.
  - It puts 1,280 generations under negatively steered caches into §0.4's exposure table, as Code counts them: 160 at
    N1-V −1, 160 at N1-P −1 and 960 at N1-R −1. Whether these count as "generated under steering" is the seat's.
  - Every reply would fall in the seat's full read of the checkpoint files, after the analyzer (n §4).
- (c) as (b), at d ∈ {0, ±1} only: 3,040 generations by Code's count. They are 480 on N1-V at 0 and ±1, 1,920 on
  N1-R at ±1, 320 on N1-P and 320 on N4. The 1,280 under negative caches are unchanged.

(b) and (c) add fields to the schema and a generation path to the runner. §2.1 and §0.4 would need the seat's words.

**What it stops:** nothing of step 6. It is needed before LOCK-n v0.1. Readings (b) and (c) add a generation path
and fields (a follow-up schema commit), and they change §0.4's exposure table.

## Q3 — The merge's reach (n §2.3, §2.4; C12)

**The text.** §2.3: "**N1-V's dose points:** {+1, +1/2, +d_20, +d_eq, 0, −1} (d_20 and d_eq added to BK's grid; a
point within 0.05 of an existing one is merged)". §2.4's N1-R reads "+1, +1/2, +d_20, +d_eq, −1". C12 (§0.10): each
arm's floor is "the 24 random slopes refit on that arm's own dose points (random reads exist at every point)".

**The reading the schema encodes** (Code's, settled with n-analyzer so both sides derive the same points; flagged):
- the merge reaches N1-R too, so its points stay N1-V's minus 0, point for point;
- a merged point is read once, under the existing point's label;
- +d_20 is merged first, then +d_eq;
- the distance is an IEEE double, at most 0.05; a tie goes to the earlier candidate;
- a point that would merge into 0 is refused.

The campaign's plan is 7,360 reads with nothing merged, 6,240 with +d_20 merged into +1, and 5,120 with +d_eq also
merged into +1/2.

**Readings to weigh:**
- (a) as encoded;
- (b) the merge applies to N1-V alone, and N1-R reads every point it lists, a merged one too.

(b) changes the read plan's counts, when a point merges, and the schema's `read_plan`.

**What it stops:** nothing of step 6. It is needed before LOCK-n v0.1, and before n-analyzer's battery fixes its
plan's counts. Reading (b) changes the schema's `read_plan`.

## Q4 — BK's label token convention

**The text.** n §2.1: "the full-vocabulary log-probabilities of the two labels' token sequences, each summed over its
tokens". BK §3.2.1: "For labels consisting of more than one token, we sum the log probabilities of their constituent
tokens."

**The fact.** BK's files committed under `data/n/bk` record each read's `logprob_S`, `logprob_U` and `margin`. They
record neither the label token ids nor the text scored after the generation prompt. For example, `floor_b0` run 0 at
d = 0 has log p(S) = −9.69, log p(U) = −11.47 and margin 1.78 (`reduced.json`, `reads.olmo_32b`). BK's Appendix B.2
prints a 1.78-nat unsteered margin for a Zone H0 / Zone W6 session.
- A prefix shared by both labels and scored in identical context leaves the margin unchanged. A candidate convention
  that re-tokenizes the labels, or appends a token after each, can move it.
- The fidelity scale also depends on the convention: max(|log p(S)|, |log p(U)|) is G-DATA (vi)'s scale of record,
  so TAU's meaning rests on it.
- G-DATA pinned the rendering by reproducing `ids_sha`; nothing in the committed files pins the label convention
  that way.

**Code's proposal, for the seat to rule on.** With the BACKEND extension on the box after the BUILD, and before LOCK-n
v0.1:
- score a declared set of candidate conventions at d = 0 on a declared subset of BK's sessions. The candidates are
  the bare label after the generation prompt, the label with a leading space, and each of those followed by the
  end-of-turn token;
- compare each candidate's log p(S) and log p(U) with BK's recorded d = 0 values, within a declared tolerance;
- print only each candidate's match count.

The candidate that reproduces BK's values becomes the convention of record, as G-DATA (iv) pinned the rendering. If
none does, it goes to the seat.

**The blinding question.** n §4: "who sees margins before VERDICTS: nobody". These are d = 0 reads, the shadows'
values, compared with BK's published ones, and only match counts are printed. Code reads that as consistent with §4,
since no Δm and no steered read is involved. A match would, however, make the campaign's d = 0 margins known within
the tolerance, from BK's published file. The ruling is the seat's.

**Readings to weigh:**
- (a) the comparison as proposed;
- (b) as (a), but with the stage's own code printing nothing beyond a verdict per candidate;
- (c) no comparison: the lock names a convention by argument, and the fidelity scale stands on it;
- (d) another procedure.

**What it stops:** nothing of step 6. It is needed before the BACKEND extension runs on the box, which would carry the
comparison, and before LOCK-n v0.1, which pins the convention.

## Q5 — The capture layer for G-READ-n (n §2.2, §2.3, §3 G-READ-n)

**The text.**
- §2.3: "**Site:** layer 32 of 64 (BK Table 1) for every direction in N1, N2 and N4".
- §2.2: "the residual at the read position captured at layers 32 and the final layer on every forward, for G-READ-n".
- §3, G-READ-n: "an L2 logistic probe on the residual at the read position (layer 32; and the final layer) … **PASS
  iff the band median AUC ≥ .90**".

**The fact.** The adapter adds an injection to a decoder layer's output at the steered positions (`olmo_hf.py`'s
forward hook). That layer's output at the read position is computed from the layer's inputs at the read position and
the positions before it, which are the previous layer's outputs. The injection touches none of them. So the read
position's residual captured at the injection layer itself is the shadow's, exactly. The state can reach the read
position only from the next layer on, through that layer's attention.

The n package's self-test (drafted, not yet committed) shows this on its numpy causal double. It asserts the
site-layer capture identical to the shadow's while the last layer's and the margin move. k's own probe bands all lie
past its site: L49–L63, L51–L61 and L51–L62, for an L48 injection (k:211; the bands at k §1.4).

**The reading the schema encodes** (Code's reading of §2.2's words, flagged): `capture_layers` is `[layer,
n_layers - 1]`, the injection site and the last decoder layer. If the capture index is the injection index, the
site-layer probe reads nothing by construction. The band median of two layers is then the midpoint of a chance-level
AUC and the last layer's, so at most 0.75: under the reading as encoded, G-READ-n cannot reach its .90 bar.

**Readings to weigh:**
- (a) capture at the injection index + 1 and the last layer: the first layer whose read-position residual can carry
  the state, and the last. Code's proposal;
- (b) a band from the injection index + 1 to the last layer, as k's G2 band (L49–L63). It costs more storage: two
  float32 layers over the campaign's 7,360 reads is about 300 MB, and every further layer adds about 150 MB;
- (c) as written, with the site-layer AUC reported as a structural null and the band median over the two layers;
- (d) the index G-VEC settles decides it.
  - BK's "layer 32 of 64" may name the input of decoder layer 32: the output of 0-based index 31, the adapter's
    index 31.
  - If G-VEC's R check (within 2% of 25.49) puts the injection at index 31, a capture at index 32 is already the site
    plus one.
  - The seat may rule that "layer 32" for the capture means index 32 in every case.

**What it stops:** nothing of step 6. It is needed before LOCK-n v0.1, since the lock pins Code's readings, the
capture layers among them.
Readings (a), (b) and (d) change the schema's `capture_layers` check, a follow-up schema commit.

## Not questions

The schema's other readings, among them these, are declared in its docstring and field tables. The BUILD entry lists
them for the seat, and none needs a ruling before the build:
- what a record is (one per read, the re-computation inside it);
- the two read paths, from BK's `prereg.precondition_cache`;
- the shadow named by reference;
- captures in float32;
- the fidelity comparison's form, and the 10% sample keyed per session;
- `math.fsum` for the log-probability sums;
- the identity check's form;
- N4's lines as §2.4's words;
- the per-session retention interval against rule 5(f)(iii);
- `pod_id` at every n stage.

The stage identity's `read_window` is also declared there.
