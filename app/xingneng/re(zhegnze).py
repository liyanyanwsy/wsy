
#encoding:utf-8

import re

it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )
# pattern = re.compile(r'\d+')   # 查找数字
# result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
# # 将匹配的数字乘以 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))
# phone = "2004-959-559 # 这是一个国外电话号码"
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print "电话号码是: ", num
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print "电话号码是 : ", num
# line = "Cats are smarter than dogs";
#
# matchObj = re.match( r'dogs', line, re.M|re.I)
# if matchObj:
#     print "match --> matchObj.group() : ", matchObj.group()
# else:
#     print "No match!!"
#
# searchObj = re.search( r'dogs', line, re.M|re.I)
# if searchObj:
#     print "search --> searchObj.group() : ", searchObj.group()
# else:
#     print "No match!!"
# line="Cats are smarter than dogs"
# searchObj=re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
# if searchObj:
#     print "searchObj.group() : ", searchObj.group()
#     print "searchObj.group(1) : ", searchObj.group(1)
#     print "searchObj.group(2) : ", searchObj.group(2)
# else:
#     print "No match!!"
# line="Cats are smarter than dogs"
# matchObj=re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# if matchObj:
#     print "matchObj.group() : ", matchObj.group()
#     print "matchObj.group(1) : ", matchObj.group(1)
#     print "matchObj.group(2) : ", matchObj.group(2)
# else:
#     print "No match!!"