# from urllib import parse
import xlrd
import requests
import json

datafile = 'C:\\Users\\lyy\\Desktop\\data.xlsx'

def getTestData(datafile, sheetname):
    '''
   从excel中获取测试数据
   '''
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    testfile = xlrd.open_workbook(datafile)
    testsheet = testfile.sheet_by_name(sheetname)
    cols = int(testsheet.ncols)
    rows = testsheet.nrows
    host = testsheet.cell(0, 1).value
    method = testsheet.cell(1, 1).value
    lists = []


    for i in range(3, rows):
        dict_params = {}
        dict_params['TestStepID'] = testsheet.cell(i, 1).value
        dict_params['Description'] = testsheet.cell(i, 2).value
        dict_params['METHOD'] = testsheet.cell(1, 1).value
        reqpath = testsheet.cell(i, 3).value
        url = 'https://' + host + reqpath
        dict_params['URL'] = url
        dict_params['DATA'] = testsheet.cell(i, 5).value
        dict_params['ExceptResult'] = testsheet.cell(i, 6).value
        dict_params['headers'] = {'Content-Type': 'application/x-www-form-urlencoded'}
        lists.append(dict_params)
        # lists.insert(i,dict_params)

    return (lists)


t = getTestData(datafile, 'TestScene')
print (t)
# c1=len(t)
# print (c1)
# a=[]
# i=0
# while i <c1:
#     a2=t[i]['ExceptResult']
#     a.append(int(a2))
#     i=i+1
# print (a)



def http_request(req_url, req_data, headers, method):
    global cookie
    if method == 'get':
        response = requests.get(req_url, data=req_data, headers=headers)  # ,cookies=cookie)
    else:
        response = requests.post(req_url, data=req_data, headers=headers)  # ,cookies=cookie)
    if response.cookies != {}:
        cookie = response.cookies
    result = response.text
    # result1=response.status_code
    # return result1
    return response


# print(type(k))
# value_list = k.values()
# print(value_list)
# print(t)
# k=t[0];
testfile = xlrd.open_workbook(datafile)
testsheet = testfile.sheet_by_name('TestScene')
# print(type(k['URL']))
# print(type(k['DATA']))
# print(type(k['headers']))
# print(type(k['METHOD']))

for k in t:
    result = http_request(k['URL'], eval(k['DATA']), k['headers'], k['METHOD'])
    result1=result.status_code
    b=k['ExceptResult']
    if int(result1)==int(b):
        print('pass')
    else:
        print('fail')






