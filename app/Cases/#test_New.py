# encoding:utf-8

import os, time, unittest
import sys
from Common import Set, screen
from appium import webdriver
class New(unittest.TestCase):
    def setUp(self):
        Set.Login(self)
    def test_new(self):
        #self.driver.find_element_by_id("com.igen.solarmanpro:id/ibtn1").click()
        #self.driver.find_element_by_xpath('//*[@resource-id="com.igen.solarmanpro:id/ibtn1"]').click()
        self.driver.find_element_by_xpath("//*[@text='搜索']").click()
        # self.driver.find_element_by_xpath("//*[@text='请输入搜索关键词']").sendkeys('1')
        #self.driver.find_element_by_xpath("//*[@text='添加']").click()
        # xpath=("//*[@resource-id='com.igen.solarmanpro:id/tv']")[2]
        # self.driver.find_element_by_xpath(xpatuh).click()
        # self.driver.find_element_by_xpath(("//*[@resource-id='com.igen.solarmanpro:id/tv']")[2]).click()
        # xpath="//android.widget.TextView[@text='添加']/preceding-sibling::android.widget.ImageView"
        # self.driver.find_element_by_xpath(xpath).click()
        #self.driver.find_element_by_xpath(u"//android.widget.TextView[@text='添加']/preceding-sibling::android.widget.ImageView").click()

if __name__ == "__main__":
    # Common.Logger.log.info("testcase")
    unittest.main()


# //android.widget.TextView[@text=”钱包”]/parent::android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.ImageButton
# //android.widget.TextView[@text="添加"]/parent::android.widget.LinearLayout/
#
# //android.widget.TextView[@text=”加入购物车”]/../../../following-sibling::android.view.View[2]/android.view.View/android.widget.TextView
# //android.widget.TextView[@text="添加"]//../../../following-sibling::android.widget.LinearLayout[]
#//android.widget.TextView[@text="添加"]preceding-sibling::android.widget.ImageView

#    //*[@resource-id='com.igen.solarmanpro:id/tv']