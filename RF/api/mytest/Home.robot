*** Settings ***
Suite Setup
Library           requests
Library           Collections
Library           HttpLibrary.HTTP
Library           RequestsLibrary
Resource          我的.txt
Resource          Global.txt

*** Test Cases ***
获取账号下电站状态统计信息
    [Template]    Kw获取账号下电站状态统计信息
    #{"region":{"level1":null,"level2":null,"level3":null,"level4":null,"level5":null,"nationId":null, "timezone":null},"tagId":null}    200
    ${region}    200

获取账号下电站发电情况统计信息
    [Template]    Kw获取账号下电站发电情况统计信息
    ${region}    200

获取我的关注电站列表
    [Template]    Kw获取我的关注电站列表
    ${region}    200

获取账号下日满发小时排名电站列表
    [Template]    Kw获取账号下电站状态统计信息
