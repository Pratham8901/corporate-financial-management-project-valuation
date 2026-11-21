# Valuation methodology and audit

This project models a hypothetical subscription platform using a 2026 valuation date (t = 0), ten operating years (2027–2036) and a terminal perpetuity. Units: **$ millions**, without asserting an underlying national currency.

## Operating forecast

- Three subscriber tiers. 2027 initial subscribers and prices; tier-dependent subscriber growth begins 2028. Growth slows after 2031.
- R&D is paid from 2026; marketing and other costs start 2027. All annual costs and subscription prices escalate with applicable inflation.
- Straight-line depreciation affects EBIT, but is added back in operating cash flow. Compute assets are replaced in 2031, and data assets in 2034.
- Cash tax in year *t* equals **27% of positive EBIT in year t−1**, with no loss carry-forward.
- Year-end working capital equals **3% of next-year operating costs**. Changes are cash flows; no terminal release under the going-concern assumption.
- Project FCF = EBITDA − lagged cash tax − capex − change in working capital − expansion spend + exit proceeds.
- Base discount rate is 14%, terminal growth is 2.5%. Terminal value equals **2036 FCF × (1+g)/(r−g)**, discounted to end-2026.

## Scenario valuation

The probability-weighted NPV uses 40% optimistic and 60% pessimistic probabilities. Inflation increases of +1 percentage point and discounting at 10% are analysed separately and jointly.

## Real options at end-2031

- Optimistic expansion: invest additional $24m and increase 2032-onward revenues by 15%. New depreciation is not added because the case does not prescribe an asset life.
- Pessimistic abandonment: receive $20m salvage, avoid 2031 compute replacement, release working capital and cease the project. Salvage-gain tax is excluded as a stated modelling assumption.
- Compare full time-zero NPVs for continue/expand and continue/abandon, then take the value-maximising branch under each scenario.

## Reconciliation: inflation sensitivity

The uploaded collaborative workbook uses **2.5%** rather than **3.5%** to grow the *other operating cost* component of projected 2037 costs in the +1 percentage-point inflation sensitivity, whereas the other components use 3.5%. This affects the 2036 working-capital balance and terminal FCF. The Python model consistently applies the higher rate to every 2037 operating-cost component. Accordingly, the original report's expected NPVs **−2.57m** (inflation-only) and **+182.00m** (combined) differ slightly from this repository's **−2.61m** and **+181.92m**. The 14% base case and 10% discount case match within rounding.

## Limitations

**Terminal-value reliance:** Recurring post-2036 infrastructure replacement capex is not separately normalised in the perpetuity. This could materially overstate value. Subscriber retention, competitive pricing, energy costs and geopolitical risks are not individually stress-tested. Currency, company and scenario values are illustrative. The model is educational, not an investable company recommendation.

See [publication checklist](publication_checklist.md) for rights and contribution disclosures.
