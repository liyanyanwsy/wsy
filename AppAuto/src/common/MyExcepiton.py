#encoding:utf-8
#自定义异常 需要继承Exception
class MyException(Exception):
    def __init__(self, *args):
        self.args = args

#常见做法定义异常基类,然后在派生不同类型的异常

class NoSuchElementException(MyException):
    def __init__(self,message = '无元素异常', args = ('无元素异常',)):
        self.args = args
        self.message = message

class TimeoutException(MyException):
    def __init__(self):
        self.args = ('超时异常',)
        self.message = '超时异常'


class NoSectionError(MyException):
    def __init__(self):
        self.args = ('无section错误',)
        self.message = '无section错误'


class NoOptionError(MyException):
    def __init__(self):
        self.args = ('无option错误',)
        self.message = '无option错误'