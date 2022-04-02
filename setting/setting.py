import sys
import os

from configobj import ConfigObj

global config


def init():
    global config
    setting_file = os.getcwd() + "\\setting.ini"
    config = ConfigObj(setting_file, encoding='UTF8')


def get_uart_baud_rate_list():
    return [2400, 4800, 9600, 57600, 115200, 230400]


def get_uart_baud_rate():
    global config
    try:
        baud_rate = config['uart']['baud_rate']
        return int(baud_rate)
    except:
        return 115200


def set_uart_baud_rate(baud_rate):
    global config
    config['uart']['baud_rate'] = baud_rate
    config.write()


def get_rts():
    global config
    try:
        rts = config['uart']['rts']
        if rts == "true":
            return True
        else:
            return False
    except:
        return False


def set_rts(rts):
    global config
    if rts:
        config['uart']['rts'] = "true"
    else:
        config['uart']['rts'] = "false"
    config.write()

def get_dtr():
    global config
    try:
        dtr = config['uart']['dtr']
        if dtr == "true":
            return True
        else:
            return False
    except:
        return False


def set_dtr(dtr):
    global config
    if dtr:
        config['uart']['dtr'] = "true"
    else:
        config['uart']['dtr'] = "false"
    config.write()
