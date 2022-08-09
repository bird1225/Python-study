# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/9

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import psycopg2  # 进行PostgreSQL数据库操作


def main():
    baseurl = 'http://movie.douban.com/top250?start='
    savePath = './'
    # 1.爬取网页
    datalist = getData(baseurl)
    saveData(savePath, datalist)


# 爬取网页
def getData(url):
    dataList = []
    return dataList


def saveData(savePath, data):
    print('savePath:{}'.format(savePath))


if __name__ == '__main__':
    main()
