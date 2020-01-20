#encoding:utf-8
from sunny.monidata.SolarmanCacheKeyword import SolarmanCacheKeyword as s
import pymysql
import json
import random
import time,datetime
import socket
import threading
# sortStr='2703'
# sortStr1=sortStr[2]+sortStr[3]+sortStr[1]+sortStr[0]
# print (sortStr1)
# # sortStr2=list(sortStr)
# # i=0
# # while i<len(sortStr2):
#
# # print (s      ortStr2)
# print(type(sortStr1))

#需要将这些写成类，写完整个流程后补充
def getDeviceType(devicename):
    device_type={
        '逆变器':'01',
        '汇流箱':'02',
        '电池(储能)':'03',
        '气象站':'04',
        '电表':'05',
        '空调':'06',
        '离网机':'07',
        '谐波表':'08',
        '质量监控（水、空气等':'09',
        '智能家居':'10',
        '太阳能跟踪器控制器':'11',
        '微逆':'15'
    }
    #添加default错误，后期优化
    devicetype=device_type.get(devicename)
    return  devicetype
    # a=getDeviceType('智能家居')
    # print(a)
    #定义数据类型
def getDataType(dataname):
    data_type={
        '信息帧':'01',
        '数据帧':'02'
    }
    datatype=data_type.get(dataname)
    return datatype
    # a=getDataType('数据帧')
    # # print(a)
    #定义传输的数据形式
def getDataTransType(dataTransName):
    trans_type={
        '普通实时':'01',
        '普通历史':'81',
        '精简实时':'11',
        '精简历史':'91'
    }
    transtype=trans_type.get(dataTransName)
    return transtype
# a=getDataTransType('普通实时')
# print(a)
# ruleCode='0102010327'
# print (type(ruleCode))
# conn = pymysql.connect(host='192.168.30.45', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
#                            port=3306, charset='utf8')
# cur=conn.cursor()
# sql="select context from data_structure_rule t where protocol_num='%s'"%ruleCode
# cur.execute(sql)
# result=cur.fetchall()
# print (result)
#连接数据库
def sqlconnect():
    conn = pymysql.connect(host='192.168.30.45', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
                           port=3306, charset='utf8')
    cur=conn.cursor()
    return cur
#通过适配协议，查找对应的数据长度,需要另外写函数,excludeKey和arraykey这两个不知道什么含义，后期了解一下
def getwantValueFromJsonAddStringExcludeStr(JsonString,jsvalue,wantGetValue,excludeKey,arraykey):
    getValueList=JsonString[jsvalue]
    print ('数据为%s'%getValueList)
    print (type(getValueList))
    i=0
    wantGetValueStringList=0
    # print (len(getValueList))
    if getValueList!='null':
        while i<len(getValueList):
            wantGetValueString=getValueList[i][wantGetValue]
            #中间涉及一个问题，适配协议中的有些字段并不传,2703发现适配协议中有一些字段并未传
            if getValueList[i][arraykey]!=excludeKey:
                wantGetValueStringList=wantGetValueStringList+wantGetValueString
            i=i+1
        # print (wantGetValueStringList)
    else:
        wantGetValueStringList='null'
    return wantGetValueStringList
#将16进制倒序排列,奇数偶数排列,以ox开头和不已ox开头的区分
def hexdatasort(str):
    # print (str[0:2])
    if str[0:2]=='0x':
        #去掉ox
        i=2
        sortStr=[]
        sortStr2=[]
        while i<len(str):
            a=str[i:i+2]
            i=i+2
            sortStr.append(a)
        # print (sortStr)
        # print (type(sortStr))
        #倒序排列
        sortStr1= sortStr[::-1]
        # print (sortStr1)
        #先进行连接操作
        sortStr3=''.join(sortStr1)
        # print (sortStr3)
    else:
        #去掉ox
        i=0
        sortStr=[]
        sortStr2=[]
        while i<len(str):
            a=str[i:i+2]
            i=i+2
            sortStr.append(a)
        # print (sortStr)
        # print (type(sortStr))
        #倒序排列
        sortStr1= sortStr[::-1]
        # print (sortStr1)
        #先进行连接操作
        sortStr3=''.join(sortStr1)
        # print (sortStr3)
    return sortStr3

# hexdatasort('0x04016B4A32')
# def hexdatasort(str):
#     # print (str[0:2])
#     if str[0:2]=='0x':
#         #去掉ox
#         i=2
#         sortStr=[]
#         sortStr2=[]
#         while i<len(str):
#             a=str[i:i+2]
#             i=i+2
#             sortStr.append(a)
#         # print (sortStr)
#         # print (type(sortStr))
#         if len(sortStr)%2==0:
#             #倒序排列
#             j=0
#             while j<len(sortStr):
#                 #高低位取出数据
#                 sortStr1=sortStr[len(sortStr)-2-j:len(sortStr)-j]
#                 # sortStr1= sortStr.reverse()
#                 #     sortStr1= sortStr[::-1]
#                 # print (sortStr1)
#                 #先进行连接操作
#                 sortStr3=''.join(sortStr1)
#                 # print (sortStr3)
#                 #连接后加入到列表中
#                 sortStr2.append(sortStr3)
#                 #将拼接成一个字符串
#                 j=j+2
#                 # sortStr3=''.join(sortStr2)
#             #最后再进行连接操作，得到最后的排序信息
#             sortStr4=''.join(sortStr2)
#             # print (sortStr4)
#         else:
#             j=0
#             while j<len(sortStr):
#                 #高低位取出数据
#                 sortStr1=sortStr[len(sortStr)-2-j:len(sortStr)-j]
#                 # sortStr1= sortStr.reverse()
#                 #     sortStr1= sortStr[::-1]
#                 # print (sortStr1)
#                 #先进行连接操作
#                 sortStr3=''.join(sortStr1)
#                 # print (sortStr3)
#                 #连接后加入到列表中
#                 sortStr2.append(sortStr3)
#                 #将拼接成一个字符串
#                 j=j+2
#                 # sortStr3=''.join(sortStr2)
#             #最后再进行连接操作，得到最后的排序信息
#             sortStr4=''.join(sortStr2)+str[2:4]
#             # print (sortStr4)
#     else:
#         #去掉ox
#         i=0
#         sortStr=[]
#         sortStr2=[]
#         while i<len(str):
#             a=str[i:i+2]
#             i=i+2
#             sortStr.append(a)
#         print (sortStr)
#         # print (type(sortStr))
#         if len(sortStr)%2==0:
#             #倒序排列
#             j=0
#             while j<len(sortStr):
#                 #高低位取出数据
#                 sortStr1=sortStr[len(sortStr)-2-j:len(sortStr)-j]
#                 # sortStr1= sortStr.reverse()
#                 #     sortStr1= sortStr[::-1]
#                 # print (sortStr1)
#                 #先进行连接操作
#                 sortStr3=''.join(sortStr1)
#                 # print (sortStr3)
#                 #连接后加入到列表中
#                 sortStr2.append(sortStr3)
#                 #将拼接成一个字符串
#                 j=j+2
#                 # sortStr3=''.join(sortStr2)
#             #最后再进行连接操作，得到最后的排序信息
#             sortStr4=''.join(sortStr2)
#             # print (sortStr4)
#         else:
#             j=0
#             while j<len(sortStr):
#                 #高低位取出数据
#                 sortStr1=sortStr[len(sortStr)-2-j:len(sortStr)-j]
#                 # sortStr1= sortStr.reverse()
#                 #     sortStr1= sortStr[::-1]
#                 # print (sortStr1)
#                 #先进行连接操作
#                 sortStr3=''.join(sortStr1)
#                 # print (sortStr3)
#                 #连接后加入到列表中
#                 sortStr2.append(sortStr3)
#                 #将拼接成一个字符串
#                 j=j+2
#                 # sortStr3=''.join(sortStr2)
#             #最后再进行连接操作，得到最后的排序信息
#             sortStr4=''.join(sortStr2)+str[0:2]
#             # print (sortStr4)
#     print (sortStr4)
#     return sortStr4

#随机十六进制
def getRadom4HexString(count):
    hexString =["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    if (count-3)>0:
        str='000'
        i=0
        while i<(count-3):
            number=random.choice(hexString)
            str=str+number
            # print(str)
            i=i+1
        # print(str)
    else:
        str='0'
        j=0
        while j<(count-1):
            number=random.choice(hexString)
            str=str+number
            # print(str)
            j=j+1
        # print(str)
    return str
#如果不超过count位，需要补0,如果为小段，需要倒序编码
def Insetzero(a,jsonstr,dataStr,count):
    # Insetzero(jsonresult[value][i]['byteOrder'],totalStr2,dataStr)
    # 若为小端则需要倒序编码
    if a==2:
        totalStr3=hexdatasort(jsonstr)
        # print (totalStr3)
        # print(type(totalStr3))
        # print (len(totalStr3))
        totalStr4=list(totalStr3)
        j=0
        if len(totalStr4)<count:
            while j<count-len(totalStr3):
                # print(totalStr4)
                totalStr4.append('0')
                # print(totalStr4)
                j=j+1
            # print (totalStr4)
            # print (type(totalStr4))
            totalStr5=''.join(totalStr4)
            dataStr1=dataStr+totalStr5
            # print ('偏移时间为%s'%dataStr1)
            # break
        else:
            dataStr1=dataStr+totalStr3
            # print ('偏移时间为%s'%dataStr1)
    else:
        totalStr4=list(jsonstr)
        j=0
        if len(jsonstr)<count:
            while j<count-len(jsonstr):
                # print(totalStr4)
                totalStr4.append('0')
                # print(totalStr4)
                j=j+1
            # print (totalStr4)
            # print (type(totalStr4))
            totalStr5=''.join(totalStr4)
            dataStr1=dataStr+totalStr5
            # print ('偏移时间为%s'%dataStr1)
            # break
        else:
            dataStr1=dataStr+jsonstr
            # print ('偏移时间为%s'%dataStr1)
    # print (dataStr1)
    return dataStr1
#检验计算方法
def Checksum(data):
    if data == 'null 'or data=='':
        return ""
    i=0
    total=0
    # print (len(data))
    while i<len(data):
        s=data[i:i+2]
        #16进制转化为十进制进行计算
        s2=int(s,16)
        # print (s)
        # print (s2)
        total=total+s2
        i=i+2
        # print ('累加和为%s'%total)
    #结果转化十六进制
    total1=hex(total)
    # print (total)
    print ('总和为%s'%total1)
    if len(total1)<4:
        check='0'+total1[-1]
        print (check)
    else:
        #截取倒数第二位到结尾
        check=total1[-2:]
        print ('检验和为%s'%check)
    return  check
#字符串转化为十六进制，设备sn
def strintohex(dataRule):
    totalStr=dataRule['g']
    # print (totalStr)
    #字符串转化为十六进制
    s_hex=""
    for i in range(len(totalStr)):
        s_hex=s_hex+hex(ord(totalStr[i]))[2:]
        # print (i)
        # print (s_hex)
    # print (s_hex)
    # i=0
    # while len(s_hex)<16:
    if len(s_hex)<32:
        shex=s_hex+(32-len(s_hex))*'0'
        # print (shex)
    else:
        shex=s_hex
    return shex

# Checksum('E1001042766BBDC5F6EE010505B53065007F1A00007A08605D01000A6F0000313130463830313842313330303534200E021D0A1E0F420042007200000000006C090000000089133B10000054010000DE300000000000000107000000000000000000000000000000000000A610000040000000860100006500E30400000D000000120E00007B150000E80313000B00080009002D0002005609CD00120000000100210202010000A3096E003F0064002A15EF001C021C0200000000400AA5002101000018002B00930100000C003E00700100000000000000000000AB07000070003501F800110014000100')
# Checksum('0E1001042766BBDC5F6')
#
#模拟数据部分
def createDataBaseRule(dataRule,jsonresult,value,transtype,ruleSensor):
    # print (jsonresult)
    # print(dataRule)
    # print(value)
    dataStr=''
    i=0
    # while i<10:
    while i<len(jsonresult[value]):
        keyString='byteSize'
        count=jsonresult[value][i][keyString]*2
        # print (count)
        ruleKeyStr=jsonresult[value][i]['storeName']
        # print (ruleKeyStr)
        # if ruleKeyStr =='a'or ruleKeyStr=='b'or ruleKeyStr=='c' or ruleKeyStr=='d'or ruleKeyStr=='e' or ruleKeyStr=='1fs':
        if ruleKeyStr in ['a','b','c','d','e','1fs','g']:
            #a取数据传输类型
            if ruleKeyStr=='a':
                dataStr=dataStr+transtype
                print ('传输类型为%s'%dataStr)
            #sensor号
            elif ruleKeyStr=='b':
                dataStr=dataStr+ruleSensor
                print ('sensor为%s'%dataStr)
            #累计工作时间
            elif ruleKeyStr=='c':
                totalStr='2019-11-08 17:08:00'
                timeArray = time.strptime(totalStr, "%Y-%m-%d %H:%M:%S")
                timeStamp = int(time.mktime(timeArray))
                # print (timeStamp)
                totalStr1=hex(timeStamp)
                # print (totalStr1)
                # #若为小端则需要倒序编码
                if jsonresult[value][i]['byteOrder']==2:
                    totalStr2=hexdatasort(totalStr1)
                    # print (totalStr2)
                    # dataStr=Insetzero(jsonresult[value][i]['byteOrder'],totalStr2,dataStr,count)
                    dataStr=dataStr+totalStr2
                else:
                    dataStr=dataStr+totalStr1

                print ('累计工作时间为%s'%dataStr)
            #本次上电时间d
            elif ruleKeyStr=='d':
                totalStr='2019-11-08 17:08:00'
                timeArray = time.strptime(totalStr, "%Y-%m-%d %H:%M:%S")
                timeStamp = int(time.mktime(timeArray))
                # print (timeStamp)
                totalStr1=hex(timeStamp)
                # print (totalStr1)
                # #若为小端则需要倒序编码
                if jsonresult[value][i]['byteOrder']==2:
                    totalStr2=hexdatasort(totalStr1)
                    # print (totalStr2)
                    # dataStr=Insetzero(jsonresult[value][i]['byteOrder'],totalStr2,dataStr,count)
                    dataStr=dataStr+totalStr2
                else:
                    dataStr=dataStr+totalStr1
                print ('本次上电时间为%s'%dataStr)
            #偏移时间e,累计工作时间写死，这样每次当前时间-累计工作时间，就是偏移时间，c+e
            elif ruleKeyStr=='e':
                totalStr='2019-11-08 17:08:00'
                totalStr1=time.strftime('%Y-%m-%d %H:%M:%S')
                timeArray = time.strptime(totalStr, "%Y-%m-%d %H:%M:%S")
                timeArray1 = time.strptime(totalStr1, "%Y-%m-%d %H:%M:%S")
                timeStamp = int(time.mktime(timeArray))
                timeStamp1= int(time.mktime(timeArray1))
                print ('偏移时间时间戳为%s'%(timeStamp1-timeStamp))
                totalStr2=hex(timeStamp1-timeStamp)
                #补0显示
                dataStr=Insetzero(jsonresult[value][i]['byteOrder'],totalStr2,dataStr,count)
                print ('偏移时间为%s'%dataStr)
                # # 若为小端则需要倒序编码
                # if jsonresult[value][i]['byteOrder']==2:
                #     totalStr3=hexdatasort(totalStr2)
                #     print (totalStr3)
                #     # print(type(totalStr3))
                #     # print (len(totalStr3))
                #     totalStr4=list(totalStr3)
                #     j=0
                #     if len(totalStr4)<8:
                #         while j<8-len(totalStr3):
                #             # print(totalStr4)
                #             totalStr4.append('0')
                #             # print(totalStr4)
                #             j=j+1
                #         # print (totalStr4)
                #         # print (type(totalStr4))
                #         totalStr5=''.join(totalStr4)
                #         dataStr=dataStr+totalStr5
                #         print ('偏移时间为%s'%dataStr)
                #         # break
                #     else:
                #         dataStr=dataStr+totalStr3
                #         print ('偏移时间为%s'%dataStr)
                # else:
                #     totalStr4=list(totalStr2)
                #     j=0
                #     if len(totalStr2)<8:
                #         while j<8-len(totalStr2):
                #             # print(totalStr4)
                #             totalStr4.append('0')
                #             # print(totalStr4)
                #             j=j+1
                #         # print (totalStr4)
                #         # print (type(totalStr4))
                #         totalStr5=''.join(totalStr4)
                #         dataStr=dataStr+totalStr5
                #         print ('偏移时间为%s'%dataStr)
                #         # break
                #     else:
                #         dataStr=dataStr+totalStr2
                #         print ('偏移时间为%s'%dataStr)
            elif ruleKeyStr=='g':
                # print (type(dataRule))
                #字符串转化为十六进制
                totalStr=strintohex(dataRule)
                print ('逆变器sn转为十六进制为%s'%totalStr)
                dataStr=Insetzero(jsonresult[value][i]['byteOrder'],totalStr,dataStr,count)
                # # #若为小端则需要倒序编码
                # if jsonresult[value][i]['byteOrder']==2:
                #     totalStr2=hexdatasort(totalStr)
                #     print (totalStr1)
                # dataStr=dataStr+totalStr2
                print ('设备sn号为%s'%dataStr)
            #ifs的处理
            else:
                totalStr=''
                dataStr=dataStr+totalStr
                # print (dataStr)
        else:
            totalStr=getRadom4HexString(count)
            dataStr=dataStr+totalStr
            # print ('十六进制为%s'%dataStr)
        i=i+1
        # datastr=dataStr+
    print('数据域为%s'%dataStr)
    return dataStr

# #模拟流水号
# def LS(num):
#     if num<256:
#         servernum=i
#         dataloggernum=i
#     else:
#     return servernum,dataloggernum
# getRadom4HexString(16)
# hexsort('6b4a1c39')
#模拟发送原始数据
def creatAndSendData():
    #sensor号
    # sensor ='2703'
    # sensor ='E02B'
    # sensor ='E050'
    # sensor ='0505'
    sensor ='2501'

    #数据帧类型
    dataname='数据帧'
    #帧传输类型
    dataTransName='普通实时'
    #设备名称
    deviceName='逆变器'
    dataRule={"za":"1800012805","a":"01","g":"test1800012805"}
    # #功能测试环境
    # Ip='10.42.6.41'
    # port='10000'
    #开发环境
    Ip='access.dev.igen'
    port='10000'
    #Ip=192.168.30.44
    #是否模拟设备5分钟发一次数据
    isMockDevice=True
    #倒序排列
    ruleSensor=sensor[2]+sensor[3]+sensor[0]+sensor[1]
    # //获取数据类型
    datatype=getDataType(dataname)
    # //获取数据传输类型
    transtype=getDataTransType(dataTransName)
    # //获取设备大类
    devicetype=getDeviceType(deviceName)
    ruleCode="01"+datatype+transtype+ruleSensor
    # print (ruleSensor)
    # print (ruleCode)
    connect=sqlconnect()
    sql="select context from data_structure_rule t where protocol_num='%s'"%ruleCode
    connect.execute(sql)
    result=connect.fetchall()
    print (result)
    # print (type(result))
    jsonresult=json.loads(result[0][0])
    print ('解析json为%s'%jsonresult)
    # print (type(jsonresult))
    #首位
    headHexStr="A5"
    #数据域长度十进制
    lensize=getwantValueFromJsonAddStringExcludeStr(jsonresult,"pdk_dataField",'byteSize','1fs','storeName')
    print ('数据域长度十进制为%s'%lensize)
    #数据域长十六进制
    #将ox去除
    lenHexStr=hex(lensize)[-2:]
    # print (lenHexStr)
    # print (len(lenHexStr))
    if len(lenHexStr)==1:
        lenHexStr2=lenHexStr+'000'
        print ('数据域长度十六进制为%s'%lenHexStr2)
    elif len(lenHexStr)==2:
        lenHexStr2=lenHexStr+'00'
        print ('数据域长度十六进制为%s'%lenHexStr2)
    elif len(lenHexStr)==3:
        lenHexStr2=lenHexStr+'0'
        print ('数据域长度十六进制为%s'%lenHexStr2)
    else:
        lenHexStr2=lenHexStr
        print ('数据域长度十六进制为%s'%lenHexStr2)
    #控制位数据1
    c1HexStr='10'
    #如果是精简实时数据和精简历史是Gprs和以太网是短连接，wifi是长连接
    #控制位数据2
    if dataRule['a']!=11 and dataRule['a']!=91:
        c2Int="01000010"
        #将二进制转化为十六进制
        c2HexStr=hex(int(c2Int,base=2))[-2:]
    else:
        c2Int='01100010'
        c2HexStr=hex(int(c2Int,base=2))[-2:]
    print ('控制位为%s'%c2HexStr)
    serverls=0
    devicels=0
    # #模拟流水号
    #服务器流水号
    serverlsHexStr='01'
    #采集器流水号
    devicelsHexStr='03'
    # #
    lenAndCHexStr=lenHexStr2+c1HexStr+c2HexStr+serverlsHexStr+devicelsHexStr
    print ('数据域长度+控制位+流水号为%s'%lenAndCHexStr)
    #采集器sn
    dataloggerStr1=dataRule['za']
    print ('采集器sn为%s'%dataloggerStr1)
    #将十进制转化为十六进制
    dataloggerStr2=hex(int(dataloggerStr1))
    print('采集器sn转为十六进制为%s'%dataloggerStr2)
    #倒序排列
    dataloggerStr=hexdatasort(dataloggerStr2)
    print ('采集器转化为十六进制倒序为%s'%dataloggerStr)
    #数据域
    DataStr=createDataBaseRule(dataRule,jsonresult,'pdk_dataField',transtype,ruleSensor)
    DataStr=lenAndCHexStr+dataloggerStr+DataStr
    print ('参与检验的数据为%s'%DataStr)
    #构造校验位
    checkBitStr=Checksum(DataStr)
    #尾部
    endHexStr="15"
    #构造原始数据,全部大写显示
    DataStr=(headHexStr+DataStr+checkBitStr+endHexStr).upper()
    print('最后模拟数据为%s'%DataStr)
    return DataStr
# creatAndSendData()
def send_timer():
    data=creatAndSendData()
    #二期测试环境
    # target_host = '192.168.30.44'
    # target_port = 10000
    # #三期功能测试环境
    # target_host = '10.42.6.41'
    # target_port = 10000
    #开发环境
    target_host = 'access.dev.igen'
    target_port = 10000
    #建立一个socket对象,AF_INET说明将使用标准的IPv4地址或主机名，SOCK_STREAM说明是一个TCP客户端
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #连接到服务器
    client.connect((target_host, target_port))
    a=bytes().fromhex(data)
    #a=data.decode('hex')  #bytes转为十六进制
    print (a)
    # print type(a)
    client.send(a)
    print (datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"))
    #接收数据
    #response = client.recv(4096)
    #print(response)
    # global timer
    timer=threading.Timer(300,send_timer)
    timer.start()
timer=threading.Timer(1,send_timer)
timer.start()










