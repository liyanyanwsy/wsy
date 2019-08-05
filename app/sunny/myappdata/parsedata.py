#encoding:utf-8
import paramiko
import json
#封装下载dataflow1
def download():
    try:
        hostname='192.168.1.52'
        port=22
        username='root'
        password='123456'
        dir_path='/data/apps/log/parse/dataflow'
        loc_path='C:/Users/lyy/Desktop/'
        src=dir_path+'/'+'dataflow1.log'
        des=loc_path+'/'+'dataflow1.log'
        scp=paramiko.Transport((hostname,port))
        scp.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(scp)
        sftp.get(src,des)
        scp.close()
    except Exception,e:
        print e
download()
#打开文件，并对文件进行处理
with open("C:/Users/lyy/Desktop/dataflow1.log", "r") as f:
    lines=f.readlines()
    data=[]
    for line in lines:
        #循环取txt中的行，去除空白
        linedata=line.strip()
        # print linedata
        # print type(linedata)
        # # print line
        #将列表转为字符串进行处理
        str2=str(linedata)
        # print type(str2)
        # print str2
        #从后往前查找对应信息
        str1 = 'E025'
        # print type(str1)
        # print str2.rfind(str1)
        if str2.rfind(str1)!= -1:
            #截取字符串
            str4=str2[29:]
            str5=str4.rstrip('\']')
            # print str4
            # print str5
            # print type(str4)
            # linedata3=eval(str4)
            # print linedata3
            # print type(linedata3)
            # print type(str4)
            # print type(linedata1)
            # print linedata1
            # 存入列表中
            data.append(str5)
f.close()

#     else:
#         print None
# print data
#取最新的一条数据
data1=data[0]
print data1
# print type(data1)
#转为字典格式
data2=json.loads(data1)
print data2
# print type(data2)
status=data2['1ez']
ipv1=data2['1a']
ipv2=data2['1b']
vpv1=data2['1j']
vpv2=data2['1k']
ppv1=data2['1s']
ppv2=data2['1t']
iacr=data2['1af']
iacs=data2['1ag']
iact=data2['1ah']
vacr=data2['1ai']
vacs=data2['1aj']
vact=data2['1ak']
pacr=data2['1al']
pacs=data2['1am']
pact=data2['1an']
ppv=data2['1ab']
pac=data2['1ao']
powerToday=data2['1bd']
powerTotal=data2['1az']
temperature=data2['1df']
fac=data2['1ar']
pf=data2['1au']
faultType=
timeTotal=data2['1eo']
ipmTemperature=data2['1dr']
epv1Today=data2['2kj']
epv1Total=data2['2km']
epv2Today=data2['2kk']
epv2Total=data2['2kn']
epvTotal=data2['1bc']
eRacToday=data2['4py']
eRacTotal=data2['2sr']
pBusVoltage=data2['1jx']
nBusVoltage=data2['1jy']

vString1=data2['1we']
vString2=data2['1wf']
vString3=data2['1wg']
vString4=data2['1wh']
vString5=data2['1wi']
vString6=data2['1wj']
vString7=data2['1wk']
vString8=data2['1wl']
currentString1=data2['1wo']
currentString2=data2['1wp']
currentString3=data2['1wq']
currentString4=data2['1wr']
currentString5=data2['1ws']
currentString6=data2['1wt']
currentString7=data2['1wu']
currentString8=data2['1wv']


import json as j
import redis as r
hostName = '192.168.1.58'
port = 6379
pool = r.ConnectionPool(host=hostName, port=port)
redis = r.Redis(connection_pool=pool)
jsonresult = redis.hget("dv:100824294","_d")
_d = j.loads(jsonresult)
statusredis=_d['1ez']
ipv1redis=_d['1a']
ipv2redis=_d['1b']
vpv1redis=_d['1j']
vpv2redis=_d['1k']
ppv1redis=_d['1s']
ppv2redis=_d['1t']
iacrredis=_d['1af']
iacsredis=_d['1ag']
iactredis=_d['1ah']
vacrredis=_d['1ai']
vacsredis=_d['1aj']
vactredis=_d['1ak']
pacrredis=_d['1al']
pacsredis=_d['1am']
pactredis=_d['1an']
ppvredis=_d['1ab']
pacredis=_d['1ao']
powerTodayredis=_d['1bd']
powerTotalredis=_d['1az']
temperatureredis=_d['1df']
facredis=_d['1ar']
pfredis=_d['1au']
faultTyperedis=
timeTotalredis=_d['1eo']
ipmTemperatureredis=_d['1dr']
epv1Todayredis=_d['2kj']
epv1Totalredis=_d['2km']
epv2Todayredis=_d['2kk']
epv2Totalredis=_d['2kn']
epvTotalredis=_d['1bc']
eRacTodayredis=_d['4py']
eRacTotalredis=_d['2sr']
pBusVoltageredis=_d['1jx']
nBusVoltageredis=_d['1jy']

vString1redis=_d['1we']
vString2redis=_d['1wf']
vString3redis=_d['1wg']
vString4redis=_d['1wh']
vString5redis=_d['1wi']
vString6redis=_d['1wj']
vString7redis=_d['1wk']
vString8redis=_d['1wl']
currentString1redis=_d['1wo']
currentString2redis=_d['1wp']
currentString3redis=_d['1wq']
currentString4redis=_d['1wr']
currentString5redis=_d['1ws']
currentString6redis=_d['1wt']
currentString7redis=_d['1wu']
currentString8redis=_d['1wv']


if status==statusredis:
    print 'pass'
elif ipv1==ipv1redis:
    print 'pass'



else:

