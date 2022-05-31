#!/root/anaconda3/bin/python

# -*- coding: utf-8 -*-
import argparse
from influxdb import DataFrameClient

INFLUX = {}
measurement = ''


def update_tag_name(start_time, end_time, old_tag_name, new_tag_name, delete_old_series):
    client = DataFrameClient(**INFLUX)
    print('成功连接influxdb!')
    print('获取数据中...')
    sql = f"select * from \"{measurement}\" where tag_name='{old_tag_name}' and time >= '{start_time}' and time < " \
          f"'{end_time}' tz('Asia/Shanghai')"
    df = client.query(sql, chunked=True, chunk_size=1000).get(f'{measurement}')
    if df is not None:
        print('成功获取数据!')
        df.drop('tag_name', axis=1, inplace=True)
        if df['value'].dtypes != float:
            df['value'] = df['value'].astype(float)
        client.write_points(df, measurement=measurement, tags={'tag_name': new_tag_name}, batch_size=1000)
        print('修改编码成功！')
    else:
        print('获取数据结果为空！')
    if delete_old_series == 'yes':
        print('删除旧数据（Series）中...')
        client.delete_series(database=INFLUX.get('database'), measurement=measurement, tags={'tag_name': old_tag_name})
        print('删除旧数据（Series）成功！')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', dest='host', default='127.0.0.1', type=str)
    parser.add_argument('--port', dest='port', dnumpyefault=8086, type=int)
    parser.add_argument('--username', dest='username', default='eric', type=str)
    parser.add_argument('--password', dest='password', default='123456', type=str)
    parser.add_argument('--database', dest='database', default='test_x', type=str)
    parser.add_argument('--measurement', dest='measurement', default='ACC_SAMPLE_RESULT', type=str)
    parser.add_argument('--startTime', dest='start_time', required=True, type=str)
    parser.add_argument('--endTime', dest='end_time', required=True, type=str)
    parser.add_argument('--oldTagName', dest='old_tag_name', required=True, type=str)
    parser.add_argument('--newTagName', dest='new_tag_name', required=True, type=str)
    parser.add_argument('--deleteOldSeries', dest='delete_old_series', default='no', type=str, choices=['yes', 'no'])

    parser = parser.parse_args()

    INFLUX = {
        'host': parser.host,
        'port': parser.port,
        'username': parser.username,
        'password': parser.password,
        'database': parser.database
    }
    measurement = parser.measurement
    try:
        update_tag_name(parser.start_time, parser.end_time, parser.old_tag_name, parser.new_tag_name, parser.delete_old_series)
        print('执行成功！')
    except Exception as e:
        print('执行失败：', e)
