import datetime
import os

from numpy import average
from pandas import DataFrame

os.curdir = "\."

import datetime
from abc import ABC, abstractmethod

from pandas import DataFrame
from Ticker import Ticker


class IIndicator(ABC):
    """Basic representation of an indicator"""
    indicators: list

    @abstractmethod
    def get(self,
            data: DataFrame,
            period: int = 3,
            start_date: str = datetime.datetime(1975, 1, 1).strftime('%Y-%m-%d'),
            end: str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            price: str = "Close"
            ) -> DataFrame:
        """
        The function/formula of the particular indicator.
        It returns the processed data
        """

class PV(IIndicator):
    def get(self,
            data: DataFrame,
            period: int = 3,
            start_date: str =  datetime.datetime(1975, 1, 1).strftime('%Y-%m-%d'),
            end_date: str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            price: str = "Close"
            ) -> DataFrame:
        """
        Formula:
        PV = PH - PL
        
        where:
        PH - Period High
        PL - Period Low
        """
        
        #data = stock.get_data_period(start_date=start_date, end_date=end_date)

        #pv = stock.get_data_period(start_date=start_date, end_date=end_date)
        
        pv = data

        for col in pv.columns:
            column_pv = pv[col]
            for i in range(period, len(col)):
                data_period = pv[col][i - period : i]
                column_pv[i] = max(data_period) - min(data_period)
            pv[col] = column_pv
        
        return pv

class ABANDS(IIndicator):
    def get(self,
            data: DataFrame,
            period: int = 3,
            start_date: str = datetime.datetime(1975, 1, 1).strftime('%Y-%m-%d'),
            end_date: str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            price: str = "Close"
            ) -> DataFrame:
        """
        Formula
        Upper Band = Simple Moving Average (High * ( 1 + 4 * (High - Low) / (High + Low)))

        Middle Band = Simple Moving Average

        Lower Band = Simple Moving Average (Low * (1 - 4 * (High - Low)/ (High + Low)))
        """
        #data = stock.get_historical_data(start_date = start_date, end_date = end_date)

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
        
        return abands
    
class AD(IIndicator):
    def get(self,
            data: DataFrame,
            period: int = 3,
            start_date: str = datetime.datetime(1975, 1, 1).strftime('%Y-%m-%d'),
            end_date: str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            price: str = "Close"
            ) -> DataFrame:
        """
        Accumulation/Distribution (AD)

        Formula
        PV = PH - PL
        MFM = ((Close - Low) - (High - Close)) / PV
        MFV = MFM * PV
        AD = cumulative (MFM * Volume)

        where:
        PH - Period High
        PL - Period Low
        PV - Period Volume
        MFM - Money Flow Multiplier
        MFV = Money Flow Volume

        """

        ad = DataFrame()
        return ad

class SMA(IIndicator):
    def get(self,
            data: DataFrame,
            period: int = 3,
            start_date: str = datetime.datetime(1975, 1, 1).strftime('%Y-%m-%d'),
            end_date: str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            price: str = "Close"
            ) -> DataFrame:
        """
        Formula
        SMA = ( Sum ( Price, n ) ) / n    

        Where: period = Time Period
        """
        # Converting data from series to dataframe type
        data = DataFrame(data)
        
        # Setting the value of sma to be equal to the values of data (we just need its shape to be the same)
        sma = data

        # Looping through every column
        for col in data.columns[1:]:
            # Looping through every row/value of the column
            for end_i in range(period, len(col)):
                # Getting the data in the time period [i-n, ..., i]
                time_period_data = data[col][end_i-period : end_i]
                # Calculating the average value of the data chunk
                sma[col][end_i] = average(time_period_data)
        
        return sma

class EMA(IIndicator):
    def get(self,
            data: DataFrame,
            period: int = 3,
            start_date: str = datetime.datetime(1975, 1, 1).strftime('%Y-%m-%d'),
            end_date: str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            price: str = "Close"
            ) -> DataFrame:
        """
        Formula
        EMA = ( ( Price - Previous EMA ) x Multiplier + Previous EMA )

        Where:
        Multiplier = 2 / ( n + 1 )
        """
        # Converting data from series to dataframe type
        data = DataFrame(data)
        
        # Setting the value of sma to be equal to the values of data (we just need its shape to be the same)
        ema = data

        # Looping through every column
        for col in data.columns[1:]:
            # Looping through every row/value of the column
            for end_i in range(period, len(col)):
                # Getting the data in the time period [i-n, ..., i]
                time_period_data = data[col][end_i-period : end_i]
                # Calculating the average value of the data chunk
                ema[col][end_i] = average(time_period_data)
        
        return ema


