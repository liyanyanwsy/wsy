#encoding:utf-8
from appium import webdriver
import unittest
import time,sys
import requests
import MySQLdb
from Common import Logger,screen

# scr_path = "D:\\appscreenshot\\"
# def verify_code():
#     try:
#         conn = MySQLdb.connect(host='192.168.1.53', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
#                                port=3306, charset='utf8')
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM sys_verify_message WHERE verify_account='17798735555' ORDER BY udpate_time DESC LIMIT 1")
#         re1 = cur.fetchall()
#         a=list(re1[0])[2]
#         cur.close()
#         conn.close()
#         return a
#     except Exception,e:
#         print e
# class FreeRegitration():
#     def setUP(self):
#         desired_caps={
#             'platformName':'Android',
#             'platformVersion':'5.1',
#             'deviceName':'Y55DJZ9D99999999',
#             'appPackage':'com.igen.solarmanpro',
#             'appActivity':'com.igen.solarmanpro.activity.MainActivity',
#             # 'unicodeKeyboard':True,
#             # 'resetKeyboarf':True
#         }
#         self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#         time.sleep(3)
#     def test_Regitration(self):
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/btnRegister").click()
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/etName").send_keys('liyanyan')
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/etPhone").send_keys('17798735555')
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/etPwd").send_keys('111111')
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/btn_1").click()
#         self.driver.implicitly_wait(15)
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/codeInput").send_keys(verify_code())
#         self.driver.find_element_by_id('com.igen.solarmanpro:id/btn_1').click()
#         self.driver.tap([(568,36),(712,132)],500)
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/btnAddLicense").click()
#         self.driver.tap([(388.3,1049.0),(0,0)],500)
#         time.sleep(5)
#         self.driver.tap([(517.9,651.0),(0,0)],500)
#         time.sleep(5)
#         self.driver.tap([(93.5,225.1),(0,0)],500)
#         time.sleep(5)
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/btnConfirm").click()
#         time.sleep(5)
#         self.driver.tap([(568,36),(712,132)],500)
#         self.driver.find_element_by_id("com.igen.solarmanpro:id/btnConfirm").click()
#     def tearDown(self):
#         Logger.log.info("TestCase:" + self._testMethodName)
#         if sys.exc_info()[0]:
#             print sys.exc_info()
#             Logger.log.info("Error:" + self._testMethodName)
#             screen.screenshot()
#             Logger.log.info("Save Img to: " + scr_path + self._testMethodName + ".png")
#         else:
#             Logger.log.info("Passed:" + self._testMethodName)
#         self.driver.quit()
# if __name__ == '__main__':
#     unittest.main()




desired_caps={
            'platformName':'Android',
            'platformVersion':'5.1',
            'deviceName':'Y55DJZ9D99999999',
            'appPackage':'com.igen.solarmanpro',
            'appActivity':'com.igen.solarmanpro.activity.MainActivity',
            # 'unicodeKeyboard':True,
            # 'resetKeyboarf':True
        }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(3)
    
    

driver.find_element_by_id("com.igen.solarmanpro:id/btnRegister").click()
driver.find_element_by_id("com.igen.solarmanpro:id/etName").send_keys('liyanyan')
driver.find_element_by_id("com.igen.solarmanpro:id/etPhone").send_keys('17798739090')
driver.find_element_by_id("com.igen.solarmanpro:id/etPwd").send_keys('111111')
driver.find_element_by_id("com.igen.solarmanpro:id/btn_1").click()
driver.implicitly_wait(15)
driver.find_element_by_id("com.igen.solarmanpro:id/codeInput").send_keys('123456')
driver.find_element_by_id('com.igen.solarmanpro:id/btn_1').click()

# driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()
# driver.find_element_by_id("com.igen.solarmanpro:id/etName").send_keys("17798735555")
# driver.find_element_by_id("com.igen.solarmanpro:id/etPsw").send_keys('111111')
# driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()

driver.find_element_by_id("com.igen.solarmanpro:id/etCompanyName").send_keys("wuxidichan889901")
driver.find_element_by_id("com.igen.solarmanpro:id/etCompanyAddr").send_keys("tiananzhihuicheng009")
driver.find_element_by_id("com.igen.solarmanpro:id/etLicense").send_keys('0009900887649')
# driver.find_element_by_xpath("//*[@text=u'下一步']").click()
driver.tap([(568,36),(712,132)],500)
driver.find_element_by_id("com.igen.solarmanpro:id/btnAddLicense").click()
driver.tap([(388.3,1049.0),(0,0)],500)

time.sleep(5)
driver.tap([(517.9,651.0),(0,0)],500)
time.sleep(5)
driver.tap([(93.5,225.1),(0,0)],500)
time.sleep(5)
driver.find_element_by_id("com.igen.solarmanpro:id/btnConfirm").click()
time.sleep(5)
driver.tap([(568,36),(712,132)],500)
driver.find_element_by_id("com.igen.solarmanpro:id/btnConfirm").click()




#1、公司名称等输入无法输入中文
#2、公司名称、公司地址、工商注册号、手机号/邮箱等不能重复，如何自动化去输入这些参数
#3、最后邮箱验证
#4、如何写成对应的测试用例











