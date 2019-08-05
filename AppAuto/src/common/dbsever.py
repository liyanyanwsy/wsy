#encoding=utf-8
import MySQLdb
#数据库连接可以封装起来

#b端邮箱/手机注册码

def b_verify_code(self,b_code):
    try:
        conn = MySQLdb.connect(host='web.solarmanpv.com', user='readonly', passwd='yingZHEN123', db='solarman2',
                               port=33306, charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM sys_verify_message WHERE verify_account=%s ORDER BY udpate_time DESC LIMIT 1") % b_code
        re1 = cur.fetchall()
        a=list(re1[0])[2]
        cur.close()
        conn.close()
        return a
    except Exception,e:
        print e

def cmobile_verify_code(self,mobile):
    try:
        conn = MySQLdb.connect(host='web.solarmanpv.com', user='readonly', passwd='yingZHEN123', db='solarman2',
                               port=33306, charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM user_pending WHERE mobile=%s ORDER BY update_time DESC LIMIT 1") %mobile
        re1 = cur.fetchall()
        a=list(re1[0])[6]

        cur.close()
        conn.close()
        #print a
        return a

    except Exception,e:
        print e
def cemail_verify_code(self,email):
    try:
        conn = MySQLdb.connect(host='web.solarmanpv.com', user='readonly', passwd='yingZHEN123', db='solarman2',
                               port=33306, charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM user_notification WHERE email=%s ORDER BY update_time DESC LIMIT 1") %email
        re2 = cur.fetchall()
        b=list(re2[0])[4]
        cur.close()
        conn.close()
        #print a
        return b

    except Exception,e:
        print e


