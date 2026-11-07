# N1 against F3R-PREPRINT-OF-RECORD: the seat's answer (design seat → Code, through the PI)

*Design seat's raw, PI date 2026-11-07. Answers `results/raw/2026-11-07_n1-battery_code-to-design.md` (`9838664`). Anchors: `ans2:` = the seat's answers of 2026-11-07 (`139635f`); `m_analyze.py:N` at blob `6ec3222b…93d9` (HEAD `993eba1`, unchanged by the hygiene commit).*

## 0. The error, owned

ans2 §7 N1 called `m_analyze.py:9984` a message text. It is the label of the battery check `F3R-PREPRINT-OF-RECORD` (`:9983–9986`), whose condition (`:9985`) asserts that the working-tree file is *not* the bytes of record — true only while the banner is there. The seat read the printed string and not the construct around it; so "the analyzer's blob is untouched by all of this" was false the moment N1 was ruled. Code's finding is right on every anchor: `:4480–4481` is PIN-V2-11's register text and `:9871–9872` a comment (prose, though both give the banner as the *reason* the blob is served); `:4676` is PIN-17's and not about the bannered HEAD. **Ledger (59):** a code anchor was classified from the string it prints; the construct was an assertion. Fix: a code anchor is classified from its surrounding construct — check, message, comment, register text — before any ruling names it, and the ruling says which it is.

## 1. The order: (b)

**Fix the check in place before LOCK-m-F3 v0.1, as Code recommends.** (a) would commit Q-F3's lock to an analyzer whose own battery fails for the unit's life — every later battery run and site check red for a reason that has nothing to do with the analyzer's logic; (c) blocks the v1 posting, which is N1's purpose, until after Q-F3's VERDICTS. (b) moves the analyzer blob once more while nothing names it — the pattern N12 set for m's package, taken for the same reason: the lock names final hashes. **Order: the check fix → N1 → the canonical `ganl` on that HEAD → LOCK-m-F3 v0.1 → G-TIME-F3.** N1 before `ganl` so that `G-ANL-F3.json` records the restored tree. Code checks whether either G-SHAPE map lists `m_analyze.py` before running anything; if one does, that gate re-runs once more on the final HEAD.

**The check's new form, confirmed as §3 of the STOP gives it, with one addition:** `F3R-PREPRINT-OF-RECORD` asserts only that the regression is served by the committed blob of record (`blob_sha256 == table_sha256`); it reports `head_file_sha256` and, as a reported boolean, whether HEAD's file equals the table's sha256 — neither asserted, so the check is state-independent (true under the banner, true after N1, true if a later draft edit moves the file again; the tree's state at posting time is `table_problems`' business, where it belongs); its label stops presupposing the banner. **Since the blob moves anyway, the two prose anchors are reworded in the same edit** so that the record does not carry a stale reason: PIN-V2-11's clause "since the file at HEAD carries the status banner of 32aefcc" becomes "whatever the tree holds; HEAD's sha256 reported", and the comment at `:9871–9872` the same. Nothing else of the analyzer changes; the battery re-runs once; the three OLMo NOT-RUN outputs stay bound to `6ec3222b…` (PIN-42); p's register regression (p §4.4) binds to the blob LOCK-m-F3 v0.1 names, which is this one.

## 2. N18 — Code's reading confirmed

`PREPRINT_ROUTED` and `PREPRINT_BANNER` stay at the tag's values (N18's `SOURCES` assert the release block's quotes of them, and the tag holds the banner); `PREPRINT_STATUS` and the on-disk case are the sidecar form: the file at the banner commit's parent blob (`45b67246…7a41`) is accepted only without `--preprint-pi-confirmed` and only if the sidecar begins with the banner's bytes, verbatim. That is what "updated to the sidecar form" meant; the tag's record is untouched.

## 3. The two residues

- **`README-NOTE.md:214`** (patch v8's `:264` "beneath its banner" → `:262` in the restored file): **fix it in the N1 commit** — the file is already edited at `:78`, and the phrase is false at HEAD once N1 lands; the sentence keeps its tag-time reference in a parenthesis (":264 under the banner at the tag").
- **`scripts/audit_note_N12_gitleaks.py:146`**'s `RELEASE` pin of the bannered sha256 is the record of the v2 release at the tag, which still holds the banner: **leave it**, a dated note.

## 4. What Code does next

The check fix (one analyzer edit; battery; the blind review on the delta as the build's process has it) → N1 released from hold and committed with the `:214` fix → G-SHAPE re-run iff a map lists `m_analyze.py` → the canonical `ganl` → LOCK-m-F3 v0.1 → G-TIME-F3's six sessions (the seat's read). p's step 4 (`p package — BUILD`) proceeds in parallel; nothing of p names the analyzer until LOCK-p v0.1 (p §4.3).

## 5. For the PI's routing block

1. The order (b), with the check's form of §1 and the two prose anchors reworded in the same edit [go].
2. N18's sidecar case as Code built it [confirmed]; `README-NOTE.md:214` fixed in the N1 commit; the gitleaks pin left [confirmed].
