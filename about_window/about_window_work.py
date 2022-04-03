from PyQt5 import QtCore, QtWidgets
import about_window
from PyQt5.QtCore import QTimer


class AboutWindowWork(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = about_window.Ui_MainWindow()
        self.ui.setupUi(self)
