from PyQt5 import QtCore, QtGui, QtWidgets

import sys
sys.path.append(".")

from Ticker import YahooTicker

import threading

class Model:
    def __init__(self) -> None:
        self.tickers = []

    def get_all_stocks_names(self):
        """TODO"""
        return ["TSLA", "AAPL", "GOOGL"]

    def get_all_cryptocurrencies_names(self):
        """TODO"""
        return ["BTC-USD", "ETH-USD"]

    def get_all_tickers_names(self):
        
        stocks = self.get_all_stocks_names()
        cryptocurrencies = self.get_all_cryptocurrencies_names()

        return stocks + cryptocurrencies
    
    def build_ticker_object(self, ticker_name):
        self.tickers.append(YahooTicker(ticker_name))

    def build_ticker_objects(self, tickers_names):
        for t_name in tickers_names:
            thread = threading.Thread(target=self.build_ticker_object, args=(t_name,))
            thread.start()
        

if __name__ == "__main__":
    pass