import argparse
import sys
from datetime import datetime

from loguru import logger

from src import pipes

_TOP_N = 10


def sector_market_pipeline(market: str, date: str, sector: str, instance_id: str = None):
    try:
        logger.info("Started sector market pipeline")

        market = pipes.load_market(market)

        tickers = pipes.market_assets(market=market, sector=sector, top=_TOP_N)

        sector_news = pipes.sector_news_retrival(sector, date)

        decisions = pipes.get_model_predictions(sector_news, tickers, instance_id=instance_id)

        logger.info("Finished sector market pipeline")

        return decisions

    except Exception as e:
        raise e


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=("Market pipeline that predicts the action to be done BEFORE opening.")
    )
    parser.add_argument(
        "--market", type=str, help="Markets to explore", choices=["sp500"], required=True
    )
    parser.add_argument(
        "--date", default=datetime.today().strftime("%Y-%m-%d"), type=str, help="Date of interest"
    )

    parser.add_argument(
        "--sector", type=str, help="Sector of interest: e.g. Industrials", required=True
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    try:
        args = parse_arguments()
        sector_market_pipeline(args.market, args.date, args.sector)
    except Exception as e:
        logger.error(f"The pipeline raised the following error: {e}")
        sys.exit(1)
