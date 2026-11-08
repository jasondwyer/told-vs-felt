# LOCK-m-F3.md — v0.1 (Q-F3's first lock, PROPOSAL-m v1.11 §3.2 m:292, §8 step 19 m:361)

## 0. Header and status

- **Version** v0.1, 2026-11-07. This is Q-F3's first lock under `PROPOSAL-m-gating-campaign-v1_11.md` (m:292; entry
  name `LOCK-m-F3 v0.1`). The proposal's sha256 and every hash a stage's licence checks are in §1, except this
  file's own sha256, which its entry names. The lexicons', the schedule files' and the banner bytes' sha256 are in
  §3, §4 and §6.
- **Drafted and committed by Code on the PI's word.** The PI's routing of 2026-11-07, item 1, as the coordinating
  session relayed it and as quoted at RESULTS.md@139635f:79–81: "1. G-ANL-F3: hygiene commit (N9, N12) → G-SHAPE-F0/F3
  re-runs → canonical `ganl` → LOCK-m-F3 v0.1 → G-TIME-F3 [go]; N10 m:312 stands [confirmed]; N13 no change
  [confirmed]." The seat's answers of 2026-11-07, §9 item 1: "LOCK-m-F3 v0.1 (naming the analyzer, the lexicons, the
  re-run G-SHAPE-F3)".
- **m:292's list, and where each item is in this lock:**

  | m:292 | here |
  |---|---|
  | Q-F3's schedules and interleave rule | §4 |
  | keys | §5 |
  | the F3 verifier | §6 |
  | banner and reasoning-block bytes | §6 |
  | module homes | §5 |
  | the reasoning-line classes | §7 |
  | G-SHAPE-F3's result | §2 |
  | G-ANL-F3's analyzer and lexicon hashes | §1, §3 |
  | every bar of its later stages with class, unit, p0, α, domain and cadence | §8 |

- **What it binds:** Q-F3's stages from G-TIME-F3 to LOCK-m-F3 v0.2 (m:293–296). They are G-TIME-F3, the cap fixed
  by its trigger, and G-ID-F3. Each non-stub mf3 stage checks the licence of §1 at its start
  (`valence_core/mf3/stages.py`, `licence_problems`). LOCK-m-F3 v0.2 records the cap, the path and the projections
  (m:296). G-F3, G-VER, G-PWR and LOCK-m-F3 v1.0 with D2 follow (m:297–298).
- **Code's readings declared here** (§9, and N10's condition in §3) are each a flag the seat may strike until
  LOCK-m-F3 v1.0, "at the cost Code states" (the F3 prebuild answers, line 50). Striking one moves the hash of its
  site's file. That is the analyzer's or mf3's package, both named here, or the driver's (F57's site,
  `scripts/mf3_sessions.py`), which this lock does not name. N10's condition has no site: striking it means building
  the count, an analyzer change, which moves the analyzer's hash.

## 1. Binding identity and the licence by file

- The tables and the verbatim blocks in §1–§9 were generated with a tool at the lock's HEAD (`lockgen.py`, Code's
  scratch), with one exception: the N10 quotation in §3, which Code typed, verbatim from the seat's answer. Nothing
  generated is transcribed by hand. The dated notes, and the counts and abbreviated hashes in the prose of §2, §3
  and §10, are Code's text, taken from the sources they cite. Every file the tables list is committed at HEAD with
  identical working-tree bytes.
- `package_sha256` follows `valence_core.m.resume.package_sha256_of`'s rule, over `valence_core/m/*.py` (m's) and
  `valence_core/mf3/*.py` (mf3's). The closures' sha256 is `scripts/m_analyze.py`'s `closure_sha256` (PIN-1's form).
- **The licence (Q1 (C2)).** Every non-stub mf3 stage checks, at its start:
  - HEAD known;
  - the proposal and this lock committed, with the working tree's bytes;
  - the analyzer's sha256 and mf3's `package_sha256` as computed now;
  - each of the eleven m files below as hashed now;
  - this lock's committed text naming verbatim the analyzer's sha256, mf3's, and the weights' revision and sha256,
    and each m file by path and sha256 on one line;
  - the weights of record, offline (`HF_HUB_OFFLINE` exactly "1", the hub cache's `refs/main` the bound revision, the
    binding recomputed on that snapshot).
- The Q-F3 VERDICTS reader (`scripts/m_analyze.py`, PIN-V2-12) refuses unless this lock names the analyzer's sha256,
  m's `package_sha256` and the Q-F3 closure's sha256.
- **How a stage cites this file** (`valence_core/mf3/stages.py`, `_extra` at :556, its PIN in the docstring; LOCK-m-F0
  v0.1's item of the same name, for Q-F3's keys).
  - A non-stub Q-F3 stage's `identity_extra` carries `lock_file` = `"LOCK-m-F3.md"` and `lock_sha256` = the sha256
    of this file as committed. The `LOCK-m-F3 v0.1` entry names it (a file cannot contain its own hash).
  - The hashes and the weights it carries beside those are this section's tables. `renders_sha16` and
    `reasoning_cap` are in the generated list below. The keys are:
    - `proposal_file` = `"PROPOSAL-m-gating-campaign-v1_11.md"` and `proposal_sha256`;
    - the analyzer's `analyzer_sha256` and mf3's `package_sha256`;
    - `m_module_sha256`, mapping each of the eleven m files to its sha256;
    - `weights_revision` and `weights_sha256`, the WEIGHTS line's;
    - `renders_sha16` and `reasoning_cap`.
  - G-TIME-F3 also carries `locked_path` `"uncached"` (m:293). `_extra` refuses `"cached"` there and any reasoning cap
    but 60. G-ID-F3 carries no `locked_path`: the path is recorded at LOCK-m-F3 v0.2 (m:295–296).
  - At stage start the licence by file (`licence_problems`, :280) checks every key above except `renders_sha16`,
    `reasoning_cap` and `locked_path`.
    - `renders_sha16` is checked against the renders of record built at stage start (`_renders_of_record`, :619).
    - `reasoning_cap` is checked by `_extra`: 60 at G-TIME-F3, and 60 or 120 from G-ID-F3 on. From G-ID-F3 on it
      is also checked by `prior_gate` against the cap G-TIME-F3's trigger fixes ("NOT THE FIXED CAP", :466–477).
    - `locked_path` is checked by `_extra`, and against the path this backend's G-ID licence gives (`_locked`,
      :642).
    - None of these three is compared with this file's text.
  - `prior_proposal_sha256s` is **none under this file**. No earlier proposal is re-adopted. G-TIME-F3 takes no
    prior stage. G-ID-F3's and G-F3's prior is G-TIME-F3 (`PRIOR_STAGE`, :397), which runs under this proposal. So a
    stage either omits the key or passes `[]`. Either way the checkpoint's licence records `[]` (`_record_licence`,
    :491), and a resume or re-finish licensed by other values is refused.
  - A driver passes this file's values. The `time` subcommand is wired at its step, after this lock's commit (§11).
    How the subcommand takes the values is that wiring's, and its entry declares it.

#### The binding identity (computed at the lock's HEAD)

| what | path or scope | sha256 |
|---|---|---|
| the proposal of record | `PROPOSAL-m-gating-campaign-v1_11.md` | `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b` |
| ADDENDUM-m1 v0.1 | `ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md` | `ea08322d601011923524021832d27d0ddf57b3e51ee4d88f265985c6c9bf9001` |
| the analyzer (G-ANL-F3) | `scripts/m_analyze.py` | `d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48` |
| m's package | `valence_core/m/*.py` (`resume.package_sha256_of`) | `7756dcf42532b222b50e3bd8f41e2dc20053fa0a7a2b60e033dda559666349bb` |
| the Q-F3 closure (PIN-V2-12) | the base closure plus `LAZY_F3_MODULES`, 22 modules | `d19f336dc69e987b7be0b69d84d32f4a55cc47c8f4728c0f13b0378608cbf039` |
| the base closure | 15 modules | `a3bc7bb9df3d8361bfa803238e61a61a7eef76a6d839540413e53cd7919cb22b` |
| mf3's package | `valence_core/mf3/*.py` | `f30ad5053904ac222a81fa220f142b5f11f4da7965fdb8cdb83cd9b19e786310` |
| G-SHAPE-F3's artifact | `data/mf3/gates/G-SHAPE-F3.json` | `0c9de56e17d0872851f941473933c4811a79e754cfd99ebcdf589ca5f4e91461` |
| G-ANL-F3's artifact | `data/m/gates/G-ANL-F3.json` | `b91a8c672e85f1d493444c6b6388588ab0a646a8c36971320421c9f03aef936c` |
| Q-F3's schedules manifest | `data/mf3/schedules/manifest.json` | `c7b5df4405981cca40d86564828c854f45c65211f2b2e9c138d43fdacd2a3314` |


#### The eleven m files mf3's licence hashes (Q1 (C2) part (b); one line each, as `stages.licence_problems` (f) reads them)

| file | sha256 |
|---|---|
| `valence_core/m/__init__.py` | `b5175bcb6a521ef277de105315dd8d2f637a7b03e5d7baf30406dd83d0db35c4` |
| `valence_core/m/audit.py` | `16d0abb91444af1b86dcdabdca919f8e61ce371055fe9581a96d02eb950e50f6` |
| `valence_core/m/banner.py` | `730442ca354d8d92fe52135d42506cd83cef2d10deb7dfc23d0a1c204a6d170c` |
| `valence_core/m/bars.py` | `e7f028d8a08c70d29b03296276dc292d8a4042a0e20ac8e6f0c70540b91e1d6c` |
| `valence_core/m/corr.py` | `74818109a284d203177bae82170cbfa1f2cec8cbd85dfa2f7db018530eb27fce` |
| `valence_core/m/guard.py` | `6aa5ac2dc7a7e071ad848053aa1a7e73c9539d1d5cb6fe1152b0f11e7a4d8b87` |
| `valence_core/m/keys.py` | `a7d5ee3a9cde0deed785df204ae840cb56ee0e1eeefa9192fe1c1b0abb6b3beb` |
| `valence_core/m/readrule.py` | `fca9e7329ec42419ed0eaa658d1a954b68db0e05a93cbb6b3a4502f781737a9e` |
| `valence_core/m/resume.py` | `78f2fc8eb8b3b16ffa39c6dac7022b37dc98d8d002f50390d5c4540f22bf8fb7` |
| `valence_core/m/scaffold.py` | `39d8b32f193c1b0a64705dbb3e5557759f3f046158af85cde31870a53c0921d5` |
| `valence_core/m/schedule.py` | `f262f9e0120bcf6e694c0850b56dc3a19ab3c931b28ba92d47009f9f49a72d0d` |


#### The weights of record (Q6; `stages.licence_problems` (g))

- WEIGHTS mlx-community/Qwen3.6-27B-4bit revision c000ac2c2057d94be3fa931000c31723aac53282 sha256 03922eed43c73bf4af06cf4c51982005d95640dc6f39b57caf604749cf001e26


#### The values a non-stub stage's identity_extra carries beside the hashes above (computed from the code)

- `renders_sha16` `a04f67b0e5105a05`: the renders of record (`scaffold.pool_and_renders`, `m_corr.renders_sha`), as `stages._renders_of_record` builds them at stage start.
- `reasoning_cap` 60 at G-TIME-F3 (`scaffold.REASONING_CAPS` = (60, 120)); from G-ID-F3 on, the cap G-TIME-F3's trigger fixes (3 or more lines at the cap without a newline: 120).
- `locked_path` `"uncached"` at G-TIME-F3. The checkpoint's licence records `analyzer_sha256`, `lock_file`, `m_module_sha256`, `package_sha256`, `prior_proposal_sha256s`, `proposal_file`, `weights_revision`, `weights_sha256` (`stages.LICENCE_KEYS`).


#### The rulings this lock rests on (each file's sha256 and the commit that added it)

| ruling | file | sha256 | committed at |
|---|---|---|---|
| the F3 prebuild answers | `results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md` | `aec58440c8b1774bef1277bd29865b72cd1cc385e6c507e159ab82814fb64df3` | `dc1ffe1` |
| the G-ANL-F3 answers | `results/raw/2026-11-06_ganl-f3_design-to-code_answers.md` | `4edfbb8e3d08844e47a329a951f9c2dd381115f0fd92c8b2b77f2207777ca42e` | `54bbfe5` |
| the G-CAL-OLMo answers | `results/raw/2026-11-06_gcal-olmo_design-to-code_answers.md` | `4c3f57d4ec4c1404026bceb2dc2f07141ef36e3d1af66705a5f383dff148bf82` | `0f35954` |
| the p pre-read answers (the FLAG rulings) | `results/raw/2026-11-07_p-preread_design-to-code_answers.md` | `ab40f470b93a7eae58a9f1552eab17e166d6159c3f0bdac917627fc7385cb08b` | `139635f` |
| the N1 battery answer (order (b)) | `results/raw/2026-11-07_n1-battery_design-to-code_answers.md` | `6b711d946f331201262242dd053d51dbb5447c6403e3d0fc86d853f5d7d5b409` | `f105bdd` |
| ADDENDUM-m1 v0.1 | `ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md` | `ea08322d601011923524021832d27d0ddf57b3e51ee4d88f265985c6c9bf9001` | `f26bc59` |


## 2. G-SHAPE-F3 (m:290): PASS, re-run on `993eba1` (`f9700ba`)

- **The re-run of record:** `python scripts/mf3_sessions.py gshape` on HEAD `993eba1`, after the hygiene commit and
  after G-SHAPE-F0's re-run, as the seat's answers of 2026-11-07 §7 order it. It writes
  `data/mf3/gates/G-SHAPE-F3.json` (sha256 in §1).
- **The result:**
  - Layer A: A1 2,816, A2 1,408 and A3 1,408 placements, 0 fired, coverage exact, every required control firing on
    every placement.
  - Layer R: 8,448 line placements, 0 fired.
  - Layer S: 0 problems.
  - Layer T: 640 joins, 0 failed.
- The superseded artifact (`0f9b7bb9…6e9c`, the BUILD (F3) commit's run) is at
  `data/mf3/gates/G-SHAPE-F3.superseded-2026-11-07.json`. The two differ only in provenance (mf3's package, its
  sources); every result is identical. The entry is at RESULTS.md (`f9700ba`).

## 3. G-ANL-F3 (m:291): the analyzer and the lexicons

- **The analyzer** is `scripts/m_analyze.py`, extended in place at `e0b4f2c` (G-ANL-F3 — BUILD). Its sha256 is in §1.
  It was edited once more in place at `10a2bbb` (the check fix, order (b): the seat's answer of 2026-11-07 on N1, §1,
  at `f105bdd`). That moved its sha256 from the BUILD's `6ec3222b…93d9` to the value in §1 before any lock or
  G-ANL-F3.json named it. m's three OLMo NOT-RUN outputs (`0f35954`) stay bound to `6ec3222b…`, the blob that wrote
  them (PIN-42).
- **The canonical run** wrote `data/m/gates/G-ANL-F3.json` (sha256 in §1; its entry `02dadb3`): the battery
  passes 525/525 and reaches all 538 coverage ids; v1's 2,160 evaluations are unchanged, and the v2 space's 519,480
  tuples are each asserted. A second run to a test directory wrote the same bytes.
- **The lexicons**, frozen here (m:292: "G-ANL-F3's … lexicon hashes"). They are counter (c)'s stage-1 terms, polarity
  terms and window (m:312 (c)), as the analyzer carries them and as the artifact's `g_anl_f3.counter_c` block records
  them. Their sha256 is declared below.

#### Counter (c)'s lexicons (m:312 (c); frozen here; `scripts/m_analyze.py`)

- stage-1 terms (19): `corrupt`, `corrupted`, `corruption`, `garbled`, `garble`, `typo`, `typos`, `misspelled`, `misspelling`, `scrambled`, `jumbled`, `mangled`, `broken`, `clean`, `correct`, `intact`, `fine`, `readable`, `legible`
- negative polarity (8): `corrupt*`, `garbl*`, `typo*`, `misspell*`, `scrambl*`, `jumbl*`, `mangl*`, `broken`
- positive polarity (6): `clean`, `correct*`, `intact`, `fine`, `readable`, `legible`
- window: ±6 tokens
- the lexicons' sha256 (compact sort-keyed JSON of the G-ANL-F3 artifact's `g_anl_f3.counter_c` block, as built by `_g_anl_f3_block`): `1b7d5a01af967d9f7953168dbce3468c562602b9f754069041f32b740d088028`


**Dated note, 2026-11-07 (N10; the seat's ruling: "m:312 stands as pinned; no revision before the lexicons freeze at
LOCK-m-F3 v0.1").** m:312's nearest-term rule, as the scorer applies it (PIN-V2-13), scores a line such as "prism is
clean, slate is corrupted" ambiguous. After punctuation is stripped, slate's nearest polarity term within the window
is "clean", one token back, and "clean" is also prism's nearest term. A shared nearest term makes the line
ambiguous. The battery asserts this case as written (`scripts/m_analyze.py:10513`). It is PIN-V2-13's known
limitation, and the rule stands. The seat's two reporting terms, neither an analyzer change:

- The first term, verbatim (Code's typing; the one verbatim block of §1–§9 not generated):

  > if the scorer's output already records the ambiguity's cause, the "same polarity, shared nearest term"
  > subclass is reported as its own count at Q-F3's VERDICTS

  - The scorer's output (`score_line_c`, `scripts/m_analyze.py:3472`, kept per line in counter (c)'s key items)
    records the line's class and each label's polarity, not which term was nearest.
  - So it records the shared polarity but not the shared term, and no such count is built.
  - This is Code's reading of the condition, and the seat may strike it.
- "the seat's blind read scores such lines by (label, polarity) as m:312 has it."

## 4. Q-F3's schedules and the interleave rule

#### Q-F3's schedule files (`data/mf3/schedules/manifest.json`)

- schema `m-schedules-manifest-v1`; construction: PROPOSAL-m v1.11 m:159-172 (Q-F3); 20 files:

| file | sha256 |
|---|---|
| `Q-F3_campaign_A1.json` | `cfc8df1a11214061206ee4d28a800ef14201c0d7e0aa70b8cb123d75c8846eeb` |
| `Q-F3_campaign_A1s.json` | `f3a0682bf1fead75712f2118f6b21c6ec83d10e2df36222be85528df490caee2` |
| `Q-F3_campaign_A2.json` | `a33df12c2dd1f534a4fff818f329cca5b43304c0fcf6547c7d057c1b31af02cb` |
| `Q-F3_campaign_A2s.json` | `319180e54c7f6e225a88b38186e14b887ed53c92fe5cea8f2baedb91615b4d17` |
| `Q-F3_campaign_A3.json` | `13bd869785f81c7527851bc84fc1226ad3b2fa79e22da54af171cf4e89aee059` |
| `Q-F3_campaign_A3s.json` | `de0826c8b643de64550a57bcaaa0fd1a302f22644ca4b3a6693dcd93035814e2` |
| `Q-F3_id_A2s.json` | `aac9cddf059c8334f9854a41876feda1bf1e860f5d6c7c0be94cda97c0af1740` |
| `Q-F3_id_A3s.json` | `ad5671cb5f1fc685ed992dfd2508afe154a1b48c501836a0a9462879b6fe2fad` |
| `Q-F3_qual_A1.json` | `8e023de668481f1450ea647f62f13c3c3cd08d5e553c410b8ece686c23f9dea0` |
| `Q-F3_qual_A1s.json` | `67acb9581556ba78c28c09e278596807fe89952ad76184aa205e68be0bbdc07b` |
| `Q-F3_qual_A2.json` | `38bcc425d568fcb18f1bc3bb789da35d94163544f81faba58b33d53062555223` |
| `Q-F3_qual_A2s.json` | `a0199a2cac2729b1d36950a303cb39182b64fb1e868d0052aafb88c186560500` |
| `Q-F3_qual_A3.json` | `a07b9a859036d94c956b5a00fca90d473cab5c4a80b9dd1535e80d72170b5eb2` |
| `Q-F3_qual_A3s.json` | `001cef2c96e6924402dd332ae685259e460157dfc7c08579c125655cd69909df` |
| `Q-F3_time_A1.json` | `493e3ae7969f9b9569b59af76976d73593dd3525b75416e1c6b364fb6423c6da` |
| `Q-F3_time_A1s.json` | `0a374318e7083233fa6068b4864de6e3e07f42d151bab2d6d4a3e98d94d7949f` |
| `Q-F3_time_A2.json` | `f857324bbd9d28a15b1364576fde052a2d506a60d7c40a5f0411c7271bad45fe` |
| `Q-F3_time_A2s.json` | `27abc7b2972c265fb79925d086e6573c5521d7b4fbf933124927117c18d50753` |
| `Q-F3_time_A3.json` | `13b1f9d65778cd0ba2626ea5ec50055f607e7d0c41dc826a946888be5979a98d` |
| `Q-F3_time_A3s.json` | `cdd9af288ba07633a2193b49d1e19bc2a7c1dea346e6f5bd64c5b1a5a45fdebe` |


#### The schedules and the interleave rule (`valence_core.mf3.schedule`'s docstring, verbatim)

```text
Q-F3's schedules: campaign balance units, gate-stage schedules, the gate-stage launch order and
the six-arm interleave (PROPOSAL-m v1.11 §2.1 m:159-172; §2.4 m:184-192, m:216-243; §3.2 m:293-297).

The CONSTRUCTION is ``valence_core.m.schedule``'s, imported: ``campaign_cells`` (pair x map x start
x clause, clause only where the TOLD line names labels -- A1/A1s; A2-A3s have no clause factor, so
16 cells), the sixteen-row ``GATE_TABLE`` (m:161-170), ``balance_report``, ``cells_sha256``, the
file layout ``dumps_schedule`` and the launch rule ``_n90_launch``. m's ``campaign_schedule``,
``gate_schedule``, ``interleave`` and file writers refuse Q-F3 (they key on keys.UNITS_BUILT), so
the Q-F3 forms are here, keyed by ``mf3.keys``.

FILES under ``data/mf3/schedules/`` with their own ``manifest.json`` -- ``data/m/schedules/`` and
its manifest are untouched (the seat's Q1). Six campaign files (one per arm), six G-TIME-F3 files
(n 1), two G-ID-F3 files (A2s, A3s; sixteen rows available) and six G-F3 files (A1 4, A1s 8, A2 4,
A2s 8, A3 8, A3s 8; m:297): 20 files plus the manifest.
```


#### The interleave rule and the gate-stage launch order (`valence_core/mf3/schedule.py`: each function's signature, docstring and PIN, verbatim)

`valence_core/mf3/schedule.py:185`:

```python
def gate_launch_order(templates_with_counts: Sequence[tuple[str, int]]) -> list[tuple[str, int]]:
    """(template, j) launch list for a multi-template gate stage: strict rotation in §2.4's table
    order, a template leaving the rotation at its count."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's launch-order PIN carried to six templates --
    # the cross-template order is §2.4's table order (A1, A1s, A2, A2s, A3, A3s; G-ID-F3: A2s, A3s);
    # any other order given is refused, not re-sorted; within a template the table's order (m:159).
```

`valence_core/mf3/schedule.py:205`:

```python
def interleave(arms_in_order: Sequence[str], done: Callable[[str], bool],
               start_counts: Mapping[str, int] | None = None) -> Iterator[str]:
    """The next arm to launch: strict rotation by launch index in §2.4's order (A1, A1s, A2, A2s,
    A3, A3s), an arm at its floor leaving the rotation for good (m:172); ``done`` evaluated lazily
    before each yield."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's interleave PIN carried to six arms -- next = the
    # live arm with the fewest launches, ties to table order (m.schedule._rotation, imported); the
    # resume counts are validated pairwise exactly as Q-F0's two-arm rule (a precedes b in table
    # order: both live -> b <= a <= b + 1; only a live -> a >= b; only b live -> b >= a - 1).
```


## 5. Keys and module homes

#### Keys (`valence_core.mf3.keys`; `stream` is m's)

- templates ('A1', 'A1s', 'A2', 'A2s', 'A3', 'A3s'); contrast ('A1', 'A2', 'A3'); sham ('A1s', 'A2s', 'A3s'); G-ID templates ('A2s', 'A3s').
- items: `m-f3-items|{s}`, gate `m-f3-items-time|{s}` (and `id`, `qual`).
- arm, time: `m-time|A1|{s}`
- arm, id: `m-id|F3|A2s|{s}`
- arm, qual: `m-f3|A1|{s}`
- arm, campaign: `m|A1|{s}`
- schedules: `m-sched|Q-F3|A1|{b}`; gate π `m-sched|Q-F3|time|A1|0`.


#### Module homes (`results/raw/2026-11-06_mf3-build_design.md` §3, verbatim)

- `__init__.py` — scope and the licence.
- `keys.py` — Q-F3's keys (m:159): items `m-f3-items|{s}` / `m-f3-items-{gate}|{s}`; arms `m|{arm}|{s}`, `m-time|{arm}|{s}`, `m-id|F3|{template}|{s}` (A2s, A3s), `m-f3|{template}|{s}`; schedules `m-sched|Q-F3|{arm}|{b}`, `m-sched|Q-F3|{gate}|{template}|0`; `stream` is m's. No Q-F3 key equals a Q-F0 or OLMo key (self-test).
- `banner.py` — the six F3 banners (A1 TOLD-MAP, A1s TOLD-MAP-SHAM, A2/A2s TOLD-OBJ, A3/A3s COMMON only) and the reasoning block, from m's constants; `spec_problems` against the proposal file and §2.4's banner column.
- `schedule.py` — campaign cells and balance units, the sixteen-row gate schedules (clause None on A2–A3s), the clause-free balance check, the six-template launch order and six-arm interleave, the files and manifest.
- `lines.py` — the reasoning line's three classes, its echo set, the Q4 review counter.
- `scaffold.py` — `F3Scaffold` (F2 block order; `reasoning(ci)` draws the line's seed before the menu order), `f3_config`, `F3Log` (the F3 record), the two-form boundary assertion, `prepick_excluded`.
- `runner.py` — `f3_startup` and `run_session_f3`.
- `verify.py` — G-VER for F3.
- `readrule.py` — F3's read rules, printed reasons, session lines and stage report.
- `bars.py` — `F3Bar` (m's `Bar` with Q-F3's vocabulary), the bar table, firing cases, the realised-n evaluation.
- `guard.py` — the cached-path licence (G-ID-F3's artifact at its cap), the static call-site guard (`valence_core.m.guard`'s scanner, subclassed with Q-F3's names), the import-set check, the forbidden-literal scan; m's insulation re-exported.
- `resume.py` — Q-F3's identity (Q-F0's keys + `reasoning_cap`, `m_module_sha256`, `weights_revision`, `weights_sha256`), `load_or_init`, the weights binding and the model of record's hub-cache directory; m's checkpoint machinery re-exported.
- `stages.py` — the gate stages, G-ID-F3, the campaign, the licence, the reports.
- `gshape.py` — G-SHAPE-F3.
- `testing.py` — the test double (self-test only).
- `scripts/mf3_sessions.py` — the driver.


## 6. Banner and reasoning-block bytes; the F3 verifier

#### Banner and reasoning-block bytes (`valence_core.mf3.banner`; m's constants by import)

| constant | bytes | sha256 |
|---|---|---|
| `SESSION_BANNER` | 34 | `6124c724758f61109af42141cd2dd576e2fb4e4b9c781e5a22af8be16a6a30ae` |
| `COMMON` | 89 | `5d915bd852b5d5984f6997623a1dd614cdf336e9518bd55e6d9916f7dffe33b0` |
| `TOLD_MAP`, clause 0 | 134 | `6bfc495be9b72cbfce0d53f952dfdd0969a51c483eefa2dfeeb5abcd54dc89ba` |
| `TOLD_MAP`, clause 1 | 134 | `a6fe3b799dc62012ec5e934a9d7a154c94d5df8fef9b6c1b307eb2661afffae4` |
| `TOLD_MAP_SHAM`, clause 0 | 107 | `5bdf99055b93792ffa5b78962f4e2b1b79569ad4fe93a295ce9ae56f0ec7e3d3` |
| `TOLD_MAP_SHAM`, clause 1 | 107 | `a8b3befdfde53cbc72233564e6d3467abc4806cc092b0073f1fb0e576b198b25` |
| `TOLD_OBJ` | 137 | `a50ca2358a40ec9ff0360489c81b93c0eebf40943a8922d27fc5c16424ce56bb` |
| `REASONING_HEADER` | 23 | `58b8d5553639b13c6e294668e56d3437da36d84d892b03181baf15574e6078b0` |
| `REASONING_LINE` | 21 | `999aca0d3a889c37761366e7a0149b3945566e4004dafd11347c0f651ea39d65` |
| `reasoning_block(5)` | 44 | `f4ea7bcb9d1e1fb715005ab0416fdafe1d2c21644acede391795eed841d9f160` |
| `reasoning_block(6)` | 44 | `5a5d76642c5d98d5d67372bd120876fac2bd35d029d6de9b0c09e31e48e703ef` |
| `reasoning_block(7)` | 44 | `d4ac390283740bb2a3321aa921c07018f4fbfbef2842e26f045128a65d75619f` |
| `reasoning_block(8)` | 44 | `50146ea013f1c48616f5fb487b52c8d95a2d5e474e16e09277a681f5ffc73606` |
| `reasoning_block(9)` | 44 | `2793670756c2335c6393e64bd7b45c2d6af419853494ac02aaaf770646cef94a` |
| `reasoning_block(10)` | 45 | `f024bc11d6c9a4b6adce3138bdc80afab4cd8415c652d976ca5b682015643541` |


#### The F3 verifier (`valence_core.mf3.verify`'s docstring, verbatim)

```text
The F3 verifier -- G-VER for Q-F3 (PROPOSAL-m v1.11 §3.1 m:284, carried by m:298; §3 m:271's
``template_breakage`` and ``schedule_mismatch``; §2.1 m:159; §2.2 m:174; §2.5 m:253).

m:284: "every session's harness bytes reconstructed from its recorded fields, the committed schedule
and the rng streams before any artifact is written". ``verify_session`` rebuilds the session's
scaffold through the SAME code path the runner used (``scaffold.f3_config``) from the record's stage,
template, s, path and reasoning cap and the committed schedule's cell, replays it with the RECORDED
generations, reasoning lines and picks, and compares:

  schedule_mismatch -- the cell, the keys (m:159), the banner bytes and Note lines (§2.5), per round
      the label, role, pole, item, delivered text, property and seed, per reasoning line its seed and
      cap, per choice the menu order -- and the template's role: A2/A2s and A3/A3s carry one banner, so
      a contrast record must have served the corrupted render on its Q role and a sham record clean
      text throughout (Code's PIN, the template name decides, the delivery is asserted);
  template_breakage -- the harness bytes (banner; forced ``seg + text + "\n"``; per free choice the
      reasoning block + line + ``"\n"``, then ``menu + " {pick}\n" + seg + text + "\n"``), the
      pieces, round and menu numbering, each pick against its read (menu_a iff p_a >= p_b, verify KL
      exactly 0.0), each reasoning line's classes and scaffold hits re-derived from its text, and the
      record's own end rules (exclusion, strict scope, hair triggers, domain, first pick, completeness).

It never raises on a malformed record (a failure to report is template_breakage); messages name a
field and a phase, never a label, a pick or a free index.
```


## 7. The reasoning-line classes

#### The reasoning-line classes (`valence_core.mf3.lines`)

- `CLASSES` = ('empty', 'cap_no_newline', 'echo'); the review counter's strings `REVIEW_STRINGS` = ('You are a helpful assistant.', '4assistant', '<|end|>').


#### The reasoning-line classes (`valence_core.mf3.lines`' docstring, verbatim)

```text
The reasoning line's classes (PROPOSAL-m v1.11 §2.6 m:265, §3.2 m:293, §4 m:308, m:312 (f),
m:314; the design seat's prebuild answers of 2026-11-06, Q4 and Q8).

m:265: "The reasoning line is not a round (Q-F3). Scored only by its defect bar, counter (c), and the
`scaffold_absorption` hair trigger (the one hair trigger that reads it and can remove a session from
the primary's domain; the runner ends the session at that fire). Its defect classes: empty line; cap
reached without a newline; reasoning-line echo = a verbatim, whitespace-normalized reproduction of
any complete harness-written line of the session (v1.3's definition). Exempt from v2/v3, the
task-round echo class, lexical, and `earlier`; the frozen ban list applies to its generation."

So nothing here calls the task-round audit: a reasoning line never reaches v2, v3, the task-round
echo class or lexical, and never enters ``earlier`` (the runner's PIN). ``classify_line`` returns its
three defect classes (``reasoning_line_defect``'s numerator is their union, m:293) and its
``scaffold_absorption`` hits, beside the echo's matched line index.

The Q4 counter (the seat's answer: the three strings from Q-F0's VERDICTS read, declared as one
descriptive rule-23 counter, deciding nothing) is ``review_counter``, a pure function of the
records' generated texts, tabulated over all sessions, excluded included.
```


## 8. Bars

Every bar of Q-F3's later stages, generated from `valence_core.mf3.bars.QF3_BARS`. Its arithmetic is
`valence_core.m.bars`', imported unchanged.

#### The bar table (generated from `valence_core.mf3.bars.QF3_BARS`; m:292's class, unit, p0, alpha, domain, cadence)

| # | bar (`name`) | stage | kind | unit | numerator (k) | p0 | α | domain | cadence | planned n / critical | on fire |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `scaffold_absorption` | every | hair_trigger | model generation (a task round or a reasoning line) | generations containing a scaffold-set string | — | — (k ≥ 1) | every | evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271) | — | STOP the stage (m:271) |
| 2 | `template_breakage` | every | hair_trigger | session | sessions failing G-VER | — | — (k ≥ 1) | every | evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271) | — | STOP the stage (m:271) |
| 3 | `schedule_mismatch` | every | hair_trigger | session | sessions differing from the committed schedule | — | — (k ≥ 1) | every | evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271) | — | STOP the stage (m:271) |
| 4 | `round_degeneracy@G-TIME-F3` | time | binomial_stage_end | task round generated (<= 10 per session: 4 forced + 6 free) | rounds claimed by audit v2 or m's harness-echo class (m:261) | 0.05 | 0.05 | sham | once at stage end on the realised n; no mid-stage evaluation (m:271) | 30 / 5 | STOP before G-ID-F3 (m:293; the bars bind alone, m:271) |
| 5 | `reasoning_line_defect@G-TIME-F3` | time | binomial_stage_end | reasoning line generated (<= 6 per session, one per free choice) | reasoning lines with any of m:265's three classes (empty, cap without newline, reasoning-line echo) | 0.10 | 0.05 | sham | once at stage end on the realised n; no mid-stage evaluation (m:271) | 18 / 5 | STOP before G-ID-F3; the seat re-specifies (m:293) |
| 6 | `gid_divergence@G-ID-F3` | id | hair_trigger | complete cached/uncached pair (4 forced rounds + 6 x (reasoning line, read, chosen round) each) | complete pairs whose transcripts differ in any byte | — | — (k ≥ 1) | pairs | per complete pair, uncached first, A2s then A3s; stops at the first divergence (m:281, m:295) | — | G-ID-F3 FAIL: Q-F3 runs uncached (m:295) |
| 7 | `round_degeneracy@G-F3` | qual | binomial_stage_end | task round generated (<= 10 per session: 4 forced + 6 free) | rounds claimed by audit v2 or m's harness-echo class (m:261) | 0.05 | 0.05 | sham | once at stage end on the realised n; no mid-stage evaluation (m:271) | 240 / 19 | STOP: Q-F3 does not run until the seat re-specifies (m:297, m:271) |
| 8 | `reasoning_line_defect@G-F3` | qual | binomial_stage_end | reasoning line generated (<= 6 per session, one per free choice) | reasoning lines with any of m:265's three classes (empty, cap without newline, reasoning-line echo) | 0.10 | 0.05 | sham | once at stage end on the realised n; no mid-stage evaluation (m:271) | 144 / 22 | STOP: Q-F3 does not run until the seat re-specifies (m:297, m:271) |
| 9 | `round_degeneracy@campaign-Q-F3` | campaign | binomial_look | task round generated (<= 10 per session: 4 forced + 6 free) | rounds claimed by audit v2 or m's harness-echo class (m:261) | 0.05 | 0.05 | sham | every 40 launches and at the end, cumulative count, alpha .05 per look, no alpha spending; look index in the resume identity (m:330) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |
| 10 | `reasoning_line_defect@campaign-Q-F3` | campaign | binomial_look | reasoning line generated (<= 6 per session, one per free choice) | reasoning lines with any of m:265's three classes (empty, cap without newline, reasoning-line echo) | 0.10 | 0.05 | sham | every 40 launches and at the end, cumulative count, alpha .05 per look, no alpha spending; look index in the resume identity (m:330) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |
| 11 | `own_pair_lexical@campaign-Q-F3` | campaign | binomial_look | task round generated in A2s / A3s | task rounds claimed lexical under m:261's claiming order, forced and free | 0.02 | 0.05 | lexical_sham | every 40 launches and at the end, cumulative count, alpha .05 per look, no alpha spending; look index in the resume identity (m:330) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |
| 12 | `exclusion_guard_fisher@campaign-Q-F3` | campaign | guard_fisher | session launched in the arm through the look (pre-pick exclusion) | pre-pick exclusions (sessions excluded before their first read: at a forced round or at reasoning line 1, m:308; the seat's Q8) | — | 0.05 | contrast_arm | at every look, per contrast arm (m:316) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |
| 13 | `exclusion_guard_abs@campaign-Q-F3` | campaign | guard_abs | session launched in the arm through the look (pre-pick exclusion) | pre-pick exclusions (sessions excluded before their first read: at a forced round or at reasoning line 1, m:308; the seat's Q8) | 0.20 | 0.05 | contrast_arm | at every look, per contrast arm (m:316) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |


- **Dated note, 2026-11-07: row 6's numerator predates the seat's F-7.**
  - The table generates row 6 from `valence_core/mf3/bars.py:197–202`, last edited at `cd9756e`. Its numerator
    reads "complete pairs whose transcripts differ in any byte".
  - The stage decides G-ID-F3 by the seat's F-7 criterion (`stages._gid_pair`, :1139, the F-7 PIN at :1140;
    `guard.GID_CRITERION`, `guard.py:46–49`). A pair is identical only if its transcripts are byte-identical **and**
    each reasoning line's (n_tok, cap_hit, stop_reason) triple is identical.
  - `gid_decide` (:1106) fails G-ID-F3 on a divergence in any pair, complete or not, and the bar fires on that FAIL.
  - F-7 governs. The row's text is not edited here: an edit to `bars.py` would move mf3's package, which this lock
    names.

## 9. PINs

- **Code's readings, declared at this lock.**
  - Two registers, each verbatim below: the F3 build's (F1 onward, the F3 build design §4) and G-ANL-F3's
    (PIN-V2-1 to PIN-V2-24, its build design §2).
  - N10's condition (§3).
  - The registers' sites are listed after them. F57's is the exception: its site, `scripts/mf3_sessions.py`,
    carries no PIN line.
  - Each reading is strikable by the seat until LOCK-m-F3 v1.0, at the cost stated in §0.
- **The seat's rulings set here** (not Code's readings):
  - F-6 (G-TIME-F3's contrast sessions report no per-line list before VERDICTS; "k of ≤ 36");
  - F-7 (G-ID-F3's identity criterion: m:281's byte-identical transcript pair **and**, per reasoning line, an
    identical (n_tok, cap_hit, stop_reason) triple; "A seat PIN at LOCK-m-F3 v0.1; set before G-ID-F3 has run.");
  - PIN-29's exception by blob (A1);
  - N10's (§3) and N13's (§10) terms.

#### The F3 build's PIN register, verbatim (`results/raw/2026-11-06_mf3-build_design.md` §4)

| # | site | reading |
|---|---|---|
| F1 | `guard.M_MODULES`, `guard.M_HASHED` | L1: the ten modules, the transitive production closure; `ABSENT_MODULES` asserted absent (N1); the licence hashes `M_HASHED`, the ten and m's `__init__.py` (finding 7) |
| F2 | `guard._gid_pass` | the licence is m's form plus `identity.reasoning_cap` equal to the asking cap |
| F3 | `stages.licence_problems` | L2's (a)–(g); (f) names each m file by path and sha256 on one line (finding 8); (g) `HF_HUB_OFFLINE` = "1" and `refs/main` = the bound revision (finding 5) |
| F4 | `stages.ANALYZER_PATH` | the analyzer is `scripts/m_analyze.py`, extended in place by G-ANL-F3 (Q3) |
| F5 | `stages.out_paths` | m's layout under `data/mf3` |
| F6 | `stages.PRIOR_STAGE`, `prior_gate` | G-ID-F3 needs G-TIME-F3 PASS; G-F3 needs G-TIME-F3 PASS and the G-ID-F3 artifact at the run's cap; the campaign needs G-F3 PASS. G-ID-F3 and G-F3 refuse any cap but the one G-TIME-F3's trigger fixes, re-computed from its checkpoint; the campaign refuses any but G-F3's (finding 4) |
| F7 | `stages.gid_artifact_problems` | an artifact at another cap is refused (B7) |
| F8 | `stages._extra` | identity_extra's keys; `reasoning_cap` 60 at G-TIME-F3; the stub's weights binding refused on a non-stub run |
| F9 | `stages._hair_hit` | the fired generation may be a reasoning line (phase "reasoning", its ci) |
| F10 | `stages._line_excerpt` | a line after the first pick lists the previous choice's pick as revealed |
| F11 | `stages.cap_trigger` | m:174's count over all six G-TIME-F3 sessions' lines (Q5); ≥ 3 → 120; applied from G-ID-F3 on (m:294–295), recorded at LOCK v0.2 (m:296) |
| F12 | `stages.gid_decide` | one complete identical pair per template, indices advancing per template (m:281's rule, Q8; N2); a divergence anywhere FAILs |
| F13 | `stages.run_gid_pair_f3` | a G-ID-F3 artifact is never overwritten (B7) |
| F14 | `stages._finish_gid` | G-ID-F3's reads are the full sham-only records (§4 exception (4)) |
| F15 | `stages.campaign_look` | the lexical bar's numerator and the beside counts (B23) |
| F16 | `stages.run_campaign` | an artifact at another cap refuses the campaign (B7) |
| F17 | `stages._campaign_report` | m's pick-free campaign report |
| F18 | `scaffold.f3_config` (path) | G-TIME-F3 uncached; G-ID-F3 both paths |
| F19 | `scaffold.f3_config` (cap) | G-TIME-F3 generates lines at 60; G-ID-F3 on, at the cap G-TIME-F3's trigger fixes (m:294–295; F6) |
| F20 | `scaffold.f3_config` (j) | j = s at gate stages, None in the campaign |
| F21 | `scaffold.assert_boundary` | rule 28(d)(a) in both forms at every generation (Q8; N6) |
| F22 | `F3Log.reasoning_hair` | a line's scaffold fire: hair {phase "reasoning", ci} and exclusion {class "scaffold", phase "reasoning", ci}; strict scope unchanged (Q8) |
| F23 | `F3Log.record` | complete = 4 forced + 6 × (line, read, round) |
| F24 | `scaffold.prepick_excluded` | pre-pick = forced, or reasoning with ci 0 (Q8's pre-pick count; m:308's domain: "up to and including the first reasoning line") |
| F25 | `lines.echo_lines` | the eight strings as rendered for the session + the headers written so far (Q8; N4) |
| F26 | `lines.classify_line` (empty) | ws_norm(text) == ""; with both EOS strings banned a whitespace-only line runs to its cap |
| F27 | `lines.classify_line` (cap) | stop_reason "cap" (Q8: the cap-length prefix kept, cap-reach); a newline as the cap-th token is not cap-reach |
| F28 | `lines.classify_line` (echo) | containment, case-sensitive, ws_norm, first match (Q8) |
| F29 | `lines.review_counter` | the Q4 counter: per (template, kind, string), all sessions; the analyzer tabulates it |
| F30 | `readrule._LINE_RX` | the declared session-line forms |
| F31 | `readrule._check_pieces` | only the last free group may be the reasoning block alone, where the line ended the session |
| F32 | `readrule.strip_contrast` (time) | ruling (h)'s form plus the per-line cap booleans (Q5); the list's length locates a free-phase end (flag F-6) |
| F33 | `readrule.strip_contrast` | a contrast session's free and reasoning hair triggers withheld from the read |
| F34 | `readrule.redact_sham` | both labels redacted in free responses and every reasoning line |
| F35 | `readrule.printed_reason` | a contrast line after the first pick prints `excluded@free`; line 1 `scaffold@reasoning`; at G-TIME-F3 every contrast line `excluded@free` (ruling (h): no class; a reasoning line is excluded only for the scaffold class, so its phase would name it; finding 3) |
| F36 | `readrule._contrast_block_time` | G-TIME-F3's contrast block: s, forced rounds generated, excluded at forced, the per-line cap booleans |
| F37 | `resume.weights_binding` | Q6's binding: the snapshot's revision and the sha256 of its load files' content addresses |
| F38 | `resume.Identity` (paths) | G-ID-F3 "cached+uncached"; G-TIME-F3 "uncached" |
| F39 | `resume.load_or_init` | m's order with Q-F3's identity; no pod id on the laptop |
| F40 | `runner.qwen_ban_list` | runner_qwen's procedure (not importable, N1) |
| F41 | `runner.run_session_f3` (licence) | a cached session outside G-ID-F3 re-reads the licence on this backend at this cap |
| F42 | `runner.run_session_f3` (seconds) | the whole session's wall-clock, to the ms |
| F43 | `schedule.L_MAX_K1` | the k = 1 materialization: A1 4352, A1s 1600, A2 = A3 6384, A2s = A3s 2640 (B21) |
| F44 | `schedule.GATE_PLAN` | G-TIME-F3 1 per arm; G-ID-F3 A2s and A3s, 16 rows each; G-F3 4/8/4/8/8/8 |
| F45 | `schedule.roster` | Q-F3's roster is Qwen's of record via `m.schedule.roster_for("Q-F0")` |
| F46 | `schedule.gate_launch_order` | strict rotation in §2.4's order, a template leaving at its count (B5) |
| F47 | `schedule.interleave` | m's rotation over six arms, the counts validated pairwise |
| F48 | `schedule._file_blobs` | m's manifest form, construction "PROPOSAL-m v1.11 m:159-172 (Q-F3)" |
| F49 | `bars._qf3_bars` | scaffold_absorption's unit is the generation (a round or a line) (B26); G-ID-F3's criterion declared `gid_divergence` |
| F50 | `bars` (G-TIME-F3 line bar) | a fire STOPs; the cap-trigger count is reported, applied by nobody until the seat re-specifies (B17) |
| F51 | `bars.counts` | m's stage_end_eval PIN carried; lines by the union of classes |
| F52 | `bars.no_test` | a gate-stage bar at realised n = 0 is reported as no test and not fired, and the stage ends on its other bars: Code's reading by analogy with m:271's Qwen rule, which says "reported, not fired" of G-TIME-F0's realised n of 2–4 and "on Qwen no such pause exists" of OLMo's G-TIME pause (m:271 says nothing of n = 0); revised on finding 6 from a PAUSE that nothing could lift; silent at a campaign look (B30) |
| F53 | `banner._label` | m's label rule |
| F54 | `verify` (read) | m's read check: menu_a iff p_a >= p_b, KL exactly 0.0 |
| F55 | `verify` (role) | A2/A2s and A3/A3s share a banner: the template name decides the role and the delivery is asserted (B22) |
| F56 | `gshape` (Layers R, T) | additions to "as G-SHAPE-F0": the reasoning line's own placements (Layer R) and the build hazard's declared check on the tokenizer of record (Layer T); §7 (Layer R's scope, finding 11) |
| F57 | `scripts/mf3_sessions.py` | what is wired (selftest, schedules, hashes, gshape) and refused (the four stages); Q6's forms (§8) |
| F58 | `guard._F3CallSiteScan`, `guard.check_call_sites` | `valence_core.m.guard`'s hardened scanner, imported and subclassed: the scanner is inherited, and six methods are overridden, each restating m's with Q-F3's names — the four that bind m's guard module or file (`__init__`, `_flag_licensed_bindings`, `_is_guard_alias`, `_licensed`: mf3's guard the one licensed binding, so Q-F0's licence is unlicensed here, m:267), `in_gid` (`run_gid_pair_f3`'s module-level body the one exemption) and `flag` (m's names in every inherited message); `run_session_f3` guarded; m's whole battery reproduces under `_battery_map` (finding 1) |
| F59 | `stages._gid_pair` (`meta_identical`) | beside m:281's criterion, descriptive only: whether a pair's generations agree in token count, cap flag and stop reason (finding 9; flag F-7) |
| F60 | `readrule._contrast_block` | a contrast template reports its sessions' first reasoning lines (pre-pick) beside its forced rounds, by class, with line-1 exclusions and hair triggers; later lines withheld with the free rounds (m:297, m:271; finding 12) |


- **Dated note, 2026-11-07: three of this register's readings are superseded by the seat's rulings, applied at
  `e0b4f2c`.**
  - The three were Code's readings at the F3 build, put to the seat as flags F-6 and F-7:
    - F32's and F36's per-line cap booleans in G-TIME-F3's contrast reports, built as the seat's Q5 ruled;
    - F59's `meta_identical`, kept as descriptive only.
  - The seat ruled both flags (the G-ANL-F3 answers, F-6 and F-7):
    - a contrast session at G-TIME-F3 reports no per-line list before VERDICTS, and its booleans go to the
      checkpoint. F-6 supersedes the per-line-list part of Q5;
    - G-ID-F3's identity criterion binds the per-line triple.
  - `e0b4f2c` applied them:
    - neither the stripped read (`strip_contrast`, `readrule.py:194`, the seat's F-6 PIN) nor the contrast block
      (`_contrast_block_time`, `readrule.py:471`; Code's PIN at :472, citing F-6) carries a per-line list;
    - `meta_identical` is gone, and the triple binds in `_gid_pair` (`stages.py:1140`, the seat's F-7 PIN).
  - The register is reproduced as written. F32's "plus the per-line cap booleans (Q5); the list's length locates a
    free-phase end (flag F-6)", F36's "the per-line cap booleans" and F59 are not Code's readings at this lock. The
    rest of the register stands.

#### G-ANL-F3's PIN register, verbatim (`results/raw/2026-11-06_ganl-f3_build_design.md` §2)

PIN-V2-1 to PIN-V2-24. Each is Code's reading, declared at LOCK-m-F3 v0.1, listed as a flag in the BUILD entry and strikable by the seat until LOCK-m-F3 v1.0 (answers:50). The cost of striking one: the analyzer's sha256 moves, G-ANL-F3 is rebuilt and re-run and its artifact superseded, and after LOCK-m-F3 v0.1 a hash that lock names moves too. Each entry's text is in `PINS_F3`, and each has at least one site, a `# PIN (Code, declared at LOCK-m-F3 v0.1 …): PIN-V2-n --` comment (PIN-V2-9 two):

| PIN | Subject |
|---|---|
| V2-1 | A3's NO-READ sub-reason; arm grain vs unit grain |
| V2-2 | the power figure of record per Q-F3 arm |
| V2-3 | the labels of cells A2 and A3 (Step 3) |
| V2-4 | the v2 sentence table |
| V2-5 | A3*, the withholding value, the v1-note; Q-F3 NOT-RUN's outputs |
| V2-6 | Step 6 rendered from m:342's own texts; "[stages]" and the power slot |
| V2-7 | §8.1 and §8.2 at v2; Step 7 |
| V2-8 | A-m1 §2.5 (1), the CLI paths |
| V2-9 | A-m1 §2.5 (2), the Clock dates |
| V2-10 | N8's era rule for PENDING |
| V2-11 | the regression's identity and the preprint of record |
| V2-12 | the Q-F3 reader's V1 (the Q-F3 closure; the posted v1 precondition; Q-F0's inputs refused) |
| V2-13 | counter (c)'s scorer (punctuation replaced by a space) |
| V2-14 | the blind-read draw (seed 20261106; staged adjudication reads) |
| V2-15 | the shared V2 helper; Q-F3's V4 |
| V2-16 | the Q-F3 arm sentence |
| V2-17 | valid-through at F3; Q-F3's secondaries |
| V2-18 | Q-F3's counters |
| V2-19 | Q-F3's NOT-RUN causes |
| V2-20 | `not-run` for Q-F3 and `--v2-closure` (`--campaign` required: the committed checkpoint, or `none` only while none exists; no campaign session) |
| V2-21 | `posting --posting v2` |
| V2-22 | the v2 enumeration's (b) treatment by A3* |
| V2-23 | the G-ANL-F3 artifact and PIN-39's widened commit check |
| V2-24 | the v2 table of record bound at Q-F3's VERDICTS (PIN-40 carried) |

The seat's rulings are recorded beside, as `SEAT_RULED_F3` (A1–A5). The two PIN-29 sites carry the seat's marker ("the seat's A1, 2026-11-06; acknowledged by the PI").


#### The PIN sites declared at LOCK-m-F3 v0.1 (90 sites: every line of `valence_core/mf3/*.py`, `scripts/mf3_sessions.py` and `scripts/m_analyze.py` that opens `PIN (Code, declared at LOCK-m-F3 v0.1` or `PIN (the seat's`, in a comment or a docstring)

| site | where | its opening |
|---|---|---|
| `scripts/m_analyze.py:112` | comment | PIN (the seat's A1, 2026-11-06; acknowledged by the PI): PIN-29's exception, by blob -- the battery's open hook |
| `scripts/m_analyze.py:131` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; A-m1 §2.5 (2); the seat's A5 item 9 (2)): PIN-V2-9 -- three declared dates, |
| `scripts/m_analyze.py:529` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:324, m:347): PIN-V2-19 -- Q-F3 takes the causes both substrates |
| `scripts/m_analyze.py:562` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; A-m1 §2.5 (2); the seat's A5 item 9 (2)): PIN-V2-9 -- the |
| `scripts/m_analyze.py:613` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; A-m1 §2.5 (2); the seat's A5 item 9 (2); N8): PIN-V2-10 -- the |
| `scripts/m_analyze.py:1878` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; A-m1 §2.5 (1); the VERDICTS read §4 item 2): PIN-V2-8 -- |
| `scripts/m_analyze.py:2048` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:271, m:308; PIN-7, PIN-34 carried): PIN-V2-15 -- the V2 block is |
| `scripts/m_analyze.py:2559` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A2 and A3; m:324): PIN-V2-20 -- `not-run` also takes |
| `scripts/m_analyze.py:2955` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; Step 3, m:339): PIN-V2-3 -- Q-F3's cells A2 and A3 are labelled Answered |
| `scripts/m_analyze.py:2971` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A3): PIN-V2-4 -- the v2 table is schema |
| `scripts/m_analyze.py:3072` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:340, m:291; the STOP's §3 items 3-5, not struck): PIN-V2-5 -- A3* is a |
| `scripts/m_analyze.py:3171` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): PIN-V2-6 -- Step 6 renders m:342's own texts (S6_*) by filling their |
| `scripts/m_analyze.py:3252` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:343; PIN-17 carried): PIN-V2-7 -- at v2 §8.1's text is v1's four |
| `scripts/m_analyze.py:3284` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:349): PIN-V2-22 -- the v2 enumeration is PIN-21's over the v2 table |
| `scripts/m_analyze.py:3368` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): PIN-V2-1 -- A3's NO-READ carries PIN-4's sub-reason |
| `scripts/m_analyze.py:3405` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): PIN-V2-2 -- A1 at α .01, P = .70 (a control, as A0); A2 at α .01, |
| `scripts/m_analyze.py:3431` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:312 (c); the STOP's §3 item 7, not struck by the seat): PIN-V2-13 -- |
| `scripts/m_analyze.py:3447` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:312 (c), "seed pinned"; the STOP's §3 item 7): PIN-V2-14 -- the |
| `scripts/m_analyze.py:3671` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:326; the seat's A5 note on item 1): PIN-V2-16 -- PIN-4's clauses |
| `scripts/m_analyze.py:3744` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:308, m:312; PIN-13 carried): PIN-V2-17 -- "valid through position p" at |
| `scripts/m_analyze.py:3802` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:314): PIN-V2-18 -- Q-F3 tabulates the Qwen counters as Q-F0 does, |
| `scripts/m_analyze.py:4106` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A3; m:271, m:318, m:324, m:326, m:358): PIN-V2-12 -- Q-F3's |
| `scripts/m_analyze.py:4148` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; Q7, the PI's word of 2026-11-06; PIN-40 carried): PIN-V2-24 -- the |
| `scripts/m_analyze.py:4348` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A2 and A3; m:336-343, m:349): PIN-V2-21 -- the v2 |
| `scripts/m_analyze.py:5076` | comment | PIN (the seat's A1, 2026-11-06; acknowledged by the PI): PIN-29's exception is by blob, not by |
| `scripts/m_analyze.py:9867` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A1; a dated note in the G-ANL-F3 entry): PIN-V2-11 -- |
| `scripts/m_analyze.py:11082` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the STOP's §3 item 11): PIN-V2-23 -- `ganl` writes |
| `valence_core/mf3/banner.py:46` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m.banner's label rule, applied here: a non-empty |
| `valence_core/mf3/bars.py:178` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:271 "unit session/round"): scaffold_absorption's unit is |
| `valence_core/mf3/bars.py:192` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B17): if G-TIME-F3's line bar fires the |
| `valence_core/mf3/bars.py:294` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's stage_end_eval PIN carried -- the domain is every |
| `valence_core/mf3/bars.py:324` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B30, revised on the build review's finding 6): |
| `valence_core/mf3/gshape.py:457` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 11): each gold is placed as a line |
| `valence_core/mf3/guard.py:46` | comment | PIN (the seat's F-7, 2026-11-06): m:281's 2/2 criterion, which m:295 carries ("as above"), and per reasoning line |
| `valence_core/mf3/guard.py:57` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q1 (C2) part (b); N1): the valence_core.m modules |
| `valence_core/mf3/guard.py:68` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 7): the licence's part (b) hashes the |
| `valence_core/mf3/guard.py:93` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174 "the cap enters the resume identity", m:295 "G-ID-F3, |
| `valence_core/mf3/guard.py:241` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 1): the check IS |
| `valence_core/mf3/lines.py:37` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "which harness lines count is the declared |
| `valence_core/mf3/lines.py:88` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): "empty line" = the text is empty after whitespace |
| `valence_core/mf3/lines.py:93` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "the cap-length prefix is the line as |
| `valence_core/mf3/lines.py:98` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: containment, "since equality misses prefixed |
| `valence_core/mf3/lines.py:131` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q4): the unit is the generation (a task round |
| `valence_core/mf3/readrule.py:52` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's _LINE_RX PIN carried to F3): the declared session-line |
| `valence_core/mf3/readrule.py:125` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): a free group is FREE_GROUP; only the last may be the |
| `valence_core/mf3/readrule.py:194` | comment | PIN (the seat's F-6, 2026-11-06; superseding the per-line-list part of Q5): a contrast session's |
| `valence_core/mf3/readrule.py:210` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's PIN carried -- a free-phase hair trigger is withheld here |
| `valence_core/mf3/readrule.py:243` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's PIN for free responses carried to the |
| `valence_core/mf3/readrule.py:319` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:263, m:271, ruling (h); the build review's finding 3): a |
| `valence_core/mf3/readrule.py:437` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:297 "contrast sessions reported beside", m:271; the build review's |
| `valence_core/mf3/readrule.py:472` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's ruling (h) carried, and its F-6 of 2026-11-06): at |
| `valence_core/mf3/resume.py:106` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q6, "The weights-snapshot binding in the identity |
| `valence_core/mf3/resume.py:180` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's path rules for Q-F3 -- G-ID-F3 "cached+uncached"; |
| `valence_core/mf3/resume.py:224` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's load_or_init, step for step, its identity validation |
| `valence_core/mf3/runner.py:59` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): the procedure of valence_core.m.runner_qwen.qwen_ban_list |
| `valence_core/mf3/runner.py:121` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's defence in depth, carried -- a cached session outside |
| `valence_core/mf3/runner.py:203` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): seconds = perf_counter wall-clock of the whole session |
| `valence_core/mf3/scaffold.py:122` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): the path is "cached" or "uncached" per session; |
| `valence_core/mf3/scaffold.py:127` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174): G-TIME-F3 generates its reasoning lines at |
| `valence_core/mf3/scaffold.py:144` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): j = s at gate stages (session j of the sixteen-row |
| `valence_core/mf3/scaffold.py:157` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8 on the "\n\n" after the reasoning segment, |
| `valence_core/mf3/scaffold.py:192` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "the fire is an exclusion event and ends |
| `valence_core/mf3/scaffold.py:216` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): complete = 2F forced rounds and N_FREE x (reasoning |
| `valence_core/mf3/scaffold.py:239` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8): the guard's and the counters' pre-pick |
| `valence_core/mf3/schedule.py:47` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's materialization PIN carried to Q-F3 -- each campaign |
| `valence_core/mf3/schedule.py:91` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): the gate-stage plan -- G-TIME-F3 one session per arm |
| `valence_core/mf3/schedule.py:105` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): Q-F3 is a Qwen unit, so its roster is Q-F0's -- read |
| `valence_core/mf3/schedule.py:188` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's launch-order PIN carried to six templates -- |
| `valence_core/mf3/schedule.py:210` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's interleave PIN carried to six arms -- next = the |
| `valence_core/mf3/schedule.py:295` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's manifest form, its construction line naming Q-F3; |
| `valence_core/mf3/stages.py:59` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): the analyzer the gate line logs and the licence hashes is |
| `valence_core/mf3/stages.py:99` | docstring | PIN (Code, declared at LOCK-m-F3 v0.1): m's layout under data/mf3 -- schedules/ (read only), |
| `valence_core/mf3/stages.py:291` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q1 (C2): "Every non-stub mf3 stage checks both at |
| `valence_core/mf3/stages.py:394` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PRIOR_STAGE carried, m:293-298): G-ID-F3 needs G-TIME-F3 |
| `valence_core/mf3/stages.py:428` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:295; the build design's B7): the artifact's cap must |
| `valence_core/mf3/stages.py:466` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:294-296; the build review's finding 4): the cap is fixed by |
| `valence_core/mf3/stages.py:559` | docstring | PIN (Code, declared at LOCK-m-F3 v0.1; m's _extra carried): identity_extra carries {lock_sha256, |
| `valence_core/mf3/stages.py:715` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's _hair_hit carried): the fired generation is the session's |
| `valence_core/mf3/stages.py:857` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): a reasoning line's excerpt is its block, its text and its |
| `valence_core/mf3/stages.py:986` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:293, the seat's Q5): the count is the lines whose |
| `valence_core/mf3/stages.py:991` | comment | PIN (the seat's F-6, 2026-11-06): what is reported is the count k against the declared maximum ("k of |
| `valence_core/mf3/stages.py:1110` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:295 "A2s and A3s once each; criterion 2/2 as above"; the seat's |
| `valence_core/mf3/stages.py:1140` | comment | PIN (the seat's F-7, 2026-11-06; a seat PIN at LOCK-m-F3 v0.1, set before G-ID-F3 has run): a pair is |
| `valence_core/mf3/stages.py:1184` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried; B7): a G-ID-F3 artifact is never overwritten |
| `valence_core/mf3/stages.py:1280` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried): G-ID-F3's sessions are sham-only and read in full |
| `valence_core/mf3/stages.py:1348` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B23): the lexical bar's numerator is the |
| `valence_core/mf3/stages.py:1412` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried, and B7): the G-ID-F3 artifact on disk is |
| `valence_core/mf3/stages.py:1627` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried): the campaign report is pick-free -- looks with |
| `valence_core/mf3/verify.py:148` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's read check, carried: the pick follows choice_read's |
| `valence_core/mf3/verify.py:173` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B22): the contrast/sham role is the |


## 10. Dated notes, 2026-11-07

- **N13's entry term (the seat's ruling).** Any v2-closure entry declaring `--campaign none` names every set-aside
  that exists for the unit and its session count, so the declaration is auditable.
- **N1 at this lock:** N1 is committed at `9480f9b` (the coordinating session's commit). `PREPRINT-v1_0-draft.md`
  holds its bytes of record (`45b67246…7a41`), and its status banner is in the sidecar
  `PREPRINT-v1_0-draft.STATUS.md`. G-ANL-F3.json was written on that HEAD, so its `g_anl_f3.regression.preprint`
  records the restored tree, with `head_file_is_table` true. The battery check `F3R-PREPRINT-OF-RECORD` asserts only
  that the committed blob of record serves the regression, whatever the tree holds (`10a2bbb`; the seat's answer §1).
- **m's package moved before this lock.** The hygiene commit (`993eba1`; the seat's N12) moved m's `package_sha256`
  from `60199b36…feec` to the value in §1. This lock names the moved value. mf3's licence's eleven files are
  unchanged by it (gcal is in mf3's `ABSENT_MODULES`).

## 11. What follows

1. **G-TIME-F3's wiring:** the `time` subcommand is wired in `scripts/mf3_sessions.py` at its step, after this
   lock's commit.
   - Code intends it as an edit under F-1's clearance: a subcommand wiring that touches no scoring-stack function, so
     no G-SHAPE-F3 re-run. The wiring's entry states that reading on the edit as made.
   - The coordinating session's routing of 2026-11-07, relayed in chat and recorded in the wiring's entry, has the
     wiring also carry:
     - the rest of m's pre-load check, in `scripts/m_sessions.py`'s forms: the MLXLM_USE_MODELSCOPE and local-path
       refusals, the hub's own offline resolution, the SNAPSHOT line, and the post-load re-read with its model-id
       STOP;
     - a DRIVER line (the committed driver's blob sha256), which LOCK-m-F3 v0.2 records.
   - The seat's F-2 places the pre-load check with the campaign subcommand's wiring. The wiring's entry quotes F-2
     and gives Code's reading in a dated note.
2. **G-TIME-F3** (m:293): its six sessions on the laptop, under m:267's checklist and the Qwen launch checklist; the
   seat's read under m:263's printed form and m's §3 rule.
3. **The cap**, fixed by G-TIME-F3's trigger (m:294).
4. **G-ID-F3** under F-7 (m:295).
5. **LOCK-m-F3 v0.2**: the cap, the path and the projections (m:296).
6. **G-F3** (m:297); **G-VER**, **G-PWR** and **LOCK-m-F3 v1.0** with D2 (m:298; ADDENDUM-m1 §2.3).
