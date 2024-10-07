import json
import os

from loguru import logger

from market_router import utils
from market_neutral import baseline_system_prompt_tpl


def get_model_predictions(news: str, tickers: list, instance_id: str = None) -> list:
    if not instance_id:
        instance_id = os.getenv("INSTANCE_ID")

    api_key = os.getenv("MARKET_ROUTER_KEY")

    decisions = []

    for ticker in tickers:
        baseline_prompt = _format_baseline_prompt(news, ticker.name)

        predictions = utils.get_predictions(baseline_prompt, api_key, instance_id)

        decision = _get_decision(predictions)

        decisions.append({"ticker": ticker, "decision": decision})

        logger.info(f"Predictions: {predictions['response']['choices'][0]['message']['content']}")

    return decisions


def _format_baseline_prompt(news: str, ticker: str):
    return baseline_system_prompt_tpl.replace("{news}", news).replace("{name}", ticker)


def _get_decision(response: str) -> str:
    try:
        content = response["response"]["choices"][0]["message"]["content"]

        return json.loads(content)["action"]

    except (json.JSONDecodeError, KeyError, IndexError) as e:
        logger.error(f"Error decoding response: {e}")
        return None
