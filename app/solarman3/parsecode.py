#coding=utf-8
import requests as re
import json as j
# import sys
# type = sys.getfilesystemencoding()

#url='http://10.42.6.21:9121/parse/config/get'

#url='http://10.42.2.17:9121/parse/config/get?'

#功能测试环境
# url='http://parse.dev.igen:9121/parse/config/get'
url='http://10.42.6.41:9121/parse/config/get'
a=['01020102BB','01020104BB','01020105BB','0102010125','0102012BE0','01020134E0','0102010CE0','0102010705','01020101B2','0102010505']
b=len(a)
i=0
while i <b:
    c=a[i]
    # print c
    payload={"protocol":"0","parseCode":'%s' %c}
    res=re.post(url,params=payload)
    result=res.content
    print result
    # print type(result)
    i+=1
print '查询结束'

