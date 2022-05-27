import pandas as pd

from .BaseIndicator import DataFrame, BaseIndicator
from .SMA import SMA


class ABANDS(Indicator):
    def get(self, data: DataFrame, price: str = "Close") -> DataFrame:
        """
        Formula
        Upper Band = Simple Moving Average (High * ( 1 + 4 * (High - Low) / (High + Low)))

        Middle Band = Simple Moving Average

        Lower Band = Simple Moving Average (Low * (1 - 4 * (High - Low)/ (High + Low)))
        """
        
        abands = DataFrame()

        upper_band = data["High"] * (1 + 4 * (data["High"] - data["Low"]) / (data["High"] + data["Low"]))
        middle_band = data[price]
        lower_band = data["Low"] * (1 - 4 * (data["High"] - data["Low"]) / (data["High"] + data["Low"]))
        
        abands["Upper Band"] = upper_band
        abands["Middle Band"] = middle_band
        abands["Lower Band"] = lower_band
        
        abands["Upper Band"] = SMA().get(abands["Upper Band"])
        abands["Middle Band"] = SMA().get(abands["Middle Band"])
        abands["Lower Band"] = SMA().get(abands["Lower Band"])
        
        print(abands)
