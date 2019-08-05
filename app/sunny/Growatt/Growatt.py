#encoding:utf-8
import MySQLdb
#该代码为查询锦浪列表中的采集器是否入到外网数据库，首先进行首位去零末尾去换行操作，并追加到列表中
# conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='solarman2',
#                        port=3306, charset='utf8')
# cur=conn.cursor()
conn = MySQLdb.connect(host='web.solarmanpv.com', user='liyanyan', passwd='Liyanyan@123', db='solarman2',
                   port=33306, charset='utf8')
cur=conn.cursor()
with open(r"D:\xingit\wsy\app\sn.txt", "r") as f:
    s = f.readlines()
    sn=[]
    for i in s:
        #去掉换行
        b=i.strip("\n")
        # print b
        # print b[0
        #去点左边的0
        c=b.lstrip("0")
        # print c
        #替换这些字符
        d=c.replace('\xef\xbb\xbf','')
        sn.append(d)
    # print sn
#列表首个中的0去掉
sn[0]=sn[0].lstrip('0')
# print sn
# if '\xef\xbb\xbf' in sn[0]:
#     sn1=sn[0].replace('\xef\xbb\xbf','')
#     print sn1
#利用循环查询sn在datalogger、b_company_device表中是否有数据
for j in sn:
     print j
     #查询是否有对应的数据信息
     cur.execute("SELECT * FROM datalogger WHERE sn='%s'" %j)
    # conn.commit()
     re1=cur.fetchall()
     #查询数据的条数
     c1=len(re1)
     # print c1
     if c1>=1:
         print "已入库datalogger表"
         cur.execute("SELECT type, firmware_developer_version FROM datalogger WHERE sn='%s'" %j)
         re3=cur.fetchall()
         print re3

     #查询武术家
     else:
         print "此sn未入库datalogger"
     cur.execute("SELECT * FROM b_company_device WHERE datalogger_sn='%s'" %j)
     re2=cur.fetchall()
     c2=len(re2)
     # print c2
     if c1>=1:
         print "已入库b_company_device表"
     else:
         print "此sn未入库b_company_device"
cur.close()
conn.close()

#     cur.execute("SELECT * FROM b_company_device WHERE datalogger_sn=%s" %j)
#     conn.commit()
#     re2=cur.fetchall()
#     print re2
    # for i in


        # print(b.replace(b[0],''))

        # c=b.strip("0")
        # print c
    #     a=a.append(b)
    #
    # print b
