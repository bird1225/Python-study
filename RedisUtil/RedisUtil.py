# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/7/21
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, password='123456')
r = redis.Redis(connection_pool=pool)
r.set('python:test:1', 123)
# r.flushall()
value = r.get('python:test:1')
if value is None:
    print('key is none')
else:
    print(value)

