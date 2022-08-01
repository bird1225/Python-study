# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/7/31
import urllib
import urllib
import re
import threading
import sys
from time import ctime
import time
import requests
from fake_useragent import UserAgent


def getProxy():
    url = 'https://api.xiaoxiangdaili.com/ip/get?appKey=871015986961469440&appSecret=kVC1uhFS&cnt=&wt=text&method=http&city=&province='
    res = requests.get(url)
    return res.text


def WriteIPadress():
    all_url = []  # 存储IP地址的容器
    # 代理IP的网址
    url = "http://api.proxy.ipidea.io/getProxyIp?num=100&return_type=txt&lb=1&sb=0&flow=1&regions=&protocol=http"
    res = requests.get(url=url)
    all_url = res.text.split("\r\n")
    with open("D:\Desktop\Python\IP.txt", 'w') as f:
        f.write(res.text)
    return all_url


proxy = getProxy()
proxies = WriteIPadress()
# 请求头信息
headers = {
    'Referer': 'http://ykhd.ldjy.fit/addons/vote/player/showplayer14?id=145373',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Content-Length': '16',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'ykhd.ldjy.fit',
    'Origin': 'http://ykhd.ldjy.fit',
    'Proxy-Connection': 'keep-alive ',
    'Referer': 'http://ykhd.ldjy.fit/addons/vote/player/showplayer14?id=145372',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
    'X-Requested-With': 'XMLHttpRequest'
}

# post表单网址
url = "http://ykhd.ldjy.fit/addons/vote/index/vote"
body = {'player_id': '145372'}

for i in range(0, 100):
    proxy = getProxy()
    print(proxy)
    with open('D:\Desktop\Python\ChinaIP.txt','a') as file:
        file.write(proxy)
        file.write('\n')
    for i in range(0, 4):
        print(i + 1)
        r = requests.post(url=url, data=body, headers=headers, proxies={'http': proxy})
        print(r)
        print(r.text)
        time.sleep(5)
    time.sleep(10)


# with open('D:\Desktop\Python\ChinaIP.txt', 'r') as file:
#     proxyList = file.read()
# for proxy in proxyList.split('\n'):
#     print(proxy)
#     r = requests.post(url=url, data=body, headers=headers, proxies={'http': proxy})
#     print(r)
#     print(r.text)
#     time.sleep(2)
