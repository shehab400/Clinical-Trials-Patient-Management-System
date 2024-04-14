import sys
from PyQt5 import QtWidgets, uic
import pyqtgraph as pg


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("GUI\Gui.ui", self)