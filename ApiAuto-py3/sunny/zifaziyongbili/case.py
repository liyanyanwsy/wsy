#encoding:utf-8
import requests
import json
import time,datetime
import socket
import threading
from src.common.excel_simple import ExcleHelper
data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\storage.xlsx','case')

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
    if generationValue2>0:
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
    generationValue=data.get_value(13524,'generationValue')
    useValue=data.get_value(13524,'useValue')
    gridValue=data.get_value(13524,'gridValue')
    buyValue=data.get_value(13524,'buyValue')
    chargeValue=data.get_value(13524,'chargeValue')
    dischargeValue=data.get_value(13524,'dischargeValue')
    # generationValue=0.09
    # useValue=0.12
    # gridValue=0
    # buyValue=0
    # chargeValue=0
    # dischargeValue=0

    generation_increment=generationValue
    use_increment=useValue
    grid_increment=gridValue
    buy_increment=buyValue
    charge_increment=chargeValue
    discharge_increment=dischargeValue
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
        return[self_use,self_charge,buy_use,generationValue,useValue,gridValue,buyValue,chargeValue,dischargeValue]
    #并网量增量大于或等于购电量增量时，若放电量增量大于充电量增量：发电量增量=a*用电量增量+c*并网量增量，放电量增量=d*用电量增量+e*并网量增量
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
        return[self_use,self_charge,buy_use,generationValue,useValue,gridValue,buyValue,chargeValue,dischargeValue]
    #购电量增量大于并网量增量时，若充电量增量大于或等于放电量增量：发电量增量=a*用电量增量+b*充电量增量，购电量增量=f*充电量增量+g用电量增量

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
        return[self_use,self_charge,buy_use,generationValue,useValue,gridValue,buyValue,chargeValue,dischargeValue]
    #购电量增量大于并网量增量时，若放电量增量大于充电量增量：发电量增量=a*用电量增量，放电量增量=d*用电量增量，购电量增量=g用电量增量

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
        return[self_use,self_charge,buy_use,generationValue,useValue,gridValue,buyValue,chargeValue,dischargeValue]
    # return[self_use,self_charge,buy_use,generationValue,useValue,buyValue,chargeValue]
a=first()
self_use=a[0]
self_charge=a[1]
buy_use=a[2]
# generationValue1=a[3]
# useValue1=a[4]
# gridValue1=a[5]
# buyValue1=a[6]
# chargeValue1=a[7]
# dischargeValue1=a[8]

self_usetotal=0
self_chargetotal=0
buy_usetotal=0

i=0
#模拟288条数据
while i<20:
    generationValue1=data.get_value(13524-i,'generationValue')
    useValue1=data.get_value(13524-i,'useValue')
    gridValue1=data.get_value(13524-i,'gridValue')
    buyValue1=data.get_value(13524-i,'buyValue')
    chargeValue1=data.get_value(13524-i,'chargeValue')
    dischargeValue1=data.get_value(13524-i,'dischargeValue')
    generationValue2=data.get_value(13523-i,'generationValue')
    useValue2=data.get_value(13523-i,'useValue')
    gridValue2=data.get_value(13523-i,'gridValue')
    buyValue2=data.get_value(13523-i,'buyValue')
    chargeValue2=data.get_value(13523-i,'chargeValue')
    dischargeValue2=data.get_value(13523-i,'dischargeValue')

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
