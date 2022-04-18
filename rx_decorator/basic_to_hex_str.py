import sys

# 修饰器名字(必须存在),会显示在软件界面的下拉列表里
NAME = "基本修饰器-转换到hex形式的文本"


# 修饰器开始工作时调用

def init():
    print("修饰器初始化")

def destroy():
    print("修饰器反初始化")





# 转换串口接收的数据
# 输入1:bytes_data  为串口收到的数据
# 输入2:bool        本修饰器后方是否还有级联的修饰器
# 输出1:str         转换后的字符串数据
# 输出2:bool        是否支持html格式

def convert(bytes_data, series):
    if series:
        return bytes_data
    else:
        return (''.join(['%02X ' % b for b in bytes_data])), False
