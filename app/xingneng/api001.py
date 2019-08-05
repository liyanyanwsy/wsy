# coding:utf-8
from locust import HttpLocust,TaskSet,task
import random
class Solarmanpro(TaskSet):
    @task(1)
    def solarman(self):
        # 定义requests的请求头
        header = {
            #"Connection": "Keep-Alive",
            #"Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.9.1"}
        r=self.client.get("/v00009/epc/plantView/doPlantList.json?uid=10516&companyId=5244&statusType=-1&pageIndex=1&pageSize=50",headers=header,verify=False)
        print r.status_code
        assert r.status_code ==200

class websitUser(HttpLocust):
    task_set = Solarmanpro
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒


if __name__ == "__main__":
    import os
    #测试结果保存为csv
    #不使用web页面，直接页面打印，并保存结果
    # os.system("locust -f app.py --host=http://47.88.18.157:18014   --csv=solarmanpro --no-web -c 100 -r 10 -n 3000")
    os.system("locust -f api001.py --host=http://47.88.18.157:18014")