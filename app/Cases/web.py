import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# driver=webdriver.Firefox()
driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://pro.solarman.cn/login/login.do")
# driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_xpath("//*[@class='close close-ico tra-fast']").click()
driver.find_element_by_id('userName').send_keys('17798736289')
time.sleep(1)
driver.find_element_by_id('password').send_keys('123456')
time.sleep(1)
driver.find_element_by_id('login').click()
driver.implicitly_wait(60)