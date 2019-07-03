# 这是一个修改所有js文件名为tsx文件名的方法，
# 升级js项目为TS项目时遇到的一个需求

import os

# 列出当前目录下所有的文件
files = os.listdir('.')
print(files, 'files')


def allfile(basepath):
    # 循环目录下的每一个元素（目录或文件）
    for item in os.listdir(basepath):
        # 路径拼接：要查询目录 + 第一级目录/文件
        path = os.path.join(basepath, item)
        if os.path.isfile(path):
            # 判断：若果为文件，直接输出path
            # print(path)
            portion = os.path.splitext(path)
            print(portion, 'portion')
            if portion[1] == ".js":
                # 重新组合文件名和后缀名
                newname = portion[0] + ".tsx"
                os.rename(path, newname)
        else:
            allfile(path)  # 如果仍是是目录，递归调用当前函数


# 获取当前路径
path = os.getcwd()
allfile(path)
