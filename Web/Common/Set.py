# -*- coding:utf-8 -*-

from Pages.LoginPage import LoginPage
import logging
import sys
import Logger

#logger = logging.getLogger("Mylogger.Case")
#scr_path = "C:\\Users\\IGEN\\Desktop\\Mytest\\Web\\Img\\"
logger=Logger.logger()
scr_path = "D:\\appscreenshot\\"

def setup(self):
    self.driver = LoginPage("Chrome")
    self.driver.max_window()
    self.driver.open_url('http://pro.solarman.cn/login/login.do?lang=1')
    self.driver.guide_close()


def teardown(self):
    logger.info("TestCase:" + self._testMethodName)
    if sys.exc_info()[0]:
        print sys.exc_info()
        logger.info("Error:" + self._testMethodName)
        self.driver.get_screen_shot(scr_path + self._testMethodName + ".png")
        logger.info("Save Img to: " + scr_path + self._testMethodName + ".png")
    else:
        logger.info("Passed:" + self._testMethodName)


