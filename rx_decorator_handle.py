import sys
import os

global _rx_decorator_module
global _rx_decorator_module_dir
global _rx_decorator_module_name_to_module_obj_dict
global _current_rx_decorator_module


# 初始化RX修饰器处理
def init():
    global _rx_decorator_module_dir
    _rx_decorator_module_dir = os.getcwd() + "\\rx_decorator\\"
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

def rgb_to_html_color(rgb_tuple):
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    return hexcolor

def string_to_html_filter(str_data):
   #注意这几行代码的顺序不能乱，否则会造成多次替换
   str_data = str_data.replace("&","&amp;")
   str_data = str_data.replace(">","&gt;")
   str_data = str_data.replace("<","&lt;")
   str_data = str_data.replace("\"","&quot;")
   str_data = str_data.replace("\'","&#39;")
   str_data = str_data.replace(" ","&nbsp;")
   str_data = str_data.replace("\n","<br>")
   str_data = str_data.replace("\r","<br>")
   return str_data

def stringToHtml(str_data,color):
    return "<span style=\" color:" + rgb_to_html_color(color) + ";\">" + str_data + "</span>"


# 通过载入的RX修饰器转换
def convert(bytes_data):
    output_flag = True
    if _current_rx_decorator_module is not None:
        ret_str, is_html = _current_rx_decorator_module.convert(bytes_data, False)
        if len(ret_str) == 0:
            output_flag = False
        if is_html:
            return ret_str, output_flag
        else:
            return stringToHtml(string_to_html_filter(ret_str),(85, 85, 85)),output_flag
