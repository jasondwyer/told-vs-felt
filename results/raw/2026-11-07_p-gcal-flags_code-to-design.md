# PROPOSAL-p: three BUILD flags to rule before G-CAL-p runs (Code → design seat, through the PI)

*Code's block, PI date 2026-11-07.*

- **Where p stands.** The p package BUILD (`a665a09`) and G-SHAPE-p (`5009e77`, PASS) are committed.
- **G-CAL-p** is one shot per checkpoint, and its artifacts are write-once. It waits for the coordinating session's go for the box, which the PI delegated in routing item 3 of 2026-11-07: "G-CAL-p on your go for the box".
- **Why Code holds the go.** The BUILD's design raw (`results/raw/2026-11-07_p-build_design.md`) carries ten flags, F-p1 to F-p10. Three of them change what G-CAL-p's artifacts record, so Code holds the go until the seat rules them. Each is a one-line change either way.

## The three rulings asked

1. **F-p3 — §5.4's date.**
   - G-CAL-p's and G-SHAPE-p's artifacts carry §5.4's disclosure with the date §5.4 gives: 2026-11-06, v0.1's date.
   - p v0.2 was committed on 2026-11-07 (`18b0111`; referent item 85).
   - **Rule the date in the disclosure:** 2026-11-06 as written, or 2026-11-07.
2. **F-p8 — the proposal pin in G-CAL-p's identity.**
   - The seat's answers of 2026-11-07, Q1 (iii): "The proposal pin stays m's; `proposal_p_sha256` is recorded beside it in every p output".
   - Code read that rule's scope as the analyzer's outputs, since Q1 is the analyzer path. As built, G-CAL-p's identity carries p's sha256 in both places:
     - `proposal_sha256`, the document the gate runs under, which its gate line checks;
     - `proposal_p_sha256`.
   - **Rule the scope:** G-CAL-p's identity as built, or m's pin with p's beside it.
3. **F-p10 — the cut log.**
   - As built, each stored-text cut (§2.2, reading (b)) is logged in the checkpoint and the artifact with the returned text, including the part after the line break. A stop keeps the returned text whole in its `stop` field.
   - The purpose is that the seat's read of every generation can see what was cut. None of it is the record's text, and none of it is graded or shown to a later round.
   - §2.2 says "Nothing after the cut is stored".
   - **Rule whether the log is storage:** keep the returned text as built, or keep only its sha256 and length.

## On the record, no ruling asked before G-CAL-p

- **The other flags.** F-p1 (§2.3's corrupted-spelling counter, a descriptive counter computable from the records at any time), F-p2, F-p4 to F-p7 and F-p9, all in the design raw.
- **The departure disclosed at `18b0111`.** The package was written in the working tree while v0.2's referent check ran, before step 3's commit, which §8 orders first.
- **The referent check's dated notes**, including items 43 (the 11-07 routing has no date item), 85 (F-p3 above) and 131. Item 131: §1.1 gained "matched case-insensitively", which is not in v0.2's "what changed" list; no render changes.

## Order

The seat's rulings come first. Code then applies each one (a constant or an argument), the coordinating session gives its go, and G-CAL-p runs.
