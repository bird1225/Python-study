# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/6/8
import sys
import time
import os
import urllib.request

print(sys.getsizeof(45))
print(sys.getsizeof('99'))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('https://www.baidu.com').read())
print(os.open('C:/Users/WANGLINGFENG/Desktop/pythontest/1.txt'),)