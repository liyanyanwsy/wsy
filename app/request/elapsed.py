#encoding:utf-8
import requests as re
r=re.get("http://www.cnblogs.com/yoyoketang/",timeout=0.01)
print r.elapsed
#总时长，单位为s
print r.elapsed.total_seconds()
#获取微秒部分，大于0小于1秒
print r.elapsed.microseconds
#秒，大于0小于1天
print r.elapsed.seconds
#以天为单位
print r.elapsed.days
#最大时间
print r.elapsed.max
#最小时间
print r.elapsed.min
#最小时间单位
print r.elapsed.resolution


