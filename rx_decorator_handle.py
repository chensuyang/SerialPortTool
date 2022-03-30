import sys
import os

global _rx_decorator_module
global _rx_decorator_module_dir
global _rx_decorator_module_name_to_module_obj_dict
global _current_rx_decorator_module


# 初始化RX修饰器处理
def init():
    global _rx_decorator_module_dir
    _rx_decorator_module_dir = sys.path[0] + "\\rx_decorator\\"
    print("rx_decorator枚举目录:" + _rx_decorator_module_dir)
    sys.path.append(_rx_decorator_module_dir)

    global _rx_decorator_module_name_to_module_obj_dict
    _rx_decorator_module_name_to_module_obj_dict = {}

    global _current_rx_decorator_module
    _current_rx_decorator_module = None

# 获取RX修饰器名字
def get_name(file_name):
    name = None
    try:
        tmp_decorator_module = __import__(file_name)
        name = tmp_decorator_module.DECORATOR_NAME
    except:
        name = None
    return name


# 遍历RX修饰器
def enumerate():
    global _rx_decorator_module_dir
    g = os.walk(_rx_decorator_module_dir)
    ret = []
    for path, dir_list, file_list in g:
        for file_name in file_list:
            if os.path.splitext(file_name)[1]==".py":
                name = None
                name = get_name(os.path.splitext(file_name)[0])
                if name is not None:
                    _rx_decorator_module_name_to_module_obj_dict[name] = __import__(os.path.splitext(file_name)[0])
                    ret.append(name)
    return ret


# 载入RX修饰器
def load(name):
    global _current_rx_decorator_module
    _current_rx_decorator_module = _rx_decorator_module_name_to_module_obj_dict[name]

    print("当前载入的RX修饰器名称:" + _current_rx_decorator_module.DECORATOR_NAME)

    # 初始化修饰器
    _current_rx_decorator_module.init()

# 释放RX修饰器
def free():
    global _current_rx_decorator_module
    if _current_rx_decorator_module is not None:
        _current_rx_decorator_module.destroy()

# 通过载入的RX修饰器转换
def convert(bytes_data):
    if _current_rx_decorator_module is not None:
        ret_str,is_html = _current_rx_decorator_module.convert(bytes_data,False)
        return ret_str
