# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/9

import urllib.request
import urllib.parse

data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding='utf-8')
respones = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(respones.read().decode('utf-8'))
