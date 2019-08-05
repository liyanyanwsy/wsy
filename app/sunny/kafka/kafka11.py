# -*- coding: utf-8 -*-
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
def producer():
    producer = KafkaProducer(bootstrap_servers='10.42.3.50:9092')
    msg_dict={"t_gc1":"19532","BMS_B_Cdcg_thd1":"3604.40","ydy_cg1":"4290.10","Etdy_use1":"1638.00","Et_pu1":"0","B_left_cap1":"28","zs1":"1285","AVb1":"916.80","PG_C1":"282.81","BMS_B_Ccg_thd1":"3245.70","za":"1800011516","ah":"965","zc":"192.168.60.146:61995","zd":"1564123948","PG_PF1":"16296","min1":"39889","zf":"200173598","zg":"D2,D2","zh":"10.42.7.21:10000","zi":2,"zj":"2","zk":"0","zl":"0","zn":"0A2A07152710_5D3AA32C_00001C57","zo":"38640.7398020.55464","sec1":"12794","SN1":"1800011516-Igen","zq":"D0002","zr":"18","zs":"0505","yr1":"54899","DSPv1":"245B","APo_t1":"632","zt":"200173582","zu":"true","zv":1564123949,"zx":"0_0505_1","zy":"PRC","t_dcg_n1":"19532","Etdy_cg1":"0.00","AC1":"3030.80","AC2":"3604.40","AC3":"943.90","E_Puse_t1":"632","_":"8614","a":"01","c":"881891","d":"1563242058","e":"1563242058","f":"A3E6","BMS_B_V1":"640.23","Etdy_dcg1":"1638.00","PG_V1":"367.70","B_C1":"1.00","Pb_lo1":"51380","ydy_dcg1":"312.40","SS_CY1":"0","tdy1":"19947","Etdy_ge1":"1638.00","Et_use1":"19532","Q_PG1":"-1844366750","INV_T0":"-3118.10","P_METER0":"632","DC2":"2831.80","DC1":"4026.60","hou1":"56092","DC4":"5487.50","t_gc_tdy1":"1638.00","DC3":"5458.30","Emon1":"2293777285","mon1":"18071","AV1":"1799.50","AV2":"59.40","AV3":"5344.10","t_cg_n1":"0","B_V1":"632.00","A_Fo1":"382.04","BMS_B_C1":"2958.70","ERR1":"","ERR2":"","ERR3":"","ERR4":"","ERR5":"","B_ST1":"1","HCIv1":"CAB0","Elast_mon1":"3501643680","Eydy_ge1":"3837.80","Etdy_pu1":"0.00","PM1":"0","zq1":"851970","DV1":"5536.60","MODE_E_MNG1":"36092","DV3":"5155.90","DV2":"5533.80","S_PGt1":"3291405940","DV4":"3648.20","Eydy1":"1075.00","Et_ge0":"19532.00","a0":"1","Eyr1":"57658568","PTCv1":"B5D6","B_HLT_EXP1":"17896","P_CURVv1":"8544","DPi_t1":"1879189392"}
    msg= json.dumps(msg_dict)
    print (type(msg))
    producer.send('sunny',msg, partition=0)
    producer.close()
def consumer():
    consumer = KafkaConsumer('sunny', bootstrap_servers='10.42.3.50:9092')
    for msg in consumer:
        recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
        print (recv)

producer()
consumer()