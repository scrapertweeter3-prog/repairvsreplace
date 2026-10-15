#!/usr/bin/env python3
"""repairvsreplace - compare fixing a broken item against buying new.

Takes the repair quote, the item's remaining realistic service life after
the repair, the price of a new replacement, and the replacement's realistic
service life, then prints cost per service year for both lanes and names
the cheaper one.

Stdlib only. Run: python3 repairvsreplace.py --price 240 --repair 40
                                  --life-repaired 12 --life-new 14
"""
import argparse
import sys


def cost_per_year(total: float, life: float) -> float:
    """Total spend divided by remaining service years.

    >>> cost_per_year(40, 12)
    3.33
    >>> cost_per_year(240, 14)
    17.14
    >>> cost_per_year(100, 0)
    inf
    """
    if life <= 0:
        return float("inf")
    return round(total / life, 2)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Compare repairing an item against replacing it.")
    p.add_argument("--price", type=float, required=True,
                   help="what a new replacement costs today")
    p.add_argument("--repair", type=float, required=True,
                   help="the repair quote")
    p.add_argument("--life-repaired", type=float, required=True,
                   help="realistic years of service left after the repair")
    p.add_argument("--life-new", type=float, required=True,
                   help="realistic years of service from a new unit")
    p.add_argument("--hustle-rate", type=float, default=0.0,
                   help="your hourly rate; values your own labor on the repair")
    args = p.parse_args(argv)

    if args.price < 0 or args.repair < 0:
        print("prices cannot be negative", file=sys.stderr)
        return 2
    repair_total = args.repair
    if args.hustle_rate > 0:
        repair_total += args.hustle_rate  # one hour of your time, conservatively

    rep = cost_per_year(repair_total, args.life_repaired)
    new = cost_per_year(args.price, args.life_new)

    print(f"Repair lane : ${repair_total:,.2f} total, "
          f"${rep:,.2f} per service year")
    print(f"Replace lane: ${args.price:,.2f} total, "
          f"${new:,.2f} per service year")
    if rep < new:
        print("Verdict: repair it.")
    elif new < rep:
        print("Verdict: replace it.")
    else:
        print("Verdict: dead even.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
