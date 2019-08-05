# -*- coding:utf-8 -*-

import unittest
import time
from Common import Set
from Common import HTMLRun,Logger

class Login(unittest.TestCase):

    def setUp(self):
        Set.setup(self)

    def tearDown(self):
        Set.teardown(self)

    def test_Login(self):
        self.driver.input_username('17798736289')
        self.driver.input_password('111111')
        self.driver.click_login_btn()
        time.sleep(5)
        url = self.driver.get_current_url()
        self.assertEqual(url, 'http://pro.solarman.cn/index/setIndex.do')

if __name__ == "__main__":
    unittest.main()


    #
    # def test_Login_1(self):
    #     self.driver.input_username('15006173014')
    #     self.driver.input_password('12345678')
    #     self.driver.click_login_btn()
    #     url = self.driver.get_current_url()
    #     self.assertEqual(url, 'http://192.168.1.58:18006/index/setIndex.do')
    #
    # def test_Login_2(self):
    #     self.input_username('15006173014')
    #     self.driver.input_password('12345678')
    #     self.driver.click_login_btn()
    #     url = self.driver.get_current_url()
    #     self.assertEqual(url, 'http://192.168.1.58:18006/index/setIndex.do')