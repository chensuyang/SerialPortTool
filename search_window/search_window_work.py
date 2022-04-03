from PyQt5 import QtCore, QtWidgets
import search_window
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
import time
from setting import setting


class SearchWindowWork(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = search_window.Ui_MainWindow()
        self.ui.setupUi(self)
