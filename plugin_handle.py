import sys
import os

global g_plugin_tab_widget
#from plugin.esp32_task_info_viewer import plugin_main
#from plugin.esp32_backtrace_viewer import plugin_main
import plugin.esp32_backtrace_viewer.plugin_main
import plugin.esp32_task_info_viewer.plugin_main


def init(tab_widget):
    global g_plugin_tab_widget
    g_plugin_tab_widget = tab_widget

    plugin.esp32_task_info_viewer.plugin_main.init(g_plugin_tab_widget)
    plugin.esp32_backtrace_viewer.plugin_main.init(g_plugin_tab_widget)

# 串口收到数据处理函数
def uart_rev_data(bytes_data):
    return plugin.esp32_task_info_viewer.plugin_main.uart_rev_data(bytes_data)


# 设置全局设置对象
def set_global_setting(global_setting):
    pass
