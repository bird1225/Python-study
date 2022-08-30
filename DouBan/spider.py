# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/10

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
import psycopg2  # 进行PostgreSQL数据库操作
from PostgreSQL import connector

baseurl = 'http://movie.douban.com/top250?start='


def main():
    savePath = './'
    # 1.爬取网页
    datalist = getData(baseurl)
    saveData(savePath, datalist)


# 请求url
def askURL(url):
    # 模拟请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
    }
    # 构建请求
    request = urllib.request.Request(url, headers=headers)
    html = ''
    try:
        respones = urllib.request.urlopen(request)
        html = respones.read().decode('utf8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


# 创建正则表达式对象，表示规则
# 影片详情连接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片的规则
# re.S让换行符包含在字符中
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 影片名称
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片的相关内容
findBd = re.compile(r'<p class="">(.*)</p>', re.S)


# 爬取网页
def getData(url):
    dataList = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        # 获取html
        html = askURL(url)
        bs = BeautifulSoup(html, 'html.parser')
        for item in bs.find_all('div', class_='item'):
            # print(item)
            # 一部电影的所有信息
            data = []
            item = str(item)
            link = re.findall(findLink, item)
            if len(link) > 0:
                data.append(link[0])
            imgSrc = re.findall(findImgSrc, item)
            if len(imgSrc) > 0:
                data.append(imgSrc[0])
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                othtle = titles[1].replace('/', '')
                data.append(othtle)
            else:
                data.append(titles[0])
                data.append(' ')
            rating = re.findall(findRating, item)
            if len(rating) > 0:
                data.append(rating[0])
            judge = re.findall(findJudge, item)
            if len(judge) > 0:
                data.append(judge[0])
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace('。', "")
                data.append(inq)
            else:
                data.append(' ')
            bd = re.findall(findBd, item)[0]
            if len(bd) > 0:
                bd = re.sub('<br(\s+)?/>(\s+)?', '', bd[0])
                bd = re.sub('/', ' ', bd)
                data.append(bd.strip())
            dataList.append(data)
    return dataList


def saveData(savePath, data):
    # print('savePath:{}'.format(savePath))
    # with open(savePath + 'movie.xlsx', 'a') as m:
    #     workbook = xlwt.Workbook(encoding='utf-8')
    #     worksheet = workbook.add_sheet('movie')
    #     worksheet.write()
    for item in data:
        sql = "insert into movie (link,img,title,rating,judge,inq,bd) values (%s,%s,%s,%s,%s,%s,%s);"
        params = (item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        connector.insert(sql, params)


def test_bs4():
    with open('./豆瓣电影 Top 250.html', encoding='utf-8') as dou:
        html = dou.read()
        bs = BeautifulSoup(html, "html.parser")
        print(bs.find_all(re.compile('a')))


if __name__ == '__main__':
    main()
