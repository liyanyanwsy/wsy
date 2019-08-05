#coding:utf-8
from pykafka import KafkaClient
import json
import logging as log
log.basicConfig(level=log.DEBUG)
host='10.42.2.30:9092,10.42.2.31:9092,10.42.2.32:9092'
client = KafkaClient(hosts=host)
print("135")
topic = client.topics['common_data_history']
producer = topic.get_producer()
# 生产消息
msg_dict ={ "zk" : "1" , "za" : "2404750462" , "a" : "01" , "b" : "E025" , "c" : "174777417" , "d" : "15809" , "e" : "1361954543" , "f" : "0065" , "ah" : "16959" , "g" : "2404750462-02101" , "1bv" : "1" , "1aa" : "231.30" , "1ab" : "231.40" , "1ac" : "230.90" , "1ad" : "4.71" , "1ae" : "2.72" , "1af" : "2.59" , "1a" : "1859" , "1b" : "888" , "1c" : "506" , "1d" : "464" , "1e" : "1344" , "1f" : "616" , "1g" : "361" , "1h" : "366" , "1i" : "2314" , "1j" : "1090" , "1k" : "627" , "1l" : "596" , "1cb" : "0.80" , "1p" : "0.82" , "1q" : "0.81" , "1r" : "0.78" , "1m" : "50.02" , "1bk" : "21726.34" , "1bl" : "276.77" , "1bm" : "21449.57" , "1bn" : "0.00" , "1bo" : "0.00" , "1bp" : "9.54" , "1bq" : "8.06" , "1br" : "1.48" , "1bs" : "0.00" , "1bt" : "0.00" , "_" : "" , "2st" : "9929.25" , "2sw" : "0.00" , "2su" : "6179.06" , "2sx" : "0.00" , "2sv" : "5619.07" , "2sy" : "0.00" , "zh" : "47.88.8.200:10000" , "zi" : "02" , "zg" : "8F,3F" , "zb" : "A5BA0010428F3F7E94558F0125E049E46A0AC13D0000EFC62D5165003F420000323430343735303436322D3032313031010909090A09050000000000000000126A00000A9B00000A1B0000074300000378000001FA000001D00000054000000268000001690000016E0000090A0000044200000273000002540323032F0326030B138A002126DA00006C1D0020BABD0000000000000000000003BA000003260000009400000000000000000000000F269D0000000000096DB200000000000892F300000000D615" , "zc" : "223.104.255.202:32646" , "zd" : "1536731968" , "ze" : "1536731970" , "zf" : "100824294" , "zl" : "0" , "a0" : 5}
msg = json.dumps(msg_dict)
msg2=msg.encode('utf-8')
producer.produce(msg2)
print msg2
producer.stop()
#
# host1 = '10.42.2.32:9092'
# client1 = KafkaClient(hosts=host1)
# print client1.topics
#
# # 消费者
# topic1 = client.topics['common_data_history']
# consumer = topic.get_simple_consumer(consumer_group='streaming-etl-job', auto_commit_enable=True, consumer_id='streaming-etl-job')
# # for message in consumer:
# #     if message is not None:
# #         print message.offset, message.value
# if msg2 in consumer:
#     print msg2.offset,msg2.value

