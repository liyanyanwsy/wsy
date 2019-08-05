#coding:utf-8
import requests as re
import MySQLdb
try:
    # conn = MySQLdb.connect(host='web.solarmanpv.com', user='liyanyan', passwd='Liyanyan@123', db='solarman2',
    #                    port=33306, charset='utf8')
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='solarman2',
                           port=3306, charset='utf8')
    cur=conn.cursor()
    sql1="select id from ad_platform"
    sql2="select id from ad_position"
    sql3="select id from ad_channel"
    sql4="SELECT name FROM ad_software_version"
    sql5="SELECT name FROM ad_hardware_version"
    #查询平台的id,并存到列表中
    cur.execute(sql1)
    re1=cur.fetchall()
    c1=len(re1)
    # print c1
    platform=[]
    i=0
    while i < c1:
        a1=list(re1[i])[0]
        platform.append(a1)
        i+=1
    # print platform
    #查询位置的id,并存到列表中
    cur.execute(sql2)
    re2=cur.fetchall()
    c2=len(re2)
    # print c2
    position=[]
    j=0
    while j < c2:
        a2=list(re2[j])[0]
        position.append(a2)
        j+=1
    # print position
    # print position[0]
    #查询渠道的id,并存到列表中
    cur.execute(sql3)
    re3=cur.fetchall()
    c3=len(re3)
# print c3
    channel=[]
    k=0
    while k < c3:
        a3=list(re3[k])[0]
        channel.append(a3)
        k+=1
    # print channel
    # print channel[0]
    #查询软件版本的name,并存到列表中
    cur.execute(sql4)
    re4=cur.fetchall()
    c4=len(re4)
    # print c4
    software=[]
    m=0
    while m < c4:
        a4=list(re4[m])[0]
        software.append(a4)
        m+=1
    # print software
    # print software[0]
    #查询硬件版本的name,并存到列表中
    cur.execute(sql5)
    re5=cur.fetchall()
    c5=len(re5)
    # print c5
    hardware=[]
    n=0
    while n < c5:
        a5=list(re5[n])[0]
        hardware.append(a5)
        n+=1
    # print hardware
    # print hardware[0]
    #接口的头文件信息
    headers={"Connection": "keep-alive",
            "host": "apic-cdn.solarman.cn",
            "User-Agent":"okhttp/3.9.1",
            "Accept-Encoding": "gzip",
            }
    # 安卓接口测试(平台为1，位置为1，2，渠道为channel[0:9]，软件版本name为1.4.1，硬件版本hardware[0:14])
    o=int(platform[0])
    r=software[0].decode("utf-8")
    for p in (position[0:2]):
        for q in (channel[0:9]):
            for s in (hardware[0:14]):
                print o,p,q,r,s
                p1=int(p)
                q1=int(p1)
                # headers={"Connection": "keep-alive",
                #         "host": "backend.solarmanpv.com:18009",
                #         "User-Agent":"okhttp/3.9.1",
                #         "Accept-Encoding": "gzip",
                #         }
                url1="http://apic-cdn.solarman.cn/ad/selectList.json?platform=%d&position=%d&runType=1&channel=%d&software=%s&hardware=%s&pageIndex=0&pageSize=1" %(o,p1,q1,r,s)
                req1=re.get(url1,headers=headers,verify=False)
                print req1.status_code
                print req1.content
    # 安卓接口测试(平台为1，位置为1，2，渠道为channel[0:9]，软件版本name为1.4.2，硬件版本hardware[0:14])
    o=int(platform[0])
    r1=software[2].decode("utf-8")
    for p in (position[0:2]):
        for q in (channel[0:9]):
            for s in (hardware[0:14]):
                print o,p,q,r,s

                p1=int(p)
                q1=int(p1)
                # headers={"Connection": "keep-alive",
                #         "host": "backend.solarmanpv.com:18009",
                #         "User-Agent":"okhttp/3.9.1",
                #         "Accept-Encoding": "gzip",
                #         }
                url1="http://apic-cdn.solarman.cn/ad/selectList.json?platform=%d&position=%d&runType=1&channel=%d&software=%s&hardware=%s&pageIndex=0&pageSize=1" %(o,p1,q1,r1,s)
                req1=re.get(url1,headers=headers,verify=False)
                print req1.status_code
                print req1.content

   # ios接口测试
    ios_o=int(platform[2])
    ios_r=software[1].decode("utf-8")
    for ios_p in (position[2:4]):
        for ios_s in (hardware[14:19]):
            print ios_o,ios_p,ios_r,ios_s
            ios_p1=int(ios_p)

            url2="http://apic-cdn.solarman.cn/ad/selectList.json?platform=%d&position=%d&runType=1&channel=&software=%s&hardware=%s&pageIndex=0&pageSize=1" %(ios_o,ios_p1,ios_r,ios_s)
            req2=re.get(url2,headers=headers,verify=False)
            print req2.status_code
            print req2.content
    # ios接口测试
    ios_o=int(platform[2])
    ios_r1=software[3].decode("utf-8")
    for ios_p in (position[2:4]):
        for ios_s in (hardware[14:19]):
            print ios_o,ios_p,ios_r,ios_s
            ios_p1=int(ios_p)

            url2="http://apic-cdn.solarman.cn/ad/selectList.json?platform=%d&position=%d&runType=1&channel=&software=%s&hardware=%s&pageIndex=0&pageSize=1" %(ios_o,ios_p1,ios_r1,ios_s)
            req2=re.get(url2,headers=headers,verify=False)
            print req2.status_code
            print req2.content



except Exception,e:
    print e


        # o1=int(o)
        # p1=int(p)
        # q1=int(q)
        # # print type(o1)
        # # print type(s)
        #
        # q1=q.encode("utf-8")
        # print q1
        # print type(q1)
        # s1=s.encode("utf-8")
        # print s1
        # print type(s1)
        #





# headers={"Connection": "keep-alive",
#         "host": "backend.solarmanpv.com:18009",
#         "User-Agent":"okhttp/3.9.1"
# ,
#         "Accept-Encoding": "gzip",
#         }
# url1="http://backend.solarmanpv.com:18009/ad/selectList.json?platform=1&position=1&runType=1&channel=1&software=1.4.1&hardware=26&pageIndex=0&pageSize=1"
# url2="http://backend.solarmanpv.com:18009/ad/selectList.json?platform=1&position=2&runType=1&channel=1&software=1.4.1&hardware=26&pageIndex=0&pageSize=1"
# r1=re.get(url1,headers=headers,verify=False)
# r2=re.get(url2,headers=headers,verify=False)
# print r1.status_code
# print r2.status_code


# print hardware
# print hardware[0]

# print hardware[0:8]

# print re1
# print re1[0]
# print list(re1[0])[0]
# a=[]
# for sql in (sql1,sql2,sql3,sql4,sql5):
#     cur.execute(sql)
#     re1=cur.fetchall()
#     a.append(re1)
#
# # print a
#
# platform=a[0]
# print platform
# print type(platform)
# platform1=list(platform)[1]
# print platform1
# headers={"Connection": "keep-alive",
#          "host": "backend.solarmanpv.com:18009",
#          "User-Agent":"okhttp/3.9.1",
#          "Accept-Encoding": "gzip",
#          }