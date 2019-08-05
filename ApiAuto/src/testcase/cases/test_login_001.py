#encoding:utf-8
import requests
import json
from src.common.excel_simple import ExcleHelper
import unittest
from src.common.logger import Log
cache={}
log=Log()
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto\config\test.xlsx','Sheet2')
        cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto\config\test.xlsx','phone')
    def setUp(self):
        # self.data=ExcleHelper()
        pass
    #test001-test004为登录信息，test005为账号权限，test006-test012为运维信息
    #手机账号登录
    def test_001(self):
        log.info("开始执行test_001")
        url=self.data.get_value('login_mobile','url')
        path=self.data.get_value('login_mobile','path')
        headers1=self.data.get_value('login_mobile','headers')
        method=self.data.get_value('login_mobile','method')
        base_params=self.data.get_value('login_mobile','params')
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
        log.info("test_001 pass")
    #获取商家列表
    def test_002(self):
        log.info("开始执行test_002")
        url=self.data.get_value('get_list','url')
        path=self.data.get_value('get_list','path')
        method=self.data.get_value('get_list','method')
        base_params=self.data.get_value('get_list','params')
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
        log.info("test_002 pass")
    #手机商家登录
    def test_003(self):
        log.info("开始执行test_003")
        url=self.data.get_value('login_mobile002','url')
        path=self.data.get_value('login_mobile002','path')
        headers1=self.data.get_value('login_mobile002','headers')
        method=self.data.get_value('login_mobile002','method')
        base_params=self.data.get_value('login_mobile002','params')
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
        log.info("test_003 pass")
    #获取用户信息
    def test_004(self):
        log.info("开始执行test_004")
        url=self.data.get_value('get_userinfo','url')
        path=self.data.get_value('get_userinfo','path')
        method=self.data.get_value('get_userinfo','method')
        base_params=self.data.get_value('get_userinfo','params')
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
        log.info("test_004 pass")
    #登录账号的权限
    def test_005(self):
        log.info("开始执行test_005")
        url=self.data.get_value('accout_role','url')
        path=self.data.get_value('accout_role','path')
        method=self.data.get_value('accout_role','method')
        base_params=self.data.get_value('accout_role','params')
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        roleid=cache['roleid']
        # print roleid
        url=(url+path+'%d') %roleid
        # print url
        if method=="get":
            response=requests.get(url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
        log.info("test_005 pass")
    #获取账号下电站状态统计信息
    def test_006(self):
        log.info("开始执行test_006")
        url=self.data.get_value('plant_status','url')
        path=self.data.get_value('plant_status','path')
        method=self.data.get_value('plant_status','method')
        #json格式
        base_params=self.data.get_value('plant_status','params')
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
        log.info("test_006 pass")
    #获取账号下电站发电情况统计信息
    def test_007(self):
        log.info("开始执行test_007")
        url=self.data.get_value('generation_summary','url')
        path=self.data.get_value('generation_summary','path')
        method=self.data.get_value('generation_summary','method')
        #json格式
        base_params=self.data.get_value('generation_summary','params')
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
        log.info("test_007 pass")
    #获取我的关注电站列表
    def test_008(self):
        log.info("开始执行test_008")
        url=self.data.get_value('mywatchlist','url')
        path=self.data.get_value('mywatchlist','path')
        method=self.data.get_value('mywatchlist','method')
        #json格式
        base_params=self.data.get_value('mywatchlist','params')
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
        log.info("test_008 pass")
    #获取账号下昨日满发小时排名电站列表
    def test_009(self):
        log.info("开始执行test_009")
        url=self.data.get_value('rank001','url')
        path=self.data.get_value('rank001','path')
        method=self.data.get_value('rank001','method')
        #json格式
        base_params=self.data.get_value('rank001','params')
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
        log.info("test_009 pass")
    #获取账号下整体发电月图表
    def test_010(self):
        log.info("开始执行test_010")
        url=self.data.get_value('view_month','url')
        path=self.data.get_value('view_month','path')
        method=self.data.get_value('view_month','method')
        #json格式
        base_params=self.data.get_value('view_month','params')
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
        log.info("test_010 pass")
    #获取账号下整体发电年图表
    def test_011(self):
        log.info("开始执行test_011")
        url=self.data.get_value('view_year','url')
        path=self.data.get_value('view_year','path')
        method=self.data.get_value('view_year','method')
        #json格式
        base_params=self.data.get_value('view_year','params')
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
        log.info("test_011 pass")
    #报警列表
    def test_012(self):
        log.info("开始执行test_12")
        url=self.data.get_value('alert','url')
        path=self.data.get_value('alert','path')
        method=self.data.get_value('alert','method')
        #json格式
        base_params=self.data.get_value('alert','params')
        # payload=json.loads(base_params)
        # plant_id=cache['inverter_id']
        # payload['plantId']='%d'%plant_id
        # payload1=json.dumps(payload)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
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
        log.info("test_12 pass")

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
