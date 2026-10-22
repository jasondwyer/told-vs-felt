# note-N2(vii) — three confirmations against arXiv:2603.21396v5 (the PDF)

- Code stamp: Thu Oct 22 03:49:17 UTC 2026 (date -u)
- HEAD at run: b991bd5c6dbfac480220412e07ee8a4c162d0f05 (no repository file is read below; the source is the PDF alone)
- Block: "2. DESIGN → CODE · 2026-10-21 · note-N2(vii): three confirmations against arXiv:2603.21396v5", routed by the PI in a laptop session on 2026-10-21; not a committed file. Read-only.
- Source: Macar, Yang, Wang, Wallich, Ameisen, Lindsey, "Mechanisms of Introspective Awareness", arXiv:2603.21396v5. arXiv lists v5 as "Wed, 10 Jun 2026 08:55:42 UTC (22,204 KB)"; license CC BY 4.0 (the abs page's "view license" link, read with WebFetch). The PDF's margin stamp reads "arXiv:2603.21396v5 [cs.LG] 10 Jun 2026".
- Acquisition: `curl -sSL https://arxiv.org/pdf/2603.21396v5` with the PI's in-session approval (WebFetch refused the file: over its 10 MB limit). HTTP 200; 27,590,572 bytes; sha256 `90c0af7497e76c44c6518dd9c8a352d9a549c6748ac21a65a31ff6077e640f92`. Kept in the session scratchpad and not committed; the hash identifies it.
- Extraction: macOS PDFKit (macOS 15.6.1, build 24G90) through two Swift 6.1 scripts, reproduced in §4. `pdfdump` gives the text layer, 50 pages, sha256 `b53057afcf8f2281a32c431c6c2c5fa27869089f591f3324a8763578a0e30d52`. `pdfrender` renders pages to PNG. Pages 1, 2, 4, 5, 7, 10, 22, 23, 25, 27 and 28 were rendered at 2×, and the Table 3 caption, the Figure 5 caption and Figure 1's refusal panel at 4×. Every quotation below was read by eye on the render as well as found in the text layer. The one exception, Figure 1's panel, is raster with no text layer, so it was read on the render only.
- Quote check: a scratchpad script, not committed, matched every quoted string and every Table 3 row in §§1–3 against the text layer. Matching ignores whitespace and is case-insensitive for the small-caps headings. The §3 sentence was split at the p. 4/5 page break, where footnote 2 falls in the text layer. All were found except three items that are not in the text layer: the Figure 5 legend and the Figure 1 panel (raster, read by eye) and N2(vi)'s own wording (not a source quote).
- Locator convention: "p." is the PDF page; on every page cited, the PDF page equals the printed folio. "Line k" counts typeset lines within the named paragraph, caption or list item, on the render. Superscript asterisks are written `*`, and minus signs are given as printed (−).
- Scope: v5 only. v1–v4 were not re-read. This raw contains no analysis and changes no note sentence or figure. RESULTS entry: none. The note arc's raws were committed without RESULTS.md entries (09c3a8c, fa1b41e and 11cc35b leave RESULTS.md untouched), and this raw follows that practice.

## 1. (a) Table 3

**Locator.** p. 5, §3.3 "The Role of Post-Training". The table is placed at the foot of the page. It is cited in the text at p. 5, in the paragraph after Figure 5 ("To understand which component of DPO is responsible …"), lines 2–3: "(Table 3; training details in Appendix D.3)".

**Caption** (3 lines, verbatim):
> Table 3: LoRA finetuning OLMo-3.1-32B SFT checkpoint with different training conditions. Introspection metrics are from L = 25 and α = 4. Rows annotated with * are official checkpoints. Introspection (%) = P(detected ∧ injected | injected). Ordered by TPR − FPR.

**Columns** (header row, verbatim): `Condition` | `TPR − FPR (%)` | `Introspection (%)`

**Rows: eleven.** The render and the text layer agree. The Digest's count of eleven holds. Rows are listed in printed order:

| # | Condition | TPR − FPR (%) | Introspection (%) |
|---|---|---|---|
| 1 | Margin + KL | +14.3 ± 1.6 | 6.8 ± 1.1 |
| 2 | DPO standard | +14.4 ± 1.6 | 7.0 ± 0.8 |
| 3 | DPO no-reference | +12.8 ± 2.1 | 5.8 ± 1.0 |
| 4 | DPO* | +9.8 ± 0.5 | 3.5 ± 0.3 |
| 5 | DPO on base (no SFT) | +8.4 ± 1.4 | 2.4 ± 0.7 |
| 6 | DPO shuffled | +0.6 ± 2.8 | 3.6 ± 0.8 |
| 7 | SFT* | −11.5 ± 2.4 | 1.7 ± 0.2 |
| 8 | SFT on chosen | −13.5 ± 3.6 | 4.6 ± 0.9 |
| 9 | SFT on chosen + KL | −15.6 ± 3.6 | 4.8 ± 1.0 |
| 10 | SFT on rejected | −16.2 ± 3.6 | 4.6 ± 0.9 |
| 11 | DPO reversed | −21.8 ± 3.2 | 1.0 ± 0.4 |

**The four rows asked.** Each is confirmed as printed, at L = 25 and α = 4 (caption, line 2):
- DPO shuffled +0.6 ± 2.8 (row 6)
- DPO reversed −21.8 ± 3.2 (row 11)
- SFT* −11.5 ± 2.4 (row 7)
- DPO* +9.8 ± 0.5 (row 4)

The two starred values also appear in Table 8 (p. 27, Appendix D.2, left half, "metrics from L = 25 and α = 4"): SFT* −11.5 ± 2.4 and DPO* +9.8 ± 0.5.

**The column.** The column is the quantity TPR − FPR, in percent. The unit is "(%)" in the header. The text uses it the same way: p. 5, the paragraph after Figure 5, line 4: "(+12.8%; measured as TPR − FPR)". TPR and FPR are defined in the metric table of §2 "Experimental Setup" (p. 2, the table after the section's single paragraph):
- "Detection rate (TPR) | P(detect | injection)"
- "False positive rate (FPR) | P(detect | no injection)"

**± in the table.** The caption does not say what ± denotes.

**An introspection rate beside each row.** Yes. All eleven rows carry a value in the `Introspection (%)` column. The definition is printed three ways, quoted as printed with no reading taken:
- Table 3 caption, line 3: "Introspection (%) = P(detected ∧ injected | injected)".
- §2 metric table, p. 2: "Introspection rate | P(detect ∧ identify | injection)".
- Figure 5 legend, p. 5 (raster): "P(detect ∧ identified | injected)".

**Printed order** (fact of the page, no inference drawn). The caption says "Ordered by TPR − FPR." Rows 1–2 print +14.3, then +14.4.

**Definitions of the non-starred conditions.** Appendix D.3 "Training Condition Details", p. 28, gives one bullet per condition. "DPO shuffled" is bullet 3 ("for each pair the chosen or rejected assignment is randomized (50% swap probability)"). "DPO reversed" is bullet 4 ("chosen and rejected are swapped for every pair").

## 2. (b) Concept count, and n for the OLMo rates

**50 concepts for OLMo.** v5 states the count in two places:
- p. 5, §3.3, Figure 5 caption, line 2 of 3: "Values are reported for the original 50 concepts from Lindsey (2025)." Figure 5 is the OLMo-3.1-32B base/SFT/DPO/instruct figure at L = 25 and α ∈ {1, 2, 4, 8}.
- p. 27, Appendix D.1, Figure 22 caption, line 3 of 3: "Results are given for the original 50 concepts from Lindsey (2025)." Figure 22 is the same figure at L = 19 and L = 22.

**500 concepts, paper-wide default.**
- p. 22, Appendix B.1 "Concepts", lines 1–2: "We use 500 concepts across all experiments unless otherwise specified: the 50 original concepts from Lindsey (2025) plus 450 additional concepts spanning 20 semantic categories (Figure 18)."
- The Gemma3-27B setting is fixed at p. 3, §2, the paragraph after the forced-identification paragraph: "L = 37 and α = 4 … yields the highest overall introspection rate for Gemma3-27B … and use this setting throughout unless otherwise specified."

Gemma3-27B passages that state 500 concepts:
- p. 3, §2, paragraph "Success and failure concept partition.", line 1: "We partition our 500 concepts".
- p. 7, Figure 9 caption: "Introspection metrics vs. injection layer for Gemma3-27B, evaluated on 500 concepts."
- p. 23, Appendix B.4, line 1: "Detection rates across 500 concepts (L = 37)".
- p. 23, Figure 19 caption, line 1: "Detection rate distribution across 500 concepts (L = 37, α = 4, 100 trials per concept)."

**Trials per concept and n.**
- **Paper-wide default.** p. 22, Appendix B.3 "Injection Trials", lines 1–2: "We use 100 injection trials per concept (10 trial numbers × 10 samples each) unless otherwise specified." B.3 (pp. 22–23) states no control-trial count.
- **The OLMo comparison as presented.** These passages state no trial count, no control-trial count and no n:
  - §3.3, p. 4, paragraph "Base models do not discriminate …", lines 5–6
  - §3.3, p. 5, paragraph "Contrastive preference training enables introspection."
  - the Figure 5 caption (p. 5)
  - the Table 3 caption (p. 5)
  - the Figure 22 caption (p. 27, D.1)
  - the Table 8 caption (p. 27, D.2)
  - the Table 9 caption (p. 28, D.4)

  Of these, Figures 5 and 22 state a concept count (50). The table captions state none.
- **The one OLMo-inclusive passage with counts.** p. 25, Appendix C.2 "Cross-Model Generalization for Abliteration Effects", lines 5–7: "Detection rates are approximated by the logit difference Yes − No, aggregated over 50 concepts × 10 trial numbers (500 injection trials) and 10 control trials per (layer, strength)." This passage covers Figure 20, the abliteration study across five models including OLMo-3.1-32B. It is not the Figure 5 comparison.
- **N2(vi)'s wording**, "the source states no n (v1–v5)", checked against v5 only:
  - For the OLMo comparison's own text and captions, it holds on the v5 PDF.
  - Read as a claim about the whole of v5, it does not hold: B.3 states a per-concept injection-trial default. The OLMo passages do not mention trials, so they neither invoke that default nor override it.

## 3. (c) Refusal-direction ablation on Gemma3-27B (§3.3, Figure 4)

**Main locator.** p. 4 → p. 5, §3.3, paragraph "Refusal ablation ("abliteration") increases true detection." Lines 4–6: line 4 is p. 4's last body line, and lines 5–6 are p. 5's first two lines. Verbatim:
> Figure 4 (right) shows that abliteration increases TPR from 10.8% to 63.8% and introspection rate from 4.6% to 24.1% (at α = 2), while increasing FPR only modestly from 0.0% to 7.3%.

As printed in this sentence:
- 10.8% → 63.8% is TPR. The block calls it "hit rate".
- 4.6% → 24.1% is the "introspection rate", and "(at α = 2)" follows that clause.
- 0.0% → 7.3% is FPR, and "only modestly" applies to it.

The block's parenthetical places 4.6% → 24.1% beside the false alarms. In the source, the false-alarm clause is 0.0% → 7.3% only.

**Footnote 2.** p. 4, footnote 2 (2 lines), attached to "Gemma3-27B instruct." in line 4 of the paragraph:
> We also focus our introspection analysis at a smaller steering strength α = 2.0, since the abliterated model exhibits coherence degradation ("brain damage") at higher strengths; see Appendix C.1 for details.

**Figure 4.** The figure is placed on p. 4, right column, above the §3.3 heading, and cited from §3.3. Caption (3 lines): "Figure 4: Introspection for Gemma3-27B base (left), instruct (middle), and abliterated (right) for L = 37, α ∈ {1, 2, 4, 8}. Shaded region: 95% CI." The caption carries no rates.

**"modest" applied to the false-positive rise.** The text layer has 5 hits for "modest" (case-insensitive), all listed here:
- p. 5, §3.3, line 5 of the paragraph above: "increasing FPR only modestly from 0.0% to 7.3%".
- p. 2, §1, contributions item 4, lines 1–2: "Ablating refusal directions improves detection from 10.8% to 63.8% with modest false positive increases (0% to 7.3%)."
- Not applied to the false-positive rise:
  - p. 2, §1 item 1, lines 1–2: "at modest nonzero rates", about detection.
  - p. 10, §5.3 "Gate and Evidence Carrier Features" (the paragraph continued from p. 9), line 7 of the page: "only modest reductions in detection rates", about ablating evidence carriers.
  - p. 27, D.2: "modest discrimination (+4.6% at best)", about the LoRA-trained Gemma variants.
- Raster: p. 1, Figure 1, right column, "Refusal ablation" panel: "Removing refusal direction boosts detection: +53%" / "Modest increase in false positives: 0%→7%". Raster figure text was searched on Figure 1 only.

**Other v5 carriers of the result** (locators only): p. 1, Abstract, lines 17–19: "ablating refusal directions improves detection by +53%, … both without meaningfully increasing false positives." The text layer has no other occurrence of 10.8 or 63.8: they appear only at p. 2 item 4 and p. 4 §3.3.

## 4. Extraction scripts (as run; sha256 of each)

`pdfdump.swift`, sha256 `6a5196159d46e1ba900c8ccae21d2733797aafcf53a7b92f18821634aed910ed`:
```swift
import Foundation
import PDFKit
let args = CommandLine.arguments
guard args.count == 2, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("usage: pdfdump <pdf>\n".data(using: .utf8)!); exit(2)
}
print("PAGES \(doc.pageCount)")
for i in 0..<doc.pageCount {
    let p = doc.page(at: i)!
    print("=====PAGE \(i + 1) label=\(p.label ?? "-")=====")
    print(p.string ?? "")
}
```

`pdfrender.swift`, sha256 `e9ded5cff0b65226d2a079df5a8473e3230bdbdeb503e771860ab7af648f19d8`. It is invoked as `pdfrender <pdf> <outdir> <scale> <page>...` and draws each page's media box into a white RGBA bitmap at the given scale with `PDFPage.draw(with:to:)`, then writes it as PNG. The 4× crops were made with `sips -c`.
