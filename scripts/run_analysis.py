"""Produce reproducible valuation summaries and data for charts."""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from cfm.valuation import calculate_all

def export_csv(path, rows):
    path.parent.mkdir(exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

def main():
    inputs = json.loads((ROOT / "config" / "assumptions.json").read_text())
    result = calculate_all(inputs)
    summary = [dict(case=k, optimistic_npv_m=f"{v['optimistic']['npv']:.6f}",
        pessimistic_npv_m=f"{v['pessimistic']['npv']:.6f}",
        probability_weighted_npv_m=f"{v['expected_npv']:.6f}")
        for k,v in result["cases"].items()]
    export_csv(ROOT / "outputs" / "npv_summary.csv", summary)
    export_csv(ROOT / "outputs" / "cashflow_forecasts.csv",
        [dict(scenario=s, **row) for s in ("optimistic","pessimistic")
        for row in result["cases"]["base"][s]["rows"]])
    choices = {"optimistic_continue": result["cases"]["base"]["optimistic"],
        "optimistic_expand": result["option_branches"]["optimistic_expand"],
        "pessimistic_continue": result["cases"]["base"]["pessimistic"],
        "pessimistic_abandon": result["option_branches"]["pessimistic_abandon"]}
    export_csv(ROOT / "outputs" / "real_options_branches.csv",
        [dict(choice=k,npv_m=f"{v['npv']:.6f}") for k,v in choices.items()])
    print("Expected NPV without options: %.3f $m" % result["cases"]["base"]["expected_npv"])
    print("Expected NPV with options: %.3f $m" % result["expected_with_options"])
    print("Value of flexibility: %.3f $m" % result["option_value"])
    print("CSV outputs written to outputs/. Publication figures are committed as SVG.")
if __name__ == "__main__":
    main()
