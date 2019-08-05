# encoding:utf-8
import MySQLdb
def data_structure_rule():
    try:
        conn = MySQLdb.connect(host='192.168.1.53', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
                               port=3306, charset='utf8')
        # conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='debug',
        #                        port=3306, charset='utf8')

        # conn = MySQLdb.connect(host='web.solarmanpv.com', user='readonly', passwd='yingZHEN123', db='solarman2',
        #                        port=33306, charset='utf8')

        cur = conn.cursor()
        with open("C:\\Users\\lyy\\Desktop\\python\\xuexi\\test.txt", "r") as f:
            s = f.readlines()
        for sen in s:
            try:
                sen1 = sen[2:4]
                sen2 = sen[0:2]
                sensor = sen2 + sen1
                num = sen1 + sen2
                protocol_num = '01__01' + num
                protocol_num1 = '01__11' + num
                protocol_num2 = '01__21' + num
                #if cur.execute("SELECT * FROM data_structure_rule WHERE protocol_num LIKE %s",protocol_num):
                if cur.execute('SELECT * FROM data_structure_rule WHERE protocol_num LIKE "'+protocol_num+'"'):
                    re = cur.fetchall()
                    for r in re:
                        print "Sensor：" + sensor + ",普实帧:",
                        print r[2]
                #elif cur.execute("SELECT * FROM data_structure_rule WHERE protocol_num LIKE %s", protocol_num1):
                elif cur.execute('SELECT * FROM data_structure_rule WHERE protocol_num LIKE "'+protocol_num1+'"'):
                    re = cur.fetchall()
                    for r in re:
                        print "Sensor：" + sensor + ",精实帧：",
                        print r[2]
                        #if cur.execute("SELECT * FROM data_structure_rule WHERE protocol_num LIKE %s", protocol_num2):
                        if cur.execute('SELECT * FROM data_structure_rule WHERE protocol_num LIKE "'+protocol_num2+'"'):
                            re1 = cur.fetchall()
                            for r1 in re1:
                                print "Sensor：" + sensor + ",信息帧：",
                                print r1[2]
                        else:
                            print "Sensor：" + sensor + ",无信息帧"
                else:
                    print "Sensor：" + sensor + ",无普通实时数据帧和精简实时数据帧"
            except Exception,e:
                print e
        cur.close()
        conn.close()

    except Exception, e:
        print e


if __name__ == "__main__":
    data_structure_rule()
