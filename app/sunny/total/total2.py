#encoding:utf-8
import requests as re
import json as j
import MySQLdb
conn = MySQLdb.connect(host='web.solarmanpv.com', user='readonly', passwd='yingZHEN123', db='solarman2',
                       port=33306, charset='utf8')
cur = conn.cursor()
#将数据库中的uid和公司id查询出来，然后再分别放到列表中
sql1="SELECT uid,company_id from b_user"
cur.execute(sql1)
re1=cur.fetchall()
c1=len(re1)
print c1
# print list(re1[0])
uid=[]
company_id=[]
i=0
while i < c1:
    a1=list(re1[i])[0]
    a2=list(re1[i])[1]
    uid.append(a1)
    company_id.append(a2)
    i+=1
# print uid
# print company_id



# companyid=
# userid=
#
#分别取列表中的数据，一一对应接口取数据
k=0
len1=0
while k<c1:
    print uid[k],company_id[k]
    #用户id和公司id均不为none的时候，进行接口取数据，不满足条件置为0
    if uid[k]!=None and company_id[k]!=None:
        url1='http://47.88.18.157:18014/v00009/epc/plantView/doPlantList.json?uid=%d&companyId=%d&statusType=-1&pageIndex=1&pageSize=10000' %(uid[k],company_id[k])
        r1=re.get(url1)
        result1=j.loads(r1.content)
    # print result1
    # print type(result1)
        list=result1['PlantListWapper']
    # print list
    # print type(list)
        #取电站id，并添加到列表中，最后打印出列表长度，即可得出电站个数。
        plant_id=[]
        l=len(list)
    # print l
        m=0
        while m<l:
            data=list[m]
        # print data
        # print data
        # print type(data)
            id=data['plantId']
        # print id
            m+=1
            plant_id.append(id)
        # print plant_id
    else:
        uid[k]=0
        company_id[k]=0

    len2=len(plant_id)
    # if len1<len2:
    #     len1=len2
    # else:
    #     print len1
    print len2
    k+=1

cur.close()
conn.close()
# energyToday=0
# energyMonth=0
# energyTotal=0
# power=0
# capacity=0
#
# for i in plant_id:
#     url2='http://47.88.18.157:18014/v00009/epc/plantDetail/doPlantData.json?plantId=%d&companyId=%d&lan=1' %(i,companyid)
#     r2=re.get(url2)
#     #返回电站详情数据
#     result2=j.loads(r2.content)
#     # print result2
#     # print type(result2)
#     #电站基本信息
#     plant=result2['Plant']
#     #电站的装机容量
#     capacity1=plant['power']
#     if capacity1=='null':
#         capacity1=0
#     capacity+=capacity1
#     #电站的数据信息
#     plant_data=result2['PlantData']
#     power1=plant_data['power']
#     if power1 is not 'null':
#         power+=power1
#     # print power1
#     # 当前功率
#     else:
#         power=power
#     energyToday1=plant_data['energyToday']
#     if energyToday1=='null':
#         energyToday1=0
#     energyMonth1=plant_data['energyMonth']
#     if energyMonth1=='null':
#         energyMonth1=0
#     energyTotal1=plant_data['energyTotal']
#     if energyTotal1=='null':
#         energyTotal1=0
#     #日、月、总发电量
#     # print energyToday1
#     # print energyMonth1
#     # print energyTotal1
#     energyToday+=energyToday1
#     energyMonth+=energyMonth1
#     energyTotal+=energyTotal1
# print energyToday,energyMonth,energyTotal,power,capacity



