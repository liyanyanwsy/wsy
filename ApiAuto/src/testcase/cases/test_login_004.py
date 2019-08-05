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
        cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto\config\test.xlsx','username2')
    def setUp(self):
        # self.data=ExcleHelper()
        pass
    #test001-test004为用户名登录信息，test005-test015为电站信息
    #用户名账号登录
    def test001(self):
        url=self.data.get_value('login_username','url')
        path=self.data.get_value('login_username','path')
        headers1=self.data.get_value('login_username','headers')
        method=self.data.get_value('login_username','method')
        base_params=self.data.get_value('login_username','params')
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
    #获取商家列表
    def test002(self):
        url=self.data.get_value('get_list003','url')
        path=self.data.get_value('get_list003','path')
        method=self.data.get_value('get_list003','method')
        base_params=self.data.get_value('get_list003','params')
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
    #用户名商家登录
    def test003(self):
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
    def test004(self):
        url=self.data.get_value('get_userinfo003','url')
        path=self.data.get_value('get_userinfo003','path')
        method=self.data.get_value('get_userinfo003','method')
        base_params=self.data.get_value('get_userinfo003','params')
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
    def test005(self):
        print "开始执行test005"
        url=self.data.get_value('plant_list','url')
        path=self.data.get_value('plant_list','path')
        method=self.data.get_value('plant_list','method')
        #json格式
        base_params=self.data.get_value('plant_list','params')
        print type(base_params)
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
            inverter_id=result['data'][1]['id']
            meter_id=result['data'][2]['id']
            cache['inverter_id']=inverter_id
            cache['meter_id']=meter_id
        elif method=="post":
            response=requests.post(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
            inverter_id=result['data'][1]['id']
            meter_id=result['data'][2]['id']
            cache['inverter_id']=inverter_id
            cache['meter_id']=meter_id
    #关于电站
    def test006(self):
        print "开始执行test006"
        url=self.data.get_value('plant_detail','url')
        path=self.data.get_value('plant_detail','path')
        path2=self.data.get_value('plant_detail','path2')
        method=self.data.get_value('plant_detail','method')
        # #json格式
        # base_params=self.data.get_value('plant_detail','params')
        # # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print url
        if method=="get":
            response=requests.get(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #电站系统概要
    def test007(self):
        print "开始执行test007"
        url=self.data.get_value('plant_summary','url')
        path=self.data.get_value('plant_summary','path')
        path2=self.data.get_value('plant_summary','path2')
        method=self.data.get_value('plant_summary','method')
        # #json格式
        # base_params=self.data.get_value('plant_detail','params')
        # # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print url
        if method=="get":
            response=requests.get(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #电站实时数据
    def test008(self):
        print "开始执行test008"
        url=self.data.get_value('plant_realtime','url')
        path=self.data.get_value('plant_realtime','path')
        method=self.data.get_value('plant_realtime','method')
        # #json格式
        # base_params=self.data.get_value('plant_detail','params')
        # # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d')%id
        print url
        if method=="get":
            response=requests.get(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #电站基本信息
    def test009(self):
        print "开始执行test009"
        url=self.data.get_value('plant_info','url')
        path=self.data.get_value('plant_info','path')
        method=self.data.get_value('plant_info','method')
        # #json格式
        # base_params=self.data.get_value('plant_detail','params')
        # # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d')%id
        print url
        if method=="get":
            response=requests.get(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #电站关注,返回不是json，不需要json.loads
    def test010(self):
        print "开始执行test010"
        url=self.data.get_value('plant_follow','url')
        path=self.data.get_value('plant_follow','path')
        method=self.data.get_value('plant_follow','method')
        Authorization=cache['Authorization2']
        print 'token004为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        payload=[]
        payload.append(id)
        payload1=json.dumps(payload)
        # print payload1
        # print type(payload1)
        if method=="get":
            response=requests.get(url=url+path,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=response.content
            print result
        elif method=="post":
            response=requests.post(url=url+path,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=response.content
            print result
    #电站关注取消
    def test011(self):
        print "开始执行test011"
        url=self.data.get_value('plant_cfollow','url')
        path=self.data.get_value('plant_cfollow','path')
        method=self.data.get_value('plant_cfollow','method')
        Authorization=cache['Authorization2']
        print 'token004为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        payload=[]
        payload.append(id)
        payload1=json.dumps(payload)
        if method=="get":
            response=requests.get(url=url+path,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=response.content
            print result
        elif method=="delete":
            response=requests.delete(url=url+path,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=response.content
            print result
    #获取电站发电历史日图表
    def test012(self):
        print "开始执行test012"
        url=self.data.get_value('plant_day','url')
        path=self.data.get_value('plant_day','path')
        path2=self.data.get_value('plant_day','path2')
        method=self.data.get_value('plant_day','method')
        #json格式
        base_params=self.data.get_value('plant_day','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['meter_id']
        url=(url+path+'%d'+path2)%id
        print url
        if method=="get":
            response=requests.get(url=url,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #获取电站发电历史月图表
    def test013(self):
        print "开始执行test013"
        url=self.data.get_value('plant_month','url')
        path=self.data.get_value('plant_month','path')
        path2=self.data.get_value('plant_month','path2')
        method=self.data.get_value('plant_month','method')
        #json格式
        base_params=self.data.get_value('plant_month','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['meter_id']
        url=(url+path+'%d'+path2)%id
        print url
        if method=="get":
            response=requests.get(url=url,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #获取电站发电历史年图表
    def test014(self):
        print "开始执行test014"
        url=self.data.get_value('plant_year','url')
        path=self.data.get_value('plant_year','path')
        path2=self.data.get_value('plant_year','path2')
        method=self.data.get_value('plant_year','method')
        #json格式
        base_params=self.data.get_value('plant_year','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['meter_id']
        url=(url+path+'%d'+path2)%id
        print url
        if method=="get":
            response=requests.get(url=url,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #获取电站发电历史z总图表
    def test015(self):
        print "开始执行test015"
        url=self.data.get_value('plant_total','url')
        path=self.data.get_value('plant_total','path')
        path2=self.data.get_value('plant_total','path2')
        method=self.data.get_value('plant_total','method')
        #json格式
        base_params=self.data.get_value('plant_total','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['meter_id']
        url=(url+path+'%d'+path2)%id
        print url
        if method=="get":
            response=requests.get(url=url,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url,params=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
    #电站报警
    def test016(self):
        log.info("开始执行test016")
        url=self.data.get_value('plant_alert','url')
        path=self.data.get_value('plant_alert','path')
        method=self.data.get_value('plant_alert','method')
        #json格式
        base_params=self.data.get_value('plant_alert','params')
        payload=json.loads(base_params)
        plant_id=cache['inverter_id']
        payload['plantId']='%d'%plant_id
        payload1=json.dumps(payload)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        if method=="get":
            response=requests.get(url=url+path,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url+path,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        log.info("test016 pass")

if __name__ == '__main__':
    unittest.main()
