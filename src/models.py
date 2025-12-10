"""Database models for the Fiindo recruitment challenge."""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TickerStatistics(Base):
    """Stores calculated statistics for individual stock tickers."""
    __tablename__ = "ticker_statistics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, unique=True, nullable=False)
    industry = Column(String, nullable=False)

    pe_ratio = Column(Float)
    revenue_growth = Column(Float)
    net_income_ttm = Column(Float)
    debt_ratio = Column(Float)

    def __repr__(self):
        return f"<TickerStatistics(symbol={self.symbol}, industry={self.industry})>"


class IndustryAggregations(Base):
    """Stores aggregated statistics for each industry."""
    __tablename__ = "industry_aggregations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    industry = Column(String, unique=True, nullable=False)

    avg_pe_ratio = Column(Float)
    avg_revenue_growth = Column(Float)
    total_revenue = Column(Float)

    def __repr__(self):
        return f"<IndustryAggregations(industry={self.industry})>"
