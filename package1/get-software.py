# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/6/11
import os
import socket
import winreg

# 检测主机名，并将主机名作文检测结果的文件名
file = open('../directory/source/software.txt', 'w')

# 定义检测位置
sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
           r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']

software_name = []
adobe = 'adobe'
for i in sub_key:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
    for j in range(0, winreg.QueryInfoKey(key)[0] - 1):
        try:
            key_name = winreg.EnumKey(key, j)
            key_path = i + '\\' + key_name
            each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
            DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
            DisplayVersion, REG_SZ1 = winreg.QueryValueEx(each_key, 'DisplayVersion')
            Publisher, REG_SZ2 = winreg.QueryValueEx(each_key, 'Publisher')
            InstallDate, REG_SZ3 = winreg.QueryValueEx(each_key, 'InstallDate')
            DisplayName = DisplayName.encode('utf-8')
            software_name.append(DisplayName)
        except WindowsError:
            pass

software_name = list(set(software_name))
software_name = sorted(software_name)

for result in software_name:
    print(result.decode("utf-8"))
    # print(result.decode("gbk"))
    # file.write(str(result) + '\n')
file.close()
