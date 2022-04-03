import sys
import re

global str_buf
global bytes_data_idle_time_cnt

# 修饰器名字(必须存在),会显示在软件界面的下拉列表里
DECORATOR_NAME = "增强修饰器-转换到gb2312编码的文本(支持ANSI着色)"


# 修饰器开始工作时调用

def init():
    global bytes_data_idle_time_cnt
    bytes_data_idle_time_cnt = 0
    global str_buf
    str_buf = bytes()
    print("修饰器初始化")


def destroy():
    print("修饰器反初始化")


def rgb_to_html_color(rgb_tuple):
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    return hexcolor


def string_to_html_filter(str_data):
    # 注意这几行代码的顺序不能乱，否则会造成多次替换
    str_data = str_data.replace("&", "&amp;")
    str_data = str_data.replace(">", "&gt;")
    str_data = str_data.replace("<", "&lt;")
    str_data = str_data.replace("\"", "&quot;")
    str_data = str_data.replace("\'", "&#39;")
    str_data = str_data.replace(" ", "&nbsp;")
    str_data = str_data.replace("\r\n", "<br>")
    str_data = str_data.replace("\n", "<br>")
    str_data = str_data.replace("\r", "<br>")
    return str_data


def stringToHtml(str_data, color):
    return "<span style=\" color:" + rgb_to_html_color(color) + ";\">" + str_data + "</span>"


RE_ANSI_COLOR = re.compile(b'\033\\[([01]);3([0-7])m')
ANSI_COLOR_END = re.compile(b'\033\[0m')


def ansi_color_str_convert(ansi_color_bytes):
    m = re.match(RE_ANSI_COLOR, ansi_color_bytes)
    rgb_color = (85, 85, 85)
    if m is not None:
        color = int(m.group(2))
        if color == 0:
            rgb_color = (0, 0, 0)
        if color == 1:
            rgb_color = (170, 0, 0)
        if color == 2:
            rgb_color = (0, 170, 0)
        if color == 3:
            rgb_color = (170, 85, 0)
        if color == 4:
            rgb_color = (0, 0, 170)
        if color == 5:
            rgb_color = (170, 0, 170)
        if color == 6:
            rgb_color = (0, 170, 170)
        if color == 7:
            rgb_color = (170, 170, 170)
        # 删除ANSI color部分
        ansi_bytes = ansi_color_bytes[m.start():m.end()]
        ansi_color_bytes = ansi_color_bytes.replace(ansi_bytes, b"")

        m_end = re.search(ANSI_COLOR_END, ansi_color_bytes)
        if m_end is not None:
            ansi_bytes = ansi_color_bytes[m_end.start():m_end.end()]
            ansi_color_bytes = ansi_color_bytes.replace(ansi_bytes, b"")

        # 转为字符串
        out_str = str(ansi_color_bytes, encoding='gb2312', errors='ignore')
        return out_str, rgb_color
    else:
        return str(ansi_color_bytes, encoding='gb2312', errors='ignore'), (85, 85, 85)


# 转换串口接收的数据
# 输入1:bytes_data  为串口收到的数据
# 输入2:bool        本修饰器后方是否还有级联的修饰器
# 输出1:str         转换后的字符串数据
# 输出2:bool        是否支持html格式

def convert(bytes_data, series):
    global bytes_data_idle_time_cnt
    global str_buf

    # 判断是否有持续的数据输入
    if len(bytes_data):
        bytes_data_idle_time_cnt = 0
    else:
        if bytes_data_idle_time_cnt < 100:
            bytes_data_idle_time_cnt = bytes_data_idle_time_cnt + 1

    if series:
        return bytes_data,False
    else:
        if len(bytes_data):
            str_buf = str_buf + bytes_data

        out_data = ""
        fund_flag = False
        while True:
            # 用换行符分割数据
            partition_str = str_buf.split(b"\r\n", 1)

            # 如果有找到有效的文本行
            if len(partition_str) > 1:
                # 开始转换
                converted_str, color = ansi_color_str_convert(partition_str[0]+b"\r\n")

                # 如果有有效的转换结果
                if converted_str is not None and len(converted_str):
                    # 将剩余的文本放回str_buf
                    str_buf = partition_str[1]
                    out_data = out_data + stringToHtml(string_to_html_filter(converted_str), color)
                    fund_flag = True
            else:
                break
        if fund_flag:
            return out_data,True
        # 如果没有找到有效的文本行,且已经有50次没有输出,则强制输出
        if bytes_data_idle_time_cnt > 50 and len(str_buf):
            print("超时打印")
            color = (85, 85, 85)
            out = str(str_buf, encoding='gb2312', errors='ignore')
            # 清空缓冲区
            str_buf = ""
            return stringToHtml(string_to_html_filter(out), color), True
    return "", True
