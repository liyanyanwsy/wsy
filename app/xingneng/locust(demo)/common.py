#encoding:utf-8
import sys,time,random,hashlib
sys.path.append('../db_set')
# from db_set.mysql_db import DB
def setUp_():
    tim = time.time()
    tim = tim*1000
    tim = str(tim)
    # ts时间戳
    ts = tim.split('.')[0]
    ran = random.randint(100,999)
    ran = str(ran)
    # reqId时间戳拼接随机数
    reqId =ts + ran
    # 密匙
    secret = 'xxxxxxxxxxx'
    #请求头
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
    #数据库
    # db = DB()
    #测试userId
    userId = "100000001000153"
    #测试liveId
    liveId = "140000002000038"
    #测试地址
    host = "http://ixxxxxxxhat.com/"
    return (ts,reqId,secret,header,userId,liveId,host)
def md5(reqSign_):
    md5 = hashlib.md5()
    str_bytes_utf8 = reqSign_.encode(encoding="utf-8")
    md5.update(str_bytes_utf8)
    sign = md5.hexdigest()
    return sign
