import json as j

import redis as r

# hostName = '192.168.1.44'
hostName = '192.168.1.53'
# port = 6380
port = 6379
# password = 1234

pool = r.ConnectionPool(host=hostName, port=port)

redis = r.Redis(connection_pool=pool)
# 查询设备缓存,并写入文件
# jsonresult = redis.hget("dv:100671243","_d")
#
# jsonstr = str(j.loads(jsonresult))
#
# with open("C:\\Users\\樊宇雯\\Desktop\\temp.json","a+") as f:
#     for s in jsonstr:
#         f.write(s)

# 查询电站缓存,并写入文件
jsonresult = redis.hget("c.p", "150912")

jsonstr = str(j.loads(jsonresult))

with open("C:\\Users\\lyy\\Desktop\\temp.json", "a+") as f:
    f.writelines(jsonstr)
    print("写出完毕")

# consoleResult = redis.hdel("c,p", "156788")
#
# print(consoleResult)