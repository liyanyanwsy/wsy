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
        cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto\config\test.xlsx','username3')
    def setUp(self):
        # self.data=ExcleHelper()
        pass
    #test001-test004为用户名登录信息，test005-test015为设备信息
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
    #电站列表,选择all on grid,self-consumption,第二个和第三个电站
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
    #获取电站下逆变器列表,取逆变器的id和systemid
    def test006(self):
        print "开始执行test006"
        url=self.data.get_value('inverter_list','url')
        path=self.data.get_value('inverter_list','path')
        path2=self.data.get_value('inverter_list','path2')
        method=self.data.get_value('inverter_list','method')
        #json格式
        base_params=self.data.get_value('inverter_list','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print url
        if method=="get":
            response=requests.get(url=url,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
            deviceId=result['data'][0]['id']
            siteId=result['data'][0]['systemId']
            cache['deviceId']=deviceId
            cache['siteId']=siteId
        elif method=="post":
            response=requests.post(url=url,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
            deviceId=result['data'][0]['id']
            siteId=result['data'][0]['systemId']
            cache['deviceId']=deviceId
            cache['siteId']=siteId
    #设备详情，传的参数中有变量，先转化为字典，增加字典，然后字典再转化为json,返回中取产品id
    def test007(self):
        print "开始执行test007"
        url=self.data.get_value('device_detail','url')
        path=self.data.get_value('device_detail','path')
        method=self.data.get_value('device_detail','method')
        #json格式
        base_params=self.data.get_value('device_detail','params')
        payload=json.loads(base_params)
        deviceId=cache['deviceId']
        siteId=cache['siteId']
        payload['deviceId']='%s'%deviceId
        payload['siteId']='%s'%siteId
        payload1=json.dumps(payload)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        if method=="get":
            response=requests.get(url=url+path,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
            productId=result['productId']
            cache['productId']=productId
        elif method=="post":
            response=requests.post(url=url+path,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
            productId=result['productId']
            cache['productId']=productId
            print productId
    #历史图表参数显示,目前python2不支持中文显示，
    # 后期用python3
    def test008(self):
        print "开始执行test008"
        url=self.data.get_value('params','url')
        path=self.data.get_value('params','path')
        method=self.data.get_value('params','method')
        #json格式
        base_params=self.data.get_value('params','params')
        payload=json.loads(base_params)
        productId=cache['productId']
        payload['productId']='%s'%productId
        # payload1=json.dumps(payload)
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
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
    #获取设备日图表
    def test009(self):
        print "开始执行test009"
        url=self.data.get_value('device_day','url')
        path=self.data.get_value('device_day','path')
        path2=self.data.get_value('device_day','path2')
        method=self.data.get_value('device_day','method')
        #json格式
        base_params=self.data.get_value('device_day','params')
        payload=json.loads(base_params)
        print payload
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        deviceId=cache['deviceId']
        url=(url+path+'%d'+path2)%deviceId
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
    #wifi配置时候 调用 判断是否刚配置过
    def test010(self):
        log.info("开始执行test_010")
        url=self.data.get_value('gateway_version','url')
        path=self.data.get_value('gateway_version','path')
        method=self.data.get_value('gateway_version','method')
        Authorization=cache['Authorization2']
        print 'token为%s'%Authorization
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        sn='0506293503'
        path2=path+"%s"%sn
        print url+path2
        if method=="get":
            response=requests.get(url=url+path2,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        elif method=="post":
            response=requests.post(url=url+path2,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print result
        log.info("test_010 pass")

if __name__ == '__main__':
    unittest.main()

