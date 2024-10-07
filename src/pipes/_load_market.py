import pandas as pd
from loguru import logger

from market_router import MARKET_DIR


def load_market(market: str) -> pd.DataFrame:
    filepath = f"{MARKET_DIR}/{market}.csv"

    return pd.read_csv(filepath)
