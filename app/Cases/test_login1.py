# encoding:utf-8
import os, time, unittest
import sys
from appium import webdriver
from Common import Set, screen

class login(unittest.TestCase):
    def setUp(self):
        #Common.Logger.log.info("step: Setup")
        Set.setup(self)
    def tearDown(self):           # error d to D
        #Common.Logger.log.info("step: Tear down")
        Set.teardown(self)
    def test_login(self):
        #print("step:case")
        # #Common.Logger.log.info("step: Test case")
        # # 点击登录按钮
        # # self.driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.igen.solarmanpro:id/btnLogin"]').click()

        # self.driver.find_element_by_id("com.igen.solarmanpro:id/etName").send_keys("17798736289")
        self.driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/etName']").send_keys("17798736289")

        # #self.driver.find_element_by_id("com.igen.solarmanpro:id/etPsw").send_keys("111111")
        self.driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/etPsw']").send_keys("111112")
        self.driver.hide_keyboard()
        # self.driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/btnLogin']").click()
        # toast.find_toast(self,u'用户名密码错误')
        # #toast.find_toast(self,'Wrong Username Password')
        # if (toast.find_toast(self,u'用户名密码错误')==True):
        # #if (toast.find_toast(self,'Wrong U'sername Password')==True):
        #
        #     print '正确'
        # else:
        #      print '错误'

        time.sleep(3)
        screen.screenshot()
if __name__ == "__main__":
    # Common.Logger.log.info("testcase")
    unittest.main()
