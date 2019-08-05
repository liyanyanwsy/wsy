#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
import random
# import requests as re
import re
profileDir = r'C:\Users\lyy\AppData\Roaming\Mozilla\Firefox\Profiles\11gp24o4.default'
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)
driver=webdriver.Firefox()
driver.implicitly_wait(10)

# #绕过验证码
# driver.get("http://pro.solarman.cn/login/login.do")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@class='close close-ico tra-fast']").click()
# driver.find_element_by_link_text("免费开通").click()
# driver.find_element_by_id("name").send_keys('liyanyan')
# driver.find_element_by_id("email").send_keys('liyanyanwtfwsy@yopmail.com')
# driver.find_element_by_id("password").send_keys('111111')
# driver.find_element_by_id("reg1").click()




#js处理滚动条


##绕过验证码
# driver.get("http://www.cnblogs.com/wanshiyu")
# #添加cookie
# c1={u'domain': u'.cnblogs.com',
#     u'name': u'.CNBlogsCookie',
#     u'value': u'96BDD9A687E6AAB8E8C64C9B1A802CB1CBFB045A71BF519C2246A3FAEEB0F7150D63DDD5E3068A98674176BA44356FEE4C37065C6AE79EB6E68E3A59688023078E2174CDC3473CC34785F96EA2A02CAFD078340EFBCAA423280329182AF8851168637845',
#     u'expiry': 1491887887,
#     u'path': u'/',
#     u'httpOnly': True,
#     u'secure': False
#     }
# c2={u'domain': u'.cnblogs.com',
#     u'name': u'.Cnblogs.AspNetCore.Cookies',
#     u'value': u'CfDJ8FHXRRtkJWRFtU30nh_M9mDXGI8J9_0QDuPnmHbJaKm3hsX86gcqn9fhq0lpUL5aXqzBugChKwH3X4CxX0E7hRYyF_TFfsZo_Crip4qamdMWSDs18CQ5DLk_QwSywR406blclkfML29IT_ijPENZ-Ce0Xq7YdqRzTW3bwyS59KQLPnIOakTIWlPEooFSngg8lCYxEPUFLCqenkzEqCe5zV2fOhLuuM4KSGfXyxDMW9hsyxsk3ZDs1dtv55QhhKrtNkudEhBMyTv7nCkyu6UdAEHd85XxA8tmc9zFI7m6Aw9OiP7SDzLuCKRyK1CbnzbRYg',
#     u'expiry': 1491887887,
#     u'path': u'/',
#     u'httpOnly': True,
#     u'secure': False
#     }
# driver.add_cookie(c1)
# driver.add_cookie(c2)
# time.sleep(3)
# driver.refresh()

















# .CNBlogsCookie=9B574CCCC7AA2CE53B5DDA069F6DC1D820DCF2C3F4EC11FB447BDD8BE67E6457483428998602E98571FE796EFE2AB33C4BB8310DC13C792A2301B5E0CC4E450775BD3B914E5321682EB7D857F5071E01E0743B27E6A144EA04F39D32EA50CEA30ED619CD
# .Cnblogs.AspNetCore.Cookies=CfDJ8FHXRRtkJWRFtU30nh_M9mCBogCIjqgFQpbgoHVU9TPhibjxxqne30ZM7amruV4cgR0WqAUUfKZmV-pF6VNcy1u8Cyhh64xrmdydMXTG4MKTNsnTGUBOe-y8VZeEIwRXpD2CqgSweycZKrGI93eQIlZOawiT0td6o2JJWhNLc-PeGR48rBcVYPTGDai-BM9E-TsOLy27-LYz1A1l1EJCEgmrqIyVTYEPRxOCSd805DDauGxS0udhenS2bE4qqzEsVGkX09IV7QcaoBshXC6xgIYRSstVQz6eyAWmgtnfgeH3
#




# #cookies
# print driver.get_cookies()
# driver.get("http://192.168.1.31/testlink/login.php")
# driver.implicitly_wait(10)
# driver.maximize_window()
# print driver.get_cookies()
# #登录后获取cookies
# driver.find_element_by_id("login").send_keys("liyanyan")
# driver.find_element_by_name("tl_password").send_keys("1")
# driver.find_element_by_name("login_submit").click()
# time.sleep(3)
# print driver.get_cookies()
# # #获取指定name的cookies
# # print driver.get_cookies(name='TESTLINK_USER_AUTH_COOKIE')
#
# #清除指定


# page=driver.page_source
# # print page
# # "非贪婪匹配,re.S('.'匹配字符,包括换行符)"
# url_list=re.findall('href=\"(.*?)\"',page.re.S)
# url_all=[]
# for url in url_list:
#     if "http" in url:
#         print url
#         url_all.append(url)
# print url_all


##获取元素属性
# driver.get("https://www.baidu.com/")
# time.sleep(2)
# # #获取到页面的title
# # title=driver.title
# # print title
# # #获取到元素的文本
# # text=driver.find_element_by_id("setf").text
# # print text
# # #获取到元素的标签
# # tag_name=driver.find_element_by_id("setf").tag_name
# # print tag_name
# # #获取元素的其他属性
# # name=driver.find_element_by_id("setf").get_attribute("target")
# # print name
# # #获取输入框的文本值
# # driver.find_element_by_id("kw").send_keys(123456)
# # value=driver.find_element_by_id("kw").get_attribute("value")
# # print value
# # #获取浏览器名称
# # print driver.name



# #文件上传
# profileDir = r'C:\Users\lyy\AppData\Roaming\Mozilla\Firefox\Profiles\11gp24o4.default'
# profile = webdriver.FirefoxProfile(profileDir)
# driver = webdriver.Firefox(profile)
# driver.implicitly_wait(10)
# driver.get("http://www.cnblogs.com/wanshiyu")
# #点击新随笔
# driver.find_element_by_link_text("新随笔").click()
# time.sleep(3)
# #点击相册
# driver.find_element_by_id("TabGalleries").click()
# #点击管理照片
# driver.find_element_by_link_text("管理照片").click()
# driver.find_element_by_id("AddImages_ImageFile").send_keys(r"C:\Users\lyy\Pictures\5\333333.jpg")
# driver.find_element_by_id("AddImages_lbkAddImage").click()



# ##文本编辑
# #加载浏览器配置好文件
# profileDir = r'C:\Users\lyy\AppData\Roaming\Mozilla\Firefox\Profiles\11gp24o4.default'
# profile = webdriver.FirefoxProfile(profileDir)
# driver = webdriver.Firefox(profile)
# blogurl="http://www.cnblogs.com/"
# wsyblog=blogurl+"wanshiyu"
# driver.get(wsyblog)
# driver.find_element_by_id("blog_nav_newpost").click()
# time.sleep(10)
# edittile=u"selenium2+python自动化-富文本"
# editbody=u"这里是发帖的正文"
# driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(edittile)
# driver.find_element_by_id("Editor_Edit_EditorBody").send_keys(editbody)







# url = "https://passport.cnblogs.com/user/signin"
# driver.get(url)
# headers={"Connection": "keep-alive",
#          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#          "Upgrade-Insecure-Requests": "1",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#          "Cache-Control": "max-age=0",
#          "Accept-Encoding": "gzip, deflate, br",
#          "Accept-Language": "zh-CN,zh;q=0.9",
#          "Cookie": "_ga=GA1.2.1150486742.1531561243; UM_distinctid=1649ce6a356167-0aeb22c1711e5c-5e442e19-100200-1649ce6a3581ea; __gads=ID=2ac08f0ece715090:T=1534495917:S=ALNI_MbVUr5fzn_ZJ94VBF46NVPL16TbhQ; _gid=GA1.2.556537721.1534834087; ASP.NET_SessionId=fyvr4bj42tzlan4r01a4ubjv; SERVERID=34e1ee01aa40e94e2474dffd938824db|1534905425|1534901887"
#          }
# s=re.session()
# r=s.get(url,headers=headers,verify=False)
# print s.cookies
#
# #  添加登录需要的两个cookie
# c = re.cookies.RequestsCookieJar()
# c.set('.CNBlogsCookie', '94A187458E86456A2007FED6C7AD8080F1CEF83B61A62EC390FEF9B4001DF2B6153C6EBC2D16714BAF58BC4121E4916EDF7EECEBF3A2E247C64CA4E6918D1910075B1B28AD2D60B6F0D049373C8F4207A972A9481D6C4F6CAC4EF2912FC6A2C9C43A520F')
# c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8FHXRRtkJWRFtU30nh_M9mCJDLso5RIAJ3VmVbSPLl4p3eez169Ke_-_74GZS5NZq2Pq-OhIm11J6O4xUkPIdBO9Lw_b-bRMs843AQMyaPib49094G4gLUR5rEM35yP1KBd-BKURym_cjvXdJbXjtsZ-dw9YJqxruJuU4wihS9PJqgKhYjj4XHTIp0k6BAJ5v2v-Pa7C60Af_JZILu67ggiU73nmImPMkk6TShnihC0RvPYMEYSwyRHE28iDYzu_bKIzsMBNO_my_N2TCL2zxm0gXDSRRNqYkT0L2hgfSNQg') #
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)
# print s.cookies
# r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)



# # driver=webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.get("http://www.cnblogs.com/yoyoketang/")
# driver.find_element_by_link_text("新随笔").click()
#
# time.sleep(3)
# # 点开编辑器图片
# driver.find_element_by_css_selector("img.mceIcon").click()
# time.sleep(3)
# # 定位所有iframe,取第二个
# iframe = driver.find_elements_by_tag_name('iframe')[1]
# #  切换到iframe上
# driver.switch_to_frame(iframe)
# # 文件路径
# driver.find_element_by_name('file').send_keys(r"D:\test\xuexi\test\14.png")

# t=random.randint(0,9)
# print t
# driver=webdriver.Firefox()
# driver.get("http://www.cnblogs.com/yoyoketang/")




# driver.get("file:///C:/Users/lyy/Desktop/sex.html")
# driver.find_element_by_id("boy").click()
# r=driver.find_element_by_id("boy").is_selected()
# print r
# driver.implicitly_wait(10)
# driver.find_element_by_id("girl").click()
# s=driver.find_element_by_id("girl").is_selected()
# print s
# driver.implicitly_wait(5)
# driver.find_element_by_id("c1").click()
#
# checkboxs=driver.find_elements_by_xpath(".//*[@type='checkbox']")
# for i in checkboxs:
#     i.click()


# driver.implicitly_wait(20)
# mouse=driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(mouse).perform()
# driver.find_element_by_link_text("搜索设置").click()
# s=driver.find_element_by_id("nr")
# Select(s).select_by_value('20')
# Select(s).select_by_visible_text("每页显示10条")

# s=driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='50']").click()
# driver.find_element_by_xpath("//*[@id='nr']/option[2]").click()
# driver.find_element_by_xpath("//select[@id='nr']/option[1]").click()
# driver.switch_to.frame("x-URS-iframe")
# driver.switch_to_frame("x-URS-iframe")
# driver.find_element_by_name("email").send_keys("liyanyan8759@163.com")
# driver.find_element_by_name("password").send_keys("987901")

driver.switch_to.default_content()
# driver.find_element_by_id("kw").send_keys(u"测试部落")
# driver.find_element_by_id("su").click()
# s=driver.find_elements_by_css_selector("h3.t>a")
# # for i in s:
# #     print i.get_attribute("href")
#
# t=random.randint(0,9)
# s[t].click()
# a=s[t].get_attribute("href")
# print a
# driver.get(a)



# driver.get("http://bj.ganji.com/")
# driver.implicitly_wait(10)
# h=driver.current_window_handle
# print h
# driver.find_element_by_link_text(u"工作").click()
# all_h=driver.window_handles
# print all_h
# driver.switch_to.window(all_h[1])
# print driver.title
# driver.close()
# driver.switch_to.window(h)
# print driver.title

# driver.get("https://www.baidu.com/")
# driver.implicitly_wait(10)
#
# mouse=driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(mouse).perform()


# driver.find_element_by_css_selector("#kw").send_keys(u"测试部落")
# driver.find_element_by_css_selector("#kw").send_keys(Keys.ENTER)
# driver.find_element_by_css_selector("#kw").submit()
# driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
# driver.find_element_by_xpath("//*[contains(@id,'kw')]").click()
# driver.find_element_by_css_selector("#kw").send_keys("python")
# driver.find_element_by_css_selector(".s_ipt").send_keys(123)


# driver.find_element_by_xpath("//*[@id=kw]").send_keys("python")"
# driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys("css")
# driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys("java")

# driver.get_screenshot_as_file("")
# driver.set_window_size(540,960)
# time.sleep(5)
# driver.maximize_window()
# driver.refresh()
# driver.get("http://10.42.1.10:3000/")
# time.sleep(5)
# driver.back()
# time.sleep(5)
# driver.forward()
# driver.close()
# driver.quit()