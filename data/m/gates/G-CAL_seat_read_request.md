# G-CAL -- the seat's legibility read of record (condition (3))

renders_sha256: `a04f67b0e5105a0514a0f33e64a4545ef3a3a3c75cece320d78434e853cd4372`

Source: PROPOSAL-m v1.11 §2.3 (m:176); model-free artifact `G-CAL_model-free.json` (package_sha256 `4b49658739523c60`, proposal_sha256 `42ab36ecc814c9c4`).

## How to read -- before section A

For each render, write down the task as you read it and its answer, before opening section B. Read each render alone, in order, and record one line per render number 0-15 (the task as you read it; its answer). Read section A before section B.

## A. The 16 renders of record -- read these first, each alone

0. `Clopuie 31 + 46.`
1. `State the number oq dsys in a wemk.`
2. `Name thy thiru month of the yebr.`
3. `Coepqte 60 diyided by 5.`
4. `State the numbev of szbes of a tryangle.`
5. `Writa the oppcsite oc 'hot'.`
6. `Combuks 14 times 2.`
7. `State whqch iy heayier: a kilogram of iron or holf a kilogdam of feathwis.`
8. `Name the ftrst month of the ybaa.`
9. `Comgute 90 miyms 45.`
10. `State the nfmber of wheeqs on a bicyaxe.`
11. `Writo the oppssitu of 'up'.`
12. `Cnmzote 11 + 33.`
13. `State the numbxi of hourw in a day.`
14. `Coltute 8 timns 8.`
15. `Wtite thn opposite on 'open'.`

---

## B. Key -- open only after section A

Condition (3) (m:176): "the seat's legibility read of the 16 renders of record finds every gold recoverable". For each item 0-15, compare the answer you wrote down in section A with the item's gold below and record whether the gold is recoverable from the render (yes or no, with the answer recovered). Condition (3) passes iff all 16 are; "(3) or (4) failing → STOP and re-specify" (m:176); "the read of record is repeated at G-CAL on the renders of record" (m:176). Changed positions are 0-based character offsets into the clean task (clean letter > rendered letter); the walk never touches a word-initial letter or the single-quoted operand.

Reply with the renders_sha256 at the top and the 16 per-item records (the task as read, its answer, recoverable yes or no). The read of record is recorded in the G-CAL entry and carried into LOCK-m-F0 v0.1, whose calibration artifacts include the seat's read (m:176).

### Item 0
- render: `Clopuie 31 + 46.`
- clean task: `Compute 31 + 46.`
- gold: `77`
- k: 3 (n_eligible 6)
- changed positions: 1 (o>l), 2 (m>o), 5 (t>i)
- operand span excluded: none

### Item 1
- render: `State the number oq dsys in a wemk.`
- clean task: `State the number of days in a week.`
- gold: `7`, `seven`
- k: 3 (n_eligible 19)
- changed positions: 18 (f>q), 21 (a>s), 32 (e>m)
- operand span excluded: none

### Item 2
- render: `Name thy thiru month of the yebr.`
- clean task: `Name the third month of the year.`
- gold: `march`
- k: 3 (n_eligible 19)
- changed positions: 7 (e>y), 13 (d>u), 30 (a>b)
- operand span excluded: none

### Item 3
- render: `Coepqte 60 diyided by 5.`
- clean task: `Compute 60 divided by 5.`
- gold: `12`, `twelve`
- k: 3 (n_eligible 13)
- changed positions: 2 (m>e), 4 (u>q), 13 (v>y)
- operand span excluded: none

### Item 4
- render: `State the numbev of szbes of a tryangle.`
- clean task: `State the number of sides of a triangle.`
- gold: `3`, `three`
- k: 4 (n_eligible 24)
- changed positions: 15 (r>v), 21 (i>z), 22 (d>b), 33 (i>y)
- operand span excluded: none

### Item 5
- render: `Writa the oppcsite oc 'hot'.`
- clean task: `Write the opposite of 'hot'.`
- gold: `cold`
- k: 3 (n_eligible 14)
- changed positions: 4 (e>a), 13 (o>c), 20 (f>c)
- operand span excluded: `'hot'` [22, 27)

### Item 6
- render: `Combuks 14 times 2.`
- clean task: `Compute 14 times 2.`
- gold: `28`
- k: 3 (n_eligible 10)
- changed positions: 3 (p>b), 5 (t>k), 6 (e>s)
- operand span excluded: none

### Item 7
- render: `State whqch iy heayier: a kilogram of iron or holf a kilogdam of feathwis.`
- clean task: `State which is heavier: a kilogram of iron or half a kilogram of feathers.`
- gold: `iron`
- k: 7 (n_eligible 45)
- changed positions: 8 (i>q), 13 (s>y), 18 (v>y), 47 (a>o), 58 (r>d), 70 (e>w), 71 (r>i)
- operand span excluded: none

### Item 8
- render: `Name the ftrst month of the ybaa.`
- clean task: `Name the first month of the year.`
- gold: `january`
- k: 3 (n_eligible 19)
- changed positions: 10 (i>t), 29 (e>b), 31 (r>a)
- operand span excluded: none

### Item 9
- render: `Comgute 90 miyms 45.`
- clean task: `Compute 90 minus 45.`
- gold: `45`
- k: 3 (n_eligible 10)
- changed positions: 3 (p>g), 13 (n>y), 14 (u>m)
- operand span excluded: none

### Item 10
- render: `State the nfmber of wheeqs on a bicyaxe.`
- clean task: `State the number of wheels on a bicycle.`
- gold: `2`, `two`
- k: 4 (n_eligible 24)
- changed positions: 11 (u>f), 24 (l>q), 36 (c>a), 37 (l>x)
- operand span excluded: none

### Item 11
- render: `Writo the oppssitu of 'up'.`
- clean task: `Write the opposite of 'up'.`
- gold: `down`
- k: 3 (n_eligible 14)
- changed positions: 4 (e>o), 13 (o>s), 17 (e>u)
- operand span excluded: `'up'` [22, 26)

### Item 12
- render: `Cnmzote 11 + 33.`
- clean task: `Compute 11 + 33.`
- gold: `44`
- k: 3 (n_eligible 6)
- changed positions: 1 (o>n), 3 (p>z), 4 (u>o)
- operand span excluded: none

### Item 13
- render: `State the numbxi of hourw in a day.`
- clean task: `State the number of hours in a day.`
- gold: `24`, `twenty-four`
- k: 3 (n_eligible 19)
- changed positions: 14 (e>x), 15 (r>i), 24 (s>w)
- operand span excluded: none

### Item 14
- render: `Coltute 8 timns 8.`
- clean task: `Compute 8 times 8.`
- gold: `64`
- k: 3 (n_eligible 10)
- changed positions: 2 (m>l), 3 (p>t), 13 (e>n)
- operand span excluded: none

### Item 15
- render: `Wtite thn opposite on 'open'.`
- clean task: `Write the opposite of 'open'.`
- gold: `closed`, `shut`
- k: 3 (n_eligible 14)
- changed positions: 1 (r>t), 8 (e>n), 20 (f>n)
- operand span excluded: `'open'` [22, 28)
