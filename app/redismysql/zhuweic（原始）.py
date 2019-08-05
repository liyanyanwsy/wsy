# -*- coding:utf-8 -*-
import MySQLdb

# def data_structure_rule():
#     try:
#         conn = MySQLdb.connect(host='web.solarmanpv.com', user='readonly', passwd='yingZHEN123', db='solarman2',
#                                port=33306, charset='utf8')
#         cur = conn.cursor()
#         with open("C:\\Users\\lyy\\Desktop\\test.txt", "r") as f:
#             s = f.readlines()
#         for sen in s:
#             sen1 = sen[2:4]
#             sen2 = sen[0:2]
#             sensor = sen2 + sen1
#             num = sen1 + sen2
#             protocol_num = '01__01' + num
#             protocol_num1 = '01__11' + num
#             protocol_num2 = '01__21' + num
#             if cur.execute("SELECT * FROM data_structure_rule WHERE protocol_num LIKE %s", protocol_num):
#                 re = cur.fetchall()
#                 for r in re:
#                     print "Sensor：" + sensor + ",普实帧：" + r[2]
#             elif cur.execute("SELECT * FROM data_structure_rule WHERE protocol_num LIKE %s", protocol_num1):
#                 re = cur.fetchall()
#                 for r in re:
#                     print "Sensor：" + sensor + ",精实帧：" + r[2]
#                     if cur.execute("SELECT * FROM data_structure_rule WHERE protocol_num LIKE %s", protocol_num2):
#                         re1 = cur.fetchall()
#                         for r1 in re1:
#                             print "Sensor：" + sensor + ",信息帧：" + r1[2]
#                     else:
#                         print "Sensor：" + sensor + ",无信息帧"
#             else:
#                 print "Sensor：" + sensor + ",无普通实时数据帧和精简实时数据帧"
#         cur.close()
#         conn.close()
#
#     except Exception, e:
#         print e


def datalogger_insert():
    try:
        conn = MySQLdb.connect(host='192.168.1.53', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
                               port=3306, charset='utf8')
        cur = conn.cursor()
        with open("C:\\Users\\lyy\\Desktop\\python\\xuexi\\sn.txt", "r") as f:
            s = f.readlines()

        for sn in s:
            cur.execute("INSERT INTO datalogger (sn,create_date,cluster_no,hardware_version,wifi_version,material_num,mcu_major_version,factory_date) "
                        "VALUES (%s,'2018-04-18 12:01:00','1','','','','','2018-04-18 12:01:00')", sn.strip('\n'))
            conn.commit()
            if cur.execute("SELECT * FROM datalogger WHERE sn = %s", sn.strip('\n')):
                re = cur.fetchall()
                if cur.rowcount > 0:
                    print sn.strip('\n') + ",已入datalogger表"
                else:
                    print sn.strip('\n') + ",入库失败"
            cur.execute("insert into b_company_device (datalogger_sn,device_id,device_type,company_id,grand_level,distributor_level,status,create_date,update_time,is_bind,is_grant,is_reg,original_company_id) "
                        "values (%s,0,99,1,0,null,1,'2018-04-18 12:01:00','2018-04-18 12:01:00',1,1,0,null)", sn.strip('\n'))
            conn.commit()
            if cur.execute("SELECT * FROM b_company_device WHERE datalogger_sn = %s", sn.strip('\n')):
                re = cur.fetchall()
                if cur.rowcount > 0:
                    print sn.strip('\n') + ",已入b_company_device表"
                else:
                    print sn.strip('\n') + ",入库失败"
        cur.close()
        conn.close()

    except Exception, e:
        print e
if __name__ == "__main__":
    datalogger_insert()