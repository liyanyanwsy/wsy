# -*- coding: utf-8 -*-
import requests,re,sys,time,datetime
import json
from bs4 import BeautifulSoup
from src.common.excel_simple import ExcleHelper
#点击事件
#一个月内的数据
end_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
today = datetime.datetime.now()
offset = datetime.timedelta(days=-30)
start_time=(today + offset).strftime('%Y-%m-%d')
# print (start_time,end_time)

url='https://www.talkingdata.com/app/rest/data.json/query/cf0d498a5865'
headers={
    "Content-Type":"application/json",
    "Cookie":"JSESSIONID=node1yw6jt5xs8jyuwi402auk4nw0; xn_dvid_kf_9488=2767E1-0D75F9AC-CB38-2E37-71B1-18CC8094B29A; i18next=zh_cn; tdce=LavinDuck@163.com; Hm_lvt_6b82c15e44f810b130c2eb92b0b36483=1570690439; xn_sid_kf_9488=1570690444568860; comment_author=a857b49d-9db2-4f4d-9ed4-e8ccf5eb45b9; tdppt=a857b49d-9db2-4f4d-9ed4-e8ccf5eb45b9; Hm_lpvt_6b82c15e44f810b130c2eb92b0b36483=1570690469; JSESSIONID=node1yw6jt5xs8jyuwi402auk4nw0.node1; _app_token_=cf0d498a5865; Hm_lvt_8243304aaae4143469bb3251c96f78c3=1568625352,1568625818,1568769233,1570691222; Hm_lpvt_8243304aaae4143469bb3251c96f78c3=1570691222; _canary_user_new=LavinDuck@163.com"
}

#不是字典格式，有null，先是字符格式
payload='{{"metrics":["eventcount"],"groupby":"eventid","conditions":{"developerid":3270065,"productid_list":[3285547],"platformid":"","start":%s,"end":%s,"eventid_list":["A01-登录","A02-注册第一步邮箱注册","A03-注册第一步手机号注册","A04-注册第二步完善账号信息","A05-注册第三步完善商家信息","A06-注册第四步注册成功","A11-运维-首页","A12-运维-电站","A13-电站详情","A14-运维-报警","A15-设备-设备","A16-点击应用","A17-点击消息","A19-点击新建电站","A21-编辑所属标签","A22-点击添加网关/采集器","A25-点击报警","A26-点击关于电站","A28-点击打开报警详情","A34-授权用户","A35-授权商家","A36-授权内部成员","A37-设备-设备详情","A01-登录","A02-注册第一步邮箱注册","A03-注册第一步手机号注册","A04-注册第二步完善账号信息","A05-注册第三步完善商家信息","A06-注册第四步注册成功","A07-忘记密码第一步邮箱确认","A08-忘记密码第一步手机号确认","A11-运维-首页","A12-运维-电站","A13-电站详情","A14-运维-报警","A15-设备-设备","A16-点击应用","A17-点击消息","A19-点击新建电站","A21-编辑所属标签","A22-点击添加网关/采集器","A25-点击报警","A26-点击关于电站","A28-点击打开报警详情","A34-授权用户","A35-授权商家","A36-授权内部成员","A37-设备-设备详情"]}}}'%(start_time,end_time)


# print (payload)
# print (type(payload))
#转化为字典格式
data1=json.loads(payload)
# print (type(data1))
# print (data1)
#转化为json格式
data2=json.dumps(data1)
response=requests.post(url=url,data=data2,headers=headers,verify=False)
result=json.loads(response.content)
# print (result)
# print (type(result))
#将埋点编号存到列表中
result2=result['result']
result2_len=len(result2)
# print (result2)
# print (type(result2))
result3=[]
j=0
while j<result2_len:
    result4=result2[j]['eventvalue']
    print (result4)
    result3.append(result4)
    j+=1


mydata=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\maidian.xlsx','Sheet1')
rows_num = mydata.get_row()
print (rows_num)
i=1

while i <rows_num:
    maidian_data=mydata.get_value(i,'埋点编号')
    maidian_data2=int(maidian_data)
    # print (maidian_data2)
    maidian_data3=str(maidian_data2)
    # print (maidian_data3)
    if maidian_data3 in result3:
        # print ('该埋点:%s已在talkdata中'%maidian_data3)
        print ('pass')
    else:
        print ('该埋点:%s不在talkdata中'%maidian_data3)
    i=i+1




