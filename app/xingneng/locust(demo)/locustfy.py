#encoding:utf-8
from locust import HttpLocust,TaskSet,task
from xingneng.common import  setUp_,md5
from xingneng.readData import Readdata # 导入参数化的类

# 定义用户行为
class SpeakAdd(TaskSet):
    # 定义类的实例变量
    ts = setUp_()[0]
    reqId = setUp_()[1]
    secret = setUp_()[2]
    header = setUp_()[3]
    # db = setUp_()[4]
    # userId = setUp_()[4]
    # liveId = setUp_()[5]
    # 获取参数化数据
    rd = Readdata()
    # 发言类型type，因为不同用户这个是不同的
    type = rd.readType()
    # 获取发言人id，这里和发言类型对应，上面做了处理
    userId = rd.readUserid()
    #加密
    reqSign = reqId + ':' + secret + ':' + ts
    sign = md5(reqSign)
    # 请求参数
    data = { "id": reqId,
             "timestamp": ts,
             "sign": sign,
             "data": {   "commentId":"",
                         "topicId": "100000046000082",
                         "type": type,
                         "liveId": "140000002000038",
                         "content": "我正在发言，" + ts,
                         "isReplay": "N",
                         "page": {"size": "20", "page": "1"},
                         "userId": userId}}
    @task(1)
    def testSpeakadd(self):
        # 和requests请求一样写
        r = self.client.post("/h5/speak/add",json=self.data,headers=self.header,timeout=30)
        result = r.json()# 返回字典
        # 断言
        assert r.status_code == 200
        assert result['state']['code'] == 0


# 设置性能测试
class WebsiteUser(HttpLocust):
    task_set = SpeakAdd
    # 接口测试think time 设置为0
    min_wait = 0
    max_wait = 0

# 下面可以通过直接运行Python locustfile1.py c r n 进行测试，这种方式适合 --no-web运行
if __name__ == "__main__":
    import os,sys
    # sys.argv是一个list，元素是用户自定义的，原来是str类型，需要转换为int
    c = int(sys.argv[1])
    r = int(sys.argv[2])
    t = int(sys.argv[3])
    for i in range(2):
        # os.system(命令)，可以运行shell、Windows命令
        os.system("locust -f locustfile1.py --host=http://xxxxxt2.qlchat.com --no-web -c %d -r %d -n %d" %(c,r,t))
