from PyQt5 import QtCore, QtGui, QtWidgets

class ButtonsGroup(QtWidgets.QBoxLayout):
    def __init__(self) -> None:
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
    
    def load_buttons(self, buttons: list[QtWidgets.QCheckBox]):
        shape = (2, len(buttons) + len(buttons) % 2)

        for n, button in enumerate(buttons):
            
            row = int(n > len(buttons) / shape[0]) + 1
            col = n - shape[1] * row

            self.addWidget(button, 0, 2, row, col)
