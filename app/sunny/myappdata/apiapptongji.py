#coding:utf-8
import requests as re
import json
import jsonpath
import paramiko
import os

#封装登录函数
def mylogin():
    #登录接口
    url="http://192.168.1.58:18003/v/ap.2.0/user/login?user_id=wsy@163.com&user_pass=111111&terminate=android&push_sn=69cb9502a514b6c56341f0e0cc4c17cf&timezone=8&lan=zh&country=CN"
    #保持会话
    # s=re.session()
    r=re.get(url)
    print r.url
    return r.cookies

s=re.session()
#使用已登录的cookies
cookies=mylogin()
#获取电站详情数据
#目标接口
url2="http://192.168.1.58:18003/v/ap.2.0/plant/get_plant_overview?uid=164855&plant_id=237270"
#接口的参数
r2=s.get(url2,cookies=cookies)
print r2.url
b=r2.content
#转化为字典格式
c=json.loads(b)
#使用jsonpath提取电站数据
print c

power_in=jsonpath.jsonpath(c,"$..power_in")
power_out=jsonpath.jsonpath(c,"$..power_out")
battery=jsonpath.jsonpath(c,"$..battery")
power_net=jsonpath.jsonpath(c,"$..power_net")
print power_in
print battery
print power_net
print power_out
#当日发电量
energy_day=power_out[0]['energy_day']
print energy_day
#累计发电量
energy_total=
#当日用电量
energy_useage_day=power_in[0]['energy_useage_day']
#累计用电量
energy_useage_month=power_in[0]['energy_useage_day']
#电池容量
battery1=
#剩余电池容量
soc=
#当日充电
battery_in=battery[0]['battery_in']
#当日放电
battery_out=battery[0]['battery_out']


def nn():
    try:
        hostname='10.42.2.32'
        port=22
        username='root'
        password='1234'


    except Exception,e:
        print e


get 'analysis:powerplant_last_result','00000163657'


当日发电量
u
当日用电量
nj
当日充电量
gp
当日放电量
gq


累计发电量
v
累计用电量
yb


电池容量

剩余电池容量


