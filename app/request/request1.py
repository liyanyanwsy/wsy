# coding:utf-8
import requests
import json as j
import  unittest
import time

url='http://192.168.1.58:18003/v/ap.2.0/user/login?user_id=zedlital@163.com&user_pass=zedl1990&terminate=android&push_sn=c7e00abffee028f5ced1705f5a2d77c8&timezone=8&lan=zh&country=CN'
res = requests.get(url)
result=res.content
print result
result1=j.loads(result)
print type(result)
print type(result1)
print result1['result']

# s=requests.session()
# def login(s,url,payload):
#     headers={"Connection": "keep-alive",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#             "Upgrade-Insecure-Requests": "1",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#             "Cache-Control": "max-age=0",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Accept-Language": "zh-CN,zh;q=0.9",
#             "Cookie": "_ga=GA1.2.1150486742.1531561243; UM_distinctid=1649ce6a356167-0aeb22c1711e5c-5e442e19-100200-1649ce6a3581ea; ASP.NET_SessionId=xvdhuve5rugl0wzqisr5ause; SERVERID=34e1ee01aa40e94e2474dffd938824db|1534232048|1534230068"
#             }
#     r=s.post(url,json=payload,headers=headers,verify=False)
#     result=r.json()
#     print result
#     return result['sucess']
# def save_box(s,url2,title,body_data):
#     body = {"__VIEWSTATE": "",
#             "__VIEWSTATEGENERATOR":"FE27D343",
#             "Editor$Edit$txbTitle":"快乐的人",
#             "Editor$Edit$EditorBody":"<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
#             "Editor$Edit$Advanced$ckbPublished":"on",
#             "Editor$Edit$Advanced$chkDisplayHomePage":"on",
#             "Editor$Edit$Advanced$chkComments":"on",
#             "Editor$Edit$Advanced$chkMainSyndication":"on",
#             "Editor$Edit$Advanced$txbEntryName":"",
#             "Editor$Edit$Advanced$txbExcerpt":"",
#             "Editor$Edit$Advanced$tbEnryPassword":"",
#             "Editor$Edit$lkbDraft":"存为草稿",
#         }
#     r2=s.post(url2,data=body,verify=False)
#     print r2.url
#     return r2.url
# def get_postid(u):
#     import re
#     postid=re.findall(r"postid=(.+?)&",u)
#     print postid
#     if len(postid)<1:
#         return ''
#     else:
#         return postid[0]
# def delete_box(s,url3,postid):
#     json3={"postid":postid}
#     r3=s.post(url3,json=json3,verify=False)
#     print r3.json()
#
# if __name__ == '__main__':
#     url = "https://passport.cnblogs.com/user/signin"
#     payload={
#         "input1":"lrsE5FsoolUzJIRWNPPbWGAtz+w/MIyAYGVRdb+Ra6WaXmJtBU+xSEcTl1N1DIyCdvMCCzeNH033VvzGkRmRMW+M+i9kbtWysJZePQKc1OLpo67VBr85HDTlYPjC6maSup/U2F5HXxHGpI4V9NAoGTQsx1Z5SN38BpJW8gqiEsA=",
#         "input2":"CvQJAcHyzeAx7sBd13/AevpkRBEt2PnoR/nakiV4nHrxSq+0vPRdMPj9PxeufMm3GuWO5LEKSxWmz38w/Qxp/mIVH9hCP5kZyNglnVAEBHwXTCGQnRoszeqXit/xuE0ARaPAROeeTCiIL2/XgHQkXUTFfrQlTt9nMQqCH9S1K7o=",
#         "remember":"True"
#     }
#     s=requests.session()
#     login(s,url,payload)
#     url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
#     u=save_box(s,url2,"标题","正文内容")
#     postid=get_postid(u)
#     url3=""
#     delete_box(s,url3,postid)





# class TEST_Kuaidi(unittest.TestCase):
#     def setUp(self):
#         self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
#         self.s=re.session()
#     def test_zhongtong(self):
#         danhao='63542972711'
#         kd='zhongtong'
#         #url进行参数化
#         self.url="http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao,kd)
#         print self.url
#         #第一步发请求
#         r=self.s.get(self.url,headers=self.headers,verify=False)
#         result=r.json()
#         print result
#         #第二部获取结果
#         print (result['companytype'])
#         data=result["data"]
#         print data
#         print data[]
#         get_result=data[0]['context']
#         print (get_result)
#         #断言：测试结果与期望结果对比
#         self.assertEqual("zhongtong",result['company'])
#         self.assertIn(u"已签收",get_result)
    # def test_tiantian(self):
    #     danhao='1202247993797'
    #     kd='tiantian'
    #     #url进行参数化
    #     self.url="http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao,kd)
    #     print self.url
    #     #第一步发请求
    #     r=self.s.get(self.url,headers=self.headers,verify=False)
    #     result=r.json()
    #     #第二部获取结果
    #     print (result['company'])
    #     data=result["data"]
    #     print data
    #     print (data[0])
    #     get_result=data[0]['context']
    #     print (get_result)
    #     #断言：测试结果与期望结果对比
    #     self.assertEqual(u"天天快递",result['company'])
    #     self.assertIn(u"已签收",get_result)
#
# if __name__=='__main__':
#     unittest.main()



# #启动重定向
# headers={"Connection": "keep-alive",
#          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#          "Upgrade-Insecure-Requests": "1",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#          "Cache-Control": "max-age=0",
#          "Accept-Encoding": "gzip, deflate, br",
#          "Accept-Language": "zh-CN,zh;q=0.9",
#          "Cookie": "_ga=GA1.2.1150486742.1531561243; UM_distinctid=1649ce6a356167-0aeb22c1711e5c-5e442e19-100200-1649ce6a3581ea; ASP.NET_SessionId=xvdhuve5rugl0wzqisr5ause; SERVERID=34e1ee01aa40e94e2474dffd938824db|1534232048|1534230068"
#          }
# s=re.session()
# r=s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1",headers=headers,allow_redirects=True,verify=False)
# new_url=r.headers["location"]
# print new_url
# print r.status_code

##json处理
# url="http://www.kuaidi100.com/query?type=zhongtong&postid=635421972711&temp=0.20714497163703705"
# headers={"Connection": "keep-alive",
#          "Accept": "application/json, text/javascript, */*; q=0.01",
#          "X-Requested-With": "XMLHttpRequest",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#          "Refere": "http://www.kuaidi100.com/?from=openv",
#          "Accept-Encoding": "gzip, deflate",
#          "Accept-Language": "zh-CN,zh;q=0.9",
#          "Cookie": "WWWID=WWW38B8A9E7BE9B35F2EF68C945991A59D4; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1534295873; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1534295888"
#          }
# s=re.session()
# r=s.get(url,headers=headers,verify=False)
# result=r.json()
# # print result
# data=result["data"]
# # print data
# print data[0]
# get_result=data[0]['context']
# print get_result
#
# if u"已在 【海宁长安】 签收,签收人: 本人" in get_result:
#     print "已签收"
# else:
#     print "未签收"
# payload={"userName":"17798736289",
#          "password":"111111",
#          "lan":"True",
#          "domain":"False"
#          }
# print type(payload)
# #转化成json格式
# data_json=j.dumps(payload)
# print type(data_json)
# print data_json

# #绕开验证登录并保持会话操作
# #先打开登录首页，获取部分cookie
# url = "https://passport.cnblogs.com/user/signin"
# headers={"Connection": "keep-alive",
#          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#          "Upgrade-Insecure-Requests": "1",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#          "Cache-Control": "max-age=0",
#          "Accept-Encoding": "gzip, deflate, br",
#          "Accept-Language": "zh-CN,zh;q=0.9",
#          "Cookie": "_ga=GA1.2.1150486742.1531561243; UM_distinctid=1649ce6a356167-0aeb22c1711e5c-5e442e19-100200-1649ce6a3581ea; ASP.NET_SessionId=xvdhuve5rugl0wzqisr5ause; SERVERID=34e1ee01aa40e94e2474dffd938824db|1534232048|1534230068"
#          }
# s=re.session()
# r=s.get(url,headers=headers,verify=False)
# print s.cookies
#
# #  添加登录需要的两个cookie
# c = re.cookies.RequestsCookieJar()
# c.set('.CNBlogsCookie', '94AE83BFEBD98294B5476699D2664002457DD1BFEB7F1B8640CE7AF711A508B0DD2DB67AD37A4A684824281A8ABBADE56990FEF18FCEF4940E1E5E336C34944F70D296E78721A1359535833256F5299AC4CBAB1D4C80CE52B79744BDC6F67836DABEC8FD')
# c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8FHXRRtkJWRFtU30nh_M9mCl_xXU84PuseZz-qkULxCwyHDo8yX79S7y5KVhlYast7gZIDIST9Af36MvooP7XVS8LZk0XVkKAXoJY5zAoRAY7Cf9Lxue7iXvaPVGsLroo9ZSmSNEHGz4VCObOAaf1w-Sdf6kYU5Mu5cC3KdmtbqFfxE55jGiRk9g00HC-SPJ7ve-o7vQLWjX5mLirjXNL2Yc4YLn7SR2YI3GV89xUlXANoVl-5PPTTaveNfyn0MwQ-Dh-wn1otw_lMq9dkHvL7fEckqHxa3VC0PURuKU8JmY') #
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)
# print s.cookies
# #模拟登录博客园，但这只是第一步，一般登录后，还会有其它的操作，如发帖，评论等，这时候如何保持会话呢
# #登录成功后，保存编辑内容
# url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# body = {"__VIEWSTATE": "",
#         "__VIEWSTATEGENERATOR":"FE27D343",
#         "Editor$Edit$txbTitle":"快乐的人",
#         "Editor$Edit$EditorBody":"<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
#         "Editor$Edit$Advanced$ckbPublished":"on",
#         "Editor$Edit$Advanced$chkDisplayHomePage":"on",
#         "Editor$Edit$Advanced$chkComments":"on",
#         "Editor$Edit$Advanced$chkMainSyndication":"on",
#         "Editor$Edit$Advanced$txbEntryName":"",
#         "Editor$Edit$Advanced$txbExcerpt":"",
#         "Editor$Edit$Advanced$tbEnryPassword":"",
#         "Editor$Edit$lkbDraft":"存为草稿",
#         }
# r2=s.post(url2,data=body,verify=False)
# print r2.content





# #https 请求
# r=re.get("https://passport.cnblogs.com/user/signin",verify=False)
# print r.status_code

# payload={"j_userName":"yanyan.li@igen-tech.com",
#          "j_password":"111111",
#          "from":"/",
#          "Jenkins-Crumb":"9d4337c33d83c81f85c3c1b36ac888d4",
#          "json": {"j_username":"yanyan.li@igen-tech.com",
#                   "j_password": "111111",
#                   "remember_me": False,
#                   "from": "/",
#                   "Jenkins-Crumb": "9d4337c33d83c81f85c3c1b36ac888d4"},
#          "Submit":"登录",
#          }
#
# headers={"Connection": "keep-alive",
#          "Content-Length": "357",
#          "Cache-Control": "max-age=0",
#          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#          "Origin": "http://localhost:8080",
#          "Upgrade-Insecure-Requests": "1",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#          "Content-Type": "application/x-www-form-urlencoded",
#          "Referer": "http://localhost:8080/login?from=%2F",
#          "Accept-Encoding": "gzip, deflate, br",
#          "Accept-Language": "zh-CN,zh;q=0.9",
#          "Cookie": "screenResolution=1366x768; JSESSIONID.64833c61=node0gyyrjstg47kn1bm44cnlwg0lj8.node0"
#          }
# url="http://localhost:8080/j_acegi_security_check"
# s=re.session()
# r=s.post(url,headers=headers,data=payload)
# # r=re.post("url",params=payload)
# print r.text
# print r.status_code
# #print r.headers
# print r.content

# payload={"userName":"17798736289",
#          "password":"111111",
#          "lan":"1",
#          "domain":"pro.solarman.cn"
# }
# headers={"Connection": "keep-alive",
#          "Content-Length": "65",
#          "Accept": "*/*",
#          "Origin": "http://pro.solarman.cn",
#          "X-Requested-With": "XMLHttpRequest",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#          "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#          "Referer": "http://pro.solarman.cn/login/login.do",
#          "Accept-Encoding": "gzip, deflate",
#          "Accept-Language": "zh-CN,zh;q=0.9",
#          "Cookie": "gr_user_id=9cd27a51-4a93-492c-8a92-fcc7bd95f23d; autoLogin=on; guideNewPlant=pass; guideReg=pass; language=1; Language=zh_CN; timeOffset=28800000; SHRIOSESSIONID=d505c46d-4af0-4fc6-81d0-b84b0dca2ca1"
# }
# url="http://pro.solarman.cn/login/validateLogin.json"
# s=re.session()
# r=s.post(url,headers=headers,data=payload)
# # r=re.post("url",params=payload)
# print r.text
# print r.status_code
# #print r.headers
# print r.content



# class Web_login(unittest.TestCase):
#     def login(self,username,psw,reme=True):
#         url="http://pro.solarman.cn/login/login.do?lang=1"
#         headers{
#             "Connection": "keep-alive"
#             "Content-Length": "65"
#             "Origin": "http://pro.solarman.cn"
#             "X-Requested-With": "XMLHttpRequest"
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
#             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
#             Referer: http://pro.solarman.cn/login/login.do?lang=1
#             Accept-Encoding: gzip, deflate
#             Accept-Language: zh-CN,zh;q=0.9
#             Cookie: gr_user_id=9cd27a51-4a93-492c-8a92-fcc7bd95f23d; autoLogin=on; guideNewPlant=pass; guideReg=pass; language=1; Language=zh_CN; timeOffset=28800000; SHRIOSESSIONID=967fc043-9de7-4cc5-b78a-1b17af6b6fb1
#         }
#



# print help(unittest)
# #请求博客首页,
# r=re.get('http://www.cnblogs.com/yoyoketang/')
# print r.status_code
# print r.text
#找找看搜索功能,params
# par={"Keywords": "yoyoketang"}
# r=re.get('http://zzk.cnblogs.com/s/blogpost',params=par)
# print r.status_code
# print r.text
# #content
# r=re.get('https://www.baidu.com/')
# print r.url
# print r.encoding
# print r.content
# print r.headers
# print r.cookies

# payload={"yoyo":"hello world",
#          "pythonQQ群":"226296743"}
# #转化成json格式
# data_json=j.dumps(payload)
# r=re.post('http://httpbin.org/post',params=data_json)
# # r=re.post('http://httpbin.org/post',params=payload)
# print (r.text)

# class IntegerArithmeticTestCase(unittest.TestCase):
#     def setUp(self):
#         pass
#     def tearDown(self):
#         pass
#     def testAdd(self):  ## test method names begin 'test*'
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)
#
# if __name__ == '__main__':
#     unittest.main()


# class Test(unittest.TestCase):
#     def setUp(self):
#         print "start!"
#     def tearDown(self):
#         time.sleep(1)
#         print "end!"
#     def test01(self):
#         print "执行测试用例01"
#     def test03(self):
#         print "执行测试用例03"
#     def test02(self):
#         print "执行测试用例02"
#     def addtest(self):
#         print "add方法"
# if __name__ == "__main__":
#     unittest.main()

# class Test(unittest.TestCase):
#     def test01(self):
#         '''判断 a == b '''
#         a = 1
#         b = 1
#         self.assertEqual(a, b)
#     def test02(self):
#         '''判断 a in b '''
#         a = "hello"
#         b = "hello world!"
#         self.assertIn(a, b)
#     def test03(self):
#         '''判断 a is True '''
#         a = True
#         self.assertTrue(a)
#     def test04(self):
#         '''失败案例'''
#         a = "上海-悠悠"
#         b = "yoyo"
#         self.assertEqual(a,b,msg="失败原因:%s !=%s"%(a,b))
#
# if __name__=='__main__':
#     unittest.main()
#

