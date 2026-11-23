"""Compare a fund exit with a primary share issue in the NovaThera teaching case.

Amounts are in A$ millions. The IPO uses the pre-money convention specified
in the case. Run from the repository root with Python 3.10 or later.
"""

import argparse
import math

STANDALONE_EV = 836.7
NET_CASH = 30.0
FUND_STAKE = 0.25
FUND_COST = 40.0
TARGET_FLOAT = 0.20


def sale_outcome(enterprise_value):
    equity_value = enterprise_value + NET_CASH
    proceeds = equity_value * FUND_STAKE
    return equity_value, proceeds, proceeds / FUND_COST


def ipo_outcome(pre_money, primary):
    post_money = pre_money + primary
    primary_float = primary / post_money
    retained_stake = FUND_STAKE * pre_money / post_money
    secondary_needed = max(0.0, TARGET_FLOAT * post_money - primary)
    return primary_float, retained_stake, secondary_needed


def nonnegative_amount(text):
    amount = float(text)
    if not math.isfinite(amount) or amount < 0:
        raise argparse.ArgumentTypeError("enter a finite, nonnegative A$ million amount")
    return amount


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sale-ev", type=nonnegative_amount, default=880.0,
                        help="sale enterprise value in A$ millions (default 880)")
    parser.add_argument("--primary", type=nonnegative_amount, default=95.0,
                        help="new IPO capital in A$ millions (default 95)")
    args = parser.parse_args()

    net_synergies = 14.0 * (1 - 0.30) / 0.09 - 25.0
    indicated_ev = STANDALONE_EV + 0.5 * net_synergies
    equity, proceeds, multiple = sale_outcome(args.sale_ev)
    print(f"Standalone EV plus seller's share of synergies: A${indicated_ev:.1f}m")
    print(f"Sale equity value: A${equity:.1f}m")
    print(f"Gross proceeds to the fund on a cash exit: A${proceeds:.1f}m ({multiple:.2f}x cost)")

    for label, pre_money in (("Case convention", STANDALONE_EV),
                             ("Including existing net cash", STANDALONE_EV + NET_CASH)):
        new_float, retained, secondary = ipo_outcome(pre_money, args.primary)
        print(f"{label}: {new_float:.2%} primary float, {retained:.2%} fund ownership")
        print(f"  Secondary sale needed for a 20% float: A${secondary:.2f}m")


if __name__ == "__main__":
    main()
