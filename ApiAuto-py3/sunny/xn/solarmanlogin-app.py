# coding:utf-8
from locust import HttpLocust,TaskSet,task
import random,json
from src.common.excel_simple import ExcleHelper
from src.common.logger import Log
import threading
cache={}
log=Log()
class Solarmanbusiness(TaskSet):
    data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\test.xlsx','phone')
    #手机账号登录
    @task(1)
    def test_001(self):
        # log.info("开始执行test_001")
        url=self.data.get_value('login_mobile','url')
        path=self.data.get_value('login_mobile','path')
        headers1=self.data.get_value('login_mobile','headers')
        base_params=self.data.get_value('login_mobile','params')
        #json.loads是将转化为json
        payload=json.loads(base_params)
        headers=json.loads(headers1)
        # print type(headers)
        print (url+path)
        response=self.client.post(url=url+path,data=payload,headers=headers)
        print (response.status_code)
        assert response.status_code ==200
        result=json.loads(response.content)
        access_token=result['access_token']
        bearer=result['token_type']
        Authorization=bearer+" "+access_token
        cache['Authorization1']=Authorization
        # print cache
        # log.info("test_001 pass")
    #获取商家列表
    @task(1)
    def test_002(self):
        url=self.data.get_value('get_list','url')
        path=self.data.get_value('get_list','path')
        method=self.data.get_value('get_list','method')
        base_params=self.data.get_value('get_list','params')
        # Authorization=self.test_001()
        Authorization=cache['Authorization1']
        print ("token002为%s'%Authorization")
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print (url+path)
        response=self.client.get(url=url+path,headers=headers)
        print (response.status_code)
        assert response.status_code ==200
        result=json.loads(response.content)
        # print type(result)
        rog_id=result[0]['org']['id']
        cache['rog_id']=rog_id
        return rog_id
    #手机商家登录
    @task(1)
    def test_003(self):
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
        print (url+path)
        response=self.client.post(url=url+path,data=payload,headers=headers)
        print (response.status_code)
        assert response.status_code ==200
        result=json.loads(response.content)
        access_token=result['access_token']
        bearer=result['token_type']
        Authorization=bearer+" "+access_token
        print ('token003为%s'%Authorization)
        cache['Authorization2']=Authorization
    #获取用户信息
    @task(1)
    def test_004(self):
        url=self.data.get_value('get_userinfo','url')
        path=self.data.get_value('get_userinfo','path')
        method=self.data.get_value('get_userinfo','method')
        base_params=self.data.get_value('get_userinfo','params')
        #Authorization=self.test_003()
        Authorization=cache['Authorization2']
        headers={"authorization":"%s"%Authorization,
                 "User-agent":"okhttp/3.9.1"}
        print (url+path)
        if method=="get":
            response=self.client.get(url=url+path,headers=headers)
            print (response.status_code)
            assert response.status_code ==20
            result=json.loads(response.content)
            roleid=result['orgUser']['roleId']
            cache['roleid']=roleid

class websitUser(HttpLocust):
    task_set = Solarmanbusiness
    min_wait = 1000  # 单位毫秒
    max_wait = 1000  # 单位毫秒
if __name__ == "__main__":
    import os
    #测试结果保存为csv
    #不使用web页面，直接页面打印，并保存结果
    # os.system("locust -f app.py --host=http://47.88.18.157:18014   --csv=solarmanpro --no-web -c 100 -r 10 -n 3000")
    os.system("locust -f solarmanlogin-app.py --host =http://api4csi.solarman.cn")
