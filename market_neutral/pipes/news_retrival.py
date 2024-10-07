from typing import List

from loguru import logger

from market_router.objects import SectorNews


def sector_news_retrival(sector: str, eval_date: str) -> List:
    logger.info("Started Downloading sector news")
    try:
        sector_news = SectorNews(sector, eval_date=eval_date).get()
        logger.info("Finished downloading sector news")
        return sector_news
    except Exception as e:
        logger.exception(f"Could not retrieve the sector news due to: {e}")
