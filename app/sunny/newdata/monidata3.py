#encoding:utf-8
import requests as re
import json as j
import time,datetime
import socket
import threading
#生产环境
url2='http://101.132.44.31:35601/elasticsearch/_msearch'
payload={"index":"dataflow-access-*","ignore_unavailable":true,"preference":1554864788206}
{"version":true,
 "size":500,
 "sort":[{"@timestamp":{"order":"desc","unmapped_type":"boolean"}}],"_source":{"excludes":[]},"aggs":{"2":{"date_histogram":{"field":"@timestamp","interval":"30s","time_zone":"Asia/Shanghai","min_doc_count":1}}},"stored_fields":["*"],"script_fields":{},"docvalue_fields":[{"field":"@timestamp","format":"date_time"},{"field":"接收时间","format":"date_time"},{"field":"采集时间","format":"date_time"}],"query":{"bool":{"must":[{"query_string":{"query":"1800011003","analyze_wildcard":true,"default_field":"*"}},{"range":{"@timestamp":{"gte":1554864102221,"lte":1554865002221,"format":"epoch_millis"}}}],"filter":[],"should":[],"must_not":[]}},"highlight":{"pre_tags":["@kibana-highlighted-field@"],"post_tags":["@/kibana-highlighted-field@"],"fields":{"*":{}},"fragment_size":2147483647},"timeout":"30000ms"}

def fun_timer():

    #采集器sn
    gatewaysn='2403650718'
    #帧类型
    type=2
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
        print "无设备数据"
    else:
        first_data=datas[0]
        # print first_data
        alldata=first_data['allData']
        # print alldata
        data=j.loads(alldata)['zb']
        print data
        #二期测试环境
        # target_host = '192.168.1.52'
        # target_port = 10000
        #三期功能测试环境
        target_host = 'group-a.f-qa.igen'
        target_port = 10000
        #建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个TCP客户端
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #连接到服务器
        client.connect((target_host, target_port))
        a=data.decode('hex')  #bytes转为十六进制
        print a
        # print type(a)
        client.send(a)
        print datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
        #接收数据
        #response = client.recv(4096)
        #print(response)
        global timer
        timer=threading.Timer(300,fun_timer)
        timer.start()
timer=threading.Timer(1,fun_timer)
timer.start()


