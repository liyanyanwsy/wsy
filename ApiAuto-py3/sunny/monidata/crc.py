#encoding:utf-8
# data='9700104201030B044A6B0107547030C55D7030C55D288DA400000B0005B8366C797930323831310000000D00070004000F000CD57A0006000C0004000F0008000D0006000A000C000200020006000B000A000C0003000D000200000009000B000E00030001000300090009000B000A0000000F000E000C0009000900050006000D0004000D00040002000E000D000600030006000D000C0003000A000500060002000D000700090000000300020000000A0001000E000E0007000D00020007000C000C0004000B0008204E759EF8CC000700050008000E0002000A0003000B000200020002000A000D000F000C000B00020002B31C3FC03C2A00066D4C227054B4000D143D676095790006000AA43300020002000BEAE7000A0005000318F3000EEE9200000000000B55F400010000690900030007000F2D75E65DD181CDB2E0850B40BD209E36DD72196E46454BF1D5313E73F19F92F1BC5D5C62C344FFD074D35AB76F6DD32D7E0F4E2E6E1AF8BA6DD0569BC42AE083B7F5BA0C32403CA7E1812180B60643785EE718340D7AA69613F878F708E2D930AAC577433E57BF0634EA7D60499D63A5924263710D5FFB065E58AD357170BC2DDDA937A6B7C5EBF5E70542FAAFCB18E73CFDE8888A2B7F97A51271B00D807384CC300B9771E7EDA19CC59324F69A9E3BAD68BC24C27E59E8BDBC1019EBBED430000400020E090000000D0005000500090009000F0006000700010005000E000C000A0002000F000D00090005000F0002000C000000050001000C0004000B0002000B000600090001000F000D0003000900090001000200000004000800040004000D0001000F000D000E0006000B00040007000E0008000D00000009000E00060009000E00070008000F0002000E000C000D0004000B000E000D000E00010000000500020004000A0002000B0004000E000800020003000400080004000D000600080000000F000700060000000600090005000900060000000400090005000C00060005000E0009000A000A0005000A000F00010002000000040003000D0005000D000900060002000F000E00060006000F000B000F00050001000D000800010006000C000D00050002000E000D000800000005000D0008000E0005000A00010008000B000700070003000B0004000900030008000F000500000005000C0006000F000F000A00050007000A000B000F0007000A0006000E0006000600050003000200050006000A0009000300090008000100070003000C000E0009000F0002000C000A0004000F0004'
# def crc16(x, invert):
#     a = 0xFFFF
#     b = 0xA001
#     for byte in x:
#         a ^= ord(byte)
#         for i in range(8):
#             last = a % 2
#             a >>= 1
#             if last == 1:
#                 a ^= b
#     s = hex(a).upper()
#     return s[4:6]+s[2:4] if invert == True else s[2:4]+s[4:6]
# crcdff=crc16(data,False)
# print(crcdff)

# Queue.Queue(maxsize=0) FIFO，如果maxsize小于1就表示队列长度无限
# Queue.LifoQueue(maxsize=0) LIFO，如果maxsize小于1就表示队列长度无限
# Queue.qsize() 返回队列的大小
# Queue.empty() 如果队列为空，返回True,反之False
# Queue.full() 如果队列满了，返回True,反之False
# Queue.get([block[,timeout]]) 读队列，timeout等待时间
# Queue.put(item, [block[,timeout]]) 写队列，timeout等待时间
# Queue.queue.clear() 清空队列
# import queue
#
# q = queue.Queue()
#
# for i in range(5):
#     q.put(i)
#
# while not q.empty():
#     print(q.get())
from locust import HttpLocust, TaskSet,task

# import queue
#
# class test_taskset(TaskSet):
#
#     @task(1)
#     def register(self):
#
#         try:
#
#             data = self.locust.queueData.get() //获取队列里的数据
#             print(data)
#
#         except queue.Empty: //队列取空后，直接退出
#
#             print('no data exist')
#
#         exit(0)
#
#     data['password']))
#
#     payload = {
#
#         'username': data['password'],
#
#         'password': data['username'],
#
#     }
#     self.client.post('login', data=payload)//POST方法发送请求
#
#     class test_run(HttpLocust):
#
#     host = 'xxx/zhuce'
#
#     task_set = test_taskset
#
#     queueData = queue.Queue() //队列实例化
#
#     for count in range(50): //循环数据生成
#
#     data = {
#
#         "username": "test%d" % count,
#
#         "password": "pwd%d" % count,}


from locust import HttpLocust, TaskSet, task
from random import randint

# Web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    # 随机返回登录用户
    def login_user1(self):
        users = {"8617798736289":'1',"2972049643@qq.com":'2',"wsy":'3'}
        data = randint(1, 3)
        username = "user"+str(data)
        identity_type = users[username]
        return self.username, self.identity_type
    @task
    def login(self):
        username, identity_type = login_user1(self)


        

        self.client.post("/oauth-s/oauth/token", {"username":username, "password":password,'grant_type':'password','client_id':'test','clear_text_pwd':'123456','identity_type':identity_type})


class User(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000
    host = "http://www.f-qa.igen"
