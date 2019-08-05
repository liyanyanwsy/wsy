#encoding=utf-8
import unittest,time,json
from appium import webdriver
from src.common.logger import Log
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
        # self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.support.v7.app.ActionBar.e[2]").click()#切到超模25tab
        # self.driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout'and @index='2']").click()
        # self.driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[3]").click()
        # self.driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout'][3]").click()
        # self.driver.find_element_by_xpath("//*[@resouce_id='com.igen.rrgf:id/iv'][1]").click()
        # self.driver.find_element_by_xpath("//*[@resource-id='com.igen.rrgf:id/lyContainer']").click()
        # self.driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.igen.rrgf:id/lyContainer']/child::android.widget.FrameLayout[3]/*[@resource-id='com.igen.rrgf:id/iv']).click()
        #使用坐标来定位
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print x,y
        self.driver.tap([(0.67*x,0.93*y),(x,y)],500)
        #直接使用具体的坐标值进行定位
        # self.driver.tap([(480,1186),(720,1280)],500)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name(u'关于小麦光伏').click()
        self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.quit()
    def test_001(self):
        self.log.info("------功能介绍：start!---------")
        self.driver.find_element_by_name(u'功能介绍').click()
        self.driver.implicitly_wait(5)
        name=self.driver.find_element_by_name(u'功能介绍').text
        self.assertEqual(name,u'功能介绍','打开功能介绍失败')
        self.log.info("----------pass!-------")
    def test_002(self):
        self.log.info("------常见问题：start!---------")
        self.driver.find_element_by_name(u'常见问题').click()
        self.driver.implicitly_wait(5)
        name=self.driver.find_element_by_name(u'常见问题').text
        self.assertEqual(name,u'常见问题','打开常见问题失败')
        self.log.info("----------pass!-------")
    def test_003(self):
        self.log.info("------意见反馈：start!---------")
        self.driver.find_element_by_name(u'意见反馈').click()
        self.driver.implicitly_wait(10)
        name=self.driver.find_element_by_id('com.igen.rrgf:id/title_text').text
        self.assertEqual(name,u'意见反馈','打开意见反馈失败')
        self.log.info("----------pass!-------")
    def test_004(self):
        self.log.info("------隐私政策：start!---------")
        self.driver.find_element_by_name(u'隐私政策').click()
        self.driver.implicitly_wait(5)
        name=self.driver.find_element_by_name(u'隐私政策').text
        self.assertEqual(name,u'隐私政策','打开隐私政策失败')
        self.log.info("----------pass!-------")
    def test_005(self):
        self.log.info("------求打分：start!---------")
        self.driver.find_element_by_name(u'小麦光伏').click()
        self.driver.implicitly_wait(5)
        name=self.driver.find_element_by_name(u'小麦光伏').text
        self.assertEqual(name,u'小麦光伏','打开求打分失败')
        self.log.info("----------pass!-------")

    def test_006(self):
        self.log.info("------官网：start!---------")
        self.driver.find_element_by_id('com.igen.rrgf:id/tvOffice').click()
        self.driver.implicitly_wait(5)
        name=self.driver.find_element_by_name(u'官网').text
        self.assertEqual(name,u'12官网','打开官网失败')
        self.log.info("----------pass!-------")
    def test_007(self):
        self.log.info("------微博：start!---------")
        self.driver.find_element_by_id('com.igen.rrgf:id/tvWeibo').click()
        self.driver.implicitly_wait(10)
        name=self.driver.find_element_by_name(u'官方微博').text
        self.assertEqual(name,u'官方微博','打开微博失败')
        self.log.info("----------pass!-------")
    def test_008(self):
        self.log.info("------微信公众号：start!---------")
        self.driver.find_element_by_id('com.igen.rrgf:id/tvWechat').click()
        self.driver.implicitly_wait(5)
        name=self.driver.find_element_by_name(u'微信').text
        self.assertEqual(name,u'微信','打开微信失败')
        self.log.info("----------pass!-------")

if __name__ == '__main__':
    unittest.main()


