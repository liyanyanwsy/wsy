#encoding:utf-8
import pymysql
import requests as re
def guanggao():
    try:
        # conn = MySQLdb.connect(host='web.solarmanpv.com', user='liyanyan', passwd='Liyanyan@123', db='solarman2',
        #                    port=33306, charset='utf8')
        # conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='solarman2',
        #                        port=3306, charset='utf8')
        conn = pymysql.connect(host='192.168.30.45', user='zhouwei', passwd='Zhouwei@123', db='advert',
                               port=3306, charset='utf8')

        cur=conn.cursor()
        sql1='select id from ad_value'
        sql2='select cname from ad_value'

        #查询平台、位置、渠道id,并存到列表中
        cur.execute(sql1)
        re1=cur.fetchall()
        c1=len(re1)
        a=[]
        i=0
        while i < c1:
            a1=list(re1[i])[0]
            a.append(a1)
            i+=1

        cur.execute(sql2)
        re2=cur.fetchall()
        c2=len(re2)
        b=[]
        j=0
        while j < c2:
            b1=list(re2[j])[0]
            b.append(b1)
            j+=1

        print (b)
        #小麦用户版平台取值，不分安卓和ios
        platform=a[89:90]
        #位置取值
        positon=a[2:5]
        #安卓渠道取值
        channel1=a[7:16]
        #ios渠道取值
        channel2=a[]
        #软件版本号
        soft_version=b[90:91]
        print (platform,positon,channel1)

        headers={"Connection": "keep-alive",
                 "host": "10.42.7.23:19194",
                 # "host": "apic-cdn.solarman.cn",
                 "User-Agent":"okhttp/3.11.0",
                 "Accept-Encoding": "gzip",
                 }
        # 小麦家庭版安卓接口测试正常(平台为5，位置为13,14,15，渠道为channel，软件版本soft_version，硬件版本hard_version
        for pl in platform:
            for po in positon:
                for ch in channel1:
                    for so in soft_version:
                            pl1=int(pl)
                            po1=int(po)
                            ch1=int(ch)
                            print (pl1,po1,ch1,so)
                            url1="http://10.42.7.23:19194/advert/api/search?platform=%d&position=%d&runType=16&channel=%d&softversion=%s&hardversion=12" %(pl1,po1,ch1,so)
                            print (url1)
                            # url1="https://apic-cdn.solarman.cn/advert/search?platform=%d&position=%d&runType=16&channel=%d&softversion=%s&hardversion=%s" %(pl1,po1,ch1,so1,ha1)
                            req1=re.get(url1,headsers=headers,verify=False)
                            print (req1.status_code)
                            print (req1.content)
        print('小麦家庭版安卓测试完毕')
        # #安卓接口测试异常
        # for pl2 in range(1,3):
        #     for po2 in range(0,12):
        #         for ch2 in range(0,17):
        #             for so2 in range(0,2):
        #                 for ha2 in range(3,5):
        #
        #                     # so3=so2.decode('utf-8')
        #                     # ha3=ha2.decode("utf-8")
        #                     print pl2,po2,ch2,so2,ha2
        #                     url1="http://192.168.1.58:8080/advert/search?platform=cxvxvxvvxvxv&position=%d&runType=16&channel=%d&softversion=%s&hardversion=%s" %(po2,ch2,so2,ha2)
        #                     req1=re.get(url1,headers=headers,verify=False)
        #                     print req1.status_code
        #                     print req1.content
        # 小麦家庭版ios接口测试正常(平台为52，位置为13,14,15，渠道为60，软件版本ios_soft_version，硬件版本ios_hard_version
        for o in ios_platform:
            for p in positon:
                for q in ios_channel:
                    for r in ios_soft_version:
                        for s in ios_hard_version:

                            o1=int(o)
                            p1=int(p)
                            q1=int(q)
                            r1=r.decode('utf-8')
                            s1=s.decode("utf-8")
                            print (o1,p1,q1,r1,s1)
                            url1="http://10.42.7.23:19194/advert/api/search?platform=%d&position=%d&runType=16&channel=%d&softversion=%s&hardversion=%s" %(o1,p1,q1,r1,s1)
                            # url1="http://apic-cdn.solarman.cn/advert/search?platform=%d&position=%d&runType=16&channel=%d&softversion=%s&hardversion=%s" %(o1,p1,q1,r1,s1)
                            req1=re.get(url1,headers=headers,verify=False)
                            print (req1.status_code)
                            print (req1.content)
        print ('小麦家庭版ios测试完毕')
        # 小麦专业版安卓接口测试正常(平台为4，位置为13,14,15，渠道为channel，软件版本pro_soft_version，硬件版本pro_hard_version
        for pro_pl in pro_platform:
            for pro_po in positon:
                for pro_ch in channel:
                    for pro_so in pro_soft_version:
                        for pro_ha in pro_hare_version:
                            pro_pl1=int(pro_pl)
                            pro_po1=int(pro_po)
                            pro_ch1=int(pro_ch)
                            pro_so1=pro_so.decode('utf-8')
                            pro_ha1=pro_ha.decode("utf-8")
                            print (pro_pl1,pro_po1,pro_ch1,pro_so1,pro_ha1)
                            url1="http://10.42.7.23:19194/advert/api/search?platform=%d&position=%d&runType=16&channel=%d&softversion=%s&hardversion=%s" %(pro_pl1,pro_po1,pro_ch1,pro_so1,pro_ha1)
                            # url1="https://apic-cdn.solarman.cn/advert/search?platform=%d&position=%d&runType=16&channel=%d&softversion=%s&hardversion=%s" %(pl1,po1,ch1,so1,ha1)
                            req1=re.get(url1,headers=headers,verify=False)
                            print (req1.status_code)
                            print (req1.content)
        print ('小麦专业版安卓测试完毕')
        # 小麦专业版ios接口测试正常(平台为，位置为13,14,15，渠道为ios_channel，软件版本pro_ios_soft_version，硬件版本pro_ios_hard_version
        for pro_ios_pl in pro_ios_platform:
            for pro_ios_po in positon:
                for pro_ios_ch in ios_channel:
                    for pro_ios_so in pro_ios_soft_version:
                        for pro_ios_ha in pro_ios_hard_version:
                            pro_ios_pl1=int(pro_ios_pl)
                            pro_ios_po1=int(pro_ios_po)
                            pro_ios_ch1=int(pro_ios_ch)
                            pro_ios_so1=pro_ios_so.decode('utf-8')
                            pro_ios_ha1=pro_ios_ha.decode("utf-8")
                            print (pro_ios_pl1,pro_ios_po1,pro_ios_ch1,pro_ios_so1,pro_ios_ha1)
                            url1="http://10.42.7.23:19194/advert/api/search?platform=%d&position=%d&runType=16&channel=%d&softversion=%s&hardversion=%s" %(pro_ios_pl1,pro_ios_po1,pro_ios_ch1,pro_ios_so1,pro_ios_ha1)
                            # url1="https://apic-cdn.solarman.cn/advert/search?platform=%d&position=%d&runType=16&channel=%d&softversion=%s&hardversion=%s" %(pl1,po1,ch1,so1,ha1)
                            req1=re.get(url1,headers=headers,verify=False)
                            print (req1.status_code)
                            print (req1.content)
        print ('小麦专业版ios测试完毕')
    except Exception:
        print ("erro")

guanggao()


