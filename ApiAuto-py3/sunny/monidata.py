#encoding:utf-8
import requests as re
import json as j
import time,datetime
import socket
import threading
def fun_timer():
    global timer
    #date=d.datetime.now()
    #获取当前的日期格式为2019-03-21
    date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    #获取当前的时间取小时数，并减去8，取utc时间
    date1=datetime.datetime.now()
    hour=date1.hour-8
    hour1='0'+str(hour)+'%3A00%2C'
    # print hour1
    # print date
    # print hour
    # print type(date)
    # print type(hour)
    #组合取得符合格式的日期时间
    date2=date+'+'+hour1
    print (date2)
    #采集器sn
    gatewaysn='704948209'
    #帧类型
    type=2
    #url='http://backend.solarmanpv.com:8180/solarman2Demo/cong/totalMsg.action?date=s%&gatewaySn=%s&type=%d' %(date,gatewaysn,type)
    #取该接口中的第一条数据
    #url='http://backend.solarmanpv.com:8180/solarman2Demo/cong/totalMsg.action?date=2019-03-21+07%3A00%2C&gatewaySn=804998682&type=2'
    url='http://backend.solarmanpv.com:8180/solarman2Demo/cong/totalMsg.action?date=%s&gatewaySn=%s&type=%d' %(date2,gatewaysn,type)
    r1=re.get(url)
    # print r1
    result1=j.loads(r1.content)
    # print result1
    datas=result1['datas']
    # print datas
    if len(datas)==0:
        print ("无设备数据")
        timer=threading.Timer(300,fun_timer)
        timer.start()
    else:
        first_data=datas[0]
        second_data=datas[1]
        # print first_data
        alldata=first_data['allData']
        alldata2=second_data['allData']
        # print alldata
        data=j.loads(alldata)['zb']
        data2=j.loads(alldata2)['zb']
        print (data)
        # print (type(first_data))
        print (data2)
        #二期测试环境
        target_host = '192.168.30.44'
        target_port = 10000
        # #三期功能测试环境
        # target_host = 'group-a.f-qa.igen'
        # target_port = 10000
        #建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个TCP客户端
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #连接到服务器
        client.connect((target_host, target_port))
        a=bytes().fromhex(data)
        a2=bytes().fromhex(data2)
        #a=data.decode('hex')  #bytes转为十六进制
        print (a)
        print (a2)
        # print type(a)
        client.send(a)
        client.send(a2)
        print (datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"))
        #接收数据
        #response = client.recv(4096)
        #print(response)
        # global timer
        timer=threading.Timer(300,fun_timer)
        timer.start()
timer=threading.Timer(1,fun_timer)
timer.start()


