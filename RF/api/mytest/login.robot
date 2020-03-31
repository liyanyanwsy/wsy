*** Settings ***
Library           requests
Library           Collections
Library           HttpLibrary.HTTP
Library           RequestsLibrary
Resource          我的.txt
Resource          Global.txt

*** Test Cases ***
Login001_yc
    [Template]    KwLogin001_yc
    8888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c9    3    412
    \    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c9    3    412
    8888    \    3    412
    888888888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    3    412
    18888888888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    1    412
    8618888888888    \    1    412
    \    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    1    412
    8618888888888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c9    1    412

Login002_nomal
    [Template]    KwLogin002_nomal
    8618888888888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    1    200
    2972049643@qq.com    bcb15f821479b4d5772bd0ca866c00ad5f926e3580720659cc80d39c9d09802a    2    200
    117798736289    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    1    200
    8888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    3    200

List_business
    [Template]    KwList_business
    zh
    #en

Login003_yc
    [Template]    KwLogin003_yc
    8888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c9    3    412

Login004_nomal
    [Template]    KwAuthorization
    8888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    3    200
