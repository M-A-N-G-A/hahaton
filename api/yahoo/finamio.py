from datetime import datetime
from finam import Exporter, Market, LookupComparator, export
from finam.const import Timeframe
from pandas.core.frame import DataFrame

START_FROM = datetime.strptime("2021-10-27", "%Y-%m-%d").date()
exporter = Exporter()


class Currency:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.data: DataFrame = self.get_data()

    def get_data(self) -> DataFrame:
        lookup = exporter.lookup(name=self.name, market=Market.CURRENCIES)

        data: DataFrame = exporter.download(
            lookup.index[0],
            start_date=START_FROM,
            market=Market.CURRENCIES,
        )
        return data

    def get_current_price(self) -> DataFrame:
        return self.get_data().tail(1)

    def get_history(self) -> DataFrame:
        return self.get_data()


# rub = Currency("USDRUB_TOD")
# print(rub.get_current_price())
# print(rub.get_history())


class Bond:
    def __init__(self, name: str):
        self.name = name
        self.data = self.get_data()

    def get_data(self):
        lookup = exporter.lookup(name=self.name, market=Market.BONDS)
        data = exporter.download(
            lookup.index[0], start_date=START_FROM, market=Market.BONDS
        )
        return data

    def get_current_price(self):
        return self.get_data().tail(1)

    def get_history(self):
        return self.get_data()


# ofz = Bond("ОФЗ 25083")
# print(ofz.get_data())


class EtfMoex:
    def __init__(self, name):
        self.name = name
        self.data = self.get_data()

    def get_data(self):
        lookup = exporter.lookup(name=self.name, market=Market.ETF_MOEX)
        data = exporter.download(
            lookup.index[0], start_date=START_FROM, market=Market.ETF_MOEX
        )
        return data

    def get_current_price(self):
        return self.get_data().tail(1)

    def get_history(self):
        return self.get_data()


# etf = EtfMoex("FXRU ETF")
# print(etf.get_current_price())


class Share:
    def __init__(self, name):
        self.name = name
        self.data = self.get_data()

    def get_data(self):
        lookup = exporter.lookup(name=self.name, market=Market.SHARES)
        data = exporter.download(
            lookup.index[0], start_date=START_FROM, market=Market.SHARES
        )
        return data

    def get_current_price(self):
        return self.get_data().tail(1)

    def get_history(self):
        return self.get_data()


aero = Share("Аэрофлот")
print(aero.get_current_price())
print(aero.get_history())
