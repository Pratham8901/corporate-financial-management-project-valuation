# Corporate finance | Valuation and financing decisions

Three projects from the Master of Finance at RMIT University. Each starts with a decision, shows which assumption matters most, and gives the reader a way to inspect the evidence.

| Case study | Decision and finding | Evidence |
|---|---|---|
| **[NovaThera Pharmaceuticals](assessment-3-novathera-exit/README.md)** · Individual | A strategic sale at A$880m enterprise value would return A$227.5m to the venture fund. An A$95m primary IPO would fund the company while leaving the fund invested. | [Exit proceeds and dilution model](scripts/compare_exit_routes.py) |
| **[Texas Instruments](assessment-2-texas-instruments/README.md)** · Team | The team's estimated weighted average cost of capital rose from 9.65% to 12.25% between March and September 2026. Omitting one influential month lowered the September estimate to 10.43%. | [Reported metrics](assessment-2-texas-instruments/reported-metrics.csv) · [Estimation assumptions](assessment-2-texas-instruments/methodology-and-limitations.md) |
| **[Subscription platform investment](assessment-1-project-valuation/README.md)** · Team | With fixed operating plans the model produced an expected net present value of −$16.94m. The option to expand after strong adoption raised it to +$5.91m. | [Ten-year cash-flow model](src/cfm/valuation.py) · [Sensitivity results](outputs/npv_summary.csv) |

## Run the models

Use Python 3.10 or later from the repository root. The numerical models and tests use the standard library.

```bash
python scripts/compare_exit_routes.py
python scripts/run_analysis.py
python -m unittest discover -s tests -v
```

The first command compares a cash sale with a primary IPO and a secondary share sale. The second rebuilds the subscription platform valuation from the model assumptions. For Texas Instruments, the published figures come from the team's final presentation.

The first two course assessments were group projects. NovaThera was an individual report. The companion Python models and portfolio pages were prepared after submission with AI assistance. [Attribution and source rights](NOTICE.md)
