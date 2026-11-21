# Capital Budgeting & Real Options | Corporate Financial Management

**RMIT University · Master of Finance · BAFI3257 · Collaborative academic project**

A finance portfolio case study evaluating a hypothetical subscription-based AI entertainment business through discounted cash-flow valuation, scenario analysis, sensitivity testing, and managerial real options. The repository is a **portfolio-style Python companion** to a collaborative Excel modelling project; it is **not** the original assessment submission.

> **Publication status: private-first draft.** The input assumptions originate from a university case and the original analysis was collaborative. See [publication checklist](docs/publication_checklist.md) and [rights notice](NOTICE.md).

## Executive summary

The project models ten years of operating cash flows (2027–2036), using a 2026 valuation date, lagged income tax, tiered subscriber growth, scheduled infrastructure replacements, working capital, and a terminal perpetuity. An explicit decision tree compares expansion under favourable demand with abandonment under unfavourable demand.

### Key results — base case

| Metric | NPV ($m) |
|:--|--:|
| Optimistic scenario | **+29.06** |
| Pessimistic scenario | **−47.60** |
| Expected NPV before managerial options (40%/60%) | **−16.94** |
| Optimistic expansion branch | **+86.18** |
| Pessimistic abandonment branch | **−157.02** |
| Expected NPV after optimal real options | **+5.91** |
| **Value of managerial flexibility** | **+22.85** |

**Interpretation:** The conventional probability-weighted base case would not justify immediate acceptance on NPV alone. Conditional managerial flexibility raises the expected modelled value to a modest positive figure, principally through expansion in the optimistic scenario. That conclusion is fragile because terminal value drives much of the valuation.

### Sensitivity analysis (Python model output)

| Assumption set | Optimistic | Pessimistic | Probability-weighted |
|:--|--:|--:|--:|
| Base case — 14% discount | +29.06 | −47.60 | −16.94 |
| Inflation +1 percentage point | +46.77 | −35.52 | −2.61 |
| Discount rate 10% | +233.36 | +99.34 | +152.95 |
| Both adjustments | +268.78 | +124.01 | +181.92 |

The original spreadsheet reported **+46.81 / −35.48** for the inflation-only scenario and **+268.86 / +124.09** for both adjustments; the small differences result from an end-2036 working-capital projection inconsistency identified during reconciliation. This implementation consistently escalates all projected 2037 cost components. See [methodology and audit](docs/methodology.md).

## Visual analysis

![Free cash flow comparison](figures/cashflow_by_scenario.png)

![NPV sensitivity comparison](figures/npv_sensitivity.png)

![Managerial flexibility valuation](figures/real_options_value.png)

## Skills demonstrated

- **Capital budgeting:** DCF, terminal-value modelling, project NPV, and weighted scenario valuation.
- **Financial modelling:** revenue build, operating expense forecast, depreciation, delayed tax payments, asset replacement, and net working capital.
- **Risk and decision analysis:** sensitivity to inflation and hurdle rates; expansion-versus-continuation and abandonment-versus-continuation decisions.
- **Reproducible analytics:** parameterised Python model, CSV exports, automated charts, and regression/unit tests.

## Repository structure

```text
config/assumptions.json          # Case input assumptions (publication clearance needed)
src/cfm/valuation.py            # Reusable DCF and options engine
scripts/run_analysis.py         # Export CSV analyses and generate figures
tests/test_valuation.py         # Reconciliation and unit tests
outputs/                        # NPV, cash-flow and decision CSVs
figures/                        # Revenue, cash flow, NPV and real-options charts
docs/methodology.md             # Calculation conventions and audit trail
docs/publication_checklist.md   # Academic-integrity and data-rights checks
NOTICE.md                       # Attribution and rights guidance
```

## Run locally

Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python scripts/run_analysis.py
python -m unittest discover -s tests -v
```

Change the financial assumptions in `config/assumptions.json`, then rerun to refresh scenario results, figures, and CSVs. No original group report, original spreadsheet, personal identifiers or university assignment PDF is included.

## Methodology at a glance

For each year, calculate tiered subscription revenues and operating cash costs. Cash tax equals 27% of **previous-year positive EBIT**. Working capital equals 3% of the **following year's operating expenses**. Free cash flow excludes depreciation as a cash expense but includes investment and the yearly change in working capital. Discount a 10-year forecast and a Gordon-growth terminal value; then probability-weight the demand scenarios. Finally, conditionally exercise real options at end-2031 where exercise value exceeds continuing operations.

More details, assumptions and model limitations are documented in [methodology.md](docs/methodology.md).

## Attribution and responsible use

The source Excel modelling and written case analysis were prepared in a **student group** as part of the Master of Finance curriculum at RMIT University. This repository presents a separately organised Python reconstruction and explanatory materials prepared with AI assistance. Individual contributions should be described accurately in interviews and in any public version. No endorsement by RMIT University is implied. **Do not present AI-generated code as independently written without reviewing and being able to explain it.**

This example is educational, not financial advice, and the results are conditional on hypothetical assumptions.
