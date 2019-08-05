# encoding:utf8
import json as j
import socket
import threading
import requests as re
import time
import datetime as d
import MySQLdb
#通过接口中的原始数据来发送数据，暂时未实现，该接口中的设备数据未采集器数据，不知道是bug，还是故意这样设计
device_id=100551846
# device_id=100824294
# device_id=101214889

# device_id=100683351
def userinfo():
    # conn = MySQLdb.connect(host='192.168.1.53', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
    #                        port=3306, charset='utf8')
    conn = MySQLdb.connect(host='web.solarmanpv.com', user='readonly', passwd='yingZHEN123', db='solarman2',
                           port=33306, charset='utf8')
    cur=conn.cursor()
    # cur.execute("SELECT * FROM sys_verify_message WHERE verify_account='17798735555' ORDER BY udpate_time DESC LIMIT 1")
    #通过device_id从数据库中查询用户id和公司id
    sql1="SELECT us.uid,us.company_id FROM device de INNER JOIN group_entity en ON en.entity_sn=de.datalogger_sn INNER JOIN user_group_profile gr ON gr.group_id=en.group_id INNER JOIN b_user us ON us.uid=gr.uid WHERE de.device_id=%d AND en.entity_type=99 LIMIT 2" %device_id
    cur.execute(sql1)
    re1 = cur.fetchone()
    cur.close()
    conn.close()
    # print  re1
    # print type(re1)
    # a=re1[0]
    # print a
    # print type(a)
    # uid=a[0]
    # complany_id=a[1]
    return  re1

def fun_timer():
    #逆变器详情页面接口
    uid=userinfo()[0]
    print uid
    complany_id=userinfo()[1]
    print complany_id
    # device_id=100551846
    url1='http://apipro-cdn.solarman.cn/v00009/epc/device/inverter/doDetail.json?uid=%d&companyId=%d&deviceId=%d&lan=1' %(uid,complany_id,device_id)
    print url1
    r1=re.get(url1)
    result1=j.loads(r1.content)
    # print result1
    # print type(result1)
    #通过接口返回数据中取原始数据
    DeviceWapper=result1['DeviceWapper']
    # print DataloggerWapper
    # print type(DataloggerWapper)
    extend=DeviceWapper['extend']
    # print extend
    # print type(extend)
    extend1=j.loads(extend)
    # print extend1
    # print type(extend1)
    zb=extend1['zb']
    print zb
    print type(zb)
    #只能发送到测试环境，不能发送到外网
    target_host = '192.168.1.52'
    target_port = 10000
    #建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个TCP客户端
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #连接到服务器
    client.connect((target_host, target_port))
    #发送数据
    a=zb.decode('hex')  #bytes转为十六进制
    print type(a)
    #print a
    #client.send(str.encode(d))
    client.send(a)
    #aa=a.encode('hex')  #转为bytes
    print d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    #接收数据
    #response = client.recv(4096)
    #print(response)
    global timer
    #五分钟发送一次模拟数据
    timer=threading.Timer(300,fun_timer)
    timer.start()
timer=threading.Timer(1,fun_timer)
timer.start()


