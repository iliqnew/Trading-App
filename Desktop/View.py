
from PyQt5 import QtCore, QtGui, QtWidgets

from widgets.TickerBox import TickerBox

class View(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("MainWindow")
        self.showFullScreen()
        self.showMaximized()

        self.ticker_boxes = {}
    
    def setup(self, ticker_boxes: list[TickerBox]):
        print("Setting up ticker boxes...")
        for tb in ticker_boxes:
            print(tb)
    
    def update(self, tickers):
        for ticker in tickers:
            self.ticker_boxes.graph = ticker.graph
        

if __name__ == "__main__":
    import sys
    from Model import Model

    app = QtWidgets.QApplication(sys.argv)
    
    view = View()
    view.setup(Model().tickers)
    
    sys.exit(app.exec_())
