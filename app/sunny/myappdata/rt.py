#本来想实现的功能：修改redis的值比对app页面，减少人去查看，结果感觉实现不了，显示的值是客户端控制的。
# encoding:utf-8
import json as j
import redis as r
import time
import requests as re
import jsonpath
import unittest
from appium import webdriver
class Test_base(unittest.TestCase):
    def setUp(self):
        desired_caps={
            'platformName':'Android',
            'platformVersion':'5.1',
            'deviceName':'Y55DJZ9D99999999',
            'appPackage':'com.igen.rrgf',
            'appActivity':'com.igen.rrgf.activity.AdActivity',
            'unicodeKeyboard':True,
            'resetKeyboarf':True,
            'noReset':True,
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        time.sleep(5)
        #使用坐标来定位，默认查看第一个电站
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        print x,y
        self.driver.tap([(0.33*x,0.25*y),(0.65*x,0.3*y)],500)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()



#封装登录函数
def mylogin(user,password):
    #登录接口
    url="http://192.168.1.58:18003/v/ap.2.0/user/login?user_id=%s&user_pass=%s&terminate=android&push_sn=69cb9502a514b6c56341f0e0cc4c17cf&timezone=8&lan=zh&country=CN" %(user,password)
    #保持会话
    # s=re.session()
    r=re.get(url)
    print r.url
    return r.cookies

def inverter_data(username,password,plantid,deviceid):
    s=re.session()
    #使用已登录的cookies
    cookies=mylogin(username,password)
    #获取详情数据
    #目标接口
    url2="http://192.168.1.58:18003/v/ap.2.0/device/doInverterDetail?uid=1&lan=1&plantId=%s&deviceId=%s" %(plantid,deviceid)
    #接口的参数
    r2=s.get(url2,cookies=cookies)
    print r2.url
    b=r2.content
    # print b
    #转化为字典格式
    c=j.loads(b)
    #使用jsonpath提取设备数据
    # # print c
    # #固定数据
    # gudingdata=jsonpath.jsonpath(c,"$..realTimeDataImp")
    #
    # #设备发电数据
    # power_out=jsonpath.jsonpath(c,"$..realTimeDataPower")
    #设备电池数据
    battery=jsonpath.jsonpath(c,"$..realTimeDataBattery")
    print battery[0][0]
    battery_status=battery[0][0]['1ff']

    print battery
    print battery_status

if __name__ == '__main__':
    username='wsy@163.com'
    password='111111'
    plantid='237091'
    deviceid='100680858'
    inverter_data(username,password,plantid,deviceid)