from PyQt5 import QtCore, QtWidgets
import main_window
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QDesktopWidget
import uart_handle
from PyQt5.QtCore import QTimer
import rx_decorator_handle
import tx_decorator_handle
import time
from setting import setting
import os
import pprint
import plugin_handle
from set_rev_data_text_edit_max_block_count_window import set_rev_data_text_edit_max_block_count_window_work
import qtmodern.styles
import qtmodern.windows


# 当前PC中所有被枚举出的串口信息列表
global g_current_uart_info_list
g_current_uart_info_list = None
# 当前软件已经打开的串口信息
global g_current_opened_uart_info
g_current_opened_uart_info = None

global set_rev_data_text_edit_max_block_count_window

class UpdateThread(QThread):
    # 实时显示追加线程（要继承QThread， 继承threading.Thread不行）
    rev_data_text_edit_append_text_signal = pyqtSignal(str)  # 接收数据文本浏览器添加文本信号
    uart_read_fail_signal = pyqtSignal()  # 串口读取失败信号

    def run(self):
        while True:
            global g_current_opened_uart_info
            # 如果当前有打开的串口
            if g_current_opened_uart_info is not None:

                read_data, state = uart_handle.read()
                if state:
                    # 调用插件
                    ret, discard, out = plugin_handle.uart_rev_data(read_data)

                    # 如果插件处理完成
                    if ret:
                        # 如果当前插件不丢弃数据,则调用RX修饰器来输出数据
                        if not discard:
                            # 调用RX修饰器来转换串口的数据
                            append_str, output_flag = rx_decorator_handle.convert(read_data)
                            # 如果有有效数据,则更新到界面
                            if append_str is not None and len(append_str) and output_flag:
                                self.rev_data_text_edit_append_text_signal.emit(append_str)  # 发射信号(实参类型要和定义信号的参数类型一致)

                        # 判断插件是否需要输出数据
                        if out is not None:
                            self.rev_data_text_edit_append_text_signal.emit(str(out))  # 发射信号(实参类型要和定义信号的参数类型一致
                else:
                    self.uart_read_fail_signal.emit()  # 发射信号
            time.sleep(0.05)


class MainWindowWork(QtWidgets.QMainWindow):
    close_signal = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        global g_current_opened_uart_info
        g_current_opened_uart_info = None
        # 初始化设置
        setting.init()

        self.ui.set_rev_data_text_edit_max_block_count.triggered.connect(self.slot_set_rev_data_text_edit_max_block_count)

        # 设置显示接收数据的textEdit为只读
        self.ui.RevDataTextEdit.setReadOnly(True)

        # 更新全局的当前串口信息列表,并根据列表刷新界面上的串口选择列表
        global g_current_uart_info_list
        g_current_uart_info_list = uart_handle.get_current_uart_info_list()
        self.init_uart_list_combo_box(g_current_uart_info_list)

        # 更新串口波特率选择列表
        self.init_baud_rate_combo_box(setting.get_uart_baud_rate_list())

        # 选中当前设置的波特率
        i = 0
        setting_baud_rate = setting.get_uart_baud_rate()
        for baud_rate in setting.get_uart_baud_rate_list():
            if baud_rate == setting_baud_rate:
                self.ui.BaudRate_comboBox.setCurrentIndex(i)
            i = i + 1

        # 初始化RX的修饰器处理
        rx_decorator_handle.init()

        # 遍历所有RX修饰器
        rx_decorator_list = rx_decorator_handle.enumerate()

        # 更新选择框中的RX修饰器列表
        self.ui.UartRxPlugin_comboBox.clear()
        i = 0
        # 遍历所有的修饰器名字
        for rx_decorator in rx_decorator_list:
            # 添加到选择框中
            self.ui.UartRxPlugin_comboBox.addItem(rx_decorator)

            # 如果出现与设置文件相同名字的修饰器,则默认选中
            if setting.get_rx_decorator_name() == rx_decorator:
                self.ui.UartRxPlugin_comboBox.setCurrentIndex(i)
            i = i + 1

        # 初始化插件处理
        plugin_handle.init(self.ui.tabWidget)

        # 根据存储的配置设置RTS DTR选择框
        self.ui.RTS_CheckBox.setChecked(setting.get_rts())
        self.ui.DTR_CheckBox.setChecked(setting.get_dtr())

        # UI事件绑定
        self.ui.Save_Window_Data_Button.clicked.connect(self.save_win_data_button_callback)
        self.ui.Save_Rev_Data_CheckBox.stateChanged.connect(self.save_rev_data_check_box_changed_callback)
        self.ui.OpenUartpushButton.clicked.connect(self.open_uart_button_callback)
        self.ui.RTS_CheckBox.stateChanged.connect(self.rts_check_box_changed_callback)
        self.ui.DTR_CheckBox.stateChanged.connect(self.dtr_check_box_changed_callback)
        self.ui.BaudRate_comboBox.currentIndexChanged.connect(self.baud_rate_combo_box_current_index_changed_callback)
        self.ui.UartRxPlugin_comboBox.currentIndexChanged.connect(
            self.rx_plugin_combo_box_current_index_changed_callback)

        self.ui.ClearRevWinDataButton.clicked.connect(self.clear_rev_win_data_callback)
        # 初始化定时器
        self.uart_list_combo_box_refresh_timer = QTimer()
        # 计时结束调⽤uart_list_combo_box_refresh_timer_callback()⽅法
        self.uart_list_combo_box_refresh_timer.timeout.connect(self.uart_list_combo_box_refresh_timer_callback)
        # 设置计时间隔并启动(0.5S)
        self.uart_list_combo_box_refresh_timer.setSingleShot(False)
        self.uart_list_combo_box_refresh_timer.start(500)

        # 5.实时追加文本(采用多线程方式追加，不然界面会卡死)
        self.update_thread = UpdateThread()
        self.update_thread.rev_data_text_edit_append_text_signal.connect(
            self.slot_rev_data_text_edit_append_str)  # 连接槽函数
        self.update_thread.uart_read_fail_signal.connect(self.slot_auto_close_uart)  # 连接槽函数
        self.update_thread.start()

    def slot_set_rev_data_text_edit_max_block_count(self):
        global set_rev_data_text_edit_max_block_count_window
        set_rev_data_text_edit_max_block_count_window = set_rev_data_text_edit_max_block_count_window_work.SetRevDataTextEditMaxBlockCountWindowWork()
        window = qtmodern.windows.ModernWindow(set_rev_data_text_edit_max_block_count_window)

        # 获取窗口大小
        screen = QDesktopWidget().screenGeometry()
        size = window.geometry()

        # 窗体运动
        window.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        window.show()
        set_rev_data_text_edit_max_block_count_window.ui.pushButton.clicked.connect(self.slot_update_rev_data_text_edit_max_block_count)

        # 往窗口中添加可选择的块数量列表
        block_count_list = [100,1000,2000,5000,10000]
        for block_count in block_count_list:
            set_rev_data_text_edit_max_block_count_window.add_block_count(str(block_count))


    def slot_update_rev_data_text_edit_max_block_count(self):
        global set_rev_data_text_edit_max_block_count_window
        if set_rev_data_text_edit_max_block_count_window is not None:
            setting.set_rev_data_text_edit_max_block_count(int(set_rev_data_text_edit_max_block_count_window.ui.comboBox.currentText()))
            set_rev_data_text_edit_max_block_count_window.close()

            # 设置显示接收数据的textEdit最大显示行数
            self.ui.RevDataTextEdit.document().setMaximumBlockCount(setting.get_rev_data_text_edit_max_block_count())
            print("update_rev_data_text_edit_max_block_count:"+str(setting.get_rev_data_text_edit_max_block_count()))


    def slot_rev_data_text_edit_append_str(self, text):
        self.ui.RevDataTextEdit.moveCursor(self.ui.RevDataTextEdit.textCursor().End)
        self.ui.RevDataTextEdit.insertHtml(text)

    def slot_auto_close_uart(self):
        # 自动关闭串口
        try:
            # 释放RX修饰器
            rx_decorator_handle.free()

            # 关闭串口
            uart_handle.close_uart()
        except:
            pass

        # 清空全局串口信息
        global g_current_opened_uart_info
        g_current_opened_uart_info = None
        self.ui.OpenUartpushButton.setText("打开串口")
        self.statusBar().showMessage("因串口故障而自动关闭串口")

    def save_win_data_button_callback(self):
        file_path = os.getcwd() + "\\" + str(
            time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())) + "_rev_window_data_save.txt"
        QMessageBox.information(self, "记录到文件", "接收窗口中的数据将记录到" + file_path + "文件中", QMessageBox.Yes)
        try:
            file = open(file_path, "w")
            file.write(self.ui.RevDataTextEdit.toPlainText())
            file.close()
        except:
            QMessageBox.warning(self, "记录到文件", "保存文件失败", QMessageBox.Yes)

    def save_rev_data_check_box_changed_callback(self):
        if self.ui.Save_Rev_Data_CheckBox.isChecked():
            file_path = os.getcwd() + "\\rev_data_save.txt"
            QMessageBox.information(self, "记录到文件", "接收的串口数据将记录到" + file_path + "文件中", QMessageBox.Yes)
        else:
            pass

    def clear_rev_win_data_callback(self):
        self.ui.RevDataTextEdit.clear()

    def rx_plugin_combo_box_current_index_changed_callback(self):
        setting.set_rx_decorator_name(self.ui.UartRxPlugin_comboBox.currentText())

    def baud_rate_combo_box_current_index_changed_callback(self):
        setting.set_uart_baud_rate(int(self.ui.BaudRate_comboBox.currentText()))

    def rts_check_box_changed_callback(self):
        global g_current_opened_uart_info
        if g_current_opened_uart_info is not None:
            setting.set_rts(self.ui.RTS_CheckBox.isChecked())
            if self.ui.RTS_CheckBox.isChecked():
                uart_handle.set_rts_state(False)
            else:
                uart_handle.set_rts_state(True)

    def dtr_check_box_changed_callback(self):
        global g_current_opened_uart_info
        if g_current_opened_uart_info is not None:
            setting.set_dtr(self.ui.DTR_CheckBox.isChecked())
            if self.ui.DTR_CheckBox.isChecked():
                uart_handle.set_dtr_state(False)
            else:
                uart_handle.set_dtr_state(True)

    def uart_list_combo_box_refresh_timer_callback(self):
        global g_current_opened_uart_info
        global g_current_uart_info_list
        # 如果当前没有打开串口
        if g_current_opened_uart_info is None:
            # 如果当前串口列表发生变化
            if g_current_uart_info_list != uart_handle.get_current_uart_info_list():
                # 更新列表框内容
                g_current_uart_info_list = uart_handle.get_current_uart_info_list()
                self.init_uart_list_combo_box(g_current_uart_info_list)

    def init_baud_rate_combo_box(self, baud_rate_list):
        self.ui.BaudRate_comboBox.clear()
        for baud_rate in baud_rate_list:
            self.ui.BaudRate_comboBox.addItem(str(baud_rate))

    def init_uart_list_combo_box(self, uart_info_list):
        self.ui.UartNumber_comboBox.clear()
        for uar_info in uart_info_list:
            self.ui.UartNumber_comboBox.addItem(uart_handle.uart_info_get_uart_name(uar_info))

    def open_uart_button_callback(self):
        global g_current_opened_uart_info
        if g_current_opened_uart_info is None:
            try:
                # 打开串口
                uart_handle.open_uart(g_current_uart_info_list[self.ui.UartNumber_comboBox.currentIndex()],
                                      baud_rate=int(self.ui.BaudRate_comboBox.currentText()))
                # 给全局对象赋值
                g_current_opened_uart_info = g_current_uart_info_list[self.ui.UartNumber_comboBox.currentIndex()]
                self.ui.OpenUartpushButton.setText("关闭串口")
                # 载入RX修饰器
                rx_decorator_handle.load(self.ui.UartRxPlugin_comboBox.currentText())

                # 打开串口的时候调用一下rts与dtr的回调,以生效rts与dtr电平
                self.rts_check_box_changed_callback()
                self.dtr_check_box_changed_callback()
                self.statusBar().showMessage("串口已打开")

            except:
                self.ui.OpenUartpushButton.setText("打开串口")
                QMessageBox.warning(self, "串口操作", "打开串口失败", QMessageBox.Yes)
                self.statusBar().showMessage("串口打开失败")
        else:
            current_opened_uart_info_bak = g_current_opened_uart_info
            try:
                g_current_opened_uart_info = None
                time.sleep(0.1)
                uart_handle.close_uart()
                # 释放RX修饰器
                rx_decorator_handle.free()
                self.ui.OpenUartpushButton.setText("打开串口")
                self.statusBar().showMessage("串口已关闭")
            except:
                g_current_opened_uart_info = current_opened_uart_info_bak
                self.ui.OpenUartpushButton.setText("关闭串口")
                QMessageBox.warning(self, "串口操作", "关闭串口失败", QMessageBox.Yes)
                self.statusBar().showMessage("串口关闭失败")

    def closeEvent(self, e):
        global g_current_opened_uart_info
        if g_current_opened_uart_info is not None:
            g_current_opened_uart_info = None
            time.sleep(0.1)
            uart_handle.close_uart()
            # 释放RX修饰器
            rx_decorator_handle.free()
        e.accept()
        QtWidgets.QWidget.closeEvent(self, e)
