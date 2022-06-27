# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/6/25
import csv
from influxdb import InfluxDBClient
import os
import json
import time
import datetime

ALI_IP = '120.25.208.163'
ERIC_IP = 'localhost'
INFLUXDB_PORT = 8086
ALI_USERNAME = 'zeda'
ALI_PASSWORD = '@q1w2e3r4'
ERIC_USERNAME = 'eric'
ERIC_PASSWORD = '@ericinfluxdb'
WAVE_DATABASE = 'mars_data_wave_index'
# 阿里云Mars客户端
mars_client = InfluxDBClient(ALI_IP, INFLUXDB_PORT, ALI_USERNAME, ALI_PASSWORD)
# Eric客户端
eric_client = InfluxDBClient(ERIC_IP, INFLUXDB_PORT, ERIC_USERNAME, ERIC_PASSWORD)
eric_client2 = InfluxDBClient(ERIC_IP, INFLUXDB_PORT, ERIC_USERNAME, ERIC_PASSWORD)
# 获取所有database
# print('mars-databases', mars_client.get_list_database())
# 选择数据库
# mars_client.switch_database('mars_data_wave_index')
# 获取所有measurement
# print('mars-measurements', mars_client.get_list_measurements())
# result = mars_client.query('SELECT * FROM data_vib_wave_20')
# items = list(result.get_points())

'''
查看数据库记录条数
'''


def show_count(influxdb_client, measurement):
    result = influxdb_client.query('SELECT count(*) FROM ' + measurement)
    # print(measurement, ' count==> ', dir(result))
    points = result.get_points()
    for item in points:
        print(item[u'count_value'])
        with open('./InfluxDB-Count.txt', 'a') as count_file:
            count_file.write(measurement + ' ' + str(item[u'count_value']))
            count_file.write('\n')

def show_databases(influxdb_client):
    pass
def create_database(influxdb_client, database):
    influxdb_client.create_database(database)


def show_mars_data_wave_index(influxdb_client):
    for i in range(0, 100):
        measurement = 'data_vib_wave_' + str(i)
        show_count(mars_client, measurement)


def get_points(influxdb_client, database, measurement):
    influxdb_client.switch_database(database)
    result = eric_client.query('SELECT * FROM ' + str(measurement))
    points = result.get_points()
    return points

eric_client.switch_database(WAVE_DATABASE)
eric_client2.switch_database('mars')
result = eric_client.query('SELECT * FROM data_vib_wave_20')
points = result.get_points()
for item in points:
    print(item)
# eric_client2.write_points(points)
print("Game Over")
