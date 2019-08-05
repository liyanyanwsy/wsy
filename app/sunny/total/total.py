#encoding:utf-8
import requests as re
import json as j
import ConfigParser
def read_config():
    global user,passw
    cf=ConfigParser.ConfigParser()
    cf.read("total.ini")
    user=cf.get("baseconf","username")
    passw=cf.get("baseconf","password")
    print user
    print passw
def generationtotal():
    #需求：统计账号下所有电站的发电量、装机容量等的求和。
    #账号和密码
    # user='zedlital@gmail.com'
    # password='12345678'
    # user='admin@solarman.cn'
    # password='yingzhen123'
    # user='18812341234'
    # password='123456'
    # user='18669908999'
    # password='981231'
    #登录接口，返回用户id和公司id
    url='http://47.88.18.157:18014/v00009/epc/user/login.json?userId=%s&userPass=%s&terminate=Android&pushSn=&lan=2&customization=4' %(user,passw)
    r=re.get(url)
    result=j.loads(r.content)
    buser=result['buser']
    companyid=buser['companyId']
    userid=buser['uid']
    print "公司id为%d,用户id%d" %(companyid,userid)
    #电站列表接口，返回电站id
    url1='http://47.88.18.157:18014/v00009/epc/plantView/doPlantList.json?uid=%d&companyId=%d&statusType=-1&pageIndex=1&pageSize=5000' %(userid,companyid)
    r1=re.get(url1)
    result1=j.loads(r1.content)
    # print result1
    # print type(result1)
    list=result1['PlantListWapper']
    # print list
    # print type(list)
    plant_id=[]
    l=len(list)
    print "电站个数为%d" %l
    i=0
    while i<l:
        data=list[i]
        # print data
        # print type(data)
        id=data['plantId']
        # print id
        i+=1
        plant_id.append(id)
        # print plant_id
    energyToday=0
    energyMonth=0
    energyTotal=0
    power=0
    capacity=0
    #电站详情-电站数据接口，返回装机容量、当前功率、当日发电量、当月发电量、总发电量，该账号下所有电站的数据叠加。
    for i in plant_id:
        url2='http://47.88.18.157:18014/v00009/epc/plantDetail/doPlantData.json?plantId=%d&companyId=%d&lan=1' %(i,companyid)
        r2=re.get(url2)

        #返回电站详情数据
        result2=j.loads(r2.content)
        # print result2
        # print type(result2)
        #电站基本信息
        plant=result2['Plant']
        #电站的装机容量
        capacity1=plant['power']
        # print capacity1
        #装机容量不为空时，进行叠加，为空时直接置为0
        if capacity1!='None':
            capacity+=capacity1
        else:
            capacity1=0

        #电站的数据信息
        plant_data=result2['PlantData']
        power1=plant_data['power']
        # print power1
        if power1!=None:
            power+=power1
        # print power1
        # 当前功率
        else:
            power1=0

        energyToday1=plant_data['energyToday']
        if energyToday1!=None:
            energyToday+=energyToday1
        else:
            energyTotal1=0
        energyMonth1=plant_data['energyMonth']
        if energyMonth1!=None:
            energyMonth+=energyMonth1
        else:
            energyMonth1=0
        energyTotal1=plant_data['energyTotal']
        if energyTotal1!=None:
            energyTotal+=energyTotal1
        else:
            energyTotal1=0
        #日、月、总发电量
        # print energyToday1
        # print energyMonth1
        # print energyTotal1
        # print power
        # print capacity
        # energyToday+=energyToday1
        # energyMonth+=energyMonth1
        # energyTotal+=energyTotal1
    print '当日发电量为%s'%energyToday
    print '当月发电量为%s' %energyMonth
    print '总发电量为%s' %energyTotal
    print '发电功率为%s' %power
    print '装机容量为%s' %capacity

if __name__ == '__main__':
    read_config()
    generationtotal()

