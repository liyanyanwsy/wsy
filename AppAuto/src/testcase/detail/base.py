#encoding:utf-8
import unittest,time,json
from appium import webdriver
from src.common.logger import Log
from src.common import dbsever
from src.common import MyExcepiton as M
def findItem(self,el):
    source = self.driver.page_source
    print source
    if el in source:
        return True
    else:
        return False
def isElement(self,identify,el):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    flag=None
    try:
        if identify == "id":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_id(el)
        elif identify == "xpath":
            #self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath(el)
        elif identify == "class":
            self.driver.find_element_by_class_name(el)
        elif identify == "link text":
            self.driver.find_element_by_link_text(el)
        elif identify == "partial link text":
            self.driver.find_element_by_partial_link_text(el)
        elif identify == "name":
            self.driver.find_element_by_name(el)
        elif identify == "tag name":
            self.driver.find_element_by_tag_name(el)
        elif identify == "css selector":
            self.driver.find_element_by_css_selector(el)
        flag = True
    except M.NoSuchElementException,e:
        flag = False
    finally:
        return flag


class Test_base(unittest.TestCase):
    log=Log()
    def setUp(self):
        desired_caps={
            'platformName':'Android',
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
        #使用坐标来定位，默认查看第一个电站
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print x,y
        self.driver.tap([(0.33*x,0.25*y),(0.65*x,0.3*y)],500)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
    # def test_001(self):
    #     self.log.info("------天气：start!---------")
    #     plant_status=self.driver.find_element_by_id('com.igen.rrgf:id/tvStatus').get_attribute('clickable')
    #     print plant_status
    #     if plant_status=='true':
    #         self.driver.find_element_by_id('com.igen.rrgf:id/tvStatus').click()
    #         self.driver.implicitly_wait(3)
    #         self.driver.find_element_by_id('com.igen.rrgf:id/ivWeather').click()
    #         self.driver.implicitly_wait(3)
    #         sunraise=self.driver.find_element_by_name(u'日出时间').text
    #         self.assertTrue(sunraise==u'日出时间','fail')
    #         self.log.info("----------天气pass!-------")
    #     else:
    #         self.driver.find_element_by_id('com.igen.rrgf:id/ivWeather').click()
    #         self.driver.implicitly_wait(3)
    #         sunset=self.driver.find_element_by_name(u'日落时间').text
    #         print sunset
    #         self.assertTrue(sunset==u'日落时间','fail')
    #         self.log.info("----------天气pass!-------")
    #
    #     #退出气象详情页面，点击后退按钮,现在直接使用坐标点击，后续需要改进
    #     x = self.driver.get_window_size()['width']
    #     y = self.driver.get_window_size()['height']
    #     print x,y
    #     self.driver.tap([(8,36),(88,132)],500)
    #     # self.driver.tap([(0.01*x,0.03*y),(0.12*x,0.1*y)],500)
    #     time.sleep(5)

    # def test_002(self):
    #     #暂时只显示点击进入到页面，然后关闭页面
    #     self.log.info("------分享：start!---------")
    #     self.driver.find_element_by_id('com.igen.rrgf:id/btnShare').click()
    #     self.driver.implicitly_wait(3)
    #     share_close=self.driver.find_element_by_id('com.igen.rrgf:id/btnMore').get_attribute('clickable')
    #     self.assertTrue(share_close=='true','fail')
    #     self.driver.implicitly_wait(3)
    #     self.driver.find_element_by_id('com.igen.rrgf:id/btnMore').click()
    #     self.log.info("----------分享pass!-------")

    def test_003(self):
        #未完成
        #报警，需要分有报警和没报警两种情况，最好选择有报警的电站进行测试
        self.log.info("------报警：start!---------")
        self.driver.find_element_by_id('com.igen.rrgf:id/btnAlert').click()
        time.sleep(5)
        # alarm_status=self.driver.find_element_by_name(u'暂无报警').is_displayed()
        # baojing=self.driver.find_element_by_name(u'暂无报警')
        alarm_status=isElement("name",u'暂无报警')
        print alarm_status
        #有报警情况
        if alarm_status==False:
            #类型筛选

            self.driver.find_element_by_id('com.igen.rrgf:id/tv_1').click()
            self.driver.implicitly_wait(3)
            #警报
            self.driver.tap([(20,377),(700,444)],500)

            #故障









        #设备筛选
        #时间筛选
        #报警详情
        else:
            pass
    def test_004(self):
        #未完成，无定位元素
        #更多
        self.driver.find_element_by_id('com.igen.rrgf:id/btnMore').click()
        self.driver.implicitly_wait(3)



        #编辑电站
        #电站设置
        #删除电站

    def test_005(self):
        #未完成
        #上传图片
        self.driver.find_element_by_id('com.igen.rrgf:id/btnMore').click()
        self.driver.implicitly_wait(3)

    def test_006(self):
        #电站简介
        self.driver.find_element_by_id('com.igen.rrgf:id/tv_cursor_1').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/tvName').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys()







    def test_007(self):
        #概览

    def test_008(self):
        #设备


if __name__ == '__main__':
    unittest.main()



