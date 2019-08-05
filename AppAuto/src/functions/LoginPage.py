# -*- coding:utf-8 -*-
from BaseAction import Page
from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.common.by import By
page=Page()
class LoginPage(object):
    id=MobileBy.ID
    login_btn1 = (id, 'com.igen.rrgf:id/tvLogin')
    print login_btn1
    print type(login_btn1)
    login_username = (id, 'com.igen.rrgf:id/et_1')
    login_password = (id, 'com.igen.rrgf:id/et_2')
    login_btn2 = (id, 'com.igen.rrgf:id/btn_1')
    #注册相关
    register_btn1 = (id, 'com.igen.rrgf:id/tvRegister')
    # nickname=
    # mobile/email=
    # password
    #
    def click_login_btn1(self):
        page.click(self.login_btn1)
        # self.click(self.login_btn1)
    def input_username(self, username):
        page.send_key(self.login_username, username)
    def input_password(self, password):
        page.send_key(self.login_password, password)
    def click_login_btn2(self):
        page.click(self.login_btn2)
#
# LoginPage().click_login_btn1()
