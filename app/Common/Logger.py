# -*- coding:utf-8 -*-
import time
import logging
import os
from appium import webdriver
scr_path = "D:\\appscreenshot\\"
path_log = "D:\\Program Files\\Git\\11\\app\\Report"
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
def logger():
    myloggername = os.path.join(path_log, '%s.log' % now)
    # 创建一个logger
    logger = logging.getLogger('Mylogger')
    logger.setLevel(logging.INFO)
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(myloggername)
    fh.setLevel(logging.DEBUG)
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # 定义handler的输出格式
    formatter = logging.Formatter(
        '[%(asctime)s][%(name)s][%(levelname)s] ## %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
log=logger()

