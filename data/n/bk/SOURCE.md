# BK's replication files, read as data

**Attribution.** Berg, C. & Kaiser, C. (2026). *Language Models Act on Hidden Valence*. arXiv:2609.35591 v2.
Replication files from the authors' repository, github.com/camberg23/act-on-valence, at commit
`7631f8a06cdeffaf8b7a89212e5ccbe55a657732` (tree `d6f1d50525874355d1ea992f8f652358742ae282`, committed 2026-10-05),
licensed CC BY 4.0. BK's license notice, which links the CC BY 4.0 legal code, is `LICENSE` in this folder, copied
unmodified.

**What is here.** 26 files, each a byte-for-byte copy at the authors' own repository path, unmodified. `SHA256SUMS`
lists each file's sha256; `shasum -a 256 -c SHA256SUMS` run from this folder checks them. The set is PROPOSAL-n
v0.2's G-DATA (ii) list plus `LICENSE`:

- the 160 neutral OLMo-2-32B Instruct session records, in 14 skeleton files
  (`experiment_results_json/fixed_text_design/skeletons/olmo_32b/neutral/`: `floor_b0`–`floor_b7`, 5 records each;
  `neu_b0`–`neu_b5`, 20 records each);
- `experiment_results_csv/`: `figure3.csv`, `figure4.csv`, `figureA8.csv`, `figureA10.csv`, `table1_banks.csv`;
- `experiment_results_json/fixed_text_design/neutral_passages/`: `reduced.json`, `prereg.json`, `analysis.json`,
  `spec.json`;
- `experiment_results_json/fixed_text_design/strength_ladder/`: `analysis.json`, `spans.json`.

**How they are used.** As inputs to PROPOSAL-n, this program's reconciliation unit. Nothing in them is executed.
Copied by Code at PROPOSAL-n v0.2 §8 step 3 (2026-11-06); G-DATA (ii) re-verifies these hashes against a fresh clone
at the same commit.
