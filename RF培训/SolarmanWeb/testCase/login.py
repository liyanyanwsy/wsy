__author__ = 'tianya'


class Login:
    def __init__(self, testSuite):
        self.tc = testSuite.tests.create("登录", tags=['smoking', 'high'])
        testSuite.resource.variables.create('${count}', '5')

    def login(self, username, password):
        self.tc.keywords.create("Wait Until Page Contains Element", args=["name=username"])
        self.tc.keywords.create("Input Text", args=["name=username", username])

        self.tc.keywords.create("Wait Until Page Contains Element", args=["name=password"])
        self.tc.keywords.create("Input Password", args=["name=password", password])

        self.tc.keywords.create("Wait Until Page Contains Element", args=["id=login"])
        self.tc.keywords.create("Click Element", args=["id=login"])
        self.tc.keywords.create("Sleep", args=["3"])
        # self.tc.keywords.create("Set Variable", args=["${count}", 5])
        self.tc.keywords.create("Log To Console", args=["${count}"])
        self.tc.keywords.create("Get Element Count", args=["xpath=//div[@id='alert' and @status='true']"], assign=['${count}'])

        self.tc.keywords.create("Log To Console", args=["${count}"])

        #self.tc.keywords.create("Run Keyword If", args=["${count} == 1", "Run Keywords", "Click Button", "xpath=//button[text()='我知道了'"])
        #self.tc.keywords.create("Click Button", args=["xpath=//button[text()='我知道了'"])





