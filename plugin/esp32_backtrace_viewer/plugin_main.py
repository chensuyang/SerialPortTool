from plugin.esp32_backtrace_viewer import esp32_backtrace_viewer
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox


class PluginWindowWork(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = esp32_backtrace_viewer.Ui_Form()
        self.ui.setupUi(self)


def init(tab_widget):
    plugin_window = PluginWindowWork()

    tab_widget.addTab(plugin_window, "ESP32 backtrace显示器")
    # tab_widget.setCurrentWidget(plugin_window)
