# repairvsreplace

One-file Python calculator that puts a repair quote and a new-item price on
the same scale: cost per remaining service year.

The store quotes one number for the new item and the shop quotes another for
the fix, and neither tells you which one is cheaper per year of use. Feed it
the repair quote, how long the item realistically keeps working after the
fix, the new-item price, and how long the new one lasts. It prints total and
per-year cost for both lanes and names the cheaper one. An optional
`--hustle-rate` values an hour of your own labor on the repair, the number
most DIY math quietly pretends is zero.

## Usage

    python3 repairvsreplace.py --price 240 --repair 40 \
        --life-repaired 12 --life-new 14

    Repair lane : $40.00 total, $3.33 per service year
    Replace lane: $240.00 total, $17.14 per service year
    Verdict: repair it.

## Notes

- Stdlib only, single file, no install step.
- Doctest coverage on the math (`python3 -m doctest repairvsreplace.py`).
- Refuses negative prices; a zero-year life lane reads as infinite cost.

The repair-vs-replace habit comes from [Durable Picks](https://durablepicks.com),
where gear gets ranked by how it fails and what a decade of it costs.
