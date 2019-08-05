# encoding:utf8
import json as j
import redis as r
import socket
import threading
import time
import datetime as d
def fun_timer():

    hostName = '47.88.4.103'
    port = 16379
    pool = r.ConnectionPool(host=hostName, port=port)
    redis = r.Redis(connection_pool=pool)
    #模拟0503数据，sn201612029
    jsonresult1 = redis.hget("dv:101154730","_d")
    #模拟0504数据，sn704200687
    jsonresult2 = redis.hget("dv:101108982","_d")
    #模拟0505数据，sn705359405
    jsonresult3 = redis.hget("dv:101207144","_d")
    #模拟0507数据，sn707293997
    jsonresult4 = redis.hget("dv:101218342","_d")
    _d1 = j.loads(jsonresult1)
    _d2 = j.loads(jsonresult2)
    _d3 = j.loads(jsonresult3)
    _d4 = j.loads(jsonresult4)
    zb1=_d1['zb']
    zb2=_d2['zb']
    zb3=_d3['zb']
    zb4=_d4['zb']
    print zb1
    print zb2
    print zb3
    print zb4
    print type(zb1) #查看数据类型
    print type(zb2)
    print type(zb3) #查看数据类型
    print type(zb4)
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
    a1=zb1.decode('hex')  #bytes转为十六进制
    a2=zb2.decode('hex')
    a3=zb3.decode('hex')
    a4=zb4.decode('hex')
    print type(a1)
    print type(a2)
    print type(a3)
    print type(a4)

    #print a
    #client.send(str.encode(d))
    client.send(a1)
    client.send(a2)
    client.send(a3)
    client.send(a4)
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






