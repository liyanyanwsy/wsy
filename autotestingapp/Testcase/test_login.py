# encoding:utf-8
import os, time, unittest
import sys
from appium import webdriver
from Functions import run
class mytest(unittest.TestCase):
    def setUp(self):
        run.setup(self)
    def test_login(self):
        #点击登录按钮
        self.driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()
        self.driver.find_element_by_id("com.igen.solarmanpro:id/etName").send_keys("17798736289")
        self.driver.find_element_by_id("com.igen.solarmanpro:id/etPsw").send_keys("123456")
        self.driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()
        time.sleep(3)
    def screenshot(self):
        run.screenshot()




    def teardown(self):
        run.tearDown(self)
if __name__ == "__main__":
    unittest.main()