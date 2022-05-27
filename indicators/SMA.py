from numpy import average

from .Indicator import DataFrame, Indicator


class SMA(Indicator):
    def get(self, data: DataFrame, period: int = 3) -> DataFrame:
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
