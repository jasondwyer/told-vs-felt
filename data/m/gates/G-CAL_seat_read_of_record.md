# G-CAL — the seat's legibility read of record (condition (3), m:176)

renders_sha256: `a04f67b0e5105a0514a0f33e64a4545ef3a3a3c75cece320d78434e853cd4372`

Design seat, 2026-10-09. Read against `data/m/gates/G-CAL_seat_read_request.md` (HEAD `961e90a`; the m thread's last commit `cf8eb5b`). For the PI to route to Code; Code records it in the G-CAL entry and carries it into LOCK-m-F0 v0.1 per m:176. Suggested placement: `data/m/gates/G-CAL_seat_read_of_record.md`.

**Result: condition (3) PASSES — every gold is recoverable from its render, 16 of 16.** Every answer written in section A matches the item's gold in section B.

**Reading conditions, disclosed.** The sixteen renders were first seen together in one listing on 2026-10-08, while the seat was reading the repository to report on the audit's progress (a `head -30` of the request file, which ended at the rule before section B). They were not read one at a time on first sight, as the request asks. The per-item lines below were written on 2026-10-09 from that listing, and committed to a file, before section B or anything after it was opened; nothing in section B informed any line. Code may weigh the batch exposure as it sees fit; the seat's view is that it does not bear on recoverability, which is the condition.

## Per-item records

| # | task as read | answer | gold | recoverable |
|---|---|---|---|---|
| 0 | Compute 31 + 46. | 77 | `77` | yes |
| 1 | State the number of days in a week. | 7 | `7`, `seven` | yes |
| 2 | Name the third month of the year. | March | `march` | yes |
| 3 | Compute 60 divided by 5. | 12 | `12`, `twelve` | yes |
| 4 | State the number of sides of a triangle. | 3 | `3`, `three` | yes |
| 5 | Write the opposite of 'hot'. | cold | `cold` | yes |
| 6 | Compute 14 times 2. | 28 | `28` | yes |
| 7 | State which is heavier: a kilogram of iron or half a kilogram of feathers. | the kilogram of iron | `iron` | yes |
| 8 | Name the first month of the year. | January | `january` | yes |
| 9 | Compute 90 minus 45. | 45 | `45` | yes |
| 10 | State the number of wheels on a bicycle. | 2 | `2`, `two` | yes |
| 11 | Write the opposite of 'up'. | down | `down` | yes |
| 12 | Compute 11 + 33. | 44 | `44` | yes |
| 13 | State the number of hours in a day. | 24 | `24`, `twenty-four` | yes |
| 14 | Compute 8 times 8. | 64 | `64` | yes |
| 15 | Write the opposite of 'open'. | closed | `closed`, `shut` | yes |

Every task as read equals the clean task in section B verbatim (item 7's answer is the gold with the noun phrase around it).

## Read notes (descriptive; for the G-CAL entry, not for the condition)

- Items 0, 3, 6, 9, 12, 14: the verb was recovered from the template and the arithmetic that follows it, not from its letters — `Clopuie`, `Coepqte`, `Combuks`, `Comgute`, `Cnmzote`, `Coltute` share with "Compute" only the initial letter and the length. The 0.12 walk at k = 3 on a seven-letter word leaves four of seven letters; the word is still unreadable on its own and fully readable in its frame.
- Item 7 (k = 7 over 45 eligible): three content words corrupted in one clause (`holf`, `kilogdam`, `feathwis`), recovered from the fixed phrase; the longest render reads as easily as the shortest because the phrase is a known one.
- Item 15: the preposition is wrong (`on` for `of`) and was read through without noticing on first pass.
- The operand spans excluded from the walk (`'hot'`, `'up'`, `'open'`) are the answer-bearing tokens; their exclusion is what keeps items 5, 11 and 15 recoverable at all, since the task's verb and noun can be corrupted freely around a clean operand. Worth a sentence in the LOCK's calibration note.
- No render was illegible; none was ambiguous between two tasks; no answer required a guess between candidates.
