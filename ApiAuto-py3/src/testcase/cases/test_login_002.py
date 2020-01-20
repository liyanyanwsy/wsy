#encoding:utf-8
import requests
import json
from src.common.excel_simple import ExcleHelper
import unittest
from src.common.logger import Log
cache={}
log=Log()
class Login(unittest.TestCase):
    # log=Log()
    @classmethod
    def setUpClass(cls):
        # cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto\config\test.xlsx','Sheet2')
        cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\test.xlsx','email')
    def setUp(self):
        # self.data=ExcleHelper()
        pass
    #test001-test004为登录信息，test005为电站列表信息，通用信息
    #邮箱账号登录
    def test_001(self):
        log.info("开始执行test_001")
        url=self.data.get_value('login_email','url')
        path=self.data.get_value('login_email','path')
        headers1=self.data.get_value('login_email','headers')
        method=self.data.get_value('login_email','method')
        base_params=self.data.get_value('login_email','params')
        #json.loads是将转化为json
        payload=json.loads(base_params)
        headers=json.loads(headers1)
        # print type(headers)
        print (url+path)
        if method=="get":
            response=requests.get(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            # print response.status_code
            result=json.loads(response.content)
            access_token=result['access_token']
            bearer=result['token_type']
            Authorization=access_token+" "+bearer
            return Authorization
        elif method=="post":
            response=requests.post(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            # print response.status_code
            result=json.loads(response.content)
            access_token=result['access_token']
            bearer=result['token_type']
            Authorization=bearer+" "+access_token
            cache['Authorization1']=Authorization
            # print cache
        log.info("test_001 pass")
    #获取商家列表
    def test_002(self):
        log.info("开始执行test_002")
        url=self.data.get_value('get_list002','url')
        path=self.data.get_value('get_list002','path')
        method=self.data.get_value('get_list002','method')
        base_params=self.data.get_value('get_list002','params')
        # Authorization=self.test_001()
        Authorization=cache['Authorization1']
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print (url+path)
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
        log.info("test_002 pass")
    #邮箱商家登录
    def test_003(self):
        log.info("开始执行test_003")
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
        print (url+path)
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
            cache['Authorization2']=Authorization
            return Authorization
        log.info("test_0013 pass")
    #获取用户信息
    def test_004(self):
        log.info("开始执行test_004")
        url=self.data.get_value('get_userinfo002','url')
        path=self.data.get_value('get_userinfo002','path')
        method=self.data.get_value('get_userinfo002','method')
        base_params=self.data.get_value('get_userinfo002','params')
        #Authorization=self.test_003()
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print(url+path)
        if method=="get":
            response=requests.get(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            roleid=result['orgUser']['roleId']
            cache['roleid']=roleid
        elif method=="post":
            response=requests.post(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
        log.info("test_004pass")
    #电站列表
    def test_user005(self):
        log.info("开始执行test_005")
        url=self.data.get_value('plant_list','url')
        path=self.data.get_value('plant_list','path')
        method=self.data.get_value('plant_list','method')
        #json格式
        base_params=self.data.get_value('plant_list','params')
        # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        print (url+path)
        if method=="get":
            response=requests.get(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_004 pass")
    #中文时区列表
    def test_user006(self):
        log.info("开始执行test_006")
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
        print (url+path)
        if method=="get":
            response=requests.get(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url+path,data=payload)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_006 pass")
    #中文货币列表
    def test_user007(self):
        log.info("开始执行test_007")
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
        print (url+path)
        if method=="get":
            response=requests.get(url=url+path,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url+path,data=payload)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print(result)
    #中文根据经纬度获取地理信息
    def test_user008(self):
        log.info("开始执行test_008")
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
        print (url+path)
        if method=="get":
            response=requests.get(url=url+path,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url+path,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_008 pass")
    def test_user009(self):
        log.info("开始执行test_009")

        log.info("test_008 pass")
    #创建电站
    def test_user010(self):
        log.info("开始执行test_0010")
        url=self.data.get_value('plant_create001','url')
        path=self.data.get_value('plant_create001','path')
        method=self.data.get_value('plant_create001','method')
        #json格式
        base_params=self.data.get_value('plant_create001','params')
        # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        print (url+path)
        print (cache)
        if method=="get":
            response=requests.get(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
    print (cache)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
