import sys
import os
import importlib

global g_plugin_tab_widget
# from plugin.esp32_task_info_viewer import plugin_main
# from plugin.esp32_backtrace_viewer import plugin_main
import plugin.esp32_backtrace_viewer.plugin_main
import plugin.esp32_task_info_viewer.plugin_main

global _plugin_dir
global _plugin_name_to_module_obj_dict

# 获取插件名字
def get_name(file_path_name):
    name = None
    try:
        tmp_decorator_module = importlib.import_module(file_path_name)
        name = tmp_decorator_module.NAME
    except:
        name = None
    return name


# 遍历插件
def enumerate():
    ret = []
    global _plugin_dir

    _plugin_dir = []

    for root, dirs, files in os.walk(os.getcwd() + "\\plugin\\"):
        for name in dirs:
            print("plugin枚举目录:" + root + name)
            sys.path.append(root + name)
            _plugin_dir.append(root + name)

    for plugin_dir in _plugin_dir:
        g = os.walk(plugin_dir)
        for path, dir_list, file_list in g:
            for file_name in file_list:
                if file_name == "plugin_main.py":
                    tmp_str = plugin_dir.replace(os.getcwd(),"")+"\\"+os.path.splitext(file_name)[0]
                    tmp_str=tmp_str[1:]
                    tmp_str = tmp_str.replace("\\",".")
                    print(tmp_str)
                    name = None
                    name = get_name(tmp_str)
                    if name is not None:
                        print("已加载:" + name)
                        global _plugin_name_to_module_obj_dict
                        _plugin_name_to_module_obj_dict[name] = importlib.import_module(tmp_str)
                        ret.append(name)

    return ret



def init(tab_widget):
    global g_plugin_tab_widget
    g_plugin_tab_widget = tab_widget


    global _plugin_name_to_module_obj_dict
    _plugin_name_to_module_obj_dict={}

    # 遍历插件
    enumerate()
    # 初始化插件
    for plugin_module in _plugin_name_to_module_obj_dict.values():
        plugin_module.init(g_plugin_tab_widget)



# 串口收到数据处理函数
def uart_rev_data(bytes_data):
    ret = True
    discard = False
    out = None

    for plugin_module in _plugin_name_to_module_obj_dict.values():
        plugin_module.uart_rev_data(bytes_data)

    return ret, discard, out


# 设置全局设置对象
def set_global_setting(global_setting):
    pass
