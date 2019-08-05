# coding:utf-8
from appium import webdriver
import time
desired_caps={
    'platformName':'Android',
    'platformVersion':'5.1',
    'deviceName':'Y55DJZ9D99999999',
    'appPackage':'com.baidu.yuedu',
    'appActivity':'com.baidu.yuedu.splash.SplashActivity',
    # 'unicodeKeyboard':True,
    # 'resetKeyboarf':True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(20)
# driver.find_element_by_id("com.baidu.yuedu:id/main_activity_tab_pager").click()
# driver.find_element_by_name(u"图书").click()
driver.find_element_by_class_name("android.webkit.WebView").click()
# driver.tap([(287,153),(343,191)],500)
time.sleep(15)
contexts=driver.contexts
print contexts

