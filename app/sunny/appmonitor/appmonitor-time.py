#coding:utf-8
import threading
import requests as re
import sunny.appmonitor.sendemail
import time
def fun_timer():
    try:
        s=re.session()
        headers={"token": "_8687d8c11e364e82a156b68cd9853480",
                 "sign": "69ee291fbd62",
                 "num": "1534400484533",
                 "Host": "apipro-cdn.solarman.cn",
                 "Connection": "Keep-Alive",
                 "Accept-Encoding": "gzip",
                 "User-Agent": "okhttp/3.6.0"
                 }
        url="http://apipro-cdn.solarman.cn/v00008/epc/user/login.json?userId=17712341234&userPass=123456&terminate=Android&pushSn=aab93e92c97e30962cd41bae2fcdbf77&lan=1&customization="
        r=s.get(url,headers=headers,verify=False)
        print r.status_code
        if r.status_code==200:
            print u"小麦专业版app系统正常"
        else:
            print u"小麦专业版app系统异常"
            sunny.appmonitor.sendemail.sendemail()
    except Exception,e:
        print e

    try:
        s=re.session()
        headers={"Host": "apic-cdn.solarman.cn",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.8.1"
                }
        url="http://apic-cdn.solarman.cn/v/ap.2.0/user/login?user_id=zedlital@163.com&user_pass=zedl1990&terminate=android&push_sn=18169700c541778ff4076fc5e8cab3f6&timezone=8&lan=zh&country=CN"
        r=s.get(url,headers=headers,verify=False)
        print r.status_code
        if r.status_code==200:
            print u"小麦光伏app系统正常"
        else:
            print u"小麦光伏app系统异常"
            sunny.appmonitor.sendemail.sendemail2()
    except Exception,e:
        print e

    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    print timestamp
    global timer
    timer=threading.Timer(600,fun_timer)
    timer.start()
timer=threading.Timer(1,fun_timer)
timer.start()