import datetime
from abc import ABC, abstractmethod

import pandas as pd
import pandas_datareader.data as web
from pandas import DataFrame

class Ticker(ABC):
    _symbol: str
    _data: DataFrame

    @abstractmethod
    def _get_historical_data(self, data_source: int="yahoo") -> DataFrame:
        """Webscrapes the data for the particular ticker and period in yahoo finance"""
    
    @abstractmethod
    def get_data_period(self,
                        start_date: str = datetime.datetime(1970, 1, 1).strftime('%Y-%m-%d'),
                        end_date: str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                        ) -> DataFrame:
        """Returns a certain period chunk of the data"""

class YahooTicker(Ticker):
    def __init__(self, symbol: str) -> None:
        self._symbol = symbol
        self._data = self._get_historical_data("yahoo")
    
    def __str__(self) -> str:
        return self._symbol
    
    def _get_historical_data(self, data_source: str="yahoo") -> DataFrame:
        # Scraping the historical data from yahoo
        print(self._symbol)
        raw_df = web.DataReader(self._symbol, data_source)
        
        # Formating the raw data to DataFrame
        df = DataFrame(raw_df)
        
        # Converting the data to float
        for col in df.columns:
            df[col] = df[col].astype(float)
        
        # Converting the indices to date_time strings
        df.index = pd.to_datetime(df.index)

        return df

    def get_data_period(self,
                        start_date: str = "1970-01-01",
                        end_date: str = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                        ) -> DataFrame:
        # Geting the period of interest
        data = self._data
        data = data[data.index >= start_date]
        data = data[data.index <= end_date]

        return(data)