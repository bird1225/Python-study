# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/7/21
import redis

master_host = '192.168.31.88'
master_port = 6380
password = 123456
pool = redis.ConnectionPool(host=master_host, port=master_port, password=password)
r = redis.Redis(connection_pool=pool)
r.set('python:test:4', 123)
# r.flushall()
value = r.get('python:test:1')
if value is None:
    print('key is none')
else:
    print(value)
