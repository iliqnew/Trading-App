from indicators.Indicators import PV, ABANDS, AD
from Stock import Stock

stock = Stock("GOOGL")
#print(stock._data)
#SMA().get(stock)
#ABANDS().get(stock, 3)
print(ABANDS().get(PV().get(stock._data)))
