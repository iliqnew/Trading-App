from PyQt5 import QtCore, QtGui, QtWidgets

from .ButtonsGroup import ButtonsGroup
from .Graph import Graph


class TickerBox(QtWidgets.QVBoxLayout):
    def __init__(self) -> None:
        self.graph = Graph()
        self.buttons_group = ButtonsGroup()

        self.setup()
    
    def load(self, ticker):
        self.graph.load(ticker)

    def setup_graph(self):
        print("Setting up graph...")
        self.addWidget(self.graph)

    def setup_buttons_group(self):
        print("Setting up buttons...")
        self.addWidget(self.buttons_group)

    def setup(self):
        self.setup_graph()
        self.setup_buttons_group()
