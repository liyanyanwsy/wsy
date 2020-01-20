#encoding:utf-8
import requests,json
from  src.common.excel_simple import ExcleHelper
import unittest
from src.common.logger import Log
from src.common.settings import Login
cache=Login()
print (cache)
log=Log()
# class Tag(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\test.xlsx','tag')
#     def setUp(self):
#         pass
#     def test_tag001(self):
#         log.info("开始执行test_tag001")
#         url=self.data.get_value('tag_list','url')
#         path=self.data.get_value('tag_list','path')
#         path2=self.data.get_value('tag_list','path2')
#         Authorization=cache['Authorization2']
#



