# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/7/14
import os

print(os.system('influxd backup -portable -host dev-server:8088 /home/wlf/storage-test/Backup/InfluxDB'))
