#encoding:utf-8
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import  re
import time
# firefox浏览器配置文件地址
profile_directory = r'C:\Users\admin\AppData\Roaming\Mozilla\Firefox\Profiles\yn80ouvt.default'
# 加载配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)

driver.get('https://home.cnblogs.com/u/wanshiyu/relation/following')
time.sleep(3)
cookies=driver.get_cookies()
print cookies
driver.quit()

s=requests.session()
c = requests.cookies.RequestsCookieJar()
for i in cookies:
    c.set(i['name'],i['value'])
s.cookies.update(c)

r1=s.get("")



