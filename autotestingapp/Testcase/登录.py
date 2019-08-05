# -*- coding:utf-8 -*-
import os, time, unittest
from appium  import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '5.1'  # 设备系统版本
desired_caps['deviceName'] = 'Y55DJZ9D99999999'  #  设备名称
desired_caps['appPackage'] = 'com.igen.solarmanpro'
desired_caps['appActivity'] = 'com.igen.solarmanpro.activity.MainActivity'
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
#点击登录按钮
driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()
driver.find_element_by_id("com.igen.solarmanpro:id/etName").send_keys("17798736289")
driver.find_element_by_id("com.igen.solarmanpro:id/etPsw").send_keys("123456")
driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()