__author__ = 'tianya'

from testSuite.solarmanSuite import SolarmanSuite
from testCase.login import Login
from robot.api import ResultWriter

if __name__ == "__main__":
    suite = SolarmanSuite("solarman")
    suite.setup('http://10.42.3.10/login')
    testSuite = suite.getTestSuite()
    tc = Login(testSuite)
    listUser = ['',  '9~!@#$%^&*()_+0', 'invalidUser@invalid.com', '18896723689']
    listPsw = ['123456', '9~!@#$%^&*()_+0', '', '123456']
    for i in range(len(listUser)):
        tc.login(listUser[i], listPsw[i])

    suite.teardown()
    # 运行套件
    result = testSuite.run(critical="solarman",
                                output="output.xml")

    # 生成日志、报告文件
    ResultWriter(result).write_results(
            report="report.html", log="log.html")

