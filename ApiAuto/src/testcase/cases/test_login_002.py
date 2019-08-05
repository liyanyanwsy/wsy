#encoding:utf-8
import requests
import json
from src.common.excel_simple import ExcleHelper
import unittest
from src.common.logger import Log
cache={}

class Login(unittest.TestCase):
    # log=Log()
    @classmethod
    def setUpClass(cls):
        # cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto\config\test.xlsx','Sheet2')
        cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto\config\test.xlsx','email')
    def setUp(self):
        # self.data=ExcleHelper()
        pass
    #test001-test004为登录信息，test005
    #邮箱账号登录开始为通用信息
    def test_001(self):
        url=self.data.get_value('login_email','url')
        path=self.data.get_value('login_email','path')
        headers1=self.data.get_value('login_email','headers')
        method=self.data.get_value('login_email','method')
        base_params=self.data.get_value('login_email','params')
        #json.loads是将转化为json
        payload=json.loads(base_params)
        headers=json.loads(headers1)
        # print type(headers)
        print url+path
        if method=="get":
            response=requests.get(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            # print response.status_code
            result=json.loads(response.content)
            access_token=result['access_token']
            bearer=result['token_type']
            Authorization=access_token+" "+bearer
            print 'token001为%s'%Authorization
            return Authorization
        elif method=="post":
            response=requests.post(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            # print response.status_code
            result=json.loads(response.content)
            access_token=result['access_token']
            bearer=result['token_type']
            Authorization=bearer+" "+access_token
            print 'token001为%s'%Authorization
            cache['Authorization1']=Authorization
            # print cache
        print 'pass'
    #获取商家列表
    def test_002(self):
        url=self.data.get_value('get_list002','url')
        path=self.data.get_value('get_list002','path')
        method=self.data.get_value('get_list002','method')
        base_params=self.data.get_value('get_list002','params')
        # Authorization=self.test_001()
        Authorization=cache['Authorization1']
        print 'token002为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print url+path
        if method=="get":
            response=requests.get(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            # print type(result)
            rog_id=result[0]['org']['id']
            cache['rog_id']=rog_id
            return rog_id
            # self.assertEqual(result[''],200,msg='返回值不是200')
        # print result
        elif method=="post":
            response=requests.post(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
        print '002ok'
    #邮箱商家登录
    def test_003(self):
        url=self.data.get_value('login_email002','url')
        path=self.data.get_value('login_email002','path')
        headers1=self.data.get_value('login_email002','headers')
        method=self.data.get_value('login_email002','method')
        base_params=self.data.get_value('login_email002','params')
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
        print url+path
        if method=="get":
            response=requests.get(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
        elif method=="post":
            response=requests.post(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            access_token=result['access_token']
            bearer=result['token_type']
            Authorization=bearer+" "+access_token
            print 'token003为%s'%Authorization
            cache['Authorization2']=Authorization
            print cache
            return Authorization
        print '003ok'
    #获取用户信息
    def test_004(self):
        url=self.data.get_value('get_userinfo002','url')
        path=self.data.get_value('get_userinfo002','path')
        method=self.data.get_value('get_userinfo002','method')
        base_params=self.data.get_value('get_userinfo002','params')
        #Authorization=self.test_003()
        Authorization=cache['Authorization2']
        print 'token004为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print url+path
        if method=="get":
            response=requests.get(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print type(result)
            print "用户信息为%s"%result
            roleid=result['orgUser']['roleId']
            cache['roleid']=roleid
        elif method=="post":
            response=requests.post(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
        print '004ok'
    #电站列表
    def test_user005(self):
        print "开始执行test005"
        url=self.data.get_value('plant_list','url')
        path=self.data.get_value('plant_list','path')
        method=self.data.get_value('plant_list','method')
        #json格式
        base_params=self.data.get_value('plant_list','params')
        # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token004为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        print url+path
        if method=="get":
            response=requests.get(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #中文时区列表
    def test_user006(self):
        print "开始执行test006"
        url=self.data.get_value('timezonelist','url')
        path=self.data.get_value('timezonelist','path')
        method=self.data.get_value('timezonelist','method')
        #json格式
        base_params=self.data.get_value('timezonelist','params')
        # print base_params
        # print type(base_params)
        payload=json.loads(base_params)
        # print payload
        # print type(payload)
        # Authorization=cache['Authorization2']
        # print 'token004为%s'%Authorization
        headers={"User-agent":"okhttp/3.9.1"}
        print url+path
        if method=="get":
            response=requests.get(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url+path,data=payload)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #中文货币列表
    def test_user007(self):
        print "开始执行test007"
        url=self.data.get_value('currencylist','url')
        path=self.data.get_value('currencylist','path')
        method=self.data.get_value('currencylist','method')
        #json格式
        base_params=self.data.get_value('currencylist','params')
        # print base_params
        # print type(base_params)
        payload=json.loads(base_params)
        # print payload
        # print type(payload)
        # Authorization=cache['Authorization2']
        # print 'token004为%s'%Authorization
        headers={"User-agent":"okhttp/3.9.1"}
        print url+path
        if method=="get":
            response=requests.get(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url+path,data=payload)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #中文根据经纬度获取地理信息
    def test_user008(self):
        print "开始执行test008"
        url=self.data.get_value('AreaDetails','url')
        path=self.data.get_value('AreaDetails','path')
        method=self.data.get_value('AreaDetails','method')
        #json格式
        base_params=self.data.get_value('AreaDetails','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        # print 'token004为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print url+path
        if method=="get":
            response=requests.get(url=url+path,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url+path,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #创建电站
    def test_user010(self):
        print "开始执行test010"
        url=self.data.get_value('plant_create001','url')
        path=self.data.get_value('plant_create001','path')
        method=self.data.get_value('plant_create001','method')
        #json格式
        base_params=self.data.get_value('plant_create001','params')
        # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token004为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        print url+path
        if method=="get":
            response=requests.get(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
