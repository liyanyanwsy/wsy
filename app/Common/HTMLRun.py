# -*- coding:utf-8 -*-

import time
from Common import HTMLTestRunner
from Common import Testsuit
import logging


#html_path = "C:\\Users\\IGEN\\Desktop\\Mytest\\Web\\Report"
html_path = "D:\\Program Files\\Git\\11\\app\\Report"

def html_run():
    logger = logging.getLogger("Mylogger.htmlrun")
    all_tests = Testsuit.test_suit()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    test_report_html = html_path + '\\' + now + '_Result.html'
    logger.info("Save HTML Report to: " + test_report_html)
    fp = file(test_report_html, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='IGEN', description='Detail', verbosity=2)
    runner.run(all_tests)
    fp.close()
