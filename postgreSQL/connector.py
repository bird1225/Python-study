# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/8

import psycopg2

host = 'localhost'
port = '5432'
user = 'postgres'
password = '123456'
database = 'test'

# 获得连接
conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
# 设置自动提交
conn.autocommit = True
# 获得游标对象
cursor = conn.cursor()
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
insert_sql = "INSERT INTO {} (id, name,age) VALUES(2,'tom',18);".format(table_name)
cursor.execute(insert_sql)
# 查询数据
# 关闭数据库连接
conn.close()
