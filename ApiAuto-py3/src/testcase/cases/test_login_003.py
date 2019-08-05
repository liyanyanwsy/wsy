#encoding:utf-8
import requests
import json
from src.common.excel_simple import ExcleHelper
import unittest
from src.common.logger import Log
cache={}
log=Log()
#test_user001-test_user004为用户名登录信息，test_user005-test_user011为列表信息，test_user012-test_user018为添加网关，子设备，删除网关设备
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto\config\test.xlsx','Sheet2')
        cls.data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\test.xlsx','username')
    def setUp(self):
        # self.data=ExcleHelper()
        pass
    #test_user001-test_user004为用户名登录信息，test_user005-test_user011为列表信息，test_user012-test_user018为添加网关，子设备，删除网关设备
    #用户名账号登录
    def test_user001(self):
        log.info("开始执行test_user001")
        url=self.data.get_value('login_username','url')
        path=self.data.get_value('login_username','path')
        headers1=self.data.get_value('login_username','headers')
        method=self.data.get_value('login_username','method')
        base_params=self.data.get_value('login_username','params')
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
        log.info("test_user001 pass")
        #获取商家列表
    #获取商家列表
    def test_user002(self):
        log.info("开始执行test_user002")
        url=self.data.get_value('get_list003','url')
        path=self.data.get_value('get_list003','path')
        method=self.data.get_value('get_list003','method')
        base_params=self.data.get_value('get_list003','params')
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
        log.info("test_user002 pass")
    #用户名商家登录
    def test_user003(self):
        log.info("开始执行test_user003")
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
        log.info("开始执行test_user003")
    #获取用户信息
    def test_user004(self):
        log.info("开始执行test_user003")
        url=self.data.get_value('get_userinfo003','url')
        path=self.data.get_value('get_userinfo003','path')
        method=self.data.get_value('get_userinfo003','method')
        base_params=self.data.get_value('get_userinfo003','params')
        #Authorization=self.test_003()
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print (url+path)
        if method=="get":
            response=requests.get(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            roleid=result['orgUser']['roleId']
            cache['roleid']=roleid
        elif method=="post":
            response=requests.post(url=url+path,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
        log.info("test_user004 pass")
    #电站列表
    def test_user005(self):
        log.info("开始执行test_user005")
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
            inverter_id=result['data'][1]['id']
            meter_id=result['data'][2]['id']
            cache['inverter_id']=inverter_id
            cache['meter_id']=meter_id
        elif method=="post":
            response=requests.post(url=url+path,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
            inverter_id=result['data'][1]['id']
            meter_id=result['data'][2]['id']
            cache['inverter_id']=inverter_id
            cache['meter_id']=meter_id
        log.info("test_user005 pass")
    #获取电站下网关设备设备列表
    def test_user006(self):
        log.info("开始执行test_user006")
        url=self.data.get_value('device_list','url')
        path=self.data.get_value('device_list','path')
        path2=self.data.get_value('device_list','path2')
        method=self.data.get_value('device_list','method')
        #json格式
        base_params=self.data.get_value('device_list','params')
        # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_user006 pass")
    #获取电站下采集器列表
    def test_user007(self):
        log.info("开始执行test_user007")
        url=self.data.get_value('collector_list','url')
        path=self.data.get_value('collector_list','path')
        path2=self.data.get_value('collector_list','path2')
        method=self.data.get_value('collector_list','method')
        #json格式
        base_params=self.data.get_value('collector_list','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_user007 pass")
    #获取电站下逆变器列表
    def test_user008(self):
        log.info("开始执行test_user008")
        url=self.data.get_value('inverter_list','url')
        path=self.data.get_value('inverter_list','path')
        path2=self.data.get_value('inverter_list','path2')
        method=self.data.get_value('inverter_list','method')
        #json格式
        base_params=self.data.get_value('inverter_list','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_user008 pass")
    #获取电站下电表列表
    def test_user009(self):
        log.info("开始执行test_user009")
        url=self.data.get_value('meter_list','url')
        path=self.data.get_value('meter_list','path')
        path2=self.data.get_value('meter_list','path2')
        method=self.data.get_value('meter_list','method')
        #json格式
        base_params=self.data.get_value('meter_list','params')
        payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['meter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.get(url=url,data=payload,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_user009 pass")
    #获取电站下组件列表010
    #获取电站下气象站列表011
    #判断网关设备能否被添加到某个电站
    def test_user012(self):
        log.info("开始执行test_user012")
        url=self.data.get_value('system_gateway','url')
        path=self.data.get_value('system_gateway','path')
        path2=self.data.get_value('system_gateway','path2')
        method=self.data.get_value('system_gateway','method')
        #json格式
        # base_params=self.data.get_value('system_gateway','params')
        # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_user012 pass")
    #电站添加网关设备及其子设备,选择手动关联，并添加子设备016
    def test_user013(self):
        log.info("开始执行test_user013")
        url=self.data.get_value('gateway','url')
        path=self.data.get_value('gateway','path')
        path2=self.data.get_value('gateway','path2')
        method=self.data.get_value('gateway','method')
        #json格式
        base_params=self.data.get_value('gateway','params')
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            #返回信息为json
            result=response.content
            print (result)
        log.info("test_user013 pass")
    #获取网关设备下子设备列表
    def test_user014(self):
        log.info("开始执行test_user014")
        url=self.data.get_value('system_device_list','url')
        path=self.data.get_value('system_device_list','path')
        method=self.data.get_value('system_device_list','method')
        #参数直接写到excel中
        #json格式
        # base_params=self.data.get_value('system_device_list','params')
        # print type(base_params)
        # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 #"Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        url=url+path
        print (url)
        if method=="get":
            response=requests.get(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            deviceid=result['data'][0]['deviceId']
            gatewayid=result['data'][0]['gatewayId']
            cache['deviceid']=deviceid
            cache['gatewayid']=gatewayid
        elif method=="post":
            response=requests.post(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        log.info("test_user014 pass")
    #关联子设备，json格式的如何取值
    def test_user015(self):
        log.info("开始执行test_user015")
        url=self.data.get_value('device','url')
        path=self.data.get_value('device','path')
        path2=self.data.get_value('device','path2')
        method=self.data.get_value('device','method')
        #json格式
        # base_params=self.data.get_value('device','params')
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        gatewayId=cache['gatewayid']
        deviceId=cache['deviceid']
        payload=[{
            "deviceId":'%d' %deviceId,
            "gatewayId":'%d'%gatewayId
        }]
        payload1=json.dumps(payload)
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            #返回信息为json
            result=response.content
            print (result)
        log.info("test_user015 pass")
    #电站添加网关设备及其子设备,选择自动关联，获取到id,并进行删除操作
    def test_user016(self):
        log.info("开始执行test_user016")
        url=self.data.get_value('gateway002','url')
        path=self.data.get_value('gateway002','path')
        path2=self.data.get_value('gateway002','path2')
        method=self.data.get_value('gateway002','method')
        #json格式
        base_params=self.data.get_value('gateway002','params')
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
        elif method=="post":
            response=requests.post(url=url,data=base_params,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            #返回信息为json
            result=response.content
            print (result)
        log.info("test_user016 pass")
    #获取网关设备列表
    def test_user017(self):
        log.info("开始执行test_user017")
        url=self.data.get_value('system_gateway_list','url')
        path=self.data.get_value('system_gateway_list','path')
        path2=self.data.get_value('system_gateway_list','path2')
        method=self.data.get_value('system_gateway_list','method')
        #json格式
        # base_params=self.data.get_value('system_gateway_list','params')
        # payload=json.loads(base_params)
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        if method=="get":
            response=requests.get(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
            device_id=result[3]['deviceId']
            cache['device_id']=device_id
        elif method=="post":
            response=requests.post(url=url,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=json.loads(response.content)
            print (result)
            device_id=result[2]['deviceId']
            cache['device_id']=device_id
        log.info("test_user017 pass")
    #删除电站下网关设备，json格式的如何取值
    def test_user018(self):
        log.info("开始执行test_user018")
        url=self.data.get_value('delete_gateway','url')
        path=self.data.get_value('delete_gateway','path')
        path2=self.data.get_value('delete_gateway','path2')
        method=self.data.get_value('delete_gateway','method')
        #json格式
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "Content-Type":"application/json",
                 "User-agent":"okhttp/3.9.1"}
        device_id=cache['device_id']
        # print device_id
        payload=[]
        payload.append(device_id)
        # print payload
        # print type(payload)
        payload1=json.dumps(payload)
        # print payload1
        # print type(payload1)
        id=cache['inverter_id']
        url=(url+path+'%d'+path2)%id
        print (url)
        print (cache)
        if method=="delete":
            response=requests.delete(url=url,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=response.content
            print (result)
        elif method=="post":
            response=requests.delete(url=url,data=payload1,headers=headers)
            self.assertEqual(response.status_code,200,msg='返回值不是200')
            result=response.content
            print (result)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
