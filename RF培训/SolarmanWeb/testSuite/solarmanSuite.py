__author__ = 'tianya'

from robot.api import TestSuite


class SolarmanSuite:
    def __init__(self, name):
        # 创建TestSuite
        self.testSuite = TestSuite(name)

    def setup(self, url, browser='chrome', librarys=["SeleniumLibrary"]):
        for lib in librarys:
            self.testSuite.resource.imports.library(lib)
        tc = self.testSuite.tests.create("setup")
        tc.keywords.create("Open Browser", args=[url, browser])

    def teardown(self):
        tc = self.testSuite.tests.create("teardown")
        tc.keywords.create("Close All Browsers")

    def getTestSuite(self):
        return self.testSuite
