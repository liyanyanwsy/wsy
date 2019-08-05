# coding:utf-8
from locust import HttpLocust,TaskSet,task
import random

class Solarmanhome(TaskSet):
    '''专业版登录并发测试'''
    @task(1)
    def solarmanhome(self):
        # 定义requests的请求头
        header = {
            "Host": "192.168.1.58",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.9.1"}
        r=self.client.get("/v/ap.2.0/user/login?user_id=zcf317@126.com&user_pass=123456&terminate=android&push_sn=11a387fddbbae0474670e27ae5040686&timezone=8&lan=zh&country=CN",headers=header,verify=False)
        print r.status_code
        assert r.status_code ==200

        # r1 = self.client.get("/advert/search?platform=%s&position=%s&runType=%s&channel=19&softversion=Home_Android_1.4.4&hardversion=Home_Android_22",  headers=header, verify=False)
        # r2 = self.client.get("/advert/search?platform=%s&position=%s&runType=%s&channel=20&softversion=Home_Android_1.4.4&hardversion=Home_Android_24",  headers=header, verify=False)
        # r3 = self.client.get("/advert/search?platform=%s&position=%s&runType=%s&channel=21&softversion=Home_Android_1.4.4&hardversion=Home_Android_26",  headers=header, verify=False)
        # print r1.status_code
        # print r2.status_code
        # print r3.status_code
        # assert r1.status_code ==200
        # assert r2.status_code ==200
        # assert r3.status_code ==200

class websitUser(HttpLocust):
    task_set = Solarmanhome
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒

if __name__ == "__main__":
    import os
    #测试结果保存为csv
    #不使用web页面，直接页面打印，并保存结果
    os.system("locust -f solarmanhome.py --host=http://192.168.1.58:18003  --csv=solarmanhome --no-web -c 100 -r 10 -n 3000")


