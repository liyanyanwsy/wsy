# encoding:utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def find_toast(self,message):
    try:
        message = '//*[@text=\'{}\']'.format(message)
        element = WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, message)))
        return element.get_attribute('text')
    except selenium.common.exceptions.TimeoutException:
        print('Time Out')
    except selenium.common.exceptions.NoSuchElementException:
        print('NoSuchElement')