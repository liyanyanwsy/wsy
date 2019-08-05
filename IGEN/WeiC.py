# -*- coding:utf-8 -*-

# import unittest
# import HTMLTestRunner
import time
import json
import MySQLdb
from Functions import Function
import xlrd
import logging
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# import Function


def run_test():
    Function.run_initialze()
    time.sleep(2)
    Function.htmlreport_Run()


def conn_db():
    try:
        conn = MySQLdb.connect(host='192.168.1.53', user='root', passwd='123456', db='solarman2', port=3306, charset='utf8')
        cur = conn.cursor()
        cur.execute('SELECT * FROM error_code WHERE description IS NOT NULL AND is_del = 0')

        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        result_file = "C:\Users\lyy\Desktop\python\IGEN\\" + now + "_b.json"
        data = cur.fetchall()
        with open(result_file, "a") as fo:
            try:
                for i in data:
                    d = i[3]
                    jsob = json.dumps(d)
                    print (jsob)
                    fo.writelines(jsob + '\n')
            except:
                print ("error")
                fo.writelines("error" + '\n')
        cur.close()
        conn.close()
    except:
        print(sys.exc_info())


# 根据采集器号批量查询采集器的信号强度
def search_signal():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    result_file = "C:\\Users\\IGEN\\Desktop\\Mytest\\IGEN\\" + now + "_b.txt"
    json_file = "C:\\Users\\IGEN\\Desktop\\Mytest\\IGEN\\json1"
    # fo = open(result_file + "_" + now, "a")
    with open(result_file, "a") as fo, open(json_file, 'r') as f:
        lists = f.readlines()
        for i in lists:
            try:
                data = json.loads(i)
                print (data['za'], data['l'])
                fo.writelines(data['za'] + '  ' + data['l'] + '\n')
            except Exception:
                print ('error')
                fo.writelines('error ' + '\n')


# 查找excel表中每一行有区别的记录,每行一对一关系
def search_excel():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    result_file = "C:\\Users\\IGEN\\Desktop\\Mytest\\IGEN\\" + now + "_c.txt"
    xlrd_file = r'C:\Users\IGEN\Desktop\test.xlsx'
    book = xlrd.open_workbook(xlrd_file)
    test_sheet = book.sheet_by_index(3)
    rows = test_sheet.get_rows()
    with open(result_file, 'a') as f:
        for row in rows:
            # print row
            if row[0].value == row[1].value:
                pass
            else:
                if row[0].value == '':
                    row[0].value = 'none'
                if row[1].value == '':
                    row[1].value = 'none'
                print row[0].value, row[1].value
                f.writelines(str(row[0].value) + ',' + str(row[1].value) + '\n')


# 查找excel表中两列有区别的记录,无序
def search_excel_difference():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    result_file = "C:\\Users\\IGEN\\Desktop\\Mytest\\IGEN\\" + now + "_d.txt"
    xlrd_file = r'C:\Users\IGEN\Desktop\zhanyuan12@163.com.xlsx'
    book = xlrd.open_workbook(xlrd_file)
    test_sheet = book.sheet_by_index(0)
    cols1 = test_sheet.col_values(0)
    cols2 = test_sheet.col_values(1)
    with open(result_file, 'a') as f:
        d1 = list(set(cols1).difference(set(cols2)))
        for i in range(len(d1)):
            print d1[i]
            f.writelines(str(d1[i]) + '\n')
        d2 = list(set(cols2).difference(set(cols1)))
        for j in range(len(d2)):
            print d2[j]
            f.writelines(str(d2[j]) + '\n')


def gin_long_log(logger):

    old_plant_id_list = []
    new_plant_id_list = []
    gateway_sn_list = []
    data_logger_sn = []
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    result_user = "C:\\Users\\IGEN\\Desktop\\Mytest\\IGEN\\" + now + "_1to2_user.txt"
    result_plant = "C:\\Users\\IGEN\\Desktop\\Mytest\\IGEN\\" + now + "_1to2_plant.txt"
    try:
        conn1 = MySQLdb.connect(host='47.88.5.119', user='readonly', passwd='yingZHEN0.0', db='solarman', port=3306, charset='utf8')
        cur1 = conn1.cursor()
        conn2 = MySQLdb.connect(host='192.168.1.53', user='root', passwd='123456', db='solarman2', port=3306, charset='utf8')
        cur2 = conn2.cursor()
        with open("C:\\Users\\IGEN\\Desktop\\Mytest\\IGEN\\test.txt", "r") as f:
            # while True:
            old_uids = f.readlines()
            logger.info("************************************************************************************************")
            logger.info(old_uids)

        for old_uid in old_uids:
            cur1.execute("SELECT * FROM users WHERE id = %s", old_uid)
            old_user = cur1.fetchall()
            # 判断是否为终端用户
            if old_user[0][5] == 5:

                # 验证终端用户是否迁移
                if cur2.execute("SELECT * FROM user_source WHERE old_uid = %s AND platform = 3", old_uid):
                    user_source = cur2.fetchall()
                    new_uid = user_source[0][7]
                    logger.info("********************************************************************************************")
                    logger.info("user_source:" + old_uid.strip('\n') + " (old_uid) " + "  ==>  " + str(new_uid) + " (new_uid), " + str(user_source[0][5]) + " (old_plants)")
                    if cur2.execute("SELECT * FROM user WHERE uid = %s", new_uid):
                        logger.info("old_uid:" + old_uid.strip('\n') + ", new_uid:" + str(new_uid) + ', 用户已迁移')

                        # 验证终端用户下电站是否迁移
                        cur1.execute("SELECT * FROM powerstations WHERE DecreaseSO2 = %s", old_user[0][1])
                        old_plant_id = cur1.fetchall()
                        old_plant_id_list.append(old_plant_id[0][0])
                        for i in old_plant_id_list:
                            if cur2.execute("SELECT * FROM plant_source WHERE old_plant_id = %s AND platform = 3", i):
                                plant_source = cur2.fetchall()
                                new_plant_id_list.append(plant_source[0][4])
                                logger.info("plant_source:(old_plant) " + str(old_plant_id_list) + "  ==>  " + str(new_plant_id_list) + " (new_plant)")

                                # 一期电站下的采集器
                                cur1.execute("SELECT * FROM gateways WHERE PowserStationId = %s", i)
                                station_id = cur1.fetchall()
                                gateway_sn_list.append(station_id[0][4])

                                for j in new_plant_id_list:
                                    if cur2.execute("SELECT * FROM plant WHERE plant_id = %s AND is_del = 0", j):
                                        logger.info("old_plant_id:" + str(old_plant_id_list) + ", new_plant_id:" + str(new_plant_id_list) + " 电站已迁移")

                                        # 验证电站下采集器和设备是否迁移
                                        for k in gateway_sn_list:
                                            if cur2.execute("SELECT * FROM group_entity WHERE group_id = %s AND entity_sn = %s AND is_del = 0", [j, k]):
                                                group_entity = cur2.fetchall()
                                                data_logger_sn.append(group_entity[0][3])
                                                logger.info("GatewaySN:" + str(gateway_sn_list) + ", Datalogger_SN;" + str(data_logger_sn) + "采集器已迁移")
                                            else:
                                                logger.warning("GatewaySN:" + str(gateway_sn_list) + ", Datalogger_SN;" + str(data_logger_sn) + "采集器在二期未被迁移")
                                        data_logger_sn[:] = []
                                    else:
                                        logger.warning("old_plant_id:" + str(old_plant_id_list) + ", new_plant_id:" + str(new_plant_id_list) + " 电站有迁移记录，但是电站在二期未被创建")

                                gateway_sn_list[:] = []

                                new_plant_id_list[:] = []

                            # 将没有迁移的电站写入文件
                            else:
                                with open(result_plant, "w") as fp:
                                    fp.writelines(str(i[0][0]) + '\n')
                                    logger.info("********************************************************************************************")
                                    logger.info(str(i[0][0]) + "该电站未迁移")

                            old_plant_id_list[:] = []

                # 将没有迁移的用户写入文件
                else:
                    with open(result_user, "a") as fu:
                        fu.writelines(str(old_user[0][0]) + '\n')
                        logger.info("********************************************************************************************")
                        logger.info(str(old_user[0][0]) + "该用户未迁移")

        cur1.close()
        conn1.close()
        cur2.close()
        conn2.close()
    except:
        # print(sys.exc_info())
        logger.info(sys.exc_info())


def gin_long_test():
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 创建一个logger
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(now + '_mig.log')
    fh.setLevel(logging.DEBUG)
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # 定义handler的输出格式
    formatter = logging.Formatter(
        '[%(asctime)s][%(levelname)s] ## %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    gin_long_log(logger)

if __name__ == '__main__':
    gin_long_test()
    # run_test()
    # search_signal()
    # conn_db(）
    # search_excel()
    # search_excel_difference()

