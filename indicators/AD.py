from Indicator import Indicator, DataFrame

class AD(Indicator):
    def get(self, data: DataFrame) -> DataFrame:
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