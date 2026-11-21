"""Discounted cash-flow and managerial real-options model.

All monetary figures are in currency millions ($m); subscriber counts and
subscription prices are in ordinary units. Reconstructed as a portfolio example.
"""
from __future__ import annotations
from typing import Any

YEAR_ZERO = 2026
LAST_YEAR = 2036


def inflation(year: int, a: dict[str, Any]) -> float:
    e = a["economic"]
    return float(e["inflation_by_year"].get(str(year), e["inflation_from_2029"]))


def subscribers(year: int, tier: dict, scenario: dict) -> float:
    value = float(tier["initial_subscribers"])
    for y in range(2028, year + 1):
        key = "growth_years_2_to_5" if y <= 2031 else "growth_years_6_to_10"
        value *= 1 + float(scenario[key][tier["name"]])
    return value


def annual_revenue(year: int, scenario: dict, a: dict) -> float:
    total = 0.0
    for tier in scenario["tiers"]:
        price = float(tier["annual_price_2027"])
        for y in range(2028, year + 1):
            price *= 1 + inflation(y, a)
        total += subscribers(year, tier, scenario) * price / 1_000_000
    return total


def expenses(year: int, a: dict) -> dict[str, float]:
    costs = a["operating_costs_millions"]
    rnd = float(costs["research_and_development_2026"])
    for y in range(2027, year + 1):
        rnd *= 1 + inflation(y, a)
    if year == YEAR_ZERO:
        return {"rnd": rnd, "marketing": 0.0, "other": 0.0}
    marketing, other = float(costs["marketing_2027"]), float(costs["other_2027"])
    for y in range(2028, year + 1):
        factor = 1 + inflation(y, a)
        marketing *= factor
        other *= factor
    return {"rnd": rnd, "marketing": marketing, "other": other}


def depreciation(year: int, a: dict) -> float:
    cap = a["capital_expenditure_millions"]
    value = 0.0
    if 2027 <= year <= 2034:
        value += cap["initial_data"] / cap["data_life_years"]
    if 2027 <= year <= 2031:
        value += cap["initial_compute"] / cap["compute_life_years"]
    if 2035 <= year <= 2036:
        value += cap["replacement_data"] / cap["data_life_years"]
    if 2032 <= year <= 2036:
        value += cap["replacement_compute"] / cap["compute_life_years"]
    return value


def capex(year: int, a: dict) -> float:
    cap = a["capital_expenditure_millions"]
    if year == 2026:
        return float(cap["initial_data"] + cap["initial_compute"])
    if year == 2031:
        return float(cap["replacement_compute"])
    if year == 2034:
        return float(cap["replacement_data"])
    return 0.0


def forecast(scenario_name: str, a: dict, *, expand: bool = False, abandon: bool = False,
             rate: float | None = None, inflation_extra: float = 0) -> dict:
    if expand and abandon:
        raise ValueError("Only one real option can be exercised")
    if inflation_extra:
        econ = a["economic"]
        a = {**a, "economic": {**econ,
             "inflation_by_year": {k: v + inflation_extra for k, v in econ["inflation_by_year"].items()},
             "inflation_from_2029": econ["inflation_from_2029"] + inflation_extra}}
    e, scenario = a["economic"], a["scenarios"][scenario_name]
    r = float(e["discount_rate"] if rate is None else rate)
    g = float(e["terminal_growth"])
    if r <= g:
        raise ValueError("Discount rate must exceed perpetuity growth")
    option, tax = a["real_options"], float(e["tax_rate"])
    last_wc = last_ebit = 0.0
    rows = []
    for year in range(YEAR_ZERO, LAST_YEAR + 1):
        if abandon and year > 2031:
            break
        period = year - YEAR_ZERO
        revenue = 0 if year == YEAR_ZERO else annual_revenue(year, scenario, a)
        if expand and year >= 2032:
            revenue *= 1 + option["revenue_uplift_after_expansion"]
        operating_cost = sum(expenses(year, a).values())
        ebitda = revenue - operating_cost
        dep = 0.0 if year == YEAR_ZERO else depreciation(year, a)
        ebit = ebitda - dep
        taxes_paid = tax * max(last_ebit, 0.0) if period else 0.0
        op_cf = ebitda - taxes_paid
        wc = float(e["working_capital_fraction"]) * sum(expenses(year + 1, a).values())
        delta_wc = wc - last_wc
        investment = capex(year, a)
        expansion = option["expansion_cost_millions"] if expand and year == 2031 else 0.0
        salvage = option["abandonment_salvage_millions"] if abandon and year == 2031 else 0.0
        if abandon and year == 2031:
            investment, delta_wc, wc = 0.0, -last_wc, 0.0
        fcf = op_cf - investment - expansion - delta_wc + salvage
        rows.append(dict(year=year, period=period, revenue=revenue,
            operating_costs=operating_cost, ebitda=ebitda, depreciation=dep,
            ebit=ebit, taxes_paid=taxes_paid, after_tax_operating_cf=op_cf,
            capex=investment, expansion_capex=expansion, salvage=salvage,
            working_capital_balance=wc, delta_working_capital=delta_wc,
            free_cash_flow=fcf, pv_free_cash_flow=fcf/(1+r)**period))
        last_wc, last_ebit = wc, ebit
    terminal = 0.0 if abandon else rows[-1]["free_cash_flow"]*(1+g)/(r-g)
    pv_terminal = 0.0 if abandon else terminal/(1+r)**(LAST_YEAR-YEAR_ZERO)
    pv_explicit = sum(x["pv_free_cash_flow"] for x in rows)
    return dict(scenario=scenario_name, discount_rate=r, expand=expand, abandon=abandon,
        rows=rows, terminal_value=terminal, pv_terminal_value=pv_terminal,
        pv_explicit=pv_explicit, npv=pv_explicit+pv_terminal)


def calculate_all(a: dict) -> dict:
    cases = {}
    for key, rate, extra in [
        ("base", None, 0), ("inflation_plus_1pp", None, .01),
        ("discount_10pct", .10, 0), ("combined", .10, .01)
    ]:
        opt = forecast("optimistic", a, rate=rate, inflation_extra=extra)
        pes = forecast("pessimistic", a, rate=rate, inflation_extra=extra)
        cases[key] = dict(optimistic=opt, pessimistic=pes,
            expected_npv=opt["npv"]*.4+pes["npv"]*.6)
    expanded = forecast("optimistic", a, expand=True)
    abandoned = forecast("pessimistic", a, abandon=True)
    best_opt = max([expanded, cases["base"]["optimistic"]], key=lambda x:x["npv"])
    best_pes = max([abandoned, cases["base"]["pessimistic"]], key=lambda x:x["npv"])
    expected = .4*best_opt["npv"]+.6*best_pes["npv"]
    return dict(cases=cases, option_branches={"optimistic_expand":expanded,
        "pessimistic_abandon":abandoned}, optimal_branches={"optimistic":best_opt,
        "pessimistic":best_pes}, expected_with_options=expected,
        option_value=expected-cases["base"]["expected_npv"])
