# -*- coding:utf-8 -*-
#from Pages.LoginPage import LoginPage
import sys
from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
import time
# import os
from Common import screen
import Logger
#scr_path = "D:\\Program Files\\Git\\11\\app\\Img\\"
scr_path = "D:\\appscreenshot\\"
def setup(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 设备系统
    desired_caps['platformVersion'] = '5.1'  # 设备系统版本
    #desired_caps['platformVersion'] = '6.0'  # 设备系统版本
    #desired_caps['platformVersion'] = '7.0'
    #desired_caps['deviceName'] = '55CDU16C07007057'
    desired_caps['deviceName'] = 'Y55DJZ9D99999999'  #  设备名称
    #desired_caps['deviceName'] = '3cec677 device'  #  设备名称
    desired_caps['appPackage'] = 'com.igen.solarmanpro'
    desired_caps['appActivity'] = 'com.igen.solarmanpro.activity.MainActivity'
    #time.sleep(5)
    #desired_caps['automationName'] ="UiAutomator2"
    #desired_caps['automationName'] = 'Selendroid'

    #time.sleep(5)
    self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    time.sleep(5)

def teardown(self):
    Logger.log.info("TestCase:" + self._testMethodName)
    if sys.exc_info()[0]:
        print sys.exc_info()
        Logger.log.info("Error:" + self._testMethodName)
        screen.screenshot()
        Logger.log.info("Save Img to: " + scr_path + self._testMethodName + ".png")
    else:
        Logger.log.info("Passed:" + self._testMethodName)
    self.driver.quit()

def Login(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 设备系统
    desired_caps['platformVersion'] = '5.1'  # 设备系统版本
    #desired_caps['platformVersion'] = '6.0'  # 设备系统版本
    desired_caps['deviceName'] = 'Y55DJZ9D99999999'  #  设备名称
    #desired_caps['deviceName'] = '3cec677 device'  #  设备名称
    desired_caps['appPackage'] = 'com.igen.solarmanpro'
    desired_caps['appActivity'] = 'com.igen.solarmanpro.activity.MainActivity'
    self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    time.sleep(5)
    self.driver.find_element_by_xpath('//*[@resource-id="com.igen.solarmanpro:id/btnLogin"]').click()
    self.driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/etName']").send_keys("17798736289")
    self.driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/etPsw']").send_keys("111111")
    self.driver.hide_keyboard()
    self.driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/btnLogin']").click()
    time.sleep(10)

# def screenshot():
#     timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
#     os.popen("adb wait-for-device")
#     os.popen("adb shell screencap -p /sdcard/data/local/tmp/tmp.png")
#     temp='D:/appscreenshot/' +timestamp + '.png'
#     os.popen("adb pull /sdcard/data/local/tmp/tmp.png " + temp )
#     os.popen("adb shell rm /sdcard/data/local/tmp/tmp.png")
#     print "success"





