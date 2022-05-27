from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from pandas.core.frame import DataFrame
from PyQt5 import QtCore, QtGui, QtWidgets

from Controller import Controller
from Model import Model
from View import QtWidgets, View
from widgets.TickerBox import TickerBox


class Subject:
    _observers: List[Observer]
    _model: Model

    def __init__(self, model: Model) -> None:
        self._observers= []
        self._model = model
    
    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, subject: Subject):
        for observer in self._observers:
            observer.update(subject)

    def update(self):
        pass

class Observer:
    _subject: Subject

    def update(self, subject: Subject):
        self._subject = subject

class View(QtWidgets.QMainWindow, Observer):
    _ticker_boxes: List[TickerBox] = []

    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("MainWindow")
        self.showFullScreen()
        self.showMaximized()

    def attach(self, ticker_box: TickerBox):
        self._ticker_boxes.append(ticker_box)
    
    def detach(self, ticker_box: TickerBox):
        self._ticker_boxes.remove(ticker_box)
    
    def update(self):
        for n, ticker in enumerate(self._subject):
            print(ticker)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())

"""
class Main:
    def __init__(self, controller):
        self.controller = controller
    
    def setup(self):
        self.controller.view.setup([])
    
    def run(self):
        self.controller.start()
    

if __name__ == '__main__':
    import sys

    model = Model()

    app = QtWidgets.QApplication(sys.argv)
    view = View()
    
    controller = Controller(model, view)

    m = Main(controller)
    m.setup()
    m.run()

    sys.exit(app.exec_())
"""
