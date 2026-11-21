# Assessment 2 | Methodology and limitations

[← Texas Instruments case study](README.md)

## Source hierarchy and provenance

This companion guide is based on the **final user-provided submitted presentation** (`Texas instruments Team 6.pptx`) and the associated submitted calculation workbook (`Team 6 Workbook.xlsx`). The presentation reported analyses performed using **LSEG Workspace**, **Federal Reserve H.15/FRED**, Texas Instruments filings and team assumptions. The files are not committed to this repository.

Results shown here are **transcriptions of the team's reported figures**. This README/visual refresh is *not* an independent extraction and verification of every workbook formula, bond record or third-party data input.

## Methods presented

1. **Beta and expected equity return:** Four years of monthly equity and market excess returns were regressed with OLS. The market proxy was S&P 500/SPY in the team's methodology. The beta estimate entered the CAPM equation `rE = rf + beta × MRP`, with a team-assumed **5%** market risk premium.
2. **Debt cost:** A bond-yield approach used long-dated TXN yields after an estimate of expected default loss; a separate debt-CAPM approach provided a comparison. The team favoured the yield-based estimate for WACC.
3. **Market-value balance sheet:** Equity market value from share price × shares outstanding; debt market value based on bond cash-flow pricing against an interpolated Treasury curve and spread. The WACC calculation applied `WACC = (E/V) × rE + (D/V) × rD × (1 − tax_rate)`, with the study's **21%** corporate tax rate.
4. **Uncertainty:** The team reported a 95% September beta interval of **0.867–2.075**, compared a five-year-method beta to LSEG's beta, and analysed the effect of excluding a single influential April observation.
5. **Capital structure stress:** The team's scenario included loss of **50% of China-exposed revenue**, **10% weaker demand elsewhere**, **70% decremental EBITDA margin** and **+100 bp credit spreads**, in conjunction with hypothetical acquisition financing. A mitigated funding scenario was then compared.

## Key modelling caveats

- **Different horizons and dates:** The headline is a historical two-date comparison, not an up-to-date cost-of-capital estimate.
- **Beta precision:** The reported interval is wide and overlapping estimates do not establish a statistically significant change.
- **Outlier sensitivity:** Dropping April 2026 is a *diagnostic sensitivity test*, not justification for ignoring material market information.
- **WACC decomposition:** A sequential attribution depends on the order in which drivers are changed.
- **Debt valuation:** The original spreadsheet contained licensed market inputs; the full bond-level reconstruction is not published or independently checked here.
- **Stress assumptions:** Hypothetical shocks should not be mistaken for probabilities or TXN's actual future financial performance.
- **Valuation versus recommendation:** The 11% planning hurdle rate is a team's proposed operating judgement and differs from the reported 12.25% point estimate.
- **Collaborative work:** The original analysis was submitted by a student group; portfolio summaries should not misrepresent individual contribution.

## What is reproduced in this repository

The four SVG charts and `reported-metrics.csv` are **new presentation artifacts** redrawn from final team-reported numbers. They are static documentation, not a fully reproducible LSEG-to-WACC software pipeline. The case should be evaluated on its declared analytical reasoning and documented limitations rather than unverified claims of independent calculation.

## Original source categories

LSEG Workspace company data and security data; Federal Reserve H.15 and FRED rate series; company filings and corporate releases; reference finance textbooks and project assumptions. For exact dates and source citations, consult the final academic submission rather than assuming these summaries provide the complete original bibliography.

[Rights and attribution](attribution-and-sources.md)
