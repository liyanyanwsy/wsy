# coding=utf-8
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
# 真机
#"deviceName": "MKJNW18623000168",
desired_caps = {
    "platformName": "Android",
    'platformVersion':'5.1',
    'deviceName':'Y55DJZ9D99999999',
    #"udid": "Y55DJZ9D99999999",
    "appPackage": "com.igen.solarmanpro",
    "appActivity": "com.igen.solarmanpro.activity.MainActivity",
    "noReset": 'true',
    'automationName': 'uiautomator2'
}

#uiautomator2 只有automationName的参数为uiautomator2 才可以处理弹出框 谨记谨记谨记
# 连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(2)

#
# print('元素检测')
# # 用于检测是否是第一次打开APP（第一次打开APP会有引导页）
# try:
#   my = driver.find_element_by_id('com.igen.solarmanpro:id/btnLogin')
# except Exception as e:
#   print('未找到元素')
# else:
#  my.click()
# # 输入用户名
# driver.find_element_by_id('com.igen.solarmanpro:id/etName').clear()
# driver.find_element_by_id('com.igen.solarmanpro:id/etName').click()
# driver.find_element_by_id('com.igen.solarmanpro:id/etName').send_keys('2911050293@qq.com')
# # 输入密码
# driver.find_element_by_id('com.igen.solarmanpro:id/etPsw').click()
# driver.find_element_by_id('com.igen.solarmanpro:id/etPsw').send_keys('624614ying')
#
# # 点击登录
# element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID,'com.igen.solarmanpro:id/btnLogin')))
# element.click()

elementplant = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID,'com.igen.solarmanpro:id/ibtn1')))
elementplant.click()
sleep(5)
driver.find_elements_by_id("com.igen.solarmanpro:id/tvName")[0].click()


width=driver.get_window_size().get('width')
height=driver.get_window_size().get('height')
print(width)
print(height)
driver.swipe(int(width)/2,int(height)/2,int(width)/2,int(height)/4,duration=sleep(2))