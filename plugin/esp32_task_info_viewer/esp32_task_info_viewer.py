# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'esp32_backtrace_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(316, 595)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.free_internal_memory_label = QtWidgets.QLabel(Form)
        self.free_internal_memory_label.setObjectName("free_internal_memory_label")
        self.verticalLayout.addWidget(self.free_internal_memory_label)
        self.free_internal_memory_pushButton = QtWidgets.QPushButton(Form)
        self.free_internal_memory_pushButton.setObjectName("free_internal_memory_pushButton")
        self.verticalLayout.addWidget(self.free_internal_memory_pushButton)
        self.free_external_memory_label = QtWidgets.QLabel(Form)
        self.free_external_memory_label.setObjectName("free_external_memory_label")
        self.verticalLayout.addWidget(self.free_external_memory_label)
        self.free_external_memory_pushButton = QtWidgets.QPushButton(Form)
        self.free_external_memory_pushButton.setObjectName("free_external_memory_pushButton")
        self.verticalLayout.addWidget(self.free_external_memory_pushButton)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.TaskInfotableWidget = QtWidgets.QTableWidget(Form)
        self.TaskInfotableWidget.setObjectName("TaskInfotableWidget")
        self.TaskInfotableWidget.setColumnCount(5)
        self.TaskInfotableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TaskInfotableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TaskInfotableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TaskInfotableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TaskInfotableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TaskInfotableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.TaskInfotableWidget)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.free_internal_memory_label.setText(_translate("Form", "????????????(??????):"))
        self.free_internal_memory_pushButton.setText(_translate("Form", "??????????????????"))
        self.free_external_memory_label.setText(_translate("Form", "????????????(??????):"))
        self.free_external_memory_pushButton.setText(_translate("Form", "??????????????????"))
        self.label_3.setText(_translate("Form", "Task??????:"))
        item = self.TaskInfotableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "??????"))
        item = self.TaskInfotableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "CPU?????????"))
        item = self.TaskInfotableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "?????????????????????"))
        item = self.TaskInfotableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "??????"))
        item = self.TaskInfotableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "?????????"))
        self.pushButton.setText(_translate("Form", "???????????????????????????ESP32??????"))
