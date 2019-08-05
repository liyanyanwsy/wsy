#encoding:utf-8
import unittest,time,json
import requests
from appium import webdriver
from src.common.logger import Log
#from src.common.dbsever import clogin_verify_code
desired_caps={
    'platformName':'Android',
    # 'platformVersion':'8.0.0',
    # 'deviceName':'MKJNW18623000168',
    'platformVersion':'5.1',
    'deviceName':'Y55DJZ9D99999999',
    # 'appPackage':'com.igen.rrgf',
    # 'appActivity':'com.igen.rrgf.activity.dActivity',
    "appPackage": "com.igen.solarmanpro",
    "appActivity": "com.igen.solarmanpro.activity.MainActivity",
    'automationName': 'uiautomator2'
    # 'unicodeKeyboard':True,
    # 'resetKeyboarf':Trueri}
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(3)
driver.find_element_by_id("com.igen.solarmanpro:id/btnLogin").click()
time.sleep(5)
driver.find_element_by_id('com.igen.solarmanpro:id/tvLoginProblem').click()
time.sleep(5)
driver.find_element_by_id('com.igen.solarmanpro:id/et_1').send_keys('17798736289')
time.sleep(5)
driver.find_element_by_id('com.igen.solarmanpro:id/btn_1').click()

driver.find_element_by_id('com.igen.solarmanpro:id/codeInput').send_keys('123456')

time.sleep(20)
driver.quit()







#     def loginpro(self,mobile,pass1,pass2):
#         self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(mobile)
#         time.sleep(3)
#         self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
#         time.sleep(5)
#         verify_code=clogin_verify_code()
#         self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(verify_code)
#         time.sleep(5)
#         self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
#         time.sleep(3)
#         self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(pass1)
#         time.sleep(5)
#         self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(pass2)
#         time.sleep(5)
#         self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
#         time.sleep(5)
#         url=self.driver.current_url
#         print url
#         res=requests.get(url)
#         result1=res.content
#         self.log.info("小麦光伏重置密码结果：%s"%result1)
#         result2=json.loads(result1)
#         return result2
#
#
#
#     def test_loginpro_001(self):
#         u'''可以正确发送验证码并成功修改密码'''
#         self.log.info("------成功修改密码用例：start!---------")
#         mobile='17798736289'
#         pass1='222222'
#         pass2='222222'
#         result=self.loginpro(mobile,pass1,pass2)
#         self.log.info("获取测试结果：%s"%result)
#         self.assertEqual(result['result']=='1', True)
#         self.log.info("----------pass!-------")
#     def tearDown(self):
#         self.driver.quit()
# if __name__ == '__main__':
#     unittest.main()












