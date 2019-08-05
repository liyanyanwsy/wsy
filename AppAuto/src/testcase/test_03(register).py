#encoding:utf-8
import unittest,time,json
import requests
from appium import webdriver
from src.common.logger import Log
from src.common.dbsever import clogin_verify_code
class Test_cregister(unittest.TestCase):
    log=Log()
    def setUp(self):
        desired_caps={
            'platformName':'Android',
            'platformVersion':'5.1',
            'deviceName':'Y55DJZ9D99999999',
            'appPackage':'com.igen.rrgf',
            'appActivity':'com.igen.rrgf.activity.AdActivity',
            # 'unicodeKeyboard':True,
            # 'resetKeyboarf':Trueri
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(3)
        self.driver.find_element_by_id("com.igen.rrgf:id/tvRegister").click()
        time.sleep(3)
    def register1(self,nickname,email,password):
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(nickname)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys(email)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_3').send_keys(password)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/tvStatement').click()
        self.driver.implicitly_wait(3)
        self.assertEqual((self.driver.find_element_by_name(u'服务协议')),u'服务协议','fail')
        self.driver.tap([(8,36),(88,132)],500)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/cbStatement').click()
        self.driver.implicitly_wait(3)
        #加个判断选择狂是否选中
        self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
        self.driver.implicitly_wait(3)
        title=self.driver.find_element_by_name(u'首页')
        return title
    def register2(self,nickname,mobile,password):
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(nickname)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys(mobile)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_3').send_keys(password)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/tvStatement').click()
        self.driver.implicitly_wait(3)
        self.assertEqual((self.driver.find_element_by_name(u'服务协议')),u'服务协议','fail')
        self.driver.tap([(8,36),(88,132)],500)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/cbStatement').click()
        self.driver.implicitly_wait(3)
        #加个判断选择狂是否选中
        self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
        self.driver.implicitly_wait(3)
        title=self.driver.find_element_by_name(u'首页')
        return title

    def test_register_001(self):
        u'''邮箱注册账号'''
        self.log.info("------邮箱注册用例：start!---------")
        nickname=''
        email=''
        password=''
        title=self.register1(nickname,email,password)
        self.assertEqual(title,u'首页', False)
        self.log.info("----------pass!-------")
    def test_register_002(self):
        u'''手机注册账号 '''
        self.log.info("------手机注册用例：start!---------")
        nickname=''
        mobile=''
        password=''
        password=''
        title=self.register2(nickname,mobile,password)
        self.assertEqual(title,u'首页', False)
        self.log.info("----------pass!-------")
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
