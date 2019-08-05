#encoding:utf-8
import redis as r
import json as j
hostName = '47.88.4.103'
port = 16379
# hostName = '192.168.1.53'
# port = 6379
pool = r.ConnectionPool(host=hostName, port=port)
redis = r.Redis(connection_pool=pool)
#多个电表求和
def Dbqhgeneration():
    try:
        # dvresult1 = redis.hget("dv:100676105","_d")
        # dvresult2 = redis.hget("dv:100676106","_d")
        # dvresult3 = redis.hget("dv:100676107","_d")
        dvresult1 = redis.hget("dv:101146246","_d")
        dvresult2 = redis.hget("dv:101146271","_d")
        dvresult3 = redis.hget("dv:101146315","_d")
        _d1 = j.loads(dvresult1)
        _d2 = j.loads(dvresult2)
        _d3 = j.loads(dvresult3)
        #CT1、CT2、CT3总正向电能，总反向电能
        a1=float(_d1['2st'])
        b1=float(_d1['2sw'])

        c1=float(_d1['2su'])
        d1=float(_d1['2sx'])

        e1=float(_d1['2sv'])
        f1=float(_d1['2sy'])

        a2=float(_d2['2st'])
        b2=float(_d2['2sw'])

        c2=float(_d2['2su'])
        d2=float(_d2['2sx'])

        e2=float(_d2['2sv'])
        f2=float(_d2['2sy'])


        a3=float(_d3['2st'])
        b3=float(_d3['2sw'])

        c3=float(_d3['2su'])
        d3=float(_d3['2sx'])

        e3=float(_d3['2sv'])
        f3=float(_d3['2sy'])

        #CT1、CT2、CT3有功功率
        g1=float(_d1['1b'])
        h1=float(_d1['1c'])
        i1=float(_d1['1d'])

        g2=float(_d2['1b'])
        h2=float(_d2['1c'])
        i2=float(_d2['1d'])

        g3=float(_d3['1b'])
        h3=float(_d3['1c'])
        i3=float(_d3['1d'])
        # print a1
        # print type(a1)
        # t=float(a1)
        # print t
        # print type(t)
        #首条中CT1、CT2、CT3总正向电能，总反向电能
        # dfresult1 = redis.hget("df:100676105","f")
        # dfresult2 = redis.hget("df:100676106","f")
        # dfresult3 = redis.hget("df:100676107","f")
        dfresult1 = redis.hget("df:101146246","f")
        dfresult2 = redis.hget("df:101146271","f")
        dfresult3 = redis.hget("df:101146315","f")

        _df1 = j.loads(dfresult1)
        _df2 = j.loads(dfresult2)
        _df3 = j.loads(dfresult3)
        #CT1、CT2、CT3总正向电能，总反向电能
        a1df=float(_df1['2st'])
        b1df=float(_df1['2sw'])

        c1df=float(_df1['2su'])
        d1df=float(_df1['2sx'])

        e1df=float(_df1['2sv'])
        f1df=float(_df1['2sy'])

        a2df=float(_df2['2st'])
        b2df=float(_df2['2sw'])

        c2df=float(_df2['2su'])
        d2df=float(_df2['2sx'])

        e2df=float(_df2['2sv'])
        f2df=float(_df2['2sy'])


        a3df=float(_df3['2st'])
        b3df=float(_df3['2sw'])

        c3df=float(_df3['2su'])
        d3df=float(_df3['2sx'])

        e3df=float(_df3['2sv'])
        f3df=float(_df3['2sy'])



        #电表都安装在发电侧
        #累计发电量计算
        total=a1+b1+c1+d1+e1+f1+a2+b2+c2+d2+e2+f2+a3+b3+c3+d3+e3+f3
        print a1,b1,c1,d1,e1,f1,a2,b2,c2,d2,e2,f2,a3,b3,c3,d3,e3,f3
        total1=(total/1000)
        #print '累计发电量为%s' %total1
        # print '累计发电量为%s' %total
        #有功功率计算
        Activepower=g1+h1+i1+g2+h2+i2+g3+h3+i3
        Activepower1=Activepower/1000
        print g1,h1,i1,g2,h2,i2,g3,h3,i3
        # print '有功功率为%s,' %Activepower1

        #当日发电量计算
        CT1Positive1=a1-a1df

        CT1Negative1=b1-b1df

        CT2Positive1=c1-c1df

        CT2Negative1=d1-d1df
        CT3Positive1=e1-e1df
        CT3Negative1=f1-f1df

        CT1Positive2=a2-a2df

        CT1Negative2=b2-b2df

        CT2Positive2=c2-c2df

        CT2Negative2=d2-d2df
        CT3Positive2=e2-e2df
        CT3Negative2=f2-f2df

        CT1Positive3=a3-a3df

        CT1Negative3=b3-b3df

        CT2Positive3=c3-c3df

        CT2Negative3=d3-d3df
        CT3Positive3=e3-e3df
        CT3Negative3=f3-f3df
        print CT1Negative1,CT1Negative2,CT1Negative3,CT1Positive1,CT1Positive2,CT1Positive3,CT2Negative1,CT2Negative2,CT2Negative3,CT2Positive1,CT2Positive2,CT2Positive3,CT3Negative1,CT3Negative2,CT3Negative3,CT3Positive1,CT3Positive2,CT3Positive3
        Dayenergy =CT1Negative1+CT1Negative2+CT1Negative3+CT1Positive1+CT1Positive2+CT1Positive3+CT2Negative1+CT2Negative2+CT2Negative3+CT2Positive1+CT2Positive2+CT2Positive3+CT3Negative1+CT3Negative2+CT3Negative3+CT3Positive1+CT3Positive2+CT3Positive3
        print '有功功率为%s,' %Activepower1
        print '当日发电量为%s' %Dayenergy
        print '累计发电量为%s' %total1
    except Exception,e:
        print e
def Dbqhgeneration1():
    try:
        dvresult1 = redis.hget("dv:100676105","_d")

        _d1 = j.loads(dvresult1)

        #CT1、CT2、CT3总正向电能，总反向电能
        a1=float(_d1['2st'])
        b1=float(_d1['2sw'])

        c1=float(_d1['2su'])
        d1=float(_d1['2sx'])

        e1=float(_d1['2sv'])
        f1=float(_d1['2sy'])


        #CT1、CT2、CT3有功功率
        g1=float(_d1['1b'])
        h1=float(_d1['1c'])
        i1=float(_d1['1d'])

        # print a1
        # print type(a1)
        # t=float(a1)
        # print t
        # print type(t)
        #首条中CT1、CT2、CT3总正向电能，总反向电能
        dfresult1 = redis.hget("df:100676105","f")


        _df1 = j.loads(dfresult1)

        #CT1、CT2、CT3总正向电能，总反向电能
        a1df=float(_df1['2st'])
        b1df=float(_df1['2sw'])

        c1df=float(_df1['2su'])
        d1df=float(_df1['2sx'])

        e1df=float(_df1['2sv'])
        f1df=float(_df1['2sy'])

        #电表都安装在发电侧
        #累计发电量计算
        total=a1+b1+c1+d1+e1+f1
        print a1,b1,c1,d1,e1,f1
        total1=(total/1000)
        #print '累计发电量为%s' %total1
        # print '累计发电量为%s' %total
        #有功功率计算
        Activepower=g1+h1+i1
        Activepower1=Activepower/1000
        print g1,h1,i1
        # print '有功功率为%s,' %Activepower1

        #当日发电量计算
        CT1Positive1=a1-a1df

        CT1Negative1=b1-b1df

        CT2Positive1=c1-c1df

        CT2Negative1=d1-d1df
        CT3Positive1=e1-e1df
        CT3Negative1=f1-f1df


        print CT1Negative1,CT1Positive1,CT2Negative1,CT2Positive1,CT3Negative1,CT3Positive1
        Dayenergy =CT1Negative1+CT1Positive1+CT2Negative1+CT2Positive1+CT3Negative1++CT3Positive1
        print '有功功率为%s,' %Activepower1
        print '当日发电量为%s' %Dayenergy
        print '累计发电量为%s' %total1
    except Exception,e:
        print e
def Dbqhgeneration2():
    try:
        dvresult1 = redis.hget("dv:100676105","_d")
        dvresult2 = redis.hget("dv:100676106","_d")
        _d1 = j.loads(dvresult1)
        _d2 = j.loads(dvresult2)

        #CT1、CT2、CT3总正向电能，总反向电能
        a1=float(_d1['2st'])
        b1=float(_d1['2sw'])

        c1=float(_d1['2su'])
        d1=float(_d1['2sx'])

        e1=float(_d1['2sv'])
        f1=float(_d1['2sy'])

        a2=float(_d2['2st'])
        b2=float(_d2['2sw'])

        c2=float(_d2['2su'])
        d2=float(_d2['2sx'])

        e2=float(_d2['2sv'])
        f2=float(_d2['2sy'])

        #CT1、CT2、CT3有功功率
        g1=float(_d1['1b'])
        h1=float(_d1['1c'])
        i1=float(_d1['1d'])

        g2=float(_d2['1b'])
        h2=float(_d2['1c'])
        i2=float(_d2['1d'])

        # print a1
        # print type(a1)
        # t=float(a1)
        # print t
        # print type(t)
        #首条中CT1、CT2、CT3总正向电能，总反向电能
        dfresult1 = redis.hget("df:100676105","f")
        dfresult2 = redis.hget("df:100676106","f")
        _df1 = j.loads(dfresult1)
        _df2 = j.loads(dfresult2)

        #CT1、CT2、CT3总正向电能，总反向电能
        a1df=float(_df1['2st'])
        b1df=float(_df1['2sw'])

        c1df=float(_df1['2su'])
        d1df=float(_df1['2sx'])

        e1df=float(_df1['2sv'])
        f1df=float(_df1['2sy'])

        a2df=float(_df2['2st'])
        b2df=float(_df2['2sw'])

        c2df=float(_df2['2su'])
        d2df=float(_df2['2sx'])
        e2df=float(_df2['2sv'])
        f2df=float(_df2['2sy'])
        #电表都安装在发电侧
        #累计发电量计算
        total=a1+b1+c1+d1+e1+f1+a2+b2+c2+d2+e2+f2
        print a1,b1,c1,d1,e1,f1,a2,b2,c2,d2,e2,f2
        total1=(total/1000)
        #print '累计发电量为%s' %total1
        # print '累计发电量为%s' %total
        #有功功率计算
        Activepower=g1+h1+i1+g2+h2+i2
        Activepower1=Activepower/1000
        print g1,h1,i1,g2,h2,i2
        # print '有功功率为%s,' %Activepower1

        #当日发电量计算
        CT1Positive1=a1-a1df

        CT1Negative1=b1-b1df

        CT2Positive1=c1-c1df

        CT2Negative1=d1-d1df
        CT3Positive1=e1-e1df
        CT3Negative1=f1-f1df

        CT1Positive2=a2-a2df

        CT1Negative2=b2-b2df

        CT2Positive2=c2-c2df

        CT2Negative2=d2-d2df
        CT3Positive2=e2-e2df
        CT3Negative2=f2-f2df
        print CT1Negative1,CT1Negative2,CT1Positive1,CT1Positive2,CT2Negative1,CT2Negative2,CT2Positive1,CT2Positive2,CT3Negative1,CT3Negative2,CT3Positive1,CT3Positive2,
        Dayenergy =CT1Negative1+CT1Negative2+CT1Positive1+CT1Positive2+CT2Negative1+CT2Negative2+CT2Positive1+CT2Positive2+CT3Negative1+CT3Negative2+CT3Positive1+CT3Positive2

        print '有功功率为%s,' %Activepower1
        print '当日发电量为%s' %Dayenergy
        print '累计发电量为%s' %total1
    except Exception,e:
        print e
#电网侧
def Dbqhgrid():
    #沿着购电方向
    try:
        dvresult1 = redis.hget("dv:100676105","_d")
        dvresult2 = redis.hget("dv:100676106","_d")
        dvresult3 = redis.hget("dv:100676107","_d")
        _d1 = j.loads(dvresult1)
        _d2 = j.loads(dvresult2)
        _d3 = j.loads(dvresult3)
        #CT1、CT2、CT3总正向电能，总反向电能
        a1=float(_d1['2st'])
        b1=float(_d1['2sw'])

        c1=float(_d1['2su'])
        d1=float(_d1['2sx'])

        e1=float(_d1['2sv'])
        f1=float(_d1['2sy'])

        a2=float(_d2['2st'])
        b2=float(_d2['2sw'])

        c2=float(_d2['2su'])
        d2=float(_d2['2sx'])

        e2=float(_d2['2sv'])
        f2=float(_d2['2sy'])


        a3=float(_d3['2st'])
        b3=float(_d3['2sw'])

        c3=float(_d3['2su'])
        d3=float(_d3['2sx'])

        e3=float(_d3['2sv'])
        f3=float(_d3['2sy'])

        #CT1、CT2、CT3有功功率
        g1=float(_d1['1b'])
        h1=float(_d1['1c'])
        i1=float(_d1['1d'])

        g2=float(_d2['1b'])
        h2=float(_d2['1c'])
        i2=float(_d2['1d'])

        g3=float(_d3['1b'])
        h3=float(_d3['1c'])
        i3=float(_d3['1d'])
        # print a1
        # print type(a1)
        # t=float(a1)
        # print t
        # print type(t)
        #首条中CT1、CT2、CT3总正向电能，总反向电能
        dfresult1 = redis.hget("df:100676105","f")
        dfresult2 = redis.hget("df:100676106","f")
        dfresult3 = redis.hget("df:100676107","f")

        _df1 = j.loads(dfresult1)
        _df2 = j.loads(dfresult2)
        _df3 = j.loads(dfresult3)
        #CT1、CT2、CT3总正向电能，总反向电能
        a1df=float(_df1['2st'])
        b1df=float(_df1['2sw'])

        c1df=float(_df1['2su'])
        d1df=float(_df1['2sx'])

        e1df=float(_df1['2sv'])
        f1df=float(_df1['2sy'])

        a2df=float(_df2['2st'])
        b2df=float(_df2['2sw'])

        c2df=float(_df2['2su'])
        d2df=float(_df2['2sx'])

        e2df=float(_df2['2sv'])
        f2df=float(_df2['2sy'])


        a3df=float(_df3['2st'])
        b3df=float(_df3['2sw'])

        c3df=float(_df3['2su'])
        d3df=float(_df3['2sx'])

        e3df=float(_df3['2sv'])
        f3df=float(_df3['2sy'])

        #电表都安装在电网
        #累计购电量计算
        total1=a1+c1+e1+a2+c2+e2+a3+c3+e3
        total2=b1+d1+f1+b2+d2+f2+b3+d3+f3
        #累计并网量计算
        total11=(total1/1000.0)
        total22=(total2/1000.0)
        # print '累计购电量为%s' %total11
        # print '累计并网量为%s' %total22
        #有功功率计算
        Activepower=g1+h1+i1+g2+h2+i2+g3+h3+i3
        print g1,h1,i1,g2,h2,i2,g3,h3,i3
        # print '有功功率为%s,' %Activepower

        #当日发电量计算
        CT1Positive1=a1-a1df

        CT1Negative1=b1-b1df

        CT2Positive1=c1-c1df

        CT2Negative1=d1-d1df
        CT3Positive1=e1-e1df
        CT3Negative1=f1-f1df

        CT1Positive2=a2-a2df

        CT1Negative2=b2-b2df

        CT2Positive2=c2-c2df

        CT2Negative2=d2-d2df
        CT3Positive2=e2-e2df
        CT3Negative2=f2-f2df

        CT1Positive3=a3-a3df

        CT1Negative3=b3-b3df

        CT2Positive3=c3-c3df

        CT2Negative3=d3-d3df
        CT3Positive3=e3-e3df
        CT3Negative3=f3-f3df
        print CT1Negative1,CT1Negative2,CT1Negative3,CT1Positive1,CT1Positive2,CT1Positive3,CT2Negative1,CT2Negative2,CT2Negative3,CT2Positive1,CT2Positive2,CT2Positive3,CT3Negative1,CT3Negative2,CT3Negative3,CT3Positive1,CT3Positive2,CT3Positive3
        Dayenergy1=CT1Positive1+CT1Positive2+CT1Positive3+CT2Positive1+CT2Positive2+CT2Positive3+CT3Positive1+CT3Positive2+CT3Positive3
        Dayenergy2=CT1Negative1+CT1Negative2+CT1Negative3+CT2Negative1+CT2Negative2+CT2Negative3+CT3Negative1+CT3Negative2+CT3Negative3
        print '有功功率为%s' %Activepower
        print '当日并网量为%s' %Dayenergy2
        print '当日购电量为%s' %Dayenergy1

        print '累计购电量为%s' %total11
        print '累计并网量为%s' %total22

    except Exception,e:
        print e
#单个电表求和

def Dbuseage():
    try:
        result1 = redis.hget("dv:100676010","_d")
        _dv1 = j.loads(result1)
        #CT1、CT2、CT3总正向电能，总反向电能
        j1=float(_dv1['2st'])
        k1=float(_dv1['2sw'])

        l1=float(_dv1['2su'])
        m1=float(_dv1['2sx'])

        n1=float(_dv1['2sv'])
        o1=float(_dv1['2sy'])
        #CT1、CT2、CT3有功功率
        p1=float(_dv1['1b'])
        q1=float(_dv1['1c'])
        r1=float(_dv1['1d'])

        #首条中CT1、CT2、CT3总正向电能，总反向电能
        result1df= redis.hget("df:100676010","f")
        _df11 = j.loads(result1df)
        #CT1、CT2、CT3总正向电能，总反向电能
        j1df=float(_df11['2st'])
        k1df=float(_df11['2sw'])

        l1df=float(_df11['2su'])
        m1df=float(_df11['2sx'])

        n1df=float(_df11['2sv'])
        o1df=float(_df11['2sy'])

        #累计用电量计算
        total11=j1+k1+l1+m1+n1+o1
        total22=total11/1000
        print j1,k1,l1,m1,n1,o1
        # print '累计用电量为%s' %total22
        #有功功率计算
        Activepower11=p1+q1+r1
        Activepower22=Activepower11/1000
        print p1,q1,r1
        # print '有功功率为%s,' %Activepower11

        #当日用电量计算
        CT1Positive11=j1-j1df

        CT1Negative11=k1-k1df

        CT2Positive11=l1-l1df

        CT2Negative11=m1-m1df
        CT3Positive11=n1-n1df
        CT3Negative11=o1-o1df

        Dayenergy11 =CT1Negative11+CT1Positive11+CT2Negative11+CT2Positive11+CT3Negative11+CT3Positive11
        print CT1Positive11,CT1Negative11,CT2Positive11,CT2Negative11,CT3Positive11,CT3Negative11
        print '有功功率为%s,' %Activepower22
        print '当日用电量为%s' %Dayenergy11
        print '累计用电量为%s' %total22
    except Exception,e:
        print e
def Dbgeneration():
    try:
        result1 = redis.hget("dv:100676010","_d")
        _dv1 = j.loads(result1)
        #CT1、CT2、CT3总正向电能，总反向电能
        j1=float(_dv1['2st'])
        k1=float(_dv1['2sw'])

        l1=float(_dv1['2su'])
        m1=float(_dv1['2sx'])

        n1=float(_dv1['2sv'])
        o1=float(_dv1['2sy'])
        #CT1、CT2、CT3有功功率
        p1=float(_dv1['1b'])
        q1=float(_dv1['1c'])
        r1=float(_dv1['1d'])

        #首条中CT1、CT2、CT3总正向电能，总反向电能
        result1df= redis.hget("df:100676010","f")
        _df11 = j.loads(result1df)
        #CT1、CT2、CT3总正向电能，总反向电能
        j1df=float(_df11['2st'])
        k1df=float(_df11['2sw'])

        l1df=float(_df11['2su'])
        m1df=float(_df11['2sx'])

        n1df=float(_df11['2sv'])
        o1df=float(_df11['2sy'])

        #累计发电量计算
        total11=j1+k1+l1+m1+n1+o1
        total22=total11/1000
        print j1,k1,l1,m1,n1,o1
        # print '累计发电量为%s' %total22
        #有功功率计算
        Activepower11=p1+q1+r1
        Activepower22=Activepower11/1000
        print p1,q1,r1
        # print '有功功率为%s,' %Activepower11

        #当日发电量计算
        CT1Positive11=j1-j1df

        CT1Negative11=k1-k1df

        CT2Positive11=l1-l1df

        CT2Negative11=m1-m1df
        CT3Positive11=n1-n1df
        CT3Negative11=o1-o1df

        Dayenergy11 =CT1Negative11+CT1Positive11+CT2Negative11+CT2Positive11+CT3Negative11+CT3Positive11
        print CT1Positive11,CT1Negative11,CT2Positive11,CT2Negative11,CT3Positive11,CT3Negative11
        print '有功功率为%s,' %Activepower22
        print '当日发电量为%s' %Dayenergy11
        print '累计发电量为%s' %total22
    except Exception,e:
        print e
#沿着购电方向
def Dbgrid():
    try:
        # result1 = redis.hget("dv:100676010","_d")
        result1 = redis.hget("dv:101106880","_d")
        _dv1 = j.loads(result1)
        #CT1、CT2、CT3总正向电能，总反向电能
        j1=float(_dv1['2st'])
        k1=float(_dv1['2sw'])

        l1=float(_dv1['2su'])
        m1=float(_dv1['2sx'])

        n1=float(_dv1['2sv'])
        o1=float(_dv1['2sy'])
        #CT1、CT2、CT3有功功率
        p1=float(_dv1['1b'])
        q1=float(_dv1['1c'])
        r1=float(_dv1['1d'])

        #首条中CT1、CT2、CT3总正向电能，总反向电能
        result1df= redis.hget("df:101106880","f")
        _df11 = j.loads(result1df)
        #CT1、CT2、CT3总正向电能，总反向电能
        j1df=float(_df11['2st'])
        k1df=float(_df11['2sw'])

        l1df=float(_df11['2su'])
        m1df=float(_df11['2sx'])

        n1df=float(_df11['2sv'])
        o1df=float(_df11['2sy'])
        #
        # #累计并网量计算
        # total11=j1+l1+n1
        # print '累计购电量为%s' %total11
        # #累计购电量计算
        # total22=k1+m1+o1
        # print '累计并网量为%s' %total22

        #有功功率计算

        Activepower11=abs(p1)+abs(q1)+abs(r1)
        print p1,q1,r1
        # print '有功功率为%s,' %Activepower11

        #当日并网量、购电量计算
        CT1Positive11=j1-j1df

        CT1Negative11=k1-k1df

        CT2Positive11=l1-l1df

        CT2Negative11=m1-m1df
        CT3Positive11=n1-n1df
        CT3Negative11=o1-o1df

        Dayenergy11 =CT1Positive11+CT2Positive11+CT3Positive11
        print '有功功率为%s,' %Activepower11
        print '当日购电量为%s' %Dayenergy11
        Dayenergy22=CT1Negative11+CT2Negative11+CT3Negative11
        print '当日并网量为%s' %Dayenergy22

        #累计并网量计算
        total11=j1+l1+n1
        print '累计购电量为%s' %total11
        #累计购电量计算
        total22=k1+m1+o1
        print '累计并网量为%s' %total22
    except Exception,e:
        print e

#沿着并网方向
def Dbgrid1():
    try:
        result1 = redis.hget("dv:100676010","_d")
        _dv1 = j.loads(result1)
        #CT1、CT2、CT3总正向电能，总反向电能
        j1=float(_dv1['2st'])
        k1=float(_dv1['2sw'])

        l1=float(_dv1['2su'])
        m1=float(_dv1['2sx'])

        n1=float(_dv1['2sv'])
        o1=float(_dv1['2sy'])
        #CT1、CT2、CT3有功功率
        p1=float(_dv1['1b'])
        q1=float(_dv1['1c'])
        r1=float(_dv1['1d'])

        #首条中CT1、CT2、CT3总正向电能，总反向电能
        result1df= redis.hget("df:100676010","f")
        _df11 = j.loads(result1df)
        #CT1、CT2、CT3总正向电能，总反向电能
        j1df=float(_df11['2st'])
        k1df=float(_df11['2sw'])

        l1df=float(_df11['2su'])
        m1df=float(_df11['2sx'])

        n1df=float(_df11['2sv'])
        o1df=float(_df11['2sy'])

        #累计并网量计算
        total11=j1+l1+n1
        print '累计并网量为%s' %total11
        #累计购电量计算
        total22=k1+m1+o1
        print '累计购电量为%s' %total22

        #有功功率计算
        Activepower11=abs(p1)+abs(q1)+abs(r1)
        print p1,q1,r1
        print '有功功率为%s,' %Activepower11

        #当日并网量、购电量计算
        CT1Positive11=j1-j1df

        CT1Negative11=k1-k1df

        CT2Positive11=l1-l1df

        CT2Negative11=m1-m1df
        CT3Positive11=n1-n1df
        CT3Negative11=o1-o1df

        Dayenergy11 =CT1Positive11+CT2Positive11+CT3Positive11
        print '当日并网量为%s' %Dayenergy11
        Dayenergy22=CT1Negative11+CT2Negative11+CT3Negative11
        print '当日购电量为%s' %Dayenergy22
    except Exception,e:
        print e

#3个设备，都在发电侧，电表求和
Dbqhgeneration()
#一个设备在发电侧
# Dbgeneration()
# #一个设备在用电测
# Dbuseage()
# # 3个设备，都在电网侧，电表求和
# Dbqhgrid()
#一个设备沿着购电方向
# Dbgrid()

# #三个设备中，统计一个设备
# Dbqhgeneration1()

# #三个设备中，统计两个设备
# Dbqhgeneration2()

# #一个设备沿着并网方向
# Dbgrid1()













