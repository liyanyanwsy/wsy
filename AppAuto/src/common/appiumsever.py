#encoding:utf-8
import os
import subprocess
import time
from config import IniHelper


class AppiumServer(object):
    '''启动、关闭appium server'''
    def __init__(self):
        global cmd_start_appium,base_url
        cmd_start_appium= IniHelper.IniHelper('cfginfo.ini').get_value('appium', 'start_appium')
        base_url= IniHelper.IniHelper('cfginfo.ini').get_value('appium', 'base_url')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
    def start_server(self):
        '''启动appium'''
        appium_log_path=log_dir+'appium.log'
        subprocess.call(cmd_start_appium,shell=True,stdout=(open(appium_log_path,'w'),stderr=subprocess.ST)

        time.sleep(4)









