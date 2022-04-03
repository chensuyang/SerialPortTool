import serial
import serial.tools.list_ports
import pprint

global current_opened_uart


def get_current_uart_info_list():
    return list(serial.tools.list_ports.comports())


def uart_info_get_uart_com(uart_info):
    return uart_info.device


def uart_info_get_uart_name(uart_info):
    return uart_info.description


def open_uart(uart_info, baud_rate=9600, timeout=0.5):
    global current_opened_uart
    current_opened_uart = serial.Serial(uart_info_get_uart_com(uart_info), baud_rate, timeout=0.01)
    return current_opened_uart


def close_uart():
    global current_opened_uart
    if current_opened_uart != None:
        current_opened_uart.close()
        current_opened_uart = None
        return True
    return False


def set_rts_state(state):
    global current_opened_uart
    current_opened_uart.setRTS(state)


def set_dtr_state(state):
    global current_opened_uart
    current_opened_uart.setDTR(state)


def read():
    global current_opened_uart
    try:
        read_data = current_opened_uart.read(1024)
        return read_data,True
    except:
        return None,False
