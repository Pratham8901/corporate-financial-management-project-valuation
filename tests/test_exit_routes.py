import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from compare_exit_routes import ipo_outcome, sale_outcome


class ExitRouteTests(unittest.TestCase):
    def test_sale_adds_cash_before_applying_the_fund_stake(self):
        equity, proceeds, multiple = sale_outcome(880)
        self.assertEqual((equity, proceeds, multiple), (910, 227.5, 5.6875))

    def test_primary_and_secondary_have_different_recipients(self):
        pre_money, primary = 836.7, 95
        issued, fund_stake, secondary = ipo_outcome(pre_money, primary)
        post_money = pre_money + primary
        self.assertAlmostEqual(fund_stake * post_money, 0.25 * pre_money)
        self.assertAlmostEqual(issued + secondary / post_money, 0.20)
        self.assertAlmostEqual(secondary, 91.34)

    def test_large_primary_already_meets_the_float_target(self):
        issued, _, secondary = ipo_outcome(836.7, 220)
        self.assertGreater(issued, 0.20)
        self.assertEqual(secondary, 0)


if __name__ == "__main__":
    unittest.main()
