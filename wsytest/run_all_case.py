
#coding:utf-8
import unittest
import HTMLTestRunner
# 待执行用例的目录
report_path="D:\\Program Files\\Git\\11\\wsytest\\report\\html"
def all_case():
    case_dir="D:\\Program Files\\Git\\11\\wsytest\\case1"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    testcase.addTests(discover)
    # #discover方法筛选出来的用例，并循环添加到测试套件中
    # for test_suit in discover:
    #     for test_case in test_suit:
    #         # 添加用例到 testcase
    #         testcase.addTest(test_case)
    print (testcase)
    return testcase
if __name__ == '__main__':
    #runner=unittest.TextTestRunner()
    report_path="D:\\Program Files\\Git\\11\\wsytest\\report\\result.html"
    fp=open(report_path,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"这是我的自动化测试报告",description=u"用例执行情况")
    runner.run(all_case())
    fp.close()