#encoding:utf-8
import requests,json
from src.common.excel_simple import ExcleHelper
cache={}
class setting():
    def value(sheetname,api_name):
        data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\test.xlsx',sheetname)
        url=data.get_value(api_name,'url')
        path=data.get_value(api_name,'path')
        headers1=data.get_value(api_name,'headers')
        method=data.get_value(api_name,'method')
        base_params=data.get_value(api_name,'params')
        cache['url']=url
        cache['path']=path
        cache['headers1']=headers1
        cache['method']=method
        cache['base-params']=base_params
        return cache


a=setting.value('new','business_info')
print (a)