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

url='https://www.talkingdata.com/app/rest/data.json/query/2e7248c01427'
headers={
    "Content-Type":"application/json",
    "Cookie":"JSESSIONID=node1cw5po0oghdzu1gacva7186tqi; xn_dvid_kf_9488=2767E1-0D75F9AC-CB38-2E37-71B1-18CC8094B29A; Hm_lvt_6b82c15e44f810b130c2eb92b0b36483=1568079119; i18next=zh_cn; tdce=LavinDuck@163.com; _canary_user_new=LavinDuck@163.com; xn_sid_kf_9488=1568769196465983; comment_author=fe86938a-63ae-4b83-8df2-78a1db4e5525; tdppt=fe86938a-63ae-4b83-8df2-78a1db4e5525; Hm_lpvt_6b82c15e44f810b130c2eb92b0b36483=1568769227; JSESSIONID=node1cw5po0oghdzu1gacva7186tqi.node1; _app_token_=2e7248c01427; Hm_lvt_8243304aaae4143469bb3251c96f78c3=1568624209,1568625352,1568625818,1568769233; Hm_lpvt_8243304aaae4143469bb3251c96f78c3=1568769233"
}

#不是字典格式，有null，先是字符格式
payload='{"metrics":["eventcount"],"groupby":"eventvalue","conditions":{"developerid":3270065,"productid_list":[3286748],"platformid":"","start":"%s","end":"%s","eventid_list":["点击事件"],"eventlabel_list":null,"eventkey_list":["code"],"eventvalue_list":null,"type":"string"},"limit":1000}'%(start_time,end_time)


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




