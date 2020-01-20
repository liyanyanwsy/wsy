import requests
import json
cache={}
def login_token():

    url = "https://website.pm.private.igen-tech.com/oauth_s/oauth/token"

    querystring = {"username":"admin","password":"3357f8826655d5ca2abbef75f7f3f111afb01b02492b7dd981a349e0af086ef2","clear_text_pwd":"Rhzl@2014","client_id":"test","grant_type":"password","identity_type":"3"}

    headers = {'Content-Type': "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, headers=headers, params=querystring)

    r=response.text

    data=json.loads(r)

    token_type=data.get('token_type')

    access_token=data.get('access_token')

    refresh_token=data.get('refresh_token')
    # print (token_type)
    # print (access_token)
    # print (refresh_token)
    cache['Authorization']=token_type+' '+access_token
    print (cache)

def login():

    url='https://website.pm.private.igen-tech.com/user_s/acc/org/login-user'
    #tokenKey=json.dumps(login_token()[1])
    #refrshtoken=json.dumps(login_token())
    Authorization=cache['Authorization']
    headers={'Authorization':"%s"%Authorization}
    data={'ts':'1571020967146'}

    response=requests.get(url,data=data,headers=headers)

    a=response.text

    userinfo=json.loads(a)

    print(userinfo)
login_token()
login()
