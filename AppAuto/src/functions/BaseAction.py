# -*- coding:utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
#你可以用selenium提供的 expected_conditions 模块中的各种条件
from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.action_chains import ActionChains
import time
class Page(object):
    def setup(self):
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
    def teardown(self):
        self.driver.quit()
    def set_window_size(self, wide, high):
        self.driver.set_window_size(wide, high)
    def wait(self, sec):
        self.driver.implicitly_wait(sec)
    def sleep(self, sec):
        time.sleep(sec)
    def find_element(self, *element):
        by = element[0]
        value = element[1]
        if by == 'id':
            return self.driver.find_element_by_id(value)
        elif by == 'name':
            return self.driver.find_element_by_class_name(value)
        elif by == "class name":
            return self.driver.find_element_by_class_name(value)
        elif by == "link text":
            return self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css selector":
            return self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class name','link text','xpath','css selector'.")

    def wait_element(self, *element):
        sec = 5
        by = element[0]
        value = element[1]

        if by == 'id':
            #以下两个条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, ‘kw’)
            # 顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行
            # presence_of_element_located
            # presence_of_all_elements_located
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((MobileBy.ID, value)))
        elif by == "NAME":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((MobileBy.NAME, value)))
        elif by == "class name":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((MobileBy.CLASS_NAME, value)))
        elif by == "link text":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((MobileBy.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((MobileBy.XPATH, value)))
        elif by == "css selector":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((MobileBy.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class name','link text','xpath','css selector'.")

    def send_key(self, element, text):
        self.wait_element(*element)
        self.find_element(*element).clear()
        self.find_element(*element).send_keys(text)

    def click(self, element):
        self.wait_element(*element)
        self.find_element(*element).click()
    #
    # def right_click(self, element):
    #     self.wait_element(*element)
    #     ActionChains(self.driver).context_click(self.find_element(*element)).perform()
    #
    # def double_click(self, element):
    #     self.wait_element(*element)
    #     ActionChains(self.driver).double_click(self.find_element(*element)).perform()
    #
    # def move_to_element(self, element):
    #     self.wait_element(*element)
    #     ActionChains(self.driver).move_to_element(self.find_element(*element)).perform()
    #
    # def click_hold(self, element):
    #     self.wait_element(*element)
    #     ActionChains(self.driver).click_and_hold(self.find_element(*element)).perform()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def get_text(self, element):
        self.wait_element(*element)
        return self.find_element(*element).text

    def is_display(self, element):
        self.wait_element(*element)
        return self.find_element(*element).is_displayed()

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_screen_shot(self, file_path):
        time.sleep(2)
        self.driver.get_screenshot_as_file(file_path)

    def submit(self, element):
        self.wait_element(*element)
        self.find_element(*element).submit()

    def switch_to_frame(self, element):
        self.wait_element(*element)
        self.driver.switch_to.frame(self.find_element(*element))

    def switch_to_frame_out(self):
        self.driver.switch_to.default_content()

    def open_new_window(self, element):
        current_windows = self.driver.current_window_handle
        self.find_element(*element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)

    def refresh(self):
        self.driver.refresh()

    def js(self, script):
        self.driver.execute_script(script)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def get_cookies(self):
        self.driver.get_cookies()




# #encoding:utf-8
# # from appium import webdriver
# # from appium.webdriver.webdriver import WebDriverWait
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support import expected_conditions as ec
# # from selenium.webdriver.common.action_chains import ActionChains
# # import time
# # from src.common import MyExcepiton as M
# # class BaseAction(object):
# #     def __init__(self,driver):
# #         self.driver=driver
# #     def find_element(self,ele_type,value):
# #         ele=None
# #         try:
# #             if ele_type=="id":
# #                 WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_id(value))
# #                 ele=self.driver.find_element_by_id(value)
# #             elif ele_type=="name":
# #                 WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_name(value))
# #                 ele=self.driver.find_element_by_name(value)
# #             elif ele_type=="link_text":
# #                 WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_link_text(value))
# #                 ele=self.driver.find_element_by_link_text(value)
# #             elif ele_type=="tag_name":
# #                 WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_tag_name(value))
# #                 ele=self.driver.find_element_by_tag_name(value)
# #             elif ele_type=="xpath":
# #                 WebDriverWait(self.driver,15).until(lambda driver:driver.find_element_by_xpath(value))
# #                 ele=self.driver.find_element_by_xpath(value)
# #             else:
# #                 print "没有这种元素定位方式{}".format(ele_type)
# #         except M.NoSuchElementException,e:
# #             print e.message
# #         except M.TimeoutException,e:
# #             print e.message
# #         return  ele
# #
# #     def send_key(self, element, text):
# #         self.find_element(*element).clear()
# #         self.find_element(*element).send_keys(text)
# #
# #     def click(self, element):
# #         self.find_element(*element).click()
#
#
#
# #
# #     // 判断元素是否可见
# #     def findElement(self, mOperate):
# #         '''
# #         查找元素.mOperate是字典
# #         operate_type：对应的操作
# #         element_info：元素详情
# #         find_type: find类型
# #         '''
# #         try:
# #         WebDriverWait(self.cts, common.WAIT_TIME).until(lambda x: elements_by(mOperate, self.cts))
# #         return True
# #         except selenium.common.exceptions.TimeoutException:
# #             return False
# #     except selenium.common.exceptions.NoSuchElementException:
# #         print("找不到数据")
# #         return False
# #
# # // 操作之前，需要判断元素是否存在
# def operate_element(self,  mOperate):
# #     if self.findElement(mOperate):
# #         elements = {
# #             common.CLICK: lambda: operate_click(mOperate, self.cts),
# #             # common.TAP: lambda: operate_tap(mOperate["find_type"], self.cts,  mOperate["element_info"], arg),
# #             common.SEND_KEYS: lambda: send_keys(mOperate, self.cts),
# #             common.SWIPELEFT: lambda : opreate_swipe_left(mOperate, self.cts)
# #         }
# #         return elements[mOperate["operate_type"]]()
# #     return False
# #
# #
# # def isElement(self,identifyBy,c):
# #     '''
# #     Determine whether elements exist
# #     Usage:
# #     isElement(By.XPATH,"//a")
# #     '''
# #     flag=None
# #     try:
# #         if identifyBy == "id":
# #             #self.driver.implicitly_wait(60)
# #             self.driver.find_element_by_id(c)
# #         elif identifyBy == "xpath":
# #             #self.driver.implicitly_wait(60)
# #             self.driver.find_element_by_xpath(c)
# #         elif identifyBy == "class":
# #             self.driver.find_element_by_class_name(c)
# #         elif identifyBy == "link text":
# #             self.driver.find_element_by_link_text(c)
# #         elif identifyBy == "partial link text":
# #             self.driver.find_element_by_partial_link_text(c)
# #         elif identifyBy == "name":
# #             self.driver.find_element_by_name(c)
# #         elif identifyBy == "tag name":
# #             self.driver.find_element_by_tag_name(c)
# #         elif identifyBy == "css selector":
# #             self.driver.find_element_by_css_selector(c)
# #         flag = True
# #     except M.NoSuchElementException,e:
# #         flag = False
# #     finally:
# #         return flag
# #