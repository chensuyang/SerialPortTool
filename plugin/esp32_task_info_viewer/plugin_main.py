from plugin.esp32_task_info_viewer import esp32_task_info_viewer
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np
import time
import re
import pprint

global esp32_task_info_viewer_pattern
global uart_rev_str_buf
global free_internal_heap_size
global free_spi_ram_heap_size
global task_name
global task_current_state
global task_current_priority
global task_stack_high_water_mark
global task_cpu_time_percentage
global plugin_window

global record_start_timestamp
global free_internal_memory_history_data
global free_memory_history_timestamp
global free_external_memory_history_data

# 插件名字(必须存在),会显示在软件界面
NAME = "ESP32任务信息显示器"


class PluginWindowWork(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = esp32_task_info_viewer.Ui_Form()
        self.ui.setupUi(self)

        self.ui.free_external_memory_pushButton.clicked.connect(self.show_free_external_memory_history_data)
        self.ui.free_internal_memory_pushButton.clicked.connect(self.show_free_internal_memory_history_data)

    def show_free_external_memory_history_data(self):
        pprint.pprint(free_memory_history_timestamp)
        pprint.pprint(free_external_memory_history_data)
        plt.figure(figsize=(8, 6))  # 定义图的大小
        plt.xlabel("time(s)")  # X轴标签
        plt.ylabel("byte")  # Y轴坐标标签
        plt.title("剩余内存(外部)历史曲线",fontproperties='SimHei')  # 曲线图的标题
        plt.plot(free_memory_history_timestamp, free_external_memory_history_data)  # 绘制曲线图
        plt.ticklabel_format(style='plain')
        plt.show()

    def show_free_internal_memory_history_data(self):
        pprint.pprint(free_memory_history_timestamp)
        pprint.pprint(free_internal_memory_history_data)
        plt.figure(figsize=(8, 6))  # 定义图的大小
        plt.xlabel("time(s)")  # X轴标签
        plt.ylabel("byte")  # Y轴坐标标签
        plt.title("剩余内存(外部)历史曲线",fontproperties='SimHei')  # 曲线图的标题
        plt.plot(free_memory_history_timestamp, free_internal_memory_history_data)  # 绘制曲线图
        plt.ticklabel_format(style='plain')
        plt.show()

    def refresh_task_info(self):
        global free_internal_heap_size
        global free_spi_ram_heap_size
        self.ui.free_internal_memory_label.setText("剩余内存(内部):" + str(round(free_internal_heap_size / 1024, 4)) + "KB")
        self.ui.free_external_memory_label.setText("剩余内存(外部):" + str(round(free_spi_ram_heap_size / 1024, 4)) + "KB")
        # self.ui.TaskInfotableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        global task_name
        global task_current_state
        global task_current_priority
        global task_stack_high_water_mark
        global task_cpu_time_percentage

        self.ui.TaskInfotableWidget.clearContents()
        self.ui.TaskInfotableWidget.setRowCount(len(task_name))
        self.ui.TaskInfotableWidget.setColumnCount(5)
        for i in range(len(task_name)):
            # 添加数据
            newItem = QTableWidgetItem(task_name[i])
            self.ui.TaskInfotableWidget.setItem(i, 0, newItem)

            newItem = QTableWidgetItem(str(task_cpu_time_percentage[i]))
            self.ui.TaskInfotableWidget.setItem(i, 1, newItem)

            newItem = QTableWidgetItem(str(task_stack_high_water_mark[i]))
            self.ui.TaskInfotableWidget.setItem(i, 2, newItem)

            if int(task_current_state[i]) == 0:
                newItem = QTableWidgetItem("运行中")
            elif int(task_current_state[i]) == 1:
                newItem = QTableWidgetItem("已就绪")
            elif int(task_current_state[i]) == 2:
                newItem = QTableWidgetItem("阻塞中")
            elif int(task_current_state[i]) == 3:
                newItem = QTableWidgetItem("暂停中")
            elif int(task_current_state[i]) == 4:
                newItem = QTableWidgetItem("删除中")
            else:
                newItem = QTableWidgetItem("未知状态:" + str(task_current_state[i]))
            self.ui.TaskInfotableWidget.setItem(i, 3, newItem)

            newItem = QTableWidgetItem(str(task_current_priority[i]))
            self.ui.TaskInfotableWidget.setItem(i, 4, newItem)


def init(tab_widget):
    global plugin_window
    plugin_window = PluginWindowWork()

    tab_widget.addTab(plugin_window, "ESP32任务信息显示器")
    # tab_widget.setCurrentWidget(plugin_window)

    global esp32_task_info_viewer_pattern
    esp32_task_info_viewer_pattern = re.compile("esp32_task_info_viewer_s,[0-9]+,[0-9]+.+,esp32_task_info_viewer_e")

    global uart_rev_str_buf
    uart_rev_str_buf = ""

    global task_name
    global task_current_state
    global task_current_priority
    global task_stack_high_water_mark
    global task_cpu_time_percentage
    global free_internal_memory_history_data
    global free_memory_history_timestamp
    global free_external_memory_history_data
    global record_start_timestamp
    task_name = []
    task_current_state = []
    task_current_priority = []
    task_stack_high_water_mark = []
    task_cpu_time_percentage = []
    free_internal_memory_history_data = []
    free_memory_history_timestamp = []
    free_external_memory_history_data = []
    record_start_timestamp = 0


def uart_rev_data(bytes_data):
    ret = True
    discard = False
    out = None
    global uart_rev_str_buf
    # 如果当前buf长度已经过长
    if len(uart_rev_str_buf) > 4096:
        uart_rev_str_buf = uart_rev_str_buf[2048:]
    if len(bytes_data):
        uart_rev_str_buf = uart_rev_str_buf + str(bytes_data, encoding='gb2312', errors='ignore')
    global esp32_task_info_viewer_pattern
    m = esp32_task_info_viewer_pattern.search(uart_rev_str_buf)
    if m is not None:
        esp32_task_info_viewer_str = m.group()
        str_split = esp32_task_info_viewer_str.split(",")

        global free_internal_heap_size
        global free_spi_ram_heap_size
        global task_name
        global task_current_state
        global task_current_priority
        global task_stack_high_water_mark
        global task_cpu_time_percentage
        free_internal_heap_size = int(str_split[1])
        free_spi_ram_heap_size = int(str_split[2])

        global free_internal_memory_history_data
        global free_memory_history_timestamp
        global free_external_memory_history_data
        global record_start_timestamp

        # 如果还没有开始时间戳,则记录当前时间为开始时间戳
        if record_start_timestamp == 0:
            record_start_timestamp = time.time()

        # 记录历史数据
        free_memory_history_timestamp.append(time.time() - record_start_timestamp)
        free_internal_memory_history_data.append(free_internal_heap_size)
        free_external_memory_history_data.append(free_spi_ram_heap_size)

        task_name.clear()
        task_current_state.clear()
        task_current_priority.clear()
        task_stack_high_water_mark.clear()

        for i in range(int((len(str_split) - 4) / 5)):
            task_name.insert(i, str_split[3 + i * 5])
            task_current_state.insert(i, str_split[3 + i * 5 + 1])
            task_current_priority.insert(i, str_split[3 + i * 5 + 2])
            task_stack_high_water_mark.insert(i, str_split[3 + i * 5 + 3])
            task_cpu_time_percentage.insert(i, str_split[3 + i * 5 + 4])
        plugin_window.refresh_task_info()

        uart_rev_str_buf = ""
    else:
        # print("未找到数据:"+uart_rev_str_buf)
        pass

    return ret, discard, out
