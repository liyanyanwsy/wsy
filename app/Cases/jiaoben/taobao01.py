# -*- coding:utf-8 -*-
from appium import webdriver
import time
desired_caps={
            'platformName':'Android',
            'platformVersion':'5.1',
            'deviceName':'Y55DJZ9D99999999',
            'appPackage':'com.taobao.taobao',
            'appActivity':'com.taobao.tao.welcome.Welcome',
            'unicodeKeyboard':True,
            'resetKeyboarf':True
            }

# desired_caps = {}
# desired_caps['platformName'] = 'Android'  # 设备系统
# desired_caps['platformVersion'] = '5.1'  # 设备系统版本
# #desired_caps['platformVersion'] = '6.0'  # 设备系统版本
# desired_caps['deviceName'] = 'Y55DJZ9D99999999'  #  设备名称
# #desired_caps['deviceName'] = '3cec677 device'  #  设备名称
# desired_caps['appPackage'] = 'com.taobao.taobao'
# desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
# driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"hao")
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys(u"餐椅")
driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()
# driver.find_element_by_name("天猫").click()
#driver.tap([(19,362),(136,454)],500)

# driver.find_element_by_xpath('//*[@resource-id="com.igen.sox`larmanpro:id/btnLogin"]').click()
# driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/etName']").send_keys("17798736289")
# driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/etPsw']").send_keys("111111")
# driver.hide_keyboard()
# driver.find_element_by_xpath("//*[@resource-id='com.igen.solarmanpro:id/btnLogin']").click()