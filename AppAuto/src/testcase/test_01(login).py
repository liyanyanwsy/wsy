#encoding:utf-8
import unittest,time,json
import requests
from appium import webdriver
from src.common.logger import Log
from src.functions.LoginPage import LoginPage
from src.functions.BaseAction import Page
page=Page()
loginpage=LoginPage()
class Test_clogin(unittest.TestCase):
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
            # 'unicodeKeyboard':True,
            # 'resetKeyboarf':True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        page.sleep(10)
        loginpage.click_login_btn1()
    def login(self,username,password):
        # self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(username)
        # self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys(password)
        # self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
        loginpage.input_username(username)
        loginpage.input_password(password)
        loginpage.click_login_btn2()
        url='http://apic-cdn.solarman.cn/v/ap.2.0/user/login?user_id=%s&user_pass=%s&terminate=android&push_sn=c78d93f9d937ef8ce8660a8570d291b9&timezone=8&lan=zh&country=CN' %(username,password)
        res = requests.get(url)
        result1=res.content
        self.log.info("小麦光伏登录结果：%s"%result1)
        result2=json.loads(result1)
        return result2
    def test_login_001(self):
        driver=self
        u'''测试登录：正确账号，错误密码'''
        self.log.info("------登录失败用例：start!---------")
        username='zedlital@163.com'
        self.log.info("输入正确账号：%s"%username)
        password='111111'
        self.log.info("输入错误密码：%s"%password)
        result = self.login(username, password)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result['result']=='1', False)
        self.log.info("----------pass!-------")
    def test_login_002(self):
        u'''测试登录：正确账号，正确密码'''
        self.log.info("------登录成功用例：start!---------")
        username='zedlital@163.com'
        self.log.info("输入正确账号：%s"%username)
        password='zedl1990'
        self.log.info("输入正确密码：%s"%password)
        result = self.login(username, password)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result['result']=='1', True)
        self.log.info("----------pass!-------")

    def tearDown(self):
        page.teardown()
if __name__ == '__main__':
     unittest.main()

