*** Settings ***
Library           requests
Library           Collections
Library           HttpLibrary.HTTP
Library           RequestsLibrary
Resource          02-UserKeyword

*** Test Cases ***
Login_001
    [Template]    Login_001
    8888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    3
    18888888888    8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92    1

list

login_002
