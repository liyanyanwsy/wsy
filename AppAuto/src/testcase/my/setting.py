#encoding=utf-8
import unittest,time,json
from appium import webdriver
from src.common.logger import Log
from src.common import dbsever
class Test_about(unittest.TestCase):
    log=Log()
    def setUp(self):
        desired_caps={
            'platformName':'Android',
            # 'platformVersion':'8.0.0',
            # 'deviceName':'MKJNW18623000168',
            'platformVersion':'5.1',
            'deviceName':'Y55DJZ9D99999999',
            'appPackage':'com.igen.rrgf',
            'appActivity':'com.igen.rrgf.activity.AdActivity',
            'unicodeKeyboard':True,
            'resetKeyboarf':True,
            'noReset':True,
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(5)
        #使用坐标来定位
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print x,y
        self.driver.tap([(0.67*x,0.93*y),(x,y)],500)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.igen.rrgf:id/lySet').click()
        self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.quit()
    def Accout(self,pass1,pass2,mobile,email):
        self.log.info("------账号安全：start!---------")
        self.driver.find_element_by_name(u'账户安全').click()
        self.driver.implicitly_wait(3)

        #手机号
        self.driver.find_element_by_id('com.igen.rrgf:id/lyMobile').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(mobile)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
        self.driver.implicitly_wait(3)
        mobile_code=dbsever.cmobile_verify_code(mobile)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(mobile_code)
        time.sleep(5)
        self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
        #邮箱


        #修改密码
        self.driver.find_element_by_id('com.igen.rrgf:id/lyChangPwd').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(pass1)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys(pass2)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_name(u'完成').click()
        self.log.info("------修改密码pass!---------")
    def test_001(self):
        u'''账号安全'''
        self.log.info("------设置001：start!---------")
        pass1='12345678'
        pass2='12345678'
        mobile='17712356789'
        email=''

    #报警消息中为找到断言方法
    # def test_002(self):
    #     self.log.info("------消息：start!---------")
    #     self.driver.find_element_by_name(u'消息').click()
    #     self.driver.implicitly_wait(3)
    #     self.assertEqual((self.driver.find_element_by_name(u'消息').text),u'消息','fail')
    #     self.driver.find_element_by_name(u'报警消息').click()
    #     self.driver.implicitly_wait(5)
    #     #报警消息
    #     #需要加判断，查看是否选择，如果没有选择，进行选择操作，选择后断言是否被选择上
    #     swnotice=self.driver.find_element_by_id('com.igen.rrgf:id/swNotice').is_selected()
    #     swNoticeEmail=self.driver.find_element_by_id('com.igen.rrgf:id/swNoticeEmail').is_selected()
    #     swNoticeSms=self.driver.find_element_by_id('com.igen.rrgf:id/swNoticeSms').is_selected()
    #
    #     print swnotice,swNoticeEmail,swNoticeSms
    #     if swnotice==False:
    #         self.driver.find_element_by_id('com.igen.rrgf:id/swNotice').click()
    #         self.driver.implicitly_wait(3)
    #         self.assertTrue(swnotice==True,'fail')
    #     else:
    #         self.driver.find_element_by_id('com.igen.rrgf:id/swNotice').click()
    #         self.driver.implicitly_wait(3)
    #         self.assertTrue(swnotice==False,'fail')


    #隐私中为找到断言方法
    # def test_003(self):
    #     self.log.info("------隐私：start!---------")

    # def test_004(self):
    #     self.log.info("------通用：start!---------")
    #     self.driver.find_element_by_name(u'通用').click()
    #     self.driver.implicitly_wait(3)
    #     self.assertEqual((self.driver.find_element_by_name(u'通用').text),u'通用','fail')
    #     #温度单位
    #     self.driver.find_element_by_id('com.igen.rrgf:id/tvTempUnit').click()
    #     time.sleep(5)
    #     # ssd=self.driver.find_element_by_name(u'摄氏度(℃)').is_selected()
    #     # hsd=self.driver.find_element_by_name(u'华氏度(℉)').is_selected()
    #     ssd=self.driver.find_element_by_name(u'摄氏度(℃)').get_attribute('checked')
    #     hsd=self.driver.find_element_by_name(u'华氏度(℉)').get_attribute('checked')
    #     print ssd,hsd
    #     if ssd=='false':
    #         self.driver.find_element_by_name(u'摄氏度(℃)').click()
    #         self.driver.implicitly_wait(3)
    #         temp=(self.driver.find_element_by_id('com.igen.rrgf:id/tvTempUnit')).text
    #         self.assertTrue(temp==u'℃','fail')
    #     else:
    #         self.driver.find_element_by_name(u'华氏度(℉)').click()
    #         self.driver.implicitly_wait(3)
    #         temp=(self.driver.find_element_by_id('com.igen.rrgf:id/tvTempUnit')).text
    #         self.assertTrue(temp==u'℉','fail')
    #     self.log.info("----------温度单位pass!-------")
    #     #自动横屏
    #     self.driver.find_element_by_id('com.igen.rrgf:id/tvOrientation').click()
    #     time.sleep(5)
    #     # ssd=self.driver.find_element_by_name(u'摄氏度(℃)').is_selected()
    #     # hsd=self.driver.find_element_by_name(u'华氏度(℉)').is_selected()
    #     jz=self.driver.find_element_by_name(u'禁止').get_attribute('checked')
    #     yx=self.driver.find_element_by_name(u'允许').get_attribute('checked')
    #     print jz,yx
    #     if jz=='false':
    #         self.driver.find_element_by_name(u'禁止').click()
    #         self.driver.implicitly_wait(3)
    #         hp=(self.driver.find_element_by_id('com.igen.rrgf:id/tvOrientation')).text
    #         self.assertTrue(hp==u'禁止','fail')
    #     else:
    #         self.driver.find_element_by_name(u'允许').click()
    #         self.driver.implicitly_wait(3)
    #         hp=(self.driver.find_element_by_id('com.igen.rrgf:id/tvOrientation')).text
    #         self.assertTrue(hp==u'允许','fail')
    #     self.log.info("----------自动横屏pass!-------")
    #     #多语言
    #     self.driver.find_element_by_id('com.igen.rrgf:id/tvLanguage').click()
    #     time.sleep(5)
    #     gsxt=self.driver.find_element_by_name(u'跟随系统').get_attribute('checked')
    #     jtzw=self.driver.find_element_by_name(u'简体中文').get_attribute('checked')
    #     en=self.driver.find_element_by_name(u'English').get_attribute('checked')
    #     print gsxt,jtzw,en
    #     if gsxt=='false':
    #         self.driver.find_element_by_name(u'跟随系统').click()
    #         time.sleep(5)
    #         #使用坐标来定位
    #         x = self.driver.get_window_size()['width']
    #         y = self.driver.get_window_size()['height']
    #         print x,y
    #         self.driver.tap([(0.67*x,0.93*y),(x,y)],500)
    #         time.sleep(5)
    #         self.driver.find_element_by_id('com.igen.rrgf:id/lySet').click()
    #         self.driver.implicitly_wait(5)
    #         self.driver.find_element_by_name(u'通用').click()
    #         lan=(self.driver.find_element_by_id('com.igen.rrgf:id/tvLanguage')).text
    #         self.assertTrue(lan==u'跟随系统','fail')
    #     else:
    #         self.driver.find_element_by_name(u'English').click()
    #         time.sleep(5)
    #         #使用坐标来定位
    #         x = self.driver.get_window_size()['width']
    #         y = self.driver.get_window_size()['height']
    #         print x,y
    #         self.driver.tap([(0.67*x,0.93*y),(x,y)],500)
    #         time.sleep(5)
    #         self.driver.find_element_by_id('com.igen.rrgf:id/lySet').click()
    #         self.driver.implicitly_wait(5)
    #         self.driver.find_element_by_name(u'General').click()
    #         lan=(self.driver.find_element_by_id('com.igen.rrgf:id/tvLanguage')).text
    #         self.assertTrue(lan==u'English','fail')
    #         self.driver.find_element_by_id('com.igen.rrgf:id/tvLanguage').click()
    #         self.driver.implicitly_wait(3)
    #         #点击跟随系统后跳转到首页
    #         self.driver.find_element_by_name(u'Follow the system').click()
    #         time.sleep(5)
    #
    #     self.log.info("----------多语言pass!-------")

    # def test_005(self):
    #     self.log.info("------编辑个人信息：start!---------")
    #     #头像上传不知道如何进行断言操作，后续补充，先进行截图操作
    #     self.driver.find_element_by_id('com.igen.rrgf:id/iv_1').click()
    #     self.driver.implicitly_wait(3)
    #     #头像
    #     self.driver.find_element_by_id('com.igen.rrgf:id/lyPortrait').click()
    #     # x=self.driver.get_window_size['width']
    #     # y=self.driver.get_window_size['height']
    #
    #     self.driver.tap([(431,997),(0,0)],500)
    #     time.sleep(5)
    #     self.driver.tap([(200,368),(0,0)],500)
    #     time.sleep(5)
    #     self.driver.find_element_by_id('com.igen.rrgf:id/clip_sure').click()
    #     time.sleep(5)
    #     self.log.info("----------头像上传pass!-------")
    #     #头像上传不知道如何进行断言操作，后续补充，先进行截图操作
    #     #昵称
    #     self.driver.find_element_by_id('com.igen.rrgf:id/tv_2').click()
    #     self.driver.implicitly_wait(3)
    #     self.driver.find_element_by_id('com.igen.rrgf:id/et_1').clear()
    #     self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys('juaile123')
    #     self.driver.find_element_by_name(u'完成').click()
    #     self.driver.implicitly_wait(3)
    #     nickname=self.driver.find_element_by_id('com.igen.rrgf:id/tv_2').text
    #     self.assertTrue(nickname=='juaile123','fail')
    #     self.log.info("----------昵称pass!-------")
    #     #简介
    #     self.driver.find_element_by_id('com.igen.rrgf:id/tv_3').click()
    #     self.driver.implicitly_wait(3)
    #     self.driver.find_element_by_id('com.igen.rrgf:id/et_1').clear()
    #     self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys('111abc')
    #     self.driver.find_element_by_name(u'完成').click()
    #     self.driver.implicitly_wait(3)
    #     jj=self.driver.find_element_by_id('com.igen.rrgf:id/tv_3').text
    #     self.assertTrue(jj=='111abc','fail')
    #     self.log.info("----------简介pass!-------")
    #     #常住地
    #     self.driver.find_element_by_id('com.igen.rrgf:id/tvResidence').click()
    #     time.sleep(5)
    #     # self.driver.find_element_by_id('com.igen.rrgf:id/tv_1').click()
    #     self.driver.find_element_by_name(u'无锡').click()
    #     time.sleep(5)
    #     czd=self.driver.find_element_by_id('com.igen.rrgf:id/tvResidence').text
    #     self.assertTrue(czd==u'无锡','fail')
    #     self.log.info("----------常住地pass!-------")

if __name__ == '__main__':
    unittest.main()

