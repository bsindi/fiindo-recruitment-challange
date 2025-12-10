from api_client import get_tickers, get_ticker_details
from processing import calculate_ticker_stats
from db import SessionLocal, init_db
from models import TickerStatistics, IndustryAggregations
from statistics import mean


TARGET_INDUSTRIES = [
    "Banks - Diversified",
    "Software - Application",
    "Consumer Electronics"
]


def save_ticker_stats(stats_list):
    """Speichert berechnete Ticker-Daten in die SQLite-Datenbank."""
    session = SessionLocal()
    try:
        for stats in stats_list:
            existing = session.query(TickerStatistics).filter_by(symbol=stats["symbol"]).first()
            if existing:
                print(f"{stats['symbol']} existiert bereits, wird übersprungen.")
                continue

            ticker = TickerStatistics(
                symbol=stats["symbol"],
                industry=stats["industry"],
                pe_ratio=stats["pe_ratio"],
                revenue_growth=stats["revenue_growth"],
                net_income_ttm=stats["net_income_ttm"],
                debt_ratio=stats["debt_ratio"]
            )
            session.add(ticker)
        session.commit()
        print("Ticker-Daten gespeichert.")
    finally:
        session.close()


def save_industry_aggregations(aggregations):
    """Speichert aggregierte Branchenwerte in die SQLite-Datenbank."""
    session = SessionLocal()
    try:
        for agg in aggregations:
            existing = session.query(IndustryAggregations).filter_by(industry=agg["industry"]).first()
            if existing:
                print(f"{agg['industry']} existiert bereits, wird übersprungen.")
                continue

            industry = IndustryAggregations(
                industry=agg["industry"],
                avg_pe_ratio=agg["avg_pe_ratio"],
                avg_revenue_growth=agg["avg_revenue_growth"],
                total_revenue=agg["total_revenue"]
            )
            session.add(industry)
        session.commit()
        print("Industrie-Aggregationen gespeichert.")
    finally:
        session.close()


def calculate_industry_aggregations(ticker_stats):
    """Berechnet Durchschnittswerte und Summen pro Industrie."""
    industries = {}
    for stats in ticker_stats:
        industry = stats["industry"]
        if industry not in industries:
            industries[industry] = {
                "pe_ratios": [],
                "revenue_growths": [],
                "revenues": []
            }
        if stats["pe_ratio"] is not None:
            industries[industry]["pe_ratios"].append(stats["pe_ratio"])
        if stats["revenue_growth"] is not None:
            industries[industry]["revenue_growths"].append(stats["revenue_growth"])
        if stats["net_income_ttm"] is not None:
            industries[industry]["revenues"].append(stats["net_income_ttm"])

    aggregations = []
    for industry, values in industries.items():
        agg = {
            "industry": industry,
            "avg_pe_ratio": mean(values["pe_ratios"]) if values["pe_ratios"] else None,
            "avg_revenue_growth": mean(values["revenue_growths"]) if values["revenue_growths"] else None,
            "total_revenue": sum(values["revenues"]) if values["revenues"] else None
        }
        aggregations.append(agg)

    return aggregations


def main():
    """Hauptfunktion: API-Daten holen, berechnen und speichern."""
    tickers = get_tickers()
    print(f"{len(tickers)} Ticker abgerufen.")

    results = []
    for ticker in tickers:
        if ticker["industry"] not in TARGET_INDUSTRIES:
            continue
        details = get_ticker_details(ticker["symbol"])
        stats = calculate_ticker_stats(details)
        if stats:
            results.append(stats)

    print(f"{len(results)} Ticker verarbeitet.")

    save_ticker_stats(results)
    aggregations = calculate_industry_aggregations(results)
    save_industry_aggregations(aggregations)

    print("Daten erfolgreich berechnet und gespeichert.")


if __name__ == "__main__":
    init_db()

    dummy_tickers = [
        {
            "symbol": "AAPL",
            "industry": "Consumer Electronics",
            "pe_ratio": 28.5,
            "revenue_growth": 0.07,
            "net_income_ttm": 95000.0,
            "debt_ratio": 1.2
        },
        {
            "symbol": "MSFT",
            "industry": "Software - Application",
            "pe_ratio": 30.2,
            "revenue_growth": 0.09,
            "net_income_ttm": 85000.0,
            "debt_ratio": 0.8
        },
        {
            "symbol": "JPM",
            "industry": "Banks - Diversified",
            "pe_ratio": 12.8,
            "revenue_growth": 0.03,
            "net_income_ttm": 35000.0,
            "debt_ratio": 2.1
        }
    ]

    dummy_aggregations = calculate_industry_aggregations(dummy_tickers)

    save_ticker_stats(dummy_tickers)
    save_industry_aggregations(dummy_aggregations)

    print("Dummy-Daten und Aggregationen gespeichert.")
