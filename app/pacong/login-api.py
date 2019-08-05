#coding:utf-8
import requests as re
import json
import jsonpath

class Data():
    def __int__(self,s):
        self.s=s
    #封装登录函数

    def mylogin(self):
        #登录接口
        url="http://pro.solarman.cn/login/validateLogin.json"
        #请求头
        headers={
            "Connection": "keep-alive",
            "host": "pro.solarman.cn",
            "Content-Length":"76",
            "Accept": "*/*",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://pro.solarman.cn/login/login.do?lang=1",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "gr_user_id=9cd27a51-4a93-492c-8a92-fcc7bd95f23d; autoLogin=on; guideNewPlant=pass; guideReg=pass; language=1; Language=zh_CN; timeOffset=28800000; JSESSIONID=eac44a79-7c20-458a-a067-a27b0bd6d5ea"
            }
        #登录参数
        data={"userName":"zedlital@gmail.com",
            "password":"12345678",
            "lan":"1",
            "domain":"pro.solarman.cn",
            }
        #保持会话
        # s=re.session()
        r=re.post(url,headers=headers,data=data,verify=False)
        print r.url
        return r.cookies

# s=re.session()
# #使用已登录的cookies
# cookies=mylogin()
# #获取电站详情数据
# #目标接口
# url2="http://pro.solarman.cn/epc/plantDetail/showPlantDetailAjax.json"
# #接口的参数
# data2={"plantId":"47674"}
# r2=s.post(url2,data=data2,cookies=cookies)
# print r2.url
# b=r2.content
# #转化为字典格式
# c=json.loads(b)
# #使用jsonpath提取电站数据
# #f=jsonpath.jsonpath(c,"$..plantData")
# f=jsonpath.jsonpath(c,"$..energyBuyMonth")
# print f
#
# #获取设备详情数据
# url3="http://pro.solarman.cn/device/inverter/goDetailAjax.json"
# data3={"deviceId":"100551846"}
# r3=s.post(url3,data=data3,cookies=cookies)
# print r3.url
# h=r3.content
# # print h
# i=json.loads(h)
# j=jsonpath.jsonpath(i,"$..realTimeDataBattery")
# print j

#直接通过字典提取电站数据
# d=c['result']
# e=d['plantAllWapper']
# f=e['plantData']
# print f






# print type(f)
# soup=BeautifulSoup(b,"html.parser")
# # print soup.prettify()
# print type(soup)
# url2="http://pro.solarman.cn/epc/plantDetail/showPlantDetailAjax.json"
# #接口的参数
# data2={"plantId":"47674"}
# r2=s.post(url2,data=data2,cookies=cookies)
# print r2.url
# b=r2.content
# print b
# soup=BeautifulSoup(b,"html.parser")
# # print soup.prettify()
# print type(soup)
# tag=soup.title
# print type(tag)
# string=tag.string
# print type(string)



# driver=webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.get("http://pro.solarman.cn/login/login.do")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@class='close close-ico tra-fast']").click()
# driver.find_element_by_id("userName").send_keys("zedlital@gmail.com")
# driver.find_element_by_id("password").send_keys("12345678")
# driver.find_element_by_id("login").click()
# time.sleep(20)

# url="http://pro.solarman.cn/login/validateLogin.json"
# url="http://pro.solarman.cn/index/setIndex.do?type=24&param1=47674"
# url="http://pro.solarman.cn/epc/plantDetail/showPlantDetailAjax.json "
# headers={"Connection": "keep-alive",
#          "host": "pro.solarman.cn",
#          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#          "Upgrade-Insecure-Requests": "1",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#          "Referer": "http://www.solarman.cn/",
#          "Accept-Encoding": "gzip, deflate",
#          "Accept-Language": "zh-CN,zh;q=0.9",
#          "Cookie": "gr_user_id=9cd27a51-4a93-492c-8a92-fcc7bd95f23d; autoLogin=on; guideNewPlant=pass; guideReg=pass; gr_session_id_a52752511891058f=eb0ae4b6-7213-406d-b7c9-91ad4757d1cb; gr_session_id_a52752511891058f_eb0ae4b6-7213-406d-b7c9-91ad4757d1cb=false"
#         }



# headers={"Connection": "keep-alive",
#          "Origin": "pro.solarman.cn",
#          "Content-Length":"76",
#          "X-Requested-With":"XMLHttpRequest",
#          "Accept": "*/*",
#          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#          "Referer": "http://pro.solarman.cn/login/login.do?lang=1",
#          "Accept-Encoding": "gzip, deflate",
#          "Accept-Language": "zh-CN,zh;q=0.9",
#          "Cookie": "gr_user_id=9cd27a51-4a93-492c-8a92-fcc7bd95f23d; autoLogin=on; guideNewPlant=pass; guideReg=pass; gr_session_id_a52752511891058f=eb0ae4b6-7213-406d-b7c9-91ad4757d1cb; gr_session_id_a52752511891058f_eb0ae4b6-7213-406d-b7c9-91ad4757d1cb=true; JSESSIONID=83622377-573f-497c-a6e7-910d14083a0c; language=1; Language=zh_CN"
#         }
# data={"userName":"zedlital@gmail.com",
#       "password":"12345678",
#       "lan":"1",
#       "domain":"pro.solarman.cn",
#       }
# # s=re.session()
# r=re.post(url,headers=headers,data=data)
# print r.url
# print r.content

# url2="http://pro.solarman.cn/epc/plantDetail/showPlantDetailAjax.json"
# data2={"plantId":"47674"}
# r2=s.post(url2,headers=headers,data2=data2)
# print r2.url
# print r2.content

# r2=s.get("http://pro.solarman.cn/index/setIndex.do?type=24&param1=47674")
# print r2.url
# print r2.content