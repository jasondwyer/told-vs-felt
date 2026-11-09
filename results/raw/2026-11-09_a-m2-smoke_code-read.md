# The A-m2 smoke — Code's read: the rule's computation, counter (b), and STOP for the seat

*Code's raw, PI date 2026-11-09. ADDENDUM-m2 v0.3 §3 (sha256 `83093812…fa67`); the smoke is never of record, and
its sessions, sham only and of no unit, are readable in full (§3.2). This read is Code's (rule 25: every line of the
raw was read). The rule, not the read, selects (§3.3). The seat reads every reasoning line and response and confirms
the computation in its own raw.*

**What ran.**
- The committed driver, `scripts/mf3_sessions.py` `c9393a48…4d9b` (committed at `9c7062e`), as `time --smoke`, on
  HEAD `0afd842`. It was launched 2026-11-09 18:14:32 UTC (Code's `date -u` stamp, in the raw's header) with m:267's
  line as written, on the coordinating session's go, after a CLEAR dry pre-launch check.
  - An earlier dry pre-launch check, at HEAD `9c7062e`, was refused (ONE PROCESS): the pod session's model-free
    `scripts/p_analyze.py --selftest` was running from the jlens venv. Code reported it and launched nothing. The CLEAR
    check came later, at HEAD `0afd842`.
- Qwen `mlx-community/Qwen3.6-27B-4bit` (snapshot `c000ac2c2057…`, unchanged after the load), uncached, reasoning
  cap 60, under LOCK-m-F3 v0.1's licence (`377c5d60…`). After the load, each of these passed on its own line in the
  raw: the snapshot re-read, m:267's laptop checklist (the GATE line), the licence, and the A-m2 check. The backend is
  `a734dadec8f8ce9b`, the backend of record (§3.2).
- Twelve sham sessions, form-major: F-0, F-a, F-b, F-c, each over A1s, A2s and A3s. Below, **Sk** is the raw's
  `SMOKE SESSION k/12` and the output `{k:02d}_{form}_{template}.json`. All twelve ran, with G-VER clean in each. No
  driver refusal fired, and the wrapper printed `EXIT=0`.
- Two sessions were excluded, both on a `lexical` claim in a free round, and both are counted here (§3.4: excluded
  sessions included). S4 (F-a A1s) was excluded at round 10 and is complete. S10 (F-c A1s) was excluded at round 5 and
  ended there, so it has 5 rounds and 1 reasoning line.

**Committed with this read** (byte identities in the entry):
- `results/raw/2026-11-09_a-m2-smoke.txt`: the raw, 1,047 lines, with every reasoning line and every response.
  Lines 4 (INVOCATION) and 6 (SNAPSHOT) are scrubbed of local paths (`<repo>`, `<tmp>`, `<home>`), as the header
  already was by the wrapper; no other byte changes.
- `results/raw/2026-11-09_a-m2-smoke_{01_F-0_A1s … 12_F-c_A3s, summary}.json`: the driver's thirteen outputs,
  byte-identical. They hold no local path.

## 1. The driver's computation, verbatim (the raw's last seven lines)

```text
SMOKE TALLY F-0: sessions 3 (valid 3, complete 3); lines 18; echo 3, empty 0, cap 0, union 3; counter (a) 5; task responses 30 (free 18)
SMOKE TALLY F-a: sessions 3 (valid 2, complete 3); lines 18; echo 5, empty 0, cap 1, union 6; counter (a) 11; task responses 30 (free 18)
SMOKE TALLY F-b: sessions 3 (valid 3, complete 3); lines 18; echo 0, empty 0, cap 3, union 3; counter (a) 0; task responses 30 (free 18)
SMOKE TALLY F-c: sessions 3 (valid 2, complete 2); lines 13; echo 2, empty 0, cap 0, union 2; counter (a) 2; task responses 25 (free 13)
SMOKE RULE (A-m2 v0.3 §3.3: (i) the union of empty, cap-reach and echo lines; ties by (ii), counter (a); then F-a before F-b; selectable F-a and F-b, F-0 the control, F-c a diagnostic arm): keys (i, ii, departure) {'F-a': [6, 11, 0], 'F-b': [3, 0, 1]}; selected: F-b; tied with it on (i) and (ii): none
SMOKE STOPS (A-m2 v0.3 §3.3): F-0 below 3 defect lines: no; the selected form at 3 or more: FIRES; adopted: none
EXIT=0
```

## 2. Code's cross-check

Before reading the raw, Code ran `read_aid.py` (Appendix A, verbatim; standard library only, reading the thirteen
JSONs). It re-tallies every form from the session JSONs, re-applies §3.3's rule to the re-tally, and compares both
with `summary.json`. The first eight lines of its output follow, verbatim. In the full output a per-session listing of
every round and line comes next, and it re-lists what the raw holds.

```text
FILES ['01_F-0_A1s.json', '02_F-0_A2s.json', '03_F-0_A3s.json', '04_F-a_A1s.json', '05_F-a_A2s.json', '06_F-a_A3s.json', '07_F-b_A1s.json', '08_F-b_A2s.json', '09_F-b_A3s.json', '10_F-c_A1s.json', '11_F-c_A2s.json', '12_F-c_A3s.json', 'summary.json']
RE-TALLY equals summary.json's tally: True
RE-RULE: {'selected': 'F-b', 'keys': {'F-a': [6, 11, 0], 'F-b': [3, 0, 1]}, 'stop_uninformative': False, 'stop_selected_defects': True, 'adopted': None}
RE-RULE equals summary.json's selection: True ; i_key union
  F-0: lines 18, (i) 3 (echo 3, empty 0, cap 0), (ii) 5, sessions 3 (valid 3, complete 3), responses 30 (free 18)
  F-a: lines 18, (i) 6 (echo 5, empty 0, cap 1), (ii) 11, sessions 3 (valid 2, complete 3), responses 30 (free 18)
  F-b: lines 18, (i) 3 (echo 0, empty 0, cap 3), (ii) 0, sessions 3 (valid 3, complete 3), responses 30 (free 18)
  F-c: lines 13, (i) 2 (echo 2, empty 0, cap 0), (ii) 2, sessions 3 (valid 2, complete 2), responses 25 (free 13)
```

`summary.json`'s `tied_on_i_ii` is `[]`, its `i_key` is `union`, and its `selectable` is `['F-a', 'F-b']`. The
driver's printed lines (§1) carry the same numbers.

## 3. The rule's choice, stated (A-m2 v0.3 §3.3)

- **(i)**, the bar's numerator (the union of empty, cap reached without a newline, and echo under §1):
  - F-0: 3 (echo 3).
  - F-a: 6 (echo 5, cap 1).
  - F-b: 3 (cap 3).
  - F-c: 2 (echo 2).
  - No form has an empty line.
- **(ii)**, counter (a): F-0 5, F-a 11, F-b 0, F-c 2.
- **Selection** among the selectable forms, F-a and F-b, by fewest (i): **F-b**, with 3 against F-a's 6. There is no
  tie on (i), so neither (ii) nor the departure order is reached.
- **The first stop** (F-0 below 3 defect lines: the smoke uninformative) **does not fire.** F-0 shows 3, at the
  threshold.
- **The second stop** (the selected form at 3 or more of its ≤ 18 lines) **fires.** F-b shows 3 of 18.
- **So:** "no change is made and the seat re-specifies again before any re-run" (§3.3). **Adopted: none.** §4's
  form is not set by this smoke, and §6 item 4 does not start.

## 4. The (i) lines, by form, session and line (14)

```text
S2 F-0 A2s line 5: echo (n_tok 5, stop newline): '=== Config evaluation session ==='
S2 F-0 A2s line 6: echo (n_tok 5, stop newline): '=== Config evaluation session ==='
S2 F-0 A2s line 10: echo (n_tok 5, stop newline): '=== Config evaluation session ==='
S4 F-a A1s line 5: echo (n_tok 6, stop newline): '=== Config evaluation session ==='
S4 F-a A1s line 7: echo (n_tok 5, stop newline): '=== Config evaluation session ==='
S4 F-a A1s line 9: cap_no_newline (n_tok 60, stop cap): 'Based on the performance in the previous rounds, both ridge and saddle have provided correct answers. However, the system instructions explicitly state to "Prefer clean task text," and both configs are noted to present clean task text. Since saddle was chosen in the immediately preceding rounds (7 and 8)'
S4 F-a A1s line 10: echo (n_tok 6, stop newline): '=== Config evaluation session ==='
S5 F-a A2s line 5: echo (n_tok 6, stop newline): '=== Config evaluation session ==='
S5 F-a A2s line 6: echo (n_tok 5, stop newline): '=== Config evaluation session ==='
S7 F-b A1s line 9: cap_no_newline (n_tok 60, stop cap): 'geometry (triangle sides), arithmetic (11+33, 31+4, 90-45), opposites (hot/cold), and general knowledge (wheels on bicycle) tasks have been handled perfectly by ridge (6/6), while saddle has only completed two'
S8 F-b A2s line 5: cap_no_newline (n_tok 60, stop cap): 'prism got 2/2 correct and slate got 2/2 correct. Both are perfect. Let\'s compare task cleanliness: prism had "State the number of sides of a triangle." and "State the task text exactly as given." (wait, no, round 2 task was "State'
S8 F-b A2s line 10: cap_no_newline (n_tok 60, stop cap): "prism has 4/4 correct and slate has 4/4 correct. Wait, let's recount. Prism rounds: 1,5,6,7 (4 rounds). Slate rounds: 3,4,8,9 (4 rounds). Both have 4/4 correct"
S12 F-c A3s line 8: echo (n_tok 5, stop newline): '=== Config evaluation session ==='
S12 F-c A3s line 10: echo (n_tok 5, stop newline): '=== Config evaluation session ==='
```

## 5. The counter (a) lines (18; descriptive, §3.4)

Each line's `contains` (it contains a complete harness-written line of the session) and `frame` (it keeps the
banner's `=== … ===` frame; the driver's test is the pattern `=== .+? ===`), as the driver wrote them:

```text
S2 F-0 A2s line 5: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S2 F-0 A2s line 6: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S2 F-0 A2s line 7: contains False, frame True; in (i): False: '=== Config `prism` evaluation session ==='
S2 F-0 A2s line 8: contains False, frame True; in (i): False: '=== Config `prism` evaluation session ==='
S2 F-0 A2s line 10: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S4 F-a A1s line 5: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S4 F-a A1s line 7: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S4 F-a A1s line 8: contains False, frame True; in (i): False: '=== Config the config evaluation session ==='
S4 F-a A1s line 10: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S5 F-a A2s line 5: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S5 F-a A2s line 6: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S6 F-a A3s line 6: contains True, frame False; in (i): False: '[Please provide reasoning for `[round 6 | reasoning]`]'
S6 F-a A3s line 7: contains True, frame False; in (i): False: '[Please provide reliable reasoning for `[round 7 | reasoning]` based on the performance of the configs in the previous rounds]'
S6 F-a A3s line 8: contains True, frame False; in (i): False: "[Please provide reliable reasoning for `[round 7 | reasoning]` based on `prism`'s correct answers to all its tasks so far]"
S6 F-a A3s line 9: contains True, frame False; in (i): False: '[Please provide reasoning for `[round 9 | reasoning]` based on格式错误'
S6 F-a A3s line 10: contains True, frame False; in (i): False: "[Please to provide the reasoning for `[round 9 | reasoning]` to `slate`'s correct answer]"
S12 F-c A3s line 8: contains True, frame True; in (i): True: '=== Config evaluation session ==='
S12 F-c A3s line 10: contains True, frame True; in (i): True: '=== Config evaluation session ==='
```

## 6. Counter (b): Code's declared read (§3.4)

**Domain.** Every task response of the twelve sessions, excluded ones included: 115 in all (30, 30, 30 and 25 by
form). (b) counts responses that no audit class claims and that attempt no task. In §3.4's words, "any answer attempt,
correct, wrong, partial or to another item, is not (b)". The seat confirms or corrects each item.

**(b): 2 responses. F-0 1, F-a 1, F-b 0, F-c 0. Both are free rounds; no forced round is (b).**

```text
S3 F-0 A3s round 7 (free, P, item 5; claim None; stop newline, n_tok 13)
    task:     "Write the opposite of 'hot'."
    response: 'Based on the performance history and logical deduction regarding the configurations:'
S6 F-a A3s round 8 (free, P, item 10; claim None; stop newline, n_tok 2)
    task:     'State the number of wheels on a bicycle.'
    response: 'Perfect.'
```

1. **S3 round 7: (b).** A preamble to reasoning about the choice, which ends at a colon and answers nothing. It is A3s
   round 8's kind at G-TIME-F3 (§2).
2. **S6 round 8: (b), on Code's reading.** "Perfect." does not attempt the task, so it is no answer to the bicycle
   question. It is also none of §3.4's named kinds word for word. Code reads it as an evaluative remark on the
   session, nearest to "a description of the session or its configs". The session's reasoning line at round 8, just
   before this response, ends "based on `prism`'s correct answers to all its tasks so far]". The seat confirms or
   corrects.

**Considered, and read as not (b).** These are answer attempts under §3.4's sentence. Each is listed because it is
malformed or partly off-task, so that the seat can confirm or correct the reading:

```text
S2 F-0 A2s round 8 (free, P, item 9; claim None; stop newline, n_tok 4)
    task:     'Compute 90 minus 45.'
    response: 'and 45'
S4 F-a A1s round 9 (free, Q, item 7; claim None; stop newline, n_tok 5)
    task:     'State which is heavier: a kilogram of iron or half a kilogram of feathers.'
    response: 'A kilogram of trick question'
S5 F-a A2s round 3 (forced, Q, item 12; claim None; stop newline, n_tok 16)
    task:     'Compute 11 + 33.'
    response: 'DAILY ROUTINE : 11 + 33 = 44'
S5 F-a A2s round 4 (forced, Q, item 3; claim None; stop newline, n_tok 12)
    task:     'Compute 60 divided by 5.'
    response: '60 divided by 15 is 12.'
S5 F-a A2s round 10 (free, P, item 6; claim None; stop newline, n_tok 3)
    task:     'Compute 14 times 2.'
    response: '1 direct.'
S10 F-c A1s round 4 (forced, Q, item 3; claim None; stop newline, n_tok 28)
    task:     'Compute 60 divided by 5.'
    response: '60 divided by  after 4 rounds of evaluation, after 4 rounds of evaluation, after 60 divided by 5.'
S12 F-c A3s round 3 (forced, Q, item 12; claim None; stop newline, n_tok 6)
    task:     'Compute 11 + 33.'
    response: '11 + 3assistant'
S12 F-c A3s round 7 (free, P, item 9; claim None; stop newline, n_tok 6)
    task:     'Compute 90 minus 45.'
    response: '90 minus 44'
```

- **S2 round 8** (`'and 45'`): it contains 45, the task's result, which is also its second operand.
- **S4 round 9** (`'A kilogram of trick question'`): a partial answer, which begins the right one.
- **S5 round 3** (`'DAILY ROUTINE : 11 + 33 = 44'`): a correct answer behind a header-like prefix. The answer
  governs.
- **S5 round 4** (`'60 divided by 15 is 12.'`): the right result, with a misquoted operand.
- **S5 round 10** (`'1 direct.'`): Code reads the leading numeral as a wrong answer, or as the start of a
  restatement ("14 times 2", as S5 restates its tasks in rounds 4, 5 and 7). Either reading is an attempt. This is the
  weakest reading of the eight. If the seat reads it as no attempt, it is (b) and fits none of the named kinds.
- **S10 round 4**: a restatement of the computation, unfinished, with "after 4 rounds of evaluation" repeated (the
  banner's Note says "after the first four rounds"). Code reads it as a partial attempt. Its session phrase is the
  nearest thing in the eight to "a description of the session".
- **S12 round 3** (`'11 + 3assistant'`): an unfinished restatement, then the role word "assistant". The driver
  records scaffold `[]` and claim None.
- **S12 round 7** (`'90 minus 44'`): a restatement with a wrong operand and no result. Read as a wrong attempt. S2's
  reasoning line 9 is `'Task: Compute 90 minus 44.'`.

Plainly wrong or loose answers are not listed: S6 round 4 (`'64'` to "Compute 60 divided by 5."), S7 round 10
(`'31'` to "Compute 14 times 2."), S12 round 4 (`'60 divided by 12'`) and S12 round 9 (`'close'`).

**Claimed by an audit class, so outside (b) by its definition.** These are listed for completeness; they are every
claimed response of the smoke:

```text
S4 F-a A1s round 10 (free, P, item 5; claim lexical; stop cap, n_tok 60)
    task:     "Write the opposite of 'hot'."
    response: 'Based on the performance in the previous rounds, both ridge and saddle have provided correct answers. However, the system instructions explicitly state to "Prefer clean task text," and both configs are noted to present clean task text. Since saddle was chosen in the immediately preceding rounds (7 and 8)'
S10 F-c A1s round 5 (free, P, item 0; claim lexical; stop newline, n_tok 10)
    task:     'Compute 31 + 46.'
    response: '31 + 4 configs: ridge, saddle'
S11 F-c A2s round 8 (free, P, item 5; claim v2; stop cap, n_tok 60)
    task:     "Write the opposite of 'hot'."
    response: 'Based on the evaluation session, both `prism` and `slate` have demonstrated 100% accuracy on the four previous rounds (simple facts and arithmetic). The prompt instructions explicitly state to "Prefer the config whose rounds have presented fewer corrupted characters." Since there are no visible'
```

- **S4 round 10** is round 9's reasoning line again, word for word, up to the cap. It is the session's exclusion
  (`lexical:ridge`).
- **S10 round 5** is the session's exclusion (`lexical:ridge`), and the session ends there.
- **S11 round 8** is reasoning about the choice, at the cap, claimed `v2`. The session stays valid.

## 7. Observations (post-hoc and descriptive; under rule 11 they decide nothing, and could license a pre-registration, never a verdict)

1. **F-b's three (i) lines are all cap-reach. It has no echo, and counter (a) is 0.**
   - Each of its 18 lines is prose about the two configs.
   - Its lines' token counts, in session and line order: [48, 50, 57, 59, 60, 53, 60, 30, 44, 23, 57, 60, 59, 53, 54, 38, 40, 44].
   - Besides the three at the cap, four lines ended at a newline within three tokens of it: S7 lines 7 and 8 (57 and
     59), S8 line 9 (57) and S9 line 5 (59).
   - By comparison, the longest line elsewhere runs 12 tokens in F-0 and 52 in F-c.
     In F-a it is S4 line 9, at the cap; the next longest runs 37.
2. **Three F-b lines end mid-sentence at a newline the model wrote:** S8 lines 6, 7 and 8, at 30, 44 and 23 tokens,
   stop `newline`. The class's member is "cap reached without a newline", so they are not (i) as written.
   - Line 6 ends `'prism had "State the number of'`.
   - Line 7 ends `'prism had "State the number of sides of a triangle.", "State the number of'`.
   - Line 8 is `'prissing has 5/5 correct and prissing has 5/5 correct. Both are perfect. Let'` ("prism" garbled).
3. **Lines in neither (i) nor (a)** (Code's grouping):
   - **Header-like lines the harness had not written when the line was generated,** and so outside §1's domain
     (6 lines: F-0 2, F-c 4). S1 line 6 is no header the harness writes:
     - S1 lines 5 and 6: `'[round 5 | choice]'`, `'[round rounds 6–10 | choice]'`;
     - S10 line 5 and S12 line 5: `'[round 6 | reasoning]'`;
     - S12 lines 7 and 9: `'[round 7 | choice]'`, `'[round 9 | choice]'`.
   - **`'...'`:** S3 lines 5, 6, 8, 9 and 10 (F-0 A3s; five of its six lines).
   - **`'==='`:** S11 lines 5 to 8 and 10 (F-c A2s; five of its six). The frame pattern needs text between two
     markers, so a bare `===` does not keep the frame.
   - **Others that give no reasoning:**
     - S2 line 9, `'Task: Compute 90 minus 44.'`: a task line the harness never wrote;
     - S4 line 6, `'Config choice (one word):'`: the choice line's label with no pick;
     - S6 line 5, `'[Please provide reasoning for which config to choose for rounds 5, 6, and 7]'`;
     - S3 line 7, `'Q: What is the main difference between the two configs?'`.
4. **F-a A3s (S6) wrote a bracketed request in all six of its lines.** Five contain a round header and are (a). Line 9
   breaks off into Chinese, `'格式错误'` ("format error").
5. **In F-a A2s (S5), lines 7 to 10 say slate's outputs were corrupted or wrong.**
   - Line 8, for example: `'prism has consistently provided accurate and clean responses in all its rounds, whereas slate produced corrupted text and calculation errors.'`.
   - The task texts at slate's rounds 3 and 4 were clean (`'Compute 11 + 33.'`, `'Compute 60 divided by 5.'`). The
     model's own responses there were `'DAILY ROUTINE : 11 + 33 = 44'` and `'60 divided by 15 is 12.'`.
6. **Reasoning that misstates the record,** for example:
   - S9 lines 5 and 6 (F-b A3s) name "the next task", and lines 7 and 8 "the task", as division, subtraction, division
     and division. No such task comes.
   - S8 line 5 misquotes round 2's task.
   - S7 line 9 credits ridge with "11+33" (saddle's round 3), and gives round 5's task as "31+4" (it was 31 + 46).
   - S8 line 10 counts prism's rounds as "1,5,6,7 (4 rounds)"; prism ran rounds 1, 2, 5, 6 and 7.
   - S9 line 10 gives "Prism 5/5"; prism had run six rounds (1, 2, 5, 6, 8 and 9).
   - S11 line 9 says "both configurations have demonstrated 100% accuracy on the previous tasks"; prism's round 8
     response was the claimed `v2` text, not an answer.

   S7 line 10's "I met with ridge" is garbled wording, and its figures match the record.
7. **Runtime.**
   - Session seconds by form: F-0 800.3, F-a 2,196.4, F-b 4,239.9 and F-c 1,024.1.
   - The total is 8,260.7 s, about 138 min. §3.2 estimated "≈ 50 min of generation at the stage's observed
     rate".
   - Each F-b session ran 1,294.5 to 1,621.5 s.
8. **Choice reads,** as printed per read in the raw:
   - `low_label_mass` is True in 4/18 reads (F-0), 2/18 (F-a), 1/18 (F-b) and 2/13 (F-c).
   - `top1_not_label` is True in 6, 7, 2 and 3 of them.
   - Code draws nothing from these.
9. **F-0 against the stage.** G-TIME-F3's sham lines held the banner verbatim 9 times in 13 (A2s five of six, A3s
   four of six; §0.1). The smoke's F-0 is a fresh draw on the same cells (§3.2). It holds the banner 3 times in 18,
   all in A2s (S2), and its A3s session (S3) wrote `'...'` five times instead.

## 8. Processes during the window (the launch to the end)

- **Code's own:** no Python process. There was only a zsh wait loop (`pgrep`, `sleep`) and shell reads of the raw
  and the output directory.
- **Other sessions:** by their own accounts, relayed by the coordinating session (Code did not check them).
  Neither session ran a model process.
  - **The pod session.**
    - **Which list.** The coordinating session first passed the pod session's list verbatim (v1, written 18:54:31Z,
      sha256 `2a2d442a…9c2c`). It then passed v2 (sha256 `b2c2424d…10f0`, a hash it checked), which supersedes v1 and
      brackets each run by its own transcript stamps. v2 corrects three points: the values-check subagent's end time, a
      count and times for that subagent's runs, and one run's duration. Code states v2.
    - **Every run was model-free,** with no model and no tokenizer.
    - **No Python ran from the launch to 18:22:35Z.**
    - **Its main session:** 14 calls and 16 processes, 18:23:04.964Z–18:52:19.663Z, all plain `python3` (miniconda
      base), un-niced. They read its G-TIME-OLMo (p) reports and reads, assembled its raw, tabulated the reads,
      checked bindings, applied its values-check's fixes, scrubbed a raw, inserted its RESULTS.md entry, and made two
      memory edits.
    - **Its blind values-check subagent:** 20 calls and 23 processes, 18:28:28.518Z–18:50:51.251Z.
      - 22 were plain `python3`, un-niced: JSON, hash and text checks.
      - 1 was `nice -n 19 jlens-qwen36/.venv/bin/python -B -`, 18:36:28.566Z–18:36:29.032Z. It imported
        `valence_core.m.resume` to recompute a backend identifier from its raw.
    - **After 18:52:19.663Z,** no Python ran until the relay of the smoke's end. The coordinating session adds that the
      pod session was idle from 18:54:43Z.
  - **The coordinating session:** no Python in the window. Its calls were `date -u`, `ps`, a heredoc to a memory
    file, two runpod API reads, session reads, `git`, `grep`, `sed` and `shasum`.
- **Git:** one commit came after the launch, the pod session's `2258c52`, its G-TIME-OLMo (p) entry. HEAD at the launch
  was `0afd842`. The commit touches `RESULTS.md`, files under `data/p/` and three `results/raw/2026-11-09_p-gtime*`
  files. None of them is a file named by the raw's GATE, LICENCE or A-M2 lines.

## 9. STOP for the seat (§3.3)

The rule's second stop fired: the selected form, F-b, shows 3 defect lines of its 18. Per §3.3, no change is made,
and the seat re-specifies again before any re-run. Asked of the seat:
1. Read every reasoning line and response of the twelve sessions (the committed raw), and confirm the rule's
   computation in a raw.
2. Confirm or correct each (b) item in §6, including the eight read as not (b).
3. Re-specify (§3.3).

Nothing of §4 or of §6 item 4 starts. Nothing is pushed.

## Appendix A: `read_aid.py`, verbatim

```python
"""Code's read aid for the A-m2 smoke (run after the smoke ends; model-free, standard library only).

1. Re-tallies every form from the twelve session JSONs (each reasoning line's classes and (a) flag as the driver wrote
   them; the rounds from the record) and checks the result equals summary.json's tally, key by key.
2. Re-applies A-m2 v0.3 §3.3's rule to that re-tally (fewest (i) among F-a and F-b, ties by (ii), then F-a before F-b;
   the two stops at 3 defect lines) and checks it equals summary.json's selection.
3. Lists, per session, every task response with its round, phase, role, item and audit claim (the (b) read's input:
   §3.4 (b) is drawn from responses no audit class claims), and every reasoning line with its classes and (a).

Usage: python3 -I read_aid.py OUT_DIR > listing.txt
"""
import json
import sys
from pathlib import Path

FORMS = ("F-0", "F-a", "F-b", "F-c")
TEMPLATES = ("A1s", "A2s", "A3s")
SELECTABLE = ("F-a", "F-b")
STOP_DEFECTS = 3

out = Path(sys.argv[1])
names = sorted(p.name for p in out.iterdir())
want = [f"{k:02d}_{f}_{t}.json" for k, (f, t) in enumerate(((f, t) for f in FORMS for t in TEMPLATES), 1)]
print("FILES", names)
assert names == sorted(want + ["summary.json"]), ("unexpected file set", names)

summary = json.loads((out / "summary.json").read_text(encoding="utf-8"))
tally = {f: {"sessions": 0, "valid": 0, "complete": 0, "lines": 0, "echo": 0, "empty": 0, "cap": 0, "union": 0,
             "counter_a": 0, "responses": 0, "free_responses": 0} for f in FORMS}
listing = []
for name in want:
    d = json.loads((out / name).read_text(encoding="utf-8"))
    rec, lines = d["record"], d["lines"]
    assert d["g_ver"] == [] and d["lines_error"] is None, (name, d["g_ver"], d["lines_error"])
    f = d["form"]
    x = tally[f]
    x["sessions"] += 1
    x["valid"] += int(not rec["excluded"])
    x["complete"] += int(bool(rec["complete"]))
    for r in lines:
        x["lines"] += 1
        x["echo"] += int("echo" in r["classes"])
        x["empty"] += int("empty" in r["classes"])
        x["cap"] += int("cap_no_newline" in r["classes"])
        x["union"] += int(bool(r["classes"]))
        x["counter_a"] += int(r["counter_a"])
    x["responses"] += len(rec["rounds"])
    x["free_responses"] += sum(r["phase"] == "free" for r in rec["rounds"])
    exc = rec.get("exclusion") or {}
    listing.append(f"\n## {name}: {f} {rec['template']}; "
                   f"{'excluded ' + str(exc.get('class')) + '@' + str(exc.get('phase')) if rec['excluded'] else 'valid'}; "
                   f"complete {rec['complete']}; rounds {len(rec['rounds'])}; lines {len(lines)}; choices {len(rec['choices'])}")
    for r in rec["rounds"]:
        a = r["audit"]
        listing.append(f"  R{r['n']:>2} {r['phase']:<6} {r['role']:<8} item {r['item']!s:<6} claim {a['claim']!s:<8} "
                       f"{r['stop_reason']}: {r['text']!r}")
    for r in lines:
        listing.append(f"  L{r['n']:>2} classes {r['classes']} (a) {r['counter_a']}: {r['text']!r}")

ok_tally = tally == summary["tally"]
print("RE-TALLY equals summary.json's tally:", ok_tally)
if not ok_tally:
    for f in FORMS:
        if tally[f] != summary["tally"][f]:
            print("  differs", f, tally[f], summary["tally"][f])


def key(f):
    return (tally[f]["union"], tally[f]["counter_a"], SELECTABLE.index(f))


sel = min(SELECTABLE, key=key)
stop1 = tally["F-0"]["union"] < STOP_DEFECTS
stop2 = tally[sel]["union"] >= STOP_DEFECTS
mine = {"selected": sel, "keys": {f: list(key(f)) for f in SELECTABLE}, "stop_uninformative": stop1,
        "stop_selected_defects": stop2, "adopted": None if (stop1 or stop2) else sel}
print("RE-RULE:", mine)
print("RE-RULE equals summary.json's selection:", mine == summary["selection"], "; i_key", summary["i_key"])
for f in FORMS:
    x = tally[f]
    print(f"  {f}: lines {x['lines']}, (i) {x['union']} (echo {x['echo']}, empty {x['empty']}, cap {x['cap']}), "
          f"(ii) {x['counter_a']}, sessions {x['sessions']} (valid {x['valid']}, complete {x['complete']}), "
          f"responses {x['responses']} (free {x['free_responses']})")
print("\n".join(listing))
```
