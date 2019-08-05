#encoding:utf-8
import unittest,time,json
import requests
from appium import webdriver
from src.common.logger import Log
from appium.webdriver.webelement import WebElement
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from appium.webdriver.webdriver import WebDriverWait
class Test_cplant(unittest.TestCase):
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
        self.driver.implicitly_wait(3)
        # self.driver.find_element_by_id("com.igen.rrgf:id/tvLogin").click()
        # self.dri ver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys('17798736289')
        # self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys('111111')
        # self.driver.find_element_by_id('com.igen.rrgf:id/btn_1').click()
    def tearDown(self):
        self.driver.quit()
    def createplant1(self,plant_name,connect):
        #默认，不添加设备
        self.log.info("------创建电站：start!---------")
        self.driver.find_element_by_id('com.igen.rrgf:id/btnAdd').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_name(u"暂无设备").click()
        time.sleep(10)
        # plant_type=self.driver.find_element_by_id('com.igen.rrgf:id/rdBtn_1').is_selected()
        # self.assertEqual(plant_type,True)
        # grip_type=self.driver.find_element_by_id('com.igen.rrgf:id/rdBtn_21').is_selected()
        # self.assertEqual(grip_type,True)
        self.driver.find_element_by_name(u"下一步").click()
        time.sleep(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(plant_name)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys(connect)
        time.sleep(3)
        self.driver.find_element_by_name(u"完成").click()
        time.sleep(5)
        plantname=self.driver.find_element_by_id('com.igen.rrgf:id/tvName').text
        return plantname
    def createplant2(self,capacity,currency,etPrice,plant_name,connect):
        #修改参数，商用屋顶，储能，不添加设备
        self.log.info("------创建电站：start!---------")
        self.driver.find_element_by_id('com.igen.rrgf:id/btnAdd').click()
        time.sleep(3)
        self.driver.find_element_by_name(u"暂无设备").click()
        time.sleep(5)
        self.driver.find_element_by_id('com.igen.rrgf:id/rdBtn_2').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/rdBtn_24').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.igen.rrgf:id/etCapacity').clear()
        self.driver.find_element_by_id('com.igen.rrgf:id/etCapacity').send_keys(capacity)
        # self.driver.scroll()
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        # print x,y
        # #屏幕向下滑动
        # x1 = x * 0.5  #x坐标
        # y1 = y * 0.75   #起始y坐标
        # y2 = y* 0.25   #终点y坐标
        # print x1,y1,y2
        # self.driver.swipe(x1,y1,x1,y2,1000)

        # origin_el=self.driver.find_element_by_id('com.igen.rrgf:id/lyLoc')
        # destination_el=self.driver.find_element_by_id('com.igen.rrgf:id/lyStandardPrice')
        # self.driver.scroll(self, origin_el, destination_el)
        time.sleep(5)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print x,y
        #屏幕向下滑动
        x1 = int(x * 0.5)  #x坐标
        y1 = int(y * 0.75)   #起始y坐标
        y2 =int(y* 0.25)   #终点y坐标
        print x1,y1,y2
        self.driver.swipe(x1,y1,x1,y2,1000)
        # self.driver.scroll()
        self.driver.implicitly_wait(3)
        time.sleep(5)
        # WebDriverWait(self.driver,6).until(lambda driver:self.driver.find_element_by_name(u'币种'))
        self.driver.find_element_by_id('com.igen.rrgf:id/tvCurrency').click()
        time.sleep(5)
        self.driver.find_element_by_name(currency).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_name(u'保存').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.igen.rrgf:id/etPrice').clear()
        self.driver.find_element_by_id('com.igen.rrgf:id/etPrice').send_keys(etPrice)
        time.sleep(3)
        self.driver.find_element_by_name(u"下一步").click()
        time.sleep(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(plant_name)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys(connect)
        time.sleep(3)
        self.driver.find_element_by_name(u"完成").click()
        # WebDriverWait(self.driver,5).until()
        plantname=self.driver.find_element_by_id('com.igen.rrgf:id/tvName').text
        return plantname
    def createplant3(self,sn,capacity,currency,standardPrice,plant_name,connect):
        #默认，手动添加设备
        self.log.info("------创建电站：start!---------")
        self.driver.find_element_by_id('com.igen.rrgf:id/btnAdd').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/btnManual').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/etSn').send_keys(sn)
        time.sleep(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/btn').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.igen.rrgf:id/etCapacity').clear()
        self.driver.find_element_by_id('com.igen.rrgf:id/etCapacity').send_keys(capacity)
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        #屏幕向下滑动
        x1 = int(x * 0.5)  #x坐标
        y1 = int(y * 0.75)   #起始y坐标
        y2 =int(y* 0.25)   #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,1000)
        self.driver.implicitly_wait(3)

        self.driver.find_element_by_id('com.igen.rrgf:id/tvCurrency').click()
        time.sleep(5)
        self.driver.find_element_by_name(currency).click()
        time.sleep(5)
        self.driver.find_element_by_name(u'保存').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.igen.rrgf:id/etStandardPrice').clear()
        self.driver.find_element_by_id('com.igen.rrgf:id/etStandardPrice').send_keys(standardPrice)
        time.sleep(3)
        self.driver.find_element_by_name(u"下一步").click()
        time.sleep(3)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_1').send_keys(plant_name)
        self.driver.find_element_by_id('com.igen.rrgf:id/et_2').send_keys(connect)
        time.sleep(3)
        self.driver.find_element_by_name(u"完成").click()
        time.sleep(3)
        plantname=self.driver.find_element_by_id('com.igen.rrgf:id/tvName').text
        return plantname
    def test_createplant001(self):
        u'''默认创建电站'''
        self.log.info("------创建电站用例001：start!---------")
        plant_name='test001'
        self.log.info("电站名称为：%s"%plant_name)
        connect='17798736289'
        self.log.info("联系电话为：%s"%connect)
        plantname = self.createplant1(plant_name,connect)
        self.assertEqual(plantname,plant_name,'创建电站失败')
        #self.assertTrue(plantname.text==plant_name,False)
        self.log.info("----------pass!-------")
    def test_createplant002(self):
        u'''修改参数'''
        self.log.info("------创建电站用例002：start!---------")
        capacity='10'
        self.log.info("装机容量为：%s"%capacity)
        currency=u"JPY (日元)"
        self.log.info("币种为：%s"%currency)
        AvgPrice='1.750'
        self.log.info("平均电价为：%s"%AvgPrice)
        plant_name='test002'
        self.log.info("电站名称为：%s"%plant_name)
        connect='17798736289'
        self.log.info("联系电话为：%s"%connect)
        plantname = self.createplant2(capacity,currency,AvgPrice,plant_name,connect)
        self.assertEqual(plantname,plant_name,'创建电站失败')
        self.log.info("----------pass!-------")
    def test_createplant003(self):

        u'''添加设备'''
        self.log.info("------创建电站用例003：start!---------")
        sn='523123'
        self.log.info("sn为：%s"%sn)
        capacity='10'
        self.log.info("装机容量为：%s"%capacity)
        currency=u"JPY (日元)"
        self.log.info("币种为：%s"%currency)
        standardPrice='1.750'
        self.log.info("标杆电价为：%s"%standardPrice)
        plant_name='test003'
        self.log.info("电站名称为：%s"%plant_name)
        connect='17798736289'
        self.log.info("联系电话为：%s"%connect)
        plantname = self.createplant3(sn,capacity,currency,standardPrice,plant_name,connect)
        self.assertEqual(plantname,plant_name,'创建电站失败')
        self.log.info("----------pass!-------")

if __name__ == '__main__':
    unittest.main()


















