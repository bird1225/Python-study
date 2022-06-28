# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/6/25
import csv
from logging import exception

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


def arr_size(arr, size):
    s = []
    for i in range(0, int(len(arr)) + 1, size):
        c = arr[i:i + size]
        s.append(c)
    newlist = [x for x in s if x]
    return newlist


mars_client.switch_database(WAVE_DATABASE)
eric_client.switch_database(WAVE_DATABASE)
for i in range(0, 100):
    measurement = 'data_vib_wave_' + str(i)
    print(WAVE_DATABASE, '==>', measurement)
    tag_keys = mars_client.query('SHOW tag keys FROM ' + measurement)
    try:
        for tag_key in tag_keys.raw['series'][0]['values']:
            print(tag_key[0])
        field_keys = mars_client.query('SHOW field keys FROM ' + measurement)

        for field_key in field_keys.raw['series'][0]['values']:
            print(field_key[0])
    except Exception as e:
        print(e)

    result = mars_client.query('SELECT * FROM ' + measurement)
    points = result.get_points()
    json_body = []
    for point in points:
        # print(point)
        try:
            json_body.append(
                {"measurement": measurement,  # 数据表的名称
                 "tags": {
                     "code": point['code'],
                     "id": point['id']
                 },
                 "time": point['time'],
                 "fields": {
                     "DasCode": point['DasCode'],
                     "IndexC": point['IndexC'],
                     "IndexEven": point['IndexEven'],
                     "IndexI": point['IndexI'],
                     "IndexK": point['IndexK'],
                     "IndexKur": point['IndexKur'],
                     "IndexL": point['IndexL'],
                     "IndexMax": point['IndexMax'],
                     "IndexMean": point['IndexMean'],
                     "IndexMin": point['IndexMin'],
                     "IndexP": point['IndexP'],
                     "IndexPP": point['IndexPP'],
                     "IndexSK": point['IndexSK'],
                     "IndexXr": point['IndexXr'],
                     "RmsValue": point['RmsValue'],
                     "TimeIndexTag": point['TimeIndexTag'],
                     "WaveDataSrc": point['WaveDataSrc'],
                     "alarm_level": point['alarm_level'],
                     "convert_coef": point['convert_coef'],
                     "data_section": point['data_section'],
                     "desc": point['desc'],
                     "isErrorSignal": point['isErrorSignal'],
                     "quality": point['quality'],
                     "rate": point['rate'],
                     "rpm": point['rpm'],
                     "src": point['src'],
                     "station_code": point['station_code'],
                     "unit": point['unit'],
                     "value": point['value']
                 }
                 }
            )
        except Exception as e:
            print(e)
    arrs = arr_size(json_body, 20000)
    for a in arrs:
        eric_client.write_points(a)

# eric_client.switch_database(WAVE_DATABASE)
# eric_client2.switch_database('mars')
# result = eric_client.query('SELECT * FROM data_vib_wave_20')
# points = result.get_points()
# for item in points:
# print(item)
# eric_client2.write_points(points)
print("Game Over")
