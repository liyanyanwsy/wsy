#encoding:utf-8
import requests
import json
import time,datetime
# import socket
# import threading
system_id=24327
#鉴权信息
def auth():
    url='http://www.f-qa.igen/oauth_s/oauth/token'
    headers={"Content-Type":"application/x-www-form-urlencoded",
             "User-Agent":"okhttp/3.9.1"}
    base_params={"grant_type":"password",
                 "username":"8617798736289",
                 "password":"8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92",
                 "clear_text_pwd":"123456",
                 "client_id":"test",
                 "identity_type":"1"}
    response=requests.post(url=url,data=base_params,headers=headers)
    result=json.loads(response.content)
    access_token=result['access_token']
    bearer=result['token_type']
    Authorization=bearer+" "+access_token
    return Authorization
#首条比例信息
def radio(generationValue,useValue,buyValue,chargeValue,self_use,self_charge,buy_use):
    if generationValue>0:
        #自发自用比例
        useRatio=min(self_use,useValue,generationValue)/generationValue
        #自发充电比例
        chargeRatio=min(self_charge,chargeValue,generationValue)/generationValue
        if useRatio+chargeRatio>1:
            chargeRatio=1-useRatio
            gridRatio=0
            print('自发自用比例为%s,自发充电比例为%s,自发并网比例为%s'%(useRatio,chargeRatio,gridRatio))
        else:
            #自发并网比例
            gridRatio=1-useRatio-chargeRatio
            print('自发自用比例为%s,自发充电比例为%s,自发并网比例为%s'%(useRatio,chargeRatio,gridRatio))
    else:
        useRatio=None
        chargeRatio=None
        gridRatio=None
        print('自发自用比例为%s,自发充电比例为%s,自发并网比例为%s'%(useRatio,chargeRatio,gridRatio))
    if useValue>0:
        #用电来源于发电量比例
        generationRatio=min(self_use,useValue,generationValue)/useValue
        #用电来源于购电比例
        buyRatio=min(buy_use,useValue,buyValue)/useValue
        if generationRatio+buyRatio>1:
            buyRatio=1-generationRatio
            useDischargeRatio=0
            print('用电来源于发电量比例为%s,用电来源于购电比例为%s,用电量来源于放电量比例为%s'%(generationRatio,buyRatio,useDischargeRatio))

        else:
            #用电量来源于放电量比例
            useDischargeRatio=1-generationRatio-buyRatio
            print('用电来源于发电量比例为%s,用电来源于购电比例为%s,用电量来源于放电量比例为%s'%(generationRatio,buyRatio,useDischargeRatio))
    else:
        generationRatio=None
        buyRatio=None
        useDischargeRatio=None
        print('用电来源于发电量比例为%s,用电来源于购电比例为%s,用电量来源于放电量比例为%s'%(generationRatio,buyRatio,useDischargeRatio))
#第二条起比例信息
def radio1(generationValue2,useValue2,buyValue2,chargeValue2,self_usetotal,self_use,self_chargetotal,self_charge,buy_usetotal,buy_use):
    if (generationValue2)>0:
        #自发自用比例
        useRatio=min(self_usetotal+self_use,useValue2,generationValue2)/generationValue2
        #自发充电比例
        chargeRatio=min(self_chargetotal+self_charge,chargeValue2,generationValue2)/generationValue2
        if useRatio+chargeRatio>1:
            chargeRatio=1-useRatio
            gridRatio=0
            print('自发自用比例为%s,自发充电比例为%s,自发并网比例为%s'%(useRatio,chargeRatio,gridRatio))
        else:
            #自发并网比例
            gridRatio=1-useRatio-chargeRatio
            print('自发自用比例为%s,自发充电比例为%s,自发并网比例为%s'%(useRatio,chargeRatio,gridRatio))
    else:
        useRatio=None
        chargeRatio=None
        gridRatio=None
        print('自发自用比例为%s,自发充电比例为%s,自发并网比例为%s'%(useRatio,chargeRatio,gridRatio))
    if (useValue2)>0:
        #用电来源于发电量比例
        generationRatio=min(self_usetotal+self_use,useValue2,generationValue2)/(useValue2)
        #用电来源于购电比例
        buyRatio=min(buy_usetotal+buy_use,useValue2,buyValue2)/(useValue2)
        if generationRatio+buyRatio>1:
            buyRatio=1-generationRatio
            useDischargeRatio=0
            print('用电来源于发电量比例为%s,用电来源于购电比例为%s,用电量来源于放电量比例为%s'%(generationRatio,buyRatio,useDischargeRatio))
        else:
            #用电量来源于放电量比例
            useDischargeRatio=1-generationRatio-buyRatio
        print('用电来源于发电量比例为%s,用电来源于购电比例为%s,用电量来源于放电量比例为%s'%(generationRatio,buyRatio,useDischargeRatio))
    else:
        generationRatio=None
        buyRatio=None
        useDischargeRatio=None
        print('用电来源于发电量比例为%s,用电来源于购电比例为%s,用电量来源于放电量比例为%s'%(generationRatio,buyRatio,useDischargeRatio))
#本日第一条数据信息，参与比例计算，返回首条的增量信息
def first():
    Authorization=auth()
    url='http://www.f-qa.igen/maintain_s/operating/system/+%d'%system_id
    headers={"authorization":"%s"%Authorization,
             "User-agent":"okhttp/3.9.1"}
    response=requests.get(url,headers=headers)
    result=json.loads(response.content)
    #今日发电量取值
    generationValue=result['generationValue']
    print (type(generationValue))
    # print ('当日发电量为%s'%generationValue)
    #今日用电量取值
    useValue=result['useValue']
    #今日并网量取值
    gridValue=result['gridValue']
    #今日购电量取值
    buyValue=result['buyValue']
    #今日充电量取值
    chargeValue=result['chargeValue']
    #今日放电量取值
    dischargeValue=result['dischargeValue']
    print('首条的电量数据信息')
    print('当日发电量为%s,当日用电量为%s,当日并网量为%s,当日购电量为%s,当日充电量为%s,当日放电量为%s'%(generationValue,useValue,gridValue,buyValue,chargeValue,dischargeValue))
    #增量数据
    generation_increment=generationValue
    use_increment=useValue
    grid_increment=gridValue
    buy_increment=buyValue
    charge_increment=chargeValue
    discharge_increment=dischargeValue

    # print('当日发电量增量为%s,当日用电量增量为%s,当日并网量增量为%s,当日购电量增量为%s,当日充电量增量为%s,当日放电量增量为%s'%(generation_increment,use_increment,grid_increment,buy_increment,charge_increment,discharge_increment))
    # generationValue=0.09
    # useValue=0.12
    # chargeValue=0
    # buyValue=0
    # generation_increment=0.09
    # use_increment=0.12
    # grid_increment=0.0
    # buy_increment=0.0
    # charge_increment=0.0
    # discharge_increment=0.03
    if grid_increment>=buy_increment and charge_increment>=discharge_increment:
        if use_increment>0:
            a=min(1,generation_increment/use_increment)
        else:
            a=0
        if charge_increment>0:
            b=min(1,(generation_increment-a*use_increment)/charge_increment)
        else:
            b=0
        print ('a的值为%s,b的值为%s'%(a,b))
        #自发自用增量
        self_use=a*use_increment
        #自发充电增量
        self_charge=b*charge_increment
        #购电自用增量
        buy_use=0
        print ('自发自用增量为%s,自发充电增量为%s'%(self_use,self_charge))
        radio(generationValue,useValue,buyValue,chargeValue,self_use,self_charge,buy_use)
        return[self_use,self_charge,buy_use]
    #并网量增量大于或等于购电量增量时，若放电量增量大于充电量增量：发电量增量=a*用电量增量+c*并网量增量，放电量增量=d*用电量增量+e*并网量增量
    # generationValue=6
    # useValue=4
    # chargeValue2=2
    # buyValue=3
    #
    # generation_increment=1.0
    # use_increment=1.0
    # grid_increment=0.8
    # buy_increment=0.6
    # charge_increment=0.4
    # discharge_increment=0.6

    if grid_increment>=buy_increment and charge_increment<discharge_increment:
        if use_increment>0:
            a=min(1,generation_increment/use_increment)
            d=min(1-a,discharge_increment/use_increment)
        else:
            a=0
            d=0
        print ('a的值为%s,d的值为%s'%(a,d))
        #自发自用增量
        self_use=a*use_increment
        #自发充电增量
        self_charge=0
        #购电自用增量
        buy_use=0
        print ('自发自用增量为%s,自发充电增量为%s,购电自用增量为%s'%(self_use,self_charge,buy_use))
        radio(generationValue,useValue,buyValue,chargeValue,self_use,self_charge,buy_use)
        return[self_use,self_charge,buy_use]
    #购电量增量大于并网量增量时，若充电量增量大于或等于放电量增量：发电量增量=a*用电量增量+b*充电量增量，购电量增量=f*充电量增量+g用电量增量
    # generationValue=6
    # useValue=4
    # chargeValue2=2
    # buyValue=3
    #
    # generation_increment=0.6
    # use_increment=0.6
    # grid_increment=0.6
    # buy_increment=0.8
    # charge_increment=0.6
    # discharge_increment=0.4
    #
    if grid_increment<buy_increment and charge_increment>=discharge_increment:
        if use_increment>0:
            a=min(1,generation_increment/use_increment)
            g=min(1-a,buy_increment/use_increment)
        else:
            a=0
            g=0
        if charge_increment>0:
            b=min(1,(generation_increment-a*use_increment)/charge_increment)
        else:
            b=0
        print ('a的值为%s,b的值为%s,g的值为%s'%(a,b,g))
        #自发自用增量
        self_use=a*use_increment
        #自发充电增量
        self_charge=b*charge_increment
        #购电自用增量
        buy_use=g*use_increment
        print ('自发自用增量为%s,自发充电增量为%s,购电自用增量为%s'%(self_use,self_charge,buy_use))
        radio(generationValue,useValue,buyValue,chargeValue,self_use,self_charge,buy_use)
        return[self_use,self_charge,buy_use]
    #购电量增量大于并网量增量时，若放电量增量大于充电量增量：发电量增量=a*用电量增量，放电量增量=d*用电量增量，购电量增量=g用电量增量
    # generationValue=6
    # useValue=4
    # chargeValue2=2
    # buyValue=3
    #
    # generation_increment=0.6
    # use_increment=1.0
    # grid_increment=0.6
    # buy_increment=0.8
    # charge_increment=0.4
    # discharge_increment=0.6
    #
    if grid_increment<buy_increment and charge_increment<discharge_increment:
        if use_increment>0:
            a=min(1,generation_increment/use_increment)
            d=min(1-a,discharge_increment/use_increment)
            g=min(1-a-d,buy_increment/use_increment)
        else:
            a=0
            d=0
            g=0
        print ('a的值为%s,d的值为%s,g的值为%s'%(a,d,g))
        #自发自用增量
        self_use=a*use_increment
        #自发充电增量?
        self_charge=0
        #购电自用增量
        buy_use=g*use_increment
        print ('自发自用增量为%s,自发充电增量为%s,购电自用增量为%s'%(self_use,self_charge,buy_use))
        radio(generationValue,useValue,buyValue,chargeValue,self_use,self_charge,buy_use)
        return[self_use,self_charge,buy_use]
    # return[self_use,self_charge,buy_use,generationValue,useValue,buyValue,chargeValue]
a=first()
self_use=a[0]
self_charge=a[1]
buy_use=a[2]
# generationValue=a[3]
# useValue=a[4]
# buyValue=a[5]
# chargeValue=a[6]
print ('首条的自发自用增量为%s,首条的自发充电增量为%s，首条的自发购电增量为%s'%(self_use,self_charge,buy_use))
self_usetotal=0
self_chargetotal=0
buy_usetotal=0
i=0
#模拟288条数据
while i<287:
    Authorization=auth()
    url='http://www.f-qa.igen/maintain_s/operating/system/+%d'%system_id
    headers={"authorization":"%s"%Authorization,
             "User-agent":"okhttp/3.9.1"}
    response=requests.get(url,headers=headers)
    result=json.loads(response.content)
    #今日发电量取值
    generationValue1=result['generationValue']
    # print ('当日发电量为%s'%generationValue1)
    #今日用电量取值
    useValue1=result['useValue']
    #今日并网量取值
    gridValue1=result['gridValue']
    #今日购电量取值
    buyValue1=result['buyValue']
    #今日充电量取值
    chargeValue1=result['chargeValue']
    #今日放电量取值
    dischargeValue1=result['dischargeValue']
    print('上一条的电量数据信息')
    print('当日发电量为%s,当日用电量为%s,当日并网量为%s,当日购电量为%s,当日充电量为%s,当日放电量为%s'%(generationValue1,useValue1,gridValue1,buyValue1,chargeValue1,dischargeValue1))

    time.sleep(300)

    response2=requests.get(url,headers=headers)
    result2=json.loads(response2.content)

    #今日发电量取值
    generationValue2=result2['generationValue']
    # print ('当日发电量为%s'%generationValue1)
    #今日用电量取值
    useValue2=result2['useValue']
    #今日并网量取值
    gridValue2=result2['gridValue']
    #今日购电量取值
    buyValue2=result2['buyValue']
    #今日充电量取值
    chargeValue2=result2['chargeValue']
    #今日放电量取值
    dischargeValue2=result2['dischargeValue']
    print('本条的电量数据信息')
    print('当日发电量为%s,当日用电量为%s,当日并网量为%s,当日购电量为%s,当日充电量为%s,当日放电量为%s'%(generationValue2,useValue2,gridValue2,buyValue2,chargeValue2,dischargeValue2))
    #增量数据
    if (generationValue2-generationValue1)<0:
        generation_increment2=min(0,generationValue2-generationValue1)
    else:
        generation_increment2=generationValue2-generationValue1
    if (useValue2-useValue1)<0:
        use_increment2=min(0,useValue2-useValue1)
    else:
        use_increment2=useValue2-useValue1
    if (gridValue2-gridValue1)<0:
        grid_increment2=min(0,gridValue2-gridValue1)
    else:
        grid_increment2=gridValue2-gridValue1
    if (buyValue2-buyValue1)<0:
        buy_increment2=min(0,buyValue2-buyValue1)
    else:
        buy_increment2=buyValue2-buyValue1
    if (chargeValue2-chargeValue1)<0:
        charge_increment2=min(0,chargeValue2-chargeValue1)
    else:
        charge_increment2=chargeValue2-chargeValue1
    if (dischargeValue2-dischargeValue1)<0:
        discharge_increment2=min(0,dischargeValue2-dischargeValue1)
    else:
        discharge_increment2=dischargeValue2-dischargeValue1
    print('当日发电量增量为%s,当日用电量增量为%s,当日并网量增量为%s,当日购电量增量为%s,当日充电量增量为%s,当日放电量增量为%s'%(generation_increment2,use_increment2,grid_increment2,buy_increment2,charge_increment2,discharge_increment2))
    #自发自用量比例、自发充电量比例、自发并网量比例、放电自用量比例、放电并网量比例、购电充电量比例、购电自用量比例、用电量来源于放电量比例、用电量来源于发电量比例、用电量来源于购电量比例
    #并网量增量大于或等于购电量增量时，若充电量增量大于或等于放电量增量：发电量增量=a*用电量增量+b*充电量增量+c*并网量增量
    #a,b,d,g
    #
    # generationValue2=0.11
    # useValue2=0.14
    # chargeValue2=0
    # buyValue2=0
    # generation_increment2=0.02
    # use_increment2=0.02
    # grid_increment2=0.0
    # buy_increment2=0.0
    # charge_increment2=0.0
    # discharge_increment2=0.0
    if grid_increment2>=buy_increment2 and charge_increment2>=discharge_increment2:
        if use_increment2>0:
            a=min(1,generation_increment2/use_increment2)
        else:
            a=0
        if charge_increment2>0:
            b=min(1,(generation_increment2-a*use_increment2)/charge_increment2)
        else:
            b=0
        print ('a的值为%s,b的值为%s'%(a,b))
        #自发自用增量
        self_use2=a*use_increment2
        #自发充电增量
        self_charge2=b*charge_increment2
        #购电自用增量
        buy_use2=0
        print ('自发自用增量为%s,自发充电增量为%s'%(self_use2,self_charge2))
        #自发自用增量总和

        self_usetotal=self_use2+self_usetotal
        #自发充电增量总和

        self_chargetotal=self_charge2+self_chargetotal
        #购电自用增量总和
        buy_usetotal=buy_use2+buy_usetotal
        radio1(generationValue2,useValue2,buyValue2,chargeValue2,self_usetotal,self_use,self_chargetotal,self_charge,buy_usetotal,buy_use)
    #并网量增量大于或等于购电量增量时，若放电量增量大于充电量增量：发电量增量=a*用电量增量+c*并网量增量，放电量增量=d*用电量增量+e*并网量增量
    # generationValue2=6
    # useValue2=4
    # chargeValue2=2
    # buyValue2=3
    #
    # generation_increment2=1.0
    # use_increment2=1.0
    # grid_increment2=0.8
    # buy_increment2=0.6
    # charge_increment2=0.4
    # discharge_increment2=0.6
    if grid_increment2>=buy_increment2 and charge_increment2<discharge_increment2:
        if use_increment2>0:
            a=min(1,generation_increment2/use_increment2)
            d=min(1-a,discharge_increment2/use_increment2)
        else:
            a=0
            d=0
        print ('a的值为%s,d的值为%s'%(a,d))
        #自发自用增量
        self_use2=a*use_increment2
        #自发充电增量
        self_charge2=0
        #购电自用增量
        buy_use2=0
        #自发自用增量总和
        self_usetotal=self_use2+self_usetotal
        #自发充电增量总和

        self_chargetotal=self_charge2+self_chargetotal
        #购电自用增量总和
        buy_usetotal=buy_use2+buy_usetotal
        print ('自发自用增量为%s,自发充电增量为%s,购电自用增量为%s'%(self_use2,self_charge2,buy_use2))
        radio1(generationValue2,useValue2,buyValue2,chargeValue2,self_usetotal,self_use,self_chargetotal,self_charge,buy_usetotal,buy_use)
    #购电量增量大于并网量增量时，若充电量增量大于或等于放电量增量：发电量增量=a*用电量增量+b*充电量增量，购电量增量=f*充电量增量+g用电量增量
    # generationValue2=6
    # useValue2=4
    # chargeValue2=2
    # buyValue2=3
    #
    # generation_increment2=0.6
    # use_increment2=0.6
    # grid_increment2=0.6
    # buy_increment2=0.8
    # charge_increment2=0.6
    # discharge_increment2=0.4
    #
    if grid_increment2<buy_increment2 and charge_increment2>=discharge_increment2:
        if use_increment2>0:
            a=min(1,generation_increment2/use_increment2)
            g=min(1-a,buy_increment2/use_increment2)
        else:
            a=0
            g=0
        if charge_increment2>0:
            b=min(1,(generation_increment2-a*use_increment2)/charge_increment2)
        else:
            b=0
        print ('a的值为%s,b的值为%s,g的值为%s'%(a,b,g))
        #自发自用增量
        self_use2=a*use_increment2
        #自发充电增量
        self_charge2=b*charge_increment2
        #购电自用增量
        buy_use2=g*use_increment2
        #自发自用增量总和
        self_usetotal=self_use2+self_usetotal
        #自发充电增量总和
        self_chargetotal=self_charge2+self_chargetotal
        #购电自用增量总和
        buy_usetotal=buy_use2+buy_usetotal
        print ('自发自用增量为%s,自发充电增量为%s,购电自用增量为%s'%(self_use2,self_charge2,buy_use2))
        radio1(generationValue2,useValue2,buyValue2,chargeValue2,self_usetotal,self_use,self_chargetotal,self_charge,buy_usetotal,buy_use)
    #购电量增量大于并网量增量时，若放电量增量大于充电量增量：发电量增量=a*用电量增量，放电量增量=d*用电量增量，购电量增量=g用电量增量
    # generationValue2=6
    # useValue2=4
    # chargeValue2=2
    # buyValue2=3
    #
    # generation_increment2=0.6
    # use_increment2=1.0
    # grid_increment2=0.6
    # buy_increment2=0.8
    # charge_increment2=0.4
    # discharge_increment2=0.6
    #
    if grid_increment2<buy_increment2 and charge_increment2<discharge_increment2:
        if use_increment2>0:
            a=min(1,generation_increment2/use_increment2)
            d=min(1-a,discharge_increment2/use_increment2)
            g=min(1-a-d,buy_increment2/use_increment2)
        else:
            a=0
            d=0
            g=0
        print ('a的值为%s,d的值为%s,g的值为%s'%(a,d,g))
        #自发自用增量
        self_use2=a*use_increment2
        #自发充电增量?
        self_charge2=0
        #购电自用增量
        buy_use2=g*use_increment2
        #自发自用增量总和
        self_usetotal=self_use2+self_usetotal
        #自发充电增量总和
        self_chargetotal=self_charge2+self_chargetotal
        #购电自用增量总和
        buy_usetotal=buy_use2+buy_usetotal
        print ('自发自用增量为%s,自发充电增量为%s,购电自用增量为%s'%(self_use2,self_charge2,buy_use2))
        radio1(generationValue2,useValue2,buyValue2,chargeValue2,self_usetotal,self_use,self_chargetotal,self_charge,buy_usetotal,buy_use)
    i+=1
#第一个要考虑的是算法中的，a,b，d,g计算方式,不涉及的不需要计算
#第二个要考虑首条不为0
#是自发自用增量总和，自发充电增量总和,购电自用增量总和，放电自用增量总和