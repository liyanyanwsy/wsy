# -*- coding:utf-8 -*-
import unittest
import time
from appium import webdriver
from Common import Set
from Pages.LoginPage import LoginPage
class Login(unittest.TestCase):
    def setUp(self):
        Set.setup(self)
    def test_Login(self):
        LoginPage.click_login_btn()
        LoginPage.input_username('17798736289')
        LoginPage.input_password('987901')
        LoginPage.click_login_btn1()
        # self.driver.click_login_btn0()
        # self.driver.input_username('17798736289')
        # self.driver.input_password('987901')
        # self.driver.click_login_btn()
    def tearDown(self):
        Set.teardown(self)
if __name__ == "__main__":
    unittest.main()
