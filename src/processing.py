def calculate_ticker_stats(ticker_data):
    """Calculate financial metrics for one ticker."""
    try:
        price = ticker_data["price"]
        eps = ticker_data["earnings_per_share"]
        revenue_q1 = ticker_data["revenue_q1"]
        revenue_q2 = ticker_data["revenue_q2"]
        net_incomes = ticker_data["net_income_last_4_quarters"]
        total_debt = ticker_data["total_debt"]
        total_equity = ticker_data["total_equity"]

        pe_ratio = price / eps if eps else None
        revenue_growth = ((revenue_q1 - revenue_q2) / revenue_q2) if revenue_q2 else None
        net_income_ttm = sum(net_incomes)
        debt_ratio = total_debt / total_equity if total_equity else None

        return {
            "symbol": ticker_data["symbol"],
            "industry": ticker_data["industry"],
            "pe_ratio": pe_ratio,
            "revenue_growth": revenue_growth,
            "net_income_ttm": net_income_ttm,
            "debt_ratio": debt_ratio,
        }

    except KeyError as e:
        print(f"Missing key: {e}")
        return None
