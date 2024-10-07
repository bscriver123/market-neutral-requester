from dataclasses import dataclass


@dataclass(frozen=True)
class TickerDTO:
    name: str
    symbol: str
    sector: str
    sub_industry: str
    market: str
