import json as j
import redis as r
import time
import requests as re

def connect():
    try:
        hostName = '10.42.1.7'
        port = 6379
        password = 123456
        pool = r.ConnectionPool(host=hostName, port=port)
        redis = r.Redis(connection_pool=pool)
        return redis
    except Exception:
        print ("erro")

connect()