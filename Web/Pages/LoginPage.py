# -*- coding:utf-8 -*-

from Pages.BasePage import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    guide = (By.XPATH, u'//*[@id="guideReg"]/div/button')
    login_username = (By.XPATH, u'//*[@id="userName"]')
    login_password = (By.XPATH, u'//*[@id="password"]')
    login_btn = (By.XPATH, u'//*[@id="login"]')

    def guide_close(self):
        self.click(self.guide)

    def input_username(self, username):
        self.send_key(self.login_username, username)

    def input_password(self, password):
        self.send_key(self.login_password, password)

    def click_login_btn(self):
        self.click(self.login_btn)

    def get_cookies(self):
        self.get_cookies()

