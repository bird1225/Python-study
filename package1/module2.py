# @Author  : 汪凌峰（Eric Wang）
# @Date    : 2022/6/8
with open('../directory/source/1.txt', 'a') as file1:
    file1.write(' hello')
with open('../directory/source/1.txt', 'r') as file2:
    print(file2.read())
