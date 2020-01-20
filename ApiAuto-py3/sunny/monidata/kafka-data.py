from kafka import KafkaConsumer
from kafka import KafkaProducer
import threading
import datetime,time
from src.common.excel_simple import ExcleHelper
data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\kafka.xls','data')
server_list = ["10.42.3.50:9092"]
i=1
while i<4:
    msg = {"Eyr1": "57658568", "SN1": "1800011516-Igen", "E_Puse_t1": "632", "Et_use1": "19532", "INV_T0": "-3118.10", "A_Fo1": "382.04", "t_dcg_n1": "19532", "HCIv1": "CAB0", "Et_ge0": "19532.00", "DC4": "5487.50", "DC2": "2831.80", "DC3": "5458.30", "DC1": "4026.60", "d": "1563242058", "Etdy_dcg1": "1638.00", "B_C1": "1.00", "DPi_t1": "1879189392", "Elast_mon1": "3501643680", "zl": "0", "zn": "0A2A07152710_5D3AA32C_00001C57", "PG_PF1": "16296", "zh": "10.42.7.21:10000", "zi": 2, "Etdy_use1": "1638.00", "zk": "0", "zd": "1564123948", "Pb_lo1": "51380", "zf": "200173598", "zg": "D2,D2", "P_CURVv1": "8544", "za": "1800011516", "AV2": "59.40", "zc": "192.168.60.146:61995", "zx": "0_0505_1", "zy": "PRC", "zt": "200173582", "zu": "true", "zv": 1564123949, "zq": "D0002", "zr": "18", "zs": "0505", "Emon1": "2293777285", "Eydy1": "1075.00", "mon1": "18071", "Etdy_cg1": "0.00", "tdy1": "19947", "Eydy_ge1": "3837.80", "DV4": "3648.20", "_": "8614", "zs1": "1285", "c": "881891", "a0": "1", "Etdy_pu1": "0.00", "DV3": "5155.90", "AV3": "5344.10", "BMS_B_Ccg_thd1": "3245.70", "BMS_B_V1": "640.23", "zo": "38640.7398020.55464", "BMS_B_C1": "2958.70", "hou1": "56092", "S_PGt1": "3291405940", "PG_C1": "282.81", "B_HLT_EXP1": "17896", "MODE_E_MNG1": "36092", "PM1": "0", "AVb1": "916.80", "AV1": "1799.50", "e": "1563242058", "t_gc_tdy1": "1638.00", "SS_CY1": "0", "f": "A3E6", "AC3": "943.90", "AC2": "3604.40", "AC1": "3030.80", "yr1": "54899", "DV1": "5536.60", "zj": "2", "DV2": "5533.80", "t_cg_n1": "0", "Q_PG1": "-1844366750", "DSPv1": "245B", "ah": "965", "B_left_cap1": "28", "APo_t1": "632", "B_ST1": "1", "zq1": "851970", "sec1": "12794", "PTCv1": "B5D6", "t_gc1": "19532", "ydy_dcg1": "312.40", "Etdy_ge1": "1638.00", "min1": "39889", "PG_V1": "367.70", "ydy_cg1": "4290.10", "a": "01", "B_V1": "632.00", "BMS_B_Cdcg_thd1": "3604.40", "Et_pu1": "0", "P_METER0": "632", "ERR3": "", "ERR2": "", "ERR1": "", "ERR5": "", "ERR4": ""}
    #当日发电量
    msg['Etdy_ge1']=data.get_value(i,'generationValue')
    #当日用电量
    msg['Etdy_use1']=data.get_value(i,'useValue')
    #当日并网量
    msg['t_gc_tdy1']=data.get_value(i,'gridValue')
    msg['Etdy_pu1']=data.get_value(i,'buyValue')
    #当日放电量
    msg['Etdy_dcg1']=data.get_value(i,'dischargeValue')
    msg['Etdy_cg1']=data.get_value(i,'chargeValue')
    # msg['zu']=true
    producer = KafkaProducer(bootstrap_servers=server_list, compression_type='gzip')
    print(type(msg))
    # bmsg = str(msg)
    # bmsg = str(msg).encode('utf-8')
    bmsg = bytes(str(msg).encode('utf-8'))
    # bmsg1=bmsg.decode('utf-8')
    print (type(bmsg))
    # print (type(bmsg1))
    producer.send('sunny', bmsg)
    consumer = KafkaConsumer('sunny', auto_offset_reset='earliest', bootstrap_servers=server_list)
    print (bmsg)
    print(consumer)
    print (datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"))
    i=i+1
    print (i)
    time.sleep(300)
# def fun_timer():
# # 生产者
#     global timer
#     i=1
#     print (i)
#     msg = {"Eyr1": "57658568", "SN1": "1800011516-Igen", "E_Puse_t1": "632", "Et_use1": "19532", "INV_T0": "-3118.10", "A_Fo1": "382.04", "t_dcg_n1": "19532", "HCIv1": "CAB0", "Et_ge0": "19532.00", "DC4": "5487.50", "DC2": "2831.80", "DC3": "5458.30", "DC1": "4026.60", "d": "1563242058", "Etdy_dcg1": "1638.00", "B_C1": "1.00", "DPi_t1": "1879189392", "Elast_mon1": "3501643680", "zl": "0", "zn": "0A2A07152710_5D3AA32C_00001C57", "PG_PF1": "16296", "zh": "10.42.7.21:10000", "zi": 2, "Etdy_use1": "1638.00", "zk": "0", "zd": "1564123948", "Pb_lo1": "51380", "zf": "200173598", "zg": "D2,D2", "P_CURVv1": "8544", "za": "1800011516", "AV2": "59.40", "zc": "192.168.60.146:61995", "zx": "0_0505_1", "zy": "PRC", "zt": "200173582", "zu": "true", "zv": 1564123949, "zq": "D0002", "zr": "18", "zs": "0505", "Emon1": "2293777285", "Eydy1": "1075.00", "mon1": "18071", "Etdy_cg1": "0.00", "tdy1": "19947", "Eydy_ge1": "3837.80", "DV4": "3648.20", "_": "8614", "zs1": "1285", "c": "881891", "a0": "1", "Etdy_pu1": "0.00", "DV3": "5155.90", "AV3": "5344.10", "BMS_B_Ccg_thd1": "3245.70", "BMS_B_V1": "640.23", "zo": "38640.7398020.55464", "BMS_B_C1": "2958.70", "hou1": "56092", "S_PGt1": "3291405940", "PG_C1": "282.81", "B_HLT_EXP1": "17896", "MODE_E_MNG1": "36092", "PM1": "0", "AVb1": "916.80", "AV1": "1799.50", "e": "1563242058", "t_gc_tdy1": "1638.00", "SS_CY1": "0", "f": "A3E6", "AC3": "943.90", "AC2": "3604.40", "AC1": "3030.80", "yr1": "54899", "DV1": "5536.60", "zj": "2", "DV2": "5533.80", "t_cg_n1": "0", "Q_PG1": "-1844366750", "DSPv1": "245B", "ah": "965", "B_left_cap1": "28", "APo_t1": "632", "B_ST1": "1", "zq1": "851970", "sec1": "12794", "PTCv1": "B5D6", "t_gc1": "19532", "ydy_dcg1": "312.40", "Etdy_ge1": "1638.00", "min1": "39889", "PG_V1": "367.70", "ydy_cg1": "4290.10", "a": "01", "B_V1": "632.00", "BMS_B_Cdcg_thd1": "3604.40", "Et_pu1": "0", "P_METER0": "632", "ERR3": "", "ERR2": "", "ERR1": "", "ERR5": "", "ERR4": ""}
#     #当日发电量
#     msg['Etdy_ge1']=data.get_value(i,'generationValue')
#     #当日用电量
#     msg['Etdy_use1']=data.get_value(i,'useValue')
#     #当日并网量
#     msg['t_gc_tdy1']=data.get_value(i,'gridValue')
#     msg['Etdy_pu1']=data.get_value(i,'buyValue')
#     #当日放电量
#     msg['Etdy_dcg1']=data.get_value(i,'dischargeValue')
#     msg['Etdy_cg1']=data.get_value(i,'chargeValue')
#     producer = KafkaProducer(bootstrap_servers=server_list, compression_type='gzip')
#     bmsg = bytes(str(msg).encode('utf-8'))
#     producer.send('sunny', bmsg)
#     consumer = KafkaConsumer('sunny', auto_offset_reset='earliest', bootstrap_servers=server_list)
#     print (msg)
#     print(consumer)
#     print (datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S"))
#     i=i+1
#     print (i)
#     # for msg in consumer:
#     #     print(msg)
#     timer=threading.Timer(300,fun_timer)
#     timer.start()
# timer=threading.Timer(1,fun_timer)
# timer.start()