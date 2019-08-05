#encoding:utf-8
import unittest,time,json
import requests
from appium import webdriver
from src.common.logger import Log
def login(self,username,password):
    desired_caps={
                'platformName':'Android',
            # 'platformVersion':'8.0.0',
            # 'deviceName':'MKJNW18623000168',
            'platformVersion':'5.1',
            'deviceName':'Y55DJZ9D99999999',
            'appPackage':'com.igen.rrgf',
            'appActivity':'com.igen.rrgf.activity.AdActivity',
            # 'unicodeKeyboard':True,
            # 'resetKeyboarf':True
                }
    self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    time.sleep(3)
    self.driver.find_element_by_id("com.igen.rrgf:id/tvLogin").click()
    self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(username)
    self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys(password)
    self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
    return self.driver




