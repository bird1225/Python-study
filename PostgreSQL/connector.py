# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/8
import random

import psycopg2

host = 'localhost'
port = '5433'
user = 'postgres'
password = '123456'
database = 'test'

# 获得连接
conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
# 设置自动提交
conn.autocommit = True
# 获得游标对象
cursor = conn.cursor()


def test():
    # sql语句
    version_sql = 'SELECT VERSION()'

    # 执行语句
    cursor.execute(version_sql)
    # 获取单条数据.
    version = cursor.fetchone()
    # 打印
    print('database version : %s ' % version)
    # 创建数据库
    create_db_sql = 'CREATE DATABASE {}'.format(database)
    print('create_db_sql:', create_db_sql)
    # cursor.execute(create_db_sql)
    # 创建表格
    table_name = 't_b_user'
    create_table_sql = 'CREATE TABLE {} (' \
                       'id bigint NOT NULL,' \
                       'name varchar(255) NOT NULL,' \
                       'age int,' \
                       'PRIMARY KEY(id))'.format(table_name)
    print('create_table_sql:', create_table_sql)
    # cursor.execute(create_table_sql)
    # 插入数据
    insert_sql = "INSERT INTO {} (id, name,age) VALUES(1,'tom',18);".format(table_name)
    # cursor.execute(insert_sql)
    # 查询数据
    select_sql = 'SELECT * FROM {}'.format(table_name)
    cursor.execute(select_sql)
    users = cursor.fetchall()
    print('users:{}'.format(users))
    # 关闭数据库连接
    conn.close()


def insert(sql, params):
    print(sql)
    # 获得连接
    conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
    # 设置自动提交
    conn.autocommit = True
    # 获得游标对象
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.close()


if __name__ == '__main__':
    create_movie = '''CREATE TABLE IF NOT EXISTS movie(
   id serial  NOT NULL,
   link VARCHAR(100),
   img VARCHAR(100),
   title VARCHAR(100),
   rating VARCHAR(100),
   judge VARCHAR(100),
   inq VARCHAR(100),
   bd VARCHAR(100),
   PRIMARY KEY ( id )
)'''
    insert(create_movie)
