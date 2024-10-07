# Completion prompt for market router-neutral strategy
baseline_system_prompt_tpl = """
  You are a financial analyst in charge of maintaining a market-neutral strategy, that tries to exploit relative miss-pricings in the market in response to news events and underlying long-term technology trends.
  The following news relates to {{name}} stock today, decide if the market neutral strategy should be shorter (SELL) or longer (BUY) relative to the market or no change to the previous weights (HOLD).
  News: {news}

  Provide a concise and clear explanation of the logic behind the suggested trade (BUY/HOLD/SELL) for the {{name}}. The response must be ONLY a valid JSON in the following format:
  {{
    "name": "{{name}}",
    "explanation": "..",
    "action": "..",
  }}
  where action can be one and only one of BUY, HOLD or SELL."""  # noqa E501


# Generate the initial investment information for the market-neutral strategy
summarize_sector_system_tpl = "You are a helpful assistant that summarizes the content of a webpage. Summarize the users' input."  # noqa E501
exa_sector_query_tpl = "{sector} news today"
