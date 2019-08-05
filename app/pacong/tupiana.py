import requests as re
import os
from bs4 import BeautifulSoup

r=re.get("http://m.sohu.com/a/151842313_579014")
a=r.content
soup=BeautifulSoup(a,"html.parser")
images=soup.find_all(class_="content-image")
print images
for i in images:
    jpg_url=i['src']
    jpg_title=i['title']
    print jpg_url
    print jpg_title
