# coding:utf-8
from locust import HttpLocust,TaskSet,task
import random

class Guanggaoxn(TaskSet):
    '''广告接口性能测试'''
    @task(1)
    def guangao(self):
        # 定义requests的请求头
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        platform=[13,14,15]
        positon=[4,5]
        channel=[18,19,20,21,22,23,24,25,26]

        a=range(len(platform))
        b=range(len(positon))
        c=range(len(channel))
        for i in a:
            for j in b:
                for k in c:
                    platform1=platform[i]
                    positon1=positon[j]
                    channel1=channel[k]
                    print platform1,positon1,channel1
                    r = self.client.get("/advert/search?platform=%d&position=%d&runType=16&channel=%d&softversion=Home_Android_1.4.4&hardversion=Home_Android_22" %(platform1,positon1,channel1),headers=header, verify=False)
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
    task_set = Guanggaoxn
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒

if __name__ == "__main__":
    import os
    #测试结果保存为csv
    #不使用web页面，直接页面打印，并保存结果
    os.system("locust -f guanggaoxn.py --host=http://192.168.1.58:28080  --csv=guanggao --no-web -c 100 -r 10 -n 3000")
