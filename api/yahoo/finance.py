import json
from pprint import pprint
import yfinance as yf


class Stock:
    def __init__(self, ticker: str) -> None:
        self.ticker: str = ticker
        self.data: dict = self.get_info()

    def get_stock(self) -> yf.Ticker:
        return yf.Ticker(self.ticker)

    def get_info(self) -> dict:
        return self.get_stock().info

    def get_current_price(self) -> float:
        return self.data["currentPrice"]

    def get_open_price(self) -> float:
        return self.data["open"]

    def get_previous_close(self) -> float:
        return self.data["previousClose"]

    def get_price_change_percent(self) -> float:
        return (self.get_current_price() / self.get_open_price()) * 100 - 100

    def get_price_change_abs(self) -> float:
        return self.get_current_price() - self.get_open_price()

    def get_stock_logo(self) -> str:
        return self.data["logo_url"]


# aapl = Stock("aapl")
# # info = aapl.get_info()
# print(aapl.get_current_price())
# print(aapl.get_price_change_abs())
# print(aapl.get_stock_logo())
