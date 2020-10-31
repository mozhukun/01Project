import re
import pandas as pd
import numpy as np

np.set_printoptions(suppress=True)

widthList = []
nameyearList = []
allNameList = []
lineList = []

openExcel = r"E:\test2\txt\阿里河.txt"

writeExcel = r'E:\test2\alh01.xlsx'
with open(openExcel, "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        treeNumber = line[0:6]
        if treeNumber == 'alh01':
            line = line.split()
            widthLine = line[1:]
            print(widthList)
            for i in widthLine:
                widthList.append(i)
            nameyear = line[0:1]
            for i in nameyear:
                nameyearList.append(i)
id = ['1'] * len(widthList)
a = nameyearList[0]
print(a)
firstYear = a[-4:]
yearList = []
print(firstYear)
for year in range(int(firstYear), int(firstYear) + len(widthList)):
    yearList.append(str(year))
print(yearList)
print(len(yearList))
print(widthList)
print(len(widthList))

ageList = []
for i in range(1, 1 + len(widthList)):
    ageList.append(i)
R = []
sum = 0
print('*' * 100)
for i in widthList:
    print(i)
    sum = sum + float(int(i))
    R.append(sum / 10000)
print(widthList)
print('R: ', R)
R2 = R[0:len(R) - 1]
R2.insert(0, 0)
print('R2:', R2)

v = list(map(lambda x: 3.14 * (x[0] * x[0] - x[1] * x[1]), zip(R, R2)))
BAI = np.array(v)

data = {'ID': id, 'year': yearList, 'age': ageList, 'width': widthList, 'R(cm)': R, 'BAI(cm2)': BAI}
df = pd.DataFrame(data)
pd.DataFrame(df).to_excel(writeExcel, sheet_name='Sheet1', index=False, header=True)

print('id:', len(id))
print('year:', len(yearList))
print('age:', len(ageList))
print('width:', len(widthList))
