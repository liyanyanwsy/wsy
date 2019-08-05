#encoding:utf-8
import json as j
with open(r"C:\Users\lyy\Desktop\sensor.txt", "r") as f:
    s = f.readlines()
    print s
    print type(s)
    a=s[0]
    print a

    # b=j.loads(a)
    # print b






    # c=j.loads(a)
    # print c
    # print type(c)
    # b=a.decode(encoding='UTF-8')
    # print b