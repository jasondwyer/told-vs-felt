# ADDENDUM-n2 v0.1: the referent check of its §6.4, and Code's grading (PI date 2026-11-18)

Code's raw for `ADDENDUM-n2 v0.1 — COMMITTED`. The addendum's §6.3 (1) asks for "referent check of 6.4; an
unresolved substantive item → STOP". One fresh blind checker, a subagent of the coordinating session, checked every
statement of the addendum that quotes, cites, paraphrases or gives a number from a referent §6.4 lists, and the other
sources the addendum cites. Its brief:
- quoted the list of record v2's items 1–5, with item 4's amendment by C.2 of 2026-11-16;
- carried the briefs' two lines, "a git command in a check takes item 3's pathspec" and "a glob is expanded and read
  before it is looped over";
- required the `data/mf3` exclusion while Q-F3's campaign runs;
- allowed no interpreter.

Its report is reproduced whole, as its hand-back message gave it, with the harness's two-space indent removed. The
result is byte-identical to the unindented copy of the report that the session's record also holds (430 lines). It
held no local path. Code's grading and dispositions follow it.

## 1. The checker's report, whole

Referent check of ADDENDUM-n2 v0.1: 52 listings covering 49 distinct statements (three are cross-listed). Grades: CONFIRMED 36, IMPRECISE (minor) 13, IMPRECISE (substantive) 0, FAIL 1 (a section citation that changes nothing the addendum rules), NOT CHECKABLE 2.

HEADER

Document
- `ADDENDUM-n2-fidelity-on-the-box-of-record-v0_1.md`, at the repo root, untracked (a scoped status shows "??").
- sha256 41f76c49…bb3f, abbreviated by cut. In full it equals the expected value.
- 9,671 bytes.
- Checkout HEAD: 3b2b855.

Labels used below
- n = `PROPOSAL-n-bk-reconciliation-v0_2.md`
- A-n1 = `ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md`
- S2 = `results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md` (the second sitting of 2026-11-18)
- S3 = `results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md` (the third sitting; context only)
- RUL = `results/raw/2026-11-18_n-step4-p01_ruling.md`
- STOP = `results/raw/2026-11-18_n-step4-run-pause_code-to-design_STOP.md`
- RUN = `results/raw/2026-11-18_n-step4_bext-run3_out.txt`
- DIAG = `results/raw/2026-11-18_n-step4_bext-diag_out.txt`
- NB16 = `results/raw/2026-11-16_n-build_design-to-code_answers.md`
- NG16 = `results/raw/2026-11-16_n-ganl_design-to-code_answers.md`
- Q718 = `results/raw/2026-11-16_n-schema_code-to-design_questions.md`
- GD = `results/raw/2026-11-06_n-gdata.md`
- SSTOP = `results/raw/2026-11-18_n-step4-smoke-pause_code-to-design_STOP.md` (0eb7671's block; context only)
- DRV = `scripts/n_sessions.py` (context only)

Provenance
All referents are tracked and clean against HEAD (scoped status). Commits come from `git log` per file; hashes are abbreviated by cut.
- n: 30a3d0f5…04f4; its only commit is 5916097.
- A-n1: e979f8f2…5e03; only commit a61f13d.
- S2: cdecf39e…01d3, the value STOP:20 cites; only commit dc6a1cf.
- NB16 and NG16: both only at 52b2c97.
- STOP, RUN and DIAG: only at 6df2131. RUN is 910e20a7…0e48 and DIAG is 0d311f01…fc8b, the values STOP and S3:3 cite.
- Q718: only at 718c48e.
- GD: only at 1d51673.
- RUL: e2b1c77a…2a8a; only at 3b2b855.
- S3: only at 3b2b855.

What I read
- The addendum :1–51, in full.
- n :1–165, in full.
- A-n1 :1–86, in full.
- In full: S2 :1–76, S3 :1–67, RUL :1–10, STOP :1–224, RUN :1–88, DIAG :1–51, NB16 :1–79, NG16 :1–70.
- Q718 :134–175 (Q4), plus a heading grep.
- GD :40–69 and :180–234, plus a fixed-string grep.
- CLAUDE.md :325–345 (rule 21 is :333–341).
- RESULTS.md by fixed-string grep only, output truncated: :610 for "(82)"; :11510 and nearby lines for "D_n".
- SSTOP by grep only: :127–129, :139, :176 and the R6 lines.
- DRV :60–82, plus a grep for "R3" (:65, :76, :1220).

Tools
- shasum -a 256, with cut for abbreviations.
- wc -c on the addendum; wc -l on the referents. None is under data/.
- git rev-parse HEAD.
- git ls-files, git log --format (ids, dates, truncated subjects), git grep -l -F and git show --name-only --format=%h. Each took either `.` with `':!data/**' ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'`, or a named file with the three `/**` exclusions.
- One git status scoped to named paths (see DEPARTURES).
- /usr/bin/grep (-n, -c, -F) on named files; sed -n; cut; sort -g; tail; head.
- One name-only ls of results/raw.
- zsh's built-in arithmetic expansion.
- The file-read tool.

Not done
- No file written.
- No git add, commit, checkout, reset or stash, and nothing else that changes the index, the tree or a ref.
- Nothing under data/ read, listed, hashed or searched, data/mf3 included.
- No interpreter: no python, node, ruby, perl or osascript, and no awk or bc.
- No network.
- No --stat or --numstat.
- No whole-tree status.
- No marker word in any argv.
- No search outside the repo.

CLAIMS

A. PROPOSAL-n v0.2

1. Header: "PROPOSAL-n v0.2 (tracked at root, sha256 `30a3d0f5…04f4`) stays the proposal of record".
   CONFIRMED. The hash is 30a3d0f5…04f4; the file is tracked; its only commit is 5916097.

2. §0.1: "n §2.1 adjudicates each read's cached-versus-fresh discordance by BK's TAU, 0.0178835444 of the read's scale".
   CONFIRMED. n:77: "|cached − fresh| is adjudicated by BK's frozen scale-relative criterion, TAU = 0.0178835444 of the read's scale".

3. §0.1, the quoted clause "by exact binomial against p0 declared in LOCK v0.1 from BK's measured rate at TAU on the 160 sessions (G-DATA (vi))".
   CONFIRMED. Verbatim at n:77 (fixed-string match).

4. §1's heading "(amends n §2.1 and §0.10 B2)", and §6.1's "§0.10 B2 (p0's source)".
   IMPRECISE (minor).
   - B2 (n:47) carries p0's source.
   - B2 also says "the d = 0 identity bound is the backend's measured nondeterminism", which §2.2 replaces with C.
   - Neither §2's heading ("amends n §2.1 "Identity" and n §6") nor §6.1 lists B2 for that clause.
   - §2.2 states the new bound outright, so nothing that runs changes.

5. §1.1: "TAU, the cadence of 160 reads, the exact-binomial test at the lock's alpha, the pause-and-adjudicate form and the ungated primary are unchanged". §6.1: "Unchanged: TAU, the cadence, alpha, …".
   IMPRECISE (minor).
   - Confirmed at n:77 (and n:47): TAU; "cadence every 160 reads"; "exact binomial"; "a fire pauses and the seat adjudicates (rule 21)"; "the primary analysis is ungated".
   - Neither n v0.2 nor A-n1 names any alpha (a case-insensitive search finds none).
   - The binomial's alpha in force is the driver's R5, `BEXT_ALPHA` (SSTOP:128–129). The smoke's pause record shows it as 0.01 (SSTOP:139).
   - S2:32 keeps it declared: "R5's alpha is moot at p0 = 0 and stays declared".
   - So v0.2 has no alpha for it to be "unchanged" from, and "the lock's alpha" is one LOCK-n v0.1 has yet to state.

6. §2.2: the quote "the d = 0 read is the vanilla forward's margin within the backend's measured nondeterminism", and the clause it strikes, "exact on a deterministic backend".
   CONFIRMED. Both are at n:77 (fixed-string matches). The clause is the parenthetical "(`BACKEND — characterization`; exact on a deterministic backend)".

7. §2.1: "n §6's pause-and-adjudicate form". §2.2: "n §6's "the identity bound exceeded at d = 0"".
   CONFIRMED. n:148: "Pause-and-adjudicate: the fidelity binomial (§2.1); a rendering mismatch; NaN/inf; the identity bound exceeded at d = 0; …".

8. §3: "The row at TAU/4 stays as BK's form" (it amends n §2.1 and §4 (f)).
   CONFIRMED.
   - n:77: "a sensitivity row drops reads above TAU/4".
   - n:47: "a sensitivity row at TAU/4, as BK report theirs".
   - n:128: "(f) the fidelity sensitivity row (TAU/4) for every primary".

9. §0.2: "below BK's own maximum of 0.125 on their box". §2.1: "0.25 is twice BK's maximum of 0.125 nats".
   CONFIRMED.
   - n:77: "BK's own reads: median 0.031 nats, maximum 0.125".
   - GD:57–58: "median 0.03125, maximum 0.125".

10. §5: "small against the session SD BK report at d = +1 (0.623 nats) and the effects n §2.5 sizes".
    IMPRECISE (minor).
    - 0.623 is at n:97, and GD:49 reproduces it as 0.6233.
    - But n §2.5 is marked "[S; population SDs, ddof 0]" and computes the figure "From BK's released reads". It is the seat's figure, not one BK report.
    - The per-read maximum (≤ 0.0868 nats, claim 32) is small against the d = +1 sizing: the 0.545 bar and SE 0.049.
    - It is of the same order as n §2.5's lower d_eq estimate, "≈ 0.12 at 1/3 by interpolation" (n:97). There, "small" rests on the sentence's own "averages across sessions" (n:97 gives SE ≈ 0.02 at d_eq).
    - Not substantive: every arm reads through the same path.

11. G-ACQ as the addendum uses it: "the BACKEND extension", "the extension's 24 reads", and §2.2's reading of the identity bound as "the cached shadow against the fresh forward".
    CONFIRMED. n:109: "`BACKEND — characterization` for this box, extended with the fresh-versus-cached discordance distribution over 24 reads (§2.1's identity bound)".

12. Header: "It changes no arm, dose, bar or sentence of n §5, and not the Clock (D_n 2026-12-15)".
    CONFIRMED.
    - n:152: "D_n (N-pod) proposed **2026-12-15**".
    - RESULTS.md:11510 records "D_n = 2026-12-15" under v0.2.
    - No text of n:132–144 is edited by the addendum.

13. §6.3: "Entries this addendum adds to n §8's list".
    CONFIRMED. n:161 is §8's entries list.

14. §6.2 (2), the declined form: "p0 stays BK's 0 of 2,400 and the campaign pauses at its first exceedance".
    IMPRECISE (minor).
    - The binomial is evaluated at "cadence every 160 reads" (n:77) and at a run's end (S2:32), not at the exceeding read.
    - The run of record shows this: read 1 exceeded TAU (RUN:58), and the stage paused only at its end (RUN:81).
    - Under p0 = 0 the pause comes at the first evaluation after an exceedance, and PIN-n-37 (S3:44) then stands it on the batch's range.
    - Not substantive: the sentence describes the declined alternative.

B. ADDENDUM-n1 v0.1

15. Header: "ADDENDUM-n1 v0.1 (`a61f13d`, sha256 `e979f8f2…5e03`)".
    CONFIRMED. The hash is e979f8f2…5e03; the file is tracked; its only commit is a61f13d.

16. §5's heading, "settles A-n1 §1.4's reservation, the seat's answers of 2026-11-18, second sitting, §1.4", and §6.4's "ADDENDUM-n1 v0.1 at root: §1.4 (as the seat's answers of 2026-11-18, second sitting, carry it)".
    FAIL (the citation only; not substantive).
    - A-n1 §1.4 (A-n1:26) is "Generated text (G-CAL-n)": G-CAL-n's turns are consumed as their emitted ids. It holds no reservation on the read of record.
    - The reservation is S2's own §1.4, at S2:30: "The read of record. If the diagnostic puts the discordance in the continuation tokens, the fresh path … is the candidate read of record …". S2 cites no A-n1 section there.
    - S3:24 calls it "§1.4 of the previous sitting".
    - The heading's second citation names the right place, so §5's ruling, and what runs under it, are unaffected.
    - Fix: drop "A-n1 §1.4's" from §5's heading, and drop the A-n1 §1.4 item from §6.4.

17. §0.2: "the label convention of record, which A-n1 §2's check settles on the same resume".
    IMPRECISE (minor).
    - A-n1:32 places the check in the BACKEND extension's session, and the resume prints it (RUL:8; S2:23).
    - But A-n1:32 names a convention of record only when "Exactly one candidate at 40 of 40" matches. Otherwise "none, or more than one, goes to the seat with the four counts".
    - So the check settles the convention only in that one case.

18. §4.1: "taken under the label convention of record (A-n1 §2). If the check names "bare" … If it names another candidate …".
    CONFIRMED. A-n1:32's candidates are "the bare label after the generation prompt; the label with a leading space; each followed by the end-of-turn token".

C. The seat's answers of 2026-11-18, second sitting (S2, dc6a1cf)

19. §5's heading, second citation: "the seat's answers of 2026-11-18, second sitting, §1.4".
    CONFIRMED. S2:26–30 is §1.4. Its read-of-record bullet (:30) ends: "the seat decides at the adjudication. If the discordance sits in the first token, the paths are equally noisy and the cached path stays."

20. §5: "The cached path … stays the read of record, as BK's design has it".
    CONFIRMED.
    - S2:30 leaves the decision to the seat.
    - Its condition was met: STOP:186–188, and S3:24 ("it does").
    - S2:30 says the fresh path's implementation "departs from BK's".
    - S3:24: "BK's read of record is the cached margin".

21. §0.3: "a base rate for the binomial that is the monitored box's (ledger (82))".
    CONFIRMED.
    - Ledger (82) is at S2:17. It is the item's only text in the repo; RESULTS.md:610 points to it.
    - Its fix ends: "a base rate borrowed with a bar (ledger (51)) is the box's where the bar binds a box."

22. §2.2: "a deterministic backend repeats each path exactly and still differs between them (ledger (82))".
    CONFIRMED. Verbatim at S2:17 (fixed-string match).

23. §1.2: "What the monitor then detects is a rise above the box's own rate … which is what rule 21 asks of it".
    CONFIRMED. S2:27: "The monitor then detects a rise above the box's own rate, which is what rule 21 wants of it." Rule 21 itself is claim 46.

24. §5: "The cached path — one prefill under the mask, each label's tokens continued through the cache".
    IMPRECISE (minor).
    - S2:15: "one prefill with the cache kept, each label's tokens but the last continued through it, the cache cropped back".
    - STOP:123–126: "per label, its tokens but the last go through the cache in one forward".

D. The seat's answers of 2026-11-16, second sitting, §3 (52b2c97)

25. §2.1: "a new kind, `fidelity-ceiling`, after `non-finite` in the precedence of the seat's answers of 2026-11-16, second sitting, §3".
    IMPRECISE (minor).
    - The precedence is in NB16 §3 (:46). NB16:50: "the precedence fixed here: a rendering mismatch (no read), then non-finite, then the identity bound at d = 0, then the fidelity binomial". Routing item 4 (:74) carries it.
    - `non-finite` is second in that order.
    - That sitting placed two n answer raws at 52b2c97, and each has a §3. NG16's §3 (:54, "What moves, and the order") holds no precedence.
    - The citation does not say which raw.

E. 6df2131's block and the two outputs it commits

26. Header and §0.1: "24 reads, 10 above TAU". §6.4: "the 24 fid lines (10 above TAU; 0.086070 the largest)".
    CONFIRMED by tool over RUN:57–80.
    - 24 read lines.
    - 10 marked "> TAU", at launch indices 1, 4, 7, 8, 10, 14, 16, 19, 20 and 23.
    - 14 marked "<= TAU"; 7 read 0.000000.
    - The largest is fid=0.086070, read 1 (RUN:58).
    - STOP:31 and :92 agree.

27. "under the "bare" (label) convention".
    CONFIRMED.
    - DIAG:33: "the BACKEND extension's 24 reads (labels 'bare', d = 0)".
    - STOP:133: "all 12 "bare" labels".
    - RUN itself does not name the convention. The driver's R2 declares it as "bare" (DRV:74–75).

28. "pause `p01`", and §0.1's "the stage paused at its end".
    CONFIRMED.
    - RUN:81–82: "PAUSE fidelity-binomial at the run's end"; "end PAUSE: 24/24 reads".
    - STOP:32: "fired under p0 = 0 of 2,400: pause `p01`".

29. §0.2: "the first label token agrees exactly between the paths in 24 of 24 reads". §6.4: "the first token exact in 24 of 24".
    CONFIRMED.
    - DIAG:37 and :42: token 0, n 24, min, median and max all 0, for both labels.
    - DIAG:40, :45 and :47 agree; so does STOP:36.

30. §0.2: "the divergent label token carries all of it (medians 0.0031 and 0.0086 nats, maxima 0.0375 and 0.0492)", with §6.4's 0.00314801, 0.00860631, 0.0375112 and 0.0492441.
    The figures are CONFIRMED.
    - DIAG:38: label S, token 1, median 0.00314801, max 0.0375112.
    - DIAG:43: label U, token 1, median 0.00860631, max 0.0492441.
    - Token 1 is the divergent token: STOP:133–134 counts 1 distinct id at token 0 and 12 at token 1.
    The words "all of it" are IMPRECISE (minor).
    - Token 2 carries up to 1.81453e-06 (DIAG:44).
    - STOP:132: "The rest summed is token 1's to within 2e-06".
    - RUL:9 says "carries the discordance".

31. §0.2: "the third token is below 2e-06 nats". §6.4: "token 2 below 2e-06".
    CONFIRMED. The maxima are 1.44522e-06 (DIAG:39) and 1.81453e-06 (DIAG:44); STOP:131 agrees.

32. §0.2: "In nats the margin's discordance is at most about 0.09". §5: "(at most about 0.09 nats on this box)".
    CONFIRMED, as a bound.
    - No referent prints this figure. RUN prints rel; DIAG prints per-label values.
    - Token 0 is shared and is 0 on both paths. So |Δm| ≤ 0.0375097 + 0.0492442 = 0.0867539 nats, using the "rest summed" maxima at DIAG:41 and :46.
    - Lower bound: read 1 has rel 0.086070, and its scale is at least ln 2 because p(S) + p(U) ≤ 1. That puts the box's maximum at 0.0597 or more.
    - The resume prints the exact figure.
    - RUL:9 gives the same bound.

33. §2.1: "0.25 is … about three times this box's under "bare"".
    IMPRECISE (minor).
    - Against the bound in claim 32, 0.25/0.0867539 = 2.88.
    - The referents place the box's maximum between 0.0597 and 0.0868, so the ratio is between 2.9 and 4.2.
    - Either way C = 0.25 under "bare", since 2 × 0.0868 < 0.25.

34. §2.1: "no bf16 realization of either path reaches it, and a cache-path defect does".
    NOT CHECKABLE. This is forward-looking.
    - The referents give observed maxima only: BK's 0.125 nats over 2,400 reads (n:77), and this box's ≤ 0.0868 over 24.
    - The defect leg rests on RUL:9: "a position error would be of order one nat".

35. §5: "the diagnostic shows the two paths agreeing exactly where a label token is near certain and differing by rounding where it is not, on both paths alike".
    IMPRECISE (minor).
    - The diagnostic shows exact agreement at token 0 only (DIAG:37, :42).
    - At token 2 it shows agreement within 1.81e-06, which is not exact (DIAG:39, :44). The discordance sits at token 1.
    - It prints no log-probability (STOP:53), so "near certain", "where it is not" and "on both paths alike" are the seat's reading, not something it shows.
    - S3:16 itself says the diagnostic "cannot tell a continuation-kernel difference from any other bf16 difference".
    - Not substantive: §5 also stands on "as BK's design has it", and S2:30 left the decision to the seat.

36. §5: "The fresh pair's cost, measured at the extension (median 357.1 ms against the cached read's 309.0 ms)".
    IMPRECISE (minor).
    - The figures are confirmed at DIAG:49.
    - They come from the diagnostic's timing line, a declared addition that is never of record (STOP:145–149, :152–156).
    - They do not come from the extension run's records, whose `duration_ms_fresh` stayed closed (STOP:148–149, :192–193).
    - S3:24 says "from the diagnostic".

37. (Cross-listed; same statement as claim 24.) The cached path's description, against STOP:123–126.
    IMPRECISE (minor).

F. 718c48e's block, Q4

38. §0.2: "BK's recorded label log-probabilities are near −10 (for example −9.69 and −11.47 at d = 0 for `floor_b0` run 0), a scale of about 11 nats". §6.4: "−9.69, −11.47".
    CONFIRMED.
    - Q718:141–142: "`floor_b0` run 0 at d = 0 has log p(S) = −9.69, log p(U) = −11.47 and margin 1.78".
    - The scale is "max(|log p(S)|, |log p(U)|)" (Q718:146; GD:186), so 11.47 for this read.
    - BK's mean scale is 11.15 (n:77; GD:187).

39. §0.2: "where probable bare labels give a scale near 1".
    NOT CHECKABLE.
    - No referent prints a log-probability or a scale under "bare" (STOP:53).
    - Where a bound can be derived, it agrees: read 1's scale is |Δm|/rel ≤ 0.0867539/0.086070 = 1.008, and at least ln 2. Read 4's is ≤ 1.30.

40. §0.2: "So the rule, as borrowed, binds about ten times tighter in nats on "bare" than it did on BK's reads".
    CONFIRMED, as arithmetic.
    - TAU × 11.15 = 0.199 nats, against TAU × ~1 ≈ 0.018 nats.
    - For read 1 that is at least 11 times. The claim rests on claim 39.

G. G-DATA (vi), as n §2.1 and GD carry it

41. §0.1: "…(G-DATA (vi))": 0 of 2,400". §1.1 and §6.2: "BK's 0 of 2,400".
    CONFIRMED.
    - GD:192–194: "BK's per-read failure rate at TAU on the 160 sessions … is **0 / 2,400** … **p0 = 0.**"
    - Also GD:225 (G-4), S2:15 and RUL:7.

42. §0.1: "Under p0 = 0 one exceedance fires (rule 21's zero-base-rate form)".
    CONFIRMED.
    - GD:195–196: "rule 21's zero-base-rate form, a hair trigger: one exceedance fires a pause".
    - S2:15: "at p0 = 0 one exceedance fires".

43. §6.4: "G-DATA (vi) as n §2.1 quotes it: median 0.031 nats, maximum 0.125, mean scale 11.15; 0 of 2,400 at TAU".
    IMPRECISE (minor). Every value is correct, but the attribution is loose:
    - n:77 quotes the median, maximum and mean scale as [C] figures, and names G-DATA (vi) only as the source of p0.
    - GD reproduces the median and maximum in (iii) (:57–58), and the mean scale in (vi) (:186–187).
    - "0 of 2,400" is not in n v0.2, which predates G-DATA. It is (vi)'s result (:192–194).

44. (Cross-listed; same statement as claim 9.) BK's maximum of 0.125 nats.
    CONFIRMED. GD:57–58.

H. CLAUDE.md rule 21

45. §0.1: "rule 21's zero-base-rate form".
    CONFIRMED. CLAUDE.md:333–334: "hair-trigger bars only for ~zero-base-rate defect classes".

46. (Cross-listed; same statement as claim 23.) §1.2: "a rise above the box's own rate — a batch whose exceedance count is improbable under p0 — which is what rule 21 asks of it".
    CONFIRMED.
    - CLAUDE.md:334–335: "measured-base-rate classes bind by exact binomial vs declared p0 at every scale".
    - The header's "changes no … bar or sentence of n §5" also fits :336–337: "verdict criteria untouchable by monitoring changes".

I. The ruling raw

47. Header: "the seat's ruling on `p01` (`results/raw/2026-11-18_n-step4-p01_ruling.md`)". §6.4: "by path".
    CONFIRMED. The file is tracked; its only commit is 3b2b855; sha256 e2b1c77a…2a8a, as the brief states.

48. §0.1: "the seat cleared the pause as the measurement".
    CONFIRMED.
    - RUL:1: "cleared as the measurement".
    - RUL:7: "`p01` is cleared … The 24 reads are that measurement."

49. §4.1: "adjudicated by the seat on the same ground as `p01`'s ruling".
    CONFIRMED. The ground is RUL:7–9.

J. Other sources the addendum cites

50. §6.2: "decision (n-3)" and "decision (n-4)".
    CONFIRMED. A-n1:82 uses (n-1) and (n-2); S3:58 has "decisions (n-3) … and (n-4)".

51. §6.3's order: the resume; the comparison; `backend-ext-2` if the convention is not "bare"; the new kind in the runner and the schema, settled with n-analyzer, "the pin moving as before"; n-analyzer's changes; LOCK-n v0.1 drafted to the seat.
    CONFIRMED. S3:28 ("The order"), S3:56–58 and :62; NB16:61 ("The analyzer's pin moves after it, as before").

52. "Placed untracked over the bridge at root"; "PI date 2026-11-18".
    CONFIRMED. The scoped status at HEAD 3b2b855 shows "??". S3:3 gives the date and names the addendum as placed with it.

OBSERVATIONS

1. The comparison's tolerance against C: a mismatch between S3 and the addendum. Read one way, it could change what runs.
   - A-n1:32 (as NB16:37 has it) sets A-n1 §2's tolerance as "half a unit in the last decimal BK's `reduced.json` records, plus the backend's identity bound".
   - §2.2 makes the identity bound C, which is at least 0.25 nats.
   - S3:20 keeps the two apart: "Code's R3 — the comparison's bound as the largest per-label discordance — is accepted as a printed measurement; the lock's bound is ADDENDUM-n2's C".
   - The driver carries R3 (DRV:65, :76–78; 18f19b8e…4f5c, last committed at ad856f0). On DIAG:46's figures R3 is about 0.049 nats.
   - The addendum names neither R3 nor the comparison's bound.
   - Read through §2.2, A-n1 §2's tolerance would be about five times R3. A tolerance that wide could fail to separate candidates that differ by less, for example one label with and without a near-certain end-of-turn token. "More than one" would then go to the seat.
   - One sentence in §2.2 or §4.1 would close this.

2. The identity kind and the ceiling coincide at d = 0.
   - The §2.1 ceiling applies to every re-computed read, at any dose, against C.
   - §2.2 reads the identity bound as the same quantity at d = 0, against the same C. So every d = 0 read above C fires both kinds.
   - NB16:50's precedence runs: rendering mismatch, then non-finite, then identity, then the binomial.
   - If "after `non-finite`" means directly after it, the ceiling always claims such a read and the identity kind never fires.
   - The place is to be fixed in §6.3 (3)'s follow-up schema commit.

3. Under "bare", C is the floor.
   - By claim 32, twice the box's maximum is at most 0.1735, below 0.25. So C = 0.25, which is twice BK's maximum, not a function of this box's figures.
   - RUL:10 says "the fidelity rule's p0 and the identity bound are set from this box's figures under the convention of record".
   - Ledger (82)'s fix (S2:17) reads "a bound on a difference between two computations is declared from a measurement of that difference on the box of record".
   - Within the addendum, §0.3 calls the ceiling "convention-independent", while §2.1's second term is taken "under the convention of record".
   - These differ in wording, not in figures. The seat may want to say that the floor is the declared margin.

4. Alpha now matters.
   - At p0 = 0, alpha was moot (SSTOP:128–129; S2:32).
   - Under §1.1, with this run's k = 10 of n = 24 (if "bare" stands), p0 = 11/26 ≈ 0.42, and alpha decides when the binomial fires.
   - n v0.2 declares no alpha, and §4.2's list of LOCK-n v0.1 declarations does not name one. n:117's "every trigger with its bar" would carry it.
   - Separately, §1.1 calls p0 "the box's measured per-read rate" but defines it as (k + 1)/(n + 2), not k/n.

5. §4.1 branches only on the check naming "bare" or naming another candidate. It has no branch for A-n1:32's third outcome: "none, or more than one, goes to the seat with the four counts".

6. The second sensitivity row's trigger has changed.
   - S2:29 declared the second row "where it empties (PIN-n-20's `tau4-emptied`)".
   - §3, like S3:28, triggers it "where it drops more than half of an arm's reads at a point". That is a different condition from PIN-n-20's.
   - n-analyzer's reader change (§6.3 (4)) needs the new one.

7. All 24 extension reads are N1-V shadows at d = 0 (RUN:57–80, "N1-V none 0"). So p0, C and the median rel come from d = 0 alone. The binomial and the ceiling also bind the re-computed reads at d = ±1 and the 10% sample (n:77).

8. "Not a reference." S2:30 described the fresh path as "the computation BK's own identity check calls the reference". §5 calls the fresh forward "not a reference". S3:24 gives the reason; the addendum does not mention BK's term.

9. Token 0's exact zero has two readings.
   - S2:22 expected the first token to agree because both paths compute it alike: "the same kernel on nearly the same length".
   - S3:16 and §5 attribute the agreement to near-certainty instead.
   - Token 0 is exactly 0 in 24 of 24 (DIAG:37, :42), while token 2 is nonzero, 1.07e-09 to 1.81e-06 (DIAG:39, :44). That fits the first reading at least as well.
   - S3:16 says the diagnostic cannot separate them. This bears only on §5's rationale.

10. Wording differences between S3 and the addendum; the formulas are the same.
    - S3 says "Laplace's floor" (:9, and the routing default at :58); the addendum says "Laplace's rule" (§1.1, §6.2 (2)).
    - S3's short form says "a 0.25-nat ceiling as the identity bound" (:9). S3:28 and the addendum's §2.1 both give C = max(0.25, 2 × …).
    - S3:24 and STOP:152 put the timings "from the diagnostic"; §5 says "measured at the extension" (claim 36).

11. §6.1 does not list n §3 among the sections changed, although §4.2 adds C and the extension median rel to LOCK-n v0.1's contents (n:117).

12. Apart from observations 1, 3 and 10, S3, RUL and the addendum agree on every figure I checked:
    - 24 reads, 10 above TAU, 0.086070 the largest;
    - the per-token pattern with its medians and maxima;
    - at most 0.09 nats, against BK's 0.125;
    - the timings, 357.1 and 309.0 ms;
    - the formulas for p0 and C;
    - `backend-ext-2`, and the order of work.

DEPARTURES (HEAD 3b2b855 throughout)

1. A path-taking git command run without item 3's pathspec and without the data/mf3 exclusion.
   - The command was `git status --porcelain --` over the 13 named referent paths and the addendum. All are outside data/.
   - It printed one line: "?? ADDENDUM-n2-fidelity-on-the-box-of-record-v0_1.md".
   - No path under data/ was named or printed.

2. For the seat to class, under item 5 (a running stage):
   - One name-only `ls results/raw`, piped to `/usr/bin/grep -F '2026-11-18_n-step4'`. It printed 18 names, all n raws of 2026-11-18.
   - If Q-F3's running stage keeps a raw under results/raw, this listing passed over its name.
   - Nothing of that name was printed, and no size or time.

3. For the seat to class, under the no-interpreter rule:
   - I used zsh's built-in arithmetic expansion `$(( … ))` for the five sums and ratios behind claims 32, 33, 39 and 40.
   - No external program ran.

## 2. Code's grading and dispositions

**The addendum is committed as the seat placed it** (`41f76c49…bb3f`). Nothing in it is edited, and no item below is
applied to its text.

**One FAIL, claim 16, graded not substantive, so no STOP under §6.3 (1).**
- The claim: §5's heading, "settles A-n1 §1.4's reservation", and §6.4's "ADDENDUM-n1 v0.1 at root: §1.4 (as the
  seat's answers of 2026-11-18, second sitting, carry it)".
- Code read both places itself. A-n1 §1.4 (its line 26) is "Generated text (G-CAL-n)". The reservation on the read of
  record is the last bullet of the second sitting's own §1.4 (that raw's line 30, "The read of record. If the
  diagnostic puts the discordance in the continuation tokens …"). No A-n1 section is cited there.
- §5's heading names that place in its second citation. §5's ruling, that the cached path stays the read of record,
  and what runs under it are unaffected.
- Code's grading: a citation error, for the seat to correct. The seat may regrade it, and a regrading would come as a
  ruling.

**The thirteen minor IMPRECISE listings** (claims 4, 5, 10, 14, 17, 24, 25, 30 for its words, 33, 35, 36, 37 and 43;
37 is 24 cross-listed) and **the two NOT CHECKABLE items** (34, 39): recorded for the seat, unapplied.

**The twelve observations:** recorded for the seat. Six bear on what runs next. Each was sent to the session it
touches as information; nothing is applied.
- **Observation 1, the comparison's tolerance against C.** A-n1 §2's tolerance includes "the backend's identity
  bound", which §2.2 makes C.
  - Code's reading: the answers' §1.4 settles it for the resume. "Code's R3 — the comparison's bound as the largest
    per-label discordance — is accepted as a printed measurement; the lock's bound is ADDENDUM-n2's C."
  - The structure agrees. C is computed from the extension's largest discordance "under the convention of record"
    (§2.1), and the comparison is what names that convention (§4.1). C cannot bind the comparison that names the
    convention it is computed under.
  - So the resume's comparison runs with R3, as the committed driver carries it, and C binds from the lock. Code
    grades this resolved, not a STOP. One sentence from the seat would close it. The checker placed that sentence in
    §2.2 or §4.1. With the addendum committed as placed, it can go in the lock or in a ruling, and a ruling would
    reach the resume's comparison, which runs before the lock. The n-build session was told.
- **Observation 2, the identity kind and the ceiling at d = 0.** Both read the same quantity against the same C.
  - The ceiling's place in the precedence is fixed in §6.3 (3)'s follow-up schema commit, settled between the n-build
    and n-analyzer sessions; both were told.
  - Whether "after `non-finite`" means directly after it is the seat's.
- **Observation 4, alpha.** Under §1.1, p0 is no longer 0, and the binomial's alpha decides when it fires.
  - n v0.2 declares no alpha, and §4.2's list does not name one. The driver's R5 holds 0.01.
  - LOCK-n v0.1 must state "the lock's alpha" (§1.1). The n-build session was told, for its draft.
- **Observation 5, A-n1 §2's third outcome.** §4.1 has no branch for "none, or more than one". A-n1 §2's own words send
  that case to the seat with the four counts. The coordinating session's relay to the n-build session already says
  so: a STOP.
- **Observation 6, the second row's trigger.** §3's "Where it drops more than half of an arm's reads at a point"
  replaces the second sitting's "where it empties (PIN-n-20's `tau4-emptied`)". The n-analyzer session's reader takes
  §3's trigger, the committed text's. It was told.
- **Observation 7, d = 0 only.** p0, C and the median rel come from 24 N1-V shadows at d = 0. p0 and C bind the
  re-computed reads at every dose, and the median rel sets the descriptive second row. For the seat; both n sessions
  were told.

Observations 3 and 8–10 concern wording or the reasoning behind §5. Observation 11 notes that §6.1 does not list n §3
among the sections changed, though §4.2 adds to LOCK-n v0.1's contents. Observation 12 records that, apart from
observations 1, 3 and 10, the figures agree. They are for the seat.

**The checker's departures**, each disclosed in its report, at HEAD `3b2b855`, for the seat to class:
- a `git status --porcelain` over 14 named paths outside `data/`, without item 3's pathspec or the `data/mf3`
  exclusion, which printed one line (the addendum's "??");
- a name-only `ls results/raw`, piped to a fixed-string grep for `2026-11-18_n-step4` (this date's n step-4 raws),
  which printed 18 names. Under item 5, this matters if Q-F3's running stage keeps a raw in that folder;
- zsh's built-in arithmetic for five sums and ratios, with no external program run.

It read nothing under `data/`, ran no interpreter and wrote no file.

**Anchors.** The report's line numbers index the files at `3b2b855`. Its RESULTS.md anchors (:610, :11510) index
`3b2b855`'s RESULTS.md. The commit that carries this raw adds lines at the Log's head and under `25c9340`'s note,
which moves them (to :778 and :11678 in it).

**A values-check** of this raw's header and §2, of §1's byte-identity with the report's copy, of the
`ADDENDUM-n2 v0.1 — COMMITTED` entry, of the coordinating session's close line on `25c9340`'s note and of the
PI-routing raw is recorded in
[`2026-11-18_addendum-n2_valuescheck.md`](2026-11-18_addendum-n2_valuescheck.md).
