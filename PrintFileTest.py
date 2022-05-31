# @Author  : WangLingFeng
# @Date    : 2022/5/29
import  keyword
fp = open('C:/Users/WANGLINGFENG/Desktop/pythontest/1.txt', 'a+')
print(keyword.kwlist, file=fp)
fp.close()
