from typing import List, Optional

import pandas as pd
from loguru import logger

from market_router.expections import MarketAssetError
from src.schemas.ticker import TickerDTO


def _get_tickers_by_filters(
    market: pd.DataFrame, sector: str, limit: Optional[int] = None
) -> List[TickerDTO]:
    sector_market = market[market["sector"] == sector]
    tickers = sector_market.head(limit) if limit is not None else sector_market
    return [
        TickerDTO(
            name=row["company_name"],
            symbol=row["symbol"],
            sector=row["sector"],
            sub_industry=row["sub_industry"],
            market=row["market_cap"],
        )
        for _, row in tickers.iterrows()
    ]


def market_assets(market: pd.DataFrame, sector: str, top: Optional[int] = None) -> list[TickerDTO]:
    try:
        logger.info("Started getting market assets")

        tickers: list[TickerDTO] = []

        tickers = _get_tickers_by_filters(market, sector, top)

        logger.info("Finished getting market assets")

        return tickers
    except Exception as e:
        logger.error(f"Unable to retrieve market assets: {e}")
        raise MarketAssetError(f"Unable to retrieve market assets: {e}")
