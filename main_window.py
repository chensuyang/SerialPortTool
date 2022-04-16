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
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(40960, 20480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 8, 1, 1)
        self.RevDataTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.RevDataTextEdit.setAcceptDrops(False)
        self.RevDataTextEdit.setLineWidth(1)
        self.RevDataTextEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.RevDataTextEdit.setObjectName("RevDataTextEdit")
        self.gridLayout.addWidget(self.RevDataTextEdit, 4, 0, 3, 9)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.RTS_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.RTS_CheckBox.setFont(font)
        self.RTS_CheckBox.setObjectName("RTS_CheckBox")
        self.gridLayout.addWidget(self.RTS_CheckBox, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.UartNumber_comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.UartNumber_comboBox.setFont(font)
        self.UartNumber_comboBox.setObjectName("UartNumber_comboBox")
        self.gridLayout.addWidget(self.UartNumber_comboBox, 0, 1, 1, 5)
        self.SendDatatextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.SendDatatextEdit.setObjectName("SendDatatextEdit")
        self.gridLayout.addWidget(self.SendDatatextEdit, 8, 0, 1, 9)
        self.Save_Window_Data_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_Window_Data_Button.setObjectName("Save_Window_Data_Button")
        self.gridLayout.addWidget(self.Save_Window_Data_Button, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 10, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)
        self.UartTxPlugin_comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.UartTxPlugin_comboBox.setFont(font)
        self.UartTxPlugin_comboBox.setObjectName("UartTxPlugin_comboBox")
        self.gridLayout.addWidget(self.UartTxPlugin_comboBox, 9, 2, 1, 5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 600, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 7, 1, 1)
        self.UartRxPlugin_comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.UartRxPlugin_comboBox.setFont(font)
        self.UartRxPlugin_comboBox.setObjectName("UartRxPlugin_comboBox")
        self.gridLayout.addWidget(self.UartRxPlugin_comboBox, 3, 7, 1, 2)
        self.DTR_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.DTR_CheckBox.setFont(font)
        self.DTR_CheckBox.setObjectName("DTR_CheckBox")
        self.gridLayout.addWidget(self.DTR_CheckBox, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 2)
        self.SendDatapushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.SendDatapushButton.setFont(font)
        self.SendDatapushButton.setObjectName("SendDatapushButton")
        self.gridLayout.addWidget(self.SendDatapushButton, 9, 8, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 1, 10, 9, 1)
        self.OpenUartpushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.OpenUartpushButton.setFont(font)
        self.OpenUartpushButton.setObjectName("OpenUartpushButton")
        self.gridLayout.addWidget(self.OpenUartpushButton, 0, 6, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 9, 7, 1, 1)
        self.BaudRate_comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.BaudRate_comboBox.setFont(font)
        self.BaudRate_comboBox.setObjectName("BaudRate_comboBox")
        self.gridLayout.addWidget(self.BaudRate_comboBox, 1, 1, 1, 3)
        self.Save_Rev_Data_CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.Save_Rev_Data_CheckBox.setFont(font)
        self.Save_Rev_Data_CheckBox.setObjectName("Save_Rev_Data_CheckBox")
        self.gridLayout.addWidget(self.Save_Rev_Data_CheckBox, 2, 3, 1, 3)
        self.ClearRevWinDataButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.ClearRevWinDataButton.setFont(font)
        self.ClearRevWinDataButton.setObjectName("ClearRevWinDataButton")
        self.gridLayout.addWidget(self.ClearRevWinDataButton, 2, 8, 1, 1)
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
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口工具"))
        self.label_2.setText(_translate("MainWindow", "波特率:"))
        self.RTS_CheckBox.setText(_translate("MainWindow", "RTS"))
        self.label.setText(_translate("MainWindow", "串口:"))
        self.Save_Window_Data_Button.setText(_translate("MainWindow", "保存窗口中的内容到文件"))
        self.label_4.setText(_translate("MainWindow", "发送内容:"))
        self.label_3.setText(_translate("MainWindow", "接收内容:"))
        self.label_6.setText(_translate("MainWindow", "当前使用的数据接收修饰器:"))
        self.DTR_CheckBox.setText(_translate("MainWindow", "DTR"))
        self.label_5.setText(_translate("MainWindow", "当前使用的数据发送修饰器:"))
        self.SendDatapushButton.setText(_translate("MainWindow", "发送数据"))
        self.OpenUartpushButton.setText(_translate("MainWindow", "打开串口"))
        self.Save_Rev_Data_CheckBox.setText(_translate("MainWindow", "保存接收的数据到文件"))
        self.ClearRevWinDataButton.setText(_translate("MainWindow", "清空接收内容"))
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
