"""Regression checks against the original, collaborative spreadsheet model."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from cfm.valuation import forecast, calculate_all
A = json.loads((ROOT/"config"/"assumptions.json").read_text())

class ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = calculate_all(A)

    def test_base_npvs(self):
        b=self.r["cases"]["base"]
        self.assertAlmostEqual(b["optimistic"]["npv"],29.05799,places=3)
        self.assertAlmostEqual(b["pessimistic"]["npv"],-47.59736,places=3)
        self.assertAlmostEqual(b["expected_npv"],-16.93522,places=3)

    def test_first_year_and_initial_capex(self):
        rows=self.r["cases"]["base"]["optimistic"]["rows"]
        self.assertAlmostEqual(rows[0]["capex"],100)
        self.assertAlmostEqual(rows[1]["revenue"],35.1)
        self.assertAlmostEqual(rows[0]["free_cash_flow"],-118.87785,places=5)

    def test_prior_year_tax(self):
        rows=self.r["cases"]["base"]["optimistic"]["rows"]
        for current, previous in zip(rows[1:],rows[:-1]):
            self.assertAlmostEqual(current["taxes_paid"],.27*max(previous["ebit"],0),places=7)

    def test_replacement_capex(self):
        data={row["year"]:row for row in self.r["cases"]["base"]["optimistic"]["rows"]}
        self.assertEqual(data[2031]["capex"],70)
        self.assertEqual(data[2034]["capex"],54)

    def test_discount_rate_sensitivity(self):
        x=self.r["cases"]["discount_10pct"]
        self.assertAlmostEqual(x["optimistic"]["npv"],233.36032,places=3)
        self.assertAlmostEqual(x["pessimistic"]["npv"],99.33986,places=3)

    def test_options(self):
        x=self.r
        self.assertAlmostEqual(x["option_branches"]["optimistic_expand"]["npv"],86.17648,places=3)
        self.assertAlmostEqual(x["option_branches"]["pessimistic_abandon"]["npv"],-157.02227,places=3)
        self.assertTrue(x["optimal_branches"]["optimistic"]["expand"])
        self.assertFalse(x["optimal_branches"]["pessimistic"]["abandon"])
        self.assertAlmostEqual(x["expected_with_options"],5.91217,places=3)
        self.assertAlmostEqual(x["option_value"],22.84740,places=3)

    def test_inflation_extension(self):
        x=self.r["cases"]["inflation_plus_1pp"]["optimistic"]
        self.assertAlmostEqual(x["rows"][-1]["working_capital_balance"],2.668918274,places=6)

    def test_invalid_discount_rate(self):
        with self.assertRaises(ValueError):
            forecast("optimistic",A,rate=.01)

if __name__=="__main__":
    unittest.main()
