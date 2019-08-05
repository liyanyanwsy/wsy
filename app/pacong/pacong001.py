#coding:utf-8
import requests as re
from bs4 import BeautifulSoup
r=re.get("http://www.cnblogs.com/yoyoketang/")
#请求首页后获取整个html页面
blog=r.content
print blog
#用html.parser解析html
soup=BeautifulSoup(blog,'html.parser')
#获取所有的class属性为dayTitle,返回Tag类

times=soup.find_all(class_='dayTitle')
# for i in times:
#     print i.a.string
titles=soup.find_all(class_='postTitle')
# for j in titles:
#     print j.a.string
descs=soup.find_all(class_='postCon')
# for k in descs:
#     print k.div.contents[0]
for i,j,k in zip(times,titles,descs):
    print i.a.string
    print j.a.string
    print k.div.contents[0]
    print ""






