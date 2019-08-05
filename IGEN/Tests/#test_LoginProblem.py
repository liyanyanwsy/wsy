import time
import unittest

import actions
from Functions import Function


class test_LoginProblem(unittest.TestCase):

    def setUp(self):
        Function.setup(self)

    def tearDown(self):
        Function.teardown(self)

    def test_LoginProblem(self):
        # self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/div[3]/a').click()
        self.driver.find_element_by_xpath(actions.loginproblembtn).click()
        time.sleep(10)
        url = self.driver.current_url
        print url
        self.assertEqual(url, 'http://pro.solarman.cn/login/goRePassword1.do')

