# @Author  : WangLingFeng
# @Date    : 2022\\5\\30
import os
import shutil

source = 'C:\\PythonTest\\source'
target = 'C:\\PythonTest\\target'

# list = os.listdir(source)
# for item in list:
#     from_path = os.path.join(source, item)
#     if os.path.isdir(from_path):
#         print('dir', from_path)
#     else:
#         shutil.copy(from_path, from_path.replace(source, target))

#
# def lsdir(dir):
#     contents = os.walk(dir)
#     for path, folder, file in contents:
#         # print('path:', path, '\nfolder:', folder, "\nfile:", file, "\n")
#         for f in file:
#             file_name = path + '/' + f
#             print(file_name)
#             target_name = str(file_name).replace(source, target)
#             print('target', target_name)
#             shutil.copyfile(file_name, target_name)


# lsdir(source)

shutil.copytree(source, target)
