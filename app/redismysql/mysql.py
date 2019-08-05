import MySQLdb
# def verify_code():
#     try:
#         conn = MySQLdb.connect(host='192.168.1.53', user='zhouwei', passwd='Zhouwei@123', db='solarman2',
#                                port=3306, charset='utf8')
#
#         cur=conn.cursor()
#         cur.execute("SELECT * FROM sys_verify_message WHERE verify_account='17798735555' ORDER BY udpate_time DESC LIMIT 1")
#         re1 = cur.fetchall()
#         a=list(re1[0])[2]
#         cur.close()
#         conn.close()
#         print a
#         return a
#     except Exception,e:
#         print e
def verify_code():
    try:
        conn = MySQLdb.connect(host='public-server.f-qa.igen', user='root', passwd='1234', db='solarman3_acc',port=3306, charset='utf8'
                               )
        cur=conn.cursor()
        cur.execute("SELECT * FROM captcha WHERE target ='337286157@qq.com' ORDER BY last_modified_date DESC LIMIT 1")
        re1 = cur.fetchall()
        a=list(re1[0])[5]
        cur.close()
        conn.close()
        print a
        return a
    except Exception,e:
        print e
verify_code()

# print re1[0]
# print list(re1[0])

# b=json.dumps(re1)
# print re1[0]
# print b

# print b
# a=re1[0]
# b2=b[0]
# print a
# print b2
