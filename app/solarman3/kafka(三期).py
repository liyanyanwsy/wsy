#encoding:utf-8
#向kafka发送数据进行测试
import json
from kafka import SimpleProducer
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.client import KafkaClient
from kafka.errors import KafkaError
import  datetime as d
import time
topic = 'common_data_history'
msg1= { "zk" : "1" , "za" : "705009450" , "a" : "01" , "b" : "0505" , "c" : "5696749" , "d" : "10021" , "e" : "1542697991" , "f" : "0001" , "ah" : "3318" , "g" : "110F50187200010" , "1df" : "27.50" , "1a" : "38" , "1b" : "3.90" , "1j" : "0.00" , "1k" : "0.00" , "1ai" : "0.60" , "1aj" : "0.00" , "1ak" : "0.00" , "1af" : "244.80" , "1ag" : "0.00" , "1ah" : "0.00" , "1ar" : "50.02" , "1ao" : "0" , "1bd" : "0.00" , "1bc" : "406.00" , "_" : "0000" , "ap" : "0000" , "aq" : "0000" , "ar" : "0000" , "as" : "0000" , "at" : "0000" , "1c" : "0.00" , "1l" : "0.00" , "1d" : "0.00" , "1m" : "0.00" , "1ab" : "0" , "1be" : "93" , "1ru" : "104" , "1aw" : "2.70" , "1bf" : "93" , "1lf" : "29" , "1rw" : "0" , "1br" : "293" , "1bs" : "293" , "1bt" : "1000" , "1vw" : "19" , "1vx" : "1" , "1vy" : "26" , "1vz" : "6" , "1wa" : "46" , "1wb" : "31" , "1bj" : "245.40" , "1bm" : "2.17" , "2tp" : "-133" , "2qf" : "1" , "1cr" : "49.20" , "1cs" : "1.40" , "1ff" : "1" , "2ve" : "244.80" , "1cv" : "22" , "2tm" : "100" , "2tt" : "49.14" , "2tu" : "0.40" , "2tv" : "20.00" , "2tw" : "50.00" , "1fs" : "" , "1cj" : "0" , "2vg" : "0" , "1cx" : "0" , "1cz" : "0.00" , "2vc" : "0.00" , "1cy" : "0" , "1da" : "0.00" , "2vd" : "0.00" , "1bv" : "0" , "1bx" : "0.00" , "1bu" : "0" , "1bw" : "0.00" , "1cn" : "0" , "1co" : "0.00" , "2vb" : "0.00" , "1gr" : "00F5" , "1ki" : "000F" , "1sm" : "000F" , "1ll" : "0001" , "zh" : "server52:10000" , "zi" : "02" , "zg" : "40,78" , "zb" : "A5E100104240782A97052A010505EDEC56002527000007B4F35B0100F60C000031313046353031383732303030313020130126002700000000000600000000009009000000008A130000000000000000DC0F0000000000000107000000000000000000000000000000000000000000005D000000680000001B005D0000001D0000002501000025010000E803130001001A0006002E001F009609D9007BFFFFFF0100EC010E000100900906001600640032130400C800F4010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000F5000F000F0001004F15" , "zc" : "192.168.2.116:52977" , "zd" : "1548394957" , "ze" : "1548394960" , "zf" : "100683953" , "zl" : "0" , "a0" : 1}
print msg1
print type(msg1)

#time1=d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
# print time1
def Timestamp():
    #日期转化为对应的时间戳
    # time1='2019-01-25 15:24:00'
    # print time1
    # print type(time1)
    time1=d.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
    print time1
    # 转为时间数组
    timeArray = time.strptime(time1, "%Y.%m.%d-%H:%M:%S")
    # timeArray = time.strptime(time1, "%Y-%m-%d %H:%M:%S")
    # otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
    print timeArray
    #timeArray可以调用tm_year等
    print timeArray.tm_year
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    print timeStamp
    #替换msg1中e字段对应的时间戳,从而使发送的数据是最新的。
    #打印出c字段的时间戳
    print msg1['c']
    # print type(msg1['c'])
    # print msg1['e']
    msg1['e']=int(timeStamp)-int(msg1['c'])
    print str(msg1['e'])
    # print type(str(msg1['e']))
    print msg1
    print type(msg1)
    return  timeStamp
# print msg1[0]
# print type(msg1[0])
msg2=json.dumps(msg1)
mess={"deviceId":msg1['zf'],"timestamp":str(Timestamp()),"seriaNum":"","json":msg2,"type":"01"}
print mess
print type(mess)
# 主题名称
def Producer():
    # producer = KafkaProducer(bootstrap_servers ='10.42.2.92:9092')
    producer = KafkaProducer(bootstrap_servers='10.42.2.92:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    print('send to kafka start!')
    # msg = json.dumps(msg1)
    # print type(msg)
    # msg = json.dumps(mess)
    # print type(msg)
    # producer.send(topic, msg.encode())
    producer.send(topic, mess)
    # producer.send(topic, msg1)
    time.sleep(1)
    print('send to kafka finished!')
    producer.close()


def Consumer():
    consumer=KafkaConsumer(topic,group_id='consumer-sunny20190129',bootstrap_servers=['10.42.2.92:9092'])
    for message in consumer:
        print message
        print type(message)
        # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key,message.value))
        print "%s:%d:%d: key=%s value=%s" %(message.topic,message.partition,message.offset,message.key,message.value)
        break



Timestamp()
Producer()
Consumer()







a=((1, 1), (3, 1), (7, 1), (1, 1), (3, 1), (7, 1), (0, 0), (0, 0), (0, 0), (51, 2), (74, 3), (83, 3), (104, 4), (0, 0), (0, 0), (0, 0), (176, 8), (187, 9), (202, 9), (0, 0), (0, 0), (0, 0), (252, 9), (291, 12), (300, 11), (0, 0), (0, 0), (0, 0), (151, 12), (122, 16), (410, 14), (0, 0), (0, 0), (0, 0), (455, 17), (171, 22), (562, 8), (0, 0), (0, 0), (0, 0), (568, 19), (593, 20), (221, 17), (0, 0), (0, 0), (0, 0), (256, 24), (148, 9), (168, 8), (0, 0), (0, 0), (0, 0), (360, 14), (350, 25), (241, 25), (0, 0), (0, 0), (0, 0), (658, 32), (658, 32), (698, 33), (0, 0), (0, 0), (0, 0), (724, 16), (678, 33), (714, 30), (0, 0), (0, 0), (0, 0), (534, 27), (754, 30), (146, 22), (0, 0), (0, 0), (0, 0), (405, 25), (197, 16), (268, 12), (0, 0), (0, 0), (0, 0), (727, 32), (245, 32), (724, 27), (0, 0), (0, 0), (0, 0), (222, 25), (249, 22), (416, 28), (0, 0), (0, 0), (0, 0), (586, 28), (632, 30), (592, 24), (0, 0), (0, 0), (0, 0), (546, 27), (526, 25), (509, 25), (0, 0), (0, 0), (0, 0), (499, 19), (455, 24), (498, 22), (0, 0), (0, 0), (0, 0), (369, 16), (347, 17), (346, 16), (0, 0), (0, 0), (0, 0), (273, 14), (274, 12), (236, 12), (0, 0), (0, 0), (0, 0), (42, 4), (144, 8), (124, 6), (0, 0), (0, 0), (0, 0), (67, 3), (56, 1), (42, 3), (0, 0), (0, 0), (0, 0), (13, 1), (10, 1), (6, 1), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0))
#
#
#
# # deviceId=msg1['zf']
# # timestamp=timeStamp
# # seriaNum=1A
# # json=
# # type=01



