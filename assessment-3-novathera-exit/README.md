# NovaThera Pharmaceuticals | Strategic sale or IPO?

**Individual research project · Corporate Financial Management · RMIT Master of Finance · October 2026**

A venture fund owns 25% of a hypothetical pharmaceutical company and wants to realise its investment. The company also needs A$95m to fund growth. A sale gives the fund liquidity. A primary share issue sends the money to the company. That difference drives the recommendation.

**Case recommendation.** Seek a strategic sale near A$880m enterprise value, with a cash election for the fund and a rollover option for other holders. Keep an IPO with a secondary share sale available if bidders offer too little. All amounts are Australian dollars.

## How the exit routes compare

| Route | Cash to the fund before fees and tax | What the fund retains |
|---|---:|---|
| Sale at A$880m enterprise value, fund elects cash | A$227.5m | No remaining stake. A$30m of net cash takes equity value to A$910m. The fund receives 25%, or 5.69× its A$40m cost. |
| A$95m primary IPO | A$0 at issue | 22.45% ownership after dilution. New public investors hold 10.20% under the case convention. |
| A$95m primary IPO plus secondary shares sold by the fund | A$91.34m at issue | About 12.65% ownership. Counting both legs gives a 20% float under the same assumptions. |

The mixed IPO funds the same growth plan as the primary-only issue. The secondary proceeds come from selling existing shares, so they go to the fund and add no cash to the company.

## What supports the sale price

The report estimated standalone enterprise value at A$836.7m from peer multiples. It assumed A$14m of annual pre-tax synergies, a 30% tax rate, a 9% capitalisation rate and A$25m of integration costs. Giving the seller half of the estimated net synergies yields A$878.6m, rounded to A$880m for the exit comparison.

Only two peers had usable earnings multiples. The synergy calculation capitalises the full run rate immediately, although the business case allowed up to three years to achieve it. A slower ramp or a smaller share of savings would weaken the case for the premium.

## Why the IPO denominator matters

The coursework uses standalone enterprise value as its pre-money IPO base. On that basis, A$95m divided by A$931.7m gives a 10.20% float. Including the existing A$30m of net cash in pre-money equity gives 9.88%. Both calculations assume all new shares qualify as free float and all existing shares are held outside it. The 20% target is one of several ASX admission criteria. [ASX listing requirements](https://www.asx.com.au/listings/listing-considerations/listing-requirements)

## Reproduce the comparison

From the repository root, run the default case or change the offer price and primary raise. The companion script uses the Python standard library.

```bash
python scripts/compare_exit_routes.py
python scripts/compare_exit_routes.py --sale-ev 700 --primary 100
```

[Python model](../scripts/compare_exit_routes.py) · [Calculation checks](../tests/test_exit_routes.py) · [Corporate finance portfolio](../README.md)

Pratham Kurele completed the underlying individual research project. This post-submission, AI-assisted portfolio reconstruction uses selected case assumptions and gross scenario results. The peer valuation comes from the report. The companion model recalculates the transaction arithmetic.
