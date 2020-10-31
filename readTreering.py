import pandas as pd
import os

inputPath = r"C:\Users\mozhukun\Desktop\数据（20201013）\落叶松数据\落叶松年轮\克一河"


def mkdir2(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
    else:
        print("---  There is this folder!  ---")


def delYoungTree(path):
    data = pd.read_excel(path)
    age = list(data["age"])
    folderPath, filename = os.path.split(path)
    if age[-1] < 60:
        print("删除数据：%s   age:%s" % (path, age[-1]))
        os.remove(path)
        txtPath = os.path.join(folderPath, "删除数据信息.txt")
        with open(txtPath, "a+") as f:
            str1 = str(path) + "    " + "age:" + str(age[-1])
            f.write(str(str1) + '\n')
    if age[-1] >= 60:
        print("%s  树木年龄为:%s" % (path, age[-1]))


def extractTree(path):
    folderPath, fileName = os.path.split(path)
    path2 = str(folderPath) + "\\新数据(1950-1960)"
    mkdir2(path2)
    data = pd.read_excel(path)
    year = list(data["year"])
    if str(year[-1]) == "2010":
        print(path)
        df = pd.DataFrame(data.tail(61))
        path3 = os.path.join(path2, filename)
        pd.DataFrame(df).to_excel(path3, sheet_name='Sheet1', index=False, header=True)
        print(path3)
        print("*" * 100)


for maindir, subdir, filenames in os.walk(inputPath):
    for filename in filenames:
        path = os.path.join(maindir, filename)
        name, extension = os.path.splitext(filename)
        if extension == ".xlsx":
            # delYoungTree(path)
            extractTree(path)
