import unittest
import time
from Functions import Function
from selenium.webdriver.common.action_chains import ActionChains


class test_Login(unittest.TestCase):

    def setUp(self):
        Function.setup(self)

    def tearDown(self):
        Function.teardown(self)

    # def test_LoginPwWrong(self):
    #     self.driver.find_element_by_id('userName').send_keys('15006173014')
    #     time.sleep(1)
    #     self.driver.find_element_by_id('password').send_keys('123')
    #     time.sleep(1)
    #     self.driver.find_element_by_id('login').click()
    #     time.sleep(10)
    #     url = self.driver.current_url
    #     self.assertEqual(url,'http://pro.solarman.cn/index/setIndex.do')

    def test_Login(self):
        self.driver.find_element_by_id('userName').send_keys('15006173014')
        time.sleep(1)
        self.driver.find_element_by_id('password').send_keys('123456')
        time.sleep(1)
        self.driver.find_element_by_id('login').click()
        self.driver.implicitly_wait(60)
        # self.driver.find_element_by_xpath('/html/body/section/div[2]/div[2]/a')

        # self.driver.switch_to.frame('mainIframe')
        self.driver.switch_to.frame(self.driver.find_element_by_id('mainIframe'))
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="guideNewPlant"]/div/button').click()
        time.sleep(1)
        target = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]')
        target_hidden = self.driver.find_element_by_xpath('//*[@id="mCSB_2_container"]/div/button[2]')
        ActionChains(self.driver).move_to_element(target).click(target_hidden).perform()
        # self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]').click()
        # time.sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="mCSB_2_container"]/div/button[2]').click()
        time.sleep(2)
        self.driver.switch_to_default_content()
        url = self.driver.current_url
        self.assertEqual(url, 'http://pro.solarman.cn/index/setIndex.do')
unittest.main()



