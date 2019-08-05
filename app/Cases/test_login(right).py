# encoding:utf-8
import time, unittest
from appium import webdriver
from Common import Set
class login(unittest.TestCase):
    def setUp(self):
        Set.setup(self)
    def test_login(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.igen.solarmanpro:id/btnLogin"]').click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.igen.solarmanpro:id/etName']").send_keys("17798736289")
        self.driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/etPsw']").send_keys("111111")
        self.driver.hide_keyboard()
        self.driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/btnLogin']").click()
if __name__ == "__main__":
    unittest.main()
