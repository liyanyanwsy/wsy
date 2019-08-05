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
#使用已登录的cookiesze
cookies=mylogin()
#获取详情数据
#目标接口
url2="http://192.168.1.58:18003/v/ap.2.0/device/doInverterDetail?uid=1&lan=1&plantId=237270&deviceId=100674399"
#接口的参数
r2=s.get(url2,cookies=cookies)
print r2.url
b=r2.content
# print b
#转化为字典格式
c=json.loads(b)
#使用jsonpath提取设备数据
# print c
#固定数据
gudingdata=jsonpath.jsonpath(c,"$..realTimeDataImp")

#设备发电数据
power_out=jsonpath.jsonpath(c,"$..realTimeDataPower")
#设备电池数据
battery=jsonpath.jsonpath(c,"$..realTimeDataBattery")
print gudingdata
print type(gudingdata)
print power_out
print battery
# status=gudingdata[]
# ipv1
# ipv2
# vpv1
# vpv2
# ppv1
# ppv2
# iacr
# iacs
# iact
# vacr
# vacs
# vact
# pacr
# pacs
# pact
# ppv
# pac
# powerToday
# powerTotal
# temperature
# fac
# pf
# time
# faultType
# timeTotal
# ipmTemperature
# epv1Today
# epv1Total
# epv2Today
# epv2Total
# epvTotal
# eRacToday
# eRacTotal
# pBusVoltage
# nBusVoltage
# "dwStringWarnin
# gValue1"
# "wStringStatusVal
# ue"
# wPIDFaultValue
# vPidPvape
# iPidPvape
# pidStatus
# vPidPvbpe
# iPidPvbpe
# strFault
# vString1
# vString2
# vString3
# vString4
# vString5
# vString6
# vString7
# vString8
# currentString1
# currentString2
# currentString3
# currentString4
# currentString5
# currentString6
# currentString7
# currentString8

# print battery
# print power_out
# #当日发电量
# energy_day=power_out[0]['energy_day']
# print energy_day
# #累计发电量
# energy_total=
# #当日用电量
# energy_useage_day=power_in[0]['energy_useage_day']
# #累计用电量
# energy_useage_month=power_in[0]['energy_useage_day']
# #电池容量
# battery1=
# #剩余电池容量
# soc=
# #当日充电
# battery_in=battery[0]['battery_in']
# #当日放电
# battery_out=battery[0]['battery_out']







