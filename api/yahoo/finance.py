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

    def get_key_stats(self) -> dict:
        stats: list = [
            "previousClose",
            "open",
            "bid",
            "ask",
            "52WeekChange",
            "volume",
            "averageVolume",
            "marketCap",
            "pegRatio",
            "ebitda",
            "longBusinessSummary",
        ]
        key_stats: dict = {}
        for stat in stats:
            key_stats[stat] = self.data[stat]

        return key_stats

    def get_data_for_graph(self) -> dict:
        df = self.get_stock().history("1mo", "1d")["Open"]
        history_data: dict = {}
        for key, value in df.to_dict().items():
            history_data[str(key.date())] = value

        return history_data  # Y axis = date, X axis = value


# aapl = Stock("GAZP")
# pprint(aapl.get_info())
# pprint(aapl.get_key_stats())
# print(aapl.get_current_price())
# print(aapl.get_price_change_percent())
# print(aapl.get_stock_logo())
# print(aapl.get_data_for_graph())
