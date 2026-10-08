# AUDIT-note-release v1.2 -- N14: sham-arm pseudo-statistics, the three label-artifact captures

- Code stamp: Thu Oct  8 11:26:15 UTC 2026 (date -u)  [run metadata]
- HEAD at run time: cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55  [run metadata; every record read below is pinned to bbc9ffe]
- Pin: bbc9ffe = bbc9ffe72fb8a942431c9bf2622a36e581fdf93c
- Block: `AUDIT-note-release-v1_2.md`@bbc9ffe sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841` (141 lines; MATCH vs routed 8cd8a9ac...3841); item N14 = block lines 115-116
- Script: `scripts/audit_note_N14.py` sha256 `933b36529326788e4afd1b98fe7a974d04a1147f196af499f60075191e0e1e95`
- Interpreter: /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python (Python 3.12.9); stdlib only (math.comb, fractions.Fraction); no numpy/scipy/sklearn use; no model
- Command: `/Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python scripts/audit_note_N14.py` (run from the repository root)

Status vocabulary: reproduced (computed here from committed JSON/JSONL and equal to the stored field) | log-only (prose only; pinned locator) | not found | discrepant | computed-new (asked-for or supporting computation with no stored counterpart). Locators are `path@bbc9ffe:line` as in `git show bbc9ffe:<path>`; every line number below was found by this script by searching the pinned text, not typed.

The item, quoted from the block:

> AUDIT-note-release-v1_2.md@bbc9ffe:115: ### N14. Sham-arm pseudo-statistics (the artifact captures)
> AUDIT-note-release-v1_2.md@bbc9ffe:116: *Defends:* "what the shields caught." *Referents:* `data/e2a`, `data/f`, `data/olmo` as above. *Procedure:* the three captures with their arm, map, n and statistic in one table: e2a sham +0.111/−0.079 beside state +0.104/−0.031; f1 CORR +.121/−.130; OLMo DPO +0.1667 single map with the other map's figure beside it. *Output:* `…_note-N14-artifacts.md`.

## 0. Referents and integrity

Every artifact is read from the pin with `git show`; its sha256 at the pin and the working tree's blob against the pin (informational; nothing here reads the working tree's copy):

| artifact | sha256 at pin | working tree vs pin |
|---|---|---|
| `data/e2a/sessions.jsonl` | `58a7949fc0e98e714b4f96070d4b2ba945c47df85a992e7f617f39c6197bd24e` | EQUAL to pin |
| `data/e2a/analysis.json` | `79cd53c0adf55878628d38a5a00e4045d2a216d28b1f0b2ed90b2304920dd52e` | EQUAL to pin |
| `data/f/sessions.jsonl` | `d49913e5ffdfb935d0ae344bd4202d852cb5723394c17870e37b619aa1033dcc` | EQUAL to pin |
| `data/f/screen_analysis.json` | `f71048c63fd61bebf8acda4eb237614427fa6e76018552ba4d9f3d0895ca920d` | EQUAL to pin |
| `data/olmo/b3_screen_base.json` | `7d2ac0d5ffb429e2496ad69ff42b01dd5e80fce5ad953720a0be6d7c595731d8` | EQUAL to pin |
| `data/olmo/b3_analysis_base.json` | `953d01834b1b78897eddeaa0da4942e11240b5bc7d6fb0c8252cf2b7945d38b6` | EQUAL to pin |
| `data/olmo/b3_screen_sft.json` | `015aed2bf5fb730f5509c5793a91b195ccce5ec4b6d2966215faa7360ff71e66` | EQUAL to pin |
| `data/olmo/b3_analysis_sft.json` | `a860572ba4a37747c83835742b4c2e89b1450e3bde2c2135096c8380ac0d71ba` | EQUAL to pin |
| `data/olmo/b3_screen_dpo.json` | `e900b67606c4a3c113689e8a4d402705de6d51b1e749abd3710e90f2f26d1067` | EQUAL to pin |
| `data/olmo/b3_analysis_dpo.json` | `8dc645e04f0103b2998ab4c684fabe39301ddea68cc62905f96df218ddf47318` | EQUAL to pin |
| `data/olmo/b3_screen_instruct.json` | `9ba4b64d95b26e1cd720902d569a0ed6179d67b6ea5aa344614b546cfc32bd24` | EQUAL to pin |
| `data/olmo/b3_analysis_instruct.json` | `014cb8283a271b0d44e3718448da0b43b0960da30aa153ef496fc7cc492e3863` | EQUAL to pin |
| `data/e2b/h3_tagscreen.json` | `2b764063a1b635d35f0b989c204cd9ccdea7130bde21d57ea15bd0daa2745f30` | EQUAL to pin |
| `data/f/pools.json` | `8547d9a11ba55b95dda2988d4e9bdc685196abcda55870d7713703df372d17a0` | EQUAL to pin |
| `valence_core/e2d/habit.py` (executed from its pinned blob) | `2d042d98eb0a02bcacd1afddf7aedefe15fb5c601e84b92131aedcdbb66f2ceb` | EQUAL to pin |

Analyzers of record that live in the gitignored clone (absent from any clone of the repository; opened read-only, quoted for definitions only, nothing executed): `jlens-qwen36/scripts/e2a_sessions.py` sha256 `0950b0054ad84a4a1fd0a6e90912d1643ef46a48f1a452daad62e3c655bec1dc`; `jlens-qwen36/scripts/f_sessions.py` sha256 `d2dcde569080fe86d69da3f7d908a0c7fde401f4d201bfd3ffcec4b7891ee071`. The tracked reproduction paths are `scripts/e2a_recount.py` (e2a) and `scripts/b3_analyze.py` (B3). For f1, no tracked code at the pin recomputes the by-map figures from `data/f/sessions.jsonl` (the regression suite's `check_screen_pvalues`, valence_core/regression/analysis.py@bbc9ffe:69, recovers k from the stored `delta` and re-tests the p-values; it does not read the maps), so this script's recount is the tracked reproduction of the f1 map figures below.

Structural assertions on the session records (all passed, or the script would have stopped): tag_plus/tag_P = pair[1] iff swap (e2a, f1) and tag_plus = pair[map] (B3); each stored first-pick flag equals the first choice's picked pole. f1 forced phase = 2 rounds per config alternating from the start config (`jlens-qwen36/scripts/f_sessions.py:85`, `:296`): 283/283 valid sessions match; the fifth round ran the config the first free choice picked in 283/283. B3 forced order starts +pole iff the arm's session index is even (`scripts/box_b3_sessions.py@bbc9ffe:141`): base 89/89; sft 99/99; dpo 94/94; instruct 95/95 sessions (all run sessions, incl. excluded). Added at the round-2 values-check: in every capture arm the +label is pair[0] in map A / 0 and pair[1] in map B / 1; for every valid session the tag-form habit break (first pick ≠ start label) equals decompose()'s pole form; the per-pair break counts sum to the pooled decomposition's; maple and cedar occur only as the pair maple/cedar in the ten Qwen arms; and H3's four C pairs are exactly e2a's and f1's four pairs.

## 1. The three captures in one table

Statistic in every row: **Δ_map = k/n − ½**, n = the arm's VALID sessions in that label map (excluded sessions and sessions with no first free choice removed, as each campaign's analyzer removes them), k = those whose FIRST free choice picked the arm's +label (+pole / P). Domain of every rate: valid sessions of the named arm and map. Stored values are 4 dp in e2a and f1 (rounded by the analyzer), full floats in B3. e2a: validity is the session record's stored `excluded` flag (stored exclusions: reward 10/112, sham 3/40, random1 1/24, random2 2/24), i.e. the FROZEN audit's exclusion set, the published rule that `analysis.json` carries (scripts/e2a_recount.py@bbc9ffe:120, "55/102 under the frozen audit; 54/101 under v2"). Every e2a figure here is on that domain; the v2 recount (54/101) is N4's, not this item's.

| # | model | campaign | arm | role | map | k/n | Δ_map (exact) | Δ_map | stored | stored field | match | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qwen3.6-27B (MLX 4-bit) | e2a | sham | capture (sham arm) | A | 11/18 | 1/9 | **+0.1111** | +0.1111 | `data/e2a/analysis.json:sham.by_map.A` | YES | reproduced |
| 1 | Qwen3.6-27B (MLX 4-bit) | e2a | sham | capture (sham arm) | B | 8/19 | -3/38 | **-0.0789** | -0.0789 | `data/e2a/analysis.json:sham.by_map.B` | YES | reproduced |
| 1 | Qwen3.6-27B (MLX 4-bit) | e2a | reward | beside (state arm) | A | 32/53 | 11/106 | **+0.1038** | +0.1038 | `data/e2a/analysis.json:reward.by_map.A` | YES | reproduced |
| 1 | Qwen3.6-27B (MLX 4-bit) | e2a | reward | beside (state arm) | B | 23/49 | -3/98 | **-0.0306** | -0.0306 | `data/e2a/analysis.json:reward.by_map.B` | YES | reproduced |
| 2 | Qwen3.6-27B (MLX 4-bit) | f1 | CORR | capture (contrast arm) | A | 18/29 | 7/58 | **+0.1207** | +0.1207 | `data/f/screen_analysis.json:contrasts.CORR.by_map.A` | YES | reproduced |
| 2 | Qwen3.6-27B (MLX 4-bit) | f1 | CORR | capture (contrast arm) | B | 10/27 | -7/54 | **-0.1296** | -0.1296 | `data/f/screen_analysis.json:contrasts.CORR.by_map.B` | YES | reproduced |
| 2 | Qwen3.6-27B (MLX 4-bit) | f1 | sham | beside (sham arm) | A | 9/14 | 1/7 | **+0.1429** | — | `recomputed from data/f/sessions.jsonl (no stored by-map field for sham)` | n/a (not stored) | computed-new |
| 2 | Qwen3.6-27B (MLX 4-bit) | f1 | sham | beside (sham arm) | B | 9/19 | -1/38 | **-0.0263** | — | `recomputed from data/f/sessions.jsonl (no stored by-map field for sham)` | n/a (not stored) | computed-new |
| 3 | OLMo-3.1-32B-Instruct-DPO (bf16) | B3-dpo | marker | capture (marker arm) | 1 | 16/24 | 1/6 | **+0.1667** | +0.1667 (16/24) | `data/olmo/b3_analysis_dpo.json:by_label_map.1` | YES | reproduced |
| 3 | OLMo-3.1-32B-Instruct-DPO (bf16) | B3-dpo | marker | beside (other map) | 0 | 11/24 | -1/24 | **-0.0417** | -0.0417 (11/24) | `data/olmo/b3_analysis_dpo.json:by_label_map.0` | YES | reproduced |
| 3 | OLMo-3.1-32B-Instruct-DPO (bf16) | B3-dpo | sham | beside (sham arm) | 0 | 4/8 | 0 | **+0.0000** | — | `recomputed from data/olmo/b3_screen_dpo.json (by-map not stored for controls)` | n/a (not stored) | computed-new |
| 3 | OLMo-3.1-32B-Instruct-DPO (bf16) | B3-dpo | sham | beside (sham arm) | 1 | 4/10 | -1/10 | **-0.1000** | — | `recomputed from data/olmo/b3_screen_dpo.json (by-map not stored for controls)` | n/a (not stored) | computed-new |
| 3 | OLMo-3.1-32B-Instruct-DPO (bf16) | B3-dpo | random | beside (random arm) | 0 | 4/10 | -1/10 | **-0.1000** | — | `recomputed from data/olmo/b3_screen_dpo.json (by-map not stored for controls)` | n/a (not stored) | computed-new |
| 3 | OLMo-3.1-32B-Instruct-DPO (bf16) | B3-dpo | random | beside (random arm) | 1 | 2/8 | -1/4 | **-0.2500** | — | `recomputed from data/olmo/b3_screen_dpo.json (by-map not stored for controls)` | n/a (not stored) | computed-new |

Pooled over both maps, same arms (Δ = k/n − ½ over valid sessions of the arm):

| capture | campaign | arm | k/n | Δ pooled | stored | stored field | match |
|---|---|---|---|---|---|---|---|
| 1 | e2a | reward | 55/102 | +0.0392 | +0.0392 | `data/e2a/analysis.json:reward.delta_first` | YES |
| 1 | e2a | sham | 19/37 | +0.0135 | +0.0135 | `data/e2a/analysis.json:sham.delta_first` | YES |
| 2 | f1 | CORR | 28/56 | +0.0000 | +0.0000 | `data/f/screen_analysis.json:contrasts.CORR.delta` | YES |
| 2 | f1 | sham | 18/33 | +0.0455 | 0.045455 (absolute value, as stored) | `data/f/screen_analysis.json:sham_pseudo` | YES |
| 3 | B3-dpo | marker | 27/48 | +0.0625 | +0.0625 | `data/olmo/b3_analysis_dpo.json:delta_first` | YES |
| 3 | B3-dpo | sham | 8/18 | -0.0556 | -0.0556 | `data/olmo/b3_analysis_dpo.json:controls.sham.pseudo_delta` | YES |
| 3 | B3-dpo | random | 6/18 | -0.1667 | -0.1667 | `data/olmo/b3_analysis_dpo.json:controls.random.pseudo_delta` | YES |

The pooled Δ is the n-weighted mean of the two map Δs, not their simple mean (exact Fractions):

| arm | pooled | n-weighted mean of maps | identity holds | simple mean of maps |
|---|---|---|---|---|
| e2a reward | +0.0392 | +0.0392 | True | +0.0366 |
| e2a sham | +0.0135 | +0.0135 | True | +0.0161 |
| f1 CORR | +0.0000 | +0.0000 | True | -0.0045 |
| f1 sham | +0.0455 | +0.0455 | True | +0.0583 |
| B3-dpo marker | +0.0625 | +0.0625 | True | +0.0625 |

f1 CORR's exact 0.000 is an outcome of the counts, not of the design: map A 18/29 and map B 10/27 give k − n/2 = 7/2 and -7/2, pooled 28/56. Counterbalancing makes a map-locked artifact cancel in expectation; the exact zero here is the realized counts.

## 2. Definitions of record, per capture

**e2a (capture 1).** Producing analyzer in the gitignored clone; tracked recount `scripts/e2a_recount.py`.

```
jlens-qwen36/scripts/e2a_sessions.py:186:     swap = (s // 4) % 2 == 1
jlens-qwen36/scripts/e2a_sessions.py:187:     tag_plus, tag_minus = (pair[1], pair[0]) if swap else pair
jlens-qwen36/scripts/e2a_sessions.py:188:     start_plus = (s // 8) % 2 == 0
jlens-qwen36/scripts/e2a_sessions.py:354:         firsts = [r["first_free_pick_pos"] for r in sub]
jlens-qwen36/scripts/e2a_sessions.py:355:         d = float(np.mean(firsts)) - 0.5
jlens-qwen36/scripts/e2a_sessions.py:358:             mm = [r["first_free_pick_pos"] for r in sub if r["swap"] == m]
jlens-qwen36/scripts/e2a_sessions.py:359:             by_map["B" if m else "A"] = (round(float(np.mean(mm)) - 0.5, 4)
jlens-qwen36/scripts/e2a_sessions.py:372:         pseudo = [abs(out[a]["delta_first"]) for a in
jlens-qwen36/scripts/e2a_sessions.py:373:                   ("sham", "random1", "random2") if a in out]
scripts/e2a_recount.py@bbc9ffe:118: def primary(audit):
scripts/e2a_recount.py@bbc9ffe:119:     """e2a's primary DV: share of VALID reward-arm sessions whose first free
scripts/e2a_recount.py@bbc9ffe:120:     pick was the +pole label. 55/102 under the frozen audit; 54/101 under v2."""
scripts/e2a_recount.py@bbc9ffe:121:     valid = [s for s in ROWS if s['arm'] == 'reward' and exclusion(s, audit) is None]
scripts/e2a_recount.py@bbc9ffe:122:     k = sum(1 for s in valid if s['first_free_pick_pos'])
```

Pre-registered statistic and conjunct (2): archive/RESULTS-cycles3-4.md@bbc9ffe:1306 and :1308 ("Δ = P(choose +pole) − 0.5 pooled over counterbalance maps"; "(2) Δ ≥ 0 in BOTH counterbalance maps"). Map = which label of the rotated pair is +pole: A = swap False (tag_plus = pair[0]); B = swap True (tag_plus = pair[1]); swap = (s // 4) % 2. In the sham arm no label carries a state; its +pole is designated by the same rule, so its map Δs are the identical statistic on an arm where no contingency exists. The control envelope (conjunct 1) is max |pooled Δ| over sham, random1, random2 (absolute values, `jlens-qwen36/scripts/e2a_sessions.py:372`); the map split enters only conjunct (2).

**f1 CORR (capture 2).** Producing analyzer in the gitignored clone (`analyze()`); no tracked analyzer at the pin.

```
jlens-qwen36/scripts/f_sessions.py:276:     swap = (s // 4) % 2 == 1
jlens-qwen36/scripts/f_sessions.py:277:     tag_P, tag_Q = (pair[1], pair[0]) if swap else pair
jlens-qwen36/scripts/f_sessions.py:278:     start_P = (s // 8) % 2 == 0
jlens-qwen36/scripts/f_sessions.py:456:     pseudo = abs(float(np.mean(sham_first)) - 0.5) if sham_first else None
jlens-qwen36/scripts/f_sessions.py:461:         firsts = [r["first_free_pick_P"] for r in valid if r["arm"] == c
jlens-qwen36/scripts/f_sessions.py:462:                   and r["first_free_pick_P"] is not None]
jlens-qwen36/scripts/f_sessions.py:469:             mm = [r["first_free_pick_P"] for r in valid
jlens-qwen36/scripts/f_sessions.py:470:                   if r["arm"] == c and r["swap"] == m
jlens-qwen36/scripts/f_sessions.py:471:                   and r["first_free_pick_P"] is not None]
jlens-qwen36/scripts/f_sessions.py:472:             by_map["B" if m else "A"] = (round(float(np.mean(mm)) - 0.5, 4)
```

Pre-registered screen-hit criterion: PROPOSAL-f-natural-reinforcer-screen.md@bbc9ffe:104-106 ("(2) sign consistency across both maps"). Map = which label of the pair denotes P: A = swap False (tag_P = pair[0]); B = swap True (tag_P = pair[1]); swap = (s // 4) % 2. For CORR, P = clean text and Q = seeded character-level corruption (target direction: avoid corrupted, one-sided; PROPOSAL-f-natural-reinforcer-screen.md@bbc9ffe:86, the CORR table row). f1 has no injected state in any arm (PROPOSAL-f-natural-reinforcer-screen.md@bbc9ffe:27, "Nothing is injected", under the §0 heading at :17; FINDINGS-4.md@bbc9ffe:15). The stored sham statistic is an absolute value (`sham_pseudo` = |share − ½|).

**B3 DPO (capture 3).** Tracked analyzer `scripts/b3_analyze.py` (committed before any campaign ran, per its docstring).

```
scripts/b3_analyze.py@bbc9ffe:55: def delta(sessions, arm) -> tuple[float, int, int]:
scripts/b3_analyze.py@bbc9ffe:56:     """(Delta, k_plus, n) over VALID sessions of one arm."""
scripts/b3_analyze.py@bbc9ffe:57:     rows = [s for s in sessions
scripts/b3_analyze.py@bbc9ffe:58:             if s["arm"] == arm and not s["excluded"]
scripts/b3_analyze.py@bbc9ffe:59:             and s["first_free_pole"] is not None]
scripts/b3_analyze.py@bbc9ffe:60:     n = len(rows)
scripts/b3_analyze.py@bbc9ffe:61:     k = sum(1 for s in rows if s["first_free_pole"] == "pos")
scripts/b3_analyze.py@bbc9ffe:62:     return ((k / n - 0.5) if n else float("nan")), k, n
scripts/b3_analyze.py@bbc9ffe:63: 
scripts/b3_analyze.py@bbc9ffe:65: def by_map(sessions, arm) -> dict:
scripts/b3_analyze.py@bbc9ffe:66:     out = {}
scripts/b3_analyze.py@bbc9ffe:67:     for m in (0, 1):
scripts/b3_analyze.py@bbc9ffe:68:         rows = [s for s in sessions
scripts/b3_analyze.py@bbc9ffe:69:                 if s["arm"] == arm and not s["excluded"]
scripts/b3_analyze.py@bbc9ffe:70:                 and s["cell"]["map"] == m and s["first_free_pole"] is not None]
scripts/b3_analyze.py@bbc9ffe:71:         n = len(rows)
scripts/b3_analyze.py@bbc9ffe:72:         k = sum(1 for s in rows if s["first_free_pole"] == "pos")
scripts/b3_analyze.py@bbc9ffe:73:         out[str(m)] = {"delta": (k / n - 0.5) if n else float("nan"),
scripts/b3_analyze.py@bbc9ffe:74:                        "k": k, "n": n}
scripts/b3_analyze.py@bbc9ffe:75:     return out
scripts/b3_analyze.py@bbc9ffe:122:     def locks_toward(positive: bool) -> bool:
scripts/b3_analyze.py@bbc9ffe:123:         return all(v["n"] and v["delta"] != 0
scripts/b3_analyze.py@bbc9ffe:124:                    and (v["delta"] > 0) == positive for v in maps.values())
scripts/box_b3_sessions.py@bbc9ffe:107:     """4 roster pairs x 2 label maps = 8 cells."""
scripts/box_b3_sessions.py@bbc9ffe:108:     out = []
scripts/box_b3_sessions.py@bbc9ffe:109:     for pair in roster:
scripts/box_b3_sessions.py@bbc9ffe:110:         for m in (0, 1):
scripts/box_b3_sessions.py@bbc9ffe:111:             tp, tm = (pair[0], pair[1]) if m == 0 else (pair[1], pair[0])
scripts/box_b3_sessions.py@bbc9ffe:112:             out.append({"pair": list(pair), "map": m,
scripts/box_b3_sessions.py@bbc9ffe:113:                         "tag_plus": tp, "tag_minus": tm})
scripts/box_b3_sessions.py@bbc9ffe:114:     return out
```

Pre-registered screen trigger: LOCK-g.md@bbc9ffe:151-154 (marker Δ exceeds the campaign's own control envelope = max |pseudo-Δ| over sham and random, AND sign locks across maps). Map = 0: tag_plus = pair[0]; 1: tag_plus = pair[1] (strata = 4 roster pairs x 2 maps). sign-lock requires both maps non-zero and of one sign (`locks_toward`). Registered valid targets 48:18:18 (`data/olmo/b3_screen_dpo.json:targets`), scheduled per stratum 6:3:3 over 8 strata (4 pairs x 2 maps; `data/olmo/b3_screen_dpo.json:per_stratum`, `:strata`); realized per-map valid n at DPO: marker 24/24, sham 8/10, random 10/8 (map 0 / map 1).

## 3. The sham (and random) arms beside each capture

| capture | arm | map | k/n | Δ_map | pooled k/n | pooled Δ | status |
|---|---|---|---|---|---|---|---|
| 1 (e2a) | sham | A | 11/18 | +0.1111 | 19/37 | +0.0135 | reproduced |
| 1 (e2a) | sham | B | 8/19 | -0.0789 | 19/37 | +0.0135 | reproduced |
| 2 (f1) | sham | A | 9/14 | +0.1429 | 18/33 | +0.0455 | computed-new |
| 2 (f1) | sham | B | 9/19 | -0.0263 | 18/33 | +0.0455 | computed-new |
| 3 (B3-dpo) | sham | 0 | 4/8 | +0.0000 | 8/18 | -0.0556 | computed-new |
| 3 (B3-dpo) | sham | 1 | 4/10 | -0.1000 | 8/18 | -0.0556 | computed-new |
| 3 (B3-dpo) | random | 0 | 4/10 | -0.1000 | 6/18 | -0.1667 | computed-new |
| 3 (B3-dpo) | random | 1 | 2/8 | -0.2500 | 6/18 | -0.1667 | computed-new |

Only capture 1 is itself a sham-arm statistic. Capture 2 is a contrast arm (CORR) whose maps cancel; capture 3 is the marker arm, one map positive. Which shield disposed of each excursion, from the stored or recomputed conjuncts: e2a reward -- envelope conjunct False (Δ +0.0392 vs max abs pseudo-Δ 0.1522, recomputed from analysis.json with the analyzer's abs reading), both-maps-≥0 conjunct False; f1 CORR -- the counterbalanced pooling itself cancels the excursion (pooled 0.000), and the stored conjuncts (envelope, sign consistency, binomial) are [False, False, False] (`data/f/screen_analysis.json:contrasts.CORR.conjuncts`); B3 DPO -- stored `delta_exceeds_envelope_upward` False, `sign_locks_positive` False (`data/olmo/b3_analysis_dpo.json:conjuncts`). The sham arm's role in captures 2 and 3 is the envelope (f1: sham pseudo-Δ; B3: max over sham and random).

## 4. Why the record classed each an artifact capture (quoted, pinned)

**Capture 1, e2a.** The e2a VERDICT entry, conjunct (2):

> archive/RESULTS-cycles3-4.md@bbc9ffe:655:     (2) FAIL: map A +0.104 / map B −0.031 — sign not locked; the same
> archive/RESULTS-cycles3-4.md@bbc9ffe:656:     A-positive/B-negative pattern appears in sham (+0.111/−0.079),
> archive/RESULTS-cycles3-4.md@bbc9ffe:657:     identifying it as a label/order artifact correctly absorbed by
> archive/RESULTS-cycles3-4.md@bbc9ffe:658:     counterbalancing. Conjunct (3) FAIL: binomial p = 0.244.

Restated in the synthesis:

> FINDINGS-3.md@bbc9ffe:86: (A +0.104 / B −0.031) with the **identical pattern in sham**
> FINDINGS-3.md@bbc9ffe:87: (+0.111/−0.079) — a label/order artifact of ≈ 0.10 that an
> FINDINGS-3.md@bbc9ffe:88: uncounterbalanced, sham-less version of this experiment would have
> FINDINGS-3.md@bbc9ffe:89: published as approach behavior; binomial p = 0.244.

Basis (Code's paraphrase of the quoted entry): the state arm's map pattern (A positive, B negative) recurs in the arm with no state, so the pattern cannot be the state's; the counterbalanced pooled Δ absorbs it.

**Capture 2, f1 CORR.** The f1 SCREEN VERDICT entry:

> archive/RESULTS-cycles3-4.md@bbc9ffe:82:     map-inconsistent), p=.86 — null. CORR n=56, Δ = 0.000 exactly
> archive/RESULTS-cycles3-4.md@bbc9ffe:83:     (maps +.121/−.130 mirror-cancel — the label artifact absorbed by
> archive/RESULTS-cycles3-4.md@bbc9ffe:84:     design). FDBK n=44, +.023 (map-inconsistent), p=.44 — null.

and the synthesis, which names it the second live capture:

> FINDINGS-4.md@bbc9ffe:71: **4. The territory manufactures false positives, demonstration two.**
> FINDINGS-4.md@bbc9ffe:72: CORR's maps read +.121 and −.130 and cancel to Δ = 0.000 exactly —
> FINDINGS-4.md@bbc9ffe:73: the ~0.1-scale label/order artifact captured live for the second time
> FINDINGS-4.md@bbc9ffe:74: (e2a's sham-mirrored +.10 was the first). An uncounterbalanced,
> FINDINGS-4.md@bbc9ffe:75: sham-less version of either experiment publishes a discovery.
> FINDINGS-4.md@bbc9ffe:76: Shield-first design is the difference between a null and a false
> FINDINGS-4.md@bbc9ffe:77: claim, now shown twice at the same magnitude.

Basis (Code's paraphrase of the quoted entry): equal-and-opposite map Δs on a contrast whose property is fixed across maps; only the label-to-property assignment flips, so a map-locked effect is a label effect.

**Capture 3, B3 DPO.** The B3 SCREEN entry:

> RESULTS.md@bbc9ffe:7673:   - **DPO is the one that shows why the criterion is conjunctive.** It is the
> RESULTS.md@bbc9ffe:7674:     only stage with Δ pointing the coupling direction (+0.0625), and it fails
> RESULTS.md@bbc9ffe:7675:     **both** conjuncts independently: it does not clear its envelope, and the
> RESULTS.md@bbc9ffe:7676:     entire positive Δ is carried by one label map (+0.1667) while the other
> RESULTS.md@bbc9ffe:7677:     runs negative (−0.0417). That is a **label artifact, not a state effect**,
> RESULTS.md@bbc9ffe:7678:     and it is the size rule 12 names as first-order (~0.10). A screen testing
> RESULTS.md@bbc9ffe:7679:     |Δ| alone would have owed this stage a second look; the sign-lock
> RESULTS.md@bbc9ffe:7680:     requirement disposes of it on the design's own terms. Counterbalancing
> RESULTS.md@bbc9ffe:7681:     earned its keep here.

Basis (Code's paraphrase of the quoted entry): the pooled Δ (+0.0625) is carried by one map while the other is negative, so the sign-lock conjunct fails; magnitude at rule 12's first-order scale.

**The count of three, and rule 12.**

> PROPOSAL-j-dose-escalation.md@bbc9ffe:288: 3. **Label artifact (~0.10; three live captures across two models)** —
> PROPOSAL-j-dose-escalation.md@bbc9ffe:289:    counterbalanced maps, arm S, the sign-locks conjunct. A fourth
> PROPOSAL-j-dose-escalation.md@bbc9ffe:290:    capture is expected and is not a finding.
> CLAUDE.md@bbc9ffe:313: 12. Counterbalance + sham always; position/label artifacts are
> CLAUDE.md@bbc9ffe:314:     first-order (~0.10), captured live twice.

CLAUDE.md's "captured live twice" predates the B3 entry (RESULTS.md@bbc9ffe:7655, 2026-08-24); PROPOSAL-j's "three live captures across two models" counts e2a and f1 (Qwen) and B3 DPO (OLMo). Rule 12's text is not this audit's to change; the note should say three.

## 5. What the captured artifacts consist of (computed-new; POST-HOC, descriptive, deciding nothing)

Rule 11 applies: everything in this section is post-hoc on committed data; it changes no verdict and no label. The frame is the record's own: the alternation habit (`valence_core/e2d/habit.py@bbc9ffe:22`, weighted form :25; "algebra, not a finding", :37). Every session in these arms has F = 2 forced rounds per label, alternating, so the last forced label is the complement of the start label and the habit predicts that the first free pick returns to the START label. Per map, exactly (Fractions; asserted):

    Δ_map = (n_fe− / N − ½)  +  (B₊ − B₋) / N

where n_fe− = sessions whose last forced round was the −label (= sessions that started on the +label; the habit then picks +), B₊ = habit breaks that picked +, B₋ = habit breaks that picked −. The first term is the forced-order balance within the map (set by the schedule and by exclusions), the second the net direction of the habit breaks. The record's `habit.break_rates` (executed from the pinned blob) returns the same Δ in its weighted form for every row (column 'habit ✓').

| arm | map | N | k₊ | Δ_map | started on + (n_fe−) | forced-order term | breaks to + / to − | net-break term | breaks to pair[0] / pair[1] | follows habit | habit ✓ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| e2a reward | A | 53 | 32 | +0.1038 | 26 | -0.0094 | 7 / 1 | +0.1132 | 7 / 1 | 45/53 | True |
| e2a reward | B | 49 | 23 | -0.0306 | 23 | -0.0306 | 4 / 4 | +0.0000 | 4 / 4 | 41/49 | True |
| e2a reward | pooled | 102 | 55 | +0.0392 | 49 | -0.0196 | 11 / 5 | +0.0588 | 11 / 5 | 86/102 | True |
| e2a sham | A | 18 | 11 | +0.1111 | 10 | +0.0556 | 3 / 2 | +0.0556 | 3 / 2 | 13/18 | True |
| e2a sham | B | 19 | 8 | -0.0789 | 11 | +0.0789 | 0 / 3 | -0.1579 | 3 / 0 | 16/19 | True |
| e2a sham | pooled | 37 | 19 | +0.0135 | 21 | +0.0676 | 3 / 5 | -0.0541 | 6 / 2 | 29/37 | True |
| f1 CORR | A | 29 | 18 | +0.1207 | 15 | +0.0172 | 3 / 0 | +0.1034 | 3 / 0 | 26/29 | True |
| f1 CORR | B | 27 | 10 | -0.1296 | 12 | -0.0556 | 1 / 3 | -0.0741 | 3 / 1 | 23/27 | True |
| f1 CORR | pooled | 56 | 28 | +0.0000 | 27 | -0.0179 | 4 / 3 | +0.0179 | 6 / 1 | 49/56 | True |
| f1 sham | A | 14 | 9 | +0.1429 | 8 | +0.0714 | 1 / 0 | +0.0714 | 1 / 0 | 13/14 | True |
| f1 sham | B | 19 | 9 | -0.0263 | 12 | +0.1316 | 0 / 3 | -0.1579 | 3 / 0 | 16/19 | True |
| f1 sham | pooled | 33 | 18 | +0.0455 | 20 | +0.1061 | 1 / 3 | -0.0606 | 4 / 0 | 29/33 | True |
| B3-dpo marker | 0 | 24 | 11 | -0.0417 | 11 | -0.0417 | 2 / 2 | +0.0000 | 2 / 2 | 20/24 | True |
| B3-dpo marker | 1 | 24 | 16 | +0.1667 | 15 | +0.1250 | 3 / 2 | +0.0417 | 2 / 3 | 19/24 | True |
| B3-dpo marker | pooled | 48 | 27 | +0.0625 | 26 | +0.0417 | 5 / 4 | +0.0208 | 4 / 5 | 39/48 | True |
| B3-dpo sham | 0 | 8 | 4 | +0.0000 | 4 | +0.0000 | 0 / 0 | +0.0000 | 0 / 0 | 8/8 | True |
| B3-dpo sham | 1 | 10 | 4 | -0.1000 | 6 | +0.1000 | 0 / 2 | -0.2000 | 2 / 0 | 8/10 | True |
| B3-dpo sham | pooled | 18 | 8 | -0.0556 | 10 | +0.0556 | 0 / 2 | -0.1111 | 2 / 0 | 16/18 | True |
| B3-dpo random | 0 | 10 | 4 | -0.1000 | 6 | +0.1000 | 0 / 2 | -0.2000 | 0 / 2 | 8/10 | True |
| B3-dpo random | 1 | 8 | 2 | -0.2500 | 3 | -0.1250 | 0 / 1 | -0.1250 | 1 / 0 | 7/8 | True |
| B3-dpo random | pooled | 18 | 6 | -0.1667 | 9 | +0.0000 | 0 / 3 | -0.1667 | 1 / 2 | 15/18 | True |

Forced-order balance by map, as scheduled (all launched sessions, from each runner's schedule field: e2a `start_plus`, f1 `start_P`, B3 session-index parity) and as realized among valid sessions:

| arm | map | launched | launched starting on + | valid | valid starting on + |
|---|---|---|---|---|---|
| e2a reward | A | 56 | 28 | 53 | 26 |
| e2a reward | B | 56 | 28 | 49 | 23 |
| e2a sham | A | 20 | 12 | 18 | 10 |
| e2a sham | B | 20 | 12 | 19 | 11 |
| f1 CORR | A | 32 | 16 | 29 | 15 |
| f1 CORR | B | 32 | 16 | 27 | 12 |
| f1 sham | A | 20 | 12 | 14 | 8 |
| f1 sham | B | 20 | 12 | 19 | 12 |
| B3-dpo marker | 0 | 27 | 12 | 24 | 11 |
| B3-dpo marker | 1 | 26 | 15 | 24 | 15 |
| B3-dpo sham | 0 | 10 | 5 | 8 | 4 |
| B3-dpo sham | 1 | 11 | 6 | 10 | 6 |
| B3-dpo random | 0 | 11 | 7 | 10 | 6 |
| B3-dpo random | 1 | 9 | 3 | 8 | 3 |

Exact tests on the pooled break direction (pair[0] = the first-listed tag of each rotated pair: e2a granite, maple, plaza, slate; f1 granite, maple, plaza, slate; B3 amber, copper, maple, quartz), exact binomial two-sided vs ½ over habit-breaking sessions of the arm (domain: valid sessions that broke the habit). This is the pair[0] coordinate pooled over the four pairs; it sums breaks toward four different tags, and the per-pair table below shows what it hides:

| arm | breaks to pair[0] / pair[1] (pooled over pairs) | p (exact binomial, two-sided) |
|---|---|---|
| e2a reward | 11 / 5 | 0.2101 |
| e2a sham | 6 / 2 | 0.2891 |
| f1 CORR | 6 / 1 | 0.1250 |
| f1 sham | 4 / 0 | 0.1250 |
| B3-dpo marker | 4 / 5 | 1.0000 |
| B3-dpo sham | 2 / 0 | 0.5000 |
| B3-dpo random | 1 / 2 | 1.0000 |

First-free-pick reads by label identity and by menu position (domain: valid sessions of the arm; exact binomial, two-sided vs ½):

| arm | n | picked pair[0] | p | picked first-listed menu item | p | picked the start label (habit) |
|---|---|---|---|---|---|---|
| e2a reward | 102 | 58 | 0.1978 | 48 | 0.6208 | 86/102 |
| e2a sham | 37 | 22 | 0.3240 | 12 | 0.0470 | 29/37 |
| f1 CORR | 56 | 35 | 0.0814 | 27 | 0.8939 | 49/56 |
| f1 sham | 33 | 19 | 0.4869 | 16 | 1.0000 | 29/33 |
| B3-dpo marker | 48 | 19 | 0.1934 | 20 | 0.3123 | 39/48 |
| B3-dpo sham | 18 | 10 | 0.8145 | 11 | 0.4807 | 16/18 |
| B3-dpo random | 18 | 10 | 0.8145 | 2 | 0.0013 | 15/18 |

Is each capture's arm-level map split distinguishable from sampling noise on its own? Fisher exact, two-sided, on the 2×2 (map × first pick +label) pooled over the four pairs; and the positive map alone as a one-arm test (exact binomial P(X ≥ k | n, ½), one-sided, the registered direction). Domain: valid sessions of the arm, all pairs:

| capture arm | positive map k/n | other map k/n | Fisher two-sided p (maps differ; pooled over pairs) | positive map alone, one-sided exact binomial p |
|---|---|---|---|---|
| e2a reward | A: 32/53 | B: 23/49 | 0.2330 | 0.0845 |
| e2a sham | A: 11/18 | B: 8/19 | 0.3300 | 0.2403 |
| f1 CORR | A: 18/29 | B: 10/27 | 0.1078 | 0.1325 |
| B3-dpo marker | 1: 16/24 | 0: 11/24 | 0.2443 | 0.0758 |

**Per pair, capture arms (post-hoc; added at the round-2 values-check).** Domain: valid sessions of the arm in that pair. '+label share' is k/n of first picks to the +label in the map whose +label is pair[0] (e2a/f1 map A, B3 map 0) and in the map whose +label is pair[1] (map B / map 1). 'Started on t: broke/n' counts sessions that started on tag t and whose first free pick went to the other tag (a habit break), per map in the same order. p: exact binomial, two-sided vs ½, on first pick = pair[0]; Fisher: exact, two-sided, on the within-pair 2×2 (map × first pick +label). Every pair of every capture arm is listed, so no pair is selected silently; the reading below names maple/cedar because of what this table shows, which is a post-hoc selection (rule 11).

| arm | pair[0]/pair[1] | n | first pick pair[0] : pair[1] | p | +label share, map + = pair[0] | +label share, map + = pair[1] | Fisher p (maps, within pair) | started on pair[0]: broke/n (by map) | started on pair[1]: broke/n (by map) | breaks by tag |
|---|---|---|---|---|---|---|---|---|---|---|
| e2a reward | granite/lattice | 26 | 11 : 15 | 0.5572 | 5/13 | 7/13 | 0.6951 | 1/6; 1/7 | 0/7; 0/6 | granite 0, lattice 2 |
| e2a reward | maple/cedar | 21 | 20 : 1 | 2.1e-05 | 11/12 | 0/9 | 3.4e-05 | 0/6; 0/6 | 5/6; 3/3 | maple 8, cedar 0 |
| e2a reward | plaza/saddle | 27 | 10 : 17 | 0.2478 | 7/14 | 10/13 | 0.2365 | 0/7; 3/6 | 0/7; 0/7 | plaza 0, saddle 3 |
| e2a reward | slate/prism | 28 | 17 : 11 | 0.3449 | 9/14 | 6/14 | 0.4495 | 0/7; 0/7 | 2/7; 1/7 | slate 3, prism 0 |
| e2a sham | granite/lattice | 9 | 3 : 6 | 0.5078 | 1/4 | 3/5 | 0.5238 | 1/2; 0/2 | 0/2; 0/3 | granite 0, lattice 1 |
| e2a sham | maple/cedar | 10 | 10 : 0 | 0.0020 | 5/5 | 0/5 | 0.0079 | 0/3; 0/2 | 2/2; 3/3 | maple 5, cedar 0 |
| e2a sham | plaza/saddle | 9 | 4 : 5 | 1.0000 | 2/4 | 3/5 | 1.0000 | 0/2; 0/2 | 0/2; 0/3 | plaza 0, saddle 0 |
| e2a sham | slate/prism | 9 | 5 : 4 | 1.0000 | 3/5 | 2/4 | 1.0000 | 1/3; 0/2 | 1/2; 0/2 | slate 1, prism 1 |
| f1 CORR | granite/lattice | 16 | 7 : 9 | 0.8036 | 4/8 | 5/8 | 1.0000 | 0/4; 1/4 | 0/4; 0/4 | granite 0, lattice 1 |
| f1 CORR | maple/cedar | 13 | 12 : 1 | 0.0034 | 5/6 | 0/7 | 0.0047 | 0/3; 0/4 | 2/3; 3/3 | maple 5, cedar 0 |
| f1 CORR | plaza/saddle | 14 | 8 : 6 | 0.7905 | 4/7 | 3/7 | 1.0000 | 0/4; 0/4 | 0/3; 0/3 | plaza 0, saddle 0 |
| f1 CORR | slate/prism | 13 | 8 : 5 | 0.5811 | 5/8 | 2/5 | 0.5921 | 0/4; 0/3 | 1/4; 0/2 | slate 1, prism 0 |
| f1 sham | granite/lattice | 8 | 3 : 5 | 0.7266 | 2/4 | 3/4 | 1.0000 | 0/2; 0/1 | 0/2; 0/3 | granite 0, lattice 0 |
| f1 sham | maple/cedar | 10 | 9 : 1 | 0.0215 | 4/5 | 0/5 | 0.0476 | 0/3; 0/2 | 1/2; 3/3 | maple 4, cedar 0 |
| f1 sham | plaza/saddle | 9 | 4 : 5 | 1.0000 | 2/4 | 3/5 | 1.0000 | 0/2; 0/2 | 0/2; 0/3 | plaza 0, saddle 0 |
| f1 sham | slate/prism | 6 | 3 : 3 | 1.0000 | 1/1 | 3/5 | 1.0000 | 0/1; 0/2 | 0/0; 0/3 | slate 0, prism 0 |
| B3-dpo marker | amber/granite | 12 | 1 : 11 | 0.0063 | 1/6 | 6/6 | 0.0152 | 1/2; 0/0 | 0/4; 0/6 | amber 0, granite 1 |
| B3-dpo marker | copper/walnut | 12 | 8 : 4 | 0.3877 | 4/6 | 2/6 | 0.5671 | 0/2; 0/3 | 2/4; 1/3 | copper 3, walnut 0 |
| B3-dpo marker | maple/saddle | 10 | 8 : 2 | 0.1094 | 4/5 | 1/5 | 0.2063 | 0/4; 0/3 | 0/1; 1/2 | maple 1, saddle 0 |
| B3-dpo marker | quartz/velvet | 14 | 2 : 12 | 0.0129 | 2/7 | 7/7 | 0.0210 | 1/3; 3/3 | 0/4; 0/4 | quartz 0, velvet 4 |

**maple/cedar across all ten Qwen arms** (e2a random1, e2a random2, e2a reward, e2a sham, f1 CORR, f1 DIFF, f1 FDBK, f1 NOV, f1 SOLV, f1 sham; valid sessions; post-hoc, counts only, no test): maple was the first free pick in 103/113 maple/cedar sessions. Sessions that started on cedar broke the habit toward maple in 43/53: 17/26 in map A (maple = +label) and 26/27 in map B (maple = −label). Sessions that started on maple broke toward cedar in 0/60. In the other three pairs, 28/354 sessions broke the habit at all. The break follows the tag, not the pole, in both maps.

**Maps with maple/cedar removed, and maple/cedar alone (Qwen capture arms; post-hoc).** Δ = k/n − ½ over valid sessions of the arm and map in the other three pairs; breaks to + / to − in the same domain; the maple/cedar sessions alone pooled over both maps; and how many of the arm's breaks toward pair[0] (all pairs) went to maple:

| arm | map A k/n → Δ (no maple/cedar) | map B k/n → Δ (no maple/cedar) | opposite-signed | breaks to + / to − (A; B) | p (breaks + vs −, pooled over maps, exact binomial two-sided) | maple/cedar alone, pooled over maps | pair[0] breaks that went to maple |
|---|---|---|---|---|---|---|---|
| e2a reward | 21/41 → +0.0122 | 23/40 → +0.0750 | no | 2 / 1; 4 / 1 | 0.2891 | 11/21 → +0.0238 | 8 of 11 |
| e2a sham | 6/13 → -0.0385 | 8/14 → +0.0714 | yes | 1 / 2; 0 / 0 | 1.0000 | 5/10 → +0.0000 | 5 of 6 |
| f1 CORR | 13/23 → +0.0652 | 10/20 → +0.0000 | no | 1 / 0; 1 / 0 | 0.5000 | 5/13 → -0.1154 | 5 of 6 |
| f1 sham | 5/9 → +0.0556 | 9/14 → +0.1429 | no | 0 / 0; 0 / 0 | — | 4/10 → -0.1000 | 4 of 4 |

**B3 DPO marker, map 1 (the +0.1667 map) by pair (post-hoc).** Started on the +label = the forced-order term's numerator; map-1 breaks to + = its net-break term's positive part:

| pair | map-1 +label | n | started on +label | of those, first pick = +label | map-1 breaks to + |
|---|---|---|---|---|---|
| amber/granite | granite | 6 | 6 | 6 | 0 |
| copper/walnut | walnut | 6 | 3 | 2 | 0 |
| maple/saddle | saddle | 5 | 2 | 1 | 0 |
| quartz/velvet | velvet | 7 | 4 | 4 | 3 |

**The record's own identity measurement on Qwen: the H3 tag screen** (RESULTS.md@bbc9ffe:11254, 2026-08-20, after e2a's verdict at archive/RESULTS-cycles3-4.md@bbc9ffe:646 and f1's at :65; table row :11271). `data/e2b/h3_tagscreen.json` at the pin, scaffold format (the format of record), n = 16 restricted-choice probes per pair with menu order alternated; `identity_split` is the share taken by `tag_lo`, the alphabetically first tag (valence_core/tagscreen.py@bbc9ffe:78); band 0.5 ± 0.1. Its C pairs (C1 prism/slate, C2 cedar/maple, C3 granite/lattice, C4 plaza/saddle) are exactly e2a's and f1's four pairs (asserted). Recomputed from the per-probe rows with tagscreen's formula:

| H3 pair | tag_lo / tag_hi | identity_split (stored) | recomputed | match | imbalance | in band | tag_hi's share |
|---|---|---|---|---|---|---|---|
| C1 | prism / slate | 0.4809 | 0.4809 | YES | 0.0191 | yes | 0.5191 |
| C2 | cedar / maple | 0.2066 | 0.2066 | YES | 0.2934 | no | 0.7934 |
| C3 | granite / lattice | 0.4351 | 0.4351 | YES | 0.0649 | yes | 0.5649 |
| C4 | plaza / saddle | 0.4772 | 0.4772 | YES | 0.0228 | yes | 0.5228 |

**Reading (post-hoc, descriptive).**

- In every capture arm the first free pick follows the alternation habit in most sessions: e2a reward 86/102; e2a sham 29/37; f1 CORR 49/56; B3-dpo marker 39/48. A map's Δ therefore moves with two small quantities: which label the map's sessions started on, and which way the few habit breaks went.
- **Qwen captures (e2a, f1).** e2a reward map A +0.1038 = (-0.0094) (forced order) + (+0.1132) (net breaks, 7 to + vs 1 to −). e2a sham map A +0.1111 = (+0.0556) + (+0.0556); map B -0.0789 = (+0.0789) + (-0.1579) (breaks 0 to + vs 3 to −). f1 CORR map A +0.1207 = (+0.0172) + (+0.1034); map B -0.1296 = (-0.0556) + (-0.0741). The positive map (A) of the state arm and of CORR is carried mostly by the net-break term. In the e2a sham the forced-order term is positive in both maps because its schedule started more sessions on the +label in both (launched 12/20 and 12/20; 40 launched sessions, not a multiple of the 16-session (map x start) cycle); its map B goes negative through the breaks.
- **What carries the Qwen map splits: one tag pair (maple/cedar).** Pooled over the four pairs, the habit breaks lean toward pair[0] (e2a reward 11 vs 5; e2a sham 6 vs 2; f1 CORR 6 vs 1; f1 sham 4 vs 0; no count significant on its own), but the pair[0] coordinate sums breaks toward four different tags, and the per-pair table shows one tag doing the work: of those pair[0] breaks, maple took 8 of 11 (e2a reward), 5 of 6 (e2a sham), 5 of 6 (f1 CORR), 4 of 4 (f1 sham). Maple was the first free pick in 20/21 (e2a reward), 10/10 (e2a sham), 12/13 (f1 CORR), 9/10 (f1 sham) of these arms' maple/cedar sessions, so within maple/cedar the maps split hard (+label share in map A, where maple = +, vs map B, where maple = −: e2a reward 11/12 vs 0/9, Fisher two-sided p = 3.4e-05; e2a sham 5/5 vs 0/5, Fisher two-sided p = 0.0079; f1 CORR 5/6 vs 0/7, Fisher two-sided p = 0.0047; f1 sham 4/5 vs 0/5, Fisher two-sided p = 0.0476); no other pair's within-pair split in these four arms reaches .05 (smallest p = 0.2365). Across all ten Qwen arms the break follows the tag, not the pole (paragraph above the maple/cedar-removed table). With maple/cedar removed, the A-positive/B-negative pattern is gone from all three captures (e2a reward A +0.0122 / B +0.0750; e2a sham A -0.0385 / B +0.0714, opposite-signed the other way at n = 13/14; f1 CORR A +0.0652 / B +0.0000). The Qwen label artifact is therefore a measured tag-identity imbalance, maple over cedar, concentrated in one pair of four. The record measured that imbalance on Qwen, on restricted-choice probes rather than sessions, on 2026-08-20 (10 days after f1's verdict of 2026-08-10): H3's C2 maple/cedar, identity_split 0.2066 (cedar's share; maple 0.7934), imbalance 0.2934 against the ±0.1 band, the largest of e2a/f1's four pairs (RESULTS.md@bbc9ffe:11271; recomputed above). The label-map counterbalance turns the prior into opposite-signed maps and cancels most of it in the pooled Δ (maple/cedar sessions alone, pooled over maps: e2a reward 11/21 → +0.0238, e2a sham 5/10 → +0.0000, f1 CORR 5/13 → -0.1154, f1 sham 4/10 → -0.1000; the cancellation is exact only in expectation), which is the mechanism the record states for OLMo's prism prior: 'Only the label-MAP swap ... can absorb it' (RESULTS.md@bbc9ffe:12273-12275).
- **The state arm, separated by pair.** Of e2a reward's 16 habit breaks, 8 are maple/cedar sessions that started on cedar and broke to maple (5 toward + in map A, 3 toward − in map B). Outside maple/cedar its breaks go 2 to + vs 1 to − in map A and 4 vs 1 in map B: toward + in both maps, the direction a state effect would take, at 6 vs 2 (exact binomial, two-sided, p = 0.2891), too few to read. On the other three pairs both state-arm maps are ≥ 0 (+0.0122, +0.0750): a subset chosen after seeing the data, which re-reads no conjunct and moves no verdict (rule 11); conjunct (1), the envelope, and conjunct (3), the binomial, failed on the full arm regardless (section 3; archive/RESULTS-cycles3-4.md@bbc9ffe:652-658). The sham's no-state breaks toward pair[0] (A 3 vs 2, B 3 vs 0) are maple's (5 of 6), which is the record's disambiguating observation (the same pattern in sham) in decomposed form: the same tag prior in an arm with no state.
- **OLMo capture (B3 DPO).** The +0.1667 map is carried mostly by the forced-order term: 15 of its 24 valid sessions started on the +label, giving +0.1250 before any break, and the net breaks add +0.0417 (3 to + vs 2 to −). Map 1's forced-order imbalance is concentrated in one pair: all 6 of amber/granite's valid map-1 sessions started on granite (= +label) and picked it, against 9/18 starting on + in the other three pairs (table above). Read per pair, all 9 marker breaks (both maps) run one way within their pair: granite 1/1 (amber/granite), copper 3/3 (copper/walnut), maple 1/1 (maple/saddle), velvet 4/4 (quartz/velvet), which the pooled pair[0] coordinate (copper and maple are pair[0]) reads as 4 vs 5; the 3 map-1 breaks to the +label are all velvet's, and the tags that broke in both maps follow the tag, not the pole (copper: 2 to + in map 0, 1 to − in map 1; velvet: 1 to − in map 0, 3 to + in map 1). B3's start label is set by the parity of the arm's running session index (`scripts/box_b3_sessions.py@bbc9ffe:141`), while the cell (pair, map) comes from a seeded shuffle of the schedule, so within-map start balance is not enforced (launched marker map 1: 15/26 starting on +). e2a and f1 tie the start to s // 8 and the map to s // 4 (`jlens-qwen36/scripts/e2a_sessions.py:188`, `jlens-qwen36/scripts/f_sessions.py:278`), balanced per map in every 16 consecutive sessions. On this decomposition the DPO excursion is mostly a forced-order (start-label) imbalance under the alternation habit (forced-order term +0.1250 against a net-break term of +0.0417), and the residual break term is tag-specific (velvet), not absent. The record's conclusion -- an artifact, not a state effect -- is unaffected: the forced-order term is set by the schedule and by which sessions were excluded (map 1: launched 15/26, valid 15/24 starting on +), not by the first free choice; and the net-break term, which is where a state effect on the choice would appear, is +0.0417 in map 1 (3 vs 2) and +0.0000 in map 0 (2 vs 2), its breaks following tags rather than the +pole. Whether the note says 'label' or 'order' artifact is the design seat's wording.
- Taken one at a time, no capture's arm-level map split -- the test pooled over the four pairs -- is distinguishable from sampling noise at .05 (Fisher two-sided p: e2a reward 0.233, e2a sham 0.330, f1 CORR 0.108, B3-dpo marker 0.244). On Qwen that pooled test dilutes a within-pair effect that is distinguishable: maple/cedar's within-pair splits (Fisher p 3.4e-05 e2a reward, 0.0079 e2a sham, 0.0047 f1 CORR), with the same tag prior measured independently by H3's C2. So on Qwen 'label artifact' names a demonstrated within-campaign effect, a tag-identity prior, whose arm-level consequence (opposite-signed maps) the map counterbalance absorbs; what no single campaign demonstrates is a map effect pooled over pairs. At B3 DPO the within-pair splits below .05 (amber/granite p = 0.0152, quartz/velvet p = 0.0210) are, respectively, the start schedule (10 of amber/granite's 12 sessions started on granite) and velvet's breaks (4 of 4). The record classed all three captures by pattern and by the counterbalance's logic, not by a test; the preprint's 'caught by structure rather than by suspicion' remains the accurate description of how they were caught. The within-pair p values come from a table built after the pattern was seen (rule 11) and are descriptive.
- A single-map design at the positive map's own n would not have crossed one-sided α = .05 in any capture (exact binomial, one-sided: e2a reward 0.084, e2a sham 0.240, f1 CORR 0.132, B3-dpo marker 0.076). FINDINGS-3's 'an uncounterbalanced, sham-less version of this experiment would have published [it] as approach behavior' is a counterfactual about a full-n single-map run; it is not computable from these data and is not tested here.
- Multiplicity: this section ran 72 post-hoc exact tests, uncorrected; 14 fall below .05 (e2a sham first pick = first-listed menu item p = 0.0470; B3-dpo random first pick = first-listed menu item p = 0.0013; e2a reward maple/cedar first pick = pair[0] p = 2.1e-05; e2a reward maple/cedar Fisher maps differ (within pair) p = 3.4e-05; e2a sham maple/cedar first pick = pair[0] p = 0.0020; e2a sham maple/cedar Fisher maps differ (within pair) p = 0.0079; f1 CORR maple/cedar first pick = pair[0] p = 0.0034; f1 CORR maple/cedar Fisher maps differ (within pair) p = 0.0047; f1 sham maple/cedar first pick = pair[0] p = 0.0215; f1 sham maple/cedar Fisher maps differ (within pair) p = 0.0476; B3-dpo marker amber/granite first pick = pair[0] p = 0.0063; B3-dpo marker amber/granite Fisher maps differ (within pair) p = 0.0152; B3-dpo marker quartz/velvet first pick = pair[0] p = 0.0129; B3-dpo marker quartz/velvet Fisher maps differ (within pair) p = 0.0210). They are descriptive only and license nothing.

## 6. Context: every arm's map split in the three campaigns (computed-new count; stored maps re-verified)

| campaign | arm | maps (k/n → Δ) | opposite-signed | max abs map Δ | source |
|---|---|---|---|---|---|
| e2a | reward | A: 32/53 → +0.1038; B: 23/49 → -0.0306 | yes | 0.1038 | `data/e2a/analysis.json:reward.by_map` |
| e2a | sham | A: 11/18 → +0.1111; B: 8/19 → -0.0789 | yes | 0.1111 | `data/e2a/analysis.json:sham.by_map` |
| e2a | random1 | A: 9/11 → +0.3182; B: 6/12 → +0.0000 | no | 0.3182 | `data/e2a/analysis.json:random1.by_map` |
| e2a | random2 | A: 7/10 → +0.2000; B: 5/12 → -0.0833 | yes | 0.2000 | `data/e2a/analysis.json:random2.by_map` |
| f1 | SOLV | A: 15/26 → +0.0769; B: 11/24 → -0.0417 | yes | 0.0769 | `data/f/screen_analysis.json:contrasts.SOLV.by_map` |
| f1 | DIFF | A: 11/25 → -0.0600; B: 8/22 → -0.1364 | no | 0.1364 | `data/f/screen_analysis.json:contrasts.DIFF.by_map` |
| f1 | NOV | A: 14/27 → +0.0185; B: 9/26 → -0.1538 | yes | 0.1538 | `data/f/screen_analysis.json:contrasts.NOV.by_map` |
| f1 | CORR | A: 18/29 → +0.1207; B: 10/27 → -0.1296 | yes | 0.1296 | `data/f/screen_analysis.json:contrasts.CORR.by_map` |
| f1 | FDBK | A: 13/20 → +0.1500; B: 10/24 → -0.0833 | yes | 0.1500 | `data/f/screen_analysis.json:contrasts.FDBK.by_map` |
| f1 | sham | A: 9/14 → +0.1429; B: 9/19 → -0.0263 | yes | 0.1429 | `recomputed from data/f/sessions.jsonl` |
| B3-base | marker | 0: 10/24 → -0.0833; 1: 11/24 → -0.0417 | no | 0.0833 | `data/olmo/b3_analysis_base.json:by_label_map` |
| B3-base | sham | 0: 7/8 → +0.3750; 1: 4/10 → -0.1000 | yes | 0.3750 | `recomputed from data/olmo/b3_screen_base.json` |
| B3-base | random | 0: 5/10 → +0.0000; 1: 2/8 → -0.2500 | no | 0.2500 | `recomputed from data/olmo/b3_screen_base.json` |
| B3-sft | marker | 0: 11/23 → -0.0217; 1: 12/25 → -0.0200 | no | 0.0217 | `data/olmo/b3_analysis_sft.json:by_label_map` |
| B3-sft | sham | 0: 4/8 → +0.0000; 1: 5/10 → +0.0000 | no | 0.0000 | `recomputed from data/olmo/b3_screen_sft.json` |
| B3-sft | random | 0: 4/10 → -0.1000; 1: 3/8 → -0.1250 | no | 0.1250 | `recomputed from data/olmo/b3_screen_sft.json` |
| B3-dpo | marker | 0: 11/24 → -0.0417; 1: 16/24 → +0.1667 | yes | 0.1667 | `data/olmo/b3_analysis_dpo.json:by_label_map` |
| B3-dpo | sham | 0: 4/8 → +0.0000; 1: 4/10 → -0.1000 | no | 0.1000 | `recomputed from data/olmo/b3_screen_dpo.json` |
| B3-dpo | random | 0: 4/10 → -0.1000; 1: 2/8 → -0.2500 | no | 0.2500 | `recomputed from data/olmo/b3_screen_dpo.json` |
| B3-instruct | marker | 0: 11/23 → -0.0217; 1: 13/25 → +0.0200 | yes | 0.0217 | `data/olmo/b3_analysis_instruct.json:by_label_map` |
| B3-instruct | sham | 0: 5/8 → +0.1250; 1: 4/10 → -0.1000 | yes | 0.1250 | `recomputed from data/olmo/b3_screen_instruct.json` |
| B3-instruct | random | 0: 4/10 → -0.1000; 1: 2/8 → -0.2500 | no | 0.2500 | `recomputed from data/olmo/b3_screen_instruct.json` |

Of 22 arm-campaign cells, 12 have opposite-signed maps (one map > 0, the other < 0) and 17 have a map with abs(Δ_map) ≥ 0.10 (exact Fractions; 1 cell exactly at 0.10 -- B3-dpo sham; 16/22 with abs(Δ_map) > 0.10 strictly). Every stored map value re-verified from the session records: YES. Per-map valid n in these cells runs 8-53; the largest single-map abs(Δ) is 0.3750 (B3-base sham). Opposite-signed maps and single-map excursions of 0.10 or more are common at these n, in arms with and without a state. That is consistent with PROPOSAL-j's "A fourth capture is expected and is not a finding" (PROPOSAL-j-dose-escalation.md@bbc9ffe:290), which itself rests the expectation only on the three captures (:288); the 22-cell count is this audit's computed-new, not the record's basis. The three named captures are the ones the record discussed, not the only cells with that shape: e.g. e2a random1 (map A +0.3182, map B +0.0000) has one map carrying the pooled Δ at a larger magnitude than B3 DPO, and the record read random1's pooled +0.152 as "noise doing its criterion job" (archive/RESULTS-cycles3-4.md@bbc9ffe:684-685).

## 7. Notes (referents and wording; none is a STOP)

1. **The heading 'sham-arm pseudo-statistics' fits capture 1 only.** f1 CORR is a contrast arm and B3 DPO the marker arm (sections 1, 3). The three are the record's label-artifact captures (PROPOSAL-j-dose-escalation.md@bbc9ffe:288); the sham arm's own map split for f1 and B3 is reported beside them as computed-new.
2. **Preprint wording (PREPRINT-v1_0-draft.md, untracked working-tree file, sha256 d6431e97d35e5914574ff9884c0e64463a7baf1cf9d279f27ed45a683a6222b8, equal to the block's d6431e97...222b8; line numbers are working-tree, not pinned; PREPRINT-v1_1-draft.md and the note are absent from this machine).** (a) :190 'appears identically in the sham arm' -- the sign pattern recurs; the magnitudes do not (state B -0.0306 vs sham B -0.0789). FINDINGS-3's 'identical pattern' has the same scope. Suggested: 'the same A-positive/B-negative pattern'. (b) 'cancelled to 0.000 by construction' (:190) -- the pooling is by construction; the exact zero is the realized counts (18/29 and 10/27; section 1). The record's own wording is 'absorbed by design' (archive/RESULTS-cycles3-4.md@bbc9ffe:83). (c) :190 'In the OLMo DPO screen one map returned +0.1667' -- reproduced; the other map is -0.0417 (11/24).
3. **PROPOSAL-h §1 cites the f1 mirror-cancel as the 'receipt' that the map counterbalance absorbs the injected vector's token-level logit leak** (PROPOSAL-h-state-present-choice.md@bbc9ffe:63-68). f1 injected nothing in any arm (section 2 locators). What the receipt does show: a label-locked lean with no state behind it cancels under the map swap, which is the structural property §1 relies on (a push that lands on the same token for opposite meanings). f1 CORR's opposite-signed maps are, by construction, a lean toward the pair's first-listed tag in both maps: the first free pick went to pair[0] in 35/56 valid sessions (exact binomial, two-sided vs ½, p = 0.0814) and its habit breaks went 6 vs 1 toward pair[0] (section 5; part of map B's excursion is the forced-order term, -0.0556). The lean is one tag's: maple was the first pick in 12/13 of CORR's maple/cedar sessions and took 5 of the 6 pair[0] breaks (section 5, per-pair table), so the receipt is a tag-identity prior cancelling, which is the same structural property. What it does not show is the size or form of a vector-borne push; §1 itself assigns that calibration to H1 (:68, "H1 measures the residual"). A design-seat note on the receipt's scope, not a record error in any figure.
4. **Rule 12's 'captured live twice'** (CLAUDE.md@bbc9ffe:313-314) predates capture 3: `git log -S` puts the phrase into CLAUDE.md at c07a5e0 2026-08-12 and the B3 entry into RESULTS.md at 720a104 2026-08-24. PROPOSAL-j's three is current (section 4).
5. **The ~0.10 scale.** Largest |Δ_map| per capture arm: e2a reward 0.1038, e2a sham 0.1111, f1 CORR 0.1296, B3 DPO marker 0.1667. 'Δ ≈ 0.10 scale' fits the Qwen captures; the OLMo map is 0.1667, which the B3 entry calls 'the size rule 12 names as first-order (~0.10)'. At n = 24 per map one session moves a map Δ by 0.0417. The ~0.10 itself is a prose scale in the record (FINDINGS-3.md@bbc9ffe:87, RESULTS.md@bbc9ffe:7678, CLAUDE.md@bbc9ffe:314, PROPOSAL-j-dose-escalation.md@bbc9ffe:288), not a stored field; only the per-arm maxima above are this audit's.
6. **Cross-reference.** The e2a figures here are the same fields N4 reproduces (`results/raw/2026-10-08_note-N4-e2a.md`, section (i-f)); the f1 pooled CORR figure is N5's; the B3 DPO figures are N7's. This raw recomputes all of them independently from the pinned session records. f1 CORR's delivery: N5 section 7 ('The CORR contrast's dose', `results/raw/2026-10-08_note-N5-f1.md`, a sibling raw of this audit, not at the pin) reports that at rate .12 two of the 16 CORR items rendered unchanged, so clean text reached some corrupted-label rounds; this script's check of the stored task field (stored at most 40 characters; equal to a `CORR_clean` item of `data/f/pools.json` on that prefix) agrees: 40 of 306 Q rounds across all 64 CORR sessions, items [1, 12], and 16 of the 56 valid sessions saw one corrupted forced task rather than two. It moves no figure here; the CORR map split is maple-carried (section 5).
7. **For the PI and the design seat (post-hoc throughout; no verdict moves).** The note's 'what the shields caught' can name the Qwen source concretely: a maple-over-cedar identity prior in one of e2a's and f1's four pairs (section 5), the prior the record measured independently with H3 (C2, RESULTS.md@bbc9ffe:11271). The H3 entry's 'no published preference number is impeached by an identity prior on its own tags' (RESULTS.md@bbc9ffe:11279-11281) rests on slate/prism alone (its basis, :11276-11279), while e2a's and f1's rosters also carried maple/cedar, 'order-counterbalanced but never screened' and 'not admitted' (PROPOSAL-j-dose-escalation.md@bbc9ffe:359-361). The pooled Δs stand: they are map-counterbalanced, and e2a and f1 are nulls. What the prior did is produce the opposite-signed maps the record called the label artifact, and leave the maple/cedar sessions' first picks near-fixed by the tag (maple 20/21 in the state arm), the case the record's OLMo entry describes as a prior that 'spends power the contrast needs' (RESULTS.md@bbc9ffe:12275-12277). Whether the H3 sentence's scope is restated is the design seat's call.

## Figures (feeds N1's claims ledger)

| figure as the block writes it | value printed | source | status | note |
|---|---|---|---|---|
| e2a sham +0.111 (map A) | 11/18 → +0.1111 | `data/e2a/analysis.json:sham.by_map.A` | reproduced | Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records |
| e2a sham −0.079 (map B) | 8/19 → -0.0789 | `data/e2a/analysis.json:sham.by_map.B` | reproduced | Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records |
| e2a state +0.104 (map A) | 32/53 → +0.1038 | `data/e2a/analysis.json:reward.by_map.A` | reproduced | Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records |
| e2a state −0.031 (map B) | 23/49 → -0.0306 | `data/e2a/analysis.json:reward.by_map.B` | reproduced | Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records |
| f1 CORR +.121 (map A) | 18/29 → +0.1207 | `data/f/screen_analysis.json:contrasts.CORR.by_map.A` | reproduced | Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records |
| f1 CORR −.130 (map B) | 10/27 → -0.1296 | `data/f/screen_analysis.json:contrasts.CORR.by_map.B` | reproduced | Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records |
| OLMo DPO +0.1667 single map | 16/24 → +0.1667 | `data/olmo/b3_analysis_dpo.json:by_label_map.1` | reproduced | Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records |
| OLMo DPO other map (block: 'the other map's figure beside it') | 11/24 → -0.0417 | `data/olmo/b3_analysis_dpo.json:by_label_map.0` | reproduced | Δ_map = k/n − ½ over valid sessions of the map; recomputed from session records |
| e2a reward pooled | 55/102 → +0.0392 | `data/e2a/analysis.json:reward.delta_first` | reproduced | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; frozen-audit domain; N4 reproduces the same field |
| e2a sham pooled | 19/37 → +0.0135 | `data/e2a/analysis.json:sham.delta_first` | reproduced | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; frozen-audit domain; N4 reproduces the same field |
| f1 CORR pooled 0.000 (maps mirror-cancel) | 28/56 → +0.0000 | `data/f/screen_analysis.json:contrasts.CORR.delta; prose archive/RESULTS-cycles3-4.md@bbc9ffe:82` | reproduced | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; the record's figure (N5's, block line 98); the exact zero is the realized counts, not the design (note 2b) |
| f1 sham pseudo-Δ .045 | 18/33 → +0.0455 (stored as absolute value) | `data/f/screen_analysis.json:sham_pseudo; prose archive/RESULTS-cycles3-4.md@bbc9ffe:85` | reproduced | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; the record's figure ('Sham pseudo-Δ = .045.'), f1's control envelope |
| OLMo DPO marker pooled | 27/48 → +0.0625 | `data/olmo/b3_analysis_dpo.json:delta_first` | reproduced | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture |
| OLMo DPO sham pooled | 8/18 → -0.0556 | `data/olmo/b3_analysis_dpo.json:controls.sham.pseudo_delta` | reproduced | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture |
| OLMo DPO random pooled | 6/18 → -0.1667 | `data/olmo/b3_analysis_dpo.json:controls.random.pseudo_delta` | reproduced | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture |
| f1 sham map A (sham/random beside the capture) | 9/14 → +0.1429 | `recomputed from data/f/sessions.jsonl (no stored by-map field for sham)` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; no stored by-map field for this arm |
| f1 sham map B (sham/random beside the capture) | 9/19 → -0.0263 | `recomputed from data/f/sessions.jsonl (no stored by-map field for sham)` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; no stored by-map field for this arm |
| B3-dpo sham map 0 (sham/random beside the capture) | 4/8 → +0.0000 | `recomputed from data/olmo/b3_screen_dpo.json (by-map not stored for controls)` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; no stored by-map field for this arm |
| B3-dpo sham map 1 (sham/random beside the capture) | 4/10 → -0.1000 | `recomputed from data/olmo/b3_screen_dpo.json (by-map not stored for controls)` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; no stored by-map field for this arm |
| B3-dpo random map 0 (sham/random beside the capture) | 4/10 → -0.1000 | `recomputed from data/olmo/b3_screen_dpo.json (by-map not stored for controls)` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; no stored by-map field for this arm |
| B3-dpo random map 1 (sham/random beside the capture) | 2/8 → -0.2500 | `recomputed from data/olmo/b3_screen_dpo.json (by-map not stored for controls)` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); beside the capture; no stored by-map field for this arm |
| three live captures across two models | e2a sham (Qwen), f1 CORR (Qwen), B3 DPO marker (OLMo): consistent | `PROPOSAL-j-dose-escalation.md@bbc9ffe:288` | log-only | the block writes 'the three captures'; 'across two models' is PROPOSAL-j's; a count in design prose; the three cells reproduce |
| e2a: 'label/order artifact correctly absorbed by counterbalancing' | classification (prose) | `archive/RESULTS-cycles3-4.md@bbc9ffe:655-658` | log-only | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); the record's classification; basis: same sign pattern in the no-state arm; post-hoc (section 5): concentrated in maple/cedar, a tag-identity prior (H3 C2) |
| f1: 'maps +.121/−.130 mirror-cancel -- the label artifact absorbed by design' | classification (prose) | `archive/RESULTS-cycles3-4.md@bbc9ffe:82-84` | log-only | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); the record's classification; post-hoc (section 5): concentrated in maple/cedar, a tag-identity prior (H3 C2) |
| B3 DPO: 'label artifact, not a state effect' | classification (prose) | `RESULTS.md@bbc9ffe:7673-7681` | log-only | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); the record's classification; post-hoc decomposition (section 5): mostly forced-order imbalance under the alternation habit (concentrated in amber/granite); residual break term tag-specific (velvet) |
| Δ ≈ 0.10 scale (rule 12; preprint §5.6) | ≈ 0.10 / ~0.10 (prose scale) | `FINDINGS-3.md@bbc9ffe:87; RESULTS.md@bbc9ffe:7678; CLAUDE.md@bbc9ffe:314; PROPOSAL-j-dose-escalation.md@bbc9ffe:288` | log-only | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); a scale stated in prose, no stored field; the per-capture maxima are the next row |
| largest abs map Δ per capture arm (beside the ~0.10 scale) | e2a reward 0.1038, e2a sham 0.1111, f1 CORR 0.1296, B3 DPO marker 0.1667 | `section 1 cells` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); the OLMo map is above 0.10 (note 5) |
| maps differ beyond noise, arm level (not a record figure; asked of 'what the shields caught') | Fisher two-sided p, pooled over pairs: e2a reward 0.233, e2a sham 0.330, f1 CORR 0.108, B3-dpo marker 0.244 | `section 5` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); post-hoc; 0 of 4 below .05; the pooled-over-pairs test; the record's classification is by design logic, not by test |
| maps differ within maple/cedar (Qwen capture arms) | Fisher two-sided p: e2a reward 11/12 vs 0/9 3.4e-05, e2a sham 5/5 vs 0/5 0.0079, f1 CORR 5/6 vs 0/7 0.0047, f1 sham 4/5 vs 0/5 0.0476 | `section 5 per-pair table` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); post-hoc, pair named after the table was seen (rule 11); every pair of every capture arm is tabulated; no other Qwen pair below .05 |
| maple first free pick (Qwen) | e2a reward 20/21, e2a sham 10/10, f1 CORR 12/13, f1 sham 9/10; all ten Qwen arms 103/113; cedar-start → maple 43/53 (17/26 maple = +, 26/27 maple = −); maple-start → cedar 0/60 | `section 5` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); post-hoc, descriptive |
| Qwen maps with maple/cedar removed | e2a reward A +0.0122 / B +0.0750; e2a sham A -0.0385 / B +0.0714; f1 CORR A +0.0652 / B +0.0000 | `section 5` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); post-hoc subset; re-reads no conjunct (rule 11) |
| H3 C2 maple/cedar on Qwen: identity_split 0.207, imbalance 0.293 (scaffold) | 0.2066 (cedar's share; recomputed 0.2066); imbalance 0.2934 | `data/e2b/h3_tagscreen.json:pairs[C2].formats.scaffold; prose RESULTS.md@bbc9ffe:11271` | reproduced | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); the record's measurement, cited at the round-2 values-check; identity_split recomputed from the per-probe rows; the prose's 3-dp values match |
| B3 DPO marker breaks per pair | granite 1/1 (amber/granite), copper 3/3 (copper/walnut), maple 1/1 (maple/saddle), velvet 4/4 (quartz/velvet) (pair[0] coordinate 4 vs 5) | `section 5` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); post-hoc, descriptive |
| forced-order / net-break decomposition per map | section 5 table | `habit.py identity on session records` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); post-hoc, descriptive |
| opposite-signed maps across the three campaigns | 12/22 arm cells; 17/22 with a map abs(Δ) ≥ 0.10 (16/22 strictly > 0.10; exactly at 0.10: B3-dpo sham) | `section 6` | computed-new | not in N14's block text (AUDIT-note-release-v1_2.md@bbc9ffe:116); consistent with PROPOSAL-j's 'a fourth capture is expected' (PROPOSAL-j-dose-escalation.md@bbc9ffe:290), which does not rest on this count |

## STOPs

None. Every stored figure the block names reproduces exactly from the pinned session records; no analyzer change is needed for any of them.

## Values-check

Pass 1 (independent checker; its own scratch code read the pinned artifacts through `git show`): 165 claims checked; every independent recomputation agreed (all 8 block map figures, 7 pooled figures, the computed-new sham/random maps, the 22-cell context table, every decomposition row with the pinned habit.py, the start-balance table and all post-hoc exact tests); the redaction check was clean. Eight minor findings, none changing a number or a status. Each was re-checked against the pinned record by a tool run before it was applied; none was rejected.

| # | finding | disposition | what changed |
|---|---|---|---|
| 1 | f1 'no injection' locator PROPOSAL-f:17 is the §0 heading; the explicit line is :27 | fixed | section 2 now cites PROPOSAL-f-natural-reinforcer-screen.md@bbc9ffe:27 ("Nothing is injected"), with the §0 heading at :17; anchor searched, not typed |
| 2 | four Figures rows (e2a reward/sham pooled, f1 CORR pooled 0.000, f1 sham .045) read as block figures; .045 had no record locator | fixed | every row that N14's block text (:116) does not write now says so in its note (applied to all such rows, not only the four); f1 CORR 0.000 carries archive/RESULTS-cycles3-4.md@bbc9ffe:82 and N5's block line 98; f1 sham .045 carries archive/RESULTS-cycles3-4.md@bbc9ffe:85 |
| 3 | note 3 overstated: the f1 receipt does show a label-locked push cancelling under the swap; what it lacks is the size/form of a vector-borne push | fixed | note 3 reworded to that scope, with the lean computed here (pair[0] 35/56, p = 0.0814 two-sided; breaks 6 vs 1) and §1's own H1 clause (:68); the forced-order share of map B disclosed |
| 4 | section 6 called the 22-cell count 'the premise of' PROPOSAL-j's 'a fourth capture is expected' | fixed | now 'consistent with'; adds that PROPOSAL-j rests the expectation on the three captures (:288) and that the count is computed-new |
| 5 | 17/22 includes a cell exactly at 0.10 (B3-dpo sham); 16/22 under a strict '>' | fixed | max abs map Δ now compared as exact Fractions; section 6 and the Figures row print 17/22 ≥ 0.10, 16/22 > 0.10, cells exactly at 0.10: B3-dpo sham |
| 6 | missing locators for the CORR target direction and B3's 48:18:18 targets | fixed | PROPOSAL-f-natural-reinforcer-screen.md@bbc9ffe:86 (CORR table row); targets 48:18:18 and per_stratum 6:3:3 now read from `data/olmo/b3_screen_dpo.json:targets` / `:per_stratum` at the pin and printed |
| 7 | e2a domain sentence does not say which audit (frozen vs v2) the map figures use | fixed | section 1 states the frozen audit (stored `excluded` flag; exclusions per arm printed from the pinned records) with scripts/e2a_recount.py@bbc9ffe:120; Code also ran `jlens-qwen36/.venv/bin/python scripts/e2a_recount.py` from the repository root with the root on PYTHONPATH (read-only, writes nothing; it reads the working tree's data/e2a/sessions.jsonl, EQUAL to the pin per section 0), which printed 'session set identical = True; every reason string identical = True' for the frozen audit and 55/102 (frozen) / 54/101 (v2), both '[MATCHES the record]' |
| 8 | JSON header has no exact command | fixed | J['command'] added (the same string as the raw's Command line) |

Round 2 (tier-2 residual findings, applied by Code; each re-verified by a tool run before it was applied; none rejected):

| # | severity | finding | disposition | verified by | what changed |
|---|---|---|---|---|---|
| R2-1 | substantive | section 5's Qwen reading ('habit breaks lean toward pair[0]'; 'cannot be separated at these counts'; 'should not be read as a demonstrated effect in any single campaign') is misleading for the two Qwen captures: the pooled pair[0] coordinate hides one strong tag preference, maple over cedar, which the record measured (H3 C2) and N14 did not cite | fixed | every count in the finding reproduced, first by Code's own scratch code (pinned artifacts via git show), then by this script: maple first 20/21 (e2a reward, p = 2.1e-05), 10/10 (e2a sham), 12/13 (f1 CORR); within-pair Fisher 3.4e-05, 0.0079, 0.0047; ten arms 103/113; cedar-start → maple 43/53 (17/26, 26/27); maple-start → cedar 0/60; other pairs 28/354; maps without maple/cedar and maple's share of the pair[0] breaks as the finding states; H3 C2 identity_split 0.2066 = cedar's share (tag_lo) per valence_core/tagscreen.py@bbc9ffe:78, recomputed from the per-probe rows. Two refinements from the pinned text: PROPOSAL-j's sentence is at :359-361 (the finding cited 360-363); and with maple/cedar removed e2a sham's maps are still opposite-signed, the other way (A -0.0385, B +0.0714), so the raw says the A-positive/B-negative pattern is gone rather than that opposite signs are | section 5 gains a per-pair table for every pair of every capture arm (first pick by tag with exact binomial p; +label share by map with within-pair Fisher p; breaks by start tag and map; breaks by tag), the maple/cedar paragraph over all ten Qwen arms, a maps-without-maple/cedar table (with maple/cedar alone pooled over maps and maple's share of the pair[0] breaks), and the H3 C pairs recomputed; the Qwen bullets are rewritten (the label artifact is a measured tag-identity imbalance, maple over cedar, H3 C2 at RESULTS.md@bbc9ffe:11271, concentrated in one pair of four, which the map counterbalance turns into opposite-signed maps and mostly cancels); 'cannot be separated at these counts' is replaced by the per-pair separation of the state arm; 'should not be read as a demonstrated effect in any single campaign' is dropped; the arm-level Fisher table and Figures row now say they are the pooled-over-pairs test; note 7 (PI/design seat) names the source and the H3 sentence's slate/prism-only basis (RESULTS.md@bbc9ffe:11279-11281); note 3 says the receipt's lean is maple's; the e2a/f1 classification rows carry the post-hoc pointer. Post-hoc test count 72 (was 29), every one listed when below .05. Rule 11 stated at each step; no verdict moves |
| R2-2 | minor | B3 DPO: 'its breaks do not lean toward pair[0] (4 vs 5 pooled)' and 'rather than a label-identity preference' hide per-pair breaks that all run one way | fixed | this script: granite 1/1 (amber/granite), copper 3/3 (copper/walnut), maple 1/1 (maple/saddle), velvet 4/4 (quartz/velvet); pair[0] coordinate 4 vs 5; map-1 breaks to + all velvet; amber/granite map 1 6/6 started on granite (+label) and 6 picked it; forced-order +0.1250 vs net-break +0.0417; base quartz/velvet first pick quartz 0/12 (B3-base marker; verified, not added to the body because base is not a capture arm) | the B3 bullet now gives the per-pair break statement, the amber/granite concentration of map 1's forced-order term and a per-pair map-1 table; 'mostly forced-order' kept with the exact terms; 'rather than a label-identity preference' replaced by 'the residual break term is tag-specific (velvet), not absent'; the B3 classification row's note updated |
| R2-3 | minor | section 6 cites the random1 'noise doing its criterion job' phrase at :684; it spans two lines | fixed | git show bbc9ffe:archive/RESULTS-cycles3-4.md lines 684-685; the script now asserts the phrase's end is on the second line | cited as archive/RESULTS-cycles3-4.md@bbc9ffe:684-685 |
| R2-4 | minor | Figures row 'Δ ≈ 0.10 scale' is marked computed-new, but the ~0.10 is a record prose figure | fixed | anchors searched in the pinned text: FINDINGS-3.md:87, RESULTS.md:7678, CLAUDE.md:314, PROPOSAL-j-dose-escalation.md:288; the maxima reproduce (0.1038, 0.1111, 0.1296, 0.1667) | the row is now log-only with the four locators; the per-capture maxima are a separate computed-new row; note 5 carries the locators |
| R2-5 | minor | N14 does not point to N5's CORR delivery artifact (clean text in corrupted-label rounds at rate .12) | fixed | this script's check of the stored task field against `data/f/pools.json:CORR_clean` at the pin: 40/306 Q rounds, items [1, 12], 16/56 valid sessions with one corrupted forced task, as N5 reports | note 6 points to N5 section 7 by heading (N5's raw is an untracked sibling still under revision, so no line number is cited) with the corroborated counts; no N14 number moves |

