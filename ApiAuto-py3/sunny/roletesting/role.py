#encoding=utf-8
import requests,json
from  src.common.excel_simple import ExcleHelper
data=ExcleHelper(r'D:\xingit\wsy\ApiAuto-py3\config\test.xlsx','role')
cache={}
url=data.get_value('login_username','url')
path1=data.get_value('login_username','path')
headers1=data.get_value('login_username','headers')
base_params1=data.get_value('login_username','params')
path2=data.get_value('get_list','path')
path3=data.get_value('login_username1','path')
headers3=data.get_value('login_username1','headers')
base_params3=data.get_value('login_username1','params')
path4=data.get_value('get_userinfo','path')
path5=data.get_value('modify_role','path')
path6=data.get_value('role_info','path')

payload1=json.loads(base_params1)
head1=json.loads(headers1)
payload3=json.loads(base_params3)
head3=json.loads(headers3)

print (url+path1)
print (url+path2)
print (url+path3)
print (url+path4)
print (url+path5)
print (url+path6)
def login():
    cache={}
    #用户账号登录
    response1=requests.post(url=url+path1,data=payload1,headers=head1)
    result1=json.loads(response1.content)
    access_token=result1['access_token']
    bearer=result1['token_type']
    Authorization1=bearer+" "+access_token
    cache['Authorization1']=Authorization1
    # print (cache)
    #获取商家列表
    Authorization2=cache['Authorization1']
    print ("token为'%s'%Authorization")
    head2={"authorization":"%s"%Authorization2,
             "User-agent":"okhttp/3.9.1"}
    response2=requests.get(url=url+path2,headers=head2)
    result2=json.loads(response2.content)
    print (result2)
    rog_id=result2[0]['org']['id']
    # print (rog_id)
    cache['rog_id']=rog_id
    # print (cache)
    #选择商家登录
    org_id=cache['rog_id']
    payload3['org_id']=org_id
    response3=requests.post(url=url+path3,data=payload3,headers=head3)
    result3=json.loads(response3.content)
    access_token=result3['access_token']
    bearer=result3['token_type']
    Authorization3=bearer+" "+access_token
    # print ('token为%s'%Authorization3)
    cache['Authorization2']=Authorization3
    # print (cache)
    #获取用户信息
    Authorization4=cache['Authorization2']
    head4={"authorization":"%s"%Authorization4,
         "User-agent":"okhttp/3.9.1"}
    response4=requests.get(url=url+path4,headers=head4)
    result4=json.loads(response4.content)
    # print (result4)
    roleid=result4['orgUser']['roleId']
    print (roleid)
    cache['roleid']=roleid
    print (cache)
    return cache
# login()
def role_test():
#修改权限信息
    Authorization5=cache['Authorization2']
    head5={"authorization":"%s"%Authorization5,
           "content-type": "application/json;charset=UTF-8",
            "User-agent":"okhttp/3.9.1"}
    payload5={}
























    #
    # path5=data.get_value('role_info','path')
    # path6=data.get_value('modify_role','path')










