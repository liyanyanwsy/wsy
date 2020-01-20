#encoding:utf-8
import requests
import json
import threading
import time
from src.common.excel_simple import ExcleHelper
import pymysql
import configparser
def read_config():
    global path,sheetname2,sheetname1,itemcode_data,data,gateway_sn,sleeptime,url,count
    cf=configparser.ConfigParser()
    cf.read("config.ini",)
    path=cf.get('file','path')
    sheetname1=cf.get('file','sheetname1')
    sheetname2=cf.get('file','sheetname2')
    # print (path)
    # print(sheetname1)
    # print(sheetname2)
    itemcode_data=ExcleHelper(path,sheetname1)
    data=ExcleHelper(path,sheetname2)
    url=cf.get('env','url')
    gateway_sn=cf.get('sn','gateway_sn')
    sleeptime=cf.get('time','sleeptime')
    count=cf.get('count','j')
    print ('******************************')
    print ('基础信息如下：')
    print ('设备sn为%s'%gateway_sn)
    print ('间隔时间为%s'%sleeptime)
    print ('环境信息为%s'%url)
    print ('测试起点场景%s'%count)
    print ('******************************')
cache={}
#通过接口取个iccid
#手机登录接口，获取商家列表接口，手机再次登录接口，获取iccid接口，获取通信质量检测接口，获取通信解决方案接口
#先获取到token
def login():
    #手机登录，第一个token
    path=data.get_value('login_mobile','path')
    header=data.get_value('login_mobile','headers')
    base_params=data.get_value('login_mobile','params')
    #json.loads是将转化为json
    payload=json.loads(base_params)
    headers=json.loads(header)
    response=requests.post(url=url+path,data=payload,headers=headers)
    result=json.loads(response.content)
    access_token=result['access_token']
    bearer=result['token_type']
    Authorization=bearer+" "+access_token
    cache['Authorization1']=Authorization
    #获取商家列表
    path2=data.get_value('get_list','path')
    base_params2=data.get_value('get_list','params')
    Authorization=cache['Authorization1']
    headers2={"authorization":"%s"%Authorization,
              "User-agent":"okhttp/3.9.1"}
    response2=requests.get(url=url+path2,headers=headers2)
    result2=json.loads(response2.content)
    # print (result2)
    rog_id=result2[0]['org']['id']
    cache['rog_id']=rog_id
    #手机登录第二个token
    path3=data.get_value('login_mobile002','path')
    headers4=data.get_value('login_mobile002','headers')
    base_params3=data.get_value('login_mobile002','params')
    #json.loads是将转化为json
    payload3=json.loads(base_params3)
    org_id=cache['rog_id']
    # print org_id
    headers3=json.loads(headers4)
    payload['org_id']=org_id
    response3=requests.post(url=url+path3,data=payload3,headers=headers3)
    result3=json.loads(response3.content)
    access_token=result3['access_token']
    bearer=result3['token_type']
    Authorization3=bearer+" "+access_token
    cache['Authorization2']=Authorization3
    return cache
#获取iccid接口
def iccid():
    path4=data.get_value('iccid','path')
    Authorization4=login()['Authorization2']
    # print (au)
    headers4={"authorization":"%s"%Authorization4,
              "Content-Type":"application/json"}
    #传入参数
    payload4=[]
    payload4.append(gateway_sn)
    # print (payload4)
    # print (type(payload4))
    #列表转为json
    payload5=json.dumps(payload4)
    # print (payload5)
    # print (type(payload5))
    response4=requests.post(url=url+path4,data=payload5,headers=headers4)
    result4=json.loads(response4.content)
    # print (result4)
    cache['iccid']=result4[0]['iccid']
    # print (cache)
    return cache
# iccid()
# a=login()
# print (a)
# iccid=iccid()['iccid']
# print ('iccid为%s'%iccid)
#通讯质量检测信息
def communicate_check():
    path5=data.get_value('communicate_check','path')
    Authorization5=cache['Authorization2']
    headers5={"authorization":"%s"%Authorization5,
              "User-agent":"okhttp/3.9.1"}
    # payload6={"deviceSn":"%s"%gateway_sn}
    # print (payload6)
    # print (type(payload6))
    # print (url+path5)
    # data6={'deviceSn':'1800011625'}
    url6=url+path5+gateway_sn
    response5=requests.get(url=url6,headers=headers5)
    result5=json.loads(response5.content)
    print (result5)
    cache['itemCode']=result5['itemCode']
    # print (type(result5))
    return result5
#解决方案
def communicate_result():
    path6=data.get_value('communicate_result','path')
    Authorization6=cache['Authorization2']
    headers6={"authorization":"%s"%Authorization6,
              "User-agent":"okhttp/3.9.1"}
    itemcode6=cache['itemCode']
    # payload7={'itemCode':'%s'%itemcode6}
    url7=url+path6+itemcode6
    #这边待验证是否正确，将通讯解决方案的code加入到列表中
    response6=requests.get(url=url7,headers=headers6)
    result6=json.loads(response6.content)
    print (result6)
    reslove=[]
    if len(result6)!=0:
        k=0
        while k<len(result6):
            a=result6[k]['solutionCode']
            # print (a)
            reslove.append(a)
            k+=1
        print (reslove)
        # print (type(reslove))
    return reslove

# communicate_check()
# communicate_result()

#mix_config_info表里communication_mode可以获取到通讯方式
# sim表里面的show_status可以获取到sim卡信息设备状态
# device_analysis_data_operation中connect_status可以获取到设备状态（空，离线和正常都可以获取到，报警不可以）
# device_analysis_data_operation中other中SGits1获取到信号强度

#device_analysis_data_operation,可以查下到设备状态和信号强度
def sqlconnect1():
    conn = pymysql.connect(host='public-server.f-qa.igen', user='root', passwd='1234', db='solarman3_device',
                           port=3306, charset='utf8')
    return conn
#mix_config_info表里面可以查下到通讯方式
def sqlconnect2():
    conn = pymysql.connect(host='public-server.f-qa.igen', user='root', passwd='1234', db='solarman3_device_mix',
                           port=3306, charset='utf8')
    return conn
#sim表种可以查下到通讯方式
def sqlconnect3():
    conn = pymysql.connect(host='10.42.1.2', user='dev', passwd='123456', db='sim',
                           port=3306, charset='utf8')
    return conn
def check():

    j=int(count)
    row_num=itemcode_data.get_row()
    # print (row_num)
    # while j<row_num:
    while j<row_num:
        db1=sqlconnect1()
        db2=sqlconnect2()
        db3=sqlconnect3()
        cur1=db1.cursor()
        cur2=db2.cursor()
        cur3=db3.cursor()
        #将excel中设备状态、信号强度、通信方式、sim卡状态取出来
        deviceStatus=itemcode_data.get_value(j,'deviceStatus')
        signalStrength=itemcode_data.get_value(j,'signalStrength')
        communicateMode=itemcode_data.get_value(j,'communicateMode')
        simStatus=itemcode_data.get_value(j,'simStatus')
        itemCode=itemcode_data.get_value(j,'itemcode')
        communicateResult=itemcode_data.get_value(j,'communicateResult')
        #需要将字符转化为列表
        resolveResult=itemcode_data.get_value(j,'resolveResult')
        # print(resolveResult)
        # print (type(resolveResult))
        if deviceStatus!='null':
            deviceStatus=int(deviceStatus)
        if signalStrength!='null':
            signalStrength=int(signalStrength)
        else:
            signalStrength=''
        if simStatus!='null':
            simStatus=int(simStatus)
        print ('******************************')
        print('表格取值信息如下：')
        print ('设备状态：%s'%deviceStatus)
        print ('信号强度：%s'%signalStrength)
        print ('通讯方式：%s'%communicateMode)
        print ('sim卡状态：%s'%simStatus)
        print ('通讯码：%s'%itemCode)
        # print (type(itemCode))
        print ('通讯结果：%s'%communicateResult)
        # print (type(communicateResult))
        print ('解决方案：%s'%resolveResult)
        # print (type(resolveResult))
        print ('******************************')

        #由于设备状态有两种情况，非报警的时候直接是connect_status字段，有报警的时候分为用户、商家、设备商
        if deviceStatus !=2:
            #deviceStatus，修改设备状态
            sql1="UPDATE device_analysis_data_operation set connect_status=%s,status_within=-1,status_outside=-1 where device_sn='%s'"%(deviceStatus,gateway_sn)
            #signalStrength,修改信号强度
            sql2='UPDATE device_analysis_data_operation SET other=\'{"SGits1":"%s","MDUv1":"5A0AEDC7A2","ICCID1":"%s"}\' WHERE device_sn=\'%s\''%(signalStrength,iccid,gateway_sn)
            #communicateMode，修改通信方式
            sql3="UPDATE mix_config_info SET communication_mode='%s' WHERE device_sn='%s'"%(communicateMode,gateway_sn)
            #simStatus,修改数据库表中的sim卡状态信息
            sql4="UPDATE sim SET show_status=%s WHERE iccid='%s'"%(simStatus,iccid)
            # print (sql1)
            # print (sql2)
            # print (sql3)
            # print (sql4)
            # try:
            #     cur1.execute(sql1)
            #     db1.commit()
            # except:
            #     db1.rollback()
            # db1.close()
            cur1.execute(sql1)
            db1.commit()
            cur1.execute(sql2)
            db1.commit()
            cur2.execute(sql3)
            db2.commit()
            cur3.execute(sql4)
            db3.commit()
        else:
            #deviceStatus，修改设备状态,status_within,status_outside
            sql5="UPDATE device_analysis_data_operation set status_within=1,status_outside=1 where device_sn='%s'"%(gateway_sn)
            #signalStrength
            sql6='UPDATE device_analysis_data_operation SET other=\'{"SGits1":"%s","MDUv1":"5A0AEDC7A2","ICCID1":"%s"}\' WHERE device_sn=\'%s\''%(signalStrength,iccid,gateway_sn)
            #communicateMode，修改通信方式
            sql7="UPDATE mix_config_info SET communication_mode='%s' WHERE device_sn='%s'"%(communicateMode,gateway_sn)
            #simStatus,修改数据库表中的sim卡状态信息
            sql8="UPDATE sim SET show_status=%s WHERE iccid='%s'"%(simStatus,iccid)
            # print (sql5)
            # print (sql6)
            # print (sql7)
            # print (sql8)
            cur1.execute(sql5)
            db1.commit()
            cur1.execute(sql6)
            db1.commit()
            cur2.execute(sql7)
            db2.commit()
            cur3.execute(sql8)
            db3.commit()
        #调用通讯检测信息结果进行验证
        print('通信质量检测信息：')
        communicateinfo=communicate_check()
        # print (communicateinfo['itemCode'])
        # print (communicateinfo['communicateResult'])
        # print (itemCode.strip())
        # print (communicateResult.strip())
        #排除调通讯方式找不到的
        if communicateinfo['communicateResult']!='COMMUNICATE_MODE_NOT_FOUND':
            if communicateinfo['itemCode']==itemCode.strip() and communicateinfo['communicateResult']==communicateResult.strip():
                print('通讯检测信息正确pass')
            else:
                print('通讯检测信息错误fail')
            #调用通讯解决方案接口进行验证
            print('解决方案信息：')
            communicatereslove=communicate_result()
            #将list转化为str
            communicatereslove1=str(communicatereslove)
            # print (communicatereslove1.strip())
            # print (resolveResult)
            if communicatereslove1!='[]':
                if communicatereslove1.strip()==resolveResult.strip():
                        print('通讯检测解决方案正确pass')
                else:
                    print('通讯检测解决方案错误fail')
            else:
                print ('通讯正常，无通讯解决方案pass')
        else:
            print ('通讯方式未找到fail')
        print ('第%d个场景测试结束'%j)
        print ('******************************')
        j+=1
        db1.close()
        db2.close()
        db3.close()
        time.sleep(int(sleeptime))
if __name__ == '__main__':
    read_config()
    iccid=iccid()['iccid']
    print ('iccid为%s'%iccid)
    check()





