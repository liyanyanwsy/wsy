# -*- coding:utf-8 -*-
import MySQLdb
#先查询是否入库，如果未入库，进行入库操作。
def datalogger_insert():
    try:
        conn = MySQLdb.connect(host='192.168.1.53', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
                               port=3306, charset='utf8')
        cur = conn.cursor()
        with open("D:\\study\\python\\xuexi\sn.txt", "r") as f:
            s = f.readlines()
            print
        for sn in s:
            # print sn
            # print sn.strip('\n')
            #%s需要加''
            #需要先查询该sn有没有进行入库操作

            cur.execute("SELECT * FROM datalogger WHERE sn = '%s'" %(sn.strip('\n')))
            re = cur.fetchall()
            if cur.rowcount>0:
                print sn.strip('\n') + ",已入datalogger表,不需要重复入库"
            #为入库进行入库操作
            else:
                cur.execute("INSERT INTO datalogger (sn,create_date,cluster_no,hardware_version,wifi_version,material_num,mcu_major_version,factory_date) "
                            "VALUES ('%s','2018-04-18 12:01:00','1','','','','','2018-04-18 12:01:00')" %(sn.strip('\n')))
                conn.commit()
                if cur.rowcount>0:
                    print sn.strip('\n') + ",已入datalogger表"

            cur.execute("SELECT * FROM b_company_device WHERE datalogger_sn = '%s'" %(sn.strip('\n')))
            re = cur.fetchall()
            if cur.rowcount > 0:
                print sn.strip('\n') + ",已入b_company_device表，不需要重复入库"
            else:
                cur.execute("insert into b_company_device (datalogger_sn,device_id,device_type,company_id,grand_level,distributor_level,status,create_date,update_time,is_bind,is_grant,is_reg,original_company_id) "
                             "values ('%s',0,99,1,0,null,1,'2018-04-18 12:01:00','2018-04-18 12:01:00',1,1,0,null)" %(sn.strip('\n')))
                conn.commit()
                if cur.rowcount>0:
                    print sn.strip('\n') + ",已入b_company_device表"
        cur.close()
        conn.close()

    except Exception, e:
        print e
if __name__ == "__main__":
    datalogger_insert()

