# @Author  : WangLingFeng
# @Date    : 2022\\5\\30
import os
import shutil

source = 'C:\\Users\\WANGLINGFENG\\Desktop\\pythontest\\source'
target = 'C:\\Users\\WANGLINGFENG\\Desktop\\pythontest\\target'


# list = os.listdir(source)
# for item in list:
#     from_path = os.path.join(source, item)
#     if os.path.isdir(from_path):
#         print('dir', from_path)
#     else:
#         shutil.copy(from_path, from_path.replace(source, target))


def lsdir(dir):
    contents = os.walk(dir)
    for path, folder, file in contents:
        print('path:', path, '\nfolder:', folder, "\nfile:", file, "\n")


lsdir(source)
