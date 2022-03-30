# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 835)
        MainWindow.setMinimumSize(QtCore.QSize(1240, 835))
        MainWindow.setMaximumSize(QtCore.QSize(1240, 835))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.UartNumber_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.UartNumber_comboBox.setGeometry(QtCore.QRect(60, 10, 351, 31))
        self.UartNumber_comboBox.setObjectName("UartNumber_comboBox")
        self.OpenUartpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.OpenUartpushButton.setGeometry(QtCore.QRect(420, 10, 81, 31))
        self.OpenUartpushButton.setObjectName("OpenUartpushButton")
        self.RevDatatextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.RevDatatextEdit.setGeometry(QtCore.QRect(10, 120, 951, 441))
        self.RevDatatextEdit.setObjectName("RevDatatextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.BaudRate_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.BaudRate_comboBox.setGeometry(QtCore.QRect(90, 50, 141, 31))
        self.BaudRate_comboBox.setObjectName("BaudRate_comboBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.RTS_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.RTS_CheckBox.setGeometry(QtCore.QRect(240, 50, 51, 31))
        self.RTS_CheckBox.setObjectName("RTS_CheckBox")
        self.DTR_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.DTR_CheckBox.setGeometry(QtCore.QRect(300, 50, 51, 31))
        self.DTR_CheckBox.setObjectName("DTR_CheckBox")
        self.SendDatatextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.SendDatatextEdit.setGeometry(QtCore.QRect(10, 590, 951, 161))
        self.SendDatatextEdit.setObjectName("SendDatatextEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 570, 71, 16))
        self.label_4.setObjectName("label_4")
        self.SendDatapushButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendDatapushButton.setGeometry(QtCore.QRect(800, 760, 161, 31))
        self.SendDatapushButton.setObjectName("SendDatapushButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(970, 0, 271, 791))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(710, 760, 101, 31))
        self.checkBox.setObjectName("checkBox")
        self.UartTxPlugin_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.UartTxPlugin_comboBox.setGeometry(QtCore.QRect(260, 760, 241, 31))
        self.UartTxPlugin_comboBox.setObjectName("UartTxPlugin_comboBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 752, 241, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.UartRxPlugin_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.UartRxPlugin_comboBox.setGeometry(QtCore.QRect(720, 88, 241, 31))
        self.UartRxPlugin_comboBox.setObjectName("UartRxPlugin_comboBox")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 80, 241, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1240, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menuBar)
        self.actionsez = QtWidgets.QAction(MainWindow)
        self.actionsez.setObjectName("actionsez")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_2.addAction(self.action_8)
        self.menu_3.addAction(self.action_9)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口工具"))
        self.label.setText(_translate("MainWindow", "串口:"))
        self.OpenUartpushButton.setText(_translate("MainWindow", "打开串口"))
        self.label_2.setText(_translate("MainWindow", "波特率:"))
        self.label_3.setText(_translate("MainWindow", "接收内容:"))
        self.RTS_CheckBox.setText(_translate("MainWindow", "RTS"))
        self.DTR_CheckBox.setText(_translate("MainWindow", "DTR"))
        self.label_4.setText(_translate("MainWindow", "发送内容:"))
        self.SendDatapushButton.setText(_translate("MainWindow", "发送数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.checkBox.setText(_translate("MainWindow", "HEX形式发送"))
        self.label_5.setText(_translate("MainWindow", "当前使用的数据发送修饰器:"))
        self.label_6.setText(_translate("MainWindow", "当前使用的数据接收修饰器:"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "插件"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.actionsez.setText(_translate("MainWindow", "sez"))
        self.action.setText(_translate("MainWindow", "打开文件并作为虚拟串口接收数据"))
        self.action_2.setText(_translate("MainWindow", "设置保存接收数据时的文件目录"))
        self.action_4.setText(_translate("MainWindow", "打开插件目录"))
        self.action_5.setText(_translate("MainWindow", "打开数据接收修饰器目录"))
        self.action_6.setText(_translate("MainWindow", "打开数据发送修饰器目录"))
        self.action_7.setText(_translate("MainWindow", "管理插件与修饰器"))
        self.action_8.setText(_translate("MainWindow", "安装插件或修饰器"))
        self.action_9.setText(_translate("MainWindow", "关于本软件"))