from plugin.esp32_backtrace_viewer import esp32_backtrace_viewer
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox

# 插件名字(必须存在),会显示在软件界面
NAME = "ESP32 backtrace显示器"

class PluginWindowWork(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = esp32_backtrace_viewer.Ui_Form()
        self.ui.setupUi(self)


def init(tab_widget):
    plugin_window = PluginWindowWork()

    tab_widget.addTab(plugin_window, "ESP32 backtrace显示器")
    # tab_widget.setCurrentWidget(plugin_window)


def uart_rev_data(bytes_data):
    ret = True
    discard = False
    out = None

    return ret, discard, out
