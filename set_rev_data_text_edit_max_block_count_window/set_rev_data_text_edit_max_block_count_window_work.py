from PyQt5 import QtCore, QtWidgets
import main_window
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QDesktopWidget
from PyQt5.QtCore import QTimer
from set_rev_data_text_edit_max_block_count_window import set_rev_data_text_edit_max_block_count_window
from setting import setting

class SetRevDataTextEditMaxBlockCountWindowWork(QtWidgets.QMainWindow):
    close_signal = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = set_rev_data_text_edit_max_block_count_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.clear()


    def add_block_count(self,block_count):
        self.ui.comboBox.addItem(str(block_count))

