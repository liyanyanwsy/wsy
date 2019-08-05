# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time


class Page(object):

    def __init__(self, browser='Chrome'):
        if browser == 'Chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('disable-infobars')
            self.driver = webdriver.Chrome(chrome_options=options)
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Ie':
            self.driver = webdriver.Ie()
        else:
            raise NameError("Please enter 'Chrome', 'Firefox', 'Ie'.")

    def open_url(self, url):
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    def close_browser(self):
        self.driver.close()

    def max_window(self):
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        self.driver.set_window_size(wide, high)

    def wait(self, sec):
        self.driver.implicitly_wait(sec)

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
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.NAME, value)))
        elif by == "class name":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link text":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.XPATH, value)))
        elif by == "css selector":
            WebDriverWait(self.driver, sec, 1).until(ec.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class name','link text','xpath','css selector'.")

    def send_key(self, element, text):
        self.wait_element(*element)
        self.find_element(*element).clear()
        self.find_element(*element).send_keys(text)

    def click(self, element):
        self.wait_element(*element)
        self.find_element(*element).click()

    def right_click(self, element):
        self.wait_element(*element)
        ActionChains(self.driver).context_click(self.find_element(*element)).perform()

    def double_click(self, element):
        self.wait_element(*element)
        ActionChains(self.driver).double_click(self.find_element(*element)).perform()

    def move_to_element(self, element):
        self.wait_element(*element)
        ActionChains(self.driver).move_to_element(self.find_element(*element)).perform()

    def click_hold(self, element):
        self.wait_element(*element)
        ActionChains(self.driver).click_and_hold(self.find_element(*element)).perform()

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
