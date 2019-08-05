import MySQLdb
def verify_code():
    try:
        conn = MySQLdb.connect(host='192.168.1.53', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
                               port=3306, charset='utf8')
        cur = conn.cursor()

        cur.execute("SELECT * FROM sys_verify_message WHERE verify_account='17798736289' ORDER BY udpate_time DESC LIMIT 1")
        re1 = cur.fetchall()
        print re1
        print type(re1)
        #a=list(re1[0])[2]
        a=re1[0][2]
        print a
        b=str(a)
        print b
        print len(b)
        cur.close()
        conn.close()
        print type(b)
        c=b[0]
        print c
        return a

    except Exception,e:
        print e
verify_code()

e='123456'
print type(e)
b=e[0]
print b