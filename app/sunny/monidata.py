# encoding:utf8
import json as j
import redis as r
import socket
import threading
import time
import datetime as d

def fun_timer():

    #hostName = '192.168.1.53'
    #port = 6379
    hostName = '47.88.4.103'
    port = 16379
    pool = r.ConnectionPool(host=hostName, port=port)
    redis = r.Redis(connection_pool=pool)
    #jsonresult = redis.hget("dv:100662512","_d")
    # jsonresult = redis.hget("dv:100824294","_d")
    # #模拟0505数据，sn705717329
    # jsonresult = redis.hget("dv:101193463","_d")
    #模拟数据5407，sn:517515105
    jsonresult = redis.hget("dv:101204361","_d")
    #模拟数据0507，sn:707948301
    jsonresult1 = redis.hget("dv:101214889","_d")
    _d = j.loads(jsonresult)
    _d1 = j.loads(jsonresult1)
    zb=_d['zb']
    zb1=_d1['zb']
    print zb
    print zb1
    print type(zb) #查看数据类型

    #target_host = '192.168.88.1'
    #target_port = 12345
    target_host = '192.168.1.52'
    target_port = 10000
    #建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个TCP客户端
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #连接到服务器
    client.connect((target_host, target_port))

    #发送数据
    #d='A5B900104228792ED30830010327F7840D01FD1E0000CF83D25901006EDE000053453145533333304835333032332020000000000000000000000000000000006E0900000000801300000000000000000000000000000000000000000000000000000000FFFF2E13E8FF1400F2FF0D001000000000005200520030040000FE000000FF0300009C060000000080000000A600B500FDFF6E095F000000070000000C001E000000140009001000FAFFF7FF0000000000000000000000000000170300000000DA15'
    #a=bytes().fromhex('A5B900104228792ED30830010327F7840D01FD1E0000CF83D25901006EDE000053453145533333304835333032332020000000000000000000000000000000006E0900000000801300000000000000000000000000000000000000000000000000000000FFFF2E13E8FF1400F2FF0D001000000000005200520030040000FE000000FF0300009C060000000080000000A600B500FDFF6E095F000000070000000C001E000000140009001000FAFFF7FF0000000000000000000000000000170300000000DA15')
    #a=bytes().fromhex(zb)
    a=zb.decode('hex')  #bytes转为十六进制
    a1=zb1.decode('hex')
    print type(a)
    #print a
    #client.send(str.encode(d))
    client.send(a)
    client.send(a1)
    #aa=a.encode('hex')  #转为bytes

    #print aa
    print d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    #接收数据
    #response = client.recv(4096)
    #print(response)
    global timer
    timer=threading.Timer(300,fun_timer)
    timer.start()
    
timer=threading.Timer(1,fun_timer)
timer.start()






