
#encoding:utf-8
import requests,json
from src.common.excel_simple import ExcleHelper

cache={}
class Login():
    data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\test.xlsx','username')
    #用户名账号登录
    def test_tag001(self):
        url=self.data.get_value('login_username','url')
        path=self.data.get_value('login_username','path')
        headers1=self.data.get_value('login_username','headers')
        base_params=self.data.get_value('login_username','params')
        #json.loads是将转化为json
        payload=json.loads(base_params)
        headers=json.loads(headers1)
        # print type(headers)
        # print (url+path)
        response=requests.post(url=url+path,data=payload,headers=headers)
        result=json.loads(response.content)
        access_token=result['access_token']
        bearer=result['token_type']
        Authorization=bearer+" "+access_token
        cache['Authorization1']=Authorization
    #获取商家列表
    def test_tag002(self):
        url=self.data.get_value('get_list003','url')
        path=self.data.get_value('get_list003','path')
        method=self.data.get_value('get_list003','method')
        base_params=self.data.get_value('get_list003','params')
        Authorization=cache['Authorization1']
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print (url+path)
        response=requests.get(url=url+path,headers=headers)
        result=json.loads(response.content)
        # print type(result)
        rog_id=result[0]['org']['id']
        cache['rog_id']=rog_id
    #用户名商家登录
    def test_user003(self):
        url=self.data.get_value('login_username002','url')
        path=self.data.get_value('login_username002','path')
        headers1=self.data.get_value('login_username002','headers')
        method=self.data.get_value('login_username002','method')
        base_params=self.data.get_value('login_username002','params')
        #json.loads是将转化为json
        payload=json.loads(base_params)
        #org_id=self.test_002()
        org_id=cache['rog_id']
        # print org_id
        headers=json.loads(headers1)
        # data={'org_id':'%d' %org_id}
        payload['org_id']=org_id
        # print payload
        # print type(payload)
        print (url+path)
        response=requests.post(url=url+path,data=payload,headers=headers)
        result=json.loads(response.content)
        access_token=result['access_token']
        bearer=result['token_type']
        Authorization=bearer+" "+access_token
        cache['Authorization2']=Authorization
        return cache


    #
# def send_params(self,api_name,payload):
#     url=self.data.get_value('api_name','url')
#     path=self.data.get_value('api_name','path')
#     headers1=self.data.get_value('api_name','headers')
#     method=self.data.get_value('api_name','method')
#     base_params=self.data.get_value('api_name','params')
#
#
# def send_data(self,api_name,payload):
#     url=self.data.get_value('api_name','url')
#     path=self.data.get_value('api_name','path')
#     headers1=self.data.get_value('api_name','headers')
#     method=self.data.get_value('api_name','method')
#     base_params=self.data.get_value('api_name','params')





