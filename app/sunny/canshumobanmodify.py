# encoding:utf-8
import json as j
import redis as r
import time
import requests as re
import jsonpath
def connect():
    try:
        hostName = '192.168.1.53'
        port = 6379
        # password = 1234
        pool = r.ConnectionPool(host=hostName, port=port)
        redis = r.Redis(connection_pool=pool)
        return redis
    except Exception,e:
        print e


def Ez1():
    try:
        #修改逆变器状态为1ez
        redis1=connect()
        #sensor:B601
        jsonresult = redis1.hget("dv:100672591", "_d")
        _d = j.loads(jsonresult)  #将字符串转换为字典
        ez=_d['1ez'] #取字典中某个字段的值
        print ez

        _d['1ez']=99 #重新定义字段的值
        print _d['1ez']
        #print _d
        jsonresult1=j.dumps(_d) #将字典转换为字符串
        #print jsonresult1
        # jsonresult2=jsonresult1.replace('"','\\\"') #将双引号前加入\
        # print jsonresult2
        redis1.hset("dv:100672591","_d",jsonresult1) #修改_d的值
        jsonresult3=redis1.hget("dv:100672591","_d")#获取_d的值
        print jsonresult3
    except Exception,e:
        print e

def pj2():
    try:
        #修改电池运行状态为2pj
        redis1=connect()
        #sensor:B401
        jsonresult = redis1.hget("dv:100672351", "_d")
        _d = j.loads(jsonresult)  #将字符串转换为字典
        pj=_d['2pj'] #取字典中某个字段的值
        print pj

        _d['2pj']=6#重新定义字段的值
        print _d['2pj']
        #print _d
        jsonresult1=j.dumps(_d) #将字典转换为字符串
        #print jsonresult1
        # jsonresult2=jsonresult1.replace('"','\\\"') #将双引号前加入\
        # print jsonresult2
        redis1.hset("dv:100672351","_d",jsonresult1) #修改_d的值
        jsonresult3=redis1.hget("dv:100672351","_d")#获取_d的值
        print jsonresult3
    except Exception,e:
        print e
def gu4():
    try:
        #修改电池运行状态为2pj
        redis1=connect()
        #sensor:0507
        jsonresult = redis1.hget("dv:100671628", "_d")
        _d = j.loads(jsonresult)  #将字符串转换为字典
        pj=_d['4gu'] #取字典中某个字段的值
        print pj

        _d['4gu']=1#重新定义字段的值
        print _d['4gu']
        #print _d
        jsonresult1=j.dumps(_d) #将字典转换为字符串
        #print jsonresult1
        # jsonresult2=jsonresult1.replace('"','\\\"') #将双引号前加入\
        # print jsonresult2
        redis1.hset("dv:100671628","_d",jsonresult1) #修改_d的值
        jsonresult3=redis1.hget("dv:100671628","_d")#获取_d的值
        print jsonresult3
    except Exception,e:
        print e

def mi1():
    try:
        #修改储能逆变器功率
        redis1=connect()
        #sensor:2708
        jsonresult = redis1.hget("dv:100672410", "_d")
        _d = j.loads(jsonresult)  #将字符串转换为字典
        pj=_d['1mi'] #取字典中某个字段的值
        print pj

        _d['1mi']=200#重新定义字段的值
        print _d['1mi']
        #print _d
        jsonresult1=j.dumps(_d) #将字典转换为字符串
        #print jsonresult1
        # jsonresult2=jsonresult1.replace('"','\\\"') #将双引号前加入\
        # print jsonresult2
        redis1.hset("dv:100672410","_d",jsonresult1) #修改_d的值
        jsonresult3=redis1.hget("dv:100672410","_d")#获取_d的值
        print jsonresult3
    except Exception,e:
        print e

#bms连接状态
def kr4():
    try:
        redis1=connect()
        #sensor:B601
        jsonresult = redis1.hget("dv:100680858", "_d")
        _d = j.loads(jsonresult)  #将字符串转换为字典
        kr=_d['4kr']  #取字典中某个字段的值
        print kr
        _d['4kr']=0
        print  _d['4kr']
        jsonresult1=j.dumps(_d)
        print jsonresult1
        redis1.hset("dv:100680858","_d",jsonresult1) #修改_d的值
        jsonresult3=redis1.hget("dv:100680858", "_d")#获取_d的值
        print jsonresult3
    except Exception,e:
        print e

def rj4():
    try:
        #修改电表连接状态
        redis1=connect()
        #sensor:B801
        jsonresult = redis1.hget("dv:100680858", "_d")
        _d = j.loads(jsonresult)  #将字符串转换为字典
        rj=_d['4rj'] #取字典中某个字段的值
        print rj


        _d['4rj']=0#重新定义字段的值
        print _d['4rj']
        #print _d
        jsonresult1=j.dumps(_d) #将字典转换为字符串
        #print jsonresult1
        # jsonresult2=jsonresult1.replace('"','\\\"') #将双引号前加入\
        # print jsonresult2
        redis1.hset("dv:100680858","_d",jsonresult1) #修改_d的值
        jsonresult3=redis1.hget("dv:100680858","_d")#获取_d的值
        print jsonresult3
    except Exception,e:
        print e
#循环修改状态值，等待时间为30s
def ff1():
    try:
        #修改电池状态

        redis1=connect()
        #sensor:B801 100680858,sensor:B901 100680859
        battery_status=[5,6,7,8,9,10,11,12]
        battery_status1=battery_status[0:6]
        print battery_status1
        battery_status2=battery_status[6:8]
        print battery_status2

        for status in battery_status1:
            print status
            jsonresult = redis1.hget("dv:100680858", "_d")
            #sensor:B901 100680859
            _d = j.loads(jsonresult)  #将字符串转换为字典
            ff=_d['1ff'] #取字典中某个字段的值
            print ff
            _d['1ff']=status #重新定义字段的值
            print _d['1ff']
            jsonresult1=j.dumps(_d) #将字典转换为字符串
            #sensor:B801
            redis1.hset("dv:100680858","_d",jsonresult1) #修改_d的值
            jsonresult3=redis1.hget("dv:100680858","_d")#获取_d的值
            print jsonresult3
            time.sleep(30)
        for status in battery_status2:
            print status
            jsonresult = redis1.hget("dv:100680859", "_d")
            #sensor:B901 100680859
            _d = j.loads(jsonresult)  #将字符串转换为字典
            ff=_d['1ff'] #取字典中某个字段的值
            print ff
            _d['1ff']=status #重新定义字段的值
            print _d['1ff']
            jsonresult1=j.dumps(_d) #将字典转换为字符串
            #sensor:B801
            redis1.hset("dv:100680859","_d",jsonresult1) #修改_d的值
            jsonresult3=redis1.hget("dv:100680859","_d")#获取_d的值
            print jsonresult3
            time.sleep(30)
    except Exception,e:
        print e


#连接状态
kr4()
# #电表连接状态
# rj4()
# #电池状态
# ff1()
# abc()

# mi1()
# pj2()
# Ez1()
# gu4()


    # #修改电池类型为2pm
    # def Pm2():
    #     pm=_d['2pm'] #取字典中某个字段的值
    #     print pm
    #     _d['2pm']=9 #重新定义字段的值
    #     print _d['2pm']
    #     # print _d
    #     jsonresult1=j.dumps(_d) #将字典转换为字符串
    #     print jsonresult1
    #     # jsonresult2=jsonresult1.replace('"','\\\"') #将双引号前加入\
    #     # print jsonresult2
    #     redis.hset("dv:100671631","_d",jsonresult1) #修改_d的值
    #     jsonresult3=redis.hget("dv:100671631", "_d")#获取_d的值
    #     print jsonresult3

    # def X():
    #     #修改逆变器状态为x
    #     x=_d['x'] #取字典中某个字段的值
    #     print x
    #     _d['x']=80 #重新定义字段的值
    #     print _d['x']
    #     #print _d
    #     jsonresult1=j.dumps(_d) #将字典转换为字符串
    #     #print jsonresult1
    #     # jsonresult2=jsonresult1.replace('"','\\\"') #将双引号前加入\
    #     # print jsonresult2
    #     redis.hset("dv:100672177","_d",jsonresult1) #修改_d的值
    #     jsonresult3=redis.hget("dv:100672177","_d")#获取_d的值
    #     print jsonresult3





