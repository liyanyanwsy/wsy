# encoding:utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def find_toast(self,message):
    '''判断toast信息'''
    try:
        toast_loc = ("xpath", ".//*[contains(@text,message)]")
        #element = WebDriverWait(self,10,0.01).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,message)))
        element = WebDriverWait(self,10,0.1).until(EC.presence_of_element_located(toast_loc))
        print element

        return True
    except:
        return False







