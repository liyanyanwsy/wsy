import unittest
import HTMLTestRunner
import time, os
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# ----------Path----------
def get_testcase_path():
    path_testcase = "C:\Users\lyy\Desktop\python\\IGEN"
    return path_testcase


def get_HTMLresult_path():
    get_HTMLresult = get_testcase_path() + "\\Results\\HTML_Report"
    return get_HTMLresult


def get_ResultsLog_path():
    get_ResultsLog = get_testcase_path()+"\\Results\\ResultsLog"
    return  get_ResultsLog


def get_ResultsLog_path_new():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    get_ResultsLog_new = get_ResultsLog_path() + "\\ResultsLog_" + now + ".txt"
    return get_ResultsLog_new


def get_FailedList_path():
    get_FailedList = get_testcase_path()+"\\Results\\FailedList"
    return get_FailedList


def get_FailedList_path_new():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    get_FailedList_new = get_FailedList_path() + "\\FailedList_" + now + ".txt"
    return get_FailedList_new


def get_screenshot_path():
    path_screenshot = get_testcase_path() + "\\Results\\Screenshot"
    return path_screenshot


def get_screenshot_path_new():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    path_screenshot_new = get_testcase_path() + "\\Results\\Screenshot_" + now
    return path_screenshot_new


def setup(self):
    print "TestCase " + self._testMethodName
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')

    prefs = {"": ""}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    options.add_experimental_option("prefs", prefs)
    self.driver = webdriver.Chrome(chrome_options=options)
    testcase_initialize(self.driver)


def teardown(self):
    End_do(self.driver, self._testMethodName)
    self.driver.quit()


# ----------Create TestSuit----------
def createtestsuit():
    tests_in_file = unittest.defaultTestLoader.discover(get_testcase_path() + "\\Tests", pattern='test*.py', top_level_dir=None)
    print tests_in_file
    return tests_in_file


# ----------HTMLTestRunner----------
def htmlreport_Run():
    alltests = createtestsuit()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    test_report_html = get_HTMLresult_path() + '\\' + now + '_Result.html'
    print(test_report_html)
    fp = file(test_report_html, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='IGEN', description='Detail', verbosity=2)
    runner.run(alltests)
    fp.close()


# ----------Run initialzation----------
def run_initialze():
    if not os.path.isdir(get_testcase_path() + "\\Results"):
        os.mkdir(get_testcase_path() + "\\Results")

    if not os.path.isdir(get_HTMLresult_path()):
        os.mkdir(get_HTMLresult_path())

    if not os.path.isdir(get_screenshot_path()):
        os.mkdir(get_screenshot_path())
    else:
        os.renames(get_screenshot_path(), get_screenshot_path_new())
        os.mkdir(get_screenshot_path())

    if not os.path.isdir(get_ResultsLog_path()):
        os.mkdir(get_ResultsLog_path())
    if os.path.exists(get_ResultsLog_path() + "\\ResultsLog.txt"):
        os.renames(get_ResultsLog_path() + "\\ResultsLog.txt", get_ResultsLog_path_new())

    if not os.path.isdir(get_FailedList_path()):
        os.mkdir(get_FailedList_path())
    if os.path.exists(get_FailedList_path() + "\\FailedList.txt"):
        os.renames(get_FailedList_path() + "\\FailedList.txt", get_FailedList_path_new())


# ----------Testcase initialzation----------
def testcase_initialize(driver):
    driver.maximize_window()
    driver.get('http://pro.solarman.cn/login/login.do')
    # driver.get('https://www.baidu.com')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="guideReg"]/div/button').click()
    time.sleep(1)


# ----------Testcase End ----------
def End_do(driver, testcasename):
    log(testcasename)
    driver.get_screenshot_as_file(get_screenshot_path() + '\\' + testcasename + '.png')
    time.sleep(2)
    if sys.exc_info()[0]:
        failedlist(testcasename)
        time.sleep(2)
    else:
        open(get_FailedList_path() + "\\FailedList.txt", "a")
        # os.mknod(get_FailedList_path() + "\\FailedList.txt")


def log(testcasename):
    fo = open(get_ResultsLog_path() + "\\ResultsLog.txt", "a")
    fo.writelines("Testcase: " + testcasename + "\n")
    fo.writelines(str(sys.exc_info()) + "\n")
    fo.writelines("Save screenshot to " + get_screenshot_path() + '\\' + testcasename + '.png' + "\n\n")
    time.sleep(2)
    fo.close()


def failedlist(testcasename):
    fo = open(get_FailedList_path() + "\\FailedList.txt", "a")
    fo.writelines(testcasename + "\n")
    time.sleep(2)
    fo.close()


